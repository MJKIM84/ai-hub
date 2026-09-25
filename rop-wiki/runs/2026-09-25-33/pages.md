# 스토리텔러 산출 2026-09-25-33

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/d-planning-and-optimization/13-task-allocation-mrta.md | draft | 섹션 3~11 신규 작성(분류 체계·배정 방식·Open-RMF 입찰·LLM 기반 배정·열린 질문), 트랙 반영 제안 반영, 페이지 상태 마커 추가 |
| create | docs/topics/2026/2026-09-25-area13-s6.md | draft | 자동 분리: 13. 작업 배정 — MRTA 의 "6. 대표 접근법과 기술" 절(1,913자)을 옮겼다. 형식 수정: 27. AI·학습·적응과 모델 운영, 16. 공용 자원·충전·에너지 최적화 링크 경로를 주제 페이지 위치 기준으로 고쳤다 |
| create | docs/topics/2026/2026-09-25-area13-s8.md | draft | 자동 분리: 13. 작업 배정 — MRTA 의 "8. 대표 연구와 자료" 절(1,428자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area13-s11.md | draft | 자동 분리: 13. 작업 배정 — MRTA 의 "11. 열린 질문" 절(949자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area13-s7.md | draft | 자동 분리: 13. 작업 배정 — MRTA 의 "7. 관련 표준·프레임워크·오픈소스" 절(848자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 13. 작업 배정 — MRTA | 영역 심화: 3~11절 신규 작성(분류 체계·시장 기반·최근접 규칙·Open-RMF 입찰·LLM 기반 배정), 트랙 반영 제안 반영 | run 2026-09-25-33
- 홈 최근 업데이트: 2026-09-25 — 13. 작업 배정 — MRTA: 3~11절 신규 작성(MRTA 분류 체계, 시장 기반·최근접·학습·LLM 기반 배정, Open-RMF 입찰, 열린 질문 3건 추가)
- 대분류 최근 업데이트: 2026-09-25 — 13. 작업 배정 — MRTA: 3~11절 신규 작성(배정 방식 비교, Open-RMF·VDA 5050 의 배정 책임, 최근접 배정의 한계)
- 세부영역 최근 업데이트: 2026-09-25 — 13. 작업 배정 — MRTA: 영역 심화로 3~11절 신규 작성, 트랙 자연어 업무 지시 챗봇의 반영 제안(LLM 기반 배정) 반영

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 헝가리안 방법 | Hungarian Method | 작업과 수행자 사이 일대일 배정에서 총비용을 최소로 하는 최적 배정 문제를 다항 시간에 푸는 고전 알고리즘이다. | 13 | ref-648 |
| new | 시장 기반 작업 배정 | Market-based Task Allocation | 로봇이 작업에 대한 비용·효용을 입찰하고 경매로 낙찰자를 정해 작업을 나누는 배정 방식이다. | 13 | ref-651 |
| new | 합의 기반 번들 알고리즘 | Consensus-Based Bundle Algorithm (CBBA) | 각 로봇이 작업 묶음에 입찰하고 이웃과의 국소 통신 합의로 낙찰 충돌을 풀어 중앙 없이 충돌 없는 배정에 이르는 분산 배정 알고리즘이다. | 13 | ref-650 |
| new | 최근접 차량 우선 규칙 | Nearest Vehicle First (NVF) Rule | 운반 요청이 생기면 요청 위치까지 이동 거리가 가장 짧은 유휴 차량·로봇에 작업을 맡기는 배차 규칙이다. | 13 | ref-655 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-648 | Gerkey, B. P., & Matarić, M. J. | A Formal Analysis and Taxonomy of Task Allocation in Multi-Robot Systems | 논문 | medium | https://journals.sagepub.com/doi/10.1177/0278364904045564 |
| ref-649 | Korsah, G. A., Stentz, A., & Dias, M. B. | A comprehensive taxonomy for multi-robot task allocation | 논문 | medium | https://journals.sagepub.com/doi/10.1177/0278364913496484 |
| ref-650 | Choi, H.-L., Brunet, L., & How, J. P. | Consensus-Based Decentralized Auctions for Robust Task Allocation | 논문 | medium | https://dl.acm.org/doi/10.1109/tro.2009.2022423 |
| ref-651 | Dias, M. B., Zlot, R., Kalra, N., & Stentz, A. | Market-Based Multirobot Coordination: A Survey and Analysis | 논문 | medium | https://www.ri.cmu.edu/pub_files/2006/7/01677943-1.pdf |
| ref-652 | Aziz, H., Chan, H., Cseh, Á., Li, B., Ramezani, F., & Wang, C. | Multi-Robot Task Allocation—Complexity and Approximation | 논문 | medium | https://arxiv.org/abs/2103.12370 |
| ref-653 | Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L. | Decision rules for robotic mobile fulfillment systems | 논문 | medium | https://www.sciencedirect.com/science/article/pii/S2214716019300946 |
| ref-654 | Wang, Z., & Gombolay, M. | Heterogeneous graph attention networks for scalable multi-robot scheduling with temporospatial constraints | 논문 | medium | https://link.springer.com/article/10.1007/s10514-021-09997-2 |
| ref-655 | International Journal of Planning and Scheduling 게재 논문(저자 미확인) | Automated guided vehicle dispatching based on combinatorial optimisation to minimise job waiting time on shop floors | 논문 | medium | https://www.inderscience.com/info/inarticle.php?artid=103016 |
| ref-656 | Open Robotics | Tasks in RMF (task) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/task.html |
| ref-657 | KISTI ScienceON 수록 국가R&D 과제 보고서(수행기관 미확인) | 클라우드에 연결된 개별 로봇 및 로봇그룹의 작업 계획 기술 개발 | 정부·연구기관 | medium | https://scienceon.kisti.re.kr/srch/selectPORSrchReport.do?cn=TRKO202400003952 |
| ref-658 | KISTI ScienceON 수록 논문(저자 미확인) | 시뮬레이션과 메타모델을 이용한 자동물류센터 설계 최적화 | 논문 | medium | https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=JAKO200634515151716 |
| ref-659 | Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin) | Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots | 논문 | medium | https://arxiv.org/abs/2603.22731 |
| ref-660 | Open Robotics (open-rmf) | rmf_task — README | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_task |
| ref-006 | Ma, H., Li, J., Kumar, T. K. S., & Koenig, S. | Lifelong Multi-Agent Path Finding for Online Pickup and Delivery Tasks | 논문 | medium | https://arxiv.org/abs/1705.10868 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-105 | Open Robotics (open-rmf) | fleet_adapter_template — fleet_adapter_template/config.yaml | 오픈소스 문서 | medium | https://github.com/open-rmf/fleet_adapter_template/blob/main/fleet_adapter_template/config.yaml |
| ref-152 | Meseguer Valenzuela, A., & Blanes Noguera, F. | Task Allocation in Mobile Robot Fleets: A review | 논문 | medium | https://arxiv.org/abs/2501.08726 |
| ref-101 | Merschformann, M. (RAWSim-O GitHub) | RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README) | 오픈소스 문서 | medium | https://github.com/merschformann/RAWSim-O |
| ref-132 | Yu, S., & Srinivas, S. | Collaborative Human–Robot Teaming for Dynamic Order Picking: Interventionist strategies for improving warehouse intralogistics operations | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S1366554525001231 |
| ref-089 | SMARTlab-Purdue (Purdue University) | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models (GitHub README) | 오픈소스 문서 | medium | https://github.com/SMARTlab-Purdue/SMART-LLM |
| ref-090 | Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models | 논문 | medium | https://arxiv.org/abs/2309.10062 |
| ref-059 | Wang, Y. 외(DART-LLM 저자) | DART-LLM: Dependency-Aware Multi-Robot Task Decomposition and Execution using Large Language Models | 논문 | medium | https://arxiv.org/abs/2411.09022 |
| ref-166 | Obata, K., Aoki, T., Horii, T., Taniguchi, T., & Nagai, T. | LiP-LLM: Integrating Linear Programming and dependency graph with Large Language Models for multi-robot task planning | 논문 | medium | https://arxiv.org/abs/2410.21040 |
| ref-181 | Shi, G., Wu, Y., Kumar, V., & Sukhatme, G. S. | PIP-LLM: Integrating PDDL-Integer Programming with LLMs for Coordinating Multi-Robot Teams Using Natural Language | 논문 | medium | https://arxiv.org/abs/2510.22784 |
| ref-242 | Rivera, C., Byrd, G., Booker, M., Kemp, B., Gaines, A., Holmes, E., Uplinger, J., de Melo, C. M., & Handelman, D.(JHU APL·JHU·DEVCOM ARL) | FLEET: Formal Language-Grounded Scheduling for Heterogeneous Robot Teams | 논문 | medium | https://arxiv.org/abs/2510.07417 |
| ref-167 | Peng, M., Chen, Z., Yang, J., Huang, J., Shi, Z., Liu, Q., Li, X., & Gao, L. | Automatic MILP Model Construction for Multi-Robot Task Allocation and Scheduling Based on Large Language Models | 논문 | medium | https://arxiv.org/abs/2503.13813 |
| ref-168 | Kaitha, S., & Yu, S. 외(arXiv 2512.02810) | Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms | 논문 | medium | https://arxiv.org/abs/2512.02810 |
| ref-236 | Electronics(MDPI) 게재 논문(저자 미확인) | Semantic Feasibility Reasoning for Heterogeneous Multi-Robot Task Allocation | 논문 | medium | https://doi.org/10.3390/electronics15163562 |
| ref-237 | Kluge-Wilkes, A. 외(RWTH Aachen WZL) | Ontology-based task allocation for heterogeneous resources in Line-less Mobile Assembly Systems | 논문 | medium | https://www.techrxiv.org/users/685235/articles/679210-ontology-based-task-allocation-for-heterogeneous-resources-in-line-less-mobile-assembly-systems |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 국내외 물류센터에서 최근접 배정 규칙과 전역 최적화(또는 LLM 기반) 배정을 같은 조건에서 비교해 총 이동거리·처리량·납기 준수를 실측한 자료가 있는가? | 13, 4 | 열림 | — |
| new | — | ROP 가 플릿 단위로 작업을 입찰·배정하고 제조사 관제가 플릿 안에서 다시 로봇을 고르는 두 수준 배정에서 전체 최적성이 얼마나 손실되며, 이를 줄이려면 제조사 관제가 어떤 비용·상태 정보를 내야 하는가? (관련 기존 질문: oq-031) | 13, 9 | 열림 | — |
| new | — | 출하 마감·납기 같은 상위 업무 제약을 배정 목적함수(완료 시각 최소화, 비용 최소화)와 어떻게 결합하는지 정한 공개 설계나 창고 사례가 있는가? (관련 기존 질문: oq-019) | 13, 14, 1 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 피킹 | 시작 조건 | docs/categories/d-planning-and-optimization/13-task-allocation-mrta.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 13. 작업 배정 — MRTA |
| 피킹 | 작업 대상 | docs/categories/d-planning-and-optimization/13-task-allocation-mrta.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 13. 작업 배정 — MRTA |
| 피킹 | 수행 자원 | docs/categories/d-planning-and-optimization/13-task-allocation-mrta.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 13. 작업 배정 — MRTA |
| 피킹 | 제약 | docs/categories/d-planning-and-optimization/13-task-allocation-mrta.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 13. 작업 배정 — MRTA |
| 피킹 | 예외·성과 | docs/categories/d-planning-and-optimization/13-task-allocation-mrta.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 13. 작업 배정 — MRTA |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| rmf_task (Open-RMF 작업 계획기 TaskPlanner) | 오픈소스 | Open Robotics (open-rmf) | 13, 14, 16 | ref-660 | https://github.com/open-rmf/rmf_task |

## 추가 조사 요청

- 5절 완료·인계 칸: 배정 결과가 작업 완료·재고 변경 확인으로 이어지는 기준(12. 명령·작업 실행의 신뢰성과의 경계)에 관한 근거가 브리프에 없어 '해당 없음'으로 두었다. 배정 이후 완료 인정 조건을 다룬 자료 조사가 필요하다.
- 3·8절: 창고(물류센터) 현장에서 최근접 배정과 최적화·LLM 배정을 같은 조건에서 비교한 실측 자료가 없다. 한국어·영어로 추가 조사가 필요하다.
- 11절 oq-030: LTAA(arXiv 2512.02810) 원문을 열어 완료율 비교 결과를 확인해야 출처 충돌을 해소할 수 있다.
- 6절: 문헌 검토(ref-152)의 검토 편수·계열 구분·플릿 규모 수치와 Merschformann 외(ref-653)의 정량 결과는 원문 열람 후에만 쓸 수 있다.
- 8절: ref-651·ref-652·ref-654 는 검증자 재검색 없이 실재를 판단했으므로 다음 실행에서 서지(게재 연도 포함) 재확인이 필요하다.
- 8절 국내 자료: 국내 물류센터의 실제 로봇 배정 규칙 운영 사례와 ref-657·ref-658 의 저자·수행기관·발행연도 확인이 필요하다.
- 트랙 반영 제안 중 COHERENT(ref-169)·LaMMA-P(ref-164)·IMR-LLM(ref-170)과 SMART-LLM 벤치마크 구성은 이번 브리프에 없어 반영하지 못했다. 재확인 후 6·8절 반영을 검토한다.

## 이행한 수정 지시

- f16 강등 — 6절 첫 단락에서 [추정]으로 쓰고 편수·계열 수·중앙집중·플릿 규모 수치를 빼고 '미확인'으로 명시했다.
- f12 결과 문장 — 3절·8절에서 '작업장 사례 연구에서 앞으로의 운반 요청을 고려한 조합 최적화 배차가 무작위·최근접 규칙보다 작업 대기 시간을 더 잘 통제했다고 저자가 보고했다'로 좁혀 썼다.
- f18 — 2단계 방법 서술을 삭제하고 6절에 배정과 충전 결정의 결합만 쓰며 배터리 열화 모델은 16. 공용 자원·충전·에너지 최적화로 넘겼고, ref-659 기관 표기를 각주·reference_updates 에서 'Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin)'로 고쳤다.
- f13 — 8절 본문과 ref-653 각주에 'arXiv 2018-01 공개, Operations Research Perspectives 2019 게재, 이산 사건 시뮬레이션 조건'을 병기하고 3절에서 용어집의 '로봇 이동형 풀필먼트 시스템(RMFS)'을 링크해 썼다.
- f14 — 6·8절에서 저자·발행연도를 '미확인'으로 두고 시뮬레이션 설계 연구임을 병기했으며, 10절에서 f13·f14 시뮬레이션을 22. 시뮬레이션·예측용 디지털 트윈의 가정한 미래 실험 도구로만 연결하고 8. 실시간 세계 상태·데이터 일관성과 연결하지 않았다.
- f11 — 6절에서 '토큰을 받은 에이전트가 가까운 미배정 작업을 스스로 맡는다' 수준으로만 쓰고 세부 조건은 서술하지 않았다.
- f2 — 4·6절에서 복잡도 차수를 쓰지 않고 '다항 시간'까지만 썼다.
- 원문 미열람 표기 — fetched=false 출처 전체의 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었으며, ref-656·ref-660·ref-031 에는 붙이지 않았다.
- 트랙 반영 범위 — SMART-LLM 난이도 벤치마크, COHERENT·LaMMA-P·IMR-LLM 을 6·8절에 넣지 않고 additional_research_requests 로 돌렸다.
- f22·oq-030 — LTAA 완료율 수치를 본문에 쓰지 않고 11절에 oq-030 을 두 보고를 모두 언급한 '출처 충돌 미해소'로 유지했다.
- 교차 규칙 — f17 과 f19~f22·f28 을 6절(학습 기반 배차, LLM 기반 배정)에 두고 10절에서 27. AI·학습·적응과 모델 운영과의 양쪽 연결을 명시했다.
- f25·f26·f28 은 [추정]으로 쓰고 f26 은 '분담이 가능할 것으로 보인다' 수준을 유지했으며, f27 은 9절에 '연계 대상: '으로 짧게 두었다.
- 열린 질문 — 11절과 open_question_updates 에서 새 질문 3에 oq-019, 새 질문 2에 oq-031 을 함께 적고, 새 질문 1은 트랙 백로그 q3-05 에 링크만 두었으며, oq-024 는 f23 과 함께 열림 상태로 유지했다.
- f9 — 5·7절에서 recharge_threshold 0.10 이 템플릿 설정의 예시값임을 밝혔다.
- 용어집 — 헝가리안 방법·시장 기반 작업 배정·합의 기반 번들 알고리즘(CBBA)·최근접 차량 우선 규칙 4건을 related_areas [13] 으로 glossary_updates 에 냈고, 본문에서 RMFS·MRTA·MAPD·MILP 기존 용어 페이지를 링크했다.
- 분량 초과 자동 분리: 13. 작업 배정 — MRTA 본문 8,497자 > 기준 4,000자 → 4개 절을 주제 페이지로 옮김, 남은 본문 3,933자
- 형식 수정: docs/topics/2026/2026-09-25-area13-s6.md 의 깨진 링크 두 개를 주제 페이지 위치 기준 경로(../../categories/g-safety-security-intelligence-and-governance/27-ai-learning-adaptation-and-model-operations.md, ../../categories/d-planning-and-optimization/16-shared-resource-charging-and-energy-optimization.md)로 고쳤다. 주장·태그·각주는 바꾸지 않았다.
