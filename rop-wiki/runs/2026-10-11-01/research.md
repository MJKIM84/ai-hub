# 리서치 브리프 2026-10-11-01

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-11-01 |
| 날짜 | 2026-10-11 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 21. 상호운용 표준·적합성 |
| 대분류 | F. 연동 |

## 갭(비어 있거나 약한 섹션)

- 섹션 5. 적용 사례 (현장 유형 명시) — 수행 자원 칸이 'VDA 5050 3.0.0 에서 주문 배정·경로 계산…은 관제 쪽'으로 경로 계산을 모든 로봇에 일반화함(원문은 선 유도 로봇). 물류창고 외 현장 유형 사례 없음
- 섹션 6. 대표 접근법과 기술(주제 페이지로 분리) — '제조사가 자체 인증하거나' 문장의 근거 없음(정정 필요). 선택 필드·재전송·취소 후 갱신을 확인하는 동작 시험 방법 없음. OTTO 인증 발표 각주가 원문 미열람
- 섹션 7. 관련 표준·프레임워크·오픈소스(주제 페이지로 분리) — VDA 5050 행 발행일 표기, MassRobotics 행 '원문 미열람', OPC 행 '자체·독립 시험소 인증' 표현. 3.0.0 태그 스키마 끝 쉼표, OPC UA Robotics 서버 Facet, KS B ISO 22166-202 미반영. 트랙 반영 제안(2026-10-09-26, 건축 도면 자동 인식 단계 2: IDS 1.0 을 BIM 데이터 교환 요구·적합성 검사 수단으로) 미처리
- 섹션 8. 대표 연구와 자료 — vda5050-lab 원문 미열람 표시, VDA 5050 통신 평가 논문 없음
- 섹션 10. 다른 연구영역과의 연결 — 42. 분산 시스템·통신·컴퓨팅 구조, 14. 도면·BIM에서 지도 만들기 연결 없음
- 섹션 11. 열린 질문 — oq-005·oq-055·oq-091·oq-026 부분 근거 미반영
- 정정 요청 없음

## 조사 질문

