# 리서치 브리프 2026-10-09-23

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-09-23 |
| 날짜 | 2026-10-09 |
| 실행 유형 | track (트랙 실행) |
| 대상 영역 | 5. 로봇 능력·작업 표현 |
| 대분류 | B. 로봇 온톨로지 |

트랙 실행: 트랙 `manual-capability-ontology` · 단계 2 · 답한 질문 q2-02, q2-03, q2-05

## 갭(비어 있거나 약한 섹션)

- 단계 2 질문 q2-02·q2-03 조사 중(실행 2026-09-25-57·2026-10-09-22 부분 답), q2-05 열림 — target.json 지정(사용자 지정 0건, 되돌아온 질문 0건, 현재 단계 열린 질문 5건 중 오래된 순)
- q2-02 남은 부분: 형태별(문장·표·그림·코드) 추출 난이도를 측정한 자료 없음
- q2-03 남은 부분: AMR 제조사 공개 매뉴얼 샘플 없음, 포털 매뉴얼 문서의 이용 조건 미확인
- q2-05 미조사: 단계 2 페이지 3절에 소제목 없음
- 완료 조건: 문서 유형 매트릭스 64칸 가운데 9칸만 채움(사용자 매뉴얼·오류 코드표·치수도·도면 행 미조사), 공개 문서 샘플 목록에 AMR 샘플 없음
- 능력 온톨로지 초안 6절 '근거 문서의 단위와 버전' 질문이 q2-05 결과를 기다림

## 조사 질문

