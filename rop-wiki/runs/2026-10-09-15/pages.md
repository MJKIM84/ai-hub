# 스토리텔러 산출 2026-10-09-15

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md | draft | 5절 현장 사례를 6건(병원 2·물류창고·실외·가정·기타)으로 늘리고 '찾지 못했다' 문장 교체, 7절에 VDA 5050 동작 상태·오류 수준·logReport, MassRobotics 운용 상태, Open-RMF 배차·개입 기록, ISO 11064, IEEE 7001-2021, 윤리적 블랙박스 초안 행 추가와 rmf-web 행 갱신, 9절에 상태 값 정규화·실외 인증·EU AI Act 로그 보관 경계 추가, 11절 oq-237 해결·부분 근거·새 질문 2건, 13절 각주 갱신 |
| create | docs/topics/2026/2026-10-09-area37-s7.md | draft | 자동 분리: 37. 관제 화면·실행 기록 의 "7. 관련 표준·프레임워크·오픈소스" 절(2,936자)을 옮겼다 |
| create | docs/topics/2026/2026-10-09-area37-s11.md | draft | 자동 분리: 37. 관제 화면·실행 기록 의 "11. 열린 질문" 절(2,787자)을 옮겼다 |
| create | docs/topics/2026/2026-10-09-area37-s3.md | draft | 자동 분리: 37. 관제 화면·실행 기록 의 "3. 왜 중요한가" 절(485자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-10-09 | 37. 관제 화면·실행 기록 | 갱신: 5절 현장 사례 6건(병원 2·물류창고·실외·가정·기타), 7절 VDA 5050·MassRobotics 상태 값 규약·ISO 11064·IEEE 7001-2021·윤리적 블랙박스 초안 추가와 rmf-web 저장 설정 갱신, 9절 상태 값 정규화·실외 인증·EU AI Act 로그 보관 경계, 11절 oq-237 해결·새 질문 2건 | run 2026-10-09-15
- 홈 최근 업데이트: 2026-10-09 — 37. 관제 화면·실행 기록: 공개 상태 값 규약(VDA 5050 동작 상태·오류 수준, MassRobotics 운용 상태)과 현장 사례 6건을 더하고 oq-237 을 해결로 정리
- 대분류 최근 업데이트: 2026-10-09 — 37. 관제 화면·실행 기록: 5·7·9·11절 갱신(병원·물류창고·실외·가정·기타 사례, 상태 값 규약·관제실·투명성 표준, EU AI Act 로그 보관 연계 경계, oq-237 해결)
- 세부영역 최근 업데이트: 2026-10-09 — 37. 관제 화면·실행 기록: 갱신(차등) 5절 사례 6건, 7절 표준 행 7개 추가·rmf-web 행 갱신, 9절 경계 2행·로그 보관 단락, 11절 oq-237 해결·부분 근거·새 질문 2건, 13절 각주 32건(1차 조건부 승인 수정 15건 반영)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 운용 상태 | Operational State (MassRobotics statusReport operationalState) | MassRobotics AMR 상호운용 표준의 상태 보고에서 로봇이 지금 주행·대기·충전·사람 대기·수동 조작 중 어느 상태인지를 아홉 값 가운데 하나로 알리는 필드다. | 37, 20, 21 | ref-253 |
| new | 동작 상태 | Action Status (VDA 5050 actionStatus) | VDA 5050 에서 로봇이 받은 각 동작의 진행을 INITIALIZING·RUNNING·PAUSED·FINISHED·FAILED·RETRIABLE 값으로 플릿 관제에 보고하는 상태 값이다. | 37, 20, 29 | ref-031 |
| new | 자율 시스템 투명성 수준 | Transparency Level (IEEE 7001-2021) | IEEE 7001-2021 이 사용자·인증 담당자·사고 조사자 등 이해관계자 범주마다 최소 수준부터 엄격한 수준까지 다섯 단계로 정한, 객관적으로 평가할 수 있는 투명성 등급이다. | 37, 31, 50 | ref-1338 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json |
| ref-302 | Open Robotics (open-rmf) | rmf-web — README | 오픈소스 문서 | high | https://github.com/open-rmf/rmf-web |
| ref-1095 | Open Robotics (open-rmf/rmf_api_msgs) | rmf_api_msgs schemas — log_entry.json | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/log_entry.json |
| ref-944 | 로봇신문 | 국내 최고의 서비스 로봇 활용 병원 '한림대학교성심병원' | 기사 | low | http://www.irobotnews.com/news/articleView.html?idxno=34601 |
| ref-1007 | 뉴스토마토 (이규하) | 방제·운반·점검 '농업 로봇' 하나로 연결…통합관리기술 가동 | 기사 | low | https://www.newstomato.com/ReadNews.aspx?no=1259970 |
| ref-976 | 정보통신신문 (김연균) | 로봇배송 ‘관제·통신·전력 고도화’ 따라 성장 ‘쑥쑥’ | 기사 | low | https://www.koit.co.kr/news/articleView.html?idxno=123976 |
| ref-980 | 한국로봇산업진흥원 | 실외이동로봇 운행안전인증 | 정부·연구기관 | medium | https://www.kiria.org/portal/cert/portalCertEstiSafe.do |
| ref-1099 | Roldán, J. J., Peña-Tapia, E., Martín-Barrio, A. 외 (Sensors 17(8)) | Multi-Robot Interfaces and Operator Situational Awareness: Study of the Impact of Immersion and Prediction | 논문 | medium | https://pmc.ncbi.nlm.nih.gov/articles/PMC5579739/ |
| ref-253 | MassRobotics (MassRobotics-AMR/AMR_Interop_Standard) | AMR_Interop_Standard.json — MassRobotics AMR Interoperability Standard JSON schema | 표준 | medium | https://github.com/MassRobotics-AMR/AMR_Interop_Standard |
| ref-1338 | IEEE Standards Association | How To Make Autonomous Systems More Transparent and Trustworthy | 표준 | medium | https://standards.ieee.org/beyond-standards/how-to-make-autonomous-systems-more-transparent-and-trustworthy |
| ref-1120 | Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv, ICRES 2022 제출) | An Ethical Black Box for Social Robots: a draft Open Standard | 논문 | medium | https://arxiv.org/abs/2205.06564 |
| ref-863 | European Commission, AI Act Service Desk (Regulation (EU) 2024/1689) | Article 12: Record-keeping | 정부·연구기관 | high | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12 |
| ref-1341 | European Commission, AI Act Service Desk (Regulation (EU) 2024/1689) | Article 19: Automatically generated logs | 정부·연구기관 | high | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-19 |
| ref-1342 | European Commission, AI Act Service Desk (Regulation (EU) 2024/1689) | Article 26: Obligations of deployers of high-risk AI systems | 정부·연구기관 | high | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26 |
| ref-1343 | LG CNS (LG 미디어 보도자료) | ‘로봇 통합운영 플랫폼’ 개발 | 벤더 문서 | low | https://lg.co.kr/media/release/26480 |
| ref-1344 | 코메디닷컴 | [메디피플 365] 로봇 73대가 병원 곳곳서 환자·의료진 척척 돕죠 | 기사 | low | https://kormedi.com/1682189/ |
| ref-1345 | 바이라인네트워크 (이진호) | 뉴빌리티, 실외이동 로봇 운행안전 인증 획득 | 기사 | low | https://byline.network/2024/01/240131_00004/ |
| ref-762 | Open Robotics (open-rmf/rmf-web) | rmf-web packages/api-server — README | 오픈소스 문서 | high | https://github.com/open-rmf/rmf-web/blob/main/packages/api-server/README.md |
| ref-1347 | Patel, J., Ramaswamy, T., Li, Z., & Pinciroli, C. (arXiv) | Transparency in Multi-Human Multi-Robot Interaction | 논문 | medium | https://arxiv.org/abs/2101.10495 |
| ref-1348 | Rohrer, T., Farhang Ghahfarokhi, A., Behery, M., Lakemeyer, G., & van der Aalst, W. M. P. (arXiv) | Predictive Object-Centric Process Monitoring | 논문 | medium | https://arxiv.org/abs/2207.10017 |
| ref-1349 | ISO (ANSI Webstore 미리보기) | ISO 11064-1:2000 Ergonomic design of control centres — Part 1: Principles for the design of control centres (preview) | 표준 | medium | https://webstore.ansi.org/preview-pages/ISO/preview_ISO+11064-1-2000.pdf |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| update | oq-237 | 여러 제조사 로봇의 작업 상태와 실행 로그를 한 화면·한 기록 형식으로 모을 때 공통 작업 상태 값과 로그 수준을 정한 표준이나 공개 규약이 Open-RMF 작업 상태 스키마 말고도 있는가? | 37, 21 | 해결 | docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md#11-열린-질문 |
| new | — | VDA 5050 동작 상태, MassRobotics 운용 상태, Open-RMF 작업 상태 값 사이의 대응표를 공개한 표준 기구나 프로젝트가 있는가, 없다면 플릿 관제 기록에서 어떤 기준으로 대응시키는가? | 37, 21 | 열림 | — |
| new | — | 국내 실외이동로봇 운행안전인증의 관제 장치 항목은 관제 화면 표시와 운행 기록 저장·보관을 어디까지 요구하는가? 평가 항목 수가 바이라인네트워크 보도(16개 항목)와 한국로봇산업진흥원 안내(관제장치를 포함한 8개 심사 항목)에서 다르게 표현되므로 현행 기준도 함께 확인해야 한다. | 37, 59, 66 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 병원 | 수행 자원 | docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md#5-적용-사례-현장-유형-명시 | 37. 관제 화면·실행 기록 |
| 병원 | 예외·성과 | docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md#5-적용-사례-현장-유형-명시 | 37. 관제 화면·실행 기록 |
| 물류창고 | 수행 자원 | docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md#5-적용-사례-현장-유형-명시 | 37. 관제 화면·실행 기록 |
| 실외 | 제약 | docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md#5-적용-사례-현장-유형-명시 | 37. 관제 화면·실행 기록 |
| 가정 | 시작 조건 | docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md#5-적용-사례-현장-유형-명시 | 37. 관제 화면·실행 기록 |
| 가정 | 작업 대상 | docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md#5-적용-사례-현장-유형-명시 | 37. 관제 화면·실행 기록 |
| 기타 | 수행 자원 | docs/categories/field-operations-and-monitoring/control-screen-and-execution-records.md#5-적용-사례-현장-유형-명시 | 37. 관제 화면·실행 기록 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| ISO 11064 관제 센터 인간공학 설계(Ergonomic design of control centres) 계열 | 표준 | ISO | 37, 38 | ref-1349 | https://webstore.ansi.org/preview-pages/ISO/preview_ISO+11064-1-2000.pdf |
| IEEE 7001-2021 자율 시스템 투명성 표준 | 표준 | IEEE Standards Association | 37, 31, 50 | ref-1338 | https://standards.ieee.org/beyond-standards/how-to-make-autonomous-systems-more-transparent-and-trustworthy |

