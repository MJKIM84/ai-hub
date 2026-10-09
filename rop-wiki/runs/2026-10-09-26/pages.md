# 스토리텔러 산출 2026-10-09-26

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/floorplan-recognition/stage-2-data-and-standards.md | draft | q2-04·q2-06 답함(3절 소제목 신설, q2-02 표 갱신 칸 병기), 2절 표·상태 줄 갱신, 4절 결론·불확실성 보강, 후속 질문 3건, 6절 완료 조건(전환 아니오), 출처·이력 추가. 2차: q2-04 소절의 충전 위치 소절 위치 표기와 2절 첫 문단 표현 수정 |
| update | docs/tracks/floorplan-recognition/space-graph-schema-draft.md | draft | v1.2 → v1.3: 충전 위치에 속성 'BIM 표현(후보)' 추가(2절 보충 표), 6절 충전소 항목 범위 한정·RECHARGER·IDS 근거 보강 |
| update | docs/ideas/floorplan-recognition.md | draft | 3절에 공개 데이터셋 비교표 갱신 소절(CubiCasa5K·AI Hub 행, q2-04), 4절에 표준 밖 운영 시설의 IFC 표현과 IDS 납품 요구 소절(q2-06, BIM 소절 셋째 항목 범위 한정) 추가 |
| update | docs/tracks/floorplan-recognition/stage-1-prior-work-and-products.md | draft | 3절 끝에 q1-08 보강 소절(f25·f26) 추가, 출처 ref-1437, 이력 메모. 2차: 머리말 패치로 프런트매터 sources 에 ref-1437 추가 |
| update | docs/tracks/floorplan-recognition/index.md | draft | 6절에 실행 2026-10-09-26 요약 문단 추가(스키마 초안 v1.3, q2-04·q2-06 답함). 상태 줄은 이미 최신이라 바꾸지 않음 |

## 변경 이력·색인

