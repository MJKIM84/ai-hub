# 리서치 브리프 2026-10-12-05

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-12-05 |
| 날짜 | 2026-10-12 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 44. 로봇 기반 모델·언어 모델 계획 |
| 대분류 | L. AI·학습 기술 |

## 갭(비어 있거나 약한 섹션)

- 섹션 5. 적용 사례 — 제조 공장 사례가 BMW 보도자료(ref-1051) 하나에 기대며, 93행 'Figure AI 자체 발표로는 교차 확인하지 못했다'가 Figure AI 발표(2025-11-19, 2026-06-30)의 존재와 맞지 않음. 10개월·11개월 문구의 출처 위치(CEO 인용·본문)와 Figure 쪽 기간 축, 99% 성공률이 목표치라는 구분이 없음. 연구 실물 사례(IMR-LLM 로봇 팔 3대)도 없음
- 섹션 6. 대표 접근법과 기술(분리 2026-09-30-area44-s6) — SMART-LLM·IMR-LLM 은 초록 수준 서술뿐이라 평가 규모(36 지시, 23장면·50작업)·실패 양상(불가능 과제, 도달 불가 배정)·풀이 방식(FIFO)이 없고, LLM+P·KnowNo 류 보장의 입력 전제(사람이 준 도메인, i.i.d., 무오류 실행)가 적혀 있지 않음. 다중 로봇 등각 예측 계획(S-ATLAS) 없음. disjunctive graph 번역어가 위키 안에서 셋으로 갈림
- 섹션 7. 관련 표준·프레임워크·오픈소스(분리 2026-09-30-area44-s7) — 'OpenVLA의 라이선스는 확인하지 못했다'(표 바로 아래)와 GR00T N1 '오픈소스(공개 모델)' 표기에 코드·가중치 라이선스 구분과 문서 간 충돌이 없음. VLA 배포물의 입출력 계약(정규화·행동 청크·개방 루프)과 GR00T N1.7 EA 상태, ROSA 의 물리 실행 조건이 없음
- 섹션 8. 대표 연구와 자료(분리 2026-09-30-area44-s8) — 최근 로봇 기반 모델(π0.7)과 VLA 견고성 벤치마크(LIBERO-Plus)가 없고, 국내 동향이 2025-05 기사 하나뿐(산업부 M.AX 휴머노이드 과제 표 없음)
- 섹션 9. 책임 경계 — 도구 호출(MCP)로 로봇을 움직일 때 힌트·권한·승인·세션 종료·물리 정지의 관계가 없음
- 섹션 11. 열린 질문(분리 2026-09-30-area44-s11) — oq-216~oq-219 모두 열림. 부분 근거(배포물별 입출력, 연구 벤치마크 규모, Figure 기간 축)가 연결돼 있지 않음
- 정정 요청 없음(target.json corrections 비어 있음). 메모·검증에서 나온 위키 내부 정정: s7 OpenVLA 라이선스 문장, 5절 93행 Figure 자체 발표 문장

## 조사 질문

