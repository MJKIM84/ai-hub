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
- verification_stage: second
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

### runs/2026-10-12-05/verification.json

```json
{
  "run_id": "2026-10-12-05",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv v2 HTML §V-A '36 high-level instructions', 과제별 로봇 1~4대, AI2-THOR(범주 6+8+14+8=36). 단일 출처."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §VI-A GPT-4·Claude-3 은 배정 계획을 만들지 않았고 GPT-3.5·Llama2 는 부적합 로봇 배정, 'not included in Table I', 과제 수·실행 수 미보고. 'Claude-3 비교는 v2 에만 있다'는 검증에서 판 비교를 하지 않았으므로 본문에 쓰지 않는다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv v1 §V-A 23장면(생산 라인 설계 전문가가 실제 산업 환경에서 수집·각색), 장면당 1~7대, 50작업, KunWu 플랫폼. ICRA 2026 채택은 ICRA 2026 수상 후보 목록에서 확인했으나 쪽수 pp.7609–7616 은 확인하지 못함."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §IV-A 휴리스틱 FIFO 로 disjunctive graph 를 푼다(같은 상호배타 자원 작업은 작업 집합 순서로 처리). 전역 최적 보장으로 읽지 않는다는 단서 적절."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §V-C 로봇 팔 3대, 전문가가 약 15분 걸려 수동 작성한 장면 설명, 시뮬레이션·실물 모두 반복 횟수·분산 미보고."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §V-B 복잡 다중 로봇 작업의 SR 하락 원인을 잘못된 분해·배정(도달 불가 로봇 배정 예)으로 정성 서술. SR 하락 자체는 표 I 에 있으나(0.87→GPT-4o 0.68, Qwen3-32B 0.60) 원인별 빈도는 정량화하지 않음 — finding 문구와 일치."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv v3 §III-C 'a human expert can provide a domain description … available as a PDDL domain file', 언어 모델은 problem PDDL 을 추론."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv v4 Remark III.6 보장은 'calibration and test scenarios are i.i.d.'일 때만. RA-L 10(1):160–167(2025-01)은 NSF PAR 기록으로 확인. arXiv 초판 제목은 'Safe Task Planning for Language-Instructed Multi-Robot Systems using Conformal Prediction'으로 달랐다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Theorem IV.2(a) 'Assuming error-free execution of the designed plans', 증명 Case II 는 사용자가 'faithfully provide help'를 전제(그렇지 않으면 분포 이동)."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §V-A '110 (validation) scenarios', N∈{1,3,10,15}, AI2-THOR. 검증 열람은 본문 앞 100,000자(전체 약 144,000자) 범위이며 그 범위에서 실물 실험 서술 없음 — '열람한 본문에서' 한정 표현 유지."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: HF openvla-7b 카드(main) Uses — 언어 지시+작업공간 카메라 영상 입력, 정규화된 7-DoF 엔드이펙터 변위 출력, 로봇·데이터셋별 통계로 un-normalize."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 커밋 c8f03f4 README 'all code in this repository is released under an MIT License'. 커밋 날짜 미확인."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인하되 표현 주의: README 는 'may inherit restrictions'(제약을 물려받을 수 있다)라고 한 뒤 'both … derived from Llama-2, and as such are subject to the Llama Community License'라고 단정한다. '적용될 수 있다'로 뭉뚱그리지 말고 두 문장을 원문대로 구분해 서술(수정 지시)."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 카드(main) 'All OpenVLA checkpoints, as well as our training codebase are released under an MIT License', 메타데이터 license: mit. README 와 충돌. 카드 커밋 47a0ec7 의 날짜(2026-02-17)는 검증에서 확인하지 않음. 같은 팀 자료라 독립 확인 아님 — 충돌 병기·열린 질문 처리 적절."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: docs/remote_inference.md 'This returns an action chunk of shape (action_horizon, action_dim).'"
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 같은 파일 '… from the predicted action chunk open-loop in the remaining steps.' 예시 설명이며 안전 정지 근거 아님이라는 단서 적절."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: README Base Models 표 pi0_base·pi0_fast_base·pi05_base, π0.7 없음. '기반 체크포인트' 한정을 유지한다(미세조정 체크포인트 목록과 혼동하지 않음)."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: n1.7-release README 'Early Access (EA) release … support and stability guarantees are limited until the GA release', GA 항목 'Production deployment with commercial support'. 브랜치 기준 열람(커밋 미고정) — 기준일 2026-10-12 명시 필요."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: License 절 Code Apache 2.0, Model weights NVIDIA Open Model License."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: README 'fully commercially licensable under Apache 2.0' 문구 존재, 같은 문서 License 절과 불일치. [추정]·벤더 주장 유지."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 커밋 6949d5d LICENSE 표제 'NVIDIA License', §3.3 비상업 한정·NVIDIA 및 계열사 상업 사용 예외·'non-commercially' = 연구·평가 목적."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 3B 카드 'released under the NVIDIA Open Model License Agreement', 'ready for commercial/non-commercial use'; README·LICENSE 와 함께 세 갈래 서술. 모두 NVIDIA 자료라 독립 확인 아님. 이 finding 은 GR00T N1.7 에 관한 것이며 GR00T N1(ref-1049) 행에 옮겨 적지 않는다(수정 지시)."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv v2 §V-D c∈{joint, ee}, 'at runtime, we can pick the control mode depending on the task'. 회사 자체 보고서 [추정]·벤더 주장 유지."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §VI-B 학습 중 0~12 타임스텝 지연 모사, 50Hz 에서 최대 240ms; 'The UR5e robots run at 20 Hz'. 학습 조건이며 실측 지연 아님이라는 단서 유지."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Discussion 에서 seen/unseen 을 'practically difficult' 하게 구분한다고 한계로 적음. [추정] 유지."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv v3 §2.1 일곱 단일 축 교란(물체 배치·카메라 시점·로봇 초기 상태·언어 지시·조명·배경 질감·센서 잡음). CVPR 2026 게재(pp.38574–38583, 다른 제목)는 CVF 오픈액세스 HTML·포스터 페이지로 확인, 게재본 PDF 는 검증에서 403 으로 열지 못함."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "사실 → 추정: '판마다 다르다'는 해석이 틀렸다. arXiv v3 안에 두 표가 모두 있다 — 표 1(원래 LIBERO 설정의 단일 축 교란 분석: OpenVLA-OFT 원본 97.1·카메라 59.7·로봇 초기 상태 37.2)과 표 2(LIBERO-Plus 벤치마크 견고성 평가: 카메라 56.4·로봇 31.9·전체 69.6). 수치 차이는 판 차이가 아니라 평가 설정 차이다. 게재본 표 2 의 'Original 97.1' 열은 게재본 PDF 를 열지 못해 검증에서 확인하지 못함. 수정 지시대로 고쳐 쓴다."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ROSA Wiki FAQ(raw) 'limited to text-based interactions and cannot interact with the physical world', 맞춤 도구·프롬프트 필요. 릴리스 미고정 위키 문서 — 접근일 기준 명시."
    },
    {
      "finding_id": "f29",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 같은 FAQ 의 맞춤 도구 매개변수 검증·행동 제한, 실행 전 로봇 상태·능력 확인 권고. 권고이며 자동 제공 기능 아님이라는 단서 유지."
    },
    {
      "finding_id": "f30",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: MCP 블로그(2026-03-16, Hungerford·Morrow·Chang) 'They aren't enforcement.' … 'a job for network controls or sandboxing'. 규범 명세가 아닌 해설 글임을 명시."
    },
    {
      "finding_id": "f31",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: MoveIt Pro 문서(Version 10) 배포 MCP 키 읽기 전용, 동작은 호스트 사용자 세션에서 기존 Objective 시작·취소로 한정. [추정]·벤더 주장 유지. 발행일 미확인."
    },
    {
      "finding_id": "f32",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 'clients may auto-approve calls. The server adds no confirmation prompt.' [추정]·벤더 주장 유지."
    },
    {
      "finding_id": "f33",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: run_objective 'keeps moving if the session ends', cancel_objective 'best effort, not an emergency stop', 물리 비상정지 대체 불가. [추정]·벤더 주장 유지."
    },
    {
      "finding_id": "f34",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Figure 발표(2025-11-19) '11 month … deployment', 6개월 안 납품·시험, 10개월 안 전면 배치, 6개월 일일 가동·1,250시간 이상. BMW 보도자료(2026-06-25) 재열람: 'over ten months'는 본문, '11-month'는 Figure CEO Brett Adcock 인용. 당사자 자료라 독립 확인 아님. [추정]·벤더 주장 유지."
    },
    {
      "finding_id": "f35",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 'Our target was > 99% success per shift.', 'The goal was zero per shift.' 달성 여부 미기재. 목표치로만 적는다."
    },
    {
      "finding_id": "f36",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 'F.03 Arrives at BMW'(2026-06-30) 'first demonstration of Figure 03 performing a logistics workflow at BMW Group Plant Spartanburg', Helix 02 'pixels-to-actions VLA'가 손·팔·몸통·발을 조율해 바퀴 달린 무거운 대차를 끎. [추정]·벤더 주장 유지."
    },
    {
      "finding_id": "f37",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Figure 자체 발표 2건이 실재하므로 대상 페이지 5절의 'Figure AI 자체 발표로는 교차 확인하지 못했다'는 사실과 맞지 않음. 정정 문구는 '당사자 발표가 일치함(독립 확인 아님)'으로 한다."
    },
    {
      "finding_id": "f38",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "motir.go.kr 원문은 검증에서 두 번 모두 ECONNRESET 으로 열지 못했고 검색에도 이 URL 이 나오지 않았다(원문 미열람(검증)). 내용(2025-11-24 산업부–서울대 MOU, 휴머노이드 AI 파운데이션 모델 2028년까지 484억 원, 장병탁·박재흥, 기업 데이터·플랫폼 제공 → 서울대 모델 개발 → 기업 탑재)은 같은 발표를 다룬 언론 보도 검색 결과와 일치. 보도는 보도자료에서 나온 것이라 독립 교차 확인으로 세지 않음. medium 상한."
    },
    {
      "finding_id": "f39",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. 근거 f2·f6 은 확인됨. 누구의 의견인지(이 위키·구축자 의견) 밝힌다(수정 지시)."
    },
    {
      "finding_id": "f40",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. 근거 f4·f7·f8·f9 확인. 구축자 의견 표시 필요."
    },
    {
      "finding_id": "f41",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. 근거 f5 확인. 구축자 의견 표시 필요."
    },
    {
      "finding_id": "f42",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. 근거 f11·f15·f16·f23 확인. 'ROP 설계 제안이며 표준이 아니다' 단서 유지, 구축자 의견 표시."
    },
    {
      "finding_id": "f43",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. 근거 f12~f14·f18~f22 확인. 법률 판단 아님 단서 유지."
    },
    {
      "finding_id": "f44",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지하되 근거 f27 의 해석 오류를 따라 '판(arXiv 판·게재본)을 밝혀'를 '표·평가 설정(단일 축 교란 분석인지 벤치마크 평가인지)과 판을 밝혀'로 고친다(수정 지시)."
    },
    {
      "finding_id": "f45",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. 근거 f28~f33 확인. 물리 비상정지는 연계 대상으로 쓴다(범위 수정 지시)."
    },
    {
      "finding_id": "f46",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. 근거 f34~f38 확인. 구축자 의견 표시 필요."
    }
  ],
  "category_fit": {
    "ok": true,
    "reassign_to": null
  },
  "scope_boundary": {
    "ok": true,
    "issues": [
      "f31~f33·f45 (9절 도구 호출 실행 경계): MoveIt Pro 의 cancel_objective·물리 비상정지 서술을 ROP 가 비상정지를 제공하는 것처럼 쓰면 범위 위반이다. 물리 비상정지와 로봇 런타임 정지는 로봇 자체 지능·제어/설비 안전 제어의 연계 대상으로 짧게 적고, ROP 는 권한·승인·완료 판정·정지 절차 연결만 맡는 것으로 쓴다.",
      "f12~f22: 코드·가중치 라이선스의 적용 판단은 59. 법·규제·보험·라이선스 쪽 연계 대상이며 7절에서는 문서 문구 대조까지만 쓴다(브리프 self_check 와 같은 판단)."
    ]
  },
  "duplication": {
    "ok": true,
    "overlaps": [
      "f1 은 chat-based-configuration-and-operation 트랙 stage-2-data-and-standards.md 의 SMART-LLM 36개 지시 서술(원문 미열람)과 같은 수치 — 원문 확인 보강으로만 쓰고 기존 각주 ref-090 재사용",
      "f30 은 2026-09-29-area13-s6.md(ref-856)·트랙 stage-4(ref-696)의 MCP 명세 서술과 같은 방향 — 보완 관계로 짧게 쓰고 재서술하지 않음",
      "f34 는 대상 페이지 5절의 10/11개월 충돌과 oq-219 에 이미 있는 내용 — 위치(CEO 인용·본문)와 Figure 쪽 기간 축만 보탬",
      "f22 는 2026-09-30-area44-s7.md 표의 'GR00T N1 — 오픈소스(공개 모델)' 행과 대상 모델 판이 다름(N1.7 대 N1) — 충돌로 처리하지 말고 별도 판으로 구분"
    ]
  },
  "terminology": {
    "ok": true,
    "conflicts": [
      "disjunctive graph 번역어가 위키 안에서 '선택 그래프'(2026-09-30-area44-s6.md)·'선언 그래프'·'이접 그래프'(트랙 stage-1)로 갈림. 용어집에는 항목이 없음. 이번 갱신 페이지에서는 '이접 그래프(disjunctive graph)'로 통일하고 다른 페이지는 후속 정리로 남긴다."
    ]
  },
  "quotation_check": {
    "ok": true
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "f27: [사실] → [추정]으로 강등하고 문장을 고쳐 쓴다 — 'arXiv v3 안의 표 1(원래 LIBERO 설정의 단일 축 교란 분석: OpenVLA-OFT 원본 97.1, 카메라 시점 59.7, 로봇 초기 상태 37.2)과 표 2(LIBERO-Plus 벤치마크 견고성 평가: 카메라 56.4, 로봇 31.9, 전체 69.6)는 평가 설정이 다른 두 표'로 쓰고, '판마다 다르다'·'arXiv 판과 게재본의 수치 차이' 표현은 지운다 — 검증에서 두 표가 모두 arXiv v3 에 있음을 확인했고, 게재본 PDF 는 열지 못해 게재본 '원본 97.1' 열은 확인하지 못했다.",
    "f44: '벤치마크 수치는 판(arXiv 판·게재본)을 밝혀 인용하며'를 '벤치마크 수치는 표·평가 설정(단일 축 교란 분석인지 벤치마크 평가인지)과 판을 밝혀 인용하며'로 고친다 — 근거 f27 의 해석이 바뀌었다.",
    "8절(분리 2026-09-30-area44-s8) LIBERO-Plus 항목: 수치 병기를 위 f27 수정 문구로 하고, ref-1615(CVPR 2026 게재본, 제목 다름)는 게재 사실·일곱 교란 축의 근거로만 각주를 단다.",
    "f13: 'Llama Community License 가 적용될 수 있다'로 뭉뚱그리지 말고 README 원문대로 '사전학습 모델이 기반 모델의 제약을 물려받을 수 있다'와 '두 모델은 Llama 2 에서 파생돼 Llama Community License 를 따른다고 적는다'를 구분해 쓴다 — README 는 뒤 문장을 단정형('are subject to')으로 적는다. 법적 적용 판정이 아님은 유지한다.",
    "7절(분리 2026-09-30-area44-s7) GR00T 서술: f18~f22 는 GR00T N1.7(ref-1611·ref-1612)에 관한 것이므로 기존 'GR00T N1(ref-1049) — 오픈소스(공개 모델)' 행의 유형 칸을 N1.7 근거로 고치지 않는다. N1.7 을 별도 행이나 별도 문장으로 두고 'EA 릴리스, 코드 Apache 2.0, 가중치는 문서마다 조건이 다름(README 소개·License 절·3B 카드·3B LICENSE 3.3절)'으로 적는다 — N1 의 가중치 라이선스는 이번 브리프에 근거가 없다.",
    "7절: 표 바로 아래 'OpenVLA의 라이선스는 확인하지 못했다'를 지우고 코드 MIT(f12), README 의 Llama 2 파생 문구(f13), HF 카드 '모든 체크포인트 MIT'(f14)를 충돌 그대로 병기하며 어느 쪽도 고르지 않는다. 충돌은 open_questions_new 의 출처 충돌 질문으로 연결한다.",
    "5절 제조 공장 사례: 'Figure AI 자체 발표로는 교차 확인하지 못했다'를 지우고 'Figure AI 자체 발표(2025-11-19 F.02 회고, 2026-06-30 F.03 첫 시연)가 같은 배치·착수를 설명하나 같은 프로젝트 당사자 자료라 독립 확인은 아니다'로 고친다(f37). [추정] 벤더 주장 표기와 각주 ref-1619·ref-1620·ref-1051 을 단다.",
    "5절 제조 공장 예외·성과 칸: '교대당 99% 초과 성공률·개입 0회'는 '목표치(실측 아님)'로만 적고(f35), 10/11개월 문장에는 11개월이 Figure CEO 인용, 10개월이 BMW 본문이라는 위치와 Figure 쪽 6·10·11개월 이정표를 덧붙이되 하나로 정하지 않는다(f34). oq-219 는 열림 유지.",
    "5절에 IMR-LLM 실물 시험(f5)을 넣을 경우 '연구 평가(로봇 팔 3대 단일 장면, 전문가 약 15분 수동 장면 작성, 반복 횟수 미보고)'로 표시하고 장기 운영 실적으로 쓰지 않는다. 현장 유형은 '제조 공장'으로 명시하고 여섯 항목 가운데 근거 없는 칸은 '미확인'으로 둔다.",
    "5절 물류창고: 산업부 M.AX 휴머노이드 과제(f38)는 로보티즈–BGF로지스 과제(ref-1052)와 별도 문장으로 쓰고 같은 사업인지 미확인임을 밝힌다. ref-1621 각주는 검증에서 원문을 열지 못했으므로 기준일(2025-11-24 등록)을 반드시 남긴다.",
    "9절: 도구 호출 실행 경계 문단에서 물리 비상정지·런타임 소프트웨어 정지는 '연계 대상'(로봇 자체 제어·설비 안전 제어)으로 짧게 적고, ROP 가 직접 맡는 것은 읽기/실행 권한, 승인된 계획 대상 확인, 완료 판정, 세션 종료와 정지 절차의 연결로 한정한다. MoveIt Pro 서술(f31~f33)은 모두 [추정] 벤더 주장, MCP 블로그(f30)는 '규범 명세가 아닌 프로젝트 해설'임을 밝힌다.",
    "f39~f46: [의견] 문장마다 누구의 의견인지 밝힌다(예: '이 위키의 의견' 또는 '구축자 의견'). 외부 조사 메모의 시사점을 옮긴 것이므로 출처의 주장처럼 쓰지 않는다.",
    "6절(분리 2026-09-30-area44-s6): 57행 '선택 그래프(disjunctive graph)'를 '이접 그래프(disjunctive graph)'로 고친다. 트랙 페이지 등 다른 페이지의 번역어는 이번 갱신에서 고치지 않고 후속 정리로 남긴다.",
    "ref-170(IMR-LLM): ICRA 2026 채택은 적을 수 있으나 쪽수(pp.7609–7616)는 검증에서 확인하지 못했으므로 본문·각주에 쓰지 않는다. 같은 이유로 SMART-LLM 의 IROS 2024 쪽수(pp.12140–12147)도 쓰지 않는다.",
    "f18·f28: 브랜치·위키 문서처럼 판이 고정되지 않은 출처(ref-1611 n1.7-release 브랜치, ref-1616 ROSA Wiki FAQ)는 본문 또는 각주에 '접근일 2026-10-12 기준'임을 밝힌다.",
    "11절(분리 2026-09-30-area44-s11): oq-216·oq-217·oq-219 는 '부분 근거'로만 연결하고 상태는 열림 유지. oq-141 은 이 영역 질문 목록에 없으므로 13. 대화형 기능의 신뢰·기반 쪽 질문으로 연결만 하고 이 페이지에서 상태를 바꾸지 않는다. open_questions_new 4건은 브리프 문구대로 등록한다.",
    "각주 정의: 이번에 다시 연 기존 출처(ref-090·ref-170·ref-092·ref-1051)를 갱신하는 절은 접근일을 2026-10-12 로 쓰고, 새 출처 ref-1607~ref-1621 은 브리프의 기관·제목·발행일(없으면 '미확인')·URL 그대로 각주를 단다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 45건, 미확인 1건, 교차 확인 0건. 강등: f27 사실 → 추정(LIBERO-Plus 수치 차이는 arXiv 판과 게재본의 차이가 아니라 arXiv v3 안의 표 1(단일 축 교란 분석)과 표 2(벤치마크 평가)의 평가 설정 차이). 원문 미열람 출처: ref-1621(검증에서 두 차례 접속 실패. 내용은 2025-11-24 협약 보도와 일치), ref-1615 게재본 PDF(HTML·포스터 페이지로 실재만 확인). 주의: 모든 [사실] finding 은 단일 출처이거나 같은 팀·기관·프로젝트 자료여서 독립 교차 확인이 없다. OpenVLA(코드 MIT, README 의 Llama 2 파생 문구, HF 카드의 모든 체크포인트 MIT)와 GR00T N1.7(README 소개의 Apache 2.0 상용 가능, License 절·3B 카드의 NVIDIA Open Model License, 3B LICENSE 3.3절 비상업 한정)의 라이선스 문서는 서로 충돌하며 어느 쪽도 고르지 않았다. 법적 판단도 아니다. GR00T N1.7 근거를 GR00T N1 행에 옮겨 적지 않는다. Figure·BMW·MoveIt Pro·π0.7 서술은 벤더 주장이고, 99% 성공률·개입 0회는 목표치다. ICRA 2026·IROS 2024 쪽수는 확인하지 못했다. 브리프 출처 가운데 ref-1051·ref-1617~ref-1621 은 fetched: true 인데 fetch_url 이 비어 있다. 검증에서 ref-1051·ref-1617~ref-1620 은 열람을 확인했다. 정정 요청 없음. 갱신 범위가 대상 페이지와 분리 주제 페이지(s6·s7·s8·s11)에 걸친다.",
  "retry_reason": null
}
```

