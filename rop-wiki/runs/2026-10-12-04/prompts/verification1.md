(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-12-04
- date: 2026-10-12
- run_type: update (갱신)
- 대상: 47. AI·학습·적응과 모델 운영 (L. AI·학습 기술)
- 예산:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2
- 환경 알림: web_fetch_available: true · fetch_mode: full
- 세부영역 반영 제안: 15건 — 트랙 실행이 이 영역 페이지에 반영하자고 제안한 내용(입력 data/area_reflection_proposals.json). 이번 실행의 조사·검증을 거쳐 해당 절에 반영을 검토한다(사양서 6.3 절차 9 '반영은 다음 해당 영역 실행에서')
- 언어: ko
- verification_stage: first
- verifier_budget:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
    - max_retries: 2

## 입력

### runs/2026-10-12-04/target.json

```json
{
  "run_id": "2026-10-12-04",
  "date": "2026-10-12",
  "weekday": "Mon",
  "run_number": 176,
  "run_type": "update",
  "forced": true,
  "target": {
    "area_no": 47,
    "area_name": "47. AI·학습·적응과 모델 운영",
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
  "selection_rationale": "CLI 지정 run_type=update, area=47"
}
```

### runs/2026-10-12-04/research.json

```json
{
  "run_id": "2026-10-12-04",
  "date": "2026-10-12",
  "run_type": "update",
  "target": {
    "area_no": 47,
    "area_name": "47. AI·학습·적응과 모델 운영",
    "category": "L. AI·학습 기술"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 — 67행 규제 문단이 한국 인공지능기본법을 '2026-01-22 시행'으로만 두고 '개정 법률의 시행일 … 미확인'으로 남김. EU AI Act 를 '부속서 I(기계류 등) 제품의 안전 구성요소 → 고위험'으로만 적어 2026/1744 개정(기계류의 Section B 이동, 제2조 2항 적용 조문 한정)을 반영하지 못함",
    "섹션 4. 핵심 개념과 용어(분리 2026-09-25-area27-s4) — 등각 예측 항목(41행)에 보장의 전제(i.i.d. 보정, 정확한 사람 도움)가 없고, 모델 레지스트리 항목(44행)이 별칭 반영 시점을 말하지 않음. 정책·데이터 형식 호환성(전처리·보정판) 개념 없음",
    "섹션 5. 적용 사례 — 가상 시나리오 두 개와 한진 기사뿐이고, 실제 플릿 단계 배포·운영 중 학습·국내 학습–운영 연계 사례가 없음",
    "섹션 6. 대표 접근법과 기술(분리 2026-09-25-area27-s6) — '모델 운영 관리' 소절(69행)이 ML Test Score 항목 수와 MLflow 별칭 교체 두 문장뿐이라 승인·카나리·롤백 연습, 배포 중단·롤백 실패 상태가 없음. KnowNo 문장(57행)이 보장 조건 없이 [사실]",
    "섹션 7. 관련 표준·프레임워크·오픈소스(분리 2026-09-25-area27-s7) — 모든 행이 원문 미열람, 로봇 정책 배포 호환성(LeRobot)·국내 공개 학습 데이터 판 관리 행 없음, NIST AI RMF 는 보도자료(ref-617)만 근거. 관련 법 문단(48행)이 3절과 같은 낡은 서술",
    "섹션 8. 대표 연구와 자료(분리 2026-09-25-area27-s8) — 분포 이동 아래 재보정 연구와 플릿 규모 운영 중 학습 연구가 없음",
    "섹션 9. 책임 경계 — 배포 후 감시·변경관리·복구 실패 처리의 책임 분담이 없음",
    "섹션 11. 열린 질문 — oq-030 이 '이번 실행에서는 조사하지 않았다'로 남아 있으나 2026-10-10 영역 25 갱신에서 원문 수치가 이미 정리됨. 세 질문이 oq id 없이 '(신규 …)'로 표시됨. oq-105·oq-106·oq-107 근거 없음",
    "정정 요청 없음(target.json corrections 비어 있음). 메모·검증에서 나온 위키 내부 정정: 한국 법 개정 시행일, EU AI Act 기계류 Section B 이동, KnowNo 보장 조건, ref-168 저자 표기(후속)"
  ],
  "research_questions": [
    "AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? [분류원문]",
    "모델 레지스트리의 별칭 교체·정책 정규화·데이터 형식 변경은 로봇에서 실제로 실행되는 모델 판과 어떻게 어긋날 수 있으며, 단계 배포·중단·롤백 실패는 어떤 상태로 기록되는가? (섹션 4·6·7 겨냥, oq-213)",
    "oq-107 KnowNo 등각 예측 보장의 전제는 무엇이며, 분포가 바뀔 때 재보정은 어떤 조건(정답 관측·피드백)을 요구하는가? (섹션 4·6·8 겨냥, oq-222)",
    "플릿 규모 운영 중 학습과 국내 학습–운영 연계 발표는 어떤 조건·증거 수준의 사례인가, 국내 공개 로봇 조작 데이터의 판·분할 메타데이터는 믿을 만한가? (섹션 5·7·8 겨냥)",
    "oq-106 2026-07-27 AI Act 통합판에서 기계류 연계 로봇 AI 에 어떤 조문이 적용되며, 중대한 변경 재평가·시판 후 감시 조문은 무엇을 정하는가? (섹션 3·7·11 겨냥)",
    "oq-105 한국 인공지능기본법의 현행 판 시행일과 고영향 AI 사업자의 문서화 책무는 무엇인가? (섹션 3·7·11 겨냥)",
    "oq-030 LTAA 원문 수치 충돌은 위키 안에서 어디까지 정리됐는가? (섹션 11 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "MLflow v3.1.0 모델 레지스트리 문서는 별칭(alias)을 새 모델 버전으로 재지정하면 같은 별칭 기반 모델 로딩 코드가 다음에 실행될 때 새 버전을 자동으로 가져온다고 설명한다. 이미 실행 중인 프로세스나 연결이 끊긴 장치의 모델이 바로 바뀐다는 뜻은 아니다.",
      "tag": "사실",
      "source_ids": [
        "ref-1577"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "workflow.mdx 'Fetching an MLflow Model'(v3.1.0 태그, 308~310행): \"the next execution of this snippet will automatically pick up the new model\". 기존 위키 '별칭을 옮겨 운영 모델을 교체'(2026-09-25-area27-s6.md 69행, s7 44행, s4 44행)의 범위 보충. 3.1.0 은 2025-06-10 PyPI 판으로 약 16개월 전 판에 고정된 문서",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "ROP 는 레지스트리의 목표 모델 버전과 각 로봇이 실제로 실행 중인 버전을 따로 기록하고, 별칭 변경 뒤 장치별 로딩·검증 응답을 받아야 교체가 끝났다고 볼 수 있다.",
      "tag": "의견",
      "source_ids": [
        "ref-1577"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "메모 A01 ROP 시사점. 근거는 f1(별칭 변경은 다음 로딩 시점에 반영)이며 플릿 전체 원자적 교체·자동 복구 보장은 확인 못 함",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "LeRobot v0.6.0 하위 호환성 문서는 PR #1452 이후 정책 가중치에 내장되던 정규화 계층을 없애고 외부 PolicyProcessorPipeline 구성요소가 정규화를 맡도록 바꾼 변경을 '호환성 깨짐(Breaking Change)'으로 명시하고, 이전 모델은 이전(migration)이 필요하다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1578"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "backwardcomp.mdx 'Policy Normalization Migration': \"Normalization is now handled by external `PolicyProcessorPipeline` components.\" 표: 정규화 위치 '가중치 내장(normalize_inputs.*)' → '외부 파이프라인'. 로봇별 배포 성능 검증은 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "같은 문서는 하드웨어 API 재설계(PR #777) 이전의 보정 방식으로 기록한 궤적을 그대로 불러오면 잘못 재생된다고 경고한다(SO100/SO101 예시의 관절 보정·입출력 변환).",
      "tag": "사실",
      "source_ids": [
        "ref-1578"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "backwardcomp.mdx 'Hardware API redesign / Impact on existing datasets': \"Recorded trajectories created before PR #777 will replay incorrectly if loaded directly\". 예시 기종(SO100/SO101) 밖으로 일반화하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "LeRobotDataset v3.0 형식은 여러 에피소드의 표 행과 영상 프레임을 큰 파일로 이어 붙이고, 에피소드별 구간은 파일 경계가 아니라 메타데이터로 복원한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1578"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "lerobot-dataset-v3.mdx(v0.6.0 태그) Format design: \"Episode-specific views are reconstructed via metadata, not file boundaries.\" 코드 판 v0.6.0 과 데이터 형식 판 v3.0 은 다른 번호",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "학습 정책을 로봇에 배포할 때는 가중치 해시, 전·후처리기와 정규화 통계, 학습 데이터 커밋과 데이터 형식 판, 카메라·관절 스키마, 하드웨어 보정판, 런타임 판을 하나의 배포 묶음으로 기록하고 이전 묶음을 보존해야 되돌림이 가능하다.",
      "tag": "의견",
      "source_ids": [
        "ref-1578"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "메모 A02 ROP 시사점. 근거 f3~f5(정규화 외부화, 보정 방식 변경 시 재생 오류, 메타데이터 기반 에피소드 복원). 실제 모델 변환·실물 재생 시험은 하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "Mender 문서는 사용자 정의 업데이트 모듈(Update Module)이 롤백을 지원하려면 SupportsRollback 질의에 Yes 로 답하고, 설치 전에 '알려진 정상 상태(known good state)'를 저장했다가 롤백 때 복원하는 구현을 모듈 작성자가 넣어야 한다고 설명한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1579"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: docs.mender.io 'Create a custom Update Module' 롤백 예제: SupportsRollback \"Yes\", \"save a \\\"known good state\\\" before the installation\". 일반 파일 갱신 예제이며 모델·전처리기·데이터 일관 복구를 시험한 결과 아님. 상태 스크립트·A/B 원자 배포는 기존 내용(2026-10-09-area43-s6.md 48~50행, ref-1323·ref-1040)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f8",
      "claim": "Mender 문서는 전원 상실 뒤 업데이트 상태가 다시 실행될 수 있으므로 업데이트 모듈을 멱등(idempotent)하게 만들어야 한다고 권고한다(should).",
      "tag": "추정",
      "source_ids": [
        "ref-1579"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 같은 문서 'Power loss': \"you should develop Update Modules to be idempotent\" — 같은 상태를 여러 번(부분 실행 포함) 다시 실행해도 마지막 실행이 완전하면 한 번 실행한 것과 같아야 함. 권고(should) 강도",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f9",
      "claim": "AWS IoT Jobs 문서는 작업 배포 속도(rollout)와 중단(abort) 설정을 두고, 실패한 장치 수 등이 지정한 기준에 도달하면 작업 배포를 취소할 수 있다고 설명한다. 이는 새 배포를 멈추는 것이며 이미 설치된 장치의 원복과는 별개다.",
      "tag": "추정",
      "source_ids": [
        "ref-1581"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 'How job configurations work' — \"Job rollout, scheduling, and abort configurations\", 기준 충족 시 \"you can cancel the job rollout\". 일반 IoT 작업 문서. 기존 ref-556(aws-samples ROS 2 OTA README)의 자동 롤백 이점 나열과 달리 중단 기준만 새 내용",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f10",
      "claim": "AWS IoT Greengrass v2 문서는 장치별 배포 실패 상태를 롤백 미요청(FAILED_ROLLBACK_NOT_REQUESTED), 이전 정상 구성으로 롤백 완료(FAILED_ROLLBACK_COMPLETE), 롤백 실패(FAILED_UNABLE_TO_ROLLBACK)로 나누고, 롤백하지 않았거나 롤백에 실패한 장치는 정상 동작하지 않을 수 있다고 적는다.",
      "tag": "추정",
      "source_ids": [
        "ref-1580"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 'Check deployment status': FAILED_ROLLBACK_COMPLETE \"successfully rolled back to a previous working configuration\" / FAILED_UNABLE_TO_ROLLBACK \"failed to roll back … might not be functioning correctly\". 부트스트랩 배포는 실패 시 항상 롤백 시도. ref-1581 과 같은 AWS 자료라 독립 교차 확인 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f11",
      "claim": "모델 배포는 배포 중단, 이전 모델 복원 시도, 복원 확인을 서로 다른 상태로 기록하고, 확대 배포 여부는 집단 성공률만이 아니라 장치별 현재 버전·실패 사유·복구 결과로 판단하며, 복구하지 못한 로봇은 새 작업 배정에서 빼는 운영 정책을 두는 것이 맞다.",
      "tag": "의견",
      "source_ids": [
        "ref-1579",
        "ref-1580",
        "ref-1581"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "메모 A03·A04 ROP 시사점. 근거 f7~f10(벤더 문서 단독). 연결 단절 중 즉시 원복 기능은 확인 못 함",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "Viam 문서는 새 모델을 플릿에 내보낼 때 갱신한 구성 조각(fragment)을 먼저 첫 집단(예: 카나리 위치)에만 적용해 관찰한 뒤 나머지 집단으로 넓히는 절차를 제시한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1582"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 'Roll out a new model to a fleet' — \"Apply the updated fragment to the first group only (for example, a 'canary' location).\" 비전 모델·fragment 기반 구성 절차이며 안전 인증 절차나 고객 현장 성과 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f13",
      "claim": "같은 Viam 문서는 새 모델이 잘못 보이면 구성 조각에서 이전 판을 고정해 되돌리며, 장치들은 다음 구성 동기화 때(정상 운영에서는 수 초 안에) 이전 판으로 수렴한다고 설명한다. 연결이 끊긴 장치의 즉시 변경은 아니다.",
      "tag": "추정",
      "source_ids": [
        "ref-1582"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 같은 문서 \"roll back by pinning the previous version in the fragment. Machines converge to the previous version on the next config sync\", 구성 반영은 \"within seconds under normal operation\". 통신 장애·장기 성능의 독립 재현 없음(oq-213 부분 근거)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f14",
      "claim": "ML Test Score 의 Infra4 항목은 모델이 실제 요청에 영향을 주기 전에 품질을 자동 검사해 모델을 승인(bless)하거나 거부(veto)해 운영 투입을 막는 절차를 권한다.",
      "tag": "사실",
      "source_ids": [
        "ref-625"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Breck 외(IEEE Big Data 2017) §IV Infra4, PDF 5쪽: \"either bless the model or veto it, terminating its entry to the production environment\". 일반 ML 서비스 운영 지침이며 로봇 안전 요구는 아님. 28개 항목 소개는 기존 내용(s6 69행)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f15",
      "claim": "같은 논문의 Infra6 항목은 오프라인 시험이 아무리 광범위해도 그것만으로는 운영 환경에서의 모델 성능을 보장할 수 없다고 밝히고, 소수 트래픽에 먼저 내보내는 카나리 방식을 완화책으로 든다.",
      "tag": "사실",
      "source_ids": [
        "ref-625"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§IV Infra6, PDF 5쪽: \"Offline testing, however extensive, cannot by itself guarantee the model will perform well in live production settings.\" 카나리는 위험 완화 방법이며 물리적 위험 노출을 허가하는 근거가 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "같은 논문의 Infra7 항목은 운영 모델을 이전 정상판으로 되돌리는 롤백을 비상 절차로 두고, 운영자가 비상 상황이 아닐 때 미리 연습해야 한다고 권고한다(should).",
      "tag": "사실",
      "source_ids": [
        "ref-625"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§IV Infra7, PDF 5~6쪽: 롤백은 \"an emergency procedure, operators should practice doing it\" 정상 운영 중에. 권고 강도(should). DOI 10.1109/BigData.2017.8258038, pp.1123–1132",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f17",
      "claim": "로봇 모델의 운영 투입 승인 기록에는 장치·현장별 성능 하한, 기존 판 대비 퇴행, 로딩·추론 지연, 개입·실패 사례, 실제 롤백 연습 결과를 연결하고, 위험한 행동의 시험은 현장 안전 절차와 분리하지 않아야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-625"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "메모 A06 ROP 시사점. 근거 f14~f16. 로봇용 보편 임계값·합격 점수는 이번 조사로 정하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f18",
      "claim": "KnowNo(Ren 외, CoRL 2023, PMLR 229) §3.1 의 등각 예측 보장은 보정 집합과 새 시험 표본이 같은 미지의 분포 D 에서 독립·동일 분포(i.i.d.)로 뽑힌다는 가정 위에 선다.",
      "tag": "사실",
      "source_ids": [
        "ref-351"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "PMLR 229:661–682 판 §3.1, PDF 4쪽: 보정 데이터는 분포 D 에서 추출, \"given a new i.i.d. sample z_test\". 계절·고객 변화에도 보장이 유지된다는 뜻 아님. 기존 위키 s6 57행(보장 서술)·s4 41행에 조건을 덧붙이는 근거(카테고리 index 116행은 이미 조건 언급)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f19",
      "claim": "KnowNo 의 과제 성공 보장(§3.2 명제)의 증명은 사람이 정확하게 도와준다는 가정에 기댄다.",
      "tag": "사실",
      "source_ids": [
        "ref-351"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§3.2, PDF 5쪽: \"The proof immediately follows from the fact that under the assumption of accurate human help\". 사람이 오판하는 현장에서는 보장이 그대로 성립하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "KnowNo 는 다단계 계획에서 시점 사이 의존성 때문에 i.i.d. 가정이 깨지는 문제를 다루려고 개별 시점 대신 시퀀스 수준에서 보정(sequence-level calibration)한다.",
      "tag": "사실",
      "source_ids": [
        "ref-351"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§3.3, PDF 5쪽: \"Sequence-level calibration. The key ideas are to (i) lift the data to sequences, and (ii) perform calibration\"; 시퀀스 수준 포함 하한 P(y∈C(x))≥1−ε. 운영 분포의 임의 변화에 대한 증명 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "적응형 등각 추론(Adaptive Conformal Inference, Gibbs·Candès, NeurIPS 2021)의 명제 4.1 은 분포가 시간에 따라 바뀌어도 장기간의 경험적 포함 빈도가 목표값에 맞는다는 장기 평균 보장을 준다. 논문 실험은 주가 변동성·선거 데이터이며 로봇 실험은 없다.",
      "tag": "사실",
      "source_ids": [
        "ref-1583"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "NeurIPS 34 pp.1660–1672, §4.1, PDF 6쪽: 방법이 \"the correct long-term empirical coverage frequency\"를 준다. 매 시점 보장이나 로봇 안전 보장 아님. KnowNo 와 결과 종류가 달라 서로의 교차 확인으로 세지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "같은 방법의 온라인 갱신은 직전 예측 집합들이 정답을 놓친 경험적 빈도(empirical miscoverage)를 보고 임계값을 조정하므로, 운영 중 정답(Y_t)을 관측할 수 있어야 쓸 수 있다.",
      "tag": "사실",
      "source_ids": [
        "ref-1583"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§2 식 (2), PDF 3쪽: \"empirical miscoverage frequency of the previous prediction sets\"에 따라 임계값을 올리거나 내림. 피드백 지연·정답 수집 비용이 있는 로봇 현장 성능은 미확인",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "물류 지시 분포가 바뀌는 현장에서는 고정 간격(예: 매월) 재보정을 근거 없는 기본값으로 두지 말고, 지시 유형별 보정 오차와 데이터 변화 신호를 감시하며 피드백 지연·정답 수집 비용을 고려한 재보정 정책을 시험해야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-351",
        "ref-1583"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "메모 A07·A08 ROP 시사점. 근거 f18~f22. oq-107(재보정 주기)의 부분 답이며 최적 주기는 미해결",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "제조사 연구(저자 전원 AGIBOT 소속, 저자 보고)인 Learning While Deploying(LWD, arXiv v4)은 자사 Agibot G1 양팔 로봇 16대 플릿(식료품 보충 작업 4대, 장기 작업마다 3대)으로 8개 실물 조작 작업에서 온라인 학습을 했고, 방법마다 실험당 4시간 벽시계 예산(플릿 합계 약 60시간)을 줬다.",
      "tag": "사실",
      "source_ids": [
        "ref-1585"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2605.00416v4(2026-09-16) §V-A: \"All experiments are conducted on the Agibot G1\", \"4 robots for the grocery restocking tasks and 3 robots for each long-horizon task\", \"4-hour wall-clock budget, corresponding to approximately 60 total hours\". 동일 플랫폼이며 이기종 플릿 아님. 프리프린트, 학회 게재 미확인",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f25",
      "claim": "LWD 의 학습기는 50 학습 단계마다 갱신 정책을 플릿에 내보내고, 로봇 액터는 에피소드 경계에서 새 정책을 다시 불러온다(제조사 연구, 저자 보고).",
      "tag": "사실",
      "source_ids": [
        "ref-1585"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§V-A: \"The learner broadcasts the updated shared policy to the robot fleet every 50 training steps.\" 부록 D: actors \"reload the new policy at episode boundaries\". 연구 구현이며 상용 플릿의 원자적 배포 보장 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f26",
      "claim": "LWD 저자는 한계 절에서 현재 정책 학습 틀이 실행 안전을 명시적으로 모델링하지 않으며, 단순한 실시간 갱신 일정이 대규모·장기 배포에 최적이 아닐 수 있다고 밝힌다.",
      "tag": "사실",
      "source_ids": [
        "ref-1585"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "§VI 한계: \"our current policy learning framework does not explicitly model execution safety\"; 갱신 일정은 \"may not be optimal for larger-scale deployment\". 식료품 작업 이진 성공률과 장기 작업 부분 점수가 달라 표 평균을 임무 완료율로 인용하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f27",
      "claim": "운영 중 학습하는 정책을 쓰는 플릿에서는 작업 이력마다 실행한 정책 판을 붙이고, 새 정책을 적용하는 경계(예: 에피소드·임무 단위)와 승인 주체를 명시해야 임무 도중 모델이 바뀌는 문제를 관리할 수 있다.",
      "tag": "의견",
      "source_ids": [
        "ref-1585"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "메모 A09 ROP 시사점. 근거 f24~f26. 이기종·중단 불가 장기 임무에의 적합성은 미확인(새 열린 질문)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f28",
      "claim": "LG CNS 는 2026-05-07 발표에서 로봇 학습·운영 플랫폼 '피지컬웍스'의 포지(Forge)에서 학습·검증한 로봇을 바통(Baton)으로 운영·관제하고, 이 과정에서 축적한 데이터를 다시 학습에 쓰는 선순환 체계를 구축했다고 밝혔다.",
      "tag": "추정",
      "source_ids": [
        "ref-1584"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 회사 보도자료(뉴스와이어 재게시 동일): \"피지컬웍스 포지에서 학습·검증한 로봇을 피지컬웍스 바통을 통해 운영·관제하고, 이 과정에서 축적된 데이터를 다시 학습에 활용\". 모델 판 승인·복구 기록은 공개되지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f29",
      "claim": "같은 발표는 AMR·AGV 등 100대 규모 운영 환경에 바통을 적용하면 생산성이 약 15% 이상 오르고 운영비가 최대 18% 줄 것으로 '기대된다'고 적으며, 이는 실측 비교 결과가 아니라 회사의 기대치다.",
      "tag": "추정",
      "source_ids": [
        "ref-1584"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: \"생산성은 약 15% 이상 향상, 운영비는 최대 18%까지 절감할 수 있을 것으로 기대된다\". 측정 조건·기간 공개 없음. 뉴스와이어 재게시는 교차 확인이 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f30",
      "claim": "같은 발표는 포지가 20곳 이상 고객사와 로봇 개념검증(PoC)을 진행 중이고, 바통이 부산 스마트시티 국가 시범도시 사업에서 순찰·바리스타·짐캐리·청소 4종 로봇의 통합 관제에 쓰이고 있다고 주장한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1584"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: \"20곳 이상의 고객사와 로봇 개념검증(PoC) 프로젝트를 진행 중\", 부산 스마트시티 4종 로봇 통합 관제 활용. 독립 확인 없음. PoC 는 상시 운영 성과가 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f31",
      "claim": "학습·운영 연계 플랫폼을 도입 검토할 때는 시연, PoC, 상시 운영을 서로 다른 수준의 증거로 받고, 모델 갱신 이력·고객 검수·장애 복구 기록을 따로 요청해야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-1584"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "메모 A10 ROP 시사점. 근거 f28~f30(회사 발표 단독)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f32",
      "claim": "AI-Hub '대규모 물리환경 로봇조작 데이터'(dataSetSn 71825)의 변경이력은 v1.0 을 2025-04-16 데이터 개방(Beta), v1.1 을 2025-06-30 데이터 최종 개방으로 표시한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1588"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "데이터 변경이력 표: \"1.1 / 2025-06-30 / 데이터 최종 개방\", \"1.0 / 2025-04-16 / 데이터 개방 / Beta Version\". 공식 메타데이터이며 실제 파일 완전성 검증은 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f33",
      "claim": "같은 페이지의 데이터 히스토리에서 2026-05-06 항목은 '기타 – 태그 추가'로만 표시돼 새 데이터 판 발행으로 볼 근거가 없다.",
      "tag": "사실",
      "source_ids": [
        "ref-1588"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "데이터 히스토리: \"2026-05-06 / 기타 / 태그 추가\", \"2025-04-16 / 산출물 최종 공개\". 최근 1년 안 변경은 태그뿐",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f34",
      "claim": "같은 데이터의 학습용 구성표(라벨링 JSON 기준)는 총 262,166 건 중 학습 238,266 건, 테스트 23,900 건을 적으면서 표제는 '학습 데이터 (80%)', '테스트 데이터 (10%)'로 달아, 실제 비율(약 90.9%·9.1%)과 맞지 않고 검증 분할은 표기하지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1588"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "데이터 구축 규모 표: 총량 262,166 / 학습 238,266 / 테스트 23,900, 표제 \"학습 데이터 (80%)\" \"테스트 데이터 (10%)\". 90.9%·9.1% 는 이 위키가 238,266/262,166 등으로 계산한 값이며 원문 값 아님",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f35",
      "claim": "같은 데이터의 원천 데이터는 실제환경 77,984 장, 가상환경 184,182 장(RGB 기준, Depth 같은 수)으로, 전체 262,166 장 가운데 약 70% 가 가상환경에서 취득됐다.",
      "tag": "사실",
      "source_ids": [
        "ref-1588"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원천데이터 분포 표: 실제환경 png 77,984 장, 가상환경 png 184,182 장. 약 70.3% 는 184,182/262,166 계산값. 데이터 설명: \"실제와 가상환경에서 취득한 RGB-D이미지\". 실물 조작 성능 근거로 읽을 때 실제·가상을 구분해야 함",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f36",
      "claim": "같은 페이지의 분포 표는 원천 데이터 분포 비율을 실제 14.29%·가상 85.71% 로 적어 수량(약 29.7%·70.3%)과 맞지 않고, 라벨링 JSON 수량(77,984 + 184,182 = 262,166)의 합계를 524,332 로 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1588"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "분포 표: \"실제환경 … 77,984 … 14.29%\", \"가상환경 … 184,182 … 85.71%\", 가공(라벨링) 데이터 \"합계 524,332\". 524,332 는 RGB+Depth 이미지 합(2×262,166)과 같아 JSON 합계로는 오기로 보이나 제공자 확인 전에는 정답을 정하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f37",
      "claim": "공개 데이터의 분할비·합계가 서로 맞지 않으면 제공자 확인 전에는 표제 분할비를 모델 승인 근거로 쓰지 말고, 실물·가상 구분, 중복, 평가용 누출을 실제 파일로 따로 검사해야 한다.",
      "tag": "의견",
      "source_ids": [
        "ref-1588"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "메모 A11 ROP 시사점. 근거 f34~f36. 실제 데이터 파일은 열지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f38",
      "claim": "NIST AI RMF 1.0(NIST AI 100-1)의 MANAGE 4.1 은 배포 후 AI 시스템 감시 계획에 사용자·관련 AI 행위자 의견 수집·평가, 이의 제기와 무효화(override), 폐기, 사고 대응, 복구, 변경관리 장치를 넣어 실행하도록 한다(자율 적용 프레임워크).",
      "tag": "사실",
      "source_ids": [
        "ref-1586"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "NIST AI 100-1 Table 4, PDF 38쪽(인쇄 33쪽): \"MANAGE 4.1: Post-deployment AI system monitoring plans are implemented, including mechanisms for … incident response, recovery, and change management.\" 법적 의무가 아닌 자율 프레임워크. 네 기능 소개는 기존 내용(s7 41행, ref-617)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f39",
      "claim": "모델 공급자의 학습·검증 책임, ROP 의 배포·실행 판 기록, 현장 운영자의 개입·사고 통보 역할은 계약과 운영 절차에서 따로 정해야 하며, 조직 단위 관리 체계 인증만으로 특정 로봇 모델의 안전 성능을 승인해서는 안 된다.",
      "tag": "의견",
      "source_ids": [
        "ref-1586"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "메모 A12 ROP 시사점. 근거 f38. ISO/IEC 42001 공식 페이지는 이번에 열지 못해(Cloudflare) 인용하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f40",
      "claim": "EUR-Lex 의 AI Act(Regulation (EU) 2024/1689) 2026-07-27 통합판은 Regulation (EU) 2026/1744(2026-07-08 채택, 관보 2026-07-24 게재) 개정을 반영하며, 이 개정으로 부속서 I Section A 에서 기계류(1번 항목)가 삭제되고 Section B 21번에 기계류 규정 (EU) 2023/1230 이 추가됐다.",
      "tag": "사실",
      "source_ids": [
        "ref-1587"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "통합판 머리 'Amended by: ►M1 Regulation (EU) 2026/1744 … of 8 July 2026, L 1744, 24.7.2026'. 부속서 I Section A 첫 항목 자리 '▼M1 —————'(삭제), Section B '▼M1 21. Regulation (EU) 2023/1230 … on machinery'. 기존 ref-1322 해설은 적용일 연기만 다룸",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f41",
      "claim": "개정된 AI Act 제2조 2항은 부속서 I Section B 의 조화 법령 대상 제품과 관련해 제6조 1항으로 고위험이 되는 AI 시스템에는 제6조 1항, 제60a조, 제102~112조만 적용하고, 제57~59조는 해당 법령에 고위험 요구사항이 통합된 범위에서만 적용한다고 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1587"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "통합판 제2조 2항(▼M1): \"only Article 6(1), Article 60a and Articles 102 to 112 shall apply. Articles 57, 58 and 59 shall apply only in so far as the requirements … have been integrated in that Union harmonisation legislation.\"",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f42",
      "claim": "AI Act 제43조 4항은 적합성 평가를 거친 고위험 AI 시스템이 중대한 변경(substantial modification)을 겪으면, 변경된 시스템을 다시 유통하든 같은 배포자가 계속 쓰든 새 적합성 평가 절차를 거치도록 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1587"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "통합판 제43조 4항: \"shall undergo a new conformity assessment procedure in the event of a substantial modification, regardless of whether the modified system is intended to be further distributed or continues to be used by the current deployer\". 제2조 2항에 따라 Section B 제품 관련 AI 에는 이 조가 적용되지 않음(f41)",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f43",
      "claim": "같은 항은 출시·사용 개시 뒤에도 계속 학습하는 고위험 AI 시스템에서, 제공자가 최초 적합성 평가 때 미리 정하고 부속서 IV 2(f) 기술문서에 담은 시스템·성능 변경은 중대한 변경으로 보지 않는다고 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1587"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "제43조 4항 둘째 문단: changes \"pre-determined by the provider at the moment of the initial conformity assessment and are part of the information contained in the technical documentation referred to in point 2(f) of Annex IV, shall not constitute a substantial modification\"",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f44",
      "claim": "AI Act 제72조 2항은 제공자의 시판 후 감시 체계가 배포자 제공 등으로 얻은 고위험 AI 시스템의 성능 관련 데이터를 수명 전반에 걸쳐 능동적·체계적으로 수집·문서화·분석하고, 관련되는 경우 다른 AI 시스템과의 상호작용 분석을 포함하도록 정한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1587"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "통합판 제72조 2항: \"actively and systematically collect, document and analyse relevant data … on the performance of high-risk AI systems throughout their lifetime\"; \"Where relevant, … analysis of the interaction with other AI systems\". 의무 주체는 제공자",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f45",
      "claim": "제2조 2항 개정에 따라 기계류 규정 대상 로봇의 안전 구성요소로서 부속서 I 경로로 고위험이 되는 AI 에는 제43조(중대한 변경 시 재평가)와 제72조(시판 후 감시)가 AI Act 조문으로 바로 적용된다고 볼 수 없으며, 이 두 조문은 Section A 법령·부속서 III 경로의 고위험 AI 에 해당하는 내용으로만 소개해야 한다. 위키의 '부속서 I(기계류 등) 고위험' 서술도 이 이동을 반영해야 한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1587"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "f40·f41 의 조문 범위에서 이끈 적용 해석(법률 판단 아님). 기계류 규정 쪽에 AI 요구가 어떻게 통합되는지, 개별 로봇·ROP 의 분류·제공자 지위는 확인하지 않음. 정정 대상: 본 페이지 3절 67행, 2026-09-25-area27-s7.md 48행",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f46",
      "claim": "EU 시장을 대상으로 할 때는 적용 관할·시스템 분류·공급자 지위를 먼저 정하고, 그 뒤 최초 평가에서 허용한 변경 범위와 실제 모델 변경 내역을 대조할 수 있도록 변경 기록을 보존하는 것이 맞다.",
      "tag": "의견",
      "source_ids": [
        "ref-1587"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "메모 A13 ROP 시사점(검증 결과의 적용 범위 주의 반영). 근거 f41~f45",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f47",
      "claim": "한국 인공지능기본법 제34조 1항은 고영향 인공지능 또는 이를 이용한 제품·서비스를 제공하는 인공지능사업자가 대통령령으로 정하는 바에 따라 각 호의 안전성·신뢰성 확보 조치를 이행하도록 하며, 5호는 그 조치 내용을 확인할 수 있는 문서의 작성과 보관이다.",
      "tag": "사실",
      "source_ids": [
        "ref-620"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "국가법령정보센터 조문 제34조 ①: \"…다음 각 호의 내용을 포함하는 조치를 대통령령으로 정하는 바에 따라 이행하여야 한다\", 5. \"안전성ㆍ신뢰성 확보를 위한 조치의 내용을 확인할 수 있는 문서의 작성과 보관\". 1~4호(위험관리방안, 설명 방안, 이용자 보호, 사람의 관리·감독) 포함",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f48",
      "claim": "국가법령정보센터의 현행 조문은 「인공지능 발전과 신뢰 기반 조성 등에 관한 기본법」을 법률 제21311호(2026-01-20 공포·일부개정), 시행 2026-07-21 판으로 표시한다. 위키의 '2026-01-22 시행'은 최초 법률·시행령 기준이고 개정 법률의 시행일은 2026-07-21 이다.",
      "tag": "사실",
      "source_ids": [
        "ref-620"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "조문 머리말: \"[시행 2026. 7. 21.] [법률 제21311호, 2026. 1. 20., 일부개정]\". 기존 위키 '개정 법률의 시행일 … 미확인'(본 페이지 3절 67행, s7 48행)을 채움. 시행령 개정 판(검증 보고상 2026-08-18 공포)은 이번에 원문 확인하지 않음",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f49",
      "claim": "제34조의 문서 작성·보관 책무가 물류 현장의 작업 계획·배정 AI 를 쓰는 ROP 에 걸리는지는 고영향 인공지능 해당성과 사업자 지위(제공자·이용자) 판단이 먼저이며, 시행령상 보존 기간도 이번에 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-620"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f47 의 조문 범위('고영향 인공지능 … 제공하는 경우', '대통령령으로 정하는 바에 따라')에서 이끈 해석. 고영향 영역 목록·시행령·고시는 열지 않음. oq-105 부분 답",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f50",
      "claim": "ROP 는 학습용 데이터 개요, 모델 판, 위험 조치, 사람 감독, 승인·복구 기록을 서로 연결해 두어, 고영향 해당성이 판단되면 제34조 문서로 낼 수 있는 구조를 미리 갖추는 것이 좋다.",
      "tag": "의견",
      "source_ids": [
        "ref-620"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "메모 A14 ROP 시사점. 근거 f47~f49",
      "as_of": "2026-10-12",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-1577",
      "org": "MLflow 프로젝트 (Linux Foundation 오픈소스 프로젝트)",
      "title": "Model Registry Workflows (docs/docs/classic-ml/model-registry/workflow.mdx, MLflow v3.1.0)",
      "published": "2025-06-10",
      "url": "https://github.com/mlflow/mlflow/blob/v3.1.0/docs/docs/classic-ml/model-registry/workflow.mdx",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "MLflow v3.1.0 태그의 모델 레지스트리 작업 흐름 문서. 별칭 재지정 뒤 같은 로딩 코드의 다음 실행이 새 버전을 가져온다고 설명한다. 발행일은 3.1.0 판 공개일(PyPI) 기준이며 latest 문서(ref-626)와 다른 고정 판이다.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/mlflow/mlflow/v3.1.0/docs/docs/classic-ml/model-registry/workflow.mdx",
      "source_unopened": false
    },
    {
      "id": "ref-1578",
      "org": "Hugging Face LeRobot 기여자 (huggingface/lerobot)",
      "title": "Backward compatibility (docs/source/backwardcomp.mdx, LeRobot v0.6.0)",
      "published": "2026-07-06",
      "url": "https://github.com/huggingface/lerobot/blob/v0.6.0/docs/source/backwardcomp.mdx",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "LeRobot v0.6.0 태그의 하위 호환성 문서(정규화의 외부 PolicyProcessorPipeline 이동, PR #777 이전 궤적 재생 오류). 같은 태그의 lerobot-dataset-v3.mdx·inference.mdx 도 함께 열었다. 발행일은 0.6.0 판 공개일(PyPI) 기준.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/huggingface/lerobot/v0.6.0/docs/source/backwardcomp.mdx",
      "source_unopened": false
    },
    {
      "id": "ref-1579",
      "org": "Northern.tech (Mender documentation)",
      "title": "Create a custom Update Module",
      "published": null,
      "url": "https://docs.mender.io/artifact-creation/create-a-custom-update-module",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "Mender 사용자 정의 업데이트 모듈 작성 안내. 롤백 지원(SupportsRollback, 알려진 정상 상태 저장·복원)과 전원 상실 대비 멱등 구현 권고를 담는다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1580",
      "org": "Amazon Web Services (AWS IoT Greengrass V2 Developer Guide)",
      "title": "Check deployment status",
      "published": null,
      "url": "https://docs.aws.amazon.com/greengrass/v2/developerguide/check-deployment-status.html",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "Greengrass v2 의 배포·장치별 배포 상태 정의(FAILED_ROLLBACK_NOT_REQUESTED·FAILED_ROLLBACK_COMPLETE·FAILED_UNABLE_TO_ROLLBACK). 같은 안내서의 'Create deployments' 쪽도 함께 열었다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1581",
      "org": "Amazon Web Services (AWS IoT Core Developer Guide)",
      "title": "How job configurations work",
      "published": null,
      "url": "https://docs.aws.amazon.com/iot/latest/developerguide/jobs-configurations-details.html",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "AWS IoT Jobs 의 배포 속도·일정·중단(abort) 설정 안내. 실패 기준 충족 시 작업 배포를 취소할 수 있다고 설명한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1582",
      "org": "Viam",
      "title": "Roll out a new model to a fleet",
      "published": null,
      "url": "https://docs.viam.com/vision/deploy-and-maintain/roll-out-to-fleet/",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "Viam 플랫폼에서 비전 모델을 구성 조각(fragment)으로 첫 집단에 먼저 적용하고 확대·되돌리는 절차 문서.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1583",
      "org": "Gibbs, I., & Candès, E. J. (NeurIPS 2021)",
      "title": "Adaptive Conformal Inference Under Distribution Shift",
      "published": "2021-12-06",
      "url": "https://papers.nips.cc/paper/2021/file/0d441de75945e5acbc865406fc9a2559-Paper.pdf",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "분포 이동 아래 등각 예측 임계값을 온라인으로 조정하는 적응형 등각 추론(Advances in Neural Information Processing Systems 34, pp.1660–1672). 장기 경험적 포함 빈도 보장을 주며 실험은 주가 변동성·선거 데이터다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1584",
      "org": "LG CNS",
      "title": "LG CNS, 로봇 학습·운영 플랫폼 '피지컬웍스' 공개",
      "published": "2026-05-07",
      "url": "https://www.lgcns.com/kr/newsroom/press/detail.rx-2605-1",
      "type": "벤더 문서",
      "reliability": "low",
      "accessed": "2026-10-12",
      "summary": "LG CNS 보도자료(뉴스와이어 2026-05-07 재게시 동일). 피지컬웍스 포지·바통의 학습–운영 연계, 100대 기준 기대 효과, PoC·부산 스마트시티 활용을 회사가 주장한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.newswire.co.kr/newsRead.php?no=1033918",
      "source_unopened": false
    },
    {
      "id": "ref-1585",
      "org": "Wang, Y. 외 (AGIBOT)",
      "title": "Learning While Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies",
      "published": "2026-09-16",
      "url": "https://arxiv.org/abs/2605.00416v4",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "AGIBOT 소속 저자들의 제조사 연구 프리프린트(v1 2026-05-01, v4 2026-09-16). 자사 Agibot G1 16대 플릿에서 배포 중 오프라인–온라인 강화학습을 하고 에피소드 경계에서 정책을 갱신한다. 학회 게재 미확인.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2605.00416v4",
      "source_unopened": false
    },
    {
      "id": "ref-1586",
      "org": "NIST",
      "title": "Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1",
      "published": "2023-01",
      "url": "https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "NIST AI RMF 1.0 본문(DOI 10.6028/NIST.AI.100-1). Table 4 의 MANAGE 4.1 은 배포 후 감시 계획에 사고 대응·복구·변경관리를 포함한다. 기존 ref-617 은 발표 보도자료다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1587",
      "org": "European Union (EUR-Lex)",
      "title": "Regulation (EU) 2024/1689 (Artificial Intelligence Act) — consolidated text 02024R1689-20260727 (incl. M1 Regulation (EU) 2026/1744)",
      "published": "2026-07-27",
      "url": "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02024R1689-20260727",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "AI Act 2026-07-27 통합판. 옴니버스 개정 (EU) 2026/1744(2026-07-08 채택, 관보 2026-07-24)으로 기계류 규정이 부속서 I Section B 로 옮겨졌고 제2조 2항이 Section B 관련 고위험 AI 의 적용 조문을 한정한다. 제43조 4항·제72조 2항 확인.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:02024R1689-20260727",
      "source_unopened": false
    },
    {
      "id": "ref-1588",
      "org": "AI-Hub (한국지능정보사회진흥원)",
      "title": "대규모 물리환경 로봇조작 데이터",
      "published": "2025-06-30",
      "url": "https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&dataSetSn=71825&topMenu=100",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "AI-Hub 공개 데이터 71825 설명 페이지. v1.1 2025-06-30 최종 개방, 2026-05-06 태그 추가, 학습 238,266·테스트 23,900(총 262,166), 실제 77,984·가상 184,182 장. 표제 비율·합계에 불일치가 있다. 데이터 파일은 열지 않았다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-625",
      "org": "Breck, E. 외 (Google Research)",
      "title": "The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction",
      "published": "2017-12",
      "url": "https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "ML 시스템 운영 준비도 28개 항목 기준표(기존 출처). 이번에 IEEE Big Data 2017 원고 PDF(DOI 10.1109/BigData.2017.8258038, pp.1123–1132)에서 Infra4·Infra6·Infra7 을 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://storage.googleapis.com/gweb-research2023-media/pubtools/4156.pdf",
      "source_unopened": false
    },
    {
      "id": "ref-351",
      "org": "Ren, A. Z. 외",
      "title": "Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners",
      "published": "2023-07",
      "url": "https://arxiv.org/abs/2307.01928",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "KnowNo 논문(기존 출처, arXiv 2023-07). 이번에 학회판 PMLR 229:661–682(CoRL 2023, 2023-12-02 게시)의 §3.1~3.3 에서 i.i.d.·정확한 사람 도움 가정과 시퀀스 수준 보정을 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://proceedings.mlr.press/v229/ren23a/ren23a.pdf",
      "source_unopened": false
    },
    {
      "id": "ref-620",
      "org": "국가법령정보센터(과학기술정보통신부)",
      "title": "인공지능 발전과 신뢰 기반 조성 등에 관한 기본법",
      "published": "2026-01-20",
      "url": "https://www.law.go.kr/lsInfoP.do?lsiSeq=268543",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "인공지능기본법(기존 출처). 이번에 국가법령정보센터 조문(법률 제21311호, 2026-01-20 일부개정·공포, 2026-07-21 시행)에서 제34조 1항 각 호를 확인했다. 발행일은 이 개정판의 공포일이다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://law.go.kr/lsLinkCommonInfo.do?chrClsCd=010202&lsJoLnkSeq=1031810845",
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md",
      "sections": [
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "11"
      ],
      "rationale": "갱신(차등): 섹션 3 — 67행 법·규제 문단 정정: 한국 인공지능기본법은 '2026-01-22 시행(최초 법률·시행령)'에 개정 법률 제21311호(2026-01-20 공포, 2026-07-21 시행, f48)를 더해 '개정 법률의 시행일 … 미확인'을 지움, 제34조 1항 5호 문서 작성·보관(f47, 해당성은 f49 [추정]). EU AI Act '부속서 I(기계류 등) … 고위험' 문장은 2026-07-27 통합판 기준으로 기계류 규정 (EU) 2023/1230 이 Section B(21번)로 옮겨졌고(f40) 제2조 2항이 Section B 관련 고위험 AI 에는 제6조 1항·제60a조·제102~112조만 적용한다(f41)는 점을 덧붙이고, 제43·72조를 로봇(기계류) AI 에 바로 연결하지 않음(f45 [추정]) / 섹션 4(분리 2026-09-25-area27-s4) — '등각 예측' 항목(41행)에 i.i.d. 보정 조건(f18)과 사람 도움 정확성 가정(f19) 추가, '모델 레지스트리' 항목(44행)에 별칭 반영 시점이 다음 로딩(f1)임을 보충, 배포 묶음 호환성(정규화 외부화 f3, 보정 방식 변경 f4, 메타데이터 기반 에피소드 f5) 항목 추가 / 섹션 5 — 출하 시나리오 '예외·성과' 칸(105행)에 별칭 반영 시점(f1)·오프라인 시험 한계와 카나리(f15)·롤백 연습(f16) 보강; 사례 추가: Viam 단계 배포·이전 판 고정(f12·f13, 벤더 주장 [추정]), LWD 플릿 온라인 학습(f24·f25·f26, '제조사 연구·저자 보고' 표기, 이종 플릿 아님), LG CNS 피지컬웍스 학습–운영 연계(f28~f30, 벤더 주장 [추정], 15%·18% 는 회사 기대치); 의견 f27·f31 / 섹션 6(분리 2026-09-25-area27-s6) — '모델 운영 관리' 소절(69행): MLflow 별칭 문장에 반영 시점 범위(f1, 기존 문장은 틀리지 않음 — 범위 보충), ML Test Score 28개 항목 문장 뒤에 Infra4 승인·거부(f14), Infra6 오프라인 시험 한계(f15), Infra7 롤백 연습(f16); 롤백 구현 책임·배포 중단 상태(Mender f7·f8, AWS IoT Jobs f9, Greengrass f10 — 모두 벤더 주장 [추정]) 새 소절; '필요할 때 되묻기' 소절(57행) KnowNo 문장에 보장 조건(f18·f19·f20); 의견 f2·f11·f17·f23. 기존 내용 확인(새로 넣지 않음): Mender 상태 스크립트·롤백 표시·A/B 원자 배포·단계적 배포(2026-10-09-area43-s6.md 48~50행, 2026-09-30-area43-s6.md 57행; ref-1323·ref-1324·ref-1040), aws-samples ROS 2 OTA 자동 롤백(ref-556) / 섹션 7(분리 2026-09-25-area27-s7) — 표: MLflow 행(44행)에 v3.1.0 고정 문서 근거(f1, ref-1577, ref-626 은 latest 판), LeRobot v0.6.0 호환성·LeRobotDataset v3.0 행 추가(f3~f5), NIST AI RMF 행에 MANAGE 4.1(f38, 본문 PDF ref-1586), AI-Hub 71825 행 추가(f32~f36: v1.1 2025-06-30, 2026-05-06 은 태그만, 표제 80%/10% 와 실제 약 90.9%/9.1% 불일치·검증 분할 없음, 가상환경 약 70%, 분포 비율·JSON 합계 불일치; 의견 f37). 48행 관련 법 문단: 한국 법 시행일·제34조(f47·f48·f49, 의견 f50), EU AI Act 문장에 Section B 이동·제2조 2항(f40·f41)과 제43조 4항 재평가·사전 정한 지속학습 변경 예외(f42·f43)·제72조 2항(f44)을 '조문 내용 소개'로만 넣고 기계류 연계 로봇 AI 에 바로 적용되지 않음을 명시(f45 [추정]); 의견 f46. ISO/IEC 42001 행은 그대로(이번 원문 미확인) / 섹션 8(분리 2026-09-25-area27-s8) — KnowNo 항목(41행)에 PMLR 229 학회판과 가정(f18·f19·f20), ML Test Score 항목(50행)에 Infra4·6·7(f14~f16), ACI 항목 추가(f21·f22, 로봇 실험 없음), LWD 항목 추가(f24~f26, 제조사 연구·프리프린트) / 섹션 9 — 책임 경계: 배포 후 감시·변경관리(f38)와 공급자·ROP·현장 운영자 역할 분리(의견 f39), 배포 중단·복원 상태 기록과 복구 실패 로봇의 배정 제외(의견 f11) / 섹션 11 — oq-030: '이번 실행에서는 조사하지 않았다'를 기존 내용 확인으로 갱신(2026-10-10-area25-s6.md 59~63행, 2026-10-10-area25-s11.md 41행, 후속 질문 oq-356; LTAA 75.97%·77.1%·DP 0.95 는 새 finding 으로 넣지 않음), 상태 열림 유지. id 없이 '(신규 …)'로 적힌 세 질문은 docs/open-questions.md 문구 대조로 oq-105·oq-106·oq-107 과 같으므로 id 를 붙임. 부분 답(열림 유지): oq-105(f47·f48·f49), oq-106(f40~f45: 제품 안전 구성요소 해당성은 판단하지 않고, 기계류는 Section B·제2조 2항 경로임만 확인), oq-107(f18~f23: 가정 확인, 재보정 주기 미해결), oq-213(f12·f13 Viam 단계 배포·되돌림, 벤더 주장), oq-222(f21·f22 분포 이동 아래 온라인 재보정의 조건, 배정 정책 되돌림 기준은 아님). 새 질문 4건 / 후속 정리(이번 갱신 범위 밖, 다른 페이지): docs/categories/ai-and-learning/index.md 131행·160행과 docs/categories/safety/index.md 149행의 'EU AI Act 부속서 I(기계류 등) 고위험' 서술에 Section B 이동·제2조 2항(f40·f41) 반영, index.md 160행 '2026-01-22 시행'에 개정 법률 2026-07-21 시행(f48) 반영, ref-168 저자 표기('Kaitha, S., & Yu, S. 외' → Shyam prasad reddy Kaitha·Hongrui Yu 2명), ref-626 은 latest 판이라 고정 판 ref-1577 과 구분. 다음 실행 후보: 43. 데이터·관측성·배포(f7~f13), 57. 자산·소프트웨어 수명주기 관리(f3~f6), 59. 법·규제·보험·라이선스(f40~f49)"
    }
  ],
  "glossary_candidates": [],
  "open_questions_new": [
    "학습 모델·전처리기(정규화 통계)·하드웨어 보정판이 함께 바뀌는 변경을 로봇 플릿에서 어느 시험 단위로 승인하고, 실패 시 어느 묶음 단위로 복구할 것인가? | 관련 영역: 47. AI·학습·적응과 모델 운영, 57. 자산·소프트웨어 수명주기 관리 | 근거: f6 | 종류: 일반",
    "운영 중 학습 정책을 에피소드 경계에서 갱신하는 방식이 제조사가 다른 이기종 로봇과 중간에 끊을 수 없는 장기 임무에서도 적절한가, 임무 도중 정책 판이 바뀌지 않게 하는 경계를 어떻게 정할 것인가? | 관련 영역: 47. AI·학습·적응과 모델 운영, 43. 데이터·관측성·배포 | 근거: f25 | 종류: 일반",
    "출처 충돌: AI-Hub 대규모 물리환경 로봇조작 데이터(71825)의 분할 표제(학습 80%·테스트 10%)와 건수(238,266·23,900), 원천 분포 비율(14.29%·85.71%)과 수량(77,984·184,182), 라벨링 JSON 합계(524,332)와 건수 합(262,166) 가운데 어느 값이 맞으며 실제 배포 파일과 일치하는가? | 관련 영역: 47. AI·학습·적응과 모델 운영 | 근거: f36 | 종류: 출처 충돌",
    "모델 공급자와 ROP 가 함께 확인할 수 있는 모델 변경·배포·복구 증거(판 식별, 승인 기록, 장치별 적용·롤백 결과)의 최소 항목은 무엇인가? | 관련 영역: 47. AI·학습·적응과 모델 운영, 59. 법·규제·보험·라이선스 | 근거: f39 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 15,
    "cross_checked_count": 0,
    "unverified": [
      "리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-12-04/external_research.md)를 변환했다. 2026-10-12 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.",
      "f45: EU AI Act 제2조 2항 개정에 따른 기계류 연계 로봇 AI 의 적용 조문 해석은 조문 범위에서 이끈 [추정]이다. 기계류 규정 (EU) 2023/1230 쪽에 AI 고위험 요구가 어떻게 통합되는지(제102~112조 개정 내용)와 개별 ROP 의 분류·제공자 지위는 확인하지 않음",
      "f48: 인공지능기본법 시행령의 개정 판(독립 검증 보고상 2026-08-18 공포)과 고영향 영역 목록·보존 기간은 원문 확인하지 않음. 최초 법률·시행령의 2026-01-22 시행은 기존 위키 기준(ref-620)이며 이번에 다시 대조하지 않음",
      "f32~f36: AI-Hub 71825 는 설명 페이지 메타데이터만 확인했고 실제 데이터 파일(건수·분할·실제/가상 구분)은 열지 않음. 표의 비율·합계 불일치의 정답은 제공자 확인 필요",
      "f24~f26: LWD 는 저자 전원 AGIBOT 소속의 제조사 연구 프리프린트이며 독립 재현·안전 검증·이기종 장기 운영 성과는 없음",
      "f7~f13, f28~f30: Mender·AWS·Viam·LG CNS 문서·발표만 근거라 벤더 주장 [추정]. 기존 위키는 Mender ref-1323 을 [사실]로 두었으나 이번 변환은 저장소 규칙(벤더 문서 단독 → 추정)을 적용. LG CNS 의 15%·18% 기대 효과와 PoC 현황은 독립 측정·확인 없음",
      "메모 F21(ISO/IEC 42001 공식 FAQ)은 독립 검증에서 원문을 열지 못했고(Cloudflare) 기존 위키(s7 42행, ref-618)와 중복이라 넣지 않음. ISO/IEC 42001·23894 유료 본문과 국내 로봇기업 인증 범위는 미확인",
      "메모 A15(LTAA 75.97%·77.1%·DP 0.95)는 2026-10-10 영역 25 갱신(2026-10-10-area25-s6.md 59~63행, area25-s11.md 41행, oq-356)과 완전 중복이라 새 finding 으로 넣지 않음. DP 0.95 와 Heavy Excels 77.1% 의 동일 조건 비교는 여전히 미해결",
      "MLflow 별칭 변경이 이기종 플릿 전체에 원자적으로 반영되거나 연결이 끊긴 장치에서 즉시 복구되는지, 모델·전처리·보정판을 묶은 실물 전원 차단·복구 시험 결과는 확인하지 못함",
      "KnowNo 의 물류 현장 재보정 주기(oq-107), ACI 의 피드백 지연 환경 로봇 성능, 로봇 모델별 보편 회귀 허용 임계값은 미확인",
      "메모가 조사 기준으로 쓴 고정 위키 커밋과 현재 배포판의 동일성은 확인하지 않음"
    ],
    "scope_violations": [
      "f40~f49: EU AI Act·한국 인공지능기본법의 적용 해석은 59. 법·규제·보험·라이선스 쪽 내용이므로 조문 확인과 적용 범위 주의까지만 하고 개별 제품·사업자의 의무 발생 여부는 판단하지 않음",
      "f7~f13: 장치 업데이트·단계 배포 도구(Mender·AWS IoT·Viam)는 43. 데이터·관측성·배포, 57. 자산·소프트웨어 수명주기 관리와 겹치며, 이 영역에는 모델 교체·되돌림 관점으로만 씀",
      "f24~f26: LWD 의 저수준 조작 정책 학습 자체는 로봇 자체 지능·제어(연계 대상)이며, 이 영역에는 정책 판 갱신 경계와 운영 기록 관점으로만 씀"
    ],
    "budget_used": {
      "queries": 0,
      "sources": 12
    },
    "limits": "외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 12건/15(ref-1577~ref-1588, 예약 구간 ref-1577~ref-1606 안), 재사용 3건(ref-625·ref-351·ref-620). 출처 매핑(검증 결과 기준): 메모 n1→ref-1577(MLflow v3.1.0 고정 문서; ref-626 은 latest 판이라 새 id), n2→ref-1578, n3→ref-1579, n4→ref-1580, n5→ref-1581(URL 을 /iot/latest/developerguide/ 표준 경로로), n6→ref-1582, n7→ref-351(PMLR 229 학회판으로 열람), n8→ref-1583, n9→ref-1584(뉴스와이어 재게시는 같은 출처), n10→ref-1585, n11→ref-625(DOI 10.1109/BigData.2017.8258038), n12→ref-1586(본문 PDF; 기존 ref-617 은 보도자료), n13→ref-1587(M1 Regulation (EU) 2026/1744 명시), n14→ref-620(법률 제21311호 조문), n15(ISO/IEC 42001)·n17(LTAA, ref-168)은 finding 이 없어 출처에서 뺌. 교차 확인 0건(모든 사실 finding 이 단일 출처, AWS 두 문서는 같은 기관). 검증 반영: (a) A13 에 옴니버스 2026/1744 의 Section B 이동·제2조 2항(f40·f41)을 넣고 제43·72조(f42~f44)는 조문 내용 소개로 한정, 로봇(기계류) AI 에 바로 연결하지 않는다는 점을 f45 [추정]으로 명시, oq-106 부분 답; (b) A15 LTAA 수치는 완전 중복이라 제외하고 11절 oq-030 문장 갱신만 제안; A11 의 '학습 80%' 표제를 사실로 옮기지 않고 불일치(f34·f36)와 가상환경 약 70%(f35)를 추가; LWD 는 '제조사 연구·저자 보고' 표기(f24~f26); 한국 법 시행일 2026-07-21·법률 제21311호(f48); 벤더 문서(Mender·AWS·Viam·LG CNS) 단독 finding 은 추정+벤더 주장(f7~f10, f12·f13, f28~f30); Mender 상태 스크립트·단계 배포·A/B 원자 배포, AWS ROS 2 OTA 샘플, ISO 42001 정의는 기존 내용 확인으로만 rationale 에 적음. 열린 질문: 해결 없음. 부분 답 oq-105·oq-106·oq-107·oq-213·oq-222, oq-030 은 기존 내용 확인(열림 유지). 메모 '답한 열린 질문'의 new-1~new-3 은 docs/open-questions.md 문구 대조로 oq-105·oq-106·oq-107 과 같아 새로 만들지 않음. 메모의 '새로 생긴 열린 질문' 4건은 기존 질문과 문구가 겹치지 않아 새로 올림. 메모의 '.research-work' 로컬 경로·행 번호는 쓰지 않고 원문 절·쪽·조와 위키 실제 위치를 적었다. 2026-10-10-area27-* 는 다른 영역이라 쓰지 않음. 정정 요청 없음. 용어 후보 없음."
  }
}
```

### docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md

```markdown
---
title: "47. AI·학습·적응과 모델 운영"
type: area
category: "L. AI·학습 기술"
area_no: 47
related_areas: [5, 15, 21, 25, 31, 38, 48, 54, 55, 57]
tags: [LLM 계획 접지, 등각 예측, 학습 기반 배차, 모델 레지스트리, AI 위험관리]
status: published
confidence: medium
created: 2026-09-24
updated: 2026-09-25
sources: [ref-617, ref-618, ref-619, ref-620, ref-621, ref-088, ref-092, ref-351, ref-622, ref-623, ref-624, ref-625, ref-626, ref-627, ref-354, ref-359, ref-056, ref-541, ref-417]
last_run: 2026-09-25
version: 2
---

[홈](../../index.md) › [L. AI·학습 기술](index.md) › 47. AI·학습·적응과 모델 운영

# 47. AI·학습·적응과 모델 운영

!!! info "소속 대분류"
    [L. AI·학습 기술](index.md) — 핵심 질문:
    학습·언어 모델 같은 AI 기술을 어디에 쓰고, 그 결과를 어떤 기준으로 믿을 것인가? [분류원문]

<!-- auto:area-tracks:start -->
!!! note "관련 연구 트랙"
    이 세부영역을 가로지르는 중점 연구 트랙과 확장 아이디어다. 트랙은 분류를 바꾸지 않으며, 트랙에서 확인된 사실은 이 페이지에 반영하도록 제안된다. 전체 매핑은 [확장 아이디어 연결 구조](../../ideas/index.md)에 있다.

    - [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 1. 로봇 기능 온톨로지](../../ideas/robot-capability-ontology.md)
    - [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 2. 채팅 기반 구성·운영](../../ideas/chat-based-configuration-and-operation.md)
    - [건축 도면 자동 인식](../../tracks/floorplan-recognition/index.md) — 함께 필요한 영역(○) · 확장 아이디어: [아이디어 3. 건축 도면 자동 인식](../../ideas/floorplan-recognition.md)
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 2 · 마지막 갱신: 2026-09-25 · 마지막 실행: 2026-09-25
<!-- auto:page-status:end -->

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

## 3. 왜 중요한가

AI가 만든 계획·해석을 실행에 쓰는 기준은 한 가지 장치가 아니라 실행 가능성 접지, 형식 명세·계획기 경유 검증, 불확실할 때 사람 확인, 실행 전 안전 판정, 승인된 모델 버전·시험 기준이 겹친 구조로 정리될 수 있어 보인다. [추정][^ref-088][^ref-092][^ref-056][^ref-351][^ref-359][^ref-417][^ref-625][^ref-626][^ref-618] 이 구조는 각 출처가 다루는 서로 다른 단계를 이 위키가 묶은 것이며, 하나의 출처가 제시한 채택 기준은 아니다.

기준이 필요한 이유는 모델이 한 번 넣고 끝나는 부품이 아니기 때문이다. Sculley 외(2015)는 실제 머신러닝(Machine Learning, ML) 시스템이 일반 코드의 유지보수 문제에 더해 경계 침식, 얽힘, 숨은 피드백 루프, 선언되지 않은 소비자, 데이터 의존성 등 ML 고유 위험으로 큰 유지 비용을 낳는다고 지적했다. [사실][^ref-624]

규제도 같은 방향을 가리킨다. 한국 「인공지능 발전과 신뢰 기반 조성 등에 관한 기본법」과 시행령은 2026-01-22 시행되었고, 사람의 생명·안전·기본권에 중대한 영향을 미칠 수 있는 영역의 AI를 고영향 인공지능으로 두어 별도 책무를 부과한다(기준일 2026-01-22). [사실][^ref-620] 개정 법률의 시행일과 고영향 영역 목록은 미확인이다. EU AI Act(Regulation (EU) 2024/1689)는 위험 기반 규제로, 부속서 I의 EU 조화 법령(기계류 등) 대상 제품의 안전 구성요소이거나 제품 자체이고 제3자 적합성 평가 대상인 AI 시스템을 고위험 AI로 분류한다. [사실][^ref-621] 적용 시점은 개정(AI Omnibus) 논의로 이 페이지에서 확정하지 않는다.

## 4. 핵심 개념과 용어

이 영역의 기준을 이해하려면 LLM 출력을 현실과 잇는 개념과 모델을 관리하는 개념을 함께 알아야 한다.

자세한 내용은 주제 페이지 [47. AI·학습·적응과 모델 운영 — 핵심 개념과 용어](../../topics/2026/2026-09-25-area27-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다.

**물류 흐름 단계:** 피킹, 출하

**시나리오:** 자연어 피킹 지시의 해석 검증과 출하 마감 시간대의 학습 배차 모델 교체

다음은 설명을 위한 가상의 시나리오이다. 수치는 넣지 않았고, 근거 출처의 실험 환경(가정·주방·벤치마크, 시뮬레이션 창고)은 물류 현장과 다르다.

### 가. 피킹 — 자연어 지시 해석

| 항목 | 내용 |
|---|---|
| 시작 조건 | 관리자가 “오늘 마감 주문을 B구역부터 피킹”처럼 자연어로 지시하면, LLM 해석 결과를 계획기 입력 형식으로 바꿔 검증하고 구역·마감 같은 인자가 모호하면 실행 전에 되물어야 오해석이 작업 발생으로 이어지지 않을 것으로 보인다. [추정][^ref-092][^ref-351][^ref-354] |
| 작업 대상 | 해당 없음 |
| 수행 자원 | LLM은 지시를 해석하고, ROP는 해석 결과의 채택·거부와 사람 확인 요청, 채택·거부 기록을 맡는 구조로 보인다. [추정][^ref-351] |
| 제약 | 이런 AI 활용이 인공지능 기본법의 고영향 인공지능에 해당하는지는 미확인이다(11절 열린 질문). |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해석 후보가 불확실하면 사람에게 묻는다. KnowNo는 필요할 때 사람에게 도움을 요청하게 하며 사람 도움을 줄이는 것을 목표로 한다(저자 보고). [사실][^ref-351] |

### 나. 출하 — 학습 배차 모델 교체

| 항목 | 내용 |
|---|---|
| 시작 조건 | 출하 마감 시간대에 학습 기반 배차 모델을 새 버전으로 바꾸려는 변경 요청(설명용 가정) |
| 작업 대상 | 해당 없음 |
| 수행 자원 | 창고 다중 로봇 작업 배정을 강화학습 정책으로 수행하는 방법이 연구되어 있다(RTAW, 시뮬레이션 창고 조건). [사실][^ref-623] |
| 제약 | 해당 없음 |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 모델 레지스트리의 버전·별칭으로 교체·되돌림 경로를 두고 교체 전 시험·감시 기준을 통과시켜야, 데이터 의존성·숨은 피드백 루프 같은 ML 고유 위험에서 오는 배정 품질 저하가 출하 지연으로 번지는 것을 막을 수 있을 것으로 보인다. [추정][^ref-626][^ref-625][^ref-623][^ref-624] |

피킹 시나리오에서 이 영역이 관여하는 칸은 시작 조건(지시가 작업으로 바뀌는 순간)과 예외·성과(되묻기)다. 출하 시나리오에서는 모델 교체가 예외·성과 칸의 위험이 된다.

국내 기사에 따르면 한진은 대전 메가허브에 AI 기반 적재량 예측 시스템을 적용해 간선차량 상·하차 종료 시점을 미리 파악하고 다음 차량 접안 대기시간을 줄였다고 한다. [추정] 벤더 주장[^ref-627] 이런 예측을 ROP 관점에서 쓴다면 ROP의 몫은 입출고 시간·접안·현장 상·하차 작업의 동기화까지이고, 간선 배차·운송계획은 분류 원문 19장 “거점 간 운송”의 연계 대상이다([범위 경계](../../about/scope-boundary.md)).

## 6. 대표 접근법과 기술

LLM이 만든 계획은 실행 가능성 확인, 형식 검증, 되묻기, 안전 판정을 거쳐야 하고, 학습 모델은 운영 중 버전·시험 관리가 따로 필요하다. [추정][^ref-088][^ref-626] 3절의 겹 구조를 이 위키가 그린 도식은 주제 페이지에 있다.

자세한 내용은 주제 페이지 [47. AI·학습·적응과 모델 운영 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area27-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

조직 차원의 AI 위험관리·관리 체계 표준과 모델 운영 도구, 평가용 데이터가 이 영역의 기준을 받친다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [47. AI·학습·적응과 모델 운영 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area27-s7.md)에 있다.

## 8. 대표 연구와 자료

이 절의 자료는 대부분 원문 미열람 상태에서 검색 결과로 확인했고, AmbiK와 LoTa-Bench는 검증 과정에서 공식 저장소 README로 확인했다. 수치는 저자 보고다.

자세한 내용은 주제 페이지 [47. AI·학습·적응과 모델 운영 — 대표 연구와 자료](../../topics/2026/2026-09-25-area27-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

ROP가 직접 맡을 AI 관련 몫은 LLM·학습 모델이 낸 계획·배정·해석을 실행에 채택하는 기준과 검증 단계, 사람 확인 요청, 채택·거부 기록, 운영 모델의 버전·변경 승인 관리로 보인다. [추정][^ref-618][^ref-617][^ref-619][^ref-351][^ref-626]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | AI가 낸 계획의 실행 가능 여부 확인, 채택·거부와 기록 | 인식 출력 처리·파지·저수준 동작 정책을 학습하거나 생성하는 모델(연계 대상) |
| 상위 업무 시스템 | 주문·납기 제약을 받은 배정·계획 모델의 버전·변경 승인 | 수요예측 모델(연계 대상) |
| 거점 간 운송 | 입출고 시간·접안·현장 상·하차 작업 동기화 | 간선 배차·운송계획(연계 대상) |

연계 대상: Code as Policies의 저수준 정책 코드, SayCan의 사전 학습 기술 같은 저수준 정책·파지 학습과 수요예측 모델은 로봇 자체 지능·제어와 상위 업무 시스템 쪽이며, ROP는 그 결과와 가능 여부를 받아 쓰는 쪽으로 보인다. [추정][^ref-622][^ref-088] 조직 차원의 AI 관리 체계(ISO/IEC 42001)와 위험관리(NIST AI RMF, ISO/IEC 23894)는 ROP의 채택 기준을 둘러싼 운영 틀로 보인다. [추정][^ref-618][^ref-617][^ref-619] 경계는 제품 전략에 따라 이동할 수 있으며, 자세한 기준은 [범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

분류 개정 전 원문 8장의 교차 규칙에 따라 이 영역의 AI 방법은 적용 대상 영역과 양쪽으로 연결된다.

자세한 내용은 주제 페이지 [47. AI·학습·적응과 모델 운영 — 다른 연구영역과의 연결](../../topics/2026/2026-09-25-area27-s10.md)에 있다.

## 11. 열린 질문

아직 확인하지 못한 사실과 판단이 필요한 쟁점은 다음과 같다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- **oq-030** (상태: 열림) 출처 충돌: LTAA(arXiv 2512.02810) 초록 요약은 로봇 전문화가 강한 설정에서 LLM 배정이 작업 완료율 77%로 전통 기법을 모두 앞섰다고 하지만, 다른 2차 요약은 동적 계획법의 완료율이 더 높다고 적는다. 어느 쪽이 원문 결과인가? 이번 실행에서는 조사하지 않았다.
- (신규, 상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-68) 물류 현장 로봇의 작업 계획·배정에 쓰는 AI가 한국 인공지능 기본법의 고영향 인공지능 영역에 해당하는가, 해당하면 ROP 사업자와 현장 운영사 중 누가 책무를 지는가?[^ref-620]
- (신규, 상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-68) LLM이나 학습 모델이 ROP의 정지·경로·구역 결정에 관여할 때 EU AI Act가 말하는 제품 안전 구성요소로 볼 수 있는가?[^ref-621]
- (신규, 상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-68) KnowNo의 등각 예측 보장은 보정 데이터와 운영 분포가 같다는 조건에 기대는데, 물류 지시 분포가 계절·고객에 따라 바뀔 때 보정을 얼마나 자주 다시 해야 하는가?[^ref-351]

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-25 · 갱신 · [47. AI·학습·적응과 모델 운영](ai-learning-adaptation-and-model-operations.md) — 영역 심화: 3~11절 신규 작성(LLM 계획 접지·검증·되묻기·안전 판정, 학습 기반 배차, 모델 운영, AI 위험관리 표준·법), 페이지 상태 자동 영역 추가, 각주 19건. 2차: 7·8절 도입 문장의 태그·각주 제거, 6절 도식 지시어 수정 (실행 2026-09-25-68)
- 2026-09-25 · 생성 · [47. AI·학습·적응과 모델 운영 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area27-s6.md) — 자동 분리: 27. AI·학습·적응과 모델 운영 의 "6. 대표 접근법과 기술" 절(1,218자)을 옮겼다 (실행 2026-09-25-68)
- 2026-09-25 · 생성 · [47. AI·학습·적응과 모델 운영 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-25-area27-s7.md) — 자동 분리: 27. AI·학습·적응과 모델 운영 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,001자)을 옮겼다. 2차: 도입 문장의 [사실] 태그와 ref-618 각주를 떼어 안내 문장으로 바꿨다 (실행 2026-09-25-68)
- 2026-09-25 · 생성 · [47. AI·학습·적응과 모델 운영 — 대표 연구와 자료](../../topics/2026/2026-09-25-area27-s8.md) — 자동 분리: 27. AI·학습·적응과 모델 운영 의 "8. 대표 연구와 자료" 절(969자)을 옮겼다. 2차: 도입 문장의 태그·각주 제거와 README 확인 출처 명시, KnowNo 항목 문구 수정(필요할 때·저자 보고) (실행 2026-09-25-68)
- 2026-09-25 · 생성 · [47. AI·학습·적응과 모델 운영 — 다른 연구영역과의 연결](../../topics/2026/2026-09-25-area27-s10.md) — 자동 분리: 27. AI·학습·적응과 모델 운영 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(760자)을 옮겼다. 본문 링크를 주제 페이지 위치 기준 경로(../../categories/…)로 고쳤다 (실행 2026-09-25-68)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-617]: NIST, NIST Risk Management Framework Aims to Improve Trustworthiness of Artificial Intelligence, 2023-01-26, https://nist.gov/news-events/news/2023/01/nist-risk-management-framework-aims-improve-trustworthiness-artificial, 접근일 2026-09-25 (원문 미열람)
[^ref-618]: ISO/IEC, ISO/IEC 42001:2023 - AI management systems, 2023, https://www.iso.org/standard/42001, 접근일 2026-09-25 (원문 미열람)
[^ref-619]: ISO/IEC, ISO/IEC 23894:2023 - AI — Guidance on risk management, 2023-02, https://www.iso.org/standard/77304.html, 접근일 2026-09-25 (원문 미열람)
[^ref-620]: 국가법령정보센터(과학기술정보통신부), 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법, 미확인, https://www.law.go.kr/lsInfoP.do?lsiSeq=268543, 접근일 2026-09-25 (원문 미열람)
[^ref-621]: European Commission, AI Act (Shaping Europe's digital future), 미확인, https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai, 접근일 2026-09-25 (원문 미열람)
[^ref-088]: Ahn, M. 외, Do As I Can, Not As I Say: Grounding Language in Robotic Affordances, 2022-04, https://arxiv.org/abs/2204.01691, 접근일 2026-09-25 (원문 미열람)
[^ref-092]: Liu, B. 외, LLM+P: Empowering Large Language Models with Optimal Planning Proficiency, 2023-04, https://arxiv.org/abs/2304.11477, 접근일 2026-09-25 (원문 미열람)
[^ref-351]: Ren, A. Z. 외, Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners, 2023-07, https://arxiv.org/abs/2307.01928, 접근일 2026-09-25 (원문 미열람)
[^ref-622]: Liang, J. 외, Code as Policies: Language Model Programs for Embodied Control, 2022-09, https://arxiv.org/abs/2209.07753, 접근일 2026-09-25 (원문 미열람)
[^ref-623]: Agrawal, A. 외, RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments, 2022-09, https://arxiv.org/abs/2209.05738, 접근일 2026-09-25 (원문 미열람)
[^ref-624]: Sculley, D. 외, Hidden Technical Debt in Machine Learning Systems, 2015, https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems, 접근일 2026-09-25 (원문 미열람)
[^ref-625]: Breck, E. 외 (Google Research), The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction, 2017, https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/, 접근일 2026-09-25 (원문 미열람)
[^ref-626]: MLflow (Linux Foundation 오픈소스 프로젝트), ML Model Registry (MLflow AI Platform), 미확인, https://mlflow.org/docs/latest/ml/model-registry/, 접근일 2026-09-25 (원문 미열람)
[^ref-627]: 머니투데이, 포장은 로봇이, 간선운송은 무인차가…물류현장 스며든 '피지컬 AI', 2026-09-19, https://www.mt.co.kr/industry/2026/09/19/2026091818023697394, 접근일 2026-09-25 (원문 미열람)
[^ref-354]: cog-model (AmbiK 저자), AmbiK-dataset — README (AmbiK: Dataset of Ambiguous Tasks in Kitchen Environment), 미확인, https://github.com/cog-model/AmbiK-dataset, 접근일 2026-09-25 (원문 미열람)
[^ref-359]: Wang, W. 외, Learning to Ask: When LLM Agents Meet Unclear Instruction, 2024-09, https://arxiv.org/abs/2409.00557, 접근일 2026-09-25 (원문 미열람)
[^ref-056]: Liu, J. X. 외, Grounding Complex Natural Language Commands for Temporal Tasks in Unseen Environments, 2023-02, https://arxiv.org/abs/2302.11649, 접근일 2026-09-25 (원문 미열람)
[^ref-417]: arXiv (SafeGate 저자, 저자명 미확인), Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems, 2026-04, https://arxiv.org/abs/2604.05427, 접근일 2026-09-25 (원문 미열람)
```

### data/area_reflection_proposals.json (대상 영역 47. AI·학습·적응과 모델 운영 에 대한 트랙 반영 제안 15건, status 제안 — 반영은 이 실행에서: 사양서 6.3 절차 9·공통 규칙 11)

```json
{
  "items": [
    {
      "run_id": "2026-09-25-71",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 3,
      "area_no": 47,
      "section": "6. 대표 접근법과 기술",
      "summary": "트랙 단계 3(실행 2026-09-25-71): 신경-기호 구조 — SDI(LLM 은 언어 이해만, 검증·순서·실행은 결정적, ref-674), SPCA(Plan 단계 PDDL·LLM·하이브리드 수용, 하이브리드 파이프라인은 [추정], ref-675·ref-676), 관리형 블랙보드(에이전트·휴리스틱·최적화 모듈 제안을 결정적 검증·원자적 반영으로만 수용, ref-711), LLM 출력 반영 직전 단계 경계마다 검증 게이트를 두는 배치([추정]). 적용 대상 13. 작업 배정 — MRTA 와 함께 연결한다.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-71",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 3,
      "area_no": 47,
      "section": "8. 대표 연구와 자료",
      "summary": "SDI 기호 검증기 절제 실험: 검증기를 같은 방식으로 프롬프트한 LLM 으로 바꾸면 성공률 98.1%→3.8%(그룹 A–D 52개 명령 부분집합, 저자 보고값, 독립 재현 미확인, 원문 미열람, ref-674).",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-74",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 3,
      "area_no": 47,
      "section": "6. 대표 접근법과 기술",
      "summary": "LLM 과 해법기를 함수 호출로 결합해 IIS 로 불능 원인을 찾고 설명·수정 제안을 내는 OptiChat(f11), 내성적 계획과 등각 예측 결합(f16), 명세·모델 불확실성을 나눈 EVPI 기반 되묻기(f17). 적용 대상 13. 작업 배정 — MRTA·18. 사람–로봇 협업·운영 인터페이스와 양쪽 연결.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-74",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 3,
      "area_no": 47,
      "section": "8. 대표 연구와 자료",
      "summary": "해결 불가 설명 연구: Göbelbecker 외 excuse(ICAPS 2010, f9), Sreedharan 외 plan advice 해결 불가 설명(f10), CE-MRS(IEEE RA-L 9권 2024, f12). 계획 실패 유형 벤치마크 Plan-Failure-Bench(f19)는 개인 연구자의 동료심사 전 자료로 신뢰도 low 참고 사례로만 표시.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-77",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 3,
      "area_no": 47,
      "section": "8. 대표 연구와 자료",
      "summary": "교차 규칙에 따라 LLM 에이전트의 사용자 끼어들기(추가·수정·철회) 적응 한계를 보고한 InterruptBench(웹 탐색 조건, 저자 보고, ref-684)와 채팅 의도 변경이 재계획·재배정을 촉발하는 CoMuRoS(실험실 조건, ref-677)를 적용 대상 13. 작업 배정 — MRTA·14. 작업 순서·스케줄링과 함께 연결.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-79",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 4,
      "area_no": 47,
      "section": "6. 대표 접근법과 기술",
      "summary": "LLM 로봇 계획·배정 출력의 형식 논리 가드레일(Safety Chip, RoboGuard 92% → 2.5% 미만 저자 보고, SafePlan, SafeGate)을 소개하고 적용 대상 13. 작업 배정 — MRTA·18. 사람–로봇 협업·운영 인터페이스에 연결한다. 로봇 쪽 안전 기능은 연계 대상으로 짧게 둔다.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-79",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 4,
      "area_no": 47,
      "section": "8. 대표 연구와 자료",
      "summary": "사람의 관리·감독 규정으로 EU AI Act 제14조 제4항 (b)호의 자동화 편향 인식 요구([추정], 공식 관보 원문 미확인)와 한국 인공지능기본법 제34조(고영향 인공지능 사업자의 사람의 관리·감독 조치)를 자료로 추가한다. 물류 배정 AI 의 해당 여부는 oq-105.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-80",
      "date": "2026-09-25",
      "track": "floorplan-recognition",
      "stage": 5,
      "area_no": 47,
      "section": "6. 대표 접근법과 기술",
      "summary": "도면 해석 모델의 평가 지표: 모서리·방·각도 정밀도·재현율·F1(Floor-SP), 파놉틱 품질(FloorPlanCAD), 클래스별 IoU(CubiCasa5K), 엣지 F1(Raster-to-Graph), IoU·그래프 편집 거리 가중합(SSIG). 분류 원문 8장 교차 규칙에 따라 적용 대상 6. 지도·공간·위치 모델과 양쪽 연결 (근거 f1·f2·f3·f4·f6, 실행 2026-09-25-80)",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-98",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 5,
      "area_no": 47,
      "section": "6. 대표 접근법과 기술",
      "summary": "LLM 해석·출력 평가 지표: 의도 정확도·슬롯 F1·전체 정확도(SLU 서베이), 결합 목표 정확도의 과소평가와 상대 슬롯 정확도(ACL 2022), 도구 호출 AST·실행 평가(BFCL), LLM 직접 최적화의 실행 가능성–최적성 분리(ConstraintBench). 적용 대상 13. 작업 배정 — MRTA·18. 사람–로봇 협업·운영 인터페이스와 함께 연결한다.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-99",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 5,
      "area_no": 47,
      "section": "6. 대표 접근법과 기술",
      "summary": "LLM 기반 챗봇 평가 방법: LLM 모의 사용자와 끝 상태 채점·pass^k(τ-bench), 모의 사용자가 실제 사용자 성과를 체계적으로 틀리게 추정한다는 보고(Lost in Simulation, 게재처 미확인), 결정적 설정에서도 LLM 정확도가 반복 실행마다 달라진다는 보고(Atil 외, arXiv 판 기준). 모의 관리자 결과의 실제 표본 보정과 반복 분포 보고는 추정. 적용 대상 13. 작업 배정 — MRTA·23. 시험·형식 검증·벤치마크와 연결.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-81",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 4,
      "area_no": 47,
      "section": "6. 대표 접근법과 기술",
      "summary": "LLM 출력 검증 방법: 구조화 출력의 스키마 준수와 값 오류 한계([추정] 벤더 주장, ref-362), 제약 디코딩 벤치마크(ref-749·ref-750), LTL 제약 디코딩(ref-761), 판정자 LLM(ref-754), 방법별로 놓치는 오류([추정] 이 위키의 종합). 적용 대상 13. 작업 배정 — MRTA·18. 사람–로봇 협업·운영 인터페이스와 함께 연결. 근거 f2·f3·f12·f19·f22(실행 2026-09-25-81).",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-82",
      "date": "2026-09-25",
      "track": "floorplan-recognition",
      "stage": 5,
      "area_no": 47,
      "section": "6. 대표 접근법과 기술",
      "summary": "도면 해석 모델을 정확도가 아니라 사람 수정 노력으로 평가하는 방법: 편집 비용([사실], ref-793), 클릭 수([사실], ref-795), 전문가 편집 이력 데이터셋 A-Scan2BIM과 연산 순서·다음 벽 예측 평가([사실], ref-797·ref-798). 분류 원문 8장 교차 규칙에 따라 적용 대상 6. 지도·공간·위치 모델과 양쪽에 연결.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-83",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 4,
      "area_no": 47,
      "section": "6. 대표 접근법과 기술",
      "summary": "LLM 에이전트 권한 통제 연구: Conseca 의 과제별 즉시 정책과 결정적 집행([사실] ref-771), 인증된 위임([사실] ref-770), Progent 의 도구·인자 규칙 정책([추정] ref-769, 수치는 요약마다 다름), AgentGuard 의 속성 기반 접근 통제([추정] ref-772, 세부 미확인), LLM 생성 정책의 보장 부족을 지적한 MiniScope([추정] ref-773), 도구 호출 출처 기록 서베이([추정] ref-776). 적용 대상 13. 작업 배정 — MRTA·18. 사람–로봇 협업·운영 인터페이스와 양쪽 연결.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-85",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 4,
      "area_no": 47,
      "section": "6. 대표 접근법과 기술",
      "summary": "트랙 자연어 업무 지시 챗봇 q4-04(f1·f3·f4·f5·f18): 불확실성 기반 되묻기 기준(KnowNo 등각 예측, 내성적 계획, SAGE-Agent EVPI, 저자 보고값)과 AmbiK 모호성 탐지 한계를 적고, 불확실성 점수와 규칙 조건을 함께 쓰는 선택지(추정)를 둔다. 적용 대상인 13. 작업 배정 — MRTA와 18. 사람–로봇 협업·운영 인터페이스에 함께 연결한다.",
      "status": "제안"
    },
    {
      "run_id": "2026-09-25-86",
      "date": "2026-09-25",
      "track": "chat-based-configuration-and-operation",
      "stage": 5,
      "area_no": 47,
      "section": "6. 대표 접근법과 기술",
      "summary": "모듈형 접지 구조가 직접 코드 생성 기준선보다 조작 과제 성공률이 높았다는 보고(원인: 접지 부족·개루프 실행, 로봇 자체 지능·제어는 연계 대상), 기호 검증기를 LLM 으로 바꾼 절제 실험의 성공률 급락(98.1%→3.8%, 산업 셀·저자 보고), 결정적 설정 LLM 의 반복 정확도 변동(최대 15%), LLM 이 루프 밖에서 설계한 스케줄링 규칙(제조·AGV 시뮬레이션). 적용 대상 13. 작업 배정 — MRTA 와 함께 연결",
      "status": "제안"
    }
  ]
}
```

### docs/categories/ai-and-learning/robot-foundation-models-and-llm-planning.md (요약)

```markdown
# 44. 로봇 기반 모델·언어 모델 계획

소속 대분류: L. AI·학습 기술 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

시각–언어–행동 모델 같은 로봇 기반 모델의 흐름과 언어 모델 기반 작업 계획 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **언어 모델 기반 작업 계획**: 언어 모델 에이전트로 작업을 계획·분해하는 방법과 한계를 다룬다
- **로봇 기반 모델·임바디드 AI 동향**: 시각–언어–행동 모델, 범용 로봇·휴머노이드 같은 흐름이 오케스트레이션에 주는 영향을 추적한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 27번 영역 ‘AI·학습·적응과 모델 운영’에서 왔다. 그 본문은 [47. AI·학습·적응과 모델 운영](ai-learning-adaptation-and-model-operations.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

범용 로봇 모델과 언어 모델은 오케스트레이션의 무엇을 바꾸는가? [분류원문]
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

### docs/categories/space-and-map-model/map-space-and-location-model.md (요약)

```markdown
# 15. 지도·공간·위치 모델

소속 대분류: D. 공간·지도 모델 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

로봇마다 다른 지도·좌표·층을 하나의 공간 모델로 통합하고 위치 신뢰도를 관리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **로봇별 지도·좌표계 정렬**: 제조사마다 다른 지도·좌표계·층 표현을 하나의 공통 좌표로 맞춘다
- **다층·수직 이동 모델**: 층·승강기·계단·경사로의 연결과 통과 조건을 모델링한다
- **공간 그래프**: 이동 가능한 공간을 노드·연결·통과 조건의 그래프로 표현한다(IndoorGML 등)
- **위치추정 신뢰도 관리**: 로봇이 보고한 위치를 얼마나 믿을 수 있는지 판단하고 오류를 감지한다
- **실외·광역 지도**: GIS·도로망·위성 위치를 실내 지도와 이어 붙인다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [14. 도면·BIM에서 지도 만들기](maps-from-floor-plans-and-bim.md), [16. 장소 의미·지도 관리](place-semantics-and-map-management.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 6번 영역 ‘지도·공간·위치 모델’(옛 대분류 B. 공통 정보·환경 모델)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: BIM·CAD·센서 지도에서 이동 공간과 경로를 만들고, 로봇별 좌표계·층·목적지를 정렬 [옛 분류원문]

> 옛 질문: 제조사마다 다른 지도에서 ‘3층 출하 대기장’을 어떻게 동일한 장소로 인식할까? [옛 분류원문]

> 옛 원문 주석: 6번에는 지도 생성뿐 아니라 **현장과 도면의 차이 확인, 지도 버전 관리, 위치추정 결과의 신뢰도**도 포함해야 한다. [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

제조사마다 다른 지도·좌표·층을 어떻게 하나의 공간으로 맞출 것인가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

> 원문 주석: 지도는 한 번 만들고 끝나지 않는다. **현장과 도면의 차이 확인(14번), 좌표 정렬과 위치추정 신뢰도(15번), 지도 버전 관리(16번)**가 함께 필요하다. [분류원문]
```

### docs/categories/integration/interoperability-standards-and-conformance.md (요약)

```markdown
# 21. 상호운용 표준·적합성

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-10-11 · 버전: 3

## 1. 한 줄 정의

로봇 상호운용 표준을 채택·변환하고 적합성을 시험한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **상호운용 표준 채택**: VDA 5050·MassRobotics 상호운용 표준·Open-RMF·ROS 2·OPC UA 같은 표준을 채택하고 서로 변환한다
- **적합성 시험**: 표준과 연동 규격을 지키는지 시험한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [58. 다사업자 책임·계약·데이터](../governance-law-and-society/multi-party-responsibility-contracts-and-data.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 28번 영역 ‘표준·상호운용성·다사업자 거버넌스’(옛 대분류 G. 안전·보안·지능·거버넌스)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 공통 규격, 적합성 시험, 제조사 간 책임, 데이터 소유권, API 변경 정책, 서비스 수준과 감사 이력 [옛 분류원문]

> 옛 질문: 제조사·ROP·설비업체 중 누가 연동 오류를 수정하고 변경을 승인할까? [옛 분류원문]

## 2. 핵심 질문

어떤 상호운용 표준을 따르고, 제조사가 그 표준을 지키는지 어떻게 확인할 것인가? [분류원문]
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

### docs/categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md (요약)

```markdown
# 38. 모니터링·이상 탐지·원인 분석

소속 대분류: J. 현장 운영·관제 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-10-09 · 버전: 3

## 1. 한 줄 정의

감시, 로봇 건강 상태 진단, 이상 탐지, 원인 분석, 알림 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **운영 모니터링**: 로그·이벤트·지표를 연결해 현재 운영을 감시한다
- **이상 탐지**: 평소와 다른 지연·정지·패턴을 찾아낸다
- **원인 분석**: 지연의 원인이 로봇·설비·통신·앞 작업 가운데 어디인지 가려낸다
- **알림·에스컬레이션**: 이상·지연·안전 사건을 알맞은 사람에게 알리고 필요하면 상위로 올린다
- **로봇 건강 상태 진단**: 배터리·모터·센서·통신 상태를 모아 로봇별 건강 상태를 보여 주고 이상을 알린다

이전 분류(2026-09-24)에서 이 페이지는 옛 19번 영역 ‘모니터링·이상 탐지·원인 분석’(옛 대분류 E. 협업·현장 운영)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 로그·이벤트·성능 지표를 연결해 이상을 탐지하고, 로봇·설비·통신·공정 원인을 구분 [옛 분류원문]

> 옛 질문: 지연 원인이 로봇 고장인지, 문인지, 앞 공정인지 어떻게 찾을까? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

지연의 원인이 로봇인지, 설비인지, 통신인지, 앞 작업인지 어떻게 찾을까? [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]
```

### docs/categories/safety/safety-and-risk-management.md (요약)

```markdown
# 48. 안전·위험 관리

소속 대분류: M. 안전 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-10-11 · 버전: 4

## 1. 한 줄 정의

위험성 평가, 안전 책임 경계, 정지·재개, 비상 대응 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **위험성 평가**: 로봇·사람·설비가 함께 움직일 때 새로 생기는 위험을 찾고 평가한다
- **정지·재개 절차**: 비상 정지·보호 정지와 재개 조건을 정한다
- **비상 상황 대응**: 화재·대피·정전 때 로봇·승강기·통로를 어떻게 할지 정한다
- **안전 책임 경계**: 제조사·플랫폼·설비업체·현장의 안전 책임을 나눈다

이전 분류(2026-09-24)에서 이 페이지는 옛 25번 영역 ‘안전·위험 관리’(옛 대분류 G. 안전·보안·지능·거버넌스)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 로봇·사람·설비 상호작용의 위험, 안전 조건, 정지·재개 절차, 비상 상황 대응, 안전 책임 경계 [옛 분류원문]

> 옛 질문: 여러 장비는 각각 안전해도 함께 움직일 때 새로운 위험이 생기지 않는가? [옛 분류원문]

## 2. 핵심 질문

여러 장비는 각각 안전해도 함께 움직일 때 새로운 위험이 생기지 않는가? [분류원문]
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

### docs/categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md (요약)

```markdown
# 55. 현장 조사·설치·시운전

소속 대분류: O. 검증·도입·수명주기 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

현장 조사, 설치·설정, 교정, 시운전, 인수 시험 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **현장 설치·설정**: 로봇·충전기·네트워크·설비를 설치하고 설정하며, 반복되는 설치 절차를 자동화한다
- **교정**: 센서·좌표·지도를 현장에 맞게 교정한다
- **현장 시운전**: 연동과 작업을 현장에서 시험 운전하며 문제를 잡는다
- **현장 조사**: 설치 전에 현장 치수·네트워크·설비·동선을 조사한다
- **인수 시험**: 합의한 수용 기준으로 인수 여부를 판정한다

이전 분류의 이 영역 가운데 일부는 새 분류에서 [4. 이기종 로봇 등록](../robot-ontology/heterogeneous-robot-registration.md)(으)로 나뉘었다. 그 영역들은 이 페이지의 본문을 출발점으로 삼는다.

이전 분류(2026-09-24)에서 이 페이지는 옛 21번 영역 ‘온보딩·설정·현장 시운전’(옛 대분류 F. 도입·검증·유지관리)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 로봇 등록, 기능 탐색, 문서 분석, 지도·설비 설정, 교정, 설치 절차 자동화 [옛 분류원문]

> 옛 질문: 새 제조사나 새 물류센터를 추가할 때 반복 작업을 얼마나 줄일까? [옛 분류원문]

> 옛 원문 주석: 27번의 AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 5·21번, 도면 해석은 6번, 학습 기반 배차는 13번, 장애 분석은 19번**에 적용되는 연구 방법이다. [옛 분류원문]

## 2. 핵심 질문

새 현장에 설치하고 시운전할 때 반복 작업을 얼마나 줄일 수 있는가? [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]
```

### docs/categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md (요약)

```markdown
# 57. 자산·소프트웨어 수명주기 관리

소속 대분류: O. 검증·도입·수명주기 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

정비·고장 예측, 버전 관리, 장비 교체, 폐기 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **정비·고장 예측**: 고장을 예측하고 예방 정비를 계획하며 배터리 열화를 관리한다
- **소프트웨어·펌웨어·어댑터 버전 관리**: 펌웨어·어댑터·지도·모델 버전의 호환을 관리하고, 바뀔 때 다시 검증할 범위를 정하며 배포·복구한다
- **장비 교체**: 로봇을 바꿀 때 설정·지도·능력 정의를 새 장비로 옮긴다
- **폐기·데이터 삭제**: 로봇과 시스템을 폐기할 때 데이터를 지우고 자산을 처리한다

이전 분류(2026-09-24)에서 이 페이지는 옛 24번 영역 ‘자산·소프트웨어 수명주기 관리’(옛 대분류 F. 도입·검증·유지관리)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 고장 예측·정비, 배터리 열화, 펌웨어·어댑터·지도·모델 버전, 배포·복구, 장비 교체 [옛 분류원문]

> 옛 질문: 제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? [옛 분류원문]

## 2. 핵심 질문

제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 19건 / 전체 1486건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-056 | Liu, J. X. 외 | Grounding Complex Natural Language Commands for Temporal Tasks in Unseen Environments | 2023-02 | https://arxiv.org/abs/2302.11649 | 2026-09-25 | 아니오 |
| ref-088 | Ahn, M. 외(Google) | Do As I Can, Not As I Say: Grounding Language in Robotic Affordances | 2022-04 | https://arxiv.org/abs/2204.01691 | 2026-09-25 | 아니오 |
| ref-092 | Liu, B., Jiang, Y., Zhang, X., Liu, Q., Zhang, S., Biswas, J., & Stone, P. | LLM+P: Empowering Large Language Models with Optimal Planning Proficiency | 2023-04 | https://arxiv.org/abs/2304.11477 | 2026-09-25 | 아니오 |
| ref-351 | Ren, A. Z. 외 | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners | 2023-07 | https://arxiv.org/abs/2307.01928 | 2026-09-25 | 아니오 |
| ref-354 | cog-model (AmbiK 저자) | AmbiK-dataset — README (AmbiK: Dataset of Ambiguous Tasks in Kitchen Environment) | 미확인 | https://github.com/cog-model/AmbiK-dataset | 2026-09-25 | 예 |
| ref-359 | Wang, W. 외 | Learning to Ask: When LLM Agents Meet Unclear Instruction | 2024-09 | https://arxiv.org/abs/2409.00557 | 2026-09-25 | 아니오 |
| ref-417 | Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab) | Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems | 2026-04 | https://arxiv.org/abs/2604.05427 | 2026-09-25 | 아니오 |
| ref-541 | lbaa2022 (LoTa-Bench 공식 저장소) | LLMTaskPlanning — LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents (ICLR 2024) (GitHub README) | 미확인 | https://github.com/lbaa2022/LLMTaskPlanning | 2026-09-25 | 예 |
| ref-617 | NIST | NIST Risk Management Framework Aims to Improve Trustworthiness of Artificial Intelligence | 2023-01-26 | https://nist.gov/news-events/news/2023/01/nist-risk-management-framework-aims-improve-trustworthiness-artificial | 2026-09-25 | 아니오 |
| ref-618 | ISO/IEC | ISO/IEC 42001:2023 - AI management systems | 2023 | https://www.iso.org/standard/42001 | 2026-09-25 | 아니오 |
| ref-619 | ISO/IEC | ISO/IEC 23894:2023 - AI — Guidance on risk management | 2023-02 | https://www.iso.org/standard/77304.html | 2026-09-25 | 아니오 |
| ref-620 | 국가법령정보센터(과학기술정보통신부) | 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법 | 미확인 | https://www.law.go.kr/lsInfoP.do?lsiSeq=268543 | 2026-09-25 | 아니오 |
| ref-621 | European Commission | AI Act | Shaping Europe's digital future | 미확인 | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | 2026-09-25 | 아니오 |
| ref-622 | Liang, J. 외 | Code as Policies: Language Model Programs for Embodied Control | 2022-09 | https://arxiv.org/abs/2209.07753 | 2026-09-25 | 아니오 |
| ref-623 | Agrawal, A. 외 | RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments | 2022-09 | https://arxiv.org/abs/2209.05738 | 2026-09-25 | 아니오 |
| ref-624 | Sculley, D. 외 | Hidden Technical Debt in Machine Learning Systems | 2015 | https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems | 2026-09-25 | 아니오 |
| ref-625 | Breck, E. 외 (Google Research) | The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction | 2017 | https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/ | 2026-09-25 | 아니오 |
| ref-626 | MLflow (Linux Foundation 오픈소스 프로젝트) | ML Model Registry | MLflow AI Platform | 미확인 | https://mlflow.org/docs/latest/ml/model-registry/ | 2026-09-25 | 아니오 |
| ref-627 | 머니투데이 | 포장은 로봇이, 간선운송은 무인차가…물류현장 스며든 '피지컬 AI' | 2026-09-19 | https://www.mt.co.kr/industry/2026/09/19/2026091818023697394 | 2026-09-25 | 아니오 |
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

### docs/open-questions.md (요약: 대상 영역 [47] 에 걸린 10건 / 전체 393건)

```markdown
- oq-030 [열림] 출처 충돌: LTAA(arXiv 2512.02810) 초록 요약은 로봇 전문화가 강한 설정에서 LLM 배정이 작업 완료율 77%로 전통 기법을 모두 앞섰다고 하지만, 다른 2차 요약은 동적 계획법의 완료율이 더 높다고 적는다. 어느 쪽이 원문 결과인가? (영역 25, 47)
- oq-104 [열림] 창고 이동로봇 플릿의 재배정·재스케줄링 주기에서 LLM 추론 지연이 허용되는 한계를 측정했거나, LLM 을 결정 루프 밖에 둔 운영 사례가 있는가? (영역 26, 47)
- oq-105 [열림] 물류 현장 로봇의 작업 계획·배정에 쓰는 AI 가 한국 인공지능 기본법의 고영향 인공지능 영역에 해당하는가, 해당하면 ROP 사업자와 현장 운영사 중 누가 책무를 지는가? (영역 21, 47)
- oq-106 [열림] LLM 이나 학습 모델이 ROP 의 정지·경로·구역 결정에 관여할 때 EU AI Act 가 말하는 제품 안전 구성요소로 볼 수 있는가? (영역 47, 48)
- oq-107 [열림] KnowNo 의 등각 예측 보장은 보정 데이터와 운영 분포가 같다는 조건에 기대는데, 물류 지시 분포가 계절·고객에 따라 바뀔 때 보정을 얼마나 자주 다시 해야 하는가? (영역 31, 47)
- oq-222 [열림] 학습된 배정·경로 정책을 현장에 쓸 때 분포 이동을 감지해 탐색·규칙 기반 정책으로 되돌리는 기준을 정한 연구나 제품이 있는가? (영역 46, 47)
- oq-315 [열림] 언어 모델 기반 고장 진단(REFLECT, SYSDIAGBENCH)을 제조사가 다른 이동로봇 플릿의 실행 기록·오류 코드에 적용해 원인 분석 정확도를 측정한 사례가 있는가? (영역 47, 38, 44)
- oq-316 [열림] 로봇 플랫폼의 AI 구성요소가 EU AI Act 고위험 AI 로 분류되면 제12조 자동 사건 기록 요건을 플랫폼 실행 기록이 충족해야 하는가, 그 기록의 보관 주체는 플랫폼 사업자와 배포자 가운데 누구인가? (영역 47, 37, 43)
- oq-356 [열림] LTAA 의 결정적 비교군(brute force·greedy·DP)과 확률적 비교군(LTAA·Q-learning·DQN)을 같은 성공 확률 모델과 작업 집합으로 재평가한 공개 재현 자료가 있는가? (관련 기존 질문: oq-030) (영역 25, 47)
- oq-381 [열림] SafeGate 논문의 충돌률(CR)은 실행된 작업이 0건일 때 어떻게 산정되며, 표 II 의 183건과 전체 230건 사이에서 빠진 47건은 어떤 범주(판단 보류 등)인지 저자 코드·원자료로 재현할 수 있는가? (영역 48, 47)
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

### runs/2026-10-12-01/research.md

```markdown
# 리서치 브리프 2026-10-12-01

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-12-01 |
| 날짜 | 2026-10-12 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 58. 다사업자 책임·계약·데이터 |
| 대분류 | P. 거버넌스·법규·사회 |

## 갭(비어 있거나 약한 섹션)

- 섹션 4. 핵심 개념과 용어(분리 2026-09-30-area58-s4) — '데이터 보유자' 항목(40행)이 '사용자 동의 없이 비개인 데이터를 이용할 수 없다'로 데이터법 제4조(13)의 '사용자와의 계약을 근거로만'과 다르고, 근거가 해설 페이지(ref-1191)뿐
- 섹션 5. 적용 사례 — 병원 사례가 2025 공고 하나(ref-872, 각주에 '원문 미열람')에 기대며 '연 2회 평가·인증'(71행 표 '수행 자원', 76행 본문)을 원어 'bi-annual' 의 한 해석으로 단정, 2026 공고(연례·AutoveX 2026-09-01부터 2년) 미반영. 상업·물류 현장의 실제 공개 계약 문안(지원 응답·시설 장애·책임 상한) 사례 없음
- 섹션 6. 대표 접근법과 기술(분리 2026-09-30-area58-s6) — 데이터 계약 소절(51·53행)에 '쉽게 이용 가능한 데이터' 범위·제3조(1) 설계 의무의 별도 적용일·MCT/SCC 의 제3자 면책 공백 없음. 변경 주체 책임 소절에 EU 제조물책임지침(소프트웨어 포함·실질적 변경자·업무용 재산 제외·증거 공개 비례성) 없음. 서비스 수준 소절(65행)이 ISO/IEC 19086-1(원문 미열람) 일반론뿐이라 응답·복구 시계, 시설 장애 예외, API 가용성 측정식 같은 실제 조항 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스(분리 2026-09-30-area58-s7) — 표에 EU 제조물책임지침과 RFC 9745(폐기 예고·종료 시각) 행이 없고, 데이터법 행(41행)이 일반 적용일만 적음
- 섹션 8. 대표 연구와 자료 — 세 건뿐이며 데이터 접근 거절(영업비밀) 관할별 관행을 다룬 동료심사 연구 없음
- 섹션 11. 열린 질문(분리 2026-09-30-area58-s11) — oq-241·oq-268·oq-279·oq-280·oq-259·oq-185 에 붙일 공개 원문 근거 없음
- 정정 요청 없음(target.json corrections 비어 있음). 메모·검증에서 나온 위키 내부 정정: s4.md 40행 데이터 보유자 정의, 본 페이지 71·76행 '연 2회', ref-872·ref-706 의 '원문 미열람' 표시

## 조사 질문

1. 제조사·플랫폼·설비업체 중 누가 연동 오류를 고치고 변경을 승인할까? [분류원문]
2. EU 데이터법에서 데이터 보유자의 비개인 데이터 이용 근거와 사용자에게 제공할 데이터 범위, 설계 의무의 적용 시점은 원문상 무엇인가(oq-279·oq-320)? (섹션 4·6·7 겨냥)
3. 공개된 모델 계약 조항·표준 계약 조항과 EU 개정 제조물책임지침은 제3자 청구·소프트웨어 결함·실질적 변경·증거 공개를 다사업자 사이에서 어떻게 다루는가(oq-241·oq-289)? (섹션 6·7 겨냥)
4. 로봇 서비스·관제 플랫폼의 공개 약관은 지원 응답 시간·시설 장애 예외·책임 상한·과금 단위·가용성 측정을 어떻게 정하는가(oq-112·oq-268)? (섹션 5·6 겨냥)
5. API 폐기 예고와 종료 시각의 관계를 정한 표준은 무엇을 정하고 무엇을 계약에 남기는가(oq-280)? (섹션 7 겨냥)
6. 통합자 사전 자격(RoMi-H 등재)의 주기·유효기간과, 영상 처리 위탁·데이터 접근 거절의 관리 기준은 공개 원문상 무엇인가(oq-149·oq-259)? (섹션 5·6·8 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | EU 데이터법(Regulation (EU) 2023/2854) 제4조(13)은 데이터 보유자가 쉽게 이용 가능한 데이터 가운데 비개인 데이터를 사용자와의 계약을 근거로만 이용할 수 있다고 정하고, 그 데이터로 사용자의 경제 상황·자산·생산 방식을 추론해 사용자의 시장 지위를 해치는 이용을 금지한다. | ref-636 | 아니오 | medium | 2026-10-12 | — | — |
| f2 | [사실] | 데이터법 제4조(1)은 사용자가 연결 제품·관련 서비스에서 데이터에 직접 접근할 수 없을 때 데이터 보유자가 '쉽게 이용 가능한 데이터'와 그 해석·이용에 필요한 관련 메타데이터를 지체 없이 무료로 제공하도록 하며, 제2조(17)은 '쉽게 이용 가능한 데이터'를 데이터 보유자가 과도한 노력 없이 연결 제품·관련 서비스에서 적법하게 얻거나 얻을 수 있는 제품 데이터·관련 서비스 데이터로 정의한다. | ref-636 | 아니오 | medium | 2026-10-12 | — | — |
| f3 | [사실] | 데이터법 제50조는 이 규정을 2025-09-12부터 적용한다고 하면서, 제3조(1)의 설계 의무(연결 제품·관련 서비스를 데이터에 직접 접근 가능하게 설계·제조할 의무)는 2026-09-12 후에 시장에 출시되는 연결 제품과 관련 서비스에 적용한다고 따로 정한다. | ref-636 | 아니오 | medium | 2026-10-12 | — | — |
| f4 | [사실] | 집행위원회 권고 초안 부속서(C(2025) 7750 final ANNEX, 2025-11-19)의 클라우드 표준 계약 조항(SCC) 중 책임 조항 설명(Annex X)은 '이 SCC 는 면책(indemnification) 조항을 포함하지 않는다'고 적고, 한 당사자의 중대한 의무 위반으로 생긴 제3자 청구에 대해 면책·보호 조항이 필요한지와 그 범위를 당사자가 검토하도록 권한다. | ref-1489, ref-1192 | 아니오 | medium | 2026-10-12 | — | — |
| f5 | [사실] | EU 개정 제조물책임지침(Directive (EU) 2024/2853) 제4조(1)은 '제품'에 소프트웨어를 포함하고, 제2조(2)는 상업 활동 밖에서 개발·공급된 자유·오픈소스 소프트웨어에는 지침을 적용하지 않는다고 정한다. | ref-1490 | 아니오 | medium | 2026-10-12 | — | — |
| f6 | [사실] | 같은 지침 제8조(2)는 제조자의 통제 밖에서 제품을 실질적으로 변경한 뒤 시장에 내놓거나 사용에 투입한 자연인·법인을 그 제품의 제조자로 본다. | ref-1490 | 아니오 | medium | 2026-10-12 | — | — |
| f7 | [사실] | 지침 제2조(1)의 적용 대상은 2026-05-07 정오표(OJ L 2026/90364)로 '2026-12-09 후'에서 '2026-12-08 후(after 8 December 2026)' 시장에 출시되거나 사용에 투입된 제품으로 고쳐졌으며, 따라서 2026-12-09 당일부터 출시·투입되는 제품에 적용된다. | ref-1490 | 아니오 | medium | 2026-10-12 | — | — |
| f8 | [사실] | 지침 제22조(1)은 회원국이 지침 이행 법령을 2026-12-09까지 시행하도록 정하고, 제21조는 구 제조물책임지침 85/374/EEC 를 2026-12-09 부로 폐지하되 그 전에 출시·사용 투입된 제품에는 계속 적용한다고 정한다. | ref-1490 | 아니오 | medium | 2026-10-12 | — | — |
| f9 | [사실] | 지침 제6조(1)(b)(iii)은 전적으로 업무 목적으로만 쓰는 재산의 손해를 이 지침의 보상 대상 손해에서 제외한다. | ref-1490 | 아니오 | medium | 2026-10-12 | — | — |
| f10 | [사실] | 지침 제9조(3)은 같은 조 제1·2항에 따른 증거 공개를 필요하고 비례적인 범위로 제한하도록 회원국에 요구하고, 제9조(4)는 그 판단에서 제3자를 포함한 모든 당사자의 정당한 이익, 특히 기밀·영업비밀 보호를 고려하게 한다. | ref-1490 | 아니오 | medium | 2026-10-12 | — | — |
| f11 | [사실] | 창이종합병원 CHART 의 2025년 RoMi-H 등재 공고는 프로그램을 'a bi-annual RoMi-H Empanelment Program'으로 적고, 같은 공고에서 등재 통합자 5개사(HOPE Technik, Medisys Innovation, Panasonic Asia Pacific, QuikBot Technologies, Techfox)의 등재가 2025-05-01부터 2년간 유효하다고 게시한다. | ref-872 | 아니오 | medium | 2026-10-12 | — | — |
| f12 | [추정] | 2025년 공고의 'bi-annual'은 '연 2회'로도 '2년마다'로도 읽힐 수 있고 같은 공고가 등재 유효기간을 2년으로 적고 있어, 위키 5절의 '연 2회 평가·인증'(본문 76행, 표 '수행 자원' 행)은 원어 인용과 두 해석을 함께 적거나 [추정]으로 낮춰야 한다. | ref-872, ref-1495 | 아니오 | low | 2026-10-12 | — | — |
| f13 | [사실] | SingHealth/CHART 의 2026년 RoMi-H 등재 공고(2026-05-06 게시, 2026-08-24 갱신)는 CHART 가 연례(annual) 등재 프로그램을 운영해 통합자의 RoMi-H 배치 역량을 평가·재평가한다고 적고, 등재 통합자는 CHART 웹사이트에 공개되어 공공 의료기관이 제안요청(RFP/RFI) 참여를 위해 연락할 수 있다고 적는다. | ref-1495 | 아니오 | medium | 2026-10-12 | 병원 / 수행 자원 | — |
| f14 | [사실] | 2026년 공고의 등재 명단은 AutoveX Pte Ltd 1개사이며 등재는 2026-09-01부터 2년간 유효하다. | ref-1495 | 아니오 | medium | 2026-10-12 | 병원 / 수행 자원 | — |
| f15 | [사실] | 개인정보보호위원회는 「이동형 영상정보처리기기를 위한 개인영상정보 보호ㆍ활용 안내서」 발표 보도자료(2024-10-14 게시)에서 외부업체 위수탁으로 개인영상정보를 처리하는 경우 보호책임자 지정과 주기적인 점검ㆍ교육 등으로 안전하게 관리할 것을 당부했다. | ref-1494 | 아니오 | medium | 2026-10-12 | — | — |
| f16 | [사실] | RFC 9745(2025-03, Standards Track) §5 는 자원을 폐기 예정(deprecated)으로 표시하는 행위가 자원의 동작을 바꾸지 않으며, 클라이언트는 폐기 표시 전과 같은 방식으로 자원을 계속 쓸 수 있다고 정한다. | ref-706 | 아니오 | medium | 2026-10-12 | — | — |
| f17 | [사실] | RFC 9745 §4 는 Sunset 헤더(RFC 8594)로 자원이 응답하지 않게 될 시각을 함께 알릴 수 있게 하고, Sunset 시각이 Deprecation 시각보다 빨라서는 안 된다(MUST NOT)고 정하며, 두 시각 사이의 최소 간격은 정하지 않는다. | ref-706 | 아니오 | medium | 2026-10-12 | — | — |
| f18 | [사실] | De Noyette·Stähler·Margoni(IIC 56(5):984–1014, 2025)는 데이터법의 영업비밀 체계를 분석하며, 회원국 관할 당국마다 영업비밀 관련 행정 관행이 달라져 더 파편화될 위험이 있다고 지적한다. | ref-1488 | 아니오 | medium | 2026-10-12 | — | — |
| f19 | [추정] | Relay Robotics 공개 약관의 서비스 수준 부속서(Exhibit A)에 따르면 Tier 1(24시간 콜센터)은 서비스 개시일 이후 이메일 지원 요청을 받은 뒤 60분 안에 응답하도록 '상업적으로 합리적인 노력'을 기울이는 조건이며, 복구 완료 시각을 보장하는 문구는 아니다. | ref-1491 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f20 | [추정] | Relay 약관의 같은 부속서 예외 조항에 따르면 고객의 네트워크나 시설(예: 승강기 고장)에서 생긴 문제는 고객이 고칠 때까지 지원 기한이 연장되고, Relay 는 고객 네트워크·시설 문제의 수리 책임을 지지 않는다. | ref-1491 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f21 | [추정] | Relay 약관 §12 에 따르면 면책 의무, 고객의 라이선스 위반, 양측의 비밀유지 위반을 제외한 각 당사자의 책임은 청구 발생 전 18개월 동안 고객이 지급했거나 지급할 요금 총액을 넘지 않으며, 약관 준거법은 미국 캘리포니아주법이다. | ref-1491 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f22 | [추정] | Relay 약관 §5.2 에 따르면 당사자 사이에서 고객이 Relay 와 공유하기로 한 개인정보는 고객 소유이며, Relay 는 서비스 제공 목적에만 쓴다. | ref-1491 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f23 | [추정] | Formant 일반 약관(2026-04-16 갱신)에 따르면 고객이 지정한 통합자('Development Consultant')는 고객의 지시로만 일하며 고객이 그 통합자의 작위·부작위에 책임을 진다. | ref-1496 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f24 | [추정] | Formant 약관의 'Device' 정의에 따르면 하나의 장치에 가상 환경(PLC, Jetson, 가상 머신 등)이 둘 이상 있으면 가상 환경마다 별도 Device 로 센다. | ref-1496 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f25 | [추정] | Formant 약관의 Formant AI 추가 조건에 따르면 고객은 AI 출력에 의존하거나 그 출력으로 명령을 실행하기 전에 출력을 검증하는 사람의 검토 절차를 사용 과정에 두어야 한다. | ref-1496 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f26 | [추정] | AIRROBO(Best Epoch Technology)의 EU 데이터법 고지 §4(b)에 따르면 사용자는 앱에서 데이터를 내보내 한 번에 공유하거나, 승인된 QR 코드로 제3자와 지속 공유할 수 있으며 지속 공유를 받으려는 제3자는 Tuya 클라우드 플랫폼에 등록해야 한다. | ref-1487 | 아니오 | low | 2026-10-12 | 가정 / 작업 대상 | 벤더 주장 |
| f27 | [추정] | AWS IoT RoboRunner 서비스 수준 협약(2022-11-28 갱신)에 따르면 'Error'는 500 또는 503 오류 코드를 돌려준 요청이고, 가용성은 5분 구간마다 오류 없이 처리된 요청 비율로 계산한다. | ref-1492 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f28 | [추정] | 같은 SLA 는 요청이 하나도 없던 5분 구간을 가용성 100%로 간주한다. | ref-1492 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f29 | [추정] | 1X Technologies 의 사전예약 약관(2025-10-28 갱신) §2.4 에 따르면 주문 초대를 받아 로봇을 받으려는 사람은 구매 시점에 제시되는 별도 판매약관(Terms of Sale)에 동의해야 하며, 취소·배송·보증 세부는 주문 초대나 판매약관에 둔다. | ref-1493 | 아니오 | low | 2026-10-12 | 가정 | 벤더 주장 |
| f30 | [의견] | ROP 의 데이터 자산 대장은 데이터 항목마다 데이터법상 역할(사용자·데이터 보유자·제3자), 이용 근거(사용자와의 계약), 요청 가능 범위(쉽게 이용 가능한 데이터·메타데이터), 연결 제품의 출시일(2026-09-12 후 출시 여부)을 따로 기록하고, 개인정보 처리 근거는 별도로 심사하는 편이 좋다. | ref-636 | 아니오 | low | 2026-10-12 | — | — |
| f31 | [의견] | 다사업자 계약은 클라우드 SCC 의 책임 조항을 그대로 옮기지 말고, 로봇 제조사·통합자·시설 관리주체·플랫폼 사이의 제3자 청구 면책을 따로 정해야 하며, 제조물책임지침이 업무 전용 재산 손해를 보상 대상에서 빼므로 사업장 설비·재고 손해는 계약 조항으로 다룰 필요가 커 보인다. | ref-1489, ref-1490 | 아니오 | low | 2026-10-12 | — | — |
| f32 | [의견] | ROP 는 사고 뒤 증거 공개가 법원 판단으로 필요·비례 범위에 한정된다는 점을 전제로, 로그 보관 기간·사고 후 동결·내보내기 형식·영업비밀 분리 절차를 계약 부속서에 미리 정해 두는 편이 좋다. | ref-1490 | 아니오 | low | 2026-10-12 | — | — |
| f33 | [의견] | 서비스 수준 부속서는 응답 시각·원인 분석·복구 완료 시각을 나누고, 시설 장애로 지원 기한이 멈추는 구간의 시작·종료와 확인 주체를 기록하며, API 오류율과 별도로 작업 성공률·지연·시설 대기 시간을 지표로 합의하는 편이 좋다. | ref-1491, ref-1492 | 아니오 | low | 2026-10-12 | — | — |
| f34 | [의견] | 플랫폼 약관과 고객–통합자 계약을 함께 대조해 통합자 행위의 책임 귀속, 과금 수량 단위(로봇 대수·가상 환경·설치 인스턴스)의 대응표와 계량 이의 절차, AI 출력으로 명령을 실행할 때의 검토자·승인 기록을 정하는 편이 좋다. | ref-1496, ref-1491 | 아니오 | low | 2026-10-12 | — | — |
| f35 | [의견] | 제조사의 데이터법 고지가 안내하는 내보내기·제3자 지속 공유 경로는 ROP 온보딩 때 제3자 등록·필드 목록·지연·승인 철회를 직접 시험해 확인하는 편이 좋다. | ref-1487 | 아니오 | low | 2026-10-12 | — | — |
| f36 | [의견] | 통합자 등재(사전 자격)는 연동 역량 평가일 뿐이므로, 등재 사실과 별도로 인수 기준·장애 복구 책임·등재 유효기간 만료 시 처리를 계약에 적는 편이 좋다. | ref-872, ref-1495 | 아니오 | low | 2026-10-12 | 병원 / 완료·인계 | — |
| f37 | [의견] | ROP 어댑터는 제조사 API 의 폐기 예고 시각·종료(Sunset) 시각·전환 문서 링크를 따로 저장하고, 두 시각 사이의 최소 통지 기간은 RFC 가 정하지 않으므로 계약에서 따로 확인하는 편이 좋다. | ref-706 | 아니오 | low | 2026-10-12 | — | — |
| f38 | [의견] | 영상 처리를 다른 사업자에게 맡길 때는 위탁 범위·보호책임자·교육·주기 점검 증빙을 계약 부속서로 관리하고, 데이터 접근 거절(영업비밀) 사유와 이의 경로는 관할별로 기록하되 법학 논문의 제안을 검증된 운영 성과로 표시하지 않는 편이 좋다. | ref-1494, ref-1488 | 아니오 | low | 2026-10-12 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-636 | European Union (EUR-Lex) | Regulation (EU) 2023/2854 of the European Parliament and of the Council of 13 December 2023 on harmonised rules on fair access to and use of data (Data Act) | 2023-12-13 | 정부·연구기관 | high | 2026-10-12 | https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng | 아니오 |
| ref-1192 | European Commission (Shaping Europe's digital future) | Draft Recommendation on non-binding model contractual terms on data access and use and non-binding standard contractual clauses for cloud computing contracts | 2025-11-19 | 정부·연구기관 | high | 2026-10-12 | https://digital-strategy.ec.europa.eu/en/library/draft-recommendation-non-binding-model-contractual-terms-data-access-and-use-and-non-binding | 아니오 |
| ref-872 | Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART) | RoMi-H Empanelment Programme 2025 | 2025-05-01 | 정부·연구기관 | medium | 2026-10-12 | https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste | 아니오 |
| ref-706 | IETF (RFC Editor) | RFC 9745: The Deprecation HTTP Response Header Field | 2025-03 | 표준 | high | 2026-10-12 | https://www.rfc-editor.org/info/rfc9745/ | 아니오 |
| ref-1487 | Best Epoch Technology Co., Ltd. (AIRROBO) | EU DATA ACT Notice | 미확인 | 벤더 문서 | medium | 2026-10-12 | https://owebsite-cdn.ubtrobot.com/resources/file/2025/12/25/755762357268549.pdf | 아니오 |
| ref-1488 | De Noyette, E., Stähler, L., Margoni, T. (IIC 56(5)) | Data Secrets: The Data Act's New Trade Secrets Framework | 2025-04-24 | 논문 | medium | 2026-10-12 | https://link.springer.com/article/10.1007/s40319-025-01601-9 | 아니오 |
| ref-1489 | European Commission | ANNEX to the Communication to the Commission — Approval of the draft Commission Recommendation on non-binding model contractual terms on data access and use and non-binding standard contractual clauses for cloud computing contracts (with Annexes), C(2025) 7750 final | 2025-11-19 | 정부·연구기관 | high | 2026-10-12 | https://ec.europa.eu/newsroom/dae/redirection/document/121719 | 아니오 |
| ref-1490 | European Union (EUR-Lex) | Directive (EU) 2024/2853 of the European Parliament and of the Council of 23 October 2024 on liability for defective products and repealing Council Directive 85/374/EEC | 2024-11-18 | 정부·연구기관 | high | 2026-10-12 | https://eur-lex.europa.eu/eli/dir/2024/2853/oj/eng | 아니오 |
| ref-1491 | Relay Robotics | Terms of Service (Exhibit A: Service Level Agreement) | 2023-03-01 | 벤더 문서 | medium | 2026-10-12 | https://relayrobotics.com/tos | 아니오 |
| ref-1492 | Amazon Web Services | AWS IoT RoboRunner Service Level Agreement | 2022-11-28 | 벤더 문서 | medium | 2026-10-12 | https://aws.amazon.com/roborunner/sla/ | 아니오 |
| ref-1493 | 1X Technologies, Inc. | Pre-Order Terms | 2025-10-28 | 벤더 문서 | medium | 2026-10-12 | https://www.1x.tech/legal | 아니오 |
| ref-1494 | 개인정보보호위원회 | 자율주행 인공지능(AI) 발전을 위한 개인영상정보 보호ㆍ활용 기준 나왔다 | 2024-10-14 | 정부·연구기관 | high | 2026-10-12 | https://pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=10678 | 아니오 |
| ref-1495 | SingHealth / Changi General Hospital CHART | RoMi-H Empanelment Programme 2026 | 2026-05-06 | 정부·연구기관 | medium | 2026-10-12 | https://www.singhealth.com.sg/news/robotics/romi-h-empanelment-programme-2026 | 아니오 |
| ref-1496 | Formant | General Terms | 2026-04-16 | 벤더 문서 | medium | 2026-10-12 | https://www.formant.ai/terms_of_use | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md | 4, 5, 6, 7, 8, 11 | 갱신(차등): 섹션 4(분리 2026-09-30-area58-s4) — 40행 '데이터 보유자' 항목 정정: '사용자와 계약을 맺어야 하고 사용자 동의 없이 비개인 데이터를 이용할 수 없다'[사실][^ref-1191] → '쉽게 이용 가능한 비개인 데이터를 사용자와의 계약을 근거로만 이용할 수 있고, 사용자의 시장 지위를 해치는 추론에 쓸 수 없다'(f1, 근거 ref-636 원문). '쉽게 이용 가능한 데이터' 범위(f2)를 같은 항목이나 새 줄로 / 섹션 5 — 병원 사례: 71행 표 '수행 자원'과 76행 본문의 '연 2회'를 원어 'bi-annual'(2025 공고) 인용과 두 해석(연 2회/2년마다) 병기 또는 [추정]으로 정정(f11·f12), 2025 등재 5개사·2년 유효(f11), 2026 공고의 연례 표현·RFP/RFI 연락 경로(f13)와 AutoveX 2026-09-01부터 2년(f14)을 추가하고 '(2025-05 기준)'을 연차별로 나눔. ref-872 각주의 '(원문 미열람)' 해소. 의견 f36. 새 사례 블록(배송 로봇 서비스 계약; 약관이 현장 유형을 특정하지 않아 '병원·호텔 배송 로봇 업체의 공개 약관'으로만 표기): Relay 약관의 Tier 1 60분 응답 노력(f19), 시설 장애(승강기 고장) 시 지원 기한 연장(f20)을 '단일 업체 약관에 따르면' [추정]·벤더 주장으로, 완료·인계/예외·성과는 미확인. 가정 사례에 AIRROBO 고지의 QR 지속 공유 경로(f26)와 1X 사전예약 약관의 판매약관 위임(f29)을 [추정]·벤더 주장으로 짧게; 의견 f35 / 섹션 6(분리 2026-09-30-area58-s6) — 데이터 접근·공유 계약 소절: 일반 적용일(기존 51행) 뒤에 제3조(1) 설계 의무는 2026-09-12 후 출시 제품에만 적용(f3), 제4조(1)·(13) 범위와 계약 근거(f1·f2); MCT/SCC 문단(53행) 뒤에 부속서 X 의 면책 조항 부재와 제3자 청구 검토 권고(f4); 의견 f30·f31. 변경 주체 책임 소절: EU 개정 제조물책임지침의 다사업자 책임 관점 핵심만 — 소프트웨어 포함·비상업 FOSS 제외(f5), 실질적 변경자=제조자(f6), 적용 대상 '2026-12-08 후' 출시·투입 = 2026-12-09부터(f7, 정오표 2026-05-07; '2026-12-08부터'로 쓰지 말 것), 이행 기한 2026-12-09·구 지침 폐지(f8), 업무 전용 재산 손해 제외(f9), 증거 공개 필요·비례성과 영업비밀 고려(f10); 의견 f31·f32. 서비스 수준 약속과 감사 이력 소절: 공개 약관 비교 — Relay 책임 상한 18개월 요금·예외 3가지·캘리포니아 준거법(f21), 개인정보 고객 귀속(f22), Formant 통합자 책임 고객 귀속(f23)·가상 환경별 Device 계수(f24)·AI 출력 사람 검토(f25), AWS RoboRunner Error=500/503·5분 가용성·요청 없는 구간 100%(f27·f28) — 모두 [추정]·벤더 주장, 문장에 'OO사 약관에 따르면', 단일 업체 사례로 한정하고 업체 간 교차 확인으로 세지 않음; 의견 f33·f34. 영상 위탁 관리: 개인정보위 보도자료의 위수탁 시 보호책임자·주기 점검·교육 당부(f15)를 한두 문장으로만 넣고 53영역으로 연결; 의견 f38 / 섹션 7(분리 2026-09-30-area58-s7) — 데이터법 행(41행)에 '제3조(1)은 2026-09-12 후 출시 제품' 추가(f3). 행 추가: EU 개정 제조물책임지침(Directive (EU) 2024/2853, 소프트웨어 포함·실질적 변경자·적용 2026-12-09부터·이행 기한 2026-12-09, f5~f8), RFC 9745(폐기 표시는 동작 불변, Sunset≥Deprecation, 최소 간격 미규정, f16·f17); 의견 f37 / 섹션 8 — 연구 항목 추가: De Noyette·Stähler·Margoni(IIC 2025) 데이터법 영업비밀 체계와 관할별 행정 관행 파편화 위험(f18); 기존 MCT 항목(109행)은 기존 내용 확인(부속서 X 면책 공백은 6절로) / 섹션 11(분리 2026-09-30-area58-s11) — 해결 없음. 부분 근거: oq-241(f19~f25, 네 당사자 공통 분담표는 여전히 없음), oq-268(f24·f27·f28·f20; 메모의 'Formant 가상 환경 수량 공동 검증 주문서' 질문은 oq-268 의 하위 질문이라 새로 만들지 않음), oq-279·oq-320(f1·f2, 특정 ROP 지위 미판정), oq-280·oq-207(f16·f17, 로봇 계약상 최소 통지 일수 미확인), oq-259(f15), oq-185(f29, 원격 조작자 책임 미확인), oq-249(f10 은 법원 증거 공개 범위일 뿐 기계 규정 로그 의무의 플랫폼 적용은 미판정), oq-289(f5·f6 원문 조문만, 오케스트레이션 SW 해당 여부 미판정), oq-149(f13·f14, 국내 사례 없음), oq-110(f1~f3·f26). 답하지 못함: oq-145, oq-265, oq-281(가이드 본문 미열람), oq-282, oq-283, oq-290. 새 질문 3건 / 기존 내용 확인(새로 넣지 않음): MCT·SCC 사용이 자발적이라는 점(메모 F04) — s6.md 53행·s7.md 42행·본 페이지 109행·용어집 model-contractual-terms; 데이터법 일반 적용일 2025-09-12 — s6.md 51행·s7.md 41행; RFC 9745 Sunset≥Deprecation — 2026-09-25-area28-s4.md 40행(원문 미열람 근거였음); 증거 공개 제도 자체 — 2026-09-30-area59-s6.md 45행; 영상 위탁 점검 — privacy-and-video-data.md 108행(기사 ref-1136 근거) / 후속 정리(이번 갱신 범위 밖, 다른 페이지): docs/glossary/data-holder.md 정의가 '연결 제품' 정의처럼 잘못 쓰임, docs/categories/security-and-privacy/index.md 169행의 비슷한 서술(ref-1274, ref-1191 과 같은 EC 해설 페이지), docs/topics/2026/2026-09-25-area28-s3.md 41행 '주요 조항의 적용 개시일은 미확인'(f3 로 해소 가능), docs/topics/2026/2026-09-30-area03-s7.md 44행·2026-09-30-area56-s7.md 46행 '연 2회'(f12), 59영역(2026-09-30-area59-s3·s4·s6·s7·s8, glossary/product-liability.md, standards/index.md 342행)의 제조물책임지침 서술 근거를 Gibson Dunn 해설(ref-1227)에서 원문(ref-1490)으로, 53영역 108행 근거를 1차 보도자료(ref-1494)로, ref-706 서지(발행 2025-03, 원문 열람). EU AI법 제25·26조 서술(s6.md 43·65행)은 개정 여부 점검 필요(미확인). 다음 실행 후보: 59. 법·규제·보험·라이선스(f5~f10), 63. 병원·의료(f11~f14), 3. 경제성·조달·사업 모델(f24·f27·f28) |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- 여러 사업자가 얽힌 장애·사고에서 서비스 수준 협약의 지원 기한을 멈추는 사유(시설 장애 등)와 재개 시점을 누가 확인·승인하며, 각 계약의 로그를 어떤 공통 식별자로 연결하는가? (관련: oq-112) | 관련 영역: 58. 다사업자 책임·계약·데이터, 32. 예외 복구·재계획·업무 연속성 | 근거: f20 | 종류: 일반
- 제조사의 데이터법 고지가 안내하는 제3자 지속 공유 경로(승인 QR 코드·외부 플랫폼 등록 등)는 실제로 어떤 필드를 어떤 지연으로 제공하며, 사용자가 승인을 철회하면 언제 공유가 끊기는가? (관련: oq-110, oq-279) | 관련 영역: 58. 다사업자 책임·계약·데이터, 20. 로봇·제조사 관제 연동 | 근거: f26 | 종류: 일반
- RoMi-H 통합자 등재 프로그램의 실제 운영 주기는 무엇인가(2025 공고 'bi-annual', 2026 공고 'annual', 등재 유효 2년), 그리고 유효기간이 끝난 등재 통합자가 맡은 연동의 유지·장애 복구 책임은 어떻게 이어지는가? (관련: oq-149) | 관련 영역: 58. 다사업자 책임·계약·데이터, 63. 병원·의료 | 근거: f12 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 14 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 10건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-12-01/external_research.md)를 변환했다. 2026-10-12 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.
    - f4: C(2025) 7750 final 의 권고가 최종 채택(관보 게재)되었는지와 다국어본 공개 상태는 확인하지 못함(EC 페이지는 2026-03-03 갱신에도 Draft 표기). 합리적 보상 지침의 후속 발표 여부도 미확인
    - f5~f10: 회원국별 제조물책임지침 이행 법령과 국내 제조물책임법의 소프트웨어 포함 개정 여부(oq-290)는 확인하지 못함. 오케스트레이션 소프트웨어가 제품·관련 서비스에 해당하는지(oq-289)는 판단하지 않음
    - f11·f12: 2025 공고 'bi-annual'의 의도(연 2회/2년마다)는 공고 원문만으로 확정할 수 없음
    - f15: 개인정보위 보도자료는 독립 검증 보고의 원문 대조 기준이며, 안내서 본문(ref-1135)과 개인정보 보호법 조문은 이번에 다시 열지 않음
    - f18: 논문 §4.1.4 구절은 독립 검증 보고의 원문 대조 기준(로컬 저장본은 접근 차단 페이지), 서지는 Crossref 로 확인
    - f19~f29: 벤더 약관은 공개 웹 문안이며 개별 체결본·주문서·단가·이행 실적은 미확인. AWS IoT RoboRunner 의 조사일 현재 신규 제공·지원 상태 미확인(지원 종료 공지는 찾지 못함). AIRROBO 고지의 발행일 미확인(PDF 작성 2025-12-23)
    - 검증 보고의 2차 자료 언급: 데이터법 개정안(Digital Omnibus, COM(2025) 837)이 협상 중으로 보이고 EU AI법이 개정되었다는 점은 원문으로 확인하지 않아 finding 으로 넣지 않음 — s6.md 의 AI법 제25·26조 서술 영향은 후속 점검
    - oq-145(모델 대체·라우팅 희석 계약), oq-265(R15.08-3 사용자 의무), oq-281(산업데이터 계약 가이드 432쪽 본문), oq-282(기계 규정 실질적 변경과 플랫폼 설정 변경), oq-283(로봇-승강기 연동 표준 결과물)은 이번 메모가 답하지 못함
- 범위 경계 위반 의심:
    - f5~f10: EU 제조물책임지침의 법적 효력·적용 판단은 59. 법·규제·보험·라이선스 쪽 내용이므로 조문 확인까지만 하고 다사업자 책임 관점 핵심만 씀
    - f15: 영상 위탁 관리는 53. 개인정보·영상 데이터와 겹치며, 이 영역에는 계약 부속서 관리 관점의 짧은 연결로만 씀
    - f11~f14: RoMi-H 등재는 63. 병원·의료와 겹치며, 이 영역에는 통합자 사전 자격과 책임 주체 관점으로만 씀
    - f16·f17: RFC 9745 는 41. 플랫폼 아키텍처·외부 API, 21. 상호운용 표준·적합성과 겹치며, 이 영역에는 제조사 API 폐기 통지의 계약 관점으로만 씀
- 한계: 외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 10건/15(ref-1487~ref-1496, 예약 구간 ref-1487~ref-1516 안), 재사용 4건(ref-636·ref-1192·ref-872·ref-706). 출처 매핑(검증 결과 기준): 메모 n1→ref-636, n2→ref-1487(UBTech CDN), n3→ref-1488, n4→ref-1192, n5→ref-1489(미러 dirittobancario.it 대신 공식 EC URL), n6→ref-1490(EUR-Lex 원문; ref-1227 은 해설이라 쓰지 않음), n7→ref-1491(약관 표기 2023-03-01), n8→ref-1492, n9→ref-1493, n10→ref-1494(안내서 ref-1135·기사 ref-1136 과 별개 1차 보도자료), n11→ref-1495, n12→ref-872, n13→ref-706(원문 열람), n14→ref-1496. 교차 확인 0건(모든 사실 finding 이 단일 출처이거나 같은 기관 계열: EC 발표·부속서, CHART 2025·2026 공고) — 신뢰도 medium 이하. 벤더 약관 11건(Relay·Formant·AIRROBO·AWS·1X)은 모두 [추정]·vendor_claim, 서로 다른 업체의 다른 조건이라 교차 확인으로 세지 않음. 검증 반영: A01 정정 위치를 6절이 아니라 s4.md 40행(4절)으로, 근거 ref-1191→ref-636(f1); F03 제3조(1) 적용 대상(2026-09-12 후 출시)과 일반 적용일(2025-09-12) 구분(f3); F04 는 기존 내용이라 제외; F05 출처를 공식 EC URL 로(f4, 면책 조항 없음); 제조물책임지침은 다사업자 책임 관점 핵심만(f5~f10) 넣고 정오표 표기 '2026-12-08 후'=2026-12-09부터로 명시(f7), 제8조(2) 실질적 변경자 추가(f6); F13 'bi-annual' 원어 인용과 두 해석으로 정정(f11 사실·f12 추정); F14 는 53영역 중복이라 짧게(f15); RFC 9745 는 원문 열람으로 보강(f16·f17); 벤더 약관 X01~X11 은 '○○사 약관에 따르면'·단일 업체 사례로 한정(f19~f29), Formant 는 정의 번호 대신 용어 이름으로 인용. 열린 질문: 해결 없음. 부분 근거 oq-241·oq-268·oq-279·oq-320·oq-280·oq-207·oq-259·oq-185·oq-249·oq-289·oq-149·oq-110. 메모의 '답한 열린 질문' 가운데 '새 질문' 5건은 문구 대조로 기존 oq-279~oq-283 과 같아 새로 만들지 않음. 메모의 '새로 생긴 열린 질문' 3건 중 지원 기한 정지·제3자 공유 실동작 2건을 새로 올리고 Formant 수량 검증 건은 oq-268 에 묶음; RoMi-H 주기 질문 1건 추가. 메모의 '.research-work' 로컬 경로·행 번호(L…)는 쓰지 않고 원문 조·절·쪽과 위키 실제 위치를 적었다. 정정 요청 없음. 용어 후보 없음.
```
