# 출처·원문 열람·실패 기록

접근일은 모두 **2026-10-13 (KST)**. 기준 위키/시뮬레이터는 **9c4de242d0f08ac8804707b7cc7787fbd261fef4**. 검색 결과 요약만으로 기술·법령 주장을 확정하지 않았다. 본문에서 사용한 S01~S23은 아래 적은 원문/해당 절을 실제 열었다. **S21은 저자 초록만** 읽었으며 논문 전문 열람으로 세지 않는다. 모든 원문 전편을 읽었다는 뜻도 아니다.

## 1. 공개 출처

|ID·제목|URL|판/식별|발행일|읽은 절·위치|짧은 원문 구절|적용 한계|
|---|---|---|---|---|---|---|
|S01 SoftBank/Hyundai 인수 조건 합의|[원문](https://group.softbank/en/news/press/20201211_0)|보도자료|2020-12-11|첫 본문·거래 종결 조건|“agreed on main terms”|벤더 단독 연혁 발표. 완료일 아님|
|S02 Hyundai 인수 완료 발표|[원문](https://www.prnewswire.com/news-releases/hyundai-motor-group-completes-acquisition-of-boston-dynamics-from-softbank-301316206.html)|당사자 보도자료 배포본|2021-06-21|본문 첫 문단|“announced the completion”|언론 독립 검증으로 세지 않음|
|S03 Boston Dynamics 전동 Atlas|[원문](https://bostondynamics.com/blog/electric-new-era-for-atlas/)|블로그·HTML JSON-LD|2024-04-17|첫 문단; datePublished 2024-04-17T12:50:13+00:00|“a fully electric Atlas robot”|벤더 주장. 성능/공장 성공 입증 아님|
|S04 Atlas 제품 버전 공개|[원문](https://bostondynamics.com/blog/boston-dynamics-unveils-new-atlas-robot-to-revolutionize-industry/)|보도자료|2026-01-05|첫 3문단·운용 모드 문단|“product version”|공개·생산 개시 계획·현장 양산을 분리|
|S05 Hyundai CES 로봇 전략|[원문](https://www.hyundaimotorgroup.com/en/news/hyundai-motor-group-announces-ai-robotics-strategy--to-lead-human-centered-robotics-era-at-ces-2026)|CES 2026 발표|2026-01 (일자 미확인)|도입 일정 요약·Atlas 배치 계획|“parts sequencing in 2028”|벤더 미래 계획. 실현/발표 전사 숫자의 정답 아님|
|S06 Spot TerrainParams·StairsMode|[원문](https://github.com/boston-dynamics/spot-sdk/blob/master/protos/bosdyn/api/spot/robot_command.proto)|master blob 183f8fa21869da813cb96e84b415fad6fd798b6f|미확인|TerrainParams L232~235; StairsMode L80~93|“Terrain coefficient of friction user hint”|SDK 선언·주석만 확인; 오일 제거/성공 보장 아님|
|S07 Spot GraphNav 기술 개요|[원문](https://github.com/boston-dynamics/spot-sdk/blob/master/docs/concepts/autonomy/graphnav_tech_summary.md)|master blob b92aad6f1ab282ed326065f6bfee4528adb211f2|미확인|feature data; Lost robots|“Areas that are largely empty”|환경 특징과 위치 추정의 벤더 설명; 해당 현장 원인 확증 아님|
|S08 Spot GraphNav 실행·피드백|[원문](https://github.com/boston-dynamics/spot-sdk/blob/master/docs/concepts/autonomy/graphnav_and_robot_locomotion.md)|master blob 136205162572d711884fda50eed126d085d4a1e3|미확인|NavigateRoute; Status and feedback; errors|“STATUS_LOST”|목표 도달 후 위치 재확인 및 명령 기한 설명; SDK 실제 운전 미시험|
|S09 NIST 응급 대응 로봇 시험 방법|[원문](https://www.nist.gov/programs-projects/performance-emergency-response-robots)|프로젝트 공식 문서|페이지 발행일 미확인|시험 방법·통제 변수 설명|“Variables are controlled initially”|반복·변수 통제 방법 재사용; 제조 현장 합격 수치로 전용 금지|
|S10 W3C SSN/SOSA|[원문](https://www.w3.org/TR/vocab-ssn/)|W3C Recommendation; 2017 문서, December 2017 상태 갱신|정확한 발행일 미확인|§5.1.2.20~21 hasOperatingRange/OperatingRange; Abstract|“under some specified Conditions”|센서/시스템 조건 어휘; 완성된 ROP 배정 모델 아님|
|S11 VDA 5050 공식 명세|[원문](https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md)|3.0.0; blob ba40d1e57368dced7ec3fbe5056a6c03d0d726ea|미확인|§2, §4.1, base 설명, state 주기|“fulfills the order up to the last released node”|안전/시설 인터페이스/프로젝트 책임/교통 알고리즘은 범위 밖|
|S12 gRPC Deadlines|[원문](https://grpc.io/docs/guides/deadlines/)|공식 가이드(언어별 구현 차이 있음)|미확인|Deadlines on the Client/Server|“gRPC does not set a deadline”|RPC 기한이지 물리 작업 완료 보장 아님|
|S13 OASIS MQTT|[원문](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html)|Version 5.0 OASIS Standard|2019-03-07|§4.3.1~3 QoS|“At most once”|메시지 전달 등급; 전체 업무의 exactly-once 아님|
|S14 Apache Kafka Design|[원문](https://kafka.apache.org/41/design/design/)|4.1 문서|미확인|Message Delivery Semantics|“requires cooperation with such systems”|외부 목적 시스템의 exactly-once는 협조 필요|
|S15 Model Context Protocol|[원문](https://modelcontextprotocol.io/specification/2025-11-25)|2025-11-25|2025-11-25(판 식별일)|Overview; Features; Security|“external data sources and tools”|LLM 도구/문맥 접속; 로봇 제어 안전성 보장 근거 아님|
|S16 Agent2Agent|[원문](https://a2a-protocol.org/v0.3.0/specification/)|0.3.0 고정판; latest와 구별|판 발행일 미확인|§1, §3, §5~7|“independent, potentially opaque AI agent systems”|agent 협업 메시지/작업; 로봇 간 물리 인계 규약 아님|
|S17 산업안전보건기준에 관한 규칙 제8조|[원문](https://www.law.go.kr/LSW/lsSideInfoP.do?docCls=jo&joBrNo=00&joNo=0008&lsiSeq=273603&urlMode=lsScJoRltInfoR)|고용노동부령 제450호; 시행 2025-09-01|2025-09-01|제8조 본문·1~4호|“근로자가 상시 작업하는 장소의 작업면 조도”|현행 연결 조문에서 확인. 모든 공간의 상시 점등 규정으로 확대 금지|
|S18 건축법 시행령 제51조|[원문](https://www.law.go.kr/LSW/lsSideInfoP.do?docCls=jo&joBrNo=00&joNo=0051&lsiSeq=290833&urlMode=lsScJoRltInfoR)|대통령령 제36746호; 시행 2026-10-06|2026-10-06|제51조제4항·단서|“11층 이하의 층”|아파트 예외 및 하위 규칙 적용; 모든 층 무조건 아님|
|S19 건축물방화구조규칙 제18조의2|[원문](https://www.law.go.kr/LSW/lsSideInfoP.do?docCls=jo&joBrNo=02&joNo=0018&lsiSeq=291033&urlMode=lsScJoRltInfoR)|국토교통부령 제1631호; 시행 2026-10-06|2026-10-06|제18조의2 1·1의2·2~6호|“2층 이상 11층 이하인 층”|web 실패 후 직접 curl -fsSL HTML 열람 성공. 층 예외·표시·크기·유리 세부조건|
|S20 Open-RMF Simulation|[원문](https://osrf.github.io/ros2multirobotbook/simulation.html)|공식 책 웹 문서|미확인|Robot plugins / slotcar|“rail-like”|교통/설비 시험 중심. 실제 로컬 내비게이션 충실도 보장 아님|
|S21 ClearGrasp|[원문](https://arxiv.org/abs/1910.02550)|arXiv v2; 저자 원문 초록만 열람|2019-10-14(v2), 2019-10-06(v1)|Abstract|“accurate depth estimates”|투명체 깊이 문제 연구; 발표 로봇·유리·현장 원인에 직접 적용하지 않음|
|S22 FLIR Measuring temperatures|[원문](https://docs.flir.com/T810605/en-US/latest/s10.html)|T810605; latest(상세 판 미확인)|미확인|Object parameters / Emissivity, Reflected temperature, Object distance|“Emissivity”|벤더 측정 문서; 해당 로봇 센서/대상 보정 성능 미확인|
|S23 Spot GraphNav map.proto|[원문](https://github.com/boston-dynamics/spot-sdk/blob/master/protos/bosdyn/api/graph_nav/map.proto)|master blob f37e49668480c2404e68e3d903714646414b76ba|미확인|Edge.Annotations.StairData/DescentPreference; PathFollowingMode|“PATH_MODE_STRICT”|정확한 수치/현장 사용 버전/중심 원인 미확인|

## 2. 출처별 주장 대조

|원문 근거|이 조사에서 허용한 주장|허용하지 않은 주장|
|---|---|---|
|S01~02 각 첫 본문|[추정] 벤더 주장: 합의 발표와 거래 완료 발표의 날짜가 다름|발표 전사 문장 자체가 정확했다는 확인|
|S03 본문·HTML datePublished|[추정] 벤더 주장: 전동 Atlas 소개 2024-04-17|2026 제품 버전과 동일 사건|
|S04 제품 발표·S05 계획|[추정] 벤더 주장: 제품 버전 공개·생산/배치 계획|장기 목표 달성·현장 성공률·발표 숫자 복원|
|S06 TerrainParams·S23 enum/주석|[추정] 벤더 주장: 마찰 힌트·strict path·하강 방향 옵션 존재|발표 수치·실제 해당 FW 설정·안전 성능|
|S07 특징 데이터·Lost robots, S08 피드백/오류|[추정] 벤더 주장: 특징 부족 설명과 LOST/STUCK 등 구분|발표 현장의 실제 원인과 회복 성능|
|S09 반복/환경 변수 시험 설명|[사실] 조건을 통제하고 단계적으로 바꾸는 시험 방법|NIST 응급 대응 시험의 수치를 제조/병원 합격값으로 전용|
|S10 OperatingRange|[사실] 지정 조건 아래 시스템의 정상 운용 특성 표현|전체 ROP 조건부 배정 모델이 표준에 이미 완성됨|
|S11 §2/4.1/상태·base|[사실] 관제–로봇 통신, 범위 제외, released node 수행·QoS|시설·안전·계약 책임·로봇 물리 결과의 보장|
|S12~16 명시 절|[사실] 각 프로토콜의 역할/전달·작업 의미|서로 같은 층의 대체재, 물리 실행 exactly-once, 실시간 안전|
|S17~19 현행 연결 조문|[사실] 조도 적용 장소, 진입창 층·예외·유리 조건|모든 조명 상시 점등, 모든 층 의무, 무파편 성능, 개별 차광안 적법 판정|
|S20 slotcar|[사실] 단순화된 교통 중심 시뮬레이션|이 저장소의 모든 모델과 동일 구현|
|S21 저자 초록|[사실] 투명체 깊이 추정 문제를 다룬 연구|발표 현장의 센서 원인·모델 적용 성능|
|S22 Object parameters|[추정] 벤더 주장: 방사율·반사 온도·거리 등 측정 매개변수|발표 기체/대상의 교정 정확도|

## 3. 법령 확인 과정과 판

- S17: 법령명/제8조 현행 링크에서 국가법령정보센터 조문으로 이동, 제8조 본문·1~4호 및 상단 시행일 확인. 근로자가 상시 작업하는 장소의 작업면과 작업 종류·단서를 구별한다.
- S18: 법령명/제51조 현행 링크에서 조문 이동, 제4항·아파트 예외와 시행 2026-10-06 표시 확인.
- S19: 법령명 전체 현행 링크가 lsiSeq=291033, efYd=20261006으로 연결됨을 확인한 뒤 제18조의2의 해당 lsiSeq HTML을 curl -fsSL로 읽음. 상단 국토교통부령 제1631호·시행 2026-10-06, 제1호·1의2호·2~6호 확인.
- [의견] 시행일은 해당 열람본 전체 법령의 시행 표시다. 개별 조항의 신설/개정일, 개별 건축물의 허가일·경과규정 적용과 혼동하지 않는다. 이번 조사에서 특정 건물의 적법성은 판정하지 않았다.

## 4. 열람 실패·불채택 기록

|대상/URL|결과·사유|처리|
|---|---|---|
|[ref-041 원 논문](https://www.nature.com/articles/s41598-025-16649-3)|web 열람이 idp.nature.com 인증 리다이렉트로 실패(500/non-retryable)|기존 위키에 그런 연구 카드가 있다는 사실만 대조. 논문 기술 주장·성능은 새 사실로 쓰지 않음|
|[산업안전보건규칙 제8조 현행 간편 링크](https://www.law.go.kr/법령/산업안전보건기준에관한규칙/제8조)|처음에는 lawService 래퍼 1줄만 보임|연결된 조문 원문으로 이동해 S17 회복; 래퍼를 원문 열람으로 세지 않음|
|[건축법 시행령 제51조 현행 간편 링크](https://www.law.go.kr/법령/건축법시행령/제51조)|처음에는 lawService 래퍼 1줄만 보임|연결된 조문 원문으로 이동해 S18 회복|
|[건축물방화구조규칙 제18조의2 간편 링크](https://www.law.go.kr/법령/건축물의피난ㆍ방화구조등의기준에관한규칙/제18조의2)|web Internal Error / not accessible|현행 전체 법령 링크에서 판 식별 후 S19 직접 URL 사용|
|S19 lsSideInfoP URL (단일/이중 슬래시)|web Internal Error 반복; python subprocess curl 시 DNS 해석 실패 1회|직접 curl -fsSL 호출에서 HTML 열람 성공. 원문 저장 파일은 만들지 않고 해당 조문만 읽음|
|[SoftBank /20201211](https://group.softbank/en/news/press/20201211)|열렸으나 자사주 매입 기사로 주제가 다름|인수 근거로 불채택. 검색 후 /20201211_0 원문을 열어 S01로 사용|
|[GraphNav Map Structure](https://dev.bostondynamics.com/docs/concepts/autonomy/graphnav_map_structure.html)|원문은 열렸으나 strict/방향 수치의 해당 근거를 찾지 못함|이 페이지에서 기능 부재를 결론내리지 않음. SDK map.proto S23의 해당 선언/주석을 추가 확인|
|[A2A latest](https://a2a-protocol.org/latest/specification/)|열람 성공, 가변 URL·판 혼합 가능|기술 표는 0.3.0 고정판 S16으로 한정. latest 내용을 0.3.0 규칙으로 섞지 않음|

[의견] 위키 ref-229(IDTA)·ref-470(ISO)의 카드를 읽은 것은 해당 표준 전문을 열었다는 뜻이 아니다. 이번 산출물에서 전문의 세부 수용 수치나 인증 요구를 새 [사실]로 채우지 않았다.

## 5. 기존 위키 열람 범위

기준 SHA의 본문 §9·11과 관련 정의/질문을 읽고, 본문에서 연결되는 s6 분리 페이지 §3의 관련 부분을 대조했다. 일부는 관련 부분만 읽었으므로 아래 목록을 전편 정독/모든 인용 검증 목록으로 해석하지 않는다. [01 차이표](01_existing-wiki-gap-matrix.md)에 28개 본문 파일과 절을 연결했다.

- robot-ontology 4~7; integration 20~22(23 업무 시스템은 연결 검토).
- platform 41~43; execution 29·31·32(30 물리 인계도 연결 검토).
- design 34·36; operations 38·39; planning 28; verification 55·56.
- site 62~66(61 창고는 연결 검토).
- docs/open-questions.md의 oq-022/024/032/033/208/210/213 및 관련 질문.
- manual-capability-ontology의 ontology-draft.md v0.5 §6, evaluation-and-verification.md §1~6, question-backlog.md 관련 q4/q5/q6.
- docs/references/ref-031.md, ref-041.md, ref-229.md, ref-406.md, ref-470.md의 서지·열람 상태. 참고문헌 카드의 이전 열람 성공/실패는 **이번 원문 열람과 구별**했다.
- _work/external_research_results/2026-10-11/STATUS.md의 완료/열람/부록 E 범위와 F-22-facility-and-building-system-integration.md 요약·초반 보완. 최근 결과 13개 전문을 재검증한 것은 아니다. 최신 integration 분리 페이지의 반영 내용도 함께 대조했다.

### 실제 연결을 따라 확인한 분리 페이지

- [docs/topics/2026/2026-09-25-area22-s6.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/topics/2026/2026-09-25-area22-s6.md) — 관련 §3. 번호만으로 현재 영역과 대응하지 않음.
- [docs/topics/2026/2026-09-30-area36-s6.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/topics/2026/2026-09-30-area36-s6.md) — 관련 §3. 번호만으로 현재 영역과 대응하지 않음.
- [docs/topics/2026/2026-09-25-area12-s6.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/topics/2026/2026-09-25-area12-s6.md) — 관련 §3. 번호만으로 현재 영역과 대응하지 않음.
- [docs/topics/2026/2026-09-25-area20-s6.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/topics/2026/2026-09-25-area20-s6.md) — 관련 §3. 번호만으로 현재 영역과 대응하지 않음.
- [docs/topics/2026/2026-09-25-area17-s6.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/topics/2026/2026-09-25-area17-s6.md) — 관련 §3. 번호만으로 현재 영역과 대응하지 않음.
- [docs/topics/2026/2026-09-25-area19-s6.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/topics/2026/2026-09-25-area19-s6.md) — 관련 §3. 번호만으로 현재 영역과 대응하지 않음.
- [docs/topics/2026/2026-09-25-area04-s6.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/topics/2026/2026-09-25-area04-s6.md) — 관련 §3. 번호만으로 현재 영역과 대응하지 않음.
- [docs/topics/2026/2026-09-25-area01-s6.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/topics/2026/2026-09-25-area01-s6.md) — 관련 §3. 번호만으로 현재 영역과 대응하지 않음.
- [docs/topics/2026/2026-10-11-area23-s6.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/topics/2026/2026-10-11-area23-s6.md) — 관련 §3. 번호만으로 현재 영역과 대응하지 않음.
- [docs/topics/2026/2026-10-11-area22-s6.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/topics/2026/2026-10-11-area22-s6.md) — 관련 §3. 번호만으로 현재 영역과 대응하지 않음.
- [docs/topics/2026/2026-09-25-area28-s6.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/topics/2026/2026-09-25-area28-s6.md) — 관련 §3. 번호만으로 현재 영역과 대응하지 않음.
- [docs/topics/2026/2026-10-11-area21-s6.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/topics/2026/2026-10-11-area21-s6.md) — 관련 §3. 번호만으로 현재 영역과 대응하지 않음.
- [docs/topics/2026/2026-10-10-area20-s6.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/topics/2026/2026-10-10-area20-s6.md) — 관련 §3. 번호만으로 현재 영역과 대응하지 않음.
- [docs/topics/2026/2026-10-10-area28-s6.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/topics/2026/2026-10-10-area28-s6.md) — 관련 §3. 번호만으로 현재 영역과 대응하지 않음.
- [docs/topics/2026/2026-09-25-area16-s6.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/topics/2026/2026-09-25-area16-s6.md) — 관련 §3. 번호만으로 현재 영역과 대응하지 않음.
- [docs/topics/2026/2026-10-09-area43-s6.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/topics/2026/2026-10-09-area43-s6.md) — 관련 §3. 번호만으로 현재 영역과 대응하지 않음.
- [docs/topics/2026/2026-09-25-area11-s6.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/topics/2026/2026-09-25-area11-s6.md) — 관련 §3. 번호만으로 현재 영역과 대응하지 않음.
- [docs/topics/2026/2026-10-09-area41-s6.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/topics/2026/2026-10-09-area41-s6.md) — 관련 §3. 번호만으로 현재 영역과 대응하지 않음.
- [docs/topics/2026/2026-09-29-area04-s6.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/topics/2026/2026-09-29-area04-s6.md) — 관련 §3. 번호만으로 현재 영역과 대응하지 않음.
- [docs/topics/2026/2026-09-29-area06-s6.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/topics/2026/2026-09-29-area06-s6.md) — 관련 §3. 번호만으로 현재 영역과 대응하지 않음.
- [docs/topics/2026/2026-09-29-area07-s6.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/topics/2026/2026-09-29-area07-s6.md) — 관련 §3. 번호만으로 현재 영역과 대응하지 않음.
- [docs/topics/2026/2026-09-25-area05-s6.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/topics/2026/2026-09-25-area05-s6.md) — 관련 §3. 번호만으로 현재 영역과 대응하지 않음.
- [docs/topics/2026/2026-09-29-area64-s6.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/topics/2026/2026-09-29-area64-s6.md) — 관련 §3. 번호만으로 현재 영역과 대응하지 않음.
- [docs/topics/2026/2026-09-29-area65-s6.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/topics/2026/2026-09-29-area65-s6.md) — 관련 §3. 번호만으로 현재 영역과 대응하지 않음.
- [docs/topics/2026/2026-09-29-area63-s6.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/topics/2026/2026-09-29-area63-s6.md) — 관련 §3. 번호만으로 현재 영역과 대응하지 않음.
- [docs/topics/2026/2026-09-29-area62-s6.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/topics/2026/2026-09-29-area62-s6.md) — 관련 §3. 번호만으로 현재 영역과 대응하지 않음.
- [docs/topics/2026/2026-09-29-area61-s6.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/topics/2026/2026-09-29-area61-s6.md) — 관련 §3. 번호만으로 현재 영역과 대응하지 않음.
- [docs/topics/2026/2026-09-30-area56-s6.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/topics/2026/2026-09-30-area56-s6.md) — 관련 §3. 번호만으로 현재 영역과 대응하지 않음.
- [docs/topics/2026/2026-09-25-area21-s6.md](https://github.com/MJKIM84/ai-hub/blob/9c4de242d0f08ac8804707b7cc7787fbd261fef4/rop-wiki/docs/topics/2026/2026-09-25-area21-s6.md) — 관련 §3. 번호만으로 현재 영역과 대응하지 않음.

## 6. 시뮬레이터 코드 근거

C-SIM1~6의 원문 파일·줄·함수는 [06](06_simulation-validation-boundaries.md#1-이-저장소에서-확인한-근거)에 있다. incidents.py와 sensing.py는 함수 본문, physics.py는 마찰/접촉·range_scan·tracked_people·시설 관측 관련 부분, facilities.py는 recover/_fresh 관련 부분을 읽었다. 기준 SHA 고정, 수정/실행 없음. 지원 범위를 저장소 이름이나 3D 화면으로 추측하지 않았다.

## 7. 공개/비공개·증거 강도 검토

- 발표 정리 원문 파일은 입력으로만 읽었다. 공개 산출물에는 발표자 실명·구체 비공개 현장명·실적/설정 수치를 옮기지 않았다.
- 발표 취지의 일반화는 [발표 내 확인], 독립적으로 확인한 일반 규약/법령/연구는 원문 근거, 미확인 전사는 질문으로 분리했다.
- 당사자 보도자료가 다른 사이트에 재배포된 경우 독립 출처로 세지 않는다(S02). 같은 회사 블로그/SDK 여러 페이지도 해당 현장 성과의 독립 교차 검증이 아니다.
- 이번 발표 사례의 현장 인과/개선 효과를 독립 교차 검증한 건수는 0이다. 공개 문서와 발표가 양립한다는 것만으로 수치를 검증했다고 하지 않는다.
- 비용·허용 지연·조건부 배정·재현 계획은 [의견]으로 제안했다. 실제 실험·성능·법적 승인으로 표현하지 않았다.
- S01~S23은 필요한 해당 원문 부분을 열람했다(23/23, S21 초록 한정). Nature 논문 실패 1건은 이 분모에 넣지 않았으며 위 실패 표에 별도 공개했다. 이것을 전체 문헌 전문 열람률이나 현장 검증률로 부르지 않는다.
