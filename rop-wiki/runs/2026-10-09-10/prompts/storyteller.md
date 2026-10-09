(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/storyteller.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

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
        "ref-1304"
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
        "ref-1304",
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
        "ref-1367"
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
        "ref-1367",
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
        "ref-1342"
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
        "ref-1425"
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
        "ref-1425"
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
      "id": "ref-1304",
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
      "id": "ref-1342",
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
      "id": "ref-1425",
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
      "id": "ref-1367",
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
    "limits": "web_fetch_available: true · fetch_mode full. 대분류 연결(category_link) 실행이다. 근거는 먼저 게시된 51·52·53 페이지와 A·B·D·E·F·G 대분류 페이지, 이전 브리프(2026-10-09-08, 2026-10-09-09)의 검증된 주장에서 찾고 재사용 출처 id 를 썼다(재사용 35건 가운데 이번에 다시 연 것은 ref-031(github_raw) 1건이고 나머지 34건은 fetched false·source_unopened true). 신규 출처는 10건(ref-1367~ref-1376, 예약 구간 안)이며 ref-1371(CNIL 공지)을 뺀 9건은 원문을 열었다. 검색 13회/30, 신규 출처 10건/15. 교차 확인 2건(f42 ISO 10218 사이버보안, f52 CNIL Amazon 과징금). 벤더 주장 2건(f2·f18). 같은 정부 발표를 옮긴 기사 쌍(f1, f51)과 같은 연구자 공개를 옮긴 기사 쌍(f20 등)은 독립 출처로 보지 않아 교차 확인으로 세지 않았다. 한국 자료: 신규 ref-1372·ref-1373, 재사용 ref-589·ref-588·ref-969·ref-1111·ref-1136·ref-1138·ref-1141·ref-1301·ref-1342. 현장 유형: 물류창고(f52·f53, 로봇이 아닌 스캐너 사례)·제조 공장(f44)·병원(f18·f21·f56)·상업 시설(f20·f29·f34)·가정(f14·f39·f48)·실외(f40·f51)·기타(f55) 각 1건 이상. 18. 실시간 세계 상태·데이터 일관성(현재 상태, f16·f17)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래, f30·f31)을 구분했다. 분류 원문 교차 규칙에 해당하는 L. AI·학습 기술 연결(f11·f40·f41)은 적용 대상 영역과 함께 제안했다. 열린 질문 oq-056·oq-082·oq-099·oq-100·oq-102·oq-113·oq-214·oq-246·oq-248·oq-249·oq-250·oq-259·oq-285·oq-291 에는 부분 근거만 더했고 해결 제안은 없다. 대분류 페이지 절 번호는 이전 대분류 연결 실행과 같이 제목 순서(핵심 질문·개요·세부 연구영역·핵심 포인트·다른 대분류와의 연결)에 따라 '5'로 매겼다 [가정]. 아직 근거를 찾지 못한 연결은 page_proposals 의 rationale 에 적었다. 정정 요청 없음. 우선 지정 질문 없음. 입력 누락 없음."
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
      "note": "확인: M 대분류 연결 f56 과 같은 검증 주장(ref-1304 이번 실행 원문 미열람). 가정한 미래를 실험하는 34번 쪽."
    },
    {
      "finding_id": "f31",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 추정. 18번(현재 상태)과 34·36번(가정한 미래·재현)의 구분이 원문 주석과 맞음. ref-1304·ref-588 원문 미열람."
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
      "note": "ref-1367 재열람: 2026-09-11 시행, 제조자의 적극 악용 취약점·중대 사고 보고, 24시간 조기 경보·72시간 통지·취약점 최종 보고는 시정 조치 뒤 14일·중대 사고는 72시간 통지 뒤 한 달, 오픈소스 관리자 2027-12-11, 페이지 갱신 2026-09-11 확인. 다만 통지는 ENISA 단일 보고 플랫폼을 '거쳐' 주 사업장 CSIRT 로 가므로 'ENISA 로 알려야'는 바로잡는다. 규정 원문 미열람, 집행위원회 안내 페이지 기준."
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
      "note": "확인: 53 페이지·L 대분류 연결의 검증 주장 재인용. 두 출처는 서로 다른 시점의 조치. ref-1138·ref-1342 이번 실행 원문 미열람."
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
      "note": "확인: M 대분류 연결 f23 재인용(ref-1425 원문 미열람). 초안 기준, 최종판 반영 미확인(oq-254)."
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
      "f42·f45·f30 은 M. 안전 대분류 연결(2026-10-09-09 실행 f54·f57·f56)과 같은 주장 — 같은 각주(ref-1116·ref-1076·ref-1425·ref-1304)와 태그를 재사용한다",
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
    "원문 미열람 표기: ref-494·ref-588·ref-589·ref-857·ref-700·ref-854·ref-863·ref-969·ref-1076·ref-1105·ref-1106·ref-1107·ref-1109·ref-1110·ref-1111·ref-1112·ref-1113·ref-1114·ref-1116·ref-1136·ref-1138·ref-1141·ref-1145·ref-1146·ref-1173·ref-1299·ref-1301·ref-1304·ref-1342·ref-1371·ref-1425 의 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣는다 — 이번 실행에서 본문을 읽지 않았다.",
    "ref-009·ref-010·ref-031·ref-405·ref-579 는 입력의 data/source_texts 원문이 있으므로 각주에 '(원문 미열람)'을 붙이지 않는다 — 브리프 summary 의 '원문 미열람' 문구는 source_texts 원문 존재와 맞지 않는다.",
    "ref-1367 각주의 발행일 자리에 '미확인(페이지 최종 갱신 2026-09-11)', ref-1376 은 '미확인(페이지 최종 갱신 2025-12-15)'을 쓴다 — 검증 열람에서 갱신일을 확인했다.",
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
  "verification_note": "판정: 조건부 승인. 확인 56건, 미확인 0건, 교차 확인 2건(f42 ISO 10218 2025년판 사이버보안 요구, f52 CNIL 의 Amazon France Logistique 과징금). 강등: 없음. 다만 f17·f35·f49·f5 의 문구는 출처 범위에 맞게 고친다. 검증에서 새 출처 9건과 ref-031 VDA 5050 원문을 다시 열어 확인했다. 원문 미열람 출처: ref-494, ref-588, ref-589, ref-857, ref-700, ref-854, ref-863, ref-969, ref-1076, ref-1105, ref-1106, ref-1107, ref-1109, ref-1110, ref-1111, ref-1112, ref-1113, ref-1114, ref-1116, ref-1136, ref-1138, ref-1141, ref-1145, ref-1146, ref-1173, ref-1299, ref-1301, ref-1304, ref-1342, ref-1425, ref-1371. 다시 연 출처는 ref-1367~ref-1370, ref-1372~ref-1376(webfetch), ref-031(github_raw)이다. ref-009·ref-010·ref-405·ref-579 는 입력 원문 텍스트로 대조했다. 브리프는 이 넷을 fetched: true 로 적으면서 summary 에 '원문 미열람'이라고 써서 서로 맞지 않는다. 벤더 주장은 f2(KUKA SL2 인증 '최초')와 f18(Zena RX)이다. Pudu 사례(f20·f29·f34·f55)는 같은 연구자 공개를 옮긴 기사 두 건 기준이라 교차 확인이 아니다. 주의: 연결의 절반 가까이가 [추정]이고 근거 대부분이 단일 출처의 재인용이다. f52 는 로봇이 아닌 작업자 스캐너 사례다. 로봇 제어기·승강기·기기 쪽 보안과 법 적용 판단은 연계 대상이다. 검색은 3회 썼다(리서치 13회와 합쳐 16/30). 정정 요청은 없다.",
  "retry_reason": null
}
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

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 45건 / 전체 1262건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

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

