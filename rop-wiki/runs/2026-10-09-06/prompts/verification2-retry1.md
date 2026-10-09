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
        "ref-1120"
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
        "ref-1120",
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
      "id": "ref-1120",
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

### runs/2026-10-09-06/verification.json

```json
{
  "run_id": "2026-10-09-06",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 finops.org/framework/phases 열람 확인: Inform·Optimize·Operate 세 단계를 빠르게 되풀이하는 주기로 설명. 발행일 미확인. 브리프에서는 원문 미열람(fetched false)."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 FinOps 발표 글 열람 확인: 2025-06-03, SaaS·PaaS 청구 데이터를 같은 스키마에 포함, 청구서 대사용 invoice ID 열 추가. 명세 본문이 아닌 발표 글 기준이라는 단서 유지."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 다중 제조사 플랫폼 과금 단위 공개 자료 없음(oq-267) 단서 유지. 근거 출처 ref-1041·ref-1042·ref-1037 은 검증 중 열람 확인."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·vendor_claim true·'벤더 주장: ' 표시 확인. ref-309 는 이번 검증에서도 열지 않았다(42. 분산 시스템·통신·컴퓨팅 구조 3절 게재 주장 재인용). 기사 발행일·조사 방법·하한 미확인 단서를 본문에 유지해야 한다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·vendor_claim true 확인. ref-1023 원문 미열람(41. 플랫폼 아키텍처·외부 API 5절 재인용). 본문에 '벤더 주장' 병기 필수."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "입력 data/source_texts/ref-105 원문 대조 확인: task_capabilities(loop·delivery)와 actions 선언. 발행일 미확인."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. ref-004·ref-105 원문 텍스트 입력으로 확인. 6. 온톨로지 기반 시스템·로봇 연동이 어댑터 설정 초안을 만드는 공개 사례는 없음."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 두 기록을 잇는 공개 사례 미확인 단서 유지. ref-1040 은 검증 중 raw README 열람 확인."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 Discourse 안내문 열람 확인: 2026-06-25 게시, Open-RMF REST API 를 LLM 호출 도구로 노출하는 MCP 서버, 평이한 영어 지시를 다단계 RMF 임무로 바꾸는 에이전트, Isaac Sim 창고 시연(사전 안내 기준). 발표 내용 자체 미열람 단서 유지."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. ref-762 원문 텍스트로 OIDC·역할/동작/권한 그룹 확인, ref-854 열람 확인. 13. 대화형 기능의 신뢰·기반의 권한 집행 지점이라는 판단은 해석."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 raw 원문 열람 확인: gen_ai.client.inference.usage.input_tokens·output_tokens 등 토큰 사용량 지표, 안정성 Development. 발행일 미확인."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 근거 ref-1037·ref-1043 열람 확인(ref-1043 서론이 클라우드 API 비용·지연을 언급)."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·vendor_claim true 확인. ref-1023 원문 미열람. 위치 추정은 분류 원문 19장 로봇 자체 지능·제어 경계의 연계 대상이며 ROP 직접 범위 근거로 쓰지 않는다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ROS 2 QoS(ref-282)는 검증 중 jazzy 문서 원본(rst) 열람으로 Deadline·Liveliness 확인, Sparkplug(ref-287)는 raw 원문에서 NDEATH 수신 시 이전 NBIRTH 지표를 STALE 로 표시하는 요구 확인, VDA 5050(ref-031)은 last will·CONNECTION_BROKEN 확인. 세 출처는 각각 한 장치만 다루므로 교차 확인 아님. B·E·F 대분류 페이지와 같은 각주 재사용."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "입력 원문 텍스트 대조 확인: ref-148 unix_millis_time, ref-051 timestamp(ISO8601). E. 사물·사람·실시간 상태 대분류 페이지와 같은 각주 재사용."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. ref-045 원문 텍스트(EPCIS 2.0 온톨로지, 2021-09-30) 입력 확인. E 대분류 페이지 K 항목과 같은 연결."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 VDA5050_EN.md raw 열람 확인: 연결 실패·메시지 손실을 고려, order·instantActions·state 토픽에 QoS 0."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "ref-004 원문 텍스트 확인: 모든 플릿 관리자가 예상 이동 경로를 교통 스케줄에 보고, 제어 범주 Full Control·Traffic Light·Read Only(No Interface 는 비호환). ref-251 원문 텍스트로 보강. 같은 기관이라 교차 확인 아님."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지(42. 분산 시스템·통신·컴퓨팅 구조 5절 추론 재인용). 클라우드 WMS 새 주문·재고 확정은 상위 업무 시스템 경계의 연계 대상으로 서술해야 한다. 물류센터 운영 기준 미확인(oq-038)."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·vendor_claim true 확인. ref-1030 원문 미열람. 주문 최적화 판단은 WMS·로봇 공급사 몫이고 ROP 는 연동 인터페이스만 다룬다는 경계 문구 유지."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "검증 중 SAGE 전문 열람(PMC 는 차단): 로봇 시스템 로그는 승강기 호출·탑승·문 동작·하차 시각을 남기고, '1 Hz' 는 승강기–로봇 통신 로그(승강기 상태·문·위치·로봇 명령)의 기록 주기다. 주장은 1 Hz 를 로봇 시스템 로그에 붙여 귀속이 틀렸다. 쓰인 그대로는 [사실]로 둘 수 없다. 정정 지시대로 고쳐 쓰면 원문과 일치한다. 게시된 43. 데이터·관측성·배포 5절에도 같은 귀속 오류가 있다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 열람 확인: OpenAPI 3.1.0(2021-02-15)은 HTTP API 용 표준·언어 중립 인터페이스, AsyncAPI 3.1.0 은 메시지 기반 API 를 기계가독으로 기술하는 명세(발행일 미확인). as_of 2021-02-15 는 OpenAPI 에만 해당."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 국내 TTA·KS 표준 미확인(oq-209) 단서 유지."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 arXiv 2609.13711 초록 열람 확인: 2026-09-12 제출, CBAA·ACBBA·PI·HIPC·DMCHBA·DGA, Bernoulli·Gilbert–Elliott 손실과 Rayleigh 페이딩 조건. 프리프린트."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. G. 계획·최적화 대분류 페이지의 같은 [추정] 연결 재사용. ref-401 원문 미열람, 물류센터 적용 근거 없음(oq-083)."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 중앙 교통 스케줄 보고 구조는 ref-004 원문 텍스트로 확인. 단절 시 영향은 실측 없는 추론."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 raw 원문 열람 확인: 연결이 끊겨도 주문 정보를 유지하고 'fulfills the order up to the last released node'. 직접 인용은 이 한 구절만(ref-031 출처당 1회)."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. VDA 5050 의 QoS 0 과 '사건 발생 시 또는 적어도 30초마다' 상태 발행은 raw 원문으로 확인. 재연결 뒤 처리는 해석. ref-306 원문 미열람."
    },
    {
      "finding_id": "f29",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 PMC12390455 열람 확인: Sensors 25(16):5067, 2025-08-14, Turtlebot4 4대·OptiTrack 실내 실험, Kubernetes 복구로 노드 장애 중에도 위치 정확도 유지. 다만 5개 파드 모두 종료한 조건에서 한 로봇 RMSE 가 0.230 m 로 올랐다는 예외가 있다. 실험실 결과 단서 유지."
    },
    {
      "finding_id": "f30",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "ref-374 는 F. 연동 대분류 페이지에 게재된 출처이나 이번 검증에서 GitHub 이슈·API 모두 403 이었고, 검색으로도 이슈 #224 와 SQLite 풀 리퀘스트 언급을 찾지 못했다(실재 확인은 이전 게재 기록 기준). '재시작하면 배정된 작업 추적을 잃는다'는 취지는 Open-RMF Discourse 의 옛 스레드(#5) 검색 결과와 맞지만, SQLite 백업 제안 부분은 이번에 확인하지 못했다. [사실] → [추정]."
    },
    {
      "finding_id": "f31",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 arXiv 2412.05408 초록 열람 확인: 독립적인 상태 비저장(stateless) 로봇 서비스를 여러 클라우드에 자동 복제하고 먼저 온 응답을 쓰는 방식, IROS 2024 최우수 논문 후보. 대상이 상태 비저장 서비스라는 범위를 본문에 밝혀야 한다(작업 상태 보존과 혼동 방지)."
    },
    {
      "finding_id": "f32",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 KubeEdge raw README 열람 확인: 클라우드–엣지 네트워크가 불안정할 때 엣지 노드·애플리케이션이 자율적으로 정상 동작(Edge Autonomy), 오프라인·재시작 노드도 다룸. 42. 분산 시스템·통신·컴퓨팅 구조 7절과 같은 각주 재사용. 발행일 미확인."
    },
    {
      "finding_id": "f33",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·vendor_claim true 확인. ref-1044 원문 미열람(43. 데이터·관측성·배포 5절 재인용). 시뮬레이션은 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈의 내용이며 배포 전 검증 근거로만 쓴다."
    },
    {
      "finding_id": "f34",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 ros2_documentation 원본(rst)과 rosbag2 raw README 열람 확인: Iron GA 2023-05-23, 새 백의 기본 형식 mcap, ~/set_rate·rate 매개변수, --clock 으로 /clock 발행, -i 여러 백을 원래 기록 시각순으로 재생. 두 출처는 다른 내용이라 교차 확인 아님."
    },
    {
      "finding_id": "f35",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 지난 기록을 다루는 36. 가상 시운전·실제 상황 재현 연결과 현재 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성의 구분이 명시돼 있다. oq-131·oq-211 미해결."
    },
    {
      "finding_id": "f36",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "입력 data/source_texts/ref-762 대조 확인: 기본 in-memory SQLite, PostgreSQL·SQLite·MySQL·MariaDB 지원. J. 현장 운영·관제 연결 조사(2026-10-09-05 f6)와 같은 주장."
    },
    {
      "finding_id": "f37",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 arXiv 2201.00393 초록 열람 확인: 모든 ROS 2 계측을 켰을 때 종단 메시지 지연 오버헤드 평균 0.0033 ms, IEEE RA-L 7(3), 2022-07. 저자 실험값·독립 재현 미확인 단서 유지. 같은 논문이 ref-1361 로도 등록돼 있으므로 ref-1032 하나만 쓴다."
    },
    {
      "finding_id": "f38",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. J. 현장 운영·관제 브리프(2026-10-09-05 f21)와 같은 연결이나 그쪽은 ref-447·ref-1361 을 썼다. 이번에는 ref-1036·ref-1032 를 쓴다. ref-1036 원문 미열람. oq-210 미해결."
    },
    {
      "finding_id": "f39",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 arXiv 2606.10746 초록 열람 확인: 2026-06-09 제출, DDS 도메인에 참여하는 관찰 도구의 probe effect 를 커널 안 선택 필터로 줄임. 프리프린트."
    },
    {
      "finding_id": "f40",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 arXiv 초록과 HTML 전문 서론 열람: 2026-09-24 제출(IEEE GCCE 2026 채택), 로컬 오픈소스·클라우드 모델 3종 비교. 서론이 클라우드 API 의 요청당 비용 누적·네트워크 지연·연결 의존 위험을 로컬 배치의 이유로 든다. 실험은 계획 성공률만 측정하고 비용·지연은 측정하지 않았다는 단서를 덧붙일 것."
    },
    {
      "finding_id": "f41",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 arXiv 2205.09778 초록 열람 확인: 클라우드·포그 로보틱스를 돕는 오픈소스 플랫폼, 2022-05-19 제출(v2 2023-04-24). 로봇 내부 계산의 실행 위치 선택은 로봇 자체 지능·제어 경계의 연계 대상."
    },
    {
      "finding_id": "f42",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 raw 원문 열람 확인: 기능·운영·시스템 안전 요구를 정하지 않으며 안전 표준으로 간주·적용해서는 안 된다고 명시. G. 계획·최적화 대분류 페이지와 같은 각주."
    },
    {
      "finding_id": "f43",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 arXiv 2205.06564 초록 열람 확인: 2022-05-13, 소셜 로봇의 센서·구동기·제어 결정 데이터를 안전하게 기록해 사고 조사를 돕는 하드웨어·소프트웨어 기록 장치의 초안 공개 표준. 플릿·플랫폼 수준 기록은 다루지 않는다는 단서 유지."
    },
    {
      "finding_id": "f44",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 단일 로봇 블랙박스와 개인정보 접속기록 고시를 플랫폼 기록에 옮긴 추론. oq-211 미해결."
    },
    {
      "finding_id": "f45",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "입력 data/source_texts/ref-762 대조 확인: OIDC 신원 공급자 인증, 앱 안 역할·동작·권한 그룹 판정, 관리자 전 권한, 현재 모든 자원은 빈 문자열 기본 그룹."
    },
    {
      "finding_id": "f46",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "입력 원문 텍스트 대조 확인: ref-009 의 PKI 인증·거버넌스/권한 파일 접근통제·암호화 플러그인, ref-405 의 SROS 2 인클레이브와 대시보드 TLS·OIDC. 서로 다른 계층이라 교차 확인 아님. F. 연동 대분류 페이지와 같은 각주."
    },
    {
      "finding_id": "f47",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "국가법령정보센터 원문은 열지 않았다. 검색 결과(2차 게재 사이트)로 개인정보보호위원회고시 제2023-6호(2023-09-22 시행) 제8조 '접속기록의 보관 및 점검' 존재 확인(원문 미열람). 현행 조문 동일 여부 미확인(oq-214)."
    },
    {
      "finding_id": "f48",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 mender raw README 열람 확인: IoT·임베디드 리눅스용 오픈소스 OTA 업데이트 관리자, 이중 A/B rootfs 이미지 배포, 실패 시 자동 롤백. 로봇 운영체제·펌웨어 무선 업데이트는 연계 대상 문구 유지."
    },
    {
      "finding_id": "f49",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지(비벤더 출처). 두 출처 모두 운행 중 작업과의 관계는 다루지 않는다는 단서 유지(oq-213)."
    },
    {
      "finding_id": "f50",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·'연계 대상: ' 표시 유지. 법적 보관 의무 해석은 59. 법·규제·보험·라이선스와 운영 사업자 몫으로만 짧게 다룬다."
    },
    {
      "finding_id": "f51",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 창이종합병원 CHART 페이지 열람 확인: Machine·Control·Central·Integration 네 도메인(층), OMG DDS 사용, 2019-10-31 ROSCon 2019 공식 출범. 페이지 표현은 'zone' 이 아니라 'domain' 이므로 '영역' 표기는 유지 가능."
    },
    {
      "finding_id": "f52",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 arXiv 2512.15215 초록 열람 확인: 2025-12-17 제출, 기반 시설 센싱·현장(on-premise) 클라우드 컴퓨팅·온보드 자율을 결합한 기준 아키텍처, heavy-vehicle 제조 환경 실배치와 사용자 경험 평가. 초록은 판단을 층별로 어떻게 나누는지는 밝히지 않는다."
    },
    {
      "finding_id": "f53",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·vendor_claim true 확인. ref-307 원문 미열람. 5G 특화망 구축은 ROP 가 소유하지 않는 통신 기반 연계 대상에 가깝다는 문구 유지."
    },
    {
      "finding_id": "f54",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검증 중 SAGE 전문 열람 확인(2026-03-31 온라인 게재): 2025-06-18~29 비응급 임무 122건, 실패 14건 = 승강기 진입·하차 막힘 8, 복도 자율주행 오류 4, 승강기 호출 통신 오류 2. 논문의 전체 성공률 87.03% 는 108/122(약 88.5%)와 맞지 않는다(oq-215)."
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
      "f14·f15·f16 은 E. 사물·사람·실시간 상태 대분류 페이지의 K 항목·F 항목 연결과 같은 주장이다 — 같은 각주(ref-282·ref-287·ref-031·ref-148·ref-051·ref-045)를 재사용하고 태그도 그 페이지와 같게 둔다",
      "f6·f18·f30·f46 은 B. 로봇 온톨로지·F. 연동 대분류 페이지의 연결과 같은 주장이다 — 같은 각주 재사용",
      "f24·f25 는 G. 계획·최적화 대분류 페이지의 25. 작업 배정 — MRTA ↔ 42. 분산 시스템·통신·컴퓨팅 구조 연결과 같다 — 태그(f24 사실, f25 추정) 유지",
      "f36·f37·f38·f43·f45 는 J. 현장 운영·관제 연결 브리프(2026-10-09-05 f6·f22·f21·f10·f37)와 같은 주장이다. 그 브리프의 ref-1361 은 ref-1032 와 같은 arXiv 2201.00393 논문이다 — 이번 절에서는 ref-1032 하나만 쓴다",
      "f21·f54 의 ref-943(PMC 링크)은 참고문헌의 ref-060(doi 링크)과 같은 Lee 외 Digital Health 논문이다 — 이번 절에서는 ref-943 하나만 인용한다",
      "f21 은 게시된 43. 데이터·관측성·배포 5절의 문장('로봇 시스템 로그는 … 1 Hz 로 남겼고')과 같은 귀속 오류를 갖는다. 원문(SAGE 전문)에서는 1 Hz 가 승강기–로봇 통신 로그의 주기다 — 이번 절은 정정해 쓰고, 43 페이지 정정은 다음 갱신 실행으로 넘긴다",
      "f17·f19·f27·f28·f32 는 42. 분산 시스템·통신·컴퓨팅 구조 5·7절의 검증된 주장과 같다 — 같은 각주 재사용",
      "새 열린 질문 1(플랫폼 서비스 재시작 뒤 작업 상태 보존)은 oq-048(어댑터 SQLite 복구의 배포판 반영)·oq-213(무중단 순차 배포)과 인접한다 — 중복은 아니나 본문에서 함께 연결한다"
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
    "patches 의 절 제목: '5. 다른 대분류와의 연결'이 아니라 번호 없는 '다른 대분류와의 연결'로 보낸다 — 대분류 페이지 절 제목 정본(부록 C category)은 번호가 없고 입력 페이지의 H2 도 '다른 대분류와의 연결'이다.",
    "f21: '승강기 호출·탑승·문 동작 시각을 1 Hz 로 남긴 로봇 시스템 로그'를 '승강기 호출·탑승·문 동작·하차 시각을 남긴 로봇 시스템 로그, 승강기 상태·문·위치·로봇 명령을 1 Hz 로 남긴 승강기–로봇 통신 로그, 관찰자 기록지'로 고쳐 쓴다. 이렇게 정정하면 [사실][^ref-943]으로 둘 수 있고, 정정하지 않으면 [추정]으로 강등한다 — 검증 중 원문(SAGE 전문)에서 1 Hz 는 승강기–로봇 통신 로그의 주기로 확인됐다. 승강기 통신 로그 생성은 시설·설비 제어 경계의 연계 대상이고 ROP 몫은 수집·결합이라는 문구를 유지한다.",
    "f30: [사실] → [추정]으로 강등하고, 'SQLite 백업 기능이 별도 풀 리퀘스트로 제안되었다' 부분은 쓰지 않거나 '이번 확인에서 재확인하지 못함'을 밝힌다 — ref-374 를 이번 검증에서 열지 못했고(403) 검색으로도 그 내용을 확인하지 못했다. 배포판 반영 여부 미확인(oq-048) 연결은 유지한다.",
    "f31: 'FogROS2-FT 는 독립적인 상태 비저장(stateless) 로봇 서비스를 여러 클라우드에 복제하고 먼저 온 응답을 쓴다'로 범위를 밝힌다 — 초록이 대상을 상태 비저장 서비스로 한정하므로, 32. 예외 복구·재계획·업무 연속성의 작업 상태 보존 근거처럼 읽히지 않게 한다.",
    "f52: '판단을 세 층에 나눠 두는 기준 아키텍처'를 '기반 시설 센싱·현장(on-premise) 클라우드 컴퓨팅·온보드 자율을 결합한 기준 아키텍처'로, '대형 상용차'를 '대형 차량(heavy-vehicle)'으로 고친다 — 초록 표현이 그렇고 층별 판단 분담은 초록에 없다.",
    "f40: '비교의 동기는 클라우드 API 비용과 지연이었다' 뒤에 '비용·지연 자체는 측정하지 않았다'는 단서를 붙인다 — 검증 중 전문 서론에서 동기는 확인했으나 실험은 계획 성공률만 측정했다.",
    "f22: AsyncAPI 3.1.0 의 각주 발행일은 '미확인'으로 두고, 기준일 2021-02-15 는 OpenAPI 3.1.0 에만 붙인다 — 브리프 as_of 가 두 명세에 함께 걸려 있다.",
    "f37·f38: ros2_tracing 은 ref-1032 하나로만 인용하고 ref-1361 을 같은 절에 쓰지 않는다 — 두 id 가 같은 arXiv 2201.00393 논문이다. f21·f54 의 병원 논문도 ref-943 하나로만 인용하고 ref-060 을 함께 붙이지 않는다.",
    "f4·f5·f13·f20·f33·f53: 본문에 [추정]과 '벤더 주장'을 병기한다 — 모두 제조사·판매사 자료이고 독립 확인이 없다(f4 는 판매사 조사를 인용한 기사).",
    "범위 경계 문구: f13·f41(위치 추정·로봇 내부 계산 배치)은 로봇 자체 지능·제어 경계, f21(승강기 통신 로그 생성)은 시설·설비 제어 경계, f19·f20(WMS 주문·재고 판단)은 상위 업무 시스템 경계, f48(로봇 OS·펌웨어 무선 업데이트)·f53(무선망 구축)은 연계 대상임을 각 문장에서 짧게 밝힌다. f50 은 '연계 대상:'으로 시작하는 문장으로 둔다 — 분류 원문 19장.",
    "18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈: f14·f15·f16 은 현재 상태를 표현하는 18 쪽으로, f33 은 가정한 미래를 실험하는 34 쪽으로, f34·f35 는 지난 기록을 재현하는 36. 가상 시운전·실제 상황 재현 쪽으로 나눠 쓰고, 셋을 '디지털 트윈'이라는 한 이름으로 섞지 않는다.",
    "C. 채팅 기반 구성·운영 항목(f9~f12)은 분류 원문 4장 주석대로 12. 채팅으로 업무 지시·오케스트레이션의 엔진이 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링임을 밝히고 G. 계획·최적화 항목과 함께 읽게 연결한다. L. AI·학습 기술 항목(f40·f41)은 44. 로봇 기반 모델·언어 모델 계획 링크와 적용 대상인 K 쪽 세부영역(41·42·43) 링크를 함께 둔다 — 공통 규칙 5.",
    "'아직 다루지 않은 연결' 목록을 finding 이 실제로 다루지 않은 세부영역과 맞춘다: 2. 사용 사례·요구·책임 범위, 4. 이기종 로봇 등록, 5. 로봇 능력·작업 표현, 8. 채팅으로 맵 작성, 9. 채팅으로 시나리오 구성, 10. 채팅으로 로봇 구성, 11. 채팅으로 실제 상황 시뮬레이션 재현, 14. 도면·BIM에서 지도 만들기, 16. 장소 의미·지도 관리, 19. 사람·보행자 모델, 24. 작업·워크플로 모델링, 26. 작업 순서·스케줄링, 28. 공용 자원·충전·에너지 최적화, 30. 로봇 간 협업·물리적 인계, 31. 사람–로봇 협업, 33. 시나리오 모델·편집, 35. 처리능력·규모·배치 설계, 39. 운영 성과 측정·개선, 40. 운영 절차·요청 창구, 45. 문서·도면·장면 이해, 46. 예측·학습 기반 최적화, 47. AI·학습·적응과 모델 운영, 49. 사람 근접 안전, 54. 시험·형식 검증·벤치마크, 55. 현장 조사·설치·시운전, 56. 운영 이관·확대·교육, 58. 다사업자 책임·계약·데이터, 60. 노동·수용성·접근성, 64. 상업 시설, 65. 가정·공동주택, 66. 실외. P. 거버넌스·법규·사회 연결은 f50 하나(연계 대상 추정)뿐임을 밝힌다. '모든 대분류와 연결' 같은 완전성 표현은 쓰지 않는다.",
    "Q. 현장 유형별 적용 항목은 사례마다 현장 유형을 이름으로 밝힌다: f51·f54·f21 병원(63. 병원·의료), f52 제조 공장(62. 제조 공장), f4·f19·f20·f33·f53 물류창고(61. 물류창고), f5·f13 기타(67. 기타 현장, 기업 사옥). f51 은 특정 병원의 배치 결과가 아니라 미들웨어 구조라는 단서를 유지한다.",
    "각주 원문 미열람 표기: 브리프에서 fetched false 인 출처(ref-282, ref-300, ref-304, ref-306, ref-307, ref-308, ref-309, ref-310, ref-374, ref-401, ref-493, ref-766, ref-831, ref-854, ref-937, ref-943, ref-1023, ref-1024, ref-1025, ref-1030, ref-1031, ref-1032, ref-1033, ref-1034, ref-1036, ref-1037, ref-1039, ref-1040, ref-1041, ref-1042, ref-1043, ref-1044, ref-1120)의 각주 정의에는 접근일 2026-10-09 뒤 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣는다. 입력에 data/source_texts 원문이 있는 ref-004, ref-009, ref-031, ref-045, ref-051, ref-105, ref-148, ref-251, ref-287, ref-405, ref-762 에는 표기하지 않는다.",
    "각주 형식: 기존 참고문헌 줄을 그대로 쓰되 발행일을 아는 것은 채운다 — ref-1042 2025-06-03, ref-1025 2021-02-15, ref-1034 2023-05-23, ref-943 2026-03-31, ref-1039 2025-08-14, ref-1120 2022-05-13, ref-045 2021-09-30. ref-766 의 제목·발행일은 43. 데이터·관측성·배포 페이지 각주(개인정보보호위원회고시 제2023-6호, 2023-09-22)와 맞춘다.",
    "f47·f50: 접속기록 보관 조항은 '2023-09-22 시행 판 고시 제8조 기준, 현행 조문 미확인(oq-214)'으로만 쓰고 구체 보관 기간 수치는 넣지 않는다 — 검증은 2차 게재 사이트 검색 결과로만 했다.",
    "open_question_updates: 새 질문 1은 관련 영역을 '43. 데이터·관측성·배포, 41. 플랫폼 아키텍처·외부 API, 32. 예외 복구·재계획·업무 연속성'으로 두고 본문에서 oq-048·oq-213 과 함께 연결한다. 새 질문 2는 '41. 플랫폼 아키텍처·외부 API, 21. 상호운용 표준·적합성'으로 두고 oq-209 와 함께 연결한다. question 문자열에 '|'·'관련 영역:' 같은 필드 문자열을 남기지 않는다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 52건, 미확인 2건(f21·f30), 교차 확인 0건. 강등: f21 사실 → 추정(1 Hz 를 로봇 시스템 로그에 잘못 붙임 — 원문대로 승강기–로봇 통신 로그로 정정하면 사실 유지 가능), f30 사실 → 추정(ref-374 를 이번에 열지 못했고 SQLite 백업 제안 부분 미확인). 원문 미열람 출처: ref-282, ref-300, ref-304, ref-306, ref-307, ref-308, ref-309, ref-310, ref-374, ref-401, ref-493, ref-766, ref-831, ref-854, ref-937, ref-943, ref-1023, ref-1024, ref-1025, ref-1030, ref-1031, ref-1032, ref-1033, ref-1034, ref-1036, ref-1037, ref-1039, ref-1040, ref-1041, ref-1042, ref-1043, ref-1044, ref-1120(브리프 기준). 이 가운데 검증 중 ref-282·ref-300·ref-304·ref-308·ref-493·ref-831·ref-854·ref-937·ref-943·ref-1024·ref-1025·ref-1031·ref-1032·ref-1033·ref-1034·ref-1037·ref-1039·ref-1040·ref-1041·ref-1042·ref-1043·ref-1120 은 원문·초록을 열어 해당 진술을 확인했고, ref-766 은 검색 결과로만 확인했으며, ref-306·ref-307·ref-309·ref-310·ref-374·ref-401·ref-1023·ref-1030·ref-1036·ref-1044 는 열지 않았다. 주의: 이 절의 연결은 모두 단일 출처이거나 게시된 세부영역·대분류 페이지의 재인용이고, 연결 해석 22건은 [추정]이다. 벤더 주장 6건(f4·f5·f13·f20·f33·f53)은 독립 확인되지 않았다. 상업 시설·가정·실외 현장 근거가 없다. 브리프는 재실행에서 새 검색 없이 재구성되어, ref-004·009·031·045·051·105·148·251·287·405·762 를 fetched true 로 두면서 요약은 '원문 미열람.'으로 쓰고 자체 점검에는 '모두 fetched false'라고 적는 등 열람 표시가 어긋난다(입력의 data/source_texts 원문으로 이 11건의 열람은 인정했다). 게시된 43. 데이터·관측성·배포 5절에도 f21 과 같은 1 Hz 귀속 오류가 있어 다음 갱신 실행에서 정정이 필요하다. ros2_tracing 이 ref-1032·ref-1361 로, 구로병원 논문이 ref-943·ref-060 으로 참고문헌에 이중 등록돼 있다. 구로병원 논문의 성공률 87.03% 는 실패 14건/122건(약 88.5%)과 맞지 않는다(oq-215). 정정 요청 없음. 검증 검색 4회, 열람 약 30회.",
  "retry_reason": null
}
```