1. 로봇이 할 수 있는 일과 작업이 요구하는 조건을 어떻게 같은 말로 표현할 것인가? [분류원문]
2. q2-02 기능 정보는 어떤 형태(문장, 표, 그림·다이어그램, 코드 예제, 파라미터 표)로 존재하며 형태별 추출 난이도는 어떠한가?
3. q2-03 공개적으로 접근할 수 있는 대표 문서 샘플(AMR, 협동로봇, 로봇팔 등)은 무엇이고 이용 조건은 어떠한가?
4. q2-05 언어·문서 버전·옵션 장비에 따라 같은 기종의 정보가 어떻게 달라지는가?
5. 문서 이해 벤치마크와 기술 매뉴얼 질의응답 연구는 근거 형태(텍스트·레이아웃·표·차트·이미지)별 정확도를 어떻게 보고하는가? (단계 2 페이지 3절 q2-02 남은 부분 겨냥)
6. AMR·협동로봇 제조사의 공개 문서 포털은 문서별로 어떤 접근 조건(로그인·승인)과 재사용 조건(저작권 표기)을 두는가? (단계 2 페이지 3절 q2-03, 문서 유형 매트릭스 4절 겨냥)
7. 설명서의 원본·번역 구분과 언어 요건을 정한 규정은 무엇이고 국내 제조사 웹 매뉴얼은 판·언어를 어떻게 관리하는가? (q2-05, 한국 자료 우선)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | MMLongBench-Doc(NeurIPS 2024)은 지침·튜토리얼을 포함한 7개 유형의 긴 PDF 135건에 대해 질문마다 근거 형태(텍스트·레이아웃·차트·표·이미지)를 표시하고, GPT-4o 의 근거 형태별 정확도를 텍스트 46.3, 레이아웃 46.0, 차트 45.3, 표 50.0, 이미지 44.1로 보고했다. | ref-1409 | 아니오 | medium | 2024-07 | — | — |
| f2 | [사실] | 같은 벤치마크에서 공개 시각-언어 모델은 차트·이미지 근거 질문에서 더 낮았고(InternVL-Chat-v1.5 차트 7.1 대 텍스트 14.0), OCR 파싱 텍스트를 받은 텍스트 전용 모델(Mixtral 8x22B)도 텍스트 34.2 대 차트 19.5·이미지 19.2로 낮아져, 저자들은 이를 OCR 이 차트·이미지를 읽지 못하는 한계로 설명했다. | ref-1409 | 아니오 | medium | 2024-07 | — | — |
| f3 | [사실] | Riedler·Langer(2024)는 산업 문서 대상 검색 증강 생성에서 이미지 검색이 텍스트 검색보다 어렵고, 이미지를 다중 모달 임베딩으로 다루는 것보다 텍스트 요약으로 바꾸는 쪽이 더 유망하다고 보고했다. | ref-1410 | 아니오 | medium | 2024-10-29 | — | — |
| f4 | [사실] | Xia 외(IEEE Access, 2024)는 기술 자산 데이터시트의 텍스트에서 LLM 에이전트로 자산관리셸 모델을 생성해, 원문 정보가 오류 없이 옮겨진 비율(유효 생성률)을 62~79%로 보고했다. | ref-1072 | 아니오 | medium | 2024-03 | — | — |
| f5 | [사실] | Groß·Heidrich(arXiv 2609.07334)는 비슷한 자산관리셸 인스턴스에서 찾은 추출 예시로 맞춤 예시를 만드는 방식(AAS-RAIL)이 PDF 제품 데이터시트 추출에서 일반 소수 예시 프롬프트보다 30.4~52.4% 상대 개선을 보였다고 보고하며, 이를 회사별 명명·서식 차이에 맞추는 방법으로 제시했다. | ref-1071 | 아니오 | medium | 2026-09-07 | — | — |
| f6 | [사실] | Singh 외(arXiv 2511.11847)는 Universal Robots UR5e 협동로봇을 포함한 기계 3종의 운전·안전 매뉴얼로 질의응답 벤치마크를 만들어 검색 증강 생성 구성 24가지를 비교했고, 배포용으로 고른 구성의 정확도를 86.66%로 보고했으나 초록에는 표·그림·텍스트 근거별 결과가 없다. | ref-1412 | 아니오 | medium | 2025-11-14 | 제조 공장 | — |
| f7 | [추정] | 두산로보틱스 한국어 웹 매뉴얼(3.2.1)은 M1013 사양을 '구분 / 항목 / 사양 정보' 세 열의 HTML 표로 두고 가반 하중·최대 반경·관절 범위와 속도·반복 정밀도·IP 등급·사용 환경을 단위와 함께 적으며, 그 페이지에 작업 영역 그림은 없다. | ref-1407 | 아니오 | medium | 2026-10-09 | — | 벤더 주장 |
| f8 | [추정] | Universal Robots 사용자 매뉴얼 안내 페이지는 로봇 사용자 매뉴얼과 별도로 오류 코드(Error Codes), 스크립트 명세(Script Directory), 소프트웨어 핸드북을 메뉴로 두어, 오류 의미와 명령 인터페이스 정보가 사용자 매뉴얼 밖의 별도 문서에 있음을 보여 준다. | ref-1399 | 아니오 | medium | 2026-10-09 | — | 벤더 주장 |
| f9 | [추정] | 확인한 측정 자료를 종합하면 문서 추출 난이도는 HTML·텍스트 파라미터 표가 가장 낮고, OCR 을 거치는 차트·그림·이미지에서 가장 높으며(공개 모델·OCR 파이프라인에서 특히), 기술 매뉴얼 질의응답 연구는 형태별이 아니라 전체 정확도만 보고하므로 로봇 매뉴얼의 형태별 추출 난이도는 범용 문서 벤치마크로 유추할 수 있을 뿐 직접 측정된 것은 아닌 것으로 보인다. | ref-1409, ref-1410, ref-1412, ref-1072, ref-1407 | 아니오 | low | 2026-10-09 | — | — |
| f10 | [추정] | MiR 의 제품 문서 페이지(MiR250 HW 2.0 SW 2.x, MiR1350 Pallet Lift HW 1.0 SW 2.x)는 사용자 가이드·빠른 시작·적합성 문서는 로그인 표시 없이 내려받게 하지만 인터페이스·시운전·기술·위험성평가·사이버보안 가이드와 버전별 REST API 참조는 MiR 지원 포털 로그인을 요구하고, 문서 이용 조건은 페이지에 적지 않는다. | ref-1397, ref-1398 | 아니오 | medium | 2026-10-09 | — | 벤더 주장 |
| f11 | [추정] | Clearpath Robotics 의 IndoorNav 사용자 매뉴얼(OTTO Motors 실내 자율주행 소프트웨어 기반)은 로그인 없이 열리는 웹 문서로 'All rights reserved' 를 표기하고, 전체 ROS 2 API 문서는 설치 패키지(clearpath-api) 안에 있거나 OTTO Motors 계정이 필요한 docs.ottomotors.com 에 둔다. | ref-1401, ref-1402 | 아니오 | medium | 2025-07-18 | — | 벤더 주장 |
| f12 | [추정] | OMRON 로보틱스 다운로드 센터는 자료에 접근하려면 양식을 제출해 승인을 받게 한다. | ref-1404 | 아니오 | medium | 2026-10-09 | — | 벤더 주장 |
| f13 | [추정] | Universal Robots 매뉴얼의 저작권 고지는 내용을 Universal Robots A/S 의 사전 서면 승인 없이 전체든 일부든 복제하지 못하게 하고, 내용이 예고 없이 바뀔 수 있다고 적는다. | ref-1400 | 아니오 | medium | 2026-10-09 | — | 벤더 주장 |
| f14 | [추정] | 두산로보틱스 웹 매뉴얼은 로그인 없이 열리며 매뉴얼 PDF 내려받기·ROS 2 문서·API 문서 링크를 두지만, 하단에는 'Copyright Doosan Robotics Inc.' 표기와 개인정보 처리방침 링크만 있고 별도의 이용 조건이나 재사용 허락 문구는 없다. | ref-1406 | 아니오 | medium | 2026-10-09 | — | 벤더 주장 |
| f15 | [추정] | AMR 쪽에도 공개 문서 샘플(MiR 사용자 가이드, Clearpath IndoorNav·OutdoorNav 웹 매뉴얼)이 있지만 통합 수준 문서(REST API 참조·인터페이스·시운전 가이드·전체 API)는 계정·승인 뒤에 두는 경향이 있고, 공개 문서도 '모든 권리 보유'나 서면 승인 없는 복제 금지를 표기하므로, 매뉴얼을 자동 추출해 능력 온톨로지에 재가공하려면 제조사의 명시적 허락을 따로 확인해야 할 것으로 보인다. | ref-1397, ref-1401, ref-1402, ref-1404, ref-1400, ref-1406 | 아니오 | low | 2026-10-09 | — | — |
| f16 | [사실] | EU 기계류 지침 2006/42/EC 부속서 I 1.7.4.1 은 설명서를 하나 이상의 공식 공동체 언어로 쓰게 하고, 제조자가 확인한 언어판에 'Original instructions' 를, 사용국 언어로 옮긴 판에 'Translation of the original instructions' 를 표기하게 한다. | ref-1408 | 아니오 | medium | 2006-05-17 | — | — |
| f17 | [추정] | MiR250 제품 문서 페이지는 로봇 하드웨어 2.0·소프트웨어 2.x·SICK 설정 파일 판 단위로 문서를 묶고, 문서마다 제공 언어가 달라 사용자 가이드는 10개, 빠른 시작은 16개, 인터페이스 가이드는 5개 언어이며 기술·위험성평가·사이버보안 가이드는 영어로만 제공한다. | ref-1397 | 아니오 | medium | 2026-10-09 | — | 벤더 주장 |
| f18 | [추정] | MiR1350 Pallet Lift 문서 페이지는 로봇 하드웨어 1.0 과 별도로 상위 모듈 하드웨어 1.0·소프트웨어 2.x·SICK 설정 파일 판을 적어, 상위 모듈(옵션 장비)을 단 구성이 자체 문서 묶음과 판을 갖는다. | ref-1398 | 아니오 | medium | 2026-10-09 | — | 벤더 주장 |
| f19 | [추정] | MiR250 페이지에서 사용자 가이드·빠른 시작은 모든 언어에 판 2.1 로 표시되지만 포르투갈어 링크는 1.4·1.5 판 이름의 경로를 가리켜, 언어판 사이에 판이 어긋날 수 있는 것으로 보인다. | ref-1397 | 아니오 | low | 2026-10-09 | — | 벤더 주장 |
| f20 | [추정] | 두산로보틱스 웹 매뉴얼은 판 선택(3.2.0~3.7.0), 한국어를 포함한 13개 언어, 제품군 메뉴(M/H·A·E·P 시리즈)를 두고, V2 이전 판은 별도의 레거시 매뉴얼 사이트로 분리한다. | ref-1406 | 아니오 | medium | 2026-10-09 | — | 벤더 주장 |
| f21 | [추정] | Universal Robots 는 사용자 매뉴얼을 로봇 모델별로 나누고 같은 모델(예: UR20)에도 PolyScope 5 와 PolyScope X(10.x) 두 소프트웨어 계열의 매뉴얼을 따로 두며, 매뉴얼 주소에 소프트웨어 판(SW5_26, SW10_13)과 언어를 구분해 담는다. | ref-1399, ref-1400 | 아니오 | medium | 2026-10-09 | — | 벤더 주장 |
| f22 | [추정] | Boston Dynamics Spot SDK 릴리스 노트는 판마다 Breaking Changes·New Features·Deprecations 절을 두고, 판에 따라 기능이 더해지거나(4.1.0 의 계단 사용 금지 STAIRS_MODE_PROHIBITED) 필드가 폐기되며(5.0.0 SystemFault uid), 일부 예제는 로봇이 5.1.0 이상을 실행해야 한다고 적는다. | ref-1405 | 아니오 | medium | 2026-10-09 | — | 벤더 주장 |
| f23 | [추정] | Clearpath OutdoorNav 매뉴얼은 판 선택(0.7.0~2.3.0과 Legacy)을 두고 1.0.0 판을 '더 이상 유지되지 않음'으로 표시하며 그 판의 API 를 ROS 1 Noetic 기준으로 설명하고, IndoorNav API 문서 경로에도 판(ros2-api-1.3.3)이 들어 있다. | ref-1403, ref-1402 | 아니오 | medium | 2026-10-09 | — | 벤더 주장 |
| f24 | [사실] | VDA 5050 팩트시트 스키마(main, 3.0.0)는 팩트시트를 이동로봇 유형 시리즈의 기본 정보로 설명하면서도 serialNumber 를 필수로 두고, 구성 블록(mobileRobotConfiguration)에 하드웨어·소프트웨어 판의 키-값 배열(versions)을 두며, 적재 취급 장치 목록(loadPositions)이 없거나 비면 적재 취급 장치가 없는 것으로 정한다. | ref-228 | 아니오 | medium | 2026-10-09 | — | — |
| f25 | [사실] | Agri-Query(Gun·Oksanen, 2025)는 배치가 같은 165쪽 농기계 매뉴얼의 영어·프랑스어·독일어 공식판에 영어로 질문했을 때 키워드 검색 RAG 정확도가 크게 떨어졌고(Gemini 2.5 Flash 0.852 → 0.583·0.528), 혼합 검색 RAG 는 하락이 작았다(0.880·0.824·0.870)고 보고했으며, 표·그림 해석은 평가하지 않았다. | ref-1411 | 아니오 | medium | 2025-08-25 | — | — |
| f26 | [추정] | 확인한 사례를 종합하면 같은 기종의 정보는 (가) 언어판(원본과 번역, 문서 유형별로 다른 언어 범위, 판이 어긋난 번역판), (나) 소프트웨어·문서 판(판별 기능 추가·폐기, 유지 중단된 판), (다) 하드웨어·상위 모듈·옵션 구성(별도 문서 묶음, 적재 취급 장치 유무)에 따라 달라지므로, 근거 문서에는 언어·원본 여부와 적용 하드웨어·소프트웨어·모듈 판을 함께 기록해야 할 것으로 보인다. | ref-1408, ref-1397, ref-1398, ref-1406, ref-1399, ref-1405, ref-1403, ref-228 | 아니오 | low | 2026-10-09 | — | — |

