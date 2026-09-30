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
- verification_stage: first
- verifier_budget:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
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
        "ref-1118"
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
        "ref-1118"
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
        "ref-1117"
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
        "ref-1113"
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
        "ref-1106"
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
        "ref-1107"
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
        "ref-1118",
        "ref-1117",
        "ref-1109",
        "ref-1119",
        "ref-1106",
        "ref-1115",
        "ref-1107",
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
        "ref-1118",
        "ref-1117",
        "ref-1109",
        "ref-1106",
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
        "ref-1118",
        "ref-1117",
        "ref-010",
        "ref-1105",
        "ref-1107",
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
        "ref-1118",
        "ref-1109",
        "ref-1110",
        "ref-1113",
        "ref-1106",
        "ref-1116",
        "ref-1115",
        "ref-1107",
        "ref-1108",
        "ref-1117",
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
      "id": "ref-1106",
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
      "id": "ref-1107",
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
      "id": "ref-1113",
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
      "id": "ref-1117",
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
      "id": "ref-1118",
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
      "f3 DDS-Security 로깅 미사용: ref-009 와 ref-1118 이 같은 ROS 계열 문서라 독립 교차 확인으로 보지 않음",
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
    "limits": "web_fetch_available: true · fetch_mode full. 검색 16회/30, 신규 출처 15건/15(ref-1105~ref-1119)로 출처 상한에 도달해 IEC 62443 감사 요구 원문 대체 자료, MCP 도구 설명 오염 사례, 물류창고 사례를 더 넣지 못했다. 재사용 2건(ref-009 ROS 2 DDS-Security, ref-010 ROS 2 위협 모델): 입력 참고문헌 요약에 행이 없어 기관·제목·URL 은 공통 규칙의 대응표와 원문 머리말을 따랐고 발행일은 null 로 두었다(퍼블리셔가 기존 값으로 합칠 것). 주의: 입력의 이전 브리프 2026-09-30-09 가 ref-1105~ref-1118 을 이미 다른 출처에 썼다. 실행 컨텍스트가 이 구간을 이번 실행 전용으로 예약했다고 해 그대로 따랐으나 id 충돌 가능성이 있어 퍼블리셔 확인이 필요하다. 원문 열람: 16건 열었고(webfetch 12, github_raw 4) Quarta 외(ref-1119)만 403 으로 못 열었다. 논문은 모두 초록 기준이다. 교차 확인 0건: 핵심 수치가 모두 단일 출처라 finding 신뢰도는 medium 이하다. 벤더 기능·성능 주장은 쓰지 않았다(CISA 권고·연구 보고 중심). 분류 원문 핵심 질문에는 f21 로 답했고 결론은 '통신 인증·암호화 수단은 있으나 규격이 보안을 운영자에게 맡기고, LLM 층은 쉽게 탈옥되며, LLM 밖 규칙 검사·사람 승인·권한 분리·변조 방지 감사 기록을 겹친 다층 방어가 필요하다'는 추정이다. 현장 유형 사례는 병원(f8·f9)·가정(f12)·제조 공장(f10, 원문 미열람)이며 물류창고·상업 시설·실외는 찾지 못했다. 국내 자료는 KISA·소비자원 점검(f12, 기사)과 KISA 로봇 보안모델 배포(f13, 기사) 2건이고 KISA 원문은 인증서 오류로 열지 못했다. oq-144 는 f15·f17 이 부분 근거(시뮬레이션·실험실 수치)이며 현장 시험이 없어 해결 제안하지 않았다. 교차 규칙에 따라 대화 입력 방어 finding 은 13. 대화형 기능의 신뢰·기반·44. 로봇 기반 모델·언어 모델 계획과 함께 연결하도록 제안했다. 용어집에 이미 있는 프롬프트 주입·탈옥·DDS 보안 규격·인클레이브·보안 구역과 도관·감사 추적·과도한 에이전시·혼란된 대리인은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음."
  }
}
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

### docs/categories/security-and-privacy/authentication-authorization-and-isolation.md (요약)

```markdown
# 51. 인증·권한·격리

소속 대분류: N. 보안·개인정보 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

장비·사용자 인증, 명령 권한, 원격 접속 계정, 고객·현장 격리 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **장비·사용자 인증**: 로봇·설비·사용자를 인증한다
- **명령 권한 관리**: 누가 어느 로봇에 어떤 명령까지 내릴 수 있는지 정하고 강제한다
- **원격 접속·유지보수 계정**: 외부 유지보수 계정이 접속할 수 있는 범위와 기록을 관리한다
- **고객·현장 격리**: 고객·현장·방문자별로 데이터와 제어를 분리한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [52. 통신 보호·위협 관리·감사](communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](privacy-and-video-data.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 26번 영역 ‘사이버보안·접근권한·개인정보’(옛 대분류 G. 안전·보안·지능·거버넌스)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 장비 인증, 통신 보호, 명령 권한, 원격 접속, 고객별 격리, 영상·작업자 데이터 보호 [옛 분류원문]

> 옛 질문: 외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가? [옛 분류원문]

## 2. 핵심 질문

외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가? [분류원문]
```

### docs/categories/security-and-privacy/privacy-and-video-data.md (요약)

```markdown
# 53. 개인정보·영상 데이터

소속 대분류: N. 보안·개인정보 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-28 · 버전: 1

## 1. 한 줄 정의

영상·작업자·거주자 데이터 보호, 최소 수집·익명화 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **개인정보·영상 데이터 보호**: 카메라 영상과 작업자·환자·거주자 데이터를 보호한다
- **사람 데이터 최소 수집·익명화**: 보행자 위치·영상에서 신원을 떼어 내고 필요한 만큼만 모은다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 26번 영역 ‘사이버보안·접근권한·개인정보’에서 왔다. 그 본문은 [51. 인증·권한·격리](authentication-authorization-and-isolation.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

로봇이 찍은 영상과 사람의 위치 정보를 어디까지 모으고 어떻게 지킬 것인가? [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 1074건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 293개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- explicit-implicit-confirmation: 명시적 확인·암시적 확인 (Explicit / Implicit Confirmation)
- failure-explanation: 실패 설명 (Failure Explanation)
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
- managed-node: 관리형 노드 (Managed Node (ROS 2 Lifecycle Node))
- map-alignment: 지도 정합 (Map Alignment)
- map-version: 지도 버전 (Map Version (VDA 5050 mapId / mapVersion))
- mapf: 다중 에이전트 경로 찾기 (Multi-Agent Path Finding (MAPF))
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
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- predictive-maintenance: 예지 정비 (Predictive Maintenance)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- prompt-injection: 프롬프트 주입 (Prompt Injection)
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
- situation-awareness-based-agent-transparency: 상황 인식 기반 에이전트 투명성 (Situation Awareness-based Agent Transparency (SAT))
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

### docs/open-questions.md (요약: 대상 영역 [52] 에 걸린 1건 / 전체 228건)

```markdown
- oq-144 [열림] 로봇 대화 지시에 특화된 프롬프트 주입·탈옥 방어(도구 설명 신뢰 경계, 실행 전 물리 제약 검사, 다중 모델 감독)의 효과를 잰 공개 벤치마크나 현장 시험 결과가 있는가? (영역 13, 52, 48)
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

### runs/2026-09-30-10/research.md

