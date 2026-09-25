(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-25-73
- date: 2026-09-25
- run_type: category_link (대분류 연결)
- 대상: 대분류 G. 안전·보안·지능·거버넌스 페이지의 '다른 대분류와의 연결' 절(대분류 연결 실행). 게시된 세부영역 페이지를 근거로 다른 대분류와의 연결을 조사·서술한다. 스토리텔러는 그 절만 patches 로 바꾼다
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

## 입력

### runs/2026-09-25-73/target.json

```json
{
  "run_id": "2026-09-25-73",
  "date": "2026-09-25",
  "weekday": "Fri",
  "run_number": 73,
  "run_type": "category_link",
  "forced": true,
  "target": {
    "area_no": null,
    "area_name": null,
    "category": "G. 안전·보안·지능·거버넌스",
    "category_letter": "G"
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
  "selection_rationale": "CLI 지정 run_type=category_link"
}
```

### runs/2026-09-25-73/research.json

```json
{
  "run_id": "2026-09-25-73",
  "date": "2026-09-25",
  "run_type": "category_link",
  "target": {
    "area_no": null,
    "area_name": null,
    "category": "G. 안전·보안·지능·거버넌스"
  },
  "gaps": [
    "G. 안전·보안·지능·거버넌스 대분류 페이지의 '다른 대분류와의 연결' 절이 '아직 작성되지 않음' 상태",
    "C. 연결·실행 기반 페이지가 27. AI·학습·적응과 모델 운영과의 연결을 '근거 없음'으로 두었음(이번 실행에서 보강 후보를 냄)",
    "A. 업무·공급망 설계 페이지가 25. 안전·위험 관리, 26. 사이버보안·접근권한·개인정보, 27. AI·학습·적응과 모델 운영과의 연결을 아직 다루지 않았음",
    "E. 협업·현장 운영 페이지가 26. 사이버보안·접근권한·개인정보와의 연결을 '근거 없음'으로 두었음(이번 실행에서 보강 후보를 냄)",
    "F. 도입·검증·유지관리 쪽 24. 자산·소프트웨어 수명주기 관리 ↔ 27. AI·학습·적응과 모델 운영(모델 버전 관리) 연결이 어느 대분류 페이지에도 없음"
  ],
  "research_questions": [
    "전체 영역에 어떤 공통 제약과 관리 체계를 적용할 것인가? [분류원문]",
    "25. 안전·위험 관리는 C. 연결·실행 기반·D. 계획·최적화·E. 협업·현장 운영의 어느 세부영역에 어떤 안전 상태·구역·비상 신호로 제약을 거는가, 그리고 ROP 몫과 연계 대상의 경계는 어디인가?",
    "26. 사이버보안·접근권한·개인정보는 9. 로봇·제조사 관제 연동, 10. 설비·건물 시스템 연동, 13. 작업 배정 — MRTA, 18. 사람–로봇 협업·운영 인터페이스, 24. 자산·소프트웨어 수명주기 관리와 어떤 권한·인증서·패치·영상 데이터로 이어지는가?",
    "27. AI·학습·적응과 모델 운영은 분류 원문 8장 교차 규칙의 적용 대상(5. 로봇 능력·작업 온톨로지, 6. 지도·공간·위치 모델, 13. 작업 배정 — MRTA, 19. 모니터링·이상 탐지·원인 분석, 21. 온보딩·설정·현장 시운전) 외에 C. 연결·실행 기반·F. 도입·검증·유지관리와 무엇으로 이어지는가? (C. 연결·실행 기반 페이지의 '근거 없음' 갭 겨냥)",
    "28. 표준·상호운용성·다사업자 거버넌스는 1. 주문·업무 시스템 연계, 9. 로봇·제조사 관제 연동, 15. 다중 로봇 경로·교통 관리 — MAPF, 19. 모니터링·이상 탐지·원인 분석, 23. 시험·형식 검증·벤치마크, 24. 자산·소프트웨어 수명주기 관리에 어떤 표준·판·책임 문제를 넘겨받는가?",
    "게시된 다른 대분류 페이지(A~F)의 G. 안전·보안·지능·거버넌스 쪽 연결 서술 가운데 G 쪽 세부영역 근거로 다시 확인·보강할 것은 무엇인가?"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스 ↔ A. 업무·공급망 설계의 1. 주문·업무 시스템 연계: ISA-95 계열 작업 지시 동사·메서드(B2MML CHANGE·CANCEL, OPC UA for ISA-95 Job Control)와 VDA 5050·Open-RMF 주문·작업 요청을 잇는 표준 매핑이 확인되지 않아, 번역 규칙의 소유와 변경 승인이 거버넌스 과제로 넘어갈 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-129",
        "ref-130",
        "ref-031",
        "ref-125"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "A. 업무·공급망 설계 페이지 G 연결 항목과 같은 근거. 표준 매핑 부재는 조사 범위의 관찰이며 부재 확인은 아님(oq-020). (재인용: 2026-09-25-29)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f2",
      "claim": "G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스 ↔ A. 업무·공급망 설계의 1. 주문·업무 시스템 연계: 상위 업무 시스템에 여는 ROP API 의 판 번호·폐기 예고 정책은 ROP 몫으로 보이며, 의미적 버전 관리(SemVer 2.0.0)와 RFC 9745 Deprecation 헤더가 그 규칙의 후보가 된다.",
      "tag": "추정",
      "source_ids": [
        "ref-635",
        "ref-706"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "28. 표준·상호운용성·다사업자 거버넌스 9절 표 '상위 업무 시스템' 행의 [추정] 주장(ref-635, ref-706). SemVer 는 호환되지 않는 API 변경에 주 버전을 올리게 한다.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f3",
      "claim": "G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영 ↔ A. 업무·공급망 설계의 1. 주문·업무 시스템 연계: 주문·납기 제약을 받는 배정·계획 모델의 버전·변경 승인은 ROP 몫이고, 수요예측 모델은 분류 원문 9장 상위 업무 시스템 경계의 연계 대상으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-626",
        "ref-618"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "27. AI·학습·적응과 모델 운영 9절 표 '상위 업무 시스템' 행: ROP 는 배정·계획 모델의 버전·변경 승인, 수요예측 모델은 연계 대상.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f4",
      "claim": "G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영 ↔ B. 공통 정보·환경 모델의 5. 로봇 능력·작업 온톨로지: 대규모 언어 모델로 능력 온톨로지를 생성하는 연구(2024-04)와 로봇 기술 파일(URDF)에서 로봇 온톨로지를 LLM 으로 채우는 연구(2026-06)가 있어, 분류 원문 8장의 매뉴얼 해석 교차 규칙이 두 대분류를 잇는다.",
      "tag": "사실",
      "source_ids": [
        "ref-238",
        "ref-239"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "B. 공통 정보·환경 모델 페이지 G 연결 항목의 [사실] 주장과 같은 각주. 두 연구는 각각 단일 출처. (재인용: 2026-09-25-32)",
      "as_of": "2026-06",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f5",
      "claim": "G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영 ↔ B. 공통 정보·환경 모델의 6. 지도·공간·위치 모델: 비전 언어 모델로 평면도 지도를 해석하는 연구(2024-09)가 있어, 분류 원문 8장 교차 규칙의 도면 해석이 두 대분류를 잇는다.",
      "tag": "사실",
      "source_ids": [
        "ref-076"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "DeFazio 외, Vision Language Models Can Parse Floor Plan Maps(2024-09). B. 공통 정보·환경 모델 페이지 G 연결 항목과 같은 각주. (재인용: 2026-09-25-32)",
      "as_of": "2024-09",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f6",
      "claim": "G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스 ↔ B. 공통 정보·환경 모델의 5. 로봇 능력·작업 온톨로지: 무인운반차 기술 데이터 서브모델 IDTA 02047, 서비스 로봇 모듈 공통 정보 모델 ISO 22166-201(2024-02), 국내 KS B 7321-2 같은 제조사 독립 정보 모델 표준이 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-234",
        "ref-240",
        "ref-138"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "B. 공통 정보·환경 모델 페이지 G 연결 항목과 같은 각주. KS 부합화 여부는 oq-004·oq-026 에서 열림. (재인용: 2026-09-25-32)",
      "as_of": "2024-02",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f7",
      "claim": "G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스 ↔ B. 공통 정보·환경 모델의 6. 지도·공간·위치 모델: ISO 21423 은 산업용 이동로봇의 통신·상호운용성을 다루는 국제표준이며, 그 공통 좌표계와 제조사 지도 식별자의 대응은 확인되지 않았다.",
      "tag": "사실",
      "source_ids": [
        "ref-159"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability. 발행 여부·좌표계 정의 미확인(oq-027). (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f8",
      "claim": "G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ B. 공통 정보·환경 모델의 8. 실시간 세계 상태·데이터 일관성: Open-RMF 승강기 상태의 운영 모드에 사람·AGV·화재·오프라인·비상이 있으므로, 탑승 확정 전에 최신 모드를 확인하는 규칙이 안전 조건과 맞물릴 것으로 보이며, 설비 안전 제어 자체는 연계 대상이다.",
      "tag": "추정",
      "source_ids": [
        "ref-286"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "LiftState.msg 운영 모드 값(HUMAN·AGV·FIRE·OFFLINE·EMERGENCY). B. 공통 정보·환경 모델 페이지 G 연결 항목과 같은 주장. (재인용: 2026-09-25-32)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f9",
      "claim": "G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ C. 연결·실행 기반의 10. 설비·건물 시스템 연동: 국가기술표준원은 2021-11 이동 로봇의 엘리베이터 탑승 안전 요구사항과 평가 방법을 정한 KS B 7317 을 제정했고, Open-RMF 승강기 상태의 운영 모드에는 화재·비상이 포함된다.",
      "tag": "사실",
      "source_ids": [
        "ref-314",
        "ref-315",
        "ref-286"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "C. 연결·실행 기반 페이지 G 연결 항목과 같은 각주. 승강기 탑승 안전과 설비 안전 제어 자체는 분류 원문 9장 시설·설비 제어 경계의 연계 대상. (재인용: 2026-09-25-38)",
      "as_of": "2021-11",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f10",
      "claim": "G. 안전·보안·지능·거버넌스의 26. 사이버보안·접근권한·개인정보 ↔ C. 연결·실행 기반의 9. 로봇·제조사 관제 연동·11. 분산 시스템·통신·컴퓨팅 구조: ROS 2 는 DDS 보안 규격의 인증·접근통제·암호화 플러그인을 쓰고, Open-RMF 는 같은 신원과 접근통제 규칙을 공유하는 SROS 2 인클레이브로 구성요소 권한을 나누며 웹 대시보드에는 TLS 와 OpenID Connect 기반 역할 토큰을 쓴다.",
      "tag": "사실",
      "source_ids": [
        "ref-009",
        "ref-405"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Open-RMF 보안 문서: \"An 'enclave' is a process or group of processes that will share the same identity and access control rules.\" 대시보드는 TLS·OIDC(Keycloak), 역할별 ID 토큰.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f11",
      "claim": "G. 안전·보안·지능·거버넌스의 26. 사이버보안·접근권한·개인정보 ↔ C. 연결·실행 기반의 9. 로봇·제조사 관제 연동: VDA 5050 3.0.0 은 MQTT 용 TLS 자격증명을 내려받는 사전 정의 동작 updateCertificate 를 두고, 내려받기도 TLS 로 보호하고 인증서 체인을 검증하도록 권하므로, 인증서 교체가 관제 연동 경로를 거치는 보안 명령이 된다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "VDA 5050 6.2.3.1 사전 정의 동작 updateCertificate. 명세는 보안 기구 전체는 범위 밖으로 둔다. 26. 사이버보안·접근권한·개인정보 9절의 '보안 명령 조율' [추정]의 근거.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "G. 안전·보안·지능·거버넌스의 26. 사이버보안·접근권한·개인정보 ↔ C. 연결·실행 기반의 9. 로봇·제조사 관제 연동: ROS 2 위협 모델 초안은 기본 사용자명·암호가 설정된 이미지의 SSH 접속을 진입점으로 들고, CISA 권고(ICSA-21-280-02)는 MiR 차량과 플릿 소프트웨어 취약점으로 로봇 제어와 서비스 거부가 가능하다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-010",
        "ref-583"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "위협 모델(DRAFT, 최종 수정 2021-01): \"Many images are setup with a default username and password.\" CISA 권고 내용은 26. 사이버보안·접근권한·개인정보 5절 기준(원문 미열람).",
      "as_of": "2021-01",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f13",
      "claim": "G. 안전·보안·지능·거버넌스의 26. 사이버보안·접근권한·개인정보 ↔ C. 연결·실행 기반의 10. 설비·건물 시스템 연동: 로봇 관제가 문·승강기 어댑터에 요청을 보내는 구조에서는 어느 관제 구성요소가 어떤 설비 명령을 낼 수 있는지를 인클레이브·권한 파일 같은 접근통제 단위로 정해야 할 것으로 보이며, 공개 구성·사례는 확인되지 않았다.",
      "tag": "추정",
      "source_ids": [
        "ref-405",
        "ref-283",
        "ref-284"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "C. 연결·실행 기반 페이지 G 연결 항목과 같은 주장. 관련 열린 질문 oq-043·oq-056. (재인용: 2026-09-25-38)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f14",
      "claim": "G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ C. 연결·실행 기반의 12. 명령·작업 실행의 신뢰성: VDA 5050 3.0.0 상태 메시지의 safetyState 는 비상정지 종류(eStop)와 보호 필드 침범(fieldViolation)을 보고하며, 명세는 스스로 기능·운영·시스템 안전 요구를 정하지 않고 안전 표준으로 적용해서는 안 된다고 밝힌다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "VDA 5050 2장 범위: \"does not define functional, operational, or system safety requirements and shall not be regarded or applied as a safety standard.\"",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f15",
      "claim": "G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ C. 연결·실행 기반의 12. 명령·작업 실행의 신뢰성: ROP 는 로봇이 보고한 안전 상태가 해제되고 운용 모드가 자동으로 돌아온 뒤 재개를 지시하는 운영 조율을 맡고, 정지·재개 지시를 확실하게 전달하는 문제가 12. 명령·작업 실행의 신뢰성과 맞물리는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "25. 안전·위험 관리 5절 피킹 시나리오와 10절 연결의 [추정] 주장. 원격 비상정지 지시 경로의 성능 수준 요구 여부는 oq-095 로 열림.",
      "as_of": "2026-09-25",
      "flow_step": "피킹",
      "flow_item": "제약"
    },
    {
      "id": "f16",
      "claim": "G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스 ↔ C. 연결·실행 기반의 9. 로봇·제조사 관제 연동: VDA 5050 3.0.0 은 경로 계산·교착 해소·교통 관리를 관제 기능으로, 위치 추정과 주문 실행을 이동로봇 기능으로 나누며, 제조사 중립 연동의 기준으로 VDA 5050 외에 MassRobotics AMR 상호운용 표준과 ISO 21423 이 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-031",
        "ref-253",
        "ref-159"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "VDA 5050 5.3~5.4 관제·이동로봇 기능 구분(원문 열람). MassRobotics·ISO 21423 은 C. 연결·실행 기반 페이지 G 연결 항목 기준(원문 미열람).",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f17",
      "claim": "G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스 ↔ C. 연결·실행 기반의 9. 로봇·제조사 관제 연동: 확인한 VDA 5050 적합성 시험 근거가 제3자 오픈소스 도구와 벤더 발표뿐이라, 어느 시험 결과를 연동 승인 기준으로 삼고 누가 연동 오류를 판정할지가 거버넌스 과제로 넘어갈 것으로 보이며, 공식 인증 절차의 부재는 확정되지 않았다.",
      "tag": "추정",
      "source_ids": [
        "ref-407",
        "ref-408",
        "ref-608",
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "C. 연결·실행 기반·F. 도입·검증·유지관리 페이지의 같은 [추정] 주장. OTTO 인증 발표는 벤더 주장이며 시험 항목 미확인(oq-055).",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f18",
      "claim": "G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스 ↔ C. 연결·실행 기반의 10. 설비·건물 시스템 연동: 국내에서 로봇 엘리베이터 탑승 KS 가 제정되었고, 대한승강기협회가 엘리베이터와 로봇 연동 단체표준을 제정했다고 기사로 전해져, 설비 연동 표준이 두 대분류를 잇는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-709",
        "ref-316",
        "ref-317"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "단체표준 원문·발행일 미확인(기사 보도 기준). 메시지 내용은 oq-041 로 열림.",
      "as_of": "2021-11-11",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f19",
      "claim": "G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영 ↔ C. 연결·실행 기반의 9. 로봇·제조사 관제 연동: 오픈소스 ROS-MCP-Server 는 rosbridge 를 통해 LLM 에게 ROS 토픽 발행·구독, 서비스·액션 호출, 파라미터 설정을 도구로 노출하며, README 는 권한 기능을 앞으로 기여받을 기능으로만 언급한다.",
      "tag": "사실",
      "source_ids": [
        "ref-679"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: \"publish & subscribe to topics, call services & actions, set parameters, read sensor data, and monitor robot state in real time.\" 기여 안내에 'permissions' 가 새 기능 후보로 적힘.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영·26. 사이버보안·접근권한·개인정보 ↔ C. 연결·실행 기반의 12. 명령·작업 실행의 신뢰성: LLM 에 저수준 로봇 도구를 직접 열면 명령 상태 관리와 실행 전 검증을 우회할 수 있으므로, ROP 는 검증 경로로 들어가는 상위 도구(작업 요청 제출 등)만 노출해야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-679",
        "ref-417"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "트랙 nl-task-chatbot 단계 3 finding f20 의 종합 판단을 대분류 연결로 옮김. 검증 전 트랙 추정이다. (재인용: 2026-09-25-71)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f21",
      "claim": "G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영 ↔ C. 연결·실행 기반의 12. 명령·작업 실행의 신뢰성: Tang 외(2026-06, 프리프린트)는 산업용 다중 로봇에서 LLM 에이전트의 제안이 결정적 검증과 원자적 반영(atomic commit)을 거쳐야만 실행 상태·자원 잠금 기록에 받아들여지는 구조를 제안했다.",
      "tag": "사실",
      "source_ids": [
        "ref-677"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Verification-Gated Agentic Mission-State Governance(arXiv 2606.31339). 산업용 다중 로봇 대상이며 물류 적용 미확인. (재인용: 2026-09-25-71)",
      "as_of": "2026-06",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f22",
      "claim": "G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영 ↔ D. 계획·최적화의 13. 작업 배정 — MRTA: 분류 원문 8장 교차 규칙대로 학습 기반 배차 연구(이종 그래프 어텐션 스케줄러, 창고 강화학습 배정 RTAW)와 LLM 기반 다중 로봇 작업 배정 연구가 두 영역을 잇는다.",
      "tag": "사실",
      "source_ids": [
        "ref-399",
        "ref-623",
        "ref-090",
        "ref-168"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "D. 계획·최적화 페이지 G 연결 항목과 27. AI·학습·적응과 모델 운영 5절 근거. LLM 배정 결과 수치는 출처 충돌(oq-030)로 쓰지 않는다.",
      "as_of": "2025-12",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f23",
      "claim": "G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영 ↔ D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF·16. 공용 자원·충전·에너지 최적화: 모방 학습을 적용한 지속형 MAPF 연구(2024-10)와 자율 피킹 로봇의 배터리 관리에 심층 강화학습을 쓰는 연구(2026-07)가 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-199",
        "ref-531"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "D. 계획·최적화 페이지 G 연결 항목 기준. 두 연구 모두 프리프린트, 원문 미열람.",
      "as_of": "2026-07",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f24",
      "claim": "G. 안전·보안·지능·거버넌스의 26. 사이버보안·접근권한·개인정보 ↔ D. 계획·최적화의 13. 작업 배정 — MRTA: 2026-08 프리프린트는 위치 스푸핑으로 오염된 에이전트가 롤아웃 기반 다중 로봇 배정·경로 계획의 비용 개선을 없앨 수 있다고 보고 탐지된 적대 에이전트를 이후 계획에서 빼는 방법을 제안했으며, 실험은 GPS 스푸핑 데이터와 택시 수요로 했다.",
      "tag": "사실",
      "source_ids": [
        "ref-494"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "D. 계획·최적화 페이지 G 연결 항목 기준. 물류센터 적용 미확인. 배정 전 보고값 검증 기준은 oq-082 로 열림.",
      "as_of": "2026-08",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f25",
      "claim": "G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF: VDA 5050 3.0.0 은 진입 금지(BLOCKED)·해제(RELEASE)·속도 제한(SPEED_LIMIT)·우선(PRIORITY)·벌점(PENALTY) 같은 구역 유형을 교통 관리 수단으로 정의하되, 안전 표준으로 적용하지 말라고 밝힌다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "VDA 5050 6.4.1 구역 유형(BLOCKED: \"shall not enter\" 등)과 2장 범위의 안전 표준 부인 문구. 교통 수단과 안전 기능을 구분하는 근거.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "제약"
    },
    {
      "id": "f26",
      "claim": "G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ D. 계획·최적화의 16. 공용 자원·충전·에너지 최적화: Open-RMF 데모는 비상 경보가 켜지면 로봇들을 가장 가까운 주차 위치로 보내고, 2025-04-04 기능 요청 이슈 기준 비상 신호는 대상 플릿을 구분하지 않는 불리언 값이었다.",
      "tag": "사실",
      "source_ids": [
        "ref-104",
        "ref-567"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "rmf_demos README·open-rmf/rmf 이슈 #658. 이후 구현 여부 미확인. 주차 위치 배분이 공용 자원 문제와 겹친다.",
      "as_of": "2025-04-04",
      "flow_step": "출하",
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f27",
      "claim": "G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF: Open-RMF 는 긴급 작업을 높은 우선순위 참여자가 교통 협상을 강제하는 방식으로 다룬다.",
      "tag": "사실",
      "source_ids": [
        "ref-004"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "25. 안전·위험 관리 5절 출하 시나리오 제약 칸과 10절 15. 다중 로봇 경로·교통 관리 — MAPF 연결의 근거(RMF Core Overview).",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f28",
      "claim": "G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스 ↔ D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF: VDA 5050 은 교통 조율 전략을 명세에서 빼고 Open-RMF 는 시스템 통합사가 배치한 판정자가 협상 결과를 고르게 하므로, 한 현장의 우선권 판정 규칙을 누가 정하고 승인하는지가 거버넌스 과제로 넘어갈 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-004"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "D. 계획·최적화 페이지 G 연결 항목의 [추정] 주장(oq-057). (재인용: 2026-09-25-55)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f29",
      "claim": "G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ E. 협업·현장 운영의 17. 로봇 간 협업·물리적 인계: ANSI/A3 R15.08-2-2023 은 이동 플랫폼에 로봇팔을 단 모바일 매니퓰레이터를 산업용 이동로봇 유형 C 로 다루며 시스템·적용 단위의 안전 요구를 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-210",
        "ref-472"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "E. 협업·현장 운영 페이지 G 연결 항목 기준(원문 미열람). 국내 대응 KS 여부는 oq-064.",
      "as_of": "2023-10",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f30",
      "claim": "G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ E. 협업·현장 운영의 17. 로봇 간 협업·물리적 인계·18. 사람–로봇 협업·운영 인터페이스: 사람 감지·보호 필드·비상정지 같은 안전 기능은 제조사·통합사·설비 쪽 연계 대상이고, ROP 는 로봇이 보고한 안전 상태를 표시하고 재개·수동 전환 승인을 작업 흐름에 반영하는 경계로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-470",
        "ref-051",
        "ref-210"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "E. 협업·현장 운영 페이지 G 연결 항목과 25. 안전·위험 관리 9절의 [추정] 경계. (재인용: 2026-09-25-60)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f31",
      "claim": "G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ E. 협업·현장 운영의 18. 사람–로봇 협업·운영 인터페이스(국내): 고용노동부는 2023-07 고정식·이동식 산업용 로봇의 협동작업 안전 가이드를 배포했고, 중소벤처기업부는 2024-11 이동식 협동로봇 안전기준 산업표준 제정을 발표했다.",
      "tag": "사실",
      "source_ids": [
        "ref-473",
        "ref-475",
        "ref-561"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "게시물 제목·요약 기준(원문 미열람). 제정 KS 번호·내용은 oq-070 로 열림.",
      "as_of": "2024-11",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f32",
      "claim": "G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영·25. 안전·위험 관리 ↔ E. 협업·현장 운영의 18. 사람–로봇 협업·운영 인터페이스: LLM 계획기가 불확실할 때 사람에게 되묻는 연구(KnowNo, 2023-07), 사용자 명령의 모호성을 해소하는 연구(CLARA, 2024), 자연어 명령의 실행 전 안전 게이트 연구(SafeGate, 2026-04)가 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-351",
        "ref-353",
        "ref-417"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "E. 협업·현장 운영 페이지 G 연결 항목과 25·27 페이지 근거. 실험 환경은 물류 현장이 아님.",
      "as_of": "2026-04",
      "flow_step": "피킹",
      "flow_item": "시작 조건",
      "source_unopened": true
    },
    {
      "id": "f33",
      "claim": "G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영 ↔ E. 협업·현장 운영의 19. 모니터링·이상 탐지·원인 분석: Das 외(2021-01)는 로봇 실패 설명을 생성해 사용자의 고장 복구 지원을 개선하는 연구를 발표했으며, 분류 원문 8장 교차 규칙의 장애 분석이 두 대분류를 잇는다.",
      "tag": "사실",
      "source_ids": [
        "ref-476"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Explainable AI for Robot Failures(2021-01). E. 협업·현장 운영 페이지 G 연결 항목과 같은 각주. (재인용: 2026-09-25-60)",
      "as_of": "2021-01",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f34",
      "claim": "G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스 ↔ E. 협업·현장 운영의 19. 모니터링·이상 탐지·원인 분석: VDA 5050 오류 수준, MassRobotics 운용 상태, Open-RMF 작업 상태가 서로 다른 어휘이고 공통 매핑 표준이 확인되지 않아, 이종 플릿의 오류·원인 범주 해석 규칙을 누가 정하고 바꾸는지가 거버넌스 과제로 넘어갈 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-051",
        "ref-230",
        "ref-111"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "E. 협업·현장 운영 페이지 G 연결 항목의 [추정] 주장(oq-033, oq-073). (재인용: 2026-09-25-60)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f35",
      "claim": "G. 안전·보안·지능·거버넌스의 26. 사이버보안·접근권한·개인정보 ↔ E. 협업·현장 운영의 18. 사람–로봇 협업·운영 인터페이스: 근로자참여 및 협력증진에 관한 법률 제20조는 사업장 내 근로자 감시 설비의 설치를 노사협의회 협의 사항으로 두어, 카메라를 단 로봇이 작업자를 촬영하는 현장에서 영상 수집 조건이 사람–로봇 협업의 제약이 된다.",
      "tag": "사실",
      "source_ids": [
        "ref-589",
        "ref-010"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "26. 사이버보안·접근권한·개인정보 5절 입고 시나리오 제약 칸(호 번호 미확인). 위협 모델은 카메라 영상을 사적 데이터로 분류. 적용 해석은 oq-099.",
      "as_of": "2026-09-25",
      "flow_step": "입고",
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f36",
      "claim": "G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ E. 협업·현장 운영의 20. 예외 복구·재계획·업무 연속성: 비상 해제 후 어떤 작업을 어떤 순서로 재개할지와 대상 플릿 구분이 출하 마감 준수에 영향을 주므로, 비상 대응 뒤의 재개가 예외 복구 과제로 넘어가는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-567",
        "ref-004"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "25. 안전·위험 관리 5절 출하 시나리오 예외·성과 칸의 [추정] 주장.",
      "as_of": "2026-09-25",
      "flow_step": "출하",
      "flow_item": "예외·성과",
      "source_unopened": false
    },
    {
      "id": "f37",
      "claim": "G. 안전·보안·지능·거버넌스의 26. 사이버보안·접근권한·개인정보 ↔ E. 협업·현장 운영의 20. 예외 복구·재계획·업무 연속성: 출하 마감 중 오류 로봇을 제조사 원격 유지보수로 복구하려 할 때, 대상 로봇·진단 명령만 허용하고 이동 명령은 막으며 세션을 감사 기록으로 남기는 권한 제약이 복구 속도와 맞물릴 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-010",
        "ref-583",
        "ref-405"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "26. 사이버보안·접근권한·개인정보 5절 원격 유지보수 시나리오의 [추정] 주장. 로봇·명령 단위 권한 매트릭스 공개 표준은 미확인(oq-100).",
      "as_of": "2026-09-25",
      "flow_step": "출하",
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f38",
      "claim": "연계 대상: G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ F. 도입·검증·유지관리의 21. 온보딩·설정·현장 시운전·23. 시험·형식 검증·벤치마크 — ISO 3691-4:2023 은 무인 산업 차량과 그 시스템의 안전 요구와 검증 수단을 정하고 운용 구역 준비를 부속서 A 에 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-470"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "25. 안전·위험 관리 4절과 F. 도입·검증·유지관리 페이지 G 연결 항목 기준(원문 미열람). 세부 시험 항목 미확인.",
      "as_of": "2023-06",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f39",
      "claim": "G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ F. 도입·검증·유지관리의 24. 자산·소프트웨어 수명주기 관리: 업체 가이드가 설비·작업 변경 시 위험성평가를 다시 하도록 권하므로 펌웨어·안전 파라미터·오케스트레이션 정책 변경이 재평가 촉발 조건이 될 수 있어 보이나, 국내 공식 규정은 확인되지 않았다.",
      "tag": "추정",
      "source_ids": [
        "ref-559"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "F. 도입·검증·유지관리 페이지 G 연결 항목의 [추정] 주장(oq-092, oq-093). 근거가 업체 자료 하나다.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f40",
      "claim": "G. 안전·보안·지능·거버넌스의 26. 사이버보안·접근권한·개인정보 ↔ F. 도입·검증·유지관리의 24. 자산·소프트웨어 수명주기 관리: IEC TR 62443-2-3:2015 는 산업 자동화·제어 시스템 환경의 패치 관리를 다루고, ROS 2 위협 모델 초안은 빌드 팜·개발자 작업 환경을 통한 공급망 위협에 바이너리 서명과 소스 감사를 완화책으로 든다.",
      "tag": "사실",
      "source_ids": [
        "ref-554",
        "ref-010"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "위협 모델: \"An attacker compromising the build-farm or the developer workstation could introduce a vulnerability in a binary...\" IEC TR 은 F 페이지 기준(원문 미열람).",
      "as_of": "2021-01",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f41",
      "claim": "G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영 ↔ F. 도입·검증·유지관리의 21. 온보딩·설정·현장 시운전·23. 시험·형식 검증·벤치마크: 자연어 능력 설명에서 LLM 으로 능력 온톨로지를 생성하는 방법(2024-06)이 제안되었고, ALFRED 와 LoTa-Bench 는 자연어 지시를 행동 계획으로 바꾸는 체화 에이전트를 시뮬레이터 결과로 자동 평가하는 공개 벤치마크다(물류 지시 데이터셋 아님).",
      "tag": "사실",
      "source_ids": [
        "ref-465",
        "ref-539",
        "ref-541"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "F. 도입·검증·유지관리 페이지 G 연결 항목 기준. 온보딩 현장 적용 사례 미확인.",
      "as_of": "2024-06",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f42",
      "claim": "G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영 ↔ F. 도입·검증·유지관리의 24. 자산·소프트웨어 수명주기 관리: 24. 자산·소프트웨어 수명주기 관리의 정의가 '모델 버전'과 배포·복구를 포함하므로, 학습 배차 모델 교체를 모델 레지스트리의 버전·별칭과 운영 준비도 시험 기준으로 관리하는 일이 두 대분류를 잇는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-626",
        "ref-625"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "27. AI·학습·적응과 모델 운영 5절 출하 시나리오 예외·성과 칸의 [추정] 주장과 분류 원문 24 정의의 '모델 버전'. 어느 대분류 페이지에도 아직 없는 연결.",
      "as_of": "2026-09-25",
      "flow_step": "출하",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f43",
      "claim": "G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스 ↔ F. 도입·검증·유지관리의 22. 시뮬레이션·예측용 디지털 트윈: 제조용 디지털 트윈 프레임워크 ISO 23247 은 국내에 KS X ISO 23247-1 로 등재되어 있고 2026 년 디지털 트윈 결합을 다루는 Part 6 이 발행되었으나, 제조 대상 표준이다.",
      "tag": "사실",
      "source_ids": [
        "ref-516",
        "ref-518"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "F. 도입·검증·유지관리 페이지 G 연결 항목 기준. 물류센터 적용 여부는 oq-085.",
      "as_of": "2026",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f44",
      "claim": "G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스 ↔ F. 도입·검증·유지관리의 23. 시험·형식 검증·벤치마크: 국내에는 로봇 자체 성능 시험(KS B ISO 18646-1, 한국로봇산업진흥원 시험평가)과 소프트웨어 모듈 정보모델 상호운용성 시험 절차(KOROS 1148-8:2025)가 있어, 로봇 성능 시험은 시험기관 쪽이고 ROP 몫은 그 결과를 연동 승인·등록 조건으로 받는 쪽으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-606",
        "ref-607",
        "ref-710",
        "ref-466"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "F. 도입·검증·유지관리 페이지 G 연결 항목과 28 페이지 각주. 물류로봇 시험인증 협력은 기사 기준. 관련 oq-089·oq-111.",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f45",
      "claim": "G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스 ↔ F. 도입·검증·유지관리의 24. 자산·소프트웨어 수명주기 관리: 관제가 VDA 5050 헤더 version 으로 판 차이를 감지하고 로봇이 지원하지 않는 선택 필드는 UNSUPPORTED_PARAMETER 오류로 드러나므로, 펌웨어·프로토콜 판 이행 때 호환 시험과 수정 책임을 누가 지는지가 두 대분류 사이의 과제로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-051",
        "ref-635"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "28. 표준·상호운용성·다사업자 거버넌스 5절 출하 시나리오 예외·성과 칸의 [추정] 주장. 2.x·3.0.0 혼재 운영은 oq-091.",
      "as_of": "2026-09-25",
      "flow_step": "출하",
      "flow_item": "예외·성과",
      "source_unopened": false
    }
  ],
  "sources": [
    {
      "id": "ref-004",
      "org": "Open Robotics",
      "title": "RMF Core Overview — Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/rmf-core.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "RMF 교통 스케줄·협상·긴급 작업 우선 협상 구조(이전 실행에서 원문 열람, 이번 실행 재열람 안 함).",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-009",
      "org": "ROS 2 Design",
      "title": "ROS 2 DDS-Security Integration",
      "published": null,
      "url": "https://design.ros2.org/articles/ros2_dds_security.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. ROS 2 의 DDS-Security 인증·접근통제·암호화 플러그인 통합 설계(이번 실행 재열람 안 함).",
      "source_unopened": false,
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null
    },
    {
      "id": "ref-010",
      "org": "ROS 2 Design",
      "title": "ROS 2 Robotic Systems Threat Model",
      "published": null,
      "url": "https://design.ros2.org/articles/ros2_threat_model.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "ROS 2 로봇 시스템 위협 모델 초안(최종 수정 2021-01). 기본 자격증명 SSH, 카메라 영상·로그 민감 자산, 빌드 팜 공급망 위협과 감사·서명 완화책.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/ros2/design/gh-pages/articles/183_ros2_threat_model.md",
      "source_unopened": false
    },
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "VDA 5050 3.0.0 명세. 안전 표준 부인 문구, safetyState, updateCertificate, 관제·로봇 기능 구분, 구역 유형을 이번 실행에서 원문으로 확인.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/VDA5050_EN.md",
      "source_unopened": false
    },
    {
      "id": "ref-051",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/state.schema",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. VDA 5050 상태 메시지 JSON 스키마(오류 수준·운용 모드·적재물·배터리 필드).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-076",
      "org": "DeFazio, D., Mehta, H., Wang, M., Yang, P., Blackburn, J., & Zhang, S.",
      "title": "Vision Language Models Can Parse Floor Plan Maps",
      "published": "2024-09",
      "url": "https://arxiv.org/abs/2409.12842",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 비전 언어 모델로 평면도 지도를 해석하는 연구.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-090",
      "org": "Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C.",
      "title": "SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models",
      "published": "2023-09",
      "url": "https://arxiv.org/abs/2309.10062",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. LLM 기반 다중 로봇 작업 계획·배정.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-104",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_demos — Demonstrations of Open-RMF (README)",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_demos",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. Open-RMF 데모 구성과 비상 경보 시 주차 동작.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-111",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_api_msgs — rmf_api_msgs/schemas/task_state.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. Open-RMF 작업 상태 스키마.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-125",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_api_msgs — rmf_api_msgs/schemas/task_request.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. Open-RMF 작업 요청 스키마.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-129",
      "org": "MESA International",
      "title": "B2MML-BatchML/Schema/B2MML-TransactionProfile.xsd",
      "published": "2023",
      "url": "https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-TransactionProfile.xsd",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. B2MML 거래 동사(CHANGE·CANCEL 등) 정의.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-130",
      "org": "OPC Foundation",
      "title": "UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv)",
      "published": "2024-01-31",
      "url": "https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. OPC UA for ISA-95 Job Control 작업 지시 메서드.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-138",
      "org": "국가표준인증통합정보시스템(KSSN)",
      "title": "KS B 7321-2 로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델",
      "published": null,
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010147546",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 서비스 로봇 소프트웨어 모듈 정보 모델 KS.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-159",
      "org": "ISO",
      "title": "ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability",
      "published": null,
      "url": "https://www.iso.org/standard/86749.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 산업용 이동로봇 통신·상호운용성 국제표준(발행 여부 미확인).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-168",
      "org": "Kaitha, S., & Yu, S. 외(arXiv 2512.02810)",
      "title": "Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms",
      "published": "2025-12",
      "url": "https://arxiv.org/abs/2512.02810",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. LLM 기반 로봇 작업 배정 벤치마크(결과 수치 출처 충돌, oq-030).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-199",
      "org": "arXiv 2410.21415 저자(미확인)",
      "title": "Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding",
      "published": "2024-10",
      "url": "https://arxiv.org/abs/2410.21415",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 모방 학습 기반 지속형 MAPF.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-210",
      "org": "ANSI / A3(Association for Advancing Automation)",
      "title": "ANSI/A3 R15.08-2-2023 - Industrial Mobile Robots - Safety Requirements - Part 2: Requirements for IMR system(s) and IMR application(s)",
      "published": "2023",
      "url": "https://webstore.ansi.org/standards/ria/ansia3r15082023",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 산업용 이동로봇 시스템·적용 안전 요구(유형 C 모바일 매니퓰레이터 포함).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-230",
      "org": "MassRobotics",
      "title": "MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json",
      "published": null,
      "url": "https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. MassRobotics 상태 보고 JSON 스키마(운용 상태 어휘).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-234",
      "org": "IDTA(Industrial Digital Twin Association)",
      "title": "IDTA 02047 Technical Data for Automated Guided Vehicles 1.0 — README (admin-shell-io/submodel-templates)",
      "published": null,
      "url": "https://github.com/admin-shell-io/submodel-templates/tree/main/published/Technical%20Data%20for%20Automated%20Guided%20Vehicles",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 무인운반차 기술 데이터 서브모델.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-238",
      "org": "Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A.",
      "title": "On the Use of Large Language Models to Generate Capability Ontologies",
      "published": "2024-04",
      "url": "https://arxiv.org/abs/2404.17524",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. LLM 으로 능력 온톨로지 생성.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-239",
      "org": "Dussard, B., & Sarthou, G. (LAAS-CNRS)",
      "title": "Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF",
      "published": "2026-06",
      "url": "https://arxiv.org/abs/2606.17073",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. URDF 에서 로봇 온톨로지를 LLM 으로 채우는 연구.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-240",
      "org": "ISO",
      "title": "ISO 22166-201:2024 - Robotics — Modularity for service robots — Part 201: Common information model for modules",
      "published": "2024-02",
      "url": "https://www.iso.org/standard/82334.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 서비스 로봇 모듈 공통 정보 모델.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-253",
      "org": "MassRobotics",
      "title": "MassRobotics-AMR/AMR_Interop_Standard — README",
      "published": null,
      "url": "https://github.com/MassRobotics-AMR/AMR_Interop_Standard",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. MassRobotics AMR 상호운용 표준 저장소(신원·상태 보고).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-283",
      "org": "Open Robotics",
      "title": "Doors (integration_doors) - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/integration_doors.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. Open-RMF 문 연동.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-284",
      "org": "Open Robotics",
      "title": "Lifts (integration_lifts) - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/integration_lifts.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. Open-RMF 승강기 연동.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-286",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 승강기 상태 메시지(층 이름, 운영 모드).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-314",
      "org": "국가표준인증통합정보시스템(KSSN)",
      "title": "KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법",
      "published": "2021-11",
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010135682",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 이동 로봇 엘리베이터 탑승 안전 KS.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-315",
      "org": "산업통상자원부 국가기술표준원(대한민국 정책브리핑)",
      "title": "국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다",
      "published": "2021-11",
      "url": "https://www.korea.kr/briefing/pressReleaseView.do?newsId=156480155",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 로봇 엘리베이터 탑승 KS 제정 보도자료.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-316",
      "org": "건설기술신문",
      "title": "승강기협, 엘리베이터-로봇 연동 단체표준 제정",
      "published": null,
      "url": "https://www.ctman.kr/35296",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 대한승강기협회 엘리베이터–로봇 연동 단체표준 제정 기사.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-317",
      "org": "전기신문",
      "title": "승강기협회 '로봇-승강기 연동 표준개발'로 승강기 4차산업 견인",
      "published": null,
      "url": "https://www.electimes.com/news/articleView.html?idxno=320147",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 로봇–승강기 연동 표준 개발 기사.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-351",
      "org": "Ren, A. Z. 외",
      "title": "Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners",
      "published": "2023-07",
      "url": "https://arxiv.org/abs/2307.01928",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. KnowNo: 등각 예측 기반으로 불확실할 때 사람에게 묻는 LLM 계획기.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-353",
      "org": "Park, J., Lim, S., Lee, J., Park, S., Chang, M., Yu, Y., & Choi, S.",
      "title": "CLARA: Classifying and Disambiguating User Commands for Reliable Interactive Robotic Agents",
      "published": "2024",
      "url": "https://arxiv.org/abs/2306.10376",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 사용자 명령 분류·모호성 해소.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-399",
      "org": "Wang, Z., & Gombolay, M.",
      "title": "Heterogeneous graph attention networks for scalable multi-robot scheduling with temporospatial constraints",
      "published": null,
      "url": "https://link.springer.com/article/10.1007/s10514-021-09997-2",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 학습 기반 다중 로봇 스케줄링.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-405",
      "org": "Open Robotics",
      "title": "Security - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/security.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "RMF 의 SROS 2 인클레이브·서명 권한 파일, 대시보드 TLS·OIDC 역할 토큰.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/security.md",
      "source_unopened": false
    },
    {
      "id": "ref-407",
      "org": "gpue (GitHub)",
      "title": "vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS)",
      "published": null,
      "url": "https://github.com/gpue/vda5050-sim",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. VDA 5050 3.0.0 시뮬레이터와 적합성 시험 묶음(개인 프로젝트).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-408",
      "org": "ekusiadadus (GitHub)",
      "title": "vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces)",
      "published": null,
      "url": "https://github.com/ekusiadadus/vda5050-lab",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. MQTT 기록 기반 VDA 5050 진단 도구(개인 프로젝트).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-417",
      "org": "Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab)",
      "title": "Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems",
      "published": "2026-04",
      "url": "https://arxiv.org/abs/2604.05427",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. SafeGate: 자연어 명령 실행 전 결정적 안전 판정과 작업 안전 계약.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-465",
      "org": "Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A.",
      "title": "Toward a Method to Generate Capability Ontologies from Natural Language Descriptions",
      "published": "2024-06",
      "url": "https://arxiv.org/abs/2406.07962",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 자연어 능력 설명에서 LLM 으로 능력 온톨로지 생성.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-466",
      "org": "부산일보",
      "title": "KTL·통합물류협회 ‘물류로봇 시험인증’ 협력 강화 ‘맞손’",
      "published": "2026-07-24",
      "url": "https://www.busan.com/view/busan/view.php?code=2026072420194685883",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. KTL·통합물류협회 물류로봇 시험인증 협력 기사.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-470",
      "org": "ISO",
      "title": "ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems",
      "published": "2023-06",
      "url": "https://www.iso.org/standard/83545.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 무인 산업 차량과 시스템의 안전 요구·검증, 운용 구역 부속서 A.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-472",
      "org": "A3(Association for Advancing Automation)",
      "title": "ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available",
      "published": "2023-10",
      "url": "https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. R15.08-2 발행 안내.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-473",
      "org": "고용노동부",
      "title": "고정식 이동식 산업용 로봇의 협동작업 안전 가이드 배포",
      "published": "2023-07",
      "url": "https://www.moel.go.kr/policy/policydata/view.do?bbs_seq=20230700065",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 산업용 로봇 협동작업 안전 가이드 배포 게시물.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-475",
      "org": "중소벤처기업부(대한민국 정책브리핑)",
      "title": "｢대구 이동식 협동로봇 규제자유특구｣ 산업표준 제정으로, 이동식 협동로봇 상용화 길 열렸다!",
      "published": "2024-11",
      "url": "https://www.korea.kr/briefing/pressReleaseView.do?newsId=156658517",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 이동식 협동로봇 산업표준 제정 보도자료.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-476",
      "org": "Das, D., Banerjee, S., & Chernova, S.",
      "title": "Explainable AI for Robot Failures: Generating Explanations that Improve User Assistance in Fault Recovery",
      "published": "2021-01",
      "url": "https://arxiv.org/abs/2101.01625",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 로봇 실패 설명 생성으로 고장 복구 지원 개선.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-494",
      "org": "Francos, R. M., Garces, D., Akgün, O. E., Bastian, N. D., & Gil, S.(Harvard·JHU)",
      "title": "Trust-Aware Sequential Decision Making and Rollout Planning for Resilient Multi-Robot Systems",
      "published": "2026-08",
      "url": "https://arxiv.org/abs/2608.25690",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 위치 스푸핑 에이전트를 고려한 신뢰 인지 다중 로봇 배정·계획.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-516",
      "org": "한국표준협회 KSSN(국가표준인증종합정보센터)",
      "title": "KS X ISO 23247-1 자동화 시스템 및 통합 — 제조를 위한 디지털 트윈 프레임워크 — 제1부: 개요 및 일반 원리",
      "published": null,
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010140724",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 제조용 디지털 트윈 프레임워크 KS 부합화 표준.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-518",
      "org": "ISO",
      "title": "ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition",
      "published": "2026",
      "url": "https://www.iso.org/standard/87426.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 디지털 트윈 결합 표준.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-531",
      "org": "arXiv 2607.05683 저자(미확인)",
      "title": "Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers",
      "published": "2026-07",
      "url": "https://arxiv.org/abs/2607.05683",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 자율 피킹 로봇 배터리 관리의 심층 강화학습.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-539",
      "org": "askforalfred (ALFRED 공식 저장소)",
      "title": "ALFRED — A Benchmark for Interpreting Grounded Instructions for Everyday Tasks (GitHub README)",
      "published": null,
      "url": "https://github.com/askforalfred/alfred",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 자연어 지시 기반 체화 에이전트 벤치마크.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-541",
      "org": "lbaa2022 (LoTa-Bench 공식 저장소)",
      "title": "LLMTaskPlanning — LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents (ICLR 2024) (GitHub README)",
      "published": null,
      "url": "https://github.com/lbaa2022/LLMTaskPlanning",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 언어 기반 작업 계획기 자동 평가 벤치마크.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-554",
      "org": "IEC",
      "title": "IEC TR 62443-2-3:2015 Security for industrial automation and control systems - Part 2-3: Patch management in the IACS environment",
      "published": "2015-06",
      "url": "https://webstore.iec.ch/en/publication/22811",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. IACS 환경 패치 관리 기술 보고서.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-559",
      "org": "세이프틱스(Safetics)",
      "title": "로봇 시스템 위험성평가 가이드",
      "published": null,
      "url": "https://doc.safetics.io/insight-risk-assessment/",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 업체의 로봇 시스템 위험성평가 가이드(변경 시 재평가 권고).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-561",
      "org": "대한민국 정책브리핑(중소벤처기업부)",
      "title": "이동식 협동로봇 ‘안전기준 산업표준’ 제정…상용화 길 열어",
      "published": "2024-11-03",
      "url": "https://www.korea.kr/news/policyNewsView.do?newsId=148935814",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 이동식 협동로봇 안전기준 산업표준 제정 소식.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-567",
      "org": "Open-RMF (open-rmf/rmf GitHub)",
      "title": "[Feature request]: Fire alarm separation for different fleets · Issue #658 · open-rmf/rmf",
      "published": "2025-04-04",
      "url": "https://github.com/open-rmf/rmf/issues/658",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 화재경보 시 로봇 주차와 플릿별 구분 기능 요청.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-583",
      "org": "CISA",
      "title": "Mobile Industrial Robots Vehicles and MiR Fleet Software (ICSA-21-280-02)",
      "published": null,
      "url": "https://www.cisa.gov/news-events/ics-advisories/icsa-21-280-02",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. MiR 차량·플릿 소프트웨어 취약점 권고.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-589",
      "org": "법제처 국가법령정보센터",
      "title": "근로자참여 및 협력증진에 관한 법률",
      "published": null,
      "url": "https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=105636",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 제20조 노사협의회 협의 사항(근로자 감시 설비 설치).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-606",
      "org": "한국표준협회 KSSN(국가표준인증종합정보센터)",
      "title": "KS B ISO 18646-1 로봇 — 서비스 로봇의 성능 기준 및 관련 시험방법 — 제1부 : 바퀴형 로봇의 이동능력",
      "published": null,
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010113281",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 바퀴형 서비스 로봇 이동 성능 시험방법 KS.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-607",
      "org": "한국로봇산업진흥원(KIRIA)",
      "title": "시험평가 — KIRIA 첨단로봇 실증지원 디지털 플랫폼",
      "published": null,
      "url": "https://kiria.org/rp/kiria/tva/inr/page.dn",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 한국로봇산업진흥원 시험평가 서비스 안내.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-608",
      "org": "OTTO by Rockwell Automation",
      "title": "OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments",
      "published": "2026-04",
      "url": "https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. VDA 5050 인증 취득 벤더 발표(시험 항목 미확인).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-618",
      "org": "ISO/IEC",
      "title": "ISO/IEC 42001:2023 - AI management systems",
      "published": "2023",
      "url": "https://www.iso.org/standard/42001",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. AI 관리 시스템 표준.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-623",
      "org": "Agrawal, A. 외",
      "title": "RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments",
      "published": "2022-09",
      "url": "https://arxiv.org/abs/2209.05738",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 창고 다중 로봇 작업 배정 강화학습(시뮬레이션 창고).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-625",
      "org": "Breck, E. 외 (Google Research)",
      "title": "The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction",
      "published": "2017",
      "url": "https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. ML 운영 준비도 시험 기준.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-626",
      "org": "MLflow (Linux Foundation 오픈소스 프로젝트)",
      "title": "ML Model Registry | MLflow AI Platform",
      "published": null,
      "url": "https://mlflow.org/docs/latest/ml/model-registry/",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 모델 레지스트리의 버전·별칭 관리.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-635",
      "org": "Semantic Versioning (Tom Preston-Werner, semver.org)",
      "title": "Semantic Versioning 2.0.0",
      "published": null,
      "url": "https://semver.org/spec/v2.0.0.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 의미적 버전 관리 규칙(이전 실행에서 열람, 이번 실행 재열람 안 함).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-677",
      "org": "Tang, G. 외(arXiv 2606.31339)",
      "title": "Verification-Gated Agentic Mission-State Governance for Intelligent Industrial Multi-Robot Systems",
      "published": "2026-06",
      "url": "https://arxiv.org/abs/2606.31339",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. LLM 제안의 결정적 검증과 원자적 반영을 거치는 관리형 블랙보드 구조.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-679",
      "org": "robotmcp (ROS-MCP-Server 공식 저장소)",
      "title": "ros-mcp-server — Connect AI models like Claude & GPT with robots using MCP and ROS (GitHub README)",
      "published": null,
      "url": "https://github.com/robotmcp/ros-mcp-server",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "rosbridge 로 LLM 에 ROS 토픽·서비스·액션·파라미터를 도구로 노출. 권한 기능은 향후 기여 항목.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/robotmcp/ros-mcp-server/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-706",
      "org": "IETF (RFC Editor)",
      "title": "RFC 9745: The Deprecation HTTP Response Header Field",
      "published": null,
      "url": "https://www.rfc-editor.org/info/rfc9745/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. API 폐기 예고 HTTP 헤더.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-709",
      "org": "대한민국 정책브리핑(산업통상자원부 국가기술표준원)",
      "title": "국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다",
      "published": "2021-11-11",
      "url": "https://korea.kr/news/pressReleaseView.do?newsId=156480155",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 로봇 엘리베이터 탑승 KS 제정 발표(속도 제어·보호 정지 등).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-710",
      "org": "한국지능형로봇표준포럼(KOROS)",
      "title": "KOROS 1148-8:2025 서비스 로봇을 위한 모듈 - 제2-8부 : 소프트웨어 모듈용 정보모델 상호운용성 시험 절차",
      "published": "2025-06-04",
      "url": "http://www.koros.or.kr/bbs/board.php?bo_table=notice27&wr_id=223",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 소프트웨어 모듈 정보모델 상호운용성 시험 절차 단체표준.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/g-safety-security-intelligence-and-governance/index.md",
      "sections": [
        "5. 다른 대분류와의 연결"
      ],
      "rationale": "'다른 대분류와의 연결' 절만 채운다(patches replace). A. 업무·공급망 설계: f1·f2·f3 / B. 공통 정보·환경 모델: f4·f5·f6·f7·f8 / C. 연결·실행 기반: f9·f10·f11·f12·f13·f14·f15·f16·f17·f18·f19·f20·f21(C 페이지의 27. AI·학습·적응과 모델 운영 '근거 없음' 갭에 대한 보강 후보 f19~f21) / D. 계획·최적화: f22·f23·f24·f25·f26·f27·f28 / E. 협업·현장 운영: f29~f37(E 페이지가 근거 없음으로 둔 26. 사이버보안·접근권한·개인정보 연결 후보 f35·f37) / F. 도입·검증·유지관리: f38~f45(24. 자산·소프트웨어 수명주기 관리 ↔ 27. AI·학습·적응과 모델 운영 신규 연결 f42). 게시된 A~F 대분류 페이지의 G 쪽 서술과 같은 각주를 재사용해 상호 참조 링크를 둔다. 교차 확인된 연결은 없음. '아직 다루지 않은 연결'에 11. 분산 시스템·통신·컴퓨팅 구조 ↔ 25·27, 7. 화물·재고·자산 식별과 추적 ↔ G, 2·3·4 ↔ 25·26, 14. 작업 순서·스케줄링 ↔ G 를 적는다."
    }
  ],
  "glossary_candidates": [],
  "open_questions_new": [
    "ROP 가 VDA 5050 updateCertificate 같은 보안 명령으로 제조사 로봇의 인증서를 교체할 때, 교체 시점·대상 승인과 실패 시 되돌림 책임은 ROP 사업자·제조사·현장 IT 조직 중 누가 지는가? | 관련 영역: 26. 사이버보안·접근권한·개인정보, 9. 로봇·제조사 관제 연동, 24. 자산·소프트웨어 수명주기 관리 | 근거: f11 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 70,
    "cross_checked_count": 0,
    "unverified": [
      "모든 finding 교차 확인 없음: 연결마다 단일 출처이거나 같은 발행 주체 출처",
      "f19~f21: C. 연결·실행 기반 페이지가 '근거 없음'으로 둔 27. AI·학습·적응과 모델 운영 연결의 보강 후보이며, f20·f21 은 트랙 nl-task-chatbot 실행 2026-09-25-71 의 검증 전 finding 을 재인용",
      "f42: 24. 자산·소프트웨어 수명주기 관리 ↔ 27. AI·학습·적응과 모델 운영 연결은 게시 페이지의 [추정] 주장과 분류 원문 정의에 기댄 새 연결",
      "ref-031 의 '책임 분배는 범위 밖' 문구는 WebFetch 요약에만 나타나 원문 구절을 확인하지 못해 쓰지 않음",
      "ISO 10218-1:2025 사이버보안 조항(5.1.16 로 검색 요약에 나옴)은 G 내부 연결(25↔26)이라 이번 대분류 연결에 쓰지 않았고 oq-102 해결 근거로도 올리지 않음"
    ],
    "scope_violations": [
      "f38: ISO 3691-4 안전 요구는 로봇 자체 안전 기능 쪽이라 '연계 대상: '으로 표시",
      "f8·f9·f26: 승강기·비상 신호 관련 설비 안전 제어는 분류 원문 9장 시설·설비 제어 경계의 연계 대상이며 ROP 는 운영 모드 확인만 맡는다고 claim·excerpt 에 적음",
      "f3: 수요예측 모델은 상위 업무 시스템 경계의 연계 대상으로 명시",
      "f19·f20: 로봇 토픽·액션 직접 제어는 로봇 자체 지능·제어 경계와 맞닿아 ROP 는 상위 도구 노출 경계만 판단"
    ],
    "budget_used": {
      "queries": 1,
      "sources": 0
    },
    "limits": "대분류 연결(category_link) 실행. web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문을 연 출처: ref-031(VDA5050_EN.md), ref-405(security.md), ref-010(ros2 threat model), ref-679(ros-mcp-server README). 나머지 재사용 66건은 이번 실행에서 열지 않아 fetched false·신뢰도 상한 medium. 신규 출처 0건(예약 구간 ref-711~ref-740 미사용), 검색 1회/30(ISO 10218-1:2025 사이버보안 조항 확인용, 결과는 G 내부 연결이라 finding 에 쓰지 않음). 근거는 게시된 25~28 세부영역 페이지와 A~F 대분류 페이지의 G 쪽 연결 서술(검증된 주장·각주)을 재사용했고, 같은 주장은 기존 태그를 유지하거나 낮췄다. 한국어 검색은 하지 않음(국내 근거는 기존 KS·정부 출처 재사용: ref-314·315·473·475·561·589·606·607·709·710). 교차 규칙: 27. AI·학습·적응과 모델 운영 finding 은 적용 대상 5. 로봇 능력·작업 온톨로지(f4), 6. 지도·공간·위치 모델(f5), 13. 작업 배정 — MRTA(f22), 19. 모니터링·이상 탐지·원인 분석(f33), 21. 온보딩·설정·현장 시운전(f41)과 함께 냈다. 8. 실시간 세계 상태·데이터 일관성(f8)과 22. 시뮬레이션·예측용 디지털 트윈(f43)은 섞지 않았다. 정정 요청 없음. 용어 후보 없음(관련 용어는 이미 용어집에 있음). 아직 근거가 없는 연결: 11. 분산 시스템·통신·컴퓨팅 구조 ↔ 25·27, 7. 화물·재고·자산 식별과 추적 ↔ G, 14. 작업 순서·스케줄링 ↔ G, 2·3·4 ↔ 25·26."
  }
}
```

### runs/2026-09-25-73/verification.json

```json
{
  "run_id": "2026-09-25-73",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: A. 업무·공급망 설계 페이지 G 연결 항목의 [추정]과 같은 근거(ref-129·130·031·125). ref-129·130·125 원문 미열람. 표준 매핑이 없다는 것은 조사 범위의 관찰이다(oq-020)."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 28. 표준·상호운용성·다사업자 거버넌스 9절 '상위 업무 시스템' 행의 [추정](ref-635·706)과 같다. VDA 5050 원문 1장도 의미적 버전 관리를 쓴다. ref-635·706 이번 실행 원문 미열람."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 27. AI·학습·적응과 모델 운영 9절 표와 도입 문단의 [추정](ref-618·626)과 같다. 수요예측이 연계 대상이라는 부분은 분류 원문 9장 상위 업무 시스템 경계에서 온다. 두 출처 모두 원문 미열람."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: B. 공통 정보·환경 모델 페이지 G 연결 항목의 [사실]과 같은 각주(ref-238 2024-04, ref-239 2026-06). 연구 두 건이 각각 단일 출처이고 원문 미열람. 분류 원문 8장 교차 규칙(매뉴얼 해석 → 5. 로봇 능력·작업 온톨로지)에 맞다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: B. 공통 정보·환경 모델 페이지의 [사실](ref-076, 2024-09)과 같다. 원문 미열람. 도면 해석 교차 규칙(6. 지도·공간·위치 모델)에 맞다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: B. 공통 정보·환경 모델 페이지의 [사실](ref-234·240·138)과 같다. 모두 원문 미열람. KS 부합화 여부는 oq-004·oq-026에서 열려 있다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "출처 제목이 ISO 21423의 주제(산업용 이동로봇의 통신·상호운용성)를 확인해 준다. 다만 C. 연결·실행 기반 페이지는 이 표준을 검색 결과상 FDIS 단계로, 발행 여부는 미확인으로 적는다. '국제표준이며'라는 문구는 이미 발행된 것처럼 읽히므로 '발행 여부 미확인'을 덧붙이는 수정을 지시한다. ref-159 원문 미열람."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: B. 공통 정보·환경 모델 페이지 G 연결 항목의 [추정](ref-286)과 같다. ref-286 원문 미열람. 설비 안전 제어를 연계 대상으로 명시했으므로 범위 경계를 지켰다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: C. 연결·실행 기반 페이지 G 연결 항목의 [사실](ref-314·315·286, 2021-11)과 같다. 모두 원문 미열람. ref-315와 ref-709는 같은 국가기술표준원 보도자료를 가리키는 서로 다른 id다(중복 항목 참고)."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문 ref-009에서 인증(Authentication)·접근통제(Access control)·암호화(Cryptographic) 세 플러그인을 확인했다. ref-405 원문(raw security.md)도 이번 검증에서 열어 인클레이브 정의 구절과 대시보드의 TLS·OIDC(Keycloak)·역할이 담긴 서명 ID 토큰을 확인했다. 다만 두 출처의 발행 주체가 같은 계열(Open Robotics/ROS 2)이다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: VDA 5050 원문(raw)을 이번 검증에서 열었다. updateCertificate(service 값 'MQTT')가 있고, 내려받기도 TLS로 보호해야 하며(shall) 활성화 전에 인증서 체인을 검증하는 것이 바람직하다고(advisable) 적혀 있다. 같은 명세 2장은 사이버보안 대책 자체는 범위 밖으로 둔다. 문장 뒷부분 '보안 명령이 된다'는 해석이므로 해석 부분은 [추정]으로 분리하도록 지시한다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 위협 모델 원문(raw)을 이번 검증에서 열었다. SSH 진입점 절에 'Many images are setup with a default username and password…' 구절이 있다(DRAFT, 최종 수정 2021-01). CISA 권고 ref-583은 원문 미열람이며, 26. 사이버보안·접근권한·개인정보 페이지의 게시된 [사실]에 기댄다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: C. 연결·실행 기반 페이지 G 연결 항목의 [추정]과 같다. ref-405는 이번 검증에서 원문을 열었고, ref-283·284는 원문 미열람. 공개 구성 사례는 oq-043·oq-056에서 열려 있다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문 ref-031 2장에 안전 표준 부인 구절이 그대로 있다. raw 원문에서 safetyState의 eStop과 fieldViolation 필드도 확인했다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 25. 안전·위험 관리 5절 피킹 시나리오와 10절의 [추정](ref-031)과 같다. 흐름 단계 피킹·항목 제약이 맞다. 원격 비상정지 지시 경로의 성능 수준 문제는 oq-095에 있다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문 ref-031 5.3·5.4에서 관제 기능(배정·경로 계산·막힘 탐지와 해소·교통 제어)과 이동로봇 기능(위치 추정·경로 실행)의 구분을 확인했다. 같은 명세 2장은 교통 조율 알고리즘 자체를 범위 밖에 둔다. ref-253·159는 원문 미열람이며, ISO 21423에는 f7과 같은 발행 여부 단서가 필요하다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: C. 연결·실행 기반과 F. 도입·검증·유지관리 페이지의 [추정]과 같다. ref-608(OTTO 발표)은 벤더 문서이므로 본문에서 언급하면 '벤더 주장'을 병기해야 한다. ref-407·408·608 원문 미열람."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: C. 연결·실행 기반과 28. 표준·상호운용성·다사업자 거버넌스 페이지에 같은 내용이 있다. 단체표준 부분은 기사(ref-316·317) 기준이며 원문·발행일 미확인. 모두 원문 미열람."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ROS-MCP-Server README 원문(raw)을 이번 검증에서 열었다. 토픽 발행·구독, 서비스·액션 호출, 파라미터 설정 구절과 rosbridge만 추가하면 된다는 설명이 있고, 기여 안내에 'New features (e.g., Action support, permissions)'가 있다. 확인 기준일은 2026-09-25다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "트랙 nl-task-chatbot 실행 2026-09-25-71의 종합 추정을 다시 인용했다. 출처(ref-679·417)는 도구 노출 방식과 실행 전 게이트를 뒷받침할 뿐이고, '우회할 수 있다·상위 도구만 노출해야 한다'는 이 위키의 판단이다. [추정]을 유지하되, 트랙 쪽 판단이라는 점과 게시 전 트랙 추정이라는 점을 밝히도록 지시한다. ref-417 원문 미열람."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검색 결과로 확인(원문 미열람): arXiv 2606.31339, 2026-06-30 공개. 스니펫이 작업 숲·관리형 블랙보드와 에이전트 제안을 결정적 검증·원자적 반영으로만 받아들이는 구조를 뒷받침한다. 스니펫은 'agentic proposals'라고만 쓰고 LLM이라고 못 박지 않는다. 산업용 대상 프리프린트이며 물류 적용은 미확인이다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: D. 계획·최적화 페이지의 [사실](ref-399·090·168)과 27. AI·학습·적응과 모델 운영 5절(ref-623)에 있다. 학습 기반 배차 교차 규칙(13. 작업 배정 — MRTA)에 맞다. LLM 배정 수치는 oq-030 때문에 쓰지 않는다. 모두 원문 미열람."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: D. 계획·최적화 페이지의 항목과 같다. 그런데 D 페이지는 ref-531 연결을 [추정]으로 실었다. 여기서는 연구가 존재한다는 진술만 [사실]로 쓰는 것이므로 유지하되, 연결 해석은 [추정]으로 둔다. 프리프린트이며 원문 미열람."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: D. 계획·최적화 페이지의 [사실](ref-494, 2026-08)과 같다. GPS 스푸핑 데이터·택시 수요로 실험했다는 한계가 명시돼 있다. 원문 미열람."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: VDA 5050 원문(raw) 6.4.1에서 BLOCKED·RELEASE·SPEED_LIMIT·PRIORITY·PENALTY를 포함한 구역 유형 10종을 확인했다. BLOCKED의 'shall not enter'와 BLOCKED_ZONE_VIOLATION 오류도 있다. 안전 표준 부인 구절은 2장에 있다."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: D. 계획·최적화와 25. 안전·위험 관리 페이지의 [사실](ref-104·567)과 같다. 기준일은 이슈 작성일 2025-04-04이고, 이후 구현 여부는 미확인이다. 두 출처 모두 원문 미열람."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문 ref-004 Negotiation 절에 긴급 작업이 협상을 강제하고, 판정자가 높은 우선순위 참여자를 택하도록 구현할 수 있다는 내용이 있다."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문 ref-004에 판정자를 시스템 통합사가 배치한다(deployed by the system integrator)는 구절이 있고, ref-031 2장은 교통 조율 로직을 범위에서 뺀다. 거버넌스 과제로 넘어간다는 부분은 [추정]이다(oq-057)."
    },
    {
      "finding_id": "f29",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: E. 협업·현장 운영 페이지의 [사실](ref-210)과 같다. 표준 소개 기준이며 원문 미열람. 국내 KS 대응은 oq-064에 있다."
    },
    {
      "finding_id": "f30",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: E. 협업·현장 운영 페이지와 25. 안전·위험 관리 9절의 [추정] 경계와 같다. 안전 기능을 연계 대상으로 둔 서술이 범위 경계에 맞다. 원문 미열람 출처가 섞여 있다."
    },
    {
      "finding_id": "f31",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: E. 협업·현장 운영 페이지의 [사실](ref-473·475)과 25. 안전·위험 관리 11절(ref-561)에 있다. 게시물 제목·요약 기준이며 원문 미열람. KS 번호는 oq-070에서 열려 있다."
    },
    {
      "finding_id": "f32",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: E. 협업·현장 운영 페이지의 [사실](ref-351·353·417)과 같다. 실험 환경이 물류 현장이 아니라는 단서를 유지해야 한다. 원문 미열람."
    },
    {
      "finding_id": "f33",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: E. 협업·현장 운영 페이지의 [사실](ref-476, 2021-01)과 같다. 장애 분석 교차 규칙(19. 모니터링·이상 탐지·원인 분석)에 맞다. 적용 확장 해석 부분은 E 페이지처럼 [추정]으로 둔다. 원문 미열람."
    },
    {
      "finding_id": "f34",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: E. 협업·현장 운영 페이지의 [추정](oq-033·oq-073)과 같다. 모두 원문 미열람."
    },
    {
      "finding_id": "f35",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 26. 사이버보안·접근권한·개인정보 5절의 [사실]과 같다(호 번호 미확인, ref-589 원문 미열람). 위협 모델 원문(raw)에서 카메라 영상이 사적 데이터(Robot Data Assets)로 분류된 것을 확인했다. 문장 뒷부분 '제약이 된다'는 26 페이지가 [추정]으로 쓴 해석이므로 분리를 지시한다(oq-099)."
    },
    {
      "finding_id": "f36",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 25. 안전·위험 관리 5절 출하 시나리오 예외·성과 칸의 [추정]과 같다. ref-567은 원문 미열람인데 finding에는 source_unopened false로 표시돼 있다(브리프 표시 누락)."
    },
    {
      "finding_id": "f37",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 26. 사이버보안·접근권한·개인정보 5절 원격 유지보수 시나리오의 [추정]과 같다. ref-583 원문 미열람. 공개 표준이 없다는 것은 oq-100에서 열려 있다."
    },
    {
      "finding_id": "f38",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 25. 안전·위험 관리 4절과 F. 도입·검증·유지관리 페이지의 [사실](ref-470, 2023-06)과 같다. '연계 대상:' 표시가 있다. 원문 미열람."
    },
    {
      "finding_id": "f39",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: F. 도입·검증·유지관리 페이지의 [추정]과 같다. 근거가 업체(세이프틱스) 자료 하나이므로 본문에 '업체 자료'라고 밝히도록 지시한다. 원문 미열람(oq-092·oq-093)."
    },
    {
      "finding_id": "f40",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 위협 모델 원문(raw)에서 빌드 팜·개발자 작업 환경 구절과 완화책(바이너리 디지털 서명, 소스 보안 감사)을 확인했다. IEC TR 62443-2-3(ref-554, 2015-06)은 F. 도입·검증·유지관리 페이지 기준이며 원문 미열람. 발행 2년이 지난 출처라 월간 재검증 대상이다."
    },
    {
      "finding_id": "f41",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: F. 도입·검증·유지관리 페이지의 [사실](ref-465·539·541)과 같다. '물류 지시 데이터셋 아님' 단서가 있다. 원문 미열람. 매뉴얼 해석 교차 규칙(21. 온보딩·설정·현장 시운전)에 맞다."
    },
    {
      "finding_id": "f42",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "게시 페이지에 없는 새 연결이다. 분류 원문 24 정의의 '모델 버전'과 27. AI·학습·적응과 모델 운영 5절의 [추정](ref-626·625)에 기댄다. [추정]을 유지한다. 두 출처 모두 원문 미열람."
    },
    {
      "finding_id": "f43",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: F. 도입·검증·유지관리 페이지의 [사실](ref-516·518)과 같다. 22. 시뮬레이션·예측용 디지털 트윈 쪽 내용이며 8. 실시간 세계 상태·데이터 일관성과 섞이지 않았다. 물류 적용은 oq-085. 원문 미열람."
    },
    {
      "finding_id": "f44",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: F. 도입·검증·유지관리와 28. 표준·상호운용성·다사업자 거버넌스 페이지의 각주와 같다. ref-466은 기사 기준이다. 모두 원문 미열람(oq-089·oq-111)."
    },
    {
      "finding_id": "f45",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: VDA 5050 원문(raw)에서 UNSUPPORTED_PARAMETER(CRITICAL) 구절과 의미적 버전 관리 규정을 확인했다. 28. 표준·상호운용성·다사업자 거버넌스 5절의 [추정]과 같다(oq-091). ref-051·635 원문 미열람."
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
      "대부분의 finding은 A~F 대분류 페이지 G 연결 항목과 25~28 세부영역 페이지에 이미 게시된 주장이다. 같은 각주 id를 재사용해야 한다(브리프가 이미 재사용함).",
      "ref-315(www.korea.kr/briefing/…)와 ref-709(korea.kr/news/…)는 같은 국가기술표준원 보도자료(2021-11-11)다. f9는 ref-315를, f18은 ref-709를 쓴다.",
      "f7·f16의 ISO 21423 서술('국제표준')이 C. 연결·실행 기반 페이지의 '개발 중, FDIS 단계, 발행 여부 미확인' 서술과 어긋나 보인다.",
      "f19~f21·f35·f37·f42는 C. 연결·실행 기반·E. 협업·현장 운영 페이지가 '근거 없음'으로 둔 연결을 보강하는 후보다. 이번 실행은 G. 안전·보안·지능·거버넌스 페이지만 바꾼다."
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
    "page_proposals 절 이름: patches의 section을 대분류 정본 H2 '다른 대분류와의 연결'로 쓰고 '5. '를 붙이지 않는다. 대분류 H2에는 번호가 없고, 번호를 붙이면 퍼블리셔가 반려한다.",
    "'아직 다루지 않은 연결' 목록: rationale의 '2·3·4 ↔ 25·26', '11. 분산 시스템·통신·컴퓨팅 구조 ↔ 25·27' 같은 번호 약칭을 '2. 공정·워크플로 모델링, 3. 처리능력·거점·설비 계획, 4. 성과·경제성·프로세스 개선 ↔ 25. 안전·위험 관리, 26. 사이버보안·접근권한·개인정보'처럼 번호와 이름으로 풀어 쓴다. 번호만 쓴 호칭은 공통 규칙 위반이다.",
    "f7·f16: ISO 21423을 '국제표준이다'로 단정하지 않는다. C. 연결·실행 기반 페이지와 같게 '산업용 이동로봇의 통신·상호운용성을 다루는 ISO 표준(검색 결과상 FDIS 단계, 발행 여부 미확인)'으로 쓴다. ref-159 원문을 열지 못했다.",
    "f11: 사실 부분만 [사실][^ref-031]로 둔다. 사실 부분은 updateCertificate 동작, MQTT용 자격증명 내려받기, 내려받기의 TLS 보호, 인증서 체인 검증 권고다. '인증서 교체가 관제 연동 경로를 거치는 보안 명령이 된다'는 별도 문장 [추정][^ref-031]으로 나눈다. 명세가 사이버보안 대책 자체를 범위 밖에 두기 때문이다.",
    "f35: 법 조항 내용(제20조의 근로자 감시 설비 설치 협의, 호 번호 미확인)과 위협 모델의 카메라 영상 사적 데이터 분류만 [사실]로 둔다. '영상 수집 조건이 사람–로봇 협업의 제약이 된다'는 26. 사이버보안·접근권한·개인정보 페이지처럼 [추정]으로 나누고 oq-099를 연결한다.",
    "f17: 본문에서 OTTO(ref-608) 인증 발표를 언급하면 '[추정] 벤더 주장'을 병기하고 시험 항목 미확인을 밝힌다. 출처가 벤더 보도자료다.",
    "f20: 이 문장이 트랙 nl-task-chatbot 실행 2026-09-25-71에서 이 위키가 종합한 판단임을 밝히고 [추정]으로 유지한다. 출처 ref-679·417은 도구 노출 방식과 실행 전 게이트의 존재만 뒷받침한다.",
    "f21: '산업용 다중 로봇 대상 프리프린트이며 물류 적용 미확인'을 함께 적는다. 확인 근거가 검색 결과(원문 미열람)이기 때문이다.",
    "f23·f33: 연구가 있다는 진술은 [사실]로 두고, 그것이 두 대분류를 잇는다는 해석은 [추정]으로 나눈다. D. 계획·최적화·E. 협업·현장 운영 페이지의 태그 분리와 맞추기 위해서다.",
    "f39: ref-559를 '업체(세이프틱스) 자료'로 밝히고 국내 공식 규정 미확인 단서를 유지한다. 근거가 업체 자료 하나다.",
    "원문 미열람 표기: 이번 실행에서 원문을 연 ref-004·ref-009·ref-010·ref-031·ref-405·ref-679를 뺀 모든 출처의 각주 정의에서 접근일 뒤에 ' (원문 미열람)'을 붙인다. reference_updates의 해당 항목에도 source_unopened: true를 넣는다. 특히 ref-567·ref-583·ref-589는 finding 표시(source_unopened false)와 달리 미열람이다.",
    "교차 규칙: 27. AI·학습·적응과 모델 운영 항목(f4·f5·f22·f33·f41)은 적용 대상 세부영역(5. 로봇 능력·작업 온톨로지, 6. 지도·공간·위치 모델, 13. 작업 배정 — MRTA, 19. 모니터링·이상 탐지·원인 분석, 21. 온보딩·설정·현장 시운전) 페이지 링크와 함께 쓴다. f43은 22. 시뮬레이션·예측용 디지털 트윈 쪽으로만 두고 8. 실시간 세계 상태·데이터 일관성과 섞지 않는다.",
    "C. 연결·실행 기반·E. 협업·현장 운영 페이지가 '근거 없음'으로 둔 연결(f19~f21, f35·f37)은 G 페이지에만 쓴다. 다른 대분류 페이지는 이번 실행에서 고치지 않고, 보강 후보라는 점만 한 줄로 적는다.",
    "open_questions_new의 인증서 교체 책임 질문(근거 f11)은 그대로 등록한다. 관련 영역은 26. 사이버보안·접근권한·개인정보, 9. 로봇·제조사 관제 연동, 24. 자산·소프트웨어 수명주기 관리이고, 종류는 일반이다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 이번 실행은 원문 열람이 차단된 환경에서 검증했다(mirror_only). 확인 45건, 미확인 0건, 교차 확인 0건. 강등: 없음. 대신 f11·f23·f33·f35의 해석 부분을 [추정]으로 분리하고, f7·f16의 ISO 21423 문구에 발행 여부 미확인 단서를 붙이도록 지시했다. 원문 열람: ref-031·ref-405·ref-010·ref-679는 이번 검증에서 raw.githubusercontent.com으로 다시 열었고, ref-004·ref-009는 입력 원문 텍스트로 확인했다. 원문 미열람 출처: 위 6건을 뺀 재사용 출처 전부. ref-677은 검색 결과로만 확인했다. 주의: 연결 대부분은 게시된 A~F 대분류 페이지와 25~28 세부영역 페이지의 주장을 다시 인용한 것이다. 모든 연결이 단일 출처이거나 같은 발행 주체 출처라 교차 확인된 것은 없다. f19~f21·f35·f37·f42는 다른 대분류 페이지가 '근거 없음'으로 둔 연결의 보강 후보이며, f20은 게시 전 트랙 추정을 다시 인용했다. ref-315와 ref-709는 같은 보도자료를 가리킨다. ref-009의 브리프 summary가 '원문 미열람'으로 시작해 fetched 표시와 맞지 않는다. 입력 원문 텍스트가 있으므로 원문 열람으로 본다. 반대로 f36·f37의 ref-567·ref-583은 미열람인데 finding 표시(source_unopened false)가 빠졌다. 한국어 검색은 하지 않았고, 국내 근거는 기존 KS·정부 출처를 재사용했다. VDA 5050 원문 2장은 사업자 간 운영 책임 배분도 범위 밖에 둔다(브리프는 이 구절을 확인하지 못했다고 적었다). 정정 요청 없음.",
  "retry_reason": null
}
```

### runs/2026-09-25-73/pages.json

```json
{
  "run_id": "2026-09-25-73",
  "outline": [
    {
      "path": "docs/categories/g-safety-security-intelligence-and-governance/index.md",
      "section": "다른 대분류와의 연결",
      "budget_chars": 7500,
      "summary": "G. 안전·보안·지능·거버넌스의 25~28 세부영역은 A~F 대분류의 세부영역에 안전 상태·접근권한·모델 운영·표준 책임 문제로 이어지며, 연결마다 단일 출처라 교차 확인된 연결은 없다. 예: VDA 5050 3.0.0은 스스로 안전 표준으로 적용해서는 안 된다고 밝힌다. [사실][^ref-031]",
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
        "f23",
        "f24",
        "f25",
        "f26",
        "f27",
        "f28",
        "f29",
        "f30",
        "f31",
        "f32",
        "f33",
        "f34",
        "f35",
        "f36",
        "f37",
        "f38",
        "f39",
        "f40",
        "f41",
        "f42",
        "f43",
        "f44",
        "f45"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/g-safety-security-intelligence-and-governance/index.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "'다른 대분류와의 연결' 절 첫 작성: A~F 대분류와의 연결 45건, C·E 페이지 보강 후보 표시, 아직 다루지 않은 연결 목록, 절 끝 각주 정의",
      "patches": [
        {
          "section": "다른 대분류와의 연결",
          "action": "replace",
          "frontmatter": {
            "sources": [
              "ref-004",
              "ref-009",
              "ref-010",
              "ref-031",
              "ref-051",
              "ref-076",
              "ref-090",
              "ref-104",
              "ref-111",
              "ref-125",
              "ref-129",
              "ref-130",
              "ref-138",
              "ref-159",
              "ref-168",
              "ref-199",
              "ref-210",
              "ref-230",
              "ref-234",
              "ref-238",
              "ref-239",
              "ref-240",
              "ref-253",
              "ref-283",
              "ref-284",
              "ref-286",
              "ref-314",
              "ref-315",
              "ref-316",
              "ref-317",
              "ref-351",
              "ref-353",
              "ref-399",
              "ref-405",
              "ref-407",
              "ref-408",
              "ref-417",
              "ref-465",
              "ref-466",
              "ref-470",
              "ref-472",
              "ref-473",
              "ref-475",
              "ref-476",
              "ref-494",
              "ref-516",
              "ref-518",
              "ref-531",
              "ref-539",
              "ref-541",
              "ref-554",
              "ref-559",
              "ref-561",
              "ref-567",
              "ref-583",
              "ref-589",
              "ref-606",
              "ref-607",
              "ref-608",
              "ref-618",
              "ref-623",
              "ref-625",
              "ref-626",
              "ref-635",
              "ref-677",
              "ref-679",
              "ref-706",
              "ref-709",
              "ref-710"
            ]
          },
          "content": "(절 본문 생략 — runs/2026-09-25-73/pages/categories/g-safety-security-intelligence-and-governance/index.md 의 해당 절을 본다)"
        }
      ]
    }
  ],
  "changelog_entry": "2026-09-25 | G. 안전·보안·지능·거버넌스 | '다른 대분류와의 연결' 절 첫 작성(A~F 대분류와의 연결 45건, 교차 확인 없음, 아직 다루지 않은 연결 목록) | run 2026-09-25-73",
  "index_updates": {
    "home_recent": "2026-09-25 — G. 안전·보안·지능·거버넌스: '다른 대분류와의 연결' 절 첫 작성(A~F 대분류의 세부영역과 안전 상태·접근권한·모델 운영·표준 책임으로 잇는 연결, 교차 확인 없음)",
    "category_recent": "2026-09-25 — G. 안전·보안·지능·거버넌스: '다른 대분류와의 연결' 절 첫 작성(A~F 대분류와의 연결 45건, 24. 자산·소프트웨어 수명주기 관리 ↔ 27. AI·학습·적응과 모델 운영 연결 신규)"
  },
  "glossary_updates": [],
  "reference_updates": [
    {
      "id": "ref-004",
      "org": "Open Robotics",
      "title": "RMF Core Overview — Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/rmf-core.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "RMF 교통 스케줄·협상·긴급 작업 우선 협상 구조.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-009",
      "org": "ROS 2 Design",
      "title": "ROS 2 DDS-Security Integration",
      "published": null,
      "url": "https://design.ros2.org/articles/ros2_dds_security.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "ROS 2 의 DDS-Security 인증·접근통제·암호화 플러그인 통합 설계.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-010",
      "org": "ROS 2 Design",
      "title": "ROS 2 Robotic Systems Threat Model",
      "published": null,
      "url": "https://design.ros2.org/articles/ros2_threat_model.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "ROS 2 로봇 시스템 위협 모델 초안(최종 수정 2021-01). 기본 자격증명 SSH, 카메라 영상·로그 민감 자산, 빌드 팜 공급망 위협과 감사·서명 완화책.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "VDA 5050 3.0.0 명세. 안전 표준 부인 문구, safetyState, updateCertificate, 관제·로봇 기능 구분, 구역 유형.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-051",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — json_schemas/state.schema",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. VDA 5050 상태 메시지 JSON 스키마(오류 수준·운용 모드·적재물·배터리 필드).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-076",
      "org": "DeFazio, D., Mehta, H., Wang, M., Yang, P., Blackburn, J., & Zhang, S.",
      "title": "Vision Language Models Can Parse Floor Plan Maps",
      "published": "2024-09",
      "url": "https://arxiv.org/abs/2409.12842",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 비전 언어 모델로 평면도 지도를 해석하는 연구.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-090",
      "org": "Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C.",
      "title": "SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models",
      "published": "2023-09",
      "url": "https://arxiv.org/abs/2309.10062",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. LLM 기반 다중 로봇 작업 계획·배정.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-104",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_demos — Demonstrations of Open-RMF (README)",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_demos",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. Open-RMF 데모 구성과 비상 경보 시 주차 동작.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-111",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_api_msgs — rmf_api_msgs/schemas/task_state.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. Open-RMF 작업 상태 스키마.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-125",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_api_msgs — rmf_api_msgs/schemas/task_request.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. Open-RMF 작업 요청 스키마.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-129",
      "org": "MESA International",
      "title": "B2MML-BatchML/Schema/B2MML-TransactionProfile.xsd",
      "published": "2023",
      "url": "https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-TransactionProfile.xsd",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. B2MML 거래 동사(CHANGE·CANCEL 등) 정의.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-130",
      "org": "OPC Foundation",
      "title": "UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv)",
      "published": "2024-01-31",
      "url": "https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. OPC UA for ISA-95 Job Control 작업 지시 메서드.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
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
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 서비스 로봇 소프트웨어 모듈 정보 모델 KS.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-159",
      "org": "ISO",
      "title": "ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability",
      "published": null,
      "url": "https://www.iso.org/standard/86749.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 산업용 이동로봇 통신·상호운용성 ISO 표준(검색 결과상 FDIS 단계, 발행 여부 미확인).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-168",
      "org": "Kaitha, S., & Yu, S. 외(arXiv 2512.02810)",
      "title": "Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms",
      "published": "2025-12",
      "url": "https://arxiv.org/abs/2512.02810",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. LLM 기반 로봇 작업 배정 벤치마크(결과 수치 출처 충돌, oq-030).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-199",
      "org": "arXiv 2410.21415 저자(미확인)",
      "title": "Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding",
      "published": "2024-10",
      "url": "https://arxiv.org/abs/2410.21415",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 모방 학습 기반 지속형 MAPF.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-210",
      "org": "ANSI / A3(Association for Advancing Automation)",
      "title": "ANSI/A3 R15.08-2-2023 - Industrial Mobile Robots - Safety Requirements - Part 2: Requirements for IMR system(s) and IMR application(s)",
      "published": "2023",
      "url": "https://webstore.ansi.org/standards/ria/ansia3r15082023",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 산업용 이동로봇 시스템·적용 안전 요구(유형 C 모바일 매니퓰레이터 포함).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-230",
      "org": "MassRobotics",
      "title": "MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json",
      "published": null,
      "url": "https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. MassRobotics 상태 보고 JSON 스키마(운용 상태 어휘).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-234",
      "org": "IDTA(Industrial Digital Twin Association)",
      "title": "IDTA 02047 Technical Data for Automated Guided Vehicles 1.0 — README (admin-shell-io/submodel-templates)",
      "published": null,
      "url": "https://github.com/admin-shell-io/submodel-templates/tree/main/published/Technical%20Data%20for%20Automated%20Guided%20Vehicles",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 무인운반차 기술 데이터 서브모델.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-238",
      "org": "Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A.",
      "title": "On the Use of Large Language Models to Generate Capability Ontologies",
      "published": "2024-04",
      "url": "https://arxiv.org/abs/2404.17524",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. LLM 으로 능력 온톨로지 생성.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-239",
      "org": "Dussard, B., & Sarthou, G. (LAAS-CNRS)",
      "title": "Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF",
      "published": "2026-06",
      "url": "https://arxiv.org/abs/2606.17073",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. URDF 에서 로봇 온톨로지를 LLM 으로 채우는 연구.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-240",
      "org": "ISO",
      "title": "ISO 22166-201:2024 - Robotics — Modularity for service robots — Part 201: Common information model for modules",
      "published": "2024-02",
      "url": "https://www.iso.org/standard/82334.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 서비스 로봇 모듈 공통 정보 모델.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-253",
      "org": "MassRobotics",
      "title": "MassRobotics-AMR/AMR_Interop_Standard — README",
      "published": null,
      "url": "https://github.com/MassRobotics-AMR/AMR_Interop_Standard",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. MassRobotics AMR 상호운용 표준 저장소(신원·상태 보고).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-283",
      "org": "Open Robotics",
      "title": "Doors (integration_doors) - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/integration_doors.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. Open-RMF 문 연동.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-284",
      "org": "Open Robotics",
      "title": "Lifts (integration_lifts) - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/integration_lifts.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. Open-RMF 승강기 연동.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-286",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 승강기 상태 메시지(층 이름, 운영 모드).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-314",
      "org": "국가표준인증통합정보시스템(KSSN)",
      "title": "KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법",
      "published": "2021-11",
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010135682",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 이동 로봇 엘리베이터 탑승 안전 KS.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
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
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 로봇 엘리베이터 탑승 KS 제정 보도자료(ref-709 와 같은 보도자료).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-316",
      "org": "건설기술신문",
      "title": "승강기협, 엘리베이터-로봇 연동 단체표준 제정",
      "published": null,
      "url": "https://www.ctman.kr/35296",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 대한승강기협회 엘리베이터–로봇 연동 단체표준 제정 기사.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-317",
      "org": "전기신문",
      "title": "승강기협회 '로봇-승강기 연동 표준개발'로 승강기 4차산업 견인",
      "published": null,
      "url": "https://www.electimes.com/news/articleView.html?idxno=320147",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 로봇–승강기 연동 표준 개발 기사.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-351",
      "org": "Ren, A. Z. 외",
      "title": "Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners",
      "published": "2023-07",
      "url": "https://arxiv.org/abs/2307.01928",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. KnowNo: 등각 예측 기반으로 불확실할 때 사람에게 묻는 LLM 계획기.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-353",
      "org": "Park, J., Lim, S., Lee, J., Park, S., Chang, M., Yu, Y., & Choi, S.",
      "title": "CLARA: Classifying and Disambiguating User Commands for Reliable Interactive Robotic Agents",
      "published": "2024",
      "url": "https://arxiv.org/abs/2306.10376",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 사용자 명령 분류·모호성 해소.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-399",
      "org": "Wang, Z., & Gombolay, M.",
      "title": "Heterogeneous graph attention networks for scalable multi-robot scheduling with temporospatial constraints",
      "published": null,
      "url": "https://link.springer.com/article/10.1007/s10514-021-09997-2",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 학습 기반 다중 로봇 스케줄링.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-405",
      "org": "Open Robotics",
      "title": "Security - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/security.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "RMF 의 SROS 2 인클레이브·서명 권한 파일, 대시보드 TLS·OIDC 역할 토큰.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-407",
      "org": "gpue (GitHub)",
      "title": "vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS)",
      "published": null,
      "url": "https://github.com/gpue/vda5050-sim",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. VDA 5050 3.0.0 시뮬레이터와 적합성 시험 묶음(개인 프로젝트).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
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
      "accessed": "2026-09-25",
      "summary": "원문 미열람. MQTT 기록 기반 VDA 5050 진단 도구(개인 프로젝트).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-417",
      "org": "Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab)",
      "title": "Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems",
      "published": "2026-04",
      "url": "https://arxiv.org/abs/2604.05427",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. SafeGate: 자연어 명령 실행 전 결정적 안전 판정과 작업 안전 계약.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-465",
      "org": "Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A.",
      "title": "Toward a Method to Generate Capability Ontologies from Natural Language Descriptions",
      "published": "2024-06",
      "url": "https://arxiv.org/abs/2406.07962",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 자연어 능력 설명에서 LLM 으로 능력 온톨로지 생성.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-466",
      "org": "부산일보",
      "title": "KTL·통합물류협회 ‘물류로봇 시험인증’ 협력 강화 ‘맞손’",
      "published": "2026-07-24",
      "url": "https://www.busan.com/view/busan/view.php?code=2026072420194685883",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. KTL·통합물류협회 물류로봇 시험인증 협력 기사.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-470",
      "org": "ISO",
      "title": "ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems",
      "published": "2023-06",
      "url": "https://www.iso.org/standard/83545.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 무인 산업 차량과 시스템의 안전 요구·검증, 운용 구역 부속서 A.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-472",
      "org": "A3(Association for Advancing Automation)",
      "title": "ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available",
      "published": "2023-10",
      "url": "https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. R15.08-2 발행 안내.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-473",
      "org": "고용노동부",
      "title": "고정식 이동식 산업용 로봇의 협동작업 안전 가이드 배포",
      "published": "2023-07",
      "url": "https://www.moel.go.kr/policy/policydata/view.do?bbs_seq=20230700065",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 산업용 로봇 협동작업 안전 가이드 배포 게시물.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-475",
      "org": "중소벤처기업부(대한민국 정책브리핑)",
      "title": "｢대구 이동식 협동로봇 규제자유특구｣ 산업표준 제정으로, 이동식 협동로봇 상용화 길 열렸다!",
      "published": "2024-11",
      "url": "https://www.korea.kr/briefing/pressReleaseView.do?newsId=156658517",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 이동식 협동로봇 산업표준 제정 보도자료.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-476",
      "org": "Das, D., Banerjee, S., & Chernova, S.",
      "title": "Explainable AI for Robot Failures: Generating Explanations that Improve User Assistance in Fault Recovery",
      "published": "2021-01",
      "url": "https://arxiv.org/abs/2101.01625",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 로봇 실패 설명 생성으로 고장 복구 지원 개선.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-494",
      "org": "Francos, R. M., Garces, D., Akgün, O. E., Bastian, N. D., & Gil, S.(Harvard·JHU)",
      "title": "Trust-Aware Sequential Decision Making and Rollout Planning for Resilient Multi-Robot Systems",
      "published": "2026-08",
      "url": "https://arxiv.org/abs/2608.25690",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 위치 스푸핑 에이전트를 고려한 신뢰 인지 다중 로봇 배정·계획.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-516",
      "org": "한국표준협회 KSSN(국가표준인증종합정보센터)",
      "title": "KS X ISO 23247-1 자동화 시스템 및 통합 — 제조를 위한 디지털 트윈 프레임워크 — 제1부: 개요 및 일반 원리",
      "published": null,
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010140724",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 제조용 디지털 트윈 프레임워크 KS 부합화 표준.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-518",
      "org": "ISO",
      "title": "ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition",
      "published": "2026",
      "url": "https://www.iso.org/standard/87426.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 디지털 트윈 결합 표준.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-531",
      "org": "arXiv 2607.05683 저자(미확인)",
      "title": "Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers",
      "published": "2026-07",
      "url": "https://arxiv.org/abs/2607.05683",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 자율 피킹 로봇 배터리 관리의 심층 강화학습.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-539",
      "org": "askforalfred (ALFRED 공식 저장소)",
      "title": "ALFRED — A Benchmark for Interpreting Grounded Instructions for Everyday Tasks (GitHub README)",
      "published": null,
      "url": "https://github.com/askforalfred/alfred",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 자연어 지시 기반 체화 에이전트 벤치마크.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-541",
      "org": "lbaa2022 (LoTa-Bench 공식 저장소)",
      "title": "LLMTaskPlanning — LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents (ICLR 2024) (GitHub README)",
      "published": null,
      "url": "https://github.com/lbaa2022/LLMTaskPlanning",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 언어 기반 작업 계획기 자동 평가 벤치마크.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-554",
      "org": "IEC",
      "title": "IEC TR 62443-2-3:2015 Security for industrial automation and control systems - Part 2-3: Patch management in the IACS environment",
      "published": "2015-06",
      "url": "https://webstore.iec.ch/en/publication/22811",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. IACS 환경 패치 관리 기술 보고서.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-559",
      "org": "세이프틱스(Safetics)",
      "title": "로봇 시스템 위험성평가 가이드",
      "published": null,
      "url": "https://doc.safetics.io/insight-risk-assessment/",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 업체의 로봇 시스템 위험성평가 가이드(변경 시 재평가 권고).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-561",
      "org": "대한민국 정책브리핑(중소벤처기업부)",
      "title": "이동식 협동로봇 ‘안전기준 산업표준’ 제정…상용화 길 열어",
      "published": "2024-11-03",
      "url": "https://www.korea.kr/news/policyNewsView.do?newsId=148935814",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 이동식 협동로봇 안전기준 산업표준 제정 소식.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-567",
      "org": "Open-RMF (open-rmf/rmf GitHub)",
      "title": "[Feature request]: Fire alarm separation for different fleets · Issue #658 · open-rmf/rmf",
      "published": "2025-04-04",
      "url": "https://github.com/open-rmf/rmf/issues/658",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 화재경보 시 로봇 주차와 플릿별 구분 기능 요청.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-583",
      "org": "CISA",
      "title": "Mobile Industrial Robots Vehicles and MiR Fleet Software (ICSA-21-280-02)",
      "published": null,
      "url": "https://www.cisa.gov/news-events/ics-advisories/icsa-21-280-02",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. MiR 차량·플릿 소프트웨어 취약점 권고.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-589",
      "org": "법제처 국가법령정보센터",
      "title": "근로자참여 및 협력증진에 관한 법률",
      "published": null,
      "url": "https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=105636",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 제20조 노사협의회 협의 사항(근로자 감시 설비 설치).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-606",
      "org": "한국표준협회 KSSN(국가표준인증종합정보센터)",
      "title": "KS B ISO 18646-1 로봇 — 서비스 로봇의 성능 기준 및 관련 시험방법 — 제1부 : 바퀴형 로봇의 이동능력",
      "published": null,
      "url": "https://www.kssn.net/search/stddetail.do?itemNo=K001010113281",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 바퀴형 서비스 로봇 이동 성능 시험방법 KS.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-607",
      "org": "한국로봇산업진흥원(KIRIA)",
      "title": "시험평가 — KIRIA 첨단로봇 실증지원 디지털 플랫폼",
      "published": null,
      "url": "https://kiria.org/rp/kiria/tva/inr/page.dn",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 한국로봇산업진흥원 시험평가 서비스 안내.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-608",
      "org": "OTTO by Rockwell Automation",
      "title": "OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments",
      "published": "2026-04",
      "url": "https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. VDA 5050 인증 취득 벤더 발표(시험 항목 미확인).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-618",
      "org": "ISO/IEC",
      "title": "ISO/IEC 42001:2023 - AI management systems",
      "published": "2023",
      "url": "https://www.iso.org/standard/42001",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. AI 관리 시스템 표준.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-623",
      "org": "Agrawal, A. 외",
      "title": "RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments",
      "published": "2022-09",
      "url": "https://arxiv.org/abs/2209.05738",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 창고 다중 로봇 작업 배정 강화학습(시뮬레이션 창고).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-625",
      "org": "Breck, E. 외 (Google Research)",
      "title": "The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction",
      "published": "2017",
      "url": "https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. ML 운영 준비도 시험 기준.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-626",
      "org": "MLflow (Linux Foundation 오픈소스 프로젝트)",
      "title": "ML Model Registry | MLflow AI Platform",
      "published": null,
      "url": "https://mlflow.org/docs/latest/ml/model-registry/",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 모델 레지스트리의 버전·별칭 관리.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-635",
      "org": "Semantic Versioning (Tom Preston-Werner, semver.org)",
      "title": "Semantic Versioning 2.0.0",
      "published": null,
      "url": "https://semver.org/spec/v2.0.0.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 의미적 버전 관리 규칙(이번 실행 재열람 안 함).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-677",
      "org": "Tang, G. 외(arXiv 2606.31339)",
      "title": "Verification-Gated Agentic Mission-State Governance for Intelligent Industrial Multi-Robot Systems",
      "published": "2026-06",
      "url": "https://arxiv.org/abs/2606.31339",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 에이전트 제안의 결정적 검증과 원자적 반영을 거치는 관리형 블랙보드 구조(검색 결과로만 확인).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-679",
      "org": "robotmcp (ROS-MCP-Server 공식 저장소)",
      "title": "ros-mcp-server — Connect AI models like Claude & GPT with robots using MCP and ROS (GitHub README)",
      "published": null,
      "url": "https://github.com/robotmcp/ros-mcp-server",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "rosbridge 로 LLM 에 ROS 토픽·서비스·액션·파라미터를 도구로 노출. 권한 기능은 향후 기여 항목.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-706",
      "org": "IETF (RFC Editor)",
      "title": "RFC 9745: The Deprecation HTTP Response Header Field",
      "published": null,
      "url": "https://www.rfc-editor.org/info/rfc9745/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. API 폐기 예고 HTTP 헤더.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
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
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 로봇 엘리베이터 탑승 KS 제정 발표(ref-315 와 같은 보도자료).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    },
    {
      "id": "ref-710",
      "org": "한국지능형로봇표준포럼(KOROS)",
      "title": "KOROS 1148-8:2025 서비스 로봇을 위한 모듈 - 제2-8부 : 소프트웨어 모듈용 정보모델 상호운용성 시험 절차",
      "published": "2025-06-04",
      "url": "http://www.koros.or.kr/bbs/board.php?bo_table=notice27&wr_id=223",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 소프트웨어 모듈 정보모델 상호운용성 시험 절차 단체표준.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/g-safety-security-intelligence-and-governance/index.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "ROP 가 VDA 5050 updateCertificate 같은 보안 명령으로 제조사 로봇의 인증서를 교체할 때, 교체 시점·대상 승인과 실패 시 되돌림 책임은 ROP 사업자·제조사·현장 IT 조직 중 누가 지는가?",
      "areas": [
        26,
        9,
        24
      ],
      "status": "열림",
      "link": null
    }
  ],
  "flow_matrix_updates": [],
  "additional_research_requests": [
    "'다른 대분류와의 연결' 절 '아직 다루지 않은 연결': 11. 분산 시스템·통신·컴퓨팅 구조 ↔ 25. 안전·위험 관리·27. AI·학습·적응과 모델 운영, 7. 화물·재고·자산 식별과 추적 ↔ G. 안전·보안·지능·거버넌스, 14. 작업 순서·스케줄링 ↔ G. 안전·보안·지능·거버넌스, 2. 공정·워크플로 모델링·3. 처리능력·거점·설비 계획·4. 성과·경제성·프로세스 개선 ↔ 25. 안전·위험 관리·26. 사이버보안·접근권한·개인정보의 연결 근거가 브리프에 없어 쓰지 못했다. 다음 연결 실행에서 조사가 필요하다.",
    "ISO 21423(ref-159)의 발행 여부와 발행판의 공통 좌표계 정의: 본문에서 'FDIS 단계, 발행 여부 미확인'으로 두었으므로 원문 또는 ISO 카탈로그 확인이 필요하다(oq-027).",
    "Tang 외(ref-677) 원문 열람: 제안 주체가 LLM 에이전트로 한정되는지와 물류 적용 여부를 확인해야 C. 연결·실행 기반과의 연결 서술을 보강할 수 있다.",
    "모든 연결이 단일 출처이거나 같은 발행 주체 출처다. 핵심 연결(VDA 5050 안전 표준 부인, SROS 2 인클레이브 권한 분리)에 독립 출처가 있으면 교차 확인에 필요하다.",
    "ref-315 와 ref-709 는 같은 국가기술표준원 보도자료다. 참고문헌 id 통합 여부를 퍼블리셔·참고문헌 담당이 결정해야 한다."
  ],
  "fixes_applied": [
    "절 이름 — patches 의 section 을 대분류 정본 H2 '다른 대분류와의 연결'로 썼고 번호를 붙이지 않았다.",
    "'아직 다루지 않은 연결' 번호 약칭 — 소제목 '아직 다루지 않은 연결' 목록에서 모든 세부영역을 '2. 공정·워크플로 모델링, 3. 처리능력·거점·설비 계획, 4. 성과·경제성·프로세스 개선 ↔ 25. 안전·위험 관리, 26. 사이버보안·접근권한·개인정보'처럼 번호와 이름으로 풀어 썼다.",
    "f7·f16 ISO 21423 — B. 공통 정보·환경 모델의 6. 지도·공간·위치 모델 항목과 C. 연결·실행 기반의 9. 로봇·제조사 관제 연동 항목 모두 '산업용 이동로봇의 통신·상호운용성을 다루는 ISO 표준(검색 결과상 FDIS 단계, 발행 여부 미확인)'으로 썼다.",
    "f11 분리 — updateCertificate 동작, MQTT용 자격증명 내려받기, 내려받기의 TLS 보호, 인증서 체인 검증 권고를 [사실][^ref-031]로 두고, '인증서 교체가 관제 연동 경로를 거치는 보안 명령이 된다'는 문장을 [추정][^ref-031]로 따로 나눴다.",
    "f35 분리 — 제20조 협의 사항(호 번호 미확인)을 [사실][^ref-589], 위협 모델의 카메라 영상 사적 데이터 분류를 [사실][^ref-010]로 두고, '영상 수집 조건이 사람–로봇 협업의 제약이 된다'를 [추정]으로 나눈 뒤 oq-099 링크를 붙였다.",
    "f17 OTTO — C. 연결·실행 기반 9. 로봇·제조사 관제 연동 항목에서 OTTO 인증 발표를 '[추정] 벤더 주장[^ref-608]'으로 쓰고 시험 항목 미확인을 밝혔다.",
    "f20 — 트랙 자연어 업무 지시 챗봇 실행 2026-09-25-71(단계 3)에서 이 위키가 종합한 판단이라고 문장 앞에 밝히고 [추정]을 유지했으며, 출처는 도구 노출 방식과 실행 전 게이트의 존재만 뒷받침하고 게시 전 트랙 추정이라는 문장을 덧붙였다.",
    "f21 — '산업용 다중 로봇 대상 프리프린트이며 물류 적용은 확인되지 않았다'를 함께 적었고, 원문 미열람으로 제안 주체가 LLM 에이전트로 한정되는지 확인하지 않았다는 단서도 더했다.",
    "f23·f33 분리 — 연구 존재 진술은 [사실]로 두고, 두 대분류를 잇는다는 해석은 각각 별도 문장 [추정][^ref-199][^ref-531], [추정][^ref-476]으로 나눴다.",
    "f39 — ref-559 를 '업체(세이프틱스) 자료'로 밝히고 근거가 그 자료 하나이며 국내 공식 규정은 확인되지 않았다는 단서를 유지했다.",
    "원문 미열람 표기 — ref-004·009·010·031·405·679 를 뺀 모든 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙였고(ref-567·583·589 포함), reference_updates 의 해당 항목에 source_unopened: true 와 '원문 미열람. '으로 시작하는 summary 를 넣었다. ref-009 는 입력 원문으로 확인됐으므로 summary 에서 '원문 미열람' 접두어를 뺐다.",
    "교차 규칙 — f4·f5·f22·f33·f41 항목에 5. 로봇 능력·작업 온톨로지, 6. 지도·공간·위치 모델, 13. 작업 배정 — MRTA, 19. 모니터링·이상 탐지·원인 분석, 21. 온보딩·설정·현장 시운전 페이지 링크와 27. AI·학습·적응과 모델 운영 링크를 함께 두었다. f43 은 22. 시뮬레이션·예측용 디지털 트윈 쪽으로만 두고, 8. 실시간 세계 상태·데이터 일관성과 구분한다는 문장을 덧붙였다.",
    "'근거 없음' 연결 — f19~f21, f35·f37 은 G. 안전·보안·지능·거버넌스 페이지에만 썼다. C. 연결·실행 기반과 E. 협업·현장 운영 블록 끝에 각각 보강 후보라는 점과 해당 페이지를 이번 실행에서 고치지 않았다는 점을 한 줄로 적었다.",
    "열린 질문 — 인증서 교체 책임 질문(근거 f11)을 open_question_updates 에 new 로 등록했다. 관련 영역은 26. 사이버보안·접근권한·개인정보, 9. 로봇·제조사 관제 연동, 24. 자산·소프트웨어 수명주기 관리이고, 종류는 일반이라 접두어를 붙이지 않았다."
  ]
}
```

### runs/2026-09-25-73/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/g-safety-security-intelligence-and-governance/index.md (1개 절)
```

### runs/2026-09-25-73/pages/categories/g-safety-security-intelligence-and-governance/index.md

```markdown
---
title: "G. 안전·보안·지능·거버넌스"
type: category
status: draft
created: 2026-09-24
updated: 2026-09-25
version: 2
sources: [ref-004, ref-009, ref-010, ref-031, ref-051, ref-076, ref-090, ref-104, ref-111, ref-125, ref-129, ref-130, ref-138, ref-159, ref-168, ref-199, ref-210, ref-230, ref-234, ref-238, ref-239, ref-240, ref-253, ref-283, ref-284, ref-286, ref-314, ref-315, ref-316, ref-317, ref-351, ref-353, ref-399, ref-405, ref-407, ref-408, ref-417, ref-465, ref-466, ref-470, ref-472, ref-473, ref-475, ref-476, ref-494, ref-516, ref-518, ref-531, ref-539, ref-541, ref-554, ref-559, ref-561, ref-567, ref-583, ref-589, ref-606, ref-607, ref-608, ref-618, ref-623, ref-625, ref-626, ref-635, ref-677, ref-679, ref-706, ref-709, ref-710]
---

[홈](../../index.md) › G. 안전·보안·지능·거버넌스

# G. 안전·보안·지능·거버넌스

## 핵심 질문

전체 영역에 어떤 공통 제약과 관리 체계를 적용할 것인가? [분류원문]

## 개요

위 여섯 영역 전체에 적용되는 연구다. 마지막에 추가하는 부가기능으로 보면 누락되기 쉽다. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·SCM 관점의 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **25. 안전·위험 관리** | 로봇·사람·설비 상호작용의 위험, 안전 조건, 정지·재개 절차, 비상 상황 대응, 안전 책임 경계 | 여러 장비는 각각 안전해도 함께 움직일 때 새로운 위험이 생기지 않는가? | [25. 안전·위험 관리](25-safety-and-risk-management.md) | published |
| **26. 사이버보안·접근권한·개인정보** | 장비 인증, 통신 보호, 명령 권한, 원격 접속, 고객별 격리, 영상·작업자 데이터 보호 | 외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가? | [26. 사이버보안·접근권한·개인정보](26-cybersecurity-access-control-and-privacy.md) | published |
| **27. AI·학습·적응과 모델 운영** | 문서·도면 해석, 수요·고장 예측, 학습 기반 계획, LLM 에이전트, 불확실성 평가, 모델 변경 관리 | AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? | [27. AI·학습·적응과 모델 운영](27-ai-learning-adaptation-and-model-operations.md) | published |
| **28. 표준·상호운용성·다사업자 거버넌스** | 공통 규격, 적합성 시험, 제조사 간 책임, 데이터 소유권, API 변경 정책, 서비스 수준과 감사 이력 | 제조사·ROP·설비업체 중 누가 연동 오류를 수정하고 변경을 승인할까? | [28. 표준·상호운용성·다사업자 거버넌스](28-standards-interoperability-and-multi-vendor-governance.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

ROS 2도 인증·암호화·접근권한과 보안 위협 모델을 별도로 다룬다. 기능 연동과 보안 연동은 함께 설계해야 하는 영역이다. [9][10] [분류원문]

27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [분류원문]

## 다른 대분류와의 연결

G. 안전·보안·지능·거버넌스의 네 세부영역은 나머지 여섯 대분류의 세부영역에 공통 제약과 관리 체계로 걸린다. 아래 연결은 게시된 세부영역 페이지(25. 안전·위험 관리, 26. 사이버보안·접근권한·개인정보, 27. AI·학습·적응과 모델 운영, 28. 표준·상호운용성·다사업자 거버넌스)와 A~F 대분류 페이지의 연결 서술을 같은 각주로 다시 인용한 것이다(기준일 2026-09-25). 연결마다 출처가 하나이거나 발행 주체가 같은 출처여서, 교차 확인된 연결은 아직 없다.

### A. 업무·공급망 설계

- [A. 업무·공급망 설계](../a-business-supply-chain-design/index.md) — [28. 표준·상호운용성·다사업자 거버넌스](28-standards-interoperability-and-multi-vendor-governance.md) ↔ [1. 주문·업무 시스템 연계](../a-business-supply-chain-design/01-order-and-business-system-integration.md): ISA-95 계열 작업 지시 동사·메서드(B2MML의 CHANGE·CANCEL, OPC UA for ISA-95 Job Control)를 VDA 5050·Open-RMF 주문·작업 요청과 잇는 표준 매핑이 확인되지 않았다. 따라서 번역 규칙을 누가 소유하고 변경을 승인하는지가 거버넌스 과제로 넘어갈 것으로 보인다. [추정][^ref-129][^ref-130][^ref-031][^ref-125] 표준 매핑이 없다는 것은 조사 범위 안에서 관찰한 것이며, 부재가 확인되지는 않았다([oq-020](../../open-questions.md)).
- 같은 두 영역: 상위 업무 시스템에 여는 ROP API의 판 번호와 폐기 예고 정책은 ROP 몫으로 보인다. 그 규칙의 후보로 의미적 버전 관리(Semantic Versioning, SemVer 2.0.0)와 RFC 9745 Deprecation 헤더가 있다. [추정][^ref-635][^ref-706]
- [27. AI·학습·적응과 모델 운영](27-ai-learning-adaptation-and-model-operations.md) ↔ [1. 주문·업무 시스템 연계](../a-business-supply-chain-design/01-order-and-business-system-integration.md): 주문·납기 제약을 받는 배정·계획 모델의 버전과 변경 승인은 ROP 몫으로 보인다. 수요예측 모델은 분류 원문 9장의 상위 업무 시스템 경계에 따라 연계 대상으로 보인다. [추정][^ref-626][^ref-618]

### B. 공통 정보·환경 모델

- [B. 공통 정보·환경 모델](../b-common-information-and-environment-model/index.md) — [27. AI·학습·적응과 모델 운영](27-ai-learning-adaptation-and-model-operations.md) ↔ [5. 로봇 능력·작업 온톨로지](../b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md): 대규모 언어 모델(Large Language Model, LLM)로 능력 온톨로지를 생성하는 연구(2024-04)가 있다. 로봇 기술 파일(URDF)에서 로봇 온톨로지를 LLM으로 채우는 연구(2026-06)도 있다. 분류 원문 8장 교차 규칙의 매뉴얼 해석이 이 두 대분류를 잇는다. [사실][^ref-238][^ref-239]
- [27. AI·학습·적응과 모델 운영](27-ai-learning-adaptation-and-model-operations.md) ↔ [6. 지도·공간·위치 모델](../b-common-information-and-environment-model/06-map-space-and-location-model.md): 비전 언어 모델로 평면도 지도를 해석하는 연구(2024-09)가 있다. 교차 규칙의 도면 해석이 두 대분류를 잇는다. [사실][^ref-076]
- [28. 표준·상호운용성·다사업자 거버넌스](28-standards-interoperability-and-multi-vendor-governance.md) ↔ [5. 로봇 능력·작업 온톨로지](../b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md): 제조사와 무관하게 쓰는 정보 모델 표준으로 세 가지가 있다. 무인운반차 기술 데이터 서브모델 IDTA 02047, 서비스 로봇 모듈 공통 정보 모델 ISO 22166-201(2024-02), 국내 KS B 7321-2다. [사실][^ref-234][^ref-240][^ref-138] KS 부합화 여부는 [oq-004·oq-026](../../open-questions.md)에서 열려 있다.
- [28. 표준·상호운용성·다사업자 거버넌스](28-standards-interoperability-and-multi-vendor-governance.md) ↔ [6. 지도·공간·위치 모델](../b-common-information-and-environment-model/06-map-space-and-location-model.md): ISO 21423은 산업용 이동로봇의 통신·상호운용성을 다루는 ISO 표준이다(검색 결과상 FDIS 단계, 발행 여부 미확인). 그 공통 좌표계와 제조사 지도 식별자가 어떻게 대응하는지는 확인되지 않았다. [사실][^ref-159] 관련 질문은 [oq-027](../../open-questions.md)이다.
- [25. 안전·위험 관리](25-safety-and-risk-management.md) ↔ [8. 실시간 세계 상태·데이터 일관성](../b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md): Open-RMF 승강기 상태의 운영 모드에는 사람·AGV·화재·오프라인·비상이 있다. 따라서 탑승을 확정하기 전에 최신 모드를 확인하는 규칙이 안전 조건과 맞물릴 것으로 보인다. 설비 안전 제어 자체는 연계 대상이다. [추정][^ref-286]

### C. 연결·실행 기반

- [C. 연결·실행 기반](../c-connectivity-and-execution-foundation/index.md) — [25. 안전·위험 관리](25-safety-and-risk-management.md) ↔ [10. 설비·건물 시스템 연동](../c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md): 국가기술표준원은 2021-11 KS B 7317을 제정했다. 이 표준은 이동 로봇이 엘리베이터에 탑승할 때의 안전 요구사항과 평가 방법을 정한다. Open-RMF 승강기 상태의 운영 모드에는 화재·비상이 들어 있다. [사실][^ref-314][^ref-315][^ref-286] 승강기 탑승 안전과 설비 안전 제어 자체는 분류 원문 9장 시설·설비 제어 경계의 연계 대상이다.
- [25. 안전·위험 관리](25-safety-and-risk-management.md) ↔ [12. 명령·작업 실행의 신뢰성](../c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md): VDA 5050 3.0.0 상태 메시지의 safetyState는 비상정지 종류(eStop)와 보호 필드 침범(fieldViolation)을 보고한다. 명세는 스스로 기능·운영·시스템 안전 요구를 정하지 않으며, 안전 표준으로 적용해서는 안 된다고 밝힌다. [사실][^ref-031] ROP는 로봇이 보고한 안전 상태가 해제되고 운용 모드가 자동으로 돌아온 뒤 재개를 지시하는 운영 조율을 맡는다. 정지·재개 지시를 확실히 전달하는 문제는 12. 명령·작업 실행의 신뢰성과 맞물리는 것으로 보인다. [추정][^ref-031] 원격 비상정지 지시 경로가 성능 수준 요구를 받는지는 [oq-095](../../open-questions.md)에서 열려 있다.
- [26. 사이버보안·접근권한·개인정보](26-cybersecurity-access-control-and-privacy.md) ↔ [9. 로봇·제조사 관제 연동](../c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md)·[11. 분산 시스템·통신·컴퓨팅 구조](../c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md): ROS 2는 DDS 보안 규격의 인증·접근통제·암호화 플러그인을 쓴다. Open-RMF는 같은 신원과 접근통제 규칙을 공유하는 SROS 2 인클레이브(enclave)로 구성요소의 권한을 나눈다. 웹 대시보드에는 TLS(Transport Layer Security)와 OpenID Connect 기반 역할 토큰을 쓴다. [사실][^ref-009][^ref-405]
- [26. 사이버보안·접근권한·개인정보](26-cybersecurity-access-control-and-privacy.md) ↔ [9. 로봇·제조사 관제 연동](../c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md): VDA 5050 3.0.0에는 MQTT(Message Queuing Telemetry Transport)용 TLS 자격증명을 내려받는 사전 정의 동작 updateCertificate가 있다. 명세는 내려받기도 TLS로 보호하고, 인증서를 활성화하기 전에 인증서 체인을 검증하도록 권한다. [사실][^ref-031] 명세는 보안 기구 전체를 범위 밖에 둔다. 그래서 인증서 교체가 관제 연동 경로를 거치는 보안 명령이 된다는 것은 이 위키의 해석이다. [추정][^ref-031] 교체 시점·대상 승인과 실패 시 되돌림을 누가 책임지는지는 이번 실행에서 열린 질문으로 올렸다.
- 같은 두 영역: ROS 2 위협 모델 초안(최종 수정 2021-01)은 기본 사용자명·암호가 설정된 이미지에 SSH로 접속하는 경로를 진입점으로 든다. CISA 권고(ICSA-21-280-02)는 MiR 차량과 플릿 소프트웨어의 취약점으로 로봇 제어와 서비스 거부가 가능하다고 보고했다. [사실][^ref-010][^ref-583]
- [26. 사이버보안·접근권한·개인정보](26-cybersecurity-access-control-and-privacy.md) ↔ [10. 설비·건물 시스템 연동](../c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md): 로봇 관제가 문·승강기 어댑터에 요청을 보내는 구조에서는 어느 관제 구성요소가 어떤 설비 명령을 낼 수 있는지를 정해야 할 것으로 보인다. 그 단위는 인클레이브·권한 파일 같은 접근통제 단위이며, 공개된 구성이나 사례는 확인되지 않았다. [추정][^ref-405][^ref-283][^ref-284] 관련 질문은 [oq-043·oq-056](../../open-questions.md)이다.
- [28. 표준·상호운용성·다사업자 거버넌스](28-standards-interoperability-and-multi-vendor-governance.md) ↔ [9. 로봇·제조사 관제 연동](../c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md): VDA 5050 3.0.0은 경로 계산·교착 해소·교통 관리를 관제 기능으로, 위치 추정과 주문 실행을 이동로봇 기능으로 나눈다. 제조사 중립 연동의 기준은 VDA 5050 말고도 MassRobotics AMR 상호운용 표준과 ISO 21423이 있다. ISO 21423은 산업용 이동로봇의 통신·상호운용성을 다루는 ISO 표준이다(검색 결과상 FDIS 단계, 발행 여부 미확인). [사실][^ref-031][^ref-253][^ref-159]
- 같은 두 영역: 확인한 VDA 5050 적합성 시험 근거는 제3자 오픈소스 도구와 벤더 발표뿐이다. 따라서 어느 시험 결과를 연동 승인 기준으로 삼고, 누가 연동 오류를 판정할지가 거버넌스 과제로 넘어갈 것으로 보인다. 공식 인증 절차가 없다는 것은 확정되지 않았다. [추정][^ref-407][^ref-408][^ref-031] OTTO는 2026-04 VDA 5050 인증을 추가했다고 발표했으나, 시험 항목은 확인되지 않았다. [추정] 벤더 주장[^ref-608] 관련 질문은 [oq-055](../../open-questions.md)다.
- [28. 표준·상호운용성·다사업자 거버넌스](28-standards-interoperability-and-multi-vendor-governance.md) ↔ [10. 설비·건물 시스템 연동](../c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md): 국내에서는 로봇 엘리베이터 탑승 KS가 제정되었다. 대한승강기협회가 엘리베이터와 로봇 연동 단체표준을 제정했다는 기사도 있어, 설비 연동 표준이 두 대분류를 잇는 것으로 보인다. 단체표준의 원문과 발행일은 확인되지 않았다. [추정][^ref-709][^ref-316][^ref-317] 메시지 내용은 [oq-041](../../open-questions.md)에서 열려 있다.
- [27. AI·학습·적응과 모델 운영](27-ai-learning-adaptation-and-model-operations.md) ↔ [9. 로봇·제조사 관제 연동](../c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md): 오픈소스 ROS-MCP-Server는 rosbridge를 통해 ROS 기능을 LLM에게 도구로 노출한다. 노출하는 기능은 토픽 발행·구독, 서비스·액션 호출, 파라미터 설정이다. README는 권한 기능을 앞으로 기여받을 기능으로만 언급한다(2026-09-25 확인). [사실][^ref-679]
- [27. AI·학습·적응과 모델 운영](27-ai-learning-adaptation-and-model-operations.md)·[26. 사이버보안·접근권한·개인정보](26-cybersecurity-access-control-and-privacy.md) ↔ [12. 명령·작업 실행의 신뢰성](../c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md): 다음 판단은 트랙 [자연어 업무 지시 챗봇](../../tracks/nl-task-chatbot/index.md)의 실행 2026-09-25-71([단계 3](../../tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md))에서 이 위키가 종합한 것이다. LLM에 저수준 로봇 도구를 직접 열면 명령 상태 관리와 실행 전 검증을 우회할 수 있다. 그래서 ROP는 검증 경로로 들어가는 상위 도구(작업 요청 제출 등)만 노출해야 할 것으로 보인다. [추정][^ref-679][^ref-417] 출처는 도구 노출 방식과 실행 전 안전 게이트가 있다는 것만 뒷받침한다. 이 판단은 게시 전인 트랙 추정이다.
- 같은 두 영역: Tang 외(2026-06)는 산업용 다중 로봇을 위한 구조를 제안했다. 에이전트의 제안은 결정적 검증과 원자적 반영(atomic commit)을 거쳐야만 실행 상태·자원 잠금 기록에 받아들여진다. [사실][^ref-677] 이 연구는 산업용 다중 로봇을 대상으로 한 프리프린트이며, 물류 적용은 확인되지 않았다. 원문을 열지 못해 제안 주체가 LLM 에이전트로 한정되는지도 확인하지 않았다.
- C. 연결·실행 기반 페이지는 27. AI·학습·적응과 모델 운영과의 연결을 '근거 없음'으로 두었다. 위 세 항목은 그 페이지를 보강할 후보이며, 이번 실행에서는 C. 연결·실행 기반 페이지를 고치지 않았다.

### D. 계획·최적화

- [D. 계획·최적화](../d-planning-and-optimization/index.md) — [27. AI·학습·적응과 모델 운영](27-ai-learning-adaptation-and-model-operations.md) ↔ [13. 작업 배정 — MRTA](../d-planning-and-optimization/13-task-allocation-mrta.md): 분류 원문 8장 교차 규칙에 따라 학습 기반 배차 연구가 두 영역을 잇는다. 이종 그래프 어텐션 스케줄러, 창고 강화학습 배정 RTAW, LLM 기반 다중 로봇 작업 배정 연구가 그 예다. [사실][^ref-399][^ref-623][^ref-090][^ref-168] LLM 배정 결과 수치는 출처가 서로 달라([oq-030](../../open-questions.md)) 싣지 않는다.
- [27. AI·학습·적응과 모델 운영](27-ai-learning-adaptation-and-model-operations.md) ↔ [15. 다중 로봇 경로·교통 관리 — MAPF](../d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md)·[16. 공용 자원·충전·에너지 최적화](../d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md): 모방 학습을 적용한 지속형 MAPF 연구(2024-10)가 있다. 자율 피킹 로봇의 배터리 관리에 심층 강화학습을 쓰는 연구(2026-07)도 있다. [사실][^ref-199][^ref-531] 이 연구들로 보아 학습 기반 방법이 경로·충전 계획에도 들어와 두 대분류를 잇는 것으로 보인다. 두 연구 모두 프리프린트다. [추정][^ref-199][^ref-531]
- [26. 사이버보안·접근권한·개인정보](26-cybersecurity-access-control-and-privacy.md) ↔ [13. 작업 배정 — MRTA](../d-planning-and-optimization/13-task-allocation-mrta.md): 2026-08 프리프린트는 위치 스푸핑으로 오염된 에이전트가 롤아웃 기반 다중 로봇 배정·경로 계획의 비용 개선을 없앨 수 있다고 보고했다. 이 연구는 탐지된 적대 에이전트를 이후 계획에서 빼는 방법을 제안했으며, 실험은 GPS 스푸핑 데이터와 택시 수요로 했다. [사실][^ref-494] 물류센터 적용은 확인되지 않았다. 배정 전에 보고값을 검증하는 기준은 [oq-082](../../open-questions.md)에서 열려 있다.
- [25. 안전·위험 관리](25-safety-and-risk-management.md) ↔ [15. 다중 로봇 경로·교통 관리 — MAPF](../d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md): VDA 5050 3.0.0은 여러 구역 유형을 교통 관리 수단으로 정의한다. 진입 금지(BLOCKED)·해제(RELEASE)·속도 제한(SPEED_LIMIT)·우선(PRIORITY)·벌점(PENALTY) 같은 유형이다. 그러면서도 명세는 안전 표준으로 적용하지 말라고 밝힌다. [사실][^ref-031] Open-RMF는 긴급 작업을 높은 우선순위 참여자가 교통 협상을 강제하는 방식으로 다룬다. [사실][^ref-004]
- [25. 안전·위험 관리](25-safety-and-risk-management.md) ↔ [16. 공용 자원·충전·에너지 최적화](../d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md): Open-RMF 데모는 비상 경보가 켜지면 로봇들을 가장 가까운 주차 위치로 보낸다. 2025-04-04 기능 요청 이슈를 기준으로 하면, 비상 신호는 대상 플릿을 구분하지 않는 불리언 값이었다. [사실][^ref-104][^ref-567] 그 뒤 구현 여부는 확인되지 않았다.
- [28. 표준·상호운용성·다사업자 거버넌스](28-standards-interoperability-and-multi-vendor-governance.md) ↔ [15. 다중 로봇 경로·교통 관리 — MAPF](../d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md): VDA 5050은 교통 조율 전략을 명세에서 뺀다. Open-RMF에서는 시스템 통합사가 배치한 판정자가 협상 결과를 고른다. 따라서 한 현장의 우선권 판정 규칙을 누가 정하고 승인하는지가 거버넌스 과제로 넘어갈 것으로 보인다. [추정][^ref-031][^ref-004] 관련 질문은 oq-057이다.

### E. 협업·현장 운영

- [E. 협업·현장 운영](../e-collaboration-and-field-operations/index.md) — [25. 안전·위험 관리](25-safety-and-risk-management.md) ↔ [17. 로봇 간 협업·물리적 인계](../e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md): ANSI/A3 R15.08-2-2023은 이동 플랫폼에 로봇팔을 단 모바일 매니퓰레이터를 산업용 이동로봇 유형 C로 다룬다. 이 표준은 시스템·적용 단위의 안전 요구를 정한다. [사실][^ref-210][^ref-472] 국내 대응 KS는 [oq-064](../../open-questions.md)에서 열려 있다.
- [25. 안전·위험 관리](25-safety-and-risk-management.md) ↔ [17. 로봇 간 협업·물리적 인계](../e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md)·[18. 사람–로봇 협업·운영 인터페이스](../e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md): 사람 감지·보호 필드·비상정지 같은 안전 기능은 제조사·통합사·설비 쪽의 연계 대상으로 보인다. ROP는 로봇이 보고한 안전 상태를 표시하고, 재개와 수동 전환 승인을 작업 흐름에 반영하는 쪽을 맡는 경계로 보인다. [추정][^ref-470][^ref-051][^ref-210]
- [25. 안전·위험 관리](25-safety-and-risk-management.md) ↔ [18. 사람–로봇 협업·운영 인터페이스](../e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md): 국내에서는 고용노동부가 2023-07 고정식·이동식 산업용 로봇의 협동작업 안전 가이드를 배포했다. 중소벤처기업부는 2024-11 이동식 협동로봇 안전기준 산업표준을 제정했다고 발표했다. [사실][^ref-473][^ref-475][^ref-561] 제정된 KS의 번호와 내용은 [oq-070](../../open-questions.md)에서 열려 있다.
- [27. AI·학습·적응과 모델 운영](27-ai-learning-adaptation-and-model-operations.md)·[25. 안전·위험 관리](25-safety-and-risk-management.md) ↔ [18. 사람–로봇 협업·운영 인터페이스](../e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md): 관련 연구로 세 가지가 있다. LLM 계획기가 불확실할 때 사람에게 되묻는 연구(KnowNo, 2023-07), 사용자 명령의 모호성을 해소하는 연구(CLARA, 2024), 자연어 명령을 실행하기 전에 거치는 안전 게이트 연구(SafeGate, 2026-04)다. [사실][^ref-351][^ref-353][^ref-417] 세 연구의 실험 환경은 물류 현장이 아니다.
- [27. AI·학습·적응과 모델 운영](27-ai-learning-adaptation-and-model-operations.md) ↔ [19. 모니터링·이상 탐지·원인 분석](../e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md): Das 외(2021-01)는 로봇 실패 설명을 생성해 사용자의 고장 복구 지원을 개선하는 연구를 발표했다. [사실][^ref-476] 이 연구는 분류 원문 8장 교차 규칙의 장애 분석에 해당하며, 두 대분류를 잇는 근거로 보인다. [추정][^ref-476]
- [28. 표준·상호운용성·다사업자 거버넌스](28-standards-interoperability-and-multi-vendor-governance.md) ↔ [19. 모니터링·이상 탐지·원인 분석](../e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md): VDA 5050 오류 수준, MassRobotics 운용 상태, Open-RMF 작업 상태는 서로 다른 어휘이고, 셋을 잇는 공통 매핑 표준은 확인되지 않았다. 따라서 이종 플릿의 오류·원인 범주 해석 규칙을 누가 정하고 바꾸는지가 거버넌스 과제로 넘어갈 것으로 보인다. [추정][^ref-051][^ref-230][^ref-111] 관련 질문은 oq-033·oq-073이다.
- [26. 사이버보안·접근권한·개인정보](26-cybersecurity-access-control-and-privacy.md) ↔ [18. 사람–로봇 협업·운영 인터페이스](../e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md): 근로자참여 및 협력증진에 관한 법률 제20조는 사업장 안의 근로자 감시 설비 설치를 노사협의회 협의 사항으로 둔다(해당 호 번호는 미확인). [사실][^ref-589] ROS 2 위협 모델 초안은 카메라 영상을 사적 데이터로 분류한다. [사실][^ref-010] 따라서 카메라를 단 로봇이 작업자를 촬영하는 현장에서는 영상 수집 조건이 사람–로봇 협업의 제약이 될 것으로 보인다. [추정][^ref-589][^ref-010] 어느 규정이 적용되는지는 [oq-099](../../open-questions.md)에서 열려 있다.
- [25. 안전·위험 관리](25-safety-and-risk-management.md) ↔ [20. 예외 복구·재계획·업무 연속성](../e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md): 비상이 해제된 뒤 어떤 작업을 어떤 순서로 재개할지, 대상 플릿을 어떻게 구분할지가 출하 마감 준수에 영향을 준다. 그래서 비상 대응 뒤의 재개는 예외 복구 과제로 넘어가는 것으로 보인다. [추정][^ref-567][^ref-004]
- [26. 사이버보안·접근권한·개인정보](26-cybersecurity-access-control-and-privacy.md) ↔ [20. 예외 복구·재계획·업무 연속성](../e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md): 출하 마감 중에 오류 로봇을 제조사 원격 유지보수로 복구하는 상황이 있다. 이때 대상 로봇과 진단 명령만 허용하고, 이동 명령은 막고, 세션을 감사 기록으로 남기는 권한 제약이 복구 속도와 맞물릴 것으로 보인다. [추정][^ref-010][^ref-583][^ref-405] 로봇·명령 단위 권한 매트릭스를 정한 공개 표준은 [oq-100](../../open-questions.md)에서 열려 있다.
- E. 협업·현장 운영 페이지는 26. 사이버보안·접근권한·개인정보와의 연결을 '근거 없음'으로 두었다. 위 18. 사람–로봇 협업·운영 인터페이스, 20. 예외 복구·재계획·업무 연속성 연결 두 건은 그 페이지를 보강할 후보이며, 이번 실행에서는 E. 협업·현장 운영 페이지를 고치지 않았다.

### F. 도입·검증·유지관리

- [F. 도입·검증·유지관리](../f-deployment-verification-and-maintenance/index.md) — 연계 대상: [25. 안전·위험 관리](25-safety-and-risk-management.md) ↔ [21. 온보딩·설정·현장 시운전](../f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md)·[23. 시험·형식 검증·벤치마크](../f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md): ISO 3691-4:2023은 무인 산업 차량과 그 시스템의 안전 요구와 검증 수단을 정하고, 운용 구역 준비를 부속서 A에 둔다. [사실][^ref-470] 이는 로봇 자체 안전 기능 쪽 내용이며, 세부 시험 항목은 확인되지 않았다.
- [25. 안전·위험 관리](25-safety-and-risk-management.md) ↔ [24. 자산·소프트웨어 수명주기 관리](../f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md): 업체(세이프틱스) 자료는 설비·작업을 바꿀 때 위험성평가를 다시 하도록 권한다. 이로 보아 펌웨어·안전 파라미터·오케스트레이션 정책 변경이 재평가를 촉발하는 조건이 될 수 있어 보인다. 근거는 이 업체 자료 하나뿐이며, 국내 공식 규정은 확인되지 않았다. [추정][^ref-559] 관련 질문은 [oq-092·oq-093](../../open-questions.md)이다.
- [26. 사이버보안·접근권한·개인정보](26-cybersecurity-access-control-and-privacy.md) ↔ [24. 자산·소프트웨어 수명주기 관리](../f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md): IEC TR 62443-2-3:2015는 산업 자동화·제어 시스템 환경의 패치 관리를 다룬다. ROS 2 위협 모델 초안은 빌드 팜과 개발자 작업 환경을 거치는 공급망 위협에 대한 완화책으로 바이너리 서명과 소스 감사를 든다. [사실][^ref-554][^ref-010]
- [27. AI·학습·적응과 모델 운영](27-ai-learning-adaptation-and-model-operations.md) ↔ [21. 온보딩·설정·현장 시운전](../f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md)·[23. 시험·형식 검증·벤치마크](../f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md): 자연어 능력 설명에서 LLM으로 능력 온톨로지를 생성하는 방법(2024-06)이 제안되었다. ALFRED와 LoTa-Bench는 자연어 지시를 행동 계획으로 바꾸는 체화 에이전트를 시뮬레이터 결과로 자동 평가하는 공개 벤치마크다. 두 벤치마크는 물류 지시 데이터셋이 아니다. [사실][^ref-465][^ref-539][^ref-541] 분류 원문 8장 교차 규칙의 매뉴얼 해석이 21. 온보딩·설정·현장 시운전에 적용되는 예다.
- [27. AI·학습·적응과 모델 운영](27-ai-learning-adaptation-and-model-operations.md) ↔ [24. 자산·소프트웨어 수명주기 관리](../f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md): 24. 자산·소프트웨어 수명주기 관리의 정의에는 모델 버전과 배포·복구가 들어 있다. 따라서 학습 배차 모델을 교체할 때 모델 레지스트리의 버전·별칭과 운영 준비도 시험 기준으로 관리하는 일이 두 대분류를 잇는 것으로 보인다. [추정][^ref-626][^ref-625] 이 연결은 아직 어느 대분류 페이지에도 없다.
- [28. 표준·상호운용성·다사업자 거버넌스](28-standards-interoperability-and-multi-vendor-governance.md) ↔ [22. 시뮬레이션·예측용 디지털 트윈](../f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md): 제조용 디지털 트윈 프레임워크 ISO 23247은 국내에 KS X ISO 23247-1로 등재되어 있다. 2026년에는 디지털 트윈 결합을 다루는 Part 6이 발행되었다. 다만 이 표준은 제조를 대상으로 한다. [사실][^ref-516][^ref-518] 물류센터에 적용할 수 있는지는 [oq-085](../../open-questions.md)에서 열려 있다. 이 연결은 가정한 미래를 실험하는 22. 시뮬레이션·예측용 디지털 트윈 쪽이며, 현재 상태를 표현하는 8. 실시간 세계 상태·데이터 일관성과는 구분한다.
- [28. 표준·상호운용성·다사업자 거버넌스](28-standards-interoperability-and-multi-vendor-governance.md) ↔ [23. 시험·형식 검증·벤치마크](../f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md): 국내에는 로봇 자체 성능 시험(KS B ISO 18646-1, 한국로봇산업진흥원 시험평가)이 있다. 소프트웨어 모듈 정보모델의 상호운용성 시험 절차(KOROS 1148-8:2025)도 있다. 로봇 성능 시험은 시험기관이 맡고, ROP는 그 결과를 연동 승인·등록 조건으로 받는 쪽으로 보인다. [추정][^ref-606][^ref-607][^ref-710][^ref-466] 관련 질문은 [oq-089·oq-111](../../open-questions.md)이다.
- [28. 표준·상호운용성·다사업자 거버넌스](28-standards-interoperability-and-multi-vendor-governance.md) ↔ [24. 자산·소프트웨어 수명주기 관리](../f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md): 관제는 VDA 5050 헤더의 version으로 판 차이를 감지한다. 로봇이 지원하지 않는 선택 필드는 UNSUPPORTED_PARAMETER 오류로 드러난다. 따라서 펌웨어·프로토콜 판을 이행할 때 호환 시험과 수정 책임을 누가 지는지가 두 대분류 사이의 과제로 보인다. [추정][^ref-031][^ref-051][^ref-635] 관련 질문은 [oq-091](../../open-questions.md)이다.

### 아직 다루지 않은 연결

다음 연결은 아직 근거를 찾지 못해 쓰지 않았다.

- 11. 분산 시스템·통신·컴퓨팅 구조 ↔ 25. 안전·위험 관리, 27. AI·학습·적응과 모델 운영
- 7. 화물·재고·자산 식별과 추적 ↔ 25. 안전·위험 관리, 26. 사이버보안·접근권한·개인정보, 27. AI·학습·적응과 모델 운영, 28. 표준·상호운용성·다사업자 거버넌스
- 14. 작업 순서·스케줄링 ↔ 25. 안전·위험 관리, 26. 사이버보안·접근권한·개인정보, 27. AI·학습·적응과 모델 운영, 28. 표준·상호운용성·다사업자 거버넌스
- 2. 공정·워크플로 모델링, 3. 처리능력·거점·설비 계획, 4. 성과·경제성·프로세스 개선 ↔ 25. 안전·위험 관리, 26. 사이버보안·접근권한·개인정보

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
[^ref-677]: Tang, G. 외(arXiv 2606.31339), Verification-Gated Agentic Mission-State Governance for Intelligent Industrial Multi-Robot Systems, 2026-06, https://arxiv.org/abs/2606.31339, 접근일 2026-09-25 (원문 미열람)
[^ref-679]: robotmcp (ROS-MCP-Server 공식 저장소), ros-mcp-server — Connect AI models like Claude & GPT with robots using MCP and ROS (GitHub README), 미확인, https://github.com/robotmcp/ros-mcp-server, 접근일 2026-09-25
[^ref-706]: IETF (RFC Editor), RFC 9745: The Deprecation HTTP Response Header Field, 미확인, https://www.rfc-editor.org/info/rfc9745/, 접근일 2026-09-25 (원문 미열람)
[^ref-709]: 대한민국 정책브리핑(산업통상자원부 국가기술표준원), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11-11, https://korea.kr/news/pressReleaseView.do?newsId=156480155, 접근일 2026-09-25 (원문 미열람)
[^ref-710]: 한국지능형로봇표준포럼(KOROS), KOROS 1148-8:2025 서비스 로봇을 위한 모듈 - 제2-8부 : 소프트웨어 모듈용 정보모델 상호운용성 시험 절차, 2025-06-04, http://www.koros.or.kr/bbs/board.php?bo_table=notice27&wr_id=223, 접근일 2026-09-25 (원문 미열람)

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-25 · 갱신 · [28. 표준·상호운용성·다사업자 거버넌스](28-standards-interoperability-and-multi-vendor-governance.md) — seed → draft: 3~11절 첫 작성, 페이지 상태 자동 영역 추가, 13절 각주. 2차: 9절 승강기 연계 칸 [추정]으로 정정, ISO 10218-2 적용 범위 미확인 단서 추가, 5절 시작 조건 칸에 가상 설정 표시와 [추정] 태그 추가 (실행 2026-09-25-69)
- 2026-09-25 · 생성 · [28. 표준·상호운용성·다사업자 거버넌스 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area28-s7.md) — 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,840자)을 옮겼다 (실행 2026-09-25-69)
- 2026-09-25 · 생성 · [28. 표준·상호운용성·다사업자 거버넌스 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area28-s6.md) — 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "6. 대표 접근법과 기술" 절(1,549자)을 옮겼다 (실행 2026-09-25-69)
- 2026-09-25 · 생성 · [28. 표준·상호운용성·다사업자 거버넌스 — 열린 질문](../../topics/2026/2026-09-25-area28-s11.md) — 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "11. 열린 질문" 절(1,233자)을 옮겼다 (실행 2026-09-25-69)
- 2026-09-25 · 생성 · [28. 표준·상호운용성·다사업자 거버넌스 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area28-s4.md) — 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "4. 핵심 개념과 용어" 절(1,053자)을 옮겼다 (실행 2026-09-25-69)
<!-- auto:category-recent:end -->

## 참고 자료

원문의 [9]는 참고문헌 [ref-009](../../references/ref-009.md)에 해당한다.[^ref-009] 원문의 [10]은 참고문헌 [ref-010](../../references/ref-010.md)에 해당한다.[^ref-010]

[^ref-009]: ROS 2 Design, ROS 2 DDS-Security Integration, 미확인, https://design.ros2.org/articles/ros2_dds_security.html, 접근일 2026-09-24
[^ref-010]: ROS 2 Design, ROS 2 Robotic Systems Threat Model, 미확인, https://design.ros2.org/articles/ros2_threat_model.html, 접근일 2026-09-24
```

### docs/categories/g-safety-security-intelligence-and-governance/index.md

```markdown
---
title: "G. 안전·보안·지능·거버넌스"
type: category
status: seed
created: 2026-09-24
updated: 2026-09-24
version: 1
---

[홈](../../index.md) › G. 안전·보안·지능·거버넌스

# G. 안전·보안·지능·거버넌스

## 핵심 질문

전체 영역에 어떤 공통 제약과 관리 체계를 적용할 것인가? [분류원문]

## 개요

위 여섯 영역 전체에 적용되는 연구다. 마지막에 추가하는 부가기능으로 보면 누락되기 쉽다. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·SCM 관점의 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | SCM 관점의 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **25. 안전·위험 관리** | 로봇·사람·설비 상호작용의 위험, 안전 조건, 정지·재개 절차, 비상 상황 대응, 안전 책임 경계 | 여러 장비는 각각 안전해도 함께 움직일 때 새로운 위험이 생기지 않는가? | [25. 안전·위험 관리](25-safety-and-risk-management.md) | published |
| **26. 사이버보안·접근권한·개인정보** | 장비 인증, 통신 보호, 명령 권한, 원격 접속, 고객별 격리, 영상·작업자 데이터 보호 | 외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가? | [26. 사이버보안·접근권한·개인정보](26-cybersecurity-access-control-and-privacy.md) | published |
| **27. AI·학습·적응과 모델 운영** | 문서·도면 해석, 수요·고장 예측, 학습 기반 계획, LLM 에이전트, 불확실성 평가, 모델 변경 관리 | AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? | [27. AI·학습·적응과 모델 운영](27-ai-learning-adaptation-and-model-operations.md) | published |
| **28. 표준·상호운용성·다사업자 거버넌스** | 공통 규격, 적합성 시험, 제조사 간 책임, 데이터 소유권, API 변경 정책, 서비스 수준과 감사 이력 | 제조사·ROP·설비업체 중 누가 연동 오류를 수정하고 변경을 승인할까? | [28. 표준·상호운용성·다사업자 거버넌스](28-standards-interoperability-and-multi-vendor-governance.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

ROS 2도 인증·암호화·접근권한과 보안 위협 모델을 별도로 다룬다. 기능 연동과 보안 연동은 함께 설계해야 하는 영역이다. [9][10] [분류원문]

27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [분류원문]

## 다른 대분류와의 연결

아직 작성되지 않음(에이전트가 채운다).

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-25 · 갱신 · [28. 표준·상호운용성·다사업자 거버넌스](28-standards-interoperability-and-multi-vendor-governance.md) — seed → draft: 3~11절 첫 작성, 페이지 상태 자동 영역 추가, 13절 각주. 2차: 9절 승강기 연계 칸 [추정]으로 정정, ISO 10218-2 적용 범위 미확인 단서 추가, 5절 시작 조건 칸에 가상 설정 표시와 [추정] 태그 추가 (실행 2026-09-25-69)
- 2026-09-25 · 생성 · [28. 표준·상호운용성·다사업자 거버넌스 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area28-s7.md) — 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,840자)을 옮겼다 (실행 2026-09-25-69)
- 2026-09-25 · 생성 · [28. 표준·상호운용성·다사업자 거버넌스 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area28-s6.md) — 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "6. 대표 접근법과 기술" 절(1,549자)을 옮겼다 (실행 2026-09-25-69)
- 2026-09-25 · 생성 · [28. 표준·상호운용성·다사업자 거버넌스 — 열린 질문](../../topics/2026/2026-09-25-area28-s11.md) — 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "11. 열린 질문" 절(1,233자)을 옮겼다 (실행 2026-09-25-69)
- 2026-09-25 · 생성 · [28. 표준·상호운용성·다사업자 거버넌스 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area28-s4.md) — 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "4. 핵심 개념과 용어" 절(1,053자)을 옮겼다 (실행 2026-09-25-69)
<!-- auto:category-recent:end -->

## 참고 자료

원문의 [9]는 참고문헌 [ref-009](../../references/ref-009.md)에 해당한다.[^ref-009] 원문의 [10]은 참고문헌 [ref-010](../../references/ref-010.md)에 해당한다.[^ref-010]

[^ref-009]: ROS 2 Design, ROS 2 DDS-Security Integration, 미확인, https://design.ros2.org/articles/ros2_dds_security.html, 접근일 2026-09-24
[^ref-010]: ROS 2 Design, ROS 2 Robotic Systems Threat Model, 미확인, https://design.ros2.org/articles/ros2_threat_model.html, 접근일 2026-09-24
```

### runs/2026-09-25-73/docs_tree.txt

```text
about/agents.md
about/how-to-contribute.md
about/idea-mapping.md
about/reading-guide.md
about/research-method.md
about/scope-boundary.md
about/what-is-rop.md
categories/a-business-supply-chain-design/01-order-and-business-system-integration.md
categories/a-business-supply-chain-design/02-process-and-workflow-modeling.md
categories/a-business-supply-chain-design/03-capacity-site-and-facility-planning.md
categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md
categories/a-business-supply-chain-design/index.md
categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md
categories/b-common-information-and-environment-model/06-map-space-and-location-model.md
categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md
categories/b-common-information-and-environment-model/08-real-time-world-state-and-data-consistency.md
categories/b-common-information-and-environment-model/index.md
categories/c-connectivity-and-execution-foundation/09-robot-and-vendor-fleet-manager-integration.md
categories/c-connectivity-and-execution-foundation/10-facility-and-building-system-integration.md
categories/c-connectivity-and-execution-foundation/11-distributed-systems-communication-and-computing.md
categories/c-connectivity-and-execution-foundation/12-command-and-task-execution-reliability.md
categories/c-connectivity-and-execution-foundation/index.md
categories/d-planning-and-optimization/13-task-allocation-mrta.md
categories/d-planning-and-optimization/14-task-sequencing-and-scheduling.md
categories/d-planning-and-optimization/15-multi-robot-path-and-traffic-management-mapf.md
categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md
categories/d-planning-and-optimization/index.md
categories/e-collaboration-and-field-operations/17-robot-to-robot-collaboration-and-physical-handover.md
categories/e-collaboration-and-field-operations/18-human-robot-collaboration-and-operator-interface.md
categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md
categories/e-collaboration-and-field-operations/20-exception-recovery-replanning-and-business-continuity.md
categories/e-collaboration-and-field-operations/index.md
categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md
categories/f-deployment-verification-and-maintenance/22-simulation-and-predictive-digital-twin.md
categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md
categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md
categories/f-deployment-verification-and-maintenance/index.md
categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md
categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md
categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md
categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md
categories/g-safety-security-intelligence-and-governance/index.md
changelog.md
corrections.md
flow-matrix.md
glossary/action-dependency-graph.md
glossary/age-of-information.md
glossary/aggregation-event.md
glossary/ariac.md
glossary/artificial-intelligence-management-system.md
glossary/asset-administration-shell.md
glossary/association-event.md
glossary/audit-trail.md
glossary/b2mml.md
glossary/battery-swapping.md
glossary/behavior-tree.md
glossary/block-reference.md
glossary/bpmn.md
glossary/building-information-modeling.md
glossary/building-topology-ontology.md
glossary/business-continuity-management-system.md
glossary/business-location.md
glossary/cap-theorem.md
glossary/capabilities-skills-services.md
glossary/capability-based-task-allocation.md
glossary/capability-matchmaking.md
glossary/cbv.md
glossary/collaborative-application.md
glossary/collaborative-perception.md
glossary/compensating-transaction.md
glossary/condition-based-maintenance.md
glossary/conflict-based-search.md
glossary/conformal-prediction.md
glossary/conformance-test.md
glossary/consensus-based-bundle-algorithm.md
glossary/cooperative-object-transport.md
glossary/cora.md
glossary/core-manufacturing-simulation-data.md
glossary/crdt.md
glossary/cross-schedule-dependency.md
glossary/dds-security.md
glossary/deadlock.md
glossary/digital-shadow.md
glossary/digital-thread.md
glossary/digital-twin-composition.md
glossary/digital-twin.md
glossary/discrete-event-simulation.md
glossary/dispenser-ingestor.md
glossary/distributed-tracing.md
glossary/drawing-exchange-format.md
glossary/eclass.md
glossary/enclave.md
glossary/epcis-error-declaration.md
glossary/epcis.md
glossary/fan-out.md
glossary/fault-detection-and-diagnosis-fdd.md
glossary/fault-injection.md
glossary/fleet-adapter.md
glossary/fleet-control-level.md
glossary/fleet-management-system.md
glossary/fleet-sizing.md
glossary/floor-plan-recognition.md
glossary/fog-computing.md
glossary/giai.md
glossary/goal-condition.md
glossary/grai.md
glossary/hallucination.md
glossary/hddl.md
glossary/hierarchical-task-network.md
glossary/high-impact-ai.md
glossary/human-in-the-loop.md
glossary/hungarian-method.md
glossary/idempotency-key.md
glossary/identity-report.md
glossary/iec-common-data-dictionary.md
glossary/ifc.md
glossary/index.md
glossary/indoor-mapping-data-format.md
glossary/indoor-space-subspacing.md
glossary/indoorgml.md
glossary/industrial-data.md
glossary/information-delivery-specification.md
glossary/information-for-use.md
glossary/intent-recognition.md
glossary/irdi.md
glossary/isa-95.md
glossary/job-shop-scheduling-problem.md
glossary/lane-closure.md
glossary/layout-interchange-format.md
glossary/lifelong-mapf.md
glossary/lift-adapter.md
glossary/linear-temporal-logic.md
glossary/littles-law.md
glossary/llm-agent.md
glossary/llm-modulo-framework.md
glossary/location-check-digit.md
glossary/managed-node.md
glossary/map-alignment.md
glossary/mapf.md
glossary/market-based-task-allocation.md
glossary/milp.md
glossary/mobile-manipulator.md
glossary/mobile-video-information-processing-device.md
glossary/model-checking.md
glossary/model-registry.md
glossary/mqtt.md
glossary/mrta.md
glossary/multi-agent-pickup-and-delivery.md
glossary/multi-fleet-orchestration.md
glossary/nearest-vehicle-first-rule.md
glossary/occupancy-grid-map.md
glossary/ocel.md
glossary/open-rmf.md
glossary/operating-mode.md
glossary/operating-zone.md
glossary/order-batching.md
glossary/over-the-air-update.md
glossary/overall-equipment-effectiveness.md
glossary/panoptic-symbol-spotting.md
glossary/pddl.md
glossary/perfect-order-fulfillment.md
glossary/plug-and-produce.md
glossary/precedence-constraint.md
glossary/priority-inheritance-with-backtracking.md
glossary/private-5g-network.md
glossary/process-mining.md
glossary/put-wall.md
glossary/raster-to-vector-conversion.md
glossary/read-point.md
glossary/regression-testing.md
glossary/release-zone.md
glossary/required-and-provided-capability.md
glossary/resource-constrained-project-scheduling-problem.md
glossary/risk-assessment.md
glossary/roadmap.md
glossary/robotic-mobile-fulfillment-system.md
glossary/root-cause-analysis-rca.md
glossary/runtime-verification.md
glossary/safe-interval-path-planning.md
glossary/saga.md
glossary/scor.md
glossary/semantic-id.md
glossary/semantic-versioning.md
glossary/semi-open-queueing-network.md
glossary/service-level-agreement.md
glossary/shacl.md
glossary/shifting-bottleneck-detection-active-period-method.md
glossary/signal-temporal-logic.md
glossary/situation-awareness-based-agent-transparency.md
glossary/skill.md
glossary/slot-filling.md
glossary/software-nameplate.md
glossary/space-graph.md
glossary/sscc.md
glossary/state-of-charge.md
glossary/state-of-health.md
glossary/stpa.md
glossary/structured-output.md
glossary/task-decomposition.md
glossary/time-window.md
glossary/topological-map.md
glossary/traversability.md
glossary/vda-5050-cancel-order.md
glossary/vda-5050-factsheet.md
glossary/vda-5050.md
glossary/verification-and-validation-of-simulation-models.md
glossary/virtual-commissioning.md
glossary/voice-picking.md
glossary/waveless-order-release.md
glossary/wes-wcs-wms-mes-tms.md
glossary/workflow-net.md
glossary/zone-set.md
glossary/zones-and-conduits.md
ideas/floorplan-recognition.md
ideas/index.md
ideas/nl-task-chatbot.md
ideas/robot-capability-ontology.md
index.md
logs/daily/2026-09-25.md
logs/index.md
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
references/ref-101.md
references/ref-102.md
references/ref-103.md
references/ref-104.md
references/ref-105.md
references/ref-106.md
references/ref-107.md
references/ref-108.md
references/ref-109.md
references/ref-110.md
references/ref-111.md
references/ref-112.md
references/ref-113.md
references/ref-114.md
references/ref-115.md
references/ref-116.md
references/ref-117.md
references/ref-118.md
references/ref-119.md
references/ref-120.md
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
references/ref-704.md
references/ref-705.md
references/ref-706.md
references/ref-707.md
references/ref-708.md
references/ref-709.md
references/ref-710.md
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
topics/index.md
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
tracks/nl-task-chatbot/experiments.md
tracks/nl-task-chatbot/index.md
tracks/nl-task-chatbot/log.md
tracks/nl-task-chatbot/question-backlog.md
tracks/nl-task-chatbot/stage-1-prior-work-and-products.md
tracks/nl-task-chatbot/stage-2-data-and-standards.md
tracks/nl-task-chatbot/stage-3-implementation-hypothesis.md
tracks/nl-task-chatbot/stage-4-misinterpretation-safeguards.md
tracks/nl-task-chatbot/stage-5-verification-and-hypotheses.md
tracks/nl-task-chatbot/task-model-draft.md
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 64건 / 전체 650건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 2026-09-25 | 예 |
| ref-009 | ROS 2 Design | ROS 2 DDS-Security Integration | 미확인 | https://design.ros2.org/articles/ros2_dds_security.html | 2026-09-25 | 예 |
| ref-010 | ROS 2 Design | ROS 2 Robotic Systems Threat Model | 미확인 | https://design.ros2.org/articles/ros2_threat_model.html | 2026-09-25 | 예 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 2026-09-25 | 예 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 2026-09-25 | 예 |
| ref-056 | Liu, J. X. 외 | Grounding Complex Natural Language Commands for Temporal Tasks in Unseen Environments | 2023-02 | https://arxiv.org/abs/2302.11649 | 2026-09-25 | 아니오 |
| ref-088 | Ahn, M. 외(Google) | Do As I Can, Not As I Say: Grounding Language in Robotic Affordances | 2022-04 | https://arxiv.org/abs/2204.01691 | 2026-09-25 | 아니오 |
| ref-092 | Liu, B., Jiang, Y., Zhang, X., Liu, Q., Zhang, S., Biswas, J., & Stone, P. | LLM+P: Empowering Large Language Models with Optimal Planning Proficiency | 2023-04 | https://arxiv.org/abs/2304.11477 | 2026-09-25 | 아니오 |
| ref-253 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — README | 미확인 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard | 2026-09-25 | 아니오 |
| ref-351 | Ren, A. Z. 외 | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners | 2023-07 | https://arxiv.org/abs/2307.01928 | 2026-09-25 | 아니오 |
| ref-354 | cog-model (AmbiK 저자) | AmbiK-dataset — README (AmbiK: Dataset of Ambiguous Tasks in Kitchen Environment) | 미확인 | https://github.com/cog-model/AmbiK-dataset | 2026-09-25 | 예 |
| ref-359 | Wang, W. 외 | Learning to Ask: When LLM Agents Meet Unclear Instruction | 2024-09 | https://arxiv.org/abs/2409.00557 | 2026-09-25 | 아니오 |
| ref-405 | Open Robotics | Security - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/security.html | 2026-09-25 | 예 |
| ref-407 | gpue (GitHub) | vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS) | 미확인 | https://github.com/gpue/vda5050-sim | 2026-09-25 | 예 |
| ref-408 | ekusiadadus (GitHub) | vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces) | 미확인 | https://github.com/ekusiadadus/vda5050-lab | 2026-09-25 | 예 |
| ref-417 | Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab) | Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems | 2026-04 | https://arxiv.org/abs/2604.05427 | 2026-09-25 | 아니오 |
| ref-470 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 2023-06 | https://www.iso.org/standard/83545.html | 2026-09-25 | 아니오 |
| ref-471 | A3(Association for Advancing Automation) | Updated ISO 10218 | Answers to Frequently Asked Questions (FAQs) | 미확인 | https://www.automate.org/robotics/blogs/updated-iso-10218-faq | 2026-09-25 | 아니오 |
| ref-472 | A3(Association for Advancing Automation) | ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available | 2023-10 | https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available | 2026-09-25 | 아니오 |
| ref-541 | lbaa2022 (LoTa-Bench 공식 저장소) | LLMTaskPlanning — LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents (ICLR 2024) (GitHub README) | 미확인 | https://github.com/lbaa2022/LLMTaskPlanning | 2026-09-25 | 예 |
| ref-555 | European Union (EUR-Lex) | Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery | 2023-06 | https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng | 2026-09-25 | 아니오 |
| ref-560 | ISO | ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells | 2025-02 | https://www.iso.org/standard/73934.html | 2026-09-25 | 아니오 |
| ref-561 | 대한민국 정책브리핑(중소벤처기업부) | 이동식 협동로봇 ‘안전기준 산업표준’ 제정…상용화 길 열어 | 2024-11-03 | https://www.korea.kr/news/policyNewsView.do?newsId=148935814 | 2026-09-25 | 아니오 |
| ref-563 | Belzile, B. 외 | From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment | 2025-02 | https://arxiv.org/abs/2502.20693 | 2026-09-25 | 아니오 |
| ref-564 | Bensaci, C., Zennir, Y., Pomorski, D. (IEEE Xplore) | A Comparative Study of STPA Hierarchical Structures in Risk Analysis: The Case of a Complex Multi-Robot Mobile System (EECS 2018 학회) | 2018-12 | https://ieeexplore.ieee.org/document/8910126/ | 2026-09-25 | 아니오 |
| ref-566 | CEN (iTeh Standards 카탈로그) | EN ISO 12100:2010 - Safety of machinery - General principles for design - Risk assessment and risk reduction | 2010 | https://standards.iteh.ai/catalog/standards/cen/74a41162-9d84-4410-a8a3-606630770ab9/en-iso-12100-2010 | 2026-09-25 | 아니오 |
| ref-567 | Open-RMF (open-rmf/rmf GitHub) | [Feature request]: Fire alarm separation for different fleets · Issue #658 · open-rmf/rmf | 2025-04-04 | https://github.com/open-rmf/rmf/issues/658 | 2026-09-25 | 아니오 |
| ref-579 | Open Robotics (ROS 2 Design) | ROS 2 Access Control Policies | 2019-08 | https://design.ros2.org/articles/ros2_access_control_policies.html | 2026-09-25 | 예 |
| ref-580 | Open Robotics (ROS 2 Design) | ROS 2 Security Enclaves | 2020-05 | https://design.ros2.org/articles/ros2_security_enclaves.html | 2026-09-25 | 예 |
| ref-581 | Eclipse Foundation (Eclipse Mosquitto) | mosquitto.conf man page | 미확인 | https://mosquitto.org/man/mosquitto-conf-5.html | 2026-09-25 | 예 |
| ref-582 | NIST | NIST SP 800-82 Rev. 3, Guide to Operational Technology (OT) Security | 2023-09 | https://csrc.nist.gov/pubs/sp/800/82/r3/final | 2026-09-25 | 아니오 |
| ref-583 | CISA | Mobile Industrial Robots Vehicles and MiR Fleet Software (ICSA-21-280-02) | 미확인 | https://www.cisa.gov/news-events/ics-advisories/icsa-21-280-02 | 2026-09-25 | 아니오 |
| ref-584 | CSA / IEC (ANSI Webstore) | CAN/CSA IEC 62443-3-3-2017 - Industrial communication networks - Network and system security - Part 3-3: System security requirements and security levels (Adopted IEC 62443-3-3:2013, first edition, 2013-08) | 2013-08 | https://webstore.ansi.org/standards/csa/csaiec624432017-2442576 | 2026-09-25 | 아니오 |
| ref-585 | Jaatun 외(Journal of Cybersecurity and Privacy 6(2), 52) | Security Aspects of Zones and Conduits in IEC 62443 | 2026 | https://www.mdpi.com/2624-800X/6/2/52 | 2026-09-25 | 아니오 |
| ref-587 | 법제처 국가법령정보센터 | 개인정보 보호법 | 미확인 | https://www.law.go.kr/lsEfInfoP.do?lsiSeq=195062 | 2026-09-25 | 아니오 |
| ref-588 | 김·장 법률사무소 | '이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서' 관련 인사이트 | 미확인 | https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=30477 | 2026-09-25 | 아니오 |
| ref-589 | 법제처 국가법령정보센터 | 근로자참여 및 협력증진에 관한 법률 | 미확인 | https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=105636 | 2026-09-25 | 아니오 |
| ref-590 | 한국인터넷진흥원(KISA) | 로봇 보안취약점 점검 체크리스트 해설서 | 미확인 | https://kisa.or.kr/2060205/form?lang_type=KO&page=&postSeq=36 | 2026-09-25 | 아니오 |
| ref-591 | European Commission (Shaping Europe's digital future) | The Cyber Resilience Act - Summary of the legislative text | 미확인 | https://digital-strategy.ec.europa.eu/en/policies/cra-summary | 2026-09-25 | 아니오 |
| ref-608 | OTTO by Rockwell Automation | OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments | 2026-04 | https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/ | 2026-09-25 | 아니오 |
| ref-617 | NIST | NIST Risk Management Framework Aims to Improve Trustworthiness of Artificial Intelligence | 2023-01-26 | https://nist.gov/news-events/news/2023/01/nist-risk-management-framework-aims-improve-trustworthiness-artificial | 2026-09-25 | 아니오 |
| ref-618 | ISO/IEC | ISO/IEC 42001:2023 - AI management systems | 2023 | https://www.iso.org/standard/42001 | 2026-09-25 | 아니오 |
| ref-619 | ISO/IEC | ISO/IEC 23894:2023 - AI — Guidance on risk management | 2023-02 | https://www.iso.org/standard/77304.html | 2026-09-25 | 아니오 |
| ref-620 | 국가법령정보센터(과학기술정보통신부) | 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법 | 미확인 | https://www.law.go.kr/lsInfoP.do?lsiSeq=268543 | 2026-09-25 | 아니오 |
| ref-621 | European Commission | AI Act | Shaping Europe's digital future | 미확인 | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | 2026-09-25 | 아니오 |
| ref-622 | Liang, J. 외 | Code as Policies: Language Model Programs for Embodied Control | 2022-09 | https://arxiv.org/abs/2209.07753 | 2026-09-25 | 아니오 |
| ref-623 | Agrawal, A. 외 | RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments | 2022-09 | https://arxiv.org/abs/2209.05738 | 2026-09-25 | 아니오 |
| ref-624 | Sculley, D. 외 | Hidden Technical Debt in Machine Learning Systems | 2015 | https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems | 2026-09-25 | 아니오 |
| ref-625 | Breck, E. 외 (Google Research) | The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction | 2017 | https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/ | 2026-09-25 | 아니오 |
| ref-626 | MLflow (Linux Foundation 오픈소스 프로젝트) | ML Model Registry | MLflow AI Platform | 미확인 | https://mlflow.org/docs/latest/ml/model-registry/ | 2026-09-25 | 아니오 |
| ref-627 | 머니투데이 | 포장은 로봇이, 간선운송은 무인차가…물류현장 스며든 '피지컬 AI' | 2026-09-19 | https://www.mt.co.kr/industry/2026/09/19/2026091818023697394 | 2026-09-25 | 아니오 |
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

### docs/glossary/index.md (요약: 용어 167개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- age-of-information: 정보 나이 (Age of Information (AoI))
- aggregation-event: 집계 이벤트 (AggregationEvent)
- ariac: 산업 자동화용 민첩 로봇 경진대회 (Agile Robotics for Industrial Automation Competition (ARIAC))
- artificial-intelligence-management-system: AI 관리 시스템 (Artificial Intelligence Management System (AIMS))
- asset-administration-shell: 자산관리셸 (Asset Administration Shell (AAS))
- association-event: 연결 이벤트 (AssociationEvent)
- audit-trail: 감사 추적 (Audit Trail)
- b2mml: B2MML (Business To Manufacturing Markup Language (B2MML))
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
- capability-matchmaking: 능력 매칭 (Capability Matchmaking)
- cbv: 핵심 업무 어휘 (Core Business Vocabulary (CBV))
- collaborative-application: 협동 적용 (Collaborative Application)
- collaborative-perception: 협동 인지 (Collaborative Perception)
- compensating-transaction: 보상 트랜잭션 (Compensating Transaction)
- condition-based-maintenance: 상태 기반 정비 (Condition-Based Maintenance (CBM))
- conflict-based-search: 충돌 기반 탐색 (Conflict-Based Search (CBS))
- conformal-prediction: 등각 예측 (Conformal Prediction)
- conformance-test: 적합성 시험 (Conformance Test)
- consensus-based-bundle-algorithm: 합의 기반 번들 알고리즘 (Consensus-Based Bundle Algorithm (CBBA))
- cooperative-object-transport: 협동 운반 (Cooperative Object Transport)
- cora: 로봇·자동화 핵심 온톨로지 (Core Ontology for Robotics and Automation (CORA))
- core-manufacturing-simulation-data: 핵심 제조 시뮬레이션 데이터 (Core Manufacturing Simulation Data (CMSD))
- crdt: 무충돌 복제 데이터 타입 (Conflict-free Replicated Data Type (CRDT))
- cross-schedule-dependency: 스케줄 간 의존 (Cross-schedule Dependency (XD))
- dds-security: DDS 보안 규격 (DDS Security (DDS-Security))
- deadlock: 교착 (Deadlock)
- digital-shadow: 디지털 섀도 (Digital Shadow)
- digital-thread: 디지털 스레드 (Digital Thread)
- digital-twin-composition: 디지털 트윈 결합 (Digital Twin Composition)
- digital-twin: 디지털 트윈 (Digital Twin)
- discrete-event-simulation: 이산 사건 시뮬레이션 (Discrete Event Simulation (DES))
- dispenser-ingestor: 디스펜서·인제스터 (Dispenser / Ingestor)
- distributed-tracing: 분산 추적 (Distributed Tracing)
- drawing-exchange-format: 도면 교환 형식 (Drawing Exchange Format (DXF))
- eclass: ECLASS (ECLASS)
- enclave: 인클레이브 (Enclave (SROS 2))
- epcis-error-declaration: 오류 선언 (Error Declaration (EPCIS errorDeclaration))
- epcis: 전자 제품 코드 정보 서비스 (Electronic Product Code Information Services (EPCIS))
- fan-out: 팬아웃 (Fan-out (human-robot team))
- fault-detection-and-diagnosis-fdd: 고장 탐지·진단 (Fault Detection and Diagnosis (FDD))
- fault-injection: 장애 주입 (Fault Injection)
- fleet-adapter: 플릿 어댑터 (Fleet Adapter)
- fleet-control-level: 플릿 제어 수준 (Fleet Control Level (Open-RMF: Full Control / Traffic Light / Read Only))
- fleet-management-system: 플릿 관리 시스템 (Fleet Management System (FMS))
- fleet-sizing: 차량 소요대수 산정 (Fleet Sizing)
- floor-plan-recognition: 평면도 인식 (Floor Plan Recognition)
- fog-computing: 포그 컴퓨팅 (Fog Computing)
- giai: 글로벌 개별 자산 식별자 (Global Individual Asset Identifier (GIAI))
- goal-condition: 목표 조건 (Goal Condition)
- grai: 글로벌 반환형 자산 식별자 (Global Returnable Asset Identifier (GRAI))
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
- isa-95: 기업–제어 시스템 통합 표준 (ISA-95 Enterprise-Control System Integration)
- job-shop-scheduling-problem: 작업장 스케줄링 문제 (Job Shop Scheduling Problem (JSSP))
- lane-closure: 차선 폐쇄 (Lane Closure)
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
- mobile-manipulator: 모바일 매니퓰레이터 (Mobile Manipulator)
- mobile-video-information-processing-device: 이동형 영상정보처리기기 (Mobile Video Information Processing Device)
- model-checking: 모델 검사 (Model Checking)
- model-registry: 모델 레지스트리 (Model Registry)
- mqtt: 메시지 큐잉 원격 측정 전송 (Message Queuing Telemetry Transport (MQTT))
- mrta: 다중 로봇 작업 배정 (Multi-Robot Task Allocation (MRTA))
- multi-agent-pickup-and-delivery: 다중 에이전트 픽업·배송 (Multi-Agent Pickup and Delivery (MAPD))
- multi-fleet-orchestration: 다중 플릿 오케스트레이션 (Multi-Fleet Orchestration)
- nearest-vehicle-first-rule: 최근접 차량 우선 규칙 (Nearest Vehicle First (NVF) Rule)
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
- operating-mode: 운용 모드 (Operating Mode (VDA 5050 operatingMode))
- operating-zone: 운용 구역 (Operating Zone (ISO 3691-4))
- order-batching: 주문 배치 (Order Batching)
- over-the-air-update: 무선 업데이트 (Over-the-Air Update (OTA))
- overall-equipment-effectiveness: 종합설비효율 (Overall Equipment Effectiveness (OEE))
- panoptic-symbol-spotting: 파놉틱 심볼 스포팅 (Panoptic Symbol Spotting)
- pddl: 계획 도메인 정의 언어 (Planning Domain Definition Language (PDDL))
- perfect-order-fulfillment: 완전 주문 이행률 (Perfect Order Fulfillment)
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- put-wall: 풋월 (Put Wall)
- raster-to-vector-conversion: 래스터–벡터 변환 (Raster-to-Vector Conversion)
- read-point: 판독 지점 (Read Point (EPCIS readPoint))
- regression-testing: 회귀 시험 (Regression Testing)
- release-zone: 해제 구역 (Release Zone)
- required-and-provided-capability: 요구 능력·제공 능력 (Required Capability / Provided (Offered) Capability)
- resource-constrained-project-scheduling-problem: 자원 제약 프로젝트 스케줄링 문제 (Resource-Constrained Project Scheduling Problem (RCPSP))
- risk-assessment: 위험성평가 (Risk Assessment (ISO 12100))
- roadmap: 경로망 (Roadmap)
- robotic-mobile-fulfillment-system: 로봇 이동형 풀필먼트 시스템 (Robotic Mobile Fulfillment System (RMFS))
- root-cause-analysis-rca: 근본 원인 분석 (Root Cause Analysis (RCA))
- runtime-verification: 런타임 검증 (Runtime Verification)
- safe-interval-path-planning: 안전 구간 경로 계획 (Safe Interval Path Planning (SIPP))
- saga: 사가 (Saga)
- scor: 공급망 운영 참조 모델 (Supply Chain Operations Reference (SCOR))
- semantic-id: 의미 식별자 (Semantic ID (semanticId))
- semantic-versioning: 의미적 버전 관리 (Semantic Versioning (SemVer))
- semi-open-queueing-network: 반개방형 대기행렬 네트워크 (Semi-Open Queueing Network (SOQN))
- service-level-agreement: 서비스 수준 협약 (Service Level Agreement (SLA))
- shacl: 형상 제약 언어 (Shapes Constraint Language (SHACL))
- shifting-bottleneck-detection-active-period-method: 이동 병목 탐지 (Shifting Bottleneck Detection (Active Period Method))
- signal-temporal-logic: 신호 시간 논리 (Signal Temporal Logic (STL))
- situation-awareness-based-agent-transparency: 상황 인식 기반 에이전트 투명성 (Situation Awareness-based Agent Transparency (SAT))
- skill: 스킬 (Skill)
- slot-filling: 슬롯 채우기 (Slot Filling)
- software-nameplate: 소프트웨어 명판 (Software Nameplate (IDTA 02007))
- space-graph: 공간 그래프 (Space Graph)
- sscc: 물류 단위 일련 코드 (Serial Shipping Container Code (SSCC))
- state-of-charge: 충전 상태 (State of Charge (SOC))
- state-of-health: 배터리 건강 상태 (State of Health (SOH))
- stpa: 시스템 이론적 프로세스 분석 (System-Theoretic Process Analysis (STPA))
- structured-output: 구조화 출력 (Structured Output)
- task-decomposition: 작업 분해 (Task Decomposition)
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- traversability: 통과 가능성 (Traversability)
- vda-5050-cancel-order: 주문 취소 즉시 동작 (cancelOrder (VDA 5050 instant action))
- vda-5050-factsheet: VDA 5050 팩트시트 (VDA 5050 factsheet)
- vda-5050: VDA 5050 (VDA 5050)
- verification-and-validation-of-simulation-models: 시뮬레이션 모델 검증·타당성 확인 (Verification and Validation (V&V) of Simulation Models)
- virtual-commissioning: 가상 시운전 (Virtual Commissioning)
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking))
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [25, 26, 27, 28] 에 걸린 38건 / 전체 112건)

