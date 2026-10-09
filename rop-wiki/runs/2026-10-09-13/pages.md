# 스토리텔러 산출 2026-10-09-13

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/design-and-simulation/scenario-model-and-editing.md | draft | 차등 갱신: 3절 면담 근거 추가, 5절 물류창고 경진대회 사례 추가·문장 교체, 6·7·8·10절 요약 덧붙임과 2026-09-30 주제 페이지 링크 복원, 9절 판 관리 문장 정정, 11절 첫 문장 건수 정정·진행 현황, 13절 각주 11건 추가, related_areas 에 57·61 추가, last_run 2026-10-09 (2차 수정 5건 반영) |
| create | docs/topics/2026/2026-10-09-area33-s6.md | draft | 자동 분리: 33. 시나리오 모델·편집 의 "6. 대표 접근법과 기술" 절(2,409자)을 옮겼다 |
| create | docs/topics/2026/2026-10-09-area33-s8.md | draft | 자동 분리: 33. 시나리오 모델·편집 의 "8. 대표 연구와 자료" 절(1,827자)을 옮겼다 |
| create | docs/topics/2026/2026-10-09-area33-s10.md | draft | 자동 분리: 33. 시나리오 모델·편집 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,294자)을 옮겼다 |
| create | docs/topics/2026/2026-10-09-area33-s11.md | draft | 자동 분리: 33. 시나리오 모델·편집 의 "11. 열린 질문" 절(1,273자)을 옮겼다 |
| create | docs/topics/2026/2026-10-09-area33-s7.md | draft | 자동 분리: 33. 시나리오 모델·편집 의 "7. 관련 표준·프레임워크·오픈소스" 절(996자)을 옮겼다 |
| create | docs/topics/2026/2026-10-09-area33-s3.md | draft | 자동 분리: 33. 시나리오 모델·편집 의 "3. 왜 중요한가" 절(589자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-10-09 | 33. 시나리오 모델·편집 | 갱신: 5절 물류창고 경진대회 사례 추가, 9절 시나리오 판 관리 문장 정정, Open-RMF Site Editor 전환·OpenSCENARIO 2 로봇 재사용·RoboVAST 반영, 1차 조건부 승인 수정 15건·2차 수정 5건 반영(2026-09-30 주제 페이지 링크 복원, 11절 건수 정정) | run 2026-10-09-13
- 홈 최근 업데이트: 2026-10-09 — 33. 시나리오 모델·편집: 물류창고 경진대회 시나리오 사례 추가, 시나리오 판 이전 규칙(OpenSCENARIO XML)과 로봇 형식 미확인을 9절에 정정 반영
- 대분류 최근 업데이트: 2026-10-09 — 33. 시나리오 모델·편집: 3·5·6·7·8·9·10·11절 차등 갱신(League of Robot Runners 물류창고 사례, Open-RMF Site Editor 전환, OpenSCENARIO 2 로봇 재사용, RoboVAST 인스턴스 기록)
- 세부영역 최근 업데이트: 2026-10-09 — 33. 시나리오 모델·편집: 갱신(차등) — 5절 물류창고 사례(경진대회 벤치마크) 추가, 9절 판 관리 문장 정정, 6·7·8·10·11절 요약 덧붙임과 2026-09-30 주제 페이지 링크 복원, 각주 11건 추가, 1차 수정 15건·2차 수정 5건 반영

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 데이터 출처 추적 | Data Provenance (W3C PROV) | 어떤 산출물이 어떤 입력·설정·실행·주체로부터 만들어졌는지를 기계가 읽을 수 있는 관계로 기록하는 일로, W3C PROV 가 그 표준 데이터 모델이며 시뮬레이션 시험의 재현성 확보에 쓰인다. | 33, 54, 57 | ref-1515 |
| new | 추상 시나리오·구체 시나리오 | Abstract Scenario / Concrete Scenario | 매개변수와 변형 범위만 정한 시나리오(추상)와 모든 값이 하나로 정해져 바로 실행할 수 있는 시나리오 인스턴스(구체)를 구분하는 말로, 시험 도구가 추상 시나리오를 여러 구체 시나리오로 펼쳐 실행한다. | 33, 54 | ref-1515, ref-1512 |
| new | 엄격 스키마 | Strict Schema (deprecated elements removed) | 형식의 판에서 폐기 예정 요소를 뺀 검증용 스키마로, 기존 시나리오 파일을 이 스키마로 검사해 다음 판에서 사라질 요소를 찾아 바꾸게 한다(ASAM OpenSCENARIO XML). | 33, 57 | ref-1511 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-482 | Open-RMF (open-rmf/rmf_site) | rmf_site — RMF Site Editor (README) | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_site |
| ref-1510 | Open Robotics Discourse (Open-RMF 상호운용 그룹, 작성자 grey) | Interoperability Interest Group June 6, 2024: Preview of the RMF Site Editor | 오픈소스 문서 | medium | https://discourse.openrobotics.org/t/interoperability-interest-group-june-6-2024-preview-of-the-rmf-site-editor/38070 |
| ref-1511 | ASAM e.V. | ASAM OpenSCENARIO XML v1.4.0 — 5 Backward compatibility | 표준 | high | https://openscenario.asam.net/ASAM_OpenSCENARIO_XML/v1.4.0/05_backward_compatibility/01_backward_compatibility.html |
| ref-1512 | Pasch, F., Mirus, F., Zhang, Y., & Scholl, K.-U. (Intel Labs 외, arXiv) | Scenario Execution for Robotics: A generic, backend-agnostic library for running reproducible robotics experiments and tests | 논문 | medium | https://arxiv.org/abs/2409.07080 |
| ref-1513 | Elmaaroufi, K., Shanker, D., Cismaru, A., Vazquez-Chanlatte, M., Sangiovanni-Vincentelli, A., Zaharia, M., & Seshia, S. A. (COLM 2024, arXiv) | ScenicNL: Generating Probabilistic Scenario Programs from Crash Reports | 논문 | medium | https://arxiv.org/abs/2405.03709 |
| ref-1514 | Jiang, H., Zhang, Y., Veerapaneni, R., & Li, J. (SoCS 2024, arXiv) | Scaling Lifelong Multi-Agent Path Finding to More Realistic Settings: Research Challenges and Opportunities | 논문 | high | https://arxiv.org/abs/2404.16162 |
| ref-1515 | Ortega, A., Wiest, S., Pasch, F., & Hochgeschwender, N. (arXiv, ERAS 2026 채택) | Replicable Simulation-Based Robot Validation through Provenance | 논문 | medium | https://arxiv.org/abs/2605.29973 |
| ref-1516 | Ortega, A., Parra, S., Schneider, S., & Hochgeschwender, N. (Frontiers in Robotics and AI 11) | Composable and executable scenarios for simulation-based testing of mobile robots | 논문 | high | https://pmc.ncbi.nlm.nih.gov/articles/PMC11327003/ |
| ref-1517 | NVIDIA | Isaac Sim Documentation — Warehouse Creator Extension | 벤더 문서 | medium | https://docs.isaacsim.omniverse.nvidia.com/latest/assets/asset_utilities/ext_omni_warehouse_creator.html |
| ref-1518 | ros2_fault_injection 프로젝트 (Read the Docs) | ros2_fault_injection documentation | 오픈소스 문서 | medium | https://ros2-fault-injection.readthedocs.io/ |
| ref-1519 | Sánchez de la Fuente, S., Prieto López, L., González Santamarta, M. Á., Matellán Olivera, V. 외 (Universidad de León, WAF 2025) | Scenario Generation for Robot Simulation from Public Data | 논문 | medium | https://portalcientifico.unileon.es/documentos/6972798ce66b2902147b1aeb |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | RoboVAST 처럼 추상 시나리오를 구체 인스턴스로 해석하고 실행마다 출처를 기록하는 방식을 여러 제조사 로봇 플릿과 승강기·문 같은 설비가 함께 있는 다중 로봇 시나리오에 적용한 사례가 있는가? | 33, 54 | 열림 | — |
| new | — | Open-RMF Site Editor 의 현장 형식이 기존 traffic-editor 의 .building.yaml 을 대체하는가, 그리고 기존 건물 파일을 옮기는 공식 변환 도구나 판 이전 규칙이 있는가? | 33, 15 | 열림 | — |
| new | — | OpenSCENARIO 2 DSL 로 다중 로봇 플릿의 작업 배정과 승강기·문 같은 설비 사건을 기술할 수 있는가, 기술하려면 어떤 확장 라이브러리가 필요한가? | 33, 22 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 물류창고 | 시작 조건 | docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시 | 33. 시나리오 모델·편집 |
| 물류창고 | 작업 대상 | docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시 | 33. 시나리오 모델·편집 |
| 물류창고 | 수행 자원 | docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시 | 33. 시나리오 모델·편집 |
| 물류창고 | 제약 | docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시 | 33. 시나리오 모델·편집 |
| 물류창고 | 예외·성과 | docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시 | 33. 시나리오 모델·편집 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| Scenario Execution for Robotics (OpenSCENARIO 2 기반 로봇 시나리오 실행 라이브러리) | 오픈소스 | Pasch, F. 외 (Intel Labs 외) | 33, 54 | ref-1512 | https://arxiv.org/abs/2409.07080 |
| RoboVAST (출처 기록 기반 시뮬레이션 시험 틀) | 프레임워크 | Ortega, A., Wiest, S., Pasch, F., & Hochgeschwender, N. | 33, 54, 57 | ref-1515 | https://arxiv.org/abs/2605.29973 |

## 추가 조사 요청

- 9절·11절(oq-234): 로봇 시뮬레이션 형식(SDFormat·Open-RMF 건물 파일·Site Editor 형식)에서 개별 시나리오 인스턴스를 형식 판 사이에서 옮기는 규칙이나 변환 도구가 있는지 — 현재 판 이전 규칙은 도로 교통 표준에서만 확인됐다.
- 6절·11절(oq-233 및 새 질문): 기존 .building.yaml 을 Site Editor 형식으로 옮기는 공식 방법과 Site Editor 저장 형식의 판 규칙 — 편집기 전환에 따른 환경 참조 이전 규칙을 서술하는 데 필요하다.
- 5절(oq-236): 실제 물류창고 현장의 시나리오 예제·템플릿과 국내 다중 로봇 시나리오 예제 라이브러리 — 현재 물류창고 사례는 경진대회 벤치마크뿐이다.
- 5절: League of Robot Runners 공식 사이트·2024 대회 자료로 지도 규모·작업 발생 규칙(f19·f20)을 교차 확인 — 현재 우승 팀 논문 단일 출처이며 Sortation 정점 수가 논문 안에서 두 값으로 적혀 있다.
- 11절(oq-135): 로봇 작업 시나리오 구성에서 되물어야 할 항목의 표준 질문 목록 — 이번 실행에서 조사하지 않았다.
- 예산으로 미룸: 주제 페이지 docs/topics/2026/2026-09-30-area33-s7.md 표에 Site Editor·Scenario Execution·RoboVAST·ros2_fault_injection·League of Robot Runners 행 추가(1차 수정 지시로 이번 실행에서 주제 페이지를 갱신하지 않음).
- 참고문헌 정리: ref-1516(PMC URL)과 ref-1134(Frontiers URL)가 같은 논문(Ortega 외, Frontiers in Robotics and AI, 2024-08-02)을 가리키므로 병합 여부 확인이 필요하다.
- 파이프라인 담당: 분량 자동 분리 코드가 이미 분리된 절을 다시 분리할 때 기존 '자세한 내용은 주제 페이지 …' 링크 줄을 버린다. 이번 재실행에서는 각 절 append 첫 줄에 다른 문구의 2026-09-30 주제 페이지 링크를 넣어 대응했으나, 분리 코드가 기존 링크를 보존하도록 고칠 것을 요청한다.

## 이행한 수정 지시

- ref-1512 기관 표기 — 13절 각주와 reference_updates 의 org 를 '(Intel Labs 외, arXiv)'로 고치고, 6·8절 본문에서도 'Pasch 외(Intel Labs 외)'로만 써서 Intel Labs 연구진으로 단정하지 않았다.
- f11 — 6절에 '…Twist·트리거 서비스·점군 장애 유형을 두고 문서에 단언(assertion)과 pluginlib 기반 주입기 팩토리 절을 둔다' 수준으로 좁힌 문장을 [사실]로 썼고, ref-1518 각주 발행일은 '미확인'으로 두었다.
- f19 — 5절 물류창고 사례 작업 대상 칸에 Sortation 정점 수를 '54,320개 — 논문 표 1 기준; 같은 논문 그림 설명은 54,230개'로 병기했다.
- f21 — '만' 한정을 빼고 '바닥·벽·기둥 같은 건물 요소를 생성한다고 설명하고, 문서에 로봇·랙 배치에 관한 설명은 없다'로 고쳤으며 [추정] 벤더 주장 병기를 유지했다.
- f21 — 5절 물류창고 사례의 여섯 항목 표 칸에는 쓰지 않고 사례 아래 설명문 한 단락에만 [추정] 벤더 주장과 함께 짧게 언급했다.
- f22 — ''만약 ~였다면' 시나리오를 탐색하게 했다' 구절을 빼고 8절에서 나머지만 [사실]로 썼다.
- 5절 — 사례 제목과 사례 아래 문장에 '경진대회 벤치마크 시나리오이며 실제 물류창고 배치가 아니다'를 밝히고, Moving AI 격자 지도를 7절에 둔 판단과의 차이를 '작업 발생 규칙(목표 도달 시 새 목표 1개 배정)과 계획 시간 제한을 갖춘 경진대회 시나리오' 기준으로 설명했으며, 기존 문장을 '실제 물류창고 현장의 시나리오 예제와 국내 자료는 여전히 찾지 못했다'로 바꿨다.
- 9절 — '개별 시나리오 인스턴스의 버전 관리 방식은 공개 자료에서 찾지 못했다' 문장을 f1·f2 의 OpenSCENARIO XML 판별 호환 선언·이전 스크립트·엄격 스키마 [사실] 두 문장과 f3·f6 [추정] 문장으로 나눠 다시 썼고, '로봇 시뮬레이션 형식(SDFormat·Open-RMF 건물 파일)의 같은 규칙은 아직 확인하지 못했다' 단서를 남겼으며 oq-234 는 열린 채로 두었다.
- 9절 표 — 업종별 조건 행의 'ROP가 직접 맡는 것' 칸에 OpenSCENARIO 2 를 '로봇 시나리오의 과제·사건 기술 언어 후보'로 [추정]으로만 쓰고 두 근거 연구가 공동 저자를 공유해 독립 확인이 아님을 적었으며, 표준 자체(ASAM 관리)는 '외부와 연계하는 것' 칸에 두었다.
- f9·f11·f12 — 6절 요약에서 '시나리오에 장애를 매개변수로 선언하는 방식의 예'로만 쓰고 센서·메시지 수준 장애 주입은 로봇 자체 지능·제어 쪽 연계 대상이라 ROP가 직접 만들지 않는다고 밝혔으며, 10절 54. 시험·형식 검증·벤치마크 연결에서도 같은 단서를 두었다.
- 3절 — f13 을 [사실]로 덧붙이며 면담 대상이 이동로봇 시뮬레이션 시험 일반의 도메인 전문가 14명임을 밝혔고, 기존 종합 문장의 [추정] 태그는 그대로 두었다.
- 분할된 절(6·7·8·10·11)은 영역 페이지 해당 절에 append 패치로만 요약을 더했고, 기존 주제 페이지 2026-09-30-area33-s6·s7·s8·s10·s11 은 갱신하지 않았으며 s7 표 행 추가는 additional_research_requests 에 다음 실행 후보로 넘겼다.
- 11절 — oq-234(f3·f6)·oq-233(f10·f18)은 부분 근거, oq-235(f12)·oq-131(f23)·oq-236(국내 자료 없음)은 미해결로 적고 oq-135 는 이번 실행에서 조사하지 않았다고 밝혔으며, 해결 처리와 open_question_updates 의 상태 변경은 하지 않았다.
- ref-1088·ref-1086·ref-116 — 13절의 기존 각주 줄(접근일 2026-09-30)을 그대로 두고 접근일을 바꾸지 않았으며, reference_updates 에는 넣지 않았다.
- ref-1515 각주 발행일을 2026-05-28(v1)로 적고 기관 표기에 'ERAS 2026 채택'을 병기했으며, ref-1511 각주 발행일은 '미확인'으로 두었다.
- 2차: 기존 주제 페이지 링크 복원 — 3·6·7·8·10절 append 패치 첫 줄과 11절 replace 본문 둘째 단락에 '2026-09-30 실행까지 정리한 내용은 [33. 시나리오 모델·편집 — … (2026-09-30)](../../topics/2026/2026-09-30-area33-sN.md)에 있다' 형식으로 2026-09-30-area33-s3·s6·s7·s8·s10·s11 링크를 하나씩 넣었다(7절은 Moving AI MAPF 벤치마크·VDMA 레이아웃 교환 형식이 그 표에 있음을 함께 밝혀 5절 끝 안내의 근거를 이었다). 링크는 영역 페이지와 분리 주제 페이지 어느 쪽에 놓여도 맞도록 ../../topics/… 형식으로 썼다.
- 2차: 11절 — replace 로 첫 문장을 '이번 실행 전 이 영역에 걸린 열린 질문은 8건이고, 이번 실행(2026-10-09-13)에서 3건을 새로 올렸으며 해결 처리한 질문은 없다'로 고쳤다(입력 열린 질문 목록 기준).
- 2차: 10절 — '이 변환은 언어 모델을 쓰므로 … 44. 로봇 기반 모델·언어 모델 계획과도 이어진다. [사실]'을 'ScenicNL 은 여러 대규모 언어 모델 프롬프트를 컴파일러·시뮬레이터와 엮는다. [사실][^ref-1513]'과 '그래서 이런 기록 변환 방식은 … 44. 로봇 기반 모델·언어 모델 계획과도 이어질 것으로 보인다. [추정][^ref-1513]' 두 문장으로 나눴다.
- 2차: 절 번호 참조 — 6절의 '8절에 정리했다', 8절의 '면담 근거는 3절에 있다'·'6절에 요약했다'·'5절 물류창고 사례의 근거다', 10절의 '(9절)'·'(5절)', 11절의 '(9절)'을 모두 '원 페이지 [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md)의 <절 번호와 절 이름>' 형식으로 고쳤고, 같은 유형인 7절 표의 '5절 물류창고 사례' 표기도 같은 형식으로 맞췄다.
- 2차: last_run — 3절 patch 의 frontmatter 에 last_run: 2026-10-09 를 넣었다.
- 분량 초과 자동 분리: 33. 시나리오 모델·편집 본문 14,129자 > 기준 4,000자 → 6개 절을 주제 페이지로 옮김, 남은 본문 6,692자
