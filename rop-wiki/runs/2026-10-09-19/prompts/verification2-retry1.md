(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-09-19
- date: 2026-10-09
- run_type: update (갱신)
- 대상: 43. 데이터·관측성·배포 (K. 플랫폼 아키텍처·인프라)
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

### runs/2026-10-09-19/target.json

```json
{
  "run_id": "2026-10-09-19",
  "date": "2026-10-09",
  "weekday": "Fri",
  "run_number": 152,
  "run_type": "update",
  "forced": true,
  "target": {
    "area_no": 43,
    "area_name": "43. 데이터·관측성·배포",
    "category": "K. 플랫폼 아키텍처·인프라",
    "category_letter": "K"
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
  "selection_rationale": "CLI 지정 run_type=update, area=43"
}
```

### runs/2026-10-09-19/research.json

```json
{
  "run_id": "2026-10-09-19",
  "date": "2026-10-09",
  "run_type": "update",
  "target": {
    "area_no": 43,
    "area_name": "43. 데이터·관측성·배포",
    "category": "K. 플랫폼 아키텍처·인프라"
  },
  "gaps": [
    "섹션 5. 적용 사례 (현장 유형 명시) — 병원 사례의 수행 자원·제약 행이 '미확인'이고, 성공률 87.03% 와 122건·실패 14건의 불일치(oq-215)가 남아 있음. 제조 공장·상업 시설·가정·실외 사례 없음",
    "섹션 6. 대표 접근법과 기술(주제 페이지로 분리) — 운행 중 로봇 작업과 맞물린 순차 배포·롤백 절차(oq-213), 이종 기록을 하나의 추적 문맥으로 잇는 방법(oq-210)의 근거가 약함",
    "섹션 7. 관련 표준·프레임워크·오픈소스(주제 페이지로 분리) — 바뀐 출처 재확인 필요: OpenTelemetry 명세 상태, 생성형 AI 의미 규약 저장소 이동과 토큰 지표 이름(oq-212)",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 — 보존 정책의 국내 근거가 2023-6호 기준이며 현행 조문 미확인(oq-214), EU AI Act 로그 보관 주체(oq-316) 미반영",
    "섹션 11. 열린 질문 — oq-210·oq-212·oq-213·oq-214·oq-215·oq-316 부분 근거 미반영",
    "정정 요청 없음"
  ],
  "research_questions": [
    "플랫폼 자체의 상태·데이터·배포·비용을 어떻게 관리할 것인가? [분류원문]",
    "oq-214 현행 「개인정보의 안전성 확보조치 기준」은 2023-6호 이후 개정되었는가, 접속기록 보관·점검 조항은 무엇이 바뀌었는가? (섹션 9·11 겨냥, 한국 자료 우선)",
    "oq-316 EU AI Act 는 고위험 AI 의 자동 생성 로그를 누가 얼마나 보관하게 하며, 2026 년 개정으로 적용 시점이 바뀌었는가? (섹션 9·10·11 겨냥)",
    "oq-212 바뀐 출처: OpenTelemetry 명세 상태와 생성형 AI 토큰 지표의 현재 이름·단계·용도는 무엇인가? (섹션 7·11 겨냥)",
    "oq-213 장치·플랫폼 소프트웨어를 단계적으로 배포하고 작업 상태에 맞춰 설치를 미루거나 되돌리는 공개 기법은 무엇인가? (섹션 6·7·11 겨냥)",
    "oq-210 서로 다른 시스템의 기록을 하나의 추적 문맥으로 잇는 표준과 ROS 2 메시지 흐름 인과 분석 연구는 무엇인가? (섹션 6·7·8·11 겨냥)",
    "oq-215 구로병원 실증 논문의 성공률 분모와 수행 자원·제약은 원문에서 무엇으로 확인되는가? (섹션 5 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "2026-10-09 확인 기준 OpenTelemetry 명세 상태 요약은 추적(API·SDK·프로토콜)과 로그(브리지 API·SDK·프로토콜)를 안정, 지표는 API·프로토콜 안정에 SDK 혼합, 프로파일은 프로토콜 개발 단계로 표시해 2026-09-30 확인 내용과 같다.",
      "tag": "사실",
      "source_ids": [
        "ref-1036"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "상태 표: Tracing Stable/Stable/Stable, Metrics Stable/Mixed/Stable, Logs Bridge API Stable/Stable/Stable, Baggage Stable/Stable/N/A, Profiles 프로토콜 Development. 페이지에 갱신일 표시 없음 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "OpenTelemetry 의미 규약 사이트의 생성형 AI 지표 페이지는 생성형 AI 의미 규약이 별도 저장소(semantic-conventions-genai)로 옮겨졌고 이 페이지는 더 이상 관리하지 않는다고 안내한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1374"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "페이지 제목 'Moved: Generative AI semantic conventions', 안내문: \"This page has moved and is no longer maintained in this repository.\" (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "semantic-conventions-genai 저장소의 현재 토큰 지표 문서는 gen_ai.client.inference.usage.* 카운터 5종(입력·출력·캐시 읽기 입력·캐시 쓰기 입력·추론 출력)과 gen_ai.client.inference.operation.* 히스토그램 2종(입력·출력)을 모두 개발(Development) 단계로 정의하며, gen_ai.client.token.usage 나 이름 변경·폐기 안내는 담지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1037"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "카운터 단위 {token}, 필수 속성 gen_ai.operation.name·gen_ai.provider.name·gen_ai.token.modality. 히스토그램은 gen_ai.token.modality 없이 operation.name·provider.name 만 필수. 문서 안에 gen_ai.client.token.usage 언급과 이름 변경 안내 없음 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "같은 토큰 지표 문서는 캐시 읽기·캐시 쓰기·추론 카운터를 입력·출력 사용량 카운터의 부분집합으로 두고, 호출별 히스토그램은 백분위·이상값 분석용이며 합계나 비용 산정용이 아니라고 구분한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1037"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "operation 히스토그램은 백분위·이상값 분석용으로 합계·비용용이 아니며 명시된 버킷 경계를 쓰도록(SHOULD) 한다. 캐시·추론 카운터는 사용량 카운터의 부분집합 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "토큰 지표가 여전히 개발 단계이고 옛 이름(gen_ai.client.token.usage)에 대한 폐기·대응 안내가 없으므로(f2·f3), 언어 모델 호출 비용 계측은 별도 저장소의 특정 판을 고정해 카운터(gen_ai.client.inference.usage.*)로 합계를 잡고 히스토그램은 지연·이상값 분석에만 쓰는 방식이 가능해 보이나, oq-212 의 고정 기준은 표준이 정해 주지 않아 열린 채로 남는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1037",
        "ref-1374"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f2(저장소 이동 안내)와 f3·f4(현재 지표 이름·단계·용도 구분)에서 도출. 안정 판 일정은 두 문서 모두 밝히지 않음",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "바이라인네트워크 보도(2025-10-31)에 따르면 2025-10-31 시행된 「개인정보의 안전성 확보조치 기준」 개정은 접속기록 보관 대상을 개인정보취급자에서 개인정보처리시스템에 접속한 모든 자(정보주체 제외)로 넓혔고, 정의·인터넷망 차단 조항은 즉시 시행하되 내부 관리계획·접근권한·접근통제·접속기록 보관·점검 관련 조항에는 1년 유예를 두었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1367"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "기사(곽중희, 2025-10-31): 즉시 시행 제2조·제6조의2, 1년 유예 내부 관리계획·접근권한 관리·접근통제·접속기록 보관 및 점검 조항. 오픈마켓 판매자 접속기록은 보관하되 점검·사후조치는 개인정보취급자에 한해 가능. 고시 번호와 제8조 조문은 기사에 없음",
      "as_of": "2025-10-31",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f7",
      "claim": "f6 의 보도대로라면 페이지 9절이 인용한 2023-6호 기준(1년·2년 이상 보관, 월 1회 이상 점검)은 현행 조문과 다를 수 있고 유예가 2026년 말 전후에 끝나므로, 로봇 플랫폼의 접속기록 대상 범위(운영자 계정 외 접속자 포함 여부)를 현행 고시 원문으로 다시 확인해야 할 것으로 보이며, 개정 고시 번호·제8조 현행 문구·유예 종료일은 이번에 확인하지 못했다(oq-214 부분 근거).",
      "tag": "추정",
      "source_ids": [
        "ref-1367",
        "ref-766"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "ref-766(2023-6호, 원문 미열람)과 ref-1367(2025-10-31 보도) 비교에서 도출. 국가법령정보센터 현행 조회는 이번 실행에서 연결 오류로 열지 못함",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f8",
      "claim": "연계 대상: EU AI Act 제19조 제1항은 고위험 AI 시스템 제공자가 자기 통제 아래 있는 제12조 제1항의 자동 생성 로그를 의도된 목적에 맞는 기간, 적어도 6개월 보관하게 하고, 다른 EU·회원국 법(특히 개인정보 보호법)이 달리 정하면 그에 따르게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1313"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"of at least six months, unless provided otherwise in the applicable Union or national law\". 제2항: 금융기관 제공자는 금융 규제상 문서의 일부로 보관. 페이지는 2026-07-27 기준 EUR-Lex 통합본을 반영하며 제19조는 개정 표시 없음",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "연계 대상: EU AI Act 제26조는 고위험 AI 시스템 배포자에게 사용 설명서에 따라 운영을 감시하고 위험이 의심되면 제공자·유통자·시장감시당국에 알리고 사용을 멈추게 하며(제5항), 자기 통제 아래 있는 자동 생성 로그를 적어도 6개월 보관하게 한다(제6항).",
      "tag": "사실",
      "source_ids": [
        "ref-1314"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제6항: 배포자는 통제 범위의 로그를 목적에 맞는 기간, 적어도 6개월(EU·회원국 법이 달리 정하지 않는 한) 보관. 제5항: 사용 설명서 기반 감시와 지체 없는 통보",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f10",
      "claim": "연계 대상: 로펌 Hunton 의 글(2026-07-28)에 따르면 AI 디지털 옴니버스 규정(Regulation (EU) 2026/1744)이 2026-07-27 발효되어 부속서 III 고위험 AI 의무 적용일을 2027-12-02 로, 부속서 I 규제 제품에 내장된 고위험 AI 의무 적용일을 2028-08-02 로 미뤘다.",
      "tag": "사실",
      "source_ids": [
        "ref-1370"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "규정 번호 2026/1744, 발효 2026-07-27(관보 게재 3일 뒤), 부속서 III 2027-12-02, 부속서 I 2028-08-02. EUR-Lex 원문은 열지 않음",
      "as_of": "2026-07-28",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f11",
      "claim": "제19조는 제공자, 제26조는 배포자에게 각자 통제하는 로그의 6개월 이상 보관을 지우므로(f8·f9), 로봇 플랫폼의 AI 구성요소가 고위험으로 분류되면 플랫폼 사업자가 제공자인지 배포자인지(또는 둘 다인지)와 로그 통제권 배분에 따라 실행 기록 보관 책임이 갈리고, 기계류 등 부속서 I 제품에 내장된 경우라면 적용 시점은 2028-08-02 로 보인다(f10, oq-316 부분 근거).",
      "tag": "추정",
      "source_ids": [
        "ref-1313",
        "ref-1314",
        "ref-1370"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f8·f9·f10 에서 도출. 로봇 플랫폼이 고위험 AI 에 해당하는지, 부속서 I·III 중 어디에 속하는지는 출처가 다루지 않음",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "구로병원 실증 논문은 배송 요청 135건에서 긴급 13건을 빼고 122건(평일 80·주말 42)을 분석 대상으로 삼았고, 실패 14건을 보고하며 3.4절에서 완료 시행 108건을 분석하지만 전체 성공률 87.03% 의 분모를 밝히지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-943"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "요청 135건 → 긴급 13건 제외 → 적격 임무 122건, 실패 14건(3.2절), 완료 시행 108건(3.4절). 87.03% 산출 방식 서술 없음",
      "as_of": "2026-03-31",
      "site_type": "병원",
      "flow_item": "예외·성과"
    },
    {
      "id": "f13",
      "claim": "논문 수치로는 122건 중 성공 108건이 약 88.5% 가 되어 87.03% 와 맞지 않으므로, oq-215 의 성공률 분모는 원문만으로 해소되지 않고 페이지의 87.03% 는 '저자 보고' 수치로 두는 것이 맞아 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-943"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "108/122 ≈ 88.5%. 원문에 다른 분모 설명이 없어 불일치 원인 미확인",
      "as_of": "2026-03-31",
      "site_type": "병원",
      "flow_item": "예외·성과"
    },
    {
      "id": "f14",
      "claim": "구로병원 실증의 수행 자원은 Level 3+ 로 소개된 DOGU IROI 배송 로봇 1대와 병원 내 물류에 주로 쓰는 직원 전용 승강기 1대(TK Elevator TK50M)였고, 단일 로봇 운영을 대상으로 했다.",
      "tag": "사실",
      "source_ids": [
        "ref-943"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "로봇 1대(DOGU IROI), 직원 전용 승강기 TK50M 1대, 단일 로봇 운영. 설문 참여자 간호사 8·약사 7·지원 인력 7명은 전체 인력 수가 아님",
      "as_of": "2026-03-31",
      "site_type": "병원",
      "flow_item": "수행 자원"
    },
    {
      "id": "f15",
      "claim": "구로병원 실증은 2025-06-18~29 평일·주말에 약제부(지하 2층)에서 응급실(1층)까지 두 층을 오가는 경로로 진행됐고, 승강기 가동률은 평일 진료 시간(09:00~17:00)에 가장 높고 야간·주말에는 50% 미만이었다.",
      "tag": "사실",
      "source_ids": [
        "ref-943"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "기간 2025-06-18~29, 경로 B2F 약제부 → 1F 응급실, EOR 평일 09–17시 최고·야간·주말 50% 미만. 로봇·승강기 속도는 보고 없음",
      "as_of": "2026-03-31",
      "site_type": "병원",
      "flow_item": "제약"
    },
    {
      "id": "f16",
      "claim": "연계 대상: 오픈소스 무선 업데이트 관리자 Mender 의 상태 스크립트는 다운로드·설치·재부팅·확정(commit)·롤백 같은 상태의 앞(Enter)·뒤(Leave)에서 실행되며, 반환값 0 은 진행, 1 은 중단·롤백, 21 은 설정한 간격 뒤 다시 실행(나중에 재시도)을 뜻하고, 재시도 총 시간 상한과 실행당 시간 상한을 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1371"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "반환값 21 = retry later(StateScriptRetryIntervalSeconds 뒤 재호출), 상한 StateScriptRetryTimeoutSeconds·StateScriptTimeoutSeconds. 사용자 확인을 기다리는 Download_Enter 예시가 있고, 다운로드는 Sync 뒤 24시간에 만료 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f17",
      "claim": "연계 대상: Mender 는 상태 스크립트 오류나 업데이트 모듈 실패 시 롤백하고 롤백된 배포를 항상 실패로 표시하며 스크립트 오류 출력을 포함한 로그를 서버로 올리지만, 상태 스크립트가 바꾼 영구 데이터는 되돌리지 않으므로 설치 전 백업·확정 시 삭제·롤백 시 복원을 스크립트로 두게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1371"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "롤백된 배포는 항상 failed, 로그 업로드(stderr 스크립트당 10 KiB 상한). 영구 변경은 ArtifactInstall_Enter 백업 → ArtifactCommit_Enter 삭제 → ArtifactRollback_Enter 복원 권고. 스크립트는 정전 재실행에 대비해 멱등이어야 함 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f18",
      "claim": "연계 대상: Mender 는 상용판(Enterprise·Professional)의 단계적 배포(phased rollout)가 배포를 시간차 단계로 나눠 단계별 장치 비율(예 5%→15%→나머지, 단계 사이 24시간)을 정하고 오류 증가가 보이면 대부분의 장치에 닿기 전에 중단할 수 있게 한다고 밝힌다.",
      "tag": "추정",
      "source_ids": [
        "ref-1372"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 단계 수(보통 3~4)·단계별 비율·단계 간 지연(보통 2일)을 정할 수 있고 업데이트 실패·오류율 증가 시 중단 가능. 중단 절차 세부는 글에 없음(2020-01-28 블로그)",
      "as_of": "2020-01-28",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f19",
      "claim": "Mender 의 '나중에 재시도' 반환값(f16)과 단계적 배포(f18)를 쓰면 로봇이 작업 중일 때 설치·재부팅을 미루고 일부 장치부터 배포할 수 있을 것으로 보이나, 확인한 자료는 로봇 작업 상태와 연동한 배포 시점·중단 기준을 다루지 않아 그 판단(작업 중 여부·충전 대기 여부 확인과 순서 결정)은 ROP 가 직접 정해야 하고 oq-213 은 열린 채로 남는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1371",
        "ref-1372"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "상태 스크립트 문서는 '장치가 유휴일 때까지 대기' 예시를 두지 않음. 로봇 관제 제품의 공개 배포 절차는 이번 검색에서 찾지 못함",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "W3C Trace Context(권고안, 2021-11-23)는 traceparent(버전·trace-id·parent-id·trace-flags)와 tracestate 헤더로 추적 문맥을 전달하는 형식을 HTTP 에 대해 정하고, 다른 통신 프로토콜에도 관련이 있다고 보면서 그 직렬화는 확장·외부 명세에 맡긴다.",
      "tag": "사실",
      "source_ids": [
        "ref-1373"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "2020-02-06 권고안의 편집 개정판. 5절: \"While trace context is defined for HTTP, the authors acknowledge it is also relevant for other communication protocols.\"",
      "as_of": "2021-11-23",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "Bédard·Lajoie·Beltrame·Dagenais 는 ros2_tracing 을 확장해 분산 ROS 2 시스템의 메시지 흐름을 분석·시각화하는 방법을 내놓았고, 입력·출력 메시지 사이의 일대다·다대다 인과 관계를 추적 데이터로 찾으며 간접 인과는 사용자 주석으로 잡고, 합성·실제 로봇 시스템에서 낮은 실행 부담을 보였다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1375"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Robotics and Autonomous Systems 161:104361. 직접 인과는 같은 구독 콜백·스레드에서 나간 출력으로 추론, 타이머 등 비동기는 사용자 추적점 주석 필요. 초록은 부담 수치를 밝히지 않음(초록 기준)",
      "as_of": "2023-01",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "W3C Trace Context 는 ROS 2·DDS 메시지용 표준 직렬화를 두지 않으므로(f20), 로봇 기록과 플랫폼 추적을 잇는 방법은 메시지에 추적 문맥 필드를 넣는 방식(ros-opentelemetry)과 필드 없이 추적 데이터에서 인과를 추론하는 방식(메시지 흐름 분석) 두 갈래로 보이며, 이종 제조사 로그까지 하나의 작업 식별자로 이은 표준·공개 사례는 이번에도 찾지 못했다(oq-210 부분 근거).",
      "tag": "추정",
      "source_ids": [
        "ref-1373",
        "ref-1038",
        "ref-1375"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f20·f21 과 기존 ref-1038(추적 문맥을 사용자 정의 메시지 필드로 전달, 이번 실행에서 다시 열지 않음)에서 도출",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f23",
      "claim": "Lumpp·Panato·Bombieri·Fummi(2024)는 ROS 기반 로봇 소프트웨어를 Docker 로 컨테이너화하고 Kubernetes(K3s)로 엣지–클라우드에 배치하면서 배포 전에 기능·비기능 제약을 검사하는 설계 흐름을 제안해 RB-Kairos 이동 로봇의 산업용 생산 라인 임무에 적용했고, 로봇 하드웨어 부하를 줄이면서 성능·네트워크 부담은 작았다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1376"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "기관 저장소 서지 페이지(초록) 기준: 다영역 구성요소 조기 검증, 작업→컨테이너 대응, 엣지–클라우드 군집 배치, 배포 전 제약 검사. 'industrial agile production chain' 이 실제 공장인지 실험실인지와 수치는 페이지에 없음",
      "as_of": "2024",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "Open-RMF 웹 API 서버(rmf-web api-server)는 데이터베이스 스키마 변경을 aerich 이행 도구로 처리해, 모델(예 TaskState)에 필드를 더한 뒤 이행 파일 생성(migrate)·적용(upgrade)·서버 재시작 순서를 거치게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-762"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README 'Database Migration' 절: aerich 는 TortoiseORM 용 이행 도구이며 init·init-db 뒤 aerich migrate 로 이행 파일을 만들고 aerich upgrade 로 적용한 다음 api-server 를 재시작 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-762",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf-web — packages/api-server/README.md",
      "published": null,
      "url": "https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 웹 API 서버의 설정·DB 지원·인증·권한·DB 이행(aerich) 절차를 설명하는 README.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-766",
      "org": "국가법령정보센터(개인정보보호위원회 고시)",
      "title": "개인정보의 안전성 확보조치 기준",
      "published": null,
      "url": "https://www.law.go.kr/admRulLsInfoP.do?chrClsCd=010202&admRulSeq=2100000229672",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 2023-6호 판 고시로 접속기록 보관·점검 의무를 정한다. 이번 실행에서 법령 사이트 연결 오류로 다시 열지 못했다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-943",
      "org": "Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health)",
      "title": "Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments",
      "published": "2026-03-31",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "혼잡한 병원에서 승강기 이용을 고려한 자율 약품 배송 로봇 실증. 이번에 분석 대상 건수·실패 건수·수행 자원·경로를 다시 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1036",
      "org": "OpenTelemetry (CNCF)",
      "title": "Specification Status Summary",
      "published": null,
      "url": "https://opentelemetry.io/docs/specs/status/",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "OpenTelemetry 신호별(추적·지표·로그·배기지·프로파일) API·SDK·프로토콜 안정성 상태 요약.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1037",
      "org": "OpenTelemetry (open-telemetry/semantic-conventions-genai)",
      "title": "semantic-conventions-genai/docs/gen-ai/gen-ai-token-metrics.md",
      "published": null,
      "url": "https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "생성형 AI 클라이언트 토큰 사용량 카운터와 호출별 토큰 히스토그램을 정의하는 의미 규약 문서(개발 단계).",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/docs/gen-ai/gen-ai-token-metrics.md",
      "source_unopened": false
    },
    {
      "id": "ref-1038",
      "org": "szobov (GitHub)",
      "title": "ros-opentelemetry — ROS2 x OpenTelemetry README",
      "published": null,
      "url": "https://github.com/szobov/ros-opentelemetry",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. ROS 2 메시지의 사용자 정의 필드로 추적 문맥을 전달해 분산 추적을 제공하는 오픈소스 라이브러리. 이번 실행에서 다시 열지 않았다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1367",
      "org": "바이라인네트워크 (곽중희)",
      "title": "개인정보위, 인터넷망 일률 차단제도 개선 “위험기반 보호로 전환”",
      "published": "2025-10-31",
      "url": "https://byline.network/2025/10/31-281/",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "개인정보보호위원회 자료를 인용해 2025-10-31 시행된 안전성 확보조치 기준 개정(위험기반 망 차단, 접속기록 대상 확대, 일부 조항 1년 유예)을 전한 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1313",
      "org": "European Commission (AI Act Service Desk)",
      "title": "Article 19: Automatically Generated Logs",
      "published": null,
      "url": "https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-19",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "EU AI Act 제19조 원문과 요약. 고위험 AI 제공자의 자동 생성 로그 6개월 이상 보관 의무. 2026-07-27 기준 EUR-Lex 통합본 반영.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1314",
      "org": "European Commission (AI Act Service Desk)",
      "title": "Article 26: Obligations of Deployers of High-Risk AI Systems",
      "published": null,
      "url": "https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "EU AI Act 제26조 원문과 요약. 고위험 AI 배포자의 운영 감시·통보 의무와 로그 6개월 이상 보관 의무.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1370",
      "org": "Hunton Andrews Kurth (Privacy & Cybersecurity Law Blog)",
      "title": "EU Digital Omnibus on AI Enters into Force",
      "published": "2026-07-28",
      "url": "https://www.hunton.com/privacy-and-cybersecurity-law-blog/eu-digital-omnibus-on-ai-enters-into-force",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "AI 디지털 옴니버스 규정(EU 2026/1744)의 발효(2026-07-27)와 고위험 AI 의무 적용일 연기(부속서 III 2027-12-02, 부속서 I 2028-08-02)를 정리한 로펌 글.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1371",
      "org": "Northern.tech (Mender documentation)",
      "title": "State scripts",
      "published": null,
      "url": "https://docs.mender.io/artifact-creation/state-scripts",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "Mender 클라이언트가 업데이트 상태 전이마다 실행하는 상태 스크립트의 종류, 반환값(진행·롤백·나중에 재시도), 시간 상한, 롤백 동작을 설명하는 공식 문서.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1372",
      "org": "Northern.tech (Mender blog, Farshad Tavakoli)",
      "title": "Managing fleets of connected devices with Phased Rollout",
      "published": "2020-01-28",
      "url": "https://mender.io/blog/managing-fleets-of-connected-devices-with-phased-rollout",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "Mender 상용판의 단계적 배포 기능(단계 수·비율·지연 설정, 문제 시 중단)을 소개하는 벤더 블로그.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1373",
      "org": "W3C",
      "title": "Trace Context",
      "published": "2021-11-23",
      "url": "https://www.w3.org/TR/trace-context/",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "분산 추적 문맥을 traceparent·tracestate 헤더로 전달하는 형식을 정한 W3C 권고안(HTTP 기준, 다른 프로토콜은 확장에 위임).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1374",
      "org": "OpenTelemetry (CNCF)",
      "title": "Moved: Generative AI semantic conventions",
      "published": null,
      "url": "https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-metrics/",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "생성형 AI 의미 규약이 별도 저장소(semantic-conventions-genai)로 옮겨져 이 페이지는 더 이상 관리하지 않는다는 이동 안내 페이지.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1375",
      "org": "Bédard, C., Lajoie, P.-Y., Beltrame, G., & Dagenais, M. (Robotics and Autonomous Systems 161, arXiv)",
      "title": "Message Flow Analysis with Complex Causal Links for Distributed ROS 2 Systems",
      "published": "2023-01",
      "url": "https://arxiv.org/abs/2204.10208",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "ros2_tracing 을 확장해 분산 ROS 2 시스템의 메시지 흐름과 일대다·다대다 인과 관계를 추적 데이터로 분석하는 방법. 초록 페이지만 열었다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1376",
      "org": "Lumpp, F., Panato, M., Bombieri, N., & Fummi, F. (Università di Verona IRIS)",
      "title": "A Design Flow based on Docker and Kubernetes for ROS-based Robotic Software Applications",
      "published": "2024",
      "url": "https://iris.univr.it/handle/11562/1092207",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "ROS 기반 로봇 소프트웨어를 Docker·Kubernetes(K3s)로 컨테이너화·배치하고 배포 전 제약을 검사하는 설계 흐름. 기관 저장소 서지 페이지(초록)만 열었다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md",
      "sections": [
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11"
      ],
      "rationale": "갱신(차등): 섹션 5 — 병원 사례 수행 자원(f14)·제약(f15) 행 채움, 성공률 분모 불일치 재확인(f12·f13, 87.03% 는 저자 보고로 유지) / 섹션 6(주제 페이지 요약) — 배포: 상태 스크립트 재시도·롤백(f16·f17)·단계적 배포(f18, 벤더 주장 병기)·작업 상태와 연동한 배포 시점 판단(f19)·배포 전 제약 검사 설계 흐름(f23)·DB 스키마 이행(f24), 관찰: 추적 문맥 표준(f20)·메시지 흐름 인과 분석(f21)·두 방식 비교(f22) / 섹션 7(주제 페이지 요약) — OpenTelemetry 상태 재확인(f1), 생성형 AI 의미 규약 저장소 이동(f2)·토큰 지표 현재 이름·용도(f3·f4), W3C Trace Context(f20), Mender 상태 스크립트(f16·f17), rmf-web aerich 이행(f24) / 섹션 8 — Bédard 외 메시지 흐름 분석(f21), Lumpp 외 설계 흐름(f23) / 섹션 9 — 국내 보존 근거의 개정 상황(f6·f7), EU AI Act 제공자·배포자 로그 보관(f8~f11)은 연계 대상으로 / 섹션 10 — 59. 법·규제·보험·라이선스 연결(f8~f11), 58. 다사업자 책임·계약·데이터 연결(f11) / 섹션 11 — oq-210(f22)·oq-212(f5)·oq-213(f19)·oq-214(f7)·oq-215(f13)·oq-316(f11) 부분 근거, 새 질문 3건. 다음 실행 후보: 59. 법·규제·보험·라이선스(f8~f11), 53. 개인정보·영상 데이터(f6·f7), 57. 자산·소프트웨어 수명주기 관리(f16~f19)."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "추적 문맥",
      "term_en": "Trace Context (W3C traceparent / tracestate)",
      "definition": "분산 추적에서 요청이 여러 서비스를 거칠 때 같은 추적에 속함을 알리도록 trace-id·parent-id·플래그를 traceparent·tracestate 로 전달하는 W3C 표준 형식이다."
    },
    {
      "term_ko": "단계적 배포",
      "term_en": "Phased Rollout (Staged Rollout)",
      "definition": "소프트웨어 업데이트를 장치 일부부터 시간차를 두고 여러 단계로 넓혀 배포하고, 문제가 보이면 나머지 단계를 멈추는 배포 방식이다."
    },
    {
      "term_ko": "상태 스크립트",
      "term_en": "State Script (Mender)",
      "definition": "무선 업데이트 관리자 Mender 가 다운로드·설치·재부팅·확정·롤백 같은 업데이트 상태 전후에 실행하는 스크립트로, 반환값으로 진행·롤백·나중에 재시도를 정한다."
    }
  ],
  "open_questions_new": [
    "2025-10-31 개정으로 접속기록 보관 대상이 개인정보처리시스템에 접속한 모든 자로 넓어졌다면, 로봇·플랫폼 서비스가 쓰는 기계 계정의 개인정보처리시스템 접속도 접속기록 보관·점검 대상에 들어가는가? | 관련 영역: 43. 데이터·관측성·배포, 53. 개인정보·영상 데이터 | 근거: f6 | 종류: 일반",
    "로봇 플랫폼 사업자와 현장 운영자가 각각 EU AI Act 의 제공자·배포자가 될 때 실행 기록의 통제권과 6개월 이상 보관 책임을 계약으로 나눈 공개 사례나 지침이 있는가? | 관련 영역: 43. 데이터·관측성·배포, 58. 다사업자 책임·계약·데이터, 59. 법·규제·보험·라이선스 | 근거: f11 | 종류: 일반",
    "W3C Trace Context 의 추적 문맥을 ROS 2·DDS 메시지나 VDA 5050 같은 MQTT 기반 로봇–관제 메시지에 싣는 공식 직렬화 규약이 있는가? | 관련 영역: 43. 데이터·관측성·배포, 21. 상호운용 표준·적합성 | 근거: f20 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 16,
    "cross_checked_count": 0,
    "unverified": [
      "f6·f7: 2025 개정 고시 번호, 제8조 현행 문구, 유예 종료일 미확인(국가법령정보센터 연결 오류·404, 개인정보위 원문 보도자료 미발견, 근거는 기사 1건)",
      "f10: AI 디지털 옴니버스 적용일은 로펌 글 1건 기준이며 EUR-Lex 원문 미열람",
      "f12·f13: 87.03% 의 분모는 원문에 설명이 없어 미확인(oq-215 미해결)",
      "f21: 메시지 흐름 분석의 실행 부담 수치와 다중 호스트·다중 로봇 실험 여부는 초록만 읽어 미확인",
      "f23: Lumpp 외 적용 환경이 실제 공장인지 실험실인지, DOI(10.1145/3594539 여부)와 수치 미확인 — site_type 을 null 로 둠",
      "ref-1038 은 이번 실행에서 다시 열지 않음",
      "oq-211·oq-297·oq-300 근거 없음(검색했으나 공식 자료 없음 또는 미조사)",
      "섹션 5 제조 공장·상업 시설·가정·실외 사례는 이번에도 찾지 못함"
    ],
    "scope_violations": [
      "f8~f11: EU AI Act 로그 보관 의무는 59. 법·규제·보험·라이선스 쪽 내용이므로 claim 을 '연계 대상: '으로 시작하고 이 영역에는 보관 정책의 외부 근거로만 씀",
      "f16~f18: Mender 는 로봇·장치 운영체제의 무선 업데이트 도구로 로봇 제조사 쪽 연계 대상이며, ROP 몫은 배포 시점·순서 판단(f19)으로 한정",
      "f6·f7: 접속기록 보관 대상 범위 판단은 53. 개인정보·영상 데이터와 함께 다뤄야 함",
      "f21·f22: ROS 2 내부 메시지 흐름 추적은 로봇 소프트웨어 쪽 기법이므로 관찰 방법 근거로만 쓴다"
    ],
    "budget_used": {
      "queries": 17,
      "sources": 10
    },
    "limits": "web_fetch_available: true · fetch_mode full. 검색 17회/30, 신규 출처 10건/15(ref-1367~ref-1376, 예약 구간 안). 재사용 6건(ref-762 inbox 원문, ref-943·ref-1036 webfetch 재열람, ref-1037 github_raw 재열람, ref-766·ref-1038 미열람). 갱신(update) 실행이고 정정 요청이 없어 바뀐 출처(OpenTelemetry 상태·생성형 AI 의미 규약)와 약한 절(5·6·7·8·9·11절), 대상 영역 열린 질문만 다뤘다. 열린 질문은 해결 제안 없이 부분 근거만 냈다: oq-210 근거 f20~f22, oq-212 근거 f2~f5, oq-213 근거 f16~f19, oq-214 근거 f6·f7, oq-215 근거 f12·f13, oq-316 근거 f8~f11. 원문 열기 실패: GitHub blob 페이지 403(raw 경로로 대체), 국가법령정보센터 ECONNRESET·404, HAL·dl.ifip.org 봇 차단, 국내 학회 PDF 본문 추출 실패. 교차 확인 0건이며 모든 사실 finding 은 단일 출처라 신뢰도 medium 이하, 기사·로펌 글 근거(f6·f10)는 low. 벤더 문서 근거 f18 은 vendor_claim·추정·'벤더 주장: ' 표시. 현장 유형 사례 finding 은 병원(f12~f15)뿐이고 제조 공장 후보(f23)는 실제 공장 여부를 확인하지 못해 site_type null. 국내 자료는 개인정보 고시 개정 보도(ref-1367)와 국내 병원 실증(ref-943). 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다. L. AI·학습 기술 관련 f3~f5(언어 모델 비용 계측)는 13. 대화형 기능의 신뢰·기반·47. AI·학습·적응과 모델 운영과, f8~f11 은 47. AI·학습·적응과 모델 운영·37. 관제 화면·실행 기록과 함께 연결하도록 제안한다. 용어집에 이미 있는 관측성·오픈텔레메트리·생성형 AI 의미 규약·분산 추적·무선 업데이트·A/B 업데이트·자동 사건 기록은 후보로 내지 않았다. 입력 누락 없음. 우선 지정 질문 없음."
  }
}
```

### runs/2026-10-09-19/verification.json

```json
{
  "run_id": "2026-10-09-19",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 2026-10-09 열람. 추적 API·SDK·프로토콜 안정, 지표 SDK 혼합, 로그 브리지 API 안정, 배기지 프로토콜 N/A, 프로파일 프로토콜 개발 단계로 일치. 페이지에 갱신일 없음(발행일 미확인)."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 제목 'Moved: Generative AI semantic conventions', 이동·관리 중단 안내문 일치. 직접 인용 1회(ref-1374)."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: raw 원문 열람. 카운터 5종·히스토그램 2종 모두 Development, 단위 {token}, 필수 속성 일치. gen_ai.client.token.usage 언급·이름 변경 안내 없음."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 히스토그램은 백분위·이상값용이며 합계·비용 산정에 쓰지 않도록, 캐시·추론 카운터는 입력·출력 카운터의 부분집합이라고 원문이 명시."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지: f2~f4 에서 도출한 운영 판단이며 두 출처 모두 안정 판 일정을 밝히지 않음. oq-212 는 해결이 아니라 부분 근거."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 바이라인네트워크 2025-10-31(곽중희) 기사 열람. 2025-10-31 시행, 접속기록 대상을 '개인정보처리시스템에 접속한 모든 자(정보주체 제외)'로 확대, 제2조·제6조의2 즉시 시행, 내부 관리계획·접근권한·접근통제·접속기록 보관·점검 조항 1년 유예 일치. 고시 번호 없음. 단일 기사(신뢰도 low)이므로 '보도에 따르면' 귀속 표현을 유지해야 [사실] 유지 가능. 검색 결과(nepla.ai 요약)가 즉시 시행·유예 범위를 같게 전하지만 독립 1차 자료가 아니어서 교차 확인으로 세지 않음."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지: ref-766(원문 미열람, 2023-6호)과 ref-1367 비교 추론. 유예 종료일·개정 고시 번호·제8조 현행 문구는 미확인으로 남겨야 함. oq-214 부분 근거."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: AI Act Service Desk 제19조 페이지 열람. 제1항(제12조 제1항 로그, 통제 범위, 적어도 6개월, EU·회원국 법 우선)·제2항(금융기관) 일치. 페이지가 2026-07-27 통합본 기준임을 명시. 직접 인용 1회. '연계 대상' 표기 적절."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 제26조 제5항(사용 설명서 기반 감시, 위험 시 제공자·유통자·시장감시당국 통보와 사용 중단), 제6항(통제 범위 로그 적어도 6개월 보관) 일치."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인: Hunton 글 열람. 규정 2026/1744, 관보 게재 3일 뒤 2026-07-27 발효, 부속서 III 2027-12-02, 부속서 I 2028-08-02 일치. 교차 확인: 검증 검색 결과(White & Case, Cooley, Cloud Security Alliance 등 독립 기관)가 같은 번호·발효일·적용일을 전함(검색 결과 일치, 원문 미열람). 다만 열람한 Hunton 페이지에서 발행일 2026-07-28 을 확인하지 못함 → 발행일 미확인 처리 지시. EUR-Lex 원문 미열람."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지: f8~f10 에서 도출. 로봇 플랫폼의 고위험 해당 여부·부속서 I/III 귀속은 출처가 다루지 않음. 검색 결과는 부속서 I 에 기계류가 포함된다고 전함. oq-316 부분 근거."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: PMC 본문 열람. 요청 135건, 긴급 13건 제외, 적격 122건(평일 80·주말 42), 실패 14건, 3.4절 완료 108건, 87.03% 분모 서술 없음 일치."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지: 108/122≈88.5% 산술 비교. 87.03% 는 '저자 보고'로 두고 oq-215 는 열린 채로 둔다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: DOGU IROI(Level 3+), 직원 전용·병원 내 물류용 승강기 TK Elevator TK50M, 단일 로봇 운영 일치. 다만 원문은 승강기 대수를 밝히지 않으므로 '승강기 1대'의 대수 표현은 삭제 지시(수정 후 [사실] 유지)."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 2025-06-18~29, B2F 약제부 → 1F 응급실, 승강기 가동률 평일 09~17시 최고·야간·주말 50% 미만 일치. 주의: 원문 다른 곳에 'four-week' 시험 기간 표현이 있어 2주 기간과 원문 내부에서 맞지 않음."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Mender 상태 스크립트 문서 열람. Enter/Leave, 반환값 0 진행·1 중단·롤백·21 나중에 재시도, StateScriptRetryIntervalSeconds·RetryTimeoutSeconds·TimeoutSeconds, Download_Enter 사용자 확인 예시, Sync 후 24시간 만료 일치. '연계 대상' 표기 적절."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 롤백된 배포는 항상 실패 표시, stderr 스크립트당 10 KiB 로그 업로드, 스크립트의 영구 변경은 되돌리지 않음과 백업(ArtifactInstall_Enter)·삭제(ArtifactCommit_Enter)·복원(ArtifactRollback_Enter) 권고, 멱등성 요구 일치."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Farshad Tavakoli 2020-01-28 블로그. Enterprise·Professional 의 단계적 배포, 5%→15%→나머지·24시간 간격 예시, 보통 3~4단계·약 2일 간격, 실패·오류율 증가 시 중단 가능 일치. vendor_claim·[추정]·'벤더 주장' 표시 적절."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지: 문서에 '장치 유휴 시까지 대기' 예시가 없음을 확인(사용자 확인 대기 예시만 있음). 배포 시점 판단을 ROP 몫으로 한정한 범위 서술 적절. oq-213 부분 근거."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: W3C 권고안 2021-11-23(2020-02-06 권고안의 편집 개정), traceparent 네 필드·tracestate, HTTP 외 프로토콜 직렬화는 확장·외부 명세에 맡김 일치. 직접 인용 1회."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 초록 열람. 저자·제목, 일대다·다대다 인과, 사용자 주석 기반 간접 인과, 합성·실제 로봇 시스템에서 낮은 실행 부담 일치. 서지 정보는 Robotics and Autonomous Systems 161:104361, 2023-03 으로 표시되어 브리프의 발행일 2023-01 과 다름 → 정정 지시."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지: f20·f21 과 기존 ref-1038(이번 실행 원문 미열람) 에서 도출. oq-210 부분 근거."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: IRIS 서지 페이지 열람. Docker·Kubernetes 컨테이너화·엣지–클라우드 군집 배치, 배포 전 기능·비기능 제약 검증, Robotnik RB-Kairos, 로봇 하드웨어 부하 감소·성능·네트워크 부담 최소 일치. 다만 K3s 는 키워드로만 표시되고 초록 본문에 없으며, 적용 대상은 'industrial agile production chain' 으로 '생산 라인'과 표현이 다름 → 문구 수정 지시. 학술지명·DOI 미확인."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문(data/source_texts/ref-762.txt) 'Database Migration' 절에서 aerich(TortoiseORM 이행 도구), init·init-db, TaskState 필드 추가, aerich migrate·upgrade, api-server 재시작 순서 일치. 원문은 PostgreSQL 기준 개발 예시임."
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
      "f1 은 기존 페이지 7절(주제 페이지 2026-09-30-area43-s7)의 OpenTelemetry 상태 서술과 같은 내용의 재확인이다 — 새 각주 없이 ref-1036 을 재사용하고 확인일만 갱신한다",
      "f12·f13 은 기존 5절 병원 사례와 oq-215 의 내용과 겹친다 — 기존 문장(87.03% 저자 보고)을 유지하고 근거만 보강한다",
      "새 열린 질문 2(EU AI Act 로그 보관 책임의 계약 배분)는 oq-316 과, 새 열린 질문 3(추적 문맥의 ROS 2·DDS·MQTT 직렬화)은 oq-210 과 일부 겹치나 묻는 대상(계약 사례, 직렬화 규약)이 달라 중복으로 보지 않는다",
      "f16·f17(Mender 상태 스크립트)은 기존 ref-1040(Mender README) 의 A/B 롤백 서술과 이어지며 57. 자산·소프트웨어 수명주기 관리와 겹칠 수 있다 — 이 영역에서는 연계 대상으로만 둔다"
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
    "f14: 5절 병원 사례 '수행 자원' 행에서 승강기의 대수 표현('1대')을 빼고 '직원 전용 승강기(TK Elevator TK50M)'로 쓴다 — 원문은 승강기 대수를 밝히지 않는다. 로봇 1대(DOGU IROI, Level 3+로 소개)·단일 로봇 운영은 [사실][^ref-943]로 유지한다.",
    "f21·ref-1375: 발행일을 2023-01 에서 2023-03 으로 고친다(각주와 reference_updates 의 published 모두) — arXiv 서지 정보가 Robotics and Autonomous Systems 161:104361, 2023-03 으로 표시한다.",
    "f10·ref-1370: 각주의 발행일을 '미확인'으로 쓰고(reference_updates 의 published 는 null) 본문 기준일은 접근일 2026-10-09 로 둔다 — 열람한 Hunton 페이지에서 발행일 2026-07-28 이 확인되지 않았다(관보 게재 2026-07-24·발효 2026-07-27 은 확인).",
    "f23: 'Kubernetes(K3s)'를 'Kubernetes'로, '산업용 생산 라인 임무'를 '산업용 애자일 생산 체인(industrial agile production chain) 임무'로 고치고, 이 연구는 5절 적용 사례가 아니라 6절(주제 페이지 요약)·8절에만 쓴다 — K3s 는 서지 페이지 키워드에만 있고 적용 환경이 실제 공장인지 확인되지 않았다.",
    "f6·f7: 9절에서 개정 내용은 '바이라인네트워크 보도(2025-10-31)에 따르면'으로 출처를 밝혀 쓰고, 개정 고시 번호·제8조 현행 문구·유예 종료일은 '미확인'으로 남긴다 — 근거가 기사 1건이고 고시 원문을 열지 못했다. 기존 문장 '2023-09-22 시행 판 고시 기준(현행 조문 미확인)'은 유지하고 f7 은 [추정]으로 둔다.",
    "f8~f11: 9절에서는 '연계 대상'으로 한두 문장만 쓰고(EU AI Act 의 제공자·배포자 로그 보관 의무를 보존 정책의 외부 근거로), 상세는 10절에서 59. 법·규제·보험·라이선스, 58. 다사업자 책임·계약·데이터, 47. AI·학습·적응과 모델 운영, 37. 관제 화면·실행 기록 으로 연결한다 — 법규 해석은 59. 법·규제·보험·라이선스 의 내용이다.",
    "f16~f18: Mender 상태 스크립트·단계적 배포는 '연계 대상'(로봇·장치 운영체제 업데이트 도구)으로 쓰고 f18 은 [추정]에 '벤더 주장'을 병기한다. ROP 직접 몫은 f19 의 배포 시점·순서 판단으로 한정한다.",
    "ref-766·ref-1038: 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 두 항목에 source_unopened: true 를 넣는다 — 이번 실행에서 두 출처 모두 원문을 열지 않았다.",
    "7절(주제 페이지 요약): OpenTelemetry 상태(f1)·생성형 AI 의미 규약(f2~f4) 행은 '2026-10-09 확인 기준'으로 기준일을 갱신하고, 토큰 지표는 개발(Development) 단계이며 gen_ai.client.token.usage 에 대한 이름 변경·폐기 안내가 현재 문서에 없다는 점만 쓴다 — 옛 이름의 존재·폐기 여부는 확인되지 않았다.",
    "열린 질문: oq-210·oq-212·oq-213·oq-214·oq-215·oq-316 은 해결로 바꾸지 않고 부분 근거(f22·f5·f19·f7·f13·f11)만 덧붙인다 — 답이 되는 [사실] finding 이 없다. 5절의 87.03% 는 '저자 보고' 표기를 유지한다.",
    "f15: 5절 '제약' 행에 기간·경로·승강기 가동률 패턴을 [사실][^ref-943]로 쓰되, 로봇·승강기 속도는 '미확인'으로 둔다(원문 보고 없음)."
  ],
  "confidence": "low",
  "verification_note": "판정: 조건부 승인. 확인 24건, 미확인 0건, 교차 확인 1건(f10: AI 디지털 옴니버스 규정 번호·발효일·적용일, 독립 로펌·기관 검색 결과 일치). 강등: 없음. 원문 미열람 출처: ref-766, ref-1038. 주의: 새 [사실] 주장은 모두 단일 출처이며, 국내 개인정보 고시 개정(f6)은 기사 1건 기준이고 개정 고시 번호·제8조 현행 문구·유예 종료일은 미확인이다. EU AI Act 적용일(f10)은 로펌 글과 검색 결과 기준이며 관보 원문은 열지 않았다. 구로병원 실증의 성공률 87.03% 는 분모가 원문에 없어 저자 보고 수치로 남고(oq-215), 원문 안에 2주 실시 기간과 '4주' 표현이 함께 있다. 승강기 대수는 원문에 없어 지웠다. 정정 요청 없음. 열린 질문 해결 인정 없음(oq-210·oq-212·oq-213·oq-214·oq-215·oq-316 부분 근거만). 검증 메모: ref-762 는 fetched_via 가 github_raw 로 적혔으나 자체 점검에는 inbox 원문으로 적혀 있고 입력 원문 텍스트로 확인했다. webfetch 출처들은 fetch_url 이 비어 있으나 검증 에이전트가 각 URL 을 직접 열어 확인했다. 검증 검색 2회(리서치 17회와 합쳐 19/30).",
  "retry_reason": null
}
```

### runs/2026-10-09-19/pages.json

```json
{
  "run_id": "2026-10-09-19",
  "outline": [
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 1900,
      "summary": "구로병원 약품 배송 실증 사례의 수행 자원(DOGU IROI 1대, 직원 전용 승강기 TK50M, 단일 로봇 운영)과 제약(2025-06-18~29, 지하 2층 약제부→1층 응급실, 승강기 가동률 패턴)을 채웠다. [사실][^ref-943] 성공률 87.03% 는 분모가 원문에 없어 저자 보고 수치로 둔다. [추정][^ref-943]",
      "planned_findings": [
        "f12",
        "f13",
        "f14",
        "f15"
      ]
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 2400,
      "summary": "배포 쪽 새 근거는 대부분 장치 운영체제 업데이트 도구(연계 대상)이며, ROP 직접 몫은 로봇 작업 상태에 맞춘 배포 시점·순서 판단으로 보인다. [추정][^ref-1371][^ref-1372] 기록 잇기는 메시지 필드 방식과 인과 추론 방식 두 갈래로 보인다. [추정][^ref-1373][^ref-1375]",
      "planned_findings": [
        "f16",
        "f17",
        "f18",
        "f19",
        "f20",
        "f21",
        "f22",
        "f23",
        "f24"
      ]
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 1500,
      "summary": "2026-09-30 주제 페이지의 표 행은 2026-09-30 확인 기준이고, OpenTelemetry 명세 상태와 생성형 AI 의미 규약 행은 2026-10-09 확인 항목으로 갱신된다. [사실][^ref-1036][^ref-1374][^ref-1037]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f5"
      ]
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 450,
      "summary": "ROS 2 메시지 흐름 인과 분석(Bédard 외, 2023-03)과 Docker·Kubernetes 기반 배포 전 제약 검사 설계 흐름(Lumpp 외, 2024)을 더했다. [사실][^ref-1375][^ref-1376]",
      "planned_findings": [
        "f21",
        "f23"
      ]
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 1100,
      "summary": "보도에 따르면 2025-10-31 시행 개정으로 접속기록 보관 대상이 넓어졌으나 현행 조문은 미확인이고, EU AI Act 의 제공자·배포자 로그 보관 의무는 연계 대상의 외부 근거로만 둔다. [사실][^ref-1367][^ref-1313][^ref-1314]",
      "planned_findings": [
        "f6",
        "f7",
        "f8",
        "f9",
        "f19"
      ]
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 1200,
      "summary": "로그 보관 의무는 59. 법·규제·보험·라이선스와 58. 다사업자 책임·계약·데이터로, 배포 시점 판단은 57. 자산·소프트웨어 수명주기 관리로, 추적 문맥 직렬화는 21. 상호운용 표준·적합성으로 이어진다. [추정][^ref-1313][^ref-1314][^ref-1371][^ref-1373]",
      "planned_findings": [
        "f6",
        "f8",
        "f9",
        "f10",
        "f11",
        "f16",
        "f19",
        "f20",
        "f22"
      ]
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md",
      "section": "11. 열린 질문",
      "budget_chars": 1400,
      "summary": "oq-210·oq-212·oq-213·oq-214·oq-215·oq-316 에 부분 근거만 더했고 해결된 질문은 없으며, 새 질문 3건을 올렸다. [추정][^ref-1373][^ref-1037][^ref-1371][^ref-1367][^ref-943][^ref-1313]",
      "planned_findings": [
        "f5",
        "f7",
        "f11",
        "f13",
        "f19",
        "f22"
      ]
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md",
      "section": "13. 참고 자료 (각주)",
      "budget_chars": 0,
      "summary": "각주 정의만 둔다. 새 출처 10건을 더하고 재사용 출처의 접근일과 원문 미열람 표시를 갱신했다."
    }
  ],
  "pages": [
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "5절 병원 사례 수행 자원·제약 행 채움과 성공률 분모 재확인, 6·7·8·9·10·11절에 2026-10-09 갱신 소절(Mender 상태 스크립트·단계적 배포(벤더 주장)·배포 시점 판단, W3C Trace Context·메시지 흐름 인과 분석, OpenTelemetry 상태·생성형 AI 토큰 지표 재확인, 개인정보 고시 개정 보도·EU AI Act 로그 보관 연계, 열린 질문 부분 근거와 새 질문 3건), 13절 각주 갱신. 2차 수정: 6·7·10·11절 갱신 소절에 2026-09-30 주제 페이지 링크 복원, 7절 기준일 문구 명확화",
      "patches": [
        {
          "section": "5. 적용 사례 (현장 유형 명시)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-09-19/pages/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md 의 해당 절을 본다)"
        },
        {
          "section": "6. 대표 접근법과 기술",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-09-19/pages/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md 의 해당 절을 본다)"
        },
        {
          "section": "7. 관련 표준·프레임워크·오픈소스",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-09-19/pages/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md 의 해당 절을 본다)"
        },
        {
          "section": "8. 대표 연구와 자료",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-09-19/pages/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md 의 해당 절을 본다)"
        },
        {
          "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-09-19/pages/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md 의 해당 절을 본다)"
        },
        {
          "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-09-19/pages/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md 의 해당 절을 본다)"
        },
        {
          "section": "11. 열린 질문",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-09-19/pages/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md 의 해당 절을 본다)"
        },
        {
          "section": "13. 참고 자료 (각주)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-09-19/pages/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md 의 해당 절을 본다)",
          "frontmatter": {
            "related_areas": [
              3,
              13,
              21,
              22,
              34,
              37,
              38,
              39,
              41,
              42,
              44,
              47,
              52,
              53,
              54,
              57,
              58,
              59,
              61,
              63
            ],
            "sources": [
              "ref-762",
              "ref-1032",
              "ref-1033",
              "ref-1034",
              "ref-1035",
              "ref-1036",
              "ref-1037",
              "ref-1038",
              "ref-1039",
              "ref-1040",
              "ref-766",
              "ref-1041",
              "ref-1042",
              "ref-943",
              "ref-1043",
              "ref-1044",
              "ref-1367",
              "ref-1313",
              "ref-1314",
              "ref-1370",
              "ref-1371",
              "ref-1372",
              "ref-1373",
              "ref-1374",
              "ref-1375",
              "ref-1376"
            ],
            "last_run": "2026-10-09"
          }
        }
      ]
    },
    {
      "path": "docs/topics/2026/2026-10-09-area43-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 43. 데이터·관측성·배포 의 \"6. 대표 접근법과 기술\" 절(2,358자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-09-area43-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 43. 데이터·관측성·배포 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,654자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-09-area43-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 43. 데이터·관측성·배포 의 \"11. 열린 질문\" 절(1,457자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-09-area43-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 43. 데이터·관측성·배포 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(1,426자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-09-area43-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 43. 데이터·관측성·배포 의 \"8. 대표 연구와 자료\" 절(1,079자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-10-09 | 43. 데이터·관측성·배포 | 5·6·7·8·9·10·11·13절 차등 갱신: 병원 사례 수행 자원·제약 채움과 성공률 분모 재확인, Mender 상태 스크립트·단계적 배포(벤더 주장)·배포 시점 판단, W3C Trace Context·메시지 흐름 인과 분석, OpenTelemetry 상태·생성형 AI 토큰 지표 재확인, 개인정보 고시 개정 보도·EU AI Act 로그 보관 연계, 열린 질문 부분 근거 6건과 새 질문 3건(2차 수정: 6·7·10·11절 이전 주제 페이지 링크 복원, 7절 기준일 문구 명확화, 표준 목록 이름의 규정 번호 삭제) | run 2026-10-09-19",
  "index_updates": {
    "home_recent": "2026-10-09 — 43. 데이터·관측성·배포: 병원 사례 보강, 배포 시점 판단·추적 문맥 잇기·생성형 AI 토큰 지표 재확인, 접속기록 개정 보도와 EU AI Act 로그 보관 연계, 새 열린 질문 3건",
    "category_recent": "2026-10-09 — 43. 데이터·관측성·배포: 5~11절 차등 갱신(구로병원 수행 자원·제약, Mender 상태 스크립트·단계적 배포(벤더 주장), W3C Trace Context·ROS 2 메시지 흐름 분석, OpenTelemetry 상태 재확인, 국내 고시 개정 보도·EU AI Act 제19·26조 연계)",
    "area_recent": "2026-10-09 — 43. 데이터·관측성·배포: 5절 병원 사례 수행 자원·제약 행 채움, 6·7·8·9·10·11절에 2026-10-09 갱신 소절 추가(2026-09-30 주제 페이지 링크 유지), 13절 각주 갱신(새 출처 10건)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "trace-context",
      "term_ko": "추적 문맥",
      "term_en": "Trace Context (W3C traceparent / tracestate)",
      "definition": "분산 추적에서 요청이 여러 서비스를 거칠 때 같은 추적에 속함을 알리도록 trace-id·parent-id·플래그를 traceparent·tracestate 로 전달하는 W3C 표준 형식이다.",
      "description": "W3C 권고안(2021-11-23)은 HTTP 에 대한 형식을 정하고, 다른 통신 프로토콜의 직렬화는 확장·외부 명세에 맡긴다.",
      "related_areas": [
        43,
        38,
        21
      ],
      "sources": [
        "ref-1373"
      ]
    },
    {
      "action": "new",
      "slug": "phased-rollout",
      "term_ko": "단계적 배포",
      "term_en": "Phased Rollout (Staged Rollout)",
      "definition": "소프트웨어 업데이트를 장치 일부부터 시간차를 두고 여러 단계로 넓혀 배포하고, 문제가 보이면 나머지 단계를 멈추는 배포 방식이다.",
      "description": "Mender 상용판은 단계별 장치 비율과 단계 간 지연을 정할 수 있다고 밝힌다(벤더 주장).",
      "related_areas": [
        43,
        57
      ],
      "sources": [
        "ref-1372"
      ]
    },
    {
      "action": "new",
      "slug": "state-script",
      "term_ko": "상태 스크립트",
      "term_en": "State Script (Mender)",
      "definition": "무선 업데이트 관리자 Mender 가 다운로드·설치·재부팅·확정·롤백 같은 업데이트 상태 전후에 실행하는 스크립트로, 반환값으로 진행·롤백·나중에 재시도를 정한다.",
      "related_areas": [
        43,
        57
      ],
      "sources": [
        "ref-1371"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-762",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf-web — packages/api-server/README.md",
      "published": null,
      "url": "https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 웹 API 서버의 설정·DB 지원·인증·권한·DB 이행(aerich) 절차를 설명하는 README.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-766",
      "org": "국가법령정보센터(개인정보보호위원회 고시)",
      "title": "개인정보의 안전성 확보조치 기준",
      "published": null,
      "url": "https://www.law.go.kr/admRulLsInfoP.do?chrClsCd=010202&admRulSeq=2100000229672",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 2023-6호 판 고시로 접속기록 보관·점검 의무를 정한다. 이번 실행에서 법령 사이트 연결 오류로 다시 열지 못했다.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-943",
      "org": "Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health)",
      "title": "Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments",
      "published": "2026-03-31",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "혼잡한 병원에서 승강기 이용을 고려한 자율 약품 배송 로봇 실증. 이번에 분석 대상 건수·실패 건수·수행 자원·경로를 다시 확인했다.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1036",
      "org": "OpenTelemetry (CNCF)",
      "title": "Specification Status Summary",
      "published": null,
      "url": "https://opentelemetry.io/docs/specs/status/",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "OpenTelemetry 신호별(추적·지표·로그·배기지·프로파일) API·SDK·프로토콜 안정성 상태 요약.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1037",
      "org": "OpenTelemetry (open-telemetry/semantic-conventions-genai)",
      "title": "semantic-conventions-genai/docs/gen-ai/gen-ai-token-metrics.md",
      "published": null,
      "url": "https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "생성형 AI 클라이언트 토큰 사용량 카운터와 호출별 토큰 히스토그램을 정의하는 의미 규약 문서(개발 단계).",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1038",
      "org": "szobov (GitHub)",
      "title": "ros-opentelemetry — ROS2 x OpenTelemetry README",
      "published": null,
      "url": "https://github.com/szobov/ros-opentelemetry",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. ROS 2 메시지의 사용자 정의 필드로 추적 문맥을 전달해 분산 추적을 제공하는 오픈소스 라이브러리. 이번 실행에서 다시 열지 않았다.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1367",
      "org": "바이라인네트워크 (곽중희)",
      "title": "개인정보위, 인터넷망 일률 차단제도 개선 “위험기반 보호로 전환”",
      "published": "2025-10-31",
      "url": "https://byline.network/2025/10/31-281/",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "개인정보보호위원회 자료를 인용해 2025-10-31 시행된 안전성 확보조치 기준 개정(위험기반 망 차단, 접속기록 대상 확대, 일부 조항 1년 유예)을 전한 기사.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1313",
      "org": "European Commission (AI Act Service Desk)",
      "title": "Article 19: Automatically Generated Logs",
      "published": null,
      "url": "https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-19",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "EU AI Act 제19조 원문과 요약. 고위험 AI 제공자의 자동 생성 로그 6개월 이상 보관 의무. 2026-07-27 기준 EUR-Lex 통합본 반영.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1314",
      "org": "European Commission (AI Act Service Desk)",
      "title": "Article 26: Obligations of Deployers of High-Risk AI Systems",
      "published": null,
      "url": "https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "EU AI Act 제26조 원문과 요약. 고위험 AI 배포자의 운영 감시·통보 의무와 로그 6개월 이상 보관 의무.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1370",
      "org": "Hunton Andrews Kurth (Privacy & Cybersecurity Law Blog)",
      "title": "EU Digital Omnibus on AI Enters into Force",
      "published": null,
      "url": "https://www.hunton.com/privacy-and-cybersecurity-law-blog/eu-digital-omnibus-on-ai-enters-into-force",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "AI 디지털 옴니버스 규정(EU 2026/1744)의 발효(2026-07-27)와 고위험 AI 의무 적용일 연기(부속서 III 2027-12-02, 부속서 I 2028-08-02)를 정리한 로펌 글. 열람 페이지에서 발행일은 확인하지 못했다.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1371",
      "org": "Northern.tech (Mender documentation)",
      "title": "State scripts",
      "published": null,
      "url": "https://docs.mender.io/artifact-creation/state-scripts",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "Mender 클라이언트가 업데이트 상태 전이마다 실행하는 상태 스크립트의 종류, 반환값(진행·롤백·나중에 재시도), 시간 상한, 롤백 동작을 설명하는 공식 문서.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1372",
      "org": "Northern.tech (Mender blog, Farshad Tavakoli)",
      "title": "Managing fleets of connected devices with Phased Rollout",
      "published": "2020-01-28",
      "url": "https://mender.io/blog/managing-fleets-of-connected-devices-with-phased-rollout",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "Mender 상용판의 단계적 배포 기능(단계 수·비율·지연 설정, 문제 시 중단)을 소개하는 벤더 블로그.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1373",
      "org": "W3C",
      "title": "Trace Context",
      "published": "2021-11-23",
      "url": "https://www.w3.org/TR/trace-context/",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "분산 추적 문맥을 traceparent·tracestate 헤더로 전달하는 형식을 정한 W3C 권고안(HTTP 기준, 다른 프로토콜은 확장에 위임).",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1374",
      "org": "OpenTelemetry (CNCF)",
      "title": "Moved: Generative AI semantic conventions",
      "published": null,
      "url": "https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-metrics/",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "생성형 AI 의미 규약이 별도 저장소(semantic-conventions-genai)로 옮겨져 이 페이지는 더 이상 관리하지 않는다는 이동 안내 페이지.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1375",
      "org": "Bédard, C., Lajoie, P.-Y., Beltrame, G., & Dagenais, M. (Robotics and Autonomous Systems 161, arXiv)",
      "title": "Message Flow Analysis with Complex Causal Links for Distributed ROS 2 Systems",
      "published": "2023-03",
      "url": "https://arxiv.org/abs/2204.10208",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "ros2_tracing 을 확장해 분산 ROS 2 시스템의 메시지 흐름과 일대다·다대다 인과 관계를 추적 데이터로 분석하는 방법. 초록 페이지만 열었다.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1376",
      "org": "Lumpp, F., Panato, M., Bombieri, N., & Fummi, F. (Università di Verona IRIS)",
      "title": "A Design Flow based on Docker and Kubernetes for ROS-based Robotic Software Applications",
      "published": "2024",
      "url": "https://iris.univr.it/handle/11562/1092207",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "ROS 기반 로봇 소프트웨어를 Docker·Kubernetes 로 컨테이너화·배치하고 배포 전 제약을 검사하는 설계 흐름. 기관 저장소 서지 페이지(초록)만 열었다.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ],
      "source_unopened": false
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "2025-10-31 개정으로 접속기록 보관 대상이 개인정보처리시스템에 접속한 모든 자로 넓어졌다면, 로봇·플랫폼 서비스가 쓰는 기계 계정의 개인정보처리시스템 접속도 접속기록 보관·점검 대상에 들어가는가?",
      "areas": [
        43,
        53
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "로봇 플랫폼 사업자와 현장 운영자가 각각 EU AI Act 의 제공자·배포자가 될 때 실행 기록의 통제권과 6개월 이상 보관 책임을 계약으로 나눈 공개 사례나 지침이 있는가?",
      "areas": [
        43,
        58,
        59
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "W3C Trace Context 의 추적 문맥을 ROS 2·DDS 메시지나 VDA 5050 같은 MQTT 기반 로봇–관제 메시지에 싣는 공식 직렬화 규약이 있는가?",
      "areas": [
        43,
        21
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md#5-적용-사례-현장-유형-명시",
      "title": "43. 데이터·관측성·배포"
    },
    {
      "site_type": "병원",
      "item": "제약",
      "link": "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md#5-적용-사례-현장-유형-명시",
      "title": "43. 데이터·관측성·배포"
    },
    {
      "site_type": "병원",
      "item": "예외·성과",
      "link": "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md#5-적용-사례-현장-유형-명시",
      "title": "43. 데이터·관측성·배포"
    }
  ],
  "additional_research_requests": [
    "9절·11절(oq-214): 2025-10-31 시행 「개인정보의 안전성 확보조치 기준」 개정 고시 번호, 제8조 현행 문구, 1년 유예 종료일을 국가법령정보센터 또는 개인정보보호위원회 원문으로 확인해야 한다 — 현재 근거가 기사 1건(ref-1367)뿐이다.",
    "10절(oq-316): AI 디지털 옴니버스 규정(Regulation (EU) 2026/1744)의 적용일을 EUR-Lex 관보 원문으로 확인해야 한다 — 현재는 로펌 글(ref-1370, 발행일 미확인)과 검색 결과 기준이다.",
    "표준 목록·10절: EU AI Act 본 규정의 공식 규정 번호를 브리프 출처로 확인해야 표준 목록 이름에 넣을 수 있다 — 2차 검증 지시로 이번 표준 목록 항목 이름에서 규정 번호를 뺐다.",
    "5절(oq-215): 구로병원 실증 논문의 성공률 87.03% 분모와, 검증 메모가 지적한 실시 기간 표기(2025-06-18~29 와 원문 다른 곳의 'four-week' 표현) 불일치를 저자 문의·정정본 등으로 확인해야 한다 — 기간 불일치는 브리프 finding 이 아니라 본문에 넣지 않았다.",
    "5절: 제조 공장·상업 시설·가정·실외 현장의 데이터 수집·관측성·배포 적용 사례가 여전히 없다. Lumpp 외(ref-1376)의 적용 환경(실제 공장 여부)·학술지명·DOI 를 본문으로 확인하면 제조 공장 사례 후보가 될 수 있다.",
    "6절·8절: Bédard 외(ref-1375) 메시지 흐름 분석의 실행 부담 수치와 다중 호스트·다중 로봇 실험 여부를 본문으로 확인해야 한다(초록만 열람).",
    "6절·11절(oq-210): ref-1038(ros-opentelemetry)을 이번 실행에서 다시 열지 못했으므로 추적 문맥 필드 방식의 현재 상태를 재확인해야 한다.",
    "pipeline 담당: 자동 분리가 절 안의 이전 주제 페이지 링크 줄('자세한 내용은 주제 페이지 …')을 지우는지 확인해야 한다 — 2차 검증 지시에 따라 이번에는 각 갱신 소절 첫머리에 '2026-09-30 까지 정리한 내용은 …에 있다' 링크 문장을 넣었다."
  ],
  "fixes_applied": [
    "f14: 승강기 대수 삭제 — 5절 병원 사례 '수행 자원' 행을 'DOGU IROI 배송 로봇 1대와 … 직원 전용 승강기(TK Elevator TK50M)'로 쓰고 승강기의 '1대' 표현을 뺐으며, 로봇 1대(Level 3+로 소개)·단일 로봇 운영은 [사실][^ref-943]로 유지했다.",
    "f21·ref-1375: 발행일 정정 — 13절 각주와 8절 본문의 발행일을 2023-03 으로 쓰고 reference_updates 의 published 를 \"2023-03\" 으로 넣었다.",
    "f10·ref-1370: 발행일 미확인 처리 — 13절 각주의 발행일을 '미확인'으로, reference_updates 의 published 를 null 로 두고, 10절 본문에 '발행일 미확인, 2026-10-09 확인'으로 기준일을 적었다.",
    "f23: 문구 수정 — 6·8절에서 'Kubernetes(K3s)'를 'Kubernetes'로, '산업용 생산 라인 임무'를 '산업용 애자일 생산 체인(industrial agile production chain) 임무'로 고쳤고, 5절 적용 사례에는 넣지 않고 5절 끝에 적용 사례로 쓰지 않는 이유만 적었다.",
    "f6·f7: 9절 갱신 소절에서 개정 내용을 '바이라인네트워크 보도(2025-10-31)에 따르면'으로 시작해 [사실][^ref-1367]로 쓰고 개정 고시 번호·제8조 현행 문구·유예 종료일을 '미확인'으로 남겼으며, 기존 '2023-09-22 시행 판 고시 기준(현행 조문 미확인)' 문장은 그대로 두고 f7 은 [추정]으로 썼다.",
    "f8~f11: 9절에는 '연계 대상:'으로 시작하는 두 문장만 두어 제공자·배포자 로그 보관 의무를 보존 정책의 외부 근거로 썼고, 상세(f8·f9·f10 [사실], f11 [추정])는 10절에서 59. 법·규제·보험·라이선스, 58. 다사업자 책임·계약·데이터, 47. AI·학습·적응과 모델 운영, 37. 관제 화면·실행 기록으로 연결했다.",
    "f16~f18: 6절에서 Mender 상태 스크립트·단계적 배포 항목을 모두 '연계 대상:'으로 시작했고 f18 은 '[추정] 벤더 주장[^ref-1372]'로 썼으며, ROP 직접 몫은 6절·9절에서 f19 의 배포 시점·순서 판단으로만 한정했다.",
    "ref-766·ref-1038: 13절 각주의 접근일 뒤에 ' (원문 미열람)'을 붙였고 reference_updates 두 항목에 source_unopened: true 를 넣었다.",
    "7절: OpenTelemetry 상태(f1)·생성형 AI 의미 규약(f2~f4) 항목을 '2026-10-09 확인 기준'으로 기준일을 갱신하고 7절 요약 문장에도 기준일 갱신을 밝혔으며, 토큰 지표는 개발 단계이고 gen_ai.client.token.usage 에 대한 이름 변경·폐기 안내가 현재 문서에 없다는 점만 쓰고 그 이름을 '옛 이름'이라 부르거나 폐기 여부를 단정하지 않았다.",
    "열린 질문: 11절에서 oq-210·oq-212·oq-213·oq-214·oq-215·oq-316 을 상태 '열림' 그대로 두고 부분 근거(f22·f5·f19·f7·f13·f11)만 [추정]으로 덧붙였으며 open_question_updates 에 해결 항목을 내지 않았고, 5절의 87.03% 는 '저자 보고' 표기를 유지했다.",
    "f15: 5절 '제약' 행에 기간·경로·승강기 가동률 패턴을 [사실][^ref-943]로 쓰고 '로봇·승강기 속도는 미확인(원문 보고 없음)'을 덧붙였다.",
    "2차: 6·7·10·11절 링크 연속성 — 각 절의 2026-10-09 갱신 소절 제목 바로 아래 첫 문장으로 '2026-09-30 까지 정리한 내용(연결·질문)은 [43. 데이터·관측성·배포 — … (2026-09-30)](../../topics/2026/2026-09-30-area43-s6·s7·s10·s11.md)에 있다' 링크 문장을 넣어, 자동 분리 뒤에도 새 주제 페이지 3절에 이전 주제 페이지 링크가 남게 했다.",
    "2차: 7절 문구 — 첫 문단을 '2026-09-30 주제 페이지 [43. 데이터·관측성·배포 — 관련 표준·프레임워크·오픈소스 (2026-09-30)](…2026-09-30-area43-s7.md)의 표 행은 2026-09-30 확인 기준이며, 그 가운데 OpenTelemetry 명세 상태와 생성형 AI 의미 규약 행은 이번 실행의 2026-10-09 확인 항목으로 갱신된다'로 고쳐 '아래'를 빼고 어느 주제 페이지의 행인지 밝혔고, 갱신 소절 첫머리에도 같은 뜻을 적었다.",
    "2차: standards_updates 의 EU AI Act 항목 — name 을 'EU AI Act 제19조 자동 생성 로그 (Article 19)'로 바꿔 브리프 밖의 규정 번호를 뺐고, 규정 번호 확인은 additional_research_requests 로 넘겼다.",
    "분량 초과 자동 분리: 43. 데이터·관측성·배포 본문 11,693자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 4,444자"
  ],
  "standards_updates": [
    {
      "name": "W3C Trace Context (traceparent·tracestate, 권고안 2021-11-23)",
      "kind": "표준",
      "org": "W3C",
      "url": "https://www.w3.org/TR/trace-context/",
      "related_areas": [
        43,
        38,
        21
      ],
      "summary": "분산 추적 문맥을 traceparent·tracestate 헤더로 전달하는 형식을 HTTP 에 대해 정한 W3C 권고안이다. 다른 통신 프로토콜의 직렬화는 확장·외부 명세에 맡긴다.",
      "ref_id": "ref-1373"
    },
    {
      "name": "EU AI Act 제19조 자동 생성 로그 (Article 19)",
      "kind": "프레임워크",
      "org": "European Union (유럽위원회 AI Act Service Desk 게재)",
      "url": "https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-19",
      "related_areas": [
        43,
        59,
        47
      ],
      "summary": "고위험 AI 시스템 제공자가 자기 통제 아래 있는 자동 생성 로그를 의도된 목적에 맞는 기간, 적어도 6개월 보관하게 하는 조항이다(2026-07-27 기준 통합본).",
      "ref_id": "ref-1313"
    }
  ]
}
```

### runs/2026-10-09-19/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md (8개 절)
- 분량 초과 자동 분리:
    - docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-10-09-area43-s6.md (2,358자)
    - docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-10-09-area43-s7.md (1,654자)
    - docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md "11. 열린 질문" → docs/topics/2026/2026-10-09-area43-s11.md (1,457자)
    - docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-10-09-area43-s10.md (1,426자)
    - docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md "8. 대표 연구와 자료" → docs/topics/2026/2026-10-09-area43-s8.md (1,079자)
```

### runs/2026-10-09-19/pages/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md

```markdown
---
title: "43. 데이터·관측성·배포"
type: area
category: "K. 플랫폼 아키텍처·인프라"
area_no: 43
related_areas: [3, 13, 21, 22, 34, 37, 38, 39, 41, 42, 44, 47, 52, 53, 54, 57, 58, 59, 61, 63]
tags: [관측성, OpenTelemetry, MCAP, 무선 업데이트, FinOps]
status: draft
confidence: low
created: 2026-09-28
updated: 2026-10-09
sources: [ref-762, ref-1032, ref-1033, ref-1034, ref-1035, ref-1036, ref-1037, ref-1038, ref-1039, ref-1040, ref-766, ref-1041, ref-1042, ref-943, ref-1043, ref-1044, ref-1367, ref-1313, ref-1314, ref-1370, ref-1371, ref-1372, ref-1373, ref-1374, ref-1375, ref-1376]
last_run: 2026-10-09
version: 3
---

[홈](../../index.md) › [K. 플랫폼 아키텍처·인프라](index.md) › 43. 데이터·관측성·배포

# 43. 데이터·관측성·배포

!!! info "소속 대분류"
    [K. 플랫폼 아키텍처·인프라](index.md) — 핵심 질문:
    플랫폼을 어디에 어떻게 두어야 끊김·확장·다현장 조건에서도 계속 동작하는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: low · 페이지 버전: 2 · 마지막 갱신: 2026-09-30 · 마지막 실행: 2026-09-30
<!-- auto:page-status:end -->

## 1. 한 줄 정의

데이터 수집·보존, 플랫폼 관측성, 배포 자동화, 운영 비용 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **데이터 수집·저장·보존**: 로그·이벤트·텔레메트리를 수집·저장하고 보존 기간을 정한다
- **플랫폼 관측성**: 플랫폼 서비스 자체의 상태·오류·성능을 추적한다
- **배포·업데이트 자동화**: 플랫폼 소프트웨어를 현장과 클라우드에 배포하고 되돌린다
- **운영 비용 관리**: 클라우드와 언어 모델 호출 비용을 측정하고 관리한다

## 2. 핵심 질문

플랫폼 자체의 상태·데이터·배포·비용을 어떻게 관리할 것인가? [분류원문]

## 3. 왜 중요한가

공개 자료를 종합하면 플랫폼 자체의 상태·데이터·배포·비용을 관리해야 하는 까닭은 기록의 한계, 관찰의 부담, 실패 원인 분석, 언어 모델 호출 비용, 기록 보관 의무 다섯 가지로 모인다. [추정][^ref-1032][^ref-1033][^ref-943][^ref-1043][^ref-766]

자세한 내용은 주제 페이지 [43. 데이터·관측성·배포 — 왜 중요한가](../../topics/2026/2026-09-30-area43-s3.md)에 있다.

## 4. 핵심 개념과 용어

용어는 기록·관찰·배포·비용 순서로 둔다.

자세한 내용은 주제 페이지 [43. 데이터·관측성·배포 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area43-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이번 조사에서 확인한 적용 사례는 병원의 운영 기록 기반 실패 분석과 물류창고의 배포 전 시뮬레이션 검증(벤더 주장) 두 건이다.

**현장 유형:** 병원

**사례:** 병원에서 약품 배송 로봇의 실패 원인을 로봇·승강기 기록으로 분석

| 항목 | 내용 |
|---|---|
| 시작 조건 | 응급실 직원이 웹 애플리케이션으로 요청하면 배송 임무가 시작됐다. [사실][^ref-943] |
| 작업 대상 | 로봇이 옮겨 넘기는 약품. [사실][^ref-943] |
| 수행 자원 | Level 3+로 소개된 DOGU IROI 배송 로봇 1대와 병원 내 물류에 주로 쓰는 직원 전용 승강기(TK Elevator TK50M)가 맡았고, 단일 로봇 운영을 대상으로 했다. [사실][^ref-943] |
| 제약 | 2025-06-18~29 평일·주말에 약제부(지하 2층)에서 응급실(1층)까지 두 층을 오가는 경로였고, 승강기 가동률은 평일 진료 시간(09:00~17:00)에 가장 높고 야간·주말에는 50% 미만이었다. [사실][^ref-943] 로봇·승강기 속도는 미확인(원문 보고 없음). |
| 완료·인계 | 로봇이 사람 개입 없이 전체 경로를 마치고 약품을 인계하는 것을 배송 성공으로 정의했다. [사실][^ref-943] |
| 예외·성과 | 로봇 시스템 로그(1 Hz)·승강기 통신 로그·관찰자 기록지를 함께 모아 실패 원인을 분석했고, 승강기 가동률이 높을수록 실패가 많았다(저자 보고: 전체 성공률 87.03%, 실패 14건). [사실][^ref-943] |

고려대학교 구로병원은 2025-06-18~29 비응급 배송 임무 122건으로 자율 약품 배송 로봇을 실증했다(2026-03-31 발표). [사실][^ref-943] 로봇 시스템 로그는 승강기 호출·탑승·문 동작·하차 시각을 1 Hz 로 남겼고, 승강기 통신 로그는 승강기 상태·문·위치·로봇 명령을, 관찰자 기록지는 탑승객·화물·결과를 담았다. [사실][^ref-943]

저자 보고에 따르면 [승강기 가동률](../../glossary/elevator-operating-rate.md)(Elevator Operating Rate, EOR) 59% 미만일 때 성공률은 95.52% 였고, 실패 14건은 승강기 막힘 8건·복도 주행 4건·통신 오류 2건이었다. [사실][^ref-943] 서로 다른 주체가 낸 기록을 함께 모으는 수집·결합이 이 사례에서 이 영역이 맡는 부분으로 보인다. [추정][^ref-943]

2026-10-09 에 원문을 다시 확인하면, 저자들은 배송 요청 135건에서 긴급 13건을 빼고 122건(평일 80·주말 42)을 분석 대상으로 삼았고, 실패 14건을 보고하며 완료 시행 108건을 따로 분석하지만 전체 성공률 87.03% 의 분모는 밝히지 않는다. [사실][^ref-943] 122건 중 성공 108건이면 약 88.5% 가 되어 87.03% 와 맞지 않으므로, 87.03% 는 저자 보고 수치로 두고 분모 문제는 11. 열린 질문의 oq-215 로 남긴다. [추정][^ref-943]

**현장 유형:** 물류창고

**사례:** 물류창고에서 로봇 교통 관리·오케스트레이션 알고리즘 변경을 적용 전에 시뮬레이션으로 검증

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인(이번 조사에서 확인하지 못함) |
| 작업 대상 | 미확인(이번 조사에서 확인하지 못함) |
| 수행 자원 | 미확인(이번 조사에서 확인하지 못함) |
| 제약 | 미확인(이번 조사에서 확인하지 못함) |
| 완료·인계 | 미확인(이번 조사에서 확인하지 못함) |
| 예외·성과 | 알고리즘과 운영 변경을 실제 창고에 적용하기 전에 시뮬레이션·디지털 트윈에서 시험하고, 12개월 동안 창고 운영 270년 분량을 시뮬레이션했다고 밝힌다. [추정] 벤더 주장[^ref-1044] |

Ocado 는 초당 10회 로봇 통신 같은 실제 운영 데이터로 시뮬레이션 모델을 다듬는다고 밝힌다(2025-06-04). [추정] 벤더 주장[^ref-1044] 이 사례는 배포 전 검증의 근거로만 쓰며, 시뮬레이션 자체는 [34. 시뮬레이션·예측용 디지털 트윈](../design-and-simulation/simulation-and-predictive-digital-twin.md)(가정한 미래를 실험)의 내용이다.

제조 공장·상업 시설·가정·실외 현장의 데이터·관측성·배포 사례는 이번 조사에서 찾지 못했다. 다중 로봇 컨테이너 오케스트레이션 연구와 서비스 로봇 언어 모델 계획 연구는 실험실·평가 실험이므로 적용 사례로 쓰지 않고 6. 대표 접근법과 기술에서 다룬다. 2026-10-09 에 더한 Lumpp 외(2024)의 컨테이너 기반 배포 설계 흐름도 적용 환경이 실제 공장인지 확인되지 않아 적용 사례로 쓰지 않고 6. 대표 접근법과 기술과 8. 대표 연구와 자료에서만 다룬다.

## 6. 대표 접근법과 기술

공개 자료를 종합하면 플랫폼 자체의 관리는 자기 기술형 기록 형식과 기록 DB(데이터), OpenTelemetry 기반 플랫폼 관찰과 저부하 로봇 내부 추적(상태), 컨테이너 자동 재시작·이미지 기반 A/B 롤백·배포 전 시뮬레이션 검증(배포), 표준 청구 데이터와 토큰 지표를 쓰는 FinOps 주기(비용)의 조합으로 보인다. [추정][^ref-1034][^ref-762][^ref-1032][^ref-1033][^ref-1036][^ref-1038][^ref-1039][^ref-1040][^ref-1037][^ref-1041][^ref-1042]

자세한 내용은 주제 페이지 [43. 데이터·관측성·배포 — 대표 접근법과 기술](../../topics/2026/2026-10-09-area43-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역의 도구는 기록(rosbag2·MCAP), 관찰(OpenTelemetry·ros2_tracing), 배포(K3s·Mender), 비용(FinOps·FOCUS)으로 나뉜다.

자세한 내용은 주제 페이지 [43. 데이터·관측성·배포 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-09-area43-s7.md)에 있다.

## 8. 대표 연구와 자료

아래 다섯 건이 이 영역의 대표 자료이며, 실행 추적·관찰 부담·배포 복원력·호출 비용·현장 기록 분석을 각각 보여 준다.

자세한 내용은 주제 페이지 [43. 데이터·관측성·배포 — 대표 연구와 자료](../../topics/2026/2026-10-09-area43-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

공개 자료를 종합하면 ROP 가 직접 맡을 범위는 플랫폼 서비스의 로그·지표·추적 수집과 보존 정책, 작업 단위 추적 문맥 전파와 로봇 기록(MCAP 등)의 수집·색인 인터페이스, 플랫폼 구성 요소의 배포·롤백·버전 기록과 배포 전 검증, 클라우드·언어 모델 호출 비용의 계측·배분으로 보인다. [추정][^ref-1036][^ref-766][^ref-1034][^ref-1038][^ref-943][^ref-1039][^ref-1044][^ref-1037][^ref-1042] 이 가운데 보존 정책의 국내 근거는 2023-09-22 시행 판 고시 기준(현행 조문 미확인)이고, 배포 전 검증의 사례 근거는 벤더 주장이다. [추정][^ref-766][^ref-1044]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 로봇이 내는 기록·업데이트 상태를 받아 작업 단위로 모으고 색인하는 인터페이스 [추정][^ref-1032][^ref-1040] | 연계 대상: 로봇 운영체제·펌웨어 무선 업데이트, 로봇 내부 ROS 2 실행 추적 [추정][^ref-1032][^ref-1040] |
| 시설·설비 제어 | 승강기 통신 로그를 로봇 기록과 함께 받아 결합 [추정][^ref-943] | 연계 대상: 승강기 통신 로그 생성과 설비 제어 [추정][^ref-943] |

클라우드 청구 데이터를 만드는 일은 클라우드 사업자의 몫이며, ROP 는 그 데이터를 받아 모으는 쪽을 맡을 것으로 보인다. [추정][^ref-1042] 경계의 기준은 [범위 경계](../../about/scope-boundary.md)에 있다.

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

### 2026-10-09 갱신: 보존 근거의 개정 상황과 배포 시점

보존 정책의 국내 근거는 위의 2023-09-22 시행 판 고시 기준(현행 조문 미확인)을 유지하고, 개정 상황을 아래처럼 덧붙인다.

- 바이라인네트워크 보도(2025-10-31)에 따르면 2025-10-31 시행된 「개인정보의 안전성 확보조치 기준」 개정은 접속기록 보관 대상을 개인정보취급자에서 개인정보처리시스템에 접속한 모든 자(정보주체 제외)로 넓혔고, 정의·인터넷망 차단 조항은 즉시 시행하되 내부 관리계획·접근권한·접근통제·접속기록 보관·점검 관련 조항에는 1년 유예를 두었다. [사실][^ref-1367] 개정 고시 번호, 제8조 현행 문구, 유예 종료일은 미확인이다.
- 이 보도대로라면 2023-6호 기준(1년·2년 이상 보관, 월 1회 이상 점검)은 현행 조문과 다를 수 있으므로, 로봇 플랫폼의 접속기록 대상 범위(운영자 계정 외 접속자 포함 여부)를 현행 고시 원문으로 다시 확인해야 할 것으로 보인다(oq-214). [추정][^ref-1367][^ref-766]
- 연계 대상: EU AI Act 제19조와 제26조는 고위험 AI 시스템의 제공자와 배포자에게 각자 통제하는 자동 생성 로그를 적어도 6개월 보관하게 한다(2026-07-27 기준 통합본, 2026-10-09 확인). [사실][^ref-1313][^ref-1314] 이 의무는 실행 기록 보존 정책의 외부 근거로만 두고, 법규 해석과 보관 책임 배분은 10. 다른 연구영역과의 연결에서 해당 영역으로 잇는다.
- 배포에서 ROP 가 직접 맡는 것은 로봇 작업 상태에 맞춘 배포 시점·순서 판단이고, 로봇·장치 운영체제의 업데이트 설치·롤백 실행은 연계 대상으로 보인다. [추정][^ref-1371][^ref-1372]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 기록을 쓰는 관제·분석 영역, 배포·검증 영역, 비용·규제 영역, 언어 모델 영역, 적용 현장과 이어진다.

자세한 내용은 주제 페이지 [43. 데이터·관측성·배포 — 다른 연구영역과의 연결](../../topics/2026/2026-10-09-area43-s10.md)에 있다.

## 11. 열린 질문

아래 질문은 이번 실행에서 새로 올렸다. 번호는 퍼블리셔가 부여하며 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [43. 데이터·관측성·배포 — 열린 질문](../../topics/2026/2026-10-09-area43-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [43. 데이터·관측성·배포](data-observability-and-deployment.md) — 섹션 3~11 신규 작성(seed → draft): 기록 형식·관측성·배포·비용 관리 접근법, 병원·물류창고 적용 사례, 책임 경계, 연결 영역 17개, 열린 질문 6건 (실행 2026-09-30-06)
- 2026-09-30 · 생성 · [43. 데이터·관측성·배포 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area43-s6.md) — 자동 분리: 43. 데이터·관측성·배포 의 "6. 대표 접근법과 기술" 절(2,750자)을 옮겼다 (실행 2026-09-30-06)
- 2026-09-30 · 생성 · [43. 데이터·관측성·배포 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area43-s10.md) — 자동 분리: 43. 데이터·관측성·배포 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,115자)을 옮겼다 (실행 2026-09-30-06)
- 2026-09-30 · 생성 · [43. 데이터·관측성·배포 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area43-s7.md) — 자동 분리: 43. 데이터·관측성·배포 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,055자)을 옮겼다 (실행 2026-09-30-06)
- 2026-09-30 · 생성 · [43. 데이터·관측성·배포 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area43-s4.md) — 자동 분리: 43. 데이터·관측성·배포 의 "4. 핵심 개념과 용어" 절(975자)을 옮겼다 (실행 2026-09-30-06)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-762]: Open Robotics (open-rmf), rmf-web — packages/api-server/README.md, 미확인, https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md, 접근일 2026-10-09
[^ref-1032]: Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L, arXiv), ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2, 2022-07, https://arxiv.org/abs/2201.00393, 접근일 2026-09-30
[^ref-1033]: Yu, J., Lee, S., Choi, Y., & Park, K.-J. (arXiv), ros2probe: Non-intrusive, Kernel-selective Observability for Robot Operating System 2 Middleware, 2026-06, https://arxiv.org/abs/2606.10746, 접근일 2026-09-30
[^ref-1034]: Open Robotics (ROS 2 Documentation), Iron Irwini (iron), 2023-05-23, https://docs.ros.org/en/rolling/Releases/Release-Iron-Irwini.html, 접근일 2026-09-30
[^ref-1036]: OpenTelemetry (CNCF), Specification Status Summary, 미확인, https://opentelemetry.io/docs/specs/status/, 접근일 2026-10-09
[^ref-1037]: OpenTelemetry (open-telemetry/semantic-conventions-genai), semantic-conventions-genai/docs/gen-ai/gen-ai-token-metrics.md, 미확인, https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md, 접근일 2026-10-09
[^ref-1038]: szobov (GitHub), ros-opentelemetry — ROS2 x OpenTelemetry README, 미확인, https://github.com/szobov/ros-opentelemetry, 접근일 2026-10-09 (원문 미열람)
[^ref-1039]: Zhang, J., Yu, X., & Westerlund, T. (Sensors 25(16):5067), Enhancing the Resilience of ROS 2-Based Multi-Robot Systems with Kubernetes: A Case Study on UWB-Based Relative Positioning, 2025-08-14, https://pmc.ncbi.nlm.nih.gov/articles/PMC12390455/, 접근일 2026-09-30
[^ref-1040]: Northern.tech (mendersoftware), mender — README, 미확인, https://github.com/mendersoftware/mender, 접근일 2026-09-30
[^ref-766]: 개인정보보호위원회 (국가법령정보센터), 개인정보의 안전성 확보조치 기준 (개인정보보호위원회고시 제2023-6호), 2023-09-22, https://www.law.go.kr/admRulLsInfoP.do?chrClsCd=010202&admRulSeq=2100000229672, 접근일 2026-10-09 (원문 미열람)
[^ref-1041]: FinOps Foundation, FinOps Phases, 미확인, https://www.finops.org/framework/phases/, 접근일 2026-09-30
[^ref-1042]: FinOps Foundation, Introducing FOCUS 1.2: SaaS/PaaS Support, Invoice Reconciliation, and more (발행 기관의 발표 글, 명세 본문 미열람), 2025-06-03, https://www.finops.org/insights/focus-1-2-available/, 접근일 2026-09-30
[^ref-943]: Lee, Y., Kim, S.-E., Kim, J. S. 외 (Digital Health 12), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-10-09
[^ref-1043]: Bruno, L. D. M., Sim, J., & Hagiwara, Y. (arXiv), Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots, 2026-09, https://arxiv.org/abs/2609.29043, 접근일 2026-09-30
[^ref-1044]: Ocado Group, Ocado's digital twins and simulations: driving efficiencies and innovation at scale, 2025-06-04, https://www.ocadogroup.com/newsroom/stories/digital-twins-and-simulations, 접근일 2026-09-30
[^ref-1367]: 바이라인네트워크 (곽중희), 개인정보위, 인터넷망 일률 차단제도 개선 “위험기반 보호로 전환”, 2025-10-31, https://byline.network/2025/10/31-281/, 접근일 2026-10-09
[^ref-1313]: European Commission (AI Act Service Desk), Article 19: Automatically Generated Logs, 미확인, https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-19, 접근일 2026-10-09
[^ref-1314]: European Commission (AI Act Service Desk), Article 26: Obligations of Deployers of High-Risk AI Systems, 미확인, https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26, 접근일 2026-10-09
[^ref-1371]: Northern.tech (Mender documentation), State scripts, 미확인, https://docs.mender.io/artifact-creation/state-scripts, 접근일 2026-10-09
[^ref-1372]: Northern.tech (Mender blog, Farshad Tavakoli), Managing fleets of connected devices with Phased Rollout, 2020-01-28, https://mender.io/blog/managing-fleets-of-connected-devices-with-phased-rollout, 접근일 2026-10-09
```

### docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md

```markdown
---
title: "43. 데이터·관측성·배포"
type: area
category: "K. 플랫폼 아키텍처·인프라"
area_no: 43
related_areas: [3, 13, 22, 34, 37, 38, 39, 41, 42, 44, 47, 52, 53, 54, 57, 61, 63]
tags: [관측성, OpenTelemetry, MCAP, 무선 업데이트, FinOps]
status: published
confidence: low
created: 2026-09-28
updated: 2026-09-30
sources: [ref-762, ref-1032, ref-1033, ref-1034, ref-1035, ref-1036, ref-1037, ref-1038, ref-1039, ref-1040, ref-766, ref-1041, ref-1042, ref-943, ref-1043, ref-1044]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [K. 플랫폼 아키텍처·인프라](index.md) › 43. 데이터·관측성·배포

# 43. 데이터·관측성·배포

!!! info "소속 대분류"
    [K. 플랫폼 아키텍처·인프라](index.md) — 핵심 질문:
    플랫폼을 어디에 어떻게 두어야 끊김·확장·다현장 조건에서도 계속 동작하는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: low · 페이지 버전: 2 · 마지막 갱신: 2026-09-30 · 마지막 실행: 2026-09-30
<!-- auto:page-status:end -->

## 1. 한 줄 정의

데이터 수집·보존, 플랫폼 관측성, 배포 자동화, 운영 비용 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **데이터 수집·저장·보존**: 로그·이벤트·텔레메트리를 수집·저장하고 보존 기간을 정한다
- **플랫폼 관측성**: 플랫폼 서비스 자체의 상태·오류·성능을 추적한다
- **배포·업데이트 자동화**: 플랫폼 소프트웨어를 현장과 클라우드에 배포하고 되돌린다
- **운영 비용 관리**: 클라우드와 언어 모델 호출 비용을 측정하고 관리한다

## 2. 핵심 질문

플랫폼 자체의 상태·데이터·배포·비용을 어떻게 관리할 것인가? [분류원문]

## 3. 왜 중요한가

공개 자료를 종합하면 플랫폼 자체의 상태·데이터·배포·비용을 관리해야 하는 까닭은 기록의 한계, 관찰의 부담, 실패 원인 분석, 언어 모델 호출 비용, 기록 보관 의무 다섯 가지로 모인다. [추정][^ref-1032][^ref-1033][^ref-943][^ref-1043][^ref-766]

자세한 내용은 주제 페이지 [43. 데이터·관측성·배포 — 왜 중요한가](../../topics/2026/2026-09-30-area43-s3.md)에 있다.

## 4. 핵심 개념과 용어

용어는 기록·관찰·배포·비용 순서로 둔다.

자세한 내용은 주제 페이지 [43. 데이터·관측성·배포 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area43-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이번 조사에서 확인한 적용 사례는 병원의 운영 기록 기반 실패 분석과 물류창고의 배포 전 시뮬레이션 검증(벤더 주장) 두 건이다.

**현장 유형:** 병원

**사례:** 병원에서 약품 배송 로봇의 실패 원인을 로봇·승강기 기록으로 분석

| 항목 | 내용 |
|---|---|
| 시작 조건 | 응급실 직원이 웹 애플리케이션으로 요청하면 배송 임무가 시작됐다. [사실][^ref-943] |
| 작업 대상 | 로봇이 옮겨 넘기는 약품. [사실][^ref-943] |
| 수행 자원 | 미확인(이번 조사에서 확인하지 못함) |
| 제약 | 미확인(이번 조사에서 확인하지 못함) |
| 완료·인계 | 로봇이 사람 개입 없이 전체 경로를 마치고 약품을 인계하는 것을 배송 성공으로 정의했다. [사실][^ref-943] |
| 예외·성과 | 로봇 시스템 로그(1 Hz)·승강기 통신 로그·관찰자 기록지를 함께 모아 실패 원인을 분석했고, 승강기 가동률이 높을수록 실패가 많았다(저자 보고: 전체 성공률 87.03%, 실패 14건). [사실][^ref-943] |

고려대학교 구로병원은 2025-06-18~29 비응급 배송 임무 122건으로 자율 약품 배송 로봇을 실증했다(2026-03-31 발표). [사실][^ref-943] 로봇 시스템 로그는 승강기 호출·탑승·문 동작·하차 시각을 1 Hz 로 남겼고, 승강기 통신 로그는 승강기 상태·문·위치·로봇 명령을, 관찰자 기록지는 탑승객·화물·결과를 담았다. [사실][^ref-943]

저자 보고에 따르면 [승강기 가동률](../../glossary/elevator-operating-rate.md)(Elevator Operating Rate, EOR) 59% 미만일 때 성공률은 95.52% 였고, 실패 14건은 승강기 막힘 8건·복도 주행 4건·통신 오류 2건이었다. [사실][^ref-943] 서로 다른 주체가 낸 기록을 함께 모으는 수집·결합이 이 사례에서 이 영역이 맡는 부분으로 보인다. [추정][^ref-943] 성공률과 실패 건수의 분모가 원문 수치 사이에서 맞지 않는 부분은 11. 열린 질문에 올렸다.

**현장 유형:** 물류창고

**사례:** 물류창고에서 로봇 교통 관리·오케스트레이션 알고리즘 변경을 적용 전에 시뮬레이션으로 검증

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인(이번 조사에서 확인하지 못함) |
| 작업 대상 | 미확인(이번 조사에서 확인하지 못함) |
| 수행 자원 | 미확인(이번 조사에서 확인하지 못함) |
| 제약 | 미확인(이번 조사에서 확인하지 못함) |
| 완료·인계 | 미확인(이번 조사에서 확인하지 못함) |
| 예외·성과 | 알고리즘과 운영 변경을 실제 창고에 적용하기 전에 시뮬레이션·디지털 트윈에서 시험하고, 12개월 동안 창고 운영 270년 분량을 시뮬레이션했다고 밝힌다. [추정] 벤더 주장[^ref-1044] |

Ocado 는 초당 10회 로봇 통신 같은 실제 운영 데이터로 시뮬레이션 모델을 다듬는다고 밝힌다(2025-06-04). [추정] 벤더 주장[^ref-1044] 이 사례는 배포 전 검증의 근거로만 쓰며, 시뮬레이션 자체는 [34. 시뮬레이션·예측용 디지털 트윈](../design-and-simulation/simulation-and-predictive-digital-twin.md)(가정한 미래를 실험)의 내용이다.

제조 공장·상업 시설·가정·실외 현장의 데이터·관측성·배포 사례는 이번 조사에서 찾지 못했다. 다중 로봇 컨테이너 오케스트레이션 연구와 서비스 로봇 언어 모델 계획 연구는 실험실·평가 실험이므로 적용 사례로 쓰지 않고 6. 대표 접근법과 기술에서 다룬다.

## 6. 대표 접근법과 기술

공개 자료를 종합하면 플랫폼 자체의 관리는 자기 기술형 기록 형식과 기록 DB(데이터), OpenTelemetry 기반 플랫폼 관찰과 저부하 로봇 내부 추적(상태), 컨테이너 자동 재시작·이미지 기반 A/B 롤백·배포 전 시뮬레이션 검증(배포), 표준 청구 데이터와 토큰 지표를 쓰는 FinOps 주기(비용)의 조합으로 보인다. [추정][^ref-1034][^ref-762][^ref-1032][^ref-1033][^ref-1036][^ref-1038][^ref-1039][^ref-1040][^ref-1037][^ref-1041][^ref-1042]

자세한 내용은 주제 페이지 [43. 데이터·관측성·배포 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area43-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역의 도구는 기록(rosbag2·MCAP), 관찰(OpenTelemetry·ros2_tracing), 배포(K3s·Mender), 비용(FinOps·FOCUS)으로 나뉜다. 모든 행은 2026-09-30 확인 기준이다.

자세한 내용은 주제 페이지 [43. 데이터·관측성·배포 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area43-s7.md)에 있다.

## 8. 대표 연구와 자료

아래 다섯 건이 이 영역의 대표 자료이며, 실행 추적·관찰 부담·배포 복원력·호출 비용·현장 기록 분석을 각각 보여 준다.

- Bédard·Lütkebohle·Dagenais, ros2_tracing(IEEE RA-L, 2022-07) — LTTng 기반 ROS 2 계측·추적 도구 모음으로, 로봇 내부 실행을 낮은 부담으로 기록하는 근거다. [사실][^ref-1032]
- Yu·Lee·Choi·Park, ros2probe(arXiv 프리프린트, 2026-06) — 관찰 도구가 대상을 교란하는 문제를 커널 선택 관찰로 줄인 연구로, 관찰 자체의 비용을 따져야 함을 보여 준다. [사실][^ref-1033]
- Zhang·Yu·Westerlund, Kubernetes 를 이용한 ROS 2 다중 로봇 시스템 복원력 연구(Sensors, 2025-08-14) — 컨테이너 자동 재시작으로 장애 중에도 위치 정확도를 유지한 실험실 결과다. [사실][^ref-1039]
- Bruno·Sim·Hagiwara, 서비스 로봇의 LLM 연쇄 기반 작업 계획(arXiv 프리프린트, 2026-09) — 클라우드 API 비용·지연을 동기로 로컬·클라우드 모델을 비교했다. [사실][^ref-1043]
- Lee 외, 혼잡한 병원에서 승강기 이용을 고려한 자율 약품 배송 로봇 실증(Digital Health, 2026-03-31) — 로봇·승강기 로그와 관찰 기록을 함께 모아 실패를 분석한 국내 현장 자료다. [사실][^ref-943]

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

공개 자료를 종합하면 ROP 가 직접 맡을 범위는 플랫폼 서비스의 로그·지표·추적 수집과 보존 정책, 작업 단위 추적 문맥 전파와 로봇 기록(MCAP 등)의 수집·색인 인터페이스, 플랫폼 구성 요소의 배포·롤백·버전 기록과 배포 전 검증, 클라우드·언어 모델 호출 비용의 계측·배분으로 보인다. [추정][^ref-1036][^ref-766][^ref-1034][^ref-1038][^ref-943][^ref-1039][^ref-1044][^ref-1037][^ref-1042] 이 가운데 보존 정책의 국내 근거는 2023-09-22 시행 판 고시 기준(현행 조문 미확인)이고, 배포 전 검증의 사례 근거는 벤더 주장이다. [추정][^ref-766][^ref-1044]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 로봇이 내는 기록·업데이트 상태를 받아 작업 단위로 모으고 색인하는 인터페이스 [추정][^ref-1032][^ref-1040] | 연계 대상: 로봇 운영체제·펌웨어 무선 업데이트, 로봇 내부 ROS 2 실행 추적 [추정][^ref-1032][^ref-1040] |
| 시설·설비 제어 | 승강기 통신 로그를 로봇 기록과 함께 받아 결합 [추정][^ref-943] | 연계 대상: 승강기 통신 로그 생성과 설비 제어 [추정][^ref-943] |

클라우드 청구 데이터를 만드는 일은 클라우드 사업자의 몫이며, ROP 는 그 데이터를 받아 모으는 쪽을 맡을 것으로 보인다. [추정][^ref-1042] 경계의 기준은 [범위 경계](../../about/scope-boundary.md)에 있다.

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 기록을 쓰는 관제·분석 영역, 배포·검증 영역, 비용·규제 영역, 언어 모델 영역, 적용 현장과 이어진다.

자세한 내용은 주제 페이지 [43. 데이터·관측성·배포 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area43-s10.md)에 있다.

## 11. 열린 질문

아래 질문은 이번 실행에서 새로 올렸다. 번호는 퍼블리셔가 부여하며 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [43. 데이터·관측성·배포 — 열린 질문](../../topics/2026/2026-09-30-area43-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [43. 데이터·관측성·배포](data-observability-and-deployment.md) — 섹션 3~11 신규 작성(seed → draft): 기록 형식·관측성·배포·비용 관리 접근법, 병원·물류창고 적용 사례, 책임 경계, 연결 영역 17개, 열린 질문 6건 (실행 2026-09-30-06)
- 2026-09-30 · 생성 · [43. 데이터·관측성·배포 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area43-s6.md) — 자동 분리: 43. 데이터·관측성·배포 의 "6. 대표 접근법과 기술" 절(2,750자)을 옮겼다 (실행 2026-09-30-06)
- 2026-09-30 · 생성 · [43. 데이터·관측성·배포 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area43-s10.md) — 자동 분리: 43. 데이터·관측성·배포 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,115자)을 옮겼다 (실행 2026-09-30-06)
- 2026-09-30 · 생성 · [43. 데이터·관측성·배포 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area43-s7.md) — 자동 분리: 43. 데이터·관측성·배포 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,055자)을 옮겼다 (실행 2026-09-30-06)
- 2026-09-30 · 생성 · [43. 데이터·관측성·배포 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area43-s4.md) — 자동 분리: 43. 데이터·관측성·배포 의 "4. 핵심 개념과 용어" 절(975자)을 옮겼다 (실행 2026-09-30-06)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-762]: Open Robotics (open-rmf), rmf-web — packages/api-server/README.md, 미확인, https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md, 접근일 2026-09-30
[^ref-1032]: Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L, arXiv), ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2, 2022-07, https://arxiv.org/abs/2201.00393, 접근일 2026-09-30
[^ref-1033]: Yu, J., Lee, S., Choi, Y., & Park, K.-J. (arXiv), ros2probe: Non-intrusive, Kernel-selective Observability for Robot Operating System 2 Middleware, 2026-06, https://arxiv.org/abs/2606.10746, 접근일 2026-09-30
[^ref-1034]: Open Robotics (ROS 2 Documentation), Iron Irwini (iron), 2023-05-23, https://docs.ros.org/en/rolling/Releases/Release-Iron-Irwini.html, 접근일 2026-09-30
[^ref-1036]: OpenTelemetry (CNCF), Specification Status Summary, 미확인, https://opentelemetry.io/docs/specs/status/, 접근일 2026-09-30
[^ref-1037]: OpenTelemetry (open-telemetry/semantic-conventions-genai), semantic-conventions-genai/docs/gen-ai/gen-ai-token-metrics.md, 미확인, https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md, 접근일 2026-09-30
[^ref-1038]: szobov (GitHub), ros-opentelemetry — ROS2 x OpenTelemetry README, 미확인, https://github.com/szobov/ros-opentelemetry, 접근일 2026-09-30
[^ref-1039]: Zhang, J., Yu, X., & Westerlund, T. (Sensors 25(16):5067), Enhancing the Resilience of ROS 2-Based Multi-Robot Systems with Kubernetes: A Case Study on UWB-Based Relative Positioning, 2025-08-14, https://pmc.ncbi.nlm.nih.gov/articles/PMC12390455/, 접근일 2026-09-30
[^ref-1040]: Northern.tech (mendersoftware), mender — README, 미확인, https://github.com/mendersoftware/mender, 접근일 2026-09-30
[^ref-766]: 개인정보보호위원회 (국가법령정보센터), 개인정보의 안전성 확보조치 기준 (개인정보보호위원회고시 제2023-6호), 2023-09-22, https://www.law.go.kr/admRulLsInfoP.do?chrClsCd=010202&admRulSeq=2100000229672, 접근일 2026-09-30 (원문 미열람)
[^ref-1041]: FinOps Foundation, FinOps Phases, 미확인, https://www.finops.org/framework/phases/, 접근일 2026-09-30
[^ref-1042]: FinOps Foundation, Introducing FOCUS 1.2: SaaS/PaaS Support, Invoice Reconciliation, and more (발행 기관의 발표 글, 명세 본문 미열람), 2025-06-03, https://www.finops.org/insights/focus-1-2-available/, 접근일 2026-09-30
[^ref-943]: Lee, Y., Kim, S.-E., Kim, J. S. 외 (Digital Health 12), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-09-30
[^ref-1043]: Bruno, L. D. M., Sim, J., & Hagiwara, Y. (arXiv), Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots, 2026-09, https://arxiv.org/abs/2609.29043, 접근일 2026-09-30
[^ref-1044]: Ocado Group, Ocado's digital twins and simulations: driving efficiencies and innovation at scale, 2025-06-04, https://www.ocadogroup.com/newsroom/stories/digital-twins-and-simulations, 접근일 2026-09-30
```

### runs/2026-10-09-19/pages/topics/2026/2026-10-09-area43-s6.md

```markdown
---
title: "43. 데이터·관측성·배포 — 대표 접근법과 기술"
type: topic
category: "K. 플랫폼 아키텍처·인프라"
primary_area_no: 43
related_areas: [3, 13, 21, 22, 34, 37, 38, 39, 41, 42, 44, 47, 52, 53, 54, 57, 58, 59, 61, 63]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-1032, ref-1033, ref-1034, ref-1036, ref-1037, ref-1038, ref-1039, ref-1040, ref-1041, ref-1042, ref-1371, ref-1372, ref-1373, ref-1375, ref-1376, ref-762]
last_run: 2026-10-09
version: 1
split_from: docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md#6
---

