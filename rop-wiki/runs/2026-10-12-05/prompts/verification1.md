(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-12-05
- date: 2026-10-12
- run_type: update (갱신)
- 대상: 44. 로봇 기반 모델·언어 모델 계획 (L. AI·학습 기술)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 언어: ko
- verification_stage: first
- verifier_budget:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2

## 입력

### runs/2026-10-12-05/target.json

```json
{
  "run_id": "2026-10-12-05",
  "date": "2026-10-12",
  "weekday": "Mon",
  "run_number": 177,
  "run_type": "update",
  "forced": true,
  "target": {
    "area_no": 44,
    "area_name": "44. 로봇 기반 모델·언어 모델 계획",
    "category": "L. AI·학습 기술",
    "category_letter": "L"
  },
  "topic": null,
  "track": null,
  "corrections": [],
  "budget": {
    "max_search_queries": 30,
    "max_sources_per_run": 15,
    "new_topic_pages": 1,
    "page_updates": 2,
    "max_retries": 2
  },
  "priority_reason": null,
  "priority_questions": [],
  "excluded_areas": [],
  "lifted_areas": [],
  "deferred": {
    "monthly_recheck": false,
    "weekly_review": false
  },
  "selection_rationale": "CLI 지정 run_type=update, area=44"
}
```

### runs/2026-10-12-05/research.json

```json
{
  "run_id": "2026-10-12-05",
  "date": "2026-10-12",
  "run_type": "update",
  "target": {
    "area_no": 44,
    "area_name": "44. 로봇 기반 모델·언어 모델 계획",
    "category": "L. AI·학습 기술"
  },
  "gaps": [
    "섹션 5. 적용 사례 — 제조 공장 사례가 BMW 보도자료(ref-1051) 하나에 기대며, 93행 'Figure AI 자체 발표로는 교차 확인하지 못했다'가 Figure AI 발표(2025-11-19, 2026-06-30)의 존재와 맞지 않음. 10개월·11개월 문구의 출처 위치(CEO 인용·본문)와 Figure 쪽 기간 축, 99% 성공률이 목표치라는 구분이 없음. 연구 실물 사례(IMR-LLM 로봇 팔 3대)도 없음",
    "섹션 6. 대표 접근법과 기술(분리 2026-09-30-area44-s6) — SMART-LLM·IMR-LLM 은 초록 수준 서술뿐이라 평가 규모(36 지시, 23장면·50작업)·실패 양상(불가능 과제, 도달 불가 배정)·풀이 방식(FIFO)이 없고, LLM+P·KnowNo 류 보장의 입력 전제(사람이 준 도메인, i.i.d., 무오류 실행)가 적혀 있지 않음. 다중 로봇 등각 예측 계획(S-ATLAS) 없음. disjunctive graph 번역어가 위키 안에서 셋으로 갈림",
    "섹션 7. 관련 표준·프레임워크·오픈소스(분리 2026-09-30-area44-s7) — 'OpenVLA의 라이선스는 확인하지 못했다'(표 바로 아래)와 GR00T N1 '오픈소스(공개 모델)' 표기에 코드·가중치 라이선스 구분과 문서 간 충돌이 없음. VLA 배포물의 입출력 계약(정규화·행동 청크·개방 루프)과 GR00T N1.7 EA 상태, ROSA 의 물리 실행 조건이 없음",
    "섹션 8. 대표 연구와 자료(분리 2026-09-30-area44-s8) — 최근 로봇 기반 모델(π0.7)과 VLA 견고성 벤치마크(LIBERO-Plus)가 없고, 국내 동향이 2025-05 기사 하나뿐(산업부 M.AX 휴머노이드 과제 표 없음)",
    "섹션 9. 책임 경계 — 도구 호출(MCP)로 로봇을 움직일 때 힌트·권한·승인·세션 종료·물리 정지의 관계가 없음",
    "섹션 11. 열린 질문(분리 2026-09-30-area44-s11) — oq-216~oq-219 모두 열림. 부분 근거(배포물별 입출력, 연구 벤치마크 규모, Figure 기간 축)가 연결돼 있지 않음",
    "정정 요청 없음(target.json corrections 비어 있음). 메모·검증에서 나온 위키 내부 정정: s7 OpenVLA 라이선스 문장, 5절 93행 Figure 자체 발표 문장"
  ],
  "research_questions": [
    "범용 로봇 모델과 언어 모델은 오케스트레이션의 무엇을 바꾸는가? [분류원문]",
    "oq-217 언어 모델 기반 다중 로봇 계획기의 공개 평가는 어떤 규모·조건(시뮬레이션/실물, 로봇 수)이며 어떤 실패 양상(능력 밖 배정)을 보고하는가? (섹션 5·6 겨냥)",
    "기호 계획기 결합·등각 예측 기반 계획의 검증·보장은 어떤 입력 전제(도메인 제공자, 분포 가정, 스킬 실행 성공)에 기대는가? (섹션 6 겨냥)",
    "oq-216 VLA 를 등록하려면 배포물마다 어떤 입출력(행동 공간·정규화·행동 청크·제어 모드)과 공개 상태(EA/GA)를 확인해야 하는가? (섹션 7·8 겨냥)",
    "OpenVLA·GR00T N1.7·openpi 의 코드와 가중치 사용 조건은 각 문서에서 무엇이라 적혀 있고 서로 맞는가? (섹션 7 겨냥)",
    "언어 모델 도구 호출(MCP·ROSA)로 로봇을 움직일 때 권한·승인·세션 종료와 물리 정지는 어떻게 나뉘는가(oq-141 관련)? (섹션 7·9 겨냥)",
    "oq-218·oq-219 BMW–Figure 와 국내 물류 실증 발표에서 목표·기간·첫 시연과 실측 성과는 어떻게 구분되는가? (섹션 5·8·11 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "SMART-LLM 의 평가 데이터셋은 AI2-THOR 가정 시뮬레이션의 고수준 지시 36개로 구성되며, 과제마다 로봇 1~4대를 쓴다.",
      "tag": "사실",
      "source_ids": [
        "ref-090"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv v2 §V-A: \"36 high-level instructions\", 과제별 로봇 1~4대, AI2-THOR. 기존 위키(docs/tracks/chat-based-configuration-and-operation/stage-2-data-and-standards.md 166행 '36개 상위 지시 … 원문 미열람', 같은 파일 370행)의 저자 보고 수치를 원문 확인으로 보강하는 것이며 새 사실 추가가 아니다. 실물 시험(대수·반복 수)은 이 수치와 별개",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "SMART-LLM 의 불가능 과제 시험(어떤 로봇도 필요한 스킬을 갖지 않은 과제)에서 GPT-4·Claude-3 기반 구성은 배정 계획을 만들지 않았고, GPT-3.5·Llama2 기반 구성은 과제에 맞지 않는 로봇이 들어간 배정 계획을 만들었다. 이 시험은 표 I 집계에 들어 있지 않고 과제 수도 보고되지 않았다.",
      "tag": "사실",
      "source_ids": [
        "ref-090"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv v2 §VI-A 'Infeasible Scenarios': \"GPT-4 and Claude-3 backbones exhibited the capacity to discern this situation and refrained from generating any task allocation plan. In contrast, … GPT-3.5 and Llama2 produced a task allocation plan involving robots ill-suited …\", \"This particular scenario is not included in Table I\". Claude-3 비교는 v2 에만 있다. 모든 모델·모든 실행으로 일반화하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "IMR-Bench 는 생산 라인 설계 전문가가 실제 산업 현장에서 수집·각색한 장면 23개(장면당 로봇 1~7대)를 바탕으로 제조 작업 50개를 구성한 벤치마크이며, KunWu 플랫폼 위에 만들어졌다.",
      "tag": "사실",
      "source_ids": [
        "ref-170"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv v1 §V-A Dataset: \"our benchmark comprises 23 scenes collected and adapted from real industrial environments by production line design experts. Each scene involves between 1 to 7 robots\", 제조 작업 50개. ICRA 2026 pp.7609–7616. 기존 위키 C 트랙(stage-1-prior-work-and-products.md 240·310행) 'IMR-Bench 규모 미확인'에 답함. 실험 데이터셋이며 상용 플릿 실적이 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "IMR-LLM 구현은 언어 모델이 구성을 도운 이접 그래프(disjunctive graph)의 일정을 휴리스틱 FIFO(선입선출) 알고리즘으로 푼다.",
      "tag": "사실",
      "source_ids": [
        "ref-170"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv v1 §IV-A: \"we use a heuristic First-In-First-Out (FIFO) [33] algorithm to solve the disjunctive graph\". 결정적 풀이를 전역 최적 보장으로 읽지 않음. 용어가 위키에 '선택 그래프'(2026-09-30-area44-s6.md 57행), '선언 그래프'(C 트랙 stage-1 112행), '이접 그래프'(같은 파일 240행)로 흩어져 있음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "IMR-LLM 의 실물 시험은 컨베이어에 공작물을 옮기는 로봇 팔 3대의 단일 장면이었고, 전문가가 약 15분 걸려 장면 설명을 손으로 작성해 입력했다. 반복 횟수는 보고되지 않았다.",
      "tag": "사실",
      "source_ids": [
        "ref-170"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv v1 §V-C: \"This scene consists of three robotic arms\", \"we used a manually constructed scene description, which took an expert approximately 15 minutes\". 반복 횟수·오류율 미보고. 장기 공장 배치 증거가 아님(기존 위키 9절 138행·s6 57행 '초록에 실제 공장 배치 없음'과 일치)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "IMR-LLM 저자는 복잡한 다중 로봇 작업에서 성공률이 떨어진 주된 이유로 언어 모델의 잘못된 분해·배정(예: 팔이 닿지 않는 로봇에 작업 배정)을 들었으나, 그 빈도는 정량화하지 않았다.",
      "tag": "사실",
      "source_ids": [
        "ref-170"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv v1 §V-B: \"we observed a decline in the SR for complex multi-robot tasks … incorrect decompositions and allocations (e.g., assigning an operation to an out-of-reach robot), which directly leads to a decrease in OC\". OC(작업 일관성) 하락 원인 예시이며 오류 건수는 없음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "LLM+P 는 행동의 전제·효과를 담은 PDDL 도메인 파일을 사람 전문가가 제공한다는 것을 입력 전제로 둔다. 언어 모델은 문제(problem) 파일만 만든다.",
      "tag": "사실",
      "source_ids": [
        "ref-092"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv v3 §III-C: \"a human expert can provide\" 도메인 PDDL. 기존 위키의 [추정](C 트랙 stage-1-prior-work-and-products.md 80행, task-model-draft.md 133행 '사람이 미리 정의 … 이 위키의 정리')을 LLM+P 에 대해서는 직접 근거로 보강. 생성된 problem 이 현장 상태와 맞는지의 검증과는 별개",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "S-ATLAS(등각 예측 기반 다중 로봇 언어 계획기)의 임무 성공률 보장은 보정(calibration) 시나리오와 시험 시나리오가 독립·동일분포(i.i.d.)라는 조건 아래에서만 성립한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1607"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv v4 Remark III.6: \"calibration and test scenarios are i.i.d.\". IEEE RA-L 10(1):160–167(2025-01). 확률은 명시한 시나리오 분포에서 정의되며 분포가 바뀐 현장까지 넓히지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "S-ATLAS 의 임무 완료율 정리(Theorem IV.2(a))는 계획 실행에 오류가 없다는 전제를 두며, 증명은 예측 집합이 단일 원소가 아닐 때 사람이 정확한 도움을 준다는 것도 전제한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1607"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv v4 Theorem IV.2(a): \"Assuming error-free execution\"; 초록 \"assuming successful plan execution\", 기여 (i) \"assuming successful execution of robot skills\". 물리적 실패·안전 인증에 대한 보장이 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f10",
      "claim": "S-ATLAS 는 AI2-THOR 시뮬레이션의 검증 시나리오 110개로 평가했고 로봇 수는 1·3·10·15대였다. 열람한 본문에서 실물 로봇 실험은 확인되지 않았다.",
      "tag": "사실",
      "source_ids": [
        "ref-1607"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv v4 §V·§V-A: \"110 (validation) scenarios\", N∈{1,3,10,15}, AI2-THOR. hardware/real robot 실험 서술 없음(본문 검색 기준). 15대는 시뮬레이터 대수",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f11",
      "claim": "OpenVLA 모델 카드에 따르면 OpenVLA 는 언어 지시와 카메라 영상 한 장을 입력받아 정규화된 7자유도 엔드이펙터 변위(x, y, z, roll, pitch, yaw, gripper)를 출력하며, 실제 로봇에서 실행하려면 로봇·데이터셋별로 계산한 통계로 역정규화해야 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1609"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Hugging Face openvla/openvla-7b 카드 Uses: \"predict (normalized) robot actions consisting of 7-DoF end-effector deltas … actions need to be *un-normalized* subject to statistics computed on a per-robot, per-dataset basis\". 공통 능력 등록 스키마가 아니라 배포물의 입출력 설명",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "OpenVLA 공식 저장소(고정 커밋 c8f03f4)의 코드 라이선스는 MIT 다.",
      "tag": "사실",
      "source_ids": [
        "ref-1608"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "LICENSE 표제 \"MIT License\"; README 606행 \"`LICENSE` - All code is made available under the MIT License\". 가중치 조건과 분리해 기록. 기존 위키 2026-09-30-area44-s7.md 표 아래 'OpenVLA의 라이선스는 확인하지 못했다'를 정정할 근거",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f13",
      "claim": "같은 OpenVLA README 는 사전학습 모델이 기반 모델의 제약을 물려받을 수 있으며, 두 모델이 Llama 2 에서 파생됐으므로 Llama Community License 가 적용될 수 있다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1608"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README 99–101행: \"our pretrained models may inherit restrictions from the underlying base models we use. Specifically, both the above models are derived from Llama-2, and as such are subject to the [Llama Community License]\". 검증에 따라 '적용된다'가 아니라 '적용될 수 있다'로 완화(앞 문장 'may inherit'). 법적 적용 판정이 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f14",
      "claim": "OpenVLA 의 Hugging Face 모델 카드는 \"모든 OpenVLA 체크포인트와 학습 코드가 MIT 라이선스로 공개된다\"고 적어, 저장소 README 의 Llama Community License 적용 가능 문구와 충돌한다. 현재 main 판(커밋 47a0ec7, 2026-02-17)도 같은 문구이며, 두 문서는 같은 개발팀 자료라 어느 쪽이 맞는지는 문서만으로 정할 수 없다.",
      "tag": "사실",
      "source_ids": [
        "ref-1609",
        "ref-1608"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "카드 20행: \"All OpenVLA checkpoints, as well as our training codebase are released under an MIT License.\", 메타데이터 license: mit. 메모가 고정한 리비전 258bd1d(2024-11-29)는 현재 main 이력에 없어 main(47a0ec7) 기준으로 대조. README·카드는 같은 프로젝트 자료라 독립 교차 확인이 아님. 충돌 해소(명시적 정정)는 확인 못 함",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f15",
      "claim": "openpi 원격 추론 예시는 정책 서버가 (action_horizon, action_dim) 형태의 행동 청크(action chunk)를 돌려준다고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1610"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "openpi 커밋 215abfb docs/remote_inference.md Querying 예시 주석: \"This returns an action chunk of shape (action_horizon, action_dim).\" 인터페이스 서술(벤더 성능 주장이 아님). 명령 수락·작업 완료 상태와 같지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "같은 openpi 예시는 다음 추론 호출 전까지 예측된 행동 청크의 나머지 행동을 개방 루프(open-loop)로 실행하도록 안내한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1610"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "docs/remote_inference.md 63행 주석: \"… from the predicted action chunk open-loop in the remaining steps.\" 예시 동작 설명이며 네트워크 장애·청크 유효기간·안전 정지 기능의 근거가 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f17",
      "claim": "openpi README(커밋 215abfb)가 제공하는 기반 체크포인트는 π0, π0-FAST, π0.5 뿐이며, π0.7 가중치는 목록에 없다.",
      "tag": "사실",
      "source_ids": [
        "ref-1610"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README 'Model Checkpoints' 표 66–68행: pi0_base, pi0_fast_base, pi05_base. π0.7 기술 보고서(ref-1613)와 공개 배포물의 대응이 없음을 뜻하며, π0.7 의 결과를 openpi 로 재현할 수 있다고 보지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f18",
      "claim": "NVIDIA Isaac GR00T 저장소의 n1.7-release README 는 GR00T N1.7 을 Early Access(EA) 릴리스로 명시하고, GA(정식) 릴리스 전까지 지원·안정성 보장이 제한되며 상용 지원을 포함한 운영 배치는 GA 대상이라고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1611"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README 49–59행: \"This is an Early Access (EA) release. … support and stability guarantees are limited until the GA release.\", GA 항목 \"Production deployment with commercial support\"; 507·511행 EA 기간 PR 미수용·best-effort 지원. 브랜치 이름 기준 열람이며 커밋 sha 로 고정하지 못함",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f19",
      "claim": "같은 GR00T README 의 License 절은 코드는 Apache 2.0, 모델 가중치는 NVIDIA Open Model License 로 구분한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1611"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README 514–517행: \"Code: Apache 2.0 — see LICENSE\", \"Model weights: NVIDIA Open Model License\". 저장소 LICENSE 파일은 Apache 2.0",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "GR00T README 소개 문단은 \"GR00T N1.7 은 Apache 2.0 으로 완전히 상용 라이선스가 가능하다\"고 적지만, 이는 같은 README 의 License 절(가중치는 별도 라이선스)·가중치 저장소 LICENSE(3.3절 비상업 한정)와 맞지 않는 벤더 소개 문구다.",
      "tag": "추정",
      "source_ids": [
        "ref-1611",
        "ref-1612"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: README 71행 \"GR00T N1.7 is fully commercially licensable under Apache 2.0.\" 같은 문서 514–517행과 GR00T-N1.7-3B LICENSE §3.3(f21)이 이와 다르게 적는다. 소개 문구만으로 가중치 상용 허용을 확정하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "Hugging Face nvidia/GR00T-N1.7-3B 저장소의 LICENSE 파일(커밋 6949d5d, 현재 main 과 같음)은 'NVIDIA License' 표제 아래 3.3절에서 저작물과 파생물을 연구·평가 목적의 비상업 용도로만 쓸 수 있게 하고, NVIDIA 와 그 계열사는 상업적으로 쓸 수 있다는 예외를 둔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1612"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "LICENSE §3.3 Use Limitation: \"The Work and any derivative works thereof only may be used or intended for use non-commercially. Notwithstanding the foregoing, NVIDIA Corporation and its affiliates may use the Work and any derivative works commercially. As used herein, 'non-commercially' means for research or evaluation purposes only.\" 이 파일만 서술하며 모든 N1.7 배포물의 사용 금지로 넓히지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "GR00T N1.7 가중치의 사용 조건은 세 문서가 서로 다르게 적는다: README 소개(Apache 2.0 으로 상용 가능), README License 절과 3B 모델 카드(NVIDIA Open Model License, 카드는 '상업·비상업 사용 준비'), 3B 저장소 LICENSE 파일(NVIDIA License 3.3절 비상업 한정). 어느 문서가 우선하는지는 문서에 적혀 있지 않다.",
      "tag": "사실",
      "source_ids": [
        "ref-1611",
        "ref-1612"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README 71·514–517행; GR00T-N1.7-3B 카드(main) \"This model is ready for commercial/non-commercial use.\", \"released under the NVIDIA Open Model License Agreement\"; 같은 저장소 LICENSE 표제 \"NVIDIA License\" §3.3. 모두 NVIDIA 자료라 독립 확인이 아니며 법적 우선순위는 판단하지 않음. 기존 위키 2026-09-30-area44-s7.md 표의 'GR00T N1 — 오픈소스(공개 모델)' 표기와도 관련",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "Physical Intelligence 의 π0.7 기술 보고서는 관절(joint)·엔드이펙터(ee) 행동을 함께 학습하고 프롬프트의 텍스트 식별자 c∈{joint, ee} 로 실행 제어 모드를 지정해 실행 시 과제에 따라 고른다고 설명한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1613"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: arXiv v2 §V-D: \"use a text identifier c∈{joint, ee} to designate the control mode in the prompt. Then at runtime, we can pick the control mode depending on the task.\" 단일 회사 보고서이며 구현을 실행해 확인하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "π0.7 보고서는 추론 지연에 대비해 학습 중 0~12 타임스텝의 지연을 모사했고, 이는 50 Hz 로봇에서 최대 240 ms 에 해당한다고 적는다. 이는 학습 조건이며 측정된 추론 지연이 아니고, 보고서의 UR5e 로봇은 20 Hz 로 동작한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1613"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: arXiv v2 §VI-B: \"During training, we simulate delays of 0 to 12 timesteps, corresponding to a maximum inference latency of 240ms on a 50Hz robot.\"; 실험 로봇 플랫폼 설명(Fig. 4 다음 문단): \"The UR5e robots run at 20 Hz, while all other robots run at 50 Hz.\" 네트워크 포함 실측 최대 지연·다중 로봇 동시 추론 수치는 없음(oq-104 관련 근거로만)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f25",
      "claim": "π0.7 저자들은 학습 데이터가 매우 커서 평가 과제가 학습 때 본(seen) 과제인지 처음 보는(unseen) 과제인지 확정하기 어렵다고 스스로 밝힌다.",
      "tag": "추정",
      "source_ids": [
        "ref-1613"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "arXiv v2 §X Discussion(seen/unseen 구분의 어려움). 회사 연구진의 한계 진술을 옮긴 것으로, 새 과제 무데이터 성공이나 이기종 플릿 일반화 보장의 근거로 쓰지 않음. 단일 출처",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f26",
      "claim": "LIBERO-Plus 는 LIBERO 시뮬레이션 조작 과제에서 물체 배치, 카메라 시점, 로봇 초기 상태, 언어 지시, 조명, 배경 질감, 센서 잡음의 7개 축으로 입력을 하나씩 교란해 VLA 모델의 견고성을 평가한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1614",
        "ref-1615"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv v3 §2.1: \"seven common single-dimension perturbations\"; CVPR 2026 게재본 Table 2 열(Camera, Robot, Language, Light, Background, Noise, Layout). 두 판은 같은 연구팀 자료라 독립 교차 확인이 아님. 단일 팔 조작 시뮬레이션이며 현장 플릿 평가가 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f27",
      "claim": "LIBERO-Plus 에서 OpenVLA-OFT 의 성공률은 교란 없는 원본 97.1% 에서 로봇 초기 상태 교란 시 크게 떨어진다. 수치는 판마다 다르다: arXiv v3 표 1 은 로봇 초기 상태 37.2%·카메라 시점 59.7%, CVPR 2026 게재본(제목 'LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models') 표 2 는 로봇 초기 상태 31.9%·카메라 시점 56.4% 다.",
      "tag": "사실",
      "source_ids": [
        "ref-1614",
        "ref-1615"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv v3 Table 1 OpenVLA-OFT 행: 97.1 | 59.7 | 37.2 | 81.5 | 85.8 | 92.4 | 76.7 | 77.1. CVPR 2026 게재본(pp.38574–38583) Table 2 OpenVLA-OFT 행: Original 97.1, Camera 56.4, Robot 31.9, Language 79.5, Light 88.7, Background 93.3, Noise 75.8, Layout 74.2, Total 69.6. 검증 수정: 메모의 '97.1/37.2'는 v3 값이라 판을 명시하고 게재본 값을 병기. 직접 재실행하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f28",
      "claim": "ROSA FAQ 는 핵심 ROSA 에이전트가 텍스트 상호작용에 한정되어 물리 세계와 상호작용할 수 없으며, 물리적 상호작용에는 사용자가 맞춤 도구와 프롬프트를 만들어야 한다고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1616"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "nasa-jpl/rosa Wiki FAQ 'What are ROSA's limitations?' 88행: \"The core ROSA agent is limited to text-based interactions and cannot interact with the physical world. To enable physical interactions, you will need to create custom tools and prompts.\" 릴리스에 고정되지 않은 위키 문서(접근일 기준)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f29",
      "claim": "같은 ROSA FAQ 는 로봇 능력을 넘는 행동을 막으려면 맞춤 도구 안에 실행 전 로봇 상태·능력 확인 제약과 매개변수 검증·행동 제한 같은 안전 검사를 직접 넣으라고 권고한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1616"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "FAQ 'Safety and Guardrails' 128행 \"Add safety checks to your custom tools to validate parameters and limit actions.\", 'How can I ensure that ROSA does not perform actions that are outside the robot's capabilities?' 152–156행 \"Implement constraints in your custom tools to check the robot's state and capabilities before executing actions.\" 기존 위키 C 트랙 stage-1-prior-work-and-products.md 118행 [추정]('README·Custom Agents 위키 범위에서 확인·권한 장치 설명이 없다')은 FAQ 범위에서는 맞지 않아 후속 정리가 필요. 권고이며 자동 제공 기능이 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f30",
      "claim": "MCP 공식 블로그(2026-03-16)는 도구 어노테이션(readOnlyHint·destructiveHint 등)이 위험을 알리는 힌트일 뿐 실행 강제 수단이 아니며, 확실한 보장이 필요하면 네트워크 통제나 샌드박스로 해야 한다고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1617"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "블로그 'What Annotations Can't Do' 75행: \"They aren't enforcement. If you need a guarantee that a tool can't exfiltrate data, that's a job for network controls or sandboxing, not a boolean hint.\" 규범 명세 개정이 아니라 프로젝트의 해설 글. 기존 위키의 MCP 명세(2025-06-18) 서술 — 2026-09-29-area13-s6.md 45행(ref-856: 신뢰하지 않는 서버의 주석 불신, 프로토콜은 강제 불가), C 트랙 stage-4-misinterpretation-safeguards.md 253행(ref-696) — 과 같은 방향이며 이를 보완함",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f31",
      "claim": "PickNik 의 MoveIt Pro MCP 서버 문서는 공유되는 배포(deployment) MCP 키는 읽기 전용이고, 로봇 동작은 호스트 사용자 세션에서 기존 Objective 를 시작·취소하는 것으로만 한정된다고 설명한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1618"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: MoveIt Pro 문서(Version 10) 74·78행: \"deployment MCP key is read-only because it is shared\", \"Robot motion over MCP is limited to starting and cancelling existing Objectives from a host-user session; the deployment MCP key never can.\" 제품을 실행해 확인하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f32",
      "claim": "같은 문서는 MCP 서버가 별도의 실행 확인 프롬프트를 추가하지 않으며, 도구 승인은 MCP 클라이언트 설정에 달려 있고 클라이언트가 자동 승인할 수도 있다고 적는다.",
      "tag": "추정",
      "source_ids": [
        "ref-1618"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 78행: \"Your MCP client controls tool approval according to its configured permissions; clients may auto-approve calls. The server adds no confirmation prompt.\" oq-141(승인 관문 위치)의 부분 근거: 이 제품은 서버가 아니라 클라이언트에 승인을 맡김",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f33",
      "claim": "같은 문서는 run_objective 로 시작한 로봇이 세션이 끝나도 계속 움직일 수 있고, cancel_objective 는 최선 노력(best effort)일 뿐 비상 정지가 아니며 MCP 취소·소프트웨어 정지는 물리적 비상 정지를 대체하지 않는다고 적는다.",
      "tag": "추정",
      "source_ids": [
        "ref-1618"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 도구 표 119행 run_objective \"The robot may move, and keeps moving if the session ends.\"; 542행 \"cancel_objective is best effort, not an emergency stop. Neither MCP cancellation nor the Runtime's software stop controls replace physical emergency-stop controls.\" 세션 종료와 물리 정지를 같은 것으로 보지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f34",
      "claim": "Figure AI 의 2025-11-19 발표는 BMW 스파턴버그의 Figure 02 를 '11개월 배치'라고 부르면서, 개발 착수 뒤 6개월 안에 공장에 납품·시험을 시작하고 10개월 안에 생산 라인 전면 배치를 시작했으며 '6개월의 일일 가동'과 1,250시간 이상 가동을 적는다. 세 기간의 기점·종점이 달라 BMW 보도자료의 10개월·11개월 차이를 해소하지 못한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1619",
        "ref-1051"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: Figure 'F.02 Contributed to the Production of 30,000 Cars at BMW' 10행 \"an 11 month Figure 02 robot deployment … Within 6 months … began testing. Within 10 months, we launched full deployment\", 27행 \"Six months of daily runtime … 1,250+ operational hours\". BMW 보도자료(ref-1051)는 11개월이 Figure CEO 인용문, 10개월(\"over ten months\")이 본문. 10/11개월 충돌은 기존 위키(5절 89·91행, oq-219)에 있고 기간 축 차이만 새로 보탬. 같은 프로젝트 당사자 자료",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f35",
      "claim": "같은 Figure 발표에서 '교대당 99% 초과 성공률'과 '교대당 개입 0회'는 목표(target·goal)로 제시되며, 달성한 실측치로 보고되지 않았다.",
      "tag": "추정",
      "source_ids": [
        "ref-1619"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 22–23행 \"Our target was > 99% success per shift.\", \"The goal was zero per shift.\" 독립 생산 로그·분모 없음. 실측 달성률로 옮기지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f36",
      "claim": "Figure AI 는 2026-06-30 발표에서 BMW 스파턴버그 공장에서 Figure 03 이 물류 작업 흐름을 수행한 것을 '첫 시연'으로 설명하고, 자사 VLA 인 Helix 02 가 손·팔·몸통·발을 함께 제어해 무거운 대차를 끌었다고 적는다.",
      "tag": "추정",
      "source_ids": [
        "ref-1620"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: Figure 'F.03 Arrives at BMW'(June 30, 2026) Highlights 14–15행: \"The first demonstration of Figure 03 performing a logistics workflow at BMW Group Plant Spartanburg.\", \"Helix 02, Figure's proprietary pixels-to-actions VLA …\". 첫 시연이며 지속 배치 성과(가동률·인계 로그)가 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f37",
      "claim": "기존 위키 5절의 'Figure AI 자체 발표로는 교차 확인하지 못했다'(Figure 03 착수 문단)는 고쳐야 한다. Figure AI 자체 발표(2026-06-30, 2025-11-19)가 있으나, BMW 와 같은 프로젝트의 당사자 자료라 독립 교차 확인으로는 세지 않는다.",
      "tag": "추정",
      "source_ids": [
        "ref-1620",
        "ref-1619",
        "ref-1051"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 대상 문장은 docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md 93행. Figure 발표 2건(ref-1619·ref-1620)이 BMW 보도자료(ref-1051)와 같은 배치·착수를 설명함. 세 출처 모두 벤더 문서라 '확인됨'이 아니라 '당사자 발표가 일치함'으로 적는 것이 맞음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f38",
      "claim": "산업통상부 2025-11-24 보도자료에 따르면 산업부와 서울대가 M.AX 얼라이언스 협력 MOU 를 맺었고, 지원 과제 표의 휴머노이드 분과 과제는 '휴머노이드 AI 파운데이션 모델 개발'(2025~2028년, 484억 원, 핵심 연구진 장병탁·박재흥 서울대 교수)이다.",
      "tag": "사실",
      "source_ids": [
        "ref-1621"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "motir.go.kr 보도자료(등록일 2025-11-24) 과제 표: \"휴머노이드 | '25~'28년, 484억원 | 장병탁, 박재흥 | 휴머노이드 AI 파운데이션 모델 개발\". 기업이 데이터·플랫폼을 주고 서울대가 모델을 개발해 기업에 다시 제공하는 구조. 기존 위키 5절 물류창고 사례의 로보티즈–BGF로지스 과제(ref-1052, 정부 출연금 약 60억 원)와 같은 사업인지는 확인되지 않음. 자동화율 80%·성공률 90% 실측 결과는 이 자료에도 없음(oq-218 미해결)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f39",
      "claim": "스킬 목록이 없거나 로봇 능력 밖인 요청을 계획기가 거절하는지(또는 닿지 않는 로봇에 배정하지 않는지)를 일반 성공률과 별도의 수용 시험 항목으로 두어야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-090",
        "ref-170"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "메모 A01·A03 ROP 시사점. 근거 f2(불가능 과제에서 일부 모델의 부적합 배정), f6(도달 불가 배정). 의견",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f40",
      "claim": "언어 모델 다중 로봇 계획의 검증 결과에는 일정 풀이 통과와 분해·배정의 정확성을 따로 적고, 계획 검증이 기대는 전제(사람이 준 도메인 판, i.i.d. 시나리오, 무오류 스킬 실행, 정확한 사람 도움)를 함께 기록해 전제가 깨질 때 보장 상태를 다시 평가해야 하며, 이 보장을 플릿의 물리적 안전 보장과 섞지 않아야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-170",
        "ref-092",
        "ref-1607"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "메모 A02·A04·A05 ROP 시사점. 근거 f4, f7, f8, f9. 의견",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f41",
      "claim": "연구 논문의 실물 시험(예: 로봇 팔 3대 단일 장면)은 사례 표에 장면 작성자·시뮬레이션 확인·복구 책임을 함께 적고 장기 운영 실적으로 표시하지 않아야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-170"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "메모 A03 ROP 시사점. 근거 f5. 의견",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f42",
      "claim": "VLA 탑재 로봇의 능력 등록에는 모델·가중치 revision(해시), 로봇 기종·카메라, 좌표계·행동 단위·제어 모드, 정규화 통계, 행동 청크의 형태·관측 시각·유효기간·중단 조건, 허용 과제와 완료 판정을 두고, 명령 완료는 로봇 외부 상태로 확인하는 것이 필요해 보인다. 이는 ROP 설계 제안이며 표준이 아니다.",
      "tag": "의견",
      "source_ids": [
        "ref-1609",
        "ref-1610",
        "ref-1613"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "메모 A06·A08·A10 ROP 시사점. 근거 f11, f15, f16, f23. oq-216 의 부분 답(공통 등록 표준·적합성 시험은 확인 못 함). 의견",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f43",
      "claim": "공개 VLA 를 도입할 때 코드 라이선스와 가중치 사용 조건을 따로 확인하고, README 소개 문구만으로 상용 허용을 확정하지 않으며, 문서끼리 충돌하는 조건은 배포자에게 서면으로 확인할 항목으로 남겨야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-1608",
        "ref-1609",
        "ref-1611",
        "ref-1612"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "메모 A07·A09 ROP 시사점. 근거 f12~f14, f18~f22. 법률 판단이 아님. 의견",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f44",
      "claim": "카메라 교체·로봇 초기 자세 변경 같은 교란을 로봇별 수용 시험에 넣고, 벤치마크 수치는 판(arXiv 판·게재본)을 밝혀 인용하며, 단일 팔 시뮬레이션 벤치마크 순위를 제조사 혼합 플릿 순위로 환산하지 않아야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-1614",
        "ref-1615"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "메모 A11 ROP 시사점. 근거 f26, f27. 의견",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f45",
      "claim": "언어 모델이 도구 호출로 로봇을 움직이는 구성에서는 어노테이션 힌트나 클라이언트 자동 승인에 기대지 말고, ROP 쪽 런타임에서 읽기/실행 권한·실행 대상·승인된 계획 revision·goal id 와 물리적 완료 판정을 검사하며, 세션 종료를 별도의 정지 절차에 연결해야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-1617",
        "ref-1618",
        "ref-1616"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "메모 A12·A13 ROP 시사점. 근거 f28~f33. 기존 위키 2026-09-29-area13-s6.md 45행의 '승인 관문은 ROP 쪽 호스트에' 추정과 같은 방향. 의견",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f46",
      "claim": "벤더·도입 기업 발표는 목표·기간·첫 시연과 실측 성과를 다른 열로 나누고, 운영 기간의 기점·종점, 성공률의 분모, 개입·실패 로그, 인계 신호가 공개될 때까지 도입 KPI 비교에 쓰지 않아야 한다. 국내 실증 목표(자동화율 80%·성공률 90%)도 같다.",
      "tag": "의견",
      "source_ids": [
        "ref-1619",
        "ref-1620",
        "ref-1051",
        "ref-1621"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "메모 A14·A15 ROP 시사점. 근거 f34~f38. 의견",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-090",
      "org": "Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C.",
      "title": "SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models",
      "published": "2023-09",
      "url": "https://arxiv.org/abs/2309.10062",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "SMART-LLM 논문(기존 출처, IROS 2024 pp.12140–12147 게재). 이번에 arXiv v2 HTML 본문에서 36개 고수준 지시 데이터셋(§V-A)과 불가능 과제 시험(§VI-A)을 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2309.10062v2",
      "source_unopened": false
    },
    {
      "id": "ref-170",
      "org": "Su, X., Xu, J., van Kaick, O., Xu, K., & Hu, R.",
      "title": "IMR-LLM: Industrial Multi-Robot Task Planning and Program Generation using Large Language Models",
      "published": "2026-03",
      "url": "https://arxiv.org/abs/2603.02669",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "IMR-LLM 논문(기존 출처, ICRA 2026 pp.7609–7616). 이번에 arXiv v1 HTML 본문에서 IMR-Bench 23장면·50작업, FIFO 휴리스틱, 로봇 팔 3대 실물 시험, 도달 불가 배정 오류를 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2603.02669v1",
      "source_unopened": false
    },
    {
      "id": "ref-092",
      "org": "Liu, B., Jiang, Y., Zhang, X., Liu, Q., Zhang, S., Biswas, J., & Stone, P.",
      "title": "LLM+P: Empowering Large Language Models with Optimal Planning Proficiency",
      "published": "2023-04",
      "url": "https://arxiv.org/abs/2304.11477",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "LLM+P 프리프린트(기존 출처). 이번에 arXiv v3 HTML §III-C 에서 사람 전문가가 PDDL 도메인을 제공한다는 입력 전제를 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2304.11477v3",
      "source_unopened": false
    },
    {
      "id": "ref-1051",
      "org": "BMW Group",
      "title": "BMW Group advances the use of Physical AI in production with Figure 03 project in Spartanburg",
      "published": "2026-06-25",
      "url": "https://www.press.bmwgroup.com/global/article/detail/T0458778EN/bmw-group-advances-the-use-of-physical-ai-in-production-with-figure-03-project-in-spartanburg?language=en",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "BMW 그룹 보도자료(기존 출처). 이번 재열람에서 '11-month deployment'는 Figure CEO 인용문, 'over ten months'는 본문에 있음을 확인했다(캐나다판 T0458794EN 도 같은 문구).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1607",
      "org": "Wang, J., He, G., & Kantaros, Y. (IEEE Robotics and Automation Letters 10(1))",
      "title": "Probabilistically Correct Language-based Multi-Robot Planning using Conformal Prediction",
      "published": "2025-01",
      "url": "https://arxiv.org/abs/2402.15368",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "등각 예측으로 사용자 지정 임무 성공률을 노리는 분산 다중 로봇 언어 계획기 S-ATLAS 논문(RA-L 10(1):160–167, DOI 10.1109/LRA.2024.3504233). arXiv v4 HTML 로 i.i.d. 조건(Remark III.6), 무오류 실행 전제(Theorem IV.2), 110개 AI2-THOR 검증 시나리오를 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2402.15368v4",
      "source_unopened": false
    },
    {
      "id": "ref-1608",
      "org": "OpenVLA 개발팀 (openvla/openvla GitHub)",
      "title": "OpenVLA — README 및 LICENSE (커밋 c8f03f4)",
      "published": null,
      "url": "https://github.com/openvla/openvla/blob/c8f03f48af692657d3060c19588038c7220e9af9/README.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "OpenVLA 공식 저장소 README·LICENSE. 코드 MIT, 사전학습 모델은 Llama 2 파생이라 Llama Community License 제약을 물려받을 수 있다는 문구(99–101행)를 확인했다. 커밋 날짜는 확인하지 못했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/openvla/openvla/c8f03f48af692657d3060c19588038c7220e9af9/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-1609",
      "org": "OpenVLA 개발팀 (Hugging Face openvla/openvla-7b)",
      "title": "openvla/openvla-7b — Model Card",
      "published": null,
      "url": "https://huggingface.co/openvla/openvla-7b",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "OpenVLA 7B 가중치 모델 카드. 입출력(언어+영상 → 정규화 7자유도 엔드이펙터 변위, 로봇·데이터셋별 역정규화)과 '모든 체크포인트 MIT' 문구를 현재 main(커밋 47a0ec7, 2026-02-17)에서 확인했다. 메모가 고정한 리비전 258bd1d 는 현재 main 이력에 없다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://huggingface.co/openvla/openvla-7b/raw/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-1610",
      "org": "Physical Intelligence (Physical-Intelligence/openpi GitHub)",
      "title": "openpi — README, docs/remote_inference.md, LICENSE (커밋 215abfb)",
      "published": null,
      "url": "https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/docs/remote_inference.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "π0 계열 공개 구현 openpi. 원격 추론의 행동 청크 형태(action_horizon, action_dim)와 개방 루프 실행 주석, 제공 체크포인트(π0·π0-FAST·π0.5), LICENSE(Apache 2.0)를 확인했다. 커밋 날짜는 확인하지 못했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/215abfb217dbac7d5f1273282331b9b1866c0479/docs/remote_inference.md",
      "source_unopened": false
    },
    {
      "id": "ref-1611",
      "org": "NVIDIA (NVIDIA/Isaac-GR00T GitHub)",
      "title": "Isaac GR00T N1.7 — README 및 LICENSE (n1.7-release 브랜치)",
      "published": null,
      "url": "https://github.com/NVIDIA/Isaac-GR00T/blob/n1.7-release/README.md",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "GR00T N1.7 공식 저장소 README. Early Access 릴리스 표기(49–59행), 소개 문단의 'Apache 2.0 으로 완전히 상용 라이선스 가능'(71행), License 절의 코드 Apache 2.0·가중치 NVIDIA Open Model License 구분(514–517행)을 확인했다. 브랜치 이름 기준이며 커밋 sha 로 고정하지 못했다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/NVIDIA/Isaac-GR00T/n1.7-release/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-1612",
      "org": "NVIDIA (Hugging Face nvidia/GR00T-N1.7-3B)",
      "title": "GR00T-N1.7-3B — LICENSE 및 모델 카드",
      "published": null,
      "url": "https://huggingface.co/nvidia/GR00T-N1.7-3B/blob/6949d5dfab2e872283e8cca8106ac3af8adcf39b/LICENSE",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "GR00T N1.7 3B 가중치 저장소. LICENSE(커밋 6949d5d, 2026-02-25; 현재 main 과 같음)의 'NVIDIA License' 3.3절 비상업 한정·NVIDIA 계열사 예외와, 모델 카드(main)의 'NVIDIA Open Model License'·'commercial/non-commercial use' 문구를 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://huggingface.co/nvidia/GR00T-N1.7-3B/raw/6949d5dfab2e872283e8cca8106ac3af8adcf39b/LICENSE",
      "source_unopened": false
    },
    {
      "id": "ref-1613",
      "org": "Physical Intelligence (Ai, B. 외, arXiv)",
      "title": "π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities",
      "published": "2026-04-16",
      "url": "https://arxiv.org/abs/2604.15483",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "Physical Intelligence 의 π0.7 기술 보고서(v1 2026-04-16, v2 2026-04-24). v2 HTML 에서 제어 모드 프롬프트(joint/ee), 학습 중 0~12 타임스텝 지연 모사(50 Hz 에서 240 ms), UR5e 20 Hz, seen/unseen 구분의 어려움을 확인했다. 회사 자체 보고서다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2604.15483v2",
      "source_unopened": false
    },
    {
      "id": "ref-1614",
      "org": "Fei, S., Wang, S., Shi, J. 외 (arXiv)",
      "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
      "published": "2025-10-15",
      "url": "https://arxiv.org/abs/2510.13626",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "VLA 모델의 7개 축 입력 교란 견고성 평가 프리프린트(v1 2025-10-15, v3 2025-12-26). v3 HTML 의 §2.1 과 표 1(OpenVLA-OFT 원본 97.1·카메라 59.7·로봇 초기 상태 37.2)을 확인했다. 학회 게재본(ref-1615)과 수치가 다르다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2510.13626v3",
      "source_unopened": false
    },
    {
      "id": "ref-1615",
      "org": "Fei, S., Wang, S., Shi, J. 외 (CVPR 2026, Computer Vision Foundation Open Access)",
      "title": "LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models",
      "published": "2026",
      "url": "https://openaccess.thecvf.com/content/CVPR2026/html/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.html",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "LIBERO-Plus 의 CVPR 2026 게재본(pp.38574–38583, arXiv 판과 제목이 다름). 표 2 의 OpenVLA-OFT 행(원본 97.1·카메라 56.4·로봇 31.9·전체 69.6)을 PDF 원문에서 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://openaccess.thecvf.com/content/CVPR2026/papers/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.pdf",
      "source_unopened": false
    },
    {
      "id": "ref-1616",
      "org": "NASA Jet Propulsion Laboratory (nasa-jpl)",
      "title": "FAQ · nasa-jpl/rosa Wiki",
      "published": null,
      "url": "https://github.com/nasa-jpl/rosa/wiki/FAQ",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "ROSA 공식 위키 FAQ(릴리스에 고정되지 않은 문서). 핵심 에이전트는 물리 세계와 상호작용할 수 없고 맞춤 도구·프롬프트가 필요하다는 한계와, 맞춤 도구에 상태·능력 확인과 안전 검사를 넣으라는 권고를 확인했다. README(ref-171)·Custom Agents 위키(ref-172)와 다른 페이지다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/wiki/nasa-jpl/rosa/FAQ.md",
      "source_unopened": false
    },
    {
      "id": "ref-1617",
      "org": "Model Context Protocol (Hungerford, O., Morrow, S., & Chang, L.)",
      "title": "Tool Annotations as Risk Vocabulary: What Hints Can and Can't Do",
      "published": "2026-03-16",
      "url": "https://blog.modelcontextprotocol.io/posts/2026-03-16-tool-annotations/",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "MCP 프로젝트 공식 블로그 해설. 도구 어노테이션은 위험 힌트이며 실행 강제 수단이 아니라는 설명('They aren't enforcement.')을 확인했다. 규범 명세 자체는 아니다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1618",
      "org": "PickNik Robotics",
      "title": "Connect an AI Assistant with the MCP Server (MoveIt Pro 문서 Version 10)",
      "published": null,
      "url": "https://docs.picknik.ai/how_to/programmatic_sdks/mcp_server/",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "MoveIt Pro 제품 문서의 MCP 서버 연결 안내. 배포 키 읽기 전용, 서버의 확인 프롬프트 없음, 세션 종료 뒤 로봇 계속 이동, cancel_objective 는 비상 정지가 아님 등 권한·실행 설명을 확인했다. 세부 제품 빌드와 발행일은 확인하지 못했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1619",
      "org": "Figure AI",
      "title": "F.02 Contributed to the Production of 30,000 Cars at BMW",
      "published": "2025-11-19",
      "url": "https://www.figure.ai/news/production-at-bmw",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "Figure 02 의 BMW 스파턴버그 배치를 회고한 Figure AI 발표. 11개월 배치, 6개월·10개월 이정표, 6개월 일일 가동·1,250시간 이상, 교대당 99% 초과 성공률·개입 0회 목표를 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1620",
      "org": "Figure AI",
      "title": "F.03 Arrives at BMW",
      "published": "2026-06-30",
      "url": "https://www.figure.ai/news/f-03-at-bmw",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "Figure 03 이 BMW 스파턴버그에서 물류 작업 흐름을 수행한 '첫 시연'과 Helix 02 전신 제어를 설명한 Figure AI 발표. BMW 보도자료(ref-1051)와 같은 프로젝트의 당사자 자료다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1621",
      "org": "산업통상부",
      "title": "서울대와 M.AX 얼라이언스가 손잡고 휴머노이드, 자율주행차, AI팩토리에 탑재될 AI 모델 공동 개발한다.",
      "published": "2025-11-24",
      "url": "https://www.motir.go.kr/kor/article/ATCL3f49a5a8c/171238/view",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "산업부–서울대 M.AX 얼라이언스 협력 MOU 보도자료. 휴머노이드 분과 'AI 파운데이션 모델 개발'(2025~2028년, 484억 원, 장병탁·박재흥) 과제 표를 확인했다. 보도자료라 medium.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md",
      "sections": [
        "5",
        "6",
        "7",
        "8",
        "9",
        "11"
      ],
      "rationale": "갱신(차등): 섹션 5 — 제조 공장: 93행 'Figure AI 자체 발표로는 교차 확인하지 못했다'를 'Figure AI 자체 발표(2026-06-30 F.03 첫 시연, 2025-11-19 F.02 회고)가 같은 내용을 설명하나 같은 프로젝트 당사자 자료라 독립 확인은 아니다'로 정정(f37, 벤더 주장 [추정]). 89·91행 10/11개월 충돌은 기존 내용 확인(5절 89·91행, oq-219) — 새로 넣지 말고 11개월은 Figure CEO 인용·10개월은 본문이라는 위치와 Figure 쪽 세 기간 축(6·10·11개월, 6개월 일일 가동·1,250시간)만 보탬(f34). 예외·성과 칸에 99% 초과 성공률·개입 0회는 목표치(f35), Figure 03 은 첫 시연(f36). 연구 실물 사례로 IMR-LLM 로봇 팔 3대 단일 장면(전문가 15분 장면 작성, 반복 미보고, f5)을 '연구 평가'로 표시해 추가할 수 있음. 물류창고: 산업부 M.AX 휴머노이드 과제(f38)는 로보티즈–BGF로지스 과제와 동일성 미확인이라 별도 문장으로, 80/90 실측 없음 유지; 의견 f41·f46 / 섹션 6(분리 2026-09-30-area44-s6) — 다중 로봇 계획 소절: SMART-LLM 36개 지시·1~4대·AI2-THOR(f1, C 트랙 stage-2 166행의 '원문 미열람' 수치를 원문 확인으로 보강), 불가능 과제의 모델별 차이(f2). IMR-LLM 23장면·50작업(f3), FIFO 휴리스틱(f4), 복잡 과제 성공률 하락과 도달 불가 배정(f6). 57행 '선택 그래프(disjunctive graph)'는 위키 안에서 '선언 그래프'(C 트랙 stage-1 112행)·'이접 그래프'(같은 파일 240행)와 갈리므로 한 용어로 통일 제안(이번 갱신은 s6 만, 트랙 페이지는 후속 정리). 기호 계획기 소절: LLM+P 의 사람 제공 도메인 전제(f7). 불확실도 소절: S-ATLAS 의 i.i.d.·무오류 실행·정확한 도움 전제와 110개 시뮬레이션 시나리오(f8~f10)를 KnowNo 다음에 추가; 의견 f39·f40 / 섹션 7(분리 2026-09-30-area44-s7) — 표 아래 'OpenVLA의 라이선스는 확인하지 못했다'를 정정: 코드 MIT(f12), README 의 Llama Community License '적용될 수 있다'(f13), HF 카드 '모든 체크포인트 MIT'(f14)를 충돌 그대로 병기하고 해소하지 않음. 입출력 계약: OpenVLA 역정규화(f11), openpi 행동 청크·개방 루프(f15·f16), openpi 체크포인트에 π0.7 없음(f17). GR00T 행: N1.7 은 EA(f18), README License 절 코드/가중치 구분(f19), README 71행 '상용 가능' 문구는 벤더 주장(f20), 3B LICENSE 3.3절 비상업·NVIDIA 예외(f21), 세 문서 충돌(f22) — 표의 'GR00T N1 오픈소스(공개 모델)' 유형 칸에 '코드 Apache 2.0, 가중치 별도 라이선스' 주석. ROSA 행: FAQ 의 물리 상호작용 조건(f28)과 맞춤 도구 안전 검사 권고(f29). MCP 어노테이션 한계(f30)는 7절 또는 9절에 두되 기존 MCP 명세 서술(2026-09-29-area13-s6.md 45행 ref-856, C 트랙 stage-4 253행 ref-696)과 보완 관계로 적고 재서술하지 않음; 의견 f42·f43 / 섹션 8(분리 2026-09-30-area44-s8) — π0.7 항목 추가: 제어 모드 프롬프트(f23), 학습 중 지연 모사 240 ms(50 Hz)·UR5e 20 Hz(f24), seen/unseen 판정 어려움(f25) — 모두 회사 자체 보고서라 [추정]. LIBERO-Plus 항목 추가: 7개 교란 축(f26), OpenVLA-OFT 수치는 판을 밝혀 arXiv v3(로봇 37.2·카메라 59.7)와 CVPR 2026 게재본(로봇 31.9·카메라 56.4) 병기(f27). 국내 동향에 산업부 M.AX 휴머노이드 AI 파운데이션 모델 과제(f38); 의견 f44 / 섹션 9 — 로봇 자체 지능·제어 경계 아래에 도구 호출 실행 경계 문단: MCP 힌트는 강제 수단이 아님(f30), MoveIt Pro 의 읽기 전용 배포 키·서버 확인 프롬프트 없음·세션 종료 뒤 계속 이동·cancel 은 비상 정지 아님(f31~f33, 벤더 주장 [추정]), ROSA 맞춤 도구 조건(f28·f29); 의견 f45 / 섹션 11(분리 2026-09-30-area44-s11) — 부분 답(열린 채 둠): oq-216(배포물별 입출력 f11·f15·f16·f23, 의견 f42; 공통 등록 표준·적합성 시험 미확인), oq-217(연구 벤치마크 규모·조건 f1~f6·f8~f10·f26·f27; 설비·안전·시간창 통합 공통 기준 미확인), oq-219(Figure 기간 축 f34; 기점·종점 없어 미해소), oq-141(MoveIt Pro 는 승인을 클라이언트에 맡김 f32, 벤더). 관련 근거만: oq-104(f24 학습 조건 지연, 실측 아님), oq-218(f38, 실측 결과 없음). 답하지 못함: oq-314, oq-161. 메모 새 질문 1번(VLA 공통 최소 항목)은 문구 대조로 oq-216 과 같아 새로 만들지 않음; 2·3번과 라이선스 출처 충돌 2건을 새로 올림 / 후속 정리(이번 갱신 범위 밖, 다른 페이지): docs/standards/index.md 287·288행 OpenVLA·GR00T N1 '오픈소스' 유형에 코드·가중치 라이선스 구분(f12~f14, f19~f22); docs/tracks/chat-based-configuration-and-operation/stage-1-prior-work-and-products.md 118행 ROSA [추정] '확인·권한 장치 설명 없음'을 FAQ(f29)로 정리, 같은 파일 112·240행과 2026-09-30-area44-s6.md 57행의 disjunctive graph 번역어 통일, 같은 파일 310행 'IMR-Bench 규모 미확인'에 f3 연결; stage-2-data-and-standards.md 166·370행 SMART-LLM '원문 미열람'에 f1 연결; task-model-draft.md 133행 LLM+P 부분에 f7 연결. 다음 실행 후보: 59. 법·규제·보험·라이선스(f12~f22), 13. 대화형 기능의 신뢰·기반(f30~f33), 54. 시험·형식 검증·벤치마크(f26·f27)"
    }
  ],
  "glossary_candidates": [],
  "open_questions_new": [
    "언어 모델 다중 로봇 계획의 검증이 기대는 가정(사람이 준 도메인 판, i.i.d. 시나리오, 무오류 스킬 실행)을 런타임에서 누가 감시하고, 가정이 깨졌을 때 어떤 계획을 중단·재검증할 것인가? | 관련 영역: 44. 로봇 기반 모델·언어 모델 계획, 54. 시험·형식 검증·벤치마크 | 근거: f9 | 종류: 일반",
    "원격 VLA 정책의 행동 청크(개방 루프 실행) 유효기간과, 도구 세션이 끝난 뒤에도 로봇이 움직일 수 있는 MCP 실행의 안전한 정지 계약을 어떻게 결합할 것인가? | 관련 영역: 44. 로봇 기반 모델·언어 모델 계획, 29. 명령·작업 실행의 신뢰성 | 근거: f16 | 종류: 일반",
    "출처 충돌: OpenVLA 공개 가중치의 사용 조건은 저장소 README(Llama 2 파생이라 Llama Community License 가 적용될 수 있음)와 Hugging Face 모델 카드(모든 체크포인트 MIT) 가운데 어느 쪽인가? | 관련 영역: 44. 로봇 기반 모델·언어 모델 계획, 59. 법·규제·보험·라이선스 | 근거: f14 | 종류: 출처 충돌",
    "출처 충돌: GR00T N1.7 가중치의 상업적 사용 가능 여부는 README 소개(Apache 2.0 으로 상용 가능), README License 절·3B 모델 카드(NVIDIA Open Model License, 상업·비상업 사용 준비), 3B 가중치 저장소 LICENSE 3.3절(NVIDIA·계열사 외 비상업 한정) 가운데 어느 문서가 정하는가? | 관련 영역: 44. 로봇 기반 모델·언어 모델 계획, 59. 법·규제·보험·라이선스 | 근거: f22 | 종류: 출처 충돌"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 19,
    "cross_checked_count": 0,
    "unverified": [
      "리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-12-05/external_research.md)를 변환했다. 2026-10-12 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.",
      "f14·f22: OpenVLA·GR00T N1.7 의 라이선스 문서 충돌은 문서끼리 대조한 것이며 배포자의 정정·법적 우선순위는 확인하지 못함. OpenVLA 카드는 메모의 고정 리비전 258bd1d 가 현재 main 이력에 없어 main(47a0ec7) 기준",
      "ref-1608·ref-1610: OpenVLA 커밋 c8f03f4, openpi 커밋 215abfb 의 커밋 날짜 미확인. ref-1611: GR00T n1.7-release 는 브랜치 이름으로만 열어 커밋 sha 고정 못 함. ref-1618: MoveIt Pro 문서 세부 빌드·발행일 미확인",
      "f17: openpi 에 π0.7 가중치가 없음을 README 목록으로 확인했을 뿐, π0.7 보고서와 공개 배포물의 대응(U10)·실제 네트워크 포함 최대 지연(U11)은 미확인",
      "f10: S-ATLAS 실물 실험이 없다는 것은 열람 본문 검색 기준이며 보충 자료는 보지 않음. SMART-LLM 실물 시험 대수·반복 수(U03), IMR-LLM 장기 운영(U04) 미확인",
      "f34: BMW–Figure 10/11개월의 기점·종점과 집계 관계, 교대별 실측 성공률·개입 분모(U13·U14), Figure 03 첫 시연 이후 가동률(U15) 미확인",
      "f38: 산업부 M.AX 휴머노이드 과제와 로보티즈–BGF로지스 물류 과제의 동일성(U17), 자동화율 80%·성공률 90% 실측 결과(U16, oq-218) 미확인",
      "메모 V01(GR00T-N1.7-ApplePnP-V1 모델 카드)와 V11(BGF로지스 매거진 회고)은 신규 출처 예산(15건) 때문에 출처째 넣지 않음. 둘 다 벤더 [추정]이며 ROP 판단에 쓰는 내용(라이선스 충돌·80/90 실측 부재)은 다른 finding 이 담음",
      "병원·상업시설·실외에서 로봇 기반 모델·언어 모델 계획을 쓴 이기종 플릿 현장 실증(U18), 벤더 혼합 장기 운영 플릿의 독립 재현 로그(U02), VLA 공통 능력 등록 표준·적합성 시험(U06) 미확인",
      "메모가 진단에 쓴 위키 고정 커밋(85960d2)과 현재 배포판의 동일성 미확인(U01)"
    ],
    "scope_violations": [
      "f12~f22: 코드·가중치 라이선스 문구는 59. 법·규제·보험·라이선스 쪽 내용이므로 문서 원문 대조까지만 하고 상용 사용 가능 여부의 법적 판단은 하지 않음",
      "f30~f33: 도구 호출 권한·승인·세션 종료는 13. 대화형 기능의 신뢰·기반, 29. 명령·작업 실행의 신뢰성과 겹치며, 이 영역에는 언어 모델 계획이 로봇 실행으로 넘어가는 경계 관점으로만 씀",
      "f26·f27: LIBERO-Plus 는 단일 팔 조작 시뮬레이션 벤치마크로 54. 시험·형식 검증·벤치마크와 겹치며, 이 영역에는 VLA 수용 시험 설계의 근거로만 씀"
    ],
    "budget_used": {
      "queries": 0,
      "sources": 15
    },
    "limits": "외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 15건/15(ref-1607~ref-1621, 예약 구간 ref-1607~ref-1636 안), 재사용 4건(ref-090·ref-170·ref-092·ref-1051). 출처 매핑(검증 결과 기준): 메모 n1→ref-090, n2→ref-170, n3→ref-092, n4→ref-1607, n5→ref-1608, n6→ref-1609(main 47a0ec7 기준), n7→ref-1610, n8(ApplePnP 카드)→예산 초과로 제외, n9→ref-1611, n10→ref-1613, n11→ref-1612(같은 저장소 모델 카드 포함), n12→ref-1617, n13→ref-1616(ref-171·172 와 다른 페이지), n14→ref-1618, n15→ref-1051(글로벌 URL, 캐나다판 대신), n16→ref-1619, n17→ref-1620, n18→ref-1621, n19(BGF 매거진)→예산 초과로 제외, n20→ref-1614, 추가: CVPR 2026 게재본→ref-1615. 모든 출처 원문 열람(fetched true). 출처 type: OpenVLA·openpi·GR00T 저장소와 Hugging Face 모델 저장소 파일은 프로젝트가 관리하는 저장소라 '오픈소스 문서'로 두어 인터페이스·라이선스 원문 옮김(f11~f19, f21·f22)은 [사실]; MoveIt Pro·Figure·BMW 는 '벤더 문서'라 해당 finding 은 모두 [추정]·vendor_claim. 교차 확인 0건(SMART-LLM/IMR-LLM/S-ATLAS 는 조건이 달라 같은 주장 아님, OpenVLA 문서쌍·GR00T 문서셋·openpi/π0.7·LIBERO-Plus 두 판·BMW/Figure 는 같은 팀·기관·프로젝트). 검증 반영: F21 은 arXiv v3 값(37.2)에 판을 명시하고 CVPR 2026 게재본 값(로봇 31.9·카메라 56.4) 병기(f27); F13 '적용된다'→'적용될 수 있다'(f13); F14 현재 main 도 같은 문구라 충돌 지속(f14); F18/README 71행 '상용 가능'은 벤더 주장으로 분리(f20)하고 README·LICENSE·카드 3자 충돌 기록(f22); F06 은 성공률 하락의 예시이며 정량화 없음; F02 에 GPT-4·Claude-3 거절과 표 I 밖 명시; F05 에 15분 수동 장면 작성·반복 미보고; U10 을 f17 로; U13 Figure 세 기간을 f34 로; 위키 5절 93행 정정 제안(f37). 중복 제거: F01 은 C 트랙 stage-2 166행 기존 수치의 원문 확인 보강으로만(f1), F07 은 기존 [추정] 보강, F23 은 기존 MCP 명세 서술과 보완 관계로 서술, V08(BMW 10/11개월 충돌)은 기존 5절·oq-219 에 있어 새 finding 으로 넣지 않고 f34 근거 메모와 rationale 에 위치만 적음. 열린 질문: 부분 답 oq-216·oq-217·oq-219·oq-141, 관련 근거 oq-104·oq-218, 해결 제안 없음(open_questions_resolved 비움). 메모 새 질문 1번은 oq-216 과 같아 만들지 않고, 2·3번과 출처 충돌 2건을 새로 올림. 메모의 '.research-work' 로컬 경로·행 번호는 쓰지 않고 원문 절·표·행(저장 원문 기준)과 위키 실제 위치를 적었다. 정정 요청 없음. 용어 후보 없음."
  }
}
```

### docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md

```markdown
---
title: "44. 로봇 기반 모델·언어 모델 계획"
type: area
category: "L. AI·학습 기술"
area_no: 44
related_areas: [1, 4, 5, 12, 13, 24, 25, 26, 29, 31, 47, 54, 61, 62, 65]
tags: [VLA, 로봇 기반 모델, 언어 모델 계획, 교차 형태 학습, 불확실도 정렬, 다중 로봇 계획]
status: published
confidence: medium
created: 2026-09-28
updated: 2026-09-30
sources: [ref-1045, ref-1046, ref-1047, ref-1048, ref-088, ref-092, ref-586, ref-090, ref-351, ref-1049, ref-170, ref-171, ref-1050, ref-1051, ref-1052]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [L. AI·학습 기술](index.md) › 44. 로봇 기반 모델·언어 모델 계획

# 44. 로봇 기반 모델·언어 모델 계획

!!! info "소속 대분류"
    [L. AI·학습 기술](index.md) — 핵심 질문:
    학습·언어 모델 같은 AI 기술을 어디에 쓰고, 그 결과를 어떤 기준으로 믿을 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-30 · 마지막 실행: 2026-09-30
<!-- auto:page-status:end -->

## 1. 한 줄 정의

시각–언어–행동 모델 같은 로봇 기반 모델의 흐름과 언어 모델 기반 작업 계획 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **언어 모델 기반 작업 계획**: 언어 모델 에이전트로 작업을 계획·분해하는 방법과 한계를 다룬다
- **로봇 기반 모델·임바디드 AI 동향**: 시각–언어–행동 모델, 범용 로봇·휴머노이드 같은 흐름이 오케스트레이션에 주는 영향을 추적한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 27번 영역 ‘AI·학습·적응과 모델 운영’에서 왔다. 그 본문은 [47. AI·학습·적응과 모델 운영](ai-learning-adaptation-and-model-operations.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

범용 로봇 모델과 언어 모델은 오케스트레이션의 무엇을 바꾸는가? [분류원문]

## 3. 왜 중요한가

로봇 기반 모델과 대규모 언어 모델(Large Language Model, LLM) 기반 계획은 ROP가 로봇의 능력을 받아들이는 방식과 대화로 받은 지시를 실행으로 옮기는 방식을 함께 바꾸고 있어, 무엇을 받아들이고 무엇을 검증할지 정해야 하는 영역이다. [추정][^ref-1048][^ref-351]

자세한 내용은 주제 페이지 [44. 로봇 기반 모델·언어 모델 계획 — 왜 중요한가](../../topics/2026/2026-09-30-area44-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 영역의 개념은 로봇 쪽의 학습된 범용 정책과 계획 쪽의 접지·검증 장치로 나뉜다. [추정][^ref-1045][^ref-586]

자세한 내용은 주제 페이지 [44. 로봇 기반 모델·언어 모델 계획 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area44-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이번 조사에서 확인한 가정 사례는 처음 보는 가정집에서의 연구 평가다. [사실][^ref-1047] 제조 공장 사례는 도입 기업의 발표이고, 물류창고 사례는 국내 실증 계획이다. [추정] 벤더 주장[^ref-1051][^ref-1052] 병원·상업 시설·실외 현장의 로봇 기반 모델·언어 모델 계획 적용 사례는 이번 조사에서 찾지 못했다.

**현장 유형:** 가정

**사례:** 처음 보는 가정집에서 부엌·침실 정리(연구 평가)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인(초록에 작업을 일으키는 요청 방식이 없다) |
| 작업 대상 | 처음 보는 가정집의 부엌·침실 공간과 그 안의 물건 [사실][^ref-1047] |
| 수행 자원 | 미확인(초록에 로봇 기종과 사람의 역할이 없다) |
| 제약 | 학습 때 보지 못한 가정집에서 장기·정교한 조작 작업을 해야 한다 [사실][^ref-1047] |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

Physical Intelligence의 π0.5는 여러 로봇의 데이터, 고수준 의미 예측, 웹 데이터 같은 이질적 과제를 함께 학습(co-training)해 “cleaning a kitchen or bedroom, in entirely new homes” 같은 장기 작업을 수행했다고 보고했다(2025-04). [사실][^ref-1047] 이것은 연구 평가(처음 보는 가정집에서의 실험)이며 상용 배치가 아니다. [사실][^ref-1047] 이 사례에서 로봇 기반 모델이 관여하는 부분은 작업 대상을 미리 정한 스킬 목록 없이 다루는 방식이다. [추정][^ref-1045][^ref-1047]

**현장 유형:** 제조 공장

**사례:** 자동차 공장에서 휴머노이드의 부품 투입과 순서 공급(BMW 그룹 스파턴버그 공장)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인(자료에 작업을 일으키는 요청 방식이 없다) |
| 작업 대상 | 용접 공정용 판금 부품(Figure 02), 대용량 용기에 섞여 들어온 부품(Figure 03, 착수 발표) [추정] 벤더 주장[^ref-1051] |
| 수행 자원 | Figure AI의 휴머노이드 Figure 02·Figure 03, 순서 대차를 조립 공정으로 옮기는 자동화 시스템 [추정] 벤더 주장[^ref-1051] |
| 제약 | 미확인 |
| 완료·인계 | 계획 내용(착수 발표): Figure 03이 부품을 순서 대차(sequencing trolley)에 정리하면 대차가 자동화 시스템으로 조립 공정에 운반된다. 수행 결과가 아니다 [추정] 벤더 주장[^ref-1051] |
| 예외·성과 | Figure 02가 BMW X3 3만 대 이상의 생산을 도왔다고 밝히나, 같은 자료 안에서 기간이 10개월과 11개월로 엇갈린다. 복구 주체는 미확인 [추정] 벤더 주장[^ref-1051] |

BMW 그룹은 2025년 스파턴버그 공장에 Figure AI의 휴머노이드 Figure 02를 배치해 용접 공정용 판금 부품 투입을 맡겼고, 이 로봇이 BMW X3 3만 대 이상의 생산을 도왔다고 밝힌다. [추정] 벤더 주장[^ref-1051] 같은 보도자료(2026-06-25) 안에는 10개월 동안 3만 대 이상 생산을 지원했다는 문장과 11개월 배치라는 문장이 함께 있어 기간을 하나로 정하지 않는다(11절 열린 질문). [추정] 벤더 주장[^ref-1051]

BMW 그룹은 또 후속 Figure 03이 스파턴버그에서 순서 공급(just in sequence) 물류 작업을 시작한다고 밝혔고(착수 발표), 이 로봇이 음성 대화 기능과 무선 충전을 갖췄다고 설명한다. [추정] 벤더 주장[^ref-1051] Figure AI 자체 발표로는 교차 확인하지 못했다.

**현장 유형:** 물류창고

**사례:** 물류센터에서 시각–언어–행동(Vision-Language-Action, VLA) 모델([비전 언어 행동 모델](../../glossary/vision-language-action-model.md))을 넣은 휴머노이드의 실증(개념 검증, Proof of Concept, PoC) 계획 — 입고·출고·피킹·반품 단계

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 입·출고·오발주 등 고난도 작업과 분류·피킹·반품 등 수작업 공정(비정형 작업) [추정] 벤더 주장[^ref-1052] |
| 수행 자원 | VLA 모델을 넣은 로보티즈의 상체형 휴머노이드 AI 워커, 협력사 BGF로지스 [추정] 벤더 주장[^ref-1052] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 목표치(실측 아님): 핵심 공정 자동화율 80% 이상, 오발주 재분류·피킹 작업 성공률 90% 이상 [추정] 벤더 주장[^ref-1052] |

헬로티 보도(2025-11-26)에 따르면 로보티즈는 정부 과제 'AI 파운데이션 모델 기반 유통 공정 특화 휴머노이드 로봇 개발'(정부 출연금 약 60억 원)로, VLA 모델을 넣은 상체형 휴머노이드 AI 워커가 BGF로지스 물류센터 실증(PoC)을 수행할 계획이다. [추정] 벤더 주장[^ref-1052] 기사가 전한 성과 수치는 목표치(실측 아님)이며, 공개된 측정 결과는 확인하지 못했다(11절 열린 질문). [추정] 벤더 주장[^ref-1052]

## 6. 대표 접근법과 기술

대표 접근법은 여러 로봇 데이터로 범용 정책을 학습하는 로봇 기반 모델과, 언어 모델 계획을 로봇 능력·기호 계획기·사람 확인에 묶어 믿을 수 있게 하는 방법으로 나뉜다. [추정][^ref-1048][^ref-092][^ref-351]

자세한 내용은 주제 페이지 [44. 로봇 기반 모델·언어 모델 계획 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area44-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이번 조사에서 확인한 관련 자원은 공개 데이터셋(Open X-Embodiment), 공개 VLA 모델(OpenVLA, GR00T N1), ROS용 언어 모델 에이전트(ROSA), 계획 표현 언어인 계획 도메인 정의 언어(Planning Domain Definition Language, PDDL)다. [사실][^ref-1048][^ref-1046][^ref-1049][^ref-171][^ref-092]

자세한 내용은 주제 페이지 [44. 로봇 기반 모델·언어 모델 계획 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area44-s7.md)에 있다.

## 8. 대표 연구와 자료

대표 자료는 로봇 기반 모델 계열과 언어 모델 계획 계열의 논문, 그리고 국내 협력 동향 기사다. [사실][^ref-1045][^ref-088][^ref-1050]

자세한 내용은 주제 페이지 [44. 로봇 기반 모델·언어 모델 계획 — 대표 연구와 자료](../../topics/2026/2026-09-30-area44-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

ROP는 언어 모델 계획을 검증하고 사람 확인을 거쳐 이종 로봇에 내리는 계층을 맡고, VLA의 저수준 조작 정책은 로봇 제조사·모델 제공자에게 연계하는 것으로 보인다. [추정][^ref-092][^ref-351][^ref-1045]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 로봇 기반 모델을 탑재한 로봇을 포함한 이종 로봇의 가능한 기능·실행 조건·완료·실패 확인을 받고, 검증된 계획을 내리는 인터페이스 [추정][^ref-088][^ref-090][^ref-171] | 연계 대상: VLA·로봇 기반 모델이 카메라 영상에서 관절·그리퍼 행동을 직접 생성하는 저수준 조작 정책(로봇 제조사·모델 제공자) [추정][^ref-1045][^ref-1046][^ref-1047][^ref-1049] |

ROP가 직접 맡을 범위는 언어 모델이 만든 작업 분해·배정 계획을 기호 계획기·제약 검사로 검증하는 계층, 불확실할 때 사람에게 확인을 요청하는 절차, 이종 로봇에 계획을 내리는 인터페이스이며, 이는 분류 원문 C. 채팅 기반 구성·운영 주석의 '사람이 확인·승인한 계획만 실행' 원칙과 같은 방향이다. [추정][^ref-092][^ref-586][^ref-351]

IMR-LLM처럼 공정 트리를 따라 실행 가능한 저수준 로봇 프로그램까지 생성하는 연구도 있으나, 그 부분은 로봇 자체 제어에 닿으므로 ROP에서는 연계 대상 문맥으로 본다. [추정][^ref-170] 이 경계는 제품 전략에 따라 이동할 수 있으며, 분류 원문은 '이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다'고 적는다([범위 경계](../../about/scope-boundary.md)).

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 로봇 능력 표현, 대화형 지시, 계획·배정, 계획 검증, 현장 유형 영역과 이어진다. [추정][^ref-1046][^ref-090]

자세한 내용은 주제 페이지 [44. 로봇 기반 모델·언어 모델 계획 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area44-s10.md)에 있다.

## 11. 열린 질문

(상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-07) 로봇 기반 모델(VLA)을 탑재해 명시적 스킬 목록 없이 학습된 범용 기능을 가진 로봇의 능력을 플랫폼의 능력 모델에 어떻게 등록·기술하고 검증할 것인가?

자세한 내용은 주제 페이지 [44. 로봇 기반 모델·언어 모델 계획 — 열린 질문](../../topics/2026/2026-09-30-area44-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [44. 로봇 기반 모델·언어 모델 계획](robot-foundation-models-and-llm-planning.md) — 영역 심화: seed → draft, 3~11절 신규 작성(자동 분리 후 요약·링크), 각주 15건, 1차 수정 지시 10건 이행. 2차: 5절 도입 문장을 가정 [사실]과 제조 공장·물류창고 [추정] 벤더 주장으로 분리, 5절에 VLA(용어집 링크)·PoC, 7절에 PDDL 풀어쓰기 (실행 2026-09-30-07)
- 2026-09-30 · 생성 · [44. 로봇 기반 모델·언어 모델 계획 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area44-s6.md) — 자동 분리: 44. 로봇 기반 모델·언어 모델 계획 의 "6. 대표 접근법과 기술" 절(1,491자)을 옮겼다(2차 재실행에서 변경 없음) (실행 2026-09-30-07)
- 2026-09-30 · 생성 · [44. 로봇 기반 모델·언어 모델 계획 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area44-s4.md) — 자동 분리: 44. 로봇 기반 모델·언어 모델 계획 의 "4. 핵심 개념과 용어" 절(1,296자)을 옮겼다(2차 재실행에서 변경 없음) (실행 2026-09-30-07)
- 2026-09-30 · 생성 · [44. 로봇 기반 모델·언어 모델 계획 — 대표 연구와 자료](../../topics/2026/2026-09-30-area44-s8.md) — 자동 분리: 44. 로봇 기반 모델·언어 모델 계획 의 "8. 대표 연구와 자료" 절을 옮겼다. 2차: RT-2 '출발점' 평가 삭제·f1·f3 범위로 재서술, LLM+P 문장을 분리해 [사실]`[^ref-092]` 부여(각주 정의·sources 추가), [의견]은 Kambhampati 외 주장에만 (실행 2026-09-30-07)
- 2026-09-30 · 생성 · [44. 로봇 기반 모델·언어 모델 계획 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area44-s10.md) — 자동 분리: 44. 로봇 기반 모델·언어 모델 계획 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(953자)을 옮겼다(2차 재실행에서 변경 없음) (실행 2026-09-30-07)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-1045]: Brohan, A., Brown, N. 외 (Google DeepMind, arXiv), RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control, 2023-07-28, https://arxiv.org/abs/2307.15818, 접근일 2026-09-30
[^ref-1046]: Kim, M. J., Pertsch, K., Karamcheti, S. 외 (arXiv), OpenVLA: An Open-Source Vision-Language-Action Model, 2024-06-13, https://arxiv.org/abs/2406.09246, 접근일 2026-09-30
[^ref-1047]: Physical Intelligence (Black, K., Finn, C., Levine, S. 외, arXiv), π0.5: a Vision-Language-Action Model with Open-World Generalization, 2025-04-22, https://arxiv.org/abs/2504.16054, 접근일 2026-09-30
[^ref-1048]: Open X-Embodiment Collaboration (arXiv), Open X-Embodiment: Robotic Learning Datasets and RT-X Models, 2023-10-13, https://arxiv.org/abs/2310.08864, 접근일 2026-09-30
[^ref-088]: Ahn, M., Brohan, A., Brown, N. 외 (arXiv), Do As I Can, Not As I Say: Grounding Language in Robotic Affordances, 2022-04-04, https://arxiv.org/abs/2204.01691, 접근일 2026-09-30
[^ref-092]: Liu, B., Jiang, Y., Zhang, X. 외 (arXiv), LLM+P: Empowering Large Language Models with Optimal Planning Proficiency, 2023-04-22, https://arxiv.org/abs/2304.11477, 접근일 2026-09-30
[^ref-586]: Kambhampati, S., Valmeekam, K., Guan, L. 외 (ICML 2024, arXiv), LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks, 2024-02-02, https://arxiv.org/abs/2402.01817, 접근일 2026-09-30
[^ref-090]: Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. (arXiv), SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models, 2023-09-18, https://arxiv.org/abs/2309.10062, 접근일 2026-09-30
[^ref-351]: Ren, A. Z., Dixit, A., Bodrova, A. 외 (CoRL 2023, arXiv), Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners, 2023-07-04, https://arxiv.org/abs/2307.01928, 접근일 2026-09-30
[^ref-1049]: NVIDIA (Bjorck, J., Castañeda, F. 외, arXiv), GR00T N1: An Open Foundation Model for Generalist Humanoid Robots, 2025-03-18, https://arxiv.org/abs/2503.14734, 접근일 2026-09-30
[^ref-170]: Su, X., Xu, J., van Kaick, O., Xu, K., & Hu, R. (arXiv), IMR-LLM: Industrial Multi-Robot Task Planning and Program Generation using Large Language Models, 2026-03-03, https://arxiv.org/abs/2603.02669, 접근일 2026-09-30
[^ref-171]: NASA Jet Propulsion Laboratory (nasa-jpl), ROSA — README, 미확인, https://github.com/nasa-jpl/rosa, 접근일 2026-09-30
[^ref-1050]: 지디넷코리아, K-휴머노이드 연합, 출범 3주 만에 협약 4건 성과, 2025-05-01, https://zdnet.co.kr/view/?no=20250501140356, 접근일 2026-09-30
[^ref-1051]: BMW Group, BMW Group advances the use of Physical AI in production with Figure 03 project in Spartanburg, 2026-06-25, https://www.press.bmwgroup.com/global/article/detail/T0458778EN/bmw-group-advances-the-use-of-physical-ai-in-production-with-figure-03-project-in-spartanburg?language=en, 접근일 2026-09-30
[^ref-1052]: 헬로티, VLA 이식한 로보티즈 'AI 워커', 물류 현장 난제 해결사로 전격 투입, 2025-11-26, https://www.hellot.net/news/article.html?no=107567, 접근일 2026-09-30
```

### docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md (요약)

```markdown
# 45. 문서·도면·장면 이해

소속 대분류: L. AI·학습 기술 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

매뉴얼·도면 해석과 플랫폼 수준의 장면 인식 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **문서·도면 해석 AI**: 매뉴얼과 도면을 해석하는 모델을 다룬다
- **플랫폼 수준 장면 인식**: 고정 카메라와 여러 로봇의 인식 결과를 모아 공간 상태를 인식한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 27번 영역 ‘AI·학습·적응과 모델 운영’에서 왔다. 그 본문은 [47. AI·학습·적응과 모델 운영](ai-learning-adaptation-and-model-operations.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

매뉴얼·도면·현장 영상을 AI가 얼마나 정확히 읽어 낼 수 있는가? [분류원문]
```

### docs/categories/ai-and-learning/prediction-and-learning-based-optimization.md (요약)

```markdown
# 46. 예측·학습 기반 최적화

소속 대분류: L. AI·학습 기술 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

학습 기반 배정·경로, 수요·고장 예측 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **학습 기반 배정·경로**: 강화학습 같은 학습 방법으로 배정과 경로를 정한다
- **수요·고장 예측**: 일의 양과 고장을 예측해 계획과 정비에 쓴다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 27번 영역 ‘AI·학습·적응과 모델 운영’에서 왔다. 그 본문은 [47. AI·학습·적응과 모델 운영](ai-learning-adaptation-and-model-operations.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

학습과 예측이 배정·경로·정비 결정을 실제로 개선하는가? [분류원문]
```

### docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md (요약)

```markdown
# 47. AI·학습·적응과 모델 운영

소속 대분류: L. AI·학습 기술 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

AI 결과를 실행에 쓰는 기준과 불확실성, 모델 운영 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **AI 결과의 실행 사용 기준**: AI가 만든 계획·해석을 어떤 기준으로 실행에 쓸지 정하고 불확실성을 평가한다
- **모델 운영**: 모델 버전·학습 데이터·배포·성능 감시를 관리한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [44. 로봇 기반 모델·언어 모델 계획](robot-foundation-models-and-llm-planning.md), [45. 문서·도면·장면 이해](document-drawing-and-scene-understanding.md), [46. 예측·학습 기반 최적화](prediction-and-learning-based-optimization.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 27번 영역 ‘AI·학습·적응과 모델 운영’(옛 대분류 G. 안전·보안·지능·거버넌스)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 문서·도면 해석, 수요·고장 예측, 학습 기반 계획, LLM 에이전트, 불확실성 평가, 모델 변경 관리 [옛 분류원문]

> 옛 질문: AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? [분류원문]
```

### docs/categories/planning-and-business/technology-market-and-vendor-trends.md (요약)

```markdown
# 1. 기술·시장·업체 동향

소속 대분류: A. 기획·사업 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

카테고리마다 연구·기사·업체 발표를 모으고, 제품·업체·로봇 종류의 지형을 정리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **기술·연구 동향 조사**: 카테고리마다 논문·기사·업체 발표를 모아 연구와 제품의 흐름을 추적한다
- **시장·업체·제품 지형**: 오케스트레이션·관제·상호운용 제품, 로봇 제조사, 통합 사업자의 지형을 정리한다
- **로봇 종류·형태 지형**: AMR·AGV·로봇팔·모바일 매니퓰레이터·사족 보행·휴머노이드·드론처럼 오케스트레이션 대상 로봇의 종류와 특성 변화를 추적한다

## 2. 핵심 질문

어떤 연구·제품·업체가 로봇 오케스트레이션의 흐름을 바꾸고 있는가? [분류원문]
```

### docs/categories/robot-ontology/heterogeneous-robot-registration.md (요약)

```markdown
# 4. 이기종 로봇 등록

소속 대분류: B. 로봇 온톨로지 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

서로 다른 제조사의 로봇을 문서 근거와 함께 등록하고, 사람이 검토·승인한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **이기종 로봇 등록**: 제조사·기종·펌웨어·SDK 버전·장착 장비·식별자를 가진 로봇을 플랫폼에 등록하고 등록부로 관리한다
- **기종 제원 기술**: 형상·치수·질량·구동 방식·센서·적재 한계·속도·에너지 특성을 기종 단위로 기술한다(URDF·MJCF·VDA 5050 팩트시트 등)
- **문서에서 능력 추출**: 매뉴얼·SDK·API 문서에서 능력·제약·인터페이스를 뽑아 원문 근거(절·줄·인용)와 함께 능력 정의 초안을 만든다
- **등록 검토·승인**: 추출한 능력을 사람이 원문 근거와 대조해 확정하거나 반려하고, 확인하지 못한 내용은 검토 대기로 남긴다
- **제조사 능력 정보 제공 경로**: 제조사가 능력·제약 정보를 정해진 형식으로 제공하고 갱신하는 절차와 책임을 정한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 5번 영역 ‘로봇 능력·작업 온톨로지’에서 왔다. 그 본문은 [5. 로봇 능력·작업 표현](robot-capability-and-task-representation.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

이 영역의 일부는 이전 분류(2026-09-24)의 옛 21번 영역 ‘온보딩·설정·현장 시운전’에서 왔다. 그 본문은 [55. 현장 조사·설치·시운전](../verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

제조사도 형식도 다른 로봇을 어떻게 빠르고 믿을 수 있게 등록할 것인가? [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]
```

### docs/categories/robot-ontology/robot-capability-and-task-representation.md (요약)

```markdown
# 5. 로봇 능력·작업 표현

소속 대분류: B. 로봇 온톨로지 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

능력·작업 요구·환경 조건을 공통 어휘로 표현하고 기존 표준과 맞춘다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **로봇 능력 표현**: 이동·계단·적재·도어 조작·충전·파지·점검 같은 능력을 매개변수·입출력·전제조건·제약·실패 모드와 함께 공통 모델로 표현한다
- **작업 유형·작업 요구 표현**: 배송·운반·인계·순찰·점검·조작 같은 작업 유형과 각 작업이 요구하는 능력·조건을 능력 모델과 같은 어휘로 표현한다
- **환경 조건과 능력 대조**: 층·문·승강기·계단·충전기 같은 공간 조건을 온톨로지에 함께 담아 로봇별로 지나갈 수 있는 곳과 쓸 수 있는 시설을 판단한다
- **표현 표준 정렬**: 능력·작업 표현을 로봇 온톨로지 표준(IEEE 1872 계열), VDA 5050 팩트시트, 자산 관리 셸 같은 기존 규격과 대응시킨다
- **온톨로지 저장·질의 기반**: 온톨로지를 저장하고 질의하는 기술(그래프 데이터베이스, RDF·OWL, SPARQL, JSON 스키마)을 고르고 성능을 확인한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [4. 이기종 로봇 등록](heterogeneous-robot-registration.md), [6. 온톨로지 기반 시스템·로봇 연동](ontology-based-system-and-robot-integration.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 5번 영역 ‘로봇 능력·작업 온톨로지’(옛 대분류 B. 공통 정보·환경 모델)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 제조사별 기능·제약·장착 장비·실행 조건을 공통 모델로 표현하고, 작업 요구와 연결 [옛 분류원문]

> 옛 질문: 같은 ‘운반 로봇’ 중 누가 이 화물을 실제로 취급할 수 있는가? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

로봇이 할 수 있는 일과 작업이 요구하는 조건을 어떻게 같은 말로 표현할 것인가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]
```

### docs/categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md (요약)

```markdown
# 12. 채팅으로 업무 지시·오케스트레이션

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

대화로 일을 지시하면 분해·배정·일정을 계획으로 제안하고, 승인 뒤 실행하며 진행 상황을 설명한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 업무 지시·오케스트레이션**: 상황과 처리할 일을 입력하면 업무를 파악·분해하고, 적합한 로봇 배정과 일정까지 실행 계획으로 제안한다
- **실행 전 계획 확인·승인**: 대화 결과는 실행 명령이 아니라 계획이며, 사람이 전체 계획을 확인·승인한 뒤에만 한 번 실행된다
- **채팅으로 진행 상황 질의·결과 설명**: 어디까지 했는지, 왜 멈췄는지를 대화로 묻고 실행 기록과 시각을 근거로 답을 받는다

## 2. 핵심 질문

대화로 받은 지시를 확인 가능한 계획으로 바꾸고, 승인 뒤 실행과 진행 설명까지 이어 갈 수 있는가? [분류원문]
```

### docs/categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md (요약)

```markdown
# 13. 대화형 기능의 신뢰·기반

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

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
```

### docs/categories/planning-and-optimization/task-and-workflow-modeling.md (요약)

```markdown
# 24. 작업·워크플로 모델링

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-10-10 · 버전: 3

## 1. 한 줄 정의

현장 업무를 단계·선후관계·완료 조건으로 정의하고, 계획과 실행이 따를 운영 정책을 정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **작업·워크플로 모델링**: 현장 업무(운반·배송·순찰·점검·조작·서비스 등)를 단계·선후관계·완료 조건으로 분해해 정의한다
- **동작 완료와 업무 완료 연결**: 로봇의 동작 완료(도착·내려놓음)와 업무 완료(인수 확인·기록 반영)를 구분해 잇는다
- **운영 정책 설정**: 우선순위·운영 시간·구역 규칙·충전 기준 같은 운영 정책을 설정하고 버전으로 관리해 계획과 실행이 따르게 한다

이전 분류(2026-09-24)에서 이 페이지는 옛 2번 영역 ‘공정·워크플로 모델링’(옛 대분류 A. 업무·공급망 설계)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 입고·검수·적치·보충·피킹·이송·생산·포장·출하·반품을 작업 단계로 분해하고, 선후관계와 완료 조건을 정의 [옛 분류원문]

> 옛 질문: ‘운반 완료’와 ‘인수 확인·재고 반영 완료’를 어떻게 연결할까? [옛 분류원문]

## 2. 핵심 질문

현장 업무를 로봇이 실행할 수 있는 단계와 완료 조건으로 어떻게 나눌 것인가? [분류원문]
```

### docs/categories/planning-and-optimization/task-allocation-mrta.md (요약)

```markdown
# 25. 작업 배정 — MRTA

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-10-10 · 버전: 3

## 1. 한 줄 정의

작업을 로봇 또는 로봇 팀에 배정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **작업 배정**: 능력·위치·적재량·배터리·기한을 고려해 로봇 또는 로봇 팀에 작업을 배정한다
- **이종 로봇 팀 구성**: 한 작업에 필요한 로봇 조합(운반·팔·순찰 등)을 정한다

이전 분류(2026-09-24)에서 이 페이지는 옛 13번 영역 ‘작업 배정 — MRTA’(옛 대분류 D. 계획·최적화)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 능력·위치·적재량·배터리·납기 등을 고려해 로봇 또는 로봇 팀에 작업을 배정 [옛 분류원문]

> 옛 질문: 가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

가장 가까운 로봇에 맡기는 것이 전체적으로도 유리한가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]
```

### docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md (요약)

```markdown
# 26. 작업 순서·스케줄링

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-10-10 · 버전: 3

## 1. 한 줄 정의

순서·시간 제약·긴급 삽입을 다루고, 계속 들어오는 작업에 맞춰 다시 계획한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **작업 순서·스케줄링**: 작업 묶음, 선후관계, 시간 제약, 작업 간 동기화, 긴급 작업 삽입을 다룬다
- **계속 들어오는 작업의 재계획**: 새 작업과 지연이 계속 생기는 조건에서 계획을 이어서 고친다

이전 분류(2026-09-24)에서 이 페이지는 옛 14번 영역 ‘작업 순서·스케줄링’(옛 대분류 D. 계획·최적화)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 주문 묶음, 작업 선후관계, 시간 제약, 공정 간 동기화, 긴급 작업 삽입 [옛 분류원문]

> 옛 질문: 피킹·운반·포장이 서로 기다리지 않게 어떤 순서로 실행할까? [옛 분류원문]

## 2. 핵심 질문

일이 계속 새로 들어올 때 무엇을 먼저, 언제 할지 어떻게 정할 것인가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]
```

### docs/categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md (요약)

```markdown
# 29. 명령·작업 실행의 신뢰성

소속 대분류: H. 실행·협업·예외 복구 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

명령 상태 관리, 중복 실행 방지, 관측 근거 완료 판정 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **명령 상태 관리**: 접수·실행·완료·취소 상태, 제어권, 시간 초과, 재시작 뒤 상태 복원을 관리한다
- **중복 실행 방지**: 응답이 끊긴 요청을 다시 보내도 같은 일을 두 번 하지 않게 한다
- **관측 근거 완료 판정**: 대기 시간이 지났다는 이유가 아니라 관측된 증거로 작업 단계의 완료를 인정한다

이전 분류(2026-09-24)에서 이 페이지는 옛 12번 영역 ‘명령·작업 실행의 신뢰성’(옛 대분류 C. 연결·실행 기반)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 접수·실행·완료·취소 상태, 제어권, 중복 요청 방지, 시간 초과, 재시작 후 상태 복원 [옛 분류원문]

> 옛 질문: 응답이 끊긴 운반 요청을 다시 보내면 같은 화물을 두 번 처리하지 않을까? [옛 분류원문]

## 2. 핵심 질문

응답이 끊긴 명령을 다시 보내도 같은 일을 두 번 하지 않게 하려면? [분류원문]
```

### docs/categories/execution-collaboration-and-recovery/human-robot-collaboration.md (요약)

```markdown
# 31. 사람–로봇 협업

소속 대분류: H. 실행·협업·예외 복구 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

사람과의 작업 분담, 수동 개입·원격 조작, 주변 사람과의 소통 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **사람–로봇 작업 분담**: 사람과 로봇이 서로 기다리지 않도록 일을 나누고 작업자의 부담(인체공학)을 고려한다
- **수동 개입·원격 조작**: 운영자가 승인·수동 전환·원격 조작으로 로봇 작업에 개입한다
- **주변 사람과의 소통**: 로봇이 빛·소리·화면으로 의도를 알리고 주변 사람을 안내한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [37. 관제 화면·실행 기록](../field-operations-and-monitoring/control-screen-and-execution-records.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 18번 영역 ‘사람–로봇 협업·운영 인터페이스’(옛 대분류 E. 협업·현장 운영)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 작업자에게 일 배정, 승인·수동 전환, 원격 조작, 설명 가능한 상태 표시, 인체공학 [옛 분류원문]

> 옛 질문: 사람이 피킹하고 로봇이 운반할 때 서로 기다리지 않게 하려면? [옛 분류원문]

## 2. 핵심 질문

사람과 로봇이 같은 공간에서 서로 기다리거나 방해하지 않게 하려면? [분류원문]
```

### docs/categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md (요약)

```markdown
# 54. 시험·형식 검증·벤치마크

소속 대분류: O. 검증·도입·수명주기 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

시험 설계·장애 주입·회귀 시험·형식 검증·벤치마크·재현 실험 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **시험 설계·시험 환경**: 시뮬레이션 시험과 실기체 시험을 설계하고 시험장을 꾸린다
- **장애 주입 시험**: 고장·통신 단절·센서 오류를 일부러 넣어 대응을 확인한다
- **형식 검증**: 교착과 제약 위반이 없음을 수학적으로 검증한다
- **회귀 시험**: 업데이트 뒤 정상 상황과 장애 상황을 다시 시험한다
- **벤치마크·성능 비교**: 공개 벤치마크와 시험 환경으로 방법과 제품을 비교한다(NIST ARIAC 등)
- **재현 가능한 실험·증거 보존**: 같은 입력으로 반복 실험하고 결과와 증거를 내보낸다

이전 분류(2026-09-24)에서 이 페이지는 옛 23번 영역 ‘시험·형식 검증·벤치마크’(옛 대분류 F. 도입·검증·유지관리)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 시뮬레이션·실기체 시험, 장애 주입, 교착·제약 위반 검증, 회귀시험, 성능 비교 [옛 분류원문]

> 옛 질문: 업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가? [옛 분류원문]

## 2. 핵심 질문

업데이트 후 정상 상황뿐 아니라 장애 상황도 여전히 처리되는가? [분류원문]
```

### docs/categories/site-type-applications/warehouse.md (요약)

```markdown
# 61. 물류창고

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

입고~반품 흐름의 로봇 작업. 기존 흐름 매트릭스와 영역 페이지의 물류 시나리오를 사례로 모은다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **물류창고 작업 흐름 적용**: 입고·적치·보충·피킹·포장·출하·반품 흐름에 로봇 작업을 대입해 시작 조건·작업 대상·수행 자원·제약·완료·예외를 정리한다

## 2. 핵심 질문

물류창고의 입고부터 반품까지 흐름에서 로봇 작업은 어디에 어떻게 들어가는가? [분류원문]
```

### docs/categories/site-type-applications/manufacturing-plant.md (요약)

```markdown
# 62. 제조 공장

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

라인 공급, 공정 간 운반, 여러 로봇이 함께 하는 공정 작업 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **제조 공장 적용**: 라인 공급·공정 간 운반·여러 로봇이 함께 하는 공정 작업과 생산 관리 시스템 연동을 다룬다

## 2. 핵심 질문

여러 로봇이 함께 하는 공장 작업을 생산 관리와 어떻게 맞출 것인가? [분류원문]
```

### docs/categories/site-type-applications/home-and-apartment.md (요약)

```markdown
# 65. 가정·공동주택

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

집안일 보조, 공동주택 배송, 사생활 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **가정·공동주택 적용**: 집안일 보조(정리·청소·세탁)와 공동주택 배송(승강기·공동현관), 거주자의 사생활을 다룬다

## 2. 핵심 질문

가정과 공동주택에서 사생활을 지키며 집안일과 배송을 어떻게 맡길 것인가? [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 15건 / 전체 1496건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-088 | Ahn, M. 외(Google) | Do As I Can, Not As I Say: Grounding Language in Robotic Affordances | 2022-04 | https://arxiv.org/abs/2204.01691 | 2026-09-25 | 아니오 |
| ref-090 | Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models | 2023-09 | https://arxiv.org/abs/2309.10062 | 2026-09-25 | 아니오 |
| ref-092 | Liu, B., Jiang, Y., Zhang, X., Liu, Q., Zhang, S., Biswas, J., & Stone, P. | LLM+P: Empowering Large Language Models with Optimal Planning Proficiency | 2023-04 | https://arxiv.org/abs/2304.11477 | 2026-09-25 | 아니오 |
| ref-170 | Su, X., Xu, J., van Kaick, O., Xu, K., & Hu, R. | IMR-LLM: Industrial Multi-Robot Task Planning and Program Generation using Large Language Models | 2026-03 | https://arxiv.org/abs/2603.02669 | 2026-09-25 | 아니오 |
| ref-171 | NASA Jet Propulsion Laboratory (nasa-jpl) | ROSA — ROS Agent (GitHub README) | 미확인 | https://github.com/nasa-jpl/rosa | 2026-09-25 | 예 |
| ref-351 | Ren, A. Z. 외 | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners | 2023-07 | https://arxiv.org/abs/2307.01928 | 2026-09-25 | 아니오 |
| ref-586 | Kambhampati, S., Valmeekam, K., Guan, L., Verma, M., Stechly, K., Bhambri, S., Saldyt, L., & Murthy, A. | LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks | 2024-02 | https://arxiv.org/abs/2402.01817 | 2026-09-25 | 아니오 |
| ref-1045 | Brohan, A., Brown, N. 외 (Google DeepMind, arXiv) | RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | 2023-07-28 | https://arxiv.org/abs/2307.15818 | 2026-09-30 | 예 |
| ref-1046 | Kim, M. J., Pertsch, K., Karamcheti, S. 외 (arXiv) | OpenVLA: An Open-Source Vision-Language-Action Model | 2024-06-13 | https://arxiv.org/abs/2406.09246 | 2026-09-30 | 예 |
| ref-1047 | Physical Intelligence (Black, K., Finn, C., Levine, S. 외, arXiv) | π0.5: a Vision-Language-Action Model with Open-World Generalization | 2025-04-22 | https://arxiv.org/abs/2504.16054 | 2026-09-30 | 예 |
| ref-1048 | Open X-Embodiment Collaboration (arXiv) | Open X-Embodiment: Robotic Learning Datasets and RT-X Models | 2023-10-13 | https://arxiv.org/abs/2310.08864 | 2026-09-30 | 예 |
| ref-1049 | NVIDIA (Bjorck, J., Castañeda, F. 외, arXiv) | GR00T N1: An Open Foundation Model for Generalist Humanoid Robots | 2025-03-18 | https://arxiv.org/abs/2503.14734 | 2026-09-30 | 예 |
| ref-1050 | 지디넷코리아 | K-휴머노이드 연합, 출범 3주 만에 협약 4건 성과 | 2025-05-01 | https://zdnet.co.kr/view/?no=20250501140356 | 2026-09-30 | 예 |
| ref-1051 | BMW Group | BMW Group advances the use of Physical AI in production with Figure 03 project in Spartanburg | 2026-06-25 | https://www.press.bmwgroup.com/global/article/detail/T0458778EN/bmw-group-advances-the-use-of-physical-ai-in-production-with-figure-03-project-in-spartanburg?language=en | 2026-09-30 | 예 |
| ref-1052 | 헬로티 | VLA 이식한 로보티즈 'AI 워커', 물류 현장 난제 해결사로 전격 투입 | 2025-11-26 | https://www.hellot.net/news/article.html?no=107567 | 2026-09-30 | 예 |
```

### docs/glossary/index.md (요약: 용어 399개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- 3d-scene-graph: 3차원 장면 그래프 (3D Scene Graph)
- 4d-scene-graph: 4차원 장면 그래프 (4D Scene Graph)
- a-b-update: A/B 업데이트 (A/B Update (Dual Partition Update with Rollback))
- aas-registry-and-discovery: 자산관리셸 레지스트리·디스커버리 (AAS Registry / Discovery)
- ablation-study: 절제 실험 (Ablation Study)
- abstract-and-concrete-scenario: 추상 시나리오·구체 시나리오 (Abstract Scenario / Concrete Scenario)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- action-status: 동작 상태 (Action Status (VDA 5050 actionStatus))
- actively-exploited-vulnerability: 적극 악용 취약점 (Actively Exploited Vulnerability (EU Cyber Resilience Act))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- agentic-ai: 에이전틱 AI (Agentic AI)
- aggregation-event: 집계 이벤트 (AggregationEvent)
- agv-technical-data-submodel: AGV 기술 데이터 서브모델 (Technical Data for AGV in Intralogistics (IDTA 02047))
- alarm-management: 경보 관리 (Alarm Management (ANSI/ISA 18.2))
- alert-tier: 경보 등급 (Alert Tier (Open-RMF Alert))
- almere-model: 알메러 모델 (Almere Model)
- alternative-name: 대체 이름 (Alternative Name (IMDF alt_name))
- amr-assisted-order-picking: AMR 협업 피킹 (AMR-assisted Order Picking)
- api-deprecation-policy: API 폐기 정책 (API Deprecation Policy)
- approval-fatigue: 승인 피로 (Approval Fatigue (Consent Fatigue))
- ariac: 산업 자동화용 민첩 로봇 경진대회 (Agile Robotics for Industrial Automation Competition (ARIAC))
- artificial-intelligence-management-system: AI 관리 시스템 (Artificial Intelligence Management System (AIMS))
- as-planned-vs-as-built-deviation: 설계–준공 편차 (As-planned vs As-built Deviation)
- asam-openscenario: 오픈시나리오 (ASAM OpenSCENARIO)
- assembly-line-feeding-problem: 조립라인 공급 문제 (Assembly Line Feeding Problem (ALFP))
- asset-administration-shell: 자산관리셸 (Asset Administration Shell (AAS))
- association-event: 연결 이벤트 (AssociationEvent)
- asyncapi-specification: AsyncAPI 명세 (AsyncAPI Specification)
- attribute-based-access-control: 속성 기반 접근 통제 (Attribute-Based Access Control (ABAC))
- audit-trail: 감사 추적 (Audit Trail)
- automatic-recording-of-events: 자동 사건 기록 (Automatic Recording of Events (Logs, EU AI Act Article 12))
- automatic-simulation-model-generation: 자동 시뮬레이션 모델 생성 (Automatic Simulation Model Generation (ASMG))
- automation-bias: 자동화 편향 (Automation Bias)
- average-displacement-error: 평균 변위 오차 (Average Displacement Error (ADE))
- b2mml: B2MML (Business To Manufacturing Markup Language (B2MML))
- bag-file: 백 파일 (Bag File (rosbag2))
- battery-swapping: 배터리 교환 (Battery Swapping)
- behavior-domain-definition-language: 행동 영역 정의 언어 (Behavior Domain Definition Language (BDDL))
- behavior-tree: 행동 트리 (Behavior Tree)
- block-reference: 블록 참조 (Block Reference (INSERT))
- bpmn: 비즈니스 프로세스 모델 및 표기법 (Business Process Model and Notation (BPMN))
- brainless-robot: 브레인리스 로봇 (Brainless Robot)
- building-element-proxy: 건물 요소 프록시 (Building Element Proxy (IfcBuildingElementProxy))
- building-information-modeling: 건물 정보 모델링 (Building Information Modeling (BIM))
- building-topology-ontology: 건물 위상 온톨로지 (Building Topology Ontology (BOT))
- buildingsmart-data-dictionary: buildingSMART 데이터 사전 (buildingSMART Data Dictionary (bSDD))
- business-continuity-management-system: 업무 연속성 관리 시스템 (Business Continuity Management System (BCMS))
- business-location: 업무 위치 (Business Location (EPCIS bizLocation))
- cap-theorem: CAP 정리 (CAP Theorem)
- capabilities-skills-services: 능력·스킬·서비스 모델 (Capabilities, Skills and Services (CSS) Model)
- capability-based-task-allocation: 능력 기반 작업 배정 (Capability-based Task Allocation)
- capability-description-submodel: 능력 기술 서브모델 (Capability Description Submodel (IDTA 02020))
- capability-matchmaking: 능력 매칭 (Capability Matchmaking)
- cbv: 핵심 업무 어휘 (Core Business Vocabulary (CBV))
- cell-based-production: 셀 생산 방식 (Cell-based Production)
- clarification-question: 명확화 질문 (Clarification Question (Follow-up Clarification))
- cloud-robotics: 클라우드 로보틱스 (Cloud Robotics)
- coalition-formation: 연합 형성 (Coalition Formation)
- collaborative-application: 협동 적용 (Collaborative Application)
- collaborative-perception: 협동 인지 (Collaborative Perception)
- common-coordinate-system: 공통 좌표계 (Common Coordinate System (CCS, ISO 21423))
- common-data-environment: 공통 데이터 환경 (Common Data Environment (CDE))
- compensating-transaction: 보상 트랜잭션 (Compensating Transaction)
- competency-question: 역량 질문 (Competency Question (CQ))
- condition-based-maintenance: 상태 기반 정비 (Condition-Based Maintenance (CBM))
- configuration-copilot: 구성 코파일럿 (Configuration Copilot)
- conflict-based-search: 충돌 기반 탐색 (Conflict-Based Search (CBS))
- conformal-prediction: 등각 예측 (Conformal Prediction)
- conformance-test: 적합성 시험 (Conformance Test)
- confused-deputy: 혼란된 대리인 (Confused Deputy)
- connection-state: 연결 상태 (Connection State (VDA 5050 connectionState))
- consensus-based-bundle-algorithm: 합의 기반 번들 알고리즘 (Consensus-Based Bundle Algorithm (CBBA))
- constrained-decoding: 제약 디코딩 (Constrained Decoding)
- contrastive-explanation: 대조적 설명 (Contrastive Explanation)
- control-barrier-function: 제어 장벽 함수 (Control Barrier Function (CBF))
- cooperative-object-transport: 협동 운반 (Cooperative Object Transport)
- cora: 로봇·자동화 핵심 온톨로지 (Core Ontology for Robotics and Automation (CORA))
- core-manufacturing-simulation-data: 핵심 제조 시뮬레이션 데이터 (Core Manufacturing Simulation Data (CMSD))
- costmap: 비용 지도 (Costmap)
- crdt: 무충돌 복제 데이터 타입 (Conflict-free Replicated Data Type (CRDT))
- cross-embodiment-learning: 교차 형태 학습 (Cross-embodiment Learning)
- cross-schedule-dependency: 스케줄 간 의존 (Cross-schedule Dependency (XD))
- curb-cut: 연석 경사로 (Curb Cut (Curb Ramp))
- cyber-resilience-act: 사이버복원력법 (Cyber Resilience Act (CRA))
- data-holder: 데이터 보유자 (Data Holder (EU Data Act))
- data-provenance: 데이터 출처 추적 (Data Provenance (W3C PROV))
- dds-security: DDS 보안 규격 (DDS Security (DDS-Security))
- deadlock: 교착 (Deadlock)
- decision-focused-learning: 결정 중심 학습 (Decision-Focused Learning)
- digital-nameplate: 디지털 명판 (Digital Nameplate (IDTA 02006))
- digital-shadow: 디지털 섀도 (Digital Shadow)
- digital-thread: 디지털 스레드 (Digital Thread)
- digital-twin-composition: 디지털 트윈 결합 (Digital Twin Composition)
- digital-twin: 디지털 트윈 (Digital Twin)
- discrete-event-simulation: 이산 사건 시뮬레이션 (Discrete Event Simulation (DES))
- dispenser-ingestor: 디스펜서·인제스터 (Dispenser / Ingestor)
- distributed-tracing: 분산 추적 (Distributed Tracing)
- document-layout-analysis: 문서 레이아웃 분석 (Document Layout Analysis)
- domain-shift: 도메인 이동 (Domain Shift)
- door-to-door-robot-delivery: 도어 투 도어 로봇 배송 (Door-to-Door Robot Delivery)
- drawing-exchange-format: 도면 교환 형식 (Drawing Exchange Format (DXF))
- dual-system-architecture: 이중 시스템 구조 (Dual-system Architecture (System 1 / System 2))
- eclass: ECLASS (ECLASS)
- edit-cost: 편집 비용 (Edit Cost)
- elevator-operating-rate: 승강기 가동률 (Elevator Operating Rate (EOR))
- empanelment-programme: 등재 프로그램 (Empanelment Programme)
- enclave: 인클레이브 (Enclave (SROS 2))
- epcis-error-declaration: 오류 선언 (Error Declaration (EPCIS errorDeclaration))
- epcis: 전자 제품 코드 정보 서비스 (Electronic Product Code Information Services (EPCIS))
- ethical-black-box: 윤리적 블랙박스 (Ethical Black Box (EBB))
- event-driven-rescheduling: 사건 기반 재스케줄링 (Event-driven Rescheduling)
- event-trace: 사건 트레이스 (Event Trace)
- excessive-agency: 과도한 에이전시 (Excessive Agency)
- expected-value-of-perfect-information: 완전 정보의 기대 가치 (Expected Value of Perfect Information (EVPI))
- explainable-mapf: 설명 가능한 다중 에이전트 경로 찾기 (Explainable Multi-Agent Path Finding (Explainable MAPF))
- explicit-implicit-confirmation: 명시적 확인·암시적 확인 (Explicit / Implicit Confirmation)
- face-obfuscation: 얼굴 가림 (Face Obfuscation)
- failure-explanation: 실패 설명 (Failure Explanation)
- falsification: 반증 기반 시험 (Falsification)
- fan-out: 팬아웃 (Fan-out (human-robot team))
- fault-detection-and-diagnosis-fdd: 고장 탐지·진단 (Fault Detection and Diagnosis (FDD))
- fault-injection: 장애 주입 (Fault Injection)
- filter-mask: 필터 마스크 (Filter Mask (Nav2 costmap filter))
- finops: 핀옵스 (FinOps)
- fleet-adapter: 플릿 어댑터 (Fleet Adapter)
- fleet-control-level: 플릿 제어 수준 (Fleet Control Level (Open-RMF: Full Control / Traffic Light / Read Only))
- fleet-management-system: 플릿 관리 시스템 (Fleet Management System (FMS))
- fleet-sizing: 차량 소요대수 산정 (Fleet Sizing)
- floor-plan-recognition: 평면도 인식 (Floor Plan Recognition)
- fog-computing: 포그 컴퓨팅 (Fog Computing)
- frozen-horizon: 동결 구간 (Frozen Horizon (Frozen Zone))
- generalized-voronoi-graph: 일반화 보로노이 그래프 (Generalized Voronoi Graph (GVG))
- giai: 글로벌 개별 자산 식별자 (Global Individual Asset Identifier (GIAI))
- gln-extension-component: GLN 확장 성분 (GLN Extension Component)
- goal-condition: 목표 조건 (Goal Condition)
- goods-to-person: 상품-대-사람 (Goods-to-Person (GTP))
- grade-certainty-of-evidence: 근거 확실성 등급 (GRADE (Grading of Recommendations, Assessment, Development and Evaluation))
- grai: 글로벌 반환형 자산 식별자 (Global Returnable Asset Identifier (GRAI))
- graph-edit-distance: 그래프 편집 거리 (Graph Edit Distance (GED))
- guidance-graph: 안내 그래프 (Guidance Graph)
- hallucination: 환각 (Hallucination)
- hardware-in-the-loop: 하드웨어 인 더 루프 (Hardware-in-the-Loop (HiL))
- hddl: 계층 도메인 정의 언어 (Hierarchical Domain Definition Language (HDDL))
- hierarchical-task-network: 계층적 작업 네트워크 (Hierarchical Task Network (HTN))
- high-impact-ai: 고영향 인공지능 (High-impact AI (Korea AI Basic Act))
- hmi-philosophy: HMI 철학 (HMI Philosophy (ISA-TR101.01))
- human-in-the-loop: 사람 참여 루프 (Human-in-the-Loop (HITL))
- human-motion-trajectory-prediction: 사람 움직임 궤적 예측 (Human Motion Trajectory Prediction)
- hungarian-method: 헝가리안 방법 (Hungarian Method)
- i-pass-handoff-program: I-PASS 인계 프로그램 (I-PASS Handoff Program)
- idempotency-key: 멱등성 키 (Idempotency Key)
- identity-report: 신원 보고 (Identity Report (MassRobotics identityReport))
- iec-common-data-dictionary: IEC 공통 데이터 사전 (IEC Common Data Dictionary (IEC CDD))
- ifc: 산업 기초 클래스 (Industry Foundation Classes (IFC))
- imitation-learning: 모방 학습 (Imitation Learning)
- indirect-prompt-injection: 간접 프롬프트 주입 (Indirect Prompt Injection)
- indoor-mapping-data-format: 실내 지도 데이터 형식 (Indoor Mapping Data Format (IMDF))
- indoor-space-subspacing: 공간 세분화 (Subspacing (Indoor Space Subdivision))
- indoorgml: IndoorGML (IndoorGML)
- industrial-data: 산업데이터 (Industrial Data)
- information-delivery-specification: 정보 전달 명세 (Information Delivery Specification (IDS))
- information-for-use: 사용 정보 (Information for Use (Instructions for Use))
- infrastructure-mounted-sensing: 인프라 장착 센서 (Infrastructure-mounted Sensing)
- integrity-risk: 무결성 위험 (Integrity Risk)
- intent-recognition: 의도 인식 (Intent Recognition (Intent Detection))
- irdi: 국제 등록 데이터 식별자 (International Registration Data Identifier (IRDI))
- irreducible-infeasible-subset: 기약 불능 제약 집합 (Irreducible Infeasible Subset (IIS))
- isa-95: 기업–제어 시스템 통합 표준 (ISA-95 Enterprise-Control System Integration)
- it-ot-convergence: IT/OT 융합 (IT/OT Convergence)
- jailbreak: 탈옥 (Jailbreak)
- job-shop-scheduling-problem: 작업장 스케줄링 문제 (Job Shop Scheduling Problem (JSSP))
- joint-goal-accuracy: 결합 목표 정확도 (Joint Goal Accuracy (JGA))
- json-schema: JSON 스키마 (JSON Schema)
- keystroke-level-model: 키 입력 수준 모델 (Keystroke-Level Model (KLM))
- kiosk-accessibility: 무인정보단말기 접근성 (Kiosk Accessibility (Unmanned Information Terminal Accessibility))
- lane-closure: 차선 폐쇄 (Lane Closure)
- language-guided-floor-plan-generation: 언어 유도 평면도 생성 (Language-guided Floor Plan Generation)
- latent-failure: 잠재 실패 (Latent Failure)
- layout-interchange-format: 레이아웃 교환 형식 (Layout Interchange Format (LIF))
- lease-expiry: 허가 만료 시각 (Lease Expiry (VDA 5050 leaseExpiry))
- level-alignment-fiducial: 층 정렬 기준점 (Fiducial (Level Alignment Fiducial))
- life-cycle-costing: 수명주기 비용 분석 (Life Cycle Costing (LCC, IEC 60300-3-3))
- lifelong-mapf: 지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF))
- lift-adapter: 승강기 어댑터 (Lift Adapter)
- linear-temporal-logic-on-finite-traces: 유한 트레이스 선형 시간 논리 (Linear Temporal Logic on Finite Traces (LTLf))
- linear-temporal-logic: 선형 시간 논리 (Linear Temporal Logic (LTL))
- littles-law: 리틀의 법칙 (Little's Law)
- llm-agent: LLM 에이전트 (LLM Agent)
- llm-modulo-framework: LLM-모듈로 프레임워크 (LLM-Modulo Framework)
- localization-score: 위치추정 품질 점수 (Localization Score (VDA 5050 localizationScore))
- location-check-digit: 위치 체크 디지트 (Location Check Digit)
- lockout-tagout: 잠금·표지 (Lockout/Tagout (LOTO))
- log-playback: 로그 재생 (Log Playback)
- makespan: 메이크스팬 (Makespan)
- managed-node: 관리형 노드 (Managed Node (ROS 2 Lifecycle Node))
- management-of-change: 변경 관리 (Management of Change (MOC))
- map-alignment: 지도 정합 (Map Alignment)
- map-distribution: 지도 배포 (Map Distribution (VDA 5050 downloadMap / enableMap / deleteMap))
- map-version: 지도 버전 (Map Version (VDA 5050 mapId / mapVersion))
- mapf: 다중 에이전트 경로 찾기 (Multi-Agent Path Finding (MAPF))
- maps-of-dynamics: 움직임 지도 (Maps of Dynamics (MoD))
- market-based-task-allocation: 시장 기반 작업 배정 (Market-based Task Allocation)
- matter: 매터 (Matter (Connectivity Standards Alliance smart home standard))
- mcap: MCAP (MCAP)
- milp: 혼합 정수 계획 (Mixed Integer Linear Programming (MILP))
- minimum-cost-flow: 최소 비용 흐름 (Minimum-Cost Flow)
- mission-specification-pattern: 미션 명세 패턴 (Mission Specification Pattern)
- mobile-manipulator: 모바일 매니퓰레이터 (Mobile Manipulator)
- mobile-video-information-processing-device: 이동형 영상정보처리기기 (Mobile Video Information Processing Device)
- model-checking: 모델 검사 (Model Checking)
- model-context-protocol: 모델 컨텍스트 프로토콜 (Model Context Protocol (MCP))
- model-contractual-terms: 모델 계약 조항 (Model Contractual Terms (MCTs))
- model-registry: 모델 레지스트리 (Model Registry)
- model-substitution-and-routing-dilution: 모델 대체·라우팅 희석 (Model Substitution / Routing Dilution)
- models-and-simulations-credibility-assessment: 모델·시뮬레이션 신뢰도 평가 (Models and Simulations Credibility Assessment (NASA-STD-7009))
- mqtt-last-will: MQTT 유언 메시지 (MQTT Last Will (Will Message))
- mqtt-quality-of-service-level: MQTT 서비스 품질 수준 (MQTT Quality of Service (QoS) Level)
- mqtt: 메시지 큐잉 원격 측정 전송 (Message Queuing Telemetry Transport (MQTT))
- mrta: 다중 로봇 작업 배정 (Multi-Robot Task Allocation (MRTA))
- multi-agent-pickup-and-delivery: 다중 에이전트 픽업·배송 (Multi-Agent Pickup and Delivery (MAPD))
- multi-fleet-orchestration: 다중 플릿 오케스트레이션 (Multi-Fleet Orchestration)
- multi-trip-vehicle-routing-problem: 다중 운행 차량 경로 문제 (Multi-Trip Vehicle Routing Problem (MTVRP))
- nearest-vehicle-first-rule: 최근접 차량 우선 규칙 (Nearest Vehicle First (NVF) Rule)
- neuro-symbolic-ai: 신경-기호 AI (Neuro-symbolic AI)
- number-of-clicks: 클릭 수 지표 (Number of Clicks (NoC))
- oauth2-client-credentials-grant: 클라이언트 자격 증명 흐름 (OAuth 2.0 Client Credentials Grant (Machine-to-Machine))
- observability: 관측성 (Observability)
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- online-simulation: 온라인 시뮬레이션 (Online Simulation)
- ontology-evolution: 온톨로지 진화 (Ontology Evolution)
- ontology-pitfall: 온톨로지 피트폴 (Ontology Pitfall)
- ontology-population: 온톨로지 채우기 (Ontology Population)
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
- openapi-specification: OpenAPI 명세 (OpenAPI Specification (OAS))
- opentelemetry-genai-semantic-conventions: 생성형 AI 의미 규약 (OpenTelemetry GenAI Semantic Conventions)
- opentelemetry: 오픈텔레메트리 (OpenTelemetry (OTel))
- operating-mode: 운용 모드 (Operating Mode (VDA 5050 operatingMode))
- operating-zone: 운용 구역 (Operating Zone (ISO 3691-4))
- operational-state: 운용 상태 (Operational State (MassRobotics statusReport operationalState))
- optimality-gap: 최적성 간격 (Optimality Gap)
- order-batching: 주문 배치 (Order Batching)
- original-instructions: 원본 설명서 (Original Instructions)
- outdoor-mobile-robot-operational-safety-certification: 실외이동로봇 운행안전인증 (Outdoor Mobile Robot Operational Safety Certification)
- over-the-air-update: 무선 업데이트 (Over-the-Air Update (OTA))
- overall-equipment-effectiveness: 종합설비효율 (Overall Equipment Effectiveness (OEE))
- panoptic-quality: 파놉틱 품질 (Panoptic Quality (PQ))
- panoptic-symbol-spotting: 파놉틱 심볼 스포팅 (Panoptic Symbol Spotting)
- pass-k: pass^k 지표 (pass^k)
- pay-per-pick: 피킹량 기반 과금 (Pay-per-pick)
- payback-period: 투자 회수 기간 (Payback Period)
- pddl: 계획 도메인 정의 언어 (Planning Domain Definition Language (PDDL))
- perfect-order-fulfillment: 완전 주문 이행률 (Perfect Order Fulfillment)
- performable-action: 수행 가능 동작 (Performable Action (Open-RMF perform_action))
- persistence-filter: 지속성 필터 (Persistence Filter)
- personal-delivery-device: 개인 배송 장치 (Personal Delivery Device (PDD))
- phased-rollout: 단계적 배포 (Phased Rollout (Staged Rollout))
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- post-encroachment-time: 침범 후 시간 (Post-Encroachment Time (PET))
- post-occupancy-evaluation: 사용 후 평가 (Post-Occupancy Evaluation (POE))
- power-and-force-limiting: 동력·힘 제한 (Power and Force Limiting (PFL))
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- precision-time-protocol: 정밀 시간 프로토콜 (Precision Time Protocol (PTP))
- predictive-maintenance: 예지 정비 (Predictive Maintenance)
- presumption-of-conformity: 적합성 추정 (Presumption of Conformity)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- product-liability: 제조물책임 (Product Liability)
- prompt-injection: 프롬프트 주입 (Prompt Injection)
- protective-separation-distance: 보호 분리 거리 (Protective Separation Distance)
- pseudonymisation: 가명처리 (Pseudonymisation)
- public-area-mobile-robot: 공공 영역 이동로봇 (Public-area Mobile Robot (PMR))
- put-wall: 풋월 (Put Wall)
- raster-to-vector-conversion: 래스터–벡터 변환 (Raster-to-Vector Conversion)
- raw-video-regulatory-sandbox-exemption: 영상정보 원본 활용 규제샌드박스 실증특례 (Regulatory Sandbox Special Demonstration Exemption for Raw Video Use)
- read-point: 판독 지점 (Read Point (EPCIS readPoint))
- reality-gap: 현실 격차 (Reality Gap (Sim-to-Real Gap))
- regression-testing: 회귀 시험 (Regression Testing)
- release-zone: 해제 구역 (Release Zone)
- remote-attestation: 원격 증명 (Remote Attestation)
- remote-controlled-small-vehicle: 원격 조작형 소형차 (Remote-controlled Small Vehicle (遠隔操作型小型車))
- required-and-provided-capability: 요구 능력·제공 능력 (Required Capability / Provided (Offered) Capability)
- resource-constrained-project-scheduling-problem: 자원 제약 프로젝트 스케줄링 문제 (Resource-Constrained Project Scheduling Problem (RCPSP))
- risk-assessment: 위험성평가 (Risk Assessment (ISO 12100))
- roadmap: 경로망 (Roadmap)
- robot-as-a-service: 서비스형 로봇 (Robot-as-a-Service (RaaS))
- robot-density: 로봇 밀도 (Robot Density)
- robot-foundation-model: 로봇 기반 모델 (Robot Foundation Model)
- robot-friendly-building-certification: 로봇 친화형 건축물 인증 (Robot-Friendly Building Certification)
- robot-standard-process-model: 로봇활용 표준공정모델 (Robot Standard Process Model (Korea))
- robot-task-fitness-matrix: 로봇–작업 적합도 행렬 (Robot–Task Fitness Matrix)
- robotic-middleware-for-healthcare: 의료 로봇 미들웨어 RoMi-H (Robotic Middleware for Healthcare (RoMi-H))
- robotic-mobile-fulfillment-system: 로봇 이동형 풀필먼트 시스템 (Robotic Mobile Fulfillment System (RMFS))
- role-ambiguity: 역할 모호성 (Role Ambiguity)
- role-based-access-control: 역할 기반 접근 통제 (Role-Based Access Control (RBAC))
- root-cause-analysis-rca: 근본 원인 분석 (Root Cause Analysis (RCA))
- runtime-tracing: 런타임 추적 (Runtime Tracing (ros2_tracing))
- runtime-verification: 런타임 검증 (Runtime Verification)
- safe-interval-path-planning: 안전 구간 경로 계획 (Safe Interval Path Planning (SIPP))
- safety-guardrail: 안전 가드레일 (Safety Guardrail (LLM-enabled robots))
- safety-state-report: 안전 상태 보고 (Safety State (VDA 5050 safetyState))
- saga: 사가 (Saga)
- satisfiability-modulo-theories: 이론 모듈로 만족 가능성 (Satisfiability Modulo Theories (SMT))
- scan-vs-bim: 스캔 대 BIM 비교 (Scan-vs-BIM)
- scenario-reconstruction: 시나리오 재구성 (Scenario Reconstruction)
- schedule-stability: 일정 안정성 (Schedule Stability)
- scor: 공급망 운영 참조 모델 (Supply Chain Operations Reference (SCOR))
- security-level-iec-62443: 보안 수준 (Security Level (SL, IEC 62443))
- self-driving-laboratory: 자율 실험실 (Self-driving Laboratory (Autonomous Laboratory))
- semantic-id: 의미 식별자 (Semantic ID (semanticId))
- semantic-map: 의미 지도 (Semantic Map)
- semantic-versioning: 의미적 버전 관리 (Semantic Versioning (SemVer))
- semi-open-queueing-network: 반개방형 대기행렬 네트워크 (Semi-Open Queueing Network (SOQN))
- semi-static-object: 반정적 객체 (Semi-static Object)
- service-level-agreement: 서비스 수준 협약 (Service Level Agreement (SLA))
- service-triad: 서비스 삼자 관계 (Service Triad (service robot, customer, frontline employee))
- shacl: 형상 제약 언어 (Shapes Constraint Language (SHACL))
- shift-handover: 교대 인수인계 (Shift Handover)
- shifting-bottleneck-detection-active-period-method: 이동 병목 탐지 (Shifting Bottleneck Detection (Active Period Method))
- shuttle-based-storage-and-retrieval-system: 셔틀 기반 저장·회수 시스템 (Shuttle-Based Storage and Retrieval System (SBS/RS))
- signal-temporal-logic: 신호 시간 논리 (Signal Temporal Logic (STL))
- sila-2: SiLA 2 (Standardization in Lab Automation 2 (SiLA 2))
- sim-vs-real-correlation-coefficient: 시뮬레이션–현실 상관 계수 (Sim-vs-Real Correlation Coefficient (SRCC))
- similarity-transformation: 유사 변환 (Similarity Transformation)
- simulation-description-format: 시뮬레이션 기술 형식 (Simulation Description Format (SDFormat))
- situation-awareness-based-agent-transparency: 상황 인식 기반 에이전트 투명성 (Situation Awareness-based Agent Transparency (SAT))
- situation-awareness: 상황 인식 (Situation Awareness (SA))
- situation-state-tracking: 상황 상태 추적 (Situation State Tracking)
- skill-interface: 스킬 인터페이스 (Skill Interface)
- skill: 스킬 (Skill)
- skos: 단순 지식 조직 체계 (Simple Knowledge Organization System (SKOS))
- slot-filling: 슬롯 채우기 (Slot Filling)
- slotcar: 슬롯카 모델 (Slotcar (Open-RMF simulated robot plugin))
- smart-hospital-leading-model: 스마트병원 선도모델 (Smart Hospital Leading Model)
- smart-logistics-center-certification: 스마트물류센터 인증 (Smart Logistics Center Certification)
- social-force-model: 사회적 힘 모델 (Social Force Model)
- social-robot-navigation: 사회적 내비게이션 (Social Robot Navigation (Human-aware Navigation))
- soft-landings: 소프트 랜딩 (Soft Landings (BSRIA BG 54))
- software-bill-of-materials: 소프트웨어 자재명세서 (Software Bill of Materials (SBOM))
- software-in-the-loop: 소프트웨어 인 더 루프 (Software-in-the-Loop (SiL))
- software-nameplate: 소프트웨어 명판 (Software Nameplate (IDTA 02007))
- source-grounding: 출처 근거 연결 (Source Grounding)
- space-boundary: 공간 경계 (Space Boundary (IfcRelSpaceBoundary))
- space-graph: 공간 그래프 (Space Graph)
- speed-and-separation-monitoring: 속도·분리 감시 (Speed and Separation Monitoring (SSM))
- sscc: 물류 단위 일련 코드 (Serial Shipping Container Code (SSCC))
- stakeholder-requirements-specification: 이해관계자 요구사항 명세 (Stakeholder Requirements Specification (StRS))
- state-of-charge: 충전 상태 (State of Charge (SOC))
- state-of-health: 배터리 건강 상태 (State of Health (SOH))
- state-script: 상태 스크립트 (State Script (Mender))
- stpa: 시스템 이론적 프로세스 분석 (System-Theoretic Process Analysis (STPA))
- strict-schema: 엄격 스키마 (Strict Schema (deprecated elements removed))
- stride-threat-classification: STRIDE 위협 분류 (STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege))
- structured-output: 구조화 출력 (Structured Output)
- substantial-modification: 실질적 변경 (Substantial Modification)
- success-weighted-by-path-length: 경로 길이 가중 성공률 (Success weighted by Path Length (SPL))
- supervisory-control: 감독 제어 (Supervisory Control)
- surrogate-model: 대리 모델 (Surrogate Model)
- synchronization-loss: 동기화 손실 (Synchronization Loss)
- table-structure-recognition: 표 구조 인식 (Table Structure Recognition)
- tamper-evident-log: 변조 탐지 로그 (Tamper-evident Log)
- task-decomposition: 작업 분해 (Task Decomposition)
- task-dependency-graph: 작업 의존 그래프 (Task Dependency Graph (Dependency DAG))
- technology-readiness-level: 기술 성숙도 (Technology Readiness Level (TRL))
- teleoperation: 원격 조작 (Teleoperation)
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- total-cost-of-ownership: 총소유비용 (Total Cost of Ownership (TCO))
- trace-context: 추적 문맥 (Trace Context (W3C traceparent / tracestate))
- transparency-level-ieee-7001: 자율 시스템 투명성 수준 (Transparency Level (IEEE 7001-2021))
- traversability: 통과 가능성 (Traversability)
- uncertainty-alignment: 불확실도 정렬 (Uncertainty Alignment)
- underspecification: 과소명세 (Underspecification)
- urdf: 통합 로봇 기술 형식 (Unified Robot Description Format (URDF))
- use-case-template: 사용 사례 템플릿 (Use Case Template (IEC 62559-2))
- user-defined-property-set: 사용자 정의 속성 세트 (User-defined Property Set)
- user-simulator: 사용자 시뮬레이터 (User Simulator)
- utaut: 통합 기술 수용 이론 (Unified Theory of Acceptance and Use of Technology (UTAUT))
- vda-5050-cancel-order: 주문 취소 즉시 동작 (cancelOrder (VDA 5050 instant action))
- vda-5050-factsheet: VDA 5050 팩트시트 (VDA 5050 factsheet)
- vda-5050-hibernation: 절전 모드 (Hibernation (VDA 5050 startHibernation / HIBERNATING))
- vda-5050: VDA 5050 (VDA 5050)
- verification-and-validation-of-simulation-models: 시뮬레이션 모델 검증·타당성 확인 (Verification and Validation (V&V) of Simulation Models)
- version-iri: 버전 IRI (Version IRI (owl:versionIRI))
- virtual-commissioning: 가상 시운전 (Virtual Commissioning)
- vision-language-action-model: 비전 언어 행동 모델 (Vision-Language-Action Model (VLA))
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking))
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release)
- webhook: 웹훅 (Webhook)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- wireless-safety-rated-emergency-stop: 무선 안전 비상정지 (Wireless Safety-rated Emergency Stop)
- workflow-diagram: 워크플로 다이어그램 (Workflow Diagram (Open-RMF 상호운용 관심 그룹 제안))
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [44] 에 걸린 7건 / 전체 396건)