### 근거 발췌

- **f1**: Table 3 기준 GPT-4o TXT 46.3 / LAY 46.0 / CHA 45.3 / TAB 50.0 / IMG 44.1, 전체 ACC 42.8·F1 44.9. 문서 유형 7종에 Guideline·Tutorial/Workshop 포함, 로봇 매뉴얼은 대상에 명시되지 않음.
- **f2**: GPT-4o 만 근거 형태 사이 성능이 비교적 고르고, 다른 모델은 차트·이미지 관련 질문에서 텍스트·레이아웃보다 나쁘다고 보고(arXiv 2407.01523v3 Table 3).
- **f3**: 초록: "image retrieval poses a greater challenge than text retrieval". GPT-4V·LLaVA, LLM-as-a-Judge 평가. 사용한 산업 문서 이름은 초록에 없음.
- **f4**: 초록 기준 effective generation rate 62–79%. 데이터시트 원문 텍스트 대상이며 표·그림 형태별 결과는 초록에 없음(원문 본문 미확인).
- **f5**: 초록: relative improvements of 30.4-52.4% over conventional few-shot prompting. 지표 이름·데이터셋 규모·표/텍스트 구분은 초록에 없음.
- **f6**: 초록: top configuration achieved an accuracy of 86.66%, 평균 비용 $0.005/질의, 지연 10.04초. 기계: Bridgeport 수동 밀링, Haas TL-1 CNC 선반, UR5e.
- **f7**: 벤더 주장: 표는 Performance, Joint Movement, 사용 환경, 툴 플랜지 & 커넥터, 중량, 마운팅, IP 등급, 소음 순으로 묶임. 문서 형태 관찰이며 사양 값 자체는 인용하지 않음. (발행일 미확인, 확인일 기준)
- **f8**: 벤더 주장: 왼쪽 메뉴에 PolyScope X Software Handbook, Robot User Manuals, Script Directory, Service Your Robot, Error Codes, Components, Kits, Software Guides. 각 문서의 내부 형태는 미확인. (발행일 미확인, 확인일 기준)
- **f9**: 이 위키의 종합: 범용 문서 벤치마크(f1·f2), 산업 문서 RAG(f3), 매뉴얼 QA(f6), 데이터시트 추출(f4), 웹 매뉴얼 표 형태(f7)를 대응시킨 추론이며 로봇 매뉴얼 대상 측정은 이번 검색 범위에서 찾지 못함(부재 확정 아님).
- **f10**: 벤더 주장: "You must sign in to MiR Support Portal to access the overview page links." REST API 참조는 모든 소프트웨어 버전·로봇용 별도 목록(로그인 필요). 페이지 하단은 개인정보·쿠키 정책·일반 인도 조건만 링크. (발행일 미확인, 확인일 기준)
- **f11**: 벤더 주장: 하단 "© Clearpath Robotics by Rockwell Automation. All rights reserved." API 는 Fleet(도메인 100)·Autonomy(110)·Platform(95, IndoorNav 미지원)으로 나뉨, 마지막 갱신 2025-07-18.
- **f12**: 벤더 주장: "Please fill out the form to access our resources." 승인·거절·검토 상태 안내가 있음. 하단에 Terms of Use 링크가 있으나 다운로드 적용 범위는 미확인. (발행일 미확인, 확인일 기준)
- **f13**: 벤더 주장: "shall not be reproduced in whole or in part without prior written approval of Universal Robots A/S." 또한 subject to change without notice. 번역·원본 표기는 이 페이지에 없음. (발행일 미확인, 확인일 기준)
- **f14**: 벤더 주장: 매뉴얼은 PART 1 안전 매뉴얼, PART 2 로봇 기동, PART 3 설치 매뉴얼(시스템 사양 포함), PART 4 사용자 매뉴얼 개요로 구성. (발행일 미확인, 확인일 기준)
- **f15**: 이 위키의 종합(f10~f14). 샘플 5개 제조사 범위의 관찰이며 법적 판단이 아님. 국내 AMR 제조사의 공개 매뉴얼·API 문서는 한국어 검색 2회에서 찾지 못함(부재 확정 아님).
- **f16**: "The words ‘Original instructions’ must appear on the language version(s) verified by the manufacturer." 사용국 언어 원본이 없으면 제조자 또는 그 언어권에 들여오는 자가 번역판을 제공. 이 지침은 규정 (EU) 2023/1230 으로 대체 예정(새 규정 원문 미열람).
- **f17**: 벤더 주장: Robot HW 2.0, SW 2.x, SICK configuration file MiR250_HW2-0_V2. 사용자 가이드에 한국어 포함. 사용자 가이드·빠른 시작만 판(2.1)을 표시. (발행일 미확인, 확인일 기준)
- **f18**: 벤더 주장: Robot HW 1.0 / Top module HW 1.0 / SW 2.x / SICK configuration file MiR1350 v6.4. 사용자 가이드 1.4, 빠른 시작 1.5. (발행일 미확인, 확인일 기준)
- **f19**: 벤더 주장: 열람 도구가 보고한 링크 경로 관찰(Portuguese links point to paths named 1,4 and 1,5). 파일을 내려받아 판을 대조하지 않음. (발행일 미확인, 확인일 기준)
- **f20**: 벤더 주장: 판 3.7.0, 3.6.0, 3.5.0, 3.4.0, 3.3.0, 3.2.2, 3.2.1, 3.2.0. 언어: 한국어·영어·중국어·체코어·네덜란드어·프랑스어·독일어·헝가리어·이탈리아어·일본어·폴란드어·포르투갈어·스페인어. Legacy manual 링크. (발행일 미확인, 확인일 기준)
- **f21**: 벤더 주장: 안내 페이지 머리에 PolyScope X 10.13, 두 시리즈 모두 "You can use PolyScope 5 and PolySocpe X"(원문 오타). 저작권 페이지 주소가 /manuals/EN/HTML/SW5_26/. (발행일 미확인, 확인일 기준)
- **f22**: 벤더 주장: 5.2.0 Graph Nav Upload 예제 "Requires robots running 5.1.0 or later." 5.1.9 Deprecations, 5.0.1 Upcoming Breaking Changes·Known Issues 절. (발행일 미확인, 확인일 기준)
- **f23**: 벤더 주장: 1.0.0 페이지 "no longer actively maintained", 최신 2.3.0 링크. API 그룹: Platform, Autonomy, Mission Manager, Mission Scheduler. (발행일 미확인, 확인일 기준)
- **f24**: versions: "Array containing various hardware and software versions running on the mobile robot." loadPositions 가 없거나 비면 로봇에 적재 취급 장치가 없음. 언어 필드는 없음.
- **f25**: Kverneland Exacta-TLX Geospread GS3 매뉴얼, 약 59k 토큰, 질문 108개(답할 수 있음 54·없음 54). Qwen 2.5 7B 혼합 RAG 0.861·0.852·0.796. 초록의 '모든 언어 85% 이상'은 표와 일부 불일치.
- **f26**: 이 위키의 종합(f16~f24). 같은 기종의 판·언어판 사이 실제 내용 차이(예: 사양 값 변경)를 문서끼리 대조해 확인하지는 않음.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 미확인 | 표준 | high | 2026-10-09 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema | 아니오 |
| ref-1397 | Mobile Industrial Robots (MiR) | MiR250 HW 2.0 SW 2.x — Product documents | 미확인 | 벤더 문서 | medium | 2026-10-09 | https://mobile-industrial-robots.com/product-documents/mir250-hw-20-sw-2-v1 | 아니오 |
| ref-1398 | Mobile Industrial Robots (MiR) | MiR1350 Pallet Lift HW 1.0 SW 2.x — Product documents | 미확인 | 벤더 문서 | medium | 2026-10-09 | https://mobile-industrial-robots.com/product-documents/mir1350-pallet-lift-hw-10-sw-2-v1 | 아니오 |
| ref-1399 | Universal Robots A/S | User Manuals (PolyScope X 10.13 landing page) | 미확인 | 벤더 문서 | medium | 2026-10-09 | https://www.universal-robots.com/manuals/EN/HTML/SW10_13/Content/Landingpages/WebPolyX/Usermanual.htm | 아니오 |
| ref-1400 | Universal Robots A/S | Copyright and disclaimers (SW 5.26 manual) | 미확인 | 벤더 문서 | medium | 2026-10-09 | https://www.universal-robots.com/manuals/EN/HTML/SW5_26/Content/prod-fu-tp/fu-tp-copyright-and-disclaimers.htm | 아니오 |
| ref-1401 | Clearpath Robotics by Rockwell Automation | IndoorNav User Manual — Getting Started | 2025-07-18 | 벤더 문서 | medium | 2026-10-09 | https://docs.clearpathrobotics.com/docs_indoornav_user_manual/getting_started | 아니오 |
| ref-1402 | Clearpath Robotics by Rockwell Automation | IndoorNav User Manual — Appendix A: IndoorNav ROS 2 API | 미확인 | 벤더 문서 | medium | 2026-10-09 | https://docs.clearpathrobotics.com/docs_indoornav_user_manual/api | 아니오 |
| ref-1403 | Clearpath Robotics by Rockwell Automation | OutdoorNav User Manual 1.0.0 — API Overview | 미확인 | 벤더 문서 | medium | 2026-10-09 | https://docs.clearpathrobotics.com/docs_outdoornav_user_manual/1.0.0/api/api_overview | 아니오 |
| ref-1404 | OMRON Robotics | Download center | 미확인 | 벤더 문서 | medium | 2026-10-09 | https://robotics.omron.com/browse-documents/?dir_id=125 | 아니오 |
| ref-1405 | Boston Dynamics | Spot SDK Release Notes | 미확인 | 벤더 문서 | medium | 2026-10-09 | https://dev.bostondynamics.com/docs/release_notes | 아니오 |
| ref-1406 | 두산로보틱스 | Doosan Robotics User Manual 3.2.1 — Manipulator (M/H Series) | 미확인 | 벤더 문서 | medium | 2026-10-09 | https://manual.doosanrobotics.com/en/user-manual/3.2.1/1-m-h-series/manipulator | 아니오 |
| ref-1407 | 두산로보틱스 | 두산로보틱스 사용자 매뉴얼 3.2.1 — M1013 | 미확인 | 벤더 문서 | medium | 2026-10-09 | https://manual.doosanrobotics.com/ko/user-manual/3.2.1/1-m-h-series/m1013 | 아니오 |
| ref-1408 | European Parliament and Council (legislation.gov.uk 게재본) | Directive 2006/42/EC on machinery — Annex I | 2006-05-17 | 정부·연구기관 | high | 2026-10-09 | https://www.legislation.gov.uk/eudr/2006/42/annex/I | 아니오 |
| ref-1409 | Ma, Y. 외 (NeurIPS 2024 Datasets and Benchmarks) | MMLongBench-Doc: Benchmarking Long-context Document Understanding with Visualizations | 2024-07 | 논문 | high | 2026-10-09 | https://arxiv.org/abs/2407.01523 | 아니오 |
| ref-1410 | Riedler, M., & Langer, S. | Beyond Text: Optimizing RAG with Multimodal Inputs for Industrial Applications | 2024-10-29 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2410.21943 | 아니오 |
| ref-1411 | Gun, J., & Oksanen, T. (Technical University of Munich) | Agri-Query: A Case Study on RAG vs. Long-Context LLMs for Cross-Lingual Technical Question Answering | 2025-08-25 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2508.18093 | 아니오 |
| ref-1412 | Singh, R. 외 | A Multimodal Manufacturing Safety Chatbot: Knowledge Base Design, Benchmark Development, and Evaluation of Multiple RAG Approaches | 2025-11-14 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2511.11847 | 아니오 |
| ref-1072 | Xia, Y., Xiao, Z., Jazdi, N., & Weyrich, M. (IEEE Access) | Generation of Asset Administration Shell with Large Language Model Agents: Toward Semantic Interoperability in Digital Twins in the Context of Industry 4.0 | 2024-03 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2403.17209 | 아니오 |
| ref-1071 | Groß, J., & Heidrich, J. | AAS-RAIL: Improving Information Extraction for Asset Administration Shells through Retrieval-Augmented In-Context Learning | 2026-09-07 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2609.07334 | 아니오 |

