# 스토리텔러 산출 2026-09-25-01

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md | draft | 영역 심화: 섹션 3~11 신규 작성(식별 키·EPCIS 이벤트·로봇 적재 보고와 인계 확인·출하 시나리오), 상태 줄 추가, 각주 15건 정의. 2차 수정: 태그 누락 2곳 보완, 9절 표 두 행 수정, 약어 풀어쓰기, 분량 축소 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 7. 화물·재고·자산 식별과 추적 | 영역 심화 초안: 3~11절 신규 작성(GS1 식별 키, EPCIS·CBV 이벤트, VDA 5050·Open-RMF 적재·하역 보고와 인계 확인, 출하 시나리오) | run 2026-09-25-01
- 홈 최근 업데이트: 2026-09-25 — 7. 화물·재고·자산 식별과 추적: 영역 심화 초안(GS1 식별 키·EPCIS 이벤트·로봇 적재 보고와 인계 확인)
- 대분류 최근 업데이트: 2026-09-25 — 7. 화물·재고·자산 식별과 추적: 3~11절 초안 작성, 출하 인계 시나리오와 열린 질문 3건
- 세부영역 최근 업데이트: 2026-09-25 — 7. 화물·재고·자산 식별과 추적: 영역 심화 초안 작성(3~11절, 신뢰도 medium, 전 출처 원문 미열람)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 물류 단위 일련 코드 | Serial Shipping Container Code (SSCC) | 케이스·팔레트·소포 등 보관·운송을 위해 묶인 물류 단위를 고유하게 식별하는 18자리 GS1 식별 키이다. | 7 | ref-016, ref-017, ref-018 |
| new | 글로벌 반환형 자산 식별자 | Global Returnable Asset Identifier (GRAI) | 팔레트·상자·트레이·케그처럼 여러 번 재사용되는 운반구를 식별하는 GS1 식별 키이다. | 7 | ref-019, ref-020 |
| new | 글로벌 개별 자산 식별자 | Global Individual Asset Identifier (GIAI) | 컨테이너·트럭·트레일러 같은 개별 자산을 식별하는 GS1 식별 키이다. | 7 | ref-020 |
| new | 핵심 업무 어휘 | Core Business Vocabulary (CBV) | EPCIS 이벤트의 업무 단계·상태·인계 유형 등에 채울 표준 어휘 값을 정한 GS1 표준(ISO/IEC 19988)이다. | 7 | ref-012, ref-014 |
| new | 집계 이벤트 | AggregationEvent | 상자를 팔레트에 싣거나 내리는 것처럼 상위 객체와 하위 객체의 물리적 결합·분리를 기록하는 EPCIS 이벤트 유형이다. | 7 | ref-013 |
| new | VDA 5050 | VDA 5050 | 독일자동차산업협회(VDA)가 정한 AGV·AMR 과 상위 관제 사이의 통신 인터페이스 권고안이다. | 7, 9 | ref-022 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-003 | GS1 | EPCIS and CBV Linked Data Model | 표준 | medium | https://ref.gs1.org/epcis/ |
| ref-011 | ISO/IEC | ISO/IEC 19987:2024 - Information technology — EPC Information Services (EPCIS) | 표준 | medium | https://www.iso.org/standard/85557.html |
| ref-012 | ISO/IEC | ISO/IEC 19988:2024 - Information technology — GS1 Core Business Vocabulary (CBV) | 표준 | medium | https://www.iso.org/standard/85558.html |
| ref-013 | OpenEPCIS | EPCIS 2.0 and EPCIS 1.2 \| OpenEPCIS Docs | 오픈소스 문서 | medium | https://openepcis.io/docs/epcis/ |
| ref-014 | GS1 | Core Business Vocabulary (CBV) Standard | 표준 | medium | https://ref.gs1.org/standards/cbv/ |
| ref-015 | GS1 | EPCIS and CBV Implementation Guideline | 표준 | medium | https://www.gs1.org/docs/epc/EPCIS_Guideline.pdf |
| ref-016 | GS1 | Serial Shipping Container Code (SSCC) | 표준 | medium | https://www.gs1.org/standards/id-keys/sscc |
| ref-017 | GS1 Korea(대한상공회의소 유통물류진흥원) | SSCC (Serial Shipping Container Code) GS1 Information Vol. 21 | 표준 | medium | http://www.gs1kr.org/front/service/File/SSCC%20%EB%B0%9C%EA%B0%84%20%EC%9E%90%EB%A3%8C.pdf |
| ref-018 | GS1 | GS1 Logistic Label Guideline | 표준 | medium | https://www.gs1.org/docs/tl/GS1_Logistic_Label_Guideline.pdf |
| ref-019 | GS1 | Global Returnable Asset Identifier (GRAI) | 표준 | medium | https://www.gs1.org/standards/id-keys/grai |
| ref-020 | GS1 | Which GS1 identification key should be used for individual assets used to transport goods? (GS1 GO Customer Service Portal) | 표준 | medium | https://support.gs1.org/support/solutions/articles/43000734294-which-gs1-identification-key-should-be-used-for-individual-assets-used-to-transport-goods- |
| ref-021 | GS1 | EPC Tag Data Standard | 표준 | medium | https://www.gs1.org/sites/default/files/docs/epc/GS1_EPC_TDS_i1_11.pdf |
| ref-022 | VDA(Verband der Automobilindustrie) | VDA 5050 Version 2.0.0 — Interface for the communication between automated guided vehicles (AGV) and a master control | 표준 | medium | https://www.vda.de/dam/jcr:f0c9c019-1506-4dee-998a-e92723fbf025/EN-VDA5050-V2_0_0.pdf |
| ref-023 | Open Robotics | Workcells - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/integration_workcells.html |
| ref-024 | Singh, J. 외 | RFID tag readability issues with palletized loads of consumer goods | 논문 | medium | https://onlinelibrary.wiley.com/doi/abs/10.1002/pts.864 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 로봇의 적재·하역 완료 신호(VDA 5050 drop 동작 완료, Open-RMF IngestorResult)를 EPCIS 인계 이벤트로 옮기는 표준 매핑이나 공개 구현 사례가 있는가? | 7, 17, 9 | 열림 | — |
| new | — | 국내 물류센터에서 SSCC 라벨이나 EPCIS 이벤트를 로봇 작업 결과(적재·하역 완료)와 연결해 운영하는 사례가 있는가? | 7, 1 | 열림 | — |
| new | — | 로봇·게이트의 바코드·RFID 판독 실패나 오판독이 생기면 인계 확정을 보류·재스캔·사람 확인 중 어떤 기준으로 처리해야 하는가? | 7, 20 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 출하 | 시작 조건 | docs/categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 7. 화물·재고·자산 식별과 추적 |
| 출하 | 작업 대상 | docs/categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 7. 화물·재고·자산 식별과 추적 |
| 출하 | 수행 자원 | docs/categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 7. 화물·재고·자산 식별과 추적 |
| 출하 | 제약 | docs/categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 7. 화물·재고·자산 식별과 추적 |
| 출하 | 완료·인계 | docs/categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 7. 화물·재고·자산 식별과 추적 |
| 출하 | 예외·성과 | docs/categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 7. 화물·재고·자산 식별과 추적 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| GS1 EPCIS 2.0 (ISO/IEC 19987:2024) | 표준 | ISO/IEC · GS1 | 7 | ref-011 | https://www.iso.org/standard/85557.html |
| GS1 CBV (Core Business Vocabulary) | 표준 | GS1 | 7 | ref-014 | https://ref.gs1.org/standards/cbv/ |
| SSCC (Serial Shipping Container Code) | 표준 | GS1 | 7 | ref-016 | https://www.gs1.org/standards/id-keys/sscc |
| GS1 Logistic Label Guideline | 표준 | GS1 | 7 | ref-018 | https://www.gs1.org/docs/tl/GS1_Logistic_Label_Guideline.pdf |
| GRAI (Global Returnable Asset Identifier) | 표준 | GS1 | 7 | ref-019 | https://www.gs1.org/standards/id-keys/grai |
| GIAI (Global Individual Asset Identifier) | 표준 | GS1 | 7 | ref-020 | https://support.gs1.org/support/solutions/articles/43000734294-which-gs1-identification-key-should-be-used-for-individual-assets-used-to-transport-goods- |
| EPC Tag Data Standard (1.11판) | 표준 | GS1 | 7 | ref-021 | https://www.gs1.org/sites/default/files/docs/epc/GS1_EPC_TDS_i1_11.pdf |
| VDA 5050 (2.0.0) | 표준 | VDA(Verband der Automobilindustrie) | 7, 9 | ref-022 | https://www.vda.de/dam/jcr:f0c9c019-1506-4dee-998a-e92723fbf025/EN-VDA5050-V2_0_0.pdf |
| OpenEPCIS | 오픈소스 | OpenEPCIS | 7 | ref-013 | https://openepcis.io/docs/epcis/ |