### runs/2026-10-12-05/pages.json

```json
{
  "run_id": "2026-10-12-05",
  "outline": [
    {
      "path": "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 3600,
      "summary": "가정 연구 평가, BMW–Figure 제조 공장 발표(10/11개월 출처 위치·목표치 구분·Figure 자체 발표는 당사자 자료), IMR-LLM 로봇 팔 3대 연구 평가, 물류창고 실증 계획과 산업부 M.AX 과제를 현장 유형별로 정리한다. [추정] 벤더 주장[^ref-1051][^ref-1619]",
      "planned_findings": [
        "f5",
        "f34",
        "f35",
        "f36",
        "f37",
        "f38",
        "f41",
        "f46"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1900,
      "summary": "SMART-LLM·IMR-LLM·S-ATLAS 의 평가 규모와 실패 양상, LLM+P·S-ATLAS 보장이 기대는 입력 전제(사람이 준 도메인, i.i.d., 무오류 실행)를 더한다. [사실][^ref-090][^ref-170][^ref-1607]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f4",
        "f6",
        "f7",
        "f8",
        "f9",
        "f10",
        "f39",
        "f40"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 2600,
      "summary": "OpenVLA·GR00T N1.7 의 코드·가중치 사용 조건 문서 충돌을 병기하고, OpenVLA·openpi 의 입출력 계약과 ROSA 의 물리 실행 조건을 더한다. [사실][^ref-1608][^ref-1609][^ref-1611][^ref-1612]",
      "planned_findings": [
        "f11",
        "f12",
        "f13",
        "f14",
        "f15",
        "f16",
        "f17",
        "f18",
        "f19",
        "f20",
        "f21",
        "f22",
        "f28",
        "f29",
        "f42",
        "f43"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 1500,
      "summary": "π0.7 기술 보고서(벤더 주장), LIBERO-Plus 의 7개 교란 축과 평가 설정이 다른 두 표, 산업부 M.AX 휴머노이드 과제를 더한다. [추정] 벤더 주장[^ref-1613]",
      "planned_findings": [
        "f23",
        "f24",
        "f25",
        "f26",
        "f27",
        "f38",
        "f44"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 2000,
      "summary": "도구 호출(MCP)로 로봇을 움직일 때 ROP 는 권한·승인된 계획 대조·완료 판정·세션 종료와 정지 절차 연결을 맡고, 물리 비상정지와 런타임 정지는 연계 대상이다. [의견][^ref-1617][^ref-1618]",
      "planned_findings": [
        "f28",
        "f29",
        "f30",
        "f31",
        "f32",
        "f33",
        "f45"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md",
      "section": "11. 열린 질문",
      "budget_chars": 1500,
      "summary": "oq-216·oq-217·oq-219 에 부분 근거를 연결하고(열림 유지) 새 질문 4건(가정 감시, 행동 청크와 정지 계약, OpenVLA·GR00T N1.7 라이선스 출처 충돌)을 올린다.",
      "planned_findings": [
        "f9",
        "f14",
        "f16",
        "f22",
        "f24",
        "f32",
        "f34",
        "f38"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md",
      "section": "13. 참고 자료 (각주)",
      "budget_chars": 0,
      "summary": "새 출처 15건 각주 정의 추가, 다시 연 기존 출처 4건 접근일 갱신."
    }
  ],
  "pages": [
    {
      "path": "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "5·9절 고침(Figure AI 자체 발표 문장 정정, 10/11개월 출처 위치·Figure 기간 축, 99%·개입 0회 목표치 구분, IMR-LLM 실물 연구 평가 사례, 산업부 M.AX 과제, 도구 호출 실행 경계), 6·7·8·11절에 2026-10-12 갱신 소절 추가, 13절에 새 각주 15건·기존 4건 접근일 갱신",
      "patches": [
        {
          "section": "5. 적용 사례 (현장 유형 명시)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-12-05/pages/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md 의 해당 절을 본다)"
        },
        {
          "section": "6. 대표 접근법과 기술",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-12-05/pages/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md 의 해당 절을 본다)"
        },
        {
          "section": "7. 관련 표준·프레임워크·오픈소스",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-12-05/pages/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md 의 해당 절을 본다)"
        },
        {
          "section": "8. 대표 연구와 자료",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-12-05/pages/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md 의 해당 절을 본다)"
        },
        {
          "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-12-05/pages/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md 의 해당 절을 본다)"
        },
        {
          "section": "11. 열린 질문",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-12-05/pages/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md 의 해당 절을 본다)"
        },
        {
          "section": "13. 참고 자료 (각주)",
          "action": "replace",
          "frontmatter": {
            "sources": [
              "ref-1045",
              "ref-1046",
              "ref-1047",
              "ref-1048",
              "ref-088",
              "ref-092",
              "ref-586",
              "ref-090",
              "ref-351",
              "ref-1049",
              "ref-170",
              "ref-171",
              "ref-1050",
              "ref-1051",
              "ref-1052",
              "ref-1607",
              "ref-1608",
              "ref-1609",
              "ref-1610",
              "ref-1611",
              "ref-1612",
              "ref-1613",
              "ref-1614",
              "ref-1615",
              "ref-1616",
              "ref-1617",
              "ref-1618",
              "ref-1619",
              "ref-1620",
              "ref-1621"
            ],
            "last_run": "2026-10-12"
          },
          "content": "(절 본문 생략 — runs/2026-10-12-05/pages/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md 의 해당 절을 본다)"
        }
      ]
    },
    {
      "path": "docs/topics/2026/2026-10-12-area44-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 44. 로봇 기반 모델·언어 모델 계획 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(2,705자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-12-area44-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 44. 로봇 기반 모델·언어 모델 계획 의 \"11. 열린 질문\" 절(1,985자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-12-area44-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 44. 로봇 기반 모델·언어 모델 계획 의 \"6. 대표 접근법과 기술\" 절(1,763자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-12-area44-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 44. 로봇 기반 모델·언어 모델 계획 의 \"8. 대표 연구와 자료\" 절(1,267자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-10-12 | 44. 로봇 기반 모델·언어 모델 계획 | 갱신: 5절 Figure AI 자체 발표 문장 정정·10/11개월 출처 위치·99% 목표치 구분·IMR-LLM 실물 연구 평가 사례·산업부 M.AX 과제, 6~8절 다중 로봇 계획 평가 조건·보장 전제·공개 VLA 입출력·라이선스 문서 충돌·π0.7·LIBERO-Plus, 9절 도구 호출 실행 경계, 새 열린 질문 4건 | run 2026-10-12-05",
  "index_updates": {
    "home_recent": "2026-10-12 — 44. 로봇 기반 모델·언어 모델 계획: 제조 공장 사례의 Figure AI 자체 발표 정정과 목표치·기간 구분, 다중 로봇 언어 계획의 평가 조건·보장 전제, 공개 VLA 입출력과 라이선스 문서 충돌, 도구 호출 실행 경계를 더했다",
    "category_recent": "2026-10-12 — 44. 로봇 기반 모델·언어 모델 계획: 5·9절 고침, 6·7·8·11절 갱신 소절 추가(SMART-LLM·IMR-LLM·S-ATLAS 평가 조건, OpenVLA·GR00T N1.7 라이선스 충돌, openpi 행동 청크, π0.7·LIBERO-Plus, MCP 도구 호출 경계), 새 출처 15건",
    "area_recent": "2026-10-12 — 44. 로봇 기반 모델·언어 모델 계획: 갱신(5·9절 고침, 6·7·8·11절에 2026-10-12 갱신 소절 추가, 새 열린 질문 4건, 새 출처 15건)"
  },
  "glossary_updates": [],
  "reference_updates": [
    {
      "id": "ref-090",
      "org": "Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C.",
      "title": "SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models",
      "published": "2023-09",
      "url": "https://arxiv.org/abs/2309.10062",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "SMART-LLM 논문(기존 출처). 이번에 arXiv v2 HTML 본문에서 36개 고수준 지시 데이터셋(§V-A)과 불가능 과제 시험(§VI-A)을 확인했다.",
      "cited_by": [
        "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md"
      ],
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
      "summary": "IMR-LLM 논문(기존 출처, ICRA 2026 채택). 이번에 arXiv v1 HTML 본문에서 IMR-Bench 23장면·50작업, FIFO 휴리스틱, 로봇 팔 3대 실물 시험, 도달 불가 배정 오류를 확인했다.",
      "cited_by": [
        "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md"
      ],
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
      "cited_by": [
        "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md"
      ],
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
      "summary": "BMW 그룹 보도자료(기존 출처). 이번 재열람에서 '11-month deployment'는 Figure CEO 인용문, 'over ten months'는 본문에 있음을 확인했다.",
      "cited_by": [
        "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md"
      ],
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
      "summary": "등각 예측으로 사용자 지정 임무 성공률을 노리는 분산 다중 로봇 언어 계획기 S-ATLAS 논문(RA-L 10(1), DOI 10.1109/LRA.2024.3504233). arXiv v4 HTML 로 i.i.d. 조건(Remark III.6), 무오류 실행 전제(Theorem IV.2), 110개 AI2-THOR 검증 시나리오를 확인했다.",
      "cited_by": [
        "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md"
      ],
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
      "summary": "OpenVLA 공식 저장소 README·LICENSE. 코드 MIT, 사전학습 모델은 기반 모델의 제약을 물려받을 수 있고 Llama 2 파생이라 Llama Community License 를 따른다는 문구(99–101행)를 확인했다. 커밋 날짜는 확인하지 못했다.",
      "cited_by": [
        "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md"
      ],
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
      "summary": "OpenVLA 7B 가중치 모델 카드. 입출력(언어+영상 → 정규화 7자유도 엔드이펙터 변위, 로봇·데이터셋별 역정규화)과 '모든 체크포인트 MIT' 문구를 현재 main(커밋 47a0ec7)에서 확인했다.",
      "cited_by": [
        "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md"
      ],
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
      "summary": "π0 계열 공개 구현 openpi. 원격 추론의 행동 청크 형태(action_horizon, action_dim)와 개방 루프 실행 주석, 제공 기반 체크포인트(π0·π0-FAST·π0.5), LICENSE(Apache 2.0)를 확인했다. 커밋 날짜는 확인하지 못했다.",
      "cited_by": [
        "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md"
      ],
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
      "summary": "GR00T N1.7 공식 저장소 README. Early Access 릴리스 표기, 소개 문단의 'Apache 2.0 으로 상용 라이선스 가능' 문구, License 절의 코드 Apache 2.0·가중치 NVIDIA Open Model License 구분을 확인했다. 브랜치 이름 기준(접근일 2026-10-12)이며 커밋 sha 로 고정하지 못했다.",
      "cited_by": [
        "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md"
      ],
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
      "summary": "GR00T N1.7 3B 가중치 저장소. LICENSE(커밋 6949d5d, 현재 main 과 같음)의 'NVIDIA License' 3.3절 비상업 한정·NVIDIA 계열사 예외와, 모델 카드(main)의 'NVIDIA Open Model License'·'commercial/non-commercial use' 문구를 확인했다.",
      "cited_by": [
        "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md"
      ],
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
      "cited_by": [
        "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md"
      ],
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
      "summary": "VLA 모델의 7개 축 입력 교란 견고성 평가 프리프린트(v1 2025-10-15, v3 2025-12-26). v3 HTML 의 §2.1 과, 평가 설정이 다른 표 1(원래 LIBERO 설정의 단일 축 교란 분석)·표 2(LIBERO-Plus 벤치마크 견고성 평가)를 확인했다.",
      "cited_by": [
        "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md"
      ],
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
      "summary": "LIBERO-Plus 의 CVPR 2026 게재본(arXiv 판과 제목이 다름). 위키에서는 게재 사실과 일곱 교란 축의 근거로만 쓴다. 검증 단계에서는 게재본 PDF 를 열지 못하고 HTML·포스터 페이지로 실재를 확인했다.",
      "cited_by": [
        "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md"
      ],
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
      "summary": "ROSA 공식 위키 FAQ(릴리스에 고정되지 않은 문서, 접근일 2026-10-12 기준). 핵심 에이전트는 물리 세계와 상호작용할 수 없고 맞춤 도구·프롬프트가 필요하다는 한계와, 맞춤 도구에 상태·능력 확인과 안전 검사를 넣으라는 권고를 확인했다. README(ref-171)와 다른 페이지다.",
      "cited_by": [
        "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md"
      ],
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
      "summary": "MCP 프로젝트 공식 블로그 해설. 도구 어노테이션은 위험 힌트이며 실행 강제 수단이 아니라는 설명을 확인했다. 규범 명세 자체는 아니다.",
      "cited_by": [
        "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md"
      ],
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
      "cited_by": [
        "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md"
      ],
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
      "cited_by": [
        "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md"
      ],
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
      "cited_by": [
        "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md"
      ],
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
      "summary": "산업부–서울대 M.AX 얼라이언스 협력 MOU 보도자료(2025-11-24 등록). 휴머노이드 분과 'AI 파운데이션 모델 개발'(2025~2028년, 484억 원, 장병탁·박재흥) 과제 표를 확인했다. 검증 단계에서는 접속 실패로 재열람하지 못했고 같은 발표의 보도와 내용이 일치했다.",
      "cited_by": [
        "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md"
      ],
      "source_unopened": false
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "언어 모델 다중 로봇 계획의 검증이 기대는 가정(사람이 준 도메인 판, i.i.d. 시나리오, 무오류 스킬 실행)을 런타임에서 누가 감시하고, 가정이 깨졌을 때 어떤 계획을 중단·재검증할 것인가?",
      "areas": [
        44,
        54
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "원격 VLA 정책의 행동 청크(개방 루프 실행) 유효기간과, 도구 세션이 끝난 뒤에도 로봇이 움직일 수 있는 MCP 실행의 안전한 정지 계약을 어떻게 결합할 것인가?",
      "areas": [
        44,
        29
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "출처 충돌: OpenVLA 공개 가중치의 사용 조건은 저장소 README(Llama 2 파생이라 Llama Community License 가 적용될 수 있음)와 Hugging Face 모델 카드(모든 체크포인트 MIT) 가운데 어느 쪽인가?",
      "areas": [
        44,
        59
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "출처 충돌: GR00T N1.7 가중치의 상업적 사용 가능 여부는 README 소개(Apache 2.0 으로 상용 가능), README License 절·3B 모델 카드(NVIDIA Open Model License, 상업·비상업 사용 준비), 3B 가중치 저장소 LICENSE 3.3절(NVIDIA·계열사 외 비상업 한정) 가운데 어느 문서가 정하는가?",
      "areas": [
        44,
        59
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "제조 공장",
      "item": "작업 대상",
      "link": "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md#5-적용-사례-현장-유형-명시",
      "title": "44. 로봇 기반 모델·언어 모델 계획"
    },
    {
      "site_type": "제조 공장",
      "item": "수행 자원",
      "link": "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md#5-적용-사례-현장-유형-명시",
      "title": "44. 로봇 기반 모델·언어 모델 계획"
    },
    {
      "site_type": "제조 공장",
      "item": "완료·인계",
      "link": "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md#5-적용-사례-현장-유형-명시",
      "title": "44. 로봇 기반 모델·언어 모델 계획"
    },
    {
      "site_type": "제조 공장",
      "item": "예외·성과",
      "link": "docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md#5-적용-사례-현장-유형-명시",
      "title": "44. 로봇 기반 모델·언어 모델 계획"
    }
  ],
  "additional_research_requests": [
    "후속 갱신(입력 누락): 분리 주제 페이지 docs/topics/2026/2026-09-30-area44-s7.md 의 표 아래 문장 'OpenVLA의 라이선스는 확인하지 못했다'를 지우고, docs/topics/2026/2026-09-30-area44-s6.md 57행 '선택 그래프(disjunctive graph)'를 '이접 그래프(disjunctive graph)'로 바꾸는 차등 갱신이 필요하다. 두 페이지의 본문이 이번 스토리텔러 입력에 없어 직접 고치지 못했고, 대상 세부영역 페이지 6·7절에 정정·용어 통일 문장만 두었다. 다음 44. 로봇 기반 모델·언어 모델 계획 갱신 실행에서 두 주제 페이지를 입력으로 넣어 달라(하루 갱신 상한 2 안에서).",
    "후속 정리(이번 갱신 범위 밖): docs/standards/index.md 의 OpenVLA·GR00T N1 '오픈소스' 항목에 코드·가중치 라이선스 구분이 없다. OpenVLA 는 ref-1608·ref-1609 의 문서 충돌을, GR00T 는 N1 과 N1.7 을 구분해 ref-1611·ref-1612 기준으로 반영할 수 있는지 59. 법·규제·보험·라이선스 실행에서 검토가 필요하다.",
    "후속 정리(트랙 페이지): chat-based-configuration-and-operation 트랙 stage-1-prior-work-and-products.md 의 ROSA '확인·권한 장치 설명이 없다' [추정]을 ROSA FAQ(ref-1616)로 정리, 같은 파일의 disjunctive graph 번역어('선언 그래프'·'이접 그래프') 통일과 'IMR-Bench 규모 미확인'에 ref-170 연결, stage-2-data-and-standards.md 의 SMART-LLM '원문 미열람' 수치에 ref-090 원문 확인 연결, task-model-draft.md 의 LLM+P 부분에 ref-092 연결.",
    "용어집: '이접 그래프(disjunctive graph)' 항목이 없다. 위키 안에서 번역어가 셋으로 갈렸으므로 정의 출처(작업장 스케줄링 문헌)를 찾아 용어 후보로 올려 달라.",
    "5절 제조 공장(BMW–Figure): 배치 기간 10/11개월의 기점·종점과 집계 관계, 교대별 실측 성공률·개입의 분모, Figure 03 첫 시연 이후 가동률을 확인할 독립 자료가 필요하다(oq-219).",
    "5절 물류창고: 산업부 M.AX 휴머노이드 과제와 로보티즈–BGF로지스 물류 과제의 동일성, 자동화율 80%·성공률 90% 실측 결과(oq-218).",
    "5·6절: SMART-LLM 실물 시험의 로봇 대수·반복 수, IMR-LLM 의 장기 운영 근거, 병원·상업 시설·실외에서 로봇 기반 모델·언어 모델 계획을 쓴 이기종 플릿 현장 실증이 필요하다.",
    "7절·11절: VLA 공통 능력 등록 표준·적합성 시험(oq-216), π0.7 보고서와 공개 배포물의 대응, 네트워크 포함 실측 최대 추론 지연(oq-104 관련)."
  ],
  "fixes_applied": [
    "f27 강등 — 8절 LIBERO-Plus 항목에서 [추정]으로 쓰고 'arXiv v3 안의 표 1(원래 LIBERO 설정의 단일 축 교란 분석: 97.1·59.7·37.2)과 표 2(LIBERO-Plus 벤치마크 견고성 평가: 56.4·31.9·69.6)는 평가 설정이 다른 두 표'로 썼으며, '판마다 다르다'·판 차이 표현은 넣지 않았다(각주 ref-1614).",
    "f44 — 8절의 의견 문장을 '벤치마크 수치는 표·평가 설정(단일 축 교란 분석인지 벤치마크 평가인지)과 판을 밝혀 인용하며'로 고쳐 썼다.",
    "8절 LIBERO-Plus — 수치 병기는 1번 수정 문구로 하고, ref-1615 는 게재본 제목과 일곱 교란 축 문장에만 각주로 달았다.",
    "f13 — 7절에서 'README 는 사전학습 모델이 기반 모델의 제약을 물려받을 수 있다고 적는다'와 'README 는 두 사전학습 모델이 Llama 2 에서 파생돼 Llama Community License 를 따른다고 단정형으로 적는다'를 두 문장으로 나눠 쓰고, 소절 머리에 법적 판단이 아님을 밝혔다.",
    "GR00T — 7절에 'GR00T N1.7(GR00T N1과 다른 판)' 별도 문단을 두어 EA 릴리스·코드 Apache 2.0·가중치는 문서마다 조건이 다름(README 소개·License 절·3B 카드·3B LICENSE 3.3절)으로 적었고, 주제 페이지 표의 GR00T N1 행은 이 근거로 고치지 않는다고 명시했다.",
    "OpenVLA 라이선스 — 대상 세부영역 페이지 7절에 정정 문단을 두어 코드 MIT(f12)·README 의 Llama 2 파생 문구(f13)·HF 카드 '모든 체크포인트 MIT'(f14)를 충돌 그대로 병기하고 어느 쪽도 고르지 않았으며 출처 충돌 열린 질문에 연결했다. 다만 분리 주제 페이지 2026-09-30-area44-s7.md 본문은 이번 입력에 없어 그 문장을 직접 지우지 못했고, 7절에 '주제 페이지 문장은 이 대조로 바로잡는다'고 적은 뒤 후속 갱신을 additional_research_requests 에 요청했다(부분 이행).",
    "5절 제조 공장 — 'Figure AI 자체 발표로는 교차 확인하지 못했다'를 지우고 'Figure AI 자체 발표(2025-11-19 F.02 회고, 2026-06-30 F.03 첫 시연)가 같은 배치·착수를 설명하나, 같은 프로젝트 당사자 자료라 독립 확인은 아니다'로 바꿔 [추정] 벤더 주장과 각주 ref-1619·ref-1620·ref-1051 을 달았다.",
    "5절 제조 공장 예외·성과 — 표 칸과 서술에서 교대당 99% 초과 성공률·개입 0회를 '목표치(실측 아님)'로만 적고, 10/11개월 문장 뒤에 10개월은 BMW 보도자료 본문·11개월은 Figure CEO 인용문이라는 위치와 Figure 쪽 6·10·11개월 이정표를 덧붙였으며 기간을 하나로 정하지 않았다. oq-219 는 11절에서 열림 유지.",
    "5절 IMR-LLM — 제조 공장 사례를 별도로 추가하고 '연구 평가(로봇 팔 3대 단일 장면, 전문가 약 15분 수동 장면 작성, 반복 횟수 미보고)'이며 장기 운영 실적이 아니라고 밝혔고, 근거 없는 시작 조건·제약·완료·인계 칸은 '미확인'으로 두었다.",
    "5절 물류창고 — 산업부 M.AX 휴머노이드 과제(f38)를 로보티즈–BGF로지스 과제와 별도 문단으로 쓰고 같은 사업인지 미확인임을 밝혔으며, 기준일 '2025-11-24 등록'을 본문과 각주에 남겼다.",
    "9절 — 표에 도구 호출 실행 행을 더하고 '도구 호출로 로봇을 움직일 때의 경계' 소절을 두어 물리 비상정지·런타임 소프트웨어 정지는 연계 대상(로봇 자체 제어·설비 안전 제어)으로 짧게 적고, ROP 직접 범위는 읽기·실행 권한, 승인된 계획 대상 확인, 완료 판정, 세션 종료와 정지 절차 연결로 한정했다. MoveIt Pro 서술(f31~f33)은 모두 [추정] 벤더 주장, MCP 블로그(f30)는 '규범 명세가 아니라 프로젝트의 해설'로 밝혔다.",
    "f39~f46 — [의견] 문장 8건(5절 f41·f46, 6절 f39·f40, 7절 f42·f43, 8절 f44, 9절 f45) 모두 '이 위키의 의견으로는'으로 시작해 누구의 의견인지 밝혔다.",
    "이접 그래프 — 대상 세부영역 페이지 6절의 새 서술은 '이접 그래프(disjunctive graph)'로 쓰고 주제 페이지의 '선택 그래프'와 같은 용어임을 밝혔다. 분리 주제 페이지 2026-09-30-area44-s6.md 57행은 본문이 입력에 없어 직접 바꾸지 못했고 후속 갱신을 요청했다(부분 이행). 트랙 페이지 번역어는 고치지 않았다.",
    "쪽수 — IMR-LLM 의 ICRA 2026 쪽수와 SMART-LLM 의 IROS 2024 쪽수를 본문·각주에 쓰지 않았고, reference_updates 의 ref-090·ref-170 요약에서도 쪽수를 뺐다.",
    "판 미고정 출처 — 7절 본문에 ref-1611 은 'n1.7-release 브랜치 README(접근일 2026-10-12 기준)', ref-1616 은 'ROSA 위키 FAQ(릴리스에 고정되지 않은 문서, 접근일 2026-10-12 기준)'로 밝혔다.",
    "11절 — oq-216·oq-217·oq-219 는 '부분 근거'로만 연결하고 열림 유지, oq-218·oq-104 는 관련 근거만, oq-141 은 13. 대화형 기능의 신뢰·기반 쪽 질문으로 연결만 하고 상태를 바꾸지 않았다. 새 질문 4건은 브리프 문구대로 11절과 open_question_updates 에 등록했다.",
    "각주 — 13절을 다시 써서 다시 연 기존 출처 ref-090·ref-170·ref-092·ref-1051 의 접근일을 2026-10-12 로 고치고, 새 출처 ref-1607~ref-1621 은 브리프의 기관·제목·발행일(없으면 '미확인')·URL 그대로 정의했으며 프런트매터 sources 에 더했다.",
    "분량 초과 자동 분리: 44. 로봇 기반 모델·언어 모델 계획 본문 14,154자 > 기준 4,000자 → 4개 절을 주제 페이지로 옮김, 남은 본문 7,111자"
  ],
  "standards_updates": [
    {
      "name": "openpi (π0 계열 공개 구현)",
      "kind": "오픈소스",
      "org": "Physical Intelligence",
      "url": "https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/docs/remote_inference.md",
      "related_areas": [
        44
      ],
      "summary": "π0 계열 로봇 기반 모델의 공개 구현. 원격 추론 예시는 (action_horizon, action_dim) 형태의 행동 청크를 돌려주고 남은 행동을 개방 루프로 실행하도록 안내하며, 기반 체크포인트는 π0·π0-FAST·π0.5다(커밋 215abfb 기준, π0.7 없음).",
      "ref_id": "ref-1610"
    },
    {
      "name": "GR00T N1.7 (Isaac GR00T, Early Access)",
      "kind": "오픈소스",
      "org": "NVIDIA",
      "url": "https://github.com/NVIDIA/Isaac-GR00T/blob/n1.7-release/README.md",
      "related_areas": [
        44,
        59
      ],
      "summary": "NVIDIA 휴머노이드 로봇 기반 모델 GR00T N1.7 의 저장소(n1.7-release 브랜치, 접근일 2026-10-12 기준 EA 릴리스). 코드는 Apache 2.0 이고 가중치 사용 조건은 README 소개·License 절·3B 모델 카드·3B LICENSE 3.3절이 서로 다르게 적는다(GR00T N1 과 다른 판).",
      "ref_id": "ref-1611"
    }
  ]
}
```