1. 어떤 상호운용 표준을 따르고, 제조사가 그 표준을 지키는지 어떻게 확인할 것인가? [분류원문]
2. oq-005 VDA 5050 3.0.0 의 날짜는 공식 저장소 명세·카탈로그·보도자료·참여 업체 발표에서 각각 무엇으로 표시되는가? (섹션 7·11 겨냥)
3. oq-055 VDA 5050 에 공식 적합성 시험·인증 절차가 있는가, 없다면 제3자 도구·벤더 간 인증·전시 시연·인정 시험소 인증을 연동 승인 근거로 어떻게 구분해 쓸 수 있는가? (섹션 6·8·11 겨냥)
4. oq-091 VDA 5050 3.0.0 태그의 JSON 스키마를 시험 입력으로 그대로 쓸 수 있는가? (섹션 7·11 겨냥)
5. oq-026 KS B 7321-2 와 KS B ISO 22166-202 는 국가표준 목록에서 무엇으로 확인되는가? TTAK.KO-10.1295-Part8 은 공식 목록에서 확인되는가? (섹션 7·11 겨냥, 한국 자료 우선)
6. 트랙 반영 제안 2026-10-09-26: IDS 1.0(buildingSMART)의 적용 대상·요구 구조·패싯·값 제한은 발행 기관 자료로 무엇이며, 21. 상호운용 표준·적합성의 적합성 검사 수단으로 볼 수 있는가? (섹션 7·10 겨냥)
7. 기존 문장 점검: VDA 5050 3.0.0 은 경로 계산을 어느 로봇에 대해 관제 책임으로 두는가, OPC Foundation 은 제조사 자체 인증을 허용하는가? (섹션 5·6·7 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA5050 공식 저장소의 3.0.0 명세 마크다운 표지는 판을 'Version 3.0.0'으로만 적고 날짜를 적지 않으며, VDA 가 배포하는 PDF 표지의 날짜 표기는 이번 실행에서 PDF 본문 텍스트를 읽지 못해 확인하지 못했다. | ref-031 | 아니오 | medium | 2026-10-11 | — | — |
| f2 | [의견] | 구축자 의견: 21번 7절 표 VDA 5050 행의 발행일은 단일 날짜로 확정하지 않고 '미확인'을 유지하되, VDA 카탈로그 표시일(2026-03-17)과 보도자료 날짜(2026-04-20)가 서로 다르다는 점은 20번 주제 페이지의 날짜 절로 연결하고, PDF 표지의 'March 2026' 표기는 원문 확인 전까지 [추정]으로 두는 것이 맞다. | ref-1412, ref-032, ref-031 | 아니오 | medium | 2026-10-11 | — | — |
| f3 | [사실] | VDA 5050 3.0.0 §5.3 의 관제 기능 목록은 경로 계산을 일반 기능이 아니라 선 유도(line-guided) 이동로봇의 경로 계산·안내로 적고, §5.4 는 이동로봇 기능을 선 유도형과 자유 주행형(freely navigating)의 경로 실행으로 나눠 서술한다. | ref-031 | 아니오 | medium | 2026-10-11 | — | — |
| f4 | [사실] | VDA 의 3.0 발표 보도자료는 자율도가 높은 이동로봇이 지정된 경유점 사이 경로를 스스로 계획해 상세 경로 계획이 로봇에서 이뤄지고, 그 경로를 경로 공유(path sharing)로 중앙 관제와 공유하는 구성을 설명한다. | ref-032 | 아니오 | medium | 2026-04-20 | — | — |
| f5 | [의견] | 구축자 의견: 21번 본문 5절 수행 자원 칸과 분리 7절 본문의 '주문 배정·경로 계산·…은 관제 쪽' 문장은 '선 유도 로봇의 경로 계산·안내'로 고치고, 자유 주행 로봇은 상세 경로를 스스로 계획해 공유할 수 있음을 병기해 모든 이동로봇의 상세 경로를 관제가 계산한다고 일반화하지 않는 것이 맞다. | ref-031, ref-032 | 아니오 | medium | 2026-10-11 | — | — |
| f6 | [사실] | VDA 5050 3.0.0 §7.1.1 은 로봇이 받은 선택(optional) 필드를 무시해서는 안 되고 쓸 수 없으면 UNSUPPORTED_PARAMETER(CRITICAL)로 알리게 하며, 관제(fleet control)에는 로봇이 지원하는 선택 필드만 보내도록 의무를 둔다. | ref-031 | 아니오 | medium | 2026-10-11 | — | — |
| f7 | [사실] | VDA 5050 3.0.0 은 연동 시험의 기대값으로 쓸 응답을 조항으로 정한다: 지원하지 않는 선택 파라미터가 든 주문은 UNSUPPORTED_PARAMETER(CRITICAL)로 거절, 같은 orderUpdateId 재전송은 내용이 같으면 무시하고 다르면 SAME_ORDER_UPDATE_ID(WARNING)를 보고하며 이전 주문을 계속, 취소된 주문의 후속 갱신은 ORDER_UPDATE_FOLLOWING_CANCEL(WARNING). | ref-031 | 아니오 | medium | 2026-10-11 | — | — |
| f8 | [의견] | 구축자 의견: 로봇 연동 승인에는 버전 문자열 확인에 더해 (1) 미지원 선택 필드 주문 거절, (2) 같은 번호·같은 내용 재전송 무시, (3) 같은 번호·다른 내용 재전송 경고, (4) 취소 후 갱신 경고, (5) 관제가 로봇 factsheet 가 지원한다고 밝힌 선택 필드만 보내는지를 확인하는 동작 시험표를 두고, 수신 직전 주문 상태와 관측 로그 누락 여부를 함께 보존하는 것이 좋다. | ref-031 | 아니오 | medium | 2026-10-11 | — | — |
| f9 | [사실] | VDA5050 공식 저장소 3.0.0 태그의 json_schemas/order.schema·factsheet.schema·visualization.schema 에는 닫는 괄호 바로 앞에 쉼표가 오는 끝 쉼표(trailing comma)가 있어 엄격한 JSON 으로 읽히지 않으며, main 브랜치의 order.schema 는 같은 자리(궤적 제어점 weight 속성)에 끝 쉼표가 없다. | ref-1430, ref-1431, ref-1432, ref-413 | 아니오 | medium | 2026-10-11 | — | — |
| f12 | [의견] | 구축자 의견: VDA 5050 3.0.0 을 시험 입력으로 쓸 때는 '공식 태그'와 '파싱 가능한 시험 입력'을 따로 확인하고, 수정한 스키마를 쓰면 원본과의 차이·수정 근거·해시를 보존하며 main 브랜치 내용을 설명 없이 섞지 않는 것이 좋다. | ref-1430, ref-413 | 아니오 | medium | 2026-10-11 | — | — |
| f13 | [사실] | vda5050-lab README(커밋 4a1a812)는 현재 판 v0.2.0 을 개발자 프리뷰(Developer Preview)로 부르며 오프라인 진단 구현과 범위가 제한된 합성 시연을 담는다고 설명하고, 공개 알파나 인증 주장이 아니며 실제 고객 기록·외부 시험 대상(DUT)·실물 하드웨어 실행을 검증하지 않았다고 밝힌다. | ref-408 | 아니오 | medium | 2026-10-11 | — | — |
| f14 | [의견] | 구축자 의견: vda5050-lab 은 MQTT 기록 진단의 보조 도구 후보로만 두고, 그 판정을 구매·연동 승인 전체의 대체물로 쓰지 않는 것이 맞다. | ref-408 | 아니오 | medium | 2026-10-11 | — | — |
| f15 | [사실] | OPC Foundation 'How to Certify' 는 제조사가 인증 시험 전에 가능한 많은 시험을 미리 해 보도록 권고하고, 재단이 제공하는 적합성 시험 도구(compliance test tools)는 시험소가 시험에 쓰는 도구라고 설명한다. | ref-705 | 아니오 | medium | 2026-10-11 | — | — |
| f16 | [사실] | OPC Foundation 인증 개요 페이지는 인증 제품이 재단이 인정한 인증 시험소에서 시험을 거쳤다고 설명하고, 인증된 SDK 를 쓴 응용도 공식 인증 제품이 되려면 각자 인증 시험을 받아야 한다고 밝힌다. | ref-1434 | 아니오 | medium | 2026-10-11 | — | — |
| f17 | [사실] | 확인한 OPC Foundation 인증 안내 두 페이지에는 제조사가 스스로 인증하는(self-certification) 경로가 없으므로, 21번 분리 6절의 '제조사가 자체 인증하거나'와 분리 7절 표 OPC 행의 '자체·독립 시험소 인증'은 이 두 출처로 뒷받침되지 않는 표현이다. | ref-705, ref-1434 | 아니오 | medium | 2026-10-11 | — | — |
| f18 | [의견] | 구축자 의견: OPC 적합성 체계는 '제조사의 적합성 시험 도구 사전 점검(권고)'과 '인정 시험소 인증'을 구분하는 문장으로 고치고, 이 구조를 VDA 5050 의 인증 체계로 그대로 옮겨 쓰지 않는 것이 맞다. | ref-705, ref-1434 | 아니오 | medium | 2026-10-11 | — | — |
| f19 | [사실] | MassRobotics AMR_Interop_Standard.json(커밋 f9357a4)의 최상위 oneOf 는 identityReport 와 statusReport 두 정의만 참조하고, 위치(location) 정의는 x·y·angle·planarDatum 네 필드를 모두 필수로 두며, 명령·주문·작업 메시지 정의는 없다. | ref-230 | 아니오 | medium | 2026-10-11 | — | — |
| f20 | [의견] | 구축자 의견: MassRobotics 보고 메시지(신원·상태) 교환만으로 작업 명령 호환성이나 좌표계 정합을 확보했다고 주장하지 않는 것이 맞다. | ref-230 | 아니오 | medium | 2026-10-11 | — | — |
| f21 | [사실] | OPC 40010-1(OPC UA for Robotics Part 1) 1.02판 §11.2.2 는 서버 기능 묶음(Facet)을 기본(Base)·운전(MDS Operation)·자산관리 확장(AM Extended)·상태감시 확장(CM Extended) 넷으로 나누고, 표 124~127 에서 각 적합성 단위를 필수(M)·선택(O)으로 구분한다. | ref-034 | 아니오 | medium | 2025-09-08 | — | — |
| f22 | [의견] | 구축자 의견: 연동 요구에는 'OPC UA 지원' 대신 OPC UA Robotics 판·서버 Facet·선택 단위·인증 범위를 적게 하고, 이 정보모델을 VDA 5050 주문 스키마와 일대일로 자동 변환할 수 있다고 보지 않는 것이 좋다. | ref-034 | 아니오 | medium | 2026-10-11 | — | — |
| f24 | [사실] | 국가표준인증통합정보시스템(KSSN) 상세 페이지에는 KS B 7321-2 '로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델'이 실려 있으나, 이번 열람에서는 번호와 제목만 보였고 제정일·국제표준 부합화·고시 정보는 보이지 않았다. | ref-138 | 아니오 | medium | 2026-10-11 | — | — |
| f25 | [사실] | KSSN 상세 페이지에는 KS B 7321-2 와 별도로 KS B ISO 22166-202 '로봇 — 서비스 로봇의 모듈화 — 제202부: 소프트웨어 모듈용 정보 모델'이 실려 있으나, 제정일·부합화 수준(IDT 여부)·고시 정보는 이번 열람에서 보이지 않았다. | ref-1435 | 아니오 | medium | 2026-10-11 | — | — |
| f26 | [의견] | 구축자 의견: oq-026 은 열림을 유지하고, KS B ISO 22166-202 가 국가표준 목록에 따로 있다는 점만 확인할 거리로 남기며, 그 제정일·부합화 수준과 KS B 7321-2 와의 대체 관계, 국내 적용 사례는 미확인으로 둔다. | ref-138, ref-1435 | 아니오 | low | 2026-10-11 | — | — |
| f30 | [추정] | OTTO by Rockwell Automation 은 2026-04-09 보도자료에서 OTTO 100·600·1200·1500 이 Idealworks·NAiSE·SYNAOS 등 VDA 5050 관제 소프트웨어 업체와 인증을 마쳤다고 밝혔으나, 시험한 프로토콜 판·시험 항목·시험 기관은 밝히지 않는다. | ref-608 | 아니오 | low | 2026-04-09 | — | 벤더 주장 |
| f31 | [사실] | VDMA 의 Mesh-Up 2025 안내는 automatica 2025(뮌헨, 2025-06-24~27) 전시장에서 9개 기업이 참여하고 MHP 가 상위 관제를 맡아, 여러 이동로봇이 작업대를 공급하는 양식화한 생산 라인을 보여 주는 혼합 플릿 시연(전시 시연이며 실제 공장 배치가 아님)을 설명한다. | ref-1436 | 아니오 | medium | 2026-10-11 | 제조 공장 / 수행 자원 | — |
| f32 | [사실] | 같은 Mesh-Up 2025 안내(automatica 2025 전시 시연, 실제 공장 배치 아님)는 관제 소프트웨어 공급자를 바꿔 고를 수 있는 점을 전시장에서 실시간으로 시연하지는 않는다고 밝힌다. | ref-1436 | 아니오 | medium | 2026-10-11 | 제조 공장 / 예외·성과 | — |
| f33 | [의견] | 구축자 의견: Mesh-Up 같은 전시 시연은 5절 '제조 공장' 현장 유형의 혼합 플릿 구성 예로만 쓰고 표 머리와 각 칸에 'automatica 2025 전시 시연, 실제 공장 배치 아님'을 밝히며, 실제 도입 사례나 현장 관제 교체가 검증된 근거로 세지 않는 것이 맞다. | ref-1436 | 아니오 | medium | 2026-10-11 | 제조 공장 | — |
| f34 | [사실] | Wagner 외(제22회 IEEE WFCS 2026)는 표준이 원격 조작(teleoperation)을 기본으로 다루지 않는다고 보고 VDA 5050 원격 조작 확장과 재현 평가용 VDA 5050 트래픽 생성기를 제안하며, VDA 5050 메시지·미들웨어 전송·Open RAN 무선 링크를 잇는 구성에서 지연과 통신 오버헤드를 평가한다. | ref-1437 | 아니오 | medium | 2026-04 | — | — |
| f36 | [사실] | TU Dortmund 통신망 연구실의 논문 소개(2026-04-24)는 이 평가가 재현성 높은 가상 무선(virtual-radio) 시험대와 실제 무선(over-the-air) 검증 구성을 함께 썼다고 설명하며, 정량 결과와 로봇 대수는 소개문에 없다. | ref-1438 | 아니오 | medium | 2026-04-24 | — | — |
| f37 | [의견] | 구축자 의견: 21번에서는 Wagner 외 연구를 VDA 5050 통신 부하·지연 평가로 소개하되 적합성 시험과 구별하고, 상세 네트워크 설계는 42. 분산 시스템·통신·컴퓨팅 구조 연결로만 두는 것이 맞다. | ref-1437, ref-1438 | 아니오 | medium | 2026-10-11 | — | — |
| f38 | [의견] | 구축자 의견: VDA 5050 연동 승인의 근거는 제3자 도구의 자체 진단, 벤더 간 인증 발표, 전시 시연, 인정 시험소 인증을 서로 다른 근거 수준으로 나눠 기록하는 것이 맞다. | ref-408, ref-608, ref-1436, ref-705, ref-1434 | 아니오 | medium | 2026-10-11 | — | — |
| f39 | [추정] | VDA 5050 작업반 참여 업체인 Idealworks 는 2026년 3월 소식 글에서 VDMA·VDA 가 2월 17일 3.0.0 판을 정식 채택했고 이어 법적 승인 절차를 거쳤다고 적어, VDA 공식 자료의 날짜 표시(카탈로그 2026-03-17·보도자료 2026-04-20)와 또 다른 날짜를 제시한다. | ref-1442 | 아니오 | low | 2026-03 | — | — |
| f40 | [사실] | buildingSMART 는 정보 전달 명세(Information Delivery Specification, IDS)를 2024-06-01 승인된 공식 표준으로 소개하고, 데이터 요구를 기계가 읽을 수 있게 기술해 IFC 모델의 적합성을 자동으로 검사할 수 있게 한다고 설명하며, 1.0 이전 판은 공식 표준이 아니라고 밝힌다. | ref-1439 | 아니오 | medium | 2024-06-01 | — | — |
| f41 | [사실] | IDS 공식 사용자 설명서는 IDS 파일이 하나 이상의 명세(specification)로 이루어지고 각 명세가 적용 대상(applicability)과 요구(requirements)를 가지며, 둘 다 엔터티·속성(attribute)·분류·속성 값(property)·재료·소속(partOf) 패싯으로 구성되고, 받는 쪽이 IDS 와 IFC 를 함께 불러 검사해 불일치 보고를 얻는다고 설명한다. | ref-1362 | 아니오 | medium | 2026-10-11 | — | — |
| f42 | [사실] | IDS 사용자 설명서는 패싯 파라미터에 단순 값 대신 열거(enumeration)·패턴(pattern)·범위(bounds)·길이(length)의 복합 제한을 걸 수 있다고 설명한다. | ref-1365 | 아니오 | medium | 2026-10-11 | — | — |
| f43 | [사실] | IDS 공식 저장소의 문서 안내는 소프트웨어 구현의 IDS 읽기·검사 기능이 올바른지 확인하기 위한 .ids·.ifc 쌍 250개 이상의 시험 파일 묶음을 TestCases 폴더에 둔다고 설명한다. | ref-1443 | 아니오 | medium | 2026-10-11 | — | — |
| f44 | [의견] | 구축자 의견: 21번 7절에는 IDS 1.0 을 '건물 정보 모델(IFC) 데이터 교환 요구의 적합성 검사 수단'으로 짧게 두고, 검사 도구 자체도 공식 시험 파일 묶음으로 확인할 수 있다는 점을 적되, 로봇–관제 메시지 적합성 시험과는 구별하며, 로봇 지도용 BIM 객체·속성 요구의 세부는 14. 도면·BIM에서 지도 만들기와 건축 도면 자동 인식 트랙에 두는 것이 맞다. | ref-1439, ref-1362, ref-1443 | 아니오 | medium | 2026-10-11 | — | — |

### 근거 발췌

- **f1**: 3.0.0 태그 VDA5050_EN.md 머리: 제목 아래 'VDA 5050', 'Version 3.0.0'만 있고 날짜 없음(data/source_texts/ref-031.txt 와 3.0.0 태그 raw 파일로 확인). VDA PDF(103쪽, A4)는 압축 스트림만 읽혀 표지 문구 대조 불가(발행일 미확인, 확인일 기준)
- **f2**: 카탈로그 항목 'March 17, 2026'(ref-1412), 보도자료 머리 'Berlin, April 20, 2026'(ref-032) 모두 이번에 다시 열어 확인. 세 자료 모두 VDA 계열이라 독립 교차 확인 아님
- **f3**: §5.3 "Route calculation and guidance of line-guided mobile robots"; §5.4 경로 실행을 선 유도·자유 주행으로 구분. 원문에 '한정' 표현은 없어 직역. 같은 직역은 2026-10-09-area41-s6 46행에 이미 있음
- **f4**: 보도자료: "the detailed route planning takes place on the vehicle itself", 경로를 'path sharing'으로 중앙 관제와 공유. 명세 §6.8 예정 경로 공유 세부는 2026-10-10-area27-s7 41~45행에 있음
- **f5**: 정정 대상: 본문 5절 수행 자원 칸 '(출하) … 주문 배정·경로 계산·교착 탐지와 해소·교통 제어는 관제 쪽', 2026-09-25-area28-s7 본문 첫 문단. 같은 일반화가 categories/governance-law-and-society/index.md 70행에도 있으나 다른 페이지라 후속 정리 대상
- **f6**: 3.0.0 태그 raw 명세 §7.1.1 재서술: 로봇은 선택 필드를 무시하지 않음, 필요한 선택 파라미터는 factsheet 로 밝힘, 관제는 로봇이 지원하는 선택 필드만 보냄(예: 궤적을 처리 못 하는 로봇에는 trajectory 를 보내지 않음)
- **f7**: §6.1.4.2·§6.1.3.1(data/source_texts/ref-031.txt), §6.1.4.5(3.0.0 태그 raw 명세) 재서술. 재전송 규칙 자체는 2026-10-09-area41-s6 56행, command-and-task-execution-reliability.md 90행에 이미 있음 — 새로운 것은 시험 기대값 관점
- **f8**: f6·f7 조항을 시험 행으로 옮긴 구축자 제안이며 VDA·VDMA 공식 인증 항목 목록이 아님. (5)행은 §7.1.1 관제 의무에서 나옴
- **f9**: 2026-10-11 raw 파일 직접 확인: order 는 controlPoint weight 설명 줄 뒤 쉼표+'}', factsheet 는 physicalParameters 치수 항목의 "unit": "m" 뒤 쉼표+'}', visualization 은 weight 와 properties 끝. main order.schema 는 쉼표 없음. 구문 관찰이며 로봇 적합성 시험이 아님. 행·열 번호는 싣지 않음
- **f12**: f9 관찰에서 나온 운영 제안. 공식 명세·태그 스키마·검사 도구 판을 각각 고정. 공식 저장소 README 는 GitHub 자료와 VDA 게시 PDF 가 다르면 PDF 가 유효하다고 적음(ref-634, 기존 페이지 각주)
- **f13**: Status 절: "not a public-alpha or certification claim"; 실제 고객 기록·외부 DUT·하드웨어 실행 미검증. 문서의 자기 기술만 확인했고 프로그램은 실행하지 않음(발행일 미확인, 확인일 기준)
- **f14**: 21번 8절 vda5050-lab 항목과 각주 '(원문 미열람)' 표시를 f13 으로 보강하는 제안. 개인 프로젝트의 한계 선언과 공식 시험기관 인증은 별개
- **f15**: "It is suggested that vendors prepare for testing"(권고 표현), 도구는 시험소가 시험을 돕는 데 씀. 페이지는 'CTT' 약어를 쓰지 않음(발행일 미확인, 확인일 기준)
- **f16**: "Certified products have been tested in an OPC Foundation accredited Certification Lab"; SDK 기반 응용은 자체 인증 시험 필요. ref-705 와 같은 기관이라 독립 교차 확인 아님(발행일 미확인, 확인일 기준)
- **f17**: 두 페이지 모두 인정 시험소 시험만 설명하고 자체 인증 언급 없음(2026-10-11 재열람). 정정 대상: 2026-09-25-area28-s6「적합성 시험과 인증」첫 문단, 2026-09-25-area28-s7 표 OPC 행, ref-705 참고문헌 요약
- **f18**: f15~f17 정정 제안. 시험 항목은 지원 프로파일에 따라 달라짐
- **f19**: 최상위 oneOf: identityReport·statusReport; location.required = [x, y, angle, planarDatum](z 는 선택). statusReport 필수 필드는 2026-10-10-area20-s7 52행에 이미 있음. 별도 표준 PDF 판·발행일 미확인(발행일 미확인, 확인일 기준)
- **f20**: f19 스키마에 명령·작업 배정 메시지가 없음. 21번 분리 7절 표 MassRobotics 행의 '(원문 미열람)'은 스키마 원문 확인으로 해소
- **f21**: §11.2.2.2~11.2.2.5, 표 124(Base, 모두 M)·125(MDS Operation)·126(AM Extended)·127(CM Extended). 표 123 은 프로파일 URI 목록. 판·범위는 2026-09-29-area04-s7 43행에 이미 있음 — 새로운 것은 Facet 구조
- **f22**: f21 에서 나온 제안
- **f24**: KSSN 상세(itemNo=K001010147546) 2026-10-11 재열람: 번호·제목만 표시. 제정일·부합화 칸 등 세부 칸은 대조 불가(발행일 미확인, 확인일 기준)
- **f25**: KSSN 상세(itemNo=K001010158171) 2026-10-11 열람: 번호·제목만 표시. 웹 검색에서도 제정 기록을 찾지 못함(발행일 미확인, 확인일 기준)
- **f26**: f24·f25 는 번호·제목만 확인. 제정일·고시번호·IDT 는 이전 브리프의 미대조 값이라 쓰지 않음
- **f30**: 벤더 주장: 'KITCHENER, ON—April 9, 2026—OTTO … announced that its autonomous mobile robots' 이하 인증 발표. 판·항목·기관 기재 없음. 인증 발표 자체는 2026-09-25-area28-s6 에 이미 있음 — 새로운 것은 날짜·기종과 각주 '(원문 미열람)' 해소
- **f31**: 행사 안내 본문: 9개 기업 시연, MHP 가 master control system, 생산 라인의 양식화 표현. 기업 수를 로봇 대수로 바꾸지 않음. automatica 2025 전시 시연, 실제 공장 배치 아님(발행일 미확인, 확인일 기준)
- **f32**: 공급자 교체는 "is not demonstrated live at automatica by the Mesh-Up"(발행일 미확인, 확인일 기준)
- **f33**: f31·f32 기반. 현장 유형 × 대분류 매트릭스에서도 도입 사례로 세지 않음
- **f34**: TUHH 저장소 초록: "teleoperation is not natively represented in the standard", 확장 제안·구성 가능한 트래픽 생성기·종단간 지연·오버헤드 평가. 논문 제안 확장이며 표준 채택 기능 아님
- **f36**: 소개문 'highly reproducible virtual-radio testbed', 'real-world over-the-air validation setup'. 트래픽 생성기는 GitHub tudo-cni/VDA-5050-Traffic-Generator 로 공개. 논문 본문 수치(로봇 수·주문 시간)는 PDF 텍스트를 읽지 못해 미확인
- **f37**: f34·f36 기반 8절·10절 제안. 원격 조작 표기는 용어집 '원격 조작 (Teleoperation)'을 따름
- **f38**: f13·f30·f32·f15~f17 종합. oq-055 부분 근거: VDA·VDMA 공인 인증 제도의 존재·부재는 확정 못 함
- **f39**: "On February 17th, VDMA and VDA formally adopted the 3.0.0 release." 뒤이어 법적 승인. 글 날짜는 'March 2026'(일 미표기). 업체 글이며 VDA 자료로 확인되지 않음 — oq-005 출처 충돌의 추가 근거
- **f40**: "On 1st June 2024 the IDS has been approved and became the official buildingSMART standard!"; IFC 모델 자동 적합성 검사. 스키마는 standards.buildingsmart.org/IDS/1.0/ids.xsd(발행일 미확인, 확인일 기준)
- **f41**: UserManual README: 적용 대상은 'what elements are subject to this specification', 'Both applicability and requirements are built with facets', 결과는 불일치 보고(발행일 미확인, 확인일 기준)
- **f42**: restrictions.md: 'Complex Restriction' 네 종류 — 허용 목록, 이름 형식(와일드카드·정규식), 수치 최소·최대(포함·제외), 문자 수. 기수(필수·선택·금지)는 이 문서에 없어 미확인(발행일 미확인, 확인일 기준)
- **f43**: Documentation/README.md: TestCases 폴더 'suite of over 250 test file pairs (.ids and .ifc)', 구현의 읽기·검사 기능 검증용(발행일 미확인, 확인일 기준)
- **f44**: 트랙 반영 제안 2026-10-09-26(IDS → 7절) 처리안. 제안 요약의 기수·사용자 정의 속성 세트 명명 규칙·뉴질랜드 OBOS 프록시 관례는 이번에 원문으로 확인하지 못해 반영하지 않음

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-10-11 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-032 | VDA(Verband der Automobilindustrie) | Version 3.0 of VDA 5050 released | 2026-04-20 | 표준 | medium | 2026-10-11 | https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN | 아니오 |
| ref-1412 | VDA(Verband der Automobilindustrie) | VDA 5050 | 2026-03-17 | 표준 | medium | 2026-10-11 | https://www.vda.de/en/news/publications/publication/vda-5050 | 아니오 |
| ref-1430 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/order.schema (tag 3.0.0) | 미확인 | 표준 | high | 2026-10-11 | https://github.com/VDA5050/VDA5050/blob/3.0.0/json_schemas/order.schema | 아니오 |
| ref-1431 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema (tag 3.0.0) | 미확인 | 표준 | high | 2026-10-11 | https://github.com/VDA5050/VDA5050/blob/3.0.0/json_schemas/factsheet.schema | 아니오 |
| ref-1432 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/visualization.schema (tag 3.0.0) | 미확인 | 표준 | high | 2026-10-11 | https://github.com/VDA5050/VDA5050/blob/3.0.0/json_schemas/visualization.schema | 아니오 |
| ref-413 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/order.schema (main) | 미확인 | 표준 | high | 2026-10-11 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/order.schema | 아니오 |
| ref-408 | ekusiadadus (GitHub) | vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces) | 미확인 | 오픈소스 문서 | medium | 2026-10-11 | https://github.com/ekusiadadus/vda5050-lab | 아니오 |
| ref-705 | OPC Foundation | How to Certify - OPC Foundation | 미확인 | 표준 | medium | 2026-10-11 | https://opcfoundation.org/certification/how-to-certify/ | 아니오 |
| ref-1434 | OPC Foundation | Overview & Benefits — OPC Foundation Certification | 미확인 | 표준 | medium | 2026-10-11 | https://opcfoundation.org/certification/overview-benefits/ | 아니오 |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 미확인 | 표준 | high | 2026-10-11 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json | 아니오 |
| ref-034 | OPC Foundation / VDMA | OPC-40010-1 – OPC UA for Robotics - Part 1: Vertical Integration | 2025-09-08 | 표준 | high | 2026-10-11 | https://reference.opcfoundation.org/specs/OPC-40010-1 | 아니오 |
| ref-138 | 국가표준인증통합정보시스템(KSSN) | KS B 7321-2 로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델 | 미확인 | 표준 | medium | 2026-10-11 | https://www.kssn.net/search/stddetail.do?itemNo=K001010147546 | 아니오 |
| ref-1435 | 국가표준인증통합정보시스템(KSSN) | KS B ISO 22166-202 로봇 — 서비스 로봇의 모듈화 — 제202부: 소프트웨어 모듈용 정보 모델 | 미확인 | 표준 | medium | 2026-10-11 | https://www.kssn.net/search/stddetail.do?itemNo=K001010158171 | 아니오 |
| ref-608 | OTTO by Rockwell Automation | OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments | 2026-04-09 | 벤더 문서 | low | 2026-10-11 | https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/ | 아니오 |
| ref-1436 | VDMA | Mobile Robots in Production: Mesh-Up 2025 | 미확인 | 업계 보고서 | medium | 2026-10-11 | https://www.vdma.eu/en/mesh-up | 아니오 |
| ref-1437 | Wagner, N. A., Toenning, L., Lünsch, D., Jost, J., Wietfeld, C., Detzner, P. | Teleoperating Mobile Robots via VDA 5050 – A First Middleware Evaluation within Open Industrial Networks | 2026-04 | 논문 | medium | 2026-10-11 | https://doi.org/10.1109/WFCS67029.2026.11511549 | 아니오 |
| ref-1438 | TU Dortmund, Communication Networks Institute (ComNets) | Interoperable Teleoperation of Mobile Robots in Intralogistics: Joint Paper Demonstrates End-to-End Network Co-Design for Smart Industries | 2026-04-24 | 정부·연구기관 | medium | 2026-10-11 | https://comnets.etit.tu-dortmund.de/details/interoperable-teleoperation-of-mobile-robots-in-intralogistics-joint-paper-demonstrates-end-to-end-network-co-design-for-smart-industries-63558/ | 아니오 |
| ref-1439 | buildingSMART International | Information Delivery Specification (IDS) | 미확인 | 표준 | high | 2026-10-11 | https://www.buildingsmart.org/standards/bsi-standards/information-delivery-specifications-ids/ | 아니오 |
| ref-1362 | buildingSMART International (buildingSMART/IDS GitHub) | IDS — Documentation/UserManual/README.md | 미확인 | 표준 | high | 2026-10-11 | https://github.com/buildingSMART/IDS/blob/development/Documentation/UserManual/README.md | 아니오 |
| ref-1365 | buildingSMART International (buildingSMART/IDS GitHub) | IDS — Documentation/UserManual/restrictions.md | 미확인 | 표준 | high | 2026-10-11 | https://github.com/buildingSMART/IDS/blob/development/Documentation/UserManual/restrictions.md | 아니오 |
| ref-1443 | buildingSMART International (buildingSMART/IDS GitHub) | IDS — Documentation/README.md | 미확인 | 표준 | high | 2026-10-11 | https://github.com/buildingSMART/IDS/blob/development/Documentation/README.md | 아니오 |
| ref-1442 | idealworks | VDA 5050 3.0.0 release (March 2026) | 2026-03 | 벤더 문서 | low | 2026-10-11 | https://idealworks.com/en/news/vda5050-300-release-march-2026 | 아니오 |

