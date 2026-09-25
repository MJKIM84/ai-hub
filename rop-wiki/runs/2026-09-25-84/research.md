# 리서치 브리프 2026-09-25-84

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-84 |
| 날짜 | 2026-09-25 |
| 실행 유형 | track (트랙 실행) |
| 대상 영역 | 6. 지도·공간·위치 모델 |
| 대분류 | B. 공통 정보·환경 모델 |

트랙 실행: 트랙 `floorplan-recognition` · 단계 5 · 답한 질문 q5-03

## 갭(비어 있거나 약한 섹션)

- 단계 5 질문 q5-03 열림(target.json 지정, CLI 지정 질문 id). 단계 5 페이지 3절에 q5-03 소제목 없음
- 완료 조건: 가설 판정표가 트랙 개요 3절에 없음(가설 1~3 모두 미판정, 판정 규칙도 정해지지 않음)
- 완료 조건: 사용자에게 제안하는 실험 계획이 실험 페이지에 없음(판정에 필요한 실험을 정할 근거가 없음)
- 아이디어 3. 건축 도면 자동 인식 6절에 가설 판정 절차(근거 수준 평가와 판정 값 규칙)가 없음
- 23. 시험·형식 검증·벤치마크 섹션 6에 여러 출처의 근거를 모아 확실성 수준을 매기는 방법 근거 없음

## 조사 질문