```markdown
- oq-216 [열림] 로봇 기반 모델(VLA)을 탑재해 명시적 스킬 목록 없이 학습된 범용 기능을 가진 로봇의 능력을 플랫폼의 능력 모델에 어떻게 등록·기술하고 검증할 것인가? (영역 44, 5)
- oq-217 [열림] 언어 모델 기반 다중 로봇 계획기를 현장 제약(설비·안전·시간창)이 있는 조건에서 비교할 공통 벤치마크나 평가 기준이 있는가? (영역 44, 54)
- oq-218 [열림] 국내 로봇 AI 파운데이션 모델 과제의 물류센터 실증 목표(자동화율 80%, 성공률 90%)에 대한 공개된 측정 결과가 있는가? (영역 44, 61)
- oq-219 [열림] 출처 충돌: BMW 그룹 보도자료(2026-06-25) 안에서 Figure 02의 스파턴버그 배치 기간이 10개월과 11개월로 엇갈리는데, 실제 배치 기간은 얼마인가? (영역 44, 62)
- oq-305 [열림] 대화로 만든 다중 로봇 작업 계획을 사람이 승인하기 전에 시뮬레이션으로 실행 가능성을 미리 확인하는 절차를 플릿 오케스트레이션에 적용한 공개 사례가 있는가? (영역 12, 36, 44)
- oq-314 [열림] RoboGuard 같은 언어 모델 로봇용 안전 가드레일을 다중 로봇 플릿의 배정·경로·구역 계획에 적용해 위험 계획 차단율을 측정한 연구나 제품이 있는가? (영역 44, 48, 13)
- oq-315 [열림] 언어 모델 기반 고장 진단(REFLECT, SYSDIAGBENCH)을 제조사가 다른 이동로봇 플릿의 실행 기록·오류 코드에 적용해 원인 분석 정확도를 측정한 사례가 있는가? (영역 47, 38, 44)
```

