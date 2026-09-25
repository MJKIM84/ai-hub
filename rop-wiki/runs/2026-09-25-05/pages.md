# 스토리텔러 산출 2026-09-25-05

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/floorplan-recognition/stage-1-prior-work-and-products.md | draft | q1-01 답함(공개 평면도 인식 데이터셋·모델), 후속 질문 3건(q1-05·q2-04·q4-05), 완료 조건 1 미충족·2 충족(막힌 질문 q1-02~q1-05), 상태 줄 갱신, 4절 결론 종합 판단 [추정] 처리, 출처 17건(ref-062~ref-078로 재부여), 이력 행 추가 |
| update | docs/tracks/floorplan-recognition/space-graph-schema-draft.md | draft | 초안 v0 → v0.1: H1 버전 표기 v0.1, 창문·난간 개념 추가, 관계 '공간 노드 / 인접한다(문 없이) / 공간 노드' 추가, 공간 노드에 방 유형 속성, 벽·문·계단·공간 노드 확정, 에스컬레이터 등 6절 질문 추가(각주 ref-062~ref-078 체계) |
| update | docs/ideas/floorplan-recognition.md | draft | 3절에 단계 1 선행 연구·데이터셋 비교표(11종), 관련 모델·로봇 적용 연구, 한계를 싣고 제품 사례는 미조사(q1-02)로 명시, LLM·VLM 약어 풀어 씀, 프런트매터 sources(ref-062~ref-078) 추가 |
| update | docs/tracks/floorplan-recognition/index.md | draft | 상태 줄의 마지막 트랙 실행을 2026-09-25로 갱신(현재 단계 유지), 머리 단락의 '조사 결과는 아직 없으며' 문장을 단계 1 결과 반영으로 수정, 6. 살아있는 산출물 링크 갱신(초안 v0.1, 아이디어 페이지 3절 초안, 후속 질문 3건), last_run 추가 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 건축 도면 자동 인식 단계 1 | q1-01 답함: 공개 평면도 인식 데이터셋·모델 비교, 공간 그래프 스키마 초안 v0.1, 후속 질문 3건 | run 2026-09-25-05
- 홈 최근 업데이트: 2026-09-25 — 건축 도면 자동 인식 단계 1: q1-01 답함(공개 평면도 인식 데이터셋·모델 11종 비교, 엘리베이터 라벨은 벡터 CAD 쪽에서만 추정 확인), 공간 그래프 스키마 초안 v0.1
- 대분류 최근 업데이트: 2026-09-25 — 건축 도면 자동 인식 단계 1: 6. 지도·공간·위치 모델과 연결되는 공개 평면도 인식 데이터셋·모델 조사, 공간 그래프 스키마 초안 v0.1(창문·난간·문 없는 인접 관계)
- 세부영역 최근 업데이트: 2026-09-25 — 건축 도면 자동 인식 트랙 단계 1: 평면도 인식 데이터셋·모델 조사 결과를 6. 대표 접근법과 기술, 7. 관련 표준·프레임워크·오픈소스, 8. 대표 연구와 자료 절에 반영 제안

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 평면도 인식 | Floor Plan Recognition | 평면도 이미지나 CAD 도면에서 벽·문·창문·계단 같은 건축 요소와 방 영역·유형을 자동으로 찾아내 구조화하는 작업이다. | 6, 27 | ref-062, ref-064, ref-066, ref-070 |
| new | 래스터–벡터 변환 | Raster-to-Vector Conversion | 픽셀 이미지로 된 평면도를 벽 선분·교차점·방 다각형 같은 기하 요소의 벡터 표현으로 바꾸는 처리이다. | 6, 27 | ref-065, ref-070 |
| new | 파놉틱 심볼 스포팅 | Panoptic Symbol Spotting | CAD 도면의 선 요소마다 문·창문 같은 셀 수 있는 기호의 개별 인스턴스와 벽 같은 셀 수 없는 영역의 의미를 함께 판별하는 과제이다. | 6, 27 | ref-066, ref-067, ref-073 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-062 | CubiCasa (Kalervo, A. 외) | CubiCasa5k — README (CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis) | 오픈소스 문서 | high | https://github.com/CubiCasa/CubiCasa5k |
| ref-063 | Kalervo, A., Ylioinas, J., Häikiö, M., Karhu, A., & Kannala, J. | CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis | 논문 | medium | https://arxiv.org/abs/1904.01920 |
| ref-064 | Zeng, Z., Li, X., Yu, Y. K., & Fu, C.-W. | DeepFloorplan — README (Deep Floor Plan Recognition using a Multi-task Network with Room-boundary-Guided Attention) | 오픈소스 문서 | high | https://github.com/zlzeng/DeepFloorplan |
| ref-065 | Liu, C., Wu, J., Kohli, P., & Furukawa, Y. | FloorplanTransformation — README (Raster-to-Vector: Revisiting Floorplan Transformation) | 오픈소스 문서 | high | https://github.com/art-programmer/FloorplanTransformation |
| ref-066 | FloorPlanCAD 프로젝트(Fan, Z. 외) | FloorPlanCAD Dataset — project page (floorplancad.github.io index.md) | 오픈소스 문서 | high | https://floorplancad.github.io/ |
| ref-067 | Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P. | FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting | 논문 | medium | https://arxiv.org/abs/2105.07147 |
| ref-068 | Voxel51 (Hugging Face) | Voxel51/FloorPlanCAD · Datasets at Hugging Face | 오픈소스 문서 | medium | https://huggingface.co/datasets/Voxel51/FloorPlanCAD |
| ref-069 | Pizarro, P. N., Hitschfeld, N., & Sipiran, I. (MLSTRUCT) | MLStructFP — README (Large-scale multi-unit floor plan dataset for architectural plan analysis and recognition) | 오픈소스 문서 | high | https://github.com/MLSTRUCT/MLStructFP |
| ref-070 | Hu, S. 외 | Raster-to-Graph — README (Raster-to-Graph: Floorplan Recognition via Autoregressive Graph Prediction with an Attention Transformer) | 오픈소스 문서 | high | https://github.com/SizheHu/Raster-to-Graph |
| ref-071 | Agour, M. 외 (ResPlan) | ResPlan — README (ResPlan: A Large-Scale Vector-Graph Dataset of 17,000 Residential Floor Plans) | 오픈소스 문서 | high | https://github.com/m-agour/ResPlan |
| ref-072 | van Engelenburg, C. 외 (MSD) | msd — README (MSD: A Benchmark Dataset for Floor Plan Generation of Building Complexes) | 오픈소스 문서 | high | https://github.com/caspervanengelenburg/msd |
| ref-073 | Luo, R. 외 | ArchCAD-400K: A Large-Scale CAD drawings Dataset and New Baseline for Panoptic Symbol Spotting | 논문 | medium | https://arxiv.org/abs/2503.22346 |
| ref-074 | 한국지능정보사회진흥원(AI Hub) | 건축 도면 데이터 | 정부·연구기관 | medium | https://aihub.or.kr/aihubdata/data/view.do?dataSetSn=71465 |
| ref-075 | de las Heras, L.-P., Terrades, O. R., Robles, S., & Sánchez, G. | CVC-FP and SGT: a new database for structural floor plan analysis and its groundtruthing tool | 논문 | medium | https://www.researchgate.net/publication/270597635_CVC-FP_and_SGT_a_new_database_for_structural_floor_plan_analysis_and_its_groundtruthing_tool |
| ref-076 | DeFazio, D., Mehta, H., Wang, M., Yang, P., Blackburn, J., & Zhang, S. | Vision Language Models Can Parse Floor Plan Maps | 논문 | medium | https://arxiv.org/abs/2409.12842 |
| ref-077 | DoorDet 저자(arXiv 2508.07714) | DoorDet: Semi-Automated Multi-Class Door Detection Dataset via Object Detection and Large Language Models | 논문 | medium | https://arxiv.org/abs/2508.07714 |
| ref-078 | Kratochvila, L., de Jong, G., Arkesteijn, M., Zemcik, T., Bilik, S., Horak, K., & Rellermeyer, J. S. | Multi-Unit Floor Plan Recognition and Reconstruction Using Improved Semantic Segmentation of Raster-Wise Floor Plans | 논문 | medium | https://arxiv.org/abs/2408.01526 |

