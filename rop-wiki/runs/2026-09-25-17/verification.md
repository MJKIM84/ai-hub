# 1차 검증(브리프) 2026-09-25-17

**판정: 조건부 승인** · 신뢰도: medium

## 주장별 검증

| finding | 출처 실재 | 주장 뒷받침 | 교차 확인 | 태그 처분 | 메모 |
|---|---|---|---|---|---|
| f1 | 예 | 예 | 아니오 | 유지 | 원문 확인(ref-031 원문 텍스트, main state.schema github_raw 열람). 정정 조건부 유지: 3.0.0 main 상태 스키마에는 positionInitialized 가 없고 필수 불리언 localized 가 있다(2.x 의 positionInitialized 가 3.0 에서 localized 로 바뀜, 검색 결과로도 확인). localizationScore 는 '위치추정 품질' 0.0~1.0, deviationRange 는 미터 단위 위치 편차 범위이며 둘 다 선택 필드다. mapId·x·y·theta 는 필수. 필드명 정정과 ref-051 추가 각주를 조건으로 사실 유지. 단일 발행 주체. |
| f2 | 예 | 예 | 아니오 | 유지 | 확인: ref-031 원문 6.3.2(maps 배열 필수 mapId·mapVersion·mapStatus), 표 4·5(downloadMap·enableMap·deleteMap, enableMap 은 같은 mapId 의 다른 판을 DISABLED). main state.schema 도 같은 필수 필드와 'mapId 당 ENABLED 하나'를 둔다. 발행일은 oq-005 대로 미확정. |
| f3 | 예 | 예 | 아니오 | 유지 | 확인: ref-031 원문 6.4.1·6.4.2(윤곽 기반·운동 중심 기반 구역 유형, 'Only a single zone set can be active at once for each mapId', 구역 집합은 mapVersion 을 참조하지 않음). |
| f4 | 예 | 예 | 아니오 | 유지 | 확인: MassRobotics 공식 저장소 AMR_Interop_Standard.json 을 github_raw 로 열어 location(x·y·z·쿼터니언 angle·planarDatum UUID), planarDatum 원점 정의 메시지 없음, 신뢰도 필드 없음을 확인했다. 다만 브리프는 근거 출처를 ref-033(발표 페이지, fetched false 인데 fetch_url 이 스키마를 가리킴)으로 적었다 — 이미 등록된 ref-230(같은 JSON 스키마)으로 바꿔야 한다. 부재는 스키마 파일 기준이며 확정은 아님. |
| f5 | 예 | 예 | 아니오 | 유지 | 확인: location_2D.json 필수 map·x·y·yaw, robot_state.json 은 location 을 이 스키마로 참조하고 불확실성 필드 없음(둘 다 github_raw 열람). 같은 저장소라 독립 교차 아님. |
| f6 | 예 | 예 | 아니오 | 유지 | 확인: traffic-editor mdBook 원본 열람(배경 이미지 캔버스, 기본 축척 1px=5cm와 측정 거리 보정, 기준점 2쌍 이상으로 이동·회전·축척 변환, 로봇 지도 레이어의 축척·이동·회전). 단 브리프의 새 id ref-079 는 이미 다른 출처(Meseguer Valenzuela 외 작업 배정 리뷰)에 쓰인 id 이고, 같은 URL 이 ref-079 로 이미 등록돼 있다 — ref-079 로 재사용해야 한다. |
| f7 | 예 | 예 | 아니오 | 유지 | 확인: 같은 원본에서 정점 속성 is_charger·is_parking_spot·is_holding_point, 문 유형 네 가지, .building.yaml 저장, GUI 결과로 시뮬레이션 월드 자동 생성 확인. 출처 id 는 ref-079 로 재사용. |
| f8 | 예 | 예 | 아니오 | 유지 | 확인: integration_nav-maps 원본 열람(층 이름 B1·L1, 미터 단위 (x, y), 충전기·주차·비상 대피 지점 플래그, 간선 일방·양방향과 속도 제한, YAML·XML·텍스트·DXF·DWG·SVG 순서, 스크린샷 'sanity-checking'). 새 id ref-080 대신 이미 등록된 ref-080(같은 URL)을 재사용해야 한다. |
| f9 | 예 | 예 | 아니오 | 유지 | 확인: 어댑터 튜토리얼 원본(reference_coordinates, nudged.estimate 와 estimate_error(MSE), 층별 변환, 'A minimum of 4 matching waypoints is recommended')과 템플릿 config.yaml(L1 좌표 4쌍) 열람. 두 출처 모두 open-rmf 라 독립 교차 아님. |
| f10 | 예 | 예 | 아니오 | 유지 | 확인: REP 105 저장소 원본 열람(map 은 불연속·이산 점프·장기 전역 기준, odom 은 한없이 드리프트, 여러 지도에서 earth 좌표계를 공통 기준으로). |
| f11 | 예 | 예 | 아니오 | 유지 | 확인: LIF README 열람(1.0.0, 2023-09, VDMA 발행, 간선·노드·스테이션 교환 형식, VDA5050 영향). 최신성 주의: ref-031(VDA 5050 3.0.0) 원문 5.2 절은 LIF 를 'VDMA 2024-03' 판으로 인용하고 경로 가져오기에 쓸 수 있다고 적는다 — README 의 1.0.0(2023-09)보다 새 판이 있을 수 있으므로 기준일·판을 명시해야 한다. 저장소가 VDMA 공식 계정인지는 미확인. |
| f12 | 예 | 예 | 아니오 | 유지 | 원문 미열람(검색 결과 일치). ISO 페이지 제목·범위 문구 일치. 검색 결과에 ISO/FDIS 21423(2026-05) 단계가 나타나 최종 발행은 확인되지 않았다 — '발행 여부 미확인'을 유지하고 FDIS 단계를 기준일과 함께 적을 수 있다. 신뢰도 medium 상한. |
| f13 | 예 | 아니오 | 아니오 | 유지 | 원문 미열람. 이번 검증 검색에서는 공통 좌표계(CCS) 안에서 위치를 공유한다는 요약만 나타났고 '기준점 3개 이상' 문구는 확인되지 않았다(리서치 검색 요약에만 있고 출처가 ISO 원문인지 해설인지 불명). 이미 [추정]이고 low 이므로 추정 유지하되 '초안 해설 요약 기준, 기준점 개수는 미확인'을 병기하고 열린 질문 1번과 연결한다. |
| f14 | 예 | 예 | 아니오 | 유지 | 확인: IfcSpace.md(개발 브랜치) github_raw 열람(정의, IfcRelAggregates 로 층에 연결, ElevationWithFlooring). 게시판 IFC 4.3 ADD2 와 문구 차이 가능 표시 유지. |
| f15 | 예 | 예 | 아니오 | 유지 | 확인: SWG README(Part 1 공개, Part 2 인코딩 작업 중 — XML 26-042·JSON 26-043·SQL 26-044 초안)와 26-042('Candidate SWG Draft', GML 3.2.1, CellSpace·CellBoundary·Node·Edge·ThematicLayer·InterLayerConnection) 열람. |
| f16 | 예 | 예 | 아니오 | 유지 | 원문 미열람(검색 결과 일치). ISO 페이지 요약에 의미 분류 체계와 '기하·위상 기술은 다루지 않음'이 나타나고 발행은 2024-08. IndoorGML 구현 관계는 요약 기준이라 문장을 '소개된다'로 유지해야 한다. |
| f17 | 예 | 예 | 아니오 | 유지 | 원문 미열람(검색 결과 일치). GS1 페이지·GLN 할당 규칙·확장 요소 페이지 스니펫에 하위 위치 GLN 부여와 확장 요소의 '내부 또는 당사자 간 합의로만 사용' 규정이 나타난다. |
| f18 | 예 | 예 | 아니오 | 유지 | 추론(추정) 유지. 근거 finding 들이 살아남았다. f1 필드명 정정과 f4·f6·f8 출처 id 재매핑을 반영해야 하며, f13 은 초안 해설 기준임을 문장에 남긴다. |
| f19 | 예 | 예 | 아니오 | 유지 | 원문 미열람(검색 결과 일치: 동적 점 제거·다세션 정합·변화 탐지·기준 지도와 변화분 기반 지도 버전 관리). 최신성: IEEE 저널 게재본(IEEE Xplore 문서 10566021)이 있어 기준일을 arXiv 2025-01 과 게재본으로 함께 적어야 한다. |
| f20 | 예 | 예 | 아니오 | 유지 | 추론(추정) 유지. 근거 f2·f9·f19 확인됨. 제조사 간 지도 판 동기화 자료 부재는 확정 아님. |
| f21 | 예 | 예 | 아니오 | 유지 | 원문 미열람(검색 결과 일치: SAGE·연구자 PDF·ResearchGate). 항공 무결성 위험 지표, EKF SLAM, 데이터 연관 오류가 이 지표로만 예측되는 큰 성능 저하, IJRR 44(6) 972-988, 2025-05 온라인 일치. |
| f22 | 예 | 예 | 아니오 | 유지 | 추론(추정) 유지. 대조 결과(VDA 5050 은 localizationScore·deviationRange 선택 필드와 localized 필수 플래그, MassRobotics 스키마·Open-RMF 로봇 상태에는 신뢰도 필드 없음)를 이번 검증 열람으로 확인했다. VDA 5050 의 두 필드가 선택 필드라는 점을 문장에 반영해야 한다. |
| f23 | 예 | 예 | 아니오 | 유지 | 원문 미열람. 이번 검증에서 재검색하지 않았다(재인용: 2026-09-25-11). 같은 arXiv 2408.01737 이 이미 ref-224(Shaheer, M. 외, 저자 확인됨)로 등록돼 있으므로 새 id ref-224(저자 미확인) 대신 ref-224 를 재사용해야 한다. 35cm·15도는 단일 출처 실험 조건 수치. |
| f24 | 예 | 예 | 아니오 | 유지 | 원문 미열람(KCI 검색 결과 일치: 저자 4인, 로봇학회 논문지 21(1) 48-57, 3D 라이다–IMU SLAM 경계 탐사, RGB-D 카메라와 4자유도 팔로 승강기 버튼). 승강기 버튼 조작은 로봇 자체 제어이므로 다층 지도 구축 사례로만 쓴다. |
| f25 | 예 | 예 | 아니오 | 유지 | 기등록 출처 ref-064·ref-078 의 제목 수준 재인용(재인용: 2026-09-25-05). 이번 검증에서 원문 재확인 안 함, 원문 미열람. medium 상한. |
| f26 | 예 | 예 | 아니오 | 유지 | 기등록 출처 ref-065·ref-070 README 제목 수준 재인용. 이번 검증에서 재확인 안 함, 원문 미열람. |
| f27 | 예 | 예 | 아니오 | 유지 | 기등록 출처 ref-067·ref-073 제목 수준 재인용. 두 출처는 발행 주체가 다르지만 이번 검증에서 두 원문을 확인하지 않았으므로 cross_checked 는 false 로 둔다(브리프의 true 를 내림). 태그 사실은 각 데이터셋 존재와 과제명 수준이라 유지. |
| f28 | 예 | 예 | 아니오 | 유지 | 기등록 출처 ref-063·ref-069·ref-071·ref-074 제목 수준 재인용. 원문 미열람. 창고 평면도 데이터셋 부재는 이 목록 기준일 뿐 확정 아님. |
| f29 | 예 | 예 | 아니오 | 유지 | 추정 유지. 라이선스 값은 이전 실행 보고의 재인용이며 이번에 원문으로 재확인하지 않았다 — 본문에서 '이전 실행 보고 기준'을 밝혀야 한다. |
| f30 | 예 | 예 | 아니오 | 유지 | 원문 미열람(검색 결과 일치: GPT-4o, 9단계 과업에서 성공률 0.96, 라벨 밀도가 높을수록 성능 향상, 지도가 크면 저하). 최신성: ELSPublishing 저널 게재본(doi 10.55092/rl20250011, 2025)이 있어 기준일에 함께 적을 수 있다. 단일 출처 수치. |
| f31 | 예 | 예 | 아니오 | 유지 | 추론(추정) 유지. 근거 f6·f7·f8(열람 확인)과 f23. 출처 id 는 ref-079·ref-080·ref-224 로 재매핑. |
| f32 | 예 | 예 | 아니오 | 유지 | 추론(추정) 유지. '연계 대상:' 표시가 있고 분류 원문 9장 '로봇 자체 지능·제어' 경계와 맞는다. ROP 직접 범위는 [추정]의 경계 제안으로만 쓴다. |