### 출처 요약

- **ref-228**: VDA 5050 main(3.0.0) 팩트시트 JSON 스키마. 이번에 raw 원문 뒷부분(구성 블록 versions·batteryCharging, 적재 명세)을 열어 확인.
- **ref-1397**: MiR250 하드웨어·소프트웨어 판별 문서 페이지. 문서 유형·언어별 제공 범위와 지원 포털 로그인 요구를 보여 준다.
- **ref-1398**: 상위 모듈(팔레트 리프트)을 단 MiR1350 의 문서 페이지. 로봇·상위 모듈 하드웨어 판과 소프트웨어 판을 따로 적는다.
- **ref-1399**: UR Series·e-Series 모델별 사용자 매뉴얼 안내와 오류 코드·스크립트 명세 등 별도 문서 메뉴.
- **ref-1400**: UR 매뉴얼의 저작권·면책 고지. 사전 서면 승인 없는 복제 금지와 예고 없는 변경을 적는다.
- **ref-1401**: OTTO Motors 실내 자율주행 소프트웨어 기반 IndoorNav 의 공개 웹 매뉴얼. 대상 로봇과 절 구성, 저작권 표기.
- **ref-1402**: ROS 2 API 의 세 도메인(Fleet·Autonomy·Platform)과 전체 API 문서 위치(설치 패키지, OTTO Motors 계정 필요 사이트).
- **ref-1403**: 판 선택(0.7.0~2.3.0)과 유지 중단 표시가 있는 OutdoorNav API 개요(ROS 1 Noetic 기준).
- **ref-1404**: OMRON 로보틱스 자료 다운로드 센터. 양식 제출과 승인 뒤 접근하게 한다.
- **ref-1405**: Spot SDK 판별 릴리스 노트. Breaking Changes·Deprecations 절과 로봇 소프트웨어 판 요구를 적는다(앞부분 열람).
- **ref-1406**: 두산로보틱스 V3 웹 매뉴얼. 판 선택·13개 언어·제품군 메뉴·레거시 매뉴얼 링크·저작권 표기를 보여 준다.
- **ref-1407**: M1013 시스템 사양을 HTML 표(구분·항목·사양 정보)로 제시한 한국어 웹 매뉴얼 페이지.
- **ref-1408**: EU 기계류 지침 부속서 I. 1.7.4.1 에 설명서의 언어, 'Original instructions'·'Translation of the original instructions' 표기 요건이 있다.
- **ref-1409**: 긴 PDF 135건·질문 1,082개의 문서 이해 벤치마크. 근거 형태(텍스트·레이아웃·차트·표·이미지)별 정확도를 보고한다.
- **ref-1410**: 산업 문서 RAG 에 이미지를 더하는 방식(다중 모달 임베딩 대 텍스트 요약)을 비교한 프리프린트(초록 열람).
- **ref-1411**: 영어·프랑스어·독일어 공식판 농기계 매뉴얼로 교차 언어 기술 질의응답을 평가한 프리프린트(v2 본문 열람).
- **ref-1412**: UR5e 를 포함한 기계 3종 매뉴얼로 만든 질의응답 벤치마크와 RAG 구성 24가지 비교(초록 열람).
- **ref-1072**: 데이터시트 텍스트에서 LLM 에이전트로 자산관리셸 모델을 생성한 연구(초록 열람). 유효 생성률 62~79%.
- **ref-1071**: PDF 제품 데이터시트에서 자산관리셸을 만드는 검색 기반 맞춤 예시 방법의 프리프린트(초록 열람).

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/tracks/manual-capability-ontology/stage-2-document-types.md | 2, 3, 4, 5, 6, 8, 9 | q2-02 답: f1·f2·f3·f4·f5·f6·f7·f8·f9 (신뢰도 low) / q2-03 답: f10·f11·f12·f13·f14·f15 (신뢰도 low) / q2-05 답: f16·f17·f18·f19·f20·f21·f22·f23·f24·f25·f26 (신뢰도 medium) — 2절 세 질문 상태를 답함으로, 3절 q2-02(근거 형태별 측정은 범용 문서 벤치마크 유추뿐임을 명시)·q2-03(AMR 샘플과 접근·재사용 조건, 제조사 문서는 벤더 주장 병기) 소절 보강, q2-05 소제목 신설({#q2-05}: 언어판·문서 판·하드웨어/상위 모듈 구성 세 축), 4절 결론·불확실성, 5절 후속 질문, 6절 완료 조건 현황, 8절 출처, 9절 이력 |
| update | docs/tracks/manual-capability-ontology/document-type-matrix.md | 3, 4, 5, 8 | 트랙 산출물 갱신: 3절 사양서·데이터시트 × 파라미터 범위 칸에 두산 웹 매뉴얼 HTML 사양 표 사례(f7, 벤더 주장) 병기, 오류 코드표 행에 UR 의 별도 오류 코드 문서 존재 메모(f8, 내용 미확인). 4절 공개 문서 샘플에 MiR250·MiR1350 Pallet Lift(AMR, f10·f17·f18), Clearpath IndoorNav·OutdoorNav(AMR, f11·f23), Universal Robots(f13·f21), OMRON 다운로드 센터(접근 승인, f12), 두산 웹 매뉴얼(f14·f20) 추가와 이용 조건 열 갱신. 판·언어 축 메모(f26) |
| update | docs/tracks/manual-capability-ontology/ontology-draft.md | 2, 6 | 온톨로지 변경 제안 1건(근거 문서 속성 '언어(원본 / 번역 구분)'·'적용 구성(하드웨어·소프트웨어 판, 상위 모듈·옵션 장비)' 추가, 근거 f16·f17·f18·f20·f22·f24·f26). 6절 '근거 문서의 단위와 버전' 질문에 q2-05 답 연결, 로봇 구성 버전 질문과의 관계 메모 |
| update | docs/ideas/robot-capability-ontology.md | 3, 4 | 아이디어 페이지 3절: 문서 이해·데이터시트 추출 측정 자료(f1·f2·f4·f5·f6) / 아이디어 페이지 4절: AMR 공개 문서 샘플과 접근·재사용 조건(f10~f15), 근거 문서의 언어·판·구성 기록 필요(f16·f24·f26) |
| update | docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md | 8 | 트랙 manual-capability-ontology 단계 2 반영 제안 (f1, f2, f3, f4, f5, f6, f25): 근거 형태별 문서 이해 정확도, 산업 문서 다중 모달 RAG, 데이터시트→자산관리셸 추출, 매뉴얼 질의응답과 교차 언어 검색. 교차 규칙(매뉴얼 해석은 4. 이기종 로봇 등록·55. 현장 조사·설치·시운전에 적용)에 따라 적용 대상 영역에도 연결 |
| update | docs/categories/robot-ontology/heterogeneous-robot-registration.md | 6 | 트랙 manual-capability-ontology 단계 2 반영 제안 (f10, f11, f12, f13, f14, f15, f26): 등록 때 확보할 제조사 문서의 접근 조건(로그인·승인)과 재사용 제한, 근거 문서에 언어·원본 여부·적용 판을 기록할 필요 |
| update | docs/categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md | 6 | 트랙 manual-capability-ontology 단계 2 반영 제안 (f22, f23, f24, f26): 소프트웨어 판에 따라 기능이 추가·폐기되고 문서 판의 유지가 끝나는 사례, 팩트시트 구성 블록의 하드웨어·소프트웨어 판 키-값 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 원본 설명서 | Original Instructions | 제조자 또는 그 대리인이 내용을 확인한 언어판 설명서로, EU 기계류 지침은 이 판에 'Original instructions'를, 다른 언어로 옮긴 판에 'Translation of the original instructions'를 표기하게 한다. |

## 열린 질문

새로 생긴 질문:

- 국내에서 판매·설치되는 산업용 로봇·이동로봇의 사용설명서를 한국어로 제공해야 한다는 규정이 자율안전확인 고시나 다른 법령에 있으며, 원본과 한국어 번역판의 판이 다를 때 어느 쪽을 근거로 삼는가? | 관련 영역: 59. 법·규제·보험·라이선스, 4. 이기종 로봇 등록 | 근거: f16 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 19 · 교차 확인: 0
- 예산 사용량: 검색 20회 · 신규 출처 18건
- 미확인 항목:
    - f9: 로봇 매뉴얼을 대상으로 근거 형태별 추출 정확도를 측정한 자료는 찾지 못함(범용 문서 벤치마크 유추)
    - f19: MiR 포르투갈어판 판 불일치는 링크 경로 관찰이며 파일을 내려받아 대조하지 않음
    - f26: 같은 기종의 판·언어판 사이 실제 내용(사양 값) 차이는 문서끼리 대조하지 않음
    - EU 규정 (EU) 2023/1230 의 설명서 언어·디지털 제공 조항은 EUR-Lex 열람 실패로 미확인(지침 2006/42/EC 만 확인)
    - ref-1410·ref-1412·ref-1072·ref-1071 는 초록만 열람
    - OTTO 데이터시트·Kinova 제품 소개 PDF 는 압축 바이너리라 읽지 못해 출처로 쓰지 않음
    - 국내 AMR 제조사의 공개 매뉴얼·API 문서는 한국어 검색에서 찾지 못함
    - 모든 finding 교차 확인 없음(단일 출처 또는 이 위키의 종합)
- 범위 경계 위반 의심:
    - f22: Spot 의 계단 사용 금지 같은 주행 동작은 분류 원문 19장 '로봇 자체 지능·제어' 연계 대상이며, 판에 따라 문서에 드러나는 기능이 달라진다는 근거로만 씀
    - f11·f23: IndoorNav·OutdoorNav 의 자율주행 API 는 제조사 쪽 기능이며, 문서 접근 조건과 판 관리 사례로만 씀
- 한계: web_fetch_available: true · fetch_mode full. 검색 20회/40, 신규 출처 18건/20(ref-1397~ref-1071, 예약 구간 안), 재사용 1건(ref-228 raw 원문 재열람). 질문 선택: target.json 지정 q2-02·q2-03·q2-05(오래된 순). 세 질문 모두 답함으로 냈으나 q2-02·q2-03 은 신뢰도 low: q2-02 는 형태별 난이도를 로봇 매뉴얼이 아니라 범용 문서 벤치마크(MMLongBench-Doc)와 산업 문서·데이터시트 연구로 유추했고, q2-03 은 AMR 샘플(MiR·Clearpath)과 접근 조건을 확인했으나 이용 조건은 저작권 표기 수준이며 법적 판단이 아니다. q2-05 는 원본·번역 규정과 제조사 문서 포털의 판·언어·구성 관리 사례로 답했다(신뢰도 medium, 종합 f26 은 low). 제조사 문서에서 가져온 문서 구성·접근 조건은 이전 실행 관례에 따라 모두 태그 추정, vendor_claim true, '벤더 주장: ' 표시. 한국 자료: 두산로보틱스 웹 매뉴얼(ref-1406·ref-1407, 한국어 페이지 포함). 원문 열기 실패: EUR-Lex(빈 응답), CEN-CENELEC 비교 PDF·OTTO·Kinova PDF(바이너리), fortiss 페이지(404), UR 영문 PDF(크기 초과). 온톨로지 변경 1건 제안(근거 문서 속성), 초안 6절 '근거 문서의 단위와 버전' 질문과 로봇 구성 버전 질문에 겹치므로 description 에 적음. 후속 질문 2건. 용어 후보 1건(원본 설명서). 트랙 glossary_targets 가운데 미등록 용어(로봇 능력 온톨로지, SPARQL, 온톨로지 학습)에 대한 이번 근거 없음. q2-07(AMR 공개 문서)은 이번 질문이 아니나 f10·f11·f17·f18·f23 이 부분 근거가 된다. L. AI·학습 기술 관련 finding(f1~f6·f9·f25)은 45. 문서·도면·장면 이해와 적용 대상 4. 이기종 로봇 등록에 함께 반영 제안. 18. 실시간 세계 상태·데이터 일관성·34. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 현장 유형 사례 finding 은 f6(제조 공장, 벤치마크 대상 기계)뿐. 정정 요청 없음. 입력 누락 없음.

## 트랙 블록

- 트랙: manual-capability-ontology · 단계: 2
- 답한 질문 id: q2-02, q2-03, q2-05

### 새 질문

| 제안 id | 질문 | 보낼 단계 | 근거 finding |
|---|---|---|---|
| — | 제조사 매뉴얼의 언어판 사이에 판 번호·내용이 어긋날 때(번역판이 원본보다 오래된 판인 경우) 능력 정의 초안의 추출 근거로 어느 언어판을 고르고, 언어판 사이 차이를 어떻게 검출하는가? (q2-05 에서 파생) | 3 | f19 |
| — | 로봇 매뉴얼(사양 표·오류 코드표·작업 영역 도면·코드 예제)에서 근거 형태(텍스트·레이아웃·표·차트·이미지)별 추출 정확도를 재는 평가 세트를 MMLongBench-Doc 의 근거 형태 분류로 만들 수 있는가, 정답 기준과 규모는 어떻게 정하는가? (q2-02 에서 파생) | 5 | f9 |

### 온톨로지 초안 변경 제안

| 동작 | 종류 | 이름 | 근거 finding | 설명 |
|---|---|---|---|---|
| modify | concept | 근거 문서 (Evidence Document) | f16, f17, f18, f20, f22, f24, f26 | 속성 '언어(원본 / 번역 구분)'와 '적용 구성(하드웨어·소프트웨어 판, 상위 모듈·옵션 장비)'을 더하는 제안. 근거: 기계류 지침의 원본·번역 표기(f16), MiR 의 하드웨어·소프트웨어·상위 모듈 판별 문서 묶음(f17·f18), 두산 웹 매뉴얼의 판×언어(f20), Spot SDK 판별 기능 변화(f22), 팩트시트 구성 블록 versions(f24). 기존 속성 '버전'은 문서 자체의 판이고 이 제안은 문서가 적용되는 로봇 구성의 판이라 구분된다. 초안 6절 '근거 문서의 단위와 버전' 질문, '로봇의 구성 버전' 질문(q6-02)과 겹치므로 로봇 쪽 구성 버전과의 관계는 검증 판단에 맡긴다. |

### 단계 완료 조건 자체 평가

- 충족 여부(자체 평가): 미충족
- 못 채운 조건:
    - 문서 유형 매트릭스: 사용자 매뉴얼·치수도·도면 행 미조사, 오류 코드표 행은 존재만 확인하고 내용 미조사, 64칸 가운데 대부분 미조사
    - 공개 문서 샘플 목록: AMR 샘플(MiR·Clearpath)은 이번에 근거가 생겼으나 검증 승인 전이며, 국내 AMR 샘플 없음
    - q2-06·q2-07 열림
