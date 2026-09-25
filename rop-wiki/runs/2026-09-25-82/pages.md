# 스토리텔러 산출 2026-09-25-82

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/floorplan-recognition/stage-5-verification-and-hypotheses.md | draft | q5-02 답함(3절 소제목 신설, 측정 구성 추정 중심), 후속 질문 q5-12·q5-13, 4·5·6·7·8·9절 갱신 |
| update | docs/ideas/floorplan-recognition.md | draft | 6절 전체 교체: '검증 절차: 현장 모델링 시간 단축 측정' 소절 추가(q5-02, 추정 중심), 절 첫 문단과 평가 지표 소절 끝의 미조사 문장을 새 소절과 맞춤 |
| update | docs/tracks/floorplan-recognition/index.md | draft | 6절에 실행 2026-09-25-82(단계 5, q5-02) 진행 문단 추가 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 건축 도면 자동 인식 단계 5 | q5-02 답함(현장 모델링 시간 단축을 시간·수정·결과 품질 세 축으로 재는 측정 구성, 추정 중심), 후속 질문 q5-12·q5-13, q5-11 폐기, 1차 조건부 승인 수정 15건·2차 수정 1건 이행 | run 2026-09-25-82
- 홈 최근 업데이트: 2026-09-25 — 건축 도면 자동 인식 단계 5. 검증 방법과 가설 판정: q5-02 답함 — 현장 모델링 시간 단축을 단계별 시간·요소별 수정 횟수·보정 후 결과 품질로 함께 재는 측정 구성(추정 중심)
- 대분류 최근 업데이트: 2026-09-25 — 6. 지도·공간·위치 모델(건축 도면 자동 인식 트랙 단계 5): 도면 인식 결과의 사람 수정 노력 지표와 현장 모델링 시간 단축 측정 구성(q5-02) 추가
- 세부영역 최근 업데이트: 2026-09-25 — 6. 지도·공간·위치 모델: 건축 도면 자동 인식 트랙 단계 5 에서 도면 해석 결과를 사람 수정 노력(편집 비용·클릭 수)과 단계별 시간으로 재는 방법을 정리했고, '6. 대표 접근법과 기술' 반영을 제안했다(실행 2026-09-25-82)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 편집 비용 | Edit Cost | 자동 생성 결과를 정답 수준으로 고치는 데 필요한 사람의 편집 연산(추가·삭제·이동 등)을 요소 유형별로 세거나 가중해 합한 수정 노력 지표다. | 6, 23, 27 | ref-748 |
| new | 클릭 수 지표 | Number of Clicks (NoC) | 대화형 주석·분할에서 목표 정확도(예: IoU 90%)에 이르거나 예측을 고치는 데 필요한 평균 사용자 클릭 수로, 사람 노력을 재는 지표다. | 23, 27 | ref-762, ref-750 |
| new | 키 입력 수준 모델 | Keystroke-Level Model (KLM) | 숙련 사용자가 오류 없이 과제를 수행하는 시간을 키 입력·포인팅·정신적 준비 같은 연산자 시간의 합으로 예측하는 GOMS 계열 모델이다. | 21, 23 | ref-757 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-748 | Zhang, H. (Independent Researcher, arXiv 2608.25608) | When Should a Network Emit Geometry, and When Should It Detect It? Readout, Reconciliation, and Representation in Floorplan Vectorization | 논문 | medium | https://arxiv.org/abs/2608.25608 |
| ref-749 | Opiela, M., & Hrehová, M. (Pavol Jozef Šafárik University, IPIN-WiP 2023, CEUR-WS Vol-3581) | Map Model Extraction from Image Floor Plans | 논문 | medium | https://ceur-ws.org/Vol-3581/194_WiP.pdf |
| ref-750 | Acuna, D., Ling, H., Kar, A., & Fidler, S. (CVPR 2018) | Efficient Interactive Annotation of Segmentation Datasets with Polygon-RNN++ | 논문 | medium | https://arxiv.org/abs/1803.09693 |
| ref-751 | Castrejón, L., Kundu, K., Urtasun, R., & Fidler, S. (CVPR 2017) | Annotating Object Instances with a Polygon-RNN | 논문 | medium | https://arxiv.org/abs/1704.05548 |
| ref-752 | Song, W. 외 (BMVC 2023, arXiv 2311.18166) | A-Scan2BIM: Assistive Scan to Building Information Modeling | 논문 | medium | https://arxiv.org/abs/2311.18166 |
| ref-753 | Song, W. (weiliansong/A-Scan2BIM GitHub) | A-Scan2BIM — README (Official implementation of the paper A-Scan2BIM: Assistive Scan to Building Information Modeling) | 오픈소스 문서 | medium | https://github.com/weiliansong/A-Scan2BIM |
| ref-754 | Snover, M., Dorr, B., Schwartz, R., Micciulla, L., & Makhoul, J. (AMTA 2006) | A Study of Translation Edit Rate with Targeted Human Annotation | 논문 | medium | https://aclanthology.org/2006.amta-papers.25/ |
| ref-755 | Koponen, M., Aziz, W., Ramos, L., & Specia, L. (AMTA 2012 WPTP) | Post-editing time as a measure of cognitive effort | 논문 | medium | https://aclanthology.org/2012.amta-wptp.2/ |
| ref-756 | Alvarez, S., Oliver, A., & Badia, T. (EAMT 2020) | Quantitative Analysis of Post-Editing Effort Indicators for NMT | 논문 | medium | https://aclanthology.org/2020.eamt-1.44.pdf |
| ref-757 | Kieras, D. (University of Michigan) | Using the Keystroke-Level Model to Estimate Execution Times | 논문 | low | https://www.cs.umd.edu/~golbeck/INST631/KSM.pdf |
| ref-758 | ScienceDirect 게재 논문 저자(미확인) | A structured review of virtual commissioning: simulation fidelity, industrial validation, and design-oriented decision-making | 논문 | medium | https://www.sciencedirect.com/science/article/pii/S2590123026038491 |
| ref-759 | 박준우, 김재홍, 김소현, 이지민, 최창순, 정광복, 이재욱(KIBIM Magazine 11(4), 53-62) | Scan-to-BIM 자동화 기술을 활용한 건축물 단위의 BIM 모델 생성 - 강원소방학교 BIM 모델링 실증을 중심으로 - | 논문 | medium | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002801297 |
| ref-760 | Journal of Asian Architecture and Building Engineering 게재 논문 저자(미확인) | Automated BIM generation using drawing recognition and line-text extraction | 논문 | medium | https://www.tandfonline.com/doi/full/10.1080/13467581.2020.1806071 |
| ref-761 | ResearchGate 게재 논문 저자(미확인) | Time-Benefit Analysis of Semiautomatic 3D Laser Scanning for BIM-based Facility Management | 논문 | low | https://www.researchgate.net/publication/381549957_Time-Benefit_Analysis_of_Semiautomatic_3D_Laser_Scanning_for_BIM-_based_Facility_Management |
| ref-762 | Forte, M., Price, B., Cohen, S., Xu, N., & Pitié, F. (arXiv 2003.07932) | Getting to 99% Accuracy in Interactive Segmentation | 논문 | medium | https://arxiv.org/abs/2003.07932 |
| ref-217 | Beinschob, P., Meyer, M., Reinke, C., Digani, V., Secchi, C., & Sabattini, L. | Semi-automated map creation for fast deployment of AGV fleets in modern logistics | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0921889015302724 |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 오픈소스 문서 | medium | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 국내에서 실내공간정보 구축이나 로봇 도입 시 지도·공용 자원 설정 공수(인·일)를 산정하는 품셈이나 공공 기준이 있는가? | 21, 4 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 출하 | 예외·성과 | docs/tracks/floorplan-recognition/stage-5-verification-and-hypotheses.md#q5-02 | 단계 5. 검증 방법과 가설 판정 |

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- pipeline 담당 요청: 단계 5 페이지 H1 아래 상태 줄과 트랙 개요 H1 아래 상태 줄은 H2 절 밖이라 patches 로 고칠 수 없어 이번에 갱신하지 못했다. 단계 5 상태 줄은 '단계 상태: 진행 중 · 열린 질문: 10건 · 답한 질문: 2건 · 완료 조건: 미충족 · 마지막 실행: 2026-09-25', 트랙 개요 상태 줄의 현재 단계는 '단계 5. 검증 방법과 가설 판정'이어야 한다.
- 3절 q5-02 수치 보강: 편집 비용 지표의 연산별 수치(ref-748), 평면도 주석 40분 대 5분(ref-749)과 도면→BIM 단계별 시간(ref-760)을 원문으로 확인해야 [사실]로 쓸 수 있다.
- 3절 q5-02 근거 보강: 도면·지도 보정 작업에서 편집 수와 실제 소요 시간의 상관을 잰 자료, 물류 로봇 설정 작업(공용 자원 등록·좌표 대응)의 수작업 대비 시간을 같은 조건으로 잰 연구나 국내 사례가 필요하다.
- 단계 5 완료 조건: 가설 판정표(q5-03)와 사용자에게 제안하는 실험 계획(q5-12 의 비교 실험 설계 포함)이 다음 실행에 필요하다.