[홈](../../index.md) › [주제](../index.md) › 43. 데이터·관측성·배포 — 대표 접근법과 기술

# 43. 데이터·관측성·배포 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 공개 자료를 종합하면 플랫폼 자체의 관리는 자기 기술형 기록 형식과 기록 DB(데이터), OpenTelemetry 기반 플랫폼 관찰과 저부하 로봇 내부 추적(상태), 컨테이너 자동 재시작·이미지 기반 A/B 롤백·배포 전 시뮬레이션 검증(배포), 표준 청구 데이터와 토큰 지표를 쓰는 FinOps 주기(비용)의 조합으로 보인다. [추정][^ref-1034][^ref-762][^ref-1032][^ref-1033][^ref-1036][^ref-1038][^ref-1039][^ref-1040][^ref-1037][^ref-1041][^ref-1042]
- 이 페이지는 [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

공개 자료를 종합하면 플랫폼 자체의 관리는 자기 기술형 기록 형식과 기록 DB(데이터), OpenTelemetry 기반 플랫폼 관찰과 저부하 로봇 내부 추적(상태), 컨테이너 자동 재시작·이미지 기반 A/B 롤백·배포 전 시뮬레이션 검증(배포), 표준 청구 데이터와 토큰 지표를 쓰는 FinOps 주기(비용)의 조합으로 보인다. [추정][^ref-1034][^ref-762][^ref-1032][^ref-1033][^ref-1036][^ref-1038][^ref-1039][^ref-1040][^ref-1037][^ref-1041][^ref-1042]


### 2026-10-09 갱신: 배포 시점 판단과 기록 잇기

2026-09-30 까지 정리한 내용은 [43. 데이터·관측성·배포 — 대표 접근법과 기술 (2026-09-30)](2026-09-30-area43-s6.md)에 있다.

이번 갱신에서 확인한 배포 쪽 근거는 대부분 로봇·장치 운영체제의 업데이트 도구로 연계 대상이며, ROP 가 직접 정할 몫은 로봇 작업 상태에 맞춘 배포 시점·순서 판단으로 보인다. [추정][^ref-1371][^ref-1372]

**배포와 되돌리기**

- 연계 대상: 오픈소스 무선 업데이트 관리자 Mender 의 상태 스크립트(state script)는 다운로드·설치·재부팅·확정(commit)·롤백 같은 상태의 앞(Enter)·뒤(Leave)에서 실행되며, 반환값 0 은 진행, 1 은 중단·롤백, 21 은 설정한 간격 뒤 다시 실행(나중에 재시도)을 뜻하고, 재시도 총 시간과 실행당 시간에 상한을 둔다(발행일 미확인, 2026-10-09 확인). [사실][^ref-1371]
- 연계 대상: Mender 는 상태 스크립트 오류나 업데이트 모듈 실패 시 롤백하고 롤백된 배포를 항상 실패로 표시하며 스크립트 오류 출력을 포함한 로그를 서버로 올리지만, 상태 스크립트가 바꾼 영구 데이터는 되돌리지 않으므로 설치 전 백업·확정 시 삭제·롤백 시 복원을 스크립트로 두게 한다. [사실][^ref-1371]
- 연계 대상: Mender 는 상용판(Enterprise·Professional)의 단계적 배포(phased rollout)가 배포를 시간차 단계로 나눠 단계별 장치 비율(예 5%→15%→나머지, 단계 사이 24시간)을 정하고 오류 증가가 보이면 대부분의 장치에 닿기 전에 중단할 수 있게 한다고 밝힌다(2020-01-28 블로그). [추정] 벤더 주장[^ref-1372]
- 나중에 재시도 반환값과 단계적 배포를 쓰면 로봇이 작업 중일 때 설치·재부팅을 미루고 일부 장치부터 배포할 수 있을 것으로 보이나, 확인한 자료는 로봇 작업 상태와 연동한 배포 시점·중단 기준을 다루지 않으므로 작업 중 여부·충전 대기 여부 확인과 순서 결정은 ROP 가 직접 정해야 할 것으로 보인다(oq-213). [추정][^ref-1371][^ref-1372]
- Lumpp·Panato·Bombieri·Fummi(2024)는 ROS 기반 로봇 소프트웨어를 Docker 로 컨테이너화하고 Kubernetes 로 엣지–클라우드에 배치하면서 배포 전에 기능·비기능 제약을 검사하는 설계 흐름을 제안해 RB-Kairos 이동 로봇의 산업용 애자일 생산 체인(industrial agile production chain) 임무에 적용했고, 로봇 하드웨어 부하를 줄이면서 성능·네트워크 부담은 작았다고 보고했다(기관 저장소 초록 기준, 적용 환경이 실제 공장인지와 수치는 미확인). [사실][^ref-1376]
- Open-RMF 웹 API 서버(rmf-web api-server)는 데이터베이스 스키마 변경을 aerich 이행 도구로 처리해, 모델(예 TaskState)에 필드를 더한 뒤 이행 파일 생성(migrate)·적용(upgrade)·서버 재시작 순서를 거치게 한다(발행일 미확인, 2026-10-09 확인). [사실][^ref-762]

**서로 다른 기록을 하나의 추적으로 잇기**

- W3C Trace Context(권고안, 2021-11-23)는 traceparent(버전·trace-id·parent-id·trace-flags)와 tracestate 헤더로 추적 문맥을 전달하는 형식을 HTTP 에 대해 정하고, 다른 통신 프로토콜에도 관련이 있다고 보면서 그 직렬화는 확장·외부 명세에 맡긴다. [사실][^ref-1373]
- Bédard·Lajoie·Beltrame·Dagenais(2023-03)는 ros2_tracing 을 확장해 분산 ROS 2 시스템의 메시지 흐름을 분석·시각화하는 방법을 내놓았고, 입력·출력 메시지 사이의 일대다·다대다 인과 관계를 추적 데이터로 찾으며 간접 인과는 사용자 주석으로 잡고, 합성·실제 로봇 시스템에서 낮은 실행 부담을 보였다고 보고했다(초록 기준, 부담 수치 미확인). [사실][^ref-1375]
- Trace Context 가 ROS 2·DDS 메시지용 표준 직렬화를 두지 않으므로, 로봇 기록과 플랫폼 추적을 잇는 방법은 메시지에 추적 문맥 필드를 넣는 방식(ros-opentelemetry)과 필드 없이 추적 데이터에서 인과를 추론하는 방식(메시지 흐름 분석) 두 갈래로 보이며, 이종 제조사 로그까지 하나의 작업 식별자로 이은 표준·공개 사례는 이번에도 찾지 못했다(oq-210). [추정][^ref-1373][^ref-1038][^ref-1375] ROS 2 내부 메시지 흐름 추적은 로봇 소프트웨어 쪽 기법이므로 이 영역에서는 관찰 방법의 근거로만 쓴다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1032]: Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L, arXiv), ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2, 2022-07, https://arxiv.org/abs/2201.00393, 접근일 2026-09-30
[^ref-1033]: Yu, J., Lee, S., Choi, Y., & Park, K.-J. (arXiv), ros2probe: Non-intrusive, Kernel-selective Observability for Robot Operating System 2 Middleware, 2026-06, https://arxiv.org/abs/2606.10746, 접근일 2026-09-30
[^ref-1034]: Open Robotics (ROS 2 Documentation), Iron Irwini (iron), 2023-05-23, https://docs.ros.org/en/rolling/Releases/Release-Iron-Irwini.html, 접근일 2026-09-30
[^ref-1036]: OpenTelemetry (CNCF), Specification Status Summary, 미확인, https://opentelemetry.io/docs/specs/status/, 접근일 2026-10-09
[^ref-1037]: OpenTelemetry (open-telemetry/semantic-conventions-genai), semantic-conventions-genai/docs/gen-ai/gen-ai-token-metrics.md, 미확인, https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md, 접근일 2026-10-09
[^ref-1038]: szobov (GitHub), ros-opentelemetry — ROS2 x OpenTelemetry README, 미확인, https://github.com/szobov/ros-opentelemetry, 접근일 2026-10-09 (원문 미열람)
[^ref-1039]: Zhang, J., Yu, X., & Westerlund, T. (Sensors 25(16):5067), Enhancing the Resilience of ROS 2-Based Multi-Robot Systems with Kubernetes: A Case Study on UWB-Based Relative Positioning, 2025-08-14, https://pmc.ncbi.nlm.nih.gov/articles/PMC12390455/, 접근일 2026-09-30
[^ref-1040]: Northern.tech (mendersoftware), mender — README, 미확인, https://github.com/mendersoftware/mender, 접근일 2026-09-30
[^ref-1041]: FinOps Foundation, FinOps Phases, 미확인, https://www.finops.org/framework/phases/, 접근일 2026-09-30
[^ref-1042]: FinOps Foundation, Introducing FOCUS 1.2: SaaS/PaaS Support, Invoice Reconciliation, and more (발행 기관의 발표 글, 명세 본문 미열람), 2025-06-03, https://www.finops.org/insights/focus-1-2-available/, 접근일 2026-09-30
[^ref-1371]: Northern.tech (Mender documentation), State scripts, 미확인, https://docs.mender.io/artifact-creation/state-scripts, 접근일 2026-10-09
[^ref-1372]: Northern.tech (Mender blog, Farshad Tavakoli), Managing fleets of connected devices with Phased Rollout, 2020-01-28, https://mender.io/blog/managing-fleets-of-connected-devices-with-phased-rollout, 접근일 2026-10-09
[^ref-1373]: W3C, Trace Context, 2021-11-23, https://www.w3.org/TR/trace-context/, 접근일 2026-10-09
[^ref-1375]: Bédard, C., Lajoie, P.-Y., Beltrame, G., & Dagenais, M. (Robotics and Autonomous Systems 161, arXiv), Message Flow Analysis with Complex Causal Links for Distributed ROS 2 Systems, 2023-03, https://arxiv.org/abs/2204.10208, 접근일 2026-10-09
[^ref-1376]: Lumpp, F., Panato, M., Bombieri, N., & Fummi, F. (Università di Verona IRIS), A Design Flow based on Docker and Kubernetes for ROS-based Robotic Software Applications, 2024, https://iris.univr.it/handle/11562/1092207, 접근일 2026-10-09
[^ref-762]: Open Robotics (open-rmf), rmf-web — packages/api-server/README.md, 미확인, https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md, 접근일 2026-10-09

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-09-19 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-09 | 2026-10-09-19 | 43. 데이터·관측성·배포 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-10-09-19/pages/topics/2026/2026-10-09-area43-s7.md

