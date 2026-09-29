---
title: "13. 대화형 기능의 신뢰·기반"
type: area
category: "C. 채팅 기반 구성·운영"
area_no: 13
related_areas: [8, 9, 10, 11, 12, 20, 44, 47, 48, 51, 52, 53, 54, 57, 59, 64]
tags: [프롬프트 주입, 승인 관문, 불확실도 보정, 모델 대체, 대화 기록, 대화형 기능 평가]
status: published
confidence: medium
created: 2026-09-28
updated: 2026-09-29
sources: [ref-855, ref-856, ref-857, ref-858, ref-859, ref-860, ref-861, ref-862, ref-863, ref-864, ref-865, ref-866, ref-738, ref-867, ref-868, ref-351, ref-840, ref-165, ref-753]
last_run: 2026-09-29
version: 2
---

[홈](../../index.md) › [C. 채팅 기반 구성·운영](index.md) › 13. 대화형 기능의 신뢰·기반

# 13. 대화형 기능의 신뢰·기반

!!! info "소속 대분류"
    [C. 채팅 기반 구성·운영](index.md) — 핵심 질문:
    맵 작성, 시나리오 구성, 로봇 구성, 실제 상황 재현, 업무 지시를 비전문 사용자가 대화만으로 할 수 있게 하려면? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md) — 중심 영역(●) · 확장 아이디어: [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-29 · 마지막 실행: 2026-09-29
<!-- auto:page-status:end -->

## 1. 한 줄 정의

오해석 방지, 권한, 모델 연결, 입력 채널, 대화와 화면 편집의 연동, 평가처럼 대화 기능 전체를 믿고 쓰게 하는 기반 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **오해석 방지·근거 표시**: 해석의 근거(장소·물품·문서 식별자)를 보여 주고, 없는 물품이나 검토되지 않은 문·측정값을 모델이 지어내지 못하게 막는다
- **대화 권한·기록 보호**: 사용자별로 대화로 지시할 수 있는 로봇·구역·작업의 범위를 제한하고 대화 기록을 보존·보호한다
- **언어 모델 연결·교체**: 언어 모델 공급자를 고르고 바꾸며 자격 증명을 보호하고, 모델 장애 때 임의로 다른 모델로 넘기지 않는다
- **대화형 기능 평가**: 해석·분해 정확도, 배정 적합성, 질문 횟수, 구성 완료 시간 같은 지표와 시나리오 시험으로 대화 기능을 평가한다
- **대화와 화면 편집 연동**: 지도에서 고른 장소·로봇 같은 화면 선택이 대화에 그대로 반영되고, 대화로 바꾼 내용이 편집 화면에 바로 보이게 한다
- **음성·다국어·현장 단말 대화**: 현장 사람이 음성·모바일·태블릿과 여러 언어로 지시하고 질문한다

## 2. 핵심 질문

언어 모델의 해석이 틀려도 잘못된 실행으로 이어지지 않게 하려면 무엇을 갖춰야 하는가? [분류원문]

## 3. 왜 중요한가

언어 모델의 오해석뿐 아니라 프롬프트 주입·탈옥 같은 외부 조작이 도구 호출이나 로봇의 물리 동작으로 이어진다는 위협을 서로 다른 세 발행 주체(OWASP, Robey 외, Huang 외)가 각각 보고했다. [사실][^ref-855][^ref-857][^ref-859] 이 영역이 없으면 8. 채팅으로 맵 작성부터 12. 채팅으로 업무 지시·오케스트레이션까지의 대화 기능은 편리한 만큼 위험해진다.

자세한 내용은 주제 페이지 [13. 대화형 기능의 신뢰·기반 — 왜 중요한가](../../topics/2026/2026-09-29-area13-s3.md)에 있다.

## 4. 핵심 개념과 용어

OWASP 가 낸 2025년판 LLM 응용 프로그램 Top 10 은 프롬프트 주입(LLM01), 민감 정보 노출(LLM02), 공급망(LLM03), 부적절한 출력 처리(LLM05), 과도한 에이전시(LLM06), 잘못된 정보(LLM09)를 포함한 열 가지 위험을 목록으로 정리한다. [사실][^ref-855] 아래 용어는 이 위험 목록과 그 방어·평가에서 이 영역이 자주 쓰는 것이다.

자세한 내용은 주제 페이지 [13. 대화형 기능의 신뢰·기반 — 핵심 개념과 용어](../../topics/2026/2026-09-29-area13-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

**현장 유형:** 상업 시설

**사례:** 네덜란드 슈퍼마켓에서 고객의 음성 질의에 상품 위치·정보를 안내하고 회수 요청을 받는 로봇

| 항목 | 내용 |
|---|---|
| 시작 조건 | 매장 고객이 로봇에게 영어 또는 네덜란드어 음성으로 상품을 묻거나 상품 회수를 요청한다. [사실][^ref-868] |
| 작업 대상 | 1,612개 상품 데이터베이스의 상품 정보와 고객의 질의(정보와 사람). [사실][^ref-868] |
| 수행 자원 | 로봇이 음성 인식(네 가지 기술을 비교해 Whisper 채택 근거 확보), 질의 분류기, 상·중·하 세 층의 언어 모델로 답한다. 사람은 고객으로서 질문하고 답을 평가한다. [사실][^ref-868] |
| 제약 | 영어·네덜란드어 두 언어와 성별 집단에 따른 음성 인식 정확도 차이, 모든 응답이 상품 데이터베이스 항목에 근거해야 한다는 조건. [사실][^ref-868] |
| 완료·인계 | 질의 분류기가 의도를 분류하고 상품 데이터베이스 항목을 참조한 답이 고객에게 전달되면 한 질의가 끝난다. [사실][^ref-868] |
| 예외·성과 | Whisper 가 성별·언어 집단(참가자 40명)에서 가장 낮은 단어 오류율을 보였고, 질의 분류기 정확도는 약 87%, 다층 구조는 참가자 16명 평가에서 GPT-4 Turbo 보다 13개 항목 중 4개에서 유의하게 높았다. 오인식·오답 때의 복구 절차는 이번 조사에서 확인되지 않았다. [사실][^ref-868] |

이 사례는 Nandkumar·Peternel(Frontiers in Robotics and AI, 2025-04-29)이 보고한 실제 연구다. 다중 로봇 오케스트레이션이 아니라 로봇 한 대의 음성 대화 인터페이스를 다루지만, 이 영역의 세 가지 일이 한 현장에 함께 나타난다. 모든 응답을 상품 데이터베이스 항목에 근거하게 해 환각을 줄인 점은 오해석 방지·근거 표시에, 두 언어와 성별 집단으로 음성 인식 기술을 비교한 점은 음성·다국어·현장 단말 대화에, 단어 오류율·분류 정확도·사용자 평가로 결과를 잰 점은 대화형 기능 평가에 해당한다. [사실][^ref-868]

ROP 관점에서 여섯 항목 가운데 이 영역이 관여하는 칸은 수행 자원(음성 인식 엔진과 언어 모델을 어디에 어떻게 두는가), 제약(근거 응답 조건), 예외·성과(평가 지표)다. 물류창고·제조 공장·병원·가정·실외의 대화 기능 사례와 국내 현장 자료는 이번 조사에서 확인되지 않았다(11. 열린 질문 참조).

## 6. 대표 접근법과 기술

서로 다른 두 연구 그룹(Ren 외의 KnowNo, Mullen·Manocha 의 LBAP)이 언어 모델 계획기의 불확실도를 통계적으로 보정해 확신이 없을 때만 사람에게 되묻는 설계를 각각 보고해, 불확실도 보정 기반 되묻기로 오해석이 실행으로 이어지는 것을 막는 접근이 한 곳 이상에서 확인된다. [사실][^ref-351][^ref-864]

자세한 내용은 주제 페이지 [13. 대화형 기능의 신뢰·기반 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area13-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이 영역의 규범 문서는 위협 목록(OWASP), 프로토콜 보안 원칙(MCP), 기록·개인정보 규제·안내서(EU AI Act, 개인정보보호위원회, TTA), 공개 벤치마크와 참조 구현으로 나뉜다. [사실][^ref-855][^ref-856][^ref-863] 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [13. 대화형 기능의 신뢰·기반 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-29-area13-s7.md)에 있다.

## 8. 대표 연구와 자료

이 영역의 자료는 위협·방어 연구, 되묻기·검증 연구, 평가 벤치마크, 권한·승인 연구, 모델 공급망·음성·화면 연동 연구, 국내 안내서로 나뉜다. [사실][^ref-859][^ref-858]

자세한 내용은 주제 페이지 [13. 대화형 기능의 신뢰·기반 — 대표 연구와 자료](../../topics/2026/2026-09-29-area13-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 해석 결과에 근거(장소·물품·문서 식별자)를 붙이고 불확실한 항목만 되묻는 흐름, 음성 인식 결과의 확인 절차, 언어 모델 출력의 검증·승인·기록 | 음성 인식 모델의 소음·다국어 강건성(Whisper 등), 언어 모델 공급자의 탈옥 방어·안전 학습 |
| 업종별 조건 | 대화 기록 자동 로그와 보존·보호 요구를 기록 항목·권한 제약으로 반영 | 고위험·고영향 AI 해당 여부 판단과 개인정보 법령 해석(59. 법·규제·보험·라이선스, 53. 개인정보·영상 데이터) |

확인한 자료를 종합하면 이 영역에서 ROP 가 직접 맡을 범위는 해석 결과에 근거를 붙이고 불확실한 항목만 되묻는 흐름, 도구 호출 수준의 권한 검사와 실행 전 승인 관문, 대화·도구 호출·실제 제공 모델의 기록, 모델 공급자 연결·교체 정책, 오류 유형별 평가 시나리오이며, 음성 인식 엔진의 정확도와 언어 모델 자체의 안전 정렬은 연계 대상으로 두는 것이 [분류 원문 19장의 경계](../../about/scope-boundary.md)에 맞을 것으로 보인다. [추정][^ref-856][^ref-867][^ref-865][^ref-866][^ref-858] MCP 명세가 도구 호출 전 동의를 프로토콜이 아니라 호스트의 책임으로 둔다는 점은 승인 관문이 ROP 쪽에 놓여야 한다는 판단을 뒷받침한다. [사실][^ref-856]

연계 대상은 짧게 다룬다. 음성 인식 모델의 소음·다국어 강건성과 언어 모델 공급자의 탈옥 방어·안전 학습은 원문 19장의 로봇 자체 지능 및 외부 도구 쪽이며, 이종 제조사를 잇는 ROP 는 인식 결과의 확인 절차와 모델 출력의 검증·승인·기록을 맡고 인식·모델 내부 성능은 공급자에게 맡겨야 할 것으로 보인다. [추정][^ref-866][^ref-868][^ref-857] 자사 로봇과 모델까지 만드는 제품 전략이라면 이 경계는 안쪽으로 이동할 수 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 C. 채팅 기반 구성·운영의 다섯 대화 영역이 공유하는 기반이며, 위협·방어·평가 연구는 원문 교차 규칙에 따라 L. AI·학습 기술의 해당 영역과, 권한·기록·개인정보는 N. 보안·개인정보의 영역과 함께 연결한다. [추정][^ref-858][^ref-857][^ref-863]

자세한 내용은 주제 페이지 [13. 대화형 기능의 신뢰·기반 — 다른 연구영역과의 연결](../../topics/2026/2026-09-29-area13-s10.md)에 있다.

## 11. 열린 질문

기존 질문 여섯 건은 이번 실행에서 부분 진전만 있어 열림으로 둔다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [13. 대화형 기능의 신뢰·기반 — 열린 질문](../../topics/2026/2026-09-29-area13-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-29 · 갱신 · [13. 대화형 기능의 신뢰·기반](conversational-trust-and-foundations.md) — 3~11절 신규 작성(seed → draft), 출처 19건(ref-855~ref-868 신규, ref-351·ref-840·ref-165·ref-753 재사용), 상업 시설 사례 1건, 열린 질문 4건 추가, 1차 조건부 승인 수정 7건 이행 (실행 2026-09-29-06)
- 2026-09-29 · 생성 · [13. 대화형 기능의 신뢰·기반 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area13-s6.md) — 자동 분리: 13. 대화형 기능의 신뢰·기반 의 "6. 대표 접근법과 기술" 절(3,607자)을 옮겼다 (실행 2026-09-29-06)
- 2026-09-29 · 생성 · [13. 대화형 기능의 신뢰·기반 — 대표 연구와 자료](../../topics/2026/2026-09-29-area13-s8.md) — 자동 분리: 13. 대화형 기능의 신뢰·기반 의 "8. 대표 연구와 자료" 절(1,988자)을 옮겼다 (실행 2026-09-29-06)
- 2026-09-29 · 생성 · [13. 대화형 기능의 신뢰·기반 — 열린 질문](../../topics/2026/2026-09-29-area13-s11.md) — 자동 분리: 13. 대화형 기능의 신뢰·기반 의 "11. 열린 질문" 절(1,562자)을 옮겼다 (실행 2026-09-29-06)
- 2026-09-29 · 생성 · [13. 대화형 기능의 신뢰·기반 — 핵심 개념과 용어](../../topics/2026/2026-09-29-area13-s4.md) — 자동 분리: 13. 대화형 기능의 신뢰·기반 의 "4. 핵심 개념과 용어" 절(1,495자)을 옮겼다 (실행 2026-09-29-06)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-855]: OWASP GenAI Security Project, OWASP Top 10 for LLM Applications 2025, 2025, https://genai.owasp.org/llm-top-10/, 접근일 2026-09-29
[^ref-856]: Model Context Protocol (Anthropic 주도 오픈소스 프로젝트), Specification — Model Context Protocol (2025-06-18), 2025-06-18, https://modelcontextprotocol.io/specification/2025-06-18, 접근일 2026-09-29
[^ref-857]: Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J., Jailbreaking LLM-Controlled Robots, 2024-11-09, https://arxiv.org/abs/2410.13691, 접근일 2026-09-29
[^ref-858]: Li, M., Zhao, S., Wang, Q., Wang, K., Zhou, Y., Srivastava, S., Gokmen, C., Lee, T., Li, L. E., Zhang, R., Liu, W., Liang, P., Li, F.-F., Mao, J., & Wu, J. (NeurIPS 2024 Datasets and Benchmarks), Embodied Agent Interface: Benchmarking LLMs for Embodied Decision Making, 2025-01-19, https://arxiv.org/abs/2410.07166, 접근일 2026-09-29
[^ref-859]: Huang, X., Karthick V B, S., Chen, T., Bryson, M., Chaffey, T., Chen, H., Choo, K.-K. R., & Manchester, I. R., Trust in LLM-controlled Robotics: a Survey of Security Threats, Defenses and Challenges, 2025-12-17, https://arxiv.org/abs/2601.02377, 접근일 2026-09-29
[^ref-863]: European Commission — AI Act Service Desk, Article 12: Record-keeping (Regulation (EU) 2024/1689, Artificial Intelligence Act), 2024-06-13, https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12, 접근일 2026-09-29
[^ref-864]: Mullen, J. F., Jr., & Manocha, D., Towards Robots That Know When They Need Help: Affordance-Based Uncertainty for Large Language Model Planners, 2025-06-17, https://arxiv.org/abs/2403.13198, 접근일 2026-09-29
[^ref-865]: Zhang, Y., Zhang, Z.-H., & Qin, H., Which Model Is Actually Serving You? IRIS: Budgeted Black-Box Auditing of Model Substitution and Routing Dilution in LLM Gateways, 2026-07-23, https://arxiv.org/abs/2607.20860, 접근일 2026-09-29
[^ref-866]: Li, S., Li, J., Schijve, F., Hu, J., & Barakova, E., Casting Everything to Online API Services? A Survey of Integrating Localized Speech Recognition Models in Robotic Systems, 2026-07-13, https://arxiv.org/abs/2607.11792, 접근일 2026-09-29
[^ref-867]: Michael, A. E., & Roesner, F., How Agents Ask for Permission: User Permissions for AI Agents, from Interfaces to Enforcement, 2026-07-20, https://arxiv.org/abs/2607.13718, 접근일 2026-09-29
[^ref-868]: Nandkumar, C., & Peternel, L. (Delft University of Technology), Frontiers in Robotics and AI, Enhancing supermarket robot interaction: an equitable multi-level LLM conversational interface for handling diverse customer intents, 2025-04-29, https://pmc.ncbi.nlm.nih.gov/articles/PMC12069059/, 접근일 2026-09-29
[^ref-351]: Ren, A. Z., Dixit, A., Bodrova, A., Singh, S., Tu, S., Brown, N., Xu, P., Takayama, L., Xia, F., Varley, J., Xu, Z., Sadigh, D., Zeng, A., & Majumdar, A. (CoRL 2023), Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners, 2023-09-04, https://arxiv.org/abs/2307.01928, 접근일 2026-09-29 (원문 미열람)
