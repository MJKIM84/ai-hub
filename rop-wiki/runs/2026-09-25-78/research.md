# 리서치 브리프 2026-09-25-78

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-78 |
| 날짜 | 2026-09-25 |
| 실행 유형 | track (트랙 실행) |
| 대상 영역 | 6. 지도·공간·위치 모델 |
| 대분류 | B. 공통 정보·환경 모델 |

트랙 실행: 트랙 `floorplan-recognition` · 단계 4 · 답한 질문 q4-04

## 갭(비어 있거나 약한 섹션)

- 단계 4 질문 q4-04 열림(target.json 지정, CLI 지정 질문 id). 단계 4 페이지 3절에 q4-04 소제목 없음
- 공간 그래프 스키마 초안 6절: '정렬 정보·도면–현장 차이·지도 버전을 층별 지도 속성으로 둘지 별도 개념으로 둘지' 항목 가운데 지도 버전 부분 미해결(실행 2026-09-25-44 에서 '지도 판' 속성 제안 거부)
- 공간 그래프 스키마 초안 2절: 평면도 '버전' 속성의 값 체계(도면 개정 식별 방식) 근거 없음
- 도면–현장 정합 절차 초안(실행 2026-09-25-76)에 도면·지도 판이 바뀔 때 무엇을 다시 확인하는지(재검증 범위)가 없음
- 24. 자산·소프트웨어 수명주기 관리 섹션 6에 지도 판 관리·재검증 근거 약함(이 영역 정의의 '지도' 버전)

## 조사 질문