### runs/2026-10-09-06/pages.json

```json
{
  "run_id": "2026-10-09-06",
  "outline": [
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/index.md",
      "section": "다른 대분류와의 연결",
      "budget_chars": 9000,
      "summary": "K. 플랫폼 아키텍처·인프라의 41. 플랫폼 아키텍처·외부 API, 42. 분산 시스템·통신·컴퓨팅 구조, 43. 데이터·관측성·배포가 A~Q 가운데 16개 대분류의 세부영역과 어디서 만나는지 대분류별로 정리한다. 연결 해석은 모두 [추정]이고 벤더 자료에는 '벤더 주장'을 병기했다.",
      "planned_findings": [
        "A: f1·f2·f3·f4·f5",
        "B: f6·f7·f8",
        "C: f9·f10·f11·f12 (25. 작업 배정 — MRTA·26. 작업 순서·스케줄링 엔진 짝 명시)",
        "D: f13",
        "E: f14·f15·f16 (18. 실시간 세계 상태·데이터 일관성, 현재 상태)",
        "F: f17·f18·f19·f20·f21(정정)·f22·f23",
        "G: f24·f25·f26",
        "H: f27·f28·f29·f30(강등)·f31(상태 비저장 범위)·f32",
        "I: f33(34. 시뮬레이션·예측용 디지털 트윈, 가정한 미래)·f34·f35(36. 가상 시운전·실제 상황 재현, 지난 기록)",
        "J: f36·f37·f38·f39",
        "L: f40(측정 단서)·f41, 적용 대상 41·42·43 세부영역 링크",
        "M: f42·f43·f44",
        "N: f45·f46·f47",
        "O: f48·f49",
        "P: f50(연계 대상)",
        "Q: f51·f52(정정)·f53·f54, 기타 현장 f5·f13",
        "아직 다루지 않은 연결 목록"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/index.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "'다른 대분류와의 연결' 절 신규 작성: 16개 대분류별 세부영역 연결(추정 연결 표시, 벤더 주장 6건 병기), 현장 유형별 사례, 아직 다루지 않은 세부영역 목록, 절 끝 각주 정의 44건. 2차 수정: L. AI·학습 기술 항목에 적용 대상 세부영역 링크, 약어 첫 등장 풀어 쓰기",
      "patches": [
        {
          "section": "다른 대분류와의 연결",
          "action": "replace",
          "frontmatter": {
            "sources": [
              "ref-004",
              "ref-009",
              "ref-031",
              "ref-045",
              "ref-051",
              "ref-105",
              "ref-148",
              "ref-251",
              "ref-282",
              "ref-287",
              "ref-300",
              "ref-304",
              "ref-306",
              "ref-307",
              "ref-308",
              "ref-309",
              "ref-310",
              "ref-374",
              "ref-401",
              "ref-405",
              "ref-493",
              "ref-762",
              "ref-766",
              "ref-831",
              "ref-854",
              "ref-937",
              "ref-943",
              "ref-1023",
              "ref-1024",
              "ref-1025",
              "ref-1030",
              "ref-1031",
              "ref-1032",
              "ref-1033",
              "ref-1034",
              "ref-1036",
              "ref-1037",
              "ref-1039",
              "ref-1040",
              "ref-1041",
              "ref-1042",
              "ref-1043",
              "ref-1044",
              "ref-1120"
            ]
          },
          "content": "(절 본문 생략 — runs/2026-10-09-06/pages/categories/platform-architecture-and-infrastructure/index.md 의 해당 절을 본다)"
        }
      ]
    }
  ],
  "changelog_entry": "2026-10-09 | K. 플랫폼 아키텍처·인프라 | '다른 대분류와의 연결' 절 신규 작성(16개 대분류의 세부영역 연결, 조건부 승인 수정 18건과 2차 수정 5건 반영: f21 1 Hz 귀속 정정, f30 추정 강등) | run 2026-10-09-06",
  "index_updates": {
    "home_recent": "2026-10-09 — K. 플랫폼 아키텍처·인프라: '다른 대분류와의 연결' 절을 처음 작성했다. 41. 플랫폼 아키텍처·외부 API, 42. 분산 시스템·통신·컴퓨팅 구조, 43. 데이터·관측성·배포 세부영역이 다른 대분류의 세부영역과 만나는 지점, 현장 유형별 사례, 아직 다루지 않은 세부영역 목록을 담았다",
    "category_recent": "2026-10-09 — K. 플랫폼 아키텍처·인프라: '다른 대분류와의 연결' 절 작성(비용·어댑터·대화 API·통신 단절·기록·보안·배포 연결, 추정 연결과 벤더 주장 표시)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "mqtt-last-will",
      "term_ko": "MQTT 유언 메시지",
      "term_en": "MQTT Last Will (Will Message)",
      "definition": "MQTT 클라이언트가 접속할 때 브로커에 맡겨 두고, 연결이 예기치 않게 끊기면 브로커가 대신 발행하는 메시지다. VDA 5050 은 이를 써서 로봇의 연결 끊김(CONNECTION_BROKEN)을 알린다.",
      "related_areas": [
        42,
        20,
        18
      ],
      "sources": [
        "ref-031"
      ]
    },
    {
      "action": "new",
      "slug": "a-b-update",
      "term_ko": "A/B 업데이트",
      "term_en": "A/B Update (Dual Partition Update with Rollback)",
      "definition": "장치에 두 개의 시스템 영역을 두고 쓰지 않는 쪽에 새 이미지를 설치한 뒤 전환하며, 실패하면 이전 영역으로 되돌리는 소프트웨어 업데이트 방식이다.",
      "related_areas": [
        43,
        57
      ],
      "sources": [
        "ref-1040"
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
      "accessed": "2026-10-09",
      "summary": "Open-RMF 의 작업·교통 조율, 플릿 어댑터, 설비 연동 구조 개요.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "summary": "ROS 2 의 DDS 보안 규격 인증·접근통제·암호화 플러그인 통합 설계.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "summary": "관제–이동로봇 통신 명세(3.0.0). 무선망 전제, MQTT QoS, 연결 단절 시 동작, 안전 표준 아님을 명시한다.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "summary": "EPCIS 2.0 온톨로지. 발생 시각·기록 시각·UTC 차이를 구분한다.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "summary": "VDA 5050 상태 메시지 JSON 스키마(시각, 적재물, 위치추정 품질 등).",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "summary": "Open-RMF 플릿 어댑터 템플릿 설정(task_capabilities, actions, 충전 설정, 기준 좌표).",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "summary": "Open-RMF 로봇 상태 스키마(상태 값, 배터리, 문제 목록, 밀리초 시각).",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "summary": "플릿 연동의 제어 수준(전체 제어·신호등·읽기 전용) 설명.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "summary": "Sparkplug 운영 동작. 노드 종료(NDEATH) 뒤 지표의 STALE 표시.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "summary": "원문 미열람. 기반 시설 센싱·현장 클라우드 컴퓨팅·온보드 자율을 결합한 기준 아키텍처와 대형 차량 제조 현장 실배치.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "summary": "원문 미열람. 플릿 어댑터 재시작 시 작업 유실 문제를 다룬 이슈(복구 제안 내용은 이번 확인에서 재확인하지 못함).",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "summary": "SROS 2 인클레이브, 대시보드 TLS·OIDC 등 Open-RMF 보안 구성 설명.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "summary": "rmf-server 의 데이터베이스 설정과 OIDC 인증·권한 그룹 설명.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-766",
      "org": "국가법령정보센터(개인정보보호위원회 고시)",
      "title": "개인정보의 안전성 확보조치 기준(개인정보보호위원회고시 제2023-6호)",
      "published": "2023-09-22",
      "url": "https://www.law.go.kr/admRulLsInfoP.do?chrClsCd=010202&admRulSeq=2100000229672",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 개인정보 처리자의 안전성 확보조치 기준 고시(제2023-6호, 2023-09-22 시행 판 제8조 접속기록 보관·점검 조항, 현행 조문 미확인).",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
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
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 구로병원 약품 배송 로봇 122건 실증. 로봇 시스템 로그·1 Hz 승강기–로봇 통신 로그·관찰자 기록지 기반 실패 분석.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "summary": "원문 미열람. 상태 비저장 로봇 서비스를 여러 클라우드에 복제해 먼저 온 응답을 쓰는 클라우드 로보틱스 장애 허용 연구.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "summary": "원문 미열람. 서비스 로봇 LLM 연쇄 작업 계획에서 로컬·클라우드 모델 비교(프리프린트, 계획 성공률만 측정).",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
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
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1120",
      "org": "Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv)",
      "title": "An Ethical Black Box for Social Robots: a draft Open Standard",
      "published": "2022-05-13",
      "url": "https://arxiv.org/abs/2205.06564",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 사고 조사를 위한 소셜 로봇 데이터 기록 장치의 초안 공개 표준.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/index.md"
      ],
      "source_unopened": true
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "플랫폼 관제 서비스를 다중 클라우드 복제나 컨테이너 자동 재시작으로 운영하면서, 재시작 뒤 진행 중인 로봇 작업 상태를 잃지 않고 이어 간 공개 사례나 구성이 있는가?",
      "areas": [
        43,
        41,
        32
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "로봇 오케스트레이션 플랫폼의 외부 API 를 OpenAPI·AsyncAPI 로 기술해 연동 적합성 시험의 기준으로 쓴 공개 시험 도구나 절차가 있는가?",
      "areas": [
        41,
        21
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "물류창고",
      "item": "예외·성과",
      "link": "docs/categories/platform-architecture-and-infrastructure/index.md#다른-대분류와의-연결",
      "title": "K. 플랫폼 아키텍처·인프라"
    },
    {
      "site_type": "물류창고",
      "item": "완료·인계",
      "link": "docs/categories/platform-architecture-and-infrastructure/index.md#다른-대분류와의-연결",
      "title": "K. 플랫폼 아키텍처·인프라"
    },
    {
      "site_type": "물류창고",
      "item": "시작 조건",
      "link": "docs/categories/platform-architecture-and-infrastructure/index.md#다른-대분류와의-연결",
      "title": "K. 플랫폼 아키텍처·인프라"
    },
    {
      "site_type": "물류창고",
      "item": "제약",
      "link": "docs/categories/platform-architecture-and-infrastructure/index.md#다른-대분류와의-연결",
      "title": "K. 플랫폼 아키텍처·인프라"
    },
    {
      "site_type": "병원",
      "item": "예외·성과",
      "link": "docs/categories/platform-architecture-and-infrastructure/index.md#다른-대분류와의-연결",
      "title": "K. 플랫폼 아키텍처·인프라"
    },
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/platform-architecture-and-infrastructure/index.md#다른-대분류와의-연결",
      "title": "K. 플랫폼 아키텍처·인프라"
    },
    {
      "site_type": "제조 공장",
      "item": "수행 자원",
      "link": "docs/categories/platform-architecture-and-infrastructure/index.md#다른-대분류와의-연결",
      "title": "K. 플랫폼 아키텍처·인프라"
    },
    {
      "site_type": "기타",
      "item": "수행 자원",
      "link": "docs/categories/platform-architecture-and-infrastructure/index.md#다른-대분류와의-연결",
      "title": "K. 플랫폼 아키텍처·인프라"
    }
  ],
  "additional_research_requests": [
    "43. 데이터·관측성·배포 5절 병원 사례의 '로봇 시스템 로그는 … 1 Hz 로 남겼고' 문장은 1차 검증에서 귀속 오류로 확인됐다(1 Hz 는 승강기–로봇 통신 로그의 주기). 다음 갱신 실행에서 ref-943 원문(SAGE 전문)으로 정정이 필요하다.",
    "ref-374(Open-RMF rmf_ros2 이슈 #224)를 다시 열어 SQLite 작업 로그·백업 복구 풀 리퀘스트 제안과 현재 배포판 반영 여부를 확인해야 한다(H. 실행·협업·예외 복구 항목을 [사실]로 되돌릴 근거, oq-048).",
    "K. 플랫폼 아키텍처·인프라와 P. 거버넌스·법규·사회의 58. 다사업자 책임·계약·데이터(API 변경 정책·데이터 접근 책임 등), 60. 노동·수용성·접근성을 잇는 검증된 근거가 없다. 대분류 연결 절의 P 항목이 연계 대상 추정 하나뿐이다.",
    "Q. 현장 유형별 적용의 64. 상업 시설, 65. 가정·공동주택, 66. 실외 현장에서 플랫폼 배치(클라우드·현장 서버·로봇 분담)나 통신 단절 대응을 다룬 사례가 필요하다.",
    "K. 플랫폼 아키텍처·인프라 대분류 페이지 '다른 대분류와의 연결' 절의 '아직 다루지 않은 연결' 목록에 있는 세부영역과 K. 플랫폼 아키텍처·인프라를 잇는 근거 조사가 필요하다. 특히 C. 채팅 기반 구성·운영의 8. 채팅으로 맵 작성 ~ 11. 채팅으로 실제 상황 시뮬레이션 재현과 그 짝 엔진 영역, 55. 현장 조사·설치·시운전의 현장 네트워크 조사가 우선 후보다.",
    "참고문헌 중복 등록 정리 요청: ros2_tracing 논문이 ref-1032·ref-1361 로, 구로병원 논문이 ref-943·ref-060 으로 이중 등록돼 있다(이번 절은 ref-1032·ref-943 만 인용)."
  ],
  "fixes_applied": [
    "patches 절 제목 — 번호 없는 '다른 대분류와의 연결'로 보냈다.",
    "f21 — F. 연동의 22. 설비·건물 시스템 연동 항목을 '승강기 호출·탑승·문 동작·하차 시각을 남긴 로봇 시스템 로그, 승강기 상태·문·위치·로봇 명령을 1 Hz 로 남긴 승강기–로봇 통신 로그, 관찰자 기록지'로 정정해 [사실][^ref-943]으로 두고, 승강기 통신 로그 생성은 시설·설비 제어 경계의 연계 대상이며 ROP 몫은 수집·결합이라는 문장을 유지했다.",
    "f30 — H. 실행·협업·예외 복구 항목을 [추정][^ref-374]로 강등하고 SQLite 백업 풀 리퀘스트 내용은 쓰지 않았으며, 복구 제안 내용과 배포판 반영 여부를 이번 확인에서 재확인하지 못했음을 밝히고 oq-048 연결을 유지했다.",
    "f31 — FogROS2-FT 를 '독립적인 상태 비저장(stateless) 로봇 서비스를 여러 클라우드에 복제하고 먼저 온 응답을 쓴다'로 고치고, 진행 중 작업 상태 보존의 근거로 읽지 않는다는 문장을 덧붙였다.",
    "f52 — Q. 현장 유형별 적용의 제조 공장 항목을 '기반 시설 센싱·현장(on-premise) 클라우드 컴퓨팅·온보드 자율을 결합한 기준 아키텍처', '대형 차량(heavy-vehicle) 제조 현장'으로 고쳤다.",
    "f40 — L. AI·학습 기술 항목에 '실험은 계획 성공률만 측정했고 비용·지연 자체는 측정하지 않았다'는 단서를 붙였다.",
    "f22 — 본문에서 기준일 2021-02-15 를 OpenAPI 3.1.0 에만 붙이고 AsyncAPI 3.1.0 은 '발행일 미확인'으로 썼으며, ref-1024 각주 발행일을 '미확인'으로 두었다.",
    "f37·f38·f21·f54 — ros2_tracing 은 ref-1032 하나로만, 구로병원 논문은 ref-943 하나로만 인용하고 ref-1361·ref-060 은 절에 쓰지 않았다.",
    "f4·f5·f13·f20·f33·f53 — 여섯 문장 모두 '[추정] 벤더 주장[^ref-…]' 형식으로 병기했다(f4 는 판매사 조사를 인용한 기사임을 밝혔다).",
    "범위 경계 문구 — f13(위치 추정)·f41(로봇 내부 계산 배치)은 로봇 자체 지능·제어 경계, f21 은 시설·설비 제어 경계, f19·f20 은 상위 업무 시스템 경계, f48 은 로봇 운영체제·펌웨어 무선 업데이트 연계 대상, f53 은 무선망 구축 연계 대상임을 각 항목에 밝히고, f50 은 '연계 대상:'으로 시작하는 문장으로 두었다.",
    "18·34·36 구분 — f14·f15·f16 은 E. 사물·사람·실시간 상태 항목에서 현재 상태(18. 실시간 세계 상태·데이터 일관성)로, f33 은 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래)으로, f34·f35 는 36. 가상 시운전·실제 상황 재현(지난 기록)으로 나눠 쓰고, 셋을 디지털 트윈이라는 한 이름으로 묶지 않는다는 문장을 I 항목 머리에 두었다.",
    "교차 규칙 — C. 채팅 기반 구성·운영 항목 머리에 12. 채팅으로 업무 지시·오케스트레이션의 엔진이 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링임을 밝히고 G. 계획·최적화 항목과 함께 읽도록 양쪽에 연결했다. L. AI·학습 기술 항목에는 44. 로봇 기반 모델·언어 모델 계획 링크와 적용 대상인 41·42·43 세부영역을 함께 적었다.",
    "'아직 다루지 않은 연결' 목록 — 지시된 31개 세부영역을 대분류별로 번호와 이름으로 적고, P. 거버넌스·법규·사회 연결은 f50 하나(연계 대상 추정)뿐임을 밝혔으며, 완전성 표현은 쓰지 않았다.",
    "Q. 현장 유형별 적용 — f51·f54(및 F 항목의 f21)는 병원(63. 병원·의료), f52 는 제조 공장(62. 제조 공장), f4·f19·f20·f33·f53 은 물류창고(61. 물류창고), f5·f13 은 기타(67. 기타 현장, 기업 사옥)로 현장 유형을 밝히고, f51 은 특정 병원 배치 결과가 아니라 미들웨어 구조라는 단서를 유지했다.",
    "원문 미열람 표기 — 지시된 33개 출처 각주에 접근일 2026-10-09 뒤 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었으며, 원문 텍스트가 입력된 11개 출처(ref-004·009·031·045·051·105·148·251·287·405·762)에는 표기하지 않고 source_unopened: false 로 두었다.",
    "각주 발행일 — ref-1042 2025-06-03, ref-1025 2021-02-15, ref-1034 2023-05-23, ref-943 2026-03-31, ref-1039 2025-08-14, ref-1120 2022-05-13, ref-045 2021-09-30 을 채우고, ref-766 은 제목에 '개인정보보호위원회고시 제2023-6호', 발행일 2023-09-22 로 맞췄다.",
    "f47·f50 — 접속기록 조항은 '2023-09-22 시행 판 고시 제8조 기준, 현행 조문 미확인(oq-214)'으로만 쓰고 보관 기간 수치는 넣지 않았다.",
    "open_question_updates — 새 질문 1은 areas [43, 41, 32] 로 두고 H. 실행·협업·예외 복구 항목에서 oq-048·oq-213 과 함께 연결했고, 새 질문 2는 areas [41, 21] 로 두고 F. 연동 항목에서 oq-209 와 함께 연결했으며, question 문자열에 필드 구분 문자열을 남기지 않았다.",
    "2차: index_updates.home_recent — '41·42·43 세부영역이'를 '41. 플랫폼 아키텍처·외부 API, 42. 분산 시스템·통신·컴퓨팅 구조, 43. 데이터·관측성·배포 세부영역이'로 고쳤다.",
    "2차: additional_research_requests 다섯째 항목 — 번호만 나열한 목록을 빼고 'K. 플랫폼 아키텍처·인프라 대분류 페이지 '다른 대분류와의 연결' 절의 '아직 다루지 않은 연결' 목록'을 가리키게 했으며, '8~11'을 '8. 채팅으로 맵 작성 ~ 11. 채팅으로 실제 상황 시뮬레이션 재현'으로 이름과 함께 썼다.",
    "2차: L. AI·학습 기술 항목 머리 문장의 적용 대상 세 세부영역 이름을 같은 폴더 상대 경로 링크(platform-architecture-and-external-api.md, distributed-systems-communication-and-computing.md, data-observability-and-deployment.md)로 바꿨다.",
    "2차: 약어 첫 등장 풀어 쓰기 — E 항목 f14 문장의 MQTT 를 '메시지 큐잉 원격 측정 전송(Message Queuing Telemetry Transport, MQTT)'으로(유언 표기는 용어집과 같게 '유언 메시지(Last Will)'), A 항목 f2 문장의 SaaS·PaaS 를 '서비스형 소프트웨어(Software as a Service, SaaS)·서비스형 플랫폼(Platform as a Service, PaaS)'으로, H 항목 f29 문장의 UWB 를 '초광대역(Ultra-Wideband, UWB)'으로, N 항목 f46 문장의 DDS 를 '데이터 분산 서비스(Data Distribution Service, DDS)'로 풀어 썼다. 주장·태그·각주는 바꾸지 않았다.",
    "2차: reference_updates 의 ref-766 title 을 각주와 같은 '개인정보의 안전성 확보조치 기준(개인정보보호위원회고시 제2023-6호)'로 맞췄다."
  ]
}
```