```markdown
---
title: "43. 데이터·관측성·배포 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "K. 플랫폼 아키텍처·인프라"
primary_area_no: 43
related_areas: [3, 13, 21, 22, 34, 37, 38, 39, 41, 42, 44, 47, 52, 53, 54, 57, 58, 59, 61, 63]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-1036, ref-1037, ref-1371, ref-1373, ref-1374, ref-762]
last_run: 2026-10-09
version: 1
split_from: docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md#7
---

[홈](../../index.md) › [주제](../index.md) › 43. 데이터·관측성·배포 — 관련 표준·프레임워크·오픈소스

# 43. 데이터·관측성·배포 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 도구는 기록(rosbag2·MCAP), 관찰(OpenTelemetry·ros2_tracing), 배포(K3s·Mender), 비용(FinOps·FOCUS)으로 나뉜다.
- 이 페이지는 [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 도구는 기록(rosbag2·MCAP), 관찰(OpenTelemetry·ros2_tracing), 배포(K3s·Mender), 비용(FinOps·FOCUS)으로 나뉜다. 2026-09-30 주제 페이지 [43. 데이터·관측성·배포 — 관련 표준·프레임워크·오픈소스 (2026-09-30)](2026-09-30-area43-s7.md)의 표 행은 2026-09-30 확인 기준이며, 그 가운데 OpenTelemetry 명세 상태와 생성형 AI 의미 규약 행은 이번 실행의 2026-10-09 확인 항목으로 갱신된다.

### 2026-10-09 확인 기준 갱신

2026-09-30 까지 정리한 내용은 [43. 데이터·관측성·배포 — 관련 표준·프레임워크·오픈소스 (2026-09-30)](2026-09-30-area43-s7.md)에 있다. 그 페이지 표의 OpenTelemetry 명세 상태와 생성형 AI 의미 규약 행은 아래 항목으로 기준일을 갱신하며, 아래 항목은 모두 2026-10-09 확인 기준이다. 전체 표준·오픈소스 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

- **OpenTelemetry 명세 상태**(오픈소스): 상태 요약 페이지는 추적(API·SDK·프로토콜)과 로그(브리지 API·SDK·프로토콜)를 안정, 지표는 API·프로토콜 안정에 SDK 혼합, 프로파일은 프로토콜 개발 단계로 표시해 2026-09-30 확인 내용과 같다(페이지 갱신일 미확인). [사실][^ref-1036]
- **[생성형 AI 의미 규약](../../glossary/opentelemetry-genai-semantic-conventions.md) — 토큰 지표**(오픈소스): 의미 규약 사이트의 생성형 AI 지표 페이지는 규약이 별도 저장소(semantic-conventions-genai)로 옮겨졌다며 “This page has moved and is no longer maintained in this repository.”라고 안내한다. [사실][^ref-1374] 그 저장소의 현재 토큰 지표 문서는 gen_ai.client.inference.usage.* 카운터 5종(입력·출력·캐시 읽기 입력·캐시 쓰기 입력·추론 출력)과 gen_ai.client.inference.operation.* 히스토그램 2종(입력·출력)을 모두 개발(Development) 단계로 정의하며, gen_ai.client.token.usage 에 대한 이름 변경·폐기 안내는 담지 않는다. [사실][^ref-1037] 같은 문서는 캐시 읽기·캐시 쓰기·추론 카운터를 입력·출력 사용량 카운터의 부분집합으로 두고, 호출별 히스토그램은 백분위·이상값 분석용이며 합계나 비용 산정용이 아니라고 구분한다. [사실][^ref-1037]
- 토큰 지표가 아직 개발 단계이고 안정 판 일정도 밝혀지지 않았으므로, 언어 모델 호출 비용 계측은 별도 저장소의 특정 판을 고정해 카운터(gen_ai.client.inference.usage.*)로 합계를 잡고 히스토그램은 지연·이상값 분석에만 쓰는 방식이 가능해 보이나, 고정 기준은 표준이 정해 주지 않는다(oq-212). [추정][^ref-1037][^ref-1374]
- **W3C Trace Context**(표준, 권고안 2021-11-23): 추적 문맥을 traceparent·tracestate 헤더로 전달하는 형식을 HTTP 에 대해 정하며, 다른 프로토콜의 직렬화는 확장·외부 명세에 맡긴다. [사실][^ref-1373]
- **Mender 상태 스크립트**(오픈소스, 연계 대상): 업데이트 상태 전후에 실행되어 반환값으로 진행·롤백·나중에 재시도를 정한다. [사실][^ref-1371]
- **Open-RMF rmf-web api-server 의 aerich 이행**(오픈소스): 작업 상태 모델의 스키마 변경을 이행 파일 생성·적용·서버 재시작 순서로 처리한다. [사실][^ref-762]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1036]: OpenTelemetry (CNCF), Specification Status Summary, 미확인, https://opentelemetry.io/docs/specs/status/, 접근일 2026-10-09
[^ref-1037]: OpenTelemetry (open-telemetry/semantic-conventions-genai), semantic-conventions-genai/docs/gen-ai/gen-ai-token-metrics.md, 미확인, https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md, 접근일 2026-10-09
[^ref-1371]: Northern.tech (Mender documentation), State scripts, 미확인, https://docs.mender.io/artifact-creation/state-scripts, 접근일 2026-10-09
[^ref-1373]: W3C, Trace Context, 2021-11-23, https://www.w3.org/TR/trace-context/, 접근일 2026-10-09
[^ref-1374]: OpenTelemetry (CNCF), Moved: Generative AI semantic conventions, 미확인, https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-metrics/, 접근일 2026-10-09
[^ref-762]: Open Robotics (open-rmf), rmf-web — packages/api-server/README.md, 미확인, https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md, 접근일 2026-10-09

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-09-19 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-09 | 2026-10-09-19 | 43. 데이터·관측성·배포 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-10-09-19/pages/topics/2026/2026-10-09-area43-s11.md

```markdown
---
title: "43. 데이터·관측성·배포 — 열린 질문"
type: topic
category: "K. 플랫폼 아키텍처·인프라"
primary_area_no: 43
related_areas: [3, 13, 21, 22, 34, 37, 38, 39, 41, 42, 44, 47, 52, 53, 54, 57, 58, 59, 61, 63]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-1037, ref-1038, ref-1313, ref-1314, ref-1367, ref-1370, ref-1371, ref-1372, ref-1373, ref-1374, ref-1375, ref-766, ref-943]
last_run: 2026-10-09
version: 1
split_from: docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md#11
---

