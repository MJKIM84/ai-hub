# 리서치 브리프 2026-09-30-06

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-06 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 43. 데이터·관측성·배포 |
| 대분류 | K. 플랫폼 아키텍처·인프라 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 관측성, OpenTelemetry, MCAP, FinOps·FOCUS, A/B 분할 업데이트 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 병원(운영 로그 기반 실패 분석)·물류창고(배포 전 시뮬레이션 검증) 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 기록 형식, 추적·지표·로그 수집, 컨테이너 오케스트레이션, 이미지 기반 무선 업데이트와 롤백, 비용 계측 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — rosbag2·MCAP, ros2_tracing, OpenTelemetry, Mender, FOCUS 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 0건
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 플랫폼 자체의 상태·데이터·배포·비용을 어떻게 관리할 것인가? [분류원문]
2. 로봇·플랫폼의 로그·이벤트·텔레메트리를 기록·저장하는 형식과 도구(rosbag2·MCAP, 플랫폼 기록 DB)는 무엇이며, 보존 기간을 정하는 국내 규제 근거는 무엇인가? (섹션 4·6·7 겨냥, 한국 자료 우선)
3. 플랫폼 관측성을 구현하는 표준·오픈소스(OpenTelemetry, ros2_tracing, 커널 기반 관찰)는 무엇이며 관찰 자체의 성능 부담은 얼마로 보고되는가? (섹션 6·7·8 겨냥)
4. 현장 서버·로봇·클라우드에 플랫폼 소프트웨어를 배포하고 되돌리는 방법(컨테이너 오케스트레이션, 이미지 기반 무선 업데이트와 롤백, 배포 전 시뮬레이션 검증)은 무엇이며 어떤 결과가 보고되는가? (섹션 6·7·8 겨냥)
5. 클라우드와 언어 모델 호출 비용을 측정·할당·관리하는 기준(FinOps 주기, FOCUS 청구 데이터 명세, OpenTelemetry 생성형 AI 토큰 지표)은 무엇인가? (섹션 4·6·7 겨냥)
6. 병원·물류창고 등 현장에서 운영 데이터를 수집해 실패 원인을 분석하거나 소프트웨어 변경을 배포 전에 검증한 사례는 무엇인가? (섹션 5 겨냥)
7. 데이터·관측성·배포에서 ROP가 직접 맡을 것과 로봇 제조사·클라우드 사업자·법규에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Bédard·Lütkebohle·Dagenais 의 ros2_tracing(IEEE RA-L 7(3), 2022-07)은 저부하 추적기 LTTng 를 써서 ROS 2 의 실행 정보를 수집하는 계측·추적 도구 모음으로, ROS 2 추적 데이터를 운영체제 추적과 결합할 수 있고, ROS 2 계측을 모두 켰을 때 종단 간 메시지 지연 증가가 평균 0.0033 ms 라고 보고했다. | ref-1038 | 아니오 | medium | 2022-07 | — | — |
| f2 | [사실] | ros2_tracing 저자들은 미들웨어 수준의 표준 데이터 기록만으로는 내부 계산과 성능 병목에 관한 정보가 충분하지 않다고 보고, 이를 실행 추적 도구가 필요한 이유로 든다. | ref-1038 | 아니오 | medium | 2022-07 | — | — |
| f3 | [사실] | Yu·Lee·Choi·Park 의 ros2probe(arXiv 2606.10746, 2026-06)는 ROS 2 도메인에 구독자로 참여하는 관찰 도구가 탐색(discovery) 부담과 역직렬화 비용을 더해 관찰 대상을 교란한다고 보고, 탐색 패킷으로 통신 그래프를 복원한 뒤 사용자가 지정한 토픽만 커널 안에서 걸러 관찰하는 방식으로 관찰자 CPU 사용을 최대 7배·메모리를 최대 28배 줄이고, 포화 조건에서 도메인 참여형 도구가 38.5% 메시지를 잃을 때 메시지 손실 0을 보고했다. | ref-1039 | 아니오 | medium | 2026-06 | — | — |
| f4 | [사실] | ROS 2 Iron Irwini(2023-05-23 출시)부터 rosbag2 가 새 백 파일을 기록하는 기본 형식을 sqlite3 에서 MCAP 로 바꿨고, 같은 판에서 서비스 호출로 원격에서 기록을 일시 정지·재개·분할하는 기능이 더해졌다. | ref-1040, ref-1041 | 예 | high | 2023-05-23 | — | — |
| f5 | [추정] | Foxglove 는 MCAP 이 SQLite3 의 '복원력' 모드 수준의 데이터 안전성과 '쓰기 최적화' 모드 수준의 쓰기 처리량을 함께 제공하고, zstd·lz4 압축을 고를 수 있으며, 메시지 정의를 파일 안에 담아 외부 스키마 없이 다른 도구가 읽을 수 있다고 주장한다. | ref-1041 | 아니오 | low | 2022-12-22 | — | 벤더 주장 |
| f6 | [사실] | OpenTelemetry 명세 상태 요약에 따르면 추적(tracing)은 API·SDK·프로토콜이 모두 안정(stable)이고 장기 지원 대상이며, 로그는 브리지 API·SDK·프로토콜이 안정, 지표(metrics)는 API·프로토콜이 안정이나 SDK 는 혼합 상태, 프로파일(profiles)은 프로토콜이 개발(development) 단계다. | ref-1042 | 아니오 | medium | 2026-09-30 | — | — |
| f7 | [사실] | OpenTelemetry 생성형 AI 의미 규약 저장소의 토큰 지표 문서는 입력·출력·캐시 읽기·캐시 쓰기 입력·추론 출력 토큰 카운터(gen_ai.client.inference.usage.*)와 호출별 입력·출력 토큰 히스토그램(gen_ai.client.inference.operation.*)을 정의하고, 작업 이름·제공자 이름을 필수 속성으로 두며, 모든 지표가 개발(Development) 단계다. | ref-1043 | 아니오 | medium | 2026-09-30 | — | — |
| f8 | [사실] | 오픈소스 ros-opentelemetry 는 송신 측이 추적 문맥을 ROS 2 메시지의 사용자 정의 필드에 넣고 수신 측이 꺼내 이어 붙이는 방식으로 토픽·서비스·액션을 가로지르는 분산 추적을 C++·Python 노드에 제공하고, 로그를 추적 구간(span)에 연결하는 로거를 둔다. | ref-1044 | 아니오 | medium | 2026-09-30 | — | — |
| f9 | [사실] | Zhang·Yu·Westerlund(Sensors, 2025-08)는 TurtleBot4 에 얹은 Jetson Nano 5대를 작업 노드로, 노트북 1대를 마스터로 둔 K3s 클러스터에서 컨테이너화한 ROS 2 노드로 다중 로봇 UWB 상대 위치 추정을 운영했고, 오차 보정용 LSTM 파드 5개를 모두 종료시킨 경우에도 Kubernetes 가 파드를 자동 재시작해 위치 오차(APE)가 약 0.12~0.14 m 로 장애 없는 경우와 비슷하게 유지됐다고 보고했다. | ref-1045 | 아니오 | medium | 2025-08-14 | 예외·성과 | — |
| f10 | [사실] | 연계 대상: 오픈소스 Mender 는 임베디드 리눅스·사물인터넷 장치용 클라이언트–서버 방식 무선(OTA) 업데이트 관리자로, 이중 A/B 루트 파일시스템 분할에 이미지 단위로 원자적 배포를 해 업데이트 중 전원이 끊겨도 동작하던 상태로 되돌릴 수 있게 하며, 루트 파일시스템·애플리케이션·파일·컨테이너 업데이트를 지원하고 Apache 2.0 라이선스로 공개된다. | ref-1046 | 아니오 | medium | 2026-09-30 | — | — |
| f11 | [사실] | 개인정보보호위원회 「개인정보의 안전성 확보조치 기준」(고시 제2023-6호, 2023-09-22 시행) 제8조는 개인정보처리자가 개인정보취급자의 개인정보처리시스템 접속기록을 1년 이상(5만 명 이상의 정보주체 개인정보를 처리하는 시스템 등은 2년 이상) 보관·관리하고, 월 1회 이상 점검하며, 위조·변조·도난·분실되지 않도록 안전하게 보관하게 한다. | ref-766 | 아니오 | medium | 2023-09-22 | 제약 | — |
| f12 | [사실] | FinOps 재단의 FinOps 프레임워크는 기술 비용·사용량·효율 데이터를 수집·배분·보고·예측하는 정보(Inform), 사용량 최적화와 요금 최적화를 찾는 최적화(Optimize), 엔지니어링·재무·사업 팀이 함께 개선을 실행하는 운영(Operate)의 세 단계를 반복하는 방식으로 설명하며, 대상 기술 범주에 공용 클라우드·SaaS 와 함께 AI 서비스를 든다. | ref-1048 | 아니오 | medium | 2026-09-30 | — | — |
| f13 | [사실] | FinOps 재단의 청구 데이터 명세 FOCUS 1.2(2025-05-29 비준)는 SaaS·PaaS 청구 데이터를 클라우드 비용과 같은 스키마에 넣고, 크레딧·토큰 같은 가상 통화와 다중 통화 정규화(PricingCurrency 등), 청구서 연결용 InvoiceId 열을 더했으며, AWS·Microsoft·Google Cloud·Oracle Cloud·Alibaba Cloud·Databricks·Grafana 가 지원을 밝혔다. | ref-1049 | 아니오 | medium | 2025-05-29 | — | — |
| f14 | [사실] | Bruno·Sim·Hagiwara(arXiv 2609.29043, 2026-09)는 클라우드 언어 모델 API 는 로봇이 긴 작업을 반복할수록 요청당 비용이 쌓이고 네트워크 지연이 실시간 반응을 떨어뜨린다고 보고, 두 단계 연쇄(chaining) 계획으로 추론당 프롬프트 길이를 약 45% 줄여 로컬 모델(Qwen2.5-14B·Cogito-14B)의 계획 성공을 최대 37%p 높였으며 클라우드 모델(Claude Sonnet 4.6)과 함께 비교했다. | ref-1051 | 아니오 | medium | 2026-09 | 예외·성과 | — |
| f15 | [사실] | 고려대학교 구로병원의 자율 약품 배송 로봇 실증(Lee 외, Digital Health, 2026-03)에서 배송 임무는 응급실 직원이 웹 애플리케이션으로 요청하면 시작됐다. | ref-943 | 아니오 | medium | 2026-03-31 | 병원 / 시작 조건 | — |
| f16 | [사실] | 같은 병원 실증은 로봇이 사람 개입 없이 전체 경로를 마치고 약품을 넘겨 간호사가 받는 것을 배송 성공으로 정의했다. | ref-943 | 아니오 | medium | 2026-03-31 | 병원 / 완료·인계 | — |
| f17 | [사실] | 같은 병원 실증은 승강기 호출·탑승·문 동작·하차 시각을 1 Hz 로 남긴 로봇 시스템 로그, 승강기 상태·문·위치·로봇 명령을 담은 승강기 통신 로그, 관찰자가 적은 수기 기록지(탑승객·화물·결과)를 함께 모아 분석했다. | ref-943 | 아니오 | medium | 2026-03-31 | 병원 / 작업 대상 | — |
| f18 | [사실] | 같은 병원 실증에서 전체 배송 성공률은 87.03%, 승강기 가동률 59% 미만일 때 95.52% 였고, 실패 14건은 승강기 막힘 8건·복도 주행 4건·통신 오류 2건이었으며, 승강기 가동률이 높을수록 실패가 많았다. | ref-943 | 아니오 | medium | 2026-03-31 | 병원 / 예외·성과 | — |
| f19 | [추정] | Ocado 는 물류창고 로봇 교통 관리·오케스트레이션 알고리즘과 운영 변경을 실제 창고에 적용하기 전에 시뮬레이션·디지털 트윈에서 시험하고, 초당 10회 로봇 통신 같은 실제 운영 데이터로 모델을 다듬으며, 12개월 동안 창고 운영 270년 분량을 시뮬레이션했다고 밝힌다. | ref-1052 | 아니오 | low | 2025-06-04 | 물류창고 / 예외·성과 | 벤더 주장 |
| f20 | [사실] | Open-RMF 의 웹 API 서버(rmf-web api-server)는 기록용 데이터베이스로 tortoise-orm 을 통해 PostgreSQL·SQLite·MySQL·MariaDB 를 지원하며 기본값은 메모리 SQLite 다. | ref-762 | 아니오 | medium | 2026-09-30 | — | — |
| f21 | [추정] | 확인한 자료를 종합하면 핵심 질문(플랫폼 자체의 상태·데이터·배포·비용 관리)에 대해, 데이터는 자기 기술형 기록 형식(MCAP)과 플랫폼 기록 DB 로 남기고(f4·f20), 상태는 OpenTelemetry 의 추적·지표·로그로 플랫폼 서비스를 관찰하면서 로봇 내부 실행은 저부하 추적·커널 필터로 교란 없이 보며(f1·f3·f6·f8), 배포는 컨테이너 오케스트레이션의 자동 재시작과 이미지 기반 A/B 롤백, 배포 전 시뮬레이션 검증을 조합하고(f9·f10·f19), 비용은 표준 청구 데이터(FOCUS)와 토큰 지표를 FinOps 주기로 관리하는 조합이 공개 자료의 공통 형태로 보인다(f7·f12·f13). | ref-1040, ref-762, ref-1038, ref-1039, ref-1042, ref-1044, ref-1045, ref-1046, ref-1052, ref-1043, ref-1048, ref-1049 | 아니오 | low | 2026-09-30 | — | — |
| f22 | [추정] | 확인한 자료를 종합하면 이 영역이 중요한 까닭은, 미들웨어 기록만으로는 내부 병목을 알 수 없고(f2) 관찰 도구 자체가 시스템을 교란할 수 있으며(f3), 병원 실증처럼 실패 원인이 로봇·승강기 로그를 함께 모아야 드러나고(f17·f18), 클라우드 언어 모델 호출 비용이 반복 작업에서 누적되며(f14), 개인정보를 다루는 시스템은 접속기록 보존·점검 의무를 지기 때문이다(f11). | ref-1038, ref-1039, ref-943, ref-1051, ref-766 | 아니오 | low | 2026-09-30 | — | — |
| f23 | [추정] | 확인한 자료를 종합하면 43. 데이터·관측성·배포에서 ROP 가 직접 맡을 범위는 플랫폼 서비스의 로그·지표·추적 수집과 보존 정책(f6·f11), 작업 단위 추적 문맥 전파와 로봇 기록(MCAP 등)의 수집·색인 인터페이스(f4·f8·f17), 플랫폼 구성 요소의 배포·롤백·버전 기록과 배포 전 검증(f9·f19), 클라우드·언어 모델 호출 비용의 계측·배분(f7·f13)이다. | ref-1042, ref-766, ref-1040, ref-1044, ref-943, ref-1045, ref-1052, ref-1043, ref-1049 | 아니오 | low | 2026-09-30 | — | — |
| f24 | [추정] | 연계 대상: 분류 원문 19장 기준으로 로봇 운영체제·펌웨어의 무선 업데이트와 로봇 내부 ROS 2 실행 추적(f1·f10)은 로봇 제조사에, 클라우드 청구 데이터 생성(f13)은 클라우드 사업자에, 승강기 통신 로그(f17)는 설비 제어 쪽에 속하므로, 이종 제조사를 잇는 ROP 는 이들이 내는 기록·업데이트 상태·청구 데이터를 받아 모으는 인터페이스를 맡을 것으로 보인다. | ref-1038, ref-1046, ref-1049, ref-943 | 아니오 | low | 2026-09-30 | — | — |
| f25 | [추정] | 이 영역은 실행 기록을 보여 주는 37. 관제 화면·실행 기록(f17·f20), 로그로 원인을 찾는 38. 모니터링·이상 탐지·원인 분석(f2·f18), 성과 지표의 39. 운영 성과 측정·개선(f18), 컨테이너·DDS 통신의 42. 분산 시스템·통신·컴퓨팅 구조(f9), 기록 DB 를 두는 41. 플랫폼 아키텍처·외부 API(f20), 업데이트·버전의 57. 자산·소프트웨어 수명주기 관리(f10), 배포 전 검증의 54. 시험·형식 검증·벤치마크와 34. 시뮬레이션·예측용 디지털 트윈(f19), 접속기록의 53. 개인정보·영상 데이터와 52. 통신 보호·위협 관리·감사(f11), 비용의 3. 경제성·조달·사업 모델(f12·f13), 언어 모델 비용의 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영·13. 대화형 기능의 신뢰·기반(f7·f14), 승강기 로그의 22. 설비·건물 시스템 연동(f17), 적용 현장인 63. 병원·의료(f15~f18)·61. 물류창고(f19)와 이어진다. | ref-943, ref-762, ref-1038, ref-1045, ref-1046, ref-1052, ref-766, ref-1048, ref-1049, ref-1043, ref-1051 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

