(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-25-64
- date: 2026-09-25
- run_type: area_deep_dive (영역 심화)
- 대상: 26. 사이버보안·접근권한·개인정보 (G. 안전·보안·지능·거버넌스)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: false · fetch_mode: mirror_only (일반 웹 페이지 열람은 네트워크 정책으로 막혀 있다. raw.githubusercontent.com 은 열린다: 공식 문서가 GitHub 에 있는 출처는 입력의 config/source_mirrors.yaml 경로를 WebFetch 로 열어 원문을 읽고 sources[].fetched=true, fetched_via=github_raw, fetch_url 을 적는다. 입력에 원문 텍스트(data/source_texts)가 있는 출처는 fetched_via=inbox. 그 밖의 출처는 fetched=false 이며 코드가 신뢰도 상한(medium)을 강제한다 — 공통 규칙 0절 6항)
- 언어: ko
- verification_stage: first
- verifier_budget:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2

## 입력

### runs/2026-09-25-64/target.json

```json
{
  "run_id": "2026-09-25-64",
  "date": "2026-09-25",
  "weekday": "Fri",
  "run_number": 64,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 26,
    "area_name": "26. 사이버보안·접근권한·개인정보",
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=26"
}
```

### runs/2026-09-25-64/research.json

```json
{
  "run_id": "2026-09-25-64",
  "date": "2026-09-25",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 26,
    "area_name": "26. 사이버보안·접근권한·개인정보",
    "category": "G. 안전·보안·지능·거버넌스"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음(인증·접근 제어·인클레이브·보안 구역과 도관·이동형 영상정보처리기기)",
    "섹션 5. 현장 시나리오 비어 있음(물류 흐름 단계 명시 필요)",
    "섹션 6. 대표 접근법과 기술 비어 있음(SROS 2 권한, MQTT 접근 제어, 대시보드 역할 인증, 인증서 교체)",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 비어 있음",
    "섹션 11. 열린 질문 비어 있음(대상 영역에 걸린 열린 질문 oq-043, oq-056, oq-082 반영 필요)"
  ],
  "research_questions": [
    "외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가? [분류원문]",
    "ROS 2(SROS 2), Open-RMF, VDA 5050, MQTT 브로커는 장비 인증·통신 보호·명령 권한을 어떤 구조로 제공하거나 구현자에게 맡기는가? (섹션 4·6·7 겨냥)",
    "산업 보안 표준·규제(IEC 62443, NIST SP 800-82, ISO 10218-1:2025, EU 기계 규정, EU 사이버 복원력법)는 로봇·관제 시스템에 무엇을 요구하는가? (섹션 3·7 겨냥)",
    "물류 로봇·관제 소프트웨어에서 공개된 실제 취약점 사례는 무엇이며 어떤 영향을 보고했는가? (섹션 3·8 겨냥)",
    "로봇 카메라 영상과 작업자 데이터 보호에 적용되는 한국 법규·가이드(개인정보 보호법 이동형 영상정보처리기기, 근로자 감시 설비, KISA 로봇 보안 자료)는 무엇인가? (섹션 5·9 겨냥, 한국 자료 우선)",
    "대상 영역 열린 질문 oq-043(출입통제 연동 권한), oq-056(SROS 2 인클레이브 단위), oq-082(관제 보고값 위조 검증)에 답할 근거가 있는가? (섹션 10·11 겨냥)",
    "고객별 격리와 원격 접속 중개 가운데 ROP가 직접 맡을 부분과 제조사·IT 조직에 맡길 부분은 어떻게 나뉘는가? (섹션 9 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "ROS 2 보안은 DDS-Security 의 다섯 플러그인 가운데 인증·접근 제어·암호 세 가지만 쓰며, 참여자마다 도메인 보호 방식을 정한 서명된 거버넌스 파일과 참여자 권한을 담은 서명된 권한 파일을 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-009"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "인증 플러그인은 PKI 로 참여자 신원을 확인하고, 접근 제어 플러그인은 참여자의 DDS 기능 제한을 정의·집행한다. 권한 파일은 \"A signed XML document containing the permissions of the domain participant\". 로깅·데이터 태깅은 규격 준수에 필요하지 않아 쓰지 않는다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "SROS 2 접근 제어 정책은 XML 로 인클레이브·프로파일·권한 규칙을 계층적으로 적고, 토픽(발행·구독)·서비스(요청·응답)·액션(호출·실행)마다 허용·거부를 명시하며, 거부가 같은 대상의 허용보다 우선하고 XSLT 로 DDS 권한 파일로 변환된다.",
      "tag": "사실",
      "source_ids": [
        "ref-610"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"privileges must be explicitly qualified as allowed\"; 거부된 권한은 같은 범위의 허용 권한을 누른다. 변환 과정은 XInclude 확장 → 스키마 검증 → 프로파일별 가지치기 → XSLT 변환이며, 권한은 거부 우선으로 정렬된다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "제약"
    },
    {
      "id": "f3",
      "claim": "SROS 2 인클레이브는 인증서·키·거버넌스·권한 파일을 묶은 하나의 보안 신원이며, 한 컨텍스트를 공유하는 노드들은 한 인클레이브의 권한으로 합쳐지고, 인클레이브를 적용하는 범위는 운영체제 프로세스·사용자·장치·군집 단위로 고를 수 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-611"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "DDS Security 1.1 에서 참여자는 보안 신원 하나만 쓸 수 있어 같은 컨텍스트의 노드 권한이 한 인클레이브로 통합된다. 배포 시 인클레이브 적용 범위를 조절해 모델 충실도를 정한다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "Open-RMF 보안 구성은 ROS 2 부분을 SROS 2(키스토어·인클레이브·서명된 권한)로 보호하고, 웹 대시보드는 TLS 와 Keycloak 기반 OpenID Connect 사용자 인증으로 보호하며, API 서버가 역할마다 보안이 적용된 ROS 2 노드를 하나씩 두고 사용자의 ID 토큰에 따라 접근을 준다.",
      "tag": "사실",
      "source_ids": [
        "ref-612"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"The api server runs a secured ROS 2 node per each role and provides access to them based on the id token of each user.\" 키스토어의 private 디렉터리(CA 키)는 배포 전에 제거한다. generate_policy·generate_artifacts 도구로 정책과 산출물을 만든다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f5",
      "claim": "ROS 2 로봇 시스템 위협 모델(초안)은 보안이 꺼져 있으면 어떤 노드든 어떤 토픽에나 발행할 수 있어 구성요소 신원 위조·명령 가로채기가 가능하고, 기본 자격증명의 SSH 같은 원격 접속이 권한 상승 경로가 되며, 카메라 영상·로그가 보호해야 할 민감 자산이고 빌드 팜·서드파티 구성요소를 통한 공급망 위협이 있다고 정리한다.",
      "tag": "사실",
      "source_ids": [
        "ref-010"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "TurtleBot 3·MARA 를 예로 든 초안 문서. 보안 미적용 시 \"any node can publish to any topic\". 완화책: SROS 활성화, 권한 파일, TPM 에 자격증명 보관, 바이너리 서명, 설정 변경·자격증명 사용 감사. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f6",
      "claim": "VDA 5050 3.0.0 명세는 보안 통신·데이터 보호의 메커니즘을 규정하지 않고 MQTT 프로토콜 보안을 브로커 설정에 맡기며, 운영자·시스템 통합자·차량 제조사·플릿 제어 제공자 사이의 안전·보안 책임도 배분하지 않는다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"Cybersecurity Measures: Mechanisms, technologies, or processes for secure communication or data protection are not specified.\" 프로토콜 보안은 브로커 설정에서 고려해야 하나 이 지침은 다루지 않는다. 데이터 보호 요구도 없다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "VDA 5050 3.0.0 의 즉시 동작 updateCertificate 는 서비스(MQTT)와 로봇별 개인 키·공개 인증서(선택적으로 루트 인증서)의 내려받기 링크를 받아 인증서를 설치·활성화하며, 명령 발신자를 검증할 수 없으므로 내려받기도 TLS 로 보호하고 활성화 전 인증서 체인을 확인하도록 권고한다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "매개변수 service, keyDownloadLink, certificateDownloadLink, certificateAuthorityDownloadLink(선택). 상태 RUNNING(내려받기·설치 중) → FINISHED(활성) 또는 FAILED. 체인 검증 권고. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "VDA 5050 3.0.0 에서 RELEASE 유형 구역은 플릿 제어가 진입을 허가한 뒤에만 로봇이 들어갈 수 있고, 로봇은 requestType ACCESS 인 zoneRequest 로 허가를 요청해 responses 토픽으로 승인을 받는다.",
      "tag": "사실",
      "source_ids": [
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "RELEASE 구역: 로봇은 플릿 제어로부터 접근 허가를 받은 뒤에만 진입할 수 있다. 요청은 zoneRequest(requestType ACCESS), 승인은 responses 토픽. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "제약"
    },
    {
      "id": "f9",
      "claim": "Eclipse Mosquitto MQTT 브로커는 ACL 파일로 토픽마다 read·write·readwrite·deny 접근을 정하고 pattern 규칙에서 클라이언트 id(%c)·사용자 이름(%u)을 치환할 수 있으며, require_certificate 와 use_identity_as_username 을 함께 켜면 클라이언트 인증서의 일반 이름(CN)을 접근 제어용 사용자 이름으로 쓴다.",
      "tag": "사실",
      "source_ids": [
        "ref-613"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "형식 topic [read|write|readwrite|deny] <topic>, pattern ... 에서 %c·%u 치환. require_certificate 가 참이면 유효한 인증서가 있어야 접속되고, use_identity_as_username 이면 인증서 CN 이 사용자 이름이 된다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "제약"
    },
    {
      "id": "f10",
      "claim": "VDA 5050 이 보안을 브로커 설정에 맡기므로, 로봇별 인증서(updateCertificate)의 CN 을 사용자 이름으로 쓰고 제조사·일련번호가 들어간 토픽 경로에 pattern ACL 을 걸면 로봇마다 자기 토픽만 읽고 쓰게 제한하는 구성이 가능해 보이나, 이를 규정한 공개 표준 구성은 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-613"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f6·f7·f9 의 조합에서 도출한 구성안이며 원문이 직접 권고한 것은 아니다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "제약"
    },
    {
      "id": "f11",
      "claim": "IEC 62443-3-3 은 IEC 62443-1-1 의 7개 기본 요구(식별·인증 제어, 사용 제어, 시스템 무결성, 데이터 기밀성, 데이터 흐름 제한, 사건 적시 대응, 자원 가용성)에 딸린 제어 시스템 기술 요구와 제어 시스템 능력 보안 수준을 정의한다.",
      "tag": "사실",
      "source_ids": [
        "ref-617"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원문 미열람. 판매 목록 소개: IEC 62443-3-3:2013 채택판(2013-08 초판)으로, 7개 기본 요구에 연관된 시스템 요구와 보안 수준을 정의한다. 보안 수준은 1~4 로 엄격해진다(검색 요약 기준).",
      "as_of": "2013-08",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f12",
      "claim": "IEC 62443 의 보안 구역(zone)은 기능·논리·물리적 관계에 따라 묶여 공통 보안 요구를 공유하는 시스템·구성요소 집합이고, 도관(conduit)은 두 개 이상의 구역을 잇는 통신 채널의 묶음으로 구역 경계에서 통신을 제한·여과하는 역할을 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-618"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원문 미열람. 구역과 도관 개념을 다룬 논문의 검색 요약: 위험 평가에 따라 IACS 부분마다 보안 수준이 다를 수 있고, 구역 간 통신은 도관을 통한다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f13",
      "claim": "MiR 는 자사 AMR 이 암호화 통신·접근 제어·보안 부팅을 쓰고 MiR Fleet Enterprise 가 IEC 62443-4-2(SL-C 3)에 맞춰 설계됐다고 밝힌다.",
      "tag": "추정",
      "source_ids": [
        "ref-619"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: MiR Fleet Enterprise is built to align with IEC 62443 Part 4-2 (SL-C 3). 독립 인증 문서는 확인하지 못했다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true,
      "vendor_claim": true
    },
    {
      "id": "f14",
      "claim": "미국 CISA 의 ICS 권고 ICSA-21-280-02 는 Alias Robotics 가 보고한 MiR 차량·MiR Fleet 소프트웨어의 복수 취약점(부적절한 접근 제어, 중요 기능 인증 누락, 민감 데이터 암호화 누락 등)을 공지했고, 악용되면 권한 상승·데이터 유출·로봇 제어·서비스 거부가 가능하다고 했다.",
      "tag": "사실",
      "source_ids": [
        "ref-616"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원문 미열람. 검색 요약: 취약점 유형은 improper access control, missing authentication for critical function, missing encryption of sensitive data 등이며 영향은 privilege escalation, data exfiltration, control of the robot, DoS. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "예외·성과",
      "source_unopened": true
    },
    {
      "id": "f15",
      "claim": "2025년 개정 ISO 10218-1 은 산업용 로봇 안전에 적용되는 범위에서 사이버보안 요구를 포함한다.",
      "tag": "사실",
      "source_ids": [
        "ref-614"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원문 미열람. 검색 요약: The 2025 revision of ISO 10218-1 includes requirements for cybersecurity to the extent that it applies to industrial robot safety. 조항 내용은 미확인. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f16",
      "claim": "EU 기계 규정 (EU) 2023/1230 은 부속서 III 1.1.9 에서 기계의 안전 기능이 우발적·악의적 손상(corruption)으로부터 보호되도록 설계할 것을 요구하며, 이 규정은 2027-01-20 부터 적용된다.",
      "tag": "사실",
      "source_ids": [
        "ref-759"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원문 미열람. 검색 요약: 안전 관련 제어 시스템·소프트웨어는 우발적 고장과 의도적 사이버 공격 모두에 대해 보호되어야 한다(Annex III 1.1.9). 적용일은 이전 브리프 값 (재인용: 2026-09-25-61)",
      "as_of": "2023-06",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f17",
      "claim": "EU 사이버 복원력법(Cyber Resilience Act)은 다른 기기·네트워크와 데이터 연결이 있는 하드웨어·소프트웨어 '디지털 요소가 있는 제품'에 적용되며, 제14조 보고 의무는 2026-09-11 부터, 필수 사이버보안 요구·취약점 처리 등 나머지 주요 의무는 2027-12-11 부터 적용된다.",
      "tag": "사실",
      "source_ids": [
        "ref-624"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원문 미열람. 검색 요약: reporting obligations set out in Article 14 apply from 11 September 2026; 나머지 의무는 11 December 2027 부터. 보고 의무는 이미 시장에 나온 제품에도 적용된다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f18",
      "claim": "NIST SP 800-82 Rev. 3(2023-09)은 제목을 운영 기술(OT) 보안 지침으로 바꾸고 범위를 건물 자동화·물리적 출입통제·산업용 IoT 로 넓혔으며, NIST SP 800-53 Rev. 5 통제 목록에 대한 OT 오버레이를 제공한다.",
      "tag": "사실",
      "source_ids": [
        "ref-615"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원문 미열람. 검색 요약: OT 개요·위협·취약점과 권장 대응책, 위험 관리·접근 제어·사고 대응·네트워크 분할(구역·DMZ)·원격 접속 패턴을 다룬다.",
      "as_of": "2023-09",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f19",
      "claim": "개인정보 보호법 제25조의2는 업무 목적으로 이동형 영상정보처리기기를 운영하는 자가 공개된 장소에서 사람 또는 관련 사물의 영상을 촬영하는 것을 원칙적으로 제한하되, 촬영 사실을 명확히 표시해 정보주체가 거부하지 않은 경우 등을 허용하고, 촬영 시 불빛·소리·안내판 등으로 촬영 사실을 알리도록 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-620"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원문 미열람. 검색 요약: 목욕실·화장실 등 사생활 침해 우려가 큰 장소 촬영 금지, 제15조제1항 해당 또는 촬영 사실 표시 후 거부 의사가 없는 경우 등 허용, 대통령령에 따라 불빛·소리·안내판 등으로 표시. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f20",
      "claim": "개인정보보호위원회의 '이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서'는 자율주행차·배달로봇 등이 촬영 영상을 AI 개발에 쓰려면 기기 외부에 촬영 사실을 표시하고, 공개된 장소의 불특정 다수 영상은 원칙적으로 가명처리 후 활용하며, 원본 활용은 규제샌드박스 실증특례로 안전조치를 지킬 때만 가능하다고 안내한다.",
      "tag": "사실",
      "source_ids": [
        "ref-621"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원문 미열람. 검색 요약: 차량이나 로봇 외부에 촬영 사실과 구체적 내용 표시, 얼굴 모자이크 등 가명처리 후 활용, 원본은 실증특례 조건부. 안내서 발행일은 미확인. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f21",
      "claim": "근로자참여 및 협력증진에 관한 법률은 '사업장 내 근로자 감시 설비의 설치'를 노사협의회의 협의 사항으로 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-622"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원문 미열람. 검색 요약: 제20조 제1항 제14호 '사업장 내 근로자 감시 설비의 설치'가 노사협의회 협의 사항이다. 조항 번호는 판에 따라 다를 수 있어 원문 확인 필요. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "제약",
      "source_unopened": true
    },
    {
      "id": "f22",
      "claim": "한국인터넷진흥원(KISA)은 지식플랫폼에 '로봇 보안취약점 점검 체크리스트 해설서'를 게시해 로봇 보안 취약점 점검 항목을 안내한다.",
      "tag": "사실",
      "source_ids": [
        "ref-623"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원문 미열람. 검색 결과로 게시물 존재와 제목만 확인했다. 항목 수·범주는 검색 요약끼리 달라 넣지 않았다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": true
    },
    {
      "id": "f23",
      "claim": "분류 원문 질문 '외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가?'에 대해, 확인한 자료로는 사용자 역할(OIDC ID 토큰의 역할), ROS 2 인클레이브별 토픽·서비스·액션 허용·거부, MQTT 클라이언트별 토픽 ACL 의 세 층에서 권한을 표현할 수 있으나, 로봇·명령 단위 유지보수 권한 매트릭스를 규정한 공개 표준은 찾지 못했고 VDA 5050 은 이를 구현자에게 맡긴다.",
      "tag": "추정",
      "source_ids": [
        "ref-612",
        "ref-610",
        "ref-613",
        "ref-031"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f2·f4·f6·f9 를 종합한 이 위키의 판단이다. 부재는 검색 범위의 관찰이다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f24",
      "claim": "출하 마감 시간대에 제조사 원격 유지보수 엔지니어가 로봇 한 대의 진단 접속을 요청하면, 기본 자격증명·인증 없는 원격 접속이 권한 상승·로봇 제어로 이어질 수 있으므로 ROP 는 대상 로봇·진단 명령만 허용하고 이동 명령은 막으며 세션을 감사 기록으로 남기는 제약이 필요해 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-010",
        "ref-616",
        "ref-612"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f5(원격 접속 위협)·f14(실제 취약점 영향)·f4(역할 기반 접근)에서 도출한 시나리오다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": "출하",
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f25",
      "claim": "입고 도크에서 카메라를 단 AMR 이 작업자를 촬영하는 경우, 물류센터 내부가 개인정보 보호법 제25조의2의 '공개된 장소'인지는 불분명하고 근로자 감시 설비로서 노사협의회 협의 대상이 될 수 있어, 영상 수집·보관·학습 활용 조건이 입고 작업의 제약으로 작용할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-620",
        "ref-622",
        "ref-010"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f19·f21 의 규정과 f5(카메라 영상은 민감 자산)를 물류 현장에 적용한 추정이며 공식 해석은 확인하지 못했다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": "입고",
      "flow_item": "제약",
      "source_unopened": false
    },
    {
      "id": "f26",
      "claim": "ROP 가 직접 맡을 보안 몫은 누가 어느 로봇·설비에 어떤 명령을 내릴 수 있는지의 권한 정책, 외부 유지보수 접속의 중개·감사 기록, 고객별 작업·데이터 격리, 영상 데이터 접근 정책, 로봇 인증서 교체(updateCertificate) 같은 보안 명령의 조율로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-612",
        "ref-010"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "분류 원문 9장의 경계(로봇 자체 제어는 제조사, ROP 는 인터페이스와 실행 보장)에 f4·f6·f7 을 대입한 추정이다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f27",
      "claim": "연계 대상: 로봇 내부 보안(보안 부팅, 펌웨어 서명, 자격증명 보관, 안전 PLC 설정 보호)과 로봇 안전 기능의 사이버보안 설계는 제조사 몫이고, 네트워크 분할 장비·사용자 신원 제공자는 현장 IT·OT 조직 몫이며, ROP 는 그 결과와 인터페이스를 받아 쓰는 쪽으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-010",
        "ref-616",
        "ref-614"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f5(TPM·바이너리 서명 완화책), f14(제조사 제품 취약점), f15(로봇 안전 표준의 사이버보안 요구)를 경계 판단에 쓴 추정이다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f28",
      "claim": "26. 사이버보안·접근권한·개인정보는 로봇 안전 기능의 사이버보안(25. 안전·위험 관리), 규격이 비워 둔 보안 책임 배분(28. 표준·상호운용성·다사업자 거버넌스), 운영자 역할 인증(18. 사람–로봇 협업·운영 인터페이스), 영상의 AI 학습 활용(27. AI·학습·적응과 모델 운영)과 맞물리는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-614",
        "ref-031",
        "ref-612",
        "ref-621"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f15·f6·f4·f20 을 연결 근거로 쓴 추정. 10. 설비·건물 시스템 연동(oq-043·oq-056), 13. 작업 배정 — MRTA(oq-082), 24. 자산·소프트웨어 수명주기 관리(패치)와의 연결은 기존 열린 질문·페이지에 근거. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": null,
      "source_unopened": false
    },
    {
      "id": "f29",
      "claim": "확인한 VDA 5050·SROS 2·Open-RMF 문서는 고객(화주)별 작업·데이터 격리를 규정하지 않아, 공유 창고에서 고객별 격리는 인클레이브 범위나 대시보드 역할 같은 일반 수단을 ROP 가 조합해 설계해야 할 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-031",
        "ref-611",
        "ref-612"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "세 문서를 읽은 범위에서 테넌트·고객 격리 개념을 찾지 못했다는 관찰이며 부재 확인은 아니다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "제약"
    },
    {
      "id": "f30",
      "claim": "oq-082 와 관련해, DDS 인증은 메시지를 보낸 참여자의 신원을 확인해 구성요소 위조를 막지만 위치·배터리 같은 보고값 내용의 참·거짓은 검증하지 않으므로, 오염된 보고값 검증은 인증과 별도의 타당성 검사가 필요해 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-009",
        "ref-010"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1(인증은 신원 확인)과 f5(신원 위조 위협)에서 도출. 보고값 타당성 검사 기준을 다룬 공개 자료는 이번에 확인하지 못했다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-25",
      "flow_step": null,
      "flow_item": "예외·성과"
    }
  ],
  "sources": [
    {
      "id": "ref-009",
      "org": "Open Robotics (ROS 2 Design)",
      "title": "ROS 2 DDS-Security integration",
      "published": null,
      "url": "https://design.ros2.org/articles/ros2_dds_security.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "ROS 2 가 쓰는 DDS-Security 플러그인(인증·접근 제어·암호)과 서명된 거버넌스·권한 파일 구조.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/ros2/design/gh-pages/articles/180_ros2_dds_security.md",
      "source_unopened": false
    },
    {
      "id": "ref-010",
      "org": "Open Robotics (ROS 2 Design)",
      "title": "ROS 2 Robotic Systems Threat Model",
      "published": null,
      "url": "https://design.ros2.org/articles/ros2_threat_model.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "ROS 2 로봇 시스템 위협 모델 초안. 통신 위조, 물리 접근, 공급망, 데이터 프라이버시, 원격 접속 위협과 완화책.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/ros2/design/gh-pages/articles/183_ros2_threat_model.md",
      "source_unopened": false
    },
    {
      "id": "ref-031",
      "org": "VDA / VDMA (VDA5050 GitHub)",
      "title": "VDA5050/VDA5050 — VDA5050_EN.md (VDA 5050 Version 3.0.0)",
      "published": null,
      "url": "https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "VDA 5050 3.0.0 명세 원문. 이번 실행에서는 보안 범위 제외 문구, updateCertificate 즉시 동작, RELEASE 구역 접근 허가를 확인했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/VDA5050/VDA5050/main/VDA5050_EN.md",
      "source_unopened": false
    },
    {
      "id": "ref-759",
      "org": "European Union (EUR-Lex)",
      "title": "Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery",
      "published": "2023-06",
      "url": "https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. EU 기계 규정. 2027-01-20 적용, 부속서 III 1.1.9 손상(corruption)으로부터의 보호 요구.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-610",
      "org": "Open Robotics (ROS 2 Design)",
      "title": "ROS 2 Access Control Policies",
      "published": null,
      "url": "https://design.ros2.org/articles/ros2_access_control_policies.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "SROS 2 접근 제어 정책의 XML 구조(인클레이브·프로파일·권한), 토픽·서비스·액션별 허용·거부와 DDS 권한 파일로의 변환 과정.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/ros2/design/gh-pages/articles/181_ros2_access_control_policies.md",
      "source_unopened": false
    },
    {
      "id": "ref-611",
      "org": "Open Robotics (ROS 2 Design)",
      "title": "ROS 2 Security Enclaves",
      "published": null,
      "url": "https://design.ros2.org/articles/ros2_security_enclaves.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "SROS 2 인클레이브의 정의와 컨텍스트·프로세스와의 대응, 인클레이브 적용 범위 선택 근거.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/ros2/design/gh-pages/articles/182_ros2_security_enclaves.md",
      "source_unopened": false
    },
    {
      "id": "ref-612",
      "org": "Open Robotics (osrf/ros2multirobotbook)",
      "title": "Programming Multiple Robots with ROS 2 — Security",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/security.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "Open-RMF 보안 구성: SROS 2 키스토어·인클레이브·권한 생성 도구, 대시보드의 TLS·Keycloak OIDC 인증과 역할별 보안 노드.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/security.md",
      "source_unopened": false
    },
    {
      "id": "ref-613",
      "org": "Eclipse Foundation (Eclipse Mosquitto)",
      "title": "mosquitto.conf man page",
      "published": null,
      "url": "https://mosquitto.org/man/mosquitto-conf-5.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "Mosquitto 브로커 설정 문서. ACL 파일의 토픽별 접근·pattern 치환(%c, %u), 인증서 기반 인증(require_certificate, use_identity_as_username). 공식 저장소의 man 페이지 원본(XML)으로 읽었다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/eclipse-mosquitto/mosquitto/master/man/mosquitto.conf.5.xml",
      "source_unopened": false
    },
    {
      "id": "ref-614",
      "org": "Association for Advancing Automation (A3)",
      "title": "Updated ISO 10218 | Answers to Frequently Asked Questions (FAQs)",
      "published": null,
      "url": "https://www.automate.org/robotics/blogs/updated-iso-10218-faq",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. ISO 10218 2025 개정 FAQ. 로봇 안전에 적용되는 범위의 사이버보안 요구 포함을 설명.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-615",
      "org": "NIST",
      "title": "NIST SP 800-82 Rev. 3, Guide to Operational Technology (OT) Security",
      "published": "2023-09",
      "url": "https://csrc.nist.gov/pubs/sp/800/82/r3/final",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. OT 보안 지침 3판. 범위를 건물 자동화·물리적 출입통제·산업용 IoT 로 넓히고 SP 800-53 Rev. 5 OT 오버레이 제공.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-616",
      "org": "CISA",
      "title": "Mobile Industrial Robots Vehicles and MiR Fleet Software (ICSA-21-280-02)",
      "published": null,
      "url": "https://www.cisa.gov/news-events/ics-advisories/icsa-21-280-02",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. MiR 차량·MiR Fleet 소프트웨어 복수 취약점에 대한 미국 CISA ICS 권고.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-617",
      "org": "CSA / IEC (ANSI Webstore)",
      "title": "CAN/CSA IEC 62443-3-3-2017 - Industrial communication networks - Network and system security - Part 3-3: System security requirements and security levels (Adopted IEC 62443-3-3:2013, first edition, 2013-08)",
      "published": "2013-08",
      "url": "https://webstore.ansi.org/standards/csa/csaiec624432017-2442576",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. IEC 62443-3-3 의 판매 목록 소개. 7개 기본 요구에 연관된 시스템 보안 요구와 보안 수준.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-618",
      "org": "MDPI (Journal of Cybersecurity and Privacy)",
      "title": "Security Aspects of Zones and Conduits in IEC 62443",
      "published": null,
      "url": "https://www.mdpi.com/2624-800X/6/2/52",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. IEC 62443 의 보안 구역과 도관 개념의 보안 측면을 다룬 논문.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-619",
      "org": "Mobile Industrial Robots (MiR)",
      "title": "AMRs and Cybersecurity | Secure Robotics at MiR",
      "published": null,
      "url": "https://mobile-industrial-robots.com/blog/amrs-and-cybersecurity",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. MiR 의 AMR 보안 소개 글. MiR Fleet Enterprise 의 IEC 62443-4-2 정렬 주장.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-620",
      "org": "법제처 국가법령정보센터",
      "title": "개인정보 보호법",
      "published": null,
      "url": "https://www.law.go.kr/lsEfInfoP.do?lsiSeq=195062",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 개인정보 보호법 본문. 제25조의2 이동형 영상정보처리기기의 운영 제한.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-621",
      "org": "김·장 법률사무소",
      "title": "'이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서' 관련 인사이트",
      "published": null,
      "url": "https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=30477",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 개인정보보호위원회 이동형 영상정보처리기기 안내서의 촬영 표시·가명처리·원본 활용 기준 해설.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-622",
      "org": "법제처 국가법령정보센터",
      "title": "근로자참여 및 협력증진에 관한 법률",
      "published": null,
      "url": "https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=105636",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. 노사협의회 협의 사항에 '사업장 내 근로자 감시 설비의 설치'를 두는 법률.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-623",
      "org": "한국인터넷진흥원(KISA)",
      "title": "로봇 보안취약점 점검 체크리스트 해설서",
      "published": null,
      "url": "https://kisa.or.kr/2060205/form?lang_type=KO&page=&postSeq=36",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. KISA 지식플랫폼의 로봇 보안취약점 점검 체크리스트 해설서 게시물.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-624",
      "org": "European Commission (Shaping Europe's digital future)",
      "title": "The Cyber Resilience Act - Summary of the legislative text",
      "published": null,
      "url": "https://digital-strategy.ec.europa.eu/en/policies/cra-summary",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-25",
      "summary": "원문 미열람. EU 사이버 복원력법 요약. 적용 대상과 보고 의무(2026-09-11)·주요 의무(2027-12-11) 적용일.",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md",
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
      "rationale": "seed 페이지 3~11절 첫 작성. 3절 왜 중요한가: f14(실제 AMR 취약점과 영향), f15·f16·f17(로봇 안전·기계·제품 규제가 사이버보안을 요구), f5(위협 모델) / 4절 핵심 개념: f1(인증·접근 제어·권한 파일), f3(인클레이브), f11(62443 기본 요구·보안 수준), f12(구역·도관), f19(이동형 영상정보처리기기) / 5절 현장 시나리오: f24(출하·제약, 원격 유지보수), f25(입고·제약, 카메라 영상과 작업자) / 6절 대표 접근법: f2(SROS 2 권한), f4(Open-RMF 역할 인증), f7(인증서 교체), f8(RELEASE 구역 허가), f9·f10(MQTT ACL), f13(벤더 주장 병기) / 7절 표준·오픈소스: f6(VDA 5050 보안 범위 제외), f11·f12, f15~f18, f19~f22(한국 법규·KISA) / 8절 대표 연구와 자료: f5, f14, f18, f22 / 9절 경계: f26(ROP 직접), f27('연계 대상'), f23(분류 원문 질문 — 추정) / 10절 연결: f28(25. 안전·위험 관리, 28. 표준·상호운용성·다사업자 거버넌스, 18. 사람–로봇 협업·운영 인터페이스, 27. AI·학습·적응과 모델 운영), f30(13. 작업 배정 — MRTA, oq-082), 기존 oq-043·oq-056(10. 설비·건물 시스템 연동) / 11절: 기존 oq-043·oq-056·oq-082 와 open_questions_new 4건, f29(고객별 격리)."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "보안 구역과 도관",
      "term_en": "Zones and Conduits (IEC 62443)",
      "definition": "공통 보안 요구를 공유하는 시스템 묶음(구역)과 구역 사이 통신 채널 묶음(도관)으로 산업 제어 시스템을 나눠 보호하는 IEC 62443 의 구조다."
    },
    {
      "term_ko": "보안 수준",
      "term_en": "Security Level (SL, IEC 62443)",
      "definition": "IEC 62443 에서 우발적 위반(SL 1)부터 자원을 갖춘 숙련 공격자(SL 4)까지 막아야 할 위협 수준에 따라 요구의 엄격함을 나눈 등급이다."
    },
    {
      "term_ko": "권한 파일",
      "term_en": "Permissions File (DDS-Security)",
      "definition": "DDS 참여자가 어떤 토픽을 발행·구독할 수 있는지 등 권한을 적고 권한 인증기관이 서명한 XML 문서다."
    },
    {
      "term_ko": "이동형 영상정보처리기기",
      "term_en": "Mobile Video Information Processing Device",
      "definition": "사람이 몸에 착용하거나 이동 가능한 물체에 부착해 영상을 촬영하는 장치로, 개인정보 보호법 제25조의2가 업무 목적 운영을 제한한다."
    }
  ],
  "open_questions_new": [
    "물류센터 내부처럼 공개되지 않은 작업장에서 카메라를 단 로봇이 작업자를 촬영할 때 개인정보 보호법 제25조의2와 근로자 감시 설비 협의 가운데 무엇이 적용되는지 공식 해석이 있는가? | 관련 영역: 26. 사이버보안·접근권한·개인정보, 18. 사람–로봇 협업·운영 인터페이스 | 근거: f25 | 종류: 일반",
    "외부 유지보수 계정의 권한을 로봇·명령 단위로 나눈 매트릭스(예: 진단은 허용, 이동은 불허)를 공개한 로봇 관제·ROP 구성이나 표준이 있는가? | 관련 영역: 26. 사이버보안·접근권한·개인정보, 9. 로봇·제조사 관제 연동 | 근거: f23 | 종류: 일반",
    "여러 화주가 로봇 플릿을 공유하는 창고에서 고객별 작업·데이터 격리를 오케스트레이션 수준에서 규정한 표준이나 공개 설계가 있는가? | 관련 영역: 26. 사이버보안·접근권한·개인정보, 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f29 | 종류: 일반",
    "ISO 10218-1:2025 의 사이버보안 요구는 어느 조항에서 무엇(접근 제한·원격 접속·로그 등)을 요구하며 로봇 관제 연동에 어떤 조건을 주는가? | 관련 영역: 26. 사이버보안·접근권한·개인정보, 25. 안전·위험 관리 | 근거: f15 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 19,
    "cross_checked_count": 0,
    "unverified": [
      "모든 finding 교차 확인 없음(단일 출처 또는 이 위키의 종합)",
      "f11 IEC 62443-3-3 은 판매 목록 소개만 확인, 표준 원문 미열람",
      "f14 CISA 권고 발행일·영향 제품 판 미확인(검색 요약 기준)",
      "f15 ISO 10218-1:2025 사이버보안 조항 내용 미확인",
      "f19 제25조의2 시행일 미확인",
      "f20 안내서 발행일 미확인(법률사무소 해설 경유)",
      "f21 근로자참여법 조항 번호는 판에 따라 다를 수 있음",
      "f22 KISA 해설서의 항목 수·범주는 검색 요약끼리 달라 넣지 않음",
      "oq-043·oq-056·oq-082 는 부분 근거만 확보(f3·f30)해 해결 제안하지 않음",
      "CISA 원격 접속 지침(2023·2025)은 문서 귀속을 확인하지 못해 넣지 않음"
    ],
    "scope_violations": [
      "f27: 로봇 내부 보안·안전 PLC·네트워크 장비는 분류 원문 9장 '로봇 자체 지능·제어'·'시설·설비 제어' 쪽이라 '연계 대상:'으로 표시",
      "f13: 제조사 관제 제품의 보안 인증 주장은 벤더 주장으로만 제안"
    ],
    "budget_used": {
      "queries": 16,
      "sources": 15
    },
    "limits": "재실행 1회차. 반려 사유 1(스키마 불일치: finding f27 이 sources 에 없는 ref-012 를 참조): 직전 반환값(research.json)이 이번 입력에 포함되지 않아 형식만 고칠 수 없었으므로 같은 대상·예산 안에서 브리프 전체를 다시 작성했고, 모든 findings[].source_ids 가 sources[].id 에 있는지 확인했다. ref-012 는 쓰지 않았으며 f27 은 ref-010·ref-616·ref-614 를 근거로 한다(관련 finding: f27). web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문을 연 출처: 재사용 ref-009·ref-010·ref-031, 신규 ref-610·ref-611·ref-612·ref-613. 나머지는 검색 요약 기준(원문 미열람, 신뢰도 상한 medium). 재사용 ref-009·ref-010 은 참고문헌 목록 요약이 입력에 없어 제목·기관을 원문 기준으로 적었다(같은 URL 이면 퍼블리셔가 기존 항목으로 합친다). 재사용 ref-031·ref-759 는 2026-09-25-61 브리프 값. 검색 16회/30, 신규 출처 15건/15(ref-610~ref-624, 예약 구간 안) — 신규 출처 예산에 도달해 The Robot Report(ISO 10218 교차 확인용), 비잔틴 로봇 연구 논문, KISA 로봇 보안모델 보도, 멀티테넌트 로보틱스 벤더 자료는 출처로 넣지 않았다. 교차 확인 0건. 한국 자료: 개인정보 보호법 제25조의2(ref-620), 개인정보위 안내서 해설(ref-621), 근로자참여법(ref-622), KISA 해설서(ref-623). 교차 규칙: 영상의 AI 학습 활용(f20)은 27. AI·학습·적응과 모델 운영과 연결 제안(f28). 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 정정 요청 없음."
  }
}
```

### docs/categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md

```markdown
---
title: "26. 사이버보안·접근권한·개인정보"
type: area
category: "G. 안전·보안·지능·거버넌스"
area_no: 26
related_areas: []
tags: []
status: seed
created: 2026-09-24
updated: 2026-09-24
sources: []
version: 1
---

[홈](../../index.md) › [G. 안전·보안·지능·거버넌스](index.md) › 26. 사이버보안·접근권한·개인정보

# 26. 사이버보안·접근권한·개인정보

!!! info "소속 대분류"
    [G. 안전·보안·지능·거버넌스](index.md) — 핵심 질문:
    전체 영역에 어떤 공통 제약과 관리 체계를 적용할 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [자연어 업무 지시 챗봇](../../tracks/nl-task-chatbot/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 자연어 업무 지시 챗봇](../../ideas/nl-task-chatbot.md)
<!-- auto:area-tracks:end -->

## 1. 한 줄 정의

장비 인증, 통신 보호, 명령 권한, 원격 접속, 고객별 격리, 영상·작업자 데이터 보호 [분류원문]

## 2. SCM 관점의 질문

외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가? [분류원문]

## 3. 왜 중요한가

아직 작성되지 않음

## 4. 핵심 개념과 용어

아직 작성되지 않음

## 5. 현장 시나리오 (물류 흐름의 어느 단계인지 명시)

아직 작성되지 않음

## 6. 대표 접근법과 기술

아직 작성되지 않음

## 7. 관련 표준·프레임워크·오픈소스

아직 작성되지 않음

## 8. 대표 연구와 자료

아직 작성되지 않음

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준)

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

### docs/categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md (요약)

```markdown
# 25. 안전·위험 관리

소속 대분류: G. 안전·보안·지능·거버넌스 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-24 · 버전: 1

## 1. 한 줄 정의

로봇·사람·설비 상호작용의 위험, 안전 조건, 정지·재개 절차, 비상 상황 대응, 안전 책임 경계 [분류원문]

## 2. SCM 관점의 질문

여러 장비는 각각 안전해도 함께 움직일 때 새로운 위험이 생기지 않는가? [분류원문]
```

### docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md (요약)

```markdown
# 27. AI·학습·적응과 모델 운영

소속 대분류: G. 안전·보안·지능·거버넌스 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-24 · 버전: 1

## 1. 한 줄 정의

문서·도면 해석, 수요·고장 예측, 학습 기반 계획, LLM 에이전트, 불확실성 평가, 모델 변경 관리 [분류원문]

## 2. SCM 관점의 질문

AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? [분류원문]

> 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [분류원문]
```

### docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md (요약)

```markdown
# 28. 표준·상호운용성·다사업자 거버넌스

소속 대분류: G. 안전·보안·지능·거버넌스 · 상태: seed · 신뢰도: — · 마지막 갱신: 2026-09-24 · 버전: 1

## 1. 한 줄 정의

공통 규격, 적합성 시험, 제조사 간 책임, 데이터 소유권, API 변경 정책, 서비스 수준과 감사 이력 [분류원문]

## 2. SCM 관점의 질문

제조사·ROP·설비업체 중 누가 연동 오류를 수정하고 변경을 승인할까? [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 574건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 148개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- age-of-information: 정보 나이 (Age of Information (AoI))
- aggregation-event: 집계 이벤트 (AggregationEvent)
- ariac: 산업 자동화용 민첩 로봇 경진대회 (Agile Robotics for Industrial Automation Competition (ARIAC))
- asset-administration-shell: 자산관리셸 (Asset Administration Shell (AAS))
- association-event: 연결 이벤트 (AssociationEvent)
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
- conformance-test: 적합성 시험 (Conformance Test)
- consensus-based-bundle-algorithm: 합의 기반 번들 알고리즘 (Consensus-Based Bundle Algorithm (CBBA))
- cooperative-object-transport: 협동 운반 (Cooperative Object Transport)
- cora: 로봇·자동화 핵심 온톨로지 (Core Ontology for Robotics and Automation (CORA))
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
- human-in-the-loop: 사람 참여 루프 (Human-in-the-Loop (HITL))
- hungarian-method: 헝가리안 방법 (Hungarian Method)
- idempotency-key: 멱등성 키 (Idempotency Key)
- identity-report: 신원 보고 (Identity Report (MassRobotics identityReport))
- iec-common-data-dictionary: IEC 공통 데이터 사전 (IEC Common Data Dictionary (IEC CDD))
- ifc: 산업 기초 클래스 (Industry Foundation Classes (IFC))
- indoor-mapping-data-format: 실내 지도 데이터 형식 (Indoor Mapping Data Format (IMDF))
- indoor-space-subspacing: 공간 세분화 (Subspacing (Indoor Space Subdivision))
- indoorgml: IndoorGML (IndoorGML)
- information-delivery-specification: 정보 전달 명세 (Information Delivery Specification (IDS))
- information-for-use: 사용 정보 (Information for Use (Instructions for Use))
- intent-recognition: 의도 인식 (Intent Recognition (Intent Detection))
- irdi: 국제 등록 데이터 식별자 (International Registration Data Identifier (IRDI))
- isa-95: 기업–제어 시스템 통합 표준 (ISA-95 Enterprise-Control System Integration)
- layout-interchange-format: 레이아웃 교환 형식 (Layout Interchange Format (LIF))
- lifelong-mapf: 지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF))
- lift-adapter: 승강기 어댑터 (Lift Adapter)
- linear-temporal-logic: 선형 시간 논리 (Linear Temporal Logic (LTL))
- littles-law: 리틀의 법칙 (Little's Law)
- llm-agent: LLM 에이전트 (LLM Agent)
- location-check-digit: 위치 체크 디지트 (Location Check Digit)
- managed-node: 관리형 노드 (Managed Node (ROS 2 Lifecycle Node))
- map-alignment: 지도 정합 (Map Alignment)
- mapf: 다중 에이전트 경로 찾기 (Multi-Agent Path Finding (MAPF))
- market-based-task-allocation: 시장 기반 작업 배정 (Market-based Task Allocation)
- milp: 혼합 정수 계획 (Mixed Integer Linear Programming (MILP))
- mobile-manipulator: 모바일 매니퓰레이터 (Mobile Manipulator)
- model-checking: 모델 검사 (Model Checking)
- mqtt: 메시지 큐잉 원격 측정 전송 (Message Queuing Telemetry Transport (MQTT))
- mrta: 다중 로봇 작업 배정 (Multi-Robot Task Allocation (MRTA))
- multi-agent-pickup-and-delivery: 다중 에이전트 픽업·배송 (Multi-Agent Pickup and Delivery (MAPD))
- multi-fleet-orchestration: 다중 플릿 오케스트레이션 (Multi-Fleet Orchestration)
- nearest-vehicle-first-rule: 최근접 차량 우선 규칙 (Nearest Vehicle First (NVF) Rule)
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
- operating-mode: 운용 모드 (Operating Mode (VDA 5050 operatingMode))
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
- roadmap: 경로망 (Roadmap)
- robotic-mobile-fulfillment-system: 로봇 이동형 풀필먼트 시스템 (Robotic Mobile Fulfillment System (RMFS))
- root-cause-analysis-rca: 근본 원인 분석 (Root Cause Analysis (RCA))
- runtime-verification: 런타임 검증 (Runtime Verification)
- safe-interval-path-planning: 안전 구간 경로 계획 (Safe Interval Path Planning (SIPP))
- saga: 사가 (Saga)
- scor: 공급망 운영 참조 모델 (Supply Chain Operations Reference (SCOR))
- semantic-id: 의미 식별자 (Semantic ID (semanticId))
- semi-open-queueing-network: 반개방형 대기행렬 네트워크 (Semi-Open Queueing Network (SOQN))
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
- structured-output: 구조화 출력 (Structured Output)
- task-decomposition: 작업 분해 (Task Decomposition)
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
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
```

### docs/open-questions.md (요약: 대상 영역 [26] 에 걸린 3건 / 전체 93건)

```markdown
- oq-043 [열림] 로봇 관제가 출입통제·건물 자동화 시스템(BACnet 등)을 통해 보안문을 여닫는 공개 설계나 국내 사례가 있고, 권한 확인은 누가 하는가? (영역 10, 26)
- oq-056 [열림] 로봇 관제·플릿 어댑터·승강기·문 어댑터에 SROS 2 인클레이브와 권한 파일을 어떤 단위로 나눠 설비 명령 권한을 제한하는지 공개한 구성이나 사례가 있는가? (영역 10, 26)
- oq-082 [열림] 로봇·제조사 관제가 보고하는 위치·배터리·입찰 비용이 오염되거나 위조되었을 때 ROP 는 배정 전에 이를 어떻게 검증하고, 의심 로봇을 배정 후보에서 뺄 기준은 무엇인가? (영역 13, 26, 19)
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
# area_no 는 1~28 의 세부영역 번호다. 사람이 읽기 쉽도록 주석에 영역 이름을 함께 적는다(예: 7. 화물·재고·자산 식별과 추적).
# 지정한 항목이 처리되면 목록에서 지워도 된다. 지우지 않으면 rotation.yaml 의 priority.skip_if_targeted_within_days 가 지난 뒤 다시 우선된다.
# 우선 지정은 조사 대상을 정할 뿐 검증 규칙과 하루 예산(daily_budget)을 바꾸지 않는다.

# 세부영역을 먼저 다루게 한다. weight 는 대상 선정 점수에 더하는 가중치, reason 은 로그(target.json·일일 로그)에 남는 지정 사유다.
areas: []
# 작성 예시:
# areas:
#   - area_no: 7            # 7. 화물·재고·자산 식별과 추적
#     weight: 10            # 대상 선정 점수에 더하는 가중치
#     reason: "인계 확인 사례가 부족하다"

# 특정 주제로 주제 조사(run_type topic)를 실행하게 한다. area_no 는 주 연구영역이다.
topics: []
# 작성 예시:
# topics:
#   - title: "팔레트 인계 확인에 EPCIS 이벤트를 쓰는 방법"
#     area_no: 7            # 주 연구영역: 7. 화물·재고·자산 식별과 추적
#     weight: 8

# 답을 찾게 할 질문이다. area_no 영역을 areas 와 같이 순환보다 먼저 대상으로 올리고(가중치는 rotation.yaml 의 priority.question_weight), 그 영역이 대상이 되면 리서치 에이전트의 조사 질문에 포함된다.
questions: []
# 작성 예시:
# questions:
#   - question: "로봇 도착과 실제 팔레트 인계를 어떤 이벤트로 구분해 기록하는가?"
#     area_no: 7            # 7. 화물·재고·자산 식별과 추적

# 트랙 백로그에 넣을 질문이다(8.2). 다음 트랙 실행의 대상 선정이 제기 근거 "사용자"로 백로그에 등록해 우선순위를 올린다(8.2).
# 처리 순서: 리서치 에이전트는 트랙 실행마다 현재 단계의 열린 질문 가운데 사용자 지정 → 앞 단계로 되돌아온 질문 → 오래된 순으로 1~3개를 고르므로(6.1),
# 현재 단계에 넣은 사용자 질문이 가장 앞에 온다. 사용자 질문이 여럿이면 priority(high → normal → low), 같으면 파일에 적힌 순이다 [가정].
# stage 가 현재 단계보다 앞이면 되돌아온 질문과 같이 다음 트랙 실행에서 우선 처리하고(8.2), 뒤이면 그 단계가 현재 단계가 될 때 다룬다 [가정].
track_questions: []
# 작성 예시:
# track_questions:
#   - track: manual-capability-ontology   # config/tracks/<slug>.yaml 의 slug
#     stage: 1              # 질문을 넣을 단계 번호(1~7). 예: 단계 1. 기존 능력 표현 모델과 표준 조사
#     question: "산업 상호운용 규격의 팩트시트는 적재 제약을 어떤 필드로 기술하는가?"
#     priority: high        # high / normal / low. 사용자 지정 질문이 여럿일 때 고르는 순서에만 쓴다 [가정]
```

### runs/2026-09-25-63/research.md

```markdown
# 리서치 브리프 2026-09-25-63

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-63 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 25. 안전·위험 관리 |
| 대분류 | G. 안전·보안·지능·거버넌스 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음(위험성평가, 3단계 위험 감소, 운용 구역, 안전 필드 침범, STPA)
- 섹션 5. 현장 시나리오 비어 있음(물류 흐름 단계 명시 필요)
- 섹션 6. 대표 접근법과 기술 비어 있음(트랙 nl-task-chatbot 단계 2 반영 제안 SafeGate 1건 포함)
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음
- 섹션 10. 다른 연구영역과의 연결 비어 있음
- 섹션 11. 열린 질문 비어 있음(대상 영역 열린 질문 oq-064, oq-070 걸려 있음)

## 조사 질문

1. 여러 장비는 각각 안전해도 함께 움직일 때 새로운 위험이 생기지 않는가? [분류원문]
2. 이동 로봇·산업용 로봇의 안전 표준(ISO 3691-4, ANSI/A3 R15.08, ISO 10218-2:2025, ISO 12100)은 제조사·통합자·사용자의 책임을 어떻게 나누는가? (섹션 3·7·9 겨냥)
3. 로봇 상호운용 규격과 오픈소스 오케스트레이션(VDA 5050, Open-RMF)은 비상정지·정지·재개·비상 대응을 어떤 메시지와 범위로 다루는가? (섹션 4·6·9 겨냥)
4. 여러 로봇이 함께 움직일 때 생기는 상호작용 위험을 분석하는 방법(STPA 등)과 대표 연구는 무엇인가? (섹션 6·8 겨냥)
5. oq-070 2024-11 제정된 이동식 협동로봇 안전기준 KS 의 표준 번호와 내용은 무엇이며, ISO 10218-2:2025·ISO 3691-4:2023 과 어떻게 대응하는가?
6. oq-064 국내에 ANSI/A3 R15.08-2 의 유형 C(모바일 매니퓰레이터) 통합 안전 요구에 대응하는 KS 표준이나 인증 기준이 있는가? 국내 규제(산업안전보건기준에 관한 규칙)는 로봇 방호를 어떻게 요구하는가? (섹션 3·5·11 겨냥)
7. LLM 이 만든 작업 지시를 실행 전에 안전 판정하는 접근(SafeGate)은 무엇이며 ROP 에 어떤 한계로 적용되는가? (트랙 반영 제안, 섹션 6 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 3.0.0 은 기능·운영·시스템 안전 요구를 정의하지 않으며 안전 표준으로 간주하거나 적용해서는 안 된다고 범위 절에 명시한다. | ref-569 | 아니오 | medium | 2026-09-25 | — | — |
| f2 | [사실] | VDA 5050 3.0.0 상태 메시지의 safetyState 는 비상정지 상태(eStop: AUTOACK·MANUAL·REMOTE·NONE)와 보호 필드 침범 여부(fieldViolation)를 보고하고, 즉시 동작 startPause·stopPause 로 자동 주행을 멈추고 재개하며, operatingMode 로 로봇이 자동 주문을 받는지(AUTOMATIC)·수동 제어 중인지(MANUAL)를 알린다. | ref-569 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f3 | [사실] | Open-RMF 핵심 설계에서 교통 충돌 예방은 RMF 의 교통 스케줄 데이터베이스와 협상이 맡고 경로 계획은 각 플릿 관리자가 맡으며, 비상 대응 같은 긴급 작업은 높은 우선순위 참여자가 교통 협상을 강제하는 방식으로 다룬다. | ref-004 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f4 | [사실] | Open-RMF 공식 저장소의 기능 요청(이슈 #658)에 따르면 화재경보가 울리면 로봇들이 주차 위치로 이동하며, 현재 비상 신호 메시지는 어느 건물·플릿 대상인지 구분하지 않는 불리언 값이어서 대상 플릿 목록(fleet_names)을 지정하자는 제안이 올라와 있다. | ref-580 | 아니오 | medium | 2026-09-25 | 예외·성과 | 원문 미열람 |
| f5 | [사실] | ISO 3691-4:2023 은 무인 산업 차량(AGV·AMR·자동 대차·견인차 포함)과 그 시스템의 안전 요구와 검증 방법을 정하며, 운용 구역(operating zone)의 상태가 안전 운용에 큰 영향을 준다고 보고 운용 구역 준비를 부속서 A 에 둔다. | ref-570 | 아니오 | medium | 2023 | 제약 | 원문 미열람 |
| f6 | [사실] | ANSI/A3 R15.08-2(2023)는 산업용 이동 로봇(IMR) 한 대 또는 플릿을 현장에 통합·구성·맞춤화할 때의 안전 요구를 정하는 시스템 통합자용 표준으로, 로봇 자체 요구는 Part 1 이, 사용자 요구는 예정된 Part 3 이 맡는다. | ref-571 | 아니오 | medium | 2023-10 | 수행 자원 | 원문 미열람 |
| f7 | [사실] | ISO 10218-2:2025(산업용 로봇 응용과 로봇 셀)는 2011년판을 대체해 2025년 2월 발행됐으며, 협동 운전 요구(종전 ISO/TS 15066)를 본문에 통합하고 사이버보안 요구를 더했으며 '로봇 시스템' 대신 공작물·작업 프로그램·지원 설비까지 포함하는 '로봇 응용'을 강조한다. | ref-572 | 아니오 | medium | 2025-02 | — | 원문 미열람 |
| f8 | [사실] | 중소벤처기업부는 대구 이동식 협동로봇 규제자유특구 실증으로 안전성을 검증한 뒤 이동식 협동로봇 안전기준 한국산업표준(KS)을 제정해 2024-11-01 부터 산업현장에서 활용할 수 있게 했다고 밝혔고, 그 전에는 명확한 기준이 없어 작업공간 분리나 안전펜스 설치 때문에 이동 중 작업이 사실상 불가능했다고 설명했다. | ref-573 | 아니오 | medium | 2024-11-03 | 제약 | 원문 미열람 |
| f9 | [사실] | 산업안전보건기준에 관한 규칙 제223조(운전 중 위험 방지)는 사업주에게 로봇 운전 중 위험을 막기 위해 높이 1.8m 이상 울타리 설치 등을 요구하되, 고용노동부장관이 해당 로봇의 안전기준이 한국산업표준 또는 국제적으로 통용되는 안전기준에 부합한다고 인정하면 울타리 등 조치를 생략할 수 있게 한다. | ref-574 | 아니오 | medium | 2023-07-01 | 제약 | 원문 미열람 |
| f10 | [사실] | SafeGate(arXiv 2604.05427)는 자연어 작업 명령에서 ISO 13482 에 근거한 안전 관련 속성을 뽑아 결정적 판정으로 실행 승인·사람에게 확인 요청·거부 중 하나를 내고, 승인한 작업은 불변 조건·가드·중단 조건으로 된 작업 안전 계약으로 분해해 실행 중 감시에 쓰는 구조를 제안했으며, 230개 벤치마크 작업·30개 AI2-THOR 시나리오·실로봇 실험으로 평가했다고 저자가 보고한다. | ref-575 | 아니오 | medium | 2026-04 | 시작 조건 | 원문 미열람 |
| f11 | [사실] | 국내에는 협동로봇 기술규격 ISO/TS 15066 이 KS B ISO/TS 15066 로 부합화되어 한국표준정보망에 등재되어 있다. | ref-581 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f12 | [사실] | Belzile 외(arXiv 2502.20693)는 사람이 붐비는 작업장에 이동 로봇을 배치할 때의 안전 위험을 정량 지표로 평가하는 틀을 제안하고 ISO/TS 15066·ANSI/RIA R15.08 등 관련 표준을 검토했으며, 건설 현장 사례로 검증했다. | ref-576 | 아니오 | medium | 2025-02 | 예외·성과 | 원문 미열람 |
| f13 | [사실] | STPA(System-Theoretic Process Analysis) 계층 제어 구조 비교 연구는 복잡한 다중 이동 로봇 시스템에 STPA 를 적용해 중앙집중·계층형 등 제어 구조별 위험 시나리오와 원인 요인을 도출했다. | ref-577 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f14 | [사실] | Reliability Engineering & System Safety 게재 연구는 다중 이동 로봇의 운반 작업에서 충돌 위험을 STPA 와 확률 페트리 넷(SPN)을 결합해 모델링·분석했다. | ref-578 | 아니오 | medium | 2023 | 예외·성과 | 원문 미열람 |
| f15 | [사실] | ISO 12100:2010 은 기계 설계의 위험성평가와 위험 감소 일반 원칙을 정하며, 위험 감소는 본질적 안전 설계 → 방호·보완 보호 조치 → 사용 정보의 순서로 앞 단계를 다한 뒤 다음 단계로 가는 3단계 방법을 따른다. | ref-579 | 아니오 | medium | 2010 | — | 원문 미열람 |
| f16 | [추정] | 분류 원문 질문과 관련해, 확인한 표준은 차량 단위 안전(ISO 3691-4, R15.08-1)과 현장·플릿 통합 안전(R15.08-2, ISO 10218-2:2025 의 로봇 응용)을 나누고 STPA 연구는 개별적으로 정상인 구성요소 간 상호작용에서 위험을 찾으므로, 여러 로봇을 함께 움직이는 ROP 의 경로·구역·정지 결정은 시스템 수준 위험성평가 대상이 되는 것으로 보인다. | ref-570, ref-571, ref-572, ref-577 | 아니오 | low | 2026-09-25 | 제약 | 원문 미열람 |
| f17 | [추정] | ROP 가 직접 맡을 안전 몫은 로봇이 보고하는 안전 상태(비상정지·보호 필드 침범·운용 모드) 수집, 일시정지·재개 지시, 비상 신호에 따른 플릿별 대피·주차 조율, 구역·권한 제약을 경로·배정에 반영하는 운영 조율이며, 상호운용 규격 자체가 안전 표준이 아니므로 이 조율이 안전 기능을 대신하지는 않는 것으로 보인다. | ref-569, ref-004, ref-580 | 아니오 | low | 2026-09-25 | 수행 자원 | — |
| f18 | [추정] | 연계 대상: 비상정지 회로, 안전 스캐너 보호 필드, 속도·힘 제한 같은 안전 기능의 설계·검증과 현장 방호 설비는 로봇 제조사와 설비 안전 제어(분류 원문 9장) 쪽이며, ROP 는 그 상태와 결과를 받는 쪽으로 보인다. | ref-569, ref-570, ref-572 | 아니오 | low | 2026-09-25 | — | — |
| f19 | [추정] | 피킹 구역에 작업자가 들어와 로봇이 보호 필드 침범(fieldViolation)이나 비상정지 상태를 보고하면, ROP 는 해당 로봇의 진행 중 피킹 작업을 보류·재배정하고 재개 조건(안전 상태 해제, 운용 모드 AUTOMATIC 복귀)을 확인한 뒤 stopPause 등으로 재개를 지시해야 할 것으로 보인다. | ref-569 | 아니오 | low | 2026-09-25 | 피킹 / 예외·성과 | — |
| f20 | [추정] | 출하 마감 전에 화재경보 같은 비상 신호가 오면 로봇이 주차 위치로 이동해 출하 준비 작업이 중단되므로, 비상 해제 후 어떤 작업을 어떤 순서로 재개할지와 대상 플릿 구분이 출하 성과(마감 준수)에 영향을 주는 것으로 보인다. | ref-580, ref-004 | 아니오 | low | 2026-09-25 | 출하 / 예외·성과 | — |
| f21 | [추정] | 25. 안전·위험 관리는 사이버보안 요구가 안전 표준에 들어온 점에서 26. 사이버보안·접근권한·개인정보와, LLM 명령의 실행 전 안전 판정에서 27. AI·학습·적응과 모델 운영·18. 사람–로봇 협업·운영 인터페이스와, 교통 협상에서 15. 다중 로봇 경로·교통 관리 — MAPF 와, 정지·재개 지시의 확실한 전달에서 12. 명령·작업 실행의 신뢰성과 맞물리는 것으로 보인다. | ref-572, ref-575, ref-004, ref-569 | 아니오 | low | 2026-09-25 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 아니오 |
| ref-569 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — VDA5050_EN.md (VDA 5050 Version 3.0.0) | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-570 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 2023 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/83545.html | 예 |
| ref-571 | Association for Advancing Automation (A3) | ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available | 2023-10 | 표준 | medium | 2026-09-25 | https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available | 예 |
| ref-572 | ISO | ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells | 2025-02 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/73934.html | 예 |
| ref-573 | 대한민국 정책브리핑(중소벤처기업부) | 이동식 협동로봇 ‘안전기준 산업표준’ 제정…상용화 길 열어 | 2024-11-03 | 정부·연구기관 | medium | 2026-09-25 | https://www.korea.kr/news/policyNewsView.do?newsId=148935814 | 예 |
| ref-574 | 국가법령정보센터(고용노동부) | 산업안전보건기준에 관한 규칙 제223조(운전 중 위험 방지) | 2023-07-01 | 정부·연구기관 | medium | 2026-09-25 | https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EC%82%B0%EC%97%85%EC%95%88%EC%A0%84%EB%B3%B4%EA%B1%B4%EA%B8%B0%EC%A4%80%EC%97%90%EA%B4%80%ED%95%9C%EA%B7%9C%EC%B9%99/(20230701,00367,20221018)/%EC%A0%9C223%EC%A1%B0 | 예 |
| ref-575 | arXiv (SafeGate 저자, 저자명 미확인) | Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems | 2026-04 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2604.05427 | 예 |
| ref-576 | Belzile, B. 외 | From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment | 2025-02 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2502.20693 | 예 |
| ref-577 | IEEE Xplore (저자 미확인) | A Comparative Study of STPA Hierarchical Structures in Risk Analysis: The Case of a Complex Multi-Robot Mobile System | 미확인 | 논문 | medium | 2026-09-25 | https://ieeexplore.ieee.org/document/8910126/ | 예 |
| ref-578 | Reliability Engineering & System Safety (저자 미확인) | Collision hazard modeling and analysis in a multi-mobile robots system transportation task with STPA and SPN | 2023 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0951832023000534 | 예 |
| ref-579 | CEN (iTeh Standards 카탈로그) | EN ISO 12100:2010 - Safety of machinery - General principles for design - Risk assessment and risk reduction | 2010 | 표준 | medium | 2026-09-25 | https://standards.iteh.ai/catalog/standards/cen/74a41162-9d84-4410-a8a3-606630770ab9/en-iso-12100-2010 | 예 |
| ref-580 | Open-RMF (open-rmf/rmf GitHub) | [Feature request]: Fire alarm separation for different fleets · Issue #658 · open-rmf/rmf | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf/issues/658 | 예 |
| ref-581 | 한국표준정보망(KSSN, 국가기술표준원) | KS B ISO/TS 15066 로봇 및 로봇 장치 - 협동로봇 | 미확인 | 표준 | medium | 2026-09-25 | https://www.kssn.net/search/stddetail.do?itemNo=K001010113282 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | seed 페이지 3~11절 첫 작성. 3절: f16(분류 원문 질문, 추정), f8·f9(국내 규제 맥락) / 4절: f15(위험성평가·3단계), f5(운용 구역), f2(비상정지·보호 필드 침범), f13(STPA) / 5절: f19(피킹·예외·성과), f20(출하·예외·성과) / 6절: f13·f14(STPA 기반 다중 로봇 위험 분석), f12(정량 위험 지표), f10(SafeGate — 트랙 nl-task-chatbot 단계 2 반영 제안 2026-09-25-37 f12 반영; ISO 13482 는 개인 돌봄 로봇 표준·저자 보고 평가·물류 현장 아님 병기) / 7절: f1·f2(VDA 5050), f3·f4(Open-RMF), f5(ISO 3691-4), f6(R15.08-2), f7(ISO 10218-2:2025), f11(KS B ISO/TS 15066), f8(이동식 협동로봇 KS), f9(산안규칙 제223조), f15(ISO 12100) / 8절: f12·f13·f14·f10 / 9절: f17(ROP 직접), f18('연계 대상') / 10절: f21(26. 사이버보안·접근권한·개인정보, 27. AI·학습·적응과 모델 운영, 18. 사람–로봇 협업·운영 인터페이스, 15. 다중 로봇 경로·교통 관리 — MAPF, 12. 명령·작업 실행의 신뢰성), 24. 자산·소프트웨어 수명주기 관리(2026-09-25-61 브리프의 변경 후 재평가) / 11절: oq-064·oq-070 유지와 open_questions_new 3건 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 위험성평가 | Risk Assessment (ISO 12100) | 위험원을 찾고 위험을 추정·평가해 위험 감소가 필요한지 판단하는 절차로, ISO 12100 이 기계 설계의 일반 원칙으로 정한다. |
| 3단계 위험 감소 방법 | Three-Step Method (ISO 12100) | 본질적 안전 설계, 방호·보완 보호 조치, 사용 정보의 순서로 위험을 줄이는 ISO 12100 의 우선순위 원칙이다. |
| 운용 구역 | Operating Zone (ISO 3691-4) | 무인 산업 차량이 운행하는 구역으로, ISO 3691-4 는 사람 유무 등 구역 조건에 따라 준비와 안전 요구를 달리 둔다. |
| 시스템 이론적 프로세스 분석 | System-Theoretic Process Analysis (STPA) | 개별 부품 고장보다 정상 동작하는 구성요소 사이의 안전하지 않은 제어 상호작용에서 위험 시나리오를 찾는 위험 분석 기법이다. |

## 열린 질문

새로 생긴 질문:

- ROP 가 원격 비상정지(VDA 5050 eStop REMOTE)나 플릿 일괄 정지를 지시할 때 그 지시 경로가 안전 기능으로서 성능 수준(PL) 요구를 받는가, 아니면 운영 조율로만 보는가? | 관련 영역: 25. 안전·위험 관리, 12. 명령·작업 실행의 신뢰성 | 근거: f2 | 종류: 일반
- 여러 제조사 로봇이 섞인 현장에서 R15.08-2 가 말하는 통합자의 시스템 수준 위험성평가를 ROP 사업자·제조사·설비업체 중 누가 수행하고 갱신하는가? | 관련 영역: 25. 안전·위험 관리, 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f6 | 종류: 일반
- 산업안전보건기준에 관한 규칙 제223조의 울타리 생략 인정이 물류센터의 자율이동로봇(AMR) 플릿에도 적용되며, 어떤 KS·국제 기준 부합이 요구되는가? | 관련 영역: 25. 안전·위험 관리, 18. 사람–로봇 협업·운영 인터페이스 | 근거: f9 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 14 · 교차 확인: 0
- 예산 사용량: 검색 11회 · 신규 출처 13건
- 미확인 항목:
    - 모든 finding 교차 확인 없음(단일 출처)
    - oq-070 이동식 협동로봇 KS 표준 번호 미확인(정부 보도자료 검색 요약에 번호 없음) — 미해결 유지
    - oq-064 R15.08-2 유형 C 대응 KS·인증 기준 미확인 — 미해결 유지
    - f7 ISO 10218-2:2025 변경 내용은 ISO 소개 페이지 원문 미열람, 검색 요약(인증기관·협회 해설) 기준
    - f10 SafeGate 평가 수치는 저자 보고, 원문 미열람
    - ref-575·ref-577·ref-578 저자, ref-577·ref-580·ref-581·ref-004·ref-569 발행일 미확인
    - ISO 3691-4 의 제조사–통합자 책임 분담은 2차 해설에만 있어 finding 에서 제외
- 범위 경계 위반 의심:
    - f18: 안전 기능 설계·방호 설비는 분류 원문 9장 '로봇 자체 지능·제어'·'시설·설비 제어' 쪽이라 '연계 대상:'으로 표시
    - f12: 건설 현장 사례라 방법론 근거로만 제안(업종별 조건 연계)
    - f10: 개인 돌봄 로봇 표준(ISO 13482) 기반 연구라 물류 현장 적용은 추정으로만 서술하도록 제안
- 한계: 재실행 1회차. 반려 사유 1(finding f5 가 벤더 문서만 근거로 한 [사실]인데 vendor_claim 표시 없음): 직전 반환 JSON 이 이번 입력에 포함되지 않아 형식만 고칠 수 없었으므로 브리프를 처음부터 다시 작성했다(검색 11회/30). 이번 브리프는 벤더 문서 출처를 하나도 쓰지 않았고, 모든 [사실] finding 은 표준·정부·오픈소스·논문 출처에 기대며, 벤더 문서만 근거로 한 [사실] finding 이 없다(관련 finding: f5 는 이제 ISO 3691-4 표준 근거). web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 연 출처: 신규 ref-569(VDA 5050 3.0.0 명세), 재사용 ref-004(rmf-core). 나머지 12건은 검색 요약 기준(원문 미열람, 신뢰도 상한 medium). ref-004 는 참고문헌 목록 요약이 입력에 없어 리서치 규칙 예시의 값을 그대로 썼다. 신규 출처 13건(ref-569~ref-581, 예약 구간 안). 한국 자료: 이동식 협동로봇 KS 제정 보도자료(ref-573), 산안규칙 제223조(ref-574), KS B ISO/TS 15066(ref-581). 트랙 반영 제안(nl-task-chatbot 단계 2, SafeGate)은 f10 으로 확인해 6절에 제안했다. 교차 규칙: SafeGate 는 27. AI·학습·적응과 모델 운영과 적용 대상 영역에 함께 연결하도록 f21 로 제안. 8·22 구분 관련 주장 없음. 정정 요청 없음.
```

### runs/2026-09-25-62/research.md

```markdown
# 리서치 브리프 2026-09-25-62

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-62 |
| 날짜 | 2026-09-25 |
| 실행 유형 | track (트랙 실행) |
| 대상 영역 | 13. 작업 배정 — MRTA |
| 대분류 | D. 계획·최적화 |

트랙 실행: 트랙 `nl-task-chatbot` · 단계 2 · 답한 질문 q2-03

## 갭(비어 있거나 약한 섹션)

- 단계 2 질문 q2-03 열림(target.json 지정, CLI 지정 질문 id). 단계 2 페이지 3절에 q2-03 소제목 없음
- 완료 조건: 아이디어 2. 자연어 업무 지시 챗봇 4절에 평가 데이터(지시–정답 작업 쌍) 소절 없음(q2-03 미조사로 명시됨)
- 완료 조건: 업무 분해·배정 설계 초안의 작업 요구 적재물 속성·업무 완료 조건 미확정(이번 질문 범위 밖)
- 13. 작업 배정 — MRTA 섹션 8. 대표 연구와 자료(주제 페이지)에 LLM 배정 평가 데이터셋·지표 근거 없음
- 23. 시험·형식 검증·벤치마크 페이지 seed 상태: 지시 해석·계획 평가 벤치마크 근거 없음

## 조사 질문

1. 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [분류원문]
2. q2-03 해석·분해의 정확도를 평가하려면 어떤 지시–정답 작업 쌍 데이터가 필요하며, 쓸 수 있는 공개 데이터셋이 있는가?
3. 지시를 행동 순서·목표 조건으로 바꾸는 체화 에이전트 벤치마크(ALFRED, TEACh, LoTa-Bench)는 지시와 정답을 어떤 형식(목표 조건, 전문가 시연, 최종 상태)으로 짝지우는가? (단계 2 페이지 3절 겨냥)
4. 다중 로봇 LLM 계획·배정 벤치마크(SMART-LLM 데이터셋, MAT-THOR)는 정답과 지표(성공률, 목표 조건 재현율, 로봇 활용도)를 어떻게 두는가? (13. 작업 배정 — MRTA 섹션 8, 23. 시험·형식 검증·벤치마크 연결)
5. 모호·불완전 지시와 슬롯 추출을 평가하는 데이터셋(AmbiK, NoisyToolBench, Snips NLU 벤치마크, Lang2LTL 말뭉치)은 무엇을 정답으로 두는가? (27. AI·학습·적응과 모델 운영 연결)
6. 물류·창고 지시를 대상으로 한 지시–정답 데이터셋이나 국내 공개 데이터(AI Hub)가 있는가? (한국 자료 우선 규칙)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | ALFRED 는 자연어 지시와 1인칭 시각 입력을 가정 작업의 행동 순서로 대응시키는 학습 벤치마크로, AI2-THOR 2.1.0 시뮬레이터 위에서 상위 목표 기술과 단계별 지시를 함께 제공한다. | ref-539 | 아니오 | medium | 2026-09-25 | — | — |
| f2 | [사실] | ALFRED 논문(CVPR 2020)은 25,743개의 영어 지시와 8,055개의 전문가 시연을 담고, 시연은 PDDL 로 기술한 환경 동역학과 작업별 PDDL 목표 조건을 고전 계획기에 주어 생성했다고 밝힌다. | ref-540 | 아니오 | medium | 2020 | — | 원문 미열람 |
| f3 | [사실] | LoTa-Bench(ICLR 2024)는 가정 서비스 에이전트의 언어 기반 작업 계획 성능을 자동으로 정량화하는 벤치마크로, ALFRED·AI2-THOR 와 Watch-And-Help 확장·VirtualHome 두 쌍에서 성공률로 계획기를 비교한다. | ref-541, ref-542 | 아니오 | medium | 2024-02 | — | — |
| f4 | [사실] | TEACh 는 AI2-THOR 가정 환경에서 지시하는 사람(Commander)과 수행하는 사람(Follower)이 대화하며 작업을 완수한 사람–사람 대화 세션 데이터셋으로, EDH·TfD·TATC 세 벤치마크를 두고 데이터는 CDLA-Sharing 1.0 으로 공개된다. | ref-543 | 아니오 | medium | 2026-09-25 | — | — |
| f5 | [사실] | SMART-LLM 공식 저장소는 작업 복잡도가 다른 네 범주의 상위 지시로 이루어진 다중 로봇 작업 계획 벤치마크 데이터셋을 두고, 평가용으로 작업마다 사용 가능한 로봇과 작업 후 환경의 최종 상태를 함께 제공한다. | ref-089 | 아니오 | medium | 2026-09-25 | — | — |
| f6 | [사실] | SMART-LLM 논문은 AI2-THOR 기반 36개 상위 지시 데이터셋에서 성공률, 작업 완료율, 정답 최종 상태 조건 대비 목표 조건 재현율(GCR), 정답 전이 수와 비교한 로봇 활용도(RU), 실행 가능 동작 비율(Exe)의 다섯 지표로 평가한다. | ref-090 | 아니오 | medium | 2023-09 | — | 원문 미열람 |
| f7 | [사실] | LaMMA-P 의 MAT-THOR 는 AI2-THOR 기반 다중 에이전트 가정 작업 벤치마크로, 논문은 5개 평면도의 70개 작업(복합 30, 복잡 20, 모호한 지시 20)마다 자연어 지시·정답 PDDL 도메인·목표 조건을 붙였다고 밝힌다. | ref-164, ref-544 | 아니오 | medium | 2024-09 | — | — |
| f8 | [사실] | AmbiK 데이터셋은 모호한 작업과 모호하지 않은 짝 1000쌍을 보정용 100건·시험용 900건으로 나누고, 환경 설명, 직접·간접·모호 지시문, 모호성 유형, 명확화 질문과 답, 작업 계획, 계획 안에서 모호성이 나타나는 지점을 필드로 둔다. | ref-354 | 아니오 | medium | 2026-09-25 | — | — |
| f9 | [사실] | NoisyToolBench 는 ToolBench 의 정상 표본 200건을 사람이 불완전하게 바꿔 만든 불명확 지시 벤치마크로, 핵심 인자 누락 등 지시 문제 유형을 나누고, 자동 평가기 ToolEvaluator 로 정확도와 되묻기 상호작용 효율을 함께 잰다. | ref-359 | 아니오 | medium | 2024-09 | — | 원문 미열람 |
| f10 | [사실] | Snips 의 NLU 벤치마크(2017-06)는 7개 의도마다 크라우드소싱으로 만든 2000개 이상의 질의를 두고 슬롯별 정밀도·재현율로 비교해, 의도 인식·슬롯 채우기 평가용 지시–정답 쌍의 형식을 보여 준다. | ref-545 | 아니오 | medium | 2017-06 | — | — |
| f11 | [사실] | Lang2LTL 연구는 47개 LTL 식 템플릿에서 나온 2,125개의 고유 LTL 식에 약 5만 개 영어 발화를 대응시킨 말뭉치와, 22개 OSM 환경의 1만 개 이상 명령으로 된 접지 평가 자료를 만들었다고 보고한다. | ref-056 | 아니오 | medium | 2023-02 | — | 원문 미열람 |
| f12 | [사실] | AI Hub 의 '일상생활 작업 및 명령 수행 데이터(임무수행 명령어)'는 3D 일상생활 공간에서 에이전트가 자연어 명령을 이해해 일련의 행동을 예측하고 상호작용할 객체 위치를 1인칭 시점 이미지에서 찾도록 구축한 국내 공개 학습 데이터다. | ref-546 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f13 | [사실] | 연계 대상: OpenBench 는 주거 지역 실외 라스트마일 배송 로봇의 의미 기반 항법 벤치마크로, LLM 이 배송 지시를 이해하고 OpenStreetMap 지도를 쓰는 기준 시스템(OPEN)을 함께 공개했다. | ref-547 | 아니오 | medium | 2025-02 | — | 원문 미열람 |
| f14 | [사실] | 물류 AMR 임무 명세에 LLM 을 번역 인터페이스로 쓰는 스웨덴 Högskolan Väst 학위논문은 LLM 이 신호 시간 논리(STL) 식의 구문·논리를 만들 수는 있으나 구문상 유효한 STL 식을 일관되게 만들지 못한다고 보고했다. | ref-548 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f15 | [추정] | 확인한 공개 데이터셋을 종합하면 해석·분해 평가용 지시–정답 쌍은 (1) 지시문, (2) 초기 환경 상태, (3) 정답 목표 조건·최종 상태 또는 형식 명세(PDDL·LTL), (4) 선택적으로 정답 계획·전이 수, (5) 모호 지시의 경우 모호성 유형과 명확화 질문·답을 담는 구조로 보인다. | ref-540, ref-541, ref-090, ref-544, ref-354, ref-056 | 아니오 | low | 2026-09-25 | — | — |
| f16 | [추정] | 이번에 확인한 지시–정답 데이터셋의 환경은 가정·주방(ALFRED, TEACh, SMART-LLM, MAT-THOR, AmbiK), 도구 호출 API(NoisyToolBench), 개인 비서(Snips), 실외 내비게이션·배송(Lang2LTL, OpenBench)이었고, 화물 식별자·로케이션·기한·배정 로봇을 정답으로 둔 물류 창고 지시 데이터셋은 검색 범위에서 찾지 못해 ROP 는 평가 자료를 자체 구축해야 할 것으로 보인다(부재의 확인은 아님). | ref-539, ref-543, ref-089, ref-544, ref-354, ref-359, ref-545, ref-547, ref-548 | 아니오 | low | 2026-09-25 | 피킹 / 시작 조건 | — |
| f17 | [추정] | 분류 원문 질문(가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가)과 관련해, 확인한 다중 로봇 벤치마크는 목표 상태 달성과 정답 전이 수 대비 로봇 활용도를 재지만 누구에게 배정했는지의 전체 최적성(이동거리·납기)을 정답으로 두지 않으므로, 배정 적합성을 평가하려면 정답 배정이나 목적함수 기준값을 따로 마련해야 할 것으로 보인다. | ref-090, ref-544 | 아니오 | low | 2026-09-25 | 예외·성과 | 원문 미열람 |
| f18 | [추정] | 확인한 평가 방식은 해석 단계(의도·슬롯별 정밀도·재현율, Snips)와 계획·실행 단계(시뮬레이터 최종 상태·목표 조건 달성, LoTa-Bench·SMART-LLM)로 나뉘어, 챗봇 평가도 해석 정확도와 분해·배정 결과의 목표 달성도를 따로 재는 두 층 구조가 필요할 것으로 보인다. | ref-545, ref-541, ref-090 | 아니오 | low | 2026-09-25 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-539 | askforalfred (ALFRED 공식 저장소) | ALFRED — A Benchmark for Interpreting Grounded Instructions for Everyday Tasks (GitHub README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/askforalfred/alfred | 아니오 |
| ref-540 | Shridhar, M. 외 | ALFRED: A Benchmark for Interpreting Grounded Instructions for Everyday Tasks | 2020 | 논문 | medium | 2026-09-25 | https://openaccess.thecvf.com/content_CVPR_2020/html/Shridhar_ALFRED_A_Benchmark_for_Interpreting_Grounded_Instructions_for_Everyday_Tasks_CVPR_2020_paper.html | 예 |
| ref-541 | lbaa2022 (LoTa-Bench 공식 저장소) | LLMTaskPlanning — LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents (ICLR 2024) (GitHub README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/lbaa2022/LLMTaskPlanning | 아니오 |
| ref-542 | LoTa-Bench 저자(arXiv 2402.08178) | LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents | 2024-02 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2402.08178 | 예 |
| ref-543 | Amazon Alexa (alexa/teach GitHub) | TEACh: Task-driven Embodied Agents that Chat (GitHub README) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/alexa/teach | 아니오 |
| ref-544 | Zhang, X. 외(LaMMA-P 저자) | LaMMA-P: Generalizable Multi-Agent Long-Horizon Task Allocation and Planning with LM-Driven PDDL Planner | 2024-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2409.20560 | 예 |
| ref-545 | Snips (sonos/nlu-benchmark GitHub) | nlu-benchmark — 2017-06-custom-intent-engines (README) | 2017-06 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/sonos/nlu-benchmark/tree/master/2017-06-custom-intent-engines | 아니오 |
| ref-546 | 한국지능정보사회진흥원(AI Hub) | 일상생활 작업 및 명령 수행 데이터(임무수행 명령어) | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=71547 | 예 |
| ref-547 | OpenBench 저자(arXiv 2502.09238) | OpenBench: A New Benchmark and Baseline for Semantic Navigation in Smart Logistics | 2025-02 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2502.09238 | 예 |
| ref-548 | Högskolan Väst (DiVA 학위논문, 저자 미확인) | An LLM- Interface for Robot Mission Specification in Logistics | 미확인 | 논문 | low | 2026-09-25 | https://hv.diva-portal.org/smash/get/diva2:2080486/FULLTEXT01.pdf | 예 |
| ref-089 | SMARTlab-Purdue (Purdue University) | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models (GitHub README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/SMARTlab-Purdue/SMART-LLM | 아니오 |
| ref-090 | Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models | 2023-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2309.10062 | 예 |
| ref-164 | TASL Lab (LaMMA-P 저자) | LaMMA-P: Generalizable Multi-Agent Long-Horizon Task Allocation and Planning with LM-Driven PDDL Planner (GitHub README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/tasl-lab/LaMMA-P | 아니오 |
| ref-354 | cog-model (AmbiK 저자) | AmbiK-dataset — README (AmbiK: Dataset of Ambiguous Tasks in Kitchen Environment) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/cog-model/AmbiK-dataset | 아니오 |
| ref-359 | Wang, W. 외 | Learning to Ask: When LLM Agents Meet Unclear Instruction | 2024-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2409.00557 | 예 |
| ref-056 | Liu, J. X. 외 | Grounding Complex Natural Language Commands for Temporal Tasks in Unseen Environments | 2023-02 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2302.11649 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/tracks/nl-task-chatbot/stage-2-data-and-standards.md | 2, 3, 4, 5, 6, 8, 9 | q2-03 답: f1·f2·f3·f4·f5·f6·f7·f8·f9·f10·f11·f12·f13·f14·f15·f16·f17·f18 (신뢰도 low) — 2절 q2-03 상태 답함, 3절 q2-03 소제목 신설({#q2-03}): 체화 에이전트 벤치마크(ALFRED f1·f2, LoTa-Bench f3, TEACh f4), 다중 로봇 벤치마크와 지표(SMART-LLM f5·f6, MAT-THOR f7), 모호·불완전 지시(AmbiK f8, NoisyToolBench f9), 해석 단계 데이터(Snips f10, Lang2LTL f11), 국내 데이터(AI Hub f12), 물류 인접 자료(OpenBench f13 연계 대상, STL 학위논문 f14), 필요한 쌍 구조(f15), 물류 데이터셋 공백(f16), SCM 질문 연결(f17), 두 층 평가(f18) / 4절 결론·불확실성 / 5절 후속 질문 / 6절 완료 조건 현황 / 8절 출처 / 9절 이력 |
| update | docs/ideas/nl-task-chatbot.md | 4 | 아이디어 페이지 4절: '해석·분해 평가 데이터' 소절 신설 — 공개 데이터셋 비교(f1·f3·f4·f5·f7·f8·f9·f10·f11·f12), 필요한 지시–정답 쌍 구조(f15, 추정), 물류 데이터셋 공백(f16, 추정), 배정 적합성 정답 부재(f17). 6절(검증 방법)로 이어지는 지표(f6·f18)는 단계 5 에서 다룸을 명시 |
| update | docs/categories/d-planning-and-optimization/13-task-allocation-mrta.md | 8 | 트랙 nl-task-chatbot 단계 2 반영 제안 (f5, f6, f7, f17): LLM 다중 로봇 배정 평가 데이터셋(SMART-LLM, MAT-THOR)과 지표(목표 조건 재현율·로봇 활용도), 배정 최적성 정답이 없다는 점과 분류 원문 질문 연결. 27. AI·학습·적응과 모델 운영과 양쪽 연결 |
| update | docs/categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md | 8 | 트랙 nl-task-chatbot 단계 2 반영 제안 (f3, f8, f9, f11, f18): LLM 지시 해석·계획 평가 벤치마크(LoTa-Bench, AmbiK, NoisyToolBench, Lang2LTL 말뭉치)와 해석·계획 두 층 평가. 적용 대상 13. 작업 배정 — MRTA·18. 사람–로봇 협업·운영 인터페이스와 함께 연결 |
| update | docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md | 8 | 트랙 nl-task-chatbot 단계 2 반영 제안 (f1, f3, f6, f16): 지시 수행 벤치마크(ALFRED, LoTa-Bench)와 시뮬레이터 최종 상태 기반 자동 평가, 물류 지시 평가 자료 부재(추정) |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 목표 조건 | Goal Condition | 작업이 끝났을 때 환경이 만족해야 하는 상태 조건의 집합으로, 지시 수행 벤치마크에서 계획·실행 결과가 맞았는지를 판정하는 정답으로 쓰인다. |
| 신호 시간 논리 | Signal Temporal Logic (STL) | 연속 시간 신호에 대해 시간 구간이 붙은 조건(예: 10초 안에 도착)을 기술하는 형식 논리로, 로봇 임무 명세에 쓰인다. |

## 열린 질문

새로 생긴 질문:

- 국내 물류센터의 작업 지시(피킹·운반·출하 준비)를 자연어 지시와 정답 작업·배정 결과로 짝지은 공개 데이터셋이나 구축 사업이 있는가? | 관련 영역: 13. 작업 배정 — MRTA, 27. AI·학습·적응과 모델 운영 | 근거: f16 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 16 · 교차 확인: 0
- 예산 사용량: 검색 17회 · 신규 출처 10건
- 미확인 항목:
    - 모든 finding 교차 확인 없음: 데이터셋마다 공식 저장소와 같은 저자 논문 쌍이거나 단일 출처
    - f2 ALFRED 수치(25,743·8,055)는 논문 원문 미열람, 검색 요약 기준 저자 보고값
    - f6 SMART-LLM 36개 지시·지표 정의는 논문 원문 미열람(README 는 네 범주만 기재)
    - f7 MAT-THOR 70개 작업 구성은 논문 원문 미열람. README 는 '두 복잡도 수준'이라고만 적어 범주 수 표현이 다름
    - f9 NoisyToolBench 문제 유형 비율은 2차 요약에만 있어 넣지 않음
    - f11 Lang2LTL 말뭉치 수치는 판마다 다른 요약(1,156개 명령 말뭉치 등)이 있어 판 차이 미확인
    - f12 AI Hub 데이터의 구축 기관·규모·정답 형식 미확인
    - f14 학위논문 저자·발행일·평가 자료 규모 미확인
    - f16 물류 지시 데이터셋 부재는 검색 범위의 관찰이며 부재 확인 아님
    - PlanBench(자연어·PDDL 프롬프트, Blocksworld 계열)는 README 가 리더보드만 보여 Logistics 도메인 포함 여부를 확인하지 못해 넣지 않음
- 범위 경계 위반 의심:
    - f13: OpenBench 는 실외 라스트마일 배송(분류 원문 9장 업종별 조건·실외 차량 연계 영역)이라 '연계 대상: '으로 표시하고 평가 자료 사례로만 제안
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문을 연 출처: 신규 ref-539(ALFRED README)·ref-541(LoTa-Bench README)·ref-543(TEACh README)·ref-545(Snips NLU 벤치마크 README), 재사용 ref-089(SMART-LLM README)·ref-164(LaMMA-P README)·ref-354(AmbiK README). 논문·AI Hub·학위논문(ref-540·ref-542·ref-544·ref-546·ref-547·ref-548, 재사용 ref-090·ref-359·ref-056)은 원문 미열람(신뢰도 상한 medium). 검색 17회/40, 신규 출처 10건/20(ref-539~ref-548, 예약 구간 안), 재사용 6건. 질문 선택: target.json 지정 q2-03 1건. q2-03 은 공개 데이터셋의 지시–정답 형식과 지표(사실 finding)로 답했으나 필요한 쌍 구조·물류 공백·배정 정답 부재(f15~f18)는 이 위키의 종합이라 질문 종합 신뢰도를 low 로 두었다. 한국 자료: AI Hub 국내 공개 데이터(ref-546, 가정 환경)를 찾았고 국내 물류 지시 데이터셋은 찾지 못해 일반 열린 질문 1건으로 올렸다. 교차 규칙: LLM 해석·계획 평가 finding 은 27. AI·학습·적응과 모델 운영과 적용 대상 13. 작업 배정 — MRTA 양쪽에 반영 제안했다. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음(시뮬레이터는 평가 도구로만 언급). 정정 요청 없음. 온톨로지 변경 없음: 평가 데이터는 업무 분해·배정 설계 초안의 개념·관계가 아니라 검증 자료이므로 초안 변경 근거가 되지 않는다. 후속 질문 2건. 백로그 참고: q3-09 와 q3-10 이 사실상 같은 질문으로 중복 등록되어 정리 필요.

## 트랙 블록

- 트랙: nl-task-chatbot · 단계: 2
- 답한 질문 id: q2-03

### 새 질문

| 제안 id | 질문 | 보낼 단계 | 근거 finding |
|---|---|---|---|
| — | 물류 지시 평가 자료를 자체 구축할 때 지시–정답 쌍의 정답을 무엇(업무 분해·배정 설계 초안의 작업 모델 인스턴스, 최종 상태·목표 조건, 배정 결과)으로 두고, ALFRED 목표 조건·SMART-LLM 최종 상태·AmbiK 명확화 질문 형식을 화물·로케이션·기한 항목으로 어떻게 확장하는가? (q2-03 에서 파생) | 5 | f16 |
| — | 배정 적합성을 평가하려면 목표 상태 달성 외에 정답 배정이나 목적함수 기준값이 필요한데, 이를 최적화 해법기(MILP 등)로 생성해 LLM 배정 결과와 비교하는 정답으로 쓸 수 있는가? (q2-03 에서 파생) | 5 | f17 |

### 온톨로지 초안 변경 제안

- 없음

### 단계 완료 조건 자체 평가

- 충족 여부(자체 평가): 미충족
- 못 채운 조건:
    - 아이디어 2. 자연어 업무 지시 챗봇 4절에 평가 데이터 소절은 이번 제안 검증 승인 전
    - 작업 모델 정보 항목 일부 미반영(작업 요구 적재물 속성·업무 완료 조건 미확정)
    - 열린 질문 q2-04, q2-05, q2-06, q2-07
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
…(발췌: 전체 202,769자 중 앞 49,491자)
```

### data/source_texts/ref-031.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

````text
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

- Safety Requirements: This document does not define functional, operational, or system safety requirements and shall not be regarded or applied as a safety standard.
- Traffic Management Logic: Strategies, algorithms, or decision making processes for traffic coordination (e.g., routing, prioritization, congestion handling, or deadlock resolution) are not included.
- Other Communication Interfaces: Interfaces unrelated to the communication between a fleet control system and mobile robots are excluded, such as interfaces to peripheral equipment, infrastructure components, or external IT systems.
- Project Coordination and Implementation Procedures: Project management activities, integration methodologies, commissioning workflows, validation and acceptance procedures, and similar organizational processes are not covered.
- Operational Responsibilities: This document does not allocate responsibilities among operators, system integrators, vehicle manufacturers, or fleet control providers with respect to planning, operation, maintenance, or safety.
- Cybersecurity Measures: Mechanisms, technologies, or processes for secure communication or data protection are not specified.

# 3 Definitions
The following terms and definitions apply for the purposes of this document. Terms that are not officially defined by standardization organizations may be interpreted differently in other contexts.

## 3.1 Mobile Robot
A driverless system for material transport primarily in operational settings, controlled by automation independently of their level of autonomy [Source ISO 3691-4]

## 3.2 Moving
State in which a mobile robot or any of its components undergoes a change in spatial position or orientation, including movement of wheels, load handling devices, or the robot body.

## 3.3 Driving
Operating state in which the mobile robot has a non zero translational and/or rotational velocity.

## 3.4 Automatic driving
Driving state in which the mobile robot operates without human intervention.

## 3.5 Manual driving
Driving state in which the mobile robot operates under direct human control.

## 3.6 Line-guided mobile robot
Mobile robots that follow predefined trajectories. Predefined trajectories are sent by fleet control as part of the order or defined on the robot, either explicitly or implicitly as the direct connection between nodes.

## 3.7 Freely navigating mobile robot
Mobile robots that plan their own trajectories. If fleet control sends a trajectory within the order, the robot shall follow this trajectory.

# 4 Transport protocol

Communication is expected to be done via wireless networks, considering the effects of connection failures and potential loss of messages.

The message protocol is Message Queuing Telemetry Transport (MQTT), which is to be used in combination with a JSON format.
MQTT 3.1.1 is the minimum required version for compatibility.
MQTT allows the distribution of messages to subchannels, which are called "topics".
Participants in the MQTT network subscribe to these topics and receive information that concerns them.

The JSON format allows for future extensions of the protocol with additional parameters as well as validation against schemas.

### 4.1 Connection handling, security and QoS

The MQTT protocol provides the option of setting a last will message for a client.
If the client disconnects unexpectedly for any reason, the last will is distributed by the broker to other subscribed clients.
The use of this feature is described in Section [6.5 Connection](#65-connection).

If the mobile robot disconnects from the broker, it keeps all the order information and fulfills the order up to the last released node.

To reduce the communication overhead, the MQTT QoS level 0 (Best Effort) shall be used for the topics `order`, `instantActions`, `state`, `factsheet`, `zoneSet`, `responses` and `visualization`. QoS level 1 (At Least Once) shall be used for the topic `connection`.

Protocol security needs to be taken into account by broker configuration, but is not addressed within this guideline.

### 4.2 Topic levels

The MQTT topic structure is not strictly defined due to the mandatory topic structure of cloud providers.
For a cloud-based MQTT broker the topic structure might have to be adapted individually, but it should roughly follow the proposed structure.
The topic names defined in the following sections are mandatory.

For a local broker the MQTT topic levels are suggested as followed:

**interfaceName/majorVersion/manufacturer/serialNumber/topic**

Example:
```
vda5050/v3/KIT/0001/order
```

MQTT Topic Level | Data type | Description
---|---|---
interfaceName | string | Name of the used interface
majorVersion | string | Major version number of the VDA 5050 recommendation, preceded by "v"
manufacturer | string | Manufacturer of the mobile robot.
serialNumber | string | Unique mobile robot serial number consisting of the following characters: <br>A-Z <br>a-z <br>0-9 <br>_ <br>. <br>: <br>-
topic | string | Topic (e.g., order or state) see Section [4.4 Topics for Communication](#43-topics-for-communication)

>Table 1 Explanation of suggested MQTT topic levels

Since the `/` character is used to define topic hierarchies, it shall not be used in any of the aforementioned fields.
Wildcard characters `+` and `#` as well as the character `$` that is reserved for broker internal topics should not be used either.

### 4.3 Topics for communication

The protocol uses the following topics for information exchange between fleet control and mobile robots.

Topic name | Published by | Subscribed by | Used for | Implementation | Schema
---|---|---|---|---|---
order | fleet control | mobile robot | Communication of orders | mandatory | order.schema
instantActions | fleet control | mobile robot | Communication of the actions that are to be executed immediately | mandatory | instantActions.schema
state | mobile robot | fleet control | Communication of the mobile robot state | mandatory | state.schema
visualization | mobile robot | visualization systems | High frequency communication of position and planned path | optional | visualization.schema
connection | broker / mobile robot | fleet control | Indicates when mobile robot connection is lost. Not to be used by fleet control for checking the mobile robot health, added for an MQTT protocol level check of connection | mandatory | connection.schema
factsheet | mobile robot | fleet control | Parameters or vendor-specific information to assist set-up of the mobile robot in fleet control | mandatory | factsheet.schema
zoneSet | fleet control | mobile robot | Transfer of zone sets from fleet control to the mobile robot | optional | zoneSet.schema
responses | fleet control | mobile robot | Fleet control's responses to requests from within the mobile robot's state | optional | responses.schema

>Table 2 Topics for communication between fleet control and mobile robot

# 5 Process and content of communication

## 5.1 General

There are at least the following participants for the operation of driverless transport system:

- The operator of the DTS provides basic information
- The fleet control organizes and manages the operation
- The mobile robot carries out the orders

Figure 1 describes the communication content during the operational phase.
During implementation or modification, the mobile robot and the fleet control are manually configured.

![Figure 1 Structure of the information flow](./assets/information_flow_VDA5050.png)
>Figure 1 - Structure of the information flow

## 5.2 Implementation Phase

During the implementation phase, the DTS consisting of fleet control and mobile robots is set up.
The necessary framework conditions are defined by the operator and the required information is either entered manually by them or stored in the fleet control by importing from other systems.
Essentially, this concerns the following content:

- Definition of routes:
Using the Layout Interchange Format (LIF), routes can be imported to the fleet control. The LIF is a file format of track layouts for exchange between the integrator of the driverless transport mobile robots and a (third-party) fleet control system (LIF – Layout Interchange Format, VDMA 2024-03).
Alternatively, routes can also be implemented manually in the fleet control by the operator.
Routes can be one-way streets, restricted for certain mobile robot groups (based on the size ratios), etc.
- Route network configuration:
Within the routes, stations for loading and unloading, battery charging stations, peripheral environments (gates, elevators, barriers), waiting positions, buffer stations, etc. are defined.
- Mobile robot configuration: The physical properties of a mobile robot (size, available load carrier mounts, etc.) are stored by the operator.
The mobile robot shall communicate this information via the topic `factsheet` in a specific way that is defined in Section [7.10 Implementation of the factsheet message](#710-implementation-of-the-factsheet-message) of this document.

The configuration of routes and the route network described above are not part of this document.
They form the basis for enabling order control and driving course assignment by the fleet control based on this information and the transport requirements to be completed.
The resulting orders to be executed by the robotic fleet are transferred to the individual mobile robots via MQTT.
The mobile robot then continuously reports its status to the fleet control in parallel with the execution of the order, also using MQTT.

## 5.3 Functions of the fleet control

The fleet control system performs, at minimum, the following functions:

- Assignment of orders to the mobile robots
- Route calculation and guidance of line-guided mobile robots (taking into account the limitations of the individual physical properties of each mobile robot, e.g., size, maneuverability, etc.)
- Detection and resolution of blockages ("deadlocks")
- Energy management: Charging orders can interrupt transfer orders
- Traffic control: Buffer routes and waiting positions
- (Temporary) changes in the environment, such as freeing certain areas or changing the maximum speed
- Communication with peripheral systems such as doors, gates, elevators, etc.
- Detection and resolution of communication errors

## 5.4 Functions of the mobile robots

Each mobile robot shall perform the following functions:

- Localization
- Execution of associated routes (line-guided or freely navigating)
- Execution of actions
- Continuous transmission of its status

# 6 Protocol specification

The following section describes the details of the communication protocol.
The protocol specifies the communication between the fleet control and the mobile robot.

## 6.1 Order

The topic `order` is the MQTT topic via which the mobile robot receives an order, containing instructions for the robot to move or execute actions.

### 6.1.1 Concept and logic

The core of a transport order is a node-edge-graph segment defining the route to be travelled.
The mobile robot is expected to traverse the nodes and edges to fulfill the order.
The full graph of all connected nodes and edges is held by fleet control. It may contain restrictions, e.g., which mobile robot is allowed to traverse which edge.
These restrictions will not be communicated to the mobile robot.
The fleet control only includes edges in an order which the concerning mobile robot is allowed to traverse.

![Figure 2 Graph representation in fleet control and graph transmitted in orders](./assets/graph_representation_transmission.png)
>Figure 2 - Graph representation in fleet control and graph transmitted in orders

The nodes and edges are passed as two lists in the order message.
The order of the nodes and edges within those lists also governs the sequence in which the nodes and edges shall be traversed. The 'sequenceId' is shared between nodes and edges and defines the sequence of traversal. The first node has a `sequenceId` of 0, the first edge has a `sequenceId` of 1, the second node has a `sequenceId` of 2, etc. An edge with `sequenceId` n connects the nodes with `sequenceId` n-1 and n+1. The `sequenceId` shall be continuous within an order.

For a valid order, there shall be at least one node and the number of edges shall be equal to the number of nodes minus one.

The first node of an order (`sequenceId` = 0) shall be trivially reachable for the mobile robot and always be released.
This means either that the mobile robot is already standing on the node, or that the mobile robot is in the node's deviation range. As such, the first node shall not be reported in the `nodeStates`.

Nodes and edges both have a boolean attribute `released`.
If a node or edge is released, the mobile robot is expected to traverse it.
If a node or edge is not released, the mobile robot shall not traverse it.

An edge can be released only if both the start and the end node of the edge are released.

After an unreleased edge, no released nodes or edges can follow in the sequence.

The set of released nodes and edges are called the "base".
The set of unreleased nodes and edges are called the "horizon".

It is valid to send an order without a horizon.

An order message does not necessarily describe the full transport order.
For traffic control and to accommodate resource constrained mobile robots, the full transport order (which might consist of many nodes and edges) can be split up into many sub-orders, which are connected via their `orderId` and `orderUpdateId`.
The process of updating an order is described in the next section.

### 6.1.2 Orders and order update

To support traffic management, fleet control can split the path communicated via order into two parts:

- *"Base"*: This is the defined route that the mobile robot is allowed to travel. All nodes and edges of the base route have already been released by the fleet control for the mobile robot. The last node of the base is called decision point.
- *"Horizon"*: This is the route currently planned by fleet control for the mobile robot to travel after the decision point. The horizon route has not yet been released by the fleet control.

The mobile robot shall stop at the decision point if no further nodes and edges are added to the base. In order to ensure a fluent movement, the fleet control should extend the base before the mobile robot reaches the decision point, if the traffic situation allows for it.

Since MQTT is an asynchronous protocol and transmission via wireless networks is not reliable, the base cannot be changed. The fleet control shall therefore assume that the base has already been executed by the mobile robot. A later section describes a procedure to cancel an order, but this is also considered unreliable due to the communication limitations mentioned above.

The fleet control can change the horizon by sending an updated route to the mobile robot which includes the changed list of nodes and edges. The procedure for changing the horizon route is shown in Figure 3.

![Figure 3 Procedure for changing the driving route "Horizon"](./assets/driving_route_horizon.png)
>Figure 3 - Procedure for expanding the driving route "Horizon"

In Figure 3, an initial order is first sent by the fleet control at time t = 0.
Figure 4 shows the pseudocode of a possible order.
For the sake of readability, a complete JSON example has been omitted here.

```
{
	orderId: "1234",
	orderUpdateId:0,
	nodes: [
	 	 f {released: true},
	 	 d {released: true},
	 	 g {released: true},
	 	 b {released: false},
	 	 h {released: false}
	],
	edges: [
		e1 {released: true},
		e3 {released: true},
		e8 {released: false},
		e9 {released: false}
	]
}
```
>Figure 4 Pseudocode of an order.

At a later point in time, the order is extended by sending an order update (see pseudocode in Figure 5).
Note that the `orderUpdateId` is incremented and that the first node of the order update corresponds to the last base node of the previous order message, the stitching node. The other nodes and edges from the previous base are not resent.

This ensures that the mobile robot can also perform the order update, i.e., that the first node of the order update is reachable by executing the edges already known to the mobile robot.

```
{
	orderId: "1234",
	orderUpdateId: 1,
	nodes: [
		g {released: true},
		b {released: true},
		h {released: true},
		i {released: false}
	],
	edges: [
		e8 {released: true},
		e9 {released: true},
		e10 {released: false}
	]
}
```
>Figure 5 Pseudocode of an order update. Note the change of the `orderUpdateId`.

This also aids in the event that an order update is lost (e.g., due to an unreliable wireless network).
The mobile robot can always check that the last known base node has the same `nodeId` (and `sequenceId`) as the first node of a new order update.

Also note that node g is the only base node that is sent again.
Since the base cannot be changed, a retransmission of nodes f and d is not valid.

![Figure 6 Regular update process - order extension](./assets/update_order_extension.png)
>Figure 6 - Regular update process - order extension.

Figure 6 describes how an order should be extended.
It shows the information that is currently available on the mobile robot.
The `orderId` stays the same and the `orderUpdateId` is incremented.

It is important that the contents of the decision point (node g in Figure 6) are not changed. This means actions, deviation range, etc., shall be resent (see Figure 7, `orderUpdateId` 1).
In order to release actions for the mobile robot to execute on a node it is already positioned on through an order update, the fleet control shall re-send this node once with all meta-data (including potentially already 'FINISHED'/'RUNNING' actions) from the previous order update, which will not be executed again by the mobile robot, and then add a node with the now newly released actions to be executed with this order update. This node can have the same `nodeId` as the decision node or a different `nodeId` but the same position as the decision node. The `sequenceId` of the new node is always the `sequenceId` of the decision node plus 2.

![Figure 7 Order update with additional stitching node.](./assets/update_order_stitching_node.png)
>Figure 7 - Order update with additional stitching node (e.g., to execute new actions on decision point)

The horizon may be modified or deleted entirely with any order update, or the base may be extended in a way different from the previous horizon.

Once a `sequenceId` is assigned and the node is released, it does not change with order updates (see Figure 6).

Figure 8 describes the process of accepting an order or order update.

![Figure 8 The process of accepting an order or orderUpdate](./assets/process_order_update.png)
>Figure 8 - The process of accepting an order or order update.

1) **Is received order valid?**:
All formatting and JSON data types are correct?

2) **Is received order new or an update of the current order?**:
Is `orderId` of the received order different to `orderId` of order the mobile robot currently holds?

3) **Is mobile robot idle and not waiting for an update?**:
Is the mobile robot in an idle state according to [6.6.8 Idle state of the mobile robot](#668-idle-state-of-the-mobile-robot) and not waiting for an update? Since nodes and edges and the corresponding action states of the order horizon are also included inside the state, the mobile robot might still have a horizon and therefore is waiting for an update and executing an order.

4) **Is OrderUpdateId 0?**: Is the `orderUpdateId` of the new order 0?

5) **Is start of new order close enough to current position?**:	Is the mobile robot already standing on the node, or is it in the node's deviation range ([6.1.1 Concept and logic](#611-concept-and-logic))?

6) **Is received order update deprecated?**: Is `orderUpdateId` less than or equal to one currently on the mobile robot?

7) **Is order update following cancelOrder?**: No further order updates to the cancelled order shall be sent by the fleet control or accepted by the mobile robot.

8) **Is received order update currently on mobile robot?**: Is `orderUpdateId` equal to the one currently on the mobile robot?

9) **Is the received update a valid continuation of the currently still running order?**:	Is the first node of the received order the current decision point according to the order update chapter? The mobile robot is still moving or executing actions related to the base released in previous order updates or still has a horizon and is therefore waiting for a continuation of the order. In this case, the order update is only accepted if the first node of the new base is equal to the last node of the previous base.

10) **Is the received update a valid continuation of the previously completed order?**: Is the first node of the received order the current decision point according to the order update chapter? The mobile robot is not executing any actions anymore neither is it waiting for a continuation of the order (meaning that it has completed its base with all related actions and does not have a horizon). In this case, the order update is only accepted if the first node of the new base is equal to the last node of the previous base.

11) **Populate/append** new states to the `actionStates`/`nodeStates`/`edgeStates`.

