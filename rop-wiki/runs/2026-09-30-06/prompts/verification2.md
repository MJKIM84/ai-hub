(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-30-06
- date: 2026-09-30
- run_type: area_deep_dive (영역 심화)
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

## 입력

### runs/2026-09-30-06/target.json

```json
{
  "run_id": "2026-09-30-06",
  "date": "2026-09-30",
  "weekday": "Wed",
  "run_number": 115,
  "run_type": "area_deep_dive",
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=43"
}
```

### runs/2026-09-30-06/research.json

```json
{
  "run_id": "2026-09-30-06",
  "date": "2026-09-30",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 43,
    "area_name": "43. 데이터·관측성·배포",
    "category": "K. 플랫폼 아키텍처·인프라"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 관측성, OpenTelemetry, MCAP, FinOps·FOCUS, A/B 분할 업데이트 용어 없음",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 병원(운영 로그 기반 실패 분석)·물류창고(배포 전 시뮬레이션 검증) 사례와 여섯 항목 정리 없음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 기록 형식, 추적·지표·로그 수집, 컨테이너 오케스트레이션, 이미지 기반 무선 업데이트와 롤백, 비용 계측 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — rosbag2·MCAP, ros2_tracing, OpenTelemetry, Mender, FOCUS 위치 없음",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 0건",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "플랫폼 자체의 상태·데이터·배포·비용을 어떻게 관리할 것인가? [분류원문]",
    "로봇·플랫폼의 로그·이벤트·텔레메트리를 기록·저장하는 형식과 도구(rosbag2·MCAP, 플랫폼 기록 DB)는 무엇이며, 보존 기간을 정하는 국내 규제 근거는 무엇인가? (섹션 4·6·7 겨냥, 한국 자료 우선)",
    "플랫폼 관측성을 구현하는 표준·오픈소스(OpenTelemetry, ros2_tracing, 커널 기반 관찰)는 무엇이며 관찰 자체의 성능 부담은 얼마로 보고되는가? (섹션 6·7·8 겨냥)",
    "현장 서버·로봇·클라우드에 플랫폼 소프트웨어를 배포하고 되돌리는 방법(컨테이너 오케스트레이션, 이미지 기반 무선 업데이트와 롤백, 배포 전 시뮬레이션 검증)은 무엇이며 어떤 결과가 보고되는가? (섹션 6·7·8 겨냥)",
    "클라우드와 언어 모델 호출 비용을 측정·할당·관리하는 기준(FinOps 주기, FOCUS 청구 데이터 명세, OpenTelemetry 생성형 AI 토큰 지표)은 무엇인가? (섹션 4·6·7 겨냥)",
    "병원·물류창고 등 현장에서 운영 데이터를 수집해 실패 원인을 분석하거나 소프트웨어 변경을 배포 전에 검증한 사례는 무엇인가? (섹션 5 겨냥)",
    "데이터·관측성·배포에서 ROP가 직접 맡을 것과 로봇 제조사·클라우드 사업자·법규에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "Bédard·Lütkebohle·Dagenais 의 ros2_tracing(IEEE RA-L 7(3), 2022-07)은 저부하 추적기 LTTng 를 써서 ROS 2 의 실행 정보를 수집하는 계측·추적 도구 모음으로, ROS 2 추적 데이터를 운영체제 추적과 결합할 수 있고, ROS 2 계측을 모두 켰을 때 종단 간 메시지 지연 증가가 평균 0.0033 ms 라고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1038"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록 기준: LTTng 기반 ROS 2 계측, OS 추적과 결합, 모든 ROS 2 계측 활성화 시 종단 간 메시지 지연 오버헤드 평균 0.0033 ms. 실험 조건은 본문 미확인.",
      "as_of": "2022-07",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "ros2_tracing 저자들은 미들웨어 수준의 표준 데이터 기록만으로는 내부 계산과 성능 병목에 관한 정보가 충분하지 않다고 보고, 이를 실행 추적 도구가 필요한 이유로 든다.",
      "tag": "사실",
      "source_ids": [
        "ref-1038"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"standard, middleware-based data recording does not provide sufficient information on internal computation and performance bottlenecks\"",
      "as_of": "2022-07",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "Yu·Lee·Choi·Park 의 ros2probe(arXiv 2606.10746, 2026-06)는 ROS 2 도메인에 구독자로 참여하는 관찰 도구가 탐색(discovery) 부담과 역직렬화 비용을 더해 관찰 대상을 교란한다고 보고, 탐색 패킷으로 통신 그래프를 복원한 뒤 사용자가 지정한 토픽만 커널 안에서 걸러 관찰하는 방식으로 관찰자 CPU 사용을 최대 7배·메모리를 최대 28배 줄이고, 포화 조건에서 도메인 참여형 도구가 38.5% 메시지를 잃을 때 메시지 손실 0을 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1039"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록 기준: 탐색 그래프 유지 부담 0.5% 이내, 관찰자 CPU 최대 7배·메모리 최대 28배 감소, 패킷 손실 탐지 재현율 1.0, 포화 시 손실 0 대 도메인 참여 도구 38.5%. 프리프린트.",
      "as_of": "2026-06",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "ROS 2 Iron Irwini(2023-05-23 출시)부터 rosbag2 가 새 백 파일을 기록하는 기본 형식을 sqlite3 에서 MCAP 로 바꿨고, 같은 판에서 서비스 호출로 원격에서 기록을 일시 정지·재개·분할하는 기능이 더해졌다.",
      "tag": "사실",
      "source_ids": [
        "ref-1040",
        "ref-1041"
      ],
      "cross_checked": true,
      "confidence": "high",
      "evidence_excerpt": "ROS 2 공식 문서 Iron 릴리스 노트: \"This release switches to using `mcap` as the default file format for writing new bags.\" Foxglove 블로그(2022-12-22)도 Iron 부터 MCAP 기본값을 알림.",
      "as_of": "2023-05-23",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "Foxglove 는 MCAP 이 SQLite3 의 '복원력' 모드 수준의 데이터 안전성과 '쓰기 최적화' 모드 수준의 쓰기 처리량을 함께 제공하고, zstd·lz4 압축을 고를 수 있으며, 메시지 정의를 파일 안에 담아 외부 스키마 없이 다른 도구가 읽을 수 있다고 주장한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1041"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: SQLite3 resilient 모드의 안전성과 write optimized 모드의 처리량을 함께 제공, zstd·lz4 압축 선택, 메시지 정의 내장으로 Foxglove·PlotJuggler 연동.",
      "as_of": "2022-12-22",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f6",
      "claim": "OpenTelemetry 명세 상태 요약에 따르면 추적(tracing)은 API·SDK·프로토콜이 모두 안정(stable)이고 장기 지원 대상이며, 로그는 브리지 API·SDK·프로토콜이 안정, 지표(metrics)는 API·프로토콜이 안정이나 SDK 는 혼합 상태, 프로파일(profiles)은 프로토콜이 개발(development) 단계다.",
      "tag": "사실",
      "source_ids": [
        "ref-1042"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"The tracing specification is now completely stable, and covered by long term support.\" 로그·지표 데이터 모델은 OTLP 의 일부로 공개. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "OpenTelemetry 생성형 AI 의미 규약 저장소의 토큰 지표 문서는 입력·출력·캐시 읽기·캐시 쓰기 입력·추론 출력 토큰 카운터(gen_ai.client.inference.usage.*)와 호출별 입력·출력 토큰 히스토그램(gen_ai.client.inference.operation.*)을 정의하고, 작업 이름·제공자 이름을 필수 속성으로 두며, 모든 지표가 개발(Development) 단계다.",
      "tag": "사실",
      "source_ids": [
        "ref-1043"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "토큰 지표 7종(카운터 5, 히스토그램 2), 단위 {token}, 필수 속성 gen_ai.operation.name·gen_ai.provider.name(카운터는 gen_ai.token.modality 추가), 상태 Development. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "오픈소스 ros-opentelemetry 는 송신 측이 추적 문맥을 ROS 2 메시지의 사용자 정의 필드에 넣고 수신 측이 꺼내 이어 붙이는 방식으로 토픽·서비스·액션을 가로지르는 분산 추적을 C++·Python 노드에 제공하고, 로그를 추적 구간(span)에 연결하는 로거를 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1044"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: inject_trace_context()/extract_trace_context() 로 메시지 간 추적 문맥 전파, C++(ament_cmake)·Python(ament_python) 패키지와 문맥 전파용 메시지 정의, traced logger. 라이선스 표기 미확인. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "Zhang·Yu·Westerlund(Sensors, 2025-08)는 TurtleBot4 에 얹은 Jetson Nano 5대를 작업 노드로, 노트북 1대를 마스터로 둔 K3s 클러스터에서 컨테이너화한 ROS 2 노드로 다중 로봇 UWB 상대 위치 추정을 운영했고, 오차 보정용 LSTM 파드 5개를 모두 종료시킨 경우에도 Kubernetes 가 파드를 자동 재시작해 위치 오차(APE)가 약 0.12~0.14 m 로 장애 없는 경우와 비슷하게 유지됐다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1045"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "K3s 기반 오케스트레이션, 장애 시나리오 F5(LSTM 파드 5개 종료)에서도 정확도 유지, LSTM 보정 없을 때 APE 0.66 m 이상. 복구 시간은 보고하지 않음. 실험실 환경.",
      "as_of": "2025-08-14",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f10",
      "claim": "연계 대상: 오픈소스 Mender 는 임베디드 리눅스·사물인터넷 장치용 클라이언트–서버 방식 무선(OTA) 업데이트 관리자로, 이중 A/B 루트 파일시스템 분할에 이미지 단위로 원자적 배포를 해 업데이트 중 전원이 끊겨도 동작하던 상태로 되돌릴 수 있게 하며, 루트 파일시스템·애플리케이션·파일·컨테이너 업데이트를 지원하고 Apache 2.0 라이선스로 공개된다.",
      "tag": "사실",
      "source_ids": [
        "ref-1046"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: \"atomic image-based deployments using a dual A/B rootfs partition layout\", 전원 상실 시에도 롤백, Update Modules 로 다른 구성 요소 확장. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f11",
      "claim": "개인정보보호위원회 「개인정보의 안전성 확보조치 기준」(고시 제2023-6호, 2023-09-22 시행) 제8조는 개인정보처리자가 개인정보취급자의 개인정보처리시스템 접속기록을 1년 이상(5만 명 이상의 정보주체 개인정보를 처리하는 시스템 등은 2년 이상) 보관·관리하고, 월 1회 이상 점검하며, 위조·변조·도난·분실되지 않도록 안전하게 보관하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-766"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제8조(접속기록의 보관 및 점검): 1년 이상 보관, 5만 명 이상 처리 시스템 등은 2년 이상, 월 1회 이상 점검, 위변조 방지. 5만 명 조건 문구는 검색 요약으로 보완.",
      "as_of": "2023-09-22",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f12",
      "claim": "FinOps 재단의 FinOps 프레임워크는 기술 비용·사용량·효율 데이터를 수집·배분·보고·예측하는 정보(Inform), 사용량 최적화와 요금 최적화를 찾는 최적화(Optimize), 엔지니어링·재무·사업 팀이 함께 개선을 실행하는 운영(Operate)의 세 단계를 반복하는 방식으로 설명하며, 대상 기술 범주에 공용 클라우드·SaaS 와 함께 AI 서비스를 든다.",
      "tag": "사실",
      "source_ids": [
        "ref-1048"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Inform: 데이터 수집·배분·보고·예측·단위 경제성 / Optimize: \"both usage optimization and rate optimization\" / Operate: 책임 문화와 지속 개선. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f13",
      "claim": "FinOps 재단의 청구 데이터 명세 FOCUS 1.2(2025-05-29 비준)는 SaaS·PaaS 청구 데이터를 클라우드 비용과 같은 스키마에 넣고, 크레딧·토큰 같은 가상 통화와 다중 통화 정규화(PricingCurrency 등), 청구서 연결용 InvoiceId 열을 더했으며, AWS·Microsoft·Google Cloud·Oracle Cloud·Alibaba Cloud·Databricks·Grafana 가 지원을 밝혔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1049"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "새 열 7개(InvoiceId, BillingAccountType, SubAccountType, PricingCurrency 외 3), 가상 통화로 토큰 기반 지출 분석 가능. (발행일 미확인, 확인일 기준)",
      "as_of": "2025-05-29",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f14",
      "claim": "Bruno·Sim·Hagiwara(arXiv 2609.29043, 2026-09)는 클라우드 언어 모델 API 는 로봇이 긴 작업을 반복할수록 요청당 비용이 쌓이고 네트워크 지연이 실시간 반응을 떨어뜨린다고 보고, 두 단계 연쇄(chaining) 계획으로 추론당 프롬프트 길이를 약 45% 줄여 로컬 모델(Qwen2.5-14B·Cogito-14B)의 계획 성공을 최대 37%p 높였으며 클라우드 모델(Claude Sonnet 4.6)과 함께 비교했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1051"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"Cloud APIs incur per-request cost that accumulates when a robot repeats long-horizon tasks\" RoboCup@Home GPSR 명령 100개 평가, Toyota HSR 실로봇 10개 중 6개 성공. 비용 금액은 보고하지 않음.",
      "as_of": "2026-09",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f15",
      "claim": "고려대학교 구로병원의 자율 약품 배송 로봇 실증(Lee 외, Digital Health, 2026-03)에서 배송 임무는 응급실 직원이 웹 애플리케이션으로 요청하면 시작됐다.",
      "tag": "사실",
      "source_ids": [
        "ref-943"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "비응급 임무 122건(2025-06-18~29, 평일·주말), 응급실 직원의 웹 앱 요청으로 임무 시작.",
      "as_of": "2026-03-31",
      "site_type": "병원",
      "flow_item": "시작 조건"
    },
    {
      "id": "f16",
      "claim": "같은 병원 실증은 로봇이 사람 개입 없이 전체 경로를 마치고 약품을 넘겨 간호사가 받는 것을 배송 성공으로 정의했다.",
      "tag": "사실",
      "source_ids": [
        "ref-943"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "성공 정의: 로봇이 전체 경로를 완료하고 사람 개입 없이 약품을 인계, 간호사가 수령.",
      "as_of": "2026-03-31",
      "site_type": "병원",
      "flow_item": "완료·인계"
    },
    {
      "id": "f17",
      "claim": "같은 병원 실증은 승강기 호출·탑승·문 동작·하차 시각을 1 Hz 로 남긴 로봇 시스템 로그, 승강기 상태·문·위치·로봇 명령을 담은 승강기 통신 로그, 관찰자가 적은 수기 기록지(탑승객·화물·결과)를 함께 모아 분석했다.",
      "tag": "사실",
      "source_ids": [
        "ref-943"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "자료원 3종: 로봇 시스템 로그(1 Hz 타임스탬프), 승강기 통신 로그, 훈련된 관찰자의 사례 기록지.",
      "as_of": "2026-03-31",
      "site_type": "병원",
      "flow_item": "작업 대상"
    },
    {
      "id": "f18",
      "claim": "같은 병원 실증에서 전체 배송 성공률은 87.03%, 승강기 가동률 59% 미만일 때 95.52% 였고, 실패 14건은 승강기 막힘 8건·복도 주행 4건·통신 오류 2건이었으며, 승강기 가동률이 높을수록 실패가 많았다.",
      "tag": "사실",
      "source_ids": [
        "ref-943"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "\"A higher EOR was strongly associated with more delivery failures.\" 대부분 실패는 탑승객·화물의 물리적 가로막음.",
      "as_of": "2026-03-31",
      "site_type": "병원",
      "flow_item": "예외·성과"
    },
    {
      "id": "f19",
      "claim": "Ocado 는 물류창고 로봇 교통 관리·오케스트레이션 알고리즘과 운영 변경을 실제 창고에 적용하기 전에 시뮬레이션·디지털 트윈에서 시험하고, 초당 10회 로봇 통신 같은 실제 운영 데이터로 모델을 다듬으며, 12개월 동안 창고 운영 270년 분량을 시뮬레이션했다고 밝힌다.",
      "tag": "추정",
      "source_ids": [
        "ref-1052"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: \"We can identify bottlenecks, predict congestion, evaluate new layouts or algorithms, and stress-test for peak demand.\"",
      "as_of": "2025-06-04",
      "site_type": "물류창고",
      "flow_item": "예외·성과",
      "vendor_claim": true
    },
    {
      "id": "f20",
      "claim": "Open-RMF 의 웹 API 서버(rmf-web api-server)는 기록용 데이터베이스로 tortoise-orm 을 통해 PostgreSQL·SQLite·MySQL·MariaDB 를 지원하며 기본값은 메모리 SQLite 다.",
      "tag": "사실",
      "source_ids": [
        "ref-762"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "api-server README: 기록 DB tortoise-orm, 기본 in-memory SQLite. (재인용: 2026-09-30-05)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "확인한 자료를 종합하면 핵심 질문(플랫폼 자체의 상태·데이터·배포·비용 관리)에 대해, 데이터는 자기 기술형 기록 형식(MCAP)과 플랫폼 기록 DB 로 남기고(f4·f20), 상태는 OpenTelemetry 의 추적·지표·로그로 플랫폼 서비스를 관찰하면서 로봇 내부 실행은 저부하 추적·커널 필터로 교란 없이 보며(f1·f3·f6·f8), 배포는 컨테이너 오케스트레이션의 자동 재시작과 이미지 기반 A/B 롤백, 배포 전 시뮬레이션 검증을 조합하고(f9·f10·f19), 비용은 표준 청구 데이터(FOCUS)와 토큰 지표를 FinOps 주기로 관리하는 조합이 공개 자료의 공통 형태로 보인다(f7·f12·f13).",
      "tag": "추정",
      "source_ids": [
        "ref-1040",
        "ref-762",
        "ref-1038",
        "ref-1039",
        "ref-1042",
        "ref-1044",
        "ref-1045",
        "ref-1046",
        "ref-1052",
        "ref-1043",
        "ref-1048",
        "ref-1049"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "종합 추정. 이종 제조사 로봇의 기록과 플랫폼 추적을 한 작업 단위로 잇는 공개 사례는 찾지 못함.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "확인한 자료를 종합하면 이 영역이 중요한 까닭은, 미들웨어 기록만으로는 내부 병목을 알 수 없고(f2) 관찰 도구 자체가 시스템을 교란할 수 있으며(f3), 병원 실증처럼 실패 원인이 로봇·승강기 로그를 함께 모아야 드러나고(f17·f18), 클라우드 언어 모델 호출 비용이 반복 작업에서 누적되며(f14), 개인정보를 다루는 시스템은 접속기록 보존·점검 의무를 지기 때문이다(f11).",
      "tag": "추정",
      "source_ids": [
        "ref-1038",
        "ref-1039",
        "ref-943",
        "ref-1051",
        "ref-766"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "종합 추정. 로봇 플랫폼이 개인정보처리시스템에 해당하는지는 처리 데이터(영상·사용자 정보)에 따라 달라 미확인.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "확인한 자료를 종합하면 43. 데이터·관측성·배포에서 ROP 가 직접 맡을 범위는 플랫폼 서비스의 로그·지표·추적 수집과 보존 정책(f6·f11), 작업 단위 추적 문맥 전파와 로봇 기록(MCAP 등)의 수집·색인 인터페이스(f4·f8·f17), 플랫폼 구성 요소의 배포·롤백·버전 기록과 배포 전 검증(f9·f19), 클라우드·언어 모델 호출 비용의 계측·배분(f7·f13)이다.",
      "tag": "추정",
      "source_ids": [
        "ref-1042",
        "ref-766",
        "ref-1040",
        "ref-1044",
        "ref-943",
        "ref-1045",
        "ref-1052",
        "ref-1043",
        "ref-1049"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "종합 추정. 분류 원문 19장 경계와 1절 리스트업 네 항목 기준.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "연계 대상: 분류 원문 19장 기준으로 로봇 운영체제·펌웨어의 무선 업데이트와 로봇 내부 ROS 2 실행 추적(f1·f10)은 로봇 제조사에, 클라우드 청구 데이터 생성(f13)은 클라우드 사업자에, 승강기 통신 로그(f17)는 설비 제어 쪽에 속하므로, 이종 제조사를 잇는 ROP 는 이들이 내는 기록·업데이트 상태·청구 데이터를 받아 모으는 인터페이스를 맡을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1038",
        "ref-1046",
        "ref-1049",
        "ref-943"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "종합 추정. 자사 로봇까지 만드는 경우 경계가 이동할 수 있음(분류 원문 19장).",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f25",
      "claim": "이 영역은 실행 기록을 보여 주는 37. 관제 화면·실행 기록(f17·f20), 로그로 원인을 찾는 38. 모니터링·이상 탐지·원인 분석(f2·f18), 성과 지표의 39. 운영 성과 측정·개선(f18), 컨테이너·DDS 통신의 42. 분산 시스템·통신·컴퓨팅 구조(f9), 기록 DB 를 두는 41. 플랫폼 아키텍처·외부 API(f20), 업데이트·버전의 57. 자산·소프트웨어 수명주기 관리(f10), 배포 전 검증의 54. 시험·형식 검증·벤치마크와 34. 시뮬레이션·예측용 디지털 트윈(f19), 접속기록의 53. 개인정보·영상 데이터와 52. 통신 보호·위협 관리·감사(f11), 비용의 3. 경제성·조달·사업 모델(f12·f13), 언어 모델 비용의 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영·13. 대화형 기능의 신뢰·기반(f7·f14), 승강기 로그의 22. 설비·건물 시스템 연동(f17), 적용 현장인 63. 병원·의료(f15~f18)·61. 물류창고(f19)와 이어진다.",
      "tag": "추정",
      "source_ids": [
        "ref-943",
        "ref-762",
        "ref-1038",
        "ref-1045",
        "ref-1046",
        "ref-1052",
        "ref-766",
        "ref-1048",
        "ref-1049",
        "ref-1043",
        "ref-1051"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "종합 추정. 연결 근거는 괄호 안 finding.",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-1038",
      "org": "Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L, arXiv)",
      "title": "ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2",
      "published": "2022-07",
      "url": "https://arxiv.org/abs/2201.00393",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "LTTng 기반 ROS 2 계측·추적 도구 모음. 종단 간 메시지 지연 증가 평균 0.0033 ms 보고. 초록 페이지만 열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1039",
      "org": "Yu, J., Lee, S., Choi, Y., & Park, K.-J. (arXiv)",
      "title": "ros2probe: Non-intrusive, Kernel-selective Observability for Robot Operating System 2 Middleware",
      "published": "2026-06",
      "url": "https://arxiv.org/abs/2606.10746",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "ROS 2 도메인에 참여하지 않고 커널 필터로 선택한 토픽만 관찰하는 프레임워크. 관찰자 CPU·메모리 감소와 포화 시 무손실 보고. 초록 기준.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1040",
      "org": "Open Robotics (ROS 2 Documentation)",
      "title": "Iron Irwini (iron)",
      "published": "2023-05-23",
      "url": "https://docs.ros.org/en/rolling/Releases/Release-Iron-Irwini.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "ROS 2 Iron 릴리스 노트. rosbag2 기본 기록 형식을 mcap 으로 바꾸고 원격 기록 제어 서비스 등을 더함.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/ros2/ros2_documentation/rolling/source/Releases/Release-Iron-Irwini.rst",
      "source_unopened": false
    },
    {
      "id": "ref-1041",
      "org": "Foxglove",
      "title": "MCAP as the ROS 2 Default Bag Format",
      "published": "2022-12-22",
      "url": "https://foxglove.dev/blog/mcap-as-the-ros2-default-bag-format",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "Iron 부터 MCAP 이 ROS 2 기본 백 형식이 된다는 발표와 SQLite3 대비 장점(벤더 주장).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1042",
      "org": "OpenTelemetry (CNCF)",
      "title": "Specification Status Summary",
      "published": null,
      "url": "https://opentelemetry.io/docs/specs/status/",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "OpenTelemetry 신호(추적·지표·로그·배기지·프로파일)별 API·SDK·프로토콜 안정성 상태.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1043",
      "org": "OpenTelemetry (open-telemetry/semantic-conventions-genai)",
      "title": "semantic-conventions-genai/docs/gen-ai/gen-ai-token-metrics.md",
      "published": null,
      "url": "https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "생성형 AI 추론 토큰 지표(입력·출력·캐시·추론 토큰 카운터와 호출별 히스토그램)의 의미 규약. 개발 단계.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-telemetry/semantic-conventions-genai/main/docs/gen-ai/gen-ai-token-metrics.md",
      "source_unopened": false
    },
    {
      "id": "ref-1044",
      "org": "szobov (GitHub)",
      "title": "ros-opentelemetry — ROS2 x OpenTelemetry README",
      "published": null,
      "url": "https://github.com/szobov/ros-opentelemetry",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "ROS 2 C++·Python 노드에 OpenTelemetry 분산 추적·로그 연결을 넣는 개인 관리 오픈소스 라이브러리.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/szobov/ros-opentelemetry/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-1045",
      "org": "Zhang, J., Yu, X., & Westerlund, T. (Sensors 25(16):5067)",
      "title": "Enhancing the Resilience of ROS 2-Based Multi-Robot Systems with Kubernetes: A Case Study on UWB-Based Relative Positioning",
      "published": "2025-08-14",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12390455/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "K3s 로 컨테이너화한 ROS 2 노드를 다중 로봇에서 운영하고 파드 장애 시 자동 재시작으로 위치 정확도를 유지함을 보인 연구. PMC 본문 열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1046",
      "org": "Northern.tech (mendersoftware)",
      "title": "mender — README",
      "published": null,
      "url": "https://github.com/mendersoftware/mender",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "임베디드 리눅스용 오픈소스 OTA 업데이트 관리자. A/B 루트 파일시스템 분할과 자동 롤백.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/mendersoftware/mender/master/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-766",
      "org": "개인정보보호위원회 (국가법령정보센터)",
      "title": "개인정보의 안전성 확보조치 기준 (개인정보보호위원회고시 제2023-6호)",
      "published": "2023-09-22",
      "url": "https://www.law.go.kr/admRulLsInfoP.do?chrClsCd=010202&admRulSeq=2100000229672",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "개인정보처리자의 안전성 확보조치 고시. 제8조에서 접속기록 보관 기간·점검 주기·위변조 방지를 정함.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1048",
      "org": "FinOps Foundation",
      "title": "FinOps Phases",
      "published": null,
      "url": "https://www.finops.org/framework/phases/",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "FinOps 프레임워크의 정보·최적화·운영 세 단계 설명.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1049",
      "org": "FinOps Foundation",
      "title": "Introducing FOCUS 1.2: SaaS/PaaS Support, Invoice Reconciliation, and more",
      "published": null,
      "url": "https://www.finops.org/insights/focus-1-2-available/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "청구 데이터 명세 FOCUS 1.2 의 새 기능(SaaS·PaaS, 가상 통화, InvoiceId, 다중 통화)과 지원 사업자 발표. 명세 본문이 아닌 발표 글. 제목은 검색 결과 기준.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-943",
      "org": "Lee, Y., Kim, S.-E., Kim, J. S. 외 (Digital Health 12)",
      "title": "Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments",
      "published": "2026-03-31",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "고려대학교 구로병원 약품 배송 로봇 122건 실증. 로봇·승강기 로그와 수기 기록으로 승강기 가동률과 실패의 관계 분석. PMC 본문 열람.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1051",
      "org": "Bruno, L. D. M., Sim, J., & Hagiwara, Y. (arXiv)",
      "title": "Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots",
      "published": "2026-09",
      "url": "https://arxiv.org/abs/2609.29043",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "두 단계 LLM 연쇄 계획으로 프롬프트 길이를 줄이고 로컬·클라우드 모델을 비교한 서비스 로봇 연구. 클라우드 API 비용·지연을 동기로 듦.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2609.29043",
      "source_unopened": false
    },
    {
      "id": "ref-1052",
      "org": "Ocado Group",
      "title": "Ocado's digital twins and simulations: driving efficiencies",
      "published": "2025-06-04",
      "url": "https://www.ocadogroup.com/newsroom/stories/digital-twins-and-simulations",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "Ocado 가 창고 로봇 알고리즘·운영 변경을 시뮬레이션·디지털 트윈에서 먼저 시험한다는 회사 글(벤더 주장). 제목 뒷부분은 검색 결과 기준.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-762",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf-web/packages/api-server/README.md",
      "published": null,
      "url": "https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 웹 API 서버의 REST 엔드포인트·OpenAPI 문서·기록 DB·인증 구조 설명.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md",
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
      "rationale": "섹션 3: f22(왜 중요한가), f21(핵심 질문 답, 추정) / 섹션 4: 관측성·실행 추적 f1·f2, MCAP f4·f5(벤더 주장 병기), OpenTelemetry f6, 토큰 지표 f7, A/B 분할 업데이트 f10, FinOps·FOCUS f12·f13 / 섹션 5: 병원 — f15(시작 조건)·f16(완료·인계)·f17(작업 대상: 로봇·승강기 로그 정보)·f18(예외·성과), 물류창고 — f19(배포 전 시뮬레이션 검증, 벤더 주장 병기). 제조 공장·상업 시설·가정·실외 사례는 찾지 못함을 명시 / 섹션 6: 기록 f4·f20, 관찰 f1·f3·f6·f8, 배포 f9·f10·f19, 비용 f7·f12·f13·f14 / 섹션 7: rosbag2·MCAP f4·f5, ros2_tracing f1, ros2probe f3, OpenTelemetry f6·f7, ros-opentelemetry f8, K3s f9, Mender f10, FOCUS f13, 개인정보 고시 f11 / 섹션 8: f1·f3·f9·f14·f15~f18 / 섹션 9: f23(직접 범위), f24(연계 대상) / 섹션 10: f25 — 3, 13, 22, 34, 37, 38, 39, 41, 42, 44, 47, 52, 53, 54, 57, 61, 63 / 섹션 11: open_questions_new 4건. 다음 실행 후보: 38. 모니터링·이상 탐지·원인 분석 페이지에 f1·f3·f17·f18 반영, 57. 자산·소프트웨어 수명주기 관리 페이지에 f10 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "관측성",
      "term_en": "Observability",
      "definition": "시스템이 내보내는 로그·지표·추적 같은 원격 측정 데이터만으로 내부 상태와 오류·성능 원인을 알아낼 수 있는 정도, 또는 그것을 가능하게 하는 수집·분석 체계다."
    },
    {
      "term_ko": "오픈텔레메트리",
      "term_en": "OpenTelemetry (OTel)",
      "definition": "추적·지표·로그를 생성·수집·전송하는 API·SDK·전송 프로토콜(OTLP)과 의미 규약을 정한 벤더 중립 오픈소스 관측성 표준 프로젝트다."
    },
    {
      "term_ko": "MCAP",
      "term_en": "MCAP",
      "definition": "여러 채널의 시간 표시 메시지를 스키마와 함께 담는 자기 기술형 로깅 파일 형식으로, ROS 2 Iron 부터 rosbag2 의 기본 기록 형식이다."
    },
    {
      "term_ko": "핀옵스",
      "term_en": "FinOps",
      "definition": "클라우드·SaaS·AI 서비스 비용과 사용량 데이터를 정보·최적화·운영 단계로 반복 관리하며 엔지니어링·재무·사업 팀이 비용 책임을 나누는 운영 방식이다."
    }
  ],
  "open_questions_new": [
    "서로 다른 제조사 로봇의 기록(MCAP·제조사 로그)과 플랫폼 서비스의 분산 추적을 하나의 작업 식별자로 이어 원인 분석에 쓴 공개 사례나 표준이 있는가? | 관련 영역: 43. 데이터·관측성·배포, 38. 모니터링·이상 탐지·원인 분석 | 근거: f8 | 종류: 일반",
    "로봇 플랫폼이 수집하는 텔레메트리·주행 기록·영상의 보존 기간을 정한 국내 기준이나 운영 사례가 개인정보 접속기록 규정 밖에도 있는가? | 관련 영역: 43. 데이터·관측성·배포, 53. 개인정보·영상 데이터 | 근거: f11 | 종류: 일반",
    "OpenTelemetry 생성형 AI 토큰 지표가 개발 단계에서 이름이 바뀌고 있는데, 언어 모델 호출 비용 계측을 안정 판이 나오기 전까지 어떤 기준으로 고정할 것인가? | 관련 영역: 43. 데이터·관측성·배포, 13. 대화형 기능의 신뢰·기반 | 근거: f7 | 종류: 일반",
    "운행 중인 로봇 작업을 끊지 않고 현장 서버·로봇에 플랫폼 소프트웨어를 순차 배포하고 되돌리는 시점·기준을 공개한 로봇 관제 제품이나 연구가 있는가? | 관련 영역: 43. 데이터·관측성·배포, 57. 자산·소프트웨어 수명주기 관리 | 근거: f10 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 16,
    "cross_checked_count": 1,
    "unverified": [
      "f1·f3·f14 는 논문 초록(또는 HTML 일부) 기준이며 본문 실험 조건 미확인",
      "f7: 검색 결과 요약의 다른 문서들은 gen_ai.client.token.usage 히스토그램을 설명하지만, 열어 본 현재 저장소는 gen_ai.client.inference.usage.* 로 정의함. 이름 변경 시점과 이전 이름의 폐기 여부 미확인",
      "f11 의 '5만 명 이상' 조건 문구는 검색 요약으로 보완했고 법령 페이지 요약에서는 1년/2년 구분만 확인",
      "f13 FOCUS 1.2 명세 본문(PDF) 미열람, 발표 글만 열람",
      "f8 ros-opentelemetry 라이선스·유지 주체 미확인(개인 관리 저장소)",
      "ref-1049·ref-1052 제목 일부는 검색 결과 제목 기준",
      "Zampetti 외 CPS CI/CD 인터뷰 연구(ACM TOSEM 2023)는 ACM 403·PDF 본문 추출 실패로 넣지 않음",
      "Docker·Kubernetes 기반 ROS 설계 흐름 논문(ACM 10.1145/3594539)은 403 으로 넣지 않음",
      "실외이동로봇 운행안전인증에서 관제·소프트웨어 원격 업데이트 시 변경 인증 필요 여부는 KIRIA 안내 페이지에 없어 확인하지 못함",
      "제조 공장·상업 시설·가정·실외 현장의 데이터·배포 사례는 찾지 못함"
    ],
    "scope_violations": [
      "f1·f3: ROS 2 내부 실행 추적은 로봇 소프트웨어 쪽 기법이므로 관찰 방법 근거로만 쓰고, 이종 제조사 로봇 내부 추적은 f24 에서 연계 대상으로 구분함",
      "f10: 로봇 운영체제·펌웨어 OTA 는 로봇 제조사 영역이므로 claim 을 '연계 대상: '으로 시작함",
      "f14: 언어 모델 계획 자체는 44. 로봇 기반 모델·언어 모델 계획의 내용이며 이 영역에는 비용·지연 근거로만 제안함",
      "f17: 승강기 통신 로그 생성은 설비 제어 쪽이며 ROP 는 수집·결합만 맡는 것으로 f24 에서 구분함",
      "f19: 시뮬레이션·디지털 트윈 자체는 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)의 내용이며 이 영역에는 배포 전 검증 근거로만 제안함. 18. 실시간 세계 상태·데이터 일관성과 섞지 않음"
    ],
    "budget_used": {
      "queries": 22,
      "sources": 15
    },
    "limits": "web_fetch_available: true · fetch_mode full. 검색 22회/30, 신규 출처 15건/15(출처 상한 도달). 신규 출처 id: 실행 컨텍스트의 예약 구간은 ref-1032 부터이나, 입력의 같은 날 이전 브리프(2026-09-30-04·2026-09-30-05)가 ref-1032~ref-1037 을 다른 출처에 이미 썼으므로 충돌을 피하려고 예약 구간 안의 ref-1038~ref-1052 를 순서대로 썼다. 재사용 1건(ref-762, 이전 브리프 2026-09-30-05 재인용, 이번에 다시 열지 않음; 값은 그 브리프의 출처 표를 따랐고 참고문헌 목록 전체는 입력에 없음). 원문 열람: 신규 15건 모두 열었다(webfetch 11건, github_raw 4건). 논문 가운데 Zhang 외(ref-1045)·Lee 외(ref-943)는 PMC 본문을, 나머지는 초록 페이지를 열었다. 교차 확인 1건(f4: ROS 2 공식 릴리스 노트와 Foxglove 블로그). 벤더 문서만 근거로 한 f5·f19 는 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈다. 분류 원문 핵심 질문(플랫폼 자체의 상태·데이터·배포·비용 관리)에는 f21 로 답했고 결론은 '자기 기술형 기록 형식과 기록 DB + OpenTelemetry 기반 플랫폼 관찰과 저부하 로봇 내부 추적 + 컨테이너 자동 재시작·A/B 롤백·배포 전 시뮬레이션 검증 + 표준 청구 데이터와 토큰 지표를 쓰는 FinOps 주기'라는 추정이다. 현장 유형 사례는 병원(f15~f18, 국내 고려대학교 구로병원)·물류창고(f19, 벤더 주장)뿐이다. 국내 자료는 개인정보보호위원회 고시(ref-766)와 국내 병원 실증 논문(ref-943) 두 건이다. L. AI·학습 기술 관련 f7·f14 는 교차 규칙에 따라 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영과 함께 연결하도록 제안했다. 용어집에 이미 있는 분산 추적·백 파일·무선 업데이트·서비스 수준 협약·감사 추적·모델 레지스트리는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 없음."
  }
}
```

### runs/2026-09-30-06/verification.json

```json
{
  "run_id": "2026-09-30-06",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 초록 페이지 열람. 저자·제목·IEEE RA-L 7(3) pp. 6511-6518, 2022-07 일치. LTTng 사용, OS 추적과 결합, 모든 ROS 2 계측을 켰을 때 종단 간 메시지 지연 오버헤드 평균 0.0033 ms 가 초록에 있다. 단일 출처(저자 보고), 실험 조건은 초록 기준."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 초록 둘째 문장과 인용 구절이 글자 단위로 일치. ref-1038 의 직접 인용은 이 1회만 쓴다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 초록·HTML 열람. 저자 Yu·Lee·Choi·Park, 2026-06-09 제출 일치. 도메인 참여 관찰자의 탐색 부담·역직렬화 비용, 탐색 패킷으로 통신 상태 복원, 사용자 지정 토픽만 커널 안 필터(eBPF)로 수집, CPU 최대 7배·메모리 최대 28배 감소, 포화 시 손실 0 대 38.5% 가 본문·초록에 있다. 동료 심사 전 프리프린트이므로 본문에 그 사실을 밝힌다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인: ROS 2 문서 Iron 릴리스 노트(github_raw)에서 출시일 2023-05-23, 'mcap' 기본 형식 전환 문장, 서비스 호출로 원격 기록 일시 정지·재개·분할 기능을 확인. Foxglove 블로그(2022-12-22)도 Iron 부터 MCAP 기본값을 알린다. 다만 Foxglove 는 MCAP 개발사이므로 교차 확인은 'MCAP 기본값 전환'에만 해당하고 원격 기록 제어는 릴리스 노트 단일 출처다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Foxglove 블로그(James Smith, 2022-12-22) 열람. SQLite3 resilient 모드 안전성과 write optimized 모드 처리량 동시 제공, zstd·lz4 선택, 메시지 정의 내장(자기 완결) 문구 일치. 벤더 주장 표시·추정 태그 적정."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: OpenTelemetry 명세 상태 요약 열람. 추적 API·SDK·프로토콜 stable, 지표 SDK mixed, 로그 Bridge API·SDK·프로토콜 stable, 프로파일 프로토콜 development, 장기 지원 문장 일치. 페이지에 발행·갱신일 없음 — 기준일은 확인일 2026-09-30."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: semantic-conventions-genai 저장소 원문(github_raw) 열람. 카운터 5종(gen_ai.client.inference.usage.*)·히스토그램 2종(gen_ai.client.inference.operation.*), 단위 {token}, 필수 속성 gen_ai.operation.name·gen_ai.provider.name(카운터는 gen_ai.token.modality 추가), 모두 Development 일치. 이전 이름(gen_ai.client.token.usage)과의 관계는 미확인 — 이름 변경을 단정하지 않는다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: README 열람. inject_trace_context()/extract_trace_context(), 사용자 정의 메시지에 TraceMetadata 필드 추가, C++·Python 패키지, 추적 ID 를 넣는 로거(RCLCPP_ERROR_TRACED, wrap_logger) 일치. 라이선스 표기 없음. 개인 관리 저장소이므로 채택 현황은 주장하지 않는다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: PMC 본문 열람. Sensors 25:5067, 2025-08-14. Jetson Nano 5대(TurtleBot4 탑재) 작업 노드 + 노트북 마스터, K3s v1.27.4, ROS 2 Galactic. F5(LSTM 파드 5개 종료)에서 K3s 자동 재시작 후 오차 약 0.12~0.14 m 로 무장애와 비슷. LSTM 보정 없음은 한 로봇 기준 0.661 m. 복구 시간 미보고. 실험실 환경이므로 현장 유형 적용 사례로 쓰지 않는다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Mender README(github_raw) 열람. IoT·임베디드 리눅스용 오픈소스 OTA 관리자, 클라이언트–서버, dual A/B rootfs 원자적 이미지 배포, 전원 상실 대비 롤백, 루트 파일시스템·애플리케이션·파일·컨테이너 업데이트, Update Modules, Apache 2.0 일치. README 는 상용 제공사(Northern.tech) 문서이므로 '전원이 끊겨도 되돌릴 수 있다'는 신뢰성 부분은 README 의 설명으로 서술한다. '연계 대상:' 표시 적정."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정. ref-766 페이지는 고시명·제2023-6호·2023-09-22 시행까지 일치하나 검증 열람에서 제8조 조문 본문이 표시되지 않았다(동적 로딩). 1년/2년·월 1회 문구는 검색 요약으로만 확인. 또한 검증 검색에서 이 고시가 개인정보보호위원회고시 제2025-9호(국가법령정보센터 기준 2025-10-31)로 다시 개정됐고, 접속기록 점검 주기를 내부관리계획으로 정하게 바꾸는 개정(유예 후 시행)이 보도됐다 — 2023-6호 조문을 현행 기준으로 서술할 수 없다(최신성)."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: FinOps Phases 페이지 열람. Inform·Optimize·Operate 세 단계, 사용량 최적화와 요금 최적화 구분, 기술 범주에 Public Cloud·SaaS·AI services 등 일치. 발행일 표시 없음 — 기준일 확인일."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: FinOps 재단 발표 글 열람. FOCUS 1.2 비준 2025-05-29, 글 게시 2025-06-03(저자 Mike Fuller 외). 새 열 7개(InvoiceId, BillingAccountType, SubAccountType, PricingCurrency 외 3), SaaS·PaaS 통합, 크레딧·토큰 등 가상 통화, 기존 AWS·Microsoft·Google Cloud·Oracle Cloud 와 새로 Alibaba Cloud·Databricks·Grafana 지원 일치. 브리프 published 가 null — 2025-06-03 이다. 명세 본문이 아닌 발행 기관의 발표 글."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 초록·HTML 열람(2026-09-24 제출). 'Cloud APIs incur per-request cost …' 문장, 네트워크 지연, 프롬프트 약 45% 감소, 로컬 모델 Qwen2.5-14B·Cogito-14B, 최대 37%p 개선, 클라우드 모델 Claude Sonnet 4.6, GPSR 명령 100개, Toyota HSR 10개 중 6개 일치. 비용 금액 미보고. 프리프린트. L. AI·학습 기술 교차 규칙에 따라 44·47 과 연결."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: PMC 본문 열람. Digital Health, 2026-03-31, 고려대학교 구로병원, 비응급 임무 122건(2025-06-18~29), 응급실 직원의 웹 애플리케이션 요청으로 시작 일치."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(부분 표현 수정): 원문 성공 정의는 '로봇이 전체 경로를 마치고 사람 개입 없이 약품을 인계'이다. '간호사가 받는 것'은 검증 열람에서 정의 문장 안에 확인되지 않았으므로 정의의 일부로 쓰지 않는다(required_fixes)."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 로봇 시스템 로그(1 Hz, 승강기 호출·탑승·문 동작), 승강기 통신 로그, 관찰자 사례 기록지(탑승객 수·화물 수·성공 여부) 일치. 저자는 탑승객 수가 로봇 탑재 센서로는 얻을 수 없어 관찰자 기록에 의존했다고 밝힌다. flow_item '작업 대상'은 배송 작업의 대상(약품)과 맞지 않으므로 적용 사례 표에서는 예외·성과(실패 원인 분석 자료)로 둔다(required_fixes)."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 전체 성공률 87.03%, EOR 59% 미만 95.52%, 실패 14건(승강기 막힘 8·복도 주행 4·통신 오류 2), 인용 문장 일치. 다만 원문은 분모를 122건이라 하는데 122건 중 14건 실패면 약 88.5%가 되어 원문 수치 사이에 불일치가 있다(87.03%는 108건 기준 계산과 맞음). 수치는 저자 보고대로만 옮긴다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Ocado 글(2025-06-04) 열람. 인용 구절, 초당 10회 로봇 통신, 12개월에 창고 운영 270년 분량 시뮬레이션 일치. 정확한 제목은 'Ocado's digital twins and simulations: driving efficiencies and innovation at scale'. 벤더 주장 표시·추정 태그 적정. 34. 시뮬레이션·예측용 디지털 트윈의 내용을 배포 전 검증 근거로만 쓴다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 data/source_texts/ref-762.txt 와 raw README 에서 tortoise-orm 경유 PostgreSQL·SQLite·MySQL·MariaDB 지원, 기본 in-memory SQLite 일치. 2026-09-30-05 브리프 f1 과 같은 주장 — 기존 ref-762 각주 재사용."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 괄호 안 finding 의 종합 추정으로 추정 태그 적정. 근거 finding 가운데 f5·f19 는 벤더 주장이므로 서술 시 그 부분에 벤더 주장임을 유지한다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 종합 추정. 다만 근거 f11 이 강등됐으므로 '접속기록 보존·점검 의무' 부분은 판(2023-09-22 시행 판 기준)과 현행 여부 미확인을 밝혀 쓴다(required_fixes)."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 종합 추정. 분류 원문 19장 경계와 1절 리스트업 네 항목에 맞는다. 보존 정책 근거 f11 은 강등된 추정임을 유지한다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 종합 추정. 로봇 운영체제·펌웨어 OTA 와 로봇 내부 실행 추적을 제조사에, 청구 데이터 생성을 클라우드 사업자에, 승강기 통신 로그를 설비 제어에 둔 구분이 원문 19장 표와 맞다."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 연결 영역 번호·이름이 부록 A 와 일치(3, 13, 22, 34, 37, 38, 39, 41, 42, 44, 47, 52, 53, 54, 57, 61, 63). L. AI·학습 기술 교차 규칙(44·47)과 18/34 구분 준수."
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
      "f20 은 2026-09-30-05 브리프 f1(41. 플랫폼 아키텍처·외부 API)과 같은 주장이다 — 새 각주를 만들지 않고 ref-762 를 재사용한다(브리프가 이미 재사용).",
      "f15~f18 의 고려대학교 구로병원 실증은 용어집 '승강기 가동률 (Elevator Operating Rate (EOR))' 항목과 같은 연구일 가능성이 있다 — 같은 URL 이 참고문헌에 이미 있으면 퍼블리셔가 기존 id 로 합치며, 본문 용어는 용어집의 '승강기 가동률'을 쓴다."
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
    "f11: [사실] → [추정]으로 강등하고 본문에 '「개인정보의 안전성 확보조치 기준」 제2023-6호(2023-09-22 시행 판) 기준이며 이후 개정 여부와 현행 조문은 미확인'을 밝힌다. '월 1회 이상 점검'을 현행 의무처럼 쓰지 않는다 — 검증 열람에서 조문 본문이 확인되지 않았고 이후 개정 고시가 확인됐다.",
    "f11·ref-766: 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 ref-766 에 source_unopened: true 를 넣는다 — 법령 페이지에서 제8조 조문 본문이 열람되지 않았다.",
    "11절 열린 질문과 open_question_updates 에 '로봇 플랫폼에 적용될 수 있는 현행 「개인정보의 안전성 확보조치 기준」(2023-6호 이후 개정판)의 접속기록 보관 기간·점검 주기 조항이 2023-6호와 같은가? | 관련 영역: 43. 데이터·관측성·배포, 53. 개인정보·영상 데이터 | 근거: f11 | 종류: 일반' 을 더하고, additional_research_requests 에 '개인정보보호위원회고시 제2025-9호 제8조와 부칙 시행일 확인'을 넣는다.",
    "f22: 3절 서술에서 '개인정보를 다루는 시스템은 접속기록 보존·점검 의무를 진다' 부분을 '2023-09-22 시행 판 기준 접속기록 보관 의무가 있었다(현행 조문 미확인)'로 한정한다 — 근거 f11 이 강등됐다.",
    "f16: 5절 병원 사례의 완료·인계 칸에서 성공 정의를 '로봇이 사람 개입 없이 전체 경로를 마치고 약품을 인계'로 쓰고 '간호사가 받는 것'을 정의의 일부로 쓰지 않는다 — 원문 정의 문장에서 수령인이 확인되지 않았다.",
    "f17: 5절 병원 사례에서 로봇·승강기 로그와 관찰 기록지를 '작업 대상' 칸이 아니라 '예외·성과' 칸(실패 원인 분석 자료)에 두고, 작업 대상 칸은 f15·f16 이 근거하는 약품으로 둔다. site_matrix_updates 의 item 도 그에 맞춘다 — 배송 작업의 대상은 약품이다.",
    "f18: 성공률·실패 건수는 저자 보고대로만 옮기고 분모를 새로 계산해 덧붙이지 않는다. 11절에 '구로병원 실증의 전체 성공률 87.03% 가 122건 중 실패 14건과 맞지 않는데(약 88.5%) 성공률의 분모는 무엇인가? | 관련 영역: 43. 데이터·관측성·배포, 63. 병원·의료 | 근거: f18 | 종류: 일반' 을 올린다 — 원문 수치 사이에 불일치가 있다.",
    "5절: 병원 사례의 수행 자원·제약, 물류창고 사례(f19)의 시작 조건·작업 대상·수행 자원·제약·완료·인계는 '미확인'으로 두고, 제조 공장·상업 시설·가정·실외 사례를 찾지 못했음을 밝힌다. f9(실험실)·f14(평가 실험)는 현장 유형 적용 사례로 쓰지 않는다.",
    "f5·f19: [추정]에 '벤더 주장'을 병기한 채 유지하고, f21 에서 f19 에 기댄 '배포 전 시뮬레이션 검증' 부분도 벤더 주장 근거임을 밝힌다.",
    "f10: '업데이트 중 전원이 끊겨도 동작하던 상태로 되돌릴 수 있다'는 부분은 'Mender README 는 …라고 설명한다'처럼 출처의 설명으로 서술한다 — 상용 제공사 문서이고 독립 확인이 없다.",
    "f3·f14: 본문에 arXiv 프리프린트(동료 심사 전)임을 밝힌다.",
    "ref-1049: reference_updates 의 발행일을 2025-06-03 으로 적고(FOCUS 1.2 비준일 2025-05-29 는 본문 기준일로 유지), 유형은 발행 기관의 발표 글이며 명세 본문 미열람임을 각주에 밝힌다.",
    "ref-1052: 참고문헌 제목을 'Ocado's digital twins and simulations: driving efficiencies and innovation at scale' 로 고친다 — 원문 제목과 다르다.",
    "11절 열린 질문 셋째 항목: '토큰 지표가 개발 단계에서 이름이 바뀌고 있는데'를 '개발 단계인 토큰 지표의 이름(gen_ai.client.inference.usage.* 와 다른 문서의 gen_ai.client.token.usage)이 바뀌었는지 미확인인데'로 고쳐 단정을 없앤다 — 이름 변경은 브리프에서 미확인이다.",
    "10절: f7·f14 는 교차 규칙에 따라 44. 로봇 기반 모델·언어 모델 계획, 47. AI·학습·적응과 모델 운영과 13. 대화형 기능의 신뢰·기반에 번호와 이름을 함께 써서 연결하고, f19 는 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)에만 연결하며 18. 실시간 세계 상태·데이터 일관성과 섞지 않는다."
  ],
  "confidence": "low",
  "verification_note": "판정: 조건부 승인. 확인 24건, 미확인 1건, 교차 확인 1건. 강등: f11 사실 → 추정(법령 페이지에서 조문 본문 미확인, 검증 중 이후 개정 고시(개인정보보호위원회고시 제2025-9호) 확인으로 현행 여부 미확인). 원문 미열람 출처: ref-766(조문 본문). 주의: 3. 왜 중요한가와 9. 책임 경계를 이루는 핵심 주장(f22·f23·f24)은 종합 추정이고, 6절 근거 대부분이 단일 출처이며 교차 확인은 f4(ROS 2 Iron 부터 MCAP 기본값) 1건뿐이다. f3·f14 는 동료 심사 전 프리프린트, f5·f19 는 벤더 주장이다. 구로병원 실증(f18)은 원문의 성공률과 실패 건수의 분모가 서로 맞지 않는다. 현장 유형 사례는 병원·물류창고(벤더 주장)뿐이다. 참고: ref-762 는 이번 실행에서 다시 열지 않았다고 적혀 있으나 fetched: true 로 기록됐다(입력 원문 텍스트로 검증함). 여러 출처의 fetch_url 이 비어 있다. 정정 요청 없음. 검증 검색 3회 사용.",
  "retry_reason": null
}
```

### runs/2026-09-30-06/pages.json

```json
{
  "run_id": "2026-09-30-06",
  "outline": [
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 900,
      "summary": "공개 자료를 종합하면 플랫폼 자체를 관리해야 하는 까닭은 기록의 한계, 관찰의 부담, 실패 원인 분석, 언어 모델 호출 비용, 기록 보관 의무 다섯 가지로 모인다. [추정][^ref-1038][^ref-1039][^ref-943][^ref-1051][^ref-766]",
      "planned_findings": [
        "f22",
        "f2",
        "f3",
        "f17",
        "f14",
        "f11"
      ]
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 900,
      "summary": "기록은 백 파일과 MCAP, 관찰은 OpenTelemetry 신호와 실행 추적, 배포는 A/B 분할 업데이트, 비용은 FinOps·FOCUS 가 기본 용어다. [사실][^ref-1040][^ref-1042][^ref-1048]",
      "planned_findings": [
        "f4",
        "f5",
        "f6",
        "f1",
        "f8",
        "f7",
        "f10",
        "f12",
        "f13"
      ]
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 1300,
      "summary": "병원(고려대학교 구로병원 약품 배송 로봇 실증의 로봇·승강기 로그 기반 실패 분석)과 물류창고(Ocado 의 배포 전 시뮬레이션 검증, 벤더 주장) 두 사례이며 다른 현장 유형 사례는 찾지 못했다. [사실][^ref-943]",
      "planned_findings": [
        "f15",
        "f16",
        "f17",
        "f18",
        "f19"
      ]
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 2200,
      "summary": "자기 기술형 기록 형식과 기록 DB, OpenTelemetry 기반 플랫폼 관찰과 저부하 로봇 내부 추적, 컨테이너 자동 재시작·A/B 롤백·배포 전 검증, 표준 청구 데이터와 토큰 지표를 쓰는 FinOps 주기의 조합이 공통 형태로 보인다. [추정][^ref-1040][^ref-1042][^ref-1045][^ref-1049]",
      "planned_findings": [
        "f21",
        "f4",
        "f5",
        "f20",
        "f6",
        "f8",
        "f1",
        "f3",
        "f9",
        "f10",
        "f19",
        "f12",
        "f13",
        "f7",
        "f14"
      ]
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 800,
      "summary": "rosbag2·MCAP, ros2_tracing, ros2probe, OpenTelemetry 명세와 생성형 AI 토큰 지표, ros-opentelemetry, K3s, Mender(연계 대상), FinOps 프레임워크, FOCUS 1.2 와 2023-6호 개인정보 고시(현행 미확인). [사실][^ref-1040][^ref-1042][^ref-1049]",
      "planned_findings": [
        "f4",
        "f1",
        "f3",
        "f6",
        "f7",
        "f8",
        "f9",
        "f10",
        "f12",
        "f13",
        "f11"
      ]
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 700,
      "summary": "ros2_tracing(2022), ros2probe(2026 프리프린트), K3s 다중 로봇 복원력 연구(2025), 서비스 로봇 LLM 연쇄 계획(2026 프리프린트), 구로병원 약품 배송 실증(2026)이 대표 자료다. [사실][^ref-1038][^ref-943]",
      "planned_findings": [
        "f1",
        "f3",
        "f9",
        "f14",
        "f15",
        "f18"
      ]
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 900,
      "summary": "ROP 는 플랫폼 서비스의 관찰·보존, 작업 단위 추적 문맥과 로봇·설비 기록의 수집 인터페이스, 플랫폼 배포·롤백, 비용 계측을 맡고 로봇 펌웨어 OTA·로봇 내부 추적·승강기 로그 생성·청구 데이터 생성은 연계 대상으로 보인다. [추정][^ref-1042][^ref-1046][^ref-943]",
      "planned_findings": [
        "f23",
        "f24"
      ]
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 1100,
      "summary": "관제·분석(37·38·39), 아키텍처·통신(41·42), 수명주기·시험(54·57), 시뮬레이션(34), 보안·개인정보(52·53), 비용(3), 언어 모델(13·44·47), 설비(22), 현장(61·63)과 이어진다. [추정][^ref-943]",
      "planned_findings": [
        "f25"
      ]
    },
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md",
      "section": "11. 열린 질문",
      "budget_chars": 900,
      "summary": "이종 기록·추적 연결, 텔레메트리 보존 기준, 토큰 지표 이름 고정, 무중단 순차 배포 기준, 현행 개인정보 고시 조항, 구로병원 성공률 분모 여섯 질문을 올린다.",
      "planned_findings": [
        "f8",
        "f11",
        "f7",
        "f10",
        "f18"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "섹션 3~11 신규 작성(seed → draft): 기록 형식·관측성·배포·비용 관리 접근법, 병원·물류창고 적용 사례, 책임 경계, 연결 영역 17개, 열린 질문 6건"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area43-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 43. 데이터·관측성·배포 의 \"6. 대표 접근법과 기술\" 절(2,750자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area43-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 43. 데이터·관측성·배포 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(1,115자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area43-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 43. 데이터·관측성·배포 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(1,055자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area43-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 43. 데이터·관측성·배포 의 \"4. 핵심 개념과 용어\" 절(975자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area43-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 43. 데이터·관측성·배포 의 \"11. 열린 질문\" 절(889자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area43-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 43. 데이터·관측성·배포 의 \"3. 왜 중요한가\" 절(743자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-30 | 43. 데이터·관측성·배포 | 섹션 3~11 신규 작성(seed → draft): 기록·관측성·배포·비용 접근법, 병원·물류창고 적용 사례, 책임 경계, 열린 질문 6건. 1차 조건부 승인 수정 15건 이행 | run 2026-09-30-06",
  "index_updates": {
    "home_recent": "2026-09-30 — 43. 데이터·관측성·배포: 섹션 3~11 신규 작성(MCAP·OpenTelemetry·A/B 롤백·FinOps 접근법, 병원·물류창고 적용 사례, 책임 경계, 열린 질문 6건)",
    "category_recent": "2026-09-30 — 43. 데이터·관측성·배포: 섹션 3~11 신규 작성(seed → draft). 기록 형식·플랫폼 관찰·배포 롤백·비용 계측과 책임 경계 정리",
    "area_recent": "2026-09-30 — 43. 데이터·관측성·배포: 섹션 3~11 신규 작성, 1차 조건부 승인 수정 15건 이행 (실행 2026-09-30-06)"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "observability",
      "term_ko": "관측성",
      "term_en": "Observability",
      "definition": "시스템이 내보내는 로그·지표·추적 같은 원격 측정 데이터만으로 내부 상태와 오류·성능 원인을 알아낼 수 있는 정도, 또는 그것을 가능하게 하는 수집·분석 체계다.",
      "related_areas": [
        43,
        37,
        38
      ],
      "sources": [
        "ref-1042"
      ]
    },
    {
      "action": "new",
      "slug": "opentelemetry",
      "term_ko": "오픈텔레메트리",
      "term_en": "OpenTelemetry (OTel)",
      "definition": "추적·지표·로그를 생성·수집·전송하는 API·SDK·전송 프로토콜(OTLP)과 의미 규약을 정한 벤더 중립 오픈소스 관측성 표준 프로젝트다.",
      "related_areas": [
        43,
        38,
        47
      ],
      "sources": [
        "ref-1042",
        "ref-1043"
      ]
    },
    {
      "action": "new",
      "slug": "mcap",
      "term_ko": "MCAP",
      "term_en": "MCAP",
      "definition": "여러 채널의 시간 표시 메시지를 스키마와 함께 담는 자기 기술형 로깅 파일 형식으로, ROS 2 Iron 부터 rosbag2 의 기본 기록 형식이다.",
      "related_areas": [
        43,
        37,
        38
      ],
      "sources": [
        "ref-1040",
        "ref-1041"
      ]
    },
    {
      "action": "new",
      "slug": "finops",
      "term_ko": "핀옵스",
      "term_en": "FinOps",
      "definition": "클라우드·SaaS·AI 서비스 비용과 사용량 데이터를 정보·최적화·운영 단계로 반복 관리하며 엔지니어링·재무·사업 팀이 비용 책임을 나누는 운영 방식이다.",
      "related_areas": [
        43,
        3
      ],
      "sources": [
        "ref-1048"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-762",
      "org": "Open Robotics (open-rmf)",
      "title": "rmf-web/packages/api-server/README.md",
      "published": null,
      "url": "https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "Open-RMF 웹 API 서버의 REST 엔드포인트·OpenAPI 문서·기록 DB·인증 구조 설명.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ]
    },
    {
      "id": "ref-1038",
      "org": "Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L, arXiv)",
      "title": "ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2",
      "published": "2022-07",
      "url": "https://arxiv.org/abs/2201.00393",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "LTTng 기반 ROS 2 계측·추적 도구 모음. 종단 간 메시지 지연 증가 평균 0.0033 ms 보고. 초록 페이지만 열람.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1039",
      "org": "Yu, J., Lee, S., Choi, Y., & Park, K.-J. (arXiv)",
      "title": "ros2probe: Non-intrusive, Kernel-selective Observability for Robot Operating System 2 Middleware",
      "published": "2026-06",
      "url": "https://arxiv.org/abs/2606.10746",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "ROS 2 도메인에 참여하지 않고 커널 필터로 선택한 토픽만 관찰하는 프레임워크(동료 심사 전 프리프린트). 관찰자 CPU·메모리 감소와 포화 시 무손실 보고. 초록 기준.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1040",
      "org": "Open Robotics (ROS 2 Documentation)",
      "title": "Iron Irwini (iron)",
      "published": "2023-05-23",
      "url": "https://docs.ros.org/en/rolling/Releases/Release-Iron-Irwini.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "ROS 2 Iron 릴리스 노트. rosbag2 기본 기록 형식을 mcap 으로 바꾸고 원격 기록 제어 서비스 등을 더함.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1041",
      "org": "Foxglove",
      "title": "MCAP as the ROS 2 Default Bag Format",
      "published": "2022-12-22",
      "url": "https://foxglove.dev/blog/mcap-as-the-ros2-default-bag-format",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "Iron 부터 MCAP 이 ROS 2 기본 백 형식이 된다는 발표와 SQLite3 대비 장점(벤더 주장).",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1042",
      "org": "OpenTelemetry (CNCF)",
      "title": "Specification Status Summary",
      "published": null,
      "url": "https://opentelemetry.io/docs/specs/status/",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "OpenTelemetry 신호(추적·지표·로그·배기지·프로파일)별 API·SDK·프로토콜 안정성 상태.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1043",
      "org": "OpenTelemetry (open-telemetry/semantic-conventions-genai)",
      "title": "semantic-conventions-genai/docs/gen-ai/gen-ai-token-metrics.md",
      "published": null,
      "url": "https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "생성형 AI 추론 토큰 지표(입력·출력·캐시·추론 토큰 카운터와 호출별 히스토그램)의 의미 규약. 개발 단계.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1044",
      "org": "szobov (GitHub)",
      "title": "ros-opentelemetry — ROS2 x OpenTelemetry README",
      "published": null,
      "url": "https://github.com/szobov/ros-opentelemetry",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "ROS 2 C++·Python 노드에 OpenTelemetry 분산 추적·로그 연결을 넣는 개인 관리 오픈소스 라이브러리. 라이선스 표기 미확인.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1045",
      "org": "Zhang, J., Yu, X., & Westerlund, T. (Sensors 25(16):5067)",
      "title": "Enhancing the Resilience of ROS 2-Based Multi-Robot Systems with Kubernetes: A Case Study on UWB-Based Relative Positioning",
      "published": "2025-08-14",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12390455/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "K3s 로 컨테이너화한 ROS 2 노드를 다중 로봇에서 운영하고 파드 장애 시 자동 재시작으로 위치 정확도를 유지함을 보인 실험실 연구. PMC 본문 열람.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1046",
      "org": "Northern.tech (mendersoftware)",
      "title": "mender — README",
      "published": null,
      "url": "https://github.com/mendersoftware/mender",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "임베디드 리눅스용 오픈소스 OTA 업데이트 관리자. A/B 루트 파일시스템 분할과 자동 롤백(README 설명).",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-766",
      "org": "개인정보보호위원회 (국가법령정보센터)",
      "title": "개인정보의 안전성 확보조치 기준 (개인정보보호위원회고시 제2023-6호)",
      "published": "2023-09-22",
      "url": "https://www.law.go.kr/admRulLsInfoP.do?chrClsCd=010202&admRulSeq=2100000229672",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람(제8조 조문 본문). 개인정보처리자의 안전성 확보조치 고시 2023-6호 판. 접속기록 보관 기간 등은 검색 요약 기준이며 이후 개정 고시(제2025-9호)가 있어 현행 조문 미확인.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1048",
      "org": "FinOps Foundation",
      "title": "FinOps Phases",
      "published": null,
      "url": "https://www.finops.org/framework/phases/",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "FinOps 프레임워크의 정보·최적화·운영 세 단계 설명.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1049",
      "org": "FinOps Foundation",
      "title": "Introducing FOCUS 1.2: SaaS/PaaS Support, Invoice Reconciliation, and more",
      "published": "2025-06-03",
      "url": "https://www.finops.org/insights/focus-1-2-available/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "발행 기관의 발표 글(명세 본문 미열람). 청구 데이터 명세 FOCUS 1.2(2025-05-29 비준)의 새 기능(SaaS·PaaS, 가상 통화, InvoiceId, 다중 통화)과 지원 사업자 발표.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-943",
      "org": "Lee, Y., Kim, S.-E., Kim, J. S. 외 (Digital Health 12)",
      "title": "Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments",
      "published": "2026-03-31",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "고려대학교 구로병원 약품 배송 로봇 122건 실증. 로봇·승강기 로그와 수기 기록으로 승강기 가동률과 실패의 관계 분석. PMC 본문 열람.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1051",
      "org": "Bruno, L. D. M., Sim, J., & Hagiwara, Y. (arXiv)",
      "title": "Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots",
      "published": "2026-09",
      "url": "https://arxiv.org/abs/2609.29043",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "두 단계 LLM 연쇄 계획으로 프롬프트 길이를 줄이고 로컬·클라우드 모델을 비교한 서비스 로봇 연구(동료 심사 전 프리프린트). 클라우드 API 비용·지연을 동기로 듦.",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1052",
      "org": "Ocado Group",
      "title": "Ocado's digital twins and simulations: driving efficiencies and innovation at scale",
      "published": "2025-06-04",
      "url": "https://www.ocadogroup.com/newsroom/stories/digital-twins-and-simulations",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "Ocado 가 창고 로봇 알고리즘·운영 변경을 시뮬레이션·디지털 트윈에서 먼저 시험한다는 회사 글(벤더 주장).",
      "cited_by": [
        "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md"
      ],
      "source_unopened": false
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "서로 다른 제조사 로봇의 기록(MCAP·제조사 로그)과 플랫폼 서비스의 분산 추적을 하나의 작업 식별자로 이어 원인 분석에 쓴 공개 사례나 표준이 있는가?",
      "areas": [
        43,
        38
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "로봇 플랫폼이 수집하는 텔레메트리·주행 기록·영상의 보존 기간을 정한 국내 기준이나 운영 사례가 개인정보 접속기록 규정 밖에도 있는가?",
      "areas": [
        43,
        53
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "개발 단계인 토큰 지표의 이름(gen_ai.client.inference.usage.* 와 다른 문서의 gen_ai.client.token.usage)이 바뀌었는지 미확인인데, 언어 모델 호출 비용 계측을 안정 판이 나오기 전까지 어떤 기준으로 고정할 것인가?",
      "areas": [
        43,
        13
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "운행 중인 로봇 작업을 끊지 않고 현장 서버·로봇에 플랫폼 소프트웨어를 순차 배포하고 되돌리는 시점·기준을 공개한 로봇 관제 제품이나 연구가 있는가?",
      "areas": [
        43,
        57
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "로봇 플랫폼에 적용될 수 있는 현행 「개인정보의 안전성 확보조치 기준」(2023-6호 이후 개정판)의 접속기록 보관 기간·점검 주기 조항이 2023-6호와 같은가?",
      "areas": [
        43,
        53
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "구로병원 실증의 전체 성공률 87.03% 가 122건 중 실패 14건과 맞지 않는데(약 88.5%) 성공률의 분모는 무엇인가?",
      "areas": [
        43,
        63
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "병원",
      "item": "시작 조건",
      "link": "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md#5-적용-사례-현장-유형-명시",
      "title": "43. 데이터·관측성·배포"
    },
    {
      "site_type": "병원",
      "item": "작업 대상",
      "link": "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md#5-적용-사례-현장-유형-명시",
      "title": "43. 데이터·관측성·배포"
    },
    {
      "site_type": "병원",
      "item": "완료·인계",
      "link": "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md#5-적용-사례-현장-유형-명시",
      "title": "43. 데이터·관측성·배포"
    },
    {
      "site_type": "병원",
      "item": "예외·성과",
      "link": "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md#5-적용-사례-현장-유형-명시",
      "title": "43. 데이터·관측성·배포"
    },
    {
      "site_type": "물류창고",
      "item": "예외·성과",
      "link": "docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md#5-적용-사례-현장-유형-명시",
      "title": "43. 데이터·관측성·배포"
    }
  ],
  "standards_updates": [
    {
      "name": "MCAP (rosbag2 기본 기록 형식, ROS 2 Iron 부터)",
      "kind": "오픈소스",
      "org": "Foxglove (ROS 2 채택: Open Robotics)",
      "url": "https://foxglove.dev/blog/mcap-as-the-ros2-default-bag-format",
      "related_areas": [
        43,
        37,
        38
      ],
      "summary": "여러 채널의 시간 표시 메시지를 메시지 정의와 함께 담는 기록 형식. ROS 2 Iron Irwini(2023-05-23)부터 rosbag2 의 기본 기록 형식이다.",
      "ref_id": "ref-1041"
    },
    {
      "name": "OpenTelemetry 생성형 AI 의미 규약 — 토큰 지표",
      "kind": "오픈소스",
      "org": "OpenTelemetry (CNCF)",
      "url": "https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md",
      "related_areas": [
        43,
        13,
        47
      ],
      "summary": "언어 모델 호출의 입력·출력·캐시·추론 토큰 카운터와 호출별 토큰 히스토그램을 정의한다. 2026-09-30 확인 기준 모두 개발 단계.",
      "ref_id": "ref-1043"
    },
    {
      "name": "ros-opentelemetry",
      "kind": "오픈소스",
      "org": "szobov (GitHub, 개인 저장소)",
      "url": "https://github.com/szobov/ros-opentelemetry",
      "related_areas": [
        43,
        38
      ],
      "summary": "ROS 2 메시지의 사용자 정의 필드로 추적 문맥을 전파해 토픽·서비스·액션을 가로지르는 분산 추적과 로그 연결을 제공하는 라이브러리. 라이선스 표기 미확인.",
      "ref_id": "ref-1044"
    },
    {
      "name": "Mender (OTA 업데이트 관리자)",
      "kind": "오픈소스",
      "org": "Northern.tech (mendersoftware)",
      "url": "https://github.com/mendersoftware/mender",
      "related_areas": [
        43,
        57
      ],
      "summary": "임베디드 리눅스·사물인터넷 장치용 클라이언트–서버 방식 무선 업데이트 관리자. A/B 루트 파일시스템 분할과 이미지 단위 원자적 배포, Apache 2.0.",
      "ref_id": "ref-1046"
    },
    {
      "name": "FinOps 프레임워크 (FinOps Phases)",
      "kind": "프레임워크",
      "org": "FinOps Foundation",
      "url": "https://www.finops.org/framework/phases/",
      "related_areas": [
        43,
        3
      ],
      "summary": "기술 비용·사용량 데이터를 정보·최적화·운영 세 단계로 반복 관리하는 방식. 대상에 공용 클라우드·SaaS·AI 서비스를 포함한다.",
      "ref_id": "ref-1048"
    },
    {
      "name": "FOCUS 1.2 (FinOps 청구 데이터 명세)",
      "kind": "표준",
      "org": "FinOps Foundation",
      "url": "https://www.finops.org/insights/focus-1-2-available/",
      "related_areas": [
        43,
        3
      ],
      "summary": "2025-05-29 비준. SaaS·PaaS 청구 데이터를 클라우드 비용과 같은 스키마에 넣고 가상 통화(크레딧·토큰)·다중 통화·InvoiceId 를 더했다(발표 글 기준, 명세 본문 미열람).",
      "ref_id": "ref-1049"
    }
  ],
  "additional_research_requests": [
    "3·7·9·11절: 개인정보보호위원회고시 제2025-9호 제8조와 부칙 시행일 확인 — 현행 접속기록 보관 기간·점검 주기 조항이 2023-6호와 같은지 알아야 강등된 보존 의무 서술을 [사실]로 바로잡을 수 있다.",
    "5절 병원 사례: 구로병원 약품 배송 로봇 실증의 수행 자원(로봇·간호사·승강기 역할 분담)과 제약(승강기·시간·구역 제약) — 여섯 항목 가운데 두 칸이 미확인이다. 수령인(간호사) 확인 여부와 성공률 분모도 원문에서 재확인이 필요하다.",
    "5절 물류창고 사례: Ocado 또는 다른 창고의 배포 전 검증 사례에서 시작 조건·작업 대상·수행 자원·제약·완료·인계 — 벤더 글 외 독립 출처가 없고 다섯 칸이 미확인이다.",
    "5절: 제조 공장·상업 시설·가정·실외·기타 현장에서 운영 데이터 수집·관측성·소프트웨어 배포(롤백 포함)를 다룬 사례 — 이번 조사에서 찾지 못했다.",
    "6·11절: OpenTelemetry 생성형 AI 토큰 지표의 이전 이름(gen_ai.client.token.usage)과 현재 이름(gen_ai.client.inference.usage.*)의 관계와 변경 시점.",
    "6·7절: FOCUS 1.2 명세 본문(PDF) 열람 — 발표 글만 근거로 했다.",
    "6·11절: 이종 제조사 로봇 기록과 플랫폼 분산 추적을 한 작업 식별자로 잇는 공개 사례·표준, 운행 중 로봇 작업을 끊지 않는 순차 배포·롤백 기준을 공개한 관제 제품·연구.",
    "6·8절: ros2_tracing·ros2probe·LLM 연쇄 계획 논문의 본문 실험 조건(초록 기준 서술을 보강하기 위해).",
    "다음 실행 제안: 38. 모니터링·이상 탐지·원인 분석 페이지에 ros2_tracing·ros2probe·구로병원 로그 분석 결과 반영, 57. 자산·소프트웨어 수명주기 관리 페이지에 Mender A/B 업데이트 반영."
  ],
  "fixes_applied": [
    "f11 강등 — 3·7·9·10절의 접속기록 문장을 모두 [추정]으로 쓰고 7절에 '제2023-6호(2023-09-22 시행 판) 기준이며 이후 개정 여부와 현행 조문(점검 주기 포함)은 미확인'을 밝혔으며 '월 1회 이상 점검'은 본문에서 뺐다.",
    "ref-766 원문 미열람 — 13절 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 ref-766 에 source_unopened: true 와 신뢰도 medium 을 넣었다.",
    "현행 고시 열린 질문 — 11절과 open_question_updates 에 현행 「개인정보의 안전성 확보조치 기준」 접속기록 조항 질문(관련 영역 43·53)을 더하고 additional_research_requests 에 '개인정보보호위원회고시 제2025-9호 제8조와 부칙 시행일 확인'을 넣었다.",
    "f22 한정 — 3절 다섯째 까닭을 '2023-09-22 시행 판 기준 접속기록 보관 의무가 있었다(현행 조문 미확인)'로 한정해 [추정]으로 썼다.",
    "f16 — 5절 병원 사례 완료·인계 칸을 '로봇이 사람 개입 없이 전체 경로를 마치고 약품을 인계'로 쓰고 간호사 수령은 정의에 넣지 않았다.",
    "f17 — 로봇·승강기 로그와 관찰 기록지를 병원 사례의 예외·성과 칸과 서술에 두고 작업 대상 칸은 약품으로 썼으며 site_matrix_updates 도 시작 조건·작업 대상·완료·인계·예외·성과로 맞췄다.",
    "f18 — 성공률·실패 건수를 '저자 보고'로만 옮기고 분모를 계산해 덧붙이지 않았으며, 11절과 open_question_updates 에 성공률 분모 질문(관련 영역 43·63)을 지시 문구대로 올렸다.",
    "5절 미확인 — 병원 사례의 수행 자원·제약과 물류창고 사례의 시작 조건·작업 대상·수행 자원·제약·완료·인계를 '미확인'으로 두고, 제조 공장·상업 시설·가정·실외 사례를 찾지 못했음을 밝혔으며 K3s 실험실 연구와 LLM 계획 평가 실험은 적용 사례로 쓰지 않았다.",
    "f5·f19 벤더 주장 — MCAP 장점과 Ocado 문장을 모두 '[추정] 벤더 주장'으로 쓰고, 6절 첫머리 종합 추정에서 배포 전 시뮬레이션 검증이 벤더 주장 근거임을 별도 문장으로 밝혔다(9·10절에도 같은 한정).",
    "f10 — 6절에서 'Mender README 는 업데이트 중 전원이 끊겨도 동작하던 상태로 되돌릴 수 있다고 설명한다'처럼 출처의 설명으로 서술하고 '연계 대상:'으로 시작했다.",
    "f3·f14 — 3·6·8절에서 ros2probe 와 LLM 연쇄 계획 연구를 '동료 심사 전 arXiv 프리프린트'로 밝혔다.",
    "ref-1049 — reference_updates 의 발행일을 2025-06-03 으로 적고 본문 기준일은 비준일 2025-05-29 로 유지했으며, 각주에 '발행 기관의 발표 글, 명세 본문 미열람'을 밝혔다.",
    "ref-1052 — 참고문헌과 각주의 제목을 'Ocado's digital twins and simulations: driving efficiencies and innovation at scale' 로 고쳤다.",
    "11절 셋째 질문 — '개발 단계인 토큰 지표의 이름(gen_ai.client.inference.usage.* 와 다른 문서의 gen_ai.client.token.usage)이 바뀌었는지 미확인인데'로 고쳐 이름 변경 단정을 없앴고 open_question_updates 에도 같은 문구로 냈다.",
    "10절 교차 규칙 — 토큰 지표·LLM 호출 비용을 44. 로봇 기반 모델·언어 모델 계획, 47. AI·학습·적응과 모델 운영, 13. 대화형 기능의 신뢰·기반에 번호와 이름으로 연결하고, Ocado 사례는 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)에만 연결했으며 18. 실시간 세계 상태·데이터 일관성은 연결하지 않았다.",
    "분량 초과 자동 분리: 43. 데이터·관측성·배포 본문 10,414자 > 기준 4,000자 → 6개 절을 주제 페이지로 옮김, 남은 본문 3,745자"
  ]
}
```

### runs/2026-09-30-06/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 분량 초과 자동 분리:
    - docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-09-30-area43-s6.md (2,750자)
    - docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-09-30-area43-s10.md (1,115자)
    - docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-09-30-area43-s7.md (1,055자)
    - docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-09-30-area43-s4.md (975자)
    - docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md "11. 열린 질문" → docs/topics/2026/2026-09-30-area43-s11.md (889자)
    - docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md "3. 왜 중요한가" → docs/topics/2026/2026-09-30-area43-s3.md (743자)
```

### runs/2026-09-30-06/pages/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md

```markdown
---
title: "43. 데이터·관측성·배포"
type: area
category: "K. 플랫폼 아키텍처·인프라"
area_no: 43
related_areas: [3, 13, 22, 34, 37, 38, 39, 41, 42, 44, 47, 52, 53, 54, 57, 61, 63]
tags: [관측성, OpenTelemetry, MCAP, 무선 업데이트, FinOps]
status: draft
confidence: low
created: 2026-09-28
updated: 2026-09-30
sources: [ref-762, ref-1038, ref-1039, ref-1040, ref-1041, ref-1042, ref-1043, ref-1044, ref-1045, ref-1046, ref-766, ref-1048, ref-1049, ref-943, ref-1051, ref-1052]
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
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
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

공개 자료를 종합하면 플랫폼 자체의 상태·데이터·배포·비용을 관리해야 하는 까닭은 기록의 한계, 관찰의 부담, 실패 원인 분석, 언어 모델 호출 비용, 기록 보관 의무 다섯 가지로 모인다. [추정][^ref-1038][^ref-1039][^ref-943][^ref-1051][^ref-766]

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
| 예외·성과 | 알고리즘과 운영 변경을 실제 창고에 적용하기 전에 시뮬레이션·디지털 트윈에서 시험하고, 12개월 동안 창고 운영 270년 분량을 시뮬레이션했다고 밝힌다. [추정] 벤더 주장[^ref-1052] |

Ocado 는 초당 10회 로봇 통신 같은 실제 운영 데이터로 시뮬레이션 모델을 다듬는다고 밝힌다(2025-06-04). [추정] 벤더 주장[^ref-1052] 이 사례는 배포 전 검증의 근거로만 쓰며, 시뮬레이션 자체는 [34. 시뮬레이션·예측용 디지털 트윈](../design-and-simulation/simulation-and-predictive-digital-twin.md)(가정한 미래를 실험)의 내용이다.

제조 공장·상업 시설·가정·실외 현장의 데이터·관측성·배포 사례는 이번 조사에서 찾지 못했다. 다중 로봇 컨테이너 오케스트레이션 연구와 서비스 로봇 언어 모델 계획 연구는 실험실·평가 실험이므로 적용 사례로 쓰지 않고 6. 대표 접근법과 기술에서 다룬다.

## 6. 대표 접근법과 기술

공개 자료를 종합하면 플랫폼 자체의 관리는 자기 기술형 기록 형식과 기록 DB(데이터), OpenTelemetry 기반 플랫폼 관찰과 저부하 로봇 내부 추적(상태), 컨테이너 자동 재시작·이미지 기반 A/B 롤백·배포 전 시뮬레이션 검증(배포), 표준 청구 데이터와 토큰 지표를 쓰는 FinOps 주기(비용)의 조합으로 보인다. [추정][^ref-1040][^ref-762][^ref-1038][^ref-1039][^ref-1042][^ref-1044][^ref-1045][^ref-1046][^ref-1043][^ref-1048][^ref-1049]

자세한 내용은 주제 페이지 [43. 데이터·관측성·배포 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area43-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역의 도구는 기록(rosbag2·MCAP), 관찰(OpenTelemetry·ros2_tracing), 배포(K3s·Mender), 비용(FinOps·FOCUS)으로 나뉜다. 모든 행은 2026-09-30 확인 기준이다.

자세한 내용은 주제 페이지 [43. 데이터·관측성·배포 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area43-s7.md)에 있다.

## 8. 대표 연구와 자료

아래 다섯 건이 이 영역의 대표 자료이며, 실행 추적·관찰 부담·배포 복원력·호출 비용·현장 기록 분석을 각각 보여 준다.

- Bédard·Lütkebohle·Dagenais, ros2_tracing(IEEE RA-L, 2022-07) — LTTng 기반 ROS 2 계측·추적 도구 모음으로, 로봇 내부 실행을 낮은 부담으로 기록하는 근거다. [사실][^ref-1038]
- Yu·Lee·Choi·Park, ros2probe(arXiv 프리프린트, 2026-06) — 관찰 도구가 대상을 교란하는 문제를 커널 선택 관찰로 줄인 연구로, 관찰 자체의 비용을 따져야 함을 보여 준다. [사실][^ref-1039]
- Zhang·Yu·Westerlund, Kubernetes 를 이용한 ROS 2 다중 로봇 시스템 복원력 연구(Sensors, 2025-08-14) — 컨테이너 자동 재시작으로 장애 중에도 위치 정확도를 유지한 실험실 결과다. [사실][^ref-1045]
- Bruno·Sim·Hagiwara, 서비스 로봇의 LLM 연쇄 기반 작업 계획(arXiv 프리프린트, 2026-09) — 클라우드 API 비용·지연을 동기로 로컬·클라우드 모델을 비교했다. [사실][^ref-1051]
- Lee 외, 혼잡한 병원에서 승강기 이용을 고려한 자율 약품 배송 로봇 실증(Digital Health, 2026-03-31) — 로봇·승강기 로그와 관찰 기록을 함께 모아 실패를 분석한 국내 현장 자료다. [사실][^ref-943]

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

공개 자료를 종합하면 ROP 가 직접 맡을 범위는 플랫폼 서비스의 로그·지표·추적 수집과 보존 정책, 작업 단위 추적 문맥 전파와 로봇 기록(MCAP 등)의 수집·색인 인터페이스, 플랫폼 구성 요소의 배포·롤백·버전 기록과 배포 전 검증, 클라우드·언어 모델 호출 비용의 계측·배분으로 보인다. [추정][^ref-1042][^ref-766][^ref-1040][^ref-1044][^ref-943][^ref-1045][^ref-1052][^ref-1043][^ref-1049] 이 가운데 보존 정책의 국내 근거는 2023-09-22 시행 판 고시 기준(현행 조문 미확인)이고, 배포 전 검증의 사례 근거는 벤더 주장이다. [추정][^ref-766][^ref-1052]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 로봇이 내는 기록·업데이트 상태를 받아 작업 단위로 모으고 색인하는 인터페이스 [추정][^ref-1038][^ref-1046] | 연계 대상: 로봇 운영체제·펌웨어 무선 업데이트, 로봇 내부 ROS 2 실행 추적 [추정][^ref-1038][^ref-1046] |
| 시설·설비 제어 | 승강기 통신 로그를 로봇 기록과 함께 받아 결합 [추정][^ref-943] | 연계 대상: 승강기 통신 로그 생성과 설비 제어 [추정][^ref-943] |

클라우드 청구 데이터를 만드는 일은 클라우드 사업자의 몫이며, ROP 는 그 데이터를 받아 모으는 쪽을 맡을 것으로 보인다. [추정][^ref-1049] 경계의 기준은 [범위 경계](../../about/scope-boundary.md)에 있다.

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 기록을 쓰는 관제·분석 영역, 배포·검증 영역, 비용·규제 영역, 언어 모델 영역, 적용 현장과 이어진다.

자세한 내용은 주제 페이지 [43. 데이터·관측성·배포 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area43-s10.md)에 있다.

## 11. 열린 질문

아래 질문은 이번 실행에서 새로 올렸다. 번호는 퍼블리셔가 부여하며 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [43. 데이터·관측성·배포 — 열린 질문](../../topics/2026/2026-09-30-area43-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-762]: Open Robotics (open-rmf), rmf-web — packages/api-server/README.md, 미확인, https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md, 접근일 2026-09-30
[^ref-1038]: Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L, arXiv), ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2, 2022-07, https://arxiv.org/abs/2201.00393, 접근일 2026-09-30
[^ref-1039]: Yu, J., Lee, S., Choi, Y., & Park, K.-J. (arXiv), ros2probe: Non-intrusive, Kernel-selective Observability for Robot Operating System 2 Middleware, 2026-06, https://arxiv.org/abs/2606.10746, 접근일 2026-09-30
[^ref-1040]: Open Robotics (ROS 2 Documentation), Iron Irwini (iron), 2023-05-23, https://docs.ros.org/en/rolling/Releases/Release-Iron-Irwini.html, 접근일 2026-09-30
[^ref-1042]: OpenTelemetry (CNCF), Specification Status Summary, 미확인, https://opentelemetry.io/docs/specs/status/, 접근일 2026-09-30
[^ref-1043]: OpenTelemetry (open-telemetry/semantic-conventions-genai), semantic-conventions-genai/docs/gen-ai/gen-ai-token-metrics.md, 미확인, https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md, 접근일 2026-09-30
[^ref-1044]: szobov (GitHub), ros-opentelemetry — ROS2 x OpenTelemetry README, 미확인, https://github.com/szobov/ros-opentelemetry, 접근일 2026-09-30
[^ref-1045]: Zhang, J., Yu, X., & Westerlund, T. (Sensors 25(16):5067), Enhancing the Resilience of ROS 2-Based Multi-Robot Systems with Kubernetes: A Case Study on UWB-Based Relative Positioning, 2025-08-14, https://pmc.ncbi.nlm.nih.gov/articles/PMC12390455/, 접근일 2026-09-30
[^ref-1046]: Northern.tech (mendersoftware), mender — README, 미확인, https://github.com/mendersoftware/mender, 접근일 2026-09-30
[^ref-766]: 개인정보보호위원회 (국가법령정보센터), 개인정보의 안전성 확보조치 기준 (개인정보보호위원회고시 제2023-6호), 2023-09-22, https://www.law.go.kr/admRulLsInfoP.do?chrClsCd=010202&admRulSeq=2100000229672, 접근일 2026-09-30 (원문 미열람)
[^ref-1048]: FinOps Foundation, FinOps Phases, 미확인, https://www.finops.org/framework/phases/, 접근일 2026-09-30
[^ref-1049]: FinOps Foundation, Introducing FOCUS 1.2: SaaS/PaaS Support, Invoice Reconciliation, and more (발행 기관의 발표 글, 명세 본문 미열람), 2025-06-03, https://www.finops.org/insights/focus-1-2-available/, 접근일 2026-09-30
[^ref-943]: Lee, Y., Kim, S.-E., Kim, J. S. 외 (Digital Health 12), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-09-30
[^ref-1051]: Bruno, L. D. M., Sim, J., & Hagiwara, Y. (arXiv), Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots, 2026-09, https://arxiv.org/abs/2609.29043, 접근일 2026-09-30
[^ref-1052]: Ocado Group, Ocado's digital twins and simulations: driving efficiencies and innovation at scale, 2025-06-04, https://www.ocadogroup.com/newsroom/stories/digital-twins-and-simulations, 접근일 2026-09-30
```

### docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md

```markdown
---
title: "43. 데이터·관측성·배포"
type: area
category: "K. 플랫폼 아키텍처·인프라"
area_no: 43
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [K. 플랫폼 아키텍처·인프라](index.md) › 43. 데이터·관측성·배포

# 43. 데이터·관측성·배포

!!! info "소속 대분류"
    [K. 플랫폼 아키텍처·인프라](index.md) — 핵심 질문:
    플랫폼을 어디에 어떻게 두어야 끊김·확장·다현장 조건에서도 계속 동작하는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
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

### runs/2026-09-30-06/pages/topics/2026/2026-09-30-area43-s6.md

```markdown
---
title: "43. 데이터·관측성·배포 — 대표 접근법과 기술"
type: topic
category: "K. 플랫폼 아키텍처·인프라"
primary_area_no: 43
related_areas: [3, 13, 22, 34, 37, 38, 39, 41, 42, 44, 47, 52, 53, 54, 57, 61, 63]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1038, ref-1039, ref-1040, ref-1041, ref-1042, ref-1043, ref-1044, ref-1045, ref-1046, ref-1048, ref-1049, ref-1051, ref-1052, ref-762]
last_run: 2026-09-30
version: 1
split_from: docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md#6
---

[홈](../../index.md) › [주제](../index.md) › 43. 데이터·관측성·배포 — 대표 접근법과 기술

# 43. 데이터·관측성·배포 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 공개 자료를 종합하면 플랫폼 자체의 관리는 자기 기술형 기록 형식과 기록 DB(데이터), OpenTelemetry 기반 플랫폼 관찰과 저부하 로봇 내부 추적(상태), 컨테이너 자동 재시작·이미지 기반 A/B 롤백·배포 전 시뮬레이션 검증(배포), 표준 청구 데이터와 토큰 지표를 쓰는 FinOps 주기(비용)의 조합으로 보인다. [추정][^ref-1040][^ref-762][^ref-1038][^ref-1039][^ref-1042][^ref-1044][^ref-1045][^ref-1046][^ref-1043][^ref-1048][^ref-1049]
- 이 페이지는 [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

공개 자료를 종합하면 플랫폼 자체의 관리는 자기 기술형 기록 형식과 기록 DB(데이터), OpenTelemetry 기반 플랫폼 관찰과 저부하 로봇 내부 추적(상태), 컨테이너 자동 재시작·이미지 기반 A/B 롤백·배포 전 시뮬레이션 검증(배포), 표준 청구 데이터와 토큰 지표를 쓰는 FinOps 주기(비용)의 조합으로 보인다. [추정][^ref-1040][^ref-762][^ref-1038][^ref-1039][^ref-1042][^ref-1044][^ref-1045][^ref-1046][^ref-1043][^ref-1048][^ref-1049] 이 가운데 배포 전 시뮬레이션 검증은 벤더 주장에 기댄 부분이다. [추정] 벤더 주장[^ref-1052]

### 데이터: 기록 형식과 기록 DB

ROS 2 Iron Irwini(2023-05-23)부터 rosbag2 는 새 백 파일의 기본 기록 형식을 sqlite3 에서 MCAP 로 바꿨다. [사실][^ref-1040][^ref-1041] 같은 판에서 서비스 호출로 원격에서 기록을 일시 정지·재개·분할하는 기능도 더해졌다. [사실][^ref-1040] Foxglove 는 MCAP 이 SQLite3 '복원력' 모드 수준의 데이터 안전성과 '쓰기 최적화' 모드 수준의 쓰기 처리량을 함께 제공하고 zstd·lz4 압축을 고를 수 있다고 주장한다(2022-12-22). [추정] 벤더 주장[^ref-1041]

플랫폼 쪽 기록은 별도 DB 에 둔다. Open-RMF 의 웹 API 서버는 기록용 데이터베이스로 tortoise-orm 을 통해 PostgreSQL·SQLite·MySQL·MariaDB 를 지원하며 기본값은 메모리 SQLite 다(2026-09-30 확인). [사실][^ref-762]

### 상태: 플랫폼 관찰과 로봇 내부 추적

OpenTelemetry 명세 상태 요약(2026-09-30 확인)에서 추적은 API·SDK·프로토콜이 모두 안정이고 장기 지원 대상이며, 로그는 브리지 API·SDK·프로토콜이 안정, 지표는 API·프로토콜이 안정이나 SDK 는 혼합 상태, 프로파일은 프로토콜이 개발 단계다. [사실][^ref-1042]

ROS 2 쪽에서는 오픈소스 ros-opentelemetry 가 송신 측이 추적 문맥을 메시지의 사용자 정의 필드에 넣고 수신 측이 꺼내 잇는 방식으로 토픽·서비스·액션을 가로지르는 분산 추적을 C++·Python 노드에 제공하고, 로그를 추적 구간(span)에 연결하는 로거를 둔다. [사실][^ref-1044] 개인이 관리하는 저장소이며 라이선스 표기는 확인하지 못했다. [사실][^ref-1044]

로봇 내부 실행은 저부하 추적으로 본다. ros2_tracing 은 ROS 2 계측을 모두 켰을 때 종단 간 메시지 지연 증가가 평균 0.0033 ms 라고 보고했다(2022-07, 초록 기준). [사실][^ref-1038] ros2probe 는 도메인에 참여하지 않고 탐색 패킷으로 통신 그래프를 복원한 뒤 사용자가 지정한 토픽만 커널 안에서 걸러 관찰해, 관찰자 CPU 사용을 최대 7배·메모리를 최대 28배 줄이고 포화 조건에서 도메인 참여형 도구가 38.5% 메시지를 잃을 때 손실 0을 보고했다(2026-06, 동료 심사 전 arXiv 프리프린트). [사실][^ref-1039]

### 배포: 자동 재시작, 이미지 기반 롤백, 배포 전 검증

Zhang·Yu·Westerlund 는 TurtleBot4 에 얹은 Jetson Nano 5대와 마스터 노트북 1대로 된 K3s 클러스터에서 컨테이너화한 ROS 2 노드로 다중 로봇 UWB(Ultra-Wideband) 상대 위치 추정을 운영했다(2025-08). [사실][^ref-1045] 오차 보정용 LSTM(Long Short-Term Memory) 파드 5개를 모두 종료시켜도 Kubernetes 가 파드를 자동 재시작해 위치 오차(APE)가 약 0.12~0.14 m 로 장애 없는 경우와 비슷하게 유지됐다. [사실][^ref-1045] 실험실 환경이며 복구 시간은 보고되지 않았다. [사실][^ref-1045]

연계 대상: 로봇·장치 쪽 업데이트에는 Mender 같은 클라이언트–서버 방식 무선 업데이트 관리자가 있다. Mender 는 이중 A/B 루트 파일시스템 분할에 이미지 단위로 원자적 배포를 하며, Mender README 는 업데이트 중 전원이 끊겨도 동작하던 상태로 되돌릴 수 있다고 설명한다. [사실][^ref-1046] 루트 파일시스템·애플리케이션·파일·컨테이너 업데이트를 지원하고 Apache 2.0 라이선스로 공개된다(2026-09-30 확인). [사실][^ref-1046]

배포 전 검증으로는 Ocado 가 창고 로봇 교통 관리·오케스트레이션 알고리즘과 운영 변경을 실제 창고에 적용하기 전에 시뮬레이션·디지털 트윈에서 시험한다고 밝힌다(2025-06-04). [추정] 벤더 주장[^ref-1052]

### 비용: 표준 청구 데이터·토큰 지표·FinOps 주기

FinOps 재단은 기술 비용·사용량·효율 데이터를 수집·배분·보고·예측하는 정보, 사용량 최적화와 요금 최적화를 찾는 최적화, 엔지니어링·재무·사업 팀이 함께 개선을 실행하는 운영의 세 단계를 반복하는 방식으로 FinOps 를 설명하고, 대상에 공용 클라우드·SaaS(Software as a Service)와 함께 AI 서비스를 든다(2026-09-30 확인). [사실][^ref-1048]

청구 데이터 명세 FOCUS 1.2(2025-05-29 비준)는 SaaS·PaaS(Platform as a Service) 청구 데이터를 클라우드 비용과 같은 스키마에 넣고, 크레딧·토큰 같은 가상 통화와 다중 통화 정규화, 청구서 연결용 InvoiceId 열을 더했으며, AWS·Microsoft·Google Cloud·Oracle Cloud·Alibaba Cloud·Databricks·Grafana 가 지원을 밝혔다(발행 기관 발표 글 기준). [사실][^ref-1049]

언어 모델 호출에 대해서는 OpenTelemetry 생성형 AI 의미 규약이 입력·출력·캐시 읽기·캐시 쓰기 입력·추론 출력 토큰 카운터와 호출별 입력·출력 토큰 히스토그램을 정의하고, 작업 이름·제공자 이름을 필수 속성으로 둔다. [사실][^ref-1043] 이 지표는 모두 개발 단계다(2026-09-30 확인). [사실][^ref-1043] 로봇 쪽 연구로는 두 단계 연쇄(chaining) 계획으로 추론당 프롬프트 길이를 약 45% 줄여 로컬 모델(Qwen2.5-14B·Cogito-14B)의 계획 성공을 최대 37%p 높이고 클라우드 모델(Claude Sonnet 4.6)과 비교한 결과가 있다(2026-09, 동료 심사 전 arXiv 프리프린트). [사실][^ref-1051] 이 연구는 비용 금액을 보고하지 않았다. [사실][^ref-1051]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1038]: Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L, arXiv), ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2, 2022-07, https://arxiv.org/abs/2201.00393, 접근일 2026-09-30
[^ref-1039]: Yu, J., Lee, S., Choi, Y., & Park, K.-J. (arXiv), ros2probe: Non-intrusive, Kernel-selective Observability for Robot Operating System 2 Middleware, 2026-06, https://arxiv.org/abs/2606.10746, 접근일 2026-09-30
[^ref-1040]: Open Robotics (ROS 2 Documentation), Iron Irwini (iron), 2023-05-23, https://docs.ros.org/en/rolling/Releases/Release-Iron-Irwini.html, 접근일 2026-09-30
[^ref-1041]: Foxglove, MCAP as the ROS 2 Default Bag Format, 2022-12-22, https://foxglove.dev/blog/mcap-as-the-ros2-default-bag-format, 접근일 2026-09-30
[^ref-1042]: OpenTelemetry (CNCF), Specification Status Summary, 미확인, https://opentelemetry.io/docs/specs/status/, 접근일 2026-09-30
[^ref-1043]: OpenTelemetry (open-telemetry/semantic-conventions-genai), semantic-conventions-genai/docs/gen-ai/gen-ai-token-metrics.md, 미확인, https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md, 접근일 2026-09-30
[^ref-1044]: szobov (GitHub), ros-opentelemetry — ROS2 x OpenTelemetry README, 미확인, https://github.com/szobov/ros-opentelemetry, 접근일 2026-09-30
[^ref-1045]: Zhang, J., Yu, X., & Westerlund, T. (Sensors 25(16):5067), Enhancing the Resilience of ROS 2-Based Multi-Robot Systems with Kubernetes: A Case Study on UWB-Based Relative Positioning, 2025-08-14, https://pmc.ncbi.nlm.nih.gov/articles/PMC12390455/, 접근일 2026-09-30
[^ref-1046]: Northern.tech (mendersoftware), mender — README, 미확인, https://github.com/mendersoftware/mender, 접근일 2026-09-30
[^ref-1048]: FinOps Foundation, FinOps Phases, 미확인, https://www.finops.org/framework/phases/, 접근일 2026-09-30
[^ref-1049]: FinOps Foundation, Introducing FOCUS 1.2: SaaS/PaaS Support, Invoice Reconciliation, and more (발행 기관의 발표 글, 명세 본문 미열람), 2025-06-03, https://www.finops.org/insights/focus-1-2-available/, 접근일 2026-09-30
[^ref-1051]: Bruno, L. D. M., Sim, J., & Hagiwara, Y. (arXiv), Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots, 2026-09, https://arxiv.org/abs/2609.29043, 접근일 2026-09-30
[^ref-1052]: Ocado Group, Ocado's digital twins and simulations: driving efficiencies and innovation at scale, 2025-06-04, https://www.ocadogroup.com/newsroom/stories/digital-twins-and-simulations, 접근일 2026-09-30
[^ref-762]: Open Robotics (open-rmf), rmf-web — packages/api-server/README.md, 미확인, https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-06 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-06 | 43. 데이터·관측성·배포 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-30-06/pages/topics/2026/2026-09-30-area43-s10.md

```markdown
---
title: "43. 데이터·관측성·배포 — 다른 연구영역과의 연결"
type: topic
category: "K. 플랫폼 아키텍처·인프라"
primary_area_no: 43
related_areas: [3, 13, 22, 34, 37, 38, 39, 41, 42, 44, 47, 52, 53, 54, 57, 61, 63]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1038, ref-1043, ref-1045, ref-1046, ref-766, ref-1048, ref-1049, ref-943, ref-1051, ref-1052, ref-762]
last_run: 2026-09-30
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