1. 제조사마다 다른 지도에서 ‘3층 출하 대기장’을 어떻게 동일한 장소로 인식할까? [분류원문]
2. q4-04 도면과 지도가 바뀔 때 버전 관리와 재검증은 어떻게 두는가?
3. 로봇 관제·교환 형식(VDA 5050 3.0.0 지도·구역 집합 배포, Open-RMF 건물 지도 메시지, VDMA LIF)은 지도·레이아웃의 판을 무엇으로 식별하고 새 판의 배포·활성화·삭제를 어떻게 다루는가? (단계 4 페이지 3절, 스키마 초안 6절 겨냥)
4. 건축 도면·BIM 쪽은 도면 개정을 어떻게 식별·관리하고(ISO 19650 공통 데이터 환경의 상태·개정 코드, 국내 CDE 연구) 두 판의 차이를 어떻게 계산하는가(IFC 비교 도구, 버전 관리 연구)? (한국 자료 우선 규칙)
5. 지도가 바뀐 뒤 무엇을 다시 검증해야 하는가 — 지도 갱신의 안전장치, 운용 구역 변경과 위험성평가 갱신(ISO 3691-4, ANSI/A3 R15.08-2)은 재검증에 무엇을 요구하는가? (25. 안전·위험 관리, 23. 시험·형식 검증·벤치마크 연결)
6. 도면 판·공간 그래프 판·제조사 지도 판·구역 집합·좌표 변환을 어떻게 서로 대응시켜 재검증 범위를 좁히는가? (24. 자산·소프트웨어 수명주기 관리 섹션 6 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 3.0.0 은 지도를 지도 식별자(mapId, 로봇 작업 공간의 특정 구역)와 지도 판(mapVersion, 이전 판의 갱신)의 조합으로 유일하게 식별하고, 로봇은 주문을 받기 전에 주문의 각 mapId 에 해당하는 지도가 있는지 확인해 없으면 UNKNOWN_MAP_ID 경고를 보고하며, 올바른 지도가 활성화되었는지 보장하는 책임은 관제에 둔다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f2 | [사실] | VDA 5050 3.0.0 은 지도 파일을 지도 서버에서 로봇이 미리 내려받게 하고(downloadMap, 선택 파라미터 mapHash) 내려받기와 활성화(enableMap)를 별개 절차로 두며, 활성화 시 같은 mapId 의 다른 판은 비활성화되어 mapId 마다 한 판만 활성이고, 같은 mapId·mapVersion 의 재다운로드는 DUPLICATE_MAP 으로 거부되며, 로봇은 지도를 스스로 지우지 않고 삭제는 관제가 deleteMap 으로 요청한다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f3 | [사실] | VDA 5050 3.0.0 에서 구역 집합(zoneSet)은 mapId 에만 연결되고 mapVersion 은 참조하지 않아 같은 구역 집합을 한 지도의 여러 판에 쓸 수 있으며, 구역 집합의 내용은 바뀌지 않아 변경 시 새 zoneSetId 를 쓰고, 새로 추가된 구역 집합은 DISABLED 상태였다가 enableZoneSet 으로 활성화되며 mapId 마다 하나만 활성이다. | ref-031 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f4 | [사실] | VDA 5050 3.0.0 은 관제가 주문의 노드 위치에 mapId 를 보낼 때 해당 지도가 로봇에 활성화되어 있도록 보장하게 하고, 로봇을 새 지도의 특정 위치에 놓아야 하면 initializePosition 즉시 동작(x·y·theta·mapId·lastNodeId)을 쓰게 한다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f5 | [사실] | Open-RMF 건물 지도 메시지(BuildingMap)는 이름(name)·층 목록(levels)·승강기 목록(lifts) 세 필드만 두고 판·개정·시각·해시 필드는 두지 않는다. | ref-744 | 아니오 | medium | 2026-09-25 | — | — |
| f6 | [사실] | VDMA LIF 에 대한 제3자(continua-systems) JSON 스키마에서 레이아웃은 층과 함께 판(layoutVersion)을 가지며, 이를 LIF 공식 구조로 확정하지는 못했다. | ref-212 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f7 | [사실] | ISO 19650 을 따르는 공통 데이터 환경(Common Data Environment, CDE)에서는 도면·모델 같은 정보 컨테이너가 작업 중(WIP)·공유·발행·보관 상태를 거치며, 컨테이너마다 상태(용도 적합성) 코드와 개정(revision) 코드를 메타데이터로 붙인다. | ref-745, ref-746 | 아니오 | medium | 2020-09 | — | 원문 미열람 |
| f8 | [사실] | 국내 연구(이일곤·김현민·안준상·최재웅, 2023)는 ISO 19650 기반 한국형 공통 데이터 환경 개발을 위해 CDE 워크플로우와 정보 컨테이너 체계를 수립했다. | ref-747 | 아니오 | medium | 2023 | — | 원문 미열람 |
| f9 | [사실] | IfcOpenShell 의 IfcDiff 는 두 IFC 모델을 비교해 새 모델에만 있는 요소(추가)·옛 모델에만 있는 요소(삭제)·양쪽에 있으나 바뀐 요소(변경)의 GlobalId 목록을 JSON 으로 내며, 같은 요소는 두 모델에서 GlobalId 가 같다고 가정하고, 형상·속성·관계 외에 유형·속성 세트·공간 컨테이너·집합·분류 비교를 선택할 수 있다. | ref-743 | 아니오 | medium | 2026-09-25 | — | — |
| f10 | [사실] | Liu 외(arXiv 2312.14931)는 IFC 데이터의 그래프 구조에서 일어나는 등가 변환 때문에 IFC 파일의 판 비교와 증분 저장이 어렵다고 보고, 정규화한 IFC 파일을 Git 같은 도구로 판 비교·증분 저장할 수 있게 하는 병렬 정규화 방법을 제안했다. | ref-748 | 아니오 | medium | 2023-12 | — | 원문 미열람 |
| f11 | [사실] | Esser·Vilgertshofer·Borrmann(Automation in Construction 155, 2023-11)은 BIM 모델을 그래프로 표현하고 그래프 변환으로 객체 수준의 증분 변경을 기술해, 동시에 수정된 모델의 충돌하지 않는 변경과 충돌하는 변경을 가려 병합하는 버전 관리 방법을 제안했다. | ref-749 | 아니오 | medium | 2023-11 | — | 원문 미열람 |
| f12 | [사실] | 연계 대상: Stefanini 외(2023)의 라이다 지도 갱신 방법은 위치추정 오차가 커질 때 잘못된 지도 갱신을 막는 위치추정 성능 기반 안전장치를 둔다. | ref-652 | 아니오 | medium | 2023-06-30 | — | 원문 미열람 |
| f13 | [사실] | ISO 3691-4 는 운용 구역의 상태가 무인 산업용 트럭의 안전한 운행에 큰 영향을 준다고 보고, 운용 구역의 위험을 없애기 위한 준비를 부속서 A 에 규정한다. | ref-470 | 아니오 | medium | 2023 | 제약 | 원문 미열람 |
| f14 | [사실] | ANSI/A3 R15.08-2-2023 은 산업용 이동로봇이나 그 플릿을 현장에 통합·설정·맞춤화할 때의 요구사항을 정하고, 위험성평가를 반복 과정으로 강조한다. | ref-472 | 아니오 | medium | 2023-10 | — | 원문 미열람 |
| f15 | [추정] | NODE Robotics 는 NODE.maps 가 연결된 모든 로봇에 지도를 올리고 편집·유지·배포하며 개별 로봇의 실시간 갱신을 공유 지도로 합친다고 소개한다. | ref-752 | 아니오 | low | 2026-09-25 | — | 원문 미열람, 벤더 주장 |
| f16 | [사실] | Open-RMF 플릿 어댑터는 로봇 지도와 RMF 좌표의 변환을 층(지도)마다 대응 경유점(최소 4쌍 권장)으로 따로 추정하고 층별 변환 오차 추정값을 기록하게 한다. | ref-153 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f17 | [추정] | 확인한 식별 방식을 이 위키가 묶으면, 도면–지도 체계에는 도면 개정(CDE 상태·개정 코드, IFC GlobalId), 공통 공간 그래프 판, 제조사별 지도 판(mapId·mapVersion), 구역 집합(zoneSetId), 제조사·층별 좌표 변환이 각기 다른 계보로 존재하므로, ROP 는 이들을 한 행으로 묶는 판 대응표를 따로 두어야 할 것으로 보인다. | ref-745, ref-743, ref-031, ref-212, ref-744, ref-153 | 아니오 | low | 2026-09-25 | — | — |
| f18 | [추정] | 재검증 범위는 도면 판 차이(추가·삭제·변경 요소)에서 영향받는 공간 노드·차선·목적지를 추리고, 그 요소가 걸친 제조사 지도·구역 집합·좌표 변환만 다시 확인(목적지 대응점 잔차 재계산, 해당 차선·구역 규칙 재확인)하는 식으로 좁힐 수 있을 것으로 보이며, GlobalId 가 없는 CAD·래스터 도면은 요소 대응을 따로 만들어야 할 것으로 보인다. | ref-743, ref-748, ref-749, ref-031, ref-153 | 아니오 | low | 2026-09-25 | — | — |
| f19 | [추정] | VDA 5050 의 사전 적재·별도 활성화·mapId 당 단일 활성 판 규칙을 이용하면, 새 지도 판을 미리 내려받아 비활성 상태로 두고 재검증을 마친 뒤 같은 시점에 활성화하며 직전 판은 삭제 전까지 되돌림 후보로 남기는 배포 순서가 가능해 보이지만, 명세는 되돌림 절차를 따로 정하지 않는다. | ref-031 | 아니오 | low | 2026-09-25 | — | — |
| f20 | [추정] | Open-RMF 건물 지도 메시지에 판 필드가 없고 LIF 판 필드는 제3자 스키마로만 확인되므로, 이종 제조사를 연결하는 ROP 는 공간 그래프·건물 지도의 판 식별자와 생성 이력을 형식 밖 메타데이터로 직접 관리해야 할 것으로 보인다. | ref-744, ref-212, ref-031 | 아니오 | low | 2026-09-25 | — | — |
| f21 | [추정] | 운용 구역 상태가 안전 운행에 영향을 주고 위험성평가가 반복 과정이라는 표준의 입장을 보면, 도면·지도 변경은 구역·동선 변경 여부에 따라 안전 재검토가 필요한 변경과 그렇지 않은 변경으로 나누어야 할 것으로 보이며, 보호 영역·안전 기능의 재검증 자체는 로봇·통합자 쪽 연계 대상이다. | ref-470, ref-472 | 아니오 | low | 2026-09-25 | 예외·성과 | 원문 미열람 |
| f22 | [추정] | ‘3층 출하 대기장’의 랙 배치가 바뀌어 한 제조사 지도만 새 판으로 바뀌면, 판 대응표의 해당 행(대기장 목적지·제조사 mapVersion·좌표 변환)이 활성 판과 일치하는지 확인하기 전까지 그 로봇의 대기장 도착 판정을 보류하는 규칙이 필요할 것으로 보인다(설명용 가정 사례). | ref-031, ref-153 | 아니오 | low | 2026-09-25 | 출하 / 완료·인계 | — |
| f23 | [추정] | 이번 검색 범위(한국어 2회 포함 13회)에서는 건축 도면 개정과 로봇 지도 판을 연결해 재검증 범위를 정한 표준·연구나 국내 물류센터 사례를 찾지 못했다(부재 확인 아님). | ref-747, ref-745, ref-031 | 아니오 | low | 2026-09-25 | — | — |

### 근거 발췌

- **f1**: 6.3.1: 각 지도는 mapId 와 mapVersion 조합으로 식별. 주문 수락 전 mapId 별 지도 보유 확인, 없으면 'UNKNOWN_MAP_ID'(WARNING). "It is the responsibility of the fleet control to ensure that the correct maps are enabled" (명세 3.0.0, 발행일 미확인, 확인일 기준)
- **f2**: 6.3.1~6.3.5: 지도는 로봇에 사전 적재·버퍼링, 전송과 활성화는 다른 과정, 활성화 시 같은 mapId 다른 mapVersion 은 DISABLED, 중복 판 다운로드는 'DUPLICATE_MAP', 'The mobile robot itself shall not delete maps.' (발행일 미확인, 확인일 기준)
- **f3**: 6.4.2: zoneSet 은 mapId 로 단일 지도에 연결, 'The mapVersion shall not be referenced, as the same zone set might be intended to be used for several versions of one map.' 내용 불변·새 zoneSetId, 신규는 DISABLED (발행일 미확인, 확인일 기준)
- **f4**: 6.3.4: 관제는 주문 nodePosition 의 mapId 에 맞는 지도가 활성화되도록 보장해야 하며, 새 지도의 특정 위치에 로봇을 두려면 initializePosition 을 써야 한다 (발행일 미확인, 확인일 기준)
- **f5**: BuildingMap.msg 필드: string name, Level[] levels, Lift[] lifts. version·revision·timestamp·hash 필드 없음(메시지 정의 범위 관찰, 발행일 미확인, 확인일 기준)
- **f6**: 제3자 스키마 기준: 레이아웃은 layoutVersion 으로 판을 식별(공식 LIF 저장소 README 는 이번에 열었으나 명세 머리말만 읽혀 필드 확인 못 함) (재인용: 2026-09-25-44) (발행일 미확인, 확인일 기준)
- **f7**: UK BIM Framework Guidance Part C(2020-09): CDE 메타데이터에 이름·설명·Status·Revision·작성자 등, 상태 코드는 ISO 19650-2 국가 부속서 기준. 상태 WIP·Shared·Published·Archived 는 BibLus(벤더 블로그) 요약 기준, 원문 미열람
- **f8**: 논문 제목 'ISO 19650 기반의 한국형 공통데이터환경(CDE) 개발을 위한 CDE 워크플로우와 정보컨테이너 체계 수립 연구', 2023-12-06 게재 승인(검색 요약 기준, 게재지·세부 체계 미확인)
- **f9**: "Changes are made on the assumption that the GlobalId of an element in one model is consistent with the same element in another model." 출력 Added·Deleted·Changed, 기본 파일 diff.json (IfcOpenShell v0.8.0 문서 원본, 확인일 기준)
- **f10**: 초록 요약: 등가 변환의 영향을 줄이는 IFC 정규화로 정규화 파일을 Git 류 도구의 판 비교·증분 저장에 직접 사용, CDE 응용 가능성 제시(원문 미열람)
- **f11**: 검색 요약: 객체 수준 낙관적 동시성 제어, 그래프 변환으로 증분 변경 기술, 비충돌·충돌 수정 식별과 병합(원문 미열람)
- **f12**: 검색 요약: 위치추정 성능 기반 fail-safe 가 위치추정 오차 증가 시 잘못된 지도 갱신을 방지(원문 미열람)
- **f13**: 검색 요약: 운용 구역 상태가 안전 운행에 큰 영향, 운용 구역 준비는 Annex A 에 규정(원문 미열람, 2023 판 페이지 기준, 변경 시 재검증 조문은 미확인)
- **f14**: A3 발표: R15.08-2 는 IMR·IMR 플릿의 현장 통합·설정·맞춤화 요구사항, 'risk assessment as an iterative process' 강조(원문 미열람, 지도 변경 시 재평가 조문은 미확인)
- **f15**: 벤더 주장: 지도 업로드·편집·유지·배포로 플릿 운영의 일관된 기준 제공, Live Maps 가 로봇별 갱신을 전역 지도로 병합(원문 미열람, 발행일 미확인, 확인일 기준)
- **f16**: 층마다 대응 경유점 4쌍 이상 권장, nudged 로 회전·축척·이동 추정 후 층별 MSE 기록 (재인용: 2026-09-25-76) (발행일 미확인, 확인일 기준)
- **f17**: 이 위키의 종합. 근거: CDE 개정 메타데이터(f7), GlobalId 기반 비교(f9), mapId·mapVersion·zoneSetId(f1·f3), LIF layoutVersion(f6), BuildingMap 판 필드 부재(f5), 층별 변환(f16). 단일 출처 없음
- **f18**: 이 위키의 종합. IfcDiff 의 추가·삭제·변경 목록(f9)과 IFC 판 비교의 어려움(f10)·객체 수준 증분 변경(f11)을 재검증 범위 산정에 쓰는 사례는 찾지 못함
- **f19**: 근거 f2(사전 적재, 다운로드≠활성화, enableMap 시 같은 mapId 다른 판 DISABLED, 로봇은 지도 자체 삭제 금지). 되돌림 순서는 이 위키의 추정
- **f20**: 이 위키의 종합. 근거 f5·f6·f1. 다른 Open-RMF 산출물(주행 그래프 파일 등)의 판 표기는 미확인
- **f21**: 이 위키의 종합. 근거 f13·f14. 변경 분류 기준을 정한 조문은 원문 미열람으로 미확인
- **f22**: 이 위키의 추정. VDA 5050 은 주문 mapId 에 맞는 지도 활성화를 관제 책임으로 둠(f1·f4), 좌표 변환은 층·지도별(f16)
- **f23**: 도면 쪽(CDE·IFC 비교)과 로봇 쪽(VDA 5050 지도 배포, 지도 갱신 연구)이 따로 확인됨. 둘을 잇는 자료는 검색 범위에서 없음

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-212 | continua-systems (GitHub) | vdma-lif — schema/lif-schema.json (JSON parsers and models for the VDMA LIF, VDMA 공식 산출물이 아닌 제3자 스키마) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/continua-systems/vdma-lif/blob/main/schema/lif-schema.json | 예 |
| ref-652 | Stefanini, E., Ciancolini, E., Settimi, A., & Pallottino, L. | Safe and Robust Map Updating for Long-Term Operations in Dynamic Environments | 2023-06-30 | 논문 | medium | 2026-09-25 | https://www.mdpi.com/1424-8220/23/13/6066 | 예 |
| ref-153 | Open Robotics | Fleet Adapter Tutorial - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html | 예 |
| ref-743 | IfcOpenShell (IfcOpenShell GitHub) | IfcDiff - IfcOpenShell documentation (src/ifcopenshell-python/docs/ifcdiff.rst, v0.8.0) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://docs.ifcopenshell.org/ifcdiff.html | 아니오 |
| ref-744 | Open Robotics (open-rmf) | rmf_building_map_msgs — rmf_building_map_msgs/msg/BuildingMap.msg | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_building_map_msgs/blob/main/rmf_building_map_msgs/msg/BuildingMap.msg | 아니오 |
| ref-745 | UK BIM Framework | Information management according to BS EN ISO 19650 Guidance Part C: Facilitating the common data environment (workflow and technical solutions), Edition 1 | 2020-09 | 정부·연구기관 | medium | 2026-09-25 | https://ukbimframework.org/wp-content/uploads/2020/09/Guidance-Part-C_Facilitating-the-common-data-environment-workflow-and-technical-solutions_Edition-1.pdf | 예 |
| ref-746 | ACCA software (BibLus) | Container Information States ISO 19650: WIP, Shared, Published, Archived | 미확인 | 벤더 문서 | low | 2026-09-25 | https://biblus.accasoftware.com/en/container-information-states-iso-19650-wip-shared-published-archived/ | 예 |
| ref-747 | 이일곤, 김현민, 안준상, 최재웅 | ISO 19650 기반의 한국형 공통데이터환경(CDE) 개발을 위한 CDE 워크플로우와 정보컨테이너 체계 수립 연구 | 2023 | 논문 | medium | 2026-09-25 | https://koreascience.kr/article/JAKO202309243229252.pdf | 예 |
| ref-748 | Liu, H. 외 | A Parallel IFC Normalization Algorithm for Incremental Storage and Version Control | 2023-12 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2312.14931 | 예 |
| ref-749 | Esser, S., Vilgertshofer, S., & Borrmann, A. (Automation in Construction 155, 105063) | Version control for asynchronous BIM collaboration: Model merging through graph analysis and transformation | 2023-11 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/pii/S0926580523003230 | 예 |
| ref-472 | A3 (Association for Advancing Automation) | ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available | 2023-10 | 표준 | medium | 2026-09-25 | https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available | 예 |
| ref-470 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 2023 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/83545.html | 예 |
| ref-752 | NODE Robotics | Real-time Robot Map Management for Mobile Fleets (NODE.maps) | 미확인 | 벤더 문서 | low | 2026-09-25 | https://node-robotics.com/solutions/node-fleet-autonomy-services/nodemaps | 예 |

### 출처 요약

- **ref-031**: VDA 5050 3.0.0 명세. 지도 식별(mapId·mapVersion)·배포·활성화·삭제, 구역 집합 전달 규칙을 확인했다.
- **ref-212**: 원문 미열람. VDMA LIF 제3자 JSON 스키마. 레이아웃의 층·판(layoutVersion)과 스테이션 구조(이전 실행 확인 내용 재인용).
- **ref-652**: 원문 미열람. 장기 운영용 라이다 지도 갱신 방법. 위치추정 성능 기반 안전장치로 잘못된 갱신을 막는다.
- **ref-153**: 원문 미열람(이번 실행에서 다시 열지 않음). 층별 대응 경유점으로 로봇 지도–RMF 좌표 변환과 오차를 구하는 절차(실행 2026-09-25-76 재인용).
- **ref-743**: 두 IFC 모델을 GlobalId 기준으로 비교해 추가·삭제·변경 요소를 JSON 으로 내는 오픈소스 도구 문서.
- **ref-744**: Open-RMF 건물 지도 메시지 정의. name·levels·lifts 세 필드만 있고 판 필드는 없다.
- **ref-745**: 원문 미열람. ISO 19650 공통 데이터 환경 워크플로우 지침. 정보 컨테이너의 상태·개정 메타데이터와 상태 전환을 다룬다.
- **ref-746**: 원문 미열람. ISO 19650 정보 컨테이너 상태(작업 중·공유·발행·보관)를 설명하는 BIM 소프트웨어 업체 블로그.
- **ref-747**: 원문 미열람. ISO 19650 기반 한국형 CDE 의 워크플로우와 정보 컨테이너 체계를 수립한 국내 연구.
- **ref-748**: 원문 미열람. IFC 등가 변환의 영향을 줄이는 정규화로 Git 류 도구의 판 비교·증분 저장을 가능하게 하는 방법(프리프린트).
- **ref-749**: 원문 미열람. BIM 모델의 그래프 표현과 그래프 변환으로 객체 수준 증분 변경을 기술하고 동시 수정을 병합하는 버전 관리 방법.
- **ref-472**: 원문 미열람. 표준 발행 기관의 R15.08-2 발행 안내. 산업용 이동로봇 플릿의 현장 통합 요구사항과 반복적 위험성평가를 소개한다.
- **ref-470**: 원문 미열람. 무인 산업용 트럭과 그 시스템의 안전 요구사항·검증 표준. 운용 구역 준비를 부속서 A 에 둔다.
- **ref-752**: 원문 미열람. 플릿 지도 관리 서비스 소개(업로드·편집·배포·실시간 병합), 벤더 주장.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md | 2, 3, 4, 5, 6, 8, 9 | q4-04 답: f1·f2·f3·f4·f5·f6·f7·f8·f9·f10·f11·f12·f13·f14·f15·f16·f17·f18·f19·f20·f21·f22·f23 (신뢰도 low) — 2절 q4-04 상태 답함, 3절 q4-04 소제목 신설({#q4-04}): 로봇 쪽 지도 판 식별·배포(VDA 5050 mapId·mapVersion·사전 적재·활성화·삭제 f1·f2·f4, 구역 집합과 판 f3, Open-RMF 건물 지도 판 필드 부재 f5, LIF layoutVersion f6, 벤더 지도 관리 f15 벤더 주장), 도면 쪽 개정 관리(ISO 19650 CDE 상태·개정 f7, 국내 CDE 연구 f8), 판 차이 계산(IfcDiff f9, IFC 정규화 f10, 그래프 기반 병합 f11), 재검증 요구(지도 갱신 안전장치 f12 연계 대상, 운용 구역·위험성평가 f13·f14, 층별 변환 f16), 종합: 판 대응표(f17)·차이 기반 재검증 범위(f18, mermaid 흐름 권장)·사전 적재 후 활성화 배포 순서(f19)·형식 밖 판 메타데이터(f20)·안전 재검토 구분(f21)·‘3층 출하 대기장’ 판 불일치 시나리오(f22)·근거 공백(f23) / 4절 결론·불확실성 / 5절 후속 질문 / 6절 완료 조건 현황 / 8절 출처 / 9절 이력 |
| update | docs/ideas/floorplan-recognition.md | 5 | 아이디어 페이지 5절(트랙 산출물): '도면·지도 판 관리와 재검증' 소절 신설 — 근거 f1·f2·f3·f5·f7·f9, 구현 가설 f17·f18·f19·f20(추정). 도면–현장 정합 절차 초안의 6단계(운영 중 처리) 뒤에 판 교체 시 재검증 단계를 잇는 형태로 제안 |
| update | docs/tracks/floorplan-recognition/space-graph-schema-draft.md | 2, 6 | 트랙 산출물 갱신: track.ontology_changes 가 승인되면 2절 평면도 '버전' 속성 값 후보(ISO 19650 상태·개정 코드, f7)와 층별 지도 '판 식별자(후보)' 속성(f1·f5·f6) 반영. 미승인 시 6절 '정렬 정보·도면–현장 차이·지도 버전' 항목의 지도 버전 부분 근거 보강(f1·f2·f3·f5·f17·f19·f20) |
| update | docs/categories/f-deployment-verification-and-maintenance/24-asset-and-software-lifecycle-management.md | 6 | 트랙 floorplan-recognition 단계 4 반영 제안 (f1, f2, f3, f7, f9, f17, f18, f19): 지도 판 식별·사전 적재·활성화·삭제 규칙, 도면 개정 관리(CDE)와 IFC 판 비교, 판 대응표와 차이 기반 재검증 범위(추정) |
| update | docs/categories/b-common-information-and-environment-model/06-map-space-and-location-model.md | 6, 9 | 트랙 floorplan-recognition 단계 4 반영 제안 (f1, f5, f17, f20, f22): 6절(주제 페이지 area06-s6)에 지도 판 관리와 판 대응표(추정), 9절에 판 대응표·재검증 범위 산정은 ROP, 지도 갱신 계산·안전 기능 재검증은 연계 대상이라는 경계(추정) |
| update | docs/categories/f-deployment-verification-and-maintenance/23-testing-formal-verification-and-benchmarking.md | 6 | 트랙 floorplan-recognition 단계 4 반영 제안 (f9, f18, f21): 도면 판 차이(추가·삭제·변경)에서 재검증 범위를 좁히는 방법과 안전 재검토가 필요한 변경의 구분(추정), oq-090 근거 보강 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 공통 데이터 환경 | Common Data Environment (CDE) | ISO 19650 이 정한, 프로젝트·자산의 정보 컨테이너를 합의된 절차로 모으고 관리·배포하는 단일 정보원으로, 컨테이너를 작업 중·공유·발행·보관 상태로 다루고 상태·개정 메타데이터를 붙인다. |
| 정보 컨테이너 | Information Container | 파일·시스템·응용 저장소에서 꺼낼 수 있는 이름 붙은 지속적 정보 묶음으로, 도면·모델·문서가 이에 해당하며 공통 데이터 환경에서 상태와 개정이 관리된다. |

## 열린 질문

새로 생긴 질문:

- 제조사가 자사 로봇 지도(SLAM 지도)의 판을 바꿀 때 변경 내용과 판 식별자를 ROP 나 상위 관제에 알리는 계약·인터페이스 관행이나 공개 사례가 있는가? | 관련 영역: 24. 자산·소프트웨어 수명주기 관리, 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f5 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 14 · 교차 확인: 0
- 예산 사용량: 검색 13회 · 신규 출처 10건
- 미확인 항목:
    - 모든 finding 교차 확인 없음: 로봇 쪽 판 관리 근거(f1~f4)는 VDA 5050 명세 한 곳, f7 의 두 출처 가운데 상태 목록은 벤더 블로그 요약 기준
    - f6 LIF layoutVersion 은 제3자 스키마 재인용이며 공식 LIF 저장소 README 는 명세 머리말만 읽혀 필드를 확인하지 못함
    - f7 ISO 19650 상태·개정 코드(S0~S7, P01·C01 등) 세부 값은 블로그 검색 요약에만 있어 finding 에 넣지 않음
    - f8 국내 CDE 연구의 게재지와 워크플로우 세부 미확인
    - f13 ISO 3691-4 의 변경 후 재검증 조문, f14 R15.08-2 의 지도·경로 변경 시 재평가 조문은 원문 미열람으로 미확인(재검증 의무를 말한 자료는 업체 블로그뿐이라 넣지 않음)
    - f5 판 필드 부재는 BuildingMap.msg 한 파일 관찰이며 Open-RMF 주행 그래프 파일·building.yaml 의 판 표기는 미확인
    - f17~f23 은 이 위키의 종합이며 도면 개정과 로봇 지도 판을 잇는 단일 출처는 찾지 못함
- 범위 경계 위반 의심:
    - f12: 라이다 지도 갱신 알고리즘은 분류 원문 9장 '로봇 자체 지능·제어' 연계 영역이라 '연계 대상: '으로 표시하고 재검증 안전장치의 사례로만 씀
    - f13·f14·f21: 보호 영역·안전 기능 재검증은 로봇·통합자 쪽이며 ROP 쪽은 변경 분류와 재검토 요청까지로 한정해 서술
- 한계: web_fetch_available: false · fetch_mode mirror_only. 원문을 연 출처: ref-031(입력 원문 텍스트, inbox), raw.githubusercontent.com 으로 신규 ref-743(IfcOpenShell ifcdiff.rst v0.8.0)·ref-744(BuildingMap.msg). LIF 공식 README 는 열었으나 명세 머리말만 읽혀 출처로 쓰지 않음. 나머지 신규 8건과 재사용 ref-212·ref-652·ref-153 은 원문 미열람이라 신뢰도 상한 medium, 원문을 연 출처도 공통 규칙 0절 6항에 따라 high 를 주지 않음. 검색 13회/40(한국어 3회), 신규 출처 10건/20(ref-743~ref-752, 예약 구간 안), 재사용 4건. 질문 선택: target.json 지정 q4-04 1건. q4-04 는 로봇 쪽 지도 판 식별·배포 규칙(사실)과 도면 쪽 개정 관리·판 비교(사실)로 답했으나, 판 대응표·차이 기반 재검증 범위·배포 순서(f17~f22)는 이 위키의 종합이라 질문 종합 신뢰도 low. 한국 자료: 국내 CDE 연구(ref-747) 1건, 국내 물류센터의 지도 판 관리 사례는 찾지 못함. 교차 규칙: 27. AI·학습·적응과 모델 운영 관련 finding 없음. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 정정 요청 없음. 후속 질문 2건, 온톨로지 변경 제안 2건(층별 지도 판 식별자 제안은 실행 2026-09-25-44 의 '지도 판' 속성 거부와 같은 대상이라 description 에 충돌 명시). 일반 열린 질문 1건. 페이지 제안: 트랙 산출물 3건, 세부영역 반영 제안 3건(갱신 상한과 별도). 백로그 참고: q4-13 과 q4-14 가 같은 질문으로 중복 등록되어 정리 필요.

## 트랙 블록

- 트랙: floorplan-recognition · 단계: 4
- 답한 질문 id: q4-04

### 새 질문

| 제안 id | 질문 | 보낼 단계 | 근거 finding |
|---|---|---|---|
| — | 도면 개정의 판 차이(IfcDiff 의 추가·삭제·변경 요소)에서 영향받는 공간 노드·차선·목적지와 그 요소가 걸친 제조사별 지도 판·구역 집합·좌표 변환을 자동으로 추려 재검증 범위를 정하는 규칙은 무엇이며, GlobalId 가 없는 CAD·래스터 도면에서는 요소 대응을 어떻게 만드는가? (q4-04 에서 파생) | 4 | f18 |
| — | 지도 판을 교체한 뒤 재검증 시험(목적지 대응점 잔차, 영향받은 차선 주행, 구역 규칙 확인)의 합격 기준과 판 교체에 드는 중단 시간·재검증 공수를 어떤 지표로 측정하는가? (q4-04 에서 파생) | 5 | f19 |

### 온톨로지 초안 변경 제안

| 동작 | 종류 | 이름 | 근거 finding | 설명 |
|---|---|---|---|---|
| modify | concept | 평면도 (Floor Plan) | f7, f9 | 기존 속성 '버전'에 값 후보 'ISO 19650 공통 데이터 환경의 상태(용도 적합성) 코드·개정 코드'를 병기하고, IFC 입력은 요소 GlobalId 로 판 사이 요소를 대응시킬 수 있다는 메모를 둔다. 기존 속성과 충돌하지 않는다. 상태·개정 코드의 세부 값(S0~S7, P01·C01)은 블로그 요약 근거라 넣지 않는다. |
| modify | concept | 층별 지도 (Floor Map) | f1, f3, f5, f6 | 속성 '판 식별자(후보)'를 더한다: VDA 5050 mapId·mapVersion(구역 집합은 mapVersion 이 아니라 mapId 에 연결), 제3자 LIF 스키마의 layoutVersion, Open-RMF 건물 지도는 판 필드 없음. 실행 2026-09-25-44 에서 '지도 판' 속성 제안이 6절 지도 버전 질문을 근거 없이 결정한다는 이유로 거부된 것과 같은 대상이며, 이번 제안은 q4-04 답으로 그 질문의 판 식별 부분에 근거를 더한 것이다. 판 대응표를 별도 개념으로 둘지(f17 추정)는 정의에 넣지 않고 6절 질문으로 둔다. |

### 단계 완료 조건 자체 평가

- 충족 여부(자체 평가): 미충족
- 못 채운 조건:
    - 도면–현장 정합 절차 초안의 검증 판정이 '충족 · 미승인' 상태이며 이번 q4-04 답(판 관리·재검증)도 검증 승인 전
    - 열린 질문 q4-05·q4-07·q4-08·q4-09·q4-10·q4-11·q4-12·q4-13(q4-14 중복)
