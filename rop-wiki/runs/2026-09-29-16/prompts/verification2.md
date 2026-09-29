(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-29-16
- date: 2026-09-29
- run_type: area_deep_dive (영역 심화)
- 대상: 64. 상업 시설 (Q. 현장 유형별 적용)
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

### runs/2026-09-29-16/target.json

```json
{
  "run_id": "2026-09-29-16",
  "date": "2026-09-29",
  "weekday": "Tue",
  "run_number": 108,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 64,
    "area_name": "64. 상업 시설",
    "category": "Q. 현장 유형별 적용",
    "category_letter": "Q"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=64"
}
```

### runs/2026-09-29-16/research.json

```json
{
  "run_id": "2026-09-29-16",
  "date": "2026-09-29",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 64,
    "area_name": "64. 상업 시설",
    "category": "Q. 현장 유형별 적용"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 다중 운행 차량 경로 문제·로봇친화형 건축물 인증·서비스 삼자 관계 용어 없음(승강기 어댑터·플릿 어댑터·오픈 RMF·서비스형 로봇은 용어집에 이미 있음)",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 호텔 객실 배송(국내 호텔·일본 호텔), 식당 서빙(국내 서빙로봇 보급·노르웨이·유럽 식당), 매장·쇼핑몰 안내·청소(쇼핑몰 안내 로봇·Sam's Club·국내 상업시설 청소로봇), 실패 사례(헨나 호텔)와 여섯 항목 정리 없음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 승강기 연동 방식(버튼 조작 팔·객실 전화 연동·클라우드 API), 다층 배송 경로 계획, 테이블오더·POS 연동, 식당 도입 5단계, 반자율 원격 운영 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — KS 로봇 엘리베이터 탑승 안전 요구사항, 로봇친화형 건축물 인증, Open-RMF 위치 없음",
    "섹션 8. 대표 연구와 자료 비어 있음 — 호텔 경로 계획 논문, 호텔 관리자 인식 연구, 식당 서비스 삼자 연구, 식당 도입 사례 연구, 쇼핑몰 커뮤니케이션 로봇 현장 시험, 한국노동연구원 음식업 로봇 보고서 없음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 0건, 정정 요청 없음",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "손님이 있는 영업 시간에 호텔·식당·매장의 로봇을 어떻게 운영할 것인가? [분류원문]",
    "호텔 객실 배송에서 로봇은 승강기를 어떻게 타고(버튼 조작·객실 전화 연동·승강기 API), 손님과 승강기를 함께 쓰는 혼잡 시간은 배송 계획에 어떤 제약을 주는가? (섹션 5·6 겨냥, 현장 유형 상업 시설 명시, 한국 자료 우선)",
    "식당 서빙로봇은 국내에 얼마나 보급됐으며, 주문 시스템(테이블오더·POS)과의 연동, 매장 구조 요건, 직원과의 역할 분담, 작업장 안전은 어떻게 나타나는가? (섹션 3·5·6 겨냥)",
    "매장·쇼핑몰의 안내·청소·재고 스캔 로봇은 어떤 방식으로 운영되며 고객이 있는 공간에서 어떤 제약과 사람 개입이 필요한가? (섹션 5·6·8 겨냥)",
    "상업 시설 로봇 도입의 실패·예외 사례와 운영자(호텔 관리자·식당 직원)의 인식은 무엇을 보여 주는가? (섹션 3·8 겨냥)",
    "상업 시설 로봇이 건물을 이동하는 데 관련된 표준·인증(KS 로봇 엘리베이터 탑승, 로봇친화형 건축물 인증)과 이기종 로봇 미들웨어(Open-RMF)는 무엇을 규정·제공하는가? (섹션 7 겨냥)",
    "상업 시설에서 ROP 가 직접 맡을 것(요청 수신·이기종 배정·승강기 예약·혼잡 시간 회피·완료 반환)과 객실 관리 시스템·POS·승강기 제어·로봇 자체 기능에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "Han·Ding·Liu·Meng(Sensors, 2025-03-13)은 다층 호텔의 로봇 객실 배송을 승강기를 암묵적 경유지로 두는 다중 운행 차량 경로 문제(MTVRP)로 모델링하고 적응형 대규모 이웃 탐색(ALNS)으로 풀어, 중국 호텔(3개 층 67실) 배치 자료 실험에서 승강기 운행 시간이 40초에서 100초로 늘면 배송 시간이 거의 두 배가 되고 로봇이 5대를 넘으면 추가 로봇의 한계 이익이 크게 줄어든다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-103"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "실험 조건: 고객 노드 10~60, 로봇 1~8대(적재 12단위), 승강기 운행 40~100초. 60노드에서 ALNS 14.15초 대 Gurobi 18,000초 이상, 소규모(10~20노드)는 Gurobi 해와 일치.",
      "as_of": "2025-03-13",
      "site_type": "상업 시설",
      "flow_item": "제약"
    },
    {
      "id": "f2",
      "claim": "같은 논문은 호텔 승강기 운행 시간이 이용 패턴에 따라 달라지므로 아침 식사·체크아웃처럼 승강기 이용이 크게 늘어나는 시간대를 배송 계획에 고려하고, 혼잡 시간에는 단방향 승강기 운행 같은 전략으로 병목을 줄일 것을 제안한다.",
      "tag": "사실",
      "source_ids": [
        "ref-103"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "논문은 \"peak periods such as breakfast or check-out times, when elevator usage increases substantially\" 를 고려해야 한다고 적고 단방향 승강기 운행을 완화책으로 든다.",
      "as_of": "2025-03-13",
      "site_type": "상업 시설",
      "flow_item": "제약"
    },
    {
      "id": "f3",
      "claim": "지디넷코리아(2022-05-03)에 따르면 국내 호텔에는 로봇팔로 승강기 버튼을 직접 눌러 층간 이동하는 로보티즈 ‘집개미’(명동 헨나호텔·코트야드 메리어트 타임스퀘어), 객실 호출에 따라 순차 방문하는 LG전자 ‘클로이 서브봇’(광명 테이크호텔, 최대 15kg; 수원 바이 메리어트), 객실 전화 시스템과 연동해 호출하는 현대로보틱스·KT ‘N봇’(노보텔 앰배서더 동대문), 안내·도슨트·보안 순찰을 하는 LG전자 ‘클로이 가이드봇’(롯데월드호텔), 222nm 자외선 방역로봇(KT, 강남 안다즈호텔)이 도입됐다.",
      "tag": "사실",
      "source_ids": [
        "ref-952"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "기사는 호텔별 로봇·제조사·기능·호출 방식을 나열하고, 로봇들이 AI 로 건물 구조를 매핑해 자율주행하며 라이다·3D 카메라로 장애물을 회피한다고 적는다. 성과 수치·한계는 제시하지 않는다.",
      "as_of": "2022-05-03",
      "site_type": "상업 시설",
      "flow_item": "수행 자원"
    },
    {
      "id": "f4",
      "claim": "오티스는 자사 클라우드 기반 API 인 Otis Integrated Dispatch(OID)가 API 를 쓸 수 있는 어느 브랜드의 로봇과도 승강기 군(그룹) 단위로 연동되며, 오사카 호텔 케이한 유니버설 타워에서 2022-12 부터 AIM Technologies 의 배송 로봇이 승강기를 스스로 호출·탑승·층 선택해 24시간 객실 배송을 하고 야간에 최대 60건의 배송 요청을 처리한다고 주장한다.",
      "tag": "추정",
      "source_ids": [
        "ref-958"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: OID 는 1990년대 이후 설치된 오티스 상업용 승강기 대부분과 호환된다고 설명하며, 로봇과 승객이 승강기를 함께 쓸 때의 우선순위·안전 규칙은 명시하지 않는다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-29",
      "site_type": "상업 시설",
      "flow_item": "수행 자원",
      "vendor_claim": true
    },
    {
      "id": "f5",
      "claim": "서울경제(2025-04-02)에 따르면 경기 화성 동탄의 상업시설 ‘레이크 꼬모’는 라이노스의 AI 청소로봇 ‘휠리 J40’을 도입해 클라우드 기반 승강기 관리 솔루션 rEMS 로 로봇이 전 층을 스스로 오가게 했으며, 운영사 우미에스테이트(우미건설 자산관리회사)는 이를 상업 공간 운영 모델로 확대하겠다고 밝혔다.",
      "tag": "사실",
      "source_ids": [
        "ref-964"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "로봇은 오염 감지·작업 강도 조절, 물 교환·오수 배수·물걸레 세척·건조를 스스로 한다고 기사에 적혀 있으며, 영업시간 중·후 어느 시간대에 청소하는지는 명시되지 않았다.",
      "as_of": "2025-04-02",
      "site_type": "상업 시설",
      "flow_item": "수행 자원"
    },
    {
      "id": "f6",
      "claim": "확인한 자료를 종합하면 상업 시설 로봇의 승강기 이용 방식은 (1) 로봇팔로 승강기 버튼을 직접 누르는 방식(f3), (2) 제조사 클라우드 API 로 승강기를 호출하는 방식(f4, 벤더 주장), (3) 별도 승강기 관리 솔루션을 거치는 방식(f5)으로 나뉘며, 방식마다 승강기 호출 권한·손님과의 공유 규칙을 누가 정하는지가 달라진다.",
      "tag": "추정",
      "source_ids": [
        "ref-952",
        "ref-958",
        "ref-964"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "집개미의 로봇팔 버튼 조작(ref-952), 오티스 OID 클라우드 API(ref-958, 벤더 문서), 레이크 꼬모의 rEMS(ref-964)를 비교한 종합이며, 방식별 성능 비교 자료는 확인하지 못했다.",
      "as_of": "2026-09-29",
      "site_type": "상업 시설",
      "flow_item": "제약"
    },
    {
      "id": "f7",
      "claim": "Retail Dive(2022-02-01)에 따르면 Sam's Club 은 미국 약 600개 매장에서 이미 운영하던 자율 바닥 청소기(Tennant 제조, Brain Corp BrainOS 기반)에 재고 스캔 타워를 달아 바닥 청소와 재고 스캔을 한 로봇으로 수행하게 했고, 로봇이 모은 가격 정확도·재고 수준·상품 진열 위치 정보를 매장 관리자에게 전달한다.",
      "tag": "사실",
      "source_ids": [
        "ref-953"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Brain Corp 의 재고 스캔 기술 첫 상용 적용이자 최대 규모 배치로 소개된다. 로봇이 영업시간 중·후 어느 시간대에 움직이는지와 생산성 수치는 기사에 없다.",
      "as_of": "2022-02-01",
      "site_type": "상업 시설",
      "flow_item": "작업 대상"
    },
    {
      "id": "f8",
      "claim": "Kanda·Shiomi·Miyashita·Ishiguro·Hagita(IEEE Transactions on Robotics 26(5), 2010)는 쇼핑몰에서 쇼핑 정보 제공·길 안내·친밀감 형성을 하는 커뮤니케이션 로봇을 개발해 25일간 현장 시험으로 2,642회의 상호작용을 모았으며, 소음 속 음성 인식과 예상치 못한 지식 요구를 풀기 위해 바닥 센서·RFID 로 사람을 감지·식별하고 일부를 원격 조작자가 맡는 네트워크 로봇 시스템(반자율) 방식을 택했다.",
      "tag": "사실",
      "source_ids": [
        "ref-954"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 결과의 초록 요약 기준: 로봇의 부족한 감지·지식을 곳곳의 센서와 사람 조작자가 보완하며, 음성 인식의 어려움을 피하려고 부분 원격 조작했다. 출판사 페이지(403)와 초록 원문은 열지 못했다.",
      "as_of": "2010-10",
      "site_type": "상업 시설",
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f9",
      "claim": "Ivanov·Seyitoğlu·Markova(Information Technology & Tourism, 2020)는 불가리아 호텔 관리자(설문 79명, 면접 20명)를 조사해 관리자들이 공용 공간 청소·세탁물 배송·결제 처리 같은 반복적이고 지저분한 업무를 로봇에 맞는 일로 보는 반면 손님 감정 이해·프로그램 밖 특별 요청 처리 능력은 낮게 평가하며, 응답자 약 63%가 로봇 도입 의향이 없고 1년 안 도입 계획은 3.8%이며 비용·시설 개조·유지보수·서비스 품질 저하를 장벽으로 든다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-955"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "자료 수집 2018-12~2019-04, 수렴적 혼합 방법. 다국어 정보 제공 능력 평균 3.99/5, 감정 이해 2.30/5, 특별 요청 처리 2.08/5.",
      "as_of": "2020-09",
      "site_type": "상업 시설",
      "flow_item": "예외·성과"
    },
    {
      "id": "f10",
      "claim": "지디넷코리아(2024-07-30)에 따르면 국내 서빙로봇 업체 브이디컴퍼니는 2023년 말까지 약 3,000개 업장에 5,000대, 우아한형제들 자회사 비로보틱스는 2024년 3월 말 기준 약 2,000개 업장에 3,100대를 공급했으며, 서빙로봇은 식당을 넘어 스크린골프장·야구장·당구장·인쇄소·문화공간과 물류센터·중소형 공장으로 쓰임이 넓어지고 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-956"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "보급 대수·업장 수는 업체가 밝힌 값을 기사가 옮긴 것이며, 렌탈료·점유율·한계는 이 기사에 제시되지 않았다.",
      "as_of": "2024-07-30",
      "site_type": "상업 시설",
      "flow_item": "수행 자원"
    },
    {
      "id": "f11",
      "claim": "브이디컴퍼니는 2023-03-30 신제품 발표에서 손님이 테이블의 태블릿으로 주류·음료를 주문하면 주문 정보가 음료냉장고로 전달되고 서빙로봇이 자동으로 받아 테이블로 나르는 ‘브이디셜틀’과 레이저로 이동 경로를 바닥에 표시하는 ‘스위프트봇’을 내놓으며 2019~2022년 누적 3,000대를 공급했다고 밝혔다.",
      "tag": "추정",
      "source_ids": [
        "ref-959"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 회사는 서빙로봇 시장을 2조 원 규모로 보고 70만여 외식업장 중 3만 곳 이상에 필요하다고 주장했다(이투데이 보도).",
      "as_of": "2023-03-30",
      "site_type": "상업 시설",
      "flow_item": "시작 조건",
      "vendor_claim": true
    },
    {
      "id": "f12",
      "claim": "Karlsen 외(NTNU·Nord University, Frontiers in Robotics and AI, 2026-04-22)는 노르웨이 식당 서비스 로봇 도입 사례(면접 22회·참여자 34명·관찰)를 분석해, 도입 동기가 인력 부족·직원 건강·안전·비용이고, 계단·문턱 같은 건축 장애물이 없는 넓은 배치가 필요해 신축 단계 반영이 개조 비용을 줄이며, 통합 과정은 시설 평가 → 수동 주행으로 공간 지도 작성 → 디지털 지도에 정차점·경로 지정 → 직원 관찰을 받는 며칠간의 시험 → 맞춤 설정의 5단계로 진행됐다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-965"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "사례 로봇은 바퀴형·팔 없음·트레이 4단·적재 40kg, 가격대 약 2만~3만 달러(하위 세그먼트). 반발을 줄이려 로봇을 ‘운반 보조’·‘자동 카트’·건강·안전 조치로 소개했다.",
      "as_of": "2026-04-22",
      "site_type": "상업 시설",
      "flow_item": "제약"
    },
    {
      "id": "f13",
      "claim": "같은 연구는 서빙로봇이 피크 시간과 예약 없는 대규모 테이블에서 가장 쓸모 있고 주방 가까운 구역에서는 직원이 직접 나르는 편이 빨랐으며, 20인 테이블 기준 직원 왕복을 10회에서 2회로 줄여 약 320m 보행과 35.2kg 운반을 덜었다고 평가하고, 로봇의 이동·배치 결정에는 홀 직원이 참여해야 한다고 결론지었다.",
      "tag": "사실",
      "source_ids": [
        "ref-965"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "1회 운반 접시 8개(각 약 2.2kg) 조건의 계산값이며 단일 식당 관찰에 기댄다. 손님은 로봇을 ‘재미있고 새롭다’고 보았으나 사람 응대는 여전히 필수로 평가됐다.",
      "as_of": "2026-04-22",
      "site_type": "상업 시설",
      "flow_item": "예외·성과"
    },
    {
      "id": "f14",
      "claim": "Odekerken-Schröder·Mennens·Steins·Mahr(Journal of Service Management 33(2), 2022)는 코로나19 시기 유럽의 패스트 캐주얼 아시아 음식점에서 음료·요리를 나르는 휴머노이드 서비스 로봇 2대를 대상으로 현장 고객 108명과 실험 참가자 361명을 조사해, 로봇의 낮은 기능적 가치를 일선 직원의 높은 응대 품질이 보완할 수 있고(보완) 기능이 뛰어난 로봇은 직원 지원 의존을 줄인다(대체)는 서비스 삼자 관계 결과를 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-961"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "구조방정식 분석. 의인화는 실용적 가치에, 사회적 존재감은 쾌락적 가치에 더 크게 작용. 초록 수준 확인(출판사 페이지).",
      "as_of": "2022",
      "site_type": "상업 시설",
      "flow_item": "수행 자원"
    },
    {
      "id": "f15",
      "claim": "한국노동연구원 박수민 외(2024)의 음식업 서비스 로봇 연구는 키오스크·태블릿 주문과 서빙로봇 전달로 운영되는 음식점에서 로봇 도입에 따른 작업 동선 변화가 사람과 사물의 충돌 위험을 만들고 로봇 설치·운행에 알맞은 물리적 공간이 필요하며, 조사 사업장에서 비상정지 버튼 활용 교육과 로봇 청소 시 안전이 미흡해 정기 교육이 병행돼야 한다고 보고한다.",
      "tag": "사실",
      "source_ids": [
        "ref-960"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 결과 요약 기준(보고서 PDF·저장소 페이지 403). 비상정지·청소 안전 지적은 조리로봇을 포함한 음식업 로봇 전반에 관한 것이며 서빙로봇 단독 수치는 확인하지 못했다.",
      "as_of": "2024",
      "site_type": "상업 시설",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f16",
      "claim": "2015년 나가사키 하우스텐보스에 문을 연 일본 헨나 호텔은 2019년 1월 로봇 243대 가운데 절반 이상을 줄였는데, 객실 음성 비서 로봇이 기본 질문에 답하지 못하거나 코 고는 소리를 명령으로 오인해 손님을 깨웠고, 짐 운반 로봇과 프런트 로봇이 여권 복사 같은 업무를 해내지 못해 사람 직원이 계속 개입해야 했다.",
      "tag": "사실",
      "source_ids": [
        "ref-962",
        "ref-963"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "두 출처 모두 로봇이 직원 업무를 줄이기보다 늘렸다고 전한다. 두 출처는 서로 다른 발행 주체이나 모두 2019년 언론 보도를 바탕으로 한 2차 자료다.",
      "as_of": "2019-01",
      "site_type": "상업 시설",
      "flow_item": "예외·성과"
    },
    {
      "id": "f17",
      "claim": "지디넷코리아(2022-04-11)에 따르면 스마트도시협회는 건축·시설 설계, 네트워크·시스템, 건축 운영 관리, 로봇 지원·기타 서비스의 4개 부문 25개 지표로 최우수·우수·일반 등급을 매기는 민간 ‘로봇 친화형 건축물 인증’을 시행해 첫 대상인 네이버 제2사옥(1784)에 2022-04-06 현장 실사를 거쳐 최우수 등급을 주었고, 평가위원은 이동형 서비스 로봇의 승강기 이동 지원과 로봇용 정밀지도·측위 인프라를 평가했다.",
      "tag": "사실",
      "source_ids": [
        "ref-957"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "첫 인증 대상은 업무용 건물(오피스)이며, 호텔·쇼핑몰 같은 상업 시설의 인증 사례는 이번 조사에서 확인하지 못했다.",
      "as_of": "2022-04-11",
      "site_type": "기타",
      "flow_item": "제약"
    },
    {
      "id": "f18",
      "claim": "산업통상자원부 국가기술표준원은 2021-11-11 로봇의 엘리베이터 탑승 안전 요구사항과 실내 배송 로봇에 관한 국가표준(KS) 제정을 발표했으며, 건물 안을 이동하는 로봇이 사람과 안전하게 접촉하도록 속도 제어·위험 상황의 보호 정지·높낮이차·틈새 극복·추락·넘어짐 방지를 다룬다.",
      "tag": "사실",
      "source_ids": [
        "ref-945"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "보도자료는 적용 건물 유형을 특정하지 않는다. KS 표준 번호는 이 자료에서 확인되지 않는다. (재인용: 2026-09-29-13)",
      "as_of": "2021-11-11",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f19",
      "claim": "Open-RMF 코어는 서로 다른 제조사 플릿을 제어 수준별로 붙이는 플릿 어댑터, 교통 일정 데이터베이스와 충돌 협상, 작업 배정, 문·승강기·디스펜서 같은 건물 설비의 표준 인터페이스를 제공하므로 제조사가 다른 배송·청소·안내 로봇이 승강기를 함께 쓰는 호텔·쇼핑몰의 참고 구조가 될 수 있으나, 이번 조사에서 호텔·식당·쇼핑몰의 Open-RMF 적용 사례는 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-004"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "RMF 문서는 \"The more collaborative a fleet is with RMF, the more harmoniously all of the fleets and systems are able to operate together\" 라고 적는다(공식 저장소 원문).",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f20",
      "claim": "확인한 자료를 종합하면 상업 시설의 로봇 작업은 (1) 호텔 객실 배송 — 비품·음식을 층간 이동해 객실로(f1·f3·f4), (2) 식당 서빙·음료 전달 — 주방·음료냉장고에서 테이블로(f10·f11·f12·f13·f14), (3) 매장·쇼핑몰·호텔 안내 — 쇼핑 정보·길 안내·도슨트(f3·f8), (4) 청소·방역과 재고 스캔 — 바닥·공용 공간과 선반 정보(f3·f5·f7), (5) 프런트·객실 응대 — 체크인·객실 음성 비서(f16, 실패 사례)의 다섯 형태로 나타난다.",
      "tag": "추정",
      "source_ids": [
        "ref-103",
        "ref-952",
        "ref-958",
        "ref-956",
        "ref-959",
        "ref-965",
        "ref-961",
        "ref-954",
        "ref-964",
        "ref-953",
        "ref-962"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "위 finding 들을 작업 대상별로 묶은 종합이다. 작업 대상에는 물건(비품·음식), 공간(바닥·공용 공간), 정보(선반 재고·가격), 사람(안내받는 손님)이 모두 포함된다.",
      "as_of": "2026-09-29",
      "site_type": "상업 시설",
      "flow_item": "작업 대상"
    },
    {
      "id": "f21",
      "claim": "확인한 자료를 종합하면 상업 시설 로봇 작업의 여섯 항목은 시작 조건이 객실 호출·객실 전화·테이블 태블릿 주문(f3·f11), 작업 대상이 비품·음식·음료·바닥·선반 정보·안내받는 손님(f20), 수행 자원이 배송·서빙·청소·안내 로봇과 음식을 싣고 예외를 처리하는 직원·원격 조작자(f8·f13·f14), 제약이 손님과 함께 쓰는 승강기와 아침 식사·체크아웃 같은 혼잡 시간(f1·f2), 계단·문턱 없는 넓은 동선과 사람과의 충돌 위험(f12·f15), 승강기 탑승 안전 요구(f18), 예외·성과가 로봇 실패 시 직원 개입 부담과 보행·운반 감소 같은 지표(f13·f16)로 채워질 수 있으나, 완료·인계(손님 수령·테이블 전달 확인) 방식은 이번 자료에서 명시적으로 확인되지 않았다.",
      "tag": "추정",
      "source_ids": [
        "ref-952",
        "ref-959",
        "ref-954",
        "ref-965",
        "ref-961",
        "ref-103",
        "ref-960",
        "ref-945",
        "ref-962"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "분류 원문 21장의 여섯 항목에 이번 finding 을 대입한 종합이며, 완료·인계 칸은 근거 부족으로 비워 둘 것을 제안한다.",
      "as_of": "2026-09-29",
      "site_type": "상업 시설",
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "확인한 자료를 종합하면 64. 상업 시설에서 ROP 가 직접 맡을 범위는 객실 호출·테이블 주문·청소 일정 같은 요청을 받아 제조사가 다른 배송·서빙·청소·안내 로봇에 배정하고(f3·f10·f11), 손님과 함께 쓰는 승강기를 예약하며 아침 식사·체크아웃 같은 혼잡 시간을 배송·청소 일정의 제약으로 반영하고(f1·f2·f6), 로봇이 처리하지 못하는 요청을 직원·원격 조작자에게 넘기며(f8·f14·f16), 완료와 재고 스캔 같은 수집 정보를 업무 시스템에 돌려주는 일(f7)이고, 이를 이기종 로봇에 걸쳐 하나의 계층으로 묶은 상업 시설 공개 사례는 확인되지 않았다.",
      "tag": "추정",
      "source_ids": [
        "ref-952",
        "ref-956",
        "ref-959",
        "ref-103",
        "ref-958",
        "ref-964",
        "ref-954",
        "ref-961",
        "ref-962",
        "ref-953"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "분류 원문 19장의 직접 범위(요청·기한·자원 제약을 받아 실행하고 결과 반영, 설비의 작업 요청·예약·상태 확인)에 이번 사례를 대입한 판단이다.",
      "as_of": "2026-09-29",
      "site_type": "상업 시설",
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "연계 대상: 호텔 객실 관리 시스템·식당 POS·테이블오더·소매 재고 시스템은 분류 원문 19장의 상위 업무 시스템, 승강기 제어반과 제조사 승강기 API·승강기 관리 솔루션은 시설·설비 제어, 로봇의 자율 주행·장애물 회피·음성 인식은 로봇 자체 지능·제어, 식품 위생·숙박 손님 개인정보 같은 업종 규정은 업종별 조건에 속하므로, 이종 제조사를 잇는 ROP 는 이들에 작업 요청·예약·인계·상태 확인만 걸고 메뉴·결제·재고 판단, 승강기 제어, 주행 안전 성능은 해당 시스템·승강기 업체·로봇 제조사에 맡겨야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-959",
        "ref-953",
        "ref-958",
        "ref-964",
        "ref-952",
        "ref-954"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "테이블오더–음료냉장고–서빙로봇 연동(ref-959), 재고 스캔 정보의 관리자 전달(ref-953), 승강기 API·rEMS(ref-958·ref-964), 로봇 자체 주행·회피(ref-952), 음성 인식 한계(ref-954)를 경계별로 나눈 판단이다.",
      "as_of": "2026-09-29",
      "site_type": "상업 시설",
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "이 영역은 승강기 연동을 다루는 22. 설비·건물 시스템 연동(f4·f5·f6·f17·f18), 객실 관리 시스템·POS·테이블오더·재고 시스템을 다루는 23. 업무 시스템 연동(f7·f11), 이기종 로봇과 Open-RMF 를 다루는 20. 로봇·제조사 관제 연동(f19), 승강기를 공용 자원으로 다루는 28. 공용 자원·충전·에너지 최적화와 혼잡 시간 일정을 다루는 26. 작업 순서·스케줄링(f1·f2), 로봇 대수 한계 이익을 다루는 35. 처리능력·규모·배치 설계(f1), 쇼핑몰 보행자와 충돌을 다루는 19. 사람·보행자 모델·49. 사람 근접 안전(f8·f15), 직원과 로봇의 분담을 다루는 31. 사람–로봇 협업(f13·f14), 직원 인식·일자리 우려를 다루는 60. 노동·수용성·접근성(f9·f12·f15), 매장 지도 작성·시험 운행을 다루는 55. 현장 조사·설치·시운전(f12), 실패 사례와 직원 개입을 다루는 32. 예외 복구·재계획·업무 연속성(f16), 음성 비서 실패를 다루는 13. 대화형 기능의 신뢰·기반(f16), 보급 현황을 다루는 1. 기술·시장·업체 동향(f10), 도입 비용을 다루는 3. 경제성·조달·사업 모델(f9·f12)에 이어진다.",
      "tag": "추정",
      "source_ids": [
        "ref-958",
        "ref-964",
        "ref-957",
        "ref-945",
        "ref-953",
        "ref-959",
        "ref-004",
        "ref-103",
        "ref-954",
        "ref-960",
        "ref-965",
        "ref-961",
        "ref-955",
        "ref-962",
        "ref-956"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "각 연결은 괄호 안 finding 을 근거로 제안한 것이며 연결 영역 페이지의 내용과 대조하지 않았다.",
      "as_of": "2026-09-29",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-103",
      "org": "Han, L., Ding, J., Liu, S., & Meng, M. (Sensors)",
      "title": "The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments",
      "published": "2025-03-13",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "다층 호텔의 다중 로봇 객실 배송을 승강기를 암묵적 경유지로 둔 다중 운행 차량 경로 문제로 모델링하고 ALNS 로 푼 동료 심사 논문(오픈 액세스 원문 열람).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/",
      "source_unopened": false
    },
    {
      "id": "ref-952",
      "org": "지디넷코리아 (윤상은)",
      "title": "엘베 타고 수건 배달·안내·방역도 '척척'...호텔로 간 로봇",
      "published": "2022-05-03",
      "url": "https://zdnet.co.kr/view/?no=20220503124850",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "국내 호텔(헨나호텔 명동, 코트야드 메리어트 타임스퀘어, 테이크호텔 광명, 노보텔 앰배서더 동대문, 롯데월드호텔, 안다즈 강남 등)의 배송·안내·방역 로봇 도입과 승강기 이용·호출 방식을 정리한 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://zdnet.co.kr/view/?no=20220503124850",
      "source_unopened": false
    },
    {
      "id": "ref-953",
      "org": "Retail Dive (Sam Silverstein)",
      "title": "Sam's Club rolls out inventory-checking robots chainwide",
      "published": "2022-02-01",
      "url": "https://www.retaildive.com/news/sams-club-rolls-out-inventory-checking-robots-chainwide/618040/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "Sam's Club 이 약 600개 매장의 자율 바닥 청소기에 Brain Corp 재고 스캔 타워를 달아 청소와 재고 스캔을 함께 수행하게 한 전사 배치를 보도.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.retaildive.com/news/sams-club-rolls-out-inventory-checking-robots-chainwide/618040/",
      "source_unopened": false
    },
    {
      "id": "ref-954",
      "org": "Kanda, T., Shiomi, M., Miyashita, Z., Ishiguro, H., & Hagita, N. (IEEE Transactions on Robotics 26(5))",
      "title": "A Communication Robot in a Shopping Mall",
      "published": "2010-10",
      "url": "https://ieeexplore.ieee.org/abstract/document/5557825",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "원문 미열람. 쇼핑몰에서 쇼핑 정보·길 안내를 하는 커뮤니케이션 로봇의 25일 현장 시험(상호작용 2,642회)과 센서·원격 조작자를 결합한 반자율 네트워크 로봇 시스템을 보고한 논문. 서지는 Semantic Scholar API 로, 초록 내용은 검색 결과 요약으로만 확인.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-955",
      "org": "Ivanov, S., Seyitoğlu, F., & Markova, M. (Information Technology & Tourism)",
      "title": "Hotel managers' perceptions towards the use of robots: a mixed-methods approach",
      "published": "2020-09",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7486590/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "불가리아 호텔 관리자 설문 79명·면접 20명으로 로봇에 맞는 호텔 업무, 장단점 인식, 도입 의향과 장벽을 분석한 동료 심사 논문(오픈 액세스 원문 열람).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7486590/",
      "source_unopened": false
    },
    {
      "id": "ref-956",
      "org": "지디넷코리아 (신영빈)",
      "title": "식당 음식 나르던 서빙로봇, 공장·창고로 진격",
      "published": "2024-07-30",
      "url": "https://zdnet.co.kr/view/?no=20240730115912",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "브이디컴퍼니·비로보틱스의 국내 서빙로봇 보급 대수·업장 수와 식당 외 분야(스크린골프장·야구장·물류센터·공장)로의 확장을 보도. 원 URL 연결이 끊겨 다음 뉴스 게재본으로 열었다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://v.daum.net/v/20240730133507385",
      "source_unopened": false
    },
    {
      "id": "ref-957",
      "org": "지디넷코리아 (김성현)",
      "title": "네이버 제2사옥, 로봇 친화형 건축물 인증 획득",
      "published": "2022-04-11",
      "url": "https://zdnet.co.kr/view/?no=20220411142336",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "스마트도시협회의 민간 로봇 친화형 건축물 인증(4개 부문 25개 지표, 3개 등급)과 첫 대상 네이버 1784 의 최우수 등급 획득을 보도.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://zdnet.co.kr/view/?no=20220411142336",
      "source_unopened": false
    },
    {
      "id": "ref-958",
      "org": "Otis Elevator Company",
      "title": "Elevators and service robots",
      "published": null,
      "url": "https://www.otis.com/en/us/innovation/elevators-and-service-robots",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-29",
      "summary": "오티스의 승강기–서비스 로봇 연동(Otis Integrated Dispatch 클라우드 API)과 오사카 호텔 케이한 유니버설 타워 배송 로봇 적용을 소개하는 제조사 페이지. 기능·성과는 벤더 주장.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.otis.com/en/us/innovation/elevators-and-service-robots",
      "source_unopened": false
    },
    {
      "id": "ref-959",
      "org": "이투데이 (구예지)",
      "title": "브이디컴퍼니, 신규 서빙로봇 3종 출시…“식당 전체 자동화 이룰 것”",
      "published": "2023-03-30",
      "url": "https://www.etoday.co.kr/news/view/2235962",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "브이디컴퍼니의 신규 서빙로봇(푸두봇 프로·스위프트봇·브이디셜틀)과 태블릿 주문–음료냉장고–서빙로봇 연동, 누적 공급 대수를 회사 발표 중심으로 보도.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.etoday.co.kr/news/view/2235962",
      "source_unopened": false
    },
    {
      "id": "ref-960",
      "org": "한국노동연구원 (박수민 외)",
      "title": "음식업 서비스 로봇 도입이 직무와 작업장 안전에 미치는 영향",
      "published": "2024",
      "url": "https://repository.kli.re.kr/bitstream/2021.oak/11632/2/(%EC%97%B0%EA%B5%AC%EB%B3%B4%EA%B3%A0)2024-13_%EC%9D%8C%EC%8B%9D%EC%97%85%20%EC%84%9C%EB%B9%84%EC%8A%A4%20%EB%A1%9C%EB%B4%87%20%EB%8F%84%EC%9E%85%EC%9D%B4%EC%A7%81%EB%AC%B4%EC%99%80%20%EC%9E%91%EC%97%85%EC%9E%A5%20%EC%95%88%EC%A0%84%EC%97%90%20%EB%AF%B8%EC%B9%98%EB%8A%94%20%EC%98%81%ED%96%A5.pdf",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "원문 미열람. 한국노동연구원 연구보고서 2024-13. 급식업 조리로봇과 외식업 서빙로봇 도입의 이유·조건, 직무·동선 변화, 작업장 안전 문제를 분석(보고서 PDF·저장소 페이지 403, 검색 결과 요약만 확인).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-961",
      "org": "Odekerken-Schröder, G., Mennens, K., Steins, M., & Mahr, D. (Journal of Service Management 33(2))",
      "title": "The service triad: an empirical study of service robots, customers and frontline employees",
      "published": "2022",
      "url": "https://www.emerald.com/josm/article/33/2/246/227998/The-service-triad-an-empirical-study-of-service",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "유럽 패스트 캐주얼 식당의 휴머노이드 서비스 로봇 2대에 대한 현장 고객 108명·실험 361명 조사로 로봇·고객·일선 직원 삼자 관계에서 보완·대체 효과를 분석한 동료 심사 논문(출판사 페이지의 초록 수준 확인).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.emerald.com/josm/article/33/2/246/227998/The-service-triad-an-empirical-study-of-service",
      "source_unopened": false
    },
    {
      "id": "ref-962",
      "org": "Responsible AI Collaborative (AI Incident Database)",
      "title": "Incident 346: Robots in Japanese Hotel Annoyed Guests and Failed to Handle Simple Tasks",
      "published": null,
      "url": "https://incidentdatabase.ai/cite/346/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "일본 헨나 호텔의 로봇 243대 운영과 2019년 절반 이상 감축, 객실 비서·여권 복사 등 실패를 여러 언론 보도를 묶어 기록한 AI 사고 데이터베이스 항목.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://incidentdatabase.ai/cite/346/",
      "source_unopened": false
    },
    {
      "id": "ref-963",
      "org": "Hotel Technology News",
      "title": "Score One for The Humans: Japan's Henn-na Hotel Fires Half Its Robot Workforce",
      "published": "2019-01",
      "url": "https://hoteltechnologynews.com/2019/01/score-one-for-the-humans-japans-henn-na-hotel-fires-half-its-robot-workforce/",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-29",
      "summary": "헨나 호텔이 로봇 243대 가운데 절반 이상을 줄인 경위(객실 비서 Churi, 짐 운반 로봇, 프런트 공룡 로봇의 실패와 직원 부담)를 전한 호텔 기술 전문지 기사. 1차 출처를 명시하지 않는다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://hoteltechnologynews.com/2019/01/score-one-for-the-humans-japans-henn-na-hotel-fires-half-its-robot-workforce/",
      "source_unopened": false
    },
    {
      "id": "ref-964",
      "org": "서울경제 (백주연)",
      "title": "엘리베이터 타고 쇼핑몰 왔다갔다…바닥 물걸레질까지 하는 '로봇 청소부' 등장",
      "published": "2025-04-02",
      "url": "https://www.sedaily.com/article/14048085",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "화성 동탄 상업시설 레이크 꼬모의 라이노스 AI 청소로봇 휠리 J40 도입과 클라우드 승강기 관리 솔루션 rEMS 를 통한 전 층 이동을 보도.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.sedaily.com/article/14048085",
      "source_unopened": false
    },
    {
      "id": "ref-965",
      "org": "Karlsen, A. S. T., Andersen, B., Nevstad, K., Heirsaunet, S. E., Indergård, E., & Aarseth, W. (Frontiers in Robotics and AI)",
      "title": "Digital transformation in restaurants: key aspects of service robot deployment from project initiation to evaluation",
      "published": "2026-04-22",
      "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2026.1793138/full",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "노르웨이 식당 서비스 로봇 도입을 사업 착수·계획·통합·실행·평가 단계로 분석한 탐색·설명적 사례 연구(면접 22회·참여자 34명, 오픈 액세스 원문 열람).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2026.1793138/full",
      "source_unopened": false
    },
    {
      "id": "ref-945",
      "org": "산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재)",
      "title": "국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다",
      "published": "2021-11-11",
      "url": "https://eiec.kdi.re.kr/policy/materialView.do?num=220004",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "로봇의 엘리베이터 탑승 안전 요구사항과 실내 배송 로봇 KS 제정 발표(속도 제어·보호 정지·높낮이차·틈새 극복·추락·넘어짐 방지). 이번 실행에서 다시 열어 확인.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://eiec.kdi.re.kr/policy/materialView.do?num=220004",
      "source_unopened": false
    },
    {
      "id": "ref-004",
      "org": "Open Robotics",
      "title": "RMF Core Overview — Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/rmf-core.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "작업·교통 조율, Fleet Adapter, 설비 연동 구조 참고.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/rmf-core.md",
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/site-type-applications/commercial-facilities.md",
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
      "rationale": "섹션 3: f10(국내 서빙로봇 보급 약 8,000대 규모와 다른 업종 확장), f12(인력 부족·직원 건강이 도입 동기), f9·f16(관리자 인식과 대규모 실패 사례가 보여 주는 운영 난도) / 섹션 4: f1(다중 운행 차량 경로 문제), f17(로봇친화형 건축물 인증), f14(서비스 삼자 관계), f8(반자율 네트워크 로봇 시스템) / 섹션 5(현장 유형은 f17 을 빼고 모두 상업 시설): 호텔 객실 배송 — f3(국내 호텔 5곳 이상), f4(오사카 호텔, 벤더 주장), f1·f2(중국 호텔 자료 경로 계획); 식당 서빙 — f10·f11(국내 보급·테이블오더 연동, f11 은 벤더 주장), f12·f13(노르웨이 식당), f14(유럽 식당), f15(국내 음식업 안전); 매장·쇼핑몰 안내·청소 — f8(쇼핑몰 안내 로봇), f7(Sam's Club 청소·재고 스캔), f5(레이크 꼬모 청소로봇); 실패 사례 — f16(헨나 호텔); 작업 형태 지도 f20, 여섯 항목 정리 f21(완료·인계 칸은 근거 부족) / 섹션 6: 승강기 이용 방식 f6(f3·f4·f5), 혼잡 시간 반영 경로 계획 f1·f2, 주문 시스템 연동 f11, 식당 도입 5단계 f12, 직원 역할 분담 f13·f14, 반자율 원격 운영 f8 / 섹션 7: f18(KS 로봇 엘리베이터 탑승 안전 요구사항·실내 배송 로봇, ref-945 재사용), f17(로봇친화형 건축물 인증, 오피스 사례임을 명시), f19(Open-RMF, ref-004 재사용, 상업 시설 적용 사례 미확인) / 섹션 8: f1(호텔 경로 계획), f9(호텔 관리자 인식), f14(식당 서비스 삼자), f12·f13(식당 도입 사례 연구), f8(쇼핑몰 현장 시험), f15(한국노동연구원 보고서, 원문 미열람) / 섹션 9: f22(직접 범위: 요청 수신·이기종 배정·승강기 예약·혼잡 시간 반영·직원 인계·결과 반환), f23(연계 대상: 객실 관리 시스템·POS·테이블오더·재고 시스템, 승강기 제어, 로봇 자체 주행·음성 인식, 업종 규정) / 섹션 10: f24 — 1. 기술·시장·업체 동향, 3. 경제성·조달·사업 모델, 13. 대화형 기능의 신뢰·기반, 19. 사람·보행자 모델, 20. 로봇·제조사 관제 연동, 22. 설비·건물 시스템 연동, 23. 업무 시스템 연동, 26. 작업 순서·스케줄링, 28. 공용 자원·충전·에너지 최적화, 31. 사람–로봇 협업, 32. 예외 복구·재계획·업무 연속성, 35. 처리능력·규모·배치 설계, 49. 사람 근접 안전, 55. 현장 조사·설치·시운전, 60. 노동·수용성·접근성 / 섹션 11: open_questions_new 5건(기존 열린 질문 없음). f4·f11 은 벤더 주장 병기 필수. 다음 실행 후보: 22. 설비·건물 시스템 연동 페이지에 f6·f17 반영, 23. 업무 시스템 연동 페이지에 f7·f11 반영, 60. 노동·수용성·접근성 페이지에 f9·f15·f16 반영, 31. 사람–로봇 협업 페이지에 f13·f14 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "다중 운행 차량 경로 문제",
      "term_en": "Multi-Trip Vehicle Routing Problem (MTVRP)",
      "definition": "적재 용량이 정해진 차량(로봇)이 한 거점에서 여러 번 출발·복귀하며 여러 목적지를 도는 경로를 정하는 차량 경로 문제의 변형으로, 다층 호텔의 로봇 객실 배송 계획에 승강기를 경유지로 넣어 쓰였다."
    },
    {
      "term_ko": "로봇친화형 건축물 인증",
      "term_en": "Robot-Friendly Building Certification",
      "definition": "스마트도시협회가 2022년 시작한 민간 인증으로, 건축·시설 설계, 네트워크·시스템, 건축 운영 관리, 로봇 지원·기타 서비스 4개 부문 25개 지표로 건물이 로봇의 승강기 이동과 측위 등을 얼마나 지원하는지를 최우수·우수·일반 등급으로 평가한다."
    },
    {
      "term_ko": "서비스 삼자 관계",
      "term_en": "Service Triad (service robot, customer, frontline employee)",
      "definition": "서비스 로봇·고객·일선 직원 세 주체의 상호작용으로 서비스 가치를 설명하는 틀로, 로봇이 직원을 보완하는지 대체하는지와 직원 응대가 로봇의 기능 부족을 메우는지를 분석한다."
    }
  ],
  "open_questions_new": [
    "호텔·쇼핑몰에서 제조사가 다른 배송·청소·안내 로봇을 하나의 오케스트레이션 계층(Open-RMF 등)으로 묶어 승강기를 함께 쓰게 한 국내외 공개 사례가 있는가? | 관련 영역: 64. 상업 시설, 20. 로봇·제조사 관제 연동, 22. 설비·건물 시스템 연동 | 근거: f19 | 종류: 일반",
    "호텔 객실 배송 로봇이 객실 관리 시스템(PMS)이나 객실 전화에서 요청을 받고 배송 완료를 되돌려 주는 표준 인터페이스나 공개된 연동 구조가 있는가? | 관련 영역: 64. 상업 시설, 23. 업무 시스템 연동 | 근거: f3 | 종류: 일반",
    "영업 중인 매장·쇼핑몰에서 청소·재고 스캔 로봇을 손님이 많은 시간과 어떻게 나눠 운영하는지(운영 시간대 규칙과 그 효과)를 수치로 보인 연구나 공개 자료가 있는가? | 관련 영역: 64. 상업 시설, 26. 작업 순서·스케줄링 | 근거: f7 | 종류: 일반",
    "로봇친화형 건축물 인증이 오피스를 넘어 호텔·쇼핑몰 같은 상업 시설로 확대됐는가, 그리고 2025년 도입이 예고된 스마트+빌딩 인증과 어떤 관계인가? | 관련 영역: 64. 상업 시설, 22. 설비·건물 시스템 연동 | 근거: f17 | 종류: 일반",
    "식당 서빙로봇과 호텔 배송 로봇은 손님이 음식·물품을 받았는지(완료·인계)를 어떤 방식(무게 감지·버튼·직원 확인·객실 문 앞 알림)으로 확인하며 그 결과가 주문 시스템에 기록되는가? | 관련 영역: 64. 상업 시설, 17. 작업 대상·자산 식별과 인계 추적 | 근거: f21 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 17,
    "cross_checked_count": 1,
    "unverified": [
      "f1·f2 호텔 경로 계획 수치(승강기 시간 40→100초에서 배송 시간 약 2배, 로봇 5대 이상 한계 이익 감소)는 단일 논문·단일 호텔 자료이며 교차 확인 실패",
      "f3 국내 호텔 로봇 도입 목록은 지디넷코리아 한 건이며 현재 운영 여부 미확인",
      "f4 오티스 OID 호환 범위와 오사카 호텔 야간 60건 처리는 벤더 문서 단독(벤더 주장)",
      "f5 레이크 꼬모 청소로봇의 운영 시간대와 rEMS 연동 성능은 기사에 없음",
      "f7 Sam's Club 로봇의 운영 시간대(영업 중·후)와 생산성 수치 미확인",
      "f8 Kanda 외 2010 논문은 출판사(ACM·IEEE·ResearchGate 403, ADS 405)와 Semantic Scholar 초록 비공개로 초록 원문을 열지 못해 검색 결과 요약만 확인",
      "f10 서빙로봇 보급 대수는 업체가 밝힌 값을 기사가 옮긴 것이며 독립 집계 없음",
      "f11 브이디컴퍼니 연동 방식·시장 규모는 회사 발표(벤더 주장)",
      "f12·f13 노르웨이 식당 수치(320m·35.2kg)는 단일 사례 연구의 계산값",
      "f15 한국노동연구원 보고서 원문·노동리뷰 원고(repository.kli.re.kr 403)를 열지 못해 검색 결과 요약 범위만 사용, 서빙로봇 단독 수치 미확인",
      "f16 헨나 호텔 두 출처는 모두 2019년 언론 보도를 바탕으로 한 2차 자료이며 1차 보도(월스트리트저널 등)는 열지 않음",
      "f17 로봇친화형 건축물 인증의 상업 시설 적용 사례와 이후 제도 변화 미확인",
      "f18 KS 표준 번호·정식 명칭 미확인",
      "f19 호텔·식당·쇼핑몰의 Open-RMF 적용 사례 미확인(싱가포르 Mapletree Business City 사례는 오피스·비즈니스 파크이고 IMDA 보도자료 본문이 로드되지 않아 제외)",
      "f21 완료·인계 항목(손님 수령 확인 방식)은 근거 자료를 찾지 못함"
    ],
    "scope_violations": [
      "f23: 객실 관리 시스템·POS·테이블오더·재고 시스템의 메뉴·결제·재고 판단, 승강기 제어반·제조사 승강기 API·승강기 관리 솔루션의 제어, 로봇의 자율 주행·장애물 회피·음성 인식, 식품 위생·숙박 개인정보 규정은 분류 원문 19장의 상위 업무 시스템·시설·설비 제어·로봇 자체 지능·제어·업종별 조건 쪽이므로 '연계 대상: '으로 표시함",
      "f4·f5·f6: 승강기 연동 방식은 22. 설비·건물 시스템 연동 의 핵심이므로 이 영역에서는 상업 시설 로봇 운영의 제약·사례 근거로만 제안함",
      "f7·f11: 재고 스캔 정보 전달과 테이블오더 연동은 23. 업무 시스템 연동 의 방법이므로 이 영역에서는 시작 조건·작업 대상의 근거로만 제안함",
      "f8·f16: 음성 인식·객실 음성 비서 실패는 로봇 자체 기능과 13. 대화형 기능의 신뢰·기반 쪽이므로 이 영역에서는 사람 개입이 필요한 예외 사례로만 제안함",
      "f17: 로봇친화형 건축물 인증의 첫 사례는 오피스(현장 유형 기타)이므로 site_type 을 기타로 두고 상업 시설 사례로 쓰지 않도록 표시함"
    ],
    "budget_used": {
      "queries": 23,
      "sources": 15
    },
    "limits": "web_fetch_available: true · fetch_mode full. 검색 23회/30, 신규 출처 15건/15(ref-103~ref-965, 이 실행 전용 예약 구간 ref-103~ref-980 안) 상한 도달로 arXiv 2412.10699(상업용 실내 배송 로봇 40종 사이버·물리 보안 분석, 초록만 확인), Shiomi 외 쇼핑몰 보행자 회피 연구(Semantic Scholar 429·ResearchGate 403), Retail/상업 시설 청소로봇 벤더 블로그, 싱가포르 IMDA Mapletree Business City RMF 보도자료(본문 로드 실패, 오피스)는 넣지 않았다. 주의: 같은 날 이전 실행 2026-09-29-13 브리프가 ref-103(비즈한국)·ref-952(품질경영학회지 논문)·ref-953(한국보건산업진흥원)을 다른 URL 에 부여했다고 적혀 있으나, 이번 실행 컨텍스트가 ref-103~ref-980 을 이 실행 전용으로 예약했으므로 그 지시를 따랐다 — 퍼블리셔가 URL 기준으로 합칠 때 번호 충돌을 확인해야 한다. 원문 열람: 신규 13건 webfetch(PMC 원문 2, Frontiers 원문 1, Emerald 초록 1, 기사 7, 오티스 페이지 1, AI Incident Database 1), 미열람 2건(ref-954 Kanda 외 초록 비공개, ref-960 한국노동연구원 403). ref-956 은 원 URL 이 연결 재설정으로 끊겨 다음 뉴스 게재본으로 열었다. 재사용 2건(ref-945 은 KDI 게재 원문을, ref-004 는 공식 저장소 raw 원문을 이번에 다시 열었다; 참고문헌 목록 입력이 이 페이지 인용분 0건만 요약되어 두 항목의 기관·제목은 직전 브리프 2026-09-29-13·12 의 표를 따랐다). 교차 확인 1건(f16 헨나 호텔 — AI Incident Database 와 Hotel Technology News, 둘 다 언론 보도 기반 2차 자료라 신뢰도 medium). 신뢰도 high finding 없음. 벤더 주장 finding 2건(f4 오티스, f11 브이디컴퍼니). 분류 원문 핵심 질문(손님이 있는 영업 시간에 호텔·식당·매장의 로봇을 어떻게 운영할 것인가)에는 작업 형태 지도 f20, 여섯 항목 정리 f21, 직접 범위 f22, 연계 대상 f23 으로 답했으며 결론은 '영업 시간 운영의 핵심 제약은 손님과 함께 쓰는 승강기·동선의 혼잡 시간과 사람과의 충돌이고(f1·f2·f12·f15), 로봇은 피크 시간 운반 보조로 가치가 크되 로봇이 못 하는 요청은 직원·원격 조작자가 넘겨받는 혼합 운영이 전제이며(f8·f13·f14·f16), 이기종 로봇을 한 계층으로 묶은 상업 시설 공개 사례는 확인되지 않았다'는 추정이다. 현장 유형: f17(오피스, 기타)을 빼고 모두 상업 시설(호텔: 국내 여러 호텔·오사카·중국·불가리아·일본 헨나 / 식당: 국내 서빙로봇·노르웨이·유럽 / 매장·쇼핑몰: 미국 Sam's Club·일본 쇼핑몰·화성 레이크 꼬모)이며 이 영역의 성격상 다른 현장 유형 사례는 찾지 않았다. 국내 자료는 지디넷코리아 3건(f3·f10·f17)·이투데이(f11)·서울경제(f5)·한국노동연구원(f15)·국가기술표준원(f18, 재사용) 일곱 건이다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 섞지 않았다(f1 의 경로 계획은 26·35 쪽으로만 연결). 용어집에 이미 있는 승강기 어댑터·플릿 어댑터·오픈 RMF·서비스형 로봇·다중 플릿 오케스트레이션은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 없음, 해결된 열린 질문 없음."
  }
}
```

### runs/2026-09-29-16/verification.json

```json
{
  "run_id": "2026-09-29-16",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(PMC 원문 열람, 첫 시도는 reCAPTCHA였고 재시도에 성공. DOI 10.3390/s25061783, 2025-03-13, Han·Ding·Liu·Meng). 실제 호텔 67실(1~3층) 자료, 60노드에서 승강기 40→100초일 때 총 이동 시간 225→500초, 로봇 5→8대일 때 242→225초를 확인했다. 논문의 지표는 '총 이동 시간(total travel time)'이며, 호텔 소재국(중국)은 이번 열람 범위에서 확인하지 못했다. 단일 논문이다."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 논문 논의 절이 아침 식사·체크아웃 시간대의 승강기 이용 증가를 적고 단방향(상행 또는 하행 전용) 승강기 운행을 권고한다. 제안이며 실증 결과는 아니다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(지디넷코리아 윤상은, 2022-05-03 원문 열람). 집개미의 로봇팔 버튼 조작, 클로이 서브봇 15kg, N봇의 기가지니 객실 전화 연동, 가이드봇의 안내·도슨트·보안, 안다즈 강남 방역로봇을 확인했다. '222nm'는 이번 열람에서 확인하지 못했다. 기준일은 2022-05-03이며 현재 운영 여부는 미확인이다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(오티스 페이지 원문 열람, 발행일 미확인). 모든 브랜드 연동, 승강기 그룹 단위, 1990년대 이후 상업용 승강기 호환, 케이한 유니버설 타워 2022-12부터 AIM Technologies 협력, 바쁜 밤 최대 60건을 확인했다. 제조사 문서이므로 [추정]과 '벤더 주장' 병기를 유지한다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(서울경제 원문 열람). 레이크 꼬모, 휠리 J40, rEMS 전 층 이동, 우미에스테이트 확대 계획을 확인했다. 기사가 '24시간 운영'을 적고 있어 evidence_excerpt의 '시간대 명시 안 됨'은 원문과 다르다. 발행일 2025-04-02는 이번 열람에서 페이지로 확인하지 못했다. 오염 감지·자동 물걸레 세척 같은 기능은 운영사·제조사 설명을 옮긴 것이다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "f3·f4·f5를 종합한 추정이다. 세 방식 분류는 출처로 뒷받침된다. '방식마다 호출 권한·공유 규칙을 정하는 주체가 달라진다'는 출처에 직접 근거가 없는 추론이므로 [추정]을 유지한다. 오티스 방식은 벤더 주장이다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(Retail Dive, Sam Silverstein, 2022-02-01 원문 열람). 약 600개 매장, Tennant·BrainOS 청소기에 Inventory Scan 장착, 가격 정확도·재고 수준·진열 위치 보고, Brain Corp 첫 상용·최대 규모 배치를 확인했다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람(IEEE·ADS 405, 검증 검색 2회). 서지(IEEE T-RO 26(5):897-913, 2010)는 ACM DL·Semantic Scholar 검색 결과로 확인했다. 25일 현장 시험, 2,642회 상호작용, 바닥 센서·RFID, 사람 조작자가 일부를 맡는 반자율 네트워크 로봇 방식은 검색 결과 요약(초록)으로 확인했다. 원문 미열람이므로 medium이 상한이다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(PMC 원문 열람, Information Technology & Tourism 22(4):505-535, 2020-09-12). 설문 79명·면접 20명, 2018-12~2019-04, 평균 2.30·2.08·3.99, 약 63% 도입 의향 없음, 3.8% 1년 안 도입, 비용·시설 개조·유지보수·서비스 품질 장벽을 확인했다. 불가리아 호텔 단일 연구다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(지디넷코리아 신영빈, 2024-07-30, 다음 게재본 열람). 브이디컴퍼니 약 3,000개 업장 5,000대(2023년 말), 비로보틱스 약 2,000개 업장 3,100대(2024-03), 스크린골프장·야구장·당구장·인쇄소·물류센터·중소 공장 확장을 확인했다. 보급 대수는 업체가 밝힌 값이며 독립 집계는 없다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(이투데이 구예지, 2023-03-30 원문 열람). 브이디셜틀(태블릿 주문–냉장고–로봇 연동), 스위프트봇 레이저 경로 표시, 2022년까지 누적 3,000대, 시장 2조 원 주장을 확인했다. 회사 발표 중심이므로 [추정]과 '벤더 주장' 병기를 유지한다. evidence_excerpt의 '3만 곳 이상'은 이번 열람 요약에서 확인하지 못했다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(Frontiers 원문 열람, 2026-04-22). 면접 22회·참여자 34명, 인력 부족·직원 건강·효율의 도입 동기, 계단·문턱과 신축 단계 반영, 5단계 통합 과정(시설 평가→수동 주행 지도 작성→정차점·경로 지정→직원 피드백 시험→맞춤 설정)을 확인했다. 노르웨이 단일 사례 연구다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 피크 시간·예약 없는 대규모 테이블에서 유용하고 주방 가까운 테이블은 직원이 직접 나름, 20인 테이블 10→2회, 약 320m, 35.2kg, 직원 참여가 필수라는 내용을 확인했다. 단일 식당 관찰에 기댄 수치다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(Emerald 출판사 페이지의 초록 수준, JOSM 33(2), 2022). 유럽 패스트 캐주얼 아시아 음식점, 휴머노이드 2대, 현장 108명·실험 361명, 보완(augment)·대체(substitute), 의인화→실용적 가치·사회적 존재감→쾌락적 가치를 확인했다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정. 원문 미열람(보고서 PDF·노동리뷰 요약본 모두 403). 보고서 실재(한국노동연구원 연구보고서 2024-13, 박수민 외)는 저장소 검색 결과로 확인했다. 검증 검색 결과 요약은 서빙로봇·비상정지와 작업자 안전이 주제라는 수준까지만 보여 준다. 동선 변화로 인한 충돌 위험, 설치 공간 필요, 비상정지 교육·청소 시 안전 미흡, 정기 교육 필요라는 구체 진술은 확인하지 못했다. 브리프도 이 지적이 조리로봇을 포함한 음식업 로봇 전반에 관한 것이라고 적는다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인(AI Incident Database 346과 Hotel Technology News 2019-01 모두 원문 열람). 243대 가운데 절반 이상 감축, 객실 비서가 기본 질문에 답하지 못함, 짐 운반·프런트 로봇의 실패, 직원 업무 증가를 두 출처로 교차 확인했다. 코골이 오인은 AIID에만 있고 여권 복사 실패는 두 출처 모두에 있다. '하우스텐보스'는 두 출처 열람 요약에서 확인하지 못했다(AIID는 나가사키로 적음). 두 출처 모두 2019년 언론 보도에 기댄 2차 자료라 신뢰도 medium이다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(지디넷코리아 김성현, 2022-04-11 원문 열람). 스마트도시협회 사설 인증, 4개 부문, 최우수·우수·일반, 네이버 1784 첫 대상, 2022-04-06 현장 실사 최우수, 승강기 이동 지원·정밀지도·측위 인프라 평가를 확인했다. 기사 표현은 '25개 지표'가 아니라 '25개 평가 범주(필수·부가)'다. 현장 유형은 기타(오피스)이다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(국가기술표준원 보도자료 KDI 게재본 원문 열람, 2021-11-11). 속도 제어·보호 정지·높낮이차·틈새 극복·추락·넘어짐 방지를 확인했다. KS 번호는 자료에 없다. ref-948은 기존 id를 재사용했다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(공식 저장소 raw 원문 data/source_texts/ref-004.txt). 제어 수준별 플릿 어댑터(Full Control·Traffic Light·Read Only), 교통 일정 데이터베이스와 협상, rmf_task 작업 계획기, 문·승강기·디스펜서 인터페이스, 인용 구절을 확인했다. '참고 구조가 될 수 있다'는 추정이며 상업 시설 적용 사례는 미확인이다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "f1·f3·f4·f5·f7·f8·f10~f14·f16을 작업 대상별로 묶은 종합 추정이다. 각 형태에 근거 finding이 있다. 다섯째 형태(프런트·객실 응대)는 실패 사례 f16 하나에만 기댄다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "여섯 항목 대입 종합 추정이다. 완료·인계 칸을 근거 부족으로 비운 판단은 적절하다. 제약 칸의 f15는 강등됐으므로 [추정] 근거로만 쓴다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "분류 원문 19장 직접 범위에 사례를 대입한 추정이다. 요청 수신·배정·승강기 예약·혼잡 시간 제약·직원 인계·결과 반환은 19장의 ROP 쪽 열과 맞다. 공개 사례 미확인이라는 한계 표기도 적절하다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "'연계 대상:'으로 상위 업무 시스템·시설·설비 제어·로봇 자체 지능·업종별 조건을 19장 기준으로 나눴다. 범위 경계에 문제가 없다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "연결 영역 15개의 번호·이름이 부록 A 원문 명칭과 일치한다. 각 연결에 근거 finding이 있다. 13. 대화형 기능의 신뢰·기반 연결(f16 객실 음성 비서)은 약한 근거이며 연결 제안 수준으로만 쓴다. f15 강등에 따라 49. 사람 근접 안전·60. 노동·수용성·접근성 연결의 f15 근거는 [추정]으로 읽는다."
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
      "ref-103·ref-952·ref-953: 같은 날 2026-09-29-13 브리프(63. 병원·의료)가 같은 id를 비즈한국·품질경영학회지 논문·한국보건산업진흥원(다른 URL)에 부여했다. 참고문헌 목록 입력은 전체 950건이라 이번 id가 다음 빈 번호로 보이지만, 두 실행이 모두 게시되면 id 충돌이 생긴다. 퍼블리셔가 URL 기준으로 합칠 때 충돌 여부를 확인해야 한다.",
      "ref-945(국가기술표준원 KS 발표)은 2026-09-29-13 브리프와 같은 URL이다. 기존 id 재사용은 적절하며, 같은 주장은 63. 병원·의료 페이지의 각주를 재사용한다.",
      "ref-004(Open-RMF RMF Core)는 기존 각주를 재사용하며, 61. 물류창고·62. 제조 공장 페이지의 Open-RMF 서술과 같은 결론(현장 적용 사례 미확인)이라 모순이 없다."
    ]
  },
  "terminology": {
    "ok": false,
    "conflicts": [
      "'로봇친화형 건축물 인증'(용어 후보)과 '로봇 친화형 건축물 인증'(f17, 출처 기사 표기)의 띄어쓰기가 다르다. 출처 표기인 '로봇 친화형 건축물 인증'으로 통일한다.",
      "용어 후보 '로봇친화형 건축물 인증' 정의의 '25개 지표'가 출처 표현('25개 평가 범주(필수·부가)')과 다르다."
    ]
  },
  "quotation_check": {
    "ok": true
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "f15: [사실] → [추정]으로 강등한다. 본문에 '한국노동연구원 보고서(원문 미열람) 검색 요약 기준'임과 '조리로봇을 포함한 음식업 로봇 전반에 관한 지적'임을 밝힌다. 보고서 원문을 열지 못해 구체 진술을 검증하지 못했기 때문이다.",
    "f1: '배송 시간이 거의 두 배'를 '총 이동 시간이 거의 두 배(60노드에서 225초→500초)'로 고친다. '중국 호텔'은 '실제 호텔 배치 자료(3개 층 67실)'로 쓰고 소재국은 적지 않는다. 논문 지표가 total travel time이고 소재국은 열람 범위에서 확인되지 않았기 때문이다.",
    "f3: '222nm 자외선 방역로봇'을 '자외선 방역로봇'으로 쓴다. 기사 열람에서 파장 수치를 확인하지 못했기 때문이다. 기준일 2022-05-03을 밝히고, 현재 운영 여부는 확인되지 않았음을 적는다.",
    "f5: 운영 시간대를 '기사에 명시되지 않음'으로 쓰지 않는다. 기사는 '24시간 운영'을 적으므로 그것을 운영사 설명으로 옮긴다. 오염 감지·자동 물걸레 세척 같은 기능 서술을 쓰면 [추정]에 '벤더 주장'을 병기한다. 발행일 2025-04-02는 각주에 두되 검증에서 페이지로 재확인하지 못했음을 검증 노트에 남긴다.",
    "f16: '하우스텐보스'는 쓰지 않고 '나가사키'까지만 쓴다. '코 고는 소리를 명령으로 오인' 부분은 AI Incident Database(ref-962) 단독 각주로 단다. 두 출처 열람에서 하우스텐보스를 확인하지 못했고 코골이 사례는 한 출처에만 있기 때문이다.",
    "f17·용어 후보: '25개 지표'를 '25개 평가 범주(필수·부가)'로 고친다. 표기는 '로봇 친화형 건축물 인증'으로 통일한다. 이 인증 사례는 오피스(현장 유형 기타)이므로 5절 적용 사례에 넣지 않고 7절에서만 다룬다.",
    "f10: 보급 대수(5,000대·3,100대)는 '업체가 밝힌 값(지디넷코리아 보도)'으로 적는다. 독립 집계가 없기 때문이다.",
    "f4·f11: 본문에서 [추정]과 '벤더 주장' 병기를 유지하고 [사실]로 쓰지 않는다. 제조사 문서·회사 발표 단독이기 때문이다.",
    "f8·f15: 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고, reference_updates의 ref-954·ref-960 항목에 source_unopened: true를 넣는다.",
    "열린 질문 4번: '2025년 도입이 예고된 스마트+빌딩 인증과 어떤 관계인가' 부분을 뺀다. 이 제도의 존재와 시점을 뒷받침하는 finding이 브리프에 없기 때문이다. 질문은 '로봇 친화형 건축물 인증이 오피스를 넘어 호텔·쇼핑몰 같은 상업 시설로 확대됐는가?'로 줄인다.",
    "f6·f20·f21·f22·f23·f24: 종합 판단이므로 모두 [추정]으로 두고 각 문장에 근거 finding의 출처 각주를 단다. 9절의 직접 범위·연계 대상은 이 추정 문장으로만 서술한다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 23건, 미확인 1건, 교차 확인 1건(f16 헨나 호텔, 두 출처 모두 언론 보도 기반 2차 자료). 강등: f15 사실 → 추정(한국노동연구원 보고서 원문 미열람, 구체 진술 미확인). 원문 미열람 출처: ref-954, ref-960. 주의: 핵심 수치(f1·f2 호텔 경로 계획, f9 호텔 관리자 인식, f12·f13 노르웨이 식당)는 모두 단일 연구·단일 현장 자료이다. 보급 대수(f10)는 업체 발표 값이며, 승강기 API(f4)와 테이블오더 연동(f11)은 벤더 주장이다. 완료·인계(손님 수령 확인) 방식과 이기종 로봇을 한 계층으로 묶은 상업 시설 공개 사례는 확인되지 않았다. ref-103~ref-953은 같은 날 2026-09-29-13 브리프의 id와 겹칠 수 있어 게시 시 URL 대조가 필요하다. 검증 검색 4회(리서치 23회와 합쳐 27회/30).",
  "retry_reason": null
}
```

### runs/2026-09-29-16/pages.json

```json
{
  "run_id": "2026-09-29-16",
  "outline": [
    {
      "path": "docs/categories/site-type-applications/commercial-facilities.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 900,
      "summary": "상업 시설에서는 로봇이 손님과 같은 동선·승강기를 쓰는 영업 시간에 일하므로, 혼잡 시간·사람과의 충돌·직원 개입을 함께 다루는 운영이 성과를 가를 것으로 보인다. [추정][^ref-103][^ref-965][^ref-962]",
      "planned_findings": [
        "f10",
        "f12",
        "f16",
        "f9"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/commercial-facilities.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 900,
      "summary": "상업 시설 로봇 운영을 읽는 핵심 개념은 다중 운행 차량 경로 문제, 혼잡 시간, 로봇 친화형 건축물 인증, 서비스 삼자 관계, 반자율 네트워크 로봇 시스템, Open-RMF다. [추정][^ref-103][^ref-957][^ref-961][^ref-954]",
      "planned_findings": [
        "f1",
        "f2",
        "f17",
        "f14",
        "f8",
        "f19"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/commercial-facilities.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 3000,
      "summary": "상업 시설의 호텔 객실 배송, 식당 서빙, 매장·쇼핑몰 청소·재고 스캔·안내 세 사례를 여섯 항목으로 정리했고, 완료·인계(손님 수령 확인)는 대부분 미확인이다. [추정][^ref-952][^ref-965][^ref-953]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f7",
        "f8",
        "f10",
        "f11",
        "f12",
        "f13",
        "f14",
        "f15",
        "f16",
        "f18",
        "f20",
        "f21"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/commercial-facilities.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1400,
      "summary": "대표 접근법은 승강기 이용 방식(버튼 조작·클라우드 API·승강기 관리 솔루션), 혼잡 시간을 반영한 배송 계획, 주문 시스템 연동, 식당 도입 5단계, 직원·원격 조작자와의 역할 분담이다. [추정][^ref-103][^ref-952][^ref-959][^ref-965]",
      "planned_findings": [
        "f6",
        "f4",
        "f1",
        "f2",
        "f11",
        "f12",
        "f13",
        "f14",
        "f8"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/commercial-facilities.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 600,
      "summary": "KS 로봇 엘리베이터 탑승 안전 요구사항, 로봇 친화형 건축물 인증(첫 사례는 오피스), Open-RMF가 관련되며 상업 시설의 Open-RMF 적용 사례는 확인되지 않았다. [사실][^ref-945][^ref-957][^ref-004]",
      "planned_findings": [
        "f18",
        "f17",
        "f19"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/commercial-facilities.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 1200,
      "summary": "호텔 경로 계획, 호텔 관리자 인식, 식당 도입 사례, 식당 서비스 삼자 관계, 쇼핑몰 안내 로봇 현장 시험, 한국노동연구원 음식업 로봇 보고서, 헨나 호텔 기록이 대표 자료다. [사실][^ref-103][^ref-955][^ref-965]",
      "planned_findings": [
        "f1",
        "f9",
        "f12",
        "f14",
        "f8",
        "f15",
        "f16"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/commercial-facilities.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 1000,
      "summary": "ROP는 요청 수신·이기종 배정·승강기 예약·혼잡 시간 반영·직원 인계·결과 반환을 맡고, 객실 관리 시스템·POS·승강기 제어·로봇 자체 주행·업종 규정은 연계 대상으로 보인다. [추정][^ref-952][^ref-103][^ref-958]",
      "planned_findings": [
        "f22",
        "f23"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/commercial-facilities.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 1300,
      "summary": "승강기 연동(22), 업무 시스템(23), 관제 연동(20), 일정·공용 자원(26·28), 규모 설계(35), 사람 모델·안전(19·49), 협업·예외(31·32), 대화 신뢰(13), 시운전(55), 노동(60), 동향·경제성(1·3)과 이어진다. [추정][^ref-958][^ref-103][^ref-965]",
      "planned_findings": [
        "f24"
      ]
    },
    {
      "path": "docs/categories/site-type-applications/commercial-facilities.md",
      "section": "11. 열린 질문",
      "budget_chars": 600,
      "summary": "이기종 오케스트레이션 사례, 객실 관리 시스템 연동 구조, 매장 운영 시간대 규칙, 로봇 친화형 건축물 인증의 상업 시설 확대, 손님 수령 확인 방식이 열린 질문이다.",
      "planned_findings": [
        "f19",
        "f3",
        "f7",
        "f17",
        "f21"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/site-type-applications/commercial-facilities.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "섹션 3~11 신규 작성(seed → draft): 호텔 객실 배송·식당 서빙·매장·쇼핑몰 청소·재고 스캔·안내 세 사례를 여섯 항목으로 정리, 승강기 이용 방식·혼잡 시간 배송 계획·식당 도입 5단계, 책임 경계, 연결 영역 15개, 열린 질문 5건, 각주 17건, 1차 수정 지시 11건 이행"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area64-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 64. 상업 시설 의 \"8. 대표 연구와 자료\" 절(1,584자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area64-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 64. 상업 시설 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(1,122자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area64-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 64. 상업 시설 의 \"6. 대표 접근법과 기술\" 절(1,017자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area64-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 64. 상업 시설 의 \"4. 핵심 개념과 용어\" 절(1,000자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area64-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 64. 상업 시설 의 \"3. 왜 중요한가\" 절(726자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area64-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 64. 상업 시설 의 \"11. 열린 질문\" 절(694자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-29-area64-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 64. 상업 시설 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(636자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-29 | 64. 상업 시설 | 섹션 3~11 신규 작성(seed → draft): 호텔·식당·매장·쇼핑몰 적용 사례 3건, 승강기 이용 방식·혼잡 시간 배송 계획·책임 경계, 1차 수정 지시 11건 이행 | run 2026-09-29-16",
  "index_updates": {
    "home_recent": "2026-09-29 — 64. 상업 시설: 영역 심화 초안 작성(호텔 객실 배송·식당 서빙·매장·쇼핑몰 청소·안내 사례, 승강기 이용 방식, 책임 경계)",
    "category_recent": "2026-09-29 — 64. 상업 시설: 섹션 3~11 신규 작성(적용 사례 3건, 대표 연구 7건, 연결 영역 15개, 열린 질문 5건)",
    "area_recent": "2026-09-29 — 64. 상업 시설: 섹션 3~11 신규 작성(seed → draft), 각주 17건, 1차 수정 지시 11건 이행"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "multi-trip-vehicle-routing-problem",
      "term_ko": "다중 운행 차량 경로 문제",
      "term_en": "Multi-Trip Vehicle Routing Problem (MTVRP)",
      "definition": "적재 용량이 정해진 차량(로봇)이 한 거점에서 여러 번 출발·복귀하며 여러 목적지를 도는 경로를 정하는 차량 경로 문제의 변형이다.",
      "description": "다층 호텔의 로봇 객실 배송 계획에서 승강기를 암묵적 경유지로 넣어 모델링하고 적응형 대규모 이웃 탐색(ALNS)으로 푼 연구가 있다.",
      "related_areas": [
        64,
        26,
        35
      ],
      "sources": [
        "ref-103"
      ]
    },
    {
      "action": "new",
      "slug": "robot-friendly-building-certification",
      "term_ko": "로봇 친화형 건축물 인증",
      "term_en": "Robot-Friendly Building Certification",
      "definition": "스마트도시협회가 2022년 시작한 민간 인증으로, 건축·시설 설계, 네트워크·시스템, 건축 운영 관리, 로봇 지원·기타 서비스 4개 부문 25개 평가 범주(필수·부가)로 건물의 로봇 지원 수준을 최우수·우수·일반 등급으로 평가한다.",
      "description": "첫 대상은 네이버 제2사옥(1784, 오피스)이며 2022-04-06 현장 실사를 거쳐 최우수 등급을 받았다. 평가에는 이동형 서비스 로봇의 승강기 이동 지원과 로봇용 정밀지도·측위 인프라가 포함됐다. 호텔·쇼핑몰 같은 상업 시설 인증 사례는 확인되지 않았다.",
      "related_areas": [
        64,
        22
      ],
      "sources": [
        "ref-957"
      ]
    },
    {
      "action": "new",
      "slug": "service-triad",
      "term_ko": "서비스 삼자 관계",
      "term_en": "Service Triad (service robot, customer, frontline employee)",
      "definition": "서비스 로봇·고객·일선 직원 세 주체의 상호작용으로 서비스 가치를 설명하는 틀로, 로봇이 직원을 보완하는지 대체하는지와 직원 응대가 로봇의 기능 부족을 메우는지를 분석한다.",
      "related_areas": [
        64,
        31,
        60
      ],
      "sources": [
        "ref-961"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-004",
      "org": "Open Robotics",
      "title": "RMF Core Overview — Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/rmf-core.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "작업·교통 조율, Fleet Adapter, 설비 연동 구조 참고.",
      "cited_by": [
        "docs/categories/site-type-applications/commercial-facilities.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-945",
      "org": "산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재)",
      "title": "국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다",
      "published": "2021-11-11",
      "url": "https://eiec.kdi.re.kr/policy/materialView.do?num=220004",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "로봇의 엘리베이터 탑승 안전 요구사항과 실내 배송 로봇 KS 제정 발표(속도 제어·보호 정지·높낮이차·틈새 극복·추락·넘어짐 방지). 이번 실행에서 다시 열어 확인.",
      "cited_by": [
        "docs/categories/site-type-applications/commercial-facilities.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-103",
      "org": "Han, L., Ding, J., Liu, S., & Meng, M. (Sensors)",
      "title": "The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments",
      "published": "2025-03-13",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "다층 호텔의 다중 로봇 객실 배송을 승강기를 암묵적 경유지로 둔 다중 운행 차량 경로 문제로 모델링하고 ALNS 로 푼 동료 심사 논문(오픈 액세스 원문 열람).",
      "cited_by": [
        "docs/categories/site-type-applications/commercial-facilities.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-952",
      "org": "지디넷코리아 (윤상은)",
      "title": "엘베 타고 수건 배달·안내·방역도 '척척'...호텔로 간 로봇",
      "published": "2022-05-03",
      "url": "https://zdnet.co.kr/view/?no=20220503124850",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "국내 호텔(헨나호텔 명동, 코트야드 메리어트 타임스퀘어, 테이크호텔 광명, 노보텔 앰배서더 동대문, 롯데월드호텔, 안다즈 강남 등)의 배송·안내·방역 로봇 도입과 승강기 이용·호출 방식을 정리한 기사.",
      "cited_by": [
        "docs/categories/site-type-applications/commercial-facilities.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-953",
      "org": "Retail Dive (Sam Silverstein)",
      "title": "Sam's Club rolls out inventory-checking robots chainwide",
      "published": "2022-02-01",
      "url": "https://www.retaildive.com/news/sams-club-rolls-out-inventory-checking-robots-chainwide/618040/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "Sam's Club 이 약 600개 매장의 자율 바닥 청소기에 Brain Corp 재고 스캔 타워를 달아 청소와 재고 스캔을 함께 수행하게 한 전사 배치를 보도.",
      "cited_by": [
        "docs/categories/site-type-applications/commercial-facilities.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-954",
      "org": "Kanda, T., Shiomi, M., Miyashita, Z., Ishiguro, H., & Hagita, N. (IEEE Transactions on Robotics 26(5))",
      "title": "A Communication Robot in a Shopping Mall",
      "published": "2010-10",
      "url": "https://ieeexplore.ieee.org/abstract/document/5557825",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "원문 미열람. 쇼핑몰에서 쇼핑 정보·길 안내를 하는 커뮤니케이션 로봇의 25일 현장 시험(상호작용 2,642회)과 센서·원격 조작자를 결합한 반자율 네트워크 로봇 시스템을 보고한 논문. 서지는 Semantic Scholar API 로, 초록 내용은 검색 결과 요약으로만 확인.",
      "cited_by": [
        "docs/categories/site-type-applications/commercial-facilities.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-955",
      "org": "Ivanov, S., Seyitoğlu, F., & Markova, M. (Information Technology & Tourism)",
      "title": "Hotel managers' perceptions towards the use of robots: a mixed-methods approach",
      "published": "2020-09",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7486590/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "불가리아 호텔 관리자 설문 79명·면접 20명으로 로봇에 맞는 호텔 업무, 장단점 인식, 도입 의향과 장벽을 분석한 동료 심사 논문(오픈 액세스 원문 열람).",
      "cited_by": [
        "docs/categories/site-type-applications/commercial-facilities.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-956",
      "org": "지디넷코리아 (신영빈)",
      "title": "식당 음식 나르던 서빙로봇, 공장·창고로 진격",
      "published": "2024-07-30",
      "url": "https://zdnet.co.kr/view/?no=20240730115912",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "브이디컴퍼니·비로보틱스의 국내 서빙로봇 보급 대수·업장 수(업체가 밝힌 값)와 식당 외 분야(스크린골프장·야구장·물류센터·공장)로의 확장을 보도. 원 URL 연결이 끊겨 다음 뉴스 게재본으로 열었다.",
      "cited_by": [
        "docs/categories/site-type-applications/commercial-facilities.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-957",
      "org": "지디넷코리아 (김성현)",
      "title": "네이버 제2사옥, 로봇 친화형 건축물 인증 획득",
      "published": "2022-04-11",
      "url": "https://zdnet.co.kr/view/?no=20220411142336",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "스마트도시협회의 민간 로봇 친화형 건축물 인증(4개 부문 25개 평가 범주(필수·부가), 3개 등급)과 첫 대상 네이버 1784 의 최우수 등급 획득을 보도.",
      "cited_by": [
        "docs/categories/site-type-applications/commercial-facilities.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-958",
      "org": "Otis Elevator Company",
      "title": "Elevators and service robots",
      "published": null,
      "url": "https://www.otis.com/en/us/innovation/elevators-and-service-robots",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-29",
      "summary": "오티스의 승강기–서비스 로봇 연동(Otis Integrated Dispatch 클라우드 API)과 오사카 호텔 케이한 유니버설 타워 배송 로봇 적용을 소개하는 제조사 페이지. 기능·성과는 벤더 주장.",
      "cited_by": [
        "docs/categories/site-type-applications/commercial-facilities.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-959",
      "org": "이투데이 (구예지)",
      "title": "브이디컴퍼니, 신규 서빙로봇 3종 출시…“식당 전체 자동화 이룰 것”",
      "published": "2023-03-30",
      "url": "https://www.etoday.co.kr/news/view/2235962",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "브이디컴퍼니의 신규 서빙로봇(푸두봇 프로·스위프트봇·브이디셜틀)과 태블릿 주문–음료냉장고–서빙로봇 연동, 누적 공급 대수를 회사 발표 중심으로 보도.",
      "cited_by": [
        "docs/categories/site-type-applications/commercial-facilities.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-960",
      "org": "한국노동연구원 (박수민 외)",
      "title": "음식업 서비스 로봇 도입이 직무와 작업장 안전에 미치는 영향",
      "published": "2024",
      "url": "https://repository.kli.re.kr/bitstream/2021.oak/11632/2/(%EC%97%B0%EA%B5%AC%EB%B3%B4%EA%B3%A0)2024-13_%EC%9D%8C%EC%8B%9D%EC%97%85%20%EC%84%9C%EB%B9%84%EC%8A%A4%20%EB%A1%9C%EB%B4%87%20%EB%8F%84%EC%9E%85%EC%9D%B4%EC%A7%81%EB%AC%B4%EC%99%80%20%EC%9E%91%EC%97%85%EC%9E%A5%20%EC%95%88%EC%A0%84%EC%97%90%20%EB%AF%B8%EC%B9%98%EB%8A%94%20%EC%98%81%ED%96%A5.pdf",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "원문 미열람. 한국노동연구원 연구보고서 2024-13. 급식업 조리로봇과 외식업 서빙로봇 도입의 이유·조건, 직무·동선 변화, 작업장 안전 문제를 분석(보고서 PDF·저장소 페이지 403, 검색 결과 요약만 확인).",
      "cited_by": [
        "docs/categories/site-type-applications/commercial-facilities.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-961",
      "org": "Odekerken-Schröder, G., Mennens, K., Steins, M., & Mahr, D. (Journal of Service Management 33(2))",
      "title": "The service triad: an empirical study of service robots, customers and frontline employees",
      "published": "2022",
      "url": "https://www.emerald.com/josm/article/33/2/246/227998/The-service-triad-an-empirical-study-of-service",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "유럽 패스트 캐주얼 식당의 휴머노이드 서비스 로봇 2대에 대한 현장 고객 108명·실험 361명 조사로 로봇·고객·일선 직원 삼자 관계에서 보완·대체 효과를 분석한 동료 심사 논문(출판사 페이지의 초록 수준 확인).",
      "cited_by": [
        "docs/categories/site-type-applications/commercial-facilities.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-962",
      "org": "Responsible AI Collaborative (AI Incident Database)",
      "title": "Incident 346: Robots in Japanese Hotel Annoyed Guests and Failed to Handle Simple Tasks",
      "published": null,
      "url": "https://incidentdatabase.ai/cite/346/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "일본 헨나 호텔의 로봇 243대 운영과 2019년 절반 이상 감축, 객실 비서·여권 복사 등 실패를 여러 언론 보도를 묶어 기록한 AI 사고 데이터베이스 항목.",
      "cited_by": [
        "docs/categories/site-type-applications/commercial-facilities.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-963",
      "org": "Hotel Technology News",
      "title": "Score One for The Humans: Japan's Henn-na Hotel Fires Half Its Robot Workforce",
      "published": "2019-01",
      "url": "https://hoteltechnologynews.com/2019/01/score-one-for-the-humans-japans-henn-na-hotel-fires-half-its-robot-workforce/",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-29",
      "summary": "헨나 호텔이 로봇 243대 가운데 절반 이상을 줄인 경위(객실 비서 Churi, 짐 운반 로봇, 프런트 공룡 로봇의 실패와 직원 부담)를 전한 호텔 기술 전문지 기사. 1차 출처를 명시하지 않는다.",
      "cited_by": [
        "docs/categories/site-type-applications/commercial-facilities.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-964",
      "org": "서울경제 (백주연)",
      "title": "엘리베이터 타고 쇼핑몰 왔다갔다…바닥 물걸레질까지 하는 '로봇 청소부' 등장",
      "published": "2025-04-02",
      "url": "https://www.sedaily.com/article/14048085",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-29",
      "summary": "화성 동탄 상업시설 레이크 꼬모의 라이노스 AI 청소로봇 휠리 J40 도입과 클라우드 승강기 관리 솔루션 rEMS 를 통한 전 층 이동을 보도. 발행일은 1차 검증에서 기사 페이지로 재확인하지 못했다.",
      "cited_by": [
        "docs/categories/site-type-applications/commercial-facilities.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-965",
      "org": "Karlsen, A. S. T., Andersen, B., Nevstad, K., Heirsaunet, S. E., Indergård, E., & Aarseth, W. (Frontiers in Robotics and AI)",
      "title": "Digital transformation in restaurants: key aspects of service robot deployment from project initiation to evaluation",
      "published": "2026-04-22",
      "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2026.1793138/full",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-29",
      "summary": "노르웨이 식당 서비스 로봇 도입을 사업 착수·계획·통합·실행·평가 단계로 분석한 탐색·설명적 사례 연구(면접 22회·참여자 34명, 오픈 액세스 원문 열람).",
      "cited_by": [
        "docs/categories/site-type-applications/commercial-facilities.md"
      ],
      "source_unopened": false
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "호텔·쇼핑몰에서 제조사가 다른 배송·청소·안내 로봇을 하나의 오케스트레이션 계층(Open-RMF 등)으로 묶어 승강기를 함께 쓰게 한 국내외 공개 사례가 있는가?",
      "areas": [
        64,
        20,
        22
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "호텔 객실 배송 로봇이 객실 관리 시스템(PMS)이나 객실 전화에서 요청을 받고 배송 완료를 되돌려 주는 표준 인터페이스나 공개된 연동 구조가 있는가?",
      "areas": [
        64,
        23
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "영업 중인 매장·쇼핑몰에서 청소·재고 스캔 로봇을 손님이 많은 시간과 어떻게 나눠 운영하는지(운영 시간대 규칙과 그 효과)를 수치로 보인 연구나 공개 자료가 있는가?",
      "areas": [
        64,
        26
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "로봇 친화형 건축물 인증이 오피스를 넘어 호텔·쇼핑몰 같은 상업 시설로 확대됐는가?",
      "areas": [
        64,
        22
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "식당 서빙로봇과 호텔 배송 로봇은 손님이 음식·물품을 받았는지(완료·인계)를 어떤 방식(무게 감지·버튼·직원 확인·객실 문 앞 알림)으로 확인하며 그 결과가 주문 시스템에 기록되는가?",
      "areas": [
        64,
        17
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "상업 시설",
      "item": "시작 조건",
      "link": "docs/categories/site-type-applications/commercial-facilities.md#5-적용-사례-현장-유형-명시",
      "title": "64. 상업 시설"
    },
    {
      "site_type": "상업 시설",
      "item": "작업 대상",
      "link": "docs/categories/site-type-applications/commercial-facilities.md#5-적용-사례-현장-유형-명시",
      "title": "64. 상업 시설"
    },
    {
      "site_type": "상업 시설",
      "item": "수행 자원",
      "link": "docs/categories/site-type-applications/commercial-facilities.md#5-적용-사례-현장-유형-명시",
      "title": "64. 상업 시설"
    },
    {
      "site_type": "상업 시설",
      "item": "제약",
      "link": "docs/categories/site-type-applications/commercial-facilities.md#5-적용-사례-현장-유형-명시",
      "title": "64. 상업 시설"
    },
    {
      "site_type": "상업 시설",
      "item": "완료·인계",
      "link": "docs/categories/site-type-applications/commercial-facilities.md#5-적용-사례-현장-유형-명시",
      "title": "64. 상업 시설"
    },
    {
      "site_type": "상업 시설",
      "item": "예외·성과",
      "link": "docs/categories/site-type-applications/commercial-facilities.md#5-적용-사례-현장-유형-명시",
      "title": "64. 상업 시설"
    }
  ],
  "standards_updates": [
    {
      "name": "로봇 친화형 건축물 인증",
      "kind": "평가 프로그램",
      "org": "스마트도시협회",
      "url": "https://zdnet.co.kr/view/?no=20220411142336",
      "related_areas": [
        64,
        22
      ],
      "summary": "건축·시설 설계, 네트워크·시스템, 건축 운영 관리, 로봇 지원·기타 서비스 4개 부문 25개 평가 범주(필수·부가)로 건물의 로봇 지원 수준을 최우수·우수·일반 등급으로 평가하는 민간 인증. 첫 대상은 네이버 제2사옥(1784, 오피스)이며 2022-04-06 최우수 등급을 받았다(지디넷코리아 2022-04-11 보도 기준).",
      "ref_id": "ref-957"
    }
  ],
  "additional_research_requests": [
    "5절 완료·인계 칸: 식당 서빙로봇·호텔 배송 로봇이 손님 수령(테이블 전달·객실 문 앞 전달)을 무엇으로 확인하고 주문 시스템에 기록하는지에 관한 자료가 필요하다. 세 사례 모두 이 칸이 미확인이다.",
    "5절 매장·쇼핑몰 사례의 시작 조건: 청소·재고 스캔·안내 로봇 작업이 어떤 일정·호출로 시작되는지와 영업시간 중·후 운영 시간대(Sam's Club 등) 자료가 필요하다.",
    "7절: 로봇의 엘리베이터 탑승 안전 요구사항 KS 의 표준 번호·정식 명칭을 국가표준인증통합정보시스템 등 1차 자료로 확인해야 한다(ref-945 보도자료에는 번호가 없다).",
    "5·8절: 호텔 경로 계획(ref-103)·노르웨이 식당(ref-965)·호텔 관리자 인식(ref-955) 수치가 모두 단일 연구 자료이므로 교차 확인할 두 번째 출처가 필요하다.",
    "8절: 한국노동연구원 보고서(ref-960)와 Kanda 외 2010 논문(ref-954) 원문을 열어 검색 요약 수준에 머문 진술을 확인해야 한다.",
    "5절: 레이크 꼬모 기사(ref-964)의 발행일 2025-04-02를 기사 페이지로 다시 확인해야 한다.",
    "퍼블리셔 확인 요청: 이번 브리프는 국가기술표준원 KS 보도자료(https://eiec.kdi.re.kr/policy/materialView.do?num=220004)에 ref-945 을 썼으나, Q. 현장 유형별 적용 대분류 페이지의 자동 자료 목록에는 같은 제목·URL 이 ref-945 로, ref-945 은 비즈한국 병원 기사로 올라 있다. URL 기준으로 합칠 때 이 페이지의 [^ref-945] 각주를 기존 id 로 바꿔야 하는지 확인이 필요하다. ref-103~ref-953 도 같은 날 2026-09-29-13 실행 id 와 겹칠 수 있다."
  ],
  "fixes_applied": [
    "f15 강등 — 5절 식당 사례의 제약 칸과 서술, 8절 한국노동연구원 항목, 10절 19·49·60 연결을 모두 [추정]으로 쓰고, '원문 미열람 상태의 검색 요약 기준'임과 '조리로봇을 포함한 음식업 로봇 전반에 관한 지적'임을 본문에 밝혔다.",
    "f1 수정 — 5절 호텔 사례 제약 칸을 '총 이동 시간이 거의 두 배(고객 노드 60개에서 225초→500초)'로 쓰고 호텔은 '실제 호텔 배치 자료(3개 층 67실)'로만 적었다. 3·4·6·8절 어디에도 소재국을 쓰지 않았다.",
    "f3 수정 — 5절 호텔 사례 서술에서 '자외선 방역로봇'으로 쓰고 파장 수치를 뺐다. '2022-05-03 보도 기준'과 '지금도 운영 중인지는 확인되지 않았다'를 적었다.",
    "f5 수정 — 5절 매장·쇼핑몰 사례 서술에서 24시간 운영을 '운영사 설명에 따르면' [추정]으로 옮기고, 오염 감지·물걸레 세척 등 기능 서술을 [추정] 벤더 주장으로 썼다. 세부영역 페이지에는 검증 노트 절이 없어서, 발행일 2025-04-02를 1차 검증에서 다시 확인하지 못했다는 메모를 같은 서술과 reference_updates ref-964 요약에 남겼다.",
    "f16 수정 — 3절·5절에서 '하우스텐보스'를 쓰지 않고 '나가사키'까지만 썼으며, 코골이 오인 사례 문장은 ref-962 단독 각주로 달았다.",
    "f17·용어 후보 수정 — 4절·7절·용어집에서 '25개 평가 범주(필수·부가)'로 쓰고 표기를 '로봇 친화형 건축물 인증'으로 통일했다. 이 인증은 5절 적용 사례에 넣지 않고 4·7절(과 10절 22번 연결 근거)에서만 다뤘다.",
    "f10 수정 — 3절과 5절 식당 사례 서술에서 보급 대수 5,000대·3,100대를 '업체가 밝힌 값(지디넷코리아 보도)'으로 쓰고 독립 집계가 없음을 적었다.",
    "f4·f11 유지 — 5절·6절에서 오티스 OID·오사카 호텔(f4)과 브이디셜틀·스위프트봇(f11) 문장을 모두 [추정] 벤더 주장으로 쓰고 [사실]로 쓰지 않았다.",
    "f8·f15 각주 — 13절 ref-954·ref-960 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고, reference_updates 의 ref-954·ref-960 항목에 source_unopened: true 를 넣었다.",
    "열린 질문 4번 축약 — 11절과 open_question_updates 에서 스마트+빌딩 인증 부분을 빼고 '로봇 친화형 건축물 인증이 오피스를 넘어 호텔·쇼핑몰 같은 상업 시설로 확대됐는가?'로 줄였다.",
    "종합 판단 [추정] 유지 — f6(6절 승강기 이용 방식), f20(5절 첫 문단), f21(사례 표의 종합 칸), f22·f23(9절 표와 서술), f24(10절 각 줄)를 모두 [추정]으로 쓰고, 문장마다 근거 finding 의 출처 각주를 달았다. 9절의 직접 범위·연계 대상은 이 추정 문장과 분류원문 인용 한 줄로만 썼다.",
    "분량 초과 자동 분리: 64. 상업 시설 본문 11,678자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 5,814자"
  ]
}
```

### runs/2026-09-29-16/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 분량 초과 자동 분리:
    - docs/categories/site-type-applications/commercial-facilities.md "8. 대표 연구와 자료" → docs/topics/2026/2026-09-29-area64-s8.md (1,584자)
    - docs/categories/site-type-applications/commercial-facilities.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-09-29-area64-s10.md (1,122자)
    - docs/categories/site-type-applications/commercial-facilities.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-09-29-area64-s6.md (1,017자)
    - docs/categories/site-type-applications/commercial-facilities.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-09-29-area64-s4.md (1,000자)
    - docs/categories/site-type-applications/commercial-facilities.md "3. 왜 중요한가" → docs/topics/2026/2026-09-29-area64-s3.md (726자)
    - docs/categories/site-type-applications/commercial-facilities.md "11. 열린 질문" → docs/topics/2026/2026-09-29-area64-s11.md (694자)
    - docs/categories/site-type-applications/commercial-facilities.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-09-29-area64-s7.md (636자)
```

### runs/2026-09-29-16/pages/categories/site-type-applications/commercial-facilities.md

```markdown
---
title: "64. 상업 시설"
type: area
category: "Q. 현장 유형별 적용"
area_no: 64
related_areas: [1, 3, 13, 19, 20, 22, 23, 26, 28, 31, 32, 35, 49, 55, 60]
tags: [호텔 객실 배송, 서빙로봇, 승강기 연동, 혼잡 시간, 서비스 삼자 관계]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-29
sources: [ref-004, ref-945, ref-103, ref-952, ref-953, ref-954, ref-955, ref-956, ref-957, ref-958, ref-959, ref-960, ref-961, ref-962, ref-963, ref-964, ref-965]
last_run: 2026-09-29
version: 2
---

[홈](../../index.md) › [Q. 현장 유형별 적용](index.md) › 64. 상업 시설

# 64. 상업 시설

!!! info "소속 대분류"
    [Q. 현장 유형별 적용](index.md) — 핵심 질문:
    현장마다 다른 요구를 플랫폼이 어떻게 받아들이고, 실제로 어디에 어떻게 쓰이고 있는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

호텔 객실 배송, 식당 서빙, 매장·쇼핑몰 안내·청소 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **상업 시설 적용**: 호텔 객실 배송·식당 서빙·매장 안내·청소와 영업 시간에 맞춘 운영을 다룬다

## 2. 핵심 질문

손님이 있는 영업 시간에 호텔·식당·매장의 로봇을 어떻게 운영할 것인가? [분류원문]

## 3. 왜 중요한가

상업 시설에서는 로봇이 손님과 같은 동선·승강기를 쓰는 영업 시간에 일하므로, 로봇 한 대의 기능보다 혼잡 시간·사람과의 충돌·직원 개입을 함께 다루는 운영이 성과를 가를 것으로 보인다. [추정][^ref-103][^ref-965][^ref-962]

자세한 내용은 주제 페이지 [64. 상업 시설 — 왜 중요한가](../../topics/2026/2026-09-29-area64-s3.md)에 있다.

## 4. 핵심 개념과 용어

상업 시설 로봇 운영을 읽는 데 필요한 개념은 배송 계획 모델, 건물의 로봇 지원 평가, 로봇·손님·직원의 관계, 사람이 보완하는 반자율 운영이다. [추정][^ref-103][^ref-957][^ref-961][^ref-954]

자세한 내용은 주제 페이지 [64. 상업 시설 — 핵심 개념과 용어](../../topics/2026/2026-09-29-area64-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

상업 시설의 로봇 작업은 호텔 객실 배송, 식당 서빙·음료 전달, 매장·쇼핑몰·호텔 안내, 청소·방역과 재고 스캔, 프런트·객실 응대의 다섯 형태로 나타나며, 작업 대상에는 물건(비품·음식)·공간(바닥·공용 공간)·정보(선반 재고·가격)·사람(안내받는 손님)이 모두 들어간다. [추정][^ref-952][^ref-965][^ref-954][^ref-953][^ref-962] 아래 세 사례는 모두 실제 도입·연구 자료를 바탕으로 한다.

**현장 유형:** 상업 시설

**사례:** 호텔에서 비품·음식을 층간 이동해 객실로 배송

| 항목 | 내용 |
|---|---|
| 시작 조건 | 손님의 객실 호출에 따라 로봇이 객실을 순차 방문하거나(LG전자 클로이 서브봇), 객실 전화 시스템과 연동해 호출한다(현대로보틱스·KT N봇). [사실][^ref-952] |
| 작업 대상 | 층을 옮겨 객실로 가는 비품·음식이다. [추정][^ref-952] |
| 수행 자원 | 배송 로봇과 승강기다. 로보티즈 집개미는 로봇팔로 승강기 버튼을 직접 누르고, 클로이 서브봇은 최대 15kg을 싣는다. [사실][^ref-952] 오티스는 자사 클라우드 API(Otis Integrated Dispatch, OID)로 로봇이 승강기를 스스로 호출·탑승·층 선택한다고 설명한다. [추정] 벤더 주장[^ref-958] |
| 제약 | 손님과 함께 쓰는 승강기가 병목이다. 실제 호텔 배치 자료(3개 층 67실) 실험에서 승강기 운행 시간이 40초에서 100초로 늘면 총 이동 시간이 거의 두 배(고객 노드 60개에서 225초→500초)가 됐다. [사실][^ref-103] 아침 식사·체크아웃처럼 승강기 이용이 크게 늘어나는 시간대를 배송 계획에 고려해야 한다고 같은 논문은 제안한다. [사실][^ref-103] 국내에서는 로봇의 엘리베이터 탑승 안전 요구사항 KS 제정이 2021-11-11 발표됐다. [사실][^ref-945] |
| 완료·인계 | 미확인. 손님이 물건을 받았는지 확인하는 방식은 이번 자료에서 확인되지 않았다(11절 열린 질문). |
| 예외·성과 | 같은 실험에서 로봇이 5대를 넘으면 추가 로봇의 한계 이익이 크게 줄었다. [사실][^ref-103] 일본 헨나 호텔에서는 로봇이 해내지 못한 일을 직원이 계속 넘겨받아야 했다. [사실][^ref-962][^ref-963] |

국내 호텔에는 2022-05-03 보도 기준으로 로보티즈 집개미(명동 헨나호텔·코트야드 메리어트 타임스퀘어), LG전자 클로이 서브봇(광명 테이크호텔, 수원 바이 메리어트), 현대로보틱스·KT N봇(노보텔 앰배서더 동대문), 안내·도슨트·보안 순찰을 하는 LG전자 클로이 가이드봇(롯데월드호텔), KT 자외선 방역로봇(강남 안다즈호텔)이 도입됐다. [사실][^ref-952] 이 목록은 기사 한 건에 기댄 것이며, 지금도 운영 중인지는 확인되지 않았다.

해외에서는 오티스가 오사카의 호텔 케이한 유니버설 타워에서 2022-12부터 AIM Technologies의 배송 로봇이 승강기를 스스로 호출·탑승·층 선택해 24시간 객실 배송을 하고 야간에 최대 60건의 요청을 처리한다고 밝혔다. [추정] 벤더 주장[^ref-958]

예외 쪽에서는 헨나 호텔의 기록이 대표적이다. 객실 음성 비서 로봇이 기본 질문에 답하지 못했고, 짐 운반 로봇과 프런트 로봇이 여권 복사 같은 업무를 해내지 못해 사람 직원이 계속 개입해야 했다. [사실][^ref-962][^ref-963] 객실 비서가 코 고는 소리를 명령으로 오인해 손님을 깨운 사례도 기록돼 있다. [사실][^ref-962]

**현장 유형:** 상업 시설

**사례:** 식당에서 음식·음료를 주방·음료냉장고에서 테이블로 서빙

| 항목 | 내용 |
|---|---|
| 시작 조건 | 브이디컴퍼니는 손님이 테이블 태블릿으로 주류·음료를 주문하면 주문 정보가 음료냉장고로 전달되고 서빙로봇이 자동으로 받아 테이블로 나르는 브이디셜틀을 2023-03-30 발표했다. [추정] 벤더 주장[^ref-959] |
| 작업 대상 | 음식·음료다. 노르웨이 사례의 효과 계산은 1회에 접시 8개(각 약 2.2kg)를 나르는 조건을 썼다. [사실][^ref-965] |
| 수행 자원 | 서빙로봇(노르웨이 사례: 바퀴형·팔 없음·트레이 4단·적재 40kg)과 홀 직원이며, 사람 응대는 여전히 필수로 평가됐다. [사실][^ref-965] 유럽 식당 연구에서는 일선 직원의 높은 응대 품질이 로봇의 낮은 기능적 가치를 보완할 수 있었다. [사실][^ref-961] |
| 제약 | 계단·문턱 같은 건축 장애물이 없는 넓은 배치가 필요하고, 신축 단계에서 반영하면 개조 비용을 줄일 수 있다. [사실][^ref-965] 한국노동연구원 보고서는 원문 미열람 상태의 검색 요약 기준으로, 로봇 도입에 따른 작업 동선 변화가 사람과 사물의 충돌 위험을 만들고 설치·운행에 알맞은 물리적 공간이 필요하다고 지적한 것으로 보이며, 이는 조리로봇을 포함한 음식업 로봇 전반에 관한 지적이다. [추정][^ref-960] |
| 완료·인계 | 미확인. 테이블 전달을 무엇으로 확인하는지는 이번 자료에서 확인되지 않았다(11절 열린 질문). |
| 예외·성과 | 서빙로봇은 피크 시간과 예약 없는 대규모 테이블에서 가장 쓸모 있었고, 주방 가까운 구역은 직원이 직접 나르는 편이 빨랐다. [사실][^ref-965] 20인 테이블 기준 직원 왕복이 10회에서 2회로 줄어 약 320m 보행과 35.2kg 운반을 덜었다는 계산이 있으나, 단일 식당 관찰에 기댄 값이다. [사실][^ref-965] |

국내 서빙로봇은 업체가 밝힌 값으로 두 업체 합계 8,000대 이상이 공급됐다(3절). [사실][^ref-956] 브이디컴퍼니는 같은 발표에서 레이저로 이동 경로를 바닥에 표시하는 스위프트봇도 내놓았다. [추정] 벤더 주장[^ref-959] 노르웨이 사례에서는 직원 반발을 줄이려고 로봇을 '운반 보조'·'자동 카트'·건강·안전 조치로 소개했다. [사실][^ref-965]

코로나19 시기 유럽의 패스트 캐주얼 아시아 음식점에서 음료·요리를 나르는 휴머노이드 서비스 로봇 2대를 대상으로 현장 고객 108명과 실험 참가자 361명을 조사한 연구는, 기능이 뛰어난 로봇은 직원 지원 의존을 줄인다(대체)는 결과도 함께 보고했다. [사실][^ref-961] 한국노동연구원 보고서는 검색 요약 기준으로 조사 사업장에서 비상정지 버튼 활용 교육과 로봇 청소 시 안전이 미흡해 정기 교육이 필요하다고 본 것으로 보이나, 원문을 열지 못해 구체 진술은 검증되지 않았다. [추정][^ref-960]

**현장 유형:** 상업 시설

**사례:** 매장·쇼핑몰에서 바닥 청소·재고 스캔·손님 안내

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인. 청소·재고 스캔·안내 작업이 어떤 일정·호출로 시작되는지는 이번 자료에서 확인되지 않았다. |
| 작업 대상 | 바닥·공용 공간(공간), 선반의 가격 정확도·재고 수준·상품 진열 위치(정보), 쇼핑 정보·길 안내를 받는 손님(사람)이다. [사실][^ref-953][^ref-954] |
| 수행 자원 | Sam's Club은 미국 약 600개 매장에서 운영하던 자율 바닥 청소기(Tennant 제조, Brain Corp BrainOS 기반)에 재고 스캔 타워를 달아 청소와 재고 스캔을 한 로봇으로 수행하게 했다(2022-02-01 보도). [사실][^ref-953] 화성 동탄 상업시설 레이크 꼬모에서는 라이노스의 청소로봇 휠리 J40이 클라우드 승강기 관리 솔루션 rEMS로 전 층을 스스로 오간다. [사실][^ref-964] 쇼핑몰 안내 로봇은 일부를 원격 조작자가 맡았다. [사실][^ref-954] |
| 제약 | 쇼핑몰의 소음 속 음성 인식과 예상치 못한 지식 요구가 로봇 단독 운영을 어렵게 했다. [사실][^ref-954] 레이크 꼬모에서는 층간 이동을 승강기 관리 솔루션이 맡았다. [사실][^ref-964] Sam's Club 로봇이 영업시간 중·후 어느 시간대에 움직이는지는 보도에서 확인되지 않았다. |
| 완료·인계 | Sam's Club 로봇이 모은 가격 정확도·재고 수준·진열 위치 정보는 매장 관리자에게 전달된다. [사실][^ref-953] 작업 완료를 무엇으로 인정하는지는 미확인이다. |
| 예외·성과 | 쇼핑몰 안내 로봇은 25일간 현장 시험에서 2,642회의 상호작용을 모았다(원문 미열람, 초록 요약 기준). [사실][^ref-954] Sam's Club 로봇의 생산성 수치는 보도에 없다. |

Sam's Club 배치는 Brain Corp 재고 스캔 기술의 첫 상용 적용이자 최대 규모 배치로 소개됐다. [사실][^ref-953] 레이크 꼬모 운영사 우미에스테이트(우미건설 자산관리회사)는 이를 상업 공간 운영 모델로 확대하겠다고 밝혔다. [사실][^ref-964] 운영사 설명에 따르면 이 청소로봇은 24시간 운영된다. [추정][^ref-964] 로봇이 오염을 감지해 작업 강도를 조절하고 물 교환·오수 배수·물걸레 세척·건조를 스스로 한다는 설명은 운영사·제조사 설명을 옮긴 것이다. [추정] 벤더 주장[^ref-964] (기사 발행일 2025-04-02는 1차 검증에서 기사 페이지로 다시 확인하지 못했다.)

쇼핑몰 안내 로봇 연구(2010)는 쇼핑 정보 제공·길 안내·친밀감 형성을 맡은 커뮤니케이션 로봇이 바닥 센서·RFID로 사람을 감지·식별하고 일부를 원격 조작자가 맡는 반자율 방식을 택했다고 보고한다. [사실][^ref-954]

## 6. 대표 접근법과 기술

상업 시설의 대표 접근법은 승강기를 쓰는 방식, 혼잡 시간을 반영한 배송 계획, 주문 시스템과의 연동, 단계적 도입, 직원·원격 조작자와의 역할 분담으로 묶인다. [추정][^ref-103][^ref-952][^ref-959][^ref-965]

자세한 내용은 주제 페이지 [64. 상업 시설 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area64-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

상업 시설 로봇의 건물 이동과 관련해서는 승강기 탑승 안전 KS, 건물의 로봇 지원을 평가하는 민간 인증, 이기종 로봇을 잇는 Open-RMF가 확인됐다. [사실][^ref-945][^ref-957][^ref-004]

자세한 내용은 주제 페이지 [64. 상업 시설 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-29-area64-s7.md)에 있다.

## 8. 대표 연구와 자료

상업 시설 로봇 연구는 호텔 배송 계획, 운영자 인식, 식당 도입 과정, 로봇·고객·직원 관계, 쇼핑몰 현장 시험, 실패 사례 기록으로 나뉘며, 핵심 수치는 대부분 단일 연구·단일 현장 자료다. [추정][^ref-103][^ref-955][^ref-965]

자세한 내용은 주제 페이지 [64. 상업 시설 — 대표 연구와 자료](../../topics/2026/2026-09-29-area64-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

상업 시설에서 ROP가 직접 맡을 범위는 요청을 받아 제조사가 다른 로봇에 배정하고, 승강기를 예약해 혼잡 시간을 일정 제약으로 반영하며, 로봇이 못 하는 요청을 사람에게 넘기고 결과를 업무 시스템에 돌려주는 일로 보인다. [추정][^ref-952][^ref-103][^ref-954][^ref-953]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 객실 호출·테이블 주문·청소 일정 같은 요청을 받아 로봇에 배정하고, 완료와 재고 스캔 같은 수집 정보를 업무 시스템에 돌려준다. [추정][^ref-952][^ref-959][^ref-953] | 연계 대상: 호텔 객실 관리 시스템·식당 판매 시점 관리(Point of Sale, POS)·테이블오더·소매 재고 시스템의 메뉴·결제·재고 판단. [추정][^ref-959][^ref-953] |
| 로봇 자체 지능·제어 | 제조사가 다른 배송·서빙·청소·안내 로봇에 작업을 배정하고, 로봇이 처리하지 못하는 요청을 직원·원격 조작자에게 넘긴다. [추정][^ref-952][^ref-956][^ref-954][^ref-962] | 연계 대상: 로봇의 자율 주행·장애물 회피·음성 인식과 주행 안전 성능(로봇 제조사). [추정][^ref-952][^ref-954] |
| 시설·설비 제어 | 손님과 함께 쓰는 승강기를 예약하고, 아침 식사·체크아웃 같은 혼잡 시간을 배송·청소 일정의 제약으로 반영한다. [추정][^ref-103][^ref-958][^ref-964] | 연계 대상: 승강기 제어반, 제조사 승강기 API·승강기 관리 솔루션(승강기 업체). [추정][^ref-958][^ref-964] |
| 업종별 조건 | 업종 규정이 걸린 작업에는 작업 요청·예약·인계·상태 확인만 건다. [추정][^ref-959][^ref-952] | 연계 대상: 식품 위생·숙박 손님 개인정보 같은 업종 규정. [추정][^ref-959][^ref-952] |

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

요청 수신부터 결과 반환까지를 이기종 로봇에 걸쳐 하나의 계층으로 묶은 상업 시설 공개 사례는 이번 조사에서 확인되지 않았다. [추정][^ref-952][^ref-958][^ref-964] 경계 기준은 [범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 승강기·업무 시스템 연동, 일정·공용 자원 계획, 사람과의 협업·안전, 도입·수용성 영역과 이어진다. [추정][^ref-958][^ref-103][^ref-965]

자세한 내용은 주제 페이지 [64. 상업 시설 — 다른 연구영역과의 연결](../../topics/2026/2026-09-29-area64-s10.md)에 있다.

## 11. 열린 질문

이번 실행에서 확인하지 못한 운영 구조와 완료 확인 방식이 열린 질문으로 남았다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [64. 상업 시설 — 열린 질문](../../topics/2026/2026-09-29-area64-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-29

[^ref-945]: 산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11-11, https://eiec.kdi.re.kr/policy/materialView.do?num=220004, 접근일 2026-09-29

[^ref-103]: Han, L., Ding, J., Liu, S., & Meng, M. (Sensors), The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments, 2025-03-13, https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/, 접근일 2026-09-29

[^ref-952]: 지디넷코리아 (윤상은), 엘베 타고 수건 배달·안내·방역도 '척척'...호텔로 간 로봇, 2022-05-03, https://zdnet.co.kr/view/?no=20220503124850, 접근일 2026-09-29

[^ref-953]: Retail Dive (Sam Silverstein), Sam's Club rolls out inventory-checking robots chainwide, 2022-02-01, https://www.retaildive.com/news/sams-club-rolls-out-inventory-checking-robots-chainwide/618040/, 접근일 2026-09-29

[^ref-954]: Kanda, T., Shiomi, M., Miyashita, Z., Ishiguro, H., & Hagita, N. (IEEE Transactions on Robotics 26(5)), A Communication Robot in a Shopping Mall, 2010-10, https://ieeexplore.ieee.org/abstract/document/5557825, 접근일 2026-09-29 (원문 미열람)

[^ref-955]: Ivanov, S., Seyitoğlu, F., & Markova, M. (Information Technology & Tourism), Hotel managers' perceptions towards the use of robots: a mixed-methods approach, 2020-09, https://pmc.ncbi.nlm.nih.gov/articles/PMC7486590/, 접근일 2026-09-29

[^ref-956]: 지디넷코리아 (신영빈), 식당 음식 나르던 서빙로봇, 공장·창고로 진격, 2024-07-30, https://zdnet.co.kr/view/?no=20240730115912, 접근일 2026-09-29

[^ref-957]: 지디넷코리아 (김성현), 네이버 제2사옥, 로봇 친화형 건축물 인증 획득, 2022-04-11, https://zdnet.co.kr/view/?no=20220411142336, 접근일 2026-09-29

[^ref-958]: Otis Elevator Company, Elevators and service robots, 미확인, https://www.otis.com/en/us/innovation/elevators-and-service-robots, 접근일 2026-09-29

[^ref-959]: 이투데이 (구예지), 브이디컴퍼니, 신규 서빙로봇 3종 출시…“식당 전체 자동화 이룰 것”, 2023-03-30, https://www.etoday.co.kr/news/view/2235962, 접근일 2026-09-29

[^ref-960]: 한국노동연구원 (박수민 외), 음식업 서비스 로봇 도입이 직무와 작업장 안전에 미치는 영향, 2024, https://repository.kli.re.kr/bitstream/2021.oak/11632/2/(%EC%97%B0%EA%B5%AC%EB%B3%B4%EA%B3%A0)2024-13_%EC%9D%8C%EC%8B%9D%EC%97%85%20%EC%84%9C%EB%B9%84%EC%8A%A4%20%EB%A1%9C%EB%B4%87%20%EB%8F%84%EC%9E%85%EC%9D%B4%EC%A7%81%EB%AC%B4%EC%99%80%20%EC%9E%91%EC%97%85%EC%9E%A5%20%EC%95%88%EC%A0%84%EC%97%90%20%EB%AF%B8%EC%B9%98%EB%8A%94%20%EC%98%81%ED%96%A5.pdf, 접근일 2026-09-29 (원문 미열람)

[^ref-961]: Odekerken-Schröder, G., Mennens, K., Steins, M., & Mahr, D. (Journal of Service Management 33(2)), The service triad: an empirical study of service robots, customers and frontline employees, 2022, https://www.emerald.com/josm/article/33/2/246/227998/The-service-triad-an-empirical-study-of-service, 접근일 2026-09-29

[^ref-962]: Responsible AI Collaborative (AI Incident Database), Incident 346: Robots in Japanese Hotel Annoyed Guests and Failed to Handle Simple Tasks, 미확인, https://incidentdatabase.ai/cite/346/, 접근일 2026-09-29

[^ref-963]: Hotel Technology News, Score One for The Humans: Japan's Henn-na Hotel Fires Half Its Robot Workforce, 2019-01, https://hoteltechnologynews.com/2019/01/score-one-for-the-humans-japans-henn-na-hotel-fires-half-its-robot-workforce/, 접근일 2026-09-29

[^ref-964]: 서울경제 (백주연), 엘리베이터 타고 쇼핑몰 왔다갔다…바닥 물걸레질까지 하는 '로봇 청소부' 등장, 2025-04-02, https://www.sedaily.com/article/14048085, 접근일 2026-09-29

[^ref-965]: Karlsen, A. S. T., Andersen, B., Nevstad, K., Heirsaunet, S. E., Indergård, E., & Aarseth, W. (Frontiers in Robotics and AI), Digital transformation in restaurants: key aspects of service robot deployment from project initiation to evaluation, 2026-04-22, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2026.1793138/full, 접근일 2026-09-29
```

### docs/categories/site-type-applications/commercial-facilities.md

```markdown
---
title: "64. 상업 시설"
type: area
category: "Q. 현장 유형별 적용"
area_no: 64
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [Q. 현장 유형별 적용](index.md) › 64. 상업 시설

# 64. 상업 시설

!!! info "소속 대분류"
    [Q. 현장 유형별 적용](index.md) — 핵심 질문:
    현장마다 다른 요구를 플랫폼이 어떻게 받아들이고, 실제로 어디에 어떻게 쓰이고 있는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

호텔 객실 배송, 식당 서빙, 매장·쇼핑몰 안내·청소 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **상업 시설 적용**: 호텔 객실 배송·식당 서빙·매장 안내·청소와 영업 시간에 맞춘 운영을 다룬다

## 2. 핵심 질문

손님이 있는 영업 시간에 호텔·식당·매장의 로봇을 어떻게 운영할 것인가? [분류원문]

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

### runs/2026-09-29-16/pages/topics/2026/2026-09-29-area64-s8.md

```markdown
---
title: "64. 상업 시설 — 대표 연구와 자료"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 64
related_areas: [1, 3, 13, 19, 20, 22, 23, 26, 28, 31, 32, 35, 49, 55, 60]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-103, ref-954, ref-955, ref-960, ref-961, ref-962, ref-963, ref-965]
last_run: 2026-09-29
version: 1
split_from: docs/categories/site-type-applications/commercial-facilities.md#8
---

[홈](../../index.md) › [주제](../index.md) › 64. 상업 시설 — 대표 연구와 자료

# 64. 상업 시설 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 상업 시설 로봇 연구는 호텔 배송 계획, 운영자 인식, 식당 도입 과정, 로봇·고객·직원 관계, 쇼핑몰 현장 시험, 실패 사례 기록으로 나뉘며, 핵심 수치는 대부분 단일 연구·단일 현장 자료다. [추정][^ref-103][^ref-955][^ref-965]
- 이 페이지는 [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

상업 시설 로봇 연구는 호텔 배송 계획, 운영자 인식, 식당 도입 과정, 로봇·고객·직원 관계, 쇼핑몰 현장 시험, 실패 사례 기록으로 나뉘며, 핵심 수치는 대부분 단일 연구·단일 현장 자료다. [추정][^ref-103][^ref-955][^ref-965]

- Han, L.·Ding, J.·Liu, S.·Meng, M., The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments(Sensors, 2025) — 다층 호텔 객실 배송을 승강기를 경유지로 둔 MTVRP로 풀고, 승강기 운행 시간과 로봇 대수가 총 이동 시간에 주는 영향을 보였다. [사실][^ref-103]
- Ivanov, S.·Seyitoğlu, F.·Markova, M., Hotel managers' perceptions towards the use of robots: a mixed-methods approach(Information Technology & Tourism, 2020) — 불가리아 호텔 관리자(설문 79명·면접 20명)는 공용 공간 청소·세탁물 배송·결제 처리 같은 반복적이고 지저분한 업무를 로봇에 맞는 일로 보았고, 다국어 정보 제공 능력(평균 3.99/5)에 비해 손님 감정 이해(2.30/5)와 프로그램 밖 특별 요청 처리(2.08/5)를 낮게 평가했다. [사실][^ref-955]
- Karlsen, A. S. T. 외, Digital transformation in restaurants: key aspects of service robot deployment from project initiation to evaluation(Frontiers in Robotics and AI, 2026) — 노르웨이 식당 도입을 면접 22회·참여자 34명·관찰로 분석한 사례 연구로, 도입 동기·건축 요건·5단계 통합·피크 시간 효과를 다룬다. [사실][^ref-965]
- Odekerken-Schröder, G. 외, The service triad: an empirical study of service robots, customers and frontline employees(Journal of Service Management, 2022) — 보완·대체 효과와 함께, 의인화는 실용적 가치에, 사회적 존재감은 쾌락적 가치에 더 크게 작용했다고 보고한다. [사실][^ref-961]
- Kanda, T. 외, A Communication Robot in a Shopping Mall(IEEE Transactions on Robotics, 2010) — 쇼핑몰 안내 로봇의 25일 현장 시험과 반자율 네트워크 로봇 방식을 보고한 논문이며, 원문을 열지 못해 초록 요약 기준으로만 확인했다. [사실][^ref-954]
- 한국노동연구원 박수민 외, 음식업 서비스 로봇 도입이 직무와 작업장 안전에 미치는 영향(2024) — 급식업 조리로봇과 외식업 서빙로봇 도입의 직무·동선 변화와 작업장 안전을 다룬 연구보고서다. 원문을 열지 못해 검색 요약 범위만 확인했고, 안전 관련 지적은 조리로봇을 포함한 음식업 로봇 전반에 관한 것이다. [추정][^ref-960]
- AI Incident Database 346과 Hotel Technology News(2019) — 헨나 호텔 로봇 감축 경위를 기록한 두 자료로, 둘 다 2019년 언론 보도에 기댄 2차 자료다. [사실][^ref-962][^ref-963]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/commercial-facilities.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/commercial-facilities.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/commercial-facilities.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-103]: Han, L., Ding, J., Liu, S., & Meng, M. (Sensors), The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments, 2025-03-13, https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/, 접근일 2026-09-29
[^ref-954]: Kanda, T., Shiomi, M., Miyashita, Z., Ishiguro, H., & Hagita, N. (IEEE Transactions on Robotics 26(5)), A Communication Robot in a Shopping Mall, 2010-10, https://ieeexplore.ieee.org/abstract/document/5557825, 접근일 2026-09-29 (원문 미열람)
[^ref-955]: Ivanov, S., Seyitoğlu, F., & Markova, M. (Information Technology & Tourism), Hotel managers' perceptions towards the use of robots: a mixed-methods approach, 2020-09, https://pmc.ncbi.nlm.nih.gov/articles/PMC7486590/, 접근일 2026-09-29
[^ref-960]: 한국노동연구원 (박수민 외), 음식업 서비스 로봇 도입이 직무와 작업장 안전에 미치는 영향, 2024, https://repository.kli.re.kr/bitstream/2021.oak/11632/2/(%EC%97%B0%EA%B5%AC%EB%B3%B4%EA%B3%A0)2024-13_%EC%9D%8C%EC%8B%9D%EC%97%85%20%EC%84%9C%EB%B9%84%EC%8A%A4%20%EB%A1%9C%EB%B4%87%20%EB%8F%84%EC%9E%85%EC%9D%B4%EC%A7%81%EB%AC%B4%EC%99%80%20%EC%9E%91%EC%97%85%EC%9E%A5%20%EC%95%88%EC%A0%84%EC%97%90%20%EB%AF%B8%EC%B9%98%EB%8A%94%20%EC%98%81%ED%96%A5.pdf, 접근일 2026-09-29 (원문 미열람)
[^ref-961]: Odekerken-Schröder, G., Mennens, K., Steins, M., & Mahr, D. (Journal of Service Management 33(2)), The service triad: an empirical study of service robots, customers and frontline employees, 2022, https://www.emerald.com/josm/article/33/2/246/227998/The-service-triad-an-empirical-study-of-service, 접근일 2026-09-29
[^ref-962]: Responsible AI Collaborative (AI Incident Database), Incident 346: Robots in Japanese Hotel Annoyed Guests and Failed to Handle Simple Tasks, 미확인, https://incidentdatabase.ai/cite/346/, 접근일 2026-09-29
[^ref-963]: Hotel Technology News, Score One for The Humans: Japan's Henn-na Hotel Fires Half Its Robot Workforce, 2019-01, https://hoteltechnologynews.com/2019/01/score-one-for-the-humans-japans-henn-na-hotel-fires-half-its-robot-workforce/, 접근일 2026-09-29
[^ref-965]: Karlsen, A. S. T., Andersen, B., Nevstad, K., Heirsaunet, S. E., Indergård, E., & Aarseth, W. (Frontiers in Robotics and AI), Digital transformation in restaurants: key aspects of service robot deployment from project initiation to evaluation, 2026-04-22, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2026.1793138/full, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-16 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-16 | 64. 상업 시설 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-29-16/pages/topics/2026/2026-09-29-area64-s10.md

```markdown
---
title: "64. 상업 시설 — 다른 연구영역과의 연결"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 64
related_areas: [1, 3, 13, 19, 20, 22, 23, 26, 28, 31, 32, 35, 49, 55, 60]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-004, ref-945, ref-103, ref-953, ref-954, ref-955, ref-956, ref-957, ref-958, ref-959, ref-960, ref-961, ref-962, ref-963, ref-964, ref-965]
last_run: 2026-09-29
version: 1
split_from: docs/categories/site-type-applications/commercial-facilities.md#10
---

[홈](../../index.md) › [주제](../index.md) › 64. 상업 시설 — 다른 연구영역과의 연결

# 64. 상업 시설 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 승강기·업무 시스템 연동, 일정·공용 자원 계획, 사람과의 협업·안전, 도입·수용성 영역과 이어진다. [추정][^ref-958][^ref-103][^ref-965]
- 이 페이지는 [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 승강기·업무 시스템 연동, 일정·공용 자원 계획, 사람과의 협업·안전, 도입·수용성 영역과 이어진다. [추정][^ref-958][^ref-103][^ref-965]

- [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md) — 국내 서빙로봇 보급 규모와 다른 업종으로의 확장이 동향 자료다. [추정][^ref-956]
- [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md) — 호텔 관리자가 꼽은 비용·시설 개조 장벽과 식당 로봇의 가격대가 도입 경제성의 근거다. [추정][^ref-955][^ref-965]
- [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) — 헨나 호텔 객실 음성 비서의 실패는 대화형 기능의 신뢰 문제와 이어질 수 있다(연결 제안 수준). [추정][^ref-962]
- [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) — 쇼핑몰에서 사람을 감지·식별하는 센서 운영과 서빙 동선의 충돌 위험이 보행자 모델 요구로 이어진다. [추정][^ref-954][^ref-960]
- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) — 제조사가 다른 배송·청소·안내 로봇을 붙이는 참고 구조로 Open-RMF가 거론된다. [추정][^ref-004]
- [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) — 승강기 버튼 조작·승강기 API·승강기 관리 솔루션과 로봇 친화형 건축물 인증·KS 승강기 탑승 안전 요구가 이 영역의 연동 근거다. [추정][^ref-958][^ref-964][^ref-957][^ref-945]
- [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md) — 테이블오더 연동과 재고 스캔 정보 전달처럼 주문·재고 시스템과의 연동이 필요하다. [추정][^ref-959][^ref-953]
- [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md) — 아침 식사·체크아웃 혼잡 시간을 반영한 배송 일정 계획이 필요하다. [추정][^ref-103]
- [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) — 손님과 함께 쓰는 승강기가 공용 자원이다. [추정][^ref-103]
- [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md) — 홀 직원과 서빙로봇의 분담과 직원 응대의 보완 효과가 협업 설계로 이어진다. [추정][^ref-965][^ref-961]
- [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md) — 로봇 실패를 직원이 넘겨받은 헨나 호텔 사례가 예외 복구 설계의 근거다. [추정][^ref-962][^ref-963]
- [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md) — 로봇이 5대를 넘으면 한계 이익이 줄어든다는 결과가 대수 산정과 이어진다. [추정][^ref-103]
- [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md) — 서빙 동선의 충돌 위험과 비상정지 교육 지적(원문 미열람 보고서의 검색 요약 기준)이 사람 근접 안전과 이어진다. [추정][^ref-960]
- [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md) — 식당 도입의 시설 평가·지도 작성·시험 운행 단계가 현장 시운전 절차다. [추정][^ref-965]
- [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) — 호텔 관리자의 도입 의향, 직원 반발을 줄이는 소개 방식, 음식업 직무 변화가 수용성 문제다. [추정][^ref-955][^ref-965][^ref-960]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/commercial-facilities.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/commercial-facilities.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/commercial-facilities.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-29
[^ref-945]: 산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11-11, https://eiec.kdi.re.kr/policy/materialView.do?num=220004, 접근일 2026-09-29
[^ref-103]: Han, L., Ding, J., Liu, S., & Meng, M. (Sensors), The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments, 2025-03-13, https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/, 접근일 2026-09-29
[^ref-953]: Retail Dive (Sam Silverstein), Sam's Club rolls out inventory-checking robots chainwide, 2022-02-01, https://www.retaildive.com/news/sams-club-rolls-out-inventory-checking-robots-chainwide/618040/, 접근일 2026-09-29
[^ref-954]: Kanda, T., Shiomi, M., Miyashita, Z., Ishiguro, H., & Hagita, N. (IEEE Transactions on Robotics 26(5)), A Communication Robot in a Shopping Mall, 2010-10, https://ieeexplore.ieee.org/abstract/document/5557825, 접근일 2026-09-29 (원문 미열람)
[^ref-955]: Ivanov, S., Seyitoğlu, F., & Markova, M. (Information Technology & Tourism), Hotel managers' perceptions towards the use of robots: a mixed-methods approach, 2020-09, https://pmc.ncbi.nlm.nih.gov/articles/PMC7486590/, 접근일 2026-09-29
[^ref-956]: 지디넷코리아 (신영빈), 식당 음식 나르던 서빙로봇, 공장·창고로 진격, 2024-07-30, https://zdnet.co.kr/view/?no=20240730115912, 접근일 2026-09-29
[^ref-957]: 지디넷코리아 (김성현), 네이버 제2사옥, 로봇 친화형 건축물 인증 획득, 2022-04-11, https://zdnet.co.kr/view/?no=20220411142336, 접근일 2026-09-29
[^ref-958]: Otis Elevator Company, Elevators and service robots, 미확인, https://www.otis.com/en/us/innovation/elevators-and-service-robots, 접근일 2026-09-29
[^ref-959]: 이투데이 (구예지), 브이디컴퍼니, 신규 서빙로봇 3종 출시…“식당 전체 자동화 이룰 것”, 2023-03-30, https://www.etoday.co.kr/news/view/2235962, 접근일 2026-09-29
[^ref-960]: 한국노동연구원 (박수민 외), 음식업 서비스 로봇 도입이 직무와 작업장 안전에 미치는 영향, 2024, https://repository.kli.re.kr/bitstream/2021.oak/11632/2/(%EC%97%B0%EA%B5%AC%EB%B3%B4%EA%B3%A0)2024-13_%EC%9D%8C%EC%8B%9D%EC%97%85%20%EC%84%9C%EB%B9%84%EC%8A%A4%20%EB%A1%9C%EB%B4%87%20%EB%8F%84%EC%9E%85%EC%9D%B4%EC%A7%81%EB%AC%B4%EC%99%80%20%EC%9E%91%EC%97%85%EC%9E%A5%20%EC%95%88%EC%A0%84%EC%97%90%20%EB%AF%B8%EC%B9%98%EB%8A%94%20%EC%98%81%ED%96%A5.pdf, 접근일 2026-09-29 (원문 미열람)
[^ref-961]: Odekerken-Schröder, G., Mennens, K., Steins, M., & Mahr, D. (Journal of Service Management 33(2)), The service triad: an empirical study of service robots, customers and frontline employees, 2022, https://www.emerald.com/josm/article/33/2/246/227998/The-service-triad-an-empirical-study-of-service, 접근일 2026-09-29
[^ref-962]: Responsible AI Collaborative (AI Incident Database), Incident 346: Robots in Japanese Hotel Annoyed Guests and Failed to Handle Simple Tasks, 미확인, https://incidentdatabase.ai/cite/346/, 접근일 2026-09-29
[^ref-963]: Hotel Technology News, Score One for The Humans: Japan's Henn-na Hotel Fires Half Its Robot Workforce, 2019-01, https://hoteltechnologynews.com/2019/01/score-one-for-the-humans-japans-henn-na-hotel-fires-half-its-robot-workforce/, 접근일 2026-09-29
[^ref-964]: 서울경제 (백주연), 엘리베이터 타고 쇼핑몰 왔다갔다…바닥 물걸레질까지 하는 '로봇 청소부' 등장, 2025-04-02, https://www.sedaily.com/article/14048085, 접근일 2026-09-29
[^ref-965]: Karlsen, A. S. T., Andersen, B., Nevstad, K., Heirsaunet, S. E., Indergård, E., & Aarseth, W. (Frontiers in Robotics and AI), Digital transformation in restaurants: key aspects of service robot deployment from project initiation to evaluation, 2026-04-22, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2026.1793138/full, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-16 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-16 | 64. 상업 시설 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-29-16/pages/topics/2026/2026-09-29-area64-s6.md

```markdown
---
title: "64. 상업 시설 — 대표 접근법과 기술"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 64
related_areas: [1, 3, 13, 19, 20, 22, 23, 26, 28, 31, 32, 35, 49, 55, 60]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-103, ref-952, ref-954, ref-958, ref-959, ref-961, ref-964, ref-965]
last_run: 2026-09-29
version: 1
split_from: docs/categories/site-type-applications/commercial-facilities.md#6
---

[홈](../../index.md) › [주제](../index.md) › 64. 상업 시설 — 대표 접근법과 기술

# 64. 상업 시설 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 상업 시설의 대표 접근법은 승강기를 쓰는 방식, 혼잡 시간을 반영한 배송 계획, 주문 시스템과의 연동, 단계적 도입, 직원·원격 조작자와의 역할 분담으로 묶인다. [추정][^ref-103][^ref-952][^ref-959][^ref-965]
- 이 페이지는 [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

상업 시설의 대표 접근법은 승강기를 쓰는 방식, 혼잡 시간을 반영한 배송 계획, 주문 시스템과의 연동, 단계적 도입, 직원·원격 조작자와의 역할 분담으로 묶인다. [추정][^ref-103][^ref-952][^ref-959][^ref-965]

### 승강기 이용 방식

확인한 자료에서 상업 시설 로봇의 승강기 이용은 로봇팔로 버튼을 직접 누르는 방식(집개미), 제조사 클라우드 API로 승강기를 호출하는 방식(오티스 OID, 벤더 주장), 별도 승강기 관리 솔루션을 거치는 방식(레이크 꼬모 rEMS)으로 나뉜다. [추정][^ref-952][^ref-958][^ref-964] 방식마다 승강기 호출 권한과 손님과의 공유 규칙을 누가 정하는지가 달라질 것으로 보이나, 방식별 성능 비교 자료는 확인하지 못했다. [추정][^ref-952][^ref-958][^ref-964]

오티스는 OID가 API를 쓸 수 있는 어느 브랜드의 로봇과도 승강기 군 단위로 연동되고 1990년대 이후 설치된 자사 상업용 승강기 대부분과 호환된다고 주장한다. [추정] 벤더 주장[^ref-958] 같은 페이지는 로봇과 승객이 승강기를 함께 쓸 때의 우선순위·안전 규칙을 밝히지 않는다. [사실][^ref-958]

### 혼잡 시간을 반영한 다층 배송 계획

Han 외(2025)는 호텔 객실 배송을 MTVRP로 모델링해, 고객 노드 60개에서 ALNS가 14.15초에 해를 낸 반면 최적화 도구 Gurobi는 18,000초 이상 걸렸고 10~20노드 소규모 문제에서는 두 해가 일치했다고 보고했다. [사실][^ref-103] 논문은 혼잡 시간에 단방향 승강기 운행 같은 전략으로 병목을 줄이자고 제안하지만, 이는 실증 결과가 아니라 제안이다. [사실][^ref-103]

### 주문 시스템과 연동한 서빙

태블릿 주문–음료냉장고–서빙로봇을 잇는 브이디셜틀과 레이저로 이동 경로를 바닥에 표시하는 스위프트봇이 2023-03-30 발표됐다. [추정] 벤더 주장[^ref-959]

### 식당 도입 5단계

노르웨이 사례에서 통합은 시설 평가 → 수동 주행으로 공간 지도 작성 → 디지털 지도에 정차점·경로 지정 → 직원 관찰을 받는 며칠간의 시험 → 맞춤 설정의 5단계로 진행됐다. [사실][^ref-965]

### 직원·원격 조작자와의 역할 분담

노르웨이 연구는 로봇의 이동·배치 결정에 홀 직원이 참여해야 한다고 결론지었다. [사실][^ref-965] 유럽 식당 연구에서는 로봇의 기능이 낮을 때 직원 응대가 이를 보완했고(보완), 기능이 뛰어난 로봇은 직원 지원 의존을 줄였다(대체). [사실][^ref-961] 쇼핑몰 안내 로봇은 소음 속 음성 인식의 어려움을 피하려고 일부를 원격 조작자가 맡는 반자율 방식을 택했다. [사실][^ref-954]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/commercial-facilities.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/commercial-facilities.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/commercial-facilities.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-103]: Han, L., Ding, J., Liu, S., & Meng, M. (Sensors), The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments, 2025-03-13, https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/, 접근일 2026-09-29
[^ref-952]: 지디넷코리아 (윤상은), 엘베 타고 수건 배달·안내·방역도 '척척'...호텔로 간 로봇, 2022-05-03, https://zdnet.co.kr/view/?no=20220503124850, 접근일 2026-09-29
[^ref-954]: Kanda, T., Shiomi, M., Miyashita, Z., Ishiguro, H., & Hagita, N. (IEEE Transactions on Robotics 26(5)), A Communication Robot in a Shopping Mall, 2010-10, https://ieeexplore.ieee.org/abstract/document/5557825, 접근일 2026-09-29 (원문 미열람)
[^ref-958]: Otis Elevator Company, Elevators and service robots, 미확인, https://www.otis.com/en/us/innovation/elevators-and-service-robots, 접근일 2026-09-29
[^ref-959]: 이투데이 (구예지), 브이디컴퍼니, 신규 서빙로봇 3종 출시…“식당 전체 자동화 이룰 것”, 2023-03-30, https://www.etoday.co.kr/news/view/2235962, 접근일 2026-09-29
[^ref-961]: Odekerken-Schröder, G., Mennens, K., Steins, M., & Mahr, D. (Journal of Service Management 33(2)), The service triad: an empirical study of service robots, customers and frontline employees, 2022, https://www.emerald.com/josm/article/33/2/246/227998/The-service-triad-an-empirical-study-of-service, 접근일 2026-09-29
[^ref-964]: 서울경제 (백주연), 엘리베이터 타고 쇼핑몰 왔다갔다…바닥 물걸레질까지 하는 '로봇 청소부' 등장, 2025-04-02, https://www.sedaily.com/article/14048085, 접근일 2026-09-29
[^ref-965]: Karlsen, A. S. T., Andersen, B., Nevstad, K., Heirsaunet, S. E., Indergård, E., & Aarseth, W. (Frontiers in Robotics and AI), Digital transformation in restaurants: key aspects of service robot deployment from project initiation to evaluation, 2026-04-22, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2026.1793138/full, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-16 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-16 | 64. 상업 시설 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-29-16/pages/topics/2026/2026-09-29-area64-s4.md

```markdown
---
title: "64. 상업 시설 — 핵심 개념과 용어"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 64
related_areas: [1, 3, 13, 19, 20, 22, 23, 26, 28, 31, 32, 35, 49, 55, 60]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-004, ref-103, ref-954, ref-957, ref-961]
last_run: 2026-09-29
version: 1
split_from: docs/categories/site-type-applications/commercial-facilities.md#4
---

[홈](../../index.md) › [주제](../index.md) › 64. 상업 시설 — 핵심 개념과 용어

# 64. 상업 시설 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 상업 시설 로봇 운영을 읽는 데 필요한 개념은 배송 계획 모델, 건물의 로봇 지원 평가, 로봇·손님·직원의 관계, 사람이 보완하는 반자율 운영이다. [추정][^ref-103][^ref-957][^ref-961][^ref-954]
- 이 페이지는 [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

상업 시설 로봇 운영을 읽는 데 필요한 개념은 배송 계획 모델, 건물의 로봇 지원 평가, 로봇·손님·직원의 관계, 사람이 보완하는 반자율 운영이다. [추정][^ref-103][^ref-957][^ref-961][^ref-954]

- **다중 운행 차량 경로 문제(Multi-Trip Vehicle Routing Problem, MTVRP)** — 적재 용량이 정해진 로봇이 한 거점에서 여러 번 출발·복귀하며 여러 목적지를 도는 경로 문제로, Han 외(2025)는 다층 호텔 객실 배송에서 승강기를 암묵적 경유지로 두고 적응형 대규모 이웃 탐색(Adaptive Large Neighborhood Search, ALNS)으로 풀었다. [사실][^ref-103]
- **혼잡 시간(peak period)** — 아침 식사·체크아웃처럼 호텔 승강기 이용이 크게 늘어나는 시간대로, 같은 논문은 이를 배송 계획에 고려하라고 제안한다. [사실][^ref-103]
- **로봇 친화형 건축물 인증(Robot-Friendly Building Certification)** — 스마트도시협회가 시행하는 민간 인증으로, 건축·시설 설계, 네트워크·시스템, 건축 운영 관리, 로봇 지원·기타 서비스의 4개 부문 25개 평가 범주(필수·부가)로 최우수·우수·일반 등급을 매긴다(2022-04-11 보도 기준). [사실][^ref-957]
- **서비스 삼자 관계(Service Triad)** — 서비스 로봇·고객·일선 직원 세 주체의 상호작용으로 서비스 가치를 설명하는 틀로, 직원 응대가 로봇의 부족한 기능을 보완하는지, 로봇이 직원 지원을 대체하는지를 본다. [사실][^ref-961]
- **반자율 네트워크 로봇 시스템** — 로봇의 부족한 감지·지식을 곳곳의 센서(바닥 센서·무선 인식(Radio-Frequency Identification, RFID))와 원격 조작자가 보완하는 운영 방식으로, 쇼핑몰 안내 로봇 현장 시험에서 쓰였다. [사실][^ref-954]
- **[오픈 RMF](../../glossary/open-rmf.md)(Open-RMF)** — 코어가 서로 다른 제조사 플릿을 제어 수준별로 붙이는 [플릿 어댑터](../../glossary/fleet-adapter.md), 교통 일정 데이터베이스와 충돌 협상, 작업 배정, 문·승강기·디스펜서 같은 건물 설비의 표준 인터페이스를 제공한다. [사실][^ref-004]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/commercial-facilities.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/commercial-facilities.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/commercial-facilities.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-29
[^ref-103]: Han, L., Ding, J., Liu, S., & Meng, M. (Sensors), The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments, 2025-03-13, https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/, 접근일 2026-09-29
[^ref-954]: Kanda, T., Shiomi, M., Miyashita, Z., Ishiguro, H., & Hagita, N. (IEEE Transactions on Robotics 26(5)), A Communication Robot in a Shopping Mall, 2010-10, https://ieeexplore.ieee.org/abstract/document/5557825, 접근일 2026-09-29 (원문 미열람)
[^ref-957]: 지디넷코리아 (김성현), 네이버 제2사옥, 로봇 친화형 건축물 인증 획득, 2022-04-11, https://zdnet.co.kr/view/?no=20220411142336, 접근일 2026-09-29
[^ref-961]: Odekerken-Schröder, G., Mennens, K., Steins, M., & Mahr, D. (Journal of Service Management 33(2)), The service triad: an empirical study of service robots, customers and frontline employees, 2022, https://www.emerald.com/josm/article/33/2/246/227998/The-service-triad-an-empirical-study-of-service, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-16 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-16 | 64. 상업 시설 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-29-16/pages/topics/2026/2026-09-29-area64-s3.md

```markdown
---
title: "64. 상업 시설 — 왜 중요한가"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 64
related_areas: [1, 3, 13, 19, 20, 22, 23, 26, 28, 31, 32, 35, 49, 55, 60]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-103, ref-954, ref-955, ref-956, ref-962, ref-963, ref-965]
last_run: 2026-09-29
version: 1
split_from: docs/categories/site-type-applications/commercial-facilities.md#3
---

[홈](../../index.md) › [주제](../index.md) › 64. 상업 시설 — 왜 중요한가

# 64. 상업 시설 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 상업 시설에서는 로봇이 손님과 같은 동선·승강기를 쓰는 영업 시간에 일하므로, 로봇 한 대의 기능보다 혼잡 시간·사람과의 충돌·직원 개입을 함께 다루는 운영이 성과를 가를 것으로 보인다. [추정][^ref-103][^ref-965][^ref-962]
- 이 페이지는 [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

상업 시설에서는 로봇이 손님과 같은 동선·승강기를 쓰는 영업 시간에 일하므로, 로봇 한 대의 기능보다 혼잡 시간·사람과의 충돌·직원 개입을 함께 다루는 운영이 성과를 가를 것으로 보인다. [추정][^ref-103][^ref-965][^ref-962]

이 현장에 들어온 로봇의 수는 적지 않다. 국내 서빙로봇 업체가 밝힌 값(지디넷코리아 보도)으로는 브이디컴퍼니가 2023년 말까지 약 3,000개 업장에 5,000대, 비로보틱스가 2024년 3월 말 기준 약 2,000개 업장에 3,100대를 공급했으며, 독립 집계는 없다. [사실][^ref-956] 같은 보도는 서빙로봇의 쓰임이 식당을 넘어 스크린골프장·야구장·당구장·인쇄소·문화공간과 물류센터·중소형 공장으로 넓어지고 있다고 전한다. [사실][^ref-956] 노르웨이 식당 사례 연구에서 도입 동기는 인력 부족·직원 건강·안전·비용이었다. [사실][^ref-965]

로봇을 들이고도 사람의 일이 늘어난 사례도 있다. 2015년 나가사키에 문을 연 일본 헨나 호텔은 2019년 1월 로봇 243대 가운데 절반 이상을 줄였고, 두 기록 모두 로봇이 직원 업무를 줄이기보다 늘렸다고 전한다. [사실][^ref-962][^ref-963] 불가리아 호텔 관리자 조사(2018-12~2019-04)에서는 응답자 약 63%가 로봇 도입 의향이 없고 1년 안 도입 계획은 3.8%였으며, 비용·시설 개조·유지보수·서비스 품질 저하가 장벽으로 꼽혔다. [사실][^ref-955]

그래서 이 영역의 핵심 질문은 로봇을 몇 대 들이느냐보다, 로봇이 못 하는 요청을 직원·원격 조작자가 어떻게 넘겨받고 손님과 함께 쓰는 승강기·동선을 어떻게 나눠 쓰느냐의 문제로 읽힌다. [추정][^ref-103][^ref-954][^ref-965]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/commercial-facilities.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/commercial-facilities.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/commercial-facilities.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-103]: Han, L., Ding, J., Liu, S., & Meng, M. (Sensors), The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments, 2025-03-13, https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/, 접근일 2026-09-29
[^ref-954]: Kanda, T., Shiomi, M., Miyashita, Z., Ishiguro, H., & Hagita, N. (IEEE Transactions on Robotics 26(5)), A Communication Robot in a Shopping Mall, 2010-10, https://ieeexplore.ieee.org/abstract/document/5557825, 접근일 2026-09-29 (원문 미열람)
[^ref-955]: Ivanov, S., Seyitoğlu, F., & Markova, M. (Information Technology & Tourism), Hotel managers' perceptions towards the use of robots: a mixed-methods approach, 2020-09, https://pmc.ncbi.nlm.nih.gov/articles/PMC7486590/, 접근일 2026-09-29
[^ref-956]: 지디넷코리아 (신영빈), 식당 음식 나르던 서빙로봇, 공장·창고로 진격, 2024-07-30, https://zdnet.co.kr/view/?no=20240730115912, 접근일 2026-09-29
[^ref-962]: Responsible AI Collaborative (AI Incident Database), Incident 346: Robots in Japanese Hotel Annoyed Guests and Failed to Handle Simple Tasks, 미확인, https://incidentdatabase.ai/cite/346/, 접근일 2026-09-29
[^ref-963]: Hotel Technology News, Score One for The Humans: Japan's Henn-na Hotel Fires Half Its Robot Workforce, 2019-01, https://hoteltechnologynews.com/2019/01/score-one-for-the-humans-japans-henn-na-hotel-fires-half-its-robot-workforce/, 접근일 2026-09-29
[^ref-965]: Karlsen, A. S. T., Andersen, B., Nevstad, K., Heirsaunet, S. E., Indergård, E., & Aarseth, W. (Frontiers in Robotics and AI), Digital transformation in restaurants: key aspects of service robot deployment from project initiation to evaluation, 2026-04-22, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2026.1793138/full, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-16 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-16 | 64. 상업 시설 의 "왜 중요한가" 절에서 분리 |
```

### runs/2026-09-29-16/pages/topics/2026/2026-09-29-area64-s11.md

```markdown
---
title: "64. 상업 시설 — 열린 질문"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 64
related_areas: [1, 3, 13, 19, 20, 22, 23, 26, 28, 31, 32, 35, 49, 55, 60]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: []
last_run: 2026-09-29
version: 1
split_from: docs/categories/site-type-applications/commercial-facilities.md#11
---

[홈](../../index.md) › [주제](../index.md) › 64. 상업 시설 — 열린 질문

# 64. 상업 시설 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이번 실행에서 확인하지 못한 운영 구조와 완료 확인 방식이 열린 질문으로 남았다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이번 실행에서 확인하지 못한 운영 구조와 완료 확인 방식이 열린 질문으로 남았다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- (열림 · 제기 2026-09-29 · 실행 2026-09-29-16) 호텔·쇼핑몰에서 제조사가 다른 배송·청소·안내 로봇을 하나의 오케스트레이션 계층(Open-RMF 등)으로 묶어 승강기를 함께 쓰게 한 국내외 공개 사례가 있는가?
- (열림 · 제기 2026-09-29 · 실행 2026-09-29-16) 호텔 객실 배송 로봇이 객실 관리 시스템(PMS)이나 객실 전화에서 요청을 받고 배송 완료를 되돌려 주는 표준 인터페이스나 공개된 연동 구조가 있는가?
- (열림 · 제기 2026-09-29 · 실행 2026-09-29-16) 영업 중인 매장·쇼핑몰에서 청소·재고 스캔 로봇을 손님이 많은 시간과 어떻게 나눠 운영하는지(운영 시간대 규칙과 그 효과)를 수치로 보인 연구나 공개 자료가 있는가?
- (열림 · 제기 2026-09-29 · 실행 2026-09-29-16) 로봇 친화형 건축물 인증이 오피스를 넘어 호텔·쇼핑몰 같은 상업 시설로 확대됐는가?
- (열림 · 제기 2026-09-29 · 실행 2026-09-29-16) 식당 서빙로봇과 호텔 배송 로봇은 손님이 음식·물품을 받았는지(완료·인계)를 어떤 방식(무게 감지·버튼·직원 확인·객실 문 앞 알림)으로 확인하며 그 결과가 주문 시스템에 기록되는가?

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/commercial-facilities.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/commercial-facilities.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/commercial-facilities.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

이 절에는 각주가 없다.

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-16 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-16 | 64. 상업 시설 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-29-16/pages/topics/2026/2026-09-29-area64-s7.md

```markdown
---
title: "64. 상업 시설 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "Q. 현장 유형별 적용"
primary_area_no: 64
related_areas: [1, 3, 13, 19, 20, 22, 23, 26, 28, 31, 32, 35, 49, 55, 60]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-29
updated: 2026-09-29
sources: [ref-004, ref-945, ref-957]
last_run: 2026-09-29
version: 1
split_from: docs/categories/site-type-applications/commercial-facilities.md#7
---

[홈](../../index.md) › [주제](../index.md) › 64. 상업 시설 — 관련 표준·프레임워크·오픈소스

# 64. 상업 시설 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 상업 시설 로봇의 건물 이동과 관련해서는 승강기 탑승 안전 KS, 건물의 로봇 지원을 평가하는 민간 인증, 이기종 로봇을 잇는 Open-RMF가 확인됐다. [사실][^ref-945][^ref-957][^ref-004]
- 이 페이지는 [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

상업 시설 로봇의 건물 이동과 관련해서는 승강기 탑승 안전 KS, 건물의 로봇 지원을 평가하는 민간 인증, 이기종 로봇을 잇는 Open-RMF가 확인됐다. [사실][^ref-945][^ref-957][^ref-004]

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| KS 로봇의 엘리베이터 탑승 안전 요구사항·실내 배송 로봇(표준 번호 미확인) | 표준 | 2021-11-11 제정 발표. 건물 안을 이동하는 로봇이 사람과 안전하게 접촉하도록 속도 제어·위험 상황의 보호 정지·높낮이차·틈새 극복·추락·넘어짐 방지를 다룬다. 적용 건물 유형은 특정하지 않는다. [사실] | [^ref-945] |
| 로봇 친화형 건축물 인증 | 평가 프로그램 | 스마트도시협회 민간 인증으로 첫 대상 네이버 제2사옥(1784)이 2022-04-06 현장 실사를 거쳐 최우수 등급을 받았고, 이동형 서비스 로봇의 승강기 이동 지원과 로봇용 정밀지도·측위 인프라가 평가됐다. 첫 사례는 오피스(현장 유형 기타)이며 호텔·쇼핑몰 인증 사례는 확인되지 않았다. [사실] | [^ref-957] |
| Open-RMF | 오픈소스 | 제조사가 다른 배송·청소·안내 로봇이 승강기를 함께 쓰는 호텔·쇼핑몰의 참고 구조가 될 수 있으나, 호텔·식당·쇼핑몰 적용 사례는 확인되지 않았다. [추정] | [^ref-004] |

전체 표준 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/site-type-applications/commercial-facilities.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/site-type-applications/commercial-facilities.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [23. 업무 시스템 연동](../../categories/integration/business-system-integration.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [28. 공용 자원·충전·에너지 최적화](../../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [35. 처리능력·규모·배치 설계](../../categories/design-and-simulation/capacity-sizing-and-layout-design.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/site-type-applications/commercial-facilities.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-29
[^ref-945]: 산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11-11, https://eiec.kdi.re.kr/policy/materialView.do?num=220004, 접근일 2026-09-29
[^ref-957]: 지디넷코리아 (김성현), 네이버 제2사옥, 로봇 친화형 건축물 인증 획득, 2022-04-11, https://zdnet.co.kr/view/?no=20220411142336, 접근일 2026-09-29

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-29-16 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-29 | 2026-09-29-16 | 64. 상업 시설 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 950건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 253개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- aas-registry-and-discovery: 자산관리셸 레지스트리·디스커버리 (AAS Registry / Discovery)
- ablation-study: 절제 실험 (Ablation Study)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- agentic-ai: 에이전틱 AI (Agentic AI)
- aggregation-event: 집계 이벤트 (AggregationEvent)
- agv-technical-data-submodel: AGV 기술 데이터 서브모델 (Technical Data for AGV in Intralogistics (IDTA 02047))
- amr-assisted-order-picking: AMR 협업 피킹 (AMR-assisted Order Picking)
- approval-fatigue: 승인 피로 (Approval Fatigue (Consent Fatigue))
- ariac: 산업 자동화용 민첩 로봇 경진대회 (Agile Robotics for Industrial Automation Competition (ARIAC))
- artificial-intelligence-management-system: AI 관리 시스템 (Artificial Intelligence Management System (AIMS))
- assembly-line-feeding-problem: 조립라인 공급 문제 (Assembly Line Feeding Problem (ALFP))
- asset-administration-shell: 자산관리셸 (Asset Administration Shell (AAS))
- association-event: 연결 이벤트 (AssociationEvent)
- attribute-based-access-control: 속성 기반 접근 통제 (Attribute-Based Access Control (ABAC))
- audit-trail: 감사 추적 (Audit Trail)
- automatic-simulation-model-generation: 자동 시뮬레이션 모델 생성 (Automatic Simulation Model Generation (ASMG))
- automation-bias: 자동화 편향 (Automation Bias)
- b2mml: B2MML (Business To Manufacturing Markup Language (B2MML))
- bag-file: 백 파일 (Bag File (rosbag2))
- battery-swapping: 배터리 교환 (Battery Swapping)
- behavior-tree: 행동 트리 (Behavior Tree)
- block-reference: 블록 참조 (Block Reference (INSERT))
- bpmn: 비즈니스 프로세스 모델 및 표기법 (Business Process Model and Notation (BPMN))
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
- cooperative-object-transport: 협동 운반 (Cooperative Object Transport)
- cora: 로봇·자동화 핵심 온톨로지 (Core Ontology for Robotics and Automation (CORA))
- core-manufacturing-simulation-data: 핵심 제조 시뮬레이션 데이터 (Core Manufacturing Simulation Data (CMSD))
- costmap: 비용 지도 (Costmap)
- crdt: 무충돌 복제 데이터 타입 (Conflict-free Replicated Data Type (CRDT))
- cross-schedule-dependency: 스케줄 간 의존 (Cross-schedule Dependency (XD))
- dds-security: DDS 보안 규격 (DDS Security (DDS-Security))
- deadlock: 교착 (Deadlock)
- digital-nameplate: 디지털 명판 (Digital Nameplate (IDTA 02006))
- digital-shadow: 디지털 섀도 (Digital Shadow)
- digital-thread: 디지털 스레드 (Digital Thread)
- digital-twin-composition: 디지털 트윈 결합 (Digital Twin Composition)
- digital-twin: 디지털 트윈 (Digital Twin)
- discrete-event-simulation: 이산 사건 시뮬레이션 (Discrete Event Simulation (DES))
- dispenser-ingestor: 디스펜서·인제스터 (Dispenser / Ingestor)
- distributed-tracing: 분산 추적 (Distributed Tracing)
- drawing-exchange-format: 도면 교환 형식 (Drawing Exchange Format (DXF))
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
- explicit-implicit-confirmation: 명시적 확인·암시적 확인 (Explicit / Implicit Confirmation)
- failure-explanation: 실패 설명 (Failure Explanation)
- fan-out: 팬아웃 (Fan-out (human-robot team))
- fault-detection-and-diagnosis-fdd: 고장 탐지·진단 (Fault Detection and Diagnosis (FDD))
- fault-injection: 장애 주입 (Fault Injection)
- filter-mask: 필터 마스크 (Filter Mask (Nav2 costmap filter))
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
- hallucination: 환각 (Hallucination)
- hddl: 계층 도메인 정의 언어 (Hierarchical Domain Definition Language (HDDL))
- hierarchical-task-network: 계층적 작업 네트워크 (Hierarchical Task Network (HTN))
- high-impact-ai: 고영향 인공지능 (High-impact AI (Korea AI Basic Act))
- human-in-the-loop: 사람 참여 루프 (Human-in-the-Loop (HITL))
- hungarian-method: 헝가리안 방법 (Hungarian Method)
- idempotency-key: 멱등성 키 (Idempotency Key)
- identity-report: 신원 보고 (Identity Report (MassRobotics identityReport))
- iec-common-data-dictionary: IEC 공통 데이터 사전 (IEC Common Data Dictionary (IEC CDD))
- ifc: 산업 기초 클래스 (Industry Foundation Classes (IFC))
- indoor-mapping-data-format: 실내 지도 데이터 형식 (Indoor Mapping Data Format (IMDF))
- indoor-space-subspacing: 공간 세분화 (Subspacing (Indoor Space Subdivision))
- indoorgml: IndoorGML (IndoorGML)
- industrial-data: 산업데이터 (Industrial Data)
- information-delivery-specification: 정보 전달 명세 (Information Delivery Specification (IDS))
- information-for-use: 사용 정보 (Information for Use (Instructions for Use))
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
- lifelong-mapf: 지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF))
- lift-adapter: 승강기 어댑터 (Lift Adapter)
- linear-temporal-logic: 선형 시간 논리 (Linear Temporal Logic (LTL))
- littles-law: 리틀의 법칙 (Little's Law)
- llm-agent: LLM 에이전트 (LLM Agent)
- llm-modulo-framework: LLM-모듈로 프레임워크 (LLM-Modulo Framework)
- location-check-digit: 위치 체크 디지트 (Location Check Digit)
- managed-node: 관리형 노드 (Managed Node (ROS 2 Lifecycle Node))
- map-alignment: 지도 정합 (Map Alignment)
- mapf: 다중 에이전트 경로 찾기 (Multi-Agent Path Finding (MAPF))
- market-based-task-allocation: 시장 기반 작업 배정 (Market-based Task Allocation)
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
- nearest-vehicle-first-rule: 최근접 차량 우선 규칙 (Nearest Vehicle First (NVF) Rule)
- neuro-symbolic-ai: 신경-기호 AI (Neuro-symbolic AI)
- number-of-clicks: 클릭 수 지표 (Number of Clicks (NoC))
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- ontology-evolution: 온톨로지 진화 (Ontology Evolution)
- ontology-pitfall: 온톨로지 피트폴 (Ontology Pitfall)
- ontology-population: 온톨로지 채우기 (Ontology Population)
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
- operating-mode: 운용 모드 (Operating Mode (VDA 5050 operatingMode))
- operating-zone: 운용 구역 (Operating Zone (ISO 3691-4))
- optimality-gap: 최적성 간격 (Optimality Gap)
- order-batching: 주문 배치 (Order Batching)
- over-the-air-update: 무선 업데이트 (Over-the-Air Update (OTA))
- overall-equipment-effectiveness: 종합설비효율 (Overall Equipment Effectiveness (OEE))
- panoptic-quality: 파놉틱 품질 (Panoptic Quality (PQ))
- panoptic-symbol-spotting: 파놉틱 심볼 스포팅 (Panoptic Symbol Spotting)
- pass-k: pass^k 지표 (pass^k)
- pddl: 계획 도메인 정의 언어 (Planning Domain Definition Language (PDDL))
- perfect-order-fulfillment: 완전 주문 이행률 (Perfect Order Fulfillment)
- performable-action: 수행 가능 동작 (Performable Action (Open-RMF perform_action))
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- prompt-injection: 프롬프트 주입 (Prompt Injection)
- put-wall: 풋월 (Put Wall)
- raster-to-vector-conversion: 래스터–벡터 변환 (Raster-to-Vector Conversion)
- read-point: 판독 지점 (Read Point (EPCIS readPoint))
- reality-gap: 현실 격차 (Reality Gap (Sim-to-Real Gap))
- regression-testing: 회귀 시험 (Regression Testing)
- release-zone: 해제 구역 (Release Zone)
- required-and-provided-capability: 요구 능력·제공 능력 (Required Capability / Provided (Offered) Capability)
- resource-constrained-project-scheduling-problem: 자원 제약 프로젝트 스케줄링 문제 (Resource-Constrained Project Scheduling Problem (RCPSP))
- risk-assessment: 위험성평가 (Risk Assessment (ISO 12100))
- roadmap: 경로망 (Roadmap)
- robot-as-a-service: 서비스형 로봇 (Robot-as-a-Service (RaaS))
- robot-density: 로봇 밀도 (Robot Density)
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
- semantic-id: 의미 식별자 (Semantic ID (semanticId))
- semantic-versioning: 의미적 버전 관리 (Semantic Versioning (SemVer))
- semi-open-queueing-network: 반개방형 대기행렬 네트워크 (Semi-Open Queueing Network (SOQN))
- semi-static-object: 반정적 객체 (Semi-static Object)
- service-level-agreement: 서비스 수준 협약 (Service Level Agreement (SLA))
- shacl: 형상 제약 언어 (Shapes Constraint Language (SHACL))
- shifting-bottleneck-detection-active-period-method: 이동 병목 탐지 (Shifting Bottleneck Detection (Active Period Method))
- shuttle-based-storage-and-retrieval-system: 셔틀 기반 저장·회수 시스템 (Shuttle-Based Storage and Retrieval System (SBS/RS))
- signal-temporal-logic: 신호 시간 논리 (Signal Temporal Logic (STL))
- similarity-transformation: 유사 변환 (Similarity Transformation)
- situation-awareness-based-agent-transparency: 상황 인식 기반 에이전트 투명성 (Situation Awareness-based Agent Transparency (SAT))
- situation-state-tracking: 상황 상태 추적 (Situation State Tracking)
- skill-interface: 스킬 인터페이스 (Skill Interface)
- skill: 스킬 (Skill)
- slot-filling: 슬롯 채우기 (Slot Filling)
- smart-hospital-leading-model: 스마트병원 선도모델 (Smart Hospital Leading Model)
- smart-logistics-center-certification: 스마트물류센터 인증 (Smart Logistics Center Certification)
- software-nameplate: 소프트웨어 명판 (Software Nameplate (IDTA 02007))
- space-graph: 공간 그래프 (Space Graph)
- sscc: 물류 단위 일련 코드 (Serial Shipping Container Code (SSCC))
- state-of-charge: 충전 상태 (State of Charge (SOC))
- state-of-health: 배터리 건강 상태 (State of Health (SOH))
- stpa: 시스템 이론적 프로세스 분석 (System-Theoretic Process Analysis (STPA))
- structured-output: 구조화 출력 (Structured Output)
- success-weighted-by-path-length: 경로 길이 가중 성공률 (Success weighted by Path Length (SPL))
- supervisory-control: 감독 제어 (Supervisory Control)
- task-decomposition: 작업 분해 (Task Decomposition)
- technology-readiness-level: 기술 성숙도 (Technology Readiness Level (TRL))
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- traversability: 통과 가능성 (Traversability)
- uncertainty-alignment: 불확실도 정렬 (Uncertainty Alignment)
- underspecification: 과소명세 (Underspecification)
- urdf: 통합 로봇 기술 형식 (Unified Robot Description Format (URDF))
- user-simulator: 사용자 시뮬레이터 (User Simulator)
- vda-5050-cancel-order: 주문 취소 즉시 동작 (cancelOrder (VDA 5050 instant action))
- vda-5050-factsheet: VDA 5050 팩트시트 (VDA 5050 factsheet)
- vda-5050: VDA 5050 (VDA 5050)
- verification-and-validation-of-simulation-models: 시뮬레이션 모델 검증·타당성 확인 (Verification and Validation (V&V) of Simulation Models)
- version-iri: 버전 IRI (Version IRI (owl:versionIRI))
- virtual-commissioning: 가상 시운전 (Virtual Commissioning)
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking))
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [64] 에 걸린 0건 / 전체 175건)

```markdown
없음
```