- [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md) — FinOps 주기와 표준 청구 데이터로 계측한 비용이 경제성 판단의 입력이 된다. [추정][^ref-1048][^ref-1049]
- [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) — 언어 모델 호출의 토큰·비용·지연 계측이 대화형 기능 운영의 기반이 된다. [추정][^ref-1043][^ref-1051]
- [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) — 승강기 통신 로그처럼 설비가 낸 기록을 로봇 기록과 함께 모은다. [추정][^ref-943]
- [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md) — 배포 전 검증에 쓰는 시뮬레이션(가정한 미래를 실험)을 맡으며, 이번 근거는 벤더 사례다. [추정][^ref-1052]
- [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) — 플랫폼 기록 DB 와 로봇·설비 로그가 실행 기록의 원천이다. [추정][^ref-762][^ref-943]
- [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md) — 로그·추적으로 원인을 찾는 분석의 입력을 이 영역이 모은다. [추정][^ref-1038][^ref-943]
- [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md) — 성공률·실패 유형 같은 성과 지표가 기록에서 나온다. [추정][^ref-943]
- [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md) — 기록 DB 를 어디에 어떻게 둘지는 아키텍처 결정과 이어진다. [추정][^ref-762]
- [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md) — 컨테이너 오케스트레이션과 ROS 2 통신 구조가 배포·복구의 바탕이다. [추정][^ref-1045]
- [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) — 로컬·클라우드 모델 선택이 호출 비용과 지연을 좌우한다. [추정][^ref-1051]
- [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) — 언어 모델 운영의 토큰 사용량 계측을 이 영역이 받친다. [추정][^ref-1043]
- [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) — 접속기록의 위변조 방지 보관은 감사와 맞닿는다(2023-6호 기준, 현행 미확인). [추정][^ref-766]
- [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md) — 접속기록 보관 기준과 영상·주행 기록 보존 기간 문제가 겹친다. [추정][^ref-766]
- [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md) — 배포 전 검증이 시험 절차와 이어진다. [추정][^ref-1052]
- [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) — 장치 소프트웨어 업데이트와 버전 기록을 수명주기 관리와 나눠 맡는다. [추정][^ref-1046]
- [61. 물류창고](../../categories/site-type-applications/warehouse.md) — 창고 알고리즘 변경을 적용 전에 시뮬레이션으로 검증한다는 벤더 사례가 있다. [추정][^ref-1052]
- [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) — 약품 배송 로봇 실증이 기록 기반 실패 분석 사례다. [추정][^ref-943]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1038]: Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L, arXiv), ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2, 2022-07, https://arxiv.org/abs/2201.00393, 접근일 2026-09-30
[^ref-1043]: OpenTelemetry (open-telemetry/semantic-conventions-genai), semantic-conventions-genai/docs/gen-ai/gen-ai-token-metrics.md, 미확인, https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md, 접근일 2026-09-30
[^ref-1045]: Zhang, J., Yu, X., & Westerlund, T. (Sensors 25(16):5067), Enhancing the Resilience of ROS 2-Based Multi-Robot Systems with Kubernetes: A Case Study on UWB-Based Relative Positioning, 2025-08-14, https://pmc.ncbi.nlm.nih.gov/articles/PMC12390455/, 접근일 2026-09-30
[^ref-1046]: Northern.tech (mendersoftware), mender — README, 미확인, https://github.com/mendersoftware/mender, 접근일 2026-09-30
[^ref-766]: 개인정보보호위원회 (국가법령정보센터), 개인정보의 안전성 확보조치 기준 (개인정보보호위원회고시 제2023-6호), 2023-09-22, https://www.law.go.kr/admRulLsInfoP.do?chrClsCd=010202&admRulSeq=2100000229672, 접근일 2026-09-30 (원문 미열람)
[^ref-1048]: FinOps Foundation, FinOps Phases, 미확인, https://www.finops.org/framework/phases/, 접근일 2026-09-30
[^ref-1049]: FinOps Foundation, Introducing FOCUS 1.2: SaaS/PaaS Support, Invoice Reconciliation, and more (발행 기관의 발표 글, 명세 본문 미열람), 2025-06-03, https://www.finops.org/insights/focus-1-2-available/, 접근일 2026-09-30
[^ref-943]: Lee, Y., Kim, S.-E., Kim, J. S. 외 (Digital Health 12), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-09-30
[^ref-1051]: Bruno, L. D. M., Sim, J., & Hagiwara, Y. (arXiv), Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots, 2026-09, https://arxiv.org/abs/2609.29043, 접근일 2026-09-30
[^ref-1052]: Ocado Group, Ocado's digital twins and simulations: driving efficiencies and innovation at scale, 2025-06-04, https://www.ocadogroup.com/newsroom/stories/digital-twins-and-simulations, 접근일 2026-09-30
[^ref-762]: Open Robotics (open-rmf), rmf-web — packages/api-server/README.md, 미확인, https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-06 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-06 | 43. 데이터·관측성·배포 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-30-06/pages/topics/2026/2026-09-30-area43-s7.md