```markdown
- oq-004 [열림] IEEE 1872 계열 로봇 온톨로지 표준이나 AAS 능력 서브모델을 KS로 부합화했거나 국내 로봇 관제 사업에 적용한 사례가 있는가? (영역 28, 5)
- oq-005 [열림] 출처 충돌: VDA 5050 3.0.0의 정확한 발행일은 언제인가? 검색 요약은 3.0 발행을 2026-03-19, 보도자료를 2026-04-20로 전하지만 보도자료 URL은 2026-04-21 계열이다. (영역 9, 28)
- oq-020 [열림] ISA-95 작업 지시·작업 응답(B2MML, OPC UA for ISA-95 Job Control)을 VDA 5050 주문·상태나 Open-RMF 작업 요청·상태로 옮기는 표준 매핑이나 공개 구현이 있는가? (영역 1, 9, 28)
- oq-025 [열림] 출처 충돌: VDMA LIF 의 판과 발행일은 무엇인가(VDA 5050 3.0.0 은 VDMA 2024-03 으로 인용하고, LIF 공식 저장소 README 는 1.0.0 판을 2023-09 로 적는다)? (영역 28, 6)
- oq-026 [열림] KS B 7321-2(서비스 로봇 모듈용 정보 모델 — 소프트웨어 모듈)가 ISO 22166-202와 부합화된 표준인지, 국내 물류 로봇·관제 사업에 적용한 사례가 있는가? (IEEE 1872 계열·AAS 능력 서브모델의 KS 부합화를 묻는 oq-004와 연결된다) (영역 28, 5)
- oq-027 [열림] ISO 21423 의 공통 좌표계(CCS)는 발행판에서 어떻게 정의되며, VDA 5050 mapId·Open-RMF 지도·층 이름·MassRobotics planarDatum 과 어떻게 대응하는가? (영역 6, 28)
- oq-030 [열림] 출처 충돌: LTAA(arXiv 2512.02810) 초록 요약은 로봇 전문화가 강한 설정에서 LLM 배정이 작업 완료율 77%로 전통 기법을 모두 앞섰다고 하지만, 다른 2차 요약은 동적 계획법의 완료율이 더 높다고 적는다. 어느 쪽이 원문 결과인가? (영역 13, 27)
- oq-041 [열림] 대한승강기협회 '엘리베이터와 로봇의 상호 연동을 위한 가이드라인' 단체표준은 어떤 메시지·상태(호출·탑승·하차·세션 해제 등)를 정하며, Open-RMF 승강기 요청·상태 메시지와 어떻게 대응하는가? (영역 10, 28)
- oq-043 [열림] 로봇 관제가 출입통제·건물 자동화 시스템(BACnet 등)을 통해 보안문을 여닫는 공개 설계나 국내 사례가 있고, 권한 확인은 누가 하는가? (영역 10, 26)
- oq-044 [열림] 국내에서 ISO 19164 나 IndoorGML 2.0 을 KS 로 부합화했거나, CityGML 2.0 과 IndoorGML 공간 개념을 원칙으로 둔 실내공간정보 구축 작업규정을 새 판 표준에 맞춰 개정한 사례가 있는가? (영역 6, 28)
- oq-055 [열림] VDA 5050 에 공식 적합성 시험·인증 절차가 있는가, 없다면 제3자 오픈소스 적합성 시험 도구의 결과를 새 로봇 연동 승인 기준으로 쓸 수 있는가? (영역 9, 23, 28)
- oq-056 [열림] 로봇 관제·플릿 어댑터·승강기·문 어댑터에 SROS 2 인클레이브와 권한 파일을 어떤 단위로 나눠 설비 명령 권한을 제한하는지 공개한 구성이나 사례가 있는가? (영역 10, 26)
- oq-064 [열림] 국내에 ANSI/A3 R15.08-2 의 유형 C(모바일 매니퓰레이터) 통합 안전 요구에 대응하는 KS 표준이나 인증 기준이 있는가? (영역 17, 25)
- oq-065 [열림] 제조사가 다른 이동로봇이 같은 충전기를 함께 쓸 수 있게 하는 충전 커넥터·충전 통신의 공통 규격이나 공개 사례가 있는가? (영역 16, 28)
- oq-070 [열림] 2024-11 제정된 이동식 협동로봇 안전기준 KS 의 표준 번호와 내용은 무엇이며, ISO 10218-2:2025·ISO 3691-4:2023 과 어떻게 대응하는가? (영역 18, 25)
- oq-082 [열림] 로봇·제조사 관제가 보고하는 위치·배터리·입찰 비용이 오염되거나 위조되었을 때 ROP 는 배정 전에 이를 어떻게 검증하고, 의심 로봇을 배정 후보에서 뺄 기준은 무엇인가? (영역 13, 26, 19)
- oq-085 [열림] 제조용 ISO 23247 디지털 트윈 프레임워크(참조 구조·디지털 트윈 결합)를 물류센터의 이종 로봇·설비에 그대로 적용할 수 있는가, 물류용 확장이 필요한가? (영역 22, 28)
- oq-089 [열림] 국내 시험기관(한국로봇산업진흥원 등)의 로봇 시험 항목에 다중 로봇 관제·오케스트레이션 소프트웨어 수준의 시험이 포함되는가, 없다면 누가 그 기준을 정하는가? (영역 23, 28)
- oq-091 [열림] VDA 5050 2.x 판과 3.0.0 판 로봇이 섞인 플릿에서 주 버전 차이를 어떻게 운영·이행하는가? (영역 24, 9, 28)
- oq-092 [열림] 국내 협동로봇 설치 작업장 안전인증에서 제어기 펌웨어·안전 파라미터 변경이 재심사 대상인지 공식 규정으로 확인할 수 있는가? (영역 24, 25)
- oq-093 [열림] EU 기계 규정의 실질적 변경 판단이 로봇 동작을 바꾸는 오케스트레이션 정책·어댑터 업데이트에도 적용되는가? (영역 24, 25)
- oq-095 [열림] ROP 가 VDA 5050 의 원격(REMOTE) 비상정지나 플릿 일괄 정지를 지시할 때 그 지시 경로가 안전 기능으로서 성능 수준(PL) 요구를 받는가, 아니면 운영 조율로만 보는가? (영역 25, 12)
- oq-096 [열림] 여러 제조사 로봇이 섞인 현장에서 R15.08-2 가 말하는 통합자의 시스템 수준 위험성평가를 ROP 사업자·제조사·설비업체 중 누가 수행하고 갱신하는가? (영역 25, 28)
- oq-097 [열림] 산업안전보건기준에 관한 규칙 제223조의 울타리 생략 인정이 물류센터의 자율이동로봇(AMR) 플릿에도 적용되며, 어떤 KS·국제 기준 부합이 요구되는가? (영역 25, 18)
- oq-099 [열림] 물류센터 내부처럼 공개되지 않은 작업장에서 카메라를 단 로봇이 작업자를 촬영할 때 개인정보 보호법 제25조의2와 근로자 감시 설비 협의 가운데 무엇이 적용되는지 공식 해석이 있는가? (영역 26, 18)
- oq-100 [열림] 외부 유지보수 계정의 권한을 로봇·명령 단위로 나눈 매트릭스(예: 진단은 허용, 이동은 불허)를 공개한 로봇 관제·ROP 구성이나 표준이 있는가? (영역 26, 9)
- oq-101 [열림] 여러 화주가 로봇 플릿을 공유하는 창고에서 고객별 작업·데이터 격리를 오케스트레이션 수준에서 규정한 표준이나 공개 설계가 있는가? (영역 26, 28)
- oq-102 [열림] ISO 10218-1:2025 의 사이버보안 요구는 어느 조항에서 무엇(접근 제한·원격 접속·로그 등)을 요구하며 로봇 관제 연동에 어떤 조건을 주는가? (영역 26, 25)
- oq-103 [열림] EU 기계 규정 부속서 III 1.1.9 의 적용일이 사이버 복원력법(2027-12-11)에 맞춰 연기되는지 확정됐는가? (영역 26, 25)
- oq-104 [열림] 창고 이동로봇 플릿의 재배정·재스케줄링 주기에서 LLM 추론 지연이 허용되는 한계를 측정했거나, LLM 을 결정 루프 밖에 둔 운영 사례가 있는가? (영역 14, 27)
- oq-105 [열림] 물류 현장 로봇의 작업 계획·배정에 쓰는 AI 가 한국 인공지능 기본법의 고영향 인공지능 영역에 해당하는가, 해당하면 ROP 사업자와 현장 운영사 중 누가 책무를 지는가? (영역 27, 28)
- oq-106 [열림] LLM 이나 학습 모델이 ROP 의 정지·경로·구역 결정에 관여할 때 EU AI Act 가 말하는 제품 안전 구성요소로 볼 수 있는가? (영역 27, 25)
- oq-107 [열림] KnowNo 의 등각 예측 보장은 보정 데이터와 운영 분포가 같다는 조건에 기대는데, 물류 지시 분포가 계절·고객에 따라 바뀔 때 보정을 얼마나 자주 다시 해야 하는가? (영역 27, 18)
- oq-108 [열림] 제조용 CMSD 같은 중립 시뮬레이션 데이터 형식을 물류센터 로봇 시뮬레이션의 입력(레이아웃·주문 흐름·재고·로봇 자원)에 쓴 사례가 있는가, 없다면 물류용 확장이 필요한가? (영역 22, 28)
- oq-109 [열림] ROP 사업자·로봇 제조사·현장 운영사가 함께 만든 로봇 운행·상태 데이터의 사용·수익 권리를 산업디지털전환촉진법의 공동 생성 규정에 따라 계약에서 어떻게 나누는가, 국내 로봇 관제 계약 사례가 있는가? (영역 28)
- oq-110 [열림] EU 데이터법의 데이터 공유 의무가 이종 로봇 플릿에서 제조사가 ROP 사업자(제3자)에게 로봇 사용 데이터를 제공해야 하는 근거가 되는가, 된다면 그 범위는 무엇인가? (영역 28, 9)
- oq-111 [열림] KOROS 1148-8:2025 의 상호운용성 시험 절차는 어떤 시험 항목을 두며, 물류 로봇 관제 연동의 적합성 시험 기준으로 쓸 수 있는가? (영역 28, 23)
- oq-112 [열림] 이종 플릿 현장에서 ROP 가 고객과 맺는 가용성·응답 시간 목표를 제조사 관제·설비업체의 서비스 수준 목표와 어떻게 연쇄해 맞추며, 공개된 계약 구조나 사례가 있는가? (영역 28, 20)
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