## 추가 조사 요청

- 5절 적용 사례: 제조 공장·상업 시설에서 여러 로봇을 하나의 관제 화면·실행 기록으로 운영한 사례가 이번에도 없다. 두 현장 유형의 사례(한국 사례 우선)를 조사해 달라.
- 5절 실외 사례·새 열린 질문: 실외이동로봇 운행안전인증의 관제 장치 항목이 화면 표시·운행 기록 저장·보관을 어디까지 요구하는지, 평가 항목 수(기사 16개, 진흥원 안내 심사 항목 8개) 가운데 현행 기준이 무엇인지 인증 고시 원문으로 확인이 필요하다.
- 11절 oq-252: 윤리적 블랙박스 초안 부록(기록 항목·보관 시간 창·보안 요건)을 PDF 원문으로 읽어 플랫폼 수준 기록 항목과 비교할 근거가 필요하다.
- 11절 oq-239: 마약류 관리에 관한 법률 시행규칙 등 국내 법령 원문으로 병원 특수 물품 로봇 배송 이력의 보관 기간·무결성 요건을 확인해야 한다.
- 7절·11절 oq-240: IEEE 7001-2021 표준 본문과 ISO 11064 각 부의 적용 범위·현행 개정판을 확인해야 화면·기록 요건 포함 여부를 판단할 수 있다.
- 프런트매터 related_areas 는 10절(주제 페이지로 분리됨)과 맞추려고 바꾸지 않았다. 이번에 9·11절에서 연결한 21. 상호운용 표준·적합성, 50. 안전 표준·인증·사고 조사, 59. 법·규제·보험·라이선스, 66. 실외를 다음 갱신에서 10절 연결에 더할지 검토가 필요하다.
- 참고문헌 중복 확인(퍼블리셔 담당): 브리프의 ref-1120 는 기존 ref-1120 과, ref-762 은 기존 ref-762 와 같은 URL 이다. 브리프 id 를 그대로 썼으므로 퍼블리셔의 같은 URL 병합이 적용되는지 확인을 요청한다.