## 열린 질문 갱신

- 없음

## 흐름 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

- 없음

## 추가 조사 요청

- 참고문헌 id 재부여 확인(pipeline/publish 담당): 브리프 id ref-044~ref-060 17건을 기존 참고문헌(ref-044~ref-052 사용분)과 브리프 2026-09-25-04 사용분(ref-044~ref-059, ref-061)을 피해 ref-062~ref-078 로 순서대로 재부여했다(ref-044→ref-062, 045→063, 046→064, 047→065, 048→066, 049→067, 050→068, 051→069, 052→070, 053→071, 054→072, 055→073, 056→074, 057→075, 058→076, 059→077, 060→078). research.json·verification.json 의 출처 id 와 대응표로 연결하고, 게시 전에 ref-062~ref-078 이 비어 있는지 확인해야 한다.
- 단계 3. 구현 가설 설계 페이지의 q3-02 에 관련 근거 f20(실행 2026-09-25-05)을 연결해야 한다(1차 검증 수정 지시). 이번 입력에 단계 3 페이지가 없어 다음 단계 3 실행 또는 퍼블리셔 처리로 넘긴다.
- q1-02(도면에서 로봇용 지도·공간 모델을 만드는 제품 사례)가 완료 조건 1 충족에 필요하다: 아이디어 3 페이지 3절의 '제품 사례' 소절을 채울 제품·연구 사례와 입력 형식별 자동화 범위.
- q2-04: CubiCasa5K 80여 범주와 AI Hub 건축 도면 데이터 클래스 목록의 엘리베이터·계단 포함 여부, 두 데이터의 상업 이용 조건(원문 열람 필요).
- FloorPlanCAD 35개 범주 전체 목록을 공식 출처(논문 원문)로 확인하면 엘리베이터 범주 서술을 [추정]에서 재검토할 수 있다. 제3자 카드의 '30 object categories' 표기와의 차이도 확인이 필요하다.