1. 제조사마다 다른 지도에서 ‘3층 출하 대기장’을 어떻게 동일한 장소로 인식할까? [분류원문]
2. q5-03 가설 1~3은 단계 1~4의 결과로 어떻게 판정되는가?
3. 여러 출처의 근거를 모아 결론의 확실성을 등급으로 매기는 체계(GRADE, 소프트웨어 공학의 근거 강도 평가)는 어떤 요소로 확실성을 낮추거나 올리는가? (단계 5 페이지 3절, 23. 시험·형식 검증·벤치마크 겨냥)
4. 기술 성숙도(TRL, 국내 기술성숙도평가 업무지침)는 실험실 검증과 관련 환경 시연을 어떻게 구분하며, 가설 판정의 보조 축으로 쓸 수 있는가? (한국 자료 우선 규칙)
5. 단계 1~4 에서 확인한 근거는 가설 1(인식으로 초안 생성)·가설 2(능력 대조)·가설 3(시간 단축·시뮬레이션 초기값)의 하위 주장별로 무엇을 뒷받침하고 무엇이 비는가? (트랙 개요 3절 겨냥)
6. 물류센터 조건에서 도면 기반 지도 생성의 시간 단축이나 인식 성능을 직접 잰 새 연구·국내 사례가 있는가? (가설 판정의 직접 근거 여부)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | GRADE 접근법은 근거 묶음의 확실성을 결과(outcome)별로 높음·중간·낮음·매우 낮음 네 수준으로 매기고, 비뚤림 위험·비일관성·비직접성·비정밀성·출판 비뚤림 다섯 영역으로 확실성을 낮춘다. | ref-807 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f2 | [사실] | Dybå·Dingsøyr(ESEM 2008)는 소프트웨어 공학 체계적 문헌고찰에 근거 강도 평가를 처음 적용한 연구로, GRADE(2004판)를 풀어 설명하고 질적·관찰 연구를 함께 다루는 근거 강도 등급 체계를 검토했다. | ref-808 | 아니오 | medium | 2008 | — | 원문 미열람 |
| f3 | [사실] | NASA 의 기술 준비 수준(TRL) 정의는 TRL 5 를 관련 환경에서의 구성품·하위 시스템 검증, TRL 6 을 관련 환경의 종단간 시제품 시연으로 두어 실험실 규모와 공학 규모 검증을 구분한다. | ref-809 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f4 | [사실] | 방위사업청 '기술성숙도평가(TRA) 업무지침'은 기술성숙도(TRL)를 기술이 실제 적용에 얼마나 준비되었는지를 확인하는 정량 수준으로, 기술성숙도평가를 핵심기술요소의 성숙도를 정량 평가하는 공식 절차로 정의하며 TRL 6 이면 체계개발 진입이 가능하다고 본다. | ref-810 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f5 | [사실] | CubiCasa5K 는 래스터 평면도 5,000장에 방·창문·문 등 아이콘과 벽·난간·계단을 주석한 데이터셋이며, 엘리베이터 범주는 확인되지 않았다. | ref-063 | 아니오 | medium | 2019-04 | — | 원문 미열람 |
| f6 | [추정] | 공개 평면도 데이터셋 가운데 엘리베이터 범주는 FloorPlanCAD 의 제3자 데이터셋 카드에서만 확인되어, 래스터·벡터 인식으로 엘리베이터를 추출할 수 있다는 근거는 약한 것으로 보인다. | ref-068, ref-063 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f7 | [사실] | IFC 4.3(개발 브랜치 기준)은 엘리베이터를 운송 요소 유형 값 ELEVATOR 로, 문·계단을 IfcDoor·IfcStair 로 담아 BIM 입력에서는 이 요소들이 인식 없이 유형 객체로 주어질 수 있다. | ref-421, ref-213 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f8 | [사실] | IFC 4.3 의 콘센트 유형 열거와 전기기기 유형 열거에는 로봇·차량 충전 설비 값이 없어, 충전 위치는 BIM 표준 유형으로 도면에 담기지 않는 것으로 확인된다. | ref-214, ref-215 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f9 | [사실] | Open-RMF traffic-editor 에서는 충전소·주차 위치·도킹 이름·작업셀 이름 같은 운영 요소를 사람이 경유점 속성으로 입력한다. | ref-079 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f10 | [추정] | 이전 실행들의 검색 범위에서 물류센터·창고 평면도나 충전 위치를 라벨로 담은 공개 인식 데이터셋은 찾지 못해, 가설 1 의 근거는 주거·상업 평면도에 대한 간접 근거에 머무는 것으로 보인다(부재 확인 아님). | ref-063, ref-073, ref-074 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f11 | [사실] | 능력 기술 서브모델 IDTA 02020(1.0)은 요구 능력과 제공 능력을 모델링해 비교하게 하고 속성 제약을 전제조건으로 쓸 수 있게 하여, 공간 통과 조건과 로봇 능력을 같은 틀로 대조할 표현 수단이 존재한다. | ref-229 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f12 | [사실] | VDA 5050 팩트시트 스키마와 Open-RMF 플릿 어댑터 템플릿 설정은 속도·크기·배터리 같은 파라미터는 두지만 계단·문·승강기 이용 능력 필드는 두지 않아, 가설 2 의 대조에 쓸 로봇 쪽 능력 값이 관제 인터페이스에서 오지 않는다. | ref-228, ref-105 | 아니오 | medium | 2026-09-25 | 수행 자원 | 원문 미열람 |
| f13 | [사실] | IFC 4.3.2 의 문 공통 속성 세트는 자동 구동 여부·장애인 접근 가능을, 계단 공통 속성 세트는 단 높이·디딤판 길이·단 수를 두어 공간 쪽 통과 조건 값은 BIM 에서 얻을 수 있다. | ref-573, ref-574 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f14 | [사실] | 연계 대상: Open-RMF 에서 문 여닫기는 로봇이 아니라 문 어댑터가 처리하므로, 문 통과 가능 여부는 로봇 능력만이 아니라 설비 연동 여부에도 달려 가설 2 의 대조 규칙이 선택 조건을 가져야 한다. | ref-283 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f15 | [추정] | Opiela·Hrehová(IPIN-WiP 2023)는 평면도 지도 모델 주석에서 숙련자 수작업 40분 대비 자동 주석 뒤 수정 5분을 보고했으나, 지도 1건의 저자 보고이고 물류 로봇 설정 작업이 아니다. | ref-794 | 아니오 | low | 2023 | — | 원문 미열람 |
| f16 | [추정] | EU CORDIS 기사는 PAN-Robots 시스템이 AGV 설치 기간을 6개월에서 2개월로 줄일 수 있다고 전하나, 과제 측 보고값이며 비교 조건은 확인되지 않았다. | ref-265 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f17 | [추정] | OTTO Motors 는 소프트웨어 2.28 판에서 시설 지도·작업 흐름 설정 시간이 내부 시험으로 50% 줄었다고 밝힌다. | ref-271 | 아니오 | low | 2023 | — | 원문 미열람, 벤더 주장 |
| f18 | [사실] | Open-RMF building_map_generator 는 사람이 주석한 건물 파일에서 주행 그래프와 함께 바닥·벽·문·승강기를 담은 시뮬레이션 월드를 만들어, 도면 기반 결과를 시뮬레이션 초기값으로 옮기는 경로가 존재한다. | ref-441, ref-406 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f19 | [사실] | IFAC 2024 논문은 운영 결정용 시뮬레이션 기반 디지털 트윈을 실제 부하 상태로 초기화하면 빈 상태 기준 모델보다 과도 구간이 크게 줄어든다고 보고해, 도면 기반 정적 초기값만으로는 운영 예측용 초기값이 되지 않음을 시사한다. | ref-632 | 아니오 | medium | 2024 | 시작 조건 | 원문 미열람 |
| f20 | [사실] | 연계 대상: BIM 에서 만든 점유 격자 지도는 구조 요소만 담아 가구·설계–시공 편차가 위치추정 정확도를 떨어뜨린다고 보고되어, 도면 기반 지도가 현장 운영 지도로 바로 쓰이지 않는다는 반대 방향 근거가 된다. | ref-081 | 아니오 | medium | 2023-08 | — | 원문 미열람 |
| f21 | [추정] | q5-03 에 대해 확인한 근거 평가 체계를 이 위키가 묶으면, 가설 판정은 각 가설을 하위 주장으로 나누고 하위 주장마다 근거의 확실성을 GRADE 식 영역(비직접성: 주거·사무 건물 대 물류센터, 비정밀성: 단일 출처·표본 1건, 비뚤림: 저자·과제·벤더 보고)으로 낮춰 매긴 뒤 판정 값으로 모으는 절차가 근거가 가장 많은 것으로 보인다. | ref-807, ref-808 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f22 | [추정] | 판정 값 규칙은 지지(핵심 하위 주장 모두 물류 조건의 직접 근거가 있고 확실성 중간 이상), 부분 지지(일부 하위 주장만 근거가 있거나 빠지는 부분이 확인됨), 기각(핵심 하위 주장에 직접 반대 근거), 미판정(핵심 하위 주장에 직접 근거 없음)으로 두고, 기술 성숙도 수준(실험실 대 관련 환경 시연)을 보조 축으로 병기하는 방식이 가능해 보인다. | ref-807, ref-809, ref-810 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f23 | [추정] | 위 규칙을 단계 1~4 결과에 적용하면 가설 1 은 벽·문·계단 인식 근거와 BIM 의 엘리베이터 유형은 있으나 충전 위치·운영 요소는 도면에 담기지 않고 근거가 주거 평면도 중심이어서 잠정 '부분 지지'(확실성 낮음)로 보이며, 빠지는 것은 충전 위치·작업 스테이션·주행 차선·도면–현장 편차로 정리된다. | ref-063, ref-068, ref-421, ref-214, ref-079, ref-081 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f24 | [추정] | 가설 2 는 요구–제공 능력 비교의 표현 수단과 BIM 쪽 통과 조건 값은 확인되지만 로봇 쪽 능력 값이 관제 인터페이스에 없고 대조 판정의 정확도를 잰 근거가 없어, 잠정 '부분 지지'(표현 가능성만 확인, 확실성 낮음)로 보인다. | ref-229, ref-228, ref-105, ref-573, ref-283 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f25 | [추정] | 가설 3 은 시간 단축 근거가 물류 로봇 설정이 아닌 주석 1건의 저자 보고·과제 보고·벤더 주장뿐이고, 시뮬레이션 초기값은 월드 생성 경로만 있고 예측 정확도를 비교한 근거가 없어 '미판정'으로 두고 사용자 실험이 필요한 것으로 보인다. | ref-794, ref-265, ref-271, ref-441, ref-632 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f26 | [추정] | 판정을 미판정·부분 지지에서 옮기려면 물류센터 도면으로 q5-01 의 세 층 지표를 재는 인식 실험(가설 1), 능력 대조 판정과 실제 주행 결과를 비교하는 통행 실험(가설 2), 수작업 대 자동 생성+보정의 두 조건 모델링 시간 실험과 시뮬레이션 예측 대 현장 측정 비교(가설 3)가 사용자 실험 계획으로 필요할 것으로 보인다. | ref-809, ref-807 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f27 | [추정] | ‘3층 출하 대기장’ 사례로 보면 가설 1 은 대기장 구역·승강기를 도면에서 얻는지, 가설 2 는 승강기 엣지를 포함한 경로가 각 제조사 로봇의 통행 가능 부분 그래프 안에 있는지, 가설 3 은 도면 수신부터 첫 도착 인정까지의 설정 시간이 줄었는지로 각각 판정 항목이 나뉠 수 있어 보인다(설명용 가정 사례). | ref-079, ref-229, ref-794 | 아니오 | low | 2026-09-25 | 출하 / 예외·성과 | 원문 미열람 |
| f28 | [추정] | 이번 검색 범위(한국어 2회 포함 8회)에서는 물류센터에서 도면 기반 지도 생성의 인식 성능이나 시운전 시간 단축을 직접 잰 새 연구·국내 사례를 찾지 못해, 세 가설 모두 물류 조건의 직접 근거가 비어 있는 것으로 보인다(부재 확인 아님). | ref-217, ref-794 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |

