# 1차 검증(브리프) 2026-10-12-05

**판정: 조건부 승인** · 신뢰도: medium

## 주장별 검증

| finding | 출처 실재 | 주장 뒷받침 | 교차 확인 | 태그 처분 | 메모 |
|---|---|---|---|---|---|
| f1 | 예 | 예 | 아니오 | 유지 | 확인: arXiv v2 HTML §V-A '36 high-level instructions', 과제별 로봇 1~4대, AI2-THOR(범주 6+8+14+8=36). 단일 출처. |
| f2 | 예 | 예 | 아니오 | 유지 | 확인: §VI-A GPT-4·Claude-3 은 배정 계획을 만들지 않았고 GPT-3.5·Llama2 는 부적합 로봇 배정, 'not included in Table I', 과제 수·실행 수 미보고. 'Claude-3 비교는 v2 에만 있다'는 검증에서 판 비교를 하지 않았으므로 본문에 쓰지 않는다. |
| f3 | 예 | 예 | 아니오 | 유지 | 확인: arXiv v1 §V-A 23장면(생산 라인 설계 전문가가 실제 산업 환경에서 수집·각색), 장면당 1~7대, 50작업, KunWu 플랫폼. ICRA 2026 채택은 ICRA 2026 수상 후보 목록에서 확인했으나 쪽수 pp.7609–7616 은 확인하지 못함. |
| f4 | 예 | 예 | 아니오 | 유지 | 확인: §IV-A 휴리스틱 FIFO 로 disjunctive graph 를 푼다(같은 상호배타 자원 작업은 작업 집합 순서로 처리). 전역 최적 보장으로 읽지 않는다는 단서 적절. |
| f5 | 예 | 예 | 아니오 | 유지 | 확인: §V-C 로봇 팔 3대, 전문가가 약 15분 걸려 수동 작성한 장면 설명, 시뮬레이션·실물 모두 반복 횟수·분산 미보고. |
| f6 | 예 | 예 | 아니오 | 유지 | 확인: §V-B 복잡 다중 로봇 작업의 SR 하락 원인을 잘못된 분해·배정(도달 불가 로봇 배정 예)으로 정성 서술. SR 하락 자체는 표 I 에 있으나(0.87→GPT-4o 0.68, Qwen3-32B 0.60) 원인별 빈도는 정량화하지 않음 — finding 문구와 일치. |
| f7 | 예 | 예 | 아니오 | 유지 | 확인: arXiv v3 §III-C 'a human expert can provide a domain description … available as a PDDL domain file', 언어 모델은 problem PDDL 을 추론. |
| f8 | 예 | 예 | 아니오 | 유지 | 확인: arXiv v4 Remark III.6 보장은 'calibration and test scenarios are i.i.d.'일 때만. RA-L 10(1):160–167(2025-01)은 NSF PAR 기록으로 확인. arXiv 초판 제목은 'Safe Task Planning for Language-Instructed Multi-Robot Systems using Conformal Prediction'으로 달랐다. |
| f9 | 예 | 예 | 아니오 | 유지 | 확인: Theorem IV.2(a) 'Assuming error-free execution of the designed plans', 증명 Case II 는 사용자가 'faithfully provide help'를 전제(그렇지 않으면 분포 이동). |
| f10 | 예 | 예 | 아니오 | 유지 | 확인: §V-A '110 (validation) scenarios', N∈{1,3,10,15}, AI2-THOR. 검증 열람은 본문 앞 100,000자(전체 약 144,000자) 범위이며 그 범위에서 실물 실험 서술 없음 — '열람한 본문에서' 한정 표현 유지. |
| f11 | 예 | 예 | 아니오 | 유지 | 확인: HF openvla-7b 카드(main) Uses — 언어 지시+작업공간 카메라 영상 입력, 정규화된 7-DoF 엔드이펙터 변위 출력, 로봇·데이터셋별 통계로 un-normalize. |
| f12 | 예 | 예 | 아니오 | 유지 | 확인: 커밋 c8f03f4 README 'all code in this repository is released under an MIT License'. 커밋 날짜 미확인. |
| f13 | 예 | 예 | 아니오 | 유지 | 확인하되 표현 주의: README 는 'may inherit restrictions'(제약을 물려받을 수 있다)라고 한 뒤 'both … derived from Llama-2, and as such are subject to the Llama Community License'라고 단정한다. '적용될 수 있다'로 뭉뚱그리지 말고 두 문장을 원문대로 구분해 서술(수정 지시). |
| f14 | 예 | 예 | 아니오 | 유지 | 확인: 카드(main) 'All OpenVLA checkpoints, as well as our training codebase are released under an MIT License', 메타데이터 license: mit. README 와 충돌. 카드 커밋 47a0ec7 의 날짜(2026-02-17)는 검증에서 확인하지 않음. 같은 팀 자료라 독립 확인 아님 — 충돌 병기·열린 질문 처리 적절. |
| f15 | 예 | 예 | 아니오 | 유지 | 확인: docs/remote_inference.md 'This returns an action chunk of shape (action_horizon, action_dim).' |
| f16 | 예 | 예 | 아니오 | 유지 | 확인: 같은 파일 '… from the predicted action chunk open-loop in the remaining steps.' 예시 설명이며 안전 정지 근거 아님이라는 단서 적절. |
| f17 | 예 | 예 | 아니오 | 유지 | 확인: README Base Models 표 pi0_base·pi0_fast_base·pi05_base, π0.7 없음. '기반 체크포인트' 한정을 유지한다(미세조정 체크포인트 목록과 혼동하지 않음). |
| f18 | 예 | 예 | 아니오 | 유지 | 확인: n1.7-release README 'Early Access (EA) release … support and stability guarantees are limited until the GA release', GA 항목 'Production deployment with commercial support'. 브랜치 기준 열람(커밋 미고정) — 기준일 2026-10-12 명시 필요. |
| f19 | 예 | 예 | 아니오 | 유지 | 확인: License 절 Code Apache 2.0, Model weights NVIDIA Open Model License. |
| f20 | 예 | 예 | 아니오 | 유지 | 확인: README 'fully commercially licensable under Apache 2.0' 문구 존재, 같은 문서 License 절과 불일치. [추정]·벤더 주장 유지. |
| f21 | 예 | 예 | 아니오 | 유지 | 확인: 커밋 6949d5d LICENSE 표제 'NVIDIA License', §3.3 비상업 한정·NVIDIA 및 계열사 상업 사용 예외·'non-commercially' = 연구·평가 목적. |
| f22 | 예 | 예 | 아니오 | 유지 | 확인: 3B 카드 'released under the NVIDIA Open Model License Agreement', 'ready for commercial/non-commercial use'; README·LICENSE 와 함께 세 갈래 서술. 모두 NVIDIA 자료라 독립 확인 아님. 이 finding 은 GR00T N1.7 에 관한 것이며 GR00T N1(ref-1049) 행에 옮겨 적지 않는다(수정 지시). |
| f23 | 예 | 예 | 아니오 | 유지 | 확인: arXiv v2 §V-D c∈{joint, ee}, 'at runtime, we can pick the control mode depending on the task'. 회사 자체 보고서 [추정]·벤더 주장 유지. |
| f24 | 예 | 예 | 아니오 | 유지 | 확인: §VI-B 학습 중 0~12 타임스텝 지연 모사, 50Hz 에서 최대 240ms; 'The UR5e robots run at 20 Hz'. 학습 조건이며 실측 지연 아님이라는 단서 유지. |
| f25 | 예 | 예 | 아니오 | 유지 | 확인: Discussion 에서 seen/unseen 을 'practically difficult' 하게 구분한다고 한계로 적음. [추정] 유지. |
| f26 | 예 | 예 | 아니오 | 유지 | 확인: arXiv v3 §2.1 일곱 단일 축 교란(물체 배치·카메라 시점·로봇 초기 상태·언어 지시·조명·배경 질감·센서 잡음). CVPR 2026 게재(pp.38574–38583, 다른 제목)는 CVF 오픈액세스 HTML·포스터 페이지로 확인, 게재본 PDF 는 검증에서 403 으로 열지 못함. |
| f27 | 예 | 아니오 | 아니오 | 강등 | 사실 → 추정: '판마다 다르다'는 해석이 틀렸다. arXiv v3 안에 두 표가 모두 있다 — 표 1(원래 LIBERO 설정의 단일 축 교란 분석: OpenVLA-OFT 원본 97.1·카메라 59.7·로봇 초기 상태 37.2)과 표 2(LIBERO-Plus 벤치마크 견고성 평가: 카메라 56.4·로봇 31.9·전체 69.6). 수치 차이는 판 차이가 아니라 평가 설정 차이다. 게재본 표 2 의 'Original 97.1' 열은 게재본 PDF 를 열지 못해 검증에서 확인하지 못함. 수정 지시대로 고쳐 쓴다. |
| f28 | 예 | 예 | 아니오 | 유지 | 확인: ROSA Wiki FAQ(raw) 'limited to text-based interactions and cannot interact with the physical world', 맞춤 도구·프롬프트 필요. 릴리스 미고정 위키 문서 — 접근일 기준 명시. |
| f29 | 예 | 예 | 아니오 | 유지 | 확인: 같은 FAQ 의 맞춤 도구 매개변수 검증·행동 제한, 실행 전 로봇 상태·능력 확인 권고. 권고이며 자동 제공 기능 아님이라는 단서 유지. |
| f30 | 예 | 예 | 아니오 | 유지 | 확인: MCP 블로그(2026-03-16, Hungerford·Morrow·Chang) 'They aren't enforcement.' … 'a job for network controls or sandboxing'. 규범 명세가 아닌 해설 글임을 명시. |
| f31 | 예 | 예 | 아니오 | 유지 | 확인: MoveIt Pro 문서(Version 10) 배포 MCP 키 읽기 전용, 동작은 호스트 사용자 세션에서 기존 Objective 시작·취소로 한정. [추정]·벤더 주장 유지. 발행일 미확인. |
| f32 | 예 | 예 | 아니오 | 유지 | 확인: 'clients may auto-approve calls. The server adds no confirmation prompt.' [추정]·벤더 주장 유지. |
| f33 | 예 | 예 | 아니오 | 유지 | 확인: run_objective 'keeps moving if the session ends', cancel_objective 'best effort, not an emergency stop', 물리 비상정지 대체 불가. [추정]·벤더 주장 유지. |
| f34 | 예 | 예 | 아니오 | 유지 | 확인: Figure 발표(2025-11-19) '11 month … deployment', 6개월 안 납품·시험, 10개월 안 전면 배치, 6개월 일일 가동·1,250시간 이상. BMW 보도자료(2026-06-25) 재열람: 'over ten months'는 본문, '11-month'는 Figure CEO Brett Adcock 인용. 당사자 자료라 독립 확인 아님. [추정]·벤더 주장 유지. |
| f35 | 예 | 예 | 아니오 | 유지 | 확인: 'Our target was > 99% success per shift.', 'The goal was zero per shift.' 달성 여부 미기재. 목표치로만 적는다. |
| f36 | 예 | 예 | 아니오 | 유지 | 확인: 'F.03 Arrives at BMW'(2026-06-30) 'first demonstration of Figure 03 performing a logistics workflow at BMW Group Plant Spartanburg', Helix 02 'pixels-to-actions VLA'가 손·팔·몸통·발을 조율해 바퀴 달린 무거운 대차를 끎. [추정]·벤더 주장 유지. |
| f37 | 예 | 예 | 아니오 | 유지 | 확인: Figure 자체 발표 2건이 실재하므로 대상 페이지 5절의 'Figure AI 자체 발표로는 교차 확인하지 못했다'는 사실과 맞지 않음. 정정 문구는 '당사자 발표가 일치함(독립 확인 아님)'으로 한다. |
| f38 | 예 | 예 | 아니오 | 유지 | motir.go.kr 원문은 검증에서 두 번 모두 ECONNRESET 으로 열지 못했고 검색에도 이 URL 이 나오지 않았다(원문 미열람(검증)). 내용(2025-11-24 산업부–서울대 MOU, 휴머노이드 AI 파운데이션 모델 2028년까지 484억 원, 장병탁·박재흥, 기업 데이터·플랫폼 제공 → 서울대 모델 개발 → 기업 탑재)은 같은 발표를 다룬 언론 보도 검색 결과와 일치. 보도는 보도자료에서 나온 것이라 독립 교차 확인으로 세지 않음. medium 상한. |
| f39 | 예 | 예 | 아니오 | 유지 | [의견] 유지. 근거 f2·f6 은 확인됨. 누구의 의견인지(이 위키·구축자 의견) 밝힌다(수정 지시). |
| f40 | 예 | 예 | 아니오 | 유지 | [의견] 유지. 근거 f4·f7·f8·f9 확인. 구축자 의견 표시 필요. |
| f41 | 예 | 예 | 아니오 | 유지 | [의견] 유지. 근거 f5 확인. 구축자 의견 표시 필요. |
| f42 | 예 | 예 | 아니오 | 유지 | [의견] 유지. 근거 f11·f15·f16·f23 확인. 'ROP 설계 제안이며 표준이 아니다' 단서 유지, 구축자 의견 표시. |
| f43 | 예 | 예 | 아니오 | 유지 | [의견] 유지. 근거 f12~f14·f18~f22 확인. 법률 판단 아님 단서 유지. |
| f44 | 예 | 예 | 아니오 | 유지 | [의견] 유지하되 근거 f27 의 해석 오류를 따라 '판(arXiv 판·게재본)을 밝혀'를 '표·평가 설정(단일 축 교란 분석인지 벤치마크 평가인지)과 판을 밝혀'로 고친다(수정 지시). |
| f45 | 예 | 예 | 아니오 | 유지 | [의견] 유지. 근거 f28~f33 확인. 물리 비상정지는 연계 대상으로 쓴다(범위 수정 지시). |
| f46 | 예 | 예 | 아니오 | 유지 | [의견] 유지. 근거 f34~f38 확인. 구축자 의견 표시 필요. |