## 이행한 수정 지시

- f2 강등 — 단계 5 페이지 3절 '수작업 대비 시간 비교 사례'와 아이디어 6절 근거에서 [추정]으로 쓰고 저자 보고·IPIN 2019 대회 지도 1건·자동 처리 시간 포함 여부 미확인·검증 재검색에서 수치 미재확인을 병기했다.
- f10 강등 — 8,500㎡·15분·약 1시간 수치를 모두 빼고 '준자동 BIM 생성이 모델링 시간을 줄인다고 저자가 보고했으나 단계별 시간 수치는 미확인'으로만 [추정] 표기해 단계 페이지와 아이디어 페이지에 썼다.
- f7 강등 — [추정]으로 쓰고 세 차원의 약한 상관은 EAMT 2020 논문 서론의 Krings(2001) 등 선행 문헌 인용으로, 논문 자체 결과는 사후 편집 시간과 키 입력 수의 높은 상관으로 구분했으며 각주·reference_updates 저자를 'Alvarez, S., Oliver, A., & Badia, T.'로 고쳤다.
- f15 전제 수정 — 약한 상관 서술(서론)과 높은 상관 결과가 출처에 함께 있음을 밝힌 뒤 '수정 횟수를 시간 대용치로만 쓰지 말고 함께 기록한다'로 단계 페이지와 아이디어 페이지에 [추정]으로 썼다.
- f14·f19 — 측정 구성 표와 근거 공백 문장에서 f2·f10 수치를 쓰지 않고 '입력 준비·자동 처리·보정 시간을 따로 보고한 사례'와 사례 이름만 들었다.
- f1 — 벽 삭제 약 3회·개구부 약 6회 수치를 본문에 쓰지 않았고 발행일을 2026-08(arXiv 2026-08 제출)로 적었다.
- f5 — 16개 장면·89시간 문장에는 ref-752 각주만 달고, ref-753 README 각주는 평가 항목(복원 지표·순서 지표·다음 벽 예측 정확도) 문장에만 붙였다.
- f8 — 'Card·Moran·Newell 1983' 연도를 빼고 'Kieras 해설 기준, 강의 사이트 게재본, 발행일 미확인'으로 적었으며 각주 발행일은 미확인으로 두었다.
- f12 — [의견] 문장을 '가상 시운전 연구 36건을 검토한 구조적 리뷰(2026) 저자들의 평가로는'으로 시작해 의견의 주체를 밝혔다.
- 각주 표기 — 이번에 쓴 각주 정의에서 ref-753 를 뺀 모든 출처(ref-748~ref-752, ref-754~ref-762, ref-217, ref-105)의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었으며 ref-753 는 표시 없이 두었다. 아이디어 페이지에 이미 정의된 ref-217·ref-105 각주는 중복 정의를 피하려고 새로 쓰지 않았다.
- 단계 5 페이지 — 3절에 '### q5-02 현장 모델링 시간 단축을 재는 기준 {#q5-02}' 소제목을 신설하고, 2절 q5-02 행을 답함·2026-09-25-82·[답](#q5-02)로 바꿨으며, 4절 남은 불확실성에 '물류 로봇 설정 작업을 같은 조건으로 잰 측정 사례 없음, 측정 구성은 이 위키의 종합'을 적었다.
- q5-11 — backlog_updates 에서 상태를 폐기로 바꾸고 단계 페이지 2절 표에는 넣지 않았으며 5절 아래와 9절 이력에 q5-09 중복 폐기를 적었다.
- 단계 5 페이지 6절 — 세 행의 검증 판정을 '미충족 · 미승인'으로 두고 첫 행 근거 칸에 '검증 절차 소절이 추정 중심으로 실림(실행 2026-09-25-82)'을 적었으며, 표 아래를 '다음 단계로 전환: 아니오(가설 판정표 q5-03·실험 계획 미작성, 막힌 질문 q5-03~q5-10과 새 질문 열림)'로 쓰고 stage_transition 은 넣지 않았다.
- 아이디어 6절 — '검증 절차: 현장 모델링 시간 단축 측정' 소절을 더해 f14~f17 을 [추정]으로 싣고, 기존 '측정 대상 후보: 반복 작업 목록' 소절은 앵커 링크로 이어 같은 문장을 반복하지 않았으며, PAN-Robots 비교 조건(q5-04)과 가설 판정(q5-03)은 미조사라고 적었다.
- 세부영역 반영 — 21. 온보딩·설정·현장 시운전, 23. 시험·형식 검증·벤치마크, 27. AI·학습·적응과 모델 운영(교차 규칙에 따른 6. 지도·공간·위치 모델 포함) 페이지는 고치지 않고 area_reflection_proposals 와 트랙 로그의 '세부영역 반영 제안'으로만 냈으며, 제안 문안에서 f2·f7·f10 은 [추정]으로 적었다.
- 2차: 아이디어 페이지 6. 검증 방법 — 패치 action 을 replace 로 바꿔 절 전체를 보냈고, 첫 문단 끝 문장을 ''검증 절차: 현장 모델링 시간 단축 측정' 소절은 단계 5의 q5-02 답(실행 2026-09-25-82)의 요약이다'로 고쳤으며, '평가 지표' 소절 끝 문장에서 '검증 절차(현장 모델링 시간 단축 측정, q5-02)와'를 빼 '가설 판정(q5-03)은 아직 조사하지 않았고'만 남겼고, 새 소절 첫 문단의 '이 절 첫 문단과 … 이 소절이 채운다' 문장을 삭제했다. 나머지 문장·각주·태그는 바꾸지 않았다.

## 트랙 갱신

- 단계 페이지: docs/tracks/floorplan-recognition/stage-5-verification-and-hypotheses.md
- 온톨로지 초안 버전: 1.2
- 트랙 로그 항목: 답한 질문: q5-02(현장 모델링 시간 단축 측정 기준 — 시간·수정·결과 품질 세 축 측정 구성, 추정 중심, f1~f19) / 새 질문: q5-12(f14), q5-13(f15); q5-11 은 q5-09 중복 등록이라 폐기 / 온톨로지 변경: 없음(공간 그래프 스키마 초안 v1.2 유지 — 시간·수정 측정은 스키마 개념·관계가 아니라 검증 방법이어서 아이디어 3. 건축 도면 자동 인식 6절에 둠) / 완료 조건 평가: 미충족(부족: 가설 판정표 q5-03, 사용자에게 제안하는 실험 계획; 검증 절차는 추정 중심으로 이번에 처음 실림) / 세부영역 반영 제안: 4건 — 21. 온보딩·설정·현장 시운전(6절: 수작업 대비 공수 측정, f2·f10 [추정], f12 [의견]), 23. 시험·형식 검증·벤치마크(6절: 편집 비용·클릭 수·HTER, f7 [추정]), 27. AI·학습·적응과 모델 운영(6절: 도면 해석 모델의 수정 노력 평가), 6. 지도·공간·위치 모델(6절: 교차 규칙 연결과 ROP 측정 경계) / 다음 실행 제안: q5-03(가설 판정표), 이어서 q5-04 와 실험 계획(q5-12 기반)
- 개요 진행 현황: 단계 5 진행 중 — 열린 질문 10, 답함 2, 완료 조건 미충족(q5-02 답함, q5-11 폐기)

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q5-02 | 답함 | docs/tracks/floorplan-recognition/stage-5-verification-and-hypotheses.md#q5-02 | — | — | — |
| q5-11 | 폐기 | — | — | — | — |
| q5-12 | 열림 | — | 같은 물류센터 층을 ROP 운영자가 수작업과 '도면 자동 생성+보정' 두 조건으로 모델링하는 비교 실험에서, 학습 효과(같은 도면 반복)와 숙련도 차이를 어떻게 통제하고(참가자·층 배정, 순서 균형), 입력 준비·자동 처리·보정·검증 시간을 어떤 단위로 기록하는가? (q5-02 에서 파생) | 5 | f14 |
| q5-13 | 열림 | — | 편집 비용 지표의 연산별 가중치(벽 삭제, 문·엘리베이터·충전 위치 추가, 목적지 이름 수정 등)를 실제 보정 작업의 연산별 평균 소요 시간으로 보정하려면 어떤 기록(편집 로그·화면 기록)이 필요하며, 편집 수와 시간의 상관을 어떻게 확인하는가? (q5-02 에서 파생) | 5 | f15 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 21 | 6. 대표 접근법과 기술 | 시운전·설정 공수를 수작업 대비로 재는 방법: 같은 도면·현장을 수작업과 '자동 생성+보정' 두 조건으로 처리해 단계별 시간·요소 유형별 수정 횟수·보정 후 결과 품질을 함께 재는 구성([추정], ref-748·ref-749·ref-756). 평면도 주석의 수작업 40분 대 보정 5분 사례([추정], 저자 보고, 지도 1건, 수치 미재확인, ref-749), 도면→BIM 준자동 생성의 시간 단축 저자 보고([추정], 수치 미확인, ref-760), 설치 병목 작업([사실], ref-217), 가상 시운전 36건 리뷰 저자들의 근거 부족 평가([의견], ref-758). 분류 원문 질문 '새 제조사나 새 물류센터를 추가할 때 반복 작업을 얼마나 줄일까?'와 연결. |
| 23 | 6. 대표 접근법과 기술 | 자동 생성 결과의 사람 수정 노력 지표: 편집 연산 유형별 편집 비용([사실], ref-748), 가상 주석자 클릭 수와 NoC@90([사실], ref-750·ref-751·ref-762), 기계번역 HTER([사실], ref-754). 편집 수와 소요 시간의 관계는 출처 안에서 약한 상관 서술(서론)과 높은 상관 결과가 엇갈리므로([추정], ref-756·ref-755) 수정 횟수를 시간과 함께 기록하고 연산별 가중치를 실측 시간으로 보정하는 방식([추정]). |
| 27 | 6. 대표 접근법과 기술 | 도면 해석 모델을 정확도가 아니라 사람 수정 노력으로 평가하는 방법: 편집 비용([사실], ref-748), 클릭 수([사실], ref-750), 전문가 편집 이력 데이터셋 A-Scan2BIM과 연산 순서·다음 벽 예측 평가([사실], ref-752·ref-753). 분류 원문 8장 교차 규칙에 따라 적용 대상 6. 지도·공간·위치 모델과 양쪽에 연결. |
| 6 | 6. 대표 접근법과 기술 | 도면 해석(6. 지도·공간·위치 모델에 적용되는 27. AI·학습·적응과 모델 운영의 방법) 결과를 편집 비용·클릭 수로 평가하고, 현장 모델링 시간 단축은 도면 인식 결과 보정·공용 자원 등록·좌표·층 정렬·목적지 대응표 작성의 시간·수정 횟수로 재는 경계([추정], ref-748·ref-217·ref-105). 로봇 쪽 지도 작성 주행·위치추정 조정 시간은 연계 대상. |