- **f1**: 초록 기준: LTTng 기반 ROS 2 계측, OS 추적과 결합, 모든 ROS 2 계측 활성화 시 종단 간 메시지 지연 오버헤드 평균 0.0033 ms. 실험 조건은 본문 미확인.
- **f2**: "standard, middleware-based data recording does not provide sufficient information on internal computation and performance bottlenecks"
- **f3**: 초록 기준: 탐색 그래프 유지 부담 0.5% 이내, 관찰자 CPU 최대 7배·메모리 최대 28배 감소, 패킷 손실 탐지 재현율 1.0, 포화 시 손실 0 대 도메인 참여 도구 38.5%. 프리프린트.
- **f4**: ROS 2 공식 문서 Iron 릴리스 노트: "This release switches to using `mcap` as the default file format for writing new bags." Foxglove 블로그(2022-12-22)도 Iron 부터 MCAP 기본값을 알림.
- **f5**: 벤더 주장: SQLite3 resilient 모드의 안전성과 write optimized 모드의 처리량을 함께 제공, zstd·lz4 압축 선택, 메시지 정의 내장으로 Foxglove·PlotJuggler 연동.
- **f6**: "The tracing specification is now completely stable, and covered by long term support." 로그·지표 데이터 모델은 OTLP 의 일부로 공개. (발행일 미확인, 확인일 기준)
- **f7**: 토큰 지표 7종(카운터 5, 히스토그램 2), 단위 {token}, 필수 속성 gen_ai.operation.name·gen_ai.provider.name(카운터는 gen_ai.token.modality 추가), 상태 Development. (발행일 미확인, 확인일 기준)
- **f8**: README: inject_trace_context()/extract_trace_context() 로 메시지 간 추적 문맥 전파, C++(ament_cmake)·Python(ament_python) 패키지와 문맥 전파용 메시지 정의, traced logger. 라이선스 표기 미확인. (발행일 미확인, 확인일 기준)
- **f9**: K3s 기반 오케스트레이션, 장애 시나리오 F5(LSTM 파드 5개 종료)에서도 정확도 유지, LSTM 보정 없을 때 APE 0.66 m 이상. 복구 시간은 보고하지 않음. 실험실 환경.
- **f10**: README: "atomic image-based deployments using a dual A/B rootfs partition layout", 전원 상실 시에도 롤백, Update Modules 로 다른 구성 요소 확장. (발행일 미확인, 확인일 기준)
- **f11**: 제8조(접속기록의 보관 및 점검): 1년 이상 보관, 5만 명 이상 처리 시스템 등은 2년 이상, 월 1회 이상 점검, 위변조 방지. 5만 명 조건 문구는 검색 요약으로 보완.
- **f12**: Inform: 데이터 수집·배분·보고·예측·단위 경제성 / Optimize: "both usage optimization and rate optimization" / Operate: 책임 문화와 지속 개선. (발행일 미확인, 확인일 기준)
- **f13**: 새 열 7개(InvoiceId, BillingAccountType, SubAccountType, PricingCurrency 외 3), 가상 통화로 토큰 기반 지출 분석 가능. (발행일 미확인, 확인일 기준)
- **f14**: "Cloud APIs incur per-request cost that accumulates when a robot repeats long-horizon tasks" RoboCup@Home GPSR 명령 100개 평가, Toyota HSR 실로봇 10개 중 6개 성공. 비용 금액은 보고하지 않음.
- **f15**: 비응급 임무 122건(2025-06-18~29, 평일·주말), 응급실 직원의 웹 앱 요청으로 임무 시작.
- **f16**: 성공 정의: 로봇이 전체 경로를 완료하고 사람 개입 없이 약품을 인계, 간호사가 수령.
- **f17**: 자료원 3종: 로봇 시스템 로그(1 Hz 타임스탬프), 승강기 통신 로그, 훈련된 관찰자의 사례 기록지.
- **f18**: "A higher EOR was strongly associated with more delivery failures." 대부분 실패는 탑승객·화물의 물리적 가로막음.
- **f19**: 벤더 주장: "We can identify bottlenecks, predict congestion, evaluate new layouts or algorithms, and stress-test for peak demand."
- **f20**: api-server README: 기록 DB tortoise-orm, 기본 in-memory SQLite. (재인용: 2026-09-30-05)
- **f21**: 종합 추정. 이종 제조사 로봇의 기록과 플랫폼 추적을 한 작업 단위로 잇는 공개 사례는 찾지 못함.
- **f22**: 종합 추정. 로봇 플랫폼이 개인정보처리시스템에 해당하는지는 처리 데이터(영상·사용자 정보)에 따라 달라 미확인.
- **f23**: 종합 추정. 분류 원문 19장 경계와 1절 리스트업 네 항목 기준.
- **f24**: 종합 추정. 자사 로봇까지 만드는 경우 경계가 이동할 수 있음(분류 원문 19장).
- **f25**: 종합 추정. 연결 근거는 괄호 안 finding.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1038 | Bédard, C., Lütkebohle, I., & Dagenais, M. (IEEE RA-L, arXiv) | ros2_tracing: Multipurpose Low-Overhead Framework for Real-Time Tracing of ROS 2 | 2022-07 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2201.00393 | 아니오 |
| ref-1039 | Yu, J., Lee, S., Choi, Y., & Park, K.-J. (arXiv) | ros2probe: Non-intrusive, Kernel-selective Observability for Robot Operating System 2 Middleware | 2026-06 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2606.10746 | 아니오 |
| ref-1040 | Open Robotics (ROS 2 Documentation) | Iron Irwini (iron) | 2023-05-23 | 오픈소스 문서 | high | 2026-09-30 | https://docs.ros.org/en/rolling/Releases/Release-Iron-Irwini.html | 아니오 |
| ref-1041 | Foxglove | MCAP as the ROS 2 Default Bag Format | 2022-12-22 | 벤더 문서 | medium | 2026-09-30 | https://foxglove.dev/blog/mcap-as-the-ros2-default-bag-format | 아니오 |
| ref-1042 | OpenTelemetry (CNCF) | Specification Status Summary | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://opentelemetry.io/docs/specs/status/ | 아니오 |
| ref-1043 | OpenTelemetry (open-telemetry/semantic-conventions-genai) | semantic-conventions-genai/docs/gen-ai/gen-ai-token-metrics.md | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md | 아니오 |
| ref-1044 | szobov (GitHub) | ros-opentelemetry — ROS2 x OpenTelemetry README | 미확인 | 오픈소스 문서 | medium | 2026-09-30 | https://github.com/szobov/ros-opentelemetry | 아니오 |
| ref-1045 | Zhang, J., Yu, X., & Westerlund, T. (Sensors 25(16):5067) | Enhancing the Resilience of ROS 2-Based Multi-Robot Systems with Kubernetes: A Case Study on UWB-Based Relative Positioning | 2025-08-14 | 논문 | high | 2026-09-30 | https://pmc.ncbi.nlm.nih.gov/articles/PMC12390455/ | 아니오 |
| ref-1046 | Northern.tech (mendersoftware) | mender — README | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/mendersoftware/mender | 아니오 |
| ref-766 | 개인정보보호위원회 (국가법령정보센터) | 개인정보의 안전성 확보조치 기준 (개인정보보호위원회고시 제2023-6호) | 2023-09-22 | 정부·연구기관 | high | 2026-09-30 | https://www.law.go.kr/admRulLsInfoP.do?chrClsCd=010202&admRulSeq=2100000229672 | 아니오 |
| ref-1048 | FinOps Foundation | FinOps Phases | 미확인 | 업계 보고서 | medium | 2026-09-30 | https://www.finops.org/framework/phases/ | 아니오 |
| ref-1049 | FinOps Foundation | Introducing FOCUS 1.2: SaaS/PaaS Support, Invoice Reconciliation, and more | 미확인 | 표준 | medium | 2026-09-30 | https://www.finops.org/insights/focus-1-2-available/ | 아니오 |
| ref-943 | Lee, Y., Kim, S.-E., Kim, J. S. 외 (Digital Health 12) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 2026-03-31 | 논문 | high | 2026-09-30 | https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/ | 아니오 |
| ref-1051 | Bruno, L. D. M., Sim, J., & Hagiwara, Y. (arXiv) | Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots | 2026-09 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2609.29043 | 아니오 |
| ref-1052 | Ocado Group | Ocado's digital twins and simulations: driving efficiencies | 2025-06-04 | 벤더 문서 | medium | 2026-09-30 | https://www.ocadogroup.com/newsroom/stories/digital-twins-and-simulations | 아니오 |
| ref-762 | Open Robotics (open-rmf) | rmf-web/packages/api-server/README.md | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md | 아니오 |