## 항목별 결과

| 항목 | 결과 | 내용 |
|---|---|---|
| 분류 적합성 | 예 | — |
| 범위 경계 | 예 | f31~f33·f45 (9절 도구 호출 실행 경계): MoveIt Pro 의 cancel_objective·물리 비상정지 서술을 ROP 가 비상정지를 제공하는 것처럼 쓰면 범위 위반이다. 물리 비상정지와 로봇 런타임 정지는 로봇 자체 지능·제어/설비 안전 제어의 연계 대상으로 짧게 적고, ROP 는 권한·승인·완료 판정·정지 절차 연결만 맡는 것으로 쓴다., f12~f22: 코드·가중치 라이선스의 적용 판단은 59. 법·규제·보험·라이선스 쪽 연계 대상이며 7절에서는 문서 문구 대조까지만 쓴다(브리프 self_check 와 같은 판단). |
| 중복·모순 | 예 | f1 은 chat-based-configuration-and-operation 트랙 stage-2-data-and-standards.md 의 SMART-LLM 36개 지시 서술(원문 미열람)과 같은 수치 — 원문 확인 보강으로만 쓰고 기존 각주 ref-090 재사용, f30 은 2026-09-29-area13-s6.md(ref-856)·트랙 stage-4(ref-696)의 MCP 명세 서술과 같은 방향 — 보완 관계로 짧게 쓰고 재서술하지 않음, f34 는 대상 페이지 5절의 10/11개월 충돌과 oq-219 에 이미 있는 내용 — 위치(CEO 인용·본문)와 Figure 쪽 기간 축만 보탬, f22 는 2026-09-30-area44-s7.md 표의 'GR00T N1 — 오픈소스(공개 모델)' 행과 대상 모델 판이 다름(N1.7 대 N1) — 충돌로 처리하지 말고 별도 판으로 구분 |
| 용어 일관성 | 예 | disjunctive graph 번역어가 위키 안에서 '선택 그래프'(2026-09-30-area44-s6.md)·'선언 그래프'·'이접 그래프'(트랙 stage-1)로 갈림. 용어집에는 항목이 없음. 이번 갱신 페이지에서는 '이접 그래프(disjunctive graph)'로 통일하고 다른 페이지는 후속 정리로 남긴다. |
| 인용 길이·저작권 | 예 | — |
| 정정 요청 반영 | — | — |