[홈](../../index.md) › [주제](../index.md) › 43. 데이터·관측성·배포 — 열린 질문

# 43. 데이터·관측성·배포 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 아래 질문은 이번 실행에서 새로 올렸다. 번호는 퍼블리셔가 부여하며 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

아래 질문은 이번 실행에서 새로 올렸다. 번호는 퍼블리셔가 부여하며 전체 목록은 [열린 질문](../../open-questions.md)에 있다.


### 2026-10-09 갱신

2026-09-30 까지 올린 질문은 [43. 데이터·관측성·배포 — 열린 질문 (2026-09-30)](2026-09-30-area43-s11.md)에 있다.

이번 실행은 아래 기존 질문에 부분 근거만 더했고, 해결로 바꾼 질문은 없다.

- **oq-210** (상태: 열림 · 실행 2026-10-09-19) 부분 근거: 추적 문맥 표준은 ROS 2·DDS 메시지용 직렬화를 두지 않고, 메시지 필드 방식과 인과 추론 방식 두 갈래가 보이지만 이종 제조사 로그까지 하나의 작업 식별자로 이은 표준·공개 사례는 찾지 못했다. [추정][^ref-1373][^ref-1038][^ref-1375]
- **oq-212** (상태: 열림 · 실행 2026-10-09-19) 부분 근거: 토큰 지표는 모두 개발 단계이고 gen_ai.client.token.usage 에 대한 이름 변경·폐기 안내가 현재 문서에 없어, 특정 판을 고정하는 방식은 가능해 보이나 고정 기준은 표준이 정해 주지 않는다. [추정][^ref-1037][^ref-1374]
- **oq-213** (상태: 열림 · 실행 2026-10-09-19) 부분 근거: 장치 업데이트 도구의 나중에 재시도·단계적 배포 기능은 있으나, 로봇 작업 상태와 연동한 배포 시점·중단 기준을 공개한 자료는 찾지 못했다. [추정][^ref-1371][^ref-1372]
- **oq-214** (상태: 열림 · 실행 2026-10-09-19) 부분 근거: 2025-10-31 시행 개정으로 접속기록 대상이 넓어지고 보관·점검 조항에 1년 유예가 있다는 보도가 있으나, 개정 고시 번호·제8조 현행 문구·유예 종료일은 미확인이다. [추정][^ref-1367][^ref-766]
- **oq-215** (상태: 열림 · 실행 2026-10-09-19) 부분 근거: 원문은 122건·실패 14건·완료 108건을 밝히지만 87.03% 의 분모를 설명하지 않아, 108/122(약 88.5%)와의 불일치는 원문만으로 풀리지 않는다. [추정][^ref-943]
- **oq-316** (상태: 열림 · 실행 2026-10-09-19) 부분 근거: 제공자(제19조)와 배포자(제26조)가 각자 통제하는 로그를 6개월 이상 보관하므로 보관 주체는 역할과 로그 통제권 배분에 따라 갈리는 것으로 보이며, 로봇 플랫폼의 고위험 해당 여부는 출처가 다루지 않는다. [추정][^ref-1313][^ref-1314][^ref-1370]