1. 범용 로봇 모델과 언어 모델은 오케스트레이션의 무엇을 바꾸는가? [분류원문]
2. oq-217 언어 모델 기반 다중 로봇 계획기의 공개 평가는 어떤 규모·조건(시뮬레이션/실물, 로봇 수)이며 어떤 실패 양상(능력 밖 배정)을 보고하는가? (섹션 5·6 겨냥)
3. 기호 계획기 결합·등각 예측 기반 계획의 검증·보장은 어떤 입력 전제(도메인 제공자, 분포 가정, 스킬 실행 성공)에 기대는가? (섹션 6 겨냥)
4. oq-216 VLA 를 등록하려면 배포물마다 어떤 입출력(행동 공간·정규화·행동 청크·제어 모드)과 공개 상태(EA/GA)를 확인해야 하는가? (섹션 7·8 겨냥)
5. OpenVLA·GR00T N1.7·openpi 의 코드와 가중치 사용 조건은 각 문서에서 무엇이라 적혀 있고 서로 맞는가? (섹션 7 겨냥)
6. 언어 모델 도구 호출(MCP·ROSA)로 로봇을 움직일 때 권한·승인·세션 종료와 물리 정지는 어떻게 나뉘는가(oq-141 관련)? (섹션 7·9 겨냥)
7. oq-218·oq-219 BMW–Figure 와 국내 물류 실증 발표에서 목표·기간·첫 시연과 실측 성과는 어떻게 구분되는가? (섹션 5·8·11 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | SMART-LLM 의 평가 데이터셋은 AI2-THOR 가정 시뮬레이션의 고수준 지시 36개로 구성되며, 과제마다 로봇 1~4대를 쓴다. | ref-090 | 아니오 | medium | 2026-10-12 | — | — |
| f2 | [사실] | SMART-LLM 의 불가능 과제 시험(어떤 로봇도 필요한 스킬을 갖지 않은 과제)에서 GPT-4·Claude-3 기반 구성은 배정 계획을 만들지 않았고, GPT-3.5·Llama2 기반 구성은 과제에 맞지 않는 로봇이 들어간 배정 계획을 만들었다. 이 시험은 표 I 집계에 들어 있지 않고 과제 수도 보고되지 않았다. | ref-090 | 아니오 | medium | 2026-10-12 | — | — |
| f3 | [사실] | IMR-Bench 는 생산 라인 설계 전문가가 실제 산업 현장에서 수집·각색한 장면 23개(장면당 로봇 1~7대)를 바탕으로 제조 작업 50개를 구성한 벤치마크이며, KunWu 플랫폼 위에 만들어졌다. | ref-170 | 아니오 | medium | 2026-10-12 | — | — |
| f4 | [사실] | IMR-LLM 구현은 언어 모델이 구성을 도운 이접 그래프(disjunctive graph)의 일정을 휴리스틱 FIFO(선입선출) 알고리즘으로 푼다. | ref-170 | 아니오 | medium | 2026-10-12 | — | — |
| f5 | [사실] | IMR-LLM 의 실물 시험은 컨베이어에 공작물을 옮기는 로봇 팔 3대의 단일 장면이었고, 전문가가 약 15분 걸려 장면 설명을 손으로 작성해 입력했다. 반복 횟수는 보고되지 않았다. | ref-170 | 아니오 | medium | 2026-10-12 | — | — |
| f6 | [사실] | IMR-LLM 저자는 복잡한 다중 로봇 작업에서 성공률이 떨어진 주된 이유로 언어 모델의 잘못된 분해·배정(예: 팔이 닿지 않는 로봇에 작업 배정)을 들었으나, 그 빈도는 정량화하지 않았다. | ref-170 | 아니오 | medium | 2026-10-12 | — | — |
| f7 | [사실] | LLM+P 는 행동의 전제·효과를 담은 PDDL 도메인 파일을 사람 전문가가 제공한다는 것을 입력 전제로 둔다. 언어 모델은 문제(problem) 파일만 만든다. | ref-092 | 아니오 | medium | 2026-10-12 | — | — |
| f8 | [사실] | S-ATLAS(등각 예측 기반 다중 로봇 언어 계획기)의 임무 성공률 보장은 보정(calibration) 시나리오와 시험 시나리오가 독립·동일분포(i.i.d.)라는 조건 아래에서만 성립한다. | ref-1607 | 아니오 | medium | 2026-10-12 | — | — |
| f9 | [사실] | S-ATLAS 의 임무 완료율 정리(Theorem IV.2(a))는 계획 실행에 오류가 없다는 전제를 두며, 증명은 예측 집합이 단일 원소가 아닐 때 사람이 정확한 도움을 준다는 것도 전제한다. | ref-1607 | 아니오 | medium | 2026-10-12 | — | — |
| f10 | [사실] | S-ATLAS 는 AI2-THOR 시뮬레이션의 검증 시나리오 110개로 평가했고 로봇 수는 1·3·10·15대였다. 열람한 본문에서 실물 로봇 실험은 확인되지 않았다. | ref-1607 | 아니오 | medium | 2026-10-12 | — | — |
| f11 | [사실] | OpenVLA 모델 카드에 따르면 OpenVLA 는 언어 지시와 카메라 영상 한 장을 입력받아 정규화된 7자유도 엔드이펙터 변위(x, y, z, roll, pitch, yaw, gripper)를 출력하며, 실제 로봇에서 실행하려면 로봇·데이터셋별로 계산한 통계로 역정규화해야 한다. | ref-1609 | 아니오 | medium | 2026-10-12 | — | — |
| f12 | [사실] | OpenVLA 공식 저장소(고정 커밋 c8f03f4)의 코드 라이선스는 MIT 다. | ref-1608 | 아니오 | medium | 2026-10-12 | — | — |
| f13 | [사실] | 같은 OpenVLA README 는 사전학습 모델이 기반 모델의 제약을 물려받을 수 있으며, 두 모델이 Llama 2 에서 파생됐으므로 Llama Community License 가 적용될 수 있다고 적는다. | ref-1608 | 아니오 | medium | 2026-10-12 | — | — |
| f14 | [사실] | OpenVLA 의 Hugging Face 모델 카드는 "모든 OpenVLA 체크포인트와 학습 코드가 MIT 라이선스로 공개된다"고 적어, 저장소 README 의 Llama Community License 적용 가능 문구와 충돌한다. 현재 main 판(커밋 47a0ec7, 2026-02-17)도 같은 문구이며, 두 문서는 같은 개발팀 자료라 어느 쪽이 맞는지는 문서만으로 정할 수 없다. | ref-1609, ref-1608 | 아니오 | medium | 2026-10-12 | — | — |
| f15 | [사실] | openpi 원격 추론 예시는 정책 서버가 (action_horizon, action_dim) 형태의 행동 청크(action chunk)를 돌려준다고 설명한다. | ref-1610 | 아니오 | medium | 2026-10-12 | — | — |
| f16 | [사실] | 같은 openpi 예시는 다음 추론 호출 전까지 예측된 행동 청크의 나머지 행동을 개방 루프(open-loop)로 실행하도록 안내한다. | ref-1610 | 아니오 | medium | 2026-10-12 | — | — |
| f17 | [사실] | openpi README(커밋 215abfb)가 제공하는 기반 체크포인트는 π0, π0-FAST, π0.5 뿐이며, π0.7 가중치는 목록에 없다. | ref-1610 | 아니오 | medium | 2026-10-12 | — | — |
| f18 | [사실] | NVIDIA Isaac GR00T 저장소의 n1.7-release README 는 GR00T N1.7 을 Early Access(EA) 릴리스로 명시하고, GA(정식) 릴리스 전까지 지원·안정성 보장이 제한되며 상용 지원을 포함한 운영 배치는 GA 대상이라고 적는다. | ref-1611 | 아니오 | medium | 2026-10-12 | — | — |
| f19 | [사실] | 같은 GR00T README 의 License 절은 코드는 Apache 2.0, 모델 가중치는 NVIDIA Open Model License 로 구분한다. | ref-1611 | 아니오 | medium | 2026-10-12 | — | — |
| f20 | [추정] | GR00T README 소개 문단은 "GR00T N1.7 은 Apache 2.0 으로 완전히 상용 라이선스가 가능하다"고 적지만, 이는 같은 README 의 License 절(가중치는 별도 라이선스)·가중치 저장소 LICENSE(3.3절 비상업 한정)와 맞지 않는 벤더 소개 문구다. | ref-1611, ref-1612 | 아니오 | low | 2026-10-12 | — | — |
| f21 | [사실] | Hugging Face nvidia/GR00T-N1.7-3B 저장소의 LICENSE 파일(커밋 6949d5d, 현재 main 과 같음)은 'NVIDIA License' 표제 아래 3.3절에서 저작물과 파생물을 연구·평가 목적의 비상업 용도로만 쓸 수 있게 하고, NVIDIA 와 그 계열사는 상업적으로 쓸 수 있다는 예외를 둔다. | ref-1612 | 아니오 | medium | 2026-10-12 | — | — |
| f22 | [사실] | GR00T N1.7 가중치의 사용 조건은 세 문서가 서로 다르게 적는다: README 소개(Apache 2.0 으로 상용 가능), README License 절과 3B 모델 카드(NVIDIA Open Model License, 카드는 '상업·비상업 사용 준비'), 3B 저장소 LICENSE 파일(NVIDIA License 3.3절 비상업 한정). 어느 문서가 우선하는지는 문서에 적혀 있지 않다. | ref-1611, ref-1612 | 아니오 | medium | 2026-10-12 | — | — |
| f23 | [추정] | Physical Intelligence 의 π0.7 기술 보고서는 관절(joint)·엔드이펙터(ee) 행동을 함께 학습하고 프롬프트의 텍스트 식별자 c∈{joint, ee} 로 실행 제어 모드를 지정해 실행 시 과제에 따라 고른다고 설명한다. | ref-1613 | 아니오 | low | 2026-10-12 | — | — |
| f24 | [추정] | π0.7 보고서는 추론 지연에 대비해 학습 중 0~12 타임스텝의 지연을 모사했고, 이는 50 Hz 로봇에서 최대 240 ms 에 해당한다고 적는다. 이는 학습 조건이며 측정된 추론 지연이 아니고, 보고서의 UR5e 로봇은 20 Hz 로 동작한다. | ref-1613 | 아니오 | low | 2026-10-12 | — | — |
| f25 | [추정] | π0.7 저자들은 학습 데이터가 매우 커서 평가 과제가 학습 때 본(seen) 과제인지 처음 보는(unseen) 과제인지 확정하기 어렵다고 스스로 밝힌다. | ref-1613 | 아니오 | low | 2026-10-12 | — | — |
| f26 | [사실] | LIBERO-Plus 는 LIBERO 시뮬레이션 조작 과제에서 물체 배치, 카메라 시점, 로봇 초기 상태, 언어 지시, 조명, 배경 질감, 센서 잡음의 7개 축으로 입력을 하나씩 교란해 VLA 모델의 견고성을 평가한다. | ref-1614, ref-1615 | 아니오 | medium | 2026-10-12 | — | — |
| f27 | [사실] | LIBERO-Plus 에서 OpenVLA-OFT 의 성공률은 교란 없는 원본 97.1% 에서 로봇 초기 상태 교란 시 크게 떨어진다. 수치는 판마다 다르다: arXiv v3 표 1 은 로봇 초기 상태 37.2%·카메라 시점 59.7%, CVPR 2026 게재본(제목 'LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models') 표 2 는 로봇 초기 상태 31.9%·카메라 시점 56.4% 다. | ref-1614, ref-1615 | 아니오 | medium | 2026-10-12 | — | — |
| f28 | [사실] | ROSA FAQ 는 핵심 ROSA 에이전트가 텍스트 상호작용에 한정되어 물리 세계와 상호작용할 수 없으며, 물리적 상호작용에는 사용자가 맞춤 도구와 프롬프트를 만들어야 한다고 설명한다. | ref-1616 | 아니오 | medium | 2026-10-12 | — | — |
| f29 | [사실] | 같은 ROSA FAQ 는 로봇 능력을 넘는 행동을 막으려면 맞춤 도구 안에 실행 전 로봇 상태·능력 확인 제약과 매개변수 검증·행동 제한 같은 안전 검사를 직접 넣으라고 권고한다. | ref-1616 | 아니오 | medium | 2026-10-12 | — | — |
| f30 | [사실] | MCP 공식 블로그(2026-03-16)는 도구 어노테이션(readOnlyHint·destructiveHint 등)이 위험을 알리는 힌트일 뿐 실행 강제 수단이 아니며, 확실한 보장이 필요하면 네트워크 통제나 샌드박스로 해야 한다고 설명한다. | ref-1617 | 아니오 | medium | 2026-10-12 | — | — |
| f31 | [추정] | PickNik 의 MoveIt Pro MCP 서버 문서는 공유되는 배포(deployment) MCP 키는 읽기 전용이고, 로봇 동작은 호스트 사용자 세션에서 기존 Objective 를 시작·취소하는 것으로만 한정된다고 설명한다. | ref-1618 | 아니오 | low | 2026-10-12 | — | — |
| f32 | [추정] | 같은 문서는 MCP 서버가 별도의 실행 확인 프롬프트를 추가하지 않으며, 도구 승인은 MCP 클라이언트 설정에 달려 있고 클라이언트가 자동 승인할 수도 있다고 적는다. | ref-1618 | 아니오 | low | 2026-10-12 | — | — |
| f33 | [추정] | 같은 문서는 run_objective 로 시작한 로봇이 세션이 끝나도 계속 움직일 수 있고, cancel_objective 는 최선 노력(best effort)일 뿐 비상 정지가 아니며 MCP 취소·소프트웨어 정지는 물리적 비상 정지를 대체하지 않는다고 적는다. | ref-1618 | 아니오 | low | 2026-10-12 | — | — |
| f34 | [추정] | Figure AI 의 2025-11-19 발표는 BMW 스파턴버그의 Figure 02 를 '11개월 배치'라고 부르면서, 개발 착수 뒤 6개월 안에 공장에 납품·시험을 시작하고 10개월 안에 생산 라인 전면 배치를 시작했으며 '6개월의 일일 가동'과 1,250시간 이상 가동을 적는다. 세 기간의 기점·종점이 달라 BMW 보도자료의 10개월·11개월 차이를 해소하지 못한다. | ref-1619, ref-1051 | 아니오 | low | 2026-10-12 | — | — |
| f35 | [추정] | 같은 Figure 발표에서 '교대당 99% 초과 성공률'과 '교대당 개입 0회'는 목표(target·goal)로 제시되며, 달성한 실측치로 보고되지 않았다. | ref-1619 | 아니오 | low | 2026-10-12 | — | — |
| f36 | [추정] | Figure AI 는 2026-06-30 발표에서 BMW 스파턴버그 공장에서 Figure 03 이 물류 작업 흐름을 수행한 것을 '첫 시연'으로 설명하고, 자사 VLA 인 Helix 02 가 손·팔·몸통·발을 함께 제어해 무거운 대차를 끌었다고 적는다. | ref-1620 | 아니오 | low | 2026-10-12 | — | — |
| f37 | [추정] | 기존 위키 5절의 'Figure AI 자체 발표로는 교차 확인하지 못했다'(Figure 03 착수 문단)는 고쳐야 한다. Figure AI 자체 발표(2026-06-30, 2025-11-19)가 있으나, BMW 와 같은 프로젝트의 당사자 자료라 독립 교차 확인으로는 세지 않는다. | ref-1620, ref-1619, ref-1051 | 아니오 | low | 2026-10-12 | — | — |
| f38 | [사실] | 산업통상부 2025-11-24 보도자료에 따르면 산업부와 서울대가 M.AX 얼라이언스 협력 MOU 를 맺었고, 지원 과제 표의 휴머노이드 분과 과제는 '휴머노이드 AI 파운데이션 모델 개발'(2025~2028년, 484억 원, 핵심 연구진 장병탁·박재흥 서울대 교수)이다. | ref-1621 | 아니오 | medium | 2026-10-12 | — | — |
| f39 | [의견] | 스킬 목록이 없거나 로봇 능력 밖인 요청을 계획기가 거절하는지(또는 닿지 않는 로봇에 배정하지 않는지)를 일반 성공률과 별도의 수용 시험 항목으로 두어야 한다. | ref-090, ref-170 | 아니오 | medium | 2026-10-12 | — | — |
| f40 | [의견] | 언어 모델 다중 로봇 계획의 검증 결과에는 일정 풀이 통과와 분해·배정의 정확성을 따로 적고, 계획 검증이 기대는 전제(사람이 준 도메인 판, i.i.d. 시나리오, 무오류 스킬 실행, 정확한 사람 도움)를 함께 기록해 전제가 깨질 때 보장 상태를 다시 평가해야 하며, 이 보장을 플릿의 물리적 안전 보장과 섞지 않아야 한다. | ref-170, ref-092, ref-1607 | 아니오 | medium | 2026-10-12 | — | — |
| f41 | [의견] | 연구 논문의 실물 시험(예: 로봇 팔 3대 단일 장면)은 사례 표에 장면 작성자·시뮬레이션 확인·복구 책임을 함께 적고 장기 운영 실적으로 표시하지 않아야 한다. | ref-170 | 아니오 | medium | 2026-10-12 | — | — |
| f42 | [의견] | VLA 탑재 로봇의 능력 등록에는 모델·가중치 revision(해시), 로봇 기종·카메라, 좌표계·행동 단위·제어 모드, 정규화 통계, 행동 청크의 형태·관측 시각·유효기간·중단 조건, 허용 과제와 완료 판정을 두고, 명령 완료는 로봇 외부 상태로 확인하는 것이 필요해 보인다. 이는 ROP 설계 제안이며 표준이 아니다. | ref-1609, ref-1610, ref-1613 | 아니오 | medium | 2026-10-12 | — | — |
| f43 | [의견] | 공개 VLA 를 도입할 때 코드 라이선스와 가중치 사용 조건을 따로 확인하고, README 소개 문구만으로 상용 허용을 확정하지 않으며, 문서끼리 충돌하는 조건은 배포자에게 서면으로 확인할 항목으로 남겨야 한다. | ref-1608, ref-1609, ref-1611, ref-1612 | 아니오 | medium | 2026-10-12 | — | — |
| f44 | [의견] | 카메라 교체·로봇 초기 자세 변경 같은 교란을 로봇별 수용 시험에 넣고, 벤치마크 수치는 판(arXiv 판·게재본)을 밝혀 인용하며, 단일 팔 시뮬레이션 벤치마크 순위를 제조사 혼합 플릿 순위로 환산하지 않아야 한다. | ref-1614, ref-1615 | 아니오 | medium | 2026-10-12 | — | — |
| f45 | [의견] | 언어 모델이 도구 호출로 로봇을 움직이는 구성에서는 어노테이션 힌트나 클라이언트 자동 승인에 기대지 말고, ROP 쪽 런타임에서 읽기/실행 권한·실행 대상·승인된 계획 revision·goal id 와 물리적 완료 판정을 검사하며, 세션 종료를 별도의 정지 절차에 연결해야 한다. | ref-1617, ref-1618, ref-1616 | 아니오 | medium | 2026-10-12 | — | — |
| f46 | [의견] | 벤더·도입 기업 발표는 목표·기간·첫 시연과 실측 성과를 다른 열로 나누고, 운영 기간의 기점·종점, 성공률의 분모, 개입·실패 로그, 인계 신호가 공개될 때까지 도입 KPI 비교에 쓰지 않아야 한다. 국내 실증 목표(자동화율 80%·성공률 90%)도 같다. | ref-1619, ref-1620, ref-1051, ref-1621 | 아니오 | medium | 2026-10-12 | — | — |

### 근거 발췌

- **f1**: arXiv v2 §V-A: "36 high-level instructions", 과제별 로봇 1~4대, AI2-THOR. 기존 위키(docs/tracks/chat-based-configuration-and-operation/stage-2-data-and-standards.md 166행 '36개 상위 지시 … 원문 미열람', 같은 파일 370행)의 저자 보고 수치를 원문 확인으로 보강하는 것이며 새 사실 추가가 아니다. 실물 시험(대수·반복 수)은 이 수치와 별개
- **f2**: arXiv v2 §VI-A 'Infeasible Scenarios': "GPT-4 and Claude-3 backbones exhibited the capacity to discern this situation and refrained from generating any task allocation plan. In contrast, … GPT-3.5 and Llama2 produced a task allocation plan involving robots ill-suited …", "This particular scenario is not included in Table I". Claude-3 비교는 v2 에만 있다. 모든 모델·모든 실행으로 일반화하지 않음
- **f3**: arXiv v1 §V-A Dataset: "our benchmark comprises 23 scenes collected and adapted from real industrial environments by production line design experts. Each scene involves between 1 to 7 robots", 제조 작업 50개. ICRA 2026 pp.7609–7616. 기존 위키 C 트랙(stage-1-prior-work-and-products.md 240·310행) 'IMR-Bench 규모 미확인'에 답함. 실험 데이터셋이며 상용 플릿 실적이 아님
- **f4**: arXiv v1 §IV-A: "we use a heuristic First-In-First-Out (FIFO) [33] algorithm to solve the disjunctive graph". 결정적 풀이를 전역 최적 보장으로 읽지 않음. 용어가 위키에 '선택 그래프'(2026-09-30-area44-s6.md 57행), '선언 그래프'(C 트랙 stage-1 112행), '이접 그래프'(같은 파일 240행)로 흩어져 있음
- **f5**: arXiv v1 §V-C: "This scene consists of three robotic arms", "we used a manually constructed scene description, which took an expert approximately 15 minutes". 반복 횟수·오류율 미보고. 장기 공장 배치 증거가 아님(기존 위키 9절 138행·s6 57행 '초록에 실제 공장 배치 없음'과 일치)
- **f6**: arXiv v1 §V-B: "we observed a decline in the SR for complex multi-robot tasks … incorrect decompositions and allocations (e.g., assigning an operation to an out-of-reach robot), which directly leads to a decrease in OC". OC(작업 일관성) 하락 원인 예시이며 오류 건수는 없음
- **f7**: arXiv v3 §III-C: "a human expert can provide" 도메인 PDDL. 기존 위키의 [추정](C 트랙 stage-1-prior-work-and-products.md 80행, task-model-draft.md 133행 '사람이 미리 정의 … 이 위키의 정리')을 LLM+P 에 대해서는 직접 근거로 보강. 생성된 problem 이 현장 상태와 맞는지의 검증과는 별개
- **f8**: arXiv v4 Remark III.6: "calibration and test scenarios are i.i.d.". IEEE RA-L 10(1):160–167(2025-01). 확률은 명시한 시나리오 분포에서 정의되며 분포가 바뀐 현장까지 넓히지 않음
- **f9**: arXiv v4 Theorem IV.2(a): "Assuming error-free execution"; 초록 "assuming successful plan execution", 기여 (i) "assuming successful execution of robot skills". 물리적 실패·안전 인증에 대한 보장이 아님
- **f10**: arXiv v4 §V·§V-A: "110 (validation) scenarios", N∈{1,3,10,15}, AI2-THOR. hardware/real robot 실험 서술 없음(본문 검색 기준). 15대는 시뮬레이터 대수
- **f11**: Hugging Face openvla/openvla-7b 카드 Uses: "predict (normalized) robot actions consisting of 7-DoF end-effector deltas … actions need to be *un-normalized* subject to statistics computed on a per-robot, per-dataset basis". 공통 능력 등록 스키마가 아니라 배포물의 입출력 설명
- **f12**: LICENSE 표제 "MIT License"; README 606행 "`LICENSE` - All code is made available under the MIT License". 가중치 조건과 분리해 기록. 기존 위키 2026-09-30-area44-s7.md 표 아래 'OpenVLA의 라이선스는 확인하지 못했다'를 정정할 근거
- **f13**: README 99–101행: "our pretrained models may inherit restrictions from the underlying base models we use. Specifically, both the above models are derived from Llama-2, and as such are subject to the [Llama Community License]". 검증에 따라 '적용된다'가 아니라 '적용될 수 있다'로 완화(앞 문장 'may inherit'). 법적 적용 판정이 아님
- **f14**: 카드 20행: "All OpenVLA checkpoints, as well as our training codebase are released under an MIT License.", 메타데이터 license: mit. 메모가 고정한 리비전 258bd1d(2024-11-29)는 현재 main 이력에 없어 main(47a0ec7) 기준으로 대조. README·카드는 같은 프로젝트 자료라 독립 교차 확인이 아님. 충돌 해소(명시적 정정)는 확인 못 함
- **f15**: openpi 커밋 215abfb docs/remote_inference.md Querying 예시 주석: "This returns an action chunk of shape (action_horizon, action_dim)." 인터페이스 서술(벤더 성능 주장이 아님). 명령 수락·작업 완료 상태와 같지 않음
- **f16**: docs/remote_inference.md 63행 주석: "… from the predicted action chunk open-loop in the remaining steps." 예시 동작 설명이며 네트워크 장애·청크 유효기간·안전 정지 기능의 근거가 아님
- **f17**: README 'Model Checkpoints' 표 66–68행: pi0_base, pi0_fast_base, pi05_base. π0.7 기술 보고서(ref-1613)와 공개 배포물의 대응이 없음을 뜻하며, π0.7 의 결과를 openpi 로 재현할 수 있다고 보지 않음
- **f18**: README 49–59행: "This is an Early Access (EA) release. … support and stability guarantees are limited until the GA release.", GA 항목 "Production deployment with commercial support"; 507·511행 EA 기간 PR 미수용·best-effort 지원. 브랜치 이름 기준 열람이며 커밋 sha 로 고정하지 못함
- **f19**: README 514–517행: "Code: Apache 2.0 — see LICENSE", "Model weights: NVIDIA Open Model License". 저장소 LICENSE 파일은 Apache 2.0
- **f20**: 벤더 주장: README 71행 "GR00T N1.7 is fully commercially licensable under Apache 2.0." 같은 문서 514–517행과 GR00T-N1.7-3B LICENSE §3.3(f21)이 이와 다르게 적는다. 소개 문구만으로 가중치 상용 허용을 확정하지 않음
- **f21**: LICENSE §3.3 Use Limitation: "The Work and any derivative works thereof only may be used or intended for use non-commercially. Notwithstanding the foregoing, NVIDIA Corporation and its affiliates may use the Work and any derivative works commercially. As used herein, 'non-commercially' means for research or evaluation purposes only." 이 파일만 서술하며 모든 N1.7 배포물의 사용 금지로 넓히지 않음
- **f22**: README 71·514–517행; GR00T-N1.7-3B 카드(main) "This model is ready for commercial/non-commercial use.", "released under the NVIDIA Open Model License Agreement"; 같은 저장소 LICENSE 표제 "NVIDIA License" §3.3. 모두 NVIDIA 자료라 독립 확인이 아니며 법적 우선순위는 판단하지 않음. 기존 위키 2026-09-30-area44-s7.md 표의 'GR00T N1 — 오픈소스(공개 모델)' 표기와도 관련
- **f23**: 벤더 주장: arXiv v2 §V-D: "use a text identifier c∈{joint, ee} to designate the control mode in the prompt. Then at runtime, we can pick the control mode depending on the task." 단일 회사 보고서이며 구현을 실행해 확인하지 않음
- **f24**: 벤더 주장: arXiv v2 §VI-B: "During training, we simulate delays of 0 to 12 timesteps, corresponding to a maximum inference latency of 240ms on a 50Hz robot."; 실험 로봇 플랫폼 설명(Fig. 4 다음 문단): "The UR5e robots run at 20 Hz, while all other robots run at 50 Hz." 네트워크 포함 실측 최대 지연·다중 로봇 동시 추론 수치는 없음(oq-104 관련 근거로만)
- **f25**: arXiv v2 §X Discussion(seen/unseen 구분의 어려움). 회사 연구진의 한계 진술을 옮긴 것으로, 새 과제 무데이터 성공이나 이기종 플릿 일반화 보장의 근거로 쓰지 않음. 단일 출처
- **f26**: arXiv v3 §2.1: "seven common single-dimension perturbations"; CVPR 2026 게재본 Table 2 열(Camera, Robot, Language, Light, Background, Noise, Layout). 두 판은 같은 연구팀 자료라 독립 교차 확인이 아님. 단일 팔 조작 시뮬레이션이며 현장 플릿 평가가 아님
- **f27**: arXiv v3 Table 1 OpenVLA-OFT 행: 97.1 | 59.7 | 37.2 | 81.5 | 85.8 | 92.4 | 76.7 | 77.1. CVPR 2026 게재본(pp.38574–38583) Table 2 OpenVLA-OFT 행: Original 97.1, Camera 56.4, Robot 31.9, Language 79.5, Light 88.7, Background 93.3, Noise 75.8, Layout 74.2, Total 69.6. 검증 수정: 메모의 '97.1/37.2'는 v3 값이라 판을 명시하고 게재본 값을 병기. 직접 재실행하지 않음
- **f28**: nasa-jpl/rosa Wiki FAQ 'What are ROSA's limitations?' 88행: "The core ROSA agent is limited to text-based interactions and cannot interact with the physical world. To enable physical interactions, you will need to create custom tools and prompts." 릴리스에 고정되지 않은 위키 문서(접근일 기준)
- **f29**: FAQ 'Safety and Guardrails' 128행 "Add safety checks to your custom tools to validate parameters and limit actions.", 'How can I ensure that ROSA does not perform actions that are outside the robot's capabilities?' 152–156행 "Implement constraints in your custom tools to check the robot's state and capabilities before executing actions." 기존 위키 C 트랙 stage-1-prior-work-and-products.md 118행 [추정]('README·Custom Agents 위키 범위에서 확인·권한 장치 설명이 없다')은 FAQ 범위에서는 맞지 않아 후속 정리가 필요. 권고이며 자동 제공 기능이 아님
- **f30**: 블로그 'What Annotations Can't Do' 75행: "They aren't enforcement. If you need a guarantee that a tool can't exfiltrate data, that's a job for network controls or sandboxing, not a boolean hint." 규범 명세 개정이 아니라 프로젝트의 해설 글. 기존 위키의 MCP 명세(2025-06-18) 서술 — 2026-09-29-area13-s6.md 45행(ref-856: 신뢰하지 않는 서버의 주석 불신, 프로토콜은 강제 불가), C 트랙 stage-4-misinterpretation-safeguards.md 253행(ref-696) — 과 같은 방향이며 이를 보완함
- **f31**: 벤더 주장: MoveIt Pro 문서(Version 10) 74·78행: "deployment MCP key is read-only because it is shared", "Robot motion over MCP is limited to starting and cancelling existing Objectives from a host-user session; the deployment MCP key never can." 제품을 실행해 확인하지 않음
- **f32**: 벤더 주장: 78행: "Your MCP client controls tool approval according to its configured permissions; clients may auto-approve calls. The server adds no confirmation prompt." oq-141(승인 관문 위치)의 부분 근거: 이 제품은 서버가 아니라 클라이언트에 승인을 맡김
- **f33**: 벤더 주장: 도구 표 119행 run_objective "The robot may move, and keeps moving if the session ends."; 542행 "cancel_objective is best effort, not an emergency stop. Neither MCP cancellation nor the Runtime's software stop controls replace physical emergency-stop controls." 세션 종료와 물리 정지를 같은 것으로 보지 않음
- **f34**: 벤더 주장: Figure 'F.02 Contributed to the Production of 30,000 Cars at BMW' 10행 "an 11 month Figure 02 robot deployment … Within 6 months … began testing. Within 10 months, we launched full deployment", 27행 "Six months of daily runtime … 1,250+ operational hours". BMW 보도자료(ref-1051)는 11개월이 Figure CEO 인용문, 10개월("over ten months")이 본문. 10/11개월 충돌은 기존 위키(5절 89·91행, oq-219)에 있고 기간 축 차이만 새로 보탬. 같은 프로젝트 당사자 자료
- **f35**: 벤더 주장: 22–23행 "Our target was > 99% success per shift.", "The goal was zero per shift." 독립 생산 로그·분모 없음. 실측 달성률로 옮기지 않음
- **f36**: 벤더 주장: Figure 'F.03 Arrives at BMW'(June 30, 2026) Highlights 14–15행: "The first demonstration of Figure 03 performing a logistics workflow at BMW Group Plant Spartanburg.", "Helix 02, Figure's proprietary pixels-to-actions VLA …". 첫 시연이며 지속 배치 성과(가동률·인계 로그)가 아님
- **f37**: 벤더 주장: 대상 문장은 docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md 93행. Figure 발표 2건(ref-1619·ref-1620)이 BMW 보도자료(ref-1051)와 같은 배치·착수를 설명함. 세 출처 모두 벤더 문서라 '확인됨'이 아니라 '당사자 발표가 일치함'으로 적는 것이 맞음
- **f38**: motir.go.kr 보도자료(등록일 2025-11-24) 과제 표: "휴머노이드 | '25~'28년, 484억원 | 장병탁, 박재흥 | 휴머노이드 AI 파운데이션 모델 개발". 기업이 데이터·플랫폼을 주고 서울대가 모델을 개발해 기업에 다시 제공하는 구조. 기존 위키 5절 물류창고 사례의 로보티즈–BGF로지스 과제(ref-1052, 정부 출연금 약 60억 원)와 같은 사업인지는 확인되지 않음. 자동화율 80%·성공률 90% 실측 결과는 이 자료에도 없음(oq-218 미해결)
- **f39**: 메모 A01·A03 ROP 시사점. 근거 f2(불가능 과제에서 일부 모델의 부적합 배정), f6(도달 불가 배정). 의견
- **f40**: 메모 A02·A04·A05 ROP 시사점. 근거 f4, f7, f8, f9. 의견
- **f41**: 메모 A03 ROP 시사점. 근거 f5. 의견
- **f42**: 메모 A06·A08·A10 ROP 시사점. 근거 f11, f15, f16, f23. oq-216 의 부분 답(공통 등록 표준·적합성 시험은 확인 못 함). 의견
- **f43**: 메모 A07·A09 ROP 시사점. 근거 f12~f14, f18~f22. 법률 판단이 아님. 의견
- **f44**: 메모 A11 ROP 시사점. 근거 f26, f27. 의견
- **f45**: 메모 A12·A13 ROP 시사점. 근거 f28~f33. 기존 위키 2026-09-29-area13-s6.md 45행의 '승인 관문은 ROP 쪽 호스트에' 추정과 같은 방향. 의견
- **f46**: 메모 A14·A15 ROP 시사점. 근거 f34~f38. 의견

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-090 | Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models | 2023-09 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2309.10062 | 아니오 |
| ref-170 | Su, X., Xu, J., van Kaick, O., Xu, K., & Hu, R. | IMR-LLM: Industrial Multi-Robot Task Planning and Program Generation using Large Language Models | 2026-03 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2603.02669 | 아니오 |
| ref-092 | Liu, B., Jiang, Y., Zhang, X., Liu, Q., Zhang, S., Biswas, J., & Stone, P. | LLM+P: Empowering Large Language Models with Optimal Planning Proficiency | 2023-04 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2304.11477 | 아니오 |
| ref-1051 | BMW Group | BMW Group advances the use of Physical AI in production with Figure 03 project in Spartanburg | 2026-06-25 | 벤더 문서 | medium | 2026-10-12 | https://www.press.bmwgroup.com/global/article/detail/T0458778EN/bmw-group-advances-the-use-of-physical-ai-in-production-with-figure-03-project-in-spartanburg?language=en | 아니오 |
| ref-1607 | Wang, J., He, G., & Kantaros, Y. (IEEE Robotics and Automation Letters 10(1)) | Probabilistically Correct Language-based Multi-Robot Planning using Conformal Prediction | 2025-01 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2402.15368 | 아니오 |
| ref-1608 | OpenVLA 개발팀 (openvla/openvla GitHub) | OpenVLA — README 및 LICENSE (커밋 c8f03f4) | 미확인 | 오픈소스 문서 | high | 2026-10-12 | https://github.com/openvla/openvla/blob/c8f03f48af692657d3060c19588038c7220e9af9/README.md | 아니오 |
| ref-1609 | OpenVLA 개발팀 (Hugging Face openvla/openvla-7b) | openvla/openvla-7b — Model Card | 미확인 | 오픈소스 문서 | high | 2026-10-12 | https://huggingface.co/openvla/openvla-7b | 아니오 |
| ref-1610 | Physical Intelligence (Physical-Intelligence/openpi GitHub) | openpi — README, docs/remote_inference.md, LICENSE (커밋 215abfb) | 미확인 | 오픈소스 문서 | high | 2026-10-12 | https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/docs/remote_inference.md | 아니오 |
| ref-1611 | NVIDIA (NVIDIA/Isaac-GR00T GitHub) | Isaac GR00T N1.7 — README 및 LICENSE (n1.7-release 브랜치) | 미확인 | 오픈소스 문서 | high | 2026-10-12 | https://github.com/NVIDIA/Isaac-GR00T/blob/n1.7-release/README.md | 아니오 |
| ref-1612 | NVIDIA (Hugging Face nvidia/GR00T-N1.7-3B) | GR00T-N1.7-3B — LICENSE 및 모델 카드 | 미확인 | 오픈소스 문서 | high | 2026-10-12 | https://huggingface.co/nvidia/GR00T-N1.7-3B/blob/6949d5dfab2e872283e8cca8106ac3af8adcf39b/LICENSE | 아니오 |
| ref-1613 | Physical Intelligence (Ai, B. 외, arXiv) | π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities | 2026-04-16 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2604.15483 | 아니오 |
| ref-1614 | Fei, S., Wang, S., Shi, J. 외 (arXiv) | LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models | 2025-10-15 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2510.13626 | 아니오 |
| ref-1615 | Fei, S., Wang, S., Shi, J. 외 (CVPR 2026, Computer Vision Foundation Open Access) | LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models | 2026 | 논문 | high | 2026-10-12 | https://openaccess.thecvf.com/content/CVPR2026/html/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.html | 아니오 |
| ref-1616 | NASA Jet Propulsion Laboratory (nasa-jpl) | FAQ · nasa-jpl/rosa Wiki | 미확인 | 오픈소스 문서 | high | 2026-10-12 | https://github.com/nasa-jpl/rosa/wiki/FAQ | 아니오 |
| ref-1617 | Model Context Protocol (Hungerford, O., Morrow, S., & Chang, L.) | Tool Annotations as Risk Vocabulary: What Hints Can and Can't Do | 2026-03-16 | 오픈소스 문서 | medium | 2026-10-12 | https://blog.modelcontextprotocol.io/posts/2026-03-16-tool-annotations/ | 아니오 |
| ref-1618 | PickNik Robotics | Connect an AI Assistant with the MCP Server (MoveIt Pro 문서 Version 10) | 미확인 | 벤더 문서 | medium | 2026-10-12 | https://docs.picknik.ai/how_to/programmatic_sdks/mcp_server/ | 아니오 |
| ref-1619 | Figure AI | F.02 Contributed to the Production of 30,000 Cars at BMW | 2025-11-19 | 벤더 문서 | medium | 2026-10-12 | https://www.figure.ai/news/production-at-bmw | 아니오 |
| ref-1620 | Figure AI | F.03 Arrives at BMW | 2026-06-30 | 벤더 문서 | medium | 2026-10-12 | https://www.figure.ai/news/f-03-at-bmw | 아니오 |
| ref-1621 | 산업통상부 | 서울대와 M.AX 얼라이언스가 손잡고 휴머노이드, 자율주행차, AI팩토리에 탑재될 AI 모델 공동 개발한다. | 2025-11-24 | 정부·연구기관 | medium | 2026-10-12 | https://www.motir.go.kr/kor/article/ATCL3f49a5a8c/171238/view | 아니오 |

### 출처 요약

- **ref-090**: SMART-LLM 논문(기존 출처, IROS 2024 pp.12140–12147 게재). 이번에 arXiv v2 HTML 본문에서 36개 고수준 지시 데이터셋(§V-A)과 불가능 과제 시험(§VI-A)을 확인했다.
- **ref-170**: IMR-LLM 논문(기존 출처, ICRA 2026 pp.7609–7616). 이번에 arXiv v1 HTML 본문에서 IMR-Bench 23장면·50작업, FIFO 휴리스틱, 로봇 팔 3대 실물 시험, 도달 불가 배정 오류를 확인했다.
- **ref-092**: LLM+P 프리프린트(기존 출처). 이번에 arXiv v3 HTML §III-C 에서 사람 전문가가 PDDL 도메인을 제공한다는 입력 전제를 확인했다.
- **ref-1051**: BMW 그룹 보도자료(기존 출처). 이번 재열람에서 '11-month deployment'는 Figure CEO 인용문, 'over ten months'는 본문에 있음을 확인했다(캐나다판 T0458794EN 도 같은 문구).
- **ref-1607**: 등각 예측으로 사용자 지정 임무 성공률을 노리는 분산 다중 로봇 언어 계획기 S-ATLAS 논문(RA-L 10(1):160–167, DOI 10.1109/LRA.2024.3504233). arXiv v4 HTML 로 i.i.d. 조건(Remark III.6), 무오류 실행 전제(Theorem IV.2), 110개 AI2-THOR 검증 시나리오를 확인했다.
- **ref-1608**: OpenVLA 공식 저장소 README·LICENSE. 코드 MIT, 사전학습 모델은 Llama 2 파생이라 Llama Community License 제약을 물려받을 수 있다는 문구(99–101행)를 확인했다. 커밋 날짜는 확인하지 못했다.
- **ref-1609**: OpenVLA 7B 가중치 모델 카드. 입출력(언어+영상 → 정규화 7자유도 엔드이펙터 변위, 로봇·데이터셋별 역정규화)과 '모든 체크포인트 MIT' 문구를 현재 main(커밋 47a0ec7, 2026-02-17)에서 확인했다. 메모가 고정한 리비전 258bd1d 는 현재 main 이력에 없다.
- **ref-1610**: π0 계열 공개 구현 openpi. 원격 추론의 행동 청크 형태(action_horizon, action_dim)와 개방 루프 실행 주석, 제공 체크포인트(π0·π0-FAST·π0.5), LICENSE(Apache 2.0)를 확인했다. 커밋 날짜는 확인하지 못했다.
- **ref-1611**: GR00T N1.7 공식 저장소 README. Early Access 릴리스 표기(49–59행), 소개 문단의 'Apache 2.0 으로 완전히 상용 라이선스 가능'(71행), License 절의 코드 Apache 2.0·가중치 NVIDIA Open Model License 구분(514–517행)을 확인했다. 브랜치 이름 기준이며 커밋 sha 로 고정하지 못했다.
- **ref-1612**: GR00T N1.7 3B 가중치 저장소. LICENSE(커밋 6949d5d, 2026-02-25; 현재 main 과 같음)의 'NVIDIA License' 3.3절 비상업 한정·NVIDIA 계열사 예외와, 모델 카드(main)의 'NVIDIA Open Model License'·'commercial/non-commercial use' 문구를 확인했다.
- **ref-1613**: Physical Intelligence 의 π0.7 기술 보고서(v1 2026-04-16, v2 2026-04-24). v2 HTML 에서 제어 모드 프롬프트(joint/ee), 학습 중 0~12 타임스텝 지연 모사(50 Hz 에서 240 ms), UR5e 20 Hz, seen/unseen 구분의 어려움을 확인했다. 회사 자체 보고서다.
- **ref-1614**: VLA 모델의 7개 축 입력 교란 견고성 평가 프리프린트(v1 2025-10-15, v3 2025-12-26). v3 HTML 의 §2.1 과 표 1(OpenVLA-OFT 원본 97.1·카메라 59.7·로봇 초기 상태 37.2)을 확인했다. 학회 게재본(ref-1615)과 수치가 다르다.
- **ref-1615**: LIBERO-Plus 의 CVPR 2026 게재본(pp.38574–38583, arXiv 판과 제목이 다름). 표 2 의 OpenVLA-OFT 행(원본 97.1·카메라 56.4·로봇 31.9·전체 69.6)을 PDF 원문에서 확인했다.
- **ref-1616**: ROSA 공식 위키 FAQ(릴리스에 고정되지 않은 문서). 핵심 에이전트는 물리 세계와 상호작용할 수 없고 맞춤 도구·프롬프트가 필요하다는 한계와, 맞춤 도구에 상태·능력 확인과 안전 검사를 넣으라는 권고를 확인했다. README(ref-171)·Custom Agents 위키(ref-172)와 다른 페이지다.
- **ref-1617**: MCP 프로젝트 공식 블로그 해설. 도구 어노테이션은 위험 힌트이며 실행 강제 수단이 아니라는 설명('They aren't enforcement.')을 확인했다. 규범 명세 자체는 아니다.
- **ref-1618**: MoveIt Pro 제품 문서의 MCP 서버 연결 안내. 배포 키 읽기 전용, 서버의 확인 프롬프트 없음, 세션 종료 뒤 로봇 계속 이동, cancel_objective 는 비상 정지가 아님 등 권한·실행 설명을 확인했다. 세부 제품 빌드와 발행일은 확인하지 못했다.
- **ref-1619**: Figure 02 의 BMW 스파턴버그 배치를 회고한 Figure AI 발표. 11개월 배치, 6개월·10개월 이정표, 6개월 일일 가동·1,250시간 이상, 교대당 99% 초과 성공률·개입 0회 목표를 확인했다.
- **ref-1620**: Figure 03 이 BMW 스파턴버그에서 물류 작업 흐름을 수행한 '첫 시연'과 Helix 02 전신 제어를 설명한 Figure AI 발표. BMW 보도자료(ref-1051)와 같은 프로젝트의 당사자 자료다.
- **ref-1621**: 산업부–서울대 M.AX 얼라이언스 협력 MOU 보도자료. 휴머노이드 분과 'AI 파운데이션 모델 개발'(2025~2028년, 484억 원, 장병탁·박재흥) 과제 표를 확인했다. 보도자료라 medium.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md | 5, 6, 7, 8, 9, 11 | 갱신(차등): 섹션 5 — 제조 공장: 93행 'Figure AI 자체 발표로는 교차 확인하지 못했다'를 'Figure AI 자체 발표(2026-06-30 F.03 첫 시연, 2025-11-19 F.02 회고)가 같은 내용을 설명하나 같은 프로젝트 당사자 자료라 독립 확인은 아니다'로 정정(f37, 벤더 주장 [추정]). 89·91행 10/11개월 충돌은 기존 내용 확인(5절 89·91행, oq-219) — 새로 넣지 말고 11개월은 Figure CEO 인용·10개월은 본문이라는 위치와 Figure 쪽 세 기간 축(6·10·11개월, 6개월 일일 가동·1,250시간)만 보탬(f34). 예외·성과 칸에 99% 초과 성공률·개입 0회는 목표치(f35), Figure 03 은 첫 시연(f36). 연구 실물 사례로 IMR-LLM 로봇 팔 3대 단일 장면(전문가 15분 장면 작성, 반복 미보고, f5)을 '연구 평가'로 표시해 추가할 수 있음. 물류창고: 산업부 M.AX 휴머노이드 과제(f38)는 로보티즈–BGF로지스 과제와 동일성 미확인이라 별도 문장으로, 80/90 실측 없음 유지; 의견 f41·f46 / 섹션 6(분리 2026-09-30-area44-s6) — 다중 로봇 계획 소절: SMART-LLM 36개 지시·1~4대·AI2-THOR(f1, C 트랙 stage-2 166행의 '원문 미열람' 수치를 원문 확인으로 보강), 불가능 과제의 모델별 차이(f2). IMR-LLM 23장면·50작업(f3), FIFO 휴리스틱(f4), 복잡 과제 성공률 하락과 도달 불가 배정(f6). 57행 '선택 그래프(disjunctive graph)'는 위키 안에서 '선언 그래프'(C 트랙 stage-1 112행)·'이접 그래프'(같은 파일 240행)와 갈리므로 한 용어로 통일 제안(이번 갱신은 s6 만, 트랙 페이지는 후속 정리). 기호 계획기 소절: LLM+P 의 사람 제공 도메인 전제(f7). 불확실도 소절: S-ATLAS 의 i.i.d.·무오류 실행·정확한 도움 전제와 110개 시뮬레이션 시나리오(f8~f10)를 KnowNo 다음에 추가; 의견 f39·f40 / 섹션 7(분리 2026-09-30-area44-s7) — 표 아래 'OpenVLA의 라이선스는 확인하지 못했다'를 정정: 코드 MIT(f12), README 의 Llama Community License '적용될 수 있다'(f13), HF 카드 '모든 체크포인트 MIT'(f14)를 충돌 그대로 병기하고 해소하지 않음. 입출력 계약: OpenVLA 역정규화(f11), openpi 행동 청크·개방 루프(f15·f16), openpi 체크포인트에 π0.7 없음(f17). GR00T 행: N1.7 은 EA(f18), README License 절 코드/가중치 구분(f19), README 71행 '상용 가능' 문구는 벤더 주장(f20), 3B LICENSE 3.3절 비상업·NVIDIA 예외(f21), 세 문서 충돌(f22) — 표의 'GR00T N1 오픈소스(공개 모델)' 유형 칸에 '코드 Apache 2.0, 가중치 별도 라이선스' 주석. ROSA 행: FAQ 의 물리 상호작용 조건(f28)과 맞춤 도구 안전 검사 권고(f29). MCP 어노테이션 한계(f30)는 7절 또는 9절에 두되 기존 MCP 명세 서술(2026-09-29-area13-s6.md 45행 ref-856, C 트랙 stage-4 253행 ref-696)과 보완 관계로 적고 재서술하지 않음; 의견 f42·f43 / 섹션 8(분리 2026-09-30-area44-s8) — π0.7 항목 추가: 제어 모드 프롬프트(f23), 학습 중 지연 모사 240 ms(50 Hz)·UR5e 20 Hz(f24), seen/unseen 판정 어려움(f25) — 모두 회사 자체 보고서라 [추정]. LIBERO-Plus 항목 추가: 7개 교란 축(f26), OpenVLA-OFT 수치는 판을 밝혀 arXiv v3(로봇 37.2·카메라 59.7)와 CVPR 2026 게재본(로봇 31.9·카메라 56.4) 병기(f27). 국내 동향에 산업부 M.AX 휴머노이드 AI 파운데이션 모델 과제(f38); 의견 f44 / 섹션 9 — 로봇 자체 지능·제어 경계 아래에 도구 호출 실행 경계 문단: MCP 힌트는 강제 수단이 아님(f30), MoveIt Pro 의 읽기 전용 배포 키·서버 확인 프롬프트 없음·세션 종료 뒤 계속 이동·cancel 은 비상 정지 아님(f31~f33, 벤더 주장 [추정]), ROSA 맞춤 도구 조건(f28·f29); 의견 f45 / 섹션 11(분리 2026-09-30-area44-s11) — 부분 답(열린 채 둠): oq-216(배포물별 입출력 f11·f15·f16·f23, 의견 f42; 공통 등록 표준·적합성 시험 미확인), oq-217(연구 벤치마크 규모·조건 f1~f6·f8~f10·f26·f27; 설비·안전·시간창 통합 공통 기준 미확인), oq-219(Figure 기간 축 f34; 기점·종점 없어 미해소), oq-141(MoveIt Pro 는 승인을 클라이언트에 맡김 f32, 벤더). 관련 근거만: oq-104(f24 학습 조건 지연, 실측 아님), oq-218(f38, 실측 결과 없음). 답하지 못함: oq-314, oq-161. 메모 새 질문 1번(VLA 공통 최소 항목)은 문구 대조로 oq-216 과 같아 새로 만들지 않음; 2·3번과 라이선스 출처 충돌 2건을 새로 올림 / 후속 정리(이번 갱신 범위 밖, 다른 페이지): docs/standards/index.md 287·288행 OpenVLA·GR00T N1 '오픈소스' 유형에 코드·가중치 라이선스 구분(f12~f14, f19~f22); docs/tracks/chat-based-configuration-and-operation/stage-1-prior-work-and-products.md 118행 ROSA [추정] '확인·권한 장치 설명 없음'을 FAQ(f29)로 정리, 같은 파일 112·240행과 2026-09-30-area44-s6.md 57행의 disjunctive graph 번역어 통일, 같은 파일 310행 'IMR-Bench 규모 미확인'에 f3 연결; stage-2-data-and-standards.md 166·370행 SMART-LLM '원문 미열람'에 f1 연결; task-model-draft.md 133행 LLM+P 부분에 f7 연결. 다음 실행 후보: 59. 법·규제·보험·라이선스(f12~f22), 13. 대화형 기능의 신뢰·기반(f30~f33), 54. 시험·형식 검증·벤치마크(f26·f27) |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- 언어 모델 다중 로봇 계획의 검증이 기대는 가정(사람이 준 도메인 판, i.i.d. 시나리오, 무오류 스킬 실행)을 런타임에서 누가 감시하고, 가정이 깨졌을 때 어떤 계획을 중단·재검증할 것인가? | 관련 영역: 44. 로봇 기반 모델·언어 모델 계획, 54. 시험·형식 검증·벤치마크 | 근거: f9 | 종류: 일반
- 원격 VLA 정책의 행동 청크(개방 루프 실행) 유효기간과, 도구 세션이 끝난 뒤에도 로봇이 움직일 수 있는 MCP 실행의 안전한 정지 계약을 어떻게 결합할 것인가? | 관련 영역: 44. 로봇 기반 모델·언어 모델 계획, 29. 명령·작업 실행의 신뢰성 | 근거: f16 | 종류: 일반
- 출처 충돌: OpenVLA 공개 가중치의 사용 조건은 저장소 README(Llama 2 파생이라 Llama Community License 가 적용될 수 있음)와 Hugging Face 모델 카드(모든 체크포인트 MIT) 가운데 어느 쪽인가? | 관련 영역: 44. 로봇 기반 모델·언어 모델 계획, 59. 법·규제·보험·라이선스 | 근거: f14 | 종류: 출처 충돌
- 출처 충돌: GR00T N1.7 가중치의 상업적 사용 가능 여부는 README 소개(Apache 2.0 으로 상용 가능), README License 절·3B 모델 카드(NVIDIA Open Model License, 상업·비상업 사용 준비), 3B 가중치 저장소 LICENSE 3.3절(NVIDIA·계열사 외 비상업 한정) 가운데 어느 문서가 정하는가? | 관련 영역: 44. 로봇 기반 모델·언어 모델 계획, 59. 법·규제·보험·라이선스 | 근거: f22 | 종류: 출처 충돌

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 19 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 15건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-12-05/external_research.md)를 변환했다. 2026-10-12 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.
    - f14·f22: OpenVLA·GR00T N1.7 의 라이선스 문서 충돌은 문서끼리 대조한 것이며 배포자의 정정·법적 우선순위는 확인하지 못함. OpenVLA 카드는 메모의 고정 리비전 258bd1d 가 현재 main 이력에 없어 main(47a0ec7) 기준
    - ref-1608·ref-1610: OpenVLA 커밋 c8f03f4, openpi 커밋 215abfb 의 커밋 날짜 미확인. ref-1611: GR00T n1.7-release 는 브랜치 이름으로만 열어 커밋 sha 고정 못 함. ref-1618: MoveIt Pro 문서 세부 빌드·발행일 미확인
    - f17: openpi 에 π0.7 가중치가 없음을 README 목록으로 확인했을 뿐, π0.7 보고서와 공개 배포물의 대응(U10)·실제 네트워크 포함 최대 지연(U11)은 미확인
    - f10: S-ATLAS 실물 실험이 없다는 것은 열람 본문 검색 기준이며 보충 자료는 보지 않음. SMART-LLM 실물 시험 대수·반복 수(U03), IMR-LLM 장기 운영(U04) 미확인
    - f34: BMW–Figure 10/11개월의 기점·종점과 집계 관계, 교대별 실측 성공률·개입 분모(U13·U14), Figure 03 첫 시연 이후 가동률(U15) 미확인
    - f38: 산업부 M.AX 휴머노이드 과제와 로보티즈–BGF로지스 물류 과제의 동일성(U17), 자동화율 80%·성공률 90% 실측 결과(U16, oq-218) 미확인
    - 메모 V01(GR00T-N1.7-ApplePnP-V1 모델 카드)와 V11(BGF로지스 매거진 회고)은 신규 출처 예산(15건) 때문에 출처째 넣지 않음. 둘 다 벤더 [추정]이며 ROP 판단에 쓰는 내용(라이선스 충돌·80/90 실측 부재)은 다른 finding 이 담음
    - 병원·상업시설·실외에서 로봇 기반 모델·언어 모델 계획을 쓴 이기종 플릿 현장 실증(U18), 벤더 혼합 장기 운영 플릿의 독립 재현 로그(U02), VLA 공통 능력 등록 표준·적합성 시험(U06) 미확인
    - 메모가 진단에 쓴 위키 고정 커밋(85960d2)과 현재 배포판의 동일성 미확인(U01)
- 범위 경계 위반 의심:
    - f12~f22: 코드·가중치 라이선스 문구는 59. 법·규제·보험·라이선스 쪽 내용이므로 문서 원문 대조까지만 하고 상용 사용 가능 여부의 법적 판단은 하지 않음
    - f30~f33: 도구 호출 권한·승인·세션 종료는 13. 대화형 기능의 신뢰·기반, 29. 명령·작업 실행의 신뢰성과 겹치며, 이 영역에는 언어 모델 계획이 로봇 실행으로 넘어가는 경계 관점으로만 씀
    - f26·f27: LIBERO-Plus 는 단일 팔 조작 시뮬레이션 벤치마크로 54. 시험·형식 검증·벤치마크와 겹치며, 이 영역에는 VLA 수용 시험 설계의 근거로만 씀
- 한계: 외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 15건/15(ref-1607~ref-1621, 예약 구간 ref-1607~ref-1636 안), 재사용 4건(ref-090·ref-170·ref-092·ref-1051). 출처 매핑(검증 결과 기준): 메모 n1→ref-090, n2→ref-170, n3→ref-092, n4→ref-1607, n5→ref-1608, n6→ref-1609(main 47a0ec7 기준), n7→ref-1610, n8(ApplePnP 카드)→예산 초과로 제외, n9→ref-1611, n10→ref-1613, n11→ref-1612(같은 저장소 모델 카드 포함), n12→ref-1617, n13→ref-1616(ref-171·172 와 다른 페이지), n14→ref-1618, n15→ref-1051(글로벌 URL, 캐나다판 대신), n16→ref-1619, n17→ref-1620, n18→ref-1621, n19(BGF 매거진)→예산 초과로 제외, n20→ref-1614, 추가: CVPR 2026 게재본→ref-1615. 모든 출처 원문 열람(fetched true). 출처 type: OpenVLA·openpi·GR00T 저장소와 Hugging Face 모델 저장소 파일은 프로젝트가 관리하는 저장소라 '오픈소스 문서'로 두어 인터페이스·라이선스 원문 옮김(f11~f19, f21·f22)은 [사실]; MoveIt Pro·Figure·BMW 는 '벤더 문서'라 해당 finding 은 모두 [추정]·vendor_claim. 교차 확인 0건(SMART-LLM/IMR-LLM/S-ATLAS 는 조건이 달라 같은 주장 아님, OpenVLA 문서쌍·GR00T 문서셋·openpi/π0.7·LIBERO-Plus 두 판·BMW/Figure 는 같은 팀·기관·프로젝트). 검증 반영: F21 은 arXiv v3 값(37.2)에 판을 명시하고 CVPR 2026 게재본 값(로봇 31.9·카메라 56.4) 병기(f27); F13 '적용된다'→'적용될 수 있다'(f13); F14 현재 main 도 같은 문구라 충돌 지속(f14); F18/README 71행 '상용 가능'은 벤더 주장으로 분리(f20)하고 README·LICENSE·카드 3자 충돌 기록(f22); F06 은 성공률 하락의 예시이며 정량화 없음; F02 에 GPT-4·Claude-3 거절과 표 I 밖 명시; F05 에 15분 수동 장면 작성·반복 미보고; U10 을 f17 로; U13 Figure 세 기간을 f34 로; 위키 5절 93행 정정 제안(f37). 중복 제거: F01 은 C 트랙 stage-2 166행 기존 수치의 원문 확인 보강으로만(f1), F07 은 기존 [추정] 보강, F23 은 기존 MCP 명세 서술과 보완 관계로 서술, V08(BMW 10/11개월 충돌)은 기존 5절·oq-219 에 있어 새 finding 으로 넣지 않고 f34 근거 메모와 rationale 에 위치만 적음. 열린 질문: 부분 답 oq-216·oq-217·oq-219·oq-141, 관련 근거 oq-104·oq-218, 해결 제안 없음(open_questions_resolved 비움). 메모 새 질문 1번은 oq-216 과 같아 만들지 않고, 2·3번과 출처 충돌 2건을 새로 올림. 메모의 '.research-work' 로컬 경로·행 번호는 쓰지 않고 원문 절·표·행(저장 원문 기준)과 위키 실제 위치를 적었다. 정정 요청 없음. 용어 후보 없음.
