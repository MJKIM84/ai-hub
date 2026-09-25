# 1차 검증(브리프) 2026-09-25-52

**판정: 조건부 승인** · 신뢰도: medium

## 주장별 검증

| finding | 출처 실재 | 주장 뒷받침 | 교차 확인 | 태그 처분 | 메모 |
|---|---|---|---|---|---|
| f1 | 예 | 예 | 아니오 | 유지 | 확인: 입력 원문 ref-031 표 2(4.3절 토픽 표)에 factsheet 토픽 설명 'Parameters or vendor-specific information to assist set-up of the mobile robot in fleet control', 표 4에 factsheetRequest 즉시 동작이 있다. evidence_excerpt 가 인용 위치를 '6.10절'로 적었지만 입력 원문에서 확인한 위치는 표 2다(6.10절 본문은 발췌 범위 밖). ref-228 는 같은 저장소라 독립 출처가 아니다. |
| f2 | 예 | 아니오 | 아니오 | 강등 | 사실 → 추정: 검증자가 raw factsheet.schema 를 직접 열어 확인했다. 최상위 required 배열은 headerId·timestamp·version·manufacturer·serialNumber 와 내용 절 여섯 개(typeSpecification, physicalParameters, protocolLimits, protocolFeatures, mobileRobotGeometry, loadSpecification)다. mobileRobotConfiguration 은 필수가 아니다(선택 절이며 버전과 충전 파라미터를 담는다). 그래서 '일곱 절 필수'는 원문과 다르다. 스키마 설명문(로봇 유형 비교, 계획·규모 산정·시뮬레이션, VDA 5050 준수 관제로의 통합에 필요한 통신 인터페이스 정보)은 원문과 맞는다. |
| f3 | 예 | 예 | 아니오 | 유지 | 확인: 입력 원문 ref-031 표 4(downloadMap: mapId·mapVersion·mapDownloadLink·선택 mapHash, enableMap, deleteMap)와 6.3.1절(관제가 즉시 동작으로 지도 서버에서 끌어오는 pull 방식 다운로드를 지시, 내려받기와 활성화는 별도 과정)에 있다. |
| f4 | 예 | 예 | 아니오 | 유지 | 확인: 입력 원문 ref-031 5.2절(경로 정의·경로망 구성·로봇 구성, 'not part of this document', LIF – VDMA 2024-03). 2절 범위 제외 항목에도 commissioning workflows 가 있다. LIF 기준일이 ref-046(1.0.0, 2023-09)과 다르다(f5 비고). |
| f5 | 예 | 예 | 아니오 | 유지 | 확인: 검증자가 raw README 를 열었다. 1.0.0(2023-09), 통합사업자가 제3자 중앙 관제에 주행 레이아웃을 처음 넘기는 형식, edges·nodes·stations, 'non-binding approach'. VDA 5050 3.0.0 명세(ref-031)는 LIF 를 'VDMA 2024-03'으로 인용하므로 기준일 표기가 두 출처에서 다르다. |
| f6 | 예 | 예 | 아니오 | 유지 | 확인: 검증자가 raw AMR_Interop_Standard.json 을 열었다. identityReport 필수 6개가 일치한다. 선택 필드는 브리프 목록 외에 emergencyContactInformation·supportVendorContactInformation·thumbnailImage 도 있다(브리프 목록은 일부 나열이다). |
| f7 | 예 | 예 | 아니오 | 유지 | 확인: 검증자가 raw integration_fleets_adapter_tutorial.md 를 열었다. limits·profile·battery_system·mechanical_system·reversible·task_capabilities(loop·delivery·clean)·finishing_request·reference_coordinates(대응 웨이포인트 최소 4개 권장)·fleet_manager(prefix·인증), 제공 필드 밖을 쓰면 가져오기 오류라는 경고가 있다. |
| f8 | 예 | 예 | 아니오 | 유지 | 확인: 검증자가 raw traffic-editor.md 를 열었다. 평면도 배경, 두 점 측정선으로 축척, 정점(충전기 등 속성)·벽·문·승강기·차선 주석, 수직 정렬 기준점(fiducial)으로 층간 변환, 'standardized, vendor neutral manner through a graphical interface'. 기본 축척 1픽셀=5cm 는 검증자 열람 응답에서 확인하지 못했다(주장 본문에는 없다). |
| f9 | 예 | 예 | 아니오 | 유지 | 확인: 검증자가 raw rmf_site README 를 열었다. 'experimental approach to visualizing and editing large RMF deployment sites', rmf_site_cmake 로 시뮬레이션·주행 그래프 생성, Rust·Bevy 기반 웹·데스크톱. |
| f10 | 예 | 예 | 아니오 | 유지 | 조건부 유지: 검증자가 raw integration_fleets.md(ref-251)를 열었다. 여기에는 Full Control(경로 지정·언제든 교체)과 Traffic Light(일시정지·재개만)만 있고 'Read Only' 문구는 없다. Read Only(제어권 없이 상태만 보고)는 raw rmf-core.md(ref-004)에서 확인했다. 두 문서는 같은 책이라 독립 출처가 아니다. 마지막 절 '온보딩 때 연동 수준이 선택 사항'은 출처 문장이 아니라 추론이다. 브리프 표시는 ref-251 fetched false 그대로이며 원문 미열람이다(검증자 열람으로 실재 확인). |
| f11 | 예 | 예 | 아니오 | 유지 | 확인(원문 미열람, 검색 결과 일치): ScienceDirect·ResearchGate·Scilit 검색 결과에서 Beinschob·Meyer·Reinke·Digani·Secchi·Sabattini, RAS 87권 281–295쪽(2017), 정밀 2D 지도·픽업·하역 3D 지리 참조·수작업 경로망 병목, 레이저 스캐너 3D 의미 지도, 경로망 자동 설계, PAN-Robots(FP7)가 일치한다. |
| f12 | 예 | 예 | 아니오 | 유지 | 확인(원문 미열람, 검색 결과 일치): CORDIS 기사 제목·URL 이 일치하고, '6개월 대신 2개월' 설치는 검색 요약에 나온다. '기존 표지 활용 위치추정·반자동 공장 탐사 덕분'이라는 원인 서술은 검증자 검색 요약에서 확인하지 못했다. 과제 측 보고값이므로 [추정] 유지가 맞다. 발행일 미확인. |
| f13 | 예 | 예 | 아니오 | 유지 | 확인(원문 미열람, 검색 결과 일치): arXiv 2404.13499, Heselden·Das, 지도 작성은 새 환경 배치의 시간 소모 과정, 전역 위치·물체 위치·위상·점유 중심 표준 처리, 템플릿·절차적 생성, ICRA 2024 Field Robotics 워크숍. |
| f14 | 예 | 예 | 아니오 | 유지 | 조건부 유지(원문 미열람, 검색 결과 일치): KCI 서지(노주형·강규리·김연찬·심현철, 한국로봇학회 논문지 21권 1호 48–57쪽, 2026)가 일치한다. 검색 요약에서 3D LiDAR–IMU SLAM, 다중 센서 융합 비용 지도, RGB-D·4자유도 매니퓰레이터 버튼 조작, 처음부터 끝까지 완전 자율 다층 지도 구축을 확인했다. '사물인터넷 장치 개조나 외부 시스템 연동 없이'는 검증자 검색 요약에 나타나지 않았다. 로봇 자체 기능 연구이므로 범위상 8절 사례로만 둔다. |
| f15 | 예 | 예 | 아니오 | 유지 | 확인: 검증자가 raw Capability Description 1/0 README 를 열었다. 'enables reliable comparison between required and provided capabilities and supports efficient planning and orchestration of production processes', 버전 1.0 은 IDTA 첫 공식 발행판이다. 브리프는 fetch_url 을 적었지만 fetched false·source_unopened true 로 표시했다(과소 표시라 수정 지시 대상 아님). |
| f16 | 예 | 예 | 아니오 | 유지 | 확인(원문 미열람, 검색 결과 일치): arXiv 2307.00827, Vieira da Silva·Köcher·Gill·Weiss·Fay(HSU), ETFA 2023(IEEE Xplore 10275459). plug and produce 원칙, 온톨로지 방식과 AAS 서브모델 방식이 서로 호환되지 않음, 양방향 대응 개념. |
| f17 | 예 | 예 | 아니오 | 유지 | 확인(원문 미열람, 검색 결과 일치): arXiv 2406.07962, Vieira da Silva·Köcher·Gehlhoff·Fay. 자연어 설명 → few-shot 프롬프트 → LLM 이 능력 온톨로지 생성 → 구문·모순·환각·누락 검사 루프. 2024-10-18 개정. 교차 규칙상 27. AI·학습·적응과 모델 운영 연결이 필요하다. |
| f18 | 예 | 예 | 아니오 | 유지 | 확인(원문 미열람, 검색 결과 일치): ISO 3691-4:2023 소개 페이지(iso.org/standard/83545). 무인 산업용 트럭과 시스템의 안전 요구·검증 수단, 운행 구역 상태가 안전 운행에 큰 영향을 주고 구역 준비는 부속서 A 에 규정. 연계 대상 표시가 적절하다(25. 안전·위험 관리). |
| f19 | 예 | 예 | 아니오 | 유지 | 확인(원문 미열람, 검색 결과 일치): 부산일보 기사와 URL 이 일치하고 헬로티·데일리안·경남일보·네이트 뉴스도 같은 내용(2026-07-23 MOU, KILA 168개 회원사, AMR·AGV·팔레타이징 로봇·모바일 매니퓰레이터·자율주행 지게차, KTL 테스트베드–회원사 물류센터 연계, 단체표준 개발)을 보도한다. 다만 모두 같은 기관 발표에서 나온 보도라 독립 교차 확인으로 보지 않는다. 협약 단계이며 실적은 미확인이다. |
| f20 | 예 | 예 | 아니오 | 유지 | 확인(원문 미열람, 검색 결과 일치), 벤더 주장 [추정] 유지. 제목 'reduces launch time by three weeks'가 일치한다. 검색 요약상 내용은 IDC 가 Tecnomatix Plant Simulation 으로 고속 분류기(sortation)를 가상 시운전해, 현장 시운전만 한 유사 업그레이드 프로젝트(8주)보다 시운전 기간을 3주 줄였다는 것이다(파트너 Simsol). 브리프의 '비교 기준 미확인'은 검색 요약과 다르고, '코드를 설계와 대조 검증해 현장에서 큰 변경 불필요'는 검증자 검색 요약에서 확인하지 못했다. 발행일 미확인. |
| f21 | 예 | 예 | 아니오 | 유지 | [추정] 유지: 이 위키의 종합 추론이다. 근거 finding(f1·f4·f6·f7·f8·f11·f13)은 살아남았다. f2 가 강등됐으므로 f2 를 인용하는 부분은 정정된 f2 기준으로 쓴다. |
| f22 | 예 | 예 | 아니오 | 유지 | [추정] 유지: 검증자 열람에서도 factsheet.schema 에 좌표 변환·지도 정합 전용 필드가 없었고 identityReport 에도 없었다. MassRobotics statusReport 의 location 에는 사용 좌표계를 가리키는 planarDatum 참조가 있지만 좌표 대응 자체는 아니다. 브리프의 '팩트시트 최상위 절(7개)' 표현은 f2 정정(필수 6절 + 선택 mobileRobotConfiguration)에 맞춰야 한다. |
| f23 | 예 | 예 | 아니오 | 유지 | [추정] 유지: 분류 원문 9장 '로봇 자체 지능·제어' 경계를 적용한 추론이며 연계 대상 표시가 있다. 근거 f3·f4·f7·f10 이 살아남았다(f10 의 Read Only 근거는 ref-004). |