### runs/2026-10-09-06/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/platform-architecture-and-infrastructure/index.md (1개 절)
```

### runs/2026-10-09-06/pages/categories/platform-architecture-and-infrastructure/index.md

```markdown
---
title: "K. 플랫폼 아키텍처·인프라"
type: category
status: draft
created: 2026-09-28
updated: 2026-10-09
version: 2
sources: [ref-004, ref-009, ref-031, ref-045, ref-051, ref-105, ref-148, ref-251, ref-282, ref-287, ref-300, ref-304, ref-306, ref-307, ref-308, ref-309, ref-310, ref-374, ref-401, ref-405, ref-493, ref-762, ref-766, ref-831, ref-854, ref-937, ref-943, ref-1023, ref-1024, ref-1025, ref-1030, ref-1031, ref-1032, ref-1033, ref-1034, ref-1036, ref-1037, ref-1039, ref-1040, ref-1041, ref-1042, ref-1043, ref-1044, ref-1120]
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

K. 플랫폼 아키텍처·인프라의 세 세부영역, 곧 [41. 플랫폼 아키텍처·외부 API](platform-architecture-and-external-api.md), [42. 분산 시스템·통신·컴퓨팅 구조](distributed-systems-communication-and-computing.md), [43. 데이터·관측성·배포](data-observability-and-deployment.md)는 다른 대분류의 기능이 어디에서 돌고, 연결이 끊겼을 때 무엇을 이어 가며, 무엇을 기록으로 남기는지를 정한다. 아래 연결은 게시된 세부영역 페이지와 다른 대분류 페이지에 실린 검증된 주장을 대분류별로 묶은 것이다. 근거는 모두 단일 출처이거나 기존 페이지의 재인용이며, 교차 확인된 것은 없다. 두 영역을 잇는 해석은 추정 태그로 표시했고, 제조사·판매사 자료에 기댄 내용에는 벤더 주장을 함께 적었다.