새로 올린 질문(번호는 퍼블리셔가 부여한다):

- 2025-10-31 개정으로 접속기록 보관 대상이 개인정보처리시스템에 접속한 모든 자로 넓어졌다면, 로봇·플랫폼 서비스가 쓰는 기계 계정의 개인정보처리시스템 접속도 접속기록 보관·점검 대상에 들어가는가? [^ref-1367]
- 로봇 플랫폼 사업자와 현장 운영자가 각각 EU AI Act 의 제공자·배포자가 될 때 실행 기록의 통제권과 6개월 이상 보관 책임을 계약으로 나눈 공개 사례나 지침이 있는가? [^ref-1313][^ref-1314]
- W3C Trace Context 의 추적 문맥을 ROS 2·DDS 메시지나 VDA 5050 같은 MQTT 기반 로봇–관제 메시지에 싣는 공식 직렬화 규약이 있는가? [^ref-1373]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1037]: OpenTelemetry (open-telemetry/semantic-conventions-genai), semantic-conventions-genai/docs/gen-ai/gen-ai-token-metrics.md, 미확인, https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md, 접근일 2026-10-09
[^ref-1038]: szobov (GitHub), ros-opentelemetry — ROS2 x OpenTelemetry README, 미확인, https://github.com/szobov/ros-opentelemetry, 접근일 2026-10-09 (원문 미열람)
[^ref-1313]: European Commission (AI Act Service Desk), Article 19: Automatically Generated Logs, 미확인, https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-19, 접근일 2026-10-09
[^ref-1314]: European Commission (AI Act Service Desk), Article 26: Obligations of Deployers of High-Risk AI Systems, 미확인, https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26, 접근일 2026-10-09
[^ref-1367]: 바이라인네트워크 (곽중희), 개인정보위, 인터넷망 일률 차단제도 개선 “위험기반 보호로 전환”, 2025-10-31, https://byline.network/2025/10/31-281/, 접근일 2026-10-09
[^ref-1370]: Hunton Andrews Kurth (Privacy & Cybersecurity Law Blog), EU Digital Omnibus on AI Enters into Force, 미확인, https://www.hunton.com/privacy-and-cybersecurity-law-blog/eu-digital-omnibus-on-ai-enters-into-force, 접근일 2026-10-09
[^ref-1371]: Northern.tech (Mender documentation), State scripts, 미확인, https://docs.mender.io/artifact-creation/state-scripts, 접근일 2026-10-09
[^ref-1372]: Northern.tech (Mender blog, Farshad Tavakoli), Managing fleets of connected devices with Phased Rollout, 2020-01-28, https://mender.io/blog/managing-fleets-of-connected-devices-with-phased-rollout, 접근일 2026-10-09
[^ref-1373]: W3C, Trace Context, 2021-11-23, https://www.w3.org/TR/trace-context/, 접근일 2026-10-09
[^ref-1374]: OpenTelemetry (CNCF), Moved: Generative AI semantic conventions, 미확인, https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-metrics/, 접근일 2026-10-09
[^ref-1375]: Bédard, C., Lajoie, P.-Y., Beltrame, G., & Dagenais, M. (Robotics and Autonomous Systems 161, arXiv), Message Flow Analysis with Complex Causal Links for Distributed ROS 2 Systems, 2023-03, https://arxiv.org/abs/2204.10208, 접근일 2026-10-09
[^ref-766]: 개인정보보호위원회 (국가법령정보센터), 개인정보의 안전성 확보조치 기준 (개인정보보호위원회고시 제2023-6호), 2023-09-22, https://www.law.go.kr/admRulLsInfoP.do?chrClsCd=010202&admRulSeq=2100000229672, 접근일 2026-10-09 (원문 미열람)
[^ref-943]: Lee, Y., Kim, S.-E., Kim, J. S. 외 (Digital Health 12), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-10-09

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-09-19 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-09 | 2026-10-09-19 | 43. 데이터·관측성·배포 의 "열린 질문" 절에서 분리 |
```

### runs/2026-10-09-19/pages/topics/2026/2026-10-09-area43-s10.md

```markdown
---
title: "43. 데이터·관측성·배포 — 다른 연구영역과의 연결"
type: topic
category: "K. 플랫폼 아키텍처·인프라"
primary_area_no: 43
related_areas: [3, 13, 21, 22, 34, 37, 38, 39, 41, 42, 44, 47, 52, 53, 54, 57, 58, 59, 61, 63]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-1037, ref-1313, ref-1314, ref-1367, ref-1370, ref-1371, ref-1372, ref-1373, ref-1375]
last_run: 2026-10-09
version: 1
split_from: docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md#10
---