## 항목별 결과

| 항목 | 결과 | 내용 |
|---|---|---|
| 분류 적합성 | 예 | — |
| 범위 경계 | 예 | — |
| 중복·모순 | 아니오 | 브리프의 새 id ref-079(traffic-editor)는 참고문헌 목록에서 이미 다른 출처(Meseguer Valenzuela·Blanes Noguera, Task Allocation in Mobile Robot Fleets)의 id 이며, traffic-editor 는 같은 URL 로 ref-079 에 이미 등록돼 있다, 브리프의 새 id ref-080(integration_nav-maps)은 같은 URL 의 기존 ref-080 과 중복, 브리프의 새 id ref-224(arXiv 2408.01737, 저자 미확인)은 같은 URL 의 기존 ref-224(Shaheer, M. 외)와 중복, f4 의 근거 ref-033(MassRobotics 발표 페이지)은 실제로 열어 본 JSON 스키마가 아니며, 같은 스키마가 ref-230 으로 이미 등록돼 있다, 브리프 limits 의 '이전 실행 2026-09-25-11 이 제안한 ref-079~ref-095 는 목록의 해당 id 가 다른 출처'라는 판단은 ref-079·ref-080 에 대해서는 틀렸다(두 id 는 traffic-editor·integration_nav-maps 그대로다), 기존 열린 질문 oq-022(국내 물류센터의 CAD·BIM 도면 활용과 도면–현장 차이 확인)가 이 영역에 걸려 있으나 브리프 11절 계획에 연결이 없다, 용어 후보 IndoorGML·산업 기초 클래스(IFC)는 용어집에 이미 있다 |
| 용어 일관성 | 아니오 | 용어 후보 'IndoorGML' 은 용어집 기존 항목(indoorgml.md)과 같은 용어다 — 신규 등록이 아니라 f15 근거의 정의 갱신(action: update) 대상이다(기존 정의는 ifc2indoorgml 도구 대상이라는 부수 설명뿐이다), 용어 후보 '산업 기초 클래스(IFC)' 는 용어집 기존 항목(ifc.md)과 같은 용어다 — 신규 등록하지 않고 필요하면 f14 근거로 update 한다, VDA 5050 3.0.0 은 로봇 위치 블록을 mobileRobotPosition, 위치추정 여부를 localized 로 부른다 — f1 의 positionInitialized 는 2.x 명칭이므로 쓰지 않는다 |
| 인용 길이·저작권 | 예 | — |
| 정정 요청 반영 | — | — |