### 근거 발췌

- **f1**: Cochrane Handbook 14장 검색 요약: 확실성은 다섯 영역(risk of bias, inconsistency, indirectness, imprecision, publication bias)을 고려해 결정되고 high/moderate/low/very low 로 분류된다. (발행일 미확인, 확인일 기준)
- **f2**: 검색 요약: ESEM 2008, 178–187쪽. 체계적 문헌고찰은 근거한 증거만큼만 좋다는 원칙 아래 1차 연구 질 평가와 근거 묶음 강도 등급 체계를 개관했다.
- **f3**: 검색 요약: TRL 5 는 대표 환경에서 시제품을 철저히 시험, TRL 6 은 관련 종단간 환경에서 시스템·하위 시스템 모델 또는 시제품 시연. (발행일 미확인, 확인일 기준)
- **f4**: 검색 요약: 핵심기술요소(CTE)의 성숙도를 정량 평가하는 공식 절차; TRL 6 평가 시 체계개발 진입 가능. 2021-07-23 방위사업청 훈령 제725호 제정 기준(스니펫). (발행일 미확인, 확인일 기준)
- **f5**: 5,000장, 80여 범주, 계단 있음·엘리베이터 미확인(주거 평면도). 가설 1 의 벽·문·계단 인식 하위 주장 근거. (재인용: 2026-09-25-05)
- **f6**: FloorPlanCAD 엘리베이터·에스컬레이터 범주는 Voxel51 카드(제3자) 검색 요약 기준. (재인용: 2026-09-25-05)
- **f7**: IfcTransportElementTypeEnum 에 ELEVATOR, IfcTransportElement 는 엘리베이터·에스컬레이터·무빙워크를 예로 듦(같은 발행 주체). (재인용: 2026-09-25-36)
- **f8**: IfcOutletTypeEnum·IfcElectricApplianceTypeEnum 에 충전 설비 값 없음, USERDEFINED·NOTDEFINED 만(같은 발행 주체라 독립 교차 확인 아님). (재인용: 2026-09-25-19)
- **f9**: 경유점 속성 is_charger, is_parking_spot, dock_name, 디스펜서·인제스터 이름을 편집기에서 사람이 입력. (재인용: 2026-09-25-19)
- **f10**: CubiCasa5K·ArchCAD-400K·AI Hub 건축 도면 데이터 모두 물류 시설·충전 위치 라벨 미확인. (재인용: 2026-09-25-05)
- **f11**: 요구·제공 능력 모델링과 속성 제약 비교. 가설 2 의 표현 가능성 하위 주장 근거. (재인용: 2026-09-25-65)
- **f12**: 팩트시트 physicalParameters·typeSpecification, 템플릿 속도·차체 반경·배터리 — 계단·문·승강기 능력 필드 없음. (재인용: 2026-09-25-65)
- **f13**: Pset_DoorCommon.HasDrive·HandicapAccessible, Pset_StairCommon.RiserHeight·TreadLength·NumberOfRiser(공식 문서 검색 요약 기준). (재인용: 2026-09-25-65)
- **f14**: 문 어댑터가 DoorRequest 를 받아 진행 중인 로봇 작업을 방해하지 않을 때만 문 노드에 지시. (재인용: 2026-09-25-65)
- **f15**: IPIN 2019 대회 지도 1건, 자동 처리 시간 포함 여부 미확인, 이전 검증 재검색에서 수치 미재확인. (재인용: 2026-09-25-82)
- **f16**: 과제 측 보고값, 비교 조건·측정 방법 미확인(q5-04 열림). (발행일 미확인, 확인일 기준) (재인용: 2026-09-25-22)
- **f17**: 벤더 주장: 내부 시험, 측정 조건 미공개. 가설 3 판정 근거로 쓰지 않는 사례. (재인용: 2026-09-25-22)
- **f18**: .building.yaml → 주행 그래프 파일과 Gazebo 월드 생성(같은 Open Robotics 자료라 독립 교차 확인 아님). (재인용: 2026-09-25-70)
- **f19**: SAP EWM 배송 센터 예, 저자 미확인. (재인용: 2026-09-25-70)
- **f20**: BIM 이 현실을 정확히 나타낸다는 가정이 가구·설계–시공 편차로 성립하지 않음. (재인용: 2026-09-25-70)
- **f21**: GRADE 다섯 영역과 네 수준(f1), 소프트웨어 공학의 근거 강도 평가 적용(f2)을 가설 판정에 옮긴 이 위키의 종합이다. 가설 판정 규칙을 직접 정한 출처는 없다.
- **f22**: 판정 값 네 가지는 트랙 개요 3절 정의, 확실성 수준은 GRADE(f1), 실험실·관련 환경 구분은 TRL(f3·f4)에서 가져온 이 위키의 설계 제안.
- **f23**: f5~f10·f20 을 종합한 잠정 판정. 최종 판정은 검증 에이전트 몫이며 물류 도면에 대한 q5-01 지표 측정 전이다.
- **f24**: f11~f14 를 종합한 잠정 판정. 통행 가능 판정의 오판 측정(q5-05)과 능력 값 획득(q3-10)이 열려 있다.
- **f25**: f15~f19 를 종합한 잠정 판정. 벤더 수치(f17)는 판정 근거로 쓰지 않는다. 비교 실험(q5-12)·시뮬레이션 예측 비교(q5-06) 열림.
- **f26**: 관련 환경 시연(TRL 5·6, f3)과 비직접성 해소(f1) 논리로 도출한 실험 후보. 실험 계획 작성은 스토리텔러 몫이다.
- **f27**: 분류 원문 질문의 장소를 가설별 판정 항목으로 옮긴 이 위키의 예시. 실제 측정값 없음.
- **f28**: 검색 결과는 CAD→osmAG 연구(기존 ref-083 계열)·일반 물류 자동화 기사·벤더 소개뿐. 기존 근거 Beinschob 외는 설치 병목을 반자동화했으나 시간 비교 수치 미확인.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-807 | Cochrane | Chapter 14: Completing ‘Summary of findings’ tables and grading the certainty of the evidence | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-14 | 예 |
| ref-808 | Dybå, T., & Dingsøyr, T. (ESEM 2008) | Strength of evidence in systematic reviews in software engineering | 2008 | 논문 | medium | 2026-09-25 | https://dl.acm.org/doi/10.1145/1414004.1414034 | 예 |
| ref-809 | NASA ESTO | Definition Of Technology Readiness Levels | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://esto.nasa.gov/files/trl_definitions.pdf | 예 |
| ref-810 | 방위사업청(국가법령정보센터) | 기술성숙도평가(TRA) 업무지침 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://www.law.go.kr/LSW/admRulLsInfoP.do?admRulSeq=2000000018891 | 예 |
| ref-063 | Kalervo, A., Ylioinas, J., Häikiö, M., Karhu, A., & Kannala, J. | CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis | 2019-04 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/1904.01920 | 예 |
| ref-068 | Voxel51 (Hugging Face) | Voxel51/FloorPlanCAD · Datasets at Hugging Face | 미확인 | 오픈소스 문서 | low | 2026-09-25 | https://huggingface.co/datasets/Voxel51/FloorPlanCAD | 예 |
| ref-073 | Luo, R. 외 | ArchCAD-400K: A Large-Scale CAD drawings Dataset and New Baseline for Panoptic Symbol Spotting | 2025-03 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2503.22346 | 예 |
| ref-074 | 한국지능정보사회진흥원(AI Hub) | 건축 도면 데이터 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=71465 | 예 |
| ref-421 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcTransportElementTypeEnum (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Types/IfcTransportElementTypeEnum.md | 예 |
| ref-213 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcTransportElement (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcTransportElement.md | 예 |
| ref-214 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcOutletTypeEnum (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/domain/IfcElectricalDomain/Types/IfcOutletTypeEnum.md | 예 |
| ref-215 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcElectricApplianceTypeEnum (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/domain/IfcElectricalDomain/Types/IfcElectricApplianceTypeEnum.md | 예 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 예 |
| ref-081 | Vega-Torres, M. A. 외 | Occupancy Grid Map to Pose Graph-based Map: Robust BIM-based 2D-LiDAR Localization for Lifelong Indoor Navigation in Changing and Dynamic Environments | 2023-08 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2308.05443 | 예 |
| ref-229 | IDTA(Industrial Digital Twin Association) | IDTA 02020 Capability Description 1.0 — README (admin-shell-io/submodel-templates) | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description | 예 |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema | 예 |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml | 예 |
| ref-573 | buildingSMART International | Pset_DoorCommon - IFC 4.3.2 Documentation | 미확인 | 표준 | medium | 2026-09-25 | https://ifc43-docs.standards.buildingsmart.org/IFC/RELEASE/IFC4x3/HTML/lexical/Pset_DoorCommon.htm | 예 |
| ref-574 | buildingSMART International | Pset_StairCommon - IFC4.3.2.0 Documentation | 미확인 | 표준 | medium | 2026-09-25 | https://standards.buildingsmart.org/IFC/RELEASE/IFC4_3/HTML/lexical/Pset_StairCommon.htm | 예 |
| ref-283 | Open Robotics | Doors (integration_doors) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_doors.html | 예 |
| ref-794 | Opiela, M., & Hrehová, M. (Pavol Jozef Šafárik University, IPIN-WiP 2023, CEUR-WS Vol-3581) | Map Model Extraction from Image Floor Plans | 2023 | 논문 | medium | 2026-09-25 | https://ceur-ws.org/Vol-3581/194_WiP.pdf | 예 |
| ref-265 | European Commission (CORDIS) | PAN-ROBOTS: Automating logistics for the factory of the future | 미확인 | 기사 | low | 2026-09-25 | https://cordis.europa.eu/article/id/160857-panrobots-automating-logistics-for-the-factory-of-the-future | 예 |
| ref-271 | OTTO Motors (Rockwell Automation) | Maximize AMR productivity and simplify commissioning with our latest software release | 2023 | 벤더 문서 | low | 2026-09-25 | https://ottomotors.com/blog/amr-productivity-software-release/ | 예 |
| ref-441 | Open Robotics (open-rmf) | rmf_traffic_editor — README | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_traffic_editor | 예 |
| ref-406 | Open Robotics | Simulation - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/simulation.html | 예 |
| ref-632 | IFAC-PapersOnLine 게재 논문 저자(미확인) | Initialization of Simulation-Based Digital Twins for Internal Transport Systems | 2024 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/pii/S2405896324015374 | 예 |
| ref-217 | Beinschob, P., Meyer, M., Reinke, C., Digani, V., Secchi, C., & Sabattini, L. | Semi-automated map creation for fast deployment of AGV fleets in modern logistics | 2017 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0921889015302724 | 예 |

### 출처 요약

- **ref-807**: 원문 미열람. Cochrane 핸드북의 GRADE 확실성 평가 장. 다섯 영역으로 근거 확실성을 낮추고 네 수준으로 매긴다(검색 요약 기준).
- **ref-808**: 원문 미열람. 소프트웨어 공학 체계적 문헌고찰의 근거 강도 평가 체계(GRADE 2004 포함)를 개관한 ESEM 2008 논문.
- **ref-809**: 원문 미열람. NASA 기술 준비 수준 1~9 정의. TRL 5 관련 환경 검증, TRL 6 관련 종단간 환경 시연(검색 요약 기준).
- **ref-810**: 원문 미열람. 핵심기술요소의 기술성숙도(TRL)를 정량 평가하는 국내 행정규칙. TRL 6 이면 체계개발 진입 가능(검색 요약 기준, 판·조문 미확인).
- **ref-063**: 원문 미열람. 래스터 평면도 5,000장 주석 데이터셋과 다중 과제 모델.
- **ref-068**: 원문 미열람. FloorPlanCAD 의 제3자 데이터셋 카드(범주 목록 포함).
- **ref-073**: 원문 미열람. 벡터 CAD 조각 413,062개·27개 범주 데이터셋.
- **ref-074**: 원문 미열람. 평면도·입면도 등 건축 도면 객체·분할 데이터셋.
- **ref-421**: 원문 미열람. 운송 요소 유형 열거(ELEVATOR 등).
- **ref-213**: 원문 미열람. 엘리베이터 등 운송 요소 엔터티 정의.
- **ref-214**: 원문 미열람. 콘센트 유형 열거(충전 설비 값 없음).
- **ref-215**: 원문 미열람. 전기기기 유형 열거(충전 설비 값 없음).
- **ref-079**: 원문 미열람. 평면도 배경 위 주석으로 건물 지도·경유점 속성을 만드는 편집기 문서.
- **ref-081**: 원문 미열람. BIM 기반 격자 지도의 한계와 포즈 그래프 지도 변환.
- **ref-229**: 원문 미열람. 요구·제공 능력을 기술하는 AAS 서브모델 템플릿.
- **ref-228**: 원문 미열람. VDA 5050 팩트시트 JSON 스키마.
- **ref-105**: 원문 미열람. Open-RMF 플릿 어댑터 템플릿 설정 파일.
- **ref-573**: 원문 미열람. 문 공통 속성 세트.
- **ref-574**: 원문 미열람. 계단 공통 속성 세트.
- **ref-283**: 원문 미열람. Open-RMF 문 어댑터 연동 문서.
- **ref-794**: 원문 미열람. 평면도 이미지에서 지도 모델을 반자동 추출하는 진행 중 연구.
- **ref-265**: 원문 미열람. FP7 PAN-Robots 과제 소개 기사(설치 기간 단축 보고).
- **ref-271**: 원문 미열람. OTTO 소프트웨어 2.28 판 소개(벤더 주장).
- **ref-441**: 원문 미열람. traffic-editor 와 building_map_generator 저장소 README.
- **ref-406**: 원문 미열람. Open-RMF 시뮬레이션 월드·플러그인 문서.
- **ref-632**: 원문 미열람. 내부 운송 시스템 시뮬레이션 디지털 트윈의 실제 상태 초기화.
- **ref-217**: 원문 미열람. AGV 플릿 설치를 위한 반자동 지도·경로망 생성.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/tracks/floorplan-recognition/stage-5-verification-and-hypotheses.md | 2, 3, 4, 5, 6, 8, 9 | q5-03 답: f1·f2·f3·f4·f5·f6·f7·f8·f9·f10·f11·f12·f13·f14·f15·f16·f17·f18·f19·f20·f21·f22·f23·f24·f25·f26·f27·f28 (신뢰도 low) — 2절 q5-03 상태 답함, 3절 q5-03 소제목 신설({#q5-03}): 근거 평가 체계(GRADE f1, 소프트웨어 공학 근거 강도 f2), 기술 성숙도 보조 축(NASA TRL f3, 국내 TRA 업무지침 f4), 가설별 근거(가설 1 f5~f10·f20, 가설 2 f11~f14, 가설 3 f15~f19; f17 벤더 주장, f14·f20 연계 대상), 종합: 판정 절차(f21)·판정 값 규칙(f22, 표 권장)·잠정 판정(가설 1 부분 지지 f23, 가설 2 부분 지지 f24, 가설 3 미판정 f25, 표 권장)·필요 실험(f26)·‘3층 출하 대기장’ 시나리오(f27)·근거 공백(f28) / 4절 결론·불확실성 / 5절 후속 질문 / 6절 완료 조건 현황(가설 판정표 행) / 8절 출처 / 9절 이력 |
| update | docs/tracks/floorplan-recognition/index.md | 3 | 트랙 산출물(가설 판정표): 검증이 승인하면 3절 판정 칸에 가설 1 부분 지지(f23)·가설 2 부분 지지(f24)·가설 3 미판정(f25)과 근거 단계·실행 id 를 적고, 판정 규칙(f22) 한 단락을 둔다. 승인되지 않으면 미판정 유지. |
| update | docs/ideas/floorplan-recognition.md | 6 | 아이디어 페이지 6절(트랙 산출물): '가설 판정 절차' 소절 신설 — 근거 확실성 평가(f1·f2·f21), 판정 값 규칙과 TRL 보조 축(f3·f4·f22), 잠정 판정 요약(f23~f25), 필요 실험(f26). 모두 추정 중심 |
| update | docs/tracks/floorplan-recognition/experiments.md | — | 트랙 산출물(단계 5 stage_artifacts): 제안된 실험 계획 후보 E5-01 물류 도면 인식 지표 실험(가설 1), E5-02 능력 대조 판정 대 실제 주행 비교(가설 2, q5-05), E5-03 두 조건 모델링 시간 비교(가설 3, q5-12), E5-04 시뮬레이션 예측 대 현장 측정(가설 3, q5-06) — 근거 f26·f22 |
| update | docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md | 6 | 트랙 floorplan-recognition 단계 5 반영 제안 (f1, f2, f3, f4, f21, f22): 여러 출처의 근거를 GRADE 식 영역으로 확실성을 매기고 TRL 로 성숙도를 병기해 기술 가설을 판정하는 방법(추정) |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 기술 성숙도 | Technology Readiness Level (TRL) | 기술이 실제 적용에 얼마나 준비되었는지를 기초 원리 이해부터 실제 운용까지 1~9단계로 나타내는 지표로, 실험실 검증과 관련 환경 시연을 구분한다. |
| 근거 확실성 등급 | GRADE (Grading of Recommendations, Assessment, Development and Evaluation) | 근거 묶음의 확실성을 비뚤림 위험·비일관성·비직접성·비정밀성·출판 비뚤림으로 낮춰 높음·중간·낮음·매우 낮음으로 매기는 평가 체계다. |

## 열린 질문

새로 생긴 질문:

- 국내 로봇·물류 R&D 과제에서 도면 기반 지도 생성이나 로봇 관제 설정 자동화 기술의 성숙도를 기술성숙도(TRL) 기준으로 평가한 사례나 평가 기준이 있는가? | 관련 영역: 21. 온보딩·설정·현장 시운전, 23. 시험·형식 검증·벤치마크 | 근거: f4 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 27 · 교차 확인: 0
- 예산 사용량: 검색 8회 · 신규 출처 4건
- 미확인 항목:
    - 모든 finding 교차 확인 없음: 판정 방법 근거(f1~f4)는 체계마다 단일 출처, 가설 근거(f5~f20)는 이전 실행의 단일 출처 재인용
    - f1 GRADE 영역·수준, f2 Dybå·Dingsøyr 내용, f3 NASA TRL 정의, f4 방위사업청 업무지침 조문·판은 검색 요약 기준(원문 미열람)
    - f4 업무지침의 현행 판과 훈령 번호 미확인
    - f15 40분 대 5분 수치는 이전 검증 재검색에서도 재확인되지 않음
    - f16 PAN-Robots 비교 조건 미확인(q5-04 열림)
    - f21~f27 은 이 위키의 종합·잠정 판정이며 가설 판정 규칙을 직접 정한 출처는 없음
    - 물류센터 조건의 직접 근거(인식 성능·시간 단축·시뮬레이션 예측 정확도)는 검색 범위에서 찾지 못함
- 범위 경계 위반 의심:
    - f14: 문 여닫기 실행은 분류 원문 9장 '시설·설비 제어' 연계 영역이라 '연계 대상: '으로 표시하고 대조 규칙의 선택 조건 근거로만 씀
    - f20: BIM 격자 지도 위 위치추정은 '로봇 자체 지능·제어' 연계 영역이라 '연계 대상: '으로 표시하고 가설 1·3 의 반대 방향 근거로만 씀
    - f17: 벤더 주장은 판정 근거로 쓰지 않는 사례로만 제시
- 한계: web_fetch_available: false · fetch_mode mirror_only. 이번 신규 출처(ref-807~ref-810)는 GitHub 공식 저장소 원문이 없어 모두 원문 미열람이며, 재사용 출처도 이번 실행에서 다시 열지 않아 모든 출처·finding 에 source_unopened 표시, 신뢰도 상한 medium(종합은 low). 검색 8회/40(한국어 2회), 신규 출처 4건/20(ref-807~ref-810, 예약 구간 안), 재사용 23건. 질문 선택: target.json 지정 q5-03 1건. q5-03 은 판정 절차·규칙(f21·f22)과 가설별 근거 정리(f5~f20)로 답했으나 판정 규칙과 잠정 판정(f23~f25)은 이 위키의 종합이라 질문 종합 신뢰도 low. 잠정 판정은 제안이며 트랙 개요 3절 반영은 검증 승인 뒤. 한국 자료: 방위사업청 기술성숙도평가 업무지침(ref-810) 1건, 국내 물류 사례는 찾지 못함(일반 열린 질문 1건). 교차 규칙: 도면 해석 모델 평가는 이전 실행에서 27. AI·학습·적응과 모델 운영과 6. 지도·공간·위치 모델 양쪽에 제안됨, 이번에는 AI 방법 자체에 관한 새 finding 없음. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈: f19 는 운영 예측 시뮬레이션(22)의 초기값을 현재 상태(8)에서 받는다는 기존 구분을 따름. 정정 요청 없음. 온톨로지 변경 없음: 가설 판정은 공간 그래프 스키마의 개념·관계가 아니라 검증 방법이다. 후속 질문 2건. 페이지 제안: 트랙 산출물 4건(단계 페이지·트랙 개요 3절·아이디어 6절·실험), 세부영역 반영 제안 1건(갱신 상한과 별도).

## 트랙 블록

- 트랙: floorplan-recognition · 단계: 5
- 답한 질문 id: q5-03

### 새 질문

| 제안 id | 질문 | 보낼 단계 | 근거 finding |
|---|---|---|---|
| — | 가설 판정 규칙에서 '물류 조건의 직접 근거'로 인정할 사용자 실험의 최소 규모(도면 수·층 수·제조사 수)와, 주거·사무 건물 대상 공개 연구 결과를 비직접 근거로 한 단계 낮춰 반영하는 기준은 무엇인가? (q5-03 에서 파생) | 5 | f22 |
| — | 새 근거(사용자 실험, 새 연구)가 들어올 때 가설 판정표를 다시 여는 조건과 판정 이력(이전 판정·근거·확실성 수준·판정 실행 id)을 남기는 형식은 무엇인가? (q5-03 에서 파생) | 5 | f21 |

### 온톨로지 초안 변경 제안

- 없음

### 단계 완료 조건 자체 평가

- 충족 여부(자체 평가): 미충족
- 못 채운 조건:
    - 가설 판정표(q5-03 답 f22~f25)는 검증 승인 전이며 트랙 개요 3절에 아직 반영되지 않음
    - 사용자에게 제안하는 실험 계획이 실험 페이지에 아직 없음(f26 후보만 제안)
    - 평가 지표·검증 절차 소절이 검증 승인 전 미충족 상태로 남음
    - 열린 질문 q5-04~q5-10, q5-12, q5-13