## 항목별 결과

| 항목 | 결과 | 내용 |
|---|---|---|
| 분류 적합성 | 예 | — |
| 범위 경계 | 예 | — |
| 중복·모순 | 예 | f11·f12·f13 과 트랙 반영 제안(2026-09-25-19·22)이 같은 문헌이다: Beinschob 외 2017(제안 ref-217 ↔ 이번 ref-217), PAN-Robots CORDIS(ref-265 ↔ ref-265), Heselden·Das 2024(ref-269 ↔ ref-269). 같은 URL 이면 퍼블리셔가 기존 id 로 합쳐야 한다., f7(ref-153 플릿 어댑터 튜토리얼)이 트랙 반영 제안의 ref-105(플릿 어댑터 설정)와 같은 문서일 수 있다(퍼블리셔 URL 병합 확인 필요)., f10 은 실행 2026-09-25-50 브리프 f9(ref-251·ref-004)와 같은 주장이다. 같은 각주를 재사용한다., f4(ref-031 이 인용한 LIF 'VDMA 2024-03')와 f5(ref-046 LIF 1.0.0, 2023-09)의 기준일 표기가 다르다(출처 충돌 — 둘 다 제시). |
| 용어 일관성 | 아니오 | 브리프의 '좌표 대응·좌표 정합'(f7·f22·새 열린 질문)은 용어집 map-alignment '지도 정합 (Map Alignment)'과 같은 개념으로 보인다. 페이지 4절 용어 설명에서는 용어집 표기 '지도 정합'을 쓰고 대응점 설정을 그 방법으로 설명해야 한다., 팩트시트는 용어집 vda-5050-factsheet 'VDA 5050 팩트시트', LIF 는 layout-interchange-format '레이아웃 교환 형식', 경로망은 roadmap, 플릿 어댑터는 fleet-adapter 로 이미 있다. 새로 등록하지 말고 연결만 한다. |
| 인용 길이·저작권 | 예 | — |
| 정정 요청 반영 | — | — |