### A. 기획·사업

[A. 기획·사업](../planning-and-business/index.md)과는 비용과 업체 전략에서 만난다.

- **43. 데이터·관측성·배포 ↔ [3. 경제성·조달·사업 모델](../planning-and-business/economics-procurement-and-business-models.md)**: FinOps Foundation 은 클라우드 비용 관리를 알리기(Inform)·최적화(Optimize)·운영(Operate) 단계가 되풀이되는 주기로 설명한다(발행일 미확인, 2026-10-09 확인). [사실][^ref-1041] 같은 재단은 2025-06-03 클라우드 청구 데이터 명세 FOCUS 1.2 를 발표하면서 서비스형 소프트웨어(Software as a Service, SaaS)·서비스형 플랫폼(Platform as a Service, PaaS) 청구 데이터 지원과 청구서 대사(invoice reconciliation)를 더했다고 밝혔다(발표 글 기준이며 명세 본문은 미열람). [사실][^ref-1042] 43. 데이터·관측성·배포가 계측·배분하는 클라우드·언어 모델 호출 비용은 3. 경제성·조달·사업 모델의 총소유비용 산정과 과금 단위 결정의 입력이 될 것으로 보이나, 다중 제조사 오케스트레이션 플랫폼의 과금 단위를 공개한 자료는 확인되지 않았다(oq-267). [추정][^ref-1041][^ref-1042][^ref-1037]
- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ 3. 경제성·조달·사업 모델**: FreightWaves 기사는 하이브리드 창고 관리 시스템(Warehouse Management System, WMS) 판매사의 조사를 인용해 창고 운영 중단 비용이 시간당 최대 10만 달러라고 전하며, 이는 연결 단절이 물류창고 투자 효과 판단에 들어갈 위험 비용이 될 수 있음을 보여 준다(기사 발행일·조사 방법·표본·하한 미확인, 2026-10-09 확인). [추정] 벤더 주장[^ref-309]
- **41. 플랫폼 아키텍처·외부 API ↔ [1. 기술·시장·업체 동향](../planning-and-business/technology-market-and-vendor-trends.md)**: 업체 사례로, 네이버는 제2사옥 1784(기타 현장, 기업 사옥)에서 로봇 100여 대를 클라우드로 제어하고 로봇에는 연산·판단을 싣지 않는 구조를 쓴다고 밝힌다(발행일 미확인, 2026-10-09 확인). [추정] 벤더 주장[^ref-1023]