### 출처 요약

- **ref-031**: VDA 5050 3.0.0 명세 마크다운 원문. 입력 원문 텍스트(§4.1·§5.3·§5.4·§6.1)와 3.0.0 태그 raw 파일(§6.1.4.5·§7.1.1)로 관제–로봇 기능 분담, 선택 필드 의무, 오류 응답 조항을 확인했다.
- **ref-032**: VDA 5050 3.0 발행 보도자료. 머리 'Berlin, April 20, 2026'과 자율도 높은 로봇의 경로 자체 계획·경로 공유 설명을 다시 확인했다.
- **ref-1412**: VDA 발행물 카탈로그의 VDA 5050 Version 3.0.0 항목. 표시 날짜 'March 17, 2026'을 다시 확인했다.
- **ref-1430**: 공식 저장소 3.0.0 태그의 주문 메시지 JSON 스키마. 궤적 제어점 weight 속성 설명 줄 뒤 닫는 괄호 앞 끝 쉼표를 확인했다.
- **ref-1431**: 공식 저장소 3.0.0 태그의 팩트시트 JSON 스키마. physicalParameters 치수 항목의 unit 줄 뒤 끝 쉼표를 확인했다.
- **ref-1432**: 공식 저장소 3.0.0 태그의 시각화 메시지 JSON 스키마. properties 끝과 weight 속성의 끝 쉼표를 확인했다.
- **ref-413**: 공식 저장소 main 브랜치의 주문 메시지 JSON 스키마. 3.0.0 태그와 달리 weight 속성에 끝 쉼표가 없음을 확인했다.
- **ref-408**: MQTT 기록에서 VDA 5050 주문·재연결·취소 실패를 진단하는 개인 프로젝트 README. 커밋 4a1a812 고정본에서 v0.2.0 이 개발자 프리뷰이고 인증 주장이 아니라는 한계 선언을 확인했다.
- **ref-705**: OPC 제품 인증 절차 안내. 제조사가 시험 전에 미리 준비하도록 권고하고 적합성 시험 도구(compliance test tools)는 인정 시험소가 쓰는 도구라고 설명한다. 제조사 자체 인증 경로는 없다(기존 요약의 '자체 인증' 표현은 정정 필요).
- **ref-1434**: OPC Foundation 인증 프로그램 개요. 인증 제품은 재단이 인정한 인증 시험소에서 시험을 거치며, 인증 SDK 를 쓴 응용도 각자 인증 시험이 필요하다고 설명한다.
- **ref-230**: MassRobotics AMR 상호운용 표준의 공식 JSON 스키마. 커밋 f9357a4 고정본에서 최상위 oneOf(identityReport·statusReport), location 필수 필드 [x, y, angle, planarDatum], 명령 메시지 부재를 확인했다.
- **ref-034**: OPC UA for Robotics 1부 공식 온라인 참조(1.02판). 이번에 §11.2.2 서버 Facet 네 가지와 표 124~127 의 필수·선택 구분을 확인했다.
- **ref-138**: KS B 7321-2 의 KSSN 상세 페이지. 이번 열람에서는 번호와 제목만 보였고 제정일·부합화 칸 등 세부 정보는 확인하지 못했다(본문 미열람).
- **ref-1435**: KS B ISO 22166-202 의 KSSN 상세 페이지. 번호와 제목만 보였고 제정일·부합화 수준·고시 정보는 확인하지 못했다(본문 미열람).
- **ref-608**: OTTO AMR(OTTO 100·600·1200·1500)이 Idealworks·NAiSE·SYNAOS 등과 VDA 5050 인증을 마쳤다는 2026-04-09 보도자료(벤더 주장). 시험 판·항목·기관은 밝히지 않는다. 참고문헌 목록의 발행일 '2026-04'를 원문 기준 2026-04-09 로 고친다.
- **ref-1436**: VDMA 의 automatica 2025(2025-06-24~27) 이동로봇 혼합 플릿 공동 시연 안내. 9개 기업 참여, MHP 상위 관제, 양식화한 생산 라인 공급 시연이며 관제 공급자 교체는 현장 실시간 시연이 아니라고 밝힌다.
- **ref-1437**: 제22회 IEEE WFCS(2026) 논문. VDA 5050 원격 조작 확장과 트래픽 생성기를 제안하고 Open RAN 무선 링크를 포함한 종단간 지연·오버헤드를 평가한다. TUHH 기관 저장소의 서지·초록만 확인했고 저자 공개본 PDF 본문은 텍스트를 읽지 못했다.
- **ref-1438**: 저자 소속 연구실의 논문 소개. 가상 무선 시험대와 실제 무선 검증 구성을 썼다고 설명하고 트래픽 생성기 공개 저장소를 알린다. 정량 결과는 싣지 않는다.
- **ref-1439**: IDS 공식 소개 페이지. 2024-06-01 승인된 공식 표준이며 기계가 읽는 데이터 요구로 IFC 모델의 자동 적합성 검사를 가능하게 한다고 설명한다.
- **ref-1362**: IDS 공식 저장소 사용자 설명서. 명세·적용 대상·요구 구조, 패싯 여섯 종류, IDS 와 IFC 를 함께 불러 불일치 보고를 얻는 검사 흐름을 설명한다.
- **ref-1365**: IDS 사용자 설명서의 값 제한 절. 열거·패턴·범위·길이 네 가지 복합 제한을 설명한다.
- **ref-1443**: IDS 공식 저장소 문서 안내. 사용자 설명서 위치와, 구현의 읽기·검사 기능 검증용 .ids·.ifc 시험 파일 쌍 250개 이상(TestCases)을 안내한다.
- **ref-1442**: VDA 5050 작업반 참여 업체의 3.0.0 출시 소식 글. VDMA·VDA 가 2월 17일 3.0.0 을 정식 채택했고 이어 법적 승인 절차가 있었다고 적는다(업체 서술).

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/integration/interoperability-standards-and-conformance.md | 5, 6, 7, 8, 10, 11 | 갱신(차등): 섹션 5 — 본문 수행 자원 칸의 '경로 계산'을 '선 유도 로봇의 경로 계산·안내'로 정정(f3·f5), 자유 주행 로봇의 경로 자체 계획·공유 병기(f4; 예정 경로 공유 세부는 2026-10-10-area27-s7 41~45행 연결). 현장 유형 보완: '제조 공장' 사례로 Mesh-Up 2025(f31·f32) — 표 머리와 각 칸에 'automatica 2025 전시 시연, 실제 공장 배치 아님'을 밝히고 매트릭스에서 도입 사례로 세지 않음(f33) / 섹션 6(분리 2026-09-25-area28-s6) — 「적합성 시험과 인증」첫 문단 '제조사가 자체 인증하거나' 정정(f15~f18: 적합성 시험 도구(compliance test tools) 사전 준비는 권고, 인증은 인정 시험소, SDK 응용도 개별 시험; 'CTT' 약어는 쓰지 않음). OTTO 문단에 날짜 2026-04-09·기종 4개·'등' 표기 보강, 각주 원문 미열람 해소(f30, 벤더 주장 유지). 선택 필드·재전송·취소 후 갱신 동작 시험표(f6·f7·f8; 재전송 규칙 자체는 2026-10-09-area41-s6 56행·command-and-task-execution-reliability.md 90행 연결). 근거 수준 구분(f38) / 섹션 7(분리 2026-09-25-area28-s7) — VDA 5050 행: 단일 발행일 미확인 유지, 저장소 명세 표지는 날짜 없음(f1), 날짜 비교는 2026-10-10-area20-s7「VDA 5050 3.0.0의 날짜 표시」로 연결하고 PDF 표지 'March 2026'은 [추정] 유지(f2), Idealworks 의 2026-02-17 채택 서술은 벤더 문서 추정으로만(f39). 본문 첫 문단 '주문 배정·경로 계산…' 정정(f3·f5). OPC 행 '자체·독립 시험소 인증' → '인정 시험소 인증(시험 도구는 사전 점검용)'(f17). MassRobotics 행 '(원문 미열람)' 해소와 location 필수 4필드·명령 메시지 부재(f19·f20). 3.0.0 태그 스키마 끝 쉼표 주의사항(f9 사실, 행·열 번호는 싣지 않음; 출처는 태그 파일 ref-1430~ref-1432 와 main 파일 ref-413, f12). OPC UA Robotics 서버 Facet 표 124~127(f21·f22). 국내 표준: KS B 7321-2·KS B ISO 22166-202 는 국가표준 목록 번호·제목만(f24·f25), 제정일·부합화는 미확인(f26). 트랙 반영 제안 2026-10-09-26(건축 도면 자동 인식 단계 2, IDS 1.0 → 7절) 처리: IDS 1.0 공식 표준(2024-06-01)·명세/적용 대상/요구 구조·패싯 여섯 종류·값 제한 네 종류·구현 검증용 시험 파일 묶음을 'BIM 데이터 교환 요구의 적합성 검사 수단'으로 짧게(f40~f44); 제안 요약의 기수·사용자 정의 속성 세트 명명 규칙·OBOS 프록시 관례는 원문 미확인이라 반영하지 않고 다음 실행 후보 / 섹션 8 — vda5050-lab 항목에 v0.2.0 개발자 프리뷰·인증 주장 아님 반영, 각주 '(원문 미열람)' 해소(f13·f14). Wagner 외 WFCS 2026 통신 평가 논문 추가(f34·f36, 적합성 시험과 구별 f37; 원격 조작 표기는 용어집 따름) / 섹션 10 — 42. 분산 시스템·통신·컴퓨팅 구조 연결(f37), 14. 도면·BIM에서 지도 만들기 연결(IDS, f44) / 섹션 11 — oq-005(f1·f2·f39), oq-055(f13~f18·f30·f38), oq-091(f9·f12), oq-026(f24~f26) 부분 근거, 모두 열림 유지. oq-111 은 이번에 새 근거 없음(TTA·KOROS 원문 미확인). 새 질문 2건. 후속 정리(이번 대상 아님): categories/governance-law-and-society/index.md 70행 '경로 계산' 일반화, ref-705 참고문헌 요약의 '자체 인증' 표현, ref-608 발행일 2026-04-09. |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- VDA 5050 3.0.0 태그 스키마의 끝 쉼표를 고친 수정본을 연동 시험에 쓸 때 공식 PDF·태그와의 차이를 누가 승인하고 어떤 회귀 시험으로 확인하는가? | 관련 영역: 21. 상호운용 표준·적합성, 57. 자산·소프트웨어 수명주기 관리 | 근거: f9 | 종류: 일반
- VDA 5050 2.x·3.x 판이 섞인 플릿을 실제 현장에서 전환하면서 판별 스키마 차이와 시험 입력을 어떻게 검증했는지 공개한 기록이 있는가? (관련 기존 질문: oq-091) | 관련 영역: 20. 로봇·제조사 관제 연동, 21. 상호운용 표준·적합성 | 근거: f12 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 23 · 교차 확인: 0
- 예산 사용량: 검색 5회 · 신규 출처 14건
- 미확인 항목:
    - VDA 5050 3.0.0 VDA 배포 PDF 표지의 'March 2026' 표기: WebFetch 가 압축 PDF 본문 텍스트를 읽지 못해 대조 불가(103쪽·A4 만 확인) — 출처 항목으로 넣지 않고 f2 에서 [추정] 유지를 제안
    - f9: 끝 쉼표의 정확한 행·열 번호와 main 브랜치 factsheet·visualization 스키마의 수정 여부는 확인하지 않음(main 은 order.schema 만 확인)
    - f24·f25: KSSN 상세 페이지에서 번호·제목만 보여 제정일·부합화(IDT 여부)·고시번호·쪽수 미확인
    - TTAK.KO-10.1295-Part8: 웹 검색에서 찾지 못했고 이전 브리프의 TTA 목록 URL 은 검증에서 HTTP 400 — 출처·finding 에서 뺌
    - KOROS 1148-8:2025 제정일과 TTA 표준과의 관계: 원문 봇 차단으로 미확인 — finding 에서 뺌
    - ISO 21423 단계·범위: iso.org 미열람 — 21번에는 새로 쓰지 않음
    - VDA5050 이슈 #660: 실재 미확인 — 출처에서 뺌
    - Wagner 외 본문의 평가 시나리오(로봇 수·주문 시간·원격 조작 구간)와 향후 과제 문구: 저자 공개본 PDF 텍스트를 읽지 못해 미확인
    - IDS 의 기수(필수·선택·금지), 사용자 정의 속성 세트 명명 규칙, 뉴질랜드 OBOS 프록시 관례(트랙 반영 제안 요약 항목): 이번에 원문으로 확인하지 못함
    - f39: Idealworks 의 2026-02-17 채택 서술은 VDA 자료로 확인되지 않음
    - VDA·VDMA 공인 적합성 인증 제도의 존재·부재(oq-055)는 확정 못 함