### 출처 요약

- **ref-1038**: LTTng 기반 ROS 2 계측·추적 도구 모음. 종단 간 메시지 지연 증가 평균 0.0033 ms 보고. 초록 페이지만 열람.
- **ref-1039**: ROS 2 도메인에 참여하지 않고 커널 필터로 선택한 토픽만 관찰하는 프레임워크. 관찰자 CPU·메모리 감소와 포화 시 무손실 보고. 초록 기준.
- **ref-1040**: ROS 2 Iron 릴리스 노트. rosbag2 기본 기록 형식을 mcap 으로 바꾸고 원격 기록 제어 서비스 등을 더함.
- **ref-1041**: Iron 부터 MCAP 이 ROS 2 기본 백 형식이 된다는 발표와 SQLite3 대비 장점(벤더 주장).
- **ref-1042**: OpenTelemetry 신호(추적·지표·로그·배기지·프로파일)별 API·SDK·프로토콜 안정성 상태.
- **ref-1043**: 생성형 AI 추론 토큰 지표(입력·출력·캐시·추론 토큰 카운터와 호출별 히스토그램)의 의미 규약. 개발 단계.
- **ref-1044**: ROS 2 C++·Python 노드에 OpenTelemetry 분산 추적·로그 연결을 넣는 개인 관리 오픈소스 라이브러리.
- **ref-1045**: K3s 로 컨테이너화한 ROS 2 노드를 다중 로봇에서 운영하고 파드 장애 시 자동 재시작으로 위치 정확도를 유지함을 보인 연구. PMC 본문 열람.
- **ref-1046**: 임베디드 리눅스용 오픈소스 OTA 업데이트 관리자. A/B 루트 파일시스템 분할과 자동 롤백.
- **ref-766**: 개인정보처리자의 안전성 확보조치 고시. 제8조에서 접속기록 보관 기간·점검 주기·위변조 방지를 정함.
- **ref-1048**: FinOps 프레임워크의 정보·최적화·운영 세 단계 설명.
- **ref-1049**: 청구 데이터 명세 FOCUS 1.2 의 새 기능(SaaS·PaaS, 가상 통화, InvoiceId, 다중 통화)과 지원 사업자 발표. 명세 본문이 아닌 발표 글. 제목은 검색 결과 기준.
- **ref-943**: 고려대학교 구로병원 약품 배송 로봇 122건 실증. 로봇·승강기 로그와 수기 기록으로 승강기 가동률과 실패의 관계 분석. PMC 본문 열람.
- **ref-1051**: 두 단계 LLM 연쇄 계획으로 프롬프트 길이를 줄이고 로컬·클라우드 모델을 비교한 서비스 로봇 연구. 클라우드 API 비용·지연을 동기로 듦.
- **ref-1052**: Ocado 가 창고 로봇 알고리즘·운영 변경을 시뮬레이션·디지털 트윈에서 먼저 시험한다는 회사 글(벤더 주장). 제목 뒷부분은 검색 결과 기준.
- **ref-762**: Open-RMF 웹 API 서버의 REST 엔드포인트·OpenAPI 문서·기록 DB·인증 구조 설명.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f22(왜 중요한가), f21(핵심 질문 답, 추정) / 섹션 4: 관측성·실행 추적 f1·f2, MCAP f4·f5(벤더 주장 병기), OpenTelemetry f6, 토큰 지표 f7, A/B 분할 업데이트 f10, FinOps·FOCUS f12·f13 / 섹션 5: 병원 — f15(시작 조건)·f16(완료·인계)·f17(작업 대상: 로봇·승강기 로그 정보)·f18(예외·성과), 물류창고 — f19(배포 전 시뮬레이션 검증, 벤더 주장 병기). 제조 공장·상업 시설·가정·실외 사례는 찾지 못함을 명시 / 섹션 6: 기록 f4·f20, 관찰 f1·f3·f6·f8, 배포 f9·f10·f19, 비용 f7·f12·f13·f14 / 섹션 7: rosbag2·MCAP f4·f5, ros2_tracing f1, ros2probe f3, OpenTelemetry f6·f7, ros-opentelemetry f8, K3s f9, Mender f10, FOCUS f13, 개인정보 고시 f11 / 섹션 8: f1·f3·f9·f14·f15~f18 / 섹션 9: f23(직접 범위), f24(연계 대상) / 섹션 10: f25 — 3, 13, 22, 34, 37, 38, 39, 41, 42, 44, 47, 52, 53, 54, 57, 61, 63 / 섹션 11: open_questions_new 4건. 다음 실행 후보: 38. 모니터링·이상 탐지·원인 분석 페이지에 f1·f3·f17·f18 반영, 57. 자산·소프트웨어 수명주기 관리 페이지에 f10 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 관측성 | Observability | 시스템이 내보내는 로그·지표·추적 같은 원격 측정 데이터만으로 내부 상태와 오류·성능 원인을 알아낼 수 있는 정도, 또는 그것을 가능하게 하는 수집·분석 체계다. |
| 오픈텔레메트리 | OpenTelemetry (OTel) | 추적·지표·로그를 생성·수집·전송하는 API·SDK·전송 프로토콜(OTLP)과 의미 규약을 정한 벤더 중립 오픈소스 관측성 표준 프로젝트다. |
| MCAP | MCAP | 여러 채널의 시간 표시 메시지를 스키마와 함께 담는 자기 기술형 로깅 파일 형식으로, ROS 2 Iron 부터 rosbag2 의 기본 기록 형식이다. |
| 핀옵스 | FinOps | 클라우드·SaaS·AI 서비스 비용과 사용량 데이터를 정보·최적화·운영 단계로 반복 관리하며 엔지니어링·재무·사업 팀이 비용 책임을 나누는 운영 방식이다. |