### B. 로봇 온톨로지

[B. 로봇 온톨로지](../robot-ontology/index.md)와는 어댑터 설정과 버전 기록에서 만난다.

- **41. 플랫폼 아키텍처·외부 API ↔ [6. 온톨로지 기반 시스템·로봇 연동](../robot-ontology/ontology-based-system-and-robot-integration.md)**: Open-RMF 플릿 어댑터 템플릿 설정은 수행 가능한 작업 유형(task_capabilities)과 동작 이름(actions)을 선언한다(발행일 미확인, 2026-10-09 확인). [사실][^ref-105] 41. 플랫폼 아키텍처·외부 API가 ROP 직접 범위로 두는 제조사 어댑터 계층은 6. 온톨로지 기반 시스템·로봇 연동이 능력 모델에서 만드는 어댑터 설정·명령 매핑 초안이 반영되는 자리가 될 것으로 보이나, 그렇게 초안을 만든 공개 사례는 확인되지 않았다. [추정][^ref-004][^ref-105]
- **43. 데이터·관측성·배포 ↔ [7. 온톨로지 검증·변경 관리](../robot-ontology/ontology-verification-and-change-management.md)**: 43. 데이터·관측성·배포가 남기는 소프트웨어·펌웨어 배포 버전 기록은 7. 온톨로지 검증·변경 관리가 능력 정의를 다시 검증할 계기를 알려 주는 입력이 될 것으로 보이나, 두 기록을 잇는 공개 사례는 확인하지 못했다. [추정][^ref-1040]

### C. 채팅 기반 구성·운영

[C. 채팅 기반 구성·운영](../chat-based-configuration-and-operation/index.md)과는 대화가 부르는 외부 API 와 언어 모델 호출 계측에서 만난다. 분류 원문 4장 주석은 업무 지시를 25. 작업 배정 — MRTA와 26. 작업 순서·스케줄링의 기능을 대화로 쓰게 하는 것으로 보므로, 아래 12. 채팅으로 업무 지시·오케스트레이션 연결은 G. 계획·최적화 항목과 함께 읽는다.

- **41. 플랫폼 아키텍처·외부 API ↔ [12. 채팅으로 업무 지시·오케스트레이션](../chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md)**: Open Robotics 상호운용 SIG 의 2026-07-02 발표 안내문(2026-06-25 게시)은 Nayantra 를 소개했다. Nayantra 는 Open-RMF REST 응용 프로그래밍 인터페이스(Application Programming Interface, API)를 언어 모델이 호출하는 도구로 노출하는 모델 컨텍스트 프로토콜(Model Context Protocol, MCP) 서버와, 평이한 영어 지시를 RMF 임무로 바꾸는 에이전트로 이루어진다(안내문 기준이며 발표 내용 자체는 미열람, 시연은 Isaac Sim 창고 시뮬레이션). [사실][^ref-854]
- **41. 플랫폼 아키텍처·외부 API ↔ [13. 대화형 기능의 신뢰·기반](../chat-based-configuration-and-operation/conversational-trust-and-foundations.md)**: 대화형 기능이 플랫폼 외부 API 를 도구로 부르면, API 의 인증·권한 범위가 13. 대화형 기능의 신뢰·기반이 다루는 사용자별 대화 권한의 실제 집행 지점이 될 것으로 보인다(아래 N. 보안·개인정보 항목과 함께 읽는다). [추정][^ref-854][^ref-762]
- **43. 데이터·관측성·배포 ↔ 13. 대화형 기능의 신뢰·기반**: OpenTelemetry 생성형 AI 의미 규약 저장소는 언어 모델 클라이언트 호출의 토큰 사용량 지표를 정의하며, 이 규약은 아직 개발(Development) 단계다(발행일 미확인, 2026-10-09 확인). [사실][^ref-1037] 13. 대화형 기능의 신뢰·기반이 언어 모델 공급자를 고르고 바꾸려면 43. 데이터·관측성·배포가 호출별 토큰·비용·지연을 계측해야 할 것으로 보이나, 계측 지표 이름은 안정 판이 나오지 않아 고정되지 않았다(oq-212). [추정][^ref-1037][^ref-1043]

### D. 공간·지도 모델

- **41. 플랫폼 아키텍처·외부 API ↔ [15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md)** ([D. 공간·지도 모델](../space-and-map-model/index.md)): 네이버는 ARC eye 가 클라우드에서 디지털 트윈 데이터와 측위 AI 로 로봇 위치를 정한다고 밝히지만, 위치 모델을 클라우드에 둔 이 설계에서 연결이 끊기면 로봇이 어디까지 동작하는지는 공개되지 않았다(기타 현장, 기업 사옥, oq-206). [추정] 벤더 주장[^ref-1023] 위치 추정 자체는 분류 원문 19장의 로봇 자체 지능·제어 경계에 속하는 연계 대상이므로, 이 사례는 제품 전략 사례로만 읽고 ROP 직접 범위의 근거로 쓰지 않는다.

### E. 사물·사람·실시간 상태

[E. 사물·사람·실시간 상태](../objects-people-and-live-state/index.md)와의 연결은 지금의 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성 쪽이며, I. 설계·시뮬레이션 항목의 미래 실험·지난 기록 재현과 구분한다.

- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md)**: 통신 계층에는 상태가 오래되었음을 알리는 장치가 있으며, ROS 2 서비스 품질(Quality of Service, QoS)의 기한·생존성 정책, Sparkplug 의 노드 종료(NDEATH) 뒤 지표 STALE 표시, VDA 5050 이 메시지 큐잉 원격 측정 전송(Message Queuing Telemetry Transport, MQTT)의 유언 메시지(Last Will)로 보내는 연결 끊김 통지가 그 예다(세 출처는 각각 한 장치만 다루므로 서로 교차 확인한 것이 아니다, 2026-10-09 확인). [사실][^ref-282][^ref-287][^ref-031] Open-RMF 로봇 상태는 밀리초 단위 유닉스 시각(unix_millis_time)을, VDA 5050 상태는 ISO 8601 형식 시각(timestamp)을 담아 시각 표현이 서로 다르며, 공통 시간축 변환과 허용 시계 오차를 정한 자료는 확인되지 않았다(oq-035). [사실][^ref-148][^ref-051]
- **43. 데이터·관측성·배포 ↔ [17. 작업 대상·자산 식별과 인계 추적](../objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md)·18. 실시간 세계 상태·데이터 일관성**: EPCIS 2.0 온톨로지(2021-09-30)는 발생 시각(eventTime)·기록 시각(recordTime)·UTC 차이를 구분하므로, 실행 기록과 관측 데이터에서도 발생 시각과 수신·기록 시각을 따로 남기는 설계가 두 대분류를 잇는 지점이 될 것으로 보인다. [추정][^ref-045]

### F. 연동

[F. 연동](../integration/index.md)과는 통신 전제, 어댑터 구조, API 명세, 설비·업무 시스템 기록에서 만난다.

- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md)**: VDA 5050(3.0.0 기준)은 연결 실패와 메시지 손실이 있는 무선망을 전제해 주문·상태 토픽에 재전송 없는 MQTT QoS 0 을 쓴다(발행일 미확인, 2026-10-09 확인). [사실][^ref-031]
- **41. 플랫폼 아키텍처·외부 API ↔ 20. 로봇·제조사 관제 연동**: Open-RMF 플릿 어댑터는 로봇의 예상 이동 경로를 시설 전체의 중앙 교통 스케줄에 보고하고, 제조사 관제가 허용하는 제어 수준에 따라 전체 제어·신호등·읽기 전용 가운데 하나로 붙는다(발행일 미확인, 2026-10-09 확인). [사실][^ref-004][^ref-251] 두 자료는 같은 기관 문서라 교차 확인은 아니며, 제어 수준별 교통 성능 차이는 미확인이다(oq-032).
- **41. 플랫폼 아키텍처·외부 API ↔ [21. 상호운용 표준·적합성](../integration/interoperability-standards-and-conformance.md)**: OpenAPI 명세 3.1.0(2021-02-15)은 HTTP API 를 언어와 무관하게 기술하는 표준 인터페이스 기술 형식이고, AsyncAPI 명세 3.1.0(발행일 미확인)은 메시지 기반 API 를 기술하는 형식이다. [사실][^ref-1025][^ref-1024] 플랫폼 외부 API 를 두 형식으로 기계가 읽게 기술하면 21. 상호운용 표준·적합성이 다루는 연동 규격 적합성 시험의 기준 문서가 될 수 있을 것으로 보이나, 국내에 통합관제 플랫폼 외부 API 를 정한 TTA·KS 표준이 있는지는 확인되지 않았다(oq-209). [추정][^ref-1025][^ref-1024] 이런 기술 문서를 실제 적합성 시험에 쓴 공개 도구·절차가 있는지는 oq-209 와 함께 새 열린 질문으로 올렸다.
- **43. 데이터·관측성·배포 ↔ [22. 설비·건물 시스템 연동](../integration/facility-and-building-system-integration.md)**: 고려대학교 구로병원 약품 배송 로봇 실증(병원)은 승강기 호출·탑승·문 동작·하차 시각을 남긴 로봇 시스템 로그, 승강기 상태·문·위치·로봇 명령을 1 Hz 로 남긴 승강기–로봇 통신 로그, 관찰자 기록지를 함께 모아 실패 원인을 분석했다(2026-03-31 게재). [사실][^ref-943] 승강기 통신 로그를 만드는 일은 분류 원문 19장의 시설·설비 제어 경계에 속하는 연계 대상이고, ROP 몫은 그 기록의 수집·결합이다.
- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ [23. 업무 시스템 연동](../integration/business-system-integration.md)**: 물류창고에서 외부망이 끊긴 동안 현장 관제는 이미 받은 주문을 이어 갈 수 있을 것으로 보이나, 클라우드 WMS 의 새 주문 수신과 재고 확정은 멈추고 재연결 뒤 현장 완료 기록과 WMS 기록을 맞추는 절차가 필요할 것으로 보인다(물류센터 운영 기준 미확인, oq-038). [추정][^ref-031][^ref-300][^ref-310] 새 주문과 재고 확정은 분류 원문 19장의 상위 업무 시스템 경계에 속하는 연계 대상이고, ROP 는 받은 요청을 실행하고 결과를 반영하는 쪽을 맡는다.
- **41. 플랫폼 아키텍처·외부 API ↔ 23. 업무 시스템 연동**: Locus Robotics 는 LocusONE 이 WMS 주문을 API 로 받아 로봇 작업으로 내리고 피킹 완료 확인을 WMS 로 즉시 회신한다고 밝힌다(물류창고, 흐름 단계 피킹, 발행일 미확인, 2026-10-09 확인). [추정] 벤더 주장[^ref-1030] 주문 최적화 판단은 상위 업무 시스템 경계의 WMS·로봇 공급사 몫이고, ROP 는 연동 인터페이스만 다룬다.

