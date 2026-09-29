# 스토리텔러 산출 2026-09-29-01

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md | draft | 3~11절 신규 작성(seed → draft), 출처 15건, 열린 질문 3건, 현장 유형 사례 3건(병원·제조 공장·실외). 2차 재검증 수정 지시 이행: 10절 14. 도면·BIM에서 지도 만들기 항목을 사실 문장과 추정 문장으로 나눔(태그 상향 해소) |
| create | docs/topics/2026/2026-09-29-area08-s6.md | draft | 자동 분리: 8. 채팅으로 맵 작성 의 "6. 대표 접근법과 기술" 절(1,767자)을 옮겼다(2차 재검증에서 변경 없음) |
| create | docs/topics/2026/2026-09-29-area08-s4.md | draft | 자동 분리: 8. 채팅으로 맵 작성 의 "4. 핵심 개념과 용어" 절(1,091자)을 옮겼다(2차 재검증에서 변경 없음) |
| create | docs/topics/2026/2026-09-29-area08-s8.md | draft | 자동 분리: 8. 채팅으로 맵 작성 의 "8. 대표 연구와 자료" 절(979자)을 옮겼다(2차 재검증에서 변경 없음) |
| create | docs/topics/2026/2026-09-29-area08-s3.md | draft | 자동 분리: 8. 채팅으로 맵 작성 의 "3. 왜 중요한가" 절(742자)을 옮겼다. 2차 재검증 수정: 3절의 태그 없는 판단 문장 2건에 [추정]·[의견] 태그와 각주를 붙이고 sources·출처에 ref-815·ref-816·ref-819 추가 |
| create | docs/topics/2026/2026-09-29-area08-s7.md | draft | 자동 분리: 8. 채팅으로 맵 작성 의 "7. 관련 표준·프레임워크·오픈소스" 절(690자)을 옮겼다(2차 재검증에서 변경 없음) |
| create | docs/topics/2026/2026-09-29-area08-s10.md | draft | 자동 분리: 8. 채팅으로 맵 작성 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(618자)을 옮겼다. 2차 재검증 수정: 14. 도면·BIM에서 지도 만들기 항목을 사실·추정 문장으로 나누고 15. 지도·공간·위치 모델 항목 태그를 [추정]으로 바꿈 |
| create | docs/topics/2026/2026-09-29-area08-s11.md | draft | 자동 분리: 8. 채팅으로 맵 작성 의 "11. 열린 질문" 절(589자)을 옮겼다(2차 재검증에서 변경 없음) |

## 변경 이력·색인

