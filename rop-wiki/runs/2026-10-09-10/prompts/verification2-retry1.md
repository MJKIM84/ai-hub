(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-09-10
- date: 2026-10-09
- run_type: category_link (대분류 연결)
- 대상: 대분류 N. 보안·개인정보 페이지의 '다른 대분류와의 연결' 절(대분류 연결 실행). 게시된 세부영역 페이지를 근거로 다른 대분류와의 연결을 조사·서술한다. 스토리텔러는 그 절만 patches 로 바꾼다
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

### runs/2026-10-09-10/target.json

```json
{
  "run_id": "2026-10-09-10",
  "date": "2026-10-09",
  "weekday": "Fri",
  "run_number": 143,
  "run_type": "category_link",
  "forced": true,
  "target": {
    "area_no": null,
    "area_name": null,
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
  "selection_rationale": "CLI 지정 run_type=category_link"
}
```

### runs/2026-10-09-10/research.json

```json
{
  "run_id": "2026-10-09-10",
  "date": "2026-10-09",
  "run_type": "category_link",
  "target": {
    "area_no": null,
    "area_name": null,
    "category": "N. 보안·개인정보"
  },
  "gaps": [
    "N. 보안·개인정보 대분류 페이지의 '다른 대분류와의 연결' 절이 '아직 작성되지 않음' 상태다. 51. 인증·권한·격리, 52. 통신 보호·위협 관리·감사, 53. 개인정보·영상 데이터와 다른 16개 대분류의 연결이 정리되지 않았다",
    "51. 인증·권한·격리 페이지는 이전 분류(2026-09-25) 기준이라 C. 채팅 기반 구성·운영, D. 공간·지도 모델, J. 현장 운영·관제의 40. 운영 절차·요청 창구, P. 거버넌스·법규·사회의 58. 다사업자 책임·계약·데이터와 잇는 근거가 페이지 안에 없다",
    "51·52·53 페이지의 10절(다른 연구영역과의 연결)은 주제 페이지로 분리되어 있고 대분류 단위로 묶인 연결이 없다",
    "D. 공간·지도 모델 페이지는 N. 보안·개인정보와의 연결을 '근거 없음'으로 남겼다(지도 데이터의 접근 통제·개인정보)",
    "Q. 현장 유형별 적용 가운데 물류창고·상업 시설·기타 현장의 보안·개인정보 사례가 51·52·53 게시 페이지에 없다",
    "EU 사이버복원력법 보고 의무(2026-09-11 시행)와 EU 데이터법처럼 최근 시행된 규정이 게시 페이지에 반영되지 않았다"
  ],
  "research_questions": [
    "누가 어떤 로봇에 무엇을 시킬 수 있는지 통제하고, 데이터와 사람의 정보를 어떻게 지킬 것인가? [분류원문]",
    "외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가? [분류원문]",
    "51. 인증·권한·격리의 명령 권한·장비 인증은 B. 로봇 온톨로지(4·6·7)·F. 연동(20·22)·G. 계획·최적화(25)·H. 실행·협업·예외 복구(29)·K. 플랫폼 아키텍처·인프라(41)의 어느 인터페이스와 이어지는가? (oq-056, oq-082, oq-100, oq-113 관련)",
    "52. 통신 보호·위협 관리·감사의 위협·감사 기록은 C. 채팅 기반 구성·운영(12·13)·E. 사물·사람·실시간 상태(18)·J. 현장 운영·관제(37·38·40)·L. AI·학습 기술(44·47)·M. 안전(48·50)·O. 검증·도입·수명주기(54·55·57)와 어디서 만나는가? (oq-144, oq-246, oq-248, oq-291 관련)",
    "53. 개인정보·영상 데이터의 수집·보관 규칙은 D. 공간·지도 모델(15·16)·E. 사물·사람·실시간 상태(17·19)·L. AI·학습 기술(45·47)·P. 거버넌스·법규·사회(58·59·60)와 어떻게 이어지는가? (oq-259, oq-285, oq-214 관련)",
    "보안 인증·규제(IEC 62443, ISO 10218 개정, EU 사이버복원력법, EU 데이터법, 국내 로봇 보안모델)는 A. 기획·사업(1·2·3)에 어떤 요구를 넘기는가?",
    "N. 보안·개인정보의 적용 사례는 Q. 현장 유형별 적용의 일곱 현장 유형 가운데 어디에 근거가 있으며 한국 자료는 무엇이 있는가?"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ A. 기획·사업의 1. 기술·시장·업체 동향: 과학기술정보통신부와 한국인터넷진흥원(KISA)은 2026-03-05 로봇 보안모델 고도화판과 로봇 보안요구사항 해설서를 공개했고, 피지컬 AI 확산과 유럽·북미 사이버보안 규제 강화를 반영해 기업이 개발·수출 과정의 보안 요구를 파악하게 하는 것을 목적으로 밝혔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1373",
        "ref-1111"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "바이라인네트워크(2026-03-06): 로봇 분야는 기존 로봇 보안모델 고도화 버전과 로봇 보안요구사항 해설서를 공개, 유럽·북미 규제 강화 반영, 개발·수출 시 보안 요구 파악 지원. 구체 항목은 기사에 없음. 두 기사 모두 같은 정부 발표를 옮긴 것이라 독립 교차 확인으로 보지 않음",
      "as_of": "2026-03-05",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f2",
      "claim": "N. 보안·개인정보의 51. 인증·권한·격리 ↔ A. 기획·사업의 3. 경제성·조달·사업 모델: KUKA 는 iiQKA.OS2 운영체제와 KR C5-2 제어기 플랫폼이 IEC 62443-4-2 보안 수준 2(SL2) 인증을 받았고 로봇 제조사 가운데 처음이라고 2026-09-02 발표했으며, 발표문에는 인증 기관이 나오지 않는다.",
      "tag": "추정",
      "source_ids": [
        "ref-1375"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: KUKA 보도자료(Robotics Tomorrow 게재, 2026-09-02)는 'the first robotics manufacturer to achieve a Security Level 2 certification'이라 적고 인증 기관·EU 규정 언급은 없음",
      "as_of": "2026-09-02",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f3",
      "claim": "N. 보안·개인정보의 51. 인증·권한·격리 ↔ A. 기획·사업의 3. 경제성·조달·사업 모델: IEC 62443 이 보안 수준을 정하고 로봇 제어기 단위의 인증 발표가 나오고 있으므로, 로봇·플랫폼 조달 요구에 구성요소 보안 인증 여부와 목표 보안 수준을 넣는 일이 3. 경제성·조달·사업 모델로 넘어갈 것으로 보이나, 플릿 관리 소프트웨어 단위의 인증 사례는 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1105",
        "ref-1375"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "IEC 62443 은 구역·도관과 보안 수준(SL1~SL4)을 정함(52 페이지 7절). 로봇 제어기 인증 발표는 벤더 주장. 플릿 관리 소프트웨어 인증은 검색에서 '정렬(aligned)' 표현의 제조사 자료만 보였고 인증 근거는 찾지 못함",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f4",
      "claim": "N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ A. 기획·사업의 2. 사용 사례·요구·책임 범위: 52. 통신 보호·위협 관리·감사 페이지는 ROP 가 자신이 여는 연결의 보안과 전체 연결 구조의 위협 모델을 맡고 로봇 제어기·펌웨어와 현장 망 보안은 제조사·시설 IT/OT 쪽 연계 대상으로 두므로, 이 보안 책임 경계가 2. 사용 사례·요구·책임 범위의 책임 범위 정의에 들어가야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1114",
        "ref-1107",
        "ref-009"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "52 페이지 9절: 이종 제조사를 잇는 ROP 는 자신이 여는 연결과 전체 연결 구조의 보안을 맡고 제어기·펌웨어·현장 망은 연계 대상으로 두는 것으로 보인다 (재인용: 2026-09-30-11)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f5",
      "claim": "N. 보안·개인정보의 51. 인증·권한·격리 ↔ B. 로봇 온톨로지의 4. 이기종 로봇 등록: VDA 5050 3.0.0 은 로봇이 새 인증서 묶음을 내려받아 활성화하게 하는 즉시 동작 updateCertificate 를 두고, 내려받기도 TLS 로 보호해야 하며 활성화 전에 인증서 체인을 검증하는 것이 바람직하다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "6.2.3.3절: \"The download shall be secured via TLS as well, since the sender of the instantAction cannot be verified.\" 인증 기관·인증서·키 내려받기 링크를 선택 매개변수로 둠 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "N. 보안·개인정보의 51. 인증·권한·격리 ↔ B. 로봇 온톨로지의 4. 이기종 로봇 등록·7. 온톨로지 검증·변경 관리, O. 검증·도입·수명주기의 57. 자산·소프트웨어 수명주기 관리: 로봇마다 인증서 교체 지원 여부와 인증서 판·만료를 등록 정보로 두고 교체 이력을 판 관리와 함께 다루면 인증서 교체 대상과 시점을 추적할 수 있을 것으로 보이며, 교체 승인과 실패 때 되돌림 책임은 열린 질문(oq-113)으로 남는다.",
      "tag": "추정",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "VDA 5050 updateCertificate 는 로봇별 인증서 교체를 관제 명령으로 다루고 실패 상태를 보고하게 함. 등록 항목·판 관리로 다루는 공개 구현은 확인하지 못함",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ B. 로봇 온톨로지의 4. 이기종 로봇 등록: 53. 개인정보·영상 데이터 페이지가 카메라 유무·촬영 사실 표시 수단·영상 전송 경로 기록과 로봇 인지 출력 필드 축소를 ROP 직접 범위로 보므로, 이런 개인정보 관련 속성이 4. 이기종 로봇 등록의 등록 항목으로 넘어갈 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1145",
        "ref-588"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "53 페이지 9절 표: 로봇 등록 정보에 카메라 유무·촬영 사실 표시 수단·영상 전송 경로를 기록하고 인지 출력 필드를 과업에 필요한 만큼으로 줄이는 규칙 (재인용: 2026-09-30-16)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f8",
      "claim": "N. 보안·개인정보의 51. 인증·권한·격리 ↔ B. 로봇 온톨로지의 6. 온톨로지 기반 시스템·로봇 연동: ROS 2 접근 제어 정책은 인클레이브별로 토픽·서비스·액션 단위의 허용·거부를 두므로, '진단은 허용하고 이동은 막는' 명령 단위 권한을 걸려면 6. 온톨로지 기반 시스템·로봇 연동이 능력을 실제 명령에 묶을 때 권한 정책과 같은 명령 식별자를 공유해야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-579",
        "ref-405"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "51 페이지 5절: 사용자 역할(OIDC), ROS 2 인클레이브별 토픽·서비스·액션 허용·거부, MQTT 토픽 ACL 의 세 층으로 권한을 표현할 수 있음. 능력 모델과 권한 정책을 잇는 공개 사례는 확인하지 못함 (재인용: 2026-09-25-64)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f9",
      "claim": "N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ C. 채팅 기반 구성·운영의 13. 대화형 기능의 신뢰·기반: OWASP LLM01:2025 는 프롬프트 주입을 사용자가 직접 넣는 직접 주입과 문서·웹 같은 외부 내용에 숨은 지시가 들어오는 간접 주입으로 나누고 완화책을 정리한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1106"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "52 페이지 7절: OWASP LLM01:2025 프롬프트 주입 — 직접·간접 주입 구분과 완화책 (재인용: 2026-09-30-11)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f10",
      "claim": "N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션: 대규모 언어 모델을 통합한 이동로봇 시스템에 대한 프롬프트 주입 공격 연구(Zhang 외, 2024-08)와 다중 에이전트 로봇 시스템에서 프롬프트가 로봇을 제어할 때의 프롬프트 주입 공격 연구(Nagaraja 외, 2026-08)가 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-1113",
        "ref-1112"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "참고문헌 제목 기준: 'A Study on Prompt Injection Attack Against LLM-Integrated Mobile Robotic Systems'(2024-08), 'When Prompts Control Robots: Prompt Injection Attacks in Multi-Agent Robotic Systems'(2026-08). 수치는 이번에 확인하지 않음",
      "as_of": "2026-08",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f11",
      "claim": "N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ C. 채팅 기반 구성·운영의 13. 대화형 기능의 신뢰·기반·L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획: Robey 외는 언어 모델이 제어하는 로봇에서 탈옥 알고리즘 RoboPAIR 의 공격 성공률이 자주 100%에 이르렀다고 보고했고, Ravichandran 외의 RoboGuard 는 최악의 탈옥 공격에서 위험 계획 실행을 92% 이상에서 3% 미만으로 줄였다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-857",
        "ref-700"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "두 수치 모두 저자 보고값이며 독립 재현은 확인되지 않음. RoboPAIR: Clearpath Jackal·Unitree Go2 등. RoboGuard: 신뢰 기점 LLM + 시간 논리 제약 + 제어 합성 (재인용: 2026-10-09-08)",
      "as_of": "2025-03",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f12",
      "claim": "N. 보안·개인정보의 51. 인증·권한·격리 ↔ C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션: Open-RMF REST API 를 언어 모델 도구로 노출하는 MCP 서버(Nayantra) 같은 구조에서는 탈옥된 모델이 해로운 동작을 낼 수 있으므로, 모델에 넘기는 도구·로봇·구역 권한을 최소로 제한하는 접근 통제가 분류 원문 C 주석의 '사람이 확인·승인한 계획만 실행' 원칙과 함께 두 대분류의 경계가 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-854",
        "ref-857"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Nayantra: Open-RMF REST API 를 LLM 이 호출하는 도구로 노출하는 MCP 서버 + 영어 지시를 RMF 임무로 바꾸는 에이전트(2026-07-02 발표 안내). 권한 제한 구성은 안내문에 없음 (재인용: 2026-10-09-08)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f13",
      "claim": "N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션: '사람이 확인·승인한 계획만 실행'이 지켜졌음을 사후에 보이려면 누가 어떤 계획을 언제 승인했는지를 변조 탐지가 가능한 감사 기록으로 남겨야 할 것으로 보이며, 자율 에이전트 행동을 블록체인 기록과 언어 모델 설명으로 추적하는 구조 연구(2024-03)가 그 후보다.",
      "tag": "추정",
      "source_ids": [
        "ref-1110"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Fernández-Becerra 외(2024-03) 'Enhancing Trust in Autonomous Agents: An Architecture for Accountability and Explainability through Blockchain and Large Language Models'. 대화 승인 기록에 적용한 사례는 확인하지 못함(oq-248 관련)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "완료·인계",
      "source_unopened": true
    },
    {
      "id": "f14",
      "claim": "N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ D. 공간·지도 모델의 16. 장소 의미·지도 관리: 개인정보보호위원회가 2026-09-14 발표한 로봇청소기 5개 브랜드 점검에서 집 내부 구조를 나타내는 지도 정보는 모든 제품이 기기에 저장하고 스마트폰에는 저장하지 않았으며 일부 제품은 서버에도 저장했고, 일부 사업자는 로봇청소기 접근통제와 개인정보 전송 암호화가 미흡했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1372",
        "ref-1141"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "바이라인네트워크(2026-09-14): 점검 대상 로보락·삼성전자·LG전자·에코백스·샤오미(2025-03 기준 최신 모델), 개인정보위는 \"특별한 개인정보 침해 위험은 확인되지 않았다\"고 밝힘. 지도 저장 위치는 이 기사에서만 확인",
      "as_of": "2026-09-14",
      "site_type": "가정",
      "flow_item": "작업 대상",
      "source_unopened": false
    },
    {
      "id": "f15",
      "claim": "N. 보안·개인정보의 51. 인증·권한·격리·53. 개인정보·영상 데이터 ↔ D. 공간·지도 모델의 15. 지도·공간·위치 모델·16. 장소 의미·지도 관리: 건물 내부 지도가 개인정보 점검 대상 정보로 다뤄지고 VDA 5050 이 지도를 관제가 지정한 링크에서 내려받게 하므로, ROP 가 보관·배포하는 지도의 저장 위치·전송 암호화·접근 권한을 정하는 일이 두 대분류를 잇는 지점이 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1372",
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "로봇청소기 점검은 영상·음성·사진과 함께 지도 정보의 수집·전송·저장을 점검했다. VDA 5050 은 downloadMap 에 지도 내려받기 링크를 둠(D 페이지 기준). 업무 시설 지도의 접근 통제를 다룬 기관 자료는 찾지 못함",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성: Shen 외(2026-09, 프리프린트)는 ROS 2 에서 환경 변수 하나를 바꾸면 사전 빌드된 훅이 텔레메트리·제어 신호를 발행 전에 가로채고 주입할 수 있음을 보였고, Secure ROS 2 를 쓴 실제 Franka 로봇팔에서 약 3 ms 지터로 위조 텔레메트리를 넣어 AI 기반 탐지기 상대로도 87% 성공했다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1374"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2609.08280 초록: 원격 증명이 발행 전에 이미 오염될 수 있는 센서 데이터에 기대므로 물리 동작과 디지털 기록 사이의 신뢰 경계가 깨진다. 저자들은 ROS 2 개발진에 보고. 저자 보고값, 독립 재현 미확인",
      "as_of": "2026-09-08",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f17",
      "claim": "N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성·J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석: 로봇이 보고하는 상태가 통신 보호 이전 단계에서 위조될 수 있고 위치 스푸핑이 배정을 무너뜨린다는 연구가 있으므로, 18. 실시간 세계 상태·데이터 일관성의 상태 신뢰도 판단과 38. 모니터링·이상 탐지·원인 분석은 암호화된 보고만 믿지 말고 설비 센서·다른 로봇 관측과 교차 확인해야 할 것으로 보인다(oq-082).",
      "tag": "추정",
      "source_ids": [
        "ref-1374",
        "ref-494"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Shen 외: Secure ROS 2 에서도 발행 전 훅으로 위조 가능. Francos 외: 위치 스푸핑 오염 에이전트를 실행 행동 증거로 가려 계획에서 뺌(GPS 스푸핑·택시 수요 실험). 이동로봇 플릿 적용 사례는 미확인",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "예외·성과",
      "source_unopened": false
    },
    {
      "id": "f18",
      "claim": "N. 보안·개인정보의 51. 인증·권한·격리·53. 개인정보·영상 데이터 ↔ E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적: 병원 운반 로봇 Zena RX 는 생체 인식과 직원 PIN 으로 잠금 칸을 연다고 제조사가 밝히고 공동주택 배달 로봇 도입 계획은 비밀번호로 적재함을 열게 했으므로, '누구에게 넘겼는가' 기록은 인증 수단과 생체·전화번호 처리 규칙에 기댈 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1299",
        "ref-1301"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: Zena RX 생체 인식·PIN 잠금 칸(2024-04-29 보도자료, 독립 확인 없음). 2020-07 기사: 라이더·고객이 로봇 화면에 비밀번호를 눌러 적재함을 연다는 계획 (재인용: 2026-10-09-03)",
      "as_of": "2026-10-09",
      "site_type": "병원",
      "flow_item": "완료·인계",
      "source_unopened": true,
      "vendor_claim": true
    },
    {
      "id": "f19",
      "claim": "N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ E. 사물·사람·실시간 상태의 19. 사람·보행자 모델: ROS 규약 제안 REP-155(Draft)는 사람마다 영속 ID 를 두고 얼굴·몸·음성 ID 를 후보 대응으로 연결하며, 개인정보·동의는 다루지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1173"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "E 페이지 연결 절: REP-155(2022-01-11 작성)는 영속 사람 ID 와 얼굴·몸·음성 ID 연결을 정하고 개인정보·동의는 다루지 않음 (재인용: 2026-10-09-03)",
      "as_of": "2022-01-11",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f20",
      "claim": "N. 보안·개인정보의 51. 인증·권한·격리 ↔ F. 연동의 20. 로봇·제조사 관제 연동: 2025-08 한 보안 연구자는 Pudu Robotics 로봇 관리 소프트웨어가 유효한 인증 토큰만 확인하고 그 뒤 권한을 검사하지 않아, 교차 사이트 스크립팅이나 체험 계정으로 얻은 토큰으로 주문을 바꾸고 로봇을 다른 위치로 보내고 이름을 바꿀 수 있었다고 공개했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1368",
        "ref-1369"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "The Register(2025-08-29)·Hackmag(2025-09-05): 대상 예시 BellaBot(식당 서빙)·FlashBot. 두 기사 모두 연구자 블로그 공개를 옮긴 것이라 독립 교차 확인으로 보지 않음. 실제 악용 사례는 보도에 없음",
      "as_of": "2025-08-29",
      "site_type": "상업 시설",
      "flow_item": "예외·성과"
    },
    {
      "id": "f21",
      "claim": "N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ F. 연동의 20. 로봇·제조사 관제 연동: 미국 CISA 권고 ICSA-22-102-05(2022-04-12)는 병원 자율이동로봇 TUG 를 제어하는 Home Base Server 에서 인증 없이 웹소켓으로 로봇을 제어할 수 있는 취약점(CVE-2022-1070, CVSS 9.8)과 인가 누락 취약점을 공개했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1107"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "52 페이지 5절 병원 사례: 버전 24 이전 전체, 인가 누락 CVE-2022-1066·CVE-2022-26423(CVSS 8.2), 완화책은 버전 24 갱신·방화벽·인터넷 비노출·VPN (재인용: 2026-09-30-11)",
      "as_of": "2022-04-12",
      "site_type": "병원",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f22",
      "claim": "N. 보안·개인정보의 51. 인증·권한·격리 ↔ F. 연동의 20. 로봇·제조사 관제 연동: 식당 서빙 로봇과 병원 운반 로봇 사례 모두 제조사 플릿 서버·관리 API 의 인증·인가 결함이 로봇 제어로 이어졌으므로, ROP 가 제조사 관제를 연결할 때 연결 계정의 권한 범위와 인가 확인을 연동 승인 조건으로 둬야 할 것으로 보인다(oq-100).",
      "tag": "추정",
      "source_ids": [
        "ref-1368",
        "ref-1107"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Pudu: 인증 뒤 권한 검사 없음. TUG: 인가 누락·인증 없는 제어 채널. 연동 승인 기준으로 인가 시험을 정한 공개 기준은 확인하지 못함",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f23",
      "claim": "N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ F. 연동의 21. 상호운용 표준·적합성: VDA 5050 3.0.0 은 범위 절에서 보안 통신·데이터 보호의 메커니즘·기술·절차를 정하지 않는다고 밝히고, 프로토콜 보안은 브로커 구성으로 다뤄야 하며 이 지침에서는 다루지 않는다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "2장 범위·4.1절 연결 처리·보안·QoS 의 요지. 다만 6.2.3.3절은 보안상 관제 통신을 보호해야 하며 MQTT 브로커 통신은 보통 TLS 로 보호한다고 적음 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ F. 연동의 21. 상호운용 표준·적합성: 상호운용 규격이 통신 보안을 범위 밖 브로커 구성에 맡기므로 21. 상호운용 표준·적합성의 적합성 시험과 브로커·API 의 상호 인증·TLS 설정 확인은 별도 경로로 관리해야 할 것으로 보이며, 그 최소 요구를 정한 공개 보안 프로파일은 확인하지 못했다(oq-246).",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-1105"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "VDA 5050: 프로토콜 보안은 브로커 구성 몫. IEC 62443 은 구역·도관과 보안 수준을 정하지만 로봇 관제 브로커 프로파일을 정하지 않음(이번 확인 범위)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f25",
      "claim": "N. 보안·개인정보의 51. 인증·권한·격리 ↔ F. 연동의 22. 설비·건물 시스템 연동: 승강기 같은 설비를 조작하는 서비스 로봇(FlashBot)도 같은 관리 API 결함의 대상이 될 수 있다고 보도되었으므로, 로봇 관제·설비 어댑터 구성요소를 SROS 2 인클레이브처럼 별도 신원·접근 규칙으로 나눠 설비 명령 권한을 제한하는 설계가 두 대분류의 경계가 될 것으로 보인다(oq-056).",
      "tag": "추정",
      "source_ids": [
        "ref-1369",
        "ref-405"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Hackmag: FlashBot 은 승강기 같은 시스템을 조작하며 사무실 시스템 피해 가능성은 연구자·기자의 평가. Open-RMF 문서: 같은 신원·접근 규칙을 공유하는 SROS 2 인클레이브로 구성요소 권한을 나눔",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f26",
      "claim": "N. 보안·개인정보의 51. 인증·권한·격리 ↔ G. 계획·최적화의 25. 작업 배정 — MRTA: Francos 외(2026-08, 프리프린트)는 위치 스푸핑으로 오염된 에이전트가 롤아웃 기반 다중 로봇 배정·경로 계획의 비용 개선을 없앨 수 있다고 보고, 스푸핑 공격 모델과 탐지된 적대 에이전트를 이후 계획에서 빼는 방법을 제안했다.",
      "tag": "사실",
      "source_ids": [
        "ref-494"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "G 페이지 연결 절: 실험은 GPS 스푸핑 데이터와 택시 수요로 했으며 물류센터 적용은 확인되지 않음 (재인용: 2026-09-25-55)",
      "as_of": "2026-08",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f27",
      "claim": "N. 보안·개인정보의 51. 인증·권한·격리 ↔ G. 계획·최적화의 25. 작업 배정 — MRTA·27. 다중 로봇 경로·교통 관리 — MAPF: 제조사 관리 API 를 거쳐 주문을 바꾸거나 로봇 위치를 옮길 수 있었던 사례가 있으므로, ROP 의 배정·교통 계획은 자신이 내리지 않은 임무 변경·이동을 로봇 상태에서 감지해 해당 로봇을 계획에서 보류하는 규칙이 필요할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1368"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "The Register: 공격자가 주문을 리셋·변경하고 로봇을 새 위치로 옮길 수 있었다. 계획 쪽 감지 규칙을 다룬 자료는 확인하지 못함",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f28",
      "claim": "N. 보안·개인정보의 51. 인증·권한·격리 ↔ H. 실행·협업·예외 복구의 29. 명령·작업 실행의 신뢰성: VDA 5050 3.0.0 에서 updateCertificate 동작은 실행 중에는 인증서를 내려받아 설치 중이라는 상태로, 실패하면 내려받기 또는 설치 실패로 보고되므로, 보안 명령도 일반 명령처럼 실행 확인·실패 처리 대상이 된다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "6.2.3.2절 동작 상태: RUNNING 'Mobile robot is downloading and installing certificates', FAILED 'Download or installation failed.' (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f29",
      "claim": "N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성: 식당 서빙 로봇 관리 API 결함으로 영업 중 플릿 전체 작업을 취소하거나 멈출 수 있었다고 보도되었으므로, 보안 사고로 플릿 일부·전체를 격리하고 수동 운영으로 넘어가는 시나리오가 32. 예외 복구·재계획·업무 연속성의 복구 절차에 들어가야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1368",
        "ref-1369"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "The Register·Hackmag: 플릿 전체 정지(DoS 형태) 가능성은 연구자·매체의 평가이며 실제 사고는 보도되지 않음",
      "as_of": "2026-10-09",
      "site_type": "상업 시설",
      "flow_item": "예외·성과"
    },
    {
      "id": "f30",
      "claim": "N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈: Carr 외(2022)는 ROS 로 구동되는 시스템에서 디지털 트윈에 대한 중간자 공격이 물리 로봇의 실패로 이어질 수 있으며, 이는 산업용 로봇팔과 자율이동로봇 모두에 해당한다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1242"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "'Attacking Digital Twins of Robotic Systems to Compromise Security and Safety'(arXiv, 2022-11-17) (재인용: 2026-10-09-09)",
      "as_of": "2022-11-17",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f31",
      "claim": "N. 보안·개인정보의 52. 통신 보호·위협 관리·감사·53. 개인정보·영상 데이터 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현: 가정한 미래를 실험하는 시뮬레이션과 실제 상황 재현에 운영 기록·영상을 입력으로 쓰면 그 기록의 무결성과 '재현' 목적의 이용 범위를 함께 정해야 할 것으로 보이며, 이는 현재 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성의 상태 신뢰도 문제(f17)와 구분된다.",
      "tag": "추정",
      "source_ids": [
        "ref-1242",
        "ref-588"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "디지털 트윈 공격이 물리 실패로 이어질 수 있다는 보고와, 안내서가 수집 목적과 관련 없는 이용(가명처리 없는 AI 학습 등)에 예측 가능성을 따지는 점을 근거로 한 추정",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f32",
      "claim": "N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ J. 현장 운영·관제의 37. 관제 화면·실행 기록: Fernández-Becerra 외(2024-03)는 자율 에이전트의 행동을 블록체인 기반 기록과 대규모 언어 모델 설명으로 남겨 책임 추적성과 설명 가능성을 높이는 구조를 제안했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1110"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "52 페이지 9절이 감사 기록 근거로 인용. 수백 대 규모의 지연·저장 비용은 oq-248 로 열려 있음 (재인용: 2026-09-30-11)",
      "as_of": "2024-03",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f33",
      "claim": "N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ J. 현장 운영·관제의 37. 관제 화면·실행 기록: 업계 해설에 따르면 EU 기계류 규정 (EU) 2023/1230 은 변조 보호, 개입 증거 기록, 안전 소프트웨어 판 추적 로그를 요구하며 2027-01-20 전면 적용된다.",
      "tag": "사실",
      "source_ids": [
        "ref-1109"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "52 페이지 7절 표의 EU 기계류 규정 행(업계 해설 기준). 규정 원문(ref-555)은 열지 못함. 오케스트레이션 플랫폼에 미치는지는 oq-249 (재인용: 2026-09-30-11)",
      "as_of": "2026-08-27",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f34",
      "claim": "N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ J. 현장 운영·관제의 40. 운영 절차·요청 창구: Pudu 사례에서 연구자의 신고(2025-08-12 시작)는 보안 신고 창구가 없어 응답을 받지 못하다가 고객사(Skylark Holdings·Zensho)에 알린 뒤에야 처리되었고, 제조사는 이후 취약점을 고치고 보안 대응 센터와 신고 주소를 만들었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1368",
        "ref-1369"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "The Register: 제조사는 신고 창구 부재가 대응을 늦췄다고 밝히고 연구자에게 1만 달러 포상금을 줌. Hackmag: 제조사는 첫 메일이 수신자에게 닿지 않았다고 설명",
      "as_of": "2025-09-05",
      "site_type": "상업 시설",
      "flow_item": "예외·성과"
    },
    {
      "id": "f35",
      "claim": "N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ J. 현장 운영·관제의 40. 운영 절차·요청 창구·O. 검증·도입·수명주기의 57. 자산·소프트웨어 수명주기 관리·P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스: EU 사이버복원력법에 따라 2026-09-11 부터 디지털 요소 제품 제조자는 적극 악용되는 취약점과 중대 사고를 ENISA 단일 보고 플랫폼으로 알려야 하며, 인지 후 24시간 안에 조기 경보, 72시간 안에 통지, 취약점은 시정 조치가 나온 뒤 14일 안에 최종 보고를 낸다.",
      "tag": "사실",
      "source_ids": [
        "ref-1228"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "집행위원회 CRA reporting 페이지(2026-09-11 갱신): 중대 사고 최종 보고는 72시간 통지 뒤 한 달 안. 오픈소스 관리자(steward)는 2027-12-11 부터. 규정 원문 제14조는 열지 않음",
      "as_of": "2026-09-11",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f36",
      "claim": "N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ J. 현장 운영·관제의 40. 운영 절차·요청 창구: 신고 창구가 없던 제조사 사례와 24·72시간 보고 시한을 함께 보면, 여러 제조사 로봇을 운영하는 현장의 요청 창구에 보안 취약점·사고 접수와 제조사·ROP 사업자 사이 통보 경로를 두는 일이 40. 운영 절차·요청 창구로 넘어갈 것으로 보이며, 플랫폼 사업자의 보고 의무 해당 여부는 열린 질문(oq-291)이다.",
      "tag": "추정",
      "source_ids": [
        "ref-1228",
        "ref-1368"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "CRA 보고 의무는 제조자에 걸림. 로봇 제조사·플랫폼 사업자·현장 운영사 사이 통보 분담을 정한 자료는 확인하지 못함",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f37",
      "claim": "N. 보안·개인정보의 51. 인증·권한·격리 ↔ K. 플랫폼 아키텍처·인프라의 41. 플랫폼 아키텍처·외부 API: Open-RMF 문서는 웹 대시보드를 TLS 로 제공하고 OIDC 로 사용자 역할을 담은 서명 토큰을 API 서버에 보내 역할에 따라 접근을 허용하며, ROS 2 쪽 구성요소는 SROS 2 인클레이브로 권한을 나눈다고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-405"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Open-RMF 보안 장의 두 층(ROS 2 부분 SROS 2, 웹 대시보드 TLS·OIDC·역할 기반 접근 통제) (재인용: 2026-09-25-55)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f38",
      "claim": "N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조: ROS 2 는 DDS 보안 규격의 인증·접근 통제·암호화 플러그인을 쓰고, ROS 2 위협 모델 초안은 보안이 꺼진 시스템에서는 어떤 노드든 어떤 토픽에나 발행할 수 있어 신원 위조와 명령 가로채기가 가능하다고 정리한다.",
      "tag": "사실",
      "source_ids": [
        "ref-009",
        "ref-010"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "51 페이지 3절·F 페이지 연결 절. 두 출처는 서로 다른 내용(보안 장치 / 위협)을 다룸 (재인용: 2026-09-25-64)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f39",
      "claim": "N. 보안·개인정보의 51. 인증·권한·격리·53. 개인정보·영상 데이터 ↔ K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포: 2026-09-14 로봇청소기 점검 보도에 따르면 개인정보보호위원회는 점검 후속 조치로 접근권한 부여 내역 보관 기간을 200일에서 3년으로, 접속기록 보관 기간을 90일에서 2년 이상으로 늘리도록 했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1372"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "바이라인네트워크(2026-09-14) 기사 기준. 이 조치의 대상(점검 사업자 한정인지)과 근거 조항은 기사에 없어 미확인(oq-214 관련)",
      "as_of": "2026-09-14",
      "site_type": "가정",
      "flow_item": "제약"
    },
    {
      "id": "f40",
      "claim": "N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ L. AI·학습 기술의 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영: 개인정보보호위원회는 2023-11 자율주행차·이동형 로봇 개발에 영상데이터 원본 활용을 허용하는 방향을 밝혔고, 2026-05-06 ICT 규제샌드박스 심의위원회는 배달로봇 카메라 원본 영상을 AI 학습에 쓰는 과제에 연구 목적 내 활용·개인 식별 금지·제3자 제공 금지 등을 조건으로 실증특례를 승인했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1138",
        "ref-1263"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "두 출처는 서로 다른 시점의 조치를 다룸. 2026-05 승인 과제는 뉴빌리티 '영상정보 원본 활용 자율주행 배달 로봇 시스템 고도화'(기사 기준) (재인용: 2026-10-09-08)",
      "as_of": "2026-05-06",
      "site_type": "실외",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f41",
      "claim": "N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ L. AI·학습 기술의 47. AI·학습·적응과 모델 운영: EU AI Act 제12조는 고위험 AI 시스템이 수명 기간 동안 사건 기록(로그)을 자동으로 남길 수 있어야 하고, 위험 상황·실질적 변경 식별, 시판 후 감시, 배포자의 운영 감시에 필요한 사건을 기록하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-863"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "AI Act Service Desk 제12조 페이지. ROP 의 AI 구성요소가 고위험에 해당하는지는 oq-106·oq-143 로 열림 (재인용: 2026-10-09-08)",
      "as_of": "2024-06-13",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f42",
      "claim": "N. 보안·개인정보의 51. 인증·권한·격리·52. 통신 보호·위협 관리·감사 ↔ M. 안전의 50. 안전 표준·인증·사고 조사: 산업용 로봇 안전 표준 ISO 10218-1/-2 의 2025년 개정판에는 사이버보안 요구가 새로 들어갔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1116",
        "ref-1076"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "업계 해설과 2011·2025 판 비교 논문이 같은 내용을 말함. 조항 번호는 미확인(oq-102) (재인용: 2026-10-09-09)",
      "as_of": "2026-09-18",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f43",
      "claim": "N. 보안·개인정보의 51. 인증·권한·격리·53. 개인정보·영상 데이터 ↔ M. 안전의 50. 안전 표준·인증·사고 조사: 서비스 로봇 안전 표준 ISO 13482 개정 초안(ISO/DIS 13482:2024, DIN EN ISO 13482 2024-10 초안)은 사이버보안과 데이터 보호 절을 새로 넣었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1260"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "DIN Media 초안 소개 기준. 최종판에 남았는지는 미확인(oq-254) (재인용: 2026-10-09-09)",
      "as_of": "2024-10",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f44",
      "claim": "N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ M. 안전의 48. 안전·위험 관리: Quarta 외(IEEE S&P 2017)는 널리 쓰이는 산업용 로봇 제어기의 소프트웨어 취약점과 구조적 결함으로 제어 정확성과 작업자 안전 요구를 무너뜨릴 수 있음을 실험으로 보인 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1114"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "52 페이지 5절 제조 공장 사례(원문 미열람, 검색 결과 요약 기준). 제어기 보안은 로봇 제조사 쪽 연계 대상 (재인용: 2026-09-30-11)",
      "as_of": "2017",
      "site_type": "제조 공장",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f45",
      "claim": "N. 보안·개인정보의 51. 인증·권한·격리 ↔ M. 안전의 48. 안전·위험 관리: 산업용·서비스 로봇 안전 표준에 사이버보안과 데이터 보호가 들어오면서, ROP 가 내리는 원격 정지·재개·구역 변경 명령의 권한 통제가 안전 평가 대상이 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1116",
        "ref-1260"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "M. 안전 연결 실행의 같은 추정. 로봇 자체 안전 기능은 연계 대상 (재인용: 2026-10-09-09)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f46",
      "claim": "N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ O. 검증·도입·수명주기의 57. 자산·소프트웨어 수명주기 관리: ROS 2 위협 모델 초안은 빌드 팜과 서드파티 구성요소를 통한 공급망 위협을 주요 위협으로 들고, Shen 외(2026-09)는 제3자 Docker 컨테이너·보조 도구에 대한 폭넓은 의존을 이용해 악성 훅이 든 패키지를 퍼뜨릴 수 있다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-010",
        "ref-1374"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Shen 외 초록: 'the widespread reliance on third-party Docker containers and auxiliary tools'. 두 출처는 같은 방향이나 다른 내용이라 교차 확인으로 보지 않음",
      "as_of": "2026-09-08",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f47",
      "claim": "N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ O. 검증·도입·수명주기의 55. 현장 조사·설치·시운전: ROS 2 위협 모델 초안이 기본 자격증명을 쓰는 SSH 같은 원격 접속을 권한 상승 경로로 들므로, 설치·시운전 점검 항목에 기본 자격증명 변경과 원격 접속 범위 확인이 들어가야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-010"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "51 페이지 3절: 기본 자격증명을 쓰는 SSH 같은 원격 접속을 권한 상승 경로로 듦. 시운전 점검표에 넣은 공개 사례는 확인하지 못함",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f48",
      "claim": "N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ O. 검증·도입·수명주기의 54. 시험·형식 검증·벤치마크: 2025년 한국인터넷진흥원·한국소비자원의 로봇청소기 6종 점검은 모바일앱 보안·정책 관리·기기 보안 3개 영역 40개 항목으로 이루어졌다고 보도되어, 로봇 보안 시험 항목의 국내 참고 틀이 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-969"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "52 페이지 5절 가정 사례(2025-10-31 기사 기준, 기관 보도자료 원문 미확인). 다중 로봇 관제 플랫폼에 같은 틀을 쓴 사례는 없음",
      "as_of": "2025-10-31",
      "site_type": "가정",
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f49",
      "claim": "N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ P. 거버넌스·법규·사회의 58. 다사업자 책임·계약·데이터: EU 데이터법은 2025-09-12 부터 적용되며, 로봇·산업 기계 같은 연결 제품의 사용자가 사용으로 생긴 데이터에 접근해 직접 쓰거나 제3자와 공유할 수 있게 하고, 데이터 보유자(보통 제조사)는 사용자와 계약을 두고 생성 데이터 종류·양·수집 빈도를 알려야 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1376"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "집행위원회 'Data Act explained': 연결 제품 예로 robots, industrial machines 를 듦. 영업비밀 근거 제공 거부는 심각한 경제적 피해 가능성이 높을 때만, 거부 시 당국 통지",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f50",
      "claim": "N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ P. 거버넌스·법규·사회의 58. 다사업자 책임·계약·데이터: 여러 제조사 로봇의 데이터를 모아 관제하는 ROP 사업자가 데이터법상 사용자·제3자 가운데 어느 쪽이고 개인정보 처리에서 운영자·수탁자 가운데 어느 쪽인지가 계약으로 정해야 할 쟁점이 될 것으로 보인다(oq-259).",
      "tag": "추정",
      "source_ids": [
        "ref-1376",
        "ref-588"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "데이터법은 데이터 보유자·사용자·제3자를 구분하고, 국내 안내서는 운영 사업자와 수탁자 의무를 구분함. 플랫폼 사업자 지위를 다룬 해석은 확인하지 못함",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f51",
      "claim": "N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스: 개인정보보호위원회 이동형 영상정보처리기기 안내서 공개 보도와 법률사무소 해설은 카메라를 단 자율주행차·배달로봇이 외부에 촬영 사실을 표시하고 명확히 거부하는 사람의 의사를 받아들여야 한다고 전한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1136",
        "ref-588"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "53 페이지 5절 실외 사례. 두 출처 모두 같은 안내서 발표를 옮긴 것이라 독립 교차 확인으로 보지 않음 (재인용: 2026-09-30-16)",
      "as_of": "2024-10-14",
      "site_type": "실외",
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f52",
      "claim": "N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ P. 거버넌스·법규·사회의 60. 노동·수용성·접근성·Q. 현장 유형별 적용의 61. 물류창고: 프랑스 개인정보 감독기관 CNIL 은 2023-12-27 결정(2024-01-23 공표)으로 Amazon France Logistique 에 3,200만 유로 과징금을 부과했는데, 물류창고 작업자 스캐너 기록으로 10분 넘는 비활동을 실시간 경보하고 1.25초 안의 빠른 스캔을 표시하는 지표와 모든 데이터·지표의 31일 보관을 과도하다고 보았다.",
      "tag": "사실",
      "source_ids": [
        "ref-1370",
        "ref-1371"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "Silicon UK(2024-01-23)와 CNIL 공지(검색 결과 요약)가 금액·지표를 같게 전함. 로봇이 아니라 작업자 휴대 스캐너 기록 사례. Amazon 은 사실과 다르다며 이의 제기 권리를 유보",
      "as_of": "2024-01-23",
      "site_type": "물류창고",
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f53",
      "claim": "N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ P. 거버넌스·법규·사회의 60. 노동·수용성·접근성·J. 현장 운영·관제의 39. 운영 성과 측정·개선: 작업자 스캐너 기록의 개인별 비활동·속도 지표가 과도한 감시로 판단된 사례가 있으므로, ROP 가 로봇 작업과 연결해 개별 작업자의 처리량·위치를 기록할 때 39. 운영 성과 측정·개선의 지표를 집계 단위로 두고 보존 기간을 줄이는 설계가 필요할 것으로 보인다(oq-285).",
      "tag": "추정",
      "source_ids": [
        "ref-1370",
        "ref-589"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "CNIL 사례는 스캐너 기반이며 로봇 연동 지표에 적용된 판단은 확인하지 못함. 국내는 근로자참여법 제20조의 감시 설비 협의가 걸릴 수 있음",
      "as_of": "2026-10-09",
      "site_type": "물류창고",
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f54",
      "claim": "N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ P. 거버넌스·법규·사회의 60. 노동·수용성·접근성: 근로자참여 및 협력증진에 관한 법률 제20조는 사업장 내 근로자 감시 설비의 설치를 노사협의회 협의 사항으로 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-589"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "51 페이지 5절 시나리오 2 제약 칸(호 번호 미확인). 카메라 로봇이 감시 설비에 해당하는지는 oq-099 (재인용: 2026-09-25-64)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f55",
      "claim": "N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ Q. 현장 유형별 적용의 67. 기타 현장: Pudu 관리 API 결함 보도는 사무실에서 승강기 같은 설비를 조작하는 서비스 로봇(FlashBot)이 사무실 시스템을 망가뜨리거나 지식재산을 빼내는 데 쓰일 수 있다고 평가했는데, 이는 연구자·매체의 평가이며 확인된 사고는 아니다.",
      "tag": "추정",
      "source_ids": [
        "ref-1369",
        "ref-1368"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Hackmag·The Register 의 가능성 평가. 실제 악용·피해 보고는 없음",
      "as_of": "2025-09-05",
      "site_type": "기타",
      "flow_item": "예외·성과"
    },
    {
      "id": "f56",
      "claim": "N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ Q. 현장 유형별 적용의 63. 병원·의료: 진료실을 흉내 낸 모의 시나리오에서 의사·환자를 알아보도록 학습한 서비스 로봇은 대상이 아닌 사람의 얼굴을 안정적으로 가렸지만 자세 변화·가림·조명 변화가 인식 신뢰도를 낮췄다.",
      "tag": "사실",
      "source_ids": [
        "ref-1146"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "53 페이지 5절 병원 사례(HRI Companion '26, 원문 미열람, 검색 결과 요약 기준). 실제 병원 도입이 아님 (재인용: 2026-09-30-16)",
      "as_of": "2026-03-16",
      "site_type": "병원",
      "flow_item": "예외·성과",
      "source_unopened": true
    }
  ],
  "sources": [
    {
      "id": "ref-009",
      "org": "ROS 2 Design",
      "title": "ROS 2 DDS-Security Integration",
      "published": null,
      "url": "https://design.ros2.org/articles/ros2_dds_security.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. ROS 2 의 DDS 보안 규격 인증·접근 통제·암호화 플러그인 통합을 설명하는 설계 문서(이번 실행에서 다시 열지 않음).",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-010",
      "org": "ROS 2 Design",
      "title": "ROS 2 Robotic Systems Threat Model",
      "published": null,
      "url": "https://design.ros2.org/articles/ros2_threat_model.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 로봇 시스템 위협(신원 위조, 기본 자격증명 원격 접속, 공급망)과 완화책을 정리한 초안(이번 실행에서 다시 열지 않음).",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "VDA 5050 3.0.0 명세 원문. 보안 통신은 범위 밖·브로커 구성 몫으로 두고, updateCertificate 즉시 동작과 TLS 내려받기·인증서 체인 검증 권고를 정한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/VDA5050_EN.md",
      "source_unopened": false
    },
    {
      "id": "ref-405",
      "org": "Open Robotics",
      "title": "Security - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/security.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. Open-RMF 의 SROS 2 인클레이브와 웹 대시보드 TLS·OIDC·역할 기반 접근 통제를 설명(이번 실행에서 다시 열지 않음).",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-579",
      "org": "Open Robotics (ROS 2 Design)",
      "title": "ROS 2 Access Control Policies",
      "published": "2019-08",
      "url": "https://design.ros2.org/articles/ros2_access_control_policies.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 인클레이브별 토픽·서비스·액션 허용·거부 정책 형식을 정한 설계 문서.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-494",
      "org": "Francos, R. M., Garces, D., Akgün, O. E., Bastian, N. D., & Gil, S.(Harvard·JHU)",
      "title": "Trust-Aware Sequential Decision Making and Rollout Planning for Resilient Multi-Robot Systems",
      "published": "2026-08",
      "url": "https://arxiv.org/abs/2608.25690",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 위치 스푸핑 오염 에이전트를 신뢰 인지 모니터로 가려 다중 로봇 롤아웃 계획에서 빼는 방법(프리프린트).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-588",
      "org": "김·장 법률사무소",
      "title": "'이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서' 관련 인사이트",
      "published": null,
      "url": "https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=30477",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 개인정보위 이동형 영상정보처리기기 안내서의 촬영 표시·거부 수용·목적 외 이용·보관 요구를 해설한 법률사무소 뉴스레터.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-589",
      "org": "법제처 국가법령정보센터",
      "title": "근로자참여 및 협력증진에 관한 법률",
      "published": null,
      "url": "https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=105636",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 제20조에서 사업장 내 근로자 감시 설비 설치를 노사협의회 협의 사항으로 둔다.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-857",
      "org": "Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J.",
      "title": "Jailbreaking LLM-Controlled Robots",
      "published": "2024-11-09",
      "url": "https://arxiv.org/abs/2410.13691",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 언어 모델 제어 로봇 탈옥 알고리즘 RoboPAIR 와 높은 공격 성공률을 보고.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-700",
      "org": "Ravichandran, Z., Robey, A., Kumar, V., Pappas, G. J., & Hassani, H.(IEEE RA-L 2026 채택 표기)",
      "title": "Safety Guardrails for LLM-Enabled Robots",
      "published": "2025-03",
      "url": "https://arxiv.org/abs/2503.07885",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. RoboGuard 안전 가드레일로 탈옥 공격 시 위험 계획 실행을 줄였다고 보고.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-854",
      "org": "Open Source Robotics Alliance (OSRA) Interop SIG",
      "title": "Open Robotics Discourse, Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP)",
      "published": "2026-06-25",
      "url": "https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. Open-RMF REST API 를 MCP 도구로 노출해 자연어 지시를 RMF 임무로 바꾸는 Nayantra 발표 안내.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-863",
      "org": "European Commission — AI Act Service Desk",
      "title": "Article 12: Record-keeping (Regulation (EU) 2024/1689, Artificial Intelligence Act)",
      "published": "2024-06-13",
      "url": "https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 고위험 AI 시스템의 자동 사건 기록(로그) 요건 조문.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-969",
      "org": "바이라인네트워크",
      "title": "'로봇청소기' 다수 제품 보안 취약…대응방안은?",
      "published": "2025-10-31",
      "url": "https://byline.network/2025/10/31-283/",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. KISA·한국소비자원 로봇청소기 6종 보안 점검(40개 항목) 결과 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1076",
      "org": "Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv)",
      "title": "Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066",
      "published": "2026-02-19",
      "url": "https://arxiv.org/abs/2602.17822",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. ISO 10218 2011·2025 판을 비교해 기능안전·사이버보안 요구 확대를 정리.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1105",
      "org": "IEC (SyC Smart Energy)",
      "title": "IEC 62443",
      "published": null,
      "url": "https://syc-se.iec.ch/deliveries/cybersecurity-guidelines/security-standards-and-best-practices/iec-62443/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. IEC 62443 시리즈의 구역·도관, 보안 수준, 기본 요구를 소개하는 IEC 페이지.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1106",
      "org": "OWASP GenAI Security Project",
      "title": "LLM01:2025 Prompt Injection",
      "published": null,
      "url": "https://genai.owasp.org/llmrisk/llm01-prompt-injection/",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 직접·간접 프롬프트 주입 구분과 완화책.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1107",
      "org": "CISA (미국 사이버보안·기반시설보안청)",
      "title": "Aethon TUG Home Base Server (ICSA-22-102-05)",
      "published": "2022-04-12",
      "url": "https://www.cisa.gov/news-events/ics-advisories/icsa-22-102-05",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 병원 자율이동로봇 TUG 플릿 서버의 인가 누락·인증 없는 제어 채널 취약점 권고.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1109",
      "org": "IES (Integrated Equipment Services)",
      "title": "Machinery Regulation Guide",
      "published": "2026-08-27",
      "url": "https://www.ies.co.uk/reference-library/machinery-regulation-guide",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. EU 기계류 규정의 변조 보호·개입 증거 기록·로그 요구와 적용일을 해설.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1110",
      "org": "Fernández-Becerra, L., González-Santamarta, M. Á., Guerrero-Higueras, Á. M., Rodríguez-Lera, F. J., & Matellán Olivera, V. (arXiv)",
      "title": "Enhancing Trust in Autonomous Agents: An Architecture for Accountability and Explainability through Blockchain and Large Language Models",
      "published": "2024-03",
      "url": "https://arxiv.org/abs/2403.09567",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 블록체인 기록과 LLM 설명으로 자율 에이전트 책임 추적성을 높이는 구조.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1111",
      "org": "엠에스투데이",
      "title": "선박·위성·로봇까지 해킹 표적…정부, '피지컬 AI' 산업 보안 기준 제시",
      "published": "2026-03-06",
      "url": "https://www.mstoday.co.kr/news/articleView.html?idxno=100755",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 과기정통부·KISA 의 선박·우주·로봇 분야 보안 자료 공개 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1112",
      "org": "Nagaraja, N., Bagari, A., & Bahsi, H. (arXiv)",
      "title": "When Prompts Control Robots: Prompt Injection Attacks in Multi-Agent Robotic Systems",
      "published": "2026-08",
      "url": "https://arxiv.org/abs/2608.00747",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 다중 에이전트 로봇 시스템의 프롬프트 주입 공격 연구.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1113",
      "org": "Zhang, W., Kong, X., Dewitt, C., Braunl, T., & Hong, J. B. (arXiv)",
      "title": "A Study on Prompt Injection Attack Against LLM-Integrated Mobile Robotic Systems",
      "published": "2024-08",
      "url": "https://arxiv.org/abs/2408.03515",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. LLM 통합 이동로봇 시스템의 프롬프트 주입 공격 연구.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1114",
      "org": "Quarta, D., Pogliani, M., Polino, M., Maggi, F., Zanchettin, A. M., & Zanero, S. (IEEE S&P 2017)",
      "title": "An Experimental Security Analysis of an Industrial Robot Controller",
      "published": "2017",
      "url": "https://files01.core.ac.uk/download/pdf/84891817.pdf",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 산업용 로봇 제어기의 취약점이 제어 정확성·작업자 안전을 해칠 수 있음을 실험한 연구.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1116",
      "org": "IBF Solutions",
      "title": "New standards for industrial robots EN ISO 10218-1 and -2",
      "published": "2026-09-18",
      "url": "https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. ISO 10218-1/-2:2025 의 사이버보안 요구 추가와 EU 관보 등재를 해설.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1136",
      "org": "정보통신신문",
      "title": "\"자율주행차·로봇 카메라 촬영 시 외부에 표시해야\"",
      "published": "2024-10-14",
      "url": "https://www.koit.co.kr/news/articleView.html?idxno=125844",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 이동형 영상정보처리기기 안내서 공개(촬영 표시·거부 수용·위탁 시 보호책임자) 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1138",
      "org": "개인정보보호위원회 (대한민국 정책브리핑)",
      "title": "자율주행차·이동형 로봇 개발에 '영상데이터' 원본 활용 허용",
      "published": "2023-11-15",
      "url": "https://www.korea.kr/news/policyNewsView.do?newsId=148922669",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 자율주행차·이동형 로봇 개발에 영상 원본 활용을 허용하는 방향의 정부 발표.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1141",
      "org": "아시아경제",
      "title": "\"로봇청소기 개인정보 관리 대체로 안전…미흡 사례 ... (제목 일부만 확인)",
      "published": "2026-09-14",
      "url": "https://view.asiae.co.kr/article/2026091410054053414",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 2026-09-14 개인정보위 로봇청소기 5개 사업자 점검 결과 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1145",
      "org": "Xu, Y., & Ayday, E. (arXiv)",
      "title": "Seeing Less Is Not Seeing Safely: Privacy Leakage from Task-Scoped Robot Perception Exports",
      "published": "2026-09-02",
      "url": "https://arxiv.org/abs/2609.03055",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 과업 한정 로봇 인지 출력도 개인정보를 누출할 수 있음을 다룬 프리프린트.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1146",
      "org": "Sarfraz, B. M., Saplacan Lindblom, D., Baselizadeh, A., & Torresen, J. (HRI Companion '26)",
      "title": "The Privacy-Preserving Capabilities of a Service Robot in a Scenario-Based Healthcare Setting",
      "published": "2026-03-16",
      "url": "https://doi.org/10.1145/3776734.3794481",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 모의 진료실에서 서비스 로봇의 얼굴 가림 성능과 한계를 다룬 학회 부록 논문.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1173",
      "org": "ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan",
      "title": "REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction",
      "published": "2022-01-11",
      "url": "https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 사람 인지 규약 초안(영속 사람 ID 와 얼굴·몸·음성 ID 연결).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1299",
      "org": "ST Engineering Aethon (Newswire 게재 보도자료)",
      "title": "ST Engineering Aethon Launches Zena RX, Redefining Secure Delivery of Medications, Specimens and Sensitive Goods in Hospitals",
      "published": "2024-04-29",
      "url": "https://www.newswire.com/news/st-engineering-aethon-launches-zena-rx-redefining-secure-delivery-of-22310264",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 생체 인식·PIN 잠금 칸을 둔 병원 운반 로봇 출시 보도자료.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1301",
      "org": "경향신문 (곽희양)",
      "title": "내년 2월 자율주행 로봇이 아파트 내에서 배달 음식 나른다",
      "published": "2020-07-03",
      "url": "https://www.khan.co.kr/article/202007031130001",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 공동주택 배달 로봇 도입 계획(비밀번호로 적재함 열기) 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1242",
      "org": "Carr, C., Wang, S., Wang, P., & Han, L. (arXiv)",
      "title": "Attacking Digital Twins of Robotic Systems to Compromise Security and Safety",
      "published": "2022-11-17",
      "url": "https://arxiv.org/abs/2211.09507",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. ROS 기반 디지털 트윈에 대한 중간자 공격이 물리 로봇 실패로 이어질 수 있음을 보고.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1263",
      "org": "메트로신문",
      "title": "AI·커머스·플랫폼 분야 규제 특례 확대…사업화 지원",
      "published": "2026-05-06",
      "url": "https://www.metroseoul.co.kr/article/20260506500296",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 배달로봇 카메라 원본 영상 AI 학습 실증특례 승인(조건 포함) 보도.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1260",
      "org": "DIN Media",
      "title": "DIN EN ISO 13482 - 2024-10 (Draft standard) Robotik - Sicherheitsanforderungen für Serviceroboter (ISO/DIS 13482:2024)",
      "published": "2024-10",
      "url": "https://www.dinmedia.de/de/norm-entwurf/din-en-iso-13482/384079303",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. ISO 13482 개정 초안 소개(사이버보안·데이터 보호·승강기 협동 로봇 절 신설).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1228",
      "org": "European Commission (Shaping Europe's digital future)",
      "title": "CRA reporting",
      "published": null,
      "url": "https://digital-strategy.ec.europa.eu/en/policies/cra-reporting",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "EU 사이버복원력법 보고 의무 안내. 2026-09-11 부터 제조자의 적극 악용 취약점·중대 사고 보고, 24시간·72시간·14일(사고는 한 달) 시한, ENISA 단일 보고 플랫폼. 페이지 갱신일 2026-09-11.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://digital-strategy.ec.europa.eu/en/policies/cra-reporting",
      "source_unopened": false
    },
    {
      "id": "ref-1368",
      "org": "The Register",
      "title": "Researcher who found McDonald's free-food hack turns her attention to Chinese restaurant robots",
      "published": "2025-08-29",
      "url": "https://www.theregister.com/2025/08/29/pudu_robots_hackable/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "Pudu Robotics 로봇 관리 소프트웨어의 권한 검사 누락(유효 토큰만 확인), 주문 변경·로봇 이동·이름 변경 가능성, 신고 지연과 제조사의 수정·보안 대응 센터 개설을 보도.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.theregister.com/2025/08/29/pudu_robots_hackable/",
      "source_unopened": false
    },
    {
      "id": "ref-1369",
      "org": "Hackmag",
      "title": "Researcher finds a way to hack Chinese Pudu service robots",
      "published": "2025-09-05",
      "url": "https://hackmag.com/news/pudu-bugs",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "같은 Pudu 취약점 공개를 보도. BellaBot·FlashBot(승강기 같은 시스템 조작) 예시, 플릿 정지 가능성, 제조사 수정·보안 신고 주소 개설.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://hackmag.com/news/pudu-bugs",
      "source_unopened": false
    },
    {
      "id": "ref-1370",
      "org": "Silicon UK",
      "title": "France Fines Amazon 32m Euros Over 'Excessive' Worker Surveillance",
      "published": "2024-01-23",
      "url": "https://www.silicon.co.uk/e-marketing/ecommerce/cnil-france-amazon-fine-546858",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "CNIL 의 Amazon France Logistique 3,200만 유로 과징금 보도. 스캐너 기반 비활동(10분)·빠른 스캔(1.25초) 지표, 31일 보관을 과도하다고 판단, Amazon 의 반박과 조치.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.silicon.co.uk/e-marketing/ecommerce/cnil-france-amazon-fine-546858",
      "source_unopened": false
    },
    {
      "id": "ref-1371",
      "org": "CNIL (Commission nationale de l'informatique et des libertés)",
      "title": "Employee monitoring: CNIL fined AMAZON FRANCE LOGISTIQUE €32 million",
      "published": "2024-01-23",
      "url": "https://cnil.fr/en/employee-monitoring-cnil-fined-amazon-france-logistique-eu32-million",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. CNIL 공지(2023-12-27 결정, 2024-01-23 공표). 열었을 때 '더 이상 제공되지 않는 페이지'가 돌아와 검색 결과 요약(스캐너 기반 지표, 영상 감시 미흡 별도 위반)으로만 확인.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1372",
      "org": "바이라인네트워크 (곽중희)",
      "title": "개인정보위 \"로봇청소기 5개 브랜드, 특별한 침해 위험 없어\"",
      "published": "2026-09-14",
      "url": "https://byline.network/2026/09/14-623/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "개인정보위 로봇청소기 5개 브랜드 점검 보도. 지도 정보 저장 위치(기기·일부 서버), 접근통제·전송 암호화 미흡 사례, 접근권한 내역·접속기록 보관 기간 연장 조치.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://byline.network/2026/09/14-623/",
      "source_unopened": false
    },
    {
      "id": "ref-1373",
      "org": "바이라인네트워크",
      "title": "과기정통부, 선박·우주·로봇 보안 매뉴얼 공개",
      "published": "2026-03-06",
      "url": "https://byline.network/2026/03/6-340/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "과기정통부·KISA 의 로봇 보안모델 고도화판·로봇 보안요구사항 해설서 공개(2026-03-05 발표) 보도. 구체 요구 항목은 기사에 없음.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://byline.network/2026/03/6-340/",
      "source_unopened": false
    },
    {
      "id": "ref-1374",
      "org": "Shen, L., Geng, S., Zheng, Y., & Lu, C. X. (arXiv)",
      "title": "Seeing is Not Believing: Breaking the Physical-to-Digital Trust Boundary in Robotics",
      "published": "2026-09-08",
      "url": "https://arxiv.org/abs/2609.08280",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "ROS 2 환경 변수로 실행되는 발행 전 훅으로 텔레메트리·제어 신호를 위조하는 공격과 Docker 컨테이너 공급망 경로를 보인 프리프린트(Secure ROS 2 로봇팔 87% 성공).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2609.08280",
      "source_unopened": false
    },
    {
      "id": "ref-1375",
      "org": "KUKA (Robotics Tomorrow 게재 보도자료)",
      "title": "KUKA is First to Achieve Security Level 2 Certification for Robotics Industry",
      "published": "2026-09-02",
      "url": "https://www.roboticstomorrow.com/news/2026/09/02/kuka-is-first-to-achieve-security-level-2-certification-for-robotics-industry/27035/",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "KUKA 가 iiQKA.OS2·KR C5-2 의 IEC 62443-4-2 SL2 인증을 로봇 제조사 최초로 받았다고 주장하는 보도자료. 인증 기관 미기재.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.roboticstomorrow.com/news/2026/09/02/kuka-is-first-to-achieve-security-level-2-certification-for-robotics-industry/27035/",
      "source_unopened": false
    },
    {
      "id": "ref-1376",
      "org": "European Commission (Shaping Europe's digital future)",
      "title": "Data Act explained",
      "published": null,
      "url": "https://digital-strategy.ec.europa.eu/en/policies/data-act-explained",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "EU 데이터법 해설. 2025-09-12 적용, 연결 제품(로봇·산업 기계 포함) 사용자의 데이터 접근·공유 권리, 데이터 보유자의 계약·고지 의무, 영업비밀 예외.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://digital-strategy.ec.europa.eu/en/policies/data-act-explained",
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/security-and-privacy/index.md",
      "sections": [
        "5. 다른 대분류와의 연결"
      ],
      "rationale": "category_link: '다른 대분류와의 연결' 절만 patches 로 채운다. 대분류별 finding — A. 기획·사업: f1(1, 한국 보안모델), f2(3, 벤더 주장)·f3(3), f4(2) / B. 로봇 온톨로지: f5·f6(4·7, 인증서 교체, oq-113), f7(4, 개인정보 속성), f8(6, 명령 단위 권한) / C. 채팅 기반 구성·운영: f9(13), f10(12), f11(13·44), f12(12, 최소 권한), f13(12, 승인 감사 기록) — 분류 원문 C 주석 '사람이 확인·승인한 계획만 실행'과 함께 / D. 공간·지도 모델: f14(16, 가정 지도 저장 위치)·f15(15·16) — D 페이지가 '근거 없음'으로 둔 N 연결을 채움 / E. 사물·사람·실시간 상태: f16·f17(18, 텔레메트리 위조, oq-082), f18(17, 벤더 주장), f19(19) / F. 연동: f20·f21·f22(20, oq-100), f23·f24(21, oq-246), f25(22, oq-056) / G. 계획·최적화: f26·f27(25·27) / H. 실행·협업·예외 복구: f28(29), f29(32) / I. 설계·시뮬레이션: f30(34), f31(34·36) — 가정한 미래 실험 쪽이며 18. 실시간 세계 상태·데이터 일관성(f16·f17)과 구분 / J. 현장 운영·관제: f32·f33(37, oq-248·oq-249), f17(38), f34·f35·f36(40, oq-291) / K. 플랫폼 아키텍처·인프라: f37(41), f38(42), f39(43, oq-214) / L. AI·학습 기술: f40(45·47, 원본 영상), f41(47), f11(44) / M. 안전: f42·f43(50, oq-102·oq-254), f44·f45(48) / O. 검증·도입·수명주기: f48(54), f47(55), f46·f6·f35(57) / P. 거버넌스·법규·사회: f49·f50(58, oq-259), f35·f51(59), f52·f53·f54(60, oq-285·oq-099) / Q. 현장 유형별 적용: f52(61 물류창고, 로봇이 아닌 스캐너 사례임을 밝힘), f44(62 제조 공장), f21·f56(63 병원·의료), f20·f29·f34(64 상업 시설), f14·f39·f48(65 가정·공동주택), f40·f51(66 실외), f55(67 기타 현장). 벤더 주장 f2·f18 은 [추정]과 '벤더 주장' 병기. 로봇 제어기·펌웨어 보안, 승강기 제어, 카메라 기기 쪽 처리는 '연계 대상'으로 짧게. 아직 다루지 않은 연결: 23. 업무 시스템 연동, 24. 작업·워크플로 모델링, 26. 작업 순서·스케줄링, 28. 공용 자원·충전·에너지 최적화, 30. 로봇 간 협업·물리적 인계, 33. 시나리오 모델·편집, 35. 처리능력·규모·배치 설계, 46. 예측·학습 기반 최적화, 49. 사람 근접 안전, 56. 운영 이관·확대·교육, 5. 로봇 능력·작업 표현, 8~11. 채팅 영역. 다음 실행 후보: 51. 인증·권한·격리(이전 분류 기준) 10절에 f5·f20·f22·f37 반영, 52. 통신 보호·위협 관리·감사 7절에 f35(사이버복원력법 보고 의무) 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "적극 악용 취약점",
      "term_en": "Actively Exploited Vulnerability (EU Cyber Resilience Act)",
      "definition": "악의적 악용의 믿을 만한 증거가 있는 취약점으로, EU 사이버복원력법이 2026-09-11 부터 제조자에게 24시간 조기 경보·72시간 통지·최종 보고를 요구하는 대상이다."
    },
    {
      "term_ko": "연결 제품",
      "term_en": "Connected Product (EU Data Act)",
      "definition": "사용·성능·환경 데이터를 만들고 전송할 수 있는 제품으로, EU 데이터법이 사용자에게 그 데이터의 접근·공유 권리를 주는 대상이며 집행위원회 해설은 로봇과 산업 기계를 예로 든다."
    },
    {
      "term_ko": "원격 증명",
      "term_en": "Remote Attestation",
      "definition": "원격 검증자가 기기가 보고하는 상태·측정값을 근거로 그 기기가 정상적으로 동작하고 있음을 확인하는 절차로, 보고 데이터가 발행 전에 위조되면 무력화될 수 있다."
    }
  ],
  "open_questions_new": [
    "ROP 가 제조사 플릿 관리 서버·관리 API 를 연동하기 전에 인증 뒤 권한 검사 같은 인가 결함을 확인하는 최소 보안 시험 항목을 정한 공개 기준이나 사례가 있는가? | 관련 영역: 51. 인증·권한·격리, 20. 로봇·제조사 관제 연동, 54. 시험·형식 검증·벤치마크 | 근거: f22 | 종류: 일반",
    "로봇이 발행 전 단계에서 위조한 텔레메트리를 설비 센서·다른 로봇 관측과 교차 확인해 플릿 수준에서 탐지하는 방법의 효과를 측정한 연구가 있는가? | 관련 영역: 52. 통신 보호·위협 관리·감사, 18. 실시간 세계 상태·데이터 일관성, 38. 모니터링·이상 탐지·원인 분석 | 근거: f17 | 종류: 일반",
    "EU 데이터법에서 여러 제조사 로봇의 데이터를 모아 관제하는 오케스트레이션 플랫폼 사업자는 사용자·제3자·데이터 보유자 가운데 어느 지위이며, 제조사에 로봇 데이터 제공을 요구할 수 있는가? | 관련 영역: 58. 다사업자 책임·계약·데이터, 53. 개인정보·영상 데이터 | 근거: f50 | 종류: 일반",
    "작업자 스캐너 기록의 개인별 비활동·속도 지표를 과도한 감시로 본 CNIL 판단이 로봇 작업 기록에서 만든 작업자 지표에 적용된 감독기관 결정이나 국내 해석이 있는가? | 관련 영역: 53. 개인정보·영상 데이터, 60. 노동·수용성·접근성, 39. 운영 성과 측정·개선 | 근거: f53 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 45,
    "cross_checked_count": 2,
    "unverified": [
      "f20·f29·f34·f55 Pudu 사례는 연구자 블로그 공개를 옮긴 기사 두 건 기준이며 연구자 원문과 제조사 공식 공지는 열지 못함(교차 확인 아님)",
      "ref-1371 CNIL 공지는 페이지가 '더 이상 제공되지 않음'으로 열려 검색 결과 요약 범위로만 사용",
      "f39 접근권한 내역·접속기록 보관 기간 연장의 적용 대상과 근거 조항은 기사에 없어 미확인(oq-214)",
      "f2 KUKA IEC 62443-4-2 SL2 인증은 벤더 주장, 인증 기관·인증서 미확인",
      "MiR Fleet Enterprise 의 IEC 62443-4-2 정렬 주장은 PDF 본문을 추출하지 못해 쓰지 않음",
      "ISO 10218-1:2025 사이버보안 조항 번호는 여전히 미확인(oq-102)",
      "KISA 로봇 보안모델 고도화판·해설서의 요구 항목은 원문을 열지 못해 미확인(oq-250)",
      "EU 사이버복원력법 규정 원문(제14조)은 열지 않고 집행위원회 안내 페이지만 확인",
      "재사용 출처 35건은 이번 실행에서 다시 열지 않음"
    ],
    "scope_violations": [
      "f2·f3·f44: 로봇 제어기 보안 인증·제어기 취약점은 원문 19장 '로봇 자체 지능·제어' 경계의 제조사 몫이라 ROP 는 조달 요구·연결 대상 위협 근거로만 서술",
      "f21·f25: 병원 플릿 서버의 방화벽·VPN, 승강기 조작은 시설·설비 제어 경계의 연계 대상이며 ROP 는 연결 계정 권한과 설비 명령 권한 분리로만 서술",
      "f14·f18·f56: 로봇청소기 앱 인증·기기 저장, 잠금 칸 생체 인증, 기기 쪽 얼굴 가림은 제조사 기능이라 연계 대상이며 ROP 는 결과·상태 기록 쪽만 서술",
      "f35·f49·f51·f52·f54: 법령 해석과 적용 판단은 운영 사업자·법무 몫이며 ROP 는 기록·통보·데이터 흐름 규칙 제공 범위로만 연결",
      "f52: CNIL 사례는 로봇이 아닌 작업자 스캐너 기록이라 claim 에 그 사실을 밝힘"
    ],
    "budget_used": {
      "queries": 13,
      "sources": 10
    },
    "limits": "web_fetch_available: true · fetch_mode full. 대분류 연결(category_link) 실행이다. 근거는 먼저 게시된 51·52·53 페이지와 A·B·D·E·F·G 대분류 페이지, 이전 브리프(2026-10-09-08, 2026-10-09-09)의 검증된 주장에서 찾고 재사용 출처 id 를 썼다(재사용 35건 가운데 이번에 다시 연 것은 ref-031(github_raw) 1건이고 나머지 34건은 fetched false·source_unopened true). 신규 출처는 10건(ref-1228~ref-1376, 예약 구간 안)이며 ref-1371(CNIL 공지)을 뺀 9건은 원문을 열었다. 검색 13회/30, 신규 출처 10건/15. 교차 확인 2건(f42 ISO 10218 사이버보안, f52 CNIL Amazon 과징금). 벤더 주장 2건(f2·f18). 같은 정부 발표를 옮긴 기사 쌍(f1, f51)과 같은 연구자 공개를 옮긴 기사 쌍(f20 등)은 독립 출처로 보지 않아 교차 확인으로 세지 않았다. 한국 자료: 신규 ref-1372·ref-1373, 재사용 ref-589·ref-588·ref-969·ref-1111·ref-1136·ref-1138·ref-1141·ref-1301·ref-1263. 현장 유형: 물류창고(f52·f53, 로봇이 아닌 스캐너 사례)·제조 공장(f44)·병원(f18·f21·f56)·상업 시설(f20·f29·f34)·가정(f14·f39·f48)·실외(f40·f51)·기타(f55) 각 1건 이상. 18. 실시간 세계 상태·데이터 일관성(현재 상태, f16·f17)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래, f30·f31)을 구분했다. 분류 원문 교차 규칙에 해당하는 L. AI·학습 기술 연결(f11·f40·f41)은 적용 대상 영역과 함께 제안했다. 열린 질문 oq-056·oq-082·oq-099·oq-100·oq-102·oq-113·oq-214·oq-246·oq-248·oq-249·oq-250·oq-259·oq-285·oq-291 에는 부분 근거만 더했고 해결 제안은 없다. 대분류 페이지 절 번호는 이전 대분류 연결 실행과 같이 제목 순서(핵심 질문·개요·세부 연구영역·핵심 포인트·다른 대분류와의 연결)에 따라 '5'로 매겼다 [가정]. 아직 근거를 찾지 못한 연결은 page_proposals 의 rationale 에 적었다. 정정 요청 없음. 우선 지정 질문 없음. 입력 누락 없음."
  }
}
```

### runs/2026-10-09-10/verification.json

```json
{
  "run_id": "2026-10-09-10",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1373 검증 중 재열람: 2026-03-06 기사, 3-05 발표, 로봇 보안모델 고도화 버전·로봇 보안요구사항 해설서, 유럽·북미 규제 강화 반영·개발·수출 보안 요구 파악 목적 확인. ref-1111(원문 미열람)은 같은 발표를 옮긴 기사라 교차 확인 아님. 요구 항목은 미확인(oq-250)."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1375 재열람: 2026-09-02 보도자료, iiQKA.OS2·KR C5-2, IEC 62443-4-2 SL2, 'first robotics manufacturer' 문구, 인증 기관·EU 규정 언급 없음 확인. [추정]·벤더 주장 유지. 제어기 보안 인증은 로봇 자체 지능·제어 경계의 연계 대상."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 추정 문장. ref-1105 원문 미열람(52 페이지 7절 재인용), ref-1375 벤더 주장. 플릿 관리 소프트웨어 인증 사례 미확인을 함께 서술해야 한다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 게시된 52 페이지 9절의 [추정] 책임 경계를 재인용한 추정. ref-1114·ref-1107 원문 미열람, ref-009 는 source_texts 원문 있음."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-031 raw 재열람: 6.2.3.1 updateCertificate '새 인증서 묶음 내려받기·활성화', keyDownloadLink·certificateDownloadLink 필수, certificateAuthorityDownloadLink 선택, 6.2.3.3 TLS 보호 필수·체인 검증 권고 확인. 브리프의 '인증 기관·인증서·키 링크를 선택 매개변수'는 부정확(키·인증서 링크는 필수) — 본문에 매개변수 필수 여부를 쓰려면 바로잡는다. 발행일 미확인, 3.0.0 판."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ref-031 updateCertificate 에 기댄 추정. 등록 항목·판 관리 구현 사례 미확인, oq-113 연결."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 게시된 53 페이지 9절 [추정] 재인용. ref-1145·ref-588 원문 미열람."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-579 source_texts 원문 확인: 인클레이브(프로파일)별 topics·services·actions 의 ALLOW/DENY. 능력 모델–권한 정책 연결은 추정, 공개 사례 미확인."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 게시된 52 페이지 7절 [사실] 재인용(ref-1106 이번 실행 원문 미열람)."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 참고문헌 목록의 제목·발행 연월과 일치(ref-1112, ref-1113 이번 실행 원문 미열람). 연구 존재만 진술하고 수치 없음."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: C·L 대분류 페이지의 검증된 주장과 같음. 두 수치 모두 저자 보고값. RoboGuard 92%→3% 미만은 arXiv v2(2026-03-03) 기준이고 v1 수치는 달라 as_of '2025-03' 은 맞지 않음. ref-857 과 ref-1337, ref-700 과 ref-1338 은 같은 URL 이라 퍼블리셔가 합칠 대상."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: L 대분류 연결 f69 와 같은 추정. ref-854 안내문에는 권한 제한 구성이 없음(C 페이지 확인 범위)."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 추정. ref-1110 은 대화 승인 기록 적용 사례가 아님, oq-248 연결."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1372 재열람: 2026-09-14, 5개 브랜드(2025-03 기준 최신 모델), 지도 정보 기기 저장·스마트폰 미보관·일부 서버 저장, 일부 사업자 접근통제·전송 암호화 미흡, '특별한 개인정보 침해 위험은 확인되지 않았다' 확인. 기사 1건 기준. 가정 / 작업 대상. 앱·기기 보안은 제조사 연계 대상."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 추정. downloadMap 링크는 D 대분류 페이지 검증 주장과 같음. 업무 시설 지도 접근 통제 기관 자료 미확인."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1374 재열람: 2026-09-08 제출, 환경 변수 하나로 사전 빌드 훅이 발행 전 텔레메트리·제어 신호 가로채기·주입, Secure ROS 2 Franka 팔, 약 3 ms 지터, AI 기반 탐지기 포함 87% 성공, ROS 2 개발진에 보고 확인. 프리프린트·저자 보고값·독립 재현 미확인을 병기해야 한다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지. 다만 '위치 스푸핑이 배정을 무너뜨린다'는 ref-494 의 진술(롤아웃 기반 배정·경로 계획의 비용 개선을 없앨 수 있음, GPS 스푸핑·택시 수요 실험)보다 강한 표현이라 문구를 고친다. ref-494 원문 미열람. 현재 상태 표현(18번) 쪽 연결."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: E 대분류 페이지 검증 주장 재인용. Zena RX 는 벤더 주장(ref-1299), 공동주택은 2020-07 계획 단계 기사(ref-1301). 두 출처 원문 미열람. [추정]·벤더 주장 유지, 잠금 칸·생체 인증은 제조사 기능의 연계 대상."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: E 대분류 페이지 검증 주장 재인용(ref-1173 이번 실행 원문 미열람). Draft 상태 규약 제안임을 밝힌다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1368·ref-1369 재열람: 인증 토큰 확인 뒤 권한 검사 없음, XSS·체험 계정으로 토큰 획득, 주문 리셋·변경, 로봇 이동, 이름 변경 확인. 두 기사 모두 같은 연구자 공개를 옮긴 것이라 교차 확인 아님, 실제 악용 보도 없음. 상업 시설 / 예외·성과."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 게시된 52 페이지 5절 [사실] 재인용(ref-1107 이번 실행 원문 미열람). 방화벽·VPN 같은 망 조치는 시설 IT/OT 연계 대상."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 두 사례에 기댄 추정. 연동 승인 기준의 공개 기준 미확인, oq-100 연결."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-031 source_texts 원문 확인: 2장 범위의 'Cybersecurity Measures … are not specified', 4.1절 'Protocol security needs to be taken into account by broker configuration, but is not addressed within this guideline.' 발행일 미확인, 3.0.0 판."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 추정. 최소 보안 프로파일 미확인(oq-246). ref-1105 원문 미열람."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1369 재열람: FlashBot 이 승강기 같은 시스템을 조작한다는 보도 확인. ref-405 source_texts 원문: 같은 신원·접근 규칙을 공유하는 SROS 2 인클레이브 확인. 승강기 제어는 시설·설비 제어 경계의 연계 대상. oq-056 연결."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: G 대분류 페이지 검증 주장 재인용(ref-494 프리프린트, 원문 미열람). GPS 스푸핑·택시 수요 실험, 물류센터 적용 미확인."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ref-1368 의 주문 변경·로봇 이동 보도에 기댄 추정. 계획 쪽 감지 규칙 자료 미확인."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-031 raw 재열람: 6.2.3.2 RUNNING 'Mobile robot is downloading and installing certificates', FAILED 'Download or installation failed.' 확인. f5 와 같은 출처의 직접 인용이 겹치므로 페이지에서는 재서술한다."
    },
    {
      "finding_id": "f29",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 추정. 플릿 전체 정지 가능성은 연구자·매체의 평가이며 실제 사고 보도 없음(ref-1368·ref-1369 재열람으로 확인)."
    },
    {
      "finding_id": "f30",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: M 대분류 연결 f56 과 같은 검증 주장(ref-1242 이번 실행 원문 미열람). 가정한 미래를 실험하는 34번 쪽."
    },
    {
      "finding_id": "f31",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 추정. 18번(현재 상태)과 34·36번(가정한 미래·재현)의 구분이 원문 주석과 맞음. ref-1242·ref-588 원문 미열람."
    },
    {
      "finding_id": "f32",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 게시된 52 페이지 재인용(ref-1110 이번 실행 원문 미열람). 규모별 비용은 oq-248."
    },
    {
      "finding_id": "f33",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 52 페이지 7절의 업계 해설 기준 [사실] 재인용(ref-1109 원문 미열람, 규정 원문 ref-555 미열람). '업계 해설에 따르면' 한정과 oq-249 를 유지해야 한다."
    },
    {
      "finding_id": "f34",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1368 재열람: 2025-08-12 연락 시작, 무응답, Skylark Holdings·Zensho 통보 뒤 응답, 신고 창구 부재가 대응을 늦췄다는 제조사 인정, 보안 대응 센터·신고 주소 개설, 1만 달러 포상 확인. ref-1369 는 제조사가 '다른 경로로 보고를 받았다'고 설명했다고 전함 — 두 설명을 함께 적는다. 같은 공개를 옮긴 기사 쌍이라 교차 확인 아님."
    },
    {
      "finding_id": "f35",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1228 재열람: 2026-09-11 시행, 제조자의 적극 악용 취약점·중대 사고 보고, 24시간 조기 경보·72시간 통지·취약점 최종 보고는 시정 조치 뒤 14일·중대 사고는 72시간 통지 뒤 한 달, 오픈소스 관리자 2027-12-11, 페이지 갱신 2026-09-11 확인. 다만 통지는 ENISA 단일 보고 플랫폼을 '거쳐' 주 사업장 CSIRT 로 가므로 'ENISA 로 알려야'는 바로잡는다. 규정 원문 미열람, 집행위원회 안내 페이지 기준."
    },
    {
      "finding_id": "f36",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 추정. 보고 의무는 제조자에 걸림, 플랫폼 사업자 해당 여부는 oq-291."
    },
    {
      "finding_id": "f37",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-405 source_texts 원문 확인: 대시보드 TLS, OIDC(Keycloak) 역할을 담은 서명 id 토큰을 API 서버가 보고 역할에 맞는 보안 ROS 2 노드 접근 허용, ROS 2 쪽 SROS 2 인클레이브."
    },
    {
      "finding_id": "f38",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-009 source_texts 원문: 인증·접근 통제·암호 플러그인 사용 확인. ref-010 위협 진술은 게시된 51 페이지 3절 검증 주장과 같음(source_texts 는 발췌본). 두 출처는 서로 다른 내용이라 교차 확인 아님."
    },
    {
      "finding_id": "f39",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1372 재열람: 접근권한 부여 내역 200일→3년, 접속기록 90일→2년 이상 확인. 적용 대상(점검 사업자 한정인지)과 근거 조항은 기사에 없어 본문에 미확인으로 남겨야 한다(oq-214)."
    },
    {
      "finding_id": "f40",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 53 페이지·L 대분류 연결의 검증 주장 재인용. 두 출처는 서로 다른 시점의 조치. ref-1138·ref-1263 이번 실행 원문 미열람."
    },
    {
      "finding_id": "f41",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: C·L 대분류 페이지 검증 주장 재인용(ref-863 이번 실행 원문 미열람). 고위험 해당 여부는 oq-106·oq-143."
    },
    {
      "finding_id": "f42",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인: M 대분류 연결 f54 에서 두 출처(업계 해설·비교 논문) 교차 확인된 주장. 조항 번호 미확인(oq-102). 두 출처 이번 실행 원문 미열람."
    },
    {
      "finding_id": "f43",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: M 대분류 연결 f23 재인용(ref-1260 원문 미열람). 초안 기준, 최종판 반영 미확인(oq-254)."
    },
    {
      "finding_id": "f44",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 52 페이지 5절에서 검색 요약 기준 [추정]으로 실린 내용(ref-1114 원문 미열람). 제어기 보안은 로봇 제조사 쪽 연계 대상. 제조 공장 / 예외·성과."
    },
    {
      "finding_id": "f45",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: M 대분류 연결 f57 과 같은 추정. 로봇 자체 안전 기능은 연계 대상."
    },
    {
      "finding_id": "f46",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ref-010 의 서드파티 구성요소·배포 위협(source_texts 발췌와 51 페이지 3절), ref-1374 재열람에서 제3자 Docker 컨테이너·보조 도구 경로 확인. 같은 방향의 다른 내용이라 교차 확인 아님."
    },
    {
      "finding_id": "f47",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 51 페이지 3절의 ref-010 진술(기본 자격증명 SSH 원격 접속)에 기댄 추정. 시운전 점검표 적용 사례 미확인."
    },
    {
      "finding_id": "f48",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 52 페이지 5절 가정 사례(2025-10-31 기사, ref-969 원문 미열람)에 기댄 추정. 다중 로봇 관제 플랫폼 적용 사례 없음."
    },
    {
      "finding_id": "f49",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1376 재열람: 2025-09-12 적용, 연결 제품 예로 robots·industrial machines, 사용자 접근·제3자 공유, 데이터 보유자의 계약·데이터 종류·양·수집 빈도 고지, 영업비밀 거부는 심각한 경제적 피해 가능성이 높을 때만·당국 통지 확인. '(보통 제조사)'는 이번 열람에서 확인하지 못함. 페이지 최종 갱신 2025-12-15."
    },
    {
      "finding_id": "f50",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 추정. 플랫폼 사업자 지위 해석 미확인, oq-259 연결. 법 적용 판단은 운영자·법무 연계 대상."
    },
    {
      "finding_id": "f51",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 53 페이지 5절 실외 사례 재인용. 두 출처가 같은 안내서 발표를 옮긴 것이라 교차 확인 아님. ref-1136·ref-588 원문 미열람."
    },
    {
      "finding_id": "f52",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "ref-1370 재열람: 3,200만 유로, 10분 비활동 경보, 1.25초 미만 스캔 경보, 31일 보관 과도, Amazon 의 '사실과 다름'·이의 제기 유보 확인. ref-1371 CNIL 공지는 검색 결과로 기관·제목·URL 일치 확인(본문은 '더 이상 제공되지 않음'), 2023-12-27 결정·2024-01-23 공표는 다수 법률 해설 검색 결과와 일치. 로봇이 아니라 작업자 휴대 스캐너 사례."
    },
    {
      "finding_id": "f53",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 추정. CNIL 판단의 로봇 연동 지표 적용 사례 미확인(oq-285). 근로자참여법 제20조 협의는 f54 근거."
    },
    {
      "finding_id": "f54",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 51 페이지 5절 [사실] 재인용(ref-589 원문 미열람, 호 번호 미확인). 카메라 로봇의 감시 설비 해당 여부는 oq-099."
    },
    {
      "finding_id": "f55",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-1369·ref-1368 재열람: FlashBot 이 사무실 시스템 피해·지식재산 탈취에 쓰일 수 있다는 연구자·매체 평가 확인. 실제 피해 보고 없음. 기타 현장(사무실)."
    },
    {
      "finding_id": "f56",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 53 페이지 5절 병원 사례 재인용(ref-1146 원문 미열람, 검색 요약 기준). 모의 진료실 실험이며 실제 병원 도입 아님. 기기 쪽 얼굴 가림은 제조사 연계 대상."
    }
  ],
  "category_fit": {
    "ok": true,
    "reassign_to": null
  },
  "scope_boundary": {
    "ok": true,
    "issues": [
      "f2·f3·f44: 로봇 제어기·운영체제 보안 인증과 제어기 취약점은 원문 19장 '로봇 자체 지능·제어' 경계의 제조사 몫 — 본문에서 '연계 대상'으로 짧게 두고 ROP 는 조달 요구·연결 대상 위협 근거로만 쓴다(편집으로 해결)",
      "f21·f25·f55: 병원 플릿 서버의 방화벽·VPN, 승강기 조작은 '시설·설비 제어' 경계의 연계 대상 — ROP 몫은 연결 계정 권한·설비 명령 권한 분리로 한정(편집으로 해결)",
      "f14·f18·f56: 앱 인증·기기 저장, 잠금 칸 생체 인증, 기기 쪽 얼굴 가림은 제조사 기능의 연계 대상(편집으로 해결)",
      "f35·f39·f49·f50·f51·f52·f53·f54: 법령 해석·적용 판단은 운영 사업자·법무 몫 — ROP 는 기록·통보·데이터 흐름 규칙 제공 범위로만 연결(편집으로 해결)"
    ]
  },
  "duplication": {
    "ok": true,
    "overlaps": [
      "f42·f45·f30 은 M. 안전 대분류 연결(2026-10-09-09 실행 f54·f57·f56)과 같은 주장 — 같은 각주(ref-1116·ref-1076·ref-1260·ref-1242)와 태그를 재사용한다",
      "f11·f12·f41 은 L. AI·학습 기술(2026-10-09-08 실행 f63·f64·f69·f53)·C. 채팅 기반 구성·운영 페이지와 같은 주장 — ref-857 과 ref-1337, ref-700 과 ref-1338 은 같은 arXiv URL 이므로 이 페이지는 브리프대로 ref-857·ref-700 을 쓰고 퍼블리셔가 합친다",
      "f18·f19·f26 은 E. 사물·사람·실시간 상태·G. 계획·최적화 페이지 연결 절의 검증 주장 재인용 — 같은 각주를 쓴다",
      "f14·f15 는 D. 공간·지도 모델 페이지가 '근거 없음'으로 둔 N. 보안·개인정보 연결을 채우는 것으로 모순이 아니다(D 페이지 쪽 갱신은 별도 실행)",
      "새 열린 질문 '위조 텔레메트리 교차 확인' 은 oq-082 와, 'CNIL 판단의 로봇 작업 지표 적용' 은 oq-285 와, '데이터법상 플랫폼 지위' 는 oq-259 와 인접하나 묻는 대상이 달라 중복으로 보지 않는다"
    ]
  },
  "terminology": {
    "ok": true,
    "conflicts": []
  },
  "quotation_check": {
    "ok": false,
    "issues": [
      "ref-031 에서 f5(6.2.3.3절 TLS 문장)와 f28(6.2.3.2절 RUNNING·FAILED 설명)의 직접 인용이 두 번 계획돼 출처당 1회 규칙을 넘는다 — 페이지에서는 많아야 한 구절만 인용하고 나머지는 재서술한다"
    ]
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "page_proposals 의 절 이름 '5. 다른 대분류와의 연결' 은 대분류 정본 절 제목과 다르다 — patches 의 section 을 번호 없는 '다른 대분류와의 연결'로 쓰고, 그 절 외에는 아래 각주 정의 추가만 '참고 자료' 절에 append 한다.",
    "각주 정의: 이번에 새로 인용하는 출처마다 '참고 자료' 절 끝에 '[^ref-NNN]: 기관, 제목, 발행일, URL, 접근일 2026-10-09' 정의를 더한다 — 기존 ref-009·ref-010 정의는 유지한다.",
    "원문 미열람 표기: ref-494·ref-588·ref-589·ref-857·ref-700·ref-854·ref-863·ref-969·ref-1076·ref-1105·ref-1106·ref-1107·ref-1109·ref-1110·ref-1111·ref-1112·ref-1113·ref-1114·ref-1116·ref-1136·ref-1138·ref-1141·ref-1145·ref-1146·ref-1173·ref-1299·ref-1301·ref-1242·ref-1263·ref-1371·ref-1260 의 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣는다 — 이번 실행에서 본문을 읽지 않았다.",
    "ref-009·ref-010·ref-031·ref-405·ref-579 는 입력의 data/source_texts 원문이 있으므로 각주에 '(원문 미열람)'을 붙이지 않는다 — 브리프 summary 의 '원문 미열람' 문구는 source_texts 원문 존재와 맞지 않는다.",
    "ref-1228 각주의 발행일 자리에 '미확인(페이지 최종 갱신 2026-09-11)', ref-1376 은 '미확인(페이지 최종 갱신 2025-12-15)'을 쓴다 — 검증 열람에서 갱신일을 확인했다.",
    "f2: [추정] 뒤에 '벤더 주장'을 병기하고 '로봇 제조사 최초'와 인증 사실 모두 KUKA 보도자료의 주장이며 인증 기관이 적혀 있지 않음을 밝힌다 — 독립 확인이 없다.",
    "f18: [추정]과 '벤더 주장'을 유지하고, 공동주택 비밀번호 방식은 2020-07 계획 단계 보도임을 밝힌다 — Zena RX 는 제조사 보도자료뿐이다.",
    "f2·f3·f44 는 로봇 제어기 보안을 '연계 대상'(원문 19장 로봇 자체 지능·제어 경계)으로 짧게 쓰고, f21·f25·f55 의 방화벽·VPN·승강기 조작은 '연계 대상'(시설·설비 제어 경계)으로, f14·f18·f56 의 앱·기기 쪽 보안·가림·잠금 칸 인증은 제조사 기능의 연계 대상으로 쓴다 — ROP 직접 범위처럼 서술하지 않는다.",
    "f35·f39·f49·f50·f51·f52·f53·f54: 법 적용 여부 판단은 운영 사업자·법무가 맡는 연계 대상임을 한 번 밝히고, ROP 몫은 기록·통보·데이터 흐름 규칙으로 한정한다.",
    "f5: updateCertificate 매개변수를 쓰려면 키·인증서 내려받기 링크는 필수, 인증 기관 링크만 선택임을 맞게 쓴다 — 브리프 발췌의 '선택 매개변수' 표현은 원문과 다르다.",
    "f5·f28: ref-031 직접 인용은 많아야 한 구절로 하고 나머지는 재서술한다 — 출처당 직접 인용 1회 규칙.",
    "f11: RoboGuard 수치(92% 초과 → 3% 미만)의 기준일을 arXiv v2 개정판(2026-03-03)으로 적고, v1 은 다른 수치를 보고했다는 점과 두 수치(RoboPAIR·RoboGuard) 모두 저자 보고값·독립 재현 미확인임을 병기한다 — C 대분류 페이지의 서술과 맞춘다.",
    "f16: 프리프린트이며 87%·약 3 ms 지터가 저자 보고값이고 독립 재현은 확인되지 않았음을 병기한다.",
    "f17: '위치 스푸핑이 배정을 무너뜨린다'를 '위치 스푸핑으로 오염된 에이전트가 롤아웃 기반 배정·경로 계획의 비용 개선을 없앨 수 있다(GPS 스푸핑·택시 수요 실험, 물류센터 적용 미확인)'로 고친다 — ref-494 의 진술 범위를 넘는다.",
    "f35: '…ENISA 단일 보고 플랫폼으로 알려야' 를 '…ENISA 단일 보고 플랫폼을 통해 주 사업장 국가의 CSIRT 에 알려야' 로 고치고, 집행위원회 안내 페이지 기준(규정 원문 미열람)임을 밝힌다.",
    "f49: '(보통 제조사)'를 삭제한다 — 검증 열람에서 확인되지 않았다.",
    "f39: 보관 기간 연장 조치의 적용 대상(점검 사업자 한정 여부)과 근거 조항은 기사에 없어 미확인임을 같은 문장 또는 바로 뒤에 밝힌다(oq-214).",
    "f20·f29·f34·f55: Pudu 사례 근거 두 기사는 같은 연구자 공개를 옮긴 것으로 교차 확인이 아니라는 점, 실제 악용·피해 보도가 없다는 점, f29·f55 의 플릿 정지·사무실 시스템 피해는 연구자·매체의 가능성 평가라는 점을 밝힌다.",
    "f34: 신고 지연에 대해 The Register 는 제조사가 신고 창구 부재를 인정했다고, Hackmag 은 제조사가 다른 경로로 보고를 받았다고 설명했다고 전하므로 한쪽을 고르지 말고 두 설명을 함께 적는다.",
    "f33: '업계 해설에 따르면'과 규정 원문 미열람, 오케스트레이션 플랫폼 적용 여부가 열린 질문 oq-249 임을 유지한다.",
    "f1: 같은 정부 발표를 옮긴 기사 기준이며 로봇 보안모델·해설서의 구체 요구 항목은 미확인(oq-250)임을 밝힌다.",
    "f52: 로봇이 아니라 물류창고 작업자 휴대 스캐너 기록 사례이며 Amazon 이 사실과 다르다며 이의 제기 권리를 유보했다는 점을 본문에 밝히고, site_matrix_updates 에 이 사례를 물류창고 × N. 보안·개인정보 칸의 로봇 적용 사례로 넣지 않는다 — ROP 적용 사례가 아니다.",
    "f30·f31 은 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현 쪽, f16·f17 은 현재 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성 쪽으로 나눠 쓴다 — 분류 원문 10장 주석의 구분.",
    "L. AI·학습 기술 연결(f11·f40·f41)은 적용 대상 영역(13. 대화형 기능의 신뢰·기반, 45. 문서·도면·장면 이해, 47. AI·학습·적응과 모델 운영)과 함께 쓴다 — 교차 규칙.",
    "열린 질문 등록: '위조 텔레메트리 교차 확인 효과' 질문 문장 끝에 '(관련: oq-082)', 'CNIL 판단의 로봇 작업 지표 적용' 질문에 '(관련: oq-285)', '데이터법상 플랫폼 지위' 질문에 '(관련: oq-259)'를 붙여 기존 질문과의 관계를 밝힌다.",
    "절 끝에 브리프 rationale 의 '아직 다루지 않은 연결'(23·24·26·28·30·33·35·46·49·56·5번과 8~11번 채팅 영역)을 번호와 이름을 함께 써서 목록으로 남긴다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 56건, 미확인 0건, 교차 확인 2건(f42 ISO 10218 2025년판 사이버보안 요구, f52 CNIL 의 Amazon France Logistique 과징금). 강등: 없음. 다만 f17·f35·f49·f5 의 문구는 출처 범위에 맞게 고친다. 검증에서 새 출처 9건과 ref-031 VDA 5050 원문을 다시 열어 확인했다. 원문 미열람 출처: ref-494, ref-588, ref-589, ref-857, ref-700, ref-854, ref-863, ref-969, ref-1076, ref-1105, ref-1106, ref-1107, ref-1109, ref-1110, ref-1111, ref-1112, ref-1113, ref-1114, ref-1116, ref-1136, ref-1138, ref-1141, ref-1145, ref-1146, ref-1173, ref-1299, ref-1301, ref-1242, ref-1263, ref-1260, ref-1371. 다시 연 출처는 ref-1228~ref-1370, ref-1372~ref-1376(webfetch), ref-031(github_raw)이다. ref-009·ref-010·ref-405·ref-579 는 입력 원문 텍스트로 대조했다. 브리프는 이 넷을 fetched: true 로 적으면서 summary 에 '원문 미열람'이라고 써서 서로 맞지 않는다. 벤더 주장은 f2(KUKA SL2 인증 '최초')와 f18(Zena RX)이다. Pudu 사례(f20·f29·f34·f55)는 같은 연구자 공개를 옮긴 기사 두 건 기준이라 교차 확인이 아니다. 주의: 연결의 절반 가까이가 [추정]이고 근거 대부분이 단일 출처의 재인용이다. f52 는 로봇이 아닌 작업자 스캐너 사례다. 로봇 제어기·승강기·기기 쪽 보안과 법 적용 판단은 연계 대상이다. 검색은 3회 썼다(리서치 13회와 합쳐 16/30). 정정 요청은 없다.",
  "retry_reason": null
}
```

### runs/2026-10-09-10/pages.json

```json
{
  "run_id": "2026-10-09-10",
  "outline": [
    {
      "path": "docs/categories/security-and-privacy/index.md",
      "section": "다른 대분류와의 연결",
      "budget_chars": 9500,
      "summary": "N. 보안·개인정보의 51. 인증·권한·격리, 52. 통신 보호·위협 관리·감사, 53. 개인정보·영상 데이터가 A~Q 가운데 16개 대분류의 세부영역과 이어지는 지점을 대분류별로 정리한다. 연결의 절반 가까이는 추정이며, 로봇 제어기·설비·기기 보안과 법 적용 판단은 연계 대상으로 둔다. [의견]",
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
        "f45",
        "f46",
        "f47",
        "f48",
        "f49",
        "f50",
        "f51",
        "f52",
        "f53",
        "f54",
        "f55",
        "f56"
      ]
    },
    {
      "path": "docs/categories/security-and-privacy/index.md",
      "section": "참고 자료",
      "budget_chars": 0,
      "summary": "기존 ref-009·ref-010 정의를 두고, 다른 대분류와의 연결 절에서 새로 인용한 출처 43건의 각주 정의를 끝에 덧붙인다."
    }
  ],
  "pages": [
    {
      "path": "docs/categories/security-and-privacy/index.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "다른 대분류와의 연결 절 첫 작성(A~Q 가운데 16개 대분류와의 연결, 현장 유형별 재묶음, 아직 다루지 않은 연결 목록), 참고 자료 절 끝에 각주 정의 43건 추가, 2차 수정 3건(장면 인식 모델 단정 삭제, C. 채팅 기반 구성·운영 호칭, 약어 풀어쓰기) 반영",
      "patches": [
        {
          "section": "다른 대분류와의 연결",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-09-10/pages/categories/security-and-privacy/index.md 의 해당 절을 본다)"
        },
        {
          "section": "참고 자료",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-09-10/pages/categories/security-and-privacy/index.md 의 해당 절을 본다)",
          "frontmatter": {
            "sources": [
              "ref-009",
              "ref-010",
              "ref-031",
              "ref-405",
              "ref-494",
              "ref-579",
              "ref-588",
              "ref-589",
              "ref-700",
              "ref-854",
              "ref-857",
              "ref-863",
              "ref-969",
              "ref-1076",
              "ref-1105",
              "ref-1106",
              "ref-1107",
              "ref-1109",
              "ref-1110",
              "ref-1111",
              "ref-1112",
              "ref-1113",
              "ref-1114",
              "ref-1116",
              "ref-1136",
              "ref-1138",
              "ref-1141",
              "ref-1145",
              "ref-1146",
              "ref-1173",
              "ref-1299",
              "ref-1301",
              "ref-1242",
              "ref-1263",
              "ref-1228",
              "ref-1368",
              "ref-1369",
              "ref-1370",
              "ref-1371",
              "ref-1372",
              "ref-1373",
              "ref-1374",
              "ref-1375",
              "ref-1376",
              "ref-1260"
            ]
          }
        }
      ]
    }
  ],
  "changelog_entry": "2026-10-09 | N. 보안·개인정보 | 다른 대분류와의 연결 절 첫 작성(A~Q 가운데 16개 대분류, 현장 유형별 재묶음, 아직 다루지 않은 연결 목록), 참고 자료 각주 정의 43건 추가, 1차 수정 26건·2차 수정 3건 반영 | run 2026-10-09-10",
  "index_updates": {
    "home_recent": "2026-10-09 — N. 보안·개인정보: 다른 대분류와의 연결 절 첫 작성(16개 대분류와의 연결, EU 사이버복원력법 보고 의무·EU 데이터법·로봇 관리 API 인가 결함 사례 포함, 열린 질문 4건 추가)",
    "category_recent": "2026-10-09 — N. 보안·개인정보: 다른 대분류와의 연결 절 첫 작성 — 51. 인증·권한·격리, 52. 통신 보호·위협 관리·감사, 53. 개인정보·영상 데이터와 A~Q 16개 대분류의 연결, 참고 자료 각주 43건 추가"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "actively-exploited-vulnerability",
      "term_ko": "적극 악용 취약점",
      "term_en": "Actively Exploited Vulnerability (EU Cyber Resilience Act)",
      "definition": "악의적 악용의 믿을 만한 증거가 있는 취약점으로, EU 사이버복원력법이 2026-09-11 부터 제조자에게 24시간 조기 경보·72시간 통지·최종 보고를 요구하는 대상이다.",
      "description": "통지는 ENISA 단일 보고 플랫폼을 통해 주 사업장 국가의 CSIRT 로 간다(집행위원회 안내 페이지 기준). 오케스트레이션 플랫폼 사업자가 제조자에 해당하는지는 열린 질문 oq-291 이다.",
      "related_areas": [
        52,
        57,
        59
      ],
      "sources": [
        "ref-1228"
      ]
    },
    {
      "action": "new",
      "slug": "connected-product",
      "term_ko": "연결 제품",
      "term_en": "Connected Product (EU Data Act)",
      "definition": "사용·성능·환경 데이터를 만들고 전송할 수 있는 제품으로, EU 데이터법이 사용자에게 그 데이터의 접근·공유 권리를 주는 대상이며 집행위원회 해설은 로봇과 산업 기계를 예로 든다.",
      "related_areas": [
        53,
        58
      ],
      "sources": [
        "ref-1376"
      ]
    },
    {
      "action": "new",
      "slug": "remote-attestation",
      "term_ko": "원격 증명",
      "term_en": "Remote Attestation",
      "definition": "원격 검증자가 기기가 보고하는 상태·측정값을 근거로 그 기기가 정상적으로 동작하고 있음을 확인하는 절차로, 보고 데이터가 발행 전에 위조되면 무력화될 수 있다.",
      "description": "Shen 외(2026-09, 프리프린트)는 ROS 2 에서 발행 전 훅으로 텔레메트리를 위조해 이 신뢰 경계가 깨질 수 있음을 보고했다(저자 보고값, 독립 재현 미확인).",
      "related_areas": [
        52,
        18
      ],
      "sources": [
        "ref-1374"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-009",
      "org": "ROS 2 Design",
      "title": "ROS 2 DDS-Security Integration",
      "published": null,
      "url": "https://design.ros2.org/articles/ros2_dds_security.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "ROS 2 의 DDS 보안 규격 인증·접근 통제·암호화 플러그인 통합을 설명하는 설계 문서(입력 원문 텍스트로 대조).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
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
      "accessed": "2026-10-09",
      "summary": "로봇 시스템 위협(신원 위조, 기본 자격증명 원격 접속, 공급망)과 완화책을 정리한 초안(입력 원문 텍스트 발췌로 대조).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "VDA 5050 3.0.0 명세 원문. 보안 통신은 범위 밖·브로커 구성 몫으로 두고, updateCertificate 즉시 동작(키·인증서 링크 필수, 인증 기관 링크 선택)과 TLS 내려받기·인증서 체인 검증 권고를 정한다.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
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
      "accessed": "2026-10-09",
      "summary": "Open-RMF 의 SROS 2 인클레이브와 웹 대시보드 TLS·OIDC·역할 기반 접근 통제를 설명(입력 원문 텍스트로 대조).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
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
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 위치 스푸핑 오염 에이전트를 신뢰 인지 모니터로 가려 다중 로봇 롤아웃 계획에서 빼는 방법(프리프린트).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-579",
      "org": "Open Robotics (ROS 2 Design)",
      "title": "ROS 2 Access Control Policies",
      "published": "2019-08",
      "url": "https://design.ros2.org/articles/ros2_access_control_policies.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "인클레이브별 토픽·서비스·액션 허용·거부 정책 형식을 정한 설계 문서(입력 원문 텍스트로 대조).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-588",
      "org": "김·장 법률사무소",
      "title": "'이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서' 관련 인사이트",
      "published": null,
      "url": "https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=30477",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 개인정보위 이동형 영상정보처리기기 안내서의 촬영 표시·거부 수용·목적 외 이용·보관 요구를 해설한 법률사무소 뉴스레터.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
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
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 제20조에서 사업장 내 근로자 감시 설비 설치를 노사협의회 협의 사항으로 둔다.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-700",
      "org": "Ravichandran, Z., Robey, A., Kumar, V., Pappas, G. J., & Hassani, H.(IEEE RA-L 2026 채택 표기)",
      "title": "Safety Guardrails for LLM-Enabled Robots",
      "published": "2025-03",
      "url": "https://arxiv.org/abs/2503.07885",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. RoboGuard 안전 가드레일로 탈옥 공격 시 위험 계획 실행을 줄였다고 보고(92% 초과→3% 미만은 arXiv v2 2026-03-03 기준, v1 은 다른 수치).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-854",
      "org": "Open Source Robotics Alliance (OSRA) Interop SIG",
      "title": "Open Robotics Discourse, Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP)",
      "published": "2026-06-25",
      "url": "https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. Open-RMF REST API 를 MCP 도구로 노출해 자연어 지시를 RMF 임무로 바꾸는 Nayantra 발표 안내.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-857",
      "org": "Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J.",
      "title": "Jailbreaking LLM-Controlled Robots",
      "published": "2024-11-09",
      "url": "https://arxiv.org/abs/2410.13691",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 언어 모델 제어 로봇 탈옥 알고리즘 RoboPAIR 와 높은 공격 성공률을 보고.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-863",
      "org": "European Commission — AI Act Service Desk",
      "title": "Article 12: Record-keeping (Regulation (EU) 2024/1689, Artificial Intelligence Act)",
      "published": "2024-06-13",
      "url": "https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 고위험 AI 시스템의 자동 사건 기록(로그) 요건 조문.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-969",
      "org": "바이라인네트워크",
      "title": "'로봇청소기' 다수 제품 보안 취약…대응방안은?",
      "published": "2025-10-31",
      "url": "https://byline.network/2025/10/31-283/",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. KISA·한국소비자원 로봇청소기 6종 보안 점검(40개 항목) 결과 보도.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1076",
      "org": "Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv)",
      "title": "Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066",
      "published": "2026-02-19",
      "url": "https://arxiv.org/abs/2602.17822",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. ISO 10218 2011·2025 판을 비교해 기능안전·사이버보안 요구 확대를 정리.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1105",
      "org": "IEC (SyC Smart Energy)",
      "title": "IEC 62443",
      "published": null,
      "url": "https://syc-se.iec.ch/deliveries/cybersecurity-guidelines/security-standards-and-best-practices/iec-62443/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. IEC 62443 시리즈의 구역·도관, 보안 수준, 기본 요구를 소개하는 IEC 페이지.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1106",
      "org": "OWASP GenAI Security Project",
      "title": "LLM01:2025 Prompt Injection",
      "published": null,
      "url": "https://genai.owasp.org/llmrisk/llm01-prompt-injection/",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 직접·간접 프롬프트 주입 구분과 완화책.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1107",
      "org": "CISA (미국 사이버보안·기반시설보안청)",
      "title": "Aethon TUG Home Base Server (ICSA-22-102-05)",
      "published": "2022-04-12",
      "url": "https://www.cisa.gov/news-events/ics-advisories/icsa-22-102-05",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 병원 자율이동로봇 TUG 플릿 서버의 인가 누락·인증 없는 제어 채널 취약점 권고.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1109",
      "org": "IES (Integrated Equipment Services)",
      "title": "Machinery Regulation Guide",
      "published": "2026-08-27",
      "url": "https://www.ies.co.uk/reference-library/machinery-regulation-guide",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. EU 기계류 규정의 변조 보호·개입 증거 기록·로그 요구와 적용일을 해설.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1110",
      "org": "Fernández-Becerra, L., González-Santamarta, M. Á., Guerrero-Higueras, Á. M., Rodríguez-Lera, F. J., & Matellán Olivera, V. (arXiv)",
      "title": "Enhancing Trust in Autonomous Agents: An Architecture for Accountability and Explainability through Blockchain and Large Language Models",
      "published": "2024-03",
      "url": "https://arxiv.org/abs/2403.09567",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 블록체인 기록과 LLM 설명으로 자율 에이전트 책임 추적성을 높이는 구조.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1111",
      "org": "엠에스투데이",
      "title": "선박·위성·로봇까지 해킹 표적…정부, '피지컬 AI' 산업 보안 기준 제시",
      "published": "2026-03-06",
      "url": "https://www.mstoday.co.kr/news/articleView.html?idxno=100755",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 과기정통부·KISA 의 선박·우주·로봇 분야 보안 자료 공개 보도.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1112",
      "org": "Nagaraja, N., Bagari, A., & Bahsi, H. (arXiv)",
      "title": "When Prompts Control Robots: Prompt Injection Attacks in Multi-Agent Robotic Systems",
      "published": "2026-08",
      "url": "https://arxiv.org/abs/2608.00747",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 다중 에이전트 로봇 시스템의 프롬프트 주입 공격 연구.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1113",
      "org": "Zhang, W., Kong, X., Dewitt, C., Braunl, T., & Hong, J. B. (arXiv)",
      "title": "A Study on Prompt Injection Attack Against LLM-Integrated Mobile Robotic Systems",
      "published": "2024-08",
      "url": "https://arxiv.org/abs/2408.03515",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. LLM 통합 이동로봇 시스템의 프롬프트 주입 공격 연구.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1114",
      "org": "Quarta, D., Pogliani, M., Polino, M., Maggi, F., Zanchettin, A. M., & Zanero, S. (IEEE S&P 2017)",
      "title": "An Experimental Security Analysis of an Industrial Robot Controller",
      "published": "2017",
      "url": "https://files01.core.ac.uk/download/pdf/84891817.pdf",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 산업용 로봇 제어기의 취약점이 제어 정확성·작업자 안전을 해칠 수 있음을 실험한 연구.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1116",
      "org": "IBF Solutions",
      "title": "New standards for industrial robots EN ISO 10218-1 and -2",
      "published": "2026-09-18",
      "url": "https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. ISO 10218-1/-2:2025 의 사이버보안 요구 추가와 EU 관보 등재를 해설.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1136",
      "org": "정보통신신문",
      "title": "\"자율주행차·로봇 카메라 촬영 시 외부에 표시해야\"",
      "published": "2024-10-14",
      "url": "https://www.koit.co.kr/news/articleView.html?idxno=125844",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 이동형 영상정보처리기기 안내서 공개(촬영 표시·거부 수용·위탁 시 보호책임자) 보도.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1138",
      "org": "개인정보보호위원회 (대한민국 정책브리핑)",
      "title": "자율주행차·이동형 로봇 개발에 '영상데이터' 원본 활용 허용",
      "published": "2023-11-15",
      "url": "https://www.korea.kr/news/policyNewsView.do?newsId=148922669",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 자율주행차·이동형 로봇 개발에 영상 원본 활용을 허용하는 방향의 정부 발표.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1141",
      "org": "아시아경제",
      "title": "\"로봇청소기 개인정보 관리 대체로 안전…미흡 사례 ... (제목 일부만 확인)",
      "published": "2026-09-14",
      "url": "https://view.asiae.co.kr/article/2026091410054053414",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 2026-09-14 개인정보위 로봇청소기 5개 사업자 점검 결과 보도.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1145",
      "org": "Xu, Y., & Ayday, E. (arXiv)",
      "title": "Seeing Less Is Not Seeing Safely: Privacy Leakage from Task-Scoped Robot Perception Exports",
      "published": "2026-09-02",
      "url": "https://arxiv.org/abs/2609.03055",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 과업 한정 로봇 인지 출력도 개인정보를 누출할 수 있음을 다룬 프리프린트.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1146",
      "org": "Sarfraz, B. M., Saplacan Lindblom, D., Baselizadeh, A., & Torresen, J. (HRI Companion '26)",
      "title": "The Privacy-Preserving Capabilities of a Service Robot in a Scenario-Based Healthcare Setting",
      "published": "2026-03-16",
      "url": "https://doi.org/10.1145/3776734.3794481",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 모의 진료실에서 서비스 로봇의 얼굴 가림 성능과 한계를 다룬 학회 부록 논문.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1173",
      "org": "ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan",
      "title": "REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction",
      "published": "2022-01-11",
      "url": "https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 사람 인지 규약 초안(영속 사람 ID 와 얼굴·몸·음성 ID 연결).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1299",
      "org": "ST Engineering Aethon (Newswire 게재 보도자료)",
      "title": "ST Engineering Aethon Launches Zena RX, Redefining Secure Delivery of Medications, Specimens and Sensitive Goods in Hospitals",
      "published": "2024-04-29",
      "url": "https://www.newswire.com/news/st-engineering-aethon-launches-zena-rx-redefining-secure-delivery-of-22310264",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 생체 인식·PIN 잠금 칸을 둔 병원 운반 로봇 출시 보도자료.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1301",
      "org": "경향신문 (곽희양)",
      "title": "내년 2월 자율주행 로봇이 아파트 내에서 배달 음식 나른다",
      "published": "2020-07-03",
      "url": "https://www.khan.co.kr/article/202007031130001",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 공동주택 배달 로봇 도입 계획(비밀번호로 적재함 열기) 보도.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1242",
      "org": "Carr, C., Wang, S., Wang, P., & Han, L. (arXiv)",
      "title": "Attacking Digital Twins of Robotic Systems to Compromise Security and Safety",
      "published": "2022-11-17",
      "url": "https://arxiv.org/abs/2211.09507",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. ROS 기반 디지털 트윈에 대한 중간자 공격이 물리 로봇 실패로 이어질 수 있음을 보고.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1263",
      "org": "메트로신문",
      "title": "AI·커머스·플랫폼 분야 규제 특례 확대…사업화 지원",
      "published": "2026-05-06",
      "url": "https://www.metroseoul.co.kr/article/20260506500296",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 배달로봇 카메라 원본 영상 AI 학습 실증특례 승인(조건 포함) 보도.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1228",
      "org": "European Commission (Shaping Europe's digital future)",
      "title": "CRA reporting",
      "published": null,
      "url": "https://digital-strategy.ec.europa.eu/en/policies/cra-reporting",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "EU 사이버복원력법 보고 의무 안내. 2026-09-11 부터 제조자의 적극 악용 취약점·중대 사고 보고, 24시간·72시간·14일(사고는 한 달) 시한, ENISA 단일 보고 플랫폼을 거쳐 주 사업장 CSIRT 로 통지. 페이지 최종 갱신 2026-09-11.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1368",
      "org": "The Register",
      "title": "Researcher who found McDonald's free-food hack turns her attention to Chinese restaurant robots",
      "published": "2025-08-29",
      "url": "https://www.theregister.com/2025/08/29/pudu_robots_hackable/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "Pudu Robotics 로봇 관리 소프트웨어의 권한 검사 누락(유효 토큰만 확인), 주문 변경·로봇 이동·이름 변경 가능성, 신고 지연과 제조사의 수정·보안 대응 센터 개설을 보도.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1369",
      "org": "Hackmag",
      "title": "Researcher finds a way to hack Chinese Pudu service robots",
      "published": "2025-09-05",
      "url": "https://hackmag.com/news/pudu-bugs",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "같은 Pudu 취약점 공개를 보도. BellaBot·FlashBot(승강기 같은 시스템 조작) 예시, 플릿 정지 가능성, 제조사 수정·보안 신고 주소 개설.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1370",
      "org": "Silicon UK",
      "title": "France Fines Amazon 32m Euros Over 'Excessive' Worker Surveillance",
      "published": "2024-01-23",
      "url": "https://www.silicon.co.uk/e-marketing/ecommerce/cnil-france-amazon-fine-546858",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "CNIL 의 Amazon France Logistique 3,200만 유로 과징금 보도. 스캐너 기반 비활동(10분)·빠른 스캔(1.25초) 지표, 31일 보관을 과도하다고 판단, Amazon 의 반박과 조치.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1371",
      "org": "CNIL (Commission nationale de l'informatique et des libertés)",
      "title": "Employee monitoring: CNIL fined AMAZON FRANCE LOGISTIQUE €32 million",
      "published": "2024-01-23",
      "url": "https://cnil.fr/en/employee-monitoring-cnil-fined-amazon-france-logistique-eu32-million",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. CNIL 공지(2023-12-27 결정, 2024-01-23 공표). 열었을 때 '더 이상 제공되지 않는 페이지'가 돌아와 검색 결과 요약(스캐너 기반 지표, 영상 감시 미흡 별도 위반)으로만 확인.",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1372",
      "org": "바이라인네트워크 (곽중희)",
      "title": "개인정보위 \"로봇청소기 5개 브랜드, 특별한 침해 위험 없어\"",
      "published": "2026-09-14",
      "url": "https://byline.network/2026/09/14-623/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "개인정보위 로봇청소기 5개 브랜드 점검 보도. 지도 정보 저장 위치(기기·일부 서버), 접근통제·전송 암호화 미흡 사례, 접근권한 내역·접속기록 보관 기간 연장 조치.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1373",
      "org": "바이라인네트워크",
      "title": "과기정통부, 선박·우주·로봇 보안 매뉴얼 공개",
      "published": "2026-03-06",
      "url": "https://byline.network/2026/03/6-340/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "과기정통부·KISA 의 로봇 보안모델 고도화판·로봇 보안요구사항 해설서 공개(2026-03-05 발표) 보도. 구체 요구 항목은 기사에 없음.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1374",
      "org": "Shen, L., Geng, S., Zheng, Y., & Lu, C. X. (arXiv)",
      "title": "Seeing is Not Believing: Breaking the Physical-to-Digital Trust Boundary in Robotics",
      "published": "2026-09-08",
      "url": "https://arxiv.org/abs/2609.08280",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "ROS 2 환경 변수로 실행되는 발행 전 훅으로 텔레메트리·제어 신호를 위조하는 공격과 Docker 컨테이너 공급망 경로를 보인 프리프린트(Secure ROS 2 로봇팔 87% 성공, 저자 보고값).",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1375",
      "org": "KUKA (Robotics Tomorrow 게재 보도자료)",
      "title": "KUKA is First to Achieve Security Level 2 Certification for Robotics Industry",
      "published": "2026-09-02",
      "url": "https://www.roboticstomorrow.com/news/2026/09/02/kuka-is-first-to-achieve-security-level-2-certification-for-robotics-industry/27035/",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "KUKA 가 iiQKA.OS2·KR C5-2 의 IEC 62443-4-2 SL2 인증을 로봇 제조사 최초로 받았다고 주장하는 보도자료. 인증 기관 미기재.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1376",
      "org": "European Commission (Shaping Europe's digital future)",
      "title": "Data Act explained",
      "published": null,
      "url": "https://digital-strategy.ec.europa.eu/en/policies/data-act-explained",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "EU 데이터법 해설. 2025-09-12 적용, 연결 제품(로봇·산업 기계 포함) 사용자의 데이터 접근·공유 권리, 데이터 보유자의 계약·고지 의무, 영업비밀 예외. 페이지 최종 갱신 2025-12-15.",
      "source_unopened": false,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    },
    {
      "id": "ref-1260",
      "org": "DIN Media",
      "title": "DIN EN ISO 13482 - 2024-10 (Draft standard) Robotik - Sicherheitsanforderungen für Serviceroboter (ISO/DIS 13482:2024)",
      "published": "2024-10",
      "url": "https://www.dinmedia.de/de/norm-entwurf/din-en-iso-13482/384079303",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. ISO 13482 개정 초안 소개(사이버보안·데이터 보호·승강기 협동 로봇 절 신설).",
      "source_unopened": true,
      "cited_by": [
        "docs/categories/security-and-privacy/index.md"
      ]
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "ROP 가 제조사 플릿 관리 서버·관리 API 를 연동하기 전에 인증 뒤 권한 검사 같은 인가 결함을 확인하는 최소 보안 시험 항목을 정한 공개 기준이나 사례가 있는가?",
      "areas": [
        51,
        20,
        54
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "로봇이 발행 전 단계에서 위조한 텔레메트리를 설비 센서·다른 로봇 관측과 교차 확인해 플릿 수준에서 탐지하는 방법의 효과를 측정한 연구가 있는가? (관련: oq-082)",
      "areas": [
        52,
        18,
        38
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "EU 데이터법에서 여러 제조사 로봇의 데이터를 모아 관제하는 오케스트레이션 플랫폼 사업자는 사용자·제3자·데이터 보유자 가운데 어느 지위이며, 제조사에 로봇 데이터 제공을 요구할 수 있는가? (관련: oq-259)",
      "areas": [
        58,
        53
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "작업자 스캐너 기록의 개인별 비활동·속도 지표를 과도한 감시로 본 CNIL 판단이 로봇 작업 기록에서 만든 작업자 지표에 적용된 감독기관 결정이나 국내 해석이 있는가? (관련: oq-285)",
      "areas": [
        53,
        60,
        39
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "가정",
      "item": "작업 대상",
      "link": "docs/categories/security-and-privacy/index.md#다른-대분류와의-연결",
      "title": "N. 보안·개인정보"
    },
    {
      "site_type": "가정",
      "item": "제약",
      "link": "docs/categories/security-and-privacy/index.md#다른-대분류와의-연결",
      "title": "N. 보안·개인정보"
    },
    {
      "site_type": "병원",
      "item": "완료·인계",
      "link": "docs/categories/security-and-privacy/index.md#다른-대분류와의-연결",
      "title": "N. 보안·개인정보"
    },
    {
      "site_type": "병원",
      "item": "예외·성과",
      "link": "docs/categories/security-and-privacy/index.md#다른-대분류와의-연결",
      "title": "N. 보안·개인정보"
    },
    {
      "site_type": "상업 시설",
      "item": "예외·성과",
      "link": "docs/categories/security-and-privacy/index.md#다른-대분류와의-연결",
      "title": "N. 보안·개인정보"
    },
    {
      "site_type": "제조 공장",
      "item": "예외·성과",
      "link": "docs/categories/security-and-privacy/index.md#다른-대분류와의-연결",
      "title": "N. 보안·개인정보"
    },
    {
      "site_type": "실외",
      "item": "제약",
      "link": "docs/categories/security-and-privacy/index.md#다른-대분류와의-연결",
      "title": "N. 보안·개인정보"
    },
    {
      "site_type": "기타",
      "item": "예외·성과",
      "link": "docs/categories/security-and-privacy/index.md#다른-대분류와의-연결",
      "title": "N. 보안·개인정보"
    }
  ],
  "additional_research_requests": [
    "51. 인증·권한·격리 페이지(이전 분류 기준)의 10절에 VDA 5050 updateCertificate(f5), Pudu 관리 API 인가 결함(f20·f22), Open-RMF OIDC·SROS 2(f37) 연결을 반영할 갱신 실행이 필요하다 — 대분류 연결 절과 세부영역 페이지의 근거를 맞추기 위해서다.",
    "52. 통신 보호·위협 관리·감사 7절에 EU 사이버복원력법 보고 의무(2026-09-11 시행, ref-1228)를 반영하고, 규정 원문 제14조를 열어 통지 경로·시한을 원문으로 확인해야 한다 — 이번에는 집행위원회 안내 페이지만 확인했다.",
    "D. 공간·지도 모델 페이지의 '다른 대분류와의 연결'에서 N. 보안·개인정보 연결이 '근거 없음'으로 남아 있으므로, 이번 f14·f15 근거로 그 대분류 페이지를 갱신하는 실행이 필요하다.",
    "Pudu 사례의 연구자 원문 공개와 제조사 공식 공지를 열어, 신고 지연 이유에 대한 두 기사(The Register·Hackmag)의 엇갈린 설명을 원문으로 확인해야 한다 — 현재는 같은 공개를 옮긴 기사 두 건뿐이다.",
    "KISA 로봇 보안모델 고도화판·로봇 보안요구사항 해설서 원문의 요구 항목(oq-250)과 ISO 10218-1:2025 사이버보안 조항 번호(oq-102)를 확인해야 A. 기획·사업·M. 안전 연결을 구체화할 수 있다.",
    "배달로봇 원본 영상 실증특례(ref-1263)·개인정보위 원본 활용 허용(ref-1138)에서 원본 영상으로 학습하는 모델의 종류(예: 장면 인식·주행 모델)를 원문으로 확인해야 L. AI·학습 기술의 45. 문서·도면·장면 이해 연결을 구체화할 수 있다 — 2차 검증에서 브리프 밖 단정으로 삭제했다.",
    "N. 보안·개인정보와 5. 로봇 능력·작업 표현, 8~11. 채팅 영역, 23. 업무 시스템 연동, 24·26·28. 계획 영역, 30. 로봇 간 협업·물리적 인계, 33·35. 설계 영역, 46. 예측·학습 기반 최적화, 49. 사람 근접 안전, 56. 운영 이관·확대·교육의 연결 근거가 없다 — 다음 대분류 연결 실행의 조사 대상이다.",
    "물류창고 현장의 로봇(작업자 스캐너가 아닌) 보안·개인정보 사례가 없어 물류창고 × N. 보안·개인정보 칸을 채우지 못했다 — 물류창고 로봇 관제의 보안 사고·감독기관 결정을 찾아야 한다."
  ],
  "fixes_applied": [
    "절 이름 — patches 의 section 을 번호 없는 '다른 대분류와의 연결'로 쓰고, 그 밖에는 '참고 자료' 절에 각주 정의만 append 했다.",
    "각주 정의 — 새로 인용한 출처 43건의 정의를 '참고 자료' 절 끝에 '[^ref-NNN]: 기관, 제목, 발행일, URL, 접근일 2026-10-09' 형식으로 더했고 기존 ref-009·ref-010 정의는 그대로 두었다.",
    "원문 미열람 표기 — 지시된 31개 출처(ref-494 ~ ref-1260, ref-1371 포함)의 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었다.",
    "ref-009·ref-010·ref-031·ref-405·ref-579 — 각주에 '(원문 미열람)'을 붙이지 않았고, reference_updates 에서 summary 의 '원문 미열람.' 문구를 빼고 입력 원문 텍스트로 대조했다고 고쳐 source_unopened: false 로 두었다.",
    "ref-1228·ref-1376 발행일 — 각주 발행일 자리에 각각 '미확인(페이지 최종 갱신 2026-09-11)', '미확인(페이지 최종 갱신 2025-12-15)'을 썼다.",
    "f2 — A. 기획·사업 항목에서 [추정] 뒤에 '벤더 주장'을 병기하고, 인증 사실과 '최초'가 모두 KUKA 보도자료의 주장이며 인증 기관이 적혀 있지 않음을 밝혔다.",
    "f18 — E. 사물·사람·실시간 상태 항목에서 [추정]과 '벤더 주장'을 유지하고, Zena RX 는 제조사 보도자료(2024-04-29), 공동주택 비밀번호 방식은 2020-07 계획 단계 보도임을 밝혔다.",
    "범위 경계 — 첫머리 범위 경계 단락에 제어기·설비·기기 쪽 연계 대상을 밝히고, f2·f3·f44 는 제어기 보안을 로봇 제조사 쪽 연계 대상으로, f21·f25·f55 의 방화벽·VPN·승강기 제어는 시설·설비 제어 경계의 연계 대상으로, f14·f18·f56 의 앱·기기 보안·잠금 칸 인증·얼굴 가림은 제조사 기능의 연계 대상으로 각 항목에 짧게 적었다.",
    "법 적용 판단 — 첫머리 범위 경계 단락에서 법령·규정 적용 판단은 운영 사업자·법무가 맡는 연계 대상이고 ROP 몫은 기록·통보·데이터 흐름 규칙 제공까지라고 한 번 밝혔다.",
    "f5 — B. 로봇 온톨로지 항목에서 키·인증서 내려받기 링크는 필수, 인증 기관 내려받기 링크만 선택 매개변수라고 고쳐 썼다.",
    "f5·f28 — ref-031 은 직접 인용 없이 모두 재서술했다(B. 로봇 온톨로지, H. 실행·협업·예외 복구, F. 연동 항목).",
    "f11 — RoboGuard 수치(92% 초과→3% 미만)를 arXiv 개정판 v2(2026-03-03) 기준으로 적고, v1 은 다른 수치를 보고했으며 RoboPAIR·RoboGuard 두 수치 모두 저자 보고값·독립 재현 미확인임을 병기했다.",
    "f16 — E. 사물·사람·실시간 상태 항목에서 프리프린트임을 밝히고 87%·약 3 ms 가 저자 보고값이며 독립 재현이 확인되지 않았음을 병기했다.",
    "f17 — '위치 스푸핑이 배정을 무너뜨린다'를 '위치 스푸핑으로 오염된 에이전트가 롤아웃 기반 배정·경로 계획의 비용 개선을 없앨 수 있다(GPS 스푸핑·택시 수요 실험, 물류센터 적용 미확인)'로 고쳤다.",
    "f35 — 통지 경로를 'ENISA 단일 보고 플랫폼을 통해 주 사업장 국가의 CSIRT 에 알려야'로 고치고, 집행위원회 안내 페이지 기준이며 규정 원문은 열지 않았다고 밝혔다.",
    "f49 — '(보통 제조사)'를 삭제했다.",
    "f39 — K. 플랫폼 아키텍처·인프라 항목에서 보관 기간 연장 조치의 적용 대상(점검 사업자 한정 여부)과 근거 조항이 미확인임을 바로 뒤 문장에 밝히고 oq-214 를 붙였다.",
    "f20·f29·f34·f55 — 두 기사가 같은 연구자 공개를 옮긴 것으로 교차 확인이 아니라는 점, 실제 악용·피해 보도가 없다는 점, f29·f55 의 플릿 정지·사무실 시스템 피해는 연구자·매체의 가능성 평가라는 점을 F. 연동, H. 실행·협업·예외 복구, J. 현장 운영·관제, Q. 현장 유형별 적용 항목에 밝혔다.",
    "f34 — 신고 지연 이유를 The Register 는 제조사가 신고 창구 부재를 인정했다고, Hackmag 은 제조사가 다른 경로로 보고를 받았다고 설명했다고 전한다며 두 설명을 함께 적었다.",
    "f33 — J. 현장 운영·관제 항목에서 '업계 해설에 따르면'으로 시작하고 규정 원문 미열람과 오케스트레이션 플랫폼 적용 여부가 oq-249 임을 유지했다.",
    "f1 — A. 기획·사업 항목에서 같은 정부 발표를 옮긴 기사 기준이라 독립 교차 확인이 아니며 구체 요구 항목은 미확인(oq-250)임을 밝혔다.",
    "f52 — P. 거버넌스·법규·사회 항목에서 로봇이 아니라 작업자 휴대 스캐너 기록 사례이며 Amazon 이 사실과 다르다며 이의 제기 권리를 유보했다고 밝혔고, Q. 현장 유형별 적용의 61. 물류창고 항목에서 ROP 적용 사례로 보지 않는다고 적었으며 site_matrix_updates 에 물류창고 칸을 넣지 않았다.",
    "18·34 구분 — f16·f17 은 E. 사물·사람·실시간 상태 항목에 현재 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성 쪽으로, f30·f31 은 I. 설계·시뮬레이션 항목에 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현 쪽으로 나눠 쓰고 서로 구분된다고 밝혔다.",
    "L. AI·학습 기술 교차 규칙 — f11 은 13. 대화형 기능의 신뢰·기반과 44. 로봇 기반 모델·언어 모델 계획을 함께, f40 은 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영과 66. 실외 적용 사례를 함께, f41 은 47. AI·학습·적응과 모델 운영과 적용 대상 13. 대화형 기능의 신뢰·기반을 함께 적었다.",
    "열린 질문 등록 — 위조 텔레메트리 질문 끝에 '(관련: oq-082)', CNIL 판단 적용 질문에 '(관련: oq-285)', 데이터법상 플랫폼 지위 질문에 '(관련: oq-259)'를 붙여 open_question_updates 로 냈다.",
    "아직 다루지 않은 연결 — 절 끝 '아직 다루지 않은 연결' 소제목 아래에 5. 로봇 능력·작업 표현, 8~11. 채팅 영역, 23·24·26·28·30·33·35·46·49·56번 세부영역을 대분류별로 번호와 이름을 함께 써서 목록으로 남겼다.",
    "2차: L. AI·학습 기술 항목 장면 인식 모델 단정 — '45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영 ↔ 53. 개인정보·영상 데이터' 항목에서 '학습 데이터로 쓰이는 대상은 장면 인식 모델이며,'를 삭제하고 '현장 유형으로는 Q. 현장 유형별 적용의 66. 실외 사례다.'만 남겼으며, 학습 모델 종류 확인은 additional_research_requests 에 적었다.",
    "2차: 대분류 호칭 — C. 채팅 기반 구성·운영 소제목 아래 안내 문장의 '분류 원문 C 주석은'을 '분류 원문의 C. 채팅 기반 구성·운영 주석은'으로 고쳤다.",
    "2차: 약어 풀어쓰기 — 첫 등장에서 OWASP(Open Worldwide Application Security Project), 미국 사이버보안·기반시설보안청(Cybersecurity and Infrastructure Security Agency, CISA), 공통 취약점 식별 번호(Common Vulnerabilities and Exposures, CVE), 공통 취약점 점수 체계(Common Vulnerability Scoring System, CVSS), SROS 2(Secure ROS 2, F. 연동의 22. 설비·건물 시스템 연동 항목), 데이터 분산 서비스(Data Distribution Service, DDS)로 풀어 썼고 문장 내용·태그·각주는 바꾸지 않았다."
  ],
  "standards_updates": []
}
```

### runs/2026-10-09-10/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/security-and-privacy/index.md (2개 절)
```

### runs/2026-10-09-10/pages/categories/security-and-privacy/index.md

```markdown
---
title: "N. 보안·개인정보"
type: category
status: draft
created: 2026-09-28
updated: 2026-10-09
version: 2
sources: [ref-009, ref-010, ref-031, ref-405, ref-494, ref-579, ref-588, ref-589, ref-700, ref-854, ref-857, ref-863, ref-969, ref-1076, ref-1105, ref-1106, ref-1107, ref-1109, ref-1110, ref-1111, ref-1112, ref-1113, ref-1114, ref-1116, ref-1136, ref-1138, ref-1141, ref-1145, ref-1146, ref-1173, ref-1299, ref-1301, ref-1242, ref-1263, ref-1228, ref-1368, ref-1369, ref-1370, ref-1371, ref-1372, ref-1373, ref-1374, ref-1375, ref-1376, ref-1260]
---

[홈](../../index.md) › N. 보안·개인정보

# N. 보안·개인정보

## 핵심 질문

누가 어떤 로봇에 무엇을 시킬 수 있는지 통제하고, 데이터와 사람의 정보를 어떻게 지킬 것인가? [분류원문]

## 개요

인증·권한·격리, 통신 보호, 위협 관리와 감사 기록, 문서·대화 입력 보안, 개인정보·영상 데이터 보호. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **51. 인증·권한·격리** | 장비·사용자 인증, 명령 권한, 원격 접속 계정, 고객·현장 격리 | 외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가? | [51. 인증·권한·격리](authentication-authorization-and-isolation.md) | published |
| **52. 통신 보호·위협 관리·감사** | 통신 보호, 위협 모델·취약점, 문서·대화 입력 보안, 감사 기록 | 통신·문서·대화를 통한 공격이 로봇 동작으로 이어지지 않게 하려면? | [52. 통신 보호·위협 관리·감사](communication-protection-threat-management-and-audit.md) | published |
| **53. 개인정보·영상 데이터** | 영상·작업자·거주자 데이터 보호, 최소 수집·익명화 | 로봇이 찍은 영상과 사람의 위치 정보를 어디까지 모으고 어떻게 지킬 것인가? | [53. 개인정보·영상 데이터](privacy-and-video-data.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

ROS 2도 인증·암호화·접근권한과 보안 위협 모델을 별도로 다룬다. 기능 연동과 보안 연동은 함께 설계해야 하는 영역이다. [9][10] [분류원문]

## 다른 대분류와의 연결

이 절은 게시된 [51. 인증·권한·격리](authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](privacy-and-video-data.md) 페이지와 다른 대분류 페이지의 검증된 주장을 근거로, N. 보안·개인정보의 세 세부영역이 다른 대분류의 어느 세부영역과 무엇으로 이어지는지 정리한다. 연결의 절반 가까이가 추정이고 근거 대부분이 단일 출처의 재인용이므로, 문장마다 붙은 태그로 확인된 사실과 추정을 나눠 읽는다. 본문의 oq 번호는 [열린 질문](../../open-questions.md) 페이지의 항목이다.

범위 경계는 분류 원문 19장을 따른다. 로봇 제어기·운영체제·펌웨어 보안은 '로봇 자체 지능·제어' 경계의 제조사 몫, 현장 망의 방화벽·VPN과 승강기 조작은 '시설·설비 제어' 경계의 연계 대상, 앱·기기 쪽 보안과 얼굴 가림·잠금 칸 인증은 제조사 기능에 속하는 연계 대상이다. 법령·규정이 실제로 적용되는지의 판단은 운영 사업자·법무가 맡는 연계 대상이며, 아래 연결에서 ROP 몫은 기록·통보·데이터 흐름 규칙을 제공하는 데까지로 본다. [의견]

### A. 기획·사업

대분류 페이지: [A. 기획·사업](../planning-and-business/index.md)

- **[1. 기술·시장·업체 동향](../planning-and-business/technology-market-and-vendor-trends.md) ↔ 52. 통신 보호·위협 관리·감사.** 과학기술정보통신부와 한국인터넷진흥원(Korea Internet & Security Agency, KISA)은 2026-03-05 로봇 보안모델 고도화판과 로봇 보안요구사항 해설서를 공개했고, 피지컬 AI 확산과 유럽·북미 사이버보안 규제 강화를 반영해 기업이 개발·수출 과정의 보안 요구를 파악하게 하는 것을 목적으로 밝혔다. [사실][^ref-1373][^ref-1111] 두 근거는 같은 정부 발표를 옮긴 기사라 독립 교차 확인이 아니며, 보안모델·해설서의 구체 요구 항목은 미확인이다(oq-250).
- **[2. 사용 사례·요구·책임 범위](../planning-and-business/use-cases-requirements-and-scope.md) ↔ 52. 통신 보호·위협 관리·감사.** 52. 통신 보호·위협 관리·감사 페이지는 ROP가 자신이 여는 연결의 보안과 전체 연결 구조의 위협 모델을 맡고 로봇 제어기·펌웨어와 현장 망 보안은 제조사·시설 IT/OT(정보기술/운영기술) 쪽 연계 대상으로 두므로, 이 보안 책임 경계가 2. 사용 사례·요구·책임 범위의 책임 범위 정의에 들어가야 할 것으로 보인다. [추정][^ref-1114][^ref-1107][^ref-009]
- **[3. 경제성·조달·사업 모델](../planning-and-business/economics-procurement-and-business-models.md) ↔ 51. 인증·권한·격리.** KUKA는 iiQKA.OS2 운영체제와 KR C5-2 제어기 플랫폼이 IEC 62443-4-2 보안 수준 2(SL2) 인증을 받았고 로봇 제조사 가운데 처음이라고 2026-09-02 발표했는데, 인증 사실과 '최초'는 모두 KUKA 보도자료의 주장이고 발표문에 인증 기관은 적혀 있지 않으며 제어기 보안 인증 자체는 로봇 제조사 쪽 연계 대상이다. [추정] 벤더 주장[^ref-1375] IEC 62443이 보안 수준을 정하고 로봇 제어기 단위의 인증 발표가 나오고 있으므로 로봇·플랫폼 조달 요구에 구성요소 보안 인증 여부와 목표 보안 수준을 넣는 일이 3. 경제성·조달·사업 모델로 넘어갈 것으로 보이나, 플릿 관리 소프트웨어 단위의 인증 사례는 확인하지 못했다. [추정][^ref-1105][^ref-1375]

### B. 로봇 온톨로지

대분류 페이지: [B. 로봇 온톨로지](../robot-ontology/index.md)

- **[4. 이기종 로봇 등록](../robot-ontology/heterogeneous-robot-registration.md) ↔ 51. 인증·권한·격리.** VDA 5050 3.0.0은 로봇이 새 인증서 묶음을 내려받아 활성화하게 하는 즉시 동작 updateCertificate를 두며, 키 내려받기 링크와 인증서 내려받기 링크는 필수 매개변수이고 인증 기관 내려받기 링크만 선택 매개변수다. [사실][^ref-031] 명세는 이 내려받기도 전송 계층 보안(Transport Layer Security, TLS)으로 보호해야 하고 활성화 전에 인증서 체인을 검증하는 것이 바람직하다고 적는다(3.0.0 판, 발행일 미확인, 2026-10-09 확인). [사실][^ref-031]
- **4. 이기종 로봇 등록·[7. 온톨로지 검증·변경 관리](../robot-ontology/ontology-verification-and-change-management.md), O. 검증·도입·수명주기의 [57. 자산·소프트웨어 수명주기 관리](../verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) ↔ 51. 인증·권한·격리.** 로봇마다 인증서 교체 지원 여부와 인증서 판·만료를 등록 정보로 두고 교체 이력을 판 관리와 함께 다루면 인증서 교체 대상과 시점을 추적할 수 있을 것으로 보이나, 이를 등록 항목·판 관리로 다룬 공개 구현은 확인하지 못했다. [추정][^ref-031] 교체 승인과 실패 때 되돌림 책임은 oq-113으로 남아 있다.
- **4. 이기종 로봇 등록 ↔ 53. 개인정보·영상 데이터.** 53. 개인정보·영상 데이터 페이지가 카메라 유무·촬영 사실 표시 수단·영상 전송 경로 기록과 로봇 인지 출력 필드 축소를 ROP 직접 범위로 보므로, 이런 개인정보 관련 속성이 4. 이기종 로봇 등록의 등록 항목으로 넘어갈 것으로 보인다. [추정][^ref-1145][^ref-588]
- **[6. 온톨로지 기반 시스템·로봇 연동](../robot-ontology/ontology-based-system-and-robot-integration.md) ↔ 51. 인증·권한·격리.** ROS 2 접근 제어 정책은 인클레이브별로 토픽·서비스·액션 단위의 허용·거부를 두므로, '진단은 허용하고 이동은 막는' 명령 단위 권한을 걸려면 6. 온톨로지 기반 시스템·로봇 연동이 능력을 실제 명령에 묶을 때 권한 정책과 같은 명령 식별자를 공유해야 할 것으로 보인다. [추정][^ref-579][^ref-405] 능력 모델과 권한 정책을 잇는 공개 사례는 확인하지 못했다.

### C. 채팅 기반 구성·운영

대분류 페이지: [C. 채팅 기반 구성·운영](../chat-based-configuration-and-operation/index.md). 분류 원문의 C. 채팅 기반 구성·운영 주석은 대화 결과를 실행 명령이 아니라 계획으로 보고 사람이 확인·승인한 계획만 실행하게 하므로, 아래 보안 연결은 이 원칙과 함께 읽는다. 업무 지시 대화가 부르는 엔진은 G. 계획·최적화의 25. 작업 배정 — MRTA와 26. 작업 순서·스케줄링이다.

- **[13. 대화형 기능의 신뢰·기반](../chat-based-configuration-and-operation/conversational-trust-and-foundations.md) ↔ 52. 통신 보호·위협 관리·감사.** OWASP(Open Worldwide Application Security Project) LLM01:2025는 프롬프트 주입을 사용자가 직접 넣는 직접 주입과 문서·웹 같은 외부 내용에 숨은 지시가 들어오는 간접 주입으로 나누고 완화책을 정리한다. [사실][^ref-1106]
- **[12. 채팅으로 업무 지시·오케스트레이션](../chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) ↔ 52. 통신 보호·위협 관리·감사.** 대규모 언어 모델(Large Language Model, LLM)을 통합한 이동로봇 시스템에 대한 프롬프트 주입 공격 연구(Zhang 외, 2024-08)와 다중 에이전트 로봇 시스템에서 프롬프트가 로봇을 제어할 때의 프롬프트 주입 공격 연구(Nagaraja 외, 2026-08)가 있다. [사실][^ref-1113][^ref-1112]
- **13. 대화형 기능의 신뢰·기반, L. AI·학습 기술의 [44. 로봇 기반 모델·언어 모델 계획](../ai-and-learning/robot-foundation-models-and-llm-planning.md) ↔ 52. 통신 보호·위협 관리·감사.** Robey 외는 언어 모델이 제어하는 로봇에서 탈옥 알고리즘 RoboPAIR의 공격 성공률이 자주 100%에 이르렀다고 보고했고, Ravichandran 외의 RoboGuard는 arXiv 개정판 v2(2026-03-03) 기준으로 최악의 탈옥 공격에서 위험 계획 실행을 92% 초과에서 3% 미만으로 줄였다고 보고했다. [사실][^ref-857][^ref-700] v1은 다른 수치를 보고했고, 두 수치 모두 저자 보고값이며 독립 재현은 확인되지 않았다.
- **12. 채팅으로 업무 지시·오케스트레이션 ↔ 51. 인증·권한·격리.** Open-RMF REST API를 언어 모델 도구로 노출하는 모델 컨텍스트 프로토콜(Model Context Protocol, MCP) 서버(Nayantra) 같은 구조에서는 탈옥된 모델이 해로운 동작을 낼 수 있으므로, 모델에 넘기는 도구·로봇·구역 권한을 최소로 제한하는 접근 통제가 '사람이 확인·승인한 계획만 실행' 원칙과 함께 두 대분류의 경계가 될 것으로 보인다. [추정][^ref-854][^ref-857] 발표 안내문에는 권한 제한 구성이 나오지 않는다.
- **12. 채팅으로 업무 지시·오케스트레이션 ↔ 52. 통신 보호·위협 관리·감사.** '사람이 확인·승인한 계획만 실행'이 지켜졌음을 사후에 보이려면 누가 어떤 계획을 언제 승인했는지를 변조 탐지가 가능한 감사 기록으로 남겨야 할 것으로 보이며, 자율 에이전트 행동을 블록체인 기록과 언어 모델 설명으로 추적하는 구조 연구(2024-03)가 그 후보다. [추정][^ref-1110] 대화 승인 기록에 적용한 사례는 확인하지 못했다(oq-248).

### D. 공간·지도 모델

대분류 페이지: [D. 공간·지도 모델](../space-and-map-model/index.md)

- **[16. 장소 의미·지도 관리](../space-and-map-model/place-semantics-and-map-management.md) ↔ 53. 개인정보·영상 데이터.** 개인정보보호위원회가 2026-09-14 발표한 로봇청소기 5개 브랜드(2025-03 기준 최신 모델) 점검에서 집 내부 구조를 나타내는 지도 정보는 모든 제품이 기기에 저장하고 스마트폰에는 저장하지 않았으며 일부 제품은 서버에도 저장했고, 일부 사업자는 로봇청소기 접근통제와 개인정보 전송 암호화가 미흡했다. [사실][^ref-1372][^ref-1141] 위원회는 특별한 개인정보 침해 위험은 확인되지 않았다고 밝혔고, 지도 저장 위치는 기사 한 건에서만 확인했다. [사실][^ref-1372] 앱 인증·기기 저장은 제조사 기능의 연계 대상이다.
- **[15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md)·16. 장소 의미·지도 관리 ↔ 51. 인증·권한·격리·53. 개인정보·영상 데이터.** 건물 내부 지도가 개인정보 점검 대상 정보로 다뤄지고 VDA 5050이 지도를 관제가 지정한 링크에서 내려받게 하므로, ROP가 보관·배포하는 지도의 저장 위치·전송 암호화·접근 권한을 정하는 일이 두 대분류를 잇는 지점이 될 것으로 보인다. [추정][^ref-1372][^ref-031] 업무 시설 지도의 접근 통제를 다룬 기관 자료는 찾지 못했으며, 이 연결은 D. 공간·지도 모델 페이지가 근거 없음으로 남긴 자리를 채운다.

### E. 사물·사람·실시간 상태

대분류 페이지: [E. 사물·사람·실시간 상태](../objects-people-and-live-state/index.md)

- **[18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md) ↔ 52. 통신 보호·위협 관리·감사.** Shen 외(2026-09, 프리프린트)는 ROS 2에서 환경 변수 하나를 바꾸면 사전 빌드된 훅이 텔레메트리·제어 신호를 발행 전에 가로채고 주입할 수 있음을 보였고, Secure ROS 2를 쓴 실제 Franka 로봇팔에서 약 3 ms 지터로 위조 텔레메트리를 넣어 AI 기반 탐지기 상대로도 87% 성공했다고 보고했다. [사실][^ref-1374] 87%와 약 3 ms는 저자 보고값이고 독립 재현은 확인되지 않았다.
- **18. 실시간 세계 상태·데이터 일관성, J. 현장 운영·관제의 [38. 모니터링·이상 탐지·원인 분석](../field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) ↔ 52. 통신 보호·위협 관리·감사.** 로봇이 보고하는 상태가 통신 보호 이전 단계에서 위조될 수 있고, 위치 스푸핑으로 오염된 에이전트가 롤아웃 기반 배정·경로 계획의 비용 개선을 없앨 수 있다는 연구(GPS 스푸핑·택시 수요 실험, 물류센터 적용 미확인)가 있으므로, 18. 실시간 세계 상태·데이터 일관성의 상태 신뢰도 판단과 38. 모니터링·이상 탐지·원인 분석은 암호화된 보고만 믿지 말고 설비 센서·다른 로봇 관측과 교차 확인해야 할 것으로 보인다. [추정][^ref-1374][^ref-494] 이는 현재 상태를 표현하는 쪽의 문제이며(oq-082), I. 설계·시뮬레이션의 가정한 미래 실험과는 구분한다.
- **[17. 작업 대상·자산 식별과 인계 추적](../objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md) ↔ 51. 인증·권한·격리·53. 개인정보·영상 데이터.** 병원 운반 로봇 Zena RX는 생체 인식과 직원 PIN으로 잠금 칸을 연다고 제조사 보도자료(2024-04-29)가 밝히고, 공동주택 배달 로봇은 2020-07 계획 단계 보도에서 비밀번호로 적재함을 열게 했으므로, '누구에게 넘겼는가' 기록은 인증 수단과 생체·전화번호 처리 규칙에 기댈 것으로 보인다. [추정] 벤더 주장[^ref-1299][^ref-1301] 잠금 칸·생체 인증은 제조사 기능의 연계 대상이다(oq-293).
- **[19. 사람·보행자 모델](../objects-people-and-live-state/people-and-pedestrian-model.md) ↔ 53. 개인정보·영상 데이터.** ROS 규약 제안 REP-155(Draft 상태, 2022-01-11 작성)는 사람마다 영속 ID를 두고 얼굴·몸·음성 ID를 후보 대응으로 연결하며, 개인정보·동의는 다루지 않는다. [사실][^ref-1173]

### F. 연동

대분류 페이지: [F. 연동](../integration/index.md)

- **[20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md) ↔ 51. 인증·권한·격리.** 2025-08 한 보안 연구자는 Pudu Robotics 로봇 관리 소프트웨어가 유효한 인증 토큰만 확인하고 그 뒤 권한을 검사하지 않아, 교차 사이트 스크립팅(Cross-Site Scripting, XSS)이나 체험 계정으로 얻은 토큰으로 주문을 바꾸고 로봇을 다른 위치로 보내고 이름을 바꿀 수 있었다고 공개했다. [사실][^ref-1368][^ref-1369] 근거 두 기사는 같은 연구자 공개를 옮긴 것이라 교차 확인이 아니며, 실제 악용 사례는 보도되지 않았다.
- **20. 로봇·제조사 관제 연동 ↔ 52. 통신 보호·위협 관리·감사.** 미국 사이버보안·기반시설보안청(Cybersecurity and Infrastructure Security Agency, CISA) 권고 ICSA-22-102-05(2022-04-12)는 병원 자율이동로봇 TUG를 제어하는 Home Base Server에서 인증 없이 웹소켓으로 로봇을 제어할 수 있는 취약점(공통 취약점 식별 번호(Common Vulnerabilities and Exposures, CVE) CVE-2022-1070, 공통 취약점 점수 체계(Common Vulnerability Scoring System, CVSS) 9.8)과 인가 누락 취약점을 공개했다. [사실][^ref-1107] 권고가 드는 방화벽·VPN 같은 망 조치는 시설 IT/OT 쪽 연계 대상이다.
- **20. 로봇·제조사 관제 연동 ↔ 51. 인증·권한·격리.** 식당 서빙 로봇과 병원 운반 로봇 사례 모두 제조사 플릿 서버·관리 API의 인증·인가 결함이 로봇 제어로 이어졌으므로, ROP가 제조사 관제를 연결할 때 연결 계정의 권한 범위와 인가 확인을 연동 승인 조건으로 둬야 할 것으로 보인다. [추정][^ref-1368][^ref-1107] 그런 인가 시험을 정한 공개 기준은 확인하지 못했다(oq-100).
- **[21. 상호운용 표준·적합성](../integration/interoperability-standards-and-conformance.md) ↔ 52. 통신 보호·위협 관리·감사.** VDA 5050 3.0.0은 범위 절에서 보안 통신·데이터 보호의 메커니즘·기술·절차를 정하지 않는다고 밝히고, 프로토콜 보안은 브로커 구성으로 다뤄야 하며 이 지침에서는 다루지 않는다고 적는다. [사실][^ref-031] 상호운용 규격이 통신 보안을 범위 밖 브로커 구성에 맡기므로 21. 상호운용 표준·적합성의 적합성 시험과 브로커·API의 상호 인증·TLS 설정 확인은 별도 경로로 관리해야 할 것으로 보이며, 그 최소 요구를 정한 공개 보안 프로파일은 확인하지 못했다. [추정][^ref-031][^ref-1105] 관련 질문은 oq-246이다.
- **[22. 설비·건물 시스템 연동](../integration/facility-and-building-system-integration.md) ↔ 51. 인증·권한·격리.** 승강기 같은 설비를 조작하는 서비스 로봇(FlashBot)도 같은 관리 API 결함의 대상이 될 수 있다고 보도되었으므로, 로봇 관제·설비 어댑터 구성요소를 SROS 2(Secure ROS 2) 인클레이브처럼 별도 신원·접근 규칙으로 나눠 설비 명령 권한을 제한하는 설계가 두 대분류의 경계가 될 것으로 보인다. [추정][^ref-1369][^ref-405] 승강기 제어 자체는 시설·설비 제어 경계의 연계 대상이다(oq-056).

### G. 계획·최적화

대분류 페이지: [G. 계획·최적화](../planning-and-optimization/index.md)

- **[25. 작업 배정 — MRTA](../planning-and-optimization/task-allocation-mrta.md) ↔ 51. 인증·권한·격리.** Francos 외(2026-08, 프리프린트)는 위치 스푸핑으로 오염된 에이전트가 롤아웃 기반 다중 로봇 배정·경로 계획의 비용 개선을 없앨 수 있다고 보고, 스푸핑 공격 모델과 탐지된 적대 에이전트를 이후 계획에서 빼는 방법을 제안했다. [사실][^ref-494] 실험은 GPS 스푸핑 데이터와 택시 수요로 했으며 물류센터 적용은 확인되지 않았다.
- **25. 작업 배정 — MRTA·[27. 다중 로봇 경로·교통 관리 — MAPF](../planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) ↔ 51. 인증·권한·격리.** 제조사 관리 API를 거쳐 주문을 바꾸거나 로봇 위치를 옮길 수 있었던 사례가 있으므로, ROP의 배정·교통 계획은 자신이 내리지 않은 임무 변경·이동을 로봇 상태에서 감지해 해당 로봇을 계획에서 보류하는 규칙이 필요할 것으로 보인다. [추정][^ref-1368] 계획 쪽 감지 규칙을 다룬 자료는 확인하지 못했다.

### H. 실행·협업·예외 복구

대분류 페이지: [H. 실행·협업·예외 복구](../execution-collaboration-and-recovery/index.md)

- **[29. 명령·작업 실행의 신뢰성](../execution-collaboration-and-recovery/command-and-task-execution-reliability.md) ↔ 51. 인증·권한·격리.** VDA 5050 3.0.0에서 updateCertificate 동작은 실행 중에는 인증서를 내려받아 설치하고 있다는 상태로, 실패하면 내려받기 또는 설치 실패로 보고되므로, 보안 명령도 일반 명령처럼 실행 확인·실패 처리 대상이 된다. [사실][^ref-031]
- **[32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md) ↔ 52. 통신 보호·위협 관리·감사.** 식당 서빙 로봇 관리 API 결함으로 영업 중 플릿 전체 작업을 취소하거나 멈출 수 있었다는 보도는 연구자·매체의 가능성 평가이고 실제 사고는 보도되지 않았지만, 보안 사고로 플릿 일부·전체를 격리하고 수동 운영으로 넘어가는 시나리오가 32. 예외 복구·재계획·업무 연속성의 복구 절차에 들어가야 할 것으로 보인다. [추정][^ref-1368][^ref-1369]

### I. 설계·시뮬레이션

대분류 페이지: [I. 설계·시뮬레이션](../design-and-simulation/index.md)

- **[34. 시뮬레이션·예측용 디지털 트윈](../design-and-simulation/simulation-and-predictive-digital-twin.md) ↔ 52. 통신 보호·위협 관리·감사.** Carr 외(2022)는 ROS로 구동되는 시스템에서 디지털 트윈에 대한 중간자 공격이 물리 로봇의 실패로 이어질 수 있으며, 이는 산업용 로봇팔과 자율이동로봇 모두에 해당한다고 보고했다. [사실][^ref-1242]
- **34. 시뮬레이션·예측용 디지털 트윈·[36. 가상 시운전·실제 상황 재현](../design-and-simulation/virtual-commissioning-and-real-situation-replay.md) ↔ 52. 통신 보호·위협 관리·감사·53. 개인정보·영상 데이터.** 가정한 미래를 실험하는 시뮬레이션과 실제 상황 재현에 운영 기록·영상을 입력으로 쓰면 그 기록의 무결성과 '재현' 목적의 이용 범위를 함께 정해야 할 것으로 보이며, 이는 현재 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성의 상태 신뢰도 문제와 구분된다. [추정][^ref-1242][^ref-588] 관련 질문은 oq-306·oq-308이다.

### J. 현장 운영·관제

대분류 페이지: [J. 현장 운영·관제](../field-operations-and-monitoring/index.md)

- **[37. 관제 화면·실행 기록](../field-operations-and-monitoring/control-screen-and-execution-records.md) ↔ 52. 통신 보호·위협 관리·감사.** Fernández-Becerra 외(2024-03)는 자율 에이전트의 행동을 블록체인 기반 기록과 대규모 언어 모델 설명으로 남겨 책임 추적성과 설명 가능성을 높이는 구조를 제안했다. [사실][^ref-1110] 수백 대 규모의 지연·저장 비용은 oq-248로 열려 있다.
- **37. 관제 화면·실행 기록 ↔ 52. 통신 보호·위협 관리·감사.** 업계 해설에 따르면 EU 기계류 규정 (EU) 2023/1230은 변조 보호, 개입 증거 기록, 안전 소프트웨어 판 추적 로그를 요구하며 2027-01-20 전면 적용된다. [사실][^ref-1109] 규정 원문은 열지 못했고, 이 요구가 오케스트레이션 플랫폼에 미치는지는 oq-249로 열려 있다.
- **38. 모니터링·이상 탐지·원인 분석 ↔ 52. 통신 보호·위협 관리·감사.** 위 E. 사물·사람·실시간 상태 항목의 상태 교차 확인 추정이 38. 모니터링·이상 탐지·원인 분석에도 걸린다.
- **[40. 운영 절차·요청 창구](../field-operations-and-monitoring/operating-procedures-and-request-channels.md) ↔ 52. 통신 보호·위협 관리·감사.** Pudu 사례에서 연구자의 신고(2025-08-12 시작)는 응답을 받지 못하다가 고객사(Skylark Holdings·Zensho)에 알린 뒤에야 처리되었고, 제조사는 이후 취약점을 고치고 보안 대응 센터와 신고 주소를 만들었다. [사실][^ref-1368][^ref-1369] 지연 이유에 대해 The Register는 제조사가 보안 신고 창구가 없어 대응이 늦었다고 인정했다고 전하고, Hackmag은 제조사가 다른 경로로 보고를 받았다고 설명했다고 전한다. [사실][^ref-1368][^ref-1369] 두 기사는 같은 연구자 공개를 옮긴 것이라 교차 확인이 아니다.
- **40. 운영 절차·요청 창구, O. 검증·도입·수명주기의 57. 자산·소프트웨어 수명주기 관리, P. 거버넌스·법규·사회의 [59. 법·규제·보험·라이선스](../governance-law-and-society/law-regulation-insurance-and-licensing.md) ↔ 52. 통신 보호·위협 관리·감사.** EU 사이버복원력법(Cyber Resilience Act, CRA)에 따라 2026-09-11부터 디지털 요소 제품 제조자는 적극 악용되는 취약점과 중대 사고를 유럽연합 사이버보안청(ENISA) 단일 보고 플랫폼을 통해 주 사업장 국가의 컴퓨터 보안 사고 대응팀(Computer Security Incident Response Team, CSIRT)에 알려야 하며, 인지 후 24시간 안에 조기 경보와 72시간 안에 통지를 내고, 최종 보고는 취약점이면 시정 조치가 나온 뒤 14일 안에, 중대 사고면 72시간 통지 뒤 한 달 안에 낸다. [사실][^ref-1228] 이 내용은 집행위원회 안내 페이지 기준이며 규정 원문은 열지 않았다.
- **40. 운영 절차·요청 창구 ↔ 52. 통신 보호·위협 관리·감사.** 신고 창구가 없던 제조사 사례와 24·72시간 보고 시한을 함께 보면, 여러 제조사 로봇을 운영하는 현장의 요청 창구에 보안 취약점·사고 접수와 제조사·ROP 사업자 사이 통보 경로를 두는 일이 40. 운영 절차·요청 창구로 넘어갈 것으로 보인다. [추정][^ref-1228][^ref-1368] 보고 의무는 제조자에 걸리며, 플랫폼 사업자의 해당 여부는 oq-291로 열려 있다.

### K. 플랫폼 아키텍처·인프라

대분류 페이지: [K. 플랫폼 아키텍처·인프라](../platform-architecture-and-infrastructure/index.md)

- **[41. 플랫폼 아키텍처·외부 API](../platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) ↔ 51. 인증·권한·격리.** Open-RMF 문서는 웹 대시보드를 TLS로 제공하고 OpenID Connect(OIDC)로 사용자 역할을 담은 서명 토큰을 API 서버에 보내 역할에 따라 접근을 허용하며, ROS 2 쪽 구성요소는 SROS 2 인클레이브로 권한을 나눈다고 설명한다. [사실][^ref-405]
- **[42. 분산 시스템·통신·컴퓨팅 구조](../platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md) ↔ 52. 통신 보호·위협 관리·감사.** ROS 2는 데이터 분산 서비스(Data Distribution Service, DDS) 보안 규격의 인증·접근 통제·암호화 플러그인을 쓰고, ROS 2 위협 모델 초안은 보안이 꺼진 시스템에서는 어떤 노드든 어떤 토픽에나 발행할 수 있어 신원 위조와 명령 가로채기가 가능하다고 정리한다. [사실][^ref-009][^ref-010]
- **[43. 데이터·관측성·배포](../platform-architecture-and-infrastructure/data-observability-and-deployment.md) ↔ 51. 인증·권한·격리·53. 개인정보·영상 데이터.** 2026-09-14 로봇청소기 점검 보도에 따르면 개인정보보호위원회는 점검 후속 조치로 접근권한 부여 내역 보관 기간을 200일에서 3년으로, 접속기록 보관 기간을 90일에서 2년 이상으로 늘리도록 했다. [사실][^ref-1372] 이 조치가 점검 사업자에만 해당하는지와 근거 조항은 기사에 없어 미확인이다(oq-214).

### L. AI·학습 기술

대분류 페이지: [L. AI·학습 기술](../ai-and-learning/index.md)

- **[45. 문서·도면·장면 이해](../ai-and-learning/document-drawing-and-scene-understanding.md)·[47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md) ↔ 53. 개인정보·영상 데이터.** 개인정보보호위원회는 2023-11 자율주행차·이동형 로봇 개발에 영상데이터 원본 활용을 허용하는 방향을 밝혔고, 2026-05-06 ICT 규제샌드박스 심의위원회는 배달로봇 카메라 원본 영상을 AI 학습에 쓰는 과제에 연구 목적 내 활용·개인 식별 금지·제3자 제공 금지 등을 조건으로 실증특례를 승인했다. [사실][^ref-1138][^ref-1263] 현장 유형으로는 Q. 현장 유형별 적용의 66. 실외 사례다.
- **47. AI·학습·적응과 모델 운영 ↔ 52. 통신 보호·위협 관리·감사.** EU AI Act 제12조는 고위험 AI 시스템이 수명 기간 동안 사건 기록(로그)을 자동으로 남길 수 있어야 하고, 위험 상황·실질적 변경 식별, 시판 후 감시, 배포자의 운영 감시에 필요한 사건을 기록하게 한다. [사실][^ref-863] ROP의 AI 구성요소, 특히 13. 대화형 기능의 신뢰·기반이 다루는 대화 기능이 고위험에 해당하는지는 oq-106·oq-143으로 열려 있다.
- **44. 로봇 기반 모델·언어 모델 계획 ↔ 52. 통신 보호·위협 관리·감사.** 탈옥·가드레일 연구는 위 C. 채팅 기반 구성·운영 항목에 적용 대상 영역과 함께 적었다.

### M. 안전

대분류 페이지: [M. 안전](../safety/index.md)

- **[50. 안전 표준·인증·사고 조사](../safety/safety-standards-certification-and-incident-investigation.md) ↔ 51. 인증·권한·격리·52. 통신 보호·위협 관리·감사.** 산업용 로봇 안전 표준 ISO 10218-1/-2의 2025년 개정판에는 사이버보안 요구가 새로 들어갔다. [사실][^ref-1116][^ref-1076] 업계 해설과 판 비교 논문이 같은 내용을 전하지만 조항 번호는 미확인이다(oq-102).
- **50. 안전 표준·인증·사고 조사 ↔ 51. 인증·권한·격리·53. 개인정보·영상 데이터.** 서비스 로봇 안전 표준 ISO 13482 개정 초안(ISO/DIS 13482:2024, DIN EN ISO 13482 2024-10 초안)은 사이버보안과 데이터 보호 절을 새로 넣었다. [사실][^ref-1260] 최종판에 남았는지는 미확인이다(oq-254).
- **[48. 안전·위험 관리](../safety/safety-and-risk-management.md) ↔ 52. 통신 보호·위협 관리·감사.** Quarta 외(IEEE S&P 2017)는 널리 쓰이는 산업용 로봇 제어기의 소프트웨어 취약점과 구조적 결함으로 제어 정확성과 작업자 안전 요구를 무너뜨릴 수 있음을 실험으로 보인 것으로 보이며(검색 결과 요약 기준), 제어기 보안은 로봇 제조사 쪽 연계 대상이다. [추정][^ref-1114]
- **48. 안전·위험 관리 ↔ 51. 인증·권한·격리.** 산업용·서비스 로봇 안전 표준에 사이버보안과 데이터 보호가 들어오면서, ROP가 내리는 원격 정지·재개·구역 변경 명령의 권한 통제가 안전 평가 대상이 될 것으로 보인다. [추정][^ref-1116][^ref-1260] 로봇 자체 안전 기능은 연계 대상이다.

### O. 검증·도입·수명주기

대분류 페이지: [O. 검증·도입·수명주기](../verification-deployment-and-lifecycle/index.md)

- **[54. 시험·형식 검증·벤치마크](../verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md) ↔ 52. 통신 보호·위협 관리·감사.** 2025년 한국인터넷진흥원·한국소비자원의 로봇청소기 6종 점검은 모바일앱 보안·정책 관리·기기 보안 3개 영역 40개 항목으로 이루어졌다고 보도되어, 로봇 보안 시험 항목의 국내 참고 틀이 될 것으로 보인다. [추정][^ref-969] 다중 로봇 관제 플랫폼에 같은 틀을 쓴 사례는 확인하지 못했다.
- **[55. 현장 조사·설치·시운전](../verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md) ↔ 52. 통신 보호·위협 관리·감사.** ROS 2 위협 모델 초안이 기본 자격증명을 쓰는 SSH 같은 원격 접속을 권한 상승 경로로 들므로, 설치·시운전 점검 항목에 기본 자격증명 변경과 원격 접속 범위 확인이 들어가야 할 것으로 보인다. [추정][^ref-010]
- **57. 자산·소프트웨어 수명주기 관리 ↔ 52. 통신 보호·위협 관리·감사.** ROS 2 위협 모델 초안은 빌드 팜과 서드파티 구성요소를 통한 공급망 위협을 주요 위협으로 들고, Shen 외(2026-09)는 제3자 Docker 컨테이너·보조 도구에 대한 폭넓은 의존을 이용해 악성 훅이 든 패키지를 퍼뜨릴 수 있다고 적는다. [사실][^ref-010][^ref-1374] 위 B. 로봇 온톨로지 항목의 인증서 교체 이력과 J. 현장 운영·관제 항목의 사이버복원력법 보고 의무도 57. 자산·소프트웨어 수명주기 관리로 이어진다.

### P. 거버넌스·법규·사회

대분류 페이지: [P. 거버넌스·법규·사회](../governance-law-and-society/index.md)

- **[58. 다사업자 책임·계약·데이터](../governance-law-and-society/multi-party-responsibility-contracts-and-data.md) ↔ 53. 개인정보·영상 데이터.** EU 데이터법은 2025-09-12부터 적용되며, 로봇·산업 기계 같은 연결 제품의 사용자가 사용으로 생긴 데이터에 접근해 직접 쓰거나 제3자와 공유할 수 있게 하고, 데이터 보유자는 사용자와 계약을 두고 생성 데이터 종류·양·수집 빈도를 알려야 한다. [사실][^ref-1376] 여러 제조사 로봇의 데이터를 모아 관제하는 ROP 사업자가 데이터법상 사용자·제3자 가운데 어느 쪽이고 개인정보 처리에서 운영자·수탁자 가운데 어느 쪽인지가 계약으로 정해야 할 쟁점이 될 것으로 보인다. [추정][^ref-1376][^ref-588] 플랫폼 사업자 지위를 다룬 해석은 확인하지 못했다(oq-259).
- **59. 법·규제·보험·라이선스 ↔ 53. 개인정보·영상 데이터.** 개인정보보호위원회 이동형 영상정보처리기기 안내서 공개 보도와 법률사무소 해설은 카메라를 단 자율주행차·배달로봇이 외부에 촬영 사실을 표시하고 명확히 거부하는 사람의 의사를 받아들여야 한다고 전한다. [사실][^ref-1136][^ref-588] 두 출처는 같은 안내서 발표를 옮긴 것이라 독립 교차 확인이 아니며, 위 J. 현장 운영·관제 항목의 사이버복원력법 보고 의무도 59. 법·규제·보험·라이선스와 이어진다.
- **[60. 노동·수용성·접근성](../governance-law-and-society/labor-acceptance-and-accessibility.md) ↔ 53. 개인정보·영상 데이터.** 프랑스 개인정보 감독기관 CNIL은 2023-12-27 결정(2024-01-23 공표)으로 Amazon France Logistique에 3,200만 유로 과징금을 부과했는데, 물류창고 작업자 스캐너 기록으로 10분 넘는 비활동을 실시간 경보하고 1.25초 안의 빠른 스캔을 표시하는 지표와 모든 데이터·지표의 31일 보관을 과도하다고 보았다. [사실][^ref-1370][^ref-1371] 이 사례는 로봇이 아니라 작업자 휴대 스캐너 기록에 관한 것이며, Amazon은 사실과 다르다며 이의 제기 권리를 유보했다. [사실][^ref-1370]
- **60. 노동·수용성·접근성, J. 현장 운영·관제의 [39. 운영 성과 측정·개선](../field-operations-and-monitoring/operational-performance-measurement-and-improvement.md) ↔ 53. 개인정보·영상 데이터.** 작업자 스캐너 기록의 개인별 비활동·속도 지표가 과도한 감시로 판단된 사례가 있으므로, ROP가 로봇 작업과 연결해 개별 작업자의 처리량·위치를 기록할 때 39. 운영 성과 측정·개선의 지표를 집계 단위로 두고 보존 기간을 줄이는 설계가 필요할 것으로 보인다. [추정][^ref-1370][^ref-589] 로봇 연동 지표에 이 판단이 적용된 사례는 확인하지 못했다(oq-285).
- **60. 노동·수용성·접근성 ↔ 53. 개인정보·영상 데이터.** 근로자참여 및 협력증진에 관한 법률 제20조는 사업장 내 근로자 감시 설비의 설치를 노사협의회 협의 사항으로 둔다. [사실][^ref-589] 카메라 로봇이 감시 설비에 해당하는지는 oq-099로 열려 있다.

### Q. 현장 유형별 적용

대분류 페이지: [Q. 현장 유형별 적용](../site-type-applications/index.md). 현장마다 다른 요구는 Q. 현장 유형별 적용에 모으고 공통 기능은 위 대분류에 두므로, 위 사례를 현장 유형별로 다시 묶는다.

- **[61. 물류창고](../site-type-applications/warehouse.md):** 위 P. 거버넌스·법규·사회 항목의 CNIL 사례는 물류창고에서 일어났지만 로봇이 아닌 작업자 스캐너 기록 사례라 ROP 적용 사례로 보지 않는다.
- **[62. 제조 공장](../site-type-applications/manufacturing-plant.md):** 산업용 로봇 제어기 취약점 실험(M. 안전 항목).
- **[63. 병원·의료](../site-type-applications/hospital-and-healthcare.md):** TUG 플릿 서버 취약점(F. 연동 항목)과 Zena RX 잠금 칸 인증(E. 사물·사람·실시간 상태 항목, 벤더 주장)이 있다. 진료실을 흉내 낸 모의 시나리오에서 의사·환자를 알아보도록 학습한 서비스 로봇은 대상이 아닌 사람의 얼굴을 안정적으로 가렸지만 자세 변화·가림·조명 변화가 인식 신뢰도를 낮췄다. [사실][^ref-1146] 실제 병원 도입이 아닌 모의 실험이며, 기기 쪽 얼굴 가림은 제조사 기능의 연계 대상이다.
- **[64. 상업 시설](../site-type-applications/commercial-facilities.md):** Pudu 식당 서빙 로봇의 관리 API 결함과 신고 지연(F. 연동, H. 실행·협업·예외 복구, J. 현장 운영·관제 항목).
- **[65. 가정·공동주택](../site-type-applications/home-and-apartment.md):** 로봇청소기 지도 저장 위치(D. 공간·지도 모델 항목), 접근권한 내역·접속기록 보관 기간(K. 플랫폼 아키텍처·인프라 항목), 보안 점검 40개 항목(O. 검증·도입·수명주기 항목).
- **[66. 실외](../site-type-applications/outdoor.md):** 배달로봇 원본 영상 실증특례(L. AI·학습 기술 항목), 촬영 사실 표시·거부 수용(P. 거버넌스·법규·사회 항목).
- **[67. 기타 현장](../site-type-applications/other-sites.md):** 같은 Pudu 결함 보도는 사무실에서 승강기 같은 설비를 조작하는 서비스 로봇(FlashBot)이 사무실 시스템을 망가뜨리거나 지식재산을 빼내는 데 쓰일 수 있다고 평가했는데, 이는 연구자·매체의 가능성 평가이며 확인된 사고는 아니다. [추정][^ref-1369][^ref-1368]

### 아직 다루지 않은 연결

이번 근거로는 N. 보안·개인정보와의 연결을 찾지 못한 세부영역이다. 다음 대분류 연결 실행이나 해당 영역 실행에서 다룬다.

- B. 로봇 온톨로지: 5. 로봇 능력·작업 표현
- C. 채팅 기반 구성·운영: 8. 채팅으로 맵 작성, 9. 채팅으로 시나리오 구성, 10. 채팅으로 로봇 구성, 11. 채팅으로 실제 상황 시뮬레이션 재현
- F. 연동: 23. 업무 시스템 연동
- G. 계획·최적화: 24. 작업·워크플로 모델링, 26. 작업 순서·스케줄링, 28. 공용 자원·충전·에너지 최적화
- H. 실행·협업·예외 복구: 30. 로봇 간 협업·물리적 인계
- I. 설계·시뮬레이션: 33. 시나리오 모델·편집, 35. 처리능력·규모·배치 설계
- L. AI·학습 기술: 46. 예측·학습 기반 최적화
- M. 안전: 49. 사람 근접 안전
- O. 검증·도입·수명주기: 56. 운영 이관·확대·교육

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 45건이다(논문 13건 · 기사·보고서 11건 · 업체 발표 0건 · 표준·오픈소스·기관 자료 21건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-1145](../../references/ref-1145.md) — Xu, Y., & Ayday, E. (arXiv), Seeing Less Is Not Seeing Safely: Privacy Leakage from Task-Scoped Robot Perception Exports (발행 2026-09-02)
- [ref-1112](../../references/ref-1112.md) — Nagaraja, N., Bagari, A., & Bahsi, H. (arXiv), When Prompts Control Robots: Prompt Injection Attacks in Multi-Agent Robotic Systems (발행 2026-08)
- [ref-1144](../../references/ref-1144.md) — Huang, X., Pan, S., Reinhardt, D., & Bennewitz, M. (arXiv), Designing Privacy-Preserving Visual Perception for Robot Navigation Based on User Privacy Preferences (발행 2026-04-07)
- [ref-1146](../../references/ref-1146.md) — Sarfraz, B. M., Saplacan Lindblom, D., Baselizadeh, A., & Torresen, J. (HRI Companion '26), The Privacy-Preserving Capabilities of a Service Robot in a Scenario-Based Healthcare Setting (발행 2026-03-16)
- [ref-585](../../references/ref-585.md) — Jaatun 외(Journal of Cybersecurity and Privacy 6(2), 52), Security Aspects of Zones and Conduits in IEC 62443 (발행 2026)
- [ref-1108](../../references/ref-1108.md) — Mayoral-Vilches, V. (Alias Robotics, arXiv), The Cybersecurity of a Humanoid Robot (발행 2025-09-17)
- [ref-1143](../../references/ref-1143.md) — Choi, M. 외 (arXiv), Real-Time Privacy Preservation for Robot Visual Perception (발행 2025-05-08)
- [ref-700](../../references/ref-700.md) — Ravichandran, Z., Robey, A., Kumar, V., Pappas, G. J., & Hassani, H.(IEEE RA-L 2026 채택 표기), Safety Guardrails for LLM-Enabled Robots (발행 2025-03)
- [ref-857](../../references/ref-857.md) — Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J., Jailbreaking LLM-Controlled Robots (발행 2024-11-09)
- [ref-1113](../../references/ref-1113.md) — Zhang, W., Kong, X., Dewitt, C., Braunl, T., & Hong, J. B. (arXiv), A Study on Prompt Injection Attack Against LLM-Integrated Mobile Robotic Systems (발행 2024-08)
- 그 밖에 3건

**기사·보고서**

- [ref-1141](../../references/ref-1141.md) — 아시아경제, "로봇청소기 개인정보 관리 대체로 안전…미흡 사례 ... (제목 일부만 확인) (발행 2026-09-14)
- [ref-1109](../../references/ref-1109.md) — IES (Integrated Equipment Services), Machinery Regulation Guide (발행 2026-08-27)
- [ref-1111](../../references/ref-1111.md) — 엠에스투데이, 선박·위성·로봇까지 해킹 표적…정부, ‘피지컬 AI’ 산업 보안 기준 제시 (발행 2026-03-06)
- [ref-969](../../references/ref-969.md) — 바이라인네트워크, '로봇청소기' 다수 제품 보안 취약…대응방안은? (발행 2025-10-31)
- [ref-1140](../../references/ref-1140.md) — 경향신문, 로봇청소기가 우리집 사진 찍어 외부 유출?…6종 ... (제목 일부만 확인) (발행 2025-09-02)
- [ref-1136](../../references/ref-1136.md) — 정보통신신문, "자율주행차·로봇 카메라 촬영 시 외부에 표시해야" (발행 2024-10-14)
- [ref-1139](../../references/ref-1139.md) — 법무법인(유) 세종, 개인정보보호위원회, 비정형데이터 가명처리 관련 가명정보 처리 가이드라인 개정 (뉴스레터) (발행 2024-02-08)
- [ref-968](../../references/ref-968.md) — MIT Technology Review (Eileen Guo), A Roomba recorded a woman on the toilet. How did screenshots end up on Facebook? (발행 2022-12-19)
- [ref-588](../../references/ref-588.md) — 김·장 법률사무소, '이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서' 관련 인사이트 (발행 미확인)
- [ref-471](../../references/ref-471.md) — A3(Association for Advancing Automation), Updated ISO 10218 \| Answers to Frequently Asked Questions (FAQs) (발행 미확인)
- 그 밖에 1건

**업체 발표**

- 아직 없음

**표준·오픈소스·기관 자료**

- [ref-1135](../../references/ref-1135.md) — 개인정보보호위원회, [현재 안내서] 이동형 영상정보처리기기를 위한 개인영상정보 보호ㆍ활용 안내서(2024.9.) (발행 2024-10-14)
- [ref-1138](../../references/ref-1138.md) — 개인정보보호위원회 (대한민국 정책브리핑), 자율주행차·이동형 로봇 개발에 ‘영상데이터’ 원본 활용 허용 (발행 2023-11-15)
- [ref-582](../../references/ref-582.md) — NIST, NIST SP 800-82 Rev. 3, Guide to Operational Technology (OT) Security (발행 2023-09)
- [ref-555](../../references/ref-555.md) — European Union (EUR-Lex), Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery (발행 2023-06)
- [ref-1107](../../references/ref-1107.md) — CISA (미국 사이버보안·기반시설보안청), Aethon TUG Home Base Server (ICSA-22-102-05) (발행 2022-04-12)
- [ref-580](../../references/ref-580.md) — Open Robotics (ROS 2 Design), ROS 2 Security Enclaves (발행 2020-05)
- [ref-1147](../../references/ref-1147.md) — European Data Protection Board (EDPB), Guidelines 3/2019 on processing of personal data through video devices (발행 2020-01)
- [ref-579](../../references/ref-579.md) — Open Robotics (ROS 2 Design), ROS 2 Access Control Policies (발행 2019-08)
- [ref-584](../../references/ref-584.md) — CSA / IEC (ANSI Webstore), CAN/CSA IEC 62443-3-3-2017 - Industrial communication networks - Network and system security - Part 3-3: System security requirements and security levels (Adopted IEC 62443-3-3:2013, first edition, 2013-08) (발행 2013-08)
- [ref-591](../../references/ref-591.md) — European Commission (Shaping Europe's digital future), The Cyber Resilience Act - Summary of the legislative text (발행 미확인)
- 그 밖에 11건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-30 · 갱신 · [53. 개인정보·영상 데이터](privacy-and-video-data.md) — seed → draft: 3~11절 첫 작성(제25조의2·이동형 안내서, 목적별 이용·가명처리, 가림·저해상도·출력 필드 기술, 가정·병원·실외 사례, 책임 경계, 연결 16개 영역, 열린 질문 11건), 13절 각주, 1차 수정 15건·2차 수정 4건 반영 (실행 2026-09-30-16)
- 2026-09-30 · 생성 · [53. 개인정보·영상 데이터 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area53-s6.md) — 자동 분리: 53. 개인정보·영상 데이터 의 "6. 대표 접근법과 기술" 절(1,883자)을 옮겼다 (실행 2026-09-30-16)
- 2026-09-30 · 생성 · [53. 개인정보·영상 데이터 — 열린 질문](../../topics/2026/2026-09-30-area53-s11.md) — 자동 분리: 53. 개인정보·영상 데이터 의 "11. 열린 질문" 절을 옮겼다. 2차 수정: 기존 질문 7건을 등록 문장 그대로 옮기고 부분 근거 메모 2건에 [추정]·각주, EDPB 풀어쓰기 (실행 2026-09-30-16)
- 2026-09-30 · 생성 · [53. 개인정보·영상 데이터 — 대표 연구와 자료](../../topics/2026/2026-09-30-area53-s8.md) — 자동 분리: 53. 개인정보·영상 데이터 의 "8. 대표 연구와 자료" 절을 옮겼다. 2차 수정: Xu·Ayday 항목의 플랫폼 필드 설계 연결 문장을 [추정]으로 분리 (실행 2026-09-30-16)
- 2026-09-30 · 생성 · [53. 개인정보·영상 데이터 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area53-s4.md) — 자동 분리: 53. 개인정보·영상 데이터 의 "4. 핵심 개념과 용어" 절(1,008자)을 옮겼다 (실행 2026-09-30-16)
<!-- auto:category-recent:end -->

## 참고 자료

원문의 [9]는 참고문헌 [ref-009](../../references/ref-009.md)에 해당한다.[^ref-009] 원문의 [10]은 참고문헌 [ref-010](../../references/ref-010.md)에 해당한다.[^ref-010]

[^ref-009]: ROS 2 Design, ROS 2 DDS-Security Integration, 미확인, https://design.ros2.org/articles/ros2_dds_security.html, 접근일 2026-09-28
[^ref-010]: ROS 2 Design, ROS 2 Robotic Systems Threat Model, 미확인, https://design.ros2.org/articles/ros2_threat_model.html, 접근일 2026-09-28

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09
[^ref-405]: Open Robotics, Security - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/security.html, 접근일 2026-10-09
[^ref-494]: Francos, R. M., Garces, D., Akgün, O. E., Bastian, N. D., & Gil, S.(Harvard·JHU), Trust-Aware Sequential Decision Making and Rollout Planning for Resilient Multi-Robot Systems, 2026-08, https://arxiv.org/abs/2608.25690, 접근일 2026-10-09 (원문 미열람)
[^ref-579]: Open Robotics (ROS 2 Design), ROS 2 Access Control Policies, 2019-08, https://design.ros2.org/articles/ros2_access_control_policies.html, 접근일 2026-10-09
[^ref-588]: 김·장 법률사무소, '이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서' 관련 인사이트, 미확인, https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=30477, 접근일 2026-10-09 (원문 미열람)
[^ref-589]: 법제처 국가법령정보센터, 근로자참여 및 협력증진에 관한 법률, 미확인, https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=105636, 접근일 2026-10-09 (원문 미열람)
[^ref-700]: Ravichandran, Z., Robey, A., Kumar, V., Pappas, G. J., & Hassani, H.(IEEE RA-L 2026 채택 표기), Safety Guardrails for LLM-Enabled Robots, 2025-03, https://arxiv.org/abs/2503.07885, 접근일 2026-10-09 (원문 미열람)
[^ref-854]: Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse, Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP), 2026-06-25, https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687, 접근일 2026-10-09 (원문 미열람)
[^ref-857]: Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J., Jailbreaking LLM-Controlled Robots, 2024-11-09, https://arxiv.org/abs/2410.13691, 접근일 2026-10-09 (원문 미열람)
[^ref-863]: European Commission — AI Act Service Desk, Article 12: Record-keeping (Regulation (EU) 2024/1689, Artificial Intelligence Act), 2024-06-13, https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12, 접근일 2026-10-09 (원문 미열람)
[^ref-969]: 바이라인네트워크, '로봇청소기' 다수 제품 보안 취약…대응방안은?, 2025-10-31, https://byline.network/2025/10/31-283/, 접근일 2026-10-09 (원문 미열람)
[^ref-1076]: Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv), Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066, 2026-02-19, https://arxiv.org/abs/2602.17822, 접근일 2026-10-09 (원문 미열람)
[^ref-1105]: IEC (SyC Smart Energy), IEC 62443, 미확인, https://syc-se.iec.ch/deliveries/cybersecurity-guidelines/security-standards-and-best-practices/iec-62443/, 접근일 2026-10-09 (원문 미열람)
[^ref-1106]: OWASP GenAI Security Project, LLM01:2025 Prompt Injection, 미확인, https://genai.owasp.org/llmrisk/llm01-prompt-injection/, 접근일 2026-10-09 (원문 미열람)
[^ref-1107]: CISA (미국 사이버보안·기반시설보안청), Aethon TUG Home Base Server (ICSA-22-102-05), 2022-04-12, https://www.cisa.gov/news-events/ics-advisories/icsa-22-102-05, 접근일 2026-10-09 (원문 미열람)
[^ref-1109]: IES (Integrated Equipment Services), Machinery Regulation Guide, 2026-08-27, https://www.ies.co.uk/reference-library/machinery-regulation-guide, 접근일 2026-10-09 (원문 미열람)
[^ref-1110]: Fernández-Becerra, L., González-Santamarta, M. Á., Guerrero-Higueras, Á. M., Rodríguez-Lera, F. J., & Matellán Olivera, V. (arXiv), Enhancing Trust in Autonomous Agents: An Architecture for Accountability and Explainability through Blockchain and Large Language Models, 2024-03, https://arxiv.org/abs/2403.09567, 접근일 2026-10-09 (원문 미열람)
[^ref-1111]: 엠에스투데이, 선박·위성·로봇까지 해킹 표적…정부, '피지컬 AI' 산업 보안 기준 제시, 2026-03-06, https://www.mstoday.co.kr/news/articleView.html?idxno=100755, 접근일 2026-10-09 (원문 미열람)
[^ref-1112]: Nagaraja, N., Bagari, A., & Bahsi, H. (arXiv), When Prompts Control Robots: Prompt Injection Attacks in Multi-Agent Robotic Systems, 2026-08, https://arxiv.org/abs/2608.00747, 접근일 2026-10-09 (원문 미열람)
[^ref-1113]: Zhang, W., Kong, X., Dewitt, C., Braunl, T., & Hong, J. B. (arXiv), A Study on Prompt Injection Attack Against LLM-Integrated Mobile Robotic Systems, 2024-08, https://arxiv.org/abs/2408.03515, 접근일 2026-10-09 (원문 미열람)
[^ref-1114]: Quarta, D., Pogliani, M., Polino, M., Maggi, F., Zanchettin, A. M., & Zanero, S. (IEEE S&P 2017), An Experimental Security Analysis of an Industrial Robot Controller, 2017, https://files01.core.ac.uk/download/pdf/84891817.pdf, 접근일 2026-10-09 (원문 미열람)
[^ref-1116]: IBF Solutions, New standards for industrial robots EN ISO 10218-1 and -2, 2026-09-18, https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2, 접근일 2026-10-09 (원문 미열람)
[^ref-1136]: 정보통신신문, "자율주행차·로봇 카메라 촬영 시 외부에 표시해야", 2024-10-14, https://www.koit.co.kr/news/articleView.html?idxno=125844, 접근일 2026-10-09 (원문 미열람)
[^ref-1138]: 개인정보보호위원회 (대한민국 정책브리핑), 자율주행차·이동형 로봇 개발에 '영상데이터' 원본 활용 허용, 2023-11-15, https://www.korea.kr/news/policyNewsView.do?newsId=148922669, 접근일 2026-10-09 (원문 미열람)
[^ref-1141]: 아시아경제, "로봇청소기 개인정보 관리 대체로 안전…미흡 사례 ... (제목 일부만 확인), 2026-09-14, https://view.asiae.co.kr/article/2026091410054053414, 접근일 2026-10-09 (원문 미열람)
[^ref-1145]: Xu, Y., & Ayday, E. (arXiv), Seeing Less Is Not Seeing Safely: Privacy Leakage from Task-Scoped Robot Perception Exports, 2026-09-02, https://arxiv.org/abs/2609.03055, 접근일 2026-10-09 (원문 미열람)
[^ref-1146]: Sarfraz, B. M., Saplacan Lindblom, D., Baselizadeh, A., & Torresen, J. (HRI Companion '26), The Privacy-Preserving Capabilities of a Service Robot in a Scenario-Based Healthcare Setting, 2026-03-16, https://doi.org/10.1145/3776734.3794481, 접근일 2026-10-09 (원문 미열람)
[^ref-1173]: ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan, REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction, 2022-01-11, https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst, 접근일 2026-10-09 (원문 미열람)
[^ref-1299]: ST Engineering Aethon (Newswire 게재 보도자료), ST Engineering Aethon Launches Zena RX, Redefining Secure Delivery of Medications, Specimens and Sensitive Goods in Hospitals, 2024-04-29, https://www.newswire.com/news/st-engineering-aethon-launches-zena-rx-redefining-secure-delivery-of-22310264, 접근일 2026-10-09 (원문 미열람)
[^ref-1301]: 경향신문 (곽희양), 내년 2월 자율주행 로봇이 아파트 내에서 배달 음식 나른다, 2020-07-03, https://www.khan.co.kr/article/202007031130001, 접근일 2026-10-09 (원문 미열람)
[^ref-1242]: Carr, C., Wang, S., Wang, P., & Han, L. (arXiv), Attacking Digital Twins of Robotic Systems to Compromise Security and Safety, 2022-11-17, https://arxiv.org/abs/2211.09507, 접근일 2026-10-09 (원문 미열람)
[^ref-1263]: 메트로신문, AI·커머스·플랫폼 분야 규제 특례 확대…사업화 지원, 2026-05-06, https://www.metroseoul.co.kr/article/20260506500296, 접근일 2026-10-09 (원문 미열람)
[^ref-1228]: European Commission (Shaping Europe's digital future), CRA reporting, 미확인(페이지 최종 갱신 2026-09-11), https://digital-strategy.ec.europa.eu/en/policies/cra-reporting, 접근일 2026-10-09
[^ref-1368]: The Register, Researcher who found McDonald's free-food hack turns her attention to Chinese restaurant robots, 2025-08-29, https://www.theregister.com/2025/08/29/pudu_robots_hackable/, 접근일 2026-10-09
[^ref-1369]: Hackmag, Researcher finds a way to hack Chinese Pudu service robots, 2025-09-05, https://hackmag.com/news/pudu-bugs, 접근일 2026-10-09
[^ref-1370]: Silicon UK, France Fines Amazon 32m Euros Over 'Excessive' Worker Surveillance, 2024-01-23, https://www.silicon.co.uk/e-marketing/ecommerce/cnil-france-amazon-fine-546858, 접근일 2026-10-09
[^ref-1371]: CNIL (Commission nationale de l'informatique et des libertés), Employee monitoring: CNIL fined AMAZON FRANCE LOGISTIQUE €32 million, 2024-01-23, https://cnil.fr/en/employee-monitoring-cnil-fined-amazon-france-logistique-eu32-million, 접근일 2026-10-09 (원문 미열람)
[^ref-1372]: 바이라인네트워크 (곽중희), 개인정보위 "로봇청소기 5개 브랜드, 특별한 침해 위험 없어", 2026-09-14, https://byline.network/2026/09/14-623/, 접근일 2026-10-09
[^ref-1373]: 바이라인네트워크, 과기정통부, 선박·우주·로봇 보안 매뉴얼 공개, 2026-03-06, https://byline.network/2026/03/6-340/, 접근일 2026-10-09
[^ref-1374]: Shen, L., Geng, S., Zheng, Y., & Lu, C. X. (arXiv), Seeing is Not Believing: Breaking the Physical-to-Digital Trust Boundary in Robotics, 2026-09-08, https://arxiv.org/abs/2609.08280, 접근일 2026-10-09
[^ref-1375]: KUKA (Robotics Tomorrow 게재 보도자료), KUKA is First to Achieve Security Level 2 Certification for Robotics Industry, 2026-09-02, https://www.roboticstomorrow.com/news/2026/09/02/kuka-is-first-to-achieve-security-level-2-certification-for-robotics-industry/27035/, 접근일 2026-10-09
[^ref-1376]: European Commission (Shaping Europe's digital future), Data Act explained, 미확인(페이지 최종 갱신 2025-12-15), https://digital-strategy.ec.europa.eu/en/policies/data-act-explained, 접근일 2026-10-09
[^ref-1260]: DIN Media, DIN EN ISO 13482 - 2024-10 (Draft standard) Robotik - Sicherheitsanforderungen für Serviceroboter (ISO/DIS 13482:2024), 2024-10, https://www.dinmedia.de/de/norm-entwurf/din-en-iso-13482/384079303, 접근일 2026-10-09 (원문 미열람)
```

### docs/categories/security-and-privacy/index.md

```markdown
---
title: "N. 보안·개인정보"
type: category
status: seed
created: 2026-09-28
updated: 2026-09-28
version: 1
---

[홈](../../index.md) › N. 보안·개인정보

# N. 보안·개인정보

## 핵심 질문

누가 어떤 로봇에 무엇을 시킬 수 있는지 통제하고, 데이터와 사람의 정보를 어떻게 지킬 것인가? [분류원문]

## 개요

인증·권한·격리, 통신 보호, 위협 관리와 감사 기록, 문서·대화 입력 보안, 개인정보·영상 데이터 보호. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **51. 인증·권한·격리** | 장비·사용자 인증, 명령 권한, 원격 접속 계정, 고객·현장 격리 | 외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가? | [51. 인증·권한·격리](authentication-authorization-and-isolation.md) | published |
| **52. 통신 보호·위협 관리·감사** | 통신 보호, 위협 모델·취약점, 문서·대화 입력 보안, 감사 기록 | 통신·문서·대화를 통한 공격이 로봇 동작으로 이어지지 않게 하려면? | [52. 통신 보호·위협 관리·감사](communication-protection-threat-management-and-audit.md) | published |
| **53. 개인정보·영상 데이터** | 영상·작업자·거주자 데이터 보호, 최소 수집·익명화 | 로봇이 찍은 영상과 사람의 위치 정보를 어디까지 모으고 어떻게 지킬 것인가? | [53. 개인정보·영상 데이터](privacy-and-video-data.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

ROS 2도 인증·암호화·접근권한과 보안 위협 모델을 별도로 다룬다. 기능 연동과 보안 연동은 함께 설계해야 하는 영역이다. [9][10] [분류원문]

## 다른 대분류와의 연결

아직 작성되지 않음(에이전트가 채운다).

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 45건이다(논문 13건 · 기사·보고서 11건 · 업체 발표 0건 · 표준·오픈소스·기관 자료 21건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-1145](../../references/ref-1145.md) — Xu, Y., & Ayday, E. (arXiv), Seeing Less Is Not Seeing Safely: Privacy Leakage from Task-Scoped Robot Perception Exports (발행 2026-09-02)
- [ref-1112](../../references/ref-1112.md) — Nagaraja, N., Bagari, A., & Bahsi, H. (arXiv), When Prompts Control Robots: Prompt Injection Attacks in Multi-Agent Robotic Systems (발행 2026-08)
- [ref-1144](../../references/ref-1144.md) — Huang, X., Pan, S., Reinhardt, D., & Bennewitz, M. (arXiv), Designing Privacy-Preserving Visual Perception for Robot Navigation Based on User Privacy Preferences (발행 2026-04-07)
- [ref-1146](../../references/ref-1146.md) — Sarfraz, B. M., Saplacan Lindblom, D., Baselizadeh, A., & Torresen, J. (HRI Companion '26), The Privacy-Preserving Capabilities of a Service Robot in a Scenario-Based Healthcare Setting (발행 2026-03-16)
- [ref-585](../../references/ref-585.md) — Jaatun 외(Journal of Cybersecurity and Privacy 6(2), 52), Security Aspects of Zones and Conduits in IEC 62443 (발행 2026)
- [ref-1108](../../references/ref-1108.md) — Mayoral-Vilches, V. (Alias Robotics, arXiv), The Cybersecurity of a Humanoid Robot (발행 2025-09-17)
- [ref-1143](../../references/ref-1143.md) — Choi, M. 외 (arXiv), Real-Time Privacy Preservation for Robot Visual Perception (발행 2025-05-08)
- [ref-700](../../references/ref-700.md) — Ravichandran, Z., Robey, A., Kumar, V., Pappas, G. J., & Hassani, H.(IEEE RA-L 2026 채택 표기), Safety Guardrails for LLM-Enabled Robots (발행 2025-03)
- [ref-857](../../references/ref-857.md) — Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J., Jailbreaking LLM-Controlled Robots (발행 2024-11-09)
- [ref-1113](../../references/ref-1113.md) — Zhang, W., Kong, X., Dewitt, C., Braunl, T., & Hong, J. B. (arXiv), A Study on Prompt Injection Attack Against LLM-Integrated Mobile Robotic Systems (발행 2024-08)
- 그 밖에 3건

**기사·보고서**

- [ref-1141](../../references/ref-1141.md) — 아시아경제, "로봇청소기 개인정보 관리 대체로 안전…미흡 사례 ... (제목 일부만 확인) (발행 2026-09-14)
- [ref-1109](../../references/ref-1109.md) — IES (Integrated Equipment Services), Machinery Regulation Guide (발행 2026-08-27)
- [ref-1111](../../references/ref-1111.md) — 엠에스투데이, 선박·위성·로봇까지 해킹 표적…정부, ‘피지컬 AI’ 산업 보안 기준 제시 (발행 2026-03-06)
- [ref-969](../../references/ref-969.md) — 바이라인네트워크, '로봇청소기' 다수 제품 보안 취약…대응방안은? (발행 2025-10-31)
- [ref-1140](../../references/ref-1140.md) — 경향신문, 로봇청소기가 우리집 사진 찍어 외부 유출?…6종 ... (제목 일부만 확인) (발행 2025-09-02)
- [ref-1136](../../references/ref-1136.md) — 정보통신신문, "자율주행차·로봇 카메라 촬영 시 외부에 표시해야" (발행 2024-10-14)
- [ref-1139](../../references/ref-1139.md) — 법무법인(유) 세종, 개인정보보호위원회, 비정형데이터 가명처리 관련 가명정보 처리 가이드라인 개정 (뉴스레터) (발행 2024-02-08)
- [ref-968](../../references/ref-968.md) — MIT Technology Review (Eileen Guo), A Roomba recorded a woman on the toilet. How did screenshots end up on Facebook? (발행 2022-12-19)
- [ref-588](../../references/ref-588.md) — 김·장 법률사무소, '이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서' 관련 인사이트 (발행 미확인)
- [ref-471](../../references/ref-471.md) — A3(Association for Advancing Automation), Updated ISO 10218 \| Answers to Frequently Asked Questions (FAQs) (발행 미확인)
- 그 밖에 1건

**업체 발표**

- 아직 없음

**표준·오픈소스·기관 자료**

- [ref-1135](../../references/ref-1135.md) — 개인정보보호위원회, [현재 안내서] 이동형 영상정보처리기기를 위한 개인영상정보 보호ㆍ활용 안내서(2024.9.) (발행 2024-10-14)
- [ref-1138](../../references/ref-1138.md) — 개인정보보호위원회 (대한민국 정책브리핑), 자율주행차·이동형 로봇 개발에 ‘영상데이터’ 원본 활용 허용 (발행 2023-11-15)
- [ref-582](../../references/ref-582.md) — NIST, NIST SP 800-82 Rev. 3, Guide to Operational Technology (OT) Security (발행 2023-09)
- [ref-555](../../references/ref-555.md) — European Union (EUR-Lex), Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery (발행 2023-06)
- [ref-1107](../../references/ref-1107.md) — CISA (미국 사이버보안·기반시설보안청), Aethon TUG Home Base Server (ICSA-22-102-05) (발행 2022-04-12)
- [ref-580](../../references/ref-580.md) — Open Robotics (ROS 2 Design), ROS 2 Security Enclaves (발행 2020-05)
- [ref-1147](../../references/ref-1147.md) — European Data Protection Board (EDPB), Guidelines 3/2019 on processing of personal data through video devices (발행 2020-01)
- [ref-579](../../references/ref-579.md) — Open Robotics (ROS 2 Design), ROS 2 Access Control Policies (발행 2019-08)
- [ref-584](../../references/ref-584.md) — CSA / IEC (ANSI Webstore), CAN/CSA IEC 62443-3-3-2017 - Industrial communication networks - Network and system security - Part 3-3: System security requirements and security levels (Adopted IEC 62443-3-3:2013, first edition, 2013-08) (발행 2013-08)
- [ref-591](../../references/ref-591.md) — European Commission (Shaping Europe's digital future), The Cyber Resilience Act - Summary of the legislative text (발행 미확인)
- 그 밖에 11건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-30 · 갱신 · [53. 개인정보·영상 데이터](privacy-and-video-data.md) — seed → draft: 3~11절 첫 작성(제25조의2·이동형 안내서, 목적별 이용·가명처리, 가림·저해상도·출력 필드 기술, 가정·병원·실외 사례, 책임 경계, 연결 16개 영역, 열린 질문 11건), 13절 각주, 1차 수정 15건·2차 수정 4건 반영 (실행 2026-09-30-16)
- 2026-09-30 · 생성 · [53. 개인정보·영상 데이터 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area53-s6.md) — 자동 분리: 53. 개인정보·영상 데이터 의 "6. 대표 접근법과 기술" 절(1,883자)을 옮겼다 (실행 2026-09-30-16)
- 2026-09-30 · 생성 · [53. 개인정보·영상 데이터 — 열린 질문](../../topics/2026/2026-09-30-area53-s11.md) — 자동 분리: 53. 개인정보·영상 데이터 의 "11. 열린 질문" 절을 옮겼다. 2차 수정: 기존 질문 7건을 등록 문장 그대로 옮기고 부분 근거 메모 2건에 [추정]·각주, EDPB 풀어쓰기 (실행 2026-09-30-16)
- 2026-09-30 · 생성 · [53. 개인정보·영상 데이터 — 대표 연구와 자료](../../topics/2026/2026-09-30-area53-s8.md) — 자동 분리: 53. 개인정보·영상 데이터 의 "8. 대표 연구와 자료" 절을 옮겼다. 2차 수정: Xu·Ayday 항목의 플랫폼 필드 설계 연결 문장을 [추정]으로 분리 (실행 2026-09-30-16)
- 2026-09-30 · 생성 · [53. 개인정보·영상 데이터 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area53-s4.md) — 자동 분리: 53. 개인정보·영상 데이터 의 "4. 핵심 개념과 용어" 절(1,008자)을 옮겼다 (실행 2026-09-30-16)
<!-- auto:category-recent:end -->

## 참고 자료

원문의 [9]는 참고문헌 [ref-009](../../references/ref-009.md)에 해당한다.[^ref-009] 원문의 [10]은 참고문헌 [ref-010](../../references/ref-010.md)에 해당한다.[^ref-010]

[^ref-009]: ROS 2 Design, ROS 2 DDS-Security Integration, 미확인, https://design.ros2.org/articles/ros2_dds_security.html, 접근일 2026-09-28
[^ref-010]: ROS 2 Design, ROS 2 Robotic Systems Threat Model, 미확인, https://design.ros2.org/articles/ros2_threat_model.html, 접근일 2026-09-28
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 45건 / 전체 1273건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-009 | ROS 2 Design | ROS 2 DDS-Security Integration | 미확인 | https://design.ros2.org/articles/ros2_dds_security.html | 2026-09-25 | 예 |
| ref-010 | ROS 2 Design | ROS 2 Robotic Systems Threat Model | 미확인 | https://design.ros2.org/articles/ros2_threat_model.html | 2026-09-25 | 예 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 2026-09-25 | 예 |
| ref-405 | Open Robotics | Security - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/security.html | 2026-09-25 | 예 |
| ref-471 | A3(Association for Advancing Automation) | Updated ISO 10218 | Answers to Frequently Asked Questions (FAQs) | 미확인 | https://www.automate.org/robotics/blogs/updated-iso-10218-faq | 2026-09-25 | 아니오 |
| ref-555 | European Union (EUR-Lex) | Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery | 2023-06 | https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng | 2026-09-25 | 아니오 |
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
| ref-700 | Ravichandran, Z., Robey, A., Kumar, V., Pappas, G. J., & Hassani, H.(IEEE RA-L 2026 채택 표기) | Safety Guardrails for LLM-Enabled Robots | 2025-03 | https://arxiv.org/abs/2503.07885 | 2026-09-25 | 아니오 |
| ref-857 | Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J. | Jailbreaking LLM-Controlled Robots | 2024-11-09 | https://arxiv.org/abs/2410.13691 | 2026-09-29 | 예 |
| ref-968 | MIT Technology Review (Eileen Guo) | A Roomba recorded a woman on the toilet. How did screenshots end up on Facebook? | 2022-12-19 | https://www.technologyreview.com/2022/12/19/1065306/roomba-irobot-robot-vacuums-artificial-intelligence-training-data-privacy/ | 2026-09-29 | 예 |
| ref-969 | 바이라인네트워크 | '로봇청소기' 다수 제품 보안 취약…대응방안은? | 2025-10-31 | https://byline.network/2025/10/31-283/ | 2026-09-29 | 예 |
| ref-1105 | IEC (SyC Smart Energy) | IEC 62443 | 미확인 | https://syc-se.iec.ch/deliveries/cybersecurity-guidelines/security-standards-and-best-practices/iec-62443/ | 2026-09-30 | 예 |
| ref-1106 | OWASP GenAI Security Project | LLM01:2025 Prompt Injection | 미확인 | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ | 2026-09-30 | 예 |
| ref-1107 | CISA (미국 사이버보안·기반시설보안청) | Aethon TUG Home Base Server (ICSA-22-102-05) | 2022-04-12 | https://www.cisa.gov/news-events/ics-advisories/icsa-22-102-05 | 2026-09-30 | 예 |
| ref-1108 | Mayoral-Vilches, V. (Alias Robotics, arXiv) | The Cybersecurity of a Humanoid Robot | 2025-09-17 | https://arxiv.org/abs/2509.14096 | 2026-09-30 | 예 |
| ref-1109 | IES (Integrated Equipment Services) | Machinery Regulation Guide | 2026-08-27 | https://www.ies.co.uk/reference-library/machinery-regulation-guide | 2026-09-30 | 예 |
| ref-1110 | Fernández-Becerra, L., González-Santamarta, M. Á., Guerrero-Higueras, Á. M., Rodríguez-Lera, F. J., & Matellán Olivera, V. (arXiv) | Enhancing Trust in Autonomous Agents: An Architecture for Accountability and Explainability through Blockchain and Large Language Models | 2024-03 | https://arxiv.org/abs/2403.09567 | 2026-09-30 | 예 |
| ref-1111 | 엠에스투데이 | 선박·위성·로봇까지 해킹 표적…정부, ‘피지컬 AI’ 산업 보안 기준 제시 | 2026-03-06 | https://www.mstoday.co.kr/news/articleView.html?idxno=100755 | 2026-09-30 | 예 |
| ref-1112 | Nagaraja, N., Bagari, A., & Bahsi, H. (arXiv) | When Prompts Control Robots: Prompt Injection Attacks in Multi-Agent Robotic Systems | 2026-08 | https://arxiv.org/abs/2608.00747 | 2026-09-30 | 예 |
| ref-1113 | Zhang, W., Kong, X., Dewitt, C., Braunl, T., & Hong, J. B. (arXiv) | A Study on Prompt Injection Attack Against LLM-Integrated Mobile Robotic Systems | 2024-08 | https://arxiv.org/abs/2408.03515 | 2026-09-30 | 예 |
| ref-1114 | Quarta, D., Pogliani, M., Polino, M., Maggi, F., Zanchettin, A. M., & Zanero, S. (IEEE S&P 2017) | An Experimental Security Analysis of an Industrial Robot Controller | 2017 | https://files01.core.ac.uk/download/pdf/84891817.pdf | 2026-09-30 | 아니오 |
| ref-1135 | 개인정보보호위원회 | [현재 안내서] 이동형 영상정보처리기기를 위한 개인영상정보 보호ㆍ활용 안내서(2024.9.) | 2024-10-14 | https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS217&mCode=G010030000&nttId=10679 | 2026-09-30 | 예 |
| ref-1136 | 정보통신신문 | "자율주행차·로봇 카메라 촬영 시 외부에 표시해야" | 2024-10-14 | https://www.koit.co.kr/news/articleView.html?idxno=125844 | 2026-09-30 | 예 |
| ref-1137 | 개인정보보호위원회 (개인정보 포털) | 개인정보 포털 — 이동형 영상정보처리기기 제도 및 신청방법 안내 | 미확인 | https://www.privacy.go.kr/front/contents/cntntsView.do?contsNo=286 | 2026-09-30 | 예 |
| ref-1138 | 개인정보보호위원회 (대한민국 정책브리핑) | 자율주행차·이동형 로봇 개발에 ‘영상데이터’ 원본 활용 허용 | 2023-11-15 | https://www.korea.kr/news/policyNewsView.do?newsId=148922669 | 2026-09-30 | 예 |
| ref-1139 | 법무법인(유) 세종 | 개인정보보호위원회, 비정형데이터 가명처리 관련 가명정보 처리 가이드라인 개정 (뉴스레터) | 2024-02-08 | https://www.shinkim.com/kor/media/newsletter/2342 | 2026-09-30 | 예 |
| ref-1140 | 경향신문 | 로봇청소기가 우리집 사진 찍어 외부 유출?…6종 ... (제목 일부만 확인) | 2025-09-02 | https://www.khan.co.kr/article/202509021447001 | 2026-09-30 | 예 |
| ref-1141 | 아시아경제 | "로봇청소기 개인정보 관리 대체로 안전…미흡 사례 ... (제목 일부만 확인) | 2026-09-14 | https://view.asiae.co.kr/article/2026091410054053414 | 2026-09-30 | 예 |
| ref-1142 | Raina, N., Somasundaram, G., Zheng, K. 외 (Meta Reality Labs, arXiv) | EgoBlur: Responsible Innovation in Aria | 2023-08-24 | https://arxiv.org/abs/2308.13093 | 2026-09-30 | 예 |
| ref-1143 | Choi, M. 외 (arXiv) | Real-Time Privacy Preservation for Robot Visual Perception | 2025-05-08 | https://arxiv.org/abs/2505.05519 | 2026-09-30 | 예 |
| ref-1144 | Huang, X., Pan, S., Reinhardt, D., & Bennewitz, M. (arXiv) | Designing Privacy-Preserving Visual Perception for Robot Navigation Based on User Privacy Preferences | 2026-04-07 | https://arxiv.org/abs/2604.06382 | 2026-09-30 | 예 |
| ref-1145 | Xu, Y., & Ayday, E. (arXiv) | Seeing Less Is Not Seeing Safely: Privacy Leakage from Task-Scoped Robot Perception Exports | 2026-09-02 | https://arxiv.org/abs/2609.03055 | 2026-09-30 | 예 |
| ref-1146 | Sarfraz, B. M., Saplacan Lindblom, D., Baselizadeh, A., & Torresen, J. (HRI Companion '26) | The Privacy-Preserving Capabilities of a Service Robot in a Scenario-Based Healthcare Setting | 2026-03-16 | https://doi.org/10.1145/3776734.3794481 | 2026-09-30 | 아니오 |
| ref-1147 | European Data Protection Board (EDPB) | Guidelines 3/2019 on processing of personal data through video devices | 2020-01 | https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-32019-processing-personal-data-through-video_en | 2026-09-30 | 예 |
```

### docs/glossary/index.md (요약: 용어 362개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- 3d-scene-graph: 3차원 장면 그래프 (3D Scene Graph)
- a-b-update: A/B 업데이트 (A/B Update (Dual Partition Update with Rollback))
- aas-registry-and-discovery: 자산관리셸 레지스트리·디스커버리 (AAS Registry / Discovery)
- ablation-study: 절제 실험 (Ablation Study)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- agentic-ai: 에이전틱 AI (Agentic AI)
- aggregation-event: 집계 이벤트 (AggregationEvent)
- agv-technical-data-submodel: AGV 기술 데이터 서브모델 (Technical Data for AGV in Intralogistics (IDTA 02047))
- alarm-management: 경보 관리 (Alarm Management (ANSI/ISA 18.2))
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
- curb-cut: 연석 경사로 (Curb Cut (Curb Ramp))
- cyber-resilience-act: 사이버복원력법 (Cyber Resilience Act (CRA))
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
- opentelemetry-genai-semantic-conventions: 생성형 AI 의미 규약 (OpenTelemetry GenAI Semantic Conventions)
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

### docs/open-questions.md (요약: 대상 영역 [51, 52, 53] 에 걸린 34건 / 전체 317건)

```markdown
- oq-043 [열림] 로봇 관제가 출입통제·건물 자동화 시스템(BACnet 등)을 통해 보안문을 여닫는 공개 설계나 국내 사례가 있고, 권한 확인은 누가 하는가? (영역 22, 51)
- oq-056 [열림] 로봇 관제·플릿 어댑터·승강기·문 어댑터에 SROS 2 인클레이브와 권한 파일을 어떤 단위로 나눠 설비 명령 권한을 제한하는지 공개한 구성이나 사례가 있는가? (영역 22, 51)
- oq-082 [열림] 로봇·제조사 관제가 보고하는 위치·배터리·입찰 비용이 오염되거나 위조되었을 때 ROP 는 배정 전에 이를 어떻게 검증하고, 의심 로봇을 배정 후보에서 뺄 기준은 무엇인가? (영역 25, 38, 51)
- oq-099 [열림] 물류센터 내부처럼 공개되지 않은 작업장에서 카메라를 단 로봇이 작업자를 촬영할 때 개인정보 보호법 제25조의2와 근로자 감시 설비 협의 가운데 무엇이 적용되는지 공식 해석이 있는가? (영역 31, 51)
- oq-100 [열림] 외부 유지보수 계정의 권한을 로봇·명령 단위로 나눈 매트릭스(예: 진단은 허용, 이동은 불허)를 공개한 로봇 관제·ROP 구성이나 표준이 있는가? (영역 20, 51)
- oq-101 [열림] 여러 화주가 로봇 플릿을 공유하는 창고에서 고객별 작업·데이터 격리를 오케스트레이션 수준에서 규정한 표준이나 공개 설계가 있는가? (영역 21, 51)
- oq-102 [열림] ISO 10218-1:2025 의 사이버보안 요구는 어느 조항에서 무엇(접근 제한·원격 접속·로그 등)을 요구하며 로봇 관제 연동에 어떤 조건을 주는가? (영역 48, 51)
- oq-103 [열림] EU 기계 규정 부속서 III 1.1.9 의 적용일이 사이버 복원력법(2027-12-11)에 맞춰 연기되는지 확정됐는가? (영역 48, 51)
- oq-113 [열림] ROP 가 VDA 5050 updateCertificate 같은 보안 명령으로 제조사 로봇의 인증서를 교체할 때, 교체 시점·대상 승인과 실패 시 되돌림 책임은 ROP 사업자·제조사·현장 IT 조직 중 누가 지는가? (영역 20, 51, 57)
- oq-121 [열림] 로봇 관제 챗봇의 채팅 지시 기록에 작업자 식별 정보가 담길 때 그 시스템이 개인정보의 안전성 확보조치 기준의 개인정보처리시스템에 해당해 접근권한 기록·접속기록 보관 기준을 적용받는지 공식 해석이 있는가? (관련: oq-099) (영역 31, 51)
- oq-143 [열림] ROP 의 로봇 대화 기능이 국내 인공지능 기본법의 고영향 인공지능이나 EU AI Act 의 고위험 AI 시스템에 해당하는지, 해당한다면 대화 기록 자동 로그의 항목과 보존 기간을 어떻게 정해야 하는가? (영역 13, 59, 53)
- oq-144 [열림] 로봇 대화 지시에 특화된 프롬프트 주입·탈옥 방어(도구 설명 신뢰 경계, 실행 전 물리 제약 검사, 다중 모델 감독)의 효과를 잰 공개 벤치마크나 현장 시험 결과가 있는가? (영역 13, 52, 48)
- oq-171 [열림] 개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한)의 촬영 사실 표시·촬영 거부 규정이 병원 이송 로봇의 카메라·센서 촬영에 어떻게 적용되며, 환자·방문객 영상을 관제 계층이 어디까지 저장·전송할 수 있는지 법령 원문과 해석 사례로 확인할 수 있는가(이번 조사는 법령 원문을 열지 못했다)? (영역 63, 53)
- oq-181 [열림] 세대 안에서 거주자가 쓰는 가사 로봇·로봇청소기의 영상 수집에는 개인정보 보호법 제25조의2(이동형 영상정보처리기기)가 적용되는가, 아니면 동의 기반 처리 조항만 적용되는가, 그리고 이에 대한 개인정보보호위원회 해석이나 가이드라인이 있는가? (영역 65, 53)
- oq-185 [열림] 소유자가 원격 조작자를 예약해 가정 로봇을 안내하게 하는 방식(1X NEO 등)에서 원격 조작자의 영상 접근·사고 책임을 다루는 국내외 규제·인증 기준이 있는가? (영역 65, 53, 58)
- oq-211 [열림] 로봇 플랫폼이 수집하는 텔레메트리·주행 기록·영상의 보존 기간을 정한 국내 기준이나 운영 사례가 개인정보 접속기록 규정 밖에도 있는가? (영역 43, 53)
- oq-214 [열림] 로봇 플랫폼에 적용될 수 있는 현행 「개인정보의 안전성 확보조치 기준」(2023-6호 이후 개정판)의 접속기록 보관 기간·점검 주기 조항이 2023-6호와 같은가? (영역 43, 53)
- oq-228 [열림] 플랫폼이 시설 CCTV 영상을 로봇 운영용 장면 인식에 쓸 때 국내 개인정보 보호 법령의 고정형 영상정보처리기기 규정상 목적 외 이용이나 안내 의무가 문제 되는가? (영역 45, 53)
- oq-246 [열림] 여러 제조사 플릿 관리 서버와 VDA 5050 브로커·Open-RMF 어댑터를 잇는 ROP 에서 브로커·API 의 상호 인증과 TLS 설정의 최소 요구를 정한 공개 보안 프로파일이 있는가? (영역 52, 20, 21)
- oq-247 [열림] LLM 에이전트 여러 개가 로봇을 나눠 맡을 때 한 에이전트에 주입된 지시가 다른 에이전트로 퍼지지 않게 에이전트 간 메시지에 신뢰 경계를 두는 방어의 효과를 잰 연구가 있는가? (영역 52, 13, 12)
- oq-248 [열림] 명령·승인 감사 기록을 해시 체인·블록체인으로 변조 탐지 가능하게 남길 때 수백 대 로봇 규모의 명령 빈도에서 지연·저장 비용을 측정한 자료가 있는가? (영역 52, 37)
- oq-249 [열림] EU 기계류 규정의 개입 증거 기록·안전 소프트웨어 추적 로그 요구가 개별 기계 밖에서 여러 로봇을 지시하는 오케스트레이션 플랫폼에도 미치는가, 미친다면 기록 책임은 누구에게 있는가? (영역 52, 59, 58)
- oq-250 [열림] KISA 로봇 보안모델(고도화)과 사이버보안 요구사항 해설서는 로봇 통신 암호화·감사 기록·원격 업데이트에 어떤 요구 항목을 두며 다중 로봇 관제 플랫폼을 대상에 포함하는가? (영역 52, 59)
- oq-259 [열림] 여러 제조사 로봇의 영상과 위치 정보를 모아 관제하는 플랫폼 사업자는 개인정보 보호법상 이동형 영상정보처리기기 운영자인가, 현장 운영 사업자의 수탁자인가, 그리고 촬영 표시·거부 의사 처리 의무는 누구에게 있는가? (영역 53, 58)
- oq-260 [열림] 로봇이 플랫폼·클라우드·로그로 내보내는 인지 출력(객체 목록·의미 지도·궤적)의 재식별 위험을 측정하는 공개 평가 기준이나 벤치마크가 있는가? (영역 53, 54)
- oq-261 [열림] 피촬영자가 한 로봇에 밝힌 촬영 거부 의사를 같은 현장의 다른 로봇과 플랫폼 기록에 공통으로 반영하는 방법이나 운영 사례가 있는가? (영역 53, 19)
- oq-262 [열림] 유럽데이터보호이사회(European Data Protection Board, EDPB) 영상 장치 지침 3/2019 를 이동 로봇 카메라에 적용한 유럽 감독기관의 결정이나 해석 사례가 있으며, 보존 기간 권고는 무엇인가? (영역 53, 59)
- oq-272 [열림] 여러 제조사 로봇과 설비 센서가 각자 감지한 사람 위치를 하나의 사람 흐름 모델로 합칠 때 좌표·시각·신뢰도·익명화 형식을 정한 공개 규격이나 구현이 있는가? (영역 19, 18, 53)
- oq-285 [열림] 오케스트레이션 플랫폼이 로봇 작업과 연결해 개별 작업자의 처리량·위치를 기록하는 기능이 근로자참여법 제20조의 근로자 감시 설비나 독일 사업장조직법 제87조의 감시 장치에 해당해 도입 전 노사협의·공동결정 대상이 되는가? (영역 60, 53, 59)
- oq-291 [열림] 로봇 오케스트레이션 플랫폼이 EU 사이버복원력법의 디지털 요소 제품 제조자에 해당하는가, 해당하면 로봇 제조사와 플랫폼 사업자 사이에 취약점 보고 의무를 어떻게 나누는가? (영역 59, 52, 57)
- oq-293 [열림] 병원 운반 로봇의 생체 인식·PIN 수령 확인처럼 수령인 인증 결과를 작업 완료·인계 이벤트로 ROP 와 병원 정보 시스템에 남기는 공개 인터페이스나 표준 필드가 있는가? (영역 17, 51, 63)
- oq-306 [열림] 실시간 상태를 가상 모델에 반영하고 시뮬레이션 결과를 실제 계획·설정에 되돌리는 디지털 트윈 동기화 경로에 대해 로봇 플릿 플랫폼이 적용한 접근통제·무결성 확인 사례가 있는가? (영역 36, 52, 51)
- oq-308 [열림] 운영 기록으로 상황을 재현하기 전에 영상 기록을 익명화하면 재현 충실도가 얼마나 떨어지며, 국내 개인정보 처리 기준에서 재현용 기록을 어떻게 보관·공유해야 하는가? (영역 53, 36)
- oq-317 [열림] 실외 배달로봇에 승인된 원본 영상 AI 학습 실증특례가 병원·물류창고 같은 실내 현장의 로봇 카메라 영상에도 적용될 수 있는가, 적용 조건은 무엇인가? (영역 53, 45)
```

### runs/2026-10-09-10/verification2.json

```json
{
  "run_id": "2026-10-09-10",
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
      "본문이 새로 연결한 oq-293(E. 사물·사람·실시간 상태 항목)과 oq-306·oq-308(I. 설계·시뮬레이션 항목)은 기존 열린 질문 목록에 있는 항목을 가리키는 연결이며, 새 주장이 아니다",
      "새 열린 질문 4건 가운데 3건은 1차 지시대로 '(관련: oq-082·oq-259·oq-285)'를 붙여 기존 질문과의 관계를 밝혔다"
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
    "다른 대분류와의 연결 절 L. AI·학습 기술의 '45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영 ↔ 53. 개인정보·영상 데이터' 항목: '학습 데이터로 쓰이는 대상은 장면 인식 모델이며,'를 삭제하고 '현장 유형으로는 Q. 현장 유형별 적용의 66. 실외 사례다'만 남긴다 — 브리프 f40 과 근거 ref-1138·ref-1263 는 원본 영상을 자율주행 배달로봇의 AI 학습에 쓴다고만 하고, 학습하는 모델이 장면 인식 모델이라고 밝히지 않는다(브리프 밖 주장).",
    "다른 대분류와의 연결 절 C. 채팅 기반 구성·운영 소제목 아래 안내 문장의 '분류 원문 C 주석은'을 '분류 원문의 C. 채팅 기반 구성·운영 주석은'으로 고친다 — 대분류를 문자만으로 부르지 않는다(공통 규칙 6절 항목 호칭).",
    "다른 대분류와의 연결 절에서 다음 약어를 처음 나올 때 풀어 쓴다: OWASP(Open Worldwide Application Security Project), CISA(Cybersecurity and Infrastructure Security Agency, 이미 쓴 한국어 이름에 영문 병기), CVE(Common Vulnerabilities and Exposures), CVSS(Common Vulnerability Scoring System), SROS 2(Secure ROS 2), DDS(Data Distribution Service) — 약어는 첫 등장 시 풀어 쓴다는 문체 규칙. 문장 내용과 태그·각주는 바꾸지 않는다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인 / 2차 수정 후 재검증. 확인 56건, 미확인 0건, 교차 확인은 2건이다(f42 ISO 10218 2025년판 사이버보안 요구, f52 CNIL의 Amazon France Logistique 과징금). 강등된 주장은 없다. 다만 f17·f35·f49·f5의 문구는 출처 범위에 맞게 고쳤다. 원문 미열람 출처는 ref-494, ref-588, ref-589, ref-857, ref-700, ref-854, ref-863, ref-969, ref-1076, ref-1105, ref-1106, ref-1107, ref-1109, ref-1110, ref-1111, ref-1112, ref-1113, ref-1114, ref-1116, ref-1136, ref-1138, ref-1141, ref-1145, ref-1146, ref-1173, ref-1299, ref-1301, ref-1242, ref-1263, ref-1260, ref-1371이다. ref-009·ref-010·ref-031·ref-405·ref-579는 입력 원문 텍스트로 대조했다. 벤더 주장은 f2(KUKA SL2 인증 '최초')와 f18(Zena RX)이다. Pudu 사례(f20·f29·f34·f55)는 같은 연구자 공개를 옮긴 기사 두 건에 기대므로 교차 확인이 아니다. 주의할 점이 있다. 연결의 절반 가까이가 [추정]이고 근거 대부분이 단일 출처의 재인용이다. f52는 로봇이 아니라 작업자 스캐너 사례다. 로봇 제어기·승강기·기기 쪽 보안과 법 적용 판단은 연계 대상이다. 정정 요청은 없다. / 2차 수정 후 재검증. 드리프트 1건을 처리하도록 지시했다(L. AI·학습 기술 항목의 '장면 인식 모델' 단정). 문자만 쓴 대분류 호칭 1곳과 약어 풀어쓰기는 문체 수정 대상이다. 1차 수정 26건은 모두 페이지에 반영됐다(벤더 주장 병기, 원문 미열람 표기, f5 매개변수 필수·선택 구분, f11 v2 기준일, f16 저자 보고값, f17·f35·f49 문구, f34 두 설명 병기, f52 물류창고 칸 제외, 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈의 구분, L. AI·학습 기술의 교차 규칙). 태그는 1차 처분과 같다. [분류원문] 문장은 보존됐고, 바뀐 절은 '다른 대분류와의 연결'과 '참고 자료'(각주 정의 추가)뿐이다. 링크는 유효하다. 사소한 의견이 하나 있다. D. 공간·지도 모델 항목의 지도 저장 위치 문장에는 ref-1141 각주도 붙어 있지만 본문은 저장 위치를 기사 한 건(ref-1372)에서만 확인했다고 적는다. ref-1141은 점검 발표 자체의 근거로 읽는다.",
  "retry_reason": null
}
```