### runs/2026-10-12-05/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md (7개 절)
- 분량 초과 자동 분리:
    - docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-10-12-area44-s7.md (2,705자)
    - docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md "11. 열린 질문" → docs/topics/2026/2026-10-12-area44-s11.md (1,985자)
    - docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-10-12-area44-s6.md (1,763자)
    - docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md "8. 대표 연구와 자료" → docs/topics/2026/2026-10-12-area44-s8.md (1,267자)
```

### runs/2026-10-12-05/pages/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md

```markdown
---
title: "44. 로봇 기반 모델·언어 모델 계획"
type: area
category: "L. AI·학습 기술"
area_no: 44
related_areas: [1, 4, 5, 12, 13, 24, 25, 26, 29, 31, 47, 54, 61, 62, 65]
tags: [VLA, 로봇 기반 모델, 언어 모델 계획, 교차 형태 학습, 불확실도 정렬, 다중 로봇 계획]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-10-12
sources: [ref-1045, ref-1046, ref-1047, ref-1048, ref-088, ref-092, ref-586, ref-090, ref-351, ref-1049, ref-170, ref-171, ref-1050, ref-1051, ref-1052, ref-1607, ref-1608, ref-1609, ref-1610, ref-1611, ref-1612, ref-1613, ref-1614, ref-1615, ref-1616, ref-1617, ref-1618, ref-1619, ref-1620, ref-1621]
last_run: 2026-10-12
version: 3
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