## 열린 질문

새로 생긴 질문:

- 서로 다른 제조사 로봇의 기록(MCAP·제조사 로그)과 플랫폼 서비스의 분산 추적을 하나의 작업 식별자로 이어 원인 분석에 쓴 공개 사례나 표준이 있는가? | 관련 영역: 43. 데이터·관측성·배포, 38. 모니터링·이상 탐지·원인 분석 | 근거: f8 | 종류: 일반
- 로봇 플랫폼이 수집하는 텔레메트리·주행 기록·영상의 보존 기간을 정한 국내 기준이나 운영 사례가 개인정보 접속기록 규정 밖에도 있는가? | 관련 영역: 43. 데이터·관측성·배포, 53. 개인정보·영상 데이터 | 근거: f11 | 종류: 일반
- OpenTelemetry 생성형 AI 토큰 지표가 개발 단계에서 이름이 바뀌고 있는데, 언어 모델 호출 비용 계측을 안정 판이 나오기 전까지 어떤 기준으로 고정할 것인가? | 관련 영역: 43. 데이터·관측성·배포, 13. 대화형 기능의 신뢰·기반 | 근거: f7 | 종류: 일반
- 운행 중인 로봇 작업을 끊지 않고 현장 서버·로봇에 플랫폼 소프트웨어를 순차 배포하고 되돌리는 시점·기준을 공개한 로봇 관제 제품이나 연구가 있는가? | 관련 영역: 43. 데이터·관측성·배포, 57. 자산·소프트웨어 수명주기 관리 | 근거: f10 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 16 · 교차 확인: 1
- 예산 사용량: 검색 22회 · 신규 출처 15건
- 미확인 항목:
    - f1·f3·f14 는 논문 초록(또는 HTML 일부) 기준이며 본문 실험 조건 미확인
    - f7: 검색 결과 요약의 다른 문서들은 gen_ai.client.token.usage 히스토그램을 설명하지만, 열어 본 현재 저장소는 gen_ai.client.inference.usage.* 로 정의함. 이름 변경 시점과 이전 이름의 폐기 여부 미확인
    - f11 의 '5만 명 이상' 조건 문구는 검색 요약으로 보완했고 법령 페이지 요약에서는 1년/2년 구분만 확인
    - f13 FOCUS 1.2 명세 본문(PDF) 미열람, 발표 글만 열람
    - f8 ros-opentelemetry 라이선스·유지 주체 미확인(개인 관리 저장소)
    - ref-1049·ref-1052 제목 일부는 검색 결과 제목 기준
    - Zampetti 외 CPS CI/CD 인터뷰 연구(ACM TOSEM 2023)는 ACM 403·PDF 본문 추출 실패로 넣지 않음
    - Docker·Kubernetes 기반 ROS 설계 흐름 논문(ACM 10.1145/3594539)은 403 으로 넣지 않음
    - 실외이동로봇 운행안전인증에서 관제·소프트웨어 원격 업데이트 시 변경 인증 필요 여부는 KIRIA 안내 페이지에 없어 확인하지 못함
    - 제조 공장·상업 시설·가정·실외 현장의 데이터·배포 사례는 찾지 못함