## 수정 지시(required_fixes)

- f27: [사실] → [추정]으로 강등하고 문장을 고쳐 쓴다 — 'arXiv v3 안의 표 1(원래 LIBERO 설정의 단일 축 교란 분석: OpenVLA-OFT 원본 97.1, 카메라 시점 59.7, 로봇 초기 상태 37.2)과 표 2(LIBERO-Plus 벤치마크 견고성 평가: 카메라 56.4, 로봇 31.9, 전체 69.6)는 평가 설정이 다른 두 표'로 쓰고, '판마다 다르다'·'arXiv 판과 게재본의 수치 차이' 표현은 지운다 — 검증에서 두 표가 모두 arXiv v3 에 있음을 확인했고, 게재본 PDF 는 열지 못해 게재본 '원본 97.1' 열은 확인하지 못했다.
- f44: '벤치마크 수치는 판(arXiv 판·게재본)을 밝혀 인용하며'를 '벤치마크 수치는 표·평가 설정(단일 축 교란 분석인지 벤치마크 평가인지)과 판을 밝혀 인용하며'로 고친다 — 근거 f27 의 해석이 바뀌었다.
- 8절(분리 2026-09-30-area44-s8) LIBERO-Plus 항목: 수치 병기를 위 f27 수정 문구로 하고, ref-1615(CVPR 2026 게재본, 제목 다름)는 게재 사실·일곱 교란 축의 근거로만 각주를 단다.
- f13: 'Llama Community License 가 적용될 수 있다'로 뭉뚱그리지 말고 README 원문대로 '사전학습 모델이 기반 모델의 제약을 물려받을 수 있다'와 '두 모델은 Llama 2 에서 파생돼 Llama Community License 를 따른다고 적는다'를 구분해 쓴다 — README 는 뒤 문장을 단정형('are subject to')으로 적는다. 법적 적용 판정이 아님은 유지한다.
- 7절(분리 2026-09-30-area44-s7) GR00T 서술: f18~f22 는 GR00T N1.7(ref-1611·ref-1612)에 관한 것이므로 기존 'GR00T N1(ref-1049) — 오픈소스(공개 모델)' 행의 유형 칸을 N1.7 근거로 고치지 않는다. N1.7 을 별도 행이나 별도 문장으로 두고 'EA 릴리스, 코드 Apache 2.0, 가중치는 문서마다 조건이 다름(README 소개·License 절·3B 카드·3B LICENSE 3.3절)'으로 적는다 — N1 의 가중치 라이선스는 이번 브리프에 근거가 없다.
- 7절: 표 바로 아래 'OpenVLA의 라이선스는 확인하지 못했다'를 지우고 코드 MIT(f12), README 의 Llama 2 파생 문구(f13), HF 카드 '모든 체크포인트 MIT'(f14)를 충돌 그대로 병기하며 어느 쪽도 고르지 않는다. 충돌은 open_questions_new 의 출처 충돌 질문으로 연결한다.
- 5절 제조 공장 사례: 'Figure AI 자체 발표로는 교차 확인하지 못했다'를 지우고 'Figure AI 자체 발표(2025-11-19 F.02 회고, 2026-06-30 F.03 첫 시연)가 같은 배치·착수를 설명하나 같은 프로젝트 당사자 자료라 독립 확인은 아니다'로 고친다(f37). [추정] 벤더 주장 표기와 각주 ref-1619·ref-1620·ref-1051 을 단다.
- 5절 제조 공장 예외·성과 칸: '교대당 99% 초과 성공률·개입 0회'는 '목표치(실측 아님)'로만 적고(f35), 10/11개월 문장에는 11개월이 Figure CEO 인용, 10개월이 BMW 본문이라는 위치와 Figure 쪽 6·10·11개월 이정표를 덧붙이되 하나로 정하지 않는다(f34). oq-219 는 열림 유지.
- 5절에 IMR-LLM 실물 시험(f5)을 넣을 경우 '연구 평가(로봇 팔 3대 단일 장면, 전문가 약 15분 수동 장면 작성, 반복 횟수 미보고)'로 표시하고 장기 운영 실적으로 쓰지 않는다. 현장 유형은 '제조 공장'으로 명시하고 여섯 항목 가운데 근거 없는 칸은 '미확인'으로 둔다.
- 5절 물류창고: 산업부 M.AX 휴머노이드 과제(f38)는 로보티즈–BGF로지스 과제(ref-1052)와 별도 문장으로 쓰고 같은 사업인지 미확인임을 밝힌다. ref-1621 각주는 검증에서 원문을 열지 못했으므로 기준일(2025-11-24 등록)을 반드시 남긴다.
- 9절: 도구 호출 실행 경계 문단에서 물리 비상정지·런타임 소프트웨어 정지는 '연계 대상'(로봇 자체 제어·설비 안전 제어)으로 짧게 적고, ROP 가 직접 맡는 것은 읽기/실행 권한, 승인된 계획 대상 확인, 완료 판정, 세션 종료와 정지 절차의 연결로 한정한다. MoveIt Pro 서술(f31~f33)은 모두 [추정] 벤더 주장, MCP 블로그(f30)는 '규범 명세가 아닌 프로젝트 해설'임을 밝힌다.
- f39~f46: [의견] 문장마다 누구의 의견인지 밝힌다(예: '이 위키의 의견' 또는 '구축자 의견'). 외부 조사 메모의 시사점을 옮긴 것이므로 출처의 주장처럼 쓰지 않는다.
- 6절(분리 2026-09-30-area44-s6): 57행 '선택 그래프(disjunctive graph)'를 '이접 그래프(disjunctive graph)'로 고친다. 트랙 페이지 등 다른 페이지의 번역어는 이번 갱신에서 고치지 않고 후속 정리로 남긴다.
- ref-170(IMR-LLM): ICRA 2026 채택은 적을 수 있으나 쪽수(pp.7609–7616)는 검증에서 확인하지 못했으므로 본문·각주에 쓰지 않는다. 같은 이유로 SMART-LLM 의 IROS 2024 쪽수(pp.12140–12147)도 쓰지 않는다.
- f18·f28: 브랜치·위키 문서처럼 판이 고정되지 않은 출처(ref-1611 n1.7-release 브랜치, ref-1616 ROSA Wiki FAQ)는 본문 또는 각주에 '접근일 2026-10-12 기준'임을 밝힌다.
- 11절(분리 2026-09-30-area44-s11): oq-216·oq-217·oq-219 는 '부분 근거'로만 연결하고 상태는 열림 유지. oq-141 은 이 영역 질문 목록에 없으므로 13. 대화형 기능의 신뢰·기반 쪽 질문으로 연결만 하고 이 페이지에서 상태를 바꾸지 않는다. open_questions_new 4건은 브리프 문구대로 등록한다.
- 각주 정의: 이번에 다시 연 기존 출처(ref-090·ref-170·ref-092·ref-1051)를 갱신하는 절은 접근일을 2026-10-12 로 쓰고, 새 출처 ref-1607~ref-1621 은 브리프의 기관·제목·발행일(없으면 '미확인')·URL 그대로 각주를 단다.