### inbox/corrections.md

````markdown
# 정정 요청함 (inbox/corrections.md)

이 파일은 위키 내용에 대한 정정 요청을 모으는 곳이다. 형식, 처리 흐름, 거부되는 경우는 docs/corrections.md(정정 요청 안내)에 있다.

- 한 요청은 `## corr-NNN` 제목으로 시작하는 블록 하나다. id 는 corr-001 부터 순서대로 늘리며, 아래 "요청 목록"에 새 블록을 덧붙인다.
- 필드는 서식의 여섯 줄(페이지, 문제 문장, 근거, 요청일, 요청자, 상태)을 그대로 쓰고 값만 채운다. 각 필드는 한 줄로 쓴다. 페이지·문제 문장·근거·요청일은 빌드 사양서 7.4 의 필드이고, 요청자·상태는 구축자가 더한 것이다. [가정]
- 상태는 요청자가 `open` 으로 쓴다. `applied`(반영됨)·`rejected`(반영하지 않음)는 퍼블리셔가 바꾸고, 그때 "처리 실행"과 "처리 메모" 줄을 덧붙인다.
- 리서치 에이전트는 다음 실행에서 이 파일 전체를 읽는다. 대상 페이지에 걸린 `open` 요청은 반드시 조사 질문에 들어가고, 내용 검증 에이전트가 1차 검증 항목 11(정정 요청 반영 여부)로 확인하며, 처리 결과는 docs/changelog.md(변경 이력)에 남는다.
- 분류 원문의 명칭·번호·정의·질문은 정정 대상이 아니다. 새 주제나 우선 영역은 config/priority.yaml 에 적는다.