## 수정 지시(required_fixes)

- f1: 'positionInitialized(위치추정 초기화 여부)'를 VDA 5050 3.0.0 명칭 'localized(필수, 위치를 신뢰할 수 있는지)'로 고치고, localizationScore(위치추정 품질 0~1)·deviationRange(미터 단위 위치 편차 범위)가 선택 필드임을 적으며, 각주에 ref-051(main state.schema)을 더한다 — main 상태 스키마에 positionInitialized 가 없고 3.0 에서 localized 로 바뀌었다.
- f22: 'VDA 5050 만 0~1 점수와 정확도 범위로 보고'를 '선택 필드로 보고할 수 있게 한다'로 고친다 — 두 필드는 main 상태 스키마에서 선택 필드다.
- 출처 id 재매핑: f6·f7·f18·f31 의 ref-079 는 기존 ref-079 로, f8·f18·f31 의 ref-080 은 기존 ref-080 으로, f23·f31 의 ref-224 은 기존 ref-224(Shaheer, M. 외)로 바꾸고, reference_updates 에 ref-079·ref-080·ref-224 을 새로 등록하지 않는다 — 같은 URL 이 이미 등록돼 있고 ref-079 는 다른 출처(Meseguer Valenzuela 외)의 id 다.
- f4·f18·f22: 근거 출처 ref-033 을 ref-230(MassRobotics AMR_Interop_Standard.json)으로 바꾸고 이번 실행 reference_updates 에 ref-033 을 넣지 않는다 — 실제로 연 문서는 발표 페이지가 아니라 JSON 스키마이고 ref-230 으로 이미 등록돼 있다.
- f11: LIF 를 'README 기준 1.0.0(2023-09)'으로 판·기준일을 밝혀 적는다 — VDA 5050 3.0.0 원문(ref-031)이 LIF 를 'VDMA 2024-03' 판으로 인용해 더 새 판이 있을 수 있다.
- f12: '발행 여부 미확인'을 유지하고 기준일 2026-09-25 에 검색 결과상 FDIS 단계였음을 적을 수 있다. f13 은 [추정]을 유지하고 '초안 해설 요약 기준이며 기준점 개수는 미확인'을 병기해 열린 질문(ISO 21423 공통 좌표계)과 연결한다 — 검증 검색에서 '기준점 3개 이상' 문구를 확인하지 못했다.
- f19·f30: 기준일에 게재본을 함께 적는다(f19 는 IEEE 저널 게재본, f30 은 2025 저널 게재본) — 브리프의 arXiv 판만으로는 최신판이 드러나지 않는다.
- f25~f30 과 f23: 본문에서 '이전 실행 보고 기준, 원문 미열람'임이 드러나게 하고 태그를 올리지 않는다. f27 의 교차 확인 표시는 쓰지 않는다 — 검증에서 두 원문을 확인하지 못했다.
- 원문 미열람 표기: ref-063·ref-064·ref-065·ref-066·ref-067·ref-069·ref-070·ref-071·ref-073·ref-074·ref-076·ref-078·ref-159·ref-161·ref-162·ref-163·ref-164·ref-165·ref-224 의 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 해당 항목에 source_unopened: true 를 넣는다 — web_fetch_available: false 이며 이 출처들은 원문을 열지 않았다.
- 용어집: IndoorGML·산업 기초 클래스(IFC)는 신규 등록하지 않고, 갱신한다면 action update 로 f15·f14 근거 정의를 쓴다. 레이아웃 교환 형식(LIF)·지도 정합은 신규 등록할 수 있다.
- 11절: 기존 열린 질문 oq-022(국내 물류센터 CAD·BIM 도면 활용과 도면–현장 차이 확인)를 연결하고, open_questions_new 3건은 형식 그대로 등록한다.
- 트랙 반영 제안 처리: 2026-09-25-11 제안 4건 가운데 traffic-editor·관제 연동 층 이름·미터 좌표 요건(f6~f8)과 9절 경계(f32)만 반영하고, osmAG·osmAG-from-cad·ifc2indoorgml·Ogm2Pgbm·Boniardi 외·Vega-Torres 외·BIRS·Palacz 외·국내 BIM–건설로봇 문헌고찰은 이번 브리프에 finding 이 없으므로 본문에 넣지 않는다 — 넣으면 드리프트다. 2026-09-25-05 제안의 '축척 복원은 별도 과제'와 엘리베이터 라벨 문장도 넣지 않는다.
- 10절: 22. 시뮬레이션·예측용 디지털 트윈 연결은 traffic-editor 가 시뮬레이션 월드를 생성한다는 사실(f7)로만 쓰고, 8. 실시간 세계 상태·데이터 일관성 연결은 현재 위치 보고(f1·f5·f22)로만 쓴다 — 두 영역의 원문 구분을 지킨다. 27. AI·학습·적응과 모델 운영 연결(f25~f30)은 양쪽 페이지 연결로 둔다.
- 9절: f10·f19·f21·f23·f24 의 SLAM·위치추정·지도 작성 기술은 '연계 대상'으로 짧게 두고 ROP 가 맡는 것처럼 쓰지 않는다. ROP 쪽 경계(f32)는 [추정]으로 둔다.