이번 조사에서 확인한 가정 사례는 처음 보는 가정집에서의 연구 평가다. [사실][^ref-1047] 제조 공장 사례는 도입 기업의 발표이고, 물류창고 사례는 국내 실증 계획이다. [추정] 벤더 주장[^ref-1051][^ref-1052] 제조 공장에는 언어 모델 다중 로봇 계획기를 로봇 팔 3대 장면에서 실물로 시험한 연구 평가 사례도 있다. [사실][^ref-170] 병원·상업 시설·실외 현장의 로봇 기반 모델·언어 모델 계획 적용 사례는 이번 조사에서 찾지 못했다.

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
| 예외·성과 | Figure 02가 BMW X3 3만 대 이상의 생산을 도왔다고 밝히나, 기간은 BMW 보도자료 본문의 10개월과 보도자료에 실린 Figure AI 최고경영자 인용문의 11개월로 엇갈린다. 교대당 99% 초과 성공률·교대당 개입 0회는 Figure AI가 밝힌 목표치(실측 아님)다. 복구 주체는 미확인 [추정] 벤더 주장[^ref-1051][^ref-1619] |

BMW 그룹은 2025년 스파턴버그 공장에 Figure AI의 휴머노이드 Figure 02를 배치해 용접 공정용 판금 부품 투입을 맡겼고, 이 로봇이 BMW X3 3만 대 이상의 생산을 도왔다고 밝힌다. [추정] 벤더 주장[^ref-1051] 같은 보도자료(2026-06-25) 안에는 10개월 동안 3만 대 이상 생산을 지원했다는 문장과 11개월 배치라는 문장이 함께 있어 기간을 하나로 정하지 않는다(11절 열린 질문). [추정] 벤더 주장[^ref-1051] 2026-10-12 재열람 기준으로 10개월은 보도자료 본문에, 11개월은 보도자료에 실린 Figure AI 최고경영자(Chief Executive Officer, CEO) 인용문에 있다. [추정] 벤더 주장[^ref-1051]

