---
title: "단계 2. 로봇 문서 유형과 정보 구조 조사"
type: track-stage
track: manual-capability-ontology
stage: 2
related_areas: [4, 5, 18, 45, 47, 55, 57]
tags: [제조사 문서, 문서 유형, 정보 형태, 공개 문서 샘플, 암묵지, 벤더 주장]
status: published
confidence: low
created: 2026-09-24
updated: 2026-10-09
sources: [ref-505, ref-506, ref-507, ref-508, ref-509, ref-510, ref-511, ref-512, ref-513, ref-514, ref-515, ref-040, ref-228, ref-230, ref-105, ref-041, ref-1375, ref-1376, ref-1377, ref-1378, ref-1379, ref-1380, ref-1381, ref-1382, ref-1383, ref-1384, ref-1385, ref-1386, ref-1387, ref-1388, ref-1389, ref-1390, ref-1072, ref-1071]
last_run: 2026-10-09
version: 4
---

[홈](../../index.md) › 중점 연구 트랙 › [매뉴얼 기반 로봇 기능 온톨로지](index.md) › 단계 2. 로봇 문서 유형과 정보 구조 조사

# 단계 2. 로봇 문서 유형과 정보 구조 조사

> 단계 상태: 진행 중 · 열린 질문: 2건 · 답한 질문: 5건 · 완료 조건: 미충족 · 마지막 실행: 2026-10-09

## 1. 이 단계에서 밝힐 것

> 로봇 제조사 문서에 기능 정보가 어떤 유형·형태로 흩어져 있는가.

위 문장은 트랙 정의의 "밝힐 것"을 그대로 옮긴 것이다(트랙 정의의 단계별 밝힐 것과 완료 조건은 [트랙 개요](index.md)의 단계 진행 현황에 정리되어 있다). 이 단계는 [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md)의 정의에 나오는 제조사별 기능·제약·장착 장비·실행 조건이 실제 문서의 어느 유형·어떤 형태에 있는지를 묻는다. 문서 분석은 [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md)의 온보딩 절차 일부이기도 하다. 조사 결과는 [문서 유형 매트릭스](document-type-matrix.md)와 공개 문서 샘플 목록으로 이어진다.

## 2. 질문 목록

이 단계의 시작 질문 5개와 뒤에 더해진 질문 2개(q2-06, q2-07)다. 시작 질문 문장은 괄호 안의 내용까지 트랙 정의 그대로다. 상태와 답 위치는 [질문 백로그](question-backlog.md)와 일치시키며, 백로그의 "조사 중"은 이 표에서 "열림"으로 표시하고 "폐기"는 표에서 빼고 백로그에만 남긴다. [가정] 답은 3절의 질문 id로 시작하는 소제목에 실리고, 답 위치 칸에는 그 앵커 또는 주제 페이지 링크를 적는다. 제기 근거 칸의 값은 finding id(제안한 실행 id 병기) 또는 "사용자" 가운데 하나만 쓴다.

페이지 상단의 단계 상태 줄은 퍼블리셔가 다시 쓰는 자동 갱신 영역이 아니라, 스토리텔러 에이전트가 이 페이지를 갱신할 때 [질문 백로그](question-backlog.md)와 맞추는 값이다. 기준값은 [트랙 개요](index.md)의 단계 진행 현황 자동 표와 최근 실행 자동 표이며, 이 줄과 그 표가 다르면 그 표를 따른다. [가정]

