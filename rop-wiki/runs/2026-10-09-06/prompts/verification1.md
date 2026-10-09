(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-09-06
- date: 2026-10-09
- run_type: category_link (대분류 연결)
- 대상: 대분류 K. 플랫폼 아키텍처·인프라 페이지의 '다른 대분류와의 연결' 절(대분류 연결 실행). 게시된 세부영역 페이지를 근거로 다른 대분류와의 연결을 조사·서술한다. 스토리텔러는 그 절만 patches 로 바꾼다
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

### runs/2026-10-09-06/target.json

```json
{
  "run_id": "2026-10-09-06",
  "date": "2026-10-09",
  "weekday": "Fri",
  "run_number": 139,
  "run_type": "category_link",
  "forced": true,
  "target": {
    "area_no": null,
    "area_name": null,
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
  "selection_rationale": "CLI 지정 run_type=category_link"
}
```

### runs/2026-10-09-06/research.json

```json
{
  "run_id": "2026-10-09-06",
  "date": "2026-10-09",
  "run_type": "category_link",
  "target": {
    "area_no": null,
    "area_name": null,
    "category": "K. 플랫폼 아키텍처·인프라"
  },
  "gaps": [
    "K. 플랫폼 아키텍처·인프라 대분류 페이지의 '다른 대분류와의 연결' 절이 '아직 작성되지 않음' 상태다. 41. 플랫폼 아키텍처·외부 API, 42. 분산 시스템·통신·컴퓨팅 구조, 43. 데이터·관측성·배포와 다른 16개 대분류를 잇는 연결이 정리되지 않았다",
    "42. 분산 시스템·통신·컴퓨팅 구조 페이지는 이전 분류(2026-09-25) 기준으로 쓰였다. 그래서 C. 채팅 기반 구성·운영, L. AI·학습 기술, M. 안전, P. 거버넌스·법규·사회, Q. 현장 유형별 적용과의 연결 근거가 약하다",
    "41·42·43 페이지의 10절(다른 연구영역과의 연결)은 주제 페이지로 분리되어 있다. 대분류 단위로 묶은 연결은 없다",
    "P. 거버넌스·법규·사회의 58. 다사업자 책임·계약·데이터, 60. 노동·수용성·접근성과 K. 플랫폼 아키텍처·인프라를 잇는 검증된 근거가 게시 페이지에 없다",
    "Q. 현장 유형별 적용의 상업 시설·가정·실외 사례가 K. 플랫폼 아키텍처·인프라 페이지에 없다"
  ],
  "research_questions": [
    "플랫폼을 어디에 어떻게 두어야 끊김·확장·다현장 조건에서도 계속 동작하는가? [분류원문]",
    "41. 플랫폼 아키텍처·외부 API의 판단 배치와 외부 API 는 B. 로봇 온톨로지(6. 온톨로지 기반 시스템·로봇 연동), C. 채팅 기반 구성·운영(12. 채팅으로 업무 지시·오케스트레이션, 13. 대화형 기능의 신뢰·기반), F. 연동(20·21·23)과 무엇을 주고받는가? (oq-206, oq-207, oq-208, oq-209 관련)",
    "42. 분산 시스템·통신·컴퓨팅 구조의 단절·통신 조건은 E. 사물·사람·실시간 상태(18. 실시간 세계 상태·데이터 일관성), G. 계획·최적화(25·27), H. 실행·협업·예외 복구(29·32)의 결정과 어떻게 맞물리는가? (oq-035, oq-038, oq-083 관련)",
    "43. 데이터·관측성·배포의 기록·관측·배포·비용 관리는 I. 설계·시뮬레이션(34·36), J. 현장 운영·관제(37·38), O. 검증·도입·수명주기(57)에 무엇을 넘겨주는가? (oq-210, oq-213 관련)",
    "K. 플랫폼 아키텍처·인프라는 A. 기획·사업(비용·과금), L. AI·학습 기술(언어 모델 호출 배치), M. 안전(사고 조사 기록), N. 보안·개인정보(인증·접속기록), P. 거버넌스·법규·사회(보관 의무)와 어디서 만나는가? (oq-211, oq-212, oq-214, oq-267 관련)",
    "K. 플랫폼 아키텍처·인프라의 구조 선택은 Q. 현장 유형별 적용의 물류창고·제조 공장·병원·기타 현장 사례에서 어떻게 나타나는가?"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포 ↔ A. 기획·사업의 3. 경제성·조달·사업 모델 연결 근거: FinOps Foundation 은 클라우드 비용 관리를 알리기(Inform)·최적화(Optimize)·운영(Operate) 단계가 되풀이되는 주기로 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1041"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "43. 데이터·관측성·배포 페이지 6·7절이 비용 관리 주기의 근거로 인용한 FinOps 단계 설명. 이번 재실행에서 원문을 다시 열지 않았다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f2",
      "claim": "K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포 ↔ A. 기획·사업의 3. 경제성·조달·사업 모델 연결 근거: FinOps Foundation 은 2025-06-03 FOCUS 1.2 를 발표하면서 SaaS·PaaS 청구 데이터 지원과 청구서 대사(invoice reconciliation)를 더했다고 밝혔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1042"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "발행 기관의 발표 글 기준이며 명세 본문은 미열람이다. 43. 데이터·관측성·배포 페이지 각주가 '명세 본문 미열람'으로 표시했다.",
      "as_of": "2025-06-03",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f3",
      "claim": "K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포 ↔ A. 기획·사업의 3. 경제성·조달·사업 모델: 43. 데이터·관측성·배포가 계측·배분하는 클라우드·언어 모델 호출 비용은 3. 경제성·조달·사업 모델의 총소유비용 산정과 과금 단위 결정의 입력이 될 것으로 보인다. 다만 다중 제조사 오케스트레이션 플랫폼의 과금 단위를 공개한 자료는 확인되지 않았다(oq-267).",
      "tag": "추정",
      "source_ids": [
        "ref-1041",
        "ref-1042",
        "ref-1037"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "43. 데이터·관측성·배포 페이지 9절은 클라우드·언어 모델 호출 비용의 계측·배분을 ROP 직접 범위로 본다([추정]). 3. 경제성·조달·사업 모델 페이지는 사용량 계량과 과금을 다룬다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f4",
      "claim": "K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조 ↔ A. 기획·사업의 3. 경제성·조달·사업 모델: FreightWaves 기사는 하이브리드 WMS 판매사의 조사를 인용해 창고 운영 중단 비용이 시간당 최대 10만 달러라고 전한다. 이는 연결 단절이 투자 효과 판단에 들어갈 위험 비용이 될 수 있음을 보여 준다.",
      "tag": "추정",
      "source_ids": [
        "ref-309"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 응답 조직의 84%가 최근 24개월 안에 큰 운영 중단을 겪었고 절반 가까이가 소프트웨어·연결 중단으로 자동화 자산이 멈췄다는 판매사 조사 주장. 조사 방법·표본·하한은 미확인이다(42. 분산 시스템·통신·컴퓨팅 구조 3절). (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": "물류창고",
      "flow_item": "예외·성과",
      "source_unopened": true,
      "vendor_claim": true
    },
    {
      "id": "f5",
      "claim": "K. 플랫폼 아키텍처·인프라의 41. 플랫폼 아키텍처·외부 API ↔ A. 기획·사업의 1. 기술·시장·업체 동향: 네이버는 제2사옥 1784 에서 로봇 100여 대를 클라우드로 제어하고, 로봇에는 연산·판단을 싣지 않는 구조를 쓴다고 밝힌다.",
      "tag": "추정",
      "source_ids": [
        "ref-1023"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: ARC brain·eye·mind 가 클라우드에서 이동 계획·위치 결정·개발자용 웹 OS 를 맡는다고 소개한다(41. 플랫폼 아키텍처·외부 API 5절 기타 사례). (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": "기타",
      "flow_item": "수행 자원",
      "source_unopened": true,
      "vendor_claim": true
    },
    {
      "id": "f6",
      "claim": "K. 플랫폼 아키텍처·인프라의 41. 플랫폼 아키텍처·외부 API ↔ B. 로봇 온톨로지의 6. 온톨로지 기반 시스템·로봇 연동 연결 근거: Open-RMF 플릿 어댑터 템플릿 설정은 수행 가능한 작업 유형(task_capabilities)과 동작 이름(actions)을 선언한다.",
      "tag": "사실",
      "source_ids": [
        "ref-105"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "B. 로봇 온톨로지·F. 연동 대분류 페이지에 같은 각주로 실린 검증된 주장. 이번 재실행에서 원문을 다시 열지 않았다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f7",
      "claim": "K. 플랫폼 아키텍처·인프라의 41. 플랫폼 아키텍처·외부 API ↔ B. 로봇 온톨로지의 6. 온톨로지 기반 시스템·로봇 연동: 41. 플랫폼 아키텍처·외부 API가 ROP 직접 범위로 두는 제조사 어댑터 계층은 6. 온톨로지 기반 시스템·로봇 연동이 능력 모델에서 만드는 어댑터 설정·명령 매핑 초안이 반영되는 자리가 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-004",
        "ref-105"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "41. 플랫폼 아키텍처·외부 API 9절: 제조사 어댑터 계층을 둔 제조사 중립 기준 아키텍처([추정]). 6. 온톨로지 기반 시스템·로봇 연동 1절 리스트업: 어댑터 설정·명령 매핑 초안 생성. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f8",
      "claim": "K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포 ↔ B. 로봇 온톨로지의 7. 온톨로지 검증·변경 관리: 43. 데이터·관측성·배포가 남기는 소프트웨어·펌웨어 배포 버전 기록은 7. 온톨로지 검증·변경 관리가 능력 정의를 다시 검증할 계기를 알려 주는 입력이 될 것으로 보인다. 두 기록을 잇는 공개 사례는 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1040"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "43. 데이터·관측성·배포 9절은 플랫폼 구성 요소의 배포·롤백·버전 기록을 직접 범위로 본다. 7. 온톨로지 검증·변경 관리 1절은 문서·펌웨어 개정에 따른 능력 정의 버전 관리를 다룬다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f9",
      "claim": "K. 플랫폼 아키텍처·인프라의 41. 플랫폼 아키텍처·외부 API ↔ C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션 연결 근거: Open Robotics 상호운용 SIG 의 2026-07-02 발표 안내문은 Nayantra 를 소개했다. Nayantra 는 Open-RMF REST API 를 언어 모델이 호출하는 도구로 노출하는 MCP 서버와, 평이한 영어 지시를 RMF 임무로 바꾸는 에이전트로 이루어진다.",
      "tag": "사실",
      "source_ids": [
        "ref-854"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "E. 사물·사람·실시간 상태 대분류 페이지에 실린 검증된 주장(안내문 기준, 발표 내용 자체는 미열람, 시연은 Isaac Sim 창고 시뮬레이션).",
      "as_of": "2026-06-25",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f10",
      "claim": "K. 플랫폼 아키텍처·인프라의 41. 플랫폼 아키텍처·외부 API ↔ C. 채팅 기반 구성·운영의 13. 대화형 기능의 신뢰·기반: 대화형 기능이 플랫폼 외부 API 를 도구로 부르면, API 의 인증·권한 범위가 13. 대화형 기능의 신뢰·기반이 다루는 사용자별 대화 권한의 실제 집행 지점이 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-854",
        "ref-762"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "rmf-server 는 OIDC 인증과 역할·동작·자원 권한 그룹으로 API 접근을 판정한다(43·J 대분류 근거). Nayantra 는 REST API 를 언어 모델 도구로 노출한다(f9).",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f11",
      "claim": "K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포 ↔ C. 채팅 기반 구성·운영의 13. 대화형 기능의 신뢰·기반 연결 근거: OpenTelemetry 생성형 AI 의미 규약 저장소는 언어 모델 클라이언트 호출의 토큰 사용량 지표를 정의한다. 이 규약은 아직 개발(Development) 단계다.",
      "tag": "사실",
      "source_ids": [
        "ref-1037"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "43. 데이터·관측성·배포 페이지가 토큰 지표 근거로 인용했다. 지표 이름이 문서마다 다른지는 미확인이다(oq-212). (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f12",
      "claim": "K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포 ↔ C. 채팅 기반 구성·운영의 13. 대화형 기능의 신뢰·기반: 13. 대화형 기능의 신뢰·기반이 언어 모델 공급자를 고르고 바꾸려면, 43. 데이터·관측성·배포가 호출별 토큰·비용·지연을 계측해야 할 것으로 보인다. 다만 계측 지표 이름은 안정 판이 나오지 않아 고정되지 않았다(oq-212).",
      "tag": "추정",
      "source_ids": [
        "ref-1037",
        "ref-1043"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "토큰 지표는 개발 단계이고(f11), 서비스 로봇 연구는 클라우드 API 비용·지연을 동기로 로컬·클라우드 모델을 비교했다(f40).",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f13",
      "claim": "K. 플랫폼 아키텍처·인프라의 41. 플랫폼 아키텍처·외부 API ↔ D. 공간·지도 모델의 15. 지도·공간·위치 모델: 네이버는 ARC eye 가 클라우드에서 디지털 트윈 데이터와 측위 AI 로 로봇 위치를 정한다고 밝힌다. 위치 모델을 클라우드에 둔 이 설계에서 연결이 끊기면 로봇이 어디까지 동작하는지는 공개되지 않았다(oq-206).",
      "tag": "추정",
      "source_ids": [
        "ref-1023"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: ARC eye 가 디지털 트윈 데이터와 측위 AI 로 로봇 위치를 결정한다는 소개(41. 플랫폼 아키텍처·외부 API 5절). 위치 추정은 원문 19장 로봇 자체 지능 경계의 연계 대상이다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": "기타",
      "flow_item": "수행 자원",
      "source_unopened": true,
      "vendor_claim": true
    },
    {
      "id": "f14",
      "claim": "K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조 ↔ E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성 연결 근거: 통신 계층에는 상태가 오래되었음을 알리는 장치가 있다. ROS 2 QoS 의 기한·생존성 정책, Sparkplug 의 노드 종료(NDEATH) 뒤 지표 STALE 표시, VDA 5050 의 MQTT 유언을 통한 연결 끊김 통지가 그 예다.",
      "tag": "사실",
      "source_ids": [
        "ref-282",
        "ref-287",
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "B·E·F 대분류 페이지에 같은 각주로 실린 검증된 주장. 세 출처는 각각 한 장치만 다루므로 서로 교차 확인한 것이 아니다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f15",
      "claim": "K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조 ↔ E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성 연결 근거: Open-RMF 로봇 상태는 밀리초 단위 유닉스 시각(unix_millis_time)을, VDA 5050 상태는 ISO 8601 형식 시각(timestamp)을 담는다. 시각 표현이 서로 다른 셈이다.",
      "tag": "사실",
      "source_ids": [
        "ref-148",
        "ref-051"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "E. 사물·사람·실시간 상태 대분류 페이지의 검증된 주장. 공통 시간축 변환과 허용 시계 오차를 정한 자료는 확인되지 않았다(oq-035). (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f16",
      "claim": "K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포 ↔ E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적·18. 실시간 세계 상태·데이터 일관성: EPCIS 2.0 온톨로지는 발생 시각(eventTime)·기록 시각(recordTime)·UTC 차이를 구분한다. 그래서 실행 기록과 관측 데이터에서도 발생 시각과 수신·기록 시각을 따로 남기는 설계가 두 대분류를 잇는 지점이 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-045"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "E. 사물·사람·실시간 상태 대분류 페이지 K 항목에 실린 [추정] 연결을 재사용했다.",
      "as_of": "2021-09-30",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f17",
      "claim": "K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조 ↔ F. 연동의 20. 로봇·제조사 관제 연동 연결 근거: VDA 5050(3.0.0 기준)은 연결 실패와 메시지 손실이 있는 무선망을 전제한다. 그래서 주문·상태 토픽에 재전송 없는 MQTT QoS 0 을 쓴다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "42. 분산 시스템·통신·컴퓨팅 구조 5·7절의 검증된 주장. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f18",
      "claim": "K. 플랫폼 아키텍처·인프라의 41. 플랫폼 아키텍처·외부 API ↔ F. 연동의 20. 로봇·제조사 관제 연동 연결 근거: Open-RMF 플릿 어댑터는 로봇의 예상 이동 경로를 시설 전체의 중앙 교통 스케줄에 보고한다. 또 제조사 관제가 허용하는 제어 수준에 따라 전체 제어·신호등·읽기 전용 가운데 하나로 붙는다.",
      "tag": "사실",
      "source_ids": [
        "ref-004",
        "ref-251"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "F. 연동 대분류 페이지에 실린 검증된 주장. 제어 수준별 교통 성능 차이는 미확인이다(oq-032). (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f19",
      "claim": "K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조 ↔ F. 연동의 23. 업무 시스템 연동: 외부망이 끊긴 동안 현장 관제는 이미 받은 주문을 이어 갈 수 있을 것으로 보인다. 반면 클라우드 WMS 의 새 주문 수신과 재고 확정은 멈추고, 재연결 뒤 현장 완료 기록과 WMS 기록을 맞추는 절차가 필요할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-300",
        "ref-310"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "42. 분산 시스템·통신·컴퓨팅 구조 5절의 피킹 시나리오 추론. 관제 표준·엣지 플랫폼 문서와 CAP 제약을 대응시켜 얻은 것이다. 물류센터 운영 기준은 미확인이다(oq-038).",
      "as_of": "2026-10-09",
      "site_type": "물류창고",
      "flow_item": "완료·인계",
      "source_unopened": false
    },
    {
      "id": "f20",
      "claim": "K. 플랫폼 아키텍처·인프라의 41. 플랫폼 아키텍처·외부 API ↔ F. 연동의 23. 업무 시스템 연동: Locus Robotics 는 LocusONE 이 WMS 주문을 API 로 받아 로봇 작업으로 내리고, 피킹 완료 확인을 WMS 로 즉시 회신한다고 밝힌다.",
      "tag": "추정",
      "source_ids": [
        "ref-1030"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 주문 수신과 완료 회신을 모두 외부 API 가 맡는 구조(41. 플랫폼 아키텍처·외부 API 5절 물류창고 사례, 흐름 단계 피킹). (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": "물류창고",
      "flow_item": "시작 조건",
      "source_unopened": true,
      "vendor_claim": true
    },
    {
      "id": "f21",
      "claim": "K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포 ↔ F. 연동의 22. 설비·건물 시스템 연동 연결 근거: 고려대학교 구로병원 약품 배송 로봇 실증은 세 기록을 함께 모아 실패 원인을 분석했다. 승강기 호출·탑승·문 동작 시각을 1 Hz 로 남긴 로봇 시스템 로그, 승강기 상태·문·위치·로봇 명령을 담은 승강기 통신 로그, 관찰자 기록지다.",
      "tag": "사실",
      "source_ids": [
        "ref-943"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "43. 데이터·관측성·배포 5절 병원 사례의 검증된 주장. 승강기 통신 로그 생성은 시설·설비 제어 경계의 연계 대상이고, ROP 몫은 수집·결합이다.",
      "as_of": "2026-03-31",
      "site_type": "병원",
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f22",
      "claim": "K. 플랫폼 아키텍처·인프라의 41. 플랫폼 아키텍처·외부 API ↔ F. 연동의 21. 상호운용 표준·적합성 연결 근거: OpenAPI 명세 3.1.0 은 HTTP API 를 언어와 무관하게 기술하는 표준 인터페이스 기술 형식이다. AsyncAPI 명세 3.1.0 은 메시지 기반 API 를 기술하는 형식이다.",
      "tag": "사실",
      "source_ids": [
        "ref-1025",
        "ref-1024"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "41. 플랫폼 아키텍처·외부 API 7절이 외부 API 를 기계가 읽게 기술하는 표준으로 든 두 명세.",
      "as_of": "2021-02-15",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f23",
      "claim": "K. 플랫폼 아키텍처·인프라의 41. 플랫폼 아키텍처·외부 API ↔ F. 연동의 21. 상호운용 표준·적합성: 플랫폼 외부 API 를 OpenAPI·AsyncAPI 로 기계가 읽게 기술하면, 21. 상호운용 표준·적합성이 다루는 연동 규격 적합성 시험의 기준 문서가 될 수 있을 것으로 보인다. 국내에 통합관제 플랫폼 외부 API 를 정한 TTA·KS 표준이 있는지는 확인되지 않았다(oq-209).",
      "tag": "추정",
      "source_ids": [
        "ref-1025",
        "ref-1024"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "41. 플랫폼 아키텍처·외부 API 9절은 REST·이벤트 API 명세와 버전 표기를 ROP 직접 범위로 둔다([추정]).",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f24",
      "claim": "K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조 ↔ G. 계획·최적화의 25. 작업 배정 — MRTA 연결 근거: Lott·Honary(2026-09, 프리프린트)는 분산 작업 배정기 6종(CBAA, ACBBA, PI, HIPC, DMCHBA, DGA)을 패킷 손실·페이딩 같은 통신 저하 조건에서 비교했다.",
      "tag": "사실",
      "source_ids": [
        "ref-493"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "G. 계획·최적화 대분류 페이지에 실린 검증된 주장(원문 미열람, 초록 기준).",
      "as_of": "2026-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f25",
      "claim": "K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조 ↔ G. 계획·최적화의 25. 작업 배정 — MRTA: 배정 계산을 클라우드·현장 서버·로봇 가운데 어디에 둘지가 두 대분류를 잇는 설계 쟁점이 될 것으로 보인다. 다만 통신이 나빠질 때 중앙 방식과 분산 방식 사이를 언제 바꿀지 정한 물류센터 기준은 확인되지 않았다(oq-083).",
      "tag": "추정",
      "source_ids": [
        "ref-493",
        "ref-401"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "G. 계획·최적화 대분류 페이지의 [추정] 연결을 재사용했다. 근거는 통신 저하 비교 벤치마크와 클라우드 연결 로봇그룹 작업 계획 국내 과제 보고서이며, 물류센터 적용 근거는 없다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f26",
      "claim": "K. 플랫폼 아키텍처·인프라의 41. 플랫폼 아키텍처·외부 API·42. 분산 시스템·통신·컴퓨팅 구조 ↔ G. 계획·최적화의 27. 다중 로봇 경로·교통 관리 — MAPF: Open-RMF 교통 관리는 플릿 어댑터가 예상 경로를 중앙 교통 스케줄에 보고하는 구조다. 그래서 중앙 스케줄을 현장 서버와 클라우드 가운데 어디에 두는지가 단절 때 교통 조율을 계속할 수 있는지를 좌우할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-004"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "중앙 교통 스케줄 보고 구조(f18)를 판단 배치 정책(41. 플랫폼 아키텍처·외부 API 9절)과 대응시킨 추론. 실측 자료는 없다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f27",
      "claim": "K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성 연결 근거: VDA 5050 3.0.0 에서 로봇은 브로커와 연결이 끊겨도 받은 주문 정보를 유지하고, 마지막으로 해제된 노드까지 주문을 수행한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "명세 표현 \"fulfills the order up to the last released node\". 해제되지 않은 호라이즌 구간은 주행하지 않는다(42. 분산 시스템·통신·컴퓨팅 구조 5절). (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "예외·성과",
      "source_unopened": false
    },
    {
      "id": "f28",
      "claim": "K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조 ↔ H. 실행·협업·예외 복구의 29. 명령·작업 실행의 신뢰성: VDA 5050 은 주문·상태를 QoS 0 으로 보내고, 상태를 사건 발생 시와 최대 30초 간격으로 다시 보낸다. 그래서 재연결 뒤 관제는 끊긴 동안의 메시지가 쌓여 오기를 기대하기보다, 다음 상태 메시지로 로봇 상태를 다시 세우고 주문을 갱신해야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-306"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "42. 분산 시스템·통신·컴퓨팅 구조 5절의 [추정]. VDA 5050 이 MQTT 5.0 세션 만료를 어떻게 쓰는지는 미확인이다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "예외·성과",
      "source_unopened": false
    },
    {
      "id": "f29",
      "claim": "K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성 연결 근거: Zhang·Yu·Westerlund(Sensors, 2025-08-14)는 Kubernetes 컨테이너 자동 재시작으로, ROS 2 다중 로봇 시스템이 장애 중에도 UWB 기반 상대 위치 정확도를 유지했다고 보고했다(실험실 결과).",
      "tag": "사실",
      "source_ids": [
        "ref-1039"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "43. 데이터·관측성·배포 8절의 검증된 주장. 현장 적용 사례가 아니라 실험실 결과다.",
      "as_of": "2025-08-14",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f30",
      "claim": "K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성 연결 근거: Open-RMF 저장소 이슈 #224 는 플릿 어댑터가 재시작되면 배정된 작업이 사라진다고 지적한다. 같은 이슈는 작업 로그·백업을 SQLite 에 저장해 복구하는 기능이 별도 풀 리퀘스트로 제안되었다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-374"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "F. 연동 대분류 페이지에 실린 검증된 주장. 현재 배포판 반영 여부는 미확인이다(oq-048). (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f31",
      "claim": "K. 플랫폼 아키텍처·인프라의 41. 플랫폼 아키텍처·외부 API ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성 연결 근거: FogROS2-FT(IROS 2024)는 클라우드 로보틱스의 장애 허용을 다룬다. 여러 클라우드에 둔 복제 서비스로 한 곳에 장애가 나도 응답을 이어 가는 방식이다.",
      "tag": "사실",
      "source_ids": [
        "ref-1031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "41. 플랫폼 아키텍처·외부 API 6·8절이 다중 클라우드 장애 대응의 근거로 든 논문(초록 기준).",
      "as_of": "2024-12",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f32",
      "claim": "K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성 연결 근거: KubeEdge 는 클라우드–엣지 네트워크가 끊겨도 엣지 노드와 애플리케이션이 자율적으로 계속 동작하는 구조를 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-300"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "42. 분산 시스템·통신·컴퓨팅 구조 7절의 검증된 주장. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f33",
      "claim": "K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈: Ocado 는 교통 관리·오케스트레이션 알고리즘 변경을 실제 창고에 적용하기 전에 시뮬레이션·디지털 트윈에서 시험한다고 밝힌다. 또 12개월 동안 창고 운영 270년 분량을 시뮬레이션했다고 밝힌다.",
      "tag": "추정",
      "source_ids": [
        "ref-1044"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 배포 전 검증의 근거로만 쓴다. 시뮬레이션 자체는 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈의 내용이다(43. 데이터·관측성·배포 5절).",
      "as_of": "2025-06-04",
      "site_type": "물류창고",
      "flow_item": "예외·성과",
      "source_unopened": true,
      "vendor_claim": true
    },
    {
      "id": "f34",
      "claim": "K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현 연결 근거: ROS 2 Iron Irwini(2023-05-23)부터 rosbag2 의 기본 저장 형식은 MCAP 이다. rosbag2 는 재생 속도 조절, /clock 발행, 여러 백 파일을 기록 시각순으로 동시에 재생하는 기능을 지원한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1034",
        "ref-831"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "43. 데이터·관측성·배포 6·7절과 I. 설계·시뮬레이션 대분류 연결 조사의 검증된 주장을 합쳤다. 두 출처는 서로 다른 내용을 말하므로 교차 확인이 아니다. (재인용: 2026-10-09-04)",
      "as_of": "2023-05-23",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f35",
      "claim": "K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: 43. 데이터·관측성·배포가 정하는 기록 형식과 보존 기간이 36. 가상 시운전·실제 상황 재현이 재현에 쓸 수 있는 실제 기록의 범위를 정할 것으로 보인다. 이 연결은 지난 기록을 다루는 것이며, 18. 실시간 세계 상태·데이터 일관성의 현재 상태 표현과는 구분된다.",
      "tag": "추정",
      "source_ids": [
        "ref-1034",
        "ref-831"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "기록을 시나리오 사양으로 바꾸는 공개 형식(oq-131)과 텔레메트리·주행 기록 보존 기간 기준(oq-211)은 확인되지 않았다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f36",
      "claim": "K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포 ↔ J. 현장 운영·관제의 37. 관제 화면·실행 기록 연결 근거: Open-RMF 웹 대시보드의 API 서버(rmf-server)는 기본으로 메모리 안의 SQLite 를 쓰고, PostgreSQL·SQLite·MySQL·MariaDB 를 지원한다.",
      "tag": "사실",
      "source_ids": [
        "ref-762"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "J. 현장 운영·관제 대분류 연결 조사의 검증된 주장. 실행 기록을 영속 저장하는 것은 배포 설정의 몫이다. (재인용: 2026-10-09-05) (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f37",
      "claim": "K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포 ↔ J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석 연결 근거: ros2_tracing(IEEE RA-L 2022)은 LTTng 기반의 저부하 추적기로 ROS 2 실행 정보를 모은다. 모든 ROS 2 계측을 켰을 때 메시지 종단 지연 증가는 평균 0.0033 ms 였다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1032"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "저자 실험값이며 독립 재현은 미확인이다(43. 데이터·관측성·배포 8절, J. 현장 운영·관제 연결 조사).",
      "as_of": "2022-07",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f38",
      "claim": "K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포 ↔ J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석: 플랫폼 서비스 쪽 분산 추적(OpenTelemetry)과 ROS 2 런타임 쪽 추적(ros2_tracing)은 서로 다른 계층의 실행 정보를 모은다. 그래서 지연 원인 분석에 두 계층을 함께 쓰려면 작업 식별자로 기록을 잇는 관측성 설계가 필요할 것으로 보인다(oq-210).",
      "tag": "추정",
      "source_ids": [
        "ref-1036",
        "ref-1032"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "43. 데이터·관측성·배포 9절은 작업 단위 추적 문맥 전파를 직접 범위로 본다([추정]). 공개 사례는 확인되지 않았다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f39",
      "claim": "K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포 ↔ J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석 연결 근거: ros2probe(2026-06, 프리프린트)는 관찰 도구가 관찰 대상을 교란하는 문제를 커널 선택 관찰로 줄였다. 관찰 자체의 비용을 따져야 함을 보여 주는 연구다.",
      "tag": "사실",
      "source_ids": [
        "ref-1033"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "43. 데이터·관측성·배포 8절의 검증된 주장(프리프린트).",
      "as_of": "2026-06",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f40",
      "claim": "K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조·43. 데이터·관측성·배포 ↔ L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획 연결 근거: Bruno·Sim·Hagiwara(2026-09, 프리프린트)는 범용 서비스 로봇의 LLM 연쇄 기반 작업 계획에서 로컬 모델과 클라우드 모델을 비교했다. 비교의 동기는 클라우드 API 비용과 지연이었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1043"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "43. 데이터·관측성·배포 8절의 검증된 주장. 언어 모델 호출을 어디에 둘지가 비용·지연 문제임을 보여 준다.",
      "as_of": "2026-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f41",
      "claim": "K. 플랫폼 아키텍처·인프라의 41. 플랫폼 아키텍처·외부 API ↔ L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획 연결 근거: FogROS2(2022-05)는 ROS 2 로봇의 계산 부담이 큰 작업을 클라우드·포그로 옮겨 실행하는 플랫폼이다.",
      "tag": "사실",
      "source_ids": [
        "ref-304"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "41. 플랫폼 아키텍처·외부 API 6·8절의 근거. 로봇 내부 기능의 실행 위치 선택은 로봇 자체 지능 경계의 연계 대상이다(41. 플랫폼 아키텍처·외부 API 9절).",
      "as_of": "2022-05",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f42",
      "claim": "K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조 ↔ M. 안전의 48. 안전·위험 관리 연결 근거: VDA 5050 은 이 문서가 기능·운영·시스템 안전 요구를 정하지 않으며, 안전 표준으로 적용해서는 안 된다고 밝힌다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "G. 계획·최적화 대분류 페이지에 실린 검증된 주장. 관제 통신 계층과 안전 기능을 구분하는 근거로 쓴다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f43",
      "claim": "K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포 ↔ M. 안전의 50. 안전 표준·인증·사고 조사 연결 근거: Winfield 외(2022)의 윤리적 블랙박스 초안 공개 표준은, 사고·아차 사고 조사를 돕기 위해 소셜 로봇의 센서·구동기·제어 결정 데이터를 기록하는 모듈을 제안한다. 이 초안은 단일 로봇을 대상으로 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1360"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "J. 현장 운영·관제 연결 조사에서 확인한 주장. 플릿·플랫폼 수준 기록은 다루지 않는다. (재인용: 2026-10-09-05)",
      "as_of": "2022-05-13",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f44",
      "claim": "K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포 ↔ M. 안전의 50. 안전 표준·인증·사고 조사: 사고 조사에 쓸 플랫폼 수준 실행 기록에는 43. 데이터·관측성·배포 쪽의 보존 기간·무결성 관리가 필요할 것으로 보인다. 하지만 로봇 플랫폼 기록의 보존 기간을 정한 기준은 개인정보 접속기록 규정 밖에서는 확인되지 않았다(oq-211).",
      "tag": "추정",
      "source_ids": [
        "ref-1360",
        "ref-766"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "단일 로봇 블랙박스 초안(f43)과 접속기록 보관 고시(f47)를 플랫폼 기록에 옮긴 추론.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f45",
      "claim": "K. 플랫폼 아키텍처·인프라의 41. 플랫폼 아키텍처·외부 API ↔ N. 보안·개인정보의 51. 인증·권한·격리 연결 근거: Open-RMF API 서버(rmf-server)는 OpenID Connect 신원 공급자로 인증하고, 권한은 앱 안에서 역할·동작·자원 권한 그룹으로 판정한다. 관리자는 모든 그룹에서 모든 동작을 할 수 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-762"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "J. 현장 운영·관제 연결 조사의 검증된 주장. 현재 모든 자원은 빈 문자열 기본 그룹에 들어간다. (재인용: 2026-10-09-05) (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f46",
      "claim": "K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조 ↔ N. 보안·개인정보의 51. 인증·권한·격리·52. 통신 보호·위협 관리·감사 연결 근거: ROS 2 는 DDS 보안 규격의 인증(PKI)·접근통제(거버넌스·권한 파일)·암호화 플러그인을 쓴다. Open-RMF 문서는 SROS 2 인클레이브로 RMF 구성요소의 권한을 나누고, 웹 대시보드에는 TLS·OIDC 인증을 더한다고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-009",
        "ref-405"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "F. 연동 대분류 페이지에 실린 검증된 주장. 두 출처는 서로 다른 계층을 설명하므로 교차 확인이 아니다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f47",
      "claim": "K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포 ↔ N. 보안·개인정보의 53. 개인정보·영상 데이터 연결 근거: 개인정보보호위원회 고시 「개인정보의 안전성 확보조치 기준」(2023-6호, 2023-09-22 시행 판)은 접속기록의 보관과 점검에 관한 조항을 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-766"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "43. 데이터·관측성·배포 9절이 보존 정책의 국내 근거로 든 고시. 현행 조문이 같은지는 미확인이다(oq-214).",
      "as_of": "2023-09-22",
      "site_type": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f48",
      "claim": "K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포 ↔ O. 검증·도입·수명주기의 57. 자산·소프트웨어 수명주기 관리 연결 근거: Mender 는 임베디드 리눅스 장치용 오픈소스 무선(OTA) 업데이트 도구다. 이미지 기반 A/B 업데이트와 실패 시 롤백을 지원한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1040"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "43. 데이터·관측성·배포 6·7절이 배포 도구로 든 저장소 README. 로봇 운영체제·펌웨어 무선 업데이트는 연계 대상이다(43. 데이터·관측성·배포 9절). (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f49",
      "claim": "K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포 ↔ O. 검증·도입·수명주기의 57. 자산·소프트웨어 수명주기 관리: 43. 데이터·관측성·배포의 배포·롤백 자동화가 57. 자산·소프트웨어 수명주기 관리의 버전 관리와 맞물릴 것으로 보인다. 다만 운행 중인 로봇 작업을 끊지 않고 현장 서버·로봇에 순차 배포하고 되돌리는 시점·기준을 공개한 로봇 관제 제품이나 연구는 확인되지 않았다(oq-213).",
      "tag": "추정",
      "source_ids": [
        "ref-1040",
        "ref-1039"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "A/B 롤백 도구(f48)와 컨테이너 자동 재시작 실험(f29)을 수명주기 관리와 대응시킨 추론. 두 출처 모두 운행 중 작업과의 관계는 다루지 않는다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f50",
      "claim": "연계 대상: K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포 ↔ P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스: 접속기록 보관 같은 법적 의무의 해석과 적용 판단은 59. 법·규제·보험·라이선스와 운영 사업자의 몫으로 보인다. ROP 는 그 기준에 맞춰 기록을 수집·보존·점검하는 기능을 제공하는 쪽으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-766"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "43. 데이터·관측성·배포 9절의 보존 정책 범위를 법규 해석과 분리한 추론. 현행 조문은 미확인이다(oq-214).",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f51",
      "claim": "K. 플랫폼 아키텍처·인프라의 41. 플랫폼 아키텍처·외부 API ↔ Q. 현장 유형별 적용의 63. 병원·의료 연결 근거: 창이종합병원 CHART 의 공공 의료기관용 로봇 미들웨어 RoMi-H 는 네 영역이 역할을 나누는 구조다. 기계(하드웨어 추상화)·제어(항법·위치 추정)·중앙(플릿 관리, 로봇–기반 시설 통신)·통합(모바일·웹 앱·ICT 시스템용 API) 영역이며, OMG DDS 를 쓴다.",
      "tag": "사실",
      "source_ids": [
        "ref-937"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "41. 플랫폼 아키텍처·외부 API 5절 병원 사례. 2019-10-31 ROSCon 2019 에서 공식 출범했다. 특정 병원의 배치 결과가 아니라 미들웨어 구조다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": "병원",
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f52",
      "claim": "K. 플랫폼 아키텍처·인프라의 41. 플랫폼 아키텍처·외부 API ↔ Q. 현장 유형별 적용의 62. 제조 공장 연결 근거: Brorsson 외(2025-12)는 사내 물류 이동 로봇의 판단을 세 층에 나눠 두는 기준 아키텍처를 제시했다. 설비에 단 외부 센서·계산 자원, 현장 클라우드, 로봇 온보드 자율이며, 이를 대형 상용차 제조 현장 실배치로 보였다.",
      "tag": "사실",
      "source_ids": [
        "ref-308"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "41. 플랫폼 아키텍처·외부 API 5절 제조 공장 사례(초록 기준). 처리량·시간·비용 수치는 확인하지 못했다.",
      "as_of": "2025-12",
      "site_type": "제조 공장",
      "flow_item": "수행 자원",
      "source_unopened": true
    },
    {
      "id": "f53",
      "claim": "K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조 ↔ Q. 현장 유형별 적용의 61. 물류창고: CJ대한통운은 2023-04 이천 2풀필먼트센터에 물류센터 최초로 5G 특화망 이음5G 를 구축했다고 발표했다. 기존 와이파이의 채널 간섭·지연을 생산성 저하 원인으로 들었다.",
      "tag": "추정",
      "source_ids": [
        "ref-307"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 와이파이 대비 약 1,000배 빠른 속도를 주장했다. 발표 당시 로봇·설비 적용은 시범 뒤 확대 계획이었다(42. 분산 시스템·통신·컴퓨팅 구조 3절).",
      "as_of": "2023-04",
      "site_type": "물류창고",
      "flow_item": "제약",
      "source_unopened": true,
      "vendor_claim": true
    },
    {
      "id": "f54",
      "claim": "K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조 ↔ Q. 현장 유형별 적용의 63. 병원·의료 연결 근거: 고려대학교 구로병원 약품 배송 로봇 실증(2025-06, 비응급 임무 122건)의 실패 14건은 승강기 막힘 8건, 복도 주행 4건, 통신 오류 2건이었다.",
      "tag": "사실",
      "source_ids": [
        "ref-943"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "43. 데이터·관측성·배포 5절의 저자 보고값. 성공률 분모 불일치는 열린 질문 oq-215 에 있다.",
      "as_of": "2026-03-31",
      "site_type": "병원",
      "flow_item": "예외·성과",
      "source_unopened": true
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
      "accessed": "2026-10-09",
      "summary": "원문 미열람. Open-RMF 의 작업·교통 조율, 플릿 어댑터, 설비 연동 구조 개요.",
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
      "accessed": "2026-10-09",
      "summary": "원문 미열람. ROS 2 의 DDS 보안 규격 인증·접근통제·암호화 플러그인 통합 설계.",
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
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 관제–이동로봇 통신 명세(3.0.0). 무선망 전제, MQTT QoS, 연결 단절 시 동작, 안전 표준 아님을 명시한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-045",
      "org": "GS1",
      "title": "gs1/EPCIS — Ontology/EPCIS.ttl (EPCIS ontology 2.0)",
      "published": "2021-09-30",
      "url": "https://github.com/gs1/EPCIS/blob/master/Ontology/EPCIS.ttl",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. EPCIS 2.0 온톨로지. 발생 시각·기록 시각·UTC 차이를 구분한다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
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
      "accessed": "2026-10-09",
      "summary": "원문 미열람. VDA 5050 상태 메시지 JSON 스키마(시각, 적재물, 위치추정 품질 등).",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-105",
      "org": "Open Robotics (open-rmf)",
      "title": "fleet_adapter_template — fleet_adapter_template/config.yaml",
      "published": null,
      "url": "https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. Open-RMF 플릿 어댑터 템플릿 설정(task_capabilities, actions, 충전 설정, 기준 좌표).",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-148",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. Open-RMF 로봇 상태 스키마(상태 값, 배터리, 문제 목록, 밀리초 시각).",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-251",
      "org": "Open Robotics",
      "title": "Mobile Robot Fleets (integration_fleets) - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/integration_fleets.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 플릿 연동의 제어 수준(전체 제어·신호등·읽기 전용) 설명.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-282",
      "org": "Open Robotics (ROS 2 Documentation)",
      "title": "Quality of Service settings — ROS 2 Documentation: Jazzy",
      "published": null,
      "url": "https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. ROS 2 QoS 정책(기한·생존성 등) 설명.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-287",
      "org": "Eclipse Foundation (eclipse-sparkplug GitHub)",
      "title": "Sparkplug Specification — Chapter 5 Operational Behavior (Sparkplug_5_Operational_Behavior.adoc)",
      "published": null,
      "url": "https://github.com/eclipse-sparkplug/sparkplug/blob/master/specification/src/main/asciidoc/chapters/Sparkplug_5_Operational_Behavior.adoc",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. Sparkplug 운영 동작. 노드 종료(NDEATH) 뒤 지표의 STALE 표시.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-300",
      "org": "KubeEdge (CNCF, kubeedge GitHub)",
      "title": "KubeEdge — README",
      "published": null,
      "url": "https://github.com/kubeedge/kubeedge",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 클라우드–엣지 단절 중 엣지 자율 동작을 지원하는 쿠버네티스 엣지 플랫폼.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-304",
      "org": "Ichnowski, J., Chen, K. 외(UC Berkeley AUTOLAB)",
      "title": "FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2",
      "published": "2022-05",
      "url": "https://arxiv.org/abs/2205.09778",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. ROS 2 로봇의 계산을 클라우드·포그로 옮기는 플랫폼.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-306",
      "org": "OASIS",
      "title": "MQTT Version 5.0",
      "published": "2019-03",
      "url": "https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. MQTT 5.0 메시징 프로토콜 표준.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-307",
      "org": "CJ대한통운",
      "title": "CJ대한통운, 물류센터 최초 5G 개통 … 속도 1000배 빨라진다",
      "published": "2023-04",
      "url": "https://www.cjlogistics.com/ko/newsroom/news/NR_00001046",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 이천 2풀필먼트센터 5G 특화망 구축 보도자료(벤더 주장 포함).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-308",
      "org": "Brorsson, E. 외",
      "title": "Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives",
      "published": "2025-12",
      "url": "https://arxiv.org/abs/2512.15215",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 설비 센서·현장 클라우드·온보드 자율의 3층 기준 아키텍처와 대형 상용차 제조 현장 실배치.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-309",
      "org": "FreightWaves",
      "title": "Warehouses face $100K-hour downtime risk as cloud outages mount",
      "published": null,
      "url": "https://www.freightwaves.com/news/warehouses-face-100k-hour-downtime-risk-hybrid-wms",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 하이브리드 WMS 판매사 조사를 인용한 창고 운영 중단 비용 기사.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-310",
      "org": "Gilbert, S., & Lynch, N.",
      "title": "Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services",
      "published": "2002-06",
      "url": "https://dl.acm.org/doi/10.1145/564585.564601",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. CAP 정리의 증명 논문.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-374",
      "org": "Open Robotics (open-rmf/rmf_ros2 GitHub)",
      "title": "Task recovery when fleet adapter get restarted · Issue #224 · open-rmf/rmf_ros2",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_ros2/issues/224",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 플릿 어댑터 재시작 시 작업 유실 문제와 SQLite 백업 제안을 다룬 이슈.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-401",
      "org": "KISTI ScienceON 수록 국가R&D 과제 보고서(수행기관 미확인)",
      "title": "클라우드에 연결된 개별 로봇 및 로봇그룹의 작업 계획 기술 개발",
      "published": null,
      "url": "https://scienceon.kisti.re.kr/srch/selectPORSrchReport.do?cn=TRKO202400003952",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 클라우드 연결 로봇·로봇그룹 작업 계획 국내 과제 보고서.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
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
      "summary": "원문 미열람. SROS 2 인클레이브, 대시보드 TLS·OIDC 등 Open-RMF 보안 구성 설명.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-493",
      "org": "Lott, J., & Honary, V.(University of San Diego)",
      "title": "Decentralized Multi-Robot Task Allocation Under Degraded Communication: A Benchmark of Performance, Reliability, and Computation",
      "published": "2026-09",
      "url": "https://arxiv.org/abs/2609.13711",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 통신 저하 조건에서 분산 작업 배정기 6종 비교 벤치마크(프리프린트).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-762",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf-web — packages/api-server/README.md",
      "published": null,
      "url": "https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. rmf-server 의 데이터베이스 설정과 OIDC 인증·권한 그룹 설명.",
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
      "summary": "원문 미열람. 개인정보 처리자의 안전성 확보조치 기준 고시(접속기록 보관·점검 조항 포함, 2023-6호 기준).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-831",
      "org": "ROS 2 (ros2/rosbag2 GitHub)",
      "title": "rosbag2 — README (Recording and playback of ROS 2 communications)",
      "published": null,
      "url": "https://github.com/ros2/rosbag2",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. ROS 2 통신 기록·재생 도구 README(재생 속도, /clock, 다중 백 파일 재생).",
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
      "summary": "원문 미열람. Open-RMF REST API 를 MCP 도구로 노출하는 Nayantra 발표 안내문.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-937",
      "org": "Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART)",
      "title": "ROMI-H | Changi General Hospital",
      "published": null,
      "url": "https://www.cgh.com.sg/chart/projects/romi-h",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 공공 의료기관용 로봇 미들웨어 RoMi-H 의 네 영역 구조와 출범 이력.",
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
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 구로병원 약품 배송 로봇 122건 실증. 로봇·승강기 로그 기반 실패 분석.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1023",
      "org": "NAVER Corp.",
      "title": "로보틱스 l NAVER Corp.",
      "published": null,
      "url": "https://www.navercorp.com/tech/robotics",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 네이버 ARC(brain·eye·mind) 클라우드 로봇 운영 소개(벤더 주장).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1024",
      "org": "AsyncAPI Initiative",
      "title": "AsyncAPI Specification 3.1.0",
      "published": null,
      "url": "https://www.asyncapi.com/docs/reference/specification/v3.1.0",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 메시지 기반 API 를 기술하는 명세.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1025",
      "org": "OpenAPI Initiative",
      "title": "OpenAPI Specification v3.1.0",
      "published": "2021-02-15",
      "url": "https://spec.openapis.org/oas/v3.1.0",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. HTTP API 를 언어와 무관하게 기술하는 인터페이스 명세.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1030",
      "org": "Locus Robotics",
      "title": "Seamless Integrations with LocusOne Robotics",
      "published": null,
      "url": "https://locusrobotics.com/locusone/automated-warehouse-software/integrations",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. LocusONE 의 WMS 연동 소개(벤더 주장).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1031",
      "org": "Chen, K., Hari, K., Chung, T. 외 (IROS 2024, arXiv)",
      "title": "FogROS2-FT: Fault Tolerant Cloud Robotics",
      "published": "2024-12",
      "url": "https://arxiv.org/abs/2412.05408",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 다중 클라우드 복제를 이용한 클라우드 로보틱스 장애 허용 연구.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1032",
      "org": "Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L, arXiv)",
      "title": "ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2",
      "published": "2022-07",
      "url": "https://arxiv.org/abs/2201.00393",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. LTTng 기반 ROS 2 저부하 추적 도구 모음.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1033",
      "org": "Yu, J., Lee, S., Choi, Y., & Park, K.-J. (arXiv)",
      "title": "ros2probe: Non-intrusive, Kernel-selective Observability for Robot Operating System 2 Middleware",
      "published": "2026-06",
      "url": "https://arxiv.org/abs/2606.10746",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 관찰 교란을 줄이는 커널 선택형 ROS 2 관측 도구(프리프린트).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1034",
      "org": "Open Robotics (ROS 2 Documentation)",
      "title": "Iron Irwini (iron)",
      "published": "2023-05-23",
      "url": "https://docs.ros.org/en/rolling/Releases/Release-Iron-Irwini.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. ROS 2 Iron 릴리스 노트(rosbag2 기본 저장 형식 MCAP).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1036",
      "org": "OpenTelemetry (CNCF)",
      "title": "Specification Status Summary",
      "published": null,
      "url": "https://opentelemetry.io/docs/specs/status/",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. OpenTelemetry 명세 구성요소별 안정성 상태 요약.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1037",
      "org": "OpenTelemetry (open-telemetry/semantic-conventions-genai)",
      "title": "semantic-conventions-genai/docs/gen-ai/gen-ai-token-metrics.md",
      "published": null,
      "url": "https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 생성형 AI 클라이언트 토큰 사용량 지표 의미 규약(개발 단계).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1039",
      "org": "Zhang, J., Yu, X., & Westerlund, T. (Sensors 25(16):5067)",
      "title": "Enhancing the Resilience of ROS 2-Based Multi-Robot Systems with Kubernetes: A Case Study on UWB-Based Relative Positioning",
      "published": "2025-08-14",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12390455/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. Kubernetes 자동 재시작으로 ROS 2 다중 로봇 시스템 복원력을 시험한 실험실 연구.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1040",
      "org": "Northern.tech (mendersoftware)",
      "title": "mender — README",
      "published": null,
      "url": "https://github.com/mendersoftware/mender",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 임베디드 리눅스용 오픈소스 OTA 업데이트 도구(A/B 업데이트·롤백).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1041",
      "org": "FinOps Foundation",
      "title": "FinOps Phases",
      "published": null,
      "url": "https://www.finops.org/framework/phases/",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. FinOps 의 알리기·최적화·운영 단계 설명.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1042",
      "org": "FinOps Foundation",
      "title": "Introducing FOCUS 1.2: SaaS/PaaS Support, Invoice Reconciliation, and more",
      "published": "2025-06-03",
      "url": "https://www.finops.org/insights/focus-1-2-available/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 클라우드 청구 데이터 표준 FOCUS 1.2 발표 글(명세 본문 아님).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1043",
      "org": "Bruno, L. D. M., Sim, J., & Hagiwara, Y. (arXiv)",
      "title": "Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots",
      "published": "2026-09",
      "url": "https://arxiv.org/abs/2609.29043",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 서비스 로봇 LLM 연쇄 작업 계획에서 로컬·클라우드 모델 비교(프리프린트).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1044",
      "org": "Ocado Group",
      "title": "Ocado's digital twins and simulations: driving efficiencies and innovation at scale",
      "published": "2025-06-04",
      "url": "https://www.ocadogroup.com/newsroom/stories/digital-twins-and-simulations",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. Ocado 의 배포 전 시뮬레이션·디지털 트윈 활용 소개(벤더 주장).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1360",
      "org": "Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv)",
      "title": "An Ethical Black Box for Social Robots: a draft Open Standard",
      "published": "2022-05-13",
      "url": "https://arxiv.org/abs/2205.06564",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 사고 조사를 위한 소셜 로봇 데이터 기록 장치의 초안 공개 표준.",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/platform-architecture-and-infrastructure/index.md",
      "sections": [
        "5. 다른 대분류와의 연결"
      ],
      "rationale": "category_link: '다른 대분류와의 연결' 절만 patches 로 채운다. 대분류별 근거는 다음과 같다. A. 기획·사업: f1·f2·f3·f4(벤더 주장)·f5(벤더 주장) / B. 로봇 온톨로지: f6·f7·f8 / C. 채팅 기반 구성·운영: f9·f10·f11·f12 — 분류 원문 4장 주석(업무 지시는 25·26번)과 함께 읽는다 / D. 공간·지도 모델: f13(벤더 주장, oq-206) / E. 사물·사람·실시간 상태: f14·f15·f16 / F. 연동: f17·f18·f19·f20(벤더 주장)·f21·f22·f23 / G. 계획·최적화: f24·f25·f26 / H. 실행·협업·예외 복구: f27·f28·f29·f30·f31·f32 / I. 설계·시뮬레이션: f33(벤더 주장)·f34·f35 / J. 현장 운영·관제: f36·f37·f38·f39 / L. AI·학습 기술: f40·f41 / M. 안전: f42·f43·f44 / N. 보안·개인정보: f45·f46·f47 / O. 검증·도입·수명주기: f48·f49 / P. 거버넌스·법규·사회: f50(연계 대상) / Q. 현장 유형별 적용: f51(병원)·f52(제조 공장)·f53(물류창고, 벤더 주장)·f54(병원), 기타 현장은 f5·f13. 추정·low(f3·f7·f8·f10·f12·f16·f19·f23·f25·f26·f35·f38·f44·f49·f50)는 단정하지 말고 쓴다. 벤더 주장(f4·f5·f13·f20·f33·f53)에는 '벤더 주장'을 병기한다. 18. 실시간 세계 상태·데이터 일관성(f14·f15, 현재 상태)과 34. 시뮬레이션·예측용 디지털 트윈(f33, 가정한 미래)은 구분해 쓴다. 아직 다루지 않은 연결은 P. 거버넌스·법규·사회의 58·60, Q. 현장 유형별 적용의 64·65·66, O. 검증·도입·수명주기의 55·56, J. 현장 운영·관제의 39·40, L. AI·학습 기술의 45·46이다. 다음 실행 후보: 42. 분산 시스템·통신·컴퓨팅 구조 10절에 C·L·M 연결(f40·f42) 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "MQTT 유언 메시지",
      "term_en": "MQTT Last Will (Will Message)",
      "definition": "MQTT 클라이언트가 접속할 때 브로커에 맡겨 두고, 연결이 예기치 않게 끊기면 브로커가 대신 발행하는 메시지다. VDA 5050 은 이를 써서 로봇의 연결 끊김(CONNECTION_BROKEN)을 알린다."
    },
    {
      "term_ko": "A/B 업데이트",
      "term_en": "A/B Update (Dual Partition Update with Rollback)",
      "definition": "장치에 두 개의 시스템 영역을 두고 쓰지 않는 쪽에 새 이미지를 설치한 뒤 전환하며, 실패하면 이전 영역으로 되돌리는 소프트웨어 업데이트 방식이다."
    }
  ],
  "open_questions_new": [
    "플랫폼 관제 서비스를 다중 클라우드 복제나 컨테이너 자동 재시작으로 운영하면서, 재시작 뒤 진행 중인 로봇 작업 상태를 잃지 않고 이어 간 공개 사례나 구성이 있는가? | 관련 영역: 43. 데이터·관측성·배포, 41. 플랫폼 아키텍처·외부 API, 32. 예외 복구·재계획·업무 연속성 | 근거: f30 | 종류: 일반",
    "로봇 오케스트레이션 플랫폼의 외부 API 를 OpenAPI·AsyncAPI 로 기술해 연동 적합성 시험의 기준으로 쓴 공개 시험 도구나 절차가 있는가? | 관련 영역: 41. 플랫폼 아키텍처·외부 API, 21. 상호운용 표준·적합성 | 근거: f23 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 44,
    "cross_checked_count": 0,
    "unverified": [
      "이번 재실행은 형식 수정 재실행이다. 직전 브리프가 프롬프트에 없어 입력의 게시 페이지·대분류 페이지·이전 브리프(2026-10-09-04, 2026-10-09-05)의 검증된 주장으로 브리프를 다시 구성했다. 모든 출처를 이번에 다시 열지 않았다(fetched false)",
      "f31 FogROS2-FT 의 복제 방식 세부는 41. 플랫폼 아키텍처·외부 API 페이지의 '다중 클라우드 장애 대응' 요약 기준이며 초록 문구와의 대조는 하지 않았다",
      "f37 ros2_tracing 0.0033 ms 는 저자 실험값이며 독립 재현은 미확인이다",
      "f47 접속기록 보관·점검 조항의 구체 기간과 현행 조문은 미확인이다(oq-214)",
      "f54 구로병원 성공률 분모 불일치는 미해결이다(oq-215)",
      "P. 거버넌스·법규·사회의 58. 다사업자 책임·계약·데이터와 K. 플랫폼 아키텍처·인프라를 잇는 근거(API 변경 정책 책임 등)는 찾지 못했다(oq-207)"
    ],
    "scope_violations": [
      "f13·f41: 위치 추정·로봇 내부 계산의 클라우드 배치는 원문 19장 로봇 자체 지능 경계의 연계 대상이다. 제품 전략 사례·연구 근거로만 쓰고 ROP 직접 범위로 서술하지 않았다",
      "f20: 주문 최적화 판단은 WMS·로봇 공급사 몫이고, ROP 는 연동 인터페이스만 다룬다",
      "f21: 승강기 통신 로그 생성은 시설·설비 제어 경계의 연계 대상이다. ROP 몫은 수집·결합으로 한정했다",
      "f48: 로봇 운영체제·펌웨어 무선 업데이트는 연계 대상이다",
      "f50: 법적 보관 의무의 해석은 외부 연계 대상이라 claim 을 '연계 대상: '으로 시작했다",
      "f53: 무선망(5G 특화망) 구축은 ROP 가 소유하지 않는 통신 기반 연계 대상에 가깝다",
      "f42: VDA 5050 은 안전 표준이 아니므로 통신 계층과 안전 기능을 구분하는 근거로만 썼다"
    ],
    "budget_used": {
      "queries": 0,
      "sources": 0
    },
    "limits": "재실행 1회차. 반려 사유 1(스키마 불일치 — f49 가 벤더 문서만 근거로 한 [사실]인데 vendor_claim 표시 없음): 지시에 따라 새로 조사하지 않고 형식만 고쳤다. 다만 직전 반환값이 프롬프트에 들어 있지 않아 같은 id·내용을 그대로 유지할 수 없었다. 그래서 입력에 있는 게시 페이지(41·42·43, A·B·E·F·G 대분류 페이지)와 이전 브리프(2026-10-09-04, 2026-10-09-05)의 검증된 주장·각주만으로 브리프 전체를 다시 구성했다. 그 결과 finding 번호와 내용은 직전 브리프와 다를 수 있다. 벤더 문서·벤더 조사 인용에 기댄 기능·성능 주장(f4·f5·f13·f20·f33·f53)은 모두 vendor_claim true, 태그 추정, evidence_excerpt 첫머리 '벤더 주장: '으로 표시했다. 벤더 문서만 근거로 한 [사실]은 없다. 새 f49 는 비벤더 출처의 [추정]이다. 이번 재실행의 검색은 0회, 신규 출처는 0건이다(예약 구간 ref-1389~ref-1418 미사용). 재사용 출처 44건은 모두 이번에 다시 열지 않았다. 그래서 fetched false, source_unopened true 로 두고 신뢰도는 medium 이하로 했다. 교차 확인은 0건이다. web_fetch_available: true · fetch_mode full 이었으나 형식 수정 재실행이라 쓰지 않았다. 현장 유형 근거는 물류창고(f4·f19·f20·f33·f53)·제조 공장(f52)·병원(f21·f51·f54)·기타(f5·f13)이고, 상업 시설·가정·실외는 없다. L. AI·학습 기술 연결(f40·f41)은 적용 대상인 44. 로봇 기반 모델·언어 모델 계획과 함께 제안했다. 18. 실시간 세계 상태·데이터 일관성(현재 상태)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래)을 섞지 않았다(f35 에 구분 명시). 대분류 페이지 절 번호는 제목 순서(핵심 질문·개요·세부 연구영역·핵심 포인트·다른 대분류와의 연결)에 따라 '5'로 매겼다 [가정]. 열린 질문 oq-206·oq-207·oq-209·oq-210·oq-211·oq-212·oq-213·oq-214·oq-267 은 부분 근거만 더했고 해결 제안은 없다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음."
  }
}
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 43건 / 전체 1242건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 2026-09-25 | 예 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 2026-09-25 | 예 |
| ref-227 | Mobile Industrial Robots(MiR) | MiR Fleet Enterprise Documentation Version 1.2 (en) — 유통사(jk.de) 게재본 | 2025-01 | https://jk.de/media/a2/50/ce/1738939330/mir_fleet_enterprise_documentation_1.2_en.pdf?ts=1738939330 | 2026-09-25 | 아니오 |
| ref-256 | Open Robotics (open-rmf) | free_fleet — README (A free fleet management system) | 미확인 | https://github.com/open-rmf/free_fleet | 2026-09-25 | 예 |
| ref-300 | KubeEdge (CNCF, kubeedge GitHub) | KubeEdge — README | 미확인 | https://github.com/kubeedge/kubeedge | 2026-09-25 | 예 |
| ref-301 | Microsoft | Operate Azure IoT Edge devices offline | 2026-03-02 | https://learn.microsoft.com/en-us/azure/iot-edge/offline-capabilities | 2026-09-25 | 예 |
| ref-302 | Open Robotics (open-rmf) | rmf-web — README | 미확인 | https://github.com/open-rmf/rmf-web | 2026-09-25 | 예 |
| ref-303 | NIST | NIST Special Publication (SP) 500-325, Fog Computing Conceptual Model | 2018-03 | https://csrc.nist.gov/pubs/sp/500/325/final | 2026-09-25 | 아니오 |
| ref-304 | Ichnowski, J., Chen, K. 외(UC Berkeley AUTOLAB) | FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2 | 2022-05 | https://arxiv.org/abs/2205.09778 | 2026-09-25 | 아니오 |
| ref-306 | OASIS | MQTT Version 5.0 | 2019-03 | https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html | 2026-09-25 | 아니오 |
| ref-307 | CJ대한통운 | CJ대한통운, 물류센터 최초 5G 개통 … 속도 1000배 빨라진다 | 2023-04 | https://www.cjlogistics.com/ko/newsroom/news/NR_00001046 | 2026-09-25 | 아니오 |
| ref-308 | Brorsson, E. 외 | Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives | 2025-12 | https://arxiv.org/abs/2512.15215 | 2026-09-25 | 아니오 |
| ref-309 | FreightWaves | Warehouses face $100K-hour downtime risk as cloud outages mount | 미확인 | https://www.freightwaves.com/news/warehouses-face-100k-hour-downtime-risk-hybrid-wms | 2026-09-25 | 아니오 |
| ref-310 | Gilbert, S., & Lynch, N. | Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services | 2002-06 | https://dl.acm.org/doi/10.1145/564585.564601 | 2026-09-25 | 아니오 |
| ref-311 | ETRI Journal 게재 논문(Jun 외, 한국전자통신연구원 발행) | Ultra-low-latency services in 5G systems: A perspective from 3GPP standards | 2020 | https://onlinelibrary.wiley.com/doi/full/10.4218/etrij.2020-0200 | 2026-09-25 | 아니오 |
| ref-762 | Open Robotics (open-rmf) | rmf-web — packages/api-server/README.md | 미확인 | https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md | 2026-09-25 | 예 |
| ref-766 | 국가법령정보센터(개인정보보호위원회 고시) | 개인정보의 안전성 확보조치 기준 | 미확인 | https://www.law.go.kr/admRulLsInfoP.do?chrClsCd=010202&admRulSeq=2100000229672 | 2026-09-25 | 아니오 |
| ref-774 | Mobile Industrial Robots(MiR) | MiR Fleet | 미확인 | https://mobile-industrial-robots.com/products/software/mir-fleet | 2026-09-25 | 아니오 |
| ref-870 | 로봇신문 | [기업 최전선을 가다-클로봇] 로봇 소프트웨어로 쓰는 ‘피지컬 AI’ 시대의 서막 | 2025-11-09 | https://www.irobotnews.com/news/articleView.html?idxno=43274 | 2026-09-29 | 예 |
| ref-937 | Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART) | ROMI-H | Changi General Hospital | 미확인 | https://www.cgh.com.sg/chart/projects/romi-h | 2026-09-29 | 예 |
| ref-943 | Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 2026-03-31 | https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/ | 2026-09-29 | 예 |
| ref-1023 | NAVER Corp. | 로보틱스 l NAVER Corp. | 미확인 | https://www.navercorp.com/tech/robotics | 2026-09-30 | 예 |
| ref-1024 | AsyncAPI Initiative | AsyncAPI Specification 3.1.0 | 미확인 | https://www.asyncapi.com/docs/reference/specification/v3.1.0 | 2026-09-30 | 예 |
| ref-1025 | OpenAPI Initiative | OpenAPI Specification v3.1.0 | 2021-02-15 | https://spec.openapis.org/oas/v3.1.0 | 2026-09-30 | 예 |
| ref-1026 | 뉴스핌 | 카카오모빌리티, 로봇-인프라-사용자 연결 '플랫폼 생태계' 구축한다 | 2026-05-13 | https://www.newspim.com/news/view/20260512001077 | 2026-09-30 | 예 |
| ref-1027 | Singhal, A., Kejriwal, N., Pallav, P., Choudhury, S., Sinha, R., & Kumar, S. (arXiv) | Managing a Fleet of Autonomous Mobile Robots (AMR) using Cloud Robotics Platform | 2017-06 | https://arxiv.org/abs/1706.08931 | 2026-09-30 | 예 |
| ref-1028 | Open Robotics (open-rmf) | rmf_api_msgs — README | 미확인 | https://github.com/open-rmf/rmf_api_msgs | 2026-09-30 | 예 |
| ref-1029 | InOrbit | Contents — InOrbit Developer Portal | 미확인 | https://developer.inorbit.ai/docs | 2026-09-30 | 예 |
| ref-1030 | Locus Robotics | Seamless Integrations with LocusOne Robotics | 미확인 | https://locusrobotics.com/locusone/automated-warehouse-software/integrations | 2026-09-30 | 예 |
| ref-1031 | Chen, K., Hari, K., Chung, T. 외 (IROS 2024, arXiv) | FogROS2-FT: Fault Tolerant Cloud Robotics | 2024-12 | https://arxiv.org/abs/2412.05408 | 2026-09-30 | 예 |
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

### docs/glossary/index.md (요약: 용어 346개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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

### docs/open-questions.md (요약: 대상 영역 [41, 42, 43] 에 걸린 16건 / 전체 294건)

```markdown
- oq-035 [열림] 상태 보고 주기와 시각 체계가 다른 로봇(VDA 5050 최소 30초 주기의 ISO 8601 시각, Open-RMF 밀리초 시각)이 섞일 때 공통 세계 상태의 시각 동기화 방식과 허용 시계 오차를 규정한 자료나 사례가 있는가? (영역 18, 20, 42)
- oq-038 [열림] 외부망이 끊겨 클라우드 WMS 와 단절된 동안 현장 ROP 가 이미 받은 주문·작업을 어디까지 계속 실행하고, 재연결 뒤 재고·완료 기록을 어떻게 맞추는지 정한 국내 물류센터 운영 기준이나 사례가 있는가? (영역 23, 32, 42)
- oq-039 [열림] 물류센터 로봇 관제 통신(와이파이·5G 특화망)에서 명령·상태 메시지의 허용 지연·손실률·로밍 중단 시간을 정한 표준이나 공개 측정 자료가 있는가? (영역 20, 42)
- oq-040 [열림] 여러 거점의 로봇 운영을 한곳에서 관리할 때 거점별 현장 서버와 중앙 클라우드 사이 역할 분담과 데이터 동기화를 공개한 오픈소스 구성이나 사례가 있는가? (영역 35, 42)
- oq-083 [열림] 현장 서버·클라우드·로봇 사이 통신이 나빠질 때 물류센터의 작업 배정을 중앙 방식으로 유지할지 분산 방식으로 전환할지 정한 기준이나 실측 자료가 있는가? (영역 25, 42)
- oq-206 [열림] 네이버 ARC 처럼 위치 추정·이동 계획까지 클라우드에서 하는 구조에서 클라우드 연결이 끊기면 로봇과 현장 서버가 어디까지 계속 동작하는지 공개한 자료나 사례가 있는가? (영역 41, 42)
- oq-207 [열림] 로봇 관제 플랫폼의 외부 API 버전 관리와 하위 호환(주 버전 표기, 폐기 예고 기간) 정책을 공개한 오픈소스·제품 사례가 있는가? (영역 41, 57)
- oq-208 [열림] 로봇 플랫폼이 외부로 내보내는 웹훅·이벤트 스트림의 전달 보장(재시도, 순서, 중복 제거)을 정한 공통 기준이나 제품 문서가 있는가? (영역 41, 29)
- oq-209 [열림] 국내에 클라우드 로봇·이기종 로봇 통합관제 플랫폼의 참조 구조나 외부 API 를 정한 TTA·KS 표준이 있는가? (영역 41, 21)
- oq-210 [열림] 서로 다른 제조사 로봇의 기록(MCAP·제조사 로그)과 플랫폼 서비스의 분산 추적을 하나의 작업 식별자로 이어 원인 분석에 쓴 공개 사례나 표준이 있는가? (영역 43, 38)
- oq-211 [열림] 로봇 플랫폼이 수집하는 텔레메트리·주행 기록·영상의 보존 기간을 정한 국내 기준이나 운영 사례가 개인정보 접속기록 규정 밖에도 있는가? (영역 43, 53)
- oq-212 [열림] 개발 단계인 토큰 지표의 이름(gen_ai.client.inference.usage.* 와 다른 문서의 gen_ai.client.token.usage)이 바뀌었는지 미확인인데, 언어 모델 호출 비용 계측을 안정 판이 나오기 전까지 어떤 기준으로 고정할 것인가? (영역 43, 13)
- oq-213 [열림] 운행 중인 로봇 작업을 끊지 않고 현장 서버·로봇에 플랫폼 소프트웨어를 순차 배포하고 되돌리는 시점·기준을 공개한 로봇 관제 제품이나 연구가 있는가? (영역 43, 57)
- oq-214 [열림] 로봇 플랫폼에 적용될 수 있는 현행 「개인정보의 안전성 확보조치 기준」(2023-6호 이후 개정판)의 접속기록 보관 기간·점검 주기 조항이 2023-6호와 같은가? (영역 43, 53)
- oq-215 [열림] 구로병원 실증의 전체 성공률 87.03% 가 122건 중 실패 14건과 맞지 않는데(약 88.5%) 성공률의 분모는 무엇인가? (영역 43, 63)
- oq-267 [열림] ROP 같은 다중 제조사 오케스트레이션 플랫폼의 과금 단위(로봇당·작업당·현장당·구독)를 비교하거나 공개한 자료가 있는가? (영역 3, 41)
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

### runs/2026-10-09-05/research.md

```markdown
# 리서치 브리프 2026-10-09-05

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-09-05 |
| 날짜 | 2026-10-09 |
| 실행 유형 | category_link (대분류 연결) |
| 대상 영역 | 해당 없음 |
| 대분류 | J. 현장 운영·관제 |

## 갭(비어 있거나 약한 섹션)

- 대분류 페이지 '다른 대분류와의 연결' 절이 '아직 작성되지 않음' 상태다. J. 현장 운영·관제의 네 세부영역(37. 관제 화면·실행 기록, 38. 모니터링·이상 탐지·원인 분석, 39. 운영 성과 측정·개선, 40. 운영 절차·요청 창구)과 다른 16개 대분류를 잇는 연결이 하나도 정리되지 않았다
- 38. 모니터링·이상 탐지·원인 분석과 39. 운영 성과 측정·개선 페이지의 10절은 개정 전 분류(2026-09-25) 기준으로 쓰였다. 따라서 K. 플랫폼 아키텍처·인프라, M. 안전, N. 보안·개인정보, P. 거버넌스·법규·사회, Q. 현장 유형별 적용과의 연결 근거가 약하다
- B. 로봇 온톨로지와 J. 현장 운영·관제를 잇는 검증된 근거가 게시 페이지에 없다
- 37. 관제 화면·실행 기록과 M. 안전(사고 조사 기록), P. 거버넌스·법규·사회(기록 보관 의무)의 연결은 열린 질문(oq-239, oq-252)뿐이고 근거 자료가 없다
- 38. 모니터링·이상 탐지·원인 분석의 경보 설계를 H. 실행·협업·예외 복구의 운영자 대응(31. 사람–로봇 협업)과 잇는 근거 자료가 없다

## 조사 질문

1. 운영자가 지금 무슨 일이 일어나는지 보고, 이상을 알아차리고, 성과를 확인할 수 있는가? [분류원문]
2. 지연의 원인이 로봇인지, 설비인지, 통신인지, 앞 작업인지 어떻게 찾을까? [분류원문]
3. 37. 관제 화면·실행 기록이 남기는 실행 기록은 C. 채팅 기반 구성·운영(11. 채팅으로 실제 상황 시뮬레이션 재현, 12. 채팅으로 업무 지시·오케스트레이션), I. 설계·시뮬레이션(36. 가상 시운전·실제 상황 재현), K. 플랫폼 아키텍처·인프라(43. 데이터·관측성·배포), M. 안전(50. 안전 표준·인증·사고 조사), P. 거버넌스·법규·사회(59. 법·규제·보험·라이선스)에 무엇을 넘겨주는가? (oq-131, oq-239, oq-252 관련)
4. 38. 모니터링·이상 탐지·원인 분석은 F. 연동과 E. 사물·사람·실시간 상태에서 어떤 신호를 받는가? 그리고 판정 결과와 경보를 H. 실행·협업·예외 복구, G. 계획·최적화, L. AI·학습 기술, N. 보안·개인정보 쪽으로 어떻게 넘기는가? (oq-033, oq-072, oq-082, oq-210 관련)
5. 39. 운영 성과 측정·개선의 지표는 A. 기획·사업(투자 효과), F. 연동(주문 단위 지표), G. 계획·최적화·I. 설계·시뮬레이션(정책 비교), N. 보안·개인정보·P. 거버넌스·법규·사회(작업자 데이터)와 어디서 만나는가? (oq-015, oq-084 관련)
6. 40. 운영 절차·요청 창구의 요청 접수·권한·통제 구역·교육은 F. 연동, D. 공간·지도 모델, N. 보안·개인정보, M. 안전, O. 검증·도입·수명주기, P. 거버넌스·법규·사회, Q. 현장 유형별 적용과 어떻게 이어지는가? (oq-203, oq-265, oq-266 관련)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | J. 현장 운영·관제의 37. 관제 화면·실행 기록 ↔ D. 공간·지도 모델의 15. 지도·공간·위치 모델 연결 근거: Open-RMF rmf_visualization 은 층 평면도 위에 로봇 위치, 문·승강기, 주행 그래프, 예측 궤적을 겹쳐 표시한다. | ref-1093 | 아니오 | medium | 2026-10-09 | — | 원문 미열람 |
| f2 | [추정] | J. 현장 운영·관제의 37. 관제 화면·실행 기록 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: Open-RMF 작업 이벤트 로그는 작업·단계·사건의 3계층으로 나뉘고 MCAP 은 시각 색인을 둔 기록 형식이어서, 37. 관제 화면·실행 기록이 남긴 기록은 시간축 재현의 입력이 될 수 있어 보인다. 다만 이 기록을 시뮬레이션 시나리오로 바꾸는 공개 형식은 확인되지 않았다(oq-131). | ref-1094, ref-1096 | 아니오 | medium | 2026-10-09 | — | — |
| f3 | [추정] | J. 현장 운영·관제의 37. 관제 화면·실행 기록 ↔ C. 채팅 기반 구성·운영의 11. 채팅으로 실제 상황 시뮬레이션 재현: 11. 채팅으로 실제 상황 시뮬레이션 재현은 재현 결과를 실제 기록(시각·위치·사건 순서)과 비교해야 한다. 그 실제 기록은 37. 관제 화면·실행 기록이 정규화해 저장하는 실행 기록에서 나올 것으로 보인다. | ref-1094, ref-1096 | 아니오 | low | 2026-10-09 | — | — |
| f4 | [추정] | J. 현장 운영·관제의 37. 관제 화면·실행 기록 ↔ C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션: 12. 채팅으로 업무 지시·오케스트레이션은 진행 상황 질의에 실행 기록과 시각을 근거로 답한다. Open-RMF 작업 상태 스키마의 상태 값, 시작·종료 시각, 단계 목록, 취소·강제 종료 기록이 그 답의 근거 자료가 될 것으로 보인다. | ref-111 | 아니오 | medium | 2026-10-09 | — | — |
| f5 | [사실] | J. 현장 운영·관제의 37. 관제 화면·실행 기록 ↔ F. 연동의 20. 로봇·제조사 관제 연동 연결 근거: VDA 5050 3.0.0 은 차량 위치·계획 경로를 시각화 시스템에 보내는 visualization 토픽을 상태(state) 토픽과 따로 둔다. | ref-031 | 아니오 | medium | 2026-10-09 | — | — |
| f6 | [사실] | J. 현장 운영·관제의 37. 관제 화면·실행 기록 ↔ K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포 연결 근거: Open-RMF 웹 대시보드의 API 서버(rmf-server)는 기본으로 메모리 안의 SQLite 를 쓰고 PostgreSQL·SQLite·MySQL·MariaDB 를 지원한다. 따라서 실행 기록을 영속 저장하는 것은 배포 설정의 몫이다. | ref-762, ref-302 | 아니오 | medium | 2026-10-09 | — | — |
| f7 | [사실] | J. 현장 운영·관제의 37. 관제 화면·실행 기록 ↔ H. 실행·협업·예외 복구의 31. 사람–로봇 협업 연결 근거: 다중 로봇 인터페이스 연구(Roldán 외, Sensors 2017)는 운영자 상황 인식을 위한 설계 요건으로 정보 선별과 관련 정보로의 주의 유도를 들었다. | ref-1099 | 아니오 | medium | 2017-07-27 | — | 원문 미열람 |
| f8 | [사실] | J. 현장 운영·관제의 37. 관제 화면·실행 기록 ↔ G. 계획·최적화의 27. 다중 로봇 경로·교통 관리 — MAPF 연결 근거: 설명 가능한 다중 에이전트 경로 찾기 연구(Kottinger·Almagor·Lahijanian, ICAPS 2022)는 경로 계획을 사람이 확인할 수 있게 나눠 보여 주는 설명 문제를 다루지만 알고리즘 수준의 연구다. | ref-1098 | 아니오 | medium | 2022-02 | — | 원문 미열람 |
| f9 | [추정] | J. 현장 운영·관제의 37. 관제 화면·실행 기록 ↔ E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적: 한림대학교의료원 협약은 안면 인식 기반 수령 인증과 특수 물품 배송 이력 관리 시스템을 함께 개발하기로 한 것이다. 이를 보면 수령인 확인(17. 작업 대상·자산 식별과 인계 추적)과 배송 이력 기록(37. 관제 화면·실행 기록)은 완료·인계 단계에서 한 기록으로 묶일 것으로 보인다. | ref-1103 | 아니오 | low | 2025-04-07 | 병원 / 완료·인계 | 원문 미열람 |
| f10 | [사실] | J. 현장 운영·관제의 37. 관제 화면·실행 기록 ↔ M. 안전의 50. 안전 표준·인증·사고 조사 연결 근거: Winfield 외(2022)의 윤리적 블랙박스 초안 공개 표준은 사고·아차 사고 조사를 돕기 위해 소셜 로봇의 센서·구동기·제어 결정 데이터를 안전하게 기록하는 장치나 소프트웨어 모듈을 제안한다. 이 초안은 단일 소셜 로봇을 대상으로 하며 플릿·플랫폼 수준 기록은 다루지 않는다. | ref-1360 | 아니오 | medium | 2022-05-13 | — | — |
| f11 | [사실] | 연계 대상: J. 현장 운영·관제의 37. 관제 화면·실행 기록 ↔ P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스 연결 근거: 국내 병원·약국은 2018-05-18부터 마약류 취급 내역을 마약류통합관리시스템에 전산 보고할 수 있게 되었고, 종전 마약류 관리대장은 2년간 보관해야 한다고 보도되었다. 로봇 배송 이력이 이 보고·보관 대상에 드는지는 확인하지 못했다(oq-239). | ref-1364 | 아니오 | low | 2018-07-13 | — | — |
| f12 | [사실] | J. 현장 운영·관제의 37. 관제 화면·실행 기록 ↔ Q. 현장 유형별 적용의 63. 병원·의료 연결 근거: 국내 병원 현장에서 관제 시스템과 특수 물품 배송 이력 관리를 함께 개발하기로 한 협약이 2025-04 보도되었다. 37. 관제 화면·실행 기록 페이지가 찾은 현장 근거는 이 병원 사례 한 건뿐이다. | ref-1103 | 아니오 | low | 2025-04-07 | 병원 / 수행 자원 | 원문 미열람 |
| f13 | [추정] | J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석 ↔ E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성: Open-RMF 로봇 상태는 상태 값·문제 목록과 함께 기록 시각을 담는다. 그러므로 원인 구분은 18. 실시간 세계 상태·데이터 일관성이 시각과 함께 유지하는 로봇·문·작업의 현재 상태를 같은 시간축에 맞춘 데이터를 쓸 것으로 보인다. | ref-148, ref-051, ref-313 | 아니오 | medium | 2026-10-09 | — | — |
| f14 | [추정] | J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석 ↔ F. 연동의 20. 로봇·제조사 관제 연동: VDA 5050 의 오류 수준과 연결 상태(CONNECTION_BROKEN), MassRobotics 의 외부 사건 대기(waitingExternalEvent), Open-RMF 의 작업 지연·차단은 서로 다른 어휘로 보고된다. 그래서 20. 로봇·제조사 관제 연동에서 들어온 신호를 ROP 원인 범주로 옮기는 매핑이 필요할 것으로 보인다. 공통 매핑 표준은 확인되지 않았다(oq-033, oq-073). | ref-051, ref-449, ref-230, ref-111 | 아니오 | medium | 2026-10-09 | — | — |
| f15 | [사실] | J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석 ↔ F. 연동의 22. 설비·건물 시스템 연동 연결 근거: Open-RMF 문 모드는 closed·moving·open·offline·unknown 다섯 값이다. 문 어댑터는 진행 중인 로봇 작업을 방해하지 않을 때만 문을 움직이게 하는 상태 감독자 역할을 한다. | ref-313, ref-283 | 아니오 | medium | 2026-10-09 | — | — |
| f16 | [사실] | J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석 ↔ H. 실행·협업·예외 복구의 29. 명령·작업 실행의 신뢰성 연결 근거: Open-RMF 작업 상태 스키마는 blocked·error·failed·delayed·canceled·killed 를 포함한 12개 상태 값을 둔다. 또 작업에 걸린 중단(interruptions)·취소·강제 종료 요청 기록을 담아, 실행 결과 확인과 이상 탐지가 같은 기록을 쓴다. | ref-111 | 아니오 | medium | 2026-10-09 | — | — |
| f17 | [사실] | J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성 연결 근거: Open-RMF 경보(Alert) 메시지는 심각도 등급(info 0·warning 1·error 2), 운영자가 고를 수 있는 응답 목록(responses_available), 관련 작업 id 를 담는다. 원인 판정 뒤의 운영자 선택이 이 메시지로 복구 조치에 넘어간다. | ref-448 | 아니오 | medium | 2026-10-09 | 예외·성과 | — |
| f18 | [사실] | J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석 ↔ H. 실행·협업·예외 복구의 31. 사람–로봇 협업 연결 근거: 다중 로봇 수색·구조 과제 실험(Mehrotra·Sycara·Lewis·Chien·Wang, HFES 2011)에서 경보를 제한 없이 띄운 조건은 가장 중요한 경보 하나만 보여 준 조건보다 운영자가 고장을 더 빨리 발견했다. 탐색 면적과 발견한 피해자 수에는 차이가 없었다. | ref-1363 | 아니오 | medium | 2011 | — | — |
| f19 | [사실] | J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석 ↔ H. 실행·협업·예외 복구의 31. 사람–로봇 협업 연결 근거: ANSI/ISA 18.2-2016 은 공정 산업 시설에서 제어 시스템을 거쳐 운영자에게 표시되는 경보 전체의 수명주기 관리 원칙과 절차를 정한다. 다중 로봇 플릿에 특화된 경보 관리 표준은 이번 조사에서 찾지 못했다. | ref-1359 | 아니오 | medium | 2016 | — | — |
| f20 | [추정] | J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석 ↔ G. 계획·최적화의 25. 작업 배정 — MRTA: 위치 스푸핑을 다룬 2026-08 프리프린트의 신뢰 인지 모니터는 위치 신뢰도와 실행 행동 증거를 결합해 에이전트를 분류한다. 이로 미루어 실행 기록으로 이상 로봇을 가려 배정 후보에서 빼는 일이 두 영역의 접점이 될 것으로 보인다(oq-082). 물류센터 적용은 확인되지 않았다. | ref-494 | 아니오 | low | 2026-08 | — | 원문 미열람 |
| f21 | [추정] | J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석 ↔ K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포: 플랫폼 서비스 쪽 분산 추적(OpenTelemetry)과 ROS 2 런타임 쪽 추적(ros2_tracing)은 서로 다른 계층의 실행 정보를 모은다. 그래서 지연 원인 분석에 두 계층을 함께 쓰려면 작업 식별자로 기록을 잇는 관측성 설계가 필요할 것으로 보인다(oq-210). | ref-447, ref-1361 | 아니오 | low | 2026-10-09 | — | — |
| f22 | [사실] | J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석 ↔ K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포 연결 근거: ros2_tracing(Bédard·Lütkebohle·Dagenais, IEEE RA-L 2022)은 저부하 LTTng 추적기로 ROS 2 실행 정보를 모은다. 모든 ROS 2 계측을 켰을 때 메시지 종단 지연 증가는 평균 0.0033 ms 였다고 보고했다. | ref-1361 | 아니오 | medium | 2022-07 | — | — |
| f23 | [추정] | J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석 ↔ L. AI·학습 기술의 47. AI·학습·적응과 모델 운영: 분류 원문의 교차 규칙은 장애 분석을 38. 모니터링·이상 탐지·원인 분석에 적용되는 AI 연구 방법으로 둔다. 대규모 언어 모델로 로봇 실패를 설명하는 REFLECT(2023) 같은 연구가 두 영역을 잇는 예가 될 것으로 보인다. | ref-453 | 아니오 | low | 2023 | — | 원문 미열람 |
| f24 | [추정] | J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석 ↔ N. 보안·개인정보의 52. 통신 보호·위협 관리·감사: EU 사이버복원력법은 2026-09-11부터 디지털 요소 제품의 제조자에게 실제 악용되는 취약점과 중대 보안 사고를 24시간 안에 조기 경보하게 한다. 그래서 이상 탐지가 보안 사고를 가려내는 시점이 보고 의무와 맞물릴 수 있어 보인다. 오케스트레이션 플랫폼이 제조자에 해당하는지는 미확인이다. | ref-1236 | 아니오 | low | 2026-09-11 | — | 원문 미열람 |
| f25 | [추정] | J. 현장 운영·관제의 39. 운영 성과 측정·개선 ↔ A. 기획·사업의 3. 경제성·조달·사업 모델: 39. 운영 성과 측정·개선 페이지는 투자 수익률·순현재가치·회수 기간 같은 재무 평가를 연계 대상으로 둔다. ROP는 그 입력인 처리량·가동률·충전·예외 실행 데이터를 제공한다고 보므로, 운영 지표가 투자 효과 판단으로 넘어가는 지점에서 두 영역이 이어지는 것으로 보인다(oq-268). | ref-150, ref-139, ref-148 | 아니오 | low | 2026-10-09 | — | — |
| f26 | [사실] | J. 현장 운영·관제의 39. 운영 성과 측정·개선 ↔ E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성 연결 근거: Open-RMF 로봇 상태 스키마는 상태 값(uninitialized·offline·shutdown·idle·charging·working·error), 0~1 범위의 배터리, 현재 작업 id, 문제 목록, 기록 시각을 담는다. 이 값은 가동률·충전·오류 시간 지표의 원천이 된다. | ref-148 | 아니오 | medium | 2026-10-09 | — | — |
| f27 | [추정] | J. 현장 운영·관제의 39. 운영 성과 측정·개선 ↔ F. 연동의 23. 업무 시스템 연동: 로봇·작업 상태 기록만으로는 완전 주문 이행률·주문 이행 사이클 타임 같은 주문 단위 지표를 계산할 수 없다. 이 지표는 23. 업무 시스템 연동을 거쳐 WMS·ERP 주문 데이터와 이어야 계산될 것으로 보인다(oq-015). | ref-140, ref-148, ref-111 | 아니오 | medium | 2026-10-09 | 물류창고 / 완료·인계 | — |
| f28 | [사실] | J. 현장 운영·관제의 39. 운영 성과 측정·개선 ↔ G. 계획·최적화의 28. 공용 자원·충전·에너지 최적화 연결 근거: Omega(2024) 게재 연구는 로봇 이동형 풀필먼트 시스템에서 동적 우선순위 규칙이 선착순보다 에너지 소비를 3.41% 줄이고 처리량을 26.07% 높였다고 보고했다. 모델·시뮬레이션 조건의 저자 보고값이며 현장 실측이 아니다. | ref-146 | 아니오 | medium | 2024 | 물류창고 / 예외·성과 | 원문 미열람 |
| f29 | [사실] | J. 현장 운영·관제의 39. 운영 성과 측정·개선 ↔ I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계 연결 근거: AMR 물류센터 플릿 규모 산정 시뮬레이션 연구(FAIM 2025)에서는 충전기가 부족하면 큰 지연이, 남으면 불필요한 비용이 생겼다. 설계 단계의 충전기 수 결정이 운영 성과 지표에 그대로 나타난다는 뜻이다. | ref-102 | 아니오 | medium | 2025 | 물류창고 / 제약 | 원문 미열람 |
| f30 | [사실] | J. 현장 운영·관제의 39. 운영 성과 측정·개선 ↔ N. 보안·개인정보의 53. 개인정보·영상 데이터 연결 근거: 창고 작업자 12명을 반구조화 면담한 연구(Malik·Brandão·Coopamootoo, 2026)는 로봇 운영에 따르는 데이터 감시에 대한 작업자 우려를 확인했다. 연구는 감시 활동 알림·개인정보 통제 같은 작업자 중심 요구를 제시했다. | ref-1278 | 아니오 | medium | 2026 | 물류창고 / 제약 | 원문 미열람 |
| f31 | [추정] | J. 현장 운영·관제의 39. 운영 성과 측정·개선 ↔ P. 거버넌스·법규·사회의 60. 노동·수용성·접근성: 한국 근로자참여법 제20조는 신기계·기술 도입과 사업장 내 근로자 감시 설비 설치를 노사협의회 협의 사항으로 둔다. 따라서 성과 측정이 개별 작업자의 처리량·위치까지 기록하면 도입 전 노동자 참여 절차가 필요할 가능성이 있다. 법적 해당 여부는 확인하지 못했다. | ref-1272, ref-1278 | 아니오 | low | 2019-04-16 | 제약 | 원문 미열람 |
| f32 | [사실] | J. 현장 운영·관제의 39. 운영 성과 측정·개선 ↔ Q. 현장 유형별 적용의 61. 물류창고 연결 근거: 로봇 이동형 풀필먼트 시스템 대기행렬 모델(Lamballais 외, 2017)에서는 처리량이 보관 구역 둘레의 작업대 위치에 영향을 받았다. 협업형 AMR 피킹 해석 모델(Ghelichi·Kilaru, 2021)에서는 처리율·피킹 구역 크기·클러스터 크기가 성과를 가장 크게 좌우했다. | ref-096, ref-145 | 아니오 | medium | 2021 | 물류창고 / 수행 자원 | 원문 미열람 |
| f33 | [사실] | J. 현장 운영·관제의 39. 운영 성과 측정·개선 ↔ Q. 현장 유형별 적용의 62. 제조 공장 연결 근거: ISO 22400-2:2014 는 제조 운영 관리의 핵심성과지표 정의를 다루는 현행판이다. 에너지 관리 KPI 를 더한 개정 1(2017-04)이 있고, 개정판 ISO/DIS 22400-2 의 발행은 2026-09-26 기준 확인되지 않았다. | ref-139 | 아니오 | medium | 2014 | 제조 공장 | 원문 미열람 |
| f34 | [사실] | J. 현장 운영·관제의 40. 운영 절차·요청 창구 ↔ F. 연동의 23. 업무 시스템 연동 연결 근거: 미국 ChristianaCare 는 간호사가 키오스크에서 Moxi 로봇을 호출하던 방식에 더해, 로봇을 Cerner 전자의무기록과 연동해 주문이 들어오면 로봇이 물품을 가지러 가게 하는 계획을 밝혔다(2022-08 보도). 실제 운영 결과는 확인하지 못했다. | ref-1362 | 아니오 | low | 2022-08-11 | 병원 / 시작 조건 | — |
| f35 | [추정] | J. 현장 운영·관제의 40. 운영 절차·요청 창구 ↔ G. 계획·최적화의 26. 작업 순서·스케줄링: Open-RMF 작업 요청 스키마는 가장 이른 시작 시각과 우선순위만 두고 마감 시각 필드는 두지 않는다. 그래서 요청 창구에서 받은 긴급도·기한을 순서 결정 입력으로 옮기는 규칙이 두 영역의 접점이 될 것으로 보인다. | ref-125 | 아니오 | medium | 2026-10-09 | 시작 조건 | — |
| f36 | [추정] | J. 현장 운영·관제의 40. 운영 절차·요청 창구 ↔ D. 공간·지도 모델의 16. 장소 의미·지도 관리: Open-RMF 차선 요청(LaneRequest)은 플릿 이름과 열고 닫을 차선 목록 세 필드만 둔다. 따라서 임시 통제 구역을 누가 왜 언제까지 닫았는지는 40. 운영 절차·요청 창구의 운영 기록이, 차선·구역 반영은 16. 장소 의미·지도 관리가 맡는 접점이 될 것으로 보인다(oq-203). | ref-569 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f37 | [사실] | J. 현장 운영·관제의 40. 운영 절차·요청 창구 ↔ N. 보안·개인정보의 51. 인증·권한·격리 연결 근거: Open-RMF API 서버(rmf-server)는 OpenID Connect 신원 공급자로 인증하고 권한은 앱 안에서 역할·동작·자원 권한 그룹으로 판정한다. 관리자는 모든 그룹에서 모든 동작을 할 수 있고, 현재 모든 자원은 빈 문자열 기본 그룹에 들어간다. | ref-762 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f38 | [추정] | 연계 대상: J. 현장 운영·관제의 40. 운영 절차·요청 창구 ↔ M. 안전의 50. 안전 표준·인증·사고 조사: 40. 운영 절차·요청 창구 페이지는 로봇 교시·정비 작업 지침(산업안전보건기준에 관한 규칙 제222조)과 ANSI/A3 R15.08-3-2026 이 사용자에게 두는 운영 요구를 사업주·제조사 책임의 연계 대상으로 둔다. 이렇게 보면 ROP는 요청·권한·기록 층으로 그 이행을 받쳐 주는 쪽으로 보인다(oq-265). | ref-1157, ref-1153 | 아니오 | low | 2026-10-09 | 수행 자원 | 원문 미열람 |
| f39 | [사실] | J. 현장 운영·관제의 40. 운영 절차·요청 창구 ↔ O. 검증·도입·수명주기의 56. 운영 이관·확대·교육 연결 근거: 중국 고급 호텔 직원 19명 면담 연구(Fu·Zheng·Wong, 2022)에서는 로봇이 어느 부서 소속인지 불분명해 정비 책임과 부서 간 소통 부담이 생겼다. 근무 중 로봇 교육, 동료 교육, 고장 처리·고객 안내 같은 추가 업무도 직원의 사용 저항으로 이어졌다. | ref-1150 | 아니오 | medium | 2022 | 상업 시설 / 수행 자원 | 원문 미열람 |
| f40 | [사실] | J. 현장 운영·관제의 40. 운영 절차·요청 창구 ↔ P. 거버넌스·법규·사회의 60. 노동·수용성·접근성 연결 근거: 병원 자율 배송 로봇(TUG) 민족지 연구(Mutlu·Forlizzi, HRI 2008)에서 내과 병동은 업무 중단에 대한 낮은 허용도, 비용과 이익의 불일치, 통행이 많은 곳의 주행 중단 때문에 직원 저항을 보였다. 반면 산후 병동은 로봇을 업무 흐름에 통합했다. | ref-1151 | 아니오 | medium | 2008-03 | 병원 / 예외·성과 | 원문 미열람 |
| f41 | [사실] | J. 현장 운영·관제의 40. 운영 절차·요청 창구 ↔ Q. 현장 유형별 적용의 63. 병원·의료 연결 근거: 한림대학교성심병원은 전담 부서인 커맨드센터가 7종 73대의 서비스 로봇을 통합 관제로 운영해 의료진이 로봇을 직접 운용하지 않아도 되게 했다고 2024년 보도되었다. | ref-1199, ref-944 | 아니오 | medium | 2024-09-19 | 병원 / 수행 자원 | 원문 미열람 |
| f42 | [사실] | J. 현장 운영·관제의 40. 운영 절차·요청 창구 ↔ Q. 현장 유형별 적용의 64. 상업 시설 연결 근거: 미국 뉴욕 알로프트 호텔에서는 투숙객이 전화로 프런트에 요청하면 주문 물건과 객실 번호를 사람이 확인해 처리했다. 배송 로봇(Savioke Relay)은 객실 앞에 도착하면 객실 전화로 자동 알림을 보냈다(2017년 보도). | ref-1152 | 아니오 | low | 2017-04-18 | 상업 시설 / 시작 조건 | 원문 미열람 |
| f43 | [사실] | 연계 대상: J. 현장 운영·관제의 40. 운영 절차·요청 창구 ↔ F. 연동의 22. 설비·건물 시스템 연동 연결 근거: 미국 MultiCare 계열 두 병원의 Moxi 로봇은 복도·층간 이동에서 길을 잃고 승강기 버튼을 스스로 누르지 못해 사람이 계속 따라다녀야 했다고 2026-06 보도되었다. | ref-1154 | 아니오 | medium | 2026-06-09 | 병원 / 예외·성과 | 원문 미열람 |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1093 | Open Robotics (open-rmf/rmf_visualization) | rmf_visualization — README | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/open-rmf/rmf_visualization | 예 |
| ref-1094 | Open Robotics (open-rmf/rmf_api_msgs) | rmf_api_msgs schemas — task_log.json (Task Event Log) | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_log.json | 아니오 |
| ref-1096 | MCAP 프로젝트 (Foxglove) | MCAP Format Specification | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://mcap.dev/spec | 예 |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | medium | 2026-10-09 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-762 | Open Robotics (open-rmf) | rmf-web — packages/api-server/README.md | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md | 아니오 |
| ref-302 | Open Robotics (open-rmf) | rmf-web — README | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/open-rmf/rmf-web | 예 |
| ref-1099 | Roldán, J. J., Peña-Tapia, E., Martín-Barrio, A. 외 (Sensors 17(8)) | Multi-Robot Interfaces and Operator Situational Awareness: Study of the Impact of Immersion and Prediction | 2017-07-27 | 논문 | medium | 2026-10-09 | https://pmc.ncbi.nlm.nih.gov/articles/PMC5579739/ | 예 |
| ref-1098 | Kottinger, J., Almagor, S., & Lahijanian, M. (arXiv, ICAPS 2022) | Conflict-Based Search for Explainable Multi-Agent Path Finding | 2022-02 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2202.09930 | 예 |
| ref-1103 | 아주경제 | 현대차그룹 로보틱스 솔루션, 일선 병원에 도입된다 | 2025-04-07 | 기사 | low | 2026-10-09 | https://www.ajunews.com/view/20250407084333272 | 예 |
| ref-148 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json | 아니오 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | 표준 | medium | 2026-10-09 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 아니오 |
| ref-313 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_door_msgs/msg/DoorMode.msg | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorMode.msg | 아니오 |
| ref-449 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/connection.schema | 미확인 | 표준 | medium | 2026-10-09 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/connection.schema | 아니오 |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 미확인 | 표준 | medium | 2026-10-09 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json | 아니오 |
| ref-283 | Open Robotics | Doors (integration_doors) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://osrf.github.io/ros2multirobotbook/integration_doors.html | 아니오 |
| ref-448 | Open Robotics (open-rmf/rmf_internal_msgs) | rmf_task_msgs/msg/Alert.msg | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/Alert.msg | 아니오 |
| ref-494 | Francos, R. M., Garces, D., Akgün, O. E., Bastian, N. D., & Gil, S.(Harvard·JHU) | Trust-Aware Sequential Decision Making and Rollout Planning for Resilient Multi-Robot Systems | 2026-08 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2608.25690 | 예 |
| ref-447 | OpenTelemetry (CNCF) | OpenTelemetry Specification — Overview | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/overview.md | 아니오 |
| ref-453 | Liu, Z., Bahety, A., & Song, S. | REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction | 2023 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2306.15724 | 예 |
| ref-1236 | European Commission (Shaping Europe's digital future) | Cyber Resilience Act - Reporting obligations | 2026-09-11 | 정부·연구기관 | medium | 2026-10-09 | https://digital-strategy.ec.europa.eu/en/policies/cra-reporting | 예 |
| ref-150 | CIO Korea | 오토스토어, 물류 자동화 시스템의 경제적 효과 연구 보고서 발표 | 미확인 | 기사 | low | 2026-10-09 | https://www.cio.com/article/3517636/%EC%98%A4%ED%86%A0%EC%8A%A4%ED%86%A0%EC%96%B4-%EB%AC%BC%EB%A5%98-%EC%9E%90%EB%8F%99%ED%99%94-%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%9D%98-%EA%B2%BD%EC%A0%9C%EC%A0%81-%ED%9A%A8%EA%B3%BC-%EC%97%B0%EA%B5%AC.html | 예 |
| ref-139 | ISO | ISO 22400-2:2014 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions | 2014 | 표준 | medium | 2026-10-09 | https://www.iso.org/standard/54497.html | 예 |
| ref-140 | ASCM | SCOR Model — Performance: Reliability RL.1.1 Perfect Customer Order Fulfillment | 미확인 | 표준 | medium | 2026-10-09 | https://scor.ascm.org/performance/reliability/RL.1.1 | 예 |
| ref-146 | Omega 게재 논문(저자 미확인) | The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority | 2024 | 논문 | medium | 2026-10-09 | https://www.sciencedirect.com/science/article/abs/pii/S0305048324001336 | 예 |
| ref-102 | Springer(FAIM 2025 발표 논문, 저자 미확인) | Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics | 2025 | 논문 | medium | 2026-10-09 | https://link.springer.com/chapter/10.1007/978-3-032-07675-5_69 | 예 |
| ref-1278 | Malik, M. A. B., Brandão, M., Coopamootoo, K. (International Journal of Social Robotics) | Towards Worker-Centered Warehouse Robots: A User Study on Privacy, Inclusivity and Safety | 2026 | 논문 | medium | 2026-10-09 | https://doi.org/10.1007/s12369-026-01359-1 | 예 |
| ref-1272 | 대한민국 국회 (법률 제16320호, 케이스노트 게재) | 근로자참여 및 협력증진에 관한 법률 제20조(협의 사항) | 2019-04-16 | 정부·연구기관 | medium | 2026-10-09 | https://casenote.kr/%EB%B2%95%EB%A0%B9/%EA%B7%BC%EB%A1%9C%EC%9E%90%EC%B0%B8%EC%97%AC_%EB%B0%8F_%ED%98%91%EB%A0%A5%EC%A6%9D%EC%A7%84%EC%97%90_%EA%B4%80%ED%95%9C_%EB%B2%95%EB%A5%A0/%EC%A0%9C20%EC%A1%B0 | 예 |
| ref-096 | Lamballais, T., Roy, D., & de Koster, M. B. M. | Estimating performance in a Robotic Mobile Fulfillment System | 2017 | 논문 | medium | 2026-10-09 | https://repub.eur.nl/pub/107376/ | 예 |
| ref-145 | Ghelichi, Z., & Kilaru, S. | Analytical models for collaborative autonomous mobile robot solutions in fulfillment centers | 2021 | 논문 | medium | 2026-10-09 | https://www.sciencedirect.com/science/article/pii/S0307904X20305801 | 예 |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json | 아니오 |
| ref-569 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_fleet_msgs/msg/LaneRequest.msg | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg | 아니오 |
| ref-1153 | ANSI (The ANSI Blog) | ANSI/A3 R15.08-3-2026: Industrial Mobile Robot Applications | 미확인 | 표준 | medium | 2026-10-09 | https://blog.ansi.org/ansi/ansi-a3-r15-08-3-2026-industrial-mobile-robot/ | 예 |
| ref-1157 | 고용노동부 (국가법령정보센터) | 산업안전보건기준에 관한 규칙 제222조(교시 등) | 2025-09-01 | 정부·연구기관 | medium | 2026-10-09 | https://www.law.go.kr/LSW/lsLawLinkInfo.do?lsJoLnkSeq=1000727281&chrClsCd=010202 | 예 |
| ref-1150 | Fu, S., Zheng, X., & Wong, I. A. (International Journal of Hospitality Management) | The perils of hotel technology: The robot usage resistance model | 2022 | 논문 | medium | 2026-10-09 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8786597/ | 예 |
| ref-1151 | Mutlu, B., & Forlizzi, J. (ACM/IEEE HRI 2008) | Robots in Organizations: The Role of Workflow, Social, and Environmental Factors in Human-Robot Interaction | 2008-03 | 논문 | medium | 2026-10-09 | https://pages.cs.wisc.edu/~bilge/pubs/2008/HRI08-Mutlu.pdf | 예 |
| ref-944 | 로봇신문 | 국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원' | 2024-04-15 | 기사 | low | 2026-10-09 | http://www.irobotnews.com/news/articleView.html?idxno=34601 | 예 |
| ref-1199 | ZDNet Korea | 로봇이 병원에서 뭘 할 수 있는지 답을 찾는 사람들 ... (제목 일부만 확인) | 2024-09-19 | 기사 | low | 2026-10-09 | https://zdnet.co.kr/view/?no=20240919162124 | 예 |
| ref-1152 | 한국일보 | “딩동~ 물건 왔어요” 호텔서 주문하면 로봇이 … (제목 일부만 확인) | 2017-04-18 | 기사 | low | 2026-10-09 | https://www.hankookilbo.com/news/article/201704180418820469 | 예 |
| ref-1154 | Proof News (Varsha Bansal) | Meet the Robot That Nurses Unplugged | 2026-06-09 | 기사 | medium | 2026-10-09 | https://www.proofnews.org/moxi/ | 예 |
| ref-1359 | ISA (ANSI Webstore 게재) | ANSI/ISA 18.2-2016 Management of Alarm Systems for the Process Industries | 2016 | 표준 | medium | 2026-10-09 | https://webstore.ansi.org/standards/isa/ansiisa182016 | 아니오 |
| ref-1360 | Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv) | An Ethical Black Box for Social Robots: a draft Open Standard | 2022-05-13 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2205.06564 | 아니오 |
| ref-1361 | Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L 7(3), arXiv) | ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2 | 2022-07 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2201.00393 | 아니오 |
| ref-1362 | TechTarget (Hannah Nelson, Xtelligent Healthcare Media) | Hospital Looks to 'Cobot' EHR Integration to Alleviate Nurse Burnout | 2022-08-11 | 기사 | low | 2026-10-09 | https://techtarget.com/searchhealthit/feature/Hospital-Looks-to-Cobot-EHR-Integration-to-Alleviate-Nurse-Burnout | 아니오 |
| ref-1363 | Mehrotra, S., Sycara, K., Lewis, M., Chien, S.-Y., & Wang, H. (Proceedings of the Human Factors and Ergonomics Society) | Effects of alarms on control of robot teams | 2011 | 논문 | medium | 2026-10-09 | https://d-scholarship.pitt.edu/12400/ | 아니오 |
| ref-1364 | 데일리팜 (김지은) | 마약통합시스템 시행 2개월…병원·약국 다빈도 질문은 | 2018-07-13 | 기사 | low | 2026-10-09 | https://dailypharm.com/user/news/85066 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/field-operations-and-monitoring/index.md | 5. 다른 대분류와의 연결 | '다른 대분류와의 연결' 절만 채운다(category_link, patches). 대분류별 근거는 다음과 같다. A. 기획·사업: f25 / B. 로봇 온톨로지: 근거 없음, '아직 다루지 않은 연결'로 명시 / C. 채팅 기반 구성·운영: f3·f4 / D. 공간·지도 모델: f1·f36 / E. 사물·사람·실시간 상태: f9·f13·f26 / F. 연동: f5·f14·f15·f27·f34·f43 / G. 계획·최적화: f8·f20·f28·f35 / H. 실행·협업·예외 복구: f7·f16·f17·f18·f19 / I. 설계·시뮬레이션: f2·f29 / K. 플랫폼 아키텍처·인프라: f6·f21·f22 / L. AI·학습 기술: f23 / M. 안전: f10·f38 / N. 보안·개인정보: f24·f30·f37 / O. 검증·도입·수명주기: f39 / P. 거버넌스·법규·사회: f11·f31·f40 / Q. 현장 유형별 적용: f12·f32·f33·f41·f42. 이 중 f20·f23·f24·f31·f38 은 추정·low 이므로 단정하지 말고 쓰고, f11·f38·f43 은 '연계 대상'으로 짧게 다룬다. 18. 실시간 세계 상태·데이터 일관성(f13·f26, 현재 상태)과 34·35 쪽 시뮬레이션·설계(f2·f29, 가정한 미래)는 구분해 쓴다. 다음 실행 후보: 38. 모니터링·이상 탐지·원인 분석 10절에 f18·f19·f21·f22 반영, 37. 관제 화면·실행 기록 11절 oq-252 에 f10, oq-239 에 f11 근거 추가. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 경보 관리 | Alarm Management (ANSI/ISA 18.2) | 운영자에게 표시되는 경보를 정의·설계·운영·유지·변경하는 수명주기 전체를 관리하는 일로, 공정 산업에서는 ANSI/ISA 18.2-2016 이 일반 원칙과 절차를 정한다. |
| 런타임 추적 | Runtime Tracing (ros2_tracing) | 실행 중인 소프트웨어 내부의 콜백·메시지 전달 같은 실행 정보를 저부하 추적기로 기록하는 방법으로, ROS 2 에서는 LTTng 기반 ros2_tracing 이 이를 제공한다. |

## 열린 질문

새로 생긴 질문:

- 다중 로봇 플릿 관제에서 경보 우선순위, 경보 홍수 기준, 경보 합리화 절차를 ANSI/ISA 18.2 처럼 정한 로봇 운영용 경보 관리 표준이나 공개 지침이 있는가? | 관련 영역: 38. 모니터링·이상 탐지·원인 분석, 31. 사람–로봇 협업 | 근거: f19 | 종류: 일반
- 전자의무기록 주문이 로봇 작업 요청을 자동으로 만드는 병원 연동에서 주문 취소·변경을 진행 중인 로봇 작업에 반영하고 결과를 기록에 되돌린 공개 사례가 있는가? | 관련 영역: 40. 운영 절차·요청 창구, 23. 업무 시스템 연동, 63. 병원·의료 | 근거: f34 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 46 · 교차 확인: 0
- 예산 사용량: 검색 9회 · 신규 출처 6건
- 미확인 항목:
    - f11 마약류 관리대장 2년 보관·전산 보고는 2018년 업계 기사 기준이다. 법령 원문과 현행 여부는 미확인이다. 로봇 배송 이력이 보고 대상에 드는지도 미확인이다(oq-239 미해결)
    - f19 ANSI/ISA 18.2-2016 본문은 유료라 미열람이다. 경보 홍수 기준(10분 10건 등)은 벤더 자료 요약에만 있어 넣지 않았다
    - f22 ros2_tracing 의 0.0033 ms 는 저자 실험값이며 독립 재현은 미확인이다
    - f34 ChristianaCare 의 EHR 연동은 2022 계획 보도이며 실행 여부는 미확인이다
    - f41 한림대학교성심병원 수치는 병원 발표에서 나온 보도 두 건이라 독립 교차 확인으로 보지 않았다
    - NCS(국가직무능력표준)의 로봇 운용·관제 능력단위는 검색에서 확인하지 못했다(oq-278 미해결)
    - 이종 플릿 예지 정비 공개 연구는 벤더 자료뿐이라 넣지 않았다(oq-221 미해결)
- 범위 경계 위반 의심:
    - f11: 마약류 보고·보관 의무는 업종별 조건(의료)과 병원 업무 시스템의 몫이다. '연계 대상:'으로 표시했다
    - f38: 교시·정비 작업 지침과 사용자 측 안전 요구 이행은 사업주·제조사 몫이다. '연계 대상:'으로 표시했다
    - f43: 승강기 조작은 시설·설비 제어 경계의 연계 대상이다. '연계 대상:'으로 표시했다
    - f15: 문 개폐 제어 자체는 연계 대상이며 ROP 몫은 문 상태 확인으로 한정했다
    - f24: 사이버복원력법 보고 의무는 제조자의 법적 의무이며, 플랫폼이 제조자에 해당하는지는 판단하지 않았다
    - f19: ISA 18.2 는 공정 산업 표준이므로 로봇 플릿 적용을 단정하지 않았다
- 한계: web_fetch_available: true · fetch_mode full. 검색 9회/30, 신규 출처 6건/15(ref-1359~ref-1364, 예약 구간 안), 재사용 출처 40건. 재사용 출처 가운데 Open-RMF 공식 저장소 원문 6건(ref-111, ref-148, ref-448, ref-569, ref-762, ref-1094)은 raw.githubusercontent.com 으로 다시 열어 확인했다. 나머지 재사용 출처는 게시된 세부영역 페이지(37·38·39·40)와 이전 브리프(2026-09-30-23, 2026-09-30-24), 다른 대분류 페이지(G. 계획·최적화)의 검증된 주장을 재인용했으며 다시 열지 않았다. 참고문헌 목록 원문 열람이 '아니오'인 출처에 기댄 finding 에는 source_unopened 를 표시했다. 신규 출처 6건은 모두 열었으나 ISA 18.2 는 판매 소개 페이지, arXiv 2건과 HFES 1건은 초록만 읽었다. 교차 확인은 0건이다(대부분 단일 출처, 한림대 보도 2건은 독립이 아님). 벤더 기능·성능 주장은 finding 으로 내지 않았다(오토스토어 수치는 f25 에서 제외). B. 로봇 온톨로지와 J. 현장 운영·관제를 잇는 근거는 게시 페이지에서 찾지 못해 finding 이 없으며, 스토리텔러는 '아직 다루지 않은 연결'로 적어야 한다. 현장 유형 근거는 물류창고·제조 공장·병원·상업 시설이고 가정·실외·기타는 없다. L. AI·학습 기술 연결(f23)은 분류 원문 교차 규칙(장애 분석은 38번)에 기댄다. 18. 실시간 세계 상태·데이터 일관성(현재 상태)과 34·35(가정한 미래 실험·설계)를 섞지 않았다. 열린 질문 oq-131·oq-203·oq-210·oq-239·oq-252·oq-265 는 부분 근거만 더했고 해결 제안은 없다. 대분류 페이지 절 번호는 제목 순서(핵심 질문·개요·세부 연구영역·핵심 포인트·다른 대분류와의 연결)로 '5'를 매겼다 [가정]. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음.
```

### runs/parked/2026-10-09-04/research.md (보류: 형식 검증 실패가 형식 수정 재작성 2회 뒤에도 남음(runs/2026-10-09-04/format_check.md))

```markdown
# 리서치 브리프 2026-10-09-04

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-09-04 |
| 날짜 | 2026-10-09 |
| 실행 유형 | category_link (대분류 연결) |
| 대상 영역 | 해당 없음 |
| 대분류 | I. 설계·시뮬레이션 |

## 갭(비어 있거나 약한 섹션)

- I. 설계·시뮬레이션 대분류 페이지의 '다른 대분류와의 연결' 절이 '아직 작성되지 않음' 상태다
- 게시된 33. 시나리오 모델·편집, 34. 시뮬레이션·예측용 디지털 트윈, 35. 처리능력·규모·배치 설계, 36. 가상 시운전·실제 상황 재현 페이지에는 영역 단위 연결(10절)만 있고, 대분류 단위로 묶은 연결은 없다
- 34. 시뮬레이션·예측용 디지털 트윈과 35. 처리능력·규모·배치 설계 페이지는 이전 분류(2026-09-25) 기준으로 쓰여 C. 채팅 기반 구성·운영, L. AI·학습 기술, M. 안전, N. 보안·개인정보, P. 거버넌스·법규·사회와 잇는 근거가 없다
- H. 실행·협업·예외 복구(32 제외), J. 현장 운영·관제의 40. 운영 절차·요청 창구, K. 플랫폼 아키텍처·인프라의 41. 플랫폼 아키텍처·외부 API, N. 보안·개인정보의 53. 개인정보·영상 데이터와의 연결 근거가 게시 페이지에 없다

## 조사 질문

1. 현장을 바꾸거나 로봇을 늘리기 전에 가상으로 설계하고 결과를 미리 볼 수 있는가? [분류원문]
2. I. 설계·시뮬레이션의 네 세부영역은 C. 채팅 기반 구성·운영(9. 채팅으로 시나리오 구성, 11. 채팅으로 실제 상황 시뮬레이션 재현)과 L. AI·학습 기술(44. 로봇 기반 모델·언어 모델 계획, 47. AI·학습·적응과 모델 운영)에서 무엇을 받고 무엇을 넘기는가?
3. 34. 시뮬레이션·예측용 디지털 트윈과 36. 가상 시운전·실제 상황 재현은 F. 연동(20·21·22·23)의 어떤 인터페이스를 가상으로 대신해 시험하며, O. 검증·도입·수명주기(54·55)와 B. 로봇 온톨로지(4·7)로 무엇을 넘기는가?
4. 35. 처리능력·규모·배치 설계와 34. 시뮬레이션·예측용 디지털 트윈의 결과는 G. 계획·최적화(25. 작업 배정 — MRTA ~ 28. 공용 자원·충전·에너지 최적화)의 결정과 어떻게 맞물리는가?
5. 36. 가상 시운전·실제 상황 재현은 E. 사물·사람·실시간 상태(18·19)와 J. 현장 운영·관제(37·38)의 상태·기록을 어떻게 원천으로 쓰며, 18. 실시간 세계 상태·데이터 일관성의 현재 상태 표현과 34. 시뮬레이션·예측용 디지털 트윈의 미래 실험을 어떻게 구분하는가?
6. 시뮬레이션·디지털 트윈은 M. 안전, N. 보안·개인정보, P. 거버넌스·법규·사회, A. 기획·사업, Q. 현장 유형별 적용과 어디서 만나는가(한국 자료 포함)?

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | C. 채팅 기반 구성·운영의 9. 채팅으로 시나리오 구성 ↔ I. 설계·시뮬레이션의 33. 시나리오 모델·편집: Chat2Scenic(2026-07)은 챗봇 인터페이스로 시나리오를 대화로 다듬으면서 검색 증강 방식으로 도메인 특화 언어(DSL) 시나리오 스크립트를 만들고, 123개 시나리오 벤치마크에서 컴파일 성공률 76.42%(비교 방법 30.08%·16.26%)를 보고했다. | ref-1329 | 아니오 | medium | 2026-07-15 | — | — |
| f2 | [추정] | C. 채팅 기반 구성·운영의 9. 채팅으로 시나리오 구성·13. 대화형 기능의 신뢰·기반 ↔ I. 설계·시뮬레이션의 33. 시나리오 모델·편집: 대화로 만든 시나리오의 출력 형식은 33. 시나리오 모델·편집이 정하는 매개변수화·장애 선언 형식이 되고, 생성 스크립트가 컴파일되지 않는 경우가 남으므로 승인 전 형식 검사가 두 대분류의 인계 지점이 될 것으로 보인다. | ref-1329, ref-1088, ref-528 | 아니오 | low | 2026-10-09 | — | — |
| f3 | [사실] | C. 채팅 기반 구성·운영의 11. 채팅으로 실제 상황 시뮬레이션 재현 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈: Xia 외(2026-08, ETFA 2026 채택)는 언어 모델 에이전트가 사용자 질의와 기준 구성을 받아 비교 시뮬레이션을 설계·실행하고 결과를 해석해 공정 매개변수 변경을 권고하는 다중 에이전트 틀을 제약 공정 설계에 적용했다. | ref-1330 | 아니오 | medium | 2026-08-22 | — | — |
| f4 | [추정] | C. 채팅 기반 구성·운영의 11. 채팅으로 실제 상황 시뮬레이션 재현 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현: 대화로 조건을 바꿔 비교하는 일은 언어 모델이 34쪽 시뮬레이션 실험을 설계·실행하는 구조로 이어질 것으로 보이나, 비교 결과를 믿으려면 36쪽 재현 충실도 지표가 함께 필요하고 로봇 플릿에 적용한 사례는 확인하지 못했다. | ref-1330, ref-1127 | 아니오 | low | 2026-10-09 | — | — |
| f5 | [사실] | L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획 ↔ I. 설계·시뮬레이션의 33. 시나리오 모델·편집: Holodeck(CVPR 2024)은 GPT-4가 장면 구성과 객체 간 공간 관계를 만들고 배치를 최적화해 글 지시로 3D 환경을 생성하며, 생성 장면에서 학습한 에이전트가 처음 보는 환경에서 주행했다고 보고했다. | ref-815 | 아니오 | medium | 2023-12-14 | — | — |
| f6 | [추정] | L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획 ↔ I. 설계·시뮬레이션의 33. 시나리오 모델·편집: 언어 모델·생성 모델로 시뮬레이션 환경을 만드는 연구(Holodeck, Arena 4.0)가 33의 예제 라이브러리를 채우는 수단이 될 수 있으나, 생성 환경은 실제 현장 지도가 아니므로 D. 공간·지도 모델의 도면·현장 정합과 구분해야 할 것으로 보인다. | ref-815, ref-1089 | 아니오 | low | 2026-10-09 | — | — |
| f7 | [추정] | E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈: 제조 분야 분류 자료가 데이터 흐름 자동화 정도로 디지털 모델·디지털 섀도·디지털 트윈을 구분하므로, 18은 현장 상태를 가상 모델에 반영하는 현재 상태 표현을, 34는 그 모델을 복제해 가정한 미래를 실험하는 쪽을 맡는 것이 분류 원문의 구분과 맞을 것으로 보인다. | ref-291 | 아니오 | low | 2018 | — | 원문 미열람 |
| f8 | [사실] | F. 연동의 22. 설비·건물 시스템 연동 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈: Open-RMF 시뮬레이션은 문·승강기 플러그인이 실제와 같은 문·승강기 요청에 응답하고, door_supervisor 가 충돌을 막고 lift_supervisor 가 여러 플릿의 승강기 요청을 관리하며, TeleportDispenser·TeleportIngestor 가 배송 작업의 적재·하역을 흉내 낸다. | ref-406 | 아니오 | medium | 2026-10-09 | — | — |
| f9 | [사실] | F. 연동의 20. 로봇·제조사 관제 연동 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈: Open-RMF 의 slotcar 플러그인은 플릿 어댑터의 경로·모드 요청을 받아 로봇 상태를 발행하는 전체 제어 로봇 모델로, 경유점 사이를 레일식 직선으로 움직이고 막히면 멈추며 로봇마다 주행 스택 전체를 돌리는 계산 비용을 피한다. | ref-406 | 아니오 | medium | 2026-10-09 | — | — |
| f10 | [사실] | O. 검증·도입·수명주기의 54. 시험·형식 검증·벤치마크·55. 현장 조사·설치·시운전 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현: Open-RMF 문서는 시뮬레이션이 하드웨어 시험의 준비·정지·초기화 부담을 덜고, 시나리오를 반복해 수정을 확인하고 드문 예외를 살피며, 장시간 시뮬레이션으로 배치 전에 시설 소유자의 확신을 높인다고 설명한다. | ref-406 | 아니오 | medium | 2026-10-09 | — | — |
| f11 | [추정] | O. 검증·도입·수명주기의 55. 현장 조사·설치·시운전 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: 설비 제어 분야의 가상 시운전 정의(VDI/VDE 3693)와 실제 제어기·가상화 인스턴스를 섞은 분산 가상 시운전 연구가 있어 36의 결과가 55의 현장 시운전 준비로 넘어갈 것으로 보이나, 여러 제조사 로봇 플릿 전체를 대상으로 한 가상 시운전 절차는 확인하지 못했다(oq-255). | ref-1126, ref-1130, ref-406 | 아니오 | low | 2026-10-09 | — | — |
| f12 | [사실] | G. 계획·최적화의 25. 작업 배정 — MRTA ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: VirTooS(2026-08)는 ROS 2와 Unity 게임 엔진을 결합한 혼합 현실 환경에서 실제·가상 로봇과 실제·가상 센서를 함께 써서 자율이동로봇 팀의 플릿 관리 작업을 시험하는 도구이며, 작업 배정 예제에서 실제 로봇과 가상 로봇이 상호작용한다. | ref-1129 | 아니오 | medium | 2026-08-26 | — | — |
| f13 | [추정] | K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: 가상 시운전 도구가 여러 머신에 컨테이너로 배포되고 시뮬레이션 플러그인이 실제와 같은 요청 메시지에 응답하므로, 가상 대응물을 어느 계산 자원에 두고 실제 시스템과 어떤 통신으로 잇는지가 두 대분류를 잇는 설계 쟁점이 될 것으로 보인다. | ref-1129, ref-406 | 아니오 | low | 2026-10-09 | — | — |
| f14 | [사실] | G. 계획·최적화의 28. 공용 자원·충전·에너지 최적화 ↔ I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계: 한 유통사 물류센터 시뮬레이션 연구(2025)에서는 충전기가 부족하면 큰 지연이, 남으면 불필요한 비용이 생겼고, 로봇 이동형 풀필먼트 시스템의 충전·배터리 교환 전략 비교(2018)와 창고 충전소 배치 최적화(2024) 연구도 있다. | ref-102, ref-098, ref-109 | 아니오 | medium | 2025 | 물류창고 / 제약 | 원문 미열람 |
| f15 | [사실] | G. 계획·최적화의 25. 작업 배정 — MRTA ↔ I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계: Open-RMF 플릿 어댑터 템플릿 설정에서는 배터리가 recharge_threshold 아래인 로봇이 작업을 맡지 않으므로, 충전 설비 계획의 결과가 배정 가능한 로봇 수를 좌우하는 운영 설정으로 이어진다. | ref-105 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f16 | [사실] | G. 계획·최적화의 26. 작업 순서·스케줄링 ↔ I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계: 랙 이동 로봇 작업대의 주문·랙 순서를 함께 정한 Boysen 외(2017)는 최적화된 주문 처리가 흔한 단순 규칙보다 필요한 로봇 대수를 절반 넘게 줄였다고 보고했다(저자 계산 실험 조건). | ref-381 | 아니오 | medium | 2017 | 물류창고 / 예외·성과 | 원문 미열람 |
| f17 | [사실] | G. 계획·최적화의 25. 작업 배정 — MRTA ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈: RAWSim-O 는 로봇 이동형 풀필먼트 시스템의 여러 결정 문제를 연구하는 이산 사건 시뮬레이션이며, Merschformann 외(2019)의 시뮬레이션 조건에서는 피킹 주문 배정 규칙이 단위 처리량을 크게 바꾸었다. | ref-101, ref-398 | 아니오 | medium | 2019 | 물류창고 / 예외·성과 | 원문 미열람 |
| f18 | [사실] | G. 계획·최적화의 27. 다중 로봇 경로·교통 관리 — MAPF ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈: 다중 AGV 시스템의 경로망을 시뮬레이션으로 자동 설계하는 연구(IEEE TASE, 2024)가 있어 경로망 배치 평가가 가정한 미래를 실험하는 쪽에 걸친다. | ref-267 | 아니오 | medium | 2024 | — | 원문 미열람 |
| f19 | [사실] | G. 계획·최적화의 27. 다중 로봇 경로·교통 관리 — MAPF ↔ I. 설계·시뮬레이션의 33. 시나리오 모델·편집: Moving AI Lab 의 MAPF 벤치마크는 지도와 시나리오 파일을 묶어 공개해 경로 계획기를 같은 조건에서 비교하게 하므로, 경로 계획 평가가 시나리오 형식·라이브러리와 맞닿는다. | ref-1091 | 아니오 | medium | 2026-10-09 | — | 원문 미열람 |
| f20 | [사실] | F. 연동의 22. 설비·건물 시스템 연동·Q. 현장 유형별 적용의 63. 병원·의료 ↔ I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계·36. 가상 시운전·실제 상황 재현: 고려대학교 구로병원의 약품 배송 로봇 기록(2025-06, 122건)과 몬테카를로 재현에서 승강기 가동률 59.01% 이하일 때 배송 성공률 95.5%, 90% 초과에서 실패가 몰렸다. | ref-943 | 아니오 | medium | 2026-03-31 | 병원 / 제약 | 원문 미열람 |
| f21 | [사실] | F. 연동의 22. 설비·건물 시스템 연동·Q. 현장 유형별 적용의 64. 상업 시설 ↔ I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계: 다층 호텔의 배송 로봇 경로 계획 연구는 승강기를 경로 계획 안의 대기·운행 시간으로 모델링했다. | ref-103 | 아니오 | medium | 2026-10-09 | 상업 시설 / 제약 | 원문 미열람 |
| f22 | [의견] | G. 계획·최적화의 25. 작업 배정 — MRTA·Q. 현장 유형별 적용의 63. 병원·의료 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: Lee 외 저자들은 승강기 가동률을 혼잡 인지 배차의 제어 신호로 쓰고, 병원별 구조·통행·승강기 제어 정책을 재현한 병원 디지털 트윈으로 배치 전에 결과의 일반화 가능성을 부하 시험하자고 제안했다. | ref-943 | 아니오 | medium | 2026-03-31 | 병원 / 예외·성과 | 원문 미열람 |
| f23 | [사실] | H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성 ↔ I. 설계·시뮬레이션의 33. 시나리오 모델·편집: NIST ARIAC 는 컨베이어 고장, 전압 시험기 고장, 진공 그리퍼 파지 실패, 긴급 주문을 매개변수로 선언해 시각이나 발생 횟수 조건으로 시나리오에 주입한다. | ref-528 | 아니오 | medium | 2026-10-09 | 제조 공장 / 예외·성과 | — |
| f24 | [추정] | G. 계획·최적화의 24. 작업·워크플로 모델링 ↔ I. 설계·시뮬레이션의 33. 시나리오 모델·편집: 로봇 미션 명세·실행 형식 비교 연구와 행동 트리 편집기(Groot2)가 33의 미션 기술 형식·편집기 선택 근거로 쓰였으므로, 시나리오 안의 작업 표현은 24의 단계·선후관계·완료 조건 표현과 같은 형식을 공유해야 할 것으로 보인다. | ref-116, ref-1090 | 아니오 | low | 2026-10-09 | — | 원문 미열람 |
| f25 | [사실] | D. 공간·지도 모델의 14. 도면·BIM에서 지도 만들기·15. 지도·공간·위치 모델·16. 장소 의미·지도 관리 ↔ I. 설계·시뮬레이션의 33. 시나리오 모델·편집·34. 시뮬레이션·예측용 디지털 트윈: Open-RMF 의 building_map_generator 는 traffic-editor 로 주석한 건물 파일에서 층별 바닥·벽 메시와 문·승강기·로봇을 담은 시뮬레이션 월드를 만들고, 환경을 바꿀 때는 주석만 고쳐 다시 생성하면 된다. | ref-406, ref-079 | 아니오 | medium | 2026-10-09 | — | — |
| f26 | [추정] | B. 로봇 온톨로지의 4. 이기종 로봇 등록 ↔ I. 설계·시뮬레이션의 33. 시나리오 모델·편집·34. 시뮬레이션·예측용 디지털 트윈: 시나리오가 참조하는 로봇 모델은 SDFormat 같은 로봇·환경 기술 형식으로 시뮬레이터에 들어가므로, 4의 기종 제원 기술(형상·질량·센서 등)이 시뮬레이션 자산의 원천으로 이어질 것으로 보인다. | ref-1092 | 아니오 | low | 2026-10-09 | — | 원문 미열람 |
| f27 | [사실] | J. 현장 운영·관제의 37. 관제 화면·실행 기록·38. 모니터링·이상 탐지·원인 분석 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: rosbag2 는 ROS 2 통신을 시각이 찍힌 백 파일(기본 MCAP)로 기록하고, 재생 속도 조절·/clock 발행·시작 시각 지정·토픽 선택·여러 백 파일의 기록 시각순 동시 재생을 지원한다. | ref-831 | 아니오 | medium | 2026-10-09 | — | — |
| f28 | [추정] | J. 현장 운영·관제의 37. 관제 화면·실행 기록 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: 메시지 단위 기록 도구와 기록 기반 시뮬레이터가 있으나, 재현의 원천은 37이 남기는 오케스트레이션 수준 실행 기록(작업·배정·위치·사건 시각)이어야 할 것으로 보이며 이를 시나리오 사양으로 바꾸는 공개 형식은 확인하지 못했다(oq-131). | ref-831, ref-1128 | 아니오 | low | 2026-10-09 | — | — |
| f29 | [사실] | E. 사물·사람·실시간 상태의 19. 사람·보행자 모델 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: Waymax(2023)는 실제 주행 기록으로 다중 에이전트 주행 시뮬레이션을 초기화하거나 재생하고, 사실적 상호작용을 위해 학습된 행동 모델과 규칙 기반 행동 모델을 제공한다. | ref-1128 | 아니오 | medium | 2023-10-12 | — | — |
| f30 | [사실] | E. 사물·사람·실시간 상태의 19. 사람·보행자 모델·M. 안전의 49. 사람 근접 안전 ↔ I. 설계·시뮬레이션의 33. 시나리오 모델·편집·34. 시뮬레이션·예측용 디지털 트윈: Open-RMF 시뮬레이션은 menge 로 가상 사람을 움직이는 선택 기능 crowdsim 을 traffic-editor 에서 켤 수 있고, 공항 터미널 예제 월드가 이를 군중 시뮬레이션으로 쓴다. | ref-406, ref-104 | 아니오 | medium | 2026-10-09 | 상업 시설 / 제약 | — |
| f31 | [사실] | O. 검증·도입·수명주기의 54. 시험·형식 검증·벤치마크 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: Kadian 외(RA-L 2020)는 시뮬레이션–현실 상관 계수(SRCC)를 제안하고, LoCoBot 의 PointGoal 주행에서 Habitat 기본 설정의 성공률 SRCC 가 0.18 이었으나 시뮬레이션 매개변수를 조정해 0.844 로 높였다고 보고했다. | ref-1127 | 아니오 | medium | 2020-08 | — | — |
| f32 | [추정] | L. AI·학습 기술의 47. AI·학습·적응과 모델 운영 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: 학습 정책이 시뮬레이터의 결함을 악용하는 현실 격차가 보고되므로, 학습 기반 정책의 현실 격차 보정은 47쪽(및 로봇 제조사·시뮬레이션 도구) 일이고 36은 재현 결과와 실제의 차이 지표를 관리하는 쪽을 맡는 것으로 보인다. | ref-741, ref-1127 | 아니오 | low | 2026-10-09 | — | — |
| f33 | [사실] | O. 검증·도입·수명주기의 54. 시험·형식 검증·벤치마크 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: NASA-STD-7009B(2024-03-05)는 모델·시뮬레이션 결과를 의사결정에 쓸 때의 수용과 신뢰도 평가를 다루는 표준이다. | ref-1133 | 아니오 | medium | 2024-03-05 | — | 원문 미열람 |
| f34 | [추정] | B. 로봇 온톨로지의 7. 온톨로지 검증·변경 관리 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: 7이 능력 정의에 붙이는 지원 단계(시뮬레이션 연결·시뮬레이션 검증·실기 검증)를 판정하려면 36의 시뮬레이션 신뢰도 평가와 시뮬레이션–현실 상관 지표가 기준이 될 수 있으나, 두 체계를 대응시킨 자료는 확인하지 못했다(oq-156). | ref-1133, ref-1127 | 아니오 | low | 2026-10-09 | — | — |
| f35 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현: Huck·Ledermann·Kröger(SPCE 2020)는 사람 모델과 최적화 알고리즘으로 시뮬레이션 안에서 고위험 사람 행동을 생성해, 물리 시제품이 없는 초기 설계 단계의 산업용 로봇 셀에서 작업자 위험을 드러내는 방법을 개념 증명으로 보였다. | ref-1331 | 아니오 | medium | 2020-11-20 | 예외·성과 | — |
| f36 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ I. 설계·시뮬레이션의 33. 시나리오 모델·편집: 위험 상황을 생성·탐색하는 시뮬레이션 시험(사람 행동 최적화, 확률적 시나리오 언어 기반 반증)이 있으므로, 33에서 선언한 장애·사람 흐름 시나리오가 48의 위험 식별 입력이 될 수 있을 것으로 보이나 다중 이동로봇 플릿에 적용한 사례는 확인하지 못했다. | ref-1331, ref-1086 | 아니오 | low | 2026-10-09 | — | — |
| f37 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: Carr 외(2022)는 물리 로봇과 동기화된 ROS 기반 로봇의 디지털 트윈에 중간자 공격을 가하면 그 영향이 물리 시스템으로 전파될 수 있으며 산업용 로봇과 자율이동로봇 모두에 해당한다고 보고했다. | ref-1332 | 아니오 | medium | 2022-11-17 | — | — |
| f38 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리·52. 통신 보호·위협 관리·감사 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: 36이 다루는 디지털 트윈 동기화(실시간 상태를 가상 모델에 반영하고 결과를 되돌리는 경로)는 공격 표면이 될 수 있으므로, 시뮬레이션 결과가 실제 계획·설정에 반영되는 경로에 접근통제와 무결성 확인이 필요할 것으로 보인다. | ref-1332 | 아니오 | low | 2026-10-09 | — | — |
| f39 | [사실] | P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현: Gazebo(클래식) 모델 데이터베이스 규칙은 database.config 의 license 요소로 모델 라이선스를 지정하고 CC BY 3.0 Unported 를 권장하며, 각 모델의 model.config 에 작성자 이름·이메일을 필수로 적게 한다. | ref-1239 | 아니오 | medium | 2026-10-09 | — | 원문 미열람 |
| f40 | [사실] | F. 연동의 21. 상호운용 표준·적합성 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈: 제조용 디지털 트윈 프레임워크 ISO 23247 은 국내에 KS X ISO 23247-1 로 들어와 있고 2026년 디지털 트윈 결합을 다루는 제6부가 발행되었으나, 물류센터 이종 로봇·설비에 그대로 쓸 수 있는지는 확인되지 않았다(oq-085). | ref-516, ref-518 | 아니오 | medium | 2026 | — | 원문 미열람 |
| f41 | [추정] | 연계 대상: F. 연동의 23. 업무 시스템 연동 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈: 성수기 주문·물동량 전망 같은 시나리오 입력은 상위 업무 시스템의 수요예측에서 받는 것으로 보이며, 물류·공급망 디지털 트윈 검토는 실제 데이터로 검증한 연구가 소수라고 보고한다. | ref-521 | 아니오 | low | 2024 | 물류창고 / 시작 조건 | 원문 미열람 |
| f42 | [사실] | F. 연동의 22. 설비·건물 시스템 연동·Q. 현장 유형별 적용의 65. 가정·공동주택 ↔ I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계: 업무용 건축물 대상 로봇 친화형 건축물 인증을 아파트 단지로 확장한 국내 인증 모델(2023)은 건축·시설 설계, 네트워크·시스템, 건축 운영 관리, 로봇 지원 4개 분야 28개 항목(총점 176점)으로 구성된다. | ref-409 | 아니오 | medium | 2023 | 가정 / 제약 | 원문 미열람 |
| f43 | [추정] | J. 현장 운영·관제의 39. 운영 성과 측정·개선 ↔ I. 설계·시뮬레이션의 35. 처리능력·규모·배치 설계: 충전 방식의 비용 비교와 국내 스마트물류센터 인증 평가에서 두 영역이 만나는 것으로 보이나, 인증 세부 지표에 로봇 대수·가동률 같은 설비 계획 지표가 들어가는지는 확인하지 못했다(oq-011). | ref-098, ref-106 | 아니오 | low | 2026-10-09 | 물류창고 | 원문 미열람 |
| f44 | [추정] | A. 기획·사업의 3. 경제성·조달·사업 모델 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: Rockwell Automation 사례 소개는 미국 남부 물류센터 구축에서 통합자가 컨베이어·피킹 모듈 제어를 설치 전에 에뮬레이션으로 검증해 전체 프로젝트 기간을 18% 줄이고 현장 시운전을 5주 단축했다고 밝히지만 기준선과 측정 방법은 공개하지 않았다. | ref-1165 | 아니오 | low | 2024-08-28 | 물류창고 / 예외·성과 | 원문 미열람, 벤더 주장 |
| f45 | [사실] | Q. 현장 유형별 적용의 62. 제조 공장 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: 최성욱·박상철·왕지남(2008)은 자동차 차체 생산라인의 PLC 코드 검증을 위해 실제 PLC 와 3D 가상 공정 시뮬레이터를 양방향 통신으로 잇는 가상 플랜트 구축 절차를 제안했다. | ref-1131 | 아니오 | medium | 2008-11 | 제조 공장 | 원문 미열람 |
| f46 | [사실] | Q. 현장 유형별 적용의 64. 상업 시설 ↔ I. 설계·시뮬레이션의 33. 시나리오 모델·편집: Open-RMF 예제 호텔 월드는 로봇 플릿 3개(로봇 4대)·승강기 2대·여러 문을 담고, 공항 터미널 월드는 대형 지도에 선택적 군중 시뮬레이션과 읽기 전용 카트를 더해 순찰·배송·청소를 실행하는 시뮬레이션 예제다. | ref-104 | 아니오 | medium | 2026-10-09 | 상업 시설 / 수행 자원 | 원문 미열람 |
| f47 | [사실] | Q. 현장 유형별 적용의 65. 가정·공동주택 ↔ I. 설계·시뮬레이션의 33. 시나리오 모델·편집: BEHAVIOR-1K 는 설문으로 고른 일상 가정 활동 1,000개를 BDDL 로 명세하고 장면 50개와 주석 객체 9,000개 이상을 OmniGibson 시뮬레이터에 구현한 벤치마크다. | ref-971 | 아니오 | medium | 2024-03-14 | 가정 / 작업 대상 | 원문 미열람 |
| f48 | [추정] | A. 기획·사업의 1. 기술·시장·업체 동향 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈: NVIDIA 는 산업용 로봇 플릿 디지털 트윈을 만드는 'Mega' Omniverse 블루프린트를 발표하며 센서 시뮬레이션·합성 데이터 기반의 배치 전 플릿 검증을 내세운다. | ref-527 | 아니오 | low | 2026-10-09 | — | 원문 미열람, 벤더 주장 |
| f49 | [추정] | Q. 현장 유형별 적용의 61. 물류창고 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈: CJ대한통운은 2021-11 현실 물류센터와 같은 가상 물류센터를 단계적으로 구축해 2023년 디지털 트윈을 완성하겠다는 계획을 발표했고 작업 동선·재고 배치·설비 효율 최적화를 목표로 들었으나, 이후 적용 결과는 확인하지 못했다. | ref-526 | 아니오 | low | 2021-11 | 물류창고 | 원문 미열람, 벤더 주장 |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1329 | Gao, Y., Miao, W., Piccinini, M., Wang, H., Song, Q., & Betz, J. (TUM 외, arXiv; IROS 2026 채택으로 검색 결과에 표시) | Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving | 2026-07-15 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2607.14387 | 아니오 |
| ref-1330 | Xia, Y., Weyrich, M., Jazdi, N. 외 (University of Stuttgart·AstraZeneca, arXiv; ETFA 2026 채택) | LLM Agents Perform Controlled Experiments Using Simulation Models | 2026-08-22 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2608.23622 | 아니오 |
| ref-1331 | Huck, T. P., Ledermann, C., & Kröger, T. (arXiv; SPCE 2020) | Simulation-based Testing for Early Safety-Validation of Robot Systems | 2020-11-20 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2011.10294 | 아니오 |
| ref-1332 | Carr, C., Wang, S., Wang, P., & Han, L. (arXiv) | Attacking Digital Twins of Robotic Systems to Compromise Security and Safety | 2022-11-17 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2211.09507 | 아니오 |
| ref-406 | Open Robotics | Simulation - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://osrf.github.io/ros2multirobotbook/simulation.html | 아니오 |
| ref-831 | ROS 2 (ros2/rosbag2 GitHub) | rosbag2 — README (Recording and playback of ROS 2 communications) | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/ros2/rosbag2 | 아니오 |
| ref-1128 | Gulino, C., Fu, J., Luo, W. 외 (Waymo, arXiv) | Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research | 2023-10-12 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2310.08710 | 아니오 |
| ref-1129 | Drudi, A., Pichierri, L., Testa, A., & Notarstefano, G. (arXiv) | VirTooS: A ROS 2 - Unity Virtualization Toolkit for Fleet Management of Autonomous Mobile Robots | 2026-08-26 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2608.26066 | 아니오 |
| ref-815 | Yang, Y., Sun, F.-Y., Weihs, L. 외 (Allen Institute for AI 등) | Holodeck: Language Guided Generation of 3D Embodied AI Environments | 2023-12-14 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2312.09067 | 아니오 |
| ref-1127 | Kadian, A., Truong, J., Gokaslan, A., Clegg, A., Wijmans, E., Lee, S., Savva, M., Chernova, S., & Batra, D. (arXiv / IEEE RA-L) | Sim2Real Predictivity: Does Evaluation in Simulation Predict Real-World Performance? | 2020-08 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/1912.06321 | 아니오 |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — Demonstrations of Open-RMF (README) | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/open-rmf/rmf_demos | 예 |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml | 아니오 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 아니오 |
| ref-101 | Merschformann, M. (RAWSim-O GitHub) | RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README) | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/merschformann/RAWSim-O | 예 |
| ref-398 | Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L. | Decision rules for robotic mobile fulfillment systems | 2019 | 논문 | medium | 2026-10-09 | https://www.sciencedirect.com/science/article/pii/S2214716019300946 | 예 |
| ref-267 | IEEE 게재 논문 저자(미확인) | Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)) | 2024 | 논문 | medium | 2026-10-09 | https://ieeexplore.ieee.org/document/10287275/ | 예 |
| ref-098 | Zou, B., Gong, Y., de Koster, R., & Xu, X. | Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system | 2018 | 논문 | medium | 2026-10-09 | https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901 | 예 |
| ref-109 | Stark, H.-G. 외 | A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse | 2024-06 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2406.17003 | 예 |
| ref-102 | Springer(FAIM 2025 발표 논문, 저자 미확인) | Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics | 2025 | 논문 | medium | 2026-10-09 | https://link.springer.com/chapter/10.1007/978-3-032-07675-5_69 | 예 |
| ref-381 | Boysen, N., Briskorn, D., & Emde, S. | Parts-to-picker based order processing in a rack-moving mobile robots environment | 2017 | 논문 | medium | 2026-10-09 | https://www.sciencedirect.com/science/article/abs/pii/S0377221717302758 | 예 |
| ref-943 | Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 2026-03-31 | 논문 | medium | 2026-10-09 | https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/ | 예 |
| ref-103 | PMC 게재 논문(저자 미확인) | The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments | 미확인 | 논문 | medium | 2026-10-09 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/ | 예 |
| ref-528 | NIST (usnistgov/ARIAC_docs) | ARIAC 2025 Documentation — Challenges | 미확인 | 정부·연구기관 | medium | 2026-10-09 | https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html | 아니오 |
| ref-1088 | ASAM e.V. | ASAM OpenSCENARIO® XML | 미확인 | 표준 | medium | 2026-10-09 | https://www.asam.net/standards/detail/openscenario-xml/ | 예 |
| ref-1089 | Shcherbyna, V. 외 (arXiv) | Arena 4.0: A Comprehensive ROS2 Development and Benchmarking Platform for Human-centric Navigation Using Generative-Model-based Environment Generation | 2024-09 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2409.12471 | 예 |
| ref-116 | Filippone, G., Pettinari, S., & Pelliccione, P. | Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis | 2026-03 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2603.15427 | 예 |
| ref-1090 | BehaviorTree.CPP 프로젝트 (behaviortree.dev) | Groot2 | 미확인 | 벤더 문서 | medium | 2026-10-09 | https://www.behaviortree.dev/groot/ | 예 |
| ref-1091 | Moving AI Lab (Sturtevant 외) | MAPF Benchmarks | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://movingai.com/benchmarks/mapf/index.html | 예 |
| ref-1092 | Open Source Robotics Foundation | SDFormat (Simulation Description Format) | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | http://sdformat.org/ | 예 |
| ref-1086 | Vin, E., Kashiwa, S., Rhea, M., Fremont, D. J., Kim, E., Dreossi, T., Ghosh, S., Yue, X., Sangiovanni-Vincentelli, A. L., & Seshia, S. A. (CAV 2023, arXiv) | 3D Environment Modeling for Falsification and Beyond with Scenic 3.0 | 2023-07 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2307.03325 | 예 |
| ref-971 | Li, C., Zhang, R., Wong, J. 외 (arXiv; CoRL 2022 예비판) | BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation | 2024-03-14 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2403.09227 | 예 |
| ref-291 | Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W. | Digital Twin in manufacturing: A categorical literature review and classification | 2018 | 논문 | medium | 2026-10-09 | https://www.sciencedirect.com/science/article/pii/S2405896318316021 | 예 |
| ref-521 | Le, T. V., & Fan, R. | Digital twins for logistics and supply chain systems: Literature review, conceptual framework, research potential, and practical challenges | 2024 | 논문 | medium | 2026-10-09 | https://www.sciencedirect.com/science/article/abs/pii/S0360835223007921 | 예 |
| ref-516 | 한국표준협회 KSSN(국가표준인증종합정보센터) | KS X ISO 23247-1 자동화 시스템 및 통합 — 제조를 위한 디지털 트윈 프레임워크 — 제1부: 개요 및 일반 원리 | 미확인 | 표준 | medium | 2026-10-09 | https://www.kssn.net/search/stddetail.do?itemNo=K001010140724 | 예 |
| ref-518 | ISO | ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition | 2026 | 표준 | medium | 2026-10-09 | https://www.iso.org/standard/87426.html | 예 |
| ref-1126 | VDI/VDE (VDI/VDE-Gesellschaft Mess- und Automatisierungstechnik) | VDI/VDE 3693 Blatt 1 - Virtual commissioning - Model types, terms, and definitions | 2025-05 | 표준 | medium | 2026-10-09 | https://www.vdi.de/en/home/vdi-standards/details/vdivde-3693-blatt-1-virtual-commissioning-model-types-terms-and-definitions | 예 |
| ref-1130 | Rosenberger, J., Selig, A., Ristic, M., Bühren, M., & Schramm, D. (Sensors 23(7):3545) | Virtual Commissioning of Distributed Systems in the Industrial Internet of Things | 2023-03-28 | 논문 | medium | 2026-10-09 | https://pmc.ncbi.nlm.nih.gov/articles/PMC10099255/ | 예 |
| ref-1131 | 최성욱, 박상철, 왕지남 (아주대학교, 대한산업공학회 추계학술대회) | 자동차 차체생산라인의 PLC 코드 검증을 위한 가상플랜트 구축 프로세스 | 2008-11 | 논문 | medium | 2026-10-09 | https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE01943794 | 예 |
| ref-1133 | NASA | NASA-STD-7009B Standard for Models and Simulations | 2024-03-05 | 표준 | medium | 2026-10-09 | https://standards.nasa.gov/standard/NASA/NASA-STD-7009 | 예 |
| ref-741 | Aljalbout, E. 외(University of Zurich·NVIDIA·University of Washington) | The Reality Gap in Robotics: Challenges, Solutions, and Best Practices | 2025-10 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2510.20808 | 예 |
| ref-1239 | Open Robotics (Gazebo Classic) | Gazebo : Tutorial : Model structure and requirements | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://classic.gazebosim.org/tutorials?tut=model_structure | 예 |
| ref-409 | 한국 학술지 게재 논문(지적과 국토정보 53(1), 83-105, 저자 미확인) | 아파트 단지의 로봇 친화형 환경 인증 모델 개발 (지적과 국토정보 53(1), 83-105) | 2023 | 논문 | medium | 2026-10-09 | https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART002978381 | 예 |
| ref-106 | 한국교통연구원(인증스마트물류센터) | 인증스마트물류센터 | 미확인 | 정부·연구기관 | medium | 2026-10-09 | https://cslc.koti.re.kr/ | 예 |
| ref-1165 | Rockwell Automation | Emulation Technology Speeds Up Warehouse Automation | 2024-08-28 | 벤더 문서 | low | 2026-10-09 | https://www.rockwellautomation.com/en-ca/company/news/case-studies/warehouse-design-digital.html | 예 |
| ref-527 | NVIDIA | NVIDIA Unveils 'Mega' Omniverse Blueprint for Building Industrial Robot Fleet Digital Twins | 미확인 | 벤더 문서 | low | 2026-10-09 | https://blogs.nvidia.com/blog/mega-omniverse-blueprint | 예 |
| ref-526 | CJ대한통운 | 가상세계 쌍둥이 창고로 물류 예측... CJ대한통운, 디지털 트윈 구축 (보도자료) | 2021-11 | 벤더 문서 | low | 2026-10-09 | https://www.cjlogistics.com/ko/newsroom/news/NR_00000905 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/design-and-simulation/index.md | 5. 다른 대분류와의 연결 | 대분류 연결 실행: '다른 대분류와의 연결' 절만 patches 로 채운다. 대분류별 finding — A. 기획·사업: f44(3. 경제성·조달·사업 모델, 벤더 주장), f48(1. 기술·시장·업체 동향, 벤더 주장) / B. 로봇 온톨로지: f26(4. 이기종 로봇 등록), f34(7. 온톨로지 검증·변경 관리, oq-156) / C. 채팅 기반 구성·운영: f1·f2(9. 채팅으로 시나리오 구성·13. 대화형 기능의 신뢰·기반), f3·f4(11. 채팅으로 실제 상황 시뮬레이션 재현) — 분류 원문 4장 주석(시나리오 구성과 실제 상황 재현은 33·36번)과 짝 / D. 공간·지도 모델: f25, f6 / E. 사물·사람·실시간 상태: f7(18↔34 원문 구분), f29·f30(19. 사람·보행자 모델) / F. 연동: f8(22), f9(20), f40(21, oq-085), f41(23, 연계 대상), f20·f21·f42(22 승강기·로봇 친화 공간) / G. 계획·최적화: f14(28), f15(25), f16(26), f17(25), f18·f19(27), f24(24), f12(25), f22 / H. 실행·협업·예외 복구: f23(32) / J. 현장 운영·관제: f27·f28(37·38, oq-131), f43(39) / K. 플랫폼 아키텍처·인프라: f13(42) / L. AI·학습 기술: f5·f6(44), f32(47) / M. 안전: f35·f36(48), f30(49) / N. 보안·개인정보: f37·f38(51·52) / O. 검증·도입·수명주기: f10·f11(54·55), f31·f33(54) / P. 거버넌스·법규·사회: f39(59, oq-292) / Q. 현장 유형별 적용: f20·f22(63), f21·f30·f46(64), f42·f47(65), f45(62), f49·f16·f17(61). 아직 다루지 않은 연결: H. 실행·협업·예외 복구의 29·30·31, J. 현장 운영·관제의 40, K. 플랫폼 아키텍처·인프라의 41·43, N. 보안·개인정보의 53, P. 거버넌스·법규·사회의 58·60. 18. 실시간 세계 상태·데이터 일관성(현재 상태 표현)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험)의 구분을 f7 로 명시. 다음 실행 후보: 34·35 페이지(이전 분류 기준)의 10절에 C·L·M·N·P 연결(f3·f5·f35·f37·f39) 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 슬롯카 모델 | Slotcar (Open-RMF simulated robot plugin) | Open-RMF 시뮬레이션에서 플릿 어댑터의 경로·모드 요청을 받아 경유점 사이를 레일식 직선으로 움직이는 단순화 로봇 모델로, 로봇마다 주행 스택 전체를 돌리지 않고 플릿 조율·설비 상호작용을 시험하게 한다. |
| 혼합 현실 시험 | Mixed-Reality Testing | 실제 로봇·센서와 가상 로봇·센서를 한 환경에 함께 두고 플릿 관리 같은 기능을 시험하는 방식으로, 모든 로봇을 실물로 갖추기 전에 작업 배정 등을 검증할 수 있게 한다. |

## 열린 질문

새로 생긴 질문:

- 대화로 생성한 로봇 시나리오가 형식상 실행 가능한지와 사용자 의도에 맞는지를 승인 전에 각각 어떤 검사로 확인하는가? | 관련 영역: 9. 채팅으로 시나리오 구성, 33. 시나리오 모델·편집, 13. 대화형 기능의 신뢰·기반 | 근거: f1 | 종류: 일반
- 실시간 상태를 가상 모델에 반영하고 시뮬레이션 결과를 실제 계획·설정에 되돌리는 디지털 트윈 동기화 경로에 대해, 로봇 플릿 플랫폼이 적용한 접근통제·무결성 확인 사례가 있는가? | 관련 영역: 36. 가상 시운전·실제 상황 재현, 52. 통신 보호·위협 관리·감사, 51. 인증·권한·격리 | 근거: f37 | 종류: 일반
- 사람 행동 모델로 고위험 상황을 생성하는 시뮬레이션 위험 식별 방법을 다중 이동로봇 플릿과 보행자가 많은 병원·상업 시설 공간에 적용한 사례가 있는가? | 관련 영역: 48. 안전·위험 관리, 34. 시뮬레이션·예측용 디지털 트윈, 19. 사람·보행자 모델 | 근거: f35 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 45 · 교차 확인: 0
- 예산 사용량: 검색 8회 · 신규 출처 4건
- 미확인 항목:
    - Valiollahi 외(Scientific Reports 2026, 제조 로봇 플릿·공장 배치 시나리오 기반 디지털 트윈)는 C. 채팅 기반 구성·운영 페이지 자료 목록에 ref-838 로 있으나 검색 2회로 원문을 찾지 못해 쓰지 않음
    - f1 Chat2Scenic 의 프레임워크 정확도 수치와 Scenic 언어 명시는 초록에서 확인하지 못해 claim 에서 뺌
    - f29 Waymax 의 구체적 행동 모델 종류(기록 재생·IDM 등)는 초록에 없어 미확인
    - f19 MAPF 벤치마크의 시나리오 파일 구성은 이번 실행에서 다시 열지 않았다(재인용)
    - Gazebo Fuel 의 모델 단위 라이선스 필드는 확인하지 못함(oq-292 유지)
    - 국내 물류센터에서 AMR 시운전 전 디지털 트윈 검증 결과를 수치로 공개한 사례 미확인(한국어 검색 결과는 계획·MOU 기사뿐)
    - f2·f4·f6·f13·f24·f26·f28·f32·f34·f36·f38·f41·f43 은 연결 해석([추정])이며 단일·재인용 근거
- 범위 경계 위반 의심:
    - f41: 수요예측은 원문 19장 상위 업무 시스템 경계의 외부 영역이므로 claim 을 '연계 대상: '으로 시작함
    - f20·f21·f8: 승강기·문 제어 자체는 시설·설비 제어 경계의 연계 대상이며 ROP 는 요청·상태 확인과 제약 입력만 맡는다고 발췌에 명시
    - f45·f11: PLC·컨베이어 제어 코드의 가상 시운전은 설비 업체·통합자 몫(연계 대상)으로, ROP 가상 시운전의 방법 근거로만 사용
    - f9·f32·f48: 로봇 자체 주행·인식 거동과 센서 시뮬레이션·현실 격차 보정은 로봇 제조사·시뮬레이터 제공자 쪽 연계 대상
    - f35·f36: 안전 인증·설비 안전 제어 판단은 연계 대상이며 시나리오가 위험 식별 입력이 될 수 있다는 범위로만 서술
- 한계: web_fetch_available: true · fetch_mode full. 대분류 연결(category_link) 실행으로 근거는 먼저 게시된 33·34·35·36 페이지와 A·B·F·G 대분류 페이지, 이전 브리프(2026-09-30-23)의 검증된 주장과 각주를 재사용했다. 검색 8회/30, 신규 출처 4건/15(ref-1329~ref-1332, 예약 구간 안). 재사용 출처 41건. 원문 열람: 신규 4건(arXiv 초록)과 재사용 6건(ref-406·ref-831 은 github_raw, ref-1128·ref-1129·ref-815·ref-1127 은 arXiv 초록 webfetch)을 이번에 열었고, 나머지 재사용 35건은 다시 열지 않아 fetched false·source_unopened true 로 표시했다. 입력 참고문헌 요약에 신뢰도 열이 없어 재사용 출처의 reliability 는 researcher.md 5절 유형 기준(미열람이면 medium 이하, 벤더 문서 low)으로 적었다. ref-381·ref-101·ref-409·ref-1239 는 이번 대상 페이지가 인용하지 않은 출처라 G·F 대분류 페이지 각주와 이전 브리프 2026-09-30-23 출처 표의 값을 옮겼다. ref-1329·ref-1330 은 C. 채팅 기반 구성·운영 페이지 자료 목록의 ref-833·ref-832 와 같은 논문일 가능성이 있으나 그 URL 을 입력에서 볼 수 없어 새 id 로 적었다(같은 URL 이면 퍼블리셔 병합 필요). 교차 확인 0건(대부분 연결 주장이 단일 출처 또는 서로 다른 내용의 출처 조합). 벤더 주장 3건(f44·f48·f49). 분류 원문 핵심 질문(현장을 바꾸거나 로봇을 늘리기 전에 가상으로 설계하고 결과를 미리 볼 수 있는가?)에는 대분류 연결 실행이므로 별도 답 finding 을 내지 않았고, 연결 근거로 f10(배치 전 시뮬레이션 이점)·f31(시뮬레이션 예측력 한계)·f41(실데이터 검증 부족)을 제시했다. L. AI·학습 기술 관련 finding(f5·f6·f32)은 적용 대상인 33. 시나리오 모델·편집·36. 가상 시운전·실제 상황 재현과 함께 제안했다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 f7 에서 구분했다. 현장 유형 근거는 물류창고(f14·f16·f17·f41·f43·f44·f49), 병원(f20·f22), 상업 시설(f21·f30·f46), 가정(f42·f47), 제조 공장(f23·f45)이며 실외·기타는 로봇 현장 근거가 없어 null 로 두었다. H. 실행·협업·예외 복구의 29·30·31, J. 현장 운영·관제의 40, K. 플랫폼 아키텍처·인프라의 41·43, N. 보안·개인정보의 53, P. 거버넌스·법규·사회의 58·60 연결은 근거를 찾지 않아 '아직 다루지 않은 연결'로 남긴다. 한국 자료는 재사용(ref-1131·ref-409·ref-106·ref-516·ref-526) 위주이며 한국어 검색 1회에서 새로 쓸 만한 1차 자료는 찾지 못했다. 기존 열린 질문은 해결하지 못했다(oq-085·oq-131·oq-156·oq-235·oq-255·oq-257·oq-258·oq-292 는 연결 서술에서 참조만 함). 정정 요청 없음. 우선 지정 질문 없음. 입력 누락 없음.
```

### runs/parked/2026-10-09-04/verification.md (보류 실행의 반려 사유)

```markdown
# 1차 검증(브리프) 2026-10-09-04

**판정: 조건부 승인** · 신뢰도: medium

## 주장별 검증

| finding | 출처 실재 | 주장 뒷받침 | 교차 확인 | 태그 처분 | 메모 |
|---|---|---|---|---|---|
| f1 | 예 | 예 | 아니오 | 유지 | arXiv 2607.14387 초록 열람 확인: 챗봇 인터페이스, RAG, DSL 스크립트, 123개 시나리오, CSR 76.42%·30.08%·16.26%, IROS 2026 채택. 단 C. 채팅 기반 구성·운영 페이지가 인용한 ref-833 과 저자·제목·발행일이 같은 논문이므로 ref-833 재사용 필요. |
| f2 | 예 | 예 | 아니오 | 유지 | 연결 해석 [추정] 유지. ref-528 은 원문 텍스트 입력으로 확인, ref-1088 은 원문 미열람(재인용). 근거 발췌의 '실행 불가'는 원문 지표가 컴파일 성공률이므로 '컴파일 실패'로 써야 함. ref-1329 → ref-833. |
| f3 | 예 | 예 | 아니오 | 유지 | arXiv 2608.23622 초록 열람 확인: 질의·기준 구성 → 실험 설계 → 비교 시뮬레이션 → 해석 → 공정 매개변수 권고, 제약 공정 설계, ETFA 2026 채택. ref-832 와 같은 논문이므로 ref-832 재사용 필요. |
| f4 | 예 | 예 | 아니오 | 유지 | 연결 해석 [추정] 유지. 근거 두 건(ref-1330=ref-832, ref-1127) 모두 열람 확인, 둘 다 로봇 플릿 대상 아님을 본문에 유지. |
| f5 | 예 | 예 | 아니오 | 유지 | arXiv 2312.09067 초록 열람 확인: GPT-4 상식·공간 제약, 배치 최적화, Objaverse, 생성 장면 학습 에이전트의 새 환경 주행, CVPR 2024 게재(v2 2024-04-22). |
| f6 | 예 | 예 | 아니오 | 유지 | [추정] 유지. ref-1089 는 이번 실행 원문 미열람(재인용, 33. 시나리오 모델·편집 페이지 각주와 일치). |
| f7 | 예 | 예 | 아니오 | 유지 | [추정] 유지. ref-291 원문 미열람, B. 로봇 온톨로지 대분류 페이지·E 대분류 연결 브리프(2026-10-09-03 f30)의 같은 주장과 같은 각주 재사용. 근거가 제조 대상이라는 한계 병기. |
| f8 | 예 | 예 | 아니오 | 유지 | ref-406 원문 텍스트(data/source_texts) 대조 확인: door_supervisor 의 문 충돌 방지, lift_supervisor 의 다플릿 요청 관리, TeleportDispenser·TeleportIngestor, 같은 메시지 교환 유지 문장. 발행일 미확인. |
| f9 | 예 | 예 | 아니오 | 유지 | ref-406 원문 대조 확인: full control 로봇 플러그인, PathRequest·ModeRequest 구독, 레일식 직선 주행, 장애물 감지 시 정지, 정적 장애물 없는 경로·2륜 차동 구동 가정, 주행 스택 계산 부담 회피. |
| f10 | 예 | 예 | 아니오 | 유지 | ref-406 원문 대조 확인(Motivation 절): 준비·정지·초기화 부담, 배터리·충돌 비용 없음, 반복 시나리오로 수정 확인, 드문 예외, 장시간 시뮬레이션의 시설 소유자 확신. |
| f11 | 예 | 예 | 아니오 | 유지 | [추정] 유지. ref-1126·ref-1130 은 이번 실행 원문 미열람(36. 가상 시운전·실제 상황 재현 페이지 검증 주장 재인용). PLC·설비 제어 가상 시운전은 연계 대상으로 서술해야 함. |
| f12 | 예 | 예 | 아니오 | 유지 | arXiv 2608.26066 초록 열람 확인: ROS 2·Unity, 혼합 현실, 가상·실제 LiDAR, ChoiRbot 분산 실험, 실제·가상 로봇 작업 배정 예제, 컨테이너 배포. |
| f13 | 예 | 예 | 아니오 | 유지 | [추정] 유지. 근거 출처 열람 확인. 플랫폼 배치 근거 없음(oq-040) 문구 유지. |
| f14 | 예 | 예 | 아니오 | 유지 | 35. 처리능력·규모·배치 설계 페이지 3·10절 검증된 [사실] 재인용, 세 출처 모두 원문 미열람. 세 출처는 각각 다른 내용이며 교차 확인 아님. |
| f15 | 예 | 아니오 | 아니오 | 강등 | ref-105 원문 텍스트로 recharge_threshold 0.10('below which robots in this fleet will not operate') 확인. 그러나 '충전 설비 계획의 결과가 배정 가능한 로봇 수를 좌우하는 운영 설정으로 이어진다'는 원문에 없고 35 페이지에서도 [추정]이었다. 설정값 문장은 [사실], 결론 부분은 [추정]으로 분리. |
| f16 | 예 | 예 | 아니오 | 유지 | G. 계획·최적화 대분류 페이지 검증된 [사실] 재인용, 원문 미열람. 저자 계산 실험 조건·독립 재현 미확인 단서 유지. |
| f17 | 예 | 예 | 아니오 | 유지 | 34. 시뮬레이션·예측용 디지털 트윈 페이지와 G 대분류 페이지 검증된 [사실] 재인용, 두 출처 원문 미열람. 시뮬레이션 결과이며 현장 실측 아님 단서 유지. |
| f18 | 예 | 아니오 | 아니오 | 강등 | ref-267 원문 미열람. 연구의 존재는 34 페이지에서 [사실]이나, '경로망 배치 평가가 가정한 미래를 실험하는 쪽에 걸친다'는 G 대분류 페이지에서 [추정]으로 실린 해석이다. 연구 존재는 [사실], 위치 판단은 [추정]으로 분리. |
| f19 | 예 | 아니오 | 아니오 | 강등 | 검증 중 movingai.com MAPF 벤치마크 페이지 열람: 지도와 지도별 시나리오 파일(even·random 각 25개) 제공은 확인. '같은 조건에서 비교하게 한다'는 페이지에 명시되지 않은 해석이고 시나리오 형식과의 연결도 해석이므로, 제공 사실만 [사실], 나머지는 [추정]. |
| f20 | 예 | 예 | 아니오 | 유지 | 36 페이지 5절 검증된 [사실] 재인용(이번 실행 원문 미열람). ref-943 은 참고문헌의 ref-060(doi 링크)과 같은 논문이다. 승강기 제어는 연계 대상 문구 유지. |
| f21 | 예 | 예 | 아니오 | 유지 | 35 페이지 9절 검증된 [사실] 재인용, 원문 미열람. 승강기 제어 연계 대상 문구 유지. |
| f22 | 예 | 예 | 아니오 | 유지 | [의견] 유지, 의견 주체(Lee 외 저자들) 명시됨. 36 페이지 5절 재인용, 원문 미열람. |
| f23 | 예 | 예 | 아니오 | 유지 | ref-528 원문 텍스트 대조 확인: 컨베이어·전압 시험기 고장(START_TIME·DURATION), 진공 그리퍼(GRASP_OCCURRENCE), 긴급 주문(START_TIME·ID). 발행일 미확인. |
| f24 | 예 | 예 | 아니오 | 유지 | [추정] 유지. ref-116·ref-1090 원문 미열람(33 페이지 재인용). ref-1090 은 벤더 문서 유형이나 이 주장은 기능·성능 주장이 아님. |
| f25 | 예 | 예 | 아니오 | 유지 | ref-406 원문 대조 확인(.building.yaml → 층별 바닥·벽 메시, 문·승강기 sdf, 로봇 블록, 주석 수정 후 재생성, 기본 월드에 플러그인 없음·템플릿 월드). ref-079 원문 텍스트로 충전기·문·승강기 주석 확인. 두 출처 같은 기관이라 교차 확인 아님. |
| f26 | 예 | 예 | 아니오 | 유지 | [추정] 유지. ref-1092 원문 미열람(33 페이지 9절 재인용). 등록 정보–시뮬레이션 모델 연결 사례 미확인 단서 유지. |
| f27 | 예 | 예 | 아니오 | 유지 | rosbag2 README(rolling) 열람 확인: 기록·재생 도구, 기본 저장 형식 mcap, ~/set_rate·--clock·~/play 시작 오프셋, --topics, -i 여러 백 파일 기록 시각순 재생, 크기·기간 분할, zstd, 스냅숏 모드. 재생 속도·시작 시각은 CLI 플래그가 아니라 서비스·매개변수로 제공된다. |
| f28 | 예 | 예 | 아니오 | 유지 | [추정] 유지. 근거 출처 열람 확인, oq-131 연결 유지. |
| f29 | 예 | 예 | 아니오 | 유지 | arXiv 2310.08710 초록 열람 확인: 실제 주행 기록으로 초기화·재생, 학습·규칙 기반 행동 모델, TPU/GPU 그래프 안 시뮬레이션. 자율주행 대상이며 로봇 현장 사례 아님 단서 유지. |
| f30 | 예 | 예 | 아니오 | 유지 | ref-406 원문 대조 확인: crowdsim 은 선택 기능, menge 기반, rmf_traffic_editor 에서 켬, airport_terminal use_crowdsim:=1. ref-104 는 같은 기관(독립 교차 확인 아님)이며 원문 미열람. 공항은 33 페이지와 같이 상업 시설로 둔다. |
| f31 | 예 | 예 | 아니오 | 유지 | arXiv 1912.06321 초록 열람 확인: SRCC 제안, LoCoBot, 모델 9개 병행 시험, 성공률 SRCC 0.18 → 0.844, 벽 미끄러짐. 다만 0.18 은 'CVPR 2019 챌린지에서 쓰인 Habitat 설정'의 값이므로 '기본 설정'은 그 표현으로 고친다. RA-L 2020. |
| f32 | 예 | 예 | 아니오 | 유지 | [추정] 유지. ref-741 원문 미열람(36 페이지 9절 재인용), ref-1127 열람 확인. 현실 격차 보정은 연계 대상 문구 유지. |
| f33 | 예 | 예 | 아니오 | 유지 | 36 페이지 7절 검증된 [사실] 재인용, 이번 실행 원문 미열람. 발행일 2024-03-05. |
| f34 | 예 | 예 | 아니오 | 유지 | [추정] 유지. oq-156 연결, 대응 체계 자료 미확인 단서 유지. |
| f35 | 예 | 예 | 아니오 | 유지 | arXiv 2011.10294 초록 열람 확인: 사람 모델+최적화로 고위험 사람 행동 생성, 초기 설계 단계, 무작위·몬테카를로 탐색 비실용, 산업용 로봇 셀 개념 증명. 게재처 2020 IEEE SPCE. |
| f36 | 예 | 예 | 아니오 | 유지 | [추정] 유지. ref-1086 원문 미열람(33 페이지 재인용). 안전 인증·설비 안전 제어는 연계 대상 문구 유지. |
| f37 | 예 | 예 | 아니오 | 유지 | arXiv 2211.09507 초록 열람 확인: ROS 구동 시스템, 디지털 트윈에 대한 person-in-the-middle 공격이 물리 시스템 붕괴로 이어질 수 있음, 산업용 로봇·자율이동로봇 모두 해당, 완화 방안 논의. '중간자 공격' 표기 허용. |
| f38 | 예 | 예 | 아니오 | 유지 | [추정] 유지. 로봇 플릿 플랫폼 사례 없음 단서 유지. |
| f39 | 예 | 예 | 아니오 | 유지 | 브리프에서는 원문 미열람이었으나 검증 중 classic.gazebosim.org 튜토리얼을 열어 확인: database.config 의 license 요소, CC BY 3.0 Unported 권장(요구 아님), model.config 의 author·name·email 필수. 발행일 미확인. |
| f40 | 예 | 예 | 아니오 | 유지 | 34 페이지 7·11절 검증된 주장 재인용, 두 출처 원문 미열람. 두 출처는 서로 다른 부(제1부·제6부)를 가리키며 교차 확인 아님. |
| f41 | 예 | 예 | 아니오 | 유지 | [추정]·'연계 대상:' 표시 유지. ref-521 원문 미열람(34 페이지 재인용). 수요예측은 원문 19장 상위 업무 시스템 경계의 외부 영역. |
| f42 | 예 | 예 | 아니오 | 유지 | F. 연동 대분류 페이지 검증된 [사실] 재인용, 원문 미열람. 대상이 공동주택이며 물류센터가 아님을 유지. |
| f43 | 예 | 예 | 아니오 | 유지 | [추정] 유지. 두 출처 원문 미열람. oq-011 연결 유지. |
| f44 | 예 | 예 | 아니오 | 유지 | [추정]·vendor_claim true 확인. 36 페이지 5절 재인용, 원문 미열람. 페이지에 '벤더 주장' 병기 필수. 컨베이어·피킹 모듈 제어 에뮬레이션은 설비 업체·통합자 쪽 연계 대상. |
| f45 | 예 | 예 | 아니오 | 유지 | 36 페이지 5절 검증된 [사실] 재인용, 원문 미열람. PLC 코드 가상 시운전은 연계 대상 문구 유지. |
| f46 | 예 | 예 | 아니오 | 유지 | 33 페이지 5절 검증된 [사실] 재인용, ref-104 원문 미열람. 시뮬레이션 예제 월드이며 실제 시설 사례 아님 단서 유지. |
| f47 | 예 | 예 | 아니오 | 유지 | 33 페이지 5절 검증된 [사실] 재인용, 원문 미열람. 벤치마크이며 실제 가정 배치 아님. |
| f48 | 예 | 예 | 아니오 | 유지 | [추정]·vendor_claim true 확인. 검증 중 NVIDIA 블로그를 열어 확인: 발행일 2025-01-06, 'developing, testing and optimizing ... robot fleets at scale in a digital twin before deployment', 센서 시뮬레이션·합성 데이터. 브리프의 발행일 null·as_of 2026-10-09 는 2025-01-06 으로 고쳐야 함. |
| f49 | 예 | 예 | 아니오 | 유지 | [추정]·vendor_claim true 확인. 34 페이지 5절의 [추정] 벤더 주장 재인용, 원문 미열람. 이후 적용 결과 미확인 단서 유지(oq-084, oq-117). |

## 항목별 결과

| 항목 | 결과 | 내용 |
|---|---|---|
| 분류 적합성 | 예 | — |
| 범위 경계 | 예 | — |
| 중복·모순 | 아니오 | ref-1329(Chat2Scenic, arXiv 2607.14387)은 C. 채팅 기반 구성·운영 대분류 자료 목록의 ref-833 과 저자·제목·발행일(2026-07-15)이 같은 논문이다 — 새 id 대신 ref-833 재사용, ref-1330(Xia 외, LLM Agents Perform Controlled Experiments Using Simulation Models)은 ref-832 와 저자·제목·발행일(2026-08-22)이 같은 논문이다 — ref-832 재사용, ref-943(PMC 링크)과 ref-060(doi 링크)은 같은 Lee 외 Digital Health 논문이다. 35. 처리능력·규모·배치 설계 페이지는 ref-060, 36. 가상 시운전·실제 상황 재현 페이지는 ref-943 을 쓴다 — 이번 절에서는 ref-943 하나로만 인용, f7(18. 실시간 세계 상태·데이터 일관성 ↔ 34. 시뮬레이션·예측용 디지털 트윈 구분)은 B. 로봇 온톨로지 대분류 페이지와 E. 사물·사람·실시간 상태 연결 브리프(2026-10-09-03 f30)의 같은 주장과 겹친다 — 같은 각주 ref-291 재사용, 모순 없음, f15·f17·f18·f14·f16 은 A. 기획·사업·G. 계획·최적화 대분류 페이지의 옛 분류 기준 연결과 겹친다 — 같은 각주 재사용, 태그는 그 페이지의 사실·추정 구분을 따른다 |
| 용어 일관성 | 예 | — |
| 인용 길이·저작권 | 예 | — |
| 정정 요청 반영 | — | — |

## 수정 지시(required_fixes)

- f1·f2·ref-1329: 각주를 새 id ref-1329 가 아니라 기존 ref-833 으로 쓰고 reference_updates 에 ref-1329 를 넣지 않는다 — C. 채팅 기반 구성·운영 대분류 자료 목록의 ref-833 이 저자·제목·발행일이 같은 Chat2Scenic 논문이다.
- f3·f4·ref-1330: 각주를 기존 ref-832 로 쓰고 ref-1330 을 등록하지 않는다 — 같은 Xia 외 논문이 ref-832 로 이미 있다.
- f15: 'Open-RMF 플릿 어댑터 템플릿 설정에서 배터리가 recharge_threshold(예시값 0.10) 아래인 로봇은 작동하지 않는다'만 [사실][^ref-105]로 쓰고, '충전 설비 계획의 결과가 배정 가능한 로봇 수를 좌우하는 운영 설정으로 이어진다'는 별도 문장 [추정]으로 강등한다 — 결론 부분은 원문에 없고 35. 처리능력·규모·배치 설계 페이지에서도 [추정]이었다.
- f18: '다중 AGV 시스템의 경로망을 시뮬레이션으로 자동 설계하는 연구(IEEE TASE, 2024)가 있다'만 [사실][^ref-267], '경로망 배치 평가가 가정한 미래를 실험하는 쪽에 걸친다'는 [추정]으로 나눈다 — G. 계획·최적화 대분류 페이지가 이 해석을 [추정]으로 실었다.
- f19: 'Moving AI Lab 의 MAPF 벤치마크는 지도마다 시나리오 파일을 묶어 공개한다'만 [사실][^ref-1091], '같은 조건 비교와 시나리오 형식·라이브러리와 맞닿는다'는 [추정]으로 강등한다 — 벤치마크 페이지는 비교 목적을 명시하지 않는다(검증 중 열람 확인).
- f2: 본문에서 Chat2Scenic 수치를 '실행 불가'가 아니라 '컴파일 실패'로 쓴다 — 원문 지표는 컴파일 성공률(CSR)이다.
- f31: 'Habitat 기본 설정의 성공률 SRCC 0.18'을 'CVPR 2019 챌린지에서 쓰인 Habitat 설정의 성공률 SRCC 0.18'로 고친다 — 초록의 표현이 그렇다.
- f44·f48·f49: 본문에 [추정]과 '벤더 주장'을 병기한다. f48 의 ref-527 각주 발행일을 '미확인'에서 2025-01-06 으로 고친다 — 검증 중 NVIDIA 블로그 원문에서 확인했다.
- 각주 원문 미열람 표기: 브리프에서 원문을 열지 않은 출처(ref-104, ref-101, ref-398, ref-267, ref-098, ref-109, ref-102, ref-381, ref-943, ref-103, ref-1088, ref-1089, ref-116, ref-1090, ref-1091, ref-1092, ref-1086, ref-971, ref-291, ref-521, ref-516, ref-518, ref-1126, ref-1130, ref-1131, ref-1133, ref-741, ref-1239, ref-409, ref-106, ref-1165, ref-527, ref-526)의 각주 정의에는 접근일 뒤 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣는다. ref-079·ref-105·ref-528 은 data/source_texts 원문이 입력에 있으므로 원문 미열람 표기를 하지 않는다.
- 범위 경계 문구: f8·f20·f21·f42 의 승강기·문 제어, f11·f44·f45 의 PLC·컨베이어 제어 코드 가상 시운전, f9·f32·f48 의 로봇 자체 주행·센서 시뮬레이션·현실 격차 보정, f35·f36 의 안전 인증·설비 안전 제어는 각 문장에서 '연계 대상'으로 짧게 밝힌다. f41 은 '연계 대상:'으로 시작하는 문장 그대로 둔다 — 분류 원문 19장 경계.
- 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈: f7 로 '18은 현재 상태 표현, 34는 가정한 미래 실험'을 E. 사물·사람·실시간 상태 연결 항목에 밝히고, f37·f38 의 디지털 트윈 동기화는 36. 가상 시운전·실제 상황 재현이 두 영역을 잇는 경로로만 서술한다. 34가 현재 상태를 표현한다고 쓰지 않는다.
- f14: 세 출처(ref-102·ref-098·ref-109)는 각각 다른 내용이므로 문장을 나눠 각자의 각주를 붙이고 교차 확인된 것처럼 묶어 쓰지 않는다.
- f20·f22: Lee 외 병원 논문은 ref-943 하나로만 인용하고 ref-060 을 같은 문장에 함께 붙이지 않는다 — 두 id 가 같은 논문이다.
- '아직 다루지 않은 연결' 목록을 브리프 finding 이 실제로 다루지 않은 세부영역과 맞춘다: 브리프 rationale 의 29·30·31·40·41·43·53·58·60 에 더해 5. 로봇 능력·작업 표현, 6. 온톨로지 기반 시스템·로봇 연동, 8. 채팅으로 맵 작성, 10. 채팅으로 로봇 구성, 12. 채팅으로 업무 지시·오케스트레이션, 17. 작업 대상·자산 식별과 인계 추적, 45. 문서·도면·장면 이해, 46. 예측·학습 기반 최적화, 50. 안전 표준·인증·사고 조사, 56. 운영 이관·확대·교육, 57. 자산·소프트웨어 수명주기 관리, 66. 실외, 67. 기타 현장을 적는다. '모든 대분류와 연결' 같은 완전성 표현은 쓰지 않는다.
- 다른 대분류와 세부영역은 새 17개 대분류 기준의 문자+이름, 번호+이름으로 쓴다(예: 'F. 연동', '25. 작업 배정 — MRTA'). A·B·F·G 대분류 페이지의 옛 대분류 이름(예: 'C. 연결·실행 기반', 'F. 도입·검증·유지관리')을 옮겨 쓰지 않는다 — 그 페이지들의 연결 절은 이전 분류 기준이다.
- L. AI·학습 기술 관련 연결(f5·f6·f32)은 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영 링크와 적용 대상인 33. 시나리오 모델·편집·36. 가상 시운전·실제 상황 재현 링크를 함께 둔다 — 공통 규칙 5(교차 규칙).

## 검증 노트

판정: 조건부 승인. 확인 46건, 미확인 3건(f15·f18·f19는 사실 부분과 해석 부분이 섞여 해석을 분리), 교차 확인 0건. 강등: f15·f18·f19 사실 → 사실+추정 분리(결론·위치 판단 부분 추정). 원문 미열람 출처: ref-104, ref-101, ref-398, ref-267, ref-098, ref-109, ref-102, ref-381, ref-943, ref-103, ref-1088, ref-1089, ref-116, ref-1090, ref-1091, ref-1092, ref-1086, ref-971, ref-291, ref-521, ref-516, ref-518, ref-1126, ref-1130, ref-1131, ref-1133, ref-741, ref-1239, ref-409, ref-106, ref-1165, ref-527, ref-526(이 가운데 ref-1091·ref-1239·ref-527은 검증 중 원문을 열어 해당 진술을 확인했다). 주의: 이 절의 연결은 대부분 단일 출처 또는 게시된 세부영역 페이지의 재인용에 기대고, 연결 해석 13건은 [추정]이다. 다중 로봇 플릿 오케스트레이션에 직접 적용된 근거는 Open-RMF 시뮬레이션 문서와 VirTooS 정도이고, 대화형 시나리오 생성(Chat2Scenic: 자율주행)·언어 모델 비교 실험(제약 공정)·시뮬레이션 예측력(LoCoBot 주행)·디지털 트윈 공격(ROS 로봇) 근거는 로봇 플릿이 아닌 대상에서 나왔다. 벤더 주장 3건(f44·f48·f49)은 독립 확인되지 않았다. 신규 출처 ref-1329·ref-1330은 기존 ref-833·ref-832와 같은 논문이라 재사용을 지시했고, ref-943과 ref-060이 같은 논문으로 참고문헌에 이중 등록돼 있다. 브리프의 ref-079·ref-105·ref-528은 fetched true인데 요약이 '원문 미열람'이고 fetch_url이 비어 있어 표시가 어긋난다(입력의 data/source_texts 원문으로 열람을 확인했다). 정정 요청 없음. 검증 검색 0회, 열람 12회.
```

### data/source_texts/ref-004.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
# RMF Core Overview

This chapter describes RMF, an umbrella term for a wide range of open specifications and software
tools that aim to ease the integration and interoperability of robotic systems,
building infrastructure, and user interfaces. `rmf_core` consists of:
 - [rmf_traffic](https://github.com/open-rmf/rmf_traffic): Core scheduling and traffic management systems
 - [rmf_traffic_ros2](https://github.com/open-rmf/rmf_ros2/tree/main/rmf_traffic_ros2): rmf_traffic for ros2
 - [rmf_task](https://github.com/open-rmf/rmf_task): Task planner for rmf
 - [rmf_battery](https://github.com/open-rmf/rmf_battery): rmf battery estimation
 - [rmf_ros2](https://github.com/open-rmf/rmf_ros2): ros2 adapters and nodes and python bindings for rmf_core
 - [rmf_utils](https://github.com/open-rmf/rmf_utils): utility for rmf

## Traffic deconfliction

Avoiding mobile robot traffic conflicts is a key functionality of `rmf_core`.
There are two levels to traffic deconfliction: (1) prevention, and (2)
resolution.

### Prevention

Preventing traffic conflicts whenever possible is the best-case scenario.
To facilitate traffic conflict prevention, we have implemented a
platform-agnostic Traffic Schedule Database. The traffic schedule is a living
database whose contents will change over time to reflect delays, cancellations,
or route changes. All fleet managers that are integrated into an RMF deployment must
report the expected itineraries of their vehicles to the traffic schedule. With
the information available on the schedule, compliant fleet managers can plan
routes for their vehicles that avoid conflicts with any other vehicles, no
matter which fleet they belong to. `rmf_traffic` provides a
[`Planner`](https://github.com/open-rmf/rmf_traffic/blob/main/rmf_traffic/include/rmf_traffic/agv/Planner.hpp)
class to help facilitate this for vehicles that behave like standard AGVs (Automated Guided Vehicles),
rigidly following routes along a pre-determined grid. In the future
we intend to provide a similar utility for AMRs (Autonomous Mobile Robots) that can perform ad hoc motion
planning around unanticipated obstacles.

### Negotiation

It is not always possible to perfectly prevent traffic conflicts.
Mobile robots may experience delays because of unanticipated obstacles in their
environment, or the predicted schedule may be flawed for any number of reasons.
In cases where a conflict does arise, `rmf_traffic` has a Negotiation scheme.
When the Traffic Schedule Database detects an upcoming conflict between two or
more schedule participants, it will send a conflict notice out to the relevant
fleet managers, and a negotiation between the fleet managers will begin. Each
fleet manager will submit its preferred itineraries, and each will respond with
itineraries that can accommodate the others. A third-party judge (deployed by
the system integrator) will choose the set of proposals that is considered
preferable and notify the fleet managers about which itineraries they should
follow.

There may be situations where a sudden, urgent task needs to take place
(for example, a response to an emergency), and the current traffic schedule does not
accommodate it in a timely manner. In such a situation, a traffic participant
may intentionally post a traffic conflict onto the schedule and force a
negotiation to take place. The negotiation can be forced to choose an itinerary
arrangement that favors the emergency task by implementing the third-party
judge to always favor the high-priority participant.

## Traffic Schedule

The traffic schedule is a centralized database of all the intended robot traffic
trajectories in a facility. Note that it contains the intended trajectories; it is
looking into the future. The job of the schedule is to identify conflicts in
the intentions of the different robot fleets and notify the fleets when a
conflict is identified. Upon receiving the notification, the fleets will begin
a traffic negotiation, as described above.

![Schedule and Fleet Adapters](images/rmf_core/schedule_and_fleet_adapters.png)

## Fleet Adapters

Each robot fleet that participates in an RMF deployment is expected to have a
fleet adapter that connects its fleet-specific API to the interfaces
of the core RMF traffic scheduling and negotiation system. The fleet adapter is
also responsible for handling communication between the fleet and the various
standardized smart infrastructure interfaces, e.g. to open doors, summon lifts,
and wake up dispensers.

Different robot fleets have different features and capabilities, dependent on
how they were designed and developed. The traffic scheduling and negotiation system
does not postulate assumptions about what the capabilities of the fleets will be.
However, to minimize the duplication of integration effort, we have identified 4
different broad categories of control that we expect to encounter among various
real-world fleet managers.

**Fleet adapter type** | **Robot/Fleetmanager API feature set**  | **Remarks**
--- | --- | ---
`Full Control` | <ul><li>Read the current location of the robot [x, y, yaw]</li><li>Request robot to move to [x, y, yaw] coordinate</li><li>Pause a robot while it is navigating to [x, y, yaw]</li><li>Resume a paused robot</li><li>Get route/path taken by robot to destination</li><li>ETA to destination</li><li>Read battery status of the robot</li><li>Infer when robot is done navigating to [x, y, yaw]</li><li>Send robot to docking/charging station</li><li>Switch on board map and re-localize robot.</li><li>Start a process (such as clean Zone_A)</li><li>Pause/resume/stop process</li><li>Infer when process is complete (specific to use case)</li></ul> | RMF is provided with live status updates and full control over the paths that each individual mobile robot uses when navigating through the environment. This control level provides the highest overall efficiency and compliance with RMF, which allows RMF to minimize stoppages and deal with unexpected scenarios gracefully. *(API available)*
`Traffic Light` | <ul><li>Read the current location of the robot [x, y, yaw]</li><li>Pause a robot while it is navigating to [x, y, yaw]</li><li>Resume a paused robot</li><li>Read battery status of the robot</li><li>Send robot to docking/charging station</li><li>Start a process (such as clean Zone_A)</li><li>Pause/resume/stop process</li><li>Infer when process is complete (specific to use case)</li></ul> | RMF is given the status as well as pause/resume control over each mobile robot, which is useful for deconflicting traffic schedules especially when sharing resources like corridors, lifts and doors. *(API available)
`Read Only` | <ul><li>Read the current location of the robot [x, y, yaw]</li><li>Read or infer the path that the robot will take to its current destination</li><li>Read average speed of the robot or ETA to destination</li><li>Read battery status of the robot</li><li>Infer when process is complete (specific to use case)</li></ul> | RMF is not given any control over the mobile robots but is provided with regular status updates. This will allow other mobile robot fleets with higher control levels to avoid conflicts with this fleet. _Note that any shared space is allowed to have a maximum of just one "Read Only" fleet in operation. Having none is ideal._ *(Preliminary API available)*
`No Interface` | | Without any interface to the fleet, other fleets cannot coordinate with it through RMF, and will likely result in deadlocks when sharing the same navigable environment or resource. This level will not function with an RMF-enabled environment. *(Not compatible)*

In short, the more collaborative a fleet is with RMF, the more harmoniously all of the fleets and systems are able to operate together.
Note again that there can only ever be one "Read Only" fleet in a shared space, as any two or more of such fleets will make avoiding deadlock or resource conflict nearly impossible.

Currently we provide a reusable C++ API (as well as Python bindings) for integrating the **Full Control** category of fleet management.
A preliminary ROS 2 message API is available for the **Read Only** category, but that API will be deprecated in favor of a C++ API
(with [Python bindings](https://github.com/open-rmf/rmf_ros2/tree/main/rmf_fleet_adapter_python/) available) in a future release.
The **Traffic Light** control category is compatible with the core RMF scheduling system, but we have not yet implemented a reusable API for it.
To implement a **Traffic Light** fleet adapter, a system integrator would have to use the core traffic schedule and negotiation APIs directly, as well as implement the integration with the various infrastructure APIs (e.g. doors, lifts, and dispensers).

The API for the **Full Control** category is described in the [Mobile Robot Fleets](./integration_fleets.md) section of the Integration chapter, and the **Read Only** category is described in the [Read Only Fleets](./integration_read-only.md) section of the Integration chapter.
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
…(발췌: 전체 12,743자 중 앞 10,953자)
````

### data/source_texts/ref-031.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
![logo](./assets/logo.png)

# Interface for the Communication between Mobile Robots and a Fleet Control

## VDA 5050

## Version 3.0.0

![Fleet control system and mobile robots](./assets/csagv.png)

# Disclaimer
The following explanations are intended to provide guidance for implementing an interface that enables communication between mobile robots and a fleet management system. They are intended to be freely accessible to all users and are non-binding. Any party choosing to apply these guidelines is responsible for ensuring their correct and appropriate use in each specific case.
Users must consider the applicable state of the art at the time the guidelines are applied. The use of these proposals does not relieve any party of responsibility for its own actions. These statements do not claim to be exhaustive, nor do they constitute an authoritative interpretation of existing laws. They do not replace the need to review and comply with relevant policies, legislation, or regulations.
In addition, the specific characteristics of the respective products and their various potential applications must be considered. All users act at their own risk. Any liability on the part of the VDA and VDMA or any individuals involved in the development or application of these proposals is excluded.
If you identify any inaccuracies in the application of these proposals or potential risks of misinterpretation, please notify the VDA immediately so that any necessary corrections can be made.

**Publisher**
Verband der Automobilindustrie e. V. (VDA)
Behrenstraße 35, 10117 Berlin,
Germany
www.vda.de

**Copyright**
Association of the Automotive Industry (VDA)
Reproduction and any other form of reproduction is only permitted with specification of the source.

Version 3.0.0

## Table of contents
[0 Foreword](#0-foreword)<br>
[1 Introduction](#1-introduction)<br>
[2 Scope](#2-scope)<br>
[3 Definitions](#3-definitions)<br>
  [3.1 Mobile Robot](#31-mobile-robot)<br>
  [3.2 Moving](#32-moving)<br>
  [3.3 Driving](#33-driving)<br>
  [3.4 Automatic driving](#34-automatic-driving)<br>
  [3.5 Manual driving](#35-manual-driving)<br>
  [3.6 Line-guided mobile robot](#36-line-guided-mobile-robot)<br>
  [3.7 Freely navigating mobile robot](#37-freely-navigating-mobile-robot)<br>
[4 Transport protocol](#4-transport-protocol)<br>
  [4.1 Connection handling, security and QoS](#41-connection-handling-security-and-qos)<br>
  [4.2 Topic levels](#42-topic-levels)<br>
  [4.3 Topics for communication](#43-topics-for-communication)<br>
[5 Process and content of communication](#5-process-and-content-of-communication)<br>
  [5.1 General](#51-general)<br>
  [5.2 Implementation Phase](#52-implementation-phase)<br>
  [5.3 Functions of the fleet control](#53-functions-of-the-fleet-control)<br>
  [5.4 Functions of the mobile robots](#54-functions-of-the-mobile-robots)<br>
[6 Protocol specification](#6-protocol-specification)<br>
  [6.1 Order](#61-order)<br>
    [6.1.1 Concept and logic](#611-concept-and-logic)<br>
    [6.1.2 Orders and order updates](#612-orders-and-order-update)<br>
    [6.1.3 Order cancellation](#613-order-cancellation)<br>
    [6.1.4 Order rejection](#614-order-rejection)<br>
    [6.1.5 Corridors](#615-corridors)<br>
  [6.2 Actions](#62-actions)<br>
    [6.2.1 Instant actions](#621-instant-actions)<br>
    [6.2.2 Action blocking types and sequence](#622-action-blocking-types-and-sequence)<br>
    [6.2.3 Predefined actions](#623-predefined-actions)<br>
  [6.3 Maps](#63-maps)<br>
    [6.3.1 Map distribution](#631-map-distribution)<br>
    [6.3.2 Maps in mobile robot state](#632-maps-in-the-mobile-robot-state)<br>
    [6.3.3 Map download](#633-map-download)<br>
    [6.3.4 Enable downloaded maps](#634-enable-downloaded-maps)<br>
    [6.3.5 Delete maps on the mobile robot](#635-delete-maps-on-the-mobile-robot)<br>
  [6.4 Zones](#64-zones)<br>
    [6.4.1 Zone types](#641-zone-types)<br>
    [6.4.2 Zone set transfer](#642-zone-set-transfer)<br>
    [6.4.3 Communication for interactive zones](#643-communication-for-interactive-zones)<br>
    [6.4.4 Interaction between zones](#644-interactions-between-zones)<br>
    [6.4.5 Error handling within zones](#645-error-handling-within-zones)<br>
  [6.5 Connection](#65-connection)<br>
  [6.6 State](#66-state)<br>
    [6.6.1 Concept and logic](#661-concept-and-logic)<br>
    [6.6.2 Traversal of nodes and edges](#662-traversal-of-nodes-and-edges)<br>
    [6.6.3 Base request](#663-base-request)<br>
    [6.6.4 Information](#664-information)<br>
    [6.6.5 Errors](#665-errors)<br>
    [6.6.6 Operating Mode](#666-operating-mode)<br>
    [6.6.7 Clearing the order on the mobile robot](#667-clearing-the-order-on-the-mobile-robot)<br>
    [6.6.8 Idle state of the mobile robot](#668-idle-state-of-the-mobile-robot)<br>
    [6.6.9 Action states](#669-action-states)<br>
    [6.6.10 Request use of Corridors](#6610-request-use-of-corridors)<br>
  [6.7 Visualization](#67-visualization)<br>
  [6.8 Sharing of planned paths for freely navigating mobile robots](#68-sharing-of-planned-paths-for-freely-navigating-mobile-robots)<br>
  [6.9 Request/response mechanism](#69-requestresponse-mechanism)<br>
  [6.10 Factsheet](#610-factsheet)<br>
[7 Message specification](#7-message-specification)<br>
  [7.1 Symbols of the tables and meaning of formatting](#71-symbols-of-the-tables-and-meaning-of-formatting)<br>
    [7.1.1 Optional fields](#711-optional-fields)<br>
    [7.1.2 Permitted characters and field lengths](#712-permitted-characters-and-field-lengths)<br>
    [7.1.3 Notation of fields, topics and enumerations](#713-notation-of-fields-topics-and-enumerations)<br>
    [7.1.4 JSON data types](#714-json-data-types)<br>
  [7.2 Protocol header](#72-protocol-header)<br>
  [7.3 Implementation of the order message](#73-implementation-of-the-order-message)<br>
    [7.3.1 Format of action parameters](#731-format-of-action-parameters)<br>
  [7.4 Implementation of the instantAction message](#74-implementation-of-the-instantaction-message)<br>
  [7.5 Implementation of the response message](#75-implementation-of-the-response-message)<br>
  [7.6 Implementation of the zoneSet message](#76-implementation-of-the-zoneset-message)<br>
  [7.7 Implementation of the connection message](#77-implementation-of-the-connection-message)<br>
  [7.8 Implementation of the state message](#78-implementation-of-the-state-message)<br>
  [7.9 Implementation of the visualization message](#79-implementation-of-the-visualization-message)<br>
  [7.10 Implementation of the factsheet message](#710-implementation-of-the-factsheet-message)<br>

# 0 Foreword

The specification for this interface has been jointly developed by the Verband der Automobilindustrie e. V. (VDA) and the VDMA e. V. (Mechanical Engineering Industry Association).
The VDA represents the German automotive sector, including OEMs and Tier‑1/Tier‑n suppliers, and contributes its expertise in vehicle architectures, system integration, and safety‑critical communication.
The VDMA represents companies across the European mechanical and plant engineering industry and brings extensive knowledge in automation technology, machinery interoperability, and production system standardization.
Both organizations collaborate to ensure that the interface specification reflects current engineering requirements, supports robust and scalable system integration, and enables consistent data exchange across heterogeneous environments. Their joint development process emphasizes harmonized communication models, compatibility with established industrial standards, and long‑term maintainability of cross‑domain interfaces. This cooperation ensures that the resulting specification can be reliably implemented in automotive, machinery, and mixed‑industry applications, supporting high interoperability, operational safety, and future-proof system architectures.
The Institute for Material Handling and Logistics (IFL) at Karlsruhe Institute of Technology (KIT) is part of the department of mechanical engineering and focuses on combining research, teaching, and industrial application. Its interdisciplinary team works on future logistics challenges, including material flow analysis, automation, robotics, digitalization, AI, sustainability, and system design.
The Institute has been commissioned by the VDA and the VDMA to oversee the development of the VDA 5050. It contributes to this process by taking the lead in development, supporting issue review, and managing the official GitHub repository.

# 1 Introduction
This recommendation describes the communication interface for exchanging information between central fleet control and mobile robots.
The objective of this recommendation is to support the integration and efficient operation of mobile robot fleets under the supervision of a centralized fleet control system. This is achieved through the implementation of a standardized, vendor neutral communication interface that ensures interoperability between the fleet control system and individual mobile robots.
Various national technical guidelines and legal frameworks may offer general orientation in this context. They could provide indicative information on aspects such as planning, operation, safety, or coordination of automated systems. In addition, national standards and regulatory provisions may help ensure that technical processes and terminology are considered within a consistent overall framework.
The recommendation uses a semantic versioning schema. Major version changes (x.0.0) typically involve breaking changes, such as the introduction of new non optional fields. Minor version changes (3.x.0) generally introduce new features, for example the addition of an optional parameter for visualization. Patch version changes (3.0.x) usually address smaller corrections, such as fixing typographical errors in the documentation.
Stakeholders are invited to submit proposals for modifications or enhancements to the interface. Such proposals shall be submitted via the GitHub repository at: <https://github.com/vda5050/vda5050>.

# 2 Scope

This document describes a standardized and vendor-neutral communication interface between a fleet control system and mobile robots. Its purpose is to provide a common reference that supports interoperability in environments where multiple mobile robots operate under the coordination of a fleet control system. The use of this specification is optional and non-binding, and its application is at the discretion of the respective stakeholders.

The objectives of this specification are:

- to reduce complexity when connecting mobile robots to a fleet control system.
- to enable the coordinated operation of heterogeneous mobile robot fleets from different manufacturers within a shared physical environment.
- to provide a generic and domain independent set of interface definitions applicable to mobile robots with varying navigation principles, physical dimensions, load handling or manipulation capabilities, and autonomy levels.

This specification does not address the following topics:
…(발췌: 전체 207,642자 중 앞 11,074자)
```

### data/source_texts/ref-045.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
@prefix epcis:  <https://ref.gs1.org/epcis/> .
@prefix cbv:    <https://ref.gs1.org/cbv/> .
@prefix gs1:    <https://gs1.org/voc/> .

@prefix dct:    <http://purl.org/dc/terms/> .
@prefix owl:    <http://www.w3.org/2002/07/owl#> .
@prefix rdf:    <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:   <http://www.w3.org/2000/01/rdf-schema#> .
@prefix schema: <http://schema.org/> .
@prefix skos:   <http://www.w3.org/2004/02/skos/core#> .
@prefix sw:     <http://www.w3.org/2003/06/sw-vocab-status/ns#> .
@prefix vann:   <http://purl.org/vocab/vann/> .
@prefix xsd:    <http://www.w3.org/2001/XMLSchema#> .

#################### Ontology

epcis: a owl:Ontology;
  rdfs:label "EPCIS Ontology";
  rdfs:comment """The Electronic Product Code Information System (EPCIS) is a specification for capturing and exchanging event visibility data across the global logistics chain.
Version 2.0 is a major release that adds JSON, JSONLD and RDF payload formats, sensor reports, and other major features.""";
  dct:creator <https://gs1.org/>;
  dct:publisher <https://gs1.org/>;
  dct:created  "2021-06-01"^^xsd:date;
  dct:modified "2021-09-30"^^xsd:date;
  # dct:issued   "2021-06-30"^^xsd:date; # after release
  rdfs:seeAlso cbv:, gs1: ;
  owl:versionInfo "2.0";
  vann:preferredNamespaceUri "https://ref.gs1.org/epcis/";
  vann:preferredNamespacePrefix "epcis".

<https://gs1.org/> a schema:Organization;
  schema:name "GS1";
  schema:description "GS1 is an international organization that sets the global standards in transport and logistics".

#################### Meta-properties

epcis:jsonldLabel a owl:DatatypeProperty , rdf:Property ;
      rdfs:comment      """JSONLD term (alias) used for this property.
The default is the property local name, which is captured in rdfs:label."""@en ;
      rdfs:domain       rdf:Property;
      schema:domainIncludes rdf:Property ;
      rdfs:isDefinedBy  epcis: ;
      rdfs:label        "jsonldLabel" ;
      rdfs:range        xsd:string ;
      schema:rangeIncludes xsd:string ;
      sw:term_status    "stable" .

rdf:type epcis:jsonldLabel "type".

epcis:jsonldUriLabel a owl:DatatypeProperty , rdf:Property ;
      rdfs:comment      """JSONLD term (alias) used for the URI of nodes of this class.
There is no default: many EPCIS classes use blank nodes instead of the standard @id JSONLD term."""@en ;
      rdfs:domain       rdfs:Class;
      schema:domainIncludes rdfs:Class ;
      rdfs:isDefinedBy  epcis: ;
      rdfs:label        "jsonldUriLabel" ;
      rdfs:range        xsd:string ;
      schema:rangeIncludes xsd:string ;
      sw:term_status    "stable" .

#################### Event classes

epcis:EPCISEvent  a       owl:Class , rdfs:Class ;
        rdfs:comment      "A logistics event. This is a common superclass (base type) for all EPCIS events. All of the more specific event types are subclasses of EPCISEvent."@en ;
        rdfs:isDefinedBy  epcis: ;
        rdfs:label        "EPCISEvent" ;
        sw:term_status    "stable" .

epcis:AggregationEvent   a owl:Class , rdfs:Class ;
        rdfs:comment      "The event type AggregationEvent describes events that apply to objects that have been aggregated to one another. In such an event, there is a set of 'contained' objects that have been aggregated within a 'containing' entity that's meant to identify the aggregation itself.  This event type is intended to be used for 'aggregations', meaning an association where there is a strong physical relationship between the containing and the contained objects such that they will all occupy the same location at the same time, until such time as they are disaggregated."@en ;
        rdfs:isDefinedBy  epcis: ;
        rdfs:label        "AggregationEvent" ;
        rdfs:subClassOf   epcis:EPCISEvent ;
        epcis:jsonldUriLabel "eventID";
        sw:term_status    "stable" .

epcis:AssociationEvent   a owl:Class , rdfs:Class ;
        rdfs:comment      "The event type AssociationEvent describes the association or disassociation of one or several physical objects with a parent object or a specific physical location.  Like the AggregationEvent, the AssociationEvent is also used to capture associations where there is a strong physical relationship between the containing and the contained objects such that they will all occupy the same location at the same time, until such time as they are disaggregated. However, the AggregationEvent does not allow for associations of objects with physical locations;  if action is DELETE while omitting the childEPC and childQuantityList field, all contained children are disaggregated from the containing parent. Because there are situations in which associations are more permanent, i.e. beyond the physical flow of goods (e.g. packing/unpacking and loading/unloading), an AssociationEvent SHOULD be used: (a) when objects need to be associated with a physical location or (b) when the parent object could also be subject to other, more temporary associations (i.e. captured using AggregationEvent)."@en ;
        rdfs:isDefinedBy  epcis: ;
        rdfs:label        "AssociationEvent" ;
        rdfs:subClassOf   epcis:EPCISEvent ;
        epcis:jsonldUriLabel "eventID";
        sw:term_status    "stable" .

epcis:ObjectEvent  a      owl:Class , rdfs:Class ;
        rdfs:comment      "An ObjectEvent captures information about an event pertaining to one or more physical or digital objects identified by instance-level (EPC) or class-level (EPC Class) identifiers. In most situations, an ObjectEvent is envisioned to represent an actual observations of objects, but strictly speaking it can be used for any event a Capturing Application wants to assert about objects, including for example capturing the fact that an expected observation failed to occur."@en ;
        rdfs:isDefinedBy  epcis: ;
        rdfs:label        "ObjectEvent" ;
        rdfs:subClassOf   epcis:EPCISEvent ;
        epcis:jsonldUriLabel "eventID";
        sw:term_status    "stable" .

epcis:TransactionEvent   a owl:Class , rdfs:Class ;
        rdfs:comment      "The event type TransactionEvent describes the association or disassociation of physical or digital objects to one or more business transactions. While other event types have an optional bizTransactionList field that may be used to provide context for an event, the TransactionEvent is used to declare in an unequivocal way that certain objects have been associated or disassociated with one or more business transactions as part of the event."@en ;
        rdfs:isDefinedBy  epcis: ;
        rdfs:label        "TransactionEvent" ;
        rdfs:subClassOf   epcis:EPCISEvent ;
        epcis:jsonldUriLabel "eventID";
        sw:term_status    "stable" .

epcis:Transformation a owl:Class , rdfs:Class ;
        rdfs:comment      """A transformation business processes that takes a longer period of time than a single TransformationEvent, so is associated with a series of such events.
When events share the same Transformation, the meaning is that the inputs to any of those events may have contributed in some way to each of the outputs in any of those same events."""@en ;
        rdfs:isDefinedBy  epcis: ;
        rdfs:label        "Transformation" ;
        sw:term_status    "stable" .

epcis:TransformationEvent        a owl:Class , rdfs:Class ;
        rdfs:comment      "A TransformationEvent captures information about an event in which one or more physical or digital objects identified by instance-level (EPC) or class-level (EPC Class) identifiers are fully or partially consumed as inputs and one or more objects identified by instance-level (EPC) or class-level (EPC Class) identifiers are produced as outputs. The TransformationEvent captures the relationship between the inputs and the outputs, such that any of the inputs may have contributed in some way to each of the outputs."@en ;
        rdfs:isDefinedBy  epcis: ;
        rdfs:label        "TransformationEvent" ;
        rdfs:subClassOf   epcis:EPCISEvent ;
        epcis:jsonldUriLabel "eventID";
        sw:term_status    "stable" .

#################### Other classes

epcis:BizTransaction  a   owl:Class , rdfs:Class ;
        rdfs:comment      "Document that describes a particular business transaction. An example is a specific Purchase Order or Despatch Advice. Business Transaction information may be included in EPCIS events to record an event's participation in particular business transactions."@en ;
        rdfs:isDefinedBy  epcis: ;
        rdfs:label        "BizTransaction" ;
        epcis:jsonldUriLabel "bizTransaction";
        sw:term_status    "stable" .

epcis:EPCISDocument a      owl:Class , rdfs:Class ;
        rdfs:comment      "An EPCISDocument is a means to transport a collection of EPCIS events, optionally accompanied by relevant master data, as a single electronic document.  It is used by the concrete bindings of the EPCIS Capture Interface.  In addition, trading partners may by mutual agreement use it as a single electronic document."@en ;
        rdfs:isDefinedBy  epcis: ;
        rdfs:label        "EPCISDocument" ;
        epcis:jsonldUriLabel "id";
        sw:term_status    "stable" .

epcis:EPCISDocumentBody a      owl:Class , rdfs:Class ;
        rdfs:comment      "Intermediate node that is connected to EPCISDocument using epcisBody, and includes a list of events using eventList"@en ;
        rdfs:isDefinedBy  epcis: ;
        rdfs:label        "EPCISDocumentBody" ;
        sw:term_status    "stable" .

epcis:EPCISDocumentHeader a      owl:Class , rdfs:Class ;
        rdfs:comment      "Intermediate node that is connected to EPCISDocument using epcisHeader, and may include master data using masterData"@en ;
        rdfs:isDefinedBy  epcis: ;
        rdfs:label        "EPCISDocumentHeader" ;
        sw:term_status    "stable" .
…(발췌: 전체 60,475자 중 앞 9,823자)
```

### data/source_texts/ref-051.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
{
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "title": "state",
    "description": "State of the mobile robot.",
    "subtopic": "/state",
    "type": "object",
    "required": [
        "headerId",
        "timestamp",
        "version",
        "manufacturer",
        "serialNumber",
        "orderId",
        "orderUpdateId",
        "lastNodeId",
        "lastNodeSequenceId",
        "nodeStates",
        "edgeStates",
        "driving",
        "actionStates",
        "instantActionStates",
        "powerSupply",
        "operatingMode",
        "errors",
        "safetyState"
    ],
    "properties": {
        "headerId": {
            "type": "integer",
            "description": "headerId of the message. The headerId is defined per topic and incremented by 1 with each sent (but not necessarily received) message."
        },
        "timestamp": {
            "type": "string",
            "format": "date-time",
            "description": "Timestamp in ISO8601 format (YYYY-MM-DDTHH:mm:ss.fffZ).",
            "examples": [
                "1991-03-11T11:40:03.123Z"
            ]
        },
        "version": {
            "type": "string",
            "description": "Version of the protocol [Major].[Minor].[Patch]",
            "examples": [
                "1.3.2"
            ]
        },
        "manufacturer": {
            "type": "string",
            "description": "Manufacturer of the mobile robot"
        },
        "serialNumber": {
            "type": "string",
            "description": "Serial number of the mobile robot."
        },
        "maps":{
            "type": "array",
            "description": "Array of map-objects that are currently stored on the mobile robot.",
            "items": {
				"$ref": "#/definitions/map"
			}
        },
        "zoneSets":{
            "type": "array",
            "description": "Array of zoneSet objects that are currently stored on the mobile robot.",
            "items": {
				"$ref": "#/definitions/zoneSet"
			}
        },
        "orderId": {
            "type": "string",
            "description": "Unique order identification of the current order or the previous finished order. The orderId is kept until a new order is received. Empty string (\"\") if no previous orderId is available."
        },
        "orderUpdateId": {
            "type": "integer",
            "description": "Order Update Identification to identify that an order update has been accepted by the mobile robot. 0 if no previous orderUpdateId is available."
        },
        "lastNodeId": {
            "type": "string",
            "description": "Node ID of last reached node or, if mobile robot is currently on a node, current node (e.g., \"node7\"). Empty string (\"\") if no lastNodeId is available."
        },
        "lastNodeSequenceId": {
            "type": "integer",
            "description": "sequenceId of the last reached node or, if the mobile robot is currently on a node, sequenceId of current node. 0 if no lastNodeSequenceId is available."
        },
		"nodeStates": {
            "type": "array",
            "description": "Array of nodeState-Objects, that need to be traversed for fulfilling the order. Empty list if idle.",
            "items": {
                "$ref": "#/definitions/nodeState"
            }
        },
        "edgeStates": {
            "type": "array",
            "description": "Array of edgeState-Objects, that need to be traversed for fulfilling the order, empty list if idle.",
            "items": {
				"$ref": "#/definitions/edgeState"
			}
        },
        "plannedPath": {
            "$ref": "#/definitions/plannedPath"
        },
        "intermediatePath": {
            "$ref": "#/definitions/intermediatePath"
        },
        "mobileRobotPosition": {
            "$ref": "#/definitions/mobileRobotPosition"
        },
        "velocity": {
            "type": "object",
            "description": "The mobile robot's velocity in mobile robot coordinates",
            "properties": {
                "vx": {
                    "type": "number",
                    "description":"The mobile robot's velocity in its x direction",
                    "unit": "m/s"
                },
                "vy": {
                    "type": "number",
                    "description":"The mobile robot's velocity in its y direction",
                    "unit": "m/s"
                },
                "omega": {
                    "type": "number",
                    "description":"The mobile robot's turning speed around its z axis.",
                    "unit": "rad/s"
                }
            }
        },
        "loads": {
            "type": "array",
            "description": "Loads, that are currently handled by the mobile robot. Optional: If mobile robot cannot determine load state, leave the array out of the state. If the mobile robot can determine the load state, but the array is empty, the mobile robot is considered unloaded.",
            "items": {
                "$ref": "#/definitions/load"
            }
        },
        "driving": {
            "type": "boolean",
            "description": "True: indicates that the mobile robot is driving and/or rotating. Other movements of the mobile robot (e.g., lift movements) are not included here.\nFalse: indicates that the mobile robot is neither driving nor rotating."
        },
        "paused": {
            "type": "boolean",
            "description": "True: mobile robot is currently in a paused state, either because of the push of a physical button on the mobile robot or because of an instantAction. The mobile robot can resume the order.\nFalse: The mobile robot is currently not in a paused state."
        },
        "newBaseRequest": {
            "type": "boolean",
            "description": "True: mobile robot is almost at the end of the base and will reduce speed if no new base is transmitted. Trigger for fleet control to send new base\nFalse: no base update required."
        },
		"zoneRequests": {
            "description": "Array of zoneRequest objects that are currently active on the mobile robot. Empty array if no zone requests are active.",
            "type": "array",
            "items": {
				"$ref": "#/definitions/zoneRequest"
            }
        },
        "edgeRequests": {
            "description": "Array of edgeRequest objects that are currently active on the mobile robot. Empty array if no edge requests are active.",
            "type": "array",
            "items": {
				"$ref": "#/definitions/edgeRequest"
            }
        },
        "distanceSinceLastNode": {
            "type": "number",
            "description": "Used by line guided vehicles to indicate the distance it has been driving past the lastNodeId. Distance is in meters."
        },
        "actionStates": {
            "type": "array",
            "description": "Array of the current actions and the actions which are yet to be finished. This may include actions from previous nodes that are still in progress\nWhen an action is completed, an updated state message is published with actionStatus set to finished and if applicable with the corresponding resultDescriptor. The actionStates are kept until a new order is received.",
            "items": {
                "$ref": "#/definitions/actionState"
            }
        },
        "instantActionStates": {
            "type": "array",
            "description": "Array of all instant action states that the mobile robot received. Empty array if the mobile robot has not received any instant actions. Instant actions are kept in the state until restart or action clearInstantActions is executed.",
            "items": {
                "$ref": "#/definitions/actionState"
            }
        },
        "zoneActionStates": {
            "type": "array",
            "description": "Array of all zone actions that are in an end state or are currently running; sharing upcoming actions is optional. Zone action states are kept in the state message until restart or action clearZoneActions is executed.",
            "items": {
                "$ref": "#/definitions/actionState"
            }
        },
        "powerSupply": {
            "$ref": "#/definitions/powerSupply"
        },
        "operatingMode": {
            "type": "string",
            "description": "Current operating mode of the mobile robot.",
            "enum": [
                "STARTUP",
                "AUTOMATIC",
                "SEMIAUTOMATIC",
                "INTERVENED",
                "MANUAL",
                "SERVICE",
                "TEACH_IN"
            ]
        },
        "errors": {
            "type": "array",
            "description": "Array of error-objects. All active errors of the mobile robot should be in the list. An empty array indicates that the mobile robot has no active errors.",
            "items": {
				"$ref": "#/definitions/error"
            }
        },
        "information": {
            "type": "array",
            "description": "Array of info-objects. An empty array indicates, that the mobile robot has no information. This should only be used for visualization or debugging – it must not be used for logic in fleet control.",
            "items": {
				"$ref": "#/definitions/info"
            }
        },
        "safetyState": {
            "$ref": "#/definitions/safetyState"
        }
    },
    "definitions": {
		"map": {
			"type": "object",
			"title": "map",
			"required": [
				"mapId",
				"mapVersion",
				"mapStatus"
			],
			"properties": {
				"mapId": {
					"type": "string",
					"description": "ID of the map describing a defined area of the mobile robot's workspace."
				},
				"mapVersion": {
					"type": "string",
					"description": "Version of the map."
				},
				"mapDescriptor": {
					"type": "string",
					"description": "A user-defined, human-readable name or descriptor"
				},
				"mapStatus": {
					"type": "string",
					"description": "Information on the status of the map indicating, if a map version is currently used on the mobile robot. ENABLED: Indicates this map is currently active / used on the mobile robot. At most one map with the same mapId can have its status set to ENABLED.<br>DISABLED: Indicates this map version is currently not enabled on the mobile robot and thus could be enabled or deleted by request.",
					"enum": [
						"ENABLED",
						"DISABLED"
					]
				}
			}
		},
		"zoneSet": {
			"type": "object",
			"title": "zoneSet",
			"required": [
				"zoneSetId",
				"mapId",
				"zoneSetStatus"
			],
			"properties": {
				"zoneSetId": {
					"type": "string",
					"description": "Unique identifier of the zone set that is currently enabled for the map.<br> This field shall be left empty only if the mobile robot has no zones defined for the corresponding map."
				},
				"mapId": {
					"type": "string",
					"description": "Identifier of the corresponding map."
				},
				"zoneSetStatus": {
					"type": "string",
…(발췌: 전체 34,440자 중 앞 11,051자)
```

### data/source_texts/ref-105.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
# FLEET CONFIG =================================================================
# RMF Fleet parameters

rmf_fleet:
  name: "tinyRobot"
  limits:
    linear: [0.5, 0.75] # velocity, acceleration
    angular: [0.6, 2.0] # velocity, acceleration
  profile: # Robot profile is modelled as a circle
    footprint: 0.3 # radius in m
    vicinity: 0.5 # radius in m
  reversible: True # whether robots in this fleet can reverse
  battery_system:
    voltage: 12.0 # V
    capacity: 24.0 # Ahr
    charging_current: 5.0 # A
  mechanical_system:
    mass: 20.0 # kg
    moment_of_inertia: 10.0 #kgm^2
    friction_coefficient: 0.22
  ambient_system:
    power: 20.0 # W
  tool_system:
    power: 0.0 # W
  recharge_threshold: 0.10 # Battery level below which robots in this fleet will not operate
  recharge_soc: 1.0 # Battery level to which robots in this fleet should be charged up to during recharging tasks
  publish_fleet_state: 10.0 # Publish frequency for fleet state, ensure that it is same as robot_state_update_frequency
  account_for_battery_drain: True
  task_capabilities: # Specify the types of RMF Tasks that robots in this fleet are capable of performing
    loop: True
    delivery: True
  actions: ["some_action_here"]
  finishing_request: "park" # [park, charge, nothing]
  responsive_wait: True # Should responsive wait be on/off for the whole fleet by default? False if not specified.
  robots:
    tinyRobot1:
        charger: "tinyRobot1_charger"
        responsive_wait: False # Should responsive wait be on/off for this specific robot? Overrides the fleet-wide setting.
    tinyRobot2:
        charger: "tinyRobot2_charger"
        # No mention of responsive_wait means the fleet-wide setting will be used

  robot_state_update_frequency: 10.0 # Hz

fleet_manager:
  prefix: "http://127.0.0.1:8080"
  user: "some_user"
  password: "some_password"

# TRANSFORM CONFIG =============================================================
# For computing transforms between Robot and RMF coordinate systems

# Optional
reference_coordinates:
  L1:
    rmf: [[20.33, -3.156],
          [8.908, -2.57],
          [13.02, -3.601],
          [21.93, -4.124]]
    robot: [[59, 399],
          [57, 172],
          [68, 251],
          [75, 429]]
```

### data/source_texts/ref-148.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://raw.githubusercontent.com/open-rmf/rmf_api_msgs/main/rmf_api_msgs/schemas/robot_state.json",
  "title": "Robot State",
  "description": "The state of a robot",
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "status": {
      "description": "A simple token representing the status of the robot",
      "type": "string",
      "enum": ["uninitialized", "offline", "shutdown", "idle", "charging", "working", "error"]
    },
    "task_id": {
      "description": "The ID of the task this robot is currently working on. Empty string if the robot is not working on a task.",
      "type": "string"
    },
    "unix_millis_time": { "type": "integer" },
    "location": { "$ref": "location_2D.json" },
    "battery": {
      "description": "State of charge of the battery. Values range from 0.0 (depleted) to 1.0 (fully charged)",
      "type": "number",
      "minimum": 0.0,
      "maximum": 1.0
    },
    "issues": {
      "description": "A list of issues with the robot that operators need to address",
      "type": "array",
      "items": { "$ref": "#/$defs/issue" }
    },
    "commission": { "$ref": "commission.json" },
    "mutex_groups": {
      "description": "Information about the mutex groups that this robot is interacting with",
      "type": "object",
      "properties": {
        "locked": {
          "description": "A list of mutex groups that this robot has currently locked",
          "type": "array",
          "items": { "type": "string" }
        },
        "requesting": {
          "description": "A list of the mutex groups that this robot is currently requesting but has not lockd yet",
          "type": "array",
          "items": { "type": "string" }
        }
      }
    }
  },
  "$defs": {
    "issue": {
      "description": "An issue that an operator needs to respond to (e.g. stuck, lost)",
      "type": "object",
      "properties": {
        "category": {
          "description": "Category of the robot's issue",
          "type": "string"
        },
        "detail": {
          "description": "Detailed information about the issue",
          "anyOf": [
            { "type": "object" },
            { "type": "array" },
            { "type": "string" }
          ]
        }
      }
    }
  }
}
```

### data/source_texts/ref-251.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
# Mobile Robot Fleet Integration

Here we will cover integrating a mobile robot fleet that offers the **Full Control** category of fleet adapter, as **discussed** in the [RMF Core Overview](./rmf-core.md) chapter.
This means we assume the mobile robot fleet manager allows us to specify explicit paths for the robot to follow, and that the path can be interrupted at any time and replaced with a new path.
Furthermore, each robot's position will be updated live as the robots are moving.

## Route Map

Before such a fleet can be integrated, you will need to procure or produce a route map as described in the [previous section](./integration_nav-maps.md). The fleet adapter uses the route map to plan out feasible routes for the vehicles under its control, taking into account the schedules of all other vehicles. It will also use the route map to decide out how to negotiate with other fleet adapters when a scheduling conflict arises. The adapter will only consider moving the robots along routes that are specified on the route map, so it is important that the route coverage is comprehensive. At the same time, if there are extraneous waypoints on the route map, the adapter might spend more time considering all the possibilities than what should really be needed, so it is a good idea to have a balance of comprehensiveness and leanness.

## C++ API

The C++ API for **Full Control** automated guided vehicle (AGV) fleets can be found in the [`rmf_fleet_adapter`](https://github.com/open-rmf/rmf_ros2/tree/main/rmf_fleet_adapter) package of the `rmf_ros2` repo. The API consists of four critical classes:

* [`Adapter`](https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/Adapter.hpp) - Initializes and maintains communication with the other core RMF systems. Use this to register one or more fleets and receive a `FleetUpdateHandle` for each fleet.
* [`FleetUpdateHandle`](https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/FleetUpdateHandle.hpp) - Allows you to configure a fleet by adding robots and specifying settings for the fleet (e.g. specifying what types of deliveries the fleet can perform). New robots can be added to the fleet at any time.
* [`RobotUpdateHandle`](https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp) - Use this to update the position of a robot and to notify the adapter if the robot's progress gets interrupted.
* [`RobotCommandHandle`](https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotCommandHandle.hpp) - This is a pure abstract interface class. The functions of this class must be implemented to call upon the API of the specific fleet manager that is being adapted.

The C++ API for **Easy Full Control** fleets provides a simple and more accessible way for users to integrate with the Full Control library without having to modify its internal logic. It can be found in the [rmf_fleet_adapter](https://github.com/open-rmf/rmf_ros2/tree/main/rmf_fleet_adapter) package of the `rmf_ros2` repo. The [`EasyFullControl`](https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/EasyFullControl.hpp) class contains helpful methods for users to create a `Configuration` object from YAML files encapsulating important fleet configuration parameters and navigation graphs, as well as to make their own fleet adapter with the `Configuration` object. The `add_robot(~)` method is provided for users to add robots to the new fleet adapter. This method takes in various callbacks that should be written by the user, and will be triggered whenever RMF is retrieving robot state information from the fleet or sending out commands to perform a particular process (navigation, docking, action, etc.). An example of the EasyFullControl fleet adapter can be found in [`fleet_adapter.py`](https://github.com/open-rmf/rmf_demos/blob/main/rmf_demos_fleet_adapter/rmf_demos_fleet_adapter/fleet_adapter.py) under the `rmf_demos` repo.

The C++ API for **Traffic Light Control** fleets (i.e. fleets that only allow RMF to pause/resume each mobile robot) can also be found in the `rmf_fleet_adapter` package of the `rmf_ros2` repo. The API reuses the `Adapter` class and requires users to initialize their fleet using either of the APIs [here](https://github.com/open-rmf/rmf_ros2/blob/9b4b8a8cc38b323f875a55c70f307446584d1639/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/Adapter.hpp#L106-L180). The user has the option to integrate via the [`TrafficLight`](https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/TrafficLight.hpp) API or for greater convenience, via the [`EasyTrafficLight`](https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/EasyTrafficLight.hpp) API.

The basic workflow of developing a fleet adapter is the following:

1. Create an application that links to the `rmf_fleet_adapter` library.
2. Have the application read in runtime parameters in whatever way is desired (e.g. command line arguments, configuration file, ROS parameters, REST API calls, environment variables, etc).
3. Construct a route graph for each fleet that this application is providing the adapter for (a single adapter application can service any number of fleets), and/or parse the route graph from a YAML file using the [`rmf_fleet_adapter::agv::parse_graph`](https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/parse_graph.hpp) utility.
4. Instantiate an `rmf_fleet_adapter::agv::Adapter` using `Adapter::make(~)` or `Adapter::init_and_make(~)`.
5. Add the fleets that the application will be responsible for adapting, and save the `rmf_fleet_adapter::agv::FleetUpdateHandlePtr` instances that are passed back.
6. Implement the `RobotCommandHandle` class for the fleet manager API that is being adapted.
7. Add the robots that the adapter is responsible for controlling. The robots can be added based on the startup configuration, or they can be dynamically added during runtime as they are discovered over the fleet manager API (or both).
    - When adding a robot, you will need to create a new instance of the custom `RobotCommandHandle` that you implemented.
    - You will also need to provide a callback that will be triggered when the adapter is finished registering the robot. This callback will provide you with a new `RobotUpdateHandle` for your robot. It is imperative to save this update handle so you can use it to update the robot's position over time.
8. As new information arrives from the fleet manager API, use the collection of `RobotUpdateHandle` classes to keep the adapter up-to-date on the robots' positions.

An example of a functioning fleet adapter application can be found in the [`full_control` backwards-compatibility adapter](https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/src/full_control/main.cpp). This is a fleet adapter whose fleet-side API is the "Fleet Driver API", which is a deprecated prototype API for the RMF **Full Control** category of fleet adapters. This fleet adapter exists temporarily to maintain backwards compatibility with the old "Fleet Driver" implementations and to serve as an example of how to implement a fleet adapter using the new C++ API.

## Python Bindings

You may also choose to use Python to implement your fleet adapter. You can find Python bindings for the C++ API in the [rmf_fleet_adapter_python repo](https://github.com/open-rmf/rmf_ros2/tree/main/rmf_fleet_adapter_python). The Python bindings literally just port the C++ API into Python so that you can develop your fleet adapter using Python instead of C++. The above API and workflow are exactly the same, just in Python instead. This should be very useful for fleets that use REST APIs, because you'll have access to tools like [Swagger](https://swagger.io/tools/open-source/getting-started/) which can help you generate client code for the fleet's REST API server.

## Fleet Adapter Template
To make the process of integrating a robotic fleet with RMF even simpler, we have open-sourced a **Full Control** [template package](https://github.com/open-rmf/fleet_adapter_template) where users only need to update certain blocks of code with the API calls to their specific robot/fleet manager. This template uses the `EasyFullControl` API, where user-implemented robot callbacks are executed by RMF. This way, users can integrate RMF while using their preferred APIs between the fleet adapter and their robots. Do note that this template is just one of many ways to integrate fleets with REST or websocket based APIs. The following diagram illustrates how RMF can communicate with fleet robots using the APIs chosen by the user and the robot vendor.

<img src="images/fleet_adapter_flow.png">

This fleet adapter system is also integrated in our demos worlds with simulation robots, which is further elaborated in the next section.

You can follow these steps to build your fleet adapter on top of the given template:
1. Fill in the missing code in [`RobotClientAPI.py`](https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/fleet_adapter_template/RobotClientAPI.py). With your chosen API (it could be ROS messages or any custom API), RMF will be able to command your robots and retrieve state updates. The crucial callbacks are:
   - [`navigate()`](https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/fleet_adapter_template/RobotClientAPI.py#L43): Commands your robot to a target location given the coordinates `[x, y, yaw]`.
   - [`stop()`](https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/fleet_adapter_template/RobotClientAPI.py#L75): Commands your robot to stop in place.
   - [`execute_action()`](https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/fleet_adapter_template/fleet_adapter.py#L231): Triggers any custom action you would like your robot to perform when provided with a `category` and `description`, which detail the action name and task-specific parameters respectively. You may optionally want to make use of [`RobotAPI.start_activity`](https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/fleet_adapter_template/RobotClientAPI.py#L59) to trigger different types of actions for your robot.
   - [`map()`](https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/fleet_adapter_template/RobotClientAPI.py#L99), [`position()`](https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/fleet_adapter_template/RobotClientAPI.py#L83) and [`battery_soc()`](https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/fleet_adapter_template/RobotClientAPI.py#L91) each allows RMF to retrieve the relevant data from your robot. The robot state information helps RMF to allocate tasks, plan routes and initiate charging when needed.
2. For **each** robot fleet, create a [`config.yaml`](https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml) file to include important fleet parameters. These parameters will be passed to the fleet adapter and configured when initializing the fleet. Do note that you must list all robots in the fleet under [`robots`](https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml#L35) to ensure that they are registered to the RMF fleet.
3. [Optional] Create a fleet manager that interfaces with your fleet's robots if you'd like a consolidated manager for your fleet, rather than having RMF communicate with the individual robots. This fleet manager would be a bridge between the RMF fleet adapter and your fleet robots, as depicted in the diagram above. It should be able to relay navigation commands to the fleet robots and also report their robot statuses. If you have multiple fleets using different robot APIs, make sure to create separate fleet managers for these fleets.

   If you have opted to use a fleet manager, you may find it helpful to include any relevant data in the fleet `config.yaml`, demonstrated in the `fleet_manager` section [here](https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml#L45).

You may refer to the [Fleet Adapter Tutorial](./integration_fleets_adapter_tutorial.md) section in this Book or `rmf_demos` [`RobotClientAPI`](https://github.com/open-rmf/rmf_demos/blob/main/rmf_demos_fleet_adapter/rmf_demos_fleet_adapter/RobotClientAPI.py) for examples and in-depth step-by-step instructions.

Once you are done, you can run both the fleet adapter and any custom fleet manager. Remember to parse the configuration file and navigation graph when launching the adapter.

## Case Study: RMF Demos Fleet Adapter

The Python implementation of the **Full Control** fleet adapter classes is demonstrated in the [demos fleet adapter](https://github.com/open-rmf/rmf_demos/tree/main/rmf_demos_fleet_adapter). Building on top of the fleet adapter template, the demos fleet adapter uses REST API as an interface between the adapter and the simulation robots: the adapter sends out commands to the robots, while the robots update the adapter on their current state information. This is done by creating a [`fleet_manager`](https://github.com/open-rmf/rmf_demos/blob/main/rmf_demos_fleet_adapter/rmf_demos_fleet_adapter/fleet_manager.py) node that contains the necessary REST endpoints for `RobotClientAPI` to interact with.

<img src="images/demo_fleet_adapter_flow.png">

### Demos Fleet Manager

Whenever a command is ready to be sent from the RMF fleet adapter, it will call the relevant API function defined in `RobotClientAPI` and query the corresponding endpoint from the API server in the `fleet_manager` node. Each function either retrieves specific information about the robot's current state (including but not limited to its last known position, remaining battery level, and whether it has completed a request), or sends a command to the robot to carry out a request. The robot state information is required for the fleet adapter to update the traffic schedule, plan for subsequent tasks, and guide robots across different paths in the environment.

The demos fleet adapter is integrated with the simulation robots which publish their state information via internal ROS2 messages, hence the `fleet_manager` also serves to consolidate the messages published by different robots from its fleet and sends them to the designated robot's fleet adapter. The API endpoints are designed such that the adapter can query information or send commands to a particular robot by specifying the robot's name. The `fleet_manager` will ensure that the robot exists in the fleet before returning the requested state information or relaying commands to the simulation robot. Additionally, the adapter can retrieve the status of the entire fleet's robots.

### Fleet Configuration

There are four **Full Control** fleets in our demo simulation, each with their own fleet-specific parameters. To better consolidate and set up these configurations upon initializing the fleet, they are stored in a [`config.yaml`](https://github.com/open-rmf/rmf_demos/blob/main/rmf_demos/config/office/tinyRobot_config.yaml) file. Paths to the configuration and navigation graph files are required when running the fleet adapter and manager. General fleet settings and capabilities are defined under the `rmf_fleet` section.
…(발췌: 전체 16,319자 중 앞 15,642자)
```

### data/source_texts/ref-287.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
////
Copyright © 2016-2021 The Eclipse Foundation, Cirrus Link Solutions, and others

This program and the accompanying materials are made available under the
terms of the Eclipse Public License v. 2.0 which is available at
https://www.eclipse.org/legal/epl-2.0.

SPDX-License-Identifier: EPL-2.0

Sparkplug®, Sparkplug Compatible, and the Sparkplug Logo are trademarks of the Eclipse Foundation.
////

// set default value if assetsdir hasn't been defined
ifndef::assetsdir[:assetsdir:]

[[operational_behavior]]
== Operational Behavior

An MQTT based SCADA system is unique in that the Primary Host Application is not responsible for
establishing and maintaining connections to the Edge Nodes as is the case in most existing legacy
poll/response device protocols. With an MQTT based architecture, both the Host Applications as well
as the Edge Nodes establish MQTT Sessions with one or more central MQTT Servers. This is the desired
functionality as it provides the necessary decoupling from any one application and any given
Edge Node/Device. Additional Sparkplug Host Application MQTT clients can connect and subscribe to
any of the real time data without impacting the Primary Host Application.

Due to the nature of real time SCADA solutions, it is very important for the Primary Host
Application and all connected Edge Nodes to have the MQTT Session state
information for each other. In order to accomplish this the Sparkplug Topic Namespace definitions
for Birth/Death Certificates along with the defined payloads provide both state and context between
the Primary Host Application and the associated Edge Nodes. In most use cases and solution scenarios
there are two main reasons for this "designation" of a Primary Host Application:

[arabic]
. Only the Primary Host Application should have the permission to issue commands to Edge Nodes.
. In high availability and redundancy use cases where multiple MQTT Servers are used, Sparkplug Edge
Nodes need to be aware of whether the Primary Host Application is connected to each MQTT Server in
the infrastructure. If the Primary Host Application STATE shows that an Edge Node is connected to an
MQTT Server that the Primary Host Application is *NOT* connected to, then the Edge Node should
connect to the next available MQTT Server where STATE for the Primary Host Application shows
'online=true'.

[[operational_behavior_timestamps]]
=== Timestamps in Sparkplug

An important aspect of Sparkplug is its use of time. All timestamps must be in Coordinated
Universal Time (UTC). In order to ensure this is the case, all Sparkplug Edge Nodes and Sparkplug
Host Applications must have an accurate mechanism for ensuring their clocks remain accurate. This is
typically left to the system operating system using technologies such as Network Time Protocol
(NTP). Regardless of the mechanism used, ensuring all timestamps are accurate and in UTC is
critical to all timestamps in Sparkplug.

[[operational_behavior_case_sensitivity]]
=== Case Sensitivity in Sparkplug

The MQTT specification states that MQTT topics are case sensitive [MQTTV5-4.7.3]. For example, the
topic a/b is different than A/b. Sparkplug in turn is also case sensitive with regard to both topics
as well as metric names. So, a metric 'temperature' is not the same as the metric 'Temperature'.
However, this generally should be avoided. Many Host Applications may not be able to differentiate
the two metric names as unique. Many databases are case-insensitive and would not be able to handle
this situation well.

* [tck-testable tck-id-case-sensitivity-sparkplug-ids]#[yellow-background]*[tck-id-case-sensitivity-sparkplug-ids] Edge
Nodes in a Sparkplug environment SHOULD NOT have Sparkplug IDs (Group, Edge Node, or Device IDs)
that when converted to lower case match*#
** For example there should not be two different Edge Nodes publishing NBIRTH messages on these two
topics spBv1.0/Group1/NBIRTH/EdgeNode1 and spBv1.0/group1/NBIRTH/edgenode1
* [tck-testable tck-id-case-sensitivity-metric-names]#[yellow-background]*[tck-id-case-sensitivity-metric-names] An
Edge Node SHOULD NOT publish metric names that when converted to all lower case match.*#
** For example a DBIRTH should not contain a metric 'a' and another metric 'A'.

[[operational_behavior_primary_host_application_session_establishment]]
=== Host Application Session Establishment

The Sparkplug Host Application upon startup or reconnect will immediately try to create a Host MQTT
Session with the configured MQTT Server infrastructure. Note that the establishment of an Host
Application MQTT session is asynchronous of any other MQTT Client session. If Edge Nodes are already
connected to the MQTT Server infrastructure, the Sparkplug Host Application will synchronize using
the STATE MQTT topic. If associated Edge Nodes are not connected, the Sparkplug Host Application
will synchronize with the Edge Nodes and their data streams when the Edge Nodes publish their Birth
Certificates. Any Edge Node that has specified this Sparkplug Host Application as its Primary Host
Application will will wait to publish their Birth Certificates until after they receive the STATE
message denoting that the Primary Host application is online.

.Figure 4 - Host Session Establishment
plantuml::{assetsdir}assets/plantuml/host-session-establishment.puml[format=svg, alt="Host Session Establishment"]

The session diagram in Figure 3 - Host Session Establishment shows a very simple topology with a
single MQTT Server. The steps outlined in the session diagram are defined as follows:

[arabic]
. Sparkplug Host Applications will try to create an MQTT Session using the MQTT CONNECT Control
Packet. A Death Certificate is constructed into the MQTT Will Topic and Will Payload of the
CONNECT Control Packet with a Will QoS set to 1 and Will Retain flag set to true.
+
[tck-testable tck-id-message-flow-phid-sparkplug-clean-session-311]#[yellow-background]*[tck-id-message-flow-phid-sparkplug-clean-session-311] The
CONNECT Control Packet for all Sparkplug Host Applications when using MQTT 3.1.1 MUST set the MQTT
'Clean Session' flag to true.*#
+
[tck-testable tck-id-message-flow-phid-sparkplug-clean-session-50]#[yellow-background]*[tck-id-message-flow-phid-sparkplug-clean-session-50] The
CONNECT Control Packet for all Sparkplug Host Applications when using MQTT 5.0 MUST set the the MQTT
'Clean Start' flag to true and the 'Session Expiry Interval' to 0.*#
+
The MQTT CONNECT Control Packet is acknowledged as successful with a valid MQTT CONNACK Control
Packet from the MQTT Server. From this point forward in time, the MQTT Server is ready to deliver a
Host Death Certificate any time the Sparkplug Host Application MQTT Client loses connectivity to the
MQTT Server.

. With the MQTT Session established, Sparkplug Host Application MUST issue an MQTT subscription for
the defined Sparkplug Topic Namespace.
+
[tck-testable tck-id-message-flow-phid-sparkplug-subscription]#[yellow-background]*[tck-id-message-flow-phid-sparkplug-subscription] The
subscription on the Sparkplug Topic Namespace and the STATE topic MUST be done immediately after
successfully establishing the MQTT session and before publishing its own STATE message.*#

. [tck-testable tck-id-message-flow-phid-sparkplug-state-publish]#[yellow-background]*[tck-id-message-flow-phid-sparkplug-state-publish] Once
an MQTT Session has been established, the Sparkplug Host Application subscriptions on the Sparkplug
Topic Namespace have been established and the STATE topic subscription has been established, the
Sparkplug Host Application MUST publish a new STATE message.*#
+
[tck-testable tck-id-message-flow-phid-sparkplug-state-publish-payload]#[yellow-background]*[tck-id-message-flow-phid-sparkplug-state-publish-payload] The
Host Application Birth Certificate Payload MUST be JSON UTF-8 data. It MUST include two key/value
pairs where one key MUST be 'online' and its value is a boolean 'true'. The other key MUST be
'timestamp' and the value MUST be the same value set in the immediately prior MQTT CONNECT packet's
Will Message payload.*#
+
[tck-testable tck-id-message-flow-phid-sparkplug-state-publish-payload-timestamp]#[yellow-background]*[tck-id-message-flow-phid-sparkplug-state-publish-payload-timestamp] The
timestamp value in the Host Application Birth Certificate payload MUST be the same value set in the
immediately prior MQTT CONNECT packet's Will Message payload.*#
+
The Host Application is now ready to start receiving MQTT messages from any connected Edge Node
within the infrastructure. At this point, the Host Application can update the MQTT Client metrics in
the Host Application with a current state of 'online' once each Edge Node publishes its Sparkplug
NBIRTH and DBIRTH messages. Since the Sparkplug Host Application is also relying on the MQTT Session
to the MQTT Server(s), the availability of MQTT Servers to the Host Application is also being
monitored and reflected in the MQTT Client metrics in the Host Application.
. If at any point in time Host Application loses connectivity with the defined MQTT Server(s), the
online=true state of the Server is immediately reflected in the MQTT Client metrics in the Host
Application.
+
[tck-not-testable]#[yellow-background]*All metric data associated with any Sparkplug Edge Node that
was connected to that MQTT Server and known by the Host Application MUST be updated to a STALE data
quality if the Host Application loses connection to the MQTT Server.*#

[tck-testable tck-id-message-flow-hid-sparkplug-state-message-delivered]#[yellow-background]*[tck-id-message-flow-hid-sparkplug-state-message-delivered] After
publishing its own Host Application STATE message, if at any point the Host Application is delivered
a STATE message on its own Host Application ID with a 'online' value of false, it MUST immediately
republish its STATE message to the same MQTT Server with a 'online' value of true and the
'timestamp' set to the same value that was used for the timestamp in its own prior MQTT CONNECT
packet Will Message payload.*#

[[operational_behavior_edge_node_session_establishment]]
=== Edge Node Session Establishment

Prior to sending an NBIRTH message, the MQTT client associated with the Edge Node must subscribe to
receive NCMD messages with the following rules.

* [tck-testable tck-id-message-flow-edge-node-ncmd-subscribe]#[yellow-background]*[tck-id-message-flow-edge-node-ncmd-subscribe] The
MQTT client associated with the Edge Node MUST subscribe to a topic of the form
'spBv1.0/group_id/NCMD/edge_node_id' where group_id is the Sparkplug Group ID and the edge_node_id
is the Sparkplug Edge Node ID for this Edge Node. It MUST subscribe on this topic with a QoS of
1.*#
** This subscription is mandatory as Edge Nodes MUST be able to respond to 'rebirth requests'.

After subscribing, the Edge Node must follow these additional rules.

* [tck-testable tck-id-message-flow-edge-node-birth-publish-connect]#[yellow-background]*[tck-id-message-flow-edge-node-birth-publish-connect] Any
Edge Node in the MQTT infrastructure MUST establish an MQTT Session prior to publishing NBIRTH and
DBIRTH messages.*#
* [tck-testable tck-id-message-flow-edge-node-birth-publish-will-message]#[yellow-background]*[tck-id-message-flow-edge-node-birth-publish-will-message] When
a Sparkplug Edge Node sends its MQTT CONNECT packet, it MUST include a Will Message.*#
* [tck-testable tck-id-message-flow-edge-node-birth-publish-will-message-topic]#[yellow-background]*[tck-id-message-flow-edge-node-birth-publish-will-message-topic] The
Edge Node's MQTT Will Message's topic MUST be of the form 'spBv1.0/group_id/NDEATH/edge_node_id'
where group_id is the Sparkplug Group ID and the edge_node_id is the Sparkplug Edge Node ID for this
Edge Node*#
* [tck-testable tck-id-message-flow-edge-node-birth-publish-will-message-payload]#[yellow-background]*[tck-id-message-flow-edge-node-birth-publish-will-message-payload] The
Edge Node's MQTT Will Message's payload MUST be a Sparkplug Google Protobuf encoded payload.*#
* [tck-testable tck-id-message-flow-edge-node-birth-publish-will-message-payload-bdSeq]#[yellow-background]*[tck-id-message-flow-edge-node-birth-publish-will-message-payload-bdSeq] The
Edge Node's MQTT Will Message's payload MUST include a metric with the name of 'bdSeq', the datatype
of INT64, and the value MUST be incremented by one from the value in the previous MQTT CONNECT
packet unless the value would be greater than 255. If in the previous NBIRTH a value of 255 was
sent, the next MQTT Connect packet Will Message payload bdSeq number value MUST have a value of 0.*#
* [tck-testable tck-id-message-flow-edge-node-birth-publish-will-message-qos]#[yellow-background]*[tck-id-message-flow-edge-node-birth-publish-will-message-qos] The
Edge Node's MQTT Will Message's MQTT QoS MUST be 1.*#
* [tck-testable tck-id-message-flow-edge-node-birth-publish-will-message-will-retained]#[yellow-background]*[tck-id-message-flow-edge-node-birth-publish-will-message-will-retained] The
Edge Node's MQTT Will Message's retained flag MUST be set to false.*#

Edge Nodes can be configured to support the concept of a 'Primary Host Application'. In this case,
the Edge Node must wait until the Primary Host Application is online and subscribed to Sparkplug
messages before the Edge Node publishes its NBIRTH and DBIRTH messages. Specifying a Primary Host is
not required for an Edge Node. But it is often desired. For example say an Edge Node is in a
Sparkplug environment and there is a single consuming Host Application that historizes the data. It
would not be beneficial for the Sparkplug Edge Node to publish data if the Host Application is not
connected and subscribed to messages. Instead, it would be better for the Edge Node to store data
while the Host Application is offline. Once the Host Application is properly connected, it could
then send all of its stored data and continue publishing normally. Once the Sparkplug Edge Node has
successfully connected to the MQTT Server, it must publish a NBIRTH message. The NBIRTH message must
follow the following rules. Note if Primary Host is configured for the Edge Node, it must also wait
until the Primary Host denotes it is online before the Edge Node publishes its NBIRTH message.
…(발췌: 전체 78,622자 중 앞 14,269자)
```

### data/source_texts/ref-405.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

````text
# Security

This chapter describes how to use DDS Security tools to provide authentication,
encryption, and access control to an RMF system.

The security of the RMF system can be divided into two main parts:
its ROS 2 elements and the dashboard. The security of the ROS 2
elements is provided by the DDS security tools which help ensure authentication,
encryption and access control. The dashboard provides the user with an
instruments panel while ensuring encryption, integrity and authentication of
the connection to the server through TLS. User authentication and access control
is made by user/password checking against a database and then
 providing that user with access to the secured ROS 2 network at a level that
corresponds to the role of that user.

![Security System Infrastructure](images/security/system_infrastructure.png)

The [RMF Demos Office World](https://github.com/open-rmf/rmf_demos#office-world) repository contains an example of a
full RMF application using secured ROS 2 communications along with
step by step explanations.

## ROS 2 Security

ROS 2 contains tools that help create and load the needed security artifacts
to enable DDS-security. RMF makes uses of these tools in order to enable
security on its ROS 2 elements. A brief introduction to these tools and its
usage is provided here. For a deeper understanding of the whole system,
please refer to the [ROS 2 DDS-Security integration][SROS] documentation.

### DDS-Security overview

The [DDS-Security specification][dds_security] expands upon the [DDS specification][dds],
adding security enhancements by defining a Service Plugin Interface (SPI)
architecture, a set of builtin implementations of the SPIs, and the security model enforced by the SPIs.
Specifically, there are five SPIs defined:

- **Authentication**: Verify the identity of a given domain participant.
- **Access control**: Enforce restrictions on the DDS-related operations that can be
performed by an authenticated domain participant.
- **Cryptographic**: Handle all required encryption, signing, and hashing operations.
- **Logging**: Provide the ability to audit DDS-Security-related events.
- **Data tagging**: Provide the ability to add tags to data samples.

ROS 2's security features currently utilize only the first three.
This is due to the fact that neither **Logging** nor **Data Tagging**
are required in order to be compliant with the [DDS-Security spec][dds_security]
(see section 2.3), and thus not all DDS implementations support them.

### SROS 2 tools

Since the DDS-Security plugins require a set of security files per domain participant, these
need to be created beforehand in order to provide authentication, access control and encryption
to the ROS 2 elements of RMF. Domain participants usually map to a context within the
process in ROS 2, therefore each process will require a set of these files.

Since SROS 2 has no support for launch files yet, each binary needs to be launched separately
on its own terminal. Alternatively we recommend the creation of scripts to automate this process.
An example of this is the `tmux` script used in the [Office SROS 2 demo][https://github.com/open-rmf/rmf_demos/blob/main/docs/secure_office_world.md].

The `ros2 security` command is the way to access the SROS 2 set of tools to create and manage
your DDS-security artifacts. You can get a glimpse at its features by accessing the documentation
through the `-h` flag:

``` {.sourceCode .bash}
$ ros2 security -h
usage: ros2 security [-h] Call `ros2 security <command> -h` for more detailed usage. ...

Various security related sub-commands

optional arguments:
  -h, --help            show this help message and exit

Commands:
  create_key          Create key
  create_keystore     Create keystore
  create_permission   Create permission
  generate_artifacts  Generate keys and permission files from a list of identities and policy files
  generate_policy     Generate XML policy file from ROS graph data
  list_keys           List keys

  Call \`ros2 security <command> -h\` for more detailed usage.
```

#### SROS 2 environment variables

There are a few environment variables you should be aware of when using SROS 2:

- **ROS_SECURITY_ENABLE** is the SROS 2 enabler variable, it takes a boolean value
(true or false) and indicates if the security is enabled or not.
- **ROS_SECURITY_STRATEGY** can be set to `Enforce` or `Permissive`, with the first one it
will fail to run a participant if the security files are not found, whereas with the second one will
just run the participant in non secure mode if those files are not found.
- **ROS_SECURITY_KEYSTORE** should point to the root of the keystore directory tree. This will help `RCL`
find the location of the security artifacts to initialize the ROS 2 security environment.

#### SROS 2 security keystore

The keystore is the root directory where the DDS security artifacts are stored. `RCL` will use the
contents of this directory to provide the DDS security to the ROS 2 network. The
`ROS_SECURITY_KEYSTORE` environment variable should by convention point to this directory. In order
to initalize and populate `keystore_storage` directory files the following command can be used:

``` {.sourceCode .bash}
$ ros2 security create_keystore keystore_storage
creating keystore: keystore_storage
creating new CA key/cert pair
creating governance file: keystore_storage/enclaves/governance.xml
creating signed governance file: keystore_storage/enclaves/governance.p7s
```

After creating the keystore, its initial structure would look like this:

    keystore_storage
    ├── enclaves
    |   ├── governance.p7s
    |   └── governance.xml
    ├── private
    |   ├── ca.key.pem
    |   ├── identity_ca.key.pem
    |   └── permissions_ca.key.pem
    └── public
        ├── ca.key.pem
        ├── identity_ca.key.pem
        └── permissions_ca.key.pem

The `public` directory contains anything permissible as public, such as public certificates for
the identity or permissions Certificate Authorities (CA). As such, this can be given read access to all
executables. Note that in the default case, both `identity_ca` and `permissions_ca` point to the
same CA certificate.

The `private` directory contains anything permissible as private, such as private key material for
aforementioned certificate authorities. This directory should be removed before deploying the
keystore onto the target device/robot.

The `enclaves` directory contains the security artifacts associated with individual security enclaves.
SROS 2 introduces the concept of a security “enclave”,
where an “enclave” is a process or group of processes that will share the same identity and access
control rules. The enclaves folder may recursively nest sub-paths for organizing separate enclaves.

#### SROS 2 enclave keys

Once the `keystore` has been initialized you may wish to create the security keys for your
enclaves. This will populate the `enclaves` directory with the necessary keys and governance
files. As an example, in order to create the security files for our`/hospital/rviz` enclave the
following command would be issued:

``` {.sourceCode .bash}
$ ros2 security create_key keystore_storage /hospital/rviz
creating key for identity: '/hospital/rviz'
creating cert and key
creating permission
```

After this, they `keystore_storage` directory should contain the rviz enclave:

    keystore_storage
    ├── enclaves
    |   ├── governance.p7s
    |   ├── governance.xml
    │   └── hospital
    |       ├── rviz
    │       |   ├── cert.pem
    │       |   ├── key.pem
    │       |   ├── governance.p7s
    |       |   ├── identity_ca_cert.pem
    |       |   ├── permissions_ca.cert.pem
    |       |   ├── permissions.p7s
    |       |   └── permissions.xml
    ...     ...

Now there is an enclave containing the following files:

- **identity_ca.cert.pem**: The x.509 certificate of the CA trusted by the **Authentication** plugin
(the "Identity" CA).
- **cert.pem**: The x.509 certificate of this enclave instance (signed by the Identity CA).
- **key.pem**: The private key of this enclave instance.
- **permissions_ca.cert.pem**: The x.509 certificate of the CA trusted by the **Access control** plugin
(the "Permissions" CA).
- **governance.p7s**: The XML document that specifies to the **Access control** plugin how the domain
should be secured  (signed by the Permissions CA).
- **permissions.p7s**: The XML document that specifies the permissions of this particular enclave
instance to the **Access control** plugin (also signed by the Permissions CA).

#### SROS 2 access control

In order to provide access control the security permissions need to be added to the permissions files
of the enclave and signed by the CA. In order to do this a policy file following the
[SROS 2 policy schema][access_control] is needed.
This file specifies the permissions awarded to the enclave within the ROS 2 network.
To create and sign the permissions the `create_permission` option can be used:

``` {.sourceCode .bash}
$ ros2 security create_permission keystore_storage /hospital/rviz policy.xml
creating permission file for identity: '/hospital/rviz'
creating permission
```

After running this command, the `permissions.p7s` and `permissions.xml` files for the
`enclave` /hospital/rviz will contain the signed permissions specified in policy.xml.
We will have to specify this enclave through rosargs when starting our process:

``` {.sourceCode .bash}
$ ros2 run <package> <executable> --rosargs ---enclave /hospital/rviz
```

# SROS 2 automated generation

The process of generating keys and permissions can be sometimes tedious, so SROS 2 provides tools
to automate this process. An automated way to generate the policy is provided, it can be
triggered by running the following command:

``` {.sourceCode .bash}
$ ros2 security generate_policy policy.xml
```

This command will take the ROS graph at the point of running and generate the policy.xml file
that corresponds to it. Note that this, as it only uses the current ROS graph as a source of
information, might still miss policies for future publishers, subscribers, services or others.

The process and key and permissions generation can also be troublesome, SROS 2 provides a
command that you can use to generate all of them at once:

``` {.sourceCode .bash}
$ ros2 security generate_artifacts -k keystore_storage -p policy.xml
keystore_storage is not a valid keystore, creating new keystore
creating keystore: keystore_storage
creating new CA key/cert pair
creating governance file: keystore_storage/enclaves/governance.xml
creating signed governance file: keystore_storage/enclaves/governance.p7s
all done! enjoy your keystore in keystore_storage
cheers!
creating key for identity: '/hosptial/rviz'
creating cert and key
creating permission
creating permission file for identity: '/hosptical/rviz'
creating permission
...
```

Finally SROS 2 also provides a way to easily list the keys of a certain keystorage:

``` {.sourceCode .bash}
$ ros2 security list_keys keystore_storage
/hospital/building_map_server
/hopsital/building_systems_visualizer
/hospital/door_supervisor
/hospital/fleet_state_visualizer
/hosptial/loop_request_publisher
/hosptial/rviz2
...
```

## RMF Web Dashboard Security

[RMF Web] (https://github.com/open-rmf/rmf-web) is a web application that provides overall visualization and control over the
RMF system. It is served over TLS to ensure encryption, integrity and authentication of the
communication with the final user. The server uses [openid-connect (OIDC)][openid_connect] for
authentication, an open standard based on [oauth 2.0][oauth2] and [JOSE][jose]. Currently the
dashboard makes use of [Keycloack][keycloack], an open source implementation of OIDC. It provides
an user management system, which is used to create/delete users. Each user gets assigned a role
which is reflected on an id token generated on the user. This id token is signed securely
and sent to the api server which it can then look at the role of the user and act accordingly.
The api server runs a secured ROS 2 node per each role and provides access to them based on
the id token of each user.

[SROS]: https://design.ros2.org/articles/ros2_dds_security.html
[dds_security]: https://www.omg.org/spec/DDS-SECURITY/1.1/PDF
[dds]: https://www.omg.org/spec/DDS/1.4/PDF
[rmf_demos]: https://github.com/osrf/rmf_demos
[office_sros]: https://github.com/osrf/rmf_demos/blob/master/demos/sros2/office_deploy.bash
[fasdds]: https://github.com/eProsima/Fast-DDS
[cyclonedds]: https://github.com/ros2/rmw_cyclonedds
[enclaves]: https://design.ros2.org/articles/ros2_security_enclaves.html
[access_control]: https://design.ros2.org/articles/ros2_access_control_policies.html
[openid_connect]: https://openid.net/connect/
[oauth2]: https://oauth.net/2/
[jose]: https://jose.readthedocs.io/en/latest/
[keycloack]: https://www.keycloak.org
````

### data/source_texts/ref-762.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

````text
# Open-RMF API Server

This API server sets up the necessary endpoints with an Open-RMF deployment and enables the use of the web dashboard. The server comes with the capability of logging to databases, as well as handling authentication and permissions.

# Setup

If not already done so, [install dependencies](../../README.md#Install-dependencies), you can use
```bash
pnpm install -w --filter api-server...
```
to install dependencies for only this package.

# API

Check out the latest API definitions [here](https://open-rmf.github.io/rmf-web/docs/api-server), or visit `/docs` relative to your running server's url, e.g. `http://localhost:8000/docs`.

# Run the server

```bash
rmf_api_server
```

## Configuration

Config files are python modules that export a variable named `config`. See [default_config.py](api_server/default_config.py) for an example and list of the options available. All options are REQUIRED unless specified otherwise.

Configuration is read from the file specified in the env `RMF_API_SERVER_CONFIG`, if not provided, the default config is used.

e.g.
```bash
RMF_API_SERVER_CONFIG='my_config.py' rmf_api_server
```
To run the api-server with PostgreSQL, assuming it has been set up to listen on 127.0.0.1:5432 with user `postgres` and password `postgres`:
```
RMF_API_SERVER_CONFIG=api_server/psql_local_config.py rmf_api_server
```

## Supported databases

rmf-server uses [tortoise-orm](https://github.com/tortoise/tortoise-orm/) to perform database operations. Currently, the supported databases are

* PostgreSQL
* SQLite
* MySQL
* MariaDB

by default it uses a in-memory sqlite instance, to use other databases, install rmf-server with the relevalent extras

* PostgreSQL - postgres
* MySQL - mysql
* MariaDB - maria

.e.g.

```bash
pip3 install rmf-server[postgres]
```

Then in your config, set the `db_url` accordingly, the url should be in the form

```
DB_TYPE://USERNAME:PASSWORD@HOST:PORT/DB_NAME?PARAM1=value&PARAM2=value
```

for example, to connect to postgres

```
postgres://<user>:<password>@<host>/<database>
```

for more information, see https://tortoise-orm.readthedocs.io/en/latest/databases.html.

### PostgreSQL
If you would like to use PostgreSQL, you will also need to install and set it up. The defaults are for PostgreSQL to be listening on 127.0.0.1:5432.

#### Docker
We can use Docker to quickly bring up a PostgreSQL instance.

Install docker: `https://docs.docker.com/engine/install/ubuntu/`
Start a a database instance: `docker run -it --rm --name rmf-postgres --network=host -e POSTGRES_PASSWORD=postgres -d postgres`

To stop the instance: `docker kill rmf-postgres`

#### Bare Metal
Alternatively, we can install PostgreSQL 'bare metal'.
```
apt install postgresql postgresql-contrib -y
# Set a default password
sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'postgres';"

sudo systemctl restart postgresql
# interactive prompt
sudo -i -u postgres
```
To manually reset the database:
```
sudo -u postgres bash -c "dropdb postgres; createdb postgres"
```

## Running behind a proxy

When running behind a reverse proxy like nginx, you need to set the `public_url` option to the url where rmf-server is served on. The reverse proxy also MUST strip the prefix.

For example, if rmf-server is served on https://example.com/rmf/api/v1, `public_url` must be set to `https://example.com/rmf/api/v1` and your reverse proxy must be configured to strip the prefix such that it forwards requests from `/rmf/api/v1/something` to `/something`.

## Running with RMF simulations

When running with rmf simulations, you need to set the env `RMF_SERVER_USE_SIM_TIME=true`. This is needed to ensure that times from the client are correctly converted to RMF's simulation time.

# Authentication and Authorization

## OpenID Connect

rmf-server does not manage user identities and access levels by itself, it uses an OpenID Connect compatible identity provider to perform authentication. Authorization however, is performed in-app by rmf-server.

### Access Token Format

OpenID Connect does not define the format of the access token, the canonical way for a resource server to validate an access token is to use the token introspection endpoint of the authentication server. In order to not have to connect to the identity provider for every request, rmf-server assumes the convention that the access token is a JWT that can be verified independently. Most modern identity providers like keycloak and auth0 follows this convention.

### Access Token Claims

The access token must include the `preferred_username` claim. It will be used to determine an user's authorization levels.

If your identity provider strips standard OIDC claims (such as `preferred_username`) from access tokens issued via the OAuth 2.0 `client_credentials` (M2M) flow and requires custom claims to use a collision-resistant namespaced name, set the optional `preferred_username_claim_namespace` config value to the namespace prefix used by your provider. The authenticator will then check `f"{namespace}preferred_username"` as a fallback when the bare `preferred_username` claim is absent.

This pattern aligns with [RFC 9068 §2.2.2](https://www.rfc-editor.org/rfc/rfc9068.html#section-2.2.2) (which requires that arbitrary attributes in JWT access tokens have "collision resistant" names) and [RFC 7519 §4.2](https://www.rfc-editor.org/rfc/rfc7519.html#section-4.2) (which defines "Collision-Resistant Name" via Public Claim Names). [Auth0 enforces this policy explicitly](https://auth0.com/docs/secure/tokens/json-web-tokens/create-namespaced-custom-claims) for access tokens with a custom API audience — non-namespaced custom claims on standard OIDC names are silently dropped. Operators on other providers with comparable collision-avoidance policies may also benefit; leaving the value unset preserves the current behavior.

## Roles, Actions and Authorization Group

An user's permission to perform certain actions on a protected resource is determined by 3 values, role, action, and authorization group of the resource. A resource belongs to one authorization group and an user can belong to multiple roles. An user has access to perform an action on a resource if any of their roles has permission to perform the action on the authorization group which the resource belongs to. An admin always have permission to perform any action on any group.

For example, given the following permissions and users

Permissions:
| Role | Authz Group | Action |
| --- | --- | --- |
| role1 | group1 | task_submit |
| role2 | group2 | task_submit |
| role3 | group3 | task_submit |
| role4 | group1 | task_submit |
| role4 | group3 | task_submit |

Users:
| User | Roles | Is Admin |
| --- | --- | --- |
| user1 | role1 | false |
| user2 | role2, role3 | false |
| user3 | role4 | false |
| user4 | | true

`user1` will be able to submit a task that belongs to authorization group `group1`. `user2` can submit tasks belonging to `group2` and `group3`. `user3` can submit tasks in group `group1` and `group3`. `user4`, being an admin can submit tasks in any group.

The authorization group of a resource is determined automatically based on different factors according to the resource type. For example, a task's authorization group may be determined by the region where it takes place.

## Synchronization (or lack of) of User Data

rmf-server maintains its own database of users, roles and permissions. In order to keep compatibility with as many identitiy provider as possible and amount of code small, this database is never synchronized with the identity provider's database. Instead, rmf-server takes the following approach to keep things working even without a synchronized database.

* When an user first access any of the protected api, a new rmf-server user is automatically created, the  user will have no roles and no privileges.
  * rmf-server checks if the token is valid before creating the user. If it is valid, the user must exist in the identity provider.
* An admin can use the admin endpoints to perform various user management like
  * Create users
  * Create roles
  * Add/remove permissions to roles
  * Add/remove roles to users
* The admin endpoints only work on rmf-server's database and does not require delegation of any functions to the identity provider, as a result there are some cavaets
  * There is no endpoints to manage an user's authentication like reset user password, enable/disable users etc.
  * Endpoints that list/search users only includes users that is already added on to rmf-server.
* If an admin wishes to manage authorization for an user that exists in the identity provider, but not in rmf-server, they need to use the create user endpoint to create a new user with the same username.
* Deleting an user from rmf-server does not prevent them from accessing "semi-protected" apis (apis that require login but does not require any permissions). It also does not prevent them from logging into a frontend that connects to rmf-server (e.g. rmf dashboard).
  * This is because it does not delete the user from the identity provider and the next time they access any protected api, a new user will be automatically created.
  * Fully deleting an user so that they can no longer login should be done on the identity provider. There is no endpoint in rmf-server to forward deletion of an user to the identity provider because such behaviour may be unintuitive, undesirable and require specialized code paths for every provider.
* If the user is deleted from the identity provider, it will still exist in rmf-server.
  * This is harmless as the user will not be able to authenticate with the identity provider and get a valid token, so a "zombie" user will not be able to access any protected api.
* Since a new user is created with minimal privileges, and an admin is required to give users privileges (including the admin privilege), there is a problem.
  * This is worked around by adding a config to automatically make an user an admin on startup. Note that since there is no synchronization between the identity provider, there is no guarantee that such an user actually exists.

## TODO

A resource's authorizaion group is determined by it's contents. Exactly how they are determined for each type of resource is still either undecided or lacking information from RMF to be implemented, so currently every resource is put into a default empty group of `` (empty string).

## Database Migration

[`aerich`](https://github.com/tortoise/aerich) is a database migration tool for TortoiseORM. `aerich` requires a configuration file for initialization before doing any mutations, which can be found in `api_server.__main__.TORTOISE_ORM`.

Install `aerich`

```bash
pip3 install aerich
```

This migration example will be for PostgreSQL. First, setup `rmf-web` following [instructions](../../README.md). Then, run the `api-server` with `psql`,

```bash
# source RMF
cd ~/rmf-web/packages/api-server
pnpm run start:psql
```

In another terminal, activate the virtual environment manually and initialize `aerich`,

```bash
cd ~/rmf-web
source .venv/bin/activate
cd ~/rmf-web/packages/api-server

# First export the RMF_API_SERVER_CONFIG variable
export RMF_API_SERVER_CONFIG=psql_local_config.py

# Init aerich and save migration workspace to /tmp
aerich init -t api_server.__main__.TORTOISE_ORM --location /tmp/migrations
aerich init-db
```

You can check the current schema of a table. For example, using the `taskstate` table,

```bash
sudo -u postgres bash -c "psql -c '\d+ taskstate;'"
```

Now, modify the `TaskState` class in the `api_server/models/tortoise_models/tasks.py` to add a new field:

```python
new_field = fields.CharField(255)
```

Don't forget to make necessary changes to `api_server/repositories/tasks.py` too, to allow the dashboard to use the newly added fields.

Now attempt a migration, and allow `aerich` to find the changes required,

```bash
aerich migrate
# aerich will generate the migration file with the version
# check file at /tmp/migration/models/
```

Perform database upgrade,

```bash
aerich upgrade
```

Now, inspecting the database schema, you will find "new_field" available in the schema

```bash
sudo -u postgres bash -c "psql -c '\d+ taskstate;'"
```

Restart the `api-server` and the changes to the databse should be reflected.

## Running tests

### Running unit tests

```bash
pnpm test
```

By default in-memory sqlite database is used for testing, to test on another database, set the `RMF_API_SERVER_TEST_DB_URL` environment variable.

```bash
RMF_API_SERVER_TEST_DB_URL=<db_url> pnpm test
```

### Collecting code coverage

```bash
pnpm run test:cov
```

Generate coverage report
```bash
pnpm run test:report
```

## Live reload

```bash
uvicorn --reload api_server.app:app
```
````

### docs/categories/platform-architecture-and-infrastructure/index.md

```markdown
---
title: "K. 플랫폼 아키텍처·인프라"
type: category
status: seed
created: 2026-09-28
updated: 2026-09-28
version: 1
---

[홈](../../index.md) › K. 플랫폼 아키텍처·인프라

# K. 플랫폼 아키텍처·인프라

## 핵심 질문

플랫폼을 어디에 어떻게 두어야 끊김·확장·다현장 조건에서도 계속 동작하는가? [분류원문]

## 개요

플랫폼의 구조, 클라우드·현장 서버·로봇의 역할 분담, 네트워크·가용성·다현장, 데이터·관측성·배포·비용. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **41. 플랫폼 아키텍처·외부 API** | 기준 아키텍처, 클라우드·현장 서버·로봇 역할 분담, 외부 API·SDK | 어떤 판단을 클라우드·현장 서버·로봇 가운데 어디에서 하고, 외부에 무엇을 열어 줄 것인가? | [41. 플랫폼 아키텍처·외부 API](platform-architecture-and-external-api.md) | published |
| **42. 분산 시스템·통신·컴퓨팅 구조** | 현장 네트워크, 연결이 끊겨도 계속 운영, 다현장 구조, 확장성 | 인터넷이 끊겨도 현장에서 어디까지 계속 운영할 수 있을까? | [42. 분산 시스템·통신·컴퓨팅 구조](distributed-systems-communication-and-computing.md) | published |
| **43. 데이터·관측성·배포** | 데이터 수집·보존, 플랫폼 관측성, 배포 자동화, 운영 비용 | 플랫폼 자체의 상태·데이터·배포·비용을 어떻게 관리할 것인가? | [43. 데이터·관측성·배포](data-observability-and-deployment.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

플랫폼 구조는 현장의 네트워크 조건을 전제로 정해야 한다. **연결이 끊겼을 때 현장에서 계속할 수 있는 범위**가 구조 선택의 기준이 된다. [분류원문]

## 다른 대분류와의 연결

아직 작성되지 않음(에이전트가 채운다).

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 48건이다(논문 12건 · 기사·보고서 4건 · 업체 발표 9건 · 표준·오픈소스·기관 자료 23건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-1043](../../references/ref-1043.md) — Bruno, L. D. M., Sim, J., & Hagiwara, Y. (arXiv), Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots (발행 2026-09)
- [ref-1033](../../references/ref-1033.md) — Yu, J., Lee, S., Choi, Y., & Park, K.-J. (arXiv), ros2probe: Non-intrusive, Kernel-selective Observability for Robot Operating System 2 Middleware (발행 2026-06)
- [ref-943](../../references/ref-943.md) — Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments (발행 2026-03-31)
- [ref-308](../../references/ref-308.md) — Brorsson, E. 외, Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives (발행 2025-12)
- [ref-1039](../../references/ref-1039.md) — Zhang, J., Yu, X., & Westerlund, T. (Sensors 25(16):5067), Enhancing the Resilience of ROS 2-Based Multi-Robot Systems with Kubernetes: A Case Study on UWB-Based Relative Positioning (발행 2025-08-14)
- [ref-1031](../../references/ref-1031.md) — Chen, K., Hari, K., Chung, T. 외 (IROS 2024, arXiv), FogROS2-FT: Fault Tolerant Cloud Robotics (발행 2024-12)
- [ref-1032](../../references/ref-1032.md) — Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L, arXiv), ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2 (발행 2022-07)
- [ref-304](../../references/ref-304.md) — Ichnowski, J., Chen, K. 외(UC Berkeley AUTOLAB), FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2 (발행 2022-05)
- [ref-311](../../references/ref-311.md) — ETRI Journal 게재 논문(Jun 외, 한국전자통신연구원 발행), Ultra-low-latency services in 5G systems: A perspective from 3GPP standards (발행 2020)
- [ref-1027](../../references/ref-1027.md) — Singhal, A., Kejriwal, N., Pallav, P., Choudhury, S., Sinha, R., & Kumar, S. (arXiv), Managing a Fleet of Autonomous Mobile Robots (AMR) using Cloud Robotics Platform (발행 2017-06)
- 그 밖에 2건

**기사·보고서**

- [ref-1026](../../references/ref-1026.md) — 뉴스핌, 카카오모빌리티, 로봇-인프라-사용자 연결 '플랫폼 생태계' 구축한다 (발행 2026-05-13)
- [ref-870](../../references/ref-870.md) — 로봇신문, [기업 최전선을 가다-클로봇] 로봇 소프트웨어로 쓰는 ‘피지컬 AI’ 시대의 서막 (발행 2025-11-09)
- [ref-309](../../references/ref-309.md) — FreightWaves, Warehouses face $100K-hour downtime risk as cloud outages mount (발행 미확인)
- [ref-1041](../../references/ref-1041.md) — FinOps Foundation, FinOps Phases (발행 미확인)

**업체 발표**

- [ref-301](../../references/ref-301.md) — Microsoft, Operate Azure IoT Edge devices offline (발행 2026-03-02)
- [ref-1044](../../references/ref-1044.md) — Ocado Group, Ocado's digital twins and simulations: driving efficiencies and innovation at scale (발행 2025-06-04)
- [ref-227](../../references/ref-227.md) — Mobile Industrial Robots(MiR), MiR Fleet Enterprise Documentation Version 1.2 (en) — 유통사(jk.de) 게재본 (발행 2025-01)
- [ref-307](../../references/ref-307.md) — CJ대한통운, CJ대한통운, 물류센터 최초 5G 개통 … 속도 1000배 빨라진다 (발행 2023-04)
- [ref-1035](../../references/ref-1035.md) — Foxglove, MCAP as the ROS 2 Default Bag Format (발행 2022-12-22)
- [ref-774](../../references/ref-774.md) — Mobile Industrial Robots(MiR), MiR Fleet (발행 미확인)
- [ref-1030](../../references/ref-1030.md) — Locus Robotics, Seamless Integrations with LocusOne Robotics (발행 미확인)
- [ref-1029](../../references/ref-1029.md) — InOrbit, Contents — InOrbit Developer Portal (발행 미확인)
- [ref-1023](../../references/ref-1023.md) — NAVER Corp., 로보틱스 l NAVER Corp. (발행 미확인)

**표준·오픈소스·기관 자료**

- [ref-1042](../../references/ref-1042.md) — FinOps Foundation, Introducing FOCUS 1.2: SaaS/PaaS Support, Invoice Reconciliation, and more (발행 2025-06-03)
- [ref-1034](../../references/ref-1034.md) — Open Robotics (ROS 2 Documentation), Iron Irwini (iron) (발행 2023-05-23)
- [ref-1025](../../references/ref-1025.md) — OpenAPI Initiative, OpenAPI Specification v3.1.0 (발행 2021-02-15)
- [ref-306](../../references/ref-306.md) — OASIS, MQTT Version 5.0 (발행 2019-03)
- [ref-303](../../references/ref-303.md) — NIST, NIST Special Publication (SP) 500-325, Fog Computing Conceptual Model (발행 2018-03)
- [ref-937](../../references/ref-937.md) — Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART), ROMI-H \| Changi General Hospital (발행 미확인)
- [ref-766](../../references/ref-766.md) — 국가법령정보센터(개인정보보호위원회 고시), 개인정보의 안전성 확보조치 기준 (발행 미확인)
- [ref-762](../../references/ref-762.md) — Open Robotics (open-rmf), rmf-web — packages/api-server/README.md (발행 미확인)
- [ref-302](../../references/ref-302.md) — Open Robotics (open-rmf), rmf-web — README (발행 미확인)
- [ref-300](../../references/ref-300.md) — KubeEdge (CNCF, kubeedge GitHub), KubeEdge — README (발행 미확인)
- 그 밖에 13건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-30 · 갱신 · [43. 데이터·관측성·배포](data-observability-and-deployment.md) — 섹션 3~11 신규 작성(seed → draft): 기록 형식·관측성·배포·비용 관리 접근법, 병원·물류창고 적용 사례, 책임 경계, 연결 영역 17개, 열린 질문 6건 (실행 2026-09-30-06)
- 2026-09-30 · 생성 · [43. 데이터·관측성·배포 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area43-s6.md) — 자동 분리: 43. 데이터·관측성·배포 의 "6. 대표 접근법과 기술" 절(2,750자)을 옮겼다 (실행 2026-09-30-06)
- 2026-09-30 · 생성 · [43. 데이터·관측성·배포 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area43-s10.md) — 자동 분리: 43. 데이터·관측성·배포 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,115자)을 옮겼다 (실행 2026-09-30-06)
- 2026-09-30 · 생성 · [43. 데이터·관측성·배포 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area43-s7.md) — 자동 분리: 43. 데이터·관측성·배포 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,055자)을 옮겼다 (실행 2026-09-30-06)
- 2026-09-30 · 생성 · [43. 데이터·관측성·배포 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area43-s4.md) — 자동 분리: 43. 데이터·관측성·배포 의 "4. 핵심 개념과 용어" 절(975자)을 옮겼다 (실행 2026-09-30-06)
<!-- auto:category-recent:end -->
```

### docs/categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md

```markdown
---
title: "41. 플랫폼 아키텍처·외부 API"
type: area
category: "K. 플랫폼 아키텍처·인프라"
area_no: 41
related_areas: [1, 20, 21, 22, 23, 32, 37, 42, 43, 51, 52, 61, 62, 63, 67]
tags: [클라우드 로보틱스, 현장 클라우드, 외부 API, OpenAPI, AsyncAPI, 플릿 어댑터]
status: published
confidence: low
created: 2026-09-28
updated: 2026-09-30
sources: [ref-004, ref-031, ref-762, ref-304, ref-1023, ref-937, ref-1024, ref-1025, ref-1026, ref-870, ref-308, ref-1027, ref-1028, ref-1029, ref-774, ref-1030, ref-1031]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [K. 플랫폼 아키텍처·인프라](index.md) › 41. 플랫폼 아키텍처·외부 API

# 41. 플랫폼 아키텍처·외부 API

!!! info "소속 대분류"
    [K. 플랫폼 아키텍처·인프라](index.md) — 핵심 질문:
    플랫폼을 어디에 어떻게 두어야 끊김·확장·다현장 조건에서도 계속 동작하는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: low · 페이지 버전: 2 · 마지막 갱신: 2026-09-30 · 마지막 실행: 2026-09-30
<!-- auto:page-status:end -->

## 1. 한 줄 정의

기준 아키텍처, 클라우드·현장 서버·로봇 역할 분담, 외부 API·SDK [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **클라우드·현장 서버·로봇 역할 분담**: 어떤 판단과 데이터를 클라우드·현장 서버·로봇 가운데 어디에 둘지 정한다
- **플랫폼 기준 아키텍처**: 서비스 분리, 이벤트 구조, 제조사 중립성을 갖춘 플랫폼 구조를 정한다
- **외부 API·SDK 제공**: 다른 시스템과 개발자가 플랫폼을 부를 수 있는 API·웹훅·SDK·문서를 제공한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 11번 영역 ‘분산 시스템·통신·컴퓨팅 구조’에서 왔다. 그 본문은 [42. 분산 시스템·통신·컴퓨팅 구조](distributed-systems-communication-and-computing.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

어떤 판단을 클라우드·현장 서버·로봇 가운데 어디에서 하고, 외부에 무엇을 열어 줄 것인가? [분류원문]

## 3. 왜 중요한가

이종 로봇을 묶는 플랫폼의 외부 API 는 업무 시스템과 개발자가 로봇 운영을 만나는 단일 접점이 되고, 판단을 어디에 두느냐가 운영 연속성을 좌우하므로 이 영역이 중요하다. [추정][^ref-031][^ref-774][^ref-1030][^ref-1031]

자세한 내용은 주제 페이지 [41. 플랫폼 아키텍처·외부 API — 왜 중요한가](../../topics/2026/2026-09-30-area41-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 절은 판단 배치와 외부 API 를 이해하는 데 필요한 개념인 클라우드 로보틱스·계산 오프로딩·현장 클라우드·플릿 어댑터와 제어 수준·OpenAPI·AsyncAPI·웹훅·브레인리스 로봇을 정리한다.

자세한 내용은 주제 페이지 [41. 플랫폼 아키텍처·외부 API — 핵심 개념과 용어](../../topics/2026/2026-09-30-area41-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이 영역의 적용 사례는 플랫폼을 어디에 두고 외부에 무엇을 여는지가 드러난 병원·제조 공장·물류창고·기타 현장의 네 건이다. 상업 시설·가정·실외 사례는 이번 조사에서 찾지 못했고, 사례마다 근거가 없는 칸은 미확인으로 둔다.

### 병원

**현장 유형:** 병원

**사례:** 공공 의료기관의 로봇 시스템을 하나의 미들웨어로 묶는 구조(RoMi-H)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 미확인 |
| 수행 자원 | 기계 영역(하드웨어 추상화)·제어 영역(항법·위치 추정)·중앙 영역(플릿 관리, 로봇–로봇·로봇–기반 시설 통신)·통합 영역(모바일 앱·웹 앱·정보통신기술(ICT) 시스템용 API)의 네 영역이 역할을 나눈다. [사실][^ref-937] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

이 사례는 특정 병원의 배치 결과가 아니라 싱가포르 창이종합병원 CHART 가 공공 의료기관용으로 내놓은 미들웨어 구조다. [RoMi-H](../../glossary/robotic-middleware-for-healthcare.md)(Robotic Middleware for Healthcare)는 OMG DDS(Data Distribution Service)를 쓰며, 2018-07 개발이 발표되고 2019-10-31 ROSCon 2019 에서 공식 출범했다. [사실][^ref-937] 외부 시스템용 API 를 통합 영역으로 따로 두는 점이 이 영역의 "외부에 무엇을 열 것인가"와 이어진다(구축자 의견). [의견][^ref-937]

### 제조 공장

**현장 유형:** 제조 공장

**사례:** 대형 상용차 제조 현장의 사내 물류 이동 로봇 운영(RAIL 기준 아키텍처)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 사내 물류(internal logistics) 운반. 구체적 물품은 미확인. [사실][^ref-308] |
| 수행 자원 | 설비에 단 외부 센서·계산 자원(기반 시설), 현장 클라우드, 로봇 온보드 자율의 세 층이 나눠 맡는다. [사실][^ref-308] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인(초록은 실배치와 사용자 경험 평가를 보고하나 처리량·시간·비용 수치는 확인하지 못함) |

Brorsson 외는 이 기준 아키텍처를 대형 상용차 제조 현장 실배치와 사용자 경험 평가로 보였다(2025-12, 초록 기준). [사실][^ref-308] 로봇 온보드 지능만이 아니라 설비 쪽 센서와 현장 계산 자원까지 판단 배치의 선택지가 된다는 점을 보여 준다. [추정][^ref-308]

### 물류창고

**현장 유형:** 물류창고

**사례:** 물류창고 피킹 — WMS 주문을 로봇 작업으로 바꾸고 결과를 되돌리기(Locus Robotics LocusONE)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 창고 관리 시스템(Warehouse Management System, WMS)에서 주문을 API 로 받는다. [추정] 벤더 주장[^ref-1030] |
| 작업 대상 | WMS 주문 정보와 피킹할 품목. [추정] 벤더 주장[^ref-1030] |
| 수행 자원 | LocusONE 플랫폼이 주문을 피킹 효율 기준으로 최적화해 로봇 작업으로 내린다. [추정] 벤더 주장[^ref-1030] |
| 제약 | 기존 인프라와 분리된 전용 WiFi 망을 설치·유지한다. [추정] 벤더 주장[^ref-1030] |
| 완료·인계 | 피킹 완료 확인을 WMS 로 즉시 회신한다. [추정] 벤더 주장[^ref-1030] |
| 예외·성과 | 시간당 처리 단위(UPH)·시간당 처리 라인(LPH)·로봇·작업자 생산성 데이터를 제공한다. 실패 시 복구 주체는 미확인. [추정] 벤더 주장[^ref-1030] |

흐름 단계로는 피킹에 해당한다. 외부 API 가 작업의 시작(주문 수신)과 끝(확인 회신)을 모두 맡는 구조다. [추정] 벤더 주장[^ref-1030] 플랫폼을 클라우드와 현장 가운데 어디에 두는지는 자료에 나오지 않는다(미확인). 주문 최적화 판단 자체는 WMS·로봇 공급사 쪽의 일이고, ROP 는 연동 인터페이스만 다룬다(9절). [추정][^ref-1030]

### 기타

**현장 유형:** 기타

**사례:** 기업 사옥에서 클라우드로 로봇 운영(네이버 제2사옥 1784 의 ARC)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 미확인 |
| 수행 자원 | 클라우드의 ARC brain(이동 계획·위치 추정·작업 수행·기반 시설 연동), ARC eye(디지털 트윈 데이터와 측위 AI 로 로봇 위치 결정), ARC mind(웹 개발자용 웹 기반 OS)가 나눠 맡고, 로봇은 연산·판단을 싣지 않는다. [추정] 벤더 주장[^ref-1023] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

네이버는 1784 에서 100여 대 로봇을 클라우드로 제어한다고 밝힌다. [추정] 벤더 주장[^ref-1023] 위치 추정·이동 계획까지 클라우드에 두는 이 설계는 분류 원문 19장의 로봇 자체 지능 경계를 제품 전략으로 옮긴 사례로만 볼 수 있으며, ROP 직접 범위의 근거로 쓰지 않는다(9절). [추정][^ref-1023] ARC mind 는 웹 개발자가 로봇 서비스를 만들게 한다는 점에서 개발자에게 여는 인터페이스의 예다. [추정] 벤더 주장[^ref-1023]

## 6. 대표 접근법과 기술

이 영역의 대표 접근법은 판단을 로봇·현장 서버·클라우드에 나눠 두는 혼합 배치, 계산 오프로딩과 다중 클라우드 장애 대응, 제조사 중립 어댑터 계층, 그리고 REST·이벤트·웹훅·SDK 로 외부 API 를 여는 방식이다. [추정][^ref-1027][^ref-308][^ref-304][^ref-1031][^ref-004][^ref-1025][^ref-1024]

자세한 내용은 주제 페이지 [41. 플랫폼 아키텍처·외부 API — 대표 접근법과 기술](../../topics/2026/2026-09-30-area41-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역의 표준·오픈소스는 제조사 중립 플랫폼 구조를 보여 주는 Open-RMF·RoMi-H, 로봇–관제 인터페이스인 VDA 5050, 외부 API 를 기계가 읽게 기술하는 OpenAPI·AsyncAPI, 판단 배치 연구 플랫폼인 FogROS2 계열로 나뉜다(구축자 의견). [의견][^ref-004][^ref-937][^ref-031][^ref-1025][^ref-1024][^ref-304]

자세한 내용은 주제 페이지 [41. 플랫폼 아키텍처·외부 API — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area41-s7.md)에 있다.

## 8. 대표 연구와 자료

판단 배치와 장애 대응의 근거는 클라우드 오프로딩 두 연구와 플릿 관리 구조 두 연구이며, 모두 논문 초록 기준이다. [사실][^ref-304][^ref-1031][^ref-1027][^ref-308]

자세한 내용은 주제 페이지 [41. 플랫폼 아키텍처·외부 API — 대표 연구와 자료](../../topics/2026/2026-09-30-area41-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

이 영역에서 ROP 가 직접 맡을 범위는 제조사 어댑터 계층을 둔 제조사 중립 기준 아키텍처, 작업 요청·작업 상태·플릿 상태의 기계가독 스키마, REST·이벤트 API 와 웹훅·SDK 의 명세와 버전 표기, API 호출의 인증·권한, 그리고 판단·데이터를 로봇·현장 서버·클라우드 가운데 어디에 둘지 정하는 배치 정책으로 보인다. [추정][^ref-004][^ref-937][^ref-1028][^ref-031][^ref-1025][^ref-1024][^ref-762]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 제조사 어댑터로 로봇·제조사 관제의 기능·상태를 주고받는 인터페이스와 판단 배치 정책. [추정][^ref-004] | 연계 대상: 국지 주행·장애물 회피·SLAM 같은 로봇 자체 지능은 로봇 제조사가 맡는다. FogROS2 같은 오프로딩은 로봇 내부 기능의 실행 위치 선택이다. [추정][^ref-304][^ref-1027] |
| 상위 업무 시스템 | 업무 시스템이 부르는 외부 API(요청 수신·결과 회신)와 그 인증·권한. [추정][^ref-762][^ref-1030] | 연계 대상: 주문·재고 같은 업무 판단은 WMS·ERP 가 맡는다. [추정][^ref-1030] |

클라우드 제공자 인프라는 외부 연계 대상이고, 현장 네트워크 설계는 ROP 의 다른 세부영역인 [42. 분산 시스템·통신·컴퓨팅 구조](distributed-systems-communication-and-computing.md)에서 다룬다. [추정][^ref-1031][^ref-1030]

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

네이버가 밝힌 ARC 처럼 위치 추정·이동 계획까지 클라우드에 두는 설계는 위 경계를 제품 전략으로 옮긴 사례이며, 이종 제조사를 연결하는 ROP 의 직접 범위로 보지 않는다. [추정] 벤더 주장[^ref-1023] 경계 전체는 [범위 경계](../../about/scope-boundary.md) 페이지에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 같은 K. 플랫폼 아키텍처·인프라의 네트워크·데이터 영역, F. 연동의 네 영역, 보안·관제·복구 영역, 그리고 적용 현장 영역과 이어진다. [추정][^ref-1031][^ref-004]

자세한 내용은 주제 페이지 [41. 플랫폼 아키텍처·외부 API — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area41-s10.md)에 있다.

## 11. 열린 질문

판단 배치의 단절 대응, 외부 API 의 수명주기와 전달 보장, 국내 표준 여부가 아직 확인되지 않았다.

자세한 내용은 주제 페이지 [41. 플랫폼 아키텍처·외부 API — 열린 질문](../../topics/2026/2026-09-30-area41-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [41. 플랫폼 아키텍처·외부 API](platform-architecture-and-external-api.md) — 섹션 3~11 신규 작성(seed → draft): 판단 배치 혼합 구조, 외부 API 조합, 병원·제조 공장·물류창고·기타 적용 사례 4건, 책임 경계, 열린 질문 4건. 1차 조건부 승인 수정 17건과 2차 수정 5건(3절 일반화 2건 좁힘, 4절 도입 단락, [의견] 주체 표시, 약어 풀이) 이행 (실행 2026-09-30-05)
- 2026-09-30 · 생성 · [41. 플랫폼 아키텍처·외부 API — 대표 접근법과 기술](../../topics/2026/2026-09-30-area41-s6.md) — 자동 분리: 41. 플랫폼 아키텍처·외부 API 의 "6. 대표 접근법과 기술" 절(3,254자)을 옮겼다 (실행 2026-09-30-05)
- 2026-09-30 · 생성 · [41. 플랫폼 아키텍처·외부 API — 핵심 개념과 용어](../../topics/2026/2026-09-30-area41-s4.md) — 자동 분리: 41. 플랫폼 아키텍처·외부 API 의 "4. 핵심 개념과 용어" 절(1,132자)을 옮겼다 (실행 2026-09-30-05)
- 2026-09-30 · 생성 · [41. 플랫폼 아키텍처·외부 API — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area41-s7.md) — 자동 분리: 41. 플랫폼 아키텍처·외부 API 의 "7. 관련 표준·프레임워크·오픈소스" 절(962자)을 옮겼다 (실행 2026-09-30-05)
- 2026-09-30 · 생성 · [41. 플랫폼 아키텍처·외부 API — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area41-s10.md) — 자동 분리: 41. 플랫폼 아키텍처·외부 API 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(879자)을 옮겼다 (실행 2026-09-30-05)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-30
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-30
[^ref-762]: Open Robotics (open-rmf), rmf-web/packages/api-server/README.md, 미확인, https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md, 접근일 2026-09-30
[^ref-304]: Ichnowski, J., Chen, K., Dharmarajan, K. 외 (arXiv), FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2, 2022-05, https://arxiv.org/abs/2205.09778, 접근일 2026-09-30
[^ref-1023]: NAVER Corp., 로보틱스 l NAVER Corp., 미확인, https://www.navercorp.com/tech/robotics, 접근일 2026-09-30
[^ref-937]: Changi General Hospital — CHART (Centre for Healthcare Assistive & Robotics Technology), ROMI-H, 미확인, https://www.cgh.com.sg/chart/projects/romi-h, 접근일 2026-09-30
[^ref-1024]: AsyncAPI Initiative, AsyncAPI Specification 3.1.0, 미확인, https://www.asyncapi.com/docs/reference/specification/v3.1.0, 접근일 2026-09-30
[^ref-1025]: OpenAPI Initiative, OpenAPI Specification v3.1.0, 2021-02-15, https://spec.openapis.org/oas/v3.1.0, 접근일 2026-09-30
[^ref-308]: Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv), Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives, 2025-12, https://arxiv.org/abs/2512.15215, 접근일 2026-09-30
[^ref-1027]: Singhal, A., Kejriwal, N., Pallav, P., Choudhury, S., Sinha, R., & Kumar, S. (arXiv), Managing a Fleet of Autonomous Mobile Robots (AMR) using Cloud Robotics Platform, 2017-06, https://arxiv.org/abs/1706.08931, 접근일 2026-09-30
[^ref-1028]: Open Robotics (open-rmf), rmf_api_msgs — README, 미확인, https://github.com/open-rmf/rmf_api_msgs, 접근일 2026-09-30
[^ref-774]: Mobile Industrial Robots (MiR), MiR Fleet, 미확인, https://mobile-industrial-robots.com/products/software/mir-fleet, 접근일 2026-09-30
[^ref-1030]: Locus Robotics, Seamless Integrations with LocusOne Robotics, 미확인, https://locusrobotics.com/locusone/automated-warehouse-software/integrations, 접근일 2026-09-30
[^ref-1031]: Chen, K., Hari, K., Chung, T. 외 (IROS 2024, arXiv), FogROS2-FT: Fault Tolerant Cloud Robotics, 2024-12, https://arxiv.org/abs/2412.05408, 접근일 2026-09-30
```

### docs/categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md

```markdown
---
title: "42. 분산 시스템·통신·컴퓨팅 구조"
type: area
category: "K. 플랫폼 아키텍처·인프라"
area_no: 42
related_areas: [18, 20, 23, 29, 32, 35, 47, 51]
tags: [VDA 5050, MQTT, Zenoh, 엣지 컴퓨팅, 포그 컴퓨팅, CAP 정리]
status: published
confidence: low
created: 2026-09-24
updated: 2026-09-25
sources: [ref-031, ref-256, ref-300, ref-301, ref-304, ref-306, ref-307, ref-308, ref-309, ref-310, ref-311]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [K. 플랫폼 아키텍처·인프라](index.md) › 42. 분산 시스템·통신·컴퓨팅 구조

# 42. 분산 시스템·통신·컴퓨팅 구조

!!! info "소속 대분류"
    [K. 플랫폼 아키텍처·인프라](index.md) — 핵심 질문:
    플랫폼을 어디에 어떻게 두어야 끊김·확장·다현장 조건에서도 계속 동작하는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: low · 페이지 버전: 2 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
<!-- auto:page-status:end -->

## 1. 한 줄 정의

현장 네트워크, 연결이 끊겨도 계속 운영, 다현장 구조, 확장성 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **현장 네트워크**: 와이파이 로밍·5G·사설망, 지연·대역폭·음영 구역을 설계하고 점검한다
- **연결이 끊겨도 계속 운영**: 인터넷이나 서버가 끊겨도 현장에서 어디까지 계속 운영할지 정하고 구현한다
- **다현장 운영 구조**: 여러 현장을 한 플랫폼에서 나누어 운영하는 구조를 만든다
- **확장성·성능**: 로봇과 작업 수가 늘어도 처리 성능을 유지한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [41. 플랫폼 아키텍처·외부 API](platform-architecture-and-external-api.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 11번 영역 ‘분산 시스템·통신·컴퓨팅 구조’(옛 대분류 C. 연결·실행 기반)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 클라우드·현장 서버·로봇의 역할 분담, 네트워크 지연, 서비스 가용성, 데이터 전송 품질, 다거점 운영 [옛 분류원문]

> 옛 질문: 인터넷이 끊겨도 현장에서 어디까지 계속 운영할 수 있을까? [옛 분류원문]

## 2. 핵심 질문

인터넷이 끊겨도 현장에서 어디까지 계속 운영할 수 있을까? [분류원문]

## 3. 왜 중요한가

연결이 끊기면 자동화 자산이 멈추는 일이 창고 운영 중단의 한 원인으로 보고되지만, 그 근거는 아직 판매사 조사 수준이다. [추정][^ref-309] 하이브리드 WMS(창고 관리 시스템, Warehouse Management System) 판매사 Synergy Logistics의 조사 주장을 전한 FreightWaves 기사에 따르면, 응답 조직의 84%가 최근 24개월 안에 큰 운영 중단을 한 번 이상 겪었고 절반 가까이는 소프트웨어·연결 중단으로 자동화 자산이 멈췄다. [추정][^ref-309] 중단 비용은 시간당 최대 10만 달러로 제시되었으나 하한은 미확인이고, 조사 방법·표본과 기사 발행일도 확인하지 못했다. [추정][^ref-309]

현장 무선망의 품질도 같은 문제다. CJ대한통운은 2023년 4월 이천 2풀필먼트센터에 물류센터 최초로 5G 특화망 이음5G를 구축했다고 발표하면서 기존 와이파이의 채널 간섭·지연을 생산성 저하 원인으로 들었고, 와이파이 대비 약 1,000배 빠른 속도를 주장했다. [추정] 벤더 주장[^ref-307] 발표 당시 로봇·설비·CCTV 적용은 무선 단말 시범 적용 뒤의 확대 계획이었다. [추정] 벤더 주장[^ref-307]

그래서 2절의 질문은 로봇 한 대의 성능이 아니라 통신과 계산을 어디에 두는가의 문제가 된다. 다만 외부망 단절 중 운영 범위를 정한 물류센터의 공개 기준이나 사례는 이번 조사에서 찾지 못했고, 아래 5절의 답은 관제 표준과 엣지 플랫폼 문서에서 끌어낸 추론이다. [추정][^ref-031][^ref-300]

## 4. 핵심 개념과 용어

2절의 질문을 다루려면 계산 계층, 분산 시스템의 이론적 한계, 통신 품질을 가리키는 용어를 먼저 맞춰야 한다. 아래 용어는 이 페이지 전체에서 같은 뜻으로 쓴다.

자세한 내용은 주제 페이지 [42. 분산 시스템·통신·컴퓨팅 구조 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area11-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다.

**물류 흐름 단계:** 피킹

**시나리오:** 피킹 운반 도중 현장과 클라우드를 잇는 외부망이 끊김

| 항목 | 내용 |
|---|---|
| 시작 조건 | 클라우드 WMS가 내린 피킹 주문으로 ROP가 운반 작업을 만들어 로봇에 배정했고, 운반 도중 외부망이 끊긴다. |
| 작업 대상 | 피킹한 상품을 담은 토트·박스 |
| 수행 자원 | 현장 서버의 관제·브로커가 배정과 로봇 통신을 맡고 로봇은 받은 경로를 주행한다. Open-RMF free_fleet는 로봇마다 Zenoh 브리지를 두고 라우터를 플릿 어댑터와 같은 네트워크에서 실행하는 구성을 공개한다. [사실][^ref-256] |
| 제약 | VDA 5050(3.0.0 기준)은 연결 실패와 메시지 손실이 있는 무선망을 전제하고 주문·상태 토픽에 재전송 없는 MQTT QoS 0을 쓴다. [사실][^ref-031] 공장 자동화 같은 초저지연 서비스는 종단 간 10ms 미만 지연을 요구한다고 정리된다(2020년 논문 기준). [사실][^ref-311] |
| 완료·인계 | 단절 중에는 클라우드 WMS의 새 주문 수신과 재고 확정이 멈추고, 재연결 뒤 현장 완료 기록을 WMS 기록과 맞춰야 할 것으로 보인다. [추정][^ref-310] |
| 예외·성과 | 로봇은 브로커와 끊겨도 이미 해제된 노드까지 주문을 수행한다. [사실][^ref-031] 재연결 뒤 관제는 다음 상태 메시지로 로봇 상태를 다시 세워야 할 것으로 보인다. [추정][^ref-031][^ref-306] |

다음은 설명을 위한 가상의 시나리오이다. 관제와 브로커를 현장 서버에 두었다면 외부망 단절 중에도 이미 받은 주문과 현장 내 배정은 이어 갈 수 있으나, 클라우드 WMS의 새 주문 수신과 재고 확정은 멈추고 CAP 제약에 따라 단절 중 현장 기록과 WMS 기록을 재연결 뒤 맞추는 절차가 필요할 것으로 보인다. [추정][^ref-031][^ref-300][^ref-301][^ref-310] 이 판단은 로봇·엣지 플랫폼 문서를 대응시킨 추론이며, 물류센터의 외부망 단절 운영 기준이나 공개 사례로 확인한 것은 아니다.

현장 무선망이 끊기는 경우는 사정이 다르다. VDA 5050 3.0.0에서 로봇은 브로커와 연결이 끊겨도 받은 주문 정보를 유지하고 "fulfills the order up to the last released node" — 곧 해제된 베이스까지만 수행하고 해제되지 않은 호라이즌 구간은 주행하지 않는다. [사실][^ref-031] 주문·상태가 QoS 0이고 상태는 사건 발생 시와 적어도 30초마다(최대 간격 30초) 다시 보내므로, 재연결 뒤 관제는 끊긴 동안의 메시지가 쌓여 전달되리라 기대하기보다 다음 상태 메시지로 로봇 상태를 다시 세우고 주문을 갱신하는 구조가 필요할 것으로 보인다. [추정][^ref-031][^ref-306] VDA 5050이 MQTT 5.0의 세션 만료 같은 장치를 어떻게 쓰는지는 미확인이다.

## 6. 대표 접근법과 기술

공개 자료가 다루는 접근법은 분산 발견과 라우터 연결, 손실을 전제한 메시지 설계, 엣지의 단절 중 운영, 클라우드·포그로의 계산 이전, 관제 서버 가용성과 다거점 구성으로 나눌 수 있다. [의견]

자세한 내용은 주제 페이지 [42. 분산 시스템·통신·컴퓨팅 구조 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area11-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

VDA 5050(3.0.0 기준)은 연결 실패와 메시지 손실이 있는 무선망을 전제한 통신 방식을 정한다. [사실][^ref-031] KubeEdge는 클라우드–엣지 네트워크가 끊겨도 엣지 노드와 애플리케이션이 자율적으로 계속 동작하는 구조를 둔다. [사실][^ref-300]

자세한 내용은 주제 페이지 [42. 분산 시스템·통신·컴퓨팅 구조 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area11-s7.md)에 있다.

## 8. 대표 연구와 자료

이 영역의 학술 자료는 계산 계층 모델, 분산 시스템의 이론적 한계, 클라우드 로보틱스, 초저지연 무선 통신으로 나뉜다. [의견]

자세한 내용은 주제 페이지 [42. 분산 시스템·통신·컴퓨팅 구조 — 대표 연구와 자료](../../topics/2026/2026-09-25-area11-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

ROP는 명령·상태 메시지의 통신 품질 요구, 연결 상태 감시, 재연결 뒤 상태 재구성을 맡고, 무선망 구축과 로봇 탑재 주행·회피는 연계 대상으로 두는 것으로 보인다. [추정][^ref-031][^ref-307]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 상위 업무 시스템 | 외부망 단절 중 이미 받은 주문·현장 내 배정의 지속 범위 판단, 재연결 뒤 완료·재고 기록을 WMS와 맞추는 절차 [추정][^ref-310] | 클라우드 WMS의 새 주문 발행·재고 확정(연계 대상) |
| 로봇 자체 지능·제어 | 명령·상태 메시지의 통신 품질 요구, last will 등을 이용한 연결 상태 감시, 재연결 뒤 상태 재구성 [추정][^ref-031] | 로봇 탑재부의 실시간 주행·회피와 인식·계획 계산(클라우드·포그로 옮기는 연구 포함)은 연계 대상이다 [추정][^ref-304][^ref-308] |

무선망(와이파이·5G 특화망) 구축·운영은 분류 원문 19장 표에 명시된 항목은 아니지만, ROP가 소유하지 않는 통신 기반 연계 대상에 가까운 것으로 보인다. [추정][^ref-307] 경계 전체는 [범위 경계](../../about/scope-boundary.md) 페이지에서 본다.

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역의 통신·계산 배치 결정은 관제 연동, 명령 신뢰성, 세계 상태, 업무 연속성과 직접 맞물린다. [의견]

자세한 내용은 주제 페이지 [42. 분산 시스템·통신·컴퓨팅 구조 — 다른 연구영역과의 연결](../../topics/2026/2026-09-25-area11-s10.md)에 있다.

## 11. 열린 질문

이번 실행은 다음 질문을 새로 올린다(id 는 [열린 질문](../../open-questions.md) 목록에 등록될 때 부여된다).

- (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-27) 외부망이 끊겨 클라우드 WMS와 단절된 동안 현장 ROP가 이미 받은 주문·작업을 어디까지 계속 실행하고, 재연결 뒤 재고·완료 기록을 어떻게 맞추는지 정한 국내 물류센터 운영 기준이나 사례가 있는가?
- (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-27) 물류센터 로봇 관제 통신(와이파이·5G 특화망)에서 명령·상태 메시지의 허용 지연·손실률·로밍 중단 시간을 정한 표준이나 공개 측정 자료가 있는가?
- (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-27) 여러 거점의 로봇 운영을 한곳에서 관리할 때 거점별 현장 서버와 중앙 클라우드 사이 역할 분담과 데이터 동기화를 공개한 오픈소스 구성이나 사례가 있는가?

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [42. 분산 시스템·통신·컴퓨팅 구조](distributed-systems-communication-and-computing.md) — 섹션 3~11 신규 작성(외부망 단절 운영 범위, VDA 5050 무선망 전제·QoS·베이스/호라이즌, ROS 2 DDS·Zenoh, 엣지 단절 운영, 계산 배치 선례, 피킹 시나리오), 페이지 상태 표식 추가, 조건부 승인 수정 16건 이행, 4·6·7·8·10절 주제 페이지 분리 상태 유지. 2차 수정: 7절 첫 문장을 VDA 5050·KubeEdge 두 사례에 한정한 [사실] 문장으로 교체 (실행 2026-09-25-27)
- 2026-09-25 · 생성 · [42. 분산 시스템·통신·컴퓨팅 구조 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area11-s6.md) — 자동 분리: 11. 분산 시스템·통신·컴퓨팅 구조 의 "6. 대표 접근법과 기술" 절(2,039자)을 옮겼다 (실행 2026-09-25-27)
- 2026-09-25 · 생성 · [42. 분산 시스템·통신·컴퓨팅 구조 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area11-s4.md) — 자동 분리: 11. 분산 시스템·통신·컴퓨팅 구조 의 "4. 핵심 개념과 용어" 절(1,171자)을 옮겼다 (실행 2026-09-25-27)
- 2026-09-25 · 생성 · [42. 분산 시스템·통신·컴퓨팅 구조 — 대표 연구와 자료](../../topics/2026/2026-09-25-area11-s8.md) — 자동 분리: 11. 분산 시스템·통신·컴퓨팅 구조 의 "8. 대표 연구와 자료" 절(855자)을 옮겼다. 2차 수정: NIST 항목의 쓰임새 평가를 [의견]으로, Gilbert·Lynch 항목의 적용 구절을 [추정]으로 분리 (실행 2026-09-25-27)
- 2026-09-25 · 생성 · [42. 분산 시스템·통신·컴퓨팅 구조 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area11-s7.md) — 자동 분리: 11. 분산 시스템·통신·컴퓨팅 구조 의 "7. 관련 표준·프레임워크·오픈소스" 절(769자)을 옮겼다. 2차 수정: 세 줄 요약·본문 첫 문장의 '대부분' 일반화를 VDA 5050·KubeEdge 두 사례에 한정한 [사실] 문장으로 교체 (실행 2026-09-25-27)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-256]: Open Robotics (open-rmf), free_fleet — README (A free fleet management system), 미확인, https://github.com/open-rmf/free_fleet, 접근일 2026-09-25
[^ref-300]: KubeEdge (CNCF, kubeedge GitHub), KubeEdge — README, 미확인, https://github.com/kubeedge/kubeedge, 접근일 2026-09-25
[^ref-301]: Microsoft, Operate Azure IoT Edge devices offline, 2026-03-02, https://learn.microsoft.com/en-us/azure/iot-edge/offline-capabilities, 접근일 2026-09-25
[^ref-304]: Ichnowski, J., Chen, K. 외(UC Berkeley AUTOLAB), FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2, 2022-05, https://arxiv.org/abs/2205.09778, 접근일 2026-09-25 (원문 미열람)
[^ref-306]: OASIS, MQTT Version 5.0, 2019-03, https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html, 접근일 2026-09-25 (원문 미열람)
[^ref-307]: CJ대한통운, CJ대한통운, 물류센터 최초 5G 개통 … 속도 1000배 빨라진다, 2023-04, https://www.cjlogistics.com/ko/newsroom/news/NR_00001046, 접근일 2026-09-25 (원문 미열람)
[^ref-308]: Brorsson, E. 외, Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives, 2025-12, https://arxiv.org/abs/2512.15215, 접근일 2026-09-25 (원문 미열람)
[^ref-309]: FreightWaves, Warehouses face $100K-hour downtime risk as cloud outages mount, 미확인, https://www.freightwaves.com/news/warehouses-face-100k-hour-downtime-risk-hybrid-wms, 접근일 2026-09-25 (원문 미열람)
[^ref-310]: Gilbert, S., & Lynch, N., Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services, 2002-06, https://dl.acm.org/doi/10.1145/564585.564601, 접근일 2026-09-25 (원문 미열람)
[^ref-311]: ETRI Journal 게재 논문(Jun 외, 한국전자통신연구원 발행), Ultra-low-latency services in 5G systems: A perspective from 3GPP standards, 2020, https://onlinelibrary.wiley.com/doi/full/10.4218/etrij.2020-0200, 접근일 2026-09-25 (원문 미열람)
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

### docs/categories/planning-and-business/index.md

````markdown
---
title: "A. 기획·사업"
type: category
status: published
created: 2026-09-24
updated: 2026-09-25
version: 2
sources: [ref-002, ref-023, ref-031, ref-044, ref-049, ref-060, ref-098, ref-101, ref-102, ref-103, ref-104, ref-105, ref-111, ref-115, ref-121, ref-125, ref-129, ref-130, ref-132, ref-133, ref-134, ref-146, ref-148, ref-149]
---

[홈](../../index.md) › A. 기획·사업

# A. 기획·사업

## 핵심 질문

어떤 일을 로봇에게 맡기고, 무엇을 들여, 어떤 효과를 볼 것인가? [분류원문]

## 개요

플랫폼을 들이기 전과 들이는 동안 무엇을 왜 할지 정하는 일. 기술·시장 동향 조사, 사용 사례·요구·책임 범위, 경제성·조달·사업 모델. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **1. 기술·시장·업체 동향** | 카테고리마다 연구·기사·업체 발표를 모으고, 제품·업체·로봇 종류의 지형을 정리한다 | 어떤 연구·제품·업체가 로봇 오케스트레이션의 흐름을 바꾸고 있는가? | [1. 기술·시장·업체 동향](technology-market-and-vendor-trends.md) | published |
| **2. 사용 사례·요구·책임 범위** | 로봇에게 맡길 일과 현장 유형별 요구, 플랫폼이 직접 맡을 범위와 외부에 맡길 범위를 정한다 | 로봇에게 어떤 일을 맡기고, 플랫폼은 그중 어디까지 직접 책임질 것인가? | [2. 사용 사례·요구·책임 범위](use-cases-requirements-and-scope.md) | published |
| **3. 경제성·조달·사업 모델** | 투자 효과를 따지고, 로봇·플랫폼을 골라 계약하고, 과금 방식을 정한다 | 도입 비용을 넘는 효과가 나오며, 어떤 로봇과 플랫폼을 어떤 조건으로 들일 것인가? | [3. 경제성·조달·사업 모델](economics-procurement-and-business-models.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

핵심은 **로봇 개별 성능과 업무 전체 성과를 구분하는 것**이다. 로봇이 물건을 더 빨리 가져와도 다음 단계가 막히면 대기만 늘어날 수 있다. [분류원문]

## 다른 대분류와의 연결

> **이전 분류 기준 내용.** 아래는 이전 분류(7개 대분류)에서 A. 업무·공급망 설계 페이지에 2026-09-25 작성한 연결이다. 대분류 이름은 그때의 것이고, 링크는 새 영역 페이지로 옮겨 두었다. 새 17개 대분류 기준의 연결은 이어지는 조사에서 다시 쓴다.


A. 업무·공급망 설계가 정한 업무는 다른 여섯 대분류의 세부영역으로 넘어가 실행되고 측정된다. 예를 들어 VDA 5050 은 외부 IT 시스템과의 인터페이스를 범위에서 제외하므로, 상위 주문을 로봇 작업 요청으로 번역하는 계층이 넘겨받는 지점이 될 것으로 보인다. [추정][^ref-031][^ref-125]

아래 연결은 게시된 23. 업무 시스템 연동 ~ 39. 운영 성과 측정·개선 페이지에서 검증된 주장을 근거로 한다. 연결 상대 세부영역은 대부분 아직 심화 조사 전이라, 상대편에 관한 서술도 A. 업무·공급망 설계 쪽 근거에 기댄다. 확인일은 2026-09-25이고, 출처별 발행일은 참고 자료 절의 각주에 있다.

```mermaid
flowchart LR
  a1["23. 업무 시스템 연동"]
  a2["24. 작업·워크플로 모델링"]
  a3["35. 처리능력·규모·배치 설계"]
  a4["39. 운영 성과 측정·개선"]
  b7["17. 작업 대상·자산 식별과 인계 추적"]
  b8["18. 실시간 세계 상태·데이터 일관성"]
  c9["20. 로봇·제조사 관제 연동"]
  c10["22. 설비·건물 시스템 연동"]
  c12["29. 명령·작업 실행의 신뢰성"]
  d13["25. 작업 배정 — MRTA"]
  d14["26. 작업 순서·스케줄링"]
  d16["28. 공용 자원·충전·에너지 최적화"]
  e17["30. 로봇 간 협업·물리적 인계"]
  e19["38. 모니터링·이상 탐지·원인 분석"]
  e20["32. 예외 복구·재계획·업무 연속성"]
  f22["34. 시뮬레이션·예측용 디지털 트윈"]
  f23["54. 시험·형식 검증·벤치마크"]
  g28["21. 상호운용 표준·적합성"]
  a1 --> c9
  a1 --> c12
  a1 --> d13
  a1 --> d14
  a1 --> e20
  a1 --> g28
  a2 --> b7
  a2 --> c12
  a2 --> e17
  a2 --> f23
  a3 --> c10
  a3 --> d13
  a3 --> d16
  a3 --> f22
  a4 --> b8
  a4 --> d16
  a4 --> e19
  a4 --> f22
```

### [옛 B. 공통 정보·환경 모델](../robot-ontology/index.md)

- **[24. 작업·워크플로 모델링](../planning-and-optimization/task-and-workflow-modeling.md) ↔ [17. 작업 대상·자산 식별과 인계 추적](../objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md)** — '운반 완료'와 '인수 확인·재고 반영 완료'를 잇는 신호가 여기서 나온다. GS1 핵심 업무 어휘(Core Business Vocabulary, CBV)는 객체가 위치에 도착하는 arriving, 수령자 재고에 추가되는 receiving, 점유·소유가 바뀌는 accepting 을 서로 다른 업무 단계로 정의한다. [사실][^ref-044] VDA 5050 은 drop 동작의 완료를 적재물이 로봇을 떠나고 로봇이 새 적재 상태를 보고한 때로 정의한다. [사실][^ref-031] 로봇 완료 신호는 arriving 수준의 물리적 인도에 가까우므로, 공정 모델의 '인수 확인·재고 반영 완료' 조건은 17. 작업 대상·자산 식별과 인계 추적이 다루는 식별자와 receiving·accepting 이벤트에 기대야 할 것으로 보인다. [추정][^ref-044][^ref-031][^ref-049] 이 구성을 적용한 표준·사례는 확인하지 못했다([열린 질문](../../open-questions.md) oq-001, oq-012).
- **[39. 운영 성과 측정·개선](../field-operations-and-monitoring/operational-performance-measurement-and-improvement.md) ↔ [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md)** — Open-RMF 로봇 상태 스키마는 상태 값(idle·charging·working·error 등), 0~1 범위의 배터리, 현재 작업 id, 운영자가 대응할 문제 목록, 위치, 기록 시각을 담는다. [사실][^ref-148] 이 필드들은 가동률·충전 시간·오류 시간 같은 성과 지표를 계산하는 원천이 될 것으로 보이며, 이 연결은 현재 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성 쪽에 속한다. [추정][^ref-148]

### [옛 C. 연결·실행 기반](../integration/index.md)

- **[23. 업무 시스템 연동](../integration/business-system-integration.md) ↔ [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md)** — VDA 5050 3.0.0 명세는 관제 시스템과 이동로봇 사이 통신에 해당하지 않는 인터페이스, 곧 주변 설비·인프라·외부 IT 시스템과의 인터페이스를 범위에서 뺀다. [사실][^ref-031] 이처럼 로봇 인터페이스가 상위 시스템 연동을 범위 밖에 두므로, 상위 주문을 로봇 작업 요청(Open-RMF 작업 요청 등)으로 번역하는 계층이 두 대분류가 넘겨받는 지점이 될 것으로 보인다. [추정][^ref-031][^ref-125] 이 번역 계층을 규정한 표준은 확인하지 못했다.
- **[23. 업무 시스템 연동](../integration/business-system-integration.md)·[24. 작업·워크플로 모델링](../planning-and-optimization/task-and-workflow-modeling.md) ↔ [29. 명령·작업 실행의 신뢰성](../execution-collaboration-and-recovery/command-and-task-execution-reliability.md)** — 상위 쪽 변경·취소 명령이 로봇 쪽 실행 상태와 만나는 지점이다. B2MML 거래 프로파일은 CHANGE·CANCEL 등의 거래 동사를 정의한다. [사실][^ref-129] OPC UA for ISA-95 Job Control 은 Update·Pause·Resume·Abort·Cancel 등의 작업 지시 메서드를 정의한다. [사실][^ref-130] 로봇 쪽 VDA 5050 은 주문을 수행하는 중에 다른 주문을 받으면 로봇이 OTHER_ORDER_ACTIVE 오류를 경고(WARNING) 수준으로 보고하게 한다. [사실][^ref-031] 취소할 수 없는 동작은 주문 취소(cancelOrder) 뒤에도 실행 중(RUNNING)을 거쳐 완료(FINISHED) 또는 실패(FAILED)로 보고하게 한다. [사실][^ref-031] Open-RMF 작업 상태 스키마는 queued·underway·completed·canceled·killed·failed 등의 상태 값, 시작·종료 시각, 소요 시간 추정, 취소·강제 종료·중단 요청 기록을 담는다. [사실][^ref-111] 이 기록은 두 세부영역이 상위 시스템에 되돌려 줄 결과의 원천이 될 것으로 보인다. [추정][^ref-111]
- **[35. 처리능력·규모·배치 설계](../design-and-simulation/capacity-sizing-and-layout-design.md) ↔ [22. 설비·건물 시스템 연동](../integration/facility-and-building-system-integration.md)** — Open-RMF 데모의 호텔 환경은 승강기 2대, 여러 문, 3개 플릿(로봇 4대)이 다층 건물에서 함께 일하는 구성을 보이고, 공간과 승강기·문 같은 건물 설비를 공유하는 로봇의 교통 관리를 설명한다. [사실][^ref-104] 병원 약품 배송 로봇 사례에서는 승강기 가동률이 높을수록 배송 실패가 많고 배송 시간이 길었다. [사실][^ref-060] 다층 호텔의 배송 로봇 연구는 승강기를 경로 계획 안의 대기·운행 시간으로 모델링했다. [사실][^ref-103] 두 사례는 병원·호텔이며 물류센터 적용 여부는 미확인이다([열린 질문](../../open-questions.md) oq-010). 35. 처리능력·규모·배치 설계은 승강기를 처리능력의 제약 입력으로만 받는다. 승강기 제어 자체는 분류 원문 19장의 시설·설비 제어 경계에 따라 연계 대상이며, ROP 는 22. 설비·건물 시스템 연동을 통해 작업 요청·예약·상태 확인을 맡는다.

### [옛 D. 계획·최적화](../planning-and-optimization/index.md)

- **[23. 업무 시스템 연동](../integration/business-system-integration.md) ↔ [26. 작업 순서·스케줄링](../planning-and-optimization/task-sequencing-and-scheduling.md)** — 웨이브·웨이브리스 출고 지시 정책 연구(Gallien·Weber, 2010)와 동적으로 도착하는 주문의 피킹 재최적화 연구(Lorenz 외, 2025)는 상위 시스템의 출고 지시·우선순위 변경이 작업 순서 결정 문제로 넘어가는 지점을 다루는 것으로 보인다. [추정][^ref-134][^ref-133]
- **[23. 업무 시스템 연동](../integration/business-system-integration.md) ↔ [25. 작업 배정 — MRTA](../planning-and-optimization/task-allocation-mrta.md)** — 작업자가 피킹하고 자율이동로봇(Autonomous Mobile Robot, AMR)이 운반하는 동적 주문 피킹 연구(2025)는 AMR 가용성에 따른 개입 전략을 다룬다. [추정][^ref-132] 이 연구는 주문 변경과 로봇 배정이 맞물리는 사례가 될 것으로 보인다. [추정][^ref-132]
- **[35. 처리능력·규모·배치 설계](../design-and-simulation/capacity-sizing-and-layout-design.md) ↔ [25. 작업 배정 — MRTA](../planning-and-optimization/task-allocation-mrta.md)** — Open-RMF 플릿 어댑터 템플릿 설정은 배터리가 recharge_threshold(예시값 0.10) 아래로 내려간 로봇에게 작업을 맡기지 않게 한다. [사실][^ref-105] 또 충전 목표(recharge_soc), 로봇별 충전기, 작업 종료 후 동작(park·charge·nothing)을 둔다. [사실][^ref-105]
- **[35. 처리능력·규모·배치 설계](../design-and-simulation/capacity-sizing-and-layout-design.md) ↔ [28. 공용 자원·충전·에너지 최적화](../planning-and-optimization/shared-resource-charging-and-energy-optimization.md)** — AMR 물류센터 시뮬레이션 연구(2025)에서는 충전기가 부족하면 큰 지연이, 남으면 불필요한 비용이 생겼다. [사실][^ref-102] 로봇 이동형 풀필먼트 시스템(Robotic Mobile Fulfillment System, RMFS)의 충전·배터리 교환 전략을 비교한 연구(2018)도 있다. [사실][^ref-098]
- **[39. 운영 성과 측정·개선](../field-operations-and-monitoring/operational-performance-measurement-and-improvement.md) ↔ [28. 공용 자원·충전·에너지 최적화](../planning-and-optimization/shared-resource-charging-and-energy-optimization.md)** — Omega(2024)에 실린 연구는 RMFS 에서 동적 우선순위 규칙이 선착순보다 에너지 소비를 3.41% 줄이고 처리량을 26.07% 높였다고 보고했다. [사실][^ref-146] 이 수치는 모델·시뮬레이션 조건의 저자 보고값이며 현장 실측이 아니다. [사실][^ref-146]

### [옛 E. 협업·현장 운영](../execution-collaboration-and-recovery/index.md)

- **[23. 업무 시스템 연동](../integration/business-system-integration.md) ↔ [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md)** — 상위 시스템의 취소(CANCEL)가 로봇이 화물을 이미 실은 뒤에 오거나, 취소할 수 없는 동작이 끝까지 수행될 수 있다. [추정][^ref-031][^ref-129] 이 경우 되돌림 작업과 재고 반영이 복구·재계획 과제로 넘어갈 것으로 보인다. [추정][^ref-031][^ref-129] 되돌림 규칙을 정한 표준·사례는 확인하지 못했다([열린 질문](../../open-questions.md) oq-021).
- **[24. 작업·워크플로 모델링](../planning-and-optimization/task-and-workflow-modeling.md) ↔ [30. 로봇 간 협업·물리적 인계](../execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md)** — 공정 모델이 완료 조건으로 삼을 수 있는 인계 확인 신호가 여기에 있다. Open-RMF 배송 작업에서 로봇은 하역 지점의 워크셀(workcell)에 IngestorRequest 를 보내고, IngestorResult 를 받을 때까지 이를 반복한다. [사실][^ref-023] IngestorResult 는 시각, 요청 id, 워크셀 id, 상태(ACKNOWLEDGED·SUCCESS·FAILED)를 담는다. [사실][^ref-049]
- **[39. 운영 성과 측정·개선](../field-operations-and-monitoring/operational-performance-measurement-and-improvement.md) ↔ [38. 모니터링·이상 탐지·원인 분석](../field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md)** — 제조 처리량의 병목 탐지 방법을 검토한 문헌(2023)과 창고 이벤트 로그에 프로세스 마이닝을 적용한 사례(2015)가 있다. [추정][^ref-115][^ref-149] 이를 로봇 상태 기록에 적용하면 성과 분석과 이상·원인 분석이 같은 로그를 공유할 것으로 보인다. [추정][^ref-115][^ref-149][^ref-148] 이런 적용 연구는 확인하지 못했다([열린 질문](../../open-questions.md) oq-018).

### [옛 F. 도입·검증·유지관리](../verification-deployment-and-lifecycle/index.md)

- **[24. 작업·워크플로 모델링](../planning-and-optimization/task-and-workflow-modeling.md) ↔ [54. 시험·형식 검증·벤치마크](../verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md)** — 워크플로 넷의 건전성(soundness) 판정 복잡도를 다룬 연구(2022)가 있다. [추정][^ref-121] 따라서 공정 모델의 형식적 설계 점검은 형식 검증과 이어질 것으로 보인다. [추정][^ref-121] 물류 로봇 공정에 적용한 사례는 확인하지 못했다.
- **[35. 처리능력·규모·배치 설계](../design-and-simulation/capacity-sizing-and-layout-design.md) ↔ [34. 시뮬레이션·예측용 디지털 트윈](../design-and-simulation/simulation-and-predictive-digital-twin.md)** — RAWSim-O 는 RMFS 운영의 여러 결정 문제가 미치는 효과를 연구하기 위한 이산 사건 시뮬레이션이다. [사실][^ref-101] 이런 도구는 증차·증설처럼 가정한 미래를 실험하는 데 쓰일 것으로 보인다. [추정][^ref-101]
- **[39. 운영 성과 측정·개선](../field-operations-and-monitoring/operational-performance-measurement-and-improvement.md) ↔ [34. 시뮬레이션·예측용 디지털 트윈](../design-and-simulation/simulation-and-predictive-digital-twin.md)** — 우선순위 정책이나 충전 대안을 운영 전에 비교하는 일은 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈 쪽 일이다. 이 일은 현재 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성과 역할을 나눠 연결될 것으로 보인다. [추정][^ref-146][^ref-102]

### [옛 G. 안전·보안·지능·거버넌스](../governance-law-and-society/index.md)

- **[23. 업무 시스템 연동](../integration/business-system-integration.md) ↔ [21. 상호운용 표준·적합성](../integration/interoperability-standards-and-conformance.md)** — ISA-95 계열의 작업 지시 동사·메서드와 VDA 5050·Open-RMF 의 주문·작업 요청을 잇는 표준 매핑은 이번 조사 범위에서 확인되지 않았다. 그래서 번역 규칙을 누가 소유하고 누가 변경을 승인하는지가 상호운용성 거버넌스 과제로 넘어갈 것으로 보인다. [추정][^ref-129][^ref-130][^ref-031][^ref-125] 관련 질문은 [열린 질문](../../open-questions.md) oq-020 이다.

### 아직 다루지 않은 연결

42. 분산 시스템·통신·컴퓨팅 구조, 55. 현장 조사·설치·시운전, 57. 자산·소프트웨어 수명주기 관리, 48. 안전·위험 관리, 51. 인증·권한·격리, 47. AI·학습·적응과 모델 운영과의 연결은 검증된 근거가 아직 없어 싣지 않았다. 해당 세부영역의 조사가 게시되면 보강한다.

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 68건이다(논문 19건 · 기사·보고서 23건 · 업체 발표 2건 · 표준·오픈소스·기관 자료 24건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-1104](../../references/ref-1104.md) — Friese, C., Klebbe, R., & Heimann-Steinert, A. (JMIR Nursing), Nurses' Evaluation of a Service Robot for Inpatient Care: Technology Acceptance Study (발행 2026-04-14)
- [ref-1161](../../references/ref-1161.md) — Li, M., Liu, X., Gao, Y., Sun, Y., Li, P., Zhou, L., Wei, M., & Li, L. (Scientific Reports 16), Application management and effectiveness analysis of intelligent logistics robots in hospital drug and specimen delivery scenarios (발행 2026-04)
- [ref-060](../../references/ref-060.md) — Lee, Y. 외(Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments (발행 2026)
- [ref-1160](../../references/ref-1160.md) — Lee, J. S., & Aswani, A. (arXiv), Profit Maximization for a Robotics-as-a-Service Model (발행 2025-09-30)
- [ref-165](../../references/ref-165.md) — Autonomous Robots 게재 서베이(arXiv 2502.03814) 저자, Large Language Models for Multi-Robot Systems: A Survey (발행 2025-02)
- [ref-133](../../references/ref-133.md) — Lorenz, Otto, & Gendreau (Networks, Wiley), Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization? (발행 2025)
- [ref-132](../../references/ref-132.md) — Yu, S., & Srinivas, S., Collaborative Human–Robot Teaming for Dynamic Order Picking: Interventionist strategies for improving warehouse intralogistics operations (발행 2025)
- [ref-102](../../references/ref-102.md) — Springer(FAIM 2025 발표 논문, 저자 미확인), Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics (발행 2025)
- [ref-1162](../../references/ref-1162.md) — Sivalingam, C. S., & Subramaniam, S. K. (Heliyon), Cobot selection using hybrid AHP-TOPSIS based multi-criteria decision making technique for fuel filter assembly process (발행 2024-02-15)
- [ref-146](../../references/ref-146.md) — Omega 게재 논문(저자 미확인), The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority (발행 2024)
- 그 밖에 9건

**기사·보고서**

- [ref-909](../../references/ref-909.md) — 서울신문, 부품 배치 '척척' 무거운 짐도 '사뿐'… 아틀라스 2.5만대 로봇 학교 간다 (발행 2026-09-23)
- [ref-908](../../references/ref-908.md) — 아시아경제, CJ대한통운, 물류업계 최초 AI 휴머노이드 상용화 '첫발' (발행 2026-09-03)
- [ref-1170](../../references/ref-1170.md) — Modern Materials Handling (Bridget McCrea; Peerless Research Group·MHI 조사), 2026 Intralogistics Robotics Survey: Robotics moves into the mainstream (발행 2026-06-01)
- [ref-901](../../references/ref-901.md) — International Federation of Robotics (IFR), Robot Density Surges in Europe, Asia, and Americas (발행 2026-04-08)
- [ref-1200](../../references/ref-1200.md) — 아시아경제, 호텔 룸서비스도 카카오모빌리티 로봇이…"가동률 ... (제목 일부만 확인) (발행 2026-03-16)
- [ref-903](../../references/ref-903.md) — 로봇신문 (한국로봇산업진흥원 '2024년 국내 로봇산업 실태조사 결과 보고서' 요약), [Cover Story] '2024년 국내 로봇산업 실태 조사 결과 보고서' 요약 (발행 2026-01-25)
- [ref-902](../../references/ref-902.md) — International Federation of Robotics (IFR), Top 5 Global Robotics Trends 2026 (발행 2026-01-08)
- [ref-1166](../../references/ref-1166.md) — 전자신문, 조달청, 2026년 혁신제품 시범구매 기본계획 발표 (발행 2025-12-18)
- [ref-870](../../references/ref-870.md) — 로봇신문, [기업 최전선을 가다-클로봇] 로봇 소프트웨어로 쓰는 ‘피지컬 AI’ 시대의 서막 (발행 2025-11-09)
- [ref-899](../../references/ref-899.md) — International Federation of Robotics (IFR), World Robotics 2025 report – SERVICE ROBOTS – released by IFR (발행 2025-10-07)
- 그 밖에 13건

**업체 발표**

- [ref-906](../../references/ref-906.md) — Agility Robotics, Digit Moves Over 100,000 Totes in Commercial Deployment (발행 2025-11-20)
- [ref-1163](../../references/ref-1163.md) — AutoStore, Buying vs. RaaS: What's the Best Strategy for Investing in Warehouse Robotics? (발행 미확인)

**표준·오픈소스·기관 자료**

- [ref-872](../../references/ref-872.md) — Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025 (발행 2025-05-01)
- [ref-1158](../../references/ref-1158.md) — Messina, E. & Saidi, K. S. (NIST, National Institute of Standards and Technology), Research Opportunities for Advancing Measurement Science for Manufacturing Robotics (NIST GCR 24-054) (발행 2024-06-07)
- [ref-130](../../references/ref-130.md) — OPC Foundation, UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv) (발행 2024-01-31)
- [ref-991](../../references/ref-991.md) — 대한민국 정책브리핑 (산업통상자원부·경찰청), ‘실외이동로봇’ 보도 통행 가능해진다…배달·순찰 등 활용 (발행 2023-11-16)
- [ref-129](../../references/ref-129.md) — MESA International, B2MML-BatchML/Schema/B2MML-TransactionProfile.xsd (발행 2023)
- [ref-044](../../references/ref-044.md) — GS1, gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0) (발행 2021-09-30)
- [ref-1195](../../references/ref-1195.md) — 산업통상자원부 (KDI 경제정보센터 게재), 로봇활용 표준공정모델로 제조산업 전 분야에 로봇보급 본격 착수 (발행 2020-06-25)
- [ref-1203](../../references/ref-1203.md) — ISO / IEC / IEEE, ISO/IEC/IEEE 29148:2018 Systems and software engineering — Life cycle processes — Requirements engineering (발행 2018)
- [ref-1167](../../references/ref-1167.md) — IEC (International Electrotechnical Commission), IEC 60300-3-3:2017 Dependability management - Part 3-3: Application guide - Life cycle costing (발행 2017-01-27)
- [ref-947](../../references/ref-947.md) — 한국로봇산업진흥원, 서비스로봇 실증사업 (발행 미확인)
- 그 밖에 14건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-30 · 갱신 · [3. 경제성·조달·사업 모델](economics-procurement-and-business-models.md) — 섹션 3~11 신규 작성(현장 유형 사례 5건: 물류창고·제조 공장·병원 2·상업 시설, 표준·제도 6건, 자료 8건, 경계 2행, 연결 16개, 열린 질문 9건), 프런트매터 채움, 13절 각주. 2차: 3절 첫 문장을 설문 범위로 한정, ref-031 접근일 2026-09-30 (실행 2026-09-30-19)
- 2026-09-30 · 생성 · [3. 경제성·조달·사업 모델 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area03-s6.md) — 자동 분리: 3. 경제성·조달·사업 모델 의 "6. 대표 접근법과 기술" 절(1,380자)을 옮겼다. 2차: ref-031 접근일 2026-09-30 (실행 2026-09-30-19)
- 2026-09-30 · 생성 · [3. 경제성·조달·사업 모델 — 대표 연구와 자료](../../topics/2026/2026-09-30-area03-s8.md) — 자동 분리: 3. 경제성·조달·사업 모델 의 "8. 대표 연구와 자료" 절(1,281자)을 옮겼다 (실행 2026-09-30-19)
- 2026-09-30 · 생성 · [3. 경제성·조달·사업 모델 — 열린 질문](../../topics/2026/2026-09-30-area03-s11.md) — 자동 분리: 3. 경제성·조달·사업 모델 의 "11. 열린 질문" 절(1,265자)을 옮겼다 (실행 2026-09-30-19)
- 2026-09-30 · 생성 · [3. 경제성·조달·사업 모델 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area03-s10.md) — 자동 분리: 3. 경제성·조달·사업 모델 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,106자)을 옮겼다. 2차: ref-031 접근일 2026-09-30 (실행 2026-09-30-19)
<!-- auto:category-recent:end -->

## 참고 자료

[^ref-023]: Open Robotics, Workcells - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_workcells.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-044]: GS1, gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0), 2021-09-30, https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl, 접근일 2026-09-25
[^ref-049]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg, 접근일 2026-09-25
[^ref-060]: Lee, Y. 외(Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026, https://doi.org/10.1177/20552076261437181, 접근일 2026-09-25 (원문 미열람)
[^ref-098]: Zou, B., Gong, Y., de Koster, R., & Xu, X., Evaluating battery charging and swapping strategies in a robotic mobile fulfillment system, 2018, https://www.sciencedirect.com/science/article/abs/pii/S0377221717310901, 접근일 2026-09-25 (원문 미열람)
[^ref-101]: Merschformann, M. (RAWSim-O GitHub), RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README), 미확인, https://github.com/merschformann/RAWSim-O, 접근일 2026-09-25
[^ref-102]: Springer(FAIM 2025 발표 논문, 저자 미확인), Simulation-Driven Approach for Dimensioning AMR Fleets in Distribution Centre Logistics, 2025, https://link.springer.com/chapter/10.1007/978-3-032-07675-5_69, 접근일 2026-09-25 (원문 미열람)
[^ref-103]: PMC 게재 논문(저자 미확인), The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments, 미확인, https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/, 접근일 2026-09-25 (원문 미열람)
[^ref-104]: Open Robotics (open-rmf), rmf_demos — Demonstrations of Open-RMF (README), 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-25
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-09-25
[^ref-111]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-09-25
[^ref-115]: Production & Manufacturing Research 게재 논문(저자 미확인, Chalmers 공개본), Throughput bottleneck detection in manufacturing: a systematic review of the literature on methods and operationalization modes, 2023, https://www.tandfonline.com/doi/full/10.1080/21693277.2023.2283031, 접근일 2026-09-25 (원문 미열람)
[^ref-121]: Blondin, M., Mazowiecki, F., & Offtermatt, P. (LICS 2022), The complexity of soundness in workflow nets, 2022, https://arxiv.org/abs/2201.05588, 접근일 2026-09-25 (원문 미열람)
[^ref-125]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-09-25 (원문 미열람)
[^ref-129]: MESA International, B2MML-BatchML/Schema/B2MML-TransactionProfile.xsd, 2023, https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-TransactionProfile.xsd, 접근일 2026-09-25
[^ref-130]: OPC Foundation, UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv), 2024-01-31, https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL, 접근일 2026-09-25
[^ref-132]: Yu, S., & Srinivas, S., Collaborative Human–Robot Teaming for Dynamic Order Picking: Interventionist strategies for improving warehouse intralogistics operations, 2025, https://www.sciencedirect.com/science/article/abs/pii/S1366554525001231, 접근일 2026-09-25 (원문 미열람)
[^ref-133]: Lorenz, Otto, & Gendreau (Networks, Wiley), Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization?, 2025, https://onlinelibrary.wiley.com/doi/full/10.1002/net.22281, 접근일 2026-09-25 (원문 미열람)
[^ref-134]: Gallien, J., & Weber, T. G., To Wave or Not to Wave? Order Release Policies for Warehouses with an Automated Sorter, 2010, https://pubsonline.informs.org/doi/abs/10.1287/msom.1100.0291, 접근일 2026-09-25 (원문 미열람)
[^ref-146]: Omega 게재 논문(저자 미확인), The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority, 2024, https://www.sciencedirect.com/science/article/abs/pii/S0305048324001336, 접근일 2026-09-25 (원문 미열람)
[^ref-148]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json, 접근일 2026-09-25
[^ref-149]: Springer(학술대회 발표 논문, 저자 미확인), Material Movement Analysis for Warehouse Business Process Improvement with Process Mining: A Case Study, 2015, https://link.springer.com/chapter/10.1007/978-3-319-19509-4_9, 접근일 2026-09-25 (원문 미열람)
````

### docs/categories/planning-and-business/technology-market-and-vendor-trends.md (요약)

```markdown
# 1. 기술·시장·업체 동향

소속 대분류: A. 기획·사업 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

카테고리마다 연구·기사·업체 발표를 모으고, 제품·업체·로봇 종류의 지형을 정리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **기술·연구 동향 조사**: 카테고리마다 논문·기사·업체 발표를 모아 연구와 제품의 흐름을 추적한다
- **시장·업체·제품 지형**: 오케스트레이션·관제·상호운용 제품, 로봇 제조사, 통합 사업자의 지형을 정리한다
- **로봇 종류·형태 지형**: AMR·AGV·로봇팔·모바일 매니퓰레이터·사족 보행·휴머노이드·드론처럼 오케스트레이션 대상 로봇의 종류와 특성 변화를 추적한다

## 2. 핵심 질문

어떤 연구·제품·업체가 로봇 오케스트레이션의 흐름을 바꾸고 있는가? [분류원문]
```

### docs/categories/planning-and-business/use-cases-requirements-and-scope.md (요약)

```markdown
# 2. 사용 사례·요구·책임 범위

소속 대분류: A. 기획·사업 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

로봇에게 맡길 일과 현장 유형별 요구, 플랫폼이 직접 맡을 범위와 외부에 맡길 범위를 정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **책임 범위 정의**: 플랫폼이 직접 맡을 범위와 외부(업무 시스템·로봇 자체 지능·설비 제어·현장 간 운송·업종별 조건)에 맡길 범위를 정한다
- **사용 사례 발굴·요구 정의**: 로봇에게 맡길 일과 성공 기준·수용 기준을 정한다
- **현장 유형별 요구 정리**: 물류창고·제조 공장·병원·상업 시설·가정·실외 같은 현장 유형마다 공통 요구와 고유 요구를 정리한다

## 2. 핵심 질문

로봇에게 어떤 일을 맡기고, 플랫폼은 그중 어디까지 직접 책임질 것인가? [분류원문]
```

### docs/categories/planning-and-business/economics-procurement-and-business-models.md (요약)

```markdown
# 3. 경제성·조달·사업 모델

소속 대분류: A. 기획·사업 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

투자 효과를 따지고, 로봇·플랫폼을 골라 계약하고, 과금 방식을 정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **경제성·투자 효과 분석**: 도입 비용·운영비·총소유비용과 기대 효과를 비교해 투자 여부를 판단한다
- **로봇·솔루션 선정·조달**: 요구에 맞춰 로봇과 플랫폼을 평가하고 시범 운영과 계약을 진행한다
- **사업 모델·과금**: 서비스형 로봇(RaaS)·구독·작업당 과금 같은 사업 모델과 사용량 계량을 정한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 4번 영역 ‘성과·경제성·프로세스 개선’에서 왔다. 그 본문은 [39. 운영 성과 측정·개선](../field-operations-and-monitoring/operational-performance-measurement-and-improvement.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

도입 비용을 넘는 효과가 나오며, 어떤 로봇과 플랫폼을 어떤 조건으로 들일 것인가? [분류원문]
```

### docs/categories/robot-ontology/index.md

````markdown
---
title: "B. 로봇 온톨로지"
type: category
status: published
created: 2026-09-24
updated: 2026-09-25
version: 2
sources: [ref-003, ref-162, ref-031, ref-044, ref-148, ref-228, ref-105, ref-040, ref-153, ref-051, ref-286, ref-079, ref-023, ref-049, ref-285, ref-284, ref-282, ref-287, ref-236, ref-041, ref-014, ref-015, ref-024, ref-238, ref-239, ref-080, ref-224, ref-291, ref-290, ref-076, ref-234, ref-240, ref-138, ref-159]
---

[홈](../../index.md) › B. 로봇 온톨로지

# B. 로봇 온톨로지

## 핵심 질문

서로 다른 제조사의 로봇을 어떻게 등록하고, 할 수 있는 일을 같은 말로 표현해, 시스템과 쉽게 연결할 것인가? [분류원문]

## 개요

서로 다른 제조사의 로봇을 등록하고, 무엇을 할 수 있는지 공통 모델로 표현하고, 그 모델로 시스템과 로봇이 쉽게 연동되게 하는 온톨로지 기능 전체. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **4. 이기종 로봇 등록** | 서로 다른 제조사의 로봇을 문서 근거와 함께 등록하고, 사람이 검토·승인한다 | 제조사도 형식도 다른 로봇을 어떻게 빠르고 믿을 수 있게 등록할 것인가? | [4. 이기종 로봇 등록](heterogeneous-robot-registration.md) | published |
| **5. 로봇 능력·작업 표현** | 능력·작업 요구·환경 조건을 공통 어휘로 표현하고 기존 표준과 맞춘다 | 로봇이 할 수 있는 일과 작업이 요구하는 조건을 어떻게 같은 말로 표현할 것인가? | [5. 로봇 능력·작업 표현](robot-capability-and-task-representation.md) | published |
| **6. 온톨로지 기반 시스템·로봇 연동** | 온톨로지로 수행 가능한 로봇을 찾고, 능력을 실제 명령에 묶고, 연동 설정을 자동으로 만든다 | 온톨로지를 이용해 새 로봇과 새 시스템을 손작업 없이 어떻게 연동할 것인가? | [6. 온톨로지 기반 시스템·로봇 연동](ontology-based-system-and-robot-integration.md) | published |
| **7. 온톨로지 검증·변경 관리** | 온톨로지가 빠짐없고 정확한지 검증하고, 문서·펌웨어가 바뀔 때 버전을 관리한다 | 온톨로지가 빠짐없고 정확한지, 문서가 바뀌면 무엇을 다시 확인할지 어떻게 알 것인가? | [7. 온톨로지 검증·변경 관리](ontology-verification-and-change-management.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

같은 기능도 제조사마다 이름·매개변수·실행 조건이 다르다. **능력을 공통 모델로 표현해야** 작업에 맞는 로봇을 질의로 찾고, 새 로봇을 연동할 때 반복 작업을 줄일 수 있다. [분류원문]

## 다른 대분류와의 연결

> **이전 분류 기준 내용.** 아래는 이전 분류(7개 대분류)에서 B. 공통 정보·환경 모델 페이지에 2026-09-25 작성한 연결이다. 대분류 이름은 그때의 것이고, 링크는 새 영역 페이지로 옮겨 두었다. 새 17개 대분류 기준의 연결은 이어지는 조사에서 다시 쓴다.


이 절은 B. 공통 정보·환경 모델의 게시된 세부영역 페이지(5. 로봇 능력·작업 표현, 15. 지도·공간·위치 모델, 17. 작업 대상·자산 식별과 인계 추적, 18. 실시간 세계 상태·데이터 일관성)의 검증된 주장과 각주를 근거로, 이 대분류의 모델이 다른 대분류의 어느 세부영역과 무엇으로 이어지는지 정리한다. 연결 상대 세부영역 가운데 상당수는 아직 본문이 없으므로, 연결의 근거는 이 대분류 쪽 자료에 기댄다.

```mermaid
graph LR
  B5["5. 로봇 능력·작업 표현"]
  B6["15. 지도·공간·위치 모델"]
  B7["17. 작업 대상·자산 식별과 인계 추적"]
  B8["18. 실시간 세계 상태·데이터 일관성"]
  CatA["A. 업무·공급망 설계"]
  CatC["C. 연결·실행 기반"]
  CatD["D. 계획·최적화"]
  CatE["E. 협업·현장 운영"]
  CatF["F. 도입·검증·유지관리"]
  CatG["G. 안전·보안·지능·거버넌스"]
  B5 --> CatC
  B5 --> CatD
  B5 --> CatF
  B5 --> CatG
  B6 --> CatA
  B6 --> CatC
  B6 --> CatD
  B6 --> CatF
  B6 --> CatG
  B7 --> CatA
  B7 --> CatC
  B7 --> CatE
  B8 --> CatA
  B8 --> CatC
  B8 --> CatE
  B8 --> CatF
  B8 --> CatG
```

### [옛 A. 업무·공급망 설계](../planning-and-business/index.md)

- [15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md) ↔ [23. 업무 시스템 연동](../integration/business-system-integration.md): GS1 GLN 은 도크 문·보관 위치 같은 하위 위치를 식별할 수 있고 GLN 확장 요소는 조직 내부나 거래 당사자 간 합의로만 쓰므로, 업무 위치와 로봇 지도 장소의 대응은 ROP 쪽 대응 계층이 맡게 될 것으로 보인다. [추정][^ref-162][^ref-031] 국내 사례는 [열린 질문](../../open-questions.md) oq-029 에서 다룬다.
- [17. 작업 대상·자산 식별과 인계 추적](../objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md) ↔ [24. 작업·워크플로 모델링](../planning-and-optimization/task-and-workflow-modeling.md): GS1 CBV 는 도착(arriving)·입고(receiving)·인수(accepting)를 서로 다른 업무 단계로 정의하고, VDA 5050 은 하역(drop) 완료를 적재물이 로봇을 떠나 로봇이 새 적재 상태를 보고한 때로 정의한다. [사실][^ref-044][^ref-031] 같은 연결은 [A. 업무·공급망 설계](../planning-and-business/index.md) 페이지의 다른 대분류와의 연결 절에도 같은 각주로 실려 있다.
- [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md) ↔ [39. 운영 성과 측정·개선](../field-operations-and-monitoring/operational-performance-measurement-and-improvement.md): Open-RMF 로봇 상태 스키마는 상태(idle·charging·working·error 등), 배터리, 현재 작업 id, 문제 목록, 위치, 기록 시각을 담는다. [사실][^ref-148] 이 필드들은 가동률·충전·오류 시간 지표의 원천이 될 것으로 보인다. [추정][^ref-148] 이 연결도 [A. 업무·공급망 설계](../planning-and-business/index.md) 페이지와 같은 각주를 쓴다.

### [옛 C. 연결·실행 기반](../integration/index.md)

- [5. 로봇 능력·작업 표현](robot-capability-and-task-representation.md) ↔ [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md): VDA 5050 팩트시트는 적재 명세(loadSets: 적재 유형·최대 중량·처리 높이·픽·드롭 소요 시간)와 지원 동작(mobileRobotActions)을 선언하고, Open-RMF 플릿 어댑터 템플릿 설정은 수행 가능한 작업 유형(task_capabilities)과 동작 이름(actions)을 선언한다. [사실][^ref-228][^ref-105] 두 자료는 서로 다른 인터페이스의 사례다.
- [5. 로봇 능력·작업 표현](robot-capability-and-task-representation.md) ↔ [29. 명령·작업 실행의 신뢰성](../execution-collaboration-and-recovery/command-and-task-execution-reliability.md): 팩트시트에서 선언한 동작 이름(actionType)이 명령과 완료 보고에 그대로 쓰이고 Open-RMF 어댑터가 로봇 API 의 완료 확인 뒤 완료를 알리므로, 능력 선언이 실행 확인의 기준 어휘가 될 것으로 보인다. [추정][^ref-228][^ref-040]
- [15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md) ↔ [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md): Open-RMF 플릿 어댑터는 로봇 좌표계가 RMF 와 다르면 같은 위치를 가리키는 좌표 쌍으로 회전·축척·이동 변환을 추정하며(대응점 4개 이상 권장), 템플릿 설정은 층별 reference_coordinates 로 이 좌표 쌍을 둔다. [사실][^ref-153][^ref-105] 이 작업은 용어집의 [지도 정합](../../glossary/map-alignment.md)에 해당한다. VDA 5050 상태 스키마는 위치추정 품질(localizationScore), 편차 범위(deviationRange), 지도 식별자(mapId)를 두며, 편차를 추정할 수 없는 로봇은 편차 범위를 생략할 수 있다. [사실][^ref-051] 그래서 위치 신뢰도 보고가 제조사 구현에 따라 달라질 수 있다. [추정][^ref-051] 수용 기준은 열린 질문 oq-028 에서 다룬다.
- [15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md) ↔ [22. 설비·건물 시스템 연동](../integration/facility-and-building-system-integration.md): Open-RMF 승강기 상태는 층을 층 이름 문자열(available_floors, current_floor, destination_floor)로 나타내므로, 지도의 층 이름과 승강기의 층 이름을 맞추는 대응이 두 대분류 사이에 필요할 것으로 보인다. [추정][^ref-286][^ref-079] 이 대응 규칙은 새 열린 질문으로 올렸고, 공통 좌표계 대응(oq-027)·업무 위치 대응(oq-029)과 함께 본다.
- [17. 작업 대상·자산 식별과 인계 추적](../objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md) ↔ [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md): VDA 5050 상태 스키마의 적재물 목록(loads)은 로봇이 취급 중인 적재물을 담되 적재 상태를 판단할 수 없는 로봇은 생략할 수 있고, 적재물 식별 번호(loadId)는 바코드·RFID 같은 식별 값이며 아직 식별하지 않았으면 비워 둔다. [사실][^ref-051]
- [17. 작업 대상·자산 식별과 인계 추적](../objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md) ↔ [22. 설비·건물 시스템 연동](../integration/facility-and-building-system-integration.md): Open-RMF 배송 작업에서 로봇은 픽업 지점 워크셀에서 DispenserResult 를, 하역 지점 워크셀에서 IngestorResult 를 받을 때까지 요청을 되풀이한다. [사실][^ref-023] IngestorResult 는 시각, 요청 id, 워크셀 id, 상태(ACKNOWLEDGED·SUCCESS·FAILED)를 담는다. [사실][^ref-049]
- [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md) ↔ [22. 설비·건물 시스템 연동](../integration/facility-and-building-system-integration.md): Open-RMF 문·승강기 상태 메시지는 시각 필드(door_time, lift_time)를 담고, 승강기 어댑터는 적절하다고 판단한 요청만 승강기에 전달한다. [사실][^ref-285][^ref-286][^ref-284] 상태 발행 주기나 오래됨 판정 규칙은 이번에 연 승강기 연동 문서 범위에서는 찾지 못했다. [추정][^ref-284]
- [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md) ↔ [42. 분산 시스템·통신·컴퓨팅 구조](../platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md): ROS 2 QoS 의 기한·생존성 정책, Sparkplug 의 노드 종료(NDEATH) 뒤 지표 STALE 표시, VDA 5050 의 MQTT 유언을 통한 연결 끊김 통지처럼 통신 계층에도 상태의 오래됨을 알리는 장치가 있다. [사실][^ref-282][^ref-287][^ref-031] 세 출처는 각각 한 장치만 다룬다.

### [옛 D. 계획·최적화](../planning-and-optimization/index.md)

- [5. 로봇 능력·작업 표현](robot-capability-and-task-representation.md) ↔ [25. 작업 배정 — MRTA](../planning-and-optimization/task-allocation-mrta.md): 이종 다중 로봇 작업 배정에서 온톨로지 기반 실행 가능성 판정 결과를 배정기와 독립된 입력으로 넘기는 연구가 있다(2026-08 발행). [사실][^ref-236] 제조사가 광고한 능력과 운용 중 관측된 능력을 온톨로지로 구분해 통합하는 연구도 있어, 배정 기준을 어느 값으로 둘지가 두 대분류 사이의 쟁점이 될 것으로 보인다(열린 질문 oq-024). [추정][^ref-041]
- [15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md) ↔ [27. 다중 로봇 경로·교통 관리 — MAPF](../planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md): Open-RMF traffic-editor 로 주석한 차선·경유점 그래프는 building_map_generator 로 주행 그래프(navigation graph)로 내보내져 플릿 어댑터의 경로 계획에 쓰인다. [사실][^ref-079]
- [15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md) ↔ [28. 공용 자원·충전·에너지 최적화](../planning-and-optimization/shared-resource-charging-and-energy-optimization.md): traffic-editor 는 주차 위치·충전기 위치·승강기·문·층을 지도에 주석하게 하므로, 공용 자원의 위치 정보가 지도 모델에서 나온다. [사실][^ref-079]

### [옛 E. 협업·현장 운영](../execution-collaboration-and-recovery/index.md)

- [17. 작업 대상·자산 식별과 인계 추적](../objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md) ↔ [30. 로봇 간 협업·물리적 인계](../execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md): 설비의 인수 결과에는 화물 식별자·인계 당사자가 없고 EPCIS 는 소유·점유·위치 이전을 출발지·도착지(source/destination)로 표현하므로, 물리적 인계 확인은 17. 작업 대상·자산 식별과 인계 추적의 식별·인계 기록과 결합해야 할 것으로 보인다(열린 질문 oq-001). [추정][^ref-049][^ref-014][^ref-015]
- [17. 작업 대상·자산 식별과 인계 추적](../objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md) ↔ [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md): 팔레트 RFID 태그 판독성이 제품·포장·태그 위치·적재 패턴에 따라 달라진다는 2009년 실험 보고가 있어, 판독 실패 때 인계 보류·재스캔·사람 확인 규칙이 복구 과제로 넘어갈 것으로 보인다(열린 질문 oq-003). [추정][^ref-024]
- [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md) ↔ [38. 모니터링·이상 탐지·원인 분석](../field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md): 로봇 상태의 문제 목록·오류 상태와 설비 상태의 시각 정보를 한 세계 상태에 모으면, 지연 원인이 로봇인지 문인지 구분하는 분석이 같은 상태 기록을 쓰게 될 것으로 보인다. [추정][^ref-148][^ref-285]

### [옛 F. 도입·검증·유지관리](../verification-deployment-and-lifecycle/index.md)

- [5. 로봇 능력·작업 표현](robot-capability-and-task-representation.md) ↔ [55. 현장 조사·설치·시운전](../verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md): 매뉴얼·로봇 기술 파일을 해석해 능력 모델 초안을 만드는 일은 새 로봇 등록 때 필요한 작업이 될 것으로 보이며, 이는 분류 개정 전 원문 8장의 매뉴얼 해석 교차 규칙과 같은 방향이다. [추정][^ref-238][^ref-239] 온보딩 현장에 적용한 사례는 아직 확인하지 못했다.
- [15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md) ↔ [55. 현장 조사·설치·시운전](../verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md): 도면에서 만든 지도에는 대기 위치 같은 운영 요소와 도면–현장 편차가 자동으로 담기지 않아, 시운전 때 사람의 주석·정렬 단계가 남는 것으로 보인다(열린 질문 oq-022). [추정][^ref-079][^ref-080][^ref-224]
- [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md) ↔ [34. 시뮬레이션·예측용 디지털 트윈](../design-and-simulation/simulation-and-predictive-digital-twin.md): 제조 분야를 대상으로 한 분류 자료는 현장 상태가 한 방향으로 자동 반영되는 [디지털 섀도](../../glossary/digital-shadow.md)와 디지털 트윈을 구분하므로, 18. 실시간 세계 상태·데이터 일관성은 현재 상태 표현을, 34. 시뮬레이션·예측용 디지털 트윈은 그 표현을 복제해 가정한 미래를 실험하는 쪽을 맡는 것이 분류 원문의 구분과 맞을 것으로 보인다. [추정][^ref-291][^ref-290] 근거 자료가 물류가 아닌 제조 대상이라는 한계가 있다.

### [옛 G. 안전·보안·지능·거버넌스](../governance-law-and-society/index.md)

- [5. 로봇 능력·작업 표현](robot-capability-and-task-representation.md) ↔ [47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md): 대규모 언어 모델(Large Language Model, LLM)로 능력 온톨로지를 생성하는 연구(2024-04)와 로봇 기술 파일(URDF)에서 로봇 온톨로지를 LLM 으로 채우는 연구(2026-06)가 있다. [사실][^ref-238][^ref-239] 매뉴얼 해석의 적용 대상은 위 55. 현장 조사·설치·시운전 연결과 함께 본다.
- [15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md) ↔ [47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md): 비전 언어 모델로 평면도 지도를 해석하는 연구(2024-09)가 있어, 분류 개정 전 원문 8장 교차 규칙의 도면 해석이 두 대분류를 잇는다. [사실][^ref-076]
- [5. 로봇 능력·작업 표현](robot-capability-and-task-representation.md) ↔ [21. 상호운용 표준·적합성](../integration/interoperability-standards-and-conformance.md): 무인운반차 기술 데이터 서브모델 IDTA 02047, 서비스 로봇 모듈 공통 정보 모델 ISO 22166-201(2024-02), 국내 KS B 7321-2 같은 제조사 독립 정보 모델 표준이 있다. [사실][^ref-234][^ref-240][^ref-138] KS 부합화 여부는 열린 질문 oq-004·oq-026 에서 다룬다.
- [15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md) ↔ [21. 상호운용 표준·적합성](../integration/interoperability-standards-and-conformance.md): ISO 21423 은 산업용 이동로봇의 통신·상호운용성을 다루는 표준이다. [사실][^ref-159] 그 공통 좌표계가 제조사 지도 식별자와 어떻게 대응하는지는 아직 확인되지 않았다(열린 질문 oq-027).
- [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md) ↔ [48. 안전·위험 관리](../safety/safety-and-risk-management.md): Open-RMF 승강기 상태의 운영 모드에 사람·AGV·화재·오프라인·비상이 있으므로, 탑승 확정 전에 최신 모드를 확인하는 규칙이 안전 조건과 맞물릴 것으로 보인다. [추정][^ref-286] 여기서 ROP 는 상태를 확인하는 범위만 맡고, 설비 안전 제어 자체는 분류 원문 19장 시설·설비 제어 경계의 연계 대상이다.

### 아직 다루지 않은 연결

26. 작업 순서·스케줄링, 31. 사람–로봇 협업, 54. 시험·형식 검증·벤치마크, 57. 자산·소프트웨어 수명주기 관리, 51. 인증·권한·격리 와 이 대분류 세부영역 사이의 연결은 게시 페이지에 검증된 근거가 없어 싣지 않았다. 이 연결은 해당 세부영역 조사가 진행되면 보강한다.

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 88건이다(논문 40건 · 기사·보고서 1건 · 업체 발표 0건 · 표준·오픈소스·기관 자료 47건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-894](../../references/ref-894.md) — Nasir, F., Saeed, M. A., Ehsan, M., Ahmad, S. J., & Altaf, A. M., OntoKG-EQ: A provenance-grounded, competency-question-governed knowledge graph for auditable analyst querying (발행 2026-09-08)
- [ref-236](../../references/ref-236.md) — Electronics(MDPI) 게재 논문(저자 미확인), Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation (발행 2026-08-11)
- [ref-239](../../references/ref-239.md) — Dussard, B., & Sarthou, G. (LAAS-CNRS), Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF (발행 2026-06)
- [ref-201](../../references/ref-201.md) — Nabizada, H., Wirt, T., Vieira da Silva, L. M., Gehlhoff, F., & Fay, A., From Capability Models to Automated Planning: An AAS-Native Approach for Automatic PDDL Generation (발행 2026-06)
- [ref-898](../../references/ref-898.md) — Osmani, A., From Ontology Conformance to Admissible Reconfiguration: A RoSO/SMGI Adequacy Argument for Robotic Service Governance (발행 2026-05-05)
- [ref-896](../../references/ref-896.md) — Alharbi, R., Tamma, V., Payne, T. R., & de Berardinis, J., Characterising LLM-Generated Competency Questions: a Cross-Domain Empirical Study using Open and Closed Models (발행 2026-04-17)
- [ref-895](../../references/ref-895.md) — Abolhasani, M. S., Ba, Y., He, Y., & Pan, R. (Graph Foundation Models @ ICML 2026), Beyond Predefined Schemas: TRACE-KG for Context-Enriched Knowledge Graph Generation (발행 2026-04-03)
- [ref-041](../../references/ref-041.md) — Naqvi, M. R. 외(Scientific Reports), Ontology-driven integration of advertised and operational capabilities in robots (발행 2025-10-02)
- [ref-890](../../references/ref-890.md) — Martorana, M., Urgese, F., Tiddi, I., & Schlobach, S. (Vrije Universiteit Amsterdam), An Ontology for Unified Modeling of Tasks, Actions, Environments, and Capabilities in Personal Service Robotics (발행 2025-09-26)
- [ref-880](../../references/ref-880.md) — Ioannidou, P., Vezakis, I., Haritou, M., Petropoulou, R., Miloulis, S. T., Kouris, I., Bromis, K., Matsopoulos, G. K., & Koutsouris, D. D. (Healthcare, Basel), HEalthcare Robotics' ONtology (HERON): An Upper Ontology for Communication, Collaboration and Safety in Healthcare Robotics (발행 2025-04-30)
- 그 밖에 30건

**기사·보고서**

- [ref-870](../../references/ref-870.md) — 로봇신문, [기업 최전선을 가다-클로봇] 로봇 소프트웨어로 쓰는 ‘피지컬 AI’ 시대의 서막 (발행 2025-11-09)

**업체 발표**

- 아직 없음

**표준·오픈소스·기관 자료**

- [ref-874](../../references/ref-874.md) — OPC Foundation, OPC 40010-1: OPC UA for Robotics — Part 1: Vertical Integration (Version 1.02) (발행 2025-09-08)
- [ref-872](../../references/ref-872.md) — Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART), RoMi-H Empanelment Programme 2025 (발행 2025-05-01)
- [ref-198](../../references/ref-198.md) — IDTA(Industrial Digital Twin Association), IDTA 02047-1-0 Technical Data for AGV in Intralogistics (발행 2025-03)
- [ref-240](../../references/ref-240.md) — ISO, ISO 22166-201:2024 - Robotics — Modularity for service robots — Part 201: Common information model for modules (발행 2024-02)
- [ref-035](../../references/ref-035.md) — Plattform Industrie 4.0, Information Model for Capabilities, Skills & Services (발행 2022-11)
- [ref-026](../../references/ref-026.md) — IEEE, IEEE 1872.2-2021 - IEEE Standard for Autonomous Robotics (AuR) Ontology (발행 2022)
- [ref-044](../../references/ref-044.md) — GS1, gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0) (발행 2021-09-30)
- [ref-459](../../references/ref-459.md) — W3C RDF Data Shapes Working Group, Shapes Constraint Language (SHACL) (W3C data-shapes 저장소 편집자 초안으로 확인, 권고안(2017) 본문과 문구가 다를 수 있음) (발행 2017)
- [ref-025](../../references/ref-025.md) — IEEE, 1872-2015 - IEEE Standard Ontologies for Robotics and Automation (발행 2015)
- [ref-886](../../references/ref-886.md) — W3C (OWL Working Group), OWL 2 Web Ontology Language Structural Specification and Functional-Style Syntax (Second Edition) (발행 2012-12-11)
- 그 밖에 37건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-29 · 갱신 · [7. 온톨로지 검증·변경 관리](ontology-verification-and-change-management.md) — 영역 심화: 섹션 3~11 신규 작성(finding 27건 반영, 1차 조건부 승인 수정 13건·2차 수정 4건 이행), 프런트매터 related_areas·tags·confidence·sources·last_run 추가, version 2 (실행 2026-09-29-09)
- 2026-09-29 · 생성 · [7. 온톨로지 검증·변경 관리 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area07-s6.md) — 자동 분리: 7. 온톨로지 검증·변경 관리 의 "6. 대표 접근법과 기술" 절(2,811자)을 옮겼다 (실행 2026-09-29-09)
- 2026-09-29 · 생성 · [7. 온톨로지 검증·변경 관리 — 대표 연구와 자료](../../topics/2026/2026-09-29-area07-s8.md) — 자동 분리: 7. 온톨로지 검증·변경 관리 의 "8. 대표 연구와 자료" 절(1,834자)을 옮겼다 (실행 2026-09-29-09)
- 2026-09-29 · 생성 · [7. 온톨로지 검증·변경 관리 — 핵심 개념과 용어](../../topics/2026/2026-09-29-area07-s4.md) — 자동 분리: 7. 온톨로지 검증·변경 관리 의 "4. 핵심 개념과 용어" 절(1,478자)을 옮겼다 (실행 2026-09-29-09)
- 2026-09-29 · 생성 · [7. 온톨로지 검증·변경 관리 — 열린 질문](../../topics/2026/2026-09-29-area07-s11.md) — 자동 분리: 7. 온톨로지 검증·변경 관리 의 "11. 열린 질문" 절(1,150자)을 옮겼다. 2차 수정: 신규 질문 4번째의 태그를 진술 문장으로 옮김 (실행 2026-09-29-09)
<!-- auto:category-recent:end -->

## 참고 자료

[^ref-162]: GS1, Identifying a physical location - GLN, 미확인, https://www.gs1.org/standards/id-keys/gln/physical-location, 접근일 2026-09-25 (원문 미열람)
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-044]: GS1, gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0), 2021-09-30, https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl, 접근일 2026-09-25 (원문 미열람)
[^ref-148]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json, 접근일 2026-09-25 (원문 미열람)
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-09-25
[^ref-040]: Open Robotics, PerformAction Tutorial - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_action_tutorial.html, 접근일 2026-09-25
[^ref-153]: Open Robotics, Fleet Adapter Tutorial - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-25
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25
[^ref-286]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg, 접근일 2026-09-25
[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-25
[^ref-023]: Open Robotics, Workcells - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_workcells.html, 접근일 2026-09-25
[^ref-049]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg, 접근일 2026-09-25
[^ref-285]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_door_msgs/msg/DoorState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorState.msg, 접근일 2026-09-25
[^ref-284]: Open Robotics, Lifts (integration_lifts) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_lifts.html, 접근일 2026-09-25
[^ref-282]: Open Robotics (ROS 2 Documentation), Quality of Service settings — ROS 2 Documentation: Jazzy, 미확인, https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html, 접근일 2026-09-25 (원문 미열람)
[^ref-287]: Eclipse Foundation (eclipse-sparkplug GitHub), Sparkplug Specification — Chapter 5 Operational Behavior (Sparkplug_5_Operational_Behavior.adoc), 미확인, https://github.com/eclipse-sparkplug/sparkplug/blob/master/specification/src/main/asciidoc/chapters/Sparkplug_5_Operational_Behavior.adoc, 접근일 2026-09-25
[^ref-236]: Electronics(MDPI) 게재 논문(저자 미확인), Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation, 2026-08-11, https://doi.org/10.3390/electronics15163562, 접근일 2026-09-25 (원문 미열람)
[^ref-041]: Naqvi, M. R. 외(Scientific Reports), Ontology-driven integration of advertised and operational capabilities in robots, 2025-10-02, https://www.nature.com/articles/s41598-025-16649-3, 접근일 2026-09-25 (원문 미열람)
[^ref-014]: GS1, Core Business Vocabulary (CBV) Standard, 미확인, https://ref.gs1.org/standards/cbv/, 접근일 2026-09-25 (원문 미열람)
[^ref-015]: GS1, EPCIS and CBV Implementation Guideline, 미확인, https://www.gs1.org/docs/epc/EPCIS_Guideline.pdf, 접근일 2026-09-25 (원문 미열람)
[^ref-024]: Singh, J. 외, RFID tag readability issues with palletized loads of consumer goods, 2009, https://onlinelibrary.wiley.com/doi/abs/10.1002/pts.864, 접근일 2026-09-25 (원문 미열람)
[^ref-238]: Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A., On the Use of Large Language Models to Generate Capability Ontologies, 2024-04, https://arxiv.org/abs/2404.17524, 접근일 2026-09-25 (원문 미열람)
[^ref-239]: Dussard, B., & Sarthou, G. (LAAS-CNRS), Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF, 2026-06, https://arxiv.org/abs/2606.17073, 접근일 2026-09-25 (원문 미열람)
[^ref-080]: Open Robotics, Navigation Maps (integration_nav-maps) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_nav-maps.html, 접근일 2026-09-25 (원문 미열람)
[^ref-224]: Shaheer, M., Millan-Romera, J. A., Bavle, H., Giberna, M., Sanchez-Lopez, J. L., Civera, J., & Voos, H., Tightly Coupled SLAM with Imprecise Architectural Plans, 2024-08, https://arxiv.org/abs/2408.01737, 접근일 2026-09-25 (원문 미열람)
[^ref-291]: Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W., Digital Twin in manufacturing: A categorical literature review and classification, 2018, https://www.sciencedirect.com/science/article/pii/S2405896318316021, 접근일 2026-09-25 (원문 미열람)
[^ref-290]: NIST, DIGITAL TWINS FOR ADVANCED MANUFACTURING: THE STANDARDIZED APPROACH, 미확인, https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=957417, 접근일 2026-09-25 (원문 미열람)
[^ref-076]: DeFazio, D., Mehta, H., Wang, M., Yang, P., Blackburn, J., & Zhang, S., Vision Language Models Can Parse Floor Plan Maps, 2024-09, https://arxiv.org/abs/2409.12842, 접근일 2026-09-25 (원문 미열람)
[^ref-234]: IDTA(Industrial Digital Twin Association), IDTA 02047 Technical Data for Automated Guided Vehicles 1.0 — README (admin-shell-io/submodel-templates), 미확인, https://github.com/admin-shell-io/submodel-templates/tree/main/published/Technical%20Data%20for%20Automated%20Guided%20Vehicles, 접근일 2026-09-25 (원문 미열람)
[^ref-240]: ISO, ISO 22166-201:2024 - Robotics — Modularity for service robots — Part 201: Common information model for modules, 2024-02, https://www.iso.org/standard/82334.html, 접근일 2026-09-25 (원문 미열람)
[^ref-138]: 국가표준인증통합정보시스템(KSSN), KS B 7321-2 로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델, 미확인, https://www.kssn.net/search/stddetail.do?itemNo=K001010147546, 접근일 2026-09-25 (원문 미열람)
[^ref-159]: ISO, ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability, 미확인, https://www.iso.org/standard/86749.html, 접근일 2026-09-25 (원문 미열람)
````

### docs/categories/robot-ontology/heterogeneous-robot-registration.md (요약)

```markdown
# 4. 이기종 로봇 등록

소속 대분류: B. 로봇 온톨로지 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

서로 다른 제조사의 로봇을 문서 근거와 함께 등록하고, 사람이 검토·승인한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **이기종 로봇 등록**: 제조사·기종·펌웨어·SDK 버전·장착 장비·식별자를 가진 로봇을 플랫폼에 등록하고 등록부로 관리한다
- **기종 제원 기술**: 형상·치수·질량·구동 방식·센서·적재 한계·속도·에너지 특성을 기종 단위로 기술한다(URDF·MJCF·VDA 5050 팩트시트 등)
- **문서에서 능력 추출**: 매뉴얼·SDK·API 문서에서 능력·제약·인터페이스를 뽑아 원문 근거(절·줄·인용)와 함께 능력 정의 초안을 만든다
- **등록 검토·승인**: 추출한 능력을 사람이 원문 근거와 대조해 확정하거나 반려하고, 확인하지 못한 내용은 검토 대기로 남긴다
- **제조사 능력 정보 제공 경로**: 제조사가 능력·제약 정보를 정해진 형식으로 제공하고 갱신하는 절차와 책임을 정한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 5번 영역 ‘로봇 능력·작업 온톨로지’에서 왔다. 그 본문은 [5. 로봇 능력·작업 표현](robot-capability-and-task-representation.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

이 영역의 일부는 이전 분류(2026-09-24)의 옛 21번 영역 ‘온보딩·설정·현장 시운전’에서 왔다. 그 본문은 [55. 현장 조사·설치·시운전](../verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

제조사도 형식도 다른 로봇을 어떻게 빠르고 믿을 수 있게 등록할 것인가? [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]
```

### docs/categories/robot-ontology/robot-capability-and-task-representation.md (요약)

```markdown
# 5. 로봇 능력·작업 표현

소속 대분류: B. 로봇 온톨로지 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

능력·작업 요구·환경 조건을 공통 어휘로 표현하고 기존 표준과 맞춘다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **로봇 능력 표현**: 이동·계단·적재·도어 조작·충전·파지·점검 같은 능력을 매개변수·입출력·전제조건·제약·실패 모드와 함께 공통 모델로 표현한다
- **작업 유형·작업 요구 표현**: 배송·운반·인계·순찰·점검·조작 같은 작업 유형과 각 작업이 요구하는 능력·조건을 능력 모델과 같은 어휘로 표현한다
- **환경 조건과 능력 대조**: 층·문·승강기·계단·충전기 같은 공간 조건을 온톨로지에 함께 담아 로봇별로 지나갈 수 있는 곳과 쓸 수 있는 시설을 판단한다
- **표현 표준 정렬**: 능력·작업 표현을 로봇 온톨로지 표준(IEEE 1872 계열), VDA 5050 팩트시트, 자산 관리 셸 같은 기존 규격과 대응시킨다
- **온톨로지 저장·질의 기반**: 온톨로지를 저장하고 질의하는 기술(그래프 데이터베이스, RDF·OWL, SPARQL, JSON 스키마)을 고르고 성능을 확인한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [4. 이기종 로봇 등록](heterogeneous-robot-registration.md), [6. 온톨로지 기반 시스템·로봇 연동](ontology-based-system-and-robot-integration.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 5번 영역 ‘로봇 능력·작업 온톨로지’(옛 대분류 B. 공통 정보·환경 모델)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 제조사별 기능·제약·장착 장비·실행 조건을 공통 모델로 표현하고, 작업 요구와 연결 [옛 분류원문]

> 옛 질문: 같은 ‘운반 로봇’ 중 누가 이 화물을 실제로 취급할 수 있는가? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

로봇이 할 수 있는 일과 작업이 요구하는 조건을 어떻게 같은 말로 표현할 것인가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]
```

### docs/categories/robot-ontology/ontology-based-system-and-robot-integration.md (요약)

```markdown
# 6. 온톨로지 기반 시스템·로봇 연동

소속 대분류: B. 로봇 온톨로지 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

온톨로지로 수행 가능한 로봇을 찾고, 능력을 실제 명령에 묶고, 연동 설정을 자동으로 만든다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **능력 기반 로봇 후보 질의**: 작업 요구에 맞는 로봇 후보를 온톨로지 질의로 찾고 근거와 함께 돌려준다
- **능력–실행 연결**: 온톨로지의 능력을 실제 로봇 명령·어댑터·시뮬레이션 기능에 묶고, 검토되지 않은 연결은 실행하지 않는다
- **온톨로지 기반 연동 자동화**: 등록된 능력 모델로 어댑터 설정·명령 매핑·상태 변환 규칙의 초안을 만들어 새 로봇·새 시스템의 연동 공수를 줄인다
- **실행 시점 조건 판단**: 배터리·적재 상태·문과 승강기 상태 같은 현재 상태로 능력을 지금 실행할 수 있는지 판단한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 5번 영역 ‘로봇 능력·작업 온톨로지’에서 왔다. 그 본문은 [5. 로봇 능력·작업 표현](robot-capability-and-task-representation.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

온톨로지를 이용해 새 로봇과 새 시스템을 손작업 없이 어떻게 연동할 것인가? [분류원문]
```

### docs/categories/robot-ontology/ontology-verification-and-change-management.md (요약)

```markdown
# 7. 온톨로지 검증·변경 관리

소속 대분류: B. 로봇 온톨로지 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

온톨로지가 빠짐없고 정확한지 검증하고, 문서·펌웨어가 바뀔 때 버전을 관리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **온톨로지 검증**: 역량 질문, 원문 대조, 지원 단계 표시(문서 확인·구조화·시뮬레이션 연결·어댑터 연결·시뮬레이션 검증·실기 검증)로 완전성과 정확성을 확인한다
- **온톨로지 버전·변경 관리**: 문서·펌웨어 개정에 따라 능력 정의의 버전을 관리하고, 영향받는 작업·현장을 찾아 다시 검증한다

## 2. 핵심 질문

온톨로지가 빠짐없고 정확한지, 문서가 바뀌면 무엇을 다시 확인할지 어떻게 알 것인가? [분류원문]
```

### docs/categories/chat-based-configuration-and-operation/index.md

```markdown
---
title: "C. 채팅 기반 구성·운영"
type: category
status: seed
created: 2026-09-28
updated: 2026-09-28
version: 1
---

[홈](../../index.md) › C. 채팅 기반 구성·운영

# C. 채팅 기반 구성·운영

## 핵심 질문

맵 작성, 시나리오 구성, 로봇 구성, 실제 상황 재현, 업무 지시를 비전문 사용자가 대화만으로 할 수 있게 하려면? [분류원문]

## 개요

채팅으로 맵을 그리고, 시나리오를 구성하고, 로봇을 구성하고, 실제 상황을 시뮬레이션으로 재현하고, 업무를 지시·관리하는 대화형 기능 전체와 그 신뢰 기반. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **8. 채팅으로 맵 작성** | 대화로 층·구역·통로·문·승강기·충전 위치를 만들고 고친다 | 공간을 말로 설명하거나 도면을 올리는 것만으로 쓸 수 있는 지도를 만들 수 있는가? | [8. 채팅으로 맵 작성](chat-map-authoring.md) | published |
| **9. 채팅으로 시나리오 구성** | 대화로 할 일·물품·사람·순서·기한·실패 처리 조건을 정한다 | 할 일·사람·순서·실패 처리를 대화로 빠짐없이 정하려면 무엇을 되물어야 하는가? | [9. 채팅으로 시나리오 구성](chat-scenario-composition.md) | published |
| **10. 채팅으로 로봇 구성** | 대화로 투입 로봇의 종류·대수·장비·위치·역할을 정하고 수행 가능 여부를 확인한다 | 어떤 로봇을 몇 대, 어디에, 어떤 역할로 둘지 대화로 정하고 가능 여부를 바로 알 수 있는가? | [10. 채팅으로 로봇 구성](chat-robot-configuration.md) | published |
| **11. 채팅으로 실제 상황 시뮬레이션 재현** | 실제로 있었던 상황을 대화로 시뮬레이션에 재현하고, 재현이 실제와 얼마나 맞는지 보이며, 조건을 바꿔 비교한다 | 실제로 있었던 상황을 대화만으로 시뮬레이션에 재현하고, 조건을 바꿔 비교할 수 있는가? | [11. 채팅으로 실제 상황 시뮬레이션 재현](chat-real-situation-simulation-replay.md) | published |
| **12. 채팅으로 업무 지시·오케스트레이션** | 대화로 일을 지시하면 분해·배정·일정을 계획으로 제안하고, 승인 뒤 실행하며 진행 상황을 설명한다 | 대화로 받은 지시를 확인 가능한 계획으로 바꾸고, 승인 뒤 실행과 진행 설명까지 이어 갈 수 있는가? | [12. 채팅으로 업무 지시·오케스트레이션](chat-task-instruction-and-orchestration.md) | published |
| **13. 대화형 기능의 신뢰·기반** | 오해석 방지, 권한, 모델 연결, 입력 채널, 대화와 화면 편집의 연동, 평가처럼 대화 기능 전체를 믿고 쓰게 하는 기반 | 언어 모델의 해석이 틀려도 잘못된 실행으로 이어지지 않게 하려면 무엇을 갖춰야 하는가? | [13. 대화형 기능의 신뢰·기반](conversational-trust-and-foundations.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

대화 결과는 실행 명령이 아니라 계획이다. **사람이 확인·승인한 계획만 실행**되어야 언어 모델의 잘못된 해석이 로봇 동작으로 이어지지 않는다. [분류원문]

## 다른 대분류와의 연결

아직 작성되지 않음(에이전트가 채운다).

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 89건이다(논문 70건 · 기사·보고서 1건 · 업체 발표 2건 · 표준·오픈소스·기관 자료 16건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-819](../../references/ref-819.md) — Valerio, D., Kogler, P., Bischof, S., Hubauer, T., & Rangwala, H., Neuro-symbolic AI for Industrial Configuration (발행 2026-09-24)
- [ref-759](../../references/ref-759.md) — Ko, T.-H., & Lin, C.-T.(National Central University), Human-AI Collaboration for Multi-Line Task Adjustment Using Local Large Language Models and a Digital Twin (발행 2026-09)
- [ref-832](../../references/ref-832.md) — Xia, Y., Weyrich, M., Jazdi, N., Stümpfle, J., Sigel, J., Narla, A., Reynolds, G. K., Jawor-Baczynska, A., & Llopart, P., LLM Agents Perform Controlled Experiments Using Simulation Models (발행 2026-08-22)
- [ref-842](../../references/ref-842.md) — Tao, M., Tao, Y., & Wang, P., Intent-Driven Situation Tracking for User-Centric Multi-Turn Agents (발행 2026-08-16)
- [ref-865](../../references/ref-865.md) — Zhang, Y., Zhang, Z.-H., & Qin, H., Which Model Is Actually Serving You? IRIS: Budgeted Black-Box Auditing of Model Substitution and Routing Dilution in LLM Gateways (발행 2026-07-23)
- [ref-841](../../references/ref-841.md) — Tack, J., Laban, P., & Neville, J., LLMs Get Lost in Evolving User Intent (발행 2026-07-22)
- [ref-867](../../references/ref-867.md) — Michael, A. E., & Roesner, F., How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement (발행 2026-07-20)
- [ref-826](../../references/ref-826.md) — Ghasemloo, M., Eckman, D. J., & Li, Y., Subtrace-Conditional Validation of Simulation Models and Digital Twins (발행 2026-07-19)
- [ref-838](../../references/ref-838.md) — Valiollahi, S., Rodríguez, I., Eriksen, S. N., Zhang, W., Damsgaard, S., & Mogensen, P. (Scientific Reports), Digital twin for scenario-based design evaluation of manufacturing robotic fleets and factory layouts (발행 2026-07-18)
- [ref-833](../../references/ref-833.md) — Gao, Y., Miao, W., Piccinini, M., Wang, H., Song, Q., & Betz, J., Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving (발행 2026-07-15)
- 그 밖에 60건

**기사·보고서**

- [ref-855](../../references/ref-855.md) — OWASP GenAI Security Project, OWASP Top 10 for LLM Applications 2025 (발행 2025)

**업체 발표**

- [ref-817](../../references/ref-817.md) — 모빌리오(Mobilio), [최초 공개] 산업용 순찰 로봇, 도면 연동과 센서 관제를 웹 화면 하나로 끝내는 방법 (발행 2026-08-24)
- [ref-823](../../references/ref-823.md) — 폴라리스3D(Polaris3D), AMR 도입 ROI 어떻게 계산할까? 물류 자동화 투자 회수 기간 알아보기 (발행 2026-06-12)

**표준·오픈소스·기관 자료**

- [ref-854](../../references/ref-854.md) — Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse, Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP) (발행 2026-06-25)
- [ref-862](../../references/ref-862.md) — 개인정보보호위원회, 생성형 인공지능(AI) 개발·활용을 위한 개인정보 처리 안내서(2025.8.) (발행 2025-08)
- [ref-856](../../references/ref-856.md) — Model Context Protocol (Anthropic 주도 오픈소스 프로젝트), Specification — Model Context Protocol (2025-06-18) (발행 2025-06-18)
- [ref-863](../../references/ref-863.md) — European Commission — AI Act Service Desk, Article 12: Record-keeping (Regulation (EU) 2024/1689, Artificial Intelligence Act) (발행 2024-06-13)
- [ref-860](../../references/ref-860.md) — 과학기술정보통신부·한국정보통신기술협회(TTA), 2024 신뢰할 수 있는 인공지능 개발 안내서 — 일반분야 (일러두기) (발행 2024-02)
- [ref-851](../../references/ref-851.md) — 한국전자통신연구원(ETRI) 이준기, 박성오, 김낙우, 김은주, 고석갑 (전자통신동향분석 39(1)), 거대언어모델 기반 로봇 인공지능 기술 동향 (발행 2024-02)
- [ref-046](../../references/ref-046.md) — VDMA (Intralogistics-2X-LIF GitHub), Layout-Interchange-Format — README (Repository for the Layout Interchange Format (LIF) developed by the VDMA) (발행 2023-09)
- [ref-831](../../references/ref-831.md) — ROS 2 (ros2/rosbag2 GitHub), rosbag2 — README (Recording and playback of ROS 2 communications) (발행 미확인)
- [ref-229](../../references/ref-229.md) — IDTA(Industrial Digital Twin Association), IDTA 02020 Capability Description 1.0 — README (admin-shell-io/submodel-templates) (발행 미확인)
- [ref-125](../../references/ref-125.md) — Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_request.json (발행 미확인)
- 그 밖에 6건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-29 · 갱신 · [13. 대화형 기능의 신뢰·기반](conversational-trust-and-foundations.md) — 3~11절 신규 작성(seed → draft), 출처 19건(ref-855~ref-868 신규, ref-351·ref-840·ref-165·ref-753 재사용), 상업 시설 사례 1건, 열린 질문 4건 추가, 1차 조건부 승인 수정 7건 이행 (실행 2026-09-29-06)
- 2026-09-29 · 생성 · [13. 대화형 기능의 신뢰·기반 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area13-s6.md) — 자동 분리: 13. 대화형 기능의 신뢰·기반 의 "6. 대표 접근법과 기술" 절(3,607자)을 옮겼다 (실행 2026-09-29-06)
- 2026-09-29 · 생성 · [13. 대화형 기능의 신뢰·기반 — 대표 연구와 자료](../../topics/2026/2026-09-29-area13-s8.md) — 자동 분리: 13. 대화형 기능의 신뢰·기반 의 "8. 대표 연구와 자료" 절(1,988자)을 옮겼다 (실행 2026-09-29-06)
- 2026-09-29 · 생성 · [13. 대화형 기능의 신뢰·기반 — 열린 질문](../../topics/2026/2026-09-29-area13-s11.md) — 자동 분리: 13. 대화형 기능의 신뢰·기반 의 "11. 열린 질문" 절(1,562자)을 옮겼다 (실행 2026-09-29-06)
- 2026-09-29 · 생성 · [13. 대화형 기능의 신뢰·기반 — 핵심 개념과 용어](../../topics/2026/2026-09-29-area13-s4.md) — 자동 분리: 13. 대화형 기능의 신뢰·기반 의 "4. 핵심 개념과 용어" 절(1,495자)을 옮겼다 (실행 2026-09-29-06)
<!-- auto:category-recent:end -->
```

### docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md (요약)

```markdown
# 8. 채팅으로 맵 작성

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

대화로 층·구역·통로·문·승강기·충전 위치를 만들고 고친다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 맵 작성**: 공간을 글이나 말로 설명하거나 도면·사진을 올리면 대화로 층·구역·통로·문·승강기·충전 위치를 만들고 고친다
- **대화 중 지도 확인·확정**: 대화로 만든 지도를 화면에 보여 주고, 축척·치수·통과 조건처럼 말로 확정할 수 없는 값은 확인 질문으로 받아 확정한다

## 2. 핵심 질문

공간을 말로 설명하거나 도면을 올리는 것만으로 쓸 수 있는 지도를 만들 수 있는가? [분류원문]
```

### docs/categories/chat-based-configuration-and-operation/chat-scenario-composition.md (요약)

```markdown
# 9. 채팅으로 시나리오 구성

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

대화로 할 일·물품·사람·순서·기한·실패 처리 조건을 정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 시나리오 구성**: 할 일·물품·사람·순서·반복·기한·실패 처리 조건을 대화로 정하고, 모자란 조건은 선택지와 이유를 붙인 질문으로 채운다
- **합의 내용 보존·변경 표시**: 대화가 이어져도 이미 합의한 단계를 지우지 않고 바뀐 부분만 반영하며, 사용자가 정한 값을 모델 추정보다 우선한다

## 2. 핵심 질문

할 일·사람·순서·실패 처리를 대화로 빠짐없이 정하려면 무엇을 되물어야 하는가? [분류원문]
```

### docs/categories/chat-based-configuration-and-operation/chat-robot-configuration.md (요약)

```markdown
# 10. 채팅으로 로봇 구성

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

대화로 투입 로봇의 종류·대수·장비·위치·역할을 정하고 수행 가능 여부를 확인한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 로봇 구성**: 투입할 로봇의 종류·대수·장착 장비·초기 위치·역할을 대화로 정하고, 온톨로지로 수행 가능 여부를 확인해 알려 준다
- **로봇 구성 적합성 사전 확인**: 대화로 정한 로봇 구성이 시나리오의 작업·공간·시설 조건을 채우는지 실행 전에 확인하고 부족한 능력이나 대수를 알려 준다

## 2. 핵심 질문

어떤 로봇을 몇 대, 어디에, 어떤 역할로 둘지 대화로 정하고 가능 여부를 바로 알 수 있는가? [분류원문]
```

### docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md (요약)

```markdown
# 11. 채팅으로 실제 상황 시뮬레이션 재현

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

실제로 있었던 상황을 대화로 시뮬레이션에 재현하고, 재현이 실제와 얼마나 맞는지 보이며, 조건을 바꿔 비교한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 실제 상황 시뮬레이션 재현**: 현장에서 실제로 있었던 상황(혼잡, 고장, 승강기 대기, 사람 흐름)을 대화로 설명하거나 운영 기록을 지정하면 시뮬레이션으로 재현한다
- **대화로 조건 바꿔 비교**: 재현한 상황에서 로봇 수·경로·정책을 대화로 바꿔 다시 돌리고 결과 차이를 설명한다
- **재현 충실도 확인**: 재현한 시뮬레이션이 실제 기록(시각·위치·사건 순서)과 얼마나 맞는지 비교해 보여 주고, 맞지 않는 부분을 알려 준다

## 2. 핵심 질문

실제로 있었던 상황을 대화만으로 시뮬레이션에 재현하고, 조건을 바꿔 비교할 수 있는가? [분류원문]
```

### docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md (요약)

```markdown
# 12. 채팅으로 업무 지시·오케스트레이션

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

대화로 일을 지시하면 분해·배정·일정을 계획으로 제안하고, 승인 뒤 실행하며 진행 상황을 설명한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 업무 지시·오케스트레이션**: 상황과 처리할 일을 입력하면 업무를 파악·분해하고, 적합한 로봇 배정과 일정까지 실행 계획으로 제안한다
- **실행 전 계획 확인·승인**: 대화 결과는 실행 명령이 아니라 계획이며, 사람이 전체 계획을 확인·승인한 뒤에만 한 번 실행된다
- **채팅으로 진행 상황 질의·결과 설명**: 어디까지 했는지, 왜 멈췄는지를 대화로 묻고 실행 기록과 시각을 근거로 답을 받는다

## 2. 핵심 질문

대화로 받은 지시를 확인 가능한 계획으로 바꾸고, 승인 뒤 실행과 진행 설명까지 이어 갈 수 있는가? [분류원문]
```

### docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md (요약)

```markdown
# 13. 대화형 기능의 신뢰·기반

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

오해석 방지, 권한, 모델 연결, 입력 채널, 대화와 화면 편집의 연동, 평가처럼 대화 기능 전체를 믿고 쓰게 하는 기반 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **오해석 방지·근거 표시**: 해석의 근거(장소·물품·문서 식별자)를 보여 주고, 없는 물품이나 검토되지 않은 문·측정값을 모델이 지어내지 못하게 막는다
- **대화 권한·기록 보호**: 사용자별로 대화로 지시할 수 있는 로봇·구역·작업의 범위를 제한하고 대화 기록을 보존·보호한다
- **언어 모델 연결·교체**: 언어 모델 공급자를 고르고 바꾸며 자격 증명을 보호하고, 모델 장애 때 임의로 다른 모델로 넘기지 않는다
- **대화형 기능 평가**: 해석·분해 정확도, 배정 적합성, 질문 횟수, 구성 완료 시간 같은 지표와 시나리오 시험으로 대화 기능을 평가한다
- **대화와 화면 편집 연동**: 지도에서 고른 장소·로봇 같은 화면 선택이 대화에 그대로 반영되고, 대화로 바꾼 내용이 편집 화면에 바로 보이게 한다
- **음성·다국어·현장 단말 대화**: 현장 사람이 음성·모바일·태블릿과 여러 언어로 지시하고 질문한다

## 2. 핵심 질문

언어 모델의 해석이 틀려도 잘못된 실행으로 이어지지 않게 하려면 무엇을 갖춰야 하는가? [분류원문]
```

### docs/categories/space-and-map-model/index.md

```markdown
---
title: "D. 공간·지도 모델"
type: category
status: seed
created: 2026-09-28
updated: 2026-09-28
version: 1
---

[홈](../../index.md) › D. 공간·지도 모델

# D. 공간·지도 모델

## 핵심 질문

로봇마다 다른 지도와 건물 도면을 어떻게 하나의 공간으로 만들고 유지할 것인가? [분류원문]

## 개요

건물 도면·센서 지도·좌표계를 하나의 공간 모델로 만들고, 장소에 의미를 붙이고, 바뀔 때 관리하는 일. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **14. 도면·BIM에서 지도 만들기** | 평면도·BIM에서 공간과 시설을 인식해 지도 초안을 만들고 현장과 맞춘다 | 이미 있는 도면과 건물 모델에서 로봇이 쓸 지도를 얼마나 자동으로 만들 수 있는가? | [14. 도면·BIM에서 지도 만들기](maps-from-floor-plans-and-bim.md) | published |
| **15. 지도·공간·위치 모델** | 로봇마다 다른 지도·좌표·층을 하나의 공간 모델로 통합하고 위치 신뢰도를 관리한다 | 제조사마다 다른 지도·좌표·층을 어떻게 하나의 공간으로 맞출 것인가? | [15. 지도·공간·위치 모델](map-space-and-location-model.md) | published |
| **16. 장소 의미·지도 관리** | 장소에 이름·용도를 붙이고, 지도를 편집하고, 바뀔 때 버전을 관리한다 | 같은 장소를 모두가 같은 이름으로 부르고, 공간이 바뀌면 지도를 어떻게 따라 바꿀 것인가? | [16. 장소 의미·지도 관리](place-semantics-and-map-management.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

지도는 한 번 만들고 끝나지 않는다. **현장과 도면의 차이 확인(14번), 좌표 정렬과 위치추정 신뢰도(15번), 지도 버전 관리(16번)**가 함께 필요하다. [분류원문]

## 다른 대분류와의 연결

아직 작성되지 않음(에이전트가 채운다).

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 54건이다(논문 20건 · 기사·보고서 2건 · 업체 발표 1건 · 표준·오픈소스·기관 자료 31건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-163](../../references/ref-163.md) — 노주형, 강규리, 김연찬, 심현철(로봇학회 논문지), 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템 (발행 2026)
- [ref-1018](../../references/ref-1018.md) — Xie, F., Schwertfeger, S., & Blum, H. (RA-L 2026 채택, arXiv), osmAG-LLM: Zero-Shot Open-Vocabulary Object Navigation via Semantic Maps and Large Language Models Reasoning (발행 2025-07)
- [ref-083](../../references/ref-083.md) — Zhang, J. 외, Generation of Indoor Open Street Maps for Robot Navigation from CAD Files (발행 2025-07)
- [ref-161](../../references/ref-161.md) — Abdul Hafez, O., Joerger, M., & Spenko, M., Quantifying mobile robot localization safety for an EKF-based SLAM estimator: An integrity monitoring approach (발행 2025-05)
- [ref-073](../../references/ref-073.md) — Luo, R. 외, ArchCAD-400K: A Large-Scale CAD drawings Dataset and New Baseline for Panoptic Symbol Spotting (발행 2025-03)
- [ref-160](../../references/ref-160.md) — Prakhya, S. M., Yang, L., & Liu, Z., Lifelong 3D Mapping Framework for Hand-held & Robot-mounted LiDAR Mapping Systems (발행 2025-01)
- [ref-076](../../references/ref-076.md) — DeFazio, D., Mehta, H., Wang, M., Yang, P., Blackburn, J., & Zhang, S., Vision Language Models Can Parse Floor Plan Maps (발행 2024-09)
- [ref-224](../../references/ref-224.md) — Shaheer, M., Millan-Romera, J. A., Bavle, H., Giberna, M., Sanchez-Lopez, J. L., Civera, J., & Voos, H., Tightly Coupled SLAM with Imprecise Architectural Plans (발행 2024-08)
- [ref-221](../../references/ref-221.md) — Vega Torres, M. A., Braun, A., & Borrmann, A., BIM-SLAM: Integrating BIM Models in Multi-session SLAM for Lifelong Mapping using 3D LiDAR (발행 2024-08)
- [ref-078](../../references/ref-078.md) — Kratochvila, L., de Jong, G., Arkesteijn, M., Zemcik, T., Bilik, S., Horak, K., & Rellermeyer, J. S., Multi-Unit Floor Plan Recognition and Reconstruction Using Improved Semantic Segmentation of Raster-Wise Floor Plans (발행 2024-08)
- 그 밖에 10건

**기사·보고서**

- [ref-956](../../references/ref-956.md) — 지디넷코리아 (김성현), 네이버 제2사옥, 로봇 친화형 건축물 인증 획득 (발행 2022-04-11)
- [ref-1013](../../references/ref-1013.md) — 엔지니어링데일리, "설계부터 100% 도입" 건설산업 BIM 활성화 로드맵 공개 (발행 2020-12-28)

**업체 발표**

- [ref-817](../../references/ref-817.md) — 모빌리오(Mobilio), [최초 공개] 산업용 순찰 로봇, 도면 연동과 센서 관제를 웹 화면 하나로 끝내는 방법 (발행 2026-08-24)

**표준·오픈소스·기관 자료**

- [ref-071](../../references/ref-071.md) — Agour, M. 외 (ResPlan), ResPlan — README (ResPlan: A Large-Scale Vector-Graph Dataset of 17,000 Residential Floor Plans) (발행 2025-08)
- [ref-158](../../references/ref-158.md) — ISO, ISO 19164:2024 - Geographic information — Indoor feature model (발행 2024)
- [ref-070](../../references/ref-070.md) — Hu, S. 외, Raster-to-Graph — README (Raster-to-Graph: Floorplan Recognition via Autoregressive Graph Prediction with an Attention Transformer) (발행 2024)
- [ref-046](../../references/ref-046.md) — VDMA (Intralogistics-2X-LIF GitHub), Layout-Interchange-Format — README (Repository for the Layout Interchange Format (LIF) developed by the VDMA) (발행 2023-09)
- [ref-1012](../../references/ref-1012.md) — AI Hub (한국지능정보사회진흥원) — 구축 주관 에이치씨아이플러스(주), 건축 도면 데이터 (발행 2023-07-26)
- [ref-069](../../references/ref-069.md) — Pizarro, P. N., Hitschfeld, N., & Sipiran, I. (MLSTRUCT), MLStructFP — README (Large-scale multi-unit floor plan dataset for architectural plan analysis and recognition) (발행 2023)
- [ref-1016](../../references/ref-1016.md) — Open Geospatial Consortium (OGC), Indoor Mapping Data Format (1.0.0) — OGC Community Standard 20-094 (발행 2021-02-18)
- [ref-066](../../references/ref-066.md) — FloorPlanCAD 프로젝트(Fan, Z. 외), FloorPlanCAD Dataset — project page (floorplancad.github.io index.md) (발행 2021)
- [ref-064](../../references/ref-064.md) — Zeng, Z., Li, X., Yu, Y. K., & Fu, C.-W., DeepFloorplan — README (Deep Floor Plan Recognition using a Multi-task Network with Room-boundary-Guided Attention) (발행 2019)
- [ref-065](../../references/ref-065.md) — Liu, C., Wu, J., Kohli, P., & Furukawa, Y., FloorplanTransformation — README (Raster-to-Vector: Revisiting Floorplan Transformation) (발행 2017)
- 그 밖에 21건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-30 · 갱신 · [16. 장소 의미·지도 관리](place-semantics-and-map-management.md) — 영역 심화: 3~11절 신규 작성(병원·가정·기타 적용 사례, 장소 목록·지도 버전·구역 집합·차선 폐쇄, 책임 경계, 연결 14개 영역, 열린 질문 9건), 13절 각주, 프런트매터 갱신. 2차 수정: 8절 첫 문장을 이번 브리프 자료 범위로 한정하고 ref-1017 각주 정의 추가 (실행 2026-09-30-04)
- 2026-09-30 · 생성 · [16. 장소 의미·지도 관리 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area16-s6.md) — 자동 분리: 16. 장소 의미·지도 관리 의 "6. 대표 접근법과 기술" 절(2,190자)을 옮겼다 (실행 2026-09-30-04)
- 2026-09-30 · 생성 · [16. 장소 의미·지도 관리 — 열린 질문](../../topics/2026/2026-09-30-area16-s11.md) — 자동 분리: 16. 장소 의미·지도 관리 의 "11. 열린 질문" 절(1,766자)을 옮겼다 (실행 2026-09-30-04)
- 2026-09-30 · 생성 · [16. 장소 의미·지도 관리 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area16-s7.md) — 자동 분리: 16. 장소 의미·지도 관리 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,125자)을 옮겼다 (실행 2026-09-30-04)
- 2026-09-30 · 생성 · [16. 장소 의미·지도 관리 — 대표 연구와 자료](../../topics/2026/2026-09-30-area16-s8.md) — 자동 분리: 16. 장소 의미·지도 관리 의 "8. 대표 연구와 자료" 절을 옮겼다. 2차 수정: 1절·3절 첫 문장을 이번 브리프 자료 범위로 한정 (실행 2026-09-30-04)
<!-- auto:category-recent:end -->
```

### docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md (요약)

```markdown
# 14. 도면·BIM에서 지도 만들기

소속 대분류: D. 공간·지도 모델 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

평면도·BIM에서 공간과 시설을 인식해 지도 초안을 만들고 현장과 맞춘다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **도면 인식**: 평면도(PDF·이미지·CAD)에서 벽·문·승강기·계단·충전 위치를 인식해 층별 지도와 공용 자원 목록의 초안을 만든다
- **BIM·CAD 가져오기**: IFC 같은 건물 정보 모델에서 공간과 시설을 가져온다
- **축척 보정·도면–현장 정합**: 도면 픽셀을 미터로 보정하고, 도면과 센서 지도·현장의 차이를 확인해 맞춘다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 6번 영역 ‘지도·공간·위치 모델’에서 왔다. 그 본문은 [15. 지도·공간·위치 모델](map-space-and-location-model.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

이미 있는 도면과 건물 모델에서 로봇이 쓸 지도를 얼마나 자동으로 만들 수 있는가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

> 원문 주석: 지도는 한 번 만들고 끝나지 않는다. **현장과 도면의 차이 확인(14번), 좌표 정렬과 위치추정 신뢰도(15번), 지도 버전 관리(16번)**가 함께 필요하다. [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]
```

### docs/categories/space-and-map-model/map-space-and-location-model.md (요약)

```markdown
# 15. 지도·공간·위치 모델

소속 대분류: D. 공간·지도 모델 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

로봇마다 다른 지도·좌표·층을 하나의 공간 모델로 통합하고 위치 신뢰도를 관리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **로봇별 지도·좌표계 정렬**: 제조사마다 다른 지도·좌표계·층 표현을 하나의 공통 좌표로 맞춘다
- **다층·수직 이동 모델**: 층·승강기·계단·경사로의 연결과 통과 조건을 모델링한다
- **공간 그래프**: 이동 가능한 공간을 노드·연결·통과 조건의 그래프로 표현한다(IndoorGML 등)
- **위치추정 신뢰도 관리**: 로봇이 보고한 위치를 얼마나 믿을 수 있는지 판단하고 오류를 감지한다
- **실외·광역 지도**: GIS·도로망·위성 위치를 실내 지도와 이어 붙인다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [14. 도면·BIM에서 지도 만들기](maps-from-floor-plans-and-bim.md), [16. 장소 의미·지도 관리](place-semantics-and-map-management.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 6번 영역 ‘지도·공간·위치 모델’(옛 대분류 B. 공통 정보·환경 모델)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: BIM·CAD·센서 지도에서 이동 공간과 경로를 만들고, 로봇별 좌표계·층·목적지를 정렬 [옛 분류원문]

> 옛 질문: 제조사마다 다른 지도에서 ‘3층 출하 대기장’을 어떻게 동일한 장소로 인식할까? [옛 분류원문]

> 옛 원문 주석: 6번에는 지도 생성뿐 아니라 **현장과 도면의 차이 확인, 지도 버전 관리, 위치추정 결과의 신뢰도**도 포함해야 한다. [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

제조사마다 다른 지도·좌표·층을 어떻게 하나의 공간으로 맞출 것인가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

> 원문 주석: 지도는 한 번 만들고 끝나지 않는다. **현장과 도면의 차이 확인(14번), 좌표 정렬과 위치추정 신뢰도(15번), 지도 버전 관리(16번)**가 함께 필요하다. [분류원문]
```

### docs/categories/space-and-map-model/place-semantics-and-map-management.md (요약)

```markdown
# 16. 장소 의미·지도 관리

소속 대분류: D. 공간·지도 모델 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

장소에 이름·용도를 붙이고, 지도를 편집하고, 바뀔 때 버전을 관리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **장소 의미·이름**: 구역·방·목적지에 이름·별칭·용도를 붙여 업무와 대화에서 같은 장소를 같은 이름으로 가리키게 한다
- **지도 버전·변경 관리**: 배치 변경과 임시 통제 구역을 지도에 반영하고 지도 버전을 관리한다
- **지도·환경 편집기**: 사람이 직접 공간과 시설을 그리고 고치는 편집 화면을 제공한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 6번 영역 ‘지도·공간·위치 모델’에서 왔다. 그 본문은 [15. 지도·공간·위치 모델](map-space-and-location-model.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

같은 장소를 모두가 같은 이름으로 부르고, 공간이 바뀌면 지도를 어떻게 따라 바꿀 것인가? [분류원문]

> 원문 주석: 지도는 한 번 만들고 끝나지 않는다. **현장과 도면의 차이 확인(14번), 좌표 정렬과 위치추정 신뢰도(15번), 지도 버전 관리(16번)**가 함께 필요하다. [분류원문]
```

### docs/categories/objects-people-and-live-state/index.md

````markdown
---
title: "E. 사물·사람·실시간 상태"
type: category
status: published
created: 2026-09-28
updated: 2026-10-09
version: 2
sources: [ref-003, ref-014, ref-015, ref-023, ref-024, ref-031, ref-041, ref-044, ref-045, ref-049, ref-051, ref-104, ref-148, ref-162, ref-228, ref-282, ref-285, ref-286, ref-287, ref-290, ref-291, ref-292, ref-492, ref-854, ref-1079, ref-1128, ref-1171, ref-1172, ref-1173, ref-1177, ref-1178, ref-1179, ref-1180, ref-1181, ref-1182, ref-1214, ref-1299, ref-1300, ref-1301, ref-1302]
---

[홈](../../index.md) › E. 사물·사람·실시간 상태

# E. 사물·사람·실시간 상태

## 핵심 질문

작업 대상·사람·설비·로봇이 지금 어디에 어떤 상태로 있는지 어떻게 믿을 수 있게 알 것인가? [분류원문]

## 개요

작업 대상과 자산의 식별·인계, 현장의 사람, 로봇·설비·공간의 현재 상태를 믿을 수 있게 관리하는 일. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **17. 작업 대상·자산 식별과 인계 추적** | 물품·자산·도구 같은 작업 대상의 식별·위치·인계 책임을 추적하고, 사람에게 넘길 때 수령인을 확인한다 | 로봇이 도착했을 때 실제로 무엇이 누구에게 넘겨졌는지 어떻게 확인할 것인가? | [17. 작업 대상·자산 식별과 인계 추적](work-object-and-asset-identification-and-handover-tracking.md) | published |
| **18. 실시간 세계 상태·데이터 일관성** | 로봇·설비·공간·물품의 현재 상태를 통합하고, 관측의 신선도·신뢰도를 관리한다 | 조금 전에 받은 상태 정보를 지금의 판단에 믿고 써도 되는가? | [18. 실시간 세계 상태·데이터 일관성](real-time-world-state-and-data-consistency.md) | published |
| **19. 사람·보행자 모델** | 현장 사람의 위치·흐름·혼잡을 모델링해 계획과 안전에 쓴다 | 현장 사람의 위치와 흐름을 어떻게 알고 계획과 안전에 반영할 것인가? | [19. 사람·보행자 모델](people-and-pedestrian-model.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

**17번은 특히 빠뜨리기 쉽다.** 로봇 위치를 추적하는 것과 작업 대상의 위치·인계 책임을 추적하는 것은 다르다. GS1 EPCIS는 제품·자산의 상태, 위치, 이동, 인계에 관한 이벤트를 공유하는 참고 표준이다. [3] [분류원문]

## 다른 대분류와의 연결

이 절은 E. 사물·사람·실시간 상태의 세 세부영역([17. 작업 대상·자산 식별과 인계 추적](work-object-and-asset-identification-and-handover-tracking.md), [18. 실시간 세계 상태·데이터 일관성](real-time-world-state-and-data-consistency.md), [19. 사람·보행자 모델](people-and-pedestrian-model.md))이 다른 대분류의 어느 세부영역과 무엇을 주고받는지 정리한다. 근거는 게시된 세부영역 페이지와 다른 대분류 페이지의 검증된 주장, 그리고 대분류 연결 실행 2026-10-09-03 의 조사다.

연결의 절반 가까이가 추정이고 사실 주장도 모두 단일 출처라 교차 확인이 없으므로, 각 문장의 태그를 함께 읽어야 한다. 아래 모든 연결에서 18. 실시간 세계 상태·데이터 일관성은 현재 상태를 표현하고, 34. 시뮬레이션·예측용 디지털 트윈은 가정한 미래를 실험한다는 구분을 지킨다.

```mermaid
flowchart LR
  e17["17. 작업 대상·자산 식별과 인계 추적"]
  e18["18. 실시간 세계 상태·데이터 일관성"]
  e19["19. 사람·보행자 모델"]
  catB["B. 로봇 온톨로지"]
  catC["C. 채팅 기반 구성·운영"]
  catD["D. 공간·지도 모델"]
  catF["F. 연동"]
  catG["G. 계획·최적화"]
  catH["H. 실행·협업·예외 복구"]
  catI["I. 설계·시뮬레이션"]
  catJ["J. 현장 운영·관제"]
  catK["K. 플랫폼 아키텍처·인프라"]
  catL["L. AI·학습 기술"]
  catM["M. 안전"]
  catN["N. 보안·개인정보"]
  catO["O. 검증·도입·수명주기"]
  catP["P. 거버넌스·법규·사회"]
  catQ["Q. 현장 유형별 적용"]
  e17 --- catB
  e17 --- catD
  e17 --- catF
  e17 --- catG
  e17 --- catH
  e17 --- catK
  e17 --- catN
  e17 --- catP
  e18 --- catB
  e18 --- catC
  e18 --- catD
  e18 --- catF
  e18 --- catG
  e18 --- catH
  e18 --- catI
  e18 --- catJ
  e18 --- catK
  e18 --- catM
  e19 --- catC
  e19 --- catD
  e19 --- catG
  e19 --- catH
  e19 --- catI
  e19 --- catL
  e19 --- catM
  e19 --- catN
  e19 --- catO
  e19 --- catP
  e19 --- catQ
```

### [B. 로봇 온톨로지](../robot-ontology/index.md)

- **17. 작업 대상·자산 식별과 인계 추적 ↔ [5. 로봇 능력·작업 표현](../robot-ontology/robot-capability-and-task-representation.md)**: VDA 5050 팩트시트가 로봇이 취급할 수 있는 적재 유형을 선언하고 상태 메시지의 loadId 가 실제로 실린 적재물을 식별하므로, '이 로봇이 이 적재물을 다룰 수 있는가'를 판단하려면 능력 표현의 적재 유형과 적재물 식별을 같은 어휘로 맞춰야 할 것으로 보이며 공통 어휘는 확인되지 않았다(oq-023). [추정][^ref-228][^ref-051]
- **18. 실시간 세계 상태·데이터 일관성 ↔ 5. 로봇 능력·작업 표현**: Naqvi 외(Scientific Reports, 2025-10-02)는 제조 분야를 대상으로 한 로봇 능력 온톨로지(RCO)에서 제조사가 공개한 능력 수치와 운용 중 로봇이 실제로 보인 성능을 구분해 연결한다(원문 미열람, 검색 결과 기준). [사실][^ref-041]
- **18. 실시간 세계 상태·데이터 일관성 ↔ [6. 온톨로지 기반 시스템·로봇 연동](../robot-ontology/ontology-based-system-and-robot-integration.md)**: 18. 실시간 세계 상태·데이터 일관성이 모은 로봇의 관측 상태(배터리·문제 목록·위치)는 능력의 '지금 실행 가능 여부' 판단과 운용 능력 갱신의 입력이 될 것으로 보이며, 선언 능력과 관측 능력 가운데 무엇을 배정 기준으로 삼을지는 열린 질문 oq-024 로 남아 있다. [추정][^ref-041][^ref-148]

### [C. 채팅 기반 구성·운영](../chat-based-configuration-and-operation/index.md)

C. 채팅 기반 구성·운영의 업무 지시는 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링을, 실제 상황 재현은 33. 시나리오 모델·편집·36. 가상 시운전·실제 상황 재현을 엔진으로 쓴다. 그래서 아래 연결은 G. 계획·최적화와 I. 설계·시뮬레이션 연결과 함께 읽는다.

- **18. 실시간 세계 상태·데이터 일관성 ↔ [12. 채팅으로 업무 지시·오케스트레이션](../chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md)**: Open Robotics 상호운용 SIG 의 2026-07-02 발표 안내문(2026-06-25 게시)은 Nayantra 를, Open-RMF REST API 를 언어 모델이 호출할 수 있는 도구로 노출하는 모델 컨텍스트 프로토콜(Model Context Protocol, MCP) 서버와 평이한 영어 지시를 여러 단계의 RMF 임무로 바꿔 Open-RMF 를 거쳐 Nav2 로 보내는 에이전트로 이루어진 시스템으로 소개했다(시연은 Isaac Sim 창고 시뮬레이션이며 발표 내용 자체는 열람하지 않았다). [사실][^ref-854] 대화로 '어디까지 했는가·왜 멈췄는가'에 답하려면 로봇 상태의 시각·상태 값·문제 목록 같은 현재 상태 기록을 근거로 써야 할 것으로 보이나, 안내문에는 상태 질의 기능이 나오지 않아 이 연동이 상태 질의까지 제공하는지는 확인하지 못했다. [추정][^ref-854][^ref-148]
- **19. 사람·보행자 모델 ↔ [11. 채팅으로 실제 상황 시뮬레이션 재현](../chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md)·[36. 가상 시운전·실제 상황 재현](../design-and-simulation/virtual-commissioning-and-real-situation-replay.md)**: 실제 운영 기록을 재생해 상황을 재현하면 기록된 사람이 바뀐 조건(로봇 수·배차 정책)에 반응하지 않는 문제가 생기며, 19. 사람·보행자 모델 페이지는 이를 열린 질문 oq-256 으로 두고 기록 재현 시뮬레이터 Waymax 와 사람 행동 시뮬레이터 HuNavSim 을 참고로 든다. [추정][^ref-1128][^ref-1179]

### [D. 공간·지도 모델](../space-and-map-model/index.md)

- **18. 실시간 세계 상태·데이터 일관성 ↔ [15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md)**: VDA 5050 상태 스키마에는 위치추정 품질(localizationScore), 미터 단위 위치 편차 범위(deviationRange), 지도 식별자(mapId)가 있으며, 앞의 두 필드는 선택 필드이고 스키마는 이를 기록·시각화 용도로만 둔다고 적는다. [사실][^ref-051] 이 값을 보고된 위치를 얼마나 믿을지 판단하는 데 쓰는 것은 스키마가 정한 용도가 아니라 ROP 쪽 설계 판단이 될 것으로 보이며, 제조사마다 다른 계산 방식을 같은 기준으로 다루는 방법은 열린 질문 oq-028 이다. [추정][^ref-051]
- **17. 작업 대상·자산 식별과 인계 추적 ↔ 15. 지도·공간·위치 모델·[16. 장소 의미·지도 관리](../space-and-map-model/place-semantics-and-map-management.md)**: GS1 GLN 이 도크 문·보관 위치 같은 하위 위치를 식별할 수 있으므로, 인계 이벤트의 업무 위치와 로봇 지도 위 장소를 대응시키는 계층이 ROP 쪽에 필요할 것으로 보이며 국내 적용 사례는 확인되지 않았다(oq-029). [추정][^ref-162][^ref-031] 같은 연결은 [B. 로봇 온톨로지](../robot-ontology/index.md) 페이지의 연결 절에도 있다.
- **19. 사람·보행자 모델 ↔ 15. 지도·공간·위치 모델**: [움직임 지도](../../glossary/maps-of-dynamics.md)(maps of dynamics)는 공간에 사람의 전형적 움직임 패턴을 덧붙인 지도이며, EU ILIAD 프로젝트는 학습한 사람 흐름에 맞춰 물류창고 자율 지게차의 경로를 계획했다. [사실][^ref-1171][^ref-1180]
- **19. 사람·보행자 모델 ↔ 16. 장소 의미·지도 관리**: 병원 현장에서 한림대학교성심병원은 밤에 인식한 경로가 낮 혼잡에서는 원활하지 않을 수 있다고 보고 로봇 통행 경로와 작업 정지 지점을 전용 스티커로 표시했다(2024-07-12 기사 1건 기준). [사실][^ref-1181]

### [F. 연동](../integration/index.md)

- **17. 작업 대상·자산 식별과 인계 추적 ↔ [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md)**: VDA 5050 상태 스키마의 loads 는 로봇이 현재 취급 중인 적재물을 담고, loadId 는 바코드·RFID 같은 적재물 식별 번호, loadPosition 은 어느 적재 장치를 쓰는지를 나타낸다. [사실][^ref-051]
- **17. 작업 대상·자산 식별과 인계 추적 ↔ [22. 설비·건물 시스템 연동](../integration/facility-and-building-system-integration.md)**: Open-RMF 배송 작업에서 로봇은 픽업 지점의 DispenserResult, 하역 지점의 IngestorResult 를 받을 때까지 요청을 되풀이하고, IngestorResult 는 시각·요청 id·워크셀 id·상태(ACKNOWLEDGED·SUCCESS·FAILED)를 담는다. [사실][^ref-023][^ref-049] 설비의 인수 결과에는 화물 식별자·인계 당사자가 없으므로 설비 쪽 SUCCESS 를 식별·인계 기록과 결합해야 '무엇이 누구에게 넘겨졌는지'가 확정될 것으로 보이며, 이를 정한 표준 매핑은 확인되지 않았다(oq-001, oq-061). [추정][^ref-049][^ref-014][^ref-015] 같은 연결은 [B. 로봇 온톨로지](../robot-ontology/index.md)·[F. 연동](../integration/index.md) 페이지의 연결 절에도 있다.
- **17. 작업 대상·자산 식별과 인계 추적·18. 실시간 세계 상태·데이터 일관성 ↔ [23. 업무 시스템 연동](../integration/business-system-integration.md)**: DeHoratius·Raman(2008)은 한 소매업체 37개 매장 재고 기록의 65%가 실물과 맞지 않았다고 보고했다(한 소매업체 37개 매장 조건이며 물류센터 값이 아니다). [사실][^ref-292] 로봇이 보고한 적재물 식별 결과와 창고 관리 시스템(Warehouse Management System, WMS) 재고 기록이 어긋나면 덮어쓰지 않고 두 기록을 함께 보관해 정정 이벤트로 업무 시스템에 되돌리는 것이 두 대분류가 넘겨받는 지점이 될 것으로 보이며, 어느 쪽을 기준으로 삼고 누가 정정하는지는 열린 질문 oq-036 이다. [추정][^ref-292][^ref-051][^ref-492]
- **18. 실시간 세계 상태·데이터 일관성 ↔ 22. 설비·건물 시스템 연동**: Open-RMF 문 상태 메시지(DoorState)는 생성 시각 door_time·문 이름·현재 모드를, 승강기 상태 메시지(LiftState)는 생성 시각 lift_time·현재 층·목적 층·문 상태·운행 상태·현재 모드·제어 세션 id 를 담으며, 두 메시지 모두 허용 경과 시간은 정하지 않는다(몇 초까지 믿을지는 oq-034). [사실][^ref-285][^ref-286] 같은 연결은 [F. 연동](../integration/index.md) 페이지의 연결 절에도 있다.
- **18. 실시간 세계 상태·데이터 일관성 ↔ 20. 로봇·제조사 관제 연동**: Open-RMF 로봇 상태는 밀리초 단위 유닉스 시각(unix_millis_time), 7종 상태 값, 0~1 범위 배터리, 운영자가 풀어야 할 문제 목록(issues)을 담고, VDA 5050 상태는 ISO 8601 형식 시각(timestamp)을 담는다. [사실][^ref-148][^ref-051] 관제 인터페이스마다 시각 표현과 보고 주기가 달라 20. 로봇·제조사 관제 연동의 어댑터가 받은 상태를 공통 시간축으로 옮기는 변환·시계 오차 기준이 필요할 것으로 보이나, 이를 규정한 자료는 확인하지 못했다(oq-035). [추정][^ref-148][^ref-051]

### [G. 계획·최적화](../planning-and-optimization/index.md)

- **17. 작업 대상·자산 식별과 인계 추적 ↔ [24. 작업·워크플로 모델링](../planning-and-optimization/task-and-workflow-modeling.md)**: GS1 CBV 는 도착(arriving)·입고(receiving)·인수(accepting)를 서로 다른 업무 단계로 정의하고(2021-09-30 온톨로지 파일 기준), VDA 5050 은 하역(drop) 완료를 적재물이 로봇을 떠나 로봇이 새 적재 상태를 보고한 때로 정의한다. [사실][^ref-044][^ref-031] 같은 연결은 [A. 기획·사업](../planning-and-business/index.md)·[B. 로봇 온톨로지](../robot-ontology/index.md) 페이지의 연결 절에도 있다.
- **18. 실시간 세계 상태·데이터 일관성 ↔ [28. 공용 자원·충전·에너지 최적화](../planning-and-optimization/shared-resource-charging-and-energy-optimization.md)**: Open-RMF 로봇 상태는 배터리를 0.0(빈)~1.0(가득)으로, VDA 5050 상태는 충전 상태(powerSupply.stateOfCharge)를 퍼센트로 보고한다. [사실][^ref-148][^ref-051] Open-RMF 가 작업을 끝낼 충전량이 부족하면 충전 작업을 일정에 끼워 넣으므로, 충전 계획은 18. 실시간 세계 상태·데이터 일관성이 표현하는 현재 배터리 상태를 단위를 맞춰 입력으로 쓰는 것으로 보이며, 이는 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈과 구분된다. [추정][^ref-104][^ref-148] 같은 연결은 [G. 계획·최적화](../planning-and-optimization/index.md) 페이지의 연결 절에도 있다.
- **19. 사람·보행자 모델 ↔ [27. 다중 로봇 경로·교통 관리 — MAPF](../planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md)**: 기타 현장(대학 건물)에서 Vintr 외(2022)는 장기 시공간 보행자 흐름 지도를 경로 계획에 쓰고 예상 조우와 예상 경로 길이로 비교했으며, 현장 실험에서 불편을 드러낸 사람은 예측형 주행에서 두 세션 모두 0명, 반응형에서 2명·1명이었다(40분 세션 4회의 매우 작은 표본). [사실][^ref-1178]
- **19. 사람·보행자 모델 ↔ [26. 작업 순서·스케줄링](../planning-and-optimization/task-sequencing-and-scheduling.md)**: 낮 시간 복도 혼잡과 '무조건 대기' 규칙(병원), 혼잡을 예상해 위치를 정하는 계획(쇼핑몰 연구)처럼 사람 흐름은 로봇 작업 시간과 순서에 영향을 줄 것으로 보이나, 시간대별 혼잡을 작업 시간 추정·스케줄링에 넣어 효과를 측정한 현장 연구는 확인하지 못했다(oq-273). [추정][^ref-1181][^ref-1182]

### [H. 실행·협업·예외 복구](../execution-collaboration-and-recovery/index.md)

- **17. 작업 대상·자산 식별과 인계 추적 ↔ [30. 로봇 간 협업·물리적 인계](../execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md)**: EPCIS 가 소유·점유·위치 이전을 출발지·도착지(source/destination)로 표현하므로, 로봇·설비 사이 물리적 인계의 확인은 식별자·인계 당사자 기록과 결합해야 할 것으로 보인다(oq-001, oq-006). [추정][^ref-049][^ref-014][^ref-015] 같은 연결은 [B. 로봇 온톨로지](../robot-ontology/index.md) 페이지의 연결 절에도 있다.
- **17. 작업 대상·자산 식별과 인계 추적 ↔ [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md)**: 팔레트 RFID 태그 판독성이 제품·포장·태그 위치·적재 패턴에 따라 달라진다는 2009년 실험 보고가 있어, 판독 실패·오판독 때 인계 보류·재스캔·사람 확인 규칙이 복구 과제로 넘어갈 것으로 보인다(oq-003). [추정][^ref-024] 같은 연결은 [B. 로봇 온톨로지](../robot-ontology/index.md) 페이지의 연결 절에도 있다. EPCIS 1.2 는 이미 기록된 이벤트를 오류 선언(errorDeclaration)으로 정정하게 하므로, 고장 로봇에서 회수한 화물의 위치·이벤트 정정이 식별·추적 쪽 기록 규칙에 기대게 된다(oq-079). [사실][^ref-492]
- **18. 실시간 세계 상태·데이터 일관성 ↔ [29. 명령·작업 실행의 신뢰성](../execution-collaboration-and-recovery/command-and-task-execution-reliability.md)·32. 예외 복구·재계획·업무 연속성**: VDA 5050 3.0.0 에서 로봇 연결이 예기치 않게 끊기면 브로커가 MQTT 유언으로 CONNECTION_BROKEN 을 대신 알리고, 로봇은 받은 주문을 유지한 채 마지막으로 해제된 노드까지 수행한다. [사실][^ref-031] 같은 연결은 [F. 연동](../integration/index.md) 페이지의 연결 절에도 있다.
- **18. 실시간 세계 상태·데이터 일관성·19. 사람·보행자 모델 ↔ [31. 사람–로봇 협업](../execution-collaboration-and-recovery/human-robot-collaboration.md)**: Riedelbauch·Werner·Henrich(RAAD 2017)는 사람과 함께 쓰는 작업 공간에서 세계 모델의 정보마다 확실도 값을 붙이고, 전역 센서가 감지한 사람 존재에 따라 이 값을 시간에 따라 조정하며 손 장착(eye-in-hand) 카메라 데이터와 결합해 로봇이 정보가 아직 유효한지 판단하게 했다(조립용 시제품 실험이며 현장 유형은 명시되지 않았다). [사실][^ref-1302] 사람이 드나든 구역의 물품·설비 상태는 관측 뒤 바뀌었을 가능성이 높으므로 19. 사람·보행자 모델의 사람 위치 정보가 18. 실시간 세계 상태·데이터 일관성의 상태 신뢰도를 낮추는 근거로 쓰일 수 있을 것으로 보이나, 이동로봇 현장 적용 사례는 확인하지 못했다. [추정][^ref-1302] 이 방식을 물류창고·병원 같은 이동로봇 현장에 적용한 사례가 있는지는 새 열린 질문으로 올렸다.

### [I. 설계·시뮬레이션](../design-and-simulation/index.md)

- **18. 실시간 세계 상태·데이터 일관성 ↔ [34. 시뮬레이션·예측용 디지털 트윈](../design-and-simulation/simulation-and-predictive-digital-twin.md)**: 제조 분야 분류 자료가 현장 상태가 한 방향으로 자동 반영되는 디지털 섀도와 디지털 트윈을 구분하므로, 18. 실시간 세계 상태·데이터 일관성은 현재 상태를 표현하고 34. 시뮬레이션·예측용 디지털 트윈은 그 표현을 복제해 가정한 미래를 실험하는 쪽으로 나누는 것이 분류 원문의 구분과 맞을 것으로 보인다(근거 자료는 제조 대상). [추정][^ref-291][^ref-290]
- **19. 사람·보행자 모델 ↔ 34. 시뮬레이션·예측용 디지털 트윈**: HuNavSim(2023)은 사람 인지 내비게이션을 벤치마크하기 위한 ROS 2 사람 이동 시뮬레이터이고, Kidokoro 외(HRI 2013)는 보행자 행동 모델로 가상 주행 상황을 시뮬레이션해 혼잡을 피하는 로봇 위치를 계획했다. [사실][^ref-1179][^ref-1182]
- **19. 사람·보행자 모델 ↔ 36. 가상 시운전·실제 상황 재현**: 기록 재현에서 사람이 반응하지 않는 문제는 위 C. 채팅 기반 구성·운영 항목에 적었다(oq-256).

### [J. 현장 운영·관제](../field-operations-and-monitoring/index.md)

- **18. 실시간 세계 상태·데이터 일관성 ↔ [38. 모니터링·이상 탐지·원인 분석](../field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md)·[39. 운영 성과 측정·개선](../field-operations-and-monitoring/operational-performance-measurement-and-improvement.md)**: 로봇 상태의 상태 값·배터리·문제 목록·시각과 문·승강기 상태의 시각을 한 세계 상태 기록에 모으면, 가동률·충전·오류 시간 지표와 '지연 원인이 로봇인지 문인지' 분석이 같은 기록을 쓰게 될 것으로 보인다. [추정][^ref-148][^ref-285][^ref-286] 같은 연결은 [A. 기획·사업](../planning-and-business/index.md) 페이지의 연결 절에도 있다.

### [K. 플랫폼 아키텍처·인프라](../platform-architecture-and-infrastructure/index.md)

- **18. 실시간 세계 상태·데이터 일관성 ↔ [42. 분산 시스템·통신·컴퓨팅 구조](../platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md)**: ROS 2 QoS 의 기한·생존성 정책, Sparkplug 의 노드 종료(NDEATH) 뒤 지표 STALE 표시, VDA 5050 의 MQTT 유언을 통한 연결 끊김 통지처럼 통신 계층에 상태의 오래됨을 알리는 장치가 있으며, 세 출처는 각각 한 장치만 다룬다. [사실][^ref-282][^ref-287][^ref-031] 같은 연결은 [B. 로봇 온톨로지](../robot-ontology/index.md)·[F. 연동](../integration/index.md) 페이지의 연결 절에도 있다.
- **17. 작업 대상·자산 식별과 인계 추적·18. 실시간 세계 상태·데이터 일관성 ↔ [43. 데이터·관측성·배포](../platform-architecture-and-infrastructure/data-observability-and-deployment.md)**: EPCIS 2.0 온톨로지가 발생 시각(eventTime)·기록 시각(recordTime)·UTC 차이를 구분하므로, 실행 기록과 관측 데이터에서도 발생 시각과 수신·기록 시각을 따로 남기는 설계가 두 대분류를 잇는 지점이 될 것으로 보인다. [추정][^ref-045]

### [L. AI·학습 기술](../ai-and-learning/index.md)

- **19. 사람·보행자 모델 ↔ [46. 예측·학습 기반 최적화](../ai-and-learning/prediction-and-learning-based-optimization.md)**: Rudenko 외 서베이가 정리한 사람 움직임 궤적 예측은 19. 사람·보행자 모델의 가까운 미래 사람 위치 추정 방법이므로, 예측 결과를 경로·배정 비용에 넣는 일이 46. 예측·학습 기반 최적화와 이어질 것으로 보인다. [추정][^ref-1172]
- 이번 실행에서 근거를 확보한 L. AI·학습 기술 연결은 이 하나뿐이다. 45. 문서·도면·장면 이해와 18. 실시간 세계 상태·데이터 일관성·19. 사람·보행자 모델의 연결(oq-227)은 아래 '아직 다루지 않은 연결'에 둔다.

### [M. 안전](../safety/index.md)

- **18. 실시간 세계 상태·데이터 일관성 ↔ [48. 안전·위험 관리](../safety/safety-and-risk-management.md)**: Open-RMF 승강기 상태의 현재 모드에는 알 수 없음·사람·AGV·화재·오프라인·비상이 있으며 사람·AGV 모드만 설정할 수 있고 나머지는 읽기 전용이다. [사실][^ref-286] 승강기 화재·비상 모드 제어와 설비 안전 제어는 분류 원문 19장 시설·설비 제어 경계의 연계 대상이고, ROP 는 탑승 확정 전에 최신 모드를 확인해 작업·경로 제약에 반영하는 쪽을 맡는 것으로 보인다. [추정][^ref-286] 같은 연결은 [G. 계획·최적화](../planning-and-optimization/index.md) 페이지의 연결 절에도 있다.
- **19. 사람·보행자 모델 ↔ [49. 사람 근접 안전](../safety/human-proximity-safety.md)**: 병원의 '사람·휠체어와 마주치면 무조건 대기' 규칙과 창고의 움직임별 사회적 비용에 따른 속도 제약처럼 사람 흐름 정보는 구역별 대기·속도 규칙으로 49. 사람 근접 안전과 이어지며, ROP 는 규칙을 요청·관리하고 사람 검출·안전 정지·국소 회피는 연계 대상으로 로봇이 맡는 경계가 될 것으로 보인다. [추정][^ref-1181][^ref-1180]

### [N. 보안·개인정보](../security-and-privacy/index.md)

- **19. 사람·보행자 모델 ↔ [53. 개인정보·영상 데이터](../security-and-privacy/privacy-and-video-data.md)**: ROS 규약 제안 REP-155(Draft, 2022-01-11 작성)는 사람마다 영속 ID 를 두고 얼굴·몸·음성 ID 를 후보 대응으로 연결하며, 이 문서는 개인정보·동의를 다루지 않는다. [사실][^ref-1173] 사람 표현의 영속 ID 가 얼굴·음성 인식과 연결될 수 있으므로 ROP 가 보관하는 사람 정보는 구역·시간대 집계·익명화로 두는 것이 두 대분류의 경계가 될 것으로 보이며, 여러 출처의 사람 위치를 합치는 익명화 형식과 촬영 거부 의사 공유 방법은 열린 질문(oq-261, oq-272)이다. [추정][^ref-1173]
- **17. 작업 대상·자산 식별과 인계 추적 ↔ [51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md)**: 17. 작업 대상·자산 식별과 인계 추적의 '사람에게 넘길 때 수령인 확인'은 인증 수단과 이어진다. 병원용 운반 로봇 Zena RX(ST Engineering Aethon, 2024-04-29 출시 발표)는 생체 인식과 직원 PIN 코드로 잠금 칸을 열게 해 권한 있는 직원만 약품·검체를 꺼낼 수 있다고 제조사는 밝힌다(제조사 보도자료, 독립 확인 없음). [추정] 벤더 주장[^ref-1299] 잠금 칸·생체 인식·PIN 인증은 로봇 제조사 기능으로 연계 대상이며, ROP 몫은 그 인증 결과를 받아 인계 기록에 남기는 일로 한정된다. [추정][^ref-1299]
- 2019-10 우아한형제들 본사(서울 잠실) 시범 운영에서 배달 로봇 딜리타워는 라이더가 주문번호 앞 네 자리와 층을 입력하면 승강기로 이동해 목적 층에서 고객을 호출하며, 고객이 휴대전화 번호 뒤 네 자리를 입력해야 음식 칸이 열렸다(기사 1건 기준). [추정][^ref-1300]
- 2020-07 보도에 따르면 딜리타워의 공동주택(포레나 영등포) 도입 계획에서는 라이더와 고객이 모두 로봇 화면에 비밀번호를 눌러 적재함을 열고, 로봇은 도착 시 고객에게 문자와 전화로 알리게 되어 있었다(2020-07 계획 단계 보도이며 실제 운영 방식은 확인하지 못했다). [사실][^ref-1301]
- **17. 작업 대상·자산 식별과 인계 추적 ↔ 51. 인증·권한·격리·53. 개인정보·영상 데이터**: 확인한 사례의 수령인 확인 수단이 생체+PIN(병원), 전화번호 뒤 네 자리(사무 건물), 비밀번호(공동주택 계획)로 서로 달라, '누구에게 넘겼는가' 기록은 51. 인증·권한·격리의 인증 수단과 53. 개인정보·영상 데이터의 생체·전화번호 처리에 기대게 될 것으로 보이며, 그 결과가 주문·업무 시스템에 완료 이벤트로 기록되는지는 확인하지 못했다. [추정][^ref-1299][^ref-1300][^ref-1301] 인접한 열린 질문은 식당·호텔의 수령 확인을 다룬 [oq-180](../../open-questions.md)과 공동주택 배송로봇의 수령 인증을 다룬 [oq-184](../../open-questions.md)이며, 병원 운반 로봇의 수령인 인증 결과를 완료·인계 이벤트로 남기는 공개 인터페이스가 있는지는 새 열린 질문으로 올렸다.

### [O. 검증·도입·수명주기](../verification-deployment-and-lifecycle/index.md)

- **19. 사람·보행자 모델 ↔ [54. 시험·형식 검증·벤치마크](../verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md)**: 사회적 로봇 내비게이션 알고리즘 평가 원칙·지침(Francis 외, 2023)과 장기 시공간 보행자 흐름 지도의 벤치마크 연구(Vintr 외, 2022)가 있어, 사람 모델을 쓴 계획의 효과를 시험하는 방법이 54. 시험·형식 검증·벤치마크와 이어진다. [사실][^ref-1079][^ref-1178]

### [P. 거버넌스·법규·사회](../governance-law-and-society/index.md)

- **19. 사람·보행자 모델 ↔ [60. 노동·수용성·접근성](../governance-law-and-society/labor-acceptance-and-accessibility.md)**: 실외 보도 로봇에 대해 Han 외(CHI 2024)는 이동장애인 15명·로봇 실무자 8명 면담과 4회 공동설계 워크숍에서, 보도 로봇이 들어오면 이동장애인이 보도 공간을 두고 경쟁해야 한다고 느끼며 부족한 연석 경사로 같은 기존 장벽 위에서 로봇이 운행된다고 보고했다. [사실][^ref-1214] 보행 약자가 지나야 하는 연석 경사로·좁은 통로를 사람 흐름 모델의 양보·비정차 구역으로 표현해야 접근성 요구가 경로·대기 위치 제약으로 이어질 것으로 보이나, 국내 기준은 확인하지 못했다(oq-188 관련). [추정][^ref-1214]
- **17. 작업 대상·자산 식별과 인계 추적 ↔ [58. 다사업자 책임·계약·데이터](../governance-law-and-society/multi-party-responsibility-contracts-and-data.md)**: CBV 의 출발지·도착지 유형(owning_party·possessing_party·location)이 소유·점유 이전을 당사자 단위로 기록하므로, 제조사·운영사·화주 사이 인계 책임의 기록 근거가 17. 작업 대상·자산 식별과 인계 추적의 이벤트에서 나올 것으로 보인다. [추정][^ref-014][^ref-015][^ref-044]

### [Q. 현장 유형별 적용](../site-type-applications/index.md)

현장마다 다른 요구는 Q. 현장 유형별 적용에 모으고, 식별·상태·사람 모델처럼 모든 현장에 공통인 기능은 이 대분류에 둔다.

- **19. 사람·보행자 모델 ↔ [61. 물류창고](../site-type-applications/warehouse.md)·[63. 병원·의료](../site-type-applications/hospital-and-healthcare.md)·[64. 상업 시설](../site-type-applications/commercial-facilities.md)**: 게시된 19. 사람·보행자 모델 페이지의 적용 사례는 스웨덴 외레브로 창고의 자율 지게차 플릿(ILIAD), 한림대학교성심병원의 복도 혼잡 대응, 쇼핑몰에서 혼잡을 예상하는 로봇(Kidokoro 외)이다. [사실][^ref-1180][^ref-1181][^ref-1182]
- **19. 사람·보행자 모델 ↔ [66. 실외](../site-type-applications/outdoor.md)**: 연계 대상으로, 행정안전부 인파관리지원시스템은 2023-12-29부터 전국 중점관리지역 100곳에서 이동통신 3사 기지국 접속정보로 인파 밀집도를 추정해 위험 수준에 따라 지자체 공무원에게 경보를 보내며, 실외 로봇 운행 제약과 연동한 사례는 확인되지 않았다(oq-274). [사실][^ref-1177]
- **17. 작업 대상·자산 식별과 인계 추적 ↔ 63. 병원·의료·[65. 가정·공동주택](../site-type-applications/home-and-apartment.md)·[67. 기타 현장](../site-type-applications/other-sites.md)**: 수령인 확인 사례(병원 Zena RX, 공동주택 딜리타워 도입 계획, 사무 건물 딜리타워 시범 운영)는 위 N. 보안·개인정보 항목에 적었다.

### 아직 다루지 않은 연결

다음 연결은 이번 실행까지 검증된 근거가 없어 쓰지 않았다.

- [A. 기획·사업](../planning-and-business/index.md): 17. 작업 대상·자산 식별과 인계 추적, 18. 실시간 세계 상태·데이터 일관성, 19. 사람·보행자 모델을 1. 기술·시장·업체 동향, 2. 사용 사례·요구·책임 범위, 3. 경제성·조달·사업 모델과 직접 잇는 근거.
- L. AI·학습 기술: 18. 실시간 세계 상태·데이터 일관성·19. 사람·보행자 모델과 [45. 문서·도면·장면 이해](../ai-and-learning/document-drawing-and-scene-understanding.md)의 연결(고정 카메라와 로봇 인식 결과의 결합, oq-227).
- O. 검증·도입·수명주기: 17. 작업 대상·자산 식별과 인계 추적과 54. 시험·형식 검증·벤치마크, [55. 현장 조사·설치·시운전](../verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md)의 연결.
- J. 현장 운영·관제: [37. 관제 화면·실행 기록](../field-operations-and-monitoring/control-screen-and-execution-records.md), [40. 운영 절차·요청 창구](../field-operations-and-monitoring/operating-procedures-and-request-channels.md)와의 연결.
- N. 보안·개인정보: [52. 통신 보호·위협 관리·감사](../security-and-privacy/communication-protection-threat-management-and-audit.md)와의 연결.
- P. 거버넌스·법규·사회: [59. 법·규제·보험·라이선스](../governance-law-and-society/law-regulation-insurance-and-licensing.md)와의 연결.
- Q. 현장 유형별 적용: 19. 사람·보행자 모델의 게시 사례에는 실외·제조 공장·가정 현장 사례가 아직 없다.

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 69건이다(논문 20건 · 기사·보고서 3건 · 업체 발표 1건 · 표준·오픈소스·기관 자료 45건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-041](../../references/ref-041.md) — Naqvi, M. R. 외(Scientific Reports), Ontology-driven integration of advertised and operational capabilities in robots (발행 2025-10-02)
- [ref-1214](../../references/ref-1214.md) — Han, H. Z. 외 (Carnegie Mellon University) — CHI '24, Co-design Accessible Public Robots: Insights from People with Mobility Disability, Robotic Practitioners and Their Collaborations (발행 2024-04-07)
- [ref-1128](../../references/ref-1128.md) — Gulino, C., Fu, J., Luo, W. 외 (Waymo, arXiv), Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research (발행 2023-10-12)
- [ref-1179](../../references/ref-1179.md) — Pérez-Higueras, N., Otero, R., Caballero, F., & Merino, L. (arXiv; IEEE RA-L 2023), HuNavSim: A ROS 2 Human Navigation Simulator for Benchmarking Human-Aware Robot Navigation (발행 2023-09-13)
- [ref-1079](../../references/ref-1079.md) — Francis, A., Pérez-D'Arpino, C., Li, C. 외 (ACM Transactions on Human-Robot Interaction, arXiv), Principles and Guidelines for Evaluating Social Robot Navigation Algorithms (발행 2023-06-29)
- [ref-296](../../references/ref-296.md) — 김지형, OPC UA를 활용한 이기종 로봇의 실시간 디지털 트윈 설계 및 구현 (발행 2023)
- [ref-1171](../../references/ref-1171.md) — Kucner, T. P., Magnusson, M., Mghames, S., Palmieri, L., Verdoja, F., Swaminathan, C. S., Krajník, T., Schaffernicht, E., Bellotto, N., Hanheide, M., & Lilienthal, A. J. (The International Journal of Robotics Research 42(11)), Survey of maps of dynamics for mobile robots (발행 2023)
- [ref-1178](../../references/ref-1178.md) — Vintr, T., Blaha, J., Rektoris, M., Ulrich, J., Rouček, T., Broughton, G., Yan, Z., & Krajník, T. (Frontiers in Robotics and AI), Toward Benchmarking of Long-Term Spatio-Temporal Maps of Pedestrian Flows for Human-Aware Navigation (발행 2022-07-04)
- [ref-294](../../references/ref-294.md) — 이동건, 송승현, 이찬혁, 노상도, 윤상문, 이현영(한국CDE학회 논문집), 자동물류시스템의 설계 검증 및 운영을 위한 디지털트윈 개발 및 적용 (발행 2021-12)
- [ref-289](../../references/ref-289.md) — Yates, R. D., Sun, Y., Brown, D. R., Kaul, S. K., Modiano, E., & Ulukus, S., Age of Information: An Introduction and Survey (발행 2021-05)
- 그 밖에 10건

**기사·보고서**

- [ref-1181](../../references/ref-1181.md) — 조선비즈 (이정아, 다음 뉴스 게재), 로봇과 인간이 공존하는 병원…약 배달 로봇에 길 비켜주고 엘리베이터도 잡아줘 (발행 2024-07-12)
- [ref-1301](../../references/ref-1301.md) — 경향신문 (곽희양), 내년 2월 자율주행 로봇이 아파트 내에서 배달 음식 나른다 (발행 2020-07-03)
- [ref-1300](../../references/ref-1300.md) — 바이라인네트워크 (엄지용), 엘리베이터 타는 배달로봇과의 조우 (발행 2019-10-17)

**업체 발표**

- [ref-1299](../../references/ref-1299.md) — ST Engineering Aethon (Newswire 게재 보도자료), ST Engineering Aethon Launches Zena RX, Redefining Secure Delivery of Medications, Specimens and Sensitive Goods in Hospitals (발행 2024-04-29)

**표준·오픈소스·기관 자료**

- [ref-854](../../references/ref-854.md) — Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse, Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP) (발행 2026-06-25)
- [ref-032](../../references/ref-032.md) — VDA(Verband der Automobilindustrie), Version 3.0 of VDA 5050 released (발행 2026-04)
- [ref-011](../../references/ref-011.md) — ISO/IEC, ISO/IEC 19987:2024 - Information technology — EPC Information Services (EPCIS) (발행 2024-03)
- [ref-012](../../references/ref-012.md) — ISO/IEC, ISO/IEC 19988:2024 - Information technology — GS1 Core Business Vocabulary (CBV) (발행 2024)
- [ref-1177](../../references/ref-1177.md) — 행정안전부 (대한민국 정책브리핑), 29일부터 인파관리지원시스템 본격 운영…다중운집 인파사고 예방 (발행 2023-12-27)
- [ref-1173](../../references/ref-1173.md) — ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan, REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction (발행 2022-01-11)
- [ref-022](../../references/ref-022.md) — VDA(Verband der Automobilindustrie), VDA 5050 Version 2.0.0 — Interface for the communication between automated guided vehicles (AGV) and a master control (발행 2022-01)
- [ref-045](../../references/ref-045.md) — GS1, gs1/EPCIS — Ontology/EPCIS.ttl (EPCIS ontology 2.0) (발행 2021-09-30)
- [ref-044](../../references/ref-044.md) — GS1, gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0) (발행 2021-09-30)
- [ref-1180](../../references/ref-1180.md) — ILIAD 프로젝트 컨소시엄 (EU Horizon 2020), Concluding ILIAD (발행 2021-06)
- 그 밖에 35건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-10-09 · 갱신 · [E. 사물·사람·실시간 상태](index.md) — '다른 대분류와의 연결' 절 신규 작성(15개 대분류와의 연결, 아직 다루지 않은 연결 목록), '참고 자료' 절에 각주 정의 39건 추가 (실행 2026-10-09-03)
- 2026-10-09 · 요약 · [E. 사물·사람·실시간 상태](index.md) — E. 사물·사람·실시간 상태: '다른 대분류와의 연결' 절 신규 작성(15개 대분류 연결·아직 다루지 않은 연결 목록, f7·f41 강등 반영, 각주 39건 추가) (실행 2026-10-09-03)
- 2026-09-30 · 갱신 · [19. 사람·보행자 모델](people-and-pedestrian-model.md) — 영역 심화: 섹션 3~11 신규 작성(현장 유형 사례 4건: 물류창고·병원·상업 시설·기타), 13절 각주, 1차 조건부 승인 수정 16건 이행, 2차 수정: 5절 기타 사례 제약 칸을 비교 지표로 바로잡음·완료·인계 칸 두 곳 미확인·병원 서술의 검증 상태 문장 태그 제거, 7절 요약 문장을 사실·추정으로 분리 (실행 2026-09-30-20)
- 2026-09-30 · 생성 · [19. 사람·보행자 모델 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area19-s6.md) — 자동 분리: 19. 사람·보행자 모델 의 "6. 대표 접근법과 기술" 절을 옮겼다. 2차 수정: 장기 시공간 흐름 지도 첫 문장을 ref-1171 확인 범위(전형적 움직임 패턴 지도)로 고침 (실행 2026-09-30-20)
- 2026-09-30 · 생성 · [19. 사람·보행자 모델 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area19-s4.md) — 자동 분리: 19. 사람·보행자 모델 의 "4. 핵심 개념과 용어" 절을 옮겼다(2차 재실행에서 변경 없음) (실행 2026-09-30-20)
<!-- auto:category-recent:end -->

## 참고 자료

원문의 [3]은 참고문헌 [ref-003](../../references/ref-003.md)에 해당한다.[^ref-003]

[^ref-003]: GS1, EPCIS and CBV Linked Data Model, 미확인, https://ref.gs1.org/epcis/, 접근일 2026-09-28

[^ref-014]: GS1, Core Business Vocabulary (CBV) Standard, 미확인, https://ref.gs1.org/standards/cbv/, 접근일 2026-10-09 (원문 미열람)
[^ref-015]: GS1, EPCIS and CBV Implementation Guideline, 미확인, https://www.gs1.org/docs/epc/EPCIS_Guideline.pdf, 접근일 2026-10-09 (원문 미열람)
[^ref-023]: Open Robotics, Workcells - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_workcells.html, 접근일 2026-10-09
[^ref-024]: Singh, J. 외, RFID tag readability issues with palletized loads of consumer goods, 2009, https://onlinelibrary.wiley.com/doi/abs/10.1002/pts.864, 접근일 2026-10-09 (원문 미열람)
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09
[^ref-041]: Naqvi, M. R. 외(Scientific Reports), Ontology-driven integration of advertised and operational capabilities in robots, 2025-10-02, https://www.nature.com/articles/s41598-025-16649-3, 접근일 2026-10-09 (원문 미열람)
[^ref-044]: GS1, gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0), 2021-09-30, https://github.com/gs1/EPCIS/blob/master/Ontology/CBV.ttl, 접근일 2026-10-09
[^ref-045]: GS1, gs1/EPCIS — Ontology/EPCIS.ttl (EPCIS ontology 2.0), 2021-09-30, https://github.com/gs1/EPCIS/blob/master/Ontology/EPCIS.ttl, 접근일 2026-10-09
[^ref-049]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg, 접근일 2026-10-09
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-10-09
[^ref-104]: Open Robotics (open-rmf), rmf_demos — Demonstrations of Open-RMF (README), 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-10-09 (원문 미열람)
[^ref-148]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json, 접근일 2026-10-09
[^ref-162]: GS1, Identifying a physical location - GLN, 미확인, https://www.gs1.org/standards/id-keys/gln/physical-location, 접근일 2026-10-09 (원문 미열람)
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-10-09
[^ref-282]: Open Robotics (ROS 2 Documentation), Quality of Service settings — ROS 2 Documentation: Jazzy, 미확인, https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html, 접근일 2026-10-09 (원문 미열람)
[^ref-285]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_door_msgs/msg/DoorState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorState.msg, 접근일 2026-10-09
[^ref-286]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg, 접근일 2026-10-09
[^ref-287]: Eclipse Foundation (eclipse-sparkplug GitHub), Sparkplug Specification — Chapter 5 Operational Behavior (Sparkplug_5_Operational_Behavior.adoc), 미확인, https://github.com/eclipse-sparkplug/sparkplug/blob/master/specification/src/main/asciidoc/chapters/Sparkplug_5_Operational_Behavior.adoc, 접근일 2026-10-09
[^ref-290]: NIST, DIGITAL TWINS FOR ADVANCED MANUFACTURING: THE STANDARDIZED APPROACH, 미확인, https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=957417, 접근일 2026-10-09 (원문 미열람)
[^ref-291]: Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W., Digital Twin in manufacturing: A categorical literature review and classification, 2018, https://www.sciencedirect.com/science/article/pii/S2405896318316021, 접근일 2026-10-09 (원문 미열람)
[^ref-292]: DeHoratius, N., & Raman, A., Inventory Record Inaccuracy: An Empirical Analysis, 2008, https://pubsonline.informs.org/doi/10.1287/mnsc.1070.0789, 접근일 2026-10-09 (원문 미열람)
[^ref-492]: GS1, EPC Information Services (EPCIS) Standard 1.2, 2016-09-29, https://www.gs1.org/sites/default/files/docs/epc/EPCIS-Standard-1.2-r-2016-09-29.pdf, 접근일 2026-10-09 (원문 미열람)
[^ref-854]: Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse, Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP), 2026-06-25, https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687, 접근일 2026-10-09
[^ref-1079]: Francis, A., Pérez-D'Arpino, C., Li, C. 외 (ACM Transactions on Human-Robot Interaction, arXiv), Principles and Guidelines for Evaluating Social Robot Navigation Algorithms, 2023-06-29, https://arxiv.org/abs/2306.16740, 접근일 2026-10-09 (원문 미열람)
[^ref-1128]: Gulino, C., Fu, J., Luo, W. 외 (Waymo, arXiv), Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research, 2023-10-12, https://arxiv.org/abs/2310.08710, 접근일 2026-10-09 (원문 미열람)
[^ref-1171]: Kucner, T. P., Magnusson, M., Mghames, S., Palmieri, L., Verdoja, F., Swaminathan, C. S., Krajník, T., Schaffernicht, E., Bellotto, N., Hanheide, M., & Lilienthal, A. J. (The International Journal of Robotics Research 42(11)), Survey of maps of dynamics for mobile robots, 2023, https://journals.sagepub.com/doi/10.1177/02783649231190428, 접근일 2026-10-09 (원문 미열람)
[^ref-1172]: Rudenko, A., Palmieri, L., Herman, M., Kitani, K. M., Gavrila, D. M., & Arras, K. O. (arXiv; IJRR 39(8), 2020), Human Motion Trajectory Prediction: A Survey, 2019-12-17, https://arxiv.org/abs/1905.06113, 접근일 2026-10-09 (원문 미열람)
[^ref-1173]: ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan, REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction, 2022-01-11, https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst, 접근일 2026-10-09
[^ref-1177]: 행정안전부 (대한민국 정책브리핑), 29일부터 인파관리지원시스템 본격 운영…다중운집 인파사고 예방, 2023-12-27, https://www.korea.kr/news/policyNewsView.do?newsId=148924176, 접근일 2026-10-09 (원문 미열람)
[^ref-1178]: Vintr, T., Blaha, J., Rektoris, M., Ulrich, J., Rouček, T., Broughton, G., Yan, Z., & Krajník, T. (Frontiers in Robotics and AI), Toward Benchmarking of Long-Term Spatio-Temporal Maps of Pedestrian Flows for Human-Aware Navigation, 2022-07-04, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.890013/full, 접근일 2026-10-09 (원문 미열람)
[^ref-1179]: Pérez-Higueras, N., Otero, R., Caballero, F., & Merino, L. (arXiv; IEEE RA-L 2023), HuNavSim: A ROS 2 Human Navigation Simulator for Benchmarking Human-Aware Robot Navigation, 2023-09-13, https://arxiv.org/abs/2305.01303, 접근일 2026-10-09 (원문 미열람)
[^ref-1180]: ILIAD 프로젝트 컨소시엄 (EU Horizon 2020), Concluding ILIAD, 2021-06, https://iliad-project.eu/concluding-iliad/, 접근일 2026-10-09 (원문 미열람)
[^ref-1181]: 조선비즈 (이정아, 다음 뉴스 게재), 로봇과 인간이 공존하는 병원…약 배달 로봇에 길 비켜주고 엘리베이터도 잡아줘, 2024-07-12, https://v.daum.net/v/bc4riunbUE, 접근일 2026-10-09 (원문 미열람)
[^ref-1182]: Kidokoro, H., Kanda, T., Brščić, D., & Shiomi, M. (ACM/IEEE HRI 2013), Will I bother here? - A robot anticipating its influence on pedestrian walking comfort, 2013-03, https://www.semanticscholar.org/paper/Will-I-bother-here-A-robot-anticipating-its-on-Kidokoro-Kanda/bc0b26f1c13405fd89eb6d280bee739aed5b07a6, 접근일 2026-10-09 (원문 미열람)
[^ref-1214]: Han, H. Z. 외 (Carnegie Mellon University) — CHI '24, Co-design Accessible Public Robots: Insights from People with Mobility Disability, Robotic Practitioners and Their Collaborations, 2024-04-07, https://arxiv.org/abs/2404.05050, 접근일 2026-10-09
[^ref-1299]: ST Engineering Aethon (Newswire 게재 보도자료), ST Engineering Aethon Launches Zena RX, Redefining Secure Delivery of Medications, Specimens and Sensitive Goods in Hospitals, 2024-04-29, https://www.newswire.com/news/st-engineering-aethon-launches-zena-rx-redefining-secure-delivery-of-22310264, 접근일 2026-10-09
[^ref-1300]: 바이라인네트워크 (엄지용), 엘리베이터 타는 배달로봇과의 조우, 2019-10-17, https://byline.network/2019/10/17-73/, 접근일 2026-10-09
[^ref-1301]: 경향신문 (곽희양), 내년 2월 자율주행 로봇이 아파트 내에서 배달 음식 나른다, 2020-07-03, https://www.khan.co.kr/article/202007031130001, 접근일 2026-10-09
[^ref-1302]: Riedelbauch, D., Werner, T., & Henrich, D. (RAAD 2017, Springer), Supporting a Human-Aware World Model through Sensor Fusion, 2017, https://eref.uni-bayreuth.de/92445, 접근일 2026-10-09
````

### docs/categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md (요약)

```markdown
# 17. 작업 대상·자산 식별과 인계 추적

소속 대분류: E. 사물·사람·실시간 상태 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 4

## 1. 한 줄 정의

물품·자산·도구 같은 작업 대상의 식별·위치·인계 책임을 추적하고, 사람에게 넘길 때 수령인을 확인한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **작업 대상 식별·추적**: 물품·자산·도구·운반구·검체·세탁물처럼 작업 대상의 식별자·위치·적재 관계를 추적한다
- **인계·책임 기록**: 누가 언제 무엇을 넘겨받았는지 관측 근거와 함께 기록한다
- **이벤트 공통 형식**: 상태·위치·이동·인계 이벤트를 공통 형식으로 주고받는다(GS1 EPCIS 등)
- **수령인 확인**: 물건을 사람에게 넘길 때 받는 사람을 PIN·카드·앱으로 확인하고 인계 기록을 남긴다

이전 분류(2026-09-24)에서 이 페이지는 옛 7번 영역 ‘화물·재고·자산 식별과 추적’(옛 대분류 B. 공통 정보·환경 모델)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 제품·박스·팔레트·운반구·로봇을 식별하고, 적재 관계·위치·인계 이력을 연결 [옛 분류원문]

> 옛 질문: 로봇은 도착했는데 실제로 어떤 팔레트가 인계됐는가? [옛 분류원문]

> 옛 원문 주석: **7번은 SCM 관점에서 특히 빠뜨리기 쉽다.** 로봇 위치를 추적하는 것과 화물의 위치·인계 책임을 추적하는 것은 다르다. GS1 EPCIS는 제품·자산의 상태, 위치, 이동, 인계에 관한 이벤트를 공유하는 참고 표준이다. [3] [옛 분류원문]

이전 분류 기준: 원문의 [3]은 참고문헌 [ref-003](../../references/ref-003.md)에 해당한다.[^ref-003]

## 2. 핵심 질문

로봇이 도착했을 때 실제로 무엇이 누구에게 넘겨졌는지 어떻게 확인할 것인가? [분류원문]

> 원문 주석: **17번은 특히 빠뜨리기 쉽다.** 로봇 위치를 추적하는 것과 작업 대상의 위치·인계 책임을 추적하는 것은 다르다. GS1 EPCIS는 제품·자산의 상태, 위치, 이동, 인계에 관한 이벤트를 공유하는 참고 표준이다. [3] [분류원문]

원문의 [3]은 참고문헌 [ref-003](../../references/ref-003.md)에 해당한다.[^ref-003]
```

### docs/categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md (요약)

```markdown
# 18. 실시간 세계 상태·데이터 일관성

소속 대분류: E. 사물·사람·실시간 상태 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

로봇·설비·공간·물품의 현재 상태를 통합하고, 관측의 신선도·신뢰도를 관리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **실시간 세계 상태 통합**: 로봇·설비·공간·물품·사람의 현재 상태를 한곳에 모으고 지연·누락·충돌·불확실성을 관리한다
- **관측 신선도·신뢰도**: 오래되거나 불확실한 관측(예를 들어 30초 전의 문 상태)을 지금의 판단에 써도 되는지 정한다

이전 분류(2026-09-24)에서 이 페이지는 옛 8번 영역 ‘실시간 세계 상태·데이터 일관성’(옛 대분류 B. 공통 정보·환경 모델)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 로봇·설비·공간·화물의 현재 상태를 통합하고, 시간 지연·누락·충돌·불확실성을 관리 [옛 분류원문]

> 옛 질문: 문이 열려 있다는 정보가 30초 전이라면 지금도 통과 가능하다고 볼 수 있을까? [옛 분류원문]

> 옛 원문 주석: 8번의 실시간 모델이 **현재 상태를 표현**한다면, 22번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [옛 분류원문]

## 2. 핵심 질문

조금 전에 받은 상태 정보를 지금의 판단에 믿고 써도 되는가? [분류원문]

> 원문 주석: 18번의 실시간 모델이 **현재 상태를 표현**한다면, 34번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [분류원문]
```

### docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md (요약)

```markdown
# 19. 사람·보행자 모델

소속 대분류: E. 사물·사람·실시간 상태 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

현장 사람의 위치·흐름·혼잡을 모델링해 계획과 안전에 쓴다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **사람·보행자 모델**: 현장 사람의 위치·목적지·멈춤·교차를 모델링해 로봇 계획과 안전에 반영한다
- **사람 흐름·혼잡 추정**: 시간대·구역별 사람의 흐름과 혼잡을 추정해 경로와 작업 시간에 반영한다

## 2. 핵심 질문

현장 사람의 위치와 흐름을 어떻게 알고 계획과 안전에 반영할 것인가? [분류원문]
```

### docs/categories/integration/index.md

````markdown
---
title: "F. 연동"
type: category
status: published
created: 2026-09-24
updated: 2026-09-25
version: 2
sources: [ref-004, ref-009, ref-023, ref-031, ref-049, ref-051, ref-060, ref-079, ref-103, ref-105, ref-111, ref-125, ref-129, ref-130, ref-148, ref-153, ref-159, ref-228, ref-251, ref-253, ref-282, ref-283, ref-284, ref-285, ref-286, ref-287, ref-300, ref-310, ref-312, ref-314, ref-315, ref-316, ref-317, ref-364, ref-365, ref-367, ref-374, ref-405, ref-406, ref-407, ref-408, ref-409]
---

[홈](../../index.md) › F. 연동

# F. 연동

## 핵심 질문

제조사 관제·로봇·문·승강기·업무 시스템과 어떻게 확실하게 연결할 것인가? [분류원문]

## 개요

제조사 관제·로봇, 문·승강기 같은 설비, 업무 시스템과 실제로 연결하고 표준으로 호환성을 확보하는 일. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **20. 로봇·제조사 관제 연동** | 제조사 API·SDK·관제 시스템과 연결하는 어댑터, 공통 명령·관측 계약, 로봇과 주고받는 통신 방식 | 로봇을 하나씩 직접 움직일지, 제조사 관제에 맡길지, 어떤 방식으로 통신할지 어떻게 정할 것인가? | [20. 로봇·제조사 관제 연동](robot-and-vendor-fleet-manager-integration.md) | published |
| **21. 상호운용 표준·적합성** | 로봇 상호운용 표준을 채택·변환하고 적합성을 시험한다 | 어떤 상호운용 표준을 따르고, 제조사가 그 표준을 지키는지 어떻게 확인할 것인가? | [21. 상호운용 표준·적합성](interoperability-standards-and-conformance.md) | published |
| **22. 설비·건물 시스템 연동** | 문·승강기·출입통제·컨베이어·PLC·고정 센서와 작업을 연계한다 | 문·승강기·설비의 준비와 로봇의 도착을 어떻게 맞출 것인가? | [22. 설비·건물 시스템 연동](facility-and-building-system-integration.md) | published |
| **23. 업무 시스템 연동** | 업무 요청을 받아 작업으로 바꾸고, 진행·완료를 되돌려 반영한다 | 업무 시스템의 요청이 바뀌거나 취소되면 진행 중인 로봇 작업을 어떻게 바꿀 것인가? | [23. 업무 시스템 연동](business-system-integration.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

Open-RMF도 제조사별 Fleet Adapter와 건물 설비 인터페이스를 통해 로봇·문·승강기 등을 연결한다. **로봇 연결과 시설 연결을 함께 보는 것**이 필요하다. [4] [분류원문]

업무 시스템과 현장 운영·제어의 경계를 정리할 때는 ISA-95의 기업–제어 시스템 통합 관점이 참고가 된다. 실제 제품별로 업무 시스템·관제·ROP의 책임은 겹칠 수 있다. [2] [분류원문]

## 다른 대분류와의 연결

> **이전 분류 기준 내용.** 아래는 이전 분류(7개 대분류)에서 C. 연결·실행 기반 페이지에 2026-09-25 작성한 연결이다. 대분류 이름은 그때의 것이고, 링크는 새 영역 페이지로 옮겨 두었다. 새 17개 대분류 기준의 연결은 이어지는 조사에서 다시 쓴다.


C. 연결·실행 기반은 다른 대분류가 정한 업무·모델·계획을 로봇과 설비가 실제로 받는 명령과 상태로 옮기는 자리이므로, 다른 대분류와의 연결은 대부분 "무엇을 넘겨받고 무엇을 되돌려 주는가"의 문제로 나타난다. [의견] 이 절의 연결은 게시된 [20. 로봇·제조사 관제 연동](robot-and-vendor-fleet-manager-integration.md), [22. 설비·건물 시스템 연동](facility-and-building-system-integration.md), [42. 분산 시스템·통신·컴퓨팅 구조](../platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [29. 명령·작업 실행의 신뢰성](../execution-collaboration-and-recovery/command-and-task-execution-reliability.md) 페이지와 A. 업무·공급망 설계·B. 공통 정보·환경 모델 대분류 페이지의 검증된 주장을 다시 쓴 것이 많다. D. 계획·최적화부터 G. 안전·보안·지능·거버넌스까지의 세부영역은 대부분 아직 본문이 없어서, 상대편 쪽 서술도 C. 연결·실행 기반 쪽 근거에 기댄다.

```mermaid
flowchart LR
  C["C. 연결·실행 기반"]
  A["A. 업무·공급망 설계"]
  B["B. 공통 정보·환경 모델"]
  D["D. 계획·최적화"]
  E["E. 협업·현장 운영"]
  F["F. 도입·검증·유지관리"]
  G["G. 안전·보안·지능·거버넌스"]
  AI["47. AI·학습·적응과 모델 운영"]
  A -->|"작업 요청·변경·취소"| C
  B -->|"능력·좌표·적재물·상태"| C
  C -->|"교통 스케줄·충전·구역 점유"| D
  C -->|"오류·인계 결과·작업 기록"| E
  F -->|"설정·시뮬레이션·적합성 시험·수명주기"| C
  G -->|"안전·보안·표준 제약"| C
  AI -.->|"근거 없음"| C
```

### A. 업무·공급망 설계

[A. 업무·공급망 설계](../planning-and-business/index.md) 쪽에서 본 같은 연결은 그 페이지의 [다른 대분류와의 연결](../planning-and-business/index.md#다른-대분류와의-연결) 절에 같은 태그와 각주로 실려 있다.

- **20. 로봇·제조사 관제 연동 ↔ [23. 업무 시스템 연동](business-system-integration.md)**: VDA 5050 3.0.0 은 외부 IT 시스템과의 인터페이스를 범위에서 제외한다. 그래서 상위 주문을 Open-RMF 작업 요청 같은 로봇 작업 요청으로 번역하는 계층이 두 대분류가 일을 넘겨받는 지점이 될 것으로 보인다. [추정][^ref-031][^ref-125]
- **29. 명령·작업 실행의 신뢰성 ↔ 23. 업무 시스템 연동·[24. 작업·워크플로 모델링](../planning-and-optimization/task-and-workflow-modeling.md)**: 상위 쪽은 B2MML 거래 동사(CHANGE·CANCEL 등)와 OPC UA for ISA-95 Job Control 메서드(Update·Pause·Resume·Abort·Cancel 등)로 변경·취소를 표현한다. 로봇 쪽 Open-RMF 작업 상태는 queued·underway·completed·canceled·killed·failed 같은 상태 값과 취소·강제 종료 요청 기록을 담는다. [사실][^ref-129][^ref-130][^ref-111] 세 자료는 서로 다른 계층의 사례이며 같은 내용을 교차 확인한 것은 아니다.
- **29. 명령·작업 실행의 신뢰성 ↔ 23. 업무 시스템 연동**: Open-RMF 작업 요청·파견 요청 스키마에는 요청자가 정하는 요청 식별자 필드가 없다. 따라서 상위 요청 id 와 작업 id 의 대응을 ROP 쪽에서 보존해 중복을 걸러야 할 것으로 보인다. [추정][^ref-365][^ref-125][^ref-367] 그 대응을 얼마 동안 보존할지는 [열린 질문](../../open-questions.md) oq-046 으로 남아 있다.
- **22. 설비·건물 시스템 연동 ↔ [35. 처리능력·규모·배치 설계](../design-and-simulation/capacity-sizing-and-layout-design.md)**: 병원 약품 배송 로봇 사례에서 승강기 가동률이 높을수록 배송 실패가 많고 시간이 길었으며, 다층 호텔 배송 연구는 승강기를 경로 계획의 대기·운행 시간으로 모델링했다. [사실][^ref-060][^ref-103] 두 사례는 병원·호텔이며 물류센터 적용은 미확인이다(oq-010). 승강기 제어 자체는 분류 원문 19장 '시설·설비 제어' 경계의 연계 대상이며, 35. 처리능력·규모·배치 설계은 이를 제약 입력으로만 받는다. [의견]
- **22. 설비·건물 시스템 연동·42. 분산 시스템·통신·컴퓨팅 구조 ↔ 35. 처리능력·규모·배치 설계**: 국내에서 업무용 건축물 대상 로봇 친화형 건축물 인증을 아파트 단지로 확장한 인증 모델은 건축·시설 설계, 네트워크·시스템, 건축 운영 관리, 로봇 지원 4개 분야의 28개 항목(총점 176점)으로 구성된다(2023년 발행). [사실][^ref-409] 이 모델의 대상은 공동주택(아파트 단지)이며 물류센터가 아니다. 건물 설비와 통신 기반을 로봇 운영 조건으로 평가하는 이런 틀이 거점·설비 계획과 설비·통신 연동을 잇는 근거가 될 수 있다. [추정][^ref-409]
- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ 23. 업무 시스템 연동**: 외부망이 끊긴 동안 현장 관제는 이미 받은 주문을 이어 갈 수 있으나 클라우드 WMS 의 새 주문 수신과 재고 확정은 멈추고, CAP 제약에 따라 재연결 뒤 현장 완료 기록과 WMS 기록을 맞추는 절차가 필요할 것으로 보인다. [추정][^ref-031][^ref-300][^ref-310] 물류센터 운영 기준은 미확인이다(oq-038).

### B. 공통 정보·환경 모델

[B. 공통 정보·환경 모델](../robot-ontology/index.md) 페이지의 [다른 대분류와의 연결](../robot-ontology/index.md#다른-대분류와의-연결) 절에 같은 연결이 같은 각주로 있다.

- **20. 로봇·제조사 관제 연동 ↔ [5. 로봇 능력·작업 표현](../robot-ontology/robot-capability-and-task-representation.md)**: VDA 5050 팩트시트는 적재 명세(loadSets)와 지원 동작(mobileRobotActions)을, Open-RMF [플릿 어댑터](../../glossary/fleet-adapter.md) 템플릿 설정은 수행 가능한 작업 유형(task_capabilities)과 동작 이름(actions)을 선언한다. [사실][^ref-228][^ref-105]
- **20. 로봇·제조사 관제 연동 ↔ [15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md)**: 플릿 어댑터는 로봇 좌표계가 RMF 와 다르면 같은 위치를 가리키는 좌표 쌍으로 회전·축척·이동 변환을 추정하고, 템플릿 설정은 층별 reference_coordinates 로 이 좌표 쌍을 둔다. [사실][^ref-153][^ref-105] 이 작업이 용어집의 [지도 정합](../../glossary/map-alignment.md)이다.
- **22. 설비·건물 시스템 연동 ↔ 15. 지도·공간·위치 모델**: Open-RMF 승강기 상태는 층을 층 이름 문자열(available_floors, current_floor, destination_floor)로 나타내므로, 지도의 층 이름과 승강기 층 이름을 맞추는 대응이 필요할 것으로 보인다. [추정][^ref-286][^ref-079] 대응 규칙을 정한 표준은 미확인이다(oq-045).
- **20. 로봇·제조사 관제 연동 ↔ [17. 작업 대상·자산 식별과 인계 추적](../objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md)**: VDA 5050 상태 스키마의 적재물 목록(loads)은 적재 상태를 판단할 수 없는 로봇이 생략할 수 있고, 적재물 식별 번호(loadId)는 바코드·RFID 같은 식별 값이며 아직 식별하지 않았으면 비워 둔다. [사실][^ref-051]
- **22. 설비·건물 시스템 연동 ↔ [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md)**: Open-RMF 문·승강기 상태 메시지는 시각 필드(door_time, lift_time)를 담고, [승강기 어댑터](../../glossary/lift-adapter.md)는 적절하다고 판단한 요청만 승강기에 전달한다. [사실][^ref-285][^ref-286][^ref-284] 상태를 몇 초까지 믿을지 정한 규칙은 미확인이다(oq-034).
- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ 18. 실시간 세계 상태·데이터 일관성**: ROS 2 QoS 의 기한·생존성 정책, Sparkplug 의 노드 종료 뒤 지표 STALE 표시, VDA 5050 의 MQTT 유언을 통한 연결 끊김 통지처럼 통신 계층에 상태의 오래됨을 알리는 장치가 있다. [사실][^ref-282][^ref-287][^ref-031] 이 연결은 현재 상태를 표현하는 쪽이며, 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈과는 아래 F. 도입·검증·유지관리 항목에서 따로 다룬다.

### D. 계획·최적화

- **20. 로봇·제조사 관제 연동 ↔ [27. 다중 로봇 경로·교통 관리 — MAPF](../planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md)**: [D. 계획·최적화](../planning-and-optimization/index.md)의 교통 관리와 관련해, Open-RMF 플릿 어댑터는 로봇의 예상 이동 경로를 시설 전체의 중앙 교통 스케줄에 보고해 플릿 사이 충돌을 찾아 협상하게 하며, 제조사 관제가 허용하는 제어 수준에 따라 전체 제어·신호등·읽기 전용 가운데 하나로 붙는다. [사실][^ref-004][^ref-251] 제어 수준별 교통 성능 차이는 미확인이다(oq-032).
- **20. 로봇·제조사 관제 연동 ↔ [25. 작업 배정 — MRTA](../planning-and-optimization/task-allocation-mrta.md)**: 플릿 어댑터 템플릿 설정은 배터리가 recharge_threshold 아래로 내려간 로봇에게 작업을 맡기지 않게 하고, 충전 목표·로봇별 충전기·작업 종료 후 동작(park·charge·nothing)을 둔다. [사실][^ref-105]
- **22. 설비·건물 시스템 연동 ↔ [28. 공용 자원·충전·에너지 최적화](../planning-and-optimization/shared-resource-charging-and-energy-optimization.md)**: Open-RMF 승강기 요청은 세션 단위로 승강기를 점유하고 AGV 모드에서는 정지 시 문이 열려 있으며, VDA 5050 3.0.0 은 [해제 구역](../../glossary/release-zone.md) 진입 요청에 관제가 허가·대기·철회·거절로 답하게 한다. [사실][^ref-312][^ref-031] 이런 점유·허가 정보가 승강기와 구역을 공용 자원으로 예약·배분하는 입력이 될 것으로 보인다. [추정][^ref-312][^ref-031]
- **29. 명령·작업 실행의 신뢰성 ↔ [26. 작업 순서·스케줄링](../planning-and-optimization/task-sequencing-and-scheduling.md)**: VDA 5050 에서 이미 로봇에 넘긴 기반(base) 경로는 바꿀 수 없으므로, 우선순위 변경에 따른 재정렬은 아직 해제하지 않은 호라이즌 구간과 새 주문에만 적용할 수 있을 것으로 보인다. [추정][^ref-031]

### E. 협업·현장 운영

- **22. 설비·건물 시스템 연동 ↔ [30. 로봇 간 협업·물리적 인계](../execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md)**: [E. 협업·현장 운영](../execution-collaboration-and-recovery/index.md)의 물리적 인계와 관련해, Open-RMF 배송 작업에서 로봇은 하역 지점 워크셀([디스펜서·인제스터](../../glossary/dispenser-ingestor.md))에 IngestorRequest 를 보내고 IngestorResult 를 받을 때까지 반복하며, IngestorResult 는 시각·요청 id·워크셀 id·상태(ACKNOWLEDGED·SUCCESS·FAILED)를 담는다. [사실][^ref-023][^ref-049] 인수 결과를 화물 식별·인계 기록과 잇는 방법은 열린 질문으로 남아 있다(oq-001, oq-042).
- **20. 로봇·제조사 관제 연동 ↔ [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md)**: VDA 5050 의 주문 거절 오류(NO_ROUTE_TO_TARGET 등)·연결 단절(CONNECTION_BROKEN)과 Open-RMF 로봇 상태 error 를 공통 예외로 옮긴 뒤 재배정이나 사람 확인으로 넘기는 것이 두 대분류의 인계 지점이 될 것으로 보인다. [추정][^ref-031][^ref-148] 공통 상태·오류 어휘 매핑은 미확인이다(oq-033).
- **29. 명령·작업 실행의 신뢰성 ↔ 32. 예외 복구·재계획·업무 연속성**: Open-RMF 저장소 이슈 #224 는 플릿 어댑터가 재시작되면 배정된 작업이 사라진다고 지적하고, 작업 로그·백업을 SQLite 에 저장해 복구하는 기능이 별도 풀 리퀘스트로 제안되었다고 적는다. [사실][^ref-374] 현재 배포판 반영 여부는 미확인이다(oq-048).
- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ 32. 예외 복구·재계획·업무 연속성**: VDA 5050 3.0.0 에서 로봇은 브로커와 연결이 끊겨도 받은 주문 정보를 유지하고, 명세 표현으로 "fulfills the order up to the last released node", 곧 마지막으로 해제된 노드까지 주문을 수행한다. [사실][^ref-031]
- **29. 명령·작업 실행의 신뢰성 ↔ [38. 모니터링·이상 탐지·원인 분석](../field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md)**: Open-RMF 작업 상태 기록(취소·강제 종료·중단 요청, 시작·종료 시각)이 이상 탐지와 원인 분석의 입력이 될 것으로 보인다. [추정][^ref-111]

### F. 도입·검증·유지관리

- **20. 로봇·제조사 관제 연동 ↔ [55. 현장 조사·설치·시운전](../verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md)**: [F. 도입·검증·유지관리](../verification-deployment-and-lifecycle/index.md)의 온보딩과 관련해, 새 플릿을 붙일 때 플릿 어댑터 설정에 층별 기준 좌표 쌍·충전기·지원 작업·동작을 채우는 일이 로봇 등록·지도 설정의 반복 작업이 될 것으로 보인다. [추정][^ref-105][^ref-153] 온보딩 소요를 측정한 자료는 확인하지 못했다.
- **22. 설비·건물 시스템 연동 ↔ [34. 시뮬레이션·예측용 디지털 트윈](../design-and-simulation/simulation-and-predictive-digital-twin.md)**: Open-RMF 문서는 traffic-editor 로 주석한 지도에서 문·승강기·워크셀(TeleportDispenser·TeleportIngestor)을 포함한 시뮬레이션 세계를 생성하고, 여러 플릿의 승강기 요청을 조율하는 lift_supervisor 까지 재현하는 흐름을 제시한다. [사실][^ref-406] 이는 가정한 운영 상황을 가상으로 실험하는 쪽이며, 현재 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성의 문·승강기 상태 메시지와는 구분한다.
- **22. 설비·건물 시스템 연동 ↔ [54. 시험·형식 검증·벤치마크](../verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md)**: 같은 문서는 이렇게 만든 시뮬레이션으로 배치 전에 설비 연동을 시험해 시간과 자원을 아낄 수 있다고 설명한다. [사실][^ref-406]
- **20. 로봇·제조사 관제 연동·29. 명령·작업 실행의 신뢰성 ↔ 54. 시험·형식 검증·벤치마크**: 공개 오픈소스 가운데 VDA 5050 3.0.0 로봇 플릿 시뮬레이터(vda5050-sim)는 주문 수명주기·사전 정의 동작·교통 제어 의미를 명세와 대조하는 적합성 시험 묶음과 고장 주입을 둔다고, MQTT 기록 진단 도구(vda5050-lab)는 반복된 주문·갱신 id, 기반·호라이즌 연결, 재연결 뒤 연결 상태, 취소·동작 수명주기 불일치를 진단한다고 각각 README 에 적는다. [사실][^ref-407][^ref-408] 두 도구는 개인 프로젝트의 자기 기술이며 VDA·VDMA 공식 적합성 시험이 아니다.
- **29. 명령·작업 실행의 신뢰성 ↔ [57. 자산·소프트웨어 수명주기 관리](../verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md)**: ROS 2 [관리형 노드](../../glossary/managed-node.md)는 Unconfigured·Inactive·Active·Finalized 상태와 configure·activate·deactivate·cleanup·shutdown 같은 전이를 두어, 감독 도구가 모든 구성요소가 올바르게 준비됐는지 확인한 뒤 실행을 허용하게 한다. [사실][^ref-364]

### G. 안전·보안·지능·거버넌스

- **22. 설비·건물 시스템 연동 ↔ [48. 안전·위험 관리](../safety/safety-and-risk-management.md)**: [G. 안전·보안·지능·거버넌스](../governance-law-and-society/index.md)의 안전 관리와 관련해, 국가기술표준원은 2021년 11월 이동 로봇의 엘리베이터 탑승 안전 요구사항과 평가 방법을 정한 KS B 7317 을 제정했고, Open-RMF 승강기 상태의 운영 모드에는 사람·AGV·화재·오프라인·비상이 있다. [사실][^ref-314][^ref-315][^ref-286] ROP 는 운영 모드 확인과 작업·경로 제약 반영만 맡고, 승강기 탑승 안전과 설비 안전 제어 자체는 분류 원문 19장 '시설·설비 제어' 경계의 연계 대상이다. [의견]
- **42. 분산 시스템·통신·컴퓨팅 구조·20. 로봇·제조사 관제 연동 ↔ [51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md)**: ROS 2 는 [DDS 보안 규격](../../glossary/dds-security.md)의 인증(PKI)·접근통제(거버넌스·권한 파일)·암호화 플러그인을 쓴다. Open-RMF 문서는 같은 신원과 접근통제 규칙을 공유하는 프로세스 묶음인 SROS 2 인클레이브로 RMF 구성요소의 권한을 나누고, 웹 대시보드에는 TLS·OIDC 인증을 더한다고 설명한다. [사실][^ref-009][^ref-405]
- **22. 설비·건물 시스템 연동 ↔ 51. 인증·권한·격리**: 로봇 관제가 문·승강기 어댑터에 요청을 보내는 구조에서는 어느 관제 구성요소가 어떤 설비 명령을 낼 수 있는지를 인클레이브·권한 파일 같은 접근통제 단위로 정해야 할 것으로 보인다. [추정][^ref-405][^ref-283][^ref-284] 출입통제 시스템 연동 사례는 미확인이다(oq-043).
- **20. 로봇·제조사 관제 연동 ↔ [21. 상호운용 표준·적합성](interoperability-standards-and-conformance.md)**: 제조사 중립 연동의 기준으로 VDA 5050(관제–이동로봇 통신), MassRobotics AMR 상호운용 표준(상태 보고), 그리고 개발 중인 국제표준 ISO 21423(산업용 이동로봇의 통신·상호운용성, 검색 결과상 FDIS 단계, 발행 여부 미확인)이 있다. [사실][^ref-031][^ref-253][^ref-159]
- **20. 로봇·제조사 관제 연동 ↔ 21. 상호운용 표준·적합성**: 이번에 확인한 VDA 5050 적합성 시험 도구가 제3자 오픈소스뿐이라, 어느 시험 결과를 연동 승인 기준으로 삼고 누가 연동 오류를 판정할지가 거버넌스 과제로 넘어갈 것으로 보인다. [추정][^ref-407][^ref-408][^ref-031] VDA 공식 적합성 인증 절차가 없다는 것은 확정된 사실이 아니다.
- **22. 설비·건물 시스템 연동 ↔ 21. 상호운용 표준·적합성**: 국내에서는 대한승강기협회가 엘리베이터와 로봇의 연동을 위한 단체표준을 제정했다고 전해진다(기사 보도 기준, 단체표준 원문·발행일 미확인). [추정][^ref-316][^ref-317] 표준이 정하는 메시지 내용은 oq-041 로 남아 있다.

### 아직 다루지 않은 연결

- **[47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md)**: 이번 조사에서 C. 연결·실행 기반의 네 세부영역과 47. AI·학습·적응과 모델 운영을 잇는 검증된 근거를 찾지 못했다. 위의 29. 명령·작업 실행의 신뢰성 ↔ 38. 모니터링·이상 탐지·원인 분석 연결도 AI 기반 장애 분석이 아니라 작업 기록을 입력으로 쓰는 일반 연결로만 적었다.
- **[31. 사람–로봇 협업](../execution-collaboration-and-recovery/human-robot-collaboration.md)**, **[39. 운영 성과 측정·개선](../field-operations-and-monitoring/operational-performance-measurement-and-improvement.md)**: 이번 실행에서는 C. 연결·실행 기반과 잇는 근거를 조사하지 않았다.
- 새로 올린 열린 질문: VDA 5050 공식 적합성 시험·인증 절차의 유무와 제3자 시험 결과의 승인 기준 활용, 그리고 로봇 관제·플릿 어댑터·승강기·문 어댑터에 SROS 2 인클레이브와 권한 파일을 나누는 공개 구성 사례. 두 질문은 [열린 질문](../../open-questions.md) 목록에 등록된다.

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 91건이다(논문 12건 · 기사·보고서 10건 · 업체 발표 3건 · 표준·오픈소스·기관 자료 66건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-260](../../references/ref-260.md) — ScienceDirect 게재 논문(저자 미확인), Heterogeneous multi-agent fleet control system for material handling in a Software-Defined Factory (발행 2026)
- [ref-163](../../references/ref-163.md) — 노주형, 강규리, 김연찬, 심현철(로봇학회 논문지), 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템 (발행 2026)
- [ref-060](../../references/ref-060.md) — Lee, Y. 외(Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments (발행 2026)
- [ref-321](../../references/ref-321.md) — Electronics(MDPI) 게재 논문(저자 미확인), Efficient Graph-Based Multi-Story Path Planning with Optimized Elevator Selection for Indoor Delivery Robots (발행 2025)
- [ref-136](../../references/ref-136.md) — Applied Sciences(MDPI) 게재 논문 저자(미확인), Integrated Fleet Management of Mobile Robots for Enhancing Industrial Efficiency: A Case Study on Interoperability in Multi-Brand Environments Within the Automotive Sector (발행 2025)
- [ref-133](../../references/ref-133.md) — Lorenz, Otto, & Gendreau (Networks, Wiley), Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization? (발행 2025)
- [ref-132](../../references/ref-132.md) — Yu, S., & Srinivas, S., Collaborative Human–Robot Teaming for Dynamic Order Picking: Interventionist strategies for improving warehouse intralogistics operations (발행 2025)
- [ref-409](../../references/ref-409.md) — 한국 학술지 게재 논문(지적과 국토정보 53(1), 83-105, 저자 미확인), 아파트 단지의 로봇 친화형 환경 인증 모델 개발 (지적과 국토정보 53(1), 83-105) (발행 2023)
- [ref-259](../../references/ref-259.md) — Franke, S., Lünsch, D., Jost, J., & Roidl, M., Identification of requirements and opportunities for new types of standardized interfaces for AGV systems based on the VDA 5050 concept (발행 2023)
- [ref-134](../../references/ref-134.md) — Gallien, J., & Weber, T. G., To Wave or Not to Wave? Order Release Policies for Warehouses with an Automated Sorter (발행 2010)
- 그 밖에 2건

**기사·보고서**

- [ref-264](../../references/ref-264.md) — 머니투데이, "로봇 통합 관제 기술, 인정받았다"..노바테크, 70억원 투자 유치 (발행 2026-07-14)
- [ref-263](../../references/ref-263.md) — 디지털투데이, 카카오모빌리티, 로봇 플랫폼 사업 본격화..."이기종 로봇 통합 운영" (발행 2026-05)
- [ref-137](../../references/ref-137.md) — 머니투데이, 물류센터 관리시스템에 로봇 연동…"물류 자동화 새 표준 만든다" (발행 2025-01)
- [ref-002](../../references/ref-002.md) — ISA, Update to ISA-95 Standard Addresses Integration of Enterprise and Manufacturing Control Systems (발행 2025)
- [ref-320](../../references/ref-320.md) — 파이낸셜뉴스, 현대엘리베이터 '오픈 API' 참여 다각화..."엘리베이터와 로봇 연동" (발행 2023-02)
- [ref-319](../../references/ref-319.md) — 한국경제, 현대엘리베이터, 엘리베이터-로봇 연계 가능한 '오픈 API' 공개 (발행 2022-03)
- [ref-317](../../references/ref-317.md) — 전기신문, 승강기협회 '로봇-승강기 연동 표준개발'로 승강기 4차산업 견인 (발행 미확인)
- [ref-316](../../references/ref-316.md) — 건설기술신문, 승강기협, 엘리베이터-로봇 연동 단체표준 제정 (발행 미확인)
- [ref-261](../../references/ref-261.md) — 헬로티(HelloT), 미르, 다기종 모바일 로봇 연동 SW 어댑터 ‘MiR VDA 5050’ 론칭 (발행 미확인)
- [ref-257](../../references/ref-257.md) — Interact Analysis, AMR Multi-Fleet Orchestration Software Explained (발행 미확인)

**업체 발표**

- [ref-608](../../references/ref-608.md) — OTTO by Rockwell Automation, OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments (발행 2026-04)
- [ref-318](../../references/ref-318.md) — KONE, KONE Service Robot API (발행 미확인)
- [ref-262](../../references/ref-262.md) — 클로봇(Clobot), 통합 로봇 관제 플랫폼 크롬스[CROMS] (발행 미확인)

**표준·오픈소스·기관 자료**

- [ref-032](../../references/ref-032.md) — VDA(Verband der Automobilindustrie), Version 3.0 of VDA 5050 released (발행 2026-04)
- [ref-710](../../references/ref-710.md) — 한국지능형로봇표준포럼(KOROS), KOROS 1148-8:2025 서비스 로봇을 위한 모듈 - 제2-8부 : 소프트웨어 모듈용 정보모델 상호운용성 시험 절차 (발행 2025-06-04)
- [ref-560](../../references/ref-560.md) — ISO, ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells (발행 2025-02)
- [ref-135](../../references/ref-135.md) — ASCM, SCOR Digital Standard — Introduction and Front Matter (SCOR Version 14.0, 2025) (발행 2025)
- [ref-704](../../references/ref-704.md) — Open Source Robotics Alliance, Charter of the Open Source Robotics Alliance Project 'Open-RMF' (발행 2024-03)
- [ref-130](../../references/ref-130.md) — OPC Foundation, UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv) (발행 2024-01-31)
- [ref-636](../../references/ref-636.md) — European Union (EUR-Lex), Regulation (EU) 2023/2854 of the European Parliament and of the Council of 13 December 2023 on harmonised rules on fair access to and use of data (Data Act) (발행 2023-12-13)
- [ref-129](../../references/ref-129.md) — MESA International, B2MML-BatchML/Schema/B2MML-TransactionProfile.xsd (발행 2023)
- [ref-637](../../references/ref-637.md) — 국가법령정보센터(산업통상자원부), 산업 디지털 전환 촉진법 (법률 제18692호) (발행 2022-01-04)
- [ref-709](../../references/ref-709.md) — 대한민국 정책브리핑(산업통상자원부 국가기술표준원), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 (발행 2021-11-11)
- 그 밖에 56건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-25 · 갱신 · [21. 상호운용 표준·적합성](interoperability-standards-and-conformance.md) — seed → draft: 3~11절 첫 작성, 페이지 상태 자동 영역 추가, 13절 각주. 2차: 9절 승강기 연계 칸 [추정]으로 정정, ISO 10218-2 적용 범위 미확인 단서 추가, 5절 시작 조건 칸에 가상 설정 표시와 [추정] 태그 추가 (실행 2026-09-25-69)
- 2026-09-25 · 생성 · [21. 상호운용 표준·적합성 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area28-s7.md) — 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,840자)을 옮겼다 (실행 2026-09-25-69)
- 2026-09-25 · 생성 · [21. 상호운용 표준·적합성 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area28-s6.md) — 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "6. 대표 접근법과 기술" 절(1,549자)을 옮겼다 (실행 2026-09-25-69)
- 2026-09-25 · 생성 · [21. 상호운용 표준·적합성 — 열린 질문](../../topics/2026/2026-09-25-area28-s11.md) — 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "11. 열린 질문" 절(1,233자)을 옮겼다 (실행 2026-09-25-69)
- 2026-09-25 · 생성 · [21. 상호운용 표준·적합성 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area28-s4.md) — 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "4. 핵심 개념과 용어" 절(1,053자)을 옮겼다 (실행 2026-09-25-69)
<!-- auto:category-recent:end -->

## 참고 자료

원문의 [4]는 참고문헌 [ref-004](../../references/ref-004.md)에 해당한다.[^ref-004] 원문의 [2]는 참고문헌 [ref-002](../../references/ref-002.md)에 해당한다.[^ref-002]

[^ref-002]: ISA, Update to ISA-95 Standard Addresses Integration of Enterprise and Manufacturing Control Systems, 2025, https://www.isa.org/news-press-releases/2025/april/update-to-isa-95-standard-addresses-integration-of, 접근일 2026-09-28

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-24
[^ref-009]: ROS 2 Design, ROS 2 DDS-Security Integration, 미확인, https://design.ros2.org/articles/ros2_dds_security.html, 접근일 2026-09-25
[^ref-023]: Open Robotics, Workcells - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_workcells.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-049]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_ingestor_msgs/msg/IngestorResult.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_ingestor_msgs/msg/IngestorResult.msg, 접근일 2026-09-25 (원문 미열람)
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25 (원문 미열람)
[^ref-060]: Lee, Y. 외(Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026, https://doi.org/10.1177/20552076261437181, 접근일 2026-09-25 (원문 미열람)
[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-25 (원문 미열람)
[^ref-103]: PMC 게재 논문(저자 미확인), The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments, 미확인, https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/, 접근일 2026-09-25 (원문 미열람)
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-09-25 (원문 미열람)
[^ref-111]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json, 접근일 2026-09-25 (원문 미열람)
[^ref-125]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-09-25 (원문 미열람)
[^ref-129]: MESA International, B2MML-BatchML/Schema/B2MML-TransactionProfile.xsd, 2023, https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-TransactionProfile.xsd, 접근일 2026-09-25 (원문 미열람)
[^ref-130]: OPC Foundation, UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv), 2024-01-31, https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL, 접근일 2026-09-25 (원문 미열람)
[^ref-148]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json, 접근일 2026-09-25 (원문 미열람)
[^ref-153]: Open Robotics, Fleet Adapter Tutorial - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html, 접근일 2026-09-25 (원문 미열람)
[^ref-159]: ISO, ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability, 미확인, https://www.iso.org/standard/86749.html, 접근일 2026-09-25 (원문 미열람)
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25 (원문 미열람)
[^ref-251]: Open Robotics, Mobile Robot Fleets (integration_fleets) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets.html, 접근일 2026-09-25 (원문 미열람)
[^ref-253]: MassRobotics, MassRobotics-AMR/AMR_Interop_Standard — README, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard, 접근일 2026-09-25 (원문 미열람)
[^ref-282]: Open Robotics (ROS 2 Documentation), Quality of Service settings — ROS 2 Documentation: Jazzy, 미확인, https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html, 접근일 2026-09-25 (원문 미열람)
[^ref-283]: Open Robotics, Doors (integration_doors) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_doors.html, 접근일 2026-09-25 (원문 미열람)
[^ref-284]: Open Robotics, Lifts (integration_lifts) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_lifts.html, 접근일 2026-09-25 (원문 미열람)
[^ref-285]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_door_msgs/msg/DoorState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorState.msg, 접근일 2026-09-25 (원문 미열람)
[^ref-286]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg, 접근일 2026-09-25 (원문 미열람)
[^ref-287]: Eclipse Foundation (eclipse-sparkplug GitHub), Sparkplug Specification — Chapter 5 Operational Behavior (Sparkplug_5_Operational_Behavior.adoc), 미확인, https://github.com/eclipse-sparkplug/sparkplug/blob/master/specification/src/main/asciidoc/chapters/Sparkplug_5_Operational_Behavior.adoc, 접근일 2026-09-25 (원문 미열람)
[^ref-300]: KubeEdge (CNCF, kubeedge GitHub), KubeEdge — README, 미확인, https://github.com/kubeedge/kubeedge, 접근일 2026-09-25 (원문 미열람)
[^ref-310]: Gilbert, S., & Lynch, N., Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services, 2002-06, https://dl.acm.org/doi/10.1145/564585.564601, 접근일 2026-09-25 (원문 미열람)
[^ref-312]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg, 접근일 2026-09-25 (원문 미열람)
[^ref-314]: 국가표준인증통합정보시스템(KSSN), KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법, 2021-11, https://www.kssn.net/search/stddetail.do?itemNo=K001010135682, 접근일 2026-09-25 (원문 미열람)
[^ref-315]: 산업통상자원부 국가기술표준원(대한민국 정책브리핑), 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 2021-11, https://www.korea.kr/briefing/pressReleaseView.do?newsId=156480155, 접근일 2026-09-25 (원문 미열람)
[^ref-316]: 건설기술신문, 승강기협, 엘리베이터-로봇 연동 단체표준 제정, 미확인, https://www.ctman.kr/35296, 접근일 2026-09-25 (원문 미열람)
[^ref-317]: 전기신문, 승강기협회 '로봇-승강기 연동 표준개발'로 승강기 4차산업 견인, 미확인, https://www.electimes.com/news/articleView.html?idxno=320147, 접근일 2026-09-25 (원문 미열람)
[^ref-364]: ROS 2 Design, Managed nodes (ROS 2 Design: node_lifecycle), 미확인, https://design.ros2.org/articles/node_lifecycle.html, 접근일 2026-09-25
[^ref-365]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/dispatch_task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/dispatch_task_request.json, 접근일 2026-09-25 (원문 미열람)
[^ref-367]: IETF HTTPAPI Working Group (Jena, J., & Dalal, S.), The Idempotency-Key HTTP Header Field (draft-ietf-httpapi-idempotency-key-header), 미확인, https://github.com/ietf-wg-httpapi/idempotency/blob/main/draft-ietf-httpapi-idempotency-key-header.md, 접근일 2026-09-25 (원문 미열람)
[^ref-374]: Open Robotics (open-rmf/rmf_ros2 GitHub), Task recovery when fleet adapter get restarted · Issue #224 · open-rmf/rmf_ros2, 미확인, https://github.com/open-rmf/rmf_ros2/issues/224, 접근일 2026-09-25 (원문 미열람)
[^ref-405]: Open Robotics, Security - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/security.html, 접근일 2026-09-25
[^ref-406]: Open Robotics, Simulation - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-09-25
[^ref-407]: gpue (GitHub), vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS), 미확인, https://github.com/gpue/vda5050-sim, 접근일 2026-09-25
[^ref-408]: ekusiadadus (GitHub), vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces), 미확인, https://github.com/ekusiadadus/vda5050-lab, 접근일 2026-09-25
[^ref-409]: 한국 학술지 게재 논문(지적과 국토정보 53(1), 83-105, 저자 미확인), 아파트 단지의 로봇 친화형 환경 인증 모델 개발 (지적과 국토정보 53(1), 83-105), 2023, https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART002978381, 접근일 2026-09-25 (원문 미열람)
````

### docs/categories/integration/robot-and-vendor-fleet-manager-integration.md (요약)

```markdown
# 20. 로봇·제조사 관제 연동

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

제조사 API·SDK·관제 시스템과 연결하는 어댑터, 공통 명령·관측 계약, 로봇과 주고받는 통신 방식 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **로봇·제조사 관제 연동 어댑터**: 제조사 API·SDK·관제 시스템을 연결해 명령·상태·오류를 변환하는 어댑터를 만든다
- **제어 위임 수준 결정**: 로봇을 하나씩 직접 제어할지, 제조사 관제에 임무 단위로 맡길지 정한다
- **공통 명령·관측 계약**: 단위와 시각 기준을 명시한 제조사 중립 명령·관측 형식을 정한다
- **로봇 통신 방식·메시징**: 명령·상태·지도·영상 데이터를 어떤 통신 방식(MQTT·DDS·gRPC·WebRTC 등)과 주기로 주고받을지 정하고 끊김·지연에 대비한다

이전 분류(2026-09-24)에서 이 페이지는 옛 9번 영역 ‘로봇·제조사 관제 연동’(옛 대분류 C. 연결·실행 기반)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 제조사 API·SDK·표준 프로토콜을 연결하고 명령·상태·오류를 변환하는 어댑터 [옛 분류원문]

> 옛 질문: 개별 로봇을 제어할까, 제조사 관제에 미션을 맡길까? [옛 분류원문]

## 2. 핵심 질문

로봇을 하나씩 직접 움직일지, 제조사 관제에 맡길지, 어떤 방식으로 통신할지 어떻게 정할 것인가? [분류원문]
```

### docs/categories/integration/interoperability-standards-and-conformance.md (요약)

```markdown
# 21. 상호운용 표준·적합성

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

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
```

### docs/categories/integration/facility-and-building-system-integration.md (요약)

```markdown
# 22. 설비·건물 시스템 연동

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

문·승강기·출입통제·컨베이어·PLC·고정 센서와 작업을 연계한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **설비·건물 연동**: 문·승강기·출입통제·컨베이어·자동창고·PLC·빌딩 관리 시스템과 작업을 연계한다
- **승강기·문 예약과 연동**: 승강기와 문을 예약하고 로봇의 진입과 설비 상태를 맞물려 확인한다
- **로봇–설비 작업 동기화**: 컨베이어·작업대 준비와 로봇 도착처럼 설비와 로봇의 시점을 맞춘다
- **IoT·고정 센서 연동**: 고정 카메라·출입 센서·환경 센서처럼 로봇 밖의 센서 데이터를 연결한다

이전 분류(2026-09-24)에서 이 페이지는 옛 10번 영역 ‘설비·건물 시스템 연동’(옛 대분류 C. 연결·실행 기반)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 컨베이어, 자동창고, 작업대, PLC, 문, 승강기, 출입통제 시스템과 작업을 연계 [옛 분류원문]

> 옛 질문: 컨베이어 준비와 로봇 도착을 어떻게 맞출까? [옛 분류원문]

## 2. 핵심 질문

문·승강기·설비의 준비와 로봇의 도착을 어떻게 맞출 것인가? [분류원문]
```

### docs/categories/integration/business-system-integration.md (요약)

```markdown
# 23. 업무 시스템 연동

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

업무 요청을 받아 작업으로 바꾸고, 진행·완료를 되돌려 반영한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **업무 요청 수신·작업 변환**: 작업 요청을 만드는 업무 시스템(ERP·WMS·MES·병원 정보 시스템·호텔 객실 관리·빌딩 관리 등)에서 요청을 받아 로봇 작업으로 바꾼다
- **진행·완료 반영과 요청 변경 처리**: 작업 진행·완료를 업무 시스템에 되돌려 반영하고, 요청의 우선순위 변경·취소를 진행 중인 로봇 작업에 반영한다

이전 분류(2026-09-24)에서 이 페이지는 옛 1번 영역 ‘주문·업무 시스템 연계’(옛 대분류 A. 업무·공급망 설계)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: ERP, WMS, MES, WES, TMS의 주문·재고·생산 요청을 받아 작업으로 변환하고, 변경·취소·완료를 다시 반영하는 방법 [옛 분류원문]

> 옛 질문: 출고 우선순위가 바뀌면 이미 진행 중인 로봇 작업을 어떻게 바꿀까? [옛 분류원문]

## 2. 핵심 질문

업무 시스템의 요청이 바뀌거나 취소되면 진행 중인 로봇 작업을 어떻게 바꿀 것인가? [분류원문]
```

### docs/categories/planning-and-optimization/index.md

````markdown
---
title: "G. 계획·최적화"
type: category
status: published
created: 2026-09-24
updated: 2026-09-25
version: 2
sources: [ref-005, ref-006, ref-004, ref-031, ref-051, ref-079, ref-090, ref-104, ref-105, ref-109, ref-117, ref-125, ref-132, ref-133, ref-134, ref-146, ref-168, ref-186, ref-188, ref-199, ref-228, ref-236, ref-237, ref-267, ref-286, ref-312, ref-376, ref-381, ref-385, ref-388, ref-398, ref-399, ref-401, ref-402, ref-403, ref-405, ref-531, ref-533, ref-493, ref-494]
---

[홈](../../index.md) › G. 계획·최적화

# G. 계획·최적화

## 핵심 질문

누가, 언제, 어디로, 어떤 자원을 써서 일할 것인가? [분류원문]

## 개요

작업을 모델링·분해하고, 로봇에 배정하고, 순서·경로·공용 자원·충전을 최적화하는 결정 알고리즘. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **24. 작업·워크플로 모델링** | 현장 업무를 단계·선후관계·완료 조건으로 정의하고, 계획과 실행이 따를 운영 정책을 정한다 | 현장 업무를 로봇이 실행할 수 있는 단계와 완료 조건으로 어떻게 나눌 것인가? | [24. 작업·워크플로 모델링](task-and-workflow-modeling.md) | published |
| **25. 작업 배정 — MRTA** | 작업을 로봇 또는 로봇 팀에 배정한다 | 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? | [25. 작업 배정 — MRTA](task-allocation-mrta.md) | published |
| **26. 작업 순서·스케줄링** | 순서·시간 제약·긴급 삽입을 다루고, 계속 들어오는 작업에 맞춰 다시 계획한다 | 일이 계속 새로 들어올 때 무엇을 먼저, 언제 할지 어떻게 정할 것인가? | [26. 작업 순서·스케줄링](task-sequencing-and-scheduling.md) | published |
| **27. 다중 로봇 경로·교통 관리 — MAPF** | 여러 로봇의 경로·통과 시점·우선권을 조율한다 | 서로 다른 제조사의 로봇이 좁은 통로에서 마주치면 누가 양보할까? | [27. 다중 로봇 경로·교통 관리 — MAPF](multi-robot-path-and-traffic-management-mapf.md) | published |
| **28. 공용 자원·충전·에너지 최적화** | 공용 자원을 예약·배분하고 충전·에너지를 계획한다 | 로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까? | [28. 공용 자원·충전·에너지 최적화](shared-resource-charging-and-energy-optimization.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

로봇 운영에서는 **작업이 계속 새로 들어오는 조건**이 중요하다. 정해진 목적지까지 한 번 이동하는 문제와 요청이 계속 들어오는 운영은 다르다. 이를 다루는 연구가 *Lifelong MAPF*, *Multi-Agent Pickup and Delivery*이다. [5][6] [분류원문]

## 다른 대분류와의 연결

> **이전 분류 기준 내용.** 아래는 이전 분류(7개 대분류)에서 D. 계획·최적화 페이지에 2026-09-25 작성한 연결이다. 대분류 이름은 그때의 것이고, 링크는 새 영역 페이지로 옮겨 두었다. 새 17개 대분류 기준의 연결은 이어지는 조사에서 다시 쓴다.


D. 계획·최적화의 네 세부영역은 다른 대분류에서 주문·능력·지도·상태를 입력으로 받고, 결정한 배정·순서·경로·충전 계획을 실행 기반에 넘긴다. 아래 연결은 게시된 세부영역 페이지의 검증된 주장과, 이번 실행에서 공식 저장소 원문을 다시 연 자료(확인일 2026-09-25)에 기댄다. 연결 대부분은 단일 출처에 기대고 교차 확인되지 않았다. E. 협업·현장 운영, F. 도입·검증·유지관리, G. 안전·보안·지능·거버넌스의 세부영역 다수가 아직 심화되지 않아 그쪽 연결은 D. 계획·최적화 쪽 근거에 기댄다.

```mermaid
flowchart LR
  A[A. 업무·공급망 설계] -->|주문·시작 시각·우선순위| D[D. 계획·최적화]
  B[B. 공통 정보·환경 모델] -->|능력·경로망·배터리 상태| D
  D -->|배정·순서·경로·충전 결정| C[C. 연결·실행 기반]
  C -->|입찰·제어 수준·세션 제약| D
  D ---|사람 협업·인계·모니터링·예외 복구| E[E. 협업·현장 운영]
  F[F. 도입·검증·유지관리] -->|시뮬레이션·벤치마크·현장 설정| D
  G[G. 안전·보안·지능·거버넌스] -->|안전·보안·AI·표준 제약| D
```

### [옛 A. 업무·공급망 설계](../planning-and-business/index.md)

- **[25. 작업 배정 — MRTA](task-allocation-mrta.md) ↔ [23. 업무 시스템 연동](../integration/business-system-integration.md)**: VDA 5050 명세(3.0.0 판)는 이동로봇에 대한 주문 배정을 관제(fleet control)의 기능으로 두면서, 주변 설비·인프라·외부 IT 시스템과의 인터페이스는 명세 범위에서 뺀다. [사실][^ref-031] 로봇 인터페이스 표준이 상위 시스템 연동을 범위 밖에 두고 Open-RMF 작업 요청에도 마감 필드가 없으므로, 배정의 입력인 주문·납기·출하 마감 제약은 창고 관리 시스템(Warehouse Management System, WMS) 같은 상위 업무 시스템에서 받아 ROP가 배정 기준으로 옮겨야 할 것으로 보인다. [추정][^ref-031][^ref-125] 납기·출하 마감을 정하는 일 자체는 분류 원문 19장의 상위 업무 시스템 경계에 속하는 연계 대상이며, 결합 방법은 [열린 질문](../../open-questions.md) oq-054 로 남아 있다.
- **[26. 작업 순서·스케줄링](task-sequencing-and-scheduling.md) ↔ 23. 업무 시스템 연동**: Open-RMF 작업 요청 스키마는 시각·순서 관련 필드로 가장 이른 시작 시각과 우선순위를 두고, 마감 시각이나 다른 작업과의 선후를 지정하는 필드는 두지 않는다(2026-09-25 확인). [사실][^ref-125] 웨이브·웨이브리스 출고 지시 정책 연구(2010)와 동적으로 도착하는 주문의 피킹 재최적화 연구(2025)는 상위 시스템의 출고 지시·우선순위 변경이 작업 순서 결정 문제로 넘어가는 지점을 다루는 것으로 보인다. [추정][^ref-134][^ref-133]
- **26. 작업 순서·스케줄링 ↔ [24. 작업·워크플로 모델링](task-and-workflow-modeling.md)**: B2MML 공통 스키마의 Dependency1Type 은 두 요소 사이 실행 의존(선후·병행 금지·시작 후 간격 등)을 표현하며, 창고 물류 작업에 적용한 사례는 확인되지 않았다(oq-013). [사실][^ref-117]
- **26. 작업 순서·스케줄링 ↔ [35. 처리능력·규모·배치 설계](../design-and-simulation/capacity-sizing-and-layout-design.md)**: 랙 이동 로봇 작업대의 주문 배치·순서와 랙 도착 순서를 함께 정한 2017년 연구는, 최적화된 주문 처리가 흔한 단순 규칙보다 필요한 로봇 대수를 절반 넘게 줄였다고 보고했다. 이는 저자 계산 실험 조건의 보고값이며 독립 재현은 확인되지 않았다. [사실][^ref-381]
- **26. 작업 순서·스케줄링 ↔ [39. 운영 성과 측정·개선](../field-operations-and-monitoring/operational-performance-measurement-and-improvement.md)**: 풋월 주문 통합 연구(2019)는 빈 방출 순서가 맞지 않으면 포장 작업자가 유휴 대기한다고 보아, 포장 작업자 대기가 순서 결정의 성과 지표로 이어진다(지표 정의는 oq-051). [사실][^ref-385]
- **[28. 공용 자원·충전·에너지 최적화](shared-resource-charging-and-energy-optimization.md) ↔ 35. 처리능력·규모·배치 설계**: 충전 정책 연구(2024)와 창고 충전소 배치 최적화 연구(2024)가 있어, 충전 정책 결정이 충전기 수·위치 같은 설비 계획으로 이어지는 것으로 보인다. [추정][^ref-533][^ref-109]
- **28. 공용 자원·충전·에너지 최적화 ↔ 39. 운영 성과 측정·개선**: Omega 게재 연구(2024)는 로봇 이동형 풀필먼트 시스템에서 동적 우선순위 규칙이 선착순보다 에너지 소비를 3.41% 줄이고 처리량을 26.07% 높였다고 보고했다. 이 값은 모델·시뮬레이션 조건의 저자 보고값으로 현장 실측이 아니며 독립 재현은 확인되지 않았다. [사실][^ref-146]

### [옛 B. 공통 정보·환경 모델](../robot-ontology/index.md)

- **25. 작업 배정 — MRTA ↔ [5. 로봇 능력·작업 표현](../robot-ontology/robot-capability-and-task-representation.md)**: 능력 온톨로지로 이종 로봇·자원의 작업 수행 가능성을 추론해 배정 후보를 정하는 연구가 있다(2022, 2026-08). [사실][^ref-236][^ref-237]
- **28. 공용 자원·충전·에너지 최적화 ↔ 5. 로봇 능력·작업 표현**: VDA 5050 팩트시트는 임계 저충전 수준(criticalLowChargingLevel)과 최소·최대 희망 충전 수준·최소 충전 시간을 로봇 선언으로 두고, Open-RMF 플릿 어댑터 템플릿은 운영 설정 recharge_threshold(예시값 0.10)와 충전 목표 recharge_soc(예시값 1.0)를 둔다(2026-09-25 확인). [사실][^ref-228][^ref-105] 두 값 가운데 무엇을 충전 하한으로 삼을지는 oq-068 로 남아 있다.
- **[27. 다중 로봇 경로·교통 관리 — MAPF](multi-robot-path-and-traffic-management-mapf.md) ↔ [15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md)**: Open-RMF traffic-editor 는 차선의 양방향 여부와 대기 지점·충전소·주차 지점 같은 경유점 속성, 문·승강기를 주석하게 하고, 이 그래프를 building_map_generator 로 주행 그래프로 내보내 플릿 어댑터의 경로 계획에 쓰게 한다. [사실][^ref-079]
- **28. 공용 자원·충전·에너지 최적화 ↔ [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md)**: Open-RMF 는 로봇이 작업을 끝낼 충전량이 부족하면 충전 작업을 일정에 끼워 넣으므로, 충전 시점 계획은 로봇이 보고하는 현재 배터리 상태를 입력으로 쓰며, 이 현재 상태 표현은 18. 실시간 세계 상태·데이터 일관성 쪽에 속하는 것으로 보인다. [추정][^ref-104][^ref-051] 이 연결은 현재 상태를 표현하는 쪽이며, 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈 연결(아래 F. 도입·검증·유지관리)과 구분한다.

### [옛 C. 연결·실행 기반](../integration/index.md)

- **25. 작업 배정 — MRTA ↔ [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md)**: Open-RMF 디스패처는 작업 요청을 받으면 모든 플릿 어댑터에 입찰 공고(BidNotice)를 보내고, 처리 가능한 플릿이 비용을 담은 입찰(BidProposal)을 내면 가장 빨리 끝나는 것·가장 낮은 비용 같은 설정 기준으로 비교해 작업을 줄 플릿을 정한다. [사실][^ref-376] 작업 요청 스키마의 fleet_name 필드는 작업을 수행할 수 있는 플릿 이름(하나 또는 목록)을 지정해, 요청 단계에서 배정 후보 플릿을 제한할 수 있게 한다. [사실][^ref-125]
- **27. 다중 로봇 경로·교통 관리 — MAPF ↔ 20. 로봇·제조사 관제 연동**: Open-RMF 는 플릿 연동을 전체 제어·신호등(일시정지·재개)·읽기 전용으로 나누고 공유 공간마다 읽기 전용 플릿을 최대 하나만 허용하며, 충돌이 나면 플릿들이 선호 경로와 상대를 수용하는 경로를 내고 시스템 통합사가 배치한 제3자 판정자가 조합을 고른다. [사실][^ref-004] VDA 5050 은 경로 결정·우선순위·혼잡 처리·교착 해소 같은 교통 조율 전략과 알고리즘을 명세에서 빼면서도, 막힘 탐지·해소와 교통 제어(버퍼 경로·대기 위치)를 관제 기능으로 둔다. [사실][^ref-031]
- **28. 공용 자원·충전·에너지 최적화 ↔ 20. 로봇·제조사 관제 연동**: VDA 5050 은 충전 주문이 운반 주문을 중단시킬 수 있다는 것을 관제의 에너지 관리 기능으로 두고, 과충전 보호는 이동로봇의 책임으로 명시한다. [사실][^ref-031] 과충전 보호는 분류 원문 19장의 로봇 자체 지능·제어 경계에 속하는 연계 대상이며, ROP는 충전 시작·중지 요청과 상태 확인만 맡는다.
- **28. 공용 자원·충전·에너지 최적화 ↔ [22. 설비·건물 시스템 연동](../integration/facility-and-building-system-integration.md)**: Open-RMF 승강기 요청은 요청자 사이에서 유일한 세션 id 로 승강기를 점유하고 세션 종료 요청을 보낼 때까지 제어권이 그 세션에 남으며, AGV 모드에서는 승강기가 정지해 있는 동안 문이 열린 채 유지된다. [사실][^ref-312][^ref-286] 승강기 운행과 설비 안전 제어는 분류 원문 19장의 시설·설비 제어 경계에 속하는 연계 대상이며, ROP는 승강기 세션 요청과 운영 모드 확인만 맡는다.
- **26. 작업 순서·스케줄링 ↔ [29. 명령·작업 실행의 신뢰성](../execution-collaboration-and-recovery/command-and-task-execution-reliability.md)**: VDA 5050 에서 이미 로봇에 넘긴 기반(base) 경로는 바꿀 수 없으므로, 우선순위 변경에 따른 재정렬은 아직 해제하지 않은 호라이즌 구간과 새 주문에만 적용할 수 있을 것으로 보인다. [추정][^ref-031]
- **25. 작업 배정 — MRTA ↔ [42. 분산 시스템·통신·컴퓨팅 구조](../platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md)**: Lott·Honary(2026-09, 프리프린트, 원문 미열람)는 분산 작업 배정기 6종(CBAA, ACBBA, PI, HIPC, DMCHBA, DGA)을 패킷 손실·페이딩 등 통신 저하 조건에서 비교했다. [사실][^ref-493] 이 비교와 클라우드에 연결된 로봇·로봇그룹의 작업 계획을 다룬 국내 과제 보고서가 있어, 배정 계산을 클라우드·현장 서버·로봇 가운데 어디에 둘지가 두 영역을 잇는 설계 쟁점이 될 것으로 보이나, 물류센터 적용 근거는 없다. [추정][^ref-493][^ref-401]

### [옛 E. 협업·현장 운영](../execution-collaboration-and-recovery/index.md)

- **25. 작업 배정 — MRTA ↔ [31. 사람–로봇 협업](../execution-collaboration-and-recovery/human-robot-collaboration.md)**: 작업자가 피킹하고 자율이동로봇이 운반하는 동적 주문 피킹 연구(2025)가 있어, 로봇 배정이 사람 작업자의 배치와 맞물린다. [사실][^ref-132]
- **26. 작업 순서·스케줄링 ↔ 31. 사람–로봇 협업**: 복수 포장대와 피킹-패킹 전환 정책(작업자가 피킹과 포장 사이를 옮겨 감)의 작업자 스케줄링을 다룬 국내 연구(2025)가 있다(결과 수치는 미확인). [사실][^ref-388]
- **26. 작업 순서·스케줄링 ↔ [30. 로봇 간 협업·물리적 인계](../execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md)**: Open-RMF 배정이 플릿 단위 입찰로 이루어지고 작업 요청 스키마에 작업 간 선후 필드가 없으므로, 피킹 로봇 완료 뒤 운반 로봇 출발 같은 제조사 간 인계 선후는 ROP가 작업 흐름 수준에서 관리해야 할 것으로 보인다(oq-049). [추정][^ref-376][^ref-125]
- **27. 다중 로봇 경로·교통 관리 — MAPF ↔ [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md)**: 창고 MAPF 실행 연구(2019)는 지연이 쌓일 때 행동 의존 그래프로 순서를 지키며 실행을 이어가는 방법을 다루어, 계획 유지와 재계획의 판단이 두 영역을 잇는다. [사실][^ref-188]
- **25. 작업 배정 — MRTA ↔ 32. 예외 복구·재계획·업무 연속성**: VDA 5050 에서 브로커 연결이 끊긴 로봇은 받은 주문 정보를 유지한 채 마지막으로 해제된 노드까지 주문을 수행하므로, 통신 단절 때 ROP가 다시 배정할 수 있는 몫은 아직 해제하지 않은 구간과 새 작업으로 한정될 것으로 보인다. [추정][^ref-031]
- **25. 작업 배정 — MRTA ↔ [38. 모니터링·이상 탐지·원인 분석](../field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md)**: 위치 스푸핑을 다룬 2026-08 프리프린트의 신뢰 인지 모니터는 위치 신뢰도와 작업 실행 행동 증거를 결합해 에이전트를 분류하므로, 실행 기록으로 이상 로봇을 가려 배정 입력에서 빼는 일이 모니터링과 배정을 잇는 지점이 될 것으로 보인다. 이 연구는 GPS 스푸핑 데이터와 택시 수요로 실험했으며 물류센터 적용은 확인되지 않았다. [추정][^ref-494]

### [옛 F. 도입·검증·유지관리](../verification-deployment-and-lifecycle/index.md)

- **25. 작업 배정 — MRTA ↔ [34. 시뮬레이션·예측용 디지털 트윈](../design-and-simulation/simulation-and-predictive-digital-twin.md)**: 로봇 이동형 풀필먼트 시스템(2019)과 국내 자동물류센터의 이산 사건 시뮬레이션 연구가 배정 규칙을 가정한 미래에서 실험하는 도구로 쓰였고, 한 연구에서는 피킹 주문 배정 규칙이 단위 처리량을 크게 바꾸었다. [사실][^ref-398][^ref-402]
- **27. 다중 로봇 경로·교통 관리 — MAPF ↔ 34. 시뮬레이션·예측용 디지털 트윈**: 다중 AGV 시스템의 경로망을 시뮬레이션으로 자동 설계하는 연구(2024)가 있어, 경로망 설계 평가는 가정한 미래를 실험하는 쪽에 속하는 것으로 보인다. [추정][^ref-267]
- **27. 다중 로봇 경로·교통 관리 — MAPF ↔ [55. 현장 조사·설치·시운전](../verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md)**: 현장 도입 때 플릿별 경로망과 차선 방향, 대기·충전·주차 경유점을 traffic-editor 로 주석해 설정하는 일이 온보딩 작업이 될 것으로 보인다. [추정][^ref-079]
- **27. 다중 로봇 경로·교통 관리 — MAPF ↔ [54. 시험·형식 검증·벤치마크](../verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md)**: MAPF 연구는 정의·변형·벤치마크를 정리한 공통 틀(2019)을 가지고 있으나, 격자·단위 시간 가정의 벤치마크 성과가 실제 물류센터 처리량으로 얼마나 이어지는지는 확인되지 않았다(oq-058). [사실][^ref-186]
- **25. 작업 배정 — MRTA ↔ 54. 시험·형식 검증·벤치마크**: 분산 배정기를 같은 사례 묶음과 통신 조건에서 이동 거리·안정성·계산 부담으로 비교하는 벤치마크(2026-09, 프리프린트)가 있어, 배정 방식 선택을 시험 조건과 함께 평가하는 틀이 된다. [사실][^ref-493]
- **28. 공용 자원·충전·에너지 최적화 ↔ [57. 자산·소프트웨어 수명주기 관리](../verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md)**: 플릿 수준에서 배터리 건강(열화)을 고려해 자율이동로봇의 일정을 정하는 연구(2026-03)가 있어, 충전·배정 계획이 배터리 열화 관리와 이어진다. [사실][^ref-403]

### [옛 G. 안전·보안·지능·거버넌스](../governance-law-and-society/index.md)

- **28. 공용 자원·충전·에너지 최적화 ↔ [48. 안전·위험 관리](../safety/safety-and-risk-management.md)**: Open-RMF 승강기 상태의 운영 모드에는 사람·AGV·화재·오프라인·비상이 있고(설정은 사람·AGV 모드만 가능), Open-RMF 데모는 비상 경보가 켜지면 모든 로봇을 가장 가까운 주차 위치로 보낸다. [사실][^ref-286][^ref-104] 설비 안전 제어는 분류 원문 19장의 시설·설비 제어 경계에 속하는 연계 대상이며, ROP는 운영 모드를 확인해 계획에 반영하는 쪽을 맡는다.
- **27. 다중 로봇 경로·교통 관리 — MAPF ↔ 48. 안전·위험 관리**: VDA 5050 은 진입 금지·속도 제한·해제·우선·벌점 등 구역 유형을 교통 관리 수단으로 정의하면서, 이 문서가 기능·운영·시스템 안전 요구를 정하지 않으며 안전 표준으로 적용해서는 안 된다고 밝힌다. [사실][^ref-031] 따라서 이 연결은 교통 관리 수단과 안전 기능을 구분하는 지점으로만 다룬다.
- **25. 작업 배정 — MRTA ↔ [51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md)**: 2026-08 프리프린트는 위치 스푸핑으로 오염된 에이전트가 계획 정보와 실행을 어긋나게 하면 롤아웃 기반 다중 로봇 배정·경로 계획의 비용 개선이 사라질 수 있다고 보고, 스푸핑 공격 모델과 탐지된 적대 에이전트를 이후 계획에서 빼는 방법을 제안한다. 실험은 GPS 스푸핑 데이터와 택시 수요로 했으며 물류센터 적용은 확인되지 않았다. [사실][^ref-494] Open-RMF 문서는 같은 신원과 접근통제 규칙을 공유하는 프로세스 묶음인 SROS 2 인클레이브로 구성요소의 권한을 나누고, 웹 대시보드는 TLS 로 제공하며 OIDC 로 사용자 역할을 담은 서명 토큰을 API 서버에 보내 역할에 따라 접근을 허용한다고 설명한다. [사실][^ref-405] 작업 요청이 대시보드·API 서버를 거쳐 디스패처로 들어가고 배정이 플릿의 입찰 비용과 위치 보고에 기대므로, 누가 작업을 요청·우선 지정할 수 있는지와 입찰·위치 보고를 얼마나 믿을지가 배정의 보안 경계가 될 것으로 보인다. 창고 배정의 보안 사례는 찾지 못했다. [추정][^ref-405][^ref-376][^ref-494]
- **25. 작업 배정 — MRTA ↔ [47. AI·학습·적응과 모델 운영](../ai-and-learning/ai-learning-adaptation-and-model-operations.md)**: 분류 개정 전 원문 8장의 교차 규칙은 학습 기반 배차를 25. 작업 배정 — MRTA에 적용되는 47. AI·학습·적응과 모델 운영의 연구 방법으로 둔다. 학습 기반 배차(이종 그래프 어텐션 스케줄러)와 대규모 언어 모델(Large Language Model, LLM) 기반 다중 로봇 작업 배정 연구가 있어 이 교차 규칙에 따라 두 영역이 이어진다. [사실][^ref-399][^ref-090][^ref-168] LLM 배정의 결과 수치는 출처가 충돌해(oq-030) 여기서 쓰지 않는다.
- **27. 다중 로봇 경로·교통 관리 — MAPF ↔ 47. AI·학습·적응과 모델 운영**: 모방 학습을 적용한 지속형 MAPF 연구(2024-10)가 있어, 학습 기반 경로 계획이 두 영역을 잇는다. [사실][^ref-199]
- **28. 공용 자원·충전·에너지 최적화 ↔ 47. AI·학습·적응과 모델 운영**: 자율 피킹 로봇의 충전소 선택·충전 시간 결정에 심층 강화학습을 쓰는 연구(2026-07)가 있어, 학습 기반 충전 결정이 두 영역을 잇는 것으로 보인다. [추정][^ref-531]
- **27. 다중 로봇 경로·교통 관리 — MAPF ↔ [21. 상호운용 표준·적합성](../integration/interoperability-standards-and-conformance.md)**: VDA 5050 은 구역·경로 해제로 교통 규칙을 정하되 조율 전략은 빼고, Open-RMF 는 여러 플릿의 교통 협상에서 시스템 통합사가 배치한 판정자가 조합을 고르게 하므로, 한 현장에서 우선권 판정 규칙을 누가 정하고 승인하는지가 거버넌스 과제로 넘어갈 것으로 보인다(oq-057). [추정][^ref-031][^ref-004]

### 아직 다루지 않은 연결

- [17. 작업 대상·자산 식별과 인계 추적](../objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md)과 D. 계획·최적화를 잇는 근거는 이번 조사에서 확보하지 못했다.
- 42. 분산 시스템·통신·컴퓨팅 구조, 38. 모니터링·이상 탐지·원인 분석, 51. 인증·권한·격리와의 연결은 물류센터 조건이 아닌 2026년 프리프린트 두 편에 기대므로, 물류 현장 근거가 나오면 다시 확인한다.

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 108건이다(논문 66건 · 기사·보고서 0건 · 업체 발표 2건 · 표준·오픈소스·기관 자료 40건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-493](../../references/ref-493.md) — Lott, J., & Honary, V.(University of San Diego), Decentralized Multi-Robot Task Allocation Under Degraded Communication: A Benchmark of Performance, Reliability, and Computation (발행 2026-09)
- [ref-192](../../references/ref-192.md) — Bonetti, A., Proia, S., Guidetti, S., & Sabattini, L., A traffic management system for large and heterogeneous vehicles in narrow industrial environments (발행 2026-09)
- [ref-236](../../references/ref-236.md) — Electronics(MDPI) 게재 논문(저자 미확인), Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation (발행 2026-08-11)
- [ref-494](../../references/ref-494.md) — Francos, R. M., Garces, D., Akgün, O. E., Bastian, N. D., & Gil, S.(Harvard·JHU), Trust-Aware Sequential Decision Making and Rollout Planning for Resilient Multi-Robot Systems (발행 2026-08)
- [ref-531](../../references/ref-531.md) — arXiv 2607.05683 저자(미확인), Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers (발행 2026-07)
- [ref-403](../../references/ref-403.md) — Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin), Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots (발행 2026-03)
- [ref-116](../../references/ref-116.md) — Filippone, G., Pettinari, S., & Pelliccione, P., Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis (발행 2026-03)
- [ref-060](../../references/ref-060.md) — Lee, Y. 외(Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments (발행 2026)
- [ref-168](../../references/ref-168.md) — Kaitha, S., & Yu, S. 외(arXiv 2512.02810), Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms (발행 2025-12)
- [ref-268](../../references/ref-268.md) — Rüdt, M., Enke, C., & Furmans, K. (KIT), Automated Generation of Continuous-Space Roadmaps for Routing Mobile Robot Fleets (v2 제목: Continuous-Space Roadmap Generation for Mobile Robot Fleets with Distance Constraints and Geometry-Aware Discretization) (발행 2025-11)
- 그 밖에 56건

**기사·보고서**

- 아직 없음

**업체 발표**

- [ref-219](../../references/ref-219.md) — Mobile Industrial Robots(MiR) (ManualsLib 게재본), MiR Charge 24V Operating Manual — Setting charging station markers on the map (제조사 공식 사이트가 아닌 매뉴얼 게재 사이트 사본) (발행 미확인)
- [ref-113](../../references/ref-113.md) — Camunda, Messages \| Camunda 8 Docs (camunda-docs: docs/components/concepts/messages.md) (발행 미확인)

**표준·오픈소스·기관 자료**

- [ref-117](../../references/ref-117.md) — MESA International, B2MML-BatchML — Schema/B2MML-Common.xsd (발행 2023)
- [ref-044](../../references/ref-044.md) — GS1, gs1/EPCIS — Ontology/CBV.ttl (Core Business Vocabulary ontology 2.0) (발행 2021-09-30)
- [ref-119](../../references/ref-119.md) — IEC / ISO, IEC 62264-3:2016 - Enterprise-control system integration — Part 3: Activity models of manufacturing operations management (발행 2016)
- [ref-538](../../references/ref-538.md) — Open Robotics (open-rmf), rmf_reservation — Experimental reservation library in rust (GitHub) (발행 미확인)
- [ref-537](../../references/ref-537.md) — Open Robotics (open-rmf), rmf_ros2 — rmf_fleet_adapter/include/rmf_fleet_adapter/agv/RobotUpdateHandle.hpp (발행 미확인)
- [ref-536](../../references/ref-536.md) — Open Robotics (open-rmf), rmf_traffic — rmf_traffic/include/rmf_traffic/agv/Graph.hpp (발행 미확인)
- [ref-405](../../references/ref-405.md) — Open Robotics, Security - Programming Multiple Robots with ROS 2 (발행 미확인)
- [ref-404](../../references/ref-404.md) — Open Robotics (open-rmf), rmf_task — README (발행 미확인)
- [ref-401](../../references/ref-401.md) — KISTI ScienceON 수록 국가R&D 과제 보고서(수행기관 미확인), 클라우드에 연결된 개별 로봇 및 로봇그룹의 작업 계획 기술 개발 (발행 미확인)
- [ref-390](../../references/ref-390.md) — Open Robotics (open-rmf), rmf_task — rmf_task/include/rmf_task/BinaryPriorityScheme.hpp (발행 미확인)
- 그 밖에 30건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-25 · 갱신 · [G. 계획·최적화](index.md) — '다른 대분류와의 연결' 절 신규 작성(A·B·C·E·F·G 여섯 대분류, 아직 다루지 않은 연결에 7. 화물·재고·자산 식별과 추적 명시), '참고 자료' 끝에 새 각주 정의 38건 추가 (실행 2026-09-25-55)
- 2026-09-25 · 요약 · [G. 계획·최적화](index.md) — D. 계획·최적화: '다른 대분류와의 연결' 절 신규 작성(A·B·C·E·F·G 여섯 대분류, 1차 수정 지시 14건 이행) (실행 2026-09-25-55)
- 2026-09-25 · 갱신 · [28. 공용 자원·충전·에너지 최적화](shared-resource-charging-and-energy-optimization.md) — 섹션 3~11 신규 작성(트랙 반영 제안 4건 반영, 1차 수정 지시 13건 이행), 2차 수정: 4·8절 연결 문장 태그 제거, 5절 조사 한계 문장 태그·각주 제거와 oq-010 연결, 6절 첫 문장을 출처 범위로 좁힘 (실행 2026-09-25-40)
- 2026-09-25 · 생성 · [28. 공용 자원·충전·에너지 최적화 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area16-s6.md) — 자동 분리: 16. 공용 자원·충전·에너지 최적화 의 "6. 대표 접근법과 기술" 절을 옮겼다. 2차 수정: 세 줄 요약·본문 첫 문장을 출처 범위(충전 작업 삽입·뮤텍스 그룹·승강기 세션)로 좁혔다 (실행 2026-09-25-40)
- 2026-09-25 · 생성 · [28. 공용 자원·충전·에너지 최적화 — 대표 연구와 자료](../../topics/2026/2026-09-25-area16-s8.md) — 자동 분리: 16. 공용 자원·충전·에너지 최적화 의 "8. 대표 연구와 자료" 절을 옮겼다. 2차 수정: 첫 문장 태그 제거, 병원·호텔 연구 문구를 연관 관계로 고침, ref-535 제목 원문 복원 (실행 2026-09-25-40)
<!-- auto:category-recent:end -->

## 참고 자료

원문의 [5]는 참고문헌 [ref-005](../../references/ref-005.md)에 해당한다.[^ref-005] 원문의 [6]은 참고문헌 [ref-006](../../references/ref-006.md)에 해당한다.[^ref-006]

[^ref-005]: Li, J., Tinka, A., Kiesel, S., Durham, J. W., Kumar, T. K. S., & Koenig, S., Lifelong Multi-Agent Path Finding in Large-Scale Warehouses, 2020, https://arxiv.org/abs/2005.07371, 접근일 2026-09-24
[^ref-006]: Ma, H., Li, J., Kumar, T. K. S., & Koenig, S., Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks, 2017, https://arxiv.org/abs/1705.10868, 접근일 2026-09-24
[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-09-25
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-09-25
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-09-25 (원문 미열람)
[^ref-079]: Open Robotics, Traffic Editor - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-25
[^ref-090]: Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C., SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models, 2023-09, https://arxiv.org/abs/2309.10062, 접근일 2026-09-25 (원문 미열람)
[^ref-104]: Open Robotics (open-rmf), rmf_demos — Demonstrations of Open-RMF (README), 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-25
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-09-25
[^ref-109]: Stark, H.-G. 외, A Page-Rank-like Approach to Optimal Placement of Charging Stations in a Warehouse, 2024-06, https://arxiv.org/abs/2406.17003, 접근일 2026-09-25 (원문 미열람)
[^ref-117]: MESA International, B2MML-BatchML — Schema/B2MML-Common.xsd, 2023, https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-Common.xsd, 접근일 2026-09-25 (원문 미열람)
[^ref-125]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/task_request.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json, 접근일 2026-09-25
[^ref-132]: Yu, S., & Srinivas, S., Collaborative Human–Robot Teaming for Dynamic Order Picking: Interventionist strategies for improving warehouse intralogistics operations, 2025, https://www.sciencedirect.com/science/article/abs/pii/S1366554525001231, 접근일 2026-09-25 (원문 미열람)
[^ref-133]: Lorenz, Otto, & Gendreau (Networks, Wiley), Picking Operations in Warehouses With Dynamically Arriving Orders: How Good is Reoptimization?, 2025, https://onlinelibrary.wiley.com/doi/full/10.1002/net.22281, 접근일 2026-09-25 (원문 미열람)
[^ref-134]: Gallien, J., & Weber, T. G., To Wave or Not to Wave? Order Release Policies for Warehouses with an Automated Sorter, 2010, https://pubsonline.informs.org/doi/abs/10.1287/msom.1100.0291, 접근일 2026-09-25 (원문 미열람)
[^ref-146]: Omega 게재 논문(저자 미확인), The role of energy consumption in robotic mobile fulfillment systems: Performance evaluation and operating policies with dynamic priority, 2024, https://www.sciencedirect.com/science/article/abs/pii/S0305048324001336, 접근일 2026-09-25 (원문 미열람)
[^ref-168]: Kaitha, S., & Yu, S. 외(arXiv 2512.02810), Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms, 2025-12, https://arxiv.org/abs/2512.02810, 접근일 2026-09-25 (원문 미열람)
[^ref-186]: Stern, R., Sturtevant, N. R., Felner, A., Koenig, S. 외, Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks, 2019-06, https://arxiv.org/abs/1906.08291, 접근일 2026-09-25 (원문 미열람)
[^ref-188]: Hönig, W., Kiesel, S. 외, Persistent and Robust Execution of MAPF Schedules in Warehouses, 2019, https://ieeexplore.ieee.org/abstract/document/8620328/, 접근일 2026-09-25 (원문 미열람)
[^ref-199]: arXiv 2410.21415 저자(미확인), Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding, 2024-10, https://arxiv.org/abs/2410.21415, 접근일 2026-09-25 (원문 미열람)
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-236]: Electronics(MDPI) 게재 논문(저자 미확인), Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation, 2026-08-11, https://doi.org/10.3390/electronics15163562, 접근일 2026-09-25 (원문 미열람)
[^ref-237]: Kluge-Wilkes, A. 외(RWTH Aachen WZL), Ontology-based task allocation for heterogeneous resources in Line-less Mobile Assembly Systems, 2022, https://www.techrxiv.org/users/685235/articles/679210-ontology-based-task-allocation-for-heterogeneous-resources-in-line-less-mobile-assembly-systems, 접근일 2026-09-25 (원문 미열람)
[^ref-267]: IEEE 게재 논문 저자(미확인), Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)), 2024, https://ieeexplore.ieee.org/document/10287275/, 접근일 2026-09-25 (원문 미열람)
[^ref-286]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg, 접근일 2026-09-25
[^ref-312]: Open Robotics (open-rmf), rmf_internal_msgs — rmf_lift_msgs/msg/LiftRequest.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftRequest.msg, 접근일 2026-09-25
[^ref-376]: Open Robotics, Tasks in RMF (task) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/task.html, 접근일 2026-09-25
[^ref-381]: Boysen, N., Briskorn, D., & Emde, S., Parts-to-picker based order processing in a rack-moving mobile robots environment, 2017, https://www.sciencedirect.com/science/article/abs/pii/S0377221717302758, 접근일 2026-09-25 (원문 미열람)
[^ref-385]: Boysen, N., Stephan, K., & Weidinger, F., Manual order consolidation with put walls: the batched order bin sequencing problem, 2019, https://www.sciencedirect.com/science/article/pii/S2192437620300315, 접근일 2026-09-25 (원문 미열람)
[^ref-388]: Tran Bo Tao Huong, 이광헌, 홍순도(대한산업공학회지), 복수 포장대와 피킹-패킹 전환 정책을 운영하는 물류센터에서의 작업자 스케줄링, 2025, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003194570, 접근일 2026-09-25 (원문 미열람)
[^ref-398]: Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L., Decision rules for robotic mobile fulfillment systems, 2019, https://www.sciencedirect.com/science/article/pii/S2214716019300946, 접근일 2026-09-25 (원문 미열람)
[^ref-399]: Wang, Z., & Gombolay, M., Heterogeneous graph attention networks for scalable multi-robot scheduling with temporospatial constraints, 미확인, https://link.springer.com/article/10.1007/s10514-021-09997-2, 접근일 2026-09-25 (원문 미열람)
[^ref-401]: KISTI ScienceON 수록 국가R&D 과제 보고서(수행기관 미확인), 클라우드에 연결된 개별 로봇 및 로봇그룹의 작업 계획 기술 개발, 미확인, https://scienceon.kisti.re.kr/srch/selectPORSrchReport.do?cn=TRKO202400003952, 접근일 2026-09-25 (원문 미열람)
[^ref-402]: KISTI ScienceON 수록 논문(저자 미확인), 시뮬레이션과 메타모델을 이용한 자동물류센터 설계 최적화, 미확인, https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO200634515151716, 접근일 2026-09-25 (원문 미열람)
[^ref-403]: Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin), Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots, 2026-03, https://arxiv.org/abs/2603.22731, 접근일 2026-09-25 (원문 미열람)
[^ref-405]: Open Robotics, Security - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/security.html, 접근일 2026-09-25
[^ref-531]: arXiv 2607.05683 저자(미확인), Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers, 2026-07, https://arxiv.org/abs/2607.05683, 접근일 2026-09-25 (원문 미열람)
[^ref-533]: Chen, W., Gong, Y., Chen, Q., & Wang, H., Does battery management matter? Performance evaluation and operating policies in a self-climbing robotic warehouse, 2024-01, https://www.sciencedirect.com/science/article/abs/pii/S0377221723004770, 접근일 2026-09-25 (원문 미열람)
[^ref-493]: Lott, J., & Honary, V.(University of San Diego), Decentralized Multi-Robot Task Allocation Under Degraded Communication: A Benchmark of Performance, Reliability, and Computation, 2026-09, https://arxiv.org/abs/2609.13711, 접근일 2026-09-25 (원문 미열람)
[^ref-494]: Francos, R. M., Garces, D., Akgün, O. E., Bastian, N. D., & Gil, S.(Harvard·JHU), Trust-Aware Sequential Decision Making and Rollout Planning for Resilient Multi-Robot Systems, 2026-08, https://arxiv.org/abs/2608.25690, 접근일 2026-09-25 (원문 미열람)
````

### docs/categories/planning-and-optimization/task-and-workflow-modeling.md (요약)

```markdown
# 24. 작업·워크플로 모델링

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

현장 업무를 단계·선후관계·완료 조건으로 정의하고, 계획과 실행이 따를 운영 정책을 정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **작업·워크플로 모델링**: 현장 업무(운반·배송·순찰·점검·조작·서비스 등)를 단계·선후관계·완료 조건으로 분해해 정의한다
- **동작 완료와 업무 완료 연결**: 로봇의 동작 완료(도착·내려놓음)와 업무 완료(인수 확인·기록 반영)를 구분해 잇는다
- **운영 정책 설정**: 우선순위·운영 시간·구역 규칙·충전 기준 같은 운영 정책을 설정하고 버전으로 관리해 계획과 실행이 따르게 한다

이전 분류(2026-09-24)에서 이 페이지는 옛 2번 영역 ‘공정·워크플로 모델링’(옛 대분류 A. 업무·공급망 설계)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 입고·검수·적치·보충·피킹·이송·생산·포장·출하·반품을 작업 단계로 분해하고, 선후관계와 완료 조건을 정의 [옛 분류원문]

> 옛 질문: ‘운반 완료’와 ‘인수 확인·재고 반영 완료’를 어떻게 연결할까? [옛 분류원문]

## 2. 핵심 질문

현장 업무를 로봇이 실행할 수 있는 단계와 완료 조건으로 어떻게 나눌 것인가? [분류원문]
```

### docs/categories/planning-and-optimization/task-allocation-mrta.md (요약)

```markdown
# 25. 작업 배정 — MRTA

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

작업을 로봇 또는 로봇 팀에 배정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **작업 배정**: 능력·위치·적재량·배터리·기한을 고려해 로봇 또는 로봇 팀에 작업을 배정한다
- **이종 로봇 팀 구성**: 한 작업에 필요한 로봇 조합(운반·팔·순찰 등)을 정한다

이전 분류(2026-09-24)에서 이 페이지는 옛 13번 영역 ‘작업 배정 — MRTA’(옛 대분류 D. 계획·최적화)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 능력·위치·적재량·배터리·납기 등을 고려해 로봇 또는 로봇 팀에 작업을 배정 [옛 분류원문]

> 옛 질문: 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]
```

### docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md (요약)

```markdown
# 26. 작업 순서·스케줄링

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

순서·시간 제약·긴급 삽입을 다루고, 계속 들어오는 작업에 맞춰 다시 계획한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **작업 순서·스케줄링**: 작업 묶음, 선후관계, 시간 제약, 작업 간 동기화, 긴급 작업 삽입을 다룬다
- **계속 들어오는 작업의 재계획**: 새 작업과 지연이 계속 생기는 조건에서 계획을 이어서 고친다

이전 분류(2026-09-24)에서 이 페이지는 옛 14번 영역 ‘작업 순서·스케줄링’(옛 대분류 D. 계획·최적화)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 주문 묶음, 작업 선후관계, 시간 제약, 공정 간 동기화, 긴급 작업 삽입 [옛 분류원문]

> 옛 질문: 피킹·운반·포장이 서로 기다리지 않게 어떤 순서로 실행할까? [옛 분류원문]

## 2. 핵심 질문

일이 계속 새로 들어올 때 무엇을 먼저, 언제 할지 어떻게 정할 것인가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]
```

### docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md (요약)

```markdown
# 27. 다중 로봇 경로·교통 관리 — MAPF

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

여러 로봇의 경로·통과 시점·우선권을 조율한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **다중 로봇 경로·교통 관리**: 여러 로봇의 경로와 통과 시점을 조율하고 혼잡·교착·우선권을 처리한다
- **이기종 로봇 간 통행 우선권**: 서로 다른 제조사의 로봇이 좁은 통로에서 만날 때 누가 양보할지 정한다

이전 분류(2026-09-24)에서 이 페이지는 옛 15번 영역 ‘다중 로봇 경로·교통 관리 — MAPF’(옛 대분류 D. 계획·최적화)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 여러 로봇의 경로와 통과 시점을 조율하고, 혼잡·교착·우선권을 처리 [옛 분류원문]

> 옛 질문: 서로 다른 제조사의 로봇이 좁은 통로에서 마주치면 누가 양보할까? [옛 분류원문]

## 2. 핵심 질문

서로 다른 제조사의 로봇이 좁은 통로에서 마주치면 누가 양보할까? [분류원문]
```

### docs/categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md (요약)

```markdown
# 28. 공용 자원·충전·에너지 최적화

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

공용 자원을 예약·배분하고 충전·에너지를 계획한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **공용 자원 예약·배분**: 승강기·작업대·대기 공간·버퍼 같은 공용 자원을 예약하고 나눈다
- **충전·에너지 계획**: 충전 시점·충전기 배정·대기열과 작업별 에너지 예산을 계획한다

이전 분류(2026-09-24)에서 이 페이지는 옛 16번 영역 ‘공용 자원·충전·에너지 최적화’(옛 대분류 D. 계획·최적화)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 충전기·승강기·작업대·대기 공간·버퍼의 예약과 배분, 충전 시점과 에너지 사용 계획 [옛 분류원문]

> 옛 질문: 로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까? [옛 분류원문]

## 2. 핵심 질문

로봇들이 동시에 충전하거나 승강기를 기다리는 상황을 어떻게 줄일까? [분류원문]
```

### docs/ideas/index.md

````markdown
---
title: "확장 아이디어 연결 구조"
type: idea
subtype: index
related_areas: [5, 15, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 32, 34, 35, 38, 47, 48, 51, 54, 55, 57]
tags: [확장 아이디어, 공통 데이터 모델, 연구영역 매핑]
status: published
created: 2026-09-25
updated: 2026-09-25
version: 1
---

[홈](../index.md) › 확장 아이디어 연결 구조

# 확장 아이디어 연결 구조

이 페이지는 사용자가 제안한 세 확장 아이디어가 서로 어떻게 이어지는지, 무엇을 공통 데이터로 주고받는지, 67개 세부 연구영역과 어떻게 대응하는지를 한곳에 모은다. 아이디어는 분류를 바꾸지 않는다. 17개 대분류·67개 세부 연구영역의 이름·순서·번호·정의는 그대로이고, 아이디어는 세부영역에 연결을 더할 뿐이다. 각 아이디어의 연구는 중점 연구 트랙이 단계적으로 진행하며, 이 페이지의 구조와 데이터 모델은 구축자 제안이다. [가정]

## 세 아이디어

| 아이디어 | 정의(사용자 문구 그대로) | 연구하는 트랙 |
|---|---|---|
| [아이디어 1. 로봇 기능 온톨로지](robot-capability-ontology.md) | 로봇 매뉴얼·SDK 문서에서 로봇별 능력(이동·계단·적재·도어 조작·충전)과 제약을 추출해 온톨로지로 정리. 작업 할당 시 수행 가능한 로봇을 질의로 찾고, 신규 로봇 온보딩 시 능력 정의 초안을 자동 생성 | [매뉴얼 기반 로봇 기능 온톨로지](../tracks/manual-capability-ontology/index.md)(기존 트랙 확장) |
| [아이디어 2. 채팅 기반 구성·운영](chat-based-configuration-and-operation.md) | 사용자가 채팅으로 상황과 처리할 일을 입력하면 AI가 업무를 파악·분해하고, 온톨로지로 적합한 로봇을 찾아 배정·배치한 뒤 작업 진행과 스케줄링을 자동으로 관리 | [채팅 기반 구성·운영](../tracks/chat-based-configuration-and-operation/index.md)(새 트랙) |
| [아이디어 3. 건축 도면 자동 인식](floorplan-recognition.md) | 평면도에서 벽·문·엘리베이터·계단·충전 위치를 인식해 층별 지도와 공용 자원 목록을 자동 생성하고, 공간 그래프로 온톨로지에 적재. 현장 모델링 시간을 줄이고 시뮬레이션 초기값으로 사용 | [건축 도면 자동 인식](../tracks/floorplan-recognition/index.md)(새 트랙) |

## 이어지는 구조

세 아이디어는 하나의 흐름으로 이어진다. 도면 인식(아이디어 3)이 평면도에서 공간과 시설(공간 노드, 공용 자원)을 뽑아 공간 그래프로 온톨로지에 적재하고, 로봇 기능 온톨로지(아이디어 1)가 로봇의 능력과 제약을 같은 온톨로지에 담는다. 챗봇(아이디어 2)은 사용자의 지시를 작업으로 분해한 뒤 그 온톨로지를 질의해 작업을 할 수 있는 로봇과 경로·자원을 고른다. [가정]

이 흐름은 분류 개정 전 원문 10장의 "로봇과 건물 조건을 함께 판단" 아이디어가 가리키는 지점과 겹친다. 원문은 그 중심 연구영역을 [5. 로봇 능력·작업 표현](../categories/robot-ontology/robot-capability-and-task-representation.md), [15. 지도·공간·위치 모델](../categories/space-and-map-model/map-space-and-location-model.md), [18. 실시간 세계 상태·데이터 일관성](../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md)으로, 함께 필요한 영역을 [25. 작업 배정 — MRTA](../categories/planning-and-optimization/task-allocation-mrta.md), [28. 공용 자원·충전·에너지 최적화](../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md), [48. 안전·위험 관리](../categories/safety/safety-and-risk-management.md)로 둔다(원문 표는 [논의한 아이디어의 연구영역 매핑](../about/idea-mapping.md)에 있다).

```mermaid
flowchart LR
  plan["평면도"] --> idea3["아이디어 3. 건축 도면 자동 인식"]
  idea3 -->|"공간 노드·공용 자원"| sgraph["공간 그래프"]
  manual["로봇 매뉴얼·SDK 문서"] --> idea1["아이디어 1. 로봇 기능 온톨로지"]
  idea1 -->|"로봇 능력·제약"| onto["공통 온톨로지"]
  sgraph -->|"적재"| onto
  chat["사용자 채팅 지시"] --> idea2["아이디어 2. 채팅 기반 구성·운영"]
  idea2 -->|"작업 요구 질의"| onto
  onto -->|"수행 가능한 로봇·경로·공용 자원"| idea2
  idea2 -->|"배정·배치·일정"| rop["ROP 실행: 배정·경로·자원 예약"]
  idea3 -.->|"층별 지도(초기값)"| sim["시뮬레이션·예측용 디지털 트윈"]
  idea1 -.->|"능력 정의 초안"| onboard["신규 로봇 온보딩"]
```

## 공통 데이터 모델

세 아이디어가 함께 쓰는 네 요소다. 정의와 속성은 아이디어 정의 문구에서 구축자가 도출한 출발점이며, 각 트랙의 초안([능력 온톨로지 초안](../tracks/manual-capability-ontology/ontology-draft.md), [업무 분해·배정 설계 초안](../tracks/chat-based-configuration-and-operation/task-model-draft.md), [공간 그래프 스키마 초안](../tracks/floorplan-recognition/space-graph-schema-draft.md))이 근거와 함께 고친다. [가정]

| 요소 | 정의 | 주요 속성 | 생산하는 아이디어 | 소비하는 아이디어 |
|---|---|---|---|---|
| 공간 노드 | 로봇이 머물거나 지나가는 공간 단위(층·구역·통로)와 그 사이를 잇는 문·엘리베이터·계단 | 층, 종류, 연결된 노드, 통과 조건, 이름·별칭, 근거 도면 | 아이디어 3 | 아이디어 1(계단·도어 조작 능력과 통과 조건 대조), 아이디어 2(지시 속 장소 해석, 배치 경로) |
| 공용 자원 | 여러 로봇이 나눠 쓰는 시설(엘리베이터, 충전 위치 등) | 종류, 위치(공간 노드), 수용량, 예약·사용 조건, 설비 연동 여부 | 아이디어 3(공용 자원 목록) | 아이디어 1(충전·도어 조작 능력과 대응), 아이디어 2(배치·일정의 자원 예약) |
| 로봇 능력 | 로봇이 수행할 수 있는 기능과 그 제약(범위 능력: 이동·계단·적재·도어 조작·충전) | 기능, 제약, 장착 장비, 실행 조건, 근거 문서 | 아이디어 1 | 아이디어 2(작업 할당 질의), 아이디어 3(로봇별 통과 가능 경로 판단) |
| 작업 | 지시에서 분해된 실행 단위와 그 요구 | 작업 종류, 장소(공간 노드), 대상, 기한·우선순위, 작업 요구(필요 능력·제약), 배정 로봇, 진행 상태 | 아이디어 2 | 아이디어 1(작업 요구와 기능의 대응 질의) |

## 아이디어 사이의 입출력

| 보내는 아이디어 | 받는 아이디어 | 전달하는 것 | 받는 쪽의 쓰임 |
|---|---|---|---|
| 아이디어 3. 건축 도면 자동 인식 | 아이디어 1. 로봇 기능 온톨로지 | 공간 그래프(공간 노드·공용 자원) | 온톨로지에 적재해 로봇 능력(계단·도어 조작·충전)과 공간 조건을 같은 기준으로 대조 |
| 아이디어 3. 건축 도면 자동 인식 | 아이디어 2. 채팅 기반 구성·운영 | 층·구역 이름과 별칭, 경로, 공용 자원 목록 | 지시 속 장소 해석, 배치 경로와 자원 예약 |
| 아이디어 1. 로봇 기능 온톨로지 | 아이디어 2. 채팅 기반 구성·운영 | 작업 할당 질의 결과(수행 가능한 로봇 후보와 근거) | 배정 후보 선택과 배정 근거 설명 |
| 아이디어 2. 채팅 기반 구성·운영 | 아이디어 1. 로봇 기능 온톨로지 | 작업 요구(필요 능력·제약), 질의가 실패한 사례 | 질의 입력, 온톨로지 보강 질문 |
| 아이디어 2. 채팅 기반 구성·운영 | 아이디어 3. 건축 도면 자동 인식 | 해석하지 못한 장소 표현 | 공간 노드 이름·별칭 보강 |

표의 입출력은 구축자가 아이디어 정의에서 도출한 설계 가설이며, 각 트랙의 단계 3(구현 가설 설계)이 근거와 함께 확정하거나 고친다. [가정]

## 67개 세부 연구영역 매핑표

각 칸의 ●는 그 아이디어의 중심 영역, ○는 함께 필요한 영역, 빈칸은 직접 연결이 없음을 뜻한다. 원천은 각 트랙 정의(`config/tracks/*.yaml`)의 `idea_areas`이며, 퍼블리셔가 이 표와 세부영역 페이지 머리의 "관련 연구 트랙" 안내를 같은 원천에서 다시 만든다. 매핑 근거는 각 아이디어 페이지의 "2. 관련 세부 연구영역"과 결정 기록에 있다. 분류 개정 전 원문 10장이 정한 매핑(아이디어 1의 5·9·21·23·24, 아이디어 3의 6·15·21·22)과 8장의 교차 규칙(47. AI·학습·적응과 모델 운영의 문서·도면 해석)은 그대로 따랐고, 나머지는 구축자 제안이다. [가정]

<!-- auto:idea-area-map:start -->
| 대분류 | 세부 연구영역 | [아이디어 1. 로봇 기능 온톨로지](robot-capability-ontology.md) | [아이디어 2. 채팅 기반 구성·운영](chat-based-configuration-and-operation.md) | [아이디어 3. 건축 도면 자동 인식](floorplan-recognition.md) |
|---|---|---|---|---|
| [A. 기획·사업](../categories/planning-and-business/index.md) | [1. 기술·시장·업체 동향](../categories/planning-and-business/technology-market-and-vendor-trends.md) |  |  |  |
| [A. 기획·사업](../categories/planning-and-business/index.md) | [2. 사용 사례·요구·책임 범위](../categories/planning-and-business/use-cases-requirements-and-scope.md) |  |  |  |
| [A. 기획·사업](../categories/planning-and-business/index.md) | [3. 경제성·조달·사업 모델](../categories/planning-and-business/economics-procurement-and-business-models.md) |  |  |  |
| [B. 로봇 온톨로지](../categories/robot-ontology/index.md) | [4. 이기종 로봇 등록](../categories/robot-ontology/heterogeneous-robot-registration.md) | ○ |  |  |
| [B. 로봇 온톨로지](../categories/robot-ontology/index.md) | [5. 로봇 능력·작업 표현](../categories/robot-ontology/robot-capability-and-task-representation.md) | ● | ○ | ○ |
| [B. 로봇 온톨로지](../categories/robot-ontology/index.md) | [6. 온톨로지 기반 시스템·로봇 연동](../categories/robot-ontology/ontology-based-system-and-robot-integration.md) | ○ |  |  |
| [B. 로봇 온톨로지](../categories/robot-ontology/index.md) | [7. 온톨로지 검증·변경 관리](../categories/robot-ontology/ontology-verification-and-change-management.md) | ○ |  |  |
| [C. 채팅 기반 구성·운영](../categories/chat-based-configuration-and-operation/index.md) | [8. 채팅으로 맵 작성](../categories/chat-based-configuration-and-operation/chat-map-authoring.md) |  | ● | ○ |
| [C. 채팅 기반 구성·운영](../categories/chat-based-configuration-and-operation/index.md) | [9. 채팅으로 시나리오 구성](../categories/chat-based-configuration-and-operation/chat-scenario-composition.md) |  | ● |  |
| [C. 채팅 기반 구성·운영](../categories/chat-based-configuration-and-operation/index.md) | [10. 채팅으로 로봇 구성](../categories/chat-based-configuration-and-operation/chat-robot-configuration.md) |  | ● |  |
| [C. 채팅 기반 구성·운영](../categories/chat-based-configuration-and-operation/index.md) | [11. 채팅으로 실제 상황 시뮬레이션 재현](../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) |  | ● |  |
| [C. 채팅 기반 구성·운영](../categories/chat-based-configuration-and-operation/index.md) | [12. 채팅으로 업무 지시·오케스트레이션](../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md) |  | ● |  |
| [C. 채팅 기반 구성·운영](../categories/chat-based-configuration-and-operation/index.md) | [13. 대화형 기능의 신뢰·기반](../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) |  | ● |  |
| [D. 공간·지도 모델](../categories/space-and-map-model/index.md) | [14. 도면·BIM에서 지도 만들기](../categories/space-and-map-model/maps-from-floor-plans-and-bim.md) |  |  | ● |
| [D. 공간·지도 모델](../categories/space-and-map-model/index.md) | [15. 지도·공간·위치 모델](../categories/space-and-map-model/map-space-and-location-model.md) |  | ○ | ○ |
| [D. 공간·지도 모델](../categories/space-and-map-model/index.md) | [16. 장소 의미·지도 관리](../categories/space-and-map-model/place-semantics-and-map-management.md) |  |  |  |
| [E. 사물·사람·실시간 상태](../categories/objects-people-and-live-state/index.md) | [17. 작업 대상·자산 식별과 인계 추적](../categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md) |  |  |  |
| [E. 사물·사람·실시간 상태](../categories/objects-people-and-live-state/index.md) | [18. 실시간 세계 상태·데이터 일관성](../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md) | ○ | ○ | ○ |
| [E. 사물·사람·실시간 상태](../categories/objects-people-and-live-state/index.md) | [19. 사람·보행자 모델](../categories/objects-people-and-live-state/people-and-pedestrian-model.md) |  |  |  |
| [F. 연동](../categories/integration/index.md) | [20. 로봇·제조사 관제 연동](../categories/integration/robot-and-vendor-fleet-manager-integration.md) | ○ |  |  |
| [F. 연동](../categories/integration/index.md) | [21. 상호운용 표준·적합성](../categories/integration/interoperability-standards-and-conformance.md) | ○ |  | ○ |
| [F. 연동](../categories/integration/index.md) | [22. 설비·건물 시스템 연동](../categories/integration/facility-and-building-system-integration.md) | ○ |  | ○ |
| [F. 연동](../categories/integration/index.md) | [23. 업무 시스템 연동](../categories/integration/business-system-integration.md) |  | ○ |  |
| [G. 계획·최적화](../categories/planning-and-optimization/index.md) | [24. 작업·워크플로 모델링](../categories/planning-and-optimization/task-and-workflow-modeling.md) |  | ○ |  |
| [G. 계획·최적화](../categories/planning-and-optimization/index.md) | [25. 작업 배정 — MRTA](../categories/planning-and-optimization/task-allocation-mrta.md) | ○ | ○ |  |
| [G. 계획·최적화](../categories/planning-and-optimization/index.md) | [26. 작업 순서·스케줄링](../categories/planning-and-optimization/task-sequencing-and-scheduling.md) |  | ○ |  |
| [G. 계획·최적화](../categories/planning-and-optimization/index.md) | [27. 다중 로봇 경로·교통 관리 — MAPF](../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) |  |  | ○ |
| [G. 계획·최적화](../categories/planning-and-optimization/index.md) | [28. 공용 자원·충전·에너지 최적화](../categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md) | ○ | ○ | ○ |
| [H. 실행·협업·예외 복구](../categories/execution-collaboration-and-recovery/index.md) | [29. 명령·작업 실행의 신뢰성](../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md) | ○ | ○ |  |
| [H. 실행·협업·예외 복구](../categories/execution-collaboration-and-recovery/index.md) | [30. 로봇 간 협업·물리적 인계](../categories/execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md) |  |  |  |
| [H. 실행·협업·예외 복구](../categories/execution-collaboration-and-recovery/index.md) | [31. 사람–로봇 협업](../categories/execution-collaboration-and-recovery/human-robot-collaboration.md) |  | ○ |  |
| [H. 실행·협업·예외 복구](../categories/execution-collaboration-and-recovery/index.md) | [32. 예외 복구·재계획·업무 연속성](../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md) |  | ○ |  |
| [I. 설계·시뮬레이션](../categories/design-and-simulation/index.md) | [33. 시나리오 모델·편집](../categories/design-and-simulation/scenario-model-and-editing.md) |  |  |  |
| [I. 설계·시뮬레이션](../categories/design-and-simulation/index.md) | [34. 시뮬레이션·예측용 디지털 트윈](../categories/design-and-simulation/simulation-and-predictive-digital-twin.md) |  |  | ○ |
| [I. 설계·시뮬레이션](../categories/design-and-simulation/index.md) | [35. 처리능력·규모·배치 설계](../categories/design-and-simulation/capacity-sizing-and-layout-design.md) |  |  | ○ |
| [I. 설계·시뮬레이션](../categories/design-and-simulation/index.md) | [36. 가상 시운전·실제 상황 재현](../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) |  |  |  |
| [J. 현장 운영·관제](../categories/field-operations-and-monitoring/index.md) | [37. 관제 화면·실행 기록](../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) |  |  |  |
| [J. 현장 운영·관제](../categories/field-operations-and-monitoring/index.md) | [38. 모니터링·이상 탐지·원인 분석](../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) |  | ○ |  |
| [J. 현장 운영·관제](../categories/field-operations-and-monitoring/index.md) | [39. 운영 성과 측정·개선](../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md) |  |  |  |
| [J. 현장 운영·관제](../categories/field-operations-and-monitoring/index.md) | [40. 운영 절차·요청 창구](../categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md) |  |  |  |
| [K. 플랫폼 아키텍처·인프라](../categories/platform-architecture-and-infrastructure/index.md) | [41. 플랫폼 아키텍처·외부 API](../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) |  |  |  |
| [K. 플랫폼 아키텍처·인프라](../categories/platform-architecture-and-infrastructure/index.md) | [42. 분산 시스템·통신·컴퓨팅 구조](../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md) |  |  |  |
| [K. 플랫폼 아키텍처·인프라](../categories/platform-architecture-and-infrastructure/index.md) | [43. 데이터·관측성·배포](../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) |  |  |  |
| [L. AI·학습 기술](../categories/ai-and-learning/index.md) | [44. 로봇 기반 모델·언어 모델 계획](../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) |  |  |  |
| [L. AI·학습 기술](../categories/ai-and-learning/index.md) | [45. 문서·도면·장면 이해](../categories/ai-and-learning/document-drawing-and-scene-understanding.md) |  |  |  |
| [L. AI·학습 기술](../categories/ai-and-learning/index.md) | [46. 예측·학습 기반 최적화](../categories/ai-and-learning/prediction-and-learning-based-optimization.md) |  |  |  |
| [L. AI·학습 기술](../categories/ai-and-learning/index.md) | [47. AI·학습·적응과 모델 운영](../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) | ○ | ○ | ○ |
| [M. 안전](../categories/safety/index.md) | [48. 안전·위험 관리](../categories/safety/safety-and-risk-management.md) | ○ | ○ |  |
| [M. 안전](../categories/safety/index.md) | [49. 사람 근접 안전](../categories/safety/human-proximity-safety.md) |  |  |  |
| [M. 안전](../categories/safety/index.md) | [50. 안전 표준·인증·사고 조사](../categories/safety/safety-standards-certification-and-incident-investigation.md) |  |  |  |
| [N. 보안·개인정보](../categories/security-and-privacy/index.md) | [51. 인증·권한·격리](../categories/security-and-privacy/authentication-authorization-and-isolation.md) |  | ○ |  |
| [N. 보안·개인정보](../categories/security-and-privacy/index.md) | [52. 통신 보호·위협 관리·감사](../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) |  |  |  |
| [N. 보안·개인정보](../categories/security-and-privacy/index.md) | [53. 개인정보·영상 데이터](../categories/security-and-privacy/privacy-and-video-data.md) |  |  |  |
| [O. 검증·도입·수명주기](../categories/verification-deployment-and-lifecycle/index.md) | [54. 시험·형식 검증·벤치마크](../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md) | ○ | ○ | ○ |
| [O. 검증·도입·수명주기](../categories/verification-deployment-and-lifecycle/index.md) | [55. 현장 조사·설치·시운전](../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md) | ○ |  | ○ |
| [O. 검증·도입·수명주기](../categories/verification-deployment-and-lifecycle/index.md) | [56. 운영 이관·확대·교육](../categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md) |  |  |  |
| [O. 검증·도입·수명주기](../categories/verification-deployment-and-lifecycle/index.md) | [57. 자산·소프트웨어 수명주기 관리](../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) | ○ |  | ○ |
| [P. 거버넌스·법규·사회](../categories/governance-law-and-society/index.md) | [58. 다사업자 책임·계약·데이터](../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) |  |  |  |
| [P. 거버넌스·법규·사회](../categories/governance-law-and-society/index.md) | [59. 법·규제·보험·라이선스](../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) |  |  |  |
| [P. 거버넌스·법규·사회](../categories/governance-law-and-society/index.md) | [60. 노동·수용성·접근성](../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) |  |  |  |
| [Q. 현장 유형별 적용](../categories/site-type-applications/index.md) | [61. 물류창고](../categories/site-type-applications/warehouse.md) |  |  |  |
| [Q. 현장 유형별 적용](../categories/site-type-applications/index.md) | [62. 제조 공장](../categories/site-type-applications/manufacturing-plant.md) |  |  |  |
| [Q. 현장 유형별 적용](../categories/site-type-applications/index.md) | [63. 병원·의료](../categories/site-type-applications/hospital-and-healthcare.md) |  |  |  |
| [Q. 현장 유형별 적용](../categories/site-type-applications/index.md) | [64. 상업 시설](../categories/site-type-applications/commercial-facilities.md) |  |  |  |
| [Q. 현장 유형별 적용](../categories/site-type-applications/index.md) | [65. 가정·공동주택](../categories/site-type-applications/home-and-apartment.md) |  |  |  |
| [Q. 현장 유형별 적용](../categories/site-type-applications/index.md) | [66. 실외](../categories/site-type-applications/outdoor.md) |  |  |  |
| [Q. 현장 유형별 적용](../categories/site-type-applications/index.md) | [67. 기타 현장](../categories/site-type-applications/other-sites.md) |  |  |  |

● 중심 영역 · ○ 함께 필요한 영역 · 빈칸은 직접 연결 없음. 영역 수:

- 아이디어 1. 로봇 기능 온톨로지: ● 1개 · ○ 15개 · 합계 16개 영역 ([트랙 개요](../tracks/manual-capability-ontology/index.md))
- 아이디어 2. 채팅 기반 구성·운영: ● 6개 · ○ 16개 · 합계 22개 영역 ([트랙 개요](../tracks/chat-based-configuration-and-operation/index.md))
- 아이디어 3. 건축 도면 자동 인식: ● 1개 · ○ 14개 · 합계 15개 영역 ([트랙 개요](../tracks/floorplan-recognition/index.md))
<!-- auto:idea-area-map:end -->

## 관련 페이지

- [논의한 아이디어의 연구영역 매핑](../about/idea-mapping.md) — 분류 개정 전 원문 10장의 표 원문
- [매뉴얼 기반 로봇 기능 온톨로지](../tracks/manual-capability-ontology/index.md), [채팅 기반 구성·운영](../tracks/chat-based-configuration-and-operation/index.md), [건축 도면 자동 인식](../tracks/floorplan-recognition/index.md) — 세 아이디어를 연구하는 중점 연구 트랙
- [에이전트 소개](../about/agents.md) — 트랙 실행과 트랙 조사 비중 설정
````