Figure AI의 2025-11-19 발표는 이 배치를 '11개월 배치'라 부르면서, 개발 착수 뒤 6개월 안에 공장에 납품·시험을 시작하고 10개월 안에 생산 라인 전면 배치를 시작했으며, 6개월 동안 매일 가동해 1,250시간 이상 가동했다고 적는다. [추정] 벤더 주장[^ref-1619] 이 세 기간은 기점·종점이 서로 달라 BMW 보도자료의 10개월·11개월 차이를 해소하지 못한다. [추정] 벤더 주장[^ref-1619][^ref-1051] 따라서 이 페이지는 기간을 하나로 정하지 않는다. 같은 Figure AI 발표에서 교대당 99% 초과 성공률과 교대당 개입 0회는 목표로 제시됐을 뿐 달성한 실측치로 보고되지 않았다. [추정] 벤더 주장[^ref-1619]

BMW 그룹은 또 후속 Figure 03이 스파턴버그에서 순서 공급(just in sequence) 물류 작업을 시작한다고 밝혔고(착수 발표), 이 로봇이 음성 대화 기능과 무선 충전을 갖췄다고 설명한다. [추정] 벤더 주장[^ref-1051] Figure AI 자체 발표(2025-11-19 F.02 회고, 2026-06-30 F.03 첫 시연)가 같은 배치·착수를 설명하나, 같은 프로젝트 당사자 자료라 독립 확인은 아니다. [추정] 벤더 주장[^ref-1619][^ref-1620][^ref-1051] Figure AI는 2026-06-30 발표에서 Figure 03이 스파턴버그 공장에서 물류 작업 흐름을 수행한 것을 첫 시연으로 설명하고, 자사 VLA인 Helix 02가 손·팔·몸통·발을 함께 제어해 무거운 대차를 끌었다고 적는다. [추정] 벤더 주장[^ref-1620] 이것은 첫 시연이며 지속 배치의 성과(가동률·인계 기록)가 아니다. [추정] 벤더 주장[^ref-1620]

**현장 유형:** 제조 공장

**사례:** 컨베이어에 공작물을 옮기는 로봇 팔 3대의 언어 모델 작업 계획(IMR-LLM 연구 평가)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 컨베이어에 옮기는 공작물 [사실][^ref-170] |
| 수행 자원 | 로봇 팔 3대(단일 장면), 장면 설명을 약 15분 걸려 손으로 작성해 입력한 전문가 [사실][^ref-170] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 반복 횟수는 보고되지 않았다. 복구 주체와 처리량·시간 영향은 미확인 [사실][^ref-170] |

IMR-LLM(2026-03)의 실물 시험은 컨베이어에 공작물을 옮기는 로봇 팔 3대의 단일 장면이었고, 전문가가 약 15분 걸려 장면 설명을 손으로 작성해 입력했으며, 반복 횟수는 보고되지 않았다. [사실][^ref-170] 이것은 연구 평가(로봇 팔 3대 단일 장면, 전문가 약 15분 수동 장면 작성, 반복 횟수 미보고)이며 장기 운영 실적이 아니다. [사실][^ref-170] 이 위키의 의견으로는, 연구 논문의 실물 시험은 사례 표에 장면 작성자·시뮬레이션 확인·복구 책임을 함께 적고 장기 운영 실적으로 표시하지 않아야 한다. [의견][^ref-170]

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

이와 별도로 산업통상부 보도자료(2025-11-24 등록)에 따르면 산업부와 서울대가 M.AX 얼라이언스 협력 업무협약(Memorandum of Understanding, MOU)을 맺었고, 지원 과제 표의 휴머노이드 분과 과제는 '휴머노이드 AI 파운데이션 모델 개발'(2025~2028년, 484억 원, 핵심 연구진 장병탁·박재흥 서울대 교수)이다. [사실][^ref-1621] 이 과제가 위 로보티즈–BGF로지스 과제와 같은 사업인지는 확인되지 않았고, 이 보도자료에도 자동화율 80%·성공률 90%의 실측 결과는 없다(11절 열린 질문). [사실][^ref-1621]

이 위키의 의견으로는, 벤더·도입 기업 발표는 목표·기간·첫 시연과 실측 성과를 다른 열로 나누고, 운영 기간의 기점·종점, 성공률의 분모, 개입·실패 기록, 인계 신호가 공개될 때까지 도입 성과 지표(Key Performance Indicator, KPI) 비교에 쓰지 않아야 하며, 국내 실증 목표(자동화율 80%·성공률 90%)도 같다. [의견][^ref-1619][^ref-1620][^ref-1051][^ref-1621]

## 6. 대표 접근법과 기술

대표 접근법은 여러 로봇 데이터로 범용 정책을 학습하는 로봇 기반 모델과, 언어 모델 계획을 로봇 능력·기호 계획기·사람 확인에 묶어 믿을 수 있게 하는 방법으로 나뉜다. [추정][^ref-1048][^ref-092][^ref-351]