## 수정 지시(required_fixes)

- f2: 본문에서 '일곱 절을 필수로 둔다'를 '유형 사양·물리 파라미터·프로토콜 한계·프로토콜 기능·로봇 기하·적재 사양의 여섯 절(과 헤더 필드)을 필수로 두고, 하드웨어·소프트웨어 버전과 충전 파라미터를 담는 로봇 구성(mobileRobotConfiguration)은 선택 절로 둔다'로 고치고 태그를 [추정]으로 강등한다. 이유: 검증자가 연 factsheet.schema 의 required 배열에 mobileRobotConfiguration 이 없다.
- f22: '팩트시트 스키마 최상위 절' 서술이 f2 의 '일곱 절'을 전제하지 않게 '필수·선택 최상위 절'로 고친다. 태그는 [추정]을 유지한다.
- f10: Full Control·Traffic Light 문장에는 [^ref-251], Read Only 문장에는 공통 참고문헌 [^ref-004](RMF Core Overview)를 붙이고, '새 플릿 온보딩 때 어느 수준으로 연동할지가 선택 사항이 된다'는 부분은 별도 문장의 [추정]으로 분리한다. 이유: ref-251 원문에는 Read Only 문구가 없고 ref-004(rmf-core)에 있다.
- f14: '사물인터넷 장치 개조나 외부 시스템 연동 없이' 구절을 뺀다. 검색 요약에서 확인되지 않았다. 이 연구는 8절(대표 연구와 자료)의 사례로만 두고 ROP 직접 범위로 서술하지 않는다(로봇 자체 지능·제어 연계 영역).
- f20: [추정]·'벤더 주장' 병기를 유지한다. 비교 기준은 '현장 시운전만 한 유사 업그레이드 프로젝트(8주) 대비 시운전 기간 3주 단축(고속 분류기, Tecnomatix Plant Simulation)'으로 적는다. '코드를 시스템 설계와 대조 검증해 현장에서 큰 변경이 필요 없었다'는 빼거나 벤더 서술임을 명시한다. 이유: 검색 요약에 비교 기준이 있고 앞 구절은 확인되지 않았다.
- f4·f5: 7절에서 LIF 를 소개할 때 기준일을 둘 다 제시한다('VDA 5050 3.0.0 은 LIF 를 VDMA 2024-03 으로 인용 [^ref-031]', 'LIF 공식 저장소는 1.0.0 을 2023-09 로 표기 [^ref-046]'). 11절에 '레이아웃 교환 형식(LIF)의 현행 판과 발행일(2023-09 1.0.0 대 VDMA 2024-03)은 무엇인가? | 관련 영역: 21. 온보딩·설정·현장 시운전, 6. 지도·공간·위치 모델 | 근거: f4, f5 | 종류: 출처 충돌' 열린 질문을 올린다. 이유: 두 출처가 다르면 한쪽을 고르지 않는다.
- f12: PAN-Robots '6개월 → 2개월'은 [추정]과 '과제 측 보고값, 비교 조건 미확인'을 유지하고, 원인 설명(기존 표지 활용 위치추정·반자동 공장 탐사)은 과제 측 서술로만 적는다.
- 4절 용어: '좌표 대응·좌표 정합'은 용어집 '지도 정합 (Map Alignment)' 표기로 통일한다. 팩트시트·LIF·경로망·플릿 어댑터는 기존 용어집 항목에 연결하고 신규 등록하지 않는다. glossary_updates 신규 후보는 가상 시운전·플러그 앤 프로듀스·신원 보고 3건만 둔다.
- 각주: 모든 각주 정의가 이번 실행의 원문 열람 여부를 따르게 한다. ref-251·ref-229·ref-217~ref-163 는 접근일 뒤 ' (원문 미열람)'을 붙이고 reference_updates[].source_unopened: true 로 둔다. ref-004 는 공통 참고문헌 페이지의 각주 형식 줄을 그대로 복사한다.
- 10절 연결: f17(문서 해석 LLM)은 교차 규칙대로 5. 로봇 능력·작업 온톨로지와 27. AI·학습·적응과 모델 운영 양쪽에 연결한다. 22. 시뮬레이션·예측용 디지털 트윈 연결은 가상 시운전(f20)·팩트시트의 시뮬레이션 용도(f2)로 한정하고, 8. 실시간 세계 상태·데이터 일관성과 섞지 않는다.
- 트랙 반영 제안: 이번 브리프 finding 이 다시 확인한 내용(traffic-editor f8, 플릿 어댑터 설정 f7, Beinschob 외 f11, Heselden·Das f13, PAN-Robots f12)만 반영한다. MiR·OTTO 벤더 주장(ref-271·ref-219), Boniardi 외 2019, ref-266~ref-268, 국내 건설로봇 문헌고찰은 본문에 넣지 않고 다음 실행 후보로 둔다. 이유: 이번 실행에서 검증하지 않았다.
- f1: 팩트시트 토픽 설명의 인용 위치는 'VDA 5050 3.0.0 표 2(4.3절)'로 적는다. 직접 인용은 이 출처당 1회만 한다.