```markdown
---
title: "43. 데이터·관측성·배포 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "K. 플랫폼 아키텍처·인프라"
primary_area_no: 43
related_areas: [3, 13, 22, 34, 37, 38, 39, 41, 42, 44, 47, 52, 53, 54, 57, 61, 63]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1038, ref-1039, ref-1040, ref-1041, ref-1042, ref-1043, ref-1044, ref-1045, ref-1046, ref-766, ref-1048, ref-1049]
last_run: 2026-09-30
version: 1
split_from: docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md#7
---

[홈](../../index.md) › [주제](../index.md) › 43. 데이터·관측성·배포 — 관련 표준·프레임워크·오픈소스

# 43. 데이터·관측성·배포 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 도구는 기록(rosbag2·MCAP), 관찰(OpenTelemetry·ros2_tracing), 배포(K3s·Mender), 비용(FinOps·FOCUS)으로 나뉜다. 모든 행은 2026-09-30 확인 기준이다.
- 이 페이지는 [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 도구는 기록(rosbag2·MCAP), 관찰(OpenTelemetry·ros2_tracing), 배포(K3s·Mender), 비용(FinOps·FOCUS)으로 나뉜다. 모든 행은 2026-09-30 확인 기준이다.

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| rosbag2·MCAP | 오픈소스 | ROS 2 기록 도구와 Iron Irwini 부터의 기본 기록 형식, 원격 기록 제어 서비스 | [^ref-1040][^ref-1041] |
| ros2_tracing | 오픈소스 | LTTng 기반 ROS 2 실행 추적, 운영체제 추적과 결합 | [^ref-1038] |
| ros2probe | 프레임워크 | 커널 안 필터로 지정 토픽만 관찰하는 연구 프레임워크(프리프린트) | [^ref-1039] |
| OpenTelemetry 명세 | 오픈소스 | 플랫폼 서비스의 추적·지표·로그 수집, 신호별 안정성 상태 | [^ref-1042] |
| OpenTelemetry 생성형 AI 의미 규약(토큰 지표) | 오픈소스 | 언어 모델 호출 토큰 계측, 개발 단계 | [^ref-1043] |
| ros-opentelemetry | 오픈소스 | ROS 2 메시지 간 추적 문맥 전파와 로그 연결 | [^ref-1044] |
| K3s(Kubernetes) | 오픈소스 | 다중 로봇 연구에서 컨테이너화한 ROS 2 노드의 배포·자동 재시작에 쓰임 | [^ref-1045] |
| Mender | 오픈소스 | 연계 대상: 장치 무선 업데이트와 A/B 롤백 | [^ref-1046] |
| FinOps 프레임워크 | 프레임워크 | 비용의 정보·최적화·운영 주기 | [^ref-1048] |
| FOCUS 1.2 | 표준 | 클라우드·SaaS 청구 데이터 공통 스키마, 가상 통화(토큰) 포함 | [^ref-1049] |

국내 규제로는 개인정보보호위원회 「개인정보의 안전성 확보조치 기준」(고시 제2023-6호, 2023-09-22 시행 판) 제8조가 개인정보취급자의 접속기록을 1년 이상(5만 명 이상의 정보주체 개인정보를 처리하는 시스템 등은 2년 이상) 보관하고 위조·변조·도난·분실되지 않게 관리하도록 정했던 것으로 보인다. [추정][^ref-766] 이는 2023-6호 판 기준이며 이후 개정 여부와 현행 조문(점검 주기 포함)은 미확인이다. [추정][^ref-766]

전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1038]: Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L, arXiv), ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2, 2022-07, https://arxiv.org/abs/2201.00393, 접근일 2026-09-30
[^ref-1039]: Yu, J., Lee, S., Choi, Y., & Park, K.-J. (arXiv), ros2probe: Non-intrusive, Kernel-selective Observability for Robot Operating System 2 Middleware, 2026-06, https://arxiv.org/abs/2606.10746, 접근일 2026-09-30
[^ref-1040]: Open Robotics (ROS 2 Documentation), Iron Irwini (iron), 2023-05-23, https://docs.ros.org/en/rolling/Releases/Release-Iron-Irwini.html, 접근일 2026-09-30
[^ref-1041]: Foxglove, MCAP as the ROS 2 Default Bag Format, 2022-12-22, https://foxglove.dev/blog/mcap-as-the-ros2-default-bag-format, 접근일 2026-09-30
[^ref-1042]: OpenTelemetry (CNCF), Specification Status Summary, 미확인, https://opentelemetry.io/docs/specs/status/, 접근일 2026-09-30
[^ref-1043]: OpenTelemetry (open-telemetry/semantic-conventions-genai), semantic-conventions-genai/docs/gen-ai/gen-ai-token-metrics.md, 미확인, https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md, 접근일 2026-09-30
[^ref-1044]: szobov (GitHub), ros-opentelemetry — ROS2 x OpenTelemetry README, 미확인, https://github.com/szobov/ros-opentelemetry, 접근일 2026-09-30
[^ref-1045]: Zhang, J., Yu, X., & Westerlund, T. (Sensors 25(16):5067), Enhancing the Resilience of ROS 2-Based Multi-Robot Systems with Kubernetes: A Case Study on UWB-Based Relative Positioning, 2025-08-14, https://pmc.ncbi.nlm.nih.gov/articles/PMC12390455/, 접근일 2026-09-30
[^ref-1046]: Northern.tech (mendersoftware), mender — README, 미확인, https://github.com/mendersoftware/mender, 접근일 2026-09-30
[^ref-766]: 개인정보보호위원회 (국가법령정보센터), 개인정보의 안전성 확보조치 기준 (개인정보보호위원회고시 제2023-6호), 2023-09-22, https://www.law.go.kr/admRulLsInfoP.do?chrClsCd=010202&admRulSeq=2100000229672, 접근일 2026-09-30 (원문 미열람)
[^ref-1048]: FinOps Foundation, FinOps Phases, 미확인, https://www.finops.org/framework/phases/, 접근일 2026-09-30
[^ref-1049]: FinOps Foundation, Introducing FOCUS 1.2: SaaS/PaaS Support, Invoice Reconciliation, and more (발행 기관의 발표 글, 명세 본문 미열람), 2025-06-03, https://www.finops.org/insights/focus-1-2-available/, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-06 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-06 | 43. 데이터·관측성·배포 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-30-06/pages/topics/2026/2026-09-30-area43-s4.md

```markdown
---
title: "43. 데이터·관측성·배포 — 핵심 개념과 용어"
type: topic
category: "K. 플랫폼 아키텍처·인프라"
primary_area_no: 43
related_areas: [3, 13, 22, 34, 37, 38, 39, 41, 42, 44, 47, 52, 53, 54, 57, 61, 63]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1038, ref-1040, ref-1041, ref-1042, ref-1043, ref-1044, ref-1046, ref-1048, ref-1049]
last_run: 2026-09-30
version: 1
split_from: docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md#4
---

