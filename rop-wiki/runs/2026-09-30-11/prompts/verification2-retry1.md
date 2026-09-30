(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-30-11
- date: 2026-09-30
- run_type: area_deep_dive (영역 심화)
- 대상: 52. 통신 보호·위협 관리·감사 (N. 보안·개인정보)
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

### runs/2026-09-30-11/target.json

```json
{
  "run_id": "2026-09-30-11",
  "date": "2026-09-30",
  "weekday": "Wed",
  "run_number": 120,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 52,
    "area_name": "52. 통신 보호·위협 관리·감사",
    "category": "N. 보안·개인정보",
    "category_letter": "N"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=52"
}
```

### runs/2026-09-30-11/research.json

```json
{
  "run_id": "2026-09-30-11",
  "date": "2026-09-30",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 52,
    "area_name": "52. 통신 보호·위협 관리·감사",
    "category": "N. 보안·개인정보"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — STRIDE 위협 분류, 간접 프롬프트 주입, IEC 62443 보안 수준, 변조 탐지 로그 용어 없음",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 병원·가정·제조 공장의 통신·취약점 사례와 여섯 항목 정리 없음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — SROS 2(DDS-Security), 플릿 관리 서버·브로커 보안, LLM 계획의 실행 전 규칙 검사, 변조 방지 감사 기록 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — ROS 2 위협 모델, DDS-Security, IEC 62443, OWASP LLM01, VDA 5050 의 보안 위임, Open-RMF 보안, EU 기계류 규정, KISA 로봇 보안모델 위치 없음",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 oq-144 반영 필요",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "통신·문서·대화를 통한 공격이 로봇 동작으로 이어지지 않게 하려면? [분류원문]",
    "로봇·플랫폼·플릿 관리 서버 사이 통신을 인증·암호화하는 공개 수단(ROS 2 DDS-Security, 브로커 TLS 등)은 무엇이고, 상호운용 규격(VDA 5050, Open-RMF)은 보안을 어디까지 정하는가? (섹션 6·7 겨냥)",
    "로봇 시스템의 위협 모델과 취약점 관리 틀(ROS 2 위협 모델, IEC 62443)은 무엇을 요구하며, 병원·가정·제조 공장에서 보고된 실제 로봇 취약점 사례는 무엇인가? (섹션 5·7 겨냥, 한국 사례 우선)",
    "로봇 대화 지시에 특화된 프롬프트 주입·탈옥 방어(도구 설명 신뢰 경계, 실행 전 물리 제약 검사, 다중 모델 감독)의 효과를 잰 공개 벤치마크나 현장 시험 결과가 있는가? (oq-144, 섹션 6·8 겨냥)",
    "누가 언제 무엇을 지시·승인·변경했는지 지울 수 없게 기록하는 감사 기록에 대해 규제·표준·연구는 무엇을 요구·제안하는가? (섹션 4·6·7 겨냥)",
    "통신 보호·위협 관리·감사에서 ROP가 직접 맡을 것과 로봇 제조사·시설 IT/OT 에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "ROS 2 설계 문서 ‘ROS 2 Robotic Systems Threat Model’은 ROS 2 기반 로봇 시스템의 위협을 STRIDE(위조·변조·부인·정보 노출·서비스 거부·권한 상승)로 분류하고 DREAD 로 위험을 평가하며, TurtleBot 3 와 MARA 모듈형 로봇에 위협을 구체화하고, 통신 위협으로 구성요소 신원 위조, 메시지 가로채기·변조, 채널 무단 접근, 도청을 든다.",
      "tag": "사실",
      "source_ids": [
        "ref-010"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "2019-03 작성·2021-01 최종 수정. STRIDE 분류와 DREAD 위험 평가, 사례 TurtleBot 3 Burger·MARA. 위협 범주는 통신·소프트웨어·하드웨어·로그와 데이터이며 여러 완화책이 SROS(DDS 보안 확장) 활성화를 든다.",
      "as_of": "2021-01",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "같은 ROS 2 위협 모델 문서는 잘못된 메시지 이벤트를 기록하고 사용자에게 알리며 구성 변경도 기록해야 한다고 권고해, 통신 보호와 함께 감사 기록을 완화책으로 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-010"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원문 권고: ‘Invalid message events should be logged and users should be notified’. 구성 변경도 기록 대상으로 제시. 위협 범주에 로그·데이터의 유출·무단 접근 포함.",
      "as_of": "2021-01",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "ROS 2 설계 문서 ‘ROS 2 DDS-Security integration’에 따르면 DDS-Security 규격은 인증·접근 통제·암호(AES-GCM)·로깅·데이터 태깅의 다섯 플러그인 인터페이스를 두지만 ROS 2(SROS 2)는 앞의 셋만 쓰며, 로깅과 데이터 태깅은 규격 준수에 필수가 아니어서 모든 DDS 구현이 지원하지는 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-009",
        "ref-405"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Kyle Fazzari 작성(2019-07, 2020-07 수정). 인증은 공개 키 기반 구조, 접근 통제는 governance·permissions 파일. 로깅·데이터 태깅은 규격 준수에 필수 아님. Open-RMF 책 보안 장도 같은 내용을 싣는다(같은 ROS 계열 문서라 독립 확인으로 보지 않음).",
      "as_of": "2020-07",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "SROS 2 는 ROS_SECURITY_ENABLE·ROS_SECURITY_KEYSTORE·ROS_SECURITY_STRATEGY 환경 변수로 보안을 켜고, Enforce 전략이면 보안 자료가 없는 참여자를 거부하는 엄격 모드로, 아니면 허용 모드로 동작하며, 키 저장소의 enclaves 아래에 인클레이브별 인증서·키·governance·permissions 파일을 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-009"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "환경 변수 ROS_SECURITY_ENABLE(true 로 켬), ROS_SECURITY_KEYSTORE(키 저장소 루트), ROS_SECURITY_ENCLAVE_OVERRIDE, ROS_SECURITY_STRATEGY(Enforce 는 엄격, 그 외는 허용). 키 저장소 enclaves/ 하위 디렉터리에 인증서·키·거버넌스·권한 문서.",
      "as_of": "2020-07",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "Open-RMF 공식 책(Programming Multiple Robots with ROS 2)의 보안 장은 RMF 보안을 SROS 2 로 보호하는 ROS 2 부분과 TLS·OpenID Connect(Keycloak) 사용자 인증·역할 기반 접근 통제로 보호하는 웹 대시보드 부분의 두 층으로 설명하며, ROS 2 보안 이벤트 로깅은 구현되어 있지 않고 SROS 2 가 런치 파일을 지원하지 않는다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-405"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "두 층: ROS 2 요소(DDS Security 도구)와 웹 대시보드(TLS·사용자 인증). 대시보드는 Keycloak 기반 OIDC, 역할별 id 토큰을 API 서버에 전달. 키 저장소 private 디렉터리(CA 개인 키)는 배치 전 제거. 원문: ‘SROS 2 has no support for launch files yet’.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "VDA 5050 3.0.0 명세(공식 저장소 main)는 MQTT 통신 보안을 브로커 구성에서 고려해야 할 사항으로만 두고 이 지침 안에서 다루지 않아, 플릿 관리 시스템–무인운반차 통신의 인증·암호화 방식은 운영자와 통합 사업자가 정해야 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원문: ‘Protocol security needs to be taken into account by broker configuration, but is not addressed within this guideline.’ 문서 판 3.0.0. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f7",
      "claim": "IEC 공식 페이지에 따르면 IEC 62443 은 위험 기준으로 자산을 묶은 구역(zone)과 구역 사이 통신인 도관(conduit)을 두고 구역마다 목표 보안 수준을 정하며, IEC 62443-3-3 은 공격자 역량에 맞춘 보안 수준 SL1~SL4 와 일곱 기본 요구(식별·인증 통제, 사용 통제, 시스템 무결성, 데이터 기밀성, 데이터 흐름 제한, 사건 적시 대응, 자원 가용성)를 정의하고 보안 수준을 기본 요구별 7원소 벡터로 표현할 수 있게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1105"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원문: ‘A zone is a grouping of assets based on risk, while communications between zones is through so called conduits’. FR1~FR7 목록과 SL 벡터 표현. 표준 본문은 열지 않았고 IEC 소개 페이지 기준. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "병원 사례로, 미국 CISA 권고 ICSA-22-102-05(2022-04-12)는 병원 자율이동로봇을 제어·통신하는 Aethon TUG Home Base Server 버전 24 이전 전체에서 인가 누락(CWE-862, CVE-2022-1066·CVE-2022-26423, CVSS 8.2), 비종단점이 접근 가능한 채널(CWE-300, CVE-2022-1070, CVSS 9.8: 인증 없이 웹소켓에 접속해 TUG 로봇을 제어), 교차 사이트 스크립팅 2건을 공개했고, 악용되면 서비스 거부·로봇 기능 전면 제어·민감 정보 노출이 가능하다고 밝혔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1109"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "영향 분야 Healthcare and Public Health. 보고자 Cynerio 의 Asher Brass·Daniel Brodie. 취약점 5건(CVE-2022-1066, 26423, 1070, 27494, 1059).",
      "as_of": "2022-04-12",
      "site_type": "병원",
      "flow_item": "예외·성과"
    },
    {
      "id": "f9",
      "claim": "같은 CISA 권고는 완화책으로 버전 24 로의 갱신과 제조사의 배치 현장 방화벽 활성화 확인을 들고, 제어 시스템 기기의 네트워크 노출을 최소화해 인터넷에서 접근할 수 없게 하고 방화벽 뒤에 두며 원격 접속이 필요하면 VPN 을 쓰라고 권고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1109"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "완화: Version 24 갱신, 현장 방화벽 활성화 확인, 제어 시스템 망 격리·인터넷 비노출·원격 접속 시 VPN.",
      "as_of": "2022-04-12",
      "site_type": "병원",
      "flow_item": "제약"
    },
    {
      "id": "f10",
      "claim": "제조 공장 사례로, Quarta 외(IEEE Symposium on Security and Privacy 2017)는 널리 쓰이는 산업용 로봇 제어기를 실험적으로 분석해 공격자가 로봇 제어 컴퓨터를 원격에서 완전히 장악할 수 있는 여러 취약점(펌웨어 백도어, 인증 우회 등)을 찾았다.",
      "tag": "사실",
      "source_ids": [
        "ref-1119"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 결과 요약 기준: 주요 제조사의 현대적 산업용 로봇을 사례로 원격 완전 장악이 가능한 취약점 발견, 구현 결함(펌웨어 백도어·인증 우회)이 이론적 취약점보다 심각. 원문 PDF 403 으로 미열람.",
      "as_of": "2017",
      "site_type": "제조 공장",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f11",
      "claim": "Mayoral-Vilches(Alias Robotics, arXiv 2509.14096, 2025-09)는 Unitree G1 휴머노이드의 독자 이중 암호화(FMX)가 정적 암호 키를 써 구성 파일을 오프라인에서 복호화할 수 있고, 로봇이 음성·영상·공간·구동기 상태 데이터를 사용자의 명시적 동의 없이 외부 서버로 보낸다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1110"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 정적 암호 키로 오프라인 구성 복호화 가능, 상세 로봇 상태(음성·영상·공간·구동기) 외부 전송, 제조사 클라우드 인프라를 겨냥한 사이버보안 AI 에이전트 운용 시연.",
      "as_of": "2025-09-17",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "가정 사례로, 한국인터넷진흥원(KISA)과 한국소비자원은 2025년 3~7월 국내 판매 로봇청소기 6종을 모바일앱 보안·정책 관리·기기 보안 40개 항목으로 점검해 일부 제품(나르왈·드리미·에코백스)에서 사진·카메라 원격 접근, 미흡한 사용자 인증, 개인정보 조회, 통신 암호화 부족을 확인했다.",
      "tag": "사실",
      "source_ids": [
        "ref-969"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "바이라인네트워크(2025-10-31) 보도. 점검 주체 KISA·한국소비자원, 6종·40개 항목. 대응방안으로 펌웨어 갱신, 보안 인증, 설계 단계 보안 내재화, 5년 이상 보안 패치 보장 제시. KISA 공지 원문은 인증서 오류로 미열람.",
      "as_of": "2025-10-31",
      "site_type": "가정",
      "flow_item": "작업 대상"
    },
    {
      "id": "f13",
      "claim": "과학기술정보통신부와 KISA 는 2026년 3월 로봇 분야 보안모델 고도화판과 제품 개발·수출 때 참고할 사이버보안 요구사항 해설서를 KISA 지식플랫폼 자료실로 무료 배포했으며, 네트워크 연결·원격 업데이트·데이터 수집에 따른 해킹 위험과 유럽·북미의 로봇 보안 규제 강화를 배경으로 들었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1114"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "기사(2026-03-06): 제조·의료·서비스 분야 AI 로봇 확대로 네트워크 연결·원격 업데이트·데이터 수집 위험 증가, 개발 초기 보안 내재화로 규제 대응 비용 절감 목표. 해설서 원문(KISA)은 인증서 오류로 미열람.",
      "as_of": "2026-03-06",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f14",
      "claim": "Robey 외(펜실베이니아대, arXiv 2410.13691, 2024-10)의 RoboPAIR 는 LLM 으로 제어되는 로봇을 탈옥해 해로운 물리 행동을 끌어내는 공격으로, 화이트박스(NVIDIA Dolphins 자율주행 LLM)·그레이박스(GPT-4o 계획기를 단 Clearpath Jackal)·블랙박스(GPT-3.5 를 통합한 Unitree Go2) 세 설정에서 자주 100% 공격 성공률을 보였다.",
      "tag": "사실",
      "source_ids": [
        "ref-857"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: ‘often achieving 100% attack success rates’. 공격 LLM 이 프롬프트를 반복 개선하고 구문 검사 LLM 이 로봇 API 호환성을 확인. v1 2024-10-17, v2 2024-11-09.",
      "as_of": "2024-10",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f15",
      "claim": "Zhang 외(서호주대, arXiv 2408.03515, 2024-08)는 GPT-4o 로 텍스트·영상 다중 모달 프롬프트를 처리하는 이동 로봇 주행 시스템에 프롬프트 주입을 가해 잘못되거나 위험한 주행 명령이 나올 수 있음을 보였고, 보안 프롬프트와 응답 기반 탐지를 적용해 공격 탐지와 시스템 성능이 전체적으로 약 30.8% 개선됐다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1116"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록 기준. 시뮬레이션에 LLM 제어 이동 로봇을 배치해 강건성을 시험. 개선 수치 약 30.8%(공격 탐지와 시스템 성능). 실험 세부 조건 미확인.",
      "as_of": "2024-08",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "Nagaraja·Bagari·Bahsi(arXiv 2608.00747, 2026-08)는 LLM 기반 다중 에이전트 로봇 시스템에서 작업 지시를 겨냥한 직접 주입과 인식 모듈을 거친 간접 주입이 로봇 행동을 오염시키고 작업 성공률을 낮추며, 공유 프롬프트 구조를 통해 한 에이전트에서 다른 에이전트로 전파될 수 있음을 보였다.",
      "tag": "사실",
      "source_ids": [
        "ref-1115"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: ‘attacks can propagate from one agent to others through shared prompt structures’. 효과는 프롬프트 설계와 표적 에이전트에 따라 다름. 초록에 정량 수치·실물 여부 없음.",
      "as_of": "2026-08",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f17",
      "claim": "Ravichandran 외(arXiv 2503.07885, 2025-03 제출·2026-03 개정)의 RoboGuard 는 보호된 신뢰 기반(root-of-trust) LLM 이 미리 정한 안전 규칙을 로봇 환경에 맞춰 구체화하고 시간 논리 제어 합성으로 위험할 수 있는 계획을 안전 명세에 맞추는 2단계 가드레일로, 최악의 탈옥 공격을 가정한 시뮬레이션·실물 실험에서 안전하지 않은 계획의 실행을 92% 이상에서 3% 미만으로 줄이면서 안전한 계획의 성능은 떨어뜨리지 않았다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-700"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: unsafe plan 실행 over 92% → below 3%, 안전 계획 성능 유지. 1단계 연쇄 사고 추론을 하는 신뢰 기반 LLM, 2단계 시간 논리 제어 합성. 게재처는 초록 페이지에서 미확인.",
      "as_of": "2025-03",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f18",
      "claim": "OWASP GenAI 보안 프로젝트의 LLM01:2025 프롬프트 주입 항목은 사용자 입력이 직접 모델 행동을 바꾸는 직접 주입과 웹 페이지·파일 같은 외부 내용에 숨은 지시가 행동을 바꾸는 간접 주입을 구분하고, 완화책으로 출력 형식 정의·검증, 입출력 필터링, 최소 권한, 고위험 행동의 사람 승인, 외부 내용의 분리·표시, 적대적 시험을 들며, 확실한 차단법은 아직 불분명하다고 밝힌다.",
      "tag": "사실",
      "source_ids": [
        "ref-1108"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "완화책 7가지: 시스템 프롬프트로 행동 제한, 출력 형식 정의·검증, 입출력 필터링, 권한 통제·최소 권한, 고위험 행동 사람 승인, 외부 내용 분리·식별, 적대적 시험. 확률적 특성상 완전한 예방법은 불분명. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f19",
      "claim": "EU 기계류 규정 (EU) 2023/1230 은 2027-01-20 부터 전면 적용되며, 규정 준수에 결정적인 하드웨어·소프트웨어를 우발적·의도적 변조로부터 보호하고 기계가 자신의 안전 관련 소프트웨어를 식별하며 정당한·부당한 개입의 증거를 기록하게 하고, 출시 후 올린 안전 소프트웨어 판의 추적 로그를 5년간 남기도록 요구한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1111"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "IES 해설(2026-08-27 갱신) 기준: 변조 방지(protection against corruption), 개입 증거 기록, 안전 소프트웨어 판 추적 로그 5년 보관, 2027-01-20 전면 적용. EUR-Lex 원문은 본문이 비어 열람 실패.",
      "as_of": "2026-08-27",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f20",
      "claim": "Fernández-Becerra 외(arXiv 2403.09567, 2024-03 제출·2025-07 개정)는 ROS 기반 이동 로봇의 행동 기록을 블록체인으로 변조 방지하는 블랙박스형 책임 추적 요소와 그 기록으로 LLM 이 설명을 만드는 구조를 제안하고 세 가지 주행 시나리오에서 책임성·설명 지표를 평가했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1112"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: ‘black box-like element to provide accountability, featuring anti-tampering properties achieved through blockchain technology’. 초록에 성능·지연 수치 없음.",
      "as_of": "2024-03",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "확인한 자료를 종합하면 핵심 질문(통신·문서·대화를 통한 공격이 로봇 동작으로 이어지지 않게 하려면)에 대해, 통신 인증·암호화 수단(SROS 2, TLS·OIDC)은 있으나 상호운용 규격은 보안을 운영자에게 맡기고(f3~f6), 실제 사례에서는 인가 없는 플릿 서버·제어기가 로봇 전면 제어로 이어졌으며(f8·f10), LLM 층은 높은 확률로 탈옥되고(f14·f16) LLM 밖에서 계획을 규칙으로 검사하는 방어가 위험 계획 실행을 크게 줄이지만 완전 차단은 불분명해(f17·f18), 통신 인증·권한 분리·실행 전 규칙 검사·사람 승인·변조 방지 감사 기록을 겹쳐 두는 다층 방어가 필요한 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-009",
        "ref-405",
        "ref-031",
        "ref-1109",
        "ref-1119",
        "ref-857",
        "ref-1115",
        "ref-700",
        "ref-1108"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f3~f6·f8·f10·f14·f16~f18 종합 추정.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "확인한 자료를 종합하면 이 영역이 중요한 까닭은, ROP 가 잇는 여러 제조사 플릿 관리 서버·브로커의 보안이 규격에서 비어 있고(f5·f6), 플릿 서버 하나가 뚫리면 그 플릿의 로봇 전체가 제어권을 잃으며(f8), 채팅·문서 입력이 새 공격 경로를 더하고(f14·f16), EU 규정과 국내 보안 해설서가 개입 기록·보안 요구를 제품 요건으로 만들고 있기 때문이다(f13·f19).",
      "tag": "추정",
      "source_ids": [
        "ref-405",
        "ref-031",
        "ref-1109",
        "ref-857",
        "ref-1115",
        "ref-1114",
        "ref-1111"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f5·f6·f8·f13·f14·f16·f19 종합 추정.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "확인한 자료를 종합하면 52. 통신 보호·위협 관리·감사에서 ROP 가 직접 맡을 범위는 자신이 여는 브로커·API·ROS 2 노드의 통신 인증·암호화와 인클레이브·권한 설정(f4~f6), 여러 제조사 시스템을 포함한 전체 연결 구조의 위협 모델(f1·f7), 채팅·문서 입력과 외부 내용의 분리 및 LLM 계획의 실행 전 규칙 검사·사람 승인(f17·f18), 지시·승인·구성 변경을 변조 탐지 가능하게 남기는 감사 기록(f2·f19·f20)이다.",
      "tag": "추정",
      "source_ids": [
        "ref-009",
        "ref-405",
        "ref-031",
        "ref-010",
        "ref-1105",
        "ref-700",
        "ref-1108",
        "ref-1111",
        "ref-1112"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "분류 원문 19장 경계와 f1·f2·f4~f7·f17~f20 종합 추정.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "연계 대상: 분류 원문 19장 기준으로 로봇 제어기·펌웨어의 암호화·서명과 제조사 클라우드 원격 측정(f10·f11)은 로봇 제조사에, 현장 망의 방화벽·VPN·구역 설계(f7·f9)는 시설 IT/OT 보안 쪽에 속하므로, 이종 제조사를 잇는 ROP 는 이들에 보안 요구를 제시하고 연결 시점에 준수 여부를 확인하는 역할을 맡을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1119",
        "ref-1110",
        "ref-1105",
        "ref-1109"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f7·f9~f11 과 분류 원문 19장 경계 종합 추정.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f25",
      "claim": "이 영역은 권한·인증의 51. 인증·권한·격리(f5·f8), 영상·원격 측정 데이터의 53. 개인정보·영상 데이터(f11·f12), 대화 입력 방어의 13. 대화형 기능의 신뢰·기반·12. 채팅으로 업무 지시·오케스트레이션(f14~f18), LLM 계획의 44. 로봇 기반 모델·언어 모델 계획(f14·f17), 플릿 연결의 20. 로봇·제조사 관제 연동·21. 상호운용 표준·적합성(f6·f8), 시설 망의 22. 설비·건물 시스템 연동(f7), 통신 구조의 42. 분산 시스템·통신·컴퓨팅 구조(f3·f4), 기록의 37. 관제 화면·실행 기록(f2·f20), 사건 대응의 38. 모니터링·이상 탐지·원인 분석(f7), 물리 위험의 48. 안전·위험 관리(f14·f17), 사고 조사의 50. 안전 표준·인증·사고 조사(f19·f20), 방어 시험의 54. 시험·형식 검증·벤치마크(f15·f17), 패치의 57. 자산·소프트웨어 수명주기 관리(f9·f19), 규제의 59. 법·규제·보험·라이선스(f13·f19), 적용 현장인 62. 제조 공장(f10)·63. 병원·의료(f8·f9)·65. 가정·공동주택(f12)과 이어진다.",
      "tag": "추정",
      "source_ids": [
        "ref-405",
        "ref-1109",
        "ref-1110",
        "ref-969",
        "ref-857",
        "ref-1116",
        "ref-1115",
        "ref-700",
        "ref-1108",
        "ref-031",
        "ref-1105",
        "ref-009",
        "ref-010",
        "ref-1112",
        "ref-1111",
        "ref-1114",
        "ref-1119"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f2~f20 을 영역별로 대응시킨 추정.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-009",
      "org": "Open Robotics (ROS 2 Design, Kyle Fazzari)",
      "title": "ROS 2 DDS-Security integration",
      "published": null,
      "url": "https://design.ros2.org/articles/ros2_dds_security.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "DDS-Security 의 다섯 플러그인 인터페이스와 ROS 2(SROS 2)가 쓰는 인증·접근 통제·암호 세 가지, 보안 환경 변수와 키 저장소 구조를 설명하는 ROS 2 설계 문서.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/ros2/design/gh-pages/articles/180_ros2_dds_security.md",
      "source_unopened": false
    },
    {
      "id": "ref-010",
      "org": "Open Robotics (ROS 2 Design, Moulard·Hortala·Perez 외)",
      "title": "ROS 2 Robotic Systems Threat Model",
      "published": null,
      "url": "https://design.ros2.org/articles/ros2_threat_model.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "STRIDE·DREAD 로 ROS 2 로봇 시스템의 통신·소프트웨어·하드웨어·로그 위협과 완화책을 정리하고 TurtleBot 3·MARA 에 적용한 위협 모델 문서.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/ros2/design/gh-pages/articles/183_ros2_threat_model.md",
      "source_unopened": false
    },
    {
      "id": "ref-1105",
      "org": "IEC (SyC Smart Energy)",
      "title": "IEC 62443",
      "published": null,
      "url": "https://syc-se.iec.ch/deliveries/cybersecurity-guidelines/security-standards-and-best-practices/iec-62443/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "IEC 공식 사이트의 IEC 62443 소개. 구역·도관, 보안 수준 SL1~SL4, 일곱 기본 요구(FR1~FR7)를 설명한다. 표준 본문은 아니다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-857",
      "org": "Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J. (arXiv)",
      "title": "Jailbreaking LLM-Controlled Robots",
      "published": "2024-10",
      "url": "https://arxiv.org/abs/2410.13691",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "LLM 제어 로봇을 탈옥하는 RoboPAIR 공격을 세 로봇 설정에서 시연하고 자주 100% 성공률을 보고한 프리프린트.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-700",
      "org": "Ravichandran, Z., Robey, A. 외 (arXiv)",
      "title": "Safety Guardrails for LLM-Enabled Robots",
      "published": "2025-03",
      "url": "https://arxiv.org/abs/2503.07885",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "신뢰 기반 LLM 과 시간 논리 제어 합성으로 이뤄진 RoboGuard 가드레일이 탈옥 공격 아래 위험 계획 실행을 92% 이상에서 3% 미만으로 줄였다고 보고한 프리프린트.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1108",
      "org": "OWASP GenAI Security Project",
      "title": "LLM01:2025 Prompt Injection",
      "published": null,
      "url": "https://genai.owasp.org/llmrisk/llm01-prompt-injection/",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "직접·간접 프롬프트 주입의 정의와 최소 권한·사람 승인·외부 내용 분리 등 일곱 가지 완화책을 정리한 OWASP LLM 상위 10 위험 항목.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1109",
      "org": "CISA (미국 사이버보안·기반시설보안청)",
      "title": "Aethon TUG Home Base Server (ICSA-22-102-05)",
      "published": "2022-04-12",
      "url": "https://www.cisa.gov/news-events/ics-advisories/icsa-22-102-05",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "병원 자율이동로봇 TUG 의 플릿 서버 취약점 5건(인가 누락, 웹소켓 무인증 제어, XSS)과 완화책을 공개한 ICS 권고.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1110",
      "org": "Mayoral-Vilches, V. (Alias Robotics, arXiv)",
      "title": "The Cybersecurity of a Humanoid Robot",
      "published": "2025-09-17",
      "url": "https://arxiv.org/abs/2509.14096",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "Unitree G1 휴머노이드의 정적 키 암호화 결함과 동의 없는 원격 측정 전송을 분석한 기술 보고서.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1111",
      "org": "IES (Integrated Equipment Services)",
      "title": "Machinery Regulation Guide",
      "published": "2026-08-27",
      "url": "https://www.ies.co.uk/reference-library/machinery-regulation-guide",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "EU 기계류 규정 (EU) 2023/1230 의 변조 방지·개입 증거 기록·안전 소프트웨어 판 추적 로그 5년 보관·2027-01-20 적용을 해설한 업계 안내서.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1112",
      "org": "Fernández-Becerra, L., González-Santamarta, M. Á., Guerrero-Higueras, Á. M., Rodríguez-Lera, F. J., & Matellán Olivera, V. (arXiv)",
      "title": "Enhancing Trust in Autonomous Agents: An Architecture for Accountability and Explainability through Blockchain and Large Language Models",
      "published": "2024-03",
      "url": "https://arxiv.org/abs/2403.09567",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "ROS 기반 이동 로봇의 행동 기록을 블록체인으로 변조 방지하는 블랙박스형 책임 추적과 LLM 설명 생성 구조를 제안한 프리프린트.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-969",
      "org": "바이라인네트워크 (곽중희)",
      "title": "‘로봇청소기’ 다수 제품 보안 취약…대응방안은?",
      "published": "2025-10-31",
      "url": "https://byline.network/2025/10/31-283/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "KISA·한국소비자원의 로봇청소기 6종 40개 항목 보안 점검 결과와 대응방안을 전한 기사. KISA 공지 제목과 내용이 일치한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1114",
      "org": "엠에스투데이",
      "title": "선박·위성·로봇까지 해킹 표적…정부, ‘피지컬 AI’ 산업 보안 기준 제시",
      "published": "2026-03-06",
      "url": "https://www.mstoday.co.kr/news/articleView.html?idxno=100755",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "과기정통부·KISA 가 로봇 보안모델 고도화판과 사이버보안 요구사항 해설서를 KISA 지식플랫폼으로 배포했다고 전한 기사.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1115",
      "org": "Nagaraja, N., Bagari, A., & Bahsi, H. (arXiv)",
      "title": "When Prompts Control Robots: Prompt Injection Attacks in Multi-Agent Robotic Systems",
      "published": "2026-08",
      "url": "https://arxiv.org/abs/2608.00747",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "LLM 기반 다중 에이전트 로봇 시스템에서 직접·간접 프롬프트 주입과 에이전트 간 전파를 체계적으로 분석한 프리프린트.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1116",
      "org": "Zhang, W., Kong, X., Dewitt, C., Braunl, T., & Hong, J. B. (arXiv)",
      "title": "A Study on Prompt Injection Attack Against LLM-Integrated Mobile Robotic Systems",
      "published": "2024-08",
      "url": "https://arxiv.org/abs/2408.03515",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "GPT-4o 통합 이동 로봇 주행 시뮬레이션에서 프롬프트 주입 영향과 보안 프롬프트·응답 기반 탐지 방어(약 30.8% 개선)를 보고한 프리프린트.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 공식 저장소)",
      "title": "VDA 5050 — Interface for the communication between automated guided vehicles (AGV) and a master control (VDA5050_EN.md, 3.0.0)",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "무인운반차–마스터 제어 통신 규격 3.0.0 원문. 프로토콜 보안은 브로커 구성에 맡기고 지침 안에서 다루지 않는다고 적는다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/VDA5050_EN.md",
      "source_unopened": false
    },
    {
      "id": "ref-405",
      "org": "Open Robotics (Programming Multiple Robots with ROS 2)",
      "title": "Security",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/security.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 의 ROS 2 부분(SROS 2 키 저장소·인클레이브)과 웹 대시보드(TLS·Keycloak OIDC·역할 기반 접근 통제) 보안을 설명하는 공식 책의 보안 장.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/security.md",
      "source_unopened": false
    },
    {
      "id": "ref-1119",
      "org": "Quarta, D., Pogliani, M., Polino, M., Maggi, F., Zanchettin, A. M., & Zanero, S. (IEEE S&P 2017)",
      "title": "An Experimental Security Analysis of an Industrial Robot Controller",
      "published": "2017",
      "url": "https://files01.core.ac.uk/download/pdf/84891817.pdf",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 산업용 로봇 제어기를 실험적으로 분석해 원격 완전 장악이 가능한 취약점을 보고한 IEEE 보안 학회 논문(검색 결과 요약 기준).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md",
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
      "rationale": "섹션 3: f22(왜 중요한가), f21(핵심 질문 답, 추정) / 섹션 4: STRIDE f1, DDS-Security·인클레이브 f3·f4, 구역·도관·보안 수준 f7, 직접·간접 프롬프트 주입 f18, 변조 탐지 기록 f19·f20 / 섹션 5: 병원 — f8(예외·성과: 플릿 서버 무인증 제어)·f9(제약: 망 격리·갱신), 가정 — f12(작업 대상: 집 내부 사진·개인정보), 제조 공장 — f10(예외·성과: 제어기 원격 장악, 원문 미열람). 물류창고·상업 시설·실외 사례는 찾지 못함을 명시 / 섹션 6: 통신 보호 f3~f6, 위협 모델·취약점 관리 f1·f7·f9, 대화 입력 방어 f14~f18, 감사 기록 f2·f19·f20 / 섹션 7: ROS 2 위협 모델 f1, DDS-Security·SROS 2 f3·f4, Open-RMF 보안 f5, VDA 5050 f6, IEC 62443 f7, OWASP LLM01 f18, EU 기계류 규정 f19, KISA 로봇 보안모델·해설서 f13 / 섹션 8: f8·f10·f11·f14~f17·f20 / 섹션 9: f23(직접 범위), f24(연계 대상) / 섹션 10: f25 / 섹션 11: 기존 oq-144(부분 근거 f15·f17)과 open_questions_new 5건."
    },
    {
      "action": "update",
      "path": "docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md",
      "sections": [
        "6",
        "8",
        "11"
      ],
      "rationale": "oq-144 가 걸린 13. 대화형 기능의 신뢰·기반에 f14·f16(탈옥·다중 에이전트 주입 전파)을 섹션 8 에, f15·f17(방어 효과 수치)·f18(OWASP 완화책)을 섹션 6 에, oq-144 부분 근거를 섹션 11 에 반영 제안. 이번 실행에서 반영이 어려우면 다음 실행 후보."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "STRIDE 위협 분류",
      "term_en": "STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege)",
      "definition": "위조·변조·부인·정보 노출·서비스 거부·권한 상승 여섯 범주로 시스템 위협을 빠짐없이 떠올리도록 돕는 위협 모델링 분류로, ROS 2 위협 모델이 로봇 시스템에 적용했다."
    },
    {
      "term_ko": "간접 프롬프트 주입",
      "term_en": "Indirect Prompt Injection",
      "definition": "사용자가 직접 입력하지 않은 웹 페이지·문서·인식 결과 같은 외부 내용에 숨은 지시가 언어 모델에 들어가 모델의 행동을 의도와 다르게 바꾸는 공격이다."
    },
    {
      "term_ko": "보안 수준",
      "term_en": "Security Level (SL, IEC 62443)",
      "definition": "IEC 62443 에서 구역·도관이 견뎌야 할 공격자 역량에 따라 SL1~SL4 로 매기는 보호 등급으로, 목표·역량·달성 수준을 구분하고 기본 요구별 벡터로 표현할 수 있다."
    },
    {
      "term_ko": "변조 탐지 로그",
      "term_en": "Tamper-evident Log",
      "definition": "기록마다 앞 기록의 해시를 잇거나 외부에 고정해 나중에 기록이 고쳐지거나 지워지면 드러나게 만든 로그로, 명령·승인 감사 기록의 무결성 확보에 쓴다."
    }
  ],
  "open_questions_new": [
    "여러 제조사 플릿 관리 서버와 VDA 5050 브로커·Open-RMF 어댑터를 잇는 ROP 에서 브로커·API 의 상호 인증과 TLS 설정의 최소 요구를 정한 공개 보안 프로파일이 있는가? | 관련 영역: 52. 통신 보호·위협 관리·감사, 20. 로봇·제조사 관제 연동, 21. 상호운용 표준·적합성 | 근거: f6 | 종류: 일반",
    "LLM 에이전트 여러 개가 로봇을 나눠 맡을 때 한 에이전트에 주입된 지시가 다른 에이전트로 퍼지지 않게 에이전트 간 메시지에 신뢰 경계를 두는 방어의 효과를 잰 연구가 있는가? | 관련 영역: 52. 통신 보호·위협 관리·감사, 13. 대화형 기능의 신뢰·기반, 12. 채팅으로 업무 지시·오케스트레이션 | 근거: f16 | 종류: 일반",
    "명령·승인 감사 기록을 해시 체인·블록체인으로 변조 탐지 가능하게 남길 때 수백 대 로봇 규모의 명령 빈도에서 지연·저장 비용을 측정한 자료가 있는가? | 관련 영역: 52. 통신 보호·위협 관리·감사, 37. 관제 화면·실행 기록 | 근거: f20 | 종류: 일반",
    "EU 기계류 규정의 개입 증거 기록·안전 소프트웨어 추적 로그 요구가 개별 기계 밖에서 여러 로봇을 지시하는 오케스트레이션 플랫폼에도 미치는가, 미친다면 기록 책임은 누구에게 있는가? | 관련 영역: 52. 통신 보호·위협 관리·감사, 59. 법·규제·보험·라이선스, 58. 다사업자 책임·계약·데이터 | 근거: f19 | 종류: 일반",
    "KISA 로봇 보안모델(고도화)과 사이버보안 요구사항 해설서는 로봇 통신 암호화·감사 기록·원격 업데이트에 어떤 요구 항목을 두며 다중 로봇 관제 플랫폼을 대상에 포함하는가? | 관련 영역: 52. 통신 보호·위협 관리·감사, 59. 법·규제·보험·라이선스 | 근거: f13 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 17,
    "cross_checked_count": 0,
    "unverified": [
      "f3 DDS-Security 로깅 미사용: ref-009 와 ref-405 이 같은 ROS 계열 문서라 독립 교차 확인으로 보지 않음",
      "f10 Quarta 외: 원문 PDF 403 으로 미열람, 검색 결과 요약 범위만 사용(공격 유형·노출 기기 수는 개인 블로그 요약에만 있어 넣지 않음)",
      "f12 KISA 로봇청소기 점검 공지 원문은 kisa.or.kr 인증서 오류로 미열람, 기사 기준",
      "f13 KISA 로봇 보안모델(고도화)·보안 요구사항 해설서 원문(쪽수·항목)은 인증서 오류로 미열람",
      "f19 EUR-Lex 규정 원문은 본문이 비어 열람 실패, 업계 해설 기준. 1년 보관 요구(안전 관련 결정 기록)는 조항 위치를 확인하지 못해 넣지 않음",
      "IEC 62443-3-3 의 감사 관련 요구(SR 2.8 감사 대상 사건, SR 2.12 부인 방지, SR 3.9 감사 정보 보호 등)는 원문·공식 자료를 열지 못해 넣지 않음",
      "f6 VDA 5050 3.0.0 발행일 미확인",
      "oq-144: 방어 효과 수치는 시뮬레이션·실험실 결과(f15·f17)뿐이고 현장 시험 결과는 찾지 못해 해결 제안하지 않음",
      "물류창고·상업 시설·실외 현장의 통신·감사 사례는 찾지 못함"
    ],
    "scope_violations": [
      "f10·f11: 로봇 제어기 펌웨어·암호화 결함은 로봇 자체 지능·제어(연계 대상)의 문제이므로 위협 사례 근거로만 쓰고 f24 에서 '연계 대상: '으로 구분함",
      "f9: 현장 망 방화벽·VPN 은 시설 IT/OT 쪽 조치이므로 f24 에서 연계 대상으로 구분함",
      "f14·f17: LLM 계획 방어는 13. 대화형 기능의 신뢰·기반·44. 로봇 기반 모델·언어 모델 계획과 겹치므로 이 영역에서는 공격이 로봇 동작으로 이어지는 경로 차단 관점으로만 제안함"
    ],
    "budget_used": {
      "queries": 16,
      "sources": 15
    },
    "limits": "web_fetch_available: true · fetch_mode full. 검색 16회/30, 신규 출처 15건/15(ref-1105~ref-1119)로 출처 상한에 도달해 IEC 62443 감사 요구 원문 대체 자료, MCP 도구 설명 오염 사례, 물류창고 사례를 더 넣지 못했다. 재사용 2건(ref-009 ROS 2 DDS-Security, ref-010 ROS 2 위협 모델): 입력 참고문헌 요약에 행이 없어 기관·제목·URL 은 공통 규칙의 대응표와 원문 머리말을 따랐고 발행일은 null 로 두었다(퍼블리셔가 기존 값으로 합칠 것). 주의: 입력의 이전 브리프 2026-09-30-09 가 ref-1105~ref-405 을 이미 다른 출처에 썼다. 실행 컨텍스트가 이 구간을 이번 실행 전용으로 예약했다고 해 그대로 따랐으나 id 충돌 가능성이 있어 퍼블리셔 확인이 필요하다. 원문 열람: 16건 열었고(webfetch 12, github_raw 4) Quarta 외(ref-1119)만 403 으로 못 열었다. 논문은 모두 초록 기준이다. 교차 확인 0건: 핵심 수치가 모두 단일 출처라 finding 신뢰도는 medium 이하다. 벤더 기능·성능 주장은 쓰지 않았다(CISA 권고·연구 보고 중심). 분류 원문 핵심 질문에는 f21 로 답했고 결론은 '통신 인증·암호화 수단은 있으나 규격이 보안을 운영자에게 맡기고, LLM 층은 쉽게 탈옥되며, LLM 밖 규칙 검사·사람 승인·권한 분리·변조 방지 감사 기록을 겹친 다층 방어가 필요하다'는 추정이다. 현장 유형 사례는 병원(f8·f9)·가정(f12)·제조 공장(f10, 원문 미열람)이며 물류창고·상업 시설·실외는 찾지 못했다. 국내 자료는 KISA·소비자원 점검(f12, 기사)과 KISA 로봇 보안모델 배포(f13, 기사) 2건이고 KISA 원문은 인증서 오류로 열지 못했다. oq-144 는 f15·f17 이 부분 근거(시뮬레이션·실험실 수치)이며 현장 시험이 없어 해결 제안하지 않았다. 교차 규칙에 따라 대화 입력 방어 finding 은 13. 대화형 기능의 신뢰·기반·44. 로봇 기반 모델·언어 모델 계획과 함께 연결하도록 제안했다. 용어집에 이미 있는 프롬프트 주입·탈옥·DDS 보안 규격·인클레이브·보안 구역과 도관·감사 추적·과도한 에이전시·혼란된 대리인은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음."
  }
}
```

### runs/2026-09-30-11/verification.json

```json
{
  "run_id": "2026-09-30-11",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문 텍스트(ref-010, github_raw)에서 STRIDE 분류·DREAD 평가, TurtleBot 3·MARA 적용, 통신 위협(구성요소 신원 위조, 메시지 가로채기·변조, 채널 무단 쓰기, 도청)을 확인했다. 작성 2019-03, 최종 수정 2021-01. 원문 머리에 'DRAFT DOCUMENT' 표시와 '완화책을 모두 적용해도 제품이 안전함을 보장하지 않는다'는 면책 문구가 있다(주의 사항). 단일 출처."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ref-010 원문에서 '노드가 잘못된 데이터를 채널에 씀' 위협의 완화책에 잘못된 메시지 이벤트 기록·사용자 통지가, 구성 관리 위협의 완화책에 구성 변경 기록이 있다. 로그 유출·무단 접근도 위협 범주에 있다. 단일 출처."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ref-009 원문(작성 2019-07, 수정 2020-07)에 다섯 SPI, ROS 2 는 앞의 셋만 사용, 로깅·데이터 태깅은 규격 준수에 필수가 아니어서 모든 DDS 구현이 지원하지는 않음, AES-GCM 이 명시돼 있다. ref-405 도 같은 내용이지만 같은 ROS 계열 문서라 독립 교차 확인으로 보지 않는다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(문구 수정 필요): 환경 변수 3종과 enclaves 하위 파일 구성은 ref-009 원문과 일치한다. 다만 원문의 엄격 모드는 '보안 파일을 찾지 못하면 그 참여자를 실행하지 않는 것'이고, 허용 모드(기본값)는 '보안 없이 실행하는 것'이다. 브리프의 '보안 자료가 없는 참여자를 거부'는 다른 참여자를 거부한다는 뜻으로 읽힐 수 있어 수정을 지시한다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ref-405 원문(github_raw)을 열어 두 부분(ROS 2 요소와 대시보드), TLS·사용자 확인·Keycloak OIDC 역할 기반 접근, 배치 전 private 디렉터리 제거, 'SROS 2 has no support for launch files yet', ROS 2 가 SPI 셋만 사용(로깅 미사용)을 확인했다. 발행일 미확인."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(서지·용어 수정 필요): VDA5050_EN.md main(3.0.0)에 'Protocol security needs to be taken into account by broker configuration, but is not addressed within this guideline.' 문장이 있다. 그러나 3.0.0 문서 제목은 'Interface for the Communication between Mobile Robots and a Fleet Control'이며 AGV·master control 표현을 쓰지 않는다. 같은 문서가 인증서 다운로드는 TLS 로 보호하라고 적으므로 '보안을 전혀 다루지 않는다'는 식의 단정은 피해야 한다. '운영자와 통합 사업자가 정해야 한다'는 원문 문장이 아니라 해석이다. 발행일 미확인. 같은 URL 이 실행 2026-09-30-10 의 ref-1079 로도 쓰였다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: IEC(SyC Smart Energy) 공식 페이지에 구역·도관 정의 문장, IEC 62443-3-3 의 보안 수준 4단계와 공격자 역량 대응, FR1~FR7 목록, 7원소 보안 수준 벡터(예: SL=(3,3,3,1,2,1,3)), SL-T 언급이 있다. 발행 기관 자료이나 표준 본문은 아니다. 이 페이지는 목표·역량·달성 수준 구분을 설명하지 않는다(용어 후보 정의 수정 지시)."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: CISA ICSA-22-102-05(2022-04-12). 버전 24 이전 전체, CVE-2022-1066·26423(CWE-862, 8.2), CVE-2022-1070(CWE-300, 9.8, 인증 없이 웹소켓에 접속해 TUG 로봇 제어), XSS 2건(7.6). 영향은 서비스 거부·로봇 기능 전면 제어·민감 정보 노출, 분야 Healthcare and Public Health, 보고자 Cynerio. 단일 출처(정부 권고)."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 같은 권고의 완화책(버전 24 갱신·방화벽 활성 확인, 망 노출 최소화·인터넷 비노출·방화벽 뒤 격리·VPN). 방화벽·VPN 은 시설 IT/OT 쪽 조치이므로 연계 대상으로 서술해야 한다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정: 출처 실재는 검색 결과로 확인했다(IEEE S&P 2017, 268–286쪽, Quarta 외 6인). core.ac.uk PDF 는 검증에서도 403 이었다(원문 미열람). 검색 결과 요약은 '소프트웨어 취약점과 구조적 결함을 이용해 정밀도·제어 논리 정확성·작업자 안전 요구를 무너뜨릴 수 있다'까지만 보여 주며, '원격 완전 장악'과 '펌웨어 백도어·인증 우회'는 확인하지 못했다. 스니펫 범위로 줄이도록 지시한다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2509.14096(2025-09-17, Mayoral-Vilches) 초록에 Unitree G1, FMX 이중 암호화의 정적 키로 인한 오프라인 구성 복호화, 음성·영상·공간·구동기 상태의 동의 없는 외부 전송이 있다. 저자는 보안 업체(Alias Robotics) 소속이며 단일 출처 기술 보고서다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": true,
      "tag_decision": "강등",
      "note": "사실 → 추정: 기사(ref-969)를 다시 열어 점검 주체 KISA·한국소비자원, 2025년 3~7월, 6종, 모바일앱·정책관리·기기보안 40개 항목, 나르왈·드리미·에코백스 제품의 사진 열람·카메라 강제 활성화, 미흡한 사용자 인증, 사용자 ID 로 이름·전화번호 조회를 확인했다. 그러나 '통신 암호화 부족'은 기사에 취약점으로 나오지 않는다(암호화는 기업 대응·전문가 권고로만 언급). KISA 보도자료(kisa.or.kr)와 여러 언론의 검색 결과로 점검 개요는 교차 확인했다(검색 결과 일치, KISA 원문 미열람). 다만 수정 전 주장 전체가 출처와 일치하지 않아 강등한다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 엠에스투데이(2026-03-06) 기사에 과기정통부·KISA 의 로봇 분야 보안모델 고도화판·요구사항 해설서 배포, KISA 지식플랫폼 자료실 무료 배포, 네트워크 연결·원격 업데이트·데이터 수집 위험, 유럽·북미 규제 강화 언급이 있다. 같은 발표에서 스마트선박·우주 분야 보안모델도 함께 배포됐다. 기사 단일 출처, KISA 원문 미열람."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2410.13691(v1 2024-10-17, v2 2024-11-09) 초록에 세 설정(NVIDIA Dolphins 화이트박스, GPT-4o 계획기를 단 Clearpath Jackal 그레이박스, GPT-3.5 를 통합한 Unitree Go2 블랙박스)과 'often achieving 100% attack success rates'가 있다. 연구 환경 결과이며 단일 출처."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2408.03515 초록(GPT-4o, 다중 모달 프롬프트, 약 30.8% 개선)과 HTML 본문(EyeSim VR 시뮬레이터, secure prompting·response-based detection, LiDAR·카메라·사람 지시 입력)을 확인했다. 결과는 시뮬레이션 기준이다. 단일 출처."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2608.00747 초록에 작업 지시 직접 주입·인식 모듈 경유 간접 주입, 적대 행동 유발·작업 완료 감소, 공유 프롬프트 구조를 통한 에이전트 간 전파가 있다. 초록에 정량 수치는 없다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2503.07885(2025-03-10 제출, 2026-03-03 개정, Ravichandran·Robey·Kumar·Pappas·Hassani) 초록에 신뢰 기반 LLM + 시간 논리 제어 합성의 2단계, 위험 계획 실행 92% 초과 → 3% 미만, 안전 계획 성능 유지, 시뮬레이션·실물 실험이 있다. 게재처 미확인. 단일 출처."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: OWASP GenAI LLM01:2025 페이지에서 직접·간접 주입 정의, 완화책 7가지, '확실한 예방법이 있는지 불분명' 문구를 확인했다. 판 표기는 2025, 발행일 미확인."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인: IES 해설(2026-08-27 갱신)에서 2027-01-20 전면 적용, 규정 준수에 결정적인 하드웨어·소프트웨어의 변조 보호, 안전 소프트웨어 식별과 개입 증거 기록, 출시 뒤 올린 안전 소프트웨어 판 추적 로그 5년 보관을 확인했다. 독립 해설(Nemko·Rockwell Automation 등)의 검색 결과 요약과 일치해 교차 확인했다(두 번째 출처는 검색 결과 기준). EUR-Lex 원문은 검증에서도 본문이 비어 열람하지 못했다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 2403.09567 초록에 ROS 기반 이동 로봇용 블록체인 변조 방지 블랙박스형 요소, 그 기록 위 LLM 자연어 설명, 세 시나리오 주행 평가와 책임성·설명 지표가 있다. 성능·지연 수치는 없다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지(종합). 문구 수정 필요: 강등된 f10 에 기대어 '제어기가 로봇 전면 제어로 이어졌다'고 쓰지 않는다. '높은 확률로 탈옥'은 f14 의 연구 환경 결과에만 근거하며 f16 에는 성공률 수치가 없다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지(종합). 문구 수정 필요: f8 은 '로봇 기능 전면 제어가 가능하다'까지이며 '그 플릿의 로봇 전체가 제어권을 잃는다'는 과장이다. f13 의 KISA 해설서는 참고 자료이지 제품 요건이 아니므로 '제품 요건으로 만든다'는 f19(EU 규정)에만 쓴다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. 분류 원문 19장 경계와 맞다. 근거 finding(f1·f2·f4~f7·f17~f20)이 모두 확인됐다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. '연계 대상:'으로 로봇 제어기·펌웨어(f10·f11)와 현장 망 방화벽·VPN(f9)을 구분해 범위 경계에 맞다. f10 은 강등된 범위로만 인용한다."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. 연결 영역의 번호·이름이 부록 A 원문 명칭과 모두 일치한다. L. AI·학습 기술 교차 규칙대로 44. 로봇 기반 모델·언어 모델 계획과 연결했고, C. 채팅 기반 구성·운영의 13. 대화형 기능의 신뢰·기반, 12. 채팅으로 업무 지시·오케스트레이션과도 연결했다."
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
      "ref-031(VDA 5050 3.0.0, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md)은 실행 2026-09-30-10 브리프의 ref-1079 와 URL 이 같다. 퍼블리셔가 같은 URL 을 기존 id 로 합칠 때 두 제목이 서로 다르다(둘 다 3.0.0 원문 제목 'Interface for the Communication between Mobile Robots and a Fleet Control'과도 다름).",
      "참고문헌 id 충돌 가능성: 이번 브리프의 ref-1105~ref-405 은 실행 2026-09-30-09 브리프가 다른 출처(DeepFleet, POGEMA, CJ대한통운 등)에 이미 쓴 id 다(예: ref-1105 IEC 62443 대 DeepFleet, ref-1109 CISA 대 POGEMA, ref-031 VDA 5050 대 CJ대한통운). 퍼블리셔 확인이 필요하다.",
      "f5(Open-RMF 대시보드의 OIDC·역할 기반 접근 통제)는 51. 인증·권한·격리의 명령 권한·사용자 인증 내용과 겹칠 수 있다. 51. 인증·권한·격리 페이지 본문은 요약만 입력돼 각주 재사용 여부를 확인하지 못했다.",
      "두 번째 페이지 제안(13. 대화형 기능의 신뢰·기반)의 기존 본문이 입력에 없어 f14~f18 과의 중복·모순 검사를 하지 못했다."
    ]
  },
  "terminology": {
    "ok": false,
    "conflicts": [
      "용어 후보 'STRIDE 위협 분류' 정의의 '빠짐없이 떠올리도록'은 측정 근거 없는 완전 표현이다(공통 규칙 12).",
      "용어 후보 '보안 수준' 정의의 '목표·역량·달성 수준을 구분'은 근거 출처(ref-1105)에 없다. 그 페이지는 SL-T(목표)만 언급한다.",
      "용어 후보 '변조 탐지 로그' 정의의 '앞 기록의 해시를 잇거나 외부에 고정'은 어느 finding 에도 근거가 없다(f20 은 블록체인 기반 변조 방지만 말한다). 기존 용어 '감사 추적 (Audit Trail)'과의 관계도 밝혀야 한다.",
      "용어 후보 '간접 프롬프트 주입'은 기존 용어 '프롬프트 주입 (Prompt Injection)'의 하위 개념이다. 따로 등록한다면 기존 항목과 표기·정의를 맞추고 서로 연결해야 한다."
    ]
  },
  "quotation_check": {
    "ok": true
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "f10: [사실] → [추정]으로 강등한다. 본문에는 검색 결과 요약으로 확인된 범위(산업용 로봇 제어기의 소프트웨어 취약점과 구조적 결함으로 제어 정확성과 작업자 안전 요구를 무너뜨릴 수 있음을 보였다)만 쓰고, '원격 완전 장악'과 '펌웨어 백도어·인증 우회'는 뺀다 — 원문(ref-1119)을 검증에서도 열지 못했고 검색 결과에 해당 구절이 없다.",
    "ref-1119: 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고, reference_updates 의 해당 항목에 source_unopened: true 를 넣는다 — 원문 PDF 가 403 이어서 열지 못했다.",
    "f12: '통신 암호화 부족'을 빼고 [사실] → [추정]으로 강등한다. 남길 내용은 점검 주체·기간·6종·40개 항목과, 나르왈·드리미·에코백스 제품의 사진 열람·카메라 강제 활성화, 미흡한 사용자 인증, 개인정보 조회뿐이다 — 기사(ref-969)는 통신 암호화 부족을 취약점으로 싣지 않는다.",
    "f6·ref-031: 참고문헌 제목을 'VDA 5050 — Interface for the Communication between Mobile Robots and a Fleet Control (VDA5050_EN.md, 3.0.0)'으로 고친다. 본문의 '플릿 관리 시스템–무인운반차'는 '플릿 관제–이동 로봇'으로 바꾼다. 원문 문장 그대로 '프로토콜 보안은 브로커 구성에서 고려해야 하지만 이 지침은 다루지 않는다'로 쓰고, '운영자와 통합 사업자가 정해야 한다'는 [추정]으로 떼어 쓰거나 뺀다 — 3.0.0 원문 제목·용어와 다르고, 뒷부분은 원문에 없는 해석이다.",
    "f4: 엄격 모드를 '보안 파일을 찾지 못하면 그 참여자를 실행하지 않는 모드'로, 허용 모드를 '보안 파일이 없으면 보안 기능 없이 실행하는 기본 모드'로 고쳐 쓴다 — ref-009 원문의 정의와 맞추기 위해서다.",
    "f21: 강등된 f10 을 근거로 '제어기가 로봇 전면 제어로 이어졌다'고 쓰지 않고, 전면 제어 사례는 f8 에만 근거한다. '높은 확률로 탈옥'은 '연구 환경에서 높은 공격 성공률이 보고됐다(f14)'로 바꾼다 — f16 에는 성공률 수치가 없다.",
    "f22: '플릿 서버 하나가 뚫리면 그 플릿의 로봇 전체가 제어권을 잃는다'를 '플릿 서버 취약점이 로봇 기능 전면 제어로 이어질 수 있다(f8)'로 줄인다. KISA 해설서(f13)는 '제품 요건'이 아니라 참고 자료로 쓴다 — CISA 권고와 기사가 뒷받침하는 범위를 넘는다.",
    "3·5·6·9절: f9(방화벽·VPN·망 격리)와 f10·f11(제어기·펌웨어·제조사 원격 측정)을 ROP 가 직접 하는 대책처럼 쓰지 않는다. 사례·위협 근거로만 쓰고 9절에서 f24 에 따라 '연계 대상'으로 짧게 다룬다 — 분류 원문 19장의 로봇 자체 지능·제어, 시설·설비 제어 경계다.",
    "f19: 근거가 업계 해설(IES, 2026-08-27 갱신)임을 본문이나 각주에 밝히고, 확인하지 못한 규정 조항 번호는 쓰지 않는다 — EUR-Lex 원문을 열지 못했다.",
    "용어 후보 'STRIDE 위협 분류': 정의에서 '빠짐없이 떠올리도록 돕는'을 빼고 '여섯 범주로 위협을 분류하는'처럼 쓴다 — 측정 근거 없는 완전 표현이다.",
    "용어 후보 '보안 수준': 정의에서 '목표·역량·달성 수준을 구분하고'를 뺀다 — ref-1105 에 근거가 없고 SL-T 만 언급된다.",
    "용어 후보 '변조 탐지 로그': 정의에서 '앞 기록의 해시를 잇거나 외부에 고정해'를 빼고, f20 이 뒷받침하는 범위(블록체인 같은 수단으로 기록이 고쳐지면 드러나게 하는 기록)로 줄인다. 기존 용어 '감사 추적'과 연결한다 — 해시 체인 방식은 브리프에 근거가 없다.",
    "용어 후보 '간접 프롬프트 주입': 새로 등록한다면 기존 용어 '프롬프트 주입 (Prompt Injection)'의 하위 개념으로 표기하고 두 항목을 서로 연결한다. 정의는 f18(OWASP)의 구분을 따른다 — 기존 용어와 뜻이 겹친다.",
    "두 번째 페이지 제안(docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md): 스토리텔러 입력에 그 페이지의 현재 본문이 있을 때만 6·8·11절을 갱신하고, 같은 주장이 이미 있으면 기존 각주를 다시 쓴다. 본문이 입력에 없으면 이번 실행에서 갱신하지 않고 다음 실행 후보로 남긴다 — 검증에서 중복·모순을 확인하지 못했다.",
    "11절: oq-144 는 해결로 바꾸지 않는다. f15·f17 은 시뮬레이션·실험실 결과인 부분 근거로만 적는다 — 현장 시험 결과가 없다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 1차 조건부 승인. 확인 23건, 미확인 2건, 교차 확인 2건. 강등: f10 사실 → 추정(원문 미열람이고, 검색 결과 요약에 '원격 완전 장악·펌웨어 백도어·인증 우회'가 없음), f12 사실 → 추정('통신 암호화 부족'이 출처에 없음). 원문 미열람 출처: ref-1119(Quarta 외, 검증에서도 403). 주의: 사실 주장의 대부분은 단일 출처다(정부 권고·오픈소스 설계 문서·arXiv 초록). 교차 확인은 두 건뿐이다. 하나는 EU 기계류 규정 요구(f19, 업계 해설과 독립 해설의 검색 결과)이고, 다른 하나는 KISA·한국소비자원 로봇청소기 점검 개요(f12, 기사와 KISA 보도자료의 검색 결과)다. LLM 탈옥·주입 공격과 방어 수치(f14·f15·f17)는 연구·시뮬레이션 환경의 결과다. 3절(왜 중요한가)과 9절(책임 경계)은 추정 종합이다. ROP 2 위협 모델(ref-010)은 원문에 초안(DRAFT) 문서로 표시돼 있다. VDA 5050 3.0.0 의 원문 제목은 'Mobile Robots and a Fleet Control'이고, 같은 URL 이 실행 2026-09-30-10 의 ref-1079 로도 쓰였다. 참고문헌 id ref-1105~ref-405 은 실행 2026-09-30-09 브리프가 다른 출처에 쓴 id 와 겹치므로 퍼블리셔 확인이 필요하다. 브리프에서 webfetch 로 연 출처는 fetch_url 이 비어 있지만, 검증에서 모두 열어 내용을 확인했다(ref-1119 제외). 13. 대화형 기능의 신뢰·기반과 51. 인증·권한·격리 페이지 본문이 입력에 없어 두 페이지와의 중복 검사는 하지 못했다. oq-144 는 해결로 인정하지 않는다(부분 근거 f15·f17). 정정 요청 없음. 검증 검색 3회(리서치 16회와 합쳐 19회/30).",
  "retry_reason": null
}
```

### runs/2026-09-30-11/pages.json

```json
{
  "run_id": "2026-09-30-11",
  "outline": [
    {
      "path": "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 1100,
      "summary": "ROP는 여러 제조사 플릿 서버·브로커·로봇을 한곳에 잇기 때문에 연결 하나가 뚫리면 공격이 로봇 동작으로 이어질 수 있다. [추정][^ref-1109][^ref-031]",
      "planned_findings": [
        "f22",
        "f21",
        "f8",
        "f14",
        "f16",
        "f13",
        "f19"
      ]
    },
    {
      "path": "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 900,
      "summary": "이 영역의 용어는 통신 보호, 위협 관리, 입력 보안, 감사 기록의 네 갈래로 나눠 보면 이해하기 쉽다. [의견]",
      "planned_findings": [
        "f1",
        "f3",
        "f4",
        "f7",
        "f18",
        "f14",
        "f2",
        "f20"
      ]
    },
    {
      "path": "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 1300,
      "summary": "병원 플릿 서버 취약점 공개, 가정 로봇청소기 보안 점검, 제조 공장 산업용 로봇 제어기 분석 세 사례를 여섯 항목으로 정리한다. [추정][^ref-1109][^ref-969][^ref-1119]",
      "planned_findings": [
        "f8",
        "f9",
        "f12",
        "f10"
      ]
    },
    {
      "path": "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1700,
      "summary": "통신 인증·암호화, 위협 모델과 취약점 관리, 대화·문서 입력 방어, 변조 탐지 감사 기록의 네 접근을 겹치는 방향으로 보인다. [추정][^ref-700][^ref-1108]",
      "planned_findings": [
        "f3",
        "f4",
        "f5",
        "f6",
        "f1",
        "f7",
        "f9",
        "f18",
        "f17",
        "f15",
        "f2",
        "f19",
        "f20"
      ]
    },
    {
      "path": "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 700,
      "summary": "통신 보호는 ROS 2 계열 문서와 IEC 62443, 입력 보안은 OWASP LLM01, 감사 기록은 EU 기계류 규정이 주요 기준이다. [추정][^ref-009][^ref-1105][^ref-1108][^ref-1111]",
      "planned_findings": [
        "f1",
        "f3",
        "f5",
        "f6",
        "f7",
        "f18",
        "f19",
        "f13"
      ]
    },
    {
      "path": "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 900,
      "summary": "대표 자료는 실제 취약점 공개와 로봇 분석, LLM 제어 로봇 공격, 방어·감사 기록 연구로 나뉜다. [의견]",
      "planned_findings": [
        "f8",
        "f10",
        "f11",
        "f14",
        "f15",
        "f16",
        "f17",
        "f20"
      ]
    },
    {
      "path": "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 700,
      "summary": "ROP는 자신이 여는 연결·전체 위협 모델·입력 방어·감사 기록을 맡고, 로봇 제어기·펌웨어와 현장 망 보안은 연계 대상으로 둔다. [추정][^ref-1119][^ref-1109]",
      "planned_findings": [
        "f23",
        "f24"
      ]
    },
    {
      "path": "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 1100,
      "summary": "권한·개인정보, 채팅 입력, 플릿 연동, 기록·관제, 언어 모델 계획, 안전, 수명주기, 규제, 현장 유형 영역과 이어진다. [추정][^ref-1109]",
      "planned_findings": [
        "f25"
      ]
    },
    {
      "path": "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md",
      "section": "11. 열린 질문",
      "budget_chars": 800,
      "summary": "oq-144는 시뮬레이션·실험실 수준의 부분 근거만 있어 열림으로 두고, 브로커 보안 프로파일·에이전트 간 전파 방어·감사 기록 비용·EU 규정 적용 범위·KISA 요구 항목 다섯 질문을 새로 연다.",
      "planned_findings": [
        "f6",
        "f15",
        "f16",
        "f17",
        "f19",
        "f20",
        "f13"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "seed → draft: 3~11절 첫 작성(통신 인증·암호화, 위협 모델·IEC 62443, LLM 탈옥·프롬프트 주입 방어, 변조 탐지 감사 기록, 병원·가정·제조 공장 적용 사례, 책임 경계, 연결 19개 영역, 열린 질문), 13절 각주 17건. 2차 수정 6건 반영(5·8절 요약 태그, 6절 도식 안내 문장 분리·일반화 문장 한정, 3절 EU 규정 범위, 연계 대상 해석 태그 분리)"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area52-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 52. 통신 보호·위협 관리·감사 의 \"6. 대표 접근법과 기술\" 절(2,109자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area52-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 52. 통신 보호·위협 관리·감사 의 \"8. 대표 연구와 자료\" 절(1,206자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area52-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 52. 통신 보호·위협 관리·감사 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(1,102자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area52-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 52. 통신 보호·위협 관리·감사 의 \"3. 왜 중요한가\" 절(1,079자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area52-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 52. 통신 보호·위협 관리·감사 의 \"11. 열린 질문\" 절(1,063자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area52-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 52. 통신 보호·위협 관리·감사 의 \"4. 핵심 개념과 용어\" 절(1,031자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-30 | 52. 통신 보호·위협 관리·감사 | seed → draft: 3~11절 첫 작성(통신 인증·암호화, 위협 모델, LLM 입력 방어, 변조 탐지 감사 기록, 병원·가정·제조 공장 사례), 각주 17건 | run 2026-09-30-11",
  "index_updates": {
    "home_recent": "2026-09-30 — 52. 통신 보호·위협 관리·감사: 3~11절 첫 작성(SROS 2·Open-RMF 통신 보호, ROS 2 위협 모델·IEC 62443, LLM 탈옥·프롬프트 주입 방어, 변조 탐지 감사 기록, 병원·가정·제조 공장 사례)",
    "category_recent": "2026-09-30 — 52. 통신 보호·위협 관리·감사: seed → draft, 3~11절 첫 작성과 병원·가정·제조 공장 적용 사례, 열린 질문 5건 추가",
    "area_recent": "2026-09-30 — 52. 통신 보호·위협 관리·감사: 3~11절 첫 작성, 각주 17건, 새 열린 질문 5건(oq-144 는 열림 유지)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "stride-threat-classification",
      "term_ko": "STRIDE 위협 분류",
      "term_en": "STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege)",
      "definition": "위조·변조·부인·정보 노출·서비스 거부·권한 상승 여섯 범주로 시스템 위협을 분류하는 위협 모델링 분류로, ROS 2 위협 모델이 로봇 시스템에 적용했다.",
      "description": "ROS 2 Robotic Systems Threat Model 은 STRIDE 로 위협을 분류하고 DREAD 로 위험을 평가하며 TurtleBot 3·MARA 에 적용했다.",
      "related_areas": [
        52
      ],
      "sources": [
        "ref-010"
      ]
    },
    {
      "action": "new",
      "slug": "indirect-prompt-injection",
      "term_ko": "간접 프롬프트 주입",
      "term_en": "Indirect Prompt Injection",
      "definition": "프롬프트 주입(Prompt Injection)의 하위 유형으로, 사용자가 직접 입력하지 않은 웹 페이지·파일·인식 결과 같은 외부 내용에 숨은 지시가 언어 모델의 행동을 바꾸는 공격이다.",
      "description": "상위 용어: 프롬프트 주입(glossary/prompt-injection.md). OWASP LLM01:2025 는 사용자 입력이 직접 모델 행동을 바꾸는 직접 주입과 이를 구분한다. 다중 에이전트 로봇 시스템 연구는 인식 모듈을 거친 간접 주입이 로봇 행동을 오염시킬 수 있음을 보였다.",
      "related_areas": [
        52,
        13
      ],
      "sources": [
        "ref-1108",
        "ref-1115"
      ]
    },
    {
      "action": "new",
      "slug": "security-level-iec-62443",
      "term_ko": "보안 수준",
      "term_en": "Security Level (SL, IEC 62443)",
      "definition": "IEC 62443 에서 구역·도관이 견뎌야 할 공격자 역량에 따라 SL1~SL4 로 매기는 보호 등급으로, 일곱 기본 요구별 벡터로 표현할 수 있다.",
      "description": "관련 용어: 보안 구역과 도관(glossary/zones-and-conduits.md).",
      "related_areas": [
        52,
        22
      ],
      "sources": [
        "ref-1105"
      ]
    },
    {
      "action": "new",
      "slug": "tamper-evident-log",
      "term_ko": "변조 탐지 로그",
      "term_en": "Tamper-evident Log",
      "definition": "블록체인 같은 수단으로 기록이 나중에 고쳐지면 드러나게 만든 로그로, 책임 추적용 감사 기록의 무결성을 높이는 데 쓴다.",
      "description": "감사 추적(Audit Trail, glossary/audit-trail.md)의 기록 무결성을 높이는 방식이다. Fernández-Becerra 외는 ROS 기반 이동 로봇의 행동 기록에 블록체인 변조 방지를 적용한 블랙박스형 요소를 제안했다.",
      "related_areas": [
        52,
        37
      ],
      "sources": [
        "ref-1112"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-009",
      "org": "Open Robotics (ROS 2 Design, Kyle Fazzari)",
      "title": "ROS 2 DDS-Security integration",
      "published": null,
      "url": "https://design.ros2.org/articles/ros2_dds_security.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "DDS-Security 의 다섯 플러그인 인터페이스와 ROS 2(SROS 2)가 쓰는 인증·접근 통제·암호 세 가지, 보안 환경 변수와 키 저장소 구조를 설명하는 ROS 2 설계 문서.",
      "cited_by": [
        "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-010",
      "org": "Open Robotics (ROS 2 Design, Moulard·Hortala·Perez 외)",
      "title": "ROS 2 Robotic Systems Threat Model",
      "published": null,
      "url": "https://design.ros2.org/articles/ros2_threat_model.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "STRIDE·DREAD 로 ROS 2 로봇 시스템의 통신·소프트웨어·하드웨어·로그 위협과 완화책을 정리하고 TurtleBot 3·MARA 에 적용한 위협 모델 문서.",
      "cited_by": [
        "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1105",
      "org": "IEC (SyC Smart Energy)",
      "title": "IEC 62443",
      "published": null,
      "url": "https://syc-se.iec.ch/deliveries/cybersecurity-guidelines/security-standards-and-best-practices/iec-62443/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "IEC 공식 사이트의 IEC 62443 소개. 구역·도관, 보안 수준 SL1~SL4, 일곱 기본 요구를 설명한다. 표준 본문은 아니다.",
      "cited_by": [
        "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-857",
      "org": "Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J. (arXiv)",
      "title": "Jailbreaking LLM-Controlled Robots",
      "published": "2024-10",
      "url": "https://arxiv.org/abs/2410.13691",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "LLM 제어 로봇을 탈옥하는 RoboPAIR 공격을 세 로봇 설정에서 시연하고 자주 100% 성공률을 보고한 프리프린트.",
      "cited_by": [
        "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-700",
      "org": "Ravichandran, Z., Robey, A. 외 (arXiv)",
      "title": "Safety Guardrails for LLM-Enabled Robots",
      "published": "2025-03",
      "url": "https://arxiv.org/abs/2503.07885",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "신뢰 기반 LLM 과 시간 논리 제어 합성으로 이뤄진 RoboGuard 가드레일이 탈옥 공격 아래 위험 계획 실행을 92% 이상에서 3% 미만으로 줄였다고 보고한 프리프린트.",
      "cited_by": [
        "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1108",
      "org": "OWASP GenAI Security Project",
      "title": "LLM01:2025 Prompt Injection",
      "published": null,
      "url": "https://genai.owasp.org/llmrisk/llm01-prompt-injection/",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "직접·간접 프롬프트 주입의 정의와 최소 권한·사람 승인·외부 내용 분리 등 일곱 가지 완화책을 정리한 OWASP LLM 상위 10 위험 항목.",
      "cited_by": [
        "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1109",
      "org": "CISA (미국 사이버보안·기반시설보안청)",
      "title": "Aethon TUG Home Base Server (ICSA-22-102-05)",
      "published": "2022-04-12",
      "url": "https://www.cisa.gov/news-events/ics-advisories/icsa-22-102-05",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "병원 자율이동로봇 TUG 의 플릿 서버 취약점 5건(인가 누락, 웹소켓 무인증 제어, XSS)과 완화책을 공개한 ICS 권고.",
      "cited_by": [
        "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1110",
      "org": "Mayoral-Vilches, V. (Alias Robotics, arXiv)",
      "title": "The Cybersecurity of a Humanoid Robot",
      "published": "2025-09-17",
      "url": "https://arxiv.org/abs/2509.14096",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "Unitree G1 휴머노이드의 정적 키 암호화 결함과 동의 없는 원격 측정 전송을 분석한 기술 보고서.",
      "cited_by": [
        "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1111",
      "org": "IES (Integrated Equipment Services)",
      "title": "Machinery Regulation Guide",
      "published": "2026-08-27",
      "url": "https://www.ies.co.uk/reference-library/machinery-regulation-guide",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "EU 기계류 규정 (EU) 2023/1230 의 변조 방지·개입 증거 기록·안전 소프트웨어 판 추적 로그 5년 보관·2027-01-20 적용을 해설한 업계 안내서.",
      "cited_by": [
        "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1112",
      "org": "Fernández-Becerra, L., González-Santamarta, M. Á., Guerrero-Higueras, Á. M., Rodríguez-Lera, F. J., & Matellán Olivera, V. (arXiv)",
      "title": "Enhancing Trust in Autonomous Agents: An Architecture for Accountability and Explainability through Blockchain and Large Language Models",
      "published": "2024-03",
      "url": "https://arxiv.org/abs/2403.09567",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "ROS 기반 이동 로봇의 행동 기록을 블록체인으로 변조 방지하는 블랙박스형 책임 추적과 LLM 설명 생성 구조를 제안한 프리프린트.",
      "cited_by": [
        "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-969",
      "org": "바이라인네트워크 (곽중희)",
      "title": "‘로봇청소기’ 다수 제품 보안 취약…대응방안은?",
      "published": "2025-10-31",
      "url": "https://byline.network/2025/10/31-283/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "KISA·한국소비자원의 로봇청소기 6종 40개 항목 보안 점검 결과와 대응방안을 전한 기사. KISA 공지 제목과 내용이 일치한다.",
      "cited_by": [
        "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1114",
      "org": "엠에스투데이",
      "title": "선박·위성·로봇까지 해킹 표적…정부, ‘피지컬 AI’ 산업 보안 기준 제시",
      "published": "2026-03-06",
      "url": "https://www.mstoday.co.kr/news/articleView.html?idxno=100755",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "과기정통부·KISA 가 로봇 보안모델 고도화판과 사이버보안 요구사항 해설서를 KISA 지식플랫폼으로 배포했다고 전한 기사.",
      "cited_by": [
        "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1115",
      "org": "Nagaraja, N., Bagari, A., & Bahsi, H. (arXiv)",
      "title": "When Prompts Control Robots: Prompt Injection Attacks in Multi-Agent Robotic Systems",
      "published": "2026-08",
      "url": "https://arxiv.org/abs/2608.00747",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "LLM 기반 다중 에이전트 로봇 시스템에서 직접·간접 프롬프트 주입과 에이전트 간 전파를 체계적으로 분석한 프리프린트.",
      "cited_by": [
        "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1116",
      "org": "Zhang, W., Kong, X., Dewitt, C., Braunl, T., & Hong, J. B. (arXiv)",
      "title": "A Study on Prompt Injection Attack Against LLM-Integrated Mobile Robotic Systems",
      "published": "2024-08",
      "url": "https://arxiv.org/abs/2408.03515",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "GPT-4o 통합 이동 로봇 주행 시뮬레이션에서 프롬프트 주입 영향과 보안 프롬프트·응답 기반 탐지 방어(약 30.8% 개선)를 보고한 프리프린트.",
      "cited_by": [
        "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 공식 저장소)",
      "title": "VDA 5050 — Interface for the Communication between Mobile Robots and a Fleet Control (VDA5050_EN.md, 3.0.0)",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "이동 로봇–플릿 관제 통신 규격 3.0.0 원문. 프로토콜 보안은 브로커 구성에서 고려해야 하지만 이 지침은 다루지 않는다고 적는다.",
      "cited_by": [
        "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-405",
      "org": "Open Robotics (Programming Multiple Robots with ROS 2)",
      "title": "Security",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/security.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 의 ROS 2 부분(SROS 2 키 저장소·인클레이브)과 웹 대시보드(TLS·Keycloak OIDC·역할 기반 접근 통제) 보안을 설명하는 공식 책의 보안 장.",
      "cited_by": [
        "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1119",
      "org": "Quarta, D., Pogliani, M., Polino, M., Maggi, F., Zanchettin, A. M., & Zanero, S. (IEEE S&P 2017)",
      "title": "An Experimental Security Analysis of an Industrial Robot Controller",
      "published": "2017",
      "url": "https://files01.core.ac.uk/download/pdf/84891817.pdf",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 산업용 로봇 제어기의 소프트웨어 취약점과 구조적 결함이 제어 정확성과 작업자 안전 요구를 무너뜨릴 수 있음을 실험으로 보인 IEEE 보안 학회 논문(검색 결과 요약 기준).",
      "cited_by": [
        "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md"
      ],
      "source_unopened": true
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "여러 제조사 플릿 관리 서버와 VDA 5050 브로커·Open-RMF 어댑터를 잇는 ROP 에서 브로커·API 의 상호 인증과 TLS 설정의 최소 요구를 정한 공개 보안 프로파일이 있는가?",
      "areas": [
        52,
        20,
        21
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "LLM 에이전트 여러 개가 로봇을 나눠 맡을 때 한 에이전트에 주입된 지시가 다른 에이전트로 퍼지지 않게 에이전트 간 메시지에 신뢰 경계를 두는 방어의 효과를 잰 연구가 있는가?",
      "areas": [
        52,
        13,
        12
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "명령·승인 감사 기록을 해시 체인·블록체인으로 변조 탐지 가능하게 남길 때 수백 대 로봇 규모의 명령 빈도에서 지연·저장 비용을 측정한 자료가 있는가?",
      "areas": [
        52,
        37
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "EU 기계류 규정의 개입 증거 기록·안전 소프트웨어 추적 로그 요구가 개별 기계 밖에서 여러 로봇을 지시하는 오케스트레이션 플랫폼에도 미치는가, 미친다면 기록 책임은 누구에게 있는가?",
      "areas": [
        52,
        59,
        58
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "KISA 로봇 보안모델(고도화)과 사이버보안 요구사항 해설서는 로봇 통신 암호화·감사 기록·원격 업데이트에 어떤 요구 항목을 두며 다중 로봇 관제 플랫폼을 대상에 포함하는가?",
      "areas": [
        52,
        59
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "병원",
      "item": "작업 대상",
      "link": "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md#5-적용-사례-현장-유형-명시",
      "title": "52. 통신 보호·위협 관리·감사"
    },
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md#5-적용-사례-현장-유형-명시",
      "title": "52. 통신 보호·위협 관리·감사"
    },
    {
      "site_type": "병원",
      "item": "제약",
      "link": "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md#5-적용-사례-현장-유형-명시",
      "title": "52. 통신 보호·위협 관리·감사"
    },
    {
      "site_type": "병원",
      "item": "예외·성과",
      "link": "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md#5-적용-사례-현장-유형-명시",
      "title": "52. 통신 보호·위협 관리·감사"
    },
    {
      "site_type": "가정",
      "item": "작업 대상",
      "link": "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md#5-적용-사례-현장-유형-명시",
      "title": "52. 통신 보호·위협 관리·감사"
    },
    {
      "site_type": "가정",
      "item": "수행 자원",
      "link": "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md#5-적용-사례-현장-유형-명시",
      "title": "52. 통신 보호·위협 관리·감사"
    },
    {
      "site_type": "가정",
      "item": "예외·성과",
      "link": "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md#5-적용-사례-현장-유형-명시",
      "title": "52. 통신 보호·위협 관리·감사"
    },
    {
      "site_type": "제조 공장",
      "item": "작업 대상",
      "link": "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md#5-적용-사례-현장-유형-명시",
      "title": "52. 통신 보호·위협 관리·감사"
    },
    {
      "site_type": "제조 공장",
      "item": "예외·성과",
      "link": "docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md#5-적용-사례-현장-유형-명시",
      "title": "52. 통신 보호·위협 관리·감사"
    }
  ],
  "standards_updates": [
    {
      "name": "OWASP Top 10 for LLM Applications 2025 (LLM01 Prompt Injection)",
      "kind": "프레임워크",
      "org": "OWASP GenAI Security Project",
      "url": "https://genai.owasp.org/llmrisk/llm01-prompt-injection/",
      "related_areas": [
        52,
        13
      ],
      "summary": "직접·간접 프롬프트 주입을 구분하고 출력 형식 검증·최소 권한·고위험 행동의 사람 승인·외부 내용 분리 등 완화책을 제시하며, 확실한 예방법은 아직 불분명하다고 밝힌다.",
      "ref_id": "ref-1108"
    },
    {
      "name": "EU 기계류 규정 (EU) 2023/1230 (변조 보호·개입 증거 기록, 업계 해설 기준)",
      "kind": "프레임워크",
      "org": "European Union (IES 해설 경유)",
      "url": "https://www.ies.co.uk/reference-library/machinery-regulation-guide",
      "related_areas": [
        52,
        59,
        50
      ],
      "summary": "2027-01-20 전면 적용. 규정 준수에 결정적인 하드웨어·소프트웨어의 변조 보호, 안전 관련 소프트웨어 식별과 개입 증거 기록, 출시 후 안전 소프트웨어 판 추적 로그 5년 보관을 요구한다(업계 해설 기준, 규정 원문 미열람).",
      "ref_id": "ref-1111"
    },
    {
      "name": "KISA 로봇 분야 보안모델 고도화판·사이버보안 요구사항 해설서",
      "kind": "프레임워크",
      "org": "과학기술정보통신부·한국인터넷진흥원(KISA)",
      "url": "https://www.mstoday.co.kr/news/articleView.html?idxno=100755",
      "related_areas": [
        52,
        59
      ],
      "summary": "2026년 3월 KISA 지식플랫폼 자료실로 무료 배포된, 로봇 제품 개발·수출 때 참고할 보안 자료(기사 기준, 원문 미열람).",
      "ref_id": "ref-1114"
    }
  ],
  "additional_research_requests": [
    "13. 대화형 기능의 신뢰·기반 페이지(docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 6·8·11절 반영: 1차 검증 지시대로 현재 본문이 입력에 없어 이번 실행에서 갱신하지 않았다. 다음 실행에서 그 페이지 본문을 입력에 넣고 RoboPAIR·다중 에이전트 주입(ref-857·ref-1115), RoboGuard·보안 프롬프트 방어·OWASP LLM01(ref-700·ref-1116·ref-1108)과의 중복을 확인해 반영할 것.",
    "5절 적용 사례: 물류창고·상업 시설·실외 현장의 로봇 통신 보호·위협·감사 사례(예: 물류창고 AMR 플릿 관리 소프트웨어 취약점 권고)를 찾지 못했다. 현장 유형 균형을 위해 필요하다.",
    "4·6·7절: IEC 62443-3-3 의 감사 관련 요구(감사 대상 사건, 부인 방지, 감사 정보 보호 등)를 원문 또는 공식 자료로 확인해야 감사 기록 요구를 표준 근거로 쓸 수 있다.",
    "5·8절: Quarta 외(ref-1119) 원문을 열어 공격 유형과 원격 장악 여부를 확인하면 [추정]을 [사실]로 되돌릴 근거가 된다.",
    "6·7절: EU 기계류 규정 (EU) 2023/1230 원문(EUR-Lex)을 열어 변조 보호·개입 증거 기록·추적 로그 요구의 조항 번호와 문구를 확인할 것(현재 업계 해설 기준).",
    "7·11절: KISA 로봇 보안모델 고도화판·사이버보안 요구사항 해설서 원문의 요구 항목(통신 암호화·감사 기록·원격 업데이트)과 대상 범위를 확인할 것.",
    "퍼블리셔 확인 요청: 이번 브리프의 ref-1105~ref-1119 가 실행 2026-09-30-09 브리프의 다른 출처 id 와 겹칠 수 있고, ref-031(VDA 5050 3.0.0)은 실행 2026-09-30-10 의 ref-1079 와 URL 이 같다. id 병합·재부여 시 이 페이지의 각주 id 도 함께 바꿔야 한다.",
    "분리 코드 담당 확인 요청: 이번 재실행은 세부영역 페이지를 3~11절 전체 본문으로 다시 냈으므로 분량 자동 분리가 다시 실행돼야 한다(이전 초안의 분리 주제 페이지 6건은 이 본문에서 새로 만들어야 2차 수정이 반영된다). 분리 주제 페이지의 '9. 검증 노트'가 2차 통과 전에 '1차·2차 검증을 거쳤다'로 적히는 문제는 2차 검증이 지적했다."
  ],
  "fixes_applied": [
    "f10 강등 — 5절 제조 공장 사례의 작업 대상·예외·성과 칸과 8절 Quarta 외 항목을 [추정]으로 쓰고, 검색 결과 요약으로 확인된 범위(소프트웨어 취약점과 구조적 결함으로 제어 정확성과 작업자 안전 요구를 무너뜨릴 수 있음)만 남겼으며 '원격 완전 장악'·'펌웨어 백도어·인증 우회'는 뺐다.",
    "ref-1119 — 13절 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고, reference_updates 의 ref-1119 항목에 source_unopened: true 를 넣고 요약을 '원문 미열람.'으로 시작했다.",
    "f12 — '통신 암호화 부족'을 빼고 5절 가정 사례의 작업 대상·수행 자원·예외·성과 문장을 [추정]으로 강등했으며, 점검 주체·기간·6종·40개 항목과 나르왈·드리미·에코백스 제품의 사진 열람·카메라 강제 활성화, 미흡한 사용자 인증, 개인정보 조회만 남겼다.",
    "f6·ref-031 — 13절 각주와 reference_updates 의 제목을 'VDA 5050 — Interface for the Communication between Mobile Robots and a Fleet Control (VDA5050_EN.md, 3.0.0)'으로 고쳤고, 본문(3·6·7절)에서 '플릿 관제–이동 로봇'으로 쓰며, 6절에서 원문 문장 그대로 '프로토콜 보안은 브로커 구성에서 고려해야 하지만 이 지침은 다루지 않는다'를 [사실]로, '운영자와 통합 사업자가 정해야 한다'는 별도 문장 [추정]으로 떼어 썼다.",
    "f4 — 6절에서 엄격 모드를 '보안 파일을 찾지 못한 참여자를 실행하지 않는 모드', 허용 모드를 '보안 파일이 없으면 보안 기능 없이 실행하는 기본 모드'로 고쳐 썼다.",
    "f21 — 3절 마지막 단락의 종합 문장에서 f10(제어기) 근거를 빼고 전면 제어 사례는 CISA 권고(ref-1109)에만 기대게 했으며, '높은 확률로 탈옥'을 '연구 환경에서 높은 공격 성공률이 보고됐다'로 바꿨다.",
    "f22 — 3절에서 '플릿 서버 취약점이 로봇 기능 전면 제어로 이어질 수 있음'으로 줄였고, KISA 해설서는 '제품 개발·수출 때 참고할 자료로 배포'로만 서술해 '제품 요건' 표현을 쓰지 않았다(EU 규정은 '요구한다'로만 썼다).",
    "3·5·6·9절 — f9 의 방화벽·VPN·망 격리는 5절 제약 칸과 6절에서 '시설 IT/OT 쪽 연계 대상'으로 표시했고, f10·f11 의 제어기·펌웨어·제조사 원격 측정은 사례·위협 근거로만 쓰고 9절 표의 '연계 대상:' 칸에 짧게 두었다.",
    "f19 — 3·6·7절에서 근거가 업계 해설(IES, 2026-08-27 갱신)임을 밝히고, 6절에 규정 원문을 열지 못해 조항 번호는 적지 않는다고 적었다.",
    "용어 후보 'STRIDE 위협 분류' — glossary_updates 정의에서 '빠짐없이 떠올리도록 돕는'을 빼고 '여섯 범주로 시스템 위협을 분류하는'으로 썼다.",
    "용어 후보 '보안 수준' — glossary_updates 정의에서 '목표·역량·달성 수준을 구분하고'를 뺐다.",
    "용어 후보 '변조 탐지 로그' — glossary_updates 정의에서 '앞 기록의 해시를 잇거나 외부에 고정해'를 빼고 '블록체인 같은 수단으로 기록이 고쳐지면 드러나게 만든 로그'로 줄였으며, 설명에 기존 용어 '감사 추적(Audit Trail)'과의 관계와 링크를 적었다.",
    "용어 후보 '간접 프롬프트 주입' — glossary_updates 정의를 기존 용어 '프롬프트 주입(Prompt Injection)'의 하위 유형으로 표기하고 f18(OWASP)의 직접·간접 구분을 따랐으며, 설명에 상위 용어 링크를 적었다(4절 본문에서도 프롬프트 주입 항목 안에서 간접 주입을 설명했다).",
    "두 번째 페이지 제안(13. 대화형 기능의 신뢰·기반) — 현재 본문이 입력에 없어 이번 실행에서 갱신하지 않았고, additional_research_requests 에 다음 실행 후보로 남겼다.",
    "11절 — oq-144 를 '열림'으로 두고 f15·f17 을 시뮬레이션·실험실 수준의 부분 근거로만 적었으며, open_question_updates 에 해결 갱신을 넣지 않았다.",
    "2차: 5절 첫 문장 — 태그를 [사실]에서 [추정]으로 바꾸고 각주를 [^ref-1109][^ref-969][^ref-1119]로 늘렸다(outline 5절 요약도 같게 고쳤다).",
    "2차: 8절 첫 문장 — 태그를 [의견]으로 바꾸고 각주를 뗐다(분리 시 주제 페이지의 세 줄 요약과 본문 첫 문장에도 같은 문장이 옮겨진다. outline 8절 요약도 같게 고쳤다).",
    "2차: 6절 — '아래 도식은 이번 자료를 종합한 다층 방어의 추정 구조다.'를 첫 단락에서 떼어 mermaid 블록 바로 앞의 별도 단락으로 옮겼다.",
    "2차: 6절 '위협 모델과 취약점 관리' — 태그 없는 일반화 문장 '공개된 취약점에는 갱신과 망 격리로 대응한다.'를 지우고 'CISA는 TUG 서버 취약점의 완화책으로 버전 갱신, 방화벽 뒤 격리, 원격 접속 시 VPN을 권고했다. [사실][^ref-1109]'로 이 사례 하나에 한정해 썼다.",
    "2차: 3절 셋째 단락 — EU 기계류 규정 문장을 '규정 준수에 결정적인 하드웨어·소프트웨어의 변조 보호와, 기계가 안전 관련 소프트웨어를 식별하고 개입 증거를 기록하는 것을 요구한다'로 고쳤다(standards_updates 요약도 같게 맞췄다).",
    "2차: 5절 병원 표 '제약' 칸의 괄호를 빼고 '… VPN이다. [사실][^ref-1109] 이 가운데 망 조치는 시설 IT/OT 쪽 연계 대상이다. [추정][^ref-1109]'로 태그를 나눴고, 8절 Mayoral-Vilches 항목 끝을 '… 외부 서버로 간다고 보고했다. [사실][^ref-1110] 이는 로봇 제조사 쪽 연계 대상의 위협 근거로 보인다. [추정][^ref-1110]'로 나눴다.",
    "분량 초과 자동 분리: 52. 통신 보호·위협 관리·감사 본문 10,696자 > 기준 4,000자 → 6개 절을 주제 페이지로 옮김, 남은 본문 3,895자"
  ]
}
```

### runs/2026-09-30-11/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 분량 초과 자동 분리:
    - docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-09-30-area52-s6.md (2,109자)
    - docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md "8. 대표 연구와 자료" → docs/topics/2026/2026-09-30-area52-s8.md (1,206자)
    - docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-09-30-area52-s10.md (1,102자)
    - docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md "3. 왜 중요한가" → docs/topics/2026/2026-09-30-area52-s3.md (1,079자)
    - docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md "11. 열린 질문" → docs/topics/2026/2026-09-30-area52-s11.md (1,063자)
    - docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-09-30-area52-s4.md (1,031자)
```

### runs/2026-09-30-11/pages/categories/security-and-privacy/communication-protection-threat-management-and-audit.md

```markdown
---
title: "52. 통신 보호·위협 관리·감사"
type: area
category: "N. 보안·개인정보"
area_no: 52
related_areas: [12, 13, 20, 21, 22, 37, 38, 42, 44, 48, 50, 51, 53, 54, 57, 59, 62, 63, 65]
tags: [SROS 2, 위협 모델, IEC 62443, 프롬프트 주입, 감사 기록]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-30
sources: [ref-009, ref-010, ref-1105, ref-857, ref-700, ref-1108, ref-1109, ref-1110, ref-1111, ref-1112, ref-969, ref-1114, ref-1115, ref-1116, ref-031, ref-405, ref-1119]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [N. 보안·개인정보](index.md) › 52. 통신 보호·위협 관리·감사

# 52. 통신 보호·위협 관리·감사

!!! info "소속 대분류"
    [N. 보안·개인정보](index.md) — 핵심 질문:
    누가 어떤 로봇에 무엇을 시킬 수 있는지 통제하고, 데이터와 사람의 정보를 어떻게 지킬 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

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

## 3. 왜 중요한가

ROP는 여러 제조사의 플릿 관리 서버·브로커·로봇을 한곳에 잇기 때문에, 그 연결 가운데 하나가 뚫리면 공격이 곧 로봇 동작으로 이어질 수 있다. [추정][^ref-1109][^ref-031]

자세한 내용은 주제 페이지 [52. 통신 보호·위협 관리·감사 — 왜 중요한가](../../topics/2026/2026-09-30-area52-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 영역의 용어는 통신 보호, 위협 관리, 입력 보안, 감사 기록의 네 갈래로 나눠 보면 이해하기 쉽다. [의견]

자세한 내용은 주제 페이지 [52. 통신 보호·위협 관리·감사 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area52-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이 영역의 실제 사례는 병원의 플릿 서버 취약점 공개, 가정의 로봇청소기 보안 점검, 제조 공장의 산업용 로봇 제어기 분석에서 확인된다. [추정][^ref-1109][^ref-969][^ref-1119]

**현장 유형:** 병원

**사례:** 병원 자율이동로봇 TUG의 플릿 서버 취약점 공개(CISA 권고 ICSA-22-102-05, 2022-04-12)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 병원 자율이동로봇 TUG를 제어·통신하는 Aethon TUG Home Base Server(버전 24 이전 전체). [사실][^ref-1109] |
| 수행 자원 | TUG 로봇과 이를 제어·통신하는 Home Base Server. [사실][^ref-1109] |
| 제약 | 권고된 완화책은 버전 24 갱신, 현장 방화벽 활성화 확인, 제어 시스템 기기의 인터넷 비노출·방화벽 뒤 격리, 원격 접속 시 VPN이다. [사실][^ref-1109] 이 가운데 망 조치는 시설 IT/OT 쪽 연계 대상이다. [추정][^ref-1109] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 인가 누락(CVE-2022-1066·CVE-2022-26423, CVSS 8.2), 인증 없이 웹소켓에 접속해 로봇을 제어할 수 있는 채널(CVE-2022-1070, CVSS 9.8), 교차 사이트 스크립팅 2건이 공개됐고, 악용되면 서비스 거부·로봇 기능 전면 제어·민감 정보 노출이 가능하다. [사실][^ref-1109] |

이 사례에서 이 영역이 관여하는 곳은 작업 대상인 플릿 서버의 통신·권한과, 예외·성과에 드러난 피해 범위다. [추정][^ref-1109] 여러 제조사의 플릿 서버를 잇는 ROP라면 연결하는 서버마다 인증·인가를 확인하고, 방화벽·VPN 같은 망 조치는 병원 IT/OT 쪽과 나눠 맡는 것으로 보인다. [추정][^ref-1109]

**현장 유형:** 가정

**사례:** 국내 판매 로봇청소기 보안 점검(KISA·한국소비자원, 2025년 3~7월)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 로봇청소기가 찍은 집 안 사진·카메라 영상과 사용자 이름·전화번호 같은 개인정보. [추정][^ref-969] |
| 수행 자원 | 로봇청소기 6종과 그 모바일앱(점검 영역: 모바일앱 보안·정책 관리·기기 보안, 40개 항목). [추정][^ref-969] |
| 제약 | 해당 없음 |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 일부 제품(나르왈·드리미·에코백스)에서 사진 열람·카메라 강제 활성화, 미흡한 사용자 인증, 사용자 ID로 이름·전화번호 조회가 확인됐다고 보도됐다(2025-10-31 기사 기준). [추정][^ref-969] |

가정에서는 로봇이 다루는 정보 자체가 사생활이어서, 인증이 약하면 피해가 곧 개인정보·영상 문제로 번지는 것으로 보인다. [추정][^ref-969]

**현장 유형:** 제조 공장

**사례:** 산업용 로봇 제어기 보안 분석(Quarta 외, IEEE Symposium on Security and Privacy 2017)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | 널리 쓰이는 산업용 로봇 제어기. [추정][^ref-1119] |
| 수행 자원 | 해당 없음 |
| 제약 | 해당 없음 |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 제어기의 소프트웨어 취약점과 구조적 결함으로 제어 정확성과 작업자 안전 요구를 무너뜨릴 수 있음을 실험으로 보였다(원문 미열람, 검색 결과 요약 기준). [추정][^ref-1119] |

제어기 자체의 보안은 로봇 제조사 쪽 연계 대상이며, ROP에서는 연결 대상 로봇의 위협 근거로 쓴다. [추정][^ref-1119]

물류창고·상업 시설·실외 현장의 통신·감사 사례는 이번 조사에서 확인하지 못했다.

## 6. 대표 접근법과 기술

대표 접근법은 통신 인증·암호화, 위협 모델과 취약점 관리, 대화·문서 입력 방어, 변조 탐지 감사 기록의 네 가지이며, 어느 하나로 공격을 확실히 막는다는 근거가 없어 여러 층을 겹치는 방향으로 보인다. [추정][^ref-700][^ref-1108]

자세한 내용은 주제 페이지 [52. 통신 보호·위협 관리·감사 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area52-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

통신 보호에는 ROS 2 계열 문서와 IEC 62443, 입력 보안에는 OWASP 항목, 감사 기록에는 EU 기계류 규정이 주요 기준이 되고 있다. [추정][^ref-009][^ref-1105][^ref-1108][^ref-1111]

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| ROS 2 위협 모델(ROS 2 Robotic Systems Threat Model) | 프레임워크 | STRIDE·DREAD로 로봇 시스템 위협과 완화책을 정리한 설계 문서 | [사실][^ref-010] |
| ROS 2 DDS-Security 통합(SROS 2) | 프레임워크 | 인증·접근 통제·암호로 ROS 2 통신을 보호 | [사실][^ref-009] |
| Open-RMF 보안(공식 책 보안 장) | 오픈소스 | ROS 2 부분(SROS 2)과 웹 대시보드(TLS·OIDC·역할 기반 접근 통제)의 두 층 | [사실][^ref-405] |
| VDA 5050 3.0.0 | 표준 | 프로토콜 보안을 브로커 구성에 맡기고 지침 안에서 다루지 않음 | [사실][^ref-031] |
| IEC 62443(62443-3-3 포함) | 표준 | 구역·도관, 보안 수준 SL1~SL4, 일곱 기본 요구 | [사실][^ref-1105] |
| OWASP LLM01:2025 프롬프트 주입 | 프레임워크 | 직접·간접 주입 구분과 완화책 | [사실][^ref-1108] |
| EU 기계류 규정 (EU) 2023/1230 | 프레임워크 | 변조 보호·개입 증거 기록·안전 소프트웨어 판 추적 로그(업계 해설 기준, 2027-01-20 전면 적용) | [사실][^ref-1111] |
| KISA 로봇 분야 보안모델 고도화판·사이버보안 요구사항 해설서 | 프레임워크 | 로봇 제품 개발·수출 때 참고할 보안 자료(원문 미열람, 기사 기준) | [사실][^ref-1114] |

전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

## 8. 대표 연구와 자료

대표 자료는 실제 취약점 공개와 로봇 분석, LLM 제어 로봇 공격, 방어·감사 기록 연구로 나뉜다. [의견]

자세한 내용은 주제 페이지 [52. 통신 보호·위협 관리·감사 — 대표 연구와 자료](../../topics/2026/2026-09-30-area52-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

이종 제조사를 잇는 ROP는 자신이 여는 연결과 전체 연결 구조의 보안을 맡고, 로봇 제어기·펌웨어와 현장 망 보안은 로봇 제조사와 시설 IT/OT 쪽에 보안 요구를 제시하고 연결 시점에 준수 여부를 확인하는 연계 대상으로 두는 것으로 보인다. [추정][^ref-1119][^ref-1109]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 자신이 여는 브로커·API·ROS 2 노드의 통신 인증·암호화와 인클레이브·권한 설정, 연결 시점의 보안 요구 준수 확인. [추정][^ref-009][^ref-405] | 연계 대상: 로봇 제어기·펌웨어의 암호화·서명, 제조사 클라우드 원격 측정(로봇 제조사). [추정][^ref-1119][^ref-1110] |
| 시설·설비 제어 | 여러 제조사 시스템과 현장 망을 포함한 전체 연결 구조의 위협 모델. [추정][^ref-010][^ref-1105] | 연계 대상: 현장 망의 방화벽·VPN·구역 설계(시설 IT/OT 보안). [추정][^ref-1109][^ref-1105] |

ROP가 직접 맡을 범위는 자신이 여는 연결의 통신 보호, 전체 연결 구조의 위협 모델, 채팅·문서 입력과 외부 내용의 분리 및 언어 모델 계획의 실행 전 규칙 검사·사람 승인, 그리고 지시·승인·구성 변경을 변조 탐지 가능하게 남기는 감사 기록으로 보인다. [추정][^ref-009][^ref-010][^ref-700][^ref-1108][^ref-1111][^ref-1112]

분류 원문 19장은 "이 경계는 제품 전략에 따라 이동할 수 있다"고 적는다. 경계의 기준은 [ROP 범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 권한·개인정보, 채팅 입력, 플릿 연동, 기록·관제, 언어 모델 계획, 안전, 수명주기, 규제, 현장 유형 영역과 이어진다. [추정][^ref-1109]

자세한 내용은 주제 페이지 [52. 통신 보호·위협 관리·감사 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area52-s10.md)에 있다.

## 11. 열린 질문

대화 지시 방어의 현장 효과, 브로커 보안 프로파일, 감사 기록의 규모별 비용과 규제 적용 범위가 아직 열려 있다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [52. 통신 보호·위협 관리·감사 — 열린 질문](../../topics/2026/2026-09-30-area52-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-009]: ROS 2 Design, ROS 2 DDS-Security Integration, 미확인, https://design.ros2.org/articles/ros2_dds_security.html, 접근일 2026-09-28
[^ref-010]: ROS 2 Design, ROS 2 Robotic Systems Threat Model, 미확인, https://design.ros2.org/articles/ros2_threat_model.html, 접근일 2026-09-28
[^ref-1105]: IEC (SyC Smart Energy), IEC 62443, 미확인, https://syc-se.iec.ch/deliveries/cybersecurity-guidelines/security-standards-and-best-practices/iec-62443/, 접근일 2026-09-30
[^ref-700]: Ravichandran, Z., Robey, A. 외 (arXiv), Safety Guardrails for LLM-Enabled Robots, 2025-03, https://arxiv.org/abs/2503.07885, 접근일 2026-09-30
[^ref-1108]: OWASP GenAI Security Project, LLM01:2025 Prompt Injection, 미확인, https://genai.owasp.org/llmrisk/llm01-prompt-injection/, 접근일 2026-09-30
[^ref-1109]: CISA (미국 사이버보안·기반시설보안청), Aethon TUG Home Base Server (ICSA-22-102-05), 2022-04-12, https://www.cisa.gov/news-events/ics-advisories/icsa-22-102-05, 접근일 2026-09-30
[^ref-1110]: Mayoral-Vilches, V. (Alias Robotics, arXiv), The Cybersecurity of a Humanoid Robot, 2025-09-17, https://arxiv.org/abs/2509.14096, 접근일 2026-09-30
[^ref-1111]: IES (Integrated Equipment Services), Machinery Regulation Guide, 2026-08-27, https://www.ies.co.uk/reference-library/machinery-regulation-guide, 접근일 2026-09-30
[^ref-1112]: Fernández-Becerra, L., González-Santamarta, M. Á., Guerrero-Higueras, Á. M., Rodríguez-Lera, F. J., & Matellán Olivera, V. (arXiv), Enhancing Trust in Autonomous Agents: An Architecture for Accountability and Explainability through Blockchain and Large Language Models, 2024-03, https://arxiv.org/abs/2403.09567, 접근일 2026-09-30
[^ref-969]: 바이라인네트워크 (곽중희), ‘로봇청소기’ 다수 제품 보안 취약…대응방안은?, 2025-10-31, https://byline.network/2025/10/31-283/, 접근일 2026-09-30
[^ref-1114]: 엠에스투데이, 선박·위성·로봇까지 해킹 표적…정부, ‘피지컬 AI’ 산업 보안 기준 제시, 2026-03-06, https://www.mstoday.co.kr/news/articleView.html?idxno=100755, 접근일 2026-09-30
[^ref-031]: VDA / VDMA (VDA5050 공식 저장소), VDA 5050 — Interface for the Communication between Mobile Robots and a Fleet Control (VDA5050_EN.md, 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-405]: Open Robotics (Programming Multiple Robots with ROS 2), Security, 미확인, https://osrf.github.io/ros2multirobotbook/security.html, 접근일 2026-09-30
[^ref-1119]: Quarta, D., Pogliani, M., Polino, M., Maggi, F., Zanchettin, A. M., & Zanero, S. (IEEE S&P 2017), An Experimental Security Analysis of an Industrial Robot Controller, 2017, https://files01.core.ac.uk/download/pdf/84891817.pdf, 접근일 2026-09-30 (원문 미열람)
```

### docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md

```markdown
---
title: "52. 통신 보호·위협 관리·감사"
type: area
category: "N. 보안·개인정보"
area_no: 52
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [N. 보안·개인정보](index.md) › 52. 통신 보호·위협 관리·감사

# 52. 통신 보호·위협 관리·감사

!!! info "소속 대분류"
    [N. 보안·개인정보](index.md) — 핵심 질문:
    누가 어떤 로봇에 무엇을 시킬 수 있는지 통제하고, 데이터와 사람의 정보를 어떻게 지킬 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

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

### runs/2026-09-30-11/pages/topics/2026/2026-09-30-area52-s6.md

````markdown
---
title: "52. 통신 보호·위협 관리·감사 — 대표 접근법과 기술"
type: topic
category: "N. 보안·개인정보"
primary_area_no: 52
related_areas: [12, 13, 20, 21, 22, 37, 38, 42, 44, 48, 50, 51, 53, 54, 57, 59, 62, 63, 65]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-009, ref-010, ref-031, ref-1105, ref-1108, ref-1109, ref-1111, ref-1112, ref-1116, ref-405, ref-700]
last_run: 2026-09-30
version: 1
split_from: docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md#6
---

[홈](../../index.md) › [주제](../index.md) › 52. 통신 보호·위협 관리·감사 — 대표 접근법과 기술

# 52. 통신 보호·위협 관리·감사 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 대표 접근법은 통신 인증·암호화, 위협 모델과 취약점 관리, 대화·문서 입력 방어, 변조 탐지 감사 기록의 네 가지이며, 어느 하나로 공격을 확실히 막는다는 근거가 없어 여러 층을 겹치는 방향으로 보인다. [추정][^ref-700][^ref-1108]
- 이 페이지는 [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

대표 접근법은 통신 인증·암호화, 위협 모델과 취약점 관리, 대화·문서 입력 방어, 변조 탐지 감사 기록의 네 가지이며, 어느 하나로 공격을 확실히 막는다는 근거가 없어 여러 층을 겹치는 방향으로 보인다. [추정][^ref-700][^ref-1108]

아래 도식은 이번 자료를 종합한 다층 방어의 추정 구조다.

```mermaid
flowchart LR
  input["채팅·문서·인식 입력"] --> sep["외부 내용 분리·표시"]
  sep --> plan["언어 모델 계획"]
  plan --> check["실행 전 규칙 검사"]
  check --> approve["사람 승인"]
  approve --> comm["통신 인증·암호화"]
  comm --> robot["제조사 플릿 서버·로봇"]
  approve -.-> audit["변조 탐지 감사 기록"]
  comm -.-> audit
```

### 통신 인증·암호화

ROS 2의 보안 도구 SROS 2는 DDS-Security의 다섯 플러그인 인터페이스 가운데 인증(공개 키 기반 구조)·접근 통제(governance·permissions 파일)·암호(AES-GCM) 셋만 쓴다. [사실][^ref-009] 로깅과 데이터 태깅은 규격 준수에 필수가 아니어서 모든 DDS 구현이 지원하지는 않는다(2020-07 수정판 기준). [사실][^ref-009]

SROS 2는 ROS_SECURITY_ENABLE·ROS_SECURITY_KEYSTORE·ROS_SECURITY_STRATEGY 환경 변수로 켠다. 전략이 Enforce면 보안 파일을 찾지 못한 참여자를 실행하지 않는 엄격 모드이고, 그 밖에는 보안 파일이 없으면 보안 기능 없이 실행하는 기본 허용 모드다. [사실][^ref-009]

Open-RMF 공식 책은 보안을 SROS 2로 보호하는 ROS 2 부분과, TLS·OpenID Connect(Keycloak) 사용자 인증·역할 기반 접근 통제로 보호하는 웹 대시보드 부분의 두 층으로 설명한다. [사실][^ref-405] 같은 문서는 ROS 2 보안 이벤트 로깅이 구현돼 있지 않고 SROS 2가 런치 파일을 아직 지원하지 않는다고 적는다. [사실][^ref-405]

플릿 관제–이동 로봇 통신 규격 VDA 5050 3.0.0은 프로토콜 보안은 브로커 구성에서 고려해야 하지만 이 지침은 다루지 않는다고 적는다. [사실][^ref-031] 따라서 브로커의 인증·암호화 방식은 운영자와 통합 사업자가 정해야 하는 것으로 보인다. [추정][^ref-031]

### 위협 모델과 취약점 관리

ROS 2 위협 모델(2019-03 작성, 2021-01 최종 수정, 원문에 초안으로 표시)은 STRIDE로 위협을 분류하고 DREAD로 위험을 평가하며 TurtleBot 3와 MARA 모듈형 로봇에 적용했다. [사실][^ref-010] 통신 위협으로는 구성요소 신원 위조, 메시지 가로채기·변조, 채널 무단 접근, 도청을 든다. [사실][^ref-010]

IEC 62443은 위험 기준으로 자산을 묶은 구역과 구역 사이 통신인 도관을 두고 구역마다 목표 보안 수준을 정한다. [사실][^ref-1105] IEC 62443-3-3은 식별·인증 통제, 사용 통제, 시스템 무결성, 데이터 기밀성, 데이터 흐름 제한, 사건 적시 대응, 자원 가용성의 일곱 기본 요구와 SL1~SL4를 정의한다(IEC 소개 페이지 기준). [사실][^ref-1105]

CISA는 TUG 서버 취약점의 완화책으로 버전 갱신, 방화벽 뒤 격리, 원격 접속 시 VPN을 권고했다. [사실][^ref-1109] 이 가운데 망 조치는 ROP가 직접 하는 대책이 아니라 시설 IT/OT 쪽 연계 대상이다. [추정][^ref-1109]

### 대화·문서 입력 방어

OWASP LLM01:2025는 프롬프트 주입 완화책으로 출력 형식 정의·검증, 입출력 필터링, 최소 권한, 고위험 행동의 사람 승인, 외부 내용의 분리·표시, 적대적 시험 등을 들면서도 확실한 예방법은 아직 불분명하다고 밝힌다. [사실][^ref-1108]

RoboGuard는 보호된 신뢰 기반(root-of-trust) 언어 모델이 안전 규칙을 로봇 환경에 맞게 구체화하고, 시간 논리 제어 합성으로 위험할 수 있는 계획을 안전 명세에 맞추는 2단계 가드레일이다. [사실][^ref-700] 최악의 탈옥을 가정한 시뮬레이션·실물 실험에서 위험한 계획의 실행을 92% 이상에서 3% 미만으로 줄이고 안전한 계획의 성능은 유지했다고 보고했다. [사실][^ref-700]

Zhang 외는 GPT-4o 기반 이동 로봇 주행 시뮬레이션에서 보안 프롬프트와 응답 기반 탐지로 공격 탐지와 시스템 성능이 전체적으로 약 30.8% 개선됐다고 보고했다. [사실][^ref-1116] 두 결과 모두 연구 환경에서 나온 단일 출처 수치다. [사실][^ref-700][^ref-1116]

### 변조 탐지 감사 기록

ROS 2 위협 모델은 잘못된 메시지 이벤트를 기록하고 사용자에게 알리며 구성 변경도 기록하도록 권고한다. [사실][^ref-010] 업계 해설(IES, 2026-08-27 갱신)에 따르면 EU 기계류 규정 (EU) 2023/1230은 규정 준수에 결정적인 하드웨어·소프트웨어를 우발적·의도적 변조로부터 보호하고, 정당한·부당한 개입의 증거를 기록하며, 출시 후 올린 안전 소프트웨어 판의 추적 로그를 5년간 남기도록 요구한다(규정 원문을 열지 못해 조항 번호는 적지 않는다). [사실][^ref-1111] Fernández-Becerra 외는 ROS 기반 이동 로봇의 행동 기록을 블록체인으로 변조 방지하는 블랙박스형 요소와, 그 기록으로 언어 모델이 설명을 만드는 구조를 제안했다. [사실][^ref-1112]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md)
- 관련 영역: [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-009]: ROS 2 Design, ROS 2 DDS-Security Integration, 미확인, https://design.ros2.org/articles/ros2_dds_security.html, 접근일 2026-09-28
[^ref-010]: ROS 2 Design, ROS 2 Robotic Systems Threat Model, 미확인, https://design.ros2.org/articles/ros2_threat_model.html, 접근일 2026-09-28
[^ref-031]: VDA / VDMA (VDA5050 공식 저장소), VDA 5050 — Interface for the Communication between Mobile Robots and a Fleet Control (VDA5050_EN.md, 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-1105]: IEC (SyC Smart Energy), IEC 62443, 미확인, https://syc-se.iec.ch/deliveries/cybersecurity-guidelines/security-standards-and-best-practices/iec-62443/, 접근일 2026-09-30
[^ref-1108]: OWASP GenAI Security Project, LLM01:2025 Prompt Injection, 미확인, https://genai.owasp.org/llmrisk/llm01-prompt-injection/, 접근일 2026-09-30
[^ref-1109]: CISA (미국 사이버보안·기반시설보안청), Aethon TUG Home Base Server (ICSA-22-102-05), 2022-04-12, https://www.cisa.gov/news-events/ics-advisories/icsa-22-102-05, 접근일 2026-09-30
[^ref-1111]: IES (Integrated Equipment Services), Machinery Regulation Guide, 2026-08-27, https://www.ies.co.uk/reference-library/machinery-regulation-guide, 접근일 2026-09-30
[^ref-1112]: Fernández-Becerra, L., González-Santamarta, M. Á., Guerrero-Higueras, Á. M., Rodríguez-Lera, F. J., & Matellán Olivera, V. (arXiv), Enhancing Trust in Autonomous Agents: An Architecture for Accountability and Explainability through Blockchain and Large Language Models, 2024-03, https://arxiv.org/abs/2403.09567, 접근일 2026-09-30
[^ref-1116]: Zhang, W., Kong, X., Dewitt, C., Braunl, T., & Hong, J. B. (arXiv), A Study on Prompt Injection Attack Against LLM-Integrated Mobile Robotic Systems, 2024-08, https://arxiv.org/abs/2408.03515, 접근일 2026-09-30
[^ref-405]: Open Robotics (Programming Multiple Robots with ROS 2), Security, 미확인, https://osrf.github.io/ros2multirobotbook/security.html, 접근일 2026-09-30
[^ref-700]: Ravichandran, Z., Robey, A. 외 (arXiv), Safety Guardrails for LLM-Enabled Robots, 2025-03, https://arxiv.org/abs/2503.07885, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-11 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-11 | 52. 통신 보호·위협 관리·감사 의 "대표 접근법과 기술" 절에서 분리 |
````

### runs/2026-09-30-11/pages/topics/2026/2026-09-30-area52-s8.md

```markdown
---
title: "52. 통신 보호·위협 관리·감사 — 대표 연구와 자료"
type: topic
category: "N. 보안·개인정보"
primary_area_no: 52
related_areas: [12, 13, 20, 21, 22, 37, 38, 42, 44, 48, 50, 51, 53, 54, 57, 59, 62, 63, 65]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1109, ref-1110, ref-1112, ref-1115, ref-1116, ref-1119, ref-700, ref-857]
last_run: 2026-09-30
version: 1
split_from: docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md#8
---

[홈](../../index.md) › [주제](../index.md) › 52. 통신 보호·위협 관리·감사 — 대표 연구와 자료

# 52. 통신 보호·위협 관리·감사 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 대표 자료는 실제 취약점 공개와 로봇 분석, LLM 제어 로봇 공격, 방어·감사 기록 연구로 나뉜다. [의견]
- 이 페이지는 [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

대표 자료는 실제 취약점 공개와 로봇 분석, LLM 제어 로봇 공격, 방어·감사 기록 연구로 나뉜다. [의견]

- CISA, Aethon TUG Home Base Server(ICSA-22-102-05, 2022) — 병원 자율이동로봇 플릿 서버의 인가 누락·무인증 웹소켓 제어 취약점을 공개한 정부 권고로, 플릿 서버가 공격 경로가 되는 실제 사례다. [사실][^ref-1109]
- Quarta 외, An Experimental Security Analysis of an Industrial Robot Controller(2017) — 산업용 로봇 제어기의 소프트웨어 취약점과 구조적 결함이 제어 정확성과 작업자 안전 요구를 무너뜨릴 수 있음을 보였다(원문 미열람). [추정][^ref-1119]
- Mayoral-Vilches, The Cybersecurity of a Humanoid Robot(2025) — Unitree G1의 독자 이중 암호화가 정적 키를 써 구성 파일을 오프라인에서 복호화할 수 있고, 음성·영상·공간·구동기 상태 데이터가 사용자의 명시적 동의 없이 외부 서버로 간다고 보고했다. [사실][^ref-1110] 이는 로봇 제조사 쪽 연계 대상의 위협 근거로 보인다. [추정][^ref-1110]
- Robey 외, Jailbreaking LLM-Controlled Robots(2024) — RoboPAIR 공격이 화이트박스·그레이박스·블랙박스 세 설정에서 자주 100% 성공률을 보였다. [사실][^ref-857]
- Zhang 외, A Study on Prompt Injection Attack Against LLM-Integrated Mobile Robotic Systems(2024) — 다중 모달 프롬프트 주입이 잘못되거나 위험한 주행 명령을 낳을 수 있음을 보이고 방어 효과를 쟀다. [사실][^ref-1116]
- Nagaraja·Bagari·Bahsi, When Prompts Control Robots(2026) — 직접 주입과 인식 모듈을 거친 간접 주입이 작업 성공률을 낮추고 에이전트 사이로 번질 수 있음을 보였다. [사실][^ref-1115]
- Ravichandran 외, Safety Guardrails for LLM-Enabled Robots(2025 제출, 2026-03 개정) — RoboGuard 가드레일로 탈옥 아래 위험 계획 실행을 크게 줄였다. [사실][^ref-700]
- Fernández-Becerra 외, Enhancing Trust in Autonomous Agents(2024 제출, 2025-07 개정) — 블록체인 변조 방지 블랙박스형 기록과 언어 모델 설명을 세 주행 시나리오에서 평가했다. [사실][^ref-1112]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md)
- 관련 영역: [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1109]: CISA (미국 사이버보안·기반시설보안청), Aethon TUG Home Base Server (ICSA-22-102-05), 2022-04-12, https://www.cisa.gov/news-events/ics-advisories/icsa-22-102-05, 접근일 2026-09-30
[^ref-1110]: Mayoral-Vilches, V. (Alias Robotics, arXiv), The Cybersecurity of a Humanoid Robot, 2025-09-17, https://arxiv.org/abs/2509.14096, 접근일 2026-09-30
[^ref-1112]: Fernández-Becerra, L., González-Santamarta, M. Á., Guerrero-Higueras, Á. M., Rodríguez-Lera, F. J., & Matellán Olivera, V. (arXiv), Enhancing Trust in Autonomous Agents: An Architecture for Accountability and Explainability through Blockchain and Large Language Models, 2024-03, https://arxiv.org/abs/2403.09567, 접근일 2026-09-30
[^ref-1115]: Nagaraja, N., Bagari, A., & Bahsi, H. (arXiv), When Prompts Control Robots: Prompt Injection Attacks in Multi-Agent Robotic Systems, 2026-08, https://arxiv.org/abs/2608.00747, 접근일 2026-09-30
[^ref-1116]: Zhang, W., Kong, X., Dewitt, C., Braunl, T., & Hong, J. B. (arXiv), A Study on Prompt Injection Attack Against LLM-Integrated Mobile Robotic Systems, 2024-08, https://arxiv.org/abs/2408.03515, 접근일 2026-09-30
[^ref-1119]: Quarta, D., Pogliani, M., Polino, M., Maggi, F., Zanchettin, A. M., & Zanero, S. (IEEE S&P 2017), An Experimental Security Analysis of an Industrial Robot Controller, 2017, https://files01.core.ac.uk/download/pdf/84891817.pdf, 접근일 2026-09-30 (원문 미열람)
[^ref-700]: Ravichandran, Z., Robey, A. 외 (arXiv), Safety Guardrails for LLM-Enabled Robots, 2025-03, https://arxiv.org/abs/2503.07885, 접근일 2026-09-30
[^ref-857]: Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J. (arXiv), Jailbreaking LLM-Controlled Robots, 2024-10, https://arxiv.org/abs/2410.13691, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-11 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-11 | 52. 통신 보호·위협 관리·감사 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-30-11/pages/topics/2026/2026-09-30-area52-s10.md

```markdown
---
title: "52. 통신 보호·위협 관리·감사 — 다른 연구영역과의 연결"
type: topic
category: "N. 보안·개인정보"
primary_area_no: 52
related_areas: [12, 13, 20, 21, 22, 37, 38, 42, 44, 48, 50, 51, 53, 54, 57, 59, 62, 63, 65]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-009, ref-031, ref-1105, ref-1108, ref-1109, ref-1110, ref-1111, ref-1112, ref-1115, ref-1116, ref-1119, ref-405, ref-700, ref-857, ref-969]
last_run: 2026-09-30
version: 1
split_from: docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md#10
---

[홈](../../index.md) › [주제](../index.md) › 52. 통신 보호·위협 관리·감사 — 다른 연구영역과의 연결

# 52. 통신 보호·위협 관리·감사 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 권한·개인정보, 채팅 입력, 플릿 연동, 기록·관제, 언어 모델 계획, 안전, 수명주기, 규제, 현장 유형 영역과 이어진다. [추정][^ref-1109]
- 이 페이지는 [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 권한·개인정보, 채팅 입력, 플릿 연동, 기록·관제, 언어 모델 계획, 안전, 수명주기, 규제, 현장 유형 영역과 이어진다. [추정][^ref-1109]

- [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md) — 대시보드 사용자 인증·역할 기반 접근 통제와 플릿 서버 인가 누락은 명령 권한 통제와 직결된다. [추정][^ref-405]
- [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md) — 로봇의 영상·음성 원격 측정 전송과 로봇청소기 사진 열람 사례는 영상·개인정보 보호 문제다. [추정][^ref-1110]
- [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) — 대화 지시가 주입·탈옥 공격의 입구가 된다. [추정][^ref-1115]
- [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) — 프롬프트 주입 완화책과 사람 승인을 함께 다룬다. [추정][^ref-1108]
- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md) — 제조사 플릿 서버 연결이 공격 경로가 될 수 있다. [추정][^ref-1109]
- [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md) — VDA 5050이 통신 보안을 브로커 구성에 맡긴다. [추정][^ref-031]
- [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) — 현장 망의 구역·도관 설계와 맞물린다. [추정][^ref-1105]
- [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) — 명령·승인 감사 기록의 저장과 조회로 이어진다. [추정][^ref-1112]
- [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) — IEC 62443의 사건 적시 대응 요구와 이어진다. [추정][^ref-1105]
- [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md) — DDS·SROS 2 통신 구조 위에서 보안을 설정한다. [추정][^ref-009]
- [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) — 언어 모델 계획의 탈옥과 가드레일을 공유한다. [추정][^ref-700]
- [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md) — 탈옥이 해로운 물리 행동으로 이어질 수 있다. [추정][^ref-857]
- [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) — 개입 증거 기록과 블랙박스형 기록은 사고 조사의 근거가 된다. [추정][^ref-1111]
- [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md) — 방어 효과를 재는 시뮬레이션·실물 시험과 이어진다. [추정][^ref-1116]
- [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) — 취약점 패치와 안전 소프트웨어 판 추적이 겹친다. [추정][^ref-1109]
- [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) — EU 기계류 규정과 국내 로봇 보안 해설서를 다룬다. [추정][^ref-1111]
- [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md) — 산업용 로봇 제어기 보안 분석 사례가 있다. [추정][^ref-1119]
- [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) — 병원 자율이동로봇 플릿 서버 권고 사례가 있다. [추정][^ref-1109]
- [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md) — 로봇청소기 보안 점검 사례가 있다. [추정][^ref-969]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md)
- 관련 영역: [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-009]: ROS 2 Design, ROS 2 DDS-Security Integration, 미확인, https://design.ros2.org/articles/ros2_dds_security.html, 접근일 2026-09-28
[^ref-031]: VDA / VDMA (VDA5050 공식 저장소), VDA 5050 — Interface for the Communication between Mobile Robots and a Fleet Control (VDA5050_EN.md, 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-1105]: IEC (SyC Smart Energy), IEC 62443, 미확인, https://syc-se.iec.ch/deliveries/cybersecurity-guidelines/security-standards-and-best-practices/iec-62443/, 접근일 2026-09-30
[^ref-1108]: OWASP GenAI Security Project, LLM01:2025 Prompt Injection, 미확인, https://genai.owasp.org/llmrisk/llm01-prompt-injection/, 접근일 2026-09-30
[^ref-1109]: CISA (미국 사이버보안·기반시설보안청), Aethon TUG Home Base Server (ICSA-22-102-05), 2022-04-12, https://www.cisa.gov/news-events/ics-advisories/icsa-22-102-05, 접근일 2026-09-30
[^ref-1110]: Mayoral-Vilches, V. (Alias Robotics, arXiv), The Cybersecurity of a Humanoid Robot, 2025-09-17, https://arxiv.org/abs/2509.14096, 접근일 2026-09-30
[^ref-1111]: IES (Integrated Equipment Services), Machinery Regulation Guide, 2026-08-27, https://www.ies.co.uk/reference-library/machinery-regulation-guide, 접근일 2026-09-30
[^ref-1112]: Fernández-Becerra, L., González-Santamarta, M. Á., Guerrero-Higueras, Á. M., Rodríguez-Lera, F. J., & Matellán Olivera, V. (arXiv), Enhancing Trust in Autonomous Agents: An Architecture for Accountability and Explainability through Blockchain and Large Language Models, 2024-03, https://arxiv.org/abs/2403.09567, 접근일 2026-09-30
[^ref-1115]: Nagaraja, N., Bagari, A., & Bahsi, H. (arXiv), When Prompts Control Robots: Prompt Injection Attacks in Multi-Agent Robotic Systems, 2026-08, https://arxiv.org/abs/2608.00747, 접근일 2026-09-30
[^ref-1116]: Zhang, W., Kong, X., Dewitt, C., Braunl, T., & Hong, J. B. (arXiv), A Study on Prompt Injection Attack Against LLM-Integrated Mobile Robotic Systems, 2024-08, https://arxiv.org/abs/2408.03515, 접근일 2026-09-30
[^ref-1119]: Quarta, D., Pogliani, M., Polino, M., Maggi, F., Zanchettin, A. M., & Zanero, S. (IEEE S&P 2017), An Experimental Security Analysis of an Industrial Robot Controller, 2017, https://files01.core.ac.uk/download/pdf/84891817.pdf, 접근일 2026-09-30 (원문 미열람)
[^ref-405]: Open Robotics (Programming Multiple Robots with ROS 2), Security, 미확인, https://osrf.github.io/ros2multirobotbook/security.html, 접근일 2026-09-30
[^ref-700]: Ravichandran, Z., Robey, A. 외 (arXiv), Safety Guardrails for LLM-Enabled Robots, 2025-03, https://arxiv.org/abs/2503.07885, 접근일 2026-09-30
[^ref-857]: Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J. (arXiv), Jailbreaking LLM-Controlled Robots, 2024-10, https://arxiv.org/abs/2410.13691, 접근일 2026-09-30
[^ref-969]: 바이라인네트워크 (곽중희), ‘로봇청소기’ 다수 제품 보안 취약…대응방안은?, 2025-10-31, https://byline.network/2025/10/31-283/, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-11 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-11 | 52. 통신 보호·위협 관리·감사 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-30-11/pages/topics/2026/2026-09-30-area52-s3.md

```markdown
---
title: "52. 통신 보호·위협 관리·감사 — 왜 중요한가"
type: topic
category: "N. 보안·개인정보"
primary_area_no: 52
related_areas: [12, 13, 20, 21, 22, 37, 38, 42, 44, 48, 50, 51, 53, 54, 57, 59, 62, 63, 65]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-009, ref-031, ref-1108, ref-1109, ref-1111, ref-1114, ref-1115, ref-700, ref-857]
last_run: 2026-09-30
version: 1
split_from: docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md#3
---

[홈](../../index.md) › [주제](../index.md) › 52. 통신 보호·위협 관리·감사 — 왜 중요한가

# 52. 통신 보호·위협 관리·감사 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- ROP는 여러 제조사의 플릿 관리 서버·브로커·로봇을 한곳에 잇기 때문에, 그 연결 가운데 하나가 뚫리면 공격이 곧 로봇 동작으로 이어질 수 있다. [추정][^ref-1109][^ref-031]
- 이 페이지는 [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

ROP는 여러 제조사의 플릿 관리 서버·브로커·로봇을 한곳에 잇기 때문에, 그 연결 가운데 하나가 뚫리면 공격이 곧 로봇 동작으로 이어질 수 있다. [추정][^ref-1109][^ref-031]

2022-04-12 미국 사이버보안·기반시설보안청(Cybersecurity and Infrastructure Security Agency, CISA)은 병원 자율이동로봇을 제어·통신하는 플릿 서버에서 인증 없이 웹소켓에 접속해 로봇을 제어할 수 있는 취약점을 공개했다. [사실][^ref-1109] 이 사례는 플릿 서버 취약점이 로봇 기능 전면 제어로 이어질 수 있음을 보여 준다. [추정][^ref-1109] 게다가 플릿 관제–이동 로봇 통신 규격 VDA 5050 3.0.0은 프로토콜 보안을 브로커 구성에 맡기므로, 여러 제조사를 잇는 쪽이 통신 보호를 따로 챙겨야 하는 것으로 보인다. [추정][^ref-031]

채팅·문서 입력은 새 공격 경로를 더한다. 연구 환경에서는 언어 모델(Large Language Model, LLM)로 제어하는 로봇을 탈옥해 해로운 물리 행동을 끌어내는 공격이 자주 100% 성공률을 보였다. [사실][^ref-857] 다중 에이전트 로봇 시스템에서는 주입된 지시가 공유 프롬프트 구조를 타고 다른 에이전트로 번질 수 있음이 보고됐다. [사실][^ref-1115]

규제도 기록과 변조 방지를 요구하는 쪽으로 움직인다. 업계 해설(IES, 2026-08-27 갱신)에 따르면 EU 기계류 규정은 2027-01-20부터 전면 적용되며, 규정 준수에 결정적인 하드웨어·소프트웨어의 변조 보호와, 기계가 안전 관련 소프트웨어를 식별하고 개입 증거를 기록하는 것을 요구한다. [사실][^ref-1111] 국내에서는 과학기술정보통신부와 한국인터넷진흥원(KISA)이 2026년 3월 로봇 분야 보안모델 고도화판과 사이버보안 요구사항 해설서를 제품 개발·수출 때 참고할 자료로 배포했다. [사실][^ref-1114]

지금까지의 자료로 핵심 질문에 답하면, 통신 인증·암호화 수단은 있으나 상호운용 규격은 보안을 운영 쪽에 맡기고, 언어 모델 층은 연구 환경에서 높은 공격 성공률이 보고됐으며, 언어 모델 밖에서 계획을 규칙으로 검사하는 방어가 위험한 계획의 실행을 크게 줄이지만 확실한 차단법은 아직 불분명하다. [추정][^ref-009][^ref-031][^ref-857][^ref-700][^ref-1108] 그래서 통신 인증, 권한 분리, 실행 전 규칙 검사, 사람 승인, 변조 탐지 감사 기록을 겹쳐 두는 다층 방어가 필요한 것으로 보인다. [추정][^ref-700][^ref-1108]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md)
- 관련 영역: [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-009]: ROS 2 Design, ROS 2 DDS-Security Integration, 미확인, https://design.ros2.org/articles/ros2_dds_security.html, 접근일 2026-09-28
[^ref-031]: VDA / VDMA (VDA5050 공식 저장소), VDA 5050 — Interface for the Communication between Mobile Robots and a Fleet Control (VDA5050_EN.md, 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-1108]: OWASP GenAI Security Project, LLM01:2025 Prompt Injection, 미확인, https://genai.owasp.org/llmrisk/llm01-prompt-injection/, 접근일 2026-09-30
[^ref-1109]: CISA (미국 사이버보안·기반시설보안청), Aethon TUG Home Base Server (ICSA-22-102-05), 2022-04-12, https://www.cisa.gov/news-events/ics-advisories/icsa-22-102-05, 접근일 2026-09-30
[^ref-1111]: IES (Integrated Equipment Services), Machinery Regulation Guide, 2026-08-27, https://www.ies.co.uk/reference-library/machinery-regulation-guide, 접근일 2026-09-30
[^ref-1114]: 엠에스투데이, 선박·위성·로봇까지 해킹 표적…정부, ‘피지컬 AI’ 산업 보안 기준 제시, 2026-03-06, https://www.mstoday.co.kr/news/articleView.html?idxno=100755, 접근일 2026-09-30
[^ref-1115]: Nagaraja, N., Bagari, A., & Bahsi, H. (arXiv), When Prompts Control Robots: Prompt Injection Attacks in Multi-Agent Robotic Systems, 2026-08, https://arxiv.org/abs/2608.00747, 접근일 2026-09-30
[^ref-700]: Ravichandran, Z., Robey, A. 외 (arXiv), Safety Guardrails for LLM-Enabled Robots, 2025-03, https://arxiv.org/abs/2503.07885, 접근일 2026-09-30
[^ref-857]: Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J. (arXiv), Jailbreaking LLM-Controlled Robots, 2024-10, https://arxiv.org/abs/2410.13691, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-11 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-11 | 52. 통신 보호·위협 관리·감사 의 "왜 중요한가" 절에서 분리 |
```

### runs/2026-09-30-11/pages/topics/2026/2026-09-30-area52-s11.md

```markdown
---
title: "52. 통신 보호·위협 관리·감사 — 열린 질문"
type: topic
category: "N. 보안·개인정보"
primary_area_no: 52
related_areas: [12, 13, 20, 21, 22, 37, 38, 42, 44, 48, 50, 51, 53, 54, 57, 59, 62, 63, 65]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-031, ref-1111, ref-1112, ref-1114, ref-1115, ref-1116, ref-700]
last_run: 2026-09-30
version: 1
split_from: docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md#11
---

[홈](../../index.md) › [주제](../index.md) › 52. 통신 보호·위협 관리·감사 — 열린 질문

# 52. 통신 보호·위협 관리·감사 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 대화 지시 방어의 현장 효과, 브로커 보안 프로파일, 감사 기록의 규모별 비용과 규제 적용 범위가 아직 열려 있다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

대화 지시 방어의 현장 효과, 브로커 보안 프로파일, 감사 기록의 규모별 비용과 규제 적용 범위가 아직 열려 있다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- **oq-144** (상태: 열림) 로봇 대화 지시에 특화된 프롬프트 주입·탈옥 방어(도구 설명 신뢰 경계, 실행 전 물리 제약 검사, 다중 모델 감독)의 효과를 잰 공개 벤치마크나 현장 시험 결과가 있는가? 이번 조사에서는 RoboGuard의 시뮬레이션·실험실 수준 결과[^ref-700]와 GPT-4o 통합 이동 로봇의 시뮬레이션 방어 결과[^ref-1116]를 부분 근거로 찾았으나, 현장 시험 결과가 없어 해결로 보지 않는다.
- (새 질문 · 상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-11) 여러 제조사 플릿 관리 서버와 VDA 5050 브로커·Open-RMF 어댑터를 잇는 ROP에서 브로커·API의 상호 인증과 TLS 설정의 최소 요구를 정한 공개 보안 프로파일이 있는가?[^ref-031]
- (새 질문 · 상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-11) LLM 에이전트 여러 개가 로봇을 나눠 맡을 때 한 에이전트에 주입된 지시가 다른 에이전트로 퍼지지 않게 에이전트 간 메시지에 신뢰 경계를 두는 방어의 효과를 잰 연구가 있는가?[^ref-1115]
- (새 질문 · 상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-11) 명령·승인 감사 기록을 해시 체인·블록체인으로 변조 탐지 가능하게 남길 때 수백 대 로봇 규모의 명령 빈도에서 지연·저장 비용을 측정한 자료가 있는가?[^ref-1112]
- (새 질문 · 상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-11) EU 기계류 규정의 개입 증거 기록·안전 소프트웨어 추적 로그 요구가 개별 기계 밖에서 여러 로봇을 지시하는 오케스트레이션 플랫폼에도 미치는가, 미친다면 기록 책임은 누구에게 있는가?[^ref-1111]
- (새 질문 · 상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-11) KISA 로봇 보안모델(고도화)과 사이버보안 요구사항 해설서는 로봇 통신 암호화·감사 기록·원격 업데이트에 어떤 요구 항목을 두며 다중 로봇 관제 플랫폼을 대상에 포함하는가?[^ref-1114]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md)
- 관련 영역: [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-031]: VDA / VDMA (VDA5050 공식 저장소), VDA 5050 — Interface for the Communication between Mobile Robots and a Fleet Control (VDA5050_EN.md, 3.0.0), 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-1111]: IES (Integrated Equipment Services), Machinery Regulation Guide, 2026-08-27, https://www.ies.co.uk/reference-library/machinery-regulation-guide, 접근일 2026-09-30
[^ref-1112]: Fernández-Becerra, L., González-Santamarta, M. Á., Guerrero-Higueras, Á. M., Rodríguez-Lera, F. J., & Matellán Olivera, V. (arXiv), Enhancing Trust in Autonomous Agents: An Architecture for Accountability and Explainability through Blockchain and Large Language Models, 2024-03, https://arxiv.org/abs/2403.09567, 접근일 2026-09-30
[^ref-1114]: 엠에스투데이, 선박·위성·로봇까지 해킹 표적…정부, ‘피지컬 AI’ 산업 보안 기준 제시, 2026-03-06, https://www.mstoday.co.kr/news/articleView.html?idxno=100755, 접근일 2026-09-30
[^ref-1115]: Nagaraja, N., Bagari, A., & Bahsi, H. (arXiv), When Prompts Control Robots: Prompt Injection Attacks in Multi-Agent Robotic Systems, 2026-08, https://arxiv.org/abs/2608.00747, 접근일 2026-09-30
[^ref-1116]: Zhang, W., Kong, X., Dewitt, C., Braunl, T., & Hong, J. B. (arXiv), A Study on Prompt Injection Attack Against LLM-Integrated Mobile Robotic Systems, 2024-08, https://arxiv.org/abs/2408.03515, 접근일 2026-09-30
[^ref-700]: Ravichandran, Z., Robey, A. 외 (arXiv), Safety Guardrails for LLM-Enabled Robots, 2025-03, https://arxiv.org/abs/2503.07885, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-11 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-11 | 52. 통신 보호·위협 관리·감사 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-30-11/pages/topics/2026/2026-09-30-area52-s4.md

```markdown
---
title: "52. 통신 보호·위협 관리·감사 — 핵심 개념과 용어"
type: topic
category: "N. 보안·개인정보"
primary_area_no: 52
related_areas: [12, 13, 20, 21, 22, 37, 38, 42, 44, 48, 50, 51, 53, 54, 57, 59, 62, 63, 65]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-009, ref-010, ref-1105, ref-1108, ref-1112, ref-857]
last_run: 2026-09-30
version: 1
split_from: docs/categories/security-and-privacy/communication-protection-threat-management-and-audit.md#4
---

[홈](../../index.md) › [주제](../index.md) › 52. 통신 보호·위협 관리·감사 — 핵심 개념과 용어

# 52. 통신 보호·위협 관리·감사 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 용어는 통신 보호, 위협 관리, 입력 보안, 감사 기록의 네 갈래로 나눠 보면 이해하기 쉽다. [의견]
- 이 페이지는 [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 용어는 통신 보호, 위협 관리, 입력 보안, 감사 기록의 네 갈래로 나눠 보면 이해하기 쉽다. [의견]

- **STRIDE 위협 분류(STRIDE)** — 위조(Spoofing)·변조(Tampering)·부인(Repudiation)·정보 노출(Information Disclosure)·서비스 거부(Denial of Service)·권한 상승(Elevation of Privilege)의 여섯 범주로 위협을 분류하는 방법이다. ROS 2 위협 모델은 이 분류로 로봇 시스템 위협을 정리하고 DREAD로 위험을 평가한다. [사실][^ref-010]
- **[DDS 보안 규격](../../glossary/dds-security.md)(DDS-Security)과 SROS 2** — DDS-Security는 인증·접근 통제·암호·로깅·데이터 태깅의 다섯 플러그인 인터페이스를 두며, ROS 2의 보안 도구 SROS 2는 앞의 셋만 쓴다. [사실][^ref-009]
- **[인클레이브](../../glossary/enclave.md)(Enclave)** — SROS 2 키 저장소의 enclaves 아래에 인증서·키·governance·permissions 파일을 묶어 두는 보안 단위다. [사실][^ref-009]
- **[보안 구역과 도관](../../glossary/zones-and-conduits.md)(Zones and Conduits)과 보안 수준(Security Level, SL)** — IEC 62443은 위험 기준으로 자산을 묶은 구역과 구역 사이 통신인 도관을 두고, 공격자 역량에 맞춘 SL1~SL4를 일곱 기본 요구별 벡터로 표현할 수 있게 한다. [사실][^ref-1105]
- **[프롬프트 주입](../../glossary/prompt-injection.md)(Prompt Injection)** — 사용자 입력이 모델 행동을 바꾸는 직접 주입과, 웹 페이지·파일 같은 외부 내용에 숨은 지시가 행동을 바꾸는 간접 주입(Indirect Prompt Injection)으로 나뉜다. [사실][^ref-1108] LLM 제어 로봇을 [탈옥](../../glossary/jailbreak.md)(Jailbreak)해 해로운 물리 행동을 끌어내는 공격도 연구됐다. [사실][^ref-857]
- **[감사 추적](../../glossary/audit-trail.md)(Audit Trail)과 변조 탐지 로그(Tamper-evident Log)** — ROS 2 위협 모델은 잘못된 메시지 이벤트와 구성 변경을 기록하도록 권고한다. [사실][^ref-010] 블록체인 같은 수단으로 기록이 고쳐지면 드러나게 하는 변조 방지 기록 구조도 제안됐다. [사실][^ref-1112]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md)
- 관련 영역: [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-009]: ROS 2 Design, ROS 2 DDS-Security Integration, 미확인, https://design.ros2.org/articles/ros2_dds_security.html, 접근일 2026-09-28
[^ref-010]: ROS 2 Design, ROS 2 Robotic Systems Threat Model, 미확인, https://design.ros2.org/articles/ros2_threat_model.html, 접근일 2026-09-28
[^ref-1105]: IEC (SyC Smart Energy), IEC 62443, 미확인, https://syc-se.iec.ch/deliveries/cybersecurity-guidelines/security-standards-and-best-practices/iec-62443/, 접근일 2026-09-30
[^ref-1108]: OWASP GenAI Security Project, LLM01:2025 Prompt Injection, 미확인, https://genai.owasp.org/llmrisk/llm01-prompt-injection/, 접근일 2026-09-30
[^ref-1112]: Fernández-Becerra, L., González-Santamarta, M. Á., Guerrero-Higueras, Á. M., Rodríguez-Lera, F. J., & Matellán Olivera, V. (arXiv), Enhancing Trust in Autonomous Agents: An Architecture for Accountability and Explainability through Blockchain and Large Language Models, 2024-03, https://arxiv.org/abs/2403.09567, 접근일 2026-09-30
[^ref-857]: Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J. (arXiv), Jailbreaking LLM-Controlled Robots, 2024-10, https://arxiv.org/abs/2410.13691, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-11 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-11 | 52. 통신 보호·위협 관리·감사 의 "핵심 개념과 용어" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 1103건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 306개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- event-driven-rescheduling: 사건 기반 재스케줄링 (Event-driven Rescheduling)
- event-trace: 사건 트레이스 (Event Trace)
- excessive-agency: 과도한 에이전시 (Excessive Agency)
- expected-value-of-perfect-information: 완전 정보의 기대 가치 (Expected Value of Perfect Information (EVPI))
- explainable-mapf: 설명 가능한 다중 에이전트 경로 찾기 (Explainable Multi-Agent Path Finding (Explainable MAPF))
- explicit-implicit-confirmation: 명시적 확인·암시적 확인 (Explicit / Implicit Confirmation)
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
- hddl: 계층 도메인 정의 언어 (Hierarchical Domain Definition Language (HDDL))
- hierarchical-task-network: 계층적 작업 네트워크 (Hierarchical Task Network (HTN))
- high-impact-ai: 고영향 인공지능 (High-impact AI (Korea AI Basic Act))
- hmi-philosophy: HMI 철학 (HMI Philosophy (ISA-TR101.01))
- human-in-the-loop: 사람 참여 루프 (Human-in-the-Loop (HITL))
- hungarian-method: 헝가리안 방법 (Hungarian Method)
- idempotency-key: 멱등성 키 (Idempotency Key)
- identity-report: 신원 보고 (Identity Report (MassRobotics identityReport))
- iec-common-data-dictionary: IEC 공통 데이터 사전 (IEC Common Data Dictionary (IEC CDD))
- ifc: 산업 기초 클래스 (Industry Foundation Classes (IFC))
- imitation-learning: 모방 학습 (Imitation Learning)
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
- lifelong-mapf: 지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF))
- lift-adapter: 승강기 어댑터 (Lift Adapter)
- linear-temporal-logic: 선형 시간 논리 (Linear Temporal Logic (LTL))
- littles-law: 리틀의 법칙 (Little's Law)
- llm-agent: LLM 에이전트 (LLM Agent)
- llm-modulo-framework: LLM-모듈로 프레임워크 (LLM-Modulo Framework)
- location-check-digit: 위치 체크 디지트 (Location Check Digit)
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
- model-registry: 모델 레지스트리 (Model Registry)
- model-substitution-and-routing-dilution: 모델 대체·라우팅 희석 (Model Substitution / Routing Dilution)
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
- pddl: 계획 도메인 정의 언어 (Planning Domain Definition Language (PDDL))
- perfect-order-fulfillment: 완전 주문 이행률 (Perfect Order Fulfillment)
- performable-action: 수행 가능 동작 (Performable Action (Open-RMF perform_action))
- personal-delivery-device: 개인 배송 장치 (Personal Delivery Device (PDD))
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- post-encroachment-time: 침범 후 시간 (Post-Encroachment Time (PET))
- power-and-force-limiting: 동력·힘 제한 (Power and Force Limiting (PFL))
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- predictive-maintenance: 예지 정비 (Predictive Maintenance)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- prompt-injection: 프롬프트 주입 (Prompt Injection)
- protective-separation-distance: 보호 분리 거리 (Protective Separation Distance)
- public-area-mobile-robot: 공공 영역 이동로봇 (Public-area Mobile Robot (PMR))
- put-wall: 풋월 (Put Wall)
- raster-to-vector-conversion: 래스터–벡터 변환 (Raster-to-Vector Conversion)
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
- self-driving-laboratory: 자율 실험실 (Self-driving Laboratory (Autonomous Laboratory))
- semantic-id: 의미 식별자 (Semantic ID (semanticId))
- semantic-map: 의미 지도 (Semantic Map)
- semantic-versioning: 의미적 버전 관리 (Semantic Versioning (SemVer))
- semi-open-queueing-network: 반개방형 대기행렬 네트워크 (Semi-Open Queueing Network (SOQN))
- semi-static-object: 반정적 객체 (Semi-static Object)
- service-level-agreement: 서비스 수준 협약 (Service Level Agreement (SLA))
- service-triad: 서비스 삼자 관계 (Service Triad (service robot, customer, frontline employee))
- shacl: 형상 제약 언어 (Shapes Constraint Language (SHACL))
- shifting-bottleneck-detection-active-period-method: 이동 병목 탐지 (Shifting Bottleneck Detection (Active Period Method))
- shuttle-based-storage-and-retrieval-system: 셔틀 기반 저장·회수 시스템 (Shuttle-Based Storage and Retrieval System (SBS/RS))
- signal-temporal-logic: 신호 시간 논리 (Signal Temporal Logic (STL))
- sila-2: SiLA 2 (Standardization in Lab Automation 2 (SiLA 2))
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
- software-nameplate: 소프트웨어 명판 (Software Nameplate (IDTA 02007))
- source-grounding: 출처 근거 연결 (Source Grounding)
- space-boundary: 공간 경계 (Space Boundary (IfcRelSpaceBoundary))
- space-graph: 공간 그래프 (Space Graph)
- speed-and-separation-monitoring: 속도·분리 감시 (Speed and Separation Monitoring (SSM))
- sscc: 물류 단위 일련 코드 (Serial Shipping Container Code (SSCC))
- state-of-charge: 충전 상태 (State of Charge (SOC))
- state-of-health: 배터리 건강 상태 (State of Health (SOH))
- stpa: 시스템 이론적 프로세스 분석 (System-Theoretic Process Analysis (STPA))
- structured-output: 구조화 출력 (Structured Output)
- success-weighted-by-path-length: 경로 길이 가중 성공률 (Success weighted by Path Length (SPL))
- supervisory-control: 감독 제어 (Supervisory Control)
- table-structure-recognition: 표 구조 인식 (Table Structure Recognition)
- task-decomposition: 작업 분해 (Task Decomposition)
- technology-readiness-level: 기술 성숙도 (Technology Readiness Level (TRL))
- teleoperation: 원격 조작 (Teleoperation)
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
- vision-language-action-model: 비전 언어 행동 모델 (Vision-Language-Action Model (VLA))
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking))
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release)
- webhook: 웹훅 (Webhook)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [52] 에 걸린 1건 / 전체 240건)