[홈](../../index.md) › [주제](../index.md) › 43. 데이터·관측성·배포 — 다른 연구영역과의 연결

# 43. 데이터·관측성·배포 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 기록을 쓰는 관제·분석 영역, 배포·검증 영역, 비용·규제 영역, 언어 모델 영역, 적용 현장과 이어진다.
- 이 페이지는 [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 기록을 쓰는 관제·분석 영역, 배포·검증 영역, 비용·규제 영역, 언어 모델 영역, 적용 현장과 이어진다.


### 2026-10-09 추가 연결

2026-09-30 까지 정리한 연결은 [43. 데이터·관측성·배포 — 다른 연구영역과의 연결 (2026-09-30)](2026-09-30-area43-s10.md)에 있다.

- [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) — 연계 대상: EU AI Act 제19조 제1항은 고위험 AI 시스템 제공자가 자기 통제 아래 있는 제12조 제1항의 자동 생성 로그를 의도된 목적에 맞는 기간, 적어도 6개월 보관하게 하고 다른 EU·회원국 법(특히 개인정보 보호법)이 달리 정하면 그에 따르게 한다. [사실][^ref-1313] 제26조는 배포자에게 사용 설명서에 따라 운영을 감시하고 위험이 의심되면 제공자·유통자·시장감시당국에 알리고 사용을 멈추게 하며(제5항), 자기 통제 아래 있는 자동 생성 로그를 적어도 6개월 보관하게 한다(제6항). [사실][^ref-1314] 로펌 Hunton 의 글(발행일 미확인, 2026-10-09 확인)에 따르면 AI 디지털 옴니버스 규정(Regulation (EU) 2026/1744)이 2026-07-27 발효되어 부속서 III 고위험 AI 의무 적용일을 2027-12-02 로, 부속서 I 규제 제품에 내장된 고위험 AI 의무 적용일을 2028-08-02 로 미뤘다. [사실][^ref-1370]
- [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) — 로봇 플랫폼의 AI 구성요소가 고위험으로 분류되면 플랫폼 사업자가 제공자인지 배포자인지(또는 둘 다인지)와 로그 통제권 배분에 따라 실행 기록 보관 책임이 갈리고, 기계류 등 부속서 I 제품에 내장된 경우라면 적용 시점은 2028-08-02 로 보인다(oq-316). [추정][^ref-1313][^ref-1314][^ref-1370]
- [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)·[37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) — 보관 의무가 걸리는 자동 생성 로그는 AI 구성요소의 운영 기록과 관제 실행 기록에 해당할 것으로 보여, 이 영역의 보존 정책이 두 영역의 기록 설계와 맞물릴 것으로 보인다. [추정][^ref-1313][^ref-1314]
- [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md) — 접속기록 보관 대상 범위가 넓어졌다는 보도에 따라, 접속기록 대상 판단은 이 영역과 함께 다뤄야 할 것으로 보인다. [추정][^ref-1367]
- [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) — 장치 업데이트의 재시도·롤백 도구(연계 대상)와 ROP 의 배포 시점 판단이 소프트웨어 버전 관리와 이어질 것으로 보인다. [추정][^ref-1371][^ref-1372]
- [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md) — W3C Trace Context 는 HTTP 외 프로토콜의 직렬화를 확장에 맡기므로, 로봇–관제 메시지에 추적 문맥을 싣는 규약이 상호운용 표준의 과제가 될 것으로 보인다. [추정][^ref-1373]
- [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md)·[13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) — 메시지 흐름 인과 분석은 원인 분석의 입력이 되고, 개발 단계인 토큰 지표는 언어 모델 호출 계측 기준을 고정하는 문제로 이어질 것으로 보인다. [추정][^ref-1375][^ref-1037]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1037]: OpenTelemetry (open-telemetry/semantic-conventions-genai), semantic-conventions-genai/docs/gen-ai/gen-ai-token-metrics.md, 미확인, https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md, 접근일 2026-10-09
[^ref-1313]: European Commission (AI Act Service Desk), Article 19: Automatically Generated Logs, 미확인, https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-19, 접근일 2026-10-09
[^ref-1314]: European Commission (AI Act Service Desk), Article 26: Obligations of Deployers of High-Risk AI Systems, 미확인, https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26, 접근일 2026-10-09
[^ref-1367]: 바이라인네트워크 (곽중희), 개인정보위, 인터넷망 일률 차단제도 개선 “위험기반 보호로 전환”, 2025-10-31, https://byline.network/2025/10/31-281/, 접근일 2026-10-09
[^ref-1370]: Hunton Andrews Kurth (Privacy & Cybersecurity Law Blog), EU Digital Omnibus on AI Enters into Force, 미확인, https://www.hunton.com/privacy-and-cybersecurity-law-blog/eu-digital-omnibus-on-ai-enters-into-force, 접근일 2026-10-09
[^ref-1371]: Northern.tech (Mender documentation), State scripts, 미확인, https://docs.mender.io/artifact-creation/state-scripts, 접근일 2026-10-09
[^ref-1372]: Northern.tech (Mender blog, Farshad Tavakoli), Managing fleets of connected devices with Phased Rollout, 2020-01-28, https://mender.io/blog/managing-fleets-of-connected-devices-with-phased-rollout, 접근일 2026-10-09
[^ref-1373]: W3C, Trace Context, 2021-11-23, https://www.w3.org/TR/trace-context/, 접근일 2026-10-09
[^ref-1375]: Bédard, C., Lajoie, P.-Y., Beltrame, G., & Dagenais, M. (Robotics and Autonomous Systems 161, arXiv), Message Flow Analysis with Complex Causal Links for Distributed ROS 2 Systems, 2023-03, https://arxiv.org/abs/2204.10208, 접근일 2026-10-09

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-09-19 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-09 | 2026-10-09-19 | 43. 데이터·관측성·배포 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-10-09-19/pages/topics/2026/2026-10-09-area43-s8.md