[홈](../../index.md) › [주제](../index.md) › 43. 데이터·관측성·배포 — 핵심 개념과 용어

# 43. 데이터·관측성·배포 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 용어는 기록·관찰·배포·비용 순서로 둔다.
- 이 페이지는 [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

용어는 기록·관찰·배포·비용 순서로 둔다.

- **[백 파일](../../glossary/bag-file.md)(Bag File)과 MCAP** — ROS 2 Iron Irwini(2023-05-23 출시)부터 rosbag2 가 새 백 파일을 기록하는 기본 형식은 sqlite3 에서 MCAP 로 바뀌었다. [사실][^ref-1040][^ref-1041] MCAP 은 메시지 정의를 파일 안에 담아 외부 스키마 없이 다른 도구가 읽을 수 있다고 개발사는 설명한다. [추정] 벤더 주장[^ref-1041]
- **OpenTelemetry** — 추적(tracing)·지표(metrics)·로그·프로파일(profiles)을 신호로 다루는 관측성(Observability) 명세이며, 2026-09-30 확인 기준 추적은 API·SDK·프로토콜이 모두 안정(stable) 단계다. [사실][^ref-1042]
- **실행 추적(execution tracing)** — ros2_tracing 은 저부하 추적기 LTTng 로 ROS 2 의 실행 정보를 수집하고, 그 데이터를 운영체제 추적과 결합할 수 있다. [사실][^ref-1038]
- **[분산 추적](../../glossary/distributed-tracing.md)(Distributed Tracing)** — 추적 문맥을 메시지에 실어 여러 노드를 가로지르는 한 흐름으로 잇는다. ros-opentelemetry 는 이를 ROS 2 메시지의 사용자 정의 필드로 전파한다. [사실][^ref-1044]
- **생성형 AI 토큰 지표** — OpenTelemetry 생성형 AI 의미 규약이 정의하는 언어 모델 호출의 입력·출력·캐시·추론 토큰 계측 지표이며, 2026-09-30 확인 기준 모두 개발(Development) 단계다. [사실][^ref-1043]
- **A/B 분할 업데이트** — 루트 파일시스템을 두 벌(A/B)로 나눠 이미지 단위로 원자적으로 배포하는 [무선 업데이트](../../glossary/over-the-air-update.md)(Over-the-Air Update, OTA) 방식이다. [사실][^ref-1046]
- **FinOps 와 FOCUS** — FinOps 는 기술 비용·사용량 데이터를 정보(Inform)·최적화(Optimize)·운영(Operate) 세 단계로 반복 관리하는 방식이고 [사실][^ref-1048], FOCUS 는 FinOps 재단의 청구 데이터 명세다. [사실][^ref-1049]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1038]: Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L, arXiv), ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2, 2022-07, https://arxiv.org/abs/2201.00393, 접근일 2026-09-30
[^ref-1040]: Open Robotics (ROS 2 Documentation), Iron Irwini (iron), 2023-05-23, https://docs.ros.org/en/rolling/Releases/Release-Iron-Irwini.html, 접근일 2026-09-30
[^ref-1041]: Foxglove, MCAP as the ROS 2 Default Bag Format, 2022-12-22, https://foxglove.dev/blog/mcap-as-the-ros2-default-bag-format, 접근일 2026-09-30
[^ref-1042]: OpenTelemetry (CNCF), Specification Status Summary, 미확인, https://opentelemetry.io/docs/specs/status/, 접근일 2026-09-30
[^ref-1043]: OpenTelemetry (open-telemetry/semantic-conventions-genai), semantic-conventions-genai/docs/gen-ai/gen-ai-token-metrics.md, 미확인, https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md, 접근일 2026-09-30
[^ref-1044]: szobov (GitHub), ros-opentelemetry — ROS2 x OpenTelemetry README, 미확인, https://github.com/szobov/ros-opentelemetry, 접근일 2026-09-30
[^ref-1046]: Northern.tech (mendersoftware), mender — README, 미확인, https://github.com/mendersoftware/mender, 접근일 2026-09-30
[^ref-1048]: FinOps Foundation, FinOps Phases, 미확인, https://www.finops.org/framework/phases/, 접근일 2026-09-30
[^ref-1049]: FinOps Foundation, Introducing FOCUS 1.2: SaaS/PaaS Support, Invoice Reconciliation, and more (발행 기관의 발표 글, 명세 본문 미열람), 2025-06-03, https://www.finops.org/insights/focus-1-2-available/, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-06 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-06 | 43. 데이터·관측성·배포 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-30-06/pages/topics/2026/2026-09-30-area43-s11.md