- 범위 경계 위반 의심:
    - f1·f3: ROS 2 내부 실행 추적은 로봇 소프트웨어 쪽 기법이므로 관찰 방법 근거로만 쓰고, 이종 제조사 로봇 내부 추적은 f24 에서 연계 대상으로 구분함
    - f10: 로봇 운영체제·펌웨어 OTA 는 로봇 제조사 영역이므로 claim 을 '연계 대상: '으로 시작함
    - f14: 언어 모델 계획 자체는 44. 로봇 기반 모델·언어 모델 계획의 내용이며 이 영역에는 비용·지연 근거로만 제안함
    - f17: 승강기 통신 로그 생성은 설비 제어 쪽이며 ROP 는 수집·결합만 맡는 것으로 f24 에서 구분함
    - f19: 시뮬레이션·디지털 트윈 자체는 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)의 내용이며 이 영역에는 배포 전 검증 근거로만 제안함. 18. 실시간 세계 상태·데이터 일관성과 섞지 않음
- 한계: web_fetch_available: true · fetch_mode full. 검색 22회/30, 신규 출처 15건/15(출처 상한 도달). 신규 출처 id: 실행 컨텍스트의 예약 구간은 ref-1032 부터이나, 입력의 같은 날 이전 브리프(2026-09-30-04·2026-09-30-05)가 ref-1032~ref-1037 을 다른 출처에 이미 썼으므로 충돌을 피하려고 예약 구간 안의 ref-1038~ref-1052 를 순서대로 썼다. 재사용 1건(ref-762, 이전 브리프 2026-09-30-05 재인용, 이번에 다시 열지 않음; 값은 그 브리프의 출처 표를 따랐고 참고문헌 목록 전체는 입력에 없음). 원문 열람: 신규 15건 모두 열었다(webfetch 11건, github_raw 4건). 논문 가운데 Zhang 외(ref-1045)·Lee 외(ref-943)는 PMC 본문을, 나머지는 초록 페이지를 열었다. 교차 확인 1건(f4: ROS 2 공식 릴리스 노트와 Foxglove 블로그). 벤더 문서만 근거로 한 f5·f19 는 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈다. 분류 원문 핵심 질문(플랫폼 자체의 상태·데이터·배포·비용 관리)에는 f21 로 답했고 결론은 '자기 기술형 기록 형식과 기록 DB + OpenTelemetry 기반 플랫폼 관찰과 저부하 로봇 내부 추적 + 컨테이너 자동 재시작·A/B 롤백·배포 전 시뮬레이션 검증 + 표준 청구 데이터와 토큰 지표를 쓰는 FinOps 주기'라는 추정이다. 현장 유형 사례는 병원(f15~f18, 국내 고려대학교 구로병원)·물류창고(f19, 벤더 주장)뿐이다. 국내 자료는 개인정보보호위원회 고시(ref-766)와 국내 병원 실증 논문(ref-943) 두 건이다. L. AI·학습 기술 관련 f7·f14 는 교차 규칙에 따라 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영과 함께 연결하도록 제안했다. 용어집에 이미 있는 분산 추적·백 파일·무선 업데이트·서비스 수준 협약·감사 추적·모델 레지스트리는 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 없음.
