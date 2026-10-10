# 스토리텔러 산출 2026-10-10-02

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/planning-and-optimization/task-allocation-mrta.md | draft | 5·6·7·8·9·11·13절 차등 갱신(병원 모사 계산 실험 사례, 문헌 검토 다섯 계열, LTAA 원문 수치, BidProposal 다섯 필드·rmf_fleet_adapter 2.14.0, 2024~2026 연구 3건, 새 열린 질문 4건, 각주 정정). 2차 수정: 6·7·8·11절을 replace 로 바꿔 첫 문단에 2026-09-25 주제 페이지 링크를 넣고 8절 첫 문단을 링크 대상과 맞췄으며, 분리 뒤 오해되는 'n절' 참조를 세부영역 페이지 절 이름 참조로 바꿈 |
| create | docs/topics/2026/2026-10-10-area25-s6.md | draft | 자동 분리: 25. 작업 배정 — MRTA 의 "6. 대표 접근법과 기술" 절(2,917자)을 옮겼다 |
| create | docs/topics/2026/2026-10-10-area25-s11.md | draft | 자동 분리: 25. 작업 배정 — MRTA 의 "11. 열린 질문" 절(1,653자)을 옮겼다 |
| create | docs/topics/2026/2026-10-10-area25-s8.md | draft | 자동 분리: 25. 작업 배정 — MRTA 의 "8. 대표 연구와 자료" 절(1,232자)을 옮겼다 |
| create | docs/topics/2026/2026-10-10-area25-s7.md | draft | 자동 분리: 25. 작업 배정 — MRTA 의 "7. 관련 표준·프레임워크·오픈소스" 절(814자)을 옮겼다 |
| create | docs/topics/2026/2026-10-10-area25-s10.md | draft | 자동 분리: 25. 작업 배정 — MRTA 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(723자)을 옮겼다 |
| create | docs/topics/2026/2026-10-10-area25-s3.md | draft | 자동 분리: 25. 작업 배정 — MRTA 의 "3. 왜 중요한가" 절(438자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-10-10 | 25. 작업 배정 — MRTA | 5·6·7·8·9·11·13절 차등 갱신(병원 모사 계산 실험 사례, 문헌 검토 다섯 계열, LTAA 원문 수치와 oq-030 부분 근거, Open-RMF 입찰 제안 필드·rmf_fleet_adapter 2.14.0, 2024~2026 배정 연구 3건, 새 열린 질문 4건), 1차 수정 지시 23건·2차 수정 지시 2건(이전 주제 페이지 링크 복원, 절 상호참조 명시) 이행 | run 2026-10-10-02
- 홈 최근 업데이트: 2026-10-10 — 25. 작업 배정 — MRTA: 병원 모사 환경의 계산 실험 사례, 문헌 검토의 다섯 계열, LTAA 원문 수치(oq-030 부분 근거), Open-RMF 입찰 제안 필드, 2024~2026 배정 연구 3건을 더했다
- 대분류 최근 업데이트: 2026-10-10 — 25. 작업 배정 — MRTA: 마감·용량 제약 배정(SMT), 혼잡 반영 대규모 배정(MRTA-RM, 최소 비용 흐름), 두 수준 배정에서 플릿이 내는 입찰 정보와 한계를 갱신했다
- 세부영역 최근 업데이트: 2026-10-10 — 25. 작업 배정 — MRTA: 5·6·7·8·9·11절 차등 갱신(병원 모사 계산 실험 사례, 문헌 검토 계열, LTAA 원문 수치, BidProposal 다섯 필드, 2024~2026 연구 3건, 새 열린 질문 4건, 2026-09-25 주제 페이지 링크 유지)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 최소 비용 흐름 | Minimum-Cost Flow | 간선마다 용량과 단위 비용이 있는 네트워크에서 정해진 양의 흐름을 출발점에서 도착점으로 보낼 때 총비용이 가장 작은 흐름을 찾는 최적화 문제로, 대규모 작업 배정을 그래프 위에서 푸는 데 쓰인다. | 25, 27 | ref-1457 |
| new | 이론 모듈로 만족 가능성 | Satisfiability Modulo Theories (SMT) | 산술·비트벡터·미해석 함수 같은 이론을 포함한 논리식이 참이 되도록 하는 값이 있는지 판정하는 문제와 그 풀이 기법으로, 마감·용량 같은 제약을 모두 만족하는 배정 계획을 찾는 데 쓰인다. | 25 | ref-1454 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-152 | Meseguer Valenzuela, A., & Blanes Noguera, F. | Task Allocation in Mobile Robot Fleets: A review | 논문 | medium | https://arxiv.org/abs/2501.08726 |
| ref-168 | Kaitha, S. p. r., & Yu, H. (Virginia Tech; arXiv 2512.02810) | Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms | 논문 | medium | https://arxiv.org/abs/2512.02810 |
| ref-404 | Open Robotics (open-rmf) | rmf_task — README | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_task |
| ref-1453 | Open Robotics (open-rmf/rmf_internal_msgs) | rmf_internal_msgs — rmf_task_msgs/msg/BidProposal.msg | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/BidProposal.msg |
| ref-1454 | Tuck, V. M., Chen, P.-W., Fainekos, G., Hoxha, B., Okamoto, H., Sastry, S. S., & Seshia, S. A. (arXiv 2403.11737, NFM 2024 게재 예정) | SMT-Based Dynamic Multi-Robot Task Allocation | 논문 | medium | https://arxiv.org/html/2403.11737v1 |
| ref-1455 | Lee, S., Sim, J., & Nam, C. (arXiv 2506.07293) | Very Large-scale Multi-Robot Task Allocation in Challenging Environments via Robot Redistribution | 논문 | medium | https://arxiv.org/html/2506.07293 |
| ref-1456 | Lee, S. 외 (SeBin-Lee-SG GitHub) | MRTA-RM_public — README | 오픈소스 문서 | medium | https://github.com/SeBin-Lee-SG/MRTA-RM_public |
| ref-1457 | Zhang, Y., Chen, Z., Harabor, D., Le Bodic, P., & Stuckey, P. J. (AAMAS 2026, IFAAMAS) | Flow-Based Task Assignment for Large-Scale Online Multi-Agent Pickup and Delivery | 논문 | high | https://www.ifaamas.org/Proceedings/aamas2026/pdfs/MQIK8423.pdf |
| ref-1398 | Open Robotics (open-rmf/rmf_ros2) | rmf_ros2 — rmf_fleet_adapter/CHANGELOG.rst (2.14.0) | 오픈소스 문서 | high | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 서로 다른 제조사 관제가 낸 입찰 비용이 같은 시간·금액 단위와 같은 계산 범위를 뜻하도록 정규화하는 공개 규칙이 있는가? (관련 기존 질문: oq-053, oq-082) | 25, 20 | 열림 | — |
| new | — | 플릿이 입찰에서 밝힌 예상 수행 로봇과 실제 수행 로봇이 달라질 때 비용·완료 시각을 언제 다시 평가해야 하는가? | 25, 20 | 열림 | — |
| new | — | LTAA 의 결정적 비교군(brute force·greedy·DP)과 확률적 비교군(LTAA·Q-learning·DQN)을 같은 성공 확률 모델과 작업 집합으로 재평가한 공개 재현 자료가 있는가? (관련 기존 질문: oq-030) | 25, 47 | 열림 | — |
| new | — | 최소 비용 흐름 기반 배정에 이종 로봇의 능력·적재량·충전 제약을 더해도 대규모 계산 성능이 유지되는가? | 25, 28 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 병원 | 시작 조건 | docs/categories/planning-and-optimization/task-allocation-mrta.md#5-적용-사례-현장-유형-명시 | 25. 작업 배정 — MRTA (병원 모사 환경 계산 실험) |
| 병원 | 수행 자원 | docs/categories/planning-and-optimization/task-allocation-mrta.md#5-적용-사례-현장-유형-명시 | 25. 작업 배정 — MRTA (병원 모사 환경 계산 실험) |
| 병원 | 제약 | docs/categories/planning-and-optimization/task-allocation-mrta.md#5-적용-사례-현장-유형-명시 | 25. 작업 배정 — MRTA (병원 모사 환경 계산 실험) |
| 병원 | 예외·성과 | docs/categories/planning-and-optimization/task-allocation-mrta.md#5-적용-사례-현장-유형-명시 | 25. 작업 배정 — MRTA (병원 모사 환경 계산 실험) |
| 물류창고 | 제약 | docs/categories/planning-and-optimization/task-allocation-mrta.md#5-적용-사례-현장-유형-명시 | 25. 작업 배정 — MRTA |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| Open-RMF 입찰 제안 메시지(rmf_internal_msgs의 rmf_task_msgs BidProposal) | 오픈소스 | Open Robotics (open-rmf) | 25, 20 | ref-1453 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/BidProposal.msg |

## 추가 조사 요청

- 6절·8절(문헌 검토 ref-152): 원문이 검토 대상을 고른 절차와 편수(검증 노트상 Google Scholar 1440건 중 52편)는 이번 브리프의 finding 이 아니어서 본문에 넣지 않았다. 다음 25. 작업 배정 — MRTA 실행에서 finding 으로 확인해 달라.
- 주제 페이지 docs/topics/2026/2026-09-25-area13-s6.md·2026-09-25-area13-s7.md·2026-09-25-area13-s8.md·2026-09-25-area13-s11.md 는 이번 입력에 없어 고치지 못했다. 그 페이지에 남아 있을 수 있는 '문헌 검토 계열·플릿 규모 미확인' 문장, ref-152·ref-168 의 옛 각주(저자 Yu, S., 원문 미열람), LTAA 출처 충돌 서술을 이번 내용과 맞추려면 다음 갱신 실행 입력에 해당 주제 페이지를 넣어 달라.
- 트랙 반영 제안 16건(data/area_reflection_proposals.json, 최근접 대 MILP 비교 Choe 외 포함)은 이번 브리프의 finding 이 아니어서 반영하지 않고 '제안' 상태로 남겼다. 다음 25. 작업 배정 — MRTA 실행에서 원문 확인과 함께 다뤄 달라.
- 2절 핵심 질문(가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가?)에 답할 물류창고·다른 현장 유형의 실측 비교 자료(oq-052)와 국내 자료가 이번에도 없다. 한국어 검색을 포함한 조사가 필요하다.
- 5절 병원 모사 사례의 작업 대상(물품 종류)과 완료·인계(수령 확인) 조건, 그리고 실제 병원 배송 로봇의 배정 운영 사례가 없어 '미확인'으로 두었다.
- pipeline 담당 확인 요청: 자동 분리 코드가 append 패치 뒤 절에서 '자세한 내용은 주제 페이지'로 시작하는 기존 링크 줄을 지워 이전 주제 페이지로 가는 링크가 사라졌다(2차 검증 지적). 이번에는 6·7·8·11절을 replace 로 바꿔 첫 문단 둘째 문장에 이전 주제 페이지 링크를 넣어 우회했다. 분리 코드가 기존 링크 줄을 보존하도록 고치거나 이 규칙을 storyteller.md 에 명시해 달라.

## 이행한 수정 지시

- f4·f6 판 표기 — 6절과 11절에서 76%·Heavy Excels 77%·전통 기법 모두 우위 서술마다 'arXiv PDF v1 초록 기준'을 밝혔다.
- f4~f6 조건 병기 — 6절·11절의 LTAA 수치(75.97%·73%·77%·77.1%·0.77·0.81·0.95)를 담은 모든 문장에 '저자 보고, TEACh 데이터셋 건설 작업 실험 조건, 현장 실측 아님'을 붙였다.
- oq-030 — 11절에서 상태를 열림으로 두고 초록의 Heavy Excels 우위 표현(f6)과 본문의 DP 0.95 비교 제외(f5)를 각각 [사실]로 제시했으며, f7 은 '이 위키의 의견' [의견]으로 충돌 원인 설명으로만 썼다.
- 의견·추정 주체 표시 — f3·f7·f11·f14·f17·f20·f26 의 [의견] 문장에 '이 위키의 의견', f9·f24 의 [추정] 문장에 '이 위키의 종합'을 밝혔다.
- 6절 문헌 검토 문장 — 기존 '검토 편수·계열 구분·실험 플릿 규모 미확인' [추정] 문장을 지우고 f1(다섯 계열)·f2(표 I~V 의 열)로 바꿨으며, 플릿 규모는 본문 25대·표 I 45대·표 IV 3~48대만 근거로 들어 한 수치로 요약하지 않았고 검토 편수는 언급하지 않고 추가 조사 요청으로 넘겼다.
- f8·f9 — 7절에는 f8 만 [사실]로 두고, 9절·11절의 f9 는 [추정]으로 두며 두 출처가 같은 Open-RMF 프로젝트 자료라 독립 교차 확인이 아님을 문장에 밝혔고 oq-053 은 부분 근거로만 연결했다.
- f10·f11 — 6절·9절에서 TaskPlanner 최적 배정이 '한 플릿의 주어진 작업 집합'에 한정된다고 적고, Zhang 외의 단발 배정 최적 서술은 TaskPlanner 의 성질로 쓰지 않았다(f11 은 범위 해석에 관한 의견으로만 9절에 둠).
- f12·f14 — 5절 물류창고 표 제약 행의 '출하 마감을 배정 목적함수에 넣는 방법은 미확인이다' 문장을 그대로 두고, 병원 모사 연구의 마감 필수 제약 정식화([사실], f12)와 창고 출하 마감 연동 사례 미확인([의견], f14)을 덧붙였으며 oq-054 는 열림으로 두었다.
- f15~f17 — 5절에 현장 유형 '병원' 사례를 더하고 사례 제목에 '병원 모사 환경의 계산 실험(그래프 추상화 벤치마크)'을 밝혔으며, 시작 조건(f16)·수행 자원(f15)·제약(f12)·예외·성과(f17)만 채우고 작업 대상·완료·인계는 '미확인'으로 두었고 실증·운영 사례로 쓰지 않았다.
- site_matrix_updates — 병원 칸 네 항목(시작 조건·수행 자원·제약·예외·성과)을 site_type '병원', link 대상 세부영역 페이지 5절 앵커, title '25. 작업 배정 — MRTA (병원 모사 환경 계산 실험)'으로 냈다.
- f13 — 6절·5절·8절에서 건전·완전성을 '논문의 모델·인코딩 가정(사용 솔버의 건전·완전성, D=D_max 조건) 아래의 결과'로 적고 최소 이동 비용 최적해를 보장하지 않는다고 썼으며, 국소 경로 계획·충돌 회피는 하위 계획기(연계 대상) 몫으로 밝혔다.
- f18~f24 — 6절에서 배정 비용에 환경 구조·혼잡을 반영하는 부분만 쓰고 경로·충돌·교착 처리는 27. 다중 로봇 경로·교통 관리 — MAPF 로 링크만 했으며, MRTA-RM 을 교착 없음 보장으로 쓰지 않고(f20) 두 연구 수치를 순위로 비교하지 않았다(f24, 8절에도 명시).
- f19·ref-1456 — 8절에서 공개 구현을 '저자 공개 Python 구현(MIT 라이선스), 같은 팀 산출물이라 독립 재현 아님'까지만 쓰고 GVD 구현이라고 쓰지 않았다.
- f21~f23 — 8절의 20,000 에이전트·30,000 작업·1초 수치에 '저자 보고, 격자 지도 계산 실험, 실제 로봇 배치 아님'을 병기했고, 6절·8절 어디에도 논문 내부 절 번호를 쓰지 않았다.
- f25·f26 — 7절의 rmf_fleet_adapter 2.14.0(2026-09-26) #534 문장에 '패키지 태그 기준, ROS 배포판 반영 시점 미확인'을 병기했다.
- 용어(f18) — 6절에서 '경로망(roadmap)'으로 쓰고 용어집 roadmap 에 링크했으며, GVD 는 첫 등장 시 '일반화 보로노이 다이어그램(Generalized Voronoi Diagram, GVD)'으로 풀어 쓰고 일반화 보로노이 그래프 용어에 링크하지 않았고, makespan 은 '전체 완료 시간(makespan)'으로 썼다.
- 용어집 — '최소 비용 흐름(Minimum-Cost Flow)'·'이론 모듈로 만족 가능성(SMT)' 2건을 glossary_updates 에 신규(action: new, 스키마의 신규 값)로 등록했다.
- 인용 — ref-168 은 페이지 전체에서 직접 인용 없이 모두 재서술했다(0회).
- 참고문헌 ref-168 — 13절 각주와 reference_updates 를 저자 'Kaitha, S. p. r., & Yu, H.', 발행일 2025-12-02, 접근일 2026-10-10 으로 고치고 '(원문 미열람)'을 뗐다.
- 참고문헌 ref-152·ref-404 — 13절 각주 접근일을 2026-10-10 으로 고치고 ref-152 의 '(원문 미열람)'을 뗐다.
- 신규 참고문헌 ref-1453~ref-1398 — 13절에 '기관, 제목, 발행일, URL, 접근일 2026-10-10' 형식으로 각주를 등록하고 ref-1453·ref-1456 은 발행일 '미확인', ref-1457 은 '2026-05'로 썼으며 reference_updates 에도 냈다.
- open_questions_new 4건 — open_question_updates 에 new 로 등록하고, 1번에 관련 기존 질문 oq-053·oq-082, 3번에 oq-030 을 표시했으며 기존 질문은 해결로 바꾸지 않았다(11절에도 같은 표시).
- 트랙 반영 제안 16건 — 이번 브리프의 finding 이 아니므로 본문에 반영하지 않고 '제안' 상태로 남겼으며, additional_research_requests 에 다음 25. 작업 배정 — MRTA 실행에서 처리하도록 적었다.
- 2차: 이전 주제 페이지 링크 — 7·8·11절 패치를 append 에서 replace 로 바꾸고(6절도 같은 방식으로 정리) 각 절 첫 문단 둘째 문장에 2026-09-25 주제 페이지(2026-09-25-area13-s6·s7·s8·s11)로 가는 링크 문장을 넣었으며, 어느 문장도 '자세한 내용은 주제 페이지'로 시작하지 않는다. 링크는 ../../topics/2026/… 경로라 세부영역 페이지와 분리 주제 페이지 양쪽에서 유효하다. 기존 7절 첫 문장([사실] 주장)은 유지했고, 8절 첫 문단은 2026-09-25 에 고른 고전 연구·시뮬레이션 연구·국내 자료와 2026-10-10 에 더한 2024~2026 연구 3건을 함께 밝혀 요약과 링크 대상이 어긋나지 않게 했으며, 11절 첫 문단도 이전 질문(oq-024·oq-052 등)과 이번 부분 근거·새 질문을 나눠 밝혔다.
- 2차: 'n절' 상호참조 — 6절('9절에서 다룬다'), 7절('9절에 둔다'), 8절('5절 병원 모사 사례', '6절의 이 위키 종합 참고'), 11절(oq-030·oq-053·oq-054 의 '(6절)'·'(9절)'·'(5절)')을 모두 '세부영역 페이지 [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md)의 '<번호. 절 제목>' 절' 형식의 이름 있는 참조로 바꿨다. 링크 경로는 분리 전후 어느 위치에서도 같은 세부영역 페이지를 가리키며, 이번 실행에서 다시 생길 분리 주제 페이지 경로에는 기대지 않았다.
- 분량 초과 자동 분리: 25. 작업 배정 — MRTA 본문 11,425자 > 기준 4,000자 → 6개 절을 주제 페이지로 옮김, 남은 본문 5,008자