```markdown
---
title: "43. 데이터·관측성·배포 — 열린 질문"
type: topic
category: "K. 플랫폼 아키텍처·인프라"
primary_area_no: 43
related_areas: [3, 13, 22, 34, 37, 38, 39, 41, 42, 44, 47, 52, 53, 54, 57, 61, 63]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-09-30
updated: 2026-09-30
sources: []
last_run: 2026-09-30
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

- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-06) 서로 다른 제조사 로봇의 기록(MCAP·제조사 로그)과 플랫폼 서비스의 분산 추적을 하나의 작업 식별자로 이어 원인 분석에 쓴 공개 사례나 표준이 있는가?
- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-06) 로봇 플랫폼이 수집하는 텔레메트리·주행 기록·영상의 보존 기간을 정한 국내 기준이나 운영 사례가 개인정보 접속기록 규정 밖에도 있는가?
- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-06) 개발 단계인 토큰 지표의 이름(gen_ai.client.inference.usage.* 와 다른 문서의 gen_ai.client.token.usage)이 바뀌었는지 미확인인데, 언어 모델 호출 비용 계측을 안정 판이 나오기 전까지 어떤 기준으로 고정할 것인가?
- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-06) 운행 중인 로봇 작업을 끊지 않고 현장 서버·로봇에 플랫폼 소프트웨어를 순차 배포하고 되돌리는 시점·기준을 공개한 로봇 관제 제품이나 연구가 있는가?
- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-06) 로봇 플랫폼에 적용될 수 있는 현행 「개인정보의 안전성 확보조치 기준」(2023-6호 이후 개정판)의 접속기록 보관 기간·점검 주기 조항이 2023-6호와 같은가?
- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-06) 구로병원 실증의 전체 성공률 87.03% 가 122건 중 실패 14건과 맞지 않는데(약 88.5%) 성공률의 분모는 무엇인가?

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

이 절에는 각주가 없다.

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-06 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-06 | 43. 데이터·관측성·배포 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-30-06/pages/topics/2026/2026-09-30-area43-s3.md

```markdown
---
title: "43. 데이터·관측성·배포 — 왜 중요한가"
type: topic
category: "K. 플랫폼 아키텍처·인프라"
primary_area_no: 43
related_areas: [3, 13, 22, 34, 37, 38, 39, 41, 42, 44, 47, 52, 53, 54, 57, 61, 63]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1038, ref-1039, ref-766, ref-943, ref-1051]
last_run: 2026-09-30
version: 1
split_from: docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md#3
---