- 범위 경계 위반 의심:
    - f31~f33: Mesh-Up 2025 는 automatica 2025 전시 시연이며 실제 공장 배치가 아님. site_type '제조 공장'은 시연이 겨냥한 현장 유형을 뜻함
    - f34~f37: 무선망·Open RAN 통신 평가는 42. 분산 시스템·통신·컴퓨팅 구조 쪽 내용이라 21번에는 적합성 시험과 구별되는 통신 평가 연구로만 씀
    - f21·f22: OPC UA Robotics 정보모델은 4. 이기종 로봇 등록에서 이미 다루므로 21번에는 Facet·인증 범위 요구만 씀
    - f40~f44: IDS 는 건물 정보 모델 데이터 교환 표준으로 14. 도면·BIM에서 지도 만들기·건축 도면 자동 인식 트랙 쪽 내용이 많으므로 21번에는 적합성 검사 수단으로만 짧게 씀
- 한계: 재실행 1회차. 반려 사유 1(신규 참고문헌 id 충돌): 직전 실행 2026-10-10-06 이 같은 예약 구간에서 쓴 ref-1424~ref-1428 과 기존 출처 ref-1429(Franke 외)를 피해 신규 출처를 예약 구간 안의 ref-1430~ref-1443 으로 다시 매겼다. VDA 카탈로그는 기존 id ref-1412 을 재사용하고(이전 브리프의 ref-1412 표기 철회), OPC 개요는 ref-1434, Mesh-Up 은 ref-1436, Wagner 외는 ref-1437 로 옮겼다. 이전 브리프의 ref-1424(이슈 #660)·ref-1425(TTA 목록)·ref-1426(KSSN, 이제 ref-1435)·ref-1428·ref-1429 할당은 모두 없앴다. 실행 컨텍스트의 next_ref_id(ref-1412)가 이미 사용 중이라 구간 안 미사용 번호를 썼다 — pipeline/agent_runner.py 의 next_ref_id 계산 확인 필요. (관련 finding: f9·f16·f25·f31·f34) 반려 사유 2(원문 열람 재현 실패): ref-1412 PDF 는 이번에도 텍스트를 읽지 못해 출처에서 빼고 f1 을 저장소 마크다운 표지 사실로 바꿨다(관련 finding: f1·f2). KSSN 두 페이지는 다시 열었으나 번호·제목만 보여 f24·f25 를 그 범위의 사실로 줄이고 f26 은 열린 질문 유지 의견으로 바꿨다. TTA 목록은 웹 검색으로도 확인 못 해 f28 을 지웠다. Wagner 외는 PDF 텍스트를 읽지 못해 f35 를 지우고, f36 은 연구실 소개문(ref-1438)으로 확인한 가상 무선·실제 무선 구분만 남겼다. f10(파서별 행·열 번호)은 재현 근거가 없어 지웠다. 이번에 fetched: true 로 적은 출처는 모두 이번 실행에서 WebFetch 또는 raw 경로로 다시 열었고(ref-031 은 입력 원문 텍스트 + 3.0.0 태그 raw), fetch_url 이 다른 경우 적었다. 반려 사유 3(미확인 출처·전언 finding): ref-1424(이슈 #660)를 출처에서 빼고 f11·f23·f27 을 지웠으며, ref-159·ref-710 은 근거 finding 이 없어 sources 에서 뺐다. f29 는 지웠다(oq-111 열림 유지). 반려 사유 4(트랙 반영 제안 미처리): buildingSMART 공식 페이지와 공식 저장소 문서로 IDS 1.0 을 조사해 f40~f44 를 냈고 7절 반영안을 rationale 에 적었다. 제안 요약의 기수·사용자 정의 속성 세트·OBOS 프록시는 확인 못 해 다음 실행 후보로 남긴다. required_fixes 대응: [의견]은 모두 claim 첫머리에 '구축자 의견: '을 붙였다. f9 출처를 확인한 태그 파일별 항목(ref-1430~ref-1432)과 main 파일(ref-413)로 바꾸고 ref-051 은 뺐다. f13 은 'Developer Preview'로 재서술하고 'Synthetic Demo Preview' 인용을 없앴다. f21 표 번호를 124~127 로 고쳤다. ref-608 발행일을 2026-04-09 로 고쳤다. f31~f33 에 'automatica 2025 전시 시연, 실제 공장 배치 아님'을 넣었다. 새 열린 질문 가운데 TTA–KOROS 질문은 뺐고, 2.x·3.x 전환 질문의 근거를 f12 와 oq-091 로 바꿨다. 용어: '원격 조작' 표기, 'CTT' 대신 '적합성 시험 도구(compliance test tools)'. 열린 질문 해결 제안 없음: oq-005 근거 f1·f2·f39, oq-055 근거 f13~f18·f30·f38, oq-091 근거 f9·f12, oq-026 근거 f24~f26 (모두 부분 근거). 검색 5회/30, 신규 출처 14건/15. 재사용 9건(ref-031·ref-032·ref-1412·ref-408·ref-705·ref-230·ref-034·ref-138·ref-608, 모두 이번에 다시 엶). IDS 관련 URL 이 트랙 실행에서 이미 등록됐다면 퍼블리셔가 같은 URL 로 합쳐야 한다(참고문헌 목록 요약본에 없어 확인 못 함). 교차 확인 0건(VDA 계열 자료, 같은 저장소 파일, OPC 두 페이지는 각각 같은 기관). 정정 요청 없음. 용어 후보 없음(정보 전달 명세·적합성 시험·원격 조작은 용어집에 있음).