### docs/glossary/index.md (요약: 용어 358개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [51, 52, 53] 에 걸린 33건 / 전체 309건)

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
```

### docs/standards/index.md (요약: 322개 — 이름 · 종류 · 발행 기관)

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
- ISO/IEC Guide 71:2014 표준의 접근성 반영 지침(2판) · ISO/IEC · 표준
- 장애인차별금지법에 따른 무인정보단말기 접근성 의무(2026-01-28 전면 시행) · 보건복지부 · 프레임워크
- 근로자참여 및 협력증진에 관한 법률 제20조(협의 사항) · 대한민국 국회 · 프레임워크
- 독일 사업장조직법(BetrVG) 제87조 공동결정권 · Bundesministerium der Justiz · 프레임워크
- 지능형로봇법·도로교통법 개정(실외이동로봇 보도 통행·운용자 의무·보험 의무, 2023-11-17 시행) · 산업통상자원부·경찰청 · 프레임워크
- 버지니아주법 §46.2-908.1:1 개인 배송 장치(Personal Delivery Devices) · Commonwealth of Virginia · 프레임워크
- EU 개정 제조물책임지침 (Directive (EU) 2024/2853) · European Union (Gibson Dunn 해설 경유) · 프레임워크
- 한국 제조물책임법 · 대한민국 (김·장 법률사무소 해설 경유) · 프레임워크
- 인공지능 기본법 (2026-01-22 시행) · 과학기술정보통신부 · 프레임워크
- EU 사이버복원력법(CRA) 보고 의무 · European Commission · 프레임워크
- 산업안전보건법 안전검사 (산업용 로봇·컨베이어) · 고용노동부 · 프레임워크
- ROS 2 개발자 가이드 (패키지 라이선스·저작권 규칙) · Open Robotics (ROS 2 Documentation) · 오픈소스
- REP 2004 Package Quality Categories · ROS (ros-infrastructure/rep) · 프레임워크
- SPDX (ISO/IEC 5962:2021) · SPDX Project (Linux Foundation) · 표준
- Gazebo(클래식) 모델 구조·요구사항 (모델 데이터베이스 라이선스 표기) · Open Robotics (Gazebo Classic) · 오픈소스
- ANSI/ISA 18.2-2016 공정 산업 경보 시스템 관리 (Management of Alarm Systems for the Process Industries) · ISA(International Society of Automation) · 표준
- IDTA 02005 Provision of Simulation Models (1.0) · IDTA(Industrial Digital Twin Association) · 표준
- autoware_rosbag2_anonymizer · Autoware Foundation · 오픈소스
- Gazebo Fuel Tools (gz-fuel-tools) · Open Robotics · 오픈소스
```