### G. 계획·최적화

[G. 계획·최적화](../planning-and-optimization/index.md)와는 배정·교통 계산을 어디에 두는지에서 만난다. 위 C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션이 부르는 엔진도 여기의 25. 작업 배정 — MRTA와 [26. 작업 순서·스케줄링](../planning-and-optimization/task-sequencing-and-scheduling.md)이다.

- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ [25. 작업 배정 — MRTA](../planning-and-optimization/task-allocation-mrta.md)**: Lott·Honary(2026-09 프리프린트, 초록 기준)는 분산 작업 배정기 6종(CBAA, ACBBA, PI, HIPC, DMCHBA, DGA)을 패킷 손실·페이딩 같은 통신 저하 조건에서 비교했다. [사실][^ref-493] 배정 계산을 클라우드·현장 서버·로봇 가운데 어디에 둘지가 두 대분류를 잇는 설계 쟁점이 될 것으로 보이나, 통신이 나빠질 때 중앙 방식과 분산 방식 사이를 언제 바꿀지 정한 물류센터 기준은 확인되지 않았다(oq-083). [추정][^ref-493][^ref-401]
- **41. 플랫폼 아키텍처·외부 API·42. 분산 시스템·통신·컴퓨팅 구조 ↔ [27. 다중 로봇 경로·교통 관리 — MAPF](../planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md)**: Open-RMF 교통 관리는 플릿 어댑터가 예상 경로를 중앙 교통 스케줄에 보고하는 구조이므로, 중앙 스케줄을 현장 서버와 클라우드 가운데 어디에 두는지가 단절 때 교통 조율을 계속할 수 있는지를 좌우할 것으로 보인다(실측 자료 없음). [추정][^ref-004]

### H. 실행·협업·예외 복구

[H. 실행·협업·예외 복구](../execution-collaboration-and-recovery/index.md)와는 단절·재시작 뒤 일을 어떻게 이어 가는지에서 만난다.

- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md)**: VDA 5050 3.0.0 에서 로봇은 브로커와 연결이 끊겨도 받은 주문 정보를 유지하고, 마지막으로 해제된 노드까지 주문을 수행한다(발행일 미확인, 2026-10-09 확인). [사실][^ref-031] KubeEdge 는 클라우드–엣지 네트워크가 끊겨도 엣지 노드와 애플리케이션이 자율적으로 계속 동작하는 구조를 둔다(발행일 미확인, 2026-10-09 확인). [사실][^ref-300]
- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ [29. 명령·작업 실행의 신뢰성](../execution-collaboration-and-recovery/command-and-task-execution-reliability.md)**: VDA 5050 은 주문·상태를 QoS 0 으로 보내고 상태를 사건 발생 시와 최대 30초 간격으로 다시 보내므로, 재연결 뒤 관제는 끊긴 동안의 메시지가 쌓여 오기를 기대하기보다 다음 상태 메시지로 로봇 상태를 다시 세우고 주문을 갱신해야 할 것으로 보인다(VDA 5050 이 MQTT 5.0 세션 만료를 어떻게 쓰는지는 미확인). [추정][^ref-031][^ref-306]
- **43. 데이터·관측성·배포 ↔ 32. 예외 복구·재계획·업무 연속성**: Zhang·Yu·Westerlund(Sensors, 2025-08-14)는 Kubernetes 컨테이너 자동 재시작으로 ROS 2 다중 로봇 시스템이 장애 중에도 초광대역(Ultra-Wideband, UWB) 기반 상대 위치 정확도를 유지했다고 보고했으며, 이는 현장 적용 사례가 아니라 실험실 결과다. [사실][^ref-1039] Open-RMF 저장소 이슈 #224 는 플릿 어댑터가 재시작되면 배정된 작업이 사라진다고 지적하지만, 이번 확인에서는 이슈 원문을 다시 열지 못해 이슈가 언급한 복구 기능 제안의 내용과 현재 배포판 반영 여부를 재확인하지 못했다(oq-048). [추정][^ref-374]
- **41. 플랫폼 아키텍처·외부 API ↔ 32. 예외 복구·재계획·업무 연속성**: FogROS2-FT(IROS 2024, 초록 기준)는 클라우드 로보틱스의 장애 허용을 다루며, 독립적인 상태 비저장(stateless) 로봇 서비스를 여러 클라우드에 복제하고 먼저 온 응답을 쓴다. [사실][^ref-1031] 대상이 상태 비저장 서비스이므로, 이 방식을 진행 중인 작업 상태를 보존하는 근거로 읽지 않는다. 플랫폼 서비스를 복제하거나 자동 재시작하면서 진행 중인 작업 상태를 잃지 않은 공개 사례가 있는지는 새 열린 질문으로 올렸고, 어댑터 복구의 배포판 반영(oq-048)·무중단 순차 배포(oq-213)와 함께 본다.

### I. 설계·시뮬레이션

[I. 설계·시뮬레이션](../design-and-simulation/index.md)과의 연결은 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈과 지난 기록을 재현하는 36. 가상 시운전·실제 상황 재현으로 나뉜다. 위 E. 사물·사람·실시간 상태의 현재 상태 표현과 함께 셋을 디지털 트윈이라는 한 이름으로 묶지 않는다.

- **43. 데이터·관측성·배포 ↔ [34. 시뮬레이션·예측용 디지털 트윈](../design-and-simulation/simulation-and-predictive-digital-twin.md)**: Ocado 는 교통 관리·오케스트레이션 알고리즘 변경을 실제 창고(물류창고)에 적용하기 전에 시뮬레이션·디지털 트윈에서 시험하고, 12개월 동안 창고 운영 270년 분량을 시뮬레이션했다고 밝힌다(2025-06-04). [추정] 벤더 주장[^ref-1044] 이 사례는 43. 데이터·관측성·배포 쪽에서는 배포 전 검증의 근거로만 쓰고, 시뮬레이션 자체는 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈의 내용으로 둔다.
- **43. 데이터·관측성·배포 ↔ [36. 가상 시운전·실제 상황 재현](../design-and-simulation/virtual-commissioning-and-real-situation-replay.md)**: ROS 2 Iron Irwini(2023-05-23)부터 rosbag2 의 기본 저장 형식은 MCAP 이고, rosbag2 는 재생 속도 조절, /clock 발행, 여러 백 파일을 기록 시각순으로 동시에 재생하는 기능을 지원한다(두 출처는 서로 다른 내용을 말하므로 교차 확인이 아니다). [사실][^ref-1034][^ref-831] 43. 데이터·관측성·배포가 정하는 기록 형식과 보존 기간이 36. 가상 시운전·실제 상황 재현이 재현에 쓸 수 있는 실제 기록의 범위를 정할 것으로 보이며, 이 연결은 지난 기록을 다루는 것이라 18. 실시간 세계 상태·데이터 일관성의 현재 상태 표현과는 구분된다(oq-211). [추정][^ref-1034][^ref-831]

### J. 현장 운영·관제

[J. 현장 운영·관제](../field-operations-and-monitoring/index.md)와는 실행 기록 저장과 원인 분석용 추적에서 만난다.

- **43. 데이터·관측성·배포 ↔ [37. 관제 화면·실행 기록](../field-operations-and-monitoring/control-screen-and-execution-records.md)**: Open-RMF 웹 대시보드의 API 서버(rmf-server)는 기본으로 메모리 안의 SQLite 를 쓰고 PostgreSQL·SQLite·MySQL·MariaDB 를 지원하므로, 실행 기록을 영속 저장하는 것은 배포 설정의 몫이다(발행일 미확인, 2026-10-09 확인). [사실][^ref-762]
- **43. 데이터·관측성·배포 ↔ [38. 모니터링·이상 탐지·원인 분석](../field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md)**: ros2_tracing(IEEE RA-L, 2022-07)은 LTTng 기반 저부하 추적기로 ROS 2 실행 정보를 모으며, 모든 ROS 2 계측을 켰을 때 메시지 종단 지연 증가가 평균 0.0033 ms 였다고 보고했다(저자 실험값, 독립 재현 미확인). [사실][^ref-1032] ros2probe(2026-06 프리프린트)는 관찰 도구가 관찰 대상을 교란하는 문제를 커널 선택 관찰로 줄여, 관찰 자체의 비용을 따져야 함을 보여 준다. [사실][^ref-1033] 플랫폼 서비스 쪽 분산 추적(OpenTelemetry)과 ROS 2 런타임 쪽 추적(ros2_tracing)은 서로 다른 계층의 실행 정보를 모으므로, 지연 원인 분석에 두 계층을 함께 쓰려면 작업 식별자로 기록을 잇는 관측성 설계가 필요할 것으로 보인다(공개 사례 미확인, oq-210). [추정][^ref-1036][^ref-1032]

### L. AI·학습 기술

[L. AI·학습 기술](../ai-and-learning/index.md)과는 언어 모델·계산을 어디에서 돌리는지에서 만난다. 적용 대상은 이 대분류의 [41. 플랫폼 아키텍처·외부 API](platform-architecture-and-external-api.md), [42. 분산 시스템·통신·컴퓨팅 구조](distributed-systems-communication-and-computing.md), [43. 데이터·관측성·배포](data-observability-and-deployment.md)다.

- **42. 분산 시스템·통신·컴퓨팅 구조·43. 데이터·관측성·배포 ↔ [44. 로봇 기반 모델·언어 모델 계획](../ai-and-learning/robot-foundation-models-and-llm-planning.md)**: Bruno·Sim·Hagiwara(2026-09 프리프린트)는 범용 서비스 로봇의 대규모 언어 모델(Large Language Model, LLM) 연쇄 기반 작업 계획에서 로컬 모델과 클라우드 모델을 비교했고 비교의 동기는 클라우드 API 비용과 지연이었으나, 실험은 계획 성공률만 측정했고 비용·지연 자체는 측정하지 않았다. [사실][^ref-1043]
- **41. 플랫폼 아키텍처·외부 API ↔ 44. 로봇 기반 모델·언어 모델 계획**: FogROS2(2022-05)는 ROS 2 로봇의 계산 부담이 큰 작업을 클라우드·포그로 옮겨 실행하는 플랫폼이다. [사실][^ref-304] 로봇 내부 기능의 실행 위치 선택은 분류 원문 19장의 로봇 자체 지능·제어 경계에 속하는 연계 대상이므로, 이 연구는 계산 배치 선택지의 연구 근거로만 쓴다.

### M. 안전

[M. 안전](../safety/index.md)은 통신 계층과 안전 기능의 구분, 사고 조사용 기록에서 이 대분류와 만난다.

- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ [48. 안전·위험 관리](../safety/safety-and-risk-management.md)**: VDA 5050 은 이 문서가 기능·운영·시스템 안전 요구를 정하지 않으며 안전 표준으로 적용해서는 안 된다고 밝힌다(발행일 미확인, 2026-10-09 확인). [사실][^ref-031] 그래서 관제 통신 계층과 48. 안전·위험 관리가 다루는 안전 기능은 구분해 다룬다.
- **43. 데이터·관측성·배포 ↔ [50. 안전 표준·인증·사고 조사](../safety/safety-standards-certification-and-incident-investigation.md)**: Winfield 외(2022-05-13)의 윤리적 블랙박스 초안 공개 표준은 사고·아차 사고 조사를 돕기 위해 소셜 로봇의 센서·구동기·제어 결정 데이터를 기록하는 모듈을 제안하며, 단일 로봇을 대상으로 하고 플릿·플랫폼 수준 기록은 다루지 않는다. [사실][^ref-1120] 사고 조사에 쓸 플랫폼 수준 실행 기록에는 43. 데이터·관측성·배포 쪽의 보존 기간·무결성 관리가 필요할 것으로 보이나, 로봇 플랫폼 기록의 보존 기간을 정한 기준은 개인정보 접속기록 규정 밖에서는 확인되지 않았다(oq-211). [추정][^ref-1120][^ref-766]

### N. 보안·개인정보

[N. 보안·개인정보](../security-and-privacy/index.md)는 외부 API 인증·통신 보호·접속기록에서 이 대분류와 만난다.