자세한 내용은 주제 페이지 [44. 로봇 기반 모델·언어 모델 계획 — 대표 접근법과 기술](../../topics/2026/2026-10-12-area44-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

이번 조사에서 확인한 관련 자원은 공개 데이터셋(Open X-Embodiment), 공개 VLA 모델(OpenVLA, GR00T N1), ROS용 언어 모델 에이전트(ROSA), 계획 표현 언어인 계획 도메인 정의 언어(Planning Domain Definition Language, PDDL)다. [사실][^ref-1048][^ref-1046][^ref-1049][^ref-171][^ref-092]

자세한 내용은 주제 페이지 [44. 로봇 기반 모델·언어 모델 계획 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-12-area44-s7.md)에 있다.

## 8. 대표 연구와 자료

대표 자료는 로봇 기반 모델 계열과 언어 모델 계획 계열의 논문, 그리고 국내 협력 동향 기사다. [사실][^ref-1045][^ref-088][^ref-1050]

자세한 내용은 주제 페이지 [44. 로봇 기반 모델·언어 모델 계획 — 대표 연구와 자료](../../topics/2026/2026-10-12-area44-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

ROP는 언어 모델 계획을 검증하고 사람 확인을 거쳐 이종 로봇에 내리는 계층을 맡고, VLA의 저수준 조작 정책은 로봇 제조사·모델 제공자에게 연계하는 것으로 보인다. [추정][^ref-092][^ref-351][^ref-1045]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 로봇 기반 모델을 탑재한 로봇을 포함한 이종 로봇의 가능한 기능·실행 조건·완료·실패 확인을 받고, 검증된 계획을 내리는 인터페이스 [추정][^ref-088][^ref-090][^ref-171] | 연계 대상: VLA·로봇 기반 모델이 카메라 영상에서 관절·그리퍼 행동을 직접 생성하는 저수준 조작 정책(로봇 제조사·모델 제공자) [추정][^ref-1045][^ref-1046][^ref-1047][^ref-1049] |
| 로봇 자체 지능·제어(언어 모델 도구 호출 실행) | 이 위키의 의견으로는 도구 호출의 읽기·실행 권한 구분, 실행 대상과 승인된 계획의 대조, 물리적 완료 판정, 세션 종료와 정지 절차의 연결 [의견][^ref-1617][^ref-1618] | 연계 대상: 물리적 비상 정지와 로봇 런타임의 소프트웨어 정지(로봇 자체 제어·설비 안전 제어) [추정] 벤더 주장[^ref-1618] |

ROP가 직접 맡을 범위는 언어 모델이 만든 작업 분해·배정 계획을 기호 계획기·제약 검사로 검증하는 계층, 불확실할 때 사람에게 확인을 요청하는 절차, 이종 로봇에 계획을 내리는 인터페이스이며, 이는 분류 원문 C. 채팅 기반 구성·운영 주석의 '사람이 확인·승인한 계획만 실행' 원칙과 같은 방향이다. [추정][^ref-092][^ref-586][^ref-351]

IMR-LLM처럼 공정 트리를 따라 실행 가능한 저수준 로봇 프로그램까지 생성하는 연구도 있으나, 그 부분은 로봇 자체 제어에 닿으므로 ROP에서는 연계 대상 문맥으로 본다. [추정][^ref-170] 이 경계는 제품 전략에 따라 이동할 수 있으며, 분류 원문은 '이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다'고 적는다([범위 경계](../../about/scope-boundary.md)).

### 도구 호출로 로봇을 움직일 때의 경계(2026-10-12 갱신)

언어 모델이 모델 컨텍스트 프로토콜([Model Context Protocol, MCP](../../glossary/model-context-protocol.md)) 같은 도구 호출로 로봇을 움직이는 구성에서도 위 경계가 적용된다. MCP 공식 블로그(2026-03-16)는 도구 어노테이션(readOnlyHint·destructiveHint 등)이 위험을 알리는 힌트일 뿐 실행 강제 수단이 아니며, 확실한 보장이 필요하면 네트워크 통제나 샌드박스로 해야 한다고 설명한다. 이 글은 규범 명세가 아니라 프로젝트의 해설이며, 위키가 앞서 정리한 MCP 명세 서술([13. 대화형 기능의 신뢰·기반 — 대표 접근법과 기술](../../topics/2026/2026-09-29-area13-s6.md))을 보완한다. [사실][^ref-1617]

PickNik의 MoveIt Pro MCP 서버 문서(Version 10)는 공유되는 배포(deployment) MCP 키는 읽기 전용이고, 로봇 동작은 호스트 사용자 세션에서 기존 Objective를 시작·취소하는 것으로만 한정된다고 설명한다. [추정] 벤더 주장[^ref-1618] 같은 문서는 서버가 별도의 실행 확인 프롬프트를 추가하지 않고, 도구 승인은 MCP 클라이언트 설정에 달려 있으며 클라이언트가 자동 승인할 수도 있다고 적는다. [추정] 벤더 주장[^ref-1618] 또 run_objective로 시작한 로봇은 세션이 끝나도 계속 움직일 수 있고, cancel_objective는 'best effort'일 뿐 비상 정지가 아니며, MCP 취소·소프트웨어 정지는 물리적 비상 정지를 대체하지 않는다고 적는다. [추정] 벤더 주장[^ref-1618] ROSA FAQ도 물리적 상호작용은 사용자가 만든 맞춤 도구로만 가능하고, 상태·능력 확인과 안전 검사를 그 도구 안에 넣으라고 권고한다(7절). [사실][^ref-1616]

연계 대상: 물리적 비상 정지와 로봇 런타임의 소프트웨어 정지는 로봇 자체 지능·제어와 설비 안전 제어 쪽(로봇 제조사·설비 공급자)이 맡는다. [추정] 벤더 주장[^ref-1618] 이 위키의 의견으로는, ROP가 직접 맡는 것은 언어 모델 도구 호출에 대한 읽기·실행 권한 구분, 실행 대상이 승인된 계획 리비전·목표 식별자(goal id)와 맞는지의 확인, 물리적 완료 판정, 세션 종료를 별도 정지 절차에 연결하는 일로 한정하며, 어노테이션 힌트나 클라이언트 자동 승인에 기대지 않아야 한다. [의견][^ref-1617][^ref-1618][^ref-1616]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 로봇 능력 표현, 대화형 지시, 계획·배정, 계획 검증, 현장 유형 영역과 이어진다. [추정][^ref-1046][^ref-090]

자세한 내용은 주제 페이지 [44. 로봇 기반 모델·언어 모델 계획 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area44-s10.md)에 있다.

## 11. 열린 질문

(상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-07) 로봇 기반 모델(VLA)을 탑재해 명시적 스킬 목록 없이 학습된 범용 기능을 가진 로봇의 능력을 플랫폼의 능력 모델에 어떻게 등록·기술하고 검증할 것인가?

자세한 내용은 주제 페이지 [44. 로봇 기반 모델·언어 모델 계획 — 열린 질문](../../topics/2026/2026-10-12-area44-s11.md)에 있다.

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
[^ref-092]: Liu, B., Jiang, Y., Zhang, X. 외 (arXiv), LLM+P: Empowering Large Language Models with Optimal Planning Proficiency, 2023-04-22, https://arxiv.org/abs/2304.11477, 접근일 2026-10-12
[^ref-586]: Kambhampati, S., Valmeekam, K., Guan, L. 외 (ICML 2024, arXiv), LLMs Can't Plan, But Can Help Planning in LLM-Modulo Frameworks, 2024-02-02, https://arxiv.org/abs/2402.01817, 접근일 2026-09-30
[^ref-090]: Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. (arXiv), SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models, 2023-09-18, https://arxiv.org/abs/2309.10062, 접근일 2026-10-12
[^ref-351]: Ren, A. Z., Dixit, A., Bodrova, A. 외 (CoRL 2023, arXiv), Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners, 2023-07-04, https://arxiv.org/abs/2307.01928, 접근일 2026-09-30
[^ref-1049]: NVIDIA (Bjorck, J., Castañeda, F. 외, arXiv), GR00T N1: An Open Foundation Model for Generalist Humanoid Robots, 2025-03-18, https://arxiv.org/abs/2503.14734, 접근일 2026-09-30
[^ref-170]: Su, X., Xu, J., van Kaick, O., Xu, K., & Hu, R. (arXiv), IMR-LLM: Industrial Multi-Robot Task Planning and Program Generation using Large Language Models, 2026-03-03, https://arxiv.org/abs/2603.02669, 접근일 2026-10-12
[^ref-171]: NASA Jet Propulsion Laboratory (nasa-jpl), ROSA — README, 미확인, https://github.com/nasa-jpl/rosa, 접근일 2026-09-30
[^ref-1050]: 지디넷코리아, K-휴머노이드 연합, 출범 3주 만에 협약 4건 성과, 2025-05-01, https://zdnet.co.kr/view/?no=20250501140356, 접근일 2026-09-30
[^ref-1051]: BMW Group, BMW Group advances the use of Physical AI in production with Figure 03 project in Spartanburg, 2026-06-25, https://www.press.bmwgroup.com/global/article/detail/T0458778EN/bmw-group-advances-the-use-of-physical-ai-in-production-with-figure-03-project-in-spartanburg?language=en, 접근일 2026-10-12
[^ref-1052]: 헬로티, VLA 이식한 로보티즈 'AI 워커', 물류 현장 난제 해결사로 전격 투입, 2025-11-26, https://www.hellot.net/news/article.html?no=107567, 접근일 2026-09-30
[^ref-1616]: NASA Jet Propulsion Laboratory (nasa-jpl), FAQ · nasa-jpl/rosa Wiki, 미확인, https://github.com/nasa-jpl/rosa/wiki/FAQ, 접근일 2026-10-12
[^ref-1617]: Model Context Protocol (Hungerford, O., Morrow, S., & Chang, L.), Tool Annotations as Risk Vocabulary: What Hints Can and Can't Do, 2026-03-16, https://blog.modelcontextprotocol.io/posts/2026-03-16-tool-annotations/, 접근일 2026-10-12
[^ref-1618]: PickNik Robotics, Connect an AI Assistant with the MCP Server (MoveIt Pro 문서 Version 10), 미확인, https://docs.picknik.ai/how_to/programmatic_sdks/mcp_server/, 접근일 2026-10-12
[^ref-1619]: Figure AI, F.02 Contributed to the Production of 30,000 Cars at BMW, 2025-11-19, https://www.figure.ai/news/production-at-bmw, 접근일 2026-10-12
[^ref-1620]: Figure AI, F.03 Arrives at BMW, 2026-06-30, https://www.figure.ai/news/f-03-at-bmw, 접근일 2026-10-12
[^ref-1621]: 산업통상부, 서울대와 M.AX 얼라이언스가 손잡고 휴머노이드, 자율주행차, AI팩토리에 탑재될 AI 모델 공동 개발한다., 2025-11-24, https://www.motir.go.kr/kor/article/ATCL3f49a5a8c/171238/view, 접근일 2026-10-12
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

### runs/2026-10-12-05/pages/topics/2026/2026-10-12-area44-s7.md

```markdown
---
title: "44. 로봇 기반 모델·언어 모델 계획 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "L. AI·학습 기술"
primary_area_no: 44
related_areas: [1, 4, 5, 12, 13, 24, 25, 26, 29, 31, 47, 54, 61, 62, 65]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-092, ref-1046, ref-1048, ref-1049, ref-1608, ref-1609, ref-1610, ref-1611, ref-1612, ref-1613, ref-1616, ref-171]
last_run: 2026-10-12
version: 1
split_from: docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md#7
---

[홈](../../index.md) › [주제](../index.md) › 44. 로봇 기반 모델·언어 모델 계획 — 관련 표준·프레임워크·오픈소스

# 44. 로봇 기반 모델·언어 모델 계획 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이번 조사에서 확인한 관련 자원은 공개 데이터셋(Open X-Embodiment), 공개 VLA 모델(OpenVLA, GR00T N1), ROS용 언어 모델 에이전트(ROSA), 계획 표현 언어인 계획 도메인 정의 언어(Planning Domain Definition Language, PDDL)다. [사실][^ref-1048][^ref-1046][^ref-1049][^ref-171][^ref-092]
- 이 페이지는 [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이번 조사에서 확인한 관련 자원은 공개 데이터셋(Open X-Embodiment), 공개 VLA 모델(OpenVLA, GR00T N1), ROS용 언어 모델 에이전트(ROSA), 계획 표현 언어인 계획 도메인 정의 언어(Planning Domain Definition Language, PDDL)다. [사실][^ref-1048][^ref-1046][^ref-1049][^ref-171][^ref-092]


### 2026-10-12 갱신: 공개 VLA 배포물의 입출력과 사용 조건

아래는 공개 문서의 문구를 대조한 것이며 상용 사용 가능 여부에 대한 법적 판단이 아니다. 사용 조건의 적용 판단은 [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) 쪽 연계 대상이다.

**OpenVLA 사용 조건(정정).** 연결된 주제 페이지 표 아래의 'OpenVLA의 라이선스는 확인하지 못했다'는 다음 문서 대조로 바로잡는다. OpenVLA 공식 저장소(고정 커밋 c8f03f4)의 코드 라이선스는 MIT다. [사실][^ref-1608] 같은 저장소 README는 사전학습 모델이 기반 모델의 제약을 물려받을 수 있다고 적는다. [사실][^ref-1608] 이어서 README는 두 사전학습 모델이 Llama 2에서 파생돼 Llama Community License를 따른다고 단정형으로 적는다. [사실][^ref-1608] 반면 Hugging Face 모델 카드는 모든 OpenVLA 체크포인트와 학습 코드가 MIT 라이선스로 공개된다고 적고, 현재 main 판(커밋 47a0ec7)도 같은 문구다. [사실][^ref-1609] 두 문서는 같은 개발팀 자료라 어느 쪽이 맞는지 문서만으로 정할 수 없으며, 이 페이지는 어느 쪽도 고르지 않는다(11절 열린 질문). [사실][^ref-1608][^ref-1609]

**GR00T N1.7(GR00T N1과 다른 판).** NVIDIA Isaac GR00T 저장소의 n1.7-release 브랜치 README(접근일 2026-10-12 기준)는 GR00T N1.7을 얼리 액세스(Early Access, EA) 릴리스로 명시하고, 정식(General Availability, GA) 릴리스 전까지 지원·안정성 보장이 제한되며 상용 지원을 포함한 운영 배치는 GA 대상이라고 적는다. [사실][^ref-1611] 같은 README의 License 절은 코드는 Apache 2.0, 모델 가중치는 NVIDIA Open Model License로 구분한다. [사실][^ref-1611] 그런데 같은 README의 소개 문단은 GR00T N1.7이 Apache 2.0으로 'fully commercially licensable'하다고 적어, License 절과 가중치 저장소 LICENSE와 맞지 않는다. [추정] 벤더 주장[^ref-1611][^ref-1612] Hugging Face nvidia/GR00T-N1.7-3B 저장소의 LICENSE 파일(커밋 6949d5d)은 NVIDIA License 표제 아래 3.3절에서 저작물과 파생물을 연구·평가 목적의 비상업 용도로만 쓸 수 있게 하고, NVIDIA와 그 계열사의 상업적 사용은 예외로 둔다. [사실][^ref-1612] 같은 저장소의 모델 카드는 NVIDIA Open Model License와 상업·비상업 사용 준비를 적으며, 어느 문서가 우선하는지는 문서에 적혀 있지 않다. [사실][^ref-1611][^ref-1612] 정리하면 GR00T N1.7은 EA 릴리스이고 코드는 Apache 2.0이며, 가중치 사용 조건은 문서마다 다르다(README 소개·License 절·3B 카드·3B LICENSE 3.3절). [사실][^ref-1611][^ref-1612] 연결된 주제 페이지 표의 GR00T N1 행은 이 근거로 고치지 않는다.

**입출력 계약.** OpenVLA 모델 카드에 따르면 OpenVLA는 언어 지시와 카메라 영상 한 장을 입력받아 정규화된 7자유도 엔드이펙터 변위(x, y, z, roll, pitch, yaw, gripper)를 출력하며, 실제 로봇에서 실행하려면 로봇·데이터셋별로 계산한 통계로 역정규화해야 한다. [사실][^ref-1609] π0 계열 공개 구현 openpi의 원격 추론 예시(커밋 215abfb)는 정책 서버가 (action_horizon, action_dim) 형태의 행동 청크(action chunk)를 돌려준다고 설명한다. [사실][^ref-1610] 같은 예시는 다음 추론 호출 전까지 예측된 행동 청크의 나머지 행동을 개방 루프(open-loop)로 실행하도록 안내하며, 이는 예시 동작 설명이지 명령 수락·작업 완료 상태나 안전 정지 기능의 근거가 아니다. [사실][^ref-1610] openpi README가 제공하는 기반 체크포인트는 π0, π0-FAST, π0.5뿐이며 π0.7 가중치는 목록에 없다. [사실][^ref-1610]

**ROSA의 물리 실행 조건.** ROSA 위키 FAQ(릴리스에 고정되지 않은 문서, 접근일 2026-10-12 기준)는 핵심 ROSA 에이전트가 텍스트 상호작용에 한정되어 물리 세계와 상호작용할 수 없으며, 물리적 상호작용에는 사용자가 맞춤 도구와 프롬프트를 만들어야 한다고 설명한다. [사실][^ref-1616] 같은 FAQ는 로봇 능력을 넘는 행동을 막으려면 맞춤 도구 안에 실행 전 로봇 상태·능력 확인 제약과 매개변수 검증·행동 제한 같은 안전 검사를 직접 넣으라고 권고하며, 이는 자동으로 제공되는 기능이 아니라 권고다. [사실][^ref-1616]

**이 위키의 의견.** 이 위키의 의견으로는, VLA 탑재 로봇의 능력 등록에는 모델·가중치 리비전(해시), 로봇 기종·카메라, 좌표계·행동 단위·제어 모드, 정규화 통계, 행동 청크의 형태·관측 시각·유효기간·중단 조건, 허용 과제와 완료 판정을 두고, 명령 완료는 로봇 외부 상태로 확인하는 것이 필요해 보인다. 이는 ROP 설계 제안이며 표준이 아니다. [의견][^ref-1609][^ref-1610][^ref-1613] 또한 이 위키의 의견으로는, 공개 VLA를 도입할 때 코드 라이선스와 가중치 사용 조건을 따로 확인하고, README 소개 문구만으로 상용 허용을 확정하지 않으며, 문서끼리 충돌하는 조건은 배포자에게 서면으로 확인할 항목으로 남겨야 한다(법률 판단이 아니다). [의견][^ref-1608][^ref-1609][^ref-1611][^ref-1612]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-092]: Liu, B., Jiang, Y., Zhang, X. 외 (arXiv), LLM+P: Empowering Large Language Models with Optimal Planning Proficiency, 2023-04-22, https://arxiv.org/abs/2304.11477, 접근일 2026-10-12
[^ref-1046]: Kim, M. J., Pertsch, K., Karamcheti, S. 외 (arXiv), OpenVLA: An Open-Source Vision-Language-Action Model, 2024-06-13, https://arxiv.org/abs/2406.09246, 접근일 2026-09-30
[^ref-1048]: Open X-Embodiment Collaboration (arXiv), Open X-Embodiment: Robotic Learning Datasets and RT-X Models, 2023-10-13, https://arxiv.org/abs/2310.08864, 접근일 2026-09-30
[^ref-1049]: NVIDIA (Bjorck, J., Castañeda, F. 외, arXiv), GR00T N1: An Open Foundation Model for Generalist Humanoid Robots, 2025-03-18, https://arxiv.org/abs/2503.14734, 접근일 2026-09-30
[^ref-1608]: OpenVLA 개발팀 (openvla/openvla GitHub), OpenVLA — README 및 LICENSE (커밋 c8f03f4), 미확인, https://github.com/openvla/openvla/blob/c8f03f48af692657d3060c19588038c7220e9af9/README.md, 접근일 2026-10-12
[^ref-1609]: OpenVLA 개발팀 (Hugging Face openvla/openvla-7b), openvla/openvla-7b — Model Card, 미확인, https://huggingface.co/openvla/openvla-7b, 접근일 2026-10-12
[^ref-1610]: Physical Intelligence (Physical-Intelligence/openpi GitHub), openpi — README, docs/remote_inference.md, LICENSE (커밋 215abfb), 미확인, https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/docs/remote_inference.md, 접근일 2026-10-12
[^ref-1611]: NVIDIA (NVIDIA/Isaac-GR00T GitHub), Isaac GR00T N1.7 — README 및 LICENSE (n1.7-release 브랜치), 미확인, https://github.com/NVIDIA/Isaac-GR00T/blob/n1.7-release/README.md, 접근일 2026-10-12
[^ref-1612]: NVIDIA (Hugging Face nvidia/GR00T-N1.7-3B), GR00T-N1.7-3B — LICENSE 및 모델 카드, 미확인, https://huggingface.co/nvidia/GR00T-N1.7-3B/blob/6949d5dfab2e872283e8cca8106ac3af8adcf39b/LICENSE, 접근일 2026-10-12
[^ref-1613]: Physical Intelligence (Ai, B. 외, arXiv), π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities, 2026-04-16, https://arxiv.org/abs/2604.15483, 접근일 2026-10-12
[^ref-1616]: NASA Jet Propulsion Laboratory (nasa-jpl), FAQ · nasa-jpl/rosa Wiki, 미확인, https://github.com/nasa-jpl/rosa/wiki/FAQ, 접근일 2026-10-12
[^ref-171]: NASA Jet Propulsion Laboratory (nasa-jpl), ROSA — README, 미확인, https://github.com/nasa-jpl/rosa, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-05 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-05 | 44. 로봇 기반 모델·언어 모델 계획 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-10-12-05/pages/topics/2026/2026-10-12-area44-s11.md

```markdown
---
title: "44. 로봇 기반 모델·언어 모델 계획 — 열린 질문"
type: topic
category: "L. AI·학습 기술"
primary_area_no: 44
related_areas: [1, 4, 5, 12, 13, 24, 25, 26, 29, 31, 47, 54, 61, 62, 65]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-090, ref-1051, ref-1607, ref-1609, ref-1610, ref-1613, ref-1614, ref-1618, ref-1619, ref-1621, ref-170]
last_run: 2026-10-12
version: 1
split_from: docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md#11
---

[홈](../../index.md) › [주제](../index.md) › 44. 로봇 기반 모델·언어 모델 계획 — 열린 질문

# 44. 로봇 기반 모델·언어 모델 계획 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- (상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-07) 로봇 기반 모델(VLA)을 탑재해 명시적 스킬 목록 없이 학습된 범용 기능을 가진 로봇의 능력을 플랫폼의 능력 모델에 어떻게 등록·기술하고 검증할 것인가?
- 이 페이지는 [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

(상태: 열림 · 제기 2026-09-30 · 실행 2026-09-30-07) 로봇 기반 모델(VLA)을 탑재해 명시적 스킬 목록 없이 학습된 범용 기능을 가진 로봇의 능력을 플랫폼의 능력 모델에 어떻게 등록·기술하고 검증할 것인가?


### 2026-10-12 갱신: 부분 근거와 새 질문

아래 기존 질문에는 부분 근거만 더했으며, 모두 열림 상태를 유지한다.

- **oq-216** (상태: 열림) 부분 근거: 배포물마다 입출력이 다르다. OpenVLA는 정규화된 7자유도 엔드이펙터 변위를 내고 로봇·데이터셋별 역정규화가 필요하며, openpi 원격 추론은 행동 청크를 돌려주고 남은 행동을 개방 루프로 실행하도록 안내한다(7절). [사실][^ref-1609][^ref-1610] π0.7 보고서는 프롬프트로 관절·엔드이펙터 제어 모드를 고른다고 설명한다(8절). [추정] 벤더 주장[^ref-1613] 공통 능력 등록 표준과 적합성 시험은 확인하지 못했다.
- **oq-217** (상태: 열림) 부분 근거: 확인한 공개 평가는 SMART-LLM(AI2-THOR 지시 36개, 로봇 1~4대), IMR-Bench(장면 23개·제조 작업 50개, 장면당 로봇 1~7대), S-ATLAS(AI2-THOR 검증 시나리오 110개, 로봇 1·3·10·15대)이고, 실물 시험으로는 IMR-LLM의 로봇 팔 3대 단일 장면을 확인했다(5절·6절). [사실][^ref-090][^ref-170][^ref-1607] VLA 쪽에는 입력 교란 견고성 벤치마크 LIBERO-Plus가 있다(8절). [사실][^ref-1614] 설비·안전·시간창을 함께 다루는 공통 기준은 확인하지 못했다.
- **oq-218** (상태: 열림) 관련 근거: 산업부 M.AX 휴머노이드 AI 파운데이션 모델 과제 보도자료(2025-11-24)에도 실측 결과는 없다(5절). [사실][^ref-1621]
- **oq-219** (상태: 열림) 부분 근거: 10개월은 BMW 보도자료 본문, 11개월은 Figure AI 최고경영자 인용문에 있고, Figure AI 발표는 6·10·11개월의 다른 기간 축을 적는다. 기점·종점이 없어 충돌은 해소되지 않았다(5절). [추정] 벤더 주장[^ref-1051][^ref-1619]
- **oq-104** 관련 근거: π0.7 보고서의 240 ms(50 Hz 기준)는 학습 중 모사한 지연이며 측정된 추론 지연이 아니다(8절). [추정] 벤더 주장[^ref-1613]
- **oq-141**([13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md) 쪽 승인 관문 위치 질문) 관련 근거: MoveIt Pro MCP 서버는 확인 프롬프트를 두지 않고 도구 승인을 MCP 클라이언트 설정에 맡긴다(9절). 이 페이지에서 상태를 바꾸지 않는다. [추정] 벤더 주장[^ref-1618]

이번에 새로 올린 질문(전체 목록은 [열린 질문](../../open-questions.md)):

- (상태: 열림 · 제기 2026-10-12 · 실행 2026-10-12-05) 언어 모델 다중 로봇 계획의 검증이 기대는 가정(사람이 준 도메인 판, i.i.d. 시나리오, 무오류 스킬 실행)을 런타임에서 누가 감시하고, 가정이 깨졌을 때 어떤 계획을 중단·재검증할 것인가?
- (상태: 열림 · 제기 2026-10-12 · 실행 2026-10-12-05) 원격 VLA 정책의 행동 청크(개방 루프 실행) 유효기간과, 도구 세션이 끝난 뒤에도 로봇이 움직일 수 있는 MCP 실행의 안전한 정지 계약을 어떻게 결합할 것인가?
- (상태: 열림 · 제기 2026-10-12 · 실행 2026-10-12-05) 출처 충돌: OpenVLA 공개 가중치의 사용 조건은 저장소 README(Llama 2 파생이라 Llama Community License 가 적용될 수 있음)와 Hugging Face 모델 카드(모든 체크포인트 MIT) 가운데 어느 쪽인가?
- (상태: 열림 · 제기 2026-10-12 · 실행 2026-10-12-05) 출처 충돌: GR00T N1.7 가중치의 상업적 사용 가능 여부는 README 소개(Apache 2.0 으로 상용 가능), README License 절·3B 모델 카드(NVIDIA Open Model License, 상업·비상업 사용 준비), 3B 가중치 저장소 LICENSE 3.3절(NVIDIA·계열사 외 비상업 한정) 가운데 어느 문서가 정하는가?

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-090]: Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. (arXiv), SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models, 2023-09-18, https://arxiv.org/abs/2309.10062, 접근일 2026-10-12
[^ref-1051]: BMW Group, BMW Group advances the use of Physical AI in production with Figure 03 project in Spartanburg, 2026-06-25, https://www.press.bmwgroup.com/global/article/detail/T0458778EN/bmw-group-advances-the-use-of-physical-ai-in-production-with-figure-03-project-in-spartanburg?language=en, 접근일 2026-10-12
[^ref-1607]: Wang, J., He, G., & Kantaros, Y. (IEEE Robotics and Automation Letters 10(1)), Probabilistically Correct Language-based Multi-Robot Planning using Conformal Prediction, 2025-01, https://arxiv.org/abs/2402.15368, 접근일 2026-10-12
[^ref-1609]: OpenVLA 개발팀 (Hugging Face openvla/openvla-7b), openvla/openvla-7b — Model Card, 미확인, https://huggingface.co/openvla/openvla-7b, 접근일 2026-10-12
[^ref-1610]: Physical Intelligence (Physical-Intelligence/openpi GitHub), openpi — README, docs/remote_inference.md, LICENSE (커밋 215abfb), 미확인, https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/docs/remote_inference.md, 접근일 2026-10-12
[^ref-1613]: Physical Intelligence (Ai, B. 외, arXiv), π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities, 2026-04-16, https://arxiv.org/abs/2604.15483, 접근일 2026-10-12
[^ref-1614]: Fei, S., Wang, S., Shi, J. 외 (arXiv), LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models, 2025-10-15, https://arxiv.org/abs/2510.13626, 접근일 2026-10-12
[^ref-1618]: PickNik Robotics, Connect an AI Assistant with the MCP Server (MoveIt Pro 문서 Version 10), 미확인, https://docs.picknik.ai/how_to/programmatic_sdks/mcp_server/, 접근일 2026-10-12
[^ref-1619]: Figure AI, F.02 Contributed to the Production of 30,000 Cars at BMW, 2025-11-19, https://www.figure.ai/news/production-at-bmw, 접근일 2026-10-12
[^ref-1621]: 산업통상부, 서울대와 M.AX 얼라이언스가 손잡고 휴머노이드, 자율주행차, AI팩토리에 탑재될 AI 모델 공동 개발한다., 2025-11-24, https://www.motir.go.kr/kor/article/ATCL3f49a5a8c/171238/view, 접근일 2026-10-12
[^ref-170]: Su, X., Xu, J., van Kaick, O., Xu, K., & Hu, R. (arXiv), IMR-LLM: Industrial Multi-Robot Task Planning and Program Generation using Large Language Models, 2026-03-03, https://arxiv.org/abs/2603.02669, 접근일 2026-10-12

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-05 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-05 | 44. 로봇 기반 모델·언어 모델 계획 의 "열린 질문" 절에서 분리 |
```

### runs/2026-10-12-05/pages/topics/2026/2026-10-12-area44-s6.md

```markdown
---
title: "44. 로봇 기반 모델·언어 모델 계획 — 대표 접근법과 기술"
type: topic
category: "L. AI·학습 기술"
primary_area_no: 44
related_areas: [1, 4, 5, 12, 13, 24, 25, 26, 29, 31, 47, 54, 61, 62, 65]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-090, ref-092, ref-1048, ref-1607, ref-170, ref-351]
last_run: 2026-10-12
version: 1
split_from: docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md#6
---

