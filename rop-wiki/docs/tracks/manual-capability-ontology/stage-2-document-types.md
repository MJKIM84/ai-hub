---
title: "단계 2. 로봇 문서 유형과 정보 구조 조사"
type: track-stage
track: manual-capability-ontology
stage: 2
related_areas: [5, 27, 21]
tags: [제조사 문서, 문서 유형, 정보 형태, 공개 문서 샘플, 벤더 주장]
status: published
confidence: low
created: 2026-09-24
updated: 2026-09-25
sources: [ref-505, ref-506, ref-507, ref-508, ref-509, ref-510, ref-511, ref-512, ref-513, ref-514, ref-515, ref-040, ref-228, ref-230]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › 중점 연구 트랙 › [매뉴얼 기반 로봇 기능 온톨로지](index.md) › 단계 2. 로봇 문서 유형과 정보 구조 조사

# 단계 2. 로봇 문서 유형과 정보 구조 조사

> 단계 상태: 진행 중 · 열린 질문: 6건 · 답한 질문: 1건 · 완료 조건: 미충족 · 마지막 실행: 2026-09-25

## 1. 이 단계에서 밝힐 것

> 로봇 제조사 문서에 기능 정보가 어떤 유형·형태로 흩어져 있는가.

위 문장은 트랙 정의의 "밝힐 것"을 그대로 옮긴 것이다(트랙 정의의 단계별 밝힐 것과 완료 조건은 [트랙 개요](index.md)의 단계 진행 현황에 정리되어 있다). 이 단계는 [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md)의 정의에 나오는 제조사별 기능·제약·장착 장비·실행 조건이 실제 문서의 어느 유형·어떤 형태에 있는지를 묻는다. 문서 분석은 [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md)의 온보딩 절차 일부이기도 하다. 조사 결과는 [문서 유형 매트릭스](document-type-matrix.md)와 공개 문서 샘플 목록으로 이어진다.

## 2. 질문 목록

이 단계의 시작 질문 5개와 뒤에 더해진 질문 2개(q2-06, q2-07)다. 시작 질문 문장은 괄호 안의 내용까지 트랙 정의 그대로다. 상태와 답 위치는 [질문 백로그](question-backlog.md)와 일치시키며, 백로그의 "조사 중"은 이 표에서 "열림"으로 표시하고 "폐기"는 표에서 빼고 백로그에만 남긴다. [가정] 답은 3절의 질문 id로 시작하는 소제목에 실리고, 답 위치 칸에는 그 앵커 또는 주제 페이지 링크를 적는다. 제기 근거 칸의 값은 finding id(제안한 실행 id 병기) 또는 "사용자" 가운데 하나만 쓴다.

페이지 상단의 단계 상태 줄은 퍼블리셔가 다시 쓰는 자동 갱신 영역이 아니라, 스토리텔러 에이전트가 이 페이지를 갱신할 때 [질문 백로그](question-backlog.md)와 맞추는 값이다. 기준값은 [트랙 개요](index.md)의 단계 진행 현황 자동 표와 최근 실행 자동 표이며, 이 줄과 그 표가 다르면 그 표를 따른다. [가정]