## 이행한 수정 지시

- 참고문헌 id 충돌 — 브리프 id ref-044~ref-060 17건을 기존 참고문헌과 브리프 2026-09-25-04 사용분(ref-044~ref-059, ref-061)에 겹치지 않는 ref-062~ref-078 로 순서대로 재부여하고, 네 페이지의 각주·프런트매터 sources, reference_updates, glossary_updates 의 sources 를 같은 대응으로 통일했다(대응표는 additional_research_requests 와 reference_updates summary 에 적었다).
- 원문 열람 표시 — 네 페이지의 각주 정의에서 원문을 연 출처(ref-062·064·065·066·069·070·071·072, 브리프 ref-044·046·047·048·051·052·053·054)는 표시 없이, 원문 미열람 출처(ref-063·067·068·073·074·075·076·077·078, 브리프 ref-045·049·050·055·056·057·058·059·060)는 접근일 뒤에 ' (원문 미열람)'을 붙였고 reference_updates 에 source_unopened 를 같은 값으로 넣었다.
- f6 — 단계 1 페이지 3절과 아이디어 페이지 표에서 [추정]으로 쓰고 근거가 제3자 재배포 카드(ref-068, 브리프 ref-050)임을 밝혔으며 'stuff 범주' 부분을 삭제하고 FloorPlanCAD 범주 수는 공식 프로젝트 페이지(ref-066, 브리프 ref-048)의 35개만 썼다.
- f7 — ArchCAD-400K 범주 예시에서 '도면 기호'를 빼고 기둥·보(구조 요소), 문·창문(비구조 요소)만 썼다.
- f8 — '칠레 주거 건물 프로젝트에서 온'을 삭제하고 단계 1 페이지에 '출처 국가는 미확인'을 적었다.
- f18 — 국가 목록에서 칠레를 뺐다(핀란드·일본·스위스·국내 주택).
- f12 — CVC-FP 출처(ref-075, 브리프 ref-057) 발행일을 각주와 reference_updates 에서 2015 로 적고 본문에 2015년 발표를 밝혔다.
- f16 — 성공률 0.96 에 GPT-4o, 연구진이 라벨을 조밀하게 덧붙인 평면도, 최대 아홉 단계 이동 과제 조건과 단일 출처 수치임을 단계 1 페이지와 아이디어 페이지에 병기했다.
- f3 — README 의 '약 90% 정밀도·재현율'은 브리프 claim 밖이므로 쓰지 않았다.
- f11·f13 — MSD 계단 범주 언급과 AI Hub 규모 수치는 어느 페이지에도 쓰지 않았다(아이디어 표의 AI Hub 규모 칸은 '미확인').
- 에스컬레이터 — 공간 그래프 스키마 초안 개념 표에 넣지 않고 6절 미해결 모델링 질문으로 두었으며 '로봇이 이용할 수 없다'는 서술은 쓰지 않았다.
- 온톨로지 승인 변경 — 창문(f2·f4·f10)·난간(f2·f14) 개념 추가, 관계 '공간 노드 / 인접한다(문 없이) / 공간 노드'(f10) 추가, 공간 노드 속성 방 유형(f3·f4·f9·f10)을 확정으로 반영하고 벽(f2·f4·f8)·문(f4·f10)·계단(f2·f14)을 확정으로 바꿨으며 엘리베이터·충전 위치 등 나머지 시드 행은 초안으로 두고 ontology_version 을 '0' → '0.1' 로 올렸다(H1 은 patch 로 바꿀 수 없어 추가 요청).
- q3-02 중복 — f20 기반 새 질문을 backlog_updates 에 넣지 않고 단계 1 페이지 5절에 q3-02 관련 근거로 연결한다고 적었으며 스키마 초안 6절에 q3-02 로 연결했다. 단계 3 페이지는 입력에 없어 연결을 추가 요청으로 넘겼다.
- 단계 1 페이지 6절 — 완료 조건 1 '미충족', 완료 조건 2 '충족'으로 적고 표 아래 줄을 '다음 단계로 전환: 아니오(완료 조건 1 미충족; 막힌 질문 q1-02·q1-03·q1-04)'로 썼다.
- 아이디어 3 페이지 3절 — 브리프 finding 으로 직접 만든 데이터셋 비교표와 관련 연구·한계를 싣고 제품 사례를 '아직 조사되지 않음(q1-02)'으로 명시했다.
- 세부영역 반영 — 6. 지도·공간·위치 모델과 27. AI·학습·적응과 모델 운영 페이지는 고치지 않고 area_reflection_proposals 로만 냈으며, f16 을 도면 해석 방법으로만 쓰고 로컬 주행·경로 실행은 로봇 쪽 연계 대상임을 밝혔다.
- 2차: 단계 1 페이지 4절 결론 두 번째 항목 — 계단 부분만 '계단은 CubiCasa5K와 Kratochvila 외(2024)에서 인식 대상으로 확인됐다. [사실]'로 남기고, '벽·문·창문은 확인한 자료 대부분에서 기본 인식 대상인 것으로 보인다(종합 판단). [추정]'으로 따로 나눴다.
- 2차: 단계 1 페이지 6절 표 아래 줄을 '다음 단계로 전환: 아니오(완료 조건 1 미충족; 막힌 질문 q1-02·q1-03·q1-04·q1-05)'로 고치고 track_updates.log_entry 의 완료 조건 평가도 같은 막힌 질문 목록으로 맞췄다.
- 2차: 단계 1 페이지 H1 아래 상태 줄을 '> 단계 상태: 진행 중 · 열린 질문: 4건 · 답한 질문: 1건 · 완료 조건: 미충족 · 마지막 실행: 2026-09-25'로 고쳤다. 페이지 전문(content)으로 냈다.
- 2차: 공간 그래프 스키마 초안 H1 을 '# 공간 그래프 스키마 초안 (v0.1)'로 고쳐 프런트매터 ontology_version '0.1'·track_updates.ontology_draft_version 과 맞췄다. 페이지 전문으로 냈고 auto:page-status 마커 안은 손대지 않았다.
- 2차: 트랙 개요 상태 줄의 '마지막 트랙 실행'을 2026-09-25 로 고치고 현재 단계는 '단계 1. 선행 연구·제품 사례 조사' 그대로 두었으며, 머리 단락의 '이 트랙의 조사 결과는 아직 없으며' 문장을 '조사 결과는 각 단계 페이지와 아래 살아있는 산출물에 실리며 … 첫 결과는 실행 2026-09-25-05에서 단계 1 페이지에 실렸다'로 바꿨다.
- 2차: 아이디어 3 페이지 프런트매터에 3절 각주와 같은 sources(ref-062~ref-078)를 더했다.
- 2차: 아이디어 3 페이지 3절에서 LLM 을 '대규모 언어 모델(Large Language Model, LLM)', VLM 을 '시각-언어 모델(Vision-Language Model, VLM)'로 풀어 썼다.
- 2차: glossary_updates '래스터–벡터 변환' description 에서 '벡터 표현은 이후 지도·공간 그래프 생성의 입력이 된다'를 지우고 f3 범위의 서술(래스터 평면도를 벽·문(개구부)·방 유형·아이콘을 담은 벡터 표현으로 바꾼다)로 바꿨다.