- **41. 플랫폼 아키텍처·외부 API ↔ [51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md)**: Open-RMF API 서버(rmf-server)는 OpenID Connect(OIDC) 신원 공급자로 인증하고 권한은 앱 안에서 역할·동작·자원 권한 그룹으로 판정하며, 관리자는 모든 그룹에서 모든 동작을 할 수 있고 현재 모든 자원은 빈 문자열 기본 그룹에 들어간다(발행일 미확인, 2026-10-09 확인). [사실][^ref-762]
- **42. 분산 시스템·통신·컴퓨팅 구조 ↔ 51. 인증·권한·격리·[52. 통신 보호·위협 관리·감사](../security-and-privacy/communication-protection-threat-management-and-audit.md)**: ROS 2 는 데이터 분산 서비스(Data Distribution Service, DDS) 보안 규격의 인증(공개 키 기반 구조, PKI)·접근통제(거버넌스·권한 파일)·암호화 플러그인을 쓰고, Open-RMF 문서는 SROS 2 인클레이브로 RMF 구성요소의 권한을 나누고 웹 대시보드에는 전송 계층 보안(Transport Layer Security, TLS)·OIDC 인증을 더한다고 설명한다(두 자료는 서로 다른 계층을 설명하므로 교차 확인이 아니다). [사실][^ref-009][^ref-405]
- **43. 데이터·관측성·배포 ↔ [53. 개인정보·영상 데이터](../security-and-privacy/privacy-and-video-data.md)**: 개인정보보호위원회 고시 「개인정보의 안전성 확보조치 기준」은 접속기록의 보관과 점검에 관한 조항을 둔다(2023-09-22 시행 판 고시 제8조 기준, 현행 조문 미확인, oq-214). [사실][^ref-766]

### O. 검증·도입·수명주기

- **43. 데이터·관측성·배포 ↔ [57. 자산·소프트웨어 수명주기 관리](../verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md)** ([O. 검증·도입·수명주기](../verification-deployment-and-lifecycle/index.md)): Mender 는 임베디드 리눅스 장치용 오픈소스 무선(Over-the-Air, OTA) 업데이트 도구로, 이미지 기반 A/B 업데이트와 실패 시 롤백을 지원한다(발행일 미확인, 2026-10-09 확인). [사실][^ref-1040] 로봇 운영체제·펌웨어의 무선 업데이트 자체는 연계 대상이다. 43. 데이터·관측성·배포의 배포·롤백 자동화가 57. 자산·소프트웨어 수명주기 관리의 버전 관리와 맞물릴 것으로 보이나, 운행 중인 로봇 작업을 끊지 않고 현장 서버·로봇에 순차 배포하고 되돌리는 시점·기준을 공개한 로봇 관제 제품이나 연구는 확인되지 않았다(oq-213). [추정][^ref-1040][^ref-1039]

### P. 거버넌스·법규·사회

- **43. 데이터·관측성·배포 ↔ [59. 법·규제·보험·라이선스](../governance-law-and-society/law-regulation-insurance-and-licensing.md)** ([P. 거버넌스·법규·사회](../governance-law-and-society/index.md)): 연계 대상: 접속기록 보관 같은 법적 의무의 해석과 적용 판단은 59. 법·규제·보험·라이선스와 운영 사업자의 몫으로 보이고, ROP 는 그 기준에 맞춰 기록을 수집·보존·점검하는 기능을 제공하는 쪽으로 보인다(근거 고시는 2023-09-22 시행 판 제8조 기준, 현행 조문 미확인, oq-214). [추정][^ref-766]

P. 거버넌스·법규·사회와의 연결은 현재 위의 연계 대상 추정 하나뿐이다.

### Q. 현장 유형별 적용

[Q. 현장 유형별 적용](../site-type-applications/index.md)에는 현장마다 다른 요구를 모으고, 모든 현장에 공통인 구조 선택은 이 대분류에 둔다. 아래는 위 연결의 근거가 된 사례를 현장 유형별로 다시 묶은 것이다.

- **병원 — [63. 병원·의료](../site-type-applications/hospital-and-healthcare.md) ↔ 41. 플랫폼 아키텍처·외부 API**: 창이종합병원 CHART 의 공공 의료기관용 로봇 미들웨어 RoMi-H 는 기계(하드웨어 추상화)·제어(항법·위치 추정)·중앙(플릿 관리, 로봇–기반 시설 통신)·통합(모바일·웹 앱·ICT 시스템용 API) 네 영역이 역할을 나누는 구조이며 OMG DDS 를 쓴다(2019-10-31 ROSCon 2019 에서 공식 출범). [사실][^ref-937] 이는 특정 병원의 배치 결과가 아니라 미들웨어 구조다.
- **병원 — 63. 병원·의료 ↔ 42. 분산 시스템·통신·컴퓨팅 구조·43. 데이터·관측성·배포**: 고려대학교 구로병원 약품 배송 로봇 실증(2025-06, 비응급 임무 122건)의 실패 14건은 승강기 막힘 8건, 복도 주행 4건, 통신 오류 2건이었다(2026-03-31 게재). [사실][^ref-943] 논문이 밝힌 전체 성공률과 이 건수가 맞지 않는 문제는 oq-215 에 있고, 이 실증의 로그 결합은 위 F. 연동 항목에 있다.
- **제조 공장 — [62. 제조 공장](../site-type-applications/manufacturing-plant.md) ↔ 41. 플랫폼 아키텍처·외부 API**: Brorsson 외(2025-12, 초록 기준)는 기반 시설 센싱·현장(on-premise) 클라우드 컴퓨팅·온보드 자율을 결합한 사내 물류 이동 로봇 기준 아키텍처를 제시하고, 대형 차량(heavy-vehicle) 제조 현장 실배치로 보였다. [사실][^ref-308] 처리량·시간·비용 수치는 확인하지 못했다.
- **물류창고 — [61. 물류창고](../site-type-applications/warehouse.md) ↔ 42. 분산 시스템·통신·컴퓨팅 구조**: CJ대한통운은 2023-04 이천 2풀필먼트센터에 물류센터 최초로 5G 특화망 이음5G 를 구축했다고 발표하며 기존 와이파이의 채널 간섭·지연을 생산성 저하 원인으로 들었고, 발표 당시 로봇·설비 적용은 시범 뒤 확대 계획이었다. [추정] 벤더 주장[^ref-307] 무선망 구축은 ROP 가 소유하지 않는 통신 기반으로 연계 대상이다. 물류창고의 다른 근거는 위 A. 기획·사업(운영 중단 비용), F. 연동(단절 중 WMS 연동, 피킹 완료 회신), I. 설계·시뮬레이션(배포 전 시뮬레이션) 항목에 있다.
- **기타 — [67. 기타 현장](../site-type-applications/other-sites.md) ↔ 41. 플랫폼 아키텍처·외부 API**: 기업 사옥 사례(네이버 1784)는 위 A. 기획·사업과 D. 공간·지도 모델 항목에 벤더 주장으로 있다.
- **상업 시설·가정·실외**: [64. 상업 시설](../site-type-applications/commercial-facilities.md), [65. 가정·공동주택](../site-type-applications/home-and-apartment.md), [66. 실외](../site-type-applications/outdoor.md)와 이 대분류를 잇는 근거는 이번 정리에 없다.

### 아직 다루지 않은 연결

이번 정리의 근거가 다루지 않은 세부영역은 다음과 같다. 연결이 없다는 뜻이 아니라 아직 근거를 모으지 않았다는 뜻이다.

- A. 기획·사업: 2. 사용 사례·요구·책임 범위
- B. 로봇 온톨로지: 4. 이기종 로봇 등록, 5. 로봇 능력·작업 표현
- C. 채팅 기반 구성·운영: 8. 채팅으로 맵 작성, 9. 채팅으로 시나리오 구성, 10. 채팅으로 로봇 구성, 11. 채팅으로 실제 상황 시뮬레이션 재현
- D. 공간·지도 모델: 14. 도면·BIM에서 지도 만들기, 16. 장소 의미·지도 관리
- E. 사물·사람·실시간 상태: 19. 사람·보행자 모델
- G. 계획·최적화: 24. 작업·워크플로 모델링, 26. 작업 순서·스케줄링, 28. 공용 자원·충전·에너지 최적화
- H. 실행·협업·예외 복구: 30. 로봇 간 협업·물리적 인계, 31. 사람–로봇 협업
- I. 설계·시뮬레이션: 33. 시나리오 모델·편집, 35. 처리능력·규모·배치 설계
- J. 현장 운영·관제: 39. 운영 성과 측정·개선, 40. 운영 절차·요청 창구
- L. AI·학습 기술: 45. 문서·도면·장면 이해, 46. 예측·학습 기반 최적화, 47. AI·학습·적응과 모델 운영
- M. 안전: 49. 사람 근접 안전
- O. 검증·도입·수명주기: 54. 시험·형식 검증·벤치마크, 55. 현장 조사·설치·시운전, 56. 운영 이관·확대·교육
- P. 거버넌스·법규·사회: 58. 다사업자 책임·계약·데이터, 60. 노동·수용성·접근성
- Q. 현장 유형별 적용: 64. 상업 시설, 65. 가정·공동주택, 66. 실외

