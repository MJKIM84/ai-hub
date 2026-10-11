(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-11-01
- date: 2026-10-11
- run_type: update (갱신)
- 대상: 21. 상호운용 표준·적합성 (F. 연동)
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

### runs/2026-10-11-01/target.json

```json
{
  "run_id": "2026-10-11-01",
  "date": "2026-10-11",
  "weekday": "Sun",
  "run_number": 167,
  "run_type": "update",
  "forced": true,
  "target": {
    "area_no": 21,
    "area_name": "21. 상호운용 표준·적합성",
    "category": "F. 연동",
    "category_letter": "F"
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
  "selection_rationale": "CLI 지정 run_type=update, area=21"
}
```

### runs/2026-10-11-01/research.json

```json
{
  "run_id": "2026-10-11-01",
  "date": "2026-10-11",
  "run_type": "update",
  "target": {
    "area_no": 21,
    "area_name": "21. 상호운용 표준·적합성",
    "category": "F. 연동"
  },
  "gaps": [
    "섹션 5. 적용 사례 (현장 유형 명시) — 수행 자원 칸이 'VDA 5050 3.0.0 에서 주문 배정·경로 계산…은 관제 쪽'으로 경로 계산을 모든 로봇에 일반화함(원문은 선 유도 로봇). 물류창고 외 현장 유형 사례 없음",
    "섹션 6. 대표 접근법과 기술(주제 페이지로 분리) — '제조사가 자체 인증하거나' 문장의 근거 없음(정정 필요). 선택 필드·재전송·취소 후 갱신을 확인하는 동작 시험 방법 없음. OTTO 인증 발표 각주가 원문 미열람",
    "섹션 7. 관련 표준·프레임워크·오픈소스(주제 페이지로 분리) — VDA 5050 행 발행일 표기, MassRobotics 행 '원문 미열람', OPC 행 '자체·독립 시험소 인증' 표현. 3.0.0 태그 스키마 끝 쉼표, OPC UA Robotics 서버 Facet, KS B ISO 22166-202 미반영. 트랙 반영 제안(2026-10-09-26, 건축 도면 자동 인식 단계 2: IDS 1.0 을 BIM 데이터 교환 요구·적합성 검사 수단으로) 미처리",
    "섹션 8. 대표 연구와 자료 — vda5050-lab 원문 미열람 표시, VDA 5050 통신 평가 논문 없음",
    "섹션 10. 다른 연구영역과의 연결 — 42. 분산 시스템·통신·컴퓨팅 구조, 14. 도면·BIM에서 지도 만들기 연결 없음",
    "섹션 11. 열린 질문 — oq-005·oq-055·oq-091·oq-026 부분 근거 미반영",
    "정정 요청 없음"
  ],
  "research_questions": [
    "어떤 상호운용 표준을 따르고, 제조사가 그 표준을 지키는지 어떻게 확인할 것인가? [분류원문]",
    "oq-005 VDA 5050 3.0.0 의 날짜는 공식 저장소 명세·카탈로그·보도자료·참여 업체 발표에서 각각 무엇으로 표시되는가? (섹션 7·11 겨냥)",
    "oq-055 VDA 5050 에 공식 적합성 시험·인증 절차가 있는가, 없다면 제3자 도구·벤더 간 인증·전시 시연·인정 시험소 인증을 연동 승인 근거로 어떻게 구분해 쓸 수 있는가? (섹션 6·8·11 겨냥)",
    "oq-091 VDA 5050 3.0.0 태그의 JSON 스키마를 시험 입력으로 그대로 쓸 수 있는가? (섹션 7·11 겨냥)",
    "oq-026 KS B 7321-2 와 KS B ISO 22166-202 는 국가표준 목록에서 무엇으로 확인되는가? TTAK.KO-10.1295-Part8 은 공식 목록에서 확인되는가? (섹션 7·11 겨냥, 한국 자료 우선)",
    "트랙 반영 제안 2026-10-09-26: IDS 1.0(buildingSMART)의 적용 대상·요구 구조·패싯·값 제한은 발행 기관 자료로 무엇이며, 21. 상호운용 표준·적합성의 적합성 검사 수단으로 볼 수 있는가? (섹션 7·10 겨냥)",
    "기존 문장 점검: VDA 5050 3.0.0 은 경로 계산을 어느 로봇에 대해 관제 책임으로 두는가, OPC Foundation 은 제조사 자체 인증을 허용하는가? (섹션 5·6·7 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "VDA5050 공식 저장소의 3.0.0 명세 마크다운 표지는 판을 'Version 3.0.0'으로만 적고 날짜를 적지 않으며, VDA 가 배포하는 PDF 표지의 날짜 표기는 이번 실행에서 PDF 본문 텍스트를 읽지 못해 확인하지 못했다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "3.0.0 태그 VDA5050_EN.md 머리: 제목 아래 'VDA 5050', 'Version 3.0.0'만 있고 날짜 없음(data/source_texts/ref-031.txt 와 3.0.0 태그 raw 파일로 확인). VDA PDF(103쪽, A4)는 압축 스트림만 읽혀 표지 문구 대조 불가(발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "구축자 의견: 21번 7절 표 VDA 5050 행의 발행일은 단일 날짜로 확정하지 않고 '미확인'을 유지하되, VDA 카탈로그 표시일(2026-03-17)과 보도자료 날짜(2026-04-20)가 서로 다르다는 점은 20번 주제 페이지의 날짜 절로 연결하고, PDF 표지의 'March 2026' 표기는 원문 확인 전까지 [추정]으로 두는 것이 맞다.",
      "tag": "의견",
      "source_ids": [
        "ref-1412",
        "ref-032",
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "카탈로그 항목 'March 17, 2026'(ref-1412), 보도자료 머리 'Berlin, April 20, 2026'(ref-032) 모두 이번에 다시 열어 확인. 세 자료 모두 VDA 계열이라 독립 교차 확인 아님",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "VDA 5050 3.0.0 §5.3 의 관제 기능 목록은 경로 계산을 일반 기능이 아니라 선 유도(line-guided) 이동로봇의 경로 계산·안내로 적고, §5.4 는 이동로봇 기능을 선 유도형과 자유 주행형(freely navigating)의 경로 실행으로 나눠 서술한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§5.3 \"Route calculation and guidance of line-guided mobile robots\"; §5.4 경로 실행을 선 유도·자유 주행으로 구분. 원문에 '한정' 표현은 없어 직역. 같은 직역은 2026-10-09-area41-s6 46행에 이미 있음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "VDA 의 3.0 발표 보도자료는 자율도가 높은 이동로봇이 지정된 경유점 사이 경로를 스스로 계획해 상세 경로 계획이 로봇에서 이뤄지고, 그 경로를 경로 공유(path sharing)로 중앙 관제와 공유하는 구성을 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-032"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "보도자료: \"the detailed route planning takes place on the vehicle itself\", 경로를 'path sharing'으로 중앙 관제와 공유. 명세 §6.8 예정 경로 공유 세부는 2026-10-10-area27-s7 41~45행에 있음",
      "as_of": "2026-04-20",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "구축자 의견: 21번 본문 5절 수행 자원 칸과 분리 7절 본문의 '주문 배정·경로 계산·…은 관제 쪽' 문장은 '선 유도 로봇의 경로 계산·안내'로 고치고, 자유 주행 로봇은 상세 경로를 스스로 계획해 공유할 수 있음을 병기해 모든 이동로봇의 상세 경로를 관제가 계산한다고 일반화하지 않는 것이 맞다.",
      "tag": "의견",
      "source_ids": [
        "ref-031",
        "ref-032"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "정정 대상: 본문 5절 수행 자원 칸 '(출하) … 주문 배정·경로 계산·교착 탐지와 해소·교통 제어는 관제 쪽', 2026-09-25-area28-s7 본문 첫 문단. 같은 일반화가 categories/governance-law-and-society/index.md 70행에도 있으나 다른 페이지라 후속 정리 대상",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "VDA 5050 3.0.0 §7.1.1 은 로봇이 받은 선택(optional) 필드를 무시해서는 안 되고 쓸 수 없으면 UNSUPPORTED_PARAMETER(CRITICAL)로 알리게 하며, 관제(fleet control)에는 로봇이 지원하는 선택 필드만 보내도록 의무를 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "3.0.0 태그 raw 명세 §7.1.1 재서술: 로봇은 선택 필드를 무시하지 않음, 필요한 선택 파라미터는 factsheet 로 밝힘, 관제는 로봇이 지원하는 선택 필드만 보냄(예: 궤적을 처리 못 하는 로봇에는 trajectory 를 보내지 않음)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "VDA 5050 3.0.0 은 연동 시험의 기대값으로 쓸 응답을 조항으로 정한다: 지원하지 않는 선택 파라미터가 든 주문은 UNSUPPORTED_PARAMETER(CRITICAL)로 거절, 같은 orderUpdateId 재전송은 내용이 같으면 무시하고 다르면 SAME_ORDER_UPDATE_ID(WARNING)를 보고하며 이전 주문을 계속, 취소된 주문의 후속 갱신은 ORDER_UPDATE_FOLLOWING_CANCEL(WARNING).",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§6.1.4.2·§6.1.3.1(data/source_texts/ref-031.txt), §6.1.4.5(3.0.0 태그 raw 명세) 재서술. 재전송 규칙 자체는 2026-10-09-area41-s6 56행, command-and-task-execution-reliability.md 90행에 이미 있음 — 새로운 것은 시험 기대값 관점",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "구축자 의견: 로봇 연동 승인에는 버전 문자열 확인에 더해 (1) 미지원 선택 필드 주문 거절, (2) 같은 번호·같은 내용 재전송 무시, (3) 같은 번호·다른 내용 재전송 경고, (4) 취소 후 갱신 경고, (5) 관제가 로봇 factsheet 가 지원한다고 밝힌 선택 필드만 보내는지를 확인하는 동작 시험표를 두고, 수신 직전 주문 상태와 관측 로그 누락 여부를 함께 보존하는 것이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f6·f7 조항을 시험 행으로 옮긴 구축자 제안이며 VDA·VDMA 공식 인증 항목 목록이 아님. (5)행은 §7.1.1 관제 의무에서 나옴",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "VDA5050 공식 저장소 3.0.0 태그의 json_schemas/order.schema·factsheet.schema·visualization.schema 에는 닫는 괄호 바로 앞에 쉼표가 오는 끝 쉼표(trailing comma)가 있어 엄격한 JSON 으로 읽히지 않으며, main 브랜치의 order.schema 는 같은 자리(궤적 제어점 weight 속성)에 끝 쉼표가 없다.",
      "tag": "사실",
      "source_ids": [
        "ref-1430",
        "ref-1431",
        "ref-1432",
        "ref-413"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "2026-10-11 raw 파일 직접 확인: order 는 controlPoint weight 설명 줄 뒤 쉼표+'}', factsheet 는 physicalParameters 치수 항목의 \"unit\": \"m\" 뒤 쉼표+'}', visualization 은 weight 와 properties 끝. main order.schema 는 쉼표 없음. 구문 관찰이며 로봇 적합성 시험이 아님. 행·열 번호는 싣지 않음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "구축자 의견: VDA 5050 3.0.0 을 시험 입력으로 쓸 때는 '공식 태그'와 '파싱 가능한 시험 입력'을 따로 확인하고, 수정한 스키마를 쓰면 원본과의 차이·수정 근거·해시를 보존하며 main 브랜치 내용을 설명 없이 섞지 않는 것이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-1430",
        "ref-413"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f9 관찰에서 나온 운영 제안. 공식 명세·태그 스키마·검사 도구 판을 각각 고정. 공식 저장소 README 는 GitHub 자료와 VDA 게시 PDF 가 다르면 PDF 가 유효하다고 적음(ref-634, 기존 페이지 각주)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f13",
      "claim": "vda5050-lab README(커밋 4a1a812)는 현재 판 v0.2.0 을 개발자 프리뷰(Developer Preview)로 부르며 오프라인 진단 구현과 범위가 제한된 합성 시연을 담는다고 설명하고, 공개 알파나 인증 주장이 아니며 실제 고객 기록·외부 시험 대상(DUT)·실물 하드웨어 실행을 검증하지 않았다고 밝힌다.",
      "tag": "사실",
      "source_ids": [
        "ref-408"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Status 절: \"not a public-alpha or certification claim\"; 실제 고객 기록·외부 DUT·하드웨어 실행 미검증. 문서의 자기 기술만 확인했고 프로그램은 실행하지 않음(발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f14",
      "claim": "구축자 의견: vda5050-lab 은 MQTT 기록 진단의 보조 도구 후보로만 두고, 그 판정을 구매·연동 승인 전체의 대체물로 쓰지 않는 것이 맞다.",
      "tag": "의견",
      "source_ids": [
        "ref-408"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "21번 8절 vda5050-lab 항목과 각주 '(원문 미열람)' 표시를 f13 으로 보강하는 제안. 개인 프로젝트의 한계 선언과 공식 시험기관 인증은 별개",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f15",
      "claim": "OPC Foundation 'How to Certify' 는 제조사가 인증 시험 전에 가능한 많은 시험을 미리 해 보도록 권고하고, 재단이 제공하는 적합성 시험 도구(compliance test tools)는 시험소가 시험에 쓰는 도구라고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-705"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"It is suggested that vendors prepare for testing\"(권고 표현), 도구는 시험소가 시험을 돕는 데 씀. 페이지는 'CTT' 약어를 쓰지 않음(발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "OPC Foundation 인증 개요 페이지는 인증 제품이 재단이 인정한 인증 시험소에서 시험을 거쳤다고 설명하고, 인증된 SDK 를 쓴 응용도 공식 인증 제품이 되려면 각자 인증 시험을 받아야 한다고 밝힌다.",
      "tag": "사실",
      "source_ids": [
        "ref-1434"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"Certified products have been tested in an OPC Foundation accredited Certification Lab\"; SDK 기반 응용은 자체 인증 시험 필요. ref-705 와 같은 기관이라 독립 교차 확인 아님(발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f17",
      "claim": "확인한 OPC Foundation 인증 안내 두 페이지에는 제조사가 스스로 인증하는(self-certification) 경로가 없으므로, 21번 분리 6절의 '제조사가 자체 인증하거나'와 분리 7절 표 OPC 행의 '자체·독립 시험소 인증'은 이 두 출처로 뒷받침되지 않는 표현이다.",
      "tag": "사실",
      "source_ids": [
        "ref-705",
        "ref-1434"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "두 페이지 모두 인정 시험소 시험만 설명하고 자체 인증 언급 없음(2026-10-11 재열람). 정정 대상: 2026-09-25-area28-s6「적합성 시험과 인증」첫 문단, 2026-09-25-area28-s7 표 OPC 행, ref-705 참고문헌 요약",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f18",
      "claim": "구축자 의견: OPC 적합성 체계는 '제조사의 적합성 시험 도구 사전 점검(권고)'과 '인정 시험소 인증'을 구분하는 문장으로 고치고, 이 구조를 VDA 5050 의 인증 체계로 그대로 옮겨 쓰지 않는 것이 맞다.",
      "tag": "의견",
      "source_ids": [
        "ref-705",
        "ref-1434"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f15~f17 정정 제안. 시험 항목은 지원 프로파일에 따라 달라짐",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f19",
      "claim": "MassRobotics AMR_Interop_Standard.json(커밋 f9357a4)의 최상위 oneOf 는 identityReport 와 statusReport 두 정의만 참조하고, 위치(location) 정의는 x·y·angle·planarDatum 네 필드를 모두 필수로 두며, 명령·주문·작업 메시지 정의는 없다.",
      "tag": "사실",
      "source_ids": [
        "ref-230"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "최상위 oneOf: identityReport·statusReport; location.required = [x, y, angle, planarDatum](z 는 선택). statusReport 필수 필드는 2026-10-10-area20-s7 52행에 이미 있음. 별도 표준 PDF 판·발행일 미확인(발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "구축자 의견: MassRobotics 보고 메시지(신원·상태) 교환만으로 작업 명령 호환성이나 좌표계 정합을 확보했다고 주장하지 않는 것이 맞다.",
      "tag": "의견",
      "source_ids": [
        "ref-230"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f19 스키마에 명령·작업 배정 메시지가 없음. 21번 분리 7절 표 MassRobotics 행의 '(원문 미열람)'은 스키마 원문 확인으로 해소",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "OPC 40010-1(OPC UA for Robotics Part 1) 1.02판 §11.2.2 는 서버 기능 묶음(Facet)을 기본(Base)·운전(MDS Operation)·자산관리 확장(AM Extended)·상태감시 확장(CM Extended) 넷으로 나누고, 표 124~127 에서 각 적합성 단위를 필수(M)·선택(O)으로 구분한다.",
      "tag": "사실",
      "source_ids": [
        "ref-034"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§11.2.2.2~11.2.2.5, 표 124(Base, 모두 M)·125(MDS Operation)·126(AM Extended)·127(CM Extended). 표 123 은 프로파일 URI 목록. 판·범위는 2026-09-29-area04-s7 43행에 이미 있음 — 새로운 것은 Facet 구조",
      "as_of": "2025-09-08",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "구축자 의견: 연동 요구에는 'OPC UA 지원' 대신 OPC UA Robotics 판·서버 Facet·선택 단위·인증 범위를 적게 하고, 이 정보모델을 VDA 5050 주문 스키마와 일대일로 자동 변환할 수 있다고 보지 않는 것이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-034"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f21 에서 나온 제안",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "국가표준인증통합정보시스템(KSSN) 상세 페이지에는 KS B 7321-2 '로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델'이 실려 있으나, 이번 열람에서는 번호와 제목만 보였고 제정일·국제표준 부합화·고시 정보는 보이지 않았다.",
      "tag": "사실",
      "source_ids": [
        "ref-138"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "KSSN 상세(itemNo=K001010147546) 2026-10-11 재열람: 번호·제목만 표시. 제정일·부합화 칸 등 세부 칸은 대조 불가(발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f25",
      "claim": "KSSN 상세 페이지에는 KS B 7321-2 와 별도로 KS B ISO 22166-202 '로봇 — 서비스 로봇의 모듈화 — 제202부: 소프트웨어 모듈용 정보 모델'이 실려 있으나, 제정일·부합화 수준(IDT 여부)·고시 정보는 이번 열람에서 보이지 않았다.",
      "tag": "사실",
      "source_ids": [
        "ref-1435"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "KSSN 상세(itemNo=K001010158171) 2026-10-11 열람: 번호·제목만 표시. 웹 검색에서도 제정 기록을 찾지 못함(발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f26",
      "claim": "구축자 의견: oq-026 은 열림을 유지하고, KS B ISO 22166-202 가 국가표준 목록에 따로 있다는 점만 확인할 거리로 남기며, 그 제정일·부합화 수준과 KS B 7321-2 와의 대체 관계, 국내 적용 사례는 미확인으로 둔다.",
      "tag": "의견",
      "source_ids": [
        "ref-138",
        "ref-1435"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f24·f25 는 번호·제목만 확인. 제정일·고시번호·IDT 는 이전 브리프의 미대조 값이라 쓰지 않음",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f30",
      "claim": "OTTO by Rockwell Automation 은 2026-04-09 보도자료에서 OTTO 100·600·1200·1500 이 Idealworks·NAiSE·SYNAOS 등 VDA 5050 관제 소프트웨어 업체와 인증을 마쳤다고 밝혔으나, 시험한 프로토콜 판·시험 항목·시험 기관은 밝히지 않는다.",
      "tag": "추정",
      "source_ids": [
        "ref-608"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 'KITCHENER, ON—April 9, 2026—OTTO … announced that its autonomous mobile robots' 이하 인증 발표. 판·항목·기관 기재 없음. 인증 발표 자체는 2026-09-25-area28-s6 에 이미 있음 — 새로운 것은 날짜·기종과 각주 '(원문 미열람)' 해소",
      "as_of": "2026-04-09",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f31",
      "claim": "VDMA 의 Mesh-Up 2025 안내는 automatica 2025(뮌헨, 2025-06-24~27) 전시장에서 9개 기업이 참여하고 MHP 가 상위 관제를 맡아, 여러 이동로봇이 작업대를 공급하는 양식화한 생산 라인을 보여 주는 혼합 플릿 시연(전시 시연이며 실제 공장 배치가 아님)을 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1436"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "행사 안내 본문: 9개 기업 시연, MHP 가 master control system, 생산 라인의 양식화 표현. 기업 수를 로봇 대수로 바꾸지 않음. automatica 2025 전시 시연, 실제 공장 배치 아님(발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": "제조 공장",
      "flow_item": "수행 자원"
    },
    {
      "id": "f32",
      "claim": "같은 Mesh-Up 2025 안내(automatica 2025 전시 시연, 실제 공장 배치 아님)는 관제 소프트웨어 공급자를 바꿔 고를 수 있는 점을 전시장에서 실시간으로 시연하지는 않는다고 밝힌다.",
      "tag": "사실",
      "source_ids": [
        "ref-1436"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "공급자 교체는 \"is not demonstrated live at automatica by the Mesh-Up\"(발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": "제조 공장",
      "flow_item": "예외·성과"
    },
    {
      "id": "f33",
      "claim": "구축자 의견: Mesh-Up 같은 전시 시연은 5절 '제조 공장' 현장 유형의 혼합 플릿 구성 예로만 쓰고 표 머리와 각 칸에 'automatica 2025 전시 시연, 실제 공장 배치 아님'을 밝히며, 실제 도입 사례나 현장 관제 교체가 검증된 근거로 세지 않는 것이 맞다.",
      "tag": "의견",
      "source_ids": [
        "ref-1436"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f31·f32 기반. 현장 유형 × 대분류 매트릭스에서도 도입 사례로 세지 않음",
      "as_of": "2026-10-11",
      "site_type": "제조 공장",
      "flow_item": null
    },
    {
      "id": "f34",
      "claim": "Wagner 외(제22회 IEEE WFCS 2026)는 표준이 원격 조작(teleoperation)을 기본으로 다루지 않는다고 보고 VDA 5050 원격 조작 확장과 재현 평가용 VDA 5050 트래픽 생성기를 제안하며, VDA 5050 메시지·미들웨어 전송·Open RAN 무선 링크를 잇는 구성에서 지연과 통신 오버헤드를 평가한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1437"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "TUHH 저장소 초록: \"teleoperation is not natively represented in the standard\", 확장 제안·구성 가능한 트래픽 생성기·종단간 지연·오버헤드 평가. 논문 제안 확장이며 표준 채택 기능 아님",
      "as_of": "2026-04",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f36",
      "claim": "TU Dortmund 통신망 연구실의 논문 소개(2026-04-24)는 이 평가가 재현성 높은 가상 무선(virtual-radio) 시험대와 실제 무선(over-the-air) 검증 구성을 함께 썼다고 설명하며, 정량 결과와 로봇 대수는 소개문에 없다.",
      "tag": "사실",
      "source_ids": [
        "ref-1438"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "소개문 'highly reproducible virtual-radio testbed', 'real-world over-the-air validation setup'. 트래픽 생성기는 GitHub tudo-cni/VDA-5050-Traffic-Generator 로 공개. 논문 본문 수치(로봇 수·주문 시간)는 PDF 텍스트를 읽지 못해 미확인",
      "as_of": "2026-04-24",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f37",
      "claim": "구축자 의견: 21번에서는 Wagner 외 연구를 VDA 5050 통신 부하·지연 평가로 소개하되 적합성 시험과 구별하고, 상세 네트워크 설계는 42. 분산 시스템·통신·컴퓨팅 구조 연결로만 두는 것이 맞다.",
      "tag": "의견",
      "source_ids": [
        "ref-1437",
        "ref-1438"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f34·f36 기반 8절·10절 제안. 원격 조작 표기는 용어집 '원격 조작 (Teleoperation)'을 따름",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f38",
      "claim": "구축자 의견: VDA 5050 연동 승인의 근거는 제3자 도구의 자체 진단, 벤더 간 인증 발표, 전시 시연, 인정 시험소 인증을 서로 다른 근거 수준으로 나눠 기록하는 것이 맞다.",
      "tag": "의견",
      "source_ids": [
        "ref-408",
        "ref-608",
        "ref-1436",
        "ref-705",
        "ref-1434"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f13·f30·f32·f15~f17 종합. oq-055 부분 근거: VDA·VDMA 공인 인증 제도의 존재·부재는 확정 못 함",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f39",
      "claim": "VDA 5050 작업반 참여 업체인 Idealworks 는 2026년 3월 소식 글에서 VDMA·VDA 가 2월 17일 3.0.0 판을 정식 채택했고 이어 법적 승인 절차를 거쳤다고 적어, VDA 공식 자료의 날짜 표시(카탈로그 2026-03-17·보도자료 2026-04-20)와 또 다른 날짜를 제시한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1442"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "\"On February 17th, VDMA and VDA formally adopted the 3.0.0 release.\" 뒤이어 법적 승인. 글 날짜는 'March 2026'(일 미표기). 업체 글이며 VDA 자료로 확인되지 않음 — oq-005 출처 충돌의 추가 근거",
      "as_of": "2026-03",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f40",
      "claim": "buildingSMART 는 정보 전달 명세(Information Delivery Specification, IDS)를 2024-06-01 승인된 공식 표준으로 소개하고, 데이터 요구를 기계가 읽을 수 있게 기술해 IFC 모델의 적합성을 자동으로 검사할 수 있게 한다고 설명하며, 1.0 이전 판은 공식 표준이 아니라고 밝힌다.",
      "tag": "사실",
      "source_ids": [
        "ref-1439"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"On 1st June 2024 the IDS has been approved and became the official buildingSMART standard!\"; IFC 모델 자동 적합성 검사. 스키마는 standards.buildingsmart.org/IDS/1.0/ids.xsd(발행일 미확인, 확인일 기준)",
      "as_of": "2024-06-01",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f41",
      "claim": "IDS 공식 사용자 설명서는 IDS 파일이 하나 이상의 명세(specification)로 이루어지고 각 명세가 적용 대상(applicability)과 요구(requirements)를 가지며, 둘 다 엔터티·속성(attribute)·분류·속성 값(property)·재료·소속(partOf) 패싯으로 구성되고, 받는 쪽이 IDS 와 IFC 를 함께 불러 검사해 불일치 보고를 얻는다고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1362"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "UserManual README: 적용 대상은 'what elements are subject to this specification', 'Both applicability and requirements are built with facets', 결과는 불일치 보고(발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f42",
      "claim": "IDS 사용자 설명서는 패싯 파라미터에 단순 값 대신 열거(enumeration)·패턴(pattern)·범위(bounds)·길이(length)의 복합 제한을 걸 수 있다고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1365"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "restrictions.md: 'Complex Restriction' 네 종류 — 허용 목록, 이름 형식(와일드카드·정규식), 수치 최소·최대(포함·제외), 문자 수. 기수(필수·선택·금지)는 이 문서에 없어 미확인(발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f43",
      "claim": "IDS 공식 저장소의 문서 안내는 소프트웨어 구현의 IDS 읽기·검사 기능이 올바른지 확인하기 위한 .ids·.ifc 쌍 250개 이상의 시험 파일 묶음을 TestCases 폴더에 둔다고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1443"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Documentation/README.md: TestCases 폴더 'suite of over 250 test file pairs (.ids and .ifc)', 구현의 읽기·검사 기능 검증용(발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f44",
      "claim": "구축자 의견: 21번 7절에는 IDS 1.0 을 '건물 정보 모델(IFC) 데이터 교환 요구의 적합성 검사 수단'으로 짧게 두고, 검사 도구 자체도 공식 시험 파일 묶음으로 확인할 수 있다는 점을 적되, 로봇–관제 메시지 적합성 시험과는 구별하며, 로봇 지도용 BIM 객체·속성 요구의 세부는 14. 도면·BIM에서 지도 만들기와 건축 도면 자동 인식 트랙에 두는 것이 맞다.",
      "tag": "의견",
      "source_ids": [
        "ref-1439",
        "ref-1362",
        "ref-1443"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "트랙 반영 제안 2026-10-09-26(IDS → 7절) 처리안. 제안 요약의 기수·사용자 정의 속성 세트 명명 규칙·뉴질랜드 OBOS 프록시 관례는 이번에 원문으로 확인하지 못해 반영하지 않음",
      "as_of": "2026-10-11",
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
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "VDA 5050 3.0.0 명세 마크다운 원문. 입력 원문 텍스트(§4.1·§5.3·§5.4·§6.1)와 3.0.0 태그 raw 파일(§6.1.4.5·§7.1.1)로 관제–로봇 기능 분담, 선택 필드 의무, 오류 응답 조항을 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/3.0.0/VDA5050_EN.md",
      "source_unopened": false
    },
    {
      "id": "ref-032",
      "org": "VDA(Verband der Automobilindustrie)",
      "title": "Version 3.0 of VDA 5050 released",
      "published": "2026-04-20",
      "url": "https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "VDA 5050 3.0 발행 보도자료. 머리 'Berlin, April 20, 2026'과 자율도 높은 로봇의 경로 자체 계획·경로 공유 설명을 다시 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1412",
      "org": "VDA(Verband der Automobilindustrie)",
      "title": "VDA 5050",
      "published": "2026-03-17",
      "url": "https://www.vda.de/en/news/publications/publication/vda-5050",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "VDA 발행물 카탈로그의 VDA 5050 Version 3.0.0 항목. 표시 날짜 'March 17, 2026'을 다시 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1430",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/order.schema (tag 3.0.0)",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/3.0.0/json_schemas/order.schema",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "공식 저장소 3.0.0 태그의 주문 메시지 JSON 스키마. 궤적 제어점 weight 속성 설명 줄 뒤 닫는 괄호 앞 끝 쉼표를 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/3.0.0/json_schemas/order.schema",
      "source_unopened": false
    },
    {
      "id": "ref-1431",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/factsheet.schema (tag 3.0.0)",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/3.0.0/json_schemas/factsheet.schema",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "공식 저장소 3.0.0 태그의 팩트시트 JSON 스키마. physicalParameters 치수 항목의 unit 줄 뒤 끝 쉼표를 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/3.0.0/json_schemas/factsheet.schema",
      "source_unopened": false
    },
    {
      "id": "ref-1432",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/visualization.schema (tag 3.0.0)",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/3.0.0/json_schemas/visualization.schema",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "공식 저장소 3.0.0 태그의 시각화 메시지 JSON 스키마. properties 끝과 weight 속성의 끝 쉼표를 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/3.0.0/json_schemas/visualization.schema",
      "source_unopened": false
    },
    {
      "id": "ref-413",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/order.schema (main)",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/order.schema",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "공식 저장소 main 브랜치의 주문 메시지 JSON 스키마. 3.0.0 태그와 달리 weight 속성에 끝 쉼표가 없음을 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/json_schemas/order.schema",
      "source_unopened": false
    },
    {
      "id": "ref-408",
      "org": "ekusiadadus (GitHub)",
      "title": "vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces)",
      "published": null,
      "url": "https://github.com/ekusiadadus/vda5050-lab",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "MQTT 기록에서 VDA 5050 주문·재연결·취소 실패를 진단하는 개인 프로젝트 README. 커밋 4a1a812 고정본에서 v0.2.0 이 개발자 프리뷰이고 인증 주장이 아니라는 한계 선언을 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/ekusiadadus/vda5050-lab/4a1a812f9418084f658b65856cf3e1a5bbc2cf51/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-705",
      "org": "OPC Foundation",
      "title": "How to Certify - OPC Foundation",
      "published": null,
      "url": "https://opcfoundation.org/certification/how-to-certify/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "OPC 제품 인증 절차 안내. 제조사가 시험 전에 미리 준비하도록 권고하고 적합성 시험 도구(compliance test tools)는 인정 시험소가 쓰는 도구라고 설명한다. 제조사 자체 인증 경로는 없다(기존 요약의 '자체 인증' 표현은 정정 필요).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1434",
      "org": "OPC Foundation",
      "title": "Overview & Benefits — OPC Foundation Certification",
      "published": null,
      "url": "https://opcfoundation.org/certification/overview-benefits/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "OPC Foundation 인증 프로그램 개요. 인증 제품은 재단이 인정한 인증 시험소에서 시험을 거치며, 인증 SDK 를 쓴 응용도 각자 인증 시험이 필요하다고 설명한다.",
      "fetched": true,
      "fetched_via": "webfetch",
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
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "MassRobotics AMR 상호운용 표준의 공식 JSON 스키마. 커밋 f9357a4 고정본에서 최상위 oneOf(identityReport·statusReport), location 필수 필드 [x, y, angle, planarDatum], 명령 메시지 부재를 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/MassRobotics-AMR/AMR_Interop_Standard/f9357a423ecabc3f7112e6d10025a5231943ec50/AMR_Interop_Standard.json",
      "source_unopened": false
    },
    {
      "id": "ref-034",
      "org": "OPC Foundation / VDMA",
      "title": "OPC-40010-1 – OPC UA for Robotics - Part 1: Vertical Integration",
      "published": "2025-09-08",
      "url": "https://reference.opcfoundation.org/specs/OPC-40010-1",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "OPC UA for Robotics 1부 공식 온라인 참조(1.02판). 이번에 §11.2.2 서버 Facet 네 가지와 표 124~127 의 필수·선택 구분을 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://reference.opcfoundation.org/specs/OPC-40010-1/full",
      "source_unopened": false
    },
    {
      "id": "ref-138",
      "org": "국가표준인증통합정보시스템(KSSN)",
      "title": "KS B 7321-2 로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델",
      "published": null,
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010147546",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "KS B 7321-2 의 KSSN 상세 페이지. 이번 열람에서는 번호와 제목만 보였고 제정일·부합화 칸 등 세부 정보는 확인하지 못했다(본문 미열람).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1435",
      "org": "국가표준인증통합정보시스템(KSSN)",
      "title": "KS B ISO 22166-202 로봇 — 서비스 로봇의 모듈화 — 제202부: 소프트웨어 모듈용 정보 모델",
      "published": null,
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010158171",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "KS B ISO 22166-202 의 KSSN 상세 페이지. 번호와 제목만 보였고 제정일·부합화 수준·고시 정보는 확인하지 못했다(본문 미열람).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-608",
      "org": "OTTO by Rockwell Automation",
      "title": "OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments",
      "published": "2026-04-09",
      "url": "https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-11",
      "summary": "OTTO AMR(OTTO 100·600·1200·1500)이 Idealworks·NAiSE·SYNAOS 등과 VDA 5050 인증을 마쳤다는 2026-04-09 보도자료(벤더 주장). 시험 판·항목·기관은 밝히지 않는다. 참고문헌 목록의 발행일 '2026-04'를 원문 기준 2026-04-09 로 고친다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1436",
      "org": "VDMA",
      "title": "Mobile Robots in Production: Mesh-Up 2025",
      "published": null,
      "url": "https://www.vdma.eu/en/mesh-up",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "VDMA 의 automatica 2025(2025-06-24~27) 이동로봇 혼합 플릿 공동 시연 안내. 9개 기업 참여, MHP 상위 관제, 양식화한 생산 라인 공급 시연이며 관제 공급자 교체는 현장 실시간 시연이 아니라고 밝힌다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1437",
      "org": "Wagner, N. A., Toenning, L., Lünsch, D., Jost, J., Wietfeld, C., Detzner, P.",
      "title": "Teleoperating Mobile Robots via VDA 5050 – A First Middleware Evaluation within Open Industrial Networks",
      "published": "2026-04",
      "url": "https://doi.org/10.1109/WFCS67029.2026.11511549",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "제22회 IEEE WFCS(2026) 논문. VDA 5050 원격 조작 확장과 트래픽 생성기를 제안하고 Open RAN 무선 링크를 포함한 종단간 지연·오버헤드를 평가한다. TUHH 기관 저장소의 서지·초록만 확인했고 저자 공개본 PDF 본문은 텍스트를 읽지 못했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://tore.tuhh.de/entities/publication/c52e5a37-bd83-4969-a842-a8c34eaa43a8",
      "source_unopened": false
    },
    {
      "id": "ref-1438",
      "org": "TU Dortmund, Communication Networks Institute (ComNets)",
      "title": "Interoperable Teleoperation of Mobile Robots in Intralogistics: Joint Paper Demonstrates End-to-End Network Co-Design for Smart Industries",
      "published": "2026-04-24",
      "url": "https://comnets.etit.tu-dortmund.de/details/interoperable-teleoperation-of-mobile-robots-in-intralogistics-joint-paper-demonstrates-end-to-end-network-co-design-for-smart-industries-63558/",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "저자 소속 연구실의 논문 소개. 가상 무선 시험대와 실제 무선 검증 구성을 썼다고 설명하고 트래픽 생성기 공개 저장소를 알린다. 정량 결과는 싣지 않는다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1439",
      "org": "buildingSMART International",
      "title": "Information Delivery Specification (IDS)",
      "published": null,
      "url": "https://www.buildingsmart.org/standards/bsi-standards/information-delivery-specifications-ids/",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "IDS 공식 소개 페이지. 2024-06-01 승인된 공식 표준이며 기계가 읽는 데이터 요구로 IFC 모델의 자동 적합성 검사를 가능하게 한다고 설명한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1362",
      "org": "buildingSMART International (buildingSMART/IDS GitHub)",
      "title": "IDS — Documentation/UserManual/README.md",
      "published": null,
      "url": "https://github.com/buildingSMART/IDS/blob/development/Documentation/UserManual/README.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "IDS 공식 저장소 사용자 설명서. 명세·적용 대상·요구 구조, 패싯 여섯 종류, IDS 와 IFC 를 함께 불러 불일치 보고를 얻는 검사 흐름을 설명한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/buildingSMART/IDS/development/Documentation/UserManual/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-1365",
      "org": "buildingSMART International (buildingSMART/IDS GitHub)",
      "title": "IDS — Documentation/UserManual/restrictions.md",
      "published": null,
      "url": "https://github.com/buildingSMART/IDS/blob/development/Documentation/UserManual/restrictions.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "IDS 사용자 설명서의 값 제한 절. 열거·패턴·범위·길이 네 가지 복합 제한을 설명한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/buildingSMART/IDS/development/Documentation/UserManual/restrictions.md",
      "source_unopened": false
    },
    {
      "id": "ref-1443",
      "org": "buildingSMART International (buildingSMART/IDS GitHub)",
      "title": "IDS — Documentation/README.md",
      "published": null,
      "url": "https://github.com/buildingSMART/IDS/blob/development/Documentation/README.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "IDS 공식 저장소 문서 안내. 사용자 설명서 위치와, 구현의 읽기·검사 기능 검증용 .ids·.ifc 시험 파일 쌍 250개 이상(TestCases)을 안내한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/buildingSMART/IDS/development/Documentation/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-1442",
      "org": "idealworks",
      "title": "VDA 5050 3.0.0 release (March 2026)",
      "published": "2026-03",
      "url": "https://idealworks.com/en/news/vda5050-300-release-march-2026",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-11",
      "summary": "VDA 5050 작업반 참여 업체의 3.0.0 출시 소식 글. VDMA·VDA 가 2월 17일 3.0.0 을 정식 채택했고 이어 법적 승인 절차가 있었다고 적는다(업체 서술).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/integration/interoperability-standards-and-conformance.md",
      "sections": [
        "5",
        "6",
        "7",
        "8",
        "10",
        "11"
      ],
      "rationale": "갱신(차등): 섹션 5 — 본문 수행 자원 칸의 '경로 계산'을 '선 유도 로봇의 경로 계산·안내'로 정정(f3·f5), 자유 주행 로봇의 경로 자체 계획·공유 병기(f4; 예정 경로 공유 세부는 2026-10-10-area27-s7 41~45행 연결). 현장 유형 보완: '제조 공장' 사례로 Mesh-Up 2025(f31·f32) — 표 머리와 각 칸에 'automatica 2025 전시 시연, 실제 공장 배치 아님'을 밝히고 매트릭스에서 도입 사례로 세지 않음(f33) / 섹션 6(분리 2026-09-25-area28-s6) — 「적합성 시험과 인증」첫 문단 '제조사가 자체 인증하거나' 정정(f15~f18: 적합성 시험 도구(compliance test tools) 사전 준비는 권고, 인증은 인정 시험소, SDK 응용도 개별 시험; 'CTT' 약어는 쓰지 않음). OTTO 문단에 날짜 2026-04-09·기종 4개·'등' 표기 보강, 각주 원문 미열람 해소(f30, 벤더 주장 유지). 선택 필드·재전송·취소 후 갱신 동작 시험표(f6·f7·f8; 재전송 규칙 자체는 2026-10-09-area41-s6 56행·command-and-task-execution-reliability.md 90행 연결). 근거 수준 구분(f38) / 섹션 7(분리 2026-09-25-area28-s7) — VDA 5050 행: 단일 발행일 미확인 유지, 저장소 명세 표지는 날짜 없음(f1), 날짜 비교는 2026-10-10-area20-s7「VDA 5050 3.0.0의 날짜 표시」로 연결하고 PDF 표지 'March 2026'은 [추정] 유지(f2), Idealworks 의 2026-02-17 채택 서술은 벤더 문서 추정으로만(f39). 본문 첫 문단 '주문 배정·경로 계산…' 정정(f3·f5). OPC 행 '자체·독립 시험소 인증' → '인정 시험소 인증(시험 도구는 사전 점검용)'(f17). MassRobotics 행 '(원문 미열람)' 해소와 location 필수 4필드·명령 메시지 부재(f19·f20). 3.0.0 태그 스키마 끝 쉼표 주의사항(f9 사실, 행·열 번호는 싣지 않음; 출처는 태그 파일 ref-1430~ref-1432 와 main 파일 ref-413, f12). OPC UA Robotics 서버 Facet 표 124~127(f21·f22). 국내 표준: KS B 7321-2·KS B ISO 22166-202 는 국가표준 목록 번호·제목만(f24·f25), 제정일·부합화는 미확인(f26). 트랙 반영 제안 2026-10-09-26(건축 도면 자동 인식 단계 2, IDS 1.0 → 7절) 처리: IDS 1.0 공식 표준(2024-06-01)·명세/적용 대상/요구 구조·패싯 여섯 종류·값 제한 네 종류·구현 검증용 시험 파일 묶음을 'BIM 데이터 교환 요구의 적합성 검사 수단'으로 짧게(f40~f44); 제안 요약의 기수·사용자 정의 속성 세트 명명 규칙·OBOS 프록시 관례는 원문 미확인이라 반영하지 않고 다음 실행 후보 / 섹션 8 — vda5050-lab 항목에 v0.2.0 개발자 프리뷰·인증 주장 아님 반영, 각주 '(원문 미열람)' 해소(f13·f14). Wagner 외 WFCS 2026 통신 평가 논문 추가(f34·f36, 적합성 시험과 구별 f37; 원격 조작 표기는 용어집 따름) / 섹션 10 — 42. 분산 시스템·통신·컴퓨팅 구조 연결(f37), 14. 도면·BIM에서 지도 만들기 연결(IDS, f44) / 섹션 11 — oq-005(f1·f2·f39), oq-055(f13~f18·f30·f38), oq-091(f9·f12), oq-026(f24~f26) 부분 근거, 모두 열림 유지. oq-111 은 이번에 새 근거 없음(TTA·KOROS 원문 미확인). 새 질문 2건. 후속 정리(이번 대상 아님): categories/governance-law-and-society/index.md 70행 '경로 계산' 일반화, ref-705 참고문헌 요약의 '자체 인증' 표현, ref-608 발행일 2026-04-09."
    }
  ],
  "glossary_candidates": [],
  "open_questions_new": [
    "VDA 5050 3.0.0 태그 스키마의 끝 쉼표를 고친 수정본을 연동 시험에 쓸 때 공식 PDF·태그와의 차이를 누가 승인하고 어떤 회귀 시험으로 확인하는가? | 관련 영역: 21. 상호운용 표준·적합성, 57. 자산·소프트웨어 수명주기 관리 | 근거: f9 | 종류: 일반",
    "VDA 5050 2.x·3.x 판이 섞인 플릿을 실제 현장에서 전환하면서 판별 스키마 차이와 시험 입력을 어떻게 검증했는지 공개한 기록이 있는가? (관련 기존 질문: oq-091) | 관련 영역: 20. 로봇·제조사 관제 연동, 21. 상호운용 표준·적합성 | 근거: f12 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 23,
    "cross_checked_count": 0,
    "unverified": [
      "VDA 5050 3.0.0 VDA 배포 PDF 표지의 'March 2026' 표기: WebFetch 가 압축 PDF 본문 텍스트를 읽지 못해 대조 불가(103쪽·A4 만 확인) — 출처 항목으로 넣지 않고 f2 에서 [추정] 유지를 제안",
      "f9: 끝 쉼표의 정확한 행·열 번호와 main 브랜치 factsheet·visualization 스키마의 수정 여부는 확인하지 않음(main 은 order.schema 만 확인)",
      "f24·f25: KSSN 상세 페이지에서 번호·제목만 보여 제정일·부합화(IDT 여부)·고시번호·쪽수 미확인",
      "TTAK.KO-10.1295-Part8: 웹 검색에서 찾지 못했고 이전 브리프의 TTA 목록 URL 은 검증에서 HTTP 400 — 출처·finding 에서 뺌",
      "KOROS 1148-8:2025 제정일과 TTA 표준과의 관계: 원문 봇 차단으로 미확인 — finding 에서 뺌",
      "ISO 21423 단계·범위: iso.org 미열람 — 21번에는 새로 쓰지 않음",
      "VDA5050 이슈 #660: 실재 미확인 — 출처에서 뺌",
      "Wagner 외 본문의 평가 시나리오(로봇 수·주문 시간·원격 조작 구간)와 향후 과제 문구: 저자 공개본 PDF 텍스트를 읽지 못해 미확인",
      "IDS 의 기수(필수·선택·금지), 사용자 정의 속성 세트 명명 규칙, 뉴질랜드 OBOS 프록시 관례(트랙 반영 제안 요약 항목): 이번에 원문으로 확인하지 못함",
      "f39: Idealworks 의 2026-02-17 채택 서술은 VDA 자료로 확인되지 않음",
      "VDA·VDMA 공인 적합성 인증 제도의 존재·부재(oq-055)는 확정 못 함"
    ],
    "scope_violations": [
      "f31~f33: Mesh-Up 2025 는 automatica 2025 전시 시연이며 실제 공장 배치가 아님. site_type '제조 공장'은 시연이 겨냥한 현장 유형을 뜻함",
      "f34~f37: 무선망·Open RAN 통신 평가는 42. 분산 시스템·통신·컴퓨팅 구조 쪽 내용이라 21번에는 적합성 시험과 구별되는 통신 평가 연구로만 씀",
      "f21·f22: OPC UA Robotics 정보모델은 4. 이기종 로봇 등록에서 이미 다루므로 21번에는 Facet·인증 범위 요구만 씀",
      "f40~f44: IDS 는 건물 정보 모델 데이터 교환 표준으로 14. 도면·BIM에서 지도 만들기·건축 도면 자동 인식 트랙 쪽 내용이 많으므로 21번에는 적합성 검사 수단으로만 짧게 씀"
    ],
    "budget_used": {
      "queries": 5,
      "sources": 14
    },
    "limits": "재실행 1회차. 반려 사유 1(신규 참고문헌 id 충돌): 직전 실행 2026-10-10-06 이 같은 예약 구간에서 쓴 ref-1424~ref-1428 과 기존 출처 ref-1429(Franke 외)를 피해 신규 출처를 예약 구간 안의 ref-1430~ref-1443 으로 다시 매겼다. VDA 카탈로그는 기존 id ref-1412 을 재사용하고(이전 브리프의 ref-1412 표기 철회), OPC 개요는 ref-1434, Mesh-Up 은 ref-1436, Wagner 외는 ref-1437 로 옮겼다. 이전 브리프의 ref-1424(이슈 #660)·ref-1425(TTA 목록)·ref-1426(KSSN, 이제 ref-1435)·ref-1428·ref-1429 할당은 모두 없앴다. 실행 컨텍스트의 next_ref_id(ref-1412)가 이미 사용 중이라 구간 안 미사용 번호를 썼다 — pipeline/agent_runner.py 의 next_ref_id 계산 확인 필요. (관련 finding: f9·f16·f25·f31·f34) 반려 사유 2(원문 열람 재현 실패): ref-1412 PDF 는 이번에도 텍스트를 읽지 못해 출처에서 빼고 f1 을 저장소 마크다운 표지 사실로 바꿨다(관련 finding: f1·f2). KSSN 두 페이지는 다시 열었으나 번호·제목만 보여 f24·f25 를 그 범위의 사실로 줄이고 f26 은 열린 질문 유지 의견으로 바꿨다. TTA 목록은 웹 검색으로도 확인 못 해 f28 을 지웠다. Wagner 외는 PDF 텍스트를 읽지 못해 f35 를 지우고, f36 은 연구실 소개문(ref-1438)으로 확인한 가상 무선·실제 무선 구분만 남겼다. f10(파서별 행·열 번호)은 재현 근거가 없어 지웠다. 이번에 fetched: true 로 적은 출처는 모두 이번 실행에서 WebFetch 또는 raw 경로로 다시 열었고(ref-031 은 입력 원문 텍스트 + 3.0.0 태그 raw), fetch_url 이 다른 경우 적었다. 반려 사유 3(미확인 출처·전언 finding): ref-1424(이슈 #660)를 출처에서 빼고 f11·f23·f27 을 지웠으며, ref-159·ref-710 은 근거 finding 이 없어 sources 에서 뺐다. f29 는 지웠다(oq-111 열림 유지). 반려 사유 4(트랙 반영 제안 미처리): buildingSMART 공식 페이지와 공식 저장소 문서로 IDS 1.0 을 조사해 f40~f44 를 냈고 7절 반영안을 rationale 에 적었다. 제안 요약의 기수·사용자 정의 속성 세트·OBOS 프록시는 확인 못 해 다음 실행 후보로 남긴다. required_fixes 대응: [의견]은 모두 claim 첫머리에 '구축자 의견: '을 붙였다. f9 출처를 확인한 태그 파일별 항목(ref-1430~ref-1432)과 main 파일(ref-413)로 바꾸고 ref-051 은 뺐다. f13 은 'Developer Preview'로 재서술하고 'Synthetic Demo Preview' 인용을 없앴다. f21 표 번호를 124~127 로 고쳤다. ref-608 발행일을 2026-04-09 로 고쳤다. f31~f33 에 'automatica 2025 전시 시연, 실제 공장 배치 아님'을 넣었다. 새 열린 질문 가운데 TTA–KOROS 질문은 뺐고, 2.x·3.x 전환 질문의 근거를 f12 와 oq-091 로 바꿨다. 용어: '원격 조작' 표기, 'CTT' 대신 '적합성 시험 도구(compliance test tools)'. 열린 질문 해결 제안 없음: oq-005 근거 f1·f2·f39, oq-055 근거 f13~f18·f30·f38, oq-091 근거 f9·f12, oq-026 근거 f24~f26 (모두 부분 근거). 검색 5회/30, 신규 출처 14건/15. 재사용 9건(ref-031·ref-032·ref-1412·ref-408·ref-705·ref-230·ref-034·ref-138·ref-608, 모두 이번에 다시 엶). IDS 관련 URL 이 트랙 실행에서 이미 등록됐다면 퍼블리셔가 같은 URL 로 합쳐야 한다(참고문헌 목록 요약본에 없어 확인 못 함). 교차 확인 0건(VDA 계열 자료, 같은 저장소 파일, OPC 두 페이지는 각각 같은 기관). 정정 요청 없음. 용어 후보 없음(정보 전달 명세·적합성 시험·원격 조작은 용어집에 있음)."
  }
}
```

### runs/2026-10-11-01/verification.json

```json
{
  "run_id": "2026-10-11-01",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문 data/source_texts/ref-031.txt 의 머리는 'VDA 5050' 아래 'Version 3.0.0'만 적고 날짜가 없다. PDF 표지를 확인하지 못했다는 부분은 조사 과정에 관한 서술이다. PDF 는 이번 브리프의 출처에서 빠졌다. 직전 반려 사유 ②가 해소됐다."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 카탈로그 'March 17, 2026'(ref-1412)과 보도자료 'Berlin, April 20, 2026'(ref-032)은 직전 검증에서 대조했다. 구축자 의견임을 밝혔다. PDF 표지 'March 2026'은 이번 브리프의 출처가 아니다. 본문에서는 20번 주제 페이지의 [추정] 문장으로 연결만 한다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문 ref-031 의 §5.3 'Route calculation and guidance of line-guided mobile robots'와 §5.4 'line-guided or freely navigating'. 같은 직역이 2026-10-09-area41-s6 에도 있다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 직전 검증에서 ref-032 를 다시 열어 'detailed route planning takes place on the vehicle itself'와 path sharing 문구를 확인했다. 보도자료의 설명이고, 대상은 자율도가 높은 로봇이다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f3·f4 가 뒷받침하는 구축자 의견이다. 정정 대상 문장(5절 수행 자원 칸)이 입력 페이지에 있다. 대분류 페이지 governance-law-and-society/index.md 의 같은 일반화는 이번 대상이 아니다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 직전 1차 검증에서 3.0.0 태그 raw 명세의 §7.1.1 을 대조했다('shall not ignore the field', 'Fleet control shall only send optional fields that the mobile robot supports'). 이번 재검증에서는 다시 열지 않았다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 직전 검증에서 §6.1.4.2·§6.1.4.5·§6.1.3.1 을 3.0.0 태그 마크다운으로 대조했다. 재전송 규칙 자체는 2026-10-09-area41-s6 과 29. 명령·작업 실행의 신뢰성 페이지에 이미 있다. 이번에는 시험 기대값 관점만 새로 쓰고 나머지는 연결한다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f6·f7 조항을 시험 행으로 옮긴 구축자 의견이다. 본문에서 VDA·VDMA 공식 인증 항목이 아님을 밝혀야 한다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 직전 검증에서 raw 3.0.0 태그의 order·factsheet·visualization.schema 끝 쉼표와 main order.schema 의 수정 상태를 직접 열어 확인했다. 출처를 태그 파일별 항목(ref-1430~ref-1432)과 main 파일(ref-413)로 바꿔 서지 불일치가 해소됐다. 행·열 번호는 싣지 않는다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f9 에서 나온 구축자 의견이다. 'PDF 가 유효' 문구는 기존 각주 ref-634(입력 원문)에 있다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 직전 검증에서 커밋 4a1a812 README Status 절을 대조했다('Developer Preview', 'not a public-alpha or certification claim'). 'Synthetic Demo Preview' 인용은 없어졌다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f13 에서 나온 구축자 의견이다. 기존 8절의 [추정] 문장과 어긋나지 않는다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 직전 검증에서 How to Certify 페이지를 다시 열어 'compliance test tools' 사전 준비 권고와 'The tools are used by the lab'을 확인했다. CTT 약어는 쓰지 않는다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 직전 검증에서 Overview & Benefits 를 다시 열어 'accredited Certification Lab'과 SDK 기반 응용의 개별 인증 시험 문구를 확인했다. ref-705 와 같은 기관이라 교차 확인은 아니다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 두 페이지에 self-certification 경로가 없다. 정정 대상인 분리 6·7절 문장과 ref-705 참고문헌 요약은 입력에 없어 직접 대조하지 못했다. 스토리텔러는 실제로 있는 문장에만 정정을 적용한다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f15~f17 에서 나온 구축자 의견이다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문 data/source_texts/ref-230.txt 에서 최상위 oneOf 가 identityReport·statusReport 를 참조하고, location.required 가 [x, y, angle, planarDatum]이며, 명령 메시지 정의가 없다. 이 출처는 ref-230(JSON 스키마)이고, 기존 페이지가 쓴 ref-253(README)과는 다른 문서다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f19 에서 나온 구축자 의견이다. '(원문 미열람)' 해소는 ref-230 에만 해당하고 ref-253 에는 해당하지 않는다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 직전 검증에서 OPC-40010-1/full(1.02판, 2025-09-08) §11.2.2 와 표 124~127 의 Mandatory/Optional 구분을 확인했다. 표 번호가 바르게 고쳐졌다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f21 에서 나온 구축자 의견이다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 이번에 KSSN 상세(K001010147546)를 다시 열었다. 번호 KS B 7321-2 와 제목이 일치하고, 제정일·부합화·고시번호는 표시되지 않는다. 브리프가 주장을 열람 범위로 좁혔으므로 직전 강등 사유가 해소됐다."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 이번에 KSSN 상세(K001010158171)를 열었다. 번호 KS B ISO 22166-202 와 제목 '로봇 — 서비스 로봇의 모듈화 — 제202부: 소프트웨어 모듈용 정보 모델'이 일치하고, 제정일·IDT·고시번호는 표시되지 않는다."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: oq-026 을 열림으로 유지하자는 구축자 의견이다(신뢰도 low). 제정일·부합화·대체 관계는 본문에 쓰지 않고 미확인으로 둔다. 직전 판정 '열린 질문 이동'의 취지와 같다."
    },
    {
      "finding_id": "f30",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 직전 검증에서 2026-04-09(Kitchener), OTTO 100·600·1200·1500, Idealworks·NAiSE·SYNAOS 를 대조했다. 시험 판·항목·기관은 없다. 벤더 주장이므로 [추정]을 유지하고 vendor_claim 을 표시한다."
    },
    {
      "finding_id": "f31",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 직전 검증에서 VDMA Mesh-Up 페이지를 대조했다(2025-06-24~27, nine companies, MHP 마스터 관제). 전시 시연이며 실제 공장 배치가 아니라는 표시가 들어갔다."
    },
    {
      "finding_id": "f32",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 'is not demonstrated live at automatica by the Mesh-Up' 문구를 직전 검증에서 대조했다."
    },
    {
      "finding_id": "f33",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f31·f32 에서 나온 구축자 의견이다."
    },
    {
      "finding_id": "f34",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 직전 검증에서 TUHH 저장소 초록과 서지를 대조했다. 이번 ComNets 소개문에서도 저자 6명, WFCS(Offenburg, 2026-04) 서지가 일치한다. 원격 조작 확장은 논문이 제안한 것이며 표준이 채택한 기능이 아니다."
    },
    {
      "finding_id": "f36",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 이번에 ComNets 소개문(2026-04-24)을 열었다. 'highly reproducible virtual-radio testbed', 'real-world over-the-air validation setup', tudo-cni/VDA-5050-Traffic-Generator 저장소가 있고, 정량 결과와 로봇 수는 없다. 근거를 연구실 소개문으로 바꿔 직전 강등 사유가 해소됐다."
    },
    {
      "finding_id": "f37",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f34·f36 에서 나온 구축자 의견이다. 용어집 표기 '원격 조작'을 쓴다."
    },
    {
      "finding_id": "f38",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f13·f30·f32·f15~f17 이 뒷받침하는 구축자 의견이다. oq-055 의 부분 근거로만 쓴다."
    },
    {
      "finding_id": "f39",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 이번에 idealworks 글을 열었다. 날짜는 'March 2026', 문구는 'On February 17th, VDMA and VDA formally adopted the 3.0.0 release'이고 뒤이어 legal sign-off 를 적는다. 다만 Idealworks 가 'VDA 5050 작업반 참여 업체'라는 표현은 원문에 명시되지 않았다('at the heart of it', 'core team', 'On Idealworks' initiative'로 참여를 시사하는 정도다). 업체 서술이므로 [추정]을 유지하고 수식어는 고친다."
    },
    {
      "finding_id": "f40",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 이번에 buildingSMART IDS 페이지를 열었다. 'On 1st June 2024 the IDS has been approved and became the official buildingSMART standard!', 'allows for automatic compliance checking of IFC models', 'All the versions of IDS prior to 1.0 are not an official standard'가 있다."
    },
    {
      "finding_id": "f41",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 이번에 raw UserManual/README.md 를 열었다. 명세·적용 대상·요구 구조, 'Both applicability and requirements are built with facets', 엔터티·속성·분류·속성 값·재료·partOf 여섯 패싯, IDS 와 IFC 를 함께 불러 불일치 보고를 얻는 흐름이 있다."
    },
    {
      "finding_id": "f42",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 이번에 raw restrictions.md 를 열었다. 열거·패턴·범위(포함·제외)·길이 네 제한이 있고, 기수는 이 문서에 없다."
    },
    {
      "finding_id": "f43",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 이번에 raw Documentation/README.md 를 열었다. 'a suite of over 250 test file pairs (.ids and .ifc) for verifying the correctness of the software implementation reading and checking capabilities'가 있다."
    },
    {
      "finding_id": "f44",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: f40·f41·f43 에서 나온 구축자 의견이다. 트랙 반영 제안 2026-10-09-26 은 일부만 처리한다. 기수·사용자 정의 속성 세트 명명 규칙·OBOS 프록시 관례는 반영하지 않는다."
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
      "f3 의 선 유도 경로 계산 직역은 2026-10-09-area41-s6 과, f7 의 재전송 규칙은 2026-10-09-area41-s6·29. 명령·작업 실행의 신뢰성과, f4 의 경로 공유는 2026-10-10-area27-s7 과, f19 의 statusReport 는 2026-10-10-area20-s7 과, f21 의 판·범위는 2026-09-29-area04-s7 과, f1·f2·f39 의 날짜 표시는 2026-10-10-area20-s7「VDA 5050 3.0.0의 날짜 표시」와 겹친다. 브리프 제안대로 새로 쓰지 않고 연결한다.",
      "f39(Idealworks 2026-02-17 채택 서술)는 VDA 공식 자료의 날짜 표시(카탈로그 2026-03-17·보도자료 2026-04-20)와 충돌한다. 한쪽을 고르지 않고 함께 제시하며 oq-005 에 출처 충돌로 올린다.",
      "참고문헌 id: 직전 반려 사유였던 id 충돌은 신규 id 를 ref-1430~ref-1443 으로 다시 매겨 2026-10-10-06 의 ref-1412~ref-1429 와 겹치지 않는다. 다만 입력의 참고문헌 목록이 요약본(21건)이라 ref-1430~ref-1443 이 다른 실행에서 이미 쓰였는지는 검증하지 못했다. IDS URL 이 트랙 실행 2026-10-09-26 에서 이미 등록됐을 수 있다."
    ]
  },
  "terminology": {
    "ok": true,
    "conflicts": []
  },
  "quotation_check": {
    "ok": true,
    "issues": [
      "ref-1362(f41)의 evidence 에 직접 인용이 두 개, ref-032(f2·f4)에 두 개 있다. 페이지에서는 출처당 직접 인용을 1회 이하로 하고 나머지는 재서술한다."
    ]
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "f39: '작업반 참여 업체인 Idealworks'를 '3.0.0 작업에 참여했다고 밝힌 업체 Idealworks'로 고친다. [추정]을 유지하고 업체 서술임을 밝힌다. VDA 카탈로그(2026-03-17)·보도자료(2026-04-20) 날짜와 함께 제시하고 oq-005 에 출처 충돌로 덧붙인다 — 원문이 작업반 참여를 명시하지 않는다.",
    "f2: VDA 5050 행에 PDF 표지 'March 2026'을 새 각주나 [사실]로 쓰지 않는다. 20번 주제 페이지의 날짜 절로 연결만 한다 — PDF 는 이번 브리프의 출처가 아니다.",
    "f19·f20: MassRobotics 행의 스키마 사실(location 필수 4필드, 명령 메시지 부재)에는 각주 ref-230 을 단다. 기존 각주 ref-253(README)의 '(원문 미열람)' 표시는 지우지 않는다 — 이번에 연 문서는 ref-230 이고 ref-253 은 열지 않았다.",
    "f13·f14: 8절 vda5050-lab 항목은 ref-408 의 자기 기술만 [사실]로 쓰고 '(원문 미열람)'을 지운다. 같은 줄의 vda5050-sim(ref-407)은 이번에 열지 않았으므로 [추정]과 '(원문 미열람)'을 유지한다(문장을 나눈다).",
    "f15~f18: '제조사가 자체 인증하거나'·'자체·독립 시험소 인증' 정정은 분리 6·7절과 참고문헌 요약에 그 문구가 실제로 있을 때만 적용한다. reference_updates 로 ref-705 의 요약을 '적합성 시험 도구 사전 점검은 권고, 인증은 인정 시험소'로 고치고 '(원문 미열람)'을 지우며 접근일을 2026-10-11 로 바꾼다.",
    "f30: ref-608 의 발행일을 2026-04-09 로 고치고 '(원문 미열람)'을 지운다(reference_updates). 본문은 [추정]과 '벤더 주장'을 유지한다.",
    "f24~f26: 7절 국내 표준에는 KS B 7321-2·KS B ISO 22166-202 의 번호와 제목만 [사실][^ref-138]·[^ref-1435]로 쓴다. 제정일·부합화(IDT)·고시번호·대체 관계는 '미확인'으로 두고 oq-026 은 열림을 유지한다.",
    "f31~f33: Mesh-Up 은 5절 '제조 공장' 사례 표의 머리와 각 칸에 'automatica 2025 전시 시연, 실제 공장 배치 아님'을 적는다. site_matrix_updates 에는 넣지 않는다 — 도입 사례가 아니다.",
    "f34·f36·f37: Wagner 외는 8절에서 VDA 5050 통신 지연·오버헤드 평가 연구로 소개한다. 원격 조작 확장은 '논문 제안이며 표준 채택 기능 아님'으로 밝히고, 로봇 수·시간 같은 수치는 쓰지 않는다. 각주는 ref-1437 과 ref-1438 이다.",
    "f40~f44: IDS 1.0 은 7절에 'IFC 데이터 교환 요구의 적합성 검사 수단'으로 짧게 둔다(로봇–관제 메시지 적합성 시험과 구별한다). 트랙 반영 제안 2026-10-09-26 가운데 기수·사용자 정의 속성 세트 명명 규칙·OBOS 프록시 관례는 반영하지 않고, 처리 결과를 '일부 반영'으로 기록한다 — 원문으로 확인하지 못했다.",
    "10절: [42. 분산 시스템·통신·컴퓨팅 구조](../platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md)(f37)와 [14. 도면·BIM에서 지도 만들기](../space-and-map-model/maps-from-floor-plans-and-bim.md)(f44) 연결을 더하고, 프런트매터 related_areas 에 14·42 를 더한다.",
    "f9·f12: 3.0.0 태그 스키마의 끝 쉼표는 ref-1430~ref-1432 로, main 의 상태는 ref-413 으로 각주를 단다. 행·열 번호와 파서별 오류 메시지는 쓰지 않는다.",
    "f5: 이번에는 대상 페이지(5절 수행 자원 칸과 분리 7절 본문)만 고친다. governance-law-and-society/index.md 의 같은 일반화는 고치지 않는다 — 다른 페이지이며 오늘 갱신 예산 밖이다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인(재조사 1회차 브리프). 확인 37건, 미확인 0건, 교차 확인 0건. 강등: 없음(직전 반려 때 강등 대상이던 f1·f24·f25·f36 은 주장을 열람 범위로 좁혀 다시 냈다). 원문 미열람 출처: 없음. 이번에 새로 연 출처는 ref-1435·ref-138(KSSN, 번호·제목만 표시), ref-1438(ComNets 소개문), ref-1439~ref-1365·ref-1443(buildingSMART IDS), ref-1442(Idealworks)다. 나머지는 직전 1차 검증의 원문 대조를 따랐다. 직전 반려 사유의 처리: ① 참고문헌 id 충돌은 신규 id 를 ref-1430~ref-1443 으로 다시 매겨 해소했다. ② 재현되지 않은 열람 주장은 출처에서 빼거나 열람 범위로 줄였다. ③ 미확인 출처와 전언 finding(이슈 #660, TTA 목록, ISO 21423, KOROS)은 뺐다. ④ 트랙 반영 제안(IDS 1.0)은 f40~f44 로 일부 처리했다. 정정 요청 없음. 주의: VDA 5050 3.0.0 의 날짜는 VDA 계열 자료와 참여 업체 글이 서로 다르게 표시하므로(카탈로그 2026-03-17, 보도자료 2026-04-20, Idealworks 글 2026-02-17 채택) 단일 발행일을 확정하지 않는다. 적합성 시험 기대값 표와 승인 근거 수준 구분은 구축자 제안이며, VDA·VDMA 공식 인증 항목이 아니다. Mesh-Up 은 전시 시연으로, 실제 공장 도입 사례가 아니다. 입력의 참고문헌 목록이 요약본이라 ref-1430~ref-1443 이 다른 실행의 id 와 겹치지 않는지는 퍼블리셔가 확인해야 한다. 분리 주제 페이지(2026-09-25-area28-s6·s7·s11)를 고치는 것이 하루 갱신 상한(2건)에 걸리는지도 실행 스크립트가 확인해야 한다. 검증 검색 0회, 열람 8회.",
  "retry_reason": null
}
```

### runs/2026-10-11-01/pages.json

```json
{
  "run_id": "2026-10-11-01",
  "outline": [
    {
      "path": "docs/categories/integration/interoperability-standards-and-conformance.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 1900,
      "summary": "물류창고 사례의 수행 자원 칸에서 VDA 5050 3.0.0 의 관제 쪽 경로 계산을 선 유도 로봇으로 한정하고 자유 주행 로봇의 경로 자체 계획·공유를 병기한다. [사실][^ref-031][^ref-032] 제조 공장 사례로 Mesh-Up 2025 전시 시연을 더하되 실제 공장 배치가 아님을 표 머리와 각 칸에 밝힌다. [사실][^ref-1436]",
      "planned_findings": [
        "f3",
        "f4",
        "f5",
        "f31",
        "f32",
        "f33"
      ]
    },
    {
      "path": "docs/categories/integration/interoperability-standards-and-conformance.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1950,
      "summary": "OPC 적합성 체계는 제조사의 시험 도구 사전 점검(권고)과 인정 시험소 인증으로 나뉘며 제조사 자체 인증 경로는 확인한 안내에 없다. [사실][^ref-705][^ref-1434] VDA 5050 연동 승인 근거는 자체 진단·벤더 간 인증 발표·전시 시연·인정 시험소 인증을 서로 다른 수준으로 기록하고, 선택 필드·재전송·취소 후 갱신 동작 시험표를 둔다. [의견][^ref-031] 첫 단락에 2026-09-25 분리 페이지 링크를 둔다.",
      "planned_findings": [
        "f6",
        "f7",
        "f8",
        "f15",
        "f16",
        "f17",
        "f18",
        "f30",
        "f38"
      ]
    },
    {
      "path": "docs/categories/integration/interoperability-standards-and-conformance.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 2650,
      "summary": "VDA 5050 3.0.0 은 저장소 표지에 날짜가 없고 VDA 자료·업체 글의 날짜가 서로 달라 발행일을 미확인으로 둔다. [사실][^ref-031] 3.0.0 태그 스키마 끝 쉼표, OPC UA Robotics 서버 Facet, MassRobotics 스키마 범위, 국내 KS 두 건, IDS 1.0 을 적합성 관점에서 짧게 정리한다. [사실][^ref-1430][^ref-034][^ref-230][^ref-1439] 첫 단락에 2026-09-25 분리 페이지(표준 비교표) 링크를 둔다.",
      "planned_findings": [
        "f1",
        "f2",
        "f9",
        "f12",
        "f19",
        "f20",
        "f21",
        "f22",
        "f24",
        "f25",
        "f26",
        "f39",
        "f40",
        "f41",
        "f42",
        "f43",
        "f44"
      ]
    },
    {
      "path": "docs/categories/integration/interoperability-standards-and-conformance.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 1500,
      "summary": "vda5050-lab 은 인증 주장이 아닌 개발자 프리뷰라고 스스로 밝히는 진단 도구로 보조 후보로만 둔다. [사실][^ref-408] Wagner 외(WFCS 2026)는 VDA 5050 통신 지연·오버헤드 평가 연구로 적합성 시험과 구별한다. [사실][^ref-1437]",
      "planned_findings": [
        "f13",
        "f14",
        "f34",
        "f36",
        "f37"
      ]
    },
    {
      "path": "docs/categories/integration/interoperability-standards-and-conformance.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 350,
      "summary": "42. 분산 시스템·통신·컴퓨팅 구조(통신 평가)와 14. 도면·BIM에서 지도 만들기(IDS) 연결을 더한다. [의견]",
      "planned_findings": [
        "f37",
        "f44"
      ]
    },
    {
      "path": "docs/categories/integration/interoperability-standards-and-conformance.md",
      "section": "11. 열린 질문",
      "budget_chars": 950,
      "summary": "oq-005·oq-055·oq-091·oq-026 에 부분 근거를 더하고 모두 열림을 유지하며 새 질문 두 건을 올린다. [추정][^ref-1442] 첫 단락에 2026-09-25 분리 페이지 링크를 둔다.",
      "planned_findings": [
        "f1",
        "f2",
        "f9",
        "f12",
        "f24",
        "f25",
        "f26",
        "f38",
        "f39"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/integration/interoperability-standards-and-conformance.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "차등 갱신: 5절 수행 자원 칸 경로 계산을 선 유도 로봇으로 정정·자유 주행 로봇 경로 공유 병기, 제조 공장 전시 시연 사례(Mesh-Up 2025, 실제 공장 배치 아님) 추가; 6절 OPC 시험 도구 사전 점검과 인정 시험소 인증 구분·승인 근거 수준 표·VDA 5050 동작 시험표; 7절 VDA 5050 3.0.0 날짜(출처 충돌)·태그 스키마 끝 쉼표·OPC UA Robotics Facet·MassRobotics 스키마·KS 두 건·IDS 1.0(트랙 반영 제안 2026-10-09-26 일부 반영); 8절 vda5050-lab 자기 기술 반영·vda5050-sim 분리·Wagner 외 추가; 10절 14·42번 연결; 11절 부분 근거와 새 질문 2건; 6·7·11절 첫 단락에 2026-09-25 분리 페이지(area28-s6·s7·s11) 링크 유지; 프런트매터 sources 에 기존 ref-636·ref-637·ref-708·ref-710 유지; 13절 각주 갱신(ref-408·ref-705 원문 열람 반영, 신규 각주)",
      "patches": [
        {
          "section": "5. 적용 사례 (현장 유형 명시)",
          "action": "replace",
          "frontmatter": {
            "related_areas": [
              14,
              20,
              22,
              42,
              48,
              51,
              54,
              57
            ],
            "sources": [
              "ref-004",
              "ref-031",
              "ref-032",
              "ref-034",
              "ref-051",
              "ref-138",
              "ref-230",
              "ref-253",
              "ref-407",
              "ref-408",
              "ref-560",
              "ref-608",
              "ref-634",
              "ref-635",
              "ref-636",
              "ref-637",
              "ref-638",
              "ref-639",
              "ref-704",
              "ref-705",
              "ref-706",
              "ref-707",
              "ref-708",
              "ref-709",
              "ref-710",
              "ref-1412",
              "ref-1430",
              "ref-1431",
              "ref-1432",
              "ref-413",
              "ref-1434",
              "ref-1435",
              "ref-1436",
              "ref-1437",
              "ref-1438",
              "ref-1439",
              "ref-1362",
              "ref-1365",
              "ref-1442",
              "ref-1443"
            ],
            "last_run": "2026-10-11",
            "confidence": "medium"
          },
          "content": "(절 본문 생략 — runs/2026-10-11-01/pages/categories/integration/interoperability-standards-and-conformance.md 의 해당 절을 본다)"
        },
        {
          "section": "6. 대표 접근법과 기술",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-01/pages/categories/integration/interoperability-standards-and-conformance.md 의 해당 절을 본다)"
        },
        {
          "section": "7. 관련 표준·프레임워크·오픈소스",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-01/pages/categories/integration/interoperability-standards-and-conformance.md 의 해당 절을 본다)"
        },
        {
          "section": "8. 대표 연구와 자료",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-01/pages/categories/integration/interoperability-standards-and-conformance.md 의 해당 절을 본다)"
        },
        {
          "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-11-01/pages/categories/integration/interoperability-standards-and-conformance.md 의 해당 절을 본다)"
        },
        {
          "section": "11. 열린 질문",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-01/pages/categories/integration/interoperability-standards-and-conformance.md 의 해당 절을 본다)"
        },
        {
          "section": "13. 참고 자료 (각주)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-11-01/pages/categories/integration/interoperability-standards-and-conformance.md 의 해당 절을 본다)"
        }
      ]
    },
    {
      "path": "docs/topics/2026/2026-10-11-area21-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 21. 상호운용 표준·적합성 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(2,916자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-11-area21-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 21. 상호운용 표준·적합성 의 \"6. 대표 접근법과 기술\" 절(2,060자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-11-area21-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 21. 상호운용 표준·적합성 의 \"8. 대표 연구와 자료\" 절(1,461자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-11-area21-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 21. 상호운용 표준·적합성 의 \"11. 열린 질문\" 절(1,079자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-11-area21-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 21. 상호운용 표준·적합성 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(630자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-10-11 | 21. 상호운용 표준·적합성 | 5절 경로 계산 책임을 선 유도 로봇으로 정정하고 제조 공장 전시 시연 사례 추가, 6절 OPC 시험 도구 사전 점검과 인정 시험소 인증 구분·승인 근거 수준·VDA 5050 동작 시험표, 7절 VDA 5050 날짜 출처 충돌·태그 스키마 끝 쉼표·OPC UA Robotics Facet·MassRobotics 스키마·KS 두 건·IDS 1.0(트랙 반영 제안 2026-10-09-26 일부 반영), 8절 vda5050-lab 자기 기술·Wagner 외, 10절 14·42번 연결, 11절 부분 근거와 새 질문 2건, 2026-09-25 분리 페이지 링크 유지 | run 2026-10-11-01",
  "index_updates": {
    "home_recent": "2026-10-11 — 21. 상호운용 표준·적합성: VDA 5050 경로 계산 책임 정정, 적합성 시험과 인증의 근거 수준 구분과 동작 시험표, 3.0.0 날짜 출처 충돌과 태그 스키마 끝 쉼표, IDS 1.0 적합성 검사 추가",
    "category_recent": "2026-10-11 — 21. 상호운용 표준·적합성: 5·6·7·8·10·11절 차등 갱신(선 유도 로봇 경로 계산 정정, 제조 공장 전시 시연 사례, OPC 인정 시험소 인증 구분, VDA 5050 동작 시험표, OPC UA Robotics Facet, KS 두 건, IDS 1.0, Wagner 외 통신 평가)",
    "area_recent": "2026-10-11 — 21. 상호운용 표준·적합성: 차등 갱신 5·6·7·8·10·11·13절. 트랙 반영 제안 2026-10-09-26(IDS 1.0) 일부 반영, 2026-09-25 분리 주제 페이지(area28-s6·s7·s11) 링크 유지, 그 페이지들의 정정은 다음 실행으로 넘김"
  },
  "glossary_updates": [],
  "reference_updates": [
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "VDA 5050 3.0.0 명세 마크다운 원문. 입력 원문 텍스트와 3.0.0 태그 raw 파일로 관제–로봇 기능 분담(선 유도 로봇 경로 계산·안내), 선택 필드 의무, 오류 응답 조항, 표지에 날짜가 없음을 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/interoperability-standards-and-conformance.md"
      ]
    },
    {
      "id": "ref-032",
      "org": "VDA(Verband der Automobilindustrie)",
      "title": "Version 3.0 of VDA 5050 released",
      "published": "2026-04-20",
      "url": "https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "VDA 5050 3.0 발행 보도자료. 머리 날짜 2026-04-20 과, 자율도가 높은 로봇이 경로를 스스로 계획하고 경로 공유로 중앙 관제와 공유하는 구성 설명을 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/interoperability-standards-and-conformance.md"
      ]
    },
    {
      "id": "ref-1412",
      "org": "VDA(Verband der Automobilindustrie)",
      "title": "VDA 5050",
      "published": "2026-03-17",
      "url": "https://www.vda.de/en/news/publications/publication/vda-5050",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "VDA 발행물 카탈로그의 VDA 5050 Version 3.0.0 항목. 표시 날짜 2026-03-17 을 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/interoperability-standards-and-conformance.md"
      ]
    },
    {
      "id": "ref-1430",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/order.schema (tag 3.0.0)",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/3.0.0/json_schemas/order.schema",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "공식 저장소 3.0.0 태그의 주문 메시지 JSON 스키마. 궤적 제어점 weight 속성 뒤 닫는 괄호 앞 끝 쉼표를 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/interoperability-standards-and-conformance.md"
      ]
    },
    {
      "id": "ref-1431",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/factsheet.schema (tag 3.0.0)",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/3.0.0/json_schemas/factsheet.schema",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "공식 저장소 3.0.0 태그의 팩트시트 JSON 스키마. physicalParameters 치수 항목의 unit 줄 뒤 끝 쉼표를 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/interoperability-standards-and-conformance.md"
      ]
    },
    {
      "id": "ref-1432",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/visualization.schema (tag 3.0.0)",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/3.0.0/json_schemas/visualization.schema",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "공식 저장소 3.0.0 태그의 시각화 메시지 JSON 스키마. properties 끝과 weight 속성의 끝 쉼표를 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/interoperability-standards-and-conformance.md"
      ]
    },
    {
      "id": "ref-413",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/order.schema (main)",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/order.schema",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "공식 저장소 main 브랜치의 주문 메시지 JSON 스키마. 3.0.0 태그와 달리 weight 속성에 끝 쉼표가 없음을 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/interoperability-standards-and-conformance.md"
      ]
    },
    {
      "id": "ref-408",
      "org": "ekusiadadus (GitHub)",
      "title": "vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces)",
      "published": null,
      "url": "https://github.com/ekusiadadus/vda5050-lab",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "MQTT 기록에서 VDA 5050 주문·재연결·취소 실패를 진단하는 개인 프로젝트 README. 커밋 4a1a812 고정본에서 v0.2.0 이 개발자 프리뷰이고 인증 주장이 아니며 실제 고객 기록·외부 시험 대상·실물 하드웨어 실행을 검증하지 않았다는 한계 선언을 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/interoperability-standards-and-conformance.md"
      ]
    },
    {
      "id": "ref-705",
      "org": "OPC Foundation",
      "title": "How to Certify - OPC Foundation",
      "published": null,
      "url": "https://opcfoundation.org/certification/how-to-certify/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "OPC 제품 인증 절차 안내. 적합성 시험 도구(compliance test tools)로 하는 제조사의 사전 점검은 권고이고, 인증은 인정 시험소가 그 도구로 시험한다. 제조사 자체 인증 경로는 안내에 없다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/interoperability-standards-and-conformance.md"
      ]
    },
    {
      "id": "ref-1434",
      "org": "OPC Foundation",
      "title": "Overview & Benefits — OPC Foundation Certification",
      "published": null,
      "url": "https://opcfoundation.org/certification/overview-benefits/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "OPC Foundation 인증 프로그램 개요. 인증 제품은 재단이 인정한 인증 시험소에서 시험을 거치며, 인증 SDK 를 쓴 응용도 각자 인증 시험이 필요하다고 설명한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/interoperability-standards-and-conformance.md"
      ]
    },
    {
      "id": "ref-230",
      "org": "MassRobotics",
      "title": "MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json",
      "published": null,
      "url": "https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "MassRobotics AMR 상호운용 표준의 공식 JSON 스키마. 커밋 f9357a4 고정본에서 최상위 oneOf(identityReport·statusReport), location 필수 필드 x·y·angle·planarDatum, 명령 메시지 부재를 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/interoperability-standards-and-conformance.md"
      ]
    },
    {
      "id": "ref-034",
      "org": "OPC Foundation / VDMA",
      "title": "OPC-40010-1 – OPC UA for Robotics - Part 1: Vertical Integration",
      "published": "2025-09-08",
      "url": "https://reference.opcfoundation.org/specs/OPC-40010-1",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "OPC UA for Robotics 1부 공식 온라인 참조(1.02판). §11.2.2 서버 Facet 네 가지(Base·MDS Operation·AM Extended·CM Extended)와 표 124~127 의 필수·선택 구분을 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/interoperability-standards-and-conformance.md"
      ]
    },
    {
      "id": "ref-138",
      "org": "국가표준인증통합정보시스템(KSSN)",
      "title": "KS B 7321-2 로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델",
      "published": null,
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010147546",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "KS B 7321-2 의 KSSN 상세 페이지. 2026-10-11 열람에서는 번호와 제목만 보였고 제정일·부합화·고시 정보는 확인하지 못했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/interoperability-standards-and-conformance.md"
      ]
    },
    {
      "id": "ref-1435",
      "org": "국가표준인증통합정보시스템(KSSN)",
      "title": "KS B ISO 22166-202 로봇 — 서비스 로봇의 모듈화 — 제202부: 소프트웨어 모듈용 정보 모델",
      "published": null,
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010158171",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "KS B ISO 22166-202 의 KSSN 상세 페이지. 번호와 제목만 보였고 제정일·부합화 수준·고시 정보는 확인하지 못했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/interoperability-standards-and-conformance.md"
      ]
    },
    {
      "id": "ref-608",
      "org": "OTTO by Rockwell Automation",
      "title": "OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments",
      "published": "2026-04-09",
      "url": "https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-11",
      "summary": "OTTO 100·600·1200·1500 이 Idealworks·NAiSE·SYNAOS 등과 VDA 5050 인증을 마쳤다는 2026-04-09 보도자료(벤더 주장). 시험 판·항목·기관은 밝히지 않는다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/interoperability-standards-and-conformance.md"
      ]
    },
    {
      "id": "ref-1436",
      "org": "VDMA",
      "title": "Mobile Robots in Production: Mesh-Up 2025",
      "published": null,
      "url": "https://www.vdma.eu/en/mesh-up",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "VDMA 의 automatica 2025(2025-06-24~27) 이동로봇 혼합 플릿 공동 시연 안내. 9개 기업 참여, MHP 상위 관제, 양식화한 생산 라인 공급 시연이며 관제 공급자 교체는 현장 실시간 시연이 아니라고 밝힌다. 전시 시연이며 실제 공장 배치가 아니다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/interoperability-standards-and-conformance.md"
      ]
    },
    {
      "id": "ref-1437",
      "org": "Wagner, N. A., Toenning, L., Lünsch, D., Jost, J., Wietfeld, C., Detzner, P.",
      "title": "Teleoperating Mobile Robots via VDA 5050 – A First Middleware Evaluation within Open Industrial Networks",
      "published": "2026-04",
      "url": "https://doi.org/10.1109/WFCS67029.2026.11511549",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "제22회 IEEE WFCS(2026) 논문. VDA 5050 원격 조작 확장(논문 제안)과 트래픽 생성기를 제안하고 Open RAN 무선 링크를 포함한 종단간 지연·오버헤드를 평가한다. TUHH 기관 저장소의 서지·초록만 확인했다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/interoperability-standards-and-conformance.md"
      ]
    },
    {
      "id": "ref-1438",
      "org": "TU Dortmund, Communication Networks Institute (ComNets)",
      "title": "Interoperable Teleoperation of Mobile Robots in Intralogistics: Joint Paper Demonstrates End-to-End Network Co-Design for Smart Industries",
      "published": "2026-04-24",
      "url": "https://comnets.etit.tu-dortmund.de/details/interoperable-teleoperation-of-mobile-robots-in-intralogistics-joint-paper-demonstrates-end-to-end-network-co-design-for-smart-industries-63558/",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-11",
      "summary": "저자 소속 연구실의 논문 소개. 가상 무선 시험대와 실제 무선 검증 구성을 썼다고 설명하고 트래픽 생성기 공개 저장소를 알린다. 정량 결과는 싣지 않는다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/interoperability-standards-and-conformance.md"
      ]
    },
    {
      "id": "ref-1439",
      "org": "buildingSMART International",
      "title": "Information Delivery Specification (IDS)",
      "published": null,
      "url": "https://www.buildingsmart.org/standards/bsi-standards/information-delivery-specifications-ids/",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "IDS 공식 소개 페이지. 2024-06-01 승인된 공식 표준이며 기계가 읽는 데이터 요구로 IFC 모델의 자동 적합성 검사를 가능하게 하고, 1.0 이전 판은 공식 표준이 아니라고 설명한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/interoperability-standards-and-conformance.md"
      ]
    },
    {
      "id": "ref-1362",
      "org": "buildingSMART International (buildingSMART/IDS GitHub)",
      "title": "IDS — Documentation/UserManual/README.md",
      "published": null,
      "url": "https://github.com/buildingSMART/IDS/blob/development/Documentation/UserManual/README.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "IDS 공식 저장소 사용자 설명서. 명세·적용 대상·요구 구조, 패싯 여섯 종류, IDS 와 IFC 를 함께 불러 불일치 보고를 얻는 검사 흐름을 설명한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/interoperability-standards-and-conformance.md"
      ]
    },
    {
      "id": "ref-1365",
      "org": "buildingSMART International (buildingSMART/IDS GitHub)",
      "title": "IDS — Documentation/UserManual/restrictions.md",
      "published": null,
      "url": "https://github.com/buildingSMART/IDS/blob/development/Documentation/UserManual/restrictions.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "IDS 사용자 설명서의 값 제한 절. 열거·패턴·범위·길이 네 가지 복합 제한을 설명한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/interoperability-standards-and-conformance.md"
      ]
    },
    {
      "id": "ref-1443",
      "org": "buildingSMART International (buildingSMART/IDS GitHub)",
      "title": "IDS — Documentation/README.md",
      "published": null,
      "url": "https://github.com/buildingSMART/IDS/blob/development/Documentation/README.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-11",
      "summary": "IDS 공식 저장소 문서 안내. 구현의 읽기·검사 기능 검증용 .ids·.ifc 시험 파일 쌍 250개 이상(TestCases)을 안내한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/interoperability-standards-and-conformance.md"
      ]
    },
    {
      "id": "ref-1442",
      "org": "idealworks",
      "title": "VDA 5050 3.0.0 release (March 2026)",
      "published": "2026-03",
      "url": "https://idealworks.com/en/news/vda5050-300-release-march-2026",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-11",
      "summary": "3.0.0 작업에 참여했다고 밝힌 업체의 출시 소식 글. VDMA·VDA 가 2월 17일 3.0.0 을 정식 채택했고 이어 법적 승인 절차가 있었다고 적는다(업체 서술, VDA 자료로 미확인).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/integration/interoperability-standards-and-conformance.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "update",
      "id": "oq-005",
      "question": "출처 충돌: VDA 5050 3.0.0의 정확한 발행일은 언제인가? 검색 요약은 3.0 발행을 2026-03-19, 보도자료를 2026-04-20로 전하지만 보도자료 URL은 2026-04-21 계열이다. 공식 저장소 명세 표지에는 날짜가 없고, VDA 카탈로그는 2026-03-17 을 표시하며, 3.0.0 작업에 참여했다고 밝힌 업체 Idealworks 의 2026년 3월 글은 2026-02-17 정식 채택을 적는다.",
      "areas": [
        20,
        21
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "VDA 5050 3.0.0 태그 스키마의 끝 쉼표를 고친 수정본을 연동 시험에 쓸 때 공식 PDF·태그와의 차이를 누가 승인하고 어떤 회귀 시험으로 확인하는가?",
      "areas": [
        21,
        57
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "VDA 5050 2.x·3.x 판이 섞인 플릿을 실제 현장에서 전환하면서 판별 스키마 차이와 시험 입력을 어떻게 검증했는지 공개한 기록이 있는가? (관련 기존 질문: oq-091)",
      "areas": [
        20,
        21
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "물류창고",
      "item": "수행 자원",
      "link": "docs/categories/integration/interoperability-standards-and-conformance.md#5-적용-사례-현장-유형-명시",
      "title": "21. 상호운용 표준·적합성"
    }
  ],
  "standards_updates": [
    {
      "name": "KS B ISO 22166-202 로봇 — 서비스 로봇의 모듈화 — 제202부: 소프트웨어 모듈용 정보 모델",
      "kind": "표준",
      "org": "국가표준인증통합정보시스템(KSSN)",
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010158171",
      "related_areas": [
        21,
        5
      ],
      "summary": "KSSN 국가표준 목록에 KS B 7321-2 와 별도로 실린 국가표준(2026-10-11 번호·제목 확인). 제정일·부합화 수준(IDT 여부)·고시 정보는 미확인이다.",
      "ref_id": "ref-1435"
    }
  ],
  "additional_research_requests": [
    "분리 주제 페이지 정정(이번 입력에 본문이 없어 미이행): 2026-09-25-area28-s6「적합성 시험과 인증」첫 문단의 '제조사가 자체 인증하거나', 2026-09-25-area28-s7 표 OPC 행의 '자체·독립 시험소 인증'과 본문 첫 문단의 '주문 배정·경로 계산…은 관제 쪽' 일반화를 f3·f5·f15~f18(ref-031·ref-032·ref-705·ref-1434) 근거로 고쳐야 한다. 다음 21. 상호운용 표준·적합성 갱신 실행에 두 페이지 본문을 입력으로 넣어 달라(하루 갱신 상한 2건 안에서).",
    "표준 목록(docs/standards/index.md)의 'OPC Foundation 인증 프로그램(적합성 시험 도구 CTT·독립 시험소 인증)' 항목 이름·요약을 '적합성 시험 도구 사전 점검(권고)·인정 시험소 인증'으로 고쳐야 한다. standards_updates 에 갱신 동작이 없어 퍼블리셔·표준 목록 담당 처리가 필요하다.",
    "참고문헌 id 정리: 대분류 페이지 자료 목록의 ref-1412(VDA, VDA 5050, 2026-03-17)와 이번 브리프의 ref-1412 이 같은 VDA 카탈로그 URL 로 보인다. docs_tree 에 ref-1412.md 가 있으므로 퍼블리셔가 URL 로 합칠 때 어느 id 를 남기는지 확인하고, ref-1430~ref-1443 이 다른 실행 id 와 겹치지 않는지도 확인해 달라.",
    "트랙 반영 제안 2026-10-09-26 나머지(7. 관련 표준·프레임워크·오픈소스 절): IDS 의 기수(필수·선택·금지), IFC 사용자 정의 속성 세트 명명 규칙, 뉴질랜드 OBOS 프록시 관례를 발행 기관 원문으로 확인해야 반영할 수 있다.",
    "8. 대표 연구와 자료: Wagner 외(WFCS 2026) 본문의 평가 시나리오(로봇 수·주문 시간·원격 조작 구간)와 정량 결과는 저자 공개본 PDF 텍스트를 읽지 못해 쓰지 못했다.",
    "7. 관련 표준·프레임워크·오픈소스·11. 열린 질문(oq-026): KS B 7321-2·KS B ISO 22166-202 의 제정일·부합화 수준·고시번호·대체 관계를 KSSN 세부 칸이나 국가기술표준원 고시로 확인해야 한다.",
    "7. 관련 표준·프레임워크·오픈소스(oq-005): VDA 가 배포하는 VDA 5050 3.0.0 PDF 표지의 날짜 표기를 원문 텍스트로 확인해야 한다.",
    "후속 정리(이번 대상 아님): P. 거버넌스·법규·사회 대분류 페이지(governance-law-and-society/index.md)의 '경로 계산' 일반화 문장을 f3·f5 근거로 고쳐야 한다.",
    "후속 정리(2차 검증 의견, 이번 지시 대상 아님): 10절 요약 문장의 '상호운용 표준·적합성는'을 '21. 상호운용 표준·적합성은'으로 고치고, 분리 페이지 s10 의 덧붙인 두 항목과 기존 목록 사이 빈 줄을 정리해야 한다."
  ],
  "fixes_applied": [
    "f39 — 7절「VDA 5050 3.0.0 의 판과 날짜」에서 '3.0.0 작업에 참여했다고 밝힌 업체 Idealworks'로 쓰고 [추정]과 업체 서술임을 밝혔으며, VDA 카탈로그(2026-03-17)·보도자료(2026-04-20) 날짜와 함께 제시하고 11절 oq-005 항목과 open_question_updates 의 oq-005 갱신에 출처 충돌로 덧붙였다.",
    "f2 — PDF 표지 'March 2026'은 새 각주나 [사실]로 쓰지 않았고, 날짜 비교는 20. 로봇·제조사 관제 연동 주제 페이지(2026-10-10-area20-s7)의 날짜 절로 링크만 했다.",
    "f19·f20 — 7절 MassRobotics 소절의 스키마 사실(location 필수 4필드, 명령 메시지 부재)에 각주 ref-230 을 달았고, 13절 ref-253 각주의 '(원문 미열람)'은 그대로 두었다.",
    "f13·f14 — 8절에서 vda5050-sim(ref-407)과 vda5050-lab(ref-408)을 두 항목으로 나눴다. vda5050-lab 은 ref-408 의 자기 기술만 [사실]로, 보조 도구 제안은 [의견]으로 쓰고 ref-408 각주의 '(원문 미열람)'을 지웠으며, vda5050-sim 은 [추정]과 ref-407 각주의 '(원문 미열람)'을 유지했다.",
    "f15~f18 — 대상 페이지에는 '제조사가 자체 인증하거나'·'자체·독립 시험소 인증' 문구가 없어 6절「적합성 시험과 인증을 구분해 읽기」와 7절 OPC 소절에 정정된 서술(사전 점검 권고·인정 시험소 인증)을 새로 썼고, 분리 주제 페이지는 입력에 없어 고치지 않고 추가 조사 요청에 적었다. reference_updates 로 ref-705 요약을 '적합성 시험 도구 사전 점검은 권고, 인증은 인정 시험소'로 고치고 접근일을 2026-10-11 로 바꿨으며 13절 각주의 '(원문 미열람)'을 지웠다.",
    "f30 — reference_updates 에서 ref-608 발행일을 2026-04-09 로 고치고 원문 열람으로 표시했으며, 13절 각주에도 2026-04-09 로 적고 '(원문 미열람)' 없이 정의했다. 6절 표의 본문은 [추정]과 '벤더 주장'을 유지했다.",
    "f24~f26 — 7절 국내 표준 소절에 KS B 7321-2·KS B ISO 22166-202 의 번호와 제목만 [사실][^ref-138][^ref-1435]로 쓰고 제정일·부합화(IDT)·고시번호·대체 관계는 미확인으로 두었으며, 11절과 출력에서 oq-026 은 열림을 유지했다.",
    "f31~f33 — 5절 제조 공장 사례의 사례 줄과 표 머리, 여섯 칸 모두에 'automatica 2025 전시 시연, 실제 공장 배치 아님'을 적었고 site_matrix_updates 에는 넣지 않았다.",
    "f34·f36·f37 — 8절에 Wagner 외를 VDA 5050 통신 지연·오버헤드 평가 연구로 소개하고 원격 조작 확장을 '논문 제안이며 표준이 채택한 기능이 아니다'로 밝혔으며, 로봇 수·시간 수치는 쓰지 않고 각주 ref-1437·ref-1438 을 달았다.",
    "f40~f44 — 7절 IDS 1.0 소절을 'IFC 데이터 교환 요구의 적합성 검사 수단'으로 짧게 두고 로봇–관제 메시지 적합성 시험과 구별했으며, 트랙 반영 제안 2026-10-09-26 의 기수·사용자 정의 속성 세트 명명 규칙·OBOS 프록시 관례는 반영하지 않고 페이지·changelog·area_recent 에 '일부 반영'으로 기록했다.",
    "10절 — 42. 분산 시스템·통신·컴퓨팅 구조(f37)와 14. 도면·BIM에서 지도 만들기(f44) 연결을 지시한 상대 경로로 덧붙이고, 프런트매터 related_areas 에 14·42 를 더했다.",
    "f9·f12 — 7절 태그 스키마 소절에서 3.0.0 태그의 끝 쉼표는 ref-1430~ref-1432, main 의 상태는 ref-413 으로 각주를 달았고 행·열 번호와 파서별 오류 메시지는 쓰지 않았다.",
    "f5 — 대상 페이지 5절 물류창고 사례의 수행 자원 칸만 '선 유도 로봇의 경로 계산·안내'로 고치고 자유 주행 로봇의 경로 자체 계획·공유를 병기했다. governance-law-and-society/index.md 는 고치지 않았고, 분리 7절 본문(2026-09-25-area28-s7)은 입력에 없어 추가 조사 요청으로 넘겼다.",
    "2차: 6절 — 첫 단락(자동 분리 뒤 원 절에 남는 [의견] 요약 단락)의 둘째 문장으로 [21. 상호운용 표준·적합성 — 대표 접근법과 기술 (2026-09-25)](../../topics/2026/2026-09-25-area28-s6.md) 링크와 '그 페이지의 정정은 다음 갱신 실행으로 넘겼다'는 문장을 되살렸다.",
    "2차: 7절 — 첫 단락의 둘째 문장으로 [21. 상호운용 표준·적합성 — 관련 표준·프레임워크·오픈소스 (2026-09-25)](../../topics/2026/2026-09-25-area28-s7.md) 링크(표준 비교표가 있음을 명시)와 '그 페이지의 정정은 다음 갱신 실행으로 넘겼다'는 문장을 되살리고, 표준·프레임워크 목록 링크도 같은 문장에 유지했다.",
    "2차: 11절 — 첫 단락의 둘째 문장으로 [21. 상호운용 표준·적합성 — 열린 질문 (2026-09-25)](../../topics/2026/2026-09-25-area28-s11.md) 링크를 되살리고 전체 열린 질문 목록 링크를 같은 문장에 두었다.",
    "2차: 7절「VDA 5050 3.0.0 의 판과 날짜」 — '표의 VDA 5050 행 발행일은'을 '[2026-09-25 표준 표](../../topics/2026/2026-09-25-area28-s7.md)의 VDA 5050 행 발행일은'으로 고쳐 가리키는 표를 밝혔다.",
    "2차: 7절「IDS 1.0」 둘째 단락 — 줄 첫머리 '21. 상호운용 표준·적합성에서는'을 '이 영역(21. 상호운용 표준·적합성)에서는'으로 고쳐 번호 목록으로 렌더링되지 않게 하고 번호와 이름은 함께 유지했다.",
    "2차: 프런트매터 sources(5절 patch 의 frontmatter) — 기존 페이지에 있던 ref-636·ref-637·ref-708·ref-710 을 되살렸고, diff_summary 에도 기존 sources 유지를 적었다.",
    "분량 초과 자동 분리: 21. 상호운용 표준·적합성 본문 11,555자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 4,346자"
  ]
}
```

### runs/2026-10-11-01/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/integration/interoperability-standards-and-conformance.md (7개 절)
- 분량 초과 자동 분리:
    - docs/categories/integration/interoperability-standards-and-conformance.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-10-11-area21-s7.md (2,916자)
    - docs/categories/integration/interoperability-standards-and-conformance.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-10-11-area21-s6.md (2,060자)
    - docs/categories/integration/interoperability-standards-and-conformance.md "8. 대표 연구와 자료" → docs/topics/2026/2026-10-11-area21-s8.md (1,461자)
    - docs/categories/integration/interoperability-standards-and-conformance.md "11. 열린 질문" → docs/topics/2026/2026-10-11-area21-s11.md (1,079자)
    - docs/categories/integration/interoperability-standards-and-conformance.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-10-11-area21-s10.md (630자)
```

### runs/2026-10-11-01/pages/categories/integration/interoperability-standards-and-conformance.md

```markdown
---
title: "21. 상호운용 표준·적합성"
type: area
category: "F. 연동"
area_no: 21
related_areas: [14, 20, 22, 42, 48, 51, 54, 57]
tags: [VDA 5050, 의미적 버전 관리, 적합성 시험, 감사 추적, 데이터 권리]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-10-11
sources: [ref-004, ref-031, ref-032, ref-034, ref-051, ref-138, ref-230, ref-253, ref-407, ref-408, ref-560, ref-608, ref-634, ref-635, ref-636, ref-637, ref-638, ref-639, ref-704, ref-705, ref-706, ref-707, ref-708, ref-709, ref-710, ref-1412, ref-1430, ref-1431, ref-1432, ref-413, ref-1434, ref-1435, ref-1436, ref-1437, ref-1438, ref-1439, ref-1362, ref-1365, ref-1442, ref-1443]
last_run: 2026-10-11
version: 3
---

[홈](../../index.md) › [F. 연동](index.md) › 21. 상호운용 표준·적합성

# 21. 상호운용 표준·적합성

!!! info "소속 대분류"
    [F. 연동](index.md) — 핵심 질문:
    제조사 관제·로봇·문·승강기·업무 시스템과 어떻게 확실하게 연결할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
<!-- auto:page-status:end -->

## 1. 한 줄 정의

로봇 상호운용 표준을 채택·변환하고 적합성을 시험한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **상호운용 표준 채택**: VDA 5050·MassRobotics 상호운용 표준·Open-RMF·ROS 2·OPC UA 같은 표준을 채택하고 서로 변환한다
- **적합성 시험**: 표준과 연동 규격을 지키는지 시험한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [58. 다사업자 책임·계약·데이터](../governance-law-and-society/multi-party-responsibility-contracts-and-data.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 28번 영역 ‘표준·상호운용성·다사업자 거버넌스’(옛 대분류 G. 안전·보안·지능·거버넌스)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 공통 규격, 적합성 시험, 제조사 간 책임, 데이터 소유권, API 변경 정책, 서비스 수준과 감사 이력 [옛 분류원문]

> 옛 질문: 제조사·ROP·설비업체 중 누가 연동 오류를 수정하고 변경을 승인할까? [옛 분류원문]

## 2. 핵심 질문

어떤 상호운용 표준을 따르고, 제조사가 그 표준을 지키는지 어떻게 확인할 것인가? [분류원문]

## 3. 왜 중요한가

로봇–관제 공통 규격은 메시지 형식을 맞춰 주지만 누가 연동 오류를 고치고 변경을 승인할지는 정해 주지 않으므로, 여러 사업자가 함께 운영하는 현장에서는 이 책임을 따로 설계해야 한다. [의견]

자세한 내용은 주제 페이지 [21. 상호운용 표준·적합성 — 왜 중요한가](../../topics/2026/2026-09-25-area28-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 영역은 규격의 판을 어떻게 올리고 알리는지, 그리고 여러 사업자의 행위를 어떻게 기록하고 약속하는지에 관한 용어로 이루어진다. [의견]

자세한 내용은 주제 페이지 [21. 상호운용 표준·적합성 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area28-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다.

**물류 흐름 단계:** 입고 → 출하

**시나리오:** 새 제조사 로봇 등록(입고)과 펌웨어 갱신 뒤 출하 마감 작업 유지(출하)

| 항목 | 내용 |
|---|---|
| 시작 조건 | (입고) 입고 물량에 대응하려고 새 제조사 로봇을 현장 관제에 등록한다(설명용 가상 설정). (출하) 출하 마감 전에 한 제조사가 로봇 펌웨어를 올려 VDA 5050 프로토콜 판이 바뀐다(설명용 가상 설정). [추정][^ref-031][^ref-051] |
| 작업 대상 | 해당 없음 |
| 수행 자원 | (출하) VDA 5050 3.0.0 은 관제 쪽 기능으로 주문 배정, 선 유도(line-guided) 이동로봇의 경로 계산·안내, 교착 탐지와 해소, 교통 제어를 들고, 이동로봇 쪽 기능으로 위치 추정, 선 유도형과 자유 주행형(freely navigating)으로 나눈 경로 실행, 동작 실행, 상태의 지속 전송을 든다. [사실][^ref-031] VDA 의 3.0 발표 보도자료(2026-04-20)는 자율도가 높은 이동로봇이 지정된 경유점 사이 경로를 스스로 계획해 상세 경로 계획이 로봇에서 이뤄지고, 그 경로를 경로 공유(path sharing)로 중앙 관제와 공유하는 구성을 설명한다. [사실][^ref-032] 그래서 모든 이동로봇의 상세 경로를 관제가 계산한다고 일반화하지 않고, 선 유도 로봇의 경로 계산·안내만 관제 쪽으로 적는 것이 맞다. [의견][^ref-031][^ref-032] (입고) MassRobotics 신원 보고의 제조사명·모델·일련번호나 VDA 5050 헤더의 manufacturer·serialNumber 를 감사 기록의 주체 식별자로 쓰면 이후 연동 오류와 변경 이력을 제조사별로 귀속할 수 있을 것으로 보인다. [추정][^ref-253][^ref-051] |
| 제약 | (출하) 변경 승인 전에 판 호환 시험과 수정 책임을 계약으로 정해 두어야 할 것으로 보인다. [추정][^ref-031][^ref-051] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | (출하) 관제가 헤더 version 으로 판 차이를 감지하고, 로봇이 지원하지 않는 선택 필드는 UNSUPPORTED_PARAMETER 오류로 드러나므로, 사전 시험이 없으면 출하 마감 전 작업 실패로 이어질 수 있을 것으로 보인다. [추정][^ref-031][^ref-051] |

다음은 설명을 위한 가상의 시나리오이다. 입고 물량이 늘어 새 제조사 로봇을 들이는 날, 등록 단계에서 어떤 식별자로 제조사를 구분할지 정해 두면 뒤에 생기는 연동 오류를 누구의 것인지 가릴 수 있다. [추정][^ref-253][^ref-051]

며칠 뒤 한 제조사가 펌웨어를 올려 프로토콜 판이 바뀌면, 출하 마감 직전에 관제가 보낸 주문의 일부 필드가 거부될 수 있다. 이때 규격 불일치를 누가 고치고 판 변경을 누가 승인하는지가 미리 정해져 있어야 복구가 빨라지지만, 이를 정한 공식 기준은 확인되지 않았다. [추정][^ref-031][^ref-004][^ref-560][^ref-634]

예정 경로 공유의 세부는 [27. 다중 로봇 경로·교통 관리 — MAPF 의 관련 표준 정리](../../topics/2026/2026-10-10-area27-s7.md)에 있다.

**현장 유형:** 제조 공장

**사례:** 여러 이동로봇이 작업대를 공급하는 양식화한 생산 라인 시연 — VDMA Mesh-Up 2025 (automatica 2025 전시 시연, 실제 공장 배치 아님)

| 항목 | 내용 (automatica 2025 전시 시연, 실제 공장 배치 아님) |
|---|---|
| 시작 조건 | 미확인 (automatica 2025 전시 시연, 실제 공장 배치 아님) |
| 작업 대상 | 양식화한 생산 라인의 작업대 공급 (automatica 2025 전시 시연, 실제 공장 배치 아님). [사실][^ref-1436] |
| 수행 자원 | 9개 기업이 참여하고 MHP 가 상위 관제를 맡아 여러 이동로봇을 함께 운용한 혼합 플릿 구성 (automatica 2025 전시 시연, 실제 공장 배치 아님). [사실][^ref-1436] |
| 제약 | 미확인 (automatica 2025 전시 시연, 실제 공장 배치 아님) |
| 완료·인계 | 미확인 (automatica 2025 전시 시연, 실제 공장 배치 아님) |
| 예외·성과 | 관제 소프트웨어 공급자를 바꿔 고를 수 있다는 점은 전시장에서 실시간으로 시연하지 않는다고 안내가 밝힌다. 처리량·시간·비용에 대한 영향은 미확인이다 (automatica 2025 전시 시연, 실제 공장 배치 아님). [사실][^ref-1436] |

VDMA 의 Mesh-Up 2025 안내는 automatica 2025(뮌헨, 2025-06-24~27) 전시장에서 9개 기업이 참여하고 MHP 가 상위 관제를 맡아, 여러 이동로봇이 작업대를 공급하는 양식화한 생산 라인을 보여 주는 혼합 플릿 시연을 설명한다. [사실][^ref-1436] 이 시연은 실제 공장 배치가 아니므로 혼합 플릿 구성의 예로만 쓰고, 실제 도입 사례나 현장 관제 교체가 검증된 근거로 세지 않는 것이 맞다. [의견][^ref-1436] 같은 이유로 현장 유형 매트릭스에도 도입 사례로 넣지 않는다.

## 6. 대표 접근법과 기술

여러 사업자를 한 현장에서 묶는 대표 접근은 판 번호 규칙으로 변경을 알리고, 적합성 시험으로 구현을 확인하고, 연동 수준을 나눠 통합하며, 서비스 수준과 감사 이력을 함께 기록하는 것이다. [의견] 2026-09-25 에 쓴 이전 내용은 [21. 상호운용 표준·적합성 — 대표 접근법과 기술 (2026-09-25)](../../topics/2026/2026-09-25-area28-s6.md)에 있으며, 그 페이지의 정정은 다음 갱신 실행으로 넘겼다.

자세한 내용은 주제 페이지 [21. 상호운용 표준·적합성 — 대표 접근법과 기술](../../topics/2026/2026-10-11-area21-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역의 표준은 로봇–관제 규격, 변경 알림 규칙, 적합성 시험, 감사·서비스 관리, 국내 표준으로 나뉜다. [의견] 2026-09-25 에 쓴 표준 비교표와 이전 내용은 [21. 상호운용 표준·적합성 — 관련 표준·프레임워크·오픈소스 (2026-09-25)](../../topics/2026/2026-09-25-area28-s7.md)에 있고 그 페이지의 정정은 다음 갱신 실행으로 넘겼으며, 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [21. 상호운용 표준·적합성 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-11-area21-s7.md)에 있다.

## 8. 대표 연구와 자료

이 영역의 자료는 학술 논문보다 규격 저장소와 공공기관 자료가 중심이다. [의견]

자세한 내용은 주제 페이지 [21. 상호운용 표준·적합성 — 대표 연구와 자료](../../topics/2026/2026-10-11-area21-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 인터페이스 판·적합성·책임 경계를 정하고 확인한다. [추정][^ref-031] | 연계 대상: 로봇의 위치 추정·주행 실행, 기능·시스템 안전(제조사 쪽). [추정][^ref-031] |
| 시설·설비 제어 | 승강기 연동 표준의 요구를 작업·경로 제약으로 반영한다. [의견] | 연계 대상: 승강기 안전기준·제어. [추정][^ref-709] |
| 상위 업무 시스템 | 상위 시스템에 여는 API 의 판 번호·폐기 예고 정책. [추정][^ref-635][^ref-706] | 연계 대상: 데이터 권리의 법률 해석과 계약 조건. [의견] |

VDA 5050 3.0.0 에서 교착 탐지·해소는 관제 쪽 기능이다. [사실][^ref-031] 그러나 교통 조율 알고리즘 자체와 기능·운영·시스템 안전 요구는 명세 범위 밖이다. [사실][^ref-031] 그래서 21. 상호운용 표준·적합성에서 ROP 몫은 인터페이스 판·적합성·책임 경계를 정하고 확인하는 쪽으로 보인다. [추정][^ref-031]

분류 원문 질문과 관련해, 확인한 규격을 종합하면 연동 오류 수정 책임은 규격 불일치는 해당 메시지를 구현한 쪽(로봇 제조사 또는 관제), 플릿 어댑터·매핑 오류는 ROP, 시스템 수준 위험과 변경 승인은 통합자 역할을 맡는 쪽으로 나누는 구조가 될 수 있어 보이나, 이를 정한 공식 기준은 확인되지 않았다. [추정][^ref-031][^ref-004][^ref-560][^ref-634] ISO 10218-2:2025 는 로봇 자체를 다루는 Part 1 과 구분해 산업용 로봇 적용과 로봇 셀의 안전 요구를 다루며, 통합자가 합리적으로 예견할 수 있는 위험원과 위험 상황을 대상으로 한다. [사실][^ref-560] 물류 이동로봇 플릿에 적용되는지는 미확인이다. 이 경계는 제품 전략에 따라 이동할 수 있다([범위 경계](../../about/scope-boundary.md)).

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

상호운용 표준·적합성는 규격 판·책임 분리, 적합성 시험, 판 이행, 감사 추적, 통합자 위험성평가, 승강기 연동 표준을 통해 다른 영역과 맞물리는 것으로 보인다. [추정][^ref-031][^ref-004][^ref-705][^ref-707][^ref-560][^ref-709]

자세한 내용은 주제 페이지 [21. 상호운용 표준·적합성 — 다른 연구영역과의 연결](../../topics/2026/2026-10-11-area21-s10.md)에 있다.

## 11. 열린 질문

규격의 판·발행일, 공식 적합성 시험 유무, 운영 주체 간 책임은 아직 확인되지 않은 부분이 많다. [의견] 2026-09-25 에 정리한 이전 질문 목록은 [21. 상호운용 표준·적합성 — 열린 질문 (2026-09-25)](../../topics/2026/2026-09-25-area28-s11.md)에, 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [21. 상호운용 표준·적합성 — 열린 질문](../../topics/2026/2026-10-11-area21-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [21. 상호운용 표준·적합성](interoperability-standards-and-conformance.md) — seed → draft: 3~11절 첫 작성, 페이지 상태 자동 영역 추가, 13절 각주. 2차: 9절 승강기 연계 칸 [추정]으로 정정, ISO 10218-2 적용 범위 미확인 단서 추가, 5절 시작 조건 칸에 가상 설정 표시와 [추정] 태그 추가 (실행 2026-09-25-69)
- 2026-09-25 · 생성 · [21. 상호운용 표준·적합성 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area28-s7.md) — 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,840자)을 옮겼다 (실행 2026-09-25-69)
- 2026-09-25 · 생성 · [21. 상호운용 표준·적합성 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area28-s6.md) — 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "6. 대표 접근법과 기술" 절(1,549자)을 옮겼다 (실행 2026-09-25-69)
- 2026-09-25 · 생성 · [21. 상호운용 표준·적합성 — 열린 질문](../../topics/2026/2026-09-25-area28-s11.md) — 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "11. 열린 질문" 절(1,233자)을 옮겼다 (실행 2026-09-25-69)
- 2026-09-25 · 생성 · [21. 상호운용 표준·적합성 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area28-s4.md) — 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "4. 핵심 개념과 용어" 절(1,053자)을 옮겼다 (실행 2026-09-25-69)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-11
[^ref-032]: VDA(Verband der Automobilindustrie), Version 3.0 of VDA 5050 released, 2026-04-20, https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN, 접근일 2026-10-11
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-253]: MassRobotics, AMR_Interop_Standard — MassRobotics AMR Interoperability Standard (README, JSON schema), 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard, 접근일 2026-09-25 (원문 미열람)
[^ref-560]: ISO, ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells, 2025-02, https://www.iso.org/standard/73934.html, 접근일 2026-09-25 (원문 미열람)
[^ref-634]: VDA / VDMA / KIT IFL (VDA5050 GitHub), VDA5050/VDA5050 — README, 미확인, https://github.com/VDA5050/VDA5050, 접근일 2026-09-25
[^ref-635]: Semantic Versioning (Tom Preston-Werner, semver.org), Semantic Versioning 2.0.0, 미확인, https://semver.org/spec/v2.0.0.html, 접근일 2026-09-25
[^ref-705]: OPC Foundation, How to Certify - OPC Foundation, 미확인, https://opcfoundation.org/certification/how-to-certify/, 접근일 2026-10-11
[^ref-706]: IETF (RFC Editor), RFC 9745: The Deprecation HTTP Response Header Field, 미확인, https://www.rfc-editor.org/info/rfc9745/, 접근일 2026-09-25 (원문 미열람)
[^ref-707]: IEC, IEC 62443-3-3:2013 Industrial communication networks — Network and system security — Part 3-3: System security requirements and security levels (sample), 2013-08, https://cdn.standards.iteh.ai/samples/19488/7c0b753be32e46fc986c23c32efbdbe8/IEC-62443-3-3-2013.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-709]: 대한민국 정책브리핑(산업통상자원부 국가기술표준원), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11-11, https://korea.kr/news/pressReleaseView.do?newsId=156480155, 접근일 2026-09-25 (원문 미열람)
[^ref-1436]: VDMA, Mobile Robots in Production: Mesh-Up 2025, 미확인, https://www.vdma.eu/en/mesh-up, 접근일 2026-10-11
```

### docs/categories/integration/interoperability-standards-and-conformance.md

```markdown
---
title: "21. 상호운용 표준·적합성"
type: area
category: "F. 연동"
area_no: 21
related_areas: [20, 22, 48, 51, 54, 57]
tags: [VDA 5050, 의미적 버전 관리, 적합성 시험, 감사 추적, 데이터 권리]
status: published
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-004, ref-031, ref-051, ref-407, ref-408, ref-608, ref-634, ref-253, ref-635, ref-636, ref-637, ref-638, ref-639, ref-704, ref-705, ref-706, ref-560, ref-707, ref-708, ref-709, ref-710]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [F. 연동](index.md) › 21. 상호운용 표준·적합성

# 21. 상호운용 표준·적합성

!!! info "소속 대분류"
    [F. 연동](index.md) — 핵심 질문:
    제조사 관제·로봇·문·승강기·업무 시스템과 어떻게 확실하게 연결할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
<!-- auto:page-status:end -->

## 1. 한 줄 정의

로봇 상호운용 표준을 채택·변환하고 적합성을 시험한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **상호운용 표준 채택**: VDA 5050·MassRobotics 상호운용 표준·Open-RMF·ROS 2·OPC UA 같은 표준을 채택하고 서로 변환한다
- **적합성 시험**: 표준과 연동 규격을 지키는지 시험한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [58. 다사업자 책임·계약·데이터](../governance-law-and-society/multi-party-responsibility-contracts-and-data.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 28번 영역 ‘표준·상호운용성·다사업자 거버넌스’(옛 대분류 G. 안전·보안·지능·거버넌스)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 공통 규격, 적합성 시험, 제조사 간 책임, 데이터 소유권, API 변경 정책, 서비스 수준과 감사 이력 [옛 분류원문]

> 옛 질문: 제조사·ROP·설비업체 중 누가 연동 오류를 수정하고 변경을 승인할까? [옛 분류원문]

## 2. 핵심 질문

어떤 상호운용 표준을 따르고, 제조사가 그 표준을 지키는지 어떻게 확인할 것인가? [분류원문]

## 3. 왜 중요한가

로봇–관제 공통 규격은 메시지 형식을 맞춰 주지만 누가 연동 오류를 고치고 변경을 승인할지는 정해 주지 않으므로, 여러 사업자가 함께 운영하는 현장에서는 이 책임을 따로 설계해야 한다. [의견]

자세한 내용은 주제 페이지 [21. 상호운용 표준·적합성 — 왜 중요한가](../../topics/2026/2026-09-25-area28-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 영역은 규격의 판을 어떻게 올리고 알리는지, 그리고 여러 사업자의 행위를 어떻게 기록하고 약속하는지에 관한 용어로 이루어진다. [의견]

자세한 내용은 주제 페이지 [21. 상호운용 표준·적합성 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area28-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다.

**물류 흐름 단계:** 입고 → 출하

**시나리오:** 새 제조사 로봇 등록(입고)과 펌웨어 갱신 뒤 출하 마감 작업 유지(출하)

| 항목 | 내용 |
|---|---|
| 시작 조건 | (입고) 입고 물량에 대응하려고 새 제조사 로봇을 현장 관제에 등록한다(설명용 가상 설정). (출하) 출하 마감 전에 한 제조사가 로봇 펌웨어를 올려 VDA 5050 프로토콜 판이 바뀐다(설명용 가상 설정). [추정][^ref-031][^ref-051] |
| 작업 대상 | 해당 없음 |
| 수행 자원 | (출하) VDA 5050 3.0.0 에서 주문 배정·경로 계산·교착 탐지와 해소·교통 제어는 관제 쪽, 위치 추정·경로와 동작 실행·상태의 지속 전송은 이동로봇 쪽 책임이다. [사실][^ref-031] (입고) MassRobotics 신원 보고의 제조사명·모델·일련번호나 VDA 5050 헤더의 manufacturer·serialNumber 를 감사 기록의 주체 식별자로 쓰면 이후 연동 오류와 변경 이력을 제조사별로 귀속할 수 있을 것으로 보인다. [추정][^ref-253][^ref-051] |
| 제약 | (출하) 변경 승인 전에 판 호환 시험과 수정 책임을 계약으로 정해 두어야 할 것으로 보인다. [추정][^ref-031][^ref-051] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | (출하) 관제가 헤더 version 으로 판 차이를 감지하고, 로봇이 지원하지 않는 선택 필드는 UNSUPPORTED_PARAMETER 오류로 드러나므로, 사전 시험이 없으면 출하 마감 전 작업 실패로 이어질 수 있을 것으로 보인다. [추정][^ref-031][^ref-051] |

다음은 설명을 위한 가상의 시나리오이다. 입고 물량이 늘어 새 제조사 로봇을 들이는 날, 등록 단계에서 어떤 식별자로 제조사를 구분할지 정해 두면 뒤에 생기는 연동 오류를 누구의 것인지 가릴 수 있다. [추정][^ref-253][^ref-051]

며칠 뒤 한 제조사가 펌웨어를 올려 프로토콜 판이 바뀌면, 출하 마감 직전에 관제가 보낸 주문의 일부 필드가 거부될 수 있다. 이때 규격 불일치를 누가 고치고 판 변경을 누가 승인하는지가 미리 정해져 있어야 복구가 빨라지지만, 이를 정한 공식 기준은 확인되지 않았다. [추정][^ref-031][^ref-004][^ref-560][^ref-634]

## 6. 대표 접근법과 기술

여러 사업자를 한 현장에서 묶는 대표 접근은 판 번호 규칙으로 변경을 알리고, 적합성 시험으로 구현을 확인하고, 연동 수준을 나눠 통합하며, 서비스 수준과 감사 이력을 함께 기록하는 것이다. [의견]

자세한 내용은 주제 페이지 [21. 상호운용 표준·적합성 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area28-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역의 표준은 로봇–관제 규격, 변경 알림 규칙, 적합성 시험, 감사·서비스 관리, 국내 표준으로 나뉜다. [의견] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [21. 상호운용 표준·적합성 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area28-s7.md)에 있다.

## 8. 대표 연구와 자료

이 영역의 자료는 학술 논문보다 규격 저장소와 공공기관 자료가 중심이다. [의견]

- VDA / VDMA / KIT IFL, VDA 5050 공식 저장소 README(발행일 미확인) — 변경 제안 절차, 계획 판, 지원 의무 부인 문구를 담아 규격 거버넌스를 읽는 기본 자료다. [사실][^ref-634]
- MassRobotics, AMR_Interop_Standard 저장소(발행일 미확인) — 신원·상태 보고 스키마만 두는 보고 중심 규격이다. [사실][^ref-253]
- gpue, vda5050-sim / ekusiadadus, vda5050-lab(발행일 미확인) — VDA 5050 시뮬레이션·적합성 시험 묶음과 MQTT 기록 진단 도구로, 개인 프로젝트이며 VDA·VDMA 공식 시험이 아닌 것으로 보인다. [추정][^ref-407][^ref-408]
- OSRA, Open-RMF 프로젝트 헌장(2024-03)과 정책·절차 저장소 — 오픈소스 관제 프레임워크의 운영·개정 권한 구조를 보여 준다. [추정][^ref-704][^ref-639]
- 소프트웨어정책연구소(SPRi), 산업 디지털 전환 촉진법의 의미와 시사점(발행일 미확인) — 산업데이터 권리 규정을 해설한 국내 자료다. [사실][^ref-638]
- 국가기술표준원, 로봇 엘리베이터 탑승 KS 제정 보도자료(2021-11-11) — 속도 제어, 위험 상황 보호 정지, 높낮이차·틈새 극복, 추락·넘어짐 방지 기준을 다룬다. KS 번호는 미확인이다. [사실][^ref-709]

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 인터페이스 판·적합성·책임 경계를 정하고 확인한다. [추정][^ref-031] | 연계 대상: 로봇의 위치 추정·주행 실행, 기능·시스템 안전(제조사 쪽). [추정][^ref-031] |
| 시설·설비 제어 | 승강기 연동 표준의 요구를 작업·경로 제약으로 반영한다. [의견] | 연계 대상: 승강기 안전기준·제어. [추정][^ref-709] |
| 상위 업무 시스템 | 상위 시스템에 여는 API 의 판 번호·폐기 예고 정책. [추정][^ref-635][^ref-706] | 연계 대상: 데이터 권리의 법률 해석과 계약 조건. [의견] |

VDA 5050 3.0.0 에서 교착 탐지·해소는 관제 쪽 기능이다. [사실][^ref-031] 그러나 교통 조율 알고리즘 자체와 기능·운영·시스템 안전 요구는 명세 범위 밖이다. [사실][^ref-031] 그래서 21. 상호운용 표준·적합성에서 ROP 몫은 인터페이스 판·적합성·책임 경계를 정하고 확인하는 쪽으로 보인다. [추정][^ref-031]

분류 원문 질문과 관련해, 확인한 규격을 종합하면 연동 오류 수정 책임은 규격 불일치는 해당 메시지를 구현한 쪽(로봇 제조사 또는 관제), 플릿 어댑터·매핑 오류는 ROP, 시스템 수준 위험과 변경 승인은 통합자 역할을 맡는 쪽으로 나누는 구조가 될 수 있어 보이나, 이를 정한 공식 기준은 확인되지 않았다. [추정][^ref-031][^ref-004][^ref-560][^ref-634] ISO 10218-2:2025 는 로봇 자체를 다루는 Part 1 과 구분해 산업용 로봇 적용과 로봇 셀의 안전 요구를 다루며, 통합자가 합리적으로 예견할 수 있는 위험원과 위험 상황을 대상으로 한다. [사실][^ref-560] 물류 이동로봇 플릿에 적용되는지는 미확인이다. 이 경계는 제품 전략에 따라 이동할 수 있다([범위 경계](../../about/scope-boundary.md)).

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

21. 상호운용 표준·적합성는 규격 판·책임 분리, 적합성 시험, 판 이행, 감사 추적, 통합자 위험성평가, 승강기 연동 표준을 통해 다른 영역과 맞물리는 것으로 보인다. [추정][^ref-031][^ref-004][^ref-705][^ref-707][^ref-560][^ref-709]

- [20. 로봇·제조사 관제 연동](robot-and-vendor-fleet-manager-integration.md) — 규격 판과 관제–로봇 책임 분리가 연동 구현의 전제다.
- [22. 설비·건물 시스템 연동](facility-and-building-system-integration.md) — 로봇 승강기 탑승 KS 같은 설비 연동 표준을 공유한다.
- [54. 시험·형식 검증·벤치마크](../verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md) — 적합성 시험·인증을 새 로봇 연동 승인에 쓰는 방법을 다룬다.
- [57. 자산·소프트웨어 수명주기 관리](../verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) — 펌웨어·프로토콜 판 이행과 폐기 예고가 수명주기 관리와 겹친다.
- [48. 안전·위험 관리](../safety/safety-and-risk-management.md) — 통합자의 시스템 수준 위험성평가를 누가 맡는지가 책임 경계의 핵심이다.
- [51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md) — 감사 추적 요구가 보안 표준에서 온다.

## 11. 열린 질문

규격의 판·발행일, 공식 적합성 시험 유무, 운영 주체 간 책임은 아직 확인되지 않은 부분이 많다. [의견] 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [21. 상호운용 표준·적합성 — 열린 질문](../../topics/2026/2026-09-25-area28-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [21. 상호운용 표준·적합성](interoperability-standards-and-conformance.md) — seed → draft: 3~11절 첫 작성, 페이지 상태 자동 영역 추가, 13절 각주. 2차: 9절 승강기 연계 칸 [추정]으로 정정, ISO 10218-2 적용 범위 미확인 단서 추가, 5절 시작 조건 칸에 가상 설정 표시와 [추정] 태그 추가 (실행 2026-09-25-69)
- 2026-09-25 · 생성 · [21. 상호운용 표준·적합성 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area28-s7.md) — 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,840자)을 옮겼다 (실행 2026-09-25-69)
- 2026-09-25 · 생성 · [21. 상호운용 표준·적합성 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area28-s6.md) — 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "6. 대표 접근법과 기술" 절(1,549자)을 옮겼다 (실행 2026-09-25-69)
- 2026-09-25 · 생성 · [21. 상호운용 표준·적합성 — 열린 질문](../../topics/2026/2026-09-25-area28-s11.md) — 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "11. 열린 질문" 절(1,233자)을 옮겼다 (실행 2026-09-25-69)
- 2026-09-25 · 생성 · [21. 상호운용 표준·적합성 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area28-s4.md) — 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "4. 핵심 개념과 용어" 절(1,053자)을 옮겼다 (실행 2026-09-25-69)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-407]: gpue (GitHub), vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS), 미확인, https://github.com/gpue/vda5050-sim, 접근일 2026-09-25 (원문 미열람)
[^ref-408]: ekusiadadus (GitHub), vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces), 미확인, https://github.com/ekusiadadus/vda5050-lab, 접근일 2026-09-25 (원문 미열람)
[^ref-634]: VDA / VDMA / KIT IFL (VDA5050 GitHub), VDA5050/VDA5050 — README, 미확인, https://github.com/VDA5050/VDA5050, 접근일 2026-09-25
[^ref-253]: MassRobotics, AMR_Interop_Standard — MassRobotics AMR Interoperability Standard (README, JSON schema), 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard, 접근일 2026-09-25 (원문 미열람)
[^ref-635]: Semantic Versioning (Tom Preston-Werner, semver.org), Semantic Versioning 2.0.0, 미확인, https://semver.org/spec/v2.0.0.html, 접근일 2026-09-25
[^ref-638]: 소프트웨어정책연구소(SPRi), 산업 디지털 전환 촉진법의 의미와 시사점, 미확인, https://spri.kr/posts/view/23480?code=industry_trend, 접근일 2026-09-25 (원문 미열람)
[^ref-639]: Open Source Robotics Alliance (Open Robotics), osra-policies-and-procedures — README, 미확인, https://github.com/openrobotics/osra-policies-and-procedures, 접근일 2026-09-25
[^ref-704]: Open Source Robotics Alliance, Charter of the Open Source Robotics Alliance Project 'Open-RMF', 2024-03, https://osralliance.org/wp-content/uploads/2024/03/open-rmf-project-charter.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-705]: OPC Foundation, How to Certify - OPC Foundation, 미확인, https://opcfoundation.org/certification/how-to-certify/, 접근일 2026-09-25 (원문 미열람)
[^ref-706]: IETF (RFC Editor), RFC 9745: The Deprecation HTTP Response Header Field, 미확인, https://www.rfc-editor.org/info/rfc9745/, 접근일 2026-09-25 (원문 미열람)
[^ref-560]: ISO, ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells, 2025-02, https://www.iso.org/standard/73934.html, 접근일 2026-09-25 (원문 미열람)
[^ref-707]: IEC, IEC 62443-3-3:2013 Industrial communication networks — Network and system security — Part 3-3: System security requirements and security levels (sample), 2013-08, https://cdn.standards.iteh.ai/samples/19488/7c0b753be32e46fc986c23c32efbdbe8/IEC-62443-3-3-2013.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-709]: 대한민국 정책브리핑(산업통상자원부 국가기술표준원), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11-11, https://korea.kr/news/pressReleaseView.do?newsId=156480155, 접근일 2026-09-25 (원문 미열람)
```

### runs/2026-10-11-01/pages/topics/2026/2026-10-11-area21-s7.md

```markdown
---
title: "21. 상호운용 표준·적합성 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "F. 연동"
primary_area_no: 21
related_areas: [14, 20, 22, 42, 48, 51, 54, 57]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-031, ref-032, ref-034, ref-1362, ref-1365, ref-138, ref-1412, ref-1430, ref-1431, ref-1432, ref-1434, ref-1435, ref-1439, ref-1442, ref-1443, ref-230, ref-413, ref-705]
last_run: 2026-10-11
version: 1
split_from: docs/categories/integration/interoperability-standards-and-conformance.md#7
---

[홈](../../index.md) › [주제](../index.md) › 21. 상호운용 표준·적합성 — 관련 표준·프레임워크·오픈소스

# 21. 상호운용 표준·적합성 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 표준은 로봇–관제 규격, 변경 알림 규칙, 적합성 시험, 감사·서비스 관리, 국내 표준으로 나뉜다. [의견] 2026-09-25 에 쓴 표준 비교표와 이전 내용은 [21. 상호운용 표준·적합성 — 관련 표준·프레임워크·오픈소스 (2026-09-25)](2026-09-25-area28-s7.md)에 있고 그 페이지의 정정은 다음 갱신 실행으로 넘겼으며, 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.
- 이 페이지는 [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 표준은 로봇–관제 규격, 변경 알림 규칙, 적합성 시험, 감사·서비스 관리, 국내 표준으로 나뉜다. [의견] 2026-09-25 에 쓴 표준 비교표와 이전 내용은 [21. 상호운용 표준·적합성 — 관련 표준·프레임워크·오픈소스 (2026-09-25)](2026-09-25-area28-s7.md)에 있고 그 페이지의 정정은 다음 갱신 실행으로 넘겼으며, 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

아래 소절은 2026-10-11 실행에서 보태거나 바로잡은 내용이다.

### VDA 5050 3.0.0 의 판과 날짜

[VDA 5050](../../glossary/vda-5050.md) 공식 저장소의 3.0.0 명세 마크다운 표지는 판을 'Version 3.0.0'으로만 적고 날짜를 적지 않는다(2026-10-11 확인). [사실][^ref-031] [2026-09-25 표준 표](2026-09-25-area28-s7.md)의 VDA 5050 행 발행일은 단일 날짜로 확정하지 않고 '미확인'으로 두되, VDA 발행물 카탈로그의 표시일(2026-03-17)과 3.0 발표 보도자료의 날짜(2026-04-20)가 서로 다르다는 점은 [20. 로봇·제조사 관제 연동 — 관련 표준·프레임워크·오픈소스](2026-10-10-area20-s7.md)의 「VDA 5050 3.0.0의 날짜 표시」 부분으로 연결하는 것이 맞다. [의견][^ref-1412][^ref-032][^ref-031] 3.0.0 작업에 참여했다고 밝힌 업체 Idealworks 는 2026년 3월 소식 글에서 VDMA·VDA 가 2026-02-17 에 3.0.0 판을 정식 채택했고 이어 법적 승인 절차를 거쳤다고 적어, VDA 자료의 날짜 표시와 또 다른 날짜를 제시한다. 이는 업체 서술이며 VDA 자료로는 확인되지 않았다. [추정][^ref-1442] 세 날짜는 한쪽을 고르지 않고 함께 두며, oq-005 에 출처 충돌로 올린다.

### 공식 태그의 JSON 스키마를 시험 입력으로 쓸 때

공식 저장소 3.0.0 태그의 [JSON 스키마](../../glossary/json-schema.md) 가운데 주문(order)·팩트시트(factsheet)·시각화(visualization) 스키마에는 닫는 괄호 바로 앞에 쉼표가 오는 끝 쉼표(trailing comma)가 있어 엄격한 JSON 으로 읽히지 않는다(2026-10-11 확인). [사실][^ref-1430][^ref-1431][^ref-1432] main 브랜치의 주문 스키마는 같은 자리에 끝 쉼표가 없다. [사실][^ref-413] 두 관찰은 스키마 파일의 구문에 관한 것이며 로봇 적합성 시험 결과가 아니다. [의견] 3.0.0 을 시험 입력으로 쓸 때는 '공식 태그'와 '파싱 가능한 시험 입력'을 따로 확인하고, 수정한 스키마를 쓰면 원본과의 차이·수정 근거·해시를 보존하며, main 브랜치 내용을 설명 없이 섞지 않는 것이 좋다. [의견][^ref-1430][^ref-413]

### OPC UA for Robotics 의 서버 기능 묶음

OPC 40010-1(OPC UA for Robotics Part 1) 1.02판(2025-09-08)의 §11.2.2 는 서버 기능 묶음(Facet)을 기본(Base)·운전(MDS Operation)·자산관리 확장(AM Extended)·상태감시 확장(CM Extended) 넷으로 나누고, 표 124~127 에서 각 적합성 단위를 필수(M)와 선택(O)으로 구분한다. [사실][^ref-034] 그래서 연동 요구에는 'OPC UA 지원' 대신 OPC UA Robotics 판·서버 Facet·선택 단위·인증 범위를 적게 하고, 이 정보모델을 VDA 5050 주문 스키마와 일대일로 자동 변환할 수 있다고 보지 않는 것이 좋다. [의견][^ref-034] OPC 제품 인증은 재단이 인정한 시험소에서 받으며, 제조사는 인증 시험 전에 적합성 시험 도구로 미리 시험해 보도록 권고된다(6절). [사실][^ref-705][^ref-1434]

### MassRobotics AMR 상호운용 표준 스키마

MassRobotics 공식 JSON 스키마(커밋 f9357a4 기준)의 최상위 구조는 [신원 보고](../../glossary/identity-report.md)(identityReport)와 상태 보고(statusReport) 두 정의만 참조하고, 위치(location) 정의는 x·y·angle·planarDatum 네 필드를 모두 필수로 두며, 명령·주문·작업 메시지 정의는 없다(2026-10-11 확인). [사실][^ref-230] 따라서 이 보고 메시지(신원·상태) 교환만으로 작업 명령 호환성이나 좌표계 정합을 확보했다고 주장하지 않는 것이 맞다. [의견][^ref-230]

### 국내 표준

국가표준인증통합정보시스템(KSSN)에는 KS B 7321-2 '로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델'과, 이와 별도로 KS B ISO 22166-202 '로봇 — 서비스 로봇의 모듈화 — 제202부: 소프트웨어 모듈용 정보 모델'이 실려 있다(2026-10-11 확인). [사실][^ref-138][^ref-1435] 두 표준의 제정일·부합화 수준(IDT 여부)·고시번호와 서로의 대체 관계는 이번 열람에서 보이지 않아 미확인이다(oq-026).

### IDS 1.0 — 건물 정보 모델 데이터 교환 요구의 적합성 검사

buildingSMART 는 [정보 전달 명세](../../glossary/information-delivery-specification.md)(Information Delivery Specification, IDS)를 2024-06-01 승인된 공식 표준으로 소개하고, 데이터 요구를 기계가 읽을 수 있게 기술해 [IFC](../../glossary/ifc.md) 모델의 적합성을 자동으로 검사하게 한다고 설명하며, 1.0 이전 판은 공식 표준이 아니라고 밝힌다. [사실][^ref-1439] IDS 파일은 하나 이상의 명세(specification)로 이루어지고, 각 명세는 적용 대상(applicability)과 요구(requirements)를 가지며, 둘 다 엔터티·속성(attribute)·분류·속성 값(property)·재료·소속(partOf) 패싯으로 구성된다. [사실][^ref-1362] 받는 쪽은 IDS 와 IFC 를 함께 불러 검사해 불일치 보고를 얻는다. [사실][^ref-1362] 패싯 파라미터에는 단순 값 대신 열거·패턴·범위·길이의 복합 제한을 걸 수 있다. [사실][^ref-1365] 공식 저장소는 소프트웨어 구현의 IDS 읽기·검사 기능이 올바른지 확인하는 .ids·.ifc 쌍 250개 이상의 시험 파일 묶음도 둔다. [사실][^ref-1443]

이 영역(21. 상호운용 표준·적합성)에서는 IDS 1.0 을 IFC 데이터 교환 요구의 적합성 검사 수단으로만 짧게 두고, 검사 도구 자체도 공식 시험 파일 묶음으로 확인할 수 있다는 점을 적되 로봇–관제 메시지 적합성 시험과는 구별하는 것이 맞다. [의견][^ref-1439][^ref-1362][^ref-1443] 로봇 지도용 BIM 객체·속성 요구의 세부는 [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md)와 [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) 트랙에 두는 것이 맞다. [의견][^ref-1439] 이 소절은 건축 도면 자동 인식 트랙 실행 2026-10-09-26 의 반영 제안을 일부 반영한 것이다. 제안 가운데 기수(필수·선택·금지), 사용자 정의 속성 세트 명명 규칙, 뉴질랜드 OBOS 프록시 관례는 원문으로 확인하지 못해 싣지 않았다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/integration/interoperability-standards-and-conformance.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/integration/interoperability-standards-and-conformance.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md)
- 관련 영역: [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/integration/interoperability-standards-and-conformance.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-11
[^ref-032]: VDA(Verband der Automobilindustrie), Version 3.0 of VDA 5050 released, 2026-04-20, https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN, 접근일 2026-10-11
[^ref-034]: OPC Foundation / VDMA, OPC-40010-1 – OPC UA for Robotics - Part 1: Vertical Integration, 2025-09-08, https://reference.opcfoundation.org/specs/OPC-40010-1, 접근일 2026-10-11
[^ref-1362]: buildingSMART International (buildingSMART/IDS GitHub), IDS — Documentation/UserManual/README.md, 미확인, https://github.com/buildingSMART/IDS/blob/development/Documentation/UserManual/README.md, 접근일 2026-10-11
[^ref-1365]: buildingSMART International (buildingSMART/IDS GitHub), IDS — Documentation/UserManual/restrictions.md, 미확인, https://github.com/buildingSMART/IDS/blob/development/Documentation/UserManual/restrictions.md, 접근일 2026-10-11
[^ref-138]: 국가표준인증통합정보시스템(KSSN), KS B 7321-2 로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델, 미확인, https://www.kssn.net/search/stddetail.do?itemNo=K001010147546, 접근일 2026-10-11
[^ref-1412]: VDA(Verband der Automobilindustrie), VDA 5050, 2026-03-17, https://www.vda.de/en/news/publications/publication/vda-5050, 접근일 2026-10-11
[^ref-1430]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/order.schema (tag 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/3.0.0/json_schemas/order.schema, 접근일 2026-10-11
[^ref-1431]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema (tag 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/3.0.0/json_schemas/factsheet.schema, 접근일 2026-10-11
[^ref-1432]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/visualization.schema (tag 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/3.0.0/json_schemas/visualization.schema, 접근일 2026-10-11
[^ref-1434]: OPC Foundation, Overview & Benefits — OPC Foundation Certification, 미확인, https://opcfoundation.org/certification/overview-benefits/, 접근일 2026-10-11
[^ref-1435]: 국가표준인증통합정보시스템(KSSN), KS B ISO 22166-202 로봇 — 서비스 로봇의 모듈화 — 제202부: 소프트웨어 모듈용 정보 모델, 미확인, https://www.kssn.net/search/stddetail.do?itemNo=K001010158171, 접근일 2026-10-11
[^ref-1439]: buildingSMART International, Information Delivery Specification (IDS), 미확인, https://www.buildingsmart.org/standards/bsi-standards/information-delivery-specifications-ids/, 접근일 2026-10-11
[^ref-1442]: idealworks, VDA 5050 3.0.0 release (March 2026), 2026-03, https://idealworks.com/en/news/vda5050-300-release-march-2026, 접근일 2026-10-11
[^ref-1443]: buildingSMART International (buildingSMART/IDS GitHub), IDS — Documentation/README.md, 미확인, https://github.com/buildingSMART/IDS/blob/development/Documentation/README.md, 접근일 2026-10-11
[^ref-230]: MassRobotics, MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-10-11
[^ref-413]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/order.schema (main), 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/order.schema, 접근일 2026-10-11
[^ref-705]: OPC Foundation, How to Certify - OPC Foundation, 미확인, https://opcfoundation.org/certification/how-to-certify/, 접근일 2026-10-11

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-01 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-01 | 21. 상호운용 표준·적합성 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-10-11-01/pages/topics/2026/2026-10-11-area21-s6.md

```markdown
---
title: "21. 상호운용 표준·적합성 — 대표 접근법과 기술"
type: topic
category: "F. 연동"
primary_area_no: 21
related_areas: [14, 20, 22, 42, 48, 51, 54, 57]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-031, ref-1434, ref-1436, ref-408, ref-608, ref-705]
last_run: 2026-10-11
version: 1
split_from: docs/categories/integration/interoperability-standards-and-conformance.md#6
---

[홈](../../index.md) › [주제](../index.md) › 21. 상호운용 표준·적합성 — 대표 접근법과 기술

# 21. 상호운용 표준·적합성 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 여러 사업자를 한 현장에서 묶는 대표 접근은 판 번호 규칙으로 변경을 알리고, 적합성 시험으로 구현을 확인하고, 연동 수준을 나눠 통합하며, 서비스 수준과 감사 이력을 함께 기록하는 것이다. [의견] 2026-09-25 에 쓴 이전 내용은 [21. 상호운용 표준·적합성 — 대표 접근법과 기술 (2026-09-25)](2026-09-25-area28-s6.md)에 있으며, 그 페이지의 정정은 다음 갱신 실행으로 넘겼다.
- 이 페이지는 [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

여러 사업자를 한 현장에서 묶는 대표 접근은 판 번호 규칙으로 변경을 알리고, 적합성 시험으로 구현을 확인하고, 연동 수준을 나눠 통합하며, 서비스 수준과 감사 이력을 함께 기록하는 것이다. [의견] 2026-09-25 에 쓴 이전 내용은 [21. 상호운용 표준·적합성 — 대표 접근법과 기술 (2026-09-25)](2026-09-25-area28-s6.md)에 있으며, 그 페이지의 정정은 다음 갱신 실행으로 넘겼다.

아래 두 소절은 2026-10-11 실행에서 보태거나 바로잡은 내용이다.

### 적합성 시험과 인증을 구분해 읽기

OPC Foundation 의 인증 절차 안내는 제조사가 인증 시험 전에 가능한 많은 시험을 미리 해 보도록 권고하고, 재단이 제공하는 적합성 시험 도구(compliance test tools)는 시험소가 시험에 쓰는 도구라고 설명한다. [사실][^ref-705] 인증 개요 페이지는 인증 제품이 재단이 인정한 인증 시험소에서 시험을 거친 것이며, 인증된 SDK 를 쓴 응용도 공식 인증 제품이 되려면 각자 인증 시험을 받아야 한다고 밝힌다. [사실][^ref-1434] 2026-10-11 에 확인한 이 두 안내 페이지에는 제조사가 스스로 인증하는(self-certification) 경로가 없다. [사실][^ref-705][^ref-1434] 그래서 OPC 적합성 체계는 '제조사의 적합성 시험 도구 사전 점검(권고)'과 '인정 시험소 인증'으로 나눠 적고, 이 구조를 VDA 5050 의 인증 체계로 그대로 옮겨 쓰지 않는 것이 맞다. [의견][^ref-705][^ref-1434]

VDA 5050 에 VDA·VDMA 공인 적합성 인증 제도가 있는지는 이번에도 확정하지 못했다([열린 질문](../../open-questions.md) oq-055). 공개된 근거는 성격이 서로 다르다.

| 근거 종류 | 예 | 보여 주는 것과 한계 |
|---|---|---|
| 제3자 도구의 자체 진단 | vda5050-lab(8절) | 현재 판 v0.2.0 을 개발자 프리뷰로 부르며 인증 주장이 아니라고 스스로 밝힌다. [사실][^ref-408] |
| 벤더 간 인증 발표 | OTTO by Rockwell Automation 보도자료(2026-04-09) | OTTO 100·600·1200·1500 이 Idealworks·NAiSE·SYNAOS 등 VDA 5050 관제 소프트웨어 업체와 인증을 마쳤다고 밝히나, 시험한 프로토콜 판·시험 항목·시험 기관은 밝히지 않는다. [추정] 벤더 주장[^ref-608] |
| 전시 시연 | VDMA Mesh-Up 2025(5절 제조 공장 사례) | 혼합 플릿 구성을 보여 주지만 관제 공급자 교체는 전시장에서 실시간으로 시연하지 않는다. [사실][^ref-1436] |
| 인정 시험소 인증 | OPC Foundation 인증 프로그램 | 재단이 인정한 인증 시험소의 시험을 거친다. [사실][^ref-1434] |

VDA 5050 연동 승인의 근거는 이 네 가지를 서로 다른 근거 수준으로 나눠 기록하는 것이 맞다. [의견][^ref-408][^ref-608][^ref-1436][^ref-705][^ref-1434]

### 선택 필드·재전송·취소 후 갱신을 확인하는 동작 시험

VDA 5050 3.0.0 §7.1.1 은 로봇이 받은 선택(optional) 필드를 무시해서는 안 되고 쓸 수 없으면 UNSUPPORTED_PARAMETER(CRITICAL)로 알리게 하며, 관제(fleet control)에는 로봇이 지원하는 선택 필드만 보내도록 의무를 둔다. [사실][^ref-031] 같은 판은 연동 시험의 기대값으로 쓸 응답도 조항으로 정한다. [사실][^ref-031] 재전송 규칙 자체는 [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md)에 있고, 여기서는 시험 기대값 관점만 적는다.

| 시험 | 입력 | 기대 응답 |
|---|---|---|
| 미지원 선택 필드 | 로봇이 지원하지 않는 선택 파라미터가 든 주문 | UNSUPPORTED_PARAMETER(CRITICAL)로 주문 거절 [사실][^ref-031] |
| 같은 번호·같은 내용 재전송 | 같은 orderUpdateId, 같은 내용 | 무시 [사실][^ref-031] |
| 같은 번호·다른 내용 재전송 | 같은 orderUpdateId, 다른 내용 | SAME_ORDER_UPDATE_ID(WARNING) 보고, 이전 주문 계속 [사실][^ref-031] |
| 취소 후 갱신 | 취소된 주문의 후속 갱신 | ORDER_UPDATE_FOLLOWING_CANCEL(WARNING) [사실][^ref-031] |
| 관제 송신 범위 | 관제가 보내는 주문 | 로봇이 지원하는 선택 필드만 포함 [사실][^ref-031] |

로봇 연동 승인에는 버전 문자열 확인에 더해 위 다섯 행처럼 동작을 확인하는 시험표를 두고, 수신 직전 주문 상태와 관측 로그 누락 여부를 함께 보존하는 것이 좋다. [의견][^ref-031] 이 표는 조항을 시험 행으로 옮긴 구축자 제안이며 VDA·VDMA 공식 인증 항목 목록이 아니다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/integration/interoperability-standards-and-conformance.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/integration/interoperability-standards-and-conformance.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md)
- 관련 영역: [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/integration/interoperability-standards-and-conformance.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-11
[^ref-1434]: OPC Foundation, Overview & Benefits — OPC Foundation Certification, 미확인, https://opcfoundation.org/certification/overview-benefits/, 접근일 2026-10-11
[^ref-1436]: VDMA, Mobile Robots in Production: Mesh-Up 2025, 미확인, https://www.vdma.eu/en/mesh-up, 접근일 2026-10-11
[^ref-408]: ekusiadadus (GitHub), vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces), 미확인, https://github.com/ekusiadadus/vda5050-lab, 접근일 2026-10-11
[^ref-608]: OTTO by Rockwell Automation, OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments, 2026-04-09, https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/, 접근일 2026-10-11
[^ref-705]: OPC Foundation, How to Certify - OPC Foundation, 미확인, https://opcfoundation.org/certification/how-to-certify/, 접근일 2026-10-11

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-01 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-01 | 21. 상호운용 표준·적합성 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-10-11-01/pages/topics/2026/2026-10-11-area21-s8.md

```markdown
---
title: "21. 상호운용 표준·적합성 — 대표 연구와 자료"
type: topic
category: "F. 연동"
primary_area_no: 21
related_areas: [14, 20, 22, 42, 48, 51, 54, 57]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-1437, ref-1438, ref-253, ref-407, ref-408, ref-634, ref-638, ref-639, ref-704, ref-709]
last_run: 2026-10-11
version: 1
split_from: docs/categories/integration/interoperability-standards-and-conformance.md#8
---

[홈](../../index.md) › [주제](../index.md) › 21. 상호운용 표준·적합성 — 대표 연구와 자료

# 21. 상호운용 표준·적합성 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 자료는 학술 논문보다 규격 저장소와 공공기관 자료가 중심이다. [의견]
- 이 페이지는 [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 자료는 학술 논문보다 규격 저장소와 공공기관 자료가 중심이다. [의견]

- VDA / VDMA / KIT IFL, VDA 5050 공식 저장소 README(발행일 미확인) — 변경 제안 절차, 계획 판, 지원 의무 부인 문구를 담아 규격 거버넌스를 읽는 기본 자료다. [사실][^ref-634]
- MassRobotics, AMR_Interop_Standard 저장소(발행일 미확인) — 신원·상태 보고 스키마만 두는 보고 중심 규격이다. [사실][^ref-253]
- gpue, vda5050-sim(발행일 미확인) — VDA 5050 시뮬레이션·적합성 시험 묶음으로, 개인 프로젝트이며 VDA·VDMA 공식 시험이 아닌 것으로 보인다. [추정][^ref-407]
- ekusiadadus, vda5050-lab README(커밋 4a1a812 기준, 발행일 미확인) — MQTT 기록에서 VDA 5050 주문·재연결·취소 실패를 진단하는 도구로, 현재 판 v0.2.0 을 개발자 프리뷰(Developer Preview)로 부르며 오프라인 진단 구현과 범위가 제한된 합성 시연을 담는다고 설명하고, 공개 알파나 인증 주장이 아니며 실제 고객 기록·외부 시험 대상 장치(DUT)·실물 하드웨어 실행을 검증하지 않았다고 스스로 밝힌다(2026-10-11 확인). [사실][^ref-408] 그래서 MQTT 기록 진단의 보조 도구 후보로만 두고, 그 판정을 구매·연동 승인 전체의 대체물로 쓰지 않는 것이 맞다. [의견][^ref-408]
- Wagner, N. A. 외, Teleoperating Mobile Robots via VDA 5050 – A First Middleware Evaluation within Open Industrial Networks(제22회 IEEE WFCS, 2026-04) — 표준이 [원격 조작](../../glossary/teleoperation.md)을 기본으로 다루지 않는다고 보고 VDA 5050 원격 조작 확장(논문 제안이며 표준이 채택한 기능이 아니다)과 재현 평가용 VDA 5050 트래픽 생성기를 제안하며, VDA 5050 메시지·미들웨어 전송·Open RAN 무선 링크를 잇는 구성에서 지연과 통신 오버헤드를 평가한다. [사실][^ref-1437] 저자 소속 연구실의 소개문(2026-04-24)은 이 평가가 재현성 높은 가상 무선 시험대와 실제 무선 검증 구성을 함께 썼다고 설명하며, 정량 결과는 소개문에 없다. [사실][^ref-1438] 이 연구는 적합성 시험이 아니라 VDA 5050 통신 부하·지연 평가로 읽고, 상세 네트워크 설계는 [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md)에서 다루는 것이 맞다. [의견][^ref-1437][^ref-1438]
- OSRA, Open-RMF 프로젝트 헌장(2024-03)과 정책·절차 저장소 — 오픈소스 관제 프레임워크의 운영·개정 권한 구조를 보여 준다. [추정][^ref-704][^ref-639]
- 소프트웨어정책연구소(SPRi), 산업 디지털 전환 촉진법의 의미와 시사점(발행일 미확인) — 산업데이터 권리 규정을 해설한 국내 자료다. [사실][^ref-638]
- 국가기술표준원, 로봇 엘리베이터 탑승 KS 제정 보도자료(2021-11-11) — 속도 제어, 위험 상황 보호 정지, 높낮이차·틈새 극복, 추락·넘어짐 방지 기준을 다룬다. KS 번호는 미확인이다. [사실][^ref-709]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/integration/interoperability-standards-and-conformance.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/integration/interoperability-standards-and-conformance.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md)
- 관련 영역: [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/integration/interoperability-standards-and-conformance.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1437]: Wagner, N. A., Toenning, L., Lünsch, D., Jost, J., Wietfeld, C., Detzner, P., Teleoperating Mobile Robots via VDA 5050 – A First Middleware Evaluation within Open Industrial Networks, 2026-04, https://doi.org/10.1109/WFCS67029.2026.11511549, 접근일 2026-10-11
[^ref-1438]: TU Dortmund, Communication Networks Institute (ComNets), Interoperable Teleoperation of Mobile Robots in Intralogistics: Joint Paper Demonstrates End-to-End Network Co-Design for Smart Industries, 2026-04-24, https://comnets.etit.tu-dortmund.de/details/interoperable-teleoperation-of-mobile-robots-in-intralogistics-joint-paper-demonstrates-end-to-end-network-co-design-for-smart-industries-63558/, 접근일 2026-10-11
[^ref-253]: MassRobotics, AMR_Interop_Standard — MassRobotics AMR Interoperability Standard (README, JSON schema), 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard, 접근일 2026-09-25 (원문 미열람)
[^ref-407]: gpue (GitHub), vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS), 미확인, https://github.com/gpue/vda5050-sim, 접근일 2026-09-25 (원문 미열람)
[^ref-408]: ekusiadadus (GitHub), vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces), 미확인, https://github.com/ekusiadadus/vda5050-lab, 접근일 2026-10-11
[^ref-634]: VDA / VDMA / KIT IFL (VDA5050 GitHub), VDA5050/VDA5050 — README, 미확인, https://github.com/VDA5050/VDA5050, 접근일 2026-09-25
[^ref-638]: 소프트웨어정책연구소(SPRi), 산업 디지털 전환 촉진법의 의미와 시사점, 미확인, https://spri.kr/posts/view/23480?code=industry_trend, 접근일 2026-09-25 (원문 미열람)
[^ref-639]: Open Source Robotics Alliance (Open Robotics), osra-policies-and-procedures — README, 미확인, https://github.com/openrobotics/osra-policies-and-procedures, 접근일 2026-09-25
[^ref-704]: Open Source Robotics Alliance, Charter of the Open Source Robotics Alliance Project 'Open-RMF', 2024-03, https://osralliance.org/wp-content/uploads/2024/03/open-rmf-project-charter.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-709]: 대한민국 정책브리핑(산업통상자원부 국가기술표준원), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11-11, https://korea.kr/news/pressReleaseView.do?newsId=156480155, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-01 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-01 | 21. 상호운용 표준·적합성 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-10-11-01/pages/topics/2026/2026-10-11-area21-s11.md

```markdown
---
title: "21. 상호운용 표준·적합성 — 열린 질문"
type: topic
category: "F. 연동"
primary_area_no: 21
related_areas: [14, 20, 22, 42, 48, 51, 54, 57]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-031, ref-032, ref-1412, ref-1442]
last_run: 2026-10-11
version: 1
split_from: docs/categories/integration/interoperability-standards-and-conformance.md#11
---

[홈](../../index.md) › [주제](../index.md) › 21. 상호운용 표준·적합성 — 열린 질문

# 21. 상호운용 표준·적합성 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 규격의 판·발행일, 공식 적합성 시험 유무, 운영 주체 간 책임은 아직 확인되지 않은 부분이 많다. [의견] 2026-09-25 에 정리한 이전 질문 목록은 [21. 상호운용 표준·적합성 — 열린 질문 (2026-09-25)](2026-09-25-area28-s11.md)에, 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

규격의 판·발행일, 공식 적합성 시험 유무, 운영 주체 간 책임은 아직 확인되지 않은 부분이 많다. [의견] 2026-09-25 에 정리한 이전 질문 목록은 [21. 상호운용 표준·적합성 — 열린 질문 (2026-09-25)](2026-09-25-area28-s11.md)에, 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

2026-10-11 실행에서 부분 근거가 더해진 질문과 새 질문은 다음과 같다.

- **oq-005** (상태: 열림 · 부분 근거 실행 2026-10-11-01) 출처 충돌: VDA 5050 3.0.0 의 정확한 발행일. 저장소 명세 표지에는 날짜가 없고, VDA 카탈로그(2026-03-17)·보도자료(2026-04-20)의 날짜 표시와 업체 Idealworks 글의 2026-02-17 채택 서술이 서로 다르다(7절). [추정][^ref-031][^ref-1412][^ref-032][^ref-1442]
- **oq-055** (상태: 열림 · 부분 근거 실행 2026-10-11-01) VDA 5050 공식 적합성 시험·인증 절차의 유무는 확정하지 못했다. 제3자 도구의 자체 진단·벤더 간 인증 발표·전시 시연·인정 시험소 인증을 나눠 보는 구분은 6절에 두었다.
- **oq-091** (상태: 열림 · 부분 근거 실행 2026-10-11-01) 3.0.0 태그 스키마의 끝 쉼표(7절)는 판 이행 시험 입력을 어떻게 고정하고 관리할지의 문제와 이어진다.
- **oq-026** (상태: 열림 · 부분 근거 실행 2026-10-11-01) KS B 7321-2 와 KS B ISO 22166-202 는 국가표준 목록에서 번호·제목만 확인했고, 제정일·부합화 수준·대체 관계와 국내 적용 사례는 미확인이다.
- **새 질문** (상태: 열림 · 제기 2026-10-11 · 실행 2026-10-11-01) VDA 5050 3.0.0 태그 스키마의 끝 쉼표를 고친 수정본을 연동 시험에 쓸 때 공식 PDF·태그와의 차이를 누가 승인하고 어떤 회귀 시험으로 확인하는가?
- **새 질문** (상태: 열림 · 제기 2026-10-11 · 실행 2026-10-11-01) VDA 5050 2.x·3.x 판이 섞인 플릿을 실제 현장에서 전환하면서 판별 스키마 차이와 시험 입력을 어떻게 검증했는지 공개한 기록이 있는가? (관련 기존 질문: oq-091)

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/integration/interoperability-standards-and-conformance.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/integration/interoperability-standards-and-conformance.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md)
- 관련 영역: [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/integration/interoperability-standards-and-conformance.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-11
[^ref-032]: VDA(Verband der Automobilindustrie), Version 3.0 of VDA 5050 released, 2026-04-20, https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN, 접근일 2026-10-11
[^ref-1412]: VDA(Verband der Automobilindustrie), VDA 5050, 2026-03-17, https://www.vda.de/en/news/publications/publication/vda-5050, 접근일 2026-10-11
[^ref-1442]: idealworks, VDA 5050 3.0.0 release (March 2026), 2026-03, https://idealworks.com/en/news/vda5050-300-release-march-2026, 접근일 2026-10-11

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-01 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-01 | 21. 상호운용 표준·적합성 의 "열린 질문" 절에서 분리 |
```

### runs/2026-10-11-01/pages/topics/2026/2026-10-11-area21-s10.md

```markdown
---
title: "21. 상호운용 표준·적합성 — 다른 연구영역과의 연결"
type: topic
category: "F. 연동"
primary_area_no: 21
related_areas: [14, 20, 22, 42, 48, 51, 54, 57]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-11
updated: 2026-10-11
sources: [ref-004, ref-031, ref-560, ref-705, ref-707, ref-709]
last_run: 2026-10-11
version: 1
split_from: docs/categories/integration/interoperability-standards-and-conformance.md#10
---

[홈](../../index.md) › [주제](../index.md) › 21. 상호운용 표준·적합성 — 다른 연구영역과의 연결

# 21. 상호운용 표준·적합성 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 상호운용 표준·적합성는 규격 판·책임 분리, 적합성 시험, 판 이행, 감사 추적, 통합자 위험성평가, 승강기 연동 표준을 통해 다른 영역과 맞물리는 것으로 보인다. [추정][^ref-031][^ref-004][^ref-705][^ref-707][^ref-560][^ref-709]
- 이 페이지는 [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

21. 상호운용 표준·적합성는 규격 판·책임 분리, 적합성 시험, 판 이행, 감사 추적, 통합자 위험성평가, 승강기 연동 표준을 통해 다른 영역과 맞물리는 것으로 보인다. [추정][^ref-031][^ref-004][^ref-705][^ref-707][^ref-560][^ref-709]

- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) — 규격 판과 관제–로봇 책임 분리가 연동 구현의 전제다.
- [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) — 로봇 승강기 탑승 KS 같은 설비 연동 표준을 공유한다.
- [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md) — 적합성 시험·인증을 새 로봇 연동 승인에 쓰는 방법을 다룬다.
- [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) — 펌웨어·프로토콜 판 이행과 폐기 예고가 수명주기 관리와 겹친다.
- [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md) — 통합자의 시스템 수준 위험성평가를 누가 맡는지가 책임 경계의 핵심이다.
- [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md) — 감사 추적 요구가 보안 표준에서 온다.

- [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md) — VDA 5050 메시지의 통신 지연·오버헤드 평가와 무선망 설계는 적합성 시험과 구별해 이 영역에서 다룬다.
- [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) — IDS 1.0 으로 검사하는 BIM(IFC) 데이터 교환 요구 가운데 로봇 지도용 객체·속성 요구의 세부가 이 영역과 [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) 트랙의 몫이다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/integration/interoperability-standards-and-conformance.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/integration/interoperability-standards-and-conformance.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md)
- 관련 영역: [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/integration/interoperability-standards-and-conformance.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-11
[^ref-560]: ISO, ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells, 2025-02, https://www.iso.org/standard/73934.html, 접근일 2026-09-25 (원문 미열람)
[^ref-705]: OPC Foundation, How to Certify - OPC Foundation, 미확인, https://opcfoundation.org/certification/how-to-certify/, 접근일 2026-10-11
[^ref-707]: IEC, IEC 62443-3-3:2013 Industrial communication networks — Network and system security — Part 3-3: System security requirements and security levels (sample), 2013-08, https://cdn.standards.iteh.ai/samples/19488/7c0b753be32e46fc986c23c32efbdbe8/IEC-62443-3-3-2013.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-709]: 대한민국 정책브리핑(산업통상자원부 국가기술표준원), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11-11, https://korea.kr/news/pressReleaseView.do?newsId=156480155, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-11-01 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-11 | 2026-10-11-01 | 21. 상호운용 표준·적합성 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 21건 / 전체 1419건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 2026-09-25 | 예 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 2026-09-25 | 예 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 2026-09-25 | 예 |
| ref-253 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — README | 미확인 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard | 2026-09-25 | 아니오 |
| ref-407 | gpue (GitHub) | vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS) | 미확인 | https://github.com/gpue/vda5050-sim | 2026-09-25 | 예 |
| ref-408 | ekusiadadus (GitHub) | vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces) | 미확인 | https://github.com/ekusiadadus/vda5050-lab | 2026-09-25 | 예 |
| ref-560 | ISO | ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells | 2025-02 | https://www.iso.org/standard/73934.html | 2026-09-25 | 아니오 |
| ref-608 | OTTO by Rockwell Automation | OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments | 2026-04 | https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/ | 2026-09-25 | 아니오 |
| ref-634 | VDA / VDMA / KIT IFL (VDA5050 GitHub) | VDA5050/VDA5050 — README | 미확인 | https://github.com/VDA5050/VDA5050 | 2026-09-25 | 예 |
| ref-635 | Semantic Versioning (Tom Preston-Werner, semver.org) | Semantic Versioning 2.0.0 | 미확인 | https://semver.org/spec/v2.0.0.html | 2026-09-25 | 예 |
| ref-636 | European Union (EUR-Lex) | Regulation (EU) 2023/2854 of the European Parliament and of the Council of 13 December 2023 on harmonised rules on fair access to and use of data (Data Act) | 2023-12-13 | https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng | 2026-09-25 | 아니오 |
| ref-637 | 국가법령정보센터(산업통상자원부) | 산업 디지털 전환 촉진법 (법률 제18692호) | 2022-01-04 | https://www.law.go.kr/법령/산업디지털전환촉진법/(18692,20220104) | 2026-09-25 | 아니오 |
| ref-638 | 소프트웨어정책연구소(SPRi) | 산업 디지털 전환 촉진법의 의미와 시사점 | 미확인 | https://spri.kr/posts/view/23480?code=industry_trend | 2026-09-25 | 아니오 |
| ref-639 | Open Source Robotics Alliance (Open Robotics) | osra-policies-and-procedures — README | 미확인 | https://github.com/openrobotics/osra-policies-and-procedures | 2026-09-25 | 예 |
| ref-704 | Open Source Robotics Alliance | Charter of the Open Source Robotics Alliance Project 'Open-RMF' | 2024-03 | https://osralliance.org/wp-content/uploads/2024/03/open-rmf-project-charter.pdf | 2026-09-25 | 아니오 |
| ref-705 | OPC Foundation | How to Certify - OPC Foundation | 미확인 | https://opcfoundation.org/certification/how-to-certify/ | 2026-09-25 | 아니오 |
| ref-706 | IETF (RFC Editor) | RFC 9745: The Deprecation HTTP Response Header Field | 미확인 | https://www.rfc-editor.org/info/rfc9745/ | 2026-09-25 | 아니오 |
| ref-707 | IEC | IEC 62443-3-3:2013 Industrial communication networks — Network and system security — Part 3-3: System security requirements and security levels (sample) | 2013-08 | https://cdn.standards.iteh.ai/samples/19488/7c0b753be32e46fc986c23c32efbdbe8/IEC-62443-3-3-2013.pdf | 2026-09-25 | 아니오 |
| ref-708 | ISO/IEC | ISO/IEC 20000-1:2018 - Information technology — Service management — Part 1: Service management system requirements | 2018 | https://www.iso.org/standard/70636.html | 2026-09-25 | 아니오 |
| ref-709 | 대한민국 정책브리핑(산업통상자원부 국가기술표준원) | 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 | 2021-11-11 | https://korea.kr/news/pressReleaseView.do?newsId=156480155 | 2026-09-25 | 아니오 |
| ref-710 | 한국지능형로봇표준포럼(KOROS) | KOROS 1148-8:2025 서비스 로봇을 위한 모듈 - 제2-8부 : 소프트웨어 모듈용 정보모델 상호운용성 시험 절차 | 2025-06-04 | http://www.koros.or.kr/bbs/board.php?bo_table=notice27&wr_id=223 | 2026-09-25 | 아니오 |
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

### docs/open-questions.md (요약: 대상 영역 [21] 에 걸린 48건 / 전체 369건)

```markdown
- oq-004 [열림] IEEE 1872 계열 로봇 온톨로지 표준이나 AAS 능력 서브모델을 KS로 부합화했거나 국내 로봇 관제 사업에 적용한 사례가 있는가? (영역 5, 21)
- oq-005 [열림] 출처 충돌: VDA 5050 3.0.0의 정확한 발행일은 언제인가? 검색 요약은 3.0 발행을 2026-03-19, 보도자료를 2026-04-20로 전하지만 보도자료 URL은 2026-04-21 계열이다. (영역 20, 21)
- oq-020 [열림] ISA-95 작업 지시·작업 응답(B2MML, OPC UA for ISA-95 Job Control)을 VDA 5050 주문·상태나 Open-RMF 작업 요청·상태로 옮기는 표준 매핑이나 공개 구현이 있는가? (영역 20, 21, 23)
- oq-025 [열림] 출처 충돌: VDMA LIF 의 판과 발행일은 무엇인가(VDA 5050 3.0.0 은 VDMA 2024-03 으로 인용하고, LIF 공식 저장소 README 는 1.0.0 판을 2023-09 로 적는다)? (영역 15, 21)
- oq-026 [열림] KS B 7321-2(서비스 로봇 모듈용 정보 모델 — 소프트웨어 모듈)가 ISO 22166-202와 부합화된 표준인지, 국내 물류 로봇·관제 사업에 적용한 사례가 있는가? (IEEE 1872 계열·AAS 능력 서브모델의 KS 부합화를 묻는 oq-004와 연결된다) (영역 5, 21)
- oq-027 [열림] ISO 21423 의 공통 좌표계(CCS)는 발행판에서 어떻게 정의되며, VDA 5050 mapId·Open-RMF 지도·층 이름·MassRobotics planarDatum 과 어떻게 대응하는가? (영역 15, 21)
- oq-041 [열림] 대한승강기협회 '엘리베이터와 로봇의 상호 연동을 위한 가이드라인' 단체표준은 어떤 메시지·상태(호출·탑승·하차·세션 해제 등)를 정하며, Open-RMF 승강기 요청·상태 메시지와 어떻게 대응하는가? (영역 21, 22)
- oq-044 [열림] 국내에서 ISO 19164 나 IndoorGML 2.0 을 KS 로 부합화했거나, CityGML 2.0 과 IndoorGML 공간 개념을 원칙으로 둔 실내공간정보 구축 작업규정을 새 판 표준에 맞춰 개정한 사례가 있는가? (영역 15, 21)
- oq-055 [열림] VDA 5050 에 공식 적합성 시험·인증 절차가 있는가, 없다면 제3자 오픈소스 적합성 시험 도구의 결과를 새 로봇 연동 승인 기준으로 쓸 수 있는가? (영역 20, 21, 54)
- oq-065 [열림] 제조사가 다른 이동로봇이 같은 충전기를 함께 쓸 수 있게 하는 충전 커넥터·충전 통신의 공통 규격이나 공개 사례가 있는가? (영역 21, 28)
- oq-085 [열림] 제조용 ISO 23247 디지털 트윈 프레임워크(참조 구조·디지털 트윈 결합)를 물류센터의 이종 로봇·설비에 그대로 적용할 수 있는가, 물류용 확장이 필요한가? (영역 21, 34)
- oq-089 [열림] 국내 시험기관(한국로봇산업진흥원 등)의 로봇 시험 항목에 다중 로봇 관제·오케스트레이션 소프트웨어 수준의 시험이 포함되는가, 없다면 누가 그 기준을 정하는가? (영역 21, 54)
- oq-091 [열림] VDA 5050 2.x 판과 3.0.0 판 로봇이 섞인 플릿에서 주 버전 차이를 어떻게 운영·이행하는가? (영역 20, 21, 57)
- oq-096 [열림] 여러 제조사 로봇이 섞인 현장에서 R15.08-2 가 말하는 통합자의 시스템 수준 위험성평가를 ROP 사업자·제조사·설비업체 중 누가 수행하고 갱신하는가? (영역 21, 48)
- oq-101 [열림] 여러 화주가 로봇 플릿을 공유하는 창고에서 고객별 작업·데이터 격리를 오케스트레이션 수준에서 규정한 표준이나 공개 설계가 있는가? (영역 21, 51)
- oq-105 [열림] 물류 현장 로봇의 작업 계획·배정에 쓰는 AI 가 한국 인공지능 기본법의 고영향 인공지능 영역에 해당하는가, 해당하면 ROP 사업자와 현장 운영사 중 누가 책무를 지는가? (영역 21, 47)
- oq-108 [열림] 제조용 CMSD 같은 중립 시뮬레이션 데이터 형식을 물류센터 로봇 시뮬레이션의 입력(레이아웃·주문 흐름·재고·로봇 자원)에 쓴 사례가 있는가, 없다면 물류용 확장이 필요한가? (영역 21, 34)
- oq-109 [열림] ROP 사업자·로봇 제조사·현장 운영사가 함께 만든 로봇 운행·상태 데이터의 사용·수익 권리를 산업디지털전환촉진법의 공동 생성 규정에 따라 계약에서 어떻게 나누는가, 국내 로봇 관제 계약 사례가 있는가? (영역 21)
- oq-110 [열림] EU 데이터법의 데이터 공유 의무가 이종 로봇 플릿에서 제조사가 ROP 사업자(제3자)에게 로봇 사용 데이터를 제공해야 하는 근거가 되는가, 된다면 그 범위는 무엇인가? (영역 20, 21)
- oq-111 [열림] KOROS 1148-8:2025 의 상호운용성 시험 절차는 어떤 시험 항목을 두며, 물류 로봇 관제 연동의 적합성 시험 기준으로 쓸 수 있는가? (영역 21, 54)
- oq-112 [열림] 이종 플릿 현장에서 ROP 가 고객과 맺는 가용성·응답 시간 목표를 제조사 관제·설비업체의 서비스 수준 목표와 어떻게 연쇄해 맞추며, 공개된 계약 구조나 사례가 있는가? (영역 21, 32)
- oq-115 [열림] 제조사가 자사 로봇 지도(SLAM 지도)의 판을 바꿀 때 변경 내용과 판 식별자를 ROP 나 상위 관제에 알리는 계약·인터페이스 관행이나 공개 사례가 있는가? (영역 21, 57)
- oq-122 [열림] 산업 디지털 전환 촉진법의 제명이 '산업 디지털 전환 및 인공지능 활용 촉진법'으로 바뀌어 시행되었는가, 바뀌었다면 데이터 공동 생성 규정의 조문 번호와 내용도 달라졌는가? (관련 기존 질문: oq-109) (영역 21)
- oq-124 [열림] 대화로 만든 층·구역·통로·문·승강기·충전 위치를 Open-RMF 빌딩 맵과 VDMA LIF 처럼 서로 다른 플릿 지도 형식으로 함께 내보낼 수 있는 공통 중간 표현이나 공식 변환 규칙이 있는가? (영역 8, 15, 21)
- oq-128 [열림] 국내 현장에서 VDA 5050 팩트시트나 자산관리셸 능력 기술을 로봇 등록 데이터로 실제 쓰는 사례가 있으며, 채팅 로봇 구성이 그 데이터를 읽어 되묻기를 줄일 수 있는가? (영역 10, 4, 21)
- oq-148 [열림] VDA 5050 팩트시트·IDTA 02047 서브모델·MassRobotics identityReport 사이의 필드 대응표(예: maximumLoadMass 와 cargoMaxWeight)가 공식으로 제공되는가, ROP 등록부는 어느 형식을 정본으로 삼고 나머지를 어떻게 변환해야 하는가? (영역 4, 21, 5)
- oq-154 [열림] 제조업의 능력·스킬·서비스 모델(CSS 온톨로지·IDTA 02020)과 이동로봇 규격(VDA 5050 팩트시트·IDTA 02047 AGV 기술 데이터·Open-RMF 작업 능력) 사이의 능력 대응표가 공식으로 제공되는가, 아니면 ROP 가 직접 매핑을 만들어 관리해야 하는가? (영역 6, 21, 5)
- oq-158 [열림] IDTA 서브모델 템플릿의 이전 판이 새 판 발행 6개월 뒤 deprecated 로 옮겨질 때 그 판에 묶인 로봇 등록 데이터와 능력 정의를 ROP 는 어떤 기준으로 재검증·이관해야 하는가? (영역 7, 21, 4)
- oq-159 [열림] 국내 이기종 로봇 통합 관제 제품(크롬스 등)이 VDA 5050 이나 MassRobotics AMR 상호운용 표준을 지원하는지 공개 자료로 확인되는가? (영역 1, 21)
- oq-167 [열림] 국내 제조 공장에서 서로 다른 제조사의 AGV·AMR·모바일 매니퓰레이터를 VDA 5050 같은 표준 인터페이스로 하나의 관제 계층 아래 운영한 공개 사례가 있는가(확인된 국내 사례는 자체 로봇 도입과 정부 시범사업뿐이다)? (영역 62, 21)
- oq-182 [열림] 이동로봇 특별법안이 간소화·표준화하겠다는 공동현관·엘리베이터 통신 연동 절차는 어떤 기존 표준(KS 로봇 승강기 탑승 요구사항, 홈네트워크 월패드 규격)을 참조하며, 한 단지에서 제조사가 다른 배송로봇이 같은 인터페이스를 쓰게 하는가? (영역 65, 22, 21)
- oq-190 [열림] 나라·주마다 다른 보도 로봇 규정(속도·크기·신고·보행자 의무)을 경로·속도 제약으로 기계가 읽을 수 있게 표현하는 공통 모델이 있으며, ISO 4448 의 경로 계획 충분성·운행 데이터 기록기 부분이 이를 다루는가? (영역 66, 21, 16)
- oq-191 [열림] 싱가포르 SS 713(로봇·승강기·자동문 데이터 교환)과 TR 130(로봇·중앙 관제 상호운용)은 무엇을 규정하며, ISO 제안은 어디까지 진행됐고 국내 로봇 승강기 탑승 KS 와는 어떻게 다른가? (영역 67, 22, 21)
- oq-195 [열림] SiLA 로봇·이동 로봇 작업반은 실험실 이동 로봇의 능력과 작업 인계를 어떻게 표현하려 하며, 결과물이 공개됐는가? (영역 67, 21, 5)
- oq-200 [열림] 출처 충돌: LIF 의 판·날짜가 저장소 README 기준 1.0.0(2023-09)과 VDA 5050 3.0.0 이 인용한 VDMA 2024-03 으로 다르다. 어느 쪽이 현행이며 두 날짜는 같은 판을 가리키는가? (영역 16, 21)
- oq-202 [열림] IEEE 1873-2015 가 2026-03 비활성 보류 상태가 된 뒤 로봇 지도 데이터 교환 표준을 잇는 IEEE·ISO 작업이 있는가? (영역 16, 21)
- oq-209 [열림] 국내에 클라우드 로봇·이기종 로봇 통합관제 플랫폼의 참조 구조나 외부 API 를 정한 TTA·KS 표준이 있는가? (영역 41, 21)
- oq-232 [열림] 착용형 장치나 출입 통제 신호로 얻은 사람 위치를 제조사가 다른 여러 로봇 플릿에 동시에 전달해 감속·정지시키는 표준 인터페이스나 사례가 있는가? (영역 49, 21)
- oq-237 [해결] 여러 제조사 로봇의 작업 상태와 실행 로그를 한 화면·한 기록 형식으로 모을 때 공통 작업 상태 값과 로그 수준을 정한 표준이나 공개 규약이 Open-RMF 작업 상태 스키마 말고도 있는가? (영역 37, 21)
- oq-244 [열림] 싱가포르 RoMi-H 처럼 공공 조달에서 상호운용 플랫폼 연동을 로봇 도입 요구 조건으로 둔 한국 공공병원·공공기관 사례가 있는가? (영역 2, 21)
- oq-246 [열림] 여러 제조사 플릿 관리 서버와 VDA 5050 브로커·Open-RMF 어댑터를 잇는 ROP 에서 브로커·API 의 상호 인증과 TLS 설정의 최소 요구를 정한 공개 보안 프로파일이 있는가? (영역 52, 20, 21)
- oq-270 [열림] 국내 공공·민간 로봇 조달에서 VDA 5050 같은 개방 인터페이스 적합성이나 통합자 인증을 입찰 요구조건으로 명시한 사례가 있는가? (영역 3, 21)
- oq-301 [열림] 로봇 오케스트레이션 플랫폼의 외부 API 를 OpenAPI·AsyncAPI 로 기술해 연동 적합성 시험의 기준으로 쓴 공개 시험 도구나 절차가 있는가? (영역 41, 21)
- oq-332 [열림] VDA 5050 동작 상태, MassRobotics 운용 상태, Open-RMF 작업 상태 값 사이의 대응표를 공개한 표준 기구나 프로젝트가 있는가, 없다면 플릿 관제 기록에서 어떤 기준으로 대응시키는가? (영역 37, 21)
- oq-334 [열림] MassRobotics 상태 보고의 오류 코드는 심각도 없는 자유 문자열인데, 이 표준을 쓰는 로봇과 VDA 5050 로봇이 섞인 플릿에서 오류 심각도를 어떤 기준으로 부여해 한 경보 체계에 넣는가? (관련: oq-033, oq-073) (영역 38, 21)
- oq-339 [열림] W3C Trace Context 의 추적 문맥을 ROS 2·DDS 메시지나 VDA 5050 같은 MQTT 기반 로봇–관제 메시지에 싣는 공식 직렬화 규약이 있는가? (영역 43, 21)
- oq-345 [열림] 로봇 관제 인터페이스(VDA 5050 주문, Open-RMF 작업 요청)에 작업 사이 의존·대안 경로·기한을 표현하는 확장 제안이나 차기 판 논의가 있는가? (관련 기존 질문: oq-049, oq-137) (영역 20, 21, 24)
- oq-348 [열림] 국내 공공건축 BIM 납품 기준(건설산업 BIM 시행지침 등)이나 로봇 친화형 건축물 인증이 로봇 충전 공간·작업 스테이션을 BIM 객체·속성으로 납품하도록 요구하거나 그 IDS·속성 세트를 정한 사례가 있는가? (관련 기존 질문: oq-199) (영역 14, 21)
```

### runs/2026-10-11-01/verification2.json

```json
{
  "run_id": "2026-10-11-01",
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
    "ok": false,
    "overlaps": [
      "6·7·11절을 replace 하면서 기존 분리 주제 페이지 링크가 빠졌다. 해당 페이지는 2026-09-25-area28-s6(대표 접근법과 기술), 2026-09-25-area28-s7(관련 표준·프레임워크·오픈소스, 표준 비교표 포함), 2026-09-25-area28-s11(열린 질문)이다. 새 분리 페이지 2026-10-11-area21-s6·s7·s11 에도 이전 페이지로 가는 링크가 없다. 그래서 이미 게시·검증된 이전 내용에 21. 상호운용 표준·적합성 페이지에서 더 이상 닿을 수 없다.",
      "이전 분리 페이지 2026-09-25-area28-s6·s7 에는 이번 실행에서 바로잡은 서술(f3·f5 선 유도 로봇 경로 계산, f15~f18 OPC 인증 경로)과 다른 문장이 남아 있다고 브리프가 보고했다(f5·f17 evidence, 입력에 본문이 없어 미대조). 정정은 additional_research_requests 로 다음 갱신 실행에 넘겼으므로 수용한다. 다만 링크가 끊긴 상태로 두 판이 함께 게시되면 독자가 둘의 관계를 알 수 없다.",
      "f3·f7·f4·f19·f21·f1·f2·f39 의 겹침은 1차 지시대로 새로 쓰지 않고 연결로 처리됐다. 연결 대상은 2026-10-09-area41-s6, 29. 명령·작업 실행의 신뢰성, 2026-10-10-area27-s7, 2026-10-10-area20-s7 이다."
    ]
  },
  "terminology": {
    "ok": true,
    "conflicts": []
  },
  "quotation_check": {
    "ok": true,
    "issues": []
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "6. 대표 접근법과 기술 절 patch: 첫 단락([의견] 요약 문장이 있는 단락으로, 자동 분리 뒤 원 절에 남는다)에 기존 분리 페이지 링크를 되살린다. 링크는 [21. 상호운용 표준·적합성 — 대표 접근법과 기술 (2026-09-25)](../../topics/2026/2026-09-25-area28-s6.md)이고, 'その 페이지의 정정은 다음 갱신 실행으로 넘겼다'는 문장은 'その' 없이 '그 페이지의 정정은 다음 갱신 실행으로 넘겼다'로 쓴다 — replace 로 이 링크가 사라져 이미 검증·게시된 이전 내용에 영역 페이지에서 닿을 수 없게 됐다.",
    "7. 관련 표준·프레임워크·오픈소스 절 patch: 첫 단락에 [21. 상호운용 표준·적합성 — 관련 표준·프레임워크·오픈소스 (2026-09-25)](../../topics/2026/2026-09-25-area28-s7.md) 링크와 '그 페이지의 정정은 다음 갱신 실행으로 넘겼다'는 문장을 되살린다 — 6절과 같은 이유이고, 그 페이지에는 표준 비교표가 있다.",
    "11. 열린 질문 절 patch: 첫 단락에 [21. 상호운용 표준·적합성 — 열린 질문 (2026-09-25)](../../topics/2026/2026-09-25-area28-s11.md) 링크를 되살린다 — 6절과 같은 이유다.",
    "7절 「VDA 5050 3.0.0 의 판과 날짜」 소절: '표의 VDA 5050 행 발행일은'의 '표'가 이 페이지에 없다. 기존 분리 페이지 2026-09-25-area28-s7 의 표로 링크하거나 '[2026-09-25 표준 표](…2026-09-25-area28-s7.md)의 VDA 5050 행'처럼 대상을 밝힌다 — 지금은 가리키는 표가 없는 문장이다.",
    "7절 「IDS 1.0」 소절 둘째 단락: '21. 상호운용 표준·적합성에서는 …'처럼 줄 첫머리에 '21. '이 오면 마크다운이 번호 목록으로 렌더링한다. '이 영역(21. 상호운용 표준·적합성)에서는 …'처럼 번호와 이름이 줄 첫머리에 오지 않게 고친다 — 표기 규칙상 번호와 이름을 함께 쓰는 것은 유지해야 한다.",
    "프런트매터 sources(5절 patch 의 frontmatter): 기존 페이지 sources 에 있던 ref-636·ref-637·ref-708·ref-710 을 되살린다. 위 링크 복원으로 다시 연결되는 기존 분리 페이지가 이들을 인용하는 것으로 보인다(기존 영역 페이지 13절에는 정의가 없고 프런트매터에만 있었다). 브리프와 1차 판정도 이들의 철회를 지시하지 않았다 — 설명 없이 빠진 것이며 diff_summary 에도 적혀 있지 않다. 되살리지 않는다면 diff_summary 에 이유를 적는다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인 / 2차 수정 후 재검증. 1차 기준 확인 37건, 미확인 0건, 교차 확인 0건. 강등: 없음. 원문 미열람 출처: 이번 브리프 출처 가운데는 없다. 기존 각주 ref-253·ref-407·ref-560·ref-638·ref-704·ref-706·ref-707·ref-709 는 '(원문 미열람)'을 유지한다. 주의: VDA 5050 3.0.0 의 날짜는 자료마다 다르게 표시되므로 단일 발행일을 확정하지 않는다(카탈로그 2026-03-17, 보도자료 2026-04-20, Idealworks 글 2026-02-17 채택. Idealworks 글은 업체 서술이며 [추정]). 적합성 시험 기대값 표와 승인 근거 수준 구분은 구축자 제안이며 VDA·VDMA 공식 인증 항목이 아니다. Mesh-Up 2025 는 automatica 2025 전시 시연이며 실제 공장 도입 사례가 아니다. 2차: 드리프트 없음. 1차 수정 지시 13건은 모두 이행됐다. 분리 페이지 정정과 표준 목록 항목명 정정은 입력 범위 밖이어서 추가 조사 요청으로 넘겼고, 이는 수용한다. [분류원문] 보존, 섹션 순서 준수, 태그·각주·'벤더 주장' 병기 유지, 범위 경계 준수. 지적 사항은 다음과 같다. (1) 6·7·11절을 replace 하면서 기존 분리 주제 페이지(2026-09-25-area28-s6·s7·s11) 링크가 빠져 이전에 검증된 내용에 영역 페이지에서 닿지 않는다. (2) 7절의 '표의 VDA 5050 행'이 이 페이지에 없는 표를 가리킨다. (3) 줄 첫머리 '21. '이 번호 목록으로 렌더링된다. (4) 프런트매터 sources 에서 ref-636·ref-637·ref-708·ref-710 이 설명 없이 빠졌다. 후속 정리 의견(이번 지시 대상 아님): 10절 요약 문장의 '상호운용 표준·적합성는'은 기존 문장에서 온 것으로, 번호가 빠졌고 조사도 어긋난다('21. 상호운용 표준·적합성은'). 분리 페이지 s10 에서 덧붙인 두 항목은 빈 줄 때문에 기존 목록과 나뉘어 있다. 검증 검색 0회, 열람 0회.",
  "retry_reason": null
}
```