## 추가 조사 요청

- 5절 예외·성과·8절: Singh 외(2009, ref-024) 원문 재확인 — 지게차 속도가 판독성에 준 영향(브리프 요약 '거의 영향 없음'과 검증 요약 '느릴수록 좋음'이 상충)과 제품별 판독성 순위를 원문으로 확인해야 한다.
- 4·6·7절: EPC Tag Data Standard 최신판 기준으로 SSCC-96·GRAI-96·GIAI-96 인코딩 정의가 유지되는지 재확인이 필요하다(현재 1.11판 기준).
- 7절: EPCIS 2.0·CBV 2.0 의 GS1 비준 시점(2022년 6월)과 JSON/JSON-LD·REST API 추가를 GS1 원문으로 교차 확인해야 한다(현재 OpenEPCIS 단일 출처라 [추정]).
- 6절: VDA 5050 2.0.0 원문에서 loads 의 weight 필드, '빈 배열 = 적재물 없음', '적재 상태를 판단할 수 없으면 보내지 않음' 규정과 pick·drop actionParameters(loadId) 규정 여부를 확인해야 한다.
- 6절: CBV bizStep 표준 값에 picking 이 있는지 원문으로 확인해야 한다(현재 receiving·putting_away·shipping 만 확인).
- 5절 제약: GS1 Korea 자료의 '같은 데이터 라벨을 두 면에 부착' 권장 여부를 원문으로 확인해야 한다(검증 스니펫 미확인으로 삭제함). 2019-09 자료이므로 최신 안내 여부도 확인이 필요하다.
- 3·5·9절: 로봇 완료 신호(VDA 5050 drop, Open-RMF IngestorResult)와 EPCIS 인계 이벤트를 잇는 1차 자료(표준 매핑·공개 구현)가 필요하다(현재 [추정]).
- 전 절: GS1 계열이 아닌 독립 출처(학술 논문·연구기관)로 핵심 표준 사실을 교차 확인해야 신뢰도를 올릴 수 있다.
- 5·8절: 한국 현장 자료(국토교통부 스마트물류센터 인증 평가 항목, 국내 RFID 자동 검수 논문 등)의 내용 확인이 필요하다(이번 실행은 출처 상한으로 넣지 못함).
- 3·9절: 로봇 플릿과 WMS·MES·ERP 연동·추적 가능한 이벤트 로그의 관계, 그리고 ROP가 인계 결과를 상위 업무 시스템에 되돌리는 방식을 다룬 근거 자료가 필요하다(f18 삭제로 9절 상위 업무 시스템 행은 분류 원문 인용만 둠).