## 서식

아래 블록을 복사해 "요청 목록" 끝에 붙이고, 제목의 `corr-NNN` 을 실제 id 로 바꾼 뒤 값을 채운다. 코드 펜스 안의 서식은 요청으로 읽히지 않는다(정정 요청을 읽는 스크립트는 코드 펜스 안의 `## corr-` 줄을 제외해야 한다). [가정]

```markdown
## corr-NNN

- 페이지: docs/<경로>/<파일>.md
- 문제 문장: "페이지에 있는 문장을 태그까지 그대로 옮긴다"
- 근거: 출처 URL 또는 설명
- 요청일: YYYY-MM-DD
- 요청자: 이름 또는 역할
- 상태: open
```

## 요청 목록

(아직 요청이 없다.)
````

### config/priority.yaml

```yaml
# config/priority.yaml — 사용자가 지정하는 우선 영역·주제·질문 (빌드 사양서 7.1, 7.4, 8.2)
#
# 비어 있으면 순환 규칙(config/rotation.yaml)만 따른다. 항목이 없는 키는 빈 목록([])으로 둔다.
# 네 키(areas, topics, questions, track_questions)는 빈 목록이라도 모두 있어야 하고, 항목의 필드 이름은 아래 예시와 같아야 한다.
# 항목의 뜻과 반영 시점은 config/README.md 와 docs/about/how-to-contribute.md 에 있다.
#
# 읽는 주체:
#   - pipeline/select_target.*  : areas·topics·questions 로 그날의 대상을 정한다(순환보다 우선, 7.1). questions 는 area_no 영역을 대상으로 올리고, 2주기에는 그 영역의 점수에도 더한다
#   - 리서치·검증 에이전트       : 이 파일 전문이 프롬프트의 "## 입력"에 들어간다. 대상 영역의 questions 는 조사 질문에 포함된다
#   - pipeline/select_target.*  : 트랙 실행의 대상 선정에서 track_questions 를 트랙 백로그(data/tracks/<slug>/backlog.json)에 제기 근거 "사용자"로 먼저 등록하고 그 실행의 질문으로 고른다
#   - 퍼블리셔                   : 대상 선정 뒤에 더해진 track_questions 를 같은 방식으로 등록한다(보완)
#
# area_no 는 1~67 의 세부영역 번호다(2026-09-28 개정 분류, _source/ROP_연구분야_분류.md). 사람이 읽기 쉽도록 주석에 영역 이름을 함께 적는다(예: 17. 작업 대상·자산 식별과 인계 추적).
# 지정한 항목이 처리되면 목록에서 지워도 된다. 지우지 않으면 rotation.yaml 의 priority.skip_if_targeted_within_days 가 지난 뒤 다시 우선된다.
# 우선 지정은 조사 대상을 정할 뿐 검증 규칙과 하루 예산(daily_budget)을 바꾸지 않는다.

# 세부영역을 먼저 다루게 한다. weight 는 대상 선정 점수에 더하는 가중치, reason 은 로그(target.json·일일 로그)에 남는 지정 사유다.
areas: []
# 작성 예시:
# areas:
#   - area_no: 17           # 17. 작업 대상·자산 식별과 인계 추적
#     weight: 10            # 대상 선정 점수에 더하는 가중치
#     reason: "병원·상업 시설의 인계 확인 사례가 부족하다"

# 특정 주제로 주제 조사(run_type topic)를 실행하게 한다. area_no 는 주 연구영역이다.
topics: []
# 작성 예시:
# topics:
#   - title: "작업 대상 인계 확인에 EPCIS 이벤트를 쓰는 방법"
#     area_no: 17           # 주 연구영역: 17. 작업 대상·자산 식별과 인계 추적
#     weight: 8

# 답을 찾게 할 질문이다. area_no 영역을 areas 와 같이 순환보다 먼저 대상으로 올리고(가중치는 rotation.yaml 의 priority.question_weight), 그 영역이 대상이 되면 리서치 에이전트의 조사 질문에 포함된다.
questions: []
# 작성 예시:
# questions:
#   - question: "로봇 도착과 실제 작업 대상 인계를 어떤 이벤트로 구분해 기록하는가?"
#     area_no: 17           # 17. 작업 대상·자산 식별과 인계 추적

# 트랙 백로그에 넣을 질문이다(8.2). 다음 트랙 실행의 대상 선정이 제기 근거 "사용자"로 백로그에 등록해 우선순위를 올린다(8.2).
# 처리 순서: 리서치 에이전트는 트랙 실행마다 현재 단계의 열린 질문 가운데 사용자 지정 → 앞 단계로 되돌아온 질문 → 오래된 순으로 1~3개를 고르므로(6.1),
# 현재 단계에 넣은 사용자 질문이 가장 앞에 온다. 사용자 질문이 여럿이면 priority(high → normal → low), 같으면 파일에 적힌 순이다 [가정].
# stage 가 현재 단계보다 앞이면 되돌아온 질문과 같이 다음 트랙 실행에서 우선 처리하고(8.2), 뒤이면 그 단계가 현재 단계가 될 때 다룬다 [가정].
track_questions: []
# 작성 예시:
# track_questions:
#   - track: manual-capability-ontology   # config/tracks/<slug>.yaml 의 slug
#     stage: 1              # 질문을 넣을 단계 번호(1 ~ 그 트랙의 단계 수: 매뉴얼 기반 로봇 기능 온톨로지 7, 채팅 기반 구성·운영 10, 건축 도면 자동 인식 5). 예: 단계 1. 기존 능력 표현 모델과 표준 조사
#     question: "산업 상호운용 규격의 팩트시트는 적재 제약을 어떤 필드로 기술하는가?"
#     priority: high        # high / normal / low. 사용자 지정 질문이 여럿일 때 고르는 순서에만 쓴다 [가정]
```

