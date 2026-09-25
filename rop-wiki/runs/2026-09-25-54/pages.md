# 스토리텔러 산출 2026-09-25-54

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/floorplan-recognition/stage-3-implementation-hypothesis.md | draft | q3-01 답함(처리 흐름 네 단계·사람 검토 네 지점, 결론은 추정), 2~9절 갱신, 후속 질문 2건(q3-07·q3-08). 2차 수정: H1 아래 단계 상태 줄 갱신(진행 중 · 열린 7 · 답함 1), 6절 첫 행 검증 판정 '충족 · 전환 미승인', 전환 줄에 핵심 구성 요소 추가. 머리 영역 수정 때문에 페이지 전문으로 보냄 |
| update | docs/ideas/floorplan-recognition.md | draft | 5. 구현 가설 절 첫 작성: 처리 흐름과 사람 검토 지점(q3-01, 실행 2026-09-25-54, 추정 중심), 핵심 구성 요소·다른 아이디어와의 연결은 아직 조사되지 않음(2차 재실행에서 변경 없음) |
| update | docs/tracks/floorplan-recognition/index.md | draft | 6. 살아있는 산출물 링크: 아이디어 5절 첫 반영(q3-01), 백로그 후속 질문 15건·q3-01 답함, 스키마 초안 변경 없음 기록. 상태 줄은 입력 값 그대로(현재 단계 단계 1 유지, 마지막 트랙 실행 2026-09-25)(2차 재실행에서 변경 없음) |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 건축 도면 자동 인식 단계 3 | q3-01 답함(도면 처리 흐름 네 단계와 사람 검토 네 지점, 추정), 아이디어 3 5절 첫 반영, 후속 질문 2건, 온톨로지 변경 없음 | run 2026-09-25-54
- 홈 최근 업데이트: 2026-09-25 — 건축 도면 자동 인식 단계 3: q3-01 답함(인식 → 벡터화 → 공간 그래프 → 온톨로지 적재 흐름의 입출력과 사람 검토 지점, 추정 중심), 후속 질문 2건
- 대분류 최근 업데이트: 2026-09-25 — 6. 지도·공간·위치 모델: 건축 도면 자동 인식 트랙 단계 3에서 도면 처리 흐름과 사람 검토 지점을 정리(q3-01), 6절 반영 제안
- 세부영역 최근 업데이트: 2026-09-25 — 6. 지도·공간·위치 모델: 트랙 단계 3(q3-01)이 도면 처리 흐름의 단계 구분과 장소 이름·운영 요소의 사람 확인 지점을 6. 대표 접근법과 기술 절에 반영하도록 제안

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 사람 참여 루프 | Human-in-the-Loop (HITL) | 자동 처리 결과 가운데 불확실하거나 중요한 부분을 사람이 확인·보정하고 그 판단을 다시 처리 흐름에 넣는 설계 방식이다. | 6, 27, 18 | ref-691, ref-690 |
| new | 정보 전달 명세 | Information Delivery Specification (IDS) | buildingSMART 가 정한, IFC 모델이 갖춰야 할 정보 요구사항을 컴퓨터가 해석할 수 있게 적는 XML 기반 표준이다. | 28, 6 | ref-697 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-689 | Oraskari, J. (jyrkioraskari GitHub) | IFCtoLBD — README (IFCtoLBD converts IFC (Industry Foundation Classes STEP formatted files into the Linked Building Data ontologies) | 오픈소스 문서 | high | https://github.com/jyrkioraskari/IFCtoLBD |
| ref-690 | Ratul, A. K., Acharjee, S., Park, S., & Sakib, M. N. | Sketch2BIM: A Multi-Agent Human-AI Collaborative Pipeline to Convert Hand-Drawn Floor Plans to 3D BIM | 논문 | medium | https://arxiv.org/abs/2510.20838 |
| ref-691 | Jakubik, J., Hemmer, P., Vössing, M., Blumenstiel, B., Bartos, A., & Mohr, K. | Designing a Human-in-the-Loop System for Object Detection in Floor Plans | 논문 | medium | https://ojs.aaai.org/index.php/AAAI/article/view/21522 |
| ref-692 | W3C RDF Data Shapes Working Group | Shapes Constraint Language (SHACL) (W3C data-shapes 저장소 편집자 초안으로 확인, 권고안(2017) 본문과 문구가 다를 수 있음) | 표준 | high | https://www.w3.org/TR/shacl/ |
| ref-693 | 대한건축학회논문집 40(1), 297-303(DOI 10.5659/JAIK.2024.40.1.297) 게재 논문 저자(미확인) | 딥러닝과 경로계획 기반의 주택 평면도 3D 모델링 방법 | 논문 | medium | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003047128 |
| ref-694 | Buildings(MDPI) 게재 논문 저자(Concordia University, 목록 미확인) | Ontology for BIM-Based Robotic Navigation and Inspection Tasks | 논문 | medium | https://www.mdpi.com/2075-5309/14/8/2274 |
| ref-695 | arXiv 2507.11770 저자(미확인) | Generating Actionable Robot Knowledge Bases by Combining 3D Scene Graphs with Robot Ontologies | 논문 | medium | https://arxiv.org/abs/2507.11770 |
| ref-696 | arXiv 2602.06507 저자(미확인) | FloorplanVLM: A Vision-Language Model for Floorplan Vectorization | 논문 | medium | https://arxiv.org/abs/2602.06507 |
| ref-697 | buildingSMART (buildingSMART/IDS GitHub) | IDS — README (Information Delivery Specification) | 표준 | medium | https://github.com/buildingSMART/IDS |
| ref-084 | Zhang, J. (jiajiezhang7 GitHub) | osmAG-from-cad — README (CAD-to-osmAG pipeline) | 오픈소스 문서 | high | https://github.com/jiajiezhang7/osmAG-from-cad |
| ref-070 | Hu, S. 외 | Raster-to-Graph — README (Raster-to-Graph: Floorplan Recognition via Autoregressive Graph Prediction with an Attention Transformer) | 오픈소스 문서 | high | https://github.com/SizheHu/Raster-to-Graph |
| ref-434 | ArchiAI Lab (ArchCAD-400K 프로젝트) | ArchCAD-400k: A Large-Scale CAD drawings Dataset and New Baseline for Panoptic Symbol Spotting — project page | 오픈소스 문서 | medium | https://archiai-lab.github.io/ArchCAD.github.io/ |
| ref-441 | Open Robotics (open-rmf) | rmf_traffic_editor — README | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_traffic_editor |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/traffic-editor.html |
| ref-225 | Diakité, A. A., Díaz-Vilariño, L., Biljecki, F., Isikdag, Ü., Simmons, S., Li, K., & Zlatanova, S. | IFC2INDOORGML: An Open-Source Tool for Generating IndoorGML from IFC | 논문 | medium | https://isprs-archives.copernicus.org/articles/XLIII-B4-2022/295/2022/ |
| ref-077 | DoorDet 저자(arXiv 2508.07714) | DoorDet: Semi-Automated Multi-Class Door Detection Dataset via Object Detection and Large Language Models | 논문 | medium | https://arxiv.org/abs/2508.07714 |

## 열린 질문 갱신

- 없음

## 흐름 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| IFCtoLBD (IFC → 링크드 빌딩 데이터 변환기, 판 2.54.0) | 오픈소스 | Oraskari, J. (jyrkioraskari GitHub) | 28, 6 | ref-689 | https://github.com/jyrkioraskari/IFCtoLBD |
| SHACL (Shapes Constraint Language) | 표준 | W3C | 28, 6, 5 | ref-692 | https://www.w3.org/TR/shacl/ |
| IDS (Information Delivery Specification) | 표준 | buildingSMART | 28, 6 | ref-697 | https://github.com/buildingSMART/IDS |

## 추가 조사 요청

- 단계 3 완료 조건(아이디어 5절 핵심 구성 요소): 공간 그래프 노드·엣지 단위(q3-02)와 능력 대조(q3-03), 시뮬레이션 초기값(q3-04)에 대한 근거 finding이 필요하다 — 이번 브리프에는 없어 5절 핵심 구성 요소를 '아직 조사되지 않음'으로 두었다.
- 단계 3 완료 조건(실험 계획): 공개 DXF·IFC 도면에 osmAG-from-cad·IFCtoLBD 같은 공개 도구를 적용해 사람 검토 지점별 수정량을 재는 실험을 제안하려면 대상 공개 도면 샘플과 측정 항목의 근거가 필요하다.
- 공간 그래프 스키마 초안의 단계 3 근거 갱신: 처리 흐름에서 공간 노드에 이름 출처·검토 상태 속성을 둘지 뒷받침하는 finding이 필요하다(이번 실행은 근거 없는 설계 선택이라 반영하지 않음).
- ref-693(대한건축학회논문집 40(1), 2024)의 저자 목록과 세부 기법, ref-694·ref-695·ref-696 저자 목록 확인이 필요하다.
- SHACL 권고안(/TR/shacl/, 2017) 본문으로 정의 문구와 검증 보고서 구조를 재확인하면 편집자 초안 표기를 뗄 수 있다.

## 이행한 수정 지시

- f9 문장 분리 — 단계 페이지 3절 '공간 그래프 생성'에서 'ifc2indoorgml은 IFC 데이터에서 IndoorGML 모델을 자동 생성하는 오픈소스 도구다'만 [사실][^ref-225]로, BIM 입력이 인식·벡터화를 건너뛰는 경로는 이 위키의 해석으로 [추정][^ref-225]을 붙여 따로 썼다.
- f13 '(IROS 2025)' → '(IROS 2025 제출)' — 단계 페이지 3절 본문과 ref-695 참고문헌 요약에 반영했다.
- f14 ifcOWL 구절 — '가구·HVAC 같은 건물 개념을 ifcOWL 에서 가져온' 구절을 빼고 '(ifcOWL 개념 재사용 여부 미확인)'으로 바꿨다(단계 페이지 3절, ref-694 요약).
- f15 세부 기법명 — '인스턴스 정규화·화이트닝'을 빼고 '(세부 기법 미확인)'으로 표기했으며, ref-693 각주와 reference_updates 의 기관 자리를 '대한건축학회논문집 40(1), 297-303(DOI 10.5659/JAIK.2024.40.1.297) 게재 논문 저자(미확인)'로 보강했다.
- f11 편집자 초안 명시 — 단계 페이지 3절 본문과 아이디어 페이지 근거 사례에 'W3C data-shapes 저장소 편집자 초안으로 확인, 권고안(2017) 본문과 문구가 다를 수 있음'을 적고, 두 페이지의 ref-692 각주 제목과 reference_updates 에도 같은 표기를 넣었다.
- f3·f5·f6(·f4) 수치 — 외벽 IoU 92.52%, 벽 검출 약 83%, 50배 비용 절감 문장에 '저자 보고, 단일 출처'를 문장 안에 병기했다(단계 페이지 3절, 아이디어 페이지 5절). f5 문장은 수치가 없어 병기 대상이 없다.
- 원문 미열람 표기 — 단계 페이지 8절의 ref-079·ref-077·ref-225·ref-690·ref-691·ref-693·ref-694·ref-695·ref-696 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 의 해당 항목에 source_unopened: true 를 넣었다. 아이디어 페이지에서는 새로 정의한 ref-690·ref-691·ref-695·ref-696 에 표기했고, 기존 정의만 있는 ref-079 는 이 페이지 5절에서 인용하지 않았다(기존 ref-077·ref-225 정의는 이미 원문 미열람 표기).
- 중복 서술 회피 — f1·f2·f4·f7·f8·f9 는 새 각주를 만들지 않고 기존 ref-084·ref-070·ref-434·ref-077·ref-441·ref-225 를 재사용해 단계 페이지 3절의 처리 흐름 맥락으로만 한두 문장씩 요약했다. f7 은 절차 부분만 [사실]로 썼다.
- 단계 3 페이지 q3-01 — 2절 표를 '답함'(답한 실행 id 2026-09-25-54, 답 위치 #q3-01)으로 바꾸고, 3절에 '### q3-01 … {#q3-01}' 소제목을 두었으며, 결론 문장(f16·f17·f18)은 3절과 4절 모두 [추정]으로 유지했다.
- 중복 질문 — 가설 판정 지표 질문은 backlog_updates 에 넣지 않았고, 단계 페이지 5절 표 아래에 q5-02 와 같은 질문이라 등록하지 않았다는 메모만 남겼다(단계 5 페이지는 고치지 않음).
- 단계 전환 미승인 — track_updates.stage_transition 을 넣지 않고, 6절 아래 줄을 지시 문구 그대로 '다음 단계로 전환: 아니오(완료 조건 미충족: 아이디어 5절 다른 아이디어와의 연결·스키마 단계 3 근거 갱신·실험 계획 없음; 막힌 질문 q3-02·q3-03·q3-04·q3-05·q3-06)'로, 6절 표 검증 판정 칸을 '미충족 · 미승인'으로 썼다. 상태 줄의 완료 조건은 입력값 '미충족'이 유지되며, 트랙 개요의 현재 단계(단계 1. 선행 연구·제품 사례 조사)는 바꾸지 않았다.
- 아이디어 페이지 5절 — '처리 흐름과 사람 검토 지점' 소절에 f16·f17·f18 을 [추정]으로, 근거 사례 f1·f2·f3·f4·f5·f6·f7·f8·f10·f11 을 각 태그([사실])대로 싣고, '다른 아이디어와의 연결'과 '핵심 구성 요소'는 '아직 조사되지 않음'으로 두었다.
- IDS 용어집 정의 — glossary_updates 의 '정보 전달 명세(IDS)' 정의와 설명에 판 번호를 쓰지 않고 판·검사 범위 미확인만 적었다.
- 2차: 단계 3 페이지 H1 아래 상태 줄 — 절 패치로는 머리 영역을 고칠 수 없어 단계 3 페이지를 페이지 전문(content)으로 보내고, 상태 줄을 '> 단계 상태: 진행 중 · 열린 질문: 7건 · 답한 질문: 1건 · 완료 조건: 미충족 · 마지막 실행: 2026-09-25'로 고쳤다(2절 표의 열림 7·답함 1과 일치).
- 2차: 6절 표 첫 행 검증 판정 — '처리 흐름이 아이디어 3. 건축 도면 자동 인식의 5. 구현 가설 절에 실림' 행의 검증 판정 칸을 '미충족 · 미승인'에서 '충족 · 전환 미승인'으로 고쳤다. 나머지 행은 '미충족 · 미승인' 그대로다.
- 2차: 6절 전환 줄 — '다음 단계로 전환: 아니오(완료 조건 미충족: 아이디어 5절 핵심 구성 요소·다른 아이디어와의 연결, 스키마 단계 3 근거 갱신, 실험 계획 없음; 막힌 질문 q3-02·q3-03·q3-04·q3-05·q3-06)'로 고쳐 빠졌던 핵심 구성 요소를 넣었다.

## 트랙 갱신

- 단계 페이지: docs/tracks/floorplan-recognition/stage-3-implementation-hypothesis.md
- 온톨로지 초안 버전: 0.6
- 트랙 로그 항목: 답한 질문: q3-01(근거 f1~f18, 결론 f16·f17·f18 은 [추정]) / 새 질문: q3-07(f11), q3-08(f16); 가설 판정 지표 질문은 q5-02 와 중복으로 등록하지 않음 / 온톨로지 변경: 없음(v0.6 유지 — q3-01 은 처리 흐름 질문이며 공간 그래프 개념·관계를 새로 뒷받침하는 finding 없음) / 완료 조건 평가: 미충족(충족: 아이디어 3 5절의 처리 흐름; 부족: 아이디어 3 5절의 핵심 구성 요소·다른 아이디어와의 연결, 공간 그래프 스키마 초안의 단계 3 근거 갱신, 실험 계획; 막힌 질문 q3-02·q3-03·q3-04·q3-05·q3-06) / 세부영역 반영 제안: 6. 지도·공간·위치 모델 1건, 27. AI·학습·적응과 모델 운영 2건, 28. 표준·상호운용성·다사업자 거버넌스 1건, 21. 온보딩·설정·현장 시운전 1건, 5. 로봇 능력·작업 온톨로지 1건(총 6건) / 다음 실행 제안: q3-02(공간 그래프 단위), 이어서 q3-07·q3-08 / 비고: CLI 지정 질문 실행이라 트랙 현재 단계(단계 1)는 바꾸지 않음. 단계 3 페이지 상태 줄은 '진행 중 · 열린 질문 7건 · 답한 질문 1건 · 완료 조건 미충족 · 마지막 실행 2026-09-25'로 갱신(2차 수정).
- 개요 진행 현황: 단계 3 진행 중(CLI 지정 질문, 트랙 현재 단계는 단계 1 유지) — 열린 질문 7, 답함 1, 완료 조건 미충족

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q3-01 | 답함 | docs/tracks/floorplan-recognition/stage-3-implementation-hypothesis.md#q3-01 | — | — | — |
| q3-07 | 열림 | — | 공간 그래프를 온톨로지에 적재하기 전 검증 관문으로 쓸 SHACL 형상(예: 모든 문은 두 공간 노드를 잇는다, 모든 공간 노드는 한 층에 속한다, 충전 위치는 접근 지점을 가진다)은 무엇이며, 위반 보고서를 누가 어떻게 처리하는가? (q3-01 에서 파생) | 3 | f11 |
| q3-08 | 열림 | — | 여러 인식 방법(구조 그래프 예측, 시각-언어 모델 JSON 출력, CAD 레이어 기반 분할, IFC 직접 변환)을 바꿔 끼울 수 있게 하려면 인식·벡터화 단계의 중간 산출물 형식을 무엇으로 정해야 하는가? (q3-01 에서 파생) | 3 | f16 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 6 | 6. 대표 접근법과 기술 | 도면 처리 흐름을 입력 정리 → 인식·벡터화 → 공간 그래프 생성 → 온톨로지 적재로 나누는 이 위키의 종합([추정], f16)과 BIM 입력의 직접 변환 경로(ifc2indoorgml, f9), 사람 검토 네 지점([추정], f17), 업무 장소 이름과 공간 노드의 연결을 공간 그래프 생성 뒤 사람 확인에 두는 방향([추정], f18, osmAG 문자 이름 기본 꺼짐 f1, traffic-editor 경유점 주석 f8). 근거 실행 2026-09-25-54. |
| 27 | 6. 대표 접근법과 기술 | 교차 규칙(도면 해석은 6. 지도·공간·위치 모델에 적용)에 따라 시각-언어 모델 벡터화(FloorplanVLM, 외벽 IoU 92.52% 저자 보고 단일 출처, f3), 불확실성 기반 사람 참여 루프(Jakubik 외 2022, f5), LLM 다중 에이전트와 사람 피드백·스키마 검증(Sketch2BIM, f6), 검출기·LLM·사람 검수 반자동 절차(DoorDet, f7)를 6. 지도·공간·위치 모델 페이지와 양쪽에 연결. |
| 27 | 8. 대표 연구와 자료 | FloorplanVLM(ref-696), Jakubik 외 AAAI 2022(ref-691), Sketch2BIM(ref-690), DoorDet(ref-077)를 도면 해석 연구로 등재(모두 원문 미열람, 수치는 저자 보고). |
| 28 | 7. 관련 표준·프레임워크·오픈소스 | IFC → 링크드 빌딩 데이터 RDF 변환기 IFCtoLBD(판 2.54.0, SHACL 검증 지원, f10), 적재 전 검증 언어 W3C SHACL(2017 권고안, 편집자 초안으로 확인, f11), IFC 정보 요구 명세 buildingSMART IDS(XML 기반, 판 미확인, f12). |
| 21 | 6. 대표 접근법과 기술 | 시운전 전 도면 처리에서 사람이 입력·확인하는 항목: 축척·좌표 기준점 파라미터(osmAG-from-cad, f1), 운영 요소·경유점 주석(traffic-editor, f8), 적재 전 검증 보고서 확인(SHACL, f11) — 네 지점 구분은 [추정](f17). |
| 5 | 8. 대표 연구와 자료 | 건물·장면 정보를 로봇 온톨로지·지식 그래프에 적재한 연구: OBRNIT(로봇·건물·주행 작업·점검 작업 네 개념 묶음, ifcOWL 재사용 여부 미확인, f14), 장면 그래프를 USD로 통일하고 사람이 온톨로지 개념으로 라벨을 붙이는 흐름(arXiv 2507.11770, IROS 2025 제출, f13). 모두 원문 미열람. |
