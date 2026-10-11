(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/storyteller.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

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
- retry_count: 1
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

### runs/2026-10-12-04/verification.json

```json
{
  "run_id": "2026-10-12-04",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: raw.githubusercontent v3.1.0 workflow.mdx 를 열어 '다음 실행 때 새 모델 버전을 자동으로 가져온다'는 문장을 확인했다. 실행 중인 프로세스·끊긴 장치에 관한 단서는 위키가 덧붙인 해석이므로 문장 안에서 출처 진술과 구분한다."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. f1 범위 안의 이 위키 의견이다. 출처의 주장처럼 쓰지 않는다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: backwardcomp.mdx(v0.6.0)에서 'Breaking Change' 표기와 PolicyProcessorPipeline 이전 필요를 확인했다. PR #1452 번호는 이번 열람 요약에 나오지 않아 미확인으로 남긴다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 'PR #777 이전 궤적은 그대로 불러오면 잘못 재생된다'는 문장이 있다. SO100/SO101 은 같은 절의 비교표(영점 위치 변경)에 나온다. 예시 기종 밖으로 일반화하지 않는다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: lerobot-dataset-v3.mdx(v0.6.0)에 여러 에피소드를 큰 파일로 이어 붙인다는 문장과 '메타데이터로 복원' 문장이 있다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. f3~f5 에서 이끈 이 위키 의견이며 실물 시험은 하지 않았다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(벤더 문서): Mender 문서의 SupportsRollback 'Yes' 반환과 설치 전 'known good state' 저장을 확인했다. [추정]·벤더 주장 유지."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(벤더 문서): Power loss 절의 'should develop Update Modules to be idempotent'(권고 강도)를 확인했다. [추정]·벤더 주장 유지."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(벤더 문서): 실패 기준 충족 시 rollout 취소와 AbortConfig 를 확인했다. 문서는 중단 기준을 충족해도 QUEUED 실행만 취소하고 IN_PROGRESS 실행은 취소하지 않는다고 적어, '원복과 별개'라는 서술과 맞는다. [추정]·벤더 주장."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(벤더 문서): 세 실패 상태 정의, 'might not be functioning correctly', 부트스트랩 배포는 실패 시 항상 롤백한다는 점을 확인했다. ref-1581 과 같은 AWS 자료라 교차 확인이 아니다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. 벤더 문서(f7~f10)만 근거로 한 이 위키 의견이다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(벤더 문서): Viam 문서에서 첫 집단('canary' 위치는 예시)에만 구성 조각을 적용하는 절차를 확인했다. [추정]·벤더 주장."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(벤더 문서): 이전 판 고정, 다음 구성 동기화 때 수렴, 'within seconds under normal operation' 을 확인했다. [추정]·벤더 주장."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "서지는 research.google 발행 페이지(Breck 외 5인, IEEE Big Data 2017, 28개 항목)에서 확인했다. 원고 PDF(storage.googleapis.com)는 검증 단계에서 텍스트 추출에 실패해 Infra4 문구를 재대조하지 못했다(원문 미열람(검증)). 리서치의 fetch_url 열람 기록을 따른다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "검색 색인에서 이 문장('Offline testing, however extensive…')이 Google Research PDF 와 함께 잡혔다. 원고 텍스트 재대조는 실패했다(원문 미열람(검증)). 카나리는 완화 방법일 뿐이며 물리적 위험 노출을 허가하는 근거가 아니다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "서지는 확인했고, Infra7 문구는 원고 PDF 재대조에 실패했다(원문 미열람(검증)). 권고(should) 강도로 쓴다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. f14~f16 에서 이끈 이 위키 의견이며 임계값은 정하지 않았다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: PMLR PDF 는 텍스트 추출에 실패해 같은 논문의 arXiv 판(ar5iv)으로 대조했다. §3.1 의 i.i.d. 보정 데이터와 'new i.i.d. sample z_test' 를 확인했다. 학회판 PMLR 229 쪽 번호는 검증 단계에서 재확인하지 못했다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(arXiv 판): §3.2 에서 명제의 보장이 'under the assumption of accurate human help' 에 기댄다는 점을 확인했다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(arXiv 판): §3.3 의 'lift the data to sequences' 와 시퀀스 수준 보정을 확인했다. 운영 분포의 임의 변화에 대한 보장이 아니다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: NeurIPS PDF 는 추출에 실패해 arXiv 2106.00170(ar5iv)으로 대조했다. 'correct long-term empirical coverage frequency', 주가 변동성·2020 미국 대선 데이터, 로봇 실험 없음을 확인했다. KnowNo 와 교차 확인 관계가 아니다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(arXiv 판): 갱신식이 'empirical miscoverage frequency of the previous prediction sets' 를 보고 조정한다는 점을 확인했다. 정답 관측이 필요하다는 것은 갱신식에서 이끈 서술이다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. oq-107 의 부분 답이며 재보정 주기는 여전히 해결되지 않았다."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv HTML v4 에서 Agibot G1, 16대(식료품 4대, 장기 작업마다 3대), 8개 작업, 4시간·약 60시간을 확인했다. 다만 '저자 전원 AGIBOT 소속'은 틀렸다. 대부분 AGIBOT(Finch) 소속이고 일부는 Shanghai Innovation Institute 를 겸직하며, 1명(Jeffrey Wu)은 Columbia University 소속이다. 표현을 정정해야 한다(required_fixes). v1 2026-05-01, v4 2026-09-16, 게재처 없음."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: §V-A '50 training steps' 와 부록 D 'reload the new policy at episode boundaries' 를 확인했다. 연구 구현이다."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 결론의 한계 문장 'does not explicitly model execution safety' 와 'straightforward real-time schedule … may not be optimal for larger-scale deployment' 를 확인했다. '단순한' 대신 원문에 가까운 '직관적인(straightforward)' 표현도 무방하다."
    },
    {
      "finding_id": "f27",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. 이기종 장기 임무에 맞는지는 미확인이다."
    },
    {
      "finding_id": "f28",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인(회사 보도자료): 포지·바통 연계 선순환 문장을 확인했다. 게시일은 본문 '7일'과 이미지 경로(2026/05)로 2026-05-07 이다. [추정]·벤더 주장."
    },
    {
      "finding_id": "f29",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: '약 15% 이상 향상', '최대 18% 절감 … 기대된다'를 확인했다. 실측이 아닌 회사 기대치로만 쓴다."
    },
    {
      "finding_id": "f30",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: '20곳 이상 … PoC 진행중'과 부산 스마트시티 국가시범도시의 4종 로봇 통합 관제를 확인했다. [추정]·벤더 주장."
    },
    {
      "finding_id": "f31",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지."
    },
    {
      "finding_id": "f32",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: AI-Hub 71825 변경이력에서 1.1 2025-06-30 데이터 최종 개방, 1.0 2025-04-16 Beta 를 확인했다(첫 열람은 연결 재설정, 재시도에서 열림)."
    },
    {
      "finding_id": "f33",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 데이터 히스토리 2026-05-06 '기타/태그 추가'를 확인했다."
    },
    {
      "finding_id": "f34",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 총량 262,166, 학습 238,266, 테스트 23,900 과 표제 '학습 데이터 (80%)'·'테스트 데이터 (10%)'를 확인했다. 검증 분할 표기는 없다. 90.9%·9.1% 는 위키 계산값으로 밝힌다."
    },
    {
      "finding_id": "f35",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 실제 77,984 장, 가상 184,182 장(RGB·Depth 각각)을 확인했다. 약 70% 는 계산값이다."
    },
    {
      "finding_id": "f36",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 분포 비율 14.29%·85.71%, 합계 524,332, JSON 262,166 개 표기를 확인했다. 어느 값이 맞는지는 판정하지 않는다."
    },
    {
      "finding_id": "f37",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. 실제 파일은 열지 않았다."
    },
    {
      "finding_id": "f38",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: nvlpubs PDF 는 텍스트 추출에 실패해 NIST 공식 AIRC 의 AI RMF 핵심(Core) 페이지에서 MANAGE 4.1 문구(의견 수집·평가, 이의 제기·무효화, 폐기, 사고 대응, 복구, 변경관리)를 대조했다. 자율 적용 프레임워크다."
    },
    {
      "finding_id": "f39",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지. ISO/IEC 42001 은 인용하지 않는다."
    },
    {
      "finding_id": "f40",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "EUR-Lex 통합판(HTML·PDF)은 검증 단계에서 빈 응답이었다(원문 미열람(검증)). 해설·검색 결과(euaiact.com, 실무 노트)로 2026/1744 의 관보 게재일 2026-07-24, 2026-07-27 발효, 기계류 규정의 부속서 I Section A→B 이동을 확인했다. 부속서 I 의 항목 번호(Section A 1번 삭제, Section B 21번)는 리서치의 원문 열람 기록에만 기댄다."
    },
    {
      "finding_id": "f41",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "해설 자료는 기계류에 AI Act 가 제2조 2항을 통해서만 적용된다고 하고, 검색 결과의 독일어 조문 발췌에서 'Article 6(1), Article 60a, Articles 102 to 112 만 적용'을 확인했다. 제57~59조 단서의 정확한 문구는 원문을 재대조하지 못했다(원문 미열람(검증))."
    },
    {
      "finding_id": "f42",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 조문 사이트(artificialintelligenceact.eu)로 제43조 4항 첫 문단을 대조했다. 용어는 용어집의 '실질적 변경(Substantial Modification)'으로 맞춘다(terminology 참조)."
    },
    {
      "finding_id": "f43",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 제43조 4항 둘째 문단(사전에 정한 변경, 부속서 IV 2(f))을 같은 조문 사이트로 대조했다."
    },
    {
      "finding_id": "f44",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 제72조 2항의 능동적·체계적 수집·문서화·분석, 수명 전반, 관련 시 다른 AI 시스템과의 상호작용 분석을 확인했다. 의무 주체는 제공자다."
    },
    {
      "finding_id": "f45",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 해설 자료는 집행위원회가 위임법령으로 기계류 규정 부속서 III 에 AI Act 고위험 요구(제72·73조 포함)를 옮겨 담게 했다고 적는다. 따라서 'AI Act 조문으로 바로 적용되지 않는다'는 서술에 '기계류 규정 쪽 통합 방식은 미확인'을 반드시 함께 적어야 한다. 법률 판단이 아니다."
    },
    {
      "finding_id": "f46",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지."
    },
    {
      "finding_id": "f47",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 국가법령정보센터 조문 링크에서 제34조 1항 본문과 1~6호(5호 문서 작성·보관)를 확인했다."
    },
    {
      "finding_id": "f48",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 시행 2026-07-21, 법률 제21311호, 2026-01-20 일부개정을 확인했다. 2026-01-22 시행(최초 법률·시행령)은 기존 위키 기준으로 유지한다. 시행령 개정판은 미확인이다."
    },
    {
      "finding_id": "f49",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 조문 범위에서 이끈 해석이며 고영향 영역 목록·시행령은 열지 않았다."
    },
    {
      "finding_id": "f50",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[의견] 유지."
    }
  ],
  "category_fit": {
    "ok": true,
    "reassign_to": null
  },
  "scope_boundary": {
    "ok": true,
    "issues": []
  },
  "duplication": {
    "ok": true,
    "overlaps": [
      "f14~f16 은 기존 6절 분리 페이지(2026-09-25-area27-s6) '모델 운영 관리' 소절의 ML Test Score 28개 항목 문장에 덧붙이는 내용이다. 기존 각주 ref-625 를 재사용한다.",
      "f18~f20 은 기존 KnowNo 서술(s6 57행, s4 41행, 5절 피킹 표)에 조건을 덧붙인다. 기존 각주 ref-351 을 재사용한다.",
      "f1(ref-1577, MLflow v3.1.0 고정 문서)은 기존 ref-626(latest 문서)과 판이 다른 별개 출처다. 둘을 합치지 않는다.",
      "f38(ref-1586, AI RMF 본문)은 기존 ref-617(보도자료)과 별개 출처다. 네 기능 소개는 기존 문장을 유지한다.",
      "f7·f8 은 43. 데이터·관측성·배포 페이지의 Mender 서술(ref-1323, 그쪽은 [사실])과 겹친다. 이번 실행은 벤더 주장 [추정]으로 둔다. 다른 페이지의 태그 차이는 후속 정리 대상이며 모순으로 보지 않는다.",
      "f40·f41 은 기존 3절 문장('부속서 I(기계류 등) … 고위험', ref-621)과 겹친다. 제2조 2항이 제6조 1항을 계속 적용하므로 기존 문장은 틀린 것이 아니다. 지우지 말고 범위를 보충한다."
    ]
  },
  "terminology": {
    "ok": false,
    "conflicts": [
      "f42 의 '중대한 변경(substantial modification)'은 용어집 substantial-modification '실질적 변경 (Substantial Modification)'과 다르다. '실질적 변경'으로 맞춘다.",
      "rationale·open_questions_new 의 '단계 배포'는 용어집 phased-rollout '단계적 배포 (Phased Rollout (Staged Rollout))'와 다르다. '단계적 배포'로 맞춘다."
    ]
  },
  "quotation_check": {
    "ok": true
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "f24: 문장과 ref-1585 각주의 '저자 전원 AGIBOT 소속'을 '저자 대부분 AGIBOT(Finch) 소속(일부 Shanghai Innovation Institute 겸직, 1명 Columbia University)'로 고친다. 이유: arXiv HTML v4 의 저자 소속 표기와 다르다. '제조사 연구·저자 보고·프리프린트(학회 게재 미확인)·동일 기종 플릿(이기종 아님)' 표기는 유지한다.",
    "f42·f43(7절): '중대한 변경'을 용어집 표기 '실질적 변경(Substantial Modification)'으로 쓰고 용어집 substantial-modification 에 링크한다. 이유: 용어 충돌. 같은 이유로 '단계 배포'는 모든 절에서 '단계적 배포'로 쓴다.",
    "f2·f6·f11·f17·f23·f27·f31·f37·f39·f46·f50: [의견] 문장마다 이 위키의 의견임을 밝힌다(예: '이 위키는 … 보는 편이 좋다고 본다'). 근거 출처 각주는 붙이되 출처가 그렇게 주장한 것처럼 쓰지 않는다. 이유: 공통 규칙 5.3, 의견 주체 명시.",
    "f7~f10·f12·f13·f28~f30: [추정] 태그 뒤에 '벤더 주장'을 병기하고 '○○ 문서(또는 발표)에 따르면'으로 시작한다. f29 의 15%·18% 는 '회사가 기대치로 제시한 값(실측 아님)'으로 쓰고, f9·f10 은 같은 AWS 자료라 교차 확인으로 세지 않는다. 이유: 벤더 문서 단독.",
    "5절: 브리프의 모든 finding 에 site_type 이 없다. 따라서 Viam(f12·f13)과 LWD(f24~f26)는 현장 적용 사례 블록으로 넣지 않고 6절(접근법)·8절(연구)에만 둔다. LG CNS(f28~f30)를 5절에 넣을 때는 현장 유형 '기타'(부산 스마트시티 국가시범도시, 회사 발표)로 밝힌다. 여섯 항목 가운데 근거 있는 칸(수행 자원: 4종 로봇 통합 관제, 벤더 주장)만 채우고 나머지는 '미확인'으로 둔다. site_matrix_updates 는 실제로 채운 칸만 낸다. 기존 출하 시나리오 '예외·성과' 칸에는 f1·f15·f16 을 보강해도 된다. 이유: 현장 유형 명시 규칙(원문 21장).",
    "3절 법·규제 문단: 기존 '2026-01-22 시행' [사실] 문장은 유지한다. '개정 법률의 시행일과 고영향 영역 목록은 미확인이다'는 '개정 법률(법률 제21311호, 2026-01-20 공포)은 2026-07-21 시행되었고(f48), 고영향 영역 목록은 미확인이다'로 바꾼다. EU 문장은 지우지 말고 f40·f41(2026-07-27 통합판에서 기계류 규정이 부속서 I Section B 로 옮겨졌고, 제2조 2항이 적용 조문을 한정함)로 보충한다. '개정(AI Omnibus) 논의로'는 '개정(Regulation (EU) 2026/1744)과 관련해'로 고친다. 적용 시점은 브리프에 근거가 없으므로 계속 확정하지 않는다. 이유: 제2조 2항이 제6조 1항을 계속 적용하므로 기존 문장이 틀린 것은 아니다.",
    "f45(3·7절): [추정]으로 쓰고 '법률 판단이 아니며, 기계류 규정 (EU) 2023/1230 쪽에 AI 고위험 요구가 어떻게 통합되는지는 확인하지 않았다'를 같은 문장이나 바로 다음 문장에 적는다. 제43조 4항·제72조 2항(f42~f44)은 7절의 '조문 내용 소개'로만 두고, 로봇(기계류) AI 에 바로 적용되는 의무처럼 쓰지 않는다. 이유: 해설 자료가 위임법령을 통한 기계류 규정 통합을 언급하며, 이 통합은 이번 브리프 밖의 사실이다.",
    "각주 정의: ref-620 은 발행일 '미확인'을 '2026-01-20'으로, 접근일을 2026-10-12 로 바꾸고 '(원문 미열람)'을 뗀다. ref-351·ref-625 는 접근일을 2026-10-12 로 바꾸고 '(원문 미열람)'을 뗀다(리서치가 fetch_url 로 원문을 열었다). ref-351 을 인용하는 본문에는 학회판(CoRL 2023, PMLR 229)을 밝힌다. 새 출처 ref-1577~ref-1588 은 브리프 sources 값 그대로 각주를 만든다.",
    "f34~f36: 90.9%·9.1%·약 70%(70.3%)·29.7% 는 이 위키가 계산한 값임을 문장에 밝히고 원문 값처럼 쓰지 않는다. 표제 비율·합계 가운데 어느 값이 맞는지 판정하지 않는다. 이유: 원문 페이지 안의 표기 불일치.",
    "4·6절 KnowNo·등각 예측: 기존 보장 서술(s6 57행, s4 41행)에 f18(i.i.d. 보정)·f19(정확한 사람 도움 가정)·f20(시퀀스 수준 보정)을 조건으로 덧붙인다. f21 의 ACI 보장은 '장기 평균 포함 빈도(매 시점·로봇 안전 보장 아님, 로봇 실험 없음)'로 쓰고, KnowNo 와 교차 확인 관계로 쓰지 않는다.",
    "6절: 장치 업데이트·배포 도구(Mender·AWS IoT Jobs·Greengrass·Viam, f7~f13)는 모델 교체·되돌림 관점의 짧은 소절로 두고 43. 데이터·관측성·배포, 57. 자산·소프트웨어 수명주기 관리에 번호와 이름으로 연결한다. LWD(f24~f26)의 저수준 조작 정책 학습은 로봇 자체 지능·제어(연계 대상)로 밝히고, 정책 판 갱신 경계·운영 기록 관점으로만 쓴다. 이유: 분류 원문 19장 범위 경계.",
    "7·9절: f38(MANAGE 4.1)은 '법적 의무가 아닌 자율 적용 프레임워크'로 쓴다. 9절의 공급자·ROP·현장 운영자 역할 분리(f39)와 복구 실패 로봇의 배정 제외(f11)는 [의견]으로 둔다. f40~f49 의 법 해석은 59. 법·규제·보험·라이선스에 연결하고, 개별 ROP 의 의무 발생 여부를 판단하지 않는다.",
    "11절: id 없이 '(신규 …)'로 적힌 세 질문에 각각 oq-105·oq-106·oq-107 을 붙인다(docs/open-questions.md 문구와 같다). 셋과 oq-213·oq-222 는 '열림'을 유지하고 부분 근거만 적는다. oq-030 은 '이번 실행에서는 조사하지 않았다'를 지우고 관련 후속 질문 oq-356 만 연결한다. LTAA 수치(75.97%·77.1%·DP 0.95)는 이번 브리프에 finding 이 없으므로 넣지 않는다. 새 질문 4건은 open_questions_new 그대로 등록하되, 세 번째 질문은 'AI-Hub 한 페이지 안의 표기 불일치'임이 드러나게 쓴다.",
    "트랙 세부영역 반영 제안 15건(data/area_reflection_proposals.json)은 이번 브리프에 근거 finding 이 없으므로 이번 갱신 본문에 반영하지 않고 '제안' 상태로 둔다. 이유: 1차 검증을 거친 finding 만 서술할 수 있다.",
    "직접 인용은 출처당 1회, 짧은 구절로 한정한다. 특히 ref-1587·ref-625·ref-351·ref-1585 는 브리프 발췌가 여러 개이므로 나머지는 재서술한다.",
    "이번 갱신 범위 밖 페이지(docs/categories/ai-and-learning/index.md, docs/categories/safety/index.md, ref-168 저자 표기, 2026-10-09-area43-s6 의 Mender 태그)는 고치지 않는다. changelog_entry 에 후속 정리 대상으로만 적는다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 50건, 미확인 0건, 교차 확인 0건(모든 사실 finding 이 단일 출처이며, AWS 두 문서는 같은 기관이고 KnowNo·ACI 는 결과 종류가 달라 교차 확인으로 세지 않음). 강등: 없음. 대신 f24 저자 소속 표현('전원 AGIBOT')을 정정하고, f42 용어를 '실질적 변경'으로 바꾸도록 지시함. 원문 미열람 출처: 없음(브리프 기준). 다만 검증 단계에서는 ref-1587(EUR-Lex 통합판 본문 응답 없음, 해설·조문 사이트로 골자 대조), ref-625(원고 PDF 텍스트 추출 실패, 발행 페이지 서지와 검색 색인으로 대조)를 다시 열지 못했고, ref-351·ref-1583·ref-1586 은 같은 문서의 arXiv 판·NIST AIRC 웹판으로 대조함. 주의: Mender·AWS·Viam·LG CNS 내용은 벤더 주장이며 LG CNS 의 15%·18% 는 회사 기대치다. LWD 는 제조사 중심 연구 프리프린트이고 같은 기종 실험실 조건이다. EU AI Act 의 기계류 연계 로봇 AI 적용 범위(f45)와 한국 인공지능기본법 제34조 해당성(f49)은 법률 판단이 아닌 [추정]이다. AI-Hub 71825 의 분할비·합계 불일치는 제공자 확인 전까지 판정하지 않는다. 리서치 브리프는 외부 조사 메모를 변환한 것이라 검색 횟수 집계가 없다(budget_used.queries 0). 검증 검색은 4회 썼다. 4·6·7·8절은 분리된 주제 페이지(2026-09-25-area27-s4·s6·s7·s8)에 반영되므로 실제로 바뀌는 파일 수가 늘어난다. 트랙 반영 제안 15건은 근거 finding 이 없어 이번에 반영하지 않는다. 이 제안들은 옛 번호('13. 작업 배정 — MRTA', '18. 사람–로봇 협업·운영 인터페이스', '6. 지도·공간·위치 모델', '23. 시험·형식 검증·벤치마크')를 쓰고 있으므로, 반영할 때는 새 분류의 25. 작업 배정 — MRTA, 31. 사람–로봇 협업, 15. 지도·공간·위치 모델, 54. 시험·형식 검증·벤치마크로 바꿔야 한다. 정정 요청: 없음. 열린 질문 해결 인정: 없음(oq-105·oq-106·oq-107·oq-213·oq-222 는 부분 근거만 있어 열림 유지).",
  "retry_reason": null
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

### docs/categories/ai-and-learning/index.md

````markdown
---
title: "L. AI·학습 기술"
type: category
status: published
created: 2026-09-28
updated: 2026-10-09
version: 2
sources: [ref-063, ref-067, ref-076, ref-090, ref-092, ref-170, ref-171, ref-199, ref-201, ref-238, ref-239, ref-241, ref-304, ref-308, ref-351, ref-354, ref-359, ref-417, ref-541, ref-617, ref-618, ref-619, ref-620, ref-621, ref-623, ref-624, ref-625, ref-626, ref-741, ref-815, ref-832, ref-854, ref-863, ref-1012, ref-1018, ref-1037, ref-1043, ref-1045, ref-1047, ref-1051, ref-1052, ref-1053, ref-1054, ref-1056, ref-1057, ref-1058, ref-1059, ref-1060, ref-1061, ref-1062, ref-1063, ref-1064, ref-1065, ref-1066, ref-1070, ref-1071, ref-1072, ref-1073, ref-1074, ref-1127, ref-1172, ref-416, ref-1245, ref-822, ref-857, ref-700, ref-453, ref-1262, ref-1253, ref-1263]
---

[홈](../../index.md) › L. AI·학습 기술

# L. AI·학습 기술

## 핵심 질문

학습·언어 모델 같은 AI 기술을 어디에 쓰고, 그 결과를 어떤 기준으로 믿을 것인가? [분류원문]

## 개요

로봇 기반 모델·언어 모델, 문서·도면·장면 이해, 예측·학습 기반 최적화, AI 결과의 신뢰와 모델 운영. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **44. 로봇 기반 모델·언어 모델 계획** | 시각–언어–행동 모델 같은 로봇 기반 모델의 흐름과 언어 모델 기반 작업 계획 | 범용 로봇 모델과 언어 모델은 오케스트레이션의 무엇을 바꾸는가? | [44. 로봇 기반 모델·언어 모델 계획](robot-foundation-models-and-llm-planning.md) | published |
| **45. 문서·도면·장면 이해** | 매뉴얼·도면 해석과 플랫폼 수준의 장면 인식 | 매뉴얼·도면·현장 영상을 AI가 얼마나 정확히 읽어 낼 수 있는가? | [45. 문서·도면·장면 이해](document-drawing-and-scene-understanding.md) | published |
| **46. 예측·학습 기반 최적화** | 학습 기반 배정·경로, 수요·고장 예측 | 학습과 예측이 배정·경로·정비 결정을 실제로 개선하는가? | [46. 예측·학습 기반 최적화](prediction-and-learning-based-optimization.md) | published |
| **47. AI·학습·적응과 모델 운영** | AI 결과를 실행에 쓰는 기준과 불확실성, 모델 운영 | AI가 만든 작업 계획이나 기능 해석을 어떤 기준으로 실행에 사용할까? | [47. AI·학습·적응과 모델 운영](ai-learning-adaptation-and-model-operations.md) | published |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]

## 다른 대분류와의 연결

L. AI·학습 기술의 네 세부영역인 [44. 로봇 기반 모델·언어 모델 계획](robot-foundation-models-and-llm-planning.md), [45. 문서·도면·장면 이해](document-drawing-and-scene-understanding.md), [46. 예측·학습 기반 최적화](prediction-and-learning-based-optimization.md), [47. AI·학습·적응과 모델 운영](ai-learning-adaptation-and-model-operations.md)은 따로 떨어진 기능이라기보다 다른 대분류의 기능에 적용되는 연구 방법이다. 위 '이 대분류의 핵심 포인트'의 교차 규칙대로 매뉴얼 해석은 4. 이기종 로봇 등록과 55. 현장 조사·설치·시운전, 도면 해석은 14. 도면·BIM에서 지도 만들기, 학습 기반 배정은 25. 작업 배정 — MRTA, 장애 분석은 38. 모니터링·이상 탐지·원인 분석으로 이어진다. 아래는 이 네 갈래와 그 밖의 연결을 대분류별로 정리한 것이다.

연결 근거는 게시된 세부영역·대분류 페이지의 검증된 주장과 이번 조사에서 연 자료다. 대부분 단일 출처이거나 서로 다른 내용의 출처를 묶은 것이어서 두 출처로 교차 확인된 주장은 없다. '연계 대상'은 분류 원문 19장이 외부 연계 영역으로 둔 것으로, ROP가 직접 맡지 않는다. 본문의 oq-NNN은 [열린 질문](../../open-questions.md)의 항목이다.

```mermaid
flowchart LR
  L44["44. 로봇 기반 모델·언어 모델 계획"] -->|업무 지시 계획| C12["12. 채팅으로 업무 지시·오케스트레이션"]
  L45["45. 문서·도면·장면 이해"] -->|매뉴얼 해석| B4["4. 이기종 로봇 등록"]
  L45 -->|매뉴얼 해석| O55["55. 현장 조사·설치·시운전"]
  L45 -->|도면 해석| D14["14. 도면·BIM에서 지도 만들기"]
  L46["46. 예측·학습 기반 최적화"] -->|학습 기반 배정| G25["25. 작업 배정 — MRTA"]
  L46 -->|장애 분석| J38["38. 모니터링·이상 탐지·원인 분석"]
  L47["47. AI·학습·적응과 모델 운영"] -->|장애 분석| J38
  L47 -->|실행 전 계획 검사| M48["48. 안전·위험 관리"]
```

### [A. 기획·사업](../planning-and-business/index.md)

- **44. 로봇 기반 모델·언어 모델 계획 ↔ [1. 기술·시장·업체 동향](../planning-and-business/technology-market-and-vendor-trends.md)**: BMW 그룹은 2026-06-25 보도자료에서 2025년 스파턴버그 공장에 Figure AI의 휴머노이드 Figure 02를 배치해 용접 공정용 판금 부품 투입을 맡겼고 BMW X3 3만 대 이상 생산을 도왔다고 밝혔으나, 같은 자료 안에서 배치 기간이 10개월과 11개월로 엇갈린다(벤더 주장, oq-219). [추정][^ref-1051] 헬로티 보도(2025-11-26)에 따르면 로보티즈는 시각–언어–행동(Vision-Language-Action, VLA) 모델을 넣은 상체형 휴머노이드 AI 워커로 BGF로지스 물류센터 실증(PoC)을 계획하며, 기사가 전한 핵심 공정 자동화율 80% 이상·작업 성공률 90% 이상은 실측이 아닌 목표치다(벤더 주장, oq-218). [추정][^ref-1052] 이런 로봇의 저수준 조작 정책은 로봇 자체 지능·제어 경계의 연계 대상이고, ROP 쪽 연결은 그 능력과 실행 조건을 받아 계획에 쓰는 부분이다.
- **46. 예측·학습 기반 최적화 ↔ [3. 경제성·조달·사업 모델](../planning-and-business/economics-procurement-and-business-models.md)**: Howard(Cal Poly 석사논문, 2026-06)는 처리량 최대화 기준의 자율 이동 로봇(Autonomous Mobile Robot, AMR) 대수 산정이 서비스형 로봇(Robot-as-a-Service, RaaS) 구독 과금에서는 플릿을 과대 산정한다고 보고, 대수 산정을 주문 라인당 비용 최소화 문제로 바꿔 시뮬레이션·대기행렬·기계학습 대리 모델을 함께 썼다. [사실][^ref-822]
- **47. AI·학습·적응과 모델 운영 ↔ [2. 사용 사례·요구·책임 범위](../planning-and-business/use-cases-requirements-and-scope.md)**: 법무법인 태평양(BKL) 해설은 에너지·보건의료·원자력·교통·교육 등 특정 영역에서 활용되는 AI를 한국 인공지능 기본법의 고영향 인공지능으로 설명하므로, 병원·교통 현장의 로봇 작업 계획·배정에 AI를 쓸지 정하는 사용 사례 정의 단계에서 고영향 해당 여부를 함께 판단해야 할 것으로 보인다(해설은 2025-09-30 공개된 시행령(안)·고시(안)·가이드라인(안) 기준이며 확정본과의 일치는 미확인, 로봇 언급은 없음, oq-105). [추정][^ref-1253][^ref-620]

### [B. 로봇 온톨로지](../robot-ontology/index.md)

- **45. 문서·도면·장면 이해 ↔ [4. 이기종 로봇 등록](../robot-ontology/heterogeneous-robot-registration.md)·[5. 로봇 능력·작업 표현](../robot-ontology/robot-capability-and-task-representation.md)**: 검색 증강 문맥 학습으로 자산관리셸(Asset Administration Shell, AAS)용 정보 추출을 개선하는 AAS-RAIL(2026-09)과 대규모 언어 모델(Large Language Model, LLM) 에이전트로 자산관리셸을 생성하는 Xia 외(2024)가 있다. [사실][^ref-1071][^ref-1072] 두 연구는 교차 규칙의 매뉴얼 해석이 등록 정보 작성으로 이어지는 예이며, 방법이 서로 달라 같은 내용을 교차 확인한 것은 아니다. 로봇 기술 파일(Unified Robot Description Format, URDF)에서 로봇 온톨로지를 LLM으로 채우는 연구(Dussard·Sarthou, 2026-06)와 LLM으로 능력 온톨로지를 생성하는 연구(Vieira da Silva 외, 2024-04)도 있다. [사실][^ref-239][^ref-238] 이 두 연구는 4. 이기종 로봇 등록과 5. 로봇 능력·작업 표현 양쪽에 닿으며, 같은 연결은 B. 로봇 온톨로지 페이지의 연결 절에도 있다.
- **45. 문서·도면·장면 이해 ↔ [7. 온톨로지 검증·변경 관리](../robot-ontology/ontology-verification-and-change-management.md)**: 추출 항목마다 원문 위치를 붙이는 출처 근거 연결 도구(LangExtract)를 쓰면 7. 온톨로지 검증·변경 관리의 원문 대조 검증과 사람의 확정·반려가 같은 근거를 공유할 것으로 보이나, 로봇 매뉴얼에 적용한 공개 구현은 확인하지 못했다(oq-147, oq-226). [추정][^ref-1074][^ref-1071]
- **44. 로봇 기반 모델·언어 모델 계획 ↔ [6. 온톨로지 기반 시스템·로봇 연동](../robot-ontology/ontology-based-system-and-robot-integration.md)**: Nabizada 외(2026-06, CASE 2026 채택)는 VDI 3682·IEC 61360-1·IDTA 02011·IDTA 02016으로 구성한 자산관리셸 능력 모델에서 계획 도메인 정의 언어(Planning Domain Definition Language, PDDL) 문제를 자동 생성한다. [사실][^ref-201] 자연어 문제를 PDDL로 옮겨 고전 계획기로 푸는 LLM+P와 함께 보면, PDDL 같은 계획 표현이 언어 모델 계획과 온톨로지 기반 연동을 잇는 인터페이스가 될 것으로 보이나 두 방식을 한 플랫폼에서 결합한 사례는 확인하지 못했다. [추정][^ref-092][^ref-201]
- **44. 로봇 기반 모델·언어 모델 계획 ↔ 5. 로봇 능력·작업 표현**: VLA 같은 로봇 기반 모델은 카메라 영상에서 행동을 직접 생성해 미리 정한 스킬 목록 없이 작업을 다루므로, 이런 로봇의 능력을 능력 모델에 어떻게 등록·기술·검증할지가 두 대분류 사이의 열린 쟁점으로 보인다(oq-216). [추정][^ref-1045][^ref-1047]

### [C. 채팅 기반 구성·운영](../chat-based-configuration-and-operation/index.md)

분류 원문은 C. 채팅 기반 구성·운영의 원칙을 다음과 같이 적는다.

대화 결과는 실행 명령이 아니라 계획이다. **사람이 확인·승인한 계획만 실행**되어야 언어 모델의 잘못된 해석이 로봇 동작으로 이어지지 않는다. [분류원문]

- **44. 로봇 기반 모델·언어 모델 계획 ↔ [12. 채팅으로 업무 지시·오케스트레이션](../chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md)**:
    - 언어 모델 계획: 언어 모델로 다중 로봇 작업을 계획하는 SMART-LLM(2023-09)과 언어 모델의 해석을 PDDL로 옮겨 최적 계획기에 맡기는 LLM+P(2023-04)가 있다. [사실][^ref-090][^ref-092] 분류 원문 C 주석은 업무 지시를 25. 작업 배정 — MRTA·26. 작업 순서·스케줄링의 기능을 대화로 쓰게 하는 것으로 두므로, 이 연구들은 대화 지시를 계획으로 바꾸는 엔진과 언어 모델 계획이 만나는 자리에 있다.
    - Nayantra: Open Robotics 상호운용 SIG의 2026-07-02 발표 안내문(2026-06-25 게시)은 Open-RMF REST API를 언어 모델이 호출하는 도구로 노출하는 모델 컨텍스트 프로토콜(Model Context Protocol, MCP) 서버와, 평이한 영어 지시를 여러 단계의 RMF 임무로 바꾸는 에이전트로 이루어진 Nayantra를 소개했다(시연은 창고 시뮬레이션이며 발표 내용 자체는 미열람). [사실][^ref-854] 같은 연결은 E. 사물·사람·실시간 상태와 K. 플랫폼 아키텍처·인프라 페이지의 연결 절에도 있다.
    - SayPlan: SayPlan(CoRL 2023)은 언어 모델이 3차원 장면 그래프로 세운 초기 계획을 실행 전에 장면 그래프 시뮬레이터로 확인하고 그 피드백으로 실행 불가능한 동작을 고치는 반복 재계획을 둔다(단일 이동 매니퓰레이터 평가). [사실][^ref-416] 장면 그래프를 계획의 바탕으로 쓴다는 점에서 이 연구는 [15. 지도·공간·위치 모델](../space-and-map-model/map-space-and-location-model.md)과도 닿는다.
- **47. AI·학습·적응과 모델 운영 ↔ 12. 채팅으로 업무 지시·오케스트레이션·[13. 대화형 기능의 신뢰·기반](../chat-based-configuration-and-operation/conversational-trust-and-foundations.md)**: 언어 모델 계획을 기호 계획기로 검증하고 불확실할 때 사람에게 묻는 장치가 위 원칙을 구현하는 수단이 될 것으로 보이며, 47. AI·학습·적응과 모델 운영은 그 채택 기준을 정하는 쪽을 맡는 것으로 보인다. [추정][^ref-351][^ref-092] KnowNo는 언어 모델 계획기가 필요할 때 사람에게 도움을 요청하게 하고(사람 도움을 줄이는 것이 목표라는 점은 저자 보고), ‘Learning to Ask’(2024-09)는 불분명한 지시를 받은 LLM 에이전트의 되묻기를, AmbiK는 주방 환경의 모호한 작업 데이터셋을 다룬다. [사실][^ref-351][^ref-359][^ref-354]
- **44. 로봇 기반 모델·언어 모델 계획 ↔ [11. 채팅으로 실제 상황 시뮬레이션 재현](../chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md)**: Xia 외(2026-08)는 언어 모델 에이전트가 사용자 질의와 기준 구성을 받아 비교 시뮬레이션을 설계·실행하고 결과를 해석해 공정 매개변수 변경을 권고하는 다중 에이전트 틀을 제약 공정 설계에 적용했다(로봇 플릿 사례는 아님). [사실][^ref-832] 대화로 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈을 부르는 형태라는 점에서 I. 설계·시뮬레이션과도 이어진다.
- **45. 문서·도면·장면 이해 ↔ [8. 채팅으로 맵 작성](../chat-based-configuration-and-operation/chat-map-authoring.md)**: DeFazio 외(2024-09)는 비전 언어 모델로 평면도 지도를 해석하는 연구를 냈다. [사실][^ref-076] 도면을 올려 대화로 지도를 만드는 기능은 45. 문서·도면·장면 이해의 도면 해석과 14. 도면·BIM에서 지도 만들기·15. 지도·공간·위치 모델의 엔진을 함께 부를 것으로 보이며, 건축·공학 도면 이해 벤치마크가 따로 있을 만큼 해석 오류가 남으므로 확인 질문이 필요할 것으로 보인다. [추정][^ref-076][^ref-1073]

### [D. 공간·지도 모델](../space-and-map-model/index.md)

- **45. 문서·도면·장면 이해 ↔ [14. 도면·BIM에서 지도 만들기](../space-and-map-model/maps-from-floor-plans-and-bim.md)**: 평면도 영상 분석 데이터셋 CubiCasa5K(2019-04), CAD 도면 파놉틱 심볼 스포팅 데이터셋 FloorPlanCAD(2021-05), 국내 AI Hub 건축 도면 데이터(2023-07-26)가 공개되어 있다. [사실][^ref-063][^ref-067][^ref-1012] 이 자료들은 교차 규칙의 도면 해석을 학습·평가하는 데 쓰이며, AI Hub 라벨에 로봇 운영에 필요한 클래스가 있는지는 oq-197로 남아 있다. Su 외(Sensors, 2022-03)는 쇼핑몰 평면도 25장의 점포 1,340개를 대상으로 공간 분할 정확도 92.54%, 점포 인식 정확도 90.56%, 전체 검출 정확도 83.81%를 보고했다(논문 평가값이며 로봇 현장 배치 결과는 아님). [사실][^ref-1066] AECV-Bench(2026-01)는 다중 모달 모델의 건축·공학 도면 이해를 평가하는 벤치마크다. [사실][^ref-1073]
- **45. 문서·도면·장면 이해 ↔ 15. 지도·공간·위치 모델·[16. 장소 의미·지도 관리](../space-and-map-model/place-semantics-and-map-management.md)**: Strader 외(2025-07)는 개방형 객체 지도를 담은 공유 3차원 장면 그래프로 여러 로봇의 장면 그래프를 융합하고, LLM이 장면 그래프와 로봇 능력에서 문맥을 뽑아 운영자의 자연어 의도를 PDDL 목표로 바꾸게 해 대규모 실외 환경에서 평가했다(로봇 대수·실험 수치는 초록에 없음). [사실][^ref-1070]
- **44. 로봇 기반 모델·언어 모델 계획 ↔ 16. 장소 의미·지도 관리**: osmAG-LLM(2025-07, RA-L 2026)은 계층적 위상·계량 의미 지도를 문맥으로 쓰고 LLM이 질의에 맞는 후보 장소를 추론하게 해, 물체가 옮겨졌거나 지도에 없는 경우도 찾게 하는 방법이다. [사실][^ref-1018] 같은 연결은 D. 공간·지도 모델 페이지의 연결 절에도 있다.

### [E. 사물·사람·실시간 상태](../objects-people-and-live-state/index.md)

- **45. 문서·도면·장면 이해 ↔ [18. 실시간 세계 상태·데이터 일관성](../objects-people-and-live-state/real-time-world-state-and-data-consistency.md)**: Brorsson 외(2025-12)가 보고한 대형 상용차 공장 사례에서는 약 8 m 높이 카메라 15대가 로봇의 ArUco 표식으로 위치를 계산하고 영상 분할로 장애물을 격자 단위로 구분했으며, 카메라 간 하드웨어 동기화가 없어 생기는 시간 차 오류가 제약으로 꼽혔다. [사실][^ref-308] 카메라 설치·동기화 자체는 시설·설비 경계의 연계 대상이다. 고정 카메라와 여러 로봇의 인식 결과를 시간·좌표를 맞춰 하나의 공간 상태로 합치는 일은 현재 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성의 입력이 될 것으로 보이며, 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈과는 구분되고, 허용 시간 차·정합 기준은 확인하지 못했다(oq-227). [추정][^ref-308][^ref-1070]
- **46. 예측·학습 기반 최적화 ↔ [19. 사람·보행자 모델](../objects-people-and-live-state/people-and-pedestrian-model.md)**: Rudenko 외 서베이가 정리한 사람 움직임 궤적 예측은 가까운 미래 사람 위치를 추정하는 방법이므로, 예측 결과를 경로·배정 비용에 넣는 일이 두 영역을 잇는 것으로 보인다. [추정][^ref-1172] 같은 연결은 E. 사물·사람·실시간 상태 페이지의 연결 절에도 있다.

### [F. 연동](../integration/index.md)

- **44. 로봇 기반 모델·언어 모델 계획 ↔ [20. 로봇·제조사 관제 연동](../integration/robot-and-vendor-fleet-manager-integration.md)**: NASA JPL의 ROSA는 ROS(Robot Operating System)용 언어 모델 에이전트로 공개되어 있다. [사실][^ref-171] C. 채팅 기반 구성·운영에서 본 Nayantra도 Open-RMF 플릿 API를 언어 모델의 도구로 노출한다는 점에서 이 영역과 이어진다.
- **44. 로봇 기반 모델·언어 모델 계획 ↔ [21. 상호운용 표준·적합성](../integration/interoperability-standards-and-conformance.md)**: B. 로봇 온톨로지에서 본 Nabizada 외의 PDDL 자동 생성은 표준 기반 능력 모델(VDI 3682·IEC 61360-1·IDTA 서브모델)을 계획 입력으로 쓰므로 표준 적합성과도 닿는다.
- **45. 문서·도면·장면 이해 ↔ [22. 설비·건물 시스템 연동](../integration/facility-and-building-system-integration.md)**: Robinson 외(2026-06)는 실제 창고에서 CCTV 카메라 30대만으로 작업용 주행 장비를 싣지 않은 로봇 4대를 영상 공간에서 계획·제어하고, 시야가 겹치는 카메라 구역을 배타적 자원으로 관리해 충돌·교착을 막는 시연을 보고했다(저자는 첫 현장 시연이라 밝힘). [사실][^ref-1065]
- **46. 예측·학습 기반 최적화 ↔ [23. 업무 시스템 연동](../integration/business-system-integration.md)**: 연계 대상: CJ대한통운은 이커머스 통합 플랫폼 iFlex가 AI·빅데이터로 주문 유형별 물량을 예측해 물류센터 인력 배치를 최적화한다고 밝혔으며(2021-07-28, 벤더 주장), 이는 상위 업무 시스템 쪽 수요예측이라 로봇 배정용 요청 예측과의 경계가 열린 질문으로 남아 있다(oq-223). [추정][^ref-1063]

### [G. 계획·최적화](../planning-and-optimization/index.md)

- **46. 예측·학습 기반 최적화 ↔ [25. 작업 배정 — MRTA](../planning-and-optimization/task-allocation-mrta.md)**: 교차 규칙의 학습 기반 배정이 이 연결이다. 어텐션 기반 강화학습으로 창고 다중 로봇 작업 배정을 하는 RTAW(2022-09, ICRA 2023)가 있다(시뮬레이션 창고 조건). [사실][^ref-623] Garces 외(2026-08, 프리프린트)는 병원 입원 병동의 실제 간호 업무 요청 데이터로 예측 인지형 모델 기반 강화학습을 평가했고, 요청 분포가 바뀌면 최근 예측 오차로 예측 요청을 다시 가중하고 아직 시작하지 않은 배정만 다시 최적화해 대기 시간을 줄였다고 보고했다(저자 보고). [사실][^ref-1062] 아마존 연구진의 DeepFleet은 전 세계 아마존 창고 수십만 대 로봇의 이동 데이터로 학습한 다중 로봇 기반 모델 모음이다(2025-08 공개). [사실][^ref-1053] 아마존은 DeepFleet을 혼잡 예측으로 작업 배정과 경로를 조정하는 데 쓰며 로봇 이동 효율을 10% 높였다고 주장한다(벤더 주장, 독립 측정 미확인). [추정][^ref-1054]
- **46. 예측·학습 기반 최적화 ↔ [27. 다중 로봇 경로·교통 관리 — MAPF](../planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md)**: 같은 조건 비교에서는 탐색 기반 다중 에이전트 경로 찾기(Multi-Agent Path Finding, MAPF) 방법이 아직 앞서고, 학습은 탐색·최적화와 결합할 때 개선이 보고되는 것으로 보인다. [추정][^ref-1056][^ref-199][^ref-1064] 위 DeepFleet의 혼잡 예측도 경로 조정에 쓰인다는 점에서 이 영역에 닿는다.
- **46. 예측·학습 기반 최적화 ↔ [28. 공용 자원·충전·에너지 최적화](../planning-and-optimization/shared-resource-charging-and-energy-optimization.md)**: Poskart 외(Sensors, 2022-12)는 다중 로봇 시스템의 지능형 임무 계획을 위해 이동로봇 배터리 방전을 여러 매개변수로 예측하는 모델을 제시했다. [사실][^ref-1058]
- **44. 로봇 기반 모델·언어 모델 계획 ↔ [24. 작업·워크플로 모델링](../planning-and-optimization/task-and-workflow-modeling.md)·[26. 작업 순서·스케줄링](../planning-and-optimization/task-sequencing-and-scheduling.md)**: IMR-LLM(2026-03)은 대규모 언어 모델로 산업용 다중 로봇의 작업 계획과 프로그램 생성을 다루는 연구다. [사실][^ref-170] 이 가운데 저수준 로봇 프로그램 생성은 로봇 자체 제어에 닿아 연계 대상이고, ROP 쪽 연결은 작업 계획 단계다.
- **46. 예측·학습 기반 최적화 ↔ 26. 작업 순서·스케줄링·25. 작업 배정 — MRTA**: Elmachtoub·Grigas의 Smart ‘Predict, then Optimize’(2017-10)는 예측 모델을 예측 오차가 아니라 그 예측으로 내린 최적화 결정의 품질로 학습시키는 틀이다(로봇 배정·스케줄링 현장 적용은 미확인). [사실][^ref-1061]

### [H. 실행·협업·예외 복구](../execution-collaboration-and-recovery/index.md)

- **47. AI·학습·적응과 모델 운영 ↔ [29. 명령·작업 실행의 신뢰성](../execution-collaboration-and-recovery/command-and-task-execution-reliability.md)**: Obi 외(2026-04)는 언어 모델이 제어하는 로봇 시스템에 실행 전 안전 게이트와 작업 안전 계약을 두는 방법을 제안했다. [사실][^ref-417]
- **47. AI·학습·적응과 모델 운영 ↔ [31. 사람–로봇 협업](../execution-collaboration-and-recovery/human-robot-collaboration.md)**: 해석이 불확실할 때 사람에게 묻는 장치는 사람–로봇 협업의 개입 지점이 되지만, KnowNo의 등각 예측 보장은 보정 데이터와 운영 분포가 같다는 조건에 기대므로 지시 분포가 바뀌면 재보정 주기가 문제로 남을 것으로 보인다(oq-107). [추정][^ref-351]
- **44. 로봇 기반 모델·언어 모델 계획 ↔ [32. 예외 복구·재계획·업무 연속성](../execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md)**: REFLECT(Liu·Bahety·Song, CoRL 2023)는 다중 감각 관측에서 로봇 경험의 계층적 요약을 만들어 LLM이 실패 원인을 설명하게 하고, 그 설명을 조건으로 언어 기반 계획기가 실패를 고쳐 작업을 마치는 계획을 만들게 하며, RoboFail 데이터셋으로 평가했다(단일 로봇 조작 작업이며 다중 로봇 플릿 적용은 아님). [사실][^ref-453]

### [I. 설계·시뮬레이션](../design-and-simulation/index.md)

- **46. 예측·학습 기반 최적화 ↔ [34. 시뮬레이션·예측용 디지털 트윈](../design-and-simulation/simulation-and-predictive-digital-twin.md)**: Smit 외(2024-04)는 작업자와 AMR이 피킹 위치에서 만나는 창고에서 작업자–AMR 배정을 다목적 심층 강화학습으로 정하고, 학습·평가용 이산 사건 시뮬레이션 모델을 만들어 학습 정책이 효율과 작업자 부하 공정성에서 비교 방법을 앞섰다고 보고했다. [사실][^ref-1245] DeepFleet 같은 운영 중 혼잡 예측은 배정·경로 결정에 바로 쓰이는 예측이고 34. 시뮬레이션·예측용 디지털 트윈은 가정한 미래를 실험하는 쪽이므로, 두 기능을 구분해 연결해야 할 것으로 보인다. [추정][^ref-1053][^ref-1054] 45. 문서·도면·장면 이해 쪽에서는 Sommer 외(2023)가 기존 건물 환경의 스캔과 객체 인식을 입력으로 생산 계획용 디지털 트윈을 자동 생성하는 방법을 다룬다. [사실][^ref-241]
- **46. 예측·학습 기반 최적화 ↔ [35. 처리능력·규모·배치 설계](../design-and-simulation/capacity-sizing-and-layout-design.md)**: Howard(2026)는 반개방형 대기행렬 모델로 설계안을 걸러 내고 XGBoost 대리 모델과 등각 예측 구간으로 추가 시뮬레이션 없이 연속 설계 공간의 비용을 예측했으며, 대기행렬 모델은 시뮬레이션 라인당 비용과 약 5%, 대리 모델은 교차 검증에서 3% 안에서 맞았다고 보고했다(저자 보고값). [사실][^ref-822]
- **44. 로봇 기반 모델·언어 모델 계획 ↔ [33. 시나리오 모델·편집](../design-and-simulation/scenario-model-and-editing.md)**: Holodeck(CVPR 2024)은 GPT-4가 장면 구성과 객체 간 공간 관계를 만들고 배치를 최적화해 글 지시로 3D 환경을 생성한다(생성 환경은 실제 현장 지도가 아님). [사실][^ref-815]
- **47. AI·학습·적응과 모델 운영 ↔ [36. 가상 시운전·실제 상황 재현](../design-and-simulation/virtual-commissioning-and-real-situation-replay.md)**: Kadian 외(RA-L 2020)는 시뮬레이션–현실 상관 계수(Sim-vs-Real Correlation Coefficient, SRCC)를 제안하고, LoCoBot PointGoal 주행에서 CVPR 2019 챌린지에서 쓰인 Habitat 설정의 성공률 SRCC가 0.18이었으나 시뮬레이션 매개변수 조정으로 0.844로 높였다고 보고했다. [사실][^ref-1127] 학습 정책이 시뮬레이터의 결함을 이용하는 현실 격차가 보고되므로, 학습 정책의 현실 격차 보정은 47. AI·학습·적응과 모델 운영(및 로봇 제조사·시뮬레이션 도구) 쪽이고 36. 가상 시운전·실제 상황 재현은 재현과 실제의 차이 지표를 관리하는 쪽을 맡는 것으로 보인다. [추정][^ref-741][^ref-1127] 이 대분류의 연결은 I. 설계·시뮬레이션 페이지의 연결 절에도 같은 각주로 있다.

### [J. 현장 운영·관제](../field-operations-and-monitoring/index.md)

- **46. 예측·학습 기반 최적화·47. AI·학습·적응과 모델 운영 ↔ [38. 모니터링·이상 탐지·원인 분석](../field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md)**: 교차 규칙의 장애 분석이 이 연결이다.
    - 언어 모델 진단: Herrmann 외(2024-10)는 산업용 로봇 시스템 진단 문제 2,500건 이상으로 비공개 벤치마크 SYSDIAGBENCH를 만들어 언어 모델의 근본 원인 분석을 평가했고, QLoRA 미세조정한 70억 매개변수 모델이 진단 정확도에서 GPT-4를 앞섰다고 보고했다(구체 정확도 수치는 초록에 없음). [사실][^ref-1262] H. 실행·협업·예외 복구에서 본 REFLECT도 실패 원인 설명을 만든다는 점에서 이 영역에 닿는다.
    - 예지 정비: Pookkuttath 외(Sensors, 2021-12)는 대학 캠퍼스에서 청소 로봇의 관성 측정 장치(Inertial Measurement Unit, IMU) 진동 신호를 1차원 합성곱 신경망으로 정상·지형·충돌·조립 풀림·구조 불균형 5종으로 분류해 동시적 위치추정·지도작성(SLAM) 지도에 겹친 예지 정비 지도를 만들고, 실시간 현장 시험 정확도 91%를 보고했다(저자 보고). [사실][^ref-1057] 파이낸셜뉴스가 전한 현대자동차 발표에 따르면 AI 고장예측 시스템이 산업용 로봇팔의 모터 부하·진동·전류 신호로 고장 약 5일 전에 90% 이상 정확도로 이상을 감지한다(2026-05-28, 벤더 주장, 정확도 산정 방법 미공개). [추정][^ref-1059] 부품 수준의 신호 감시는 제조사·설비 정비 쪽 연계 대상이고, ROP 몫은 예측 결과를 정비·배정에 반영하는 데 있다. ISO 13381-1:2025는 기계 시스템 상태 감시·진단의 예지(prognostics) 일반 지침과 요구사항을 다루는 표준이다. [사실][^ref-1060]
- **47. AI·학습·적응과 모델 운영 ↔ [37. 관제 화면·실행 기록](../field-operations-and-monitoring/control-screen-and-execution-records.md)**: EU AI Act 제12조(2026-07-27 EUR-Lex 통합본 기준)는 고위험 AI 시스템이 수명 기간 동안 사건 기록을 자동으로 남길 수 있어야 한다고 정하고(원문 표현 ‘automatic recording of events (logs)’), 위험 상황·실질적 변경 식별, 시판 후 감시, 배포자의 운영 감시에 필요한 사건을 기록하게 한다. [사실][^ref-863] ROP의 AI 구성요소가 EU AI Act 고위험 분류(부속서 I 제품의 안전 구성요소 등)에 들어간다면 37. 관제 화면·실행 기록과 43. 데이터·관측성·배포가 남기는 기록이 제12조 로그 요건을 받쳐야 할 것으로 보이나, 해당 여부 자체가 열린 질문이다(oq-106). [추정][^ref-863][^ref-621]

### [K. 플랫폼 아키텍처·인프라](../platform-architecture-and-infrastructure/index.md)

- **44. 로봇 기반 모델·언어 모델 계획 ↔ [42. 분산 시스템·통신·컴퓨팅 구조](../platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md)**: Bruno·Sim·Hagiwara(2026-09, 프리프린트)는 범용 서비스 로봇의 LLM 연쇄 기반 작업 계획에서 로컬 오픈소스와 프런티어 클라우드 배치 맥락의 모델을 함께 평가했다. [사실][^ref-1043] FogROS2(2022-05)는 ROS 2 로봇의 계산 부담이 큰 작업을 클라우드·포그로 옮겨 실행하는 플랫폼이다. [사실][^ref-304]
- **47. AI·학습·적응과 모델 운영 ↔ [43. 데이터·관측성·배포](../platform-architecture-and-infrastructure/data-observability-and-deployment.md)**: OpenTelemetry 생성형 AI 의미 규약 저장소는 언어 모델 클라이언트 호출의 토큰 사용량 지표를 정의하며, 이 규약은 아직 개발(Development) 단계다(oq-212). [사실][^ref-1037] MLflow 모델 레지스트리는 모델 버전과 별칭으로 운영 모델의 교체·되돌림 경로를 관리하게 하는 오픈소스 도구다(로봇 플랫폼 적용 사례는 미확인). [사실][^ref-626] FogROS2와 OpenTelemetry 연결은 K. 플랫폼 아키텍처·인프라 페이지의 연결 절에도 같은 각주로 있다.

### [M. 안전](../safety/index.md)

M. 안전은 여러 대분류에 걸쳐 적용되며, L. AI·학습 기술과는 언어 모델이 만든 계획을 실행 전에 어떻게 검사하느냐에서 만난다. 로봇 자체의 안전 기능과 안전 인증은 연계 대상이고, 아래 연결은 ROP가 계획을 채택하기 전 검사 범위로만 읽는다.

- **44. 로봇 기반 모델·언어 모델 계획 ↔ [48. 안전·위험 관리](../safety/safety-and-risk-management.md)**: Robey 외(2024-10)는 언어 모델이 제어하는 로봇에 해로운 물리 행동을 하게 만드는 탈옥 알고리즘 RoboPAIR를 제시하고, 자율주행 LLM, GPT-4o 계획기를 쓴 Clearpath Jackal, GPT-3.5를 연동한 Unitree Go2의 세 설정에서 RoboPAIR와 여러 정적 기준 방법의 공격 성공률이 자주 100%에 이르렀다고 보고했다(어느 설정에서 100%였는지는 미확인, 저자 보고값). [사실][^ref-857] Ravichandran 외(2025-03 v1, 2026-03 v2)의 RoboGuard는 악성 프롬프트에서 격리한 신뢰 기점 LLM이 미리 정한 안전 규칙을 환경에 맞춰 시간 논리 제약으로 바꾸고, 제어 합성으로 계획과의 충돌을 해소해 최악의 탈옥 공격에서 위험 계획 실행을 92% 이상에서 3% 미만으로 줄였다고 보고했다(v2 기준, 저자 보고값). [사실][^ref-700]
- **47. AI·학습·적응과 모델 운영 ↔ 48. 안전·위험 관리**: 실행 전 안전 게이트나 가드레일 같은 계획 검사는 ROP가 AI 계획을 채택하기 전 검증 단계의 후보가 될 것으로 보이며, 로봇 자체의 안전 기능과 인증은 연계 대상으로 남고, 이런 AI가 제품 안전 구성요소로 분류되는지는 열린 질문이다(oq-106). [추정][^ref-417][^ref-700][^ref-621] EU AI Act(Regulation (EU) 2024/1689)는 부속서 I의 EU 조화 법령(기계류 등) 대상 제품의 안전 구성요소이거나 제품 자체이고 제3자 적합성 평가 대상인 AI 시스템을 고위험 AI로 분류한다(적용 시점은 개정 논의로 확정되지 않음). [사실][^ref-621] 태평양(BKL) 해설에 따르면 과기정통부의 고영향 인공지능사업자 책무 고시·가이드라인 초안은 개발 단계에서 사람이 개입할 기준과 긴급 정지 같은 개입 방법을, 운영 단계에서 성능 저하·오류 정기 점검 계획과 관리자 교육·훈련을 요구한다(2025-09-30 공개된 시행령(안)·고시(안)·가이드라인(안) 기준이며 확정본과의 일치는 미확인). [사실][^ref-1253] AI 위험관리·관리 체계 표준으로는 ISO/IEC 42001:2023(AI 관리 시스템), ISO/IEC 23894:2023(AI 위험관리 지침, 2023-02), NIST AI 위험관리 프레임워크(2023-01 발표)가 있다. [사실][^ref-618][^ref-619][^ref-617]

### [N. 보안·개인정보](../security-and-privacy/index.md)

- **44. 로봇 기반 모델·언어 모델 계획 ↔ [51. 인증·권한·격리](../security-and-privacy/authentication-authorization-and-isolation.md)**: 언어 모델 에이전트가 플랫폼 API를 도구로 호출하는 구조에서는 탈옥된 모델이 해로운 동작을 낼 수 있으므로, 모델에 넘기는 도구·로봇·구역 권한을 최소로 제한하는 접근통제가 두 대분류의 경계가 될 것으로 보인다(로봇 플릿 플랫폼의 권한 설계 사례는 미확인). [추정][^ref-854][^ref-857]
- **44. 로봇 기반 모델·언어 모델 계획 ↔ [52. 통신 보호·위협 관리·감사](../security-and-privacy/communication-protection-threat-management-and-audit.md)**: M. 안전에서 본 RoboPAIR(언어 모델 제어 로봇 탈옥 알고리즘) 결과가 이 영역에도 닿는다.
- **45. 문서·도면·장면 이해 ↔ [53. 개인정보·영상 데이터](../security-and-privacy/privacy-and-video-data.md)**: 2026-05-06 ICT 규제샌드박스 심의위원회는 뉴빌리티의 ‘영상정보 원본 활용 자율주행 배달 로봇 시스템 고도화’ 과제에 실증특례를 승인해 배달로봇 카메라 원본 영상을 AI 학습에 쓰게 했고, 연구 목적 내 활용·개인 식별 금지·제3자 제공 금지·전담 조직·보호대책을 조건으로 붙였다(기사 1건 기준이며 정부 보도자료는 확인하지 못했다). [사실][^ref-1263] Brorsson 외(2025-12)는 천장 카메라 기반 운반 로봇 사례의 제약으로 작업자·독점 제품·기밀 공정이 영상에 찍히는 개인정보·기밀 문제를 들었다(oq-228). [사실][^ref-308]

### [O. 검증·도입·수명주기](../verification-deployment-and-lifecycle/index.md)

- **44. 로봇 기반 모델·언어 모델 계획·46. 예측·학습 기반 최적화·47. AI·학습·적응과 모델 운영 ↔ [54. 시험·형식 검증·벤치마크](../verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md)**: Breck 외(Google Research, 2017)의 ML Test Score는 머신러닝 시스템의 운영 준비 상태와 기술 부채 감소를 점검하는 평가 기준표다. [사실][^ref-625] LoTa-Bench(ICLR 2024)는 언어 지향 작업 계획기를 체화 에이전트 환경에서 평가하는 벤치마크로 공식 저장소가 공개되어 있다. [사실][^ref-541] 다만 현장 제약이 있는 다중 로봇 계획기의 공통 벤치마크는 이번 조사에서 확인하지 못했다(oq-217). POGEMA(ICLR 2025)는 협력 다중 에이전트 경로 찾기의 학습 기반·탐색 기반 방법을 같은 조건에서 비교하는 벤치마크 플랫폼이다(격자 조건의 성과가 현장 처리량으로 이어지는지는 미확인, oq-220). [사실][^ref-1056] I. 설계·시뮬레이션에서 본 SRCC도 시뮬레이션 평가가 현실 성능을 얼마나 예측하는지 재는 지표라는 점에서 이 영역에 닿는다.
- **45. 문서·도면·장면 이해 ↔ [55. 현장 조사·설치·시운전](../verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md)**: 교차 규칙의 매뉴얼 해석 대상인 55. 현장 조사·설치·시운전에서는 URDF·자산관리셸에서 능력 정의 초안을 LLM으로 만드는 방법이 새 로봇 온보딩의 반복 작업을 줄이는 데 쓰일 것으로 보이나, 온보딩 현장에 적용해 소요를 측정한 사례는 확인하지 못했다. [추정][^ref-239][^ref-1072]
- **47. AI·학습·적응과 모델 운영 ↔ [56. 운영 이관·확대·교육](../verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md)**: M. 안전에서 본 고영향 인공지능사업자 책무 초안의 관리자 교육·훈련 요구가 이 영역의 운영 이관·교육과 이어진다.
- **47. AI·학습·적응과 모델 운영 ↔ [57. 자산·소프트웨어 수명주기 관리](../verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md)**: Sculley 외(2015)는 실제 머신러닝 시스템이 일반 코드의 유지보수 문제에 더해 경계 침식, 얽힘, 숨은 피드백 루프, 선언되지 않은 소비자, 데이터 의존성 같은 고유 위험으로 큰 유지 비용을 낳는다고 지적했다. [사실][^ref-624] K. 플랫폼 아키텍처·인프라에서 본 MLflow 모델 레지스트리의 교체·되돌림 경로도 이 영역의 모델 수명주기 관리와 이어진다.

### [P. 거버넌스·법규·사회](../governance-law-and-society/index.md)

- **47. AI·학습·적응과 모델 운영 ↔ [59. 법·규제·보험·라이선스](../governance-law-and-society/law-regulation-insurance-and-licensing.md)**: 한국 「인공지능 발전과 신뢰 기반 조성 등에 관한 기본법」과 시행령은 2026-01-22 시행되었고, 사람의 생명·안전·기본권에 중대한 영향을 미칠 수 있는 영역의 AI를 고영향 인공지능으로 두어 별도 책무를 부과한다(개정 법률 시행일과 고영향 영역 목록은 미확인). [사실][^ref-620] 태평양(BKL) 해설에 따르면 고영향 인공지능사업자 책무 초안은 위험관리방안(수명주기 전반 준수·주기적 점검), 결과 도출 기준과 학습용 데이터 개요의 설명 방안, 이용자 보호방안을 요구하고 홈페이지 게시와 관련 문서 5년 보관을 정한다(2025-09-30 공개된 시행령(안)·고시(안)·가이드라인(안) 기준이며 확정본과의 일치는 미확인). [사실][^ref-1253] M. 안전에서 본 EU AI Act의 고위험 분류도 이 영역에 속한다.
- **47. AI·학습·적응과 모델 운영 ↔ [58. 다사업자 책임·계약·데이터](../governance-law-and-society/multi-party-responsibility-contracts-and-data.md)**: 고영향 인공지능 책무가 ‘사업자’에게 부과되므로 로봇 작업 계획·배정 AI를 ROP 사업자·현장 운영사·로봇 제조사 가운데 누가 개발·이용 사업자로서 책임질지가 다사업자 계약 항목이 될 것으로 보이며, 조직 차원의 AI 관리 체계(ISO/IEC 42001)가 그 운영 틀이 될 수 있어 보인다(oq-105). [추정][^ref-620][^ref-618][^ref-1253] 법령 해석과 적용 판단은 법무·운영 사업자 쪽 연계 대상이며, ROP가 맡을 몫은 그 판단에 필요한 기록·설명 기능이다.

### [Q. 현장 유형별 적용](../site-type-applications/index.md)

Q. 현장 유형별 적용은 현장마다 다른 요구를 모으고, 모든 현장에 공통인 기능은 A~P에 둔다. 위 연결의 근거 가운데 현장 유형이 드러난 것은 다음과 같다.

- [61. 물류창고](../site-type-applications/warehouse.md): 로보티즈 AI 워커 실증 계획(목표치, 벤더 주장), CCTV 카메라망만으로 여러 로봇을 계획·제어한 시연, DeepFleet과 그 혼잡 예측(효율 수치는 벤더 주장), 작업자–AMR 배정 강화학습, RaaS 과금 조건의 AMR 대수 산정.
- [62. 제조 공장](../site-type-applications/manufacturing-plant.md): BMW 스파턴버그 공장의 Figure 02 배치(벤더 주장, 기간 충돌), 상용차 공장의 천장 카메라 기반 운반 로봇과 영상의 개인정보·기밀 제약, 현대자동차 로봇팔 고장예측(벤더 주장).
- [63. 병원·의료](../site-type-applications/hospital-and-healthcare.md): 입원 병동 간호 업무 요청 데이터로 평가한 예측 인지형 배정 강화학습.
- [64. 상업 시설](../site-type-applications/commercial-facilities.md): 쇼핑몰 평면도 분할·점포 인식(논문 평가값).
- [65. 가정·공동주택](../site-type-applications/home-and-apartment.md): Physical Intelligence의 π0.5(2025-04)는 여러 로봇 데이터·고수준 의미 예측·웹 데이터를 함께 학습해 처음 보는 가정집에서 부엌·침실 정리 같은 장기 작업을 수행했다고 보고했으며, 이는 상용 배치가 아닌 연구 평가다. [사실][^ref-1047] 저수준 조작 정책은 연계 대상이다.
- [66. 실외](../site-type-applications/outdoor.md): 대규모 실외 환경의 다중 로봇 3차원 장면 그래프와 언어 접지 계획, 배달로봇 원본 영상 AI 학습 실증특례.
- [67. 기타 현장](../site-type-applications/other-sites.md): 대학 캠퍼스 청소 로봇의 진동 기반 예지 정비 지도.

### 아직 근거를 찾지 못한 연결

게시 페이지와 이번 조사에서 L. AI·학습 기술과 잇는 근거를 찾지 못한 세부영역은 17. 작업 대상·자산 식별과 인계 추적, 30. 로봇 간 협업·물리적 인계, 39. 운영 성과 측정·개선, 40. 운영 절차·요청 창구, 49. 사람 근접 안전, 50. 안전 표준·인증·사고 조사, 60. 노동·수용성·접근성이다. 다음 조사에서 근거를 찾으면 이 절에 더한다.

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 84건이다(논문 59건 · 기사·보고서 6건 · 업체 발표 3건 · 표준·오픈소스·기관 자료 16건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-1071](../../references/ref-1071.md) — Groß, J., & Heidrich, J. (arXiv), AAS-RAIL: Improving Information Extraction for Asset Administration Shells through Retrieval-Augmented In-Context Learning (발행 2026-09-07)
- [ref-1043](../../references/ref-1043.md) — Bruno, L. D. M., Sim, J., & Hagiwara, Y. (arXiv), Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots (발행 2026-09)
- [ref-832](../../references/ref-832.md) — Xia, Y., Weyrich, M., Jazdi, N., Stümpfle, J., Sigel, J., Narla, A., Reynolds, G. K., Jawor-Baczynska, A., & Llopart, P., LLM Agents Perform Controlled Experiments Using Simulation Models (발행 2026-08-22)
- [ref-1062](../../references/ref-1062.md) — Garces, D., Castro, S., Haimovich, A., Crowe, B., & Gil, S. (arXiv), Model-Based Reinforcement Learning for Heterogeneous Multi-Robot Task Assignment Under Distribution Shifts (발행 2026-08)
- [ref-1065](../../references/ref-1065.md) — Robinson, L., Ramtoula, B., Izaaryene, A., Newman, P., & De Martini, D. (arXiv), Multi-Robot Planning and Control from CCTV Camera Networks in a Real Warehouse (발행 2026-06-04)
- [ref-822](../../references/ref-822.md) — Howard, T. L. (California Polytechnic State University, 석사논문), A Simulation, Analytical, and Machine-Learning Approach for Collaborative Autonomous Mobile Robot Fleet Sizing in Picker-to-Parts Facilities (발행 2026-06)
- [ref-239](../../references/ref-239.md) — Dussard, B., & Sarthou, G. (LAAS-CNRS), Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF (발행 2026-06)
- [ref-201](../../references/ref-201.md) — Nabizada, H., Wirt, T., Vieira da Silva, L. M., Gehlhoff, F., & Fay, A., From Capability Models to Automated Planning: An AAS-Native Approach for Automatic PDDL Generation (발행 2026-06)
- [ref-1069](../../references/ref-1069.md) — Modi, G., Buoso, D., Averta, G., & De Martini, D. (arXiv), RGB-only Active 3D Scene Graph Generation for Indoor Mobile Robots (발행 2026-05-18)
- [ref-417](../../references/ref-417.md) — Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab), Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems (발행 2026-04)
- 그 밖에 49건

**기사·보고서**

- [ref-627](../../references/ref-627.md) — 머니투데이, 포장은 로봇이, 간선운송은 무인차가…물류현장 스며든 '피지컬 AI' (발행 2026-09-19)
- [ref-1059](../../references/ref-1059.md) — 파이낸셜뉴스, 현대차, '로봇 고장' AI로 잡는다…5일전 90%이상 감지 (발행 2026-05-28)
- [ref-1263](../../references/ref-1263.md) — 메트로신문, AI·커머스·플랫폼 분야 규제 특례 확대…사업화 지원 (발행 2026-05-06)
- [ref-1052](../../references/ref-1052.md) — 헬로티, VLA 이식한 로보티즈 'AI 워커', 물류 현장 난제 해결사로 전격 투입 (발행 2025-11-26)
- [ref-1253](../../references/ref-1253.md) — 법무법인 태평양(BKL) AI팀, AI기본법 가이드라인 해설 시리즈 (4) 고영향 인공지능사업자의 책무 관련 고시 및 가이드라인 (발행 2025-09-30)
- [ref-1050](../../references/ref-1050.md) — 지디넷코리아, K-휴머노이드 연합, 출범 3주 만에 협약 4건 성과 (발행 2025-05-01)

**업체 발표**

- [ref-1051](../../references/ref-1051.md) — BMW Group, BMW Group advances the use of Physical AI in production with Figure 03 project in Spartanburg (발행 2026-06-25)
- [ref-1054](../../references/ref-1054.md) — Amazon Science, Amazon builds first foundation model for multirobot coordination (발행 2025-08-11)
- [ref-1063](../../references/ref-1063.md) — CJ대한통운, 'AI 혁신 기술'이 이끄는 CJ대한통운의 스마트 물류 혁명 (발행 2021-07-28)

**표준·오픈소스·기관 자료**

- [ref-854](../../references/ref-854.md) — Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse, Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP) (발행 2026-06-25)
- [ref-1060](../../references/ref-1060.md) — ISO (ISO/TC 108), ISO 13381-1:2025 Condition monitoring and diagnostics of machine systems — Prognostics — Part 1: General guidelines and requirements (발행 2025)
- [ref-863](../../references/ref-863.md) — European Commission — AI Act Service Desk, Article 12: Record-keeping (Regulation (EU) 2024/1689, Artificial Intelligence Act) (발행 2024-06-13)
- [ref-1012](../../references/ref-1012.md) — AI Hub (한국지능정보사회진흥원) — 구축 주관 에이치씨아이플러스(주), 건축 도면 데이터 (발행 2023-07-26)
- [ref-619](../../references/ref-619.md) — ISO/IEC, ISO/IEC 23894:2023 - AI — Guidance on risk management (발행 2023-02)
- [ref-617](../../references/ref-617.md) — NIST, NIST Risk Management Framework Aims to Improve Trustworthiness of Artificial Intelligence (발행 2023-01-26)
- [ref-618](../../references/ref-618.md) — ISO/IEC, ISO/IEC 42001:2023 - AI management systems (발행 2023)
- [ref-626](../../references/ref-626.md) — MLflow (Linux Foundation 오픈소스 프로젝트), ML Model Registry \| MLflow AI Platform (발행 미확인)
- [ref-621](../../references/ref-621.md) — European Commission, AI Act \| Shaping Europe's digital future (발행 미확인)
- [ref-620](../../references/ref-620.md) — 국가법령정보센터(과학기술정보통신부), 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법 (발행 미확인)
- 그 밖에 6건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-10-09 · 갱신 · [L. AI·학습 기술](index.md) — '다른 대분류와의 연결' 절 신규 작성(A~K·M~Q 16개 대분류, 교차 규칙 네 갈래와 C 원칙 반영, 미연결 7개 영역 명시), 페이지 끝에 '참고 자료' 절 추가(각주 정의 70건). 2차: 번호만 쓴 항목 제목 2곳 수정, 52번 항목의 근거 없는 해석 문장을 태그 없는 연결 설명으로 교체, 38·12번 항목을 하위 항목으로 나눔, ROS 첫 등장 풀어쓰기 (실행 2026-10-09-08)
- 2026-10-09 · 요약 · [L. AI·학습 기술](index.md) — L. AI·학습 기술: 다른 대분류와의 연결 절 신규 작성(A~K·M~Q 16개 대분류, 교차 규칙 네 갈래·C 원칙 반영, 미연결 7개 영역 명시)과 참고 자료 절 추가 (실행 2026-10-09-08)
- 2026-09-30 · 갱신 · [46. 예측·학습 기반 최적화](prediction-and-learning-based-optimization.md) — 영역 심화: 섹션 3~11 신규 작성(학습 기반 배정·경로, 결정 중심 학습, 배터리·고장 예측, 현장 사례 4종), 각주 14건, 프런트매터 related_areas·tags·sources·confidence 추가(2차 재실행: 이 페이지 본문 변경 없음) (실행 2026-09-30-09)
- 2026-09-30 · 생성 · [46. 예측·학습 기반 최적화 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area46-s6.md) — 자동 분리: 46. 예측·학습 기반 최적화 의 "6. 대표 접근법과 기술" 절(1,868자)을 옮겼다. 2차: DeepFleet·34. 시뮬레이션·예측용 디지털 트윈 구분 문장의 태그를 [의견]에서 [추정]으로 되돌렸다 (실행 2026-09-30-09)
- 2026-09-30 · 생성 · [46. 예측·학습 기반 최적화 — 대표 연구와 자료](../../topics/2026/2026-09-30-area46-s8.md) — 자동 분리: 46. 예측·학습 기반 최적화 의 "8. 대표 연구와 자료" 절(1,712자)을 옮겼다 (실행 2026-09-30-09)
<!-- auto:category-recent:end -->

## 참고 자료

[^ref-1051]: BMW Group, BMW Group advances the use of Physical AI in production with Figure 03 project in Spartanburg, 2026-06-25, https://www.press.bmwgroup.com/global/article/detail/T0458778EN/bmw-group-advances-the-use-of-physical-ai-in-production-with-figure-03-project-in-spartanburg?language=en, 접근일 2026-10-09 (원문 미열람)
[^ref-1052]: 헬로티, VLA 이식한 로보티즈 'AI 워커', 물류 현장 난제 해결사로 전격 투입, 2025-11-26, https://www.hellot.net/news/article.html?no=107567, 접근일 2026-10-09 (원문 미열람)
[^ref-822]: Howard, T. L. (California Polytechnic State University, San Luis Obispo, 석사논문), A Simulation, Analytical, and Machine-Learning Approach for Collaborative Autonomous Mobile Robot Fleet Sizing in Picker-to-Parts Facilities, 2026-06, https://digitalcommons.calpoly.edu/theses/3387, 접근일 2026-10-09 (원문 미열람)
[^ref-1253]: 법무법인 태평양(BKL) AI팀, AI기본법 가이드라인 해설 시리즈 (4) 고영향 인공지능사업자의 책무 관련 고시 및 가이드라인, 2025-09-30, https://www.bkl.co.kr/law/insight/newsletter/6248, 접근일 2026-10-09
[^ref-620]: 국가법령정보센터(과학기술정보통신부), 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법, 미확인, https://www.law.go.kr/lsInfoP.do?lsiSeq=268543, 접근일 2026-10-09 (원문 미열람)
[^ref-1071]: Groß, J., & Heidrich, J. (arXiv), AAS-RAIL: Improving Information Extraction for Asset Administration Shells through Retrieval-Augmented In-Context Learning, 2026-09-07, https://arxiv.org/abs/2609.07334, 접근일 2026-10-09 (원문 미열람)
[^ref-1072]: Xia, Y., Xiao, Z., Jazdi, N., & Weyrich, M. (IEEE Access, arXiv), Generation of Asset Administration Shell with Large Language Model Agents: Toward Semantic Interoperability in Digital Twins in the Context of Industry 4.0, 2024-06-24, https://arxiv.org/abs/2403.17209, 접근일 2026-10-09 (원문 미열람)
[^ref-239]: Dussard, B., & Sarthou, G. (LAAS-CNRS), Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF, 2026-06, https://arxiv.org/abs/2606.17073, 접근일 2026-10-09 (원문 미열람)
[^ref-238]: Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A., On the Use of Large Language Models to Generate Capability Ontologies, 2024-04, https://arxiv.org/abs/2404.17524, 접근일 2026-10-09 (원문 미열람)
[^ref-1074]: Google (google/langextract), LangExtract — README, 미확인, https://github.com/google/langextract, 접근일 2026-10-09 (원문 미열람)
[^ref-201]: Nabizada, H., Wirt, T., Vieira da Silva, L. M., Gehlhoff, F., & Fay, A., From Capability Models to Automated Planning: An AAS-Native Approach for Automatic PDDL Generation, 2026-06, https://arxiv.org/abs/2606.02167, 접근일 2026-10-09 (원문 미열람)
[^ref-092]: Liu, B., Jiang, Y., Zhang, X., Liu, Q., Zhang, S., Biswas, J., & Stone, P., LLM+P: Empowering Large Language Models with Optimal Planning Proficiency, 2023-04, https://arxiv.org/abs/2304.11477, 접근일 2026-10-09 (원문 미열람)
[^ref-1045]: Brohan, A., Brown, N. 외 (Google DeepMind, arXiv), RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control, 2023-07-28, https://arxiv.org/abs/2307.15818, 접근일 2026-10-09 (원문 미열람)
[^ref-1047]: Physical Intelligence (Black, K., Finn, C., Levine, S. 외, arXiv), π0.5: a Vision-Language-Action Model with Open-World Generalization, 2025-04-22, https://arxiv.org/abs/2504.16054, 접근일 2026-10-09 (원문 미열람)
[^ref-090]: Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C., SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models, 2023-09, https://arxiv.org/abs/2309.10062, 접근일 2026-10-09 (원문 미열람)
[^ref-854]: Open Source Robotics Alliance (OSRA) Interop SIG, Open Robotics Discourse, Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP), 2026-06-25, https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687, 접근일 2026-10-09 (원문 미열람)
[^ref-416]: Rana, K., Haviland, J., Garg, S., Abou-Chakra, J., Reid, I., & Suenderhauf, N. (CoRL 2023, arXiv), SayPlan: Grounding Large Language Models using 3D Scene Graphs for Scalable Robot Task Planning, 2023-07-12, https://arxiv.org/abs/2307.06135, 접근일 2026-10-09 (원문 미열람)
[^ref-351]: Ren, A. Z. 외, Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners, 2023-07, https://arxiv.org/abs/2307.01928, 접근일 2026-10-09 (원문 미열람)
[^ref-359]: Wang, W. 외, Learning to Ask: When LLM Agents Meet Unclear Instruction, 2024-09, https://arxiv.org/abs/2409.00557, 접근일 2026-10-09 (원문 미열람)
[^ref-354]: cog-model (AmbiK 저자), AmbiK-dataset — README (AmbiK: Dataset of Ambiguous Tasks in Kitchen Environment), 미확인, https://github.com/cog-model/AmbiK-dataset, 접근일 2026-10-09 (원문 미열람)
[^ref-832]: Xia, Y., Weyrich, M., Jazdi, N., Stümpfle, J., Sigel, J., Narla, A., Reynolds, G. K., Jawor-Baczynska, A., & Llopart, P., LLM Agents Perform Controlled Experiments Using Simulation Models, 2026-08-22, https://arxiv.org/abs/2608.23622, 접근일 2026-10-09 (원문 미열람)
[^ref-076]: DeFazio, D., Mehta, H., Wang, M., Yang, P., Blackburn, J., & Zhang, S., Vision Language Models Can Parse Floor Plan Maps, 2024-09, https://arxiv.org/abs/2409.12842, 접근일 2026-10-09 (원문 미열람)
[^ref-1073]: Kondratenko, A., Birhane, M., Hsain, H. E., & Maciocci, G. (arXiv), AECV-Bench: Benchmarking Multimodal Models on Architectural and Engineering Drawings Understanding, 2026-01-08, https://arxiv.org/abs/2601.04819, 접근일 2026-10-09 (원문 미열람)
[^ref-063]: Kalervo, A., Ylioinas, J., Häikiö, M., Karhu, A., & Kannala, J., CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis, 2019-04, https://arxiv.org/abs/1904.01920, 접근일 2026-10-09 (원문 미열람)
[^ref-067]: Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P., FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting, 2021-05, https://arxiv.org/abs/2105.07147, 접근일 2026-10-09 (원문 미열람)
[^ref-1012]: AI Hub (한국지능정보사회진흥원) — 구축 주관 에이치씨아이플러스(주), 건축 도면 데이터, 2023-07-26, https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71465, 접근일 2026-10-09 (원문 미열람)
[^ref-1066]: Su, M., Shi, W., Zhao, D., Cheng, D., & Zhang, J. (Sensors 22(7)), A High-Precision Method for Segmentation and Recognition of Shopping Mall Plans, 2022-03-25, https://pmc.ncbi.nlm.nih.gov/articles/PMC9003070/, 접근일 2026-10-09 (원문 미열람)
[^ref-1070]: Strader, J., Ray, A., Arkin, J. 외 (arXiv), Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs, 2025-07-10, https://arxiv.org/abs/2506.07454, 접근일 2026-10-09 (원문 미열람)
[^ref-1018]: Xie, F., Schwertfeger, S., & Blum, H. (RA-L 2026 채택, arXiv), osmAG-LLM: Zero-Shot Open-Vocabulary Object Navigation via Semantic Maps and Large Language Models Reasoning, 2025-07, https://arxiv.org/abs/2507.12753, 접근일 2026-10-09 (원문 미열람)
[^ref-308]: Brorsson, E. 외, Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives, 2025-12, https://arxiv.org/abs/2512.15215, 접근일 2026-10-09 (원문 미열람)
[^ref-1172]: Rudenko, A., Palmieri, L., Herman, M., Kitani, K. M., Gavrila, D. M., & Arras, K. O. (arXiv; IJRR 39(8), 2020), Human Motion Trajectory Prediction: A Survey, 2019-12-17, https://arxiv.org/abs/1905.06113, 접근일 2026-10-09 (원문 미열람)
[^ref-171]: NASA Jet Propulsion Laboratory (nasa-jpl), ROSA — ROS Agent (GitHub README), 미확인, https://github.com/nasa-jpl/rosa, 접근일 2026-10-09 (원문 미열람)
[^ref-1065]: Robinson, L., Ramtoula, B., Izaaryene, A., Newman, P., & De Martini, D. (arXiv), Multi-Robot Planning and Control from CCTV Camera Networks in a Real Warehouse, 2026-06-04, https://arxiv.org/abs/2606.06762, 접근일 2026-10-09 (원문 미열람)
[^ref-1063]: CJ대한통운, 'AI 혁신 기술'이 이끄는 CJ대한통운의 스마트 물류 혁명, 2021-07-28, https://www.cjlogistics.com/ko/newsroom/latest/LT_00000238, 접근일 2026-10-09 (원문 미열람)
[^ref-623]: Agrawal, A. 외, RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments, 2022-09, https://arxiv.org/abs/2209.05738, 접근일 2026-10-09 (원문 미열람)
[^ref-1062]: Garces, D., Castro, S., Haimovich, A., Crowe, B., & Gil, S. (arXiv), Model-Based Reinforcement Learning for Heterogeneous Multi-Robot Task Assignment Under Distribution Shifts, 2026-08, https://arxiv.org/abs/2608.21554, 접근일 2026-10-09 (원문 미열람)
[^ref-1053]: Agaskar, A., Siva, S., Pickering, W. 외 (Amazon, arXiv), DeepFleet: Multi-Agent Foundation Models for Mobile Robots, 2025-08, https://arxiv.org/abs/2508.08574, 접근일 2026-10-09 (원문 미열람)
[^ref-1054]: Amazon Science, Amazon builds first foundation model for multirobot coordination, 2025-08-11, https://www.amazon.science/blog/amazon-builds-first-foundation-model-for-multirobot-coordination, 접근일 2026-10-09 (원문 미열람)
[^ref-1056]: Skrynnik, A., Andreychuk, A., Borzilov, A., Chernyavskiy, A., Yakovlev, K., & Panov, A. (ICLR 2025, arXiv), POGEMA: A Benchmark Platform for Cooperative Multi-Agent Pathfinding, 2025-04, https://arxiv.org/abs/2407.14931, 접근일 2026-10-09 (원문 미열람)
[^ref-199]: arXiv 2410.21415 저자(미확인), Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding, 2024-10, https://arxiv.org/abs/2410.21415, 접근일 2026-10-09 (원문 미열람)
[^ref-1064]: Zhang, Y., Jiang, H., Bhatt, V., Nikolaidis, S., & Li, J. (arXiv, IJCAI 2024), Guidance Graph Optimization for Lifelong Multi-Agent Path Finding, 2024-02, https://arxiv.org/abs/2402.01446, 접근일 2026-10-09 (원문 미열람)
[^ref-1058]: Poskart, B., Iskierka, G., Krot, K., Burduk, R., Gwizdal, P., & Gola, A. (Sensors), Multi-Parameter Predictive Model of Mobile Robot's Battery Discharge for Intelligent Mission Planning in Multi-Robot Systems, 2022-12-15, https://pmc.ncbi.nlm.nih.gov/articles/PMC9786877/, 접근일 2026-10-09 (원문 미열람)
[^ref-170]: Su, X., Xu, J., van Kaick, O., Xu, K., & Hu, R., IMR-LLM: Industrial Multi-Robot Task Planning and Program Generation using Large Language Models, 2026-03, https://arxiv.org/abs/2603.02669, 접근일 2026-10-09 (원문 미열람)
[^ref-1061]: Elmachtoub, A. N., & Grigas, P. (arXiv), Smart "Predict, then Optimize", 2017-10, https://arxiv.org/abs/1710.08005, 접근일 2026-10-09 (원문 미열람)
[^ref-417]: Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab), Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems, 2026-04, https://arxiv.org/abs/2604.05427, 접근일 2026-10-09 (원문 미열람)
[^ref-453]: Liu, Z., Bahety, A., & Song, S. (CoRL 2023, arXiv), REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction, 2023-06-27, https://arxiv.org/abs/2306.15724, 접근일 2026-10-09
[^ref-1245]: Smit, I. G., Bukhsh, Z., Pechenizkiy, M., Alogariastos, K., Hendriks, K., & Zhang, Y. (arXiv), Learning Efficient and Fair Policies for Uncertainty-Aware Collaborative Human-Robot Order Picking, 2024-04-09, https://arxiv.org/abs/2404.08006, 접근일 2026-10-09 (원문 미열람)
[^ref-241]: Sommer, M., Stjepandić, J., Stobrawa, S., & von Soden, M., Automated generation of digital twin for a built environment using scan and object detection as input for production planning, 2023, https://www.sciencedirect.com/science/article/abs/pii/S2452414X23000353, 접근일 2026-10-09 (원문 미열람)
[^ref-815]: Yang, Y., Sun, F.-Y., Weihs, L. 외 (Allen Institute for AI 등), Holodeck: Language Guided Generation of 3D Embodied AI Environments, 2023-12-14, https://arxiv.org/abs/2312.09067, 접근일 2026-10-09 (원문 미열람)
[^ref-1127]: Kadian, A., Truong, J., Gokaslan, A., Clegg, A., Wijmans, E., Lee, S., Savva, M., Chernova, S., & Batra, D. (arXiv / IEEE RA-L), Sim2Real Predictivity: Does Evaluation in Simulation Predict Real-World Performance?, 2020-08, https://arxiv.org/abs/1912.06321, 접근일 2026-10-09 (원문 미열람)
[^ref-741]: Aljalbout, E. 외(University of Zurich·NVIDIA·University of Washington), The Reality Gap in Robotics: Challenges, Solutions, and Best Practices, 2025-10, https://arxiv.org/abs/2510.20808, 접근일 2026-10-09 (원문 미열람)
[^ref-1262]: Herrmann, J. E., Gopinath, A. M., Norrlöf, M., & Müller, M. N. (arXiv), Diagnosing Robotics Systems Issues with Large Language Models, 2024-10-06, https://arxiv.org/abs/2410.09084, 접근일 2026-10-09
[^ref-1057]: Pookkuttath, S., Elara, M. R., Sivanantham, V., & Ramalingam, B. (Sensors), AI-Enabled Predictive Maintenance Framework for Autonomous Mobile Cleaning Robots, 2021-12-21, https://pmc.ncbi.nlm.nih.gov/articles/PMC8747287/, 접근일 2026-10-09 (원문 미열람)
[^ref-1059]: 파이낸셜뉴스, 현대차, '로봇 고장' AI로 잡는다…5일전 90%이상 감지, 2026-05-28, https://www.fnnews.com/news/202605280925297568, 접근일 2026-10-09 (원문 미열람)
[^ref-1060]: ISO (ISO/TC 108), ISO 13381-1:2025 Condition monitoring and diagnostics of machine systems — Prognostics — Part 1: General guidelines and requirements, 2025, https://www.iso.org/standard/88029.html, 접근일 2026-10-09 (원문 미열람)
[^ref-863]: European Commission — AI Act Service Desk, Article 12: Record-keeping (Regulation (EU) 2024/1689, Artificial Intelligence Act), 2024-06-13, https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12, 접근일 2026-10-09
[^ref-621]: European Commission, AI Act | Shaping Europe's digital future, 미확인, https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai, 접근일 2026-10-09 (원문 미열람)
[^ref-1043]: Bruno, L. D. M., Sim, J., & Hagiwara, Y. (arXiv), Design and Evaluation of LLM Chaining-Based Task Planning for General Purpose Service Robots, 2026-09, https://arxiv.org/abs/2609.29043, 접근일 2026-10-09 (원문 미열람)
[^ref-304]: Ichnowski, J., Chen, K. 외(UC Berkeley AUTOLAB), FogROS2: An Adaptive Platform for Cloud and Fog Robotics Using ROS 2, 2022-05, https://arxiv.org/abs/2205.09778, 접근일 2026-10-09 (원문 미열람)
[^ref-1037]: OpenTelemetry (open-telemetry/semantic-conventions-genai), semantic-conventions-genai/docs/gen-ai/gen-ai-token-metrics.md, 미확인, https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/gen-ai/gen-ai-token-metrics.md, 접근일 2026-10-09 (원문 미열람)
[^ref-626]: MLflow (Linux Foundation 오픈소스 프로젝트), ML Model Registry | MLflow AI Platform, 미확인, https://mlflow.org/docs/latest/ml/model-registry/, 접근일 2026-10-09 (원문 미열람)
[^ref-857]: Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J. (University of Pennsylvania, arXiv), Jailbreaking LLM-Controlled Robots, 2024-10-17, https://arxiv.org/abs/2410.13691, 접근일 2026-10-09
[^ref-700]: Ravichandran, Z., Robey, A., Kumar, V., Pappas, G. J., & Hassani, H. (arXiv), Safety Guardrails for LLM-Enabled Robots, 2025-03-10, https://arxiv.org/abs/2503.07885, 접근일 2026-10-09
[^ref-618]: ISO/IEC, ISO/IEC 42001:2023 - AI management systems, 2023, https://www.iso.org/standard/42001, 접근일 2026-10-09 (원문 미열람)
[^ref-619]: ISO/IEC, ISO/IEC 23894:2023 - AI — Guidance on risk management, 2023-02, https://www.iso.org/standard/77304.html, 접근일 2026-10-09 (원문 미열람)
[^ref-617]: NIST, NIST Risk Management Framework Aims to Improve Trustworthiness of Artificial Intelligence, 2023-01-26, https://nist.gov/news-events/news/2023/01/nist-risk-management-framework-aims-improve-trustworthiness-artificial, 접근일 2026-10-09 (원문 미열람)
[^ref-1263]: 메트로신문, AI·커머스·플랫폼 분야 규제 특례 확대…사업화 지원, 2026-05-06, https://www.metroseoul.co.kr/article/20260506500296, 접근일 2026-10-09
[^ref-625]: Breck, E. 외 (Google Research), The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction, 2017, https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/, 접근일 2026-10-09 (원문 미열람)
[^ref-541]: lbaa2022 (LoTa-Bench 공식 저장소), LLMTaskPlanning — LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents (ICLR 2024) (GitHub README), 미확인, https://github.com/lbaa2022/LLMTaskPlanning, 접근일 2026-10-09 (원문 미열람)
[^ref-624]: Sculley, D. 외, Hidden Technical Debt in Machine Learning Systems, 2015, https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems, 접근일 2026-10-09 (원문 미열람)
````

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

### templates/area.md

```markdown
---
title: "{{area_no}}. {{area_name}}"        # 원문 명칭 그대로. 예: "17. 작업 대상·자산 식별과 인계 추적"
type: area
category: "{{category}}"                    # 소속 대분류 원문 명칭. 예: "E. 사물·사람·실시간 상태"
area_no: {{area_no}}                        # 1~67 정수
related_areas: [{{related_areas}}]          # 10절에서 연결한 세부영역 번호. 예: [18, 29, 30]. 없으면 []
tags: [{{tags}}]                            # 핵심 용어 3~6개. 예: [EPCIS, 인계 확인, 자산 추적]. 시드면 []
status: {{status}}                          # seed | draft | verified | published | needs_update | deprecated
confidence: {{confidence}}                  # high | medium | low. 내용 검증 에이전트가 부여. 시드면 이 줄을 뺀다
created: {{created}}                        # YYYY-MM-DD. 페이지를 처음 만든 날
updated: {{updated}}                        # YYYY-MM-DD. 마지막으로 내용을 바꾼 날
sources: [{{sources}}]                      # 이 페이지 각주에 쓴 참고문헌 id. 예: [ref-003, ref-021]. 없으면 []
last_run: {{last_run}}                      # 이 페이지를 마지막으로 다룬 실행 날짜 YYYY-MM-DD. 시드면 이 줄을 뺀다
version: {{version}}                        # 정수. 시드 1, 갱신마다 +1
---
<!--
[템플릿] 세부 연구영역 페이지 (type: area)
경로: docs/categories/<대분류 slug>/<영역 slug>.md  (아래 경로 규약 표. 2026-09-28 개정부터 폴더·파일 이름에 대분류 문자·영역 번호를 붙이지 않는다)
쓰임: 구축 시 시드 생성 → 영역 심화 실행(1주기)에서 3~11절 작성 → 갱신·월간 재검증 실행에서 부분 갱신.
시드 규칙(4.4): 1절·2절의 원문 정의·질문, 소속 대분류, 원문 주석(2절의 "> 원문 주석:" 인용 블록. 예: 17. 작업 대상·자산 식별과 인계 추적의 EPCIS 언급, 14. 도면·BIM에서 지도 만들기·15. 지도·공간·위치 모델·16. 장소 의미·지도 관리의 지도 관리 주석, 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈의 구분, L. AI·학습 기술의 교차 적용 주석, C. 채팅 기반 구성·운영의 엔진 짝 주석), 1절 아래 "이 영역이 다루는 일(2026-09-28 리스트업 기준)" 목록(data/area_items.json)과 옛 영역에서 이어받은 경우의 계보 안내(data/area_lineage.json)만 넣고, 3~11절은 제목만 두고 "아직 작성되지 않음"으로 표시한다. status 는 seed.
분량: 3~11절의 본문 글자 수(공백 포함, 표 구분 기호·각주 정의·프런트매터 제외)를 4,000자 이내로 한다. 넘치면 주제 페이지(docs/topics/)로 분리하고 이 페이지에서는 링크한다.
갱신 규칙: 갱신 실행에서는 기존 본문 중 유지할 부분과 바꿀 부분을 정하고, 브리프에 없는 새 사실을 더하지 않는다. 조건부 승인의 수정 목록은 모두 반영한다. 변경 요약은 pages.json 의 diff_summary 와 changelog_entry 로 내고(12절 최근 업데이트는 퍼블리셔가 채운다) version 을 올린다.
절 제목: 아래 13개 H2 문자열은 사양서 5.4 문구 그대로(괄호 설명 포함)이며 pipeline/checks/protect_source.py 의 AREA_SECTIONS 와 글자 단위로 같다. 괄호까지 포함해 그대로 쓴다. 다르면 "섹션 제목·순서 불일치"로 반려된다.

[공통 규칙] 모든 템플릿에 같은 규칙이 적용된다.
1. 자리 표시: {{...}} 는 모두 실제 값으로 바꾼다. 자리 표시({{ }})가 남은 페이지는 퍼블리셔가 반려한다. 값이 없는 선택 필드는 줄 자체를 지운다.
2. 섹션 제목과 순서는 고정이다. 제목 문구를 바꾸거나, 섹션을 빼거나, 순서를 바꾸지 않는다. 채울 근거가 없는 섹션은 제목 아래에 "아직 작성되지 않음" 한 줄만 둔다. 섹션 안의 소제목(###)은 자유롭게 둘 수 있다.
3. 자동 갱신 영역: auto:<key>:start 와 auto:<key>:end 마커 사이는 퍼블리셔 스크립트가 다시 쓴다. 마커를 지우거나 옮기지 않으며, 마커 사이의 내용은 손대지 않는다(새 페이지에서는 템플릿의 안내 문구를 그대로 둔다). 마커 밖의 본문은 스크립트가 건드리지 않는다.
4. 안내 주석 처리: 이 블록을 포함한 HTML 주석과 프런트매터의 # 주석은 완성 페이지에서 지운다. auto 마커 주석만 남긴다.
5. 문체: 한국어 평서체("~이다/~한다"), 짧은 단락, 전문용어는 첫 등장 시 영문 병기, 약어는 첫 등장 시 풀어 쓴다. 마케팅 표현 금지, 근거 없는 단정 금지. 독자는 로봇·플랫폼·기획 실무자이며 전문가가 아니어도 이해할 수 있어야 한다.
6. 항목 호칭: 대분류·세부영역은 항상 번호와 이름을 함께 쓴다. 예: "17. 작업 대상·자산 식별과 인계 추적", "B. 로봇 온톨로지". "B-7", "2-1", "7번"처럼 코드·번호만으로 부르지 않는다. 표·도식·링크 텍스트 안에서도 같다.
7. 사실 표기: 주장 문장의 끝에 [사실] / [추정] / [의견] 중 하나와 각주를 함께 붙인다. 예: "GS1 EPCIS는 제품·자산의 상태·위치·이동·인계 이벤트를 공유하는 표준이다. [사실][^ref-003]". 트랙 가설은 [가설], 사용자가 experiments/ 에 넣은 실험 결과는 [사용자 실험]으로 표기하고, 둘 다 [사실]로 올리려면 내용 검증 에이전트의 판정이 필요하다. 벤더의 기능·성능 주장은 독립 출처로 확인되기 전까지 [추정]에 "벤더 주장"을 병기한다. 출처 없는 수치·사례는 쓰지 않는다. 핵심 수치는 2개 이상 출처로 교차 확인한다. 확인하지 못한 것은 지어내지 않고 "미확인"으로 남기거나 열린 질문으로 보낸다. 모든 사실에는 기준일(발행일 또는 확인일)을 남긴다. 서로 다른 출처가 충돌하면 한쪽을 고르지 않고 둘 다 제시하고 열린 질문에 올린다. "빠짐없이", "완전", "모든 기능" 같은 표현은 측정 결과(커버리지 지표)가 있을 때만 쓴다.
8. 분류 원문: _source/ROP_연구분야_분류.md 에서 가져온 문장은 한 글자도 바꾸지 않고(굵게·기울임 같은 마크다운 표기와 원문의 [1]~[10] 번호 표기 포함) 문장(또는 표) 끝에 [분류원문] 을 붙인다. 2026-09-28 개정 전 원문(보관본 _source/archive/ROP_SCM_연구분야_분류_2026-09-24.md)의 문장은 옛 영역의 정의·질문·주석을 이력으로 남길 때만 같은 방식으로 옮기고 [옛 분류원문] 을 붙인다. 두 태그 줄 모두 퍼블리셔가 해당 원문과 글자 단위로 대조한다. 원문의 대분류·세부영역 명칭·번호·정의·질문은 변경·축약·병합하지 않는다(B. 로봇 온톨로지, C. 채팅 기반 구성·운영과 그 세부영역 이름도 줄이지 않는다). 세부영역을 새로 만들거나 분류를 확장하지 않는다. 필요해 보이면 열린 질문에 "분류 확장 제안"으로만 기록한다.
9. 각주: 본문에서는 [^ref-003] 형식으로 쓴다. 각주 정의는 페이지 마지막 "참고 자료" 또는 "출처" 섹션에 "[^ref-003]: 기관, 제목, 발행일, URL, 접근일 YYYY-MM-DD" 형식으로 둔다(시드 docs/references/ref-003.md·docs/about/what-is-rop.md 와 같은 형식. 예: "[^ref-003]: GS1, EPCIS and CBV Linked Data Model, 미확인, https://ref.gs1.org/epcis/, 접근일 2026-09-24"). 발행일을 모르면 발행일 자리에 "미확인"을 쓰고, 접근일은 날짜 앞에 "접근일 "을 붙인다. 원문을 열지 못한 출처는 접근일 뒤에 " (원문 미열람)"을 붙인다. 참고문헌 id 는 ref-001 ~ ref-010 이 분류 원문 22장(참고 자료)의 1~10번에 대응한다(ref-001 ASCM SCOR Digital Standard(이전 판 분류가 업무 프로세스 범위를 잡을 때 참고한 자료), ref-002 ISA-95, ref-003 GS1 EPCIS, ref-004 Open-RMF, ref-005 Li et al. Lifelong MAPF, ref-006 Ma et al. MAPD, ref-007 NIST 협업 로봇 성능, ref-008 NIST ARIAC, ref-009 ROS 2 DDS-Security, ref-010 ROS 2 위협 모델). 새 출처는 ref-011 부터 리서치 브리프가 준 id 를 그대로 쓴다. 같은 주장에는 기존 각주를 재사용한다. 출처 원문 직접 인용은 출처당 1회, 짧은 구절만 허용하고 나머지는 요약·재서술한다. 표·그림은 복제하지 않고 필요하면 Mermaid로 직접 그린다.
10. 링크: 이 페이지의 위치 기준 상대 경로 마크다운 링크를 쓰고 .md 확장자를 포함한다. 링크 텍스트는 원문 명칭 그대로 쓴다.
11. 도식: mermaid 코드 펜스를 쓴다. 노드 id 는 영문으로, 표시 이름은 한국어 이름으로 쓴다. 도식 안에서도 번호만 쓰지 말고 이름을 쓴다.
12. 범위 경계: 분류 원문 19장을 기준으로 한다. 외부 연계 영역(수요예측·구매·재무·전사 자원 계획 / 센서 인식·SLAM·로컬 회피·파지·모터·관절 제어 / 승강기·컨베이어·PLC·설비 안전 제어 / 배차·운송계획·운임·국제물류 / 의료·식품·위험물·실외 차량·드론 등의 전문 요구사항)은 "연계 대상"으로 짧게 다루고 ROP 직접 범위처럼 서술하지 않는다.
13. 교차 규칙: L. AI·학습 기술의 AI는 매뉴얼 해석은 4. 이기종 로봇 등록과 55. 현장 조사·설치·시운전, 도면 해석은 14. 도면·BIM에서 지도 만들기, 학습 기반 배정은 25. 작업 배정 — MRTA, 장애 분석은 38. 모니터링·이상 탐지·원인 분석에 적용되는 연구 방법이다. AI 관련 내용은 L. AI·학습 기술의 해당 영역 페이지(예: 45. 문서·도면·장면 이해, 47. AI·학습·적응과 모델 운영)와 적용 대상 영역 페이지 양쪽에 연결한다. 18. 실시간 세계 상태·데이터 일관성(현재 상태를 표현)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)의 구분을 지킨다. C. 채팅 기반 구성·운영의 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다(맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번 영역). 채팅 영역을 다루면 짝이 되는 엔진 영역을 함께 연결한다.
14. 날짜는 YYYY-MM-DD(Asia/Seoul). 실행 id 는 YYYY-MM-DD-NN(예 2026-09-25-01). 열린 질문 id 는 oq-001 부터, 트랙 백로그 질문 id 는 q<단계>-<두 자리>(예 q1-01), 참고문헌 id 는 ref-NNN.
15. 현장 유형: 이 위키는 ROP를 구현하고 운영하는 데 관여하는 일 전체의 기술 지형도이며, 물류창고는 현장 유형(물류창고·제조 공장·병원·상업 시설·가정·실외·기타) 가운데 하나다. 적용 사례·예시는 현장 유형 하나를 명시하고 여섯 항목(시작 조건, 작업 대상, 수행 자원, 제약, 완료·인계, 예외·성과, 원문 21장)을 채운다. 물류 흐름(입고~반품)을 모든 영역의 기본 틀로 쓰지 않는다.

[경로 규약] 대분류 폴더와 세부영역 파일. 같은 대분류 안의 세부영역은 파일명만으로, 다른 대분류의 세부영역은 ../<대분류 slug>/<파일>로 링크한다. 홈은 ../../index.md, 열린 질문은 ../../open-questions.md, 현장 유형 매트릭스는 ../../site-matrix.md, 용어집은 ../../glossary/<slug>.md, 참고문헌은 ../../references/ref-NNN.md, 표준 목록은 ../../standards/index.md, 주제 페이지는 ../../topics/YYYY/YYYY-MM-DD-slug.md, 트랙 개요는 ../../tracks/<트랙 slug>/index.md(예: manual-capability-ontology, chat-based-configuration-and-operation, floorplan-recognition) 이다.
| 대분류 | 핵심 질문 | 폴더 (docs/categories/ 아래, index.md 가 대분류 페이지) |
|-|-|-|
| A. 기획·사업 | 어떤 일을 로봇에게 맡기고, 무엇을 들여, 어떤 효과를 볼 것인가? | planning-and-business/ |
| B. 로봇 온톨로지 | 서로 다른 제조사의 로봇을 어떻게 등록하고, 할 수 있는 일을 같은 말로 표현해, 시스템과 쉽게 연결할 것인가? | robot-ontology/ |
| C. 채팅 기반 구성·운영 | 맵 작성, 시나리오 구성, 로봇 구성, 실제 상황 재현, 업무 지시를 비전문 사용자가 대화만으로 할 수 있게 하려면? | chat-based-configuration-and-operation/ |
| D. 공간·지도 모델 | 로봇마다 다른 지도와 건물 도면을 어떻게 하나의 공간으로 만들고 유지할 것인가? | space-and-map-model/ |
| E. 사물·사람·실시간 상태 | 작업 대상·사람·설비·로봇이 지금 어디에 어떤 상태로 있는지 어떻게 믿을 수 있게 알 것인가? | objects-people-and-live-state/ |
| F. 연동 | 제조사 관제·로봇·문·승강기·업무 시스템과 어떻게 확실하게 연결할 것인가? | integration/ |
| G. 계획·최적화 | 누가, 언제, 어디로, 어떤 자원을 써서 일할 것인가? | planning-and-optimization/ |
| H. 실행·협업·예외 복구 | 계획한 일을 여러 로봇과 사람이 함께 끝까지 해내고, 어긋나면 어떻게 이어 갈 것인가? | execution-collaboration-and-recovery/ |
| I. 설계·시뮬레이션 | 현장을 바꾸거나 로봇을 늘리기 전에 가상으로 설계하고 결과를 미리 볼 수 있는가? | design-and-simulation/ |
| J. 현장 운영·관제 | 운영자가 지금 무슨 일이 일어나는지 보고, 이상을 알아차리고, 성과를 확인할 수 있는가? | field-operations-and-monitoring/ |
| K. 플랫폼 아키텍처·인프라 | 플랫폼을 어디에 어떻게 두어야 끊김·확장·다현장 조건에서도 계속 동작하는가? | platform-architecture-and-infrastructure/ |
| L. AI·학습 기술 | 학습·언어 모델 같은 AI 기술을 어디에 쓰고, 그 결과를 어떤 기준으로 믿을 것인가? | ai-and-learning/ |
| M. 안전 | 여러 로봇·사람·설비가 함께 움직일 때 생기는 위험을 어떻게 찾고 막을 것인가? | safety/ |
| N. 보안·개인정보 | 누가 어떤 로봇에 무엇을 시킬 수 있는지 통제하고, 데이터와 사람의 정보를 어떻게 지킬 것인가? | security-and-privacy/ |
| O. 검증·도입·수명주기 | 만든 것을 어떻게 검증하고, 현장에 설치해 넘기고, 오래 바꿔 가며 운영할 것인가? | verification-deployment-and-lifecycle/ |
| P. 거버넌스·법규·사회 | 여러 사업자와 법, 사회적 요구 속에서 책임과 규칙을 어떻게 정할 것인가? | governance-law-and-society/ |
| Q. 현장 유형별 적용 | 현장마다 다른 요구를 플랫폼이 어떻게 받아들이고, 실제로 어디에 어떻게 쓰이고 있는가? | site-type-applications/ |

| 번호 | 세부영역(원문 명칭) | 대분류 | 파일 (docs/categories/ 아래) |
|-|-|-|-|
| 1 | 1. 기술·시장·업체 동향 | A. 기획·사업 | planning-and-business/technology-market-and-vendor-trends.md |
| 2 | 2. 사용 사례·요구·책임 범위 | A. 기획·사업 | planning-and-business/use-cases-requirements-and-scope.md |
| 3 | 3. 경제성·조달·사업 모델 | A. 기획·사업 | planning-and-business/economics-procurement-and-business-models.md |
| 4 | 4. 이기종 로봇 등록 | B. 로봇 온톨로지 | robot-ontology/heterogeneous-robot-registration.md |
| 5 | 5. 로봇 능력·작업 표현 | B. 로봇 온톨로지 | robot-ontology/robot-capability-and-task-representation.md |
| 6 | 6. 온톨로지 기반 시스템·로봇 연동 | B. 로봇 온톨로지 | robot-ontology/ontology-based-system-and-robot-integration.md |
| 7 | 7. 온톨로지 검증·변경 관리 | B. 로봇 온톨로지 | robot-ontology/ontology-verification-and-change-management.md |
| 8 | 8. 채팅으로 맵 작성 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-map-authoring.md |
| 9 | 9. 채팅으로 시나리오 구성 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-scenario-composition.md |
| 10 | 10. 채팅으로 로봇 구성 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-robot-configuration.md |
| 11 | 11. 채팅으로 실제 상황 시뮬레이션 재현 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md |
| 12 | 12. 채팅으로 업무 지시·오케스트레이션 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md |
| 13 | 13. 대화형 기능의 신뢰·기반 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/conversational-trust-and-foundations.md |
| 14 | 14. 도면·BIM에서 지도 만들기 | D. 공간·지도 모델 | space-and-map-model/maps-from-floor-plans-and-bim.md |
| 15 | 15. 지도·공간·위치 모델 | D. 공간·지도 모델 | space-and-map-model/map-space-and-location-model.md |
| 16 | 16. 장소 의미·지도 관리 | D. 공간·지도 모델 | space-and-map-model/place-semantics-and-map-management.md |
| 17 | 17. 작업 대상·자산 식별과 인계 추적 | E. 사물·사람·실시간 상태 | objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md |
| 18 | 18. 실시간 세계 상태·데이터 일관성 | E. 사물·사람·실시간 상태 | objects-people-and-live-state/real-time-world-state-and-data-consistency.md |
| 19 | 19. 사람·보행자 모델 | E. 사물·사람·실시간 상태 | objects-people-and-live-state/people-and-pedestrian-model.md |
| 20 | 20. 로봇·제조사 관제 연동 | F. 연동 | integration/robot-and-vendor-fleet-manager-integration.md |
| 21 | 21. 상호운용 표준·적합성 | F. 연동 | integration/interoperability-standards-and-conformance.md |
| 22 | 22. 설비·건물 시스템 연동 | F. 연동 | integration/facility-and-building-system-integration.md |
| 23 | 23. 업무 시스템 연동 | F. 연동 | integration/business-system-integration.md |
| 24 | 24. 작업·워크플로 모델링 | G. 계획·최적화 | planning-and-optimization/task-and-workflow-modeling.md |
| 25 | 25. 작업 배정 — MRTA | G. 계획·최적화 | planning-and-optimization/task-allocation-mrta.md |
| 26 | 26. 작업 순서·스케줄링 | G. 계획·최적화 | planning-and-optimization/task-sequencing-and-scheduling.md |
| 27 | 27. 다중 로봇 경로·교통 관리 — MAPF | G. 계획·최적화 | planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md |
| 28 | 28. 공용 자원·충전·에너지 최적화 | G. 계획·최적화 | planning-and-optimization/shared-resource-charging-and-energy-optimization.md |
| 29 | 29. 명령·작업 실행의 신뢰성 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/command-and-task-execution-reliability.md |
| 30 | 30. 로봇 간 협업·물리적 인계 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md |
| 31 | 31. 사람–로봇 협업 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/human-robot-collaboration.md |
| 32 | 32. 예외 복구·재계획·업무 연속성 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md |
| 33 | 33. 시나리오 모델·편집 | I. 설계·시뮬레이션 | design-and-simulation/scenario-model-and-editing.md |
| 34 | 34. 시뮬레이션·예측용 디지털 트윈 | I. 설계·시뮬레이션 | design-and-simulation/simulation-and-predictive-digital-twin.md |
| 35 | 35. 처리능력·규모·배치 설계 | I. 설계·시뮬레이션 | design-and-simulation/capacity-sizing-and-layout-design.md |
| 36 | 36. 가상 시운전·실제 상황 재현 | I. 설계·시뮬레이션 | design-and-simulation/virtual-commissioning-and-real-situation-replay.md |
| 37 | 37. 관제 화면·실행 기록 | J. 현장 운영·관제 | field-operations-and-monitoring/control-screen-and-execution-records.md |
| 38 | 38. 모니터링·이상 탐지·원인 분석 | J. 현장 운영·관제 | field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md |
| 39 | 39. 운영 성과 측정·개선 | J. 현장 운영·관제 | field-operations-and-monitoring/operational-performance-measurement-and-improvement.md |
| 40 | 40. 운영 절차·요청 창구 | J. 현장 운영·관제 | field-operations-and-monitoring/operating-procedures-and-request-channels.md |
| 41 | 41. 플랫폼 아키텍처·외부 API | K. 플랫폼 아키텍처·인프라 | platform-architecture-and-infrastructure/platform-architecture-and-external-api.md |
| 42 | 42. 분산 시스템·통신·컴퓨팅 구조 | K. 플랫폼 아키텍처·인프라 | platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md |
| 43 | 43. 데이터·관측성·배포 | K. 플랫폼 아키텍처·인프라 | platform-architecture-and-infrastructure/data-observability-and-deployment.md |
| 44 | 44. 로봇 기반 모델·언어 모델 계획 | L. AI·학습 기술 | ai-and-learning/robot-foundation-models-and-llm-planning.md |
| 45 | 45. 문서·도면·장면 이해 | L. AI·학습 기술 | ai-and-learning/document-drawing-and-scene-understanding.md |
| 46 | 46. 예측·학습 기반 최적화 | L. AI·학습 기술 | ai-and-learning/prediction-and-learning-based-optimization.md |
| 47 | 47. AI·학습·적응과 모델 운영 | L. AI·학습 기술 | ai-and-learning/ai-learning-adaptation-and-model-operations.md |
| 48 | 48. 안전·위험 관리 | M. 안전 | safety/safety-and-risk-management.md |
| 49 | 49. 사람 근접 안전 | M. 안전 | safety/human-proximity-safety.md |
| 50 | 50. 안전 표준·인증·사고 조사 | M. 안전 | safety/safety-standards-certification-and-incident-investigation.md |
| 51 | 51. 인증·권한·격리 | N. 보안·개인정보 | security-and-privacy/authentication-authorization-and-isolation.md |
| 52 | 52. 통신 보호·위협 관리·감사 | N. 보안·개인정보 | security-and-privacy/communication-protection-threat-management-and-audit.md |
| 53 | 53. 개인정보·영상 데이터 | N. 보안·개인정보 | security-and-privacy/privacy-and-video-data.md |
| 54 | 54. 시험·형식 검증·벤치마크 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md |
| 55 | 55. 현장 조사·설치·시운전 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md |
| 56 | 56. 운영 이관·확대·교육 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md |
| 57 | 57. 자산·소프트웨어 수명주기 관리 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md |
| 58 | 58. 다사업자 책임·계약·데이터 | P. 거버넌스·법규·사회 | governance-law-and-society/multi-party-responsibility-contracts-and-data.md |
| 59 | 59. 법·규제·보험·라이선스 | P. 거버넌스·법규·사회 | governance-law-and-society/law-regulation-insurance-and-licensing.md |
| 60 | 60. 노동·수용성·접근성 | P. 거버넌스·법규·사회 | governance-law-and-society/labor-acceptance-and-accessibility.md |
| 61 | 61. 물류창고 | Q. 현장 유형별 적용 | site-type-applications/warehouse.md |
| 62 | 62. 제조 공장 | Q. 현장 유형별 적용 | site-type-applications/manufacturing-plant.md |
| 63 | 63. 병원·의료 | Q. 현장 유형별 적용 | site-type-applications/hospital-and-healthcare.md |
| 64 | 64. 상업 시설 | Q. 현장 유형별 적용 | site-type-applications/commercial-facilities.md |
| 65 | 65. 가정·공동주택 | Q. 현장 유형별 적용 | site-type-applications/home-and-apartment.md |
| 66 | 66. 실외 | Q. 현장 유형별 적용 | site-type-applications/outdoor.md |
| 67 | 67. 기타 현장 | Q. 현장 유형별 적용 | site-type-applications/other-sites.md |
-->
[홈](../../index.md) › [{{category}}](index.md) › {{area_no}}. {{area_name}}

# {{area_no}}. {{area_name}}

!!! info "소속 대분류"
    [{{category}}](index.md) — 핵심 질문:
    {{category_core_question}} [분류원문]
<!-- 4.8: 세부영역 페이지 상단에 소속 대분류와 핵심 질문을 노출한다. 시드 67페이지(예: docs/categories/robot-ontology/robot-capability-and-task-representation.md)·agents/storyteller.md 4.2·agents/verifier.md 11절 항목 3·부록 C 와 같은 세 줄 admonition 블록이다.
1줄: !!! info "소속 대분류"
2줄: 공백 4칸 + 대분류 링크 + " — 핵심 질문:" (콜론에서 줄이 끝난다. 콜론 뒤에 공백을 두지 않는다)
3줄: 공백 4칸 + 분류 원문 1장 표의 핵심 질문 문장 그대로(위 경로 규약의 대분류 표 참고) + " [분류원문]"
예(B. 로봇 온톨로지):
!!! info "소속 대분류"
    [B. 로봇 온톨로지](index.md) — 핵심 질문:
    서로 다른 제조사의 로봇을 어떻게 등록하고, 할 수 있는 일을 같은 말로 표현해, 시스템과 쉽게 연결할 것인가? [분류원문]
3줄은 태그를 뗀 문자열이 분류 원문 표 셀 하나와 글자 단위로 같아야 퍼블리셔 원문 보호 검사(protect_source.py 의 check_area·check_tagged_lines)를 통과한다. 링크와 핵심 질문을 한 줄에 합치면 태그 줄이 원문 셀과 달라져 반려된다. 갱신 실행에서는 입력으로 받은 시드의 이 세 줄을 들여쓰기·줄바꿈 위치까지 한 글자도 바꾸지 않고 그대로 둔다. 2차 검증(verifier.md 항목 3·부록 C)은 이 블록을 입력 시드와 줄바꿈까지 글자 단위로 대조하며, 한 줄로 합치거나 "**소속 대분류:** …" 단락으로 바꾸면 [분류원문] 훼손으로 불통과된다. -->

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->
<!-- "관련 연구 트랙" 안내. 퍼블리셔가 config/tracks/*.yaml 의 primary_area·related_areas·idea_areas 에서 만든다(연결된 트랙이 없으면 빈 영역). 시드 67페이지 모두 admonition 블록 바로 아래에 이 마커가 있다. 마커를 지우거나 옮기지 않는다. -->

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->
<!-- 페이지 상태 줄은 손으로 쓰지 않는다. 상태의 단일 원천은 프런트매터(status·confidence·version·updated·last_run)이며, 퍼블리셔가 이 마커 안에 "> 페이지 상태: … · 신뢰도: … · 페이지 버전: … · 마지막 갱신: … · 마지막 실행: …" 한 줄을 만든다. 마커 밖에 "페이지 상태:" 나 "> 상태: draft …" 같은 줄을 쓰면 check_frontmatter 가 반려한다. 시드 세부영역에는 이 마커가 없으며, 영역 심화 실행에서 area-tracks 마커 아래(1절 제목 위)에 빈 마커 두 줄을 넣는다. 새 시드를 이 템플릿으로 만들 때는 이 마커를 지운다. -->

## 1. 한 줄 정의

{{definition}} [분류원문]

{{area_items_block}}
<!--
첫 내용 줄: 분류 원문 표의 "무엇을 연구하는가" 칸 문장을 한 글자도 바꾸지 않고 옮기고 끝에 " [분류원문]" 을 붙인다. 예: "물품·자산·도구 같은 작업 대상의 식별·위치·인계 책임을 추적하고, 사람에게 넘길 때 수령인을 확인한다 [분류원문]".
이 절의 첫 내용 줄은 정의 문장 + " [분류원문]" 과 글자 단위로 같아야 한다. 태그 뒤에 각주나 다른 글자를 붙이지 않는다. 원문 주석(현재 원문)은 이 절이 아니라 2절의 인용 블록에 둔다.
{{area_items_block}}: 시드가 넣은 위키 문구를 그대로 둔다(pipeline/scaffold.py area_items_block). (1) "이 영역이 다루는 일(2026-09-28 리스트업 기준):" 과 그 아래 "- **일 이름**: 정의" 목록(data/area_items.json), (2) 옛 영역에서 일부를 이어받은 영역이면 계보 안내 문장(data/area_lineage.json), (3) 옛 영역 본문을 이어받은 영역이면 옛 영역 안내 문장과 옛 정의·질문·주석 인용 블록("> 옛 정의: … [옛 분류원문]", "> 옛 질문: … [옛 분류원문]", "> 옛 원문 주석: … [옛 분류원문]"). 옛 인용 블록은 보관한 옛 원문(_source/archive/ROP_SCM_연구분야_분류_2026-09-24.md)과 글자 단위로 같아야 하며(protect_source.py check_tagged_lines), 이력 기록이므로 에이전트가 고치거나 새 문장을 [옛 분류원문] 으로 태그하지 않는다. 해당 내용이 없는 영역은 이 자리 표시 줄을 지운다.
이 절의 원문 문장과 옛 원문 인용은 에이전트가 수정하지 않는다. 퍼블리셔(pipeline/checks/protect_source.py check_area)가 _source/ 원문과 글자 단위로 대조한다.
-->

## 2. 핵심 질문

{{core_question}} [분류원문]

> 원문 주석: {{source_note_paragraph}} [분류원문]

{{source_note_footnote_sentence}}
<!--
첫 내용 줄은 분류 원문 세부영역 표의 "핵심 질문" 칸 문장 + " [분류원문]" 과 글자 단위로 같아야 한다. 예: "로봇이 도착했을 때 실제로 무엇이 누구에게 넘겨졌는지 어떻게 확인할 것인가? [분류원문]". 수정 금지. (대분류 페이지의 핵심 질문과 다른 문장이다. 소속 대분류의 핵심 질문은 H1 아래 admonition 에 둔다.)
원문 주석: 분류 원문에서 이 세부영역을 "N번"으로 명시해 언급하는 표 아래 문단이 있는 영역은 문단마다 이 절 안에 "> 원문 주석: <문단 그대로> [분류원문]" 인용 블록 하나를 둔다. 해당 영역(2026-09-28 원문 기준): 4. 이기종 로봇 등록, 5. 로봇 능력·작업 표현, 14. 도면·BIM에서 지도 만들기, 15. 지도·공간·위치 모델, 16. 장소 의미·지도 관리, 17. 작업 대상·자산 식별과 인계 추적, 18. 실시간 세계 상태·데이터 일관성, 25. 작업 배정 — MRTA, 26. 작업 순서·스케줄링, 30. 로봇 간 협업·물리적 인계, 33. 시나리오 모델·편집, 34. 시뮬레이션·예측용 디지털 트윈, 36. 가상 시운전·실제 상황 재현, 38. 모니터링·이상 탐지·원인 분석, 55. 현장 조사·설치·시운전. 예: 17. 작업 대상·자산 식별과 인계 추적의 EPCIS 언급, 14~16번의 지도 관리 주석, 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈의 구분, L. AI·학습 기술의 교차 적용 주석("매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번"), C. 채팅 기반 구성·운영의 엔진 짝 주석("맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번").
굵게 표기와 원문의 [n] 번호를 그대로 두고, 인용 블록은 " [분류원문]" 으로 끝나야 하며 그 뒤에 각주를 붙이지 않는다. 한 문단이 여러 영역을 언급하면 각 영역 페이지에 같은 인용 블록을 둔다. 문단이 여럿인 영역(예: 14. 도면·BIM에서 지도 만들기는 셋, 15. 지도·공간·위치 모델과 25. 작업 배정 — MRTA는 둘)은 인용 블록도 원문 순서대로 그 수만큼 둔다. 원문 주석이 없는 영역은 인용 블록 줄과 각주 문장 줄을 지운다. 정확한 목록은 pipeline/lib/source.py 의 area_notes(번호)가 정한다.
각주: 원문의 [n] 에 대응하는 참고문헌 각주는 인용 블록 밖의 별도 문장에 둔다. 예: "원문의 [3]은 참고문헌 [ref-003](../../references/ref-003.md)에 해당한다.[^ref-003]". 각주 정의는 13절에 둔다. [n] 이 없는 주석이면 각주 문장 줄을 지운다.
퍼블리셔(pipeline/checks/protect_source.py check_area)가 이 절의 첫 줄과 "> 원문 주석:" 인용 블록 목록을 _source/ 원문과 글자 단위로 대조한다. 인용 블록이 1절에 있거나, "원문 주석: "으로 시작하지 않거나, 태그 뒤에 각주가 붙으면 "원문 주석 인용 불일치"로 반려된다.
-->

## 3. 왜 중요한가

{{why_it_matters}}
<!--
2~4개의 짧은 단락. 이 영역이 없으면 ROP를 구현·운영할 때 무엇이 막히는지, 로봇 개별 성능과 업무 전체 성과가 어떻게 갈리는지를 쓴다. 2절의 핵심 질문에서 출발한다. 특정 현장 유형(예: 물류창고)에만 해당하는 이야기로 좁히지 말고, 현장 유형에 따라 달라지는 점이 있으면 어느 현장 유형인지 밝힌다.
주장마다 태그와 각주를 붙인다. 근거가 브리프에 없으면 [의견]으로 쓰거나 쓰지 않는다. 사례·수치는 출처가 있을 때만 쓴다.
-->

## 4. 핵심 개념과 용어

{{key_concepts}}
<!--
형식: "- **용어(영문)** — 한 줄 설명. [태그][^ref]" 목록. 3~8개.
약어는 첫 등장 시 풀어 쓴다. 예: "VDA 5050(독일자동차산업협회 무인운반차 인터페이스)", "WMS(Warehouse Management System, 창고 관리 시스템)". 용어집에 있는 용어는 ../../glossary/<slug>.md 로 링크한다. 새 용어는 pages.json 의 glossary_updates 로도 낸다.
-->

## 5. 적용 사례 (현장 유형 명시)

**현장 유형:** {{site_types}}
<!-- 이 사례가 놓이는 현장 유형을 분류 원문 21장의 일곱 가지(물류창고 / 제조 공장 / 병원 / 상업 시설 / 가정 / 실외 / 기타) 가운데 하나로 명시한다. 예: "병원". 물류창고는 일곱 현장 유형 가운데 하나일 뿐이므로 기본값으로 쓰지 않고, 브리프 근거가 있는 현장 유형을 고른다. 물류창고 사례라면 입고 → 적치 → 보충 → 피킹 → 포장 → 출하 → 반품 중 어느 단계인지를 사례 제목이나 서술에 덧붙일 수 있다. -->

**사례:** {{case_title}}
<!-- 한 현장의 구체적 작업 하나를 제목으로 쓴다. 예: "병원에서 검체를 검사실로 운반", "제조 공장에서 공정 사이 부품 운반". -->

| 항목 | 내용 |
|---|---|
| 시작 조건 | {{trigger}} |
| 작업 대상 | {{object}} |
| 수행 자원 | {{resources}} |
| 제약 | {{constraints}} |
| 완료·인계 | {{completion_handover}} |
| 예외·성과 | {{exception_performance}} |

{{case_narrative}}
<!--
여섯 항목은 분류 원문 21장의 정의를 따른다. 시작 조건: 어떤 요청·이벤트가 작업을 발생시키는가? / 작업 대상: 어떤 물건·공간·정보·사람을 다루는가? / 수행 자원: 로봇·사람·설비 중 누가 어떤 부분을 맡는가? / 제약: 시간·공간·적재량·설비·권한·안전 제약은 무엇인가? / 완료·인계: 무엇이 확인돼야 일이 끝났다고 인정하는가? / 예외·성과: 실패하면 누가 복구하며, 처리량·시간·비용에 어떤 영향을 주는가?
표 아래에 1~3단락으로 사례를 서술한다. 이 영역이 여섯 항목 중 어디에 관여하는지가 드러나야 한다. 실제 도입 사례는 출처 각주와 함께 쓰고, 설명용 가상 사례이면 첫 문장에 밝힌다(예: "다음은 설명을 위한 가상의 사례이다."). 지어낸 현장 수치는 쓰지 않는다.
사례가 여럿이면 "**현장 유형:** … / **사례:** … / 여섯 항목 표 / 서술" 묶음을 사례마다 반복한다(서로 다른 현장 유형의 사례를 우선한다). 2026-09-28 개정 전에 쓴 물류창고 시나리오는 "현장 유형: 물류창고" 사례로 유지한다.
다룬 칸(현장 유형 × 항목)은 pages.json 의 site_matrix_updates 로 함께 낸다(항목마다 site_type·item·link·title. 대분류는 퍼블리셔가 link 에서 정한다). 현장 유형 매트릭스 페이지: ../../site-matrix.md
-->

## 6. 대표 접근법과 기술

{{approaches}}
<!--
소제목(###)별로 접근법을 2~5개 정리한다. 각 접근법: 무엇을 해결하는가, 어떻게 동작하는가, 한계는 무엇인가. 주장마다 태그·각주.
벤더 제품의 기능·성능은 [추정]에 "벤더 주장"을 병기한다. 표·그림은 복제하지 않고 필요하면 mermaid 로 직접 그린다.
-->

## 7. 관련 표준·프레임워크·오픈소스

{{standards}}
<!--
표 형식: | 이름 | 유형(표준 / 오픈소스 / 평가 프로그램 / 프레임워크) | 이 영역과의 관계 | 출처 |. 각 행의 출처 칸에 각주.
표준·규격은 발행 기관의 공식 자료를 근거로 하고, 원문을 못 열었으면 "원문 미열람"을 표기한다. 대체·개정된 표준은 현재 버전을 확인해 기준일을 쓴다. 표준 목록 페이지(../../standards/index.md)와 용어집 링크를 함께 둔다.
-->

## 8. 대표 연구와 자료

{{key_research}}
<!--
목록 형식: "- 저자 또는 기관, 제목(연도) — 한두 문장 요약과 이 영역에서의 의미. [태그][^ref]". 3~8건. 학술 논문·표준·정부·연구기관 보고서를 우선하고 기사·벤더 문서는 보조로 둔다.
-->

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| {{boundary_row}} | {{owned}} | {{external}} |

{{boundary_note}}
<!--
분류 원문 19장(ROP가 직접 소유할 범위와 외부 연계 경계)의 다섯 경계(상위 업무 시스템 / 로봇 자체 지능·제어 / 시설·설비 제어 / 현장 간 운송 / 업종별 조건) 중 이 영역에 해당하는 행만 골라 채운다(최소 1행). 이 표는 위키의 열 이름과 영역에 맞게 고쳐 쓴 셀을 섞은 합성 표이므로 행 끝에 [분류원문] 을 붙이지 않는다(원문의 줄도 셀도 아닌 문장에 태그가 붙으면 태그 줄 원문 대조에 실패한다). 원문 19장 표를 열 이름·셀까지 그대로 옮길 때만 표 아래 빈 줄 다음에 [분류원문] 한 줄을 두고, 영역에 맞게 고쳐 쓴 행·문장에는 태그를 붙이지 않고 주장에 [사실]/[추정]/[의견]과 각주를 붙인다. 원문 셀 문구를 인용할 때는 문장 안에 따옴표로 인용하고 범위 경계 페이지(../../about/scope-boundary.md)로 링크한다.
표 아래 1~2단락: 경계가 제품 전략에 따라 이동할 수 있다는 점과, 이 영역에서 이종 제조사를 연결하는 ROP가 어디까지를 인터페이스와 실행 보장으로 맡는지를 쓴다. 외부 연계 영역을 ROP 직접 범위처럼 서술하지 않는다. 범위 경계 페이지: ../../about/scope-boundary.md
-->

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

{{connections}}
<!--
목록 형식: "- [18. 실시간 세계 상태·데이터 일관성](real-time-world-state-and-data-consistency.md) — 연결 이유 한 문장"(같은 대분류 E. 사물·사람·실시간 상태 안의 예). 다른 대분류의 영역은 ../<대분류 slug>/<파일>.md 로 링크한다(경로 규약 표 참고).
반드시 번호와 이름을 함께 쓴다. 여기에 적은 번호를 프런트매터 related_areas 에 넣는다.
교차 규칙: AI를 다루면 L. AI·학습 기술의 해당 영역(예: 45. 문서·도면·장면 이해, 47. AI·학습·적응과 모델 운영)을 연결한다. 18. 실시간 세계 상태·데이터 일관성(현재 상태를 표현)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)의 구분을 지킨다. C. 채팅 기반 구성·운영의 영역이면 짝이 되는 엔진 영역(맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번)을 연결한다. 현장 유형별 요구·도입 사례는 Q. 현장 유형별 적용의 해당 영역(61. 물류창고 ~ 67. 기타 현장)을 연결한다. 트랙과 관련된 영역이면 트랙 개요(../../tracks/<트랙 slug>/index.md. 예: manual-capability-ontology, chat-based-configuration-and-operation, floorplan-recognition)도 연결한다.
-->

## 11. 열린 질문

{{open_questions}}
<!--
목록 형식: "- **oq-012** (상태: 열림 | 조사 중 | 해결 | 보류 · 제기 2026-09-25 · 실행 2026-09-25-01) 질문 문장". 해결된 질문은 답이 실린 페이지 링크를 덧붙인다.
새 질문·해결된 질문은 pages.json 의 open_question_updates 로도 낸다. 전체 목록: ../../open-questions.md
트랙 전용 질문(q1-01 형식)은 여기에 두지 않고 트랙 백로그(../../tracks/<트랙 slug>/question-backlog.md)로 링크만 둔다.
출처가 충돌한 주장, 확인하지 못한 수치, "분류 확장 제안"은 여기에 질문으로 올린다.
-->

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
퍼블리셔가 자동으로 채운다.
<!-- auto:area-recent:end -->
<!-- 퍼블리셔가 이 영역을 다룬 실행과 주제 페이지를 최신순으로 넣는다(날짜 | 실행 id | 변경 요약 | 페이지 링크). 스토리텔러는 마커 사이를 건드리지 않는다. -->

## 13. 참고 자료 (각주)

{{footnotes}}
<!--
각주 정의만 둔다. 형식: "[^ref-003]: GS1, EPCIS and CBV Linked Data Model, 미확인, https://ref.gs1.org/epcis/, 접근일 2026-09-24"(공통 규칙 9). 본문에서 쓴 각주는 모두 여기에 정의하고, 정의만 있고 본문에 없는 각주는 지운다. 프런트매터 sources 와 일치시킨다.
시드 페이지는 2절 원문 주석의 [n] 에 대응하는 각주 정의만 둔다(없으면 "아직 작성되지 않음"). 각주 정의는 이 절에만 두고 [분류원문] 이 붙은 줄에는 붙이지 않는다.
-->
```

### templates/topic.md

```markdown
---
title: "{{title}}"                          # 주제 제목. 질문형 또는 명사구. 예: "로봇 도착과 작업 대상 인계 확인은 어떻게 다른가"
type: topic
category: "{{category}}"                    # 주 연구영역이 속한 대분류 원문 명칭. 예: "E. 사물·사람·실시간 상태"
primary_area_no: {{primary_area_no}}        # 주 연구영역 번호(1~67). 반드시 하나
track: {{track_slug}}                       # 트랙 실행에서 나온 주제 페이지만. 예: manual-capability-ontology, chat-based-configuration-and-operation, floorplan-recognition. 아니면 이 줄을 뺀다
related_areas: [{{related_areas}}]          # 관련 영역 번호 0개 이상. 예: [18, 29]. 없으면 []
tags: [{{tags}}]                            # 핵심 용어 3~6개
status: {{status}}                          # draft | verified | published | needs_update | deprecated
confidence: {{confidence}}                  # high | medium | low. 내용 검증 에이전트가 부여
created: {{created}}                        # YYYY-MM-DD
updated: {{updated}}                        # YYYY-MM-DD
sources: [{{sources}}]                      # 이 페이지 각주에 쓴 참고문헌 id
last_run: {{last_run}}                      # 이 페이지를 마지막으로 다룬 실행 날짜
version: {{version}}                        # 정수. 신규 1, 갱신마다 +1
---
<!--
[템플릿] 주제 페이지 (type: topic)
경로: docs/topics/YYYY/YYYY-MM-DD-slug.md  (YYYY-MM-DD 는 생성한 실행 날짜, slug 는 영문 소문자·하이픈)
쓰임: 파이프라인 2주기부터의 주제 조사 실행, 세부영역 페이지가 4,000자를 넘어 분리한 글, 트랙 실행에서 하나의 질문을 깊게 다룬 글. 하루 신규 주제 페이지 상한은 daily_budget.new_topic_pages 를 따른다.
필수: 주 연구영역 하나(primary_area_no)와 0개 이상의 관련 영역. 트랙 실행에서 나온 페이지는 프런트매터에 track 을 넣고, 해당 트랙 단계 페이지의 3절(조사 결과)에서 이 페이지를 링크한다.
분량: 1~7절 텍스트 합계(공백 포함, 표 구분 기호·각주 정의·프런트매터 제외) 1,500~2,500자.
서사 골격: 왜 중요한가 → 현장에서 무슨 일이 벌어지는가(현장 유형을 밝힌 적용 사례) → 무엇이 알려져 있는가(검증된 사실) → ROP는 무엇을 맡고 무엇을 연계하는가 → 다른 영역과 어떻게 이어지는가 → 아직 모르는 것.
브리프의 발견 사항(finding)만 쓴다. 새 사실을 더하지 않는다. 필요한 사실이 브리프에 없으면 본문에 넣지 않고 pages.json 의 additional_research_requests 에 기록한다.

[공통 규칙] 모든 템플릿에 같은 규칙이 적용된다.
1. 자리 표시: {{...}} 는 모두 실제 값으로 바꾼다. 자리 표시({{ }})가 남은 페이지는 퍼블리셔가 반려한다. 값이 없는 선택 필드는 줄 자체를 지운다.
2. 섹션 제목과 순서는 고정이다. 제목 문구를 바꾸거나, 섹션을 빼거나, 순서를 바꾸지 않는다. 채울 근거가 없는 섹션은 제목 아래에 "아직 작성되지 않음" 한 줄만 둔다. 섹션 안의 소제목(###)은 자유롭게 둘 수 있다.
3. 자동 갱신 영역: auto:<key>:start 와 auto:<key>:end 마커 사이는 퍼블리셔 스크립트가 다시 쓴다. 마커를 지우거나 옮기지 않으며, 마커 사이의 내용은 손대지 않는다(새 페이지에서는 템플릿의 안내 문구를 그대로 둔다). 마커 밖의 본문은 스크립트가 건드리지 않는다.
4. 안내 주석 처리: 이 블록을 포함한 HTML 주석과 프런트매터의 # 주석은 완성 페이지에서 지운다. auto 마커 주석만 남긴다.
5. 문체: 한국어 평서체("~이다/~한다"), 짧은 단락, 전문용어는 첫 등장 시 영문 병기, 약어는 첫 등장 시 풀어 쓴다. 마케팅 표현 금지, 근거 없는 단정 금지. 독자는 로봇·플랫폼·기획 실무자이며 전문가가 아니어도 이해할 수 있어야 한다.
6. 항목 호칭: 대분류·세부영역은 항상 번호와 이름을 함께 쓴다. 예: "17. 작업 대상·자산 식별과 인계 추적", "B. 로봇 온톨로지". "B-7", "2-1", "7번"처럼 코드·번호만으로 부르지 않는다. 표·도식·링크 텍스트 안에서도 같다.
7. 사실 표기: 주장 문장의 끝에 [사실] / [추정] / [의견] 중 하나와 각주를 함께 붙인다. 예: "GS1 EPCIS는 제품·자산의 상태·위치·이동·인계 이벤트를 공유하는 표준이다. [사실][^ref-003]". 트랙 가설은 [가설], 사용자가 experiments/ 에 넣은 실험 결과는 [사용자 실험]으로 표기하고, 둘 다 [사실]로 올리려면 내용 검증 에이전트의 판정이 필요하다. 벤더의 기능·성능 주장은 독립 출처로 확인되기 전까지 [추정]에 "벤더 주장"을 병기한다. 출처 없는 수치·사례는 쓰지 않는다. 핵심 수치는 2개 이상 출처로 교차 확인한다. 확인하지 못한 것은 지어내지 않고 "미확인"으로 남기거나 열린 질문으로 보낸다. 모든 사실에는 기준일(발행일 또는 확인일)을 남긴다. 서로 다른 출처가 충돌하면 한쪽을 고르지 않고 둘 다 제시하고 열린 질문에 올린다. "빠짐없이", "완전", "모든 기능" 같은 표현은 측정 결과(커버리지 지표)가 있을 때만 쓴다.
8. 분류 원문: _source/ROP_연구분야_분류.md 에서 가져온 문장은 한 글자도 바꾸지 않고(굵게·기울임 같은 마크다운 표기와 원문의 [1]~[10] 번호 표기 포함) 문장(또는 표) 끝에 [분류원문] 을 붙인다. 2026-09-28 개정 전 원문(보관본 _source/archive/ROP_SCM_연구분야_분류_2026-09-24.md)의 문장은 옛 영역의 정의·질문·주석을 이력으로 남길 때만 같은 방식으로 옮기고 [옛 분류원문] 을 붙인다. 두 태그 줄 모두 퍼블리셔가 해당 원문과 글자 단위로 대조한다. 원문의 대분류·세부영역 명칭·번호·정의·질문은 변경·축약·병합하지 않는다(B. 로봇 온톨로지, C. 채팅 기반 구성·운영과 그 세부영역 이름도 줄이지 않는다). 세부영역을 새로 만들거나 분류를 확장하지 않는다. 필요해 보이면 열린 질문에 "분류 확장 제안"으로만 기록한다.
9. 각주: 본문에서는 [^ref-003] 형식으로 쓴다. 각주 정의는 페이지 마지막 "참고 자료" 또는 "출처" 섹션에 "[^ref-003]: 기관, 제목, 발행일, URL, 접근일 YYYY-MM-DD" 형식으로 둔다(시드 docs/references/ref-003.md·docs/about/what-is-rop.md 와 같은 형식. 예: "[^ref-003]: GS1, EPCIS and CBV Linked Data Model, 미확인, https://ref.gs1.org/epcis/, 접근일 2026-09-24"). 발행일을 모르면 발행일 자리에 "미확인"을 쓰고, 접근일은 날짜 앞에 "접근일 "을 붙인다. 원문을 열지 못한 출처는 접근일 뒤에 " (원문 미열람)"을 붙인다. 참고문헌 id 는 ref-001 ~ ref-010 이 분류 원문 22장(참고 자료)의 1~10번에 대응한다(ref-001 ASCM SCOR Digital Standard(이전 판 분류가 업무 프로세스 범위를 잡을 때 참고한 자료), ref-002 ISA-95, ref-003 GS1 EPCIS, ref-004 Open-RMF, ref-005 Li et al. Lifelong MAPF, ref-006 Ma et al. MAPD, ref-007 NIST 협업 로봇 성능, ref-008 NIST ARIAC, ref-009 ROS 2 DDS-Security, ref-010 ROS 2 위협 모델). 새 출처는 ref-011 부터 리서치 브리프가 준 id 를 그대로 쓴다. 같은 주장에는 기존 각주를 재사용한다. 출처 원문 직접 인용은 출처당 1회, 짧은 구절만 허용하고 나머지는 요약·재서술한다. 표·그림은 복제하지 않고 필요하면 Mermaid로 직접 그린다.
10. 링크: 이 페이지의 위치 기준 상대 경로 마크다운 링크를 쓰고 .md 확장자를 포함한다. 링크 텍스트는 원문 명칭 그대로 쓴다.
11. 도식: mermaid 코드 펜스를 쓴다. 노드 id 는 영문으로, 표시 이름은 한국어 이름으로 쓴다. 도식 안에서도 번호만 쓰지 말고 이름을 쓴다.
12. 범위 경계: 분류 원문 19장을 기준으로 한다. 외부 연계 영역(수요예측·구매·재무·전사 자원 계획 / 센서 인식·SLAM·로컬 회피·파지·모터·관절 제어 / 승강기·컨베이어·PLC·설비 안전 제어 / 배차·운송계획·운임·국제물류 / 의료·식품·위험물·실외 차량·드론 등의 전문 요구사항)은 "연계 대상"으로 짧게 다루고 ROP 직접 범위처럼 서술하지 않는다.
13. 교차 규칙: L. AI·학습 기술의 AI는 매뉴얼 해석은 4. 이기종 로봇 등록과 55. 현장 조사·설치·시운전, 도면 해석은 14. 도면·BIM에서 지도 만들기, 학습 기반 배정은 25. 작업 배정 — MRTA, 장애 분석은 38. 모니터링·이상 탐지·원인 분석에 적용되는 연구 방법이다. AI 관련 내용은 L. AI·학습 기술의 해당 영역 페이지(예: 45. 문서·도면·장면 이해, 47. AI·학습·적응과 모델 운영)와 적용 대상 영역 페이지 양쪽에 연결한다. 18. 실시간 세계 상태·데이터 일관성(현재 상태를 표현)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래를 실험)의 구분을 지킨다. C. 채팅 기반 구성·운영의 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다(맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번 영역). 채팅 영역을 다루면 짝이 되는 엔진 영역을 함께 연결한다.
14. 날짜는 YYYY-MM-DD(Asia/Seoul). 실행 id 는 YYYY-MM-DD-NN(예 2026-09-25-01). 열린 질문 id 는 oq-001 부터, 트랙 백로그 질문 id 는 q<단계>-<두 자리>(예 q1-01), 참고문헌 id 는 ref-NNN.
15. 현장 유형: 이 위키는 ROP를 구현하고 운영하는 데 관여하는 일 전체의 기술 지형도이며, 물류창고는 현장 유형(물류창고·제조 공장·병원·상업 시설·가정·실외·기타) 가운데 하나다. 적용 사례·예시는 현장 유형 하나를 명시하고 여섯 항목(시작 조건, 작업 대상, 수행 자원, 제약, 완료·인계, 예외·성과, 원문 21장)을 채운다. 물류 흐름(입고~반품)을 모든 영역의 기본 틀로 쓰지 않는다.

[경로 규약] 이 페이지에서 홈은 ../../index.md, 주제 목록은 ../index.md, 세부영역 페이지는 ../../categories/<대분류 slug>/<파일>, 대분류 페이지는 ../../categories/<대분류 slug>/index.md, 용어집은 ../../glossary/<slug>.md, 참고문헌은 ../../references/ref-NNN.md, 열린 질문은 ../../open-questions.md, 현장 유형 매트릭스는 ../../site-matrix.md, 트랙은 ../../tracks/<트랙 slug>/<파일>.md 이다.
| 대분류 | 핵심 질문 | 폴더 (docs/categories/ 아래, index.md 가 대분류 페이지) |
|-|-|-|
| A. 기획·사업 | 어떤 일을 로봇에게 맡기고, 무엇을 들여, 어떤 효과를 볼 것인가? | planning-and-business/ |
| B. 로봇 온톨로지 | 서로 다른 제조사의 로봇을 어떻게 등록하고, 할 수 있는 일을 같은 말로 표현해, 시스템과 쉽게 연결할 것인가? | robot-ontology/ |
| C. 채팅 기반 구성·운영 | 맵 작성, 시나리오 구성, 로봇 구성, 실제 상황 재현, 업무 지시를 비전문 사용자가 대화만으로 할 수 있게 하려면? | chat-based-configuration-and-operation/ |
| D. 공간·지도 모델 | 로봇마다 다른 지도와 건물 도면을 어떻게 하나의 공간으로 만들고 유지할 것인가? | space-and-map-model/ |
| E. 사물·사람·실시간 상태 | 작업 대상·사람·설비·로봇이 지금 어디에 어떤 상태로 있는지 어떻게 믿을 수 있게 알 것인가? | objects-people-and-live-state/ |
| F. 연동 | 제조사 관제·로봇·문·승강기·업무 시스템과 어떻게 확실하게 연결할 것인가? | integration/ |
| G. 계획·최적화 | 누가, 언제, 어디로, 어떤 자원을 써서 일할 것인가? | planning-and-optimization/ |
| H. 실행·협업·예외 복구 | 계획한 일을 여러 로봇과 사람이 함께 끝까지 해내고, 어긋나면 어떻게 이어 갈 것인가? | execution-collaboration-and-recovery/ |
| I. 설계·시뮬레이션 | 현장을 바꾸거나 로봇을 늘리기 전에 가상으로 설계하고 결과를 미리 볼 수 있는가? | design-and-simulation/ |
| J. 현장 운영·관제 | 운영자가 지금 무슨 일이 일어나는지 보고, 이상을 알아차리고, 성과를 확인할 수 있는가? | field-operations-and-monitoring/ |
| K. 플랫폼 아키텍처·인프라 | 플랫폼을 어디에 어떻게 두어야 끊김·확장·다현장 조건에서도 계속 동작하는가? | platform-architecture-and-infrastructure/ |
| L. AI·학습 기술 | 학습·언어 모델 같은 AI 기술을 어디에 쓰고, 그 결과를 어떤 기준으로 믿을 것인가? | ai-and-learning/ |
| M. 안전 | 여러 로봇·사람·설비가 함께 움직일 때 생기는 위험을 어떻게 찾고 막을 것인가? | safety/ |
| N. 보안·개인정보 | 누가 어떤 로봇에 무엇을 시킬 수 있는지 통제하고, 데이터와 사람의 정보를 어떻게 지킬 것인가? | security-and-privacy/ |
| O. 검증·도입·수명주기 | 만든 것을 어떻게 검증하고, 현장에 설치해 넘기고, 오래 바꿔 가며 운영할 것인가? | verification-deployment-and-lifecycle/ |
| P. 거버넌스·법규·사회 | 여러 사업자와 법, 사회적 요구 속에서 책임과 규칙을 어떻게 정할 것인가? | governance-law-and-society/ |
| Q. 현장 유형별 적용 | 현장마다 다른 요구를 플랫폼이 어떻게 받아들이고, 실제로 어디에 어떻게 쓰이고 있는가? | site-type-applications/ |

| 번호 | 세부영역(원문 명칭) | 대분류 | 파일 (docs/categories/ 아래) |
|-|-|-|-|
| 1 | 1. 기술·시장·업체 동향 | A. 기획·사업 | planning-and-business/technology-market-and-vendor-trends.md |
| 2 | 2. 사용 사례·요구·책임 범위 | A. 기획·사업 | planning-and-business/use-cases-requirements-and-scope.md |
| 3 | 3. 경제성·조달·사업 모델 | A. 기획·사업 | planning-and-business/economics-procurement-and-business-models.md |
| 4 | 4. 이기종 로봇 등록 | B. 로봇 온톨로지 | robot-ontology/heterogeneous-robot-registration.md |
| 5 | 5. 로봇 능력·작업 표현 | B. 로봇 온톨로지 | robot-ontology/robot-capability-and-task-representation.md |
| 6 | 6. 온톨로지 기반 시스템·로봇 연동 | B. 로봇 온톨로지 | robot-ontology/ontology-based-system-and-robot-integration.md |
| 7 | 7. 온톨로지 검증·변경 관리 | B. 로봇 온톨로지 | robot-ontology/ontology-verification-and-change-management.md |
| 8 | 8. 채팅으로 맵 작성 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-map-authoring.md |
| 9 | 9. 채팅으로 시나리오 구성 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-scenario-composition.md |
| 10 | 10. 채팅으로 로봇 구성 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-robot-configuration.md |
| 11 | 11. 채팅으로 실제 상황 시뮬레이션 재현 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md |
| 12 | 12. 채팅으로 업무 지시·오케스트레이션 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md |
| 13 | 13. 대화형 기능의 신뢰·기반 | C. 채팅 기반 구성·운영 | chat-based-configuration-and-operation/conversational-trust-and-foundations.md |
| 14 | 14. 도면·BIM에서 지도 만들기 | D. 공간·지도 모델 | space-and-map-model/maps-from-floor-plans-and-bim.md |
| 15 | 15. 지도·공간·위치 모델 | D. 공간·지도 모델 | space-and-map-model/map-space-and-location-model.md |
| 16 | 16. 장소 의미·지도 관리 | D. 공간·지도 모델 | space-and-map-model/place-semantics-and-map-management.md |
| 17 | 17. 작업 대상·자산 식별과 인계 추적 | E. 사물·사람·실시간 상태 | objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md |
| 18 | 18. 실시간 세계 상태·데이터 일관성 | E. 사물·사람·실시간 상태 | objects-people-and-live-state/real-time-world-state-and-data-consistency.md |
| 19 | 19. 사람·보행자 모델 | E. 사물·사람·실시간 상태 | objects-people-and-live-state/people-and-pedestrian-model.md |
| 20 | 20. 로봇·제조사 관제 연동 | F. 연동 | integration/robot-and-vendor-fleet-manager-integration.md |
| 21 | 21. 상호운용 표준·적합성 | F. 연동 | integration/interoperability-standards-and-conformance.md |
| 22 | 22. 설비·건물 시스템 연동 | F. 연동 | integration/facility-and-building-system-integration.md |
| 23 | 23. 업무 시스템 연동 | F. 연동 | integration/business-system-integration.md |
| 24 | 24. 작업·워크플로 모델링 | G. 계획·최적화 | planning-and-optimization/task-and-workflow-modeling.md |
| 25 | 25. 작업 배정 — MRTA | G. 계획·최적화 | planning-and-optimization/task-allocation-mrta.md |
| 26 | 26. 작업 순서·스케줄링 | G. 계획·최적화 | planning-and-optimization/task-sequencing-and-scheduling.md |
| 27 | 27. 다중 로봇 경로·교통 관리 — MAPF | G. 계획·최적화 | planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md |
| 28 | 28. 공용 자원·충전·에너지 최적화 | G. 계획·최적화 | planning-and-optimization/shared-resource-charging-and-energy-optimization.md |
| 29 | 29. 명령·작업 실행의 신뢰성 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/command-and-task-execution-reliability.md |
| 30 | 30. 로봇 간 협업·물리적 인계 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md |
| 31 | 31. 사람–로봇 협업 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/human-robot-collaboration.md |
| 32 | 32. 예외 복구·재계획·업무 연속성 | H. 실행·협업·예외 복구 | execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md |
| 33 | 33. 시나리오 모델·편집 | I. 설계·시뮬레이션 | design-and-simulation/scenario-model-and-editing.md |
| 34 | 34. 시뮬레이션·예측용 디지털 트윈 | I. 설계·시뮬레이션 | design-and-simulation/simulation-and-predictive-digital-twin.md |
| 35 | 35. 처리능력·규모·배치 설계 | I. 설계·시뮬레이션 | design-and-simulation/capacity-sizing-and-layout-design.md |
| 36 | 36. 가상 시운전·실제 상황 재현 | I. 설계·시뮬레이션 | design-and-simulation/virtual-commissioning-and-real-situation-replay.md |
| 37 | 37. 관제 화면·실행 기록 | J. 현장 운영·관제 | field-operations-and-monitoring/control-screen-and-execution-records.md |
| 38 | 38. 모니터링·이상 탐지·원인 분석 | J. 현장 운영·관제 | field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md |
| 39 | 39. 운영 성과 측정·개선 | J. 현장 운영·관제 | field-operations-and-monitoring/operational-performance-measurement-and-improvement.md |
| 40 | 40. 운영 절차·요청 창구 | J. 현장 운영·관제 | field-operations-and-monitoring/operating-procedures-and-request-channels.md |
| 41 | 41. 플랫폼 아키텍처·외부 API | K. 플랫폼 아키텍처·인프라 | platform-architecture-and-infrastructure/platform-architecture-and-external-api.md |
| 42 | 42. 분산 시스템·통신·컴퓨팅 구조 | K. 플랫폼 아키텍처·인프라 | platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md |
| 43 | 43. 데이터·관측성·배포 | K. 플랫폼 아키텍처·인프라 | platform-architecture-and-infrastructure/data-observability-and-deployment.md |
| 44 | 44. 로봇 기반 모델·언어 모델 계획 | L. AI·학습 기술 | ai-and-learning/robot-foundation-models-and-llm-planning.md |
| 45 | 45. 문서·도면·장면 이해 | L. AI·학습 기술 | ai-and-learning/document-drawing-and-scene-understanding.md |
| 46 | 46. 예측·학습 기반 최적화 | L. AI·학습 기술 | ai-and-learning/prediction-and-learning-based-optimization.md |
| 47 | 47. AI·학습·적응과 모델 운영 | L. AI·학습 기술 | ai-and-learning/ai-learning-adaptation-and-model-operations.md |
| 48 | 48. 안전·위험 관리 | M. 안전 | safety/safety-and-risk-management.md |
| 49 | 49. 사람 근접 안전 | M. 안전 | safety/human-proximity-safety.md |
| 50 | 50. 안전 표준·인증·사고 조사 | M. 안전 | safety/safety-standards-certification-and-incident-investigation.md |
| 51 | 51. 인증·권한·격리 | N. 보안·개인정보 | security-and-privacy/authentication-authorization-and-isolation.md |
| 52 | 52. 통신 보호·위협 관리·감사 | N. 보안·개인정보 | security-and-privacy/communication-protection-threat-management-and-audit.md |
| 53 | 53. 개인정보·영상 데이터 | N. 보안·개인정보 | security-and-privacy/privacy-and-video-data.md |
| 54 | 54. 시험·형식 검증·벤치마크 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md |
| 55 | 55. 현장 조사·설치·시운전 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md |
| 56 | 56. 운영 이관·확대·교육 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md |
| 57 | 57. 자산·소프트웨어 수명주기 관리 | O. 검증·도입·수명주기 | verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md |
| 58 | 58. 다사업자 책임·계약·데이터 | P. 거버넌스·법규·사회 | governance-law-and-society/multi-party-responsibility-contracts-and-data.md |
| 59 | 59. 법·규제·보험·라이선스 | P. 거버넌스·법규·사회 | governance-law-and-society/law-regulation-insurance-and-licensing.md |
| 60 | 60. 노동·수용성·접근성 | P. 거버넌스·법규·사회 | governance-law-and-society/labor-acceptance-and-accessibility.md |
| 61 | 61. 물류창고 | Q. 현장 유형별 적용 | site-type-applications/warehouse.md |
| 62 | 62. 제조 공장 | Q. 현장 유형별 적용 | site-type-applications/manufacturing-plant.md |
| 63 | 63. 병원·의료 | Q. 현장 유형별 적용 | site-type-applications/hospital-and-healthcare.md |
| 64 | 64. 상업 시설 | Q. 현장 유형별 적용 | site-type-applications/commercial-facilities.md |
| 65 | 65. 가정·공동주택 | Q. 현장 유형별 적용 | site-type-applications/home-and-apartment.md |
| 66 | 66. 실외 | Q. 현장 유형별 적용 | site-type-applications/outdoor.md |
| 67 | 67. 기타 현장 | Q. 현장 유형별 적용 | site-type-applications/other-sites.md |
-->
[홈](../../index.md) › [주제](../index.md) › {{title}}

# {{title}}

**주 연구영역:** [{{primary_area_no}}. {{primary_area_name}}](../../categories/{{category_slug}}/{{area_file}}.md) · **관련 영역:** {{related_area_links_or_없음}} · **실행:** {{run_id}}
<!-- 관련 영역 링크는 "[18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md)" 형식으로 쉼표 구분. 트랙 페이지면 "· **트랙:** [트랙 이름](../../tracks/<트랙 slug>/index.md) 단계 n" 을 덧붙인다(예: [매뉴얼 기반 로봇 기능 온톨로지](../../tracks/manual-capability-ontology/index.md), [채팅 기반 구성·운영](../../tracks/chat-based-configuration-and-operation/index.md)). -->

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->
<!-- 페이지 상태 줄은 손으로 쓰지 않는다. 상태의 단일 원천은 프런트매터이며, 퍼블리셔가 이 마커 안에 "> 페이지 상태: … · 신뢰도: … · 페이지 버전: … · 마지막 갱신: … · 마지막 실행: …" 한 줄을 만든다. 마커 밖에 "페이지 상태:" 나 "> 상태: draft …" 같은 줄을 쓰면 check_frontmatter 가 반려한다. 새 페이지에는 빈 마커 두 줄만 둔다. -->

## 1. 세 줄 요약

- {{summary_line_1}}
- {{summary_line_2}}
- {{summary_line_3}}
<!-- 정확히 세 줄. 각 줄은 한 문장. 첫 줄은 무엇을 밝혔는가, 둘째 줄은 ROP 운영에 무엇을 뜻하는가, 셋째 줄은 무엇이 아직 확인되지 않았는가. 요약에도 핵심 주장에는 태그를 붙인다. -->

## 2. 배경

{{background}}
<!--
어느 연구영역의 어떤 질문에서 출발했는지 쓴다. 주 연구영역의 원문 "핵심 질문"을 인용하면 그대로 옮기고 [분류원문] 을 붙인다. 출발점이 열린 질문(oq-NNN)이나 트랙 백로그 질문(q1-01), 정정 요청, priority.yaml 의 우선 주제이면 그 id 와 링크를 적는다. 1~2단락.
-->

## 3. 본문

### {{subheading_1}}

{{body_1}}

### {{subheading_2}}

{{body_2}}
<!--
소제목은 자유(2~5개). 주장마다 태그·각주. 검증된 발견 사항만 쓰고 순서는 서사 골격을 따른다. 출처가 충돌하면 둘 다 제시하고 7절 열린 질문에 올린다.
표·그림 복제 금지. 도식이 필요하면 mermaid 로 그리고 도식 안에서도 이름을 쓴다. 벤더 주장은 [추정]에 "벤더 주장" 병기. 조건부 승인의 수정 목록을 모두 반영하고 pages.json 의 fixes_applied 에 표시한다.
-->

## 4. 현장 시나리오

**현장 유형:** {{site_types}}

**사례:** {{case_title}}

| 항목 | 내용 |
|---|---|
| 시작 조건 | {{trigger}} |
| 작업 대상 | {{object}} |
| 수행 자원 | {{resources}} |
| 제약 | {{constraints}} |
| 완료·인계 | {{completion_handover}} |
| 예외·성과 | {{exception_performance}} |

{{case_narrative}}
<!--
절 제목 "4. 현장 시나리오"는 파이프라인(pipeline/lib/validate.py)이 쓰는 고정 문자열이므로 바꾸지 않는다. 내용은 분류 원문 21장의 방법대로 쓴다: 현장 유형(물류창고 / 제조 공장 / 병원 / 상업 시설 / 가정 / 실외 / 기타) 하나를 명시하고, 여섯 항목(시작 조건: 어떤 요청·이벤트가 작업을 발생시키는가 / 작업 대상: 어떤 물건·공간·정보·사람을 다루는가 / 수행 자원 / 제약 / 완료·인계 / 예외·성과)을 채운다. 물류창고는 일곱 현장 유형 가운데 하나이므로 기본값으로 쓰지 않는다. 이 주제와 직접 관련 없는 항목은 "해당 없음"으로 둔다. 실제 사례는 출처 각주와 함께, 설명용 가상 사례이면 첫 문장에 밝히고 지어낸 수치는 쓰지 않는다. 다룬 칸(현장 유형 × 항목)은 pages.json 의 site_matrix_updates 로 낸다.
-->

## 5. ROP 관점의 시사점

**직접 범위:**
{{direct_scope_implications}}

**연계 범위:**
{{external_scope_implications}}
<!-- 분류 원문 19장(ROP가 직접 소유할 범위와 외부 연계 경계)의 경계를 기준으로 ROP가 직접 맡는 것과 외부와 연계하는 것을 나누어 쓴다. 각 항목은 목록으로, 주장마다 태그·각주. 외부 연계 영역을 ROP 직접 범위처럼 쓰지 않는다. -->

## 6. 연결되는 연구영역

{{connected_areas}}
<!-- 목록 형식: "- [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) — 연결 이유 한 문장". 주 연구영역을 첫 줄에, 관련 영역을 그 아래에. 번호와 이름을 함께 쓴다. 여기 적은 번호는 프런트매터 primary_area_no·related_areas 와 일치시킨다. AI를 다루면 27. AI·학습·적응과 모델 운영을 함께 연결한다. -->

## 7. 열린 질문

{{open_questions}}
<!-- 목록 형식: "- **oq-012** (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-01) 질문 문장". 이 글에서 새로 생긴 질문과 답한(해결한) 질문을 나누어 적고, 해결한 질문에는 답이 있는 절을 표시한다. 트랙 질문(q1-01)은 트랙 백로그 링크만 둔다. pages.json 의 open_question_updates 로도 낸다. 없으면 "없음"과 이유. -->

## 8. 출처

{{footnotes}}
<!-- 각주 정의만 둔다. 형식: "[^ref-003]: 기관, 제목, 발행일, URL, 접근일 YYYY-MM-DD". 본문의 각주와 프런트매터 sources 를 일치시킨다. 새 출처는 pages.json 의 reference_updates 로도 낸다. -->

## 9. 검증 노트

- 판정: 1차 {{first_verdict}} / 2차 {{second_verdict}}
- 확인·미확인: 확인 {{confirmed_count}}건 · 미확인 {{unconfirmed_count}}건 · 교차 확인 {{cross_checked_count}}건
- 강등된 주장: {{downgraded_claims_or_없음}}
- 검증자 주의: {{verification_note}}
- 신뢰도: {{confidence}}
<!-- 내용 검증 에이전트의 verification.json 에서 옮긴다. 판정 값: 1차 = 승인 | 조건부 승인 | 반려, 2차 = 통과 | 수정 후 재검증 | 불통과. 강등된 주장은 finding id 와 "사실 → 추정" 같은 변경을 적는다. "검증자 주의"는 verification_note 문구를 그대로 쓴다. 스토리텔러는 여기에 자기 의견을 넣지 않는다. -->

## 10. 이력

| 날짜 | 실행 id | 변경 | 버전 |
|---|---|---|---|
| {{date}} | {{run_id}} | {{change_summary}} | {{version}} |
<!-- 신규 작성은 "신규 작성". 갱신마다 한 행을 위에 추가하고 프런트매터 version 을 올린다. 정정 요청을 반영했으면 corr-NNN id 를 적는다. -->
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

### docs/standards/index.md (요약: 361개 — 이름 · 종류 · 발행 기관)

```markdown
- SCOR (SCOR Digital Standard) · 표준 · ASCM(Association for Supply Chain Management)
- ISA-95 (ANSI/ISA-95) · 표준 · ISA(International Society of Automation)
- GS1 EPCIS · 표준 · GS1
- Open-RMF · 오픈소스 · Open Robotics
- ROS 2 DDS-Security (ROS 2 DDS-Security Integration) · 프레임워크 · ROS 2 Design
- ROS 2 위협 모델 (ROS 2 Robotic Systems Threat Model) · 프레임워크 · ROS 2 Design
- NIST 협업 로봇 성능 (Performance of Collaborative Robot Systems) · 평가 프로그램 · NIST(National Institute of Standards and Technology)
- ARIAC · 평가 프로그램 · NIST
- GS1 EPCIS 2.0 (ISO/IEC 19987:2024) · ISO/IEC · GS1 · 표준
- GS1 CBV (Core Business Vocabulary) · GS1 · 표준
- SSCC (Serial Shipping Container Code) · GS1 · 표준
- GS1 Logistic Label Guideline · GS1 · 표준
- GRAI (Global Returnable Asset Identifier) · GS1 · 표준
- GIAI (Global Individual Asset Identifier) · GS1 · 표준
- EPC Tag Data Standard (1.11판) · GS1 · 표준
- VDA 5050 (2.0.0) · VDA(Verband der Automobilindustrie) · 표준
- OpenEPCIS · OpenEPCIS · 오픈소스
- IEEE 1872-2015 Standard Ontologies for Robotics and Automation (CORA) · IEEE · 표준
- IEEE 1872.2-2021 Standard for Autonomous Robotics (AuR) Ontology · IEEE · 표준
- W3C/OGC Semantic Sensor Network Ontology (SSN/SOSA) · W3C / OGC · 표준
- VDA 5050 (3.0.0) · VDA(Verband der Automobilindustrie) · 표준
- MassRobotics AMR Interoperability Standard (1.0) · MassRobotics · 표준
- OPC UA for Robotics Part 1: Vertical Integration (OPC 40010-1) · OPC Foundation / VDMA · 표준
- Information Model for Capabilities, Skills & Services (CSS) · Plattform Industrie 4.0 · 프레임워크
- Oliot EPCIS (GS1 EPCIS/CBV 2.0 오픈소스 구현) · Auto-ID Labs Korea(세종대학교) · 오픈소스
- RAWSim-O · Merschformann, M. (RAWSim-O GitHub) · 오픈소스
- 스마트물류센터 인증제 · 한국교통연구원(인증스마트물류센터) · 평가 프로그램
- BPMN 2.0 (ISO/IEC 19510:2013) · OMG(Object Management Group) · ISO/IEC · 표준
- IEC 62264-3:2016 (ISA-95 Part 3) 제조 운영 관리 활동 모델 · IEC / ISO · 표준
- B2MML (Business To Manufacturing Markup Language, 판 0701) · MESA International · 표준
- OCEL 2.0 (Object-Centric Event Log) · arXiv:2403.01975 저자(미확인) · 표준
- ISO 22400-2:2014 제조 운영 관리 KPI 정의 · ISO · 표준
- WERC DC Measures · WERC(Warehousing Education and Research Council) · 평가 프로그램
- PM4Py · Process Intelligence Solutions · 오픈소스
- OPC UA for ISA-95 Part 4: Job Control (OPC 10031-4, 노드셋 2.0.0) · OPC Foundation / ISA · 표준
- osmAG-from-cad (CAD-to-osmAG 파이프라인) · Zhang, J. (jiajiezhang7 GitHub) · 오픈소스
- Ogm2Pgbm · Vega-Torres, M. A. (MigVega GitHub) · 오픈소스
- ifc2indoorgml · Diakité, A. A. 외 · 오픈소스
- IDTA 02020 Capability Description 1.0 · IDTA(Industrial Digital Twin Association) · 표준
- IDTA 02047 Technical Data for Automated Guided Vehicles 1.0 · IDTA(Industrial Digital Twin Association) · 표준
- CaSkMan · CaSkade-Automation (GitHub) · 오픈소스
- SOMA (Socio-physical Model of Activities) · EASE CRC · 오픈소스
- IEEE 1872.2 AuR 온톨로지 OWL 구현(IndustrialStandard-ODP-IEEE1872-2) · Helmut Schmidt University, Institute of Automation Technology · 오픈소스
- ISO 22166-201:2024 서비스 로봇 모듈 공통 정보 모델 · ISO · 표준
- KS B 7321-2 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델 · 국가표준인증통합정보시스템(KSSN) · 표준
- VDMA LIF (Layout Interchange Format) · VDMA · 표준
- IFC 4.3 (Industry Foundation Classes, 개발 저장소 ifc4.3-main) · buildingSMART · 표준
- Nav2 Docking Framework (nav2_docking) · ROS Navigation (Open Navigation) · 오픈소스
- IDTA 02020 Capability Description (AAS 서브모델 1.0) · IDTA(Industrial Digital Twin Association) · 표준
- IDTA 02047 Technical Data for Automated Guided Vehicles (1.0) · IDTA(Industrial Digital Twin Association) · 표준
- AAS Part 3a: Data Specification – IEC 61360 (IDTA-01003-a 3.0.2) · IDTA(Industrial Digital Twin Association) · 표준
- ISO 22166-202:2025 서비스 로봇 소프트웨어 모듈 정보 모델 · ISO · 표준
- KS B 7321-2 로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델 · 국가표준인증통합정보시스템(KSSN) · 표준
- SkiROS2 · RVMI lab, Aalborg University · 오픈소스
- LIF (Layout Interchange Format) 1.0.0 · VDMA · 표준
- ISO 21423 Industrial mobile robots — Communications and interoperability · ISO · 표준
- IFC 4.3 (IfcSpace) · buildingSMART International · 표준
- OGC IndoorGML 2.0 · OGC · 표준
- ISO 19164:2024 Indoor feature model · ISO · 표준
- GS1 GLN (Global Location Number) · GS1 · 표준
- REP 105 Coordinate Frames for Mobile Platforms · ROS (ros-infrastructure/rep) · 프레임워크
- ROSA (ROS Agent) · NASA Jet Propulsion Laboratory · 오픈소스
- RAI · Robotec.ai · 오픈소스
- free_fleet (Open-RMF 플릿 어댑터) · Open Robotics (open-rmf) · 오픈소스
- ros_amr_interop (VDA5050 커넥터·MassRobotics 송신 노드) · InOrbit · 오픈소스
- Open-RMF fleet_adapter_template · Open Robotics (open-rmf) · 오픈소스
- SLAM Toolbox · Macenski, S. (SteveMacenski GitHub) · 오픈소스
- ROS 2 QoS 정책 (Deadline·Lifespan·Liveliness, Jazzy 문서) · Open Robotics (ROS 2 Documentation) · 오픈소스
- Eclipse Sparkplug (Chapter 5 Operational Behavior) · Eclipse Foundation · 표준
- OPC UA Part 4: Services (7.11 DataValue) · OPC Foundation · 표준
- ISO 23247 제조 디지털 트윈 프레임워크 · ISO (NIST 해설 경유) · 표준
- ROS 2 설계 문서 — ROS on DDS · QoS 정책 · ROS 2 Design · 프레임워크
- rmw_zenoh (Zenoh 기반 ROS 2 미들웨어) · ROS 2 (ros2/rmw_zenoh) · 오픈소스
- KubeEdge · KubeEdge (CNCF) · 오픈소스
- Open-RMF rmf-web (대시보드·API 서버) · Open Robotics (open-rmf) · 오픈소스
- MQTT Version 5.0 · OASIS · 표준
- NIST SP 500-325 Fog Computing Conceptual Model · NIST · 프레임워크
- KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법 · 산업통상자원부 국가기술표준원 · 표준
- Open-RMF 승강기·문 메시지(rmf_internal_msgs의 rmf_lift_msgs·rmf_door_msgs) · Open Robotics (open-rmf) · 오픈소스
- KnowRob (하이브리드 지식 베이스) · KnowRob (knowrob GitHub) · 오픈소스
- IEEE1872-owl (CORA 공개 OWL 번역, 제3자) · srfiorini (IEEE1872-owl GitHub) · 오픈소스
- CityGML 3.0 Part 1: Conceptual Model (OGC 20-010) · OGC · 표준
- IMDF (Indoor Mapping Data Format) 1.0.0 · OGC / Apple · 표준
- BOT (Building Topology Ontology) 0.3.2 · W3C Linked Building Data Community Group · 프레임워크
- ifcOWL · buildingSMART · 표준
- Brick Schema · Brick Consortium · 오픈소스
- ISO 16739-1:2024 (IFC 4.3) · ISO · 표준
- Rasa 폼(Forms, Rasa 3.x) · Rasa Technologies · 오픈소스
- ROS 2 액션 설계(Actions) · ROS 2 Design · 프레임워크
- ROS 2 관리형 노드 수명주기(Managed nodes) · ROS 2 Design · 프레임워크
- Open-RMF rmf_task · Open Robotics (open-rmf) · 오픈소스
- IETF Idempotency-Key HTTP 헤더 초안(draft-ietf-httpapi-idempotency-key-header) · IETF HTTPAPI Working Group · 표준
- OPC UA Part 10: Programs (v1.04) · OPC Foundation · 표준
- ISA-TR88.00.02 Machine and Unit States (PackML) · ISA · 표준
- BehaviorTree.CPP · BehaviorTree (GitHub) · 오픈소스
- OR-Tools CP-SAT (스케줄링 레시피) · Google · 오픈소스
- Open-RMF rmf_task (TaskPlanner·BinaryPriorityScheme) · Open Robotics (open-rmf) · 오픈소스
- rmf_task (Open-RMF 작업 계획기 TaskPlanner) · Open Robotics (open-rmf) · 오픈소스
- ISO 13567-1:2017 CAD 레이어 구성·명명 — Part 1: 개요와 원칙 · ISO · 표준
- 미국 국가 CAD 표준(NCS) AIA CAD 레이어 이름 형식(V5, V6 판 있음) · National Institute of Building Sciences · 표준
- KS F 1542 CAD 도면 작성을 위한 레이어 원칙과 기준 · 국가표준인증통합정보시스템(KSSN) · 표준
- 건설CALS/EC 전자도면 작성표준(V1.1, KCCS-0001-2006) · 한국건설기술연구원(건설CALS 체계) · 표준
- ezdxf (DXF 읽기·쓰기 라이브러리) · Moitzi, M. (mozman/ezdxf GitHub) · 오픈소스
- ECLASS (제품·서비스 분류·속성 사전, Release 15.0·16.0) · ECLASS e.V. · 표준
- IEC 공통 데이터 사전(IEC CDD) · IEC · 표준
- rmf_traffic (Open-RMF 교통 스케줄링·협상 패키지) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF Traffic Editor · Open Robotics · 오픈소스
- MAPF-LRR2023 (League of Robot Runners 2023 팀 해법 WPPL) · DiligentPanda (Team Pikachu, GitHub) · 오픈소스
- SEMI E84 Enhanced Carrier Handoff Parallel I/O Interface · SEMI · 표준
- ASTM F3499-21 A-UGV 도킹 성능 시험 방법 · ASTM International · 표준
- ANSI/A3 R15.08-2-2023 Industrial Mobile Robots — Safety Requirements — Part 2 · ANSI / A3 · 표준
- KS B ISO 10218-2 산업용 로봇의 안전 — 제2부: 로봇 시스템 및 통합 · 국가표준인증통합정보시스템(KSSN) · 표준
- Open-RMF 디스펜서·인제스터 메시지(rmf_internal_msgs의 rmf_dispenser_msgs) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF rmf_traffic (교통 그래프·뮤텍스 그룹) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF rmf_reservation (실험적 예약 라이브러리) · Open Robotics (open-rmf) · 오픈소스
- ISO 3691-4:2023 무인 산업용 트럭과 그 시스템의 안전 요구·검증 · ISO · 표준
- ISO 10218-1·10218-2:2025 산업용 로봇 안전(협동 적용 통합) · ISO (A3 해설 경유) · 표준
- ANSI/A3 R15.08-2 산업용 이동로봇 시스템·적용 안전 표준 · A3(Association for Advancing Automation) · 표준
- 고정식·이동식 산업용 로봇의 협동작업 안전 가이드 · 고용노동부·한국산업안전보건공단 · 프레임워크
- 이동식 협동로봇 안전기준 KS(표준 번호 미확인) · 중소벤처기업부 발표(대구 이동식 협동로봇 규제자유특구) · 표준
- Open-RMF rmf_demos · Open Robotics (open-rmf) · 오픈소스
- IEC 61360-7:2024 교차 도메인 개념 데이터 사전(General items) · IEC · 표준
- IDTA 02003 Generic Frame for Technical Data for Industrial Equipment in Manufacturing (1.2) · IDTA(Industrial Digital Twin Association) · 표준
- Nav2 map_server (ROS 2 지도 서버, 점유 격자 지도 YAML 형식) · ROS Navigation (ros-navigation/navigation2) · 오픈소스
- ROS 2 diagnostics · ROS (ros/diagnostics GitHub) · 오픈소스
- ros2_tracing · ROS 2 (ros2/ros2_tracing GitHub) · 오픈소스
- OpenTelemetry Specification · OpenTelemetry (CNCF) · 오픈소스
- Open-RMF 작업 상태 스키마(rmf_api_msgs task_state) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF 경보 메시지(rmf_task_msgs Alert) · Open Robotics (open-rmf) · 오픈소스
- IFCtoLBD (IFC → 링크드 빌딩 데이터 변환기, 판 2.54.0) · Oraskari, J. (jyrkioraskari GitHub) · 오픈소스
- SHACL (Shapes Constraint Language) · W3C · 표준
- IDS (Information Delivery Specification) · buildingSMART · 표준
- RMF Site Editor (rmf_site) · Open Robotics (open-rmf) · 오픈소스
- ISO 22301:2019 업무 연속성 관리 시스템 요구사항(개정 1:2024 별도) · ISO · 표준
- 기업재난관리표준·재해경감 우수기업 인증제 · 행정안전부 · 평가 프로그램
- 중소규모 사업장 기능연속성계획(BCP) 수립 가이드(2022) · 고용노동부 · 프레임워크
- 보상 트랜잭션 패턴(Compensating Transaction pattern) · Microsoft (Azure Architecture Center) · 프레임워크
- Open-RMF rmf_ros2 플릿 어댑터(RobotUpdateHandle) · Open Robotics (open-rmf) · 오픈소스
- IEEE 1872.1-2024 Standard for Robot Task Representation · IEEE Standards Association · 표준
- Serverless Workflow (Open Workflow Specification) DSL · CNCF Serverless Workflow · 오픈소스
- HDDL (Hierarchical Domain Definition Language) · Höller 외(IPC 2020 계층 계획 부문) · 프레임워크
- FaMe (BPMN 기반 다중 로봇 시스템 개발 틀) · Pettinari, S. (UNICAM PROS) · 오픈소스
- ISO 20607:2019 기계 안전 — 설명서 일반 작성 원칙 · ISO · 표준
- IEC/IEEE 82079-1:2019 제품 사용 정보 작성 — Part 1: 원칙과 일반 요구사항 · IEC / IEEE / ISO · 표준
- OmniDocBench (PDF 문서 파싱 벤치마크) · OpenDataLab · 오픈소스
- ISO 23247-6:2026 제조 디지털 트윈 프레임워크 — 제6부: 디지털 트윈 결합 · ISO · 표준
- KS X ISO 23247 제조를 위한 디지털 트윈 프레임워크(제1부 개요 및 일반 원리 등) · 국가표준인증종합정보센터(KSSN) · 표준
- Open-RMF rmf_simulation (시뮬레이션 플러그인) · Open Robotics (open-rmf) · 오픈소스
- OFacT (Open Factory Twin) · OpenFactoryTwin (Fraunhofer ISST, HSBI, FH Dortmund) · 오픈소스
- League of Robot Runners · League of Robot Runners (Amazon Robotics 후원) · 평가 프로그램
- ASTM F45 위원회(무인 자동 유도 산업 차량) · ASTM International (NIST 참여) · 표준
- KS B ISO 18646-1 서비스 로봇 성능 기준 및 시험방법 — 제1부: 바퀴형 로봇의 이동능력 · 국가표준인증종합정보센터(KSSN) · 표준
- 한국로봇산업진흥원 로봇 시험평가 · 한국로봇산업진흥원(KIRIA) · 평가 프로그램
- ros2_fault_injection · reeceholland (GitHub) · 오픈소스
- ROSMonitoring · University of Liverpool Autonomy and Verification · 오픈소스
- LSMART (Lifelong Scalable Multi-Agent Realistic Testbed) · Yan, J. 외(arXiv 2602.15721) · 오픈소스
- IDTA 02007 Nameplate for Software in Manufacturing (Software Nameplate 1.0) · IDTA(Industrial Digital Twin Association) · 표준
- ISO 17359:2018 기계 상태 감시·진단 일반 지침 · ISO · 표준
- ISO 55000:2024 자산 관리 — 용어·개요·원칙 · ISO (ISO/TC 251) · 표준
- IEC TR 62443-2-3:2015 IACS 환경의 패치 관리 · IEC · 표준
- REP 2000 ROS 2 Releases and Target Platforms · Open Robotics (ROS REP) · 프레임워크
- rmf_simulation (Open-RMF 시뮬레이션 플러그인) · Open Robotics (open-rmf) · 오픈소스
- 협동로봇 설치 작업장 안전인증 · 한국로봇사용자협회 · 평가 프로그램
- ISO 12100:2010 기계 안전 — 설계 일반 원칙 — 위험성평가와 위험 감소 · ISO (CEN EN ISO 12100:2010) · 표준
- KS B ISO/TS 15066 로봇 및 로봇 장치 — 협동로봇 · 국가기술표준원(KSSN) · 표준
- Nav2 Route Server (nav2_route) · ROS Navigation (ros-navigation/navigation2) · 오픈소스
- NIST SP 800-82 Rev. 3 Guide to Operational Technology (OT) Security · NIST · 프레임워크
- Eclipse Mosquitto (MQTT 브로커, mosquitto.conf ACL·인증서 인증) · Eclipse Foundation · 오픈소스
- SROS 2 접근 제어 정책(ROS 2 Access Control Policies) · ROS 2 Design · 프레임워크
- ROS 2 보안 인클레이브(ROS 2 Security Enclaves) · ROS 2 Design · 프레임워크
- KISA 로봇 보안취약점 점검 체크리스트 해설서 · 한국인터넷진흥원(KISA) · 프레임워크
- NIST AI RMF 1.0 (NIST AI 100-1) · NIST · 프레임워크
- ISO/IEC 42001:2023 AI 관리 시스템 · ISO/IEC · 표준
- ISO/IEC 23894:2023 AI 위험관리 지침 · ISO/IEC · 표준
- MLflow 모델 레지스트리 · MLflow (Linux Foundation 오픈소스 프로젝트) · 오픈소스
- LoTa-Bench · lbaa2022 (LoTa-Bench 공식 저장소) · 오픈소스
- AmbiK 데이터셋 · cog-model (AmbiK 저자) · 오픈소스
- SISO CMSD (Core Manufacturing Simulation Data, SISO-STD-008-2010·SISO-STD-008-01-2012) · SISO(Simulation Interoperability Standards Organization) · 표준
- SLAPStack (블록 적재 창고 저장 위치 배정 시뮬레이션) · Rinciog, A. 외 (malerinc/slapstack GitHub) · 오픈소스
- Semantic Versioning 2.0.0 · Semantic Versioning (semver.org) · 프레임워크
- IETF RFC 9745 The Deprecation HTTP Response Header Field · IETF · 표준
- IEC 62443-3-3:2013 시스템 보안 요구사항과 보안 수준 · IEC · 표준
- ISO/IEC 20000-1:2018 서비스 관리 시스템 요구사항 · ISO/IEC · 표준
- KOROS 1148-8:2025 서비스 로봇을 위한 모듈 — 제2-8부: 소프트웨어 모듈용 정보모델 상호운용성 시험 절차 · 한국지능형로봇표준포럼(KOROS) · 표준
- OPC Foundation 인증 프로그램(적합성 시험 도구 CTT·독립 시험소 인증) · OPC Foundation · 평가 프로그램
- Nav2 costmap_2d (비용 지도·비용 지도 필터: 금지 구역·속도 제한) · ROS Navigation (ros-navigation/navigation2) · 오픈소스
- SLAM2REF (라이다 데이터의 기준 지도 다중 세션 정렬 도구) · Vega-Torres, M. A. (MigVega GitHub) · 오픈소스
- Open-RMF rmf_task_ros2 디스패처·입찰 경매자(평가기) · Open Robotics (open-rmf) · 오픈소스
- Rasa 폴백·사람 인계(Fallback and Human Handoff, Rasa 3.x) · Rasa Technologies · 오픈소스
- nudged (2D 유사 변환 추정 라이브러리) · Palonen, A. (axelpale/nudged GitHub) · 오픈소스
- Rasa CALM 대화 복구 패턴(rasa-calm-demo patterns.yml) · Rasa Technologies · 오픈소스
- IfcDiff (IfcOpenShell IFC 모델 비교 도구, v0.8.0 문서) · IfcOpenShell · 오픈소스
- BS EN ISO 19650 Guidance Part C: 공통 데이터 환경(Edition 1) · UK BIM Framework · 프레임워크
- OWASP Top 10 for LLM Applications 2025 (LLM06 Excessive Agency) · OWASP · 프레임워크
- Model Context Protocol 명세 2025-06-18 (Server Features: Tools) · Model Context Protocol (modelcontextprotocol GitHub) · 표준
- LangChain Human-in-the-loop 미들웨어 · LangChain · 오픈소스
- ISO 18646-2:2024 서비스 로봇 성능 기준과 시험 방법 — Part 2: 주행 · ISO · 표준
- ASTM F3244 Standard Test Method for Navigation: Defined Area · ASTM International · 표준
- SSIG (평면도 구조 유사도 지표) · van Engelenburg, C. 외 (caspervanengelenburg GitHub) · 오픈소스
- SLABIM (SLAM–BIM 결합 데이터셋) · HKUST Aerial Robotics Group · 오픈소스
- vda5050-sim (VDA 5050 가상 로봇 플릿 시뮬레이터) · gpue (vda5050-sim GitHub, 개인 저장소) · 오픈소스
- vda-5050-lib.js (가상 AGV 어댑터 포함 VDA 5050 라이브러리) · coatyio · 오픈소스
- τ-bench (도구–에이전트–사용자 상호작용 벤치마크) · sierra-research · 평가 프로그램
- SafeAgentBench (LLM 체화 에이전트 안전 계획 벤치마크) · SafeAgentBench 저자(shengyin1224 공식 저장소) · 평가 프로그램
- JSON Schema Validation (json-schema-spec, main 브랜치 차기판 초안) · JSON Schema (json-schema-org) · 표준
- VAL (PDDL 계획 검증 도구) · KCL-Planning · 오픈소스
- JSONSchemaBench · guidance-ai · 오픈소스
- Model Context Protocol 명세 2025-06-18 (Basic: Authorization) · Model Context Protocol (modelcontextprotocol GitHub) · 표준
- NIST SP 800-162 속성 기반 접근 통제(ABAC) 정의와 고려 사항 · NIST · 프레임워크
- RobotFleet (LLM·MILP 작업 배정기를 둔 중앙 다중 로봇 계획 틀) · therohangupta (RobotFleet 공식 저장소) · 오픈소스
- rosbag2 · ROS 2 (ros2/rosbag2 GitHub) · 오픈소스
- Simod (로그 기반 업무 프로세스 시뮬레이션 모델 자동 발견 도구) · Camargo, M., Dumas, M., & González-Rojas, O. · 오픈소스
- Open-RMF 작업 요청 스키마(rmf_api_msgs task_request) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF 작업 구성(compose 범주)과 단계 API(ros2multirobotbook task_new) · Open Robotics · 오픈소스
- VerifyLLM (LLM 기반 사전 실행 작업 계획 검증 모듈, 코드 공개) · Grigorev, D. S., Kovalev, A. K., & Panov, A. I. (IROS 2025) · 오픈소스
- EU AI Act 제12조 기록 보관 (Regulation (EU) 2024/1689, Article 12 Record-keeping) · European Union (유럽위원회 AI Act Service Desk 게재) · 프레임워크
- 생성형 인공지능(AI) 개발·활용을 위한 개인정보 처리 안내서(2025.8.) · 개인정보보호위원회 · 프레임워크
- 2024 신뢰할 수 있는 인공지능 개발 안내서 — 일반분야 · 과학기술정보통신부·한국정보통신기술협회(TTA) · 프레임워크
- Embodied Agent Interface (체화 의사결정 언어 모델 벤치마크) · Li, M. 외 (NeurIPS 2024 Datasets and Benchmarks) · 평가 프로그램
- langbar (다중 모달 GUI–MCP 아키텍처 참조 구현) · van Dam, H. G. W. · 오픈소스
- IDTA 02006 Digital Nameplate for Industrial Equipment (3.0) · IDTA(Industrial Digital Twin Association) · 표준
- IDTA-01002 Asset Administration Shell Specification — API (3.2.0) · IDTA(Industrial Digital Twin Association) · 표준
- RoMi-H Empanelment Programme (싱가포르 공공 의료기관 시스템 통합사 등재) · Changi General Hospital CHART(Centre for Healthcare Assistive & Robotics Technology) · 평가 프로그램
- CSS 온톨로지 (CaSkade-Automation/CSS, Plattform Industrie 4.0 능력·스킬·서비스 모델의 OWL 구현) · CaSkade-Automation (Helmut Schmidt University, Institute of Automation Technology) · 오픈소스
- OWL 2 Web Ontology Language Structural Specification (Second Edition) · W3C · 표준
- IDTA 서브모델 템플릿 공식 저장소(admin-shell-io/submodel-templates) 판·폐기 규칙 · IDTA(Industrial Digital Twin Association) · 표준
- KGCL (Knowledge Graph Change Language) · Hegde, H. 외 (Database, Oxford) · 프레임워크
- ISO 13482 (서비스 로봇 안전 요구사항) · ISO · 표준
- RoMi-H (Robotic Middleware for Healthcare) · Changi General Hospital CHART(Centre for Healthcare Assistive & Robotics Technology) · 오픈소스
- 서비스로봇 실증사업 · 한국로봇산업진흥원 · 평가 프로그램
- 스마트병원 선도모델(9개 모듈) · 한국보건산업진흥원 스마트병원 확산지원센터 · 프레임워크
- 로봇 친화형 건축물 인증 · 스마트도시협회 · 평가 프로그램
- Matter 1.2 (로봇청소기 장치 유형 포함) · Connectivity Standards Alliance (CSA) · 표준
- 실외이동로봇 운행안전인증 (지능형로봇법 제40조의2) · 한국로봇산업진흥원 · 평가 프로그램
- ISO/TR 4448-1:2024 Public-area mobile robots (PMR) — Part 1: Overview of paradigm · ISO (ISO/TC 204) · 표준
- ISO 4448 시리즈 (Public-area mobile robots, Part 6·9·16 개발 중) · ISO/TC 204 · 표준
- Nav2 GPS 항법 구성 (navsat_transform·두 EKF 융합·rolling 전역 비용 지도) · Open Navigation (Nav2) · 오픈소스
- SiLA 2 (Standardization in Lab Automation 2) · SiLA Consortium · 표준
- ISO 18497-3:2024 부분 자동·반자율·자율 농업기계 안전 — 제3부: 자율 운용 구역 · ISO · 표준
- SS 713 Data Exchange Between Robots, Lifts and Automated Doorways · 싱가포르(발행 기관명 미확인, The Robot Report 보도 기준) · 표준
- TR 130 Interoperability Between Robots and Central Command Systems · 싱가포르(발행 기관명 미확인, The Robot Report 보도 기준) · 표준
- IEEE 1873-2015 Robot Map Data Representation for Navigation · IEEE Standards Association (IEEE RAS) · 표준
- osmAG (OSM 형식 계층형 위상·거리 의미 지도) · Feng, D. 외 (arXiv) · 프레임워크
- Open-RMF 차선 요청 메시지(rmf_fleet_msgs LaneRequest) · Open Robotics (open-rmf) · 오픈소스
- OpenAPI Specification 3.1.0 · OpenAPI Initiative · 표준
- AsyncAPI Specification 3.1.0 · AsyncAPI Initiative · 표준
- FogROS2 (클라우드·포그 로보틱스 플랫폼) · Ichnowski, J., Chen, K., Dharmarajan, K. 외 · 오픈소스
- MCAP (rosbag2 기본 기록 형식, ROS 2 Iron 부터) · Foxglove (ROS 2 채택: Open Robotics) · 오픈소스
- OpenTelemetry 생성형 AI 의미 규약 — 토큰 지표 · OpenTelemetry (CNCF) · 오픈소스
- ros-opentelemetry · szobov (GitHub, 개인 저장소) · 오픈소스
- Mender (OTA 업데이트 관리자) · Northern.tech (mendersoftware) · 오픈소스
- FinOps 프레임워크 (FinOps Phases) · FinOps Foundation · 프레임워크
- FOCUS 1.2 (FinOps 청구 데이터 명세) · FinOps Foundation · 표준
- Open X-Embodiment 데이터셋·RT-X 모델 · Open X-Embodiment Collaboration · 오픈소스
- OpenVLA · Kim, M. J., Pertsch, K., Karamcheti, S. 외 · 오픈소스
- GR00T N1 · NVIDIA · 오픈소스
- POGEMA (협동 다중 에이전트 경로 찾기 벤치마크 플랫폼) · Skrynnik, A. 외 (ICLR 2025) · 평가 프로그램
- ISO 13381-1:2025 기계 상태 감시·진단 — 예지 — Part 1: 일반 지침과 요구사항 · ISO (ISO/TC 108) · 표준
- Docling (AI 기반 문서 변환 오픈소스 도구) · IBM Research · 오픈소스
- LangExtract (원문 위치 근거를 붙이는 LLM 정보 추출 라이브러리) · Google (google/langextract) · 오픈소스
- AECV-Bench (건축·엔지니어링 도면 이해 벤치마크) · Kondratenko, A. 외 (arXiv 2601.04819) · 평가 프로그램
- FloorPlanCAD (파놉틱 심볼 스포팅용 CAD 평면도 데이터셋) · Fan, Z. 외 (arXiv 2105.07147) · 평가 프로그램
- Nav2 Collision Monitor (nav2_collision_monitor) · Open Navigation (ros-navigation/navigation2) · 오픈소스
- ASAM OpenSCENARIO XML (1.4.0) · ASAM e.V. · 표준
- SDFormat (Simulation Description Format) · Open Source Robotics Foundation · 오픈소스
- BEHAVIOR-1K (BDDL 활동 명세·OmniGibson) · Stanford 등 (Li, C. 외) · 평가 프로그램
- Moving AI MAPF 벤치마크 · Moving AI Lab (Sturtevant 외) · 평가 프로그램
- Arena-Bench · Kästner, L. 외 (RA-L 2022) · 평가 프로그램
- ISA-101 시리즈 (ISA-101.01-2015, ISA-TR101.01-2022 HMI 철학, ISA-TR101.02-2019 HMI 사용성과 성능) · ISA(International Society of Automation) · 표준
- Open-RMF rmf_visualization · Open Robotics (open-rmf) · 오픈소스
- Open-RMF 작업 로그 스키마(rmf_api_msgs task_log·log_entry) · Open Robotics (open-rmf) · 오픈소스
- IEC 62559 사용 사례 방법론 (Part 1~4) · IEC · 표준
- ISO/IEC/IEEE 29148:2018 요구공학 · ISO / IEC / IEEE · 표준
- 로봇활용 표준공정모델 · 산업통상자원부 · 프레임워크
- OWASP Top 10 for LLM Applications 2025 (LLM01 Prompt Injection) · OWASP GenAI Security Project · 프레임워크
- EU 기계류 규정 (EU) 2023/1230 (변조 보호·개입 증거 기록, 업계 해설 기준) · European Union (IES 해설 경유) · 프레임워크
- KISA 로봇 분야 보안모델 고도화판·사이버보안 요구사항 해설서 · 과학기술정보통신부·한국인터넷진흥원(KISA) · 프레임워크
- 윤리적 블랙박스(EBB) 공개 표준 초안 (An Ethical Black Box for Social Robots: a draft Open Standard) · Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv) · 프레임워크
- VDI/VDE 3693 Blatt 1 가상 시운전 — 모델 유형·용어·정의 (2025-05 개정판) · VDI/VDE (VDI/VDE-Gesellschaft Mess- und Automatisierungstechnik) · 표준
- NASA-STD-7009B Standard for Models and Simulations · NASA · 표준
- 개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한) · 개인정보보호위원회 · 프레임워크
- 이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서(2024.9.) · 개인정보보호위원회 · 프레임워크
- 가명정보 처리 가이드라인(2024-02 개정, 비정형 데이터 포함) · 개인정보보호위원회 · 프레임워크
- 영상정보 원본 활용 규제샌드박스 실증특례 · 개인정보보호위원회 · 프레임워크
- EDPB Guidelines 3/2019 on processing of personal data through video devices · European Data Protection Board (EDPB) · 프레임워크
- EgoBlur · Meta Reality Labs · 오픈소스
- ANSI/A3 R15.08-3-2026 산업용 이동로봇 안전 요구사항 제3부: IMR 응용의 사용 · ANSI / A3(Association for Advancing Automation) · 표준
- HSE Human Factors Briefing Note No. 8 — Safety-Critical Communications · UK Health and Safety Executive (HSE) · 프레임워크
- IEC 60300-3-3:2017 신뢰성 관리 — 적용 지침 — 수명주기 비용 · IEC(International Electrotechnical Commission) · 표준
- REP 155 Conventions, Topics, Interfaces for Perception in Human-Robot Interaction (ROS4HRI) · ROS (ros-infrastructure/rep) · 프레임워크
- HuNavSim (ROS 2 사람 보행 시뮬레이터) · Pérez-Higueras, N., Otero, R., Caballero, F., & Merino, L. · 오픈소스
- Open-RMF CrowdSim (Menge 기반 군중 시뮬레이션) · Open Robotics · 오픈소스
- 사회적 내비게이션 평가 원칙·지침 (Principles and Guidelines for Evaluating Social Robot Navigation Algorithms) · Francis, A. 외 · 프레임워크
- BSRIA BG 54/2018 Soft Landings Framework (소프트 랜딩 프레임워크) · BSRIA · 프레임워크
- 산업안전보건법 시행규칙 별표 5 로봇작업 특별교육 · 법제처(법령해석 법제처-23-0872 경유) · 프레임워크
- EU 데이터법 (Regulation (EU) 2023/2854, Data Act) · European Union (European Commission 해설) · 프레임워크
- EU 데이터법 모델 계약 조항·클라우드 표준 계약 조항 권고 초안 · European Commission · 프레임워크
- 산업데이터 계약 가이드라인 · 산업통상부 · 프레임워크
- Kubernetes Deprecation Policy (API 폐기 정책) · The Kubernetes Authors · 오픈소스
- ISO/IEC 19086-1:2016 클라우드 SLA 프레임워크 — Part 1: 개요와 개념 · ISO/IEC (JTC 1) · 표준
- IEC 62443-2-4:2023 IACS 서비스 제공자 보안 프로그램 요구사항 · IEC · 표준
- EU AI법 제25조(AI 가치사슬 책임)·제26조(고위험 AI 배포자 의무) · European Union (Future of Life Institute 비공식 게재본 경유) · 프레임워크
- 21 CFR Part 11 §11.10 폐쇄형 시스템 통제(감사 추적) · U.S. Food and Drug Administration · 프레임워크
- ISO/IEC Guide 71:2014 표준의 접근성 반영 지침(2판) · ISO/IEC · 표준
- 장애인차별금지법에 따른 무인정보단말기 접근성 의무(2026-01-28 전면 시행) · 보건복지부 · 프레임워크
- 근로자참여 및 협력증진에 관한 법률 제20조(협의 사항) · 대한민국 국회 · 프레임워크
- 독일 사업장조직법(BetrVG) 제87조 공동결정권 · Bundesministerium der Justiz · 프레임워크
- 지능형로봇법·도로교통법 개정(실외이동로봇 보도 통행·운용자 의무·보험 의무, 2023-11-17 시행) · 산업통상자원부·경찰청 · 프레임워크
- 버지니아주법 §46.2-908.1:1 개인 배송 장치(Personal Delivery Devices) · Commonwealth of Virginia · 프레임워크
- EU 개정 제조물책임지침 (Directive (EU) 2024/2853) · European Union (Gibson Dunn 해설 경유) · 프레임워크
- 한국 제조물책임법 · 대한민국 (김·장 법률사무소 해설 경유) · 프레임워크
- 인공지능 기본법 (2026-01-22 시행) · 과학기술정보통신부 · 프레임워크
- EU 사이버복원력법(CRA) 보고 의무 · European Commission · 프레임워크
- 산업안전보건법 안전검사 (산업용 로봇·컨베이어) · 고용노동부 · 프레임워크
- ROS 2 개발자 가이드 (패키지 라이선스·저작권 규칙) · Open Robotics (ROS 2 Documentation) · 오픈소스
- REP 2004 Package Quality Categories · ROS (ros-infrastructure/rep) · 프레임워크
- SPDX (ISO/IEC 5962:2021) · SPDX Project (Linux Foundation) · 표준
- Gazebo(클래식) 모델 구조·요구사항 (모델 데이터베이스 라이선스 표기) · Open Robotics (Gazebo Classic) · 오픈소스
- ANSI/ISA 18.2-2016 공정 산업 경보 시스템 관리 (Management of Alarm Systems for the Process Industries) · ISA(International Society of Automation) · 표준
- IDTA 02005 Provision of Simulation Models (1.0) · IDTA(Industrial Digital Twin Association) · 표준
- autoware_rosbag2_anonymizer · Autoware Foundation · 오픈소스
- Gazebo Fuel Tools (gz-fuel-tools) · Open Robotics · 오픈소스
- ISO/AWI 26159-2 로봇 응용을 위한 기반시설 — 승강기·자동문 연동 요구사항 (초안) · ISO (ISO/TC 299 Robotics) · 표준
- ISO/CD TS 8100-11 승강기와 다른 시스템의 상호운용 (위원회 초안) · ISO (ISO/TC 178 Lifts, escalators and moving walks) · 표준
- 싱가포르 Technical Reference 93 (TR 93) 로봇–건물 설비 데이터 교환 · 싱가포르 (CGH 보도자료 기준, 발행 기관명 미확인) · 표준
- Open-RMF 장애물 메시지(rmf_internal_msgs의 rmf_obstacle_msgs) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF rmf_obstacle (사람 검출·lane_blocker) · Open Robotics (open-rmf) · 오픈소스
- Scenario Execution for Robotics (OpenSCENARIO 2 기반 로봇 시나리오 실행 라이브러리) · Pasch, F. 외 (Intel Labs 외) · 오픈소스
- RoboVAST (출처 기록 기반 시뮬레이션 시험 틀) · Ortega, A., Wiest, S., Pasch, F., & Hochgeschwender, N. · 프레임워크
- ISO 11064 관제 센터 인간공학 설계(Ergonomic design of control centres) 계열 · ISO · 표준
- IEEE 7001-2021 자율 시스템 투명성 표준 · IEEE Standards Association · 표준
- W3C Trace Context (traceparent·tracestate, 권고안 2021-11-23) · W3C · 표준
- EU AI Act 제19조 자동 생성 로그 (Article 19) · European Union (유럽위원회 AI Act Service Desk 게재) · 프레임워크
- EU 기계류 지침 2006/42/EC 부속서 I 1.7.4.1 (설명서 언어·원본·번역 표기) · European Parliament and Council (legislation.gov.uk 게재본) · 프레임워크
- MMLongBench-Doc (긴 문서 이해 벤치마크) · Ma, Y. 외 (NeurIPS 2024 Datasets and Benchmarks) · 평가 프로그램
- NVIDIA Isaac Mission Dispatch · NVIDIA (nvidia-isaac) · 오픈소스
- NVIDIA Isaac Mission Control · NVIDIA (nvidia-isaac) · 오픈소스
- PlanSys2 (ROS 2 Planning System) · PlanSys2 프로젝트 · 오픈소스
- crossflow · Open Robotics (open-rmf) · 오픈소스
- Open BIM Object standard (OBOS) V1.0 · Construction Information Limited (Masterspec, 뉴질랜드) · 표준
- W3C SKOS (Simple Knowledge Organization System) Reference · W3C · 표준
- BPMN 2.0.2 (OMG formal/13-12-09) · OMG(Object Management Group) · 표준
- Open-RMF 입찰 제안 메시지(rmf_internal_msgs의 rmf_task_msgs BidProposal) · Open Robotics (open-rmf) · 오픈소스
- KS B ISO 22166-202 로봇 — 서비스 로봇의 모듈화 — 제202부: 소프트웨어 모듈용 정보 모델 · 국가표준인증통합정보시스템(KSSN) · 표준
- 엘리베이터와 로봇의 상호 연동을 위한 가이드라인 (대한승강기협회 단체표준) · 대한승강기협회(KOLA) · 표준
- KONE RMF Lift Adapter (kone-ros-api) · CHART (KABAM-Robotics 보존 저장소) · 오픈소스
- door_adapter_dormakaba (Open-RMF Dormakaba 문 어댑터) · Open Robotics (open-rmf) · 오픈소스
- Open-RMF 작업 배정·취소 응답 스키마(rmf_api_msgs dispatch_task_response·cancel_task_response·simple_response) · Open Robotics (open-rmf) · 오픈소스
- KS B 7327 산업용 이동 머니퓰레이터의 응용을 위한 안전 요구사항 · 국가기술표준원(한국표준협회 KSSN) · 표준
- KS B ISO 3691-4 산업용 트럭 — 안전 요구사항과 검증 — 제4부: 무인 산업용 트럭과 시스템 · 국가기술표준원(한국표준협회 KSSN) · 표준
- 사업장 위험성평가에 관한 지침(고용노동부고시 제2024-76호) · 고용노동부 · 프레임워크
- STPA Handbook · MIT Partnership for Systems Approaches to Safety and Security · 프레임워크
- KS B 8252 실내 이동로봇의 보호정지 시험방법 · 국가기술표준원 (e-나라표준인증) · 표준
- 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시(산업통상부고시 제2025-21호) 별표 3 · 산업통상부 · 평가 프로그램
- human_detection_fusion (YOLO·UWB 사람 위치 융합 ROS 2 패키지) · ATHENA RC (EU ARISE 'KIRO' 실험) · 오픈소스
- UL 3100 Automated Mobile Platforms (AMPs) · UL Standards & Engagement · 표준
- UL 3300 (SCIEE 로봇 표준, Simbe Tally 인증 발표) · UL Solutions · 표준
- ISO/DIS 3691-4 (제3판) 무인 산업용 트럭과 그 시스템 안전 요구·검증 개정안 · ISO · 표준
- KS B ISO 10218-1 산업용 로봇의 안전에 관한 요구사항 — 제1부: 로봇 · 국가기술표준원 · 표준
- 산업용 로봇 자율안전확인 · 안전보건공단 산업안전보건인증원 · 평가 프로그램
- 위원회 시행결정 (EU) 2026/2015 (기계류 지침 조화 표준 목록 개정·폐지) · European Commission · 프레임워크
```

### runs/2026-10-12-04/docs_tree.txt

```text
about/agents.md
about/how-to-contribute.md
about/idea-mapping.md
about/reading-guide.md
about/research-method.md
about/scope-boundary.md
about/simulator.md
about/what-is-rop.md
categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md
categories/ai-and-learning/document-drawing-and-scene-understanding.md
categories/ai-and-learning/index.md
categories/ai-and-learning/prediction-and-learning-based-optimization.md
categories/ai-and-learning/robot-foundation-models-and-llm-planning.md
categories/chat-based-configuration-and-operation/chat-map-authoring.md
categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md
categories/chat-based-configuration-and-operation/chat-robot-configuration.md
categories/chat-based-configuration-and-operation/chat-scenario-composition.md
categories/chat-based-configuration-and-operation/chat-task-instruction-and-orchestration.md
categories/chat-based-configuration-and-operation/conversational-trust-and-foundations.md
categories/chat-based-configuration-and-operation/index.md
categories/design-and-simulation/capacity-sizing-and-layout-design.md
categories/design-and-simulation/index.md
categories/design-and-simulation/scenario-model-and-editing.md
categories/design-and-simulation/simulation-and-predictive-digital-twin.md
categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md
categories/execution-collaboration-and-recovery/command-and-task-execution-reliability.md
categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md
categories/execution-collaboration-and-recovery/human-robot-collaboration.md
categories/execution-collaboration-and-recovery/index.md
categories/execution-collaboration-and-recovery/robot-to-robot-collaboration-and-physical-handover.md
categories/field-operations-and-monitoring/control-screen-and-execution-records.md
categories/field-operations-and-monitoring/index.md
categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md
categories/field-operations-and-monitoring/operating-procedures-and-request-channels.md
categories/field-operations-and-monitoring/operational-performance-measurement-and-improvement.md
categories/governance-law-and-society/index.md
categories/governance-law-and-society/labor-acceptance-and-accessibility.md
categories/governance-law-and-society/law-regulation-insurance-and-licensing.md
categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md
categories/integration/business-system-integration.md
categories/integration/facility-and-building-system-integration.md
categories/integration/index.md
categories/integration/interoperability-standards-and-conformance.md
categories/integration/robot-and-vendor-fleet-manager-integration.md
categories/objects-people-and-live-state/index.md
categories/objects-people-and-live-state/people-and-pedestrian-model.md
categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md
categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md
categories/planning-and-business/economics-procurement-and-business-models.md
categories/planning-and-business/index.md
categories/planning-and-business/technology-market-and-vendor-trends.md
categories/planning-and-business/use-cases-requirements-and-scope.md
categories/planning-and-optimization/index.md
categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md
categories/planning-and-optimization/shared-resource-charging-and-energy-optimization.md
categories/planning-and-optimization/task-allocation-mrta.md
categories/planning-and-optimization/task-and-workflow-modeling.md
categories/planning-and-optimization/task-sequencing-and-scheduling.md
categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md
categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md
categories/platform-architecture-and-infrastructure/index.md
categories/platform-architecture-and-infrastructure/platform-architecture-and-external-api.md
categories/robot-ontology/heterogeneous-robot-registration.md
categories/robot-ontology/index.md
categories/robot-ontology/ontology-based-system-and-robot-integration.md
categories/robot-ontology/ontology-verification-and-change-management.md
categories/robot-ontology/robot-capability-and-task-representation.md
categories/safety/human-proximity-safety.md
categories/safety/index.md
categories/safety/safety-and-risk-management.md
categories/safety/safety-standards-certification-and-incident-investigation.md
categories/security-and-privacy/authentication-authorization-and-isolation.md
categories/security-and-privacy/communication-protection-threat-management-and-audit.md
categories/security-and-privacy/index.md
categories/security-and-privacy/privacy-and-video-data.md
categories/site-type-applications/commercial-facilities.md
categories/site-type-applications/home-and-apartment.md
categories/site-type-applications/hospital-and-healthcare.md
categories/site-type-applications/index.md
categories/site-type-applications/manufacturing-plant.md
categories/site-type-applications/other-sites.md
categories/site-type-applications/outdoor.md
categories/site-type-applications/warehouse.md
categories/space-and-map-model/index.md
categories/space-and-map-model/map-space-and-location-model.md
categories/space-and-map-model/maps-from-floor-plans-and-bim.md
categories/space-and-map-model/place-semantics-and-map-management.md
categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md
categories/verification-deployment-and-lifecycle/index.md
categories/verification-deployment-and-lifecycle/operations-handover-scale-out-and-training.md
categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md
categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md
changelog.md
corrections.md
glossary/3d-scene-graph.md
glossary/4d-scene-graph.md
glossary/a-b-update.md
glossary/aas-registry-and-discovery.md
glossary/ablation-study.md
glossary/abstract-and-concrete-scenario.md
glossary/action-dependency-graph.md
glossary/action-status.md
glossary/actively-exploited-vulnerability.md
glossary/affordance.md
glossary/age-of-information.md
glossary/agentic-ai.md
glossary/aggregation-event.md
glossary/agv-technical-data-submodel.md
glossary/alarm-management.md
glossary/alert-tier.md
glossary/almere-model.md
glossary/alternative-name.md
glossary/amr-assisted-order-picking.md
glossary/api-deprecation-policy.md
glossary/approval-fatigue.md
glossary/ariac.md
glossary/artificial-intelligence-management-system.md
glossary/as-planned-vs-as-built-deviation.md
glossary/asam-openscenario.md
glossary/assembly-line-feeding-problem.md
glossary/asset-administration-shell.md
glossary/association-event.md
glossary/asyncapi-specification.md
glossary/attribute-based-access-control.md
glossary/audit-trail.md
glossary/automatic-recording-of-events.md
glossary/automatic-simulation-model-generation.md
glossary/automation-bias.md
glossary/average-displacement-error.md
glossary/b2mml.md
glossary/bag-file.md
glossary/battery-swapping.md
glossary/behavior-domain-definition-language.md
glossary/behavior-tree.md
glossary/block-reference.md
glossary/bpmn.md
glossary/brainless-robot.md
glossary/building-element-proxy.md
glossary/building-information-modeling.md
glossary/building-topology-ontology.md
glossary/buildingsmart-data-dictionary.md
glossary/business-continuity-management-system.md
glossary/business-location.md
glossary/cap-theorem.md
glossary/capabilities-skills-services.md
glossary/capability-based-task-allocation.md
glossary/capability-description-submodel.md
glossary/capability-matchmaking.md
glossary/cbv.md
glossary/cell-based-production.md
glossary/clarification-question.md
glossary/cloud-robotics.md
glossary/coalition-formation.md
glossary/collaborative-application.md
glossary/collaborative-perception.md
glossary/common-coordinate-system.md
glossary/common-data-environment.md
glossary/compensating-transaction.md
glossary/competency-question.md
glossary/condition-based-maintenance.md
glossary/configuration-copilot.md
glossary/conflict-based-search.md
glossary/conformal-prediction.md
glossary/conformance-test.md
glossary/confused-deputy.md
glossary/connection-state.md
glossary/consensus-based-bundle-algorithm.md
glossary/constrained-decoding.md
glossary/contrastive-explanation.md
glossary/control-barrier-function.md
glossary/cooperative-object-transport.md
glossary/cora.md
glossary/core-manufacturing-simulation-data.md
glossary/costmap.md
glossary/crdt.md
glossary/cross-embodiment-learning.md
glossary/cross-schedule-dependency.md
glossary/curb-cut.md
glossary/cyber-resilience-act.md
glossary/data-holder.md
glossary/data-provenance.md
glossary/dds-security.md
glossary/deadlock.md
glossary/decision-focused-learning.md
glossary/digital-nameplate.md
glossary/digital-shadow.md
glossary/digital-thread.md
glossary/digital-twin-composition.md
glossary/digital-twin.md
glossary/discrete-event-simulation.md
glossary/dispenser-ingestor.md
glossary/distributed-tracing.md
glossary/document-layout-analysis.md
glossary/domain-shift.md
glossary/door-to-door-robot-delivery.md
glossary/drawing-exchange-format.md
glossary/dual-system-architecture.md
glossary/eclass.md
glossary/edit-cost.md
glossary/elevator-operating-rate.md
glossary/empanelment-programme.md
glossary/enclave.md
glossary/epcis-error-declaration.md
glossary/epcis.md
glossary/ethical-black-box.md
glossary/event-driven-rescheduling.md
glossary/event-trace.md
glossary/excessive-agency.md
glossary/expected-value-of-perfect-information.md
glossary/explainable-mapf.md
glossary/explicit-implicit-confirmation.md
glossary/face-obfuscation.md
glossary/failure-explanation.md
glossary/falsification.md
glossary/fan-out.md
glossary/fault-detection-and-diagnosis-fdd.md
glossary/fault-injection.md
glossary/filter-mask.md
glossary/finops.md
glossary/fleet-adapter.md
glossary/fleet-control-level.md
glossary/fleet-management-system.md
glossary/fleet-sizing.md
glossary/floor-plan-recognition.md
glossary/fog-computing.md
glossary/frozen-horizon.md
glossary/generalized-voronoi-graph.md
glossary/giai.md
glossary/gln-extension-component.md
glossary/goal-condition.md
glossary/goods-to-person.md
glossary/grade-certainty-of-evidence.md
glossary/grai.md
glossary/graph-edit-distance.md
glossary/guidance-graph.md
glossary/hallucination.md
glossary/hardware-in-the-loop.md
glossary/hddl.md
glossary/hierarchical-task-network.md
glossary/high-impact-ai.md
glossary/hmi-philosophy.md
glossary/human-in-the-loop.md
glossary/human-motion-trajectory-prediction.md
glossary/hungarian-method.md
glossary/i-pass-handoff-program.md
glossary/idempotency-key.md
glossary/identity-report.md
glossary/iec-common-data-dictionary.md
glossary/ifc.md
glossary/imitation-learning.md
glossary/index.md
glossary/indirect-prompt-injection.md
glossary/indoor-mapping-data-format.md
glossary/indoor-space-subspacing.md
glossary/indoorgml.md
glossary/industrial-data.md
glossary/information-delivery-specification.md
glossary/information-for-use.md
glossary/infrastructure-mounted-sensing.md
glossary/integrity-risk.md
glossary/intent-recognition.md
glossary/irdi.md
glossary/irreducible-infeasible-subset.md
glossary/isa-95.md
glossary/it-ot-convergence.md
glossary/jailbreak.md
glossary/job-shop-scheduling-problem.md
glossary/joint-goal-accuracy.md
glossary/json-schema.md
glossary/keystroke-level-model.md
glossary/kiosk-accessibility.md
glossary/lane-closure.md
glossary/language-guided-floor-plan-generation.md
glossary/latent-failure.md
glossary/layout-interchange-format.md
glossary/lease-expiry.md
glossary/level-alignment-fiducial.md
glossary/life-cycle-costing.md
glossary/lifelong-mapf.md
glossary/lift-adapter.md
glossary/linear-temporal-logic-on-finite-traces.md
glossary/linear-temporal-logic.md
glossary/littles-law.md
glossary/llm-agent.md
glossary/llm-modulo-framework.md
glossary/localization-score.md
glossary/location-check-digit.md
glossary/lockout-tagout.md
glossary/log-playback.md
glossary/makespan.md
glossary/managed-node.md
glossary/management-of-change.md
glossary/map-alignment.md
glossary/map-distribution.md
glossary/map-version.md
glossary/mapf.md
glossary/maps-of-dynamics.md
glossary/market-based-task-allocation.md
glossary/matter.md
glossary/mcap.md
glossary/milp.md
glossary/minimum-cost-flow.md
glossary/mission-specification-pattern.md
glossary/mobile-manipulator.md
glossary/mobile-video-information-processing-device.md
glossary/model-checking.md
glossary/model-context-protocol.md
glossary/model-contractual-terms.md
glossary/model-registry.md
glossary/model-substitution-and-routing-dilution.md
glossary/models-and-simulations-credibility-assessment.md
glossary/mqtt-last-will.md
glossary/mqtt-quality-of-service-level.md
glossary/mqtt.md
glossary/mrta.md
glossary/multi-agent-pickup-and-delivery.md
glossary/multi-fleet-orchestration.md
glossary/multi-trip-vehicle-routing-problem.md
glossary/nearest-vehicle-first-rule.md
glossary/neuro-symbolic-ai.md
glossary/number-of-clicks.md
glossary/oauth2-client-credentials-grant.md
glossary/observability.md
glossary/occupancy-grid-map.md
glossary/ocel.md
glossary/online-simulation.md
glossary/ontology-evolution.md
glossary/ontology-pitfall.md
glossary/ontology-population.md
glossary/open-rmf.md
glossary/openapi-specification.md
glossary/opentelemetry-genai-semantic-conventions.md
glossary/opentelemetry.md
glossary/operating-mode.md
glossary/operating-zone.md
glossary/operational-state.md
glossary/optimality-gap.md
glossary/order-batching.md
glossary/original-instructions.md
glossary/outdoor-mobile-robot-operational-safety-certification.md
glossary/over-the-air-update.md
glossary/overall-equipment-effectiveness.md
glossary/panoptic-quality.md
glossary/panoptic-symbol-spotting.md
glossary/pass-k.md
glossary/pay-per-pick.md
glossary/payback-period.md
glossary/pddl.md
glossary/perfect-order-fulfillment.md
glossary/performable-action.md
glossary/persistence-filter.md
glossary/personal-delivery-device.md
glossary/phased-rollout.md
glossary/plug-and-produce.md
glossary/post-encroachment-time.md
glossary/post-occupancy-evaluation.md
glossary/power-and-force-limiting.md
glossary/pre-execution-plan-verification.md
glossary/pre-hold-post-condition.md
glossary/precedence-constraint.md
glossary/precision-time-protocol.md
glossary/predictive-maintenance.md
glossary/presumption-of-conformity.md
glossary/priority-inheritance-with-backtracking.md
glossary/private-5g-network.md
glossary/process-mining.md
glossary/product-liability.md
glossary/prompt-injection.md
glossary/protective-separation-distance.md
glossary/pseudonymisation.md
glossary/public-area-mobile-robot.md
glossary/put-wall.md
glossary/raster-to-vector-conversion.md
glossary/raw-video-regulatory-sandbox-exemption.md
glossary/read-point.md
glossary/reality-gap.md
glossary/regression-testing.md
glossary/release-zone.md
glossary/remote-attestation.md
glossary/remote-controlled-small-vehicle.md
glossary/required-and-provided-capability.md
glossary/resource-constrained-project-scheduling-problem.md
glossary/risk-assessment.md
glossary/roadmap.md
glossary/robot-as-a-service.md
glossary/robot-density.md
glossary/robot-foundation-model.md
glossary/robot-friendly-building-certification.md
glossary/robot-standard-process-model.md
glossary/robot-task-fitness-matrix.md
glossary/robotic-middleware-for-healthcare.md
glossary/robotic-mobile-fulfillment-system.md
glossary/role-ambiguity.md
glossary/role-based-access-control.md
glossary/root-cause-analysis-rca.md
glossary/runtime-tracing.md
glossary/runtime-verification.md
glossary/safe-interval-path-planning.md
glossary/safety-guardrail.md
glossary/safety-state-report.md
glossary/saga.md
glossary/satisfiability-modulo-theories.md
glossary/scan-vs-bim.md
glossary/scenario-reconstruction.md
glossary/schedule-stability.md
glossary/scor.md
glossary/security-level-iec-62443.md
glossary/self-driving-laboratory.md
glossary/semantic-id.md
glossary/semantic-map.md
glossary/semantic-versioning.md
glossary/semi-open-queueing-network.md
glossary/semi-static-object.md
glossary/service-level-agreement.md
glossary/service-triad.md
glossary/shacl.md
glossary/shift-handover.md
glossary/shifting-bottleneck-detection-active-period-method.md
glossary/shuttle-based-storage-and-retrieval-system.md
glossary/signal-temporal-logic.md
glossary/sila-2.md
glossary/sim-vs-real-correlation-coefficient.md
glossary/similarity-transformation.md
glossary/simulation-description-format.md
glossary/situation-awareness-based-agent-transparency.md
glossary/situation-awareness.md
glossary/situation-state-tracking.md
glossary/skill-interface.md
glossary/skill.md
glossary/skos.md
glossary/slot-filling.md
glossary/slotcar.md
glossary/smart-hospital-leading-model.md
glossary/smart-logistics-center-certification.md
glossary/social-force-model.md
glossary/social-robot-navigation.md
glossary/soft-landings.md
glossary/software-bill-of-materials.md
glossary/software-in-the-loop.md
glossary/software-nameplate.md
glossary/source-grounding.md
glossary/space-boundary.md
glossary/space-graph.md
glossary/speed-and-separation-monitoring.md
glossary/sscc.md
glossary/stakeholder-requirements-specification.md
glossary/state-of-charge.md
glossary/state-of-health.md
glossary/state-script.md
glossary/stpa.md
glossary/strict-schema.md
glossary/stride-threat-classification.md
glossary/structured-output.md
glossary/substantial-modification.md
glossary/success-weighted-by-path-length.md
glossary/supervisory-control.md
glossary/surrogate-model.md
glossary/synchronization-loss.md
glossary/table-structure-recognition.md
glossary/tamper-evident-log.md
glossary/task-decomposition.md
glossary/task-dependency-graph.md
glossary/technology-readiness-level.md
glossary/teleoperation.md
glossary/time-window.md
glossary/topological-map.md
glossary/total-cost-of-ownership.md
glossary/trace-context.md
glossary/transparency-level-ieee-7001.md
glossary/traversability.md
glossary/uncertainty-alignment.md
glossary/underspecification.md
glossary/urdf.md
glossary/use-case-template.md
glossary/user-defined-property-set.md
glossary/user-simulator.md
glossary/utaut.md
glossary/vda-5050-cancel-order.md
glossary/vda-5050-factsheet.md
glossary/vda-5050-hibernation.md
glossary/vda-5050.md
glossary/verification-and-validation-of-simulation-models.md
glossary/version-iri.md
glossary/virtual-commissioning.md
glossary/vision-language-action-model.md
glossary/voice-picking.md
glossary/waveless-order-release.md
glossary/webhook.md
glossary/wes-wcs-wms-mes-tms.md
glossary/wireless-safety-rated-emergency-stop.md
glossary/workflow-diagram.md
glossary/workflow-net.md
glossary/zone-set.md
glossary/zones-and-conduits.md
ideas/chat-based-configuration-and-operation.md
ideas/floorplan-recognition.md
ideas/index.md
ideas/robot-capability-ontology.md
index.md
logs/daily/2026-09-25.md
logs/daily/2026-09-26.md
logs/daily/2026-09-29.md
logs/daily/2026-09-30.md
logs/daily/2026-10-09.md
logs/daily/2026-10-10.md
logs/daily/2026-10-11.md
logs/index.md
logs/weekly/2026-W39.md
metrics.md
open-questions.md
references/index.md
references/ref-001.md
references/ref-002.md
references/ref-003.md
references/ref-004.md
references/ref-005.md
references/ref-006.md
references/ref-007.md
references/ref-008.md
references/ref-009.md
references/ref-010.md
references/ref-011.md
references/ref-012.md
references/ref-013.md
references/ref-014.md
references/ref-015.md
references/ref-016.md
references/ref-017.md
references/ref-018.md
references/ref-019.md
references/ref-020.md
references/ref-021.md
references/ref-022.md
references/ref-023.md
references/ref-024.md
references/ref-025.md
references/ref-026.md
references/ref-027.md
references/ref-028.md
references/ref-029.md
references/ref-030.md
references/ref-031.md
references/ref-032.md
references/ref-033.md
references/ref-034.md
references/ref-035.md
references/ref-036.md
references/ref-037.md
references/ref-038.md
references/ref-039.md
references/ref-040.md
references/ref-041.md
references/ref-042.md
references/ref-043.md
references/ref-044.md
references/ref-045.md
references/ref-046.md
references/ref-047.md
references/ref-048.md
references/ref-049.md
references/ref-050.md
references/ref-051.md
references/ref-052.md
references/ref-053.md
references/ref-054.md
references/ref-055.md
references/ref-056.md
references/ref-057.md
references/ref-058.md
references/ref-059.md
references/ref-060.md
references/ref-061.md
references/ref-062.md
references/ref-063.md
references/ref-064.md
references/ref-065.md
references/ref-066.md
references/ref-067.md
references/ref-068.md
references/ref-069.md
references/ref-070.md
references/ref-071.md
references/ref-072.md
references/ref-073.md
references/ref-074.md
references/ref-075.md
references/ref-076.md
references/ref-077.md
references/ref-078.md
references/ref-079.md
references/ref-080.md
references/ref-081.md
references/ref-082.md
references/ref-083.md
references/ref-084.md
references/ref-085.md
references/ref-086.md
references/ref-087.md
references/ref-088.md
references/ref-089.md
references/ref-090.md
references/ref-091.md
references/ref-092.md
references/ref-093.md
references/ref-094.md
references/ref-095.md
references/ref-096.md
references/ref-097.md
references/ref-098.md
references/ref-099.md
references/ref-100.md
references/ref-1000.md
references/ref-1001.md
references/ref-1002.md
references/ref-1003.md
references/ref-1004.md
references/ref-1005.md
references/ref-1006.md
references/ref-1007.md
references/ref-1008.md
references/ref-1009.md
references/ref-101.md
references/ref-1010.md
references/ref-1011.md
references/ref-1012.md
references/ref-1013.md
references/ref-1014.md
references/ref-1015.md
references/ref-1016.md
references/ref-1017.md
references/ref-1018.md
references/ref-1019.md
references/ref-102.md
references/ref-1020.md
references/ref-1021.md
references/ref-1022.md
references/ref-1023.md
references/ref-1024.md
references/ref-1025.md
references/ref-1026.md
references/ref-1027.md
references/ref-1028.md
references/ref-1029.md
references/ref-103.md
references/ref-1030.md
references/ref-1031.md
references/ref-1032.md
references/ref-1033.md
references/ref-1034.md
references/ref-1035.md
references/ref-1036.md
references/ref-1037.md
references/ref-1038.md
references/ref-1039.md
references/ref-104.md
references/ref-1040.md
references/ref-1041.md
references/ref-1042.md
references/ref-1043.md
references/ref-1044.md
references/ref-1045.md
references/ref-1046.md
references/ref-1047.md
references/ref-1048.md
references/ref-1049.md
references/ref-105.md
references/ref-1050.md
references/ref-1051.md
references/ref-1052.md
references/ref-1053.md
references/ref-1054.md
references/ref-1055.md
references/ref-1056.md
references/ref-1057.md
references/ref-1058.md
references/ref-1059.md
references/ref-106.md
references/ref-1060.md
references/ref-1061.md
references/ref-1062.md
references/ref-1063.md
references/ref-1064.md
references/ref-1065.md
references/ref-1066.md
references/ref-1067.md
references/ref-1068.md
references/ref-1069.md
references/ref-107.md
references/ref-1070.md
references/ref-1071.md
references/ref-1072.md
references/ref-1073.md
references/ref-1074.md
references/ref-1075.md
references/ref-1076.md
references/ref-1077.md
references/ref-1078.md
references/ref-1079.md
references/ref-108.md
references/ref-1080.md
references/ref-1081.md
references/ref-1082.md
references/ref-1083.md
references/ref-1084.md
references/ref-1085.md
references/ref-1086.md
references/ref-1087.md
references/ref-1088.md
references/ref-1089.md
references/ref-109.md
references/ref-1090.md
references/ref-1091.md
references/ref-1092.md
references/ref-1093.md
references/ref-1094.md
references/ref-1095.md
references/ref-1096.md
references/ref-1097.md
references/ref-1098.md
references/ref-1099.md
references/ref-110.md
references/ref-1100.md
references/ref-1101.md
references/ref-1102.md
references/ref-1103.md
references/ref-1104.md
references/ref-1105.md
references/ref-1106.md
references/ref-1107.md
references/ref-1108.md
references/ref-1109.md
references/ref-111.md
references/ref-1110.md
references/ref-1111.md
references/ref-1112.md
references/ref-1113.md
references/ref-1114.md
references/ref-1115.md
references/ref-1116.md
references/ref-1117.md
references/ref-1118.md
references/ref-1119.md
references/ref-112.md
references/ref-1120.md
references/ref-1121.md
references/ref-1122.md
references/ref-1123.md
references/ref-1124.md
references/ref-1125.md
references/ref-1126.md
references/ref-1127.md
references/ref-1128.md
references/ref-1129.md
references/ref-113.md
references/ref-1130.md
references/ref-1131.md
references/ref-1132.md
references/ref-1133.md
references/ref-1134.md
references/ref-1135.md
references/ref-1136.md
references/ref-1137.md
references/ref-1138.md
references/ref-1139.md
references/ref-114.md
references/ref-1140.md
references/ref-1141.md
references/ref-1142.md
references/ref-1143.md
references/ref-1144.md
references/ref-1145.md
references/ref-1146.md
references/ref-1147.md
references/ref-1148.md
references/ref-1149.md
references/ref-115.md
references/ref-1150.md
references/ref-1151.md
references/ref-1152.md
references/ref-1153.md
references/ref-1154.md
references/ref-1155.md
references/ref-1156.md
references/ref-1157.md
references/ref-1158.md
references/ref-1159.md
references/ref-116.md
references/ref-1160.md
references/ref-1161.md
references/ref-1162.md
references/ref-1163.md
references/ref-1164.md
references/ref-1165.md
references/ref-1166.md
references/ref-1167.md
references/ref-1168.md
references/ref-1169.md
references/ref-117.md
references/ref-1170.md
references/ref-1171.md
references/ref-1172.md
references/ref-1173.md
references/ref-1174.md
references/ref-1175.md
references/ref-1176.md
references/ref-1177.md
references/ref-1178.md
references/ref-1179.md
references/ref-118.md
references/ref-1180.md
references/ref-1181.md
references/ref-1182.md
references/ref-1183.md
references/ref-1184.md
references/ref-1185.md
references/ref-1186.md
references/ref-1187.md
references/ref-1188.md
references/ref-1189.md
references/ref-119.md
references/ref-1190.md
references/ref-1191.md
references/ref-1192.md
references/ref-1193.md
references/ref-1194.md
references/ref-1195.md
references/ref-1196.md
references/ref-1197.md
references/ref-1198.md
references/ref-1199.md
references/ref-120.md
references/ref-1200.md
references/ref-1201.md
references/ref-1202.md
references/ref-1203.md
references/ref-1204.md
references/ref-1205.md
references/ref-1206.md
references/ref-1207.md
references/ref-1208.md
references/ref-1209.md
references/ref-121.md
references/ref-1210.md
references/ref-1211.md
references/ref-1212.md
references/ref-1213.md
references/ref-1214.md
references/ref-1215.md
references/ref-1216.md
references/ref-1217.md
references/ref-1218.md
references/ref-1219.md
references/ref-122.md
references/ref-1220.md
references/ref-1221.md
references/ref-1222.md
references/ref-1223.md
references/ref-1224.md
references/ref-1225.md
references/ref-1226.md
references/ref-1227.md
references/ref-1228.md
references/ref-1229.md
references/ref-123.md
references/ref-1230.md
references/ref-1231.md
references/ref-1232.md
references/ref-1233.md
references/ref-1234.md
references/ref-1235.md
references/ref-1236.md
references/ref-1237.md
references/ref-1238.md
references/ref-1239.md
references/ref-124.md
references/ref-1240.md
references/ref-1241.md
references/ref-1242.md
references/ref-1243.md
references/ref-1244.md
references/ref-1245.md
references/ref-1246.md
references/ref-1247.md
references/ref-1248.md
references/ref-1249.md
references/ref-125.md
references/ref-1250.md
references/ref-1251.md
references/ref-1252.md
references/ref-1253.md
references/ref-1254.md
references/ref-1255.md
references/ref-1256.md
references/ref-1257.md
references/ref-1258.md
references/ref-1259.md
references/ref-126.md
references/ref-1260.md
references/ref-1261.md
references/ref-1262.md
references/ref-1263.md
references/ref-1264.md
references/ref-1265.md
references/ref-1266.md
references/ref-1267.md
references/ref-1268.md
references/ref-1269.md
references/ref-127.md
references/ref-1270.md
references/ref-1271.md
references/ref-1272.md
references/ref-1273.md
references/ref-1274.md
references/ref-1275.md
references/ref-1276.md
references/ref-1277.md
references/ref-1278.md
references/ref-1279.md
references/ref-128.md
references/ref-1280.md
references/ref-1281.md
references/ref-1282.md
references/ref-1283.md
references/ref-1284.md
references/ref-1285.md
references/ref-1286.md
references/ref-1287.md
references/ref-1288.md
references/ref-1289.md
references/ref-129.md
references/ref-1290.md
references/ref-1291.md
references/ref-1292.md
references/ref-1293.md
references/ref-1294.md
references/ref-1295.md
references/ref-1296.md
references/ref-1297.md
references/ref-1298.md
references/ref-1299.md
references/ref-130.md
references/ref-1300.md
references/ref-1301.md
references/ref-1302.md
references/ref-1303.md
references/ref-1304.md
references/ref-1305.md
references/ref-1306.md
references/ref-1307.md
references/ref-1308.md
references/ref-1309.md
references/ref-131.md
references/ref-1310.md
references/ref-1311.md
references/ref-1312.md
references/ref-1313.md
references/ref-1314.md
references/ref-1315.md
references/ref-1316.md
references/ref-1317.md
references/ref-1318.md
references/ref-1319.md
references/ref-132.md
references/ref-1320.md
references/ref-1321.md
references/ref-1322.md
references/ref-1323.md
references/ref-1324.md
references/ref-1325.md
references/ref-1326.md
references/ref-1327.md
references/ref-1328.md
references/ref-1329.md
references/ref-133.md
references/ref-1330.md
references/ref-1331.md
references/ref-1332.md
references/ref-1333.md
references/ref-1334.md
references/ref-1335.md
references/ref-1336.md
references/ref-1337.md
references/ref-1338.md
references/ref-1339.md
references/ref-134.md
references/ref-1340.md
references/ref-1341.md
references/ref-1342.md
references/ref-1343.md
references/ref-1344.md
references/ref-1345.md
references/ref-1346.md
references/ref-1347.md
references/ref-1348.md
references/ref-1349.md
references/ref-135.md
references/ref-1350.md
references/ref-1351.md
references/ref-1352.md
references/ref-1353.md
references/ref-1354.md
references/ref-1355.md
references/ref-1356.md
references/ref-1357.md
references/ref-1358.md
references/ref-1359.md
references/ref-136.md
references/ref-1360.md
references/ref-1361.md
references/ref-1362.md
references/ref-1363.md
references/ref-1364.md
references/ref-1365.md
references/ref-1366.md
references/ref-1367.md
references/ref-1368.md
references/ref-1369.md
references/ref-137.md
references/ref-1370.md
references/ref-1371.md
references/ref-1372.md
references/ref-1373.md
references/ref-1374.md
references/ref-1375.md
references/ref-1376.md
references/ref-1377.md
references/ref-1378.md
references/ref-1379.md
references/ref-138.md
references/ref-1380.md
references/ref-1381.md
references/ref-1382.md
references/ref-1383.md
references/ref-1384.md
references/ref-1385.md
references/ref-1386.md
references/ref-1387.md
references/ref-1388.md
references/ref-1389.md
references/ref-139.md
references/ref-1390.md
references/ref-1391.md
references/ref-1392.md
references/ref-1393.md
references/ref-1394.md
references/ref-1395.md
references/ref-1396.md
references/ref-1397.md
references/ref-1398.md
references/ref-1399.md
references/ref-140.md
references/ref-1400.md
references/ref-1401.md
references/ref-1402.md
references/ref-1403.md
references/ref-1404.md
references/ref-1405.md
references/ref-1406.md
references/ref-1407.md
references/ref-1408.md
references/ref-1409.md
references/ref-141.md
references/ref-1410.md
references/ref-1411.md
references/ref-1412.md
references/ref-1413.md
references/ref-1414.md
references/ref-1415.md
references/ref-1416.md
references/ref-1417.md
references/ref-1418.md
references/ref-1419.md
references/ref-142.md
references/ref-1420.md
references/ref-1421.md
references/ref-1422.md
references/ref-1423.md
references/ref-1424.md
references/ref-1425.md
references/ref-1426.md
references/ref-1427.md
references/ref-1428.md
references/ref-1429.md
references/ref-143.md
references/ref-1430.md
references/ref-1431.md
references/ref-1432.md
references/ref-1433.md
references/ref-1434.md
references/ref-1435.md
references/ref-1436.md
references/ref-1437.md
references/ref-1438.md
references/ref-1439.md
references/ref-144.md
references/ref-1440.md
references/ref-1441.md
references/ref-1442.md
references/ref-1443.md
references/ref-1444.md
references/ref-1445.md
references/ref-1446.md
references/ref-1447.md
references/ref-1448.md
references/ref-1449.md
references/ref-145.md
references/ref-1450.md
references/ref-1451.md
references/ref-1452.md
references/ref-1453.md
references/ref-1454.md
references/ref-1455.md
references/ref-1456.md
references/ref-1457.md
references/ref-1458.md
references/ref-1459.md
references/ref-146.md
references/ref-1460.md
references/ref-1461.md
references/ref-1462.md
references/ref-1463.md
references/ref-1464.md
references/ref-1465.md
references/ref-1466.md
references/ref-1467.md
references/ref-1468.md
references/ref-1469.md
references/ref-147.md
references/ref-1470.md
references/ref-1471.md
references/ref-1472.md
references/ref-1473.md
references/ref-1474.md
references/ref-1475.md
references/ref-1476.md
references/ref-1477.md
references/ref-1478.md
references/ref-1479.md
references/ref-148.md
references/ref-1480.md
references/ref-1481.md
references/ref-1482.md
references/ref-1483.md
references/ref-1484.md
references/ref-1485.md
references/ref-1486.md
references/ref-149.md
references/ref-150.md
references/ref-151.md
references/ref-152.md
references/ref-153.md
references/ref-154.md
references/ref-155.md
references/ref-156.md
references/ref-157.md
references/ref-158.md
references/ref-159.md
references/ref-160.md
references/ref-161.md
references/ref-162.md
references/ref-163.md
references/ref-164.md
references/ref-165.md
references/ref-166.md
references/ref-167.md
references/ref-168.md
references/ref-169.md
references/ref-170.md
references/ref-171.md
references/ref-172.md
references/ref-173.md
references/ref-174.md
references/ref-175.md
references/ref-176.md
references/ref-177.md
references/ref-178.md
references/ref-179.md
references/ref-180.md
references/ref-181.md
references/ref-182.md
references/ref-183.md
references/ref-184.md
references/ref-185.md
references/ref-186.md
references/ref-187.md
references/ref-188.md
references/ref-189.md
references/ref-190.md
references/ref-191.md
references/ref-192.md
references/ref-193.md
references/ref-194.md
references/ref-195.md
references/ref-196.md
references/ref-197.md
references/ref-198.md
references/ref-199.md
references/ref-200.md
references/ref-201.md
references/ref-202.md
references/ref-203.md
references/ref-204.md
references/ref-205.md
references/ref-206.md
references/ref-207.md
references/ref-208.md
references/ref-209.md
references/ref-210.md
references/ref-211.md
references/ref-212.md
references/ref-213.md
references/ref-214.md
references/ref-215.md
references/ref-216.md
references/ref-217.md
references/ref-218.md
references/ref-219.md
references/ref-220.md
references/ref-221.md
references/ref-222.md
references/ref-223.md
references/ref-224.md
references/ref-225.md
references/ref-226.md
references/ref-227.md
references/ref-228.md
references/ref-229.md
references/ref-230.md
references/ref-231.md
references/ref-232.md
references/ref-233.md
references/ref-234.md
references/ref-235.md
references/ref-236.md
references/ref-237.md
references/ref-238.md
references/ref-239.md
references/ref-240.md
references/ref-241.md
references/ref-242.md
references/ref-243.md
references/ref-244.md
references/ref-245.md
references/ref-246.md
references/ref-247.md
references/ref-248.md
references/ref-249.md
references/ref-250.md
references/ref-251.md
references/ref-252.md
references/ref-253.md
references/ref-254.md
references/ref-255.md
references/ref-256.md
references/ref-257.md
references/ref-258.md
references/ref-259.md
references/ref-260.md
references/ref-261.md
references/ref-262.md
references/ref-263.md
references/ref-264.md
references/ref-265.md
references/ref-266.md
references/ref-267.md
references/ref-268.md
references/ref-269.md
references/ref-270.md
references/ref-271.md
references/ref-272.md
references/ref-273.md
references/ref-274.md
references/ref-275.md
references/ref-276.md
references/ref-277.md
references/ref-278.md
references/ref-279.md
references/ref-280.md
references/ref-281.md
references/ref-282.md
references/ref-283.md
references/ref-284.md
references/ref-285.md
references/ref-286.md
references/ref-287.md
references/ref-288.md
references/ref-289.md
references/ref-290.md
references/ref-291.md
references/ref-292.md
references/ref-293.md
references/ref-294.md
references/ref-295.md
references/ref-296.md
references/ref-297.md
references/ref-298.md
references/ref-299.md
references/ref-300.md
references/ref-301.md
references/ref-302.md
references/ref-303.md
references/ref-304.md
references/ref-305.md
references/ref-306.md
references/ref-307.md
references/ref-308.md
references/ref-309.md
references/ref-310.md
references/ref-311.md
references/ref-312.md
references/ref-313.md
references/ref-314.md
references/ref-315.md
references/ref-316.md
references/ref-317.md
references/ref-318.md
references/ref-319.md
references/ref-320.md
references/ref-321.md
references/ref-322.md
references/ref-323.md
references/ref-324.md
references/ref-325.md
references/ref-326.md
references/ref-327.md
references/ref-328.md
references/ref-329.md
references/ref-330.md
references/ref-331.md
references/ref-332.md
references/ref-333.md
references/ref-334.md
references/ref-335.md
references/ref-336.md
references/ref-337.md
references/ref-338.md
references/ref-339.md
references/ref-340.md
references/ref-341.md
references/ref-342.md
references/ref-343.md
references/ref-344.md
references/ref-345.md
references/ref-346.md
references/ref-347.md
references/ref-348.md
references/ref-349.md
references/ref-350.md
references/ref-351.md
references/ref-352.md
references/ref-353.md
references/ref-354.md
references/ref-355.md
references/ref-356.md
references/ref-357.md
references/ref-358.md
references/ref-359.md
references/ref-360.md
references/ref-361.md
references/ref-362.md
references/ref-363.md
references/ref-364.md
references/ref-365.md
references/ref-366.md
references/ref-367.md
references/ref-368.md
references/ref-369.md
references/ref-370.md
references/ref-371.md
references/ref-372.md
references/ref-373.md
references/ref-374.md
references/ref-375.md
references/ref-376.md
references/ref-377.md
references/ref-378.md
references/ref-379.md
references/ref-380.md
references/ref-381.md
references/ref-382.md
references/ref-383.md
references/ref-384.md
references/ref-385.md
references/ref-386.md
references/ref-387.md
references/ref-388.md
references/ref-389.md
references/ref-390.md
references/ref-391.md
references/ref-392.md
references/ref-393.md
references/ref-394.md
references/ref-395.md
references/ref-396.md
references/ref-397.md
references/ref-398.md
references/ref-399.md
references/ref-400.md
references/ref-401.md
references/ref-402.md
references/ref-403.md
references/ref-404.md
references/ref-405.md
references/ref-406.md
references/ref-407.md
references/ref-408.md
references/ref-409.md
references/ref-410.md
references/ref-411.md
references/ref-412.md
references/ref-413.md
references/ref-414.md
references/ref-415.md
references/ref-416.md
references/ref-417.md
references/ref-418.md
references/ref-419.md
references/ref-420.md
references/ref-421.md
references/ref-422.md
references/ref-423.md
references/ref-424.md
references/ref-425.md
references/ref-426.md
references/ref-427.md
references/ref-428.md
references/ref-429.md
references/ref-430.md
references/ref-431.md
references/ref-432.md
references/ref-433.md
references/ref-434.md
references/ref-435.md
references/ref-436.md
references/ref-437.md
references/ref-438.md
references/ref-439.md
references/ref-440.md
references/ref-441.md
references/ref-442.md
references/ref-443.md
references/ref-444.md
references/ref-445.md
references/ref-446.md
references/ref-447.md
references/ref-448.md
references/ref-449.md
references/ref-450.md
references/ref-451.md
references/ref-452.md
references/ref-453.md
references/ref-454.md
references/ref-455.md
references/ref-456.md
references/ref-457.md
references/ref-458.md
references/ref-459.md
references/ref-460.md
references/ref-461.md
references/ref-462.md
references/ref-463.md
references/ref-464.md
references/ref-465.md
references/ref-466.md
references/ref-467.md
references/ref-468.md
references/ref-469.md
references/ref-470.md
references/ref-471.md
references/ref-472.md
references/ref-473.md
references/ref-474.md
references/ref-475.md
references/ref-476.md
references/ref-477.md
references/ref-478.md
references/ref-479.md
references/ref-480.md
references/ref-481.md
references/ref-482.md
references/ref-483.md
references/ref-484.md
references/ref-485.md
references/ref-486.md
references/ref-487.md
references/ref-488.md
references/ref-489.md
references/ref-490.md
references/ref-491.md
references/ref-492.md
references/ref-493.md
references/ref-494.md
references/ref-495.md
references/ref-496.md
references/ref-497.md
references/ref-498.md
references/ref-499.md
references/ref-500.md
references/ref-501.md
references/ref-502.md
references/ref-503.md
references/ref-504.md
references/ref-505.md
references/ref-506.md
references/ref-507.md
references/ref-508.md
references/ref-509.md
references/ref-510.md
references/ref-511.md
references/ref-512.md
references/ref-513.md
references/ref-514.md
references/ref-515.md
references/ref-516.md
references/ref-517.md
references/ref-518.md
references/ref-519.md
references/ref-520.md
references/ref-521.md
references/ref-522.md
references/ref-523.md
references/ref-524.md
references/ref-525.md
references/ref-526.md
references/ref-527.md
references/ref-528.md
references/ref-529.md
references/ref-530.md
references/ref-531.md
references/ref-532.md
references/ref-533.md
references/ref-534.md
references/ref-535.md
references/ref-536.md
references/ref-537.md
references/ref-538.md
references/ref-539.md
references/ref-540.md
references/ref-541.md
references/ref-542.md
references/ref-543.md
references/ref-544.md
references/ref-545.md
references/ref-546.md
references/ref-547.md
references/ref-548.md
references/ref-549.md
references/ref-550.md
references/ref-551.md
references/ref-552.md
references/ref-553.md
references/ref-554.md
references/ref-555.md
references/ref-556.md
references/ref-557.md
references/ref-558.md
references/ref-559.md
references/ref-560.md
references/ref-561.md
references/ref-562.md
references/ref-563.md
references/ref-564.md
references/ref-565.md
references/ref-566.md
references/ref-567.md
references/ref-568.md
references/ref-569.md
references/ref-570.md
references/ref-571.md
references/ref-572.md
references/ref-573.md
references/ref-574.md
references/ref-575.md
references/ref-576.md
references/ref-577.md
references/ref-578.md
references/ref-579.md
references/ref-580.md
references/ref-581.md
references/ref-582.md
references/ref-583.md
references/ref-584.md
references/ref-585.md
references/ref-586.md
references/ref-587.md
references/ref-588.md
references/ref-589.md
references/ref-590.md
references/ref-591.md
references/ref-592.md
references/ref-593.md
references/ref-594.md
references/ref-595.md
references/ref-596.md
references/ref-597.md
references/ref-598.md
references/ref-599.md
references/ref-600.md
references/ref-601.md
references/ref-602.md
references/ref-603.md
references/ref-604.md
references/ref-605.md
references/ref-606.md
references/ref-607.md
references/ref-608.md
references/ref-609.md
references/ref-610.md
references/ref-611.md
references/ref-612.md
references/ref-613.md
references/ref-614.md
references/ref-615.md
references/ref-616.md
references/ref-617.md
references/ref-618.md
references/ref-619.md
references/ref-620.md
references/ref-621.md
references/ref-622.md
references/ref-623.md
references/ref-624.md
references/ref-625.md
references/ref-626.md
references/ref-627.md
references/ref-628.md
references/ref-629.md
references/ref-630.md
references/ref-631.md
references/ref-632.md
references/ref-633.md
references/ref-634.md
references/ref-635.md
references/ref-636.md
references/ref-637.md
references/ref-638.md
references/ref-639.md
references/ref-640.md
references/ref-641.md
references/ref-642.md
references/ref-643.md
references/ref-644.md
references/ref-645.md
references/ref-646.md
references/ref-647.md
references/ref-648.md
references/ref-649.md
references/ref-650.md
references/ref-651.md
references/ref-652.md
references/ref-653.md
references/ref-654.md
references/ref-655.md
references/ref-656.md
references/ref-657.md
references/ref-658.md
references/ref-659.md
references/ref-660.md
references/ref-661.md
references/ref-662.md
references/ref-663.md
references/ref-664.md
references/ref-665.md
references/ref-666.md
references/ref-667.md
references/ref-668.md
references/ref-669.md
references/ref-670.md
references/ref-671.md
references/ref-672.md
references/ref-673.md
references/ref-674.md
references/ref-675.md
references/ref-676.md
references/ref-677.md
references/ref-678.md
references/ref-679.md
references/ref-680.md
references/ref-681.md
references/ref-682.md
references/ref-683.md
references/ref-684.md
references/ref-685.md
references/ref-686.md
references/ref-687.md
references/ref-688.md
references/ref-689.md
references/ref-690.md
references/ref-691.md
references/ref-692.md
references/ref-693.md
references/ref-694.md
references/ref-695.md
references/ref-696.md
references/ref-697.md
references/ref-698.md
references/ref-699.md
references/ref-700.md
references/ref-701.md
references/ref-702.md
references/ref-703.md
references/ref-704.md
references/ref-705.md
references/ref-706.md
references/ref-707.md
references/ref-708.md
references/ref-709.md
references/ref-710.md
references/ref-711.md
references/ref-712.md
references/ref-713.md
references/ref-714.md
references/ref-715.md
references/ref-716.md
references/ref-717.md
references/ref-718.md
references/ref-719.md
references/ref-720.md
references/ref-721.md
references/ref-722.md
references/ref-723.md
references/ref-724.md
references/ref-725.md
references/ref-726.md
references/ref-727.md
references/ref-728.md
references/ref-729.md
references/ref-730.md
references/ref-731.md
references/ref-732.md
references/ref-733.md
references/ref-734.md
references/ref-735.md
references/ref-736.md
references/ref-737.md
references/ref-738.md
references/ref-739.md
references/ref-740.md
references/ref-741.md
references/ref-742.md
references/ref-743.md
references/ref-744.md
references/ref-745.md
references/ref-746.md
references/ref-747.md
references/ref-748.md
references/ref-749.md
references/ref-750.md
references/ref-751.md
references/ref-752.md
references/ref-753.md
references/ref-754.md
references/ref-755.md
references/ref-756.md
references/ref-757.md
references/ref-758.md
references/ref-759.md
references/ref-760.md
references/ref-761.md
references/ref-762.md
references/ref-763.md
references/ref-764.md
references/ref-765.md
references/ref-766.md
references/ref-767.md
references/ref-768.md
references/ref-769.md
references/ref-770.md
references/ref-771.md
references/ref-772.md
references/ref-773.md
references/ref-774.md
references/ref-775.md
references/ref-776.md
references/ref-777.md
references/ref-778.md
references/ref-779.md
references/ref-780.md
references/ref-781.md
references/ref-782.md
references/ref-783.md
references/ref-784.md
references/ref-785.md
references/ref-786.md
references/ref-787.md
references/ref-788.md
references/ref-789.md
references/ref-790.md
references/ref-791.md
references/ref-792.md
references/ref-793.md
references/ref-794.md
references/ref-795.md
references/ref-796.md
references/ref-797.md
references/ref-798.md
references/ref-799.md
references/ref-800.md
references/ref-801.md
references/ref-802.md
references/ref-803.md
references/ref-804.md
references/ref-805.md
references/ref-806.md
references/ref-807.md
references/ref-808.md
references/ref-809.md
references/ref-810.md
references/ref-811.md
references/ref-812.md
references/ref-813.md
references/ref-814.md
references/ref-815.md
references/ref-816.md
references/ref-817.md
references/ref-818.md
references/ref-819.md
references/ref-820.md
references/ref-821.md
references/ref-822.md
references/ref-823.md
references/ref-824.md
references/ref-825.md
references/ref-826.md
references/ref-827.md
references/ref-828.md
references/ref-829.md
references/ref-830.md
references/ref-831.md
references/ref-832.md
references/ref-833.md
references/ref-834.md
references/ref-835.md
references/ref-836.md
references/ref-837.md
references/ref-838.md
references/ref-839.md
references/ref-840.md
references/ref-841.md
references/ref-842.md
references/ref-843.md
references/ref-844.md
references/ref-845.md
references/ref-846.md
references/ref-847.md
references/ref-848.md
references/ref-849.md
references/ref-850.md
references/ref-851.md
references/ref-852.md
references/ref-853.md
references/ref-854.md
references/ref-855.md
references/ref-856.md
references/ref-857.md
references/ref-858.md
references/ref-859.md
references/ref-860.md
references/ref-861.md
references/ref-862.md
references/ref-863.md
references/ref-864.md
references/ref-865.md
references/ref-866.md
references/ref-867.md
references/ref-868.md
references/ref-869.md
references/ref-870.md
references/ref-871.md
references/ref-872.md
references/ref-873.md
references/ref-874.md
references/ref-875.md
references/ref-876.md
references/ref-877.md
references/ref-878.md
references/ref-879.md
references/ref-880.md
references/ref-881.md
references/ref-882.md
references/ref-883.md
references/ref-884.md
references/ref-885.md
references/ref-886.md
references/ref-887.md
references/ref-888.md
references/ref-889.md
references/ref-890.md
references/ref-891.md
references/ref-892.md
references/ref-893.md
references/ref-894.md
references/ref-895.md
references/ref-896.md
references/ref-897.md
references/ref-898.md
references/ref-899.md
references/ref-900.md
references/ref-901.md
references/ref-902.md
references/ref-903.md
references/ref-904.md
references/ref-905.md
references/ref-906.md
references/ref-907.md
references/ref-908.md
references/ref-909.md
references/ref-910.md
references/ref-911.md
references/ref-912.md
references/ref-913.md
references/ref-914.md
references/ref-915.md
references/ref-916.md
references/ref-917.md
references/ref-918.md
references/ref-919.md
references/ref-920.md
references/ref-921.md
references/ref-922.md
references/ref-923.md
references/ref-924.md
references/ref-925.md
references/ref-926.md
references/ref-927.md
references/ref-928.md
references/ref-929.md
references/ref-930.md
references/ref-931.md
references/ref-932.md
references/ref-933.md
references/ref-934.md
references/ref-935.md
references/ref-936.md
references/ref-937.md
references/ref-938.md
references/ref-939.md
references/ref-940.md
references/ref-941.md
references/ref-942.md
references/ref-943.md
references/ref-944.md
references/ref-945.md
references/ref-946.md
references/ref-947.md
references/ref-948.md
references/ref-949.md
references/ref-950.md
references/ref-951.md
references/ref-952.md
references/ref-953.md
references/ref-954.md
references/ref-955.md
references/ref-956.md
references/ref-957.md
references/ref-958.md
references/ref-959.md
references/ref-960.md
references/ref-961.md
references/ref-962.md
references/ref-963.md
references/ref-964.md
references/ref-965.md
references/ref-966.md
references/ref-967.md
references/ref-968.md
references/ref-969.md
references/ref-970.md
references/ref-971.md
references/ref-972.md
references/ref-973.md
references/ref-974.md
references/ref-975.md
references/ref-976.md
references/ref-977.md
references/ref-978.md
references/ref-979.md
references/ref-980.md
references/ref-981.md
references/ref-982.md
references/ref-983.md
references/ref-984.md
references/ref-985.md
references/ref-986.md
references/ref-987.md
references/ref-988.md
references/ref-989.md
references/ref-990.md
references/ref-991.md
references/ref-992.md
references/ref-993.md
references/ref-994.md
references/ref-995.md
references/ref-996.md
references/ref-997.md
references/ref-998.md
references/ref-999.md
site-matrix.md
standards/index.md
topics/2026/2026-09-25-area01-s11.md
topics/2026/2026-09-25-area01-s3.md
topics/2026/2026-09-25-area01-s4.md
topics/2026/2026-09-25-area01-s6.md
topics/2026/2026-09-25-area01-s7.md
topics/2026/2026-09-25-area01-s8.md
topics/2026/2026-09-25-area02-s10.md
topics/2026/2026-09-25-area02-s11.md
topics/2026/2026-09-25-area02-s4.md
topics/2026/2026-09-25-area02-s6.md
topics/2026/2026-09-25-area02-s7.md
topics/2026/2026-09-25-area02-s8.md
topics/2026/2026-09-25-area03-s11.md
topics/2026/2026-09-25-area03-s6.md
topics/2026/2026-09-25-area03-s7.md
topics/2026/2026-09-25-area03-s8.md
topics/2026/2026-09-25-area04-s11.md
topics/2026/2026-09-25-area04-s4.md
topics/2026/2026-09-25-area04-s6.md
topics/2026/2026-09-25-area04-s7.md
topics/2026/2026-09-25-area04-s8.md
topics/2026/2026-09-25-area05-s4.md
topics/2026/2026-09-25-area05-s6.md
topics/2026/2026-09-25-area05-s7.md
topics/2026/2026-09-25-area05-s8.md
topics/2026/2026-09-25-area06-s10.md
topics/2026/2026-09-25-area06-s3.md
topics/2026/2026-09-25-area06-s4.md
topics/2026/2026-09-25-area06-s6.md
topics/2026/2026-09-25-area06-s7.md
topics/2026/2026-09-25-area06-s8.md
topics/2026/2026-09-25-area07-s6.md
topics/2026/2026-09-25-area07-s7.md
topics/2026/2026-09-25-area08-s10.md
topics/2026/2026-09-25-area08-s11.md
topics/2026/2026-09-25-area08-s3.md
topics/2026/2026-09-25-area08-s4.md
topics/2026/2026-09-25-area08-s6.md
topics/2026/2026-09-25-area08-s7.md
topics/2026/2026-09-25-area08-s8.md
topics/2026/2026-09-25-area09-s10.md
topics/2026/2026-09-25-area09-s11.md
topics/2026/2026-09-25-area09-s4.md
topics/2026/2026-09-25-area09-s6.md
topics/2026/2026-09-25-area09-s7.md
topics/2026/2026-09-25-area09-s8.md
topics/2026/2026-09-25-area10-s10.md
topics/2026/2026-09-25-area10-s11.md
topics/2026/2026-09-25-area10-s4.md
topics/2026/2026-09-25-area10-s7.md
topics/2026/2026-09-25-area10-s8.md
topics/2026/2026-09-25-area11-s10.md
topics/2026/2026-09-25-area11-s4.md
topics/2026/2026-09-25-area11-s6.md
topics/2026/2026-09-25-area11-s7.md
topics/2026/2026-09-25-area11-s8.md
topics/2026/2026-09-25-area12-s11.md
topics/2026/2026-09-25-area12-s4.md
topics/2026/2026-09-25-area12-s6.md
topics/2026/2026-09-25-area12-s7.md
topics/2026/2026-09-25-area12-s8.md
topics/2026/2026-09-25-area13-s11.md
topics/2026/2026-09-25-area13-s4.md
topics/2026/2026-09-25-area13-s6.md
topics/2026/2026-09-25-area13-s7.md
topics/2026/2026-09-25-area13-s8.md
topics/2026/2026-09-25-area14-s11.md
topics/2026/2026-09-25-area14-s4.md
topics/2026/2026-09-25-area14-s6.md
topics/2026/2026-09-25-area14-s8.md
topics/2026/2026-09-25-area15-s3.md
topics/2026/2026-09-25-area15-s4.md
topics/2026/2026-09-25-area15-s6.md
topics/2026/2026-09-25-area15-s7.md
topics/2026/2026-09-25-area15-s8.md
topics/2026/2026-09-25-area16-s11.md
topics/2026/2026-09-25-area16-s4.md
topics/2026/2026-09-25-area16-s6.md
topics/2026/2026-09-25-area16-s7.md
topics/2026/2026-09-25-area16-s8.md
topics/2026/2026-09-25-area17-s10.md
topics/2026/2026-09-25-area17-s11.md
topics/2026/2026-09-25-area17-s4.md
topics/2026/2026-09-25-area17-s6.md
topics/2026/2026-09-25-area17-s7.md
topics/2026/2026-09-25-area17-s8.md
topics/2026/2026-09-25-area18-s4.md
topics/2026/2026-09-25-area18-s6.md
topics/2026/2026-09-25-area18-s7.md
topics/2026/2026-09-25-area18-s8.md
topics/2026/2026-09-25-area19-s11.md
topics/2026/2026-09-25-area19-s4.md
topics/2026/2026-09-25-area19-s6.md
topics/2026/2026-09-25-area19-s7.md
topics/2026/2026-09-25-area19-s8.md
topics/2026/2026-09-25-area20-s10.md
topics/2026/2026-09-25-area20-s11.md
topics/2026/2026-09-25-area20-s4.md
topics/2026/2026-09-25-area20-s6.md
topics/2026/2026-09-25-area20-s7.md
topics/2026/2026-09-25-area21-s4.md
topics/2026/2026-09-25-area21-s6.md
topics/2026/2026-09-25-area21-s7.md
topics/2026/2026-09-25-area21-s8.md
topics/2026/2026-09-25-area22-s10.md
topics/2026/2026-09-25-area22-s4.md
topics/2026/2026-09-25-area22-s6.md
topics/2026/2026-09-25-area22-s7.md
topics/2026/2026-09-25-area22-s8.md
topics/2026/2026-09-25-area23-s10.md
topics/2026/2026-09-25-area23-s11.md
topics/2026/2026-09-25-area23-s4.md
topics/2026/2026-09-25-area23-s6.md
topics/2026/2026-09-25-area23-s7.md
topics/2026/2026-09-25-area24-s10.md
topics/2026/2026-09-25-area24-s3.md
topics/2026/2026-09-25-area24-s4.md
topics/2026/2026-09-25-area24-s6.md
topics/2026/2026-09-25-area24-s7.md
topics/2026/2026-09-25-area25-s11.md
topics/2026/2026-09-25-area25-s3.md
topics/2026/2026-09-25-area25-s6.md
topics/2026/2026-09-25-area25-s7.md
topics/2026/2026-09-25-area25-s8.md
topics/2026/2026-09-25-area26-s10.md
topics/2026/2026-09-25-area26-s11.md
topics/2026/2026-09-25-area26-s3.md
topics/2026/2026-09-25-area26-s4.md
topics/2026/2026-09-25-area26-s6.md
topics/2026/2026-09-25-area26-s7.md
topics/2026/2026-09-25-area26-s8.md
topics/2026/2026-09-25-area27-s10.md
topics/2026/2026-09-25-area27-s4.md
topics/2026/2026-09-25-area27-s6.md
topics/2026/2026-09-25-area27-s7.md
topics/2026/2026-09-25-area27-s8.md
topics/2026/2026-09-25-area28-s11.md
topics/2026/2026-09-25-area28-s3.md
topics/2026/2026-09-25-area28-s4.md
topics/2026/2026-09-25-area28-s6.md
topics/2026/2026-09-25-area28-s7.md
topics/2026/2026-09-25-epcis-event-design-for-robot-handover.md
topics/2026/2026-09-25-robot-load-reporting-handover-confirmation.md
topics/2026/2026-09-26-area04-s10.md
topics/2026/2026-09-26-area25-s7.md
topics/2026/2026-09-29-area01-s10.md
topics/2026/2026-09-29-area01-s11.md
topics/2026/2026-09-29-area01-s3.md
topics/2026/2026-09-29-area01-s4.md
topics/2026/2026-09-29-area01-s6.md
topics/2026/2026-09-29-area01-s7.md
topics/2026/2026-09-29-area01-s8.md
topics/2026/2026-09-29-area04-s10.md
topics/2026/2026-09-29-area04-s11.md
topics/2026/2026-09-29-area04-s3.md
topics/2026/2026-09-29-area04-s4.md
topics/2026/2026-09-29-area04-s6.md
topics/2026/2026-09-29-area04-s7.md
topics/2026/2026-09-29-area04-s8.md
topics/2026/2026-09-29-area06-s10.md
topics/2026/2026-09-29-area06-s11.md
topics/2026/2026-09-29-area06-s3.md
topics/2026/2026-09-29-area06-s4.md
topics/2026/2026-09-29-area06-s6.md
topics/2026/2026-09-29-area06-s7.md
topics/2026/2026-09-29-area06-s8.md
topics/2026/2026-09-29-area07-s10.md
topics/2026/2026-09-29-area07-s11.md
topics/2026/2026-09-29-area07-s3.md
topics/2026/2026-09-29-area07-s4.md
topics/2026/2026-09-29-area07-s6.md
topics/2026/2026-09-29-area07-s7.md
topics/2026/2026-09-29-area07-s8.md
topics/2026/2026-09-29-area08-s10.md
topics/2026/2026-09-29-area08-s11.md
topics/2026/2026-09-29-area08-s3.md
topics/2026/2026-09-29-area08-s4.md
topics/2026/2026-09-29-area08-s6.md
topics/2026/2026-09-29-area08-s7.md
topics/2026/2026-09-29-area08-s8.md
topics/2026/2026-09-29-area09-s10.md
topics/2026/2026-09-29-area09-s11.md
topics/2026/2026-09-29-area09-s3.md
topics/2026/2026-09-29-area09-s4.md
topics/2026/2026-09-29-area09-s6.md
topics/2026/2026-09-29-area09-s7.md
topics/2026/2026-09-29-area09-s8.md
topics/2026/2026-09-29-area10-s10.md
topics/2026/2026-09-29-area10-s11.md
topics/2026/2026-09-29-area10-s3.md
topics/2026/2026-09-29-area10-s4.md
topics/2026/2026-09-29-area10-s6.md
topics/2026/2026-09-29-area10-s7.md
topics/2026/2026-09-29-area10-s8.md
topics/2026/2026-09-29-area11-s10.md
topics/2026/2026-09-29-area11-s11.md
topics/2026/2026-09-29-area11-s3.md
topics/2026/2026-09-29-area11-s4.md
topics/2026/2026-09-29-area11-s6.md
topics/2026/2026-09-29-area11-s7.md
topics/2026/2026-09-29-area11-s8.md
topics/2026/2026-09-29-area12-s10.md
topics/2026/2026-09-29-area12-s11.md
topics/2026/2026-09-29-area12-s3.md
topics/2026/2026-09-29-area12-s4.md
topics/2026/2026-09-29-area12-s6.md
topics/2026/2026-09-29-area12-s7.md
topics/2026/2026-09-29-area12-s8.md
topics/2026/2026-09-29-area13-s10.md
topics/2026/2026-09-29-area13-s11.md
topics/2026/2026-09-29-area13-s3.md
topics/2026/2026-09-29-area13-s4.md
topics/2026/2026-09-29-area13-s6.md
topics/2026/2026-09-29-area13-s7.md
topics/2026/2026-09-29-area13-s8.md
topics/2026/2026-09-29-area61-s10.md
topics/2026/2026-09-29-area61-s11.md
topics/2026/2026-09-29-area61-s3.md
topics/2026/2026-09-29-area61-s4.md
topics/2026/2026-09-29-area61-s6.md
topics/2026/2026-09-29-area61-s7.md
topics/2026/2026-09-29-area61-s8.md
topics/2026/2026-09-29-area62-s10.md
topics/2026/2026-09-29-area62-s11.md
topics/2026/2026-09-29-area62-s3.md
topics/2026/2026-09-29-area62-s4.md
topics/2026/2026-09-29-area62-s6.md
topics/2026/2026-09-29-area62-s7.md
topics/2026/2026-09-29-area62-s8.md
topics/2026/2026-09-29-area63-s10.md
topics/2026/2026-09-29-area63-s11.md
topics/2026/2026-09-29-area63-s3.md
topics/2026/2026-09-29-area63-s4.md
topics/2026/2026-09-29-area63-s6.md
topics/2026/2026-09-29-area63-s7.md
topics/2026/2026-09-29-area63-s8.md
topics/2026/2026-09-29-area64-s10.md
topics/2026/2026-09-29-area64-s11.md
topics/2026/2026-09-29-area64-s3.md
topics/2026/2026-09-29-area64-s4.md
topics/2026/2026-09-29-area64-s6.md
topics/2026/2026-09-29-area64-s7.md
topics/2026/2026-09-29-area64-s8.md
topics/2026/2026-09-29-area65-s10.md
topics/2026/2026-09-29-area65-s11.md
topics/2026/2026-09-29-area65-s3.md
topics/2026/2026-09-29-area65-s4.md
topics/2026/2026-09-29-area65-s6.md
topics/2026/2026-09-29-area65-s7.md
topics/2026/2026-09-29-area65-s8.md
topics/2026/2026-09-30-area02-s10.md
topics/2026/2026-09-30-area02-s11.md
topics/2026/2026-09-30-area02-s3.md
topics/2026/2026-09-30-area02-s4.md
topics/2026/2026-09-30-area02-s6.md
topics/2026/2026-09-30-area02-s7.md
topics/2026/2026-09-30-area02-s8.md
topics/2026/2026-09-30-area03-s10.md
topics/2026/2026-09-30-area03-s11.md
topics/2026/2026-09-30-area03-s3.md
topics/2026/2026-09-30-area03-s4.md
topics/2026/2026-09-30-area03-s6.md
topics/2026/2026-09-30-area03-s7.md
topics/2026/2026-09-30-area03-s8.md
topics/2026/2026-09-30-area14-s10.md
topics/2026/2026-09-30-area14-s11.md
topics/2026/2026-09-30-area14-s3.md
topics/2026/2026-09-30-area14-s4.md
topics/2026/2026-09-30-area14-s6.md
topics/2026/2026-09-30-area14-s8.md
topics/2026/2026-09-30-area16-s10.md
topics/2026/2026-09-30-area16-s11.md
topics/2026/2026-09-30-area16-s4.md
topics/2026/2026-09-30-area16-s6.md
topics/2026/2026-09-30-area16-s7.md
topics/2026/2026-09-30-area16-s8.md
topics/2026/2026-09-30-area19-s10.md
topics/2026/2026-09-30-area19-s11.md
topics/2026/2026-09-30-area19-s3.md
topics/2026/2026-09-30-area19-s4.md
topics/2026/2026-09-30-area19-s6.md
topics/2026/2026-09-30-area19-s7.md
topics/2026/2026-09-30-area19-s8.md
topics/2026/2026-09-30-area33-s10.md
topics/2026/2026-09-30-area33-s11.md
topics/2026/2026-09-30-area33-s3.md
topics/2026/2026-09-30-area33-s4.md
topics/2026/2026-09-30-area33-s6.md
topics/2026/2026-09-30-area33-s7.md
topics/2026/2026-09-30-area33-s8.md
topics/2026/2026-09-30-area36-s10.md
topics/2026/2026-09-30-area36-s11.md
topics/2026/2026-09-30-area36-s3.md
topics/2026/2026-09-30-area36-s4.md
topics/2026/2026-09-30-area36-s6.md
topics/2026/2026-09-30-area36-s7.md
topics/2026/2026-09-30-area36-s8.md
topics/2026/2026-09-30-area37-s10.md
topics/2026/2026-09-30-area37-s4.md
topics/2026/2026-09-30-area37-s6.md
topics/2026/2026-09-30-area37-s8.md
topics/2026/2026-09-30-area40-s10.md
topics/2026/2026-09-30-area40-s11.md
topics/2026/2026-09-30-area40-s3.md
topics/2026/2026-09-30-area40-s4.md
topics/2026/2026-09-30-area40-s6.md
topics/2026/2026-09-30-area40-s7.md
topics/2026/2026-09-30-area40-s8.md
topics/2026/2026-09-30-area41-s10.md
topics/2026/2026-09-30-area41-s11.md
topics/2026/2026-09-30-area41-s3.md
topics/2026/2026-09-30-area41-s4.md
topics/2026/2026-09-30-area41-s6.md
topics/2026/2026-09-30-area41-s7.md
topics/2026/2026-09-30-area41-s8.md
topics/2026/2026-09-30-area43-s10.md
topics/2026/2026-09-30-area43-s11.md
topics/2026/2026-09-30-area43-s3.md
topics/2026/2026-09-30-area43-s4.md
topics/2026/2026-09-30-area43-s6.md
topics/2026/2026-09-30-area43-s7.md
topics/2026/2026-09-30-area44-s10.md
topics/2026/2026-09-30-area44-s11.md
topics/2026/2026-09-30-area44-s3.md
topics/2026/2026-09-30-area44-s4.md
topics/2026/2026-09-30-area44-s6.md
topics/2026/2026-09-30-area44-s7.md
topics/2026/2026-09-30-area44-s8.md
topics/2026/2026-09-30-area45-s10.md
topics/2026/2026-09-30-area45-s11.md
topics/2026/2026-09-30-area45-s3.md
topics/2026/2026-09-30-area45-s4.md
topics/2026/2026-09-30-area45-s6.md
topics/2026/2026-09-30-area45-s7.md
topics/2026/2026-09-30-area45-s8.md
topics/2026/2026-09-30-area46-s10.md
topics/2026/2026-09-30-area46-s11.md
topics/2026/2026-09-30-area46-s3.md
topics/2026/2026-09-30-area46-s4.md
topics/2026/2026-09-30-area46-s6.md
topics/2026/2026-09-30-area46-s7.md
topics/2026/2026-09-30-area46-s8.md
topics/2026/2026-09-30-area49-s10.md
topics/2026/2026-09-30-area49-s11.md
topics/2026/2026-09-30-area49-s3.md
topics/2026/2026-09-30-area49-s4.md
topics/2026/2026-09-30-area49-s6.md
topics/2026/2026-09-30-area49-s7.md
topics/2026/2026-09-30-area49-s8.md
topics/2026/2026-09-30-area50-s10.md
topics/2026/2026-09-30-area50-s11.md
topics/2026/2026-09-30-area50-s3.md
topics/2026/2026-09-30-area50-s4.md
topics/2026/2026-09-30-area50-s6.md
topics/2026/2026-09-30-area50-s7.md
topics/2026/2026-09-30-area50-s8.md
topics/2026/2026-09-30-area52-s10.md
topics/2026/2026-09-30-area52-s11.md
topics/2026/2026-09-30-area52-s3.md
topics/2026/2026-09-30-area52-s4.md
topics/2026/2026-09-30-area52-s6.md
topics/2026/2026-09-30-area52-s8.md
topics/2026/2026-09-30-area53-s10.md
topics/2026/2026-09-30-area53-s11.md
topics/2026/2026-09-30-area53-s3.md
topics/2026/2026-09-30-area53-s4.md
topics/2026/2026-09-30-area53-s6.md
topics/2026/2026-09-30-area53-s7.md
topics/2026/2026-09-30-area53-s8.md
topics/2026/2026-09-30-area56-s10.md
topics/2026/2026-09-30-area56-s11.md
topics/2026/2026-09-30-area56-s3.md
topics/2026/2026-09-30-area56-s4.md
topics/2026/2026-09-30-area56-s6.md
topics/2026/2026-09-30-area56-s7.md
topics/2026/2026-09-30-area56-s8.md
topics/2026/2026-09-30-area58-s10.md
topics/2026/2026-09-30-area58-s11.md
topics/2026/2026-09-30-area58-s3.md
topics/2026/2026-09-30-area58-s4.md
topics/2026/2026-09-30-area58-s6.md
topics/2026/2026-09-30-area58-s7.md
topics/2026/2026-09-30-area59-s10.md
topics/2026/2026-09-30-area59-s11.md
topics/2026/2026-09-30-area59-s3.md
topics/2026/2026-09-30-area59-s4.md
topics/2026/2026-09-30-area59-s6.md
topics/2026/2026-09-30-area59-s7.md
topics/2026/2026-09-30-area59-s8.md
topics/2026/2026-09-30-area60-s10.md
topics/2026/2026-09-30-area60-s11.md
topics/2026/2026-09-30-area60-s3.md
topics/2026/2026-09-30-area60-s4.md
topics/2026/2026-09-30-area60-s6.md
topics/2026/2026-09-30-area60-s7.md
topics/2026/2026-09-30-area60-s8.md
topics/2026/2026-09-30-area66-s10.md
topics/2026/2026-09-30-area66-s11.md
topics/2026/2026-09-30-area66-s3.md
topics/2026/2026-09-30-area66-s4.md
topics/2026/2026-09-30-area66-s6.md
topics/2026/2026-09-30-area66-s7.md
topics/2026/2026-09-30-area66-s8.md
topics/2026/2026-09-30-area67-s10.md
topics/2026/2026-09-30-area67-s11.md
topics/2026/2026-09-30-area67-s3.md
topics/2026/2026-09-30-area67-s4.md
topics/2026/2026-09-30-area67-s6.md
topics/2026/2026-09-30-area67-s7.md
topics/2026/2026-09-30-area67-s8.md
topics/2026/2026-10-09-area18-s10.md
topics/2026/2026-10-09-area18-s11.md
topics/2026/2026-10-09-area18-s6.md
topics/2026/2026-10-09-area18-s7.md
topics/2026/2026-10-09-area18-s8.md
topics/2026/2026-10-09-area19-s10.md
topics/2026/2026-10-09-area19-s11.md
topics/2026/2026-10-09-area19-s6.md
topics/2026/2026-10-09-area19-s7.md
topics/2026/2026-10-09-area19-s8.md
topics/2026/2026-10-09-area33-s10.md
topics/2026/2026-10-09-area33-s11.md
topics/2026/2026-10-09-area33-s3.md
topics/2026/2026-10-09-area33-s6.md
topics/2026/2026-10-09-area33-s7.md
topics/2026/2026-10-09-area33-s8.md
topics/2026/2026-10-09-area37-s11.md
topics/2026/2026-10-09-area37-s3.md
topics/2026/2026-10-09-area37-s7.md
topics/2026/2026-10-09-area38-s10.md
topics/2026/2026-10-09-area38-s11.md
topics/2026/2026-10-09-area38-s3.md
topics/2026/2026-10-09-area38-s7.md
topics/2026/2026-10-09-area41-s11.md
topics/2026/2026-10-09-area41-s6.md
topics/2026/2026-10-09-area41-s7.md
topics/2026/2026-10-09-area42-s10.md
topics/2026/2026-10-09-area42-s11.md
topics/2026/2026-10-09-area42-s3.md
topics/2026/2026-10-09-area42-s7.md
topics/2026/2026-10-09-area43-s10.md
topics/2026/2026-10-09-area43-s11.md
topics/2026/2026-10-09-area43-s6.md
topics/2026/2026-10-09-area43-s7.md
topics/2026/2026-10-09-area43-s8.md
topics/2026/2026-10-10-area20-s10.md
topics/2026/2026-10-10-area20-s11.md
topics/2026/2026-10-10-area20-s3.md
topics/2026/2026-10-10-area20-s6.md
topics/2026/2026-10-10-area20-s7.md
topics/2026/2026-10-10-area20-s8.md
topics/2026/2026-10-10-area24-s11.md
topics/2026/2026-10-10-area24-s3.md
topics/2026/2026-10-10-area24-s6.md
topics/2026/2026-10-10-area24-s7.md
topics/2026/2026-10-10-area24-s8.md
topics/2026/2026-10-10-area25-s10.md
topics/2026/2026-10-10-area25-s11.md
topics/2026/2026-10-10-area25-s3.md
topics/2026/2026-10-10-area25-s6.md
topics/2026/2026-10-10-area25-s7.md
topics/2026/2026-10-10-area25-s8.md
topics/2026/2026-10-10-area26-s10.md
topics/2026/2026-10-10-area26-s11.md
topics/2026/2026-10-10-area26-s3.md
topics/2026/2026-10-10-area26-s7.md
topics/2026/2026-10-10-area26-s8.md
topics/2026/2026-10-10-area27-s10.md
topics/2026/2026-10-10-area27-s11.md
topics/2026/2026-10-10-area27-s6.md
topics/2026/2026-10-10-area27-s7.md
topics/2026/2026-10-10-area27-s8.md
topics/2026/2026-10-10-area28-s10.md
topics/2026/2026-10-10-area28-s11.md
topics/2026/2026-10-10-area28-s3.md
topics/2026/2026-10-10-area28-s6.md
topics/2026/2026-10-10-area28-s7.md
topics/2026/2026-10-10-area28-s8.md
topics/2026/2026-10-10-binary-priority-cost-deadline-and-replanning.md
topics/2026/2026-10-10-charging-threshold-charger-lift-evidence.md
topics/2026/2026-10-11-area21-s10.md
topics/2026/2026-10-11-area21-s11.md
topics/2026/2026-10-11-area21-s6.md
topics/2026/2026-10-11-area21-s7.md
topics/2026/2026-10-11-area21-s8.md
topics/2026/2026-10-11-area22-s10.md
topics/2026/2026-10-11-area22-s11.md
topics/2026/2026-10-11-area22-s3.md
topics/2026/2026-10-11-area22-s6.md
topics/2026/2026-10-11-area22-s7.md
topics/2026/2026-10-11-area22-s8.md
topics/2026/2026-10-11-area23-s10.md
topics/2026/2026-10-11-area23-s11.md
topics/2026/2026-10-11-area23-s3.md
topics/2026/2026-10-11-area23-s4.md
topics/2026/2026-10-11-area23-s6.md
topics/2026/2026-10-11-area23-s7.md
topics/2026/2026-10-11-area23-s8.md
topics/2026/2026-10-11-area48-s10.md
topics/2026/2026-10-11-area48-s11.md
topics/2026/2026-10-11-area48-s3.md
topics/2026/2026-10-11-area48-s4.md
topics/2026/2026-10-11-area48-s6.md
topics/2026/2026-10-11-area48-s7.md
topics/2026/2026-10-11-area48-s8.md
topics/2026/2026-10-11-area49-s11.md
topics/2026/2026-10-11-area49-s4.md
topics/2026/2026-10-11-area49-s6.md
topics/2026/2026-10-11-area49-s7.md
topics/2026/2026-10-11-area49-s8.md
topics/2026/2026-10-11-area50-s10.md
topics/2026/2026-10-11-area50-s11.md
topics/2026/2026-10-11-area50-s4.md
topics/2026/2026-10-11-area50-s6.md
topics/2026/2026-10-11-area50-s7.md
topics/2026/2026-10-11-area50-s8.md
topics/index.md
tracks/chat-based-configuration-and-operation/experiments.md
tracks/chat-based-configuration-and-operation/index.md
tracks/chat-based-configuration-and-operation/log.md
tracks/chat-based-configuration-and-operation/question-backlog.md
tracks/chat-based-configuration-and-operation/stage-1-prior-work-and-products.md
tracks/chat-based-configuration-and-operation/stage-10-integrated-verification.md
tracks/chat-based-configuration-and-operation/stage-2-data-and-standards.md
tracks/chat-based-configuration-and-operation/stage-3-implementation-hypothesis.md
tracks/chat-based-configuration-and-operation/stage-4-misinterpretation-safeguards.md
tracks/chat-based-configuration-and-operation/stage-5-verification-and-hypotheses.md
tracks/chat-based-configuration-and-operation/stage-6-chat-map-authoring.md
tracks/chat-based-configuration-and-operation/stage-7-chat-scenario-composition.md
tracks/chat-based-configuration-and-operation/stage-8-chat-robot-configuration.md
tracks/chat-based-configuration-and-operation/stage-9-chat-real-situation-replay.md
tracks/chat-based-configuration-and-operation/task-model-draft.md
tracks/floorplan-recognition/experiments.md
tracks/floorplan-recognition/index.md
tracks/floorplan-recognition/log.md
tracks/floorplan-recognition/question-backlog.md
tracks/floorplan-recognition/space-graph-schema-draft.md
tracks/floorplan-recognition/stage-1-prior-work-and-products.md
tracks/floorplan-recognition/stage-2-data-and-standards.md
tracks/floorplan-recognition/stage-3-implementation-hypothesis.md
tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md
tracks/floorplan-recognition/stage-5-verification-and-hypotheses.md
tracks/manual-capability-ontology/document-type-matrix.md
tracks/manual-capability-ontology/evaluation-and-verification.md
tracks/manual-capability-ontology/experiments.md
tracks/manual-capability-ontology/index.md
tracks/manual-capability-ontology/log.md
tracks/manual-capability-ontology/model-standard-comparison.md
tracks/manual-capability-ontology/ontology-draft.md
tracks/manual-capability-ontology/question-backlog.md
tracks/manual-capability-ontology/stage-1-existing-models-and-standards.md
tracks/manual-capability-ontology/stage-2-document-types.md
tracks/manual-capability-ontology/stage-3-extraction-methods.md
tracks/manual-capability-ontology/stage-4-execution-grounding.md
tracks/manual-capability-ontology/stage-5-completeness-verification.md
tracks/manual-capability-ontology/stage-6-lifecycle-governance.md
tracks/manual-capability-ontology/stage-7-rop-scenarios-and-hypotheses.md
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

### runs/2026-10-12-04/pages.json

```json
{
  "run_id": "2026-10-12-04",
  "outline": [
    {
      "path": "docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 1500,
      "summary": "한국 인공지능기본법 개정 법률(법률 제21311호)은 2026-07-21 시행되었고 제34조 1항 5호가 조치 문서의 작성·보관을 정한다. [사실][^ref-620] EU AI Act 2026-07-27 통합판에서 기계류 규정은 부속서 I Section B 로 옮겨졌고 제2조 2항이 적용 조문을 한정한다. [사실][^ref-1587]",
      "planned_findings": [
        "f40",
        "f41",
        "f45",
        "f47",
        "f48",
        "f49"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 900,
      "summary": "KnowNo 의 등각 예측 보장은 i.i.d. 보정과 정확한 사람 도움 가정에 선다. [사실][^ref-351] MLflow 별칭 재지정은 다음 로딩 때 반영되고, LeRobot 은 정규화 외부화를 호환성 깨짐으로 표시한다. [사실][^ref-1577][^ref-1578]",
      "planned_findings": [
        "f1",
        "f3",
        "f4",
        "f5",
        "f6",
        "f18",
        "f19"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 900,
      "summary": "물류창고 출하 시나리오의 예외·성과 칸에 별칭 반영 시점과 카나리·롤백 연습을 보강하고, 현장 유형 기타(부산 스마트시티) 사례로 LG CNS 바통의 4종 로봇 통합 관제를 벤더 주장으로 둔다. [추정] 벤더 주장[^ref-1584]",
      "planned_findings": [
        "f1",
        "f15",
        "f16",
        "f28",
        "f29",
        "f30",
        "f31"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 2600,
      "summary": "ML Test Score 의 Infra4·6·7 은 자동 승인·거부, 오프라인 시험의 한계와 카나리, 롤백 연습을 권한다. [사실][^ref-625] 장치 업데이트 도구의 배포 중단·롤백 상태와 KnowNo·ACI 의 보장 조건, LWD 의 에피소드 경계 정책 갱신을 더한다.",
      "planned_findings": [
        "f1",
        "f2",
        "f7",
        "f8",
        "f9",
        "f10",
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
        "f23",
        "f24",
        "f25",
        "f26",
        "f27"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 2200,
      "summary": "MLflow v3.1.0 고정 문서, LeRobot v0.6.0·LeRobotDataset v3.0, NIST AI RMF MANAGE 4.1 행을 더하고 AI-Hub 71825 의 판 이력·분할 표기 불일치를 적는다. [사실][^ref-1588] 관련 법 문단을 갱신하고 제43조 4항·제72조 2항은 조문 내용 소개로만 둔다.",
      "planned_findings": [
        "f1",
        "f3",
        "f4",
        "f5",
        "f32",
        "f33",
        "f34",
        "f35",
        "f36",
        "f37",
        "f38",
        "f42",
        "f43",
        "f44",
        "f45",
        "f46",
        "f47",
        "f48",
        "f50"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 700,
      "summary": "KnowNo 학회판의 가정, ML Test Score Infra 항목, 적응형 등각 추론, Learning While Deploying 을 자료로 더한다. [사실][^ref-1583][^ref-1585]",
      "planned_findings": [
        "f14",
        "f15",
        "f16",
        "f18",
        "f19",
        "f20",
        "f21",
        "f22",
        "f24",
        "f25",
        "f26"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 650,
      "summary": "NIST AI RMF MANAGE 4.1 은 배포 후 감시 계획에 사고 대응·복구·변경관리를 넣도록 하는 자율 적용 항목이다. [사실][^ref-1586] 공급자·ROP·현장 운영자 역할 분리와 복구 실패 로봇의 배정 제외는 이 위키의 의견이다.",
      "planned_findings": [
        "f11",
        "f38",
        "f39"
      ]
    },
    {
      "path": "docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 350,
      "summary": "43. 데이터·관측성·배포, 57. 자산·소프트웨어 수명주기 관리, 59. 법·규제·보험·라이선스 연결을 더한다.",
      "planned_findings": []
    },
    {
      "path": "docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md",
      "section": "11. 열린 질문",
      "budget_chars": 1400,
      "summary": "oq-105·oq-106·oq-107 에 id 를 붙이고 부분 근거를 적으며, oq-030 은 oq-356 과 연결하고, 새 질문 4건을 올린다.",
      "planned_findings": [
        "f6",
        "f25",
        "f36",
        "f39"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "차등 갱신: 3절 법·규제 문단 정정(인공지능기본법 개정 법률 2026-07-21 시행·제34조, EU AI Act 2026/1744 개정의 기계류 Section B 이동·제2조 2항), 4·6·7·8절에 갱신 소절 추가(별칭 반영 시점, 배포 묶음 호환성, ML Test Score Infra4·6·7, 배포 중단·롤백 상태, KnowNo·ACI 보장 조건, LWD, AI-Hub 71825, NIST MANAGE 4.1, 제43·72조 조문 소개), 5절 출하 예외·성과 보강과 기타 현장 사례 추가, 9절 배포 후 감시 책임 경계, 10절 연결 3건, 11절 oq id 부여·부분 근거·새 질문 4건, 13절 각주 갱신(신규 12건)",
      "patches": [
        {
          "section": "3. 왜 중요한가",
          "action": "replace",
          "frontmatter": {
            "related_areas": [
              5,
              15,
              21,
              25,
              31,
              38,
              43,
              48,
              54,
              55,
              57,
              59
            ],
            "tags": [
              "LLM 계획 접지",
              "등각 예측",
              "학습 기반 배차",
              "모델 레지스트리",
              "단계적 배포",
              "AI 위험관리"
            ],
            "sources": [
              "ref-617",
              "ref-618",
              "ref-619",
              "ref-620",
              "ref-621",
              "ref-088",
              "ref-092",
              "ref-351",
              "ref-622",
              "ref-623",
              "ref-624",
              "ref-625",
              "ref-626",
              "ref-627",
              "ref-354",
              "ref-359",
              "ref-056",
              "ref-541",
              "ref-417",
              "ref-1577",
              "ref-1578",
              "ref-1579",
              "ref-1580",
              "ref-1581",
              "ref-1582",
              "ref-1583",
              "ref-1584",
              "ref-1585",
              "ref-1586",
              "ref-1587",
              "ref-1588"
            ],
            "last_run": "2026-10-12"
          },
          "content": "AI가 만든 계획·해석을 실행에 쓰는 기준은 한 가지 장치가 아니라 실행 가능성 접지, 형식 명세·계획기 경유 검증, 불확실할 때 사람 확인, 실행 전 안전 판정, 승인된 모델 버전·시험 기준이 겹친 구조로 정리될 수 있어 보인다. [추정][^ref-088][^ref-092][^ref-056][^ref-351][^ref-359][^ref-417][^ref-625][^ref-626][^ref-618] 이 구조는 각 출처가 다루는 서로 다른 단계를 이 위키가 묶은 것이며, 하나의 출처가 제시한 채택 기준은 아니다.\n\n기준이 필요한 이유는 모델이 한 번 넣고 끝나는 부품이 아니기 때문이다. Sculley 외(2015)는 실제 머신러닝(Machine Learning, ML) 시스템이 일반 코드의 유지보수 문제에 더해 경계 침식, 얽힘, 숨은 피드백 루프, 선언되지 않은 소비자, 데이터 의존성 등 ML 고유 위험으로 큰 유지 비용을 낳는다고 지적했다. [사실][^ref-624]\n\n규제도 같은 방향을 가리킨다. 한국 「인공지능 발전과 신뢰 기반 조성 등에 관한 기본법」과 시행령은 2026-01-22 시행되었고, 사람의 생명·안전·기본권에 중대한 영향을 미칠 수 있는 영역의 AI를 고영향 인공지능으로 두어 별도 책무를 부과한다(기준일 2026-01-22). [사실][^ref-620] 개정 법률(법률 제21311호, 2026-01-20 공포)은 2026-07-21 시행되었고, 고영향 영역 목록은 미확인이다. [사실][^ref-620] 현행 제34조 1항은 [고영향 인공지능](../../glossary/high-impact-ai.md)이나 이를 이용한 제품·서비스를 제공하는 인공지능사업자가 대통령령에 따라 안전성·신뢰성 확보 조치를 이행하도록 하고, 그 5호로 조치 내용을 확인할 수 있는 문서의 작성·보관을 둔다. [사실][^ref-620] 이 책무가 작업 계획·배정 AI를 쓰는 ROP에 걸리는지는 고영향 해당성과 사업자 지위(제공자·이용자) 판단이 먼저이며, 시행령상 보존 기간은 이번에 확인하지 못했다. [추정][^ref-620]\n\nEU AI Act(Regulation (EU) 2024/1689)는 위험 기반 규제로, 부속서 I의 EU 조화 법령(기계류 등) 대상 제품의 안전 구성요소이거나 제품 자체이고 제3자 적합성 평가 대상인 AI 시스템을 고위험 AI로 분류한다. [사실][^ref-621] 2026-07-27 EUR-Lex 통합판은 Regulation (EU) 2026/1744(2026-07-08 채택, 관보 2026-07-24 게재) 개정을 반영하며, 이 개정으로 기계류 규정 (EU) 2023/1230이 부속서 I Section A에서 빠지고 Section B(21번)에 들어갔다. [사실][^ref-1587] 개정된 제2조 2항은 Section B 조화 법령 대상 제품과 관련해 제6조 1항으로 고위험이 되는 AI 시스템에는 제6조 1항, 제60a조, 제102~112조만 적용하고, 제57~59조는 해당 법령에 고위험 요구사항이 통합된 범위에서만 적용한다고 정한다. [사실][^ref-1587] 따라서 기계류 규정 대상 로봇의 안전 구성요소로서 고위험이 되는 AI에는 제43조(실질적 변경 시 재평가)와 제72조(시판 후 감시)가 AI Act 조문으로 바로 적용된다고 볼 수 없어 보인다. [추정][^ref-1587] 이는 법률 판단이 아니며, 기계류 규정 (EU) 2023/1230 쪽에 AI 고위험 요구가 어떻게 통합되는지는 확인하지 않았다. 적용 시점은 개정(Regulation (EU) 2026/1744)과 관련해 이 페이지에서 확정하지 않는다. 법 해석의 상세는 [59. 법·규제·보험·라이선스](../governance-law-and-society/law-regulation-insurance-and-licensing.md)와 이어진다."
        },
        {
          "section": "4. 핵심 개념과 용어",
          "action": "append",
          "content": "### 2026-10-12 갱신: 보장의 전제와 배포 묶음\n\n주제 페이지의 개념 목록에 다음 조건과 개념을 덧붙인다.\n\n- **[등각 예측](../../glossary/conformal-prediction.md)(Conformal Prediction)의 전제** — KnowNo(CoRL 2023, PMLR 229)의 등각 예측 보장은 보정 집합과 새 시험 표본이 같은 미지의 분포에서 독립·동일 분포(independent and identically distributed, i.i.d.)로 뽑힌다는 가정 위에 서며, 과제 성공 보장의 증명은 사람이 정확하게 도와준다는 가정에 기댄다. [사실][^ref-351]\n- **[모델 레지스트리](../../glossary/model-registry.md)(Model Registry) 별칭의 반영 시점** — MLflow v3.1.0 문서는 별칭(alias)을 새 모델 버전으로 재지정하면 같은 별칭으로 모델을 불러오는 코드가 다음에 실행될 때 새 버전을 가져온다고 설명할 뿐, 이미 실행 중인 프로세스나 연결이 끊긴 장치의 모델이 즉시 바뀐다고 말하지 않는다. [사실][^ref-1577]\n- **정책·데이터 형식 호환성(Policy and Dataset Compatibility)** — LeRobot v0.6.0 하위 호환성 문서는 정책 가중치에 내장되던 정규화 계층을 없애고 외부 전·후처리 파이프라인(PolicyProcessorPipeline)이 정규화를 맡도록 바꾼 변경을 호환성 깨짐으로 명시하고, 이전 모델은 이전(migration)이 필요하다고 적는다. [사실][^ref-1578] 같은 문서는 하드웨어 API 재설계 이전의 보정 방식으로 기록한 궤적을 그대로 불러오면 잘못 재생된다고 경고한다(SO100·SO101 예시의 관절 보정·입출력 변환이며 다른 기종으로 일반화하지 않음). [사실][^ref-1578] LeRobotDataset v3.0 형식은 여러 에피소드의 표 행과 영상 프레임을 큰 파일로 이어 붙이고, 에피소드별 구간을 파일 경계가 아니라 메타데이터로 복원한다(코드 판 v0.6.0과 데이터 형식 판 v3.0은 다른 번호). [사실][^ref-1578]\n- **배포 묶음(Deployment Bundle)** — 이 위키는 학습 정책을 로봇에 배포할 때 가중치 해시, 전·후처리기와 정규화 통계, 학습 데이터 커밋과 데이터 형식 판, 카메라·관절 스키마, 하드웨어 보정판, 런타임 판을 하나의 배포 묶음으로 기록하고 이전 묶음을 보존해야 되돌릴 수 있다고 본다(실물 재생 시험은 하지 않은 의견). [의견][^ref-1578]"
        },
        {
          "section": "5. 적용 사례 (현장 유형 명시)",
          "action": "replace",
          "content": "> **현장 유형: 물류창고.** 아래 시나리오는 이전 분류가 모든 영역에 물류 흐름 7단계를 적용하던 때(2026-09-25) 쓴 물류창고 사례다. 다른 현장 유형의 적용 사례는 이어지는 조사에서 더한다.\n\n**물류 흐름 단계:** 피킹, 출하\n\n**시나리오:** 자연어 피킹 지시의 해석 검증과 출하 마감 시간대의 학습 배차 모델 교체\n\n다음은 설명을 위한 가상의 시나리오이다. 수치는 넣지 않았고, 근거 출처의 실험 환경(가정·주방·벤치마크, 시뮬레이션 창고)은 물류 현장과 다르다.\n\n### 가. 피킹 — 자연어 지시 해석\n\n| 항목 | 내용 |\n|---|---|\n| 시작 조건 | 관리자가 “오늘 마감 주문을 B구역부터 피킹”처럼 자연어로 지시하면, LLM 해석 결과를 계획기 입력 형식으로 바꿔 검증하고 구역·마감 같은 인자가 모호하면 실행 전에 되물어야 오해석이 작업 발생으로 이어지지 않을 것으로 보인다. [추정][^ref-092][^ref-351][^ref-354] |\n| 작업 대상 | 해당 없음 |\n| 수행 자원 | LLM은 지시를 해석하고, ROP는 해석 결과의 채택·거부와 사람 확인 요청, 채택·거부 기록을 맡는 구조로 보인다. [추정][^ref-351] |\n| 제약 | 이런 AI 활용이 인공지능 기본법의 고영향 인공지능에 해당하는지는 미확인이다(11절 열린 질문). |\n| 완료·인계 | 해당 없음 |\n| 예외·성과 | 해석 후보가 불확실하면 사람에게 묻는다. KnowNo는 필요할 때 사람에게 도움을 요청하게 하며 사람 도움을 줄이는 것을 목표로 한다(저자 보고). [사실][^ref-351] |\n\n### 나. 출하 — 학습 배차 모델 교체\n\n| 항목 | 내용 |\n|---|---|\n| 시작 조건 | 출하 마감 시간대에 학습 기반 배차 모델을 새 버전으로 바꾸려는 변경 요청(설명용 가정) |\n| 작업 대상 | 해당 없음 |\n| 수행 자원 | 창고 다중 로봇 작업 배정을 강화학습 정책으로 수행하는 방법이 연구되어 있다(RTAW, 시뮬레이션 창고 조건). [사실][^ref-623] |\n| 제약 | 해당 없음 |\n| 완료·인계 | 해당 없음 |\n| 예외·성과 | 모델 레지스트리의 버전·별칭으로 교체·되돌림 경로를 두고 교체 전 시험·감시 기준을 통과시켜야, 데이터 의존성·숨은 피드백 루프 같은 ML 고유 위험에서 오는 배정 품질 저하가 출하 지연으로 번지는 것을 막을 수 있을 것으로 보인다. [추정][^ref-626][^ref-625][^ref-623][^ref-624] MLflow v3.1.0 문서 기준으로 별칭 재지정은 같은 별칭으로 모델을 불러오는 코드가 다음에 실행될 때 반영된다. [사실][^ref-1577] ML Test Score는 오프라인 시험만으로는 운영 성능을 보장할 수 없다며 소수 트래픽에 먼저 내보내는 카나리를 완화책으로 들고, 롤백을 비상 절차로 두되 평상시에 연습하라고 권고한다(일반 ML 서비스 지침). [사실][^ref-625] |\n\n피킹 시나리오에서 이 영역이 관여하는 칸은 시작 조건(지시가 작업으로 바뀌는 순간)과 예외·성과(되묻기)다. 출하 시나리오에서는 모델 교체가 예외·성과 칸의 위험이 된다.\n\n국내 기사에 따르면 한진은 대전 메가허브에 AI 기반 적재량 예측 시스템을 적용해 간선차량 상·하차 종료 시점을 미리 파악하고 다음 차량 접안 대기시간을 줄였다고 한다. [추정] 벤더 주장[^ref-627] 이런 예측을 ROP 관점에서 쓴다면 ROP의 몫은 입출고 시간·접안·현장 상·하차 작업의 동기화까지이고, 간선 배차·운송계획은 분류 원문 19장 “거점 간 운송”의 연계 대상이다([범위 경계](../../about/scope-boundary.md)).\n\n**현장 유형:** 기타\n\n**사례:** 부산 스마트시티 국가 시범도시의 서비스 로봇 4종 통합 관제(회사 발표)\n\n| 항목 | 내용 |\n|---|---|\n| 시작 조건 | 미확인 |\n| 작업 대상 | 미확인 |\n| 수행 자원 | LG CNS 발표에 따르면 로봇 학습·운영 플랫폼 ‘피지컬웍스’의 운영·관제 도구 바통(Baton)이 부산 스마트시티 국가 시범도시 사업에서 순찰·바리스타·짐캐리·청소 4종 로봇의 통합 관제에 쓰이고 있다. [추정] 벤더 주장[^ref-1584] |\n| 제약 | 미확인 |\n| 완료·인계 | 미확인 |\n| 예외·성과 | 미확인 |\n\nLG CNS 발표(2026-05-07)에 따르면 피지컬웍스의 포지(Forge)에서 학습·검증한 로봇을 바통으로 운영·관제하고, 이 과정에서 쌓인 데이터를 다시 학습에 쓰는 선순환 체계를 구축했다고 한다. [추정] 벤더 주장[^ref-1584] 같은 발표에 따르면 AMR·AGV 등 100대 규모 운영 환경에 바통을 적용하면 생산성이 약 15% 이상 오르고 운영비가 최대 18% 줄 것으로 기대된다고 하나, 이는 회사가 기대치로 제시한 값(실측 아님)이다. [추정] 벤더 주장[^ref-1584] 같은 발표에 따르면 포지는 20곳 이상 고객사와 개념검증(Proof of Concept, PoC)을 진행 중이며, 이 주장은 독립적으로 확인되지 않았다. [추정] 벤더 주장[^ref-1584]\n\n이 사례에서 이 영역이 관여하는 부분은 학습과 운영 사이의 모델 갱신이지만, 공개 자료로 채울 수 있는 칸은 수행 자원뿐이었다. 이 위키는 학습·운영 연계 플랫폼을 도입 검토할 때 시연, PoC, 상시 운영을 서로 다른 수준의 증거로 받고, 모델 갱신 이력·고객 검수·장애 복구 기록을 따로 요청하는 편이 좋다고 본다. [의견][^ref-1584]"
        },
        {
          "section": "6. 대표 접근법과 기술",
          "action": "append",
          "content": "### 2026-10-12 갱신: 모델 교체·되돌림과 보장 조건\n\n주제 페이지의 ‘모델 운영 관리’와 ‘필요할 때 되묻기’ 소절에 아래 내용을 덧붙인다.\n\n#### 운영 투입 승인·카나리·롤백 연습\n\nML Test Score(Breck 외, IEEE Big Data 2017)의 Infra4 항목은 모델이 실제 요청에 영향을 주기 전에 품질을 자동 검사해 모델을 승인하거나 거부해 운영 투입을 막는 절차를 권한다(일반 ML 서비스 운영 지침이며 로봇 안전 요구는 아님). [사실][^ref-625] Infra6 항목은 오프라인 시험이 아무리 넓어도 그것만으로 운영 환경 성능을 보장할 수 없다고 보고 소수 트래픽에 먼저 내보내는 카나리를 완화책으로 들며, Infra7 항목은 이전 정상판으로 되돌리는 롤백을 비상 절차로 두되 비상이 아닐 때 미리 연습하라고 권고한다(권고 강도). [사실][^ref-625] 이 위키는 카나리가 위험 완화 방법일 뿐 로봇의 물리적 위험 노출을 허가하는 근거가 아니므로, 로봇 모델의 운영 투입 승인 기록에 장치·현장별 성능 하한, 기존 판 대비 퇴행, 로딩·추론 지연, 개입·실패 사례, 실제 롤백 연습 결과를 연결하고 위험한 행동의 시험을 현장 안전 절차와 분리하지 않는 편이 좋다고 본다(보편 임계값은 정하지 않음). [의견][^ref-625]\n\n기존 소절의 MLflow 별칭 교체 문장은 반영 시점과 함께 읽는다. MLflow v3.1.0 문서 기준으로 별칭 재지정은 같은 별칭으로 모델을 불러오는 코드가 다음에 실행될 때 반영된다. [사실][^ref-1577] 이 위키는 ROP가 레지스트리의 목표 모델 버전과 로봇마다 실제로 실행 중인 버전을 따로 기록하고, 별칭 변경 뒤 장치별 로딩·검증 응답을 받아야 교체가 끝났다고 보는 편이 맞다고 본다(플릿 전체 원자적 교체는 확인하지 못함). [의견][^ref-1577]\n\n#### 장치 업데이트 도구에서 본 배포 중단과 롤백 상태\n\n아래 도구는 [43. 데이터·관측성·배포](../platform-architecture-and-infrastructure/data-observability-and-deployment.md)와 [57. 자산·소프트웨어 수명주기 관리](../verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md)에서 다루는 장치 업데이트 도구이며, 여기서는 모델 교체·되돌림 관점만 본다.\n\n- Mender 문서에 따르면 사용자 정의 업데이트 모듈이 롤백을 지원하려면 롤백 지원 질의(SupportsRollback)에 ‘예’로 답하고, 설치 전에 알려진 정상 상태를 저장했다가 롤백 때 복원하는 구현을 모듈 작성자가 넣어야 한다. [추정] 벤더 주장[^ref-1579] 같은 문서에 따르면 전원 상실 뒤 업데이트 상태가 다시 실행될 수 있으므로 업데이트 모듈을 멱등하게 만들도록 권고한다. [추정] 벤더 주장[^ref-1579]\n- AWS IoT Jobs 문서에 따르면 작업 배포 속도와 중단(abort) 설정을 두고, 실패한 장치 수 등이 지정한 기준에 이르면 작업 배포를 취소할 수 있으며, 이는 새 배포를 멈추는 것이지 이미 설치된 장치의 원복과는 별개다. [추정] 벤더 주장[^ref-1581]\n- AWS IoT Greengrass v2 문서에 따르면 장치별 배포 실패 상태를 롤백 미요청, 이전 정상 구성으로 롤백 완료, 롤백 실패로 나누고, 롤백하지 않았거나 롤백에 실패한 장치는 정상 동작하지 않을 수 있다. [추정] 벤더 주장[^ref-1580] 두 AWS 문서는 같은 기관 자료라 서로의 교차 확인으로 세지 않는다.\n- Viam 문서에 따르면 새 모델을 플릿에 내보낼 때 갱신한 구성 조각(fragment)을 먼저 첫 집단(예: 카나리 위치)에만 적용해 관찰한 뒤 나머지로 넓히는 [단계적 배포](../../glossary/phased-rollout.md) 절차를 둔다. [추정] 벤더 주장[^ref-1582] 같은 문서에 따르면 새 모델이 잘못 보이면 구성 조각에서 이전 판을 고정해 되돌리며, 장치는 다음 구성 동기화 때(정상 운영에서는 수 초 안에) 이전 판으로 수렴하고, 이는 연결이 끊긴 장치의 즉시 변경이 아니다. [추정] 벤더 주장[^ref-1582]\n\n이 위키는 모델 배포가 배포 중단, 이전 모델 복원 시도, 복원 확인을 서로 다른 상태로 기록하고, 확대 배포 여부를 집단 성공률만이 아니라 장치별 현재 버전·실패 사유·복구 결과로 판단하며, 복구하지 못한 로봇은 새 작업 배정에서 빼는 운영 정책을 두는 편이 맞다고 본다. [의견][^ref-1579][^ref-1580][^ref-1581]\n\n#### 필요할 때 되묻기 — 등각 예측 보장의 조건\n\n주제 페이지의 KnowNo 보장 서술은 다음 조건 위에서 읽는다. KnowNo(CoRL 2023, PMLR 229)의 등각 예측 보장은 보정 집합과 새 시험 표본이 같은 분포에서 i.i.d.로 뽑힌다는 가정에 서고, 과제 성공 보장의 증명은 사람이 정확하게 도와준다는 가정에 기댄다. [사실][^ref-351] 다단계 계획에서는 시점 사이 의존성 때문에 i.i.d. 가정이 깨지므로 KnowNo는 개별 시점 대신 시퀀스 수준에서 보정하며, 이는 운영 분포가 임의로 바뀌는 경우까지 보장하는 것이 아니다. [사실][^ref-351]\n\n분포가 시간에 따라 바뀌는 경우에는 적응형 등각 추론(Adaptive Conformal Inference, ACI; Gibbs·Candès, NeurIPS 2021)이 장기간의 경험적 포함 빈도가 목표값에 맞는다는 장기 평균 보장을 주며, 이는 매 시점 보장이나 로봇 안전 보장이 아니고 논문 실험도 주가 변동성·선거 데이터로 로봇 실험은 없다. [사실][^ref-1583] ACI의 온라인 갱신은 직전 예측 집합들이 정답을 놓친 경험적 빈도를 보고 임계값을 조정하므로, 운영 중 정답을 관측할 수 있어야 쓸 수 있다. [사실][^ref-1583] KnowNo와 ACI는 보장의 종류가 달라 서로의 교차 확인이 아니다. 이 위키는 물류 지시 분포가 바뀌는 현장에서 고정 간격(예: 매월) 재보정을 근거 없는 기본값으로 두지 말고, 지시 유형별 보정 오차와 데이터 변화 신호를 감시하며 피드백 지연·정답 수집 비용을 고려한 재보정 정책을 시험하는 편이 좋다고 본다(최적 주기는 미해결). [의견][^ref-351][^ref-1583]\n\n#### 운영 중 학습하는 플릿의 정책 판 경계\n\n로봇의 저수준 조작 정책 학습 자체는 로봇 자체 지능·제어 경계의 연계 대상이며, 여기서는 정책 판 갱신 경계와 운영 기록 관점만 본다. Learning While Deploying(LWD, arXiv v4 2026-09-16, 학회 게재 미확인 프리프린트)은 저자 대부분이 AGIBOT(Finch) 소속(일부 Shanghai Innovation Institute 겸직, 1명 Columbia University)인 제조사 연구로, 자사 Agibot G1 양팔 로봇 16대 플릿(식료품 보충 작업 4대, 장기 작업마다 3대)으로 8개 실물 조작 작업에서 온라인 학습을 했고 방법마다 실험당 4시간 벽시계 예산(플릿 합계 약 60시간)을 줬다(저자 보고, 동일 기종 플릿이며 이기종 아님). [사실][^ref-1585] 학습기는 50 학습 단계마다 갱신 정책을 플릿에 내보내고, 로봇은 에피소드 경계에서 새 정책을 다시 불러온다(연구 구현, 저자 보고). [사실][^ref-1585] 저자는 한계로 현재 학습 틀이 실행 안전을 명시적으로 모델링하지 않으며 직관적인 실시간 갱신 일정이 더 큰 규모의 배포에는 최적이 아닐 수 있다고 밝힌다. [사실][^ref-1585] 이 위키는 운영 중 학습하는 정책을 쓰는 플릿에서는 작업 이력마다 실행한 정책 판을 붙이고, 새 정책을 적용하는 경계(예: 에피소드·임무 단위)와 승인 주체를 명시해야 임무 도중 모델이 바뀌는 문제를 관리할 수 있다고 본다. [의견][^ref-1585]"
        },
        {
          "section": "7. 관련 표준·프레임워크·오픈소스",
          "action": "append",
          "content": "### 2026-10-12 갱신\n\n주제 페이지의 표에 다음 행을 더한다. 기존 MLflow 행의 근거(ref-626)는 최신(latest) 문서이고, 아래 행은 판을 고정한 문서다.\n\n| 이름 | 유형 | 이 영역과의 관계 | 출처 |\n|---|---|---|---|\n| MLflow 모델 레지스트리(v3.1.0 고정 문서) | 오픈소스 | 별칭 재지정은 같은 별칭 로딩 코드가 다음에 실행될 때 반영된다 | [사실][^ref-1577] |\n| LeRobot v0.6.0 하위 호환성 문서 | 오픈소스 | 정규화의 외부 전·후처리 파이프라인 이동을 호환성 깨짐으로 표시하고, 옛 보정 방식 궤적의 재생 오류를 경고한다 | [사실][^ref-1578] |\n| LeRobotDataset v3.0 | 오픈소스 | 여러 에피소드를 큰 파일로 묶고 에피소드 구간을 메타데이터로 복원하는 데이터 형식 | [사실][^ref-1578] |\n| NIST AI RMF 1.0(NIST AI 100-1) MANAGE 4.1 | 프레임워크 | 배포 후 감시 계획에 의견 수집·평가, 이의 제기·무효화, 폐기, 사고 대응, 복구, 변경관리 장치를 넣어 실행하도록 한다(법적 의무가 아닌 자율 적용 프레임워크) | [사실][^ref-1586] |\n\n#### 국내 공개 로봇 조작 데이터의 판·분할 메타데이터\n\nAI-Hub ‘대규모 물리환경 로봇조작 데이터’(dataSetSn 71825)의 변경이력은 v1.0을 2025-04-16 데이터 개방(Beta), v1.1을 2025-06-30 데이터 최종 개방으로 표시하고, 데이터 히스토리의 2026-05-06 항목은 ‘태그 추가’뿐이라 새 데이터 판으로 볼 근거가 없다. [사실][^ref-1588] 같은 페이지의 구성표는 총 262,166건 중 학습 238,266건, 테스트 23,900건을 적으면서 표제는 학습 80%·테스트 10%로 달았고, 검증 분할은 표기하지 않는다. [사실][^ref-1588] 건수로 이 위키가 계산하면 학습 약 90.9%·테스트 약 9.1%로 표제 비율과 맞지 않는다(원문 값이 아닌 계산값). 원천 데이터는 실제환경 77,984장, 가상환경 184,182장(RGB 기준, Depth도 같은 수)이다. [사실][^ref-1588] 이 위키의 계산으로는 약 70%(70.3%)가 가상환경에서 취득됐으므로, 실물 조작 성능 근거로 읽을 때 실제·가상을 구분해야 한다. 같은 페이지의 분포 표는 원천 데이터 비율을 실제 14.29%·가상 85.71%로 적어 수량으로 이 위키가 계산한 비율(약 29.7%·70.3%)과 맞지 않고, 라벨링 JSON 합계를 건수 합 262,166이 아닌 524,332로 적는다. [사실][^ref-1588] 어느 값이 맞는지는 제공자 확인 전까지 판정하지 않는다(11절 열린 질문). 이 위키는 이처럼 분할비·합계가 맞지 않는 공개 데이터는 제공자 확인 전에는 표제 분할비를 모델 승인 근거로 쓰지 말고, 실물·가상 구분, 중복, 평가용 누출을 실제 파일로 따로 검사하는 편이 좋다고 본다(실제 파일은 열지 않음). [의견][^ref-1588]\n\n#### 관련 법 문단 갱신(주제 페이지의 2026-09-25 서술 보충)\n\n주제 페이지의 관련 법 문단은 이 갱신 전 서술이며, 아래가 2026-10-12 기준이다. 법 해석과 의무 발생 판단은 [59. 법·규제·보험·라이선스](../governance-law-and-society/law-regulation-insurance-and-licensing.md)와 연결하고, 이 페이지는 개별 ROP의 의무 발생 여부를 판단하지 않는다.\n\n국가법령정보센터의 현행 조문은 「인공지능 발전과 신뢰 기반 조성 등에 관한 기본법」을 법률 제21311호(2026-01-20 공포·일부개정), 시행 2026-07-21 판으로 표시한다(2026-01-22 시행은 최초 법률·시행령 기준). [사실][^ref-620] 제34조 1항은 고영향 인공지능 제공 사업자의 안전성·신뢰성 확보 조치로 위험관리방안, 설명 방안, 이용자 보호, 사람의 관리·감독과 함께 5호의 조치 내용 확인 문서 작성·보관을 둔다. [사실][^ref-620] 이 위키는 ROP가 학습용 데이터 개요, 모델 판, 위험 조치, 사람 감독, 승인·복구 기록을 서로 연결해 두어 고영향 해당성이 판단되면 제34조 문서로 낼 수 있는 구조를 미리 갖추는 편이 좋다고 본다. [의견][^ref-620]\n\nEU AI Act는 2026-07-27 통합판에서 기계류 규정이 부속서 I Section B로 옮겨졌고 제2조 2항이 Section B 관련 고위험 AI의 적용 조문을 한정한다(3절). 다음 두 조문은 조문 내용 소개이며, 기계류 연계 로봇 AI에 바로 적용되는 의무로 읽지 않는다. 제43조 4항은 적합성 평가를 거친 고위험 AI 시스템이 [실질적 변경](../../glossary/substantial-modification.md)(Substantial Modification)을 겪으면, 변경된 시스템을 다시 유통하든 같은 배포자가 계속 쓰든 새 적합성 평가 절차를 거치도록 정한다. [사실][^ref-1587] 같은 항은 출시·사용 개시 뒤에도 계속 학습하는 고위험 AI 시스템에서 제공자가 최초 적합성 평가 때 미리 정하고 부속서 IV 2(f) 기술문서에 담은 시스템·성능 변경은 실질적 변경으로 보지 않는다고 정한다. [사실][^ref-1587] 제72조 2항은 제공자의 시판 후 감시 체계가 배포자 제공 등으로 얻은 고위험 AI 시스템의 성능 데이터를 수명 전반에 걸쳐 능동적·체계적으로 수집·문서화·분석하고, 관련되면 다른 AI 시스템과의 상호작용 분석을 포함하도록 정한다. [사실][^ref-1587] 제2조 2항에 따라 이 두 조문은 Section A 법령·부속서 III 경로의 고위험 AI에 해당하는 내용으로 소개하며, 기계류 규정 대상 로봇의 안전 구성요소로서 고위험이 되는 AI에 AI Act 조문으로 바로 적용된다고 볼 수 없어 보인다. [추정][^ref-1587] 이는 법률 판단이 아니며, 기계류 규정 (EU) 2023/1230 쪽에 AI 고위험 요구가 어떻게 통합되는지는 확인하지 않았다. 이 위키는 EU 시장을 대상으로 할 때 적용 관할·시스템 분류·공급자 지위를 먼저 정하고, 최초 평가에서 허용한 변경 범위와 실제 모델 변경 내역을 대조할 수 있도록 변경 기록을 보존하는 편이 맞다고 본다. [의견][^ref-1587]"
        },
        {
          "section": "8. 대표 연구와 자료",
          "action": "append",
          "content": "### 2026-10-12 갱신\n\n- Ren, A. Z. 외, Robots That Ask For Help(KnowNo, CoRL 2023, PMLR 229) — 주제 페이지 항목에 보장의 가정을 덧붙인다: i.i.d. 보정, 정확한 사람 도움, 다단계 계획의 시퀀스 수준 보정. [사실][^ref-351]\n- Breck, E. 외, The ML Test Score(IEEE Big Data 2017) — 28개 항목 가운데 Infra4(자동 품질 검사로 승인·거부), Infra6(오프라인 시험의 한계와 카나리), Infra7(평상시 롤백 연습 권고)이 모델 교체 절차와 직접 이어진다. [사실][^ref-625]\n- Gibbs, I.·Candès, E. J., Adaptive Conformal Inference Under Distribution Shift(NeurIPS 2021) — 분포 이동 아래 장기 평균 포함 빈도를 보장하는 온라인 재보정 방법으로, 정답 관측이 필요하고 로봇 실험은 없다. [사실][^ref-1583]\n- Wang, Y. 외, Learning While Deploying(arXiv v4, 2026-09-16) — 제조사 중심 연구 프리프린트(학회 게재 미확인)로, 동일 기종 16대 플릿에서 에피소드 경계에 정책을 갱신했고 실행 안전을 명시적으로 모델링하지 않는다는 한계를 저자가 밝힌다. [사실][^ref-1585]"
        },
        {
          "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
          "action": "append",
          "content": "### 배포 후 감시·변경관리·복구 실패 처리\n\nNIST AI RMF 1.0의 MANAGE 4.1은 배포 후 AI 시스템 감시 계획에 사용자·관련 AI 행위자 의견 수집·평가, 이의 제기와 무효화, 폐기, 사고 대응, 복구, 변경관리 장치를 넣어 실행하도록 하는 항목이며, 법적 의무가 아닌 자율 적용 프레임워크다. [사실][^ref-1586] 이 위키는 모델 공급자의 학습·검증 책임, ROP의 배포·실행 판 기록, 현장 운영자의 개입·사고 통보 역할을 계약과 운영 절차에서 따로 정해야 하며, 조직 단위 관리 체계 인증만으로 특정 로봇 모델의 안전 성능을 승인해서는 안 된다고 본다. [의견][^ref-1586] 같은 맥락에서 이 위키는 ROP가 배포 중단·이전 모델 복원 시도·복원 확인을 서로 다른 상태로 기록하고, 복구하지 못한 로봇을 새 작업 배정에서 빼는 정책을 맡는 편이 맞다고 본다. [의견][^ref-1579][^ref-1580][^ref-1581] 장치 업데이트 실행 수단은 [43. 데이터·관측성·배포](../platform-architecture-and-infrastructure/data-observability-and-deployment.md), 법 해석과 의무 발생 판단은 [59. 법·규제·보험·라이선스](../governance-law-and-society/law-regulation-insurance-and-licensing.md)와 법무·운영 사업자 쪽 연계 대상이며, 이 페이지는 개별 ROP의 의무 발생 여부를 판단하지 않는다."
        },
        {
          "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
          "action": "append",
          "content": "### 2026-10-12 갱신으로 더한 연결\n\n- [43. 데이터·관측성·배포](../platform-architecture-and-infrastructure/data-observability-and-deployment.md) — 장치 업데이트 도구의 단계적 배포·배포 중단·롤백 상태가 모델 교체·되돌림의 실행 수단이 된다.\n- [57. 자산·소프트웨어 수명주기 관리](../verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) — 가중치·전처리기·데이터 형식·보정판을 묶은 배포 묶음의 판 관리와 이전 묶음 보존이 이어진다.\n- [59. 법·규제·보험·라이선스](../governance-law-and-society/law-regulation-insurance-and-licensing.md) — 한국 인공지능기본법 제34조의 문서 책무와 EU AI Act 개정(부속서 I Section B, 제2조 2항)의 해석이 이어진다."
        },
        {
          "section": "11. 열린 질문",
          "action": "replace",
          "content": "아직 확인하지 못한 사실과 판단이 필요한 쟁점은 다음과 같다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.\n\n- **oq-030** (상태: 열림) 출처 충돌: LTAA(arXiv 2512.02810) 초록 요약은 로봇 전문화가 강한 설정에서 LLM 배정이 작업 완료율 77%로 전통 기법을 모두 앞섰다고 하지만, 다른 2차 요약은 동적 계획법의 완료율이 더 높다고 적는다. 어느 쪽이 원문 결과인가? 관련 후속 질문은 oq-356(같은 성공 확률 모델·작업 집합으로 비교군을 재평가한 공개 재현 자료가 있는가)이다.\n- **oq-105** (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-68) 물류 현장 로봇의 작업 계획·배정에 쓰는 AI가 한국 인공지능 기본법의 고영향 인공지능 영역에 해당하는가, 해당하면 ROP 사업자와 현장 운영사 중 누가 책무를 지는가? 부분 근거: 개정 법률 제21311호가 2026-07-21 시행되었고 제34조 1항 5호가 조치 내용 문서의 작성·보관을 정하나, 고영향 해당성·사업자 지위·시행령상 보존 기간은 확인하지 못했다(3절).[^ref-620]\n- **oq-106** (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-68) LLM이나 학습 모델이 ROP의 정지·경로·구역 결정에 관여할 때 EU AI Act가 말하는 제품 안전 구성요소로 볼 수 있는가? 부분 근거: 2026-07-27 통합판에서 기계류 규정은 부속서 I Section B로 옮겨졌고 제2조 2항이 적용 조문을 한정한다는 점만 확인했으며, 제품 안전 구성요소 해당성은 판단하지 않았다(3·7절).[^ref-1587]\n- **oq-107** (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-68) KnowNo의 등각 예측 보장은 보정 데이터와 운영 분포가 같다는 조건에 기대는데, 물류 지시 분포가 계절·고객에 따라 바뀔 때 보정을 얼마나 자주 다시 해야 하는가? 부분 근거: KnowNo 보장은 i.i.d. 보정과 정확한 사람 도움 가정에 서고, 적응형 등각 추론은 정답 관측을 전제로 장기 평균 보장만 준다. 재보정 주기는 미해결이다(6절).[^ref-351][^ref-1583]\n- **oq-213** (상태: 열림) 부분 근거: Viam 문서의 단계적 배포와 이전 판 고정·다음 구성 동기화 때 수렴하는 되돌림 절차(벤더 주장, 6절).[^ref-1582]\n- **oq-222** (상태: 열림) 학습된 배정·경로 정책을 현장에 쓸 때 분포 이동을 감지해 탐색·규칙 기반 정책으로 되돌리는 기준을 정한 연구나 제품이 있는가? 부분 근거: 분포 이동 아래 온라인 재보정은 정답 관측을 요구한다는 점을 확인했으나, 배정 정책 되돌림 기준은 아니다(6절).[^ref-1583]\n- (신규, 상태: 열림 · 제기 2026-10-12 · 실행 2026-10-12-04) 학습 모델·전처리기(정규화 통계)·하드웨어 보정판이 함께 바뀌는 변경을 로봇 플릿에서 어느 시험 단위로 승인하고, 실패 시 어느 묶음 단위로 복구할 것인가?[^ref-1578]\n- (신규, 상태: 열림 · 제기 2026-10-12 · 실행 2026-10-12-04) 운영 중 학습 정책을 에피소드 경계에서 갱신하는 방식이 제조사가 다른 이기종 로봇과 중간에 끊을 수 없는 장기 임무에서도 적절한가, 임무 도중 정책 판이 바뀌지 않게 하는 경계를 어떻게 정할 것인가?[^ref-1585]\n- (신규, 상태: 열림 · 제기 2026-10-12 · 실행 2026-10-12-04) 출처 충돌: AI-Hub 대규모 물리환경 로봇조작 데이터(71825) 설명 페이지 한 곳 안에서 분할 표제(학습 80%·테스트 10%)와 건수(238,266·23,900), 원천 분포 비율(14.29%·85.71%)과 수량(77,984·184,182), 라벨링 JSON 합계(524,332)와 건수 합(262,166)이 서로 맞지 않는데, 어느 값이 맞으며 실제 배포 파일과 일치하는가?[^ref-1588]\n- (신규, 상태: 열림 · 제기 2026-10-12 · 실행 2026-10-12-04) 모델 공급자와 ROP가 함께 확인할 수 있는 모델 변경·배포·복구 증거(판 식별, 승인 기록, 장치별 적용·롤백 결과)의 최소 항목은 무엇인가?[^ref-1586]"
        },
        {
          "section": "13. 참고 자료 (각주)",
          "action": "replace",
          "content": "[^ref-617]: NIST, NIST Risk Management Framework Aims to Improve Trustworthiness of Artificial Intelligence, 2023-01-26, https://nist.gov/news-events/news/2023/01/nist-risk-management-framework-aims-improve-trustworthiness-artificial, 접근일 2026-09-25 (원문 미열람)\n[^ref-618]: ISO/IEC, ISO/IEC 42001:2023 - AI management systems, 2023, https://www.iso.org/standard/42001, 접근일 2026-09-25 (원문 미열람)\n[^ref-619]: ISO/IEC, ISO/IEC 23894:2023 - AI — Guidance on risk management, 2023-02, https://www.iso.org/standard/77304.html, 접근일 2026-09-25 (원문 미열람)\n[^ref-620]: 국가법령정보센터(과학기술정보통신부), 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법, 2026-01-20, https://www.law.go.kr/lsInfoP.do?lsiSeq=268543, 접근일 2026-10-12\n[^ref-621]: European Commission, AI Act (Shaping Europe's digital future), 미확인, https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai, 접근일 2026-09-25 (원문 미열람)\n[^ref-088]: Ahn, M. 외, Do As I Can, Not As I Say: Grounding Language in Robotic Affordances, 2022-04, https://arxiv.org/abs/2204.01691, 접근일 2026-09-25 (원문 미열람)\n[^ref-092]: Liu, B. 외, LLM+P: Empowering Large Language Models with Optimal Planning Proficiency, 2023-04, https://arxiv.org/abs/2304.11477, 접근일 2026-09-25 (원문 미열람)\n[^ref-351]: Ren, A. Z. 외, Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners, 2023-07, https://arxiv.org/abs/2307.01928, 접근일 2026-10-12\n[^ref-622]: Liang, J. 외, Code as Policies: Language Model Programs for Embodied Control, 2022-09, https://arxiv.org/abs/2209.07753, 접근일 2026-09-25 (원문 미열람)\n[^ref-623]: Agrawal, A. 외, RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments, 2022-09, https://arxiv.org/abs/2209.05738, 접근일 2026-09-25 (원문 미열람)\n[^ref-624]: Sculley, D. 외, Hidden Technical Debt in Machine Learning Systems, 2015, https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems, 접근일 2026-09-25 (원문 미열람)\n[^ref-625]: Breck, E. 외 (Google Research), The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction, 2017, https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/, 접근일 2026-10-12\n[^ref-626]: MLflow (Linux Foundation 오픈소스 프로젝트), ML Model Registry (MLflow AI Platform), 미확인, https://mlflow.org/docs/latest/ml/model-registry/, 접근일 2026-09-25 (원문 미열람)\n[^ref-627]: 머니투데이, 포장은 로봇이, 간선운송은 무인차가…물류현장 스며든 '피지컬 AI', 2026-09-19, https://www.mt.co.kr/industry/2026/09/19/2026091818023697394, 접근일 2026-09-25 (원문 미열람)\n[^ref-354]: cog-model (AmbiK 저자), AmbiK-dataset — README (AmbiK: Dataset of Ambiguous Tasks in Kitchen Environment), 미확인, https://github.com/cog-model/AmbiK-dataset, 접근일 2026-09-25 (원문 미열람)\n[^ref-359]: Wang, W. 외, Learning to Ask: When LLM Agents Meet Unclear Instruction, 2024-09, https://arxiv.org/abs/2409.00557, 접근일 2026-09-25 (원문 미열람)\n[^ref-056]: Liu, J. X. 외, Grounding Complex Natural Language Commands for Temporal Tasks in Unseen Environments, 2023-02, https://arxiv.org/abs/2302.11649, 접근일 2026-09-25 (원문 미열람)\n[^ref-417]: arXiv (SafeGate 저자, 저자명 미확인), Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems, 2026-04, https://arxiv.org/abs/2604.05427, 접근일 2026-09-25 (원문 미열람)\n[^ref-1577]: MLflow 프로젝트 (Linux Foundation 오픈소스 프로젝트), Model Registry Workflows (docs/docs/classic-ml/model-registry/workflow.mdx, MLflow v3.1.0), 2025-06-10, https://github.com/mlflow/mlflow/blob/v3.1.0/docs/docs/classic-ml/model-registry/workflow.mdx, 접근일 2026-10-12\n[^ref-1578]: Hugging Face LeRobot 기여자 (huggingface/lerobot), Backward compatibility (docs/source/backwardcomp.mdx, LeRobot v0.6.0), 2026-07-06, https://github.com/huggingface/lerobot/blob/v0.6.0/docs/source/backwardcomp.mdx, 접근일 2026-10-12\n[^ref-1579]: Northern.tech (Mender documentation), Create a custom Update Module, 미확인, https://docs.mender.io/artifact-creation/create-a-custom-update-module, 접근일 2026-10-12\n[^ref-1580]: Amazon Web Services (AWS IoT Greengrass V2 Developer Guide), Check deployment status, 미확인, https://docs.aws.amazon.com/greengrass/v2/developerguide/check-deployment-status.html, 접근일 2026-10-12\n[^ref-1581]: Amazon Web Services (AWS IoT Core Developer Guide), How job configurations work, 미확인, https://docs.aws.amazon.com/iot/latest/developerguide/jobs-configurations-details.html, 접근일 2026-10-12\n[^ref-1582]: Viam, Roll out a new model to a fleet, 미확인, https://docs.viam.com/vision/deploy-and-maintain/roll-out-to-fleet/, 접근일 2026-10-12\n[^ref-1583]: Gibbs, I., & Candès, E. J. (NeurIPS 2021), Adaptive Conformal Inference Under Distribution Shift, 2021-12-06, https://papers.nips.cc/paper/2021/file/0d441de75945e5acbc865406fc9a2559-Paper.pdf, 접근일 2026-10-12\n[^ref-1584]: LG CNS, LG CNS, 로봇 학습·운영 플랫폼 '피지컬웍스' 공개, 2026-05-07, https://www.lgcns.com/kr/newsroom/press/detail.rx-2605-1, 접근일 2026-10-12\n[^ref-1585]: Wang, Y. 외 (저자 대부분 AGIBOT(Finch) 소속·일부 Shanghai Innovation Institute 겸직·1명 Columbia University), Learning While Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies, 2026-09-16, https://arxiv.org/abs/2605.00416v4, 접근일 2026-10-12\n[^ref-1586]: NIST, Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1, 2023-01, https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf, 접근일 2026-10-12\n[^ref-1587]: European Union (EUR-Lex), Regulation (EU) 2024/1689 (Artificial Intelligence Act) — consolidated text 02024R1689-20260727 (incl. M1 Regulation (EU) 2026/1744), 2026-07-27, https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02024R1689-20260727, 접근일 2026-10-12\n[^ref-1588]: AI-Hub (한국지능정보사회진흥원), 대규모 물리환경 로봇조작 데이터, 2025-06-30, https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&dataSetSn=71825&topMenu=100, 접근일 2026-10-12"
        }
      ]
    },
    {
      "path": "docs/topics/2026/2026-10-12-area47-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 47. AI·학습·적응과 모델 운영 의 \"6. 대표 접근법과 기술\" 절(3,373자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-12-area47-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 47. AI·학습·적응과 모델 운영 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(2,813자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-12-area47-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 47. AI·학습·적응과 모델 운영 의 \"11. 열린 질문\" 절(2,002자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-12-area47-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 47. AI·학습·적응과 모델 운영 의 \"3. 왜 중요한가\" 절(1,551자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-12-area47-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 47. AI·학습·적응과 모델 운영 의 \"4. 핵심 개념과 용어\" 절(1,202자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-12-area47-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 47. AI·학습·적응과 모델 운영 의 \"8. 대표 연구와 자료\" 절(773자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-10-12 | 47. AI·학습·적응과 모델 운영 | 갱신: 인공지능기본법 개정 법률(2026-07-21 시행)·제34조와 EU AI Act 2026/1744 개정(기계류 부속서 I Section B 이동·제2조 2항) 반영, 모델 별칭 반영 시점·배포 묶음 호환성·ML Test Score Infra4·6·7·배포 중단·롤백 상태(벤더 주장)·KnowNo와 적응형 등각 추론의 보장 조건·LWD·AI-Hub 71825 분할 표기 불일치 추가, 기타 현장 사례(LG CNS, 벤더 주장), 열린 질문 id 부여와 새 질문 4건. 후속 정리 대상(이번 범위 밖): L. AI·학습 기술·M. 안전 대분류 페이지의 EU AI Act·인공지능기본법 시행일 서술, ref-168 저자 표기, 43. 데이터·관측성·배포 주제 페이지의 Mender 태그, 분리 주제 페이지(2026-09-25-area27-s4·s6·s7·s8)의 기존 문장 | run 2026-10-12-04",
  "index_updates": {
    "home_recent": "2026-10-12 — 47. AI·학습·적응과 모델 운영: 인공지능기본법 개정 법률 시행일·제34조와 EU AI Act 기계류 Section B 이동 반영, 모델 교체·되돌림(별칭 반영 시점·카나리·롤백 상태)과 등각 예측 보장 조건 보강",
    "category_recent": "2026-10-12 — 47. AI·학습·적응과 모델 운영: 법·규제 문단 정정(인공지능기본법 2026-07-21 개정 시행, EU AI Act 2026/1744), 모델 배포 묶음·롤백 상태·KnowNo·ACI 조건·LWD·AI-Hub 71825 추가, 새 열린 질문 4건",
    "area_recent": "2026-10-12 — 47. AI·학습·적응과 모델 운영: 3·5·9·11·13절 갱신, 4·6·7·8·10절에 2026-10-12 갱신 소절 추가(신규 출처 12건)"
  },
  "glossary_updates": [],
  "reference_updates": [
    {
      "id": "ref-1577",
      "org": "MLflow 프로젝트 (Linux Foundation 오픈소스 프로젝트)",
      "title": "Model Registry Workflows (docs/docs/classic-ml/model-registry/workflow.mdx, MLflow v3.1.0)",
      "published": "2025-06-10",
      "url": "https://github.com/mlflow/mlflow/blob/v3.1.0/docs/docs/classic-ml/model-registry/workflow.mdx",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-12",
      "summary": "MLflow v3.1.0 태그의 모델 레지스트리 작업 흐름 문서. 별칭 재지정 뒤 같은 로딩 코드의 다음 실행이 새 버전을 가져온다고 설명한다. 발행일은 3.1.0 판 공개일 기준이며 latest 문서(ref-626)와 다른 고정 판이다.",
      "cited_by": [
        "docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md"
      ],
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
      "summary": "LeRobot v0.6.0 태그의 하위 호환성 문서(정규화의 외부 PolicyProcessorPipeline 이동, 하드웨어 API 재설계 이전 궤적의 재생 오류). 같은 태그의 lerobot-dataset-v3.mdx 도 함께 열었다. 발행일은 0.6.0 판 공개일 기준.",
      "cited_by": [
        "docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md"
      ],
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
      "cited_by": [
        "docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md"
      ],
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
      "summary": "Greengrass v2 의 배포·장치별 배포 상태 정의(롤백 미요청·롤백 완료·롤백 실패).",
      "cited_by": [
        "docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md"
      ],
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
      "cited_by": [
        "docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md"
      ],
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
      "cited_by": [
        "docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md"
      ],
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
      "summary": "분포 이동 아래 등각 예측 임계값을 온라인으로 조정하는 적응형 등각 추론(NeurIPS 34, pp.1660–1672). 장기 경험적 포함 빈도 보장을 주며 실험은 주가 변동성·선거 데이터다.",
      "cited_by": [
        "docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md"
      ],
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
      "summary": "LG CNS 보도자료(뉴스와이어 재게시 동일). 피지컬웍스 포지·바통의 학습–운영 연계, 100대 기준 기대 효과, PoC·부산 스마트시티 활용을 회사가 주장한다.",
      "cited_by": [
        "docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1585",
      "org": "Wang, Y. 외 (저자 대부분 AGIBOT(Finch) 소속, 일부 Shanghai Innovation Institute 겸직, 1명 Columbia University)",
      "title": "Learning While Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies",
      "published": "2026-09-16",
      "url": "https://arxiv.org/abs/2605.00416v4",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-12",
      "summary": "제조사 중심 연구 프리프린트(v1 2026-05-01, v4 2026-09-16, 학회 게재 미확인). 자사 Agibot G1 16대 플릿에서 배포 중 오프라인–온라인 강화학습을 하고 에피소드 경계에서 정책을 갱신한다.",
      "cited_by": [
        "docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md"
      ],
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
      "cited_by": [
        "docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md"
      ],
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
      "summary": "AI Act 2026-07-27 통합판. 개정 (EU) 2026/1744(2026-07-08 채택, 관보 2026-07-24)으로 기계류 규정이 부속서 I Section B 로 옮겨졌고 제2조 2항이 Section B 관련 고위험 AI 의 적용 조문을 한정한다. 제43조 4항·제72조 2항 확인.",
      "cited_by": [
        "docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md"
      ],
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
      "cited_by": [
        "docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md"
      ],
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
      "summary": "ML 시스템 운영 준비도 28개 항목 기준표. 이번에 IEEE Big Data 2017 원고 PDF(DOI 10.1109/BigData.2017.8258038, pp.1123–1132)에서 Infra4·Infra6·Infra7 을 확인했다.",
      "cited_by": [
        "docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md"
      ],
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
      "summary": "KnowNo 논문(arXiv 2023-07). 이번에 학회판 PMLR 229:661–682(CoRL 2023)의 §3.1~3.3 에서 i.i.d.·정확한 사람 도움 가정과 시퀀스 수준 보정을 확인했다.",
      "cited_by": [
        "docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md"
      ],
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
      "summary": "인공지능기본법. 이번에 국가법령정보센터 조문(법률 제21311호, 2026-01-20 일부개정·공포, 2026-07-21 시행)에서 제34조 1항 각 호를 확인했다. 발행일은 이 개정판의 공포일이다.",
      "cited_by": [
        "docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md"
      ],
      "source_unopened": false
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "학습 모델·전처리기(정규화 통계)·하드웨어 보정판이 함께 바뀌는 변경을 로봇 플릿에서 어느 시험 단위로 승인하고, 실패 시 어느 묶음 단위로 복구할 것인가?",
      "areas": [
        47,
        57
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "운영 중 학습 정책을 에피소드 경계에서 갱신하는 방식이 제조사가 다른 이기종 로봇과 중간에 끊을 수 없는 장기 임무에서도 적절한가, 임무 도중 정책 판이 바뀌지 않게 하는 경계를 어떻게 정할 것인가?",
      "areas": [
        47,
        43
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "출처 충돌: AI-Hub 대규모 물리환경 로봇조작 데이터(71825) 설명 페이지 한 곳 안에서 분할 표제(학습 80%·테스트 10%)와 건수(238,266·23,900), 원천 분포 비율(14.29%·85.71%)과 수량(77,984·184,182), 라벨링 JSON 합계(524,332)와 건수 합(262,166)이 서로 맞지 않는데, 어느 값이 맞으며 실제 배포 파일과 일치하는가?",
      "areas": [
        47
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "모델 공급자와 ROP 가 함께 확인할 수 있는 모델 변경·배포·복구 증거(판 식별, 승인 기록, 장치별 적용·롤백 결과)의 최소 항목은 무엇인가?",
      "areas": [
        47,
        59
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "물류창고",
      "item": "시작 조건",
      "link": "docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md#5-적용-사례-현장-유형-명시",
      "title": "47. AI·학습·적응과 모델 운영"
    },
    {
      "site_type": "물류창고",
      "item": "수행 자원",
      "link": "docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md#5-적용-사례-현장-유형-명시",
      "title": "47. AI·학습·적응과 모델 운영"
    },
    {
      "site_type": "물류창고",
      "item": "제약",
      "link": "docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md#5-적용-사례-현장-유형-명시",
      "title": "47. AI·학습·적응과 모델 운영"
    },
    {
      "site_type": "물류창고",
      "item": "예외·성과",
      "link": "docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md#5-적용-사례-현장-유형-명시",
      "title": "47. AI·학습·적응과 모델 운영"
    },
    {
      "site_type": "기타",
      "item": "수행 자원",
      "link": "docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md#5-적용-사례-현장-유형-명시",
      "title": "47. AI·학습·적응과 모델 운영"
    }
  ],
  "standards_updates": [
    {
      "name": "LeRobot v0.6.0 (하위 호환성 문서·LeRobotDataset v3.0 형식)",
      "kind": "오픈소스",
      "org": "Hugging Face LeRobot 기여자 (huggingface/lerobot)",
      "url": "https://github.com/huggingface/lerobot/blob/v0.6.0/docs/source/backwardcomp.mdx",
      "related_areas": [
        47,
        57
      ],
      "summary": "로봇 학습 정책·데이터셋 라이브러리. v0.6.0 은 정규화를 외부 전·후처리 파이프라인으로 옮긴 변경을 호환성 깨짐으로 표시하고, LeRobotDataset v3.0 은 에피소드 구간을 메타데이터로 복원한다.",
      "ref_id": "ref-1578"
    },
    {
      "name": "EU AI Act 2026-07-27 통합판 (Regulation (EU) 2026/1744 개정 반영: 부속서 I Section B·제2조 2항·제43조 4항·제72조 2항)",
      "kind": "프레임워크",
      "org": "European Union (EUR-Lex)",
      "url": "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02024R1689-20260727",
      "related_areas": [
        47,
        59
      ],
      "summary": "기계류 규정 (EU) 2023/1230 이 부속서 I Section B 로 옮겨졌고, 제2조 2항이 Section B 관련 고위험 AI 의 적용 조문을 한정한다. 제43조 4항은 실질적 변경 시 재평가, 제72조 2항은 시판 후 감시를 정한다.",
      "ref_id": "ref-1587"
    }
  ],
  "additional_research_requests": [
    "4·6·7·8·10절이 분리된 주제 페이지(docs/topics/2026/2026-09-25-area27-s4·s6·s7·s8·s10.md)의 본문이 이번 입력에 없어, 1차 검증이 지시한 기존 문장(s6 57행 KnowNo 보장, s4 41·44행 등각 예측·모델 레지스트리, s7 44·48행 MLflow 행·관련 법 문단)을 제자리에서 고치지 못하고 세부영역 페이지의 해당 절에 '2026-10-12 갱신' 소절로 덧붙였다. 다음 갱신 실행에서 해당 주제 페이지를 입력으로 주어 옛 법 문단('2026-01-22 시행'만 적은 문장, 'AI Omnibus 논의')을 직접 정정해야 한다(하루 갱신 상한 2 안에서).",
    "11절 oq-213 의 질문 문장이 입력(대상 영역 47 의 열린 질문 요약)에 없어 부분 근거만 적었다. 질문 문장 확인이 필요하다.",
    "5절 기타 현장 사례(부산 스마트시티 국가 시범도시)의 시작 조건·작업 대상·제약·완료·인계·예외·성과는 공개 근거가 없어 '미확인'으로 두었다. 사업 주관 기관 자료나 독립 기사로 칸을 채울 근거가 필요하다.",
    "트랙 반영 제안 15건(data/area_reflection_proposals.json)은 1차 검증 지시대로 반영하지 않았다. 반영하려면 각 제안의 근거(ref-674·ref-675·ref-711·ref-684·ref-677·ref-769~776 등)를 이번 영역 실행의 finding 으로 재조사·검증해야 하며, 제안에 적힌 옛 번호는 25. 작업 배정 — MRTA, 31. 사람–로봇 협업, 15. 지도·공간·위치 모델, 54. 시험·형식 검증·벤치마크, 26. 작업 순서·스케줄링으로 바꿔야 한다.",
    "EU AI Act 제2조 2항 아래 기계류 규정 (EU) 2023/1230 쪽에 AI 고위험 요구(제72·73조 포함)가 위임법령으로 어떻게 통합되는지, 인공지능기본법 시행령 개정판(검증 보고상 2026-08-18 공포)의 고영향 영역 목록·문서 보존 기간을 원문으로 확인해야 3·7절과 oq-105·oq-106 을 더 진전시킬 수 있다."
  ],
  "fixes_applied": [
    "f24 저자 소속 — 6절 LWD 문장과 8절 항목을 '저자 대부분 AGIBOT(Finch) 소속(일부 Shanghai Innovation Institute 겸직, 1명 Columbia University)'로 쓰고 ref-1585 각주·참고문헌 org 도 같이 고쳤으며, 제조사 연구·저자 보고·프리프린트(학회 게재 미확인)·동일 기종 플릿(이기종 아님) 표기는 유지했다.",
    "용어 충돌 — 3·7절에서 '실질적 변경(Substantial Modification)'으로 쓰고 7절에서 용어집 substantial-modification 에 링크했으며, 6절의 단계적 배포를 용어집 phased-rollout 에 링크하고 모든 절·질문에서 '단계 배포'를 쓰지 않았다.",
    "의견 주체 명시 — f2·f6·f11·f17·f23·f27·f31·f37·f39·f46·f50 문장을 모두 '이 위키는 … 본다' 형식으로 쓰고 근거 출처 각주만 붙였다.",
    "벤더 주장 — f7~f10·f12·f13·f28~f30 문장을 'Mender·AWS IoT Jobs·Greengrass·Viam 문서(LG CNS 발표)에 따르면'으로 시작하고 '[추정] 벤더 주장'을 병기했으며, f29 의 15%·18% 는 '회사가 기대치로 제시한 값(실측 아님)'으로 쓰고 두 AWS 문서는 교차 확인으로 세지 않는다고 6절에 적었다.",
    "5절 — Viam·LWD 는 5절에 넣지 않고 6·8절에만 두었고, LG CNS 는 현장 유형 '기타'(부산 스마트시티 국가 시범도시, 회사 발표) 사례로 수행 자원 칸만 벤더 주장으로 채우고 나머지는 '미확인'으로 두었으며, 출하 시나리오 예외·성과 칸에 f1·f15·f16 을 보강하고 site_matrix_updates 는 실제로 채운 칸만 냈다.",
    "3절 법·규제 문단 — '2026-01-22 시행' [사실] 문장은 유지하고 미확인 문장을 '개정 법률(법률 제21311호, 2026-01-20 공포)은 2026-07-21 시행되었고, 고영향 영역 목록은 미확인이다'로 바꿨으며, EU 문장은 유지한 채 f40·f41 로 보충하고 '개정(AI Omnibus) 논의로'를 '개정(Regulation (EU) 2026/1744)과 관련해'로 고쳐 적용 시점은 확정하지 않았다.",
    "f45 — 3절과 7절에서 [추정]으로 쓰고 바로 다음 문장에 '이는 법률 판단이 아니며, 기계류 규정 (EU) 2023/1230 쪽에 AI 고위험 요구가 어떻게 통합되는지는 확인하지 않았다'를 두었으며, 제43조 4항·제72조 2항은 7절의 '조문 내용 소개'로만 두었다.",
    "각주 정의 — 13절을 교체해 ref-620 발행일을 2026-01-20·접근일 2026-10-12 로 바꾸고 '(원문 미열람)'을 뗐으며, ref-351·ref-625 접근일을 2026-10-12 로 바꾸고 '(원문 미열람)'을 뗐고, ref-351 인용 본문(4·6·8절)에 CoRL 2023, PMLR 229 를 밝혔으며, ref-1577~ref-1588 은 브리프 sources 값대로 각주를 만들었다.",
    "f34~f36 — 7절에서 90.9%·9.1%·약 70%(70.3%)·29.7% 를 모두 '이 위키가 계산한 값'으로 밝히고, 표제 비율·합계 가운데 어느 값이 맞는지 판정하지 않는다고 적었다.",
    "KnowNo·등각 예측 — 4절과 6절 갱신 소절에서 기존 보장 서술에 f18·f19·f20 을 조건으로 덧붙였고, f21 의 ACI 는 '장기 평균 포함 빈도(매 시점·로봇 안전 보장 아님, 로봇 실험 없음)'로 쓰고 KnowNo 와 교차 확인 관계가 아니라고 명시했다.",
    "6절 범위 — 장치 업데이트 도구(f7~f13)는 모델 교체·되돌림 관점의 짧은 소절로 두고 43. 데이터·관측성·배포와 57. 자산·소프트웨어 수명주기 관리에 번호와 이름으로 링크했으며, LWD 의 저수준 조작 정책 학습은 로봇 자체 지능·제어 연계 대상으로 밝히고 정책 판 갱신 경계·운영 기록 관점으로만 썼다.",
    "7·9절 — f38(MANAGE 4.1)을 두 절 모두 '법적 의무가 아닌 자율 적용 프레임워크'로 썼고, 9절의 역할 분리(f39)와 복구 실패 로봇 배정 제외(f11)는 [의견]으로 두었으며, 법 해석은 59. 법·규제·보험·라이선스에 연결하고 개별 ROP 의무 발생 여부는 판단하지 않는다고 적었다.",
    "11절 — 세 질문에 oq-105·oq-106·oq-107 을 붙이고 이 셋과 oq-213·oq-222 를 '열림'으로 둔 채 부분 근거만 적었으며, oq-030 에서 '이번 실행에서는 조사하지 않았다'를 지우고 oq-356 만 연결했고 LTAA 수치는 넣지 않았으며, 새 질문 4건을 등록하면서 세 번째 질문은 AI-Hub 한 페이지 안의 표기 불일치임이 드러나게 썼다.",
    "트랙 반영 제안 15건 — 본문에 반영하지 않고 '제안' 상태로 두었으며, 재조사 필요와 새 번호 대응을 additional_research_requests 에 적었다.",
    "직접 인용 — 원문 구절의 직접 인용은 ref-1588 의 '태그 추가' 한 곳뿐이며, ref-1587·ref-625·ref-351·ref-1585 를 포함한 나머지는 모두 재서술했다.",
    "범위 밖 페이지 — L. AI·학습 기술·M. 안전 대분류 페이지, ref-168 저자 표기, 43. 데이터·관측성·배포 주제 페이지의 Mender 태그는 고치지 않고 changelog_entry 에 후속 정리 대상으로만 적었다.",
    "분량 초과 자동 분리: 47. AI·학습·적응과 모델 운영 본문 15,616자 > 기준 4,000자 → 6개 절을 주제 페이지로 옮김, 남은 본문 4,828자"
  ]
}
```

### runs/2026-10-12-04/pages/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md

```markdown
---
title: "47. AI·학습·적응과 모델 운영"
type: area
category: "L. AI·학습 기술"
area_no: 47
related_areas: [5, 15, 21, 25, 31, 38, 43, 48, 54, 55, 57, 59]
tags: [LLM 계획 접지, 등각 예측, 학습 기반 배차, 모델 레지스트리, 단계적 배포, AI 위험관리]
status: draft
confidence: medium
created: 2026-09-24
updated: 2026-10-12
sources: [ref-617, ref-618, ref-619, ref-620, ref-621, ref-088, ref-092, ref-351, ref-622, ref-623, ref-624, ref-625, ref-626, ref-627, ref-354, ref-359, ref-056, ref-541, ref-417, ref-1577, ref-1578, ref-1579, ref-1580, ref-1581, ref-1582, ref-1583, ref-1584, ref-1585, ref-1586, ref-1587, ref-1588]
last_run: 2026-10-12
version: 3
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

자세한 내용은 주제 페이지 [47. AI·학습·적응과 모델 운영 — 왜 중요한가](../../topics/2026/2026-10-12-area47-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 영역의 기준을 이해하려면 LLM 출력을 현실과 잇는 개념과 모델을 관리하는 개념을 함께 알아야 한다.

자세한 내용은 주제 페이지 [47. AI·학습·적응과 모델 운영 — 핵심 개념과 용어](../../topics/2026/2026-10-12-area47-s4.md)에 있다.

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
| 예외·성과 | 모델 레지스트리의 버전·별칭으로 교체·되돌림 경로를 두고 교체 전 시험·감시 기준을 통과시켜야, 데이터 의존성·숨은 피드백 루프 같은 ML 고유 위험에서 오는 배정 품질 저하가 출하 지연으로 번지는 것을 막을 수 있을 것으로 보인다. [추정][^ref-626][^ref-625][^ref-623][^ref-624] MLflow v3.1.0 문서 기준으로 별칭 재지정은 같은 별칭으로 모델을 불러오는 코드가 다음에 실행될 때 반영된다. [사실][^ref-1577] ML Test Score는 오프라인 시험만으로는 운영 성능을 보장할 수 없다며 소수 트래픽에 먼저 내보내는 카나리를 완화책으로 들고, 롤백을 비상 절차로 두되 평상시에 연습하라고 권고한다(일반 ML 서비스 지침). [사실][^ref-625] |

피킹 시나리오에서 이 영역이 관여하는 칸은 시작 조건(지시가 작업으로 바뀌는 순간)과 예외·성과(되묻기)다. 출하 시나리오에서는 모델 교체가 예외·성과 칸의 위험이 된다.

국내 기사에 따르면 한진은 대전 메가허브에 AI 기반 적재량 예측 시스템을 적용해 간선차량 상·하차 종료 시점을 미리 파악하고 다음 차량 접안 대기시간을 줄였다고 한다. [추정] 벤더 주장[^ref-627] 이런 예측을 ROP 관점에서 쓴다면 ROP의 몫은 입출고 시간·접안·현장 상·하차 작업의 동기화까지이고, 간선 배차·운송계획은 분류 원문 19장 “거점 간 운송”의 연계 대상이다([범위 경계](../../about/scope-boundary.md)).

**현장 유형:** 기타

**사례:** 부산 스마트시티 국가 시범도시의 서비스 로봇 4종 통합 관제(회사 발표)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 미확인 |
| 수행 자원 | LG CNS 발표에 따르면 로봇 학습·운영 플랫폼 ‘피지컬웍스’의 운영·관제 도구 바통(Baton)이 부산 스마트시티 국가 시범도시 사업에서 순찰·바리스타·짐캐리·청소 4종 로봇의 통합 관제에 쓰이고 있다. [추정] 벤더 주장[^ref-1584] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 미확인 |

LG CNS 발표(2026-05-07)에 따르면 피지컬웍스의 포지(Forge)에서 학습·검증한 로봇을 바통으로 운영·관제하고, 이 과정에서 쌓인 데이터를 다시 학습에 쓰는 선순환 체계를 구축했다고 한다. [추정] 벤더 주장[^ref-1584] 같은 발표에 따르면 AMR·AGV 등 100대 규모 운영 환경에 바통을 적용하면 생산성이 약 15% 이상 오르고 운영비가 최대 18% 줄 것으로 기대된다고 하나, 이는 회사가 기대치로 제시한 값(실측 아님)이다. [추정] 벤더 주장[^ref-1584] 같은 발표에 따르면 포지는 20곳 이상 고객사와 개념검증(Proof of Concept, PoC)을 진행 중이며, 이 주장은 독립적으로 확인되지 않았다. [추정] 벤더 주장[^ref-1584]

이 사례에서 이 영역이 관여하는 부분은 학습과 운영 사이의 모델 갱신이지만, 공개 자료로 채울 수 있는 칸은 수행 자원뿐이었다. 이 위키는 학습·운영 연계 플랫폼을 도입 검토할 때 시연, PoC, 상시 운영을 서로 다른 수준의 증거로 받고, 모델 갱신 이력·고객 검수·장애 복구 기록을 따로 요청하는 편이 좋다고 본다. [의견][^ref-1584]

## 6. 대표 접근법과 기술

LLM이 만든 계획은 실행 가능성 확인, 형식 검증, 되묻기, 안전 판정을 거쳐야 하고, 학습 모델은 운영 중 버전·시험 관리가 따로 필요하다. [추정][^ref-088][^ref-626] 3절의 겹 구조를 이 위키가 그린 도식은 주제 페이지에 있다.

자세한 내용은 주제 페이지 [47. AI·학습·적응과 모델 운영 — 대표 접근법과 기술](../../topics/2026/2026-10-12-area47-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

조직 차원의 AI 위험관리·관리 체계 표준과 모델 운영 도구, 평가용 데이터가 이 영역의 기준을 받친다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [47. AI·학습·적응과 모델 운영 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-12-area47-s7.md)에 있다.

## 8. 대표 연구와 자료

이 절의 자료는 대부분 원문 미열람 상태에서 검색 결과로 확인했고, AmbiK와 LoTa-Bench는 검증 과정에서 공식 저장소 README로 확인했다. 수치는 저자 보고다.

자세한 내용은 주제 페이지 [47. AI·학습·적응과 모델 운영 — 대표 연구와 자료](../../topics/2026/2026-10-12-area47-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

ROP가 직접 맡을 AI 관련 몫은 LLM·학습 모델이 낸 계획·배정·해석을 실행에 채택하는 기준과 검증 단계, 사람 확인 요청, 채택·거부 기록, 운영 모델의 버전·변경 승인 관리로 보인다. [추정][^ref-618][^ref-617][^ref-619][^ref-351][^ref-626]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | AI가 낸 계획의 실행 가능 여부 확인, 채택·거부와 기록 | 인식 출력 처리·파지·저수준 동작 정책을 학습하거나 생성하는 모델(연계 대상) |
| 상위 업무 시스템 | 주문·납기 제약을 받은 배정·계획 모델의 버전·변경 승인 | 수요예측 모델(연계 대상) |
| 거점 간 운송 | 입출고 시간·접안·현장 상·하차 작업 동기화 | 간선 배차·운송계획(연계 대상) |

연계 대상: Code as Policies의 저수준 정책 코드, SayCan의 사전 학습 기술 같은 저수준 정책·파지 학습과 수요예측 모델은 로봇 자체 지능·제어와 상위 업무 시스템 쪽이며, ROP는 그 결과와 가능 여부를 받아 쓰는 쪽으로 보인다. [추정][^ref-622][^ref-088] 조직 차원의 AI 관리 체계(ISO/IEC 42001)와 위험관리(NIST AI RMF, ISO/IEC 23894)는 ROP의 채택 기준을 둘러싼 운영 틀로 보인다. [추정][^ref-618][^ref-617][^ref-619] 경계는 제품 전략에 따라 이동할 수 있으며, 자세한 기준은 [범위 경계](../../about/scope-boundary.md)에 있다.

### 배포 후 감시·변경관리·복구 실패 처리

NIST AI RMF 1.0의 MANAGE 4.1은 배포 후 AI 시스템 감시 계획에 사용자·관련 AI 행위자 의견 수집·평가, 이의 제기와 무효화, 폐기, 사고 대응, 복구, 변경관리 장치를 넣어 실행하도록 하는 항목이며, 법적 의무가 아닌 자율 적용 프레임워크다. [사실][^ref-1586] 이 위키는 모델 공급자의 학습·검증 책임, ROP의 배포·실행 판 기록, 현장 운영자의 개입·사고 통보 역할을 계약과 운영 절차에서 따로 정해야 하며, 조직 단위 관리 체계 인증만으로 특정 로봇 모델의 안전 성능을 승인해서는 안 된다고 본다. [의견][^ref-1586] 같은 맥락에서 이 위키는 ROP가 배포 중단·이전 모델 복원 시도·복원 확인을 서로 다른 상태로 기록하고, 복구하지 못한 로봇을 새 작업 배정에서 빼는 정책을 맡는 편이 맞다고 본다. [의견][^ref-1579][^ref-1580][^ref-1581] 장치 업데이트 실행 수단은 [43. 데이터·관측성·배포](../platform-architecture-and-infrastructure/data-observability-and-deployment.md), 법 해석과 의무 발생 판단은 [59. 법·규제·보험·라이선스](../governance-law-and-society/law-regulation-insurance-and-licensing.md)와 법무·운영 사업자 쪽 연계 대상이며, 이 페이지는 개별 ROP의 의무 발생 여부를 판단하지 않는다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

분류 개정 전 원문 8장의 교차 규칙에 따라 이 영역의 AI 방법은 적용 대상 영역과 양쪽으로 연결된다.

자세한 내용은 주제 페이지 [47. AI·학습·적응과 모델 운영 — 다른 연구영역과의 연결](../../topics/2026/2026-09-25-area27-s10.md)에 있다.

### 2026-10-12 갱신으로 더한 연결

- [43. 데이터·관측성·배포](../platform-architecture-and-infrastructure/data-observability-and-deployment.md) — 장치 업데이트 도구의 단계적 배포·배포 중단·롤백 상태가 모델 교체·되돌림의 실행 수단이 된다.
- [57. 자산·소프트웨어 수명주기 관리](../verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) — 가중치·전처리기·데이터 형식·보정판을 묶은 배포 묶음의 판 관리와 이전 묶음 보존이 이어진다.
- [59. 법·규제·보험·라이선스](../governance-law-and-society/law-regulation-insurance-and-licensing.md) — 한국 인공지능기본법 제34조의 문서 책무와 EU AI Act 개정(부속서 I Section B, 제2조 2항)의 해석이 이어진다.

## 11. 열린 질문

아직 확인하지 못한 사실과 판단이 필요한 쟁점은 다음과 같다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [47. AI·학습·적응과 모델 운영 — 열린 질문](../../topics/2026/2026-10-12-area47-s11.md)에 있다.

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
[^ref-088]: Ahn, M. 외, Do As I Can, Not As I Say: Grounding Language in Robotic Affordances, 2022-04, https://arxiv.org/abs/2204.01691, 접근일 2026-09-25 (원문 미열람)
[^ref-092]: Liu, B. 외, LLM+P: Empowering Large Language Models with Optimal Planning Proficiency, 2023-04, https://arxiv.org/abs/2304.11477, 접근일 2026-09-25 (원문 미열람)
[^ref-351]: Ren, A. Z. 외, Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners, 2023-07, https://arxiv.org/abs/2307.01928, 접근일 2026-10-12
[^ref-622]: Liang, J. 외, Code as Policies: Language Model Programs for Embodied Control, 2022-09, https://arxiv.org/abs/2209.07753, 접근일 2026-09-25 (원문 미열람)
[^ref-623]: Agrawal, A. 외, RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments, 2022-09, https://arxiv.org/abs/2209.05738, 접근일 2026-09-25 (원문 미열람)
[^ref-624]: Sculley, D. 외, Hidden Technical Debt in Machine Learning Systems, 2015, https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems, 접근일 2026-09-25 (원문 미열람)
[^ref-625]: Breck, E. 외 (Google Research), The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction, 2017, https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/, 접근일 2026-10-12
[^ref-626]: MLflow (Linux Foundation 오픈소스 프로젝트), ML Model Registry (MLflow AI Platform), 미확인, https://mlflow.org/docs/latest/ml/model-registry/, 접근일 2026-09-25 (원문 미열람)
[^ref-627]: 머니투데이, 포장은 로봇이, 간선운송은 무인차가…물류현장 스며든 '피지컬 AI', 2026-09-19, https://www.mt.co.kr/industry/2026/09/19/2026091818023697394, 접근일 2026-09-25 (원문 미열람)
[^ref-354]: cog-model (AmbiK 저자), AmbiK-dataset — README (AmbiK: Dataset of Ambiguous Tasks in Kitchen Environment), 미확인, https://github.com/cog-model/AmbiK-dataset, 접근일 2026-09-25 (원문 미열람)
[^ref-359]: Wang, W. 외, Learning to Ask: When LLM Agents Meet Unclear Instruction, 2024-09, https://arxiv.org/abs/2409.00557, 접근일 2026-09-25 (원문 미열람)
[^ref-056]: Liu, J. X. 외, Grounding Complex Natural Language Commands for Temporal Tasks in Unseen Environments, 2023-02, https://arxiv.org/abs/2302.11649, 접근일 2026-09-25 (원문 미열람)
[^ref-417]: arXiv (SafeGate 저자, 저자명 미확인), Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems, 2026-04, https://arxiv.org/abs/2604.05427, 접근일 2026-09-25 (원문 미열람)
[^ref-1577]: MLflow 프로젝트 (Linux Foundation 오픈소스 프로젝트), Model Registry Workflows (docs/docs/classic-ml/model-registry/workflow.mdx, MLflow v3.1.0), 2025-06-10, https://github.com/mlflow/mlflow/blob/v3.1.0/docs/docs/classic-ml/model-registry/workflow.mdx, 접근일 2026-10-12
[^ref-1579]: Northern.tech (Mender documentation), Create a custom Update Module, 미확인, https://docs.mender.io/artifact-creation/create-a-custom-update-module, 접근일 2026-10-12
[^ref-1580]: Amazon Web Services (AWS IoT Greengrass V2 Developer Guide), Check deployment status, 미확인, https://docs.aws.amazon.com/greengrass/v2/developerguide/check-deployment-status.html, 접근일 2026-10-12
[^ref-1581]: Amazon Web Services (AWS IoT Core Developer Guide), How job configurations work, 미확인, https://docs.aws.amazon.com/iot/latest/developerguide/jobs-configurations-details.html, 접근일 2026-10-12
[^ref-1584]: LG CNS, LG CNS, 로봇 학습·운영 플랫폼 '피지컬웍스' 공개, 2026-05-07, https://www.lgcns.com/kr/newsroom/press/detail.rx-2605-1, 접근일 2026-10-12
[^ref-1586]: NIST, Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1, 2023-01, https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf, 접근일 2026-10-12
```

### runs/2026-10-12-04/pages/topics/2026/2026-10-12-area47-s6.md

```markdown
---
title: "47. AI·학습·적응과 모델 운영 — 대표 접근법과 기술"
type: topic
category: "L. AI·학습 기술"
primary_area_no: 47
related_areas: [5, 15, 21, 25, 31, 38, 43, 48, 54, 55, 57, 59]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-088, ref-1577, ref-1579, ref-1580, ref-1581, ref-1582, ref-1583, ref-1585, ref-351, ref-625, ref-626]
last_run: 2026-10-12
version: 1
split_from: docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md#6
---

[홈](../../index.md) › [주제](../index.md) › 47. AI·학습·적응과 모델 운영 — 대표 접근법과 기술

# 47. AI·학습·적응과 모델 운영 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- LLM이 만든 계획은 실행 가능성 확인, 형식 검증, 되묻기, 안전 판정을 거쳐야 하고, 학습 모델은 운영 중 버전·시험 관리가 따로 필요하다. [추정][^ref-088][^ref-626] 3절의 겹 구조를 이 위키가 그린 도식은 주제 페이지에 있다.
- 이 페이지는 [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

LLM이 만든 계획은 실행 가능성 확인, 형식 검증, 되묻기, 안전 판정을 거쳐야 하고, 학습 모델은 운영 중 버전·시험 관리가 따로 필요하다. [추정][^ref-088][^ref-626] 3절의 겹 구조를 이 위키가 그린 도식은 주제 페이지에 있다.


### 2026-10-12 갱신: 모델 교체·되돌림과 보장 조건

주제 페이지의 ‘모델 운영 관리’와 ‘필요할 때 되묻기’ 소절에 아래 내용을 덧붙인다.

#### 운영 투입 승인·카나리·롤백 연습

ML Test Score(Breck 외, IEEE Big Data 2017)의 Infra4 항목은 모델이 실제 요청에 영향을 주기 전에 품질을 자동 검사해 모델을 승인하거나 거부해 운영 투입을 막는 절차를 권한다(일반 ML 서비스 운영 지침이며 로봇 안전 요구는 아님). [사실][^ref-625] Infra6 항목은 오프라인 시험이 아무리 넓어도 그것만으로 운영 환경 성능을 보장할 수 없다고 보고 소수 트래픽에 먼저 내보내는 카나리를 완화책으로 들며, Infra7 항목은 이전 정상판으로 되돌리는 롤백을 비상 절차로 두되 비상이 아닐 때 미리 연습하라고 권고한다(권고 강도). [사실][^ref-625] 이 위키는 카나리가 위험 완화 방법일 뿐 로봇의 물리적 위험 노출을 허가하는 근거가 아니므로, 로봇 모델의 운영 투입 승인 기록에 장치·현장별 성능 하한, 기존 판 대비 퇴행, 로딩·추론 지연, 개입·실패 사례, 실제 롤백 연습 결과를 연결하고 위험한 행동의 시험을 현장 안전 절차와 분리하지 않는 편이 좋다고 본다(보편 임계값은 정하지 않음). [의견][^ref-625]

기존 소절의 MLflow 별칭 교체 문장은 반영 시점과 함께 읽는다. MLflow v3.1.0 문서 기준으로 별칭 재지정은 같은 별칭으로 모델을 불러오는 코드가 다음에 실행될 때 반영된다. [사실][^ref-1577] 이 위키는 ROP가 레지스트리의 목표 모델 버전과 로봇마다 실제로 실행 중인 버전을 따로 기록하고, 별칭 변경 뒤 장치별 로딩·검증 응답을 받아야 교체가 끝났다고 보는 편이 맞다고 본다(플릿 전체 원자적 교체는 확인하지 못함). [의견][^ref-1577]

#### 장치 업데이트 도구에서 본 배포 중단과 롤백 상태

아래 도구는 [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md)와 [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md)에서 다루는 장치 업데이트 도구이며, 여기서는 모델 교체·되돌림 관점만 본다.

- Mender 문서에 따르면 사용자 정의 업데이트 모듈이 롤백을 지원하려면 롤백 지원 질의(SupportsRollback)에 ‘예’로 답하고, 설치 전에 알려진 정상 상태를 저장했다가 롤백 때 복원하는 구현을 모듈 작성자가 넣어야 한다. [추정] 벤더 주장[^ref-1579] 같은 문서에 따르면 전원 상실 뒤 업데이트 상태가 다시 실행될 수 있으므로 업데이트 모듈을 멱등하게 만들도록 권고한다. [추정] 벤더 주장[^ref-1579]
- AWS IoT Jobs 문서에 따르면 작업 배포 속도와 중단(abort) 설정을 두고, 실패한 장치 수 등이 지정한 기준에 이르면 작업 배포를 취소할 수 있으며, 이는 새 배포를 멈추는 것이지 이미 설치된 장치의 원복과는 별개다. [추정] 벤더 주장[^ref-1581]
- AWS IoT Greengrass v2 문서에 따르면 장치별 배포 실패 상태를 롤백 미요청, 이전 정상 구성으로 롤백 완료, 롤백 실패로 나누고, 롤백하지 않았거나 롤백에 실패한 장치는 정상 동작하지 않을 수 있다. [추정] 벤더 주장[^ref-1580] 두 AWS 문서는 같은 기관 자료라 서로의 교차 확인으로 세지 않는다.
- Viam 문서에 따르면 새 모델을 플릿에 내보낼 때 갱신한 구성 조각(fragment)을 먼저 첫 집단(예: 카나리 위치)에만 적용해 관찰한 뒤 나머지로 넓히는 [단계적 배포](../../glossary/phased-rollout.md) 절차를 둔다. [추정] 벤더 주장[^ref-1582] 같은 문서에 따르면 새 모델이 잘못 보이면 구성 조각에서 이전 판을 고정해 되돌리며, 장치는 다음 구성 동기화 때(정상 운영에서는 수 초 안에) 이전 판으로 수렴하고, 이는 연결이 끊긴 장치의 즉시 변경이 아니다. [추정] 벤더 주장[^ref-1582]

이 위키는 모델 배포가 배포 중단, 이전 모델 복원 시도, 복원 확인을 서로 다른 상태로 기록하고, 확대 배포 여부를 집단 성공률만이 아니라 장치별 현재 버전·실패 사유·복구 결과로 판단하며, 복구하지 못한 로봇은 새 작업 배정에서 빼는 운영 정책을 두는 편이 맞다고 본다. [의견][^ref-1579][^ref-1580][^ref-1581]

#### 필요할 때 되묻기 — 등각 예측 보장의 조건

주제 페이지의 KnowNo 보장 서술은 다음 조건 위에서 읽는다. KnowNo(CoRL 2023, PMLR 229)의 등각 예측 보장은 보정 집합과 새 시험 표본이 같은 분포에서 i.i.d.로 뽑힌다는 가정에 서고, 과제 성공 보장의 증명은 사람이 정확하게 도와준다는 가정에 기댄다. [사실][^ref-351] 다단계 계획에서는 시점 사이 의존성 때문에 i.i.d. 가정이 깨지므로 KnowNo는 개별 시점 대신 시퀀스 수준에서 보정하며, 이는 운영 분포가 임의로 바뀌는 경우까지 보장하는 것이 아니다. [사실][^ref-351]

분포가 시간에 따라 바뀌는 경우에는 적응형 등각 추론(Adaptive Conformal Inference, ACI; Gibbs·Candès, NeurIPS 2021)이 장기간의 경험적 포함 빈도가 목표값에 맞는다는 장기 평균 보장을 주며, 이는 매 시점 보장이나 로봇 안전 보장이 아니고 논문 실험도 주가 변동성·선거 데이터로 로봇 실험은 없다. [사실][^ref-1583] ACI의 온라인 갱신은 직전 예측 집합들이 정답을 놓친 경험적 빈도를 보고 임계값을 조정하므로, 운영 중 정답을 관측할 수 있어야 쓸 수 있다. [사실][^ref-1583] KnowNo와 ACI는 보장의 종류가 달라 서로의 교차 확인이 아니다. 이 위키는 물류 지시 분포가 바뀌는 현장에서 고정 간격(예: 매월) 재보정을 근거 없는 기본값으로 두지 말고, 지시 유형별 보정 오차와 데이터 변화 신호를 감시하며 피드백 지연·정답 수집 비용을 고려한 재보정 정책을 시험하는 편이 좋다고 본다(최적 주기는 미해결). [의견][^ref-351][^ref-1583]

#### 운영 중 학습하는 플릿의 정책 판 경계

로봇의 저수준 조작 정책 학습 자체는 로봇 자체 지능·제어 경계의 연계 대상이며, 여기서는 정책 판 갱신 경계와 운영 기록 관점만 본다. Learning While Deploying(LWD, arXiv v4 2026-09-16, 학회 게재 미확인 프리프린트)은 저자 대부분이 AGIBOT(Finch) 소속(일부 Shanghai Innovation Institute 겸직, 1명 Columbia University)인 제조사 연구로, 자사 Agibot G1 양팔 로봇 16대 플릿(식료품 보충 작업 4대, 장기 작업마다 3대)으로 8개 실물 조작 작업에서 온라인 학습을 했고 방법마다 실험당 4시간 벽시계 예산(플릿 합계 약 60시간)을 줬다(저자 보고, 동일 기종 플릿이며 이기종 아님). [사실][^ref-1585] 학습기는 50 학습 단계마다 갱신 정책을 플릿에 내보내고, 로봇은 에피소드 경계에서 새 정책을 다시 불러온다(연구 구현, 저자 보고). [사실][^ref-1585] 저자는 한계로 현재 학습 틀이 실행 안전을 명시적으로 모델링하지 않으며 직관적인 실시간 갱신 일정이 더 큰 규모의 배포에는 최적이 아닐 수 있다고 밝힌다. [사실][^ref-1585] 이 위키는 운영 중 학습하는 정책을 쓰는 플릿에서는 작업 이력마다 실행한 정책 판을 붙이고, 새 정책을 적용하는 경계(예: 에피소드·임무 단위)와 승인 주체를 명시해야 임무 도중 모델이 바뀌는 문제를 관리할 수 있다고 본다. [의견][^ref-1585]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-088]: Ahn, M. 외, Do As I Can, Not As I Say: Grounding Language in Robotic Affordances, 2022-04, https://arxiv.org/abs/2204.01691, 접근일 2026-09-25 (원문 미열람)
[^ref-1577]: MLflow 프로젝트 (Linux Foundation 오픈소스 프로젝트), Model Registry Workflows (docs/docs/classic-ml/model-registry/workflow.mdx, MLflow v3.1.0), 2025-06-10, https://github.com/mlflow/mlflow/blob/v3.1.0/docs/docs/classic-ml/model-registry/workflow.mdx, 접근일 2026-10-12
[^ref-1579]: Northern.tech (Mender documentation), Create a custom Update Module, 미확인, https://docs.mender.io/artifact-creation/create-a-custom-update-module, 접근일 2026-10-12
[^ref-1580]: Amazon Web Services (AWS IoT Greengrass V2 Developer Guide), Check deployment status, 미확인, https://docs.aws.amazon.com/greengrass/v2/developerguide/check-deployment-status.html, 접근일 2026-10-12
[^ref-1581]: Amazon Web Services (AWS IoT Core Developer Guide), How job configurations work, 미확인, https://docs.aws.amazon.com/iot/latest/developerguide/jobs-configurations-details.html, 접근일 2026-10-12
[^ref-1582]: Viam, Roll out a new model to a fleet, 미확인, https://docs.viam.com/vision/deploy-and-maintain/roll-out-to-fleet/, 접근일 2026-10-12
[^ref-1583]: Gibbs, I., & Candès, E. J. (NeurIPS 2021), Adaptive Conformal Inference Under Distribution Shift, 2021-12-06, https://papers.nips.cc/paper/2021/file/0d441de75945e5acbc865406fc9a2559-Paper.pdf, 접근일 2026-10-12
[^ref-1585]: Wang, Y. 외 (저자 대부분 AGIBOT(Finch) 소속·일부 Shanghai Innovation Institute 겸직·1명 Columbia University), Learning While Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies, 2026-09-16, https://arxiv.org/abs/2605.00416v4, 접근일 2026-10-12
[^ref-351]: Ren, A. Z. 외, Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners, 2023-07, https://arxiv.org/abs/2307.01928, 접근일 2026-10-12
[^ref-625]: Breck, E. 외 (Google Research), The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction, 2017, https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/, 접근일 2026-10-12
[^ref-626]: MLflow (Linux Foundation 오픈소스 프로젝트), ML Model Registry (MLflow AI Platform), 미확인, https://mlflow.org/docs/latest/ml/model-registry/, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-04 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-04 | 47. AI·학습·적응과 모델 운영 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-10-12-04/pages/topics/2026/2026-10-12-area47-s7.md

```markdown
---
title: "47. AI·학습·적응과 모델 운영 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "L. AI·학습 기술"
primary_area_no: 47
related_areas: [5, 15, 21, 25, 31, 38, 43, 48, 54, 55, 57, 59]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-1577, ref-1578, ref-1586, ref-1587, ref-1588, ref-620]
last_run: 2026-10-12
version: 1
split_from: docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md#7
---

[홈](../../index.md) › [주제](../index.md) › 47. AI·학습·적응과 모델 운영 — 관련 표준·프레임워크·오픈소스

# 47. AI·학습·적응과 모델 운영 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 조직 차원의 AI 위험관리·관리 체계 표준과 모델 운영 도구, 평가용 데이터가 이 영역의 기준을 받친다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.
- 이 페이지는 [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

조직 차원의 AI 위험관리·관리 체계 표준과 모델 운영 도구, 평가용 데이터가 이 영역의 기준을 받친다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.


### 2026-10-12 갱신

주제 페이지의 표에 다음 행을 더한다. 기존 MLflow 행의 근거(ref-626)는 최신(latest) 문서이고, 아래 행은 판을 고정한 문서다.

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| MLflow 모델 레지스트리(v3.1.0 고정 문서) | 오픈소스 | 별칭 재지정은 같은 별칭 로딩 코드가 다음에 실행될 때 반영된다 | [사실][^ref-1577] |
| LeRobot v0.6.0 하위 호환성 문서 | 오픈소스 | 정규화의 외부 전·후처리 파이프라인 이동을 호환성 깨짐으로 표시하고, 옛 보정 방식 궤적의 재생 오류를 경고한다 | [사실][^ref-1578] |
| LeRobotDataset v3.0 | 오픈소스 | 여러 에피소드를 큰 파일로 묶고 에피소드 구간을 메타데이터로 복원하는 데이터 형식 | [사실][^ref-1578] |
| NIST AI RMF 1.0(NIST AI 100-1) MANAGE 4.1 | 프레임워크 | 배포 후 감시 계획에 의견 수집·평가, 이의 제기·무효화, 폐기, 사고 대응, 복구, 변경관리 장치를 넣어 실행하도록 한다(법적 의무가 아닌 자율 적용 프레임워크) | [사실][^ref-1586] |

#### 국내 공개 로봇 조작 데이터의 판·분할 메타데이터

AI-Hub ‘대규모 물리환경 로봇조작 데이터’(dataSetSn 71825)의 변경이력은 v1.0을 2025-04-16 데이터 개방(Beta), v1.1을 2025-06-30 데이터 최종 개방으로 표시하고, 데이터 히스토리의 2026-05-06 항목은 ‘태그 추가’뿐이라 새 데이터 판으로 볼 근거가 없다. [사실][^ref-1588] 같은 페이지의 구성표는 총 262,166건 중 학습 238,266건, 테스트 23,900건을 적으면서 표제는 학습 80%·테스트 10%로 달았고, 검증 분할은 표기하지 않는다. [사실][^ref-1588] 건수로 이 위키가 계산하면 학습 약 90.9%·테스트 약 9.1%로 표제 비율과 맞지 않는다(원문 값이 아닌 계산값). 원천 데이터는 실제환경 77,984장, 가상환경 184,182장(RGB 기준, Depth도 같은 수)이다. [사실][^ref-1588] 이 위키의 계산으로는 약 70%(70.3%)가 가상환경에서 취득됐으므로, 실물 조작 성능 근거로 읽을 때 실제·가상을 구분해야 한다. 같은 페이지의 분포 표는 원천 데이터 비율을 실제 14.29%·가상 85.71%로 적어 수량으로 이 위키가 계산한 비율(약 29.7%·70.3%)과 맞지 않고, 라벨링 JSON 합계를 건수 합 262,166이 아닌 524,332로 적는다. [사실][^ref-1588] 어느 값이 맞는지는 제공자 확인 전까지 판정하지 않는다(11절 열린 질문). 이 위키는 이처럼 분할비·합계가 맞지 않는 공개 데이터는 제공자 확인 전에는 표제 분할비를 모델 승인 근거로 쓰지 말고, 실물·가상 구분, 중복, 평가용 누출을 실제 파일로 따로 검사하는 편이 좋다고 본다(실제 파일은 열지 않음). [의견][^ref-1588]

#### 관련 법 문단 갱신(주제 페이지의 2026-09-25 서술 보충)

주제 페이지의 관련 법 문단은 이 갱신 전 서술이며, 아래가 2026-10-12 기준이다. 법 해석과 의무 발생 판단은 [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md)와 연결하고, 이 페이지는 개별 ROP의 의무 발생 여부를 판단하지 않는다.

국가법령정보센터의 현행 조문은 「인공지능 발전과 신뢰 기반 조성 등에 관한 기본법」을 법률 제21311호(2026-01-20 공포·일부개정), 시행 2026-07-21 판으로 표시한다(2026-01-22 시행은 최초 법률·시행령 기준). [사실][^ref-620] 제34조 1항은 고영향 인공지능 제공 사업자의 안전성·신뢰성 확보 조치로 위험관리방안, 설명 방안, 이용자 보호, 사람의 관리·감독과 함께 5호의 조치 내용 확인 문서 작성·보관을 둔다. [사실][^ref-620] 이 위키는 ROP가 학습용 데이터 개요, 모델 판, 위험 조치, 사람 감독, 승인·복구 기록을 서로 연결해 두어 고영향 해당성이 판단되면 제34조 문서로 낼 수 있는 구조를 미리 갖추는 편이 좋다고 본다. [의견][^ref-620]

EU AI Act는 2026-07-27 통합판에서 기계류 규정이 부속서 I Section B로 옮겨졌고 제2조 2항이 Section B 관련 고위험 AI의 적용 조문을 한정한다(3절). 다음 두 조문은 조문 내용 소개이며, 기계류 연계 로봇 AI에 바로 적용되는 의무로 읽지 않는다. 제43조 4항은 적합성 평가를 거친 고위험 AI 시스템이 [실질적 변경](../../glossary/substantial-modification.md)(Substantial Modification)을 겪으면, 변경된 시스템을 다시 유통하든 같은 배포자가 계속 쓰든 새 적합성 평가 절차를 거치도록 정한다. [사실][^ref-1587] 같은 항은 출시·사용 개시 뒤에도 계속 학습하는 고위험 AI 시스템에서 제공자가 최초 적합성 평가 때 미리 정하고 부속서 IV 2(f) 기술문서에 담은 시스템·성능 변경은 실질적 변경으로 보지 않는다고 정한다. [사실][^ref-1587] 제72조 2항은 제공자의 시판 후 감시 체계가 배포자 제공 등으로 얻은 고위험 AI 시스템의 성능 데이터를 수명 전반에 걸쳐 능동적·체계적으로 수집·문서화·분석하고, 관련되면 다른 AI 시스템과의 상호작용 분석을 포함하도록 정한다. [사실][^ref-1587] 제2조 2항에 따라 이 두 조문은 Section A 법령·부속서 III 경로의 고위험 AI에 해당하는 내용으로 소개하며, 기계류 규정 대상 로봇의 안전 구성요소로서 고위험이 되는 AI에 AI Act 조문으로 바로 적용된다고 볼 수 없어 보인다. [추정][^ref-1587] 이는 법률 판단이 아니며, 기계류 규정 (EU) 2023/1230 쪽에 AI 고위험 요구가 어떻게 통합되는지는 확인하지 않았다. 이 위키는 EU 시장을 대상으로 할 때 적용 관할·시스템 분류·공급자 지위를 먼저 정하고, 최초 평가에서 허용한 변경 범위와 실제 모델 변경 내역을 대조할 수 있도록 변경 기록을 보존하는 편이 맞다고 본다. [의견][^ref-1587]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1577]: MLflow 프로젝트 (Linux Foundation 오픈소스 프로젝트), Model Registry Workflows (docs/docs/classic-ml/model-registry/workflow.mdx, MLflow v3.1.0), 2025-06-10, https://github.com/mlflow/mlflow/blob/v3.1.0/docs/docs/classic-ml/model-registry/workflow.mdx, 접근일 2026-10-12
[^ref-1578]: Hugging Face LeRobot 기여자 (huggingface/lerobot), Backward compatibility (docs/source/backwardcomp.mdx, LeRobot v0.6.0), 2026-07-06, https://github.com/huggingface/lerobot/blob/v0.6.0/docs/source/backwardcomp.mdx, 접근일 2026-10-12
[^ref-1586]: NIST, Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1, 2023-01, https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf, 접근일 2026-10-12
[^ref-1587]: European Union (EUR-Lex), Regulation (EU) 2024/1689 (Artificial Intelligence Act) — consolidated text 02024R1689-20260727 (incl. M1 Regulation (EU) 2026/1744), 2026-07-27, https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02024R1689-20260727, 접근일 2026-10-12
[^ref-1588]: AI-Hub (한국지능정보사회진흥원), 대규모 물리환경 로봇조작 데이터, 2025-06-30, https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&dataSetSn=71825&topMenu=100, 접근일 2026-10-12
[^ref-620]: 국가법령정보센터(과학기술정보통신부), 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법, 2026-01-20, https://www.law.go.kr/lsInfoP.do?lsiSeq=268543, 접근일 2026-10-12

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-04 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-04 | 47. AI·학습·적응과 모델 운영 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-10-12-04/pages/topics/2026/2026-10-12-area47-s11.md

```markdown
---
title: "47. AI·학습·적응과 모델 운영 — 열린 질문"
type: topic
category: "L. AI·학습 기술"
primary_area_no: 47
related_areas: [5, 15, 21, 25, 31, 38, 43, 48, 54, 55, 57, 59]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-1578, ref-1582, ref-1583, ref-1585, ref-1586, ref-1587, ref-1588, ref-351, ref-620]
last_run: 2026-10-12
version: 1
split_from: docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md#11
---

[홈](../../index.md) › [주제](../index.md) › 47. AI·학습·적응과 모델 운영 — 열린 질문

# 47. AI·학습·적응과 모델 운영 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 아직 확인하지 못한 사실과 판단이 필요한 쟁점은 다음과 같다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

아직 확인하지 못한 사실과 판단이 필요한 쟁점은 다음과 같다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- **oq-030** (상태: 열림) 출처 충돌: LTAA(arXiv 2512.02810) 초록 요약은 로봇 전문화가 강한 설정에서 LLM 배정이 작업 완료율 77%로 전통 기법을 모두 앞섰다고 하지만, 다른 2차 요약은 동적 계획법의 완료율이 더 높다고 적는다. 어느 쪽이 원문 결과인가? 관련 후속 질문은 oq-356(같은 성공 확률 모델·작업 집합으로 비교군을 재평가한 공개 재현 자료가 있는가)이다.
- **oq-105** (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-68) 물류 현장 로봇의 작업 계획·배정에 쓰는 AI가 한국 인공지능 기본법의 고영향 인공지능 영역에 해당하는가, 해당하면 ROP 사업자와 현장 운영사 중 누가 책무를 지는가? 부분 근거: 개정 법률 제21311호가 2026-07-21 시행되었고 제34조 1항 5호가 조치 내용 문서의 작성·보관을 정하나, 고영향 해당성·사업자 지위·시행령상 보존 기간은 확인하지 못했다(3절).[^ref-620]
- **oq-106** (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-68) LLM이나 학습 모델이 ROP의 정지·경로·구역 결정에 관여할 때 EU AI Act가 말하는 제품 안전 구성요소로 볼 수 있는가? 부분 근거: 2026-07-27 통합판에서 기계류 규정은 부속서 I Section B로 옮겨졌고 제2조 2항이 적용 조문을 한정한다는 점만 확인했으며, 제품 안전 구성요소 해당성은 판단하지 않았다(3·7절).[^ref-1587]
- **oq-107** (상태: 열림 · 제기 2026-09-25 · 실행 2026-09-25-68) KnowNo의 등각 예측 보장은 보정 데이터와 운영 분포가 같다는 조건에 기대는데, 물류 지시 분포가 계절·고객에 따라 바뀔 때 보정을 얼마나 자주 다시 해야 하는가? 부분 근거: KnowNo 보장은 i.i.d. 보정과 정확한 사람 도움 가정에 서고, 적응형 등각 추론은 정답 관측을 전제로 장기 평균 보장만 준다. 재보정 주기는 미해결이다(6절).[^ref-351][^ref-1583]
- **oq-213** (상태: 열림) 부분 근거: Viam 문서의 단계적 배포와 이전 판 고정·다음 구성 동기화 때 수렴하는 되돌림 절차(벤더 주장, 6절).[^ref-1582]
- **oq-222** (상태: 열림) 학습된 배정·경로 정책을 현장에 쓸 때 분포 이동을 감지해 탐색·규칙 기반 정책으로 되돌리는 기준을 정한 연구나 제품이 있는가? 부분 근거: 분포 이동 아래 온라인 재보정은 정답 관측을 요구한다는 점을 확인했으나, 배정 정책 되돌림 기준은 아니다(6절).[^ref-1583]
- (신규, 상태: 열림 · 제기 2026-10-12 · 실행 2026-10-12-04) 학습 모델·전처리기(정규화 통계)·하드웨어 보정판이 함께 바뀌는 변경을 로봇 플릿에서 어느 시험 단위로 승인하고, 실패 시 어느 묶음 단위로 복구할 것인가?[^ref-1578]
- (신규, 상태: 열림 · 제기 2026-10-12 · 실행 2026-10-12-04) 운영 중 학습 정책을 에피소드 경계에서 갱신하는 방식이 제조사가 다른 이기종 로봇과 중간에 끊을 수 없는 장기 임무에서도 적절한가, 임무 도중 정책 판이 바뀌지 않게 하는 경계를 어떻게 정할 것인가?[^ref-1585]
- (신규, 상태: 열림 · 제기 2026-10-12 · 실행 2026-10-12-04) 출처 충돌: AI-Hub 대규모 물리환경 로봇조작 데이터(71825) 설명 페이지 한 곳 안에서 분할 표제(학습 80%·테스트 10%)와 건수(238,266·23,900), 원천 분포 비율(14.29%·85.71%)과 수량(77,984·184,182), 라벨링 JSON 합계(524,332)와 건수 합(262,166)이 서로 맞지 않는데, 어느 값이 맞으며 실제 배포 파일과 일치하는가?[^ref-1588]
- (신규, 상태: 열림 · 제기 2026-10-12 · 실행 2026-10-12-04) 모델 공급자와 ROP가 함께 확인할 수 있는 모델 변경·배포·복구 증거(판 식별, 승인 기록, 장치별 적용·롤백 결과)의 최소 항목은 무엇인가?[^ref-1586]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1578]: Hugging Face LeRobot 기여자 (huggingface/lerobot), Backward compatibility (docs/source/backwardcomp.mdx, LeRobot v0.6.0), 2026-07-06, https://github.com/huggingface/lerobot/blob/v0.6.0/docs/source/backwardcomp.mdx, 접근일 2026-10-12
[^ref-1582]: Viam, Roll out a new model to a fleet, 미확인, https://docs.viam.com/vision/deploy-and-maintain/roll-out-to-fleet/, 접근일 2026-10-12
[^ref-1583]: Gibbs, I., & Candès, E. J. (NeurIPS 2021), Adaptive Conformal Inference Under Distribution Shift, 2021-12-06, https://papers.nips.cc/paper/2021/file/0d441de75945e5acbc865406fc9a2559-Paper.pdf, 접근일 2026-10-12
[^ref-1585]: Wang, Y. 외 (저자 대부분 AGIBOT(Finch) 소속·일부 Shanghai Innovation Institute 겸직·1명 Columbia University), Learning While Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies, 2026-09-16, https://arxiv.org/abs/2605.00416v4, 접근일 2026-10-12
[^ref-1586]: NIST, Artificial Intelligence Risk Management Framework (AI RMF 1.0), NIST AI 100-1, 2023-01, https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf, 접근일 2026-10-12
[^ref-1587]: European Union (EUR-Lex), Regulation (EU) 2024/1689 (Artificial Intelligence Act) — consolidated text 02024R1689-20260727 (incl. M1 Regulation (EU) 2026/1744), 2026-07-27, https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02024R1689-20260727, 접근일 2026-10-12
[^ref-1588]: AI-Hub (한국지능정보사회진흥원), 대규모 물리환경 로봇조작 데이터, 2025-06-30, https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&dataSetSn=71825&topMenu=100, 접근일 2026-10-12
[^ref-351]: Ren, A. Z. 외, Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners, 2023-07, https://arxiv.org/abs/2307.01928, 접근일 2026-10-12
[^ref-620]: 국가법령정보센터(과학기술정보통신부), 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법, 2026-01-20, https://www.law.go.kr/lsInfoP.do?lsiSeq=268543, 접근일 2026-10-12

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-04 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-04 | 47. AI·학습·적응과 모델 운영 의 "열린 질문" 절에서 분리 |
```

### runs/2026-10-12-04/pages/topics/2026/2026-10-12-area47-s3.md

```markdown
---
title: "47. AI·학습·적응과 모델 운영 — 왜 중요한가"
type: topic
category: "L. AI·학습 기술"
primary_area_no: 47
related_areas: [5, 15, 21, 25, 31, 38, 43, 48, 54, 55, 57, 59]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-056, ref-088, ref-092, ref-1587, ref-351, ref-359, ref-417, ref-618, ref-620, ref-621, ref-624, ref-625, ref-626]
last_run: 2026-10-12
version: 1
split_from: docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md#3
---

[홈](../../index.md) › [주제](../index.md) › 47. AI·학습·적응과 모델 운영 — 왜 중요한가

# 47. AI·학습·적응과 모델 운영 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- AI가 만든 계획·해석을 실행에 쓰는 기준은 한 가지 장치가 아니라 실행 가능성 접지, 형식 명세·계획기 경유 검증, 불확실할 때 사람 확인, 실행 전 안전 판정, 승인된 모델 버전·시험 기준이 겹친 구조로 정리될 수 있어 보인다. [추정][^ref-088][^ref-092][^ref-056][^ref-351][^ref-359][^ref-417][^ref-625][^ref-626][^ref-618] 이 구조는 각 출처가 다루는 서로 다른 단계를 이 위키가 묶은 것이며, 하나의 출처가 제시한 채택 기준은 아니다.
- 이 페이지는 [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

AI가 만든 계획·해석을 실행에 쓰는 기준은 한 가지 장치가 아니라 실행 가능성 접지, 형식 명세·계획기 경유 검증, 불확실할 때 사람 확인, 실행 전 안전 판정, 승인된 모델 버전·시험 기준이 겹친 구조로 정리될 수 있어 보인다. [추정][^ref-088][^ref-092][^ref-056][^ref-351][^ref-359][^ref-417][^ref-625][^ref-626][^ref-618] 이 구조는 각 출처가 다루는 서로 다른 단계를 이 위키가 묶은 것이며, 하나의 출처가 제시한 채택 기준은 아니다.

기준이 필요한 이유는 모델이 한 번 넣고 끝나는 부품이 아니기 때문이다. Sculley 외(2015)는 실제 머신러닝(Machine Learning, ML) 시스템이 일반 코드의 유지보수 문제에 더해 경계 침식, 얽힘, 숨은 피드백 루프, 선언되지 않은 소비자, 데이터 의존성 등 ML 고유 위험으로 큰 유지 비용을 낳는다고 지적했다. [사실][^ref-624]

규제도 같은 방향을 가리킨다. 한국 「인공지능 발전과 신뢰 기반 조성 등에 관한 기본법」과 시행령은 2026-01-22 시행되었고, 사람의 생명·안전·기본권에 중대한 영향을 미칠 수 있는 영역의 AI를 고영향 인공지능으로 두어 별도 책무를 부과한다(기준일 2026-01-22). [사실][^ref-620] 개정 법률(법률 제21311호, 2026-01-20 공포)은 2026-07-21 시행되었고, 고영향 영역 목록은 미확인이다. [사실][^ref-620] 현행 제34조 1항은 [고영향 인공지능](../../glossary/high-impact-ai.md)이나 이를 이용한 제품·서비스를 제공하는 인공지능사업자가 대통령령에 따라 안전성·신뢰성 확보 조치를 이행하도록 하고, 그 5호로 조치 내용을 확인할 수 있는 문서의 작성·보관을 둔다. [사실][^ref-620] 이 책무가 작업 계획·배정 AI를 쓰는 ROP에 걸리는지는 고영향 해당성과 사업자 지위(제공자·이용자) 판단이 먼저이며, 시행령상 보존 기간은 이번에 확인하지 못했다. [추정][^ref-620]

EU AI Act(Regulation (EU) 2024/1689)는 위험 기반 규제로, 부속서 I의 EU 조화 법령(기계류 등) 대상 제품의 안전 구성요소이거나 제품 자체이고 제3자 적합성 평가 대상인 AI 시스템을 고위험 AI로 분류한다. [사실][^ref-621] 2026-07-27 EUR-Lex 통합판은 Regulation (EU) 2026/1744(2026-07-08 채택, 관보 2026-07-24 게재) 개정을 반영하며, 이 개정으로 기계류 규정 (EU) 2023/1230이 부속서 I Section A에서 빠지고 Section B(21번)에 들어갔다. [사실][^ref-1587] 개정된 제2조 2항은 Section B 조화 법령 대상 제품과 관련해 제6조 1항으로 고위험이 되는 AI 시스템에는 제6조 1항, 제60a조, 제102~112조만 적용하고, 제57~59조는 해당 법령에 고위험 요구사항이 통합된 범위에서만 적용한다고 정한다. [사실][^ref-1587] 따라서 기계류 규정 대상 로봇의 안전 구성요소로서 고위험이 되는 AI에는 제43조(실질적 변경 시 재평가)와 제72조(시판 후 감시)가 AI Act 조문으로 바로 적용된다고 볼 수 없어 보인다. [추정][^ref-1587] 이는 법률 판단이 아니며, 기계류 규정 (EU) 2023/1230 쪽에 AI 고위험 요구가 어떻게 통합되는지는 확인하지 않았다. 적용 시점은 개정(Regulation (EU) 2026/1744)과 관련해 이 페이지에서 확정하지 않는다. 법 해석의 상세는 [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md)와 이어진다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-056]: Liu, J. X. 외, Grounding Complex Natural Language Commands for Temporal Tasks in Unseen Environments, 2023-02, https://arxiv.org/abs/2302.11649, 접근일 2026-09-25 (원문 미열람)
[^ref-088]: Ahn, M. 외, Do As I Can, Not As I Say: Grounding Language in Robotic Affordances, 2022-04, https://arxiv.org/abs/2204.01691, 접근일 2026-09-25 (원문 미열람)
[^ref-092]: Liu, B. 외, LLM+P: Empowering Large Language Models with Optimal Planning Proficiency, 2023-04, https://arxiv.org/abs/2304.11477, 접근일 2026-09-25 (원문 미열람)
[^ref-1587]: European Union (EUR-Lex), Regulation (EU) 2024/1689 (Artificial Intelligence Act) — consolidated text 02024R1689-20260727 (incl. M1 Regulation (EU) 2026/1744), 2026-07-27, https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02024R1689-20260727, 접근일 2026-10-12
[^ref-351]: Ren, A. Z. 외, Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners, 2023-07, https://arxiv.org/abs/2307.01928, 접근일 2026-10-12
[^ref-359]: Wang, W. 외, Learning to Ask: When LLM Agents Meet Unclear Instruction, 2024-09, https://arxiv.org/abs/2409.00557, 접근일 2026-09-25 (원문 미열람)
[^ref-417]: arXiv (SafeGate 저자, 저자명 미확인), Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems, 2026-04, https://arxiv.org/abs/2604.05427, 접근일 2026-09-25 (원문 미열람)
[^ref-618]: ISO/IEC, ISO/IEC 42001:2023 - AI management systems, 2023, https://www.iso.org/standard/42001, 접근일 2026-09-25 (원문 미열람)
[^ref-620]: 국가법령정보센터(과학기술정보통신부), 인공지능 발전과 신뢰 기반 조성 등에 관한 기본법, 2026-01-20, https://www.law.go.kr/lsInfoP.do?lsiSeq=268543, 접근일 2026-10-12
[^ref-621]: European Commission, AI Act (Shaping Europe's digital future), 미확인, https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai, 접근일 2026-09-25 (원문 미열람)
[^ref-624]: Sculley, D. 외, Hidden Technical Debt in Machine Learning Systems, 2015, https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems, 접근일 2026-09-25 (원문 미열람)
[^ref-625]: Breck, E. 외 (Google Research), The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction, 2017, https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/, 접근일 2026-10-12
[^ref-626]: MLflow (Linux Foundation 오픈소스 프로젝트), ML Model Registry (MLflow AI Platform), 미확인, https://mlflow.org/docs/latest/ml/model-registry/, 접근일 2026-09-25 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-04 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-04 | 47. AI·학습·적응과 모델 운영 의 "왜 중요한가" 절에서 분리 |
```

### runs/2026-10-12-04/pages/topics/2026/2026-10-12-area47-s4.md

```markdown
---
title: "47. AI·학습·적응과 모델 운영 — 핵심 개념과 용어"
type: topic
category: "L. AI·학습 기술"
primary_area_no: 47
related_areas: [5, 15, 21, 25, 31, 38, 43, 48, 54, 55, 57, 59]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-1577, ref-1578, ref-351]
last_run: 2026-10-12
version: 1
split_from: docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md#4
---

[홈](../../index.md) › [주제](../index.md) › 47. AI·학습·적응과 모델 운영 — 핵심 개념과 용어

# 47. AI·학습·적응과 모델 운영 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역의 기준을 이해하려면 LLM 출력을 현실과 잇는 개념과 모델을 관리하는 개념을 함께 알아야 한다.
- 이 페이지는 [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역의 기준을 이해하려면 LLM 출력을 현실과 잇는 개념과 모델을 관리하는 개념을 함께 알아야 한다.


### 2026-10-12 갱신: 보장의 전제와 배포 묶음

주제 페이지의 개념 목록에 다음 조건과 개념을 덧붙인다.

- **[등각 예측](../../glossary/conformal-prediction.md)(Conformal Prediction)의 전제** — KnowNo(CoRL 2023, PMLR 229)의 등각 예측 보장은 보정 집합과 새 시험 표본이 같은 미지의 분포에서 독립·동일 분포(independent and identically distributed, i.i.d.)로 뽑힌다는 가정 위에 서며, 과제 성공 보장의 증명은 사람이 정확하게 도와준다는 가정에 기댄다. [사실][^ref-351]
- **[모델 레지스트리](../../glossary/model-registry.md)(Model Registry) 별칭의 반영 시점** — MLflow v3.1.0 문서는 별칭(alias)을 새 모델 버전으로 재지정하면 같은 별칭으로 모델을 불러오는 코드가 다음에 실행될 때 새 버전을 가져온다고 설명할 뿐, 이미 실행 중인 프로세스나 연결이 끊긴 장치의 모델이 즉시 바뀐다고 말하지 않는다. [사실][^ref-1577]
- **정책·데이터 형식 호환성(Policy and Dataset Compatibility)** — LeRobot v0.6.0 하위 호환성 문서는 정책 가중치에 내장되던 정규화 계층을 없애고 외부 전·후처리 파이프라인(PolicyProcessorPipeline)이 정규화를 맡도록 바꾼 변경을 호환성 깨짐으로 명시하고, 이전 모델은 이전(migration)이 필요하다고 적는다. [사실][^ref-1578] 같은 문서는 하드웨어 API 재설계 이전의 보정 방식으로 기록한 궤적을 그대로 불러오면 잘못 재생된다고 경고한다(SO100·SO101 예시의 관절 보정·입출력 변환이며 다른 기종으로 일반화하지 않음). [사실][^ref-1578] LeRobotDataset v3.0 형식은 여러 에피소드의 표 행과 영상 프레임을 큰 파일로 이어 붙이고, 에피소드별 구간을 파일 경계가 아니라 메타데이터로 복원한다(코드 판 v0.6.0과 데이터 형식 판 v3.0은 다른 번호). [사실][^ref-1578]
- **배포 묶음(Deployment Bundle)** — 이 위키는 학습 정책을 로봇에 배포할 때 가중치 해시, 전·후처리기와 정규화 통계, 학습 데이터 커밋과 데이터 형식 판, 카메라·관절 스키마, 하드웨어 보정판, 런타임 판을 하나의 배포 묶음으로 기록하고 이전 묶음을 보존해야 되돌릴 수 있다고 본다(실물 재생 시험은 하지 않은 의견). [의견][^ref-1578]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1577]: MLflow 프로젝트 (Linux Foundation 오픈소스 프로젝트), Model Registry Workflows (docs/docs/classic-ml/model-registry/workflow.mdx, MLflow v3.1.0), 2025-06-10, https://github.com/mlflow/mlflow/blob/v3.1.0/docs/docs/classic-ml/model-registry/workflow.mdx, 접근일 2026-10-12
[^ref-1578]: Hugging Face LeRobot 기여자 (huggingface/lerobot), Backward compatibility (docs/source/backwardcomp.mdx, LeRobot v0.6.0), 2026-07-06, https://github.com/huggingface/lerobot/blob/v0.6.0/docs/source/backwardcomp.mdx, 접근일 2026-10-12
[^ref-351]: Ren, A. Z. 외, Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners, 2023-07, https://arxiv.org/abs/2307.01928, 접근일 2026-10-12

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-04 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-04 | 47. AI·학습·적응과 모델 운영 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-10-12-04/pages/topics/2026/2026-10-12-area47-s8.md

```markdown
---
title: "47. AI·학습·적응과 모델 운영 — 대표 연구와 자료"
type: topic
category: "L. AI·학습 기술"
primary_area_no: 47
related_areas: [5, 15, 21, 25, 31, 38, 43, 48, 54, 55, 57, 59]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-10-12
updated: 2026-10-12
sources: [ref-1583, ref-1585, ref-351, ref-625]
last_run: 2026-10-12
version: 1
split_from: docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md#8
---

[홈](../../index.md) › [주제](../index.md) › 47. AI·학습·적응과 모델 운영 — 대표 연구와 자료

# 47. AI·학습·적응과 모델 운영 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 절의 자료는 대부분 원문 미열람 상태에서 검색 결과로 확인했고, AmbiK와 LoTa-Bench는 검증 과정에서 공식 저장소 README로 확인했다. 수치는 저자 보고다.
- 이 페이지는 [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 절의 자료는 대부분 원문 미열람 상태에서 검색 결과로 확인했고, AmbiK와 LoTa-Bench는 검증 과정에서 공식 저장소 README로 확인했다. 수치는 저자 보고다.


### 2026-10-12 갱신

- Ren, A. Z. 외, Robots That Ask For Help(KnowNo, CoRL 2023, PMLR 229) — 주제 페이지 항목에 보장의 가정을 덧붙인다: i.i.d. 보정, 정확한 사람 도움, 다단계 계획의 시퀀스 수준 보정. [사실][^ref-351]
- Breck, E. 외, The ML Test Score(IEEE Big Data 2017) — 28개 항목 가운데 Infra4(자동 품질 검사로 승인·거부), Infra6(오프라인 시험의 한계와 카나리), Infra7(평상시 롤백 연습 권고)이 모델 교체 절차와 직접 이어진다. [사실][^ref-625]
- Gibbs, I.·Candès, E. J., Adaptive Conformal Inference Under Distribution Shift(NeurIPS 2021) — 분포 이동 아래 장기 평균 포함 빈도를 보장하는 온라인 재보정 방법으로, 정답 관측이 필요하고 로봇 실험은 없다. [사실][^ref-1583]
- Wang, Y. 외, Learning While Deploying(arXiv v4, 2026-09-16) — 제조사 중심 연구 프리프린트(학회 게재 미확인)로, 동일 기종 16대 플릿에서 에피소드 경계에 정책을 갱신했고 실행 안전을 명시적으로 모델링하지 않는다는 한계를 저자가 밝힌다. [사실][^ref-1585]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)
- 관련 영역: [5. 로봇 능력·작업 표현](../../categories/robot-ontology/robot-capability-and-task-representation.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [38. 모니터링·이상 탐지·원인 분석](../../categories/field-operations-and-monitoring/monitoring-anomaly-detection-and-root-cause-analysis.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [55. 현장 조사·설치·시운전](../../categories/verification-deployment-and-lifecycle/site-survey-installation-and-commissioning.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1583]: Gibbs, I., & Candès, E. J. (NeurIPS 2021), Adaptive Conformal Inference Under Distribution Shift, 2021-12-06, https://papers.nips.cc/paper/2021/file/0d441de75945e5acbc865406fc9a2559-Paper.pdf, 접근일 2026-10-12
[^ref-1585]: Wang, Y. 외 (저자 대부분 AGIBOT(Finch) 소속·일부 Shanghai Innovation Institute 겸직·1명 Columbia University), Learning While Deploying: Fleet-Scale Reinforcement Learning for Generalist Robot Policies, 2026-09-16, https://arxiv.org/abs/2605.00416v4, 접근일 2026-10-12
[^ref-351]: Ren, A. Z. 외, Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners, 2023-07, https://arxiv.org/abs/2307.01928, 접근일 2026-10-12
[^ref-625]: Breck, E. 외 (Google Research), The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction, 2017, https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/, 접근일 2026-10-12

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-12-04 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-12 | 2026-10-12-04 | 47. AI·학습·적응과 모델 운영 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-10-12-04/verification2.json

```json
{
  "run_id": "2026-10-12-04",
  "stage": "second",
  "verdict": "수정 후 재검증",
  "claim_checks": [],
  "category_fit": {
    "ok": true,
    "reassign_to": null
  },
  "scope_boundary": {
    "ok": true,
    "issues": []
  },
  "duplication": {
    "ok": true,
    "overlaps": [
      "새 주제 페이지 2026-10-12-area47-s3·s7 의 한국 인공지능기본법(f47·f48) 서술은 서로 같은 내용을 반복한다. 같은 각주 ref-620 을 쓰므로 모순은 아니다.",
      "새 주제 페이지 2026-10-12-area47-s4·s6·s7·s8 은 기존 분리 주제 페이지 2026-09-25-area27-s4·s6·s7·s8 에 덧붙이는 갱신 소절이다. 그런데 기존 페이지로 가는 링크가 사라졌다(required_fixes 1). 두 페이지의 옛 문장(옛 법 문단, 'AI Omnibus 논의')을 정리하는 일은 changelog_entry·additional_research_requests 에 후속 대상으로 남아 있다."
    ]
  },
  "terminology": {
    "ok": true,
    "conflicts": []
  },
  "quotation_check": {
    "ok": true
  },
  "corrections_applied": [],
  "corrections_rejected": [],
  "required_fixes": [
    "4·6·7·8절 패치(append): 갱신 소절 첫 문장의 '주제 페이지의 …'를 기존 분리 주제 페이지로 가는 명시 링크로 바꾼다. 대상은 4절 [기존 주제 페이지](../../topics/2026/2026-09-25-area27-s4.md), 6절 …-s6.md, 7절 …-s7.md, 8절 …-s8.md 다. 예: '[기존 주제 페이지 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area27-s6.md)의 ‘모델 운영 관리’와 ‘필요할 때 되묻기’ 소절에 아래 내용을 덧붙인다'. 이유: 자동 분리가 이미 분리된 절을 다시 옮기면서 기존 '자세한 내용은 주제 페이지 […](2026-09-25-area27-s*.md)에 있다' 줄이 빠졌다. 그 결과 세부영역 페이지와 새 주제 페이지 어디에서도 기존 4·6·7·8절 본문(개념 목록, 접근법·도식, 표준 표, 연구 목록)에 닿을 수 없고, '주제 페이지의 …'와 '3절의 겹 구조를 … 그린 도식은 주제 페이지에 있다'가 가리키는 대상도 없어진다.",
    "11절(분리 주제 페이지 2026-10-12-area47-s11): 질문 문장 없이 id 와 부분 근거만 적은 '**oq-213** (상태: 열림) 부분 근거: …' 항목을 지운다. 이유: 입력의 열린 질문 목록(영역 47 에 걸린 10건)에 oq-213 이 없고 질문 문장도 확인되지 않았다. 독자가 무엇에 대한 근거인지 알 수 없다. Viam 부분 근거(f12·f13)는 6절에 이미 있으며, oq-213 문장 확인 요청은 additional_research_requests 에 그대로 둔다.",
    "7절 패치(분리 주제 페이지 2026-10-12-area47-s7, '관련 법 문단 갱신' 둘째 문단 첫 문장): 'EU AI Act는 2026-07-27 통합판에서 기계류 규정이 부속서 I Section B로 옮겨졌고 제2조 2항이 … 한정한다(3절).'에 [사실][^ref-1587] 을 붙인다. 아니면 이 문장을 '이 내용은 [3. 왜 중요한가](../../topics/2026/2026-10-12-area47-s3.md)에 있다'는 안내 문장으로 바꾼다. 이유: 태그·각주 없는 사실 문장이다. 또 주제 페이지 안에서 '(3절)'은 그 페이지의 '3. 본문'으로 읽혀 가리키는 곳이 모호하다.",
    "standards_updates 의 'EU AI Act 2026-07-27 통합판' 항목 summary: '제43조 4항은 실질적 변경 시 재평가, 제72조 2항은 시판 후 감시를 정한다' 뒤에 '(조문 내용 소개이며, 제2조 2항에 따라 기계류 연계 로봇 AI 에 AI Act 조문으로 바로 적용되는 의무로 읽지 않는다 — 기계류 규정 쪽 통합 방식은 미확인)'을 덧붙인다. 이유: 1차 수정 지시 7항(f42~f44 는 조문 소개로만, f45 [추정] 주의 병기)이 표준 목록에도 적용된다. 이 문구가 없으면 표준 표만 읽은 독자가 로봇 AI 에 적용되는 의무로 오해할 수 있다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인 / 2차 수정 후 재검증. 확인 50건, 미확인 0건, 교차 확인 0건(모든 사실 finding 이 단일 출처이며, AWS 두 문서는 같은 기관이고 KnowNo·ACI 는 결과 종류가 달라 교차 확인으로 세지 않음). 강등: 없음. 대신 f24 저자 소속을 '저자 대부분 AGIBOT(Finch) 소속'으로 정정했고 f42 용어를 '실질적 변경'으로 맞췄다. 원문 미열람 출처: 없음(브리프 기준). 다만 검증 단계에서 ref-1587(EUR-Lex 통합판)과 ref-625(원고 PDF)는 다시 열지 못해 해설·조문 사이트·서지로 대조했고, ref-351·ref-1583·ref-1586 은 같은 문서의 arXiv 판·NIST AIRC 웹판으로 대조했다. 주의: Mender·AWS·Viam·LG CNS 내용은 벤더 주장이며, LG CNS 의 15%·18% 는 회사 기대치다. LWD 는 제조사 중심 연구 프리프린트이고 같은 기종 실험 조건이다. EU AI Act 의 기계류 연계 로봇 AI 적용 범위(f45)와 인공지능기본법 제34조 해당성(f49)은 법률 판단이 아닌 [추정]이다. AI-Hub 71825 의 분할비·합계 불일치는 제공자 확인 전까지 판정하지 않는다. 4·6·7·8절 갱신은 기존 분리 주제 페이지(2026-09-25-area27-s4·s6·s7·s8)를 고치지 못하고 새 주제 페이지의 갱신 소절로 덧붙였다. 옛 법 문단은 후속 갱신에서 정정해야 한다. 트랙 반영 제안 15건은 반영하지 않았다. 정정 요청: 없음. 열린 질문 해결 인정: 없음. / 2차 수정 후 재검증. 드리프트 없음, 1차 수정 지시 16건 이행 확인, 태그 상향 없음, [분류원문]·[옛 분류원문] 보존, 섹션 순서 준수. 남은 문제는 네 건이다. (1) 다시 분리하는 과정에서 기존 분리 주제 페이지 4건으로 가는 링크가 끊겼다. (2) 11절 oq-213 항목에 질문 문장이 없다. (3) 7절 문장 하나에 태그가 없다. (4) 표준 목록의 EU AI Act 항목에 적용 범위 주의가 빠졌다. 파이프라인 담당 확인 요청: 자동 분리 코드가 이미 분리된 절을 다시 옮길 때 '자세한 내용은 주제 페이지 …' 링크 줄을 떨어뜨린다. 영역 8절 요약('대부분 원문 미열람')은 기존 자료 기준 문장이며, 이번에 더한 자료는 원문을 열어 확인했다.",
  "retry_reason": null
}
```


## 수정 지시

- 판정(verdict): 수정 후 재검증
- 재작업 사유(retry_reason): —
- 수정 지시(required_fixes):
    - 4·6·7·8절 패치(append): 갱신 소절 첫 문장의 '주제 페이지의 …'를 기존 분리 주제 페이지로 가는 명시 링크로 바꾼다. 대상은 4절 [기존 주제 페이지](../../topics/2026/2026-09-25-area27-s4.md), 6절 …-s6.md, 7절 …-s7.md, 8절 …-s8.md 다. 예: '[기존 주제 페이지 — 대표 접근법과 기술](../../topics/2026/2026-09-25-area27-s6.md)의 ‘모델 운영 관리’와 ‘필요할 때 되묻기’ 소절에 아래 내용을 덧붙인다'. 이유: 자동 분리가 이미 분리된 절을 다시 옮기면서 기존 '자세한 내용은 주제 페이지 […](2026-09-25-area27-s*.md)에 있다' 줄이 빠졌다. 그 결과 세부영역 페이지와 새 주제 페이지 어디에서도 기존 4·6·7·8절 본문(개념 목록, 접근법·도식, 표준 표, 연구 목록)에 닿을 수 없고, '주제 페이지의 …'와 '3절의 겹 구조를 … 그린 도식은 주제 페이지에 있다'가 가리키는 대상도 없어진다.
    - 11절(분리 주제 페이지 2026-10-12-area47-s11): 질문 문장 없이 id 와 부분 근거만 적은 '**oq-213** (상태: 열림) 부분 근거: …' 항목을 지운다. 이유: 입력의 열린 질문 목록(영역 47 에 걸린 10건)에 oq-213 이 없고 질문 문장도 확인되지 않았다. 독자가 무엇에 대한 근거인지 알 수 없다. Viam 부분 근거(f12·f13)는 6절에 이미 있으며, oq-213 문장 확인 요청은 additional_research_requests 에 그대로 둔다.
    - 7절 패치(분리 주제 페이지 2026-10-12-area47-s7, '관련 법 문단 갱신' 둘째 문단 첫 문장): 'EU AI Act는 2026-07-27 통합판에서 기계류 규정이 부속서 I Section B로 옮겨졌고 제2조 2항이 … 한정한다(3절).'에 [사실][^ref-1587] 을 붙인다. 아니면 이 문장을 '이 내용은 [3. 왜 중요한가](../../topics/2026/2026-10-12-area47-s3.md)에 있다'는 안내 문장으로 바꾼다. 이유: 태그·각주 없는 사실 문장이다. 또 주제 페이지 안에서 '(3절)'은 그 페이지의 '3. 본문'으로 읽혀 가리키는 곳이 모호하다.
    - standards_updates 의 'EU AI Act 2026-07-27 통합판' 항목 summary: '제43조 4항은 실질적 변경 시 재평가, 제72조 2항은 시판 후 감시를 정한다' 뒤에 '(조문 내용 소개이며, 제2조 2항에 따라 기계류 연계 로봇 AI 에 AI Act 조문으로 바로 적용되는 의무로 읽지 않는다 — 기계류 규정 쪽 통합 방식은 미확인)'을 덧붙인다. 이유: 1차 수정 지시 7항(f42~f44 는 조문 소개로만, f45 [추정] 주의 병기)이 표준 목록에도 적용된다. 이 문구가 없으면 표준 표만 읽은 독자가 로봇 AI 에 적용되는 의무로 오해할 수 있다.
- 검증 노트: 판정: 조건부 승인 / 2차 수정 후 재검증. 확인 50건, 미확인 0건, 교차 확인 0건(모든 사실 finding 이 단일 출처이며, AWS 두 문서는 같은 기관이고 KnowNo·ACI 는 결과 종류가 달라 교차 확인으로 세지 않음). 강등: 없음. 대신 f24 저자 소속을 '저자 대부분 AGIBOT(Finch) 소속'으로 정정했고 f42 용어를 '실질적 변경'으로 맞췄다. 원문 미열람 출처: 없음(브리프 기준). 다만 검증 단계에서 ref-1587(EUR-Lex 통합판)과 ref-625(원고 PDF)는 다시 열지 못해 해설·조문 사이트·서지로 대조했고, ref-351·ref-1583·ref-1586 은 같은 문서의 arXiv 판·NIST AIRC 웹판으로 대조했다. 주의: Mender·AWS·Viam·LG CNS 내용은 벤더 주장이며, LG CNS 의 15%·18% 는 회사 기대치다. LWD 는 제조사 중심 연구 프리프린트이고 같은 기종 실험 조건이다. EU AI Act 의 기계류 연계 로봇 AI 적용 범위(f45)와 인공지능기본법 제34조 해당성(f49)은 법률 판단이 아닌 [추정]이다. AI-Hub 71825 의 분할비·합계 불일치는 제공자 확인 전까지 판정하지 않는다. 4·6·7·8절 갱신은 기존 분리 주제 페이지(2026-09-25-area27-s4·s6·s7·s8)를 고치지 못하고 새 주제 페이지의 갱신 소절로 덧붙였다. 옛 법 문단은 후속 갱신에서 정정해야 한다. 트랙 반영 제안 15건은 반영하지 않았다. 정정 요청: 없음. 열린 질문 해결 인정: 없음. / 2차 수정 후 재검증. 드리프트 없음, 1차 수정 지시 16건 이행 확인, 태그 상향 없음, [분류원문]·[옛 분류원문] 보존, 섹션 순서 준수. 남은 문제는 네 건이다. (1) 다시 분리하는 과정에서 기존 분리 주제 페이지 4건으로 가는 링크가 끊겼다. (2) 11절 oq-213 항목에 질문 문장이 없다. (3) 7절 문장 하나에 태그가 없다. (4) 표준 목록의 EU AI Act 항목에 적용 범위 주의가 빠졌다. 파이프라인 담당 확인 요청: 자동 분리 코드가 이미 분리된 절을 다시 옮길 때 '자세한 내용은 주제 페이지 …' 링크 줄을 떨어뜨린다. 영역 8절 요약('대부분 원문 미열람')은 기존 자료 기준 문장이며, 이번에 더한 자료는 원문을 열어 확인했다.

이전 초안(runs/<run_id>/pages.json, pages/)과 2차 판정(verification2.json)은 입력에 있다. storyteller.md 9절대로 이행하고 모든 페이지의 content 를 포함한 전체 pages.json 을 다시 반환한다.
