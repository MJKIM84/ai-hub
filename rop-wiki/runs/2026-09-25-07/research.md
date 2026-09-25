# 리서치 브리프 2026-09-25-07

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-07 |
| 날짜 | 2026-09-25 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 7. 화물·재고·자산 식별과 추적 |
| 대분류 | B. 공통 정보·환경 모델 |

## 갭(비어 있거나 약한 섹션)

- corr-001: 섹션 7. 관련 표준·프레임워크·오픈소스 — VDA 5050 행이 2.0.0만 적고 현행판(3.0.0)이 없으며, 공식 저장소 원문을 열 수 있는데도 '원문 미열람'으로 표시됨
- corr-002: 섹션 1. 한 줄 정의 — 분류원문 문장의 수정 요청(정정 대상 아님, 반영하지 않을 근거 필요)
- 섹션 11. 열린 질문 — oq-007(3.0.0 loadId 형식 규정)의 근거가 3.0.0 상태 스키마로 재확인되지 않음
- 용어집 VDA 5050 항목의 한 줄 정의가 팩트시트(factsheet) 메시지 정의로 되어 있고 현행판 표시 없음(대상 페이지 밖, 갱신 후보)

## 조사 질문

1. 로봇은 도착했는데 실제로 어떤 팔레트가 인계됐는가? [분류원문]
2. corr-001 VDA 5050의 현행판은 무엇이며, 적재물 보고(state 메시지의 loads 배열과 loadId)가 3.0.0에도 유지되는가? (섹션 7 겨냥)
3. corr-001 공식 저장소의 2.0.0 태그·main 원문을 열면 7절 VDA 5050 행의 '원문 미열람' 표시를 어떻게 바꿔야 하는가? (섹션 7 겨냥)
4. corr-002 한 줄 정의에 바코드·RFID 식별 수단을 넣어 달라는 요청은 분류원문 보호 규칙에 비추어 반영 가능한가, 식별 수단은 페이지 어디에서 이미 다루는가? (섹션 1·4·6 겨냥)
5. oq-007 VDA 5050 3.0.0에서 loadId의 형식(SSCC 같은 GS1 키)을 정하거나 제약하는 규정이 있는가? (섹션 11 겨냥)
6. oq-005 VDA 5050 3.0.0의 발행 시점은 언제인가? (섹션 7 현행판 표기 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | corr-001 관련: VDA 5050 공식 GitHub 저장소 main 브랜치의 명세 제목은 'Version 3.0.0'이며, 저장소 README는 main 브랜치가 최신 발행판(현재 3.0.0)을 담는다고 밝힌다. | ref-031, ref-052 | 아니오 | medium | 2026-09-25 | — | — |
| f2 | [사실] | corr-001 관련: VDA 5050 3.0.0(main)의 state 스키마에도 선택 배열 loads가 있으며 loadId(바코드·RFID 등 고유 식별 번호, 식별 가능하나 아직 식별 전이면 빈 값), loadType, loadPosition, weight(kg), boundingBoxReference, loadDimensions를 담고, 로봇이 적재 상태를 판단할 수 없으면 배열을 생략한다. | ref-051 | 아니오 | medium | 2026-09-25 | 작업 대상 | — |
| f3 | [사실] | corr-001 관련: VDA 5050 공식 저장소 2.0.0 태그의 명세 마크다운은 머리에 'Version 2.0.0 RELEASE CANDIDATE, FOR REVIEW' 문구를 두고, state 메시지의 선택 배열 loads와 loadId·loadType·loadPosition·weight를 3.0.0과 같은 의미로 정의한다. | ref-022 | 아니오 | medium | 2022-01 | 작업 대상 | 원문 미열람 |
| f4 | [사실] | corr-001 관련: VDA 5050 3.0.0 명세는 pick 완료를 '적재물이 이동로봇에 들어오고 새 적재 상태를 보고함', drop 완료를 '적재물이 이동로봇을 떠나고 새 적재 상태를 보고함'으로 정의하고, 두 동작의 선택 파라미터로 lhd·stationType·stationName·loadType·loadId를 둔다. | ref-031 | 아니오 | medium | 2026-09-25 | 출하 / 완료·인계 | — |
| f5 | [사실] | VDA는 2026년에 VDA 5050 3.0판을 발표해 자율도가 높은 이동로봇 통합을 위한 구역(zone) 개념 등을 더했으며, 정확한 발행일(2026-03-19 대 보도자료 2026-04 계열)은 여전히 확인되지 않았다. | ref-032, ref-052 | 아니오 | medium | 2026 | — | — |
| f6 | [의견] | corr-001 관련: 7절 VDA 5050 행은 현행판 3.0.0(공식 저장소 main 명세·state 스키마)과 2.0.0을 함께 적고, 열람 표시를 '공식 저장소 원문 확인(2.0.0은 태그의 RELEASE CANDIDATE 마크다운이며 VDA 게시 PDF와 일치 미확인)'으로 바꾸며, 적재물 식별 보고가 두 판 모두에 있다고 적는 것이 근거와 맞다. | ref-022, ref-031, ref-051 | 아니오 | medium | 2026-09-25 | — | — |
| f7 | [추정] | 이번 실행에서 연 VDA 5050 3.0.0 state 스키마의 loadId 설명은 형식을 바코드·RFID 예시로만 들 뿐 SSCC 같은 GS1 키를 지정하거나 제약하지 않으며, 식별 결과가 지시한 loadId와 다를 때의 보고 규칙은 열람 범위에서 확인되지 않았다. | ref-051, ref-031 | 아니오 | low | 2026-09-25 | 작업 대상 | — |
| f8 | [의견] | corr-002 관련: 한 줄 정의 문장은 분류원문이라 정정 대상이 아니므로 반영하지 않으며, 요청이 말한 식별 수단(GS1-128 바코드로 표시하는 SSCC, RFID 태그용 EPC 인코딩)은 정의를 바꾸지 않고도 이미 4절·6절에서 출처와 함께 다루고 있다. | ref-018, ref-021 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |

### 근거 발췌

- **f1**: corr-001 관련: README 원문 "The main branch contains the latest published version of VDA 5050 (currently version 3.0.0)." 명세 main 머리 제목 Version 3.0.0. 두 파일 모두 같은 저장소(같은 발행 주체)라 독립 교차 아님. (발행일 미확인, 확인일 기준)
- **f2**: corr-001 관련: state.schema(main) loads 설명 "If mobile robot cannot determine load state, leave the array out of the state." loadId 는 e.g., barcode or RFID. 2.0.0의 AGV 가 mobile robot 으로 바뀐 것 외에 필드 의미는 같다. (발행일 미확인, 확인일 기준)
- **f3**: corr-001 관련: 2.0.0 태그 원문 loads "Optional: If AGV cannot determine load state, leave the array out of the state." 머리말에 RELEASE CANDIDATE 문구가 있어 VDA 게시 PDF(2022-01)와 글자 단위 일치는 미확인.
- **f4**: corr-001 관련: 3.0.0 main 6.2.3 사전 정의 action 표: drop "Load has left the mobile robot and mobile robot reports new load state." loadId (string, optional). (발행일 미확인, 확인일 기준)
- **f5**: 검색 요약: VDA 보도자료 제목 'Version 3.0 of VDA 5050 released'(URL 260421 계열), 검색 요약은 발표일을 2026-03-19로 전함. README 는 3.0.0 을 최신 발행판으로 적음. 발행일 불일치는 oq-005 로 유지.
- **f6**: corr-001 관련: f1~f4 에서 도출한 반영 제안. 3.0.0 state.schema 와 2.0.0 태그 명세 모두 loads·loadId 를 정의함을 이번 실행에서 원문으로 확인.
- **f7**: state.schema(main) loadId 설명에 형식 규정 없음. 명세 마크다운은 열람 도구가 7장(메시지 명세) 앞에서 잘려 불일치 처리 규정 존재 여부를 확인하지 못함. 부재 확인이 아님. (발행일 미확인, 확인일 기준)
- **f8**: corr-002 관련: 공통 규칙 1(분류 원문 정의 변경 금지)과 정정 요청함 안내('분류 원문의 명칭·번호·정의·질문은 정정 대상이 아니다')가 근거. GS1-128·AI 00(ref-018), EPC TDS 1.11 RFID 인코딩(ref-021)은 페이지 4·6절에 이미 있음. '실시간으로' 추가도 원문에 없는 내용.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-022 | VDA(Verband der Automobilindustrie) | VDA 5050 Version 2.0.0 — Interface for the communication between automated guided vehicles (AGV) and a master control | 2022-01 | 표준 | medium | 2026-09-25 | https://www.vda.de/dam/jcr:f0c9c019-1506-4dee-998a-e92723fbf025/EN-VDA5050-V2_0_0.pdf | 예 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-032 | VDA(Verband der Automobilindustrie) | Version 3.0 of VDA 5050 released | 2026-04 | 표준 | medium | 2026-09-25 | https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN | 예 |
| ref-018 | GS1 | GS1 Logistic Label Guideline | 미확인 | 표준 | medium | 2026-09-25 | https://www.gs1.org/docs/tl/GS1_Logistic_Label_Guideline.pdf | 예 |
| ref-021 | GS1 | EPC Tag Data Standard | 미확인 | 표준 | medium | 2026-09-25 | https://www.gs1.org/sites/default/files/docs/epc/GS1_EPC_TDS_i1_11.pdf | 예 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 아니오 |
| ref-052 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — README.md | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/README.md | 아니오 |

### 출처 요약

- **ref-022**: AGV·AMR 과 상위 관제 간 통신 권고안. order·state 메시지, pick/drop action, 적재물(loads) 보고 필드를 정의. 이번 실행은 공식 저장소 2.0.0 태그 마크다운(머리말 RELEASE CANDIDATE 문구)을 읽었으며 VDA 게시 PDF 와 글자 단위 일치는 미확인.
- **ref-031**: VDA 5050 공식 명세의 GitHub 저장소 본문(현재 main 은 3.0.0 판). pick·drop 동작 정의와 파라미터를 확인했다. 열람 도구 응답이 7장 앞에서 잘렸다.
- **ref-032**: 원문 미열람. 발행 기관의 VDA 5050 3.0 발행 보도자료. 구역 개념 등 자율도 높은 이동로봇 지원 확장을 소개.
- **ref-018**: 원문 미열람. SSCC 를 필수로 담는 GS1 물류 라벨의 구성·바코드·부착 규칙 가이드라인.
- **ref-021**: 원문 미열람. GS1 키를 RFID 태그의 EPC 로 인코딩하는 방식(SSCC-96, GRAI-96 등)을 정의한 GS1 표준(1.11판).
- **ref-051**: VDA 5050 공식 저장소 main(3.0.0)의 state 메시지 JSON 스키마. 선택 배열 loads 와 loadId·loadType·loadPosition·weight·boundingBoxReference·loadDimensions 의 설명을 담는다.
- **ref-052**: VDA 5050 공식 저장소 README. main 브랜치가 최신 발행판(현재 3.0.0)을 담는다고 밝히고 판 번호 규칙과 VDA 공식 문서 위치를 안내한다.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/b-common-information-and-environment-model/07-cargo-inventory-and-asset-identification-and-tracking.md | 7, 11 | corr-001 반영: f1·f2·f3·f4·f6 을 섹션 7 VDA 5050 행에(현행판 3.0.0 과 2.0.0 병기, 적재물 식별 보고가 두 판 모두에 있음, 열람 표시를 공식 저장소 원문 확인으로 교체하되 2.0.0 은 RELEASE CANDIDATE 태그 마크다운이라 게시 PDF 일치 미확인 명시, 각주 ref-031·ref-051 추가) / f5 는 현행판 표기 근거(발행일은 oq-005 로 미확인 유지) / f7 을 섹션 11 oq-007 항목 보강에(3.0.0 state 스키마 loadId 설명에 GS1 키 형식 규정 없음, 불일치 보고 규칙 미확인). corr-002 는 반영하지 않음: f8(분류원문 정의는 정정 대상 아님, 식별 수단은 4·6절에 이미 있음) — 섹션 1 변경 없음 |
| update | docs/glossary/vda-5050.md | — | 다음 실행 후보 겸 갱신 제안: 용어집의 VDA 5050 한 줄 정의가 팩트시트 메시지 정의('차량이 자신의 기능 정보를 상위 관제에 미리 알리는 메시지')로 되어 있어 규격 자체 정의(AGV·이동로봇과 상위 관제 사이 통신 인터페이스)와 맞지 않음. f1·f5 로 현행판 3.0.0 표기 추가 |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- 없음

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 7 · 교차 확인: 0
- 예산 사용량: 검색 2회 · 신규 출처 2건
- 미확인 항목:
    - f7 VDA 5050 3.0.0 명세 마크다운의 7장(메시지 명세) 이후는 열람 도구 응답이 잘려 loadId 불일치 보고 규정 존재 여부 미확인
    - 이전 실행 2026-09-25-03 f12 의 3.0.0 loadId 문구('Set by fleet control or mobile robot ...')는 이번에 잘린 응답 범위에서 다시 찾지 못함 — 3.0.0 state 스키마 설명은 '바코드·RFID 예시'로 2.0.0 과 같음. 두 문구가 서로 다른 위치(action 파라미터 설명 대 state 필드 설명)에 있는지 확인 필요
    - f3 2.0.0 태그 마크다운과 VDA 게시 PDF(ref-022 URL)의 글자 단위 일치 미확인
    - f5 VDA 5050 3.0.0 정확한 발행일(2026-03-19 대 2026-04 보도자료) 미확인 — oq-005 유지
    - ref-031·ref-051·ref-052 발행일 미확인
- 범위 경계 위반 의심:
    - 없음
- 한계: fetch_mode mirror_only: VDA 5050 공식 저장소 raw 원문(main 명세·README·state.schema, 2.0.0 태그 명세)을 열었고 VDA 게시 PDF·보도자료·GS1 페이지는 열지 못했다(ref-032·ref-018·ref-021 원문 미열람). 모든 근거가 같은 발행 주체(VDA/VDMA 또는 GS1)의 산출물이라 교차 확인 0건, finding 신뢰도 상한 medium. 갱신 실행이라 정정 요청 2건과 그에 걸린 열린 질문(oq-005, oq-007)만 차등 조사했다. corr-001: 반영 근거 f1~f6. corr-002: 반영하지 않을 근거 f8(분류원문 정의 보호). 검색 2회/30(한·영 각 1회), 신규 출처 2건/15(ref-051, ref-052), 재사용 5건(ref-022, ref-031, ref-032, ref-018, ref-021). oq-005·oq-007 은 해결하지 못해 해결 제안 없음. 용어집 VDA 5050 항목 정의 불일치를 발견해 갱신 제안으로 올렸다. 27. AI·학습·적응과 모델 운영 관련 finding 없음. 바코드·RFID 판독 자체는 연계 대상이라 다루지 않았다.