## 검증 노트

판정: 1차 조건부 승인. 이번 실행은 원문 열람이 차단된 환경(mirror_only)에서 검증됐다. GitHub 원문(ref-031 입력 원문, ref-228·ref-230·ref-153·ref-079·ref-643·ref-046·ref-229, ref-251·ref-004 는 검증자 열람)은 직접 대조했고, 나머지는 검색 결과 일치로 확인했다. 확인 22건, 미확인 1건, 교차 확인 0건. 강등: f2 사실 → 추정(팩트시트 필수 절은 6개이고 mobileRobotConfiguration 은 선택). 원문 미열람 출처: ref-217, ref-269, ref-037, ref-637, ref-470, ref-639, ref-640, ref-265, ref-163(ref-251·ref-229 는 브리프에 미열람으로 표시됐으나 검증자가 GitHub 원문으로 실재를 확인). 주의: 모든 주장이 단일 출처이다. 설치 기간 단축 수치(PAN-Robots 6→2개월, Siemens 3주)는 과제·벤더 측 보고값이다. f21~f23 은 이 위키의 종합 추론이다. f10 의 Read Only 근거는 ref-004 다. LIF 기준일은 두 출처가 다르다(2023-09 대 VDMA 2024-03). oq-022 는 해결되지 않았다. 정정 요청 없음. 검색은 리서치 18회와 검증 11회로 합계 29회/30이다.