```markdown
# 리서치 브리프 2026-09-30-10

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-10 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 49. 사람 근접 안전 |
| 대분류 | M. 안전 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 속도·분리 감시(SSM), 동력·힘 제한(PFL), 보호 분리 거리, 운용 구역, 속도 제한·진입 금지 구역, 움직임 지도(Maps of Dynamics) 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 물류창고·병원·실외·제조 공장 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 보호 분리 거리 계산, 로봇 측 감속·정지 영역, 플릿 수준 구역·속도 제한, 사람 인지형 배정·교통 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — ISO 10218·ISO/TS 15066, ISO 3691-4, ANSI/A3 R15.08, 실외이동로봇 운행안전인증, 산업안전보건기준에 관한 규칙 제223조, VDA 5050 구역, Nav2 Collision Monitor 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 0건
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 사람 가까이에서 로봇은 얼마나 떨어지고, 언제 느려지고 멈춰야 하는가? [분류원문]
2. 로봇과 사람 사이의 분리 거리는 표준에서 어떤 변수(사람 속도, 반응 시간, 정지 거리, 측정 불확실도)로 계산하며, 실제 구현에서 어떤 한계가 보고되는가? (섹션 4·6·8 겨냥)
3. 이동 로봇·협동로봇·실외 로봇의 사람 근접 안전을 다루는 국내외 표준·법규·인증(ISO 10218·ISO/TS 15066, ISO 3691-4, ANSI/A3 R15.08, 실외이동로봇 운행안전인증, 산업안전보건기준에 관한 규칙)은 구역·속도·감지·정지를 어떻게 규정하는가? (섹션 7 겨냥, 한국 자료 우선)
4. 구역별 속도 제한과 진입 금지를 플릿 관제 수준에서 표현·전달하는 인터페이스와 오픈소스(VDA 5050 구역, Nav2 Collision Monitor 등)는 무엇이며 안전 기능으로 인정되는가? (섹션 6·7·9 겨냥)
5. 물류창고·병원·실외·상업 시설 같은 현장에서 사람 근접 시 감속·정지·양보를 적용한 사례와 그 속도 기준은 무엇인가? (섹션 5 겨냥)
6. 안전 거리와 별개로 사람이 편안하게 느끼는 거리·속도, 사람의 움직임을 배정·교통에 반영하는 연구는 무엇을 보고하는가? (섹션 6·8 겨냥)
7. 사람 근접 안전에서 ROP가 직접 맡을 것과 로봇 제조사·시스템 통합자·설비에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Marvel·Norcross(NIST, Robotics and Computer-Integrated Manufacturing)는 ISO/TS 15066 의 속도·분리 감시(SSM)에서 보호 분리 거리가 사람 이동 속도, 로봇 반응 시간, 로봇 정지 시간(정지 거리), 침입 거리, 로봇·사람 위치 측정 불확실도로 계산되며, 분리 거리가 이 값 이하가 되면 안전 감시 정지를 건다고 정리했다. | ref-1075 | 아니오 | medium | 2016 | 제약 | — |
| f2 | [사실] | 같은 연구는 사람 속도로 ISO 13855 의 1,600 mm/s(최악 조건 2,000 mm/s), 침입 거리로 ISO 13855 기준 850~1,200 mm 를 들고, NIST 시험에서 레일 장착 로봇의 반응 시간을 약 0.113초로 측정했다고 보고했다. | ref-1075 | 아니오 | medium | 2016 | 제약 | — |
| f3 | [사실] | 같은 연구는 SSM 식이 속도의 방향을 무시하고 크기만 써서 멀어지는 로봇도 불필요한 정지를 일으킬 수 있고, 센서 잡음이 속도 추정 오차를 키우며, 갱신 주기가 낮을수록 로봇 평균 속도가 떨어지고, 보호 거리는 주로 로봇 제동 거리와 반응 시간이 좌우한다고 보고했다. | ref-1075 | 아니오 | medium | 2016 | 예외·성과 | — |
| f4 | [사실] | Hartmann 외(arXiv 2602.17822, 2026-02)는 ISO 10218-1/2 의 2025년 개정판이 협동 작업 기술 시방서 ISO/TS 15066 을 선택적 지침에서 규범적 요구로 본문에 통합하고, 로봇·협동 적용의 새 분류와 사이버보안 요구를 더했다고 분석했다. | ref-1076 | 아니오 | medium | 2026-02 | — | — |
| f5 | [사실] | 국내 산업안전보건기준에 관한 규칙 제223조는 산업용 로봇 운전 중 위험 방지를 위해 높이 1.8미터 이상의 울타리와 안전매트 설치를 기본으로 하되 2016년부터 한국산업표준 등 안전기준에 맞는 협동 운전 로봇은 울타리 설치를 면제하며, 협동 작업 방식은 속도·분리 감시(SSM), 핸드 가이딩(HGC), 동력·힘 제한(PFL)으로 나뉜다고 지디넷코리아가 전했다. | ref-1082 | 아니오 | low | 2024-03 | 제약 | — |
| f6 | [추정] | ISO 3691-4:2023(무인 산업용 트럭과 그 시스템의 안전 요구·검증)은 사람이 있는 운용 구역에서는 인력 감지를 요구하고, 훈련된 인원만 들어가는 제한 구역과 울타리 등으로 사람을 배제한 구역을 구분해 구역에 따라 보호 조치를 달리하는 것으로 알려져 있다. | ref-1077 | 아니오 | low | 2023 | 제약 | 원문 미열람 |
| f7 | [추정] | 같은 표준은 인력 감지를 끄거나 완전히 작동하지 않는 상황(예: 도킹)에서 속도를 0.3 m/s 이하로 제한하고, 인력 감지 성능을 서 있는 사람(지름 200 mm·높이 600 mm 원통)과 누운 사람(지름 70 mm·길이 400 mm 원통) 시험편으로 확인하는 것으로 알려져 있다. | ref-1077 | 아니오 | low | 2023 | 제약 | 원문 미열람 |
| f8 | [사실] | ANSI/A3 R15.08-2(2023)는 산업용 이동 로봇(IMR)을 특정 적용과 현장에 맞춰 통합·배치할 때의 안전 요구를 다루며, 배치 시스템의 위험성 평가는 IMR 시스템 통합자가 수행하도록 하고 모바일 매니퓰레이터와 잔여 위험, 최종 사용자 정보·교육을 포함한다고 The Robot Report 가 전했다. | ref-1088 | 아니오 | low | 2023-10-26 | — | — |
| f9 | [사실] | 한국로봇산업진흥원의 실외이동로봇 운행안전인증은 지능형 로봇 개발 및 보급 촉진법 제40조의2 에 근거해 배송 등 목적의 자율주행·원격제어 로봇과 관제장치의 조합을 대상으로 최고 속도 15 km/h 이하·최대 질량 500 kg 이하를 요구하고, 주변 인식·비상정지·횡단보도 통행·관제장치 등을 심사하며 2년 주기 정기점검을 둔다. | ref-1080, ref-1081 | 예 | high | 2026-09-30 | 실외 / 제약 | — |
| f10 | [사실] | 지디넷코리아(2023-07-28)는 산업통상자원부·한국로봇산업진흥원의 실외이동로봇 운행안전 기준이 로봇과 적재물 질량 합계에 따라 최고 속도를 230 kg 초과 5 km/h, 100 kg 초과 10 km/h, 그 이하 15 km/h 로 나누고, 보행 신호 중 도착한 로봇은 정지 대기 후 다음 신호에 횡단하게 하며 심사 항목을 16가지로 두었다고 전했다. | ref-1081 | 아니오 | medium | 2023-07-28 | 실외 / 제약 | — |
| f11 | [사실] | VDA 5050 3.0.0 은 플릿 관제가 이동 로봇에 전달하는 구역 유형으로 진입 금지(BLOCKED), 플릿 관제 승인 후 진입(RELEASE), 최고 속도 제한(SPEED_LIMIT), 자율 재계획 금지, 동작 유발, 우선·벌점·방향 구역을 정의하며, 속도 제한 구역에서는 로봇이 정해진 최고 속도보다 빠르게 달려서는 안 된다고 규정한다. | ref-1079 | 아니오 | medium | 2026-09-30 | 제약 | — |
| f12 | [사실] | VDA 5050 3.0.0 은 기능·운용·시스템 안전 요구를 정의하지 않으며 안전 표준으로 간주하거나 적용해서는 안 된다고 밝혀, 구역·속도 제한 전달이 안전 기능 자체를 대신하지 않음을 명시한다. | ref-1079 | 아니오 | medium | 2026-09-30 | — | — |
| f13 | [사실] | ROS 2 내비게이션 스택 Nav2 의 Collision Monitor 는 컨트롤러 속도 명령을 거르는 독립 노드로, 영역 안 장애물 점 수에 따른 정지·감속(비율)·속도 제한과 충돌까지 남은 시간 기반 접근 모델을 두고 여러 영역이 동시에 걸리면 가장 강한 조치를 쓰지만, 하드 실시간 안전 인증을 제공하지 않아 안전 등급 하드웨어를 대신하지 않는다고 밝힌다. | ref-1078 | 아니오 | medium | 2026-09-30 | 예외·성과 | — |
| f14 | [추정] | 아마존은 풀필먼트 센터에서 로봇 구역에 들어가는 직원이 로보틱스 테크 조끼를 착용·활성화하면 로봇이 자동으로 감속하거나 경로를 바꾸고 가까운 로봇은 정지한다고 설명한다. | ref-1084 | 아니오 | low | 2026-09-30 | 물류창고 / 제약 | 벤더 주장 |
| f15 | [사실] | Francis 외 52명(ACM Transactions on Human-Robot Interaction, arXiv 2306.16740)은 사회적 로봇 주행의 원칙을 안전·편안함·가독성·예의·사회적 역량·상대 이해·능동성·맥락 적합성 8가지로 정하고, 알고리즘을 공정하게 비교하기 위한 지표·시나리오·벤치마크·시뮬레이터 지침을 제시했다. | ref-1083 | 아니오 | medium | 2023-09 | — | — |
| f16 | [사실] | Jafari·Nguyen·Liu(arXiv 2604.13677, 2026-04)는 이동 로봇과 자원 보행자의 일대일 조우 실험에서 보행자가 보고한 편안함이 최소 거리와 최소 예상 충돌 시간 같은 운동학 변수와 중간 정도의 유의한 상관을 보였고, 이들을 합친 복합 지표가 오즈비 3.67 로 가장 잘 예측했다고 보고했다. | ref-1089 | 아니오 | medium | 2026-04 | 제약 | — |
| f17 | [사실] | Rondoni 외(Scientific Reports, 2024-08)는 병원 물류용 HOSBOT 과 TIAGo 를 시뮬레이션 병원 환경에서 실내 보행 속도에 견줄 만한 0.2·0.6·1.0 m/s 로 주행시켜 완료 시간·경로 길이·최소 장애물 거리 등 7개 지표로 비교했고, 속도가 높을수록 정확도가 떨어졌다고 보고했다. | ref-1085 | 아니오 | medium | 2024-08-07 | 병원 / 제약 | — |
| f18 | [사실] | Farrell 외(UC San Diego, arXiv 2503.21141, 2025-03)는 학습 기반 제어 장벽 함수(CBF)를 Open-RMF 에 통합해 창고의 다중 로봇·다중 행위자 상황에서 보행자를 포함한 정적·동적 장애물을 피하는 안전 강화 제어를 제안하고 로봇 수·속도·장애물 수를 바꿔 평가했다. | ref-1086 | 아니오 | medium | 2025-03-27 | 물류창고 | — |
| f19 | [사실] | Kazemi Eskeri 외(IROS 2025)의 사람 인지형 작업 배정(HATA)은 과거 사람 이동 패턴을 담은 시공간 질의형 움직임 지도(Maps of Dynamics)로 사람이 작업 실행 시간에 주는 영향을 확률적 비용으로 추정해 배정에 반영했고, 사람 움직임을 고려하지 않는 기준선보다 임무 완료 시간을 26%, 기존 기준선보다 19% 줄였다고 보고했다. | ref-1087 | 아니오 | medium | 2025-08-27 | 수행 자원 | — |
| f20 | [추정] | 확인한 자료를 종합하면 핵심 질문(얼마나 떨어지고 언제 느려지고 멈춰야 하는가)에 대해, 분리 거리는 고정값이 아니라 사람 속도·반응 시간·정지 거리·측정 불확실도로 그때그때 계산되고(f1~f3), 감속·정지 기준은 적용 유형별 표준·인증이 구역·속도 상한으로 정하며(f6·f7·f9·f10), 사람이 편안하게 느끼는 거리·충돌 시간은 안전 정지 거리와 별도의 기준이 필요한 것으로 보인다(f15·f16). | ref-1075, ref-1077, ref-1080, ref-1081, ref-1083, ref-1089 | 아니오 | low | 2026-09-30 | — | — |
| f21 | [추정] | 확인한 자료를 종합하면 이 영역이 중요한 까닭은, 안전 거리가 로봇 정지 성능과 센서 갱신에 따라 달라져 로봇·현장마다 다르고(f1~f3), 협동로봇·무인 트럭·실외 로봇이 각기 다른 표준·법규로 울타리 면제·구역·속도 상한을 정하며(f4~f10), 보수적인 감속·정지가 처리량과 수용성에 영향을 주기 때문이다(f3·f16·f19). | ref-1075, ref-1076, ref-1082, ref-1077, ref-1088, ref-1080, ref-1081, ref-1089, ref-1087 | 아니오 | low | 2026-09-30 | — | — |
| f22 | [추정] | 확인한 자료를 종합하면 49. 사람 근접 안전에서 ROP가 직접 맡을 범위는 구역·시간대별 속도 제한과 진입 금지·승인 구역을 정의해 이종 로봇에 전달하는 것(f11), 사람 위치·출입 신호를 받아 플릿 수준에서 감속·우회·배정을 조정하는 것(f14·f18·f19), 그 조정과 정지·재개 이력을 기록하는 것이며, 이는 로봇의 안전 기능을 대신하지 않는 보조 계층으로 보아야 할 것으로 보인다(f12·f13). | ref-1079, ref-1084, ref-1086, ref-1087, ref-1078 | 아니오 | low | 2026-09-30 | — | — |
| f23 | [추정] | 연계 대상: 분류 원문 19장 기준으로 안전 등급 인력 감지·보호 필드·보호 정지와 SSM·PFL 같은 로봇 안전 기능(f1·f5·f6·f7)은 로봇 제조사와 시스템 통합자에, 현장 배치의 위험성 평가(f8)는 시스템 통합자에, 울타리·안전매트·인터록(f5)은 설비 안전 쪽에, 실외 인증 대상인 로봇·관제장치 조합의 적합성(f9)은 운영 사업자에 속하므로, ROP 는 그 설정값과 상태를 받아 계획에 반영하는 인터페이스를 맡을 것으로 보인다. | ref-1075, ref-1082, ref-1077, ref-1088, ref-1080 | 아니오 | low | 2026-09-30 | — | — |
| f24 | [추정] | 이 영역은 위험성 평가·정지·재개의 48. 안전·위험 관리(f8), 표준·인증의 50. 안전 표준·인증·사고 조사(f4~f10), 사람 이동 모델의 19. 사람·보행자 모델(f16·f19), 구역을 담는 16. 장소 의미·지도 관리(f11), 구역을 전달하는 20. 로봇·제조사 관제 연동·21. 상호운용 표준·적합성(f11·f12), 사람 인지형 배정의 25. 작업 배정 — MRTA(f19), 구역·속도를 반영하는 27. 다중 로봇 경로·교통 관리 — MAPF(f11·f18), 협동 작업의 31. 사람–로봇 협업(f1·f5), 법규의 59. 법·규제·보험·라이선스(f5·f9), 수용성의 60. 노동·수용성·접근성(f15·f16), 평가의 54. 시험·형식 검증·벤치마크(f15·f17), 적용 현장인 61. 물류창고(f14·f18)·63. 병원·의료(f17)·66. 실외(f9·f10)와 이어진다. | ref-1088, ref-1076, ref-1080, ref-1089, ref-1087, ref-1079, ref-1086, ref-1075, ref-1082, ref-1083, ref-1085, ref-1084 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1075 | Marvel, J. A., & Norcross, R. (NIST, Robotics and Computer-Integrated Manufacturing) | Implementing Speed and Separation Monitoring in Collaborative Robot Workcells | 2016 | 논문 | high | 2026-09-30 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5117641/ | 아니오 |
| ref-1076 | Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv) | Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066 | 2026-02-19 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2602.17822 | 아니오 |
| ref-1077 | ISO (ISO/TC 110) | ISO 3691-4:2023 Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems (제목 일부는 검색 결과 기준) | 2023 | 표준 | medium | 2026-09-30 | https://www.iso.org/standard/83545.html | 예 |
| ref-1078 | Open Navigation (ros-navigation/navigation2) | nav2_collision_monitor — README | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/ros-navigation/navigation2/blob/main/nav2_collision_monitor/README.md | 아니오 |
| ref-1079 | VDA / VDMA (VDA5050/VDA5050) | VDA 5050 — Interface for the communication between transport vehicles and a master control (VDA5050_EN.md, 3.0.0) | 미확인 | 표준 | high | 2026-09-30 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-1080 | 한국로봇산업진흥원 | 실외이동로봇 운행안전인증 | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://www.kiria.org/portal/cert/portalCertEstiSafe.do | 아니오 |
| ref-1081 | 지디넷코리아 | 실외 배달로봇 '시속 15km 이하로'...16가지 안전기준 (제목 일부는 검색 결과 기준) | 2023-07-28 | 기사 | medium | 2026-09-30 | https://zdnet.co.kr/view/?no=20230728173101 | 아니오 |
| ref-1082 | 지디넷코리아 | "협동로봇 충돌 안전 계산하고 써야죠" | 2024-03 | 기사 | low | 2026-09-30 | https://zdnet.co.kr/view/?no=20240305160245 | 아니오 |
| ref-1083 | Francis, A., Pérez-D'Arpino, C., Li, C. 외 (ACM Transactions on Human-Robot Interaction, arXiv) | Principles and Guidelines for Evaluating Social Robot Navigation Algorithms | 2023-06-29 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2306.16740 | 아니오 |
| ref-1084 | Amazon | Ever wonder how people and robots team up on your Amazon order? | 미확인 | 벤더 문서 | medium | 2026-09-30 | https://www.aboutamazon.com/news/operations/ever-wonder-how-people-and-robots-team-up-on-your-amazon-order | 아니오 |
| ref-1085 | Rondoni 외 (Scientific Reports) | Navigation benchmarking for autonomous mobile robots in hospital environments | 2024-08-07 | 논문 | high | 2026-09-30 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11306802/ | 아니오 |
| ref-1086 | Farrell, S., Li, C., Yu, H., Yoshimitsu, R., Gao, S., & Christensen, H. I. (arXiv) | Safe Human Robot Navigation in Warehouse Scenario | 2025-03-27 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2503.21141 | 아니오 |
| ref-1087 | Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv) | Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments | 2025-08-27 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2508.19731 | 아니오 |
| ref-1088 | The Robot Report | New AMR safety standard available with release of ANSI/A3 R15.08-2 | 2023-10-26 | 기사 | low | 2026-09-30 | https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/ | 아니오 |
| ref-1089 | Jafari, A., Nguyen, H.-S., & Liu, Y.-C. (arXiv) | Empirical Prediction of Pedestrian Comfort in Mobile Robot Pedestrian Encounters | 2026-04-15 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2604.13677 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/safety/human-proximity-safety.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f21(왜 중요한가), f20(핵심 질문 답, 추정) / 섹션 4: 속도·분리 감시·보호 분리 거리 f1·f2, 동력·힘 제한 f5, 운용 구역 f6, 속도 제한·진입 금지·승인 구역 f11, 움직임 지도 f19, 제어 장벽 함수 f18, 사회적 주행 원칙 f15 / 섹션 5: 물류창고 — f14(제약: 조끼 신호로 감속·우회·정지, 벤더 주장 병기)·f18(연구, 창고 시나리오), 병원 — f17(제약: 보행 속도 기반 0.2~1.0 m/s, 시뮬레이션 병원임을 명시), 실외 — f9·f10(제약: 15 km/h·질량별 속도 상한·횡단보도 대기). 제조 공장은 f5(산업용 로봇 사업장 규정)로 서술하되 현장 사례가 아님을 밝히고, 상업 시설·가정·기타 사례는 찾지 못함을 명시 / 섹션 6: 계산형 보호 거리 f1~f3, 로봇 측 감속·정지 영역 f13, 플릿 수준 구역·속도 제한 f11·f12, 착용형 신호 f14, 사람 인지형 배정·교통 f18·f19, 편안함 지표 f16 / 섹션 7: ISO 10218·ISO/TS 15066 f4, ISO 3691-4 f6·f7(원문 미열람), ANSI/A3 R15.08-2 f8, 실외이동로봇 운행안전인증 f9·f10, 산업안전보건기준에 관한 규칙 제223조 f5, VDA 5050 구역 f11·f12, Nav2 Collision Monitor f13 / 섹션 8: f1·f3·f15·f16·f17·f18·f19·f4 / 섹션 9: f22(직접 범위), f23(연계 대상) / 섹션 10: f24 — 16, 19, 20, 21, 25, 27, 31, 48, 50, 54, 59, 60, 61, 63, 66 / 섹션 11: open_questions_new 4건. 다음 실행 후보: 50. 안전 표준·인증·사고 조사 페이지 섹션 7 에 f4·f6~f10 반영, 16. 장소 의미·지도 관리 페이지에 f11 구역 유형 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 속도·분리 감시 | Speed and Separation Monitoring (SSM) | 로봇과 사람의 거리와 속도를 계속 감시해 분리 거리가 보호 분리 거리보다 작아지기 전에 로봇을 감속하거나 정지시키는 협동 작업 방식이다. |
| 보호 분리 거리 | Protective Separation Distance | 사람 이동 속도, 로봇 반응·정지 시간, 침입 거리, 위치 측정 불확실도로 계산하는, 로봇이 사람에 닿기 전에 멈출 수 있도록 유지해야 하는 최소 거리다. |
| 동력·힘 제한 | Power and Force Limiting (PFL) | 로봇이 사람과 접촉하더라도 해를 주지 않도록 동력과 힘을 정해진 한계 안으로 제한해 작동시키는 협동 작업 방식이다. |
| 움직임 지도 | Maps of Dynamics (MoD) | 과거 사람 이동을 장소와 시간에 따라 모아 특정 위치·시각의 이동 방향과 흐름을 질의할 수 있게 만든 시공간 지도다. |
| 제어 장벽 함수 | Control Barrier Function (CBF) | 로봇 상태가 안전 집합 밖으로 나가지 않도록 제어 입력에 제약을 거는 함수로, 기존 제어 명령을 안전 쪽으로 걸러 내는 데 쓴다. |

## 열린 질문

새로 생긴 질문:

- 플릿 관제가 내리는 구역별 속도 제한·진입 금지는 안전 등급이 아닌 소프트웨어 기능인데, 이것을 위험성 평가에서 위험 감소 조치로 인정받으려면 로봇의 안전 등급 보호 필드 설정과 어떻게 맞추고 누가 검증하는가? | 관련 영역: 49. 사람 근접 안전, 48. 안전·위험 관리 | 근거: f12 | 종류: 일반
- 실외이동로봇 운행안전인증의 심사 항목 수를 인증기관 페이지는 8개 항목으로, 기사는 16가지로 전하는데 어느 쪽이 항목 단위이며 세부 항목 목록은 무엇인가? | 관련 영역: 49. 사람 근접 안전, 50. 안전 표준·인증·사고 조사 | 근거: f10 | 종류: 출처 충돌
- 국내 병원·상업 시설·공동주택 실내에서 운행하는 서비스 로봇의 사람 근접 속도·거리 기준을 정한 법령·표준·인증이 있는가? | 관련 영역: 49. 사람 근접 안전, 59. 법·규제·보험·라이선스 | 근거: f9 | 종류: 일반
- 착용형 장치나 출입 통제 신호로 얻은 사람 위치를 제조사가 다른 여러 로봇 플릿에 동시에 전달해 감속·정지시키는 표준 인터페이스나 사례가 있는가? | 관련 영역: 49. 사람 근접 안전, 21. 상호운용 표준·적합성 | 근거: f14 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 1
- 예산 사용량: 검색 13회 · 신규 출처 15건
- 미확인 항목:
    - f6·f7 ISO 3691-4:2023 의 구역 구분, 감지 무효화 시 0.3 m/s, 시험편 치수: ISO·ANSI 블로그 페이지 403 으로 원문 미열람, 검색 결과 요약 기준이라 추정·low 로 둠
    - f5 산업안전보건기준에 관한 규칙 제223조 조문: law.go.kr 페이지에서 조문 본문을 읽지 못했고 yeslaw 는 인증서 오류로 열지 못해 기사(ref-1082)만 근거
    - f8 ANSI/A3 R15.08-2 원문 미열람(유료). 플릿(IMRF) 포함 여부는 검색 요약에만 있어 claim 에 넣지 않음
    - f14 아마존 조끼: 2018년 25개 창고 도입 등 수치는 검색 요약(위키백과)에만 있어 넣지 않음. 독립 출처 교차 확인 실패
    - f15 근접학 거리(0.45 m·1.2 m) 예시는 검색 요약에만 있어 넣지 않음
    - f16 실험 장소·참가자 수, f18 정량 결과, f19 실험 환경은 초록에 없어 미확인
    - f10 심사 항목 16가지와 f9 인증기관 페이지 8개 항목의 차이: 출처 충돌로 열린 질문에 올림
    - ISO 13482(개인 돌봄 로봇) 개정판 내용: 검색 1회에서 2025년 개정 세부를 확인하지 못해 넣지 않음
    - 상업 시설·가정·기타 현장의 사람 근접 감속·정지 사례는 찾지 못함(쇼핑몰·공항 검색 1회, 찾은 소매점 배치 연구 arXiv 2601.01946 은 근접 안전 내용이 없어 제외)
    - 제조 공장 현장 사례는 규정(f5)과 작업셀 연구(f1~f3)만 있고 현장 유형을 밝힌 적용 사례는 찾지 못함
- 범위 경계 위반 의심:
    - f1~f3·f5~f7: 안전 등급 인력 감지·보호 정지·SSM·PFL 은 로봇 제조사·시스템 통합자의 안전 기능(원문 19장 로봇 자체 지능·제어, 설비 안전 제어 연계 대상)이므로 개념·기준 근거로만 쓰고 f23 에서 '연계 대상: '으로 구분함
    - f13: Nav2 Collision Monitor 는 로봇 측 로컬 회피 계층(연계 대상)이며 안전 인증이 없음을 명시; ROP 직접 범위로 서술하지 않도록 주의
    - f9·f10: 실외이동로봇 인증 대상은 로봇과 관제장치의 조합이라 관제장치 쪽이 ROP 범위와 겹칠 수 있음. 인증 책임은 운영 사업자 몫으로 f23 에서 구분
    - f18: 제어 장벽 함수는 로봇 제어 계층 기법이지만 Open-RMF 플릿 계층에 통합한 사례로만 인용
- 한계: web_fetch_available: true · fetch_mode full. 검색 13회/30, 신규 출처 15건/15(ref-1075~ref-1089, 예약 구간 안)로 출처 상한에 도달해 ISO 13482·ISO 13855 원문, 상업 시설·가정 사례, 국내 서비스 로봇 기준을 더 넣지 못했다. 주의: 입력의 이전 브리프 2026-09-30-08 도 ref-1075~ref-1089 를 썼으나 실행 컨텍스트가 이 구간을 이 실행 전용으로 예약했다고 밝혀 그대로 썼다(퍼블리셔의 id 충돌 확인 필요). 재사용 출처 없음(입력의 참고문헌 요약에 이 영역 인용 0건; VDA 5050·ISO 3691-4 가 기존 참고문헌에 있으면 퍼블리셔가 같은 URL 로 합쳐야 한다). 원문 열람: 14건 열었고(webfetch 12건, github_raw 2건) ISO 3691-4(ref-1077)만 403 으로 못 열어 source_unopened 로 표시했다. 논문 가운데 Marvel·Norcross(ref-1075)·Rondoni 외(ref-1085)는 PMC 본문, 나머지는 초록 페이지다. 교차 확인 1건(f9: 15 km/h·500 kg 을 인증기관 페이지와 기사로 확인). 벤더 문서는 아마존(ref-1084) 1건이며 f14 는 vendor_claim·추정·'벤더 주장: ' 첫머리로 냈다. 분류 원문 핵심 질문(얼마나 떨어지고 언제 느려지고 멈춰야 하는가)에는 f20 으로 답했고 결론은 '분리 거리는 계산값이고, 감속·정지 상한은 적용 유형별 표준·인증이 구역·속도로 정하며, 편안함 기준은 별도'라는 추정이다. 현장 유형 사례는 물류창고(f14·f18)·병원(f17, 시뮬레이션)·실외(f9·f10)이며 제조 공장은 규정 수준, 상업 시설·가정·기타는 찾지 못했다. 국내 자료는 한국로봇산업진흥원(ref-1080)·지디넷코리아 2건(ref-1081·ref-1082)이다. 용어집에 이미 있는 운용 구역·구역 집합·위험성평가·협동 적용·실외이동로봇 운행안전인증·공공 영역 이동로봇·필터 마스크·해제 구역은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 없음.
```

### runs/2026-09-30-09/research.md

