---
title: "45. 문서·도면·장면 이해"
type: area
category: "L. AI·학습 기술"
area_no: 45
related_areas: [4, 5, 7, 14, 15, 16, 18, 44, 47, 53, 54, 55, 61, 62, 64, 66]
tags: [문서 파싱, 도면 인식, 자산관리셸, 출처 근거 연결, 인프라 장착 센서, 3차원 장면 그래프]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-30
sources: [ref-308, ref-1065, ref-063, ref-1012, ref-1066, ref-239, ref-1067, ref-513, ref-1068, ref-1069, ref-1070, ref-067, ref-1071, ref-1072, ref-1073, ref-1074]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [L. AI·학습 기술](index.md) › 45. 문서·도면·장면 이해

# 45. 문서·도면·장면 이해

!!! info "소속 대분류"
    [L. AI·학습 기술](index.md) — 핵심 질문:
    학습·언어 모델 같은 AI 기술을 어디에 쓰고, 그 결과를 어떤 기준으로 믿을 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

매뉴얼·도면 해석과 플랫폼 수준의 장면 인식 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **문서·도면 해석 AI**: 매뉴얼과 도면을 해석하는 모델을 다룬다
- **플랫폼 수준 장면 인식**: 고정 카메라와 여러 로봇의 인식 결과를 모아 공간 상태를 인식한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 27번 영역 ‘AI·학습·적응과 모델 운영’에서 왔다. 그 본문은 [47. AI·학습·적응과 모델 운영](ai-learning-adaptation-and-model-operations.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

매뉴얼·도면·현장 영상을 AI가 얼마나 정확히 읽어 낼 수 있는가? [분류원문]

## 3. 왜 중요한가

이기종 로봇 등록과 능력 표현에 필요한 정보는 제조사 문서·데이터시트·[URDF(Unified Robot Description Format, 통합 로봇 기술 형식)](../../glossary/urdf.md)에 흩어져 있고, 도면에서 지도를 만들려면 도면 심볼을 정확히 읽어야 하며, 로봇 한 대로는 가려지는 공간 상태는 여러 로봇과 고정 카메라의 인식을 모아야 알 수 있으므로, 이 영역의 해석 오류는 그대로 등록 정보·지도·세계 상태의 오류로 이어진다고 볼 수 있다. [추정][^ref-1072][^ref-1071][^ref-239][^ref-1073][^ref-1066][^ref-308][^ref-1065][^ref-1069]

자세한 내용은 주제 페이지 [45. 문서·도면·장면 이해 — 왜 중요한가](../../topics/2026/2026-09-30-area45-s3.md)에 있다.

## 4. 핵심 개념과 용어

문서·도면·장면을 읽는 기술은 다음 용어로 나눠 볼 수 있다.

자세한 내용은 주제 페이지 [45. 문서·도면·장면 이해 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area45-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

아래 사례는 출처가 보고한 연구·시연이며, 출처가 다루지 않은 칸은 "미확인"으로 둔다. 병원·가정 현장의 적용 사례는 이번 조사에서 찾지 못했다.

**현장 유형:** 상업 시설

**사례:** 쇼핑몰 평면도에서 점포 공간 식별(논문 평가)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인(출처가 다루지 않음) |
| 작업 대상 | 쇼핑몰 평면도 25장과 그 안의 점포 1,340개(공간·정보) [사실][^ref-1066] |
| 수행 자원 | 도면 인식 소프트웨어: 층별 안내판 문자 인식으로 점포 번호–이름 대응을 만들고, 2단계 영역 성장 분할과 문자 인식으로 평면도의 점포 공간을 식별한다 [사실][^ref-1066] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 공간 분할 정확도 92.54%, 점포 인식 정확도 90.56%, 전체 검출 정확도 83.81%(2022-03 발표) [사실][^ref-1066] |

이 사례는 로봇 현장 배치가 아니라 쇼핑몰 평면도 25장에 대한 논문 평가 결과다. [사실][^ref-1066] 저자들은 실내 로봇 주행을 이 방법의 활용처 가운데 하나로 들었다. [사실][^ref-1066]

**현장 유형:** 제조 공장

**사례:** 대형 상용차 최종 조립 공장에서 천장 카메라로 운반 로봇의 위치와 장애물 인식

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 머플러를 약 150 m 구간에서 운반한다 [사실][^ref-308] |
| 수행 자원 | 약 8 m 높이에 단 카메라 15대(대당 약 60 m²)가 바닥을 덮고 로봇 6대가 운반한다. 카메라가 로봇에 붙인 ArUco 표식을 검출해 로봇 위치·방향을 계산하고, 저해상도 영상의 이진 의미 분할로 장애물과 빈 공간을 격자 단위로 구분한다 [사실][^ref-308] |
| 제약 | 카메라 간 하드웨어 동기화가 없어 생기는 시간 차 오류, 가림·센서 고장·제한된 시야 범위로 인한 위치 추정 중단, 작업자·독점 제품·기밀 공정이 영상에 찍히는 개인정보·기밀 문제 [사실][^ref-308] |
| 완료·인계 | 미확인 |
| 예외·성과 | 하루 최대 130회 운반(주기 약 7분) [사실][^ref-308]. 위치 추정이 끊겼을 때의 복구 주체는 미확인 |

카메라별 점유 지도를 전역 지도로 합칠 때 시야가 겹치는 곳은 가장 가까운 카메라 하나의 결과만 쓴다(2025-12 발표). [사실][^ref-308] 이 사례에서 이 영역이 맡는 부분은 로봇 밖의 카메라 인식 결과를 공간 상태로 모으는 일이다. [추정][^ref-308]

**현장 유형:** 물류창고

**사례:** 창고 CCTV 카메라망만으로 여러 로봇을 계획·제어하는 시연(흐름 단계 미확인)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 미확인(초록에 운반물 서술 없음) |
| 수행 자원 | 작업용 주행 장비를 싣지 않은 로봇 4대, 창고 CCTV 카메라 30대, 외부 계산 자원 [사실][^ref-1065] |
| 제약 | 길이 27 m 통로 6개. 시야가 겹치는 카메라 구역을 배타적 자원으로 관리해 충돌·교착을 막는다 [사실][^ref-1065] |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인(임무 시간·조율 통계 수치가 초록에 없음) |

이 시스템은 보정하지 않은 화소 단위 위상 카메라 그래프 위, 즉 영상 공간에서 여러 로봇을 계획·제어하며, 저자들은 이를 첫 현장 시연이라고 밝혔다(2026-06 발표). [사실][^ref-1065] 로봇 주행을 외부 카메라로 옮긴 방식이므로 9절에서 경계가 이동한 사례로 다룬다.

**현장 유형:** 실외

**사례:** 운영자의 자연어 의도로 여러 로봇에 대규모 실외 작업 맡기기

| 항목 | 내용 |
|---|---|
| 시작 조건 | 운영자가 자연어로 의도를 말하면 LLM(Large Language Model, 대규모 언어 모델)이 공유 장면 그래프와 로봇 능력에서 문맥을 뽑아 [PDDL(계획 도메인 정의 언어)](../../glossary/pddl.md) 목표로 바꾼다 [사실][^ref-1070] |
| 작업 대상 | 대규모 실외 환경과 그 안의 객체(개방형 객체 지도를 담은 공유 3차원 장면 그래프로 표현) [사실][^ref-1070] |
| 수행 자원 | 여러 로봇(대수 미확인)과 LLM, 다중 로봇 계획·실행 시스템 [사실][^ref-1070] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인(실험 수치가 초록에 없음) |

이 시스템은 개방형 객체 지도를 담은 공유 3차원 장면 그래프로 여러 로봇의 장면 그래프를 융합하고, 대규모 실외 환경의 실제 작업으로 평가했다(2025-07 개정판). [사실][^ref-1070]

## 6. 대표 접근법과 기술

문서·도면·장면을 읽는 접근법은 대상에 따라 다섯 갈래로 나뉘며, 어느 갈래도 사람 확인 없이 실행 정보로 쓸 수준은 아닌 것으로 보인다. [추정][^ref-1073][^ref-1071][^ref-1069]

자세한 내용은 주제 페이지 [45. 문서·도면·장면 이해 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area45-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역에서 쓰는 도구·벤치마크·데이터셋은 다음과 같다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [45. 문서·도면·장면 이해 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area45-s7.md)에 있다.

## 8. 대표 연구와 자료

이 영역의 판단 근거가 된 연구와 자료는 다음과 같다.

자세한 내용은 주제 페이지 [45. 문서·도면·장면 이해 — 대표 연구와 자료](../../topics/2026/2026-09-30-area45-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 로봇이 내는 인식 결과(위치·장면 그래프)를 받아 시간·좌표를 맞춰 고정 카메라 결과와 하나의 공간 상태로 합치는 플랫폼 수준 융합 [추정][^ref-308][^ref-1070] | 연계 대상: 로봇 온보드 센서 인식·SLAM·국지 회피는 로봇 제조사가 맡는다 [추정][^ref-308][^ref-1070] |
| 시설·설비 제어 | 시설 카메라의 영상·인식 결과를 받아 해석하는 인터페이스와 검토 절차 [추정][^ref-308][^ref-1065] | 연계 대상: CCTV·영상 관리 시스템과 카메라 설치·동기화 [추정][^ref-308][^ref-1065] |

ROP가 이 영역에서 직접 맡을 범위는 매뉴얼·데이터시트·도면을 구조화 정보로 바꾸는 파싱·추출 파이프라인과 그 정확도 평가, 추출 항목마다 원문 위치를 붙여 사람이 확정·반려하게 하는 검토 흐름, 고정 카메라와 여러 로봇의 인식 결과를 시간·좌표를 맞춰 하나의 공간 상태로 합치는 융합이다. [추정][^ref-1067][^ref-1068][^ref-1071][^ref-1074][^ref-308][^ref-1070] 도면·BIM 작성 도구와 원본 도면은 설계·건축 쪽의 연계 대상이고, ROP는 그 결과물을 받아 해석한다. [추정][^ref-067][^ref-1012] 카메라망의 소유·운영 주체는 출처가 밝히지 않아 미확인이다.

5절 물류창고 사례처럼 로봇에 작업용 주행 장비를 두지 않고 외부 카메라와 외부 계산으로 주행을 제어하는 방식은 ROP의 기본 범위가 아니라, [범위 경계](../../about/scope-boundary.md)의 원문 19장이 말하는 "이 경계는 제품 전략에 따라 이동할 수 있다"에 해당하는 사례로 본다. [추정][^ref-1065]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

분류의 교차 규칙에 따라 매뉴얼 해석은 4. 이기종 로봇 등록과 55. 현장 조사·설치·시운전에, 도면 해석은 14. 도면·BIM에서 지도 만들기에 적용되는 연구 방법으로 연결한다.

자세한 내용은 주제 페이지 [45. 문서·도면·장면 이해 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area45-s10.md)에 있다.

## 11. 열린 질문

이 영역에 걸린 질문과 이번 실행의 부분 근거는 다음과 같다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [45. 문서·도면·장면 이해 — 열린 질문](../../topics/2026/2026-09-30-area45-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-308]: Brorsson, E., Ceder, K., Zhang, Z. 외 (arXiv), Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives, 2025-12-17, https://arxiv.org/abs/2512.15215, 접근일 2026-09-30
[^ref-1065]: Robinson, L., Ramtoula, B., Izaaryene, A., Newman, P., & De Martini, D. (arXiv), Multi-Robot Planning and Control from CCTV Camera Networks in a Real Warehouse, 2026-06-04, https://arxiv.org/abs/2606.06762, 접근일 2026-09-30
[^ref-1012]: 한국지능정보사회진흥원 AI Hub (구축 주관: 에이치씨아이플러스(주)), 건축 도면 데이터, 미확인, https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71465, 접근일 2026-09-30
[^ref-1066]: Su, M., Shi, W., Zhao, D., Cheng, D., & Zhang, J. (Sensors 22(7)), A High-Precision Method for Segmentation and Recognition of Shopping Mall Plans, 2022-03-25, https://pmc.ncbi.nlm.nih.gov/articles/PMC9003070/, 접근일 2026-09-30
[^ref-239]: Dussard, B., & Sarthou, G. (LAAS-CNRS, arXiv), Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF, 2026-06-10, https://arxiv.org/abs/2606.17073, 접근일 2026-09-30
[^ref-1067]: Ouyang, L., Qu, Y., Zhou, H. 외 (CVPR 2025, arXiv), OmniDocBench: Benchmarking Diverse PDF Document Parsing with Comprehensive Annotations, 2025-03-25(v2, v1 2024-12-10), https://arxiv.org/abs/2412.07626, 접근일 2026-09-30
[^ref-1068]: Livathinos, N., Auer, C., Lysak, M. 외 (IBM Research, arXiv), Docling: An Efficient Open-Source Toolkit for AI-driven Document Conversion, 2025-01-27, https://arxiv.org/abs/2501.17887, 접근일 2026-09-30
[^ref-1069]: Modi, G., Buoso, D., Averta, G., & De Martini, D. (arXiv), RGB-only Active 3D Scene Graph Generation for Indoor Mobile Robots, 2026-05-18, https://arxiv.org/abs/2605.18197, 접근일 2026-09-30
[^ref-1070]: Strader, J., Ray, A., Arkin, J. 외 (arXiv), Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs, 2025-07-10, https://arxiv.org/abs/2506.07454, 접근일 2026-09-30
[^ref-067]: Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P. (arXiv), FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting, 2021-11-29(v2 개정, v1 2021-05-15), https://arxiv.org/abs/2105.07147, 접근일 2026-09-30
[^ref-1071]: Groß, J., & Heidrich, J. (arXiv), AAS-RAIL: Improving Information Extraction for Asset Administration Shells through Retrieval-Augmented In-Context Learning, 2026-09-07, https://arxiv.org/abs/2609.07334, 접근일 2026-09-30
[^ref-1072]: Xia, Y., Xiao, Z., Jazdi, N., & Weyrich, M. (IEEE Access, arXiv), Generation of Asset Administration Shell with Large Language Model Agents: Toward Semantic Interoperability in Digital Twins in the Context of Industry 4.0, 2024-06-24(arXiv v4, IEEE Access 게재일 미확인), https://arxiv.org/abs/2403.17209, 접근일 2026-09-30
[^ref-1073]: Kondratenko, A., Birhane, M., Hsain, H. E., & Maciocci, G. (arXiv), AECV-Bench: Benchmarking Multimodal Models on Architectural and Engineering Drawings Understanding, 2026-01-08, https://arxiv.org/abs/2601.04819, 접근일 2026-09-30
[^ref-1074]: Google (google/langextract), LangExtract — README, 미확인, https://github.com/google/langextract, 접근일 2026-09-30