```markdown
---
title: "43. 데이터·관측성·배포 — 대표 연구와 자료"
type: topic
category: "K. 플랫폼 아키텍처·인프라"
primary_area_no: 43
related_areas: [3, 13, 21, 22, 34, 37, 38, 39, 41, 42, 44, 47, 52, 53, 54, 57, 58, 59, 61, 63]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-1032, ref-1033, ref-1039, ref-1043, ref-1375, ref-1376, ref-943]
last_run: 2026-10-09
version: 1
split_from: docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md#8
---

[홈](../../index.md) › [주제](../index.md) › 43. 데이터·관측성·배포 — 대표 연구와 자료

# 43. 데이터·관측성·배포 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 아래 다섯 건이 이 영역의 대표 자료이며, 실행 추적·관찰 부담·배포 복원력·호출 비용·현장 기록 분석을 각각 보여 준다.
- 이 페이지는 [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

아래 다섯 건이 이 영역의 대표 자료이며, 실행 추적·관찰 부담·배포 복원력·호출 비용·현장 기록 분석을 각각 보여 준다.

- Bédard·Lütkebohle·Dagenais, ros2_tracing(IEEE RA-L, 2022-07) — LTTng 기반 ROS 2 계측·추적 도구 모음으로, 로봇 내부 실행을 낮은 부담으로 기록하는 근거다. [사실][^ref-1032]
- Yu·Lee·Choi·Park, ros2probe(arXiv 프리프린트, 2026-06) — 관찰 도구가 대상을 교란하는 문제를 커널 선택 관찰로 줄인 연구로, 관찰 자체의 비용을 따져야 함을 보여 준다. [사실][^ref-1033]
- Zhang·Yu·Westerlund, Kubernetes 를 이용한 ROS 2 다중 로봇 시스템 복원력 연구(Sensors, 2025-08-14) — 컨테이너 자동 재시작으로 장애 중에도 위치 정확도를 유지한 실험실 결과다. [사실][^ref-1039]
- Bruno·Sim·Hagiwara, 서비스 로봇의 LLM 연쇄 기반 작업 계획(arXiv 프리프린트, 2026-09) — 클라우드 API 비용·지연을 동기로 로컬·클라우드 모델을 비교했다. [사실][^ref-1043]
- Lee 외, 혼잡한 병원에서 승강기 이용을 고려한 자율 약품 배송 로봇 실증(Digital Health, 2026-03-31) — 로봇·승강기 로그와 관찰 기록을 함께 모아 실패를 분석한 국내 현장 자료다. [사실][^ref-943]

2026-10-09 갱신에서 기록 잇기와 배포 전 검사를 보여 주는 두 건을 더했다.

- Bédard·Lajoie·Beltrame·Dagenais, 복잡한 인과 관계를 가진 분산 ROS 2 시스템의 메시지 흐름 분석(Robotics and Autonomous Systems 161, 2023-03) — ros2_tracing 을 확장해 메시지 사이의 일대다·다대다 인과를 추적 데이터로 찾는 방법으로, 메시지에 추적 필드를 넣지 않고 기록을 잇는 근거다. [사실][^ref-1375]
- Lumpp·Panato·Bombieri·Fummi, Docker·Kubernetes 기반 ROS 로봇 소프트웨어 설계 흐름(2024) — 배포 전에 기능·비기능 제약을 검사하고 엣지–클라우드에 배치하는 흐름을 RB-Kairos 이동 로봇 임무에 적용했다(적용 환경 미확인). [사실][^ref-1376]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1032]: Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L, arXiv), ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2, 2022-07, https://arxiv.org/abs/2201.00393, 접근일 2026-09-30
[^ref-1033]: Yu, J., Lee, S., Choi, Y., & Park, K.-J. (arXiv), ros2probe: Non-intrusive, Kernel-selective Observability for Robot Operating System 2 Middleware, 2026-06, https://arxiv.org/abs/2606.10746, 접근일 2026-09-30
[^ref-1039]: Zhang, J., Yu, X., & Westerlund, T. (Sensors 25(16):5067), Enhancing the Resilience of ROS 2-Based Multi-Robot Systems with Kubernetes: A Case Study on UWB-Based Relative Positioning, 2025-08-14, https://pmc.ncbi.nlm.nih.gov/articles/PMC12390455/, 접근일 2026-09-30
[^ref-1043]: Bruno, L. D. M., Sim, J., & Hagiwara, Y. (arXiv), Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots, 2026-09, https://arxiv.org/abs/2609.29043, 접근일 2026-09-30
[^ref-1375]: Bédard, C., Lajoie, P.-Y., Beltrame, G., & Dagenais, M. (Robotics and Autonomous Systems 161, arXiv), Message Flow Analysis with Complex Causal Links for Distributed ROS 2 Systems, 2023-03, https://arxiv.org/abs/2204.10208, 접근일 2026-10-09
[^ref-1376]: Lumpp, F., Panato, M., Bombieri, N., & Fummi, F. (Università di Verona IRIS), A Design Flow based on Docker and Kubernetes for ROS-based Robotic Software Applications, 2024, https://iris.univr.it/handle/11562/1092207, 접근일 2026-10-09
[^ref-943]: Lee, Y., Kim, S.-E., Kim, J. S. 외 (Digital Health 12), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-10-09

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-09-19 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-09 | 2026-10-09-19 | 43. 데이터·관측성·배포 의 "대표 연구와 자료" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 16건 / 전체 1324건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-762 | Open Robotics (open-rmf) | rmf-web — packages/api-server/README.md | 미확인 | https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md | 2026-09-25 | 예 |
| ref-766 | 국가법령정보센터(개인정보보호위원회 고시) | 개인정보의 안전성 확보조치 기준 | 미확인 | https://www.law.go.kr/admRulLsInfoP.do?chrClsCd=010202&admRulSeq=2100000229672 | 2026-09-25 | 아니오 |
| ref-943 | Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 2026-03-31 | https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/ | 2026-09-29 | 예 |
| ref-1032 | Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L, arXiv) | ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2 | 2022-07 | https://arxiv.org/abs/2201.00393 | 2026-09-30 | 예 |
| ref-1033 | Yu, J., Lee, S., Choi, Y., & Park, K.-J. (arXiv) | ros2probe: Non-intrusive, Kernel-selective Observability for Robot Operating System 2 Middleware | 2026-06 | https://arxiv.org/abs/2606.10746 | 2026-09-30 | 예 |
| ref-1034 | Open Robotics (ROS 2 Documentation) | Iron Irwini (iron) | 2023-05-23 | https://docs.ros.org/en/rolling/Releases/Release-Iron-Irwini.html | 2026-09-30 | 예 |
| ref-1035 | Foxglove | MCAP as the ROS 2 Default Bag Format | 2022-12-22 | https://foxglove.dev/blog/mcap-as-the-ros2-default-bag-format | 2026-09-30 | 예 |
| ref-1036 | OpenTelemetry (CNCF) | Specification Status Summary | 미확인 | https://opentelemetry.io/docs/specs/status/ | 2026-09-30 | 예 |
| ref-1037 | OpenTelemetry (open-telemetry/semantic-conventions-genai) | semantic-conventions-genai/docs/gen-ai/gen-ai-token-metrics.md | 미확인 | https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md | 2026-09-30 | 예 |
| ref-1038 | szobov (GitHub) | ros-opentelemetry — ROS2 x OpenTelemetry README | 미확인 | https://github.com/szobov/ros-opentelemetry | 2026-09-30 | 예 |
| ref-1039 | Zhang, J., Yu, X., & Westerlund, T. (Sensors 25(16):5067) | Enhancing the Resilience of ROS 2-Based Multi-Robot Systems with Kubernetes: A Case Study on UWB-Based Relative Positioning | 2025-08-14 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12390455/ | 2026-09-30 | 예 |
| ref-1040 | Northern.tech (mendersoftware) | mender — README | 미확인 | https://github.com/mendersoftware/mender | 2026-09-30 | 예 |
| ref-1041 | FinOps Foundation | FinOps Phases | 미확인 | https://www.finops.org/framework/phases/ | 2026-09-30 | 예 |
| ref-1042 | FinOps Foundation | Introducing FOCUS 1.2: SaaS/PaaS Support, Invoice Reconciliation, and more | 2025-06-03 | https://www.finops.org/insights/focus-1-2-available/ | 2026-09-30 | 예 |
| ref-1043 | Bruno, L. D. M., Sim, J., & Hagiwara, Y. (arXiv) | Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots | 2026-09 | https://arxiv.org/abs/2609.29043 | 2026-09-30 | 예 |
| ref-1044 | Ocado Group | Ocado's digital twins and simulations: driving efficiencies and innovation at scale | 2025-06-04 | https://www.ocadogroup.com/newsroom/stories/digital-twins-and-simulations | 2026-09-30 | 예 |
```

