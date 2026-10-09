# 스토리텔러 산출 2026-10-09-24

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/floorplan-recognition/stage-2-data-and-standards.md | draft | q2-04·q2-06 답함(3절 {#q2-04}·{#q2-06} 신설), q2-02 비교표 보정 소절, 2절 표 갱신(q2-10·q2-11 추가), 4·5·7·8절 보강, 6절 완료 조건 미충족·미승인, 9절 이력 행 추가 |
| update | docs/tracks/floorplan-recognition/stage-1-prior-work-and-products.md | draft | 3절에 q1-08 보강 소절 추가(f21 벤더 주장·연계 대상, f22 국내 단계별 시간 자료 여전히 찾지 못함), 8절 출처에 ref-1438 추가. q1-08 은 조사 중(표에서는 열림) 유지 |
| update | docs/tracks/floorplan-recognition/space-graph-schema-draft.md | draft | 초안 v1.2 → v1.3: 충전 위치에 속성 'BIM 표현(후보)' 추가(f11·f12·f13·f14·f17, 실행 2026-10-09-24, 확정 유지), 3절 관계 변경 없음 메모, 6절 q2-06 근거 보강(IDS 납품 요구 방식·충전소 관례 부재)과 CubiCasa5K 계단 출처 충돌 메모 |
| update | docs/ideas/floorplan-recognition.md | draft | 3절에 공개 데이터셋 비교표 보정 소절(CubiCasa5K 계단·라이선스, AI Hub 엘리베이터·계단), 4절에 학습 데이터 라벨·이용 조건과 표준 밖 운영 시설의 BIM 표현·IDS 납품 요구 소절 추가 |
| update | docs/tracks/floorplan-recognition/index.md | draft | 6절에 실행 2026-10-09-24 요약 단락 추가(q2-04·q2-06 답함, 스키마 초안 v1.3, 후속 질문 q2-11·q3-13). 상태 줄(현재 단계 2, 마지막 트랙 실행 2026-10-09)은 값이 같아 그대로 |

## 변경 이력·색인

- 변경 이력: 2026-10-09 | 건축 도면 자동 인식 단계 2 | q2-04·q2-06 답함, q1-08 보강(조사 중 유지), 공간 그래프 스키마 초안 v1.2 → v1.3(충전 위치 'BIM 표현(후보)'), oq-197 해결 | run 2026-10-09-24
- 홈 최근 업데이트: 2026-10-09 — 건축 도면 자동 인식 단계 2: AI Hub·CubiCasa5K 의 계단·엘리베이터 라벨과 이용 조건(q2-04), 표준 밖 운영 시설의 IFC 표현과 IDS 납품 요구(q2-06) 정리, 공간 그래프 스키마 초안 v1.3
- 대분류 최근 업데이트: 2026-10-09 — 14. 도면·BIM에서 지도 만들기(트랙 건축 도면 자동 인식 단계 2): 도면 학습 데이터의 계단·엘리베이터 라벨과 라이선스, IFC 프록시·사용자 정의 속성 세트·IDS 1.0 확인, 반영 제안 3건
- 세부영역 최근 업데이트: 2026-10-09 — 14. 도면·BIM에서 지도 만들기: 트랙 실행 2026-10-09-24 가 7·8·11절 반영을 제안(IDS 1.0, IFC 프록시·사용자 정의 속성 세트, AI Hub·CubiCasa5K 라벨·라이선스, oq-197 해결 근거)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | buildingSMART 데이터 사전 | buildingSMART Data Dictionary (bSDD) | buildingSMART 가 IDS 를 작성할 때 쓸 수 있는 공유 속성 라이브러리로 설명하는 데이터 사전. | 14, 21 | ref-1433 |
| new | 건물 요소 프록시 | Building Element Proxy (IfcBuildingElementProxy) | 미리 정해진 의미 없이 건축 요소와 같은 기능을 하는 IFC 엔터티로, 응용이 의미를 정의할 수 없는 요소를 교환할 때 쓰며 PredefinedType 을 USERDEFINED 로 두면 ObjectType 으로 유형 이름을 적어야 한다. | 14, 21 | ref-1432 |
| new | 사용자 정의 속성 세트 | User-defined Property Set | IFC 명세에 선언되지 않은 프로젝트·조직 고유의 속성 묶음으로, 표준 세트에만 쓰는 'Pset_' 접두어 없이 이름을 짓고 IfcRelDefinesByProperties 등으로 객체에 붙인다. | 14, 21 | ref-1431 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-1427 | Zenodo (CubiCasa) | CubiCasa5k | 오픈소스 문서 | high | https://zenodo.org/record/2613548 |
| ref-1428 | CubiCasa (CubiCasa/CubiCasa5k GitHub) | CubiCasa5k — floortrans/loaders/house.py | 오픈소스 문서 | high | https://github.com/CubiCasa/CubiCasa5k/blob/master/floortrans/loaders/house.py |
| ref-1429 | 경기도 고양시(공공데이터포털) | 경기도 고양시_어린이 음성맥락 인식률 향상을 위한 방송 음성 및 자연어 처리(AI학습용)_20240105 | 정부·연구기관 | medium | https://www.data.go.kr/data/15146382/fileData.do |
| ref-1430 | 바이라인네트워크(이진호) | 모을 수 있는 데이터는 다있다…11억건 넘는 데이터 나눠주는 ‘AI 허브’ | 기사 | low | https://byline.network/2022/09/0905_03/ |
| ref-1431 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcPropertySet (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 표준 | high | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcKernel/Entities/IfcPropertySet.md |
| ref-1432 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcBuildingElementProxy (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 표준 | high | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/shared/IfcSharedBldgElements/Entities/IfcBuildingElementProxy.md |
| ref-1433 | buildingSMART International | Information Delivery Specification (IDS) | 표준 | high | https://www.buildingsmart.org/standards/bsi-standards/information-delivery-specification-ids/ |
| ref-1434 | buildingSMART (buildingSMART/IDS GitHub) | IDS — Documentation/UserManual/README.md | 표준 | high | https://github.com/buildingSMART/IDS/blob/development/Documentation/UserManual/README.md |
| ref-1435 | Construction Information Limited (Masterspec, 뉴질랜드) | 4.0 Object Properties & Property Grouping — 4.3 IFC properties (Open BIM Object standard (OBOS) V1.0) | 업계 보고서 | medium | https://masterspec.co.nz/43-IFC-Properties/7266/ |
| ref-1437 | Pauwels, P., de Koning, R., Hendrikx, B., & Torta, E. (Advanced Engineering Informatics 56, 101959) | Live semantic data from building digital twins for robot navigation: Overview of data transfer methods | 논문 | medium | https://research.tue.nl/en/publications/live-semantic-data-from-building-digital-twins-for-robot-navigati/ |
| ref-1438 | Robotics 24/7 | RGo Robotics introduces AI-powered Intelligent Mapping system | 기사 | low | https://www.robotics247.com/article/rgo-robotics-introduces-ai-powered-intelligent-mapping-system |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 출처 충돌: CubiCasa5K 는 계단을 학습 라벨로 제공하는가? 이전 실행의 검색 요약은 CubiCasa5K 가 계단을 주석한다고 전하지만, 공식 코드는 Stairs 처리 블록을 주석 처리하고 계단실·엘리베이터를 일반 방으로 합친다. 원 SVG 주석에는 계단·엘리베이터가 별도 범주로 남아 있는가? | 14, 45 | 열림 | — |
| new | — | AI허브 건축 도면 데이터의 원 이용약관은 학습 모델의 상업적 이용, 데이터 재가공·재배포, 해외 활용을 어떻게 규정하며, 공공데이터포털 샘플 페이지가 옮긴 조건과 '국내에서만 활용' 안내가 이 데이터셋에도 그대로 적용되는가? | 14, 59 | 열림 | — |
| new | — | 국내 공공건축 BIM 납품 기준(건설산업 BIM 시행지침 등)이나 로봇 친화형 건축물 인증이 로봇 충전 공간·작업 스테이션을 BIM 객체·속성으로 납품하도록 요구하거나 그 IDS·속성 세트를 정한 사례가 있는가? (관련 기존 질문: oq-199) | 14, 21 | 열림 | — |
| update | oq-197 | AI Hub 건축 도면 데이터의 라벨(구조 8종·공간 12종·객체 5종)에 충전 위치처럼 로봇 운영에 필요한 클래스가 들어 있는가, 비주거 건물 도면은 얼마나 포함되는가? | 14, 45 | 해결 | docs/tracks/floorplan-recognition/stage-2-data-and-standards.md#q2-04 |

## 현장 유형 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| Open BIM Object standard (OBOS) V1.0 — IFC 속성 규칙(4.3) | 표준 | Construction Information Limited (Masterspec, 뉴질랜드) | 14, 21 | ref-1435 | https://masterspec.co.nz/43-IFC-Properties/7266/ |

## 추가 조사 요청

- 단계 2 페이지 H1 아래 단계 상태 줄(열린 질문 5건·답한 질문 3건·마지막 실행 2026-09-25)은 H2 절 밖이라 patches 로 고칠 수 없다. 이번 실행 기준 값은 열린 질문 5건(q2-07·q2-08·q2-09·q2-10·q2-11)·답한 질문 5건·완료 조건 미충족·마지막 실행 2026-10-09 이며, 패치 적용 코드에서 갱신해 주기를 pipeline 담당에게 요청한다.
- 공간 그래프 스키마 초안 H1 의 '(v1.2)' 표기는 H2 절 밖이라 patches 로 고칠 수 없다. 프런트매터 ontology_version 을 '1.3' 으로 보냈으므로 패치 적용 시 H1 을 '(v1.3)' 으로 맞추도록 pipeline 담당에게 요청한다.
- q2-04 의 남은 불확실성: AI허브 이용약관·이용정책 원문(aihub.or.kr 이용정책 페이지)을 열어 학습 모델 상업 이용·재가공 배포·해외 활용 조건을 1차 자료로 확인할 필요가 있다.
- q2-06 의 남은 불확실성: IDS 패싯별 값 제한(열거·패턴·범위) 문법과 USERDEFINED·사용자 정의 속성 세트를 요구하는 IDS 예시를 IDS 공식 저장소 문서로 확인할 필요가 있다.
- q1-08 은 여전히 부분 답이다. 국내 물류센터 로봇 도입의 지도 작성·공용 자원 등록·좌표 정렬 단계별 소요 시간 공개 자료(한국로봇산업진흥원 실증 결과 보고서 등)를 계속 찾을 필요가 있다.
- eCAADe 2025 예고 논문(ref-1436, JuBot 프로젝트)은 제목·저자를 확인하지 못해 본문에서 뺐다. 원문 제목·저자를 확인하면 IFC 4.3 로봇 안내용 확장 제안 사례로 다시 검토할 수 있다.

## 이행한 수정 지시

- f18 삭제 — 단계 2 페이지·아이디어 페이지·스키마 초안 어디에도 싣지 않았고, reference_updates 와 단계 2 페이지 8절 출처에서 ref-1436 을 뺐으며, q2-06 종합 문장의 근거 목록과 '확장 제안' 언급도 넣지 않았다.
- f9 — 단계 2 페이지 q2-04 종합 문장과 아이디어 4절 소절에서 '상용 이용에는 권리자의 별도 허락이 필요할 것으로 보이며(법적 판단 아님)'로 쓰고 AI Hub 라벨이 주거(아파트 코어) 도면 기준이라는 단서를 유지했다.
- f5 — 근거가 다른 데이터셋(고양시 어린이 음성) 공공데이터포털 페이지의 2차 기술이라는 점과 법적 판단이 아니라는 단서를 단계 2 페이지 q2-04 와 아이디어 4절 문장에 적었다.
- f3 — 기준일을 '출처 발행 2025-08-16, 확인일 2026-10-09'로 적고 2026-06-16 은 쓰지 않았다.
- f2 — '이용정책 메뉴 링크만 둔다'로 고쳐 단계 2 페이지 q2-04 에 썼다.
- f13 — 유형 객체 연결을 '직접 연결(속성 세트의 역속성 DefinesType)'로 써 단계 2 페이지 q2-06 과 아이디어 4절에 반영했고 HasPropertySets 표현은 쓰지 않았다.
- f12 — 'IfcTransportElement 에도 USERDEFINED 일 때 ObjectType 을 요구하는 형식 제약이 있다'로 한정해 썼고 IFC 전반으로 일반화하지 않았다.
- f17 — IFC4 (Add2) 기준의 뉴질랜드 OBOS V1.0 관례이며 로봇 충전소 대상 규정이 아님을 밝히고 발행일 미확인으로 두었다(단계 2 페이지·아이디어 4절·각주 발행일 미확인).
- f19 — BIM 기반 주행 시험 앞에 '연계 대상:'을 붙이고 디지털 트윈을 건물 데이터 저장소(현재 상태 쪽, 18. 실시간 세계 상태·데이터 일관성) 의미로만 서술해 34. 시뮬레이션·예측용 디지털 트윈과 구분했다.
- f21 — 단계 1 페이지 q1-08 보강 소절에서 '연계 대상:'·[추정]·벤더 주장을 유지하고, 수개월 수작업 병목과 며칠 안에 끝나는 자동 과정 서술은 기사 서술로, 수개월→며칠 단축은 RGo 측 주장(혜택 목록)으로 나눠 적었다.
- f7·출처 충돌 — 단계 2 페이지 3절 'q2-02 비교표 보정' 소절과 아이디어 3절 '공개 데이터셋 비교표 보정' 소절에서 기존 'CubiCasa5K 계단 라벨 있음'을 지우지 않고 지시 문구를 병기했다. patches 가 H2 절 단위만 바꿀 수 있어 원 표 칸 대신 같은 절 끝 보정표로 반영했으며, open_questions_new 1번을 출처 충돌로 등록했다.
- f1 — 단계 2 페이지 q2-02 래스터 열 엘리베이터 칸과 아이디어 3절 AI Hub 행 '엘리베이터·계단' 칸을 지시 문구로 보정표에 갱신하고 각주는 ref-1012 를 썼다(ref-074 새로 인용 안 함). 원 표 칸 직접 수정은 위와 같은 patches 제약으로 보정표 방식으로 이행했다.
- q2-04 답 — 3절 {#q2-04} 를 '클래스 구성(원문 확인 근거)'(f1·f6·f7·f8·f10)과 '이용 조건(2차 근거와 추정)'(f2·f3·f4·f5·f9)으로 나눠 쓰고, AI허브 원 약관 미열람을 4절 남은 불확실성에 두었다.
- q2-06 답 — 3절 {#q2-06} 을 IFC 4.3 규칙(f11~f14)·IDS(f15·f16)·실무 관례(f17)·연구(f19)·종합(f20, 추정·low)으로 구성하고 f18 은 넣지 않았으며, IDS 첫 등장을 '정보 전달 명세(Information Delivery Specification, IDS)'로 쓰고 ../../glossary/information-delivery-specification.md 에 연결했다.
- 온톨로지 — 충전 위치 행에 속성 'BIM 표현(후보)'을 지시 문구대로 더하고 근거 칸에 finding f11·f12·f13·f14·f17 (실행 2026-10-09-24)과 각주 ref-1432·ref-213·ref-1431·ref-214·ref-215·ref-1435 를 두었으며 상태는 확정을 유지했다. 프런트매터 ontology_version·track_updates.ontology_draft_version 을 '1.3' 으로 맞췄고 상태 표식은 프런트매터에서 자동으로 채워진다. H1 '(v1.3)' 은 H2 절 밖이라 patches 로 고칠 수 없어 additional_research_requests 로 코드 반영을 요청했다. IDS 방식과 충전소 관례 부재는 6절 근거 보강으로 두고 작업 스테이션에는 적용하지 않았다.
- 용어집 — bSDD 정의를 'buildingSMART 가 IDS 를 작성할 때 쓸 수 있는 공유 속성 라이브러리로 설명하는 데이터 사전'으로 고쳐 냈고 IDS 는 새로 등록하지 않았다.
- 새 트랙 질문 — 단계 2 질문을 q2-11 로 질문 끝에 '(관련: q2-10, oq-341)'을 붙여 등록하고, 단계 3 질문을 q3-13 으로 그대로 등록했다.
- open_questions_new 3번 — 질문 끝에 '(관련 기존 질문: oq-199)'를 붙이고 관련 영역 14·21 로 등록했다.
- oq-197 — f1·f10 근거로 status 해결, link 단계 2 페이지 #q2-04 로 냈고 q2-04 본문에 해결 근거를 적었다.
- 단계 2 페이지 2절 — q2-04·q2-06 을 답함(답한 실행 id 2026-10-09-24, 답 위치 #q2-04·#q2-06, 3절 소제목 명시 id)으로 바꿨다. 단계 1 페이지 q1-08 은 2절을 고치지 않아 열림(백로그 조사 중)을 유지하고 3절에 q1-08 보강 소절로 f21·f22 를 더했다.
- 단계 2 페이지 6절 — 두 행 모두 '미충족', 검증 판정 '미충족 · 미승인'으로 두고 전환 줄을 지시 문구 그대로 썼으며 track_updates.stage_transition 은 넣지 않았다.
- ref-214·ref-215 — reference_updates 에 새 항목을 만들지 않고 기존 각주 정의를 재사용했다.
- 세부영역 반영 제안 — 14. 도면·BIM에서 지도 만들기, 45. 문서·도면·장면 이해, 21. 상호운용 표준·적합성 제안을 area_reflection_proposals 로만 내고 세부영역 페이지는 고치지 않았으며 근거에서 f18 을 뺐다.

## 트랙 갱신

- 단계 페이지: docs/tracks/floorplan-recognition/stage-2-data-and-standards.md
- 온톨로지 초안 버전: 1.3
- 트랙 로그 항목: 답한 질문: q2-04(f1·f2·f3·f4·f5·f6·f7·f8·f9·f10), q2-06(f11·f12·f13·f14·f15·f16·f17·f19·f20, f18 은 출처 실재 미확인으로 삭제); q1-08 부분 답 보강(f21·f22, 조사 중 유지) / 새 질문: q2-11(f1, 단계 2), q3-13(f20, 단계 3) / 온톨로지 변경: v1.2 → v1.3: 개념 '충전 위치'에 속성 'BIM 표현(후보)' 추가(f11·f12·f13·f14·f17). 버전 이력 행: 1.3 | 2026-10-09 | 충전 위치 속성 'BIM 표현(후보)' 추가(f11·f12·f13·f14·f17), 거부 없음(IDS 납품 요구 방식은 6절 근거 보강) | 2026-10-09-24 / 완료 조건 평가: 미충족(부족: 관계(엣지) 쪽 표준 대응 없음; 열린 질문 q2-07·q2-08·q2-09·q2-10·q2-11; 되돌아온 단계 1 질문 q1-08 조사 중) / 세부영역 반영 제안: 14. 도면·BIM에서 지도 만들기 3건, 45. 문서·도면·장면 이해 1건, 21. 상호운용 표준·적합성 1건 / 다음 실행 제안: q2-07, q2-08, q2-09
- 개요 진행 현황: 단계 2 진행 중 — 열린 질문 5, 답함 5, 완료 조건 미충족

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q2-04 | 답함 | docs/tracks/floorplan-recognition/stage-2-data-and-standards.md#q2-04 | — | — | — |
| q2-06 | 답함 | docs/tracks/floorplan-recognition/stage-2-data-and-standards.md#q2-06 | — | — | — |
| q1-08 | 조사 중 | — | — | — | — |
| q2-11 | 열림 | — | AI Hub 건축 도면 데이터의 엘리베이터·엘리베이터홀·계단실 라벨(아파트 코어 기준)로 학습한 모델이 물류센터·병원 같은 비주거 도면의 화물용 승강기·계단실을 얼마나 인식하는가, 라벨 정의서는 계단실과 엘리베이터 영역을 어떤 기준으로 그리는가? (q2-04 에서 파생) (관련: q2-10, oq-341) | 2 | f1 |
| q3-13 | 열림 | — | ROP 가 BIM 납품 요구로 쓸 로봇 운영 시설용 IDS(충전 위치·작업 스테이션을 관련 엔터티나 IfcBuildingElementProxy 의 USERDEFINED 와 ObjectType 값 목록으로 지정하고, 'Pset_' 가 아닌 프로젝트 속성 세트에 접근 자세·도킹 이름·상호작용 노드 속성을 요구하는 형태)를 어떤 항목으로 정의하며, 설계·시공 측이 그 값을 채울 수 있는가, 채울 수 없으면 어느 단계에서 누가 보완하는가? (q2-06 에서 파생) | 3 | f20 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 14 | 7. 관련 표준·프레임워크·오픈소스 | IDS 1.0(2024-06-01 승인, 객체·분류·재료·속성·값 전달 요구, 기하 제외)과 IFC 4.3 의 IfcBuildingElementProxy·USERDEFINED·ObjectType 규칙, 'Pset_' 접두어 없는 사용자 정의 속성 세트 규칙을 BIM 입력 요구 수단으로 추가(f11·f13·f15, 종합 f20 은 추정). 근거 ref-1432·ref-1431·ref-1433. |
| 14 | 8. 대표 연구와 자료 | AI Hub 건축 도면 데이터는 엘리베이터·엘리베이터홀·계단실을 공간 클래스로 두고(주거 도면 기준, 로봇 운영 클래스 없음) CubiCasa5K 는 CC BY-NC-SA 4.0 이며 공식 학습 매핑에서 계단·엘리베이터가 따로 남지 않는다는 점(f1·f6·f7, 출처 충돌 열린 질문 병기). 근거 ref-1012·ref-1427·ref-1428. |
| 14 | 11. 열린 질문 | oq-197 해결(f1·f10: AI Hub 라벨에 로봇 운영 클래스 없음, 도면 48,033장 모두 주거 유형)과 새 열린 질문(CubiCasa5K 계단 출처 충돌, AI허브 원 약관, 국내 BIM 납품 기준의 충전 공간 요구) 반영. |
| 45 | 8. 대표 연구와 자료 | 교차 규칙(도면 해석은 14. 도면·BIM에서 지도 만들기에 적용)에 따라 도면 해석 학습 데이터의 클래스 구성(CubiCasa5K 학습 매핑에서 엘리베이터·계단실이 일반 방으로 합쳐짐, AI Hub 공간 클래스)과 이용 조건(CubiCasa5K 비상업, AI허브 2차 근거 기준 재배포 제한 — 추정·법적 판단 아님)을 반영(f1·f5·f6·f7·f9). |
| 21 | 7. 관련 표준·프레임워크·오픈소스 | IDS 1.0 의 적용 대상·요구 구조와 Entity·Attribute·Classification·Property·Material·PartOf 패싯, IFC 사용자 정의 속성 세트 명명 규칙, 뉴질랜드 OBOS V1.0 의 프록시 내보내기 관례(IFC4 Add2 기준)를 BIM 데이터 교환 요구·적합성 검사 수단으로 반영(f13·f15·f16·f17). |