- 변경 이력: 2026-09-29 | 8. 채팅으로 맵 작성 | 3~11절 신규 작성(seed → draft), 출처 15건, 현장 유형 사례 3건, 열린 질문 3건, 2차 재검증 수정 지시 3건 반영(10절 태그 상향 2건 되돌림, 3절 판단 문장 태그) | run 2026-09-29-01
- 홈 최근 업데이트: 2026-09-29 — 8. 채팅으로 맵 작성: 3~11절 신규 작성. 언어→위상·의미 지도 연구, Open-RMF 빌딩 맵·VDMA LIF 형식, 축척·통과 조건은 확인 질문으로 받는 원칙 정리
- 대분류 최근 업데이트: 2026-09-29 — 8. 채팅으로 맵 작성: 3~11절 신규 작성(초안). 병원(시뮬레이션 데모)·제조 공장(벤더 주장)·실외 사례, 열린 질문 3건
- 세부영역 최근 업데이트: 2026-09-29 — 8. 채팅으로 맵 작성: 실행 2026-09-29-01 에서 3~11절 신규 작성. 출처 15건(ref-815~ref-163), 신뢰도 medium

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 트래픽 에디터 | Traffic Editor (Open-RMF) | 2D 평면도 이미지 위에 층·벽·꼭짓점·플릿별 차선·문·승강기를 그려 제조사 중립 빌딩 맵(.building.yaml)을 만드는 Open-RMF 의 GUI 편집 도구이다. | 8, 15, 22 | ref-079 |
| new | 언어 유도 평면도 생성 | Language-guided Floor Plan Generation | 방 종류·위치·크기·관계를 적은 자연어 설명에서 공간·관계 제약을 만족하는 평면도를 생성하는 과제이다. | 8, 14, 45 | ref-817, ref-823 |
| new | 명확화 질문 | Clarification Question (Follow-up Clarification) | 요청이 모호할 때 시스템이 아는 정보를 바탕으로 사용자에게 되묻는 질문으로, 확정할 수 없는 값을 추정으로 채우지 않고 사람에게 확인받는 대화 장치이다. | 8, 13 | ref-826 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-815 | Deguchi, H., Shibata, K., & Taguchi, S. (Toyota Central R&D Labs) | Language to Map: Topological map generation from natural language path instructions | 논문 | medium | https://arxiv.org/abs/2403.10008 |
| ref-816 | Rajendran Kathirvel, R. S., Chavis, Z. A., Guy, S. J., & Desingh, K. | SENT Map -- Semantically Enhanced Topological Maps with Foundation Models | 논문 | medium | https://arxiv.org/abs/2511.03165 |
| ref-817 | Leng, S., Zhou, Y., Dupty, M. H., Lee, W. S., Joyce, S. C., & Lu, W. | Tell2Design: A Dataset for Language-Guided Floor Plan Generation | 논문 | medium | https://arxiv.org/abs/2311.15941 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/traffic-editor.html |
| ref-819 | Walter, M., Hemachandra, S., Homberg, B., Tellex, S., & Teller, S. (Robotics: Science and Systems IX) | Learning Semantic Maps from Natural Language Descriptions | 논문 | medium | https://www.roboticsproceedings.org/rss09/p04.html |
| ref-820 | 김영재, 김세윤, 김홍준 (대한공간정보학회지) | 공공 맵 데이터를 이용한 자율주행 이동 로봇의 전역 경로 계획용 지도 생성 방법에 관한 연구 | 논문 | medium | https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11079654 |
| ref-046 | VDMA (Intralogistics-2X-LIF GitHub) | Layout-Interchange-Format — README (Repository for the Layout Interchange Format (LIF) developed by the VDMA) | 표준 | high | https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format |
| ref-822 | Rodionov, F., Eldesokey, A., Birsak, M., Femiani, J., Ghanem, B., & Wonka, P. | FloorplanQA: A Benchmark for Spatial Reasoning in LLMs using Structured Representations | 논문 | medium | https://arxiv.org/abs/2507.07644 |
| ref-823 | Qin, S., Weber, R. E., & Lu, X. | Tokenization Allows Multimodal Large Language Models to Understand, Generate and Edit Architectural Floor Plans | 논문 | medium | https://arxiv.org/abs/2603.11640 |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — README (Demonstrations of Open-RMF) | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_demos |
| ref-825 | Yang, Y., Sun, F.-Y., Weihs, L. 외 (Allen Institute for AI 등) | Holodeck: Language Guided Generation of 3D Embodied AI Environments | 논문 | medium | https://arxiv.org/abs/2312.09067 |
| ref-826 | Doğan, F. I., Torre, I., & Leite, I. (ACM/IEEE HRI 2022) | Asking Follow-Up Clarifications to Resolve Ambiguities in Human-Robot Conversation | 논문 | medium | https://dl.acm.org/doi/10.5555/3523760.3523822 |
| ref-827 | 모빌리오(Mobilio) | [최초 공개] 산업용 순찰 로봇, 도면 연동과 센서 관제를 웹 화면 하나로 끝내는 방법 | 벤더 문서 | low | https://www.mobilio.io/ko/%eb%aa%a8%eb%b9%8c%eb%a6%ac%ec%98%a4-%ed%86%b5%ed%95%a9-%eb%8c%80%ec%8b%9c%eb%b3%b4%eb%93%9c-%ec%86%94%eb%a3%a8%ec%85%98/ |
| ref-083 | Zhang, J., Wu, S., Ma, X., & Schwertfeger, S. | Generation of Indoor Open Street Maps for Robot Navigation from CAD Files | 논문 | medium | https://arxiv.org/abs/2507.00552 |
| ref-163 | 노주형, 강규리, 김연찬, 심현철 (로봇학회 논문지) | 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템 | 논문 | medium | https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 대화로 만든 층·구역·통로·문·승강기·충전 위치를 Open-RMF 빌딩 맵과 VDMA LIF 처럼 서로 다른 플릿 지도 형식으로 함께 내보낼 수 있는 공통 중간 표현이나 공식 변환 규칙이 있는가? | 8, 15, 21 | 열림 | — |
| new | — | 언어 모델이 대화로 만든 지도 요소의 기하 정확도와 확인 질문 횟수·구성 완료 시간을 어떤 지표와 시험 시나리오로 평가할 것인가, 로봇 지도 작성 대화에 특화된 벤치마크나 국내 사례가 있는가? | 8, 13 | 열림 | — |
| new | — | 채팅 맵 작성이 받는 도면·라이다 지도 입력의 좌표계·축척 정합 결과를 누가 확인·승인하고 어느 시점에 지도가 확정된 것으로 보는지, 이 역할을 ROP 와 로봇 제조사·통합자 가운데 누가 맡는가? | 8, 14, 55 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 병원 | 시작 조건 | docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시 | 8. 채팅으로 맵 작성 |
| 병원 | 작업 대상 | docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시 | 8. 채팅으로 맵 작성 |
| 병원 | 수행 자원 | docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시 | 8. 채팅으로 맵 작성 |
| 병원 | 제약 | docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시 | 8. 채팅으로 맵 작성 |
| 병원 | 완료·인계 | docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시 | 8. 채팅으로 맵 작성 |
| 제조 공장 | 시작 조건 | docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시 | 8. 채팅으로 맵 작성 |
| 제조 공장 | 작업 대상 | docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시 | 8. 채팅으로 맵 작성 |
| 제조 공장 | 수행 자원 | docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시 | 8. 채팅으로 맵 작성 |
| 제조 공장 | 제약 | docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시 | 8. 채팅으로 맵 작성 |
| 제조 공장 | 완료·인계 | docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시 | 8. 채팅으로 맵 작성 |
| 실외 | 시작 조건 | docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시 | 8. 채팅으로 맵 작성 |
| 실외 | 작업 대상 | docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시 | 8. 채팅으로 맵 작성 |
| 실외 | 수행 자원 | docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시 | 8. 채팅으로 맵 작성 |
| 실외 | 제약 | docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시 | 8. 채팅으로 맵 작성 |
| 실외 | 완료·인계 | docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시 | 8. 채팅으로 맵 작성 |
| 실외 | 예외·성과 | docs/categories/chat-based-configuration-and-operation/chat-map-authoring.md#5-적용-사례-현장-유형-명시 | 8. 채팅으로 맵 작성 |

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- 5절·6절: 대화만으로 로봇용 빌딩 맵·레이아웃을 채운 실제 현장 배치 사례(연구 프로토타입·시뮬레이션 데모 외)가 없어 병원 사례를 설명용으로 썼다. 실제 도입 사례가 필요하다.
- 4절·7절: VDMA LIF 의 JSON 구조 세부(층·지도 id 필드, 스테이션 속성)가 미확인이라 빌딩 맵과의 요소 대응을 쓰지 못했다. 공식 가이드라인 PDF 원문 확인이 필요하다.
- 4절·6절: 명확화 질문 연구(ref-826)의 효과 결론이 원문 미열람으로 추정에 머물렀다. ACM 원문 또는 저자 공개본(DiVA 등)으로 재확인이 필요하다.
- 6절: 지도 작성 대화에 특화된 확인 질문·모호성 해소 연구와 언어 모델 기반 지도 작성의 국내 연구가 없어 열린 질문으로만 두었다.
- 7절: Nav2 keepout 필터 문서(금지 구역 지도 요소)와 rmf_traffic_editor 저장소 README 는 이번 조사에서 열지 못해 표에 넣지 못했다.
- 5절: 병원 사례의 예외·성과 항목과 제조 공장 사례의 예외·성과 항목을 채울 처리량·시간·비용 근거가 없어 미확인으로 두었다.
- 7절: VDA 5050 의 노드·에지 개념이 LIF 노드·에지의 기원인지는 브리프에 근거가 없어 2차 지시대로 삭제했다. VDA 5050 원문(노드·에지 정의)과 LIF 가이드라인의 관계를 확인하면 7절 표와 10절 21. 상호운용 표준·적합성 연결에 반영할 수 있다.
- 10절: CAD 도면 변환 결과(Zhang 외)가 실제로 채팅 맵 작성의 입력으로 쓰인 사례가 브리프에 없어 '입력이 된다'는 역할 판단을 추정으로만 두었다. 도면 변환 → 대화 편집 → 플릿 지도 형식으로 이어진 실제 파이프라인 사례가 있으면 사실로 올릴 수 있다.