[^ref-004]: Open Robotics, RMF Core Overview — Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/rmf-core.html, 접근일 2026-10-09
[^ref-009]: ROS 2 Design, ROS 2 DDS-Security Integration, 미확인, https://design.ros2.org/articles/ros2_dds_security.html, 접근일 2026-10-09
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-09
[^ref-045]: GS1, gs1/EPCIS — Ontology/EPCIS.ttl (EPCIS ontology 2.0), 2021-09-30, https://github.com/gs1/EPCIS/blob/master/Ontology/EPCIS.ttl, 접근일 2026-10-09
[^ref-051]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/state.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema, 접근일 2026-10-09
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-10-09
[^ref-148]: Open Robotics (open-rmf), rmf_api_msgs — rmf_api_msgs/schemas/robot_state.json, 미확인, https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/robot_state.json, 접근일 2026-10-09
[^ref-251]: Open Robotics, Mobile Robot Fleets (integration_fleets) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets.html, 접근일 2026-10-09
[^ref-282]: Open Robotics (ROS 2 Documentation), Quality of Service settings — ROS 2 Documentation: Jazzy, 미확인, https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html, 접근일 2026-10-09 (원문 미열람)
[^ref-287]: Eclipse Foundation (eclipse-sparkplug GitHub), Sparkplug Specification — Chapter 5 Operational Behavior (Sparkplug_5_Operational_Behavior.adoc), 미확인, https://github.com/eclipse-sparkplug/sparkplug/blob/master/specification/src/main/asciidoc/chapters/Sparkplug_5_Operational_Behavior.adoc, 접근일 2026-10-09
[^ref-300]: KubeEdge (CNCF, kubeedge GitHub), KubeEdge — README, 미확인, https://github.com/kubeedge/kubeedge, 접근일 2026-10-09 (원문 미열람)
[^ref-304]: Ichnowski, J., Chen, K. 외(UC Berkeley AUTOLAB), FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2, 2022-05, https://arxiv.org/abs/2205.09778, 접근일 2026-10-09 (원문 미열람)
[^ref-306]: OASIS, MQTT Version 5.0, 2019-03, https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html, 접근일 2026-10-09 (원문 미열람)
[^ref-307]: CJ대한통운, CJ대한통운, 물류센터 최초 5G 개통 … 속도 1000배 빨라진다, 2023-04, https://www.cjlogistics.com/ko/newsroom/news/NR_00001046, 접근일 2026-10-09 (원문 미열람)
[^ref-308]: Brorsson, E. 외, Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives, 2025-12, https://arxiv.org/abs/2512.15215, 접근일 2026-10-09 (원문 미열람)
[^ref-309]: FreightWaves, Warehouses face $100K-hour downtime risk as cloud outages mount, 미확인, https://www.freightwaves.com/news/warehouses-face-100k-hour-downtime-risk-hybrid-wms, 접근일 2026-10-09 (원문 미열람)
[^ref-310]: Gilbert, S., & Lynch, N., Brewer's conjecture and the feasibility of consistent, available, partition-tolerant web services, 2002-06, https://dl.acm.org/doi/10.1145/564585.564601, 접근일 2026-10-09 (원문 미열람)
[^ref-374]: Open Robotics (open-rmf/rmf_ros2 GitHub), Task recovery when fleet adapter get restarted · Issue #224 · open-rmf/rmf_ros2, 미확인, https://github.com/open-rmf/rmf_ros2/issues/224, 접근일 2026-10-09 (원문 미열람)
[^ref-401]: KISTI ScienceON 수록 국가R&D 과제 보고서(수행기관 미확인), 클라우드에 연결된 개별 로봇 및 로봇그룹의 작업 계획 기술 개발, 미확인, https://scienceon.kisti.re.kr/srch/selectPORSrchReport.do?cn=TRKO202400003952, 접근일 2026-10-09 (원문 미열람)
[^ref-405]: Open Robotics, Security - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/security.html, 접근일 2026-10-09
[^ref-493]: Lott, J., & Honary, V.(University of San Diego), Decentralized Multi-Robot Task Allocation Under Degraded Communication: A Benchmark of Performance, Reliability, and Computation, 2026-09, https://arxiv.org/abs/2609.13711, 접근일 2026-10-09 (원문 미열람)
[^ref-762]: Open Robotics (open-rmf), rmf-web — packages/api-server/README.md, 미확인, https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md, 접근일 2026-10-09
[^ref-766]: 국가법령정보센터(개인정보보호위원회 고시), 개인정보의 안전성 확보조치 기준(개인정보보호위원회고시 제2023-6호), 2023-09-22, https://www.law.go.kr/admRulLsInfoP.do?chrClsCd=010202&admRulSeq=2100000229672, 접근일 2026-10-09 (원문 미열람)
[^ref-831]: ROS 2 (ros2/rosbag2 GitHub), rosbag2 — README (Recording and playback of ROS 2 communications), 미확인, https://github.com/ros2/rosbag2, 접근일 2026-10-09 (원문 미열람)
[^ref-854]: Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse, Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP), 2026-06-25, https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687, 접근일 2026-10-09 (원문 미열람)
[^ref-937]: Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART), ROMI-H | Changi General Hospital, 미확인, https://www.cgh.com.sg/chart/projects/romi-h, 접근일 2026-10-09 (원문 미열람)
[^ref-943]: Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-10-09 (원문 미열람)
[^ref-1023]: NAVER Corp., 로보틱스 l NAVER Corp., 미확인, https://www.navercorp.com/tech/robotics, 접근일 2026-10-09 (원문 미열람)
[^ref-1024]: AsyncAPI Initiative, AsyncAPI Specification 3.1.0, 미확인, https://www.asyncapi.com/docs/reference/specification/v3.1.0, 접근일 2026-10-09 (원문 미열람)
[^ref-1025]: OpenAPI Initiative, OpenAPI Specification v3.1.0, 2021-02-15, https://spec.openapis.org/oas/v3.1.0, 접근일 2026-10-09 (원문 미열람)
[^ref-1030]: Locus Robotics, Seamless Integrations with LocusOne Robotics, 미확인, https://locusrobotics.com/locusone/automated-warehouse-software/integrations, 접근일 2026-10-09 (원문 미열람)
[^ref-1031]: Chen, K., Hari, K., Chung, T. 외 (IROS 2024, arXiv), FogROS2-FT: Fault Tolerant Cloud Robotics, 2024-12, https://arxiv.org/abs/2412.05408, 접근일 2026-10-09 (원문 미열람)
[^ref-1032]: Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L, arXiv), ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2, 2022-07, https://arxiv.org/abs/2201.00393, 접근일 2026-10-09 (원문 미열람)
[^ref-1033]: Yu, J., Lee, S., Choi, Y., & Park, K.-J. (arXiv), ros2probe: Non-intrusive, Kernel-selective Observability for Robot Operating System 2 Middleware, 2026-06, https://arxiv.org/abs/2606.10746, 접근일 2026-10-09 (원문 미열람)
[^ref-1034]: Open Robotics (ROS 2 Documentation), Iron Irwini (iron), 2023-05-23, https://docs.ros.org/en/rolling/Releases/Release-Iron-Irwini.html, 접근일 2026-10-09 (원문 미열람)
[^ref-1036]: OpenTelemetry (CNCF), Specification Status Summary, 미확인, https://opentelemetry.io/docs/specs/status/, 접근일 2026-10-09 (원문 미열람)
[^ref-1037]: OpenTelemetry (open-telemetry/semantic-conventions-genai), semantic-conventions-genai/docs/gen-ai/gen-ai-token-metrics.md, 미확인, https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md, 접근일 2026-10-09 (원문 미열람)
[^ref-1039]: Zhang, J., Yu, X., & Westerlund, T. (Sensors 25(16):5067), Enhancing the Resilience of ROS 2-Based Multi-Robot Systems with Kubernetes: A Case Study on UWB-Based Relative Positioning, 2025-08-14, https://pmc.ncbi.nlm.nih.gov/articles/PMC12390455/, 접근일 2026-10-09 (원문 미열람)
[^ref-1040]: Northern.tech (mendersoftware), mender — README, 미확인, https://github.com/mendersoftware/mender, 접근일 2026-10-09 (원문 미열람)
[^ref-1041]: FinOps Foundation, FinOps Phases, 미확인, https://www.finops.org/framework/phases/, 접근일 2026-10-09 (원문 미열람)
[^ref-1042]: FinOps Foundation, Introducing FOCUS 1.2: SaaS/PaaS Support, Invoice Reconciliation, and more, 2025-06-03, https://www.finops.org/insights/focus-1-2-available/, 접근일 2026-10-09 (원문 미열람)
[^ref-1043]: Bruno, L. D. M., Sim, J., & Hagiwara, Y. (arXiv), Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots, 2026-09, https://arxiv.org/abs/2609.29043, 접근일 2026-10-09 (원문 미열람)
[^ref-1044]: Ocado Group, Ocado's digital twins and simulations: driving efficiencies and innovation at scale, 2025-06-04, https://www.ocadogroup.com/newsroom/stories/digital-twins-and-simulations, 접근일 2026-10-09 (원문 미열람)
[^ref-1120]: Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv), An Ethical Black Box for Social Robots: a draft Open Standard, 2022-05-13, https://arxiv.org/abs/2205.06564, 접근일 2026-10-09 (원문 미열람)

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

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 43건 / 전체 1248건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

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

### docs/glossary/index.md (요약: 용어 351개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- runtime-tracing: 런타임 추적 (Runtime Tracing (ros2_tracing))
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

### docs/open-questions.md (요약: 대상 영역 [41, 42, 43] 에 걸린 17건 / 전체 299건)

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
- oq-297 [열림] VDA 5050 의 지도 배포(downloadMap·enableMap·deleteMap)로 로봇마다 활성화된 지도 판과 Open-RMF 빌딩 맵·LIF 레이아웃의 판을 ROP 한 곳에서 대응시켜 관리하는 공개 구현이나 운영 절차가 있는가? (영역 16, 43, 57)
```

### runs/2026-10-09-06/verification2.json

```json
{
  "run_id": "2026-10-09-06",
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
    "overlaps": []
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
    "index_updates.home_recent: '41·42·43 세부영역이' 를 '41. 플랫폼 아키텍처·외부 API, 42. 분산 시스템·통신·컴퓨팅 구조, 43. 데이터·관측성·배포 세부영역이' 로 고친다 — 공통 규칙 6절은 JSON 문자열 안에서도 세부영역을 번호만으로 부르지 못하게 하고, 이 문자열은 홈 페이지 최근 업데이트에 그대로 게시된다.",
    "additional_research_requests 다섯째 항목: '(2·4·5·8~11·14·16·…·64~66번 세부영역, 이름은 페이지 참조)' 처럼 번호만 나열한 부분을 번호와 이름을 함께 쓴 목록으로 바꾸거나, 번호 목록을 빼고 'K. 플랫폼 아키텍처·인프라 대분류 페이지의 아직 다루지 않은 연결 목록' 으로 가리키게 고친다. 같은 항목의 '8~11' 도 '8. 채팅으로 맵 작성 ~ 11. 채팅으로 실제 상황 시뮬레이션 재현' 처럼 이름을 함께 쓴다 — 공통 규칙 6절(번호만 쓰는 호칭 금지).",
    "'다른 대분류와의 연결' 절의 L. AI·학습 기술 항목 머리 문장('적용 대상은 이 대분류의 41. 플랫폼 아키텍처·외부 API, 42. 분산 시스템·통신·컴퓨팅 구조, 43. 데이터·관측성·배포다')에서 세 세부영역 이름을 같은 폴더의 상대 경로 링크(platform-architecture-and-external-api.md, distributed-systems-communication-and-computing.md, data-observability-and-deployment.md)로 바꾼다 — 1차 수정 지시 12항이 44. 로봇 기반 모델·언어 모델 계획 링크와 적용 대상 세부영역 링크를 함께 두라고 했는데 L 항목에는 44 링크만 있다(공통 규칙 5).",
    "약어 첫 등장 풀어 쓰기: E. 사물·사람·실시간 상태 항목 f14 문장의 MQTT 를 용어집 표기대로 '메시지 큐잉 원격 측정 전송(Message Queuing Telemetry Transport, MQTT)' 으로, A. 기획·사업 항목 f2 문장의 SaaS·PaaS, H. 실행·협업·예외 복구 항목 f29 문장의 UWB, N. 보안·개인정보 항목 f46 문장의 DDS 를 첫 등장에서 풀어 쓴다 — 공통 규칙 6절(약어는 첫 등장 시 풀어 쓴다). 문장의 주장·태그·각주는 바꾸지 않는다.",
    "reference_updates 의 ref-766 title 을 페이지 각주와 같은 '개인정보의 안전성 확보조치 기준(개인정보보호위원회고시 제2023-6호)' 로 맞춘다 — 1차 수정 지시 16항에 따라 각주 정의만 고치고 참고문헌 갱신 항목은 옛 제목으로 남아 참고문헌 페이지의 '각주 형식' 줄과 이 절의 각주가 어긋나게 된다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 52건, 미확인 2건(f21·f30), 교차 확인 0건. 강등: f21 사실 → 추정(1 Hz 를 로봇 시스템 로그에 잘못 붙임 — 원문대로 승강기–로봇 통신 로그로 정정하면 사실 유지 가능), f30 사실 → 추정(ref-374 를 이번에 열지 못했고 SQLite 백업 제안 부분 미확인). 원문 미열람 출처: ref-282, ref-300, ref-304, ref-306, ref-307, ref-308, ref-309, ref-310, ref-374, ref-401, ref-493, ref-766, ref-831, ref-854, ref-937, ref-943, ref-1023, ref-1024, ref-1025, ref-1030, ref-1031, ref-1032, ref-1033, ref-1034, ref-1036, ref-1037, ref-1039, ref-1040, ref-1041, ref-1042, ref-1043, ref-1044, ref-1120(브리프 기준). 이 가운데 검증 중 ref-282·ref-300·ref-304·ref-308·ref-493·ref-831·ref-854·ref-937·ref-943·ref-1024·ref-1025·ref-1031·ref-1032·ref-1033·ref-1034·ref-1037·ref-1039·ref-1040·ref-1041·ref-1042·ref-1043·ref-1120 은 원문·초록을 열어 해당 진술을 확인했고, ref-766 은 검색 결과로만 확인했으며, ref-306·ref-307·ref-309·ref-310·ref-374·ref-401·ref-1023·ref-1030·ref-1036·ref-1044 는 열지 않았다. 주의: 이 절의 연결은 모두 단일 출처이거나 게시된 세부영역·대분류 페이지의 재인용이고, 연결 해석 22건은 [추정]이다. 벤더 주장 6건(f4·f5·f13·f20·f33·f53)은 독립 확인되지 않았다. 상업 시설·가정·실외 현장 근거가 없다. 게시된 43. 데이터·관측성·배포 5절에도 f21 과 같은 1 Hz 귀속 오류가 있어 다음 갱신 실행에서 정정이 필요하다. ros2_tracing 이 ref-1032·ref-1361 로, 구로병원 논문이 ref-943·ref-060 으로 참고문헌에 이중 등록돼 있다. 구로병원 논문의 성공률 87.03% 는 실패 14건/122건(약 88.5%)과 맞지 않는다(oq-215). 정정 요청 없음. / 2차 수정 후 재검증. 드리프트 없음(태그가 붙은 문장 모두 f1~f54 와 1차 처분에 대응하고, 덧붙은 문장은 1차 검증 메모·분류 원문 19장에서 온 단서·연결 문장이다), [분류원문] 보존, 섹션 순서 준수, 링크 유효(형식 검증 통과). 1차 수정 지시 18건 가운데 17건은 이행을 확인했다: 절 제목, f21 정정 뒤 [사실] 유지(1차 지시가 허용한 조건), f30 [추정] 강등과 SQLite 제안 삭제, f31 상태 비저장 범위, f52 초록 표현, f40 측정 단서, f22 발행일 분리, ref-1032·ref-943 단일 인용, 벤더 주장 6건 병기, 범위 경계 문구, 18·34·36 구분, 아직 다루지 않은 세부영역 31개, 현장 유형 명시, 원문 미열람 표기 33건, 각주 발행일, f47·f50 조문 표기, 새 열린 질문 2건. L. AI·학습 기술 항목의 적용 대상 세부영역 링크만 빠졌다. 남은 수정은 이 링크, 홈 최근 업데이트 문자열과 추가 조사 요청의 번호만 쓴 호칭, 약어 첫 등장 풀어 쓰기(MQTT·SaaS·PaaS·UWB·DDS), ref-766 참고문헌 제목 맞추기다. 사소한 의견: 본문의 'MQTT 유언(Last Will)' 과 용어집 새 항목 'MQTT 유언 메시지' 의 표기가 조금 다르다. 26. 작업 순서·스케줄링은 G 항목 머리 문장에 엔진으로 링크되면서 '아직 다루지 않은 연결' 목록에도 있다(1차 지시대로이며 근거 finding 이 없다는 뜻이다). 이번 2차 검증에서는 도구를 쓰지 않았다.",
  "retry_reason": null
}
```