[홈](../../index.md) › [주제](../index.md) › 43. 데이터·관측성·배포 — 왜 중요한가

# 43. 데이터·관측성·배포 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 공개 자료를 종합하면 플랫폼 자체의 상태·데이터·배포·비용을 관리해야 하는 까닭은 기록의 한계, 관찰의 부담, 실패 원인 분석, 언어 모델 호출 비용, 기록 보관 의무 다섯 가지로 모인다. [추정][^ref-1038][^ref-1039][^ref-943][^ref-1051][^ref-766]
- 이 페이지는 [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

공개 자료를 종합하면 플랫폼 자체의 상태·데이터·배포·비용을 관리해야 하는 까닭은 기록의 한계, 관찰의 부담, 실패 원인 분석, 언어 모델 호출 비용, 기록 보관 의무 다섯 가지로 모인다. [추정][^ref-1038][^ref-1039][^ref-943][^ref-1051][^ref-766]

첫째, ROS 2 실행 추적 도구 ros2_tracing 의 저자들은 미들웨어 수준의 표준 데이터 기록만으로는 내부 계산과 성능 병목을 알기에 정보가 부족하다고 보고, 이를 실행 추적 도구가 필요한 이유로 든다(2022-07). [사실][^ref-1038] 둘째, 관찰 도구가 ROS 2 도메인에 구독자로 참여하면 탐색(discovery) 부담과 역직렬화 비용을 더해 관찰 대상을 교란한다는 보고가 있다(2026-06, 동료 심사 전 arXiv 프리프린트). [사실][^ref-1039]

셋째, 국내 병원의 약품 배송 로봇 실증은 로봇 시스템 로그·승강기 통신 로그·관찰자 기록지를 함께 모아 실패를 분석했다(2026-03). [사실][^ref-943] 실패 원인이 로봇 기록과 설비 기록을 함께 모아야 드러난다는 뜻으로 읽힌다. [추정][^ref-943]

넷째, 클라우드 언어 모델 API 는 로봇이 긴 작업을 반복할수록 요청당 비용이 쌓이고 네트워크 지연이 실시간 반응을 떨어뜨린다는 지적이 있다(2026-09, 동료 심사 전 arXiv 프리프린트). [사실][^ref-1051] 다섯째, 「개인정보의 안전성 확보조치 기준」 제2023-6호(2023-09-22 시행 판) 기준으로 개인정보처리시스템에는 접속기록 보관 의무가 있었다(현행 조문 미확인). [추정][^ref-766] 로봇 플랫폼이 이 기준의 개인정보처리시스템에 해당하는지는 처리하는 데이터(영상·사용자 정보)에 따라 달라 미확인이다. [추정][^ref-766]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md)
- 관련 영역: [3. 경제성·조달·사업 모델](../../categories/planning-and-business/economics-procurement-and-business-models.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [39. 운영 성과 측정·개선](../../categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md), [41. 플랫폼 아키텍처·외부 API](../../categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md), [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1038]: Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L, arXiv), ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2, 2022-07, https://arxiv.org/abs/2201.00393, 접근일 2026-09-30
[^ref-1039]: Yu, J., Lee, S., Choi, Y., & Park, K.-J. (arXiv), ros2probe: Non-intrusive, Kernel-selective Observability for Robot Operating System 2 Middleware, 2026-06, https://arxiv.org/abs/2606.10746, 접근일 2026-09-30
[^ref-766]: 개인정보보호위원회 (국가법령정보센터), 개인정보의 안전성 확보조치 기준 (개인정보보호위원회고시 제2023-6호), 2023-09-22, https://www.law.go.kr/admRulLsInfoP.do?chrClsCd=010202&admRulSeq=2100000229672, 접근일 2026-09-30 (원문 미열람)
[^ref-943]: Lee, Y., Kim, S.-E., Kim, J. S. 외 (Digital Health 12), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/, 접근일 2026-09-30
[^ref-1051]: Bruno, L. D. M., Sim, J., & Hagiwara, Y. (arXiv), Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots, 2026-09, https://arxiv.org/abs/2609.29043, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-06 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-06 | 43. 데이터·관측성·배포 의 "왜 중요한가" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 1031건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 278개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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
- cross-schedule-dependency: 스케줄 간 의존 (Cross-schedule Dependency (XD))
- dds-security: DDS 보안 규격 (DDS Security (DDS-Security))
- deadlock: 교착 (Deadlock)
- digital-nameplate: 디지털 명판 (Digital Nameplate (IDTA 02006))
- digital-shadow: 디지털 섀도 (Digital Shadow)
- digital-thread: 디지털 스레드 (Digital Thread)
- digital-twin-composition: 디지털 트윈 결합 (Digital Twin Composition)
- digital-twin: 디지털 트윈 (Digital Twin)
- discrete-event-simulation: 이산 사건 시뮬레이션 (Discrete Event Simulation (DES))
- dispenser-ingestor: 디스펜서·인제스터 (Dispenser / Ingestor)
- distributed-tracing: 분산 추적 (Distributed Tracing)
- drawing-exchange-format: 도면 교환 형식 (Drawing Exchange Format (DXF))
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
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- ontology-evolution: 온톨로지 진화 (Ontology Evolution)
- ontology-pitfall: 온톨로지 피트폴 (Ontology Pitfall)
- ontology-population: 온톨로지 채우기 (Ontology Population)
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
- openapi-specification: OpenAPI 명세 (OpenAPI Specification (OAS))
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
- space-boundary: 공간 경계 (Space Boundary (IfcRelSpaceBoundary))
- space-graph: 공간 그래프 (Space Graph)
- sscc: 물류 단위 일련 코드 (Serial Shipping Container Code (SSCC))
- state-of-charge: 충전 상태 (State of Charge (SOC))
- state-of-health: 배터리 건강 상태 (State of Health (SOH))
- stpa: 시스템 이론적 프로세스 분석 (System-Theoretic Process Analysis (STPA))
- structured-output: 구조화 출력 (Structured Output)
- success-weighted-by-path-length: 경로 길이 가중 성공률 (Success weighted by Path Length (SPL))
- supervisory-control: 감독 제어 (Supervisory Control)
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

### docs/open-questions.md (요약: 대상 영역 [43] 에 걸린 0건 / 전체 209건)

```markdown
없음
```