### docs/glossary/index.md (요약: 용어 381개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- linear-temporal-logic: 선형 시간 논리 (Linear Temporal Logic (LTL))
- littles-law: 리틀의 법칙 (Little's Law)
- llm-agent: LLM 에이전트 (LLM Agent)
- llm-modulo-framework: LLM-모듈로 프레임워크 (LLM-Modulo Framework)
- localization-score: 위치추정 품질 점수 (Localization Score (VDA 5050 localizationScore))
- location-check-digit: 위치 체크 디지트 (Location Check Digit)
- lockout-tagout: 잠금·표지 (Lockout/Tagout (LOTO))
- log-playback: 로그 재생 (Log Playback)
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
- technology-readiness-level: 기술 성숙도 (Technology Readiness Level (TRL))
- teleoperation: 원격 조작 (Teleoperation)
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- total-cost-of-ownership: 총소유비용 (Total Cost of Ownership (TCO))
- transparency-level-ieee-7001: 자율 시스템 투명성 수준 (Transparency Level (IEEE 7001-2021))
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
- wireless-safety-rated-emergency-stop: 무선 안전 비상정지 (Wireless Safety-rated Emergency Stop)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [43] 에 걸린 9건 / 전체 336건)

```markdown
- oq-210 [열림] 서로 다른 제조사 로봇의 기록(MCAP·제조사 로그)과 플랫폼 서비스의 분산 추적을 하나의 작업 식별자로 이어 원인 분석에 쓴 공개 사례나 표준이 있는가? (영역 43, 38)
- oq-211 [열림] 로봇 플랫폼이 수집하는 텔레메트리·주행 기록·영상의 보존 기간을 정한 국내 기준이나 운영 사례가 개인정보 접속기록 규정 밖에도 있는가? (영역 43, 53)
- oq-212 [열림] 개발 단계인 토큰 지표의 이름(gen_ai.client.inference.usage.* 와 다른 문서의 gen_ai.client.token.usage)이 바뀌었는지 미확인인데, 언어 모델 호출 비용 계측을 안정 판이 나오기 전까지 어떤 기준으로 고정할 것인가? (영역 43, 13)
- oq-213 [열림] 운행 중인 로봇 작업을 끊지 않고 현장 서버·로봇에 플랫폼 소프트웨어를 순차 배포하고 되돌리는 시점·기준을 공개한 로봇 관제 제품이나 연구가 있는가? (영역 43, 57)
- oq-214 [열림] 로봇 플랫폼에 적용될 수 있는 현행 「개인정보의 안전성 확보조치 기준」(2023-6호 이후 개정판)의 접속기록 보관 기간·점검 주기 조항이 2023-6호와 같은가? (영역 43, 53)
- oq-215 [열림] 구로병원 실증의 전체 성공률 87.03% 가 122건 중 실패 14건과 맞지 않는데(약 88.5%) 성공률의 분모는 무엇인가? (영역 43, 63)
- oq-297 [열림] VDA 5050 의 지도 배포(downloadMap·enableMap·deleteMap)로 로봇마다 활성화된 지도 판과 Open-RMF 빌딩 맵·LIF 레이아웃의 판을 ROP 한 곳에서 대응시켜 관리하는 공개 구현이나 운영 절차가 있는가? (영역 16, 43, 57)
- oq-300 [열림] 플랫폼 관제 서비스를 다중 클라우드 복제나 컨테이너 자동 재시작으로 운영하면서, 재시작 뒤 진행 중인 로봇 작업 상태를 잃지 않고 이어 간 공개 사례나 구성이 있는가? (영역 43, 41, 32)
- oq-316 [열림] 로봇 플랫폼의 AI 구성요소가 EU AI Act 고위험 AI 로 분류되면 제12조 자동 사건 기록 요건을 플랫폼 실행 기록이 충족해야 하는가, 그 기록의 보관 주체는 플랫폼 사업자와 배포자 가운데 누구인가? (영역 47, 37, 43)
```

### runs/2026-10-09-19/verification2.json

```json
{
  "run_id": "2026-10-09-19",
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
      "43. 데이터·관측성·배포 6·7·10·11절이 이번 실행의 분리 주제 페이지(2026-10-09-area43-s6·s7·s10·s11)로만 연결되고, 앞서 검증·게시된 상세 내용이 담긴 2026-09-30-area43-s6·s7·s10·s11 로 가는 링크가 영역 페이지 본문과 새 주제 페이지 어디에도 남지 않았다. 4절의 2026-09-30-area43-s4 링크와 3절의 2026-09-30-area43-s3 링크는 그대로다. 새 2026-10-09-area43-s7 3절의 '주제 페이지의 행은 2026-09-30 확인 기준'이 가리키는 표는 연결된 페이지에 없다"
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
    "6·7·10·11절 링크 연속성: 각 절의 2026-10-09 갱신 소절 첫머리에 이전 주제 페이지로 가는 링크 문장을 넣는다. 예: 6절은 '2026-09-30 까지 정리한 내용은 [43. 데이터·관측성·배포 — 대표 접근법과 기술 (2026-09-30)](../../topics/2026/2026-09-30-area43-s6.md)에 있다'로 쓰고, 7절은 2026-09-30-area43-s7, 10절은 2026-09-30-area43-s10, 11절은 2026-09-30-area43-s11 로 같은 방식으로 쓴다. 이유: 지금 산출물에서는 앞서 검증·게시된 6·7·10·11절 상세 내용이 영역 페이지 본문에서 연결되지 않는다(분리 뒤에도 같은 문장이 새 주제 페이지 3절에 남아야 한다. 영역 페이지와 docs/topics/2026/ 는 docs 아래 깊이가 같으므로 상대 경로가 그대로 맞는다).",
    "7절 문구: '주제 페이지의 행은 2026-09-30 확인 기준이며, 그 가운데 … 기준일은 아래 2026-10-09 확인으로 갱신한다' 문장을 고친다. 2026-09-30 주제 페이지(2026-09-30-area43-s7)의 표 행은 2026-09-30 확인 기준이고, OpenTelemetry 명세 상태와 생성형 AI 의미 규약 행은 2026-10-09 확인 항목으로 갱신된다는 뜻이 드러나게 쓴다. 이유: 분리 뒤 영역 페이지에는 '아래' 내용이 없고, 어느 주제 페이지의 행인지 알 수 없다.",
    "standards_updates 의 EU AI Act 항목: name 에서 'Regulation (EU) 2024/1689' 를 빼고 'EU AI Act 제19조 자동 생성 로그 (Article 19)' 처럼 쓴다. 이유: 규정 번호 2024/1689 는 브리프 finding 이나 출처 요약 어디에도 없는 드리프트다. 필요하면 additional_research_requests 로 넘긴다."
  ],
  "confidence": "low",
  "verification_note": "판정: 조건부 승인 / 2차 수정 후 재검증. 확인 24건, 미확인 0건, 교차 확인 1건(f10: AI 디지털 옴니버스 규정 번호·발효일·적용일. 독립 로펌·기관의 검색 결과가 일치). 강등: 없음. 원문 미열람 출처: ref-766, ref-1038. 주의: 새 [사실] 주장은 모두 단일 출처다. 국내 개인정보 고시 개정(f6)은 기사 1건 기준이며 개정 고시 번호·제8조 현행 문구·유예 종료일은 미확인이다. EU AI Act 적용일(f10)은 로펌 글(발행일 미확인)과 검색 결과 기준이며 관보 원문은 열지 않았다. 구로병원 실증의 성공률 87.03% 는 분모가 원문에 없어 저자 보고 수치로 남는다(oq-215). 원문 안에 2주 실시 기간과 '4주' 표현이 함께 있다. 승강기 대수는 원문에 없어 지웠다. 정정 요청 없음. 열린 질문 해결 인정 없음(oq-210·oq-212·oq-213·oq-214·oq-215·oq-316 부분 근거만). / 2차: 1차 수정 지시 11건 이행 확인(f14 승강기 대수 삭제, ref-1375 발행일 2023-03, ref-1370 발행일 미확인, f23 문구, f6·f7 보도 귀속과 미확인, f8~f11 연계 대상과 10절 연결, f16~f18 연계 대상·벤더 주장, ref-766·ref-1038 원문 미열람, 7절 기준일, 열린 질문 부분 근거, f15 속도 미확인). 본문 주장 드리프트 없음, 태그는 1차 처분과 같다. 드리프트 1건 처리 지시: standards_updates 의 규정 번호 'Regulation (EU) 2024/1689' 는 브리프 밖이다. [분류원문] 보존, 섹션 순서 준수, 링크는 형식 검증을 통과했다. 다만 자동 분리 뒤 6·7·10·11절이 이전 주제 페이지(2026-09-30-area43-s6·s7·s10·s11)와 끊겨 링크 복원을 지시했다. 이 링크 줄을 분리 코드가 지운다면 스토리텔러 재실행으로는 풀리지 않으므로, pipeline 담당이 분리 시 이전 주제 페이지 링크를 보존하는지 확인해야 한다. 사소한 의견: 8절의 Bédard 외 항목 끝 '메시지에 추적 필드를 넣지 않고 기록을 잇는 근거다'는 f22([추정])의 해석에 가깝다. 기존 항목들의 서술 관행과 같아 수정 지시로 내지는 않았다.",
  "retry_reason": null
}
```