## 이행한 수정 지시

- 모든 각주 접근일 뒤 ' (원문 미열람)' 표기와 source_unopened: true — 13절 각주 15건 전부에 표기를 붙이고 reference_updates 15건 모두에 source_unopened: true 를 넣었으며, ref-003 은 기존 각주 줄(접근일 2026-09-24)을 재사용해 같은 표기를 붙였다.
- ref-025 제외 — reference_updates 와 페이지 각주·프런트매터 sources 어디에도 ref-025 를 넣지 않았다.
- f18 본문 제외 — 3절·8절에 f18 을 쓰지 않았고, 3절은 원문 주석 언급과 f14·f16·f7 의 사실, f19([추정])로만 구성했다.
- f17 강등·구절 삭제 — 5절 예외·성과와 8절에서 [추정]으로 쓰고 지게차 속도·금속 캔 구절을 뺐으며, 실험 조건(도크 도어를 모사한 RFID 포털, 2009년 논문)을 밝히고 원문 재확인을 additional_research_requests 로 넘겼다.
- f6 강등·병기 — 7절 표 아래 문장을 [추정]으로 쓰고 '비준 시점(2022년 6월)은 OpenEPCIS 문서 단일 출처이며 GS1 원문으로 교차 확인하지 못했다'를 병기했다.
- f4 구절 삭제 — 4절 집계 이벤트 항목에서 '분리 전까지 같은 위치' 구절을 빼고 parent·children 결합·분리(케이스를 팔레트에 싣거나 내리는 예)만 [사실]로 썼다.
- f5 축소 — 4절 AssociationEvent 항목에서 '또는 위치'·'(또는 해제)'를 빼고 EPCIS 2.0 도입과 센서를 컨테이너·팔레트 같은 자산에 붙이는 장기 연결 기록만 [사실]로 썼다.
- f8 수정 — 6절에서 bizStep 예시를 receiving·putting_away·shipping 으로 한정하고, 물류 흐름 단계 대응은 별도 문장의 [추정]으로 분리했다(5절 시작 조건도 shipping 만 사용).
- f11 수정 — 두 면 부착 구절을 삭제하고 5절 제약에 'GS1 Korea 자료(2019-09) 기준' 400~800mm 를 밝혔으며, 로봇·고정 스캐너 판독 위치와의 연결은 [추정]으로 분리했다.
- f13 판 명시 — 4절·6절 본문과 7절 표에 'TDS 1.11판'을 적고 각주 제목에도 '(1.11판)'을 붙였으며, 새 판 번호는 쓰지 않고 최신판 재확인을 additional_research_requests 로 넘겼다.
- f14 축소 — 3절·6절·7절에서 loadId(식별 전이면 빈 값 가능)·loadType·loadPosition 만 [사실]로 쓰고 weight·빈 배열·생략 규정은 삭제했으며, 기준 'VDA 5050 2.0.0(2022-01)'을 명시했다.
- f19 표기 — 3절과 5절 완료·인계에서 [추정]을 유지하고 같은 문장 뒤에 '위 사실에서 도출한 추론이며 두 계층을 잇는 표준 매핑은 확인되지 않았다'를 밝혔고, 6절에도 결합이 추론 단계임을 적었다.
- 9절 경계 — 바코드·RFID 판독(f20)과 RFID 포털 판독 성능(f17)을 '연계 대상:'으로 짧게 두고, ROP 직접 범위를 식별 결과의 수신·대조·기록([추정])으로 한정해 분류 원문 9장 경계에 맞췄다.
- ref-011 발행일 — 13절 각주와 reference_updates 의 published 를 2024-03 으로 적었다.
- 2차: 7절 f6 — 표 아래 두 문장을 한 문장으로 합쳐 [추정][^ref-013]으로 끝냈고, 비준 시점이 OpenEPCIS 문서 단일 출처이며 GS1 원문으로 교차 확인하지 못했다는 병기를 같은 문장 안에 두었다.
- 2차: 6절 '로봇 관제 인터페이스의 적재 보고' 마지막 문장('두 인터페이스 모두 행동 완료를 알리며, 인계 이벤트와의 결합은 3절의 추론 단계에 머문다.') 끝에 [추정][^ref-022][^ref-023]을 붙였다.
- 2차: 9절 '시설·설비 제어' 행 — '적재·하역 설비와 요청·결과를 주고받아 완료를 확인'을 [추정][^ref-023]으로 떼고, [사실][^ref-023]은 괄호 안 Open-RMF 요청·결과 메시지 문장에만 붙였다.
- 2차: 9절 '상위 업무 시스템' 행 — 근거 없는 '인계가 확정된 화물 식별자·위치를 업무 시스템에 되돌림'을 지우고 분류 원문 9장 셀 문구 "주문·납기·재고 제약을 받아 실행하고 결과 반영"(외부 연계 칸은 "수요예측, 구매, 재무, 전사 재고정책")을 따옴표로 인용했으며 원문 셀에 없는 구체 내용은 덧붙이지 않았다. 표 아래 문단의 같은 인용 문장은 중복이라 뺐다.
- 2차: 3절 약어 — 'VDA 5050'을 '독일자동차산업협회(Verband der Automobilindustrie, VDA)의 VDA 5050'으로, 'Open-RMF'를 'Open-RMF(Open Robotics Middleware Framework)'로 풀어 쓰고 용어집 open-rmf.md 링크를 3절 첫 등장 위치로 옮겼다(6절의 링크는 뺌). 3절에 처음 나오는 EPCIS 도 풀어 썼다.
- 2차: 분량 — 방법 (a)로 3절 중복 설명, 4절 목록 문장, 5절 표·서술, 6절 문장, 7절 표(식별 키 세 행을 한 행으로 합치고 출처 칸을 '원문 미열람'으로 축약), 8절(Open Robotics 항목 삭제), 9절 표 아래 문단, 10절 연결 문장을 줄여 3~11절을 약 4,000자 이내로 맞췄다(추정치이며 정확한 글자 수는 퍼블리셔 분량 검사로 확인 필요). 브리프 밖 내용은 넣지 않았고 태그·각주·1차 처분을 그대로 유지했다.
