# 스토리텔러 산출 2026-09-30-04

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/space-and-map-model/place-semantics-and-map-management.md | draft | 영역 심화: 3~11절 신규 작성(병원·가정·기타 적용 사례, 장소 목록·지도 버전·구역 집합·차선 폐쇄, 책임 경계, 연결 14개 영역, 열린 질문 9건), 13절 각주, 프런트매터 갱신. 2차 수정: 8절 첫 문장을 이번 브리프 자료 범위로 한정하고 ref-1031 각주 정의 추가 |
| create | docs/topics/2026/2026-09-30-area16-s6.md | draft | 자동 분리: 16. 장소 의미·지도 관리 의 "6. 대표 접근법과 기술" 절(2,190자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area16-s11.md | draft | 자동 분리: 16. 장소 의미·지도 관리 의 "11. 열린 질문" 절(1,766자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area16-s7.md | draft | 자동 분리: 16. 장소 의미·지도 관리 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,125자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area16-s8.md | draft | 자동 분리: 16. 장소 의미·지도 관리 의 "8. 대표 연구와 자료" 절을 옮겼다. 2차 수정: 1절·3절 첫 문장을 이번 브리프 자료 범위로 한정 |
| create | docs/topics/2026/2026-09-30-area16-s4.md | draft | 자동 분리: 16. 장소 의미·지도 관리 의 "4. 핵심 개념과 용어" 절(866자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area16-s10.md | draft | 자동 분리: 16. 장소 의미·지도 관리 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(732자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-09-30 | 16. 장소 의미·지도 관리 | 영역 심화: 3~11절 신규 작성(병원·가정·기타 적용 사례, 지도 버전·구역 집합·차선 폐쇄·장소 이름 모델, 책임 경계, 연결 14개 영역, 새 열린 질문 6건), 각주 16건 | run 2026-09-30-04
- 홈 최근 업데이트: 2026-09-30 — 16. 장소 의미·지도 관리: 영역 심화로 3~11절 신규 작성(병원·가정·기타 적용 사례, VDA 5050 지도 버전·구역 집합, IMDF 장소 이름·대체 이름, Open-RMF 차선 요청, 책임 경계, 새 열린 질문 6건)
- 대분류 최근 업데이트: 2026-09-30 — 16. 장소 의미·지도 관리: 영역 심화로 3~11절 신규 작성(적용 사례 3건, 대표 접근법·표준 7종, 책임 경계, 연결 14개 영역, 열린 질문 9건)
- 세부영역 최근 업데이트: 2026-09-30 — 16. 장소 의미·지도 관리: 영역 심화로 3~11절 신규 작성, 13절 각주 16건

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 지도 버전 | Map Version (VDA 5050 mapId / mapVersion) | 같은 작업 공간 구역을 가리키는 지도 식별자(mapId)에 붙는 갱신 표시로, VDA 5050 3.0.0 에서는 관제가 내려받게 한 여러 버전 가운데 같은 mapId 에서 한 버전만 활성화해 로봇이 쓰게 한다. | 16, 15, 57 | ref-031 |
| new | 대체 이름 | Alternative Name (IMDF alt_name) | IMDF 에서 공간·물체·서비스를 가리키는 동의어나 다른 표현으로, 기준 이름(name)과 별도로 색인·질의·검색에 쓰인다. | 16, 12 | ref-1027, ref-1026 |
| new | 의미 지도 | Semantic Map | 기하 지도 위에 방·구역·물체의 이름과 용도 같은 높은 수준의 정보를 얹어 로봇과 사람이 함께 쓰는 공간 표현이다. | 16, 45, 65 | ref-1036 |
| new | 3차원 장면 그래프 | 3D Scene Graph | 물체·장소·방·건물 같은 추상화 층을 노드와 관계로 묶어 환경을 여러 해상도로 표현하는 계층형 공간 그래프다. | 16, 45 | ref-347 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-046 | VDMA (Intralogistics-2X-LIF GitHub) | Layout-Interchange-Format — Repository for the Layout Interchange Format (LIF) | 표준 | medium | https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format |
| ref-1026 | Apple (Apple Business Register) | Unit - Indoor Mapping Data Format | 표준 | high | https://register.apple.com/resources/imdf/types/unit |
| ref-1027 | Apple (Apple Business Register) | Glossary - Indoor Mapping Data Format | 표준 | high | https://register.apple.com/resources/imdf/glossary |
| ref-1028 | Open Geospatial Consortium (OGC) | Indoor Mapping Data Format (1.0.0) — OGC Community Standard 20-094 | 표준 | high | https://docs.ogc.org/cs/20-094/index.html |
| ref-569 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_fleet_msgs/msg/LaneRequest.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg |
| ref-347 | Hughes, N., Chang, Y., Hu, S., Talak, R., Abdulhai, R., Strader, J., & Carlone, L. (arXiv 2305.07154, IJRR 투고본) | Foundations of Spatial Perception for Robotics: Hierarchical Representations and Real-time Systems | 논문 | medium | https://arxiv.org/abs/2305.07154 |
| ref-1031 | Feng, D., Li, C., Zhang, Y., Yu, C., & Schwertfeger, S. (arXiv) | osmAG: Hierarchical Semantic Topometric Area Graph Maps in the OSM Format for Mobile Robotics | 논문 | medium | https://arxiv.org/abs/2309.04791 |
| ref-1032 | Xie, F., Schwertfeger, S., & Blum, H. (RA-L 2026 채택, arXiv) | osmAG-LLM: Zero-Shot Open-Vocabulary Object Navigation via Semantic Maps and Large Language Models Reasoning | 논문 | medium | https://arxiv.org/abs/2507.12753 |
| ref-1033 | IEEE Standards Association (IEEE RAS) | IEEE 1873-2015 — IEEE Standard for Robot Map Data Representation for Navigation | 표준 | medium | https://standards.ieee.org/standard/1873-2015.html |
| ref-956 | 지디넷코리아 | 네이버 제2사옥, 로봇 친화형 건축물 인증 획득 | 기사 | low | https://zdnet.co.kr/view/?no=20220411142336 |
| ref-1035 | 국토지리정보원 | 실내공간정보 | 정부·연구기관 | high | https://www.ngii.go.kr/kor/content.do?sq=324 |
| ref-1036 | Narayana, M., Kolling, A., Nardelli, L., & Fong, P. (IROS 2020) | Lifelong update of semantic maps in dynamic environments | 논문 | medium | https://arxiv.org/abs/2010.08846 |
| ref-1037 | Stefanini, E., Ciancolini, E., Settimi, A., & Pallottino, L. (Sensors 23(13):6066) | Safe and Robust Map Updating for Long-Term Operations in Dynamic Environments | 논문 | high | https://pmc.ncbi.nlm.nih.gov/articles/PMC10346461/ |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 출처 충돌: LIF 의 판·날짜가 저장소 README 기준 1.0.0(2023-09)과 VDA 5050 3.0.0 이 인용한 VDMA 2024-03 으로 다르다. 어느 쪽이 현행이며 두 날짜는 같은 판을 가리키는가? | 16, 21 | 열림 | — |
| new | — | 제조사마다 다른 지도 버전(VDA 5050 mapVersion, 제조사 지도 파일)이 바뀔 때 ROP 의 장소 목록에 있는 이름·좌표 대응을 자동으로 옮기고 검수하는 방법이나 산업 현장 사례가 있는가? | 16, 15 | 열림 | — |
| new | — | IEEE 1873-2015 가 2026-03 비활성 보류 상태가 된 뒤 로봇 지도 데이터 교환 표준을 잇는 IEEE·ISO 작업이 있는가? | 16, 21 | 열림 | — |
| new | — | 공사·청소·감염 관리 같은 임시 통제 구역을 누가 선언·승인하고 언제 해제하는지, VDA 5050 구역 집합이나 Open-RMF 차선 폐쇄를 쓰는 운영 절차를 공개한 병원·상업 시설 사례가 있는가? | 16, 40, 63 | 열림 | — |
| new | — | IMDF·IndoorGML 같은 실내 지도 표준의 장소 이름·대체 이름을 로봇 작업 목적지나 대화형 지시의 장소 해석에 직접 쓰는 로봇 관제 제품이나 연구가 있는가? | 16, 12 | 열림 | — |
| new | — | 국토지리정보원 실내공간정보(지하철·철도역사 등)를 로봇 운영 지도나 장소 목록의 출발점으로 쓴 국내 사례가 있는가? | 16, 67 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 병원 | 작업 대상 | docs/categories/space-and-map-model/place-semantics-and-map-management.md#5-적용-사례-현장-유형-명시 | 16. 장소 의미·지도 관리 |
| 병원 | 수행 자원 | docs/categories/space-and-map-model/place-semantics-and-map-management.md#5-적용-사례-현장-유형-명시 | 16. 장소 의미·지도 관리 |
| 가정 | 작업 대상 | docs/categories/space-and-map-model/place-semantics-and-map-management.md#5-적용-사례-현장-유형-명시 | 16. 장소 의미·지도 관리 |
| 가정 | 수행 자원 | docs/categories/space-and-map-model/place-semantics-and-map-management.md#5-적용-사례-현장-유형-명시 | 16. 장소 의미·지도 관리 |
| 가정 | 제약 | docs/categories/space-and-map-model/place-semantics-and-map-management.md#5-적용-사례-현장-유형-명시 | 16. 장소 의미·지도 관리 |
| 가정 | 예외·성과 | docs/categories/space-and-map-model/place-semantics-and-map-management.md#5-적용-사례-현장-유형-명시 | 16. 장소 의미·지도 관리 |
| 기타 | 수행 자원 | docs/categories/space-and-map-model/place-semantics-and-map-management.md#5-적용-사례-현장-유형-명시 | 16. 장소 의미·지도 관리 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| IEEE 1873-2015 Robot Map Data Representation for Navigation | 표준 | IEEE Standards Association (IEEE RAS) | 16, 15, 21 | ref-1033 | https://standards.ieee.org/standard/1873-2015.html |
| osmAG (OSM 형식 계층형 위상·거리 의미 지도) | 프레임워크 | Feng, D. 외 (arXiv) | 16, 15 | ref-1031 | https://arxiv.org/abs/2309.04791 |
| Open-RMF 차선 요청 메시지(rmf_fleet_msgs LaneRequest) | 오픈소스 | Open Robotics (open-rmf) | 16, 27 | ref-569 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg |

## 추가 조사 요청

- 6·7절: LIF 스키마 필드(layoutVersion·stationName 등)를 스키마 원문으로 확인해야 LIF 가 장소 이름·버전을 어떻게 표현하는지 쓸 수 있다(README 에 필드 없음).
- 5절: 물류창고·제조 공장·상업 시설의 실제 운영 현장에서 지도 버전·장소 이름을 관리한 공개 사례가 필요하다(이번 브리프에는 물류창고 근거가 모의 실험뿐).
- 5절: 병원·가정·기타 사례의 시작 조건·완료·인계·제약·예외·성과 근거가 없어 '미확인'으로 두었다. 타르투 대학병원 논문 본문과 청소 로봇 의미 지도 논문 본문에서 해당 항목을 확인해야 한다.
- 6절: Nav2 금지 구역·속도 필터(costmap filter)와 MiR 지도 편집기(구역·위치 구성 요소)의 공식 문서를 열어 제조사·오픈소스 쪽 임시 통제 구역 방식을 보강해야 한다(이번 실행에서 열지 못함).
- 8절: 장소 의미를 지도 변화에 맞춰 유지하는 연구 분야 전반의 흐름(어느 계열이 주류인지)을 말하려면 서베이 논문 같은 근거가 필요하다. 이번에는 브리프 자료 범위로 한정해 썼다.
- 11절 oq-193: 건설 현장 점검 로봇 지도–BIM 동기화 주기의 근거가 여전히 없다.
- 13절: ref-031·ref-079·ref-869 의 참고문헌 페이지 '각주 형식' 줄이 입력에 없어 브리프 출처 필드로 각주를 만들었다. 기존 줄과 다르면 퍼블리셔가 맞춰 주어야 한다. 또 ref-046 는 기존 ref-046(LIF README)과 URL 이 같으므로 병합 여부 확인이 필요하다.

## 이행한 수정 지시

- f1 기준일 명시 — 3·4·6·7절에서 VDA 5050 을 'VDA 5050 3.0.0(공식 저장소 main)'으로 적고 확인일 2026-09-30 을 함께 두었다.
- f2 문구 수정 — 6절 '지도 버전의 배포와 활성화'에서 '명세는 지도가 사용 중이면 deleteMap 이 실패(FAILED)할 수 있다는 예를 든다'로 고쳤다.
- f3 용어·나열 수정 — 4·6절에서 '구역 집합'(용어집 zone-set 링크)으로 통일하고 구역 유형 나열에 양방향(BIDIRECTED)을 더했다.
- f4·f5 LIF 날짜 — 7절 LIF 행에 'README 기준 1.0.0(2023-09)'과 'VDA 5050 3.0.0 이 인용한 VDMA 2024-03'을 함께 제시하고, 11절에 '출처 충돌' 새 질문(관련 영역 16·21, 각주 ref-046·ref-031)을 두고 open_question_updates 에 냈다.
- f6 화장실 제외 — 6절 IMDF Unit 분류 나열을 '승강기·에스컬레이터·계단·경사로·방·비공개 구역 등'으로 쓰고 화장실을 뺐다.
- f10 분리 — 6절에서 LaneRequest 필드 구성(fleet_name·open_lanes·close_lanes)만 [사실]로 쓰고, 운영 중 차선을 닫거나 여는 쓰임은 설명 주석이 없다는 점을 밝혀 [추정]으로 분리했다(7절 표도 필드 구성만 [사실]).
- f13 발행일·범위 — ref-1037 각주·reference_updates 발행일을 2023-06-30 으로 고치고, 6·8절에서 '연계 대상:'으로 시작하는 짧은 서술로 다뤘다.
- f14 출처 표기 — ref-347 각주·8절·4절 표기를 'arXiv 2305.07154, 2023-05(IJRR 투고본, 초록 기준)'로 맞추고, Hydra 센서 기반 구축 부분은 6·8절에서 연계 대상으로 표시했다.
- f19 활용처 — 8절 국토지리정보원 항목의 활용처를 '공공분야(철도보안시스템, 시설물관리)·민간분야(실내 내비게이션, 메타버스, 좌석안내서비스)'로 바꾸고 안전·소방을 뺐다.
- f12 경계 — 5절 가정 사례 표와 서술, 6절에서 평생 의미 지도를 '로봇 제품 쪽 기능'으로 서술하고, ROP 역할은 9절의 [추정](f22·f23) 범위로만 다룬다고 밝혔다.
- f16·f24 연결 — 10절에 44. 로봇 기반 모델·언어 모델 계획(ref-1032)을 더하고 45·8·12번 연결을 유지했으며 프런트매터 related_areas 에 44 를 넣었다.
- 5절 사례 범위 — 병원(f11)·가정(f12)·기타(f18) 세 현장 유형만 쓰고 물류창고 사례를 만들지 않았으며, 근거 없는 칸(시작 조건·완료·인계 등)은 '미확인'으로 두었다.
- f18 표기 — 5절 기타 사례를 '지디넷코리아(2022-04-11)에 따르면' 형식으로 쓰고 용어집 '로봇 친화형 건축물 인증'을 링크했다.
- 각주 — ref-031·ref-079·ref-869 는 기존 id 를 재사용하고(참고문헌 페이지 줄은 입력에 없어 브리프 출처 필드로 같은 형식을 구성, additional_research_requests 에 확인 요청), reference_updates 에는 신규 ref-046~ref-1037 만 넣었다.
- 분량 초과 자동 분리: 16. 장소 의미·지도 관리 본문 10,449자 > 기준 4,000자 → 6개 절을 주제 페이지로 옮김, 남은 본문 3,485자
- 2차: standards_updates 의 osmAG 항목 org 를 'Feng, D. 외 (ShanghaiTech, arXiv)'에서 'Feng, D. 외 (arXiv)'로 고쳐 브리프에 없는 소속 기관 표기를 뺐다.
- 2차: 8절 첫 문장을 세부영역 페이지와 분리 주제 페이지 docs/topics/2026/2026-09-30-area16-s8.md 의 1절·3절에서 '이번에 확인한 연구는 로봇 쪽 의미 지도(Narayana 외)와 계층형 표현(Hughes 외의 3차원 장면 그래프, Feng 외의 osmAG)에 속한다. [추정][^ref-1036][^ref-347][^ref-1031]'로 바꿔 브리프 자료 범위로 한정했고, 세부영역 페이지 13절에 ref-1031 각주 정의를 더했다.