[홈](../../index.md) › [주제](../index.md) › 44. 로봇 기반 모델·언어 모델 계획 — 대표 접근법과 기술

# 44. 로봇 기반 모델·언어 모델 계획 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 대표 접근법은 여러 로봇 데이터로 범용 정책을 학습하는 로봇 기반 모델과, 언어 모델 계획을 로봇 능력·기호 계획기·사람 확인에 묶어 믿을 수 있게 하는 방법으로 나뉜다. [추정][^ref-1048][^ref-092][^ref-351]
- 이 페이지는 [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

대표 접근법은 여러 로봇 데이터로 범용 정책을 학습하는 로봇 기반 모델과, 언어 모델 계획을 로봇 능력·기호 계획기·사람 확인에 묶어 믿을 수 있게 하는 방법으로 나뉜다. [추정][^ref-1048][^ref-092][^ref-351]


### 2026-10-12 갱신: 다중 로봇 언어 모델 계획의 평가 조건과 보장의 전제

이 소절은 세 다중 로봇 계획 연구의 평가 규모·실패 양상과, 계획 검증이 기대는 입력 전제를 2026-10-12에 원문에서 확인한 것이다.

**SMART-LLM.** SMART-LLM의 평가 데이터셋은 AI2-THOR 가정 시뮬레이션의 고수준 지시 36개로 구성되며, 과제마다 로봇 1~4대를 쓴다. [사실][^ref-090] 어떤 로봇도 필요한 스킬을 갖지 않은 불가능 과제 시험에서 GPT-4·Claude-3 기반 구성은 배정 계획을 만들지 않았고, GPT-3.5·Llama2 기반 구성은 과제에 맞지 않는 로봇이 들어간 배정 계획을 만들었다. [사실][^ref-090] 이 시험은 표 I 집계에 들어 있지 않고 과제 수도 보고되지 않았다. [사실][^ref-090]

**IMR-LLM.** IMR-Bench는 생산 라인 설계 전문가가 실제 산업 현장에서 수집·각색한 장면 23개(장면당 로봇 1~7대)를 바탕으로 제조 작업 50개를 구성한 벤치마크이며, KunWu 플랫폼 위에 만들어졌다. [사실][^ref-170] IMR-LLM 구현은 언어 모델이 구성을 도운 이접 그래프(disjunctive graph)의 일정을 휴리스틱 선입선출(First-In-First-Out, FIFO) 알고리즘으로 푼다. [사실][^ref-170] 저자는 복잡한 다중 로봇 작업에서 성공률이 떨어진 주된 이유로 언어 모델의 잘못된 분해·배정(예: 팔이 닿지 않는 로봇에 작업 배정)을 들었으나, 그 빈도는 정량화하지 않았다. [사실][^ref-170] 연결된 주제 페이지의 '선택 그래프(disjunctive graph)'는 같은 용어이며, 이 위키는 이번 갱신부터 '이접 그래프'로 쓴다.

**기호 계획기 결합의 입력 전제.** LLM+P는 행동의 전제·효과를 담은 계획 도메인 정의 언어(Planning Domain Definition Language, PDDL) 도메인 파일을 사람 전문가가 제공한다는 것을 입력 전제로 두며, 언어 모델은 문제(problem) 파일만 만든다. [사실][^ref-092]

**등각 예측 기반 다중 로봇 계획.** [등각 예측](../../glossary/conformal-prediction.md)(conformal prediction) 기반 다중 로봇 언어 계획기 S-ATLAS(IEEE RA-L, 2025-01)의 임무 성공률 보장은 보정(calibration) 시나리오와 시험 시나리오가 독립·동일분포(independent and identically distributed, i.i.d.)라는 조건 아래에서만 성립한다. [사실][^ref-1607] 임무 완료율 정리는 계획 실행에 오류가 없다는 전제를 두며, 증명은 예측 집합이 단일 원소가 아닐 때 사람이 정확한 도움을 준다는 것도 전제한다. [사실][^ref-1607] S-ATLAS는 AI2-THOR 시뮬레이션의 검증 시나리오 110개로 평가했고 로봇 수는 1·3·10·15대였으며, 열람한 본문에서 실물 로봇 실험은 확인되지 않았다. [사실][^ref-1607]

**이 위키의 의견.** 이 위키의 의견으로는, 스킬 목록이 없거나 로봇 능력 밖인 요청을 계획기가 거절하는지(또는 닿지 않는 로봇에 배정하지 않는지)를 일반 성공률과 별도의 수용 시험 항목으로 두어야 한다. [의견][^ref-090][^ref-170] 또한 이 위키의 의견으로는, 언어 모델 다중 로봇 계획의 검증 결과에는 일정 풀이 통과와 분해·배정의 정확성을 따로 적고, 계획 검증이 기대는 전제(사람이 준 도메인 판, i.i.d. 시나리오, 무오류 스킬 실행, 정확한 사람 도움)를 함께 기록해 전제가 깨질 때 보장 상태를 다시 평가해야 하며, 이 보장을 플릿의 물리적 안전 보장과 섞지 않아야 한다. [의견][^ref-170][^ref-092][^ref-1607]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-090]: Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. (arXiv), SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models, 2023-09-18, https://arxiv.org/abs/2309.10062, 접근일 2026-10-12
[^ref-092]: Liu, B., Jiang, Y., Zhang, X. 외 (arXiv), LLM+P: Empowering Large Language Models with Optimal Planning Proficiency, 2023-04-22, https://arxiv.org/abs/2304.11477, 접근일 2026-10-12
[^ref-1048]: Open X-Embodiment Collaboration (arXiv), Open X-Embodiment: Robotic Learning Datasets and RT-X Models, 2023-10-13, https://arxiv.org/abs/2310.08864, 접근일 2026-09-30
[^ref-1607]: Wang, J., He, G., & Kantaros, Y. (IEEE Robotics and Automation Letters 10(1)), Probabilistically Correct Language-based Multi-Robot Planning using Conformal Prediction, 2025-01, https://arxiv.org/abs/2402.15368, 접근일 2026-10-12
[^ref-170]: Su, X., Xu, J., van Kaick, O., Xu, K., & Hu, R. (arXiv), IMR-LLM: Industrial Multi-Robot Task Planning and Program Generation using Large Language Models, 2026-03-03, https://arxiv.org/abs/2603.02669, 접근일 2026-10-12
[^ref-351]: Ren, A. Z., Dixit, A., Bodrova, A. 외 (CoRL 2023, arXiv), Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners, 2023-07-04, https://arxiv.org/abs/2307.01928, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-05 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-05 | 44. 로봇 기반 모델·언어 모델 계획 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-10-12-05/pages/topics/2026/2026-10-12-area44-s8.md