### runs/2026-10-12-04/research.md

```markdown
# 리서치 브리프 2026-10-12-04

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-12-04 |
| 날짜 | 2026-10-12 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 47. AI·학습·적응과 모델 운영 |
| 대분류 | L. AI·학습 기술 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 — 67행 규제 문단이 한국 인공지능기본법을 '2026-01-22 시행'으로만 두고 '개정 법률의 시행일 … 미확인'으로 남김. EU AI Act 를 '부속서 I(기계류 등) 제품의 안전 구성요소 → 고위험'으로만 적어 2026/1744 개정(기계류의 Section B 이동, 제2조 2항 적용 조문 한정)을 반영하지 못함
- 섹션 4. 핵심 개념과 용어(분리 2026-09-25-area27-s4) — 등각 예측 항목(41행)에 보장의 전제(i.i.d. 보정, 정확한 사람 도움)가 없고, 모델 레지스트리 항목(44행)이 별칭 반영 시점을 말하지 않음. 정책·데이터 형식 호환성(전처리·보정판) 개념 없음
- 섹션 5. 적용 사례 — 가상 시나리오 두 개와 한진 기사뿐이고, 실제 플릿 단계 배포·운영 중 학습·국내 학습–운영 연계 사례가 없음
- 섹션 6. 대표 접근법과 기술(분리 2026-09-25-area27-s6) — '모델 운영 관리' 소절(69행)이 ML Test Score 항목 수와 MLflow 별칭 교체 두 문장뿐이라 승인·카나리·롤백 연습, 배포 중단·롤백 실패 상태가 없음. KnowNo 문장(57행)이 보장 조건 없이 [사실]
- 섹션 7. 관련 표준·프레임워크·오픈소스(분리 2026-09-25-area27-s7) — 모든 행이 원문 미열람, 로봇 정책 배포 호환성(LeRobot)·국내 공개 학습 데이터 판 관리 행 없음, NIST AI RMF 는 보도자료(ref-617)만 근거. 관련 법 문단(48행)이 3절과 같은 낡은 서술
- 섹션 8. 대표 연구와 자료(분리 2026-09-25-area27-s8) — 분포 이동 아래 재보정 연구와 플릿 규모 운영 중 학습 연구가 없음
- 섹션 9. 책임 경계 — 배포 후 감시·변경관리·복구 실패 처리의 책임 분담이 없음
- 섹션 11. 열린 질문 — oq-030 이 '이번 실행에서는 조사하지 않았다'로 남아 있으나 2026-10-10 영역 25 갱신에서 원문 수치가 이미 정리됨. 세 질문이 oq id 없이 '(신규 …)'로 표시됨. oq-105·oq-106·oq-107 근거 없음
- 정정 요청 없음(target.json corrections 비어 있음). 메모·검증에서 나온 위키 내부 정정: 한국 법 개정 시행일, EU AI Act 기계류 Section B 이동, KnowNo 보장 조건, ref-168 저자 표기(후속)

## 조사 질문

1. AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? [분류원문]
2. 모델 레지스트리의 별칭 교체·정책 정규화·데이터 형식 변경은 로봇에서 실제로 실행되는 모델 판과 어떻게 어긋날 수 있으며, 단계 배포·중단·롤백 실패는 어떤 상태로 기록되는가? (섹션 4·6·7 겨냥, oq-213)
3. oq-107 KnowNo 등각 예측 보장의 전제는 무엇이며, 분포가 바뀔 때 재보정은 어떤 조건(정답 관측·피드백)을 요구하는가? (섹션 4·6·8 겨냥, oq-222)
4. 플릿 규모 운영 중 학습과 국내 학습–운영 연계 발표는 어떤 조건·증거 수준의 사례인가, 국내 공개 로봇 조작 데이터의 판·분할 메타데이터는 믿을 만한가? (섹션 5·7·8 겨냥)
5. oq-106 2026-07-27 AI Act 통합판에서 기계류 연계 로봇 AI 에 어떤 조문이 적용되며, 중대한 변경 재평가·시판 후 감시 조문은 무엇을 정하는가? (섹션 3·7·11 겨냥)
6. oq-105 한국 인공지능기본법의 현행 판 시행일과 고영향 AI 사업자의 문서화 책무는 무엇인가? (섹션 3·7·11 겨냥)
7. oq-030 LTAA 원문 수치 충돌은 위키 안에서 어디까지 정리됐는가? (섹션 11 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | MLflow v3.1.0 모델 레지스트리 문서는 별칭(alias)을 새 모델 버전으로 재지정하면 같은 별칭 기반 모델 로딩 코드가 다음에 실행될 때 새 버전을 자동으로 가져온다고 설명한다. 이미 실행 중인 프로세스나 연결이 끊긴 장치의 모델이 바로 바뀐다는 뜻은 아니다. | ref-1577 | 아니오 | medium | 2026-10-12 | — | — |
| f2 | [의견] | ROP 는 레지스트리의 목표 모델 버전과 각 로봇이 실제로 실행 중인 버전을 따로 기록하고, 별칭 변경 뒤 장치별 로딩·검증 응답을 받아야 교체가 끝났다고 볼 수 있다. | ref-1577 | 아니오 | low | 2026-10-12 | — | — |
| f3 | [사실] | LeRobot v0.6.0 하위 호환성 문서는 PR #1452 이후 정책 가중치에 내장되던 정규화 계층을 없애고 외부 PolicyProcessorPipeline 구성요소가 정규화를 맡도록 바꾼 변경을 '호환성 깨짐(Breaking Change)'으로 명시하고, 이전 모델은 이전(migration)이 필요하다고 적는다. | ref-1578 | 아니오 | medium | 2026-10-12 | — | — |
| f4 | [사실] | 같은 문서는 하드웨어 API 재설계(PR #777) 이전의 보정 방식으로 기록한 궤적을 그대로 불러오면 잘못 재생된다고 경고한다(SO100/SO101 예시의 관절 보정·입출력 변환). | ref-1578 | 아니오 | medium | 2026-10-12 | — | — |
| f5 | [사실] | LeRobotDataset v3.0 형식은 여러 에피소드의 표 행과 영상 프레임을 큰 파일로 이어 붙이고, 에피소드별 구간은 파일 경계가 아니라 메타데이터로 복원한다. | ref-1578 | 아니오 | medium | 2026-10-12 | — | — |
| f6 | [의견] | 학습 정책을 로봇에 배포할 때는 가중치 해시, 전·후처리기와 정규화 통계, 학습 데이터 커밋과 데이터 형식 판, 카메라·관절 스키마, 하드웨어 보정판, 런타임 판을 하나의 배포 묶음으로 기록하고 이전 묶음을 보존해야 되돌림이 가능하다. | ref-1578 | 아니오 | low | 2026-10-12 | — | — |
| f7 | [추정] | Mender 문서는 사용자 정의 업데이트 모듈(Update Module)이 롤백을 지원하려면 SupportsRollback 질의에 Yes 로 답하고, 설치 전에 '알려진 정상 상태(known good state)'를 저장했다가 롤백 때 복원하는 구현을 모듈 작성자가 넣어야 한다고 설명한다. | ref-1579 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f8 | [추정] | Mender 문서는 전원 상실 뒤 업데이트 상태가 다시 실행될 수 있으므로 업데이트 모듈을 멱등(idempotent)하게 만들어야 한다고 권고한다(should). | ref-1579 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f9 | [추정] | AWS IoT Jobs 문서는 작업 배포 속도(rollout)와 중단(abort) 설정을 두고, 실패한 장치 수 등이 지정한 기준에 도달하면 작업 배포를 취소할 수 있다고 설명한다. 이는 새 배포를 멈추는 것이며 이미 설치된 장치의 원복과는 별개다. | ref-1581 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f10 | [추정] | AWS IoT Greengrass v2 문서는 장치별 배포 실패 상태를 롤백 미요청(FAILED_ROLLBACK_NOT_REQUESTED), 이전 정상 구성으로 롤백 완료(FAILED_ROLLBACK_COMPLETE), 롤백 실패(FAILED_UNABLE_TO_ROLLBACK)로 나누고, 롤백하지 않았거나 롤백에 실패한 장치는 정상 동작하지 않을 수 있다고 적는다. | ref-1580 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f11 | [의견] | 모델 배포는 배포 중단, 이전 모델 복원 시도, 복원 확인을 서로 다른 상태로 기록하고, 확대 배포 여부는 집단 성공률만이 아니라 장치별 현재 버전·실패 사유·복구 결과로 판단하며, 복구하지 못한 로봇은 새 작업 배정에서 빼는 운영 정책을 두는 것이 맞다. | ref-1579, ref-1580, ref-1581 | 아니오 | low | 2026-10-12 | — | — |
| f12 | [추정] | Viam 문서는 새 모델을 플릿에 내보낼 때 갱신한 구성 조각(fragment)을 먼저 첫 집단(예: 카나리 위치)에만 적용해 관찰한 뒤 나머지 집단으로 넓히는 절차를 제시한다. | ref-1582 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f13 | [추정] | 같은 Viam 문서는 새 모델이 잘못 보이면 구성 조각에서 이전 판을 고정해 되돌리며, 장치들은 다음 구성 동기화 때(정상 운영에서는 수 초 안에) 이전 판으로 수렴한다고 설명한다. 연결이 끊긴 장치의 즉시 변경은 아니다. | ref-1582 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f14 | [사실] | ML Test Score 의 Infra4 항목은 모델이 실제 요청에 영향을 주기 전에 품질을 자동 검사해 모델을 승인(bless)하거나 거부(veto)해 운영 투입을 막는 절차를 권한다. | ref-625 | 아니오 | medium | 2026-10-12 | — | — |
| f15 | [사실] | 같은 논문의 Infra6 항목은 오프라인 시험이 아무리 광범위해도 그것만으로는 운영 환경에서의 모델 성능을 보장할 수 없다고 밝히고, 소수 트래픽에 먼저 내보내는 카나리 방식을 완화책으로 든다. | ref-625 | 아니오 | medium | 2026-10-12 | — | — |
| f16 | [사실] | 같은 논문의 Infra7 항목은 운영 모델을 이전 정상판으로 되돌리는 롤백을 비상 절차로 두고, 운영자가 비상 상황이 아닐 때 미리 연습해야 한다고 권고한다(should). | ref-625 | 아니오 | medium | 2026-10-12 | — | — |
| f17 | [의견] | 로봇 모델의 운영 투입 승인 기록에는 장치·현장별 성능 하한, 기존 판 대비 퇴행, 로딩·추론 지연, 개입·실패 사례, 실제 롤백 연습 결과를 연결하고, 위험한 행동의 시험은 현장 안전 절차와 분리하지 않아야 한다. | ref-625 | 아니오 | low | 2026-10-12 | — | — |
| f18 | [사실] | KnowNo(Ren 외, CoRL 2023, PMLR 229) §3.1 의 등각 예측 보장은 보정 집합과 새 시험 표본이 같은 미지의 분포 D 에서 독립·동일 분포(i.i.d.)로 뽑힌다는 가정 위에 선다. | ref-351 | 아니오 | medium | 2026-10-12 | — | — |
| f19 | [사실] | KnowNo 의 과제 성공 보장(§3.2 명제)의 증명은 사람이 정확하게 도와준다는 가정에 기댄다. | ref-351 | 아니오 | medium | 2026-10-12 | — | — |
| f20 | [사실] | KnowNo 는 다단계 계획에서 시점 사이 의존성 때문에 i.i.d. 가정이 깨지는 문제를 다루려고 개별 시점 대신 시퀀스 수준에서 보정(sequence-level calibration)한다. | ref-351 | 아니오 | medium | 2026-10-12 | — | — |
| f21 | [사실] | 적응형 등각 추론(Adaptive Conformal Inference, Gibbs·Candès, NeurIPS 2021)의 명제 4.1 은 분포가 시간에 따라 바뀌어도 장기간의 경험적 포함 빈도가 목표값에 맞는다는 장기 평균 보장을 준다. 논문 실험은 주가 변동성·선거 데이터이며 로봇 실험은 없다. | ref-1583 | 아니오 | medium | 2026-10-12 | — | — |
| f22 | [사실] | 같은 방법의 온라인 갱신은 직전 예측 집합들이 정답을 놓친 경험적 빈도(empirical miscoverage)를 보고 임계값을 조정하므로, 운영 중 정답(Y_t)을 관측할 수 있어야 쓸 수 있다. | ref-1583 | 아니오 | medium | 2026-10-12 | — | — |
| f23 | [의견] | 물류 지시 분포가 바뀌는 현장에서는 고정 간격(예: 매월) 재보정을 근거 없는 기본값으로 두지 말고, 지시 유형별 보정 오차와 데이터 변화 신호를 감시하며 피드백 지연·정답 수집 비용을 고려한 재보정 정책을 시험해야 한다. | ref-351, ref-1583 | 아니오 | low | 2026-10-12 | — | — |
| f24 | [사실] | 제조사 연구(저자 전원 AGIBOT 소속, 저자 보고)인 Learning While Deploying(LWD, arXiv v4)은 자사 Agibot G1 양팔 로봇 16대 플릿(식료품 보충 작업 4대, 장기 작업마다 3대)으로 8개 실물 조작 작업에서 온라인 학습을 했고, 방법마다 실험당 4시간 벽시계 예산(플릿 합계 약 60시간)을 줬다. | ref-1585 | 아니오 | medium | 2026-10-12 | — | — |
| f25 | [사실] | LWD 의 학습기는 50 학습 단계마다 갱신 정책을 플릿에 내보내고, 로봇 액터는 에피소드 경계에서 새 정책을 다시 불러온다(제조사 연구, 저자 보고). | ref-1585 | 아니오 | medium | 2026-10-12 | — | — |
| f26 | [사실] | LWD 저자는 한계 절에서 현재 정책 학습 틀이 실행 안전을 명시적으로 모델링하지 않으며, 단순한 실시간 갱신 일정이 대규모·장기 배포에 최적이 아닐 수 있다고 밝힌다. | ref-1585 | 아니오 | medium | 2026-10-12 | — | — |
| f27 | [의견] | 운영 중 학습하는 정책을 쓰는 플릿에서는 작업 이력마다 실행한 정책 판을 붙이고, 새 정책을 적용하는 경계(예: 에피소드·임무 단위)와 승인 주체를 명시해야 임무 도중 모델이 바뀌는 문제를 관리할 수 있다. | ref-1585 | 아니오 | low | 2026-10-12 | — | — |
| f28 | [추정] | LG CNS 는 2026-05-07 발표에서 로봇 학습·운영 플랫폼 '피지컬웍스'의 포지(Forge)에서 학습·검증한 로봇을 바통(Baton)으로 운영·관제하고, 이 과정에서 축적한 데이터를 다시 학습에 쓰는 선순환 체계를 구축했다고 밝혔다. | ref-1584 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f29 | [추정] | 같은 발표는 AMR·AGV 등 100대 규모 운영 환경에 바통을 적용하면 생산성이 약 15% 이상 오르고 운영비가 최대 18% 줄 것으로 '기대된다'고 적으며, 이는 실측 비교 결과가 아니라 회사의 기대치다. | ref-1584 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f30 | [추정] | 같은 발표는 포지가 20곳 이상 고객사와 로봇 개념검증(PoC)을 진행 중이고, 바통이 부산 스마트시티 국가 시범도시 사업에서 순찰·바리스타·짐캐리·청소 4종 로봇의 통합 관제에 쓰이고 있다고 주장한다. | ref-1584 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f31 | [의견] | 학습·운영 연계 플랫폼을 도입 검토할 때는 시연, PoC, 상시 운영을 서로 다른 수준의 증거로 받고, 모델 갱신 이력·고객 검수·장애 복구 기록을 따로 요청해야 한다. | ref-1584 | 아니오 | low | 2026-10-12 | — | — |
| f32 | [사실] | AI-Hub '대규모 물리환경 로봇조작 데이터'(dataSetSn 71825)의 변경이력은 v1.0 을 2025-04-16 데이터 개방(Beta), v1.1 을 2025-06-30 데이터 최종 개방으로 표시한다. | ref-1588 | 아니오 | medium | 2026-10-12 | — | — |
| f33 | [사실] | 같은 페이지의 데이터 히스토리에서 2026-05-06 항목은 '기타 – 태그 추가'로만 표시돼 새 데이터 판 발행으로 볼 근거가 없다. | ref-1588 | 아니오 | medium | 2026-10-12 | — | — |
| f34 | [사실] | 같은 데이터의 학습용 구성표(라벨링 JSON 기준)는 총 262,166 건 중 학습 238,266 건, 테스트 23,900 건을 적으면서 표제는 '학습 데이터 (80%)', '테스트 데이터 (10%)'로 달아, 실제 비율(약 90.9%·9.1%)과 맞지 않고 검증 분할은 표기하지 않는다. | ref-1588 | 아니오 | medium | 2026-10-12 | — | — |
| f35 | [사실] | 같은 데이터의 원천 데이터는 실제환경 77,984 장, 가상환경 184,182 장(RGB 기준, Depth 같은 수)으로, 전체 262,166 장 가운데 약 70% 가 가상환경에서 취득됐다. | ref-1588 | 아니오 | medium | 2026-10-12 | — | — |
| f36 | [사실] | 같은 페이지의 분포 표는 원천 데이터 분포 비율을 실제 14.29%·가상 85.71% 로 적어 수량(약 29.7%·70.3%)과 맞지 않고, 라벨링 JSON 수량(77,984 + 184,182 = 262,166)의 합계를 524,332 로 적는다. | ref-1588 | 아니오 | medium | 2026-10-12 | — | — |
| f37 | [의견] | 공개 데이터의 분할비·합계가 서로 맞지 않으면 제공자 확인 전에는 표제 분할비를 모델 승인 근거로 쓰지 말고, 실물·가상 구분, 중복, 평가용 누출을 실제 파일로 따로 검사해야 한다. | ref-1588 | 아니오 | low | 2026-10-12 | — | — |
| f38 | [사실] | NIST AI RMF 1.0(NIST AI 100-1)의 MANAGE 4.1 은 배포 후 AI 시스템 감시 계획에 사용자·관련 AI 행위자 의견 수집·평가, 이의 제기와 무효화(override), 폐기, 사고 대응, 복구, 변경관리 장치를 넣어 실행하도록 한다(자율 적용 프레임워크). | ref-1586 | 아니오 | medium | 2026-10-12 | — | — |
| f39 | [의견] | 모델 공급자의 학습·검증 책임, ROP 의 배포·실행 판 기록, 현장 운영자의 개입·사고 통보 역할은 계약과 운영 절차에서 따로 정해야 하며, 조직 단위 관리 체계 인증만으로 특정 로봇 모델의 안전 성능을 승인해서는 안 된다. | ref-1586 | 아니오 | low | 2026-10-12 | — | — |
| f40 | [사실] | EUR-Lex 의 AI Act(Regulation (EU) 2024/1689) 2026-07-27 통합판은 Regulation (EU) 2026/1744(2026-07-08 채택, 관보 2026-07-24 게재) 개정을 반영하며, 이 개정으로 부속서 I Section A 에서 기계류(1번 항목)가 삭제되고 Section B 21번에 기계류 규정 (EU) 2023/1230 이 추가됐다. | ref-1587 | 아니오 | medium | 2026-10-12 | — | — |
| f41 | [사실] | 개정된 AI Act 제2조 2항은 부속서 I Section B 의 조화 법령 대상 제품과 관련해 제6조 1항으로 고위험이 되는 AI 시스템에는 제6조 1항, 제60a조, 제102~112조만 적용하고, 제57~59조는 해당 법령에 고위험 요구사항이 통합된 범위에서만 적용한다고 정한다. | ref-1587 | 아니오 | medium | 2026-10-12 | — | — |
| f42 | [사실] | AI Act 제43조 4항은 적합성 평가를 거친 고위험 AI 시스템이 중대한 변경(substantial modification)을 겪으면, 변경된 시스템을 다시 유통하든 같은 배포자가 계속 쓰든 새 적합성 평가 절차를 거치도록 정한다. | ref-1587 | 아니오 | medium | 2026-10-12 | — | — |
| f43 | [사실] | 같은 항은 출시·사용 개시 뒤에도 계속 학습하는 고위험 AI 시스템에서, 제공자가 최초 적합성 평가 때 미리 정하고 부속서 IV 2(f) 기술문서에 담은 시스템·성능 변경은 중대한 변경으로 보지 않는다고 정한다. | ref-1587 | 아니오 | medium | 2026-10-12 | — | — |
| f44 | [사실] | AI Act 제72조 2항은 제공자의 시판 후 감시 체계가 배포자 제공 등으로 얻은 고위험 AI 시스템의 성능 관련 데이터를 수명 전반에 걸쳐 능동적·체계적으로 수집·문서화·분석하고, 관련되는 경우 다른 AI 시스템과의 상호작용 분석을 포함하도록 정한다. | ref-1587 | 아니오 | medium | 2026-10-12 | — | — |
| f45 | [추정] | 제2조 2항 개정에 따라 기계류 규정 대상 로봇의 안전 구성요소로서 부속서 I 경로로 고위험이 되는 AI 에는 제43조(중대한 변경 시 재평가)와 제72조(시판 후 감시)가 AI Act 조문으로 바로 적용된다고 볼 수 없으며, 이 두 조문은 Section A 법령·부속서 III 경로의 고위험 AI 에 해당하는 내용으로만 소개해야 한다. 위키의 '부속서 I(기계류 등) 고위험' 서술도 이 이동을 반영해야 한다. | ref-1587 | 아니오 | medium | 2026-10-12 | — | — |
| f46 | [의견] | EU 시장을 대상으로 할 때는 적용 관할·시스템 분류·공급자 지위를 먼저 정하고, 그 뒤 최초 평가에서 허용한 변경 범위와 실제 모델 변경 내역을 대조할 수 있도록 변경 기록을 보존하는 것이 맞다. | ref-1587 | 아니오 | low | 2026-10-12 | — | — |
| f47 | [사실] | 한국 인공지능기본법 제34조 1항은 고영향 인공지능 또는 이를 이용한 제품·서비스를 제공하는 인공지능사업자가 대통령령으로 정하는 바에 따라 각 호의 안전성·신뢰성 확보 조치를 이행하도록 하며, 5호는 그 조치 내용을 확인할 수 있는 문서의 작성과 보관이다. | ref-620 | 아니오 | medium | 2026-10-12 | — | — |
| f48 | [사실] | 국가법령정보센터의 현행 조문은 「인공지능 발전과 신뢰 기반 조성 등에 관한 기본법」을 법률 제21311호(2026-01-20 공포·일부개정), 시행 2026-07-21 판으로 표시한다. 위키의 '2026-01-22 시행'은 최초 법률·시행령 기준이고 개정 법률의 시행일은 2026-07-21 이다. | ref-620 | 아니오 | medium | 2026-10-12 | — | — |
| f49 | [추정] | 제34조의 문서 작성·보관 책무가 물류 현장의 작업 계획·배정 AI 를 쓰는 ROP 에 걸리는지는 고영향 인공지능 해당성과 사업자 지위(제공자·이용자) 판단이 먼저이며, 시행령상 보존 기간도 이번에 확인하지 못했다. | ref-620 | 아니오 | low | 2026-10-12 | — | — |
| f50 | [의견] | ROP 는 학습용 데이터 개요, 모델 판, 위험 조치, 사람 감독, 승인·복구 기록을 서로 연결해 두어, 고영향 해당성이 판단되면 제34조 문서로 낼 수 있는 구조를 미리 갖추는 것이 좋다. | ref-620 | 아니오 | low | 2026-10-12 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1577 | MLflow 프로젝트 (Linux Foundation 오픈소스 프로젝트) | Model Registry Workflows (docs/docs/classic-ml/model-registry/workflow.mdx, MLflow v3.1.0) | 2025-06-10 | 오픈소스 문서 | high | 2026-10-12 | https://github.com/mlflow/mlflow/blob/v3.1.0/docs/docs/classic-ml/model-registry/workflow.mdx | 아니오 |
| ref-1578 | Hugging Face LeRobot 기여자 (huggingface/lerobot) | Backward compatibility (docs/source/backwardcomp.mdx, LeRobot v0.6.0) | 2026-07-06 | 오픈소스 문서 | high | 2026-10-12 | https://github.com/huggingface/lerobot/blob/v0.6.0/docs/source/backwardcomp.mdx | 아니오 |
| ref-1579 | Northern.tech (Mender documentation) | Create a custom Update Module | 미확인 | 벤더 문서 | medium | 2026-10-12 | https://docs.mender.io/artifact-creation/create-a-custom-update-module | 아니오 |
| ref-1580 | Amazon Web Services (AWS IoT Greengrass V2 Developer Guide) | Check deployment status | 미확인 | 벤더 문서 | medium | 2026-10-12 | https://docs.aws.amazon.com/greengrass/v2/developerguide/check-deployment-status.html | 아니오 |
| ref-1581 | Amazon Web Services (AWS IoT Core Developer Guide) | How job configurations work | 미확인 | 벤더 문서 | medium | 2026-10-12 | https://docs.aws.amazon.com/iot/latest/developerguide/jobs-configurations-details.html | 아니오 |
| ref-1582 | Viam | Roll out a new model to a fleet | 미확인 | 벤더 문서 | medium | 2026-10-12 | https://docs.viam.com/vision/deploy-and-maintain/roll-out-to-fleet/ | 아니오 |
| ref-1583 | Gibbs, I., & Candès, E. J. (NeurIPS 2021) | Adaptive Conformal Inference Under Distribution Shift | 2021-12-06 | 논문 | high | 2026-10-12 | https://papers.nips.cc/paper/2021/file/0d441de75945e5acbc865406fc9a2559-Paper.pdf | 아니오 |
| ref-1584 | LG CNS | LG CNS, 로봇 학습·운영 플랫폼 '피지컬웍스' 공개 | 2026-05-07 | 벤더 문서 | low | 2026-10-12 | https://www.lgcns.com/kr/newsroom/press/detail.rx-2605-1 | 아니오 |
| ref-1585 | Wang, Y. 외 (AGIBOT) | Learning While Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies | 2026-09-16 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2605.00416v4 | 아니오 |
| ref-1586 | NIST | Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1 | 2023-01 | 정부·연구기관 | high | 2026-10-12 | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf | 아니오 |
| ref-1587 | European Union (EUR-Lex) | Regulation (EU) 2024/1689 (Artificial Intelligence Act) — consolidated text 02024R1689-20260727 (incl. M1 Regulation (EU) 2026/1744) | 2026-07-27 | 정부·연구기관 | high | 2026-10-12 | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02024R1689-20260727 | 아니오 |
| ref-1588 | AI-Hub (한국지능정보사회진흥원) | 대규모 물리환경 로봇조작 데이터 | 2025-06-30 | 정부·연구기관 | medium | 2026-10-12 | https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&dataSetSn=71825&topMenu=100 | 아니오 |
| ref-625 | Breck, E. 외 (Google Research) | The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction | 2017-12 | 논문 | medium | 2026-10-12 | https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/ | 아니오 |
| ref-351 | Ren, A. Z. 외 | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners | 2023-07 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2307.01928 | 아니오 |
| ref-620 | 국가법령정보센터(과학기술정보통신부) | 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법 | 2026-01-20 | 정부·연구기관 | medium | 2026-10-12 | https://www.law.go.kr/lsInfoP.do?lsiSeq=268543 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md | 3, 4, 5, 6, 7, 8, 9, 11 | 갱신(차등): 섹션 3 — 67행 법·규제 문단 정정: 한국 인공지능기본법은 '2026-01-22 시행(최초 법률·시행령)'에 개정 법률 제21311호(2026-01-20 공포, 2026-07-21 시행, f48)를 더해 '개정 법률의 시행일 … 미확인'을 지움, 제34조 1항 5호 문서 작성·보관(f47, 해당성은 f49 [추정]). EU AI Act '부속서 I(기계류 등) … 고위험' 문장은 2026-07-27 통합판 기준으로 기계류 규정 (EU) 2023/1230 이 Section B(21번)로 옮겨졌고(f40) 제2조 2항이 Section B 관련 고위험 AI 에는 제6조 1항·제60a조·제102~112조만 적용한다(f41)는 점을 덧붙이고, 제43·72조를 로봇(기계류) AI 에 바로 연결하지 않음(f45 [추정]) / 섹션 4(분리 2026-09-25-area27-s4) — '등각 예측' 항목(41행)에 i.i.d. 보정 조건(f18)과 사람 도움 정확성 가정(f19) 추가, '모델 레지스트리' 항목(44행)에 별칭 반영 시점이 다음 로딩(f1)임을 보충, 배포 묶음 호환성(정규화 외부화 f3, 보정 방식 변경 f4, 메타데이터 기반 에피소드 f5) 항목 추가 / 섹션 5 — 출하 시나리오 '예외·성과' 칸(105행)에 별칭 반영 시점(f1)·오프라인 시험 한계와 카나리(f15)·롤백 연습(f16) 보강; 사례 추가: Viam 단계 배포·이전 판 고정(f12·f13, 벤더 주장 [추정]), LWD 플릿 온라인 학습(f24·f25·f26, '제조사 연구·저자 보고' 표기, 이종 플릿 아님), LG CNS 피지컬웍스 학습–운영 연계(f28~f30, 벤더 주장 [추정], 15%·18% 는 회사 기대치); 의견 f27·f31 / 섹션 6(분리 2026-09-25-area27-s6) — '모델 운영 관리' 소절(69행): MLflow 별칭 문장에 반영 시점 범위(f1, 기존 문장은 틀리지 않음 — 범위 보충), ML Test Score 28개 항목 문장 뒤에 Infra4 승인·거부(f14), Infra6 오프라인 시험 한계(f15), Infra7 롤백 연습(f16); 롤백 구현 책임·배포 중단 상태(Mender f7·f8, AWS IoT Jobs f9, Greengrass f10 — 모두 벤더 주장 [추정]) 새 소절; '필요할 때 되묻기' 소절(57행) KnowNo 문장에 보장 조건(f18·f19·f20); 의견 f2·f11·f17·f23. 기존 내용 확인(새로 넣지 않음): Mender 상태 스크립트·롤백 표시·A/B 원자 배포·단계적 배포(2026-10-09-area43-s6.md 48~50행, 2026-09-30-area43-s6.md 57행; ref-1323·ref-1324·ref-1040), aws-samples ROS 2 OTA 자동 롤백(ref-556) / 섹션 7(분리 2026-09-25-area27-s7) — 표: MLflow 행(44행)에 v3.1.0 고정 문서 근거(f1, ref-1577, ref-626 은 latest 판), LeRobot v0.6.0 호환성·LeRobotDataset v3.0 행 추가(f3~f5), NIST AI RMF 행에 MANAGE 4.1(f38, 본문 PDF ref-1586), AI-Hub 71825 행 추가(f32~f36: v1.1 2025-06-30, 2026-05-06 은 태그만, 표제 80%/10% 와 실제 약 90.9%/9.1% 불일치·검증 분할 없음, 가상환경 약 70%, 분포 비율·JSON 합계 불일치; 의견 f37). 48행 관련 법 문단: 한국 법 시행일·제34조(f47·f48·f49, 의견 f50), EU AI Act 문장에 Section B 이동·제2조 2항(f40·f41)과 제43조 4항 재평가·사전 정한 지속학습 변경 예외(f42·f43)·제72조 2항(f44)을 '조문 내용 소개'로만 넣고 기계류 연계 로봇 AI 에 바로 적용되지 않음을 명시(f45 [추정]); 의견 f46. ISO/IEC 42001 행은 그대로(이번 원문 미확인) / 섹션 8(분리 2026-09-25-area27-s8) — KnowNo 항목(41행)에 PMLR 229 학회판과 가정(f18·f19·f20), ML Test Score 항목(50행)에 Infra4·6·7(f14~f16), ACI 항목 추가(f21·f22, 로봇 실험 없음), LWD 항목 추가(f24~f26, 제조사 연구·프리프린트) / 섹션 9 — 책임 경계: 배포 후 감시·변경관리(f38)와 공급자·ROP·현장 운영자 역할 분리(의견 f39), 배포 중단·복원 상태 기록과 복구 실패 로봇의 배정 제외(의견 f11) / 섹션 11 — oq-030: '이번 실행에서는 조사하지 않았다'를 기존 내용 확인으로 갱신(2026-10-10-area25-s6.md 59~63행, 2026-10-10-area25-s11.md 41행, 후속 질문 oq-356; LTAA 75.97%·77.1%·DP 0.95 는 새 finding 으로 넣지 않음), 상태 열림 유지. id 없이 '(신규 …)'로 적힌 세 질문은 docs/open-questions.md 문구 대조로 oq-105·oq-106·oq-107 과 같으므로 id 를 붙임. 부분 답(열림 유지): oq-105(f47·f48·f49), oq-106(f40~f45: 제품 안전 구성요소 해당성은 판단하지 않고, 기계류는 Section B·제2조 2항 경로임만 확인), oq-107(f18~f23: 가정 확인, 재보정 주기 미해결), oq-213(f12·f13 Viam 단계 배포·되돌림, 벤더 주장), oq-222(f21·f22 분포 이동 아래 온라인 재보정의 조건, 배정 정책 되돌림 기준은 아님). 새 질문 4건 / 후속 정리(이번 갱신 범위 밖, 다른 페이지): docs/categories/ai-and-learning/index.md 131행·160행과 docs/categories/safety/index.md 149행의 'EU AI Act 부속서 I(기계류 등) 고위험' 서술에 Section B 이동·제2조 2항(f40·f41) 반영, index.md 160행 '2026-01-22 시행'에 개정 법률 2026-07-21 시행(f48) 반영, ref-168 저자 표기('Kaitha, S., & Yu, S. 외' → Shyam prasad reddy Kaitha·Hongrui Yu 2명), ref-626 은 latest 판이라 고정 판 ref-1577 과 구분. 다음 실행 후보: 43. 데이터·관측성·배포(f7~f13), 57. 자산·소프트웨어 수명주기 관리(f3~f6), 59. 법·규제·보험·라이선스(f40~f49) |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- 학습 모델·전처리기(정규화 통계)·하드웨어 보정판이 함께 바뀌는 변경을 로봇 플릿에서 어느 시험 단위로 승인하고, 실패 시 어느 묶음 단위로 복구할 것인가? | 관련 영역: 47. AI·학습·적응과 모델 운영, 57. 자산·소프트웨어 수명주기 관리 | 근거: f6 | 종류: 일반
- 운영 중 학습 정책을 에피소드 경계에서 갱신하는 방식이 제조사가 다른 이기종 로봇과 중간에 끊을 수 없는 장기 임무에서도 적절한가, 임무 도중 정책 판이 바뀌지 않게 하는 경계를 어떻게 정할 것인가? | 관련 영역: 47. AI·학습·적응과 모델 운영, 43. 데이터·관측성·배포 | 근거: f25 | 종류: 일반
- 출처 충돌: AI-Hub 대규모 물리환경 로봇조작 데이터(71825)의 분할 표제(학습 80%·테스트 10%)와 건수(238,266·23,900), 원천 분포 비율(14.29%·85.71%)과 수량(77,984·184,182), 라벨링 JSON 합계(524,332)와 건수 합(262,166) 가운데 어느 값이 맞으며 실제 배포 파일과 일치하는가? | 관련 영역: 47. AI·학습·적응과 모델 운영 | 근거: f36 | 종류: 출처 충돌
- 모델 공급자와 ROP 가 함께 확인할 수 있는 모델 변경·배포·복구 증거(판 식별, 승인 기록, 장치별 적용·롤백 결과)의 최소 항목은 무엇인가? | 관련 영역: 47. AI·학습·적응과 모델 운영, 59. 법·규제·보험·라이선스 | 근거: f39 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 12건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-12-04/external_research.md)를 변환했다. 2026-10-12 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.
    - f45: EU AI Act 제2조 2항 개정에 따른 기계류 연계 로봇 AI 의 적용 조문 해석은 조문 범위에서 이끈 [추정]이다. 기계류 규정 (EU) 2023/1230 쪽에 AI 고위험 요구가 어떻게 통합되는지(제102~112조 개정 내용)와 개별 ROP 의 분류·제공자 지위는 확인하지 않음
    - f48: 인공지능기본법 시행령의 개정 판(독립 검증 보고상 2026-08-18 공포)과 고영향 영역 목록·보존 기간은 원문 확인하지 않음. 최초 법률·시행령의 2026-01-22 시행은 기존 위키 기준(ref-620)이며 이번에 다시 대조하지 않음
    - f32~f36: AI-Hub 71825 는 설명 페이지 메타데이터만 확인했고 실제 데이터 파일(건수·분할·실제/가상 구분)은 열지 않음. 표의 비율·합계 불일치의 정답은 제공자 확인 필요
    - f24~f26: LWD 는 저자 전원 AGIBOT 소속의 제조사 연구 프리프린트이며 독립 재현·안전 검증·이기종 장기 운영 성과는 없음
    - f7~f13, f28~f30: Mender·AWS·Viam·LG CNS 문서·발표만 근거라 벤더 주장 [추정]. 기존 위키는 Mender ref-1323 을 [사실]로 두었으나 이번 변환은 저장소 규칙(벤더 문서 단독 → 추정)을 적용. LG CNS 의 15%·18% 기대 효과와 PoC 현황은 독립 측정·확인 없음
    - 메모 F21(ISO/IEC 42001 공식 FAQ)은 독립 검증에서 원문을 열지 못했고(Cloudflare) 기존 위키(s7 42행, ref-618)와 중복이라 넣지 않음. ISO/IEC 42001·23894 유료 본문과 국내 로봇기업 인증 범위는 미확인
    - 메모 A15(LTAA 75.97%·77.1%·DP 0.95)는 2026-10-10 영역 25 갱신(2026-10-10-area25-s6.md 59~63행, area25-s11.md 41행, oq-356)과 완전 중복이라 새 finding 으로 넣지 않음. DP 0.95 와 Heavy Excels 77.1% 의 동일 조건 비교는 여전히 미해결
    - MLflow 별칭 변경이 이기종 플릿 전체에 원자적으로 반영되거나 연결이 끊긴 장치에서 즉시 복구되는지, 모델·전처리·보정판을 묶은 실물 전원 차단·복구 시험 결과는 확인하지 못함
    - KnowNo 의 물류 현장 재보정 주기(oq-107), ACI 의 피드백 지연 환경 로봇 성능, 로봇 모델별 보편 회귀 허용 임계값은 미확인
    - 메모가 조사 기준으로 쓴 고정 위키 커밋과 현재 배포판의 동일성은 확인하지 않음
- 범위 경계 위반 의심:
    - f40~f49: EU AI Act·한국 인공지능기본법의 적용 해석은 59. 법·규제·보험·라이선스 쪽 내용이므로 조문 확인과 적용 범위 주의까지만 하고 개별 제품·사업자의 의무 발생 여부는 판단하지 않음
    - f7~f13: 장치 업데이트·단계 배포 도구(Mender·AWS IoT·Viam)는 43. 데이터·관측성·배포, 57. 자산·소프트웨어 수명주기 관리와 겹치며, 이 영역에는 모델 교체·되돌림 관점으로만 씀
    - f24~f26: LWD 의 저수준 조작 정책 학습 자체는 로봇 자체 지능·제어(연계 대상)이며, 이 영역에는 정책 판 갱신 경계와 운영 기록 관점으로만 씀
- 한계: 외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 12건/15(ref-1577~ref-1588, 예약 구간 ref-1577~ref-1606 안), 재사용 3건(ref-625·ref-351·ref-620). 출처 매핑(검증 결과 기준): 메모 n1→ref-1577(MLflow v3.1.0 고정 문서; ref-626 은 latest 판이라 새 id), n2→ref-1578, n3→ref-1579, n4→ref-1580, n5→ref-1581(URL 을 /iot/latest/developerguide/ 표준 경로로), n6→ref-1582, n7→ref-351(PMLR 229 학회판으로 열람), n8→ref-1583, n9→ref-1584(뉴스와이어 재게시는 같은 출처), n10→ref-1585, n11→ref-625(DOI 10.1109/BigData.2017.8258038), n12→ref-1586(본문 PDF; 기존 ref-617 은 보도자료), n13→ref-1587(M1 Regulation (EU) 2026/1744 명시), n14→ref-620(법률 제21311호 조문), n15(ISO/IEC 42001)·n17(LTAA, ref-168)은 finding 이 없어 출처에서 뺌. 교차 확인 0건(모든 사실 finding 이 단일 출처, AWS 두 문서는 같은 기관). 검증 반영: (a) A13 에 옴니버스 2026/1744 의 Section B 이동·제2조 2항(f40·f41)을 넣고 제43·72조(f42~f44)는 조문 내용 소개로 한정, 로봇(기계류) AI 에 바로 연결하지 않는다는 점을 f45 [추정]으로 명시, oq-106 부분 답; (b) A15 LTAA 수치는 완전 중복이라 제외하고 11절 oq-030 문장 갱신만 제안; A11 의 '학습 80%' 표제를 사실로 옮기지 않고 불일치(f34·f36)와 가상환경 약 70%(f35)를 추가; LWD 는 '제조사 연구·저자 보고' 표기(f24~f26); 한국 법 시행일 2026-07-21·법률 제21311호(f48); 벤더 문서(Mender·AWS·Viam·LG CNS) 단독 finding 은 추정+벤더 주장(f7~f10, f12·f13, f28~f30); Mender 상태 스크립트·단계 배포·A/B 원자 배포, AWS ROS 2 OTA 샘플, ISO 42001 정의는 기존 내용 확인으로만 rationale 에 적음. 열린 질문: 해결 없음. 부분 답 oq-105·oq-106·oq-107·oq-213·oq-222, oq-030 은 기존 내용 확인(열림 유지). 메모 '답한 열린 질문'의 new-1~new-3 은 docs/open-questions.md 문구 대조로 oq-105·oq-106·oq-107 과 같아 새로 만들지 않음. 메모의 '새로 생긴 열린 질문' 4건은 기존 질문과 문구가 겹치지 않아 새로 올림. 메모의 '.research-work' 로컬 경로·행 번호는 쓰지 않고 원문 절·쪽·조와 위키 실제 위치를 적었다. 2026-10-10-area27-* 는 다른 영역이라 쓰지 않음. 정정 요청 없음. 용어 후보 없음.
```

