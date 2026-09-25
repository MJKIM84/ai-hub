(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-26-01
- date: 2026-09-26
- run_type: weekly_review (주간 정리)
- 대상: 해당 없음(주간 정리)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: false · fetch_mode: mirror_only (일반 웹 페이지 열람은 네트워크 정책으로 막혀 있다. raw.githubusercontent.com 은 열린다: 공식 문서가 GitHub 에 있는 출처는 입력의 config/source_mirrors.yaml 경로를 WebFetch 로 열어 원문을 읽고 sources[].fetched=true, fetched_via=github_raw, fetch_url 을 적는다. 입력에 원문 텍스트(data/source_texts)가 있는 출처는 fetched_via=inbox. 그 밖의 출처는 fetched=false 이며 코드가 신뢰도 상한(medium)을 강제한다 — 공통 규칙 0절 6항)
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

### runs/2026-09-26-01/target.json

```json
{
  "run_id": "2026-09-26-01",
  "date": "2026-09-26",
  "weekday": "Sat",
  "run_number": 91,
  "run_type": "weekly_review",
  "forced": true,
  "target": {
    "area_no": null,
    "area_name": null,
    "category": null
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
  "selection_rationale": "CLI 지정 run_type=weekly_review"
}
```

### runs/2026-09-26-01/research.json

```json
{
  "run_id": "2026-09-26-01",
  "date": "2026-09-26",
  "run_type": "weekly_review",
  "target": {
    "area_no": null,
    "area_name": null,
    "category": null
  },
  "gaps": [
    "url_check.json 오류 2건: ref-172(GitHub 위키, 미러 없음), ref-637(국가법령정보센터 한글 경로 URL)",
    "url_check.json 미러 오류 1건: ref-412(Open-RMF place.json)",
    "참고문헌 목록 중복 의심: ref-315·ref-709(같은 정책브리핑 보도자료), ref-584·ref-707·ref-767(같은 IEC 62443-3-3:2013)",
    "참고문헌 목록 번호 공백: ref-781~ref-791 미등록(보류 실행 산출물로 추정)"
  ],
  "research_questions": [
    "점검 대상 ref-172: https://github.com/nasa-jpl/rosa/wiki/Custom-Agents (url_check 오류, 미러 없음)",
    "점검 대상 ref-412: https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/place.json (정책 차단, 미러 오류)",
    "점검 대상 ref-637: https://www.law.go.kr/법령/산업디지털전환촉진법/(18692,20220104) (url_check 오류)",
    "점검 대상 참고문헌 중복 의심: ref-315·ref-709, ref-584·ref-707·ref-767",
    "점검 대상 내부 링크·각주: link_check.txt 통과(파일 1240개, 경고 0건) — 추가 조치 없음"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "ref-172(ROSA 위키 Custom Agents) 정규 URL 은 이 환경에서 미러가 없어 오류로 기록됐으나, GitHub 위키 원문 경로(raw.githubusercontent.com/wiki/nasa-jpl/rosa/Custom-Agents.md)는 오늘 기준 열리고 내용이 ROSA 를 다른 로봇에 맞게 도구·프롬프트로 사용자 정의하는 안내로 제목과 일치한다.",
      "tag": "사실",
      "source_ids": [
        "ref-172"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "raw 위키 원문의 절 제목 'Adding Tools', 새 클래스·인스턴스를 만들어 도구와 프롬프트로 ROSA 를 다른 로봇에 맞추는 방법을 설명한다.",
      "as_of": "2026-09-26",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "ref-412(Open-RMF rmf_ros2 place.json) 는 url_check 에서 미러 오류로 기록됐으나 오늘 raw 경로가 열리고 스키마 제목이 'Place Description' 으로 등록 제목과 일치해, 미러 오류는 일시적 실패로 보인다.",
      "tag": "사실",
      "source_ids": [
        "ref-412"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "스키마 title \"Place Description\", 설명 \"Description of a place that the robot can go to\"; 경유점 또는 경유점+선택적 방향을 받는다.",
      "as_of": "2026-09-26",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "ref-637 의 등록 URL 은 한글 경로가 퍼센트 인코딩되지 않은 형태여서 점검 스크립트에서 오류가 났으며, 같은 경로를 인코딩한 URL 이 검색 결과에 '산업디지털전환촉진법' 제목으로 나타나 문서 자체는 존재하는 것으로 확인된다.",
      "tag": "사실",
      "source_ids": [
        "ref-637"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 결과 URL: https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EC%82%B0%EC%97%85...(18692,20220104), 제목 '산업디지털전환촉진법'. 원문 미열람(정책 차단).",
      "as_of": "2026-09-26",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f4",
      "claim": "검색 결과에 국가법령정보센터 제목 '산업 디지털 전환 및 인공지능 활용 촉진법' 이 나타나고 같은 제명 변경을 담은 개정안 발의 보도가 있어, ref-637 이 가리키는 법률의 제명·현행 판이 바뀌었을 가능성이 있으나 시행 여부는 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-637"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "검색 요약: law.go.kr lsInfoP 제목 '산업 디지털 전환 및 인공지능 활용 촉진법'; 2025-10-01 시행판 링크 존재. 개정안은 현행법 제명 변경을 골자로 한다고 보도됨. 원문 미열람.",
      "as_of": "2026-09-26",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f5",
      "claim": "ref-315 와 ref-709 는 호스트만 다르고(www.korea.kr/briefing 과 korea.kr/news) 같은 보도자료 id(newsId=156480155)와 같은 제목을 가리켜 참고문헌 중복으로 보인다.",
      "tag": "사실",
      "source_ids": [
        "ref-315",
        "ref-709"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "두 항목 모두 제목 '국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다', newsId=156480155, 발행 2021-11. 참고문헌 목록 대조 결과.",
      "as_of": "2026-09-26",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f6",
      "claim": "ref-584(CSA 채택판, ANSI 웹스토어), ref-707(iTeh 샘플 PDF), ref-767(iTeh 카탈로그)은 모두 IEC 62443-3-3:2013 한 표준을 가리키는 서로 다른 URL 이어서 대표 출처 하나로 합칠 후보다.",
      "tag": "사실",
      "source_ids": [
        "ref-584",
        "ref-707",
        "ref-767"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "세 항목 제목이 모두 IEC 62443-3-3:2013(2013-08) System security requirements and security levels 이며 ref-584 는 CSA 채택판 표기. 참고문헌 목록 대조 결과.",
      "as_of": "2026-09-26",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    }
  ],
  "sources": [
    {
      "id": "ref-172",
      "org": "NASA Jet Propulsion Laboratory (nasa-jpl)",
      "title": "Custom Agents · nasa-jpl/rosa Wiki",
      "published": null,
      "url": "https://github.com/nasa-jpl/rosa/wiki/Custom-Agents",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-26",
      "summary": "ROSA 를 다른 로봇에 맞게 새 클래스·인스턴스를 만들고 도구·프롬프트로 사용자 정의하는 방법을 설명하는 공식 위키 문서.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/wiki/nasa-jpl/rosa/Custom-Agents.md",
      "source_unopened": false
    },
    {
      "id": "ref-412",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_ros2 — rmf_fleet_adapter/schemas/place.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/place.json",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-26",
      "summary": "로봇이 갈 수 있는 장소(경유점, 선택적 방향)를 기술하는 Open-RMF 작업 설명 JSON 스키마.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_ros2/main/rmf_fleet_adapter/schemas/place.json",
      "source_unopened": false
    },
    {
      "id": "ref-637",
      "org": "국가법령정보센터(산업통상자원부)",
      "title": "산업 디지털 전환 촉진법 (법률 제18692호)",
      "published": "2022-01-04",
      "url": "https://www.law.go.kr/법령/산업디지털전환촉진법/(18692,20220104)",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-26",
      "summary": "원문 미열람. 2022-01-04 공포된 산업 디지털 전환 촉진법 제정 법률 본문(국가법령정보센터).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-315",
      "org": "산업통상자원부 국가기술표준원(대한민국 정책브리핑)",
      "title": "국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다",
      "published": "2021-11",
      "url": "https://www.korea.kr/briefing/pressReleaseView.do?newsId=156480155",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-26",
      "summary": "원문 미열람. KS B 7317 제정을 알리는 국가기술표준원 보도자료.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-709",
      "org": "대한민국 정책브리핑(산업통상자원부 국가기술표준원)",
      "title": "국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다",
      "published": "2021-11-11",
      "url": "https://korea.kr/news/pressReleaseView.do?newsId=156480155",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-26",
      "summary": "원문 미열람. ref-315 와 같은 보도자료 id 를 가리키는 다른 경로의 URL.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-584",
      "org": "CSA / IEC (ANSI Webstore)",
      "title": "CAN/CSA IEC 62443-3-3-2017 - Industrial communication networks - Network and system security - Part 3-3: System security requirements and security levels (Adopted IEC 62443-3-3:2013, first edition, 2013-08)",
      "published": "2013-08",
      "url": "https://webstore.ansi.org/standards/csa/csaiec624432017-2442576",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-26",
      "summary": "원문 미열람. IEC 62443-3-3:2013 의 캐나다 채택판 판매 페이지.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-707",
      "org": "IEC",
      "title": "IEC 62443-3-3:2013 Industrial communication networks — Network and system security — Part 3-3: System security requirements and security levels (sample)",
      "published": "2013-08",
      "url": "https://cdn.standards.iteh.ai/samples/19488/7c0b753be32e46fc986c23c32efbdbe8/IEC-62443-3-3-2013.pdf",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-26",
      "summary": "원문 미열람. IEC 62443-3-3:2013 의 iTeh 샘플 PDF.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-767",
      "org": "IEC",
      "title": "IEC 62443-3-3:2013 Industrial communication networks — Network and system security — Part 3-3: System security requirements and security levels",
      "published": "2013-08",
      "url": "https://standards.iteh.ai/catalog/standards/iec/c32e05fe-78a2-467e-a24d-0fc422289f55/iec-62443-3-3-2013",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-26",
      "summary": "원문 미열람. IEC 62443-3-3:2013 의 iTeh 카탈로그 페이지.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/references/ref-637.md",
      "sections": [],
      "rationale": "needs_update 제안 (f3·f4): URL 을 퍼센트 인코딩 형태로 바꾸고, 제명이 '산업 디지털 전환 및 인공지능 활용 촉진법'으로 바뀌었는지 확인되면 현행 판 링크를 병기한다. 이 출처를 인용하는 28. 표준·상호운용성·다사업자 거버넌스 페이지의 제명 표기도 재확인 대상."
    },
    {
      "action": "update",
      "path": "docs/references/ref-709.md",
      "sections": [],
      "rationale": "deprecated 제안(대체 페이지·출처: docs/references/ref-315.md) (f5): 같은 보도자료 newsId=156480155 중복. 다음 실행 후보: ref-707·ref-767 을 ref-584 와 한 표준(IEC 62443-3-3:2013)으로 정리(f6), ref-172 를 config/source_mirrors.yaml 에 GitHub 위키 raw 경로로 등록(f1)."
    }
  ],
  "glossary_candidates": [],
  "open_questions_new": [
    "ref-637 이 가리키는 산업 디지털 전환 촉진법의 제명이 '산업 디지털 전환 및 인공지능 활용 촉진법'으로 바뀌어 시행되었는가, 바뀌었다면 데이터 공동 생성 규정의 조문 번호와 내용도 달라졌는가? | 관련 영역: 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f4 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 8,
    "cross_checked_count": 0,
    "unverified": [
      "f4 제명 변경 법률의 시행 여부·시행일 미확인(원문 정책 차단)",
      "ref-637 인코딩 URL 원문 미열람, 검색 결과 URL·제목 일치로만 확인",
      "f5·f6 중복 판단은 참고문헌 목록 대조이며 각 URL 원문 미열람"
    ],
    "scope_violations": [],
    "budget_used": {
      "queries": 2,
      "sources": 0
    },
    "limits": "주간 정리: 신규 조사 없음, 신규 출처 0건. web_fetch_available: false · fetch_mode mirror_only 로 정책 차단 797건은 링크 오류가 아니어서 다시 열지 않았고, url_check 의 오류·미러 실패 3건만 점검했다. ref-172 는 source_mirrors.yaml 에 없는 GitHub 위키 raw 경로(raw.githubusercontent.com/wiki/…)로 열렸다. ref-412 미러는 오늘 열림(일시 오류). ref-637 은 검색 2회로 URL 존재만 확인했다. 검색 중 제명 변경 가능성이 드러났으나 새 사실 조사는 하지 않고 열린 질문으로 보냈다. 페이지 제안은 갱신 상한 2건에 맞췄고 ref-707·ref-767 정리와 ref-172 미러 등록은 다음 실행 후보로 남겼다. 운영 참고(파이프라인): 참고문헌 번호 ref-781~ref-791 이 비어 있고, 보류 실행 2026-09-25-100 은 run_id 가 스키마 패턴(끝 두 자리)에 맞지 않아 2026-09-25-00 으로 기록됐으며 그 브리프의 ref-748~ref-750 은 현재 참고문헌 목록의 같은 id(JSON Schema 계열)와 다른 문헌을 가리켜 재게시 시 id 재부여가 필요하다. 이전 주간 정리 2026-09-25-87 도 보류 상태다. link_check 는 통과(경고 0건)."
  }
}
```

### runs/2026-09-26-01/verification.json

```json
{
  "run_id": "2026-09-26-01",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 검증자가 raw.githubusercontent.com/wiki/nasa-jpl/rosa/Custom-Agents.md 를 직접 열었다(github_raw, 원문 열람). 'Adding Tools' 절이 있고, ROSA 를 상속한 새 클래스 또는 새 인스턴스를 만든 뒤 도구·RobotSystemPrompts 로 사용자 정의하는 방법을 설명한다. 등록 제목과 일치한다. 이 raw 위키 경로는 config/source_mirrors.yaml 에 없다. 미러 등록은 다음 실행 후보로 둔다. 출처 상태에 관한 단일 출처 진술이다."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 검증자가 raw 경로를 직접 열었다. 스키마 title 'Place Description', description 'Description of a place that the robot can go to' 이고, 경유점(문자열 또는 음이 아닌 정수) 또는 경유점과 선택적 orientation 을 받는다. 등록 제목과 일치한다. 다만 '미러 오류는 일시적 실패'라는 부분은 오늘 열렸다는 관찰에서 나온 추론이므로 [추정]으로 나눠 쓴다(required_fixes)."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(원문 미열람, 검색 결과 일치): 검증 검색에서 퍼센트 인코딩된 law.go.kr URL(…/법령/산업디지털전환촉진법/(18692,20220104))이 제목 '산업디지털전환촉진법'으로 나타났다. 제정·개정문 페이지와 법률사무소 뉴스레터(법률 제18692호, 2022-01-04 공포)도 검색됐다. 등록 URL 은 비인코딩 한글 경로라서 점검 스크립트 오류가 난 것으로 판단된다. 발행일 2022-01-04 는 일치한다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람. 검증 검색에서 국가법령정보센터의 '산업 디지털 전환 및 인공지능 활용 촉진법' 제정·개정문 페이지(lsiSeq=281883)가 검색됐다. 개정안(대안)과 '지난 7월 시행'을 전하는 기사 요약도 보였다. 제명 변경 가능성은 뒷받침되지만 시행일·조문은 원문으로 확인하지 못했으므로 [추정]·low 를 유지한다. 주간 정리의 신규 조사 금지에 비춰 보면, 이 finding 은 등록 출처(ref-637)의 변경 여부에 관한 점검 결과로만 인정한다. 현행 판 링크 병기나 제명 교체는 이번 실행에서 하지 않는다. 기존 oq-109 가 같은 법률의 공동 생성 규정을 다루므로 새 열린 질문과 서로 연결한다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(참고문헌 목록 대조, 원문 미열람): ref-315(www.korea.kr/briefing/…)와 ref-709(korea.kr/news/…)는 같은 newsId=156480155 이고 제목이 같다. 두 항목의 발행일 표기(2021-11 대 2021-11-11)와 기관 표기 순서만 다르다. 중복 판단은 적정하다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(참고문헌 목록 대조, 원문 미열람): 세 항목은 모두 IEC 62443-3-3:2013(2013-08)을 가리킨다. 다만 ref-584 는 CAN/CSA IEC 62443-3-3-2017(캐나다 채택판) 판매 페이지이므로 IEC 원판과 같은 문서는 아니다. 합칠 때 '채택판' 구분을 남겨야 한다. finding 이 '합칠 후보'로 표현했으므로 [사실]을 유지한다. 정리는 다음 실행 후보로 둔다."
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
      "f4 와 새 열린 질문(산업 디지털 전환 촉진법 제명 변경)은 기존 oq-109(같은 법의 데이터 공동 생성 규정에 따른 권리 배분)와 대상 법률이 같다. 질문 내용은 다르므로 중복이 아니며, 두 질문을 서로 연결한다",
      "f5: ref-315 와 ref-709 는 같은 보도자료를 가리키는 중복 참고문헌이다(ref-709 deprecated 제안)",
      "f6: ref-584·ref-707·ref-767 은 같은 표준 IEC 62443-3-3:2013 을 가리킨다(정리는 다음 실행)"
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
    "docs/references/ref-637.md(f3·f4): URL 만 퍼센트 인코딩 형태(https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EC%82%B0%EC%97%85%EB%94%94%EC%A7%80%ED%84%B8%EC%A0%84%ED%99%98%EC%B4%89%EC%A7%84%EB%B2%95/(18692,20220104))로 바꾸고 제목·법률 번호·발행일 2022-01-04 는 유지한다. 상태는 needs_update 로 둔다. 제명이 '산업 디지털 전환 및 인공지능 활용 촉진법'으로 바뀌었다는 내용은 [추정]·원문 미열람으로만 적고, 현행 판 링크 병기나 제목 교체는 하지 않는다. 이유: 시행 여부와 조문을 원문으로 확인하지 못했다(f4).",
    "docs/references/ref-709.md(f5): status 를 deprecated 로 바꾸고, 상태 줄 아래에 '> 대체 페이지: [ref-315](ref-315.md)' 줄을 둔다. 페이지는 지우지 않는다. 이번 실행에서는 ref-709 를 인용한 페이지(28. 표준·상호운용성·다사업자 거버넌스 등)의 각주를 고치지 않는다. 이유: 갱신 상한이 2건이고 link_check 를 통과한 링크를 유지해야 한다.",
    "f1·f6 은 다음 실행 후보로만 기록한다. 이번 실행에서 ref-584·ref-707·ref-767 참고문헌 페이지와 config/source_mirrors.yaml 을 고치지 않는다. 주간 정리 페이지에 후보로 적을 때 ref-584 는 CSA 채택판(CAN/CSA IEC 62443-3-3-2017)이어서 IEC 원판과 구분해 정리해야 한다는 점을 함께 적는다.",
    "f2: 주간 정리 페이지에서 ref-412 는 '오늘 raw 경로가 열리고 제목이 일치한다'를 [사실]로, '미러 오류는 일시적 실패로 보인다'를 [추정]으로 나눠 쓴다. ref-412 참고문헌 페이지는 고치지 않는다.",
    "각주·참고문헌 표시: ref-637·ref-315·ref-709·ref-584·ref-707·ref-767 의 각주 정의는 접근일 뒤에 ' (원문 미열람)'을 붙이고, reference_updates 의 ref-637·ref-709 항목에 source_unopened: true 를 넣는다. ref-172·ref-412 는 github_raw 로 원문을 열었으므로 이 표시를 붙이지 않는다.",
    "주간 정리 페이지(docs/logs/weekly/2026-W39.md) 6. 링크·출처 유효성 점검: url_check 건수(정책 차단 797건은 네트워크 정책 때문이며 링크 오류가 아니다, 미러 열림 144건, 오류 2건, 미러 오류 1건)와 세 건의 점검 결과, link_check 통과(파일 1240개, 경고 0건)를 적는다. 3. 강등·폐기된 주장에는 ref-709 deprecated(대체 ref-315)를 적는다.",
    "주간 정리 페이지 4. 열린 질문 변동: 새 열린 질문(산업 디지털 전환 촉진법 제명 변경, 관련 영역 28. 표준·상호운용성·다사업자 거버넌스, 근거 f4, 종류 일반)을 다음 순번 id 로 등록한다. 질문 끝에 '(관련 기존 질문: oq-109)'를 붙인다.",
    "주간 정리 페이지 1·5절 운영 기록: 이번 주 실행 요약에 나온 보류 실행(2026-09-25-06, 2026-09-25-12, 2026-09-25-87, 2026-09-25-100)과 퍼블리셔 중단 실행(2026-09-25-08, 2026-09-25-18, 2026-09-25-43, 2026-09-25-49)을 id 로 적는다. 브리프 한계 항목의 운영 참고는 사실 태그 없이 운영 메모로 적는다: 보류 실행 2026-09-25-100 이 run_id 패턴 때문에 2026-09-25-00 으로 기록된 점, 그 브리프의 ref-748~ref-750 이 현재 참고문헌의 같은 id(JSON Schema 계열)와 다른 문헌이어서 재게시할 때 id 를 다시 부여해야 하는 점, 참고문헌 번호 ref-781~ref-791 이 비어 있는 점. 이 내용을 위키 본문의 사실 주장으로 쓰지 않는다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 1차 조건부 승인. 이번 실행은 원문 열람이 차단된 환경에서 검증됐다(fetch_mode mirror_only). ref-172(ROSA 위키)와 ref-412(Open-RMF place.json)는 검증자가 raw.githubusercontent.com 으로 직접 열어 제목·내용이 일치함을 확인했다. ref-637 은 검색 결과가 일치하는지로 확인했다. 검증 검색은 2회로, 리서치와 합쳐 4/30 이다. 확인 6건, 미확인 0건, 교차 확인 0건. 강등: 없음(f2 의 '일시적 실패' 부분만 [추정]으로 나눔). 원문 미열람 출처: ref-637, ref-315, ref-709, ref-584, ref-707, ref-767. 처리: ref-637 은 URL 인코딩 교정과 needs_update, ref-709 는 deprecated(대체 ref-315)로 처리한다. ref-584·ref-707·ref-767 통합과 ref-172 미러 등록은 다음 실행 후보다. 주의: 검증 검색에서 '산업 디지털 전환 및 인공지능 활용 촉진법' 제정·개정문 페이지와 시행 보도가 보였다. 그러나 원문을 열지 못해 제명 변경과 시행 여부는 [추정]으로 두고 열린 질문(관련: oq-109)으로 보낸다. ref-584 는 IEC 원판이 아니라 CSA 채택판이다. 운영: 보류 실행 2026-09-25-100 의 참고문헌 id(ref-748~ref-750)가 게시된 참고문헌과 겹친다. 참고문헌 번호 ref-781~ref-791 은 비어 있다. 정정 요청은 없다.",
  "retry_reason": null
}
```

### runs/2026-09-26-01/pages.json

```json
{
  "run_id": "2026-09-26-01",
  "outline": [
    {
      "path": "docs/logs/weekly/2026-W39.md",
      "section": "1. 이번 주 다룬 영역",
      "budget_chars": 4500,
      "summary": "이번 주 실행 90회를 유형별로 정리한다(영역 심화 30, 트랙 49, 대분류 연결 8, 주제 조사 1, 갱신 1, 주간 정리 1). 보류 4회, 퍼블리셔 중단 4회는 id 로 적는다.",
      "planned_findings": []
    },
    {
      "path": "docs/logs/weekly/2026-W39.md",
      "section": "2. 새로 확인된 사실",
      "budget_chars": 1500,
      "summary": "이번 주 [사실]로 게시된 주장이 실린 페이지를 안내하고, 교차 확인이 적다는 공통 한계를 적는다.",
      "planned_findings": []
    },
    {
      "path": "docs/logs/weekly/2026-W39.md",
      "section": "3. 강등·폐기된 주장",
      "budget_chars": 3500,
      "summary": "게시된 실행의 검증 노트에 기록된 강등·삭제를 실행 id 와 finding id 로 모으고, ref-709 deprecated(대체 ref-315)를 적는다.",
      "planned_findings": [
        "f5"
      ]
    },
    {
      "path": "docs/logs/weekly/2026-W39.md",
      "section": "4. 열린 질문 변동",
      "budget_chars": 900,
      "summary": "oq-001~oq-121 이 새로 열렸고 해결·보류는 없다. 산업 디지털 전환 촉진법 제명 변경 질문을 새로 올린다.",
      "planned_findings": [
        "f4"
      ]
    },
    {
      "path": "docs/logs/weekly/2026-W39.md",
      "section": "5. 다음 주 후보",
      "budget_chars": 1200,
      "summary": "참고문헌 정리 후보(ref-584·ref-707·ref-767, ref-172 미러 등록)와 보류 실행 재처리, 운영 메모를 적는다.",
      "planned_findings": [
        "f1",
        "f6"
      ]
    },
    {
      "path": "docs/logs/weekly/2026-W39.md",
      "section": "6. 링크·출처 유효성 점검",
      "budget_chars": 1600,
      "summary": "url_check 건수와 오류 3건의 점검 결과, link_check 통과를 적는다.",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f5",
        "f6"
      ]
    },
    {
      "path": "docs/logs/weekly/2026-W39.md",
      "section": "7. 용어집 정리",
      "budget_chars": 500,
      "summary": "용어 205개 가운데 draft 10개를 적고 이번 주 용어 추가 제안은 없다.",
      "planned_findings": []
    }
  ],
  "pages": [
    {
      "path": "docs/logs/weekly/2026-W39.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "2026-W39 주간 정리 신규 작성(실행 90회 정리, 링크·출처 점검 3건, 참고문헌 중복 2묶음)"
    },
    {
      "path": "docs/references/ref-637.md",
      "action": "update",
      "status": "needs_update",
      "diff_summary": "각주 형식 절에 퍼센트 인코딩 URL 을 적고 제명 변경 가능성을 [추정]·원문 미열람으로 병기, needs_update (등록 URL 교체는 pipeline 담당 요청)"
    },
    {
      "path": "docs/references/ref-709.md",
      "action": "update",
      "status": "deprecated",
      "diff_summary": "ref-315 와 같은 보도자료를 가리키는 중복 항목으로 deprecated 처리, 대체 페이지 ref-315(프런트매터 replaced_by 추가)"
    }
  ],
  "changelog_entry": "2026-09-26 | 주간 정리 2026-W39 | 이번 주 실행 90회 정리, ref-637 URL 인코딩 표기·needs_update, ref-709 deprecated(대체 ref-315), 참고문헌 중복 후보 기록 | run 2026-09-26-01",
  "index_updates": {
    "home_recent": "2026-09-26 — 주간 정리 2026-W39: 실행 90회(게시 82, 보류 4, 중단 4) 정리, 세부영역 28개 심화와 대분류 연결 7개 완료, 참고문헌 점검 3건(ref-637 각주 URL 인코딩 표기·needs_update, ref-709 중복 폐기)",
    "category_recent": "2026-09-26 — 주간 정리 2026-W39: 이번 주 세부영역 심화·대분류 연결 결과 정리, 28. 표준·상호운용성·다사업자 거버넌스가 인용하는 ref-637 은 재확인 대상(needs_update)"
  },
  "glossary_updates": [],
  "reference_updates": [
    {
      "id": "ref-172",
      "org": "NASA Jet Propulsion Laboratory (nasa-jpl)",
      "title": "Custom Agents · nasa-jpl/rosa Wiki",
      "published": null,
      "url": "https://github.com/nasa-jpl/rosa/wiki/Custom-Agents",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-26",
      "summary": "ROSA 를 다른 로봇에 맞게 새 클래스·인스턴스를 만들고 도구·프롬프트로 사용자 정의하는 방법을 설명하는 공식 위키 문서. GitHub 위키 raw 경로로 원문을 열었다.",
      "source_unopened": false,
      "cited_by": [
        "docs/logs/weekly/2026-W39.md"
      ]
    },
    {
      "id": "ref-412",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_ros2 — rmf_fleet_adapter/schemas/place.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/place.json",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-26",
      "summary": "로봇이 갈 수 있는 장소(경유점, 선택적 방향)를 기술하는 Open-RMF 작업 설명 JSON 스키마.",
      "source_unopened": false,
      "cited_by": [
        "docs/logs/weekly/2026-W39.md"
      ]
    },
    {
      "id": "ref-637",
      "org": "국가법령정보센터(산업통상자원부)",
      "title": "산업 디지털 전환 촉진법 (법률 제18692호)",
      "published": "2022-01-04",
      "url": "https://www.law.go.kr/법령/산업디지털전환촉진법/(18692,20220104)",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-26",
      "summary": "원문 미열람. 2022-01-04 공포된 산업 디지털 전환 촉진법 제정 법률 본문(국가법령정보센터). 퍼센트 인코딩 URL 은 각주 형식 줄에만 적었고 등록 URL 교체는 pipeline 담당 요청 사항이다. 제명 변경 여부는 미확인이다.",
      "source_unopened": true,
      "cited_by": [
        "docs/logs/weekly/2026-W39.md",
        "docs/references/ref-637.md"
      ]
    },
    {
      "id": "ref-315",
      "org": "산업통상자원부 국가기술표준원(대한민국 정책브리핑)",
      "title": "국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다",
      "published": "2021-11",
      "url": "https://www.korea.kr/briefing/pressReleaseView.do?newsId=156480155",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-26",
      "summary": "원문 미열람. KS B 7317 제정을 알리는 국가기술표준원 보도자료. ref-709 의 대체 항목.",
      "source_unopened": true,
      "cited_by": [
        "docs/logs/weekly/2026-W39.md"
      ]
    },
    {
      "id": "ref-709",
      "org": "대한민국 정책브리핑(산업통상자원부 국가기술표준원)",
      "title": "국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다",
      "published": "2021-11-11",
      "url": "https://korea.kr/news/pressReleaseView.do?newsId=156480155",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-26",
      "summary": "원문 미열람. ref-315 와 같은 보도자료 id 를 가리키는 다른 경로의 URL. 중복으로 deprecated, 대체 ref-315.",
      "source_unopened": true,
      "cited_by": [
        "docs/logs/weekly/2026-W39.md",
        "docs/references/ref-709.md"
      ]
    },
    {
      "id": "ref-584",
      "org": "CSA / IEC (ANSI Webstore)",
      "title": "CAN/CSA IEC 62443-3-3-2017 - Industrial communication networks - Network and system security - Part 3-3: System security requirements and security levels (Adopted IEC 62443-3-3:2013, first edition, 2013-08)",
      "published": "2013-08",
      "url": "https://webstore.ansi.org/standards/csa/csaiec624432017-2442576",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-26",
      "summary": "원문 미열람. IEC 62443-3-3:2013 의 캐나다 채택판 판매 페이지(IEC 원판과 구분).",
      "source_unopened": true,
      "cited_by": [
        "docs/logs/weekly/2026-W39.md"
      ]
    },
    {
      "id": "ref-707",
      "org": "IEC",
      "title": "IEC 62443-3-3:2013 Industrial communication networks — Network and system security — Part 3-3: System security requirements and security levels (sample)",
      "published": "2013-08",
      "url": "https://cdn.standards.iteh.ai/samples/19488/7c0b753be32e46fc986c23c32efbdbe8/IEC-62443-3-3-2013.pdf",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-26",
      "summary": "원문 미열람. IEC 62443-3-3:2013 의 iTeh 샘플 PDF.",
      "source_unopened": true,
      "cited_by": [
        "docs/logs/weekly/2026-W39.md"
      ]
    },
    {
      "id": "ref-767",
      "org": "IEC",
      "title": "IEC 62443-3-3:2013 Industrial communication networks — Network and system security — Part 3-3: System security requirements and security levels",
      "published": "2013-08",
      "url": "https://standards.iteh.ai/catalog/standards/iec/c32e05fe-78a2-467e-a24d-0fc422289f55/iec-62443-3-3-2013",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-26",
      "summary": "원문 미열람. IEC 62443-3-3:2013 의 iTeh 카탈로그 페이지.",
      "source_unopened": true,
      "cited_by": [
        "docs/logs/weekly/2026-W39.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "산업 디지털 전환 촉진법의 제명이 '산업 디지털 전환 및 인공지능 활용 촉진법'으로 바뀌어 시행되었는가, 바뀌었다면 데이터 공동 생성 규정의 조문 번호와 내용도 달라졌는가? (관련 기존 질문: oq-109)",
      "areas": [
        28
      ],
      "status": "열림",
      "link": null
    }
  ],
  "flow_matrix_updates": [],
  "additional_research_requests": [
    "ref-637: '산업 디지털 전환 및 인공지능 활용 촉진법' 으로의 제명 변경 여부와 시행일, 데이터 공동 생성 규정의 조문 변화를 국가법령정보센터 원문으로 확인해야 한다. 확인되면 ref-637 의 현행 판 링크 병기와 28. 표준·상호운용성·다사업자 거버넌스 페이지의 제명 표기를 재확인한다.",
    "ref-637 의 등록 URL(data/references 와 참고문헌 페이지 프런트매터 url·서지 정보 표)을 퍼센트 인코딩 형태(https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EC%82%B0%EC%97%85%EB%94%94%EC%A7%80%ED%84%B8%EC%A0%84%ED%99%98%EC%B4%89%EC%A7%84%EB%B2%95/(18692,20220104))로 바꾸는 작업은 pipeline 담당에게 요청한다. 퍼블리셔가 reference_updates 의 URL 변경을 '참고문헌 id 충돌'로 반려하므로 기존 id 의 URL 교정 경로가 필요하다.",
    "ref-584·ref-707·ref-767 을 IEC 62443-3-3:2013 대표 출처 하나로 정리하는 갱신(ref-584 는 CSA 채택판이라 구분 유지). 이번 실행은 갱신 상한으로 미뤘다.",
    "ref-172 의 GitHub 위키 raw 경로(raw.githubusercontent.com/wiki/nasa-jpl/rosa/Custom-Agents.md)를 config/source_mirrors.yaml 에 등록하도록 pipeline 담당에게 요청한다.",
    "ref-709 를 인용한 페이지(28. 표준·상호운용성·다사업자 거버넌스 등)의 각주를 ref-315 로 바꾸는 갱신. 이번 실행은 갱신 상한으로 미뤘다.",
    "ref-709 프런트매터 replaced_by 값의 형식(페이지 기준 상대 경로 'ref-315.md' 로 넣었다)이 validate_run.py 가 기대하는 형식과 다르면 pipeline 담당이 형식을 알려 주어야 한다.",
    "다음 주간 정리에서 표준 목록 중복 항목 점검(docs/standards/index.md 에 같은 표준·오픈소스가 판 표기만 달리해 두 번 이상 실린 것으로 보이는 항목의 확인과 정리).",
    "참고문헌 페이지 갱신 형식: 이번 재실행은 반환 스키마($defs/returned 의 content 필수)와 '(content 와 patches 는 하나만)' 반려를 함께 만족시키려고 ref-637·ref-709 를 patches 대신 전체 content 로 보냈다. 기존 페이지 갱신에 patches 만 보내도 되는지 pipeline 담당이 반환 스키마를 정리해 주어야 한다."
  ],
  "fixes_applied": [
    "docs/references/ref-637.md(f3·f4) — 각주 형식 절에서 URL 을 지시한 퍼센트 인코딩 형태로 적었다. 제목·법률 번호·발행일 2022-01-04 는 유지했고 status 는 needs_update 로 두었다. 제명 변경은 [추정]·원문 미열람으로만 적었고, 현행 판 링크 병기와 제목 교체는 하지 않았다.",
    "docs/references/ref-709.md(f5) — status 를 deprecated 로 바꾸고 '> 대체 페이지: [ref-315](ref-315.md)' 줄을 두었으며, 형식 검증 요구에 따라 프런트매터 replaced_by 에 ref-315.md 를 넣었다. 페이지는 지우지 않았고 ref-709 를 인용한 다른 페이지의 각주는 고치지 않았다.",
    "f1·f6 — 주간 정리 5절에 다음 실행 후보로만 적었고, ref-584 는 CSA 채택판(CAN/CSA IEC 62443-3-3-2017)이라 IEC 원판과 구분해 정리해야 한다는 점을 함께 적었다. ref-584·ref-707·ref-767 참고문헌 페이지와 config/source_mirrors.yaml 은 고치지 않았다.",
    "f2 — 주간 정리 6절에서 '오늘 raw 경로가 열리고 제목이 일치한다'를 [사실], '미러 오류는 일시적 실패로 보인다'를 [추정]으로 나눠 썼다. ref-412 참고문헌 페이지는 고치지 않았다.",
    "각주·참고문헌 표시 — ref-637·ref-315·ref-709·ref-584·ref-707·ref-767 의 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙였다. reference_updates 의 ref-637·ref-709(및 나머지 미열람 네 건)에 source_unopened: true 를 넣었다. ref-172·ref-412 에는 이 표시를 붙이지 않았다.",
    "주간 정리 6절 — url_check 건수(정책 차단 797건은 네트워크 정책이며 링크 오류가 아님, 미러 열림 144건, 오류 2건, 미러 오류 1건), 세 건의 점검 결과, link_check 통과(파일 1240개, 경고 0건)를 적었다. 3절 끝에 ref-709 deprecated(대체 ref-315)를 적었다.",
    "주간 정리 4절 — 새 열린 질문(산업 디지털 전환 촉진법 제명 변경, 관련 영역 28. 표준·상호운용성·다사업자 거버넌스, 근거 f4, 종류 일반)을 다음 순번 id 로 등록하도록 적었다. 질문 끝에 '(관련 기존 질문: oq-109)'를 붙였고, open_question_updates 에 new 로 냈다.",
    "주간 정리 1·5절 — 1절 운영 기록에 보류 실행(2026-09-25-06, -12, -87, -100)과 퍼블리셔 중단 실행(2026-09-25-08, -18, -43, -49)을 id 로 적었다. 5절에는 2026-09-25-100 의 run_id 기록 문제, ref-748~ref-750 id 재부여 필요, ref-781~ref-791 공백을 사실 태그 없는 운영 메모로 적었다.",
    "2차: docs/references/ref-637.md 각주 형식 절 첫 문장을 'URL 을 퍼센트 인코딩 형태로 적은 것은 이 절의 각주 형식 줄뿐이다. 등록 URL(프런트매터 url, 서지 정보 표) 교체는 pipeline 담당에게 요청했으며 아직 반영되지 않았다.'로 고쳤다. 뒤 [사실] 문장과 [추정] 문단은 그대로 두었다.",
    "2차: docs/logs/weekly/2026-W39.md 6절 3번 항목의 처리 문장을 '이번 실행에서는 참고문헌 페이지의 각주 형식과 이 페이지 각주에만 인코딩 URL 을 적었다. 등록 URL 교체는 pipeline 담당에게 요청했다. 제목·법률 번호·발행일은 유지했다.'로 고치고, 표의 ref-637 조치 칸을 '각주 URL 인코딩 표기, needs_update(등록 URL 교체 요청)'로 고쳤다.",
    "2차: index_updates.home_recent 의 '(ref-637 URL 교정, …)'를 '(ref-637 각주 URL 인코딩 표기·needs_update, …)'로 고쳤다. changelog_entry 는 그대로 두었다.",
    "2차: docs/logs/weekly/2026-W39.md 6절 끝의 표준 목록 중복 운영 메모를 삭제하고 additional_research_requests 에 '다음 주간 정리에서 표준 목록 중복 항목 점검'으로 옮겼다.",
    "2차(스키마 불일치): ref-637·ref-709 페이지에 content 와 patches 를 함께 보낸 오류를 고쳐, 반환 스키마의 content 필수 조건에 맞게 patches 를 빼고 패치를 적용한 전체 content 만 보냈다. 내용은 위 2차 수정 외에 바꾸지 않았다."
  ]
}
```

### runs/2026-09-26-01/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
```

### runs/2026-09-26-01/pages/logs/weekly/2026-W39.md

```markdown
---
title: "2026-W39 주간 정리"
type: log
status: draft
created: 2026-09-26
updated: 2026-09-26
version: 1
tags: [weekly_review]
sources: [ref-172, ref-412, ref-637, ref-315, ref-709, ref-584, ref-707, ref-767]
---

[홈](../../index.md) › [로그](../index.md) › 2026-W39 주간 정리

# 2026-W39 주간 정리

이 페이지는 2026-W39(2026-09-21 ~ 2026-09-27)에 돈 실행 90회의 산출물(runs/)과 실행 2026-09-26-01 의 점검 결과를 정리한다. 새 조사는 하지 않았다. 참고문헌 상태를 점검한 결과만 태그와 각주를 붙여 적는다.

## 1. 이번 주 다룬 영역

실행 90회의 유형별 건수다. 영역 심화 30회, 트랙 49회, 대분류 연결 8회, 주제 조사 1회, 갱신 1회, 주간 정리 1회다. 82회가 게시됐고, 4회는 보류(runs/parked/), 4회는 퍼블리셔 단계에서 중단됐다.

**영역 심화(area_deep_dive)** — 28개 세부영역 모두 이번 주에 게시된 심화 실행이 하나 이상 있다.

| 실행 id | 대상 | 판정(1차 / 2차) | 신뢰도 | 결과 |
|---|---|---|---|---|
| 2026-09-25-01 | [7. 화물·재고·자산 식별과 추적](../../categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) | 조건부 승인 / 통과 | medium | 게시 |
| 2026-09-25-08 | 1. 주문·업무 시스템 연계 | 조건부 승인 / 통과 | medium | 중단(사이트 빌드 실패). 2026-09-25-13 에서 게시 |
| 2026-09-25-09 | [2. 공정·워크플로 모델링](../../categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md) | 조건부 승인 / 통과 | medium | 게시 |
| 2026-09-25-10 | [3. 처리능력·거점·설비 계획](../../categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md) | 조건부 승인 / 통과 | medium | 게시 |
| 2026-09-25-13 | [1. 주문·업무 시스템 연계](../../categories/a-business-supply-chain-design/01-order-and-business-system-integration.md) | 조건부 승인 / 통과 | medium | 게시 |
| 2026-09-25-14 | [4. 성과·경제성·프로세스 개선](../../categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) | 조건부 승인 / 통과 | medium | 게시 |
| 2026-09-25-15 | [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) | 조건부 승인 / 통과 | medium | 게시 |
| 2026-09-25-17 | [6. 지도·공간·위치 모델](../../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md) | 조건부 승인 / 통과 | medium | 게시 |
| 2026-09-25-18 | 8. 실시간 세계 상태·데이터 일관성 | 조건부 승인 / 통과 | low | 중단(내부 링크·각주 검사 실패). 2026-09-25-24 에서 게시 |
| 2026-09-25-20 | [9. 로봇·제조사 관제 연동](../../categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | 조건부 승인 / 통과 | medium | 게시 |
| 2026-09-25-24 | [8. 실시간 세계 상태·데이터 일관성](../../categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md) | 조건부 승인 / 통과 | low | 게시 |
| 2026-09-25-25 | [10. 설비·건물 시스템 연동](../../categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md) | 조건부 승인 / 통과 | medium | 게시 |
| 2026-09-25-27 | [11. 분산 시스템·통신·컴퓨팅 구조](../../categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md) | 조건부 승인 / 통과 | low | 게시 |
| 2026-09-25-31 | [12. 명령·작업 실행의 신뢰성](../../categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md) | 조건부 승인 / 통과 | medium | 게시 |
| 2026-09-25-33 | [13. 작업 배정 — MRTA](../../categories/d-planning-and-optimization/13-task-allocation-mrta.md) | 조건부 승인 / 통과 | medium | 게시 |
| 2026-09-25-34 | [14. 작업 순서·스케줄링](../../categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md) | 조건부 승인 / 통과 | medium | 게시 |
| 2026-09-25-39 | [15. 다중 로봇 경로·교통 관리 — MAPF](../../categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md) | 조건부 승인 / 통과 | medium | 게시 |
| 2026-09-25-40 | [16. 공용 자원·충전·에너지 최적화](../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) | 조건부 승인 / 통과 | medium | 게시 |
| 2026-09-25-42 | [17. 로봇 간 협업·물리적 인계](../../categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md) | 조건부 승인 / 통과 | medium | 게시 |
| 2026-09-25-46 | [18. 사람–로봇 협업·운영 인터페이스](../../categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) | 조건부 승인 / 통과 | medium | 게시 |
| 2026-09-25-48 | [19. 모니터링·이상 탐지·원인 분석](../../categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md) | 조건부 승인 / 통과 | low | 게시 |
| 2026-09-25-50 | [20. 예외 복구·재계획·업무 연속성](../../categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) | 조건부 승인 / 통과 | medium | 게시 |
| 2026-09-25-52 | [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) | 조건부 승인 / 통과 | medium | 게시 |
| 2026-09-25-56 | [22. 시뮬레이션·예측용 디지털 트윈](../../categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) | 조건부 승인 / 통과 | medium | 게시 |
| 2026-09-25-59 | [23. 시험·형식 검증·벤치마크](../../categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) | 조건부 승인 / 통과 | medium | 게시 |
| 2026-09-25-61 | [24. 자산·소프트웨어 수명주기 관리](../../categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) | 조건부 승인 / 통과 | medium | 게시 |
| 2026-09-25-63 | [25. 안전·위험 관리](../../categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md) | 조건부 승인 / 통과 | medium | 게시 |
| 2026-09-25-64 | [26. 사이버보안·접근권한·개인정보](../../categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md) | 조건부 승인 / 통과 | medium | 게시 |
| 2026-09-25-68 | [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) | 조건부 승인 / 통과 | medium | 게시 |
| 2026-09-25-69 | [28. 표준·상호운용성·다사업자 거버넌스](../../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | 조건부 승인 / 통과 | medium | 게시 |

**주제 조사·갱신** — 2026-09-25-03(주제 조사, 7. 화물·재고·자산 식별과 추적, [EPCIS 이벤트 설계 주제 페이지](../../topics/2026/2026-09-25-epcis-event-design-for-robot-handover.md))과 2026-09-25-07(갱신, 7. 화물·재고·자산 식별과 추적)이 모두 조건부 승인 / 통과, 신뢰도 medium 으로 게시됐다.

**대분류 연결(category_link)** — 일곱 대분류의 "다른 대분류와의 연결" 절이 모두 채워졌다. 판정은 모두 조건부 승인 / 통과, 신뢰도 medium 이다.

| 실행 id | 대상 | 결과 |
|---|---|---|
| 2026-09-25-29 | [A. 업무·공급망 설계](../../categories/a-business-supply-chain-design/index.md) | 게시 |
| 2026-09-25-32 | [B. 공통 정보·환경 모델](../../categories/b-common-information-and-environment-model/index.md) | 게시 |
| 2026-09-25-38 | [C. 연결·실행 기반](../../categories/c-connectivity-and-execution-foundation/index.md) | 게시 |
| 2026-09-25-49 | D. 계획·최적화 | 중단(내부 링크·각주 검사 실패). 2026-09-25-55 에서 게시 |
| 2026-09-25-55 | [D. 계획·최적화](../../categories/d-planning-and-optimization/index.md) | 게시 |
| 2026-09-25-60 | [E. 협업·현장 운영](../../categories/e-collaboration-and-field-operations/index.md) | 게시 |
| 2026-09-25-67 | [F. 도입·검증·유지관리](../../categories/f-deployment-verification-and-maintenance/index.md) | 게시 |
| 2026-09-25-73 | [G. 안전·보안·지능·거버넌스](../../categories/g-safety-security-intelligence-and-governance/index.md) | 게시 |

**트랙(track)** — 세 트랙에서 49회가 돌았다. 판정은 모두 1차 조건부 승인이다.

| 트랙 | 실행 id(단계, 질문) | 결과 |
|---|---|---|
| [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) | 2026-09-25-02(단계 1, q1-01~q1-03), -06(단계 1, q1-03~q1-05), -16(단계 1, q1-03~q1-05), -23(단계 1, q1-03·q1-06·q1-07), -35(단계 1, q1-08·q1-09), -41·-45·-47·-53(단계 1, q1-09), -57(단계 2, q2-01~q2-03) | 10회 중 9회 게시, 2026-09-25-06 보류. 신뢰도는 -57 만 low, 나머지 medium |
| [자연어 업무 지시 챗봇](../../tracks/nl-task-chatbot/index.md) | 단계 1: -04(q1-01), -12·-21(q1-02), -26(q1-03), -30(q1-04) / 단계 2: -37(q2-01), -43·-51(q2-02), -62(q2-03) / 단계 3: -66(q3-01), -71(q3-02), -74(q3-03), -77(q3-04) / 단계 4: -79(q4-01), -81(q4-02), -83(q4-03), -85(q4-04) / 단계 5: -86(q5-03), -98(q5-01), -99(q5-02), -100(q5-03) | 21회 중 18회 게시, -12·-100 보류, -43 중단(-51 에서 게시). 신뢰도는 -04·-21 medium, 나머지 low |
| [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) | 단계 1: -05(q1-01), -11(q1-02), -19(q1-03), -22(q1-04) / 단계 2: -28(q2-01), -36(q2-02), -44(q2-03) / 단계 3: -54(q3-01), -58(q3-02), -65(q3-03), -70(q3-04) / 단계 4: -72(q4-01), -75(q4-02), -76(q4-03), -78(q4-04) / 단계 5: -80(q5-01), -82(q5-02), -84(q5-03) | 18회 모두 게시. 신뢰도는 단계 1·2 medium, 단계 3 이후 low |

**주간 정리** — 2026-09-25-87(주간 정리, 대상 전체)은 판정 없이 보류됐다.

**운영 기록(보류·중단 실행)**

- 보류(runs/parked/): 2026-09-25-06, 2026-09-25-12(2차 수정 후 재검증, 재실행 상한 도달), 2026-09-25-87, 2026-09-25-100.
- 퍼블리셔 중단: 2026-09-25-08(사이트 빌드 실패), 2026-09-25-18, 2026-09-25-43, 2026-09-25-49(내부 링크·각주 검사 실패).

## 2. 새로 확인된 사실

이번 주 `[사실]` 로 게시된 주장은 1절 표에 링크한 세부영역 28개 페이지, 대분류 7개 페이지, 주제 페이지, 세 트랙의 단계 페이지에 있다. 주장별 확인·미확인 건수는 각 실행의 검증 노트에 있다.

모든 실행이 일반 웹 원문을 열 수 없는 환경(fetch_mode mirror_only)에서 검증됐다. 원문은 GitHub 공식 저장소(raw.githubusercontent.com)와 입력으로 넣은 원문 텍스트만 열었다. 그래서 대부분의 `[사실]` 은 발행 주체 한 곳의 자료에 기대며 독립 출처로 교차 확인되지 않았다. 검증 노트에 교차 확인이 기록된 실행은 2026-09-25-09, -20, -26, -42, -56, -63, -64, -79, -80 뿐이다.

이번 실행(2026-09-26-01)에서 새로 확인한 사실은 참고문헌 상태에 관한 것뿐이며 6절에 적는다.

## 3. 강등·폐기된 주장

게시된 실행의 검증 노트에 기록된 강등·삭제다. finding id 는 실행마다 f1 부터 다시 매기므로 실행 id 와 함께 읽는다. 보류·중단된 실행의 처분은 게시되지 않았으므로 넣지 않았다.

| 실행 id | 변경 | 페이지 |
|---|---|---|
| 2026-09-25-01 | f6·f17 사실 → 추정, f18 삭제 | 7. 화물·재고·자산 식별과 추적 |
| 2026-09-25-02 | f10·f12·f17 사실 → 추정, f16 열린 질문 이동 | 매뉴얼 기반 로봇 기능 온톨로지 단계 1 |
| 2026-09-25-03 | f6·f12 사실 → 추정, f9 삭제 | EPCIS 이벤트 설계 주제 페이지 |
| 2026-09-25-05 | f6 사실 → 추정 | 건축 도면 자동 인식 단계 1 |
| 2026-09-25-09 | f15 확인 범위로 축소, f16 일부 삭제, f20 삭제 | 2. 공정·워크플로 모델링 |
| 2026-09-25-10 | f6·f11 사실 → 추정 | 3. 처리능력·거점·설비 계획 |
| 2026-09-25-11 | f16 일부 추정 | 건축 도면 자동 인식 단계 1 |
| 2026-09-25-14 | f6 사실 → 추정 | 4. 성과·경제성·프로세스 개선 |
| 2026-09-25-16 | f30 사실 → 추정 | 매뉴얼 기반 로봇 기능 온톨로지 단계 1 |
| 2026-09-25-20 | f4 연동 경로 열거 삭제 | 9. 로봇·제조사 관제 연동 |
| 2026-09-25-22 | f2 사실 → 추정, f4 비교 절 삭제, f12·f13 추론 절 추정 분리, f15 절 삭제, f10 삭제 | 건축 도면 자동 인식 단계 1 |
| 2026-09-25-25 | f14·f18·f22 사실 → 추정, f17 수치 삭제 | 10. 설비·건물 시스템 연동 |
| 2026-09-25-27 | f13·f14 사실 → 추정, f3 구절 삭제 | 11. 분산 시스템·통신·컴퓨팅 구조 |
| 2026-09-25-30 | f3 부분 강등 | 자연어 업무 지시 챗봇 단계 1 |
| 2026-09-25-31 | f21·f27 사실 → 추정 | 12. 명령·작업 실행의 신뢰성 |
| 2026-09-25-32 | f19 부분 수정, f22 사실 → 추정 | B. 공통 정보·환경 모델 |
| 2026-09-25-33 | f16 사실 → 추정 | 13. 작업 배정 — MRTA |
| 2026-09-25-36 | f22·f24 사실 → 추정 | 건축 도면 자동 인식 단계 2 |
| 2026-09-25-37 | f10 뒤 절 사실 → 추정 | 자연어 업무 지시 챗봇 단계 2 |
| 2026-09-25-38 | f31 사실 → 추정 | C. 연결·실행 기반 |
| 2026-09-25-39 | f24 삭제 | 15. 다중 로봇 경로·교통 관리 — MAPF |
| 2026-09-25-41 | f8 추정 → 의견 | 매뉴얼 기반 로봇 기능 온톨로지 단계 1 |
| 2026-09-25-42 | f23 사실 → 추정 | 17. 로봇 간 협업·물리적 인계 |
| 2026-09-25-45 | f1 사실 → 추정 | 매뉴얼 기반 로봇 기능 온톨로지 단계 1 |
| 2026-09-25-46 | f7·f15·f20 사실 → 추정 | 18. 사람–로봇 협업·운영 인터페이스 |
| 2026-09-25-47 | f2 사실 → 추정 | 매뉴얼 기반 로봇 기능 온톨로지 단계 1 |
| 2026-09-25-48 | f15·f17·f20 사실 → 추정 | 19. 모니터링·이상 탐지·원인 분석 |
| 2026-09-25-52 | f2 사실 → 추정 | 21. 온보딩·설정·현장 시운전 |
| 2026-09-25-55 | f21 일부 문구 삭제 | D. 계획·최적화 |
| 2026-09-25-56 | f21 추정 → 의견 | 22. 시뮬레이션·예측용 디지털 트윈 |
| 2026-09-25-57 | f7 축소, f8 해석 부분 추정 분리 | 매뉴얼 기반 로봇 기능 온톨로지 단계 2 |
| 2026-09-25-58 | f13 사실 → 추정 | 건축 도면 자동 인식 단계 3 |
| 2026-09-25-60 | f5·f16·f17·f20·f21·f29·f30 연결 해석 부분 추정 분리 | E. 협업·현장 운영 |
| 2026-09-25-61 | f13 일부 삭제, f17 적용 해석 추정 분리, f19 사실 → 추정 | 24. 자산·소프트웨어 수명주기 관리 |
| 2026-09-25-62 | f11 일부 사실 → 추정 | 자연어 업무 지시 챗봇 단계 2 |
| 2026-09-25-63 | f2·f12 사실 → 추정 | 25. 안전·위험 관리 |
| 2026-09-25-64 | f11·f20 사실 → 추정, f13 삭제 | 26. 사이버보안·접근권한·개인정보 |
| 2026-09-25-66 | f6·f9 사실 → 추정 | 자연어 업무 지시 챗봇 단계 3 |
| 2026-09-25-67 | f6·f18 사실 → 추정 | F. 도입·검증·유지관리 |
| 2026-09-25-69 | f12 사실 → 추정 | 28. 표준·상호운용성·다사업자 거버넌스 |
| 2026-09-25-70 | f12 사실 → 추정 | 건축 도면 자동 인식 단계 3 |
| 2026-09-25-71 | f8 사실 → 추정 | 자연어 업무 지시 챗봇 단계 3 |
| 2026-09-25-72 | f7·f10·f14 일부 추정 | 건축 도면 자동 인식 단계 4 |
| 2026-09-25-74 | f18 사실 → 추정 | 자연어 업무 지시 챗봇 단계 3 |
| 2026-09-25-76 | f11 일부 절 삭제 | 건축 도면 자동 인식 단계 4 |
| 2026-09-25-77 | f17 사실 → 추정 | 자연어 업무 지시 챗봇 단계 3 |
| 2026-09-25-78 | f7 사실 → 추정 | 건축 도면 자동 인식 단계 4 |
| 2026-09-25-79 | f13·f14 사실 → 추정 | 자연어 업무 지시 챗봇 단계 4 |
| 2026-09-25-81 | f15 사실 → 추정 | 자연어 업무 지시 챗봇 단계 4 |
| 2026-09-25-82 | f2·f7·f10 사실 → 추정 | 건축 도면 자동 인식 단계 5 |
| 2026-09-25-83 | f10·f12·f15·f17 사실 → 추정, f19 일부 추정 | 자연어 업무 지시 챗봇 단계 4 |
| 2026-09-25-84 | f2·f8·f11~f14·f18~f20 해석 부분 사실 → 추정 | 건축 도면 자동 인식 단계 5 |
| 2026-09-25-86 | f6 가운데 LTAA 부분 사실 → 추정 | 자연어 업무 지시 챗봇 단계 5 |
| 2026-09-25-98 | f11 정의 부분 추정 분리 | 자연어 업무 지시 챗봇 단계 5 |
| 2026-09-25-99 | f7 사실 → 추정 | 자연어 업무 지시 챗봇 단계 5 |

**참고문헌 폐기** — [ref-709](../../references/ref-709.md)를 deprecated 로 바꾸고 대체 항목을 [ref-315](../../references/ref-315.md)로 지정했다. 두 항목은 호스트만 다르고(www.korea.kr/briefing 과 korea.kr/news) 같은 보도자료 id(newsId=156480155)와 같은 제목을 가리킨다. [사실][^ref-315][^ref-709] ref-709 를 인용한 기존 페이지의 각주는 이번 실행에서 고치지 않았다.

## 4. 열린 질문 변동

- 새로 열림: [열린 질문](../../open-questions.md)의 oq-001 ~ oq-121(121건). 이번 주 해결·보류로 바뀐 질문은 없다.
- 이번 실행에서 새로 올리는 질문(다음 순번 id, 관련 영역 28. 표준·상호운용성·다사업자 거버넌스): 산업 디지털 전환 촉진법의 제명이 '산업 디지털 전환 및 인공지능 활용 촉진법'으로 바뀌어 시행되었는가, 바뀌었다면 데이터 공동 생성 규정의 조문 번호와 내용도 달라졌는가? (관련 기존 질문: oq-109) 근거는 6절의 ref-637 점검 결과다.[^ref-637]
- 트랙 백로그의 열린 질문은 매뉴얼 기반 로봇 기능 온톨로지 45건, 자연어 업무 지시 챗봇 48건, 건축 도면 자동 인식 35건이다(열린 질문 페이지 기준).
- 운영 메모: 보류·중단된 실행이 제안한 질문(2026-09-25-06 의 제조사별 동작 이름 공통 사전, 2026-09-25-49 의 VDA 5050 우선·벌점 구역 가중치와 배터리 건강 상태 필드)은 열린 질문 목록에 등록되지 않았다.

## 5. 다음 주 후보

- 참고문헌 정리: ref-584·ref-707·ref-767 은 모두 IEC 62443-3-3:2013 을 가리키므로 대표 출처 하나로 합칠 후보다. [사실][^ref-584][^ref-707][^ref-767] 다만 ref-584 는 IEC 원판이 아니라 CSA 채택판(CAN/CSA IEC 62443-3-3-2017) 판매 페이지이므로 합칠 때 채택판 구분을 남긴다.
- 미러 등록: ref-172 의 GitHub 위키 원문 경로(raw.githubusercontent.com/wiki/nasa-jpl/rosa/Custom-Agents.md)를 config/source_mirrors.yaml 에 등록할 후보다(6절).
- ref-709 를 인용한 페이지(28. 표준·상호운용성·다사업자 거버넌스 등)의 각주를 ref-315 로 바꾸는 갱신.
- ref-637 제명 변경 여부 확인(4절의 새 질문).
- 보류 실행 재처리: 2026-09-25-06, 2026-09-25-12, 2026-09-25-87, 2026-09-25-100.
- 신뢰도 low 로 게시된 세부영역(8. 실시간 세계 상태·데이터 일관성, 11. 분산 시스템·통신·컴퓨팅 구조, 19. 모니터링·이상 탐지·원인 분석)의 주제 조사 후보.

운영 메모(파이프라인 담당 확인용):

- 보류 실행 2026-09-25-100 은 run_id 가 스키마 패턴(끝 두 자리)에 맞지 않아 2026-09-25-00 으로 기록됐다.
- 그 브리프의 ref-748~ref-750 은 현재 참고문헌 목록의 같은 id(JSON Schema 계열)와 다른 문헌을 가리키므로, 재게시할 때 id 를 다시 부여해야 한다.
- 참고문헌 번호 ref-781~ref-791 이 비어 있다.

## 6. 링크·출처 유효성 점검

**url_check 결과**: 정책 차단 797건, 미러 열림 144건, 오류 2건, 미러 오류 1건이다. 정책 차단은 이 환경의 네트워크 정책 때문이며 링크 오류가 아니다. 오류·미러 오류 3건만 점검했다.

| 출처 | url_check 결과 | 점검 결과 | 조치 |
|---|---|---|---|
| [ref-172](../../references/ref-172.md) | 오류(미러 없음) | 아래 1 | 다음 실행에서 미러 등록 |
| [ref-412](../../references/ref-412.md) | 미러 오류 | 아래 2 | 조치 없음 |
| [ref-637](../../references/ref-637.md) | 오류 | 아래 3 | 각주 URL 인코딩 표기, needs_update(등록 URL 교체 요청) |

1. ref-172(ROSA 위키 Custom Agents)의 정규 URL 은 미러가 없어 오류로 기록됐다. GitHub 위키 원문 경로는 2026-09-26 기준 열리며, 내용이 ROSA 를 다른 로봇에 맞게 도구·프롬프트로 사용자 정의하는 안내로 등록 제목과 일치한다. [사실][^ref-172]
2. ref-412(Open-RMF rmf_ros2 place.json)는 2026-09-26 에 raw 경로가 열렸고 스키마 제목 'Place Description' 이 등록 제목과 일치한다. [사실][^ref-412] url_check 의 미러 오류는 일시적 실패로 보인다. [추정][^ref-412]
3. ref-637 의 등록 URL 은 한글 경로가 퍼센트 인코딩되지 않은 형태여서 점검 스크립트에서 오류가 났다. 같은 경로를 인코딩한 URL 이 검색 결과에 '산업디지털전환촉진법' 제목으로 나타나 문서 자체는 존재한다. [사실][^ref-637] 검색 결과에 제명 '산업 디지털 전환 및 인공지능 활용 촉진법' 이 나타나고 같은 제명 변경을 담은 개정안 발의 보도가 있어, 이 법률의 제명·현행 판이 바뀌었을 가능성이 있다. 시행 여부는 확인하지 못했다. [추정][^ref-637] 이번 실행에서는 참고문헌 페이지의 각주 형식과 이 페이지 각주에만 인코딩 URL 을 적었다. 등록 URL 교체는 pipeline 담당에게 요청했다. 제목·법률 번호·발행일은 유지했다. 현행 판 링크 병기와 제목 교체는 하지 않았다.

**참고문헌 중복 의심**: ref-315·ref-709(3절에서 ref-709 deprecated 처리)와 ref-584·ref-707·ref-767(5절 후보)이다.

**내부 링크·각주**: link_check 는 통과했다(파일 1240개, 경고 0건). 추가 조치는 없다.

## 7. 용어집 정리

용어집에는 205개 용어가 있다. 이번 주 브리프에서 새 용어 후보는 없었다. 용어 목록에서 뜻이 충돌하는 중복 용어는 찾지 못했다.

상태가 draft 로 남은 용어는 10개다: ariac, digital-twin, epcis, fleet-adapter, lifelong-mapf, mapf, mrta, multi-agent-pickup-and-delivery, scor, wes-wcs-wms-mes-tms. 다음 해당 영역 실행에서 검증을 거쳐 게시할 후보다.

[^ref-172]: NASA Jet Propulsion Laboratory (nasa-jpl), Custom Agents · nasa-jpl/rosa Wiki, 미확인, https://github.com/nasa-jpl/rosa/wiki/Custom-Agents, 접근일 2026-09-26
[^ref-412]: Open Robotics (open-rmf), rmf_ros2 — rmf_fleet_adapter/schemas/place.json, 미확인, https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/place.json, 접근일 2026-09-26
[^ref-637]: 국가법령정보센터(산업통상자원부), 산업 디지털 전환 촉진법 (법률 제18692호), 2022-01-04, https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EC%82%B0%EC%97%85%EB%94%94%EC%A7%80%ED%84%B8%EC%A0%84%ED%99%98%EC%B4%89%EC%A7%84%EB%B2%95/(18692,20220104), 접근일 2026-09-26 (원문 미열람)
[^ref-315]: 산업통상자원부 국가기술표준원(대한민국 정책브리핑), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11, https://www.korea.kr/briefing/pressReleaseView.do?newsId=156480155, 접근일 2026-09-26 (원문 미열람)
[^ref-709]: 대한민국 정책브리핑(산업통상자원부 국가기술표준원), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11-11, https://korea.kr/news/pressReleaseView.do?newsId=156480155, 접근일 2026-09-26 (원문 미열람)
[^ref-584]: CSA / IEC (ANSI Webstore), CAN/CSA IEC 62443-3-3-2017 - Industrial communication networks - Network and system security - Part 3-3: System security requirements and security levels (Adopted IEC 62443-3-3:2013, first edition, 2013-08), 2013-08, https://webstore.ansi.org/standards/csa/csaiec624432017-2442576, 접근일 2026-09-26 (원문 미열람)
[^ref-707]: IEC, IEC 62443-3-3:2013 Industrial communication networks — Network and system security — Part 3-3: System security requirements and security levels (sample), 2013-08, https://cdn.standards.iteh.ai/samples/19488/7c0b753be32e46fc986c23c32efbdbe8/IEC-62443-3-3-2013.pdf, 접근일 2026-09-26 (원문 미열람)
[^ref-767]: IEC, IEC 62443-3-3:2013 Industrial communication networks — Network and system security — Part 3-3: System security requirements and security levels, 2013-08, https://standards.iteh.ai/catalog/standards/iec/c32e05fe-78a2-467e-a24d-0fc422289f55/iec-62443-3-3-2013, 접근일 2026-09-26 (원문 미열람)
```

### runs/2026-09-26-01/pages/references/ref-637.md

```markdown
---
title: "ref-637 — 산업 디지털 전환 촉진법 (법률 제18692호)"
type: reference
ref_id: ref-637
ref_title: 산업 디지털 전환 촉진법 (법률 제18692호)
org: 국가법령정보센터(산업통상자원부)
published: 2022-01-04
url: https://www.law.go.kr/법령/산업디지털전환촉진법/(18692,20220104)
source_type: 정부·연구기관
reliability: medium
url_verified: false
url_status: null
accessed: 2026-09-25
related_areas: []
tags: []
fetched: false
fetched_via: null
fetch_url: null
status: needs_update
created: 2026-09-25
updated: 2026-09-26
version: 3
---

[홈](../index.md) › [참고문헌](index.md) › ref-637

# ref-637 — 산업 디지털 전환 촉진법 (법률 제18692호)

## 서지 정보

| 항목 | 값 |
|---|---|
| id | ref-637 |
| 기관 | 국가법령정보센터(산업통상자원부) |
| 제목 | 산업 디지털 전환 촉진법 (법률 제18692호) |
| 발행일 | 2022-01-04 |
| URL | <https://www.law.go.kr/법령/산업디지털전환촉진법/(18692,20220104)> |
| 유형 | 정부·연구기관 |
| 신뢰도 | medium |
| 원문 열람 | 미확인 — 원문 미열람 |
| 접근일 | 2026-09-25 (원문 미열람) |

## 요약

원문 미열람. 산업데이터 생성자의 사용·수익 권리, 공동 생성·제3자 제공 시 권리 귀속 규정. 2025-05-27 일부개정 판과의 조문 동일 여부는 미확인.

등록 실행: 2026-09-25-69 · 검증: 1차 조건부 승인 / 2차 통과

## 인용된 페이지

이 출처를 프런트매터 `sources` 또는 각주 `[^ref-637]` 로 인용했거나 이 페이지로 링크한 페이지의 목록이다. 퍼블리셔가 docs 전체를 스캔해 자동으로 갱신한다.

<!-- auto:reference-cited-pages:start -->
- [28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)
- [변경 이력](../changelog.md)
- [산업데이터 (Industrial Data)](../glossary/industrial-data.md)
- [28. 표준·상호운용성·다사업자 거버넌스 — 왜 중요한가](../topics/2026/2026-09-25-area28-s3.md)
- [28. 표준·상호운용성·다사업자 거버넌스 — 핵심 개념과 용어](../topics/2026/2026-09-25-area28-s4.md)
- [28. 표준·상호운용성·다사업자 거버넌스 — 대표 접근법과 기술](../topics/2026/2026-09-25-area28-s6.md)
<!-- auto:reference-cited-pages:end -->

## 각주 형식

`[^ref-637]: 국가법령정보센터(산업통상자원부), 산업 디지털 전환 촉진법 (법률 제18692호), 2022-01-04, https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EC%82%B0%EC%97%85%EB%94%94%EC%A7%80%ED%84%B8%EC%A0%84%ED%99%98%EC%B4%89%EC%A7%84%EB%B2%95/(18692,20220104), 접근일 2026-09-26 (원문 미열람)`

URL 을 퍼센트 인코딩 형태로 적은 것은 이 절의 각주 형식 줄뿐이다. 등록 URL(프런트매터 url, 서지 정보 표) 교체는 pipeline 담당에게 요청했으며 아직 반영되지 않았다. 이전 URL 은 한글 경로가 인코딩되지 않아 점검 스크립트에서 오류가 났다. 인코딩한 URL 은 검색 결과에 '산업디지털전환촉진법' 제목으로 나타나 문서 자체는 존재한다. [사실][^ref-637]

검색 결과에 제명 '산업 디지털 전환 및 인공지능 활용 촉진법' 의 국가법령정보센터 페이지와 제명 변경 개정안 보도가 나타나, 이 법률의 제명·현행 판이 바뀌었을 가능성이 있다. 다만 시행 여부와 조문은 원문으로 확인하지 못했다(2026-09-26 기준). [추정][^ref-637] 이 항목의 제목·법률 번호·발행일은 바꾸지 않았고, 확인되면 다시 갱신한다. 관련 질문은 [열린 질문](../open-questions.md)에 있다.

## 비고

원문 미열람(페이지 열람이 차단된 환경에서 검색 결과의 기관·제목·URL 일치로 실재를 확인했다). 신뢰도는 medium 이 상한이다.

<!-- source-fetch:start -->
원문 열람 상태:

| 항목 | 값 |
|---|---|
| 원문 열람 | 원문 미열람 |
| 열람 경로 | 없음 |
| 원문 텍스트 | 없음 |
| URL 확인 | 미확인(data/url_check.json 에 결과 없음) |

원문 열람 상태는 스크립트가 기록한다(pipeline/lib/sources.py). URL 확인은 `python3 pipeline/checks/check_urls.py`, 반영은 `python3 pipeline/scaffold.py --apply-url-check`, 사람이 넣은 원문은 `python3 pipeline/ingest_sources.py` 로 갱신한다.
<!-- source-fetch:end -->

[^ref-637]: 국가법령정보센터(산업통상자원부), 산업 디지털 전환 촉진법 (법률 제18692호), 2022-01-04, https://www.law.go.kr/법령/산업디지털전환촉진법/(18692,20220104), 접근일 2026-09-26 (원문 미열람)
```

### docs/references/ref-637.md

````markdown
---
title: "ref-637 — 산업 디지털 전환 촉진법 (법률 제18692호)"
type: reference
ref_id: ref-637
ref_title: 산업 디지털 전환 촉진법 (법률 제18692호)
org: 국가법령정보센터(산업통상자원부)
published: 2022-01-04
url: https://www.law.go.kr/법령/산업디지털전환촉진법/(18692,20220104)
source_type: 정부·연구기관
reliability: medium
url_verified: false
url_status: null
accessed: 2026-09-25
related_areas: []
tags: []
fetched: false
fetched_via: null
fetch_url: null
status: published
created: 2026-09-25
updated: 2026-09-25
version: 2
---

[홈](../index.md) › [참고문헌](index.md) › ref-637

# ref-637 — 산업 디지털 전환 촉진법 (법률 제18692호)

## 서지 정보

| 항목 | 값 |
|---|---|
| id | ref-637 |
| 기관 | 국가법령정보센터(산업통상자원부) |
| 제목 | 산업 디지털 전환 촉진법 (법률 제18692호) |
| 발행일 | 2022-01-04 |
| URL | <https://www.law.go.kr/법령/산업디지털전환촉진법/(18692,20220104)> |
| 유형 | 정부·연구기관 |
| 신뢰도 | medium |
| 원문 열람 | 미확인 — 원문 미열람 |
| 접근일 | 2026-09-25 (원문 미열람) |

## 요약

원문 미열람. 산업데이터 생성자의 사용·수익 권리, 공동 생성·제3자 제공 시 권리 귀속 규정. 2025-05-27 일부개정 판과의 조문 동일 여부는 미확인.

등록 실행: 2026-09-25-69 · 검증: 1차 조건부 승인 / 2차 통과

## 인용된 페이지

이 출처를 프런트매터 `sources` 또는 각주 `[^ref-637]` 로 인용했거나 이 페이지로 링크한 페이지의 목록이다. 퍼블리셔가 docs 전체를 스캔해 자동으로 갱신한다.

<!-- auto:reference-cited-pages:start -->
- [28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)
- [변경 이력](../changelog.md)
- [산업데이터 (Industrial Data)](../glossary/industrial-data.md)
- [28. 표준·상호운용성·다사업자 거버넌스 — 왜 중요한가](../topics/2026/2026-09-25-area28-s3.md)
- [28. 표준·상호운용성·다사업자 거버넌스 — 핵심 개념과 용어](../topics/2026/2026-09-25-area28-s4.md)
- [28. 표준·상호운용성·다사업자 거버넌스 — 대표 접근법과 기술](../topics/2026/2026-09-25-area28-s6.md)
<!-- auto:reference-cited-pages:end -->

## 각주 형식

이 출처를 인용할 때 쓰는 각주 정의는 다음과 같다.

```
[^ref-637]: 국가법령정보센터(산업통상자원부), 산업 디지털 전환 촉진법 (법률 제18692호), 2022-01-04, https://www.law.go.kr/법령/산업디지털전환촉진법/(18692,20220104), 접근일 2026-09-25 (원문 미열람)
```

## 비고

원문 미열람(페이지 열람이 차단된 환경에서 검색 결과의 기관·제목·URL 일치로 실재를 확인했다). 신뢰도는 medium 이 상한이다.

<!-- source-fetch:start -->
원문 열람 상태:

| 항목 | 값 |
|---|---|
| 원문 열람 | 원문 미열람 |
| 열람 경로 | 없음 |
| 원문 텍스트 | 없음 |
| URL 확인 | 미확인(data/url_check.json 에 결과 없음) |

원문 열람 상태는 스크립트가 기록한다(pipeline/lib/sources.py). URL 확인은 `python3 pipeline/checks/check_urls.py`, 반영은 `python3 pipeline/scaffold.py --apply-url-check`, 사람이 넣은 원문은 `python3 pipeline/ingest_sources.py` 로 갱신한다.
<!-- source-fetch:end -->
````

### runs/2026-09-26-01/pages/references/ref-709.md

```markdown
---
title: "ref-709 — 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다"
type: reference
ref_id: ref-709
ref_title: 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다
org: 대한민국 정책브리핑(산업통상자원부 국가기술표준원)
published: 2021-11-11
url: https://korea.kr/news/pressReleaseView.do?newsId=156480155
source_type: 정부·연구기관
reliability: medium
url_verified: false
url_status: null
accessed: 2026-09-25
related_areas: []
tags: []
fetched: false
fetched_via: null
fetch_url: null
status: deprecated
created: 2026-09-25
updated: 2026-09-26
version: 3
replaced_by: ref-315.md
---

[홈](../index.md) › [참고문헌](index.md) › ref-709

# ref-709 — 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다

## 서지 정보

| 항목 | 값 |
|---|---|
| id | ref-709 |
| 기관 | 대한민국 정책브리핑(산업통상자원부 국가기술표준원) |
| 제목 | 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 |
| 발행일 | 2021-11-11 |
| URL | <https://korea.kr/news/pressReleaseView.do?newsId=156480155> |
| 유형 | 정부·연구기관 |
| 신뢰도 | medium |
| 원문 열람 | 미확인 — 원문 미열람 |
| 접근일 | 2026-09-25 (원문 미열람) |

## 요약

원문 미열람. 로봇 엘리베이터 탑승 안전 요구사항·실내 배송 로봇 KS 제정 보도자료.

등록 실행: 2026-09-25-69 · 검증: 1차 조건부 승인 / 2차 통과

## 인용된 페이지

이 출처를 프런트매터 `sources` 또는 각주 `[^ref-709]` 로 인용했거나 이 페이지로 링크한 페이지의 목록이다. 퍼블리셔가 docs 전체를 스캔해 자동으로 갱신한다.

<!-- auto:reference-cited-pages:start -->
- [28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)
- [G. 안전·보안·지능·거버넌스](../categories/g-safety-security-intelligence-and-governance/index.md)
- [변경 이력](../changelog.md)
- [28. 표준·상호운용성·다사업자 거버넌스 — 관련 표준·프레임워크·오픈소스](../topics/2026/2026-09-25-area28-s7.md)
<!-- auto:reference-cited-pages:end -->

## 각주 형식

> 대체 페이지: [ref-315](ref-315.md)

`[^ref-709]: 대한민국 정책브리핑(산업통상자원부 국가기술표준원), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11-11, https://korea.kr/news/pressReleaseView.do?newsId=156480155, 접근일 2026-09-26 (원문 미열람)`

이 항목은 [ref-315](ref-315.md)와 호스트만 다르고(www.korea.kr/briefing 과 korea.kr/news) 같은 보도자료 id(newsId=156480155)와 같은 제목을 가리키는 중복 참고문헌이다. [사실][^ref-709] 새로 인용할 때는 ref-315 를 쓴다. 이 항목을 인용한 기존 페이지의 각주는 아직 바꾸지 않았다.

## 비고

원문 미열람(페이지 열람이 차단된 환경에서 검색 결과의 기관·제목·URL 일치로 실재를 확인했다). 신뢰도는 medium 이 상한이다.

<!-- source-fetch:start -->
원문 열람 상태:

| 항목 | 값 |
|---|---|
| 원문 열람 | 원문 미열람 |
| 열람 경로 | 없음 |
| 원문 텍스트 | 없음 |
| URL 확인 | 미확인(data/url_check.json 에 결과 없음) |

원문 열람 상태는 스크립트가 기록한다(pipeline/lib/sources.py). URL 확인은 `python3 pipeline/checks/check_urls.py`, 반영은 `python3 pipeline/scaffold.py --apply-url-check`, 사람이 넣은 원문은 `python3 pipeline/ingest_sources.py` 로 갱신한다.
<!-- source-fetch:end -->

[^ref-709]: 대한민국 정책브리핑(산업통상자원부 국가기술표준원), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11-11, https://korea.kr/news/pressReleaseView.do?newsId=156480155, 접근일 2026-09-26 (원문 미열람)
```

### docs/references/ref-709.md

````markdown
---
title: "ref-709 — 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다"
type: reference
ref_id: ref-709
ref_title: 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다
org: 대한민국 정책브리핑(산업통상자원부 국가기술표준원)
published: 2021-11-11
url: https://korea.kr/news/pressReleaseView.do?newsId=156480155
source_type: 정부·연구기관
reliability: medium
url_verified: false
url_status: null
accessed: 2026-09-25
related_areas: []
tags: []
fetched: false
fetched_via: null
fetch_url: null
status: published
created: 2026-09-25
updated: 2026-09-25
version: 2
---

[홈](../index.md) › [참고문헌](index.md) › ref-709

# ref-709 — 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다

## 서지 정보

| 항목 | 값 |
|---|---|
| id | ref-709 |
| 기관 | 대한민국 정책브리핑(산업통상자원부 국가기술표준원) |
| 제목 | 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 |
| 발행일 | 2021-11-11 |
| URL | <https://korea.kr/news/pressReleaseView.do?newsId=156480155> |
| 유형 | 정부·연구기관 |
| 신뢰도 | medium |
| 원문 열람 | 미확인 — 원문 미열람 |
| 접근일 | 2026-09-25 (원문 미열람) |

## 요약

원문 미열람. 로봇 엘리베이터 탑승 안전 요구사항·실내 배송 로봇 KS 제정 보도자료.

등록 실행: 2026-09-25-69 · 검증: 1차 조건부 승인 / 2차 통과

## 인용된 페이지

이 출처를 프런트매터 `sources` 또는 각주 `[^ref-709]` 로 인용했거나 이 페이지로 링크한 페이지의 목록이다. 퍼블리셔가 docs 전체를 스캔해 자동으로 갱신한다.

<!-- auto:reference-cited-pages:start -->
- [28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)
- [G. 안전·보안·지능·거버넌스](../categories/g-safety-security-intelligence-and-governance/index.md)
- [변경 이력](../changelog.md)
- [28. 표준·상호운용성·다사업자 거버넌스 — 관련 표준·프레임워크·오픈소스](../topics/2026/2026-09-25-area28-s7.md)
<!-- auto:reference-cited-pages:end -->

## 각주 형식

이 출처를 인용할 때 쓰는 각주 정의는 다음과 같다.

```
[^ref-709]: 대한민국 정책브리핑(산업통상자원부 국가기술표준원), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11-11, https://korea.kr/news/pressReleaseView.do?newsId=156480155, 접근일 2026-09-25 (원문 미열람)
```

## 비고

원문 미열람(페이지 열람이 차단된 환경에서 검색 결과의 기관·제목·URL 일치로 실재를 확인했다). 신뢰도는 medium 이 상한이다.

<!-- source-fetch:start -->
원문 열람 상태:

| 항목 | 값 |
|---|---|
| 원문 열람 | 원문 미열람 |
| 열람 경로 | 없음 |
| 원문 텍스트 | 없음 |
| URL 확인 | 미확인(data/url_check.json 에 결과 없음) |

원문 열람 상태는 스크립트가 기록한다(pipeline/lib/sources.py). URL 확인은 `python3 pipeline/checks/check_urls.py`, 반영은 `python3 pipeline/scaffold.py --apply-url-check`, 사람이 넣은 원문은 `python3 pipeline/ingest_sources.py` 로 갱신한다.
<!-- source-fetch:end -->
````

### agents/storyteller.md (6절 — 주간 정리 페이지의 절 구성; templates/weekly-log.md 가 없어 기준 템플릿 대용)

```markdown
**weekly_review(주간 정리)** — 신규 조사가 없다. `docs/logs/weekly/YYYY-Www.md` 를 쓴다(ISO 주, 예: 2026-09-24 → `2026-W39`). 프런트매터 `type: log`, `tags: [weekly_review]`. 절은 다음 순서로 고정한다. 1~5절은 사양서 6.3 절차 8 의 다섯 항목을 그 번호·순서 그대로 둔 것이고, 6·7절은 사양서 7.1 주간 정리 항목(링크·출처 유효성 점검, 용어집 정리)을 담는 부록 절이다 [가정]:
`## 1. 이번 주 다룬 영역`(실행 id·실행 유형·대상·판정 표) `## 2. 새로 확인된 사실`(이번 주 `[사실]` 로 게시된 주장과 페이지 링크) `## 3. 강등·폐기된 주장`(finding id·변경·페이지) `## 4. 열린 질문 변동`(새로 열림·해결·보류) `## 5. 다음 주 후보`(대상 선정 규칙으로 예상되는 영역·주제, 우선 지정 사항) `## 6. 링크·출처 유효성 점검`(입력의 스크립트 점검 결과 `url_check.json`·`link_check.txt` 와 브리프의 점검 결과 finding: 깨진 링크·닿지 않는 출처와 조치) `## 7. 용어집 정리`(중복·충돌 용어와 제안). 내용은 입력의 이번 주 실행 산출물과 브리프의 점검 결과에서만 가져온다. 열린 질문 정리는 `open_question_updates`(상태 변경은 검증이 인정한 것만), 용어집 정리는 `glossary_updates`(action: update)로 함께 낸다. `changelog_entry` 의 대상 이름은 "주간 정리 YYYY-Www".
```

### docs/references/index.md (요약형 전체 799건)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 원문 열람 |
|---|---|---|---|---|---|
| ref-001 | ASCM | SCOR Digital Standard | 미확인 | https://www.ascm.org/corporate-solutions/standards-tools/scor-ds/ | 아니오 |
| ref-002 | ISA | Update to ISA-95 Standard Addresses Integration of Enterprise and Manufacturing Control Systems | 2025 | https://www.isa.org/news-press-releases/2025/april/update-to-isa-95-standard-addresses-integration-of | 아니오 |
| ref-003 | GS1 | EPCIS and CBV Linked Data Model | 미확인 | https://ref.gs1.org/epcis/ | 아니오 |
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 예 |
| ref-005 | Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S. | Lifelong Multi-Agent Path Finding in Large-Scale Warehouses | 2020 | https://arxiv.org/abs/2005.07371 | 아니오 |
| ref-006 | Ma, H., Li, J., Kumar, T. K. S., & Koenig, S. | Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks | 2017 | https://arxiv.org/abs/1705.10868 | 아니오 |
| ref-007 | NIST | Performance of Collaborative Robot Systems | 미확인 | https://www.nist.gov/programs-projects/performance-collaborative-robot-systems | 아니오 |
| ref-008 | NIST | ARIAC Documentation | 미확인 | https://pages.nist.gov/ARIAC_docs/en/latest/ | 예 |
| ref-009 | ROS 2 Design | ROS 2 DDS-Security Integration | 미확인 | https://design.ros2.org/articles/ros2_dds_security.html | 예 |
| ref-010 | ROS 2 Design | ROS 2 Robotic Systems Threat Model | 미확인 | https://design.ros2.org/articles/ros2_threat_model.html | 예 |
| ref-011 | ISO/IEC | ISO/IEC 19987:2024 - Information technology — EPC Information Services (EPCIS) | 2024-03 | https://www.iso.org/standard/85557.html | 아니오 |
| ref-012 | ISO/IEC | ISO/IEC 19988:2024 - Information technology — GS1 Core Business Vocabulary (CBV) | 2024 | https://www.iso.org/standard/85558.html | 아니오 |
| ref-013 | OpenEPCIS | EPCIS 2.0 and EPCIS 1.2 | OpenEPCIS Docs | 미확인 | https://openepcis.io/docs/epcis/ | 아니오 |
| ref-014 | GS1 | Core Business Vocabulary (CBV) Standard | 미확인 | https://ref.gs1.org/standards/cbv/ | 아니오 |
| ref-015 | GS1 | EPCIS and CBV Implementation Guideline | 미확인 | https://www.gs1.org/docs/epc/EPCIS_Guideline.pdf | 아니오 |
| ref-016 | GS1 | Serial Shipping Container Code (SSCC) | 미확인 | https://www.gs1.org/standards/id-keys/sscc | 아니오 |
| ref-017 | GS1 Korea(대한상공회의소 유통물류진흥원) | SSCC (Serial Shipping Container Code) GS1 Information Vol. 21 | 2019-09 | http://www.gs1kr.org/front/service/File/SSCC%20%EB%B0%9C%EA%B0%84%20%EC%9E%90%EB%A3%8C.pdf | 아니오 |
| ref-018 | GS1 | GS1 Logistic Label Guideline | 미확인 | https://www.gs1.org/docs/tl/GS1_Logistic_Label_Guideline.pdf | 아니오 |
| ref-019 | GS1 | Global Returnable Asset Identifier (GRAI) | 미확인 | https://www.gs1.org/standards/id-keys/grai | 아니오 |
| ref-020 | GS1 | Which GS1 identification key should be used for individual assets used to transport goods? (GS1 GO Customer Service Portal) | 미확인 | https://support.gs1.org/support/solutions/articles/43000734294-which-gs1-identification-key-should-be-used-for-individual-assets-used-to-transport-goods- | 아니오 |
| ref-021 | GS1 | EPC Tag Data Standard | 미확인 | https://www.gs1.org/sites/default/files/docs/epc/GS1_EPC_TDS_i1_11.pdf | 아니오 |
| ref-022 | VDA(Verband der Automobilindustrie) | VDA 5050 Version 2.0.0 — Interface for the communication between automated guided vehicles (AGV) and a master control | 2022-01 | https://www.vda.de/dam/jcr:f0c9c019-1506-4dee-998a-e92723fbf025/EN-VDA5050-V2_0_0.pdf | 아니오 |
| ref-023 | Open Robotics | Workcells - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/integration_workcells.html | 예 |
| ref-024 | Singh, J. 외 | RFID tag readability issues with palletized loads of consumer goods | 2009 | https://onlinelibrary.wiley.com/doi/abs/10.1002/pts.864 | 아니오 |
| ref-025 | IEEE | 1872-2015 - IEEE Standard Ontologies for Robotics and Automation | 2015 | https://ieeexplore.ieee.org/document/7084073/ | 아니오 |
| ref-026 | IEEE | IEEE 1872.2-2021 - IEEE Standard for Autonomous Robotics (AuR) Ontology | 2022 | https://standards.ieee.org/standard/1872_2-2021.html | 아니오 |
| ref-027 | Beetz, M., Beßler, D., Haidu, A., Pomarlan, M., Bozcuoglu, A. K., & Bartels, G. | KnowRob 2.0 — A 2nd Generation Knowledge Processing Framework for Cognition-Enabled Robotic Agents | 2018 | https://ai.uni-bremen.de/papers/beetz18knowrob.pdf | 아니오 |
| ref-028 | Beßler, D. 외 | Foundations of the Socio-physical Model of Activities (SOMA) for Autonomous Robotic Agents | 2021 | https://arxiv.org/pdf/2011.11972 | 아니오 |
| ref-029 | McDermott, D. 외 | PDDL - The Planning Domain Definition Language | 1998 | https://www.researchgate.net/publication/2278933_PDDL_-_The_Planning_Domain_Definition_Language | 아니오 |
| ref-030 | W3C / OGC | Semantic Sensor Network Ontology | 2017-10-19 | https://www.w3.org/TR/vocab-ssn/ | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 예 |
| ref-032 | VDA(Verband der Automobilindustrie) | Version 3.0 of VDA 5050 released | 2026-04 | https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN | 아니오 |
| ref-033 | MassRobotics | Autonomous Mobile Robot Standards Published by MassRobotics | 2021-05 | https://www.massrobotics.org/autonomous-mobile-robot-standards-published-by-massrobotics/ | 아니오 |
| ref-034 | OPC Foundation / VDMA | OPC-40010-1 – OPC UA for Robotics - Part 1: Vertical Integration | 미확인 | https://reference.opcfoundation.org/specs/OPC-40010-1 | 아니오 |
| ref-035 | Plattform Industrie 4.0 | Information Model for Capabilities, Skills & Services | 2022-11 | https://www.plattform-i40.de/IP/Redaktion/EN/Downloads/Publikation/CapabilitiesSkillsServices.html | 아니오 |
| ref-036 | Köcher, A. 외 | A Reference Model for Common Understanding of Capabilities and Skills in Manufacturing | 2022 | https://arxiv.org/abs/2209.09632 | 아니오 |
| ref-037 | Vieira da Silva, L. M., Köcher, A., Gill, M. S., Weiss, M., & Fay, A. | Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies | 2023-07 | https://arxiv.org/abs/2307.00827 | 아니오 |
| ref-038 | Vieira da Silva, L. M., Köcher, A., & Fay, A. | A Capability and Skill Model for Heterogeneous Autonomous Robots | 2022-09 | https://arxiv.org/abs/2209.10900 | 아니오 |
| ref-039 | Open Robotics | Currently supported Tasks - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/task_types.html | 예 |
| ref-040 | Open Robotics | PerformAction Tutorial - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/integration_fleets_action_tutorial.html | 예 |
| ref-041 | Naqvi, M. R. 외(Scientific Reports) | Ontology-driven integration of advertised and operational capabilities in robots | 2025-10-02 | https://www.nature.com/articles/s41598-025-16649-3 | 아니오 |
| ref-042 | Aguado, E., Gomez, V., Hernando, M., Rossi, C., & Sanz, R. | A survey of ontology-enabled processes for dependable robot autonomy | 2024-07 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2024.1377897/full | 아니오 |
| ref-043 | 신민종, 한영석, 정재윤 | 자산관리쉘 표준을 이용한 자율이동로봇 모니터링 시스템 설계 | 2024 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003140560 | 아니오 |
| ref-044 | GS1 | gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0) | 2021-09-30 | https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl | 예 |
| ref-045 | GS1 | gs1/EPCIS — Ontology/EPCIS.ttl (EPCIS ontology 2.0) | 2021-09-30 | https://github.com/gs1/EPCIS/blob/master/Ontology/EPCIS.ttl | 예 |
| ref-046 | VDMA (Intralogistics-2X-LIF GitHub) | Layout-Interchange-Format — README (Repository for the Layout Interchange Format (LIF) developed by the VDMA) | 2023-09 | https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format | 아니오 |
| ref-047 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_dispenser_msgs/msg/DispenserRequest.msg | 미확인 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_dispenser_msgs/msg/DispenserRequest.msg | 예 |
| ref-048 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_dispenser_msgs/msg/DispenserRequestItem.msg | 미확인 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_dispenser_msgs/msg/DispenserRequestItem.msg | 예 |
| ref-049 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg | 미확인 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg | 예 |
| ref-050 | Auto-ID Labs Korea(세종대학교), Byun, J. | Oliot EPCIS for GS1 EPCIS/CBV 2.0.0 (GitHub JaewookByun/epcis README) | 미확인 | https://github.com/JaewookByun/epcis | 예 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 예 |
| ref-052 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — README.md | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/README.md | 예 |
| ref-053 | NVIDIA Research (NVlabs) | progprompt-vh — ProgPrompt: Generating Situated Robot Task Plans using Large Language Models (GitHub README) | 미확인 | https://github.com/NVlabs/progprompt-vh | 예 |
| ref-054 | Singh, I. 외 | ProgPrompt: Generating Situated Robot Task Plans using Large Language Models | 2022-09 | https://arxiv.org/abs/2209.11302 | 아니오 |
| ref-055 | Brown University H2R Lab | Lang2LTL — Code for paper Lang2LTL: Grounding Complex Natural Language Commands for Temporal Tasks in Unseen Environments (GitHub README) | 미확인 | https://github.com/h2r/Lang2LTL | 예 |
| ref-056 | Liu, J. X. 외 | Grounding Complex Natural Language Commands for Temporal Tasks in Unseen Environments | 2023-02 | https://arxiv.org/abs/2302.11649 | 아니오 |
| ref-057 | Tellex, S. 외 | Understanding Natural Language Commands for Robotic Navigation and Mobile Manipulation | 2011-08 | https://ojs.aaai.org/index.php/AAAI/article/view/7979 | 아니오 |
| ref-058 | Cohen, V., Liu, J. X., Mooney, R., Tellex, S., & Watkins, D. | A Survey of Robotic Language Grounding: Tradeoffs between Symbols and Embeddings | 2024-08 | https://www.ijcai.org/proceedings/2024/885 | 아니오 |
| ref-059 | Wang, Y. 외(DART-LLM 저자) | DART-LLM: Dependency-Aware Multi-Robot Task Decomposition and Execution using Large Language Models | 2024-11 | https://arxiv.org/abs/2411.09022 | 아니오 |
| ref-060 | Lee, Y. 외(Digital Health) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 2026 | https://doi.org/10.1177/20552076261437181 | 아니오 |
| ref-061 | Izzo, R. A., Bardaro, G., & Matteucci, M. (Politecnico di Milano AIRLab) | BTGenBot: Behavior Tree Generation for Robotic Tasks with Lightweight LLMs | 2024-03 | https://arxiv.org/abs/2403.12761 | 아니오 |
| ref-062 | CubiCasa (Kalervo, A. 외) | CubiCasa5k — README (CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis) | 미확인 | https://github.com/CubiCasa/CubiCasa5k | 아니오 |
| ref-063 | Kalervo, A., Ylioinas, J., Häikiö, M., Karhu, A., & Kannala, J. | CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis | 2019-04 | https://arxiv.org/abs/1904.01920 | 아니오 |
| ref-064 | Zeng, Z., Li, X., Yu, Y. K., & Fu, C.-W. | DeepFloorplan — README (Deep Floor Plan Recognition using a Multi-task Network with Room-boundary-Guided Attention) | 2019 | https://github.com/zlzeng/DeepFloorplan | 아니오 |
| ref-065 | Liu, C., Wu, J., Kohli, P., & Furukawa, Y. | FloorplanTransformation — README (Raster-to-Vector: Revisiting Floorplan Transformation) | 2017 | https://github.com/art-programmer/FloorplanTransformation | 아니오 |
| ref-066 | FloorPlanCAD 프로젝트(Fan, Z. 외) | FloorPlanCAD Dataset — project page (floorplancad.github.io index.md) | 2021 | https://floorplancad.github.io/ | 아니오 |
| ref-067 | Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P. | FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting | 2021-05 | https://arxiv.org/abs/2105.07147 | 아니오 |
| ref-068 | Voxel51 (Hugging Face) | Voxel51/FloorPlanCAD · Datasets at Hugging Face | 미확인 | https://huggingface.co/datasets/Voxel51/FloorPlanCAD | 아니오 |
| ref-069 | Pizarro, P. N., Hitschfeld, N., & Sipiran, I. (MLSTRUCT) | MLStructFP — README (Large-scale multi-unit floor plan dataset for architectural plan analysis and recognition) | 2023 | https://github.com/MLSTRUCT/MLStructFP | 아니오 |
| ref-070 | Hu, S. 외 | Raster-to-Graph — README (Raster-to-Graph: Floorplan Recognition via Autoregressive Graph Prediction with an Attention Transformer) | 2024 | https://github.com/SizheHu/Raster-to-Graph | 아니오 |
| ref-071 | Agour, M. 외 (ResPlan) | ResPlan — README (ResPlan: A Large-Scale Vector-Graph Dataset of 17,000 Residential Floor Plans) | 2025-08 | https://github.com/m-agour/ResPlan | 아니오 |
| ref-072 | van Engelenburg, C. 외 (MSD) | msd — README (MSD: A Benchmark Dataset for Floor Plan Generation of Building Complexes) | 2024 | https://github.com/caspervanengelenburg/msd | 아니오 |
| ref-073 | Luo, R. 외 | ArchCAD-400K: A Large-Scale CAD drawings Dataset and New Baseline for Panoptic Symbol Spotting | 2025-03 | https://arxiv.org/abs/2503.22346 | 아니오 |
| ref-074 | 한국지능정보사회진흥원(AI Hub) | 건축 도면 데이터 | 미확인 | https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=71465 | 아니오 |
| ref-075 | de las Heras, L.-P., Terrades, O. R., Robles, S., & Sánchez, G. | CVC-FP and SGT: a new database for structural floor plan analysis and its groundtruthing tool | 2015 | https://www.researchgate.net/publication/270597635_CVC-FP_and_SGT_a_new_database_for_structural_floor_plan_analysis_and_its_groundtruthing_tool | 아니오 |
| ref-076 | DeFazio, D., Mehta, H., Wang, M., Yang, P., Blackburn, J., & Zhang, S. | Vision Language Models Can Parse Floor Plan Maps | 2024-09 | https://arxiv.org/abs/2409.12842 | 아니오 |
| ref-077 | DoorDet 저자(arXiv 2508.07714) | DoorDet: Semi-Automated Multi-Class Door Detection Dataset via Object Detection and Large Language Models | 2025-08 | https://arxiv.org/abs/2508.07714 | 아니오 |
| ref-078 | Kratochvila, L., de Jong, G., Arkesteijn, M., Zemcik, T., Bilik, S., Horak, K., & Rellermeyer, J. S. | Multi-Unit Floor Plan Recognition and Reconstruction Using Improved Semantic Segmentation of Raster-Wise Floor Plans | 2024-08 | https://arxiv.org/abs/2408.01526 | 아니오 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 예 |
| ref-080 | Open Robotics | Navigation Maps (integration_nav-maps) - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/integration_nav-maps.html | 예 |
| ref-081 | Vega-Torres, M. A. 외 | Occupancy Grid Map to Pose Graph-based Map: Robust BIM-based 2D-LiDAR Localization for Lifelong Indoor Navigation in Changing and Dynamic Environments | 2023-08 | https://arxiv.org/abs/2308.05443 | 아니오 |
| ref-082 | Vega-Torres, M. A. (MigVega GitHub) | Ogm2Pgbm — README (Robust BIM-based 2D-LiDAR Localization for Lifelong Indoor Navigation in Changing and Dynamic Environments) | 미확인 | https://github.com/MigVega/Ogm2Pgbm | 예 |
| ref-083 | Zhang, J. 외 | Generation of Indoor Open Street Maps for Robot Navigation from CAD Files | 2025-07 | https://arxiv.org/abs/2507.00552 | 아니오 |
| ref-084 | Zhang, J. (jiajiezhang7 GitHub) | osmAG-from-cad — README (CAD-to-osmAG pipeline) | 미확인 | https://github.com/jiajiezhang7/osmAG-from-cad | 예 |
| ref-085 | Braga, R. G., Tahir, M. O., Karimi, S., Dah-Achinanon, U., Iordanova, I., & St-Onge, D. | Intuitive BIM-aided robotic navigation and assets localization with semantic user interfaces | 2025-03-26 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1548684/full | 아니오 |
| ref-086 | Palacz, W., Ślusarczyk, G., Strug, B., & Grabska, E. | Indoor Robot Navigation Using Graph Models Based on BIM/IFC | 2019 | https://www.researchgate.net/publication/333410520_Indoor_Robot_Navigation_Using_Graph_Models_Based_on_BIMIFC | 아니오 |
| ref-087 | Google Research | SayCan (google-research/saycan README) | 미확인 | https://github.com/google-research/google-research/blob/master/saycan/README.md | 아니오 |
| ref-088 | Ahn, M. 외(Google) | Do As I Can, Not As I Say: Grounding Language in Robotic Affordances | 2022-04 | https://arxiv.org/abs/2204.01691 | 아니오 |
| ref-089 | SMARTlab-Purdue (Purdue University) | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models (GitHub README) | 미확인 | https://github.com/SMARTlab-Purdue/SMART-LLM | 아니오 |
| ref-090 | Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models | 2023-09 | https://arxiv.org/abs/2309.10062 | 아니오 |
| ref-091 | Cranial-XIX (LLM+P 저자) | llm-pddl — LLM+P: Empowering Large Language Models with Optimal Planning Proficiency (GitHub README) | 미확인 | https://github.com/Cranial-XIX/llm-pddl | 아니오 |
| ref-092 | Liu, B., Jiang, Y., Zhang, X., Liu, Q., Zhang, S., Biswas, J., & Stone, P. | LLM+P: Empowering Large Language Models with Optimal Planning Proficiency | 2023-04 | https://arxiv.org/abs/2304.11477 | 아니오 |
| ref-093 | Huang, W., Abbeel, P., Pathak, D., & Mordatch, I. | Language Models as Zero-Shot Planners: Extracting Actionable Knowledge for Embodied Agents | 2022-07 | https://proceedings.mlr.press/v162/huang22a.html | 아니오 |
| ref-094 | Huang, W. (language-planner 공식 저장소) | language-planner — Official Code for "Language Models as Zero-Shot Planners" (GitHub README) | 미확인 | https://github.com/huangwl18/language-planner | 아니오 |
| ref-095 | Google Research | Code as Policies: Language Model Programs for Embodied Control (google-research/code_as_policies README) | 미확인 | https://github.com/google-research/google-research/blob/master/code_as_policies/README.md | 아니오 |
| ref-096 | Lamballais, T., Roy, D., & de Koster, M. B. M. | Estimating performance in a Robotic Mobile Fulfillment System | 2017 | https://repub.eur.nl/pub/107376/ | 아니오 |
| ref-097 | Lamballais, T., Roy, D., & de Koster, M. B. M. | Inventory allocation in robotic mobile fulfillment systems | 2020 | https://www.tandfonline.com/doi/abs/10.1080/24725854.2018.1560517 | 아니오 |
| ref-098 | Zou, B., Gong, Y., de Koster, R., & Xu, X. | Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system | 2018 | https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901 | 아니오 |
| ref-099 | Le-Anh, T., & de Koster, M. B. M. | A review of design and control of automated guided vehicle systems | 2006 | https://www.sciencedirect.com/science/article/abs/pii/S0377221705001840 | 아니오 |
| ref-100 | Vis, I. F. A. | Survey of research in the design and control of automated guided vehicle systems | 2006 | https://www.sciencedirect.com/science/article/abs/pii/S0377221704006459 | 아니오 |
| ref-101 | Merschformann, M. (RAWSim-O GitHub) | RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README) | 미확인 | https://github.com/merschformann/RAWSim-O | 예 |
| ref-102 | Springer(FAIM 2025 발표 논문, 저자 미확인) | Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics | 2025 | https://link.springer.com/chapter/10.1007/978-3-032-07675-5_69 | 아니오 |
| ref-103 | PMC 게재 논문(저자 미확인) | The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments | 미확인 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/ | 아니오 |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — Demonstrations of Open-RMF (README) | 미확인 | https://github.com/open-rmf/rmf_demos | 예 |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 미확인 | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml | 예 |
| ref-106 | 한국교통연구원(인증스마트물류센터) | 인증스마트물류센터 | 미확인 | https://cslc.koti.re.kr/ | 아니오 |
| ref-107 | 법제처 국가법령정보센터 | 물류시설의 개발 및 운영에 관한 법률 | 미확인 | https://www.law.go.kr/LSW/lsInfoP.do?lsId=000091 | 아니오 |
| ref-108 | 이문수, 채준재(로지스틱스연구) | AGV 기반 제조물류시스템의 성능평가를 위한 해석적 모형에 관한 연구 - 반도체 Tandem 레이아웃 시스템을 중심으로 - | 2010 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001485142 | 아니오 |
| ref-109 | Stark, H.-G. 외 | A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse | 2024-06 | https://arxiv.org/abs/2406.17003 | 아니오 |
| ref-110 | Open Robotics | Tasks in RMF (task_new) - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/task_new.html | 예 |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 예 |
| ref-112 | OMG(Object Management Group) | About the Business Process Model And Notation Specification Version 2.0 | 미확인 | https://www.omg.org/spec/BPMN/2.0/About-BPMN | 아니오 |
| ref-113 | Camunda | Messages | Camunda 8 Docs (camunda-docs: docs/components/concepts/messages.md) | 미확인 | https://docs.camunda.io/docs/components/concepts/messages/ | 예 |
| ref-114 | Corradini, F., Pettinari, S., Re, B., Rossi, L., & Tiezzi, F. | A BPMN-driven framework for Multi-Robot System development | 2023 | https://www.sciencedirect.com/science/article/abs/pii/S0921889022002111 | 아니오 |
| ref-115 | Production & Manufacturing Research 게재 논문(저자 미확인, Chalmers 공개본) | Throughput bottleneck detection in manufacturing: a systematic review of the literature on methods and operationalization modes | 2023 | https://www.tandfonline.com/doi/full/10.1080/21693277.2023.2283031 | 아니오 |
| ref-116 | Filippone, G., Pettinari, S., & Pelliccione, P. | Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis | 2026-03 | https://arxiv.org/abs/2603.15427 | 아니오 |
| ref-117 | MESA International | B2MML-BatchML — Schema/B2MML-Common.xsd | 2023 | https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-Common.xsd | 예 |
| ref-118 | MESA International | B2MML-BatchML — Schema/B2MML-OperationsDefinition.xsd | 미확인 | https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-OperationsDefinition.xsd | 예 |
| ref-119 | IEC / ISO | IEC 62264-3:2016 - Enterprise-control system integration — Part 3: Activity models of manufacturing operations management | 2016 | https://www.iso.org/standard/67480.html | 아니오 |
| ref-120 | Boniardi, F., Valada, A., Mohan, R., Caselitz, T., & Burgard, W. | Robot Localization in Floor Plans Using a Room Layout Edge Extraction Network | 2019-03 | https://arxiv.org/abs/1903.01804 | 아니오 |
| ref-121 | Blondin, M., Mazowiecki, F., & Offtermatt, P. (LICS 2022) | The complexity of soundness in workflow nets | 2022 | https://arxiv.org/abs/2201.05588 | 아니오 |
| ref-122 | arXiv:2403.01975 저자(미확인) | OCEL (Object-Centric Event Log) 2.0 Specification | 2024-03 | https://arxiv.org/abs/2403.01975 | 아니오 |
| ref-123 | ASCM | SCOR Model — Fulfill F1.3 Pick Product | 미확인 | https://scor.ascm.org/processes/fulfill/F1.3 | 아니오 |
| ref-124 | 국가물류통합정보센터(국토교통부) | 스마트물류센터 인증제 안내 | 미확인 | https://www.nlic.go.kr/nlic/board0010.action?S_DOC_ID=5897&S_DOC_SEQ=&command=VIEW | 아니오 |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 미확인 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json | 아니오 |
| ref-126 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/cancel_task_request.json | 미확인 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/cancel_task_request.json | 아니오 |
| ref-127 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/interrupt_task_request.json | 미확인 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/interrupt_task_request.json | 아니오 |
| ref-128 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/rewind_task_request.json | 미확인 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/rewind_task_request.json | 아니오 |
| ref-129 | MESA International | B2MML-BatchML/Schema/B2MML-TransactionProfile.xsd | 2023 | https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-TransactionProfile.xsd | 아니오 |
| ref-130 | OPC Foundation | UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv) | 2024-01-31 | https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL | 아니오 |
| ref-131 | OPC Foundation / ISA | OPC UA for ISA-95 - Part 4: Job Control - 6.2 ObjectTypes (OPC 10031-4) | 미확인 | https://reference.opcfoundation.org/specs/OPC-10031-4/6.2 | 아니오 |
| ref-132 | Yu, S., & Srinivas, S. | Collaborative Human–Robot Teaming for Dynamic Order Picking: Interventionist strategies for improving warehouse intralogistics operations | 2025 | https://www.sciencedirect.com/science/article/abs/pii/S1366554525001231 | 아니오 |
| ref-133 | Lorenz, Otto, & Gendreau (Networks, Wiley) | Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization? | 2025 | https://onlinelibrary.wiley.com/doi/full/10.1002/net.22281 | 아니오 |
| ref-134 | Gallien, J., & Weber, T. G. | To Wave or Not to Wave? Order Release Policies for Warehouses with an Automated Sorter | 2010 | https://pubsonline.informs.org/doi/abs/10.1287/msom.1100.0291 | 아니오 |
| ref-135 | ASCM | SCOR Digital Standard — Introduction and Front Matter (SCOR Version 14.0, 2025) | 2025 | https://www.ascm.org/globalassets/ascm_website_assets/docs/scor/intro-and-front-matter-scor-digital-standard-2025.pdf | 아니오 |
| ref-136 | Applied Sciences(MDPI) 게재 논문 저자(미확인) | Integrated Fleet Management of Mobile Robots for Enhancing Industrial Efficiency: A Case Study on Interoperability in Multi-Brand Environments Within the Automotive Sector | 2025 | https://www.mdpi.com/2076-3417/15/13/7235 | 아니오 |
| ref-137 | 머니투데이 | 물류센터 관리시스템에 로봇 연동…"물류 자동화 새 표준 만든다" | 2025-01 | https://news.mt.co.kr/mtview.php?no=2025012116183583251 | 아니오 |
| ref-138 | 국가표준인증통합정보시스템(KSSN) | KS B 7321-2 로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델 | 미확인 | https://www.kssn.net/search/stddetail.do?itemNo=K001010147546 | 아니오 |
| ref-139 | ISO | ISO 22400-2:2014 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions | 2014 | https://www.iso.org/standard/54497.html | 아니오 |
| ref-140 | ASCM | SCOR Model — Performance: Reliability RL.1.1 Perfect Customer Order Fulfillment | 미확인 | https://scor.ascm.org/performance/reliability/RL.1.1 | 아니오 |
| ref-141 | WERC(Warehousing Education and Research Council) | WERC DC Measures Survey - 2025 | 2025 | https://wercmetrics.werc.org/WERC-DC-Measures-Survey-2025.pdf | 아니오 |
| ref-142 | Computers & Industrial Engineering 게재 논문(저자 미확인) | Overall Equipment Effectiveness: consistency of ISO standard with literature | 2020 | https://www.sciencedirect.com/science/article/abs/pii/S0360835220302527 | 아니오 |
| ref-143 | Project Production Institute | Little’s Law – A Practical Approach to Understanding Production System Performance | 미확인 | https://projectproduction.org/journal/littles-law-a-practical-approach-to-understanding-production-system-performance/ | 아니오 |
| ref-144 | Azadeh, K., de Koster, R., & Roy, D. | Robotized and Automated Warehouse Systems: Review and Recent Developments | 2019 | https://pubsonline.informs.org/doi/abs/10.1287/trsc.2018.0873 | 아니오 |
| ref-145 | Ghelichi, Z., & Kilaru, S. | Analytical models for collaborative autonomous mobile robot solutions in fulfillment centers | 2021 | https://www.sciencedirect.com/science/article/pii/S0307904X20305801 | 아니오 |
| ref-146 | Omega 게재 논문(저자 미확인) | The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority | 2024 | https://www.sciencedirect.com/science/article/abs/pii/S0305048324001336 | 아니오 |
| ref-147 | Process Intelligence Solutions (PM4Py GitHub) | pm4py — Official public repository for PM4Py (Process Mining for Python) (README) | 미확인 | https://github.com/process-intelligence-solutions/pm4py | 예 |
| ref-148 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json | 미확인 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json | 예 |
| ref-149 | Springer(학술대회 발표 논문, 저자 미확인) | Material Movement Analysis for Warehouse Business Process Improvement with Process Mining: A Case Study | 2015 | https://link.springer.com/chapter/10.1007/978-3-319-19509-4_9 | 아니오 |
| ref-150 | CIO Korea | 오토스토어, 물류 자동화 시스템의 경제적 효과 연구 보고서 발표 | 미확인 | https://www.cio.com/article/3517636/%EC%98%A4%ED%86%A0%EC%8A%A4%ED%86%A0%EC%96%B4-%EB%AC%BC%EB%A5%98-%EC%9E%90%EB%8F%99%ED%99%94-%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%9D%98-%EA%B2%BD%EC%A0%9C%EC%A0%81-%ED%9A%A8%EA%B3%BC-%EC%97%B0%EA%B5%AC.html | 아니오 |
| ref-151 | 박정수, 안영효(유통경영학회지) | 화주기업과 물류기업의 공동 핵심성과지표 관리방법에 대한 연구 | 2010 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001434387 | 아니오 |
| ref-152 | Meseguer Valenzuela, A., & Blanes Noguera, F. | Task Allocation in Mobile Robot Fleets: A review | 2025-01 | https://arxiv.org/abs/2501.08726 | 아니오 |
| ref-153 | Open Robotics | Fleet Adapter Tutorial - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html | 예 |
| ref-154 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/location_2D.json | 미확인 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/location_2D.json | 예 |
| ref-155 | ROS (ros-infrastructure/rep) | REP 105 -- Coordinate Frames for Mobile Platforms | 미확인 | https://www.ros.org/reps/rep-0105.html | 예 |
| ref-156 | buildingSMART International | IFC 4.3 documentation — IfcSpace (IFC4.3.x-development) | 미확인 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcSpace.md | 예 |
| ref-157 | OGC IndoorGML SWG (opengeospatial/IndoorGML-SWG GitHub) | IndoorGML-SWG — README and OGC IndoorGML 2.0 Part 2a – XML Encoding (26-042, Candidate SWG Draft) | 미확인 | https://github.com/opengeospatial/IndoorGML-SWG | 예 |
| ref-158 | ISO | ISO 19164:2024 - Geographic information — Indoor feature model | 2024 | https://www.iso.org/standard/83153.html | 아니오 |
| ref-159 | ISO | ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability | 미확인 | https://www.iso.org/standard/86749.html | 아니오 |
| ref-160 | Prakhya, S. M., Yang, L., & Liu, Z. | Lifelong 3D Mapping Framework for Hand-held & Robot-mounted LiDAR Mapping Systems | 2025-01 | https://arxiv.org/abs/2501.18110 | 아니오 |
| ref-161 | Abdul Hafez, O., Joerger, M., & Spenko, M. | Quantifying mobile robot localization safety for an EKF-based SLAM estimator: An integrity monitoring approach | 2025-05 | https://journals.sagepub.com/doi/10.1177/02783649241287797 | 아니오 |
| ref-162 | GS1 | Identifying a physical location - GLN | 미확인 | https://www.gs1.org/standards/id-keys/gln/physical-location | 아니오 |
| ref-163 | 노주형, 강규리, 김연찬, 심현철(로봇학회 논문지) | 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템 | 2026 | https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667 | 아니오 |
| ref-164 | TASL Lab (LaMMA-P 저자) | LaMMA-P: Generalizable Multi-Agent Long-Horizon Task Allocation and Planning with LM-Driven PDDL Planner (GitHub README) | 미확인 | https://github.com/tasl-lab/LaMMA-P | 예 |
| ref-165 | Autonomous Robots 게재 서베이(arXiv 2502.03814) 저자 | Large Language Models for Multi-Robot Systems: A Survey | 2025-02 | https://arxiv.org/abs/2502.03814 | 아니오 |
| ref-166 | Obata, K., Aoki, T., Horii, T., Taniguchi, T., & Nagai, T. | LiP-LLM: Integrating Linear Programming and dependency graph with Large Language Models for multi-robot task planning | 2024-10 | https://arxiv.org/abs/2410.21040 | 아니오 |
| ref-167 | Peng, M., Chen, Z., Yang, J., Huang, J., Shi, Z., Liu, Q., Li, X., & Gao, L. | Automatic MILP Model Construction for Multi-Robot Task Allocation and Scheduling Based on Large Language Models | 2025-03 | https://arxiv.org/abs/2503.13813 | 아니오 |
| ref-168 | Kaitha, S., & Yu, S. 외(arXiv 2512.02810) | Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms | 2025-12 | https://arxiv.org/abs/2512.02810 | 아니오 |
| ref-169 | SHAILAB-IPEC (COHERENT 저자) | COHERENT: Collaboration of Heterogeneous Multi-Robot System with Large Language Models (GitHub README) | 미확인 | https://github.com/SHAILAB-IPEC/COHERENT | 예 |
| ref-170 | Su, X., Xu, J., van Kaick, O., Xu, K., & Hu, R. | IMR-LLM: Industrial Multi-Robot Task Planning and Program Generation using Large Language Models | 2026-03 | https://arxiv.org/abs/2603.02669 | 아니오 |
| ref-171 | NASA Jet Propulsion Laboratory (nasa-jpl) | ROSA — ROS Agent (GitHub README) | 미확인 | https://github.com/nasa-jpl/rosa | 예 |
| ref-172 | NASA Jet Propulsion Laboratory (nasa-jpl) | Custom Agents · nasa-jpl/rosa Wiki | 미확인 | https://github.com/nasa-jpl/rosa/wiki/Custom-Agents | 예 |
| ref-173 | Microsoft | PromptCraft-Robotics (GitHub README) | 미확인 | https://github.com/microsoft/PromptCraft-Robotics | 예 |
| ref-174 | Vemprala, S., Bonatti, R., Bucker, A., & Kapoor, A. (Microsoft) | ChatGPT for Robotics: Design Principles and Model Abilities | 2023-07 | https://arxiv.org/abs/2306.17582 | 아니오 |
| ref-175 | Robotec.ai (RobotecAI) | RAI — vendor agnostic agentic framework for Physical AI robotics (GitHub README) | 미확인 | https://github.com/RobotecAI/rai | 예 |
| ref-176 | InOrbit.AI | InOrbit Unveils RobOps Copilot for AI-Powered Robot Optimization at Automate 2024 | 2024-05 | https://www.inorbit.ai/press/inorbit-robops-copilot | 아니오 |
| ref-177 | InOrbit.AI (RoboticsTomorrow 게재 보도자료) | InOrbit.AI Demonstrates the Future of Multi-Vendor Robot Orchestration and Physical AI at Automate 2026 | 2026-06-22 | https://www.roboticstomorrow.com/news/2026/06/22/inorbitai-demonstrates-the-future-of-multi-vendor-robot-orchestration-and-physical-ai-at-automate-2026/26757/ | 아니오 |
| ref-178 | Formant (Business Wire 보도자료) | Formant F3 Brings Generative AI and Agentic Reasoning to Robot Ops | 2025-06-30 | https://www.businesswire.com/news/home/20250630008190/en/Formant-F3-Brings-Generative-AI-and-Agentic-Reasoning-to-Robot-Ops | 아니오 |
| ref-179 | 와우테일 | 다임리서치, 중기부-인텔 '인지니어스' 글로벌 협업 기업 선정 | 2026-08-27 | https://wowtale.net/2026/08/27/263530/ | 아니오 |
| ref-180 | 이종록, 황정훈, 박민철(한국전자기술연구원) | LLM 기반 로봇관제시스템의 Agent AI 구축 | 미확인 | https://d2j16w31g89z0j.cloudfront.net/site/2026w/abs/0560-YDVVV.pdf | 아니오 |
| ref-181 | Shi, G., Wu, Y., Kumar, V., & Sukhatme, G. S. | PIP-LLM: Integrating PDDL-Integer Programming with LLMs for Coordinating Multi-Robot Teams Using Natural Language | 2025-10 | https://arxiv.org/abs/2510.22784 | 아니오 |
| ref-182 | ECLASS e.V. | Neuer Content für ECLASS Release 15.0 | 미확인 | https://eclass.eu/aktuelles/news/neuer-content-fuer-eclass-release-150 | 아니오 |
| ref-183 | IEC TC 3 | Common Data Dictionary – CDD – TC 3 | 미확인 | https://tc3.iec.ch/tc-activity/common-data-dictionary-cdd/ | 아니오 |
| ref-184 | ECLASS e.V. | Classification Class - ECLASS Technischer Support | 미확인 | https://eclass.eu/support/technical-specification/structure-and-elements/classification-class | 아니오 |
| ref-185 | ECLASS e.V. | The latest ECLASS Release | 미확인 | https://eclass.eu/en/eclass-standard/releases | 아니오 |
| ref-186 | Stern, R., Sturtevant, N. R., Felner, A., Koenig, S. 외 | Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks | 2019-06 | https://arxiv.org/abs/1906.08291 | 아니오 |
| ref-187 | Sharon, G., Stern, R., Felner, A., & Sturtevant, N. R. | Conflict-based search for optimal multi-agent pathfinding | 2015 | https://dl.acm.org/doi/10.1016/j.artint.2014.11.006 | 아니오 |
| ref-188 | Hönig, W., Kiesel, S. 외 | Persistent and Robust Execution of MAPF Schedules in Warehouses | 2019 | https://ieeexplore.ieee.org/abstract/document/8620328/ | 아니오 |
| ref-189 | Okumura, K., Machida, M., Défago, X., & Tamura, Y. | Priority Inheritance with Backtracking for Iterative Multi-agent Path Finding | 2019-01 | https://arxiv.org/abs/1901.11282 | 아니오 |
| ref-190 | Yu, J., & LaValle, S. M. | Optimal Multi-Robot Path Planning on Graphs: Structure and Computational Complexity | 2015-07 | https://arxiv.org/abs/1507.03289 | 아니오 |
| ref-191 | DiligentPanda (Team Pikachu, GitHub) | MAPF-LRR2023 — README (Team Pikachu's solution in the League of Robot Runners Competition 2023) | 미확인 | https://github.com/DiligentPanda/MAPF-LRR2023 | 예 |
| ref-192 | Bonetti, A., Proia, S., Guidetti, S., & Sabattini, L. | A traffic management system for large and heterogeneous vehicles in narrow industrial environments | 2026-09 | https://arxiv.org/abs/2609.10400 | 아니오 |
| ref-193 | IEEE 게재 논문 저자(미확인) | Hierarchical Traffic Management of Multi-AGV Systems With Deadlock Prevention Applied to Industrial Environments | 2023 | https://ieeexplore.ieee.org/document/10132864/ | 아니오 |
| ref-194 | 전진표, 강재호, 류광렬, 김갑환, 윤항묵(한국항해항만학회지) | 자동화 컨테이너 터미널에서 AGV 교착 방지와 회귀 분석을 이용한 경로 선정 방안 | 2005 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001130155 | 아니오 |
| ref-195 | Phillips, M., & Likhachev, M. | SIPP: Safe interval path planning for dynamic environments | 2011 | https://www.researchgate.net/publication/224252713_SIPP_Safe_interval_path_planning_for_dynamic_environments | 아니오 |
| ref-196 | Ma, H., Koenig, S. 외 | Overview: Generalizations of Multi-Agent Path Finding to Real-World Scenarios | 2017-02 | https://arxiv.org/abs/1702.05515 | 아니오 |
| ref-197 | Open Robotics (open-rmf) | rmf_traffic — README | 미확인 | https://github.com/open-rmf/rmf_traffic | 예 |
| ref-198 | IDTA(Industrial Digital Twin Association) | IDTA 02047-1-0 Technical Data for AGV in Intralogistics | 2025-03 | https://industrialdigitaltwin.org/wp-content/uploads/2025/03/IDTA-02047-1-0-Submodel_Technical-Data-for-AGV.pdf | 아니오 |
| ref-199 | arXiv 2410.21415 저자(미확인) | Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding | 2024-10 | https://arxiv.org/abs/2410.21415 | 아니오 |
| ref-200 | IDTA / ECLASS e.V. | GUIDELINE How to transport ECLASS in the Asset Administration Shell (IDTA ECLASS Semantic Transport, 1.0) | 2024-10 | https://industrialdigitaltwin.org/wp-content/uploads/2024/10/2024-10_IDTA_ECLASS_Semantic_Transport_ECLASS_in_AAS_1.0.pdf | 아니오 |
| ref-201 | Nabizada, H., Wirt, T., Vieira da Silva, L. M., Gehlhoff, F., & Fay, A. | From Capability Models to Automated Planning: An AAS-Native Approach for Automatic PDDL Generation | 2026-06 | https://arxiv.org/abs/2606.02167 | 아니오 |
| ref-202 | SEMI | E08400 - SEMI E84 - Specification for Enhanced Carrier Handoff Parallel I/O Interface | 미확인 | https://store-us.semi.org/products/e08400-semi-e84-specification-for-enhanced-carrier-handoff-parallel-i-o-interface | 아니오 |
| ref-203 | PEER Group | SEMI E84: Carrier Handoff | 미확인 | https://www.peergroup.com/definition-of-standard/semi-e84/ | 아니오 |
| ref-204 | ASTM International | Standard Test Method for Confirming the Docking Performance of A-UGVs (ASTM F3499-21) | 2021 | https://www.astm.org/f3499-21.html | 아니오 |
| ref-205 | NIST | Design and Application of the Reconfigurable Mobile Manipulator Artifact (RMMA) | 미확인 | https://www.nist.gov/publications/design-and-application-reconfigurable-mobile-manipulator-artifact-rmma | 아니오 |
| ref-206 | Bostelman, R. 외(NIST) | Mobile Robot and Mobile Manipulator Research Towards ASTM Standards Development | 미확인 | https://pubmed.ncbi.nlm.nih.gov/28690359/ | 아니오 |
| ref-207 | Tuci, E., Alkilabi, M. H. M., & Akanyeti, O. | Cooperative Object Transport in Multi-Robot Systems: A Review of the State-of-the-Art | 2018 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2018.00059/full | 아니오 |
| ref-208 | Coltin, B., & Veloso, M. | Online pickup and delivery planning with transfers for mobile robots | 2014 | https://www.researchgate.net/publication/289338501_Online_pickup_and_delivery_planning_with_transfers_for_mobile_robots | 아니오 |
| ref-209 | Zang, C. 외 | Lifelong Multi-Subsystem Pickup and Delivery with Buffer-Limited Handover Stations | 2026-07 | https://arxiv.org/abs/2607.17724 | 아니오 |
| ref-210 | ANSI / A3(Association for Advancing Automation) | ANSI/A3 R15.08-2-2023 - Industrial Mobile Robots - Safety Requirements - Part 2: Requirements for IMR system(s) and IMR application(s) | 2023 | https://webstore.ansi.org/standards/ria/ansia3r15082023 | 아니오 |
| ref-211 | 국가표준인증통합정보시스템(KSSN) | KS B ISO 10218-2 로봇 및 로봇 장치 - 산업용 로봇의 안전에 관한 요구사항 - 제2부: 로봇 시스템 및 통합 | 미확인 | https://www.kssn.net/search/stddetail.do?itemNo=K001010083660 | 아니오 |
| ref-212 | continua-systems (GitHub) | vdma-lif — schema/lif-schema.json (JSON parsers and models for the VDMA LIF, VDMA 공식 산출물이 아닌 제3자 스키마) | 미확인 | https://github.com/continua-systems/vdma-lif/blob/main/schema/lif-schema.json | 아니오 |
| ref-213 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcTransportElement (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 미확인 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcTransportElement.md | 아니오 |
| ref-214 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcOutletTypeEnum (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 미확인 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/domain/IfcElectricalDomain/Types/IfcOutletTypeEnum.md | 아니오 |
| ref-215 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcElectricApplianceTypeEnum (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 미확인 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/domain/IfcElectricalDomain/Types/IfcElectricApplianceTypeEnum.md | 아니오 |
| ref-216 | ROS Navigation (ros-navigation/navigation2 GitHub) | nav2_docking — README (Open Navigation's Nav2 Docking Framework) | 미확인 | https://github.com/ros-navigation/navigation2/blob/main/nav2_docking/README.md | 아니오 |
| ref-217 | Beinschob, P., Meyer, M., Reinke, C., Digani, V., Secchi, C., & Sabattini, L. | Semi-automated map creation for fast deployment of AGV fleets in modern logistics | 2017 | https://www.sciencedirect.com/science/article/abs/pii/S0921889015302724 | 아니오 |
| ref-218 | Digani, V., Sabattini, L., Secchi, C., & Fantuzzi, C. | An automatic approach for the generation of the roadmap for multi-AGV systems in an industrial environment | 2014 | https://www.researchgate.net/publication/286354583_An_automatic_approach_for_the_generation_of_the_roadmap_for_multi-AGV_systems_in_an_industrial_environment | 아니오 |
| ref-219 | Mobile Industrial Robots(MiR) (ManualsLib 게재본) | MiR Charge 24V Operating Manual — Setting charging station markers on the map (제조사 공식 사이트가 아닌 매뉴얼 게재 사이트 사본) | 미확인 | https://www.manualslib.com/manual/1941068/Mir-Mir-Charge-24v.html?page=23 | 아니오 |
| ref-220 | Pointr | IMDF from Floor Plan & CAD Conversion Services | 미확인 | https://www.pointr.tech/technology/imdf | 아니오 |
| ref-221 | Vega Torres, M. A., Braun, A., & Borrmann, A. | BIM-SLAM: Integrating BIM Models in Multi-session SLAM for Lifelong Mapping using 3D LiDAR | 2024-08 | https://arxiv.org/abs/2408.15870 | 아니오 |
| ref-222 | Navitec Systems | Universal Fleet Control Software for AGVs & AMRs | 미확인 | https://navitecsystems.com/universal-fleet-control/ | 아니오 |
| ref-223 | Boniardi, F., Caselitz, T., Kümmerle, R., & Burgard, W. | Robust LiDAR-based localization in architectural floor plans | 2017 | http://ais.informatik.uni-freiburg.de/publications/papers/boniardi17iros.pdf | 아니오 |
| ref-224 | Shaheer, M., Millan-Romera, J. A., Bavle, H., Giberna, M., Sanchez-Lopez, J. L., Civera, J., & Voos, H. | Tightly Coupled SLAM with Imprecise Architectural Plans | 2024-08 | https://arxiv.org/abs/2408.01737 | 아니오 |
| ref-225 | Diakité, A. A., Díaz-Vilariño, L., Biljecki, F., Isikdag, Ü., Simmons, S., Li, K., & Zlatanova, S. | IFC2INDOORGML: An Open-Source Tool for Generating IndoorGML from IFC | 2022 | https://isprs-archives.copernicus.org/articles/XLIII-B4-2022/295/2022/ | 아니오 |
| ref-226 | 박근홍, 박병준, 이슬기(한국산학기술학회논문지) | BIM-건설로봇 통합 연구의 체계적 문헌고찰 (한국산학기술학회논문지 26(11), 218-225, DOI 10.5762/KAIS.2025.26.11.218) | 2025 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003269295 | 아니오 |
| ref-227 | Mobile Industrial Robots(MiR) | MiR Fleet Enterprise Documentation Version 1.2 (en) — 유통사(jk.de) 게재본 | 2025-01 | https://jk.de/media/a2/50/ce/1738939330/mir_fleet_enterprise_documentation_1.2_en.pdf?ts=1738939330 | 아니오 |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema | 예 |
| ref-229 | IDTA(Industrial Digital Twin Association) | IDTA 02020 Capability Description 1.0 — README (admin-shell-io/submodel-templates) | 미확인 | https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description | 아니오 |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 미확인 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json | 예 |
| ref-231 | CaSkade-Automation (GitHub) | CaSkMan - An OWL ontology to model capabilities and skills in manufacturing (README) | 미확인 | https://github.com/CaSkade-Automation/CaSkMan | 예 |
| ref-232 | Helmut Schmidt University, Institute of Automation Technology (hsu-aut GitHub) | IndustrialStandard-ODP-IEEE1872-2 — README (IEEE 1872.2 AuR ontology OWL implementation) | 미확인 | https://github.com/hsu-aut/IndustrialStandard-ODP-IEEE1872-2 | 예 |
| ref-233 | EASE CRC (ease-crc/soma) | SOMA — README (Socio-physical Model of Activities) | 미확인 | https://github.com/ease-crc/soma | 예 |
| ref-234 | IDTA(Industrial Digital Twin Association) | IDTA 02047 Technical Data for Automated Guided Vehicles 1.0 — README (admin-shell-io/submodel-templates) | 미확인 | https://github.com/admin-shell-io/submodel-templates/tree/main/published/Technical%20Data%20for%20Automated%20Guided%20Vehicles | 아니오 |
| ref-235 | W3C / OGC Spatial Data on the Web WG (w3c/sdw GitHub) | ssn/integrated/ssn-system.ttl (SSN System Capabilities module) | 미확인 | https://github.com/w3c/sdw/blob/gh-pages/ssn/integrated/ssn-system.ttl | 예 |
| ref-236 | Electronics(MDPI) 게재 논문(저자 미확인) | Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation | 2026-08-11 | https://doi.org/10.3390/electronics15163562 | 아니오 |
| ref-237 | Kluge-Wilkes, A. 외(RWTH Aachen WZL) | Ontology-based task allocation for heterogeneous resources in Line-less Mobile Assembly Systems | 2022 | https://www.techrxiv.org/users/685235/articles/679210-ontology-based-task-allocation-for-heterogeneous-resources-in-line-less-mobile-assembly-systems | 아니오 |
| ref-238 | Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A. | On the Use of Large Language Models to Generate Capability Ontologies | 2024-04 | https://arxiv.org/abs/2404.17524 | 아니오 |
| ref-239 | Dussard, B., & Sarthou, G. (LAAS-CNRS) | Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF | 2026-06 | https://arxiv.org/abs/2606.17073 | 아니오 |
| ref-240 | ISO | ISO 22166-201:2024 - Robotics — Modularity for service robots — Part 201: Common information model for modules | 2024-02 | https://www.iso.org/standard/82334.html | 아니오 |
| ref-241 | Sommer, M., Stjepandić, J., Stobrawa, S., & von Soden, M. | Automated generation of digital twin for a built environment using scan and object detection as input for production planning | 2023 | https://www.sciencedirect.com/science/article/abs/pii/S2452414X23000353 | 아니오 |
| ref-242 | Rivera, C., Byrd, G., Booker, M., Kemp, B., Gaines, A., Holmes, E., Uplinger, J., de Melo, C. M., & Handelman, D.(JHU APL·JHU·DEVCOM ARL) | FLEET: Formal Language-Grounded Scheduling for Heterogeneous Robot Teams | 2025-10 | https://arxiv.org/abs/2510.07417 | 아니오 |
| ref-243 | IDTA (admin-shell-io/submodel-templates) | IDTA 02020_Template_Capability_Description.json | 미확인 | https://github.com/admin-shell-io/submodel-templates/blob/main/published/Capability%20Description/1/0/IDTA%2002020_Template_Capability_Description.json | 예 |
| ref-244 | OPC Foundation (UA-Nodeset GitHub) | UA-Nodeset Robotics — Opc.Ua.Robotics.Nodeset2.documentation.csv | 미확인 | https://github.com/OPCFoundation/UA-Nodeset/blob/latest/Robotics/Opc.Ua.Robotics.Nodeset2.documentation.csv | 예 |
| ref-245 | IDTA (admin-shell-io/submodel-templates) | IDTA 02047-1-0 Template_TechnicalDataForAGV.json | 미확인 | https://github.com/admin-shell-io/submodel-templates/blob/main/published/Technical%20Data%20for%20Automated%20Guided%20Vehicles/1/0/IDTA%2002047-1-0%20Template_TechnicalDataForAGV.json | 예 |
| ref-246 | Sidorenko, A., Volkmann, M., Motsch, W., Wagner, A., & Ruskowski, M. | An OPC UA Model of the Skill Execution Interaction Protocol for the Active Asset Administration Shell | 2021 | https://www.sciencedirect.com/science/article/pii/S2351978921002249 | 아니오 |
| ref-247 | IDTA(Industrial Digital Twin Association) | Specification of the Asset Administration Shell Part 3a: Data Specification – IEC 61360 (IDTA-01003-a-3-0-2) | 2024-07 | https://industrialdigitaltwin.org/wp-content/uploads/2024/07/IDTA-01003-a-3-0-2_SpecificationAssetAdministrationShell_Part3a_DataSpecification_IEC613601.pdf | 아니오 |
| ref-248 | ISO | ISO 22166-202:2025 - Robotics — Modularity for service robots — Part 202: Information model for software modules | 2025 | https://www.iso.org/standard/84589.html | 아니오 |
| ref-249 | Dussard, B. 외 | Ontological Component-based Description of Robot Capabilities | 2023-06 | https://arxiv.org/abs/2306.07569 | 아니오 |
| ref-250 | RVMI lab, Aalborg University (SkiROS2 GitHub) | SkiROS2 — README (skill-based robot control platform) | 미확인 | https://github.com/RVMI/skiros2 | 예 |
| ref-251 | Open Robotics | Mobile Robot Fleets (integration_fleets) - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/integration_fleets.html | 예 |
| ref-252 | Open Robotics | Integration (integration) - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/integration.html | 예 |
| ref-253 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — README | 미확인 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard | 아니오 |
| ref-254 | Open Robotics (open-rmf) | awesome_adapters — A curated list of adapters from the community which can be used with Open-RMF (README) | 미확인 | https://github.com/open-rmf/awesome_adapters | 예 |
| ref-255 | InOrbit (inorbit-ai GitHub) | ros_amr_interop — README (ROS packages for AMR interoperability: VDA5050 connector, MassRobotics AMR sender) | 미확인 | https://github.com/inorbit-ai/ros_amr_interop | 예 |
| ref-256 | Open Robotics (open-rmf) | free_fleet — README (A free fleet management system) | 미확인 | https://github.com/open-rmf/free_fleet | 예 |
| ref-257 | Interact Analysis | AMR Multi-Fleet Orchestration Software Explained | 미확인 | https://interactanalysis.com/insight/amr-multi-fleet-orchestration-software/ | 아니오 |
| ref-258 | ARM Institute | Interoperability and Orchestration of Autonomous Mobile Robots (IO-AMRs) | 미확인 | https://arminstitute.org/projects/interoperability-and-orchestration-of-autonomous-mobile-robots-io-amrs/ | 아니오 |
| ref-259 | Franke, S., Lünsch, D., Jost, J., & Roidl, M. | Identification of requirements and opportunities for new types of standardized interfaces for AGV systems based on the VDA 5050 concept | 2023 | https://www.researchgate.net/publication/374741902_Identification_of_requirements_and_opportunities_for_new_types_of_standardized_interfaces_for_AGV_systems_based_on_the_VDA_5050_concept | 아니오 |
| ref-260 | ScienceDirect 게재 논문(저자 미확인) | Heterogeneous multi-agent fleet control system for material handling in a Software-Defined Factory | 2026 | https://www.sciencedirect.com/science/article/abs/pii/S0278612526000166 | 아니오 |
| ref-261 | 헬로티(HelloT) | 미르, 다기종 모바일 로봇 연동 SW 어댑터 ‘MiR VDA 5050’ 론칭 | 미확인 | https://www.hellot.net/news/article.html?no=99467 | 아니오 |
| ref-262 | 클로봇(Clobot) | 통합 로봇 관제 플랫폼 크롬스[CROMS] | 미확인 | https://clobot.co.kr/croms | 아니오 |
| ref-263 | 디지털투데이 | 카카오모빌리티, 로봇 플랫폼 사업 본격화..."이기종 로봇 통합 운영" | 2026-05 | https://www.digitaltoday.co.kr/news/articleView.html?idxno=665333 | 아니오 |
| ref-264 | 머니투데이 | "로봇 통합 관제 기술, 인정받았다"..노바테크, 70억원 투자 유치 | 2026-07-14 | https://www.mt.co.kr/industry/2026/07/14/2026071409414468672 | 아니오 |
| ref-265 | European Commission (CORDIS) | PAN-ROBOTS: Automating logistics for the factory of the future | 미확인 | https://cordis.europa.eu/article/id/160857-panrobots-automating-logistics-for-the-factory-of-the-future | 아니오 |
| ref-266 | Beinschob, P., & Reinke, C. | Graph SLAM based mapping for AGV localization in large-scale warehouses | 2015 | https://ieeexplore.ieee.org/document/7312637/ | 아니오 |
| ref-267 | IEEE 게재 논문 저자(미확인) | Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)) | 2024 | https://ieeexplore.ieee.org/document/10287275/ | 아니오 |
| ref-268 | Rüdt, M., Enke, C., & Furmans, K. (KIT) | Automated Generation of Continuous-Space Roadmaps for Routing Mobile Robot Fleets (v2 제목: Continuous-Space Roadmap Generation for Mobile Robot Fleets with Distance Constraints and Geometry-Aware Discretization) | 2025-11 | https://arxiv.org/abs/2511.07175 | 아니오 |
| ref-269 | Heselden, J. R., & Das, G. P. | Unified Map Handling for Robotic Systems: Enhancing Interoperability and Efficiency Across Diverse Environments | 2024-04 | https://arxiv.org/abs/2404.13499 | 아니오 |
| ref-270 | Macenski, S. (SteveMacenski GitHub) | slam_toolbox — README (Slam Toolbox for lifelong mapping and localization in potentially massive maps with ROS) | 미확인 | https://github.com/SteveMacenski/slam_toolbox | 예 |
| ref-271 | OTTO Motors (Rockwell Automation) | Maximize AMR productivity and simplify commissioning with our latest software release | 2023 | https://ottomotors.com/blog/amr-productivity-software-release/ | 아니오 |
| ref-272 | Lucas Systems | Voice-Directed Warehousing - Solutions | Lucas Systems | 미확인 | https://www.lucasware.com/voice-directed-warehousing/ | 아니오 |
| ref-273 | Mobile Industrial Robots(MiR) (ManualsLib 게재본) | MiR250 User Manual — Creating and configuring a map (page 104, 제조사 공식 사이트가 아닌 매뉴얼 게재 사이트 사본) | 미확인 | https://www.manualslib.com/manual/1941073/Mir-Mir250.html?page=104 | 아니오 |
| ref-274 | ScaliRo | LIF – Layout Interchange Format Explained | 미확인 | https://scaliro.de/en/lif/ | 아니오 |
| ref-275 | USPTO(미국 특허 공보, 양수인 VOCOLLECT, INC.) | System and method for generating and updating location check digits (US 8868519) | 미확인 | https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8868519 | 아니오 |
| ref-276 | Amazon | Amazon unveils next-gen Proteus robot as part of €10 billion European investment in its fulfillment network | 2026-06 | https://www.aboutamazon.com/news/operations/amazon-proteus-robot-europe-investment-employee-support | 아니오 |
| ref-277 | The Robot Report | Proteus gets natural-language ability as Amazon expands European robot deployments | 2026-06 | https://www.therobotreport.com/proteus-gets-natural-language-ability-amazon-expands-europe-robot-deployments/ | 아니오 |
| ref-278 | InOrbit.AI | InOrbit RobOps Copilot - Bring AI power to robot operations | 미확인 | https://www.inorbit.ai/robopscopilot | 아니오 |
| ref-279 | Locus Robotics | Efficient Robot Interface for Seamless Human-Robot Collaboration (LocusONE user interface) | 미확인 | https://locusrobotics.com/locusone/automated-warehouse-software/user-interface | 아니오 |
| ref-280 | Aila Technologies | Locus Robotics leverages Aila's scanning to increase productivity (case study) | 미확인 | https://www.ailatech.com/blog/case-study-locus-robotics/ | 아니오 |
| ref-281 | 뉴스핌 | 현대로템, 무인로봇 국책과제 2건 수주 | 2026-05-26 | https://www.newspim.com/news/view/20260526000361 | 아니오 |
| ref-282 | Open Robotics (ROS 2 Documentation) | Quality of Service settings — ROS 2 Documentation: Jazzy | 미확인 | https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html | 예 |
| ref-283 | Open Robotics | Doors (integration_doors) - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/integration_doors.html | 예 |
| ref-284 | Open Robotics | Lifts (integration_lifts) - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/integration_lifts.html | 예 |
| ref-285 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_door_msgs/msg/DoorState.msg | 미확인 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorState.msg | 예 |
| ref-286 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 미확인 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg | 예 |
| ref-287 | Eclipse Foundation (eclipse-sparkplug GitHub) | Sparkplug Specification — Chapter 5 Operational Behavior (Sparkplug_5_Operational_Behavior.adoc) | 미확인 | https://github.com/eclipse-sparkplug/sparkplug/blob/master/specification/src/main/asciidoc/chapters/Sparkplug_5_Operational_Behavior.adoc | 예 |
| ref-288 | OPC Foundation | OPC Unified Architecture – Part 4: Services - 7.11 DataValue | 미확인 | https://reference.opcfoundation.org/specs/OPC-10000-4/7.11 | 아니오 |
| ref-289 | Yates, R. D., Sun, Y., Brown, D. R., Kaul, S. K., Modiano, E., & Ulukus, S. | Age of Information: An Introduction and Survey | 2021-05 | https://arxiv.org/abs/2007.08564 | 아니오 |
| ref-290 | NIST | DIGITAL TWINS FOR ADVANCED MANUFACTURING: THE STANDARDIZED APPROACH | 미확인 | https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=957417 | 아니오 |
| ref-291 | Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W. | Digital Twin in manufacturing: A categorical literature review and classification | 2018 | https://www.sciencedirect.com/science/article/pii/S2405896318316021 | 아니오 |
| ref-292 | DeHoratius, N., & Raman, A. | Inventory Record Inaccuracy: An Empirical Analysis | 2008 | https://pubsonline.informs.org/doi/10.1287/mnsc.1070.0789 | 아니오 |
| ref-293 | Massawe, L. V. 외(Sensors) | Reducing False Negative Reads in RFID Data Streams Using an Adaptive Sliding-Window Approach | 2012-03-28 | https://doi.org/10.3390/s120404187 | 아니오 |
| ref-294 | 이동건, 송승현, 이찬혁, 노상도, 윤상문, 이현영(한국CDE학회 논문집) | 자동물류시스템의 설계 검증 및 운영을 위한 디지털트윈 개발 및 적용 | 2021-12 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002781294 | 아니오 |
| ref-295 | Preguiça, N., Baquero, C., & Shapiro, M. | Conflict-free Replicated Data Types (CRDTs) | 2018-05 | https://arxiv.org/abs/1805.06358 | 아니오 |
| ref-296 | 김지형 | OPC UA를 활용한 이기종 로봇의 실시간 디지털 트윈 설계 및 구현 | 2023 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002993454 | 아니오 |
| ref-297 | ROS 2 Design | ROS on DDS | 미확인 | https://design.ros2.org/articles/ros_on_dds.html | 예 |
| ref-298 | ROS 2 Design | ROS 2 Quality of Service policies | 미확인 | https://design.ros2.org/articles/qos.html | 예 |
| ref-299 | ROS 2 (ros2/rmw_zenoh GitHub) | rmw_zenoh — README (A ROS 2 RMW implementation based on Zenoh) | 미확인 | https://github.com/ros2/rmw_zenoh | 예 |
| ref-300 | KubeEdge (CNCF, kubeedge GitHub) | KubeEdge — README | 미확인 | https://github.com/kubeedge/kubeedge | 예 |
| ref-301 | Microsoft | Operate Azure IoT Edge devices offline | 2026-03-02 | https://learn.microsoft.com/en-us/azure/iot-edge/offline-capabilities | 예 |
| ref-302 | Open Robotics (open-rmf) | rmf-web — README | 미확인 | https://github.com/open-rmf/rmf-web | 예 |
| ref-303 | NIST | NIST Special Publication (SP) 500-325, Fog Computing Conceptual Model | 2018-03 | https://csrc.nist.gov/pubs/sp/500/325/final | 아니오 |
| ref-304 | Ichnowski, J., Chen, K. 외(UC Berkeley AUTOLAB) | FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2 | 2022-05 | https://arxiv.org/abs/2205.09778 | 아니오 |
| ref-305 | Kehoe, B., Patil, S., Abbeel, P., & Goldberg, K. | A Survey of Research on Cloud Robotics and Automation | 2015 | https://escholarship.org/uc/item/3t04p9m1 | 아니오 |
| ref-306 | OASIS | MQTT Version 5.0 | 2019-03 | https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html | 아니오 |
| ref-307 | CJ대한통운 | CJ대한통운, 물류센터 최초 5G 개통 … 속도 1000배 빨라진다 | 2023-04 | https://www.cjlogistics.com/ko/newsroom/news/NR_00001046 | 아니오 |
| ref-308 | Brorsson, E. 외 | Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives | 2025-12 | https://arxiv.org/abs/2512.15215 | 아니오 |
| ref-309 | FreightWaves | Warehouses face $100K-hour downtime risk as cloud outages mount | 미확인 | https://www.freightwaves.com/news/warehouses-face-100k-hour-downtime-risk-hybrid-wms | 아니오 |
| ref-310 | Gilbert, S., & Lynch, N. | Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services | 2002-06 | https://dl.acm.org/doi/10.1145/564585.564601 | 아니오 |
| ref-311 | ETRI Journal 게재 논문(Jun 외, 한국전자통신연구원 발행) | Ultra-low-latency services in 5G systems: A perspective from 3GPP standards | 2020 | https://onlinelibrary.wiley.com/doi/full/10.4218/etrij.2020-0200 | 아니오 |
| ref-312 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg | 미확인 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg | 예 |
| ref-313 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_door_msgs/msg/DoorMode.msg | 미확인 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorMode.msg | 예 |
| ref-314 | 국가표준인증통합정보시스템(KSSN) | KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법 | 2021-11 | https://www.kssn.net/search/stddetail.do?itemNo=K001010135682 | 아니오 |
| ref-315 | 산업통상자원부 국가기술표준원(대한민국 정책브리핑) | 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 | 2021-11 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156480155 | 아니오 |
| ref-316 | 건설기술신문 | 승강기협, 엘리베이터-로봇 연동 단체표준 제정 | 미확인 | https://www.ctman.kr/35296 | 아니오 |
| ref-317 | 전기신문 | 승강기협회 '로봇-승강기 연동 표준개발'로 승강기 4차산업 견인 | 미확인 | https://www.electimes.com/news/articleView.html?idxno=320147 | 아니오 |
| ref-318 | KONE | KONE Service Robot API | 미확인 | https://dev.kone.com/api-portal/service-robot-api/ | 아니오 |
| ref-319 | 한국경제 | 현대엘리베이터, 엘리베이터-로봇 연계 가능한 '오픈 API' 공개 | 2022-03 | https://www.hankyung.com/economy/article/202203314153Y | 아니오 |
| ref-320 | 파이낸셜뉴스 | 현대엘리베이터 '오픈 API' 참여 다각화..."엘리베이터와 로봇 연동" | 2023-02 | https://www.fnnews.com/news/202302140913318867 | 아니오 |
| ref-321 | Electronics(MDPI) 게재 논문(저자 미확인) | Efficient Graph-Based Multi-Story Path Planning with Optimized Elevator Selection for Indoor Delivery Robots | 2025 | https://doi.org/10.3390/electronics14050982 | 아니오 |
| ref-322 | 국토교통부 | 올해 '로봇 친화형 건축물 설계·시공 및 운영·관리 핵심기술 개발'부터 착수 (보도자료) | 미확인 | https://www.molit.go.kr/USR/NEWS/m_71/dtl.jsp?lcmspage=1&id=95090964 | 아니오 |
| ref-323 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 (tag 2.1.0) — json_schemas/factsheet.schema | 미확인 | https://github.com/VDA5050/VDA5050/blob/2.1.0/json_schemas/factsheet.schema | 예 |
| ref-324 | EASE CRC (ease-crc/soma) | SOMA — owl/SOMA-ACT.owl | 미확인 | https://github.com/ease-crc/soma/blob/master/owl/SOMA-ACT.owl | 예 |
| ref-325 | Helmut Schmidt University, Institute of Automation Technology (hsu-aut GitHub) | IndustrialStandard-ODP-IEEE1872-2 — AuR_IEEE1872-2.ttl | 미확인 | https://github.com/hsu-aut/IndustrialStandard-ODP-IEEE1872-2/blob/main/AuR_IEEE1872-2.ttl | 예 |
| ref-326 | KnowRob (knowrob GitHub) | knowrob — README (dev branch) | 미확인 | https://github.com/knowrob/knowrob | 예 |
| ref-327 | Järvenpää, E., Siltala, N., Hylli, O., Nylund, H., & Lanz, M. | Semantic rules for capability matchmaking in the context of manufacturing system design and reconfiguration | 2023 | https://www.tandfonline.com/doi/full/10.1080/0951192X.2022.2081361 | 아니오 |
| ref-328 | Köcher, A., Vieira da Silva, L. M., & Fay, A. | Automated Process Planning Based on a Semantic Capability Model and SMT | 2023-12 | https://arxiv.org/abs/2312.08801 | 아니오 |
| ref-329 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 (tag 2.0.0) — VDA5050_EN_V1.md | 미확인 | https://github.com/VDA5050/VDA5050/blob/2.0.0/VDA5050_EN_V1.md | 예 |
| ref-330 | srfiorini (IEEE1872-owl GitHub) | IEEE1872-owl — cora-bare.owl (OWL specification of CORA) | 미확인 | https://github.com/srfiorini/IEEE1872-owl/blob/master/cora-bare.owl | 예 |
| ref-331 | OGC (Open Geospatial Consortium) | OGC IndoorGML 2.0 Part 1 – Conceptual Model (22-045r5) | 2025-08 | https://docs.ogc.org/is/22-045r5/22-045r5.html | 아니오 |
| ref-332 | OGC (Open Geospatial Consortium) | OGC Publishes IndoorGML 2.0 Part 1 Conceptual Model Standard | 2025-08-28 | https://www.ogc.org/announcement/ogc-publishes-indoorgml-2-0-part-1-conceptual-model-standard/ | 아니오 |
| ref-333 | OGC IndoorGML SWG (opengeospatial/IndoorGML-SWG GitHub) | OGC IndoorGML 2.0 Part 2b – JSON Encoding (26-043, Candidate SWG Draft v0.5.0) | 2026-02-28 | https://github.com/opengeospatial/IndoorGML-SWG/blob/master/26-043.html | 예 |
| ref-334 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcRelSpaceBoundary (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 미확인 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcRelSpaceBoundary.md | 예 |
| ref-335 | ISO | ISO 16739-1:2024 - Industry Foundation Classes (IFC) for data sharing in the construction and facility management industries — Part 1: Data schema | 2024 | https://www.iso.org/standard/84123.html | 아니오 |
| ref-336 | W3C Linked Building Data Community Group (w3c-lbd-cg GitHub) | Building Topology Ontology (BOT) — bot.ttl (version 0.3.2) | 2020-07-31 | https://github.com/w3c-lbd-cg/bot/blob/master/bot.ttl | 예 |
| ref-337 | Rasmussen, M. H., Lefrançois, M., Schneider, G. F., & Pauwels, P. | BOT: The building topology ontology of the W3C linked building data group | 2020 | https://journals.sagepub.com/doi/10.3233/SW-200385 | 아니오 |
| ref-338 | OGC (Open Geospatial Consortium) / Apple | Indoor Mapping Data Format (1.0.0) — OGC Community Standard 20-094 | 2021-02 | https://docs.ogc.org/cs/20-094/ | 아니오 |
| ref-339 | OGC (Open Geospatial Consortium) | OGC City Geography Markup Language (CityGML) Part 1: Conceptual Model Standard (20-010) | 2021 | https://docs.ogc.org/is/20-010/20-010.html | 아니오 |
| ref-340 | PFG(Journal of Photogrammetry, Remote Sensing and Geoinformation Science) 게재 논문 저자(미확인) | CityGML 3.0: New Functions Open Up New Applications | 2020 | https://link.springer.com/article/10.1007/s41064-020-00095-z | 아니오 |
| ref-341 | Brick Consortium (Brick Schema) | Relationships — Brick Ontology Documentation | 미확인 | https://docs.brickschema.org/brick/relationships.html | 아니오 |
| ref-342 | buildingSMART (buildingsmart-community GitHub) | ifcOWL — README (ifcOWL standard) | 미확인 | https://github.com/buildingsmart-community/ifcOWL | 예 |
| ref-343 | Zhu, J., Wong, M. O., Nisbet, N., Xu, J., Kelly, T., Zlatanova, S., & Brilakis, I. | Semantics-based connectivity graph for indoor pathfinding powered by IFC-Graph | 2025 | https://www.sciencedirect.com/science/article/pii/S0926580525000597 | 아니오 |
| ref-344 | 이기준, 이지영(한국공간정보학회지) | 실내공간 표준안 IndoorGML의 개념 및 활용 | 2013 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001786322 | 아니오 |
| ref-345 | 국토교통부(법제처 국가법령정보센터) | 실내공간정보 구축 작업규정 | 2018-03-05 | https://law.go.kr/admRulLsInfoP.do?admRulSeq=2100000116559 | 아니오 |
| ref-346 | Open Robotics (open-rmf) | rmf_building_map_msgs — rmf_building_map_msgs/msg/Level.msg | 미확인 | https://github.com/open-rmf/rmf_building_map_msgs/blob/main/rmf_building_map_msgs/msg/Level.msg | 예 |
| ref-347 | Hughes, N., Chang, Y., Hu, S., Talak, R., Abdulhai, R., Strader, J., & Carlone, L. | Foundations of Spatial Perception for Robotics: Hierarchical Representations and Real-time Systems | 2023-05 | https://arxiv.org/abs/2305.07154 | 아니오 |
| ref-348 | ISPRS International Journal of Geo-Information(MDPI) 게재 논문 저자(미확인) | Data Model for IndoorGML Extension to Support Indoor Navigation of People with Mobility Disabilities | 2020 | https://www.mdpi.com/2220-9964/9/2/66 | 아니오 |
| ref-349 | Open Robotics (open-rmf) | rmf_building_map_msgs — rmf_building_map_msgs/msg/Graph.msg | 미확인 | https://github.com/open-rmf/rmf_building_map_msgs/blob/main/rmf_building_map_msgs/msg/Graph.msg | 예 |
| ref-350 | Ren, A. Z. 외(Google DeepMind·Princeton University, KnowNo 프로젝트) | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners — project page (robot-help.github.io) | 미확인 | https://robot-help.github.io/ | 예 |
| ref-351 | Ren, A. Z. 외 | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners | 2023-07 | https://arxiv.org/abs/2307.01928 | 아니오 |
| ref-352 | Park, J. 외(고려대학교·연세대학교·Google Research, CLARA 프로젝트) | CLARA: Classifying and Disambiguating User Commands for Reliable Interactive Robotic Agents — project page (clararobot.github.io) | 미확인 | https://clararobot.github.io/ | 예 |
| ref-353 | Park, J., Lim, S., Lee, J., Park, S., Chang, M., Yu, Y., & Choi, S. | CLARA: Classifying and Disambiguating User Commands for Reliable Interactive Robotic Agents | 2024 | https://arxiv.org/abs/2306.10376 | 아니오 |
| ref-354 | cog-model (AmbiK 저자) | AmbiK-dataset — README (AmbiK: Dataset of Ambiguous Tasks in Kitchen Environment) | 미확인 | https://github.com/cog-model/AmbiK-dataset | 예 |
| ref-355 | Ivanova, A. 외(AmbiK 저자, dblp 기록 기준) | AmbiK: Dataset of Ambiguous Tasks in Kitchen Environment | 2025 | https://aclanthology.org/2025.acl-long.1593/ | 아니오 |
| ref-356 | Rasa Technologies (RasaHQ/rasa GitHub) | Forms — Rasa documentation (docs/docs/forms.mdx) | 미확인 | https://github.com/RasaHQ/rasa/blob/main/docs/docs/forms.mdx | 예 |
| ref-357 | Weld, H., Huang, X., Long, S., Poon, J., & Han, S. C. | A Survey of Joint Intent Detection and Slot Filling Models in Natural Language Understanding | 2022-12 | https://dl.acm.org/doi/10.1145/3547138 | 아니오 |
| ref-358 | Chen, H. 외 | Enabling Robots to Understand Incomplete Natural Language Instructions Using Commonsense Reasoning | 2019-04 | https://arxiv.org/abs/1904.12907 | 아니오 |
| ref-359 | Wang, W. 외 | Learning to Ask: When LLM Agents Meet Unclear Instruction | 2024-09 | https://arxiv.org/abs/2409.00557 | 아니오 |
| ref-360 | arXiv 2508.19114 저자(미확인) | DELIVER: A System for LLM-Guided Coordinated Multi-Robot Pickup and Delivery using Voronoi-Based Relay Planning | 2025-08 | https://arxiv.org/abs/2508.19114 | 아니오 |
| ref-361 | Sucker, S., Neubauer, M., & Henrich, D. | Robot Tasks with Fuzzy Time Requirements from Natural Language Instructions | 2024-11 | https://arxiv.org/abs/2411.09436 | 아니오 |
| ref-362 | OpenAI | Introducing Structured Outputs in the API | 2024-08 | https://openai.com/index/introducing-structured-outputs-in-the-api/ | 아니오 |
| ref-363 | ROS 2 Design | Actions (ROS 2 Design) | 미확인 | https://design.ros2.org/articles/actions.html | 예 |
| ref-364 | ROS 2 Design | Managed nodes (ROS 2 Design: node_lifecycle) | 미확인 | https://design.ros2.org/articles/node_lifecycle.html | 예 |
| ref-365 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/dispatch_task_request.json | 미확인 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/dispatch_task_request.json | 예 |
| ref-366 | Open Robotics (open-rmf) | rmf_task — rmf_task/include/rmf_task/Task.hpp | 미확인 | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/Task.hpp | 예 |
| ref-367 | IETF HTTPAPI Working Group (Jena, J., & Dalal, S.) | The Idempotency-Key HTTP Header Field (draft-ietf-httpapi-idempotency-key-header) | 미확인 | https://github.com/ietf-wg-httpapi/idempotency/blob/main/draft-ietf-httpapi-idempotency-key-header.md | 예 |
| ref-368 | OPC Foundation | OPC 10000-10 UA Part 10: Programs - 4.2.4 Program states | 미확인 | https://reference.opcfoundation.org/Core/Part10/v104/docs/4.2.4 | 아니오 |
| ref-369 | ISA | ISA-TR88.00.02-2022, Machine and Unit States: An implementation example of ISA-88.00.01 | 2022 | https://www.isa.org/products/isa-tr88-00-02-2022-machine-and-unit-states-an-imp | 아니오 |
| ref-370 | Colledanchise, M., & Ögren, P. | Behavior Trees in Robotics and AI: An Introduction | 2017-09 | https://arxiv.org/abs/1709.00084 | 아니오 |
| ref-371 | BehaviorTree.CPP (BehaviorTree GitHub) | BehaviorTree.CPP — include/behaviortree_cpp/decorators/retry_node.h | 미확인 | https://github.com/BehaviorTree/BehaviorTree.CPP/blob/master/include/behaviortree_cpp/decorators/retry_node.h | 예 |
| ref-372 | BehaviorTree.CPP (BehaviorTree GitHub) | BehaviorTree.CPP — include/behaviortree_cpp/decorators/timeout_node.h | 미확인 | https://github.com/BehaviorTree/BehaviorTree.CPP/blob/master/include/behaviortree_cpp/decorators/timeout_node.h | 예 |
| ref-373 | Garcia-Molina, H., & Salem, K. | Sagas | 1987 | https://dl.acm.org/doi/10.1145/38713.38742 | 아니오 |
| ref-374 | Open Robotics (open-rmf/rmf_ros2 GitHub) | Task recovery when fleet adapter get restarted · Issue #224 · open-rmf/rmf_ros2 | 미확인 | https://github.com/open-rmf/rmf_ros2/issues/224 | 아니오 |
| ref-375 | Paul, T. C., Lertpongrujikorn, P., Nguyen, H. D., & Amini Salehi, M. | Benchmarking Message Brokers for IoT Edge Computing: A Comprehensive Performance Study | 2026-03-23 | https://arxiv.org/abs/2603.21600 | 아니오 |
| ref-376 | Open Robotics | Tasks in RMF (task) - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/task.html | 예 |
| ref-377 | Open Robotics (open-rmf) | rmf_task — rmf_task/include/rmf_task/TaskPlanner.hpp | 미확인 | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/TaskPlanner.hpp | 예 |
| ref-378 | Open Robotics (open-rmf) | rmf_ros2 — rmf_task_ros2/include/rmf_task_ros2/Dispatcher.hpp | 미확인 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_task_ros2/include/rmf_task_ros2/Dispatcher.hpp | 예 |
| ref-379 | Google (google/or-tools GitHub) | OR-Tools — ortools/sat/docs/scheduling.md (Scheduling recipes for the CP-SAT solver) | 미확인 | https://github.com/google/or-tools/blob/stable/ortools/sat/docs/scheduling.md | 예 |
| ref-380 | de Koster, R., Le-Duc, T., & Roodbergen, K. J. | Design and control of warehouse order picking: A literature review | 2007 | https://pure.eur.nl/en/publications/design-and-control-of-warehouse-order-picking-a-literature-review/ | 아니오 |
| ref-381 | Boysen, N., Briskorn, D., & Emde, S. | Parts-to-picker based order processing in a rack-moving mobile robots environment | 2017 | https://www.sciencedirect.com/science/article/abs/pii/S0377221717302758 | 아니오 |
| ref-382 | Boysen, N., de Koster, R., & Weidinger, F. | Warehousing in the e-commerce era: A survey | 2019 | https://pure.eur.nl/en/publications/warehousing-in-the-e-commerce-era-a-survey/ | 아니오 |
| ref-383 | Nunes, E., Manner, M., Mitiche, H., & Gini, M. | A taxonomy for task allocation problems with temporal and ordering constraints | 2017 | https://www.sciencedirect.com/science/article/abs/pii/S0921889016306157 | 아니오 |
| ref-384 | Yang, X., Hua, G., Zhang, L., Cheng, T. C. E., & Choi, T. M. | Joint order assignment and picking station scheduling in KIVA warehouses with multiple stations | 2021-08 | https://arxiv.org/abs/2108.09056 | 아니오 |
| ref-385 | Boysen, N., Stephan, K., & Weidinger, F. | Manual order consolidation with put walls: the batched order bin sequencing problem | 2019 | https://www.sciencedirect.com/science/article/pii/S2192437620300315 | 아니오 |
| ref-386 | Jiang, M., & Huang, G. Q. | Intralogistics synchronization in robotic forward-reserve warehouses for e-commerce last-mile delivery | 2022 | https://www.sciencedirect.com/science/article/abs/pii/S1366554522000175 | 아니오 |
| ref-387 | 신희철, 이강현, 방선호, 신광섭(한국빅데이터학회 학회지) | 물류센터 생산성 향상을 위한 피킹스케줄링 문제에 관한 연구 | 2024 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003163116 | 아니오 |
| ref-388 | Tran Bo Tao Huong, 이광헌, 홍순도(대한산업공학회지) | 복수 포장대와 피킹-패킹 전환 정책을 운영하는 물류센터에서의 작업자 스케줄링 | 2025 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003194570 | 아니오 |
| ref-389 | Kedia, K., Jenamani, R. K., Hazra, A., & Chakrabarti, P. P. | Optimal Multi-Agent Path Finding for Precedence Constrained Planning Tasks | 2022-02 | https://arxiv.org/abs/2202.10449 | 아니오 |
| ref-390 | Open Robotics (open-rmf) | rmf_task — rmf_task/include/rmf_task/BinaryPriorityScheme.hpp | 미확인 | https://github.com/open-rmf/rmf_task/blob/main/rmf_task/include/rmf_task/BinaryPriorityScheme.hpp | 예 |
| ref-391 | MassRobotics | What Is the MassRobotics AMR Interoperability Standard? | 미확인 | https://www.massrobotics.org/what-is-the-massrobotics-amr-interoperability-standard/ | 아니오 |
| ref-392 | ECLASS e.V. | IRDI - ECLASS Technischer Support | 미확인 | https://eclass.eu/support/technical-specification/structure-and-elements/irdi | 아니오 |
| ref-393 | Gerkey, B. P., & Matarić, M. J. | A Formal Analysis and Taxonomy of Task Allocation in Multi-Robot Systems | 2004-09 | https://journals.sagepub.com/doi/10.1177/0278364904045564 | 아니오 |
| ref-394 | Korsah, G. A., Stentz, A., & Dias, M. B. | A comprehensive taxonomy for multi-robot task allocation | 2013 | https://journals.sagepub.com/doi/10.1177/0278364913496484 | 아니오 |
| ref-395 | Choi, H.-L., Brunet, L., & How, J. P. | Consensus-Based Decentralized Auctions for Robust Task Allocation | 2009 | https://dl.acm.org/doi/10.1109/tro.2009.2022423 | 아니오 |
| ref-396 | Dias, M. B., Zlot, R., Kalra, N., & Stentz, A. | Market-Based Multirobot Coordination: A Survey and Analysis | 2006-07 | https://www.ri.cmu.edu/pub_files/2006/7/01677943-1.pdf | 아니오 |
| ref-397 | Aziz, H., Chan, H., Cseh, Á., Li, B., Ramezani, F., & Wang, C. | Multi-Robot Task Allocation—Complexity and Approximation | 2021-05 | https://arxiv.org/abs/2103.12370 | 아니오 |
| ref-398 | Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L. | Decision rules for robotic mobile fulfillment systems | 2019 | https://www.sciencedirect.com/science/article/pii/S2214716019300946 | 아니오 |
| ref-399 | Wang, Z., & Gombolay, M. | Heterogeneous graph attention networks for scalable multi-robot scheduling with temporospatial constraints | 미확인 | https://link.springer.com/article/10.1007/s10514-021-09997-2 | 아니오 |
| ref-400 | International Journal of Planning and Scheduling 게재 논문(저자 미확인) | Automated guided vehicle dispatching based on combinatorial optimisation to minimise job waiting time on shop floors | 2019 | https://www.inderscience.com/info/inarticle.php?artid=103016 | 아니오 |
| ref-401 | KISTI ScienceON 수록 국가R&D 과제 보고서(수행기관 미확인) | 클라우드에 연결된 개별 로봇 및 로봇그룹의 작업 계획 기술 개발 | 미확인 | https://scienceon.kisti.re.kr/srch/selectPORSrchReport.do?cn=TRKO202400003952 | 아니오 |
| ref-402 | KISTI ScienceON 수록 논문(저자 미확인) | 시뮬레이션과 메타모델을 이용한 자동물류센터 설계 최적화 | 미확인 | https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO200634515151716 | 아니오 |
| ref-403 | Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin) | Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots | 2026-03 | https://arxiv.org/abs/2603.22731 | 아니오 |
| ref-404 | Open Robotics (open-rmf) | rmf_task — README | 미확인 | https://github.com/open-rmf/rmf_task | 예 |
| ref-405 | Open Robotics | Security - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/security.html | 예 |
| ref-406 | Open Robotics | Simulation - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/simulation.html | 예 |
| ref-407 | gpue (GitHub) | vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS) | 미확인 | https://github.com/gpue/vda5050-sim | 예 |
| ref-408 | ekusiadadus (GitHub) | vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces) | 미확인 | https://github.com/ekusiadadus/vda5050-lab | 예 |
| ref-409 | 한국 학술지 게재 논문(지적과 국토정보 53(1), 83-105, 저자 미확인) | 아파트 단지의 로봇 친화형 환경 인증 모델 개발 (지적과 국토정보 53(1), 83-105) | 2023 | https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART002978381 | 아니오 |
| ref-410 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/schemas/task_description__delivery.json | 미확인 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/task_description__delivery.json | 예 |
| ref-411 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/schemas/event_description__payload_transfer.json | 미확인 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/event_description__payload_transfer.json | 예 |
| ref-412 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/schemas/place.json | 미확인 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/place.json | 예 |
| ref-413 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/order.schema | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/order.schema | 예 |
| ref-414 | Open Robotics (open-rmf) | rmf_building_map_msgs — rmf_building_map_msgs/msg/GraphNode.msg | 미확인 | https://github.com/open-rmf/rmf_building_map_msgs/blob/main/rmf_building_map_msgs/msg/GraphNode.msg | 예 |
| ref-415 | Martins, P. H., Custódio, L., & Ventura, R. | A deep learning approach for understanding natural language commands for mobile service robots | 2018-07 | https://arxiv.org/abs/1807.03053 | 아니오 |
| ref-416 | Rana, K. 외 | SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning | 2023-07 | https://arxiv.org/abs/2307.06135 | 아니오 |
| ref-417 | Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab) | Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems | 2026-04 | https://arxiv.org/abs/2604.05427 | 아니오 |
| ref-418 | Mecalux | Mecalux integrates generative AI into Easy WMS | 미확인 | https://www.mecalux.com/news/generative-ai-easy-wms-mecalux | 아니오 |
| ref-419 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcDoor (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 미확인 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/shared/IfcSharedBldgElements/Entities/IfcDoor.md | 예 |
| ref-420 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcStair (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 미확인 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/shared/IfcSharedBldgElements/Entities/IfcStair.md | 예 |
| ref-421 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcTransportElementTypeEnum (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 미확인 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Types/IfcTransportElementTypeEnum.md | 예 |
| ref-422 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcWall (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 미확인 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/shared/IfcSharedBldgElements/Entities/IfcWall.md | 예 |
| ref-423 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcBuildingStorey (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 미확인 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcBuildingStorey.md | 예 |
| ref-424 | Moitzi, M. (mozman/ezdxf GitHub) | ezdxf documentation — Concepts: Blocks (docs/source/concepts/blocks.rst) | 미확인 | https://github.com/mozman/ezdxf/blob/master/docs/source/concepts/blocks.rst | 예 |
| ref-425 | Moitzi, M. (mozman/ezdxf GitHub) | ezdxf documentation — Concepts: Layers (docs/source/concepts/layers.rst) | 미확인 | https://github.com/mozman/ezdxf/blob/master/docs/source/concepts/layers.rst | 예 |
| ref-426 | Moitzi, M. (mozman/ezdxf GitHub) | ezdxf documentation — Concepts: DXF Units (docs/source/concepts/units.rst) | 미확인 | https://github.com/mozman/ezdxf/blob/master/docs/source/concepts/units.rst | 예 |
| ref-427 | ISO | ISO 13567-1:2017 - Technical product documentation — Organization and naming of layers for CAD — Part 1: Overview and principles | 2017 | https://www.iso.org/standard/70181.html | 아니오 |
| ref-428 | National Institute of Building Sciences (United States National CAD Standard) | AIA CAD Layer Guidelines, Layer Name Format (NCS V5) | 미확인 | https://www.nationalcadstandard.org/ncs5/pdfs/ncs5_clg_lnf.pdf | 아니오 |
| ref-429 | 국가표준인증통합정보시스템(KSSN) | KS F 1542(2020 확인) CAD 도면 작성을 위한 레이어 원칙과 기준 | 2020-12 | https://www.kssn.net/search/stddetail.do?itemNo=K001010129900 | 아니오 |
| ref-430 | 국토교통부 건설사업정보시스템(CALS) | 건설CALS 전자도면 작성표준 | 미확인 | https://www.calspia.go.kr/portal/intro/introStandard02.do | 아니오 |
| ref-431 | 신동철(대한건축학회 논문집 계획계) | 건축 표준 캐드 레이어의 실무적용 실태 분석 연구 | 2009-11 | https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE01288876 | 아니오 |
| ref-432 | Noardo, F., Arroyo Ohori, K., Krijnen, T., & Stoter, J. (Applied Sciences 11(5), 2232) | An Inspection of IFC Models from Practice | 2021 | https://www.mdpi.com/2076-3417/11/5/2232 | 아니오 |
| ref-433 | arXiv 2607.12678 저자(미확인) | Text-Aided Multi-Modal Panoptic Symbol Spotting for CAD Floor Plan Drawings | 2026-07-14 | https://arxiv.org/abs/2607.12678 | 아니오 |
| ref-434 | ArchiAI Lab (ArchCAD-400K 프로젝트) | ArchCAD-400k: A Large-Scale CAD drawings Dataset and New Baseline for Panoptic Symbol Spotting — project page | 미확인 | https://archiai-lab.github.io/ArchCAD.github.io/ | 예 |
| ref-435 | Buildings(MDPI) 게재 논문 저자(미확인) | Raster Image-Based House-Type Recognition and Three-Dimensional Reconstruction Technology | 2025 | https://doi.org/10.3390/buildings15071178 | 아니오 |
| ref-436 | 국토교통부 | 건설산업 BIM 시행지침 정책정보 상세보기 | 2022-07 | https://www.molit.go.kr/USR/policyData/m_34681/dtl.jsp?srch_usr_titl=Y&psize=10&lcmspage=1&id=4634 | 아니오 |
| ref-437 | IEC | IEC 61360-7:2024 — Standard data element types with associated classification scheme — Part 7: Data dictionary of cross-domain concepts | 2024 | https://webstore.iec.ch/en/publication/72956 | 아니오 |
| ref-438 | IDTA(Industrial Digital Twin Association) | IDTA 02003-1-2 Generic Frame for Technical Data for Industrial Equipment in Manufacturing | 미확인 | https://industrialdigitaltwin.org/wp-content/uploads/2022/10/IDTA-02003-1-2_Submodel_TechnicalData.pdf | 아니오 |
| ref-439 | IDTA (admin-shell-io/submodel-templates) | admin-shell-io/submodel-templates — README (published Submodel Templates list) | 미확인 | https://github.com/admin-shell-io/submodel-templates | 아니오 |
| ref-440 | ROS Navigation (ros-navigation/navigation2 GitHub) | nav2_map_server — README | 미확인 | https://github.com/ros-navigation/navigation2/blob/main/nav2_map_server/README.md | 예 |
| ref-441 | Open Robotics (open-rmf) | rmf_traffic_editor — README | 미확인 | https://github.com/open-rmf/rmf_traffic_editor | 예 |
| ref-442 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/zoneSet.schema | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/zoneSet.schema | 예 |
| ref-443 | IDTA (admin-shell-io/submodel-templates) | Generic Frame for Technical Data for Industrial Equipment in Manufacturing 2.0.1 — README (published/Technical_Data/2/0/1) | 미확인 | https://github.com/admin-shell-io/submodel-templates/blob/main/published/Technical_Data/2/0/1/README.md | 예 |
| ref-444 | ZVEI / Plattform Industrie 4.0 | Submodel Templates of the Asset Administration Shell — Generic Frame for Technical Data for Industrial Equipment in Manufacturing (Version 1.1) | 2020-11 | https://www.zvei.org/fileadmin/user_upload/Presse_und_Medien/Publikationen/2020/Dezember/Submodel_Templates_of_the_Asset_Administration_Shell/201117_I40_ZVEI_SG2_Submodel_Spec_ZVEI_Technical_Data_Version_1_1.pdf | 아니오 |
| ref-445 | ROS (ros/diagnostics GitHub) | diagnostics — README (ros2 branch) | 미확인 | https://github.com/ros/diagnostics/blob/ros2/README.md | 예 |
| ref-446 | ROS 2 (ros2/ros2_tracing GitHub) | ros2_tracing — README | 미확인 | https://github.com/ros2/ros2_tracing | 예 |
| ref-447 | OpenTelemetry (CNCF) | OpenTelemetry Specification — Overview | 미확인 | https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/overview.md | 예 |
| ref-448 | Open Robotics (open-rmf/rmf_internal_msgs) | rmf_task_msgs/msg/Alert.msg | 미확인 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/Alert.msg | 예 |
| ref-449 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/connection.schema | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/connection.schema | 예 |
| ref-450 | Khalastchi, E., & Kalech, M. | Fault Detection and Diagnosis in Multi-Robot Systems: A Survey | 2019 | https://doi.org/10.3390/s19184019 | 아니오 |
| ref-451 | Roser, C., Nakano, M., & Tanaka, M. | Comparison of bottleneck detection methods for AGV systems | 2003 | https://keio.elsevierpure.com/en/publications/comparison-of-bottleneck-detection-methods-for-agv-systems/ | 아니오 |
| ref-452 | Soldani, J., & Brogi, A. | Anomaly Detection and Failure Root Cause Analysis in (Micro) Service-Based Cloud Applications: A Survey | 2022 | https://dl.acm.org/doi/full/10.1145/3501297 | 아니오 |
| ref-453 | Liu, Z., Bahety, A., & Song, S. | REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction | 2023 | https://arxiv.org/abs/2306.15724 | 아니오 |
| ref-454 | International Journal of Production Research(Taylor & Francis), 저자 미확인 | Process mining in supply chain management: state-of-the-art, use cases and research outlook | 2024 | https://www.tandfonline.com/doi/full/10.1080/00207543.2024.2412285 | 아니오 |
| ref-455 | DBpia 게재 논문(저자 미확인) | 다중 자율이동로봇 (AMR) 운영을 위한 웹 기반 사용자 중심 관제 인터페이스 설계 연구 | 2026-07 | https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE12892366 | 아니오 |
| ref-456 | Oraskari, J. (jyrkioraskari GitHub) | IFCtoLBD — README (IFCtoLBD converts IFC (Industry Foundation Classes STEP formatted files into the Linked Building Data ontologies) | 미확인 | https://github.com/jyrkioraskari/IFCtoLBD | 예 |
| ref-457 | Ratul, A. K., Acharjee, S., Park, S., & Sakib, M. N. | Sketch2BIM: A Multi-Agent Human-AI Collaborative Pipeline to Convert Hand-Drawn Floor Plans to 3D BIM | 2025-10 | https://arxiv.org/abs/2510.20838 | 아니오 |
| ref-458 | Jakubik, J., Hemmer, P., Vössing, M., Blumenstiel, B., Bartos, A., & Mohr, K. | Designing a Human-in-the-Loop System for Object Detection in Floor Plans | 2022 | https://ojs.aaai.org/index.php/AAAI/article/view/21522 | 아니오 |
| ref-459 | W3C RDF Data Shapes Working Group | Shapes Constraint Language (SHACL) (W3C data-shapes 저장소 편집자 초안으로 확인, 권고안(2017) 본문과 문구가 다를 수 있음) | 2017 | https://www.w3.org/TR/shacl/ | 예 |
| ref-460 | 대한건축학회논문집 40(1), 297-303(DOI 10.5659/JAIK.2024.40.1.297) 게재 논문 저자(미확인) | 딥러닝과 경로계획 기반의 주택 평면도 3D 모델링 방법 | 2024 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003047128 | 아니오 |
| ref-461 | Buildings(MDPI) 게재 논문 저자(Concordia University, 목록 미확인) | Ontology for BIM-Based Robotic Navigation and Inspection Tasks | 2024 | https://www.mdpi.com/2075-5309/14/8/2274 | 아니오 |
| ref-462 | arXiv 2507.11770 저자(미확인) | Generating Actionable Robot Knowledge Bases by Combining 3D Scene Graphs with Robot Ontologies | 2025-07 | https://arxiv.org/abs/2507.11770 | 아니오 |
| ref-463 | arXiv 2602.06507 저자(미확인) | FloorplanVLM: A Vision-Language Model for Floorplan Vectorization | 2026-02 | https://arxiv.org/abs/2602.06507 | 아니오 |
| ref-464 | buildingSMART (buildingSMART/IDS GitHub) | IDS — README (Information Delivery Specification) | 미확인 | https://github.com/buildingSMART/IDS | 예 |
| ref-465 | Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A. | Toward a Method to Generate Capability Ontologies from Natural Language Descriptions | 2024-06 | https://arxiv.org/abs/2406.07962 | 아니오 |
| ref-466 | 부산일보 | KTL·통합물류협회 ‘물류로봇 시험인증’ 협력 강화 ‘맞손’ | 2026-07-24 | https://www.busan.com/view/busan/view.php?code=2026072420194685883 | 아니오 |
| ref-467 | Žulj, I., Salewski, H., Goeke, D., & Schneider, M. | Order batching and batch sequencing in an AMR-assisted picker-to-parts system | 2022 | https://www.sciencedirect.com/science/article/abs/pii/S0377221721004616 | 아니오 |
| ref-468 | Löffler, M., Boysen, N., & Schneider, M. | Human-Robot Cooperation: Coordinating Autonomous Mobile Robots and Human Order Pickers | 2023 | https://pubsonline.informs.org/doi/10.1287/trsc.2023.1207 | 아니오 |
| ref-469 | Yang, P., Song, S., Huang, L., Gong, Y., & Shen, Z.-J. M. | Deploying pickers and robots in cobot-based collaborative order picking systems | 2026-03 | https://www.tandfonline.com/doi/full/10.1080/24725854.2025.2501036 | 아니오 |
| ref-470 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 2023-06 | https://www.iso.org/standard/83545.html | 아니오 |
| ref-471 | A3(Association for Advancing Automation) | Updated ISO 10218 | Answers to Frequently Asked Questions (FAQs) | 미확인 | https://www.automate.org/robotics/blogs/updated-iso-10218-faq | 아니오 |
| ref-472 | A3(Association for Advancing Automation) | ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available | 2023-10 | https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available | 아니오 |
| ref-473 | 고용노동부 | 고정식 이동식 산업용 로봇의 협동작업 안전 가이드 배포 | 2023-07 | https://www.moel.go.kr/policy/policydata/view.do?bbs_seq=20230700065 | 아니오 |
| ref-474 | 로봇신문 | '이동식 산업용 로봇' 안전 가이드 어떤 내용 담고 있나? | 미확인 | https://www.irobotnews.com/news/articleView.html?idxno=32130 | 아니오 |
| ref-475 | 중소벤처기업부(대한민국 정책브리핑) | ｢대구 이동식 협동로봇 규제자유특구｣ 산업표준 제정으로, 이동식 협동로봇 상용화 길 열렸다! | 2024-11 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156658517 | 아니오 |
| ref-476 | Das, D., Banerjee, S., & Chernova, S. | Explainable AI for Robot Failures: Generating Explanations that Improve User Assistance in Fault Recovery | 2021-01 | https://arxiv.org/abs/2101.01625 | 아니오 |
| ref-477 | Chen, J. Y. C. 외(Theoretical Issues in Ergonomics Science) | Situation awareness-based agent transparency and human-autonomy teaming effectiveness | 미확인 | https://www.tandfonline.com/doi/full/10.1080/1463922X.2017.1315750 | 아니오 |
| ref-478 | Olsen, D. R. 외(CHI 2004) | Fan-out: measuring human control of multiple robots | 2004 | https://dl.acm.org/doi/10.1145/985692.985722 | 아니오 |
| ref-479 | Rey-Becerra, E., & Wischniewski, S. | Mastering a robot workforce: review of single human multiple robots systems and their impact on occupational safety and health and system performance | 2025-07-11 | https://www.tandfonline.com/doi/full/10.1080/00140139.2025.2529316 | 아니오 |
| ref-480 | ZDNet Korea | "대형 물류센터 집품 작업, 로봇 6대로 효율화" | 2023-12-22 | https://zdnet.co.kr/view/?no=20231222165139 | 아니오 |
| ref-481 | Siemens Digital Industries Software | Virtual commissioning with Siemens solutions reduces launch time by three weeks | 미확인 | https://resources.sw.siemens.com/en-US/case-study-idc/ | 아니오 |
| ref-482 | Open Robotics (open-rmf/rmf_site) | rmf_site — README (RMF Site Editor) | 미확인 | https://github.com/open-rmf/rmf_site | 예 |
| ref-483 | Feng, Y., Paul, A., Chen, Z., & Li, J. | A Real-Time Rescheduling Algorithm for Multi-robot Plan Execution | 2024 | https://arxiv.org/abs/2403.18145 | 아니오 |
| ref-484 | Kalempa, V. C., Piardi, L., Limeira, M., & de Oliveira, A. S. | Multi-Robot Preemptive Task Scheduling with Fault Recovery: A Novel Approach to Automatic Logistics of Smart Factories | 2021-09-30 | https://www.mdpi.com/1424-8220/21/19/6536 | 아니오 |
| ref-485 | Emanuelsson, W., Penacho Riveiros, A., Li, Y., Johansson, K. H., & Mårtensson, J. (KTH) | Multiagent Rollout with Reshuffling for Warehouse Robots Path Planning | 2023 | https://arxiv.org/abs/2211.08201 | 아니오 |
| ref-486 | ISO | ISO 22301:2019 - Security and resilience — Business continuity management systems — Requirements | 2019 | https://www.iso.org/standard/75106.html | 아니오 |
| ref-487 | 행정안전부 | 재해경감 우수기업 인증제도 | 미확인 | https://www.mois.go.kr/frt/sub/a06/b10/disasterMitigationCompanies/screen.do | 아니오 |
| ref-488 | 고용노동부 | 중소규모 사업장 기능연속성계획(BCP) 수립 가이드 안내 | 2022-03 | https://www.moel.go.kr/news/notice/noticeView.do?bbs_seq=20220301591 | 아니오 |
| ref-489 | Microsoft (MicrosoftDocs/architecture-center) | Compensating Transaction pattern | 2026-04-16 | https://learn.microsoft.com/en-us/azure/architecture/patterns/compensating-transaction | 예 |
| ref-490 | Element Logic | FAQ - Element Logic (AutoStore) | 미확인 | https://www.elementlogic.net/solutions-and-services/autostore/faq/ | 아니오 |
| ref-491 | Swisslog | The benefits of using AutoStore for high-throughput retail fulfillment | 2025-07 | https://www.swisslog.com/en-us/blog/2025/07/benefits-of-autostore-htp | 아니오 |
| ref-492 | GS1 | EPC Information Services (EPCIS) Standard 1.2 | 2016-09-29 | https://www.gs1.org/sites/default/files/docs/epc/EPCIS-Standard-1.2-r-2016-09-29.pdf | 아니오 |
| ref-493 | Lott, J., & Honary, V.(University of San Diego) | Decentralized Multi-Robot Task Allocation Under Degraded Communication: A Benchmark of Performance, Reliability, and Computation | 2026-09 | https://arxiv.org/abs/2609.13711 | 아니오 |
| ref-494 | Francos, R. M., Garces, D., Akgün, O. E., Bastian, N. D., & Gil, S.(Harvard·JHU) | Trust-Aware Sequential Decision Making and Rollout Planning for Resilient Multi-Robot Systems | 2026-08 | https://arxiv.org/abs/2608.25690 | 아니오 |
| ref-495 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/schemas/task_description__compose.json | 미확인 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/task_description__compose.json | 예 |
| ref-496 | CNCF Serverless Workflow (serverlessworkflow/specification GitHub) | Serverless Workflow Specification — dsl.md | 미확인 | https://github.com/serverlessworkflow/specification/blob/main/dsl.md | 예 |
| ref-497 | Singh, A., Raut, G., & Choudhary, A. | Multi-agent Collaborative Perception for Robotic Fleet: A Systematic Review | 2024-03 | https://arxiv.org/abs/2405.15777 | 아니오 |
| ref-498 | 다음뉴스 게재 기사(원 언론사 미확인) | 유진로봇, 지능형 제조 물류시스템 공개 | 2025-11-04 | https://v.daum.net/v/20251104092138920 | 아니오 |
| ref-499 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_dispenser_msgs/msg/DispenserResult.msg | 미확인 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_dispenser_msgs/msg/DispenserResult.msg | 예 |
| ref-500 | BehaviorTree.CPP (BehaviorTree GitHub) | BehaviorTree.CPP — README | 미확인 | https://github.com/BehaviorTree/BehaviorTree.CPP | 예 |
| ref-501 | Höller, D., Behnke, G., Bercher, P., Biundo, S., Fiorino, H., Pellier, D., & Alford, R. | HDDL – A Language to Describe Hierarchical Planning Problems | 2019-11 | https://arxiv.org/abs/1911.05499 | 아니오 |
| ref-502 | OMG(Object Management Group) | Business Process Model and Notation (BPMN), Version 2.0.2 | 2014-01 | https://www.omg.org/spec/BPMN/2.0.2/ | 아니오 |
| ref-503 | Pettinari, S. (FaMe 공식 저장소, UNICAM PROS) | FaMe — a BPMN-driven framework for Multi-Robot System development (GitHub README) | 미확인 | https://github.com/SaraPettinari/fame | 예 |
| ref-504 | IEEE Standards Association | IEEE 1872.1-2024 — IEEE Standard for Robot Task Representation | 2024-06-18 | https://standards.ieee.org/ieee/1872.1/6993/ | 아니오 |
| ref-505 | Boston Dynamics (boston-dynamics/spot-sdk GitHub) | spot-sdk — README | 미확인 | https://github.com/boston-dynamics/spot-sdk | 예 |
| ref-506 | Kinova (Kinovarobotics/kortex GitHub) | kortex — readme | 미확인 | https://github.com/Kinovarobotics/kortex | 예 |
| ref-507 | Doosan Robotics (doosan-robotics/doosan-robot2 GitHub) | doosan-robot2 — README (humble) | 미확인 | https://github.com/doosan-robotics/doosan-robot2 | 예 |
| ref-508 | Rainbow Robotics (RainbowRobotics/rbpodo GitHub) | rbpodo — README | 미확인 | https://github.com/RainbowRobotics/rbpodo | 예 |
| ref-509 | ISO | ISO 20607:2019 - Safety of machinery — Instruction handbook — General drafting principles | 2019 | https://www.iso.org/standard/68519.html | 아니오 |
| ref-510 | IEC / IEEE / ISO | IEC/IEEE 82079-1:2019 - Preparation of information for use (instructions for use) of products — Part 1: Principles and general requirements | 2019 | https://www.iso.org/standard/71620.html | 아니오 |
| ref-511 | 두산로보틱스 | 매뉴얼 : Doosan Robotics Training & Service | 미확인 | https://robotlab.doosanrobotics.com/ko/board/Resources/Manual | 아니오 |
| ref-512 | Rainbow Robotics | Rainbow Robotics 협동로봇 기술자료 (rb_cobot_docs) | 미확인 | https://rainbowrobotics.github.io/rb_cobot_docs/ko/ | 아니오 |
| ref-513 | OpenDataLab (opendatalab/OmniDocBench GitHub) | OmniDocBench — README | 미확인 | https://github.com/opendatalab/OmniDocBench | 예 |
| ref-514 | Springer Nature (게재 장 저자 미확인) | Conversational Knowledge Extraction from Technical Manuals: An LLM-Based Framework with Ontological Guidance | 미확인 | https://link.springer.com/chapter/10.1007/978-3-032-19096-3_30 | 아니오 |
| ref-515 | Springer Nature (게재 장 저자 미확인) | Enhancing LLMs for Manufacturing Information Extraction | 미확인 | https://link.springer.com/chapter/10.1007/978-981-92-1468-6_21 | 아니오 |
| ref-516 | 한국표준협회 KSSN(국가표준인증종합정보센터) | KS X ISO 23247-1 자동화 시스템 및 통합 — 제조를 위한 디지털 트윈 프레임워크 — 제1부: 개요 및 일반 원리 | 미확인 | https://www.kssn.net/search/stddetail.do?itemNo=K001010140724 | 아니오 |
| ref-517 | NIST | Digital Twins for Advanced Manufacturing | 미확인 | https://www.nist.gov/programs-projects/digital-twins-advanced-manufacturing | 아니오 |
| ref-518 | ISO | ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition | 2026 | https://www.iso.org/standard/87426.html | 아니오 |
| ref-519 | 머니투데이 | 설계부터 생산까지 데이터 연결…제조 디지털 트윈 국제표준 발간 | 2026-07-28 | https://www.mt.co.kr/economy/2026/07/28/2026072809211448284 | 아니오 |
| ref-520 | Agalianos, K., Ponis, S. T., Aretoulaki, E., & Plakas, G. | Discrete Event Simulation and Digital Twins: Review and Challenges for Logistics | 2020 | https://www.sciencedirect.com/science/article/pii/S2351978920320990 | 아니오 |
| ref-521 | Le, T. V., & Fan, R. | Digital twins for logistics and supply chain systems: Literature review, conceptual framework, research potential, and practical challenges | 2024 | https://www.sciencedirect.com/science/article/abs/pii/S0360835223007921 | 아니오 |
| ref-522 | Coelho, F., Relvas, S., & Barbosa-Póvoa, A. P. | Simulation-based decision support tool for in-house logistics: the basis for a digital twin | 2021 | https://www.sciencedirect.com/science/article/abs/pii/S0360835220307646 | 아니오 |
| ref-523 | Open Robotics (open-rmf) | rmf_simulation — README | 미확인 | https://github.com/open-rmf/rmf_simulation | 예 |
| ref-524 | OpenFactoryTwin (Fraunhofer ISST, HSBI, FH Dortmund) | ofact — Simulation-based Digital Twin for Production and Logistics Material Flows (README) | 미확인 | https://github.com/OpenFactoryTwin/ofact | 예 |
| ref-525 | Sargent, R. G. | Verification and validation of simulation models (Proceedings of the 40th Conference on Winter Simulation) | 2008 | https://dl.acm.org/doi/abs/10.5555/1516744.1516780 | 아니오 |
| ref-526 | CJ대한통운 | 가상세계 쌍둥이 창고로 물류 예측... CJ대한통운, 디지털 트윈 구축 (보도자료) | 2021-11 | https://www.cjlogistics.com/ko/newsroom/news/NR_00000905 | 아니오 |
| ref-527 | NVIDIA | NVIDIA Unveils 'Mega' Omniverse Blueprint for Building Industrial Robot Fleet Digital Twins | 미확인 | https://blogs.nvidia.com/blog/mega-omniverse-blueprint | 아니오 |
| ref-528 | NIST (usnistgov/ARIAC_docs) | ARIAC 2025 Documentation — Challenges | 미확인 | https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html | 예 |
| ref-529 | NIST (usnistgov/ARIAC_docs) | ARIAC 2025 Documentation — Scoring | 미확인 | https://pages.nist.gov/ARIAC_docs/en/latest/pages/scoring.html | 예 |
| ref-530 | Computers & Industrial Engineering 게재 논문(저자 미확인) | Optimal recharge sequencing in multi-AGV systems: A mixed ILP approach | 2024-08 | https://www.sciencedirect.com/science/article/pii/S0360835224006314 | 아니오 |
| ref-531 | arXiv 2607.05683 저자(미확인) | Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers | 2026-07 | https://arxiv.org/abs/2607.05683 | 아니오 |
| ref-532 | Ma, N., Zhou, C., & Stephen, A. | Simulation model and performance evaluation of battery-powered AGV systems in automated container terminals | 2020 | https://www.sciencedirect.com/science/article/abs/pii/S1569190X2030085X | 아니오 |
| ref-533 | Chen, W., Gong, Y., Chen, Q., & Wang, H. | Does battery management matter? Performance evaluation and operating policies in a self-climbing robotic warehouse | 2024-01 | https://www.sciencedirect.com/science/article/abs/pii/S0377221723004770 | 아니오 |
| ref-534 | Dang, Q.-V., Singh, N., Adan, I., Martagan, T., & van de Sande, D. | Scheduling heterogeneous multi-load AGVs with battery constraints | 2021-12 | https://www.sciencedirect.com/science/article/pii/S0305054821002586 | 아니오 |
| ref-535 | 박재범, 조성준, 김준식, 유범재(전자공학회논문지 61(8)) | 배송 로봇의 다층, 다중 배송을 위한 효율적인 경로 계획 및 엘리베이터 층간 이동 시스템 | 2024 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003107904 | 아니오 |
| ref-536 | Open Robotics (open-rmf) | rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp | 미확인 | https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Graph.hpp | 예 |
| ref-537 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp | 미확인 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp | 예 |
| ref-538 | Open Robotics (open-rmf) | rmf_reservation — Experimental reservation library in rust (GitHub) | 미확인 | https://github.com/open-rmf/rmf_reservation | 아니오 |
| ref-539 | askforalfred (ALFRED 공식 저장소) | ALFRED — A Benchmark for Interpreting Grounded Instructions for Everyday Tasks (GitHub README) | 미확인 | https://github.com/askforalfred/alfred | 예 |
| ref-540 | Shridhar, M. 외 | ALFRED: A Benchmark for Interpreting Grounded Instructions for Everyday Tasks | 2020 | https://openaccess.thecvf.com/content_CVPR_2020/html/Shridhar_ALFRED_A_Benchmark_for_Interpreting_Grounded_Instructions_for_Everyday_Tasks_CVPR_2020_paper.html | 아니오 |
| ref-541 | lbaa2022 (LoTa-Bench 공식 저장소) | LLMTaskPlanning — LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents (ICLR 2024) (GitHub README) | 미확인 | https://github.com/lbaa2022/LLMTaskPlanning | 예 |
| ref-542 | LoTa-Bench 저자(arXiv 2402.08178) | LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents | 2024-02 | https://arxiv.org/abs/2402.08178 | 아니오 |
| ref-543 | Amazon Alexa (alexa/teach GitHub) | TEACh: Task-driven Embodied Agents that Chat (GitHub README) | 미확인 | https://github.com/alexa/teach | 예 |
| ref-544 | Zhang, X. 외(LaMMA-P 저자) | LaMMA-P: Generalizable Multi-Agent Long-Horizon Task Allocation and Planning with LM-Driven PDDL Planner | 2024-09 | https://arxiv.org/abs/2409.20560 | 아니오 |
| ref-545 | Snips (sonos/nlu-benchmark GitHub) | nlu-benchmark — 2017-06-custom-intent-engines (README) | 2017-06 | https://github.com/sonos/nlu-benchmark/tree/master/2017-06-custom-intent-engines | 예 |
| ref-546 | 한국지능정보사회진흥원(AI Hub) | 일상생활 작업 및 명령 수행 데이터(임무수행 명령어) | 미확인 | https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=71547 | 아니오 |
| ref-547 | OpenBench 저자(arXiv 2502.09238) | OpenBench: A New Benchmark and Baseline for Semantic Navigation in Smart Logistics | 2025-02 | https://arxiv.org/abs/2502.09238 | 아니오 |
| ref-548 | Högskolan Väst (DiVA 학위논문, 저자 미확인) | An LLM- Interface for Robot Mission Specification in Logistics | 미확인 | https://hv.diva-portal.org/smash/get/diva2:2080486/FULLTEXT01.pdf | 아니오 |
| ref-549 | Open Robotics (ROS REP) | REP 2000 -- ROS 2 Releases and Target Platforms | 미확인 | https://www.ros.org/reps/rep-2000.html | 예 |
| ref-550 | IDTA (admin-shell-io/id GitHub) | IDTA SoftwareNameplate 1/0 — README (Nameplate for Software in Manufacturing) | 미확인 | https://github.com/admin-shell-io/id/blob/master/idta/SoftwareNameplate/1/0/README.md | 예 |
| ref-551 | ISO | ISO 17359:2018 - Condition monitoring and diagnostics of machines — General guidelines | 2018 | https://www.iso.org/standard/71194.html | 아니오 |
| ref-552 | ISO | ISO 55000:2024 - Asset management — Vocabulary, overview and principles | 2024-07 | https://www.iso.org/standard/83053.html | 아니오 |
| ref-553 | Lei, Y., Liu, H., Li, N. 외 | Condition monitoring and fault diagnosis of industrial robots: A review (Science China Technological Sciences 68, 1110301) | 2025 | https://link.springer.com/article/10.1007/s11431-024-2810-2 | 아니오 |
| ref-554 | IEC | IEC TR 62443-2-3:2015 Security for industrial automation and control systems - Part 2-3: Patch management in the IACS environment | 2015-06 | https://webstore.iec.ch/en/publication/22811 | 아니오 |
| ref-555 | European Union (EUR-Lex) | Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery | 2023-06 | https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng | 아니오 |
| ref-556 | Amazon Web Services (aws-samples GitHub) | ros2-ota-firmware-updates — README | 미확인 | https://github.com/aws-samples/ros2-ota-firmware-updates | 예 |
| ref-557 | 네이트 뉴스(원 매체 미확인) | 클라우드 기반 OTA로 로봇이 진화하다…2026 SDR 과제 킥오프 워크숍 현장 | 2026-07-23 | https://m.news.nate.com/view/20260723n24828 | 아니오 |
| ref-558 | 한국로봇사용자협회 | 협동로봇 설치 작업장 안전인증 안내 | 미확인 | https://www.korua.or.kr/inspect/inspectInfo.do | 아니오 |
| ref-559 | 세이프틱스(Safetics) | 로봇 시스템 위험성평가 가이드 | 미확인 | https://doc.safetics.io/insight-risk-assessment/ | 아니오 |
| ref-560 | ISO | ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells | 2025-02 | https://www.iso.org/standard/73934.html | 아니오 |
| ref-561 | 대한민국 정책브리핑(중소벤처기업부) | 이동식 협동로봇 ‘안전기준 산업표준’ 제정…상용화 길 열어 | 2024-11-03 | https://www.korea.kr/news/policyNewsView.do?newsId=148935814 | 아니오 |
| ref-562 | 국가법령정보센터(고용노동부) | 산업안전보건기준에 관한 규칙 제223조(운전 중 위험 방지) | 2023-07-01 | https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EC%82%B0%EC%97%85%EC%95%88%EC%A0%84%EB%B3%B4%EA%B1%B4%EA%B8%B0%EC%A4%80%EC%97%90%EA%B4%80%ED%95%9C%EA%B7%9C%EC%B9%99/(20230701,00367,20221018)/%EC%A0%9C223%EC%A1%B0 | 아니오 |
| ref-563 | Belzile, B. 외 | From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment | 2025-02 | https://arxiv.org/abs/2502.20693 | 아니오 |
| ref-564 | Bensaci, C., Zennir, Y., Pomorski, D. (IEEE Xplore) | A Comparative Study of STPA Hierarchical Structures in Risk Analysis: The Case of a Complex Multi-Robot Mobile System (EECS 2018 학회) | 2018-12 | https://ieeexplore.ieee.org/document/8910126/ | 아니오 |
| ref-565 | Reliability Engineering & System Safety (저자 미확인) | Collision hazard modeling and analysis in a multi-mobile robots system transportation task with STPA and SPN | 2023 | https://www.sciencedirect.com/science/article/abs/pii/S0951832023000534 | 아니오 |
| ref-566 | CEN (iTeh Standards 카탈로그) | EN ISO 12100:2010 - Safety of machinery - General principles for design - Risk assessment and risk reduction | 2010 | https://standards.iteh.ai/catalog/standards/cen/74a41162-9d84-4410-a8a3-606630770ab9/en-iso-12100-2010 | 아니오 |
| ref-567 | Open-RMF (open-rmf/rmf GitHub) | [Feature request]: Fire alarm separation for different fleets · Issue #658 · open-rmf/rmf | 2025-04-04 | https://github.com/open-rmf/rmf/issues/658 | 아니오 |
| ref-568 | 한국표준정보망(KSSN, 국가기술표준원) | KS B ISO/TS 15066 로봇 및 로봇 장치 - 협동로봇 (2022-10-12 확인판 있음) | 2017-02-28 | https://www.kssn.net/search/stddetail.do?itemNo=K001010113282 | 아니오 |
| ref-569 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_fleet_msgs/msg/LaneRequest.msg | 미확인 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg | 예 |
| ref-570 | ROS Navigation (ros-navigation/navigation2 GitHub) | nav2_route — README (Nav2 Route Server) | 미확인 | https://github.com/ros-navigation/navigation2/blob/main/nav2_route/README.md | 예 |
| ref-571 | de Vos, K., van den Brandt, G., Senden, J., Pauwels, P., van de Molengraft, R., & Torta, E. | Generation of skill-specific maps from graph world models for robotic systems | 2024-02 | https://arxiv.org/abs/2402.18174 | 아니오 |
| ref-572 | Omer 외(Omer, de Vos, Pauwels, Torta, Monteriù; RoboCup 2024 심포지엄 논문집) | Semantic Path Planning for Heterogeneous Robots from Building Digital Twin Data | 2025 | https://link.springer.com/chapter/10.1007/978-3-031-85859-8_5 | 아니오 |
| ref-573 | buildingSMART International | Pset_DoorCommon - IFC 4.3.2 Documentation | 미확인 | https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_DoorCommon.htm | 아니오 |
| ref-574 | buildingSMART International | Pset_StairCommon - IFC4.3.2.0 Documentation | 미확인 | https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/HTML/lexical/Pset_StairCommon.htm | 아니오 |
| ref-575 | Schulze, P. R., Müller, S., Müller, T., & Gross, H.-M. (TU Ilmenau) | On realizing autonomous transport services in multi story buildings with doors and elevators | 2025-02-25 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1546894/full | 아니오 |
| ref-576 | Morilla-Cabello, D., & Montijano, E. | CHORAL: Traversal-Aware Planning for Safe and Efficient Heterogeneous Multi-Robot Routing | 2026-01 | https://arxiv.org/abs/2601.10340 | 아니오 |
| ref-577 | Halilovic, A., Hasic, V., & Krivic, S. | Ontology-Guided Reasoning for Affordance-Based Explanations of Robot Navigation | 2026-06 | https://arxiv.org/abs/2606.00117 | 아니오 |
| ref-578 | 이관용, 구한민, 이윤서, 정민승, 윤동근, 김갑성(지적과 국토정보 52(2), 17-34) | 로봇 친화형 건축물 인증 지표 개발: 초점집단면접(FGI)과 분석적 계층화 과정(AHP)의 활용 | 2022 | https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART002903574 | 아니오 |
| ref-579 | Open Robotics (ROS 2 Design) | ROS 2 Access Control Policies | 2019-08 | https://design.ros2.org/articles/ros2_access_control_policies.html | 예 |
| ref-580 | Open Robotics (ROS 2 Design) | ROS 2 Security Enclaves | 2020-05 | https://design.ros2.org/articles/ros2_security_enclaves.html | 예 |
| ref-581 | Eclipse Foundation (Eclipse Mosquitto) | mosquitto.conf man page | 미확인 | https://mosquitto.org/man/mosquitto-conf-5.html | 예 |
| ref-582 | NIST | NIST SP 800-82 Rev. 3, Guide to Operational Technology (OT) Security | 2023-09 | https://csrc.nist.gov/pubs/sp/800/82/r3/final | 아니오 |
| ref-583 | CISA | Mobile Industrial Robots Vehicles and MiR Fleet Software (ICSA-21-280-02) | 미확인 | https://www.cisa.gov/news-events/ics-advisories/icsa-21-280-02 | 아니오 |
| ref-584 | CSA / IEC (ANSI Webstore) | CAN/CSA IEC 62443-3-3-2017 - Industrial communication networks - Network and system security - Part 3-3: System security requirements and security levels (Adopted IEC 62443-3-3:2013, first edition, 2013-08) | 2013-08 | https://webstore.ansi.org/standards/csa/csaiec624432017-2442576 | 아니오 |
| ref-585 | Jaatun 외(Journal of Cybersecurity and Privacy 6(2), 52) | Security Aspects of Zones and Conduits in IEC 62443 | 2026 | https://www.mdpi.com/2624-800X/6/2/52 | 아니오 |
| ref-586 | Kambhampati, S., Valmeekam, K., Guan, L., Verma, M., Stechly, K., Bhambri, S., Saldyt, L., & Murthy, A. | LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks | 2024-02 | https://arxiv.org/abs/2402.01817 | 아니오 |
| ref-587 | 법제처 국가법령정보센터 | 개인정보 보호법 | 미확인 | https://www.law.go.kr/lsEfInfoP.do?lsiSeq=195062 | 아니오 |
| ref-588 | 김·장 법률사무소 | '이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서' 관련 인사이트 | 미확인 | https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=30477 | 아니오 |
| ref-589 | 법제처 국가법령정보센터 | 근로자참여 및 협력증진에 관한 법률 | 미확인 | https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=105636 | 아니오 |
| ref-590 | 한국인터넷진흥원(KISA) | 로봇 보안취약점 점검 체크리스트 해설서 | 미확인 | https://kisa.or.kr/2060205/form?lang_type=KO&page=&postSeq=36 | 아니오 |
| ref-591 | European Commission (Shaping Europe's digital future) | The Cyber Resilience Act - Summary of the legislative text | 미확인 | https://digital-strategy.ec.europa.eu/en/policies/cra-summary | 아니오 |
| ref-592 | ConstraintBench 저자(arXiv 2602.22465, 저자 미확인) | ConstraintBench: Benchmarking LLM Constraint Reasoning on Direct Optimization | 2026-02 | https://arxiv.org/abs/2602.22465 | 아니오 |
| ref-593 | Jain, R. 외(R-ConstraintBench 저자) | R-ConstraintBench: Evaluating LLMs on NP-Complete Scheduling | 2025-08 | https://arxiv.org/abs/2508.15204 | 아니오 |
| ref-594 | SCHEDBench 저자(arXiv 2608.00991, 저자 미확인) | SCHEDBench: A Benchmark for Evaluating LLM Constraint Faithfulness in Natural-Language Combinatorial Scheduling | 2026-08 | https://arxiv.org/abs/2608.00991 | 아니오 |
| ref-595 | Starjob 저자(arXiv 2503.01877, 저자 미확인) | Starjob: Dataset for LLM-Driven Job Shop Scheduling | 2025-03 | https://arxiv.org/abs/2503.01877 | 아니오 |
| ref-596 | teshnizi (OptiMUS 공식 저장소) | OptiMUS — Optimization Modeling Using mip Solvers and large language models (GitHub README) | 미확인 | https://github.com/teshnizi/OptiMUS | 예 |
| ref-597 | AhmadiTeshnizi, A. 외(OptiMUS 저자) | OptiMUS-0.3: Using Large Language Models to Model and Solve Optimization Problems at Scale | 2024-07 | https://arxiv.org/abs/2407.19633 | 아니오 |
| ref-598 | Kuroki, S., Nakagawa, M., Yoshida, S., Koyama, Y., & Kozuno, T.(OMRON SINIC X 등, IEEE Access 2026) | LAPPI: Interactive Optimization with LLM-Assisted Preference-Based Problem Instantiation | 2025-12 | https://arxiv.org/abs/2512.14138 | 아니오 |
| ref-599 | Luckcuck, M., Farrell, M., Dennis, L. A., Dixon, C., & Fisher, M. | Formal Specification and Verification of Autonomous Robotic Systems: A Survey | 2019-09 | https://arxiv.org/abs/1807.00048 | 아니오 |
| ref-600 | Afzal, A., Le Goues, C., Hilton, M., & Timperley, C. S. | A Study on Challenges of Testing Robotic Systems | 2020 | https://www.computer.org/csdl/proceedings-article/icst/2020/09159069/1m3oOVjQnIc | 아니오 |
| ref-601 | reeceholland (ros2_fault_injection GitHub) | ros2_fault_injection — README | 미확인 | https://github.com/reeceholland/ros2_fault_injection | 예 |
| ref-602 | University of Liverpool Autonomy and Verification (ROSMonitoring GitHub) | ROSMonitoring: a Runtime Verification Framework for ROS — README | 미확인 | https://github.com/autonomy-and-verification-uol/ROSMonitoring | 예 |
| ref-603 | IDM Lab (USC) 게재 초록, 저자 미확인 | The League of Robot Runners: Competition Goals, Designs, and Implementation [System Demonstration] | 2024 | https://idm-lab.org/bib/abstracts/Koen24p.html | 아니오 |
| ref-604 | Yan, J., Zhang, Y., Liu, Z., Zhang, H., Jiang, H., Chen, J., Smith, S. F., & Li, J. | Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems | 2026-02-17 | https://arxiv.org/abs/2602.15721 | 아니오 |
| ref-605 | NIST | ASTM Committee F45 on Driverless Automatic Guided Industrial Vehicles | 미확인 | https://www.nist.gov/programs-projects/astm-committee-f45-driverless-automatic-guided-industrial-vehicles | 아니오 |
| ref-606 | 한국표준협회 KSSN(국가표준인증종합정보센터) | KS B ISO 18646-1 로봇 — 서비스 로봇의 성능 기준 및 관련 시험방법 — 제1부 : 바퀴형 로봇의 이동능력 | 미확인 | https://www.kssn.net/search/stddetail.do?itemNo=K001010113281 | 아니오 |
| ref-607 | 한국로봇산업진흥원(KIRIA) | 시험평가 | KIRIA 첨단로봇 실증지원 디지털 플랫폼 | 미확인 | https://kiria.org/rp/kiria/tva/inr/page.dn | 아니오 |
| ref-608 | OTTO by Rockwell Automation | OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments | 2026-04 | https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/ | 아니오 |
| ref-609 | von Berg, B., Aichernig, B. K., & Wedenik, F. | BDD-Based Deadlock Avoidance for Automated Guided Vehicles in Warehouse Logistics (Case Study Paper) | 2026-05 | https://link.springer.com/chapter/10.1007/978-3-032-26204-2_16 | 아니오 |
| ref-610 | DynaSchedBench 저자(arXiv 2605.27566, 저자 미확인) | DynaSchedBench: Calibrated Dynamic Scheduling Benchmarks and Observability Paradox in LLM-based Scheduling Agents | 2026-05 | https://arxiv.org/abs/2605.27566 | 아니오 |
| ref-611 | RACE-Sched 저자(arXiv 2605.29262, 저자 미확인) | Harmonizing Real-Time Constraints and Long-Horizon Reasoning: An Asynchronous Agentic Framework for Dynamic Scheduling | 2026-05 | https://arxiv.org/abs/2605.29262 | 아니오 |
| ref-612 | Li, J., & Li, C.(소속 미확인) | LLM-Guided Heuristic Design from Simulation Traces: A Case Study in Dynamic Production and AGV Scheduling | 2026-08 | https://arxiv.org/abs/2608.09343 | 아니오 |
| ref-613 | Hu, J., Li, J., Lin, W., Jia, P., Ji, Y., & Lai, J. | PortAgent: LLM-driven Vehicle Dispatching Agent for Port Terminals | 2025-12 | https://arxiv.org/abs/2512.14417 | 아니오 |
| ref-614 | Wang, Y., & Li, K. | Large Language Models in Operations Research: Methods, Applications, and Challenges | 2025-09 | https://arxiv.org/abs/2509.18180 | 아니오 |
| ref-615 | Powell, C. 외(University of Strathclyde) | Generating textual explanations for scheduling systems leveraging the reasoning capabilities of large language models | 2025 | https://link.springer.com/article/10.1007/s10844-025-00940-w | 아니오 |
| ref-616 | Saha, S., Das, S., Duan, H., & Liu, X.-Y. | Hybrid LLM-based Intelligent Framework for Robot Task Scheduling | 2026-05 | https://arxiv.org/abs/2605.15486 | 아니오 |
| ref-617 | NIST | NIST Risk Management Framework Aims to Improve Trustworthiness of Artificial Intelligence | 2023-01-26 | https://nist.gov/news-events/news/2023/01/nist-risk-management-framework-aims-improve-trustworthiness-artificial | 아니오 |
| ref-618 | ISO/IEC | ISO/IEC 42001:2023 - AI management systems | 2023 | https://www.iso.org/standard/42001 | 아니오 |
| ref-619 | ISO/IEC | ISO/IEC 23894:2023 - AI — Guidance on risk management | 2023-02 | https://www.iso.org/standard/77304.html | 아니오 |
| ref-620 | 국가법령정보센터(과학기술정보통신부) | 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법 | 미확인 | https://www.law.go.kr/lsInfoP.do?lsiSeq=268543 | 아니오 |
| ref-621 | European Commission | AI Act | Shaping Europe's digital future | 미확인 | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | 아니오 |
| ref-622 | Liang, J. 외 | Code as Policies: Language Model Programs for Embodied Control | 2022-09 | https://arxiv.org/abs/2209.07753 | 아니오 |
| ref-623 | Agrawal, A. 외 | RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments | 2022-09 | https://arxiv.org/abs/2209.05738 | 아니오 |
| ref-624 | Sculley, D. 외 | Hidden Technical Debt in Machine Learning Systems | 2015 | https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems | 아니오 |
| ref-625 | Breck, E. 외 (Google Research) | The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction | 2017 | https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/ | 아니오 |
| ref-626 | MLflow (Linux Foundation 오픈소스 프로젝트) | ML Model Registry | MLflow AI Platform | 미확인 | https://mlflow.org/docs/latest/ml/model-registry/ | 아니오 |
| ref-627 | 머니투데이 | 포장은 로봇이, 간선운송은 무인차가…물류현장 스며든 '피지컬 AI' | 2026-09-19 | https://www.mt.co.kr/industry/2026/09/19/2026091818023697394 | 아니오 |
| ref-628 | Lee, H.-C., Woo, H.-M., & Shin, S. (International Journal of Precision Engineering and Manufacturing) | Digital Twin-based Sensor-Free Virtual Mapping for Autonomous Mobile Robot Localization | 2026 | https://link.springer.com/article/10.1007/s12541-026-01598-2 | 아니오 |
| ref-629 | Rinciog, A. 외 (malerinc/slapstack GitHub) | slapstack — README (SLAPStack: storage location assignment simulation for block-stacking warehouses) | 미확인 | https://github.com/malerinc/slapstack | 예 |
| ref-630 | Skoogh, A., & Johansson, B. | Time-consumption analysis of input data activities in discrete event simulation projects | 2007 | https://www.researchgate.net/publication/235719405_TIME-CONSUMPTION_ANALYSIS_OF_INPUT_DATA_ACTIVITIES_IN_DISCRETE_EVENT_SIMULATION_PROJECTS | 아니오 |
| ref-631 | Lee, Y.-T. T. (NIST, Journal of Research of NIST) | A Journey in Standard Development: The Core Manufacturing Simulation Data (CMSD) Information Model | 2015 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4730674/ | 아니오 |
| ref-632 | IFAC-PapersOnLine 게재 논문 저자(미확인) | Initialization of Simulation-Based Digital Twins for Internal Transport Systems | 2024 | https://www.sciencedirect.com/science/article/pii/S2405896324015374 | 아니오 |
| ref-633 | Oyediran, H., Turner, W., Kim, K., & Barrows, M. | Integration of 4D BIM and Robot Task Planning: Creation and Flow of Construction-Related Information for Action-Level Simulation of Indoor Wall Frame Installation | 2024-02 | https://arxiv.org/abs/2402.03602 | 아니오 |
| ref-634 | VDA / VDMA / KIT IFL (VDA5050 GitHub) | VDA5050/VDA5050 — README | 미확인 | https://github.com/VDA5050/VDA5050 | 예 |
| ref-635 | Semantic Versioning (Tom Preston-Werner, semver.org) | Semantic Versioning 2.0.0 | 미확인 | https://semver.org/spec/v2.0.0.html | 예 |
| ref-636 | European Union (EUR-Lex) | Regulation (EU) 2023/2854 of the European Parliament and of the Council of 13 December 2023 on harmonised rules on fair access to and use of data (Data Act) | 2023-12-13 | https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng | 아니오 |
| ref-637 | 국가법령정보센터(산업통상자원부) | 산업 디지털 전환 촉진법 (법률 제18692호) | 2022-01-04 | https://www.law.go.kr/법령/산업디지털전환촉진법/(18692,20220104) | 아니오 |
| ref-638 | 소프트웨어정책연구소(SPRi) | 산업 디지털 전환 촉진법의 의미와 시사점 | 미확인 | https://spri.kr/posts/view/23480?code=industry_trend | 아니오 |
| ref-639 | Open Source Robotics Alliance (Open Robotics) | osra-policies-and-procedures — README | 미확인 | https://github.com/openrobotics/osra-policies-and-procedures | 예 |
| ref-640 | Open Robotics (open-rmf) | rmf_building_map_msgs — rmf_building_map_msgs/msg/GraphEdge.msg | 미확인 | https://github.com/open-rmf/rmf_building_map_msgs/blob/main/rmf_building_map_msgs/msg/GraphEdge.msg | 예 |
| ref-641 | Henkel, C., & Toussaint, M. | Optimized Directed Roadmap Graph for Multi-Agent Path Finding Using Stochastic Gradient Descent | 2020-03 | https://arxiv.org/abs/2003.12924 | 아니오 |
| ref-642 | Claridades, A. R. C., Choi, H.-S., & Lee, J. | An Indoor Space Subspacing Framework for Implementing a 3D Hierarchical Network-Based Topological Data Model | 2022 | https://doi.org/10.3390/ijgi11020076 | 아니오 |
| ref-643 | Ray, A., Bradley, C., Carlone, L., & Roy, N. | Task and Motion Planning in Hierarchical 3D Scene Graphs (ISRR 2024) | 2024-03 | https://arxiv.org/abs/2403.08094 | 아니오 |
| ref-644 | ROS Navigation (ros-navigation/navigation2 GitHub) | nav2_costmap_2d — README | 미확인 | https://github.com/ros-navigation/navigation2/blob/main/nav2_costmap_2d/README.md | 예 |
| ref-645 | Open Navigation (Nav2 documentation) | Navigating with Keepout Zones — Nav2 documentation | 미확인 | https://docs.nav2.org/tutorials/docs/navigation2_with_keepout_filter.html | 아니오 |
| ref-646 | IEEE 학술대회 논문 저자(미확인) | BIM-to-Robot Mapping: Constructing IFC-Referenced Occupancy Grids and Semantic Metadata for Rule-Based Navigation | 미확인 | https://ieeexplore.ieee.org/document/11019519/ | 아니오 |
| ref-647 | Construction Robotics(Springer) 게재 논문 저자(미확인) | Improving autonomous robotic navigation using IFC files | 2023 | https://link.springer.com/article/10.1007/s41693-023-00112-8 | 아니오 |
| ref-648 | Tibebu, H., Roche, J., De Silva, V., & Kondoz, A. (Loughborough University London, Sensors 21(7), 2263) | LiDAR-Based Glass Detection for Improved Occupancy Grid Mapping | 2021-04 | https://www.mdpi.com/1424-8220/21/7/2263 | 아니오 |
| ref-649 | ROS Navigation (ros-navigation/navigation2 GitHub) | nav2_costmap_2d — include/nav2_costmap_2d/obstacle_layer.hpp | 미확인 | https://github.com/ros-navigation/navigation2/blob/main/nav2_costmap_2d/include/nav2_costmap_2d/obstacle_layer.hpp | 예 |
| ref-650 | Vega-Torres, M. A. (MigVega GitHub) | SLAM2REF — README (연계 논문 Construction Robotics 8(2), 2024-07, DOI 10.1007/s41693-024-00126-w) | 미확인 | https://github.com/MigVega/SLAM2REF | 예 |
| ref-651 | Bosché, F. (Advanced Engineering Informatics) | Automated recognition of 3D CAD model objects in laser scans and calculation of as-built dimensions for dimensional compliance control in construction (Advanced Engineering Informatics 24(1), 107-118) | 2010-01 | https://www.sciencedirect.com/science/article/abs/pii/S1474034609000482 | 아니오 |
| ref-652 | Stefanini, E., Ciancolini, E., Settimi, A., & Pallottino, L. | Safe and Robust Map Updating for Long-Term Operations in Dynamic Environments | 2023-06-30 | https://www.mdpi.com/1424-8220/23/13/6066 | 아니오 |
| ref-653 | Shaik, N., Liebig, T., Kirsch, C., & Müller, H. (KI 2017) | Dynamic Map Update of Non-static Facility Logistics Environment with a Multi-robot System | 2017-09 | https://link.springer.com/chapter/10.1007/978-3-319-67190-1_19 | 아니오 |
| ref-654 | Qian, J. 외 (RSS 2023) | POV-SLAM: Probabilistic Object-Aware Variational SLAM in Semi-Static Environments | 2023-07 | https://arxiv.org/abs/2307.00488 | 아니오 |
| ref-655 | 윤동희, 백주미, 심지수, 이동근, 송두삼(설비공학 논문집 36(5), 251-261) | 노후건축물에서 모바일기기를 이용한 Scan-to-BIM 역설계 도면생성 방안 | 2024 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003077202 | 아니오 |
| ref-656 | Open Robotics (open-rmf) | rmf_ros2 — rmf_task_ros2/src/rmf_task_ros2/Dispatcher.cpp | 미확인 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_task_ros2/src/rmf_task_ros2/Dispatcher.cpp | 예 |
| ref-657 | Open Robotics (open-rmf) | rmf_ros2 — rmf_task_ros2/include/rmf_task_ros2/bidding/Auctioneer.hpp | 미확인 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_task_ros2/include/rmf_task_ros2/bidding/Auctioneer.hpp | 예 |
| ref-658 | Rasa Technologies (RasaHQ/rasa GitHub) | Fallback and Human Handoff — Rasa documentation (docs/docs/fallback-handoff.mdx) | 미확인 | https://github.com/RasaHQ/rasa/blob/main/docs/docs/fallback-handoff.mdx | 예 |
| ref-659 | Göbelbecker, M., Keller, T., Eyerich, P., Brenner, M., & Nebel, B. | Coming Up With Good Excuses: What to do When no Plan Can be Found | 2010 | https://ojs.aaai.org/index.php/ICAPS/article/view/13421 | 아니오 |
| ref-660 | Sreedharan, S., Srivastava, S., Smith, D., & Kambhampati, S. | Why Couldn't You do that? Explaining Unsolvability of Classical Planning Problems in the Presence of Plan Advice | 2019-03 | https://arxiv.org/abs/1903.08218 | 아니오 |
| ref-661 | Chen, H. 외(OptiChat 저자) | Diagnosing Infeasible Optimization Problems Using Large Language Models | 2023-08 | https://arxiv.org/abs/2308.12923 | 아니오 |
| ref-662 | Schneider, E. 외(CE-MRS 저자) | CE-MRS: Contrastive Explanations for Multi-Robot Systems | 2024-10 | https://arxiv.org/abs/2410.08408 | 아니오 |
| ref-663 | Liang, K. 외(Introspective Planning 저자) | Introspective Planning: Aligning Robots' Uncertainty with Inherent Task Ambiguity | 2024-02 | https://arxiv.org/abs/2402.06529 | 아니오 |
| ref-664 | Suri, M. 외(University of Maryland·Adobe Research) | Structured Uncertainty guided Clarification for LLM Agents | 2025-11 | https://arxiv.org/abs/2511.08798 | 아니오 |
| ref-665 | Shida, Y. 외 | Reinforcement Learning of Multi-robot Task Allocation for Multi-object Transportation with Infeasible Tasks | 2024-04 | https://arxiv.org/abs/2404.11817 | 아니오 |
| ref-666 | Kazmi, M. (plan-failure-bench GitHub) | plan-failure-bench — README (Benchmark measuring how LLM planners fail at robot tasks) | 미확인 | https://github.com/munawarkazmi/plan-failure-bench | 예 |
| ref-667 | Open Robotics (open-rmf) | rmf_building_map_msgs — rmf_building_map_msgs/msg/Lift.msg | 미확인 | https://github.com/open-rmf/rmf_building_map_msgs/blob/main/rmf_building_map_msgs/msg/Lift.msg | 예 |
| ref-668 | Palonen, A. (axelpale/nudged GitHub) | nudged — README (Affine transformation estimator e.g. for multi-touch gestures and calibration) | 미확인 | https://github.com/axelpale/nudged | 예 |
| ref-669 | Umeyama, S. (IEEE Transactions on Pattern Analysis and Machine Intelligence 13(4), 376-380) | Least-Squares Estimation of Transformation Parameters Between Two Point Patterns | 1991 | https://ieeexplore.ieee.org/document/88573/ | 아니오 |
| ref-670 | ISO (iTeh Standards 미리보기) | ISO/FDIS 21423 - Robotics — Industrial mobile robots — Communications and interoperability | 미확인 | https://standards.iteh.ai/catalog/standards/iso/f772b16e-582a-4ed4-9f79-0a80ad376f40/iso-fdis-21423 | 아니오 |
| ref-671 | Carpin, S. (Autonomous Robots) | Fast and accurate map merging for multi-robot systems | 2008 | https://link.springer.com/article/10.1007/s10514-008-9097-4 | 아니오 |
| ref-672 | Kakuma, D., Tsuichihara, S., Garcia Ricardez, G. A., Takamatsu, J., & Ogasawara, T. | Alignment of Occupancy Grid and Floor Maps Using Graph Matching | 2017 | https://ieeexplore.ieee.org/document/7889504/ | 아니오 |
| ref-673 | Hou, J., Kuang, H., & Schwertfeger, S. (ROBIO 2019) | Fast 2D Map Matching Based on Area Graphs | 2019 | https://arxiv.org/abs/1911.07432 | 아니오 |
| ref-674 | Liu, Z., Fernandez-Ayala, V. N., Wang, T., Qin, Q., Wang, X. V., Dimarogonas, D. V., & Wang, L.(KTH) | Agentic Neuro-Symbolic Planning and Commissioning for Human-in-the-Loop Industrial Robotics with Digital Twins | 2026-06 | https://arxiv.org/abs/2606.08214 | 아니오 |
| ref-675 | Pesjak, D., & Žabkar, J. | Robot Planning via LLM Proposals and Symbolic Verification | 2026 | https://www.mdpi.com/2504-4990/8/1/22 | 아니오 |
| ref-676 | Pesjak, D. (minigrid-crewai 공식 저장소) | minigrid-crewai — Sense–Plan–Code–Act (SPCA) framework (GitHub README) | 미확인 | https://github.com/DrejcPesjak/minigrid-crewai | 예 |
| ref-677 | CoMuRoS 저자(arXiv 2511.22354, Frontiers in Robotics and AI 게재) | LLM-Based Generalizable Hierarchical Task Planning and Execution for Heterogeneous Robot Teams with Event-Driven Replanning | 2025-11 | https://arxiv.org/abs/2511.22354 | 아니오 |
| ref-678 | Park, J., & Kim, J. S.(소속 미확인) | STRAP-LLM: structured task allocation and planning for heterogeneous robots using large language models | 미확인 | https://link.springer.com/article/10.1007/s11370-025-00676-0 | 아니오 |
| ref-679 | 국토교통부(법제처 국가법령정보센터) | 실내공간정보구축작업규정 (고시 제2021-1445호, 2021-12-24) | 2021-12-24 | https://www.law.go.kr/%ED%96%89%EC%A0%95%EA%B7%9C%EC%B9%99/%EC%8B%A4%EB%82%B4%EA%B3%B5%EA%B0%84%EC%A0%95%EB%B3%B4%EA%B5%AC%EC%B6%95%EC%9E%91%EC%97%85%EA%B7%9C%EC%A0%95/(2021-1445,20211224) | 아니오 |
| ref-680 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/skip_phase_request.json | 미확인 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/skip_phase_request.json | 예 |
| ref-681 | OPC Foundation | OPC UA for ISA-95 - Part 4: Job Control (OPC 10031-4) — 6 ISA-95 Data Representation Model | 미확인 | https://reference.opcfoundation.org/ISA95JOBCONTROL/v200/docs/6 | 아니오 |
| ref-682 | Vieira, G. E., Herrmann, J. W., & Lin, E. (Journal of Scheduling 6(1), 35-58) | Rescheduling Manufacturing Systems: A Framework of Strategies, Policies, and Methods | 2003 | https://link.springer.com/article/10.1023/A:1022235519958 | 아니오 |
| ref-683 | Sridharan, S. V., Berry, W. L., & Udayabhanu, V. (Management Science 33(9), 1137-1149) | Freezing the Master Production Schedule Under Rolling Planning Horizons | 1987-09 | https://pubsonline.informs.org/doi/10.1287/mnsc.33.9.1137 | 아니오 |
| ref-684 | InterruptBench 저자(arXiv 2604.00892, 저자 미확인) | When Users Change Their Mind: Evaluating Interruptible Agents in Long-Horizon Web Navigation | 2026-04 | https://arxiv.org/abs/2604.00892 | 아니오 |
| ref-685 | Rasa Technologies (RasaHQ/rasa-calm-demo GitHub) | rasa-calm-demo — data/flows/patterns.yml | 미확인 | https://github.com/RasaHQ/rasa-calm-demo/blob/main/data/flows/patterns.yml | 예 |
| ref-686 | 양진홍, 유남현(한국정보전자통신기술학회논문지 18(3), 155-171) | AI 기반 멀티 에이전트 시스템 제조 환경 도입 방법론 연구(A Study on the Methodology for Implementing AI-based Multi-Agent Systems in Manufacturing Environments) | 2025-06 | https://www.koreascience.kr/article/JAKO202519736002981.page | 아니오 |
| ref-687 | IfcOpenShell (IfcOpenShell GitHub) | IfcDiff - IfcOpenShell documentation (src/ifcopenshell-python/docs/ifcdiff.rst, v0.8.0) | 미확인 | https://docs.ifcopenshell.org/ifcdiff.html | 예 |
| ref-688 | Open Robotics (open-rmf) | rmf_building_map_msgs — rmf_building_map_msgs/msg/BuildingMap.msg | 미확인 | https://github.com/open-rmf/rmf_building_map_msgs/blob/main/rmf_building_map_msgs/msg/BuildingMap.msg | 예 |
| ref-689 | UK BIM Framework | Information management according to BS EN ISO 19650 Guidance Part C: Facilitating the common data environment (workflow and technical solutions), Edition 1 | 2020-09 | https://ukbimframework.org/wp-content/uploads/2020/09/Guidance-Part-C_Facilitating-the-common-data-environment-workflow-and-technical-solutions_Edition-1.pdf | 아니오 |
| ref-690 | ACCA software (BibLus) | Container Information States ISO 19650: WIP, Shared, Published, Archived | 미확인 | https://biblus.accasoftware.com/en/container-information-states-iso-19650-wip-shared-published-archived/ | 아니오 |
| ref-691 | 이일곤, 김현민, 안준상, 최재웅 | ISO 19650 기반의 한국형 공통데이터환경(CDE) 개발을 위한 CDE 워크플로우와 정보컨테이너 체계 수립 연구 | 2023 | https://koreascience.kr/article/JAKO202309243229252.pdf | 아니오 |
| ref-692 | Liu, H., Gao, G., & Gu, M. (EG-ICE 2023, 511-520) | A Parallel IFC Normalization Algorithm for Incremental Storage and Version Control (arXiv 프리프린트) | 2023-12 | https://arxiv.org/abs/2312.14931 | 아니오 |
| ref-693 | Esser, S., Vilgertshofer, S., & Borrmann, A. (Automation in Construction 155, 105063) | Version control for asynchronous BIM collaboration: Model merging through graph analysis and transformation | 2023-11 | https://www.sciencedirect.com/science/article/pii/S0926580523003230 | 아니오 |
| ref-694 | NODE Robotics | Real-time Robot Map Management for Mobile Fleets (NODE.maps) | 미확인 | https://node-robotics.com/solutions/node-fleet-autonomy-services/nodemaps | 아니오 |
| ref-695 | OWASP Top 10 for LLM Applications 프로젝트 (OWASP GitHub) | LLM06:2025 Excessive Agency (2_0_vulns/LLM06_ExcessiveAgency.md) | 2024-11 | https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/2_0_vulns/LLM06_ExcessiveAgency.md | 예 |
| ref-696 | Model Context Protocol (modelcontextprotocol GitHub) | Specification 2025-06-18 — Server Features: Tools (docs/specification/2025-06-18/server/tools.mdx) | 2025-06-18 | https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2025-06-18/server/tools.mdx | 예 |
| ref-697 | LangChain (langchain-ai/docs GitHub) | Human-in-the-loop — LangChain docs (src/oss/langchain/human-in-the-loop.mdx) | 미확인 | https://docs.langchain.com/oss/python/langchain/human-in-the-loop | 예 |
| ref-698 | Yang, Z. 외(Brown University H2R Lab) | Plug in the Safety Chip: Enforcing Constraints for LLM-driven Robot Agents | 2023-09 | https://arxiv.org/abs/2309.09919 | 아니오 |
| ref-699 | YzyLmc (Safety Chip 공식 저장소) | ltl_safety — README (Plug in the Safety Chip) | 미확인 | https://github.com/YzyLmc/ltl_safety | 예 |
| ref-700 | Ravichandran, Z., Robey, A., Kumar, V., Pappas, G. J., & Hassani, H.(IEEE RA-L 2026 채택 표기) | Safety Guardrails for LLM-Enabled Robots | 2025-03 | https://arxiv.org/abs/2503.07885 | 아니오 |
| ref-701 | KumarRobotics (RoboGuard 공식 저장소) | RoboGuard — Safety guardrails for LLM-enabled robots (GitHub README) | 미확인 | https://github.com/KumarRobotics/RoboGuard | 예 |
| ref-702 | SafePlan 저자(arXiv 2503.06892, 저자 미확인) | SafePlan: Leveraging Formal Logic and Chain-of-Thought Reasoning for Enhanced Safety in LLM-based Robotic Task Planning | 2025-03 | https://arxiv.org/abs/2503.06892 | 아니오 |
| ref-703 | RichardHGL (CHI 2025 Plan-then-Execute 공식 저장소) | CHI2025_Plan-then-Execute_LLMAgent — README | 미확인 | https://github.com/RichardHGL/CHI2025_Plan-then-Execute_LLMAgent | 예 |
| ref-704 | Open Source Robotics Alliance | Charter of the Open Source Robotics Alliance Project 'Open-RMF' | 2024-03 | https://osralliance.org/wp-content/uploads/2024/03/open-rmf-project-charter.pdf | 아니오 |
| ref-705 | OPC Foundation | How to Certify - OPC Foundation | 미확인 | https://opcfoundation.org/certification/how-to-certify/ | 아니오 |
| ref-706 | IETF (RFC Editor) | RFC 9745: The Deprecation HTTP Response Header Field | 미확인 | https://www.rfc-editor.org/info/rfc9745/ | 아니오 |
| ref-707 | IEC | IEC 62443-3-3:2013 Industrial communication networks — Network and system security — Part 3-3: System security requirements and security levels (sample) | 2013-08 | https://cdn.standards.iteh.ai/samples/19488/7c0b753be32e46fc986c23c32efbdbe8/IEC-62443-3-3-2013.pdf | 아니오 |
| ref-708 | ISO/IEC | ISO/IEC 20000-1:2018 - Information technology — Service management — Part 1: Service management system requirements | 2018 | https://www.iso.org/standard/70636.html | 아니오 |
| ref-709 | 대한민국 정책브리핑(산업통상자원부 국가기술표준원) | 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 | 2021-11-11 | https://korea.kr/news/pressReleaseView.do?newsId=156480155 | 아니오 |
| ref-710 | 한국지능형로봇표준포럼(KOROS) | KOROS 1148-8:2025 서비스 로봇을 위한 모듈 - 제2-8부 : 소프트웨어 모듈용 정보모델 상호운용성 시험 절차 | 2025-06-04 | http://www.koros.or.kr/bbs/board.php?bo_table=notice27&wr_id=223 | 아니오 |
| ref-711 | Tang, G. 외(arXiv 2606.31339) | Verification-Gated Agentic Mission-State Governance for Intelligent Industrial Multi-Robot Systems | 2026-06 | https://arxiv.org/abs/2606.31339 | 아니오 |
| ref-712 | robotmcp (ROS-MCP-Server 공식 저장소) | ros-mcp-server — Connect AI models like Claude & GPT with robots using MCP and ROS (GitHub README) | 미확인 | https://github.com/robotmcp/ros-mcp-server | 예 |
| ref-713 | He, G., Demartini, G., & Gadiraju, U. | Plan-Then-Execute: An Empirical Study of User Trust and Team Performance When Using LLM Agents As A Daily Assistant | 2025-04 | https://dl.acm.org/doi/10.1145/3706598.3713218 | 아니오 |
| ref-714 | arXiv 2604.04918 저자(미확인) | Comparing Human Oversight Strategies for Computer-Use Agents | 2026-04 | https://arxiv.org/abs/2604.04918 | 아니오 |
| ref-715 | Future of Life Institute (artificialintelligenceact.eu, EU 규정 2024/1689 조문 게재본) | Article 14: Human Oversight | EU Artificial Intelligence Act | 2024 | https://artificialintelligenceact.eu/article/14/ | 아니오 |
| ref-716 | arXiv 2502.10036 저자(미확인) | Automation Bias in the AI Act: On the Legal Implications of Attempting to De-Bias Human Oversight of AI | 2025-02 | https://arxiv.org/abs/2502.10036 | 아니오 |
| ref-717 | Sagawa, H., Mitamura, T., & Nyberg, E. (INTERSPEECH 2004-ICSLP) | A comparison of confirmation styles for error handling in a speech dialog system | 2004-10 | https://www.isca-archive.org/interspeech_2004/sagawa04_interspeech.pdf | 아니오 |
| ref-718 | Chen, J., Liu, C., Wu, J., & Furukawa, Y. | Floor-SP: Inverse CAD for Floorplans by Sequential Room-wise Shortest Path | 2019-08 | https://arxiv.org/abs/1908.06702 | 아니오 |
| ref-719 | Stekovic, S., Rad, M., Fraundorfer, F., & Lepetit, V. | MonteFloor: Extending MCTS for Reconstructing Accurate Large-Scale Floor Plans | 2021-03 | https://arxiv.org/abs/2103.11161 | 아니오 |
| ref-720 | van Engelenburg, C. 외 (caspervanengelenburg GitHub) | ssig — README (SSIG: A Visually-Guided Graph Edit Distance for Floor Plan Similarity, ICCVW 2023) | 2023 | https://github.com/caspervanengelenburg/ssig | 예 |
| ref-721 | ISO | ISO 18646-2:2024 - Robotics — Performance criteria and related test methods for service robots — Part 2: Navigation | 2024-01 | https://www.iso.org/standard/82643.html | 아니오 |
| ref-722 | KISTI ScienceON(정부 R&D 보고서) | 이동/조작/HRI/통신성능 등 서비스로봇 성능평가 및 표준화 기술개발 | 미확인 | https://scienceon.kisti.re.kr/srch/selectPORSrchReport.do?cn=TRKO201800040065 | 아니오 |
| ref-723 | ASTM International | F3244 Standard Test Method for Navigation: Defined Area | 2021 | https://store.astm.org/f3244-21.html | 아니오 |
| ref-724 | Bostelman, R. V., Hong, T. H., & Cheok, G. S. (NIST) | Navigation Performance Evaluation for Automated Guided Vehicles | 2015 | https://www.nist.gov/publications/navigation-performance-evaluation-automated-guided-vehicles | 아니오 |
| ref-725 | Anderson, P. 외 | On Evaluation of Embodied Navigation Agents | 2018-07 | https://arxiv.org/abs/1807.06757 | 아니오 |
| ref-726 | Kästner, L. 외 | Arena-Bench: A Benchmarking Suite for Obstacle Avoidance Approaches in Highly Dynamic Environments | 2022-06 | https://arxiv.org/abs/2206.05728 | 아니오 |
| ref-727 | Filatov, A. 외 | 2D SLAM Quality Evaluation Methods | 2017-08 | https://arxiv.org/abs/1708.02354 | 아니오 |
| ref-728 | Francis, A. 외 | Long-Range Indoor Navigation with PRM-RL | 2019-02 | https://arxiv.org/abs/1902.09458 | 아니오 |
| ref-729 | HKUST Aerial Robotics Group (HKUST-Aerial-Robotics GitHub) | SLABIM — README (SLABIM: A SLAM-BIM Coupled Dataset in HKUST Main Building) | 2025-01-28 | https://github.com/HKUST-Aerial-Robotics/SLABIM | 예 |
| ref-730 | Kim, T., Yoon, H., Lee, Y., Kang, P., Bang, J., & Kim, M.(ACL 2022 Short Papers, 소속 미확인) | Mismatch between Multi-turn Dialogue and its Evaluation Metric in Dialogue State Tracking | 2022-05 | https://aclanthology.org/2022.acl-short.33/ | 아니오 |
| ref-731 | Qin, L., Xie, T., Che, W., & Liu, T.(IJCAI 2021) | A Survey on Spoken Language Understanding: Recent Advances and New Frontiers | 2021 | https://www.ijcai.org/proceedings/2021/0622.pdf | 아니오 |
| ref-732 | Gramopadhye, M., & Szafir, D. | Generating Executable Action Plans with Environmentally-Aware Language Models | 2022-10 | https://arxiv.org/abs/2210.04964 | 아니오 |
| ref-733 | Goren, S., & Sabuncuoglu, I.(IIE Transactions 40(1), 66-83) | Robustness and stability measures for scheduling: single-machine environment | 2008 | https://www.tandfonline.com/doi/full/10.1080/07408170701283198 | 아니오 |
| ref-734 | Rangsaritratsamee, R., Ferrell Jr., W. G., & Kurz, M. B.(Computers & Industrial Engineering 46) | Dynamic rescheduling that simultaneously considers efficiency and stability | 2004 | https://www.sciencedirect.com/science/article/abs/pii/S0360835203000950 | 아니오 |
| ref-735 | Aakriti05 (RTAW 공식 저장소) | RTAW-Centralised-multi-robot-task-allocation — README | 미확인 | https://github.com/Aakriti05/RTAW-Centralised-multi-robot-task-allocation | 예 |
| ref-736 | Patil, S. G. 외(Gorilla/BFCL 저자, ICML 2025 PMLR v267) | The Berkeley Function Calling Leaderboard (BFCL): From Tool Use to Agentic Evaluation of Large Language Models | 2025 | https://proceedings.mlr.press/v267/patil25a.html | 아니오 |
| ref-737 | ShishirPatil (gorilla GitHub) | berkeley-function-call-leaderboard — README | 미확인 | https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard | 예 |
| ref-738 | Yao, S. 외(Sierra, τ-bench 저자) | τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains | 2024-06 | https://arxiv.org/abs/2406.12045 | 아니오 |
| ref-739 | sierra-research (tau-bench GitHub) | tau-bench — README | 미확인 | https://github.com/sierra-research/tau-bench | 예 |
| ref-740 | Lost in Simulation 저자(arXiv 2601.17087, 게재처 미확인) | Lost in Simulation: LLM-Simulated Users are Unreliable Proxies for Human Users in Agentic Evaluations | 2026-01 | https://arxiv.org/abs/2601.17087 | 아니오 |
| ref-741 | Aljalbout, E. 외(University of Zurich·NVIDIA·University of Washington) | The Reality Gap in Robotics: Challenges, Solutions, and Best Practices | 2025-10 | https://arxiv.org/abs/2510.20808 | 아니오 |
| ref-742 | coatyio (vda-5050-lib.js GitHub) | vda-5050-lib.js — Universal VDA 5050 library for Node.js and browsers (README) | 미확인 | https://github.com/coatyio/vda-5050-lib.js | 예 |
| ref-743 | Wu, J., Lu, C., Arrieta, A., & Ali, S. 외(Simula Research Laboratory·Mondragon University·PAL Robotics) | Vision Language Model-based Testing of Industrial Autonomous Mobile Robots | 2025-08 | https://arxiv.org/abs/2508.02338 | 아니오 |
| ref-744 | Yin, S. 외(SafeAgentBench 저자) | SafeAgentBench: A Benchmark for Safe Task Planning of Embodied LLM Agents | 2024-12 | https://arxiv.org/abs/2412.13178 | 아니오 |
| ref-745 | shengyin1224 (SafeAgentBench 공식 저장소) | SafeAgentBench — README | 미확인 | https://github.com/shengyin1224/SafeAgentBench | 예 |
| ref-746 | Atil, B. 외 | Non-Determinism of "Deterministic" LLM Settings | 2024-08 | https://arxiv.org/abs/2408.04667 | 아니오 |
| ref-747 | 인더스트리뉴스 | 다임리서치, 가상검증 기술로 물류자동화 실현 | 미확인 | https://www.industrynews.co.kr/news/articleView.html?idxno=56677 | 아니오 |
| ref-748 | JSON Schema (json-schema-org/json-schema-spec GitHub) | json-schema-spec — specs/jsonschema-validation.md (JSON Schema Validation: A Vocabulary for Structural Validation of JSON) | 미확인 | https://github.com/json-schema-org/json-schema-spec/blob/main/specs/jsonschema-validation.md | 예 |
| ref-749 | guidance-ai (JSONSchemaBench GitHub) | jsonschemabench — README (JSONSchemaBench) | 미확인 | https://github.com/guidance-ai/jsonschemabench | 예 |
| ref-750 | Geng, S. 외(JSONSchemaBench 저자, arXiv 2501.10868) | JSONSchemaBench: A Rigorous Benchmark of Structured Outputs for Language Models | 2025-01 | https://arxiv.org/abs/2501.10868 | 아니오 |
| ref-751 | KCL-Planning (VAL GitHub) | VAL — The plan validation system (README) | 미확인 | https://github.com/KCL-Planning/VAL | 예 |
| ref-752 | Guan, L., Valmeekam, K., Sreedharan, S., & Kambhampati, S. | Leveraging Pre-trained Large Language Models to Construct and Utilize World Models for Model-based Task Planning | 2023-05 | https://arxiv.org/abs/2305.14909 | 아니오 |
| ref-753 | VerifyLLM 저자(arXiv 2507.05118) | VerifyLLM: LLM-Based Pre-Execution Task Plan Verification for Robots | 2025-07 | https://arxiv.org/abs/2507.05118 | 아니오 |
| ref-754 | Hariharan, A., Dongre, V., Hakkani-Tür, D., & Tur, G. | Plan Verification for LLM-Based Embodied Task Completion Agents | 2025-09 | https://arxiv.org/abs/2509.02761 | 아니오 |
| ref-755 | Raman, S. S., Cohen, V., Idrees, I., Rosen, E., Mooney, R., Tellex, S., & Paulius, D. | CAPE: Corrective Actions from Precondition Errors using Large Language Models | 2022-11 | https://arxiv.org/abs/2211.09935 | 아니오 |
| ref-756 | Lu, X., Zhang, R. H., & Zhang, R.(Pennsylvania State University) | SIMMER: Benchmarking Latent Failures in LLM Executable Planning with a World Model | 2026-06 | https://arxiv.org/abs/2606.14574 | 아니오 |
| ref-757 | Lee, Y.-H., Nam, T., Cho, D.-S., & Kim, W.-T. | LLM-Based Adaptive Control Code Generation Framework with Digital Twin-Integrated Verification for Heterogeneous Robot Systems | 2026-04 | https://doi.org/10.3390/app16083883 | 아니오 |
| ref-758 | Deng, M., Fu, B., Li, L., & Wang, X. | Integrating LLMs and Digital Twins for Adaptive Multi-Robot Task Allocation in Construction | 2025-06 | https://arxiv.org/abs/2506.18178 | 아니오 |
| ref-759 | Ko, T.-H., & Lin, C.-T.(National Central University) | Human-AI Collaboration for Multi-Line Task Adjustment Using Local Large Language Models and a Digital Twin | 2026-09 | https://arxiv.org/abs/2609.29061 | 아니오 |
| ref-760 | Köcher, A., da Silva, L. M. V., & Fay, A.(Helmut Schmidt University) | Constraint Checking of Skills using SHACL | 2021-07 | https://ieeexplore.ieee.org/abstract/document/9557549/ | 아니오 |
| ref-761 | SELP 저자(arXiv 2409.19471) | SELP: Generating Safe and Efficient Task Plans for Robot Agents with Large Language Models | 2024-09 | https://arxiv.org/abs/2409.19471 | 아니오 |
| ref-762 | Open Robotics (open-rmf) | rmf-web — packages/api-server/README.md | 미확인 | https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md | 예 |
| ref-763 | Model Context Protocol (modelcontextprotocol GitHub) | Specification 2025-06-18 — Basic: Authorization (docs/specification/2025-06-18/basic/authorization.mdx) | 2025-06-18 | https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2025-06-18/basic/authorization.mdx | 예 |
| ref-764 | Future of Life Institute (artificialintelligenceact.eu, EU 규정 2024/1689 조문 게재본) | Article 12: Record-Keeping | EU Artificial Intelligence Act | 2024 | https://artificialintelligenceact.eu/article/12/ | 아니오 |
| ref-765 | Future of Life Institute (artificialintelligenceact.eu, EU 규정 2024/1689 조문 게재본) | Article 19: Automatically Generated Logs | EU Artificial Intelligence Act | 2024 | https://artificialintelligenceact.eu/article/19/ | 아니오 |
| ref-766 | 국가법령정보센터(개인정보보호위원회 고시) | 개인정보의 안전성 확보조치 기준 | 미확인 | https://www.law.go.kr/admRulLsInfoP.do?chrClsCd=010202&admRulSeq=2100000229672 | 아니오 |
| ref-767 | IEC | IEC 62443-3-3:2013 Industrial communication networks — Network and system security — Part 3-3: System security requirements and security levels | 2013-08 | https://standards.iteh.ai/catalog/standards/iec/c32e05fe-78a2-467e-a24d-0fc422289f55/iec-62443-3-3-2013 | 아니오 |
| ref-768 | NIST | Guide to Attribute Based Access Control (ABAC) Definition and Considerations (NIST SP 800-162) | 2014-01 | https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-162.pdf | 아니오 |
| ref-769 | Shi, T. 외(Progent 저자, 소속 미확인) | Progent: Programmable Privilege Control for LLM Agents | 2025-04 | https://arxiv.org/abs/2504.11703 | 아니오 |
| ref-770 | South, T., Marro, S., Hardjono, T., Mahari, R., Whitney, C. D., Greenwood, D., Chan, A., & Pentland, A. | Authenticated Delegation and Authorized AI Agents | 2025-01 | https://arxiv.org/abs/2501.09674 | 아니오 |
| ref-771 | Tsai, L., & Bagdasarian, E.(Google, HotOS 2025) | Contextual Agent Security: A Policy for Every Purpose | 2025-01 | https://arxiv.org/abs/2501.17070 | 아니오 |
| ref-772 | Luo, J. 외(Fudan University·Shanghai Innovation Institute) | AgentGuard: An Attribute-Based Access Control Framework for Tool-Use LLM-Based Agent | 2026-05 | https://arxiv.org/abs/2605.28071 | 아니오 |
| ref-773 | Zhu, J., Tseng, K., Vernik, G., Huang, X., Patil, S. G., Fang, V., & Popa, R. A.(arXiv 2512.11147) | MiniScope: A Least-Privilege Framework for Authorizing Tool-Calling Agents | 2025-12 | https://arxiv.org/abs/2512.11147 | 아니오 |
| ref-774 | Mobile Industrial Robots(MiR) | MiR Fleet | 미확인 | https://mobile-industrial-robots.com/products/software/mir-fleet | 아니오 |
| ref-775 | Automated Warehouse | MiR Fleet Enterprise includes scalability, cybersecurity features for mobile robots | 미확인 | https://www.automatedwarehouseonline.com/mir-fleet-enterprise-includes-scalability-cybersecurity-features-mobile-robots/ | 아니오 |
| ref-776 | Wang, Y. 외(arXiv 2606.04990) | From Agent Traces to Trust: A Survey of Evidence Tracing and Execution Provenance in LLM Agents | 2026-06 | https://arxiv.org/abs/2606.04990 | 아니오 |
| ref-777 | Gupta, R. 외(RobotFleet 저자, arXiv 2510.10379) | RobotFleet: An Open-Source Framework for Centralized Multi-Robot Task Planning | 2025-10 | https://arxiv.org/abs/2510.10379 | 아니오 |
| ref-778 | therohangupta (RobotFleet 공식 저장소) | robot-fleet — RobotFleet: An Open-Source Framework for Centralized Multi-Robot Task Planning (GitHub README) | 미확인 | https://github.com/therohangupta/robot-fleet | 예 |
| ref-779 | Garrabé, É., Teixeira, P., Khoramshahi, M., & Doncieux, S. | Enhancing Robustness in Language-Driven Robotics: A Modular Approach to Failure Reduction | 2024-11 | https://arxiv.org/abs/2411.05474 | 아니오 |
| ref-780 | 강건(대한산업공학회 추계학술대회 논문집) | 제조 물류 로봇에서의 대규모 언어 모델(LLM)을 활용한 로봇 협업 인터페이스 구축 | 2023-11 | https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11609734 | 아니오 |
| ref-792 | Forte, M., Price, B., Cohen, S., Xu, N., & Pitié, F. (arXiv 2003.07932) | Getting to 99% Accuracy in Interactive Segmentation | 2020-03 | https://arxiv.org/abs/2003.07932 | 아니오 |
| ref-793 | Zhang, H. (Independent Researcher, arXiv 2608.25608) | When Should a Network Emit Geometry, and When Should It Detect It? Readout, Reconciliation, and Representation in Floorplan Vectorization | 2026-08 | https://arxiv.org/abs/2608.25608 | 아니오 |
| ref-794 | Opiela, M., & Hrehová, M. (Pavol Jozef Šafárik University, IPIN-WiP 2023, CEUR-WS Vol-3581) | Map Model Extraction from Image Floor Plans | 2023 | https://ceur-ws.org/Vol-3581/194_WiP.pdf | 아니오 |
| ref-795 | Acuna, D., Ling, H., Kar, A., & Fidler, S. (CVPR 2018) | Efficient Interactive Annotation of Segmentation Datasets with Polygon-RNN++ | 2018-03 | https://arxiv.org/abs/1803.09693 | 아니오 |
| ref-796 | Castrejón, L., Kundu, K., Urtasun, R., & Fidler, S. (CVPR 2017) | Annotating Object Instances with a Polygon-RNN | 2017-04 | https://arxiv.org/abs/1704.05548 | 아니오 |
| ref-797 | Song, W. 외 (BMVC 2023, arXiv 2311.18166) | A-Scan2BIM: Assistive Scan to Building Information Modeling | 2023-11 | https://arxiv.org/abs/2311.18166 | 아니오 |
| ref-798 | Song, W. (weiliansong/A-Scan2BIM GitHub) | A-Scan2BIM — README (Official implementation of the paper A-Scan2BIM: Assistive Scan to Building Information Modeling) | 미확인 | https://github.com/weiliansong/A-Scan2BIM | 예 |
| ref-799 | Snover, M., Dorr, B., Schwartz, R., Micciulla, L., & Makhoul, J. (AMTA 2006) | A Study of Translation Edit Rate with Targeted Human Annotation | 2006-08 | https://aclanthology.org/2006.amta-papers.25/ | 아니오 |
| ref-800 | Koponen, M., Aziz, W., Ramos, L., & Specia, L. (AMTA 2012 WPTP) | Post-editing time as a measure of cognitive effort | 2012-10 | https://aclanthology.org/2012.amta-wptp.2/ | 아니오 |
| ref-801 | Alvarez, S., Oliver, A., & Badia, T. (EAMT 2020) | Quantitative Analysis of Post-Editing Effort Indicators for NMT | 2020-11 | https://aclanthology.org/2020.eamt-1.44.pdf | 아니오 |
| ref-802 | Kieras, D. (University of Michigan) | Using the Keystroke-Level Model to Estimate Execution Times | 미확인 | https://www.cs.umd.edu/~golbeck/INST631/KSM.pdf | 아니오 |
| ref-803 | ScienceDirect 게재 논문 저자(미확인) | A structured review of virtual commissioning: simulation fidelity, industrial validation, and design-oriented decision-making | 2026 | https://www.sciencedirect.com/science/article/pii/S2590123026038491 | 아니오 |
| ref-804 | 박준우, 김재홍, 김소현, 이지민, 최창순, 정광복, 이재욱(KIBIM Magazine 11(4), 53-62) | Scan-to-BIM 자동화 기술을 활용한 건축물 단위의 BIM 모델 생성 - 강원소방학교 BIM 모델링 실증을 중심으로 - | 2021 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002801297 | 아니오 |
| ref-805 | Journal of Asian Architecture and Building Engineering 게재 논문 저자(미확인) | Automated BIM generation using drawing recognition and line-text extraction | 2020 | https://www.tandfonline.com/doi/full/10.1080/13467581.2020.1806071 | 아니오 |
| ref-806 | ResearchGate 게재 논문 저자(미확인) | Time-Benefit Analysis of Semiautomatic 3D Laser Scanning for BIM-based Facility Management | 2024-06 | https://www.researchgate.net/publication/381549957_Time-Benefit_Analysis_of_Semiautomatic_3D_Laser_Scanning_for_BIM-_based_Facility_Management | 아니오 |
| ref-807 | Cochrane | Chapter 14: Completing ‘Summary of findings’ tables and grading the certainty of the evidence | 미확인 | https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-14 | 아니오 |
| ref-808 | Dybå, T., & Dingsøyr, T. (ESEM 2008) | Strength of evidence in systematic reviews in software engineering | 2008 | https://dl.acm.org/doi/10.1145/1414004.1414034 | 아니오 |
| ref-809 | NASA ESTO | Definition Of Technology Readiness Levels | 미확인 | https://esto.nasa.gov/files/trl_definitions.pdf | 아니오 |
| ref-810 | 방위사업청(국가법령정보센터) | 기술성숙도평가(TRA) 업무지침 | 미확인 | https://www.law.go.kr/LSW/admRulLsInfoP.do?admRulSeq=2000000018891 | 아니오 |
```

### docs/glossary/index.md (요약형 전체 205개: slug: 한국어 (영어) · 상태)

```markdown
- ablation-study: 절제 실험 (Ablation Study) · published
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG)) · published
- age-of-information: 정보 나이 (Age of Information (AoI)) · published
- aggregation-event: 집계 이벤트 (AggregationEvent) · published
- ariac: 산업 자동화용 민첩 로봇 경진대회 (Agile Robotics for Industrial Automation Competition (ARIAC)) · draft
- artificial-intelligence-management-system: AI 관리 시스템 (Artificial Intelligence Management System (AIMS)) · published
- asset-administration-shell: 자산관리셸 (Asset Administration Shell (AAS)) · published
- association-event: 연결 이벤트 (AssociationEvent) · published
- attribute-based-access-control: 속성 기반 접근 통제 (Attribute-Based Access Control (ABAC)) · published
- audit-trail: 감사 추적 (Audit Trail) · published
- automation-bias: 자동화 편향 (Automation Bias) · published
- b2mml: B2MML (Business To Manufacturing Markup Language (B2MML)) · published
- battery-swapping: 배터리 교환 (Battery Swapping) · published
- behavior-tree: 행동 트리 (Behavior Tree) · published
- block-reference: 블록 참조 (Block Reference (INSERT)) · published
- bpmn: 비즈니스 프로세스 모델 및 표기법 (Business Process Model and Notation (BPMN)) · published
- building-information-modeling: 건물 정보 모델링 (Building Information Modeling (BIM)) · published
- building-topology-ontology: 건물 위상 온톨로지 (Building Topology Ontology (BOT)) · published
- business-continuity-management-system: 업무 연속성 관리 시스템 (Business Continuity Management System (BCMS)) · published
- business-location: 업무 위치 (Business Location (EPCIS bizLocation)) · published
- cap-theorem: CAP 정리 (CAP Theorem) · published
- capabilities-skills-services: 능력·스킬·서비스 모델 (Capabilities, Skills and Services (CSS) Model) · published
- capability-based-task-allocation: 능력 기반 작업 배정 (Capability-based Task Allocation) · published
- capability-matchmaking: 능력 매칭 (Capability Matchmaking) · published
- cbv: 핵심 업무 어휘 (Core Business Vocabulary (CBV)) · published
- collaborative-application: 협동 적용 (Collaborative Application) · published
- collaborative-perception: 협동 인지 (Collaborative Perception) · published
- common-coordinate-system: 공통 좌표계 (Common Coordinate System (CCS, ISO 21423)) · published
- common-data-environment: 공통 데이터 환경 (Common Data Environment (CDE)) · published
- compensating-transaction: 보상 트랜잭션 (Compensating Transaction) · published
- condition-based-maintenance: 상태 기반 정비 (Condition-Based Maintenance (CBM)) · published
- conflict-based-search: 충돌 기반 탐색 (Conflict-Based Search (CBS)) · published
- conformal-prediction: 등각 예측 (Conformal Prediction) · published
- conformance-test: 적합성 시험 (Conformance Test) · published
- confused-deputy: 혼란된 대리인 (Confused Deputy) · published
- consensus-based-bundle-algorithm: 합의 기반 번들 알고리즘 (Consensus-Based Bundle Algorithm (CBBA)) · published
- constrained-decoding: 제약 디코딩 (Constrained Decoding) · published
- contrastive-explanation: 대조적 설명 (Contrastive Explanation) · published
- cooperative-object-transport: 협동 운반 (Cooperative Object Transport) · published
- cora: 로봇·자동화 핵심 온톨로지 (Core Ontology for Robotics and Automation (CORA)) · published
- core-manufacturing-simulation-data: 핵심 제조 시뮬레이션 데이터 (Core Manufacturing Simulation Data (CMSD)) · published
- costmap: 비용 지도 (Costmap) · published
- crdt: 무충돌 복제 데이터 타입 (Conflict-free Replicated Data Type (CRDT)) · published
- cross-schedule-dependency: 스케줄 간 의존 (Cross-schedule Dependency (XD)) · published
- dds-security: DDS 보안 규격 (DDS Security (DDS-Security)) · published
- deadlock: 교착 (Deadlock) · published
- digital-shadow: 디지털 섀도 (Digital Shadow) · published
- digital-thread: 디지털 스레드 (Digital Thread) · published
- digital-twin-composition: 디지털 트윈 결합 (Digital Twin Composition) · published
- digital-twin: 디지털 트윈 (Digital Twin) · draft
- discrete-event-simulation: 이산 사건 시뮬레이션 (Discrete Event Simulation (DES)) · published
- dispenser-ingestor: 디스펜서·인제스터 (Dispenser / Ingestor) · published
- distributed-tracing: 분산 추적 (Distributed Tracing) · published
- drawing-exchange-format: 도면 교환 형식 (Drawing Exchange Format (DXF)) · published
- eclass: ECLASS (ECLASS) · published
- edit-cost: 편집 비용 (Edit Cost) · published
- enclave: 인클레이브 (Enclave (SROS 2)) · published
- epcis-error-declaration: 오류 선언 (Error Declaration (EPCIS errorDeclaration)) · published
- epcis: 전자 제품 코드 정보 서비스 (Electronic Product Code Information Services (EPCIS)) · draft
- event-driven-rescheduling: 사건 기반 재스케줄링 (Event-driven Rescheduling) · published
- excessive-agency: 과도한 에이전시 (Excessive Agency) · published
- expected-value-of-perfect-information: 완전 정보의 기대 가치 (Expected Value of Perfect Information (EVPI)) · published
- explicit-implicit-confirmation: 명시적 확인·암시적 확인 (Explicit / Implicit Confirmation) · published
- fan-out: 팬아웃 (Fan-out (human-robot team)) · published
- fault-detection-and-diagnosis-fdd: 고장 탐지·진단 (Fault Detection and Diagnosis (FDD)) · published
- fault-injection: 장애 주입 (Fault Injection) · published
- filter-mask: 필터 마스크 (Filter Mask (Nav2 costmap filter)) · published
- fleet-adapter: 플릿 어댑터 (Fleet Adapter) · draft
- fleet-control-level: 플릿 제어 수준 (Fleet Control Level (Open-RMF: Full Control / Traffic Light / Read Only)) · published
- fleet-management-system: 플릿 관리 시스템 (Fleet Management System (FMS)) · published
- fleet-sizing: 차량 소요대수 산정 (Fleet Sizing) · published
- floor-plan-recognition: 평면도 인식 (Floor Plan Recognition) · published
- fog-computing: 포그 컴퓨팅 (Fog Computing) · published
- frozen-horizon: 동결 구간 (Frozen Horizon (Frozen Zone)) · published
- giai: 글로벌 개별 자산 식별자 (Global Individual Asset Identifier (GIAI)) · published
- goal-condition: 목표 조건 (Goal Condition) · published
- grade-certainty-of-evidence: 근거 확실성 등급 (GRADE (Grading of Recommendations, Assessment, Development and Evaluation)) · published
- grai: 글로벌 반환형 자산 식별자 (Global Returnable Asset Identifier (GRAI)) · published
- graph-edit-distance: 그래프 편집 거리 (Graph Edit Distance (GED)) · published
- hallucination: 환각 (Hallucination) · published
- hddl: 계층 도메인 정의 언어 (Hierarchical Domain Definition Language (HDDL)) · published
- hierarchical-task-network: 계층적 작업 네트워크 (Hierarchical Task Network (HTN)) · published
- high-impact-ai: 고영향 인공지능 (High-impact AI (Korea AI Basic Act)) · published
- human-in-the-loop: 사람 참여 루프 (Human-in-the-Loop (HITL)) · published
- hungarian-method: 헝가리안 방법 (Hungarian Method) · published
- idempotency-key: 멱등성 키 (Idempotency Key) · published
- identity-report: 신원 보고 (Identity Report (MassRobotics identityReport)) · published
- iec-common-data-dictionary: IEC 공통 데이터 사전 (IEC Common Data Dictionary (IEC CDD)) · published
- ifc: 산업 기초 클래스 (Industry Foundation Classes (IFC)) · published
- indoor-mapping-data-format: 실내 지도 데이터 형식 (Indoor Mapping Data Format (IMDF)) · published
- indoor-space-subspacing: 공간 세분화 (Subspacing (Indoor Space Subdivision)) · published
- indoorgml: IndoorGML (IndoorGML) · published
- industrial-data: 산업데이터 (Industrial Data) · published
- information-delivery-specification: 정보 전달 명세 (Information Delivery Specification (IDS)) · published
- information-for-use: 사용 정보 (Information for Use (Instructions for Use)) · published
- intent-recognition: 의도 인식 (Intent Recognition (Intent Detection)) · published
- irdi: 국제 등록 데이터 식별자 (International Registration Data Identifier (IRDI)) · published
- irreducible-infeasible-subset: 기약 불능 제약 집합 (Irreducible Infeasible Subset (IIS)) · published
- isa-95: 기업–제어 시스템 통합 표준 (ISA-95 Enterprise-Control System Integration) · published
- job-shop-scheduling-problem: 작업장 스케줄링 문제 (Job Shop Scheduling Problem (JSSP)) · published
- joint-goal-accuracy: 결합 목표 정확도 (Joint Goal Accuracy (JGA)) · published
- json-schema: JSON 스키마 (JSON Schema) · published
- keystroke-level-model: 키 입력 수준 모델 (Keystroke-Level Model (KLM)) · published
- lane-closure: 차선 폐쇄 (Lane Closure) · published
- latent-failure: 잠재 실패 (Latent Failure) · published
- layout-interchange-format: 레이아웃 교환 형식 (Layout Interchange Format (LIF)) · published
- lifelong-mapf: 지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF)) · draft
- lift-adapter: 승강기 어댑터 (Lift Adapter) · published
- linear-temporal-logic: 선형 시간 논리 (Linear Temporal Logic (LTL)) · published
- littles-law: 리틀의 법칙 (Little's Law) · published
- llm-agent: LLM 에이전트 (LLM Agent) · published
- llm-modulo-framework: LLM-모듈로 프레임워크 (LLM-Modulo Framework) · published
- location-check-digit: 위치 체크 디지트 (Location Check Digit) · published
- managed-node: 관리형 노드 (Managed Node (ROS 2 Lifecycle Node)) · published
- map-alignment: 지도 정합 (Map Alignment) · published
- mapf: 다중 에이전트 경로 찾기 (Multi-Agent Path Finding (MAPF)) · draft
- market-based-task-allocation: 시장 기반 작업 배정 (Market-based Task Allocation) · published
- milp: 혼합 정수 계획 (Mixed Integer Linear Programming (MILP)) · published
- mobile-manipulator: 모바일 매니퓰레이터 (Mobile Manipulator) · published
- mobile-video-information-processing-device: 이동형 영상정보처리기기 (Mobile Video Information Processing Device) · published
- model-checking: 모델 검사 (Model Checking) · published
- model-context-protocol: 모델 컨텍스트 프로토콜 (Model Context Protocol (MCP)) · published
- model-registry: 모델 레지스트리 (Model Registry) · published
- mqtt: 메시지 큐잉 원격 측정 전송 (Message Queuing Telemetry Transport (MQTT)) · published
- mrta: 다중 로봇 작업 배정 (Multi-Robot Task Allocation (MRTA)) · draft
- multi-agent-pickup-and-delivery: 다중 에이전트 픽업·배송 (Multi-Agent Pickup and Delivery (MAPD)) · draft
- multi-fleet-orchestration: 다중 플릿 오케스트레이션 (Multi-Fleet Orchestration) · published
- nearest-vehicle-first-rule: 최근접 차량 우선 규칙 (Nearest Vehicle First (NVF) Rule) · published
- neuro-symbolic-ai: 신경-기호 AI (Neuro-symbolic AI) · published
- number-of-clicks: 클릭 수 지표 (Number of Clicks (NoC)) · published
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM)) · published
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL)) · published
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework)) · published
- operating-mode: 운용 모드 (Operating Mode (VDA 5050 operatingMode)) · published
- operating-zone: 운용 구역 (Operating Zone (ISO 3691-4)) · published
- optimality-gap: 최적성 간격 (Optimality Gap) · published
- order-batching: 주문 배치 (Order Batching) · published
- over-the-air-update: 무선 업데이트 (Over-the-Air Update (OTA)) · published
- overall-equipment-effectiveness: 종합설비효율 (Overall Equipment Effectiveness (OEE)) · published
- panoptic-quality: 파놉틱 품질 (Panoptic Quality (PQ)) · published
- panoptic-symbol-spotting: 파놉틱 심볼 스포팅 (Panoptic Symbol Spotting) · published
- pass-k: pass^k 지표 (pass^k) · published
- pddl: 계획 도메인 정의 언어 (Planning Domain Definition Language (PDDL)) · published
- perfect-order-fulfillment: 완전 주문 이행률 (Perfect Order Fulfillment) · published
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce) · published
- precedence-constraint: 선후 제약 (Precedence Constraint) · published
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT)) · published
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G)) · published
- process-mining: 프로세스 마이닝 (Process Mining) · published
- put-wall: 풋월 (Put Wall) · published
- raster-to-vector-conversion: 래스터–벡터 변환 (Raster-to-Vector Conversion) · published
- read-point: 판독 지점 (Read Point (EPCIS readPoint)) · published
- reality-gap: 현실 격차 (Reality Gap (Sim-to-Real Gap)) · published
- regression-testing: 회귀 시험 (Regression Testing) · published
- release-zone: 해제 구역 (Release Zone) · published
- required-and-provided-capability: 요구 능력·제공 능력 (Required Capability / Provided (Offered) Capability) · published
- resource-constrained-project-scheduling-problem: 자원 제약 프로젝트 스케줄링 문제 (Resource-Constrained Project Scheduling Problem (RCPSP)) · published
- risk-assessment: 위험성평가 (Risk Assessment (ISO 12100)) · published
- roadmap: 경로망 (Roadmap) · published
- robotic-mobile-fulfillment-system: 로봇 이동형 풀필먼트 시스템 (Robotic Mobile Fulfillment System (RMFS)) · published
- role-based-access-control: 역할 기반 접근 통제 (Role-Based Access Control (RBAC)) · published
- root-cause-analysis-rca: 근본 원인 분석 (Root Cause Analysis (RCA)) · published
- runtime-verification: 런타임 검증 (Runtime Verification) · published
- safe-interval-path-planning: 안전 구간 경로 계획 (Safe Interval Path Planning (SIPP)) · published
- saga: 사가 (Saga) · published
- scan-vs-bim: 스캔 대 BIM 비교 (Scan-vs-BIM) · published
- schedule-stability: 일정 안정성 (Schedule Stability) · published
- scor: 공급망 운영 참조 모델 (Supply Chain Operations Reference (SCOR)) · draft
- semantic-id: 의미 식별자 (Semantic ID (semanticId)) · published
- semantic-versioning: 의미적 버전 관리 (Semantic Versioning (SemVer)) · published
- semi-open-queueing-network: 반개방형 대기행렬 네트워크 (Semi-Open Queueing Network (SOQN)) · published
- semi-static-object: 반정적 객체 (Semi-static Object) · published
- service-level-agreement: 서비스 수준 협약 (Service Level Agreement (SLA)) · published
- shacl: 형상 제약 언어 (Shapes Constraint Language (SHACL)) · published
- shifting-bottleneck-detection-active-period-method: 이동 병목 탐지 (Shifting Bottleneck Detection (Active Period Method)) · published
- signal-temporal-logic: 신호 시간 논리 (Signal Temporal Logic (STL)) · published
- similarity-transformation: 유사 변환 (Similarity Transformation) · published
- situation-awareness-based-agent-transparency: 상황 인식 기반 에이전트 투명성 (Situation Awareness-based Agent Transparency (SAT)) · published
- skill: 스킬 (Skill) · published
- slot-filling: 슬롯 채우기 (Slot Filling) · published
- software-nameplate: 소프트웨어 명판 (Software Nameplate (IDTA 02007)) · published
- space-graph: 공간 그래프 (Space Graph) · published
- sscc: 물류 단위 일련 코드 (Serial Shipping Container Code (SSCC)) · published
- state-of-charge: 충전 상태 (State of Charge (SOC)) · published
- state-of-health: 배터리 건강 상태 (State of Health (SOH)) · published
- stpa: 시스템 이론적 프로세스 분석 (System-Theoretic Process Analysis (STPA)) · published
- structured-output: 구조화 출력 (Structured Output) · published
- success-weighted-by-path-length: 경로 길이 가중 성공률 (Success weighted by Path Length (SPL)) · published
- task-decomposition: 작업 분해 (Task Decomposition) · published
- technology-readiness-level: 기술 성숙도 (Technology Readiness Level (TRL)) · published
- time-window: 시간창 (Time Window) · published
- topological-map: 위상 지도 (Topological Map) · published
- traversability: 통과 가능성 (Traversability) · published
- user-simulator: 사용자 시뮬레이터 (User Simulator) · published
- vda-5050-cancel-order: 주문 취소 즉시 동작 (cancelOrder (VDA 5050 instant action)) · published
- vda-5050-factsheet: VDA 5050 팩트시트 (VDA 5050 factsheet) · published
- vda-5050: VDA 5050 (VDA 5050) · published
- verification-and-validation-of-simulation-models: 시뮬레이션 모델 검증·타당성 확인 (Verification and Validation (V&V) of Simulation Models) · published
- virtual-commissioning: 가상 시운전 (Virtual Commissioning) · published
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking)) · published
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release) · published
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System) · draft
- workflow-net: 워크플로 넷 (Workflow Net (WF-net)) · published
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet)) · published
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443)) · published
```

### docs/open-questions.md

```markdown
---
title: "열린 질문"
type: questions
status: published
created: 2026-09-24
updated: 2026-09-24
version: 1
---

[홈](index.md) › 열린 질문

# 열린 질문

아직 해결되지 않은 질문의 목록이다. 질문마다 관련 영역, 제기일, 제기한 실행, 상태(열림 / 조사 중 / 해결 / 보류), 해결 시 링크를 둔다. 세 에이전트 모두 질문을 제기할 수 있고, 해결 판정은 내용 검증 에이전트가 한다. 서로 다른 출처가 충돌하면 한쪽을 고르지 않고 둘 다 제시한 뒤 여기에 올린다. 새 세부영역이 필요해 보이면 분류를 바꾸지 않고 "분류 확장 제안"으로 여기에 기록한다.

중점 연구 트랙 전용 질문은 트랙의 질문 백로그에 두고, 여기에는 링크만 둔다. 이 표는 `data/open_questions.json` 에서 자동으로 만든다.

## 목록

<!-- auto:open-questions:start -->
| id | 질문 | 관련 영역 | 제기일 | 제기한 실행 | 상태 | 해결 시 링크 |
|---|---|---|---|---|---|---|
| oq-001 | 로봇의 적재·하역 완료 신호(VDA 5050 drop 동작 완료, Open-RMF IngestorResult)를 EPCIS 인계 이벤트로 옮기는 표준 매핑이나 공개 구현 사례가 있는가? | [7. 화물·재고·자산 식별과 추적](categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md)<br>[17. 로봇 간 협업·물리적 인계](categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md)<br>[9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | 2026-09-25 | 2026-09-25-01 | 열림 | — |
| oq-002 | 국내 물류센터에서 SSCC 라벨이나 EPCIS 이벤트를 로봇 작업 결과(적재·하역 완료)와 연결해 운영하는 사례가 있는가? | [7. 화물·재고·자산 식별과 추적](categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md)<br>[1. 주문·업무 시스템 연계](categories/a-business-supply-chain-design/01-order-and-business-system-integration.md) | 2026-09-25 | 2026-09-25-01 | 열림 | — |
| oq-003 | 로봇·게이트의 바코드·RFID 판독 실패나 오판독이 생기면 인계 확정을 보류·재스캔·사람 확인 중 어떤 기준으로 처리해야 하는가? | [7. 화물·재고·자산 식별과 추적](categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md)<br>[20. 예외 복구·재계획·업무 연속성](categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) | 2026-09-25 | 2026-09-25-01 | 열림 | — |
| oq-004 | IEEE 1872 계열 로봇 온톨로지 표준이나 AAS 능력 서브모델을 KS로 부합화했거나 국내 로봇 관제 사업에 적용한 사례가 있는가? | [28. 표준·상호운용성·다사업자 거버넌스](categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)<br>[5. 로봇 능력·작업 온톨로지](categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) | 2026-09-25 | 2026-09-25-02 | 열림 | — |
| oq-005 | 출처 충돌: VDA 5050 3.0.0의 정확한 발행일은 언제인가? 검색 요약은 3.0 발행을 2026-03-19, 보도자료를 2026-04-20로 전하지만 보도자료 URL은 2026-04-21 계열이다. | [9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | 2026-09-25 | 2026-09-25-02 | 열림 | — |
| oq-006 | CBV의 loading·unloading이 운송 수단 적재로 정의되어 있을 때 시설 안 로봇의 적재·운반·하역은 어떤 업무 단계(bizStep) 값이나 사용자 정의 어휘로 기록해야 하는가? | [7. 화물·재고·자산 식별과 추적](categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md)<br>[17. 로봇 간 협업·물리적 인계](categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md) | 2026-09-25 | 2026-09-25-03 | 열림 | — |
| oq-007 | VDA 5050 3.0.0에서 관제가 loadId를 정할 때 SSCC 같은 GS1 키를 그대로 쓰도록 권고하거나 제약하는 규정이 있는가, 로봇이 판독한 식별자와 다르면 어떻게 보고하는가? | [7. 화물·재고·자산 식별과 추적](categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md)<br>[9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | 2026-09-25 | 2026-09-25-03 | 열림 | — |
| oq-008 | 여러 거점 사이에서 로봇을 재배치·공유하거나 성수기에 임대로 보충하는 결정을 다룬 학술·공공 자료나 국내 사례가 있는가? | [3. 처리능력·거점·설비 계획](categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md)<br>[4. 성과·경제성·프로세스 개선](categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) | 2026-09-25 | 2026-09-25-10 | 열림 | — |
| oq-009 | 교대조별 작업자 수와 로봇·작업대 수를 함께 정하는 처리능력 계획 모델이나 사례가 있는가? | [3. 처리능력·거점·설비 계획](categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md)<br>[18. 사람–로봇 협업·운영 인터페이스](categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) | 2026-09-25 | 2026-09-25-10 | 열림 | — |
| oq-010 | 국내 다층 물류센터에서 화물용 승강기나 층간 반송 설비가 로봇 처리량의 병목이 된다는 정량 자료가 있는가, 병원·호텔 사례의 승강기 혼잡 결과를 물류센터에 옮길 수 있는가? | [3. 처리능력·거점·설비 계획](categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md)<br>[10. 설비·건물 시스템 연동](categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md) | 2026-09-25 | 2026-09-25-10 | 열림 | — |
| oq-011 | 스마트물류센터 인증의 세부 평가 지표에 로봇 대수·가동률·처리능력 같은 설비 계획 지표가 포함되는가? | [3. 처리능력·거점·설비 계획](categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md)<br>[4. 성과·경제성·프로세스 개선](categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) | 2026-09-25 | 2026-09-25-10 | 열림 | — |
| oq-012 | 국내 물류센터는 로봇의 운반 완료와 WMS의 입고·인수 확정을 별도 단계로 두는가, 그렇다면 두 단계를 잇는 식별 키와 확정 대기 시간 기준은 무엇인가? | [2. 공정·워크플로 모델링](categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[1. 주문·업무 시스템 연계](categories/a-business-supply-chain-design/01-order-and-business-system-integration.md) | 2026-09-25 | 2026-09-25-09 | 열림 | — |
| oq-013 | ISA-95 세그먼트 의존 유형(B2MML DependencyType)을 입고·적치·피킹·출하 같은 창고 물류 작업의 선후관계 표현에 적용한 사례나 확장이 있는가? | [2. 공정·워크플로 모델링](categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[14. 작업 순서·스케줄링](categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md) | 2026-09-25 | 2026-09-25-09 | 열림 | — |
| oq-014 | 업무 프로세스 모델(BPMN 등)의 단계 상태와 로봇 작업 상태(Open-RMF 작업 상태, VDA 5050 동작 상태)를 동기화하는 표준 매핑이나 공개 구현이 있는가? | [2. 공정·워크플로 모델링](categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md)<br>[9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[12. 명령·작업 실행의 신뢰성](categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md) | 2026-09-25 | 2026-09-25-09 | 열림 | — |
| oq-015 | 로봇 상태 기록(작업 중·유휴·충전·오류)과 WMS·ERP의 주문 이행 지표(완전 주문 이행률, 주문 이행 사이클 타임)를 같은 기간·같은 주문 단위로 연결해 로봇 도입이 출하량·비용 개선으로 이어졌는지 검증한 공개 사례가 있는가? | [4. 성과·경제성·프로세스 개선](categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md)<br>[1. 주문·업무 시스템 연계](categories/a-business-supply-chain-design/01-order-and-business-system-integration.md) | 2026-09-25 | 2026-09-25-14 | 열림 | — |
| oq-016 | 창고 이동로봇 플릿에 ISO 22400식 OEE(가용성·성능·품질)를 적용하는 합의된 정의가 있는가, 충전·대기·교통 정체 시간은 어느 손실로 분류해야 하는가? | [4. 성과·경제성·프로세스 개선](categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md)<br>[16. 공용 자원·충전·에너지 최적화](categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) | 2026-09-25 | 2026-09-25-14 | 열림 | — |
| oq-017 | 벤더 발표가 아닌 공공·학술 자료로 국내 물류 로봇 도입의 투자 효과(생산성·비용·회수 기간)를 측정한 결과가 있는가? | [4. 성과·경제성·프로세스 개선](categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md)<br>[3. 처리능력·거점·설비 계획](categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md) | 2026-09-25 | 2026-09-25-14 | 열림 | — |
| oq-018 | 이동로봇·작업대·승강기가 섞인 창고 흐름에 활성 구간 기반 이동 병목 탐지나 객체 중심 프로세스 마이닝을 적용한 연구가 있는가? | [4. 성과·경제성·프로세스 개선](categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md)<br>[19. 모니터링·이상 탐지·원인 분석](categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md) | 2026-09-25 | 2026-09-25-14 | 열림 | — |
| oq-019 | 상위 시스템의 출고 우선순위(납기·운송 마감)를 Open-RMF 우선순위 스키마나 ROP 작업 대기열 규칙으로 옮겨 진행 중 작업을 재정렬하는 공개 설계나 사례가 있는가? | [1. 주문·업무 시스템 연계](categories/a-business-supply-chain-design/01-order-and-business-system-integration.md)<br>[14. 작업 순서·스케줄링](categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md) | 2026-09-25 | 2026-09-25-13 | 열림 | — |
| oq-020 | ISA-95 작업 지시·작업 응답(B2MML, OPC UA for ISA-95 Job Control)을 VDA 5050 주문·상태나 Open-RMF 작업 요청·상태로 옮기는 표준 매핑이나 공개 구현이 있는가? | [1. 주문·업무 시스템 연계](categories/a-business-supply-chain-design/01-order-and-business-system-integration.md)<br>[9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | 2026-09-25 | 2026-09-25-13 | 열림 | — |
| oq-021 | 로봇이 이미 화물을 싣거나 옮긴 뒤 상위 시스템이 주문을 취소·변경하면 되돌림 작업과 재고 반영을 누가 어떤 규칙으로 정하는가(국내 물류센터 사례 포함)? | [1. 주문·업무 시스템 연계](categories/a-business-supply-chain-design/01-order-and-business-system-integration.md)<br>[20. 예외 복구·재계획·업무 연속성](categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) | 2026-09-25 | 2026-09-25-13 | 열림 | — |
| oq-022 | 국내 물류센터에서 설계 도면(CAD·BIM)을 로봇 지도 작성이나 시운전에 실제로 활용한 사례가 있는가, 있다면 도면–현장 차이를 어떻게 확인했는가? | [6. 지도·공간·위치 모델](categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[21. 온보딩·설정·현장 시운전](categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) | 2026-09-25 | 2026-09-25-11 | 열림 | — |
| oq-023 | VDA 5050 팩트시트의 loadType 과 MassRobotics 의 cargoType 이 자유 문자열일 때 팔레트·용기 같은 적재물 유형을 제조사 사이에 같은 의미로 맞출 공통 어휘나 코드 체계가 있는가? | [5. 로봇 능력·작업 온톨로지](categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[7. 화물·재고·자산 식별과 추적](categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) | 2026-09-25 | 2026-09-25-15 | 열림 | — |
| oq-024 | 제조사가 문서로 선언한 능력(팩트시트·매뉴얼)과 현장에서 관측한 운용 능력(적재 후 속도, 배터리 저하 등)이 다를 때 작업 배정은 어느 값을 기준으로 삼고 능력 모델을 어떻게 갱신하는가? | [5. 로봇 능력·작업 온톨로지](categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[8. 실시간 세계 상태·데이터 일관성](categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md)<br>[13. 작업 배정 — MRTA](categories/d-planning-and-optimization/13-task-allocation-mrta.md) | 2026-09-25 | 2026-09-25-15 | 열림 | — |
| oq-025 | 출처 충돌: VDMA LIF 의 판과 발행일은 무엇인가(VDA 5050 3.0.0 은 VDMA 2024-03 으로 인용하고, LIF 공식 저장소 README 는 1.0.0 판을 2023-09 로 적는다)? | [28. 표준·상호운용성·다사업자 거버넌스](categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)<br>[6. 지도·공간·위치 모델](categories/b-common-information-and-environment-model/06-map-space-and-location-model.md) | 2026-09-25 | 2026-09-25-19 | 열림 | — |
| oq-026 | KS B 7321-2(서비스 로봇 모듈용 정보 모델 — 소프트웨어 모듈)가 ISO 22166-202와 부합화된 표준인지, 국내 물류 로봇·관제 사업에 적용한 사례가 있는가? (IEEE 1872 계열·AAS 능력 서브모델의 KS 부합화를 묻는 oq-004와 연결된다) | [28. 표준·상호운용성·다사업자 거버넌스](categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)<br>[5. 로봇 능력·작업 온톨로지](categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) | 2026-09-25 | 2026-09-25-16 | 열림 | — |
| oq-027 | ISO 21423 의 공통 좌표계(CCS)는 발행판에서 어떻게 정의되며, VDA 5050 mapId·Open-RMF 지도·층 이름·MassRobotics planarDatum 과 어떻게 대응하는가? | [6. 지도·공간·위치 모델](categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | 2026-09-25 | 2026-09-25-17 | 열림 | — |
| oq-028 | 제조사마다 계산 방식이 다른 위치추정 신뢰도(VDA 5050 localizationScore 등)나 신뢰도 필드가 없는 로봇의 위치 보고를 ROP 가 같은 기준으로 수용·거부하는 방법이 있는가? | [6. 지도·공간·위치 모델](categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[8. 실시간 세계 상태·데이터 일관성](categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md) | 2026-09-25 | 2026-09-25-17 | 열림 | — |
| oq-029 | 국내 물류센터에서 GLN 하위 위치나 WMS 로케이션 코드를 로봇 지도 위 경유점·스테이션과 대응시켜 목적지로 쓰는 사례가 있는가? | [6. 지도·공간·위치 모델](categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[7. 화물·재고·자산 식별과 추적](categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) | 2026-09-25 | 2026-09-25-17 | 열림 | — |
| oq-030 | 출처 충돌: LTAA(arXiv 2512.02810) 초록 요약은 로봇 전문화가 강한 설정에서 LLM 배정이 작업 완료율 77%로 전통 기법을 모두 앞섰다고 하지만, 다른 2차 요약은 동적 계획법의 완료율이 더 높다고 적는다. 어느 쪽이 원문 결과인가? | [13. 작업 배정 — MRTA](categories/d-planning-and-optimization/13-task-allocation-mrta.md)<br>[27. AI·학습·적응과 모델 운영](categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) | 2026-09-25 | 2026-09-25-21 | 열림 | — |
| oq-031 | 국내 물류센터에서 로봇을 직접 제어하는 방식과 제조사 관제에 작업을 넘기는 방식 가운데 어느 쪽이 쓰이는지, 선택 기준이나 처리량·연동 비용을 비교한 공개 자료가 있는가? | [9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[3. 처리능력·거점·설비 계획](categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md) | 2026-09-25 | 2026-09-25-20 | 열림 | — |
| oq-032 | 제조사 관제가 일시정지·재개나 상태 보고만 허용할 때 공용 통로·승강기·문에서 다른 플릿과의 교착을 어떻게 막는가, 제어 수준에 따른 교통 성능 차이를 측정한 연구가 있는가? | [9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[15. 다중 로봇 경로·교통 관리 — MAPF](categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md) | 2026-09-25 | 2026-09-25-20 | 열림 | — |
| oq-033 | Open-RMF 로봇 상태, VDA 5050 action 상태·오류, MassRobotics 운용 상태를 하나의 공통 상태·오류 어휘로 옮기는 표준 매핑이나 공개 구현이 있는가? | [9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[12. 명령·작업 실행의 신뢰성](categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md)<br>[19. 모니터링·이상 탐지·원인 분석](categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md) | 2026-09-25 | 2026-09-25-20 | 열림 | — |
| oq-034 | 문·승강기·충전기 같은 설비 상태 정보를 몇 초까지 믿고 통과·배정을 확정할지 정한 표준이나 국내 현장 기준이 있는가, 없으면 대상별 허용 경과 시간을 어떤 근거로 정할 것인가? | [8. 실시간 세계 상태·데이터 일관성](categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md)<br>[10. 설비·건물 시스템 연동](categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md) | 2026-09-25 | 2026-09-25-24 | 열림 | — |
| oq-035 | 상태 보고 주기와 시각 체계가 다른 로봇(VDA 5050 최소 30초 주기의 ISO 8601 시각, Open-RMF 밀리초 시각)이 섞일 때 공통 세계 상태의 시각 동기화 방식과 허용 시계 오차를 규정한 자료나 사례가 있는가? | [8. 실시간 세계 상태·데이터 일관성](categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md)<br>[9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[11. 분산 시스템·통신·컴퓨팅 구조](categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md) | 2026-09-25 | 2026-09-25-24 | 열림 | — |
| oq-036 | 로봇이 보고한 적재물 식별·판독 결과와 WMS 재고 기록이 어긋날 때 어느 쪽을 기준으로 삼고 정정 기록을 누가 발행하는가(국내 물류센터 사례 포함)? | [8. 실시간 세계 상태·데이터 일관성](categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md)<br>[7. 화물·재고·자산 식별과 추적](categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) | 2026-09-25 | 2026-09-25-24 | 열림 | — |
| oq-037 | 출처 충돌: 김지형(2023) 'OPC UA를 활용한 이기종 로봇의 실시간 디지털 트윈 설계 및 구현'의 게재 학술지를 한 검색 요약은 지능정보논문지로, KoreaScience 는 한국인터넷방송통신학회논문지(DOI 10.7236/JIIBC.2023.23.4.189)로 적는다. 어느 쪽이 맞는가? | [8. 실시간 세계 상태·데이터 일관성](categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md) | 2026-09-25 | 2026-09-25-24 | 열림 | — |
| oq-038 | 외부망이 끊겨 클라우드 WMS 와 단절된 동안 현장 ROP 가 이미 받은 주문·작업을 어디까지 계속 실행하고, 재연결 뒤 재고·완료 기록을 어떻게 맞추는지 정한 국내 물류센터 운영 기준이나 사례가 있는가? | [11. 분산 시스템·통신·컴퓨팅 구조](categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md)<br>[1. 주문·업무 시스템 연계](categories/a-business-supply-chain-design/01-order-and-business-system-integration.md)<br>[20. 예외 복구·재계획·업무 연속성](categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) | 2026-09-25 | 2026-09-25-27 | 열림 | — |
| oq-039 | 물류센터 로봇 관제 통신(와이파이·5G 특화망)에서 명령·상태 메시지의 허용 지연·손실률·로밍 중단 시간을 정한 표준이나 공개 측정 자료가 있는가? | [11. 분산 시스템·통신·컴퓨팅 구조](categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md)<br>[9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | 2026-09-25 | 2026-09-25-27 | 열림 | — |
| oq-040 | 여러 거점의 로봇 운영을 한곳에서 관리할 때 거점별 현장 서버와 중앙 클라우드 사이 역할 분담과 데이터 동기화를 공개한 오픈소스 구성이나 사례가 있는가? | [11. 분산 시스템·통신·컴퓨팅 구조](categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md)<br>[3. 처리능력·거점·설비 계획](categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md) | 2026-09-25 | 2026-09-25-27 | 열림 | — |
| oq-041 | 대한승강기협회 '엘리베이터와 로봇의 상호 연동을 위한 가이드라인' 단체표준은 어떤 메시지·상태(호출·탑승·하차·세션 해제 등)를 정하며, Open-RMF 승강기 요청·상태 메시지와 어떻게 대응하는가? | [10. 설비·건물 시스템 연동](categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | 2026-09-25 | 2026-09-25-25 | 열림 | — |
| oq-042 | 컨베이어·작업대와 이동로봇 사이 적재물 인계 신호(준비·허가·이송·완료)를 제조사 중립으로 정한 공개 표준이나 규격이 있는가? | [10. 설비·건물 시스템 연동](categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md)<br>[17. 로봇 간 협업·물리적 인계](categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md) | 2026-09-25 | 2026-09-25-25 | 열림 | — |
| oq-043 | 로봇 관제가 출입통제·건물 자동화 시스템(BACnet 등)을 통해 보안문을 여닫는 공개 설계나 국내 사례가 있고, 권한 확인은 누가 하는가? | [10. 설비·건물 시스템 연동](categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md)<br>[26. 사이버보안·접근권한·개인정보](categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md) | 2026-09-25 | 2026-09-25-25 | 열림 | — |
| oq-044 | 국내에서 ISO 19164 나 IndoorGML 2.0 을 KS 로 부합화했거나, CityGML 2.0 과 IndoorGML 공간 개념을 원칙으로 둔 실내공간정보 구축 작업규정을 새 판 표준에 맞춰 개정한 사례가 있는가? | [6. 지도·공간·위치 모델](categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | 2026-09-25 | 2026-09-25-28 | 열림 | — |
| oq-045 | 로봇 지도의 층(level) 이름과 승강기 상태의 층 이름(Open-RMF available_floors 등)을 서로 대응시키는 규칙을 정한 표준이나 공개 구현이 있는가? | [6. 지도·공간·위치 모델](categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[10. 설비·건물 시스템 연동](categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md) | 2026-09-25 | 2026-09-25-32 | 열림 | — |
| oq-046 | 상위 시스템 요청의 중복을 판별하는 키(멱등성 키나 상위 요청 id)를 ROP 가 얼마 동안 보존해야 하는가, 운반 작업의 재전송 가능 기간에 맞춘 만료 기준을 정한 표준이나 사례가 있는가? | [12. 명령·작업 실행의 신뢰성](categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md)<br>[1. 주문·업무 시스템 연계](categories/a-business-supply-chain-design/01-order-and-business-system-integration.md) | 2026-09-25 | 2026-09-25-31 | 열림 | — |
| oq-047 | VDA 5050 로봇이 재부팅되면 받아 둔 주문을 유지하는지에 대한 규정이 명세에서 확인되지 않는데, 제조사 구현이나 공개 사례는 재부팅 뒤 주문·동작 상태를 어떻게 복원하거나 폐기하는가? | [12. 명령·작업 실행의 신뢰성](categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md)<br>[9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | 2026-09-25 | 2026-09-25-31 | 열림 | — |
| oq-048 | Open-RMF 플릿 어댑터 재시작 시 작업 유실을 막는 작업 백업·복원 기능(SQLite 저장 제안)이 현재 배포판에 반영되었는가, 반영되었다면 복원 뒤 로봇의 실제 위치·적재 상태와 어떻게 대조하는가? | [12. 명령·작업 실행의 신뢰성](categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md)<br>[20. 예외 복구·재계획·업무 연속성](categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) | 2026-09-25 | 2026-09-25-31 | 열림 | — |
| oq-049 | 제조사가 다른 로봇 플릿 사이의 작업 선후(예: 피킹 로봇 완료 뒤 운반 로봇 출발)를 작업 요청 수준에서 표현·집행하는 표준 필드나 공개 구현이 있는가? | [14. 작업 순서·스케줄링](categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md)<br>[13. 작업 배정 — MRTA](categories/d-planning-and-optimization/13-task-allocation-mrta.md)<br>[9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | 2026-09-25 | 2026-09-25-34 | 열림 | — |
| oq-050 | 로봇 작업대의 주문·랙 순서 최적화 연구가 보고한 로봇 대수·랙 방문 절감 효과를 이종 로봇과 사람 포장대가 섞인 국내 물류센터에서 검증한 자료가 있는가? | [14. 작업 순서·스케줄링](categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md)<br>[3. 처리능력·거점·설비 계획](categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md) | 2026-09-25 | 2026-09-25-34 | 열림 | — |
| oq-051 | 피킹–포장 동기화의 성과를 포장 작업자 대기시간이나 주문 완료 시간 분산 같은 지표로 재는 합의된 정의가 있는가, ROP 가 순서 결정의 목적함수로 쓸 수 있는가? | [14. 작업 순서·스케줄링](categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md)<br>[4. 성과·경제성·프로세스 개선](categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) | 2026-09-25 | 2026-09-25-34 | 열림 | — |
| oq-052 | 국내외 물류센터에서 최근접 배정 규칙과 전역 최적화(또는 LLM 기반) 배정을 같은 조건에서 비교해 총 이동거리·처리량·납기 준수를 실측한 자료가 있는가? | [13. 작업 배정 — MRTA](categories/d-planning-and-optimization/13-task-allocation-mrta.md)<br>[4. 성과·경제성·프로세스 개선](categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) | 2026-09-25 | 2026-09-25-33 | 열림 | — |
| oq-053 | ROP 가 플릿 단위로 작업을 입찰·배정하고 제조사 관제가 플릿 안에서 다시 로봇을 고르는 두 수준 배정에서 전체 최적성이 얼마나 손실되며, 이를 줄이려면 제조사 관제가 어떤 비용·상태 정보를 내야 하는가? (관련 기존 질문: oq-031) | [13. 작업 배정 — MRTA](categories/d-planning-and-optimization/13-task-allocation-mrta.md)<br>[9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | 2026-09-25 | 2026-09-25-33 | 열림 | — |
| oq-054 | 출하 마감·납기 같은 상위 업무 제약을 배정 목적함수(완료 시각 최소화, 비용 최소화)와 어떻게 결합하는지 정한 공개 설계나 창고 사례가 있는가? (관련 기존 질문: oq-019) | [13. 작업 배정 — MRTA](categories/d-planning-and-optimization/13-task-allocation-mrta.md)<br>[14. 작업 순서·스케줄링](categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md)<br>[1. 주문·업무 시스템 연계](categories/a-business-supply-chain-design/01-order-and-business-system-integration.md) | 2026-09-25 | 2026-09-25-33 | 열림 | — |
| oq-055 | VDA 5050 에 공식 적합성 시험·인증 절차가 있는가, 없다면 제3자 오픈소스 적합성 시험 도구의 결과를 새 로봇 연동 승인 기준으로 쓸 수 있는가? | [9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[23. 시험·형식 검증·벤치마크](categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | 2026-09-25 | 2026-09-25-38 | 열림 | — |
| oq-056 | 로봇 관제·플릿 어댑터·승강기·문 어댑터에 SROS 2 인클레이브와 권한 파일을 어떤 단위로 나눠 설비 명령 권한을 제한하는지 공개한 구성이나 사례가 있는가? | [10. 설비·건물 시스템 연동](categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md)<br>[26. 사이버보안·접근권한·개인정보](categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md) | 2026-09-25 | 2026-09-25-38 | 열림 | — |
| oq-057 | VDA 5050 3.0.0 의 해제 구역·협조 재계획 구역과 Open-RMF 교통 스케줄·협상을 한 현장에서 함께 쓰는 공개 설계나 구현이 있는가? | [15. 다중 로봇 경로·교통 관리 — MAPF](categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md)<br>[9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | 2026-09-25 | 2026-09-25-39 | 열림 | — |
| oq-058 | 격자·단위 시간 가정의 MAPF 벤치마크 성과(대회 결과 포함)가 실제 물류센터 로봇의 처리량으로 얼마나 이어지는지 측정한 공개 자료나 국내 사례가 있는가? | [15. 다중 로봇 경로·교통 관리 — MAPF](categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md)<br>[23. 시험·형식 검증·벤치마크](categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) | 2026-09-25 | 2026-09-25-39 | 열림 | — |
| oq-059 | 주문 납기·출하 마감 같은 업무 우선순위를 교통 협상·통로 양보의 우선권으로 옮기는 규칙을 정한 연구나 현장 기준이 있는가? | [15. 다중 로봇 경로·교통 관리 — MAPF](categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md)<br>[14. 작업 순서·스케줄링](categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md) | 2026-09-25 | 2026-09-25-39 | 열림 | — |
| oq-060 | 출처 충돌: IDTA 02047 1.0 에 충전 관련 요소(ChargingTimeAsSpecified, ChargingDeviceRequirements, BatteryInformation)가 있는가? 명세 PDF 검색 요약은 있다고 전하지만, 공식 저장소 템플릿 JSON 의 잘린 열람 응답에서는 확인되지 않았다. | [5. 로봇 능력·작업 온톨로지](categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)<br>[16. 공용 자원·충전·에너지 최적화](categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md) | 2026-09-25 | 2026-09-25-45 | 열림 | — |
| oq-061 | 로봇팔·워크셀의 인수 결과와 이동로봇의 적재 상태 보고가 어긋날 때(한쪽은 성공, 다른 쪽은 적재 유지) 어느 신호를 기준으로 인계 완료를 판정하는지 정한 표준이나 현장 사례가 있는가? | [17. 로봇 간 협업·물리적 인계](categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md)<br>[8. 실시간 세계 상태·데이터 일관성](categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md) | 2026-09-25 | 2026-09-25-42 | 열림 | — |
| oq-062 | 반도체 업종의 SEMI E84 같은 단계별 인계 신호를 물류센터의 이동로봇–컨베이어·작업대 인계에 적용하거나 옮긴 사례가 있는가? | [17. 로봇 간 협업·물리적 인계](categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md)<br>[10. 설비·건물 시스템 연동](categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md) | 2026-09-25 | 2026-09-25-42 | 열림 | — |
| oq-063 | ASTM F3499·NIST RMMA 같은 도킹·위치 정밀도 시험 결과를 로봇팔 파지 허용 오차와 연결해 인계 가능 여부를 정하는 기준이 있는가? | [17. 로봇 간 협업·물리적 인계](categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md)<br>[23. 시험·형식 검증·벤치마크](categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) | 2026-09-25 | 2026-09-25-42 | 열림 | — |
| oq-064 | 국내에 ANSI/A3 R15.08-2 의 유형 C(모바일 매니퓰레이터) 통합 안전 요구에 대응하는 KS 표준이나 인증 기준이 있는가? | [17. 로봇 간 협업·물리적 인계](categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md)<br>[25. 안전·위험 관리](categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md) | 2026-09-25 | 2026-09-25-42 | 열림 | — |
| oq-065 | 제조사가 다른 이동로봇이 같은 충전기를 함께 쓸 수 있게 하는 충전 커넥터·충전 통신의 공통 규격이나 공개 사례가 있는가? | [16. 공용 자원·충전·에너지 최적화](categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | 2026-09-25 | 2026-09-25-40 | 열림 | — |
| oq-066 | 물류센터 로봇의 충전 시점을 시간대별 전기 요금이나 최대 수요 전력 기준으로 계획한 연구나 국내 사례가 있는가? | [16. 공용 자원·충전·에너지 최적화](categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md)<br>[4. 성과·경제성·프로세스 개선](categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) | 2026-09-25 | 2026-09-25-40 | 열림 | — |
| oq-067 | 여러 제조사 플릿이 한 승강기를 함께 쓸 때 세션 순서·최대 점유 시간·목적층 묶음을 정하는 배분 규칙을 공개한 표준이나 구현이 있는가? | [16. 공용 자원·충전·에너지 최적화](categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md)<br>[10. 설비·건물 시스템 연동](categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md) | 2026-09-25 | 2026-09-25-40 | 열림 | — |
| oq-068 | 충전 하한을 제조사가 팩트시트로 선언한 값(criticalLowChargingLevel)과 ROP 운영 설정(recharge_threshold) 가운데 어느 것으로 삼고, 둘이 다르면 어떻게 조정하는가? | [16. 공용 자원·충전·에너지 최적화](categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md)<br>[5. 로봇 능력·작업 온톨로지](categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) | 2026-09-25 | 2026-09-25-40 | 열림 | — |
| oq-069 | 출처 충돌: Open-RMF 문서는 충전소 지정을 is_parking_spot(지원 작업 문서)과 is_charger(교통 편집기 문서·데모 README) 가운데 어느 속성으로 하는가? | [16. 공용 자원·충전·에너지 최적화](categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md)<br>[6. 지도·공간·위치 모델](categories/b-common-information-and-environment-model/06-map-space-and-location-model.md) | 2026-09-25 | 2026-09-25-40 | 열림 | — |
| oq-070 | 2024-11 제정된 이동식 협동로봇 안전기준 KS 의 표준 번호와 내용은 무엇이며, ISO 10218-2:2025·ISO 3691-4:2023 과 어떻게 대응하는가? | [18. 사람–로봇 협업·운영 인터페이스](categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md)<br>[25. 안전·위험 관리](categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md) | 2026-09-25 | 2026-09-25-46 | 열림 | — |
| oq-071 | 국내 물류센터에서 사람 피커와 운반 로봇이 서로 기다리는 시간(피커 유휴·로봇 대기)을 실측해 공개한 자료가 있는가? | [18. 사람–로봇 협업·운영 인터페이스](categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md)<br>[4. 성과·경제성·프로세스 개선](categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) | 2026-09-25 | 2026-09-25-46 | 열림 | — |
| oq-072 | 물류센터 관제 요원 한 명이 감독할 수 있는 이동로봇 수를 팬아웃이나 인지 부하 기준으로 측정한 연구나 현장 기준이 있는가? | [18. 사람–로봇 협업·운영 인터페이스](categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md)<br>[19. 모니터링·이상 탐지·원인 분석](categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md) | 2026-09-25 | 2026-09-25-46 | 열림 | — |
| oq-073 | VDA 5050 3.0.0 판의 네 단계 오류 수준(WARNING·URGENT·CRITICAL·FATAL)과 이전 판(2.x)의 오류 수준이 다를 때, 두 판이 섞인 이종 플릿에서 오류 수준을 어떻게 맞춰 해석하는가? | [19. 모니터링·이상 탐지·원인 분석](categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md)<br>[9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | 2026-09-25 | 2026-09-25-48 | 열림 | — |
| oq-074 | 물류 로봇 작업 지연을 로봇·설비·통신·공정 원인으로 나누는 공개 원인 분류 체계나 현장 데이터셋이 있는가? | [19. 모니터링·이상 탐지·원인 분석](categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md)<br>[4. 성과·경제성·프로세스 개선](categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) | 2026-09-25 | 2026-09-25-48 | 열림 | — |
| oq-075 | 국내 물류센터에서 로봇 정지·지연의 원인별 발생 비율이나 이상 대응 시간을 실측해 공개한 자료가 있는가? | [19. 모니터링·이상 탐지·원인 분석](categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md)<br>[20. 예외 복구·재계획·업무 연속성](categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) | 2026-09-25 | 2026-09-25-48 | 열림 | — |
| oq-076 | 국내 물류센터가 새 제조사 AMR 을 관제에 등록할 때 VDA 5050 팩트시트나 MassRobotics 신원 보고 같은 표준 등록 정보를 실제로 받은 사례가 있는가, 있다면 등록·설정 공수는 얼마나 줄었는가? | [21. 온보딩·설정·현장 시운전](categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md)<br>[9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | 2026-09-25 | 2026-09-25-52 | 열림 | — |
| oq-077 | 제조사 로봇 지도와 공통 관제 지도 사이 지도 정합(대응점 설정)의 오차를 현장 시운전에서 어떤 기준과 시험으로 합격 판정하는가? | [21. 온보딩·설정·현장 시운전](categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md)<br>[6. 지도·공간·위치 모델](categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)<br>[23. 시험·형식 검증·벤치마크](categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) | 2026-09-25 | 2026-09-25-52 | 열림 | — |
| oq-078 | 출처 충돌: 레이아웃 교환 형식(LIF)의 현행 판과 발행일(2023-09 1.0.0 대 VDMA 2024-03)은 무엇인가? | [21. 온보딩·설정·현장 시운전](categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md)<br>[6. 지도·공간·위치 모델](categories/b-common-information-and-environment-model/06-map-space-and-location-model.md) | 2026-09-25 | 2026-09-25-52 | 열림 | — |
| oq-079 | 운반 중 고장 난 로봇에 실린 화물을 사람이나 다른 로봇이 회수할 때 어떤 확인(스캔·무게·위치)으로 재고 위치를 바로잡는지 정한 운영 기준이나 국내 사례가 있는가? | [20. 예외 복구·재계획·업무 연속성](categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md)<br>[7. 화물·재고·자산 식별과 추적](categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md) | 2026-09-25 | 2026-09-25-50 | 열림 | — |
| oq-080 | 국내 물류센터가 로봇·관제 장애 때 수동 운영이나 제한 운영으로 전환하는 기준(허용 중단 시간, 전환·복귀 절차)을 BCP 에 정한 사례가 있는가? | [20. 예외 복구·재계획·업무 연속성](categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md)<br>[18. 사람–로봇 협업·운영 인터페이스](categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) | 2026-09-25 | 2026-09-25-50 | 열림 | — |
| oq-081 | 로봇 일부가 멈춘 제한 운영 상태의 처리량 저하를 미리 추정해 전환 결정에 쓰는 방법이나 사례가 있는가? | [20. 예외 복구·재계획·업무 연속성](categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md)<br>[22. 시뮬레이션·예측용 디지털 트윈](categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md) | 2026-09-25 | 2026-09-25-50 | 열림 | — |
| oq-082 | 로봇·제조사 관제가 보고하는 위치·배터리·입찰 비용이 오염되거나 위조되었을 때 ROP 는 배정 전에 이를 어떻게 검증하고, 의심 로봇을 배정 후보에서 뺄 기준은 무엇인가? | [13. 작업 배정 — MRTA](categories/d-planning-and-optimization/13-task-allocation-mrta.md)<br>[26. 사이버보안·접근권한·개인정보](categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md)<br>[19. 모니터링·이상 탐지·원인 분석](categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md) | 2026-09-25 | 2026-09-25-55 | 열림 | — |
| oq-083 | 현장 서버·클라우드·로봇 사이 통신이 나빠질 때 물류센터의 작업 배정을 중앙 방식으로 유지할지 분산 방식으로 전환할지 정한 기준이나 실측 자료가 있는가? | [13. 작업 배정 — MRTA](categories/d-planning-and-optimization/13-task-allocation-mrta.md)<br>[11. 분산 시스템·통신·컴퓨팅 구조](categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md) | 2026-09-25 | 2026-09-25-55 | 열림 | — |
| oq-084 | 물류센터에서 로봇 오케스트레이션 정책을 디지털 트윈으로 미리 시험한 뒤 실제 처리량과 비교해 예측 오차를 공개한 사례(특히 국내 사례)가 있는가? | [22. 시뮬레이션·예측용 디지털 트윈](categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md)<br>[4. 성과·경제성·프로세스 개선](categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) | 2026-09-25 | 2026-09-25-56 | 열림 | — |
| oq-085 | 제조용 ISO 23247 디지털 트윈 프레임워크(참조 구조·디지털 트윈 결합)를 물류센터의 이종 로봇·설비에 그대로 적용할 수 있는가, 물류용 확장이 필요한가? | [22. 시뮬레이션·예측용 디지털 트윈](categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | 2026-09-25 | 2026-09-25-56 | 열림 | — |
| oq-086 | 제조사 로봇을 단순화 모델(레일식 주행 등)로 시뮬레이션할 때 실제 거동과의 차이가 처리량·병목 예측에 주는 오차를 어떤 데이터로 보정하는가? | [22. 시뮬레이션·예측용 디지털 트윈](categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md)<br>[9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | 2026-09-25 | 2026-09-25-56 | 열림 | — |
| oq-087 | 로봇 제조사 펌웨어나 플릿 어댑터를 업데이트한 뒤 회귀 시험의 최소 기준으로 삼을 장애 시나리오 집합에 대해 공개된 기준이나 국내 사례가 있는가? | [23. 시험·형식 검증·벤치마크](categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md)<br>[24. 자산·소프트웨어 수명주기 관리](categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) | 2026-09-25 | 2026-09-25-59 | 열림 | — |
| oq-088 | BDD·모델 검사 같은 교착 부재 형식 검증을 대규모 창고 레이아웃과 동적 작업 배정에 적용하면 계산 규모의 한계는 어디이며 운영 중 재검증에 쓸 수 있는가? | [23. 시험·형식 검증·벤치마크](categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md)<br>[15. 다중 로봇 경로·교통 관리 — MAPF](categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md) | 2026-09-25 | 2026-09-25-59 | 열림 | — |
| oq-089 | 국내 시험기관(한국로봇산업진흥원 등)의 로봇 시험 항목에 다중 로봇 관제·오케스트레이션 소프트웨어 수준의 시험이 포함되는가, 없다면 누가 그 기준을 정하는가? | [23. 시험·형식 검증·벤치마크](categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | 2026-09-25 | 2026-09-25-59 | 열림 | — |
| oq-090 | 제조사 펌웨어가 바뀔 때 어느 현장·기능을 다시 검증할지 영향 범위를 산정하는 공개 절차나 표준이 있는가? | [24. 자산·소프트웨어 수명주기 관리](categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md)<br>[23. 시험·형식 검증·벤치마크](categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) | 2026-09-25 | 2026-09-25-61 | 열림 | — |
| oq-091 | VDA 5050 2.x 판과 3.0.0 판 로봇이 섞인 플릿에서 주 버전 차이를 어떻게 운영·이행하는가? | [24. 자산·소프트웨어 수명주기 관리](categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md)<br>[9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | 2026-09-25 | 2026-09-25-61 | 열림 | — |
| oq-092 | 국내 협동로봇 설치 작업장 안전인증에서 제어기 펌웨어·안전 파라미터 변경이 재심사 대상인지 공식 규정으로 확인할 수 있는가? | [24. 자산·소프트웨어 수명주기 관리](categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md)<br>[25. 안전·위험 관리](categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md) | 2026-09-25 | 2026-09-25-61 | 열림 | — |
| oq-093 | EU 기계 규정의 실질적 변경 판단이 로봇 동작을 바꾸는 오케스트레이션 정책·어댑터 업데이트에도 적용되는가? | [24. 자산·소프트웨어 수명주기 관리](categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md)<br>[25. 안전·위험 관리](categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md) | 2026-09-25 | 2026-09-25-61 | 열림 | — |
| oq-094 | Open-RMF 시뮬레이션의 lift_supervisor 처럼 여러 플릿의 승강기·문 요청 조율을 시뮬레이션에서 검증한 결과를 실제 설비 연동 시운전의 합격 기준으로 쓸 수 있는가, 쓴다면 시뮬레이션과 현장의 차이를 어떻게 확인하는가? | [22. 시뮬레이션·예측용 디지털 트윈](categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md)<br>[23. 시험·형식 검증·벤치마크](categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md)<br>[10. 설비·건물 시스템 연동](categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md)<br>[21. 온보딩·설정·현장 시운전](categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) | 2026-09-25 | 2026-09-25-67 | 열림 | — |
| oq-095 | ROP 가 VDA 5050 의 원격(REMOTE) 비상정지나 플릿 일괄 정지를 지시할 때 그 지시 경로가 안전 기능으로서 성능 수준(PL) 요구를 받는가, 아니면 운영 조율로만 보는가? | [25. 안전·위험 관리](categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md)<br>[12. 명령·작업 실행의 신뢰성](categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md) | 2026-09-25 | 2026-09-25-63 | 열림 | — |
| oq-096 | 여러 제조사 로봇이 섞인 현장에서 R15.08-2 가 말하는 통합자의 시스템 수준 위험성평가를 ROP 사업자·제조사·설비업체 중 누가 수행하고 갱신하는가? | [25. 안전·위험 관리](categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | 2026-09-25 | 2026-09-25-63 | 열림 | — |
| oq-097 | 산업안전보건기준에 관한 규칙 제223조의 울타리 생략 인정이 물류센터의 자율이동로봇(AMR) 플릿에도 적용되며, 어떤 KS·국제 기준 부합이 요구되는가? | [25. 안전·위험 관리](categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md)<br>[18. 사람–로봇 협업·운영 인터페이스](categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) | 2026-09-25 | 2026-09-25-63 | 열림 | — |
| oq-098 | KS B 7317 이 정한 이동 로봇의 승강기 탑승 단차·틈새 기준값은 무엇이며, 국내 물류센터의 화물용 승강기와 이종 제조사 로봇에 그대로 적용되는가? | [10. 설비·건물 시스템 연동](categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md)<br>[6. 지도·공간·위치 모델](categories/b-common-information-and-environment-model/06-map-space-and-location-model.md) | 2026-09-25 | 2026-09-25-65 | 열림 | — |
| oq-099 | 물류센터 내부처럼 공개되지 않은 작업장에서 카메라를 단 로봇이 작업자를 촬영할 때 개인정보 보호법 제25조의2와 근로자 감시 설비 협의 가운데 무엇이 적용되는지 공식 해석이 있는가? | [26. 사이버보안·접근권한·개인정보](categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md)<br>[18. 사람–로봇 협업·운영 인터페이스](categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) | 2026-09-25 | 2026-09-25-64 | 열림 | — |
| oq-100 | 외부 유지보수 계정의 권한을 로봇·명령 단위로 나눈 매트릭스(예: 진단은 허용, 이동은 불허)를 공개한 로봇 관제·ROP 구성이나 표준이 있는가? | [26. 사이버보안·접근권한·개인정보](categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md)<br>[9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | 2026-09-25 | 2026-09-25-64 | 열림 | — |
| oq-101 | 여러 화주가 로봇 플릿을 공유하는 창고에서 고객별 작업·데이터 격리를 오케스트레이션 수준에서 규정한 표준이나 공개 설계가 있는가? | [26. 사이버보안·접근권한·개인정보](categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | 2026-09-25 | 2026-09-25-64 | 열림 | — |
| oq-102 | ISO 10218-1:2025 의 사이버보안 요구는 어느 조항에서 무엇(접근 제한·원격 접속·로그 등)을 요구하며 로봇 관제 연동에 어떤 조건을 주는가? | [26. 사이버보안·접근권한·개인정보](categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md)<br>[25. 안전·위험 관리](categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md) | 2026-09-25 | 2026-09-25-64 | 열림 | — |
| oq-103 | EU 기계 규정 부속서 III 1.1.9 의 적용일이 사이버 복원력법(2027-12-11)에 맞춰 연기되는지 확정됐는가? | [26. 사이버보안·접근권한·개인정보](categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md)<br>[25. 안전·위험 관리](categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md) | 2026-09-25 | 2026-09-25-64 | 열림 | — |
| oq-104 | 창고 이동로봇 플릿의 재배정·재스케줄링 주기에서 LLM 추론 지연이 허용되는 한계를 측정했거나, LLM 을 결정 루프 밖에 둔 운영 사례가 있는가? | [14. 작업 순서·스케줄링](categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md)<br>[27. AI·학습·적응과 모델 운영](categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) | 2026-09-25 | 2026-09-25-66 | 열림 | — |
| oq-105 | 물류 현장 로봇의 작업 계획·배정에 쓰는 AI 가 한국 인공지능 기본법의 고영향 인공지능 영역에 해당하는가, 해당하면 ROP 사업자와 현장 운영사 중 누가 책무를 지는가? | [27. AI·학습·적응과 모델 운영](categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | 2026-09-25 | 2026-09-25-68 | 열림 | — |
| oq-106 | LLM 이나 학습 모델이 ROP 의 정지·경로·구역 결정에 관여할 때 EU AI Act 가 말하는 제품 안전 구성요소로 볼 수 있는가? | [27. AI·학습·적응과 모델 운영](categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)<br>[25. 안전·위험 관리](categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md) | 2026-09-25 | 2026-09-25-68 | 열림 | — |
| oq-107 | KnowNo 의 등각 예측 보장은 보정 데이터와 운영 분포가 같다는 조건에 기대는데, 물류 지시 분포가 계절·고객에 따라 바뀔 때 보정을 얼마나 자주 다시 해야 하는가? | [27. AI·학습·적응과 모델 운영](categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)<br>[18. 사람–로봇 협업·운영 인터페이스](categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) | 2026-09-25 | 2026-09-25-68 | 열림 | — |
| oq-108 | 제조용 CMSD 같은 중립 시뮬레이션 데이터 형식을 물류센터 로봇 시뮬레이션의 입력(레이아웃·주문 흐름·재고·로봇 자원)에 쓴 사례가 있는가, 없다면 물류용 확장이 필요한가? | [22. 시뮬레이션·예측용 디지털 트윈](categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | 2026-09-25 | 2026-09-25-70 | 열림 | — |
| oq-109 | ROP 사업자·로봇 제조사·현장 운영사가 함께 만든 로봇 운행·상태 데이터의 사용·수익 권리를 산업디지털전환촉진법의 공동 생성 규정에 따라 계약에서 어떻게 나누는가, 국내 로봇 관제 계약 사례가 있는가? | [28. 표준·상호운용성·다사업자 거버넌스](categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | 2026-09-25 | 2026-09-25-69 | 열림 | — |
| oq-110 | EU 데이터법의 데이터 공유 의무가 이종 로봇 플릿에서 제조사가 ROP 사업자(제3자)에게 로봇 사용 데이터를 제공해야 하는 근거가 되는가, 된다면 그 범위는 무엇인가? | [28. 표준·상호운용성·다사업자 거버넌스](categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)<br>[9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md) | 2026-09-25 | 2026-09-25-69 | 열림 | — |
| oq-111 | KOROS 1148-8:2025 의 상호운용성 시험 절차는 어떤 시험 항목을 두며, 물류 로봇 관제 연동의 적합성 시험 기준으로 쓸 수 있는가? | [28. 표준·상호운용성·다사업자 거버넌스](categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)<br>[23. 시험·형식 검증·벤치마크](categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) | 2026-09-25 | 2026-09-25-69 | 열림 | — |
| oq-112 | 이종 플릿 현장에서 ROP 가 고객과 맺는 가용성·응답 시간 목표를 제조사 관제·설비업체의 서비스 수준 목표와 어떻게 연쇄해 맞추며, 공개된 계약 구조나 사례가 있는가? | [28. 표준·상호운용성·다사업자 거버넌스](categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)<br>[20. 예외 복구·재계획·업무 연속성](categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md) | 2026-09-25 | 2026-09-25-69 | 열림 | — |
| oq-113 | ROP 가 VDA 5050 updateCertificate 같은 보안 명령으로 제조사 로봇의 인증서를 교체할 때, 교체 시점·대상 승인과 실패 시 되돌림 책임은 ROP 사업자·제조사·현장 IT 조직 중 누가 지는가? | [26. 사이버보안·접근권한·개인정보](categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md)<br>[9. 로봇·제조사 관제 연동](categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)<br>[24. 자산·소프트웨어 수명주기 관리](categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md) | 2026-09-25 | 2026-09-25-73 | 열림 | — |
| oq-114 | 로봇 관제가 배정 실패(수행 가능한 로봇·플릿 없음)를 WMS 등 상위 업무 시스템에 어떤 필드로 되돌리고, 상위 시스템이 이를 사람 작업 지시로 전환하는 표준이나 국내 물류센터 사례가 있는가? | [13. 작업 배정 — MRTA](categories/d-planning-and-optimization/13-task-allocation-mrta.md)<br>[1. 주문·업무 시스템 연계](categories/a-business-supply-chain-design/01-order-and-business-system-integration.md) | 2026-09-25 | 2026-09-25-74 | 열림 | — |
| oq-115 | 제조사가 자사 로봇 지도(SLAM 지도)의 판을 바꿀 때 변경 내용과 판 식별자를 ROP 나 상위 관제에 알리는 계약·인터페이스 관행이나 공개 사례가 있는가? | [24. 자산·소프트웨어 수명주기 관리](categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md)<br>[28. 표준·상호운용성·다사업자 거버넌스](categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md) | 2026-09-25 | 2026-09-25-78 | 열림 | — |
| oq-116 | ISO 18646-2:2024 의 지도 작성 정확도 시험은 무엇을 어떤 기준점과 절차로 측정하며, KS 로 부합화되어 국내 물류 로봇 시험에 쓰이는가? | [23. 시험·형식 검증·벤치마크](categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md)<br>[6. 지도·공간·위치 모델](categories/b-common-information-and-environment-model/06-map-space-and-location-model.md) | 2026-09-25 | 2026-09-25-80 | 열림 | — |
| oq-117 | 국내 물류센터 로봇 관제 도입에서 디지털 트윈·가상 로봇으로 관제 소프트웨어를 사전 검증한 결과를 실제 시운전 결과와 비교해 공개한 사례가 있는가? (관련 기존 질문: oq-094) | [22. 시뮬레이션·예측용 디지털 트윈](categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md)<br>[21. 온보딩·설정·현장 시운전](categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) | 2026-09-25 | 2026-09-25-99 | 열림 | — |
| oq-118 | 국내 물류센터 로봇 관제에서 작업 지시나 배정 결과를 배치 전에 시뮬레이션(디지털 트윈)으로 모의 실행해 확인하는 운영 사례나 연구가 있는가? | [22. 시뮬레이션·예측용 디지털 트윈](categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md)<br>[13. 작업 배정 — MRTA](categories/d-planning-and-optimization/13-task-allocation-mrta.md) | 2026-09-25 | 2026-09-25-81 | 열림 | — |
| oq-119 | 국내에서 실내공간정보 구축이나 로봇 도입 시 지도·공용 자원 설정 공수(인·일)를 산정하는 품셈이나 공공 기준이 있는가? | [21. 온보딩·설정·현장 시운전](categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md)<br>[4. 성과·경제성·프로세스 개선](categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md) | 2026-09-25 | 2026-09-25-82 | 열림 | — |
| oq-120 | 국내 로봇·물류 R&D 과제에서 도면 기반 지도 생성이나 로봇 관제 설정 자동화 기술의 성숙도를 기술성숙도(TRL) 기준으로 평가한 사례나 평가 기준이 있는가? | [21. 온보딩·설정·현장 시운전](categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md)<br>[23. 시험·형식 검증·벤치마크](categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md) | 2026-09-25 | 2026-09-25-84 | 열림 | — |
| oq-121 | 로봇 관제 챗봇의 채팅 지시 기록에 작업자 식별 정보가 담길 때 그 시스템이 개인정보의 안전성 확보조치 기준의 개인정보처리시스템에 해당해 접근권한 기록·접속기록 보관 기준을 적용받는지 공식 해석이 있는가? (관련: oq-099) | [26. 사이버보안·접근권한·개인정보](categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md)<br>[18. 사람–로봇 협업·운영 인터페이스](categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md) | 2026-09-25 | 2026-09-25-83 | 열림 | — |

상태별 건수: 열림 121건

**트랙 전용 질문(트랙 백로그)**

- 매뉴얼 기반 로봇 기능 온톨로지: [질문 백로그](tracks/manual-capability-ontology/question-backlog.md) (열린 질문 45건)
- 자연어 업무 지시 챗봇: [질문 백로그](tracks/nl-task-chatbot/question-backlog.md) (열린 질문 48건)
- 건축 도면 자동 인식: [질문 백로그](tracks/floorplan-recognition/question-backlog.md) (열린 질문 35건)
<!-- auto:open-questions:end -->
```

### _source/ROP_SCM_연구분야_분류.md

```markdown
# SCM 관점의 로봇 오케스트레이션 플랫폼 연구분야

> 문서화: 2026-09-24  
> 범위: 7개 대분류·28개 세부 연구영역, ROP의 책임 경계, 기존 아이디어의 위치, SCM 기반 분석 방법  
> 이 문서는 앞선 대화의 분류 내용을 Markdown으로 정리한 자료다. 공식 단일 분류가 아니라 공급망 프레임워크·로봇 연구·실제 플랫폼 구조를 종합한 연구 범위 점검용 분류이며, 모든 항목을 직접 개발한다는 의미는 아니다.

## 1. 전체 관점

SCM 관점에서 ROP는 **주문·물류·생산 계획을 로봇과 현장 설비의 실제 행동으로 연결하고, 결과를 다시 업무 시스템에 반영하는 실행 플랫폼**으로 볼 수 있다.

연구 범위는 다음과 같이 구분한다.

| 대분류 | 핵심 질문 | 세부영역 |
|---|---|---|
| A. 업무·공급망 설계 | 무슨 일을 왜, 얼마나 해야 하는가? | 1–4 |
| B. 공통 정보·환경 모델 | 로봇·물건·공간·상태를 어떻게 같은 의미로 이해할 것인가? | 5–8 |
| C. 연결·실행 기반 | 계획한 작업을 실제 장비가 확실하게 수행하게 하려면? | 9–12 |
| D. 계획·최적화 | 누가, 언제, 어디로, 어떤 자원을 사용해 작업할 것인가? | 13–16 |
| E. 협업·현장 운영 | 계획과 실제가 달라지는 상황에서 일을 어떻게 계속할 것인가? | 17–20 |
| F. 도입·검증·유지관리 | 새 현장에 설치하고, 변경하면서, 오래 운영하려면? | 21–24 |
| G. 안전·보안·지능·거버넌스 | 전체 영역에 어떤 공통 제약과 관리 체계를 적용할 것인가? | 25–28 |

ASCM의 SCOR는 계획·주문·조달·생산/가공·이행·반품과 이를 아우르는 Orchestrate를 다룬다. **ROP는 이 중 물리적인 작업이 발생하는 부분을 연결하는 역할**로 접근할 수 있다. SCOR의 공급망 오케스트레이션과 로봇 오케스트레이션은 범위가 다르다. [1]

## 2. A — 업무·공급망 설계

**무슨 일을 왜, 얼마나 해야 하는가**를 연구한다. 로봇을 움직이기 전에 공급망의 요구를 실행 가능한 업무로 정의하는 영역이다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **1. 주문·업무 시스템 연계** | ERP, WMS, MES, WES, TMS의 주문·재고·생산 요청을 받아 작업으로 변환하고, 변경·취소·완료를 다시 반영하는 방법 | 출고 우선순위가 바뀌면 이미 진행 중인 로봇 작업을 어떻게 바꿀까? |
| **2. 공정·워크플로 모델링** | 입고·검수·적치·보충·피킹·이송·생산·포장·출하·반품을 작업 단계로 분해하고, 선후관계와 완료 조건을 정의 | ‘운반 완료’와 ‘인수 확인·재고 반영 완료’를 어떻게 연결할까? |
| **3. 처리능력·거점·설비 계획** | 물동량에 필요한 로봇 수와 종류, 작업대·충전기 배치, 교대 운영, 여러 거점의 자원 배치를 결정 | 로봇을 늘려야 할까, 포장대나 엘리베이터가 병목일까? |
| **4. 성과·경제성·프로세스 개선** | 납기 준수율, 처리량, 리드타임, 재공품, 비용, 에너지 등을 측정하고 병목과 투자 효과를 분석 | 로봇 가동률 상승이 실제 출하량과 비용 개선으로 이어졌는가? |

핵심은 **로봇 개별 성능과 공급망 전체 성과를 구분하는 것**이다. 로봇이 물건을 더 빨리 가져와도 다음 공정이 막히면 대기 재고만 늘어날 수 있다.

기업 업무와 현장 운영·제어의 경계를 정리할 때는 ISA-95의 기업–제어 시스템 통합 관점이 참고가 된다. 실제 제품별로 WES·WCS·FMS·ROP의 책임은 겹칠 수 있다. [2]

## 3. B — 공통 정보·환경 모델

**로봇, 물건, 공간, 상태를 어떻게 같은 의미로 이해할 것인가**를 연구한다. 매뉴얼 온톨로지와 건축 도면 기반 지도가 주로 이 영역에 들어간다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **5. 로봇 능력·작업 온톨로지** | 제조사별 기능·제약·장착 장비·실행 조건을 공통 모델로 표현하고, 작업 요구와 연결 | 같은 ‘운반 로봇’ 중 누가 이 화물을 실제로 취급할 수 있는가? |
| **6. 지도·공간·위치 모델** | BIM·CAD·센서 지도에서 이동 공간과 경로를 만들고, 로봇별 좌표계·층·목적지를 정렬 | 제조사마다 다른 지도에서 ‘3층 출하 대기장’을 어떻게 동일한 장소로 인식할까? |
| **7. 화물·재고·자산 식별과 추적** | 제품·박스·팔레트·운반구·로봇을 식별하고, 적재 관계·위치·인계 이력을 연결 | 로봇은 도착했는데 실제로 어떤 팔레트가 인계됐는가? |
| **8. 실시간 세계 상태·데이터 일관성** | 로봇·설비·공간·화물의 현재 상태를 통합하고, 시간 지연·누락·충돌·불확실성을 관리 | 문이 열려 있다는 정보가 30초 전이라면 지금도 통과 가능하다고 볼 수 있을까? |

**7번은 SCM 관점에서 특히 빠뜨리기 쉽다.** 로봇 위치를 추적하는 것과 화물의 위치·인계 책임을 추적하는 것은 다르다. GS1 EPCIS는 제품·자산의 상태, 위치, 이동, 인계에 관한 이벤트를 공유하는 참고 표준이다. [3]

6번에는 지도 생성뿐 아니라 **현장과 도면의 차이 확인, 지도 버전 관리, 위치추정 결과의 신뢰도**도 포함해야 한다.

## 4. C — 연결·실행 기반

**계획한 작업을 실제 장비가 확실하게 수행하게 하는 방법**을 연구한다. 공통 모델을 실제 명령·통신·실행으로 연결하는 영역이다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **9. 로봇·제조사 관제 연동** | 제조사 API·SDK·표준 프로토콜을 연결하고 명령·상태·오류를 변환하는 어댑터 | 개별 로봇을 제어할까, 제조사 관제에 미션을 맡길까? |
| **10. 설비·건물 시스템 연동** | 컨베이어, 자동창고, 작업대, PLC, 문, 승강기, 출입통제 시스템과 작업을 연계 | 컨베이어 준비와 로봇 도착을 어떻게 맞출까? |
| **11. 분산 시스템·통신·컴퓨팅 구조** | 클라우드·현장 서버·로봇의 역할 분담, 네트워크 지연, 서비스 가용성, 데이터 전송 품질, 다거점 운영 | 인터넷이 끊겨도 현장에서 어디까지 계속 운영할 수 있을까? |
| **12. 명령·작업 실행의 신뢰성** | 접수·실행·완료·취소 상태, 제어권, 중복 요청 방지, 시간 초과, 재시작 후 상태 복원 | 응답이 끊긴 운반 요청을 다시 보내면 같은 화물을 두 번 처리하지 않을까? |

Open-RMF도 제조사별 Fleet Adapter와 건물 설비 인터페이스를 통해 로봇·문·승강기 등을 연결한다. **로봇 연결과 시설 연결을 함께 보는 것**이 필요하다. [4]

## 5. D — 계획·최적화

**누가, 언제, 어디로, 어떤 자원을 사용해 작업할 것인가**를 연구한다. 논문에서 작업 배정이나 경로 계획으로 많이 등장하는 영역이다. 네 항목은 분리해서 연구할 수 있지만 실제 운영에서는 서로 영향을 준다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **13. 작업 배정 — MRTA** | 능력·위치·적재량·배터리·납기 등을 고려해 로봇 또는 로봇 팀에 작업을 배정 | 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? |
| **14. 작업 순서·스케줄링** | 주문 묶음, 작업 선후관계, 시간 제약, 공정 간 동기화, 긴급 작업 삽입 | 피킹·운반·포장이 서로 기다리지 않게 어떤 순서로 실행할까? |
| **15. 다중 로봇 경로·교통 관리 — MAPF** | 여러 로봇의 경로와 통과 시점을 조율하고, 혼잡·교착·우선권을 처리 | 서로 다른 제조사의 로봇이 좁은 통로에서 마주치면 누가 양보할까? |
| **16. 공용 자원·충전·에너지 최적화** | 충전기·승강기·작업대·대기 공간·버퍼의 예약과 배분, 충전 시점과 에너지 사용 계획 | 로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까? |

SCM에서는 **작업이 계속 새로 들어오는 조건**이 중요하다. 정해진 목적지까지 한 번 이동하는 문제와 지속적으로 주문이 들어오는 운영은 다르다. 이를 다루는 연구가 *Lifelong MAPF*, *Multi-Agent Pickup and Delivery*이다. [5][6]

## 6. E — 협업·현장 운영

**계획과 실제가 달라지는 상황에서 일을 어떻게 계속할 것인가**를 연구한다. 정상적인 시연과 실제 운영의 차이가 많이 드러나는 영역이다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **17. 로봇 간 협업·물리적 인계** | 이동로봇–로봇팔 협업, 공동 운반, 작업 동기화, 인계 확인, 필요한 정보·인식 결과 공유 | AMR이 물건을 가져온 뒤 로봇팔이 안전하게 인수했음을 어떻게 확인할까? |
| **18. 사람–로봇 협업·운영 인터페이스** | 작업자에게 일 배정, 승인·수동 전환, 원격 조작, 설명 가능한 상태 표시, 인체공학 | 사람이 피킹하고 로봇이 운반할 때 서로 기다리지 않게 하려면? |
| **19. 모니터링·이상 탐지·원인 분석** | 로그·이벤트·성능 지표를 연결해 이상을 탐지하고, 로봇·설비·통신·공정 원인을 구분 | 지연 원인이 로봇 고장인지, 문인지, 앞 공정인지 어떻게 찾을까? |
| **20. 예외 복구·재계획·업무 연속성** | 고장·통신 단절·화물 누락·긴급 주문 등에 대해 재배정, 우회, 수동 처리, 제한 운영을 결정 | 운반 중 고장 난 로봇의 화물과 남은 주문은 어떻게 처리할까? |

17번의 협업은 이동로봇끼리 길을 양보하는 문제보다 넓다. **이동·조작·검사·사람 작업을 하나의 공정으로 묶는 문제**까지 포함한다. NIST도 이종 로봇과 사람의 협업 성능을 별도 연구·평가 대상으로 다룬다. [7]

## 7. F — 도입·검증·유지관리

**새 현장에 설치하고, 변경하면서, 오래 운영하는 방법**을 연구한다. 플랫폼 사업에서는 알고리즘 성능 못지않게 중요한 영역이다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **21. 온보딩·설정·현장 시운전** | 로봇 등록, 기능 탐색, 문서 분석, 지도·설비 설정, 교정, 설치 절차 자동화 | 새 제조사나 새 물류센터를 추가할 때 반복 작업을 얼마나 줄일까? |
| **22. 시뮬레이션·예측용 디지털 트윈** | 로봇·설비·물동량을 가상 환경에서 재현하고, 배치·운영 정책·수요 변화의 효과를 예측 | 성수기 주문량이 늘면 어디가 먼저 막힐까? |
| **23. 시험·형식 검증·벤치마크** | 시뮬레이션·실기체 시험, 장애 주입, 교착·제약 위반 검증, 회귀시험, 성능 비교 | 업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가? |
| **24. 자산·소프트웨어 수명주기 관리** | 고장 예측·정비, 배터리 열화, 펌웨어·어댑터·지도·모델 버전, 배포·복구, 장비 교체 | 제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? |

8번의 실시간 모델이 **현재 상태를 표현**한다면, 22번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다.

NIST의 ARIAC처럼 변화하는 제조 환경에서 로봇의 계획·인식·행동과 적응성을 평가하는 시험 환경도 참고할 수 있다. [8]

## 8. G — 안전·보안·지능·거버넌스

위 여섯 영역 전체에 적용되는 연구다. 마지막에 추가하는 부가기능으로 보면 누락되기 쉽다.

| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 |
|---|---|---|
| **25. 안전·위험 관리** | 로봇·사람·설비 상호작용의 위험, 안전 조건, 정지·재개 절차, 비상 상황 대응, 안전 책임 경계 | 여러 장비는 각각 안전해도 함께 움직일 때 새로운 위험이 생기지 않는가? |
| **26. 사이버보안·접근권한·개인정보** | 장비 인증, 통신 보호, 명령 권한, 원격 접속, 고객별 격리, 영상·작업자 데이터 보호 | 외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가? |
| **27. AI·학습·적응과 모델 운영** | 문서·도면 해석, 수요·고장 예측, 학습 기반 계획, LLM 에이전트, 불확실성 평가, 모델 변경 관리 | AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? |
| **28. 표준·상호운용성·다사업자 거버넌스** | 공통 규격, 적합성 시험, 제조사 간 책임, 데이터 소유권, API 변경 정책, 서비스 수준과 감사 이력 | 제조사·ROP·설비업체 중 누가 연동 오류를 수정하고 변경을 승인할까? |

ROS 2도 인증·암호화·접근권한과 보안 위협 모델을 별도로 다룬다. 기능 연동과 보안 연동은 함께 설계해야 하는 영역이다. [9][10]

27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다.

## 9. ROP가 직접 소유할 범위와 외부 연계 경계

전체를 연구하되 **ROP가 직접 소유할 범위는 별도로 정해야 한다.** 그렇지 않으면 SCM 시스템부터 로봇의 모터 제어까지 모두 만드는 프로젝트가 된다.

| 경계 | ROP에서 다룰 내용 | 주로 연계할 외부 영역 |
|---|---|---|
| **상위 업무 시스템** | 주문·납기·재고 제약을 받아 실행하고 결과 반영 | 수요예측, 구매, 재무, 전사 재고정책 |
| **로봇 자체 지능·제어** | 가능한 기능과 실행 조건, 상태·실패·완료 확인 | 센서 인식, SLAM, 로컬 회피, 파지, 모터·관절 제어 |
| **시설·설비 제어** | 작업 요청·예약·인계·상태 확인 | 승강기·컨베이어·PLC·설비 안전 제어 |
| **거점 간 운송** | 입출고 시간과 인계, 현장 작업 동기화 | 배차·운송계획·운임·국제물류 |
| **업종별 조건** | 해당 조건을 작업·경로·권한 제약으로 반영 | 의료·식품·위험물·실외 차량·드론 등의 전문 요구사항 |

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.**

## 10. 논의한 아이디어의 연구영역 매핑

| 아이디어 | 중심 연구영역 | 함께 필요한 영역 |
|---|---|---|
| 매뉴얼 기반 로봇 온톨로지 | **5. 능력·작업 온톨로지** | 9. 어댑터, 21. 온보딩, 23. 검증, 24. 버전 관리 |
| 건축 도면 기반 이동 지도 | **6. 지도·공간 모델** | 15. 교통 관리, 21. 시운전, 22. 시뮬레이션 |
| 로봇과 건물 조건을 함께 판단 | **5+6+8. 능력·공간·현재 상태** | 13. 배정, 16. 자원, 25. 안전 |
| SCM 전체와 연결한 ROP | **1+2+4. 업무 연계·공정·성과** | C~G의 필요한 기능을 조합 |

## 11. SCM 관점의 연구 시작 방법

**기술 목록에 실제 물류 흐름을 교차해서 본다.**

첫 분석 대상으로 한 현장의 **입고 → 적치 → 보충 → 피킹 → 포장 → 출하 → 반품**을 잡고, 각 단계마다 다음 여섯 항목을 채운다.

1. **시작 조건:** 어떤 주문·재고·설비 이벤트가 작업을 발생시키는가?
2. **작업 대상:** 어떤 화물·운반구를 다루는가?
3. **수행 자원:** 로봇·사람·설비 중 누가 어떤 부분을 맡는가?
4. **제약:** 납기·공간·적재량·설비·권한 제약은 무엇인가?
5. **완료·인계:** 무엇이 확인돼야 업무 완료와 재고 변경을 인정하는가?
6. **예외·성과:** 실패하면 누가 복구하며, 처리량·시간·비용에 어떤 영향을 주는가?

예를 들어 **‘피킹한 박스를 포장대로 운반’**이라는 작업 하나에서도 로봇 배정, 경로, 포장대 수용능력, 화물 식별, 인계 확인, 고장 복구가 연결된다. 이 흐름을 먼저 정하면, 온톨로지와 지도 자동화가 **전체 공급망의 어느 비용과 병목을 줄이는 기술인지** 구체적으로 판단할 수 있다.

## 12. 참고 자료

아래는 앞선 답변에서 확인·인용한 공식 자료와 연구 논문이다. 분류표 전체를 단일 출처에서 가져온 것은 아니며, 세부 분류와 연구 질문은 이를 바탕으로 구성한 분석이다.

1. ASCM. [SCOR Digital Standard](https://www.ascm.org/corporate-solutions/standards-tools/scor-ds/). 공급망 프로세스 범위 참고.
2. ISA. [Update to ISA-95 Standard Addresses Integration of Enterprise and Manufacturing Control Systems](https://www.isa.org/news-press-releases/2025/april/update-to-isa-95-standard-addresses-integration-of), 2025. 기업 업무와 제조 운영·제어의 통합 경계 참고.
3. GS1. [EPCIS and CBV Linked Data Model](https://ref.gs1.org/epcis/). 제품·자산의 상태·위치·이동·인계 이벤트 모델 참고.
4. Open Robotics. [RMF Core Overview — Programming Multiple Robots with ROS 2](https://osrf.github.io/ros2multirobotbook/rmf-core.html). 작업·교통 조율, Fleet Adapter, 설비 연동 구조 참고.
5. Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S. [Lifelong Multi-Agent Path Finding in Large-Scale Warehouses](https://arxiv.org/abs/2005.07371), 2020. 지속적으로 목표가 들어오는 다중 로봇 경로 계획 연구.
6. Ma, H., Li, J., Kumar, T. K. S., & Koenig, S. [Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks](https://arxiv.org/abs/1705.10868), 2017. 온라인 픽업·배송 작업의 배정과 충돌 없는 이동 연구.
7. NIST. [Performance of Collaborative Robot Systems](https://www.nist.gov/programs-projects/performance-collaborative-robot-systems). 사람–로봇 및 이종 로봇 협업 성능 평가 참고.
8. NIST. [ARIAC Documentation](https://pages.nist.gov/ARIAC_docs/en/latest/). 변화하는 제조 환경에서의 로봇 작업 수행·적응성 평가 참고.
9. ROS 2 Design. [ROS 2 DDS-Security Integration](https://design.ros2.org/articles/ros2_dds_security.html). 인증·암호화·접근통제 구조 참고.
10. ROS 2 Design. [ROS 2 Robotic Systems Threat Model](https://design.ros2.org/articles/ros2_threat_model.html). 로봇 시스템의 보안 위협과 대응 설계 참고.
```

### runs/2026-09-26-01/verification2.json

```json
{
  "run_id": "2026-09-26-01",
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
      "새 열린 질문(산업 디지털 전환 촉진법 제명 변경)은 oq-109 와 대상 법률이 같다. 질문 끝에 '(관련 기존 질문: oq-109)'로 연결했다(1차 지시 이행)",
      "ref-709 는 ref-315 의 중복이다. deprecated 로 처리했고 대체 항목은 ref-315 다",
      "ref-584·ref-707·ref-767 은 같은 표준 IEC 62443-3-3:2013 을 가리킨다. 다음 실행 후보로만 기록했다"
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
    "docs/references/ref-637.md 각주 형식 절: 첫 문장 '등록 URL 을 퍼센트 인코딩 형태로 바꿨다.'를 'URL 을 퍼센트 인코딩 형태로 적은 것은 이 절의 각주 형식 줄뿐이다. 등록 URL(프런트매터 url, 서지 정보 표) 교체는 pipeline 담당에게 요청했으며 아직 반영되지 않았다.'로 고친다. 이유: 이번 패치는 이 절만 바꿨다. 프런트매터 url, 서지 정보 표의 URL, 페이지 끝 각주 정의는 여전히 인코딩되지 않은 등록 URL 이다. fixes_applied 와 additional_research_requests 도 등록 URL 을 되돌렸다고 적고 있다. 따라서 지금 문장은 페이지의 실제 상태와 맞지 않는다. 뒤 문장('이전 URL 은 … 문서 자체는 존재한다. [사실][^ref-637]')과 [추정] 문단은 그대로 둔다.",
    "docs/logs/weekly/2026-W39.md 6절 3번 항목: '이번 실행에서는 URL 만 인코딩 형태로 바꾸고 제목·법률 번호·발행일은 유지했다.'를 '이번 실행에서는 참고문헌 페이지의 각주 형식과 이 페이지 각주에만 인코딩 URL 을 적었다. 등록 URL 교체는 pipeline 담당에게 요청했다. 제목·법률 번호·발행일은 유지했다.'로 고친다. 같은 절 표의 ref-637 조치 칸 'URL 교정, needs_update'는 '각주 URL 인코딩 표기, needs_update(등록 URL 교체 요청)'로 고친다. 이유: 등록 URL 은 바뀌지 않았다. 위 ref-637 수정과 표기를 맞춘다.",
    "pages.json index_updates.home_recent 의 '(ref-637 URL 교정, …)'를 '(ref-637 각주 URL 인코딩 표기·needs_update, …)'로 고친다. 이유: 등록 URL 이 바뀌지 않았으므로 '교정'은 실제 처리 내용과 다르다. changelog_entry 는 이미 '인코딩 표기'라고 적었으므로 그대로 둔다.",
    "docs/logs/weekly/2026-W39.md 6절 끝 운영 메모(표준 목록 docs/standards/index.md 의 판 표기 중복 항목: IDTA 02020, IDTA 02047, KS B 7321-2, LIF, rmf_task, rmf_simulation 등)를 삭제한다. 대신 additional_research_requests 에 '다음 주간 정리에서 표준 목록 중복 항목 점검'으로 옮긴다. 이유: 브리프 finding 과 1차 판정 어디에도 없는 관찰이어서 이번 검증 입력으로 확인할 수 없다. 주간 정리의 내용 출처 규칙(이번 주 실행 산출물과 브리프 점검 결과)에서도 벗어난다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 1차 조건부 승인. 이번 실행은 원문 열람이 차단된 환경에서 검증됐다(fetch_mode mirror_only). ref-172(ROSA 위키)와 ref-412(Open-RMF place.json)는 검증자가 raw.githubusercontent.com 으로 직접 열어 제목·내용이 일치함을 확인했다. ref-637 은 검색 결과가 일치하는지로 확인했다. 검증 검색은 2회로, 리서치와 합쳐 4/30 이다. 확인 6건, 미확인 0건, 교차 확인 0건. 강등: 없음(f2 의 '일시적 실패' 부분만 [추정]으로 나눔). 원문 미열람 출처: ref-637, ref-315, ref-709, ref-584, ref-707, ref-767. 처리: ref-637 은 URL 인코딩 교정과 needs_update, ref-709 는 deprecated(대체 ref-315)로 처리한다. ref-584·ref-707·ref-767 통합과 ref-172 미러 등록은 다음 실행 후보다. 주의: 검증 검색에서 '산업 디지털 전환 및 인공지능 활용 촉진법' 제정·개정문 페이지와 시행 보도가 보였다. 그러나 원문을 열지 못해 제명 변경과 시행 여부는 [추정]으로 두고 열린 질문(관련: oq-109)으로 보낸다. ref-584 는 IEC 원판이 아니라 CSA 채택판이다. 운영: 보류 실행 2026-09-25-100 의 참고문헌 id(ref-748~ref-750)가 게시된 참고문헌과 겹친다. 참고문헌 번호 ref-781~ref-791 은 비어 있다. 정정 요청은 없다. / 2차 수정 후 재검증. 드리프트 2건을 처리한다. 첫째, ref-637 참고문헌 페이지와 주간 정리가 등록 URL 을 바꿨다고 적었지만 실제로는 각주 형식 줄에만 인코딩 URL 을 적었고 등록 URL 교체는 pipeline 담당 요청으로 남았다(서술 정정 지시). 둘째, 주간 정리 6절의 표준 목록 중복 운영 메모는 브리프에 없는 관찰이다(삭제 후 추가 조사 요청으로 이동). 1차 수정 지시 8건 가운데 나머지는 이행을 확인했다: f2 사실·추정 분리, 원문 미열람 각주 6건, source_unopened 표시, ref-709 deprecated와 대체 줄, 새 열린 질문과 oq-109 연결, 운영 기록 id. 참고문헌 페이지에는 상태 줄이 없어서 ref-709 의 대체 페이지 줄을 각주 형식 절 첫머리에 둔 것은 인정한다. 주간 정리 4·7절의 건수(oq-001~oq-121, 트랙 백로그 45·48·35건, 용어 205개 중 draft 10개)는 입력과 일치한다. 1절의 실행 90회(게시 82, 보류 4, 중단 4)는 합계가 맞는다. 다만 1·3절의 실행별 판정·강등 내역은 이번 검증 입력에 실행 산출물 원본이 없어 합계와 형식만 확인했다. [분류원문] 보존, 섹션 순서 준수, 링크 유효(형식 검증 코드 통과).",
  "retry_reason": null
}
```