## 트랙 갱신

- 단계 페이지: docs/tracks/floorplan-recognition/stage-1-prior-work-and-products.md
- 온톨로지 초안 버전: 0.1
- 트랙 로그 항목: 답한 질문: q1-01(공개 평면도 인식 데이터셋·모델, finding f1~f21) / 새 질문: q1-05(f18), q2-04(f17), q4-05(f21) — f20 기반 질문은 q3-02 와 중복이라 등록하지 않고 q3-02 관련 근거로 연결 / 온톨로지 변경: v0 → v0.1(2026-09-25, 근거 실행 2026-09-25-05): 개념 '창문'(f2·f4·f10)·'난간'(f2·f14) 추가, 관계 '공간 노드 / 인접한다(문 없이) / 공간 노드'(f10) 추가, '공간 노드' 속성 방 유형 추가(f3·f4·f9·f10), 시드 개념 벽(f2·f4·f8)·문(f4·f10)·계단(f2·f14) 확정; 에스컬레이터(f6) 제안은 검증 거부로 6절 질문 / 완료 조건 평가: 미충족(부족: 아이디어 3. 건축 도면 자동 인식 페이지 3절의 제품 사례 비교 q1-02; 막힌 질문 q1-02·q1-03·q1-04·q1-05; 완료 조건 2 인식 대상 요소 목록 반영은 충족) / 세부영역 반영 제안: 6. 지도·공간·위치 모델 4건, 27. AI·학습·적응과 모델 운영 1건 / 참고문헌: 브리프 ref-044~ref-060 을 ref-062~ref-078 로 재부여 / 다음 실행 제안: q1-02, q1-03, q1-04, q1-05
- 개요 진행 현황: 단계 1 진행 중 — 열린 질문 4(q1-02·q1-03·q1-04·q1-05), 답함 1(q1-01), 완료 조건 미충족

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q1-01 | 답함 | docs/tracks/floorplan-recognition/stage-1-prior-work-and-products.md#q1-01 | — | — | — |
| q1-05 | 열림 | — | 물류센터·창고 평면도(랙·도크·충전 구역 포함)를 대상으로 한 공개 평면도 인식 데이터셋이나 모델이 있는가, 없으면 주거·상업 데이터셋으로 학습한 모델이 물류 시설 도면에 얼마나 옮겨지는가? | 1 | f18 |
| q2-04 | 열림 | — | AI Hub 건축 도면 데이터와 CubiCasa5K 의 클래스 목록에 계단·엘리베이터가 포함되는지, 그리고 상업적 이용 조건은 무엇인가? | 2 | f17 |
| q4-05 | 열림 | — | 축척 정보가 없는 래스터 평면도의 인식 결과를 로봇 지도 좌표(미터)로 옮기기 위해 축척을 어떻게 복원하는가(치수 문자 OCR, 문 폭 등 기준 요소, 현장 측정)? | 4 | f21 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 6 | 6. 대표 접근법과 기술 | 평면도 인식 접근 세 갈래: 래스터 이미지 분할·검출(DeepFloorplan 다중 작업 신경망, Kratochvila 외 U-Net 계열 분할과 벡터화), 래스터–벡터 변환(Raster-to-Vector), 구조 그래프 예측(Raster-to-Graph). 벡터 CAD 도면은 파놉틱 심볼 스포팅 과제로 다룬다(FloorPlanCAD, ArchCAD-400K). 축척 복원은 별도 과제로 보인다([추정], f21). 근거 f3·f4·f5·f9·f14·f21. |
| 6 | 7. 관련 표준·프레임워크·오픈소스 | 공개 데이터셋·오픈소스: CubiCasa5K, FloorPlanCAD(주석 CC BY-NC 4.0, 2022년 초 종료), MLSTRUCT-FP, ResPlan(CC BY 4.0, 방 연결 그래프), 국내 AI Hub 건축 도면 데이터. 다수 데이터셋이 비상업 라이선스·승인제라 상용 적용 시 라이선스 검토가 필요할 것으로 보인다([추정], f19). 근거 f1·f5·f8·f10·f13·f19. |
| 6 | 8. 대표 연구와 자료 | DeepFloorplan(ICCV 2019), Raster-to-Graph(EG 2024), DeFazio 외(2024) VLM 지도 파싱(GPT-4o·조밀 라벨 평면도·최대 아홉 단계 과제에서 성공률 0.96, 단일 출처). VLM 연구는 도면 해석 방법으로만 다루고 로컬 주행·경로 실행은 로봇 쪽 연계 대상. 27. AI·학습·적응과 모델 운영 페이지와 양쪽 연결. 근거 f4·f9·f16. |
| 6 | 11. 열린 질문 | 물류센터·창고 평면도와 충전 위치 라벨을 담은 공개 데이터셋은 이번 검색에서 찾지 못했다(부재 확인 아님, [추정] f18). 엘리베이터 라벨은 벡터 CAD 데이터셋에서만 제3자 자료로 확인됐다([추정] f17). 트랙 백로그 q1-05·q2-04 와 연결. |
| 27 | 8. 대표 연구와 자료 | 도면 해석(교차 규칙상 6. 지도·공간·위치 모델에 적용되는 방법): 다중 작업 신경망(DeepFloorplan), 자기회귀 그래프 예측(Raster-to-Graph), 검출기·LLM·사람 검수를 잇는 반자동 주석 구축(DoorDet, 저자 의견), VLM 평면도 파싱(DeFazio 외 2024). 6. 지도·공간·위치 모델 페이지와 양쪽 연결. 근거 f4·f9·f15·f16. |