### runs/2026-10-12-03/research.md

```markdown
# 리서치 브리프 2026-10-12-03

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-12-03 |
| 날짜 | 2026-10-12 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 60. 노동·수용성·접근성 |
| 대분류 | P. 거버넌스·법규·사회 |

## 갭(비어 있거나 약한 섹션)

- 섹션 4. 핵심 개념과 용어(분리 2026-09-30-area60-s4) — '노사협의회 협의 사항'(39행)이 법률 제16320호(2019) 기준이고 작업·휴게 시간(제7호)과 고용조정 일반원칙(제6호)이 없음. 작업자 수용성 설문 자료의 표본 조건 설명 없음
- 섹션 5. 적용 사례 — 물류창고 사례(74행 Malik 면담)의 참여자 구성 미확인, 부상 지표가 GMU 발표 단일 근거이고 회사 발표·노조 보고서의 분모·정의 차이가 없음. 병원 사례가 한림대성심병원 자체 설문뿐이라 국내 독립 연구 없음. 실외 사례에 물품 인수 접근 요구 없음
- 섹션 6. 대표 접근법과 기술(분리 2026-09-30-area60-s6) — 수용성 측정이 고령자·돌봄 모델(알메러·Q방법론)뿐이고 산업 작업자 척도·표본 한계 없음, 노동자 참여 절차에 노사 공동 검토기구 사례 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스(분리 2026-09-30-area60-s7) — 디지털 접근성 표준(WCAG 2.2, WCAG2ICT, EN 301 549, 유럽 접근성법)과 자동 검사 도구가 없음. 근로자참여법 행이 '현행 조문 여부 미확인'
- 섹션 8. 대표 연구와 자료(분리 2026-09-30-area60-s8) — Acemoglu·Restrepo 항목(40행)에 JPE 2020 게재판의 총량·지역 효과 구분이 없고, 독일 등 비교 연구 없음. 수용성 연구들의 표본 조건(국가·언어·모집·인원) 미기재
- 섹션 9. 책임 경계 — 화면 접근성의 범위(웹 관제·비웹 HMI·로봇 단말 닫힌 기능·물리 접근)와 휴게·작업 순환 정책의 노사 검토 연계가 없음
- 섹션 11. 열린 질문(분리 2026-09-30-area60-s11) — oq-146·oq-188·oq-266·oq-278·oq-284~oq-287 이 모두 열림 상태
- 정정 요청 없음(target.json corrections 비어 있음). 메모·검증에서 나온 위키 내부 정정: 근로자참여법 제20조 판(2022-12-11 시행 법률 제18927호), 메모의 SOC '비교창고 456시설' 오기, Acemoglu 범위값은 오류 아님(유지)

## 조사 질문

1. 로봇 도입이 일하는 사람과 이용하는 사람 모두에게 받아들여지는가? [분류원문]
2. 공개된 작업자·산업 수용성 설문과 척도는 어떤 국가·언어·모집 방법·표본으로 만들어졌고, 한국 현장 작업자에게 일반화할 수 있는가? (섹션 4·6·8 겨냥)
3. 창고 로봇 도입의 안전 효과를 말하는 회사 발표와 노조 보고서는 지표 정의·분모·기간·범위가 어떻게 다른가(oq-286)? (섹션 5·9 겨냥)
4. 근로자참여법 제20조의 현행 판은 작업 배정·휴게·직무 전환을 협의 사항으로 두는가, 노사 공동 검토기구 사례는 무엇이 있는가(oq-285·oq-266)? (섹션 4·6·7 겨냥)
5. 웹 관제 화면, 비웹 HMI, 로봇 단말의 닫힌 기능에 각각 어떤 접근성 기준(WCAG 2.2, WCAG2ICT, EN 301 549, 유럽 접근성법)이 어떤 범위로 적용되고 자동 검사는 무엇을 놓치는가(oq-284)? (섹션 7·9 겨냥)
6. 장애인 이용자의 보행 접근과 물품 인수 접근, 국내 간호사 요구 연구는 어떤 조건에서 나온 결과인가(oq-188·oq-287)? (섹션 5·8 겨냥)
7. 로봇의 고용 효과 연구의 게재판 수치와 국가 간 차이는 무엇인가? (섹션 8 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Liu 외(Data in Brief 61, 2025)의 공개 작업자 설문 데이터셋은 미국·캐나다·영국·호주의 블루칼라 노동자 설문 참여자 530명 가운데 데이터 공개에 동의한 337명의 응답(40문항)만 담고 있다. | ref-1547 | 아니오 | medium | 2026-10-12 | — | — |
| f2 | [사실] | 이 설문의 모집 기간은 2022-04-05~2022-07-04 이며, 데이터셋 논문 발행(2025-06)과 3년 가까이 떨어져 있다. | ref-1547 | 아니오 | medium | 2026-10-12 | — | — |
| f3 | [사실] | 이 표본은 4개 선진국(미국·캐나다·영국·호주)의 6개 업종(제조·소매·운송·배송·우편, 창고, 건설, 계약직) 회사 연락처로 이메일 모집한 군집 표본(무작위 아님)이고, 영어로만 설문했으며, 남성 응답이 여성의 약 2배, 18~40세가 약 3분의 2, 창고 종사자는 123명(36.5%)이다. | ref-1547 | 아니오 | medium | 2026-10-12 | — | — |
| f4 | [추정] | Liu 외 데이터는 4개 영어권 선진국의 회사 연락망 표본이고 한국어 문항 타당화나 한국 작업자 응답이 없으므로, 한국 산업 현장 작업자 수용성의 대리값으로 일반화할 근거가 없다. 40문항도 안전·동료·로봇 협업·데이터 프라이버시를 나눠 묻는 문항 묶음이지 단일 수용성 점수로 타당화된 척도가 아니다. | ref-1547 | 아니오 | low | 2026-10-12 | — | — |
| f5 | [추정] | Malik 외(2026) 창고 작업자 연구에서 이번에 확인된 것은 초록의 'N = 12 semi-structured interviews' 뿐이다. 외부 메모가 적은 참여자 국가(영국 창고 근무 경험)·역할 구성(비관리 5명/관리·리더 7명)·로봇 사용 경험(7명)은 원문(Springer·KCL 저장소)이 접속 차단돼 확인하지 못했으므로, 5절 74행 문장은 그대로 두고 참여자 구성을 덧붙이지 않는다. | ref-1226 | 아니오 | low | 2026-10-12 | — | 원문 미열람 |
| f6 | [사실] | 포르투갈어판 산업 맥락 수용성 척도(FSQ-IC) 검증 연구(Pinto 외 6인, Human Behavior and Emerging Technologies 2025)는 연구진 네트워크 연락처로 배포한 온라인(LimeSurvey) 횡단 조사이며, 비확률 편의·눈덩이 표본 346명을 썼다. | ref-1548 | 아니오 | medium | 2026-10-12 | — | — |
| f7 | [사실] | 같은 논문의 표 1·2 는 탐색적 요인분석(EFA) 표본을 140명, 확인적 요인분석(CFA) 표본을 210명으로 적고, 이 가운데 로봇을 다뤄 본 적 없는 응답자가 각각 102명, 147명이다. 원문은 40%/60% 분할이라고 적지만 140+210=350 으로 §3.1 의 346명과 맞지 않아 원문 자체가 불일치한다. | ref-1548 | 아니오 | medium | 2026-10-12 | — | — |
| f8 | [추정] | FSQ-IC 검증 표본은 포르투갈어를 읽는 일반 성인 중심이고 로봇 무경험자가 다수(분석 표본의 약 70~73%)라서, 제목의 '산업 맥락'만으로 산업 현장 작업자에게서 검증된 척도로 볼 수 없고 한국 현장 작업자에게 그대로 옮길 근거도 없다. | ref-1548 | 아니오 | low | 2026-10-12 | — | — |
| f9 | [추정] | Amazon 은 2026-03-12 자사 발표(2026-03-27 수정)에서 전 세계 운영의 기록대상 사고율(Global RIR)이 지난 6년간(2019 대비) 43%, 휴업 사고율(Global LTIR)이 70% 개선됐다고 밝혔다. | ref-1549 | 아니오 | low | 2026-10-12 | 물류창고 / 예외·성과 | 벤더 주장 |
| f10 | [사실] | Strategic Organizing Center(SOC)의 2025-05 보고서는 Amazon 과 다른 사업주가 2020~2024년 매년 OSHA 에 제출한 부상·질병 자료를 분석했다. | ref-1550 | 아니오 | medium | 2026-10-12 | 물류창고 / 예외·성과 | — |
| f11 | [사실] | SOC 보고서는 '중대 부상'을 경작업 전환(light duty) 또는 휴업(lost time)을 초래한 부상으로 분류한다. | ref-1550 | 아니오 | medium | 2026-10-12 | 물류창고 / 예외·성과 | — |
| f12 | [사실] | SOC 의 창고 비교는 Amazon 이 2024년 OSHA 보고에서 일반 창고·보관업(NAICS 493110)으로 분류한 Amazon 자체 시설 456곳의 부상률을 비(非)Amazon 창고 전체와 비교한 것이며, 2024년 중대 부상률은 100명당 5.9 대 3.0 이었다. 외부 메모의 '비교 창고 456시설'은 틀린 표현이다. | ref-1550 | 아니오 | medium | 2026-10-12 | 물류창고 / 예외·성과 | — |
| f13 | [사실] | SOC 는 보고서에서 스스로 SEIU(서비스노조)·CWA(미국통신노조)·UFW(농장노동자연합)와 협력하는 노동 조직이라고 밝히므로, 이 보고서는 노동조합 쪽 이해당사자 자료다. | ref-1550 | 아니오 | medium | 2026-10-12 | — | — |
| f14 | [추정] | Amazon 발표(전 세계·2025 기준·2019 대비 개선율)와 SOC 보고서(미국·2024·비Amazon 창고 대비 수준)는 범위·기간·지표·분모가 다르고 같은 OSHA 신고 자료에 일부 기초하며 양쪽 모두 이해당사자 자료이므로, 서로 독립된 교차 확인이나 단순 모순으로 셀 수 없다. 로봇 센터만의 부상 효과도 어느 쪽에서도 분리되지 않는다. | ref-1549, ref-1550 | 아니오 | low | 2026-10-12 | 물류창고 / 예외·성과 | — |
| f15 | [사실] | 2026-10-12 국가법령정보센터에서 연 근로자참여 및 협력증진에 관한 법률 제20조 [시행 2022. 12. 11.] [법률 제18927호, 2022. 6. 10., 일부개정]의 제1항 제7호는 '작업과 휴게 시간의 운용'을 노사협의회가 협의하여야 할 사항으로 둔다. | ref-1551 | 아니오 | medium | 2026-10-12 | — | — |
| f16 | [사실] | 같은 판 제20조 제1항 제6호는 '경영상 또는 기술상의 사정으로 인한 인력의 배치전환ㆍ재훈련ㆍ해고 등 고용조정의 일반원칙'을 협의 사항으로 둔다. | ref-1551 | 아니오 | medium | 2026-10-12 | — | — |
| f17 | [사실] | 2022년판(법률 제18927호) 제20조 제1항에도 위키가 인용한 제2호(근로자의 채용ㆍ배치 및 교육훈련), 제9호(신기계ㆍ기술의 도입 또는 작업 공정의 개선), 제14호(사업장 내 근로자 감시 설비의 설치)가 같은 문구로 있으며, 제1항의 마지막 개정 표시는 '<개정 2019. 4. 16.>'이다. 따라서 4·7절의 '법률 제16320호 기준, 현행 여부 미확인'은 2022-12-11 시행판 기준으로 갱신할 수 있다. | ref-1551 | 아니오 | medium | 2026-10-12 | — | — |
| f18 | [추정] | 근로자참여법 제20조는 협의 사항을 열거할 뿐이므로, ROP 의 작업 배정·휴게 반영 정책이나 개별 작업자 처리량·위치 로그가 제6·7·14호 협의 대상에 해당하는지는 조문만으로 정해지지 않으며 판례·행정해석은 이번에도 찾지 못했다. | ref-1551 | 아니오 | low | 2026-10-12 | — | — |
| f19 | [사실] | ILO Working Paper 144(2025-07, Cornell University ILR School 소속 저자 5인)는 IBM 독일의 AI 기본협약이 AI 전문가와 사용자·근로자 대표로 구성된 AI 윤리위원회를 두고, 이 위원회가 AI 적용을 평가하고 협약 이행을 감독하며 AI 도구에 대한 직원 이의·불만을 논의하고 AI 권고를 검토·수정한다고 보고한다. | ref-1552 | 아니오 | medium | 2026-10-12 | — | — |
| f20 | [추정] | ILO Working Paper 144 는 ILO 공식 입장이 아니라 저자 견해를 담은 작업논문이며(면책 문구), 면담과 문헌에 기초한 질적 사례 연구다. 협약 원문을 싣지 않았고 IBM 면담 날짜가 각주 206(2021-11-08)과 부록 1(2024-07-26)에서 다르다. 사업장협의회 위원들이 협약이 안전보건과 AI 수용을 개선했다고 '느꼈다'는 서술도 측정된 효과가 아니다. | ref-1552 | 아니오 | low | 2026-10-12 | — | — |
| f21 | [사실] | WCAG 2.2(W3C 권고, 2024-12-12판) AA 성공기준 2.5.7(Dragging Movements)은 드래그가 필수이거나 기능이 사용자 에이전트가 정하고 저자가 수정하지 않은 경우가 아니면, 드래그로 하는 모든 기능을 드래그 없이 단일 포인터로 수행할 수 있어야 한다고 정한다. | ref-1553 | 아니오 | medium | 2026-10-12 | — | — |
| f22 | [사실] | WCAG 2.2 AA 성공기준 2.5.8(Target Size (Minimum))은 간격(Spacing)·동등한 대체(Equivalent)·인라인(Inline)·사용자 에이전트(User Agent Control)·필수(Essential) 다섯 예외를 빼면 포인터 입력 대상의 크기를 최소 24×24 CSS 픽셀로 정한다. | ref-1553 | 아니오 | medium | 2026-10-12 | — | — |
| f23 | [사실] | WCAG2ICT(W3C Group Note, 2025-12-11)는 WCAG 2 를 비웹 문서·소프트웨어에 적용하는 방법에 대한 정보성 안내이며, 규범이 아니고 요구사항을 정하지 않는다고 스스로 밝힌다. | ref-1556 | 아니오 | medium | 2026-10-12 | — | — |
| f24 | [사실] | WCAG2ICT 는 제품의 하드웨어 측면은 다루지 않는다고 적용 범위에서 제외한다. | ref-1556 | 아니오 | medium | 2026-10-12 | — | — |
| f25 | [사실] | EN 301 549 의 최종판은 V4.1.1(2026-09, ETSI 배포본 04.01.01_60)이며, 2025-11 의 V4.1.0(04.01.00_20·_30)은 초안 단계 문서다. V4.1.1 머리말은 이 문서가 지침 (EU) 2019/882 를 위한 표준화 요청 C(2022) 6456 에 따라 준비됐고, EU 관보에 인용되면 적합성 추정을 준다고 적는다. | ref-1555 | 아니오 | medium | 2026-10-12 | — | — |
| f26 | [사실] | EN 301 549 V4.1.1 제5.1.5절은 닫힌 기능(closed functionality)을 쓰는 데 청각 출력이 필요하면 그 청각 정보와 동등한 시각 정보를 제공하도록 요구한다. | ref-1555 | 아니오 | medium | 2026-10-12 | — | — |
| f27 | [사실] | EN 301 549 V4.1.1 제5.1.7절은 닫힌 기능을 조작하는 데 음성이 필요하면 음성을 요구하지 않는 대체 입력 방식의 조작 모드를 적어도 하나 제공하도록 요구한다. | ref-1555 | 아니오 | medium | 2026-10-12 | — | — |
| f28 | [사실] | 유럽 접근성법(지침 (EU) 2019/882) 제2조 제1항 (b)는 2025-06-28 이후 출시되는 무인 단말기 가운데 (i) 결제 단말기는 한정 없이 열거하고, (ii) 현금자동인출기·발권기·체크인기·정보 제공 대화형 무인 단말기는 '이 지침이 다루는 서비스 제공 전용'인 것으로 한정한다. | ref-1554 | 아니오 | medium | 2026-10-12 | — | — |
| f29 | [사실] | 같은 지침 제15조 제1항은 EU 관보에 참조가 게재된 조화 표준(또는 그 일부)에 부합하는 제품·서비스가 그 표준이 다루는 범위에서 이 지침의 접근성 요구에 부합하는 것으로 추정된다고 정한다. | ref-1554 | 아니오 | medium | 2026-10-12 | — | — |
| f30 | [추정] | 로봇 본체 터치스크린, 기업용(B2B) 관제 화면, 작업자 HMI 가 지침 2019/882 제2조의 열거 제품·서비스에 드는지는 조문만으로 정해지지 않는다. 결제 기능이 있는 로봇 단말은 (i) 결제 단말기 해당 여부를, 정보 안내 화면은 (ii) 의 '서비스 제공 전용' 요건을 따로 검토해야 하는 것으로 보인다. | ref-1554 | 아니오 | low | 2026-10-12 | — | — |
| f31 | [추정] | axe-core v4.14.0 태그(CHANGELOG 2026-10-05)의 target-size 규칙 정의에는 'wcag22aa'·'wcag258'·'EN-301-549v4'·'EN-9.2.5.8' 태그가 붙어 있고 "enabled": false 로 설정돼 있다. | ref-1557 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f32 | [추정] | enabled:false 이므로 target-size 규칙은 axe-core 기본 실행에서 빠지는 것으로 보이며, EN 301 549 태그를 지정해 실행할 때 이 규칙이 켜지는지는 설정에 달려 있어 실행 시험으로 확인하지 않았다. README 는 자동 판단이 불확실한 항목을 incomplete 로 돌려 수동 검토가 필요하다고 안내한다. | ref-1557 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f33 | [사실] | Choo·Lee 의 Delphi 연구(Healthcare Informatics Research 32(1), 2026-01)는 서울의 한 상급종합병원 신경과 병동 6명과 뇌졸중 집중치료실 8명, 경력 7년 초과 간호사 14명을 전문가 패널로 3라운드 합의를 구했다. | ref-1558 | 아니오 | medium | 2026-10-12 | 병원 | — |
| f34 | [사실] | 이 Delphi 설문은 2022-11-07 부터 2023-04-12 까지 실시됐다. | ref-1558 | 아니오 | medium | 2026-10-12 | 병원 | — |
| f35 | [추정] | Choo·Lee 연구는 급성 뇌졸중 환자 돌봄에 동반 로봇을 쓰는 미래 시나리오에 대한 단일 기관 간호사 14명의 전문가 합의이며, 로봇 도입 뒤 수용률이나 간호 업무 변화를 측정한 연구가 아니다. 따라서 한국 병원 간호사 일반이나 한림대성심병원 자체 설문(ref-1222)의 독립 재현으로 볼 수 없다. | ref-1558 | 아니오 | low | 2026-10-12 | 병원 | — |
| f36 | [사실] | Han 외(CHI 2024)의 이동장애인 15명·로봇 실무자 8명 면담과 짝 공동설계 워크숍은 모두 화상회의로 진행됐다. | ref-1214 | 아니오 | medium | 2026-10-12 | 실외 | — |
| f37 | [사실] | Han 외 저자들은 자신들의 질적 결과와 제안한 상호작용을 실제 환경에서 평가할 필요가 남아 있다고 명시했다. | ref-1214 | 아니오 | medium | 2026-10-12 | 실외 | — |
| f38 | [사실] | Boadi-Agyemang 의 CMU 박사논문(CMU-RI-TR-26-106, 2026-06) 4장의 배송 로봇 공동설계는 2025년 미국 Pittsburgh 에서 2개월간 지역 모집한 장애 성인 14명(여성 9·남성 5, 31~75세, 시각·청각·이동 장애 중심)과 진행했다. | ref-1559 | 아니오 | medium | 2026-10-12 | 실외 | — |
| f39 | [사실] | Boadi-Agyemang 연구 참여자들은 보행 중 로봇과의 통행 우선권과 별개로, 손을 뻗기 어려운 이동장애인이 물품을 인수할 때는 로봇과 가까이 상호작용하는 것이 중요하다고 보았다. | ref-1559 | 아니오 | medium | 2026-10-12 | 실외 / 완료·인계 | — |
| f40 | [추정] | 통행 중 충분한 간격(연석 경사로 비우기)과 물품 인수 때의 근접은 같은 이용자 집단 안에서도 상황별로 다른 요구다. 두 연구 모두 미국 소수 참여자의 요구·설계 연구이고 실제 배송의 접근 성공률을 측정하지 않았으며, 같은 CMU 계열이라 독립 교차 확인으로 세지 않는다. | ref-1214, ref-1559 | 아니오 | low | 2026-10-12 | 실외 | — |
| f41 | [사실] | 위키 8절의 Acemoglu·Restrepo 범위값(노동자 1천 명당 로봇 1대 증가 시 고용인구비율 약 0.18~0.34%p, 임금 0.25~0.5% 감소)은 NBER 작업논문 w23285(2017-03) 초록과 일치하므로 틀린 값이 아니며 유지한다. | ref-1223 | 아니오 | medium | 2026-10-12 | — | — |
| f42 | [사실] | Journal of Political Economy 128(6):2188–2244(2020-06) 게재판은 공간 파급을 반영한 미국 총량 효과로, 노동자 1천 명당 로봇 1대 증가가 고용인구비율을 약 0.2%p, 임금을 약 0.42% 낮춘다고 추정했다. | ref-1560 | 아니오 | medium | 2026-10-12 | — | — |
| f43 | [사실] | 같은 JPE 게재판은 1990~2007년 미국 722개 통근권역 자료에서, 로봇 스톡 증가(1993~2007년 노동자 1천 명당 약 1대)가 로봇 노출이 없는 통근권역 대비 평균 고용인구비율을 0.39%p, 평균 임금을 0.77% 낮췄다고 추정했다(지역 효과). | ref-1560 | 아니오 | medium | 2026-10-12 | — | — |
| f44 | [사실] | Dauth 외(Journal of the European Economic Association 19(6), 2021)는 1994~2014년 독일 행정자료로 같은 추정 전략을 재현했을 때 로봇 노출이 총고용을 줄이는 음(-)의 효과를 찾지 못했고, 제조업 일자리 감소를 서비스업(특히 기업 대상 지역 서비스)의 새 노동 수요가 상쇄했다고 보고했다. | ref-1561 | 아니오 | medium | 2026-10-12 | — | — |
| f45 | [추정] | 미국(1990~2007, 통근권역)과 독일(1994~2014, 402개 지역·행정자료) 결과는 국가·시기·자료·노동 이동 조건이 달라 같은 주장의 재현이나 반박으로 볼 수 없고, 어느 쪽도 한국이나 개별 로봇 플릿 현장의 고용 효과를 측정한 것이 아니다. | ref-1560, ref-1561 | 아니오 | low | 2026-10-12 | — | — |
| f46 | [의견] | ROP 도입 전후 작업자 조사는 수용 의향, 실제 사용, 거부·우회, 도움 요청, 감시 우려를 별도 지표로 나누고, 응답 집단(관리자/비관리 작업자, 로봇 경험 유무)과 표본 조건(국가·언어·모집 방법·조사 시점·공개 동의 분모)을 결과와 함께 기록해야 한다. 해외 척도는 한국어 인지면담과 직군별 타당화를 거친 뒤 문항원으로만 쓴다. | ref-1547, ref-1548, ref-1558 | 아니오 | low | 2026-10-12 | — | — |
| f47 | [의견] | 플릿 도입 효과를 평가할 때는 사고 분류 정의(경작업 전환·휴업 포함 여부), 노출 시간 분모, 직군, 로봇 공정 여부, 전환 작업을 함께 기록하고, 회사 발표와 노조 보고서 같은 이해당사자 자료의 출처를 표시해야 한다. 처리량 증가나 안전감 설문을 실제 부상 감소의 대리값으로 쓰지 않는다. | ref-1549, ref-1550 | 아니오 | low | 2026-10-12 | 물류창고 / 예외·성과 | — |
| f48 | [의견] | ROP 스케줄러의 휴게 반영·작업 순환·직무 전환 정책 변경은 노사협의 기록(근로자참여법 제20조 제6·7호 협의 여부)과 연결해 이력으로 남기고, 작업자 데이터·자동 배정에 대한 이의 제기와 처리 결과를 변경 관리에 묶어야 한다. 법적 해당성 판단은 ROP 가 하지 않고 외부 결정을 제약으로 받는다. | ref-1551, ref-1552 | 아니오 | low | 2026-10-12 | — | — |
| f49 | [의견] | 접근성 시험은 브라우저 관제 화면(WCAG 2.2: 드래그 대체 조작, 24×24 CSS px 대상), 비웹 작업자 프로그램(WCAG2ICT 는 안내일 뿐), 로봇 단말의 닫힌 기능(EN 301 549 5.1.5·5.1.7: 시각 경보 동등성, 음성 외 입력), 로봇 본체 물리 접근으로 범위를 나누고, 자동 검사 보고서에는 도구 버전·규칙 ID·활성화 설정을 남긴 뒤 키보드·스크린리더·실사용자 수동 검사를 더한다. 기술 시험 통과와 법적 적용 판단은 별도 기록으로 둔다. | ref-1553, ref-1556, ref-1555, ref-1554, ref-1557 | 아니오 | low | 2026-10-12 | — | — |
| f50 | [의견] | 플릿 경로·작업 모델은 보도 통행, 대기, 물품 인수 모드를 나누어, 통행·대기 중에는 연석 경사로를 비우고 간격을 두되 인수 때는 접근 가능한 위치·높이·입력 수단과 근접 허용을 작업 배정 조건으로 다뤄야 한다. 근접 허용은 이용자 요청과 현장 안전 평가를 전제로 시험한다. | ref-1214, ref-1559 | 아니오 | low | 2026-10-12 | 실외 / 완료·인계 | — |
| f51 | [의견] | 국가 단위 로봇 노출 계수로 개별 플릿의 감원 인원을 계산하지 말고, 현장 도입 평가에서는 기존 작업자의 직무 전환, 신규 채용, 외주 전환을 구분해 수용성 조사와 함께 기록하는 것이 맞다. | ref-1560, ref-1561 | 아니오 | low | 2026-10-12 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1547 | Liu, Y. (A.), Kaur, G., Banerjee, N. K., Banerjee, S. (Clarkson University·Wright State University) — Data in Brief 61 | Dataset of worker perceptions of workforce robotics regarding safety, independence, job security, and privacy | 2025-06-03 | 논문 | medium | 2026-10-12 | https://doi.org/10.1016/j.dib.2025.111750 | 아니오 |
| ref-1548 | Pinto, A., Lemos, L., Carvalho, C., Santos, J., Menezes, P., Nomura, T. — Human Behavior and Emerging Technologies | Translation, Adaptation, and Validation in Portuguese of an Acceptance Scale for Human–Robot Interaction in an Industrial Context | 2025-01-17 | 논문 | medium | 2026-10-12 | https://doi.org/10.1155/hbe2/8816379 | 아니오 |
| ref-1549 | Amazon (Sarah Rhoads, VP Global Workplace Health & Safety) | Amazon delivers another strong year of safety progress, making our workplaces even safer for our employees | 2026-03-12 | 벤더 문서 | medium | 2026-10-12 | https://www.aboutamazon.com/news/workplace/amazon-workplace-safety-2025-injury-reduction | 아니오 |
| ref-1550 | Strategic Organizing Center (SOC; SEIU·CWA·UFW 연계 노동 조직) | Failure to Deliver: Amazon Falls Short on Safety | 2025-05 | 업계 보고서 | medium | 2026-10-12 | https://thesoc.org/wp-content/uploads/2025/05/May-2025_Strategic-Organizing-Center_Report-x-Failure-To-Deliver.pdf | 아니오 |
| ref-1551 | 법제처 국가법령정보센터 (대한민국, 법률 제18927호) | 근로자참여 및 협력증진에 관한 법률 제20조(협의 사항) [시행 2022. 12. 11.] [법률 제18927호, 2022. 6. 10., 일부개정] | 2022-06-10 | 정부·연구기관 | high | 2026-10-12 | https://law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1017145541 | 아니오 |
| ref-1552 | Doellgast, V., Appalla, S., Ginzburg, D., Kim, J., Thian, W. L. (Cornell University ILR School) — ILO Working Paper 144 | Global case studies of social dialogue on AI and algorithmic management | 2025-07 | 정부·연구기관 | medium | 2026-10-12 | https://doi.org/10.54394/VOQE4924 | 아니오 |
| ref-1553 | W3C Accessibility Guidelines Working Group | Web Content Accessibility Guidelines (WCAG) 2.2 (W3C Recommendation 12 December 2024) | 2024-12-12 | 표준 | high | 2026-10-12 | https://www.w3.org/TR/2024/REC-WCAG22-20241212/ | 아니오 |
| ref-1554 | European Parliament and Council of the European Union (Official Journal L 151) | Directive (EU) 2019/882 of 17 April 2019 on the accessibility requirements for products and services | 2019-06-07 | 정부·연구기관 | high | 2026-10-12 | https://eur-lex.europa.eu/eli/dir/2019/882/oj/eng | 아니오 |
| ref-1555 | ETSI / CEN / CENELEC | EN 301 549 V4.1.1 (2026-09) Accessibility requirements for ICT products and services | 2026-09 | 표준 | high | 2026-10-12 | https://www.etsi.org/deliver/etsi_en/301500_301599/301549/04.01.01_60/en_301549v040101p.pdf | 아니오 |
| ref-1556 | W3C Accessibility Guidelines Working Group (WCAG2ICT Task Force) | Guidance on Applying WCAG 2 to Non-Web Information and Communications Technologies (WCAG2ICT), W3C Group Note 11 December 2025 | 2025-12-11 | 표준 | medium | 2026-10-12 | https://www.w3.org/TR/2025/NOTE-wcag2ict-22-20251211/ | 아니오 |
| ref-1557 | Deque Systems / axe-core contributors | axe-core v4.14.0 (lib/rules/target-size.json, README, CHANGELOG) | 2026-10-05 | 오픈소스 문서 | medium | 2026-10-12 | https://github.com/dequelabs/axe-core/tree/v4.14.0 | 아니오 |
| ref-1558 | Choo, H.-J., Lee, S.-M. (Healthcare Informatics Research 32(1):59–68) | Nurses' Perceptions and Utilization Plans for Applying Companion Robots to Acute Stroke Patient Care: A Delphi Study | 2026-01 | 논문 | medium | 2026-10-12 | https://doi.org/10.4258/hir.2026.32.1.59 | 아니오 |
| ref-1559 | Boadi-Agyemang, A. (Carnegie Mellon University Robotics Institute, CMU-RI-TR-26-106) | From Margin to Center: Designing Inclusive and Equitable Service Robots with Disabled Adults (PhD thesis) | 2026-06 | 논문 | medium | 2026-10-12 | https://publications.ri.cmu.edu/storage/publications/2026/09/aboadiag-dissertation2026-manual-tagged-v2_20260902085808.pdf | 아니오 |
| ref-1560 | Acemoglu, D., Restrepo, P. (Journal of Political Economy 128(6):2188–2244) | Robots and Jobs: Evidence from US Labor Markets (JPE 게재판) | 2020-06 | 논문 | high | 2026-10-12 | https://doi.org/10.1086/705716 | 아니오 |
| ref-1561 | Dauth, W., Findeisen, S., Suedekum, J., Woessner, N. (Journal of the European Economic Association 19(6):3104–3153) | The Adjustment of Labor Markets to Robots | 2021-12 | 논문 | medium | 2026-10-12 | https://doi.org/10.1093/jeea/jvab012 | 아니오 |
| ref-1226 | Malik, M. A. B., Brandão, M., Coopamootoo, K. (International Journal of Social Robotics) | Towards Worker-Centered Warehouse Robots: A User Study on Privacy, Inclusivity and Safety | 2026-02-13 | 논문 | medium | 2026-10-12 | https://doi.org/10.1007/s12369-026-01359-1 | 예 |
| ref-1214 | Han, H. Z. 외 (Carnegie Mellon University) — CHI '24 | Co-design Accessible Public Robots: Insights from People with Mobility Disability, Robotic Practitioners and Their Collaborations | 2024-04-07 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2404.05050 | 아니오 |
| ref-1223 | Acemoglu, D., Restrepo, P. (NBER) | Robots and Jobs: Evidence from US Labor Markets | 2017-03 | 논문 | medium | 2026-10-12 | https://www.nber.org/papers/w23285 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/governance-law-and-society/labor-acceptance-and-accessibility.md | 4, 5, 6, 7, 8, 9, 11 | 갱신(차등): 섹션 4(분리 2026-09-30-area60-s4) — '노사협의회 협의 사항'(39행)을 2022-12-11 시행 법률 제18927호 판(ref-1551)으로 근거 갱신하고(f17: 제2·9·14호 문구 동일, 제1항 개정 표시 2019-04-16), 제6호 고용조정 일반원칙(f16)·제7호 작업과 휴게 시간의 운용(f15)을 추가. '공개 작업자 설문 데이터' 항목으로 Liu 외 표본 조건(f1~f3)과 일반화 한계(f4) 추가 / 섹션 5 — 물류창고: 74행 Malik 면담 문장은 유지하고 참여자 국가·역할·로봇 경험은 덧붙이지 않음(f5 [추정], 메모 F04 '영국'·F05·F06 확인 불가). 예외·성과 칸 아래 본문에 SOC 보고서의 자료 기간(f10)·중대 부상 정의(f11)·Amazon NAICS 493110 자체 시설 456곳 대 비Amazon 창고 비교(f12, 메모 '비교창고 456시설' 정정)와 SOC 의 노조 연계 이해당사자 성격(f13), Amazon 자사 발표 43%·70%(f9 벤더 주장 [추정])를 넣고 둘을 교차 확인으로 세지 않음(f14). 병원: Choo·Lee Delphi(서울 단일 상급종합병원 간호사 14명, 2022-11~2023-04, f33·f34)를 사례 보충으로 넣되 도입 후 효과가 아니며 한림대 설문의 재현이 아님(f35). 실외: Han 외 활동이 모두 화상회의(f36)·실환경 평가 필요(f37), Boadi-Agyemang Pittsburgh 14명(f38)·물품 인수 근접 요구(f39)와 통행 간격과의 상황 차이(f40) / 섹션 6(분리 2026-09-30-area60-s6) — '수용성 측정 모델'에 FSQ-IC(f6~f8: 포르투갈 일반 성인 편의·눈덩이 표본, 무경험자 다수, 원문 표본 수 불일치)를 표본 조건과 함께 추가, 한국 일반화 금지. '노동자 참여 절차'의 '법률 제16320호, 2019-07-17 시행 기준'을 제18927호 판으로 갱신(f17)하고 ILO WP144 IBM 독일 AI 윤리위원회(f19, Cornell ILR 저자 견해이며 ILO 공식 아님 f20), 조문 적용 해석 미확인(f18); 의견 f46·f48 / 섹션 7(분리 2026-09-30-area60-s7) — 근로자참여법 행(43행) '법률 제16320호, 현행 조문 여부 미확인'을 2022-12-11 시행 법률 제18927호 열람판으로 갱신하고 제6·7호 추가(f15~f17). 새 행: WCAG 2.2 SC 2.5.7·2.5.8(f21·f22), WCAG2ICT 정보성 안내·하드웨어 제외(f23·f24), EN 301 549 V4.1.1 최종판·관보 인용 시 적합성 추정·5.1.5·5.1.7(f25~f27, 관보 인용 여부 미확인), 지침 (EU) 2019/882 제2조(1)(b) — (i) 결제 단말기는 '서비스 제공 전용' 한정이 없고 (ii) 단말기만 한정(f28), 제15조(1)(f29), 해당성 판단 유보(f30), axe-core v4.14.0 target-size 태그·enabled:false(f31)와 수동 검토(f32) — 벤더(Deque) 저장소 단독이라 [추정]·벤더 주장; 의견 f49. 무인정보단말기 소규모 시설 대체 이행(메모 F38)은 기존 내용 확인(2026-09-30-area60-s7.md 표 2행, ref-1217; chat-based-configuration-and-operation/index.md 124행)이라 새로 넣지 않음 / 섹션 8(분리 2026-09-30-area60-s8) — Acemoglu·Restrepo 항목(40행)의 0.18~0.34%p·0.25~0.5% 는 NBER 초록과 일치해 유지(f41)하고, JPE 2020 게재판 총량 효과 -0.2%p·-0.42%(f42)와 722개 통근권역 지역 효과 -0.39%p·-0.77%(f43)를 새 출처 ref-1560 으로 덧붙임. Dauth 외 독일 비교(f44)와 재현 아님(f45) 추가; 의견 f51. 새 수용성 연구 항목(Liu 외, FSQ-IC, Choo·Lee, Boadi-Agyemang)은 표본 조건을 문장에 넣고 어느 것도 한국 산업 현장 측정이 아님을 명시. 3절(분리 s3) 42행 '2017-03 작업논문' 문장은 유지(후속 정리 시 JPE 총량값 병기 검토) / 섹션 9 — 상위 업무 시스템 행: 휴게·작업 순환·직무 전환 정책을 노사협의 기록과 연결(f15·f16·f48). 업종별 조건 행: 화면 접근성을 웹 관제·비웹 HMI·로봇 단말 닫힌 기능·물리 접근으로 나누고 법적 적용 판단은 외부 연계(f21~f32·f49), 통행/대기/인수 모드 구분(f39·f50) / 섹션 11(분리 2026-09-30-area60-s11) — 해결 제안 없음. 부분 근거: oq-285(f15~f20), oq-286(f10~f14), oq-287(f33~f35), oq-284(f28~f30, 국내 장애인차별금지법 해당성은 미확인), oq-188(f36~f40, 국내 기준 미확인), oq-266(f19, 운영 소유권 비교 연구 아님). 답하지 못함: oq-146(EN 301 549 5.1.7 은 음성 대체 입력 요구일 뿐 한국어 인식률 자료 아님), oq-278(NCS 미확인). 다른 영역 페이지의 같은 근거(근로자참여법 제20조 ref-1220 '법률 제16320호' 표기: field-operations-and-monitoring/index.md 210·268행, 2026-09-30-area60-s10.md)는 후속 정리 필요(이번에 고치지 않음). 감시 관련 CNIL Amazon France 과징금(ref-1267, security-and-privacy/index.md)·oq-321 과 oq-285 연결은 참고만. |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- 출처 충돌: FSQ-IC 포르투갈어판 검증 연구의 총 표본 346명과 두 분석 표본(EFA 140명 + CFA 210명 = 350명)이 맞지 않는 이유는 무엇이며, 어느 수가 실제 분석에 쓰였는가? | 관련 영역: 60. 노동·수용성·접근성 | 근거: f7 | 종류: 출처 충돌
- Burtch·Greenwood·Ravindran(ILR Review 2025) 원논문의 표본 시설·기간·추정식·강건성 검정은 무엇이며, 로봇 센터의 중대 부상 40% 감소·비중대 부상 77% 증가는 원논문에서 어떤 조건의 추정치인가? | 관련 영역: 60. 노동·수용성·접근성, 61. 물류창고, 49. 사람 근접 안전 | 근거: f14 | 종류: 일반
- 알메러 모델·FSQ-IC 같은 수용성 척도를 한국어로 옮겨 국내 산업 현장 작업자(물류창고·제조·병원 직군)에게 타당화한 연구가 있는가? | 관련 영역: 60. 노동·수용성·접근성, 56. 운영 이관·확대·교육 | 근거: f8 | 종류: 일반
- EN 301 549 V4.1.1(2026-09)은 지침 (EU) 2019/882 의 조화 표준으로 EU 관보에 인용됐는가, 인용됐다면 언제부터 어떤 범위에서 적합성 추정을 주는가? | 관련 영역: 60. 노동·수용성·접근성, 59. 법·규제·보험·라이선스 | 근거: f25 | 종류: 일반
- 한림대성심병원 의료서비스로봇 만족도 조사의 원 분모(간호사 109명 대 99명)·문항·조사 시점을 밝힌 병원 원보고서가 공개돼 있는가? | 관련 영역: 60. 노동·수용성·접근성, 63. 병원·의료 | 근거: f35 | 종류: 출처 충돌
- 한국노동연구원 『기술 혁신과 노동시장 변화』(2024-12)의 로봇 노출도별 임금·고용 수치(고숙련 +2.5%·+0.55%p, 저숙련 -4.5~4.9%)의 원표와 식별 조건은 무엇인가? | 관련 영역: 60. 노동·수용성·접근성, 3. 경제성·조달·사업 모델 | 근거: f45 | 종류: 일반
- Han 외(CHI 2024) 공동설계 연구 참여자의 거주 국가와 지역은 본문 어디에 명시돼 있는가? | 관련 영역: 60. 노동·수용성·접근성, 66. 실외 | 근거: f36 | 종류: 일반
- 접근성 요구가 서로 다른 이기종 로봇(배송·안내·병원 물류)의 작업 배정과 물품 인수 완료를 실제 이용자와 현장에서 검증하는 공개 시험 세트나 시나리오가 있는가? | 관련 영역: 60. 노동·수용성·접근성, 25. 작업 배정 — MRTA, 54. 시험·형식 검증·벤치마크 | 근거: f40 | 종류: 일반
- 이용자의 장애 관련 접근 요구(인수 높이·근접 허용·입력 수단)를 플릿에 전달할 때 필요한 최소 정보 항목과 동의·보존·삭제 절차를 정한 운영 규약이나 검증 사례가 있는가? | 관련 영역: 60. 노동·수용성·접근성, 53. 개인정보·영상 데이터 | 근거: f39 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 18 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 15건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-12-03/external_research.md)를 변환했다. 2026-10-12 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.
    - f5: Malik 외(ref-1226) 원문은 Springer·KCL 저장소 모두 Cloudflare 차단으로 열지 못함. 초록의 N=12 반구조화 면담만 확인. 메모 F04 의 '영국 창고 경험', F05(비관리 5/관리·리더 7), F06(로봇 경험 7명)은 확인 불가라 사실로 쓰지 않음
    - f7: FSQ-IC 원문의 346 vs 140+210=350 불일치 원인 미확인
    - f15~f17: 근로자참여법 제20조는 2026-10-12 국가법령정보센터 조문 링크로 열람한 판(시행 2022-12-11, 법률 제18927호) 기준. 열람 이후 개정 여부와 ROP 로그·배정 정책의 협의 대상 해당성(판례·행정해석)은 확인 못 함
    - f19·f20: ILO WP144 발행일 2025-07-10 은 확인 불가(PDF 표지 July/2025). IBM 면담 날짜가 각주 206(2021-11-08)과 부록 1(2024-07-26)에서 다름. IBM 협약 원문 미확보
    - f25: EN 301 549 V4.1.1 의 EU 관보 인용 여부 미확인
    - f31·f32: axe-core target-size 규칙을 실제로 실행해 enabled:false 와 태그 지정 실행의 동작을 시험하지 않음. README 의 57% 자동 검출 주장은 독립 재현 없음이라 쓰지 않음
    - f42: JPE 게재판 온라인 게재일 2020-04-22 확인 불가(권호 2020-06 만 사용). f44: Dauth 외는 저자 2021-01-21판으로 읽었고 출판 최종판과의 완전 동일성 미확인
    - f9: Amazon 발표의 지표 정의·노출 분모·로봇 센터 분리 수치 미확인(벤더 주장). 위키 Burtch 외 40%/77%(ref-1213)는 원논문 미열람 상태 그대로
    - 예산(신규 출처 15)에 맞추려고 메모 n4(Bartneck, Godspeed Questionnaire Series — 지각된 안전성 문항이 응답자 정서 상태를 묻고 Elena Knox 한국어 번역 제공, 메모 F10·F11)와 n14(W3C WAI, Selecting Web Accessibility Evaluation Tools — 'Human judgement is required', 메모 F28)는 검증에서 확인됐으나 출처에서 뺐다(후속 실행에서 추가 가능)
    - oq-146(한국어 음성 인식률), oq-278(로봇 관제 NCS)은 이번 메모가 답하지 못함. oq-188 국내 점자블록·연석 대기 위치 기준, oq-284 로봇 단말의 장애인차별금지법상 무인정보단말기 해당성은 미확인
- 범위 경계 위반 의심:
    - f15~f20·f28~f30: 근로자참여법·유럽 접근성법의 법적 해당성 해석은 59. 법·규제·보험·라이선스 쪽 판단이므로 조문이 말하는 범위까지만 쓰고 개별 ROP 기능의 적용 여부는 판단하지 않음
    - f21~f32: 웹·비웹 화면 접근성 기준은 37. 관제 화면·실행 기록, 13. 대화형 기능의 신뢰·기반과 겹치며, 이 영역에는 이용자·작업자 접근성 관점으로만 씀
    - f9~f14: 창고 부상 지표는 49. 사람 근접 안전, 39. 운영 성과 측정·개선과 겹치며, 이 영역에는 노동 영향·이해당사자 자료 해석 관점으로만 씀
- 한계: 외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 15건/15(ref-1547~ref-1561, 예약 구간 ref-1547~ref-1576 안), 재사용 3건(ref-1226·ref-1214·ref-1223). 출처 매핑(검증 결과 기준): 메모 n1→ref-1547, n2→ref-1226(미열람), n3→ref-1548, n4→예산 때문에 제외, n5→ref-1549(벤더 문서), n6→ref-1550, n7→ref-1551(2022판 새 출처; ref-1220 은 케이스노트 2019판이라 그대로 두고 비교에만 씀), n8→ref-1552, n9→ref-1553, n10→ref-1554, n11→ref-1555, n12→ref-1556, n13→ref-1557(github raw, v4.14.0 태그), n14→예산 때문에 제외, n15→ref-1558, n16→ref-1214(arXiv v1 HTML 재열람), n17→ref-1559, n18→ref-1560(JPE 게재판, NBER ref-1223 과 별도), n19→ref-1561, n20→ref-1217(메모 F38 중복이라 finding 없음, 출처에서 뺌). 추가 재사용: ref-1223(NBER 초록 재열람, 범위값 유지 근거). fetched: false 는 ref-1226. 교차 확인 0건(모든 사실 finding 이 단일 출처이거나 같은 계열: W3C 문서끼리, Han·Boadi 는 CMU 계열, Amazon·SOC 는 같은 OSHA 신고 자료 기초, Acemoglu·Dauth 는 IFR 자료·추정 전략 공유) — 단일 출처라 법령·표준 원문도 신뢰도 medium(validate 상한 규칙과 같음), 해석·벤더 finding 은 low. 중복 제거: 메모 F38(무인정보단말기 소규모 시설 대체 이행)은 2026-09-30-area60-s7.md 표·ref-1217·chat-based-configuration-and-operation/index.md 124행에 이미 있어 넣지 않음. 제20조 제2·9·14호, Han 15/8/4 숫자, 연석 경사로 사례도 기존 내용이라 재추가하지 않음. 검증 반영: F04 '영국'·F05·F06 확인 불가 → 사실 금지(f5 [추정]); A05 '비교창고 456시설' → Amazon NAICS 493110 자체 시설 456곳(f12), SOC 이해당사자 명시(f13); A06 근거 판을 2022-12-11 시행 법률 제18927호로(f15~f17); A07 ILO WP144 는 Cornell ILR 저자 견해이며 ILO 공식 아님(f19·f20); A11 (i) 결제 단말기에는 '서비스 제공 전용' 한정 없음 명시(f28); A12 axe-core 설정은 [추정]·벤더 주장(f31·f32); A15 는 Acemoglu 2017 범위값 유지(f41)와 JPE 2020 총량·지역 값 추가(f42·f43, 새 ref-1560); FSQ-IC 저자 6인으로 정정; 모든 수용성 연구는 표본 조건을 문장에 넣고 한국 일반화를 하지 않음(f4·f8·f35·f40·f45). 열린 질문: 해결 제안 없음(기존 질문 8개 모두 부분 답 또는 미답). 메모 new-1~4 는 기존 oq-284~oq-287 과 같은 질문이라 새로 만들지 않음(open-questions.md 306~309행 문구 대조). oq-146 은 페이지와 open-questions.md(168행)의 꼬리 문구만 다르고 같은 질문. 새 질문 9건(메모 U09~U17, 기존 질문과 겹침 없음 확인). 메모의 '.research-work' 로컬 경로·행 번호는 쓰지 않고 원문 절·쪽·조와 위키 실제 위치를 적었다. 정정 요청 없음. 용어 후보 없음.
```