## 이행한 수정 지시

- f4 '누가 개입했는지' 과장 수정 — 7절 'Open-RMF 작업 상태 스키마의 배차 상태·개입 기록' 행을 '작업 요청자(booking.requester)와, 일시정지·재개·취소·강제 종료·단계 건너뛰기 요청마다의 요청 시각·라벨(예: dashboard)로 어떤 창구에서 개입했는지'로 쓰고 개입 요청에는 요청자 필드가 없다고 밝혔다.
- f6 '실행 기록이 남지 않지만' 수정 — 7절 rmf-web 행을 '기본 설정은 메모리 안의 SQLite(비영속 내부 데이터베이스)를 쓰며 db_url 로 영속 저장 가능'으로 고치고 ref-762 각주를 ref-302 와 함께 달았으며 두 문서가 같은 저장소라 독립 출처가 아님을 적었다.
- f19 항목 수 차이 — 5절 실외 사례 표와 서술에서 '16개 항목'은 바이라인네트워크 보도 기준, 한국로봇산업진흥원 안내는 관제장치를 포함한 8개 심사 항목을 나열한다고 둘 다 제시했고, 이 차이를 둘째 새 열린 질문(11절과 open_question_updates)에 덧붙였으며 조합 인증·관제장치 평가는 [사실] 유지했다.
- f19 범위 경계 — 5절 실외 사례 서술과 9절 '업종별 조건(실외)' 행에 인증 판단은 인증 기관·운영자 쪽 연계 대상이고 ROP 에는 실외 현장의 운행 제약으로만 반영된다고 [추정]으로 썼다.
- f10 기준일 — 7절 ISO 11064 행에 'ISO 11064-1:2000 미리보기 머리말 기준(확인일 2026-10-09), 각 부의 이후 개정 여부와 적용 범위는 미확인'을 적었다.
- f8 공동 후원 표현 — 7절 IEEE 7001-2021 행을 'IEEE 로봇·자동화 학회가 공동 후원 학회 가운데 하나다'로 고치고 표준 본문이 아니라 IEEE SA 소개 글(2022-05-11) 기준임을 밝혔다(11절 oq-240 항목에도 소개 글 기준 표기).
- f2 logReport 경계 — 7절 표 아래 문장과 9절 '로봇 자체 지능·제어(상태 값·로봇 로그)' 행에서 logReport 로 생성되는 로그 자체는 로봇 쪽 기록(연계 대상)이고 ROP 는 생성 요청과 로그 이름(동작 상태) 수신만 맡는다고 썼다.
- f13·f14·f15 EU AI Act — 9절 표 아래 단락에서 조문 내용은 [사실]로, 고위험 AI 해당 여부와 보관 의무 해석은 59. 법·규제·보험·라이선스 쪽 연계 대상으로 짧게 다루고 ROP 몫을 보관 기간 설정과 로그 통제 주체 표시 기능으로 한정해 [추정]으로 썼으며, 제19조·제26조는 '같은 규정'이라고 밝히고 교차 확인으로 표시하지 않았다.
- f17 단일 보도 — 5절 둘째 병원 사례 표와 서술에 '3만 1607건'이 코메디닷컴 단일 보도 기준(2024-04-20)임을 밝혔다.
- f18 벤더 주장 — 5절 물류창고 사례의 표와 서술에 [추정] 뒤 '벤더 주장'을 병기하고 기술검증 착수 발표뿐이며 운영 결과는 확인되지 않았다고 썼으며, 물류 흐름 단계는 서술하지 않았다.
- f24 객체 유형·예측 대상 — 11절 oq-131 항목에서 객체 유형을 '로봇·주문·부품(제품)'으로, 예측 대상을 '이후 사건과 그 시각(남은 사건 순서 포함)'으로 썼다.
- f1·f2 VDA 5050 기준 — 7절 VDA 5050 세 행에 '기준 3.0.0(main), 발행일 미확인, 확인일 2026-10-09'를 적고 기존 각주 ref-031 을 재사용했다(13절 접근일 2026-10-09로 갱신).
- 각주 원문 미열람 표시 — 13절에서 ref-944·ref-1007·ref-976·ref-980·ref-1099·ref-253 의 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었다.
- 11절 열린 질문 정리 — oq-237 을 해결(근거 f1·f3·f4, 대응표 문제는 새 질문으로 이음)로 바꾸고, oq-238·oq-239 는 열림 유지, oq-131·oq-240·oq-252·oq-316 은 해결로 바꾸지 않고 부분 근거(f24·f25, f8·f9·f10, f11·f12, f13·f14·f15)만 덧붙였으며, 기존 '(새 질문, 상태: 열림)' 네 줄을 oq-237·oq-238·oq-239·oq-240 으로 표기했다.
- 용어집 혼동 방지 — '운용 상태'(operational-state) 항목 설명에 기존 용어 '운용 모드'(Operating Mode, VDA 5050 operatingMode)와 다른 개념임을 한 문장으로 밝혔다.
- 분량 초과 자동 분리: 37. 관제 화면·실행 기록 본문 11,771자 > 기준 4,000자 → 3개 절을 주제 페이지로 옮김, 남은 본문 5,946자