### runs/2026-10-09-10/docs_tree.txt

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
glossary/a-b-update.md
glossary/aas-registry-and-discovery.md
glossary/ablation-study.md
glossary/action-dependency-graph.md
glossary/affordance.md
glossary/age-of-information.md
glossary/agentic-ai.md
glossary/aggregation-event.md
glossary/agv-technical-data-submodel.md
glossary/alarm-management.md
glossary/almere-model.md
glossary/alternative-name.md
glossary/amr-assisted-order-picking.md
glossary/api-deprecation-policy.md
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
glossary/curb-cut.md
glossary/cyber-resilience-act.md
glossary/data-holder.md
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
glossary/human-motion-trajectory-prediction.md
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
glossary/integrity-risk.md
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
glossary/kiosk-accessibility.md
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
glossary/localization-score.md
glossary/location-check-digit.md
glossary/lockout-tagout.md
glossary/log-playback.md
glossary/managed-node.md
glossary/map-alignment.md
glossary/map-distribution.md
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
glossary/model-contractual-terms.md
glossary/model-registry.md
glossary/model-substitution-and-routing-dilution.md
glossary/models-and-simulations-credibility-assessment.md
glossary/mqtt-last-will.md
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
glossary/post-occupancy-evaluation.md
glossary/power-and-force-limiting.md
glossary/pre-execution-plan-verification.md
glossary/pre-hold-post-condition.md
glossary/precedence-constraint.md
glossary/predictive-maintenance.md
glossary/presumption-of-conformity.md
glossary/priority-inheritance-with-backtracking.md
glossary/private-5g-network.md
glossary/process-mining.md
glossary/product-liability.md
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
glossary/runtime-tracing.md
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
glossary/social-force-model.md
glossary/social-robot-navigation.md
glossary/soft-landings.md
glossary/software-bill-of-materials.md
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
glossary/substantial-modification.md
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
glossary/utaut.md
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
logs/daily/2026-10-09.md
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
references/ref-1171.md
references/ref-1172.md
references/ref-1173.md
references/ref-1174.md
references/ref-1175.md
references/ref-1176.md
references/ref-1177.md
references/ref-1178.md
references/ref-1179.md
references/ref-118.md
references/ref-1180.md
references/ref-1181.md
references/ref-1182.md
references/ref-1183.md
references/ref-1184.md
references/ref-1185.md
references/ref-1186.md
references/ref-1187.md
references/ref-1188.md
references/ref-1189.md
references/ref-119.md
references/ref-1190.md
references/ref-1191.md
references/ref-1192.md
references/ref-1193.md
references/ref-1194.md
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
references/ref-1204.md
references/ref-1205.md
references/ref-1206.md
references/ref-1207.md
references/ref-1208.md
references/ref-1209.md
references/ref-121.md
references/ref-1210.md
references/ref-1211.md
references/ref-1212.md
references/ref-1213.md
references/ref-1214.md
references/ref-1215.md
references/ref-1216.md
references/ref-1217.md
references/ref-1218.md
references/ref-1219.md
references/ref-122.md
references/ref-1220.md
references/ref-1221.md
references/ref-1222.md
references/ref-1223.md
references/ref-1224.md
references/ref-1225.md
references/ref-1226.md
references/ref-1227.md
references/ref-1228.md
references/ref-1229.md
references/ref-123.md
references/ref-1230.md
references/ref-1231.md
references/ref-1232.md
references/ref-1233.md
references/ref-1234.md
references/ref-1235.md
references/ref-1236.md
references/ref-1237.md
references/ref-1238.md
references/ref-124.md
references/ref-125.md
references/ref-126.md
references/ref-127.md
references/ref-1270.md
references/ref-1271.md
references/ref-128.md
references/ref-129.md
references/ref-1299.md
references/ref-130.md
references/ref-1300.md
references/ref-1301.md
references/ref-1302.md
references/ref-131.md
references/ref-132.md
references/ref-133.md
references/ref-1333.md
references/ref-1334.md
references/ref-1335.md
references/ref-1336.md
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
topics/2026/2026-09-30-area19-s10.md
topics/2026/2026-09-30-area19-s11.md
topics/2026/2026-09-30-area19-s3.md
topics/2026/2026-09-30-area19-s4.md
topics/2026/2026-09-30-area19-s6.md
topics/2026/2026-09-30-area19-s7.md
topics/2026/2026-09-30-area19-s8.md
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
topics/2026/2026-09-30-area56-s10.md
topics/2026/2026-09-30-area56-s11.md
topics/2026/2026-09-30-area56-s3.md
topics/2026/2026-09-30-area56-s4.md
topics/2026/2026-09-30-area56-s6.md
topics/2026/2026-09-30-area56-s7.md
topics/2026/2026-09-30-area56-s8.md
topics/2026/2026-09-30-area58-s10.md
topics/2026/2026-09-30-area58-s11.md
topics/2026/2026-09-30-area58-s3.md
topics/2026/2026-09-30-area58-s4.md
topics/2026/2026-09-30-area58-s6.md
topics/2026/2026-09-30-area58-s7.md
topics/2026/2026-09-30-area59-s10.md
topics/2026/2026-09-30-area59-s11.md
topics/2026/2026-09-30-area59-s3.md
topics/2026/2026-09-30-area59-s4.md
topics/2026/2026-09-30-area59-s6.md
topics/2026/2026-09-30-area59-s7.md
topics/2026/2026-09-30-area59-s8.md
topics/2026/2026-09-30-area60-s10.md
topics/2026/2026-09-30-area60-s11.md
topics/2026/2026-09-30-area60-s3.md
topics/2026/2026-09-30-area60-s4.md
topics/2026/2026-09-30-area60-s6.md
topics/2026/2026-09-30-area60-s7.md
topics/2026/2026-09-30-area60-s8.md
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