```markdown
# 리서치 브리프 2026-09-30-09

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-09 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 46. 예측·학습 기반 최적화 |
| 대분류 | L. AI·학습 기술 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 결정 중심 학습(예측 후 최적화), 예지 정비·예지(prognostics), 모방 학습, 안내 그래프 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 물류창고·병원·제조 공장·기타 현장의 학습·예측 적용 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 학습 기반 배정, 학습 기반 경로(MAPF), 학습과 탐색의 결합, 수요 예측의 배정 반영, 고장·배터리 예측 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — ISO 13381(예지), POGEMA 벤치마크 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 0건
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 학습과 예측이 배정·경로·정비 결정을 실제로 개선하는가? [분류원문]
2. 강화학습·모방학습·그래프 신경망 기반 다중 로봇 작업 배정 연구는 어떤 기준선 대비 어떤 개선을 보고하며, 실제 현장 검증이 있는가? (섹션 6·8 겨냥)
3. 학습 기반 다중 로봇 경로·교통(MAPF) 방법은 탐색 기반 방법과 비교해 어디서 앞서고 어디서 뒤지는가? (섹션 6·8 겨냥)
4. 작업 요청·물동량 같은 수요 예측을 배정·로봇 구성·인력 계획에 쓴 사례는 무엇이며 예측 오차와 분포 이동은 어떻게 다루는가? (섹션 5·6 겨냥)
5. 로봇 고장·배터리 상태 예측(예지 정비)을 계획·정비에 쓰는 연구·사례와 관련 표준은 무엇인가? (섹션 5·7 겨냥, 한국 사례 우선)
6. 예측 정확도가 아니라 결정 품질을 기준으로 예측 모델을 학습하는 개념(예측 후 최적화, 결정 중심 학습)은 무엇인가? (섹션 4·6 겨냥)
7. 예측·학습 기반 최적화에서 ROP가 직접 맡을 것과 로봇 제조사·상위 업무 시스템에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Amazon 연구진(Agaskar 외, arXiv 2508.08574, 2025-08 제출·2026-04 개정)의 DeepFleet 는 전 세계 아마존 창고에서 수십만 대 로봇의 위치·목표·상호작용 이동 데이터로 학습한 다중 로봇 기반 모델 모음으로, 로봇 중심(RC)·로봇–바닥(RF)·이미지–바닥(IF)·그래프–바닥(GF) 네 구조 가운데 비동기 상태 갱신과 국지 상호작용 구조를 쓰는 RC 와 GF 가 가장 유망하다고 보고했다. | ref-1105 | 아니오 | medium | 2025-08 | 물류창고 | — |
| f2 | [추정] | Amazon Science 블로그는 DeepFleet 가 풀필먼트·분류 센터 로봇의 미래 교통 패턴과 위치를 예측해 현재는 혼잡 예측으로 작업 배정과 경로를 병목 회피 쪽으로 조정하는 데 쓰이고, 앞으로 로봇별 작업 배정과 목표 위치를 직접 내는 것을 목표로 하며, 로봇 이동 효율을 10% 높였다고 주장한다. | ref-1106 | 아니오 | low | 2025-08-11 | 물류창고 / 예외·성과 | 벤더 주장 |
| f3 | [사실] | Skrynnik 외의 POGEMA 벤치마크(ICLR 2025)는 고전 MAPF 에서 탐색 기반 중앙 계획기 LaCAM 이 다른 모든 방법보다 뚜렷이 앞서고 학습형 전용 해법(DCC·SCRIMP)이 그 뒤를 따르며 순수 다중 에이전트 강화학습(MARL)은 크게 뒤처지고 분포 밖 데이터셋에서 한 인스턴스도 풀지 못했으며, 지속형(lifelong) MAPF 에서는 탐색 기반 RHCR 가 확장성 지표를 뺀 모든 경우에 우월했다고 보고했다. | ref-1109 | 아니오 | medium | 2025-04 | — | — |
| f4 | [사실] | Andreychuk 외의 MAPF-GPT(arXiv 2409.00134, AAAI 2025)는 전문가 MAPF 해의 대규모 데이터셋을 트랜스포머로 모방학습한 경로 찾기 기반 모델로, 추가 휴리스틱이나 에이전트 간 통신 없이 행동을 생성하며 기존 최고 학습형 MAPF 해법보다 뚜렷이 앞서고 학습 데이터에 없는 문제에서도 제로샷으로 동작한다고 보고했다. | ref-1107 | 아니오 | medium | 2024-08 | — | — |
| f5 | [사실] | Jiang 외의 SILLM(arXiv 2410.21415, ICRA 2025)은 모방학습에 통신 모듈·충돌 해소·전역 안내를 결합한 지속형 MAPF 방법으로, 최대 1만 대·대형 지도 6종에서 최고 학습 기반 기준선보다 처리량 137.7%, 최고 탐색 기반 기준선보다 16.0% 높았고 2023 League of Robot Runners 우승 해법을 앞섰으며 실물 로봇 10대와 가상 로봇 100대로 검증했다고 보고했다. | ref-199 | 아니오 | medium | 2024-10 | — | — |
| f6 | [사실] | Zhang 외의 안내 그래프 최적화(Guidance Graph Optimization, IJCAI 2024)는 지속형 MAPF 알고리즘이 따르는 격자 간선 가중치를 배치 전에 오프라인으로 최적화하거나 가중치를 생성하는 갱신 모델을 학습하는 방식으로, 대표적인 지속형 MAPF 알고리즘 3종의 처리량을 벤치마크 지도 8종에서 높였고 갱신 모델은 93×91 지도·에이전트 3,000개까지 적용됐다. | ref-1118 | 아니오 | medium | 2024-02 | — | — |
| f7 | [사실] | Agrawal·Bedi·Manocha 의 RTAW(ICRA 2023)는 창고 다중 로봇 작업 배정을 마르코프 결정 과정으로 두고 로봇·작업 수와 무관한 전역 임베딩을 쓰는 주의 기반 정책을 PPO 로 학습해, 시뮬레이션 창고(로봇 최대 1,000대)에서 픽업 거리 최소화 탐욕 규칙·후회(regret) 기반 방법보다 총 이동 지연을 최대 14% 줄였다고 보고했다. | ref-623 | 아니오 | medium | 2022-09 | — | — |
| f8 | [사실] | Garces 외(arXiv 2608.21554, 2026-08)는 병원 입원 병동의 실제 간호 업무 요청 데이터를 써서, 작업이 요청으로 발생하는 이기종 다중 로봇 배정을 미래 요청 시나리오를 표본 추출해 평가하되 즉시 확정은 이미 들어온 요청에만 하는 예측 인지형 모델 기반 강화학습 롤아웃으로 풀었다. | ref-1116 | 아니오 | medium | 2026-08 | 병원 / 시작 조건 | — |
| f9 | [사실] | 같은 연구(Garces 외)는 최근 예측 오차에 따라 예측 요청의 가중치를 다시 매기고 아직 시작하지 않은 배정만 다시 최적화하는 방식으로 분포 이동에 대응했으며, 배치 전에 과거 요청 데이터로 이기종 로봇 구성(차량 소요대수)을 고르는 절차를 두었다. | ref-1116 | 아니오 | medium | 2026-08 | 병원 / 수행 자원 | — |
| f10 | [사실] | 같은 연구(Garces 외)는 반응형·토큰 패싱·예측 위치 선배치·근시적 탐욕 기준선과 비교해 거의 모든 요청을 처리하면서 대기 시간을 줄였고, 개선 폭은 꼬리 지연 지표에서 가장 컸다고 보고했다. | ref-1116 | 아니오 | medium | 2026-08 | 병원 / 예외·성과 | — |
| f11 | [사실] | Elmachtoub·Grigas 의 Smart "Predict, then Optimize"(SPO)는 일반 기계학습이 예측 오차만 줄이고 예측이 어떻게 쓰일지 고려하지 않는다고 보고, 예측이 만든 결정 손실(SPO 손실)과 그 볼록 대리 손실 SPO+ 로 최적화 문제의 목적·제약을 학습에 반영했으며, 최단 경로·포트폴리오 실험에서 모형이 잘못 지정된 경우 특히 표준 예측 후 최적화보다 크게 나았다. | ref-1115 | 아니오 | medium | 2017-10 | — | — |
| f12 | [사실] | Poskart 외(Sensors, 2022-12)는 사내 물류·유연 생산 환경을 대상으로 MiR100 자율이동로봇의 미션별 배터리 소모를 회전 수·이동 거리·충전 상태(SoC)·SoC×거리 항을 쓰는 일반화 선형 모형으로 예측해 조정 결정계수 0.9629·0.9694 를 얻었고, 이 예측을 실행 전 미션 가능 여부 판단과 다른 로봇으로의 위임, 로봇 추가 필요 판단에 쓸 수 있다고 제시했다. | ref-1112 | 아니오 | medium | 2022-12-15 | 제약 | — |
| f13 | [사실] | Pookkuttath 외(Sensors, 2021-12)는 증기 걸레 청소 로봇의 관성 측정 장치(IMU) 진동 신호를 정상·지형·충돌·조립 풀림·구조 불균형 5종으로 분류하는 1차원 합성곱 신경망으로 오프라인 92.2%, 싱가포르 기술디자인대학(SUTD) 캠퍼스 로비·푸드코트·복도의 실시간 현장 시험 91% 정확도를 보고했고, 분류 결과를 SLAM 지도에 겹친 예지 정비 지도로 정비 팀이 위험 구역을 격리하고 심각도를 판단하게 했다. | ref-1111 | 아니오 | medium | 2021-12-21 | 기타 / 예외·성과 | — |
| f14 | [추정] | 파이낸셜뉴스(2026-05-28)가 전한 현대자동차 발표에 따르면 현대차는 산업용 로봇팔의 모터 부하·진동·전류 신호를 학습한 AI 고장예측 시스템으로 고장 약 5일 전에 90% 이상 정확도로 이상을 감지하며, 국내 생산 현장에 먼저 적용한 뒤 해외 생산거점으로 넓혀 사후 대응에서 계획적 예측 정비로 바꾸려 한다. | ref-1113 | 아니오 | low | 2026-05-28 | 제조 공장 / 예외·성과 | 벤더 주장 |
| f15 | [사실] | ISO 13381-1 은 기계 상태 감시·진단의 예지(prognostics) 일반 지침으로, 개발자·공급자·사용자·제조사가 예지 개념을 공유하고 정확한 예지에 필요한 데이터·특성·절차를 정하게 하는 것을 목적으로 하며, 2025년 3판이 2015년 2판을 대체했고 같은 시리즈의 다른 부는 성능 추세, 사이클 기반 수명 사용, 잔여 유효 수명 모델 같은 예지 접근을 다룬다. | ref-1114 | 아니오 | medium | 2025 | — | 원문 미열람 |
| f16 | [추정] | 연계 대상: CJ대한통운은 2021년 자사 뉴스룸에서 이커머스 통합 플랫폼 iFlex 가 AI·빅데이터로 주문 유형별 물량을 예측해 물류센터 인력 배치를 최적화한다고 밝혔다. | ref-1117 | 아니오 | low | 2021-07-28 | 물류창고 / 수행 자원 | 벤더 주장 |
| f17 | [추정] | 확인한 자료를 종합하면 핵심 질문(학습과 예측이 배정·경로·정비 결정을 실제로 개선하는가)에 대해, 개선 근거는 대부분 시뮬레이션·벤치마크이고(f3~f7) 실제 운영 개선 수치는 벤더 주장에 머물며(f2·f14·f16), 학습 단독 정책은 탐색 기반 방법보다 뒤지거나 분포 밖에서 실패할 수 있어(f3), 탐색·최적화와 결합하거나(f5·f6) 결정 손실로 예측을 학습하거나(f11) 관측된 요청만 확정하고 예측 오차로 재가중하는(f8·f9) 설계에서 개선이 보고되는 것으로 보인다. | ref-1109, ref-1107, ref-199, ref-1118, ref-623, ref-1106, ref-1113, ref-1117, ref-1115, ref-1116 | 아니오 | low | 2026-09-30 | — | — |
| f18 | [추정] | 확인한 자료를 종합하면 이 영역이 중요한 까닭은, 대규모 플릿에서 혼잡을 미리 알아야 배정·경로를 조정할 수 있고(f1·f2), 요청이 시간에 따라 달라지고 분포가 바뀌며(f8·f9), 예측 정확도가 높아도 결정 품질이 따라오지 않을 수 있고(f11), 배터리 소모와 고장이 계획을 어긋나게 하기 때문이다(f12~f14). | ref-1105, ref-1106, ref-1116, ref-1115, ref-1112, ref-1111, ref-1113 | 아니오 | low | 2026-09-30 | — | — |
| f19 | [추정] | 확인한 자료를 종합하면 46. 예측·학습 기반 최적화에서 ROP가 직접 맡을 범위는 플릿 수준의 이동·요청·배터리·경보 이력 수집과 학습·예측 모델에의 공급(f1·f8·f12), 예측 결과를 배정·경로·충전·정비 계획에 넣는 인터페이스(f2·f12), 학습 정책을 탐색·규칙 기반 기준선과 같은 조건에서 비교하는 평가와 예측 오차·분포 이동 감시(f3·f9), 학습 정책의 즉시 확정 범위 제한(f8)이다. | ref-1105, ref-1106, ref-1116, ref-1112, ref-1109 | 아니오 | low | 2026-09-30 | — | — |
| f20 | [추정] | 연계 대상: 분류 원문 19장 기준으로 모터 전류·진동·IMU 같은 로봇 부품 수준 상태 감시와 배터리 셀 관리(f13·f14)는 로봇 제조사와 설비 정비 쪽에, 전사 주문 수요예측(f16)은 상위 업무 시스템 쪽에 속하므로, 이종 제조사를 잇는 ROP 는 그 결과(고장 위험·예측 물량)를 받아 배정·정비 일정에 반영하는 역할을 맡을 것으로 보인다. | ref-1111, ref-1113, ref-1117 | 아니오 | low | 2026-09-30 | — | — |
| f21 | [추정] | 이 영역은 학습 기반 배정의 25. 작업 배정 — MRTA(f7·f8), 학습 기반 경로의 27. 다중 로봇 경로·교통 관리 — MAPF(f3~f6), 결정 중심 예측의 26. 작업 순서·스케줄링(f11), 배터리 예측의 28. 공용 자원·충전·에너지 최적화(f12), 고장 예측의 38. 모니터링·이상 탐지·원인 분석(f13·f14), 분포 이동 감시의 47. AI·학습·적응과 모델 운영(f9), 벤치마크의 54. 시험·형식 검증·벤치마크(f3), 기반 모델 흐름의 44. 로봇 기반 모델·언어 모델 계획(f1·f4), 로봇 구성 산정의 35. 처리능력·규모·배치 설계(f9·f12), 정비 기준의 57. 자산·소프트웨어 수명주기 관리(f15), 수요 정보의 23. 업무 시스템 연동(f16), 적용 현장인 61. 물류창고(f1·f2·f16)·62. 제조 공장(f14)·63. 병원·의료(f8~f10)·67. 기타 현장(f13)과 이어진다. | ref-623, ref-1116, ref-1109, ref-1107, ref-199, ref-1118, ref-1115, ref-1112, ref-1111, ref-1113, ref-1105, ref-1106, ref-1114, ref-1117 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1105 | Agaskar, A., Siva, S., Pickering, W. 외 (Amazon, arXiv) | DeepFleet: Multi-Agent Foundation Models for Mobile Robots | 2025-08 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2508.08574 | 아니오 |
| ref-1106 | Amazon Science | Amazon builds first foundation model for multirobot coordination | 2025-08-11 | 벤더 문서 | medium | 2026-09-30 | https://www.amazon.science/blog/amazon-builds-first-foundation-model-for-multirobot-coordination | 아니오 |
| ref-1107 | Andreychuk, A., Yakovlev, K., Panov, A., & Skrynnik, A. (arXiv, AAAI 2025) | MAPF-GPT: Imitation Learning for Multi-Agent Pathfinding at Scale | 2024-08 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2409.00134 | 아니오 |
| ref-199 | Jiang, H., Wang, Y., Veerapaneni, R., Duhan, T., Sartoretti, G., & Li, J. (arXiv, ICRA 2025) | Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding | 2024-10 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2410.21415 | 아니오 |
| ref-1109 | Skrynnik, A., Andreychuk, A., Borzilov, A., Chernyavskiy, A., Yakovlev, K., & Panov, A. (ICLR 2025, arXiv) | POGEMA: A Benchmark Platform for Cooperative Multi-Agent Pathfinding | 2025-04 | 논문 | high | 2026-09-30 | https://arxiv.org/abs/2407.14931 | 아니오 |
| ref-623 | Agrawal, A., Bedi, A. S., & Manocha, D. (arXiv, ICRA 2023) | RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments | 2022-09 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2209.05738 | 아니오 |
| ref-1111 | Pookkuttath, S., Elara, M. R., Sivanantham, V., & Ramalingam, B. (Sensors) | AI-Enabled Predictive Maintenance Framework for Autonomous Mobile Cleaning Robots | 2021-12-21 | 논문 | high | 2026-09-30 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8747287/ | 아니오 |
| ref-1112 | Poskart, B., Iskierka, G., Krot, K., Burduk, R., Gwizdal, P., & Gola, A. (Sensors) | Multi-Parameter Predictive Model of Mobile Robot's Battery Discharge for Intelligent Mission Planning in Multi-Robot Systems | 2022-12-15 | 논문 | high | 2026-09-30 | https://pmc.ncbi.nlm.nih.gov/articles/PMC9786877/ | 아니오 |
| ref-1113 | 파이낸셜뉴스 | 현대차, '로봇 고장' AI로 잡는다…5일전 90%이상 감지 | 2026-05-28 | 기사 | low | 2026-09-30 | https://www.fnnews.com/news/202605280925297568 | 아니오 |
| ref-1114 | ISO (ISO/TC 108) | ISO 13381-1:2025 Condition monitoring and diagnostics of machine … — Prognostics — Part 1: General guidelines (제목 일부는 검색 결과 기준) | 2025 | 표준 | medium | 2026-09-30 | https://www.iso.org/standard/88029.html | 예 |
| ref-1115 | Elmachtoub, A. N., & Grigas, P. (arXiv, Management Science) | Smart "Predict, then Optimize" | 2017-10 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/1710.08005 | 아니오 |
| ref-1116 | Garces, D., Castro, S., Haimovich, A., Crowe, B., & Gil, S. (arXiv) | Model-Based Reinforcement Learning for Heterogeneous Multi-Robot Task Assignment Under Distribution Shifts | 2026-08 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2608.21554 | 아니오 |
| ref-1117 | CJ대한통운 | 'AI 혁신 기술'이 이끄는 CJ대한통운의 스마트 … (제목 일부만 확인) | 2021-07-28 | 벤더 문서 | medium | 2026-09-30 | https://www.cjlogistics.com/ko/newsroom/latest/LT_00000238 | 아니오 |
| ref-1118 | Zhang, Y., Jiang, H., Bhatt, V., Nikolaidis, S., & Li, J. (arXiv, IJCAI 2024) | Guidance Graph Optimization for Lifelong Multi-Agent Path Finding | 2024-02 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2402.01446 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f18(왜 중요한가), f17(핵심 질문 답, 추정) / 섹션 4: 결정 중심 학습 f11, 예지·예지 정비 f13·f15, 모방 학습 f4·f5, 안내 그래프 f6 / 섹션 5: 물류창고 — f1·f2(DeepFleet, 예외·성과는 벤더 주장 병기)·f16(수행 자원: 인력 배치, 연계 대상·벤더 주장 병기), 병원 — f8(시작 조건: 간호 업무 요청)·f9(수행 자원: 이력 기반 플릿 구성)·f10(예외·성과), 제조 공장 — f14(현대차 로봇팔 고장 예측, 벤더 주장 병기), 기타 — f13(대학 캠퍼스 청소 로봇 예지 정비). 상업 시설·가정·실외 사례는 찾지 못함을 명시 / 섹션 6: 학습 기반 배정 f7·f8·f9, 학습 기반 경로 f3~f6(학습 단독 대 탐색 결합 대비), 예측을 결정 기준으로 학습 f11, 배터리·고장 예측 f12~f14 / 섹션 7: POGEMA 벤치마크 f3, ISO 13381-1 f15(원문 미열람) / 섹션 8: f1·f3~f13 / 섹션 9: f19(직접 범위), f20(연계 대상) / 섹션 10: f21 — 23, 25, 26, 27, 28, 35, 38, 44, 47, 54, 57, 61, 62, 63, 67 / 섹션 11: open_questions_new 5건. 교차 규칙에 따라 25. 작업 배정 — MRTA 페이지에 f7·f8·f17, 27. 다중 로봇 경로·교통 관리 — MAPF 페이지에 f3~f6, 38. 모니터링·이상 탐지·원인 분석 페이지에 f13·f14 반영을 다음 실행 후보로 남긴다. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 결정 중심 학습 | Decision-Focused Learning (Smart Predict-then-Optimize) | 예측 모델을 예측 오차가 아니라 그 예측으로 푼 최적화 문제의 결정 손실이 작아지도록 학습하는 방법이다. |
| 예지 정비 | Predictive Maintenance | 설비·로봇의 상태 신호로 고장이나 성능 저하를 미리 예측해 고장 전에 정비 시점과 조치를 정하는 정비 방식이다. |
| 모방 학습 | Imitation Learning | 전문가(예: 탐색 기반 계획기)가 만든 해나 행동 기록을 정답으로 삼아 같은 결정을 흉내 내는 정책을 학습하는 방법이다. |
| 안내 그래프 | Guidance Graph | 지속형 다중 에이전트 경로 찾기에서 로봇이 지나는 격자 간선에 가중치를 매겨 교통 흐름을 유도하는 그래프로, 배치 전에 최적화하거나 학습된 모델로 생성한다. |

## 열린 질문

새로 생긴 질문:

- 학습 기반 배정·경로 정책을 실제 운영 중인 창고나 병원에 적용해 탐색·규칙 기반 방법 대비 개선을 제3자가 측정해 공개한 자료가 있는가? | 관련 영역: 46. 예측·학습 기반 최적화, 54. 시험·형식 검증·벤치마크 | 근거: f2 | 종류: 일반
- 제조사마다 다른 상태·고장 데이터를 내는 이종 로봇 플릿에서 고장 예측 모델을 학습·운영하려면 어떤 공통 데이터 항목이 필요하고 누가 모델을 소유하는가? | 관련 영역: 46. 예측·학습 기반 최적화, 38. 모니터링·이상 탐지·원인 분석 | 근거: f14 | 종류: 일반
- 학습된 배정·경로 정책을 현장에 쓸 때 분포 이동을 감지해 탐색·규칙 기반 정책으로 되돌리는 기준을 정한 연구나 제품이 있는가? | 관련 영역: 46. 예측·학습 기반 최적화, 47. AI·학습·적응과 모델 운영 | 근거: f9 | 종류: 일반
- 46. 예측·학습 기반 최적화의 수요 예측(작업 요청·물동량 예측)과 분류 원문 19장이 외부 연계로 둔 수요예측(상위 업무 시스템)의 경계를 어떻게 나눌 것인가? | 관련 영역: 46. 예측·학습 기반 최적화, 23. 업무 시스템 연동 | 근거: f16 | 종류: 일반
- 국내 물류창고·병원·공장에서 로봇 배정·경로에 강화학습·모방학습 같은 학습 기반 방법을 적용한 공개 사례나 연구가 있는가? | 관련 영역: 46. 예측·학습 기반 최적화, 61. 물류창고 | 근거: f16 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 14 · 교차 확인: 0
- 예산 사용량: 검색 17회 · 신규 출처 14건
- 미확인 항목:
    - f2 DeepFleet 효율 10% 개선: 아마존 자체 자료뿐이며 독립 출처로 교차 확인하지 못함
    - f14 현대차 고장 5일 전·정확도 90% 이상: 회사 발표를 전한 기사 1건뿐, 정확도 산정 방법 미확인
    - f15 ISO 13381-1:2025: ISO·SCC 페이지 403 으로 원문 미열람, 제목 끝부분과 범위는 검색 결과 요약 기준
    - f4 MAPF-GPT 데이터셋 크기·전문가 해법·지속형 MAPF 결과는 초록에 없어 미확인(검색 요약의 지속형 MAPF 제로샷 서술은 넣지 않음)
    - f3~f8·f11 은 초록(POGEMA 는 HTML 본문 결과 절) 기준이며 실험 세부 조건 미확인
    - f16 CJ대한통운 이커머스 주문량 예측 정확도 88%: 검색 요약에만 있고 연 자사 게시물에서 확인하지 못해 넣지 않음
    - Malus 외 다중 에이전트 강화학습 AMR 주문 배차(CIRP Annals 2020, 제조 공장): ScienceDirect 403 으로 넣지 않음
    - ACM Computing Surveys 다중 로봇 작업 배정 체계적 문헌 고찰(2024): ACM 403 으로 넣지 않음
    - 상업 시설·가정·실외 현장의 학습·예측 적용 사례는 찾지 못함(보도 배달 로봇 수요 예측 검색 1회에서 적합한 1차 자료 없음)
    - 국내 학술지의 강화학습 기반 다중 로봇 배정·경로 논문은 검색 1회에서 찾지 못함
- 범위 경계 위반 의심:
    - f13·f14: 로봇 부품 수준 진동·전류 기반 고장 감지는 로봇 제조사·설비 정비 쪽 기법이므로 예측 결과를 정비 계획에 쓰는 근거로만 제안하고, 경계는 f20 에서 '연계 대상: '으로 구분함
    - f16: 전사 주문 수요예측은 분류 원문 19장의 상위 업무 시스템 연계 대상이므로 claim 을 '연계 대상: '으로 시작함. 46번 정의의 '수요·고장 예측'과의 경계는 열린 질문으로 올림
    - f1·f2: DeepFleet 의 미래 교통 예측은 운영 결정용 예측으로 다루며 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험)이나 18. 실시간 세계 상태·데이터 일관성(현재 상태 표현)과 섞지 않음
- 한계: web_fetch_available: true · fetch_mode full. 검색 17회/30, 신규 출처 14건/15(ref-1105~ref-1118, 예약 구간 안). 재사용 출처 없음(입력의 참고문헌 요약에 이 영역 인용 0건). 원문 열람: 13건 webfetch 로 열었고 ISO 13381-1(ref-1114)만 403 으로 못 열어 source_unopened 로 표시했다. 논문 가운데 Pookkuttath 외(ref-1111)·Poskart 외(ref-1112)는 PMC 본문, POGEMA(ref-1109)는 HTML 본문 결과 절, 나머지는 초록 페이지다. 교차 확인 0건: 핵심 수치가 모두 단일 출처라 finding 신뢰도는 medium 이하로 두었다. 벤더·회사 발표만 근거로 한 f2·f14·f16 은 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈다. 분류 원문 핵심 질문(학습과 예측이 배정·경로·정비 결정을 실제로 개선하는가)에는 f17 로 답했고 결론은 '개선 근거는 주로 시뮬레이션·벤치마크이고 운영 수치는 벤더 주장이며, 학습 단독보다 탐색·최적화와 결합하거나 결정 손실로 학습하는 설계에서 개선이 보고된다'는 추정이다. 현장 유형 사례는 물류창고(f1·f2·f16)·병원(f8~f10)·제조 공장(f14)·기타(f13, 대학 캠퍼스)이며 상업 시설·가정·실외는 찾지 못했다. 국내 자료는 파이낸셜뉴스(ref-1113)·CJ대한통운(ref-1117) 두 건이고 국내 학술·표준 자료는 찾지 못했다. L. AI·학습 기술 교차 규칙에 따라 학습 기반 배정은 25. 작업 배정 — MRTA, 경로는 27. 다중 로봇 경로·교통 관리 — MAPF, 고장 예측은 38. 모니터링·이상 탐지·원인 분석과 함께 연결하도록 제안했다. 용어집에 이미 있는 상태 기반 정비·현실 격차·지속형 MAPF·MRTA·충전 상태·배터리 건강 상태는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 없음.
```