## 검증 노트

판정: 조건부 승인. 확인 45건, 미확인 1건, 교차 확인 0건. 강등: f27 사실 → 추정(LIBERO-Plus 수치 차이는 arXiv 판과 게재본의 차이가 아니라 arXiv v3 안의 표 1(단일 축 교란 분석)과 표 2(벤치마크 평가)의 평가 설정 차이). 원문 미열람 출처: ref-1621(검증에서 두 차례 접속 실패. 내용은 2025-11-24 협약 보도와 일치), ref-1615 게재본 PDF(HTML·포스터 페이지로 실재만 확인). 주의: 모든 [사실] finding 은 단일 출처이거나 같은 팀·기관·프로젝트 자료여서 독립 교차 확인이 없다. OpenVLA(코드 MIT, README 의 Llama 2 파생 문구, HF 카드의 모든 체크포인트 MIT)와 GR00T N1.7(README 소개의 Apache 2.0 상용 가능, License 절·3B 카드의 NVIDIA Open Model License, 3B LICENSE 3.3절 비상업 한정)의 라이선스 문서는 서로 충돌하며 어느 쪽도 고르지 않았다. 법적 판단도 아니다. GR00T N1.7 근거를 GR00T N1 행에 옮겨 적지 않는다. Figure·BMW·MoveIt Pro·π0.7 서술은 벤더 주장이고, 99% 성공률·개입 0회는 목표치다. ICRA 2026·IROS 2024 쪽수는 확인하지 못했다. 브리프 출처 가운데 ref-1051·ref-1617~ref-1621 은 fetched: true 인데 fetch_url 이 비어 있다. 검증에서 ref-1051·ref-1617~ref-1620 은 열람을 확인했다. 정정 요청 없음. 갱신 범위가 대상 페이지와 분리 주제 페이지(s6·s7·s8·s11)에 걸친다.
