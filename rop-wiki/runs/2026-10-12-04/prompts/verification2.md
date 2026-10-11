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
- 언어: ko
- verification_stage: second
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
          "content": "(절 본문 생략 — runs/2026-10-12-04/pages/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md 의 해당 절을 본다)"
        },
        {
          "section": "4. 핵심 개념과 용어",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-12-04/pages/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md 의 해당 절을 본다)"
        },
        {
          "section": "5. 적용 사례 (현장 유형 명시)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-12-04/pages/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md 의 해당 절을 본다)"
        },
        {
          "section": "6. 대표 접근법과 기술",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-12-04/pages/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md 의 해당 절을 본다)"
        },
        {
          "section": "7. 관련 표준·프레임워크·오픈소스",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-12-04/pages/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md 의 해당 절을 본다)"
        },
        {
          "section": "8. 대표 연구와 자료",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-12-04/pages/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md 의 해당 절을 본다)"
        },
        {
          "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-12-04/pages/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md 의 해당 절을 본다)"
        },
        {
          "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-12-04/pages/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md 의 해당 절을 본다)"
        },
        {
          "section": "11. 열린 질문",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-12-04/pages/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md 의 해당 절을 본다)"
        },
        {
          "section": "13. 참고 자료 (각주)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-12-04/pages/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md 의 해당 절을 본다)"
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

### runs/2026-10-12-04/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md (10개 절)
- 분량 초과 자동 분리:
    - docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-10-12-area47-s6.md (3,373자)
    - docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-10-12-area47-s7.md (2,813자)
    - docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md "11. 열린 질문" → docs/topics/2026/2026-10-12-area47-s11.md (2,002자)
    - docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md "3. 왜 중요한가" → docs/topics/2026/2026-10-12-area47-s3.md (1,551자)
    - docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md "4. 핵심 개념과 용어" → docs/topics/2026/2026-10-12-area47-s4.md (1,202자)
    - docs/categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md "8. 대표 연구와 자료" → docs/topics/2026/2026-10-12-area47-s8.md (773자)
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