```markdown
- oq-144 [열림] 로봇 대화 지시에 특화된 프롬프트 주입·탈옥 방어(도구 설명 신뢰 경계, 실행 전 물리 제약 검사, 다중 모델 감독)의 효과를 잰 공개 벤치마크나 현장 시험 결과가 있는가? (영역 13, 52, 48)
```

### runs/2026-09-30-11/verification2.json

```json
{
  "run_id": "2026-09-30-11",
  "stage": "second",
  "verdict": "수정 후 재검증",
  "claim_checks": [
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "강등은 5절 제조 공장 표와 8절 Quarta 외 항목에 반영됐다. 다만 5절 첫 요약 문장('이 영역의 실제 사례는 병원…, 가정…, 제조 공장의 산업용 로봇 제어기 분석에서 확인된다. [사실][^ref-1109]')이 강등된 이 사례를 [사실]과 ref-1109 하나로 묶어 다시 올려 쓴다. 8절 요약 문장('…실제 취약점 공개와 로봇 분석…으로 나뉜다. [사실]')도 같은 문제다. 수정 지시 1·2를 본다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": true,
      "tag_decision": "강등",
      "note": "5절 가정 표에서 '통신 암호화 부족'은 빠졌고 [추정] 강등도 이행됐다. 그러나 5절 첫 요약 문장이 이 사례를 [사실][^ref-1109]로 함께 묶고 있다. ref-969 각주도 없다. 수정 지시 1을 본다."
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
      "참고문헌 id 충돌 가능성이 아직 풀리지 않았다. 이번 페이지가 쓰는 ref-1105~ref-1119, ref-857, ref-700, ref-969, ref-031, ref-405 는 전체 1085건 목록 안의 번호대이고, 1차 검증은 실행 2026-09-30-09 브리프가 이 가운데 일부(예: ref-1105, ref-1109, ref-031)를 다른 출처에 썼다고 지적했다. reference_updates 가 기존 참고문헌 기록을 덮어쓰거나 각주가 다른 출처 페이지를 가리킬 수 있다. 퍼블리셔가 URL 대조로 확인한 뒤 게시해야 한다.",
      "ref-031(VDA 5050 3.0.0)은 실행 2026-09-30-10 의 ref-1079 와 URL 이 같다. 병합할 때는 3.0.0 원문 제목 'Interface for the Communication between Mobile Robots and a Fleet Control'을 기준으로 삼는다.",
      "ref-009·ref-010: 13절 각주 정의는 기존 참고문헌 형식 줄(ROS 2 Design, 접근일 2026-09-28)을 따른다. 반면 reference_updates 는 기관 'Open Robotics (ROS 2 Design, …)'·접근일 2026-09-30 을 적어 서로 다르다. 퍼블리셔는 기존 기록을 유지하는 쪽으로 합친다."
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
    "5절 첫 문장('이 영역의 실제 사례는 병원의 플릿 서버 취약점 공개, 가정의 로봇청소기 보안 점검, 제조 공장의 산업용 로봇 제어기 분석에서 확인된다. [사실][^ref-1109]'): 태그를 [추정]으로 바꾸고 각주를 [^ref-1109][^ref-969][^ref-1119]로 늘린다. 이 문장은 1차에서 [추정]으로 강등한 f10·f12 사례를 [사실]로 묶고, 세 사례를 ref-1109 하나로만 뒷받침한다.",
    "8절 첫 문장('대표 자료는 실제 취약점 공개와 로봇 분석, LLM 제어 로봇 공격, 방어·감사 기록 연구로 나뉜다. [사실][^ref-1109][^ref-857]'): 태그를 4절 첫 문장처럼 [의견]으로 바꾸고 각주를 뗀다. 스토리텔러가 자료를 묶은 분류이고, 강등된 f10(Quarta 외)을 포함하므로 [사실]로 올릴 수 없다. 분리 페이지 2026-09-30-area52-s8.md 의 세 줄 요약과 본문 첫 문장에도 같이 반영된다.",
    "6절 첫 단락의 마지막 문장 '아래 도식은 이번 자료를 종합한 다층 방어의 추정 구조다.'를 첫 단락에서 떼어 mermaid 블록 바로 앞의 별도 단락으로 옮긴다. 분량 자동 분리 뒤 세부영역 페이지 6절에는 첫 단락만 남고 도식은 주제 페이지로 가므로, 지금은 세부영역 페이지에 없는 도식을 가리키는 문장이 남는다.",
    "6절 '위협 모델과 취약점 관리' 소절의 태그 없는 일반화 문장 '공개된 취약점에는 갱신과 망 격리로 대응한다.'를 지우거나, 다음 문장과 합쳐 'CISA는 TUG 서버 취약점의 완화책으로 …을 권고했다. [사실][^ref-1109]'처럼 이 사례 하나에 한정해 쓴다. 근거는 권고 한 건(f9)뿐이어서 일반 원칙으로 서술할 수 없고, 태그도 없다.",
    "3절 셋째 단락 'EU 기계류 규정은 2027-01-20부터 전면 적용되며 안전 관련 소프트웨어의 변조 보호와 개입 증거 기록을 요구한다.'를 f19 범위에 맞춰 '규정 준수에 결정적인 하드웨어·소프트웨어의 변조 보호와, 기계가 안전 관련 소프트웨어를 식별하고 개입 증거를 기록하는 것을 요구한다'로 고친다. f19 는 변조 보호 대상을 '규정 준수에 결정적인 하드웨어·소프트웨어'로 적으며, 안전 관련 소프트웨어로 좁히지 않는다.",
    "5절 병원 표 '제약' 칸 괄호 '(망 조치는 시설 IT/OT 쪽 연계 대상)'와, 8절 Mayoral-Vilches 항목 끝 문장 '제조사 쪽 연계 대상의 위협 근거다.'는 [사실] 태그 안에 든 해석(f24, 추정)이다. 각각 따로 떼어 '… [사실][^ref-1109] 이 가운데 망 조치는 시설 IT/OT 쪽 연계 대상이다. [추정][^ref-1109]', '… [사실][^ref-1110] 이는 로봇 제조사 쪽 연계 대상의 위협 근거로 보인다. [추정][^ref-1110]'처럼 태그를 나눈다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 1차 조건부 승인 / 2차 수정 후 재검증. 확인 23건, 미확인 2건, 교차 확인 2건. 강등: f10 사실 → 추정(원문 미열람이고, 검색 결과 요약에 '원격 완전 장악·펌웨어 백도어·인증 우회'가 없음), f12 사실 → 추정('통신 암호화 부족'이 출처에 없음). 원문 미열람 출처: ref-1119(Quarta 외). 주의: 사실 주장의 대부분은 단일 출처(정부 권고·오픈소스 설계 문서·arXiv 초록)이고, 교차 확인은 EU 기계류 규정 요구(f19, 업계 해설 기준)와 KISA·한국소비자원 로봇청소기 점검 개요(f12) 두 건뿐이다. LLM 탈옥·주입 공격과 방어 수치(f14·f15·f17)는 연구·시뮬레이션 환경의 결과다. 3절(왜 중요한가)과 9절(책임 경계)은 추정 종합이다. ROS 2 위협 모델(ref-010)은 원문에 초안(DRAFT)으로 표시돼 있다. 13. 대화형 기능의 신뢰·기반 페이지는 이번 실행에서 갱신하지 않았고 다음 실행 후보로 넘겼다. oq-144 는 해결로 인정하지 않는다(부분 근거 f15·f17). 정정 요청 없음. / 2차 수정 후 재검증. 1차 수정 지시 15건은 모두 이행됐다. 다만 지적 사항 6건이 남았다: 요약 문장 두 곳(5절·8절)이 태그를 [사실]로 올렸고, 6절에 태그 없는 일반화 문장 1건, 3절에 EU 규정의 변조 보호 대상을 좁힌 서술 1건, 분리 뒤 도식 없이 남은 '아래 도식' 문장 1건, 연계 대상 해석이 [사실] 태그 안에 섞인 곳 2곳이 있다. [분류원문] 보존(소속 대분류 블록·1절·2절이 시드와 같음), 섹션 순서 준수, 링크 유효(형식 검증 코드 결과 기준, docs_tree 미입력), site_matrix_updates 9칸은 5절 표와 일치한다. 퍼블리셔 확인 사항: 참고문헌 id(ref-1105~ref-1119, ref-857, ref-700, ref-969, ref-031, ref-405)가 기존 목록·실행 2026-09-30-09 와 충돌할 수 있고, ref-031 은 실행 2026-09-30-10 의 ref-1079 와 URL 이 같다. 자동 분리로 생긴 주제 페이지 6건의 9. 검증 노트는 '1차·2차 검증을 거쳤다'로 적혀 있어 2차 통과 전에는 사실과 다르다. 분리 코드 담당에게 확인을 요청한다. 2차 검증은 도구를 쓰지 않았다.",
  "retry_reason": null
}
```