## 검증 노트

판정: 조건부 승인. 이번 실행은 원문 열람이 차단된 환경에서 검증됐다(raw.githubusercontent.com 공식 저장소만 열림). 확인 32건, 미확인 0건, 교차 확인 0건. 강등: 없음(f13 은 기존 [추정] 유지, f1 은 3.0.0 필드명 positionInitialized → localized 정정 조건부 유지). 원문 미열람 출처: ref-063, ref-064, ref-065, ref-066, ref-067, ref-069, ref-070, ref-071, ref-073, ref-074, ref-076, ref-078, ref-159, ref-161, ref-162, ref-163, ref-164, ref-165, ref-224(브리프 ref-224). 검증자가 GitHub 원문으로 다시 연 출처: ref-031 원문 텍스트, ref-051 상태 스키마, ref-230 MassRobotics 스키마, ref-148·ref-155 Open-RMF 스키마, ref-079 traffic-editor, ref-080 경로 지도 요건, ref-154 어댑터 튜토리얼, ref-105 설정, ref-156 REP 105, ref-157 IfcSpace, ref-158 IndoorGML SWG, ref-160 LIF. 출처 id 정리: ref-079·ref-080·ref-224 은 기존 ref-079·ref-080·ref-224 와 같은 출처라 재사용하고, f4 의 근거는 ref-033 대신 ref-230 이다. 주의: 규격 필드 비교는 발행 주체 한 곳의 원문 기준이며 제조사 지도와 업무 장소를 잇는 대응 규칙(f18), 지도 판 동기화(f20), 신뢰도 수용 기준(f22), ROP 경계(f32)는 이 위키의 추론이다. ISO 21423 은 최종 발행이 확인되지 않았고(검색상 FDIS 단계) 공통 좌표계의 기준점 개수는 미확인이다. LIF 는 README 판(1.0.0, 2023-09)보다 새 판(VDMA 2024-03)이 VDA 5050 3.0.0 에 인용돼 있다. 평면도 인식 자료(f25~f30)는 이전 트랙 실행의 재인용이다. 2026-09-25-11 트랙 반영 제안 가운데 osmAG·BIM 기반 지도 생성·도면 기반 위치추정 연구는 이번 브리프에 근거가 없어 반영하지 않았다. 검증 검색 10회(리서치 16회와 합쳐 26/30).
