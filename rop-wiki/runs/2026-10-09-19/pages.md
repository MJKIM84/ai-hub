# 스토리텔러 산출 2026-10-09-19

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md | draft | 5절 병원 사례 수행 자원·제약 행 채움과 성공률 분모 재확인, 6·7·8·9·10·11절에 2026-10-09 갱신 소절(Mender 상태 스크립트·단계적 배포(벤더 주장)·배포 시점 판단, W3C Trace Context·메시지 흐름 인과 분석, OpenTelemetry 상태·생성형 AI 토큰 지표 재확인, 개인정보 고시 개정 보도·EU AI Act 로그 보관 연계, 열린 질문 부분 근거와 새 질문 3건), 13절 각주 갱신. 2차 수정: 6·7·10·11절 갱신 소절에 2026-09-30 주제 페이지 링크 복원, 7절 기준일 문구 명확화 |
| create | docs/topics/2026/2026-10-09-area43-s6.md | draft | 자동 분리: 43. 데이터·관측성·배포 의 "6. 대표 접근법과 기술" 절(2,358자)을 옮겼다 |
| create | docs/topics/2026/2026-10-09-area43-s7.md | draft | 자동 분리: 43. 데이터·관측성·배포 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,654자)을 옮겼다 |
| create | docs/topics/2026/2026-10-09-area43-s11.md | draft | 자동 분리: 43. 데이터·관측성·배포 의 "11. 열린 질문" 절(1,457자)을 옮겼다 |
| create | docs/topics/2026/2026-10-09-area43-s10.md | draft | 자동 분리: 43. 데이터·관측성·배포 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,426자)을 옮겼다 |
| create | docs/topics/2026/2026-10-09-area43-s8.md | draft | 자동 분리: 43. 데이터·관측성·배포 의 "8. 대표 연구와 자료" 절(1,079자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-10-09 | 43. 데이터·관측성·배포 | 5·6·7·8·9·10·11·13절 차등 갱신: 병원 사례 수행 자원·제약 채움과 성공률 분모 재확인, Mender 상태 스크립트·단계적 배포(벤더 주장)·배포 시점 판단, W3C Trace Context·메시지 흐름 인과 분석, OpenTelemetry 상태·생성형 AI 토큰 지표 재확인, 개인정보 고시 개정 보도·EU AI Act 로그 보관 연계, 열린 질문 부분 근거 6건과 새 질문 3건(2차 수정: 6·7·10·11절 이전 주제 페이지 링크 복원, 7절 기준일 문구 명확화, 표준 목록 이름의 규정 번호 삭제) | run 2026-10-09-19
- 홈 최근 업데이트: 2026-10-09 — 43. 데이터·관측성·배포: 병원 사례 보강, 배포 시점 판단·추적 문맥 잇기·생성형 AI 토큰 지표 재확인, 접속기록 개정 보도와 EU AI Act 로그 보관 연계, 새 열린 질문 3건
- 대분류 최근 업데이트: 2026-10-09 — 43. 데이터·관측성·배포: 5~11절 차등 갱신(구로병원 수행 자원·제약, Mender 상태 스크립트·단계적 배포(벤더 주장), W3C Trace Context·ROS 2 메시지 흐름 분석, OpenTelemetry 상태 재확인, 국내 고시 개정 보도·EU AI Act 제19·26조 연계)
- 세부영역 최근 업데이트: 2026-10-09 — 43. 데이터·관측성·배포: 5절 병원 사례 수행 자원·제약 행 채움, 6·7·8·9·10·11절에 2026-10-09 갱신 소절 추가(2026-09-30 주제 페이지 링크 유지), 13절 각주 갱신(새 출처 10건)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 추적 문맥 | Trace Context (W3C traceparent / tracestate) | 분산 추적에서 요청이 여러 서비스를 거칠 때 같은 추적에 속함을 알리도록 trace-id·parent-id·플래그를 traceparent·tracestate 로 전달하는 W3C 표준 형식이다. | 43, 38, 21 | ref-1373 |
| new | 단계적 배포 | Phased Rollout (Staged Rollout) | 소프트웨어 업데이트를 장치 일부부터 시간차를 두고 여러 단계로 넓혀 배포하고, 문제가 보이면 나머지 단계를 멈추는 배포 방식이다. | 43, 57 | ref-1372 |
| new | 상태 스크립트 | State Script (Mender) | 무선 업데이트 관리자 Mender 가 다운로드·설치·재부팅·확정·롤백 같은 업데이트 상태 전후에 실행하는 스크립트로, 반환값으로 진행·롤백·나중에 재시도를 정한다. | 43, 57 | ref-1371 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-762 | Open Robotics (open-rmf) | rmf-web — packages/api-server/README.md | 오픈소스 문서 | high | https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md |
| ref-766 | 국가법령정보센터(개인정보보호위원회 고시) | 개인정보의 안전성 확보조치 기준 | 정부·연구기관 | medium | https://www.law.go.kr/admRulLsInfoP.do?chrClsCd=010202&admRulSeq=2100000229672 |
| ref-943 | Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 논문 | high | https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/ |
| ref-1036 | OpenTelemetry (CNCF) | Specification Status Summary | 오픈소스 문서 | high | https://opentelemetry.io/docs/specs/status/ |
| ref-1037 | OpenTelemetry (open-telemetry/semantic-conventions-genai) | semantic-conventions-genai/docs/gen-ai/gen-ai-token-metrics.md | 오픈소스 문서 | high | https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md |
| ref-1038 | szobov (GitHub) | ros-opentelemetry — ROS2 x OpenTelemetry README | 오픈소스 문서 | medium | https://github.com/szobov/ros-opentelemetry |
| ref-1367 | 바이라인네트워크 (곽중희) | 개인정보위, 인터넷망 일률 차단제도 개선 “위험기반 보호로 전환” | 기사 | low | https://byline.network/2025/10/31-281/ |
| ref-1313 | European Commission (AI Act Service Desk) | Article 19: Automatically Generated Logs | 정부·연구기관 | high | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-19 |
| ref-1314 | European Commission (AI Act Service Desk) | Article 26: Obligations of Deployers of High-Risk AI Systems | 정부·연구기관 | high | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26 |
| ref-1370 | Hunton Andrews Kurth (Privacy & Cybersecurity Law Blog) | EU Digital Omnibus on AI Enters into Force | 기사 | low | https://www.hunton.com/privacy-and-cybersecurity-law-blog/eu-digital-omnibus-on-ai-enters-into-force |
| ref-1371 | Northern.tech (Mender documentation) | State scripts | 오픈소스 문서 | high | https://docs.mender.io/artifact-creation/state-scripts |
| ref-1372 | Northern.tech (Mender blog, Farshad Tavakoli) | Managing fleets of connected devices with Phased Rollout | 벤더 문서 | low | https://mender.io/blog/managing-fleets-of-connected-devices-with-phased-rollout |
| ref-1373 | W3C | Trace Context | 표준 | high | https://www.w3.org/TR/trace-context/ |
| ref-1374 | OpenTelemetry (CNCF) | Moved: Generative AI semantic conventions | 오픈소스 문서 | high | https://opentelemetry.io/docs/specs/semconv/gen-ai/gen-ai-metrics/ |
| ref-1375 | Bédard, C., Lajoie, P.-Y., Beltrame, G., & Dagenais, M. (Robotics and Autonomous Systems 161, arXiv) | Message Flow Analysis with Complex Causal Links for Distributed ROS 2 Systems | 논문 | medium | https://arxiv.org/abs/2204.10208 |
| ref-1376 | Lumpp, F., Panato, M., Bombieri, N., & Fummi, F. (Università di Verona IRIS) | A Design Flow based on Docker and Kubernetes for ROS-based Robotic Software Applications | 논문 | medium | https://iris.univr.it/handle/11562/1092207 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 2025-10-31 개정으로 접속기록 보관 대상이 개인정보처리시스템에 접속한 모든 자로 넓어졌다면, 로봇·플랫폼 서비스가 쓰는 기계 계정의 개인정보처리시스템 접속도 접속기록 보관·점검 대상에 들어가는가? | 43, 53 | 열림 | — |
| new | — | 로봇 플랫폼 사업자와 현장 운영자가 각각 EU AI Act 의 제공자·배포자가 될 때 실행 기록의 통제권과 6개월 이상 보관 책임을 계약으로 나눈 공개 사례나 지침이 있는가? | 43, 58, 59 | 열림 | — |
| new | — | W3C Trace Context 의 추적 문맥을 ROS 2·DDS 메시지나 VDA 5050 같은 MQTT 기반 로봇–관제 메시지에 싣는 공식 직렬화 규약이 있는가? | 43, 21 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 병원 | 수행 자원 | docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md#5-적용-사례-현장-유형-명시 | 43. 데이터·관측성·배포 |
| 병원 | 제약 | docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md#5-적용-사례-현장-유형-명시 | 43. 데이터·관측성·배포 |
| 병원 | 예외·성과 | docs/categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md#5-적용-사례-현장-유형-명시 | 43. 데이터·관측성·배포 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| W3C Trace Context (traceparent·tracestate, 권고안 2021-11-23) | 표준 | W3C | 43, 38, 21 | ref-1373 | https://www.w3.org/TR/trace-context/ |
| EU AI Act 제19조 자동 생성 로그 (Article 19) | 프레임워크 | European Union (유럽위원회 AI Act Service Desk 게재) | 43, 59, 47 | ref-1313 | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-19 |

## 추가 조사 요청

- 9절·11절(oq-214): 2025-10-31 시행 「개인정보의 안전성 확보조치 기준」 개정 고시 번호, 제8조 현행 문구, 1년 유예 종료일을 국가법령정보센터 또는 개인정보보호위원회 원문으로 확인해야 한다 — 현재 근거가 기사 1건(ref-1367)뿐이다.
- 10절(oq-316): AI 디지털 옴니버스 규정(Regulation (EU) 2026/1744)의 적용일을 EUR-Lex 관보 원문으로 확인해야 한다 — 현재는 로펌 글(ref-1370, 발행일 미확인)과 검색 결과 기준이다.
- 표준 목록·10절: EU AI Act 본 규정의 공식 규정 번호를 브리프 출처로 확인해야 표준 목록 이름에 넣을 수 있다 — 2차 검증 지시로 이번 표준 목록 항목 이름에서 규정 번호를 뺐다.
- 5절(oq-215): 구로병원 실증 논문의 성공률 87.03% 분모와, 검증 메모가 지적한 실시 기간 표기(2025-06-18~29 와 원문 다른 곳의 'four-week' 표현) 불일치를 저자 문의·정정본 등으로 확인해야 한다 — 기간 불일치는 브리프 finding 이 아니라 본문에 넣지 않았다.
- 5절: 제조 공장·상업 시설·가정·실외 현장의 데이터 수집·관측성·배포 적용 사례가 여전히 없다. Lumpp 외(ref-1376)의 적용 환경(실제 공장 여부)·학술지명·DOI 를 본문으로 확인하면 제조 공장 사례 후보가 될 수 있다.
- 6절·8절: Bédard 외(ref-1375) 메시지 흐름 분석의 실행 부담 수치와 다중 호스트·다중 로봇 실험 여부를 본문으로 확인해야 한다(초록만 열람).
- 6절·11절(oq-210): ref-1038(ros-opentelemetry)을 이번 실행에서 다시 열지 못했으므로 추적 문맥 필드 방식의 현재 상태를 재확인해야 한다.
- pipeline 담당: 자동 분리가 절 안의 이전 주제 페이지 링크 줄('자세한 내용은 주제 페이지 …')을 지우는지 확인해야 한다 — 2차 검증 지시에 따라 이번에는 각 갱신 소절 첫머리에 '2026-09-30 까지 정리한 내용은 …에 있다' 링크 문장을 넣었다.

## 이행한 수정 지시

- f14: 승강기 대수 삭제 — 5절 병원 사례 '수행 자원' 행을 'DOGU IROI 배송 로봇 1대와 … 직원 전용 승강기(TK Elevator TK50M)'로 쓰고 승강기의 '1대' 표현을 뺐으며, 로봇 1대(Level 3+로 소개)·단일 로봇 운영은 [사실][^ref-943]로 유지했다.
- f21·ref-1375: 발행일 정정 — 13절 각주와 8절 본문의 발행일을 2023-03 으로 쓰고 reference_updates 의 published 를 "2023-03" 으로 넣었다.
- f10·ref-1370: 발행일 미확인 처리 — 13절 각주의 발행일을 '미확인'으로, reference_updates 의 published 를 null 로 두고, 10절 본문에 '발행일 미확인, 2026-10-09 확인'으로 기준일을 적었다.
- f23: 문구 수정 — 6·8절에서 'Kubernetes(K3s)'를 'Kubernetes'로, '산업용 생산 라인 임무'를 '산업용 애자일 생산 체인(industrial agile production chain) 임무'로 고쳤고, 5절 적용 사례에는 넣지 않고 5절 끝에 적용 사례로 쓰지 않는 이유만 적었다.
- f6·f7: 9절 갱신 소절에서 개정 내용을 '바이라인네트워크 보도(2025-10-31)에 따르면'으로 시작해 [사실][^ref-1367]로 쓰고 개정 고시 번호·제8조 현행 문구·유예 종료일을 '미확인'으로 남겼으며, 기존 '2023-09-22 시행 판 고시 기준(현행 조문 미확인)' 문장은 그대로 두고 f7 은 [추정]으로 썼다.
- f8~f11: 9절에는 '연계 대상:'으로 시작하는 두 문장만 두어 제공자·배포자 로그 보관 의무를 보존 정책의 외부 근거로 썼고, 상세(f8·f9·f10 [사실], f11 [추정])는 10절에서 59. 법·규제·보험·라이선스, 58. 다사업자 책임·계약·데이터, 47. AI·학습·적응과 모델 운영, 37. 관제 화면·실행 기록으로 연결했다.
- f16~f18: 6절에서 Mender 상태 스크립트·단계적 배포 항목을 모두 '연계 대상:'으로 시작했고 f18 은 '[추정] 벤더 주장[^ref-1372]'로 썼으며, ROP 직접 몫은 6절·9절에서 f19 의 배포 시점·순서 판단으로만 한정했다.
- ref-766·ref-1038: 13절 각주의 접근일 뒤에 ' (원문 미열람)'을 붙였고 reference_updates 두 항목에 source_unopened: true 를 넣었다.
- 7절: OpenTelemetry 상태(f1)·생성형 AI 의미 규약(f2~f4) 항목을 '2026-10-09 확인 기준'으로 기준일을 갱신하고 7절 요약 문장에도 기준일 갱신을 밝혔으며, 토큰 지표는 개발 단계이고 gen_ai.client.token.usage 에 대한 이름 변경·폐기 안내가 현재 문서에 없다는 점만 쓰고 그 이름을 '옛 이름'이라 부르거나 폐기 여부를 단정하지 않았다.
- 열린 질문: 11절에서 oq-210·oq-212·oq-213·oq-214·oq-215·oq-316 을 상태 '열림' 그대로 두고 부분 근거(f22·f5·f19·f7·f13·f11)만 [추정]으로 덧붙였으며 open_question_updates 에 해결 항목을 내지 않았고, 5절의 87.03% 는 '저자 보고' 표기를 유지했다.
- f15: 5절 '제약' 행에 기간·경로·승강기 가동률 패턴을 [사실][^ref-943]로 쓰고 '로봇·승강기 속도는 미확인(원문 보고 없음)'을 덧붙였다.
- 2차: 6·7·10·11절 링크 연속성 — 각 절의 2026-10-09 갱신 소절 제목 바로 아래 첫 문장으로 '2026-09-30 까지 정리한 내용(연결·질문)은 [43. 데이터·관측성·배포 — … (2026-09-30)](../../topics/2026/2026-09-30-area43-s6·s7·s10·s11.md)에 있다' 링크 문장을 넣어, 자동 분리 뒤에도 새 주제 페이지 3절에 이전 주제 페이지 링크가 남게 했다.
- 2차: 7절 문구 — 첫 문단을 '2026-09-30 주제 페이지 [43. 데이터·관측성·배포 — 관련 표준·프레임워크·오픈소스 (2026-09-30)](…2026-09-30-area43-s7.md)의 표 행은 2026-09-30 확인 기준이며, 그 가운데 OpenTelemetry 명세 상태와 생성형 AI 의미 규약 행은 이번 실행의 2026-10-09 확인 항목으로 갱신된다'로 고쳐 '아래'를 빼고 어느 주제 페이지의 행인지 밝혔고, 갱신 소절 첫머리에도 같은 뜻을 적었다.
- 2차: standards_updates 의 EU AI Act 항목 — name 을 'EU AI Act 제19조 자동 생성 로그 (Article 19)'로 바꿔 브리프 밖의 규정 번호를 뺐고, 규정 번호 확인은 additional_research_requests 로 넘겼다.
- 분량 초과 자동 분리: 43. 데이터·관측성·배포 본문 11,693자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 4,444자