#### 6.1.2.1 Finishing an order

After the mobile robot has traversed the last node of an order and has finished all order related movement and actions, it is idle and shall be ready to receive a new order (see [6.6.8 Idle state of the mobile robot](#668-idle-state-of-the-mobile-robot)).

### 6.1.3 Order cancellation

Fleet control can cancel an active order using the instantAction `cancelOrder`.

Fleet control can optionally pass an `orderId` to reference which order shall be canceled.
After receiving the instantAction `cancelOrder`, the mobile robot shall attempt to stop as soon as possible.
For line-guided mobile robots, this could be the next feasible node. A freely navigating mobile robot shall stop as soon as possible, not merely at the next node.

If there are actions in the `actionStates` scheduled, these actions shall be cancelled and report 'FAILED' in their `actionState`.
If there are actions in the `actionStates` running, those actions should be cancelled and also be reported as 'FAILED'.
If the action cannot be cancelled, the `actionState` of that action should reflect that by reporting 'RUNNING' while it is running, and after that the respective state ('FINISHED', if successful and 'FAILED', if not).
While there are running actions in the `actionStates`, the cancelOrder action shall report 'RUNNING' until all actions are cancelled/finished. Actions that cannot be cancelled (cancelAllowed = false) shall be finished.
After all movement of the mobile robot and all of the actions in the `actionStates` are stopped, the `cancelOrder` action status shall report 'FINISHED'.
The mobile robot shall then be idle and ready to receive new orders.

The `orderId` and `orderUpdateId` are kept.

Figure 9 shows the expected behavior for different mobile robot capabilities.

![Figure 9 Expected behavior after a cancelOrder](./assets/process_cancel_order.png)
>Figure 9 - Expected behavior after a `cancelOrder`.

#### 6.1.3.1 Receiving a new order after cancellation

After the cancellation of an order, the mobile robot is idle and shall be ready to receive a new order. No further order updates to the cancelled order shall be sent by the fleet control. If the mobile robot receives an order update it shall report an error of type 'ORDER_UPDATE_FOLLOWING_CANCEL' and level 'WARNING'.

In the case of a mobile robot that can only localize itself on a node, the new order shall begin on the node the mobile robot is now standing on (see also Figure 4).

In case of a mobile robot that can stop in between nodes, fleet control can decide how to start the next order.
The mobile robot shall accept both methods.

There are two options:

- The first node of the new order is a temporary node that is positioned at the mobile robot's current position. The mobile robot shall then recognize that this node is trivially reachable and accept the order.
- The first node of the new order is the last traversed node of the previous order. The allowed deviation of this node is set large enough to ensure that the mobile robot is within this range. Thus, the mobile robot shall immediately treat this node as traversed and accept the order.

#### 6.1.3.2 Receiving a cancelOrder action when mobile robot is idle

If the mobile robot receives a `cancelOrder` instant action but the mobile robot is currently idle, or the `orderId` specified in the action does not match the `orderId` of the mobile robot’s currently active order, the `cancelOrder` action shall be reported as 'FAILED'.

The mobile robot shall report an error of type 'NO_ORDER_TO_CANCEL' with the level set to 'WARNING'. The `actionId` of the `instantAction` shall be passed as an `errorReference`.

### 6.1.4 Order rejection

There are several scenarios, when an order shall be rejected.
These scenarios are shown in Figure 8 and described below.

#### 6.1.4.1 Mobile robot receives a malformed order

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'VALIDATION_FAILURE' and level 'WARNING‘
3. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.2 Mobile robot receives an order with optional fields it cannot use

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer
2. The mobile robot shall report an error of type 'UNSUPPORTED_PARAMETER' with level 'CRITICAL' and the erroneous fields as errorReferences
3. The error shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.3 Mobile robot receives an order with actions it cannot perform

Example:

- lifting height higher than maximum lifting height
- lifting actions although no stroke is installed, etc.

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer
2. The mobile robot shall report an error of type 'INVALID_ORDER_ACTION' with level 'WARNING' and the erroneous fields as errorReferences
3. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.4 Mobile robot receives an order with the same orderId, but a lower orderUpdateId than the current orderUpdateId

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall keep the previous order in its buffer.
3. The mobile robot shall report an error of type 'OUTDATED_ORDER_UPDATE' and level 'WARNING'.
4. The mobile robot shall continue with executing the previous order.
5. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.5 Mobile robot receives an order with the same orderId and same orderUpdateId as the current orderUpdateId

Example:

- Fleet control resends the order because it did not yet receive any state message with the respective `orderUpdateId`.

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall keep the previous order in its buffer.
3. Reporting depends on the content of the message:
	- If the content of the new order is the same as the content of the previous one, the mobile robot shall ignore the new order.
	- If the content of the new order differs, the mobile robot shall report an error of type 'SAME_ORDER_UPDATE_ID' and level 'WARNING'.
4. The mobile robot shall continue with executing the previous order.
5. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.6 Mobile robot receives an order with orderId different to the orderId of an active order

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot keeps the previous order in its buffer.
3. The mobile robot shall report an error of type 'OTHER_ORDER_ACTIVE' and level 'WARNING'.
4. The mobile robot shall continue with executing the previous order.
5. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.7 Mobile robot receives an order with the start node being out of range

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'START_NODE_OUT_OF_RANGE' and level 'WARNING'.
3. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.8 Mobile robot receives an order with at least one node not being reachable

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'NO_ROUTE_TO_TARGET' and level 'WARNING'.
3. The warning shall be reported until the mobile robot has accepted a new order.

#### 6.1.4.9 Mobile robot receives an order while in an operating mode that does not allow new orders

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'MOBILE_ROBOT_NOT_AVAILABLE' and level 'WARNING'.
3. The warning shall be reported until the mobile robot is in an order mode that allows for new orders.

#### 6.1.4.10 Mobile robot receives an order containing nodes with unknown mapId

Resolution:

1. The mobile robot shall not take over the new order in its internal buffer.
2. The mobile robot shall report an error of type 'UNKNOWN_MAP_ID' and level 'WARNING'.
3. The warning shall be reported until the mobile robot has accepted a new order.

### 6.1.5 Corridors

The optional `corridor` edge attribute allows the mobile robot to deviate from the edge trajectory for obstacle avoidance and defines the boundaries within which the mobile robot is allowed to operate.
To use the `corridor` attribute, a predefined trajectory is required that the mobile robot would follow if no `corridor` attribute was defined. This can be either the trajectory defined on the mobile robot known to the fleet control or the trajectory sent in an order. The behavior of a mobile robot using the `corridor` attribute is still the behavior of a line-guided mobile robot, except that it is allowed to temporarily deviate from a trajectory to avoid obstacles.
Note that a corridor communicated within an order is released for the mobile robot by default. If the `releaseRequired` flag is set to true, the mobile robot shall request approval from fleet control before using the corridor as described in chapter [6.6.10 Request use of Corridors](#6610-request-use-of-corridors).

*Remark:
An edge inside an order defines a logical connection between two nodes and not necessarily the (real) trajectory that a mobile robot follows when driving from the start node to the end node.
Depending on the mobile robot type, the trajectory that a mobile robot takes between the start and end nodes is either defined by fleet control via the trajectory edge attribute or assigned to the mobile robot as a predefined trajectory.
Depending on the internal state of the mobile robot, the selected trajectory may vary.*

![Figure 10 Edges with corridor attribute.](./assets/edges_with_corridors.png)
>Figure 10 - Edges with a `corridor` attribute that defines the left and right boundaries within which a mobile robot is allowed to deviate from its predefined trajectory to avoid obstacles. On the left, the kinematic center defines the allowed deviation, while on the right, the contour of the mobile robot, possibly extended by the load, defines the allowed deviation. This is defined by the `corridorReferencePoint` parameter.
The area in which the mobile robot is allowed to navigate independently (and deviate from the original edge trajectory) is defined by a left and a right boundary.
The optional `corridorReferencePoint` field specifies whether the mobile robot control point or the mobile robot contour should be inside the defined boundary.
The boundaries of the edges shall be defined in such a way that the mobile robot is inside the boundaries of the new and now current edge as soon as it passes a node.
Instead of setting the corridor boundaries to zero, fleet control shall not use the `corridor` attribute if the mobile robot shall not deviate from the trajectory.

The mobile robot's motion control software shall constantly check that the mobile robot is within the defined boundaries.
If not, the mobile robot shall stop because it is out of the allowed navigation space and report an error of type 'OUTSIDE_OF_CORRIDOR' with level 'CRITICAL'.
The fleet control can decide if user interaction is required or if the mobile robot can continue by canceling the current order and sending a new order to the mobile robot with corridor information that allows the mobile robot to move again.

*Remark: Allowing the mobile robot to deviate from the trajectory increases the possible footprint of the mobile robot during driving. This circumstance shall be considered during initial operation, and when the fleet control makes a traffic control decision based on the mobile robot's footprint.*
See also Section [6.6.2 Traversal of nodes and edges](#662-traversal-of-nodes-and-edges) for further information.

## 6.2 Actions

If the mobile robot supports actions other than driving, these actions are instructed via the `actions` array that is attached to a node or an edge, sent via the separate topic `instantActions` (see section [6.2.1 Instant actions](#621-instant-actions)) or configured via action zones (see section [6.4.1 Zone types](#641-zone-types)).
Actions that are to be executed on an edge shall only run while the mobile robot is on the edge (see Section [6.6.2 Traversal of nodes and entering/leaving edges, triggering of actions](#662-traversal-of-nodes-and-enteringleaving-edges-triggering-of-actions)).

Actions that are triggered on nodes can run as long as they need to run and should be self-terminating (e.g., an audio signal that lasts for five seconds or a pick action, that is finished after picking up a load) or formulated pairwise (e.g., "activateWarningLights" and "deactivateWarningLights").

### 6.2.1 Instant Actions

In certain cases, it is necessary to send actions to the mobile robot that need to be performed immediately.
This is possible by publishing an `instantAction` message to the topic `instantActions`.
These actions shall not conflict with the content of the mobile robot's current order (e.g., `instantAction` to lower fork, while order says to raise fork).

Some examples for which instant actions could be relevant are:

- pause the mobile robot without changing anything in the current order
- resume order after pause
- activate signal (optical, audio, etc.)

When a mobile robot receives an `instantAction`, an appropriate `actionStatus` shall be added to the `instantActionStates` array of the mobile robot's state.
The `actionStatus` shall be updated according to the progress of the action.
See also Figure 11 for the different transitions of an `actionStatus`.
The `blockingType` of an instant action is always 'NONE'.

When the mobile robot receives an `instantAction` it cannot execute, it shall report an 'INVALID_INSTANT_ACTION' error with level 'WARNING' and the `actionId` of the `instantAction` as `errorReference`.

### 6.2.2 Action blocking types and sequence

The order of multiple actions in a list defines the sequence in which the mobile robot shall execute them.

The parallel execution of actions is governed by their respective `blockingType`.
Actions can have four distinct blocking types, described in Table 3.

-| Parallel execution allowed | Parallel execution not allowed
---|---|---
Automatic driving allowed | NONE | SINGLE
Automatic driving not allowed | SOFT | HARD

>Table 3 Definition of action blocking types dependent on driving and parallel execution

Figure 11 describes how the mobile robot shall handle the blocking type of actions. Whenever the mobile robot arrives at a point where new actions are to be executed (i.e., when it reaches a node, edge, or action zone), the actions are enqueued in the same sequence as the actions array. This queue is continually processed as shown in Figure 11. If the blocking type of any action in the queue is 'SOFT' or 'HARD', the mobile robot shall stop automatic driving. Actions are collected for parallel execution if the action's blocking type is 'NONE' or 'SOFT'. If an action with blocking type 'SINGLE' or 'HARD' is to be executed, all collected parallel actions shall be 'FINISHED' or 'FAILED' before starting the action. If there are no more actions with blocking type 'SOFT' or 'HARD' in the queue, the mobile robot can resume automatic driving. 'FINISHED' or 'FAILED' actions shall be removed from the queue.

![Figure 11 Handling multiple actions](./assets/handling_multiple_actions.png)
>Figure 11 - Handling multiple actions

### 6.2.3 Predefined Actions

This section presents predefined actions that shall be used by the mobile robot, if the mobile robot's capabilities map to the action description.
If there is a sensible way to use the defined parameters, they shall be used.
Additional parameters can be defined, if they are needed to execute an action successfully.
The actions `cancelOrder`, `startPause` and `stopPause` shall be supported by every mobile robot.

If there is no way to map some action to one of the actions of the following section, the mobile robot manufacturer can define additional actions that shall be used by fleet control.

#### 6.2.3.1 Definition, parameters, effects and scope
…(발췌: 전체 207,642자 중 앞 48,820자)
````