| id | 질문 | 상태 | 제기 근거 | 답한 실행 id | 답 위치 |
|---|---|---|---|---|---|
| q2-01 | 제조사가 제공하는 문서 유형(사용자 매뉴얼, 통합·API 가이드, 사양서·데이터시트, 안전 매뉴얼, 오류 코드표, 릴리스 노트, 치수도·도면)은 무엇이며 각각 어떤 기능 정보를 담는가? | 답함 | 사용자 | 2026-09-25-57 | [q2-01 답](#q2-01) |
| q2-02 | 기능 정보는 어떤 형태(문장, 표, 그림·다이어그램, 코드 예제, 파라미터 표)로 존재하며 형태별 추출 난이도는 어떠한가? | 답함 | 사용자 | 2026-10-09-23 | [q2-02 답](#q2-02) |
| q2-03 | 공개적으로 접근할 수 있는 대표 문서 샘플(AMR, 협동로봇, 로봇팔 등)은 무엇이고 이용 조건은 어떠한가? | 답함 | 사용자 | 2026-10-09-23 | [q2-03 답](#q2-03) |
| q2-04 | 문서에 없지만 실행에 필요한 정보(암묵지)는 무엇이고 어디서 보완하는가(제조사 문의, 시험, 커뮤니티)? | 답함 | 사용자 | 2026-10-09-22 | [q2-04 답](#q2-04) |
| q2-05 | 언어·문서 버전·옵션 장비에 따라 같은 기종의 정보가 어떻게 달라지는가? | 답함 | 사용자 | 2026-10-09-23 | [q2-05 답](#q2-05) |
| q2-06 | 제조사는 IDTA 02047 의 특수 능력(SpecialCapabilities) 같은 자유 텍스트 항목이나 매뉴얼에 계단·도어 조작·충전 같은 범위 능력을 실제로 어떻게 적는가? (q1-09 에서 파생) | 열림 | f8, 실행 2026-09-25-35 | | |
| q2-07 | AMR 제조사(MiR·OTTO·국내 물류로봇 업체 등)가 공개하는 매뉴얼·REST API 문서는 무엇이며, 공개되지 않을 때 표준 스키마(VDA 5050 팩트시트·MassRobotics)로 대신할 수 있는 정보와 없는 정보는 무엇인가? (q2-03 에서 파생) | 열림 | f20, 실행 2026-09-25-57 | | |

질문 문장 속 약어는 다음과 같다. AMR은 자율이동로봇(Autonomous Mobile Robot, AMR), API는 응용 프로그램 인터페이스(Application Programming Interface, API)이다. q2-02·q2-03은 실행 2026-09-25-57과 2026-10-09-22에서 부분 답을 낸 뒤, 실행 2026-10-09-23에서 q2-05와 함께 답함으로 처리했다. 세 질문 모두 신뢰도가 낮은 답이며, 한계는 3절의 각 소제목과 4절 남은 불확실성에 적었다. q2-07은 이번 실행의 AMR 샘플이 부분 근거가 되지만 이번에 고른 질문이 아니므로 열림 그대로 둔다.

## 3. 조사 결과

실행 2026-09-25-57은 q2-01에 답하고 q2-02·q2-03에 부분 답을 냈다. 실행 2026-10-09-22는 q2-04에 답하고(신뢰도 low), q2-02에 기계가독 형식 안의 단위 표기와 자유 텍스트 구분을 보강했으며, q2-03은 기존 출처를 다시 확인하는 데 그쳤다. 실행 2026-10-09-22는 새 검색 없이 공식 저장소·문서 원문(Open-RMF 튜토리얼과 플릿 어댑터 템플릿, VDA 5050 팩트시트 스키마, MassRobotics 스키마)과 기존 참고문헌만으로 이뤄졌다. 실행 2026-10-09-23은 q2-02·q2-03·q2-05에 답했다. 세 답은 모두 신뢰도가 낮다. q2-02의 형태별 난이도는 로봇 매뉴얼이 아니라 범용 문서 벤치마크와 산업 문서·데이터시트 연구에서 유추한 것이고, q2-03의 이용 조건은 저작권 표기·접근 조건의 관찰이며 법적 판단이 아니고, q2-05는 판·언어판 사이 실제 내용 차이를 문서끼리 대조하지 않았다. 제조사 문서는 문서 구조·정보 형태·이용 조건의 사례로만 인용하며, 문서에 적힌 내용은 독립 출처로 확인되기 전까지 벤더 주장이다.

### q2-01 제조사 문서 유형과 담긴 기능 정보 {#q2-01}

사용 정보의 구성은 두 표준이 정한다. ISO 20607:2019 는 기계 제조사가 설명서(instruction handbook)의 안전 관련 부분을 작성할 때의 요구사항을 정하며, 기계 수명주기 전 단계를 고려한 안전 관련 내용·구조·표현을 다루고 ISO 12100:2010 6.4.5 의 사용 정보 일반 요구를 구체화한다(2019 판 기준, 원문 미열람). [사실][^ref-509] IEC/IEEE 82079-1:2019 는 모든 종류 제품의 사용 정보(instructions for use) 작성 원칙과 요구사항을 정하는 2019 판 표준(2012 초판 대체)으로, 정보 품질·정보 관리 과정과 사용 정보의 실증적 평가 방법을 규범 부분에 둔다(2019 판 기준, 원문 미열람). [사실][^ref-510]

해외 제조사의 공개 문서는 다음과 같은 구조를 보인다. Boston Dynamics Spot SDK 공식 저장소 README 는 문서를 개념 설명, 파이썬 클라이언트 라이브러리(예제·빠른 시작), 페이로드 개발자 문서(기계·전기·소프트웨어 인터페이스), API 프로토콜 참조, 릴리스 노트, 라이선스로 나눈다(확인일 2026-09-25). [추정] 벤더 주장[^ref-505] Kinova Kortex API 공식 저장소 README 는 C++·Python API 메커니즘과 예제, Modbus 인터페이스, 언어별 오류 처리 문서, 펌웨어·API 판별 다운로드(Gen3 2.8.0, Gen3 lite 펌웨어 2.3.4·API 2.3.0)를 안내한다(확인일 2026-09-25). [추정] 벤더 주장[^ref-506] Kortex 문서 가운데 저수준 제어(서보 모드)를 다루는 부분은 분류 원문 19장 "로봇 자체 지능·제어" 경계의 연계 대상이므로, 이 위키에서는 문서 유형의 사례로만 보고 ROP 직접 범위로 다루지 않는다. [의견]

국내 협동로봇 제조사도 문서를 나눠 공개한다. 두산로보틱스는 로봇랩 포털에서 설치 매뉴얼(설치 방법·인터페이스·수동/자동 모드·안전 관련 기능)과 기타 매뉴얼(액세서리·퀵 가이드·ROS·API 사용 방법)을 제공한다(검색 결과 기준, 원문 미열람). [추정] 벤더 주장[^ref-511] 두산로보틱스 doosan-robot2 공식 저장소 README 는 튜토리얼 등 자세한 내용을 공식 ROS2 매뉴얼 포털로 안내하고, ROS2 Humble 에서 전 기종 지원을 밝힌다(확인일 2026-09-25). [추정] 벤더 주장[^ref-507] 레인보우로보틱스의 공식 클라이언트 라이브러리 rbpodo README 는 RB 시리즈 협동로봇용 C++17·Python 클라이언트로서 제어 박스와 5000번 포트로 명령·응답을, 5001번 포트로 상태 데이터를 주고받는다고 적고 개요·예제 문서를 링크한다(확인일 2026-09-25). [추정] 벤더 주장[^ref-508] 레인보우로보틱스는 협동로봇 기술자료 공개 페이지(rb_cobot_docs)도 두고 있다(원문 미열람). [추정] 벤더 주장[^ref-512]

이동로봇 쪽 사양서·데이터시트 정보에는 표준 스키마가 있다. VDA 5050 팩트시트 JSON 스키마(main, 3.0.0)는 유형 명세·물리 파라미터·프로토콜 한계·지원 기능·기하·적재 명세 블록(typeSpecification·physicalParameters·protocolLimits·protocolFeatures·mobileRobotGeometry·loadSpecification)을 기계가독 형식으로 둔다(확인일 2026-09-25). [사실][^ref-228] 이 팩트시트를 이동로봇 쪽 사양서·데이터시트 정보의 표준화된 대응물로 보는 것은 출처에 없는 이 위키의 해석이다. [추정][^ref-228]

위 사례를 문서 유형에 대응시키면 통합·API 가이드는 기능·인터페이스(명령·상태)·오류 처리를, 설치·안전 매뉴얼은 운전 모드·안전 제약을, 릴리스 노트는 판별 변경을, 페이로드·액세서리 문서는 장착 장비 인터페이스를, 사양서·데이터시트는 파라미터 범위를 주로 담는 것으로 보인다. 이 대응은 이 위키의 종합(추론)이며 측정 근거는 없다. [추정][^ref-505][^ref-506][^ref-511][^ref-509][^ref-228] 질문이 든 문서 유형 가운데 사용자 매뉴얼, 오류 코드표, 치수도·도면은 이번 샘플에서 확인하지 못했으며, [문서 유형 매트릭스](document-type-matrix.md)의 해당 행은 미조사로 남겼다.

### q2-02 기능 정보의 형태와 추출 난이도 {#q2-02}

기능 정보는 설정 파일·데이터 형식·코드 예제로도 존재한다. Open-RMF PerformAction 튜토리얼은 플릿이 수행할 수 있는 동작을 config.yaml 의 actions 목록으로 선언하고, 작업 요청을 JSON 으로, 동작 실행 논리를 파이썬 코드 예제로 보여 준다. [사실][^ref-040] Kinova Kortex 는 Google Protocol Buffers 문서를 참조하고 Spot SDK 는 API 프로토콜 참조를 두어, 두 제조사 모두 API 를 기계가독 프로토콜 정의와 코드 예제 형태로 제공하는 것으로 보인다(프로토콜 정의 파일 자체는 열지 않음). [추정] 벤더 주장[^ref-505][^ref-506]

**기계가독 형식 안의 단위 표기와 자유 텍스트(실행 2026-10-09-22 보강).** 기계가독 스키마도 단위를 적는 방식이 한 가지가 아니다. VDA 5050 팩트시트 JSON 스키마(main, 3.0.0)는 최대 적재 질량(maximumLoadMass, kg), 최대 속도(maximumSpeed, m/s), 최대 각속도(maximumAngularSpeed, rad/s) 같은 주요 수치 필드에 단위를 스키마 속성(unit)으로 단다. 다만 적재 치수(loadDimensions)의 길이·폭처럼 단위를 설명문에만 적는 필드도 있어, 모든 수치 필드가 단위 속성이나 최솟값 제약을 갖지는 않는다(확인일 2026-10-09). [사실][^ref-228] 같은 스키마는 시리즈 설명(seriesDescription), 동작 설명(actionDescription), 동작 결과(actionResult), 바퀴 제약(constraints)을 자유 텍스트 필드로 두고, 기구학 유형과 로봇 분류(mobileRobotClass)는 설명문에 값을 예시한 확장 가능한 열거값으로 둔다. 그래서 능력과 관련된 정보 일부가 기계가독 스키마 안에서도 문장으로 남는다(확인일 2026-10-09). [사실][^ref-228] 이 자유 텍스트 필드와 확장 열거값은 제조사마다 다른 문장·값을 담을 수 있으므로, 팩트시트를 받아도 동작의 완료 의미와 제약은 문장 해석을 거쳐야 능력 모델로 옮길 수 있을 것으로 보인다. 이는 이 위키의 추론이며 측정 근거는 없다. [추정][^ref-228]

MassRobotics AMR 상호운용 표준 스키마의 [신원 보고](../../glossary/identity-report.md)(identityReport)는 화물 최대 중량(cargoMaxWeight)을 설명에서 kg 단위로 밝히면서도 문자열형으로 정의하고, 화물 설명(cargoType)은 자유 문자열로, 제품 문서(productDocumentation)는 문서 내용이 아니라 URI 링크로 둔다(확인일 2026-10-09). [사실][^ref-230] Open-RMF 플릿 어댑터 템플릿의 config.yaml 은 수행 가능한 작업 유형(task_capabilities 의 loop·delivery 참거짓값), 동작 목록(actions), 배터리 전압·용량·충전 전류, 질량, 외형 반경을 YAML 값으로 선언하되, 배터리·기계 특성·외형 항목의 단위는 V·Ahr·A·kg·m 같은 줄 끝 주석으로만 적는다. 속도·가속도 한계(limits)에는 단위 없이 항목 이름만 주석으로 달려 있고, 템플릿의 값(tinyRobot 같은 로봇 이름, some_action_here 같은 동작 이름, 12.0 V 전압 등)은 실제 기종 값이 아니라 예시값이다(확인일 2026-10-09). [사실][^ref-105]

확인한 기계가독 형식 안에서도 단위가 스키마 속성으로 명시된 값(VDA 5050 팩트시트의 주요 수치 필드), 단위가 주석에만 있는 설정값(Open-RMF config.yaml), 수치를 문자열로 담은 값(MassRobotics 화물 최대 중량), 자유 텍스트(동작 결과·제약·화물 설명) 순으로 정규화에 드는 추가 해석이 늘 것으로 보인다. 이 순서는 값 형식을 대응시킨 이 위키의 추론이며, 형태별 추출 난이도를 측정한 자료는 이번에도 확인되지 않았다. [추정][^ref-228][^ref-105][^ref-230][^ref-513]

범용 문서 파싱 평가는 형태별로 나뉘어 있다. 문서 파싱과 추출 난이도는 [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md)가 다루는 방법의 문제다. OmniDocBench 공식 저장소 README 는 1,651개 PDF 페이지, 문서 유형 10종, 레이아웃 5종, 언어 5종으로 구성된 벤치마크에서 텍스트 문단·표·수식·읽기 순서를 나눠 정규화 편집 거리·TEDS 등으로 평가하며, 문서 유형으로 논문·연구 보고서(research report)·신문·교과서·손글씨 노트 등을 들고 매뉴얼은 명시하지 않는다(확인일 2026-09-25). [사실][^ref-513] 그래서 로봇 매뉴얼의 형태별(문장·표·그림·코드) 추출 난이도는 공개 측정 자료로 확인되지 않은 것으로 보인다. 이는 이번 조사 범위의 관찰이자 이 위키의 추론이며, 측정 자료의 부재가 확정된 것은 아니다. [추정][^ref-513][^ref-514]

매뉴얼을 대상으로 한 추출 연구는 있다. 현행 분류의 교차 규칙(L. AI·학습 기술의 주석)에서 매뉴얼 해석은 [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md)과 [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md)에 적용되는 연구 방법이며, 방법 자체는 [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md)가, AI가 해석한 결과를 실행에 쓰는 기준은 [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)이 다룬다. Springer 게재 장 "Conversational Knowledge Extraction from Technical Manuals"는 매뉴얼 전처리·색인, 온톨로지 제약을 건 검색 증강 생성(Retrieval-Augmented Generation, RAG) 기반 개체·관계 추출, 대화형 절차 안내를 결합한 대규모 언어 모델(LLM) 프레임워크를 제안했다(교육용 기술 매뉴얼 대상, 정확도 수치 미확인, 원문 미열람). [사실][^ref-514] ManuExtract 는 제조 분야 문서에서 항목–속성–값 삼중항을 추출하는 벤치마크 데이터셋으로, LLM 생성 주석을 도메인 전문가가 다듬어 구축했다(원문 미열람). [사실][^ref-515]

확인한 사례로 보면 기능 정보의 형태는 기계가독 스키마·설정(VDA 5050 팩트시트, Open-RMF config.yaml, 프로토콜 정의) → 파라미터 표 → 문장 → 그림·다이어그램 순으로 구조화 추출이 쉬워질 것으로 보인다. 이 순서는 형태별 구조 정도에서 도출한 이 위키의 추론이며 측정 근거는 없으므로 측정 결과로 읽지 않는다. [추정][^ref-228][^ref-040][^ref-513][^ref-514]

**근거 형태별 측정 자료(실행 2026-10-09-23).** 이번 실행에서 찾은 측정 자료는 범용 문서 벤치마크와 산업 문서·데이터시트 연구이며, 로봇 매뉴얼을 대상으로 한 것은 아니다. MMLongBench-Doc(NeurIPS 2024 Datasets and Benchmarks)은 지침·튜토리얼을 포함한 7개 유형의 긴 PDF 135건에 대해 질문마다 근거 형태(텍스트·레이아웃·차트·표·이미지)를 표시하고, GPT-4o 의 근거 형태별 정확도를 텍스트 46.3, 레이아웃 46.0, 차트 45.3, 표 50.0, 이미지 44.1로 보고했다(2024-07 판 기준, 로봇 매뉴얼은 대상에 명시되지 않음). [사실][^ref-1387] 같은 벤치마크에서 공개 시각-언어 모델은 차트·이미지 근거 질문에서 더 낮았고(InternVL-Chat-v1.5 차트 7.1 대 텍스트 14.0), 광학 문자 인식(Optical Character Recognition, OCR)으로 파싱한 텍스트를 받은 텍스트 전용 모델(Mixtral 8x22B)도 텍스트 34.2 대 차트 19.5·이미지 19.2로 낮아져, 저자들은 이를 OCR 이 차트·이미지를 읽지 못하는 한계로 설명했다. [사실][^ref-1387]

Riedler·Langer(2024-10-29)는 산업 문서 대상 검색 증강 생성에서 이미지 검색이 텍스트 검색보다 어렵고, 이미지를 다중 모달 임베딩으로 다루는 것보다 텍스트 요약으로 바꾸는 쪽이 더 유망하다고 보고했다(초록 열람, 사용한 산업 문서 이름 미확인). [사실][^ref-1388] Xia 외(IEEE Access, 2024)는 기술 자산 데이터시트의 텍스트에서 LLM 에이전트로 자산관리셸 모델을 생성해, 원문 정보가 오류 없이 옮겨진 비율(유효 생성률)을 62~79%로 보고했다(초록 열람, 표·그림 형태별 결과 없음). [사실][^ref-1072] Groß·Heidrich(arXiv 2609.07334, 2026-09-07)는 비슷한 자산관리셸 인스턴스에서 찾은 추출 예시로 맞춤 예시를 만드는 방식(AAS-RAIL)이 PDF 제품 데이터시트 추출에서 일반 소수 예시 프롬프트보다 30.4~52.4% 상대 개선을 보였다고 보고하며, 이를 회사별 명명·서식 차이에 맞추는 방법으로 제시했다(초록 열람). [사실][^ref-1071] Singh 외(arXiv 2511.11847, v1 2025-11-14 제출·v2 2026-02-10 개정, 초록 기준)는 Universal Robots UR5e 협동로봇을 포함한 기계 3종의 운전·안전 매뉴얼로 질의응답 벤치마크를 만들어 검색 증강 생성 구성 24가지를 비교했고, 배포용으로 고른 구성의 정확도를 86.66%로 보고했으나 초록에는 표·그림·텍스트 근거별 결과가 없다. [사실][^ref-1390]

제조사 웹 매뉴얼의 형태 사례도 있다. 두산로보틱스 한국어 웹 매뉴얼(3.2.1)은 M1013 사양을 '구분 / 항목 / 사양 정보' 세 열의 웹 페이지 표로 두고 가반 하중·최대 반경·관절 범위와 속도·반복 정밀도·IP 등급·사용 환경을 단위와 함께 적으며, 그 페이지에 작업 영역 그림은 없다(확인일 2026-10-09). [추정] 벤더 주장[^ref-1385] Universal Robots 사용자 매뉴얼 안내 페이지는 로봇 사용자 매뉴얼과 별도로 오류 코드, 스크립트 명세, 소프트웨어 핸드북을 메뉴로 두어, 오류 의미와 명령 인터페이스 정보가 사용자 매뉴얼 밖의 별도 문서에 있음을 보여 준다(각 문서의 내부 형태는 미확인, 확인일 2026-10-09). [추정] 벤더 주장[^ref-1377]

확인한 측정 자료를 종합하면, MMLongBench-Doc 에서 GPT-4o 는 근거 형태 사이 정확도가 44~50으로 고르고 표(50.0)가 가장 높으며, 차트·이미지 근거의 정확도 저하는 공개 시각-언어 모델과 OCR 파이프라인에서 큰 것으로 보인다. [추정][^ref-1387][^ref-1388] 이 자료들은 범용 문서 벤치마크와 산업 문서·데이터시트 연구이고 로봇 매뉴얼을 포함하지 않으며, 질문이 든 형태 가운데 코드 예제는 측정 자료에 없다. 기술 매뉴얼 질의응답 연구는 형태별이 아니라 전체 정확도만 보고하므로, 로봇 매뉴얼의 형태별 추출 난이도는 범용 자료로 유추할 수 있을 뿐 직접 측정된 것은 아닌 것으로 보인다(이 위키의 종합, 부재 확정 아님). [추정][^ref-1387][^ref-1390][^ref-1072] 그래서 이 질문은 답함으로 처리했지만, 답은 유추에 기대는 신뢰도 낮은 답이다.

남은 부분은 로봇 매뉴얼(사양 표·오류 코드표·작업 영역 도면·코드 예제)을 대상으로 근거 형태별 추출 정확도를 재는 평가 세트다. 이 물음은 로봇 문서 파싱 결과를 묻는 [단계 3. 비정형 문서에서 온톨로지를 추출하는 방법 조사](stage-3-extraction-methods.md)의 q3-01, 기준 정답 구축을 묻는 [단계 5. 완전성과 정확성을 검증하는 방법 조사](stage-5-completeness-verification.md)의 q5-01, 로봇 매뉴얼 대상 추출 정확도 벤치마크를 묻는 [열린 질문](../../open-questions.md) oq-226 과 함께 본다. 기계가독 스키마 안에 남은 자유 텍스트 필드를 능력 온톨로지의 완료 확인·제약으로 옮기는 추출·검토 방법은 q3-09로 같은 단계 3에 있다.

### q2-03 공개 문서 샘플과 이용 조건 {#q2-03}

실행 2026-09-25-57에서 확인한 공개 문서 샘플은 로봇팔·협동로봇(Kinova, 두산로보틱스, 레인보우로보틱스)과 4족 보행 로봇(Spot)이고, 실행 2026-10-09-23에서 AMR(MiR, Clearpath)과 협동로봇(Universal Robots, 두산로보틱스 웹 매뉴얼), OMRON 로보틱스 다운로드 센터를 더했다. 목록은 [문서 유형 매트릭스](document-type-matrix.md)의 4절에 있다.

이용 조건은 샘플마다 다르다. Spot SDK 는 GitHub 에 공개되어 있으나 사용·복제·배포가 Boston Dynamics SDK 라이선스(20191101-BDSDK-SL) 조건을 따른다. [추정] 벤더 주장[^ref-505] Kinova Kortex API 저장소는 BSD 3-Clause 라이선스로 공개되어 있다. [추정] 벤더 주장[^ref-506] 국내 협동로봇 제조사의 공개 저장소(두산 doosan-robot2: Apache 2.0·BSD 3-Clause, 레인보우 rbpodo: Apache 2.0)는 코드에 개방 라이선스를 달지만, 포털에서 내려받는 매뉴얼 문서 자체의 이용 조건은 이번에 확인하지 못했다. [추정] 벤더 주장[^ref-507][^ref-508][^ref-511]

실행 2026-10-09-22는 위 출처를 다시 인용했을 뿐 새 샘플을 더하지 않았다. 표준 스키마 쪽에서는 MassRobotics 신원 보고의 제품 문서 필드가 문서 내용이 아니라 링크(URI)만 담는다. [사실][^ref-230] 그래서 신원 보고를 받아도 매뉴얼 내용은 링크를 따라가 따로 확보해야 하는 것으로 보인다. [추정][^ref-230]

**AMR 샘플과 접근 조건(실행 2026-10-09-23).** MiR 의 제품 문서 페이지(MiR250 HW 2.0 SW 2.x, MiR1350 Pallet Lift HW 1.0 SW 2.x)는 사용자 가이드·빠른 시작·적합성 문서는 로그인 표시 없이 내려받게 하지만 인터페이스·시운전·기술·위험성평가·사이버보안 가이드와 버전별 REST API 참조는 MiR 지원 포털 로그인을 요구하고, 문서 이용 조건은 페이지에 적지 않는다(확인일 2026-10-09). [추정] 벤더 주장[^ref-1375][^ref-1376] Clearpath Robotics 의 IndoorNav 사용자 매뉴얼(OTTO Motors 실내 자율주행 소프트웨어 기반)은 로그인 없이 열리는 웹 문서로 'All rights reserved' 를 표기하고, 전체 ROS 2 API 문서는 설치 패키지(clearpath-api) 안에 있거나 OTTO Motors 계정이 필요한 docs.ottomotors.com 에 둔다(마지막 갱신 2025-07-18). [추정] 벤더 주장[^ref-1379][^ref-1380] IndoorNav·OutdoorNav 의 자율주행 API 는 분류 원문 19장 "로봇 자체 지능·제어" 경계의 연계 대상인 제조사 쪽 기능이므로, 이 위키에서는 문서 접근 조건과 판 관리의 사례로만 쓴다. [의견] OMRON 로보틱스 다운로드 센터는 자료 접근에 양식 제출을 요구하며, 제출 즉시 접근을 안내하면서도 검토 중·거절 상태 메시지를 둔다(확인일 2026-10-09). [추정] 벤더 주장[^ref-1382]

**협동로봇 문서의 재사용 표기(실행 2026-10-09-23).** Universal Robots 매뉴얼의 저작권 고지는 내용을 Universal Robots A/S 의 사전 서면 승인 없이 전체든 일부든 복제하지 못하게 하고, 내용이 예고 없이 바뀔 수 있다고 적는다(확인일 2026-10-09). [추정] 벤더 주장[^ref-1378] 두산로보틱스 웹 매뉴얼은 로그인 없이 열리며 매뉴얼 PDF 내려받기·ROS 2 문서·API 문서 링크를 두지만, 하단에는 'Copyright Doosan Robotics Inc.' 표기와 개인정보 처리방침 링크만 있고 별도의 이용 조건이나 재사용 허락 문구는 없다(PDF 내려받기 포털의 로그인 여부는 미확인, 확인일 2026-10-09). [추정] 벤더 주장[^ref-1384]

확인한 샘플을 종합하면, AMR 쪽에도 공개 문서 샘플(MiR 사용자 가이드, Clearpath IndoorNav·OutdoorNav 웹 매뉴얼)이 있지만 MiR·Clearpath 는 통합 수준 문서(REST API 참조·인터페이스·시운전 가이드·전체 API)를 계정·로그인 뒤에 두는 경향이 있는 것으로 보인다. 다만 두산로보틱스는 ROS 2·API 문서를 로그인 없이 공개하므로 예외가 있다. 공개 문서도 '모든 권리 보유'나 서면 승인 없는 복제 금지를 표기한다. 이 판단은 제조사 5곳 샘플의 관찰을 종합한 것이며 법적 판단이 아니다. [추정][^ref-1375][^ref-1379][^ref-1380][^ref-1382][^ref-1378][^ref-1384] 이 표기들이 매뉴얼을 자동 추출·재가공해 능력 온톨로지에 쓰는 데 어떤 허락을 요구하는지는 q2-03의 답으로 정하지 않고, 같은 물음을 다루는 백로그 q6-07([단계 6. 변경 관리·운영·거버넌스 조사](stage-6-lifecycle-governance.md))의 부분 근거로 넘긴다. 이번 AMR 샘플은 이번 실행이 고르지 않은 q2-07(AMR 공개 문서)의 부분 근거이기도 하지만, q2-07의 상태는 바꾸지 않는다.

### q2-04 문서에 없지만 실행에 필요한 정보와 보완 경로 {#q2-04}

이 답의 근거는 로봇 제조사 매뉴얼이 아니라 Open-RMF 통합 문서·플릿 어댑터 템플릿과 표준 스키마(VDA 5050 팩트시트, MassRobotics)다. 그래서 아래 항목이 "제조사 문서에 없다"는 판단은 이 위키의 추론이며, 질문이 든 보완 경로 가운데 제조사 문의와 커뮤니티는 이번에 근거 출처가 없어 미확인이다. 정보 항목별 요약은 [문서 유형 매트릭스](document-type-matrix.md)의 5절에 있다.

**통합자가 채우는 동작 연결 코드.** Open-RMF PerformAction 튜토리얼에서 사용자 정의 동작([수행 가능 동작](../../glossary/performable-action.md), Performable Action)은 config.yaml 의 actions 에 이름만 선언된다. 그 동작을 로봇 API 호출로 옮기는 start_activity 는 로봇과 사용 사례마다 달라 통합자가 RobotClientAPI 에 직접 구현해야 하며, 플릿 관리자가 모르는 동작이면 활동을 바로 끝낸다(확인일 2026-10-09). [사실][^ref-040] 같은 튜토리얼에서 RMF 는 사용자 정의 동작이 진행되는 동안 로봇 제어권을 내려놓는다. 튜토리얼 예시에서는 어댑터의 갱신 루프가 is_command_completed 로 로봇 API 의 완료를 확인한 뒤 execution.finished() 를 호출해 완료를 알리며, 별도 콜백으로 완료를 표시할 수도 있다. [사실][^ref-040]

**통합자가 채우는 현장 설정.** Open-RMF 플릿 어댑터 템플릿의 config.yaml 은 로봇별 충전기 이름, 운용 하한·충전 목표 배터리 수준(recharge_threshold·recharge_soc), 질량·관성 모멘트·마찰 계수, 대기·도구 소비 전력, 제조사 관제 접속 주소·계정 항목을 두며, 층별 RMF 좌표와 로봇 좌표의 대응점 네 쌍(reference_coordinates)은 선택 항목이다(값은 템플릿 예시값, 확인일 2026-10-09). [사실][^ref-105] 좌표 대응점·충전기 배정 같은 현장 설정과 동작–로봇 API 매핑·완료 확인 코드는 현장과 통합 방식에 따라 정해지므로 제조사 문서에서 가져올 수 없고, 통합자가 [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md) 단계의 측정·시험과 어댑터 구현으로 보완하는 암묵지에 해당하는 것으로 보인다. [추정][^ref-105][^ref-040]

충전 하한은 이와 다르게 두 값이 함께 있을 수 있다. VDA 5050 main(3.0.0) 팩트시트 스키마는 구성 블록의 충전 설정(batteryCharging)에 제조사가 선언하는 임계 저충전 수준(criticalLowChargingLevel)을 둔다. [사실][^ref-228] 반면 위 템플릿은 운영 설정으로 recharge_threshold 를 둔다. [사실][^ref-105] 두 값 가운데 무엇을 충전 하한의 기준으로 삼고 둘이 다르면 어떻게 조정할지는 [열린 질문](../../open-questions.md) oq-068 로 남아 있다.

**운용 중에 드러나는 값.** VDA 5050 팩트시트 스키마는 팩트시트를 특정 이동로봇 유형 시리즈의 기본 정보로 규정하고, 그 쓰임으로 유형 비교, 시스템 계획·규모 산정·시뮬레이션, VDA 5050 플릿 관제 통합을 든다(확인일 2026-10-09). [사실][^ref-228] MassRobotics 스키마의 상태 보고(statusReport)는 배터리 비율, 남은 가동 시간, 남은 적재 여유 비율, 오류 코드(자유 문자열 배열)를 선택 필드로 둔다(필수는 uuid·timestamp·operationalState·location). [사실][^ref-230] Naqvi 외(2025)는 제조사가 광고한 능력과 운용 중 관측된 능력을 온톨로지로 구분해 통합하는 방법을 제시했다. [사실][^ref-041] 팩트시트가 유형 시리즈 수준의 선언이고 남은 가동 시간·적재 여유 같은 값이 상태 보고로 드러나므로, 개체별 실제 성능 저하 같은 암묵지는 문서보다 운용 중 상태 보고와 관측 능력 기록으로 보완하는 것으로 보인다. [추정][^ref-228][^ref-230][^ref-041] 이 값들은 [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md)이 다루는 현재 상태 표현으로 보고, 34. 시뮬레이션·예측용 디지털 트윈의 미래 실험과 섞지 않는다.

상태 보고의 오류 코드는 자유 문자열로만 보고되므로, 그 뜻을 설명하는 것은 상태 보고가 아니라 오류 코드표 문서 유형의 몫으로 보인다. [추정][^ref-230] 오류 코드표 행은 [문서 유형 매트릭스](document-type-matrix.md)에서 아직 미조사다. 통합자가 구현한 동작–API 매핑과 완료 확인 코드를 능력 온톨로지의 근거 문서로 기록하고 제조사 문서 선언과 구분해 관리하는 방법은 새 질문 q4-17로 [단계 4. 온톨로지를 실행에 연결하는 방법 조사](stage-4-execution-grounding.md)에 보냈다.

### q2-05 언어·문서 판·옵션 장비에 따른 정보 차이 {#q2-05}

이 답은 설명서의 원본·번역 규정 1건과 제조사 문서 포털의 판·언어·구성 관리 사례(벤더 주장)에 기대며, 같은 기종의 판·언어판 사이 실제 내용(사양 값) 차이는 문서끼리 대조하지 않았다. 차이는 언어판, 소프트웨어·문서 판, 하드웨어·상위 모듈·옵션 구성의 세 축으로 나타난다.

**언어판.** EU 기계류 지침 2006/42/EC 부속서 I 1.7.4.1 은 설명서를 하나 이상의 공식 공동체 언어로 쓰게 하고, 제조자 또는 그 대리인이 확인한 언어판에 'Original instructions' 를, 사용국 언어로 옮긴 판에 'Translation of the original instructions' 를 표기하게 한다(2006-05-17 지침, legislation.gov.uk 게재본으로 확인, EUR-Lex 원문 미열람). [사실][^ref-1386] 이 지침은 규정 (EU) 2023/1230 으로 대체될 예정이며 새 규정의 설명서 조항은 열지 못했다. MiR250 제품 문서 페이지는 문서마다 제공 언어가 달라 사용자 가이드는 10개, 빠른 시작은 16개, 인터페이스 가이드는 5개 언어이고 기술·위험성평가·사이버보안 가이드는 영어로만 제공하며, 사용자 가이드에는 한국어판이 있다(확인일 2026-10-09). [추정] 벤더 주장[^ref-1375] 같은 페이지에서 사용자 가이드·빠른 시작은 모든 언어에 판 2.1 로 표시되지만 포르투갈어 링크는 1.4·1.5 판 이름의 경로를 가리켜, 언어판 사이에 판이 어긋날 수 있는 것으로 보인다(파일을 내려받아 대조하지 않은 링크 경로 관찰). [추정] 벤더 주장[^ref-1375]

두산로보틱스 웹 매뉴얼은 판 선택(3.2.0~3.7.0), 한국어를 포함한 13개 언어, 제품군 메뉴(M/H·A·E·P 시리즈)를 두고, V2 판 매뉴얼은 별도의 레거시 사이트(v2-manual)로 분리한다(확인일 2026-10-09). [추정] 벤더 주장[^ref-1384] Universal Robots 는 모델별(UR Series·e-Series) 매뉴얼을 나열하고 시리즈마다 두 소프트웨어 계열(PolyScope 5·PolyScope X)을 쓸 수 있다고 적으며, 매뉴얼 주소에 소프트웨어 판(SW5_26·SW10_13)과 언어가 들어 있다(확인일 2026-10-09). [추정] 벤더 주장[^ref-1377][^ref-1378] 언어판 차이가 추출에 주는 영향을 잰 연구도 있다. Agri-Query(Gun·Oksanen, 2025)는 배치가 같은 165쪽 농기계 매뉴얼의 영어·프랑스어·독일어 공식판에 영어로 질문했을 때 키워드 검색 RAG 정확도가 크게 떨어졌고(Gemini 2.5 Flash 0.852 → 0.583·0.528), 혼합 검색 RAG 는 하락이 작았다(0.880·0.824·0.870)고 보고했으며, 표·그림 해석은 평가하지 않았다(v2 본문 기준, 초록의 '모든 언어 85% 이상'은 표와 일부 불일치). [사실][^ref-1389]

**소프트웨어·문서 판.** Boston Dynamics Spot SDK 릴리스 노트는 판마다 Breaking Changes·New Features·Deprecations 절을 두고(모든 판에 세 절이 다 있지는 않음), 판에 따라 기능이 더해지거나(4.1.0 의 계단 사용 금지 STAIRS_MODE_PROHIBITED) 필드가 폐기되며(5.0.0 SystemFault uid), 일부 예제는 로봇이 5.1.0 이상을 실행해야 한다고 적는다(확인일 2026-10-09). [추정] 벤더 주장[^ref-1383] Clearpath OutdoorNav 매뉴얼은 판 선택(0.7.0~2.3.0과 Legacy)을 두고 1.0.0 판을 '더 이상 유지되지 않음'으로 표시하며 그 판의 API 를 ROS 1 Noetic 기준으로 설명하고, IndoorNav API 문서 경로에도 판(ros2-api-1.3.3)이 들어 있다(확인일 2026-10-09). [추정] 벤더 주장[^ref-1381][^ref-1380] 계단 사용 금지 같은 주행 동작과 자율주행 API 는 분류 원문 19장 "로봇 자체 지능·제어" 경계의 연계 대상이며, 여기서는 판에 따라 문서에 드러나는 기능이 달라진다는 사례로만 쓴다. [의견]

**하드웨어·상위 모듈·옵션 구성.** MiR250 제품 문서 페이지는 로봇 하드웨어 2.0·소프트웨어 2.x·SICK 설정 파일 판 단위로 문서를 묶고, MiR1350 Pallet Lift 문서 페이지는 로봇 하드웨어 1.0 과 별도로 상위 모듈 하드웨어 1.0·소프트웨어 2.x·SICK 설정 파일 판을 적어, 상위 모듈(옵션 장비)을 단 구성이 자체 문서 묶음과 판을 갖는다(확인일 2026-10-09). [추정] 벤더 주장[^ref-1375][^ref-1376] VDA 5050 팩트시트 스키마(main, 3.0.0)는 팩트시트를 이동로봇 유형 시리즈의 기본 정보로 설명하면서도 serialNumber 를 필수로 두고, 구성 블록(mobileRobotConfiguration)에 하드웨어·소프트웨어 판의 키-값 배열(versions)을 두며, 적재 취급 장치 목록(loadPositions)이 없거나 비면 적재 취급 장치가 없는 것으로 정한다(공식 저장소 원문 확인, 확인일 2026-10-09). [사실][^ref-228]

확인한 사례를 종합하면 같은 기종의 정보는 (가) 언어판(원본과 번역, 문서 유형별로 다른 언어 범위, 판이 어긋날 수 있는 번역판), (나) 소프트웨어·문서 판(판별 기능 추가·폐기, 유지 중단된 판), (다) 하드웨어·상위 모듈·옵션 구성(별도 문서 묶음, 적재 취급 장치 유무)에 따라 달라지므로, 근거 문서에는 언어·원본 여부와 적용 하드웨어·소프트웨어·모듈 판을 함께 기록해야 할 것으로 보인다. 이는 이 위키의 종합이며, (가)의 판 어긋남은 링크 경로 관찰에, (다)의 적재 취급 장치 유무는 표준 스키마 규정에 기대고, 판·언어판 사이 실제 내용 차이는 대조하지 않았다. [추정][^ref-1386][^ref-1375][^ref-1376][^ref-1384][^ref-1377][^ref-1383][^ref-1381][^ref-228] 이 가운데 근거 문서의 언어(원본 / 번역 구분)는 [능력 온톨로지 초안](ontology-draft.md) v0.5에 반영했고, 적용 구성은 초안 6절의 "근거 문서의 단위와 버전"·로봇 구성 버전(q6-02) 질문에 합쳤다. 언어판 사이 판이 어긋날 때 추출 근거로 어느 언어판을 고르고 차이를 어떻게 검출할지는 새 질문 q3-10으로 [단계 3. 비정형 문서에서 온톨로지를 추출하는 방법 조사](stage-3-extraction-methods.md)에 보냈다. 국내 설명서의 한국어 제공 규정은 [열린 질문](../../open-questions.md)으로 올렸다.

## 4. 결론과 남은 불확실성

**결론**

- 사용 정보의 작성은 ISO 20607:2019(설명서의 안전 관련 부분)와 IEC/IEEE 82079-1:2019(모든 종류 제품의 사용 정보)가 정한다. [사실][^ref-509][^ref-510]
- 공개 샘플에서 통합·API 가이드, 설치 매뉴얼, 릴리스 노트, 페이로드·액세서리 문서의 구조를 확인했고, 문서 유형별로 담긴 정보의 대응은 이 위키의 종합(추론)이다. [추정][^ref-505][^ref-506][^ref-511][^ref-228]
- 기능 정보는 문장·표뿐 아니라 설정 파일·JSON·코드 예제 형태로도 존재한다. [사실][^ref-040]
- 기계가독 형식 안에서도 단위를 스키마 속성으로 다는 값, 주석으로만 적는 값, 문자열로 담는 값이 섞여 있고, 동작 결과·제약·화물 설명은 자유 텍스트로 남는다. [사실][^ref-228][^ref-105][^ref-230]
- 범용 문서 파싱 벤치마크 OmniDocBench 는 문서 유형에 매뉴얼을 두지 않는다. [사실][^ref-513]
- 로봇 매뉴얼을 포함하지 않는 범용 문서 벤치마크 MMLongBench-Doc 에서 GPT-4o 의 근거 형태별 정확도는 44.1~50.0으로 비교적 고르고 표(50.0)가 가장 높았으며, 공개 시각-언어 모델과 OCR 텍스트를 받은 텍스트 전용 모델은 차트·이미지 근거에서 더 낮았다. [사실][^ref-1387]
- 공개 저장소의 코드는 개방 라이선스나 제조사 SDK 라이선스를 달지만, 포털 매뉴얼의 이용 조건은 확인되지 않았다. [추정] 벤더 주장[^ref-505][^ref-507][^ref-508][^ref-511]
- AMR 제조사도 사용자 가이드·웹 매뉴얼을 공개하지만 MiR·Clearpath 는 통합 수준 문서를 로그인·계정 뒤에 두고, 공개 문서는 저작권 표기나 서면 승인 없는 복제 금지를 단다. 두산로보틱스의 ROS 2·API 문서 공개는 예외다. [추정] 벤더 주장[^ref-1375][^ref-1379][^ref-1380][^ref-1378][^ref-1384]
- EU 기계류 지침은 제조자 또는 그 대리인이 확인한 언어판에 'Original instructions' 를, 옮긴 판에 'Translation of the original instructions' 를 표기하게 한다. [사실][^ref-1386]
- VDA 5050 팩트시트 스키마(main, 3.0.0)의 구성 블록은 하드웨어·소프트웨어 판의 키-값 배열(versions)을 둔다. [사실][^ref-228] 실행 2026-10-09-22에서 미확인으로 남긴 팩트시트 뒷부분(구성 블록의 versions·batteryCharging, 적재 명세의 loadPositions)은 이번 실행에서 공식 저장소 원문을 열어 확인했다.
- 같은 기종의 정보가 언어판, 소프트웨어·문서 판, 하드웨어·상위 모듈·옵션 구성에 따라 달라지므로 근거 문서에 언어·원본 여부와 적용 판을 함께 기록해야 할 것으로 보인다는 판단은 이 위키의 종합이다. [추정][^ref-1386][^ref-1375][^ref-1376][^ref-228]
- Open-RMF 통합에서 사용자 정의 동작의 로봇 API 매핑·완료 확인 코드와 좌표 대응점·충전기 배정 같은 현장 설정은 통합자가 채운다. [사실][^ref-040][^ref-105] 이것이 제조사 문서 밖의 암묵지로서 시운전과 운용 중 상태 보고·관측 능력 기록으로 보완된다는 판단은 이 위키의 추론이다. [추정][^ref-105][^ref-040][^ref-230][^ref-041]

**남은 불확실성**

- 사용자 매뉴얼, 오류 코드표, 치수도·도면 유형은 매트릭스 행으로는 아직 조사하지 않았다. Universal Robots 가 오류 코드를 별도 문서로 둔다는 것만 확인했고 그 내부 형태와 오류 코드의 뜻을 설명하는 방식은 미확인이다.
- q2-02 는 답함으로 처리했으나 신뢰도가 낮다. 측정 자료는 범용 문서 벤치마크(로봇 매뉴얼 미포함)와 산업 문서·데이터시트 연구이고, 질문이 든 형태 가운데 코드 예제는 측정 자료에 없다. 로봇 매뉴얼을 대상으로 한 근거 형태별 추출 정확도는 찾지 못했다(부재 확정 아님). Riedler·Langer, Singh 외, Xia 외, Groß·Heidrich 는 초록만 열람했다.
- q2-03 은 답함으로 처리했으나 신뢰도가 낮다. 이용 조건은 저작권 표기·접근 조건의 관찰이며 법적 판단이 아니다. 국내 AMR 제조사의 공개 매뉴얼·API 문서는 한국어 검색에서 찾지 못했다(부재 확정 아님). OMRON 하단 이용 약관이 다운로드에 적용되는지, 두산로보틱스 PDF 내려받기 포털의 로그인 여부는 미확인이다.
- q2-05 는 답함으로 처리했으나 신뢰도가 낮다. 판·언어판 사이 실제 내용(사양 값) 차이는 문서끼리 대조하지 않았고, MiR250 포르투갈어판의 판 불일치는 링크 경로 관찰이다. EU 기계류 지침은 legislation.gov.uk 게재본으로 확인했으며 EUR-Lex 원문과 대체 규정 (EU) 2023/1230 의 설명서 조항은 미열람이다. 국내 설명서 언어 규정은 확인하지 못해 열린 질문으로 올렸다.
- q2-04 는 답함으로 처리했으나 신뢰도가 낮다. 근거가 로봇 제조사 매뉴얼이 아니라 Open-RMF 통합 문서·템플릿과 표준 스키마이고, "문서에 없다"는 판단과 보완 경로는 이 위키의 추론이며, 질문이 든 보완 경로 가운데 제조사 문의·커뮤니티는 근거 출처가 없어 미확인이다.
- 충전 하한은 제조사 팩트시트 선언값(criticalLowChargingLevel)과 운영 설정값(recharge_threshold)이 함께 있을 수 있으며, 어느 쪽을 기준으로 삼을지는 열린 질문 oq-068 이다.
- 원문 미열람 출처: ISO 20607, IEC/IEEE 82079-1, 두산로보틱스 로봇랩 매뉴얼 게시판, rb_cobot_docs, Springer 게재 장 두 건, Naqvi 외(2025). Springer 게재 장 두 건은 저자·발행일도 미확인이다.
- 제조사 문서 근거는 모두 벤더 주장이며, 실행 2026-09-25-57·2026-10-09-22·2026-10-09-23의 발견 사항은 교차 확인되지 않았다.
- 온톨로지: 실행 2026-09-25-57에서 [능력 온톨로지 초안](ontology-draft.md)을 v0.3 → v0.4로 올려 근거 문서에 속성 "문서 유형"·"이용 조건"을 더하고 근거 문서를 확정했다. 속성 "정보 형태"는 반영하지 않고 초안 6절 "근거 문서의 단위와 버전" 질문에 합쳤다. 실행 2026-10-09-22는 변경 제안이 없어 v0.4를 유지했다. 실행 2026-10-09-23은 v0.4 → v0.5로 올려 근거 문서에 속성 "언어(원본 / 번역 구분)"를 더했다. 함께 제안된 속성 "적용 구성(하드웨어·소프트웨어 판, 상위 모듈·옵션 장비)"은 문서 적용 구성과 로봇 구성 버전의 대응이 단계 6 질문(q6-02)의 몫이라 반영하지 않고 초안 6절 질문에 합쳤다.

## 5. 이 단계가 낳은 후속 질문

| 새 질문 id | 질문 | 보낼 단계 | 근거 finding id | 상태 |
|---|---|---|---|---|
| q2-07 | AMR 제조사(MiR·OTTO·국내 물류로봇 업체 등)가 공개하는 매뉴얼·REST API 문서는 무엇이며, 공개되지 않을 때 표준 스키마(VDA 5050 팩트시트·MassRobotics)로 대신할 수 있는 정보와 없는 정보는 무엇인가? (q2-03 에서 파생) | 단계 2. 로봇 문서 유형과 정보 구조 조사 | f20 (실행 2026-09-25-57) | 열림 |
| q6-07 | SDK 코드 라이선스와 별개로 제조사 매뉴얼 문서를 자동 추출·재가공해 능력 온톨로지에 쓰는 것이 이용 조건상 허용되는가, 이를 누가 확인하고 기록하는가? (q2-03 에서 파생) | 단계 6. 변경 관리·운영·거버넌스 조사 | f19 (실행 2026-09-25-57) | 열림 |
| q3-09 | VDA 5050 팩트시트의 동작 결과(actionResult)·제약(constraints)·동작 설명처럼 기계가독 스키마 안에 남은 자유 텍스트 필드를 능력 온톨로지의 완료 확인·제약으로 옮길 때 어떤 추출·검토 방법을 쓰는가? (q2-02 에서 파생) | 단계 3. 비정형 문서에서 온톨로지를 추출하는 방법 조사 | f2 (실행 2026-10-09-22) | 열림 |
| q4-17 | 통합자가 플릿 어댑터에 구현한 동작–로봇 API 매핑과 완료 확인 코드를 능력 온톨로지의 근거 문서로 기록하고, 제조사 문서 선언과 어떻게 구분해 관리하는가? (q2-04 에서 파생) | 단계 4. 온톨로지를 실행에 연결하는 방법 조사 | f12 (실행 2026-10-09-22) | 열림 |
| q3-10 | 제조사 매뉴얼의 언어판 사이에 판 번호·내용이 어긋날 때(번역판이 원본보다 오래된 판인 경우) 능력 정의 초안의 추출 근거로 어느 언어판을 고르고, 언어판 사이 차이를 어떻게 검출하는가? (q2-05 에서 파생) | 단계 3. 비정형 문서에서 온톨로지를 추출하는 방법 조사 | f19 (실행 2026-10-09-23) | 열림 |

형태별 추출 정확도 측정 데이터셋·평가 방법을 묻는 후속 질문은 q2-02·q3-01과 중복되어 새로 등록하지 않았다. 실행 2026-10-09-23에서 제안된 로봇 매뉴얼 근거 형태별 평가 세트 질문(단계 5)도 q2-02·q3-01·q5-01·oq-226과 뜻이 같아 등록하지 않고 3절 q2-02의 남은 부분으로 연결했다. q2-04의 보완 경로 가운데 근거가 없는 제조사 문의·커뮤니티는 4절 남은 불확실성에 두었다.

## 6. 완료 조건 충족 현황

완료 조건은 트랙 정의의 문장을 옮기되 파일명은 페이지 링크로 바꾸고, 조건이 여러 항목이면 행을 나눴다. 충족 여부는 리서치 에이전트의 자체 평가를 스토리텔러 에이전트가 옮겨 적은 값이고, 검증 판정 칸은 내용 검증 에이전트의 1차 판정이다. 둘이 다르면 검증 판정을 따른다.

> 완료 조건: 문서 유형 × 정보 항목 매트릭스(`document-type-matrix.md`), 공개 문서 샘플 목록.

| 완료 조건 | 충족 여부 | 근거 | 검증 판정 |
|---|---|---|---|
| 문서 유형 × 정보 항목 매트릭스([document-type-matrix.md](document-type-matrix.md)) | 미충족 | [문서 유형 매트릭스](document-type-matrix.md) 64칸 가운데 9칸을 채웠다(통합·API 가이드, 안전 매뉴얼, 릴리스 노트, 사양서·데이터시트, 페이로드·액세서리 문서 행의 일부). 실행 2026-10-09-22에서 5절 "문서에 없는 정보"를 처음 채웠고, 실행 2026-10-09-23은 새 칸 없이 사양서·데이터시트와 오류 코드표 행에 메모를 더했다. 사용자 매뉴얼·오류 코드표·치수도·도면 행은 미조사 | 미충족 · 미승인 |
| 공개 문서 샘플 목록 | 미충족 | [문서 유형 매트릭스](document-type-matrix.md) 4절에 샘플 11건을 실었다(실행 2026-10-09-23에서 AMR 4건(MiR250, MiR1350 Pallet Lift, Clearpath IndoorNav·OutdoorNav)과 Universal Robots, OMRON, 두산로보틱스 웹 매뉴얼을 추가). 국내 AMR 샘플이 없고 이용 조건은 표기 관찰 수준 | 미충족 · 미승인 |

다음 단계로 전환: 아니오(완료 조건 미충족 — 문서 유형 매트릭스 사용자 매뉴얼·오류 코드표·치수도·도면 행과 대부분 칸 미조사, 국내 AMR 샘플 없음; 막힌 질문 q2-06·q2-07)

## 7. 관련 세부영역

이 트랙은 분류를 바꾸지 않는다. 각 항목 뒤에는 이 단계에서 확인된 사실을 그 영역 페이지의 어느 절에 반영하자고 제안할지를 적었다. 반영 제안은 세부영역 페이지를 직접 고치지 않고 [트랙 로그](log.md)의 "세부영역 반영 제안" 항목으로 남기며, 반영은 다음 해당 영역 실행에서 한다. 프런트매터 `related_areas`는 아래 목록과 같다.

**중심 영역**

- [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md) — 제조사별 기능·제약·장착 장비·실행 조건이 문서 어디에 어떤 형태로 있는지가 이 영역의 공통 모델을 어떻게 채울 수 있는지를 정한다. 실행 2026-09-25-57은 문서 유형·형태별 분산과 기계가독 스키마 사례를 "6. 대표 접근법과 기술" 절에 반영하도록 제안했다. 실행 2026-10-09-22는 팩트시트가 유형 시리즈 수준의 선언이고 동작 결과·제약이 자유 텍스트로 남아, 능력 모델이 문서 선언과 운용 중 관측을 함께 담아야 한다는 점을 같은 절에 반영하도록 제안했다.

**연구 방법으로 연결되는 영역(현행 분류 L. AI·학습 기술 주석의 교차 규칙)**

- [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) — 문서 파싱과 형태별 추출 난이도, 매뉴얼 대상 추출 연구는 이 영역의 방법이다. 매뉴얼 해석은 4. 이기종 로봇 등록과 55. 현장 조사·설치·시운전에 적용되는 연구 방법이다.
- [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) — AI가 해석한 기능 정보를 실행에 쓰는 기준을 다룬다. 실행 2026-09-25-57은 매뉴얼 대상 LLM 추출 연구와 문서 파싱 벤치마크를 "6. 대표 접근법과 기술"·"8. 대표 연구와 자료" 절에 반영하도록 제안했다(적용 대상인 5. 로봇 능력·작업 표현와 55. 현장 조사·설치·시운전에도 연결).

**이 단계의 질문이 언급하는 영역(트랙 개요의 배정에 따른 추가 연결, [가정])**

- [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md) — 문서 분석과 기능 탐색은 이 영역의 온보딩 절차 일부다. 실행 2026-09-25-57은 온보딩 때 모을 제조사 문서 유형과 공개 경로·이용 조건(국내 제조사 사례 포함)을 "6. 대표 접근법과 기술" 절에 반영하도록 제안했다. 실행 2026-10-09-22는 플릿 어댑터 통합 때 사람이 채우는 현장 설정(층별 좌표 대응점·충전기 배정)과 동작–로봇 API 매핑·완료 확인 코드가 제조사 문서 밖의 암묵지로 보인다는 점을 같은 절에 반영하도록 제안했다.
- [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md) — 상태 보고의 배터리 비율·남은 가동 시간·적재 여유·오류 코드는 이 영역의 현재 상태 표현이다(34. 시뮬레이션·예측용 디지털 트윈과 구분). 이번 실행은 이 영역에 반영 제안을 내지 않았다.

**실행 2026-10-09-23의 반영 제안**

- [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md) — 등록 때 확보할 제조사 문서의 접근 조건(로그인·양식 제출)과 재사용 표기, 근거 문서에 언어·원본 여부·적용 판을 함께 기록할 필요를 "6. 대표 접근법과 기술" 절에 반영하도록 제안했다. 매뉴얼 해석은 L. AI·학습 기술 주석의 교차 규칙에 따라 이 영역에 적용되는 연구 방법이다.
- [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) — 근거 형태별 문서 이해 정확도, 산업 문서 다중 모달 검색 증강 생성, 데이터시트→자산관리셸 추출, 매뉴얼 질의응답과 교차 언어 검색 연구를 "8. 대표 연구와 자료" 절에 반영하도록 제안했다.
- [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) — 소프트웨어 판에 따라 기능이 추가·폐기되고 문서 판의 유지가 끝나는 사례와 팩트시트 구성 블록의 하드웨어·소프트웨어 판 키-값을 "6. 대표 접근법과 기술" 절에 반영하도록 제안했다.

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
[^ref-040]: Open Robotics, PerformAction Tutorial - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets_action_tutorial.html, 접근일 2026-10-09
[^ref-228]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — json_schemas/factsheet.schema, 미확인, https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema, 접근일 2026-10-09
[^ref-230]: MassRobotics, MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json, 미확인, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json, 접근일 2026-10-09
[^ref-105]: Open Robotics (open-rmf), fleet_adapter_template — fleet_adapter_template/config.yaml, 미확인, https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml, 접근일 2026-10-09
[^ref-041]: Naqvi, M. R. 외(Scientific Reports), Ontology-driven integration of advertised and operational capabilities in robots, 2025-10-02, https://www.nature.com/articles/s41598-025-16649-3, 접근일 2026-09-25 (원문 미열람)
[^ref-1375]: Mobile Industrial Robots (MiR), MiR250 HW 2.0 SW 2.x — Product documents, 미확인, https://mobile-industrial-robots.com/product-documents/mir250-hw-20-sw-2-v1, 접근일 2026-10-09
[^ref-1376]: Mobile Industrial Robots (MiR), MiR1350 Pallet Lift HW 1.0 SW 2.x — Product documents, 미확인, https://mobile-industrial-robots.com/product-documents/mir1350-pallet-lift-hw-10-sw-2-v1, 접근일 2026-10-09
[^ref-1377]: Universal Robots A/S, User Manuals (PolyScope X 10.13 landing page), 미확인, https://www.universal-robots.com/manuals/EN/HTML/SW10_13/Content/Landingpages/WebPolyX/Usermanual.htm, 접근일 2026-10-09
[^ref-1378]: Universal Robots A/S, Copyright and disclaimers (SW 5.26 manual), 미확인, https://www.universal-robots.com/manuals/EN/HTML/SW5_26/Content/prod-fu-tp/fu-tp-copyright-and-disclaimers.htm, 접근일 2026-10-09
[^ref-1379]: Clearpath Robotics by Rockwell Automation, IndoorNav User Manual — Getting Started, 2025-07-18, https://docs.clearpathrobotics.com/docs_indoornav_user_manual/getting_started, 접근일 2026-10-09
[^ref-1380]: Clearpath Robotics by Rockwell Automation, IndoorNav User Manual — Appendix A: IndoorNav ROS 2 API, 미확인, https://docs.clearpathrobotics.com/docs_indoornav_user_manual/api, 접근일 2026-10-09
[^ref-1381]: Clearpath Robotics by Rockwell Automation, OutdoorNav User Manual 1.0.0 — API Overview, 미확인, https://docs.clearpathrobotics.com/docs_outdoornav_user_manual/1.0.0/api/api_overview, 접근일 2026-10-09
[^ref-1382]: OMRON Robotics, Download center, 미확인, https://robotics.omron.com/browse-documents/?dir_id=125, 접근일 2026-10-09
[^ref-1383]: Boston Dynamics, Spot SDK Release Notes, 미확인, https://dev.bostondynamics.com/docs/release_notes, 접근일 2026-10-09
[^ref-1384]: 두산로보틱스, Doosan Robotics User Manual 3.2.1 — Manipulator (M/H Series), 미확인, https://manual.doosanrobotics.com/en/user-manual/3.2.1/1-m-h-series/manipulator, 접근일 2026-10-09
[^ref-1385]: 두산로보틱스, 두산로보틱스 사용자 매뉴얼 3.2.1 — M1013, 미확인, https://manual.doosanrobotics.com/ko/user-manual/3.2.1/1-m-h-series/m1013, 접근일 2026-10-09
[^ref-1386]: European Parliament and Council (legislation.gov.uk 게재본, EUR-Lex 원문 미열람), Directive 2006/42/EC on machinery — Annex I, 2006-05-17, https://www.legislation.gov.uk/eudr/2006/42/annex/I, 접근일 2026-10-09
[^ref-1387]: Ma, Y. 외 (NeurIPS 2024 Datasets and Benchmarks), MMLongBench-Doc: Benchmarking Long-context Document Understanding with Visualizations, 2024-07, https://arxiv.org/abs/2407.01523, 접근일 2026-10-09
[^ref-1388]: Riedler, M., & Langer, S., Beyond Text: Optimizing RAG with Multimodal Inputs for Industrial Applications, 2024-10-29, https://arxiv.org/abs/2410.21943, 접근일 2026-10-09
[^ref-1389]: Gun, J., & Oksanen, T. (Technical University of Munich), Agri-Query: A Case Study on RAG vs. Long-Context LLMs for Cross-Lingual Technical Question Answering, 2025-08-25, https://arxiv.org/abs/2508.18093, 접근일 2026-10-09
[^ref-1390]: Singh, R. 외, A Multimodal Manufacturing Safety Chatbot: Knowledge Base Design, Benchmark Development, and Evaluation of Multiple RAG Approaches, 2025-11-14, https://arxiv.org/abs/2511.11847, 접근일 2026-10-09
[^ref-1072]: Xia, Y., Xiao, Z., Jazdi, N., & Weyrich, M. (IEEE Access), Generation of Asset Administration Shell with Large Language Model Agents: Toward Semantic Interoperability in Digital Twins in the Context of Industry 4.0, 2024-03, https://arxiv.org/abs/2403.17209, 접근일 2026-10-09
[^ref-1071]: Groß, J., & Heidrich, J., AAS-RAIL: Improving Information Extraction for Asset Administration Shells through Retrieval-Augmented In-Context Learning, 2026-09-07, https://arxiv.org/abs/2609.07334, 접근일 2026-10-09

## 9. 이력

실행 id는 트랙 실행의 id(YYYY-MM-DD-NN)이며, 구축 시드 항목은 [트랙 로그](log.md)와 같은 표기 `build-2026-09-24`를 쓴다. 이 값은 실행 id가 아니라 위키 구축 시점을 나타내며, 파이프라인 실행이 아니므로 일일 로그가 없다.

| 날짜 | 실행 id | 답한 질문 | 새 질문 | 온톨로지 변경 | 버전 |
|---|---|---|---|---|---|
| 2026-10-09 | 2026-10-09-23 | q2-02, q2-03, q2-05(셋 다 신뢰도 낮은 답) | q3-10 | v0.4 → v0.5 | 4 |
| 2026-10-09 | 2026-10-09-22 | q2-04(q2-02 보강·q2-03 재인용 확인, 둘 다 부분 답) | q3-09, q4-17 | 없음(v0.4 유지) | 3 |
| 2026-09-25 | 2026-09-25-57 | q2-01(q2-02·q2-03 부분 답) | q2-07, q6-07 | v0.3 → v0.4 | 2 |
| 2026-09-24 | build-2026-09-24(구축 시드, 파이프라인 실행 아님) | 없음 | 시드 q2-01~q2-05(5건, 구축 시 [질문 백로그](question-backlog.md)에 등록) | 없음(v0 시드는 [능력 온톨로지 초안](ontology-draft.md)에서 생성) | 1 |