### data/source_texts/ref-009.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

````text
---
layout: default
title: ROS 2 DDS-Security integration
permalink: articles/ros2_dds_security.html
abstract: >
  Robotics is full of experimentation: evaluating different hardware and software, pushing ahead with what works, and culling what doesn't.
  ROS was designed to be flexible to enable this experimentation; to allow existing components to easily be combined with new ones or swapped with others.
  In ROS 1, this flexibility was valued above all else, at the cost of security.
  By virtue of being designed on top of DDS, ROS 2 is able to retain that flexibility while obtaining the ability to be secured by properly utilizing the DDS-Security specification.
  This article describes how ROS 2 integrates with DDS-Security.
author:  >
  [Kyle Fazzari](https://github.com/kyrofa)
date_written: 2019-07
last_modified: 2020-07
published: true
categories: Security
---

{:toc}

# {{ page.title }}

<div class="abstract" markdown="1">
{{ page.abstract }}
</div>

Authors: {{ page.author }}

Date Written: {{ page.date_written }}

Last Modified: {% if page.last_modified %}{{ page.last_modified }}{% else %}{{ page.date_written }}{% endif %}

# DDS-Security overview

The [DDS-Security specification][dds_security] expands upon the [DDS specification][dds], adding security enhancements by defining a Service Plugin Interface (SPI) architecture, a set of builtin implementations of the SPIs, and the security model enforced by the SPIs.
Specifically, there are five SPIs defined:

- **Authentication**: Verify the identity of a given domain participant.
- **Access control**: Enforce restrictions on the DDS-related operations that can be performed by an authenticated domain participant.
- **Cryptographic**: Handle all required encryption, signing, and hashing operations.
- **Logging**: Provide the ability to audit DDS-Security-related events.
- **Data tagging**: Provide the ability to add tags to data samples.

ROS 2's security features currently utilize only the first three.
This is due to the fact that neither **Logging** nor **Data Tagging** are required in order to be compliant with the [DDS-Security spec][dds_security] (see section 2.3), and thus not all DDS implementations support them.
Let's delve a little further into those first three plugins.

## Authentication

The **Authentication** plugin (see section 8.3 of the [DDS-Security spec][dds_security]) is central to the entire SPI architecture, as it provides the concept of a confirmed identity without which further enforcement would be impossible (e.g. it would be awfully hard to make sure a given ROS identity could only access specific topics if it was impossible to securely determine which identity it was).

The SPI architecture allows for a number of potential authentication schemes, but ROS 2 uses the builtin authentication plugin (called "DDS:Auth:PKI-DH", see section 9.3 of the [DDS-Security spec][dds_security]), which uses the proven Public Key Infrastructure (PKI).
It requires a public and private key per domain participant, as well as an x.509 certificate that binds the participant's public key to a specific name.
Each x.509 certificate must be signed by (or have a signature chain to) a specific Certificate Authority (CA) that the plugin is configured to trust.

The rationale for using the builtin plugin as opposed to anything else is twofold:

1. It's the only approach described in detail by the spec.
2. It's mandatory for all compliant DDS implementations to interoperably support it (see section 2.3 of the [DDS-Security spec][dds_security]), which makes the ROS 2 security features work across vendors with minimal effort.

## Access control

The **Access control** plugin (see section 8.4 of the [DDS-Security spec][dds_security]) deals with defining and enforcing restrictions on the DDS-related capabilities of a given domain participant.
For example, it allows a user to restrict a particular participant to a specific DDS domain, or only allow the participant to read from or write to specific DDS topics, etc.

Again the SPI architecture allows for some flexibility in how the plugins accomplish this task, but ROS 2 uses the builtin access control plugin (called "DDS:Access:Permission", see section 9.4 of the [DDS-Security spec][dds_security]), which again uses PKI.
It requires two files per domain participant:

- **Governance** file: A signed XML document specifying how the domain should be secured.
- **Permissions** file: A signed XML document containing the permissions of the domain participant, bound to the name of the participant as defined by the authentication plugin (which is done via an x.509 cert, as we just discussed).

Both of these files must be signed by a CA which the plugin is configured to trust.
This may be the same CA that the **Authentication** plugin trusts, but that isn't required.

The rationale for using the builtin plugin as opposed to anything else is the same as the **Authentication** plugin:

1. It's the only approach described in detail by the spec.
2. It's mandatory for all compliant DDS implementations to interoperably support it (see section 2.3 of the [DDS-Security spec][dds_security]), which makes the ROS 2 security features work across vendors with minimal effort.

## Cryptographic

The **Cryptographic** plugin (see section 8.5 of the [DDS-Security spec][dds_security]) is where all the cryptography-related operations are handled: encryption, decryption, signing, hashing, etc.
Both the **Authentication** and **Access control** plugins utilize the capabilities of the **Cryptographic** plugin in order to verify signatures, etc.
This is also where the functionality to encrypt DDS topic communication resides.

While the SPI architecture again allows for a number of possibilities, ROS 2 uses the builtin cryptographic plugin (called "DDS:Crypto:AES-GCM-GMAC", see section 9.5 of the [DDS-Security spec][dds_security]), which provides authenticated encryption using Advanced Encryption Standard (AES) in Galois Counter Mode (AES-GCM).

The rationale for using the builtin plugin as opposed to anything else is the same as the other plugins:

1. It's the only approach described in detail by the spec.
2. It's mandatory for all compliant DDS implementations to interoperably support it (see section 2.3 of the [DDS-Security spec][dds_security]), which makes the ROS 2 security features work across vendors with minimal effort.

# DDS-Security integration with ROS 2: SROS 2

Now that we have established some shared understanding of how security is supported in DDS, let's discuss how that support is exposed in ROS 2.
By default, none of the security features of DDS are enabled in ROS 2.
The set of features and tools in ROS 2 that are used to enable them are collectively named "Secure ROS 2" (SROS 2).

## Features in the ROS client library (RCL)

Most of the user-facing runtime support for SROS 2 is contained within the [ROS Client Library](https://github.com/ros2/rcl).
Once its requirements are satisfied it takes care of configuring the middleware support for each supported DDS implementation.
RCL includes the following features for SROS 2:

- Support for security files for each domain participant.
- Support for both permissive and strict enforcement of security.
- Support for a master "on/off" switch for all SROS 2 features.

Let's discuss each of these in turn.

### Security files for each domain participant

As stated earlier, the DDS-Security plugins require a set of security files (e.g. keys, governance and permissions files, etc.) per domain participant.
Domain participants map to a context within process in ROS 2, so each process requires a set of these files.
RCL supports being pointed at a directory containing security files in two different ways:

- Directory tree of all security files.
- Manual specification.

Let's delve further into these.

#### Directory tree of all security files

RCL supports finding security files in one directory that is inside the reserved `enclaves` subfolder, within the root keystore, corresponding to the fully-qualified path of every enclave.
For example, for the `/front/camera` enclave, the directory structure would look like:

    <root>
    ├── enclaves
    │   └── front
    │       └── camera
    │           ├── cert.pem
    │           ├── key.pem
    │           ├── ...
    └── public
        ├── ...

The set of files expected within each enclave instance directory are:

- **identity_ca.cert.pem**: The x.509 certificate of the CA trusted by the **Authentication** plugin (the "Identity" CA).
- **cert.pem**: The x.509 certificate of this enclave instance (signed by the Identity CA).
- **key.pem**: The private key of this enclave instance.
- **permissions_ca.cert.pem**: The x.509 certificate of the CA trusted by the **Access control** plugin (the "Permissions" CA).
- **governance.p7s**: The XML document that specifies to the **Access control** plugin how the domain should be secured  (signed by the Permissions CA).
- **permissions.p7s**: The XML document that specifies the permissions of this particular enclave instance to the **Access control** plugin (also signed by the Permissions CA).

This can be specified by setting the `ROS_SECURITY_KEYSTORE` environment variable to point to the root of the keystore directory tree, and then specifying the enclave path using the `--ros-args` runtime argument `-e`, `--enclave`, e.g.:

``` shell
export ROS_SECURITY_KEYSTORE="/home/bob/.ros/sros2_keystore"
ros2 run <package> <executable> --ros-args --enclave="/front/camera"
```

#### Manual specification

RCL also supports specifying the enclave path for the process that needs to be launched using an overriding environmental variable.
This can be done by setting the `ROS_SECURITY_ENCLAVE_OVERRIDE` environment variable to an alternate enclave path within the keystore.
Note that this setting takes precedence over `ROS_SECURITY_KEYSTORE` with `--enclave`.

Note that the following two examples load from the same enclave path as demonstrated prior:

``` shell
export ROS_SECURITY_KEYSTORE="/home/bob/.ros/sros2_keystore"
export ROS_SECURITY_ENCLAVE_OVERRIDE="/front/camera"
ros2 run <package> <executable>
```

``` shell
export ROS_SECURITY_KEYSTORE="/home/bob/.ros/sros2_keystore"
export ROS_SECURITY_ENCLAVE_OVERRIDE="/front/camera"
ros2 run <package> <executable> --ros-args --enclave="/spam"
```

### Support for both permissive and strict enforcement of security

Participants with the security features enabled will not communicate with participants that don't, but what should RCL do if one tries to launch a participant that has no discernable enclave with keys/permissions/etc.? It has two options:

- **Permissive mode**: Try to find security files, and if they can't be found, launch the participant without enabling any security features.
This is the default behavior.
- **Strict mode**: Try to find security files, and if they can't be found, fail to run the participant.

The type of mode desired can be specified by setting the `ROS_SECURITY_STRATEGY` environment variable to "Enforce" (case-sensitive) for strict mode, and anything else for permissive mode.

### Support for a master "on/off" switch for all SROS 2 features

In addition to the supported features just discussed, RCL also supports a master shutoff for security features for easy experimentation.
If it's turned off (the default), none of the above security features will be enabled.

In order to enable SROS 2, set the `ROS_SECURITY_ENABLE` environment variable to "true" (case-sensitive).
To disable, set to any other value.

## Features in the SROS 2 CLI

Configuring a ROS 2 system to be secure in RCL involves a lot of new technology (PKI, DDS governance and permissions files and their syntax, etc.).
If a user is comfortable with these technologies, the above information should be all that's necessary to properly lock things down.
However, the [SROS 2 CLI](https://github.com/ros2/sros2) should include a tool `ros2 security` to help those who don't want to set it all up themselves, including the following capabilities:

- Create Identity and Permissions CA.
- Create directory tree containing all security files.
- Create a new identity for a given enclave, generating a keypair and signing its x.509 certificate using the Identity CA.
- Create a governance file that will encrypt all DDS traffic by default.
- Support specifying enclave permissions [in familiar ROS terms](/articles/ros2_access_control_policies.html) which are then automatically converted into low-level DDS permissions.
- Support automatically discovering required permissions from a running ROS system.

[dds_security]: https://www.omg.org/spec/DDS-SECURITY/1.1/PDF
[dds]: https://www.omg.org/spec/DDS/1.4/PDF
````

### data/source_texts/ref-010.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
---
layout: default
title: ROS 2 Robotic Systems Threat Model
permalink: articles/ros2_threat_model.html
abstract:
  This document describes security concerns robotic systems built using ROS 2
  may face.
  The first section describes potential threats to ROS 2 systems.
  The second section describes potential attacks and mitigations on a reference
  platform (TurtleBot 3).
  The third covers potential attacks, mitigations and some preliminary results in an industrial
  reference platform (MARA modular robot).
author: >
  [Thomas Moulard](https://github.com/thomas-moulard),
  [Juan Hortala](https://github.com/juanrh)
  [Xabi Perez](https://github.com/XabierPB)
  [Gorka Olalde](https://github.com/olaldiko)
  [Borja Erice](https://github.com/borkenerice)
  [Odei Olalde](https://github.com/o-olalde)
  [David Mayoral](https://github.com/dmayoral)
date_written: 2019-03
last_modified: 2021-01
published: true
categories: Security
---

{:toc}

{::options parse_block_html="true" /}

<style>
table {
    table-layout: fixed;
    width: 100%;
}

th {
    width: 11em;
}
</style>

# {{ page.title }}

Authors: {{ page.author }}

Date Written: {{ page.date_written }}

Last Modified: {% if page.last_modified %}{{ page.last_modified }}{% else %}{{ page.date_written }}{% endif %}

This is a **DRAFT DOCUMENT**.

<div class="alert alert-warning" markdown="1">
**Disclaimer**:

* This document is not exhaustive.
  Mitigating all attacks in this document does not ensure any robotic product is secure.
* This document is a live document.
  It will continue to evolve as we implement and mitigate attacks against reference platforms.

</div>

## Table of Contents

* [{{ page.title }}](#pagetitle)
  * [Table of Contents](#table-of-contents)
  * [Document Scope](#document-scope)
  * [Robotic Systems Threats Overview](#robotic-systems-threats-overview)
    * [Defining Robotic Systems Threats](#defining-robotic-systems-threats)
    * [Robot Application Actors, Assets, and Entry Points](#robot-application-actors-assets-and-entry-points)
      * [Robot Application Actors](#robot-application-actors)
      * [Assets](#assets)
      * [Entry Points](#entry-points)
    * [Robot Application Components and Trust Boundaries](#robot-application-components-and-trust-boundaries)
    * [Threat Analysis and Modeling](#threat-analysis-and-modeling)
    * [Including a new robot into the threat model](#including-a-new-robot-into-the-threat-model)
  * [Threat Analysis for the `TurtleBot 3` Robotic Platform](#threat-analysis-for-the-turtlebot-3-robotic-platform)
    * [System description](#system-description)
    * [Architecture Dataflow diagram](#architecture-dataflow-diagram)
      * [Assets](#assets-1)
        * [Hardware](#hardware)
        * [Processes](#processes)
        * [Software Dependencies](#software-dependencies)
        * [External Actors](#external-actors)
        * [Robot Data Assets](#robot-data-assets)
      * [Entry points](#entry-points)
      * [Use case scenarios](#use-case-scenarios)
      * [Threat model](#threat-model)
      * [Threat Diagram: An attacker deploys a malicious node on the robot](#threat-diagram-an-attacker-deploys-a-malicious-node-on-the-robot)
      * [Attack Tree](#attack-tree)
    * [Threat Model Validation Strategy](#threat-model-validation-strategy)
  * [Threat Analysis for the `MARA` Robotic Platform](#threat-analysis-for-the-mara-robotic-platform)
    * [System description](#system-description-1)
    * [Architecture Dataflow diagram](#architecture-dataflow-diagram-1)
      * [Assets](#assets-2)
        * [Hardware](#hardware-1)
        * [Network](#network)
        * [Software processes](#software-processes)
        * [Software dependencies](#software-dependencies)
        * [External Actors](#external-actors-1)
        * [Robot Data assets](#robot-data-assets)
      * [Use case scenarios](#use-case-scenarios-1)
      * [Entry points](#entry-points-1)
      * [Trust Boundaries for MARA in `pick & place` application](#trust-boundaries-for-mara-in-pick--place-application)
    * [Threat Model](#threat-model)
      * [Attack Trees](#attack-trees)
      * [Physical vector attack tree](#physical-vector-attack-tree)
      * [ROS 2 API vector attack tree](#ros2-api-vector-attack-tree)
      * [H-ROS API vector attack tree](#h-ros-api-vector-attack-tree)
      * [Code repository compromise vector attack tree](#code-repository-compromise-vector-attack-tree)
    * [Threat Model Validation Strategy](#threat-model-validation-strategy-1)
    * [Security Assessment preliminary results](#security-assessment-preliminary-results)
      * [Introduction](#introduction)
      * [Results](#results)
        * [Findings](#findings)
  * [References](#references)

## Document Scope

This document describes potential threats for ROS 2 robotic systems.
The document is divided into two parts:

1. Robotic Systems Threats Overview
1. Threat Analysis for the TurtleBot 3 Robotic Platform
1. Threat Analysis for the MARA Robotic Platform

The first section lists and describes threats from a theoretical point of view.
Explanations in this section should hold for any robot built using a
component-oriented architecture.
The second section instantiates those threats on a widely-available reference platform, the
TurtleBot 3.
Mitigating threats on this platform enables us to demonstrate the viability of our recommendations.

## Robotic Systems Threats Overview

<div class="alert alert-info" markdown="1">
This section is intentionally independent from ROS as robotic systems
share common threats and potential vulnerabilities.
For instance, this section describes "robotic components" while the next section will mention
"ROS 2 nodes".
</div>

### Defining Robotic Systems Threats

We will consider as a robotic system one or more general-purpose computers
connected to one or more actuators or sensors.
An actuator is defined as any device producing physical motion.
A sensor is defined as any device capturing or recording a physical property.

### Robot Application Actors, Assets, and Entry Points

This section defines actors, assets, and entry points for this threat model.

**Actors** are humans or external systems interacting with the robot.
Considering which actors interact with the robot is helpful to determine how the system
can be compromised.
For instance, actors may be able to give commands to the robot which may be abused to attack the
system.

**Assets** represent any user, resource (e.g. disk space), or property (e.g. physical
safety of users) of the system that should be defended against attackers.
Properties of assets can be related to achieving the business goals of the robot.
For example, sensor data is a resource/asset of the system and the privacy of that
data is a system property and a business goal.

**Entry points** represent how the system is interacting with the world (communication
channels, API, sensors, etc.).

#### Robot Application Actors

Actors are divided into multiple categories based on whether or not they are
physically present next to the robot (could the robot harm them?), are they
human or not and are they a "power user" or not.
A power user is defined as someone who is knowledgeable and executes tasks which are normally
not done by end-users (build and debug new software, deploy code, etc.).

<div class="table">
<table class="table">
  <thead>
    <th style="width: 7em">Actor</th>
    <th style="width: 3.3em">Co-Located?</th>
    <th style="width: 2.5em">Human?</th>
    <th style="width: 3.3em">Power User?</th>
    <th style="width: 10em">Notes</th>
  </thead>
  <tr>
    <td>Robot User</td>
    <td class="success">Y</td>
    <td class="success">Y</td>
    <td class="danger">N</td>
    <td>Human interacting physically with the robot.</td>
  </tr>
  <tr>
    <td>Robot Developer / Power User</td>
    <td class="success">Y</td>
    <td class="success">Y</td>
    <td class="success">Y</td>
    <td>User with robot administrative access or developer.</td>
  </tr>
  <tr>
    <td>Third-Party Robotic System</td>
    <td class="success">Y</td>
    <td class="danger">N</td>
    <td class="warning">-</td>
    <td>Another robot or system capable of physical interaction with the robot.
    </td>
  </tr>
  <tr>
    <td> Teleoperator / Remote User </td>
    <td class="danger">N</td>
    <td class="success">Y</td>
    <td class="danger">N</td>
    <td>A human tele-operating the robot or sending commands to it through a
        client application (e.g. smartphone app) </td>
  </tr>
  <tr>
    <td>Cloud Developer</td>
    <td class="danger">N</td>
    <td class="success">Y</td>
    <td class="success">Y</td>
    <td>A developer building a cloud service connected to the robot or an
        analyst who has been granted access to robot data.</td>
  </tr>
  <tr>
    <td> Cloud Service </td>
    <td class="danger">N</td>
    <td class="danger">N</td>
    <td class="warning">-</td>
    <td>A service sending commands to the robot automatically (e.g. cloud
        motion planning service)</td>
  </tr>
</table>
</div>

#### Assets

Assets are categorized in privacy (robot private data should not
be accessible by attackers), integrity (robot behavior should not be modified
by attacks) and availability (robot should continue to operate even under
attack).

<div class="table">
<table class="table">
  <thead>
    <th>Asset</th>
    <th>Description</th>
  </thead>

  <tr><th colspan="2">Privacy</th></tr>
  <tr>
    <td>Sensor Data Privacy</td>
    <td>Sensor data must not be accessed by unauthorized actors.</td>
  </tr>
  <tr>
    <td>Robot Data Stores Privacy</td>
    <td>Robot persistent data (logs, software, etc.) must not be accessible by
        unauthorized actors.</td>
  </tr>

  <tr><th colspan="2">Integrity</th></tr>
  <tr>
    <td>Physical Safety</td>
    <td>The robotic system must not harm its users or environment.</td>
  </tr>
  <tr>
    <td>Robot Integrity</td>
    <td>The robotic system must not damage itself.</td>
  </tr>
  <tr>
    <td>Robot Actuators Command Integrity</td>
    <td>Unallowed actors should not be able to control the robot actuators.</td>
  </tr>
  <tr>
    <td>Robot Behavior Integrity</td>
    <td>The robotic system must not allow attackers to disrupt its tasks.</td>
  </tr>
  <tr>
    <td>Robot Data Stores Integrity</td>
    <td>No attacker should be able to alter robot data.</td>
  </tr>

  <tr><th colspan="2">Availability</th></tr>
  <tr>
    <td>Compute Capabilities</td>
    <td>Robot embedded and distributed (e.g. cloud) compute resources.
    Starving a robot from its compute resources can prevent it from operating
    correctly.
    </td>
  </tr>
  <tr>
    <td>Robot Availability</td>
    <td>The robotic system must answer commands in a reasonable time.</td>
  </tr>
  <tr>
    <td>Sensor Availability</td>
    <td>Sensor data must be available to allowed actors shortly after being
    produced.</td>
  </tr>
</table>
</div>

#### Entry Points

Entry points describe the system attack surface area (how do actors interact
with the system?).

<div class="table">
<table class="table">
  <thead>
    <th>Name</th>
    <th>Description</th>
  </thead>
  <tr>
    <td>Robot Components Communication Channels</td>
    <td>Robotic applications are generally composed of multiple components
    talking over a shared bus.
    This bus may be accessible over the robot WAN link.</td>
  </tr>
  <tr>
    <td>Robot Administration Tools</td>
    <td>Tools allowing local or remote users to connect to the robot
    computers directly (e.g. SSH, VNC).</td>
  </tr>
  <tr>
    <td>Remote Application Interface</td>
    <td>Remote applications (cloud, smartphone application, etc.) can be
    used to read robot data or send robot commands (e.g. cloud REST API,
    desktop GUI, smartphone application).</td>
  </tr>
  <tr>
    <td>Robot Code Deployment Infrastructure</td>
    <td>Deployment infrastructure for binaries or configuration files are
    granted read/write access to the robot computer's filesystems.</td>
  </tr>
  <tr>
    <td>Sensors</td>
    <td>Sensors are capturing data which usually end up being injected into
    the robot middleware communication channels.</td>
  </tr>
  <tr>
    <td>Embedded Computer Physical Access</td>
    <td>External (HDMI, USB...) and internal (PCI Express, SATA...) ports.</td>
  </tr>
</table>
</div>

### Robot Application Components and Trust Boundaries

The system is divided into hardware (embedded general-purpose computer,
sensors, actuators), multiple components
(usually processes) running on multiple computers (trusted or non-trusted
components) and data stores (embedded or in the cloud).

While the computers may run well-controlled, trusted software (trusted
components), other off-the-shelf robotics components (non-trusted) nodes may be
included in the application.
Third-party components may be malicious (extract private data, install a root-kit, etc.) or their
QA validation process may not be as extensive as in-house software.
Third-party components releasing process create additional security threats (third-party component
may be compromised during their distribution).

A trusted robotic component is defined as a node developed, built, tested and
deployed by the robotic application owner or vetted partners.
As the process is owned end-to-end by a single organization, we can assume that the node will
respect its specifications and will not, for instance, try to extract and leak private information.
While carefully controlled engineering processes can reduce the risk of malicious behavior
(accidentally or voluntarily), it cannot completely eliminate it.
Trusted nodes can still leak private data, etc.

Trusted nodes should not trust non-trusted nodes.
It is likely that more than one non-trusted component is embedded in any given robotic application.
It is important for non-trusted components to not trust each other as one malicious non-trusted
node may try to compromise another non-trusted node.

An example of a trusted component could be an in-house (or carefully vetted) IMU
driver node.
This component may communicate through unsafe channels with other
driver nodes to reduce sensor data fusion latency.
Trusting components is never ideal but it may be acceptable if the software is well-controlled.

On the opposite, a non-trusted node can be a third-party object tracker.
Deploying this node without adequate sandboxing could impact:

* User privacy: the node is streaming back user video without their consent
* User safety: the robot is following the object detected by the tracker and its
  speed is proportional to the object distance.
  The malicious tracker estimates
  the object position very far away on purpose to trick the robot into suddenly
  accelerating and hurting the user.
* System availability: the node may try to consume all available computing
  resources (CPU, memory, disk) and prevent the robot from performing correctly.
* System Integrity: the robot is following the object detected by the tracker.
  The attacker can tele-operate the robot by controlling the estimated position
  of the tracked object (detect an object on the left to make the robot move to
  the left, etc.).

Nodes may also communicate with the local filesystem, cloud services or data stores.
Those services or data stores can be compromised and should not be automatically trusted.
For instance, URDF robot models are usually stored in the robot file system.
This model stores robot joint limits.
If the robot file system is compromised, those limits could be removed which would enable an
attacker to destroy the robot.

Finally, users may try to rely on sensors to inject malicious data into the
system ([Akhtar, Naveed, and Ajmal Mian. “Threat of Adversarial Attacks on
Deep Learning in Computer Vision: A Survey.”][akhtar_threat_2018]).

The diagram below illustrates an example application with different trust zones
(trust boundaries showed with dashed green lines).
The number and scope of trust zones is depending on the application.

![Robot System Threat Model](ros2_threat_model/RobotSystemThreatModel.png)
[Diagram Source](ros2_threat_model/RobotSystemThreatModel.json)
(edited with [Threat Dragon][threat_dragon])

### Threat Analysis and Modeling

The table below lists all *generic* threats which may impact a
robotic application.

Threat categorization is based on the [STRIDE][wikipedia_stride]
 (Spoofing / Tampering / Repudiation / Integrity / Denial of service
 / Elevation of privileges) model.
Risk assessment relies on [DREAD][wikipedia_dread] (Damage / Reproducibility /
 Exploitability / Affected users / Discoverability).

In the following table, the "Threat Category (STRIDE)" columns indicate the categories to which a
threat belongs.
If the "Spoofing" column is marked with a check sign (✓), it means that this threat can be used to
spoof a component of the system.
If it cannot be used to spoof a component, a cross sign will be present instead (✘).

The "Threat Risk Assessment (DREAD)" columns contain a score indicating how easy or likely it is
for a particular threat to be exploited.
The allowed score values are 1 (not at risk), 2 (may be at risk) or 3 (at risk, needs to
be mitigated).
For instance, in the damage column a 1 would mean "exploitation of the threat would cause minimum
damages", 2 "exploitation of the threat would cause significant damages" and 3 "exploitation of
the threat would cause massive damages".
The "total score" is computed by adding the score of each column.
The higher the score, the more critical the threat.

Impacted assets, entry points and business goals columns indicate whether an asset, entry point or
business goal is impacted by a given threat.
A check sign (✓) means impacted, a cross sign (✘) means not impacted.
A triangle (▲) means "impacted indirectly or under certain conditions".
For instance, compromising the robot kernel may not be enough to steal user data but it makes
stealing data much easier.

<div class="table" markdown="1">
  <table class="table">
    <tr>
      <th rowspan="2" style="width: 20em">Threat Description</th>
      <th colspan="6">Threat Category (STRIDE)</th>
      <th colspan="6">Threat Risk Assessment (DREAD)</th>
      <th colspan="7">Impacted Assets</th>
      <th colspan="5">Impacted Entry Points</th>
      <th rowspan="2" style="width: 30em">Mitigation Strategies</th>
      <th rowspan="2" style="width: 30em">Similar Attacks in the Litterature</th>
    </tr>
    <tr style="height: 13em; white-space: nowrap;">
      <th style="transform: rotate(-90deg) translateX(-5em) translateY(5em)">Spoofing</th>
      <th style="transform: rotate(-90deg) translateX(-5em) translateY(5em)">Tampering</th>
      <th style="transform: rotate(-90deg) translateX(-5em) translateY(5em)">Repudiation</th>
      <th style="transform: rotate(-90deg) translateX(-5em) translateY(5em)">Info. Disclosure</th>
      <th style="transform: rotate(-90deg) translateX(-5em) translateY(5em)">Denial of Service</th>
      <th style="transform: rotate(-90deg) translateX(-5em) translateY(5em)">Elev. of Privileges</th>
      <th style="transform: rotate(-90deg) translateX(-5em) translateY(5em)">Damage</th>
      <th style="transform: rotate(-90deg) translateX(-5em) translateY(5em)">Reproducibility</th>
      <th style="transform: rotate(-90deg) translateX(-5em) translateY(5em)">Exploitability</th>
      <th style="transform: rotate(-90deg) translateX(-5em) translateY(5em)">Affected Users</th>
      <th style="transform: rotate(-90deg) translateX(-5em) translateY(5em)">Discoverability</th>
      <th style="transform: rotate(-90deg) translateX(-5em) translateY(5em)">DREAD Score</th>
      <th style="transform: rotate(-90deg) translateX(-5em) translateY(5em)">Robot Compute Rsc.</th>
      <th style="transform: rotate(-90deg) translateX(-5em) translateY(5em)">Physical Safety</th>
      <th style="transform: rotate(-90deg) translateX(-5em) translateY(5em)">Robot Avail.</th>
      <th style="transform: rotate(-90deg) translateX(-5em) translateY(5em)">Robot Integrity</th>
      <th style="transform: rotate(-90deg) translateX(-5em) translateY(5em)">Data
Integrity</th>
      <th style="transform: rotate(-90deg) translateX(-5em) translateY(5em)">Data
Avail.</th>
      <th style="transform: rotate(-90deg) translateX(-5em) translateY(5em)">Data
Privacy</th>
      <th style="transform: rotate(-90deg) translateX(-5em) translateY(5em)">Embedded H/W</th>
      <th style="transform: rotate(-90deg) translateX(-5em) translateY(5em)">Robot Comm. Channels</th>
      <th style="transform: rotate(-90deg) translateX(-5em) translateY(5em)">Robot Admin. Tools</th>
      <th style="transform: rotate(-90deg) translateX(-5em) translateY(5em)">Remote App. Interface</th>
      <th style="transform: rotate(-90deg) translateX(-5em) translateY(5em)">Deployment Infra.</th>
      <th></th>
    </tr>
    <tr>
      <th colspan="29">Embedded / Software / Communication / Inter-Component
Communication</th>
    </tr>
    <tr>
      <td>An attacker spoofs a component identity.</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">3</td>
      <td class="success">1</td>
      <td class="success">1</td>
      <td class="warning">2</td>
      <td class="danger">3</td>
      <td>10</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td>
        <ul>
          <li>Components should authenticate themselves.</li>
          <li>Components should not be attributed similar identifiers.</li>
          <li>Component identifiers should be chosen carefully.</li>
        </ul>
      </td>
      <td>
        <a href="http://arxiv.org/abs/1504.04339">Bonaci, Tamara, Jeffrey
    Herron, Tariq Yusuf, Junjie Yan, Tadayoshi Kohno, and Howard Jay Chizeck. “To
    Make a Robot Secure: An Experimental Analysis of Cyber Security Threats Against
    Teleoperated Surgical Robots.” ArXiv:1504.04339 [Cs], April 16, 2015.</a>
      </td>
    </tr>
    <tr>
      <td>An attacker intercepts and alters a message.</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td>15</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="warning">▲</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td>
        <ul>
          <li>Messages should be signed and/or encrypted.</li>
        </ul>
      </td>
      <td>
        <a href="http://arxiv.org/abs/1504.04339">Bonaci, Tamara, Jeffrey
    Herron, Tariq Yusuf, Junjie Yan, Tadayoshi Kohno, and Howard Jay Chizeck. “To
    Make a Robot Secure: An Experimental Analysis of Cyber Security Threats Against
    Teleoperated Surgical Robots.” ArXiv:1504.04339 [Cs], April 16, 2015.</a>
      </td>
    </tr>
    <tr>
      <td>An attacker writes to a communication channel without
    authorization.</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td>15</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td>
        <ul>
          <li>Components should only communicate on encrypted channels.</li>
          <li>Sensitive inter-process communication should be done through shared
        memory whenever possible.</li>
        </ul>
      </td>
      <td>
        <a href="http://arxiv.org/abs/1504.04339">Bonaci, Tamara, Jeffrey
    Herron, Tariq Yusuf, Junjie Yan, Tadayoshi Kohno, and Howard Jay Chizeck. “To
    Make a Robot Secure: An Experimental Analysis of Cyber Security Threats Against
    Teleoperated Surgical Robots.” ArXiv:1504.04339 [Cs], April 16, 2015.</a>
      </td>
    </tr>
    <tr>
      <td>An attacker listens to a communication channel without
authorization.</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="warning">2</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td>14</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td>
        <ul>
          <li>Components should only communicate on encrypted channels.</li>
          <li>Sensitive inter-process communication should be done through shared
memory whenever possible.</li>
        </ul>
      </td>
      <td>
        <a href="http://arxiv.org/abs/1504.04339">Bonaci, Tamara, Jeffrey
    Herron, Tariq Yusuf, Junjie Yan, Tadayoshi Kohno, and Howard Jay Chizeck. “To
    Make a Robot Secure: An Experimental Analysis of Cyber Security Threats Against
    Teleoperated Surgical Robots.” ArXiv:1504.04339 [Cs], April 16, 2015.</a>
      </td>
    </tr>
    <tr>
      <td>An attacker prevents a communication channel from being usable.</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td>15</td>
      <td class="success">✓</td>
      <td class="warning">▲</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td>
        <ul>
          <li>Components should only be allowed to access channels they
require.</li>
          <li>Internet-facing channels and robot-only channels should be
isolated.</li>
          <li>Components behaviors should be tolerant of a loss of communication
(e.g. go to x,y vs set velocity to vx, vy).</li>
        </ul>
      </td>
      <td>
        <a href="http://arxiv.org/abs/1504.04339">Bonaci, Tamara, Jeffrey
Herron, Tariq Yusuf, Junjie Yan, Tadayoshi Kohno, and Howard Jay Chizeck. “To
Make a Robot Secure: An Experimental Analysis of Cyber Security Threats Against
Teleoperated Surgical Robots.” ArXiv:1504.04339 [Cs], April 16, 2015.</a>
      </td>
    </tr>
    <tr>
      <th colspan="29">Embedded / Software / Communication / Long-Range
Communication (e.g. WiFi, Cellular Connection)</th>
    </tr>
    <tr>
      <td>An attacker hijacks robot long-range communication</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">3</td>
      <td class="warning">2</td>
      <td class="success">1</td>
      <td class="danger">3</td>
      <td class="success">1</td>
      <td>10</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="warning">▲</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td>
        <ul>
          <li>Long-range communication should always use a secure transport layer
(WPA2 for WiFi for instance)</li>
        </ul>
      </td>
      <td>
        <a href="http://arxiv.org/abs/1504.04339">Bonaci, Tamara, Jeffrey
Herron, Tariq Yusuf, Junjie Yan, Tadayoshi Kohno, and Howard Jay Chizeck. “To
Make a Robot Secure: An Experimental Analysis of Cyber Security Threats Against
Teleoperated Surgical Robots.” ArXiv:1504.04339 [Cs], April 16, 2015.</a>
      </td>
    </tr>
    <tr>
      <td>An attacker intercepts robot long-range communications (e.g. MitM)</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">1</td>
      <td class="warning">2</td>
      <td class="success">1</td>
      <td class="danger">3</td>
      <td class="success">1</td>
      <td>8</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td>
        <ul>
          <li>Long-range communication should always use a secure transport layer
(WPA2 for WiFi for instance)</li>
        </ul>
      </td>
      <td>
        <a href="http://arxiv.org/abs/1504.04339">Bonaci, Tamara, Jeffrey
Herron, Tariq Yusuf, Junjie Yan, Tadayoshi Kohno, and Howard Jay Chizeck. “To
Make a Robot Secure: An Experimental Analysis of Cyber Security Threats Against
Teleoperated Surgical Robots.” ArXiv:1504.04339 [Cs], April 16, 2015.</a>
      </td>
    </tr>
    <tr>
      <td>An attacker disrupts (e.g. jams) robot long-range communication
channels.</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="warning">2</td>
      <td class="warning">2</td>
      <td class="success">1</td>
      <td class="success">1</td>
      <td class="danger">3</td>
      <td>9</td>
      <td class="danger">✘</td>
      <td class="warning">▲</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td>
        <ul>
          <li>Multiple long-range communication transport layers should be used
when possible (e.g. cellular and WiFi)</li>
        </ul>
      </td>
      <td>
        <a href="http://arxiv.org/abs/1504.04339">Bonaci, Tamara, Jeffrey
Herron, Tariq Yusuf, Junjie Yan, Tadayoshi Kohno, and Howard Jay Chizeck. “To
Make a Robot Secure: An Experimental Analysis of Cyber Security Threats Against
Teleoperated Surgical Robots.” ArXiv:1504.04339 [Cs], April 16, 2015.</a>
      </td>
    </tr>
    <tr>
      <th colspan="29">Embedded / Software / Communication / Short-Range
Communication (e.g. Bluetooth)</th>
    </tr>
    <tr>
      <td>An attacker executes arbitrary code using a short-range communication
      protocol vulnerability.</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="danger">3</td>
      <td class="warning">2</td>
      <td class="success">1</td>
      <td class="success">1</td>
      <td class="danger">3</td>
      <td>10</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td>
        <ul>
          <li>Communications protocols should be disabled if unused (by using e.g.
rfkill).</li>
          <li>Binaries and libraries required to support short-range communications
should be kept up-to-date.</li>
        </ul>
      </td>
      <td>
        <a href="http://dl.acm.org/citation.cfm?id=2028067.2028073">Checkoway,
Stephen, Damon McCoy, Brian Kantor, Danny Anderson, Hovav Shacham, Stefan
Savage, Karl Koscher, Alexei Czeskis, Franziska Roesner, and Tadayoshi Kohno.
“Comprehensive Experimental Analyses of Automotive Attack Surfaces.” In
Proceedings of the 20th USENIX Conference on Security, 6–6. SEC’11.
Berkeley, CA, USA: USENIX Association, 2011.</a></td>
  </tr>

  <tr><th colspan="29">Embedded / Software / Communication / Remote Application Interface</th></tr>

  <tr>
  <td>An attacker gains unauthenticated access to the remote application interface.</td>
  <td class="success">✓</td>
  <td class="success">✓</td>
  <td class="danger">✘</td>
  <td class="success">✓</td>
  <td class="success">✓</td>
  <td class="warning">▲</td>
  <td class="danger">3</td>
  <td class="danger">3</td>
  <td class="success">1</td>
  <td class="success">1</td>
  <td class="danger">3</td>
  <td>11</td>
  <td class="success">✓</td>
  <td class="success">✓</td>
  <td class="success">✓</td>
  <td class="success">✓</td>
  <td class="danger">✘</td>
  <td class="danger">✘</td>
  <td class="danger">✘</td>
  <td class="success">✓</td>
  <td class="danger">✘</td>
  <td class="success">✓</td>
  <td class="success">✓</td>
  <td class="success">✓</td>
  <td>
    <ul>
      <li>Implement authentication and authorization methods.</li>
      <li>Enable RBAC to limit permissions for the users.</li>
    </ul>
  </td>
  <td></td>
  </tr>
  <tr>
  <td>An attacker could eavesdrop communications to the Robot’s remote application interface.</td>
  <td class="danger">✘</td>
  <td class="danger">✘</td>
  <td class="danger">✘</td>
  <td class="success">✓</td>
  <td class="danger">✘</td>
  <td class="danger">✘</td>
  <td class="success">1</td>
  <td class="success">1</td>
  <td class="success">1</td>
  <td class="success">1</td>
  <td class="danger">3</td>
  <td>7</td>
  <td class="danger">✘</td>
  <td class="success">✓</td>
  <td class="danger">✘</td>
  <td class="danger">✘</td>
  <td class="danger">✘</td>
  <td class="danger">✘</td>
  <td class="danger">✘</td>
  <td class="danger">✘</td>
  <td class="danger">✘</td>
  <td class="danger">✘</td>
  <td class="danger">✘</td>
  <td class="danger">✘</td>
  <td>
    <ul>
      <li>Communications with the remote application interface should be done over a secure channel.</li>
    </ul>
  </td>
  <td></td>
  </tr>

  <tr>
  <td>An attacker could alter data sent to the Robot’s remote application interface.</td>
  <td class="success">✓</td>
  <td class="success">✓</td>
  <td class="danger">✘</td>
  <td class="success">✓</td>
  <td class="success">✓</td>
  <td class="warning">▲</td>
  <td class="danger">3</td>
  <td class="danger">3</td>
  <td class="success">1</td>
  <td class="success">1</td>
  <td class="danger">3</td>
  <td>11</td>
  <td class="success">✓</td>
  <td class="success">✓</td>
  <td class="success">✓</td>
  <td class="success">✓</td>
  <td class="danger">✘</td>
  <td class="danger">✘</td>
  <td class="danger">✘</td>
  <td class="success">✓</td>
  <td class="danger">✘</td>
  <td class="success">✓</td>
  <td class="success">✓</td>
  <td class="success">✓</td>
  <td>
    <ul>
      <li>Communications with the remote application interface should be done over a secure channel.</li>
    </ul>
  </td>
  <td></td>
  </tr>

  <tr><th colspan="29">Embedded / Software / OS &amp; Kernel</th></tr>

  <tr>
    <td>An attacker compromises the real-time clock to disrupt the kernel RT
scheduling guarantees.</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">3</td>
      <td class="warning">2</td>
      <td class="success">1</td>
      <td class="danger">3</td>
      <td class="warning">2</td>
      <td>11</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td>
        <ul>
          <li>Hardened kernel (prevent dynamic loading of kernel modules)</li>
          <li>Ensure only trustable kernels are used (e.g. Secure Boot)</li>
          <li>/boot should not be accessible by robot processes</li>
          <li><span markdown="1">
          [NTP security best practices][ietf_ntp_bcp] should be enforced to ensure no
          attacker can manipulate the robot computer clock.
          See also [RFC 7384][rfc_7384],
          [NTPsec][ntpsec] and
          [Emerging Solutions in Time Synchronization Security][emerging_solutions_time_sync_sec].
          Additionally, [PTP protocol][ieee_1588_2008] can be considered instead of NTP.
          </span></li>
        </ul>
      </td>
      <td>
        <a href="https://doi.org/10.1109/MSP.2012.104">Dessiatnikoff, Anthony,
Yves Deswarte, Eric Alata, and Vincent Nicomette. “Potential Attacks on
Onboard Aerospace Systems.” IEEE Security &amp; Privacy 10, no. 4 (July
2012): 71–74.</a>
      </td>
    </tr>
    <tr>
      <td>An attacker compromises the OS or kernel to alter robot data.</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">3</td>
      <td class="warning">2</td>
      <td class="success">1</td>
      <td class="danger">3</td>
      <td class="warning">2</td>
      <td>11</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td>
        <ul>
          <li>OS user accounts should be properly secured (randomized password or
e.g. SSH keys)</li>
          <li>Hardened kernel (prevent dynamic loading of kernel modules)</li>
          <li>Ensure only trustable kernels are used (e.g. Secure Boot)</li>
          <li>/boot should not be accessible by robot processes</li>
        </ul>
      </td>
      <td>
        <a href="https://doi.org/10.1109/COGSIMA.2017.7929597">Clark, George
W., Michael V. Doran, and Todd R. Andel. “Cybersecurity Issues in
Robotics.” In 2017 IEEE Conference on Cognitive and Computational Aspects of
Situation Management (CogSIMA), 1–5. Savannah, GA, USA: IEEE, 2017.</a>
      </td>
    </tr>
    <tr>
      <td>An attacker compromises the OS or kernel to eavesdrop on robot
data.</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">1</td>
      <td class="warning">2</td>
      <td class="success">1</td>
      <td class="danger">3</td>
      <td class="warning">2</td>
      <td>9</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td>
        <ul>
          <li>OS user accounts should be properly secured (randomized password or
e.g. SSH keys)</li>
          <li>Hardened kernel (prevent dynamic loading of kernel modules)</li>
          <li>Ensure only trustable kernels are used (e.g. Secure Boot)</li>
          <li>/boot should not be accessible by robot processes</li>
        </ul>
      </td>
      <td>
        <a href="https://doi.org/10.1109/COGSIMA.2017.7929597">Clark, George
W., Michael V. Doran, and Todd R. Andel. “Cybersecurity Issues in
Robotics.” In 2017 IEEE Conference on Cognitive and Computational Aspects of
Situation Management (CogSIMA), 1–5. Savannah, GA, USA: IEEE, 2017.</a>
      </td>
    </tr>
    <tr>
      <td>An attacker gains access to the robot OS through its administration
interface.</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td class="warning">2</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td>14</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td>
        <ul>
          <li>Administrative interface should be properly secured (e.g. no
default/static password).</li>
          <li>Administrative interface should be accessible by a limited number
              of physical machines.
              For instance, one may require the user to be physically co-located with the
              robot (see e.g. ADB for Android)</li>
        </ul>
      </td>
      <td></td>
    </tr>
    <tr>
      <th colspan="29">Embedded / Software / Component-Oriented
Architecture</th>
    </tr>
    <tr>
      <td>A node accidentally writes incorrect data to a communication
channel.</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="warning">2</td>
      <td class="danger">3</td>
      <td class="warning">2</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td>13</td>
      <td class="danger">✘</td>
      <td class="warning">▲</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td>
        <ul>
          <li>Components should always validate received messages.</li>
          <li>Invalid message events should be logged and users should be
notified.</li>
        </ul>
      </td>
      <td>
        <a href="http://sunnyday.mit.edu/nasa-class/Ariane5-report.html">Jacques-Louis
Lions et al. "Ariane S Flight 501 Failure." ESA Press Release 33–96, Paris,
1996.</a>
      </td>
    </tr>
    <tr>
      <td>An attacker deploys a malicious component on the robot.</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td class="warning">2</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td>14</td>
      <td class="danger">✘</td>
      <td class="warning">▲</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td>
        <ul>
          <li>Components should not trust other components (received messages
needs to be validated, etc.).</li>
          <li>Users should not be able to deploy components directly.</li>
          <li>Components binary should be digitally signed.</li>
          <li>Components source code should be audited.</li>
          <li>Components should run with minimal privileges (CPU and memory
quota, minimal I/O and access to the filesystem)</li>
        </ul>
      </td>
      <td>
        <a href="http://dl.acm.org/citation.cfm?id=2028067.2028073">Checkoway,
Stephen, Damon McCoy, Brian Kantor, Danny Anderson, Hovav Shacham, Stefan
Savage, Karl Koscher, Alexei Czeskis, Franziska Roesner, and Tadayoshi Kohno.
“Comprehensive Experimental Analyses of Automotive Attack Surfaces.” In
Proceedings of the 20th USENIX Conference on Security, 6–6. SEC’11.
Berkeley, CA, USA: USENIX Association, 2011.</a>
      </td>
    </tr>
    <tr>
      <td>An attacker can prevent a component running on the robot from executing
normally.</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="warning">2</td>
      <td class="danger">3</td>
      <td class="warning">2</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td>13</td>
      <td class="danger">✘</td>
      <td class="warning">▲</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td>
        <ul>
          <li>Components should not be trusted and be properly isolated (e.g. run
as different users)</li>
          <li>When safe, components should attempt to restart automatically when
a fatal error occurs.</li>
        </ul>
      </td>
      <td>
        <a href="https://doi.org/10.1109/MSP.2012.104">Dessiatnikoff, Anthony,
Yves Deswarte, Eric Alata, and Vincent Nicomette. “Potential Attacks on
Onboard Aerospace Systems.” IEEE Security &amp; Privacy 10, no. 4 (July
2012): 71–74.</a>
      </td>
    </tr>
    <tr>
      <th colspan="29">Embedded / Software / Configuration Management</th>
    </tr>
    <tr>
      <td>An attacker modifies configuration values without authorization.</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td>15</td>
      <td class="danger">✘</td>
      <td class="warning">▲</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="warning">▲</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td>
        <ul>
          <li>Configuration data access control list should be implemented.</li>
          <li>Configuration data modifications should be logged.</li>
          <li>Configuration write-access should be limited to the minimum set of
users and/or components.</li>
        </ul>
      </td>
      <td>
        <a href="https://doi.org/10.3390/s18051643">Ahmad Yousef, Khalil, Anas
AlMajali, Salah Ghalyon, Waleed Dweik, and Bassam Mohd. “Analyzing
Cyber-Physical Threats on Robotic Platforms.” Sensors 18, no. 5 (May 21,
2018): 1643.</a></td>
  </tr>

  <tr>
    <td>An attacker accesses configuration values without authorization.</td>
    <td class="danger">✘</td>
    <td class="danger">✘</td>
    <td class="success">✓</td>
    <td class="danger">✘</td>
    <td class="danger">✘</td>
    <td class="danger">✘</td>
    <td class="success">1</td>
    <td class="danger">3</td>
    <td class="danger">3</td>
    <td class="danger">3</td>
    <td class="danger">3</td>
    <td>13</td>
    <td class="danger">✘</td>
    <td class="success">✓</td>
    <td class="danger">✘</td>
    <td class="danger">✘</td>
    <td class="danger">✘</td>
    <td class="danger">✘</td>
    <td class="danger">✘</td>
    <td class="danger">✘</td>
    <td class="danger">✘</td>
    <td class="danger">✘</td>
    <td class="danger">✘</td>
    <td class="danger">✘</td>
    <td>
      <ul>
        <li>Configuration data should be considered as private.</li>
        <li>Configuration data should accessible by the minimum set of users
and/or components.</li>
        </ul>
      </td>
      <td>
        <a href="https://doi.org/10.3390/s18051643">Ahmad Yousef, Khalil, Anas
AlMajali, Salah Ghalyon, Waleed Dweik, and Bassam Mohd. “Analyzing
Cyber-Physical Threats on Robotic Platforms.” Sensors 18, no. 5 (May 21,
2018): 1643.</a>
      </td>
    </tr>
    <tr>
      <td>A user accidentally misconfigures the robot.</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td>15</td>
      <td class="danger">✘</td>
      <td class="warning">▲</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="warning">▲</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td>
        <ul>
          <li>Configuration data changes should be reversible.</li>
          <li>Large change should be applied atomically.</li>
          <li>Fault monitoring should be able to automatically reset the
configuration to a safe state if the robot becomes unavailable.</li>
        </ul>
      </td>
      <td></td>
    </tr>
    <tr>
      <th colspan="29">Embedded / Software / Data Storage (File
System)</th>
    </tr>
    <tr>
      <td>An attacker modifies the robot file system by physically accessing
it.</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td>15</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td>
        <ul>
          <li>Robot filesystem must be encrypted.
              The key should be stored in a secure enclave (TPM).</li>
          <li>Robot filesystem should be wiped out if the robot is physically
            compromised.</li>
        </ul>
      </td>
      <td></td>
    </tr>
    <tr>
      <td>An attacker eavesdrops on the robot file system by physically accessing
it.</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">1</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td>13</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td>
        <ul>
          <li>Robot filesystem must be encrypted.
              The key should be stored in a secure enclave (TPM).</li>
          <li>Robot filesystem should be wiped out if the robot perimeter is breached.</li>
        </ul>
      </td>
      <td></td>
    </tr>
    <tr>
      <td>An attacker saturates the robot disk with data.</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td class="success">1</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td>13</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td>
        <ul>
          <li>Robot components disk quota should be bounded.</li>
          <li>Disk usage should be properly monitored, logged and reported.</li>
          <li>Optionally, components may have the option to run w/o any file system access.
              This should be preferred whenever possible.</li>
        </ul>
      </td>
      <td></td>
    </tr>
    <tr>
      <th colspan="29">Embedded / Software / Logs</th>
    </tr>
    <tr>
      <td>An attacker exfiltrates log data to a remote server.</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="warning">2</td>
      <td class="warning">2</td>
      <td class="warning">2</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td>12</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td>
        <ul>
          <li>Logs should never contain private data.
              Log data should be anonymized when needed.</li>
          <li>Logs should be rotated and deleted after a pre-determined retention period.</li>
          <li>Logs should be encrypted in-transit and at-rest.</li>
          <li>Logs access should be ACL protected.</li>
          <li>Logs access should be monitored to enable later audits.</li>
        </ul>
      </td>
      <td></td>
    </tr>
    <tr>
      <th colspan="29">Embedded / Hardware / Sensors</th>
    </tr>
    <tr>
      <td>An attacker spoofs a robot sensor (by e.g. replacing the sensor itself
or manipulating the bus).</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">3</td>
      <td class="warning">2</td>
      <td class="success">1</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td>12</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td>
        <ul>
          <li>Sensors should embed an identifier to detect hardware
            tampering.</li>
          <li>Components should try to explicitly refer to which sensor ID they
            expect data from.</li>
          <li>Sensor data should be signed and ideally encrypted over the
            wire.</li>
        </ul>
      </td>
      <td></td>
    </tr>
    <tr>
      <th colspan="29">Embedded / Hardware / Actuators</th>
    </tr>
    <tr>
      <td>An attacker spoofs a robot actuator.</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">1</td>
      <td class="warning">2</td>
      <td class="success">1</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td>10</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td>
        <ul>
          <li>Actuators should embed an identifier.</li>
          <li>Command vector should be signed (ideally encrypted) to prevent
manipulation.</li>
        </ul>
      </td>
      <td></td>
    </tr>
    <tr>
      <td>An attacker modifies the command sent to the robot actuators.
(intercept &amp; retransmit)</td>
    <td class="danger">✘</td>
    <td class="success">✓</td>
    <td class="danger">✘</td>
    <td class="danger">✘</td>
    <td class="danger">✘</td>
    <td class="danger">✘</td>
    <td class="danger">3</td>
    <td class="warning">2</td>
    <td class="success">1</td>
    <td class="danger">3</td>
    <td class="danger">3</td>
    <td>12</td>
    <td class="danger">✘</td>
    <td class="danger">✘</td>
    <td class="danger">✘</td>
    <td class="success">✓</td>
    <td class="danger">✘</td>
    <td class="danger">✘</td>
    <td class="danger">✘</td>
    <td class="danger">✘</td>
    <td class="success">✓</td>
    <td class="danger">✘</td>
    <td class="success">✓</td>
    <td class="danger">✘</td>
    <td>
      <ul>
        <li>Actuators should embed an identifier.</li>
        <li>Command vector should be signed (ideally encrypted) to prevent
manipulation.</li>
        </ul>
      </td>
      <td></td>
    </tr>
    <tr>
      <td>An attacker intercepts the robot actuators command (can recompute localization).</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">1</td>
      <td class="warning">2</td>
      <td class="success">1</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td>10</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td>
        <ul>
          <li>Command vector should be encrypted.</li>
        </ul>
      </td>
      <td></td>
    </tr>
    <tr>
      <td>An attacker sends malicious command to actuators to trigger the
E-Stop</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="warning">2</td>
      <td class="warning">2</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td class="success">1</td>
      <td>11</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td>
        <ul>
          <li>If a joint command is exceeding the joint limits, a specific code
              path for handling out-of-bounds command should be executed instead of triggering the
              E-Stop.
              Whenever safe, the command could be discarded and the error reported to the user for
              instance.</li>
        </ul>
      </td>
      <td></td>
    </tr>
    <tr>
      <th colspan="29">Embedded / Hardware / Auxilliary Functions</th>
    </tr>
    <tr>
      <td>An attacker compromises the software or sends malicious commands to
drain the robot battery.</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="warning">2</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td>14</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td>
        <ul>
          <li>Per-node CPU quota should be enforced.</li>
          <li>Appropriate protection should be implemented to prevent actuators
from over-heating.</li>
          <li>If the battery level becomes critically low, the robot should be
able to bring itself to a stop.</li>
        </ul>
      </td>
      <td>
        <a href="https://doi.org/10.1109/MSP.2012.104">Dessiatnikoff, Anthony,
Yves Deswarte, Eric Alata, and Vincent Nicomette. “Potential Attacks on
Onboard Aerospace Systems.” IEEE Security &amp; Privacy 10, no. 4 (July
2012): 71–74.</a></td>
  </tr>

  <tr><th colspan="29">Embedded / Hardware / Communications</th></tr>

  <tr>
    <td>An attacker connects to an exposed debug port.</td>
    <td class="success">✓</td>
    <td class="success">✓</td>
    <td class="success">✓</td>
    <td class="success">✓</td>
    <td class="success">✓</td>
    <td class="success">✓</td>
    <td class="danger">3</td>
    <td class="danger">3</td>
    <td class="danger">3</td>
    <td class="danger">3</td>
    <td class="danger">3</td>
    <td>15</td>
    <td class="success">✓</td>
    <td class="success">✓</td>
    <td class="success">✓</td>
    <td class="danger">✘</td>
    <td class="success">✓</td>
    <td class="success">✓</td>
    <td class="success">✓</td>
    <td class="success">✓</td>
    <td class="success">✓</td>
    <td class="success">✓</td>
    <td class="success">✓</td>
    <td class="success">✓</td>
    <td>
      <ul>
        <li>Close the communication port to external communications or disable the service on non-development devices.</li>
      </ul>
    </td>
    <td></td>
  </tr>

  <tr>
    <td>An attacker connects to an internal communication bus.</td>
    <td class="success">✓</td>
    <td class="success">✓</td>
    <td class="danger">✘</td>
    <td class="warning">▲</td>
    <td class="warning">▲</td>
    <td class="warning">▲</td>
    <td class="danger">3</td>
    <td class="danger">3</td>
    <td class="danger">3</td>
    <td class="danger">3</td>
    <td class="danger">3</td>
    <td>15</td>
    <td class="warning">▲</td>
    <td class="warning">▲</td>
    <td class="warning">▲</td>
    <td class="danger">✘</td>
    <td class="warning">▲</td>
    <td class="warning">▲</td>
    <td class="warning">▲</td>
    <td class="warning">▲</td>
    <td class="warning">▲</td>
    <td class="warning">▲</td>
    <td class="warning">▲</td>
    <td class="warning">▲</td>
    <td>
      <ul>Limit access to internal communications and buses.
      </ul>
    </td>
    <td></td>
  </tr>

  <tr><th colspan="29">Remote / Client Application</th></tr>

  <tr>
  <td>An attacker intercepts the user credentials on their desktop machine.</td>
  <td class="danger">✘</td>
  <td class="danger">✘</td>
  <td class="danger">✘</td>
  <td class="danger">✘</td>
  <td class="danger">✘</td>
  <td class="success">✓</td>
  <td class="warning">2</td>
  <td class="warning">2</td>
  <td class="warning">2</td>
  <td class="danger">3</td>
  <td class="success">1</td>
  <td>10</td>
  <td class="danger">✘</td>
  <td class="danger">✘</td>
  <td class="danger">✘</td>
  <td class="danger">✘</td>
  <td class="danger">✘</td>
  <td class="danger">✘</td>
  <td class="success">✓</td>
  <td class="danger">✘</td>
  <td class="warning">▲</td>
  <td class="danger">✘</td>
  <td class="success">✓</td>
  <td class="danger">✘</td>
  <td>
    <ul>
      <li>Remote users should be granted minimum privileges</li>
      <li>Credentials on desktop machines should be stored securely
          (secure enclave, TPM, etc.)</li>
          <li>User credentials should be revokable or expire automatically</li>
          <li>User credentials should be tied to the user identity for audit
          purposes</li>
        </ul>
      </td>
      <td></td>
    </tr>
    <tr>
      <th colspan="29">Remote / Cloud Integration</th>
    </tr>
    <tr>
      <td>An attacker intercepts cloud service credentials deployed on the
robot.</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="warning">2</td>
      <td class="warning">2</td>
      <td class="success">1</td>
      <td class="danger">3</td>
      <td class="success">1</td>
      <td>9</td>
      <td class="danger">✘</td>
      <td class="warning">▲</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="warning">▲</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td>
        <ul>
          <li>Cloud services should be granted minimal privileges.</li>
          <li>Cloud services credentials should be revokable.</li>
          <li>Cloud services should be audited for abuse / unauthorized
access.</li>
        </ul>
      </td>
      <td></td>
    </tr>
    <tr>
      <td>An attacker gains read access to robot cloud data.</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="warning">2</td>
      <td class="warning">2</td>
      <td class="success">1</td>
      <td class="danger">3</td>
      <td class="success">1</td>
      <td>9</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="warning">▲</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td>
        <ul>
          <li>Cloud data stores should encrypt data at rest</li>
        </ul>
      </td>
      <td></td>
    </tr>
    <tr>
      <td>An attacker alters or deletes robot cloud data.</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="warning">2</td>
      <td class="warning">2</td>
      <td class="success">1</td>
      <td class="danger">3</td>
      <td class="success">1</td>
      <td>9</td>
      <td class="danger">✘</td>
      <td class="warning">▲</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="warning">▲</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td>
        <ul>
          <li>Cloud data should have proper backup mechanisms.</li>
          <li>Cloud data access should be audited.
              If an intrusion is detected, a process to restore the system back to a previous
              "uncompromised" state should be available.</li>
        </ul>
      </td>
      <td></td>
    </tr>
    <tr>
      <th colspan="29">Remote / Software Deployment</th>
    </tr>
    <tr>
      <td>An attacker spoofs the deployment service.</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td class="warning">2</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td>14</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="warning">▲</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="warning">▲</td>
      <td class="warning">▲</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td>
        <ul>
          <li>Deployment service should be authenticated• Communication with
the deployment service should be done over a secure channel.</li>
        </ul>
      </td>
      <td></td>
    </tr>
    <tr>
      <td>An attacker modifies the binaries sent by the deployment service.</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td class="warning">2</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td>14</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="warning">▲</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="warning">▲</td>
      <td class="warning">▲</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td>
        <ul>
          <li>Deployment service should be authenticated• Communication with
the deployment service should be done over a secure channel.</li>
        </ul>
      </td>
      <td></td>
    </tr>
    <tr>
      <td>An attacker intercepts the binaries sent by the deployment service.</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">1</td>
      <td class="danger">3</td>
      <td class="warning">2</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td>12</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td>
        <ul>
          <li>Deployment service should be authenticated• Communication with
the deployment service should be done over a secure channel.</li>
        </ul>
      </td>
      <td></td>
    </tr>
    <tr>
      <td>An attacker prevents the robot and the deployment service from
communicating.</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="success">1</td>
      <td class="danger">3</td>
      <td class="warning">2</td>
      <td class="danger">3</td>
      <td class="danger">3</td>
      <td>12</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <th colspan="29">Cross-Cutting Concerns / Credentials, PKI and
Secrets</th>
    </tr>
    <tr>
      <td>An attacker compromises a Certificate Authority trusted by the
robot.</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="success">✓</td>
      <td class="danger">3</td>
      <td class="success">1</td>
      <td class="success">1</td>
      <td class="warning">2</td>
      <td class="danger">3</td>
      <td>10</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="success">✓</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td class="danger">✘</td>
      <td></td>
      <td></td>
    </tr>
  </table>
</div>

### Including a new robot into the threat model

The following steps are recommended in order to extend this document with additional threat models:

1. Determine the robot evaluation scenario.
   This will include:
  * System description and specifications
  * Data assets
1. Define the robot environment:
  * External actors
  * Entry points
  * Use cases
1. Design security boundary and architectural schemas for the robotic application.
1. Evaluate and prioritize entry points
  * Make use of the RSF[rsf] to find applicable weaknesses on the robot.
  * Take existing documentation as help for finding applicable entry points.
1. Evaluate existing threats based on general threat table and add new ones to the specific threat
   table.
  * Evaluate new threats with DREAD[wikipedia_dread] and STRIDE[wikipedia_stride] methodologies.
1. Design hypothetical attack trees for each of the entry points, detailing the affected resources
   on the process.
1. Create a Pull Request and submit the changes to the ros2/design repository.

## Threat Analysis for the `TurtleBot 3` Robotic Platform

### System description

The application considered in this section is tele-operation of a Turtlebot 3 robot using an Xbox
controller.

The robot considered in this section is a [TurtleBot 3 Burger][tb3_burger].
It is a small educational robot embedding an IMU and a Lidar, two motors /
wheels, and a chassis that hosts a battery, a Pi Raspberry Pi 3 Model B+ Single
Board Computer, and a OpenCR 1.0 Arduino compatible board that interacts with the sensors.
The robot computer runs two nodes:

* [`turtlebot3_node`][turtlebot3_node] forwarding sensor data and actuator control commands,
* [`raspicam2_node`][raspicam2_node] which is forwarding camera data

We also make the assumption that the robot is running a ROS 2 port of the AWS
[CloudWatch sample application][cw_sample_app]).
A ROS 2 version of this component is not yet available, but it will help us demonstrate the threats
related to connecting a robot to a cloud service.

For the purpose of demonstrating the threats associated with distributing a ROS
graph among multiple hosts, an Xbox controller is connected to a secondary
computer (“remote host”).
The secondary computer runs two additional nodes:

* [`joy_node`][joy_node] is forwarding joystick input as ROS 2 messages,
* [`teleop_twist_joy`][teleop_twist_joy] is converting ROS 2 joystick messages to control commands.

Finally, the robot data is accessed by a test engineer through a “field testing” computer.

### Architecture Dataflow diagram

![ROS 2 Application](ros2_threat_model/ROS2_Application.png)
[Diagram Source (draw.io)](ros2_threat_model/ROS2_Application.xml)

#### Assets

##### Hardware

* [TurtleBot 3 Burger][tb3_burger] is a small, [ROS-enabled][ros_wiki_tb]
  robot for education purposes.
  * Compute resources
    * Raspberry PI 3 host: OS Raspbian Stretch with ROS 2 Crystal running
      natively (without Docker), running as root.
    * OpenCR board: using ROS 2 firmware as described in the TurtleBot3 ROS 2 setup instructions.
  * [Hardware components][tb3_burger]) include:
    * The Lidar is connected to the Raspberry PI through USB.
    * A Raspberry PI camera module is connected to the Raspberry PI 3
      through its Camera Serial Interface (CSI).
* Field testing host: conventional laptop running OS Ubuntu 18.04, no ROS installed.
  Running as a sudoer user.
* Remote Host: any conventional server running OS Ubuntu 18.04 with ROS 2 Crystal.
* CI host: any conventional server running OS Ubuntu 18.04.

* WLAN: a wifi local area network without security enabled, open for anyone to
  connect
* Corporate private network: a secure corporate wide-area network, that spans multiple cities.
  Only authenticated user with suitable credentials can connect to the network, and good security
  practices like password rotation are in place.

##### Processes

* Onboard TurtleBot3 Raspberry Pi
  * `turtlebot3_node`
  * CloudWatch nodes (hypothetical as it has not been yet ported to ROS 2)
    * `cloudwatch_metrics_collector`: subscribes to a the /metrics topic where
      other nodes publish MetricList messages that specify CloudWatch
      metrics data, and sends the corresponding metric data to CloudWatch
      metrics using the PutMetricsData API.
    * `cloudwatch_logger`: subscribes to a configured list of topics, and
      publishes all messages found in that topic to a configured log group
      and log stream, using the CloudWatch metrics API.
  * Monitoring Nodes
    * `monitor_speed`: subscribes to the topic /odom, and for each received
      odometry message, extract the linear and angular speed, build a
      MetricList message with those values, and publishes that message to
      data to the /metrics topic.
    * `health_metric_collector`: collects system metrics (free RAM, total RAM,
      total CPU usage, per core CPU usage, uptime, number of processes) and
      publishes it as a MetricList message to the /metrics topic.
  * [`raspicam2_node`][raspicam2_node] a node publishing Raspberry Pi Camera
    Module data to ROS 2.
* An XRCE Agent runs on the Raspberry, and is used by a DDS-XRCE client running
  on the [OpenCR 1.0 board][opencr_1_0], that publishes IMU sensor data to ROS
  topics, and controls the wheels of the TurtleBot based on the
  [teleoperation][tb3_teleop] messages published as ROS topics.
  This channel uses serial communication.
* A Lidar driver process running on the Raspberry interfaces with the Lidar, and
  uses a DDS-XRCE client to publish data over UDP to an XRCE agent also running on
  the Raspberry Pi.
  The agent sends the sensor data to several ROS topics.
* An SSH client process is running in the field testing host, connecting to the
  Raspberry PI for diagnostic and debugging.
* A software update agent process is running on the Raspberry PI, OpenCR board,
  and navigation hosts.
  The agent polls for updates a code deployment service process running on the CI host, that
  responds with a list of packages and versions, and a new version of each package when an update
  is required.
* The CI pipeline process on the CI host is a Jenkins instance that is polling a code repository
  for new revisions of a number of ROS packages.
  Each time a new revision is detected it rebuilds all the affected packages, packs the binary
  artifacts into several deployment packages, and eventually sends the package
  updates to the update agent when polled.

##### Software Dependencies

* OS / Kernel
  * Ubuntu 18.04
* Software
  * ROS 2 Core Libraries
  * ROS 2 Nodes: [`joy_node`][joy_node], [`turtlebot3_node`][turtlebot3_node],
    [`rospicam2_node`][raspicam2_node], [`teleop_twist_joy`][teleop_twist_joy]
  * ROS 2 system dependencies as defined by rosdep:
    * RMW implementation: we assume the RMW implementation is
      [`rmw_fastrtps`][rmw_fastrtps].
    * The threat model describes attack with the security enabled or disabled.
      If the security is enabled, [the security plugins][fastrtps_security] are assumed to be
      configured and enabled.

See [TurtleBot3 ROS 2 setup][tb3_ros2_setup] instructions for details about TurtleBot3 software
dependencies.

##### External Actors

* A test engineer is testing the robot.
* A user operates the robot with the joystick.
* A business analyst periodically checks dashboards with performance
  information for the robot in the AWS Cloudwatch web console.

##### Robot Data Assets

* Topic Message
  * Private Data
    * Camera image messages
    * Logging messages (might describe camera data)
    * CloudWatch metrics and logs messages (could contain Intellectual
      Property such as which algorithms are implemented in a particular
      node).
      * Restricted Data
    * Robot Speed and Orientation.
      Some understanding of the current robot task may be reconstructed from those messages..
* AWS CloudWatch data
  * Metrics, logs, and aggregated dashboard are all private data, as they
    are different serializations of the corresponding topics.
* Raspberry Pi System and ROS logs on Raspberry PI
  * Private data just like CloudWatch logs.
* AWS credentials on all hosts
  * Secret data, provide access to APIs and other compute assets on the AWS
    cloud.
* SSH credentials on all hosts
  * Secret data, provide access to other hosts.
* Robot embedded algorithm (e.g. `teleop_twist_joy`)
  * Secret data.
    Intellectual Property (IP) theft is a critical issue for nodes which are either easy to
    decompile or written in an interpreted language.

##### Robot Compute Assets

* AWS CloudWatch APIs and all other AWS resources accessible from the AWS
  credentials present in all the hosts.
* Robot Topics
  * `/cmd_vel` could be abused to damage the robot or hurt users.

#### Entry points

* Communication Channels
  * DDS / ROS Topics
    * Topics can be listened or written to by any actor:
      1. Connected to a network where DDS packets are routed to,
      1. Have necessary permissions (read / write) if SROS is enabled.
    * When SROS is enabled, attackers may try to compromise the CA authority
      or the private keys to generate or intercept private keys as well as
      emitting malicious certificates to allow spoofing.
    * USB connection is used for communication between Raspberry Pi and OpenCR board
      and LIDAR sensor.
  * SSH
    * SSH access is possible to anyone on the same LAN or WAN (if port-forwarding is enabled).
      Many images are setup with a default username and password with administrative
      capabilities (e.g. sudoer).
    * SSH access can be compromised by modifying the robot
* Deployed Software
  * ROS nodes are compiled either by a third-party (OSRF build-farm) or by the application
    developer.
    It can be compiled directly on the robot or copied from a developer workstation using scp or
    rsync.
  * An attacker compromising the build-farm or the developer workstation could
    introduce a vulnerability in a binary which would then be deployed to the
    robot.
* Data Store (local filesystem)
  * Robot Data
    * System and ROS logs are stored on the Raspberry Pi filesystem.
    * Robot system is subject to physical attack (physically removing the
      disk from the robot to read its data).
  * Remote Host Data
    * Machines running additional ROS nodes will also contain log files.
    * Remote hosts is subject to physical attack.
      Additionally, this host may not be as secured as the robot host.
  * Cloud Data
    * AWS CloudWatch data is accessible from public AWS API endpoints, if
      credentials are available for the corresponding AWS account.
    * AWS CloudWatch can be credentials can allow attackers to access other
      cloud resources depending on how the account has been configured.
  * Secret Management
    * DDS / ROS Topics
      * If SROS is enabled, private keys are stored on the local filesystem.
    * SSH
      * SSH credentials are stored on the robot filesystem.
      * Private SSH keys are stored in any computer allowed to log into the
        robot where public/private keys are relied on for authentication
        purposes.
    * AWS Credentials
      * AWS credentials are stored on the robot file system.

#### Use case scenarios

* Development, Testing and Validation
  * An engineer develops code or runs tests on the robot.
    They may:
    * Restart the robot
    * Restart the ROS graph
    * Physically interact with the robot
    * Log into the robot using SSH
    * Check AWS console for metrics and log
* End-User
  * A user tele-operates the robot.
    They may:
    * Start the robot.
    * Control the joystick.
  * A business analyst may access AWS CloudWatch data on the console to assess
    the robot performance.

#### Threat model

Each generic threat described in the previous section can be instantiated on
the TurtleBot 3.

This table indicates which TurtleBot particular assets and entry points are
impacted by each threat.
A check sign (✓) means impacted while a cross sign (✘) means not impacted.
The "SROS Enabled?" column explicitly states out whether using SROS would
mitigate the threat or not.
A check sign (✓) means that the threat could be exploited while SROS is enabled while a cross
sign (✘) means that the threat requires SROS to be disabled to be applicable.

<div class="table" markdown="1">
<table class="table">
  <tr>
    <th rowspan="2" style="width: 20em">Threat</th>
    <th colspan="2" style="width: 6em">TurtleBot Assets</th>
    <th colspan="3" style="width: 6em">Entry Points</th>
    <th rowspan="2" style="width: 3.25em; white-space: nowrap; transform:
rotate(-90deg) translateX(-2.5em) translateY(5.5em)">SROS Enabled?</th>
    <th rowspan="2" style="width: 30em">Attack</th>
    <th rowspan="2" style="width: 30em">Mitigation</th>
    <th rowspan="2" style="width: 30em">Mitigation Result (redesign / transfer
/ avoid / accept)</th>
    <th rowspan="2" style="width: 30em">Additional Notes / Open Questions</th>
  </tr>

  <tr style="height: 10em; white-space: nowrap;">
    <th style="transform: rotate(-90deg) translateX(-3.5em)
translateY(3em)">Human Assets</th>
    <th style="transform: rotate(-90deg) translateX(-3.5em)
translateY(3em)">Robot App.</th>
    <th style="transform: rotate(-90deg) translateX(-4em) translateY(4em)">DDS
Topic</th>
    <th style="transform: rotate(-90deg) translateX(-4em) translateY(4em)">OSRF
Build-farm</th>
    <th style="transform: rotate(-90deg) translateX(-4em)
translateY(4em)">SSH</th>
  </tr>

  <tr><th colspan="11">Embedded / Software / Communication / Inter-Component
Communication</th></tr>

  <tr>
    <td rowspan="3">An attacker spoofs a component identity.</td>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="success">✘</td>
    <td class="success">✘</td>
    <td class="success">✘</td>
    <td>Without SROS any node may have any name so spoofing is trivial.</td>
    <td><ul><li> Enable SROS / DDS Security Extension to authenticate and
encrypt DDS communications.</li></ul></td>
    <td class="success">Risk is reduced if SROS is used.</td>
    <td>Authentication codes need to be generated for every pair of
        participants rather than every participant sharing a single authentication code
        with all other participants.
        Refer to section 7.1.1.3 of the DDS Security standard.</td>
  </tr>

  <tr>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="success">✘</td>
    <td class="success">✘</td>
    <td class="danger">✓</td>
    <td>An attacker deploys a malicious node which is not enabling DDS Security
Extension and spoofs the `joy_node` forcing the robot to stop.</td>
    <td>
      <ul>
        <li>DDS Security Governance document must set `allow_unauthenticated_participants` to False
            to avoid non-authenticated participants to be allowed to communicate with
            authenticated nodes.</li>
        <li>DDS Security Governance document must set `enable_join_access_control` to True to
            explicitly whitelist node-to-node-communication.
            permissions.xml should be as restricted as possible.</li>
      </ul>
    </td>
    <td class="success">Risk is mitigated.</td>
    <td>
      <ul>
        <li>Which actions would still be possible even with restrictive permission set? (e.g. does
            a node have the ability to fetch parameters from the parameter server?</li>
        <li>How about set parameters? Query other node's lifecycle state?  Etc.).</li>
      </ul>
    </td>
  </tr>

  <tr>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="success">✘</td>
    <td class="success">✘</td>
    <td class="danger">✓</td>
    <td>An attacker steals node credentials and spoofs the
<code>joy_node</code> forcing the robot to stop.</td>
    <td>
      <ul>
        <li>Store node credentials in a secure location (secure enclave, RoT)
to reduce the probability of having a private key leaked.</li>
        <li>Run nodes in isolated sandboxes to ensure one node cannot access
another node data (including credentials)</li>
        <li>Permissions CA should digitally sign nodes binaries to prevent
running tampered binaries.</li>
        <li>Permissions CA should be able to revoke certificates in case
credentials get stolen.</li>
      </ul>
    </td>
    <td class="danger">Mitigation risk requires additional work.</td>
    <td>
      <ul>
        <li>AWS Robotics and Automation is currently evaluating the feasibility
        of storing DDS-Security credentials in a TPM.</li>
        <li>Complete mitigation would require isolation using e.g. Snap or Docker.</li>
        <li><span markdown="1">Deploying an application with proper isolation
  would require us to revive discussions around
  [ROS 2 launch system][ros2_launch_design_pr]</span></li>
        <li>Yocto / OpenEmbedded / Snap support should be considered</li>
      </ul>
    </td>
  </tr>

  <tr>
    <td>An attacker intercepts and alters a message.</td>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="success">✘</td>
    <td class="success">✘</td>
    <td class="success">✘</td>
    <td>Without SROS an attacker can modify <code>/cmd_vel</code> messages sent
through a network connection to e.g. stop the robot.</td>
    <td>
      <ul>
        <li>Enable SROS / DDS Security Extension to authenticate and encrypt DDS communications.
            Message tampering is mitigated by DDS security as message authenticity is verified by
            default (with preshared HMACs / digital signatures)</li>
      </ul>
    </td>
    <td class="success">Risk is reduced if SROS is used.</td>
    <td>Additional hardening could be implemented by forcing part of the
TurtleBot topic to only be communicated over shared memory.</td>
  </tr>

  <tr>
    <td rowspan="2">An attacker writes to a communication channel without
authorization.</td>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="success">✘</td>
    <td class="success">✘</td>
    <td class="success">✘</td>
    <td>Without SROS, any node can publish to any topic.</td>
    <td>
      <ul>
        <li>Enable SROS / DDS Security Extension to authenticate and encrypt
DDS communications.</li>
      </ul>
    </td>
    <td class="success">Risk is mitigated.</td>
    <td> </td>
  </tr>

  <tr>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="success">✘</td>
    <td class="success">✘</td>
    <td class="danger">✓</td>
    <td>An attacker obtains credentials and publishes messages to
<code>/cmd_vel</code></td>
    <td>
      <ul>
        <li><code>permissions.xml</code> must be kept as closed as
possible.</li>
        <li>Publication to sensitive topics permission must only be granted to
a limited set of nodes the robot can trust.</li>
        <li>ROS nodes must run in sandboxes to prevent interferences"</li>
      </ul>
    </td>
    <td class="warning">Transfer risk to user configuring permissions.xml</td>
    <td><code>permissions.xml</code> should ideally be generated as writing it
manually is cumbersome and error-prone.</td>
  </tr>

  <tr>
    <td rowspan="4">An attacker listens to a communication channel without
authorization.</td>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="success">✘</td>
    <td class="success">✘</td>
    <td class="success">✘</td>
    <td>Without SROS: any node can listen to any topic.</td>
    <td><ul><li> Enable SROS / DDS Security Extension to authenticate and
encrypt DDS communications.</li></ul></td>
    <td class="success">Risk is mitigated if SROS is used.</td>
    <td> </td>
  </tr>

  <tr>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="success">✘</td>
    <td class="success">✘</td>
    <td class="danger">✓</td>
    <td>DDS participants are enumerated and fingerprinted to look for potential
vulnerabilities.</td>
    <td>
      <ul>
        <li>DDS Security Governance document must set `metadata_protection_kind`
to ENCRYPT to prevent malicious actors from observing communications.</li>
        <li>DDS Security Governance document must set
`enable_discovery_protection` to True to prevent malicious actors from
enumerating and fingerprinting DDS participants.</li>
        <li>DDS Security Governance document must set `enable_liveliness_protection`
to True</li>
      </ul>
    </td>
    <td class="warning">Risk is mitigated if DDS-Security is configured
appropriately.</td>
    <td> </td>
  </tr>

  <tr>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="success">✘</td>
    <td class="success">✘</td>
    <td class="danger">✓</td>
    <td>TurtleBot camera images are saved to a remote location controlled by the attacker.</td>
    <td>
      <ul>
        <li>DDS Security Governance document must set `metadata_protection_kind`
to ENCRYPT to prevent malicious actors from observing communications.</li>
        <li>DDS Security Governance document must set
`enable_discovery_protection` to True to prevent malicious actors from
enumerating and fingerprinting DDS participants.</li>
        <li>DDS Security Governance document must set `enable_liveliness_protection`
to True</li>
      </ul>
    </td>
    <td class="warning">Risk is mitigated if DDS-Security is configured
appropriately.</td>
    <td></td>
  </tr>
  <tr>
      <td class="danger">✓</td>
      <td class="danger">✓</td>
      <td class="danger">✓</td>
      <td class="success">✘</td>
      <td class="success">✘</td>
      <td class="danger">✓</td>
      <td>TurtleBot LIDAR measurements are saved to a remote location controlled by
  the attacker.</td>
      <td>
        Local communication using XRCE should be done over the loopback interface.
      </td>
      <td class="danger"> This doesn't protect the serial communication from the
        LIDAR sensor to the Raspberry Pi.
      </td>
      <td></td>
    </tr>

  <tr>
    <td rowspan="2">An attacker prevents a communication channel from being
usable.</td>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="success">✘</td>
    <td class="success">✘</td>
    <td class="success">✘</td>
    <td>Without SROS: any node can ""spam"" any other component.</td>
    <td>
      <ul>
        <li>Enable SROS to use the DDS Security Extension.
            This does not prevent nodes from being flooded but it ensures that only communication
            from allowed participants are processed.</li>
      </ul>
    </td>
    <td class="warning">Risk may be reduced when using SROS.</td>
    <td> </td>
  </tr>

  <tr>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="success">✘</td>
    <td class="success">✘</td>
    <td class="danger">✓</td>
    <td>A node can ""spam"" another node it is allowed to communicate with.</td>
    <td>
      <ul>
        <li>Implement rate limitation on topics</li>
        <li>Define a method for topics to declare their required bandwidth /
rate.</li>
      </ul>
    </td>
    <td class="danger">Mitigating risk requires additional work.</td>
    <td>How to enforce when nodes are malicious? Observe and kill?</td>
  </tr>

<tr><th colspan="11">Embedded / Software / Communication / Long-Range
Communication (e.g. WiFi, Cellular Connection)</th></tr>

  <tr>
    <td>An attacker hijacks robot long-range communication</td>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="success">✘</td>
    <td class="success">✘</td>
    <td class="success">✘</td>
    <td class="warning">✘/✓</td>
    <td>An attacker connects to the same unprotected WiFi network than a
TurtleBot.</td>
    <td>
      <ul>
        <li>Prevent TurtleBot from connecting to non-protected WiFi network</li>
        <li>SROS should always be used for long-range DDS communication.</li>
      </ul>
    </td>
    <td class="warning">Risk is reduced for DDS if SROS is used.
                        Other protocols may still be vulnerable.</td>
    <td>Enforcing communication though a VPN could be an idea (see PR2 manual
        for a reference implementation) or only DDS communication could be allowed on
        long-range links (SSH could be replaced by e.g. adbd and be only available
        using a dedicated short-range link).</td>
  </tr>

  <tr>
    <td>An attacker intercepts robot long-range communications (e.g. MitM)</td>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="success">✘</td>
    <td class="success">✘</td>
    <td class="success">✘</td>
    <td class="warning">✘/✓</td>
    <td>An attacker connects to the same unprotected WiFi network than a
TurtleBot.</td>
    <td>
      <ul>
        <li>Prevent TurtleBot from connecting to non-protected WiFi network</li>
        <li>SROS should always be used for long-range DDS communication.</li>
      </ul>
    </td>
    <td class="warning">Risk is reduced for DDS if SROS is used.
                        Other protocols may still be vulnerable.</td>
    <td> </td>
  </tr>

  <tr>
    <td>An attacker disrupts (e.g. jams) robot long-range communication
channels.</td>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="success">✘</td>
    <td class="success">✘</td>
    <td class="success">✘</td>
    <td class="warning">✘/✓</td>
    <td>Jam the WiFi network a TurtleBot is connected to.</td>
    <td>If network connectivity is lost, switch to cellular network.</td>
    <td class="danger">Mitigating is impossible on TurtleBot (no secondary
long-range communication system).</td>
    <td> </td>
  </tr>

<tr><th colspan="11">Embedded / Software / Communication / Short-Range
Communication (e.g. Bluetooth)</th></tr>

  <tr>
    <td>An attacker executes arbitrary code using a short-range communication
        protocol vulnerability.</td>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="success">✘</td>
    <td class="danger">✓</td>
    <td class="warning">✘/✓</td>
    <td>Attacker runs a blueborne attack to execute arbitraty code on the
TurtleBot Raspberry Pi.</td>
    <td></td>
    <td></td>
    <td>A potential mitigation may be to build a minimal kernel with e.g. Yocto
        which does not enable features the robot does not use.
        In this particular case, the TurtleBot does not require Bluetooth but OS images enable it
        by default.</td>
  </tr>

  <tr><th colspan="11">Embedded / Software / OS & Kernel</th></tr>

  <tr>
    <td rowspan="2">An attacker compromises the real-time clock to disrupt the
    kernel RT scheduling guarantees.</td>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="success">✘</td>
    <td class="success">✘</td>
    <td class="success">✘</td>
    <td class="warning">✘/✓</td>
    <td>A malicious node attempts to write a compromised kernel to
        <code>/boot</code></td>
    <td> </td>
    <td class="warning">TurtleBot / Zymbit Key integration will mostly mitigate
this threat.</td>
    <td>Some level of mitigation will be possible through Turtlebot / Zymkey
        integration.
        SecureBoot support would probably be needed to completely mitigate this
        threat.</td>
  </tr>

  <tr>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="success">✘</td>
    <td class="success">✘</td>
    <td class="success">✘</td>
    <td class="warning">✘/✓</td>
    <td>
    A malicious actor sends incorrect NTP packages to enable other attacks
    (allow the use of expired certificates) or to prevent the robot software
    from behaving properly (time between sensor readings could be miscomputed).
    </td>
    <td>
      <ul>
        <li><span markdown="1">
        [Implement NTP Best Practices][ntp_best_practices]</span></li>
        <li>Use a hardware RTC clock such as the one provided by the Zymbit
        key to reduce the system reliance on NTP.</li>
        <li>If your robot relies on GPS for localization purpose, consider
        using time from your GPS received (note that it opens the door to
        other vulnerabilities such as GPS jamming).</li>
      </ul>
    </td>
    <td class="warning">
    TurtleBot / Zymbit Key integration and following best practices for
    NTP configuration will mostly mitigate this threat.</td>
    <td> </td>
  </tr>

  <tr>
    <td>An attacker compromises the OS or kernel to alter robot data.</td>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="success">✘</td>
    <td class="success">✘</td>
    <td class="success">✘</td>
    <td class="warning">✘/✓</td>
    <td>A malicious node attempts to write a compromised kernel to
        <code>/boot</code></td>
    <td></td>
    <td class="warning">TurtleBot / Zymbit Key integration will mostly mitigate
this threat.</td>
    <td> </td>
  </tr>

  <tr>
    <td>An attacker compromises the OS or kernel to eavesdrop on robot
data.</td>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="success">✘</td>
    <td class="success">✘</td>
    <td class="success">✘</td>
    <td class="warning">✘/✓</td>
    <td>A malicious node attempts to write a compromised kernel to
<code>/boot</code></td>
    <td> </td>
    <td class="warning">TurtleBot / Zymbit Key integration will mostly mitigate
this threat.</td>
    <td> </td>
  </tr>

  <tr>
    <td rowspan="2">An attacker gains access to the robot OS through its
administration interface.</td>
    <td class="danger">✓</td>
    <td class="danger">✓</td>
    <td class="success">✘</td>
    <td class="success">✘</td>
    <td class="danger">✓</td>
    <td class="warning">✘/✓</td>
    <td>An attacker connects to the TurtleBot using Raspbian default username
and password (pi / raspberry pi)</td>
    <td>
      <ul>
        <li>Default password should be changed and whenever possible password
based authentication should be replaced by SSH key based authentication</li>
      </ul>
    </td>
    <td class="danger">Demonstrating a mitigation would require significant work.
                       Building out an image using Yocto w/o a default password could be a way
                       forward.</td>
    <td>SSH is significantly increasing the attack surface.
        Adbd may be a better solution to handle administrative access.</td>
  </tr>
…(발췌: 전체 202,769자 중 앞 106,682자)
```