- 변경 이력: 2026-10-09 | 건축 도면 자동 인식 단계 2 | q2-04·q2-06 답함, q1-08 보강(조사 중 유지), 공간 그래프 스키마 초안 v1.2 → v1.3, 후속 질문 3건 | run 2026-10-09-26
- 홈 최근 업데이트: 2026-10-09 — 건축 도면 자동 인식 단계 2: q2-04(AI Hub·CubiCasa5K 계단·엘리베이터 라벨과 이용 조건)·q2-06(IFC RECHARGER 유형 값·사용자 정의 속성 세트·IDS 납품 요구) 답함, 공간 그래프 스키마 초안 v1.3
- 대분류 최근 업데이트: 2026-10-09 — 14. 도면·BIM에서 지도 만들기(건축 도면 자동 인식 트랙 단계 2): AI Hub 승강기·계단실 라벨 확인, 로봇 충전기 BIM 표현 후보와 IDS 납품 요구 경로 정리
- 세부영역 최근 업데이트: 2026-10-09 — 14. 도면·BIM에서 지도 만들기: 트랙 단계 2 결과(IDS·RECHARGER·AI Hub 라벨, oq-197 해결 근거)의 7·8·11절 반영 제안(다음 해당 영역 실행에서 반영)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | buildingSMART 데이터 사전 | buildingSMART Data Dictionary (bSDD) | buildingSMART 가 정보 전달 명세(IDS)를 작성할 때 쓸 수 있는 공유 속성 라이브러리로 설명하는 데이터 사전 서비스다. | 14, 21 | ref-1430 |
| new | 건물 요소 프록시 | Building Element Proxy (IfcBuildingElementProxy) | IFC 4.3 개발 브랜치 기준으로, 명세가 아직 정의하지 않았거나 응용이 의미 정의에 대응시킬 수 없는 건축 요소를 교환하는 IFC 엔터티이며, PredefinedType 을 USERDEFINED 로 두면 ObjectType 으로 유형 이름을 적어야 하고 IFC4.3.0.0 부터는 공간 자리표시·예비 공간 용도로 쓰지 않는다(그 용도는 IfcVirtualElement). | 14, 21 | ref-1425 |
| new | 사용자 정의 속성 세트 | User-defined Property Set | IFC 명세에 선언되지 않은 프로젝트·조직 고유의 속성 묶음으로, 명세 정의 세트에만 쓰는 'Pset_' 접두어 없이 이름을 짓고 개별 객체에는 IfcRelDefinesByProperties 로, 유형 객체에는 직접 연결로 붙인다. | 14, 21 | ref-1426, ref-1433 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-1012 | AI Hub (한국지능정보사회진흥원) — 구축 주관 에이치씨아이플러스(주) | 건축 도면 데이터 | 정부·연구기관 | high | https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71465 |
| ref-062 | CubiCasa (Kalervo, A. 외) | CubiCasa5k — README (CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis) | 오픈소스 문서 | medium | https://github.com/CubiCasa/CubiCasa5k |
| ref-213 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcTransportElement (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 표준 | medium | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcTransportElement.md |
| ref-214 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcOutletTypeEnum (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 표준 | medium | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/domain/IfcElectricalDomain/Types/IfcOutletTypeEnum.md |
| ref-215 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcElectricApplianceTypeEnum (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 표준 | medium | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/domain/IfcElectricalDomain/Types/IfcElectricApplianceTypeEnum.md |
| ref-1421 | AI Hub (한국지능정보사회진흥원) | AI 허브 이용정책 (데이터 이용정책) | 정부·연구기관 | high | https://www.aihub.or.kr/intrcn/guid/usagepolicy.do?currMenu=151&topMenu=105 |
| ref-1422 | Zenodo (CubiCasa) | CubiCasa5k | 오픈소스 문서 | high | https://zenodo.org/record/2613548 |
| ref-1423 | CubiCasa (CubiCasa/CubiCasa5k GitHub) | CubiCasa5k — floortrans/loaders/house.py | 오픈소스 문서 | high | https://github.com/CubiCasa/CubiCasa5k/blob/master/floortrans/loaders/house.py |
| ref-1424 | 경기도 고양시(공공데이터포털) | 경기도 고양시_어린이 음성맥락 인식률 향상을 위한 방송 음성 및 자연어 처리(AI학습용)_20240105 | 정부·연구기관 | medium | https://www.data.go.kr/data/15146382/fileData.do |
| ref-1425 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcBuildingElementProxy (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 표준 | high | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/shared/IfcSharedBldgElements/Entities/IfcBuildingElementProxy.md |
| ref-1426 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcPropertySet (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 표준 | high | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcKernel/Entities/IfcPropertySet.md |
| ref-1427 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcElectricFlowStorageDeviceTypeEnum (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 표준 | high | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/domain/IfcElectricalDomain/Types/IfcElectricFlowStorageDeviceTypeEnum.md |
| ref-1428 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcElectricFlowStorageDevice (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 표준 | high | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/domain/IfcElectricalDomain/Entities/IfcElectricFlowStorageDevice.md |
| ref-1429 | buildingSMART International | Pset_ElectricFlowStorageDeviceTypeRecharger — IFC 4.3.2.0 documentation (IFC4X3_ADD2 development build, 개발 빌드 경로로 이동) | 표준 | medium | https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_ElectricFlowStorageDeviceTypeRecharger.htm |
| ref-1430 | buildingSMART International | Information Delivery Specification (IDS) | 표준 | high | https://www.buildingsmart.org/standards/bsi-standards/information-delivery-specification-ids/ |
| ref-1431 | buildingSMART (buildingSMART/IDS GitHub) | IDS — Documentation/UserManual/README.md | 표준 | high | https://github.com/buildingSMART/IDS/blob/development/Documentation/UserManual/README.md |
| ref-1432 | buildingSMART (buildingSMART/IDS GitHub) | IDS — Documentation/UserManual/entity-facet.md | 표준 | high | https://github.com/buildingSMART/IDS/blob/development/Documentation/UserManual/entity-facet.md |
| ref-1433 | buildingSMART (buildingSMART/IDS GitHub) | IDS — Documentation/UserManual/property-facet.md | 표준 | high | https://github.com/buildingSMART/IDS/blob/development/Documentation/UserManual/property-facet.md |
| ref-1434 | buildingSMART (buildingSMART/IDS GitHub) | IDS — Documentation/UserManual/restrictions.md | 표준 | high | https://github.com/buildingSMART/IDS/blob/development/Documentation/UserManual/restrictions.md |
| ref-1435 | Construction Information Limited (Masterspec, 뉴질랜드) | 4.0 Object Properties & Property Grouping — 4.3 IFC properties (Open BIM Object standard (OBOS) V1.0) | 업계 보고서 | medium | https://masterspec.co.nz/43-IFC-Properties/7266/ |
| ref-1436 | Pauwels, P., de Koning, R., Hendrikx, B., & Torta, E. (Advanced Engineering Informatics 56, 101959) | Live semantic data from building digital twins for robot navigation: Overview of data transfer methods | 논문 | medium | https://research.tue.nl/en/publications/live-semantic-data-from-building-digital-twins-for-robot-navigati/ |
| ref-1437 | Robotics 24/7 | RGo Robotics introduces AI-powered Intelligent Mapping system | 기사 | low | https://www.robotics247.com/article/rgo-robotics-introduces-ai-powered-intelligent-mapping-system |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | CubiCasa5K 원 SVG 주석에는 계단(Stairs)·계단실(StairWell)·엘리베이터(Elevator) 범주가 실제로 몇 개 들어 있으며, 공식 학습 매핑이 이를 일반 방으로 합치거나 빼는 상태에서 기존 위키의 'CubiCasa5K 계단 라벨 있음' 서술은 원 주석 범주 기준으로 고쳐 써야 하는가? | 14, 45 | 열림 | — |
| new | — | AI허브 원 이용정책은 이용자가 학습시킨 모델의 배포·상업적 이용을 직접 말하지 않고 '학습용으로만'과 '영리·비영리 연구개발 활용'을 함께 적는데, 건축 도면 데이터로 학습한 도면 인식 모델을 상용 서비스로 배포하는 것이 허용되는지와 데이터셋별 별도 조건이 있는지를 운영기관 확인으로 정할 수 있는가? | 14, 59 | 열림 | — |
| new | — | 국내 공공건축 BIM 납품 기준(건설산업 BIM 시행지침 등)이나 로봇 친화형 건축물 인증이 로봇 충전 공간·작업 스테이션을 BIM 객체·속성으로 납품하도록 요구하거나 그 IDS·속성 세트를 정한 사례가 있는가? (관련 기존 질문: oq-199) | 14, 21 | 열림 | — |
| update | oq-197 | AI Hub 건축 도면 데이터의 라벨(구조 8종·공간 12종·객체 5종)에 충전 위치처럼 로봇 운영에 필요한 클래스가 들어 있는가, 비주거 건물 도면은 얼마나 포함되는가? | 14, 45 | 해결 | docs/tracks/floorplan-recognition/stage-2-data-and-standards.md#q2-04 |

## 현장 유형 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| Open BIM Object standard (OBOS) V1.0 | 표준 | Construction Information Limited (Masterspec, 뉴질랜드) | 14, 21 | ref-1435 | https://masterspec.co.nz/43-IFC-Properties/7266/ |

## 추가 조사 요청

- 단계 2 완료 조건: 공간 그래프 스키마 초안 3절 관계(엣지)와 표준(IndoorGML 쌍대 그래프 엣지, IFC 공간 경계, BOT adjacentZone 등)의 대응을 근거 finding 과 함께 조사해야 단계 2 를 마칠 수 있다.
- q2-04 보강: CubiCasa5K 원 SVG 의 Stairs·StairWell·Elevator 실제 주석 개수 — q2-02 표·아이디어 비교표 병기를 정리하는 데 필요.
- AI허브 운영기관 확인 또는 건축 도면 데이터셋별 이용 조건 문서 — 학습 모델 상용 배포 조건(새 열린 질문)에 필요.
- Pset_ElectricFlowStorageDeviceTypeRecharger 의 게시판 IFC 4.3 ADD2 공식판 포함 여부와 작업 스테이션에 대응하는 IFC 유형 값 — 스키마 초안 작업 스테이션의 BIM 표현에 필요.
- q1-08: 국내 물류센터 로봇 도입 단계별(지도 작성·공용 자원 등록·좌표 정렬) 소요 시간의 국내 공공·학술 자료.

## 이행한 수정 지시

- f14 열거 값 개수 — 단계 2 페이지 q2-06 답과 스키마 초안 6절 보강 항목에 IfcElectricFlowStorageDeviceTypeEnum 값을 'USERDEFINED·NOTDEFINED 를 포함한 11개'로 적었고 '13개'는 쓰지 않았다.
- f14·f15·f24 RECHARGER 표현 — 단계 2 페이지·스키마 초안·아이디어 페이지에서 RECHARGER 를 '배터리 충전기 일반 정의, 차량·로봇 언급 없음(개발 브랜치 기준)'으로, 속성 세트를 'IFC4.3_ADD2 개발 빌드(buildingSMART Working Draft) 문서, 게시판 공식판 포함 여부 미확인'으로 적고 로봇 충전기 표현은 [추정]의 '후보'로만 썼다.
- ref-1429 각주 — 제목 괄호에 'IFC4X3_ADD2 development build, 개발 빌드 경로로 이동'을 적어 세 페이지 각주와 reference_updates 에 같은 제목을 썼다.
- f6 한정 — q2-04 답의 종합 문장을 '이용자가 이 데이터로 학습시킨 모델의 배포·상업 이용은 직접 말하지 않으며'로 한정하고 '법적 판단 아님'을 유지했으며 열린 질문 문장도 같은 범위로 맞췄다.
- f5·f6 2차 기술 — q2-04 답에 공공데이터포털 문구가 경기도 고양시 어린이 음성 데이터셋 페이지의 2차 기술임을 밝히고, 원 정책의 '별도 협의'와 2차 기술의 '영리 판매·활용 제한 없음'을 둘 다 제시해 열린 질문으로 올렸다.
- f2 링크 표현 — q2-04 답과 아이디어 페이지 갱신 표에 '데이터셋 고유 이용 조건 문구 없이 이용정책·이용약관 링크만 둔다'로 썼고 위치 표현은 쓰지 않았다.
- q2-04 답 구성 — 단계 2 페이지 3절 '### q2-04 … {#q2-04}'에 클래스 구성(f1·f3·f7·f8·f9)과 이용 조건(f2·f4·f5, 종합 f6·f10 추정)을 나눠 적고, 4절 남은 불확실성에 주거 도면 기준과 데이터셋별 별도 조건 미확인을 두었다.
- q2-02 표·아이디어 3절 비교표 — 기존 칸을 지우지 않고 각 절에 '갱신 칸' 보충 표를 두어 CubiCasa5K 계단 칸에 원 주석 범주·공식 학습 매핑 차이(ref-1423)와 CC BY-NC-SA 4.0(ref-1422)을, 래스터 엘리베이터 칸·AI Hub 행에 f1(ref-1012)을, AI Hub 접근 조건에 f2·f4(ref-1012·ref-1421)를 병기했으며 ref-074 는 새로 인용하지 않았다(출력 분량 한도로 원 표 칸 직접 수정 대신 같은 절 보충 표로 이행).
- 충전 위치 범위 한정 — 단계 2 페이지 q2-02 갱신 칸 표와 4절 결론 추가, 아이디어 페이지 4절 새 소절 첫 문단, 스키마 초안 6절 보강 항목에서 기존 문장을 두고 '콘센트·전기기기 유형 열거 기준'을 밝힌 뒤 RECHARGER(f14)·속성 세트(f15, 작업 초안)를 병기했다(기존 문장 바로 옆이 아니라 같은 절에 덧붙인 형태).
- q2-06 답 구성 — 단계 2 페이지 3절 '### q2-06 … {#q2-06}'을 프록시·USERDEFINED(f11, f12 는 IfcTransportElement 한정), RECHARGER·속성 세트(f13~f15), 콘센트·전기기기 열거(f16), 사용자 정의 속성 세트(f17), IDS(f18~f21), 실무 관례(f22, IFC4 Add2·뉴질랜드 OBOS V1.0·로봇 충전소 대상 아님·발행일 미확인), 연구(f23), 종합(f24 추정)으로 구성하고 IDS 첫 등장을 '정보 전달 명세(Information Delivery Specification, IDS)'로 써서 ../../glossary/information-delivery-specification.md 에 연결했다.
- f23 — 주행 시험 부분에 '연계 대상:'을 붙이고 디지털 트윈을 건물 데이터 로컬 저장소(현재 상태 쪽, 18. 실시간 세계 상태·데이터 일관성) 의미로만 써 34. 시뮬레이션·예측용 디지털 트윈과 구분했으며 초록 기준임을 밝혔다.
- f25·f26 — 단계 1 페이지 3절에 q1-08 보강 소절을 덧붙여 '연계 대상:'·[추정]·'벤더 주장'을 유지하고 '수개월 수작업 병목'(기사 서술)과 '수개월에서 며칠'(RGo 측 주장)을 나눠 적었으며 f26 은 부재 확인 아님을 밝혔고, q1-08 은 백로그 '조사 중'·answer_link null 로 두었다(단계 1 페이지 입력 부재로 소절은 3절 끝에 덧붙임).
- 온톨로지 — 스키마 초안 2절에 충전 위치의 속성 'BIM 표현(후보)'을 지시 문구대로 더하고(보충 표 행) 근거에 finding f11·f13·f14·f15·f16·f17·f22(실행 2026-10-09-26)와 각주 ref-1425·ref-1428·ref-1427·ref-1429·ref-214·ref-215·ref-1426·ref-1435 를 두었으며, 상태 '확정' 유지, H1·auto:page-status 표식 값·프런트매터 ontology_version·ontology_draft_version 을 1.3 으로 맞췄고, IDS 방식과 관례 부재는 6절 보강으로 두고 작업 스테이션·관계 표는 바꾸지 않았다.
- 단계 2 페이지 2절 — q2-04·q2-06 을 '답함', 답한 실행 2026-10-09-26, 답 위치 #q2-04·#q2-06 으로 두고 새 단계 2 질문 q2-11·q2-12 를 2절 표와 5절에 '열림'으로 더했다(백로그에 있던 q2-10 도 표에 '열림'으로 더함).
- 단계 2 페이지 6절 — 첫 행 '충족'·'미승인', 둘째 행 '미충족'·'미충족 · 미승인'으로 두고 아래 줄을 지시 문구 그대로 썼으며 stage_transition 은 넣지 않았고, 상태 줄을 열린 질문 6건·답한 질문 5건으로 2절 표와 맞췄다.
- 새 트랙 질문 — 세 건을 q3-13·q2-11·q2-12 로 등록하고 q2-12 끝의 관련 표기를 '(관련: q1-05, q2-10, oq-341)'로 고쳤다.
- open_questions_new — 세 건을 종류 일반(접두어 없음)으로 냈고 3번은 '(관련 기존 질문: oq-199)'를 유지했으며 question 에 필드 구분 문자열을 남기지 않았다.
- oq-197 — f1·f3 근거로 '해결', link 를 단계 2 페이지 #q2-04 로 냈다.
- 용어집 — IDS 는 새로 등록하지 않고 기존 information-delivery-specification 에 연결했으며, bSDD 정의를 f18 범위로 쓰고, 건물 요소 프록시 정의에 'IFC 4.3 개발 브랜치 기준'과 IFC4.3.0.0 부터 공간 자리표시에 쓰지 않는다는 점을 넣었다.
- 세부영역 반영 제안 — 14. 도면·BIM에서 지도 만들기, 45. 문서·도면·장면 이해, 21. 상호운용 표준·적합성, 59. 법·규제·보험·라이선스 제안을 area_reflection_proposals 로만 남기고 세부영역 페이지는 고치지 않았으며, 59. 법·규제·보험·라이선스 제안에 '법적 판단 아님'을 붙였다.
- 2차: 충전 위치 소절 위치 표기 — 단계 2 페이지 3절 q2-04 소절의 '#### q2-02 표의 갱신 칸' 표 바로 아래 문장을 "아래 '충전 위치' 소절과 …"에서 "위 q2-02 의 '충전 위치' 소절과 …"로 고쳤다.
- 2차: 단계 1 페이지 sources — stage-1-prior-work-and-products.md 에 '머리말' 패치를 더해(이동 경로·H1·상태 줄은 입력 그대로) 프런트매터 sources 에 ref-1437 을 추가하고, 3절 q1-08 보강 소절의 [^ref-1437] 각주·8절 정의와 맞췄다.
- 2차: 단계 2 페이지 2절 첫 문단 — "앞선 트랙 실행에서 이 단계로 들어온 후속 질문 8개"를 "앞선 트랙 실행과 이번 실행(2026-10-09-26)에서 이 단계로 들어온 후속 질문 8개"로 고쳤다.

## 트랙 갱신

- 단계 페이지: docs/tracks/floorplan-recognition/stage-2-data-and-standards.md
- 온톨로지 초안 버전: 1.3
- 트랙 로그 항목: 답한 질문: q2-04, q2-06 (q1-08 은 부분 답 — 조사 중 유지, 국내 단계별 시간 자료 여전히 없음) / 새 질문: q3-13(단계 3, f24), q2-11(단계 2, f14), q2-12(단계 2, f1) / 온톨로지 변경: v1.2 → v1.3: 개념 '충전 위치'에 속성 'BIM 표현(후보)' 추가(f11·f13·f14·f15·f16·f17·f22), 거부 없음(IDS 납품 요구 방식 f24 는 6절 항목 보강). 버전 이력 행: 1.3 · 2026-10-09 · 충전 위치 속성 'BIM 표현(후보)' 추가(f11·f13·f14·f15·f16·f17·f22) · 2026-10-09-26 / 완료 조건 평가: 미충족(부족: 관계(엣지) 쪽 표준 대응 없음; 열린 질문 q2-07·q2-08·q2-09·q2-10·q2-11·q2-12; 되돌아온 단계 1 질문 q1-08 조사 중) / 세부영역 반영 제안: 14. 도면·BIM에서 지도 만들기 3건(7·8·11절), 45. 문서·도면·장면 이해 1건, 21. 상호운용 표준·적합성 1건, 59. 법·규제·보험·라이선스 1건 / 다음 실행 제안: q2-07, q2-09, q2-11 과 관계(엣지) 표준 대응 / 비고: 단계 1 페이지 q1-08 보강은 3절 끝에 덧붙였고(프런트매터 sources 에 ref-1437 추가), 출력 분량 한도로 일부 표 칸은 같은 절 보충 표로 병기했다 — 다음 트랙 실행에서 원 표에 통합 권고
- 개요 진행 현황: 단계 2 진행 중 — 열린 질문 6, 답함 5, 완료 조건 미충족 (되돌아온 단계 1 질문 q1-08 조사 중)

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q2-04 | 답함 | docs/tracks/floorplan-recognition/stage-2-data-and-standards.md#q2-04 | — | — | — |
| q2-06 | 답함 | docs/tracks/floorplan-recognition/stage-2-data-and-standards.md#q2-06 | — | — | — |
| q1-08 | 조사 중 | — | — | — | — |
| q3-13 | 열림 | — | ROP 가 BIM 납품 요구로 쓸 로봇 운영 시설용 IDS(충전 위치는 IfcElectricFlowStorageDevice RECHARGER 또는 관련 엔터티·IfcBuildingElementProxy 의 USERDEFINED·ObjectType 값으로, 작업 스테이션은 대응 유형을 정한 뒤, 'Pset_' 가 아닌 프로젝트 속성 세트에 접근 자세·도킹 이름·상호작용 노드 속성을 REQUIRED 로 요구하는 형태)를 어떤 항목으로 정의하며, 설계·시공 측이 그 값을 채울 수 있는가, 채울 수 없으면 어느 단계에서 누가 보완하는가? (q2-06 에서 파생) | 3 | f24 |
| q2-11 | 열림 | — | 로봇 충전기를 IFC 4.3 의 전기 저장 장치 유형 값 RECHARGER(배터리 충전기 일반 정의, 속성은 공급 정격 전류뿐)로 표현할지 USERDEFINED·ObjectType 으로 표현할지 정하는 기준은 무엇이며, 실무 IFC 모델에서 로봇·차량 충전기가 실제로 어느 쪽으로 내보내지는가? (q2-06 에서 파생) (관련: q2-09) | 2 | f14 |
| q2-12 | 열림 | — | AI Hub 건축 도면 데이터의 엘리베이터·엘리베이터홀·계단실 라벨(아파트 코어 기준)로 학습한 모델이 물류센터·병원 같은 비주거 도면의 화물용 승강기·계단실을 얼마나 인식하는가, 라벨 정의서는 계단실과 엘리베이터 영역을 어떤 기준으로 그리는가? (q2-04 에서 파생) (관련: q1-05, q2-10, oq-341) | 2 | f1 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 14 | 7. 관련 표준·프레임워크·오픈소스 | IDS 1.0(2024-06-01 승인)과 IFC 4.3 의 건물 요소 프록시·사용자 정의 속성 세트·전기 저장 장치 유형 값 RECHARGER(배터리 충전기 일반, 로봇 충전기 표현은 후보)를 BIM 입력 요구 수단으로 추가(f14, f17, f18, f20, f24). |
| 14 | 8. 대표 연구와 자료 | AI Hub 건축 도면 데이터의 엘리베이터·엘리베이터홀·계단실 라벨(주거 도면 48,033장)과 CubiCasa5K 의 공식 학습 매핑 차이·CC BY-NC-SA 4.0 라이선스(f1, f3, f7, f8). |
| 14 | 11. 열린 질문 | oq-197 해결 근거(AI Hub 라벨에 로봇 운영 클래스 없음, 도면 모두 주거 유형, f1·f3)와 새 열린 질문(CubiCasa5K 원 주석 개수, AI허브 학습 모델 상용 배포 조건, 공공건축 BIM 납품의 로봇 시설 요구). |
| 45 | 8. 대표 연구와 자료 | 교차 규칙(도면 해석은 14. 도면·BIM에서 지도 만들기에 적용)에 따라 도면 해석 학습 데이터의 클래스 구성(공식 학습 매핑에서 엘리베이터·계단실이 일반 방으로 합쳐짐)과 이용 조건(비상업 라이선스, AI허브 원 이용정책)을 반영(f1, f4, f6, f7, f8, f10). |
| 21 | 7. 관련 표준·프레임워크·오픈소스 | IDS 1.0 의 적용 대상·요구 구조, 엔터티·속성 패싯, 값 제한·기수와 IFC 사용자 정의 속성 세트 명명 규칙, 뉴질랜드 OBOS 프록시 관례를 BIM 데이터 교환 요구·적합성 검사 수단으로(f17, f18, f19, f20, f21, f22). |
| 59 | 7. 관련 표준·프레임워크·오픈소스 | 공공 AI 학습 데이터(AI허브) 원 이용정책과 다른 데이터셋 페이지 2차 기술의 차이, CC BY-NC-SA 4.0 평면도 데이터셋의 상용 이용 제약을 학습 데이터 라이선스 사례로(f4, f5, f6, f7). 법적 판단 아님. |