```markdown
---
title: "44. 로봇 기반 모델·언어 모델 계획 — 대표 연구와 자료"
type: topic
category: "L. AI·학습 기술"
primary_area_no: 44
related_areas: [1, 4, 5, 12, 13, 24, 25, 26, 29, 31, 47, 54, 61, 62, 65]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-088, ref-1045, ref-1050, ref-1610, ref-1613, ref-1614, ref-1615, ref-1621]
last_run: 2026-10-12
version: 1
split_from: docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md#8
---

[홈](../../index.md) › [주제](../index.md) › 44. 로봇 기반 모델·언어 모델 계획 — 대표 연구와 자료

# 44. 로봇 기반 모델·언어 모델 계획 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 대표 자료는 로봇 기반 모델 계열과 언어 모델 계획 계열의 논문, 그리고 국내 협력 동향 기사다. [사실][^ref-1045][^ref-088][^ref-1050]
- 이 페이지는 [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

대표 자료는 로봇 기반 모델 계열과 언어 모델 계획 계열의 논문, 그리고 국내 협력 동향 기사다. [사실][^ref-1045][^ref-088][^ref-1050]


### 2026-10-12 갱신: 최근 로봇 기반 모델, VLA 견고성 평가, 국내 과제

- Physical Intelligence, π0.7 기술 보고서(2026-04, arXiv v2) — 관절(joint)·엔드이펙터(ee) 행동을 함께 학습하고, 프롬프트의 텍스트 식별자로 실행 제어 모드를 지정해 실행 시 과제에 따라 고른다고 설명한다. [추정] 벤더 주장[^ref-1613] 추론 지연에 대비해 학습 중 0~12 타임스텝의 지연을 모사했고 이는 50 Hz 로봇에서 최대 240 ms에 해당한다고 적지만, 이는 학습 조건이며 측정된 추론 지연이 아니고 보고서의 UR5e 로봇은 20 Hz로 동작한다. [추정] 벤더 주장[^ref-1613] 저자들은 학습 데이터가 매우 커서 평가 과제가 학습 때 본 과제인지 처음 보는 과제인지 확정하기 어렵다고 스스로 밝힌다. [추정][^ref-1613] 공개 구현 openpi의 기반 체크포인트 목록에는 π0.7이 없다(7절). [사실][^ref-1610]
- Fei, S. 외, LIBERO-Plus(arXiv 2025-10; CVPR 2026 게재본 제목은 'LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models') — LIBERO 시뮬레이션 조작 과제에서 물체 배치, 카메라 시점, 로봇 초기 상태, 언어 지시, 조명, 배경 질감, 센서 잡음의 7개 축으로 입력을 하나씩 교란해 VLA 모델의 견고성을 평가한다. [사실][^ref-1614][^ref-1615] arXiv v3 안의 표 1(원래 LIBERO 설정의 단일 축 교란 분석: OpenVLA-OFT 성공률 원본 97.1, 카메라 시점 59.7, 로봇 초기 상태 37.2)과 표 2(LIBERO-Plus 벤치마크 견고성 평가: 카메라 56.4, 로봇 31.9, 전체 69.6)는 평가 설정이 다른 두 표다. [추정][^ref-1614] 이 벤치마크는 단일 팔 조작 시뮬레이션이며 현장 플릿 평가가 아니다. [사실][^ref-1614] 이 위키의 의견으로는, 카메라 교체·로봇 초기 자세 변경 같은 교란을 로봇별 수용 시험에 넣고, 벤치마크 수치는 표·평가 설정(단일 축 교란 분석인지 벤치마크 평가인지)과 판을 밝혀 인용하며, 단일 팔 시뮬레이션 벤치마크 순위를 제조사 혼합 플릿 순위로 환산하지 않아야 한다. [의견][^ref-1614][^ref-1615]
- 산업통상부, M.AX 얼라이언스 협력 보도자료(2025-11-24) — 휴머노이드 분과 과제 '휴머노이드 AI 파운데이션 모델 개발'(2025~2028년, 484억 원)은 기업이 데이터·플랫폼을 제공하고 서울대가 모델을 개발해 기업에 다시 제공하는 구조다. [사실][^ref-1621]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md)
- 관련 영역: [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md), [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [12. 채팅으로 업무 지시·오케스트레이션](../../categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md), [13. 대화형 기능의 신뢰·기반](../../categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [29. 명령·작업 실행의 신뢰성](../../categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-088]: Ahn, M., Brohan, A., Brown, N. 외 (arXiv), Do As I Can, Not As I Say: Grounding Language in Robotic Affordances, 2022-04-04, https://arxiv.org/abs/2204.01691, 접근일 2026-09-30
[^ref-1045]: Brohan, A., Brown, N. 외 (Google DeepMind, arXiv), RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control, 2023-07-28, https://arxiv.org/abs/2307.15818, 접근일 2026-09-30
[^ref-1050]: 지디넷코리아, K-휴머노이드 연합, 출범 3주 만에 협약 4건 성과, 2025-05-01, https://zdnet.co.kr/view/?no=20250501140356, 접근일 2026-09-30
[^ref-1610]: Physical Intelligence (Physical-Intelligence/openpi GitHub), openpi — README, docs/remote_inference.md, LICENSE (커밋 215abfb), 미확인, https://github.com/Physical-Intelligence/openpi/blob/215abfb217dbac7d5f1273282331b9b1866c0479/docs/remote_inference.md, 접근일 2026-10-12
[^ref-1613]: Physical Intelligence (Ai, B. 외, arXiv), π0.7: a Steerable Generalist Robotic Foundation Model with Emergent Capabilities, 2026-04-16, https://arxiv.org/abs/2604.15483, 접근일 2026-10-12
[^ref-1614]: Fei, S., Wang, S., Shi, J. 외 (arXiv), LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models, 2025-10-15, https://arxiv.org/abs/2510.13626, 접근일 2026-10-12
[^ref-1615]: Fei, S., Wang, S., Shi, J. 외 (CVPR 2026, Computer Vision Foundation Open Access), LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models, 2026, https://openaccess.thecvf.com/content/CVPR2026/html/Fei_LIBERO-Plus_A_Progressive_Robustness_Benchmark_for_Visual-Language-Action_Models_CVPR_2026_paper.html, 접근일 2026-10-12
[^ref-1621]: 산업통상부, 서울대와 M.AX 얼라이언스가 손잡고 휴머노이드, 자율주행차, AI팩토리에 탑재될 AI 모델 공동 개발한다., 2025-11-24, https://www.motir.go.kr/kor/article/ATCL3f49a5a8c/171238/view, 접근일 2026-10-12

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-05 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-05 | 44. 로봇 기반 모델·언어 모델 계획 의 "대표 연구와 자료" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 15건 / 전체 1538건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

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

### docs/open-questions.md (요약: 대상 영역 [44] 에 걸린 7건 / 전체 411건)

```markdown
- oq-216 [열림] 로봇 기반 모델(VLA)을 탑재해 명시적 스킬 목록 없이 학습된 범용 기능을 가진 로봇의 능력을 플랫폼의 능력 모델에 어떻게 등록·기술하고 검증할 것인가? (영역 44, 5)
- oq-217 [열림] 언어 모델 기반 다중 로봇 계획기를 현장 제약(설비·안전·시간창)이 있는 조건에서 비교할 공통 벤치마크나 평가 기준이 있는가? (영역 44, 54)
- oq-218 [열림] 국내 로봇 AI 파운데이션 모델 과제의 물류센터 실증 목표(자동화율 80%, 성공률 90%)에 대한 공개된 측정 결과가 있는가? (영역 44, 61)
- oq-219 [열림] 출처 충돌: BMW 그룹 보도자료(2026-06-25) 안에서 Figure 02의 스파턴버그 배치 기간이 10개월과 11개월로 엇갈리는데, 실제 배치 기간은 얼마인가? (영역 44, 62)
- oq-305 [열림] 대화로 만든 다중 로봇 작업 계획을 사람이 승인하기 전에 시뮬레이션으로 실행 가능성을 미리 확인하는 절차를 플릿 오케스트레이션에 적용한 공개 사례가 있는가? (영역 12, 36, 44)
- oq-314 [열림] RoboGuard 같은 언어 모델 로봇용 안전 가드레일을 다중 로봇 플릿의 배정·경로·구역 계획에 적용해 위험 계획 차단율을 측정한 연구나 제품이 있는가? (영역 44, 48, 13)
- oq-315 [열림] 언어 모델 기반 고장 진단(REFLECT, SYSDIAGBENCH)을 제조사가 다른 이동로봇 플릿의 실행 기록·오류 코드에 적용해 원인 분석 정확도를 측정한 사례가 있는가? (영역 47, 38, 44)
```