| id | 질문 | 상태 | 제기 근거 | 답한 실행 id | 답 위치 |
|---|---|---|---|---|---|
| q2-01 | 제조사가 제공하는 문서 유형(사용자 매뉴얼, 통합·API 가이드, 사양서·데이터시트, 안전 매뉴얼, 오류 코드표, 릴리스 노트, 치수도·도면)은 무엇이며 각각 어떤 기능 정보를 담는가? | 답함 | 사용자 | 2026-09-25-57 | [q2-01 답](#q2-01) |
| q2-02 | 기능 정보는 어떤 형태(문장, 표, 그림·다이어그램, 코드 예제, 파라미터 표)로 존재하며 형태별 추출 난이도는 어떠한가? | 열림 | 사용자 | | |
| q2-03 | 공개적으로 접근할 수 있는 대표 문서 샘플(AMR, 협동로봇, 로봇팔 등)은 무엇이고 이용 조건은 어떠한가? | 열림 | 사용자 | | |
| q2-04 | 문서에 없지만 실행에 필요한 정보(암묵지)는 무엇이고 어디서 보완하는가(제조사 문의, 시험, 커뮤니티)? | 열림 | 사용자 | | |
| q2-05 | 언어·문서 버전·옵션 장비에 따라 같은 기종의 정보가 어떻게 달라지는가? | 열림 | 사용자 | | |
| q2-06 | 제조사는 IDTA 02047 의 특수 능력(SpecialCapabilities) 같은 자유 텍스트 항목이나 매뉴얼에 계단·도어 조작·충전 같은 범위 능력을 실제로 어떻게 적는가? (q1-09 에서 파생) | 열림 | f8, 실행 2026-09-25-35 | | |
| q2-07 | AMR 제조사(MiR·OTTO·국내 물류로봇 업체 등)가 공개하는 매뉴얼·REST API 문서는 무엇이며, 공개되지 않을 때 표준 스키마(VDA 5050 팩트시트·MassRobotics)로 대신할 수 있는 정보와 없는 정보는 무엇인가? (q2-03 에서 파생) | 열림 | f20, 실행 2026-09-25-57 | | |

질문 문장 속 약어는 다음과 같다. AMR은 자율이동로봇(Autonomous Mobile Robot, AMR), API는 응용 프로그램 인터페이스(Application Programming Interface, API)이다. q2-02·q2-03은 이번 실행에서 부분 답을 냈으므로 백로그에서는 "조사 중"이다.

## 3. 조사 결과

실행 2026-09-25-57은 q2-01에 답하고 q2-02·q2-03에 부분 답을 냈다. 제조사 문서는 문서 구조·정보 형태·이용 조건의 사례로만 인용하며, 문서에 적힌 내용은 독립 출처로 확인되기 전까지 벤더 주장이다. 이번 실행은 원문 열람이 제한된 환경에서 이뤄졌고, GitHub 공식 저장소 원문만 직접 열었다.

### q2-01 제조사 문서 유형과 담긴 기능 정보 {#q2-01}

사용 정보의 구성은 두 표준이 정한다. ISO 20607:2019 는 기계 제조사가 설명서(instruction handbook)의 안전 관련 부분을 작성할 때의 요구사항을 정하며, 기계 수명주기 전 단계를 고려한 안전 관련 내용·구조·표현을 다루고 ISO 12100:2010 6.4.5 의 사용 정보 일반 요구를 구체화한다(2019 판 기준, 원문 미열람). [사실][^ref-509] IEC/IEEE 82079-1:2019 는 모든 종류 제품의 사용 정보(instructions for use) 작성 원칙과 요구사항을 정하는 2019 판 표준(2012 초판 대체)으로, 정보 품질·정보 관리 과정과 사용 정보의 실증적 평가 방법을 규범 부분에 둔다(2019 판 기준, 원문 미열람). [사실][^ref-510]

해외 제조사의 공개 문서는 다음과 같은 구조를 보인다. Boston Dynamics Spot SDK 공식 저장소 README 는 문서를 개념 설명, 파이썬 클라이언트 라이브러리(예제·빠른 시작), 페이로드 개발자 문서(기계·전기·소프트웨어 인터페이스), API 프로토콜 참조, 릴리스 노트, 라이선스로 나눈다(확인일 2026-09-25). [추정] 벤더 주장[^ref-505] Kinova Kortex API 공식 저장소 README 는 C++·Python API 메커니즘과 예제, Modbus 인터페이스, 언어별 오류 처리 문서, 펌웨어·API 판별 다운로드(Gen3 2.8.0, Gen3 lite 펌웨어 2.3.4·API 2.3.0)를 안내한다(확인일 2026-09-25). [추정] 벤더 주장[^ref-506] Kortex 문서 가운데 저수준 제어(서보 모드)를 다루는 부분은 분류 원문 9장 "로봇 자체 지능·제어" 경계의 연계 대상이므로, 이 위키에서는 문서 유형의 사례로만 보고 ROP 직접 범위로 다루지 않는다. [의견]

국내 협동로봇 제조사도 문서를 나눠 공개한다. 두산로보틱스는 로봇랩 포털에서 설치 매뉴얼(설치 방법·인터페이스·수동/자동 모드·안전 관련 기능)과 기타 매뉴얼(액세서리·퀵 가이드·ROS·API 사용 방법)을 제공한다(검색 결과 기준, 원문 미열람). [추정] 벤더 주장[^ref-511] 두산로보틱스 doosan-robot2 공식 저장소 README 는 튜토리얼 등 자세한 내용을 공식 ROS2 매뉴얼 포털로 안내하고, ROS2 Humble 에서 전 기종 지원을 밝힌다(확인일 2026-09-25). [추정] 벤더 주장[^ref-507] 레인보우로보틱스의 공식 클라이언트 라이브러리 rbpodo README 는 RB 시리즈 협동로봇용 C++17·Python 클라이언트로서 제어 박스와 5000번 포트로 명령·응답을, 5001번 포트로 상태 데이터를 주고받는다고 적고 개요·예제 문서를 링크한다(확인일 2026-09-25). [추정] 벤더 주장[^ref-508] 레인보우로보틱스는 협동로봇 기술자료 공개 페이지(rb_cobot_docs)도 두고 있다(원문 미열람). [추정] 벤더 주장[^ref-512]

이동로봇 쪽 사양서·데이터시트 정보에는 표준 스키마가 있다. VDA 5050 팩트시트 JSON 스키마(main, 3.0.0)는 유형 명세·물리 파라미터·프로토콜 한계·지원 기능·기하·적재 명세 블록(typeSpecification·physicalParameters·protocolLimits·protocolFeatures·mobileRobotGeometry·loadSpecification)을 기계가독 형식으로 둔다(확인일 2026-09-25). [사실][^ref-228] 이 팩트시트를 이동로봇 쪽 사양서·데이터시트 정보의 표준화된 대응물로 보는 것은 출처에 없는 이 위키의 해석이다. [추정][^ref-228]

위 사례를 문서 유형에 대응시키면 통합·API 가이드는 기능·인터페이스(명령·상태)·오류 처리를, 설치·안전 매뉴얼은 운전 모드·안전 제약을, 릴리스 노트는 판별 변경을, 페이로드·액세서리 문서는 장착 장비 인터페이스를, 사양서·데이터시트는 파라미터 범위를 주로 담는 것으로 보인다. 이 대응은 이 위키의 종합(추론)이며 측정 근거는 없다. [추정][^ref-505][^ref-506][^ref-511][^ref-509][^ref-228] 질문이 든 문서 유형 가운데 사용자 매뉴얼, 오류 코드표, 치수도·도면은 이번 샘플에서 확인하지 못했으며, [문서 유형 매트릭스](document-type-matrix.md)의 해당 행은 미조사로 남겼다.

### q2-02 기능 정보의 형태와 추출 난이도 (부분 답) {#q2-02}

기능 정보는 설정 파일·데이터 형식·코드 예제로도 존재한다. Open-RMF PerformAction 튜토리얼은 플릿이 수행할 수 있는 동작을 config.yaml 의 actions 목록으로 선언하고, 작업 요청을 JSON 으로, 동작 실행 논리를 파이썬 코드 예제로 보여 준다. [사실][^ref-040] Kinova Kortex 는 Google Protocol Buffers 문서를 참조하고 Spot SDK 는 API 프로토콜 참조를 두어, 두 제조사 모두 API 를 기계가독 프로토콜 정의와 코드 예제 형태로 제공하는 것으로 보인다(프로토콜 정의 파일 자체는 열지 않음). [추정] 벤더 주장[^ref-505][^ref-506]

범용 문서 파싱 평가는 형태별로 나뉘어 있다. OmniDocBench 공식 저장소 README 는 1,651개 PDF 페이지, 문서 유형 10종, 레이아웃 5종, 언어 5종으로 구성된 벤치마크에서 텍스트 문단·표·수식·읽기 순서를 나눠 정규화 편집 거리·TEDS 등으로 평가하며, 문서 유형으로 논문·재무 보고서·신문·교과서·손글씨 노트 등을 들고 매뉴얼은 명시하지 않는다(확인일 2026-09-25). [사실][^ref-513] 그래서 로봇 매뉴얼의 형태별(문장·표·그림·코드) 추출 난이도는 공개 측정 자료로 확인되지 않은 것으로 보인다. 이는 이번 조사 범위의 관찰이자 이 위키의 추론이며, 측정 자료의 부재가 확정된 것은 아니다. [추정][^ref-513][^ref-514]

매뉴얼을 대상으로 한 추출 연구는 있다. 매뉴얼 해석은 분류 원문 8장 교차 규칙에 따라 [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md)의 방법이 5. 로봇 능력·작업 온톨로지와 21. 온보딩·설정·현장 시운전에 적용되는 것이다. Springer 게재 장 "Conversational Knowledge Extraction from Technical Manuals"는 매뉴얼 전처리·색인, 온톨로지 제약을 건 검색 증강 생성(Retrieval-Augmented Generation, RAG) 기반 개체·관계 추출, 대화형 절차 안내를 결합한 대규모 언어 모델(LLM) 프레임워크를 제안했다(교육용 기술 매뉴얼 대상, 정확도 수치 미확인, 원문 미열람). [사실][^ref-514] ManuExtract 는 제조 분야 문서에서 항목–속성–값 삼중항을 추출하는 벤치마크 데이터셋으로, LLM 생성 주석을 도메인 전문가가 다듬어 구축했다(원문 미열람). [사실][^ref-515]

확인한 사례로 보면 기능 정보의 형태는 기계가독 스키마·설정(VDA 5050 팩트시트, Open-RMF config.yaml, 프로토콜 정의) → 파라미터 표 → 문장 → 그림·다이어그램 순으로 구조화 추출이 쉬워질 것으로 보인다. 이 순서는 형태별 구조 정도에서 도출한 이 위키의 추론이며 측정 근거는 없으므로 측정 결과로 읽지 않는다. [추정][^ref-228][^ref-040][^ref-513][^ref-514]

남은 부분은 로봇 매뉴얼의 형태별(문장·파라미터 표·그림·코드 예제) 추출 정확도를 범용 문서 파싱 벤치마크와 비교해 측정할 수 있는 공개 데이터셋이나 평가 방법이 있는지다. 이 물음은 q2-02의 남은 부분으로 두며, 로봇 문서 파싱 결과를 묻는 [단계 3. 비정형 문서에서 온톨로지를 추출하는 방법 조사](stage-3-extraction-methods.md)의 q3-01과 함께 본다.

### q2-03 공개 문서 샘플과 이용 조건 (부분 답) {#q2-03}

이번에 확인한 공개 문서 샘플은 로봇팔·협동로봇(Kinova, 두산로보틱스, 레인보우로보틱스)과 4족 보행 로봇(Spot)이다. 목록은 [문서 유형 매트릭스](document-type-matrix.md)의 4절에 있다. AMR 제조사의 공개 매뉴얼 샘플은 이번 조사에서 찾지 못했으며(부재 확정 아님), AMR 쪽은 VDA 5050 팩트시트·MassRobotics 스키마 같은 표준 스키마로만 대신되는 것으로 보인다. [추정][^ref-505][^ref-506][^ref-507][^ref-508][^ref-228][^ref-230]

이용 조건은 샘플마다 다르다. Spot SDK 는 GitHub 에 공개되어 있으나 사용·복제·배포가 Boston Dynamics SDK 라이선스(20191101-BDSDK-SL) 조건을 따른다. [추정] 벤더 주장[^ref-505] Kinova Kortex API 저장소는 BSD 3-Clause 라이선스로 공개되어 있다. [추정] 벤더 주장[^ref-506] 국내 협동로봇 제조사의 공개 저장소(두산 doosan-robot2: Apache 2.0·BSD 3-Clause, 레인보우 rbpodo: Apache 2.0)는 코드에 개방 라이선스를 달지만, 포털에서 내려받는 매뉴얼 문서 자체의 이용 조건은 이번에 확인하지 못했다. [추정] 벤더 주장[^ref-507][^ref-508][^ref-511]

남은 부분은 AMR 제조사의 공개 매뉴얼 샘플(새 질문 q2-07)과 포털 매뉴얼 문서의 이용 약관이다. 코드 라이선스와 별개로 매뉴얼을 자동 추출·재가공해 쓰는 것이 허용되는지는 새 질문 q6-07로 [단계 6. 변경 관리·운영·거버넌스 조사](stage-6-lifecycle-governance.md)에 보냈다.

## 4. 결론과 남은 불확실성

**결론**

- 사용 정보의 작성은 ISO 20607:2019(설명서의 안전 관련 부분)와 IEC/IEEE 82079-1:2019(모든 종류 제품의 사용 정보)가 정한다. [사실][^ref-509][^ref-510]
- 공개 샘플에서 통합·API 가이드, 설치 매뉴얼, 릴리스 노트, 페이로드·액세서리 문서의 구조를 확인했고, 문서 유형별로 담긴 정보의 대응은 이 위키의 종합(추론)이다. [추정][^ref-505][^ref-506][^ref-511][^ref-228]
- 기능 정보는 문장·표뿐 아니라 설정 파일·JSON·코드 예제 형태로도 존재한다. [사실][^ref-040]
- 범용 문서 파싱 벤치마크 OmniDocBench 는 문서 유형에 매뉴얼을 두지 않는다. [사실][^ref-513]
- 공개 저장소의 코드는 개방 라이선스나 제조사 SDK 라이선스를 달지만, 포털 매뉴얼의 이용 조건은 확인되지 않았다. [추정] 벤더 주장[^ref-505][^ref-507][^ref-508][^ref-511]

**남은 불확실성**

- 사용자 매뉴얼, 오류 코드표, 치수도·도면 유형은 이번 샘플에서 확인하지 못했다.
- q2-02 부분 답: 로봇 매뉴얼의 형태별(문장·표·그림·코드) 추출 정확도를 측정한 자료를 찾지 못했다(부재 확정 아님).
- q2-03 부분 답: AMR 제조사 공개 매뉴얼 샘플과 포털 매뉴얼 문서의 이용 약관이 확인되지 않았다.
- 원문 미열람 출처: ISO 20607, IEC/IEEE 82079-1, 두산로보틱스 로봇랩 매뉴얼 게시판, rb_cobot_docs, Springer 게재 장 두 건, MassRobotics 스키마. Springer 게재 장 두 건은 저자·발행일도 미확인이다.
- 제조사 문서 근거는 모두 벤더 주장이며, 이번 실행의 발견 사항은 교차 확인되지 않았다.
- 온톨로지: [능력 온톨로지 초안](ontology-draft.md)을 v0.3 → v0.4로 올려 근거 문서에 속성 "문서 유형"·"이용 조건"을 더하고 근거 문서를 확정했다. 속성 "정보 형태"는 문서 단위가 아니라 문서 안 위치 단위의 속성일 수 있고 근거가 측정 없는 추론이라 반영하지 않고 초안 6절 "근거 문서의 단위와 버전" 질문에 합쳤다.

## 5. 이 단계가 낳은 후속 질문

| 새 질문 id | 질문 | 보낼 단계 | 근거 finding id | 상태 |
|---|---|---|---|---|
| q2-07 | AMR 제조사(MiR·OTTO·국내 물류로봇 업체 등)가 공개하는 매뉴얼·REST API 문서는 무엇이며, 공개되지 않을 때 표준 스키마(VDA 5050 팩트시트·MassRobotics)로 대신할 수 있는 정보와 없는 정보는 무엇인가? (q2-03 에서 파생) | 단계 2. 로봇 문서 유형과 정보 구조 조사 | f20 (실행 2026-09-25-57) | 열림 |
| q6-07 | SDK 코드 라이선스와 별개로 제조사 매뉴얼 문서를 자동 추출·재가공해 능력 온톨로지에 쓰는 것이 이용 조건상 허용되는가, 이를 누가 확인하고 기록하는가? (q2-03 에서 파생) | 단계 6. 변경 관리·운영·거버넌스 조사 | f19 (실행 2026-09-25-57) | 열림 |

형태별 추출 정확도 측정 데이터셋·평가 방법을 묻는 후속 질문은 q2-02·q3-01과 중복되어 새로 등록하지 않고 3절 q2-02의 남은 부분으로 두었다.

## 6. 완료 조건 충족 현황

완료 조건은 트랙 정의의 문장을 옮기되 파일명은 페이지 링크로 바꾸고, 조건이 여러 항목이면 행을 나눴다. 충족 여부는 리서치 에이전트의 자체 평가를 스토리텔러 에이전트가 옮겨 적은 값이고, 검증 판정 칸은 내용 검증 에이전트의 1차 판정이다. 둘이 다르면 검증 판정을 따른다.

> 완료 조건: 문서 유형 × 정보 항목 매트릭스(`document-type-matrix.md`), 공개 문서 샘플 목록.

| 완료 조건 | 충족 여부 | 근거 | 검증 판정 |
|---|---|---|---|
| 문서 유형 × 정보 항목 매트릭스([document-type-matrix.md](document-type-matrix.md)) | 미충족 | [문서 유형 매트릭스](document-type-matrix.md) 64칸 가운데 9칸을 채웠다(통합·API 가이드, 안전 매뉴얼, 릴리스 노트, 사양서·데이터시트, 페이로드·액세서리 문서 행의 일부). 사용자 매뉴얼·오류 코드표·치수도·도면 행은 미조사 | 미충족 · 미승인 |
| 공개 문서 샘플 목록 | 미충족 | [문서 유형 매트릭스](document-type-matrix.md) 4절에 샘플 4건(Spot SDK, Kinova Kortex, 두산로보틱스, 레인보우로보틱스)을 실었다. AMR 샘플이 없고 포털 매뉴얼 이용 조건이 미확인 | 미충족 · 미승인 |

다음 단계로 전환: 아니오(q2-02·q2-03 부분 답, q2-04·q2-05·q2-06 열림, 매트릭스 미조사 칸)

## 7. 관련 세부영역

이 트랙은 분류를 바꾸지 않는다. 각 항목 뒤에는 이 단계에서 확인된 사실을 그 영역 페이지의 어느 절에 반영하자고 제안할지를 적었다. 반영 제안은 세부영역 페이지를 직접 고치지 않고 [트랙 로그](log.md)의 "세부영역 반영 제안" 항목으로 남기며, 반영은 다음 해당 영역 실행에서 한다. 프런트매터 `related_areas`는 아래 목록과 같다.

**중심 영역**

- [5. 로봇 능력·작업 온톨로지](../../categories/b-common-information-and-environment-model/05-robot-capability-and-task-ontology.md) — 제조사별 기능·제약·장착 장비·실행 조건이 문서 어디에 어떤 형태로 있는지가 이 영역의 공통 모델을 어떻게 채울 수 있는지를 정한다. 실행 2026-09-25-57은 문서 유형·형태별 분산과 기계가독 스키마 사례를 "6. 대표 접근법과 기술" 절에 반영하도록 제안했다.

**연구 방법으로 연결되는 영역(분류 원문 8장의 교차 규칙)**

- [27. AI·학습·적응과 모델 운영](../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md) — 문서 유형과 정보 형태에 따른 추출 난이도는 이 영역의 문서 해석 방법이 단계 3에서 무엇을 다뤄야 하는지를 정한다. 실행 2026-09-25-57은 매뉴얼 대상 LLM 추출 연구와 문서 파싱 벤치마크를 "6. 대표 접근법과 기술"·"8. 대표 연구와 자료" 절에 반영하도록 제안했다(적용 대상인 5. 로봇 능력·작업 온톨로지와 21. 온보딩·설정·현장 시운전에도 연결).

**이 단계의 질문이 언급하는 영역(트랙 개요의 배정에 따른 추가 연결, [가정])**

- [21. 온보딩·설정·현장 시운전](../../categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md) — 문서 분석과 기능 탐색은 이 영역의 온보딩 절차 일부다. 실행 2026-09-25-57은 온보딩 때 모을 제조사 문서 유형과 공개 경로·이용 조건(국내 제조사 사례 포함)을 "6. 대표 접근법과 기술" 절에 반영하도록 제안했다.

## 8. 출처

[^ref-505]: Boston Dynamics (boston-dynamics/spot-sdk GitHub), spot-sdk — README, 미확인, https://github.com/boston-dynamics/spot-sdk, 접근일 2026-09-25
[^ref-506]: Kinova (Kinovarobotics/kortex GitHub), kortex — readme, 미확인, https://github.com/Kinovarobotics/kortex, 접근일 2026-09-25
[^ref-507]: Doosan Robotics (doosan-robotics/doosan-robot2 GitHub), doosan-robot2 — README (humble), 미확인, https://github.com/doosan-robotics/doosan-robot2, 접근일 2026-09-25
[^ref-508]: Rainbow Robotics (RainbowRobotics/rbpodo GitHub), rbpodo — README, 미확인, https://github.com/RainbowRobotics/rbpodo, 접근일 2026-09-25
[^ref-509]: ISO, ISO 20607:2019 - Safety of machinery — Instruction handbook — General drafting principles, 2019, https://www.iso.org/standard/68519.html, 접근일 2026-09-25 (원문 미열람)
[^ref-510]: IEC / IEEE / ISO, IEC/IEEE 82079-1:2019 - Preparation of information for use (instructions for use) of products — Part 1: Principles and general requirements, 2019, https://www.iso.org/standard/71620.html, 접근일 2026-09-25 (원문 미열람)
[^ref-511]: 두산로보틱스, 매뉴얼 : Doosan Robotics Training & Service, 미확인, https://robotlab.doosanrobotics.com/ko/board/Resources/Manual, 접근일 2026-09-25 (원문 미열람)
[^ref-512]: Rainbow Robotics, Rainbow Robotics 협동로봇 기술자료 (rb_cobot_docs), 미확인, https://rainbowrobotics.github.io/rb_cobot_docs/ko/, 접근일 2026-09-25 (원문 미열람)
[^ref-513]: OpenDataLab (opendatalab/OmniDocBench GitHub), OmniDocBench — README, 미확인, https://github.com/opendatalab/OmniDocBench, 접근일 2026-09-25
[^ref-514]: Springer Nature (게재 장 저자 미확인), Conversational Knowledge Extraction from Technical Manuals: An LLM-Based Framework with Ontological Guidance, 미확인, https://link.springer.com/chapter/10.1007/978-3-032-19096-3_30, 접근일 2026-09-25 (원문 미열람)
[^ref-515]: Springer Nature (게재 장 저자 미확인), Enhancing LLMs for Manufacturing Information Extraction, 미확인, https://link.springer.com/chapter/10.1007/978-981-92-1468-6_21, 접근일 2026-09-25 (원문 미열람)
[^ref-040]: Open Robotics, PerformAction Tutorial - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_action_tutorial.html, 접근일 2026-09-25
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-09-25
[^ref-230]: MassRobotics, MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-09-25 (원문 미열람)

## 9. 이력

실행 id는 트랙 실행의 id(YYYY-MM-DD-NN)이며, 구축 시드 항목은 [트랙 로그](log.md)와 같은 표기 `build-2026-09-24`를 쓴다. 이 값은 실행 id가 아니라 위키 구축 시점을 나타내며, 파이프라인 실행이 아니므로 일일 로그가 없다.

| 날짜 | 실행 id | 답한 질문 | 새 질문 | 온톨로지 변경 | 버전 |
|---|---|---|---|---|---|
| 2026-09-25 | 2026-09-25-57 | q2-01(q2-02·q2-03 부분 답) | q2-07, q6-07 | v0.3 → v0.4 | 2 |
| 2026-09-24 | build-2026-09-24(구축 시드, 파이프라인 실행 아님) | 없음 | 시드 q2-01~q2-05(5건, 구축 시 [질문 백로그](question-backlog.md)에 등록) | 없음(v0 시드는 [능력 온톨로지 초안](ontology-draft.md)에서 생성) | 1 |