### runs/2026-09-30-07/research.md

```markdown
# 리서치 브리프 2026-09-30-07

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-07 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 44. 로봇 기반 모델·언어 모델 계획 |
| 대분류 | L. AI·학습 기술 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 로봇 기반 모델, 교차 형태 학습, 행동 토큰화, LLM-모듈로, 불확실도 정렬 연결 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 가정·제조 공장·물류창고 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 시각–언어–행동 모델, 언어 모델 계획과 기호 계획기 결합, 다중 로봇 계획, 불확실도 기반 도움 요청 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — Open X-Embodiment, OpenVLA, GR00T N1, ROSA 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 0건
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 범용 로봇 모델과 언어 모델은 오케스트레이션의 무엇을 바꾸는가? [분류원문]
2. 시각–언어–행동(Vision-Language-Action, VLA) 모델과 로봇 기반 모델은 무엇이며 어떤 데이터·구조로 여러 로봇·작업에 일반화하는가? (섹션 4·6·8 겨냥)
3. 대규모 언어 모델(LLM)로 작업을 계획·분해할 때의 한계는 무엇이고, 기호 계획기·외부 검증기·불확실도 기반 도움 요청으로 어떻게 보완하는가? (섹션 3·6·8 겨냥)
4. 언어 모델로 여러 로봇의 작업 분해·연합 형성·배정을 계획하는 연구와 공개 오픈소스(ROS 연동 에이전트 포함)는 무엇인가? (섹션 6·7 겨냥)
5. 가정·제조 공장·물류창고 등 현장(국내 포함)에서 로봇 기반 모델을 적용한 사례와 그 조건·성과는 무엇인가? (섹션 5 겨냥, 한국 자료 우선)
6. 로봇 기반 모델·언어 모델 계획에서 ROP가 직접 맡을 것과 로봇 제조사·모델 제공자에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Brohan 외의 RT-2(arXiv 2307.15818, 2023-07)는 로봇 행동을 텍스트 토큰으로 표현해 자연어 토큰과 같은 방식으로 학습 데이터에 넣고, 시각–언어 모델을 로봇 궤적 데이터와 웹 시각 질의응답 과제에 함께 미세조정한 시각–언어–행동(VLA) 모델로, 6,000회 평가에서 새 물체·학습에 없던 명령에 대한 일반화가 좋아졌다고 보고했다. | ref-1045 | 아니오 | medium | 2023-07 | — | — |
| f2 | [사실] | Open X-Embodiment 협력단(arXiv 2310.08864, 2023-10)은 21개 기관이 모은 22종 로봇의 데이터(527개 스킬, 160,266개 작업)를 표준 형식으로 공개하고, 이 데이터로 학습한 RT-X 모델이 다른 로봇의 경험을 활용해 여러 로봇의 능력을 높이는 긍정적 전이를 보였다고 보고했다. | ref-1048 | 아니오 | medium | 2023-10 | — | — |
| f3 | [사실] | Kim 외의 OpenVLA(arXiv 2406.09246, 2024-06)는 Llama 2 에 DINOv2·SigLIP 시각 특징을 결합한 70억 매개변수 공개 VLA 모델로 실제 로봇 시연 97만 건으로 학습했고, 29개 작업에서 매개변수가 7배 많은 RT-2-X(550억)보다 절대 성공률이 16.5%p 높았으며, 모델 체크포인트·미세조정 노트북·PyTorch 코드를 공개했다. | ref-1046 | 아니오 | medium | 2024-06 | — | — |
| f4 | [사실] | Physical Intelligence 의 π0.5(arXiv 2504.16054, 2025-04)는 여러 로봇의 데이터·고수준 의미 예측·웹 데이터 등 이질적 과제를 함께 학습(co-training)해, 처음 보는 가정집에서 부엌·침실 정리 같은 장기·정교한 조작 작업을 수행했다고 보고했다. | ref-1047 | 아니오 | medium | 2025-04 | 가정 / 작업 대상 | — |
| f5 | [사실] | NVIDIA 의 GR00T N1(arXiv 2503.14734, 2025-03)은 환경을 해석하는 시각–언어 모듈(System 2)과 실시간 운동 명령을 만드는 확산 트랜스포머(System 1)를 나눈 이중 시스템 구조의 공개 휴머노이드용 VLA 모델로, 실제 로봇 궤적·사람 영상·합성 데이터를 섞어 학습하고 Fourier GR-1 휴머노이드의 양손 조작에 배치했다고 보고했다. | ref-1054 | 아니오 | medium | 2025-03 | — | — |
| f6 | [사실] | Ahn 외의 SayCan(arXiv 2204.01691, 2022-04)은 언어 모델이 긴 추상적 지시를 수행하는 절차 지식을 제공하고, 로봇이 미리 학습한 스킬의 가치 함수가 현재 물리 환경에서 그 스킬이 실행 가능한 정도를 제공해 둘을 결합하는 방식으로 언어 모델 계획을 로봇 능력에 접지(grounding)했으며, 모바일 매니퓰레이터로 실험했다. | ref-088 | 아니오 | medium | 2022-04 | — | — |
| f7 | [사실] | Liu 외의 LLM+P(arXiv 2304.11477, 2023-04)는 자연어 문제 설명을 언어 모델로 PDDL(계획 도메인 정의 언어) 문제로 바꾸고 고전 계획기로 해를 찾은 뒤 다시 자연어로 옮기는 3단계 방식으로, 대부분의 벤치마크 문제에서 최적해를 낸 반면 언어 모델 단독은 대부분 실행 가능한 계획조차 내지 못했다고 보고했다. | ref-092 | 아니오 | medium | 2023-04 | — | — |
| f8 | [의견] | Kambhampati 외(ICML 2024, arXiv 2402.01817)는 자기회귀 언어 모델이 스스로 계획하거나 자기 검증할 수 없다고 보고, 언어 모델을 근사적 지식원으로 두고 외부 기호 검증기와 양방향으로 상호작용하게 하는 LLM-모듈로(LLM-Modulo) 프레임워크를 제안했다. | ref-586 | 아니오 | medium | 2024-06 | — | — |
| f9 | [사실] | Ren 외의 KnowNo(CoRL 2023, arXiv 2307.01928)는 언어 모델 계획기가 확신에 찬 환각 예측을 내는 문제에 대해 등각 예측으로 불확실도를 측정해, 공간·수량·선호·언어 모호성이 있을 때 사람에게 도움을 요청하게 하고 사람 도움을 최소화하면서 작업 완료에 통계적 보장을 주며, 모델 미세조정이 필요 없다고 보고했다. | ref-351 | 아니오 | medium | 2023-07 | 예외·성과 | — |
| f10 | [사실] | Kannan·Venkatesh·Min 의 SMART-LLM(arXiv 2309.10062, IROS 2024 투고)은 프로그램 형식의 퓨샷 프롬프트로 언어 모델이 고수준 지시를 작업 분해·연합 형성·작업 배정의 세 단계로 다중 로봇 계획으로 바꾸게 하고, 복잡도가 다른 네 범주의 지시로 된 벤치마크를 만들어 시뮬레이션과 실제 로봇으로 시험했다. | ref-090 | 아니오 | medium | 2023-09 | — | — |
| f11 | [사실] | Su 외의 IMR-LLM(arXiv 2603.02669, 2026-03)은 가정용보다 제약이 엄격한 산업 다중 로봇 생산 작업을 대상으로, 언어 모델이 선택 그래프(disjunctive graph) 구성을 돕고 결정적 풀이 방법으로 실행 가능한 고수준 계획을 얻은 뒤 공정 트리를 따라 실행 가능한 저수준 프로그램을 생성하게 했으며, 세 난이도의 벤치마크 IMR-Bench 로 평가했다(초록에는 실제 공장 배치가 적혀 있지 않다). | ref-170 | 아니오 | medium | 2026-03 | 제조 공장 / 제약 | — |
| f12 | [사실] | NASA 제트추진연구소(JPL)가 관리하는 오픈소스 ROSA(ROS Agent)는 LangChain 위에 만든 에이전트로, ROS 1(Noetic)과 ROS 2(Humble·Iron·Jazzy) 기반 로봇 시스템에 자연어로 질의하고 명령하게 한다. | ref-171 | 아니오 | medium | 2026-09-30 | — | — |
| f13 | [추정] | BMW 그룹은 2025년 스파턴버그 공장에 Figure AI 의 휴머노이드 Figure 02 를 11개월 동안 배치해 용접 공정용 판금 부품 투입을 맡겼고, 이 로봇이 BMW X3 3만 대 이상의 생산을 도왔다고 밝힌다. | ref-1058 | 아니오 | low | 2026-06-25 | 제조 공장 / 예외·성과 | 벤더 주장 |
| f14 | [추정] | 같은 BMW 그룹 자료는 후속 Figure 03 이 스파턴버그 공장에서 대용량 용기에 섞여 들어온 부품을 집어 순서 대차(sequencing trolley)에 정리하고, 대차가 자동화 시스템으로 조립 공정에 운반되는 순서 공급(just in sequence) 물류 작업을 맡으며, 음성 대화 기능과 무선 충전을 갖췄다고 밝힌다. | ref-1058 | 아니오 | low | 2026-06-25 | 제조 공장 / 완료·인계 | 벤더 주장 |
| f15 | [사실] | 지디넷코리아 보도(2025-05-01)에 따르면 2025-04-10 출범한 산업통상자원부 주도 K-휴머노이드 연합에서 레인보우로보틱스·에이로봇·홀리데이로보틱스·로보티즈·로브로스 5개 로봇기업이 개발 중인 휴머노이드를 서울대 AI연구원에 제공해 로봇 AI 파운데이션 모델 개발을 지원하기로 했다. | ref-1057 | 아니오 | low | 2025-05-01 | — | — |
| f16 | [추정] | 헬로티 보도(2025-11-26)에 따르면 로보티즈는 산업통상부 과제 'AI 파운데이션 모델 기반 유통 공정 특화 휴머노이드 로봇 개발'(정부 출연금 약 60억 원)로 VLA 모델을 넣은 상체형 휴머노이드 AI 워커를 BGF로지스 물류센터에 투입해 입·출고, 오발주 재분류, 비정형 상품 분류, 반품 처리 작업을 수행하게 한다. | ref-1059 | 아니오 | low | 2025-11-26 | 물류창고 / 작업 대상 | 벤더 주장 |
| f17 | [추정] | 같은 보도에 따르면 이 과제는 물류센터 핵심 공정 자동화율 80% 이상과 오발주 재분류·피킹 작업 성공률 90% 이상을 목표로 한다(달성 결과가 아니라 목표치다). | ref-1059 | 아니오 | low | 2025-11-26 | 물류창고 / 예외·성과 | 벤더 주장 |
| f18 | [추정] | 확인한 자료를 종합하면 핵심 질문(범용 로봇 모델과 언어 모델이 오케스트레이션의 무엇을 바꾸는가)에 대해, 로봇 기반 모델은 로봇 쪽 기능을 고정된 스킬 목록에서 새 물체·지시에 일반화하는 학습된 정책으로 바꾸고(f1~f5), 언어 모델은 지시 해석·작업 분해·다중 로봇 배정의 입력 방식을 바꾸지만(f6·f10·f11), 언어 모델 단독 계획은 실행 가능성·검증이 약해 기호 계획기·외부 검증기·불확실도 기반 사람 확인과 짝지어 쓰는 형태가 연구의 공통 방향으로 보인다(f7·f8·f9). | ref-1045, ref-1048, ref-1046, ref-1047, ref-1054, ref-088, ref-090, ref-170, ref-092, ref-586, ref-351 | 아니오 | low | 2026-09-30 | — | — |
| f19 | [추정] | 확인한 자료를 종합하면 이 영역이 중요한 까닭은, 여러 로봇의 데이터를 모아 하나의 정책을 학습하는 흐름(f2·f3)이 이종 로봇의 능력 표현과 등록 방식에 영향을 주고, 언어 모델 계획이 확신에 찬 오류를 낼 수 있어(f8·f9) 대화로 받은 지시를 실행 전에 검증할 장치가 필요하며, 제조 공장·물류창고에서 휴머노이드·VLA 적용이 시작됐다고 발표되고 있기 때문이다(f13·f16). | ref-1048, ref-1046, ref-586, ref-351, ref-1058, ref-1059 | 아니오 | low | 2026-09-30 | — | — |
| f20 | [추정] | 확인한 자료를 종합하면 44. 로봇 기반 모델·언어 모델 계획에서 ROP 가 직접 맡을 범위는 언어 모델이 만든 작업 분해·배정 계획을 기호 계획기·제약 검사로 검증하는 계층(f7·f8·f11), 불확실할 때 사람에게 확인을 요청하는 절차(f9), 로봇 기반 모델을 탑재한 로봇을 포함한 이종 로봇에 계획을 내리는 인터페이스(f6·f10·f12)다. | ref-092, ref-586, ref-170, ref-351, ref-088, ref-090, ref-171 | 아니오 | low | 2026-09-30 | — | — |
| f21 | [추정] | 연계 대상: 분류 원문 19장 기준으로 VLA·로봇 기반 모델이 카메라 영상에서 관절·그리퍼 행동을 직접 생성하는 저수준 조작 정책(f1·f3·f4·f5)은 로봇 자체 지능·제어(파지·모터·관절 제어)에 속하므로 로봇 제조사·모델 제공자가 맡고, 이종 제조사를 잇는 ROP 는 그런 로봇의 가능한 기능·실행 조건·완료·실패 확인을 받는 인터페이스를 맡을 것으로 보인다. | ref-1045, ref-1046, ref-1047, ref-1054 | 아니오 | low | 2026-09-30 | — | — |
| f22 | [추정] | 이 영역은 학습된 범용 기능을 표현해야 하는 5. 로봇 능력·작업 표현과 4. 이기종 로봇 등록(f2·f3), 언어 모델 계획을 대화로 부르는 12. 채팅으로 업무 지시·오케스트레이션과 13. 대화형 기능의 신뢰·기반(f9·f12), 작업 분해의 24. 작업·워크플로 모델링(f7·f11), 연합 형성·배정의 25. 작업 배정 — MRTA(f10), 공정 순서의 26. 작업 순서·스케줄링(f11), 계획 검증의 29. 명령·작업 실행의 신뢰성과 54. 시험·형식 검증·벤치마크(f7·f8·f11), 사람 확인의 31. 사람–로봇 협업(f9), 실행 기준의 47. AI·학습·적응과 모델 운영(f8·f9), 업체 동향의 1. 기술·시장·업체 동향(f13·f15·f16), 적용 현장인 61. 물류창고(f16)·62. 제조 공장(f11·f13)·65. 가정·공동주택(f4)과 이어진다. | ref-1048, ref-1046, ref-351, ref-171, ref-092, ref-170, ref-090, ref-586, ref-1058, ref-1057, ref-1059, ref-1047 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1045 | Brohan, A., Brown, N. 외 (Google DeepMind, arXiv) | RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | 2023-07-28 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2307.15818 | 아니오 |
| ref-1046 | Kim, M. J., Pertsch, K., Karamcheti, S. 외 (arXiv) | OpenVLA: An Open-Source Vision-Language-Action Model | 2024-06-13 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2406.09246 | 아니오 |
| ref-1047 | Physical Intelligence (Black, K., Finn, C., Levine, S. 외, arXiv) | π0.5: a Vision-Language-Action Model with Open-World Generalization | 2025-04-22 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2504.16054 | 아니오 |
| ref-1048 | Open X-Embodiment Collaboration (arXiv) | Open X-Embodiment: Robotic Learning Datasets and RT-X Models | 2023-10-13 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2310.08864 | 아니오 |
| ref-088 | Ahn, M., Brohan, A., Brown, N. 외 (arXiv) | Do As I Can, Not As I Say: Grounding Language in Robotic Affordances | 2022-04-04 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2204.01691 | 아니오 |
| ref-092 | Liu, B., Jiang, Y., Zhang, X. 외 (arXiv) | LLM+P: Empowering Large Language Models with Optimal Planning Proficiency | 2023-04-22 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2304.11477 | 아니오 |
| ref-586 | Kambhampati, S., Valmeekam, K., Guan, L. 외 (ICML 2024, arXiv) | LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks | 2024-02-02 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2402.01817 | 아니오 |
| ref-090 | Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. (arXiv) | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models | 2023-09-18 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2309.10062 | 아니오 |
| ref-351 | Ren, A. Z., Dixit, A., Bodrova, A. 외 (CoRL 2023, arXiv) | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners | 2023-07-04 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2307.01928 | 아니오 |
| ref-1054 | NVIDIA (Bjorck, J., Castañeda, F. 외, arXiv) | GR00T N1: An Open Foundation Model for Generalist Humanoid Robots | 2025-03-18 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2503.14734 | 아니오 |
| ref-170 | Su, X., Xu, J., van Kaick, O., Xu, K., & Hu, R. (arXiv) | IMR-LLM: Industrial Multi-Robot Task Planning and Program Generation using Large Language Models | 2026-03-03 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2603.02669 | 아니오 |
| ref-171 | NASA Jet Propulsion Laboratory (nasa-jpl) | ROSA — README | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/nasa-jpl/rosa | 아니오 |
| ref-1057 | 지디넷코리아 | K-휴머노이드 연합, 출범 3주 만에 협약 4건 성과 | 2025-05-01 | 기사 | low | 2026-09-30 | https://zdnet.co.kr/view/?no=20250501140356 | 아니오 |
| ref-1058 | BMW Group | BMW Group advances the use of Physical AI in production with Figure 03 project in Spartanburg | 2026-06-25 | 벤더 문서 | medium | 2026-09-30 | https://www.press.bmwgroup.com/global/article/detail/T0458778EN/bmw-group-advances-the-use-of-physical-ai-in-production-with-figure-03-project-in-spartanburg?language=en | 아니오 |
| ref-1059 | 헬로티 | VLA 이식한 로보티즈 'AI 워커', 물류 현장 난제 해결사로 전격 투입 | 2025-11-26 | 기사 | low | 2026-09-30 | https://www.hellot.net/news/article.html?no=107567 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f19(왜 중요한가), f18(핵심 질문 답, 추정) / 섹션 4: VLA·행동 토큰화 f1, 교차 형태 학습 f2, 이중 시스템 구조 f5, 접지 f6, LLM-모듈로 f8, 불확실도 정렬 f9 / 섹션 5: 가정 — f4, 제조 공장 — f11(벤치마크 한정)·f13·f14(벤더 주장 병기), 물류창고 — f16·f17(국내, 벤더 주장·목표치 병기). 병원·상업 시설·실외 사례는 찾지 못함을 명시 / 섹션 6: 로봇 기반 모델 f1~f5, 언어 모델 계획과 기호 계획기·검증기 결합 f6~f8, 다중 로봇 계획 f10·f11, 불확실도 기반 도움 요청 f9 / 섹션 7: Open X-Embodiment f2, OpenVLA f3, GR00T N1 f5, ROSA f12, PDDL f7 / 섹션 8: f1~f11, 국내 동향 f15 / 섹션 9: f20(직접 범위), f21(연계 대상) / 섹션 10: f22 — 1, 4, 5, 12, 13, 24, 25, 26, 29, 31, 47, 54, 61, 62, 65 / 섹션 11: open_questions_new 3건. 다음 실행 후보: 12. 채팅으로 업무 지시·오케스트레이션 페이지에 f7~f9 반영, 25. 작업 배정 — MRTA 페이지에 f10 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 로봇 기반 모델 | Robot Foundation Model | 여러 로봇·작업·환경의 대규모 데이터로 사전 학습해 새 작업·물체·로봇에 미세조정하거나 바로 쓸 수 있게 한 범용 로봇 모델로, 시각–언어–행동 모델이 대표적이다. |
| 교차 형태 학습 | Cross-embodiment Learning | 형태·센서·구동 방식이 다른 여러 로봇의 데이터를 함께 학습해 한 로봇의 경험이 다른 로봇의 성능을 높이게 하는 학습 방식이다. |
| 이중 시스템 구조 | Dual-system Architecture (System 1 / System 2) | 느린 시각–언어 추론 모듈(System 2)이 상황을 해석하고 빠른 행동 생성 모듈(System 1)이 실시간 운동 명령을 만드는 로봇 기반 모델 구조다. |

## 열린 질문

새로 생긴 질문:

- 로봇 기반 모델(VLA)을 탑재해 명시적 스킬 목록 없이 학습된 범용 기능을 가진 로봇의 능력을 플랫폼의 능력 모델에 어떻게 등록·기술하고 검증할 것인가? | 관련 영역: 44. 로봇 기반 모델·언어 모델 계획, 5. 로봇 능력·작업 표현 | 근거: f3 | 종류: 일반
- 언어 모델 기반 다중 로봇 계획기를 현장 제약(설비·안전·시간창)이 있는 조건에서 비교할 공통 벤치마크나 평가 기준이 있는가? | 관련 영역: 44. 로봇 기반 모델·언어 모델 계획, 54. 시험·형식 검증·벤치마크 | 근거: f11 | 종류: 일반
- 국내 로봇 AI 파운데이션 모델 과제의 물류센터 실증 목표(자동화율 80%, 성공률 90%)에 대한 공개된 측정 결과가 있는가? | 관련 영역: 44. 로봇 기반 모델·언어 모델 계획, 61. 물류창고 | 근거: f17 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 0
- 예산 사용량: 검색 5회 · 신규 출처 15건
- 미확인 항목:
    - f1~f11 은 arXiv 초록 기준이며 본문 실험 조건 미확인
    - f13·f14: Figure AI 자체 발표 페이지(figure.ai/news/production-at-bmw)는 연결 오류로 열지 못해 교차 확인 실패
    - f15: 산업통상자원부 보도자료(korea.kr, 2025-04-10) 본문은 첨부 파일에만 있어 교차 확인 실패, '2028년까지 로봇 AI 파운데이션 모델 구축' 목표는 검색 요약에만 있어 넣지 않음
    - f16·f17: 로보티즈·BGF로지스 1차 발표 미확인, 목표치는 실측 결과 아님
    - OpenVLA 라이선스는 요약 결과가 모호해 넣지 않음
    - 병원·상업 시설·실외 현장의 로봇 기반 모델·언어 모델 계획 실배치 사례는 찾지 못함
- 범위 경계 위반 의심:
    - f1·f3·f4·f5: VLA 의 저수준 조작 정책은 로봇 자체 지능·제어 영역이므로 동향 근거로만 쓰고 f21 에서 '연계 대상: '으로 구분함
    - f11: 공정 프로그램 생성은 로봇 제어 코드에 닿으므로 계획 검증 근거로만 제안함
    - f13·f14·f16·f17: 벤더·기사 주장이므로 vendor_claim: true·태그 추정으로 냄
- 한계: 재실행 1회차. 반려 사유 1(스키마 불일치 — f15·f17 이 벤더 문서만 근거로 한 [사실]인데 vendor_claim 표시 없음): 직전 반환 JSON(runs/2026-09-30-07/research.json)이 입력에 포함되지 않아 형식만 고칠 수 없었으므로, 같은 대상으로 브리프를 다시 만들고 벤더·기사가 전한 기능·성능 주장(f13·f14·f16·f17)을 모두 vendor_claim: true·태그 추정·evidence_excerpt 첫머리 '벤더 주장: '으로 냈다. 새 브리프의 f15 는 기사(ref-1057)의 정부 협력 사실 보도로 벤더 문서가 아니며 신뢰도 low 로 두었다. 직전 브리프와 finding 번호·출처 번호가 다를 수 있다. web_fetch_available: true · fetch_mode full. 검색 5회/30, 신규 출처 15건/15(ref-1045~ref-1059, 예약 구간 안)로 출처 상한 도달. 원문 열람: 15건 모두 열었다(webfetch 14건, github_raw 1건). 논문은 초록 페이지다. 교차 확인 0건. 분류 원문 핵심 질문에는 f18 로 답했고 결론은 '로봇 기반 모델은 로봇 쪽 기능을 학습된 범용 정책으로 바꾸고, 언어 모델은 지시·분해·배정의 입력을 바꾸되 기호 계획기·외부 검증기·불확실도 기반 사람 확인과 짝지어 쓰는 방향'이라는 추정이다. 현장 유형 사례는 가정(f4)·제조 공장(f11 벤치마크, f13·f14 벤더 주장)·물류창고(f16·f17 국내, 벤더 주장)다. 국내 자료는 지디넷코리아(ref-1057)·헬로티(ref-1059) 두 건이다. 교차 규칙에 따라 이 영역의 L. AI·학습 기술 내용은 적용 대상인 25. 작업 배정 — MRTA(f10)와 C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션(f7~f9)에 함께 연결하도록 제안했다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 다루지 않았다. 용어집에 이미 있는 VLA·LLM 에이전트·LLM-모듈로·PDDL·등각 예측·불확도 정렬·작업 분해·어포던스·연합 형성은 후보로 내지 않았다. 입력 누락: runs/2026-09-30-07/research.json(직전 반환값) 없음. 정정 요청 없음. 우선 지정 질문 없음. 이 영역에 걸린 기존 열린 질문 없음.
```