## 이행한 수정 지시

- f20 강등 — 4절 명확화 질문 항목과 6절 확인 질문 단락을 [추정][^ref-826]으로 쓰고, '63명 사용자 연구'까지만 확인된 것으로 두고 효과 결론(과제가 쉽게 느껴짐·로봇 역량 평가 상승)은 원문을 열지 못해 확인하지 못했다고 서술했다.
- ref-826 원문 미열람 표기 — 13절 각주 정의의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 ref-826 항목에 source_unopened: true 를 넣었다.
- f21 정합 — 6절 '공간 제약 검증과 확인 질문' 단락에서 추정을 유지하되 '명확화 질문의 효과 결론은 원문 미확인'임을 근거 문장에 밝혔다.
- f19 용어·표기 — 4절과 5절 제조 공장 사례에서 용어집 '지도 정합(Map Alignment)'을 링크해 쓰고 벤더 표기는 '맵 정합'으로 따옴표 병기했으며, 모든 문장에 [추정] 벤더 주장[^ref-827]을 유지하고 현장 유형을 제조 공장으로 명시했다.
- f13 시뮬레이션 명시 — 5절 병원 사례 첫 문장에 Open-RMF Clinic 시뮬레이션 데모 월드 기반 설명용 사례이며 실제 병원 배치 사례가 아님을 명시했다. Hotel 월드는 별도 사례로 쓰지 않고 7절 rmf_demos 행에서 데모 예시로만 언급했다.
- f18 연계 대상 — 5절 끝에 '기타 현장의 연계 대상 사례' 단락으로 짧게만 다루고(여섯 항목 표·매트릭스 칸 없음), 9절에서도 로봇 자체 지능·제어 몫으로만 언급해 ROP 직접 범위처럼 쓰지 않았다.
- f5·f6·f7 참고 표기 — 6절 소제목을 '언어 모델의 평면도 생성·편집(건축 설계용, 방법 참고)'으로 두고 첫 문장에서 로봇 지도 작성이 아닌 건축 설계용임을 밝혔으며, 8절에서도 '건축 설계용'을 적고 f6 의 기하 타당성·제어 가능성 우위는 '저자 보고값'으로 표기했다.
- f8·f16 개정 버전 병기 — FloorplanQA 는 3·6·8절에서 '2025년 7월 초판, v4 2026-05-25 개정, ICML 2026 채택'으로, Zhang 외는 3·8절에서 'v3 2026-03-31 개정'으로 기준일에 병기했다.
- f14 LIF 표기 — 4절 정의와 7절 표의 유형 칸에서 표준이 아니라 '법적 구속력 없는 VDMA 가이드라인'으로 표기하고 유형은 프레임워크로 두었다.
- f16·f24 교차 연결 — 10절에서 14. 도면·BIM에서 지도 만들기와 45. 문서·도면·장면 이해 양쪽에 연결하고, 6절에는 '연계 대상: 도면 해석·SLAM 엔진' 소제목으로 도면 해석 엔진을 연계 대상으로만 두었다.
- f11 직접 인용 1회 — 브리프의 Traffic Editor 직접 인용 구절은 본문에 옮기지 않고 f10·f11 모두 요약·재서술했으므로 ref-079 직접 인용은 0회다(출처당 1회 상한 안).
- 용어집 — '레이아웃 교환 형식(LIF)'·'위상 지도'·'지도 정합'은 기존 용어(layout-interchange-format, topological-map, map-alignment)에 링크만 하고 신규 등록하지 않았으며, '명확화 질문' 항목의 description 에 명시적 확인·암시적 확인·슬롯 채우기와의 관계를 한 문장 더했다.
- ref-079·ref-104 id 재사용 — 참고문헌 전체 목록이 입력에 없어 대조하지 못했으므로 브리프 id 그대로 넣고 reference_updates 의 두 항목 summary 에 '같은 URL 이 있으면 기존 id 로 합친다'를 적어 퍼블리셔 병합에 맡겼다.
- 2차: 6절 '연계 대상: 도면 해석·SLAM 엔진' 단락 — 문장 중간의 '[사실][^ref-083]과'·'[사실][^ref-163]은' 표기를 없애고 한 문장으로 다시 써서 끝에 '…이 위키의 추정이다. [추정][^ref-083][^ref-163]' 을 두었다(f22 처분과 일치).
- 2차: 7절 표 VDA 5050 행 — '노드·에지 개념의 근원' 구절을 지우고 'LIF 정의에 영향을 준 무인운반차 인터페이스. [사실]' 까지만 남겼으며, 삭제한 관계는 additional_research_requests 에 조사 요청으로 적었다.
- 2차: 10절 22. 설비·건물 시스템 연동 항목과 16. 장소 의미·지도 관리 항목 — 문장 끝 [사실] 을 [추정] 으로 바꿨다(각주 [^ref-104], [^ref-816][^ref-819] 유지).
- 2차: 6절 평면도 생성·편집 단락 끝 문장 — '이 위키의 의견으로, 제약을 먼저 뽑고 최적화로 배치하는 구조는 지도 요소 배치에도 참고할 만하다. [의견][^ref-825]' 로 고쳐 태그와 각주를 붙였다.
- 2차: 8절 첫 항목(Deguchi 외) — 첫 문장 끝에 [사실][^ref-815] 을 두고 '언어만으로 위상 지도가 가능함을 보인 직접 근거다.' 를 그 뒤에 이었다. 자동 분리로 첫 문장만 남아도 태그·각주가 남는다.
- 2차: 5절 제조 공장 사례 — 표 앞 첫 문장에 '모빌리오가 "맵 정합"이라 부르는 [지도 정합(Map Alignment)](../../glossary/map-alignment.md) 기능' 으로 용어집 링크와 벤더 표기 따옴표 병기를 넣고 [추정] 벤더 주장[^ref-827] 을 붙였다. 1차 f19 항목이 이제 4절·5절 모두에서 이행된다.
- 2차: SLAM·IMU·PGM 풀이 — 세부영역 페이지에 남는 5절에서 처음 나오는 자리(제조 공장 표 시작 조건 칸의 PGM·BIM, 기타 현장 단락의 IMU·SLAM)에 영문 전체 이름과 풀이를 적고, 9절 표의 '라이다 SLAM' 과 6절 연계 대상 단락에도 풀이를 병기했다. 9절 본문의 PGM 은 'PGM 형식 지도' 로 적어 5절 풀이를 따른다.
- 2차(재검증): 10절 14. 도면·BIM에서 지도 만들기 항목 — 세부영역 페이지 10절 첫 항목과 분리 페이지 2026-09-29-area08-s10.md 의 1절 첫 항목·3절 첫 항목 세 곳 모두 'CAD 파일에서 로봇 지도를 자동 생성하는 연구가 있다. [사실][^ref-083] 그 결과가 이 영역의 입력이 된다는 것은 이 위키의 추정이다. [추정][^ref-083]' 으로 사실 문장과 추정 문장으로 나눴다(f22·f24 처분과 일치).
- 2차(재검증): 10절 15. 지도·공간·위치 모델 항목 — 분리 페이지 2026-09-29-area08-s10.md 3절 두 번째 항목을 '…요소가 대화 결과를 담는 모델이라는 것이 이 위키의 추정이다. [추정][^ref-079][^ref-046]' 으로 바꿨다(f15·f23 처분과 일치).
- 2차(재검증): 3절 판단 문장 — 분리 페이지 2026-09-29-area08-s3.md 3절에서 (a) '2절의 핵심 질문에 대한 현재 답은 …에 가깝다' 를 '…에 가깝다는 것이 이 위키의 추정이다. [추정][^ref-815][^ref-816][^ref-819]' 로, (b) '말로도 그림으로도 확정할 수 없는 값을 … 핵심 설계 문제다' 를 '이 위키의 의견으로, … 핵심 설계 문제다. [의견][^ref-079]' 로 고쳤다. 새 각주 ref-815·ref-816·ref-819 를 그 페이지 8절 출처와 프런트매터 sources 에 더했다. 세부영역 페이지 3절 요약과 분리 페이지 1절 요약에는 이 두 문장이 없어 손대지 않았다.
- 분량 초과 자동 분리: 8. 채팅으로 맵 작성 본문 9,590자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 4,577자
