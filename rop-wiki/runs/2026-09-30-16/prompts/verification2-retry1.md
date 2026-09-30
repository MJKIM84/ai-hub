(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-09-30-16
- date: 2026-09-30
- run_type: area_deep_dive (영역 심화)
- 대상: 53. 개인정보·영상 데이터 (N. 보안·개인정보)
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
- retry_count: 1
- max_retries: 2

## 입력

### runs/2026-09-30-16/target.json

```json
{
  "run_id": "2026-09-30-16",
  "date": "2026-09-30",
  "weekday": "Wed",
  "run_number": 125,
  "run_type": "area_deep_dive",
  "forced": true,
  "target": {
    "area_no": 53,
    "area_name": "53. 개인정보·영상 데이터",
    "category": "N. 보안·개인정보",
    "category_letter": "N"
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
  "selection_rationale": "CLI 지정 run_type=area_deep_dive, area=53"
}
```

### runs/2026-09-30-16/research.json

```json
{
  "run_id": "2026-09-30-16",
  "date": "2026-09-30",
  "run_type": "area_deep_dive",
  "target": {
    "area_no": 53,
    "area_name": "53. 개인정보·영상 데이터",
    "category": "N. 보안·개인정보"
  },
  "gaps": [
    "섹션 3. 왜 중요한가 비어 있음",
    "섹션 4. 핵심 개념과 용어 비어 있음 — 이동형 영상정보처리기기, 촬영 거부(opt-out), 가명처리, 얼굴 가림, 작업 한정 인지 출력 용어 없음",
    "섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 가정(로봇청소기)·병원·실외(배달로봇) 사례와 여섯 항목 정리 없음",
    "섹션 6. 대표 접근법과 기술 비어 있음 — 촬영 표시, 검출 후 블러, 명세 기반 실시간 가림, 촬영 시점 저해상도화, 출력 필드 축소의 근거 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — 개인정보 보호법 제25조의2, 이동형 영상정보처리기기 안내서, 가명정보 처리 가이드라인, EDPB 영상 장치 지침, EgoBlur 위치 없음",
    "섹션 8. 대표 연구와 자료 비어 있음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음",
    "섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음",
    "섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 oq-143, oq-171, oq-181, oq-185, oq-211, oq-214, oq-228 반영 필요",
    "프런트매터 related_areas·sources 비어 있음"
  ],
  "research_questions": [
    "로봇이 찍은 영상과 사람의 위치 정보를 어디까지 모으고 어떻게 지킬 것인가? [분류원문]",
    "한국 개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한)와 개인정보보호위원회 안내서는 로봇 카메라 촬영에 무엇을 요구하며, 병원·가정 내부 촬영에는 어떻게 적용되는가? (섹션 4·7 겨냥, oq-171, oq-181)",
    "로봇 영상을 인공지능 학습·사고 조사 등 다른 목적으로 쓸 때 가명처리·원본 활용 조건은 무엇인가? (섹션 6·7 겨냥, oq-228)",
    "로봇 영상에서 얼굴 등 식별 정보를 가리거나 처음부터 적게 모으는 기술(검출 후 블러, 명세 기반 가림, 저해상도 촬영, 출력 필드 축소)은 무엇이고 한계는 무엇인가? (섹션 6·8 겨냥)",
    "현장 유형별로 로봇 영상 유출·보안 취약점·보호 조치 사례는 무엇이 보고되었는가? (섹션 3·5 겨냥, 가정·병원·실외, 한국 사례 우선)",
    "영상·위치 데이터 보호에서 ROP가 직접 맡을 것과 제조사·운영 사업자·규제기관에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥, oq-211)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "한국 개인정보 보호법상 이동형 영상정보처리기기는 사람이 신체에 착용·휴대하거나 이동 가능한 물체에 부착해 사람 또는 사물의 영상을 촬영하는 장치로, 개인정보보호위원회는 스마트안경·드론·자율주행차 등을 예로 들고 로봇을 같은 범주의 기기로 안내한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1138",
        "ref-1135"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "개인정보 포털: '사람이 신체에 착용 또는 휴대하거나 이동 가능한 물체에 부착하여 영상 등을 촬영하는 장치'. 안내서 게시글은 '드론, 로봇 등 이동형 영상정보처리기기 사용자를 위한' 지침이라고 설명. 두 출처 모두 개인정보보호위원회라 독립 교차 확인 아님 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f2",
      "claim": "개인정보 보호법 제25조의2는 업무 목적으로 공개된 장소에서 이동형 영상정보처리기기로 사람을 촬영하는 것을 원칙적으로 제한하되, 동의 등 제15조제1항의 경우와 촬영 사실을 명확히 표시했는데도 정보주체가 거부 의사를 밝히지 않은 경우 등을 허용하고, 촬영 시 불빛·소리·안내판 등으로 촬영 사실을 표시하게 하며, 목욕실 등 사생활 침해 우려가 큰 장소에서의 촬영은 금지한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1138",
        "ref-588"
      ],
      "cross_checked": true,
      "confidence": "high",
      "evidence_excerpt": "개인정보 포털: 공개 장소 업무 목적 촬영은 원칙 제한, 동의를 받거나 촬영 사실을 알 수 있었으나 거부하지 않은 경우 허용, 불빛·소리·안내판 등으로 표시, 목욕실 등 촬영 금지. 김·장 뉴스레터가 표시·거부 의사 요건을 같게 설명",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f3",
      "claim": "개인정보보호위원회는 2024-10-14 '이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서(2024.9.)'를 게시해, 제25조의2 신설에 따라 공개된 장소에서 업무 목적으로 이동형 기기로 개인을 알아볼 수 있는 영상을 촬영할 수 있는 경우와 수집·이용 시 준수할 보호·활용 기준을 제시했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1135",
        "ref-1137"
      ],
      "cross_checked": true,
      "confidence": "high",
      "evidence_excerpt": "개인정보보호위원회 게시판: 게시일 2024-10-14, 첨부 '이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서(2024.9.).pdf'. 정보통신신문 2024-10-14 보도가 같은 안내서 공개를 전함",
      "as_of": "2024-10-14",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "같은 안내서는 촬영 거부를 사전 차단 권리가 아닌 선택 해제(opt-out) 방식으로 설명해 기본적으로 촬영하되 피촬영자가 명확히 거부하면 운영자가 받아들이게 하고, 촬영 사실 표시는 불빛·소리·안내판·안내서면·안내방송 등 기기 특성에 맞는 다중 채널 방식을 권장하며, 기획·설계 단계부터 목적 명확화와 최소 수집, 보관·파기 단계의 보유기간 설정과 영상정보 보호책임자 지정·운영방침 공개를 요구한다.",
      "tag": "사실",
      "source_ids": [
        "ref-588"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "김·장 뉴스레터 요약: 촬영 거부는 '일종의 선택 해제(Opt-out) 방식', 다중 채널 표시 권장, 단계별 준수사항(기획·설계, 촬영, 이용·제공, 보관·파기) 정리 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f5",
      "claim": "같은 안내서는 안전 주행 목적으로 촬영된 사고 영상을 사고 원인 파악·보험 처리에 이용·제공하는 것은 당초 수집 목적과 관련성이 있다고 보지만, 동의 없이 인공지능 학습에 쓰는 것은 정보주체의 예측 가능성이 없어 허용되지 않는다고 설명한다.",
      "tag": "사실",
      "source_ids": [
        "ref-588"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "김·장 뉴스레터: 사고 영상을 '사고 원인 파악, 보험 처리 목적으로 이용·제공하는 것은' 수집 목적과 연관, 동의 없는 AI 학습 활용은 예측 가능성이 없어 불허 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "완료·인계"
    },
    {
      "id": "f6",
      "claim": "같은 안내서는 고속으로 이동하며 촬영해 거부 의사를 파악하기 어려운 기기의 영상을 자율주행 인공지능 개발 등에 쓸 때 얼굴 모자이크 같은 익명·가명처리를 하도록 권고하고, 연구 목적상 원본이 불가피하면 규제샌드박스 실증특례를 검토하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-588",
        "ref-1137"
      ],
      "cross_checked": true,
      "confidence": "medium",
      "evidence_excerpt": "김·장: 익명·가명처리로 권리행사 가능성 최소화가 바람직. 정보통신신문: 원본이 꼭 필요한 연구가 아니면 AI 개발 전 얼굴 모자이크 처리. 두 출처 모두 안내서의 2차 요약",
      "as_of": "2024-10-14",
      "site_type": null,
      "flow_item": "작업 대상"
    },
    {
      "id": "f7",
      "claim": "실외 사례: 안내서 공개 보도는 카메라를 단 자율주행차와 배달로봇이 차량·로봇 외부에 촬영 사실과 구체적 내용을 표시해야 하고, 영상 처리를 위탁할 때는 보호책임자 지정과 정기 점검이 필요하다고 전한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1137"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "정보통신신문 2024-10-14: 이동형 기기는 차량·로봇 외부에 '촬영에 관한 구체적 내용'을 표시, 위탁 처리 시 보호책임자 지정·정기 점검 강조",
      "as_of": "2024-10-14",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f8",
      "claim": "개인정보보호위원회는 2023-11 자율주행차와 이동형 로봇 서비스 고도화 목적에 한해 영상정보 원본 활용 규제샌드박스 실증특례를 본격 운영하고 그해 안에 9개 기업 승인을 추진한다고 발표했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1139"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "정책브리핑 2023-11-15: '영상정보 원본 활용 규제샌드박스 실증특례를 본격 운영', 11월부터 시행, 올해 안에 9개 기업 승인 추진. 구체적 안전조치 항목은 기사에 없음",
      "as_of": "2023-11-15",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f9",
      "claim": "개인정보보호위원회는 2024-02 가명정보 처리 가이드라인을 개정해 이미지·영상·음성·텍스트 같은 비정형 데이터를 포함시켰고, 처리 목적·환경·민감도에 따른 식별 위험 판단, 적용 기술의 신뢰성 문서화와 처리 후 자체 검증을 요구하며, 영상·이미지 처리 방법으로 필터링·암호화·합성 얼굴·인페인팅·AI 기반 처리를 제시한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1140"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "세종 뉴스레터: 2024-02-05 개정 가이드라인이 비정형 데이터를 다루며, 영상·이미지 방법으로 filtering, encryption, synthetic faces, inpainting, AI-based processing 제시, 의료·자율주행 등 시나리오 포함 (발행일 미확인, 확인일 기준)",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "작업 대상"
    },
    {
      "id": "f10",
      "claim": "가정 사례: 한국소비자원과 한국인터넷진흥원이 로봇청소기 6종을 모바일앱 보안·정책 관리·기기 보안으로 나눠 점검한 결과, 나르왈·드리미·에코백스 3개 제품은 사용자 인증 절차가 미비해 집 내부 사진이 외부로 노출되거나 카메라가 강제로 활성화될 수 있었고, 삼성전자·LG전자 제품은 접근 통제와 업데이트 체계가 양호했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1141"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "경향신문 2025-09-02: 세 제품은 '사용자 인증 절차 미비'로 집 사진 유출·카메라 강제 활성화 위험, 드리미는 이름·연락처 노출 위험. 점검 대상 6종 모델명 기재. 기관 보도자료는 인증서 오류로 열지 못함",
      "as_of": "2025-09-02",
      "site_type": "가정",
      "flow_item": "예외·성과"
    },
    {
      "id": "f11",
      "claim": "가정 사례: 개인정보보호위원회가 2026-09-14 발표한 로봇청소기 5개 사업자 점검에서는 영상·음성·사진의 개인정보 침해 위험이 확인되지 않았고, 실시간 영상은 암호화해 사용자 앱으로 직접 보내고, 음성 명령은 서버에 저장하지 않으며, 장애물 인식 사진은 임시 저장 뒤 24시간 안 또는 다음 청소 뒤 삭제하는 방식이 확인되었으나, 동의와 계약 이행 처리의 구분, 서비스 개선용 수집의 사전 거부 선택권, 국외 이전 고지, 국내대리인 지정은 미흡했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1142"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "아시아경제 2026-09-14: 로보락·삼성전자·LG전자·에코백스·샤오미 점검, '영상·음성·사진 개인정보 침해 위험 확인 안 돼', 장애물 사진 24시간 내 또는 다음 청소 뒤 삭제, 신규 모델 추가 점검 계획",
      "as_of": "2026-09-14",
      "site_type": "가정",
      "flow_item": "예외·성과"
    },
    {
      "id": "f12",
      "claim": "가정 사례: MIT Technology Review 조사에 따르면 카메라를 단 개발용 로봇청소기(iRobot Roomba J7 계열)가 시험 가정에서 찍은 화장실의 여성, 미성년자 등 사적 장면의 스크린샷 15장이 학습 데이터 라벨링 위탁(Scale AI의 해외 계약 작업자)을 거쳐 SNS에 유출되었고, iRobot은 Scale AI에 200만 장 넘는 이미지를 공유했으며 시험 참가자 동의와 녹화 중 표시 스티커를 근거로 들었다.",
      "tag": "사실",
      "source_ids": [
        "ref-968"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "MIT Technology Review 2022-12-19(Eileen Guo): 개발 기기 → iRobot → Scale AI → 베네수엘라 작업자 → Facebook·Discord 경로, 15장은 200만 장 이상의 일부",
      "as_of": "2022-12-19",
      "site_type": "가정",
      "flow_item": "예외·성과"
    },
    {
      "id": "f13",
      "claim": "Meta Reality Labs의 EgoBlur(arXiv 2023)는 1인칭 영상에서 행인 얼굴과 차량 번호판을 검출해 가우시안 블러로 가리는 익명화 모델을 공개했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1144"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2308.13093: 'an AI anonymization model that removes bystander faces and vehicle license plates', 검출 영역에 가우시안 블러 적용, Casual Conversations V2 로 책임 있는 AI 분석 수행",
      "as_of": "2023-08-24",
      "site_type": null,
      "flow_item": "작업 대상"
    },
    {
      "id": "f14",
      "claim": "Choi 외(arXiv 2025)의 PCVS 는 '사람이 있을 때 얼굴을 보이지 않는다' 같은 논리 명세로 가릴 대상을 정하고 프레임마다 검출과 등각 예측으로 명세 만족 확률의 하한을 보장하며 실시간으로 가리는 방법으로, 여러 데이터셋에서 95% 넘는 명세 만족을 보였고 가린 영상으로도 로봇이 정상 동작함을 확인했다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1145"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2505.05519 초록: 논리 명세 기반 실시간 가림, 'theoretical lower bound' 제시, 명세 만족 95% 이상, 로봇 동작 유지 확인(데이터셋 이름은 초록에 없음)",
      "as_of": "2025-05-08",
      "site_type": null,
      "flow_item": "작업 대상"
    },
    {
      "id": "f15",
      "claim": "Huang·Pan·Reinhardt·Bennewitz(arXiv 2026)는 카메라를 단 이동 서비스 로봇에 관한 두 차례 사용자 연구에서 사용자가 시각적 추상화와 촬영 시점 저해상도화를 선호하고 원하는 해상도가 요구 프라이버시 수준과 로봇과의 거리에 따라 달라진다는 결과를 얻어, 사용자가 설정하는 거리–해상도 프라이버시 정책을 제안했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1146"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2604.06382 초록: 'users prefer privacy-preserving visual abstractions and capture-time low-resolution preservation mechanisms', 거리–해상도 정책 제안",
      "as_of": "2026-04-07",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f16",
      "claim": "Xu·Ayday(arXiv 2026-09)는 가정용 로봇이 원본 대신 계획기·클라우드·로그·학습 파이프라인으로 내보내는 작업 한정 인지 출력 3종이 과업 성공(1.000)과 경로 효율(0.898)은 같아도 표현 수준 연결 가능성이 0.532~0.970으로 크게 다르고, 목표 레이블을 공간 영역으로 바꾸면 목표 범주 추정 정확도가 0.077로 떨어지면서 과업 성공은 0.995를 유지했다고 보고하며, 필드 제거나 추상화가 보편적으로 더 안전하지 않아 과업별 평가가 필요하다고 결론지었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1147"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 2609.03055 초록: 'representation-level linkability ranges from 0.532 to 0.970', 'neither field removal nor stronger abstraction induces a universal privacy ordering'. 실험 환경(시뮬레이션 여부)은 초록에서 미확인",
      "as_of": "2026-09-02",
      "site_type": null,
      "flow_item": "작업 대상"
    },
    {
      "id": "f17",
      "claim": "병원 사례(모의): HRI 2026 컴패니언 논문은 의사·환자를 알아보도록 학습한 얼굴 인식으로 대상이 아닌 사람의 얼굴을 가리는 서비스 로봇을 진료실 모의 시나리오로 실험해, 대상이 아닌 사람은 안정적으로 가려졌으나 자세 변화·가림·조명 변화가 인식 신뢰도를 낮춰 보호에 한계가 있음을 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1148"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "검색 결과 요약 기준: 'non-target individuals are reliably obfuscated', 실제 조건의 pose variation, occlusion, lighting 이 신뢰도를 낮춤. ACM 페이지 403 으로 원문 미열람",
      "as_of": "2026-03",
      "site_type": "병원",
      "flow_item": "작업 대상",
      "source_unopened": true
    },
    {
      "id": "f18",
      "claim": "유럽데이터보호이사회(EDPB)는 GDPR 을 영상 장치의 개인정보 처리에 적용하는 지침 3/2019 최종판을 2020-01 채택해 처리의 적법 근거, 투명성, 정보주체 권리, 기술적 보호조치를 다룬다.",
      "tag": "사실",
      "source_ids": [
        "ref-1149"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "EDPB 페이지: 'Guidelines 3/2019 on processing of personal data through video devices', 최종판 채택. PDF 본문 추출 실패로 보존 기간·가정 예외 세부는 미확인",
      "as_of": "2020-01",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f19",
      "claim": "로봇 영상 유출 사례(f12)와 안내서의 위탁 처리 요구(f7)를 보면, 로봇 영상은 촬영 장치보다 학습·라벨링 위탁 같은 이차 이용 경로에서 유출 위험이 커지므로, 영상을 모으는 쪽은 이차 이용 목적과 위탁 사슬의 접근 범위를 수집 시점부터 정해 둘 필요가 있는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-968",
        "ref-1137",
        "ref-588"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f12(라벨링 위탁 경유 유출), f7(위탁 시 보호책임자·정기 점검), f5(동의 없는 AI 학습 불허)의 종합",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f20",
      "claim": "확인한 자료를 종합하면 핵심 질문(로봇이 찍은 영상과 사람의 위치 정보를 어디까지 모으고 어떻게 지킬 것인가)에 대해, 한국에서는 공개된 장소의 로봇 촬영에 촬영 사실 표시와 거부 의사 수용이 요구되고 이차 이용(특히 인공지능 학습)에는 가명처리나 별도 특례가 필요하며, 기술적으로는 검출 후 가림, 명세 기반 실시간 가림, 촬영 시점 저해상도화, 출력 필드 축소가 제안되었지만 모두 인식 오류나 재식별 위험의 한계가 보고되어, 수집 범위를 목적별로 정하고 이차 이용을 통제하는 운영 규칙이 기술과 함께 필요한 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1138",
        "ref-588",
        "ref-1140",
        "ref-1144",
        "ref-1145",
        "ref-1146",
        "ref-1147",
        "ref-1148"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f2·f4·f6·f9(법·안내서), f13~f17(기술과 한계)의 종합. 보행자 위치 데이터만을 다룬 자료는 이번에 찾지 못함",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "확인한 자료를 종합하면 53. 개인정보·영상 데이터에서 ROP가 직접 맡을 범위는 로봇 등록 정보에 카메라 유무·촬영 사실 표시 수단·영상 전송 경로를 기록하는 일, 관제 표시·사고 조사·학습 같은 목적별로 영상·위치 데이터의 흐름과 보유 기간을 나눠 관리하는 일, 촬영 금지 장소(화장실·탈의실 등)를 지도 구역으로 표시해 경로·카메라 모드 제약으로 반영하는 일, 로봇이 내보내는 인지 출력의 필드를 과업에 필요한 만큼으로 줄이는 일, 촬영 거부 의사를 받아 여러 로봇에 전달하는 창구로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1138",
        "ref-588",
        "ref-1147",
        "ref-1142"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f2(목욕실 등 촬영 금지, 표시 의무), f4(opt-out, 보유기간), f5(목적별 이용 구분), f16(출력 필드 설계가 재식별 위험을 좌우), f11(단기 삭제·직접 전송 사례)의 종합",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "연계 대상: 분류 원문 19장 기준으로 로봇 카메라 펌웨어·기기 쪽 가림 처리·모바일앱 인증은 제조사가, 로봇 외부의 촬영 표시 부착과 영상정보 보호책임자 지정·운영방침 공개 같은 영상기기 운영자 의무는 현장 운영 사업자가, 시설 CCTV 는 시설 관리자가, 원본 영상 활용 특례 승인은 개인정보보호위원회가 맡으므로, ROP는 그 결과와 상태를 받아 작업·경로·권한 제약과 데이터 흐름 규칙에 반영하는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1141",
        "ref-588",
        "ref-1139",
        "ref-1137"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f10(앱 인증·펌웨어 취약점은 제조사 제품 문제), f4·f7(운영자 의무), f8(특례 승인 주체)의 종합",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": "수행 자원"
    },
    {
      "id": "f23",
      "claim": "이 영역은 명령 권한과 고객·현장 격리의 51. 인증·권한·격리(f10), 통신 암호화와 감사 기록의 52. 통신 보호·위협 관리·감사(f10·f11), 보행자 위치의 19. 사람·보행자 모델(f15·f16), 촬영 금지 구역을 지도에 두는 16. 장소 의미·지도 관리(f2), 영상·기록 보존의 43. 데이터·관측성·배포와 37. 관제 화면·실행 기록(f4·f11), 사고 영상 이용의 50. 안전 표준·인증·사고 조사(f5), 학습 데이터 이용의 47. AI·학습·적응과 모델 운영과 45. 문서·도면·장면 이해(f6·f9·f12·f13), 재식별 위험 평가의 54. 시험·형식 검증·벤치마크(f14·f16), 위탁·운영자 책임의 58. 다사업자 책임·계약·데이터(f7·f12), 법령의 59. 법·규제·보험·라이선스(f2·f8·f18), 사용자 선호의 60. 노동·수용성·접근성(f15), 적용 현장인 63. 병원·의료(f17)·65. 가정·공동주택(f10~f12)·66. 실외(f7)와 이어진다.",
      "tag": "추정",
      "source_ids": [
        "ref-1141",
        "ref-1142",
        "ref-1146",
        "ref-1147",
        "ref-1138",
        "ref-588",
        "ref-1140",
        "ref-968",
        "ref-1144",
        "ref-1145",
        "ref-1137",
        "ref-1139",
        "ref-1149",
        "ref-1148"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "각 연결은 괄호 안 finding 에 근거한 추정",
      "as_of": "2026-09-30",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-1135",
      "org": "개인정보보호위원회",
      "title": "[현재 안내서] 이동형 영상정보처리기기를 위한 개인영상정보 보호ㆍ활용 안내서(2024.9.)",
      "published": "2024-10-14",
      "url": "https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS217&mCode=G010030000&nttId=10679",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "개인정보보호위원회 안내서 게시글. 제25조의2 신설에 따라 드론·로봇 등 이동형 기기로 공개된 장소에서 개인 식별 영상을 촬영할 수 있는 경우와 보호·활용 기준을 안내한다고 설명한다(PDF 본문은 열지 않음).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-588",
      "org": "김·장 법률사무소",
      "title": "‘이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서’ 공개 (뉴스레터)",
      "published": null,
      "url": "https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=30477",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "2024-10-14 공개된 안내서의 요지를 정리한 법률사무소 뉴스레터. 촬영 표시 다중 채널, 촬영 거부의 opt-out 성격, 단계별 준수사항, 사고 영상 이용과 AI 학습 구분, 익명·가명처리 권고를 설명한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1137",
      "org": "정보통신신문",
      "title": "\"자율주행차·로봇 카메라 촬영 시 외부에 표시해야\" (제목 일부만 확인)",
      "published": "2024-10-14",
      "url": "https://www.koit.co.kr/news/articleView.html?idxno=125844",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "안내서 공개 보도. 자율주행차·배달로봇 외부 촬영 표시, AI 개발 전 얼굴 모자이크, 위탁 처리 시 보호책임자·정기 점검을 전한다. 내용이 개인정보보호위원회 게시 안내서와 일치해 medium.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1138",
      "org": "개인정보보호위원회 (개인정보 포털)",
      "title": "개인정보 포털 — 이동형 영상정보처리기기 제도 및 신청방법 안내",
      "published": null,
      "url": "https://www.privacy.go.kr/front/contents/cntntsView.do?contsNo=286",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "이동형 영상정보처리기기의 정의, 공개 장소 업무 목적 촬영 제한과 예외, 불빛·소리·안내판 등 촬영 표시, 목욕실 등 촬영 금지, 드론의 인터넷 공지 방식을 안내한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1139",
      "org": "개인정보보호위원회 (대한민국 정책브리핑)",
      "title": "자율주행차·이동형 로봇 개발에 ‘영상데이터’ 원본 활용 허용",
      "published": "2023-11-15",
      "url": "https://www.korea.kr/news/policyNewsView.do?newsId=148922669",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "자율주행차·이동형 로봇 서비스 고도화 목적의 영상정보 원본 활용 규제샌드박스 실증특례를 11월부터 운영하고 연내 9개 기업 승인을 추진한다는 정책 보도. 보도자료 성격이라 medium.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1140",
      "org": "법무법인(유) 세종",
      "title": "개인정보보호위원회, 비정형데이터 가명처리 관련 가명정보 처리 가이드라인 개정 (뉴스레터)",
      "published": null,
      "url": "https://www.shinkim.com/kor/media/newsletter/2342",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "2024-02 개정 가명정보 처리 가이드라인의 비정형 데이터(영상·이미지·음성·텍스트) 가명처리 기준과 처리 방법, 시나리오를 요약한 법률사무소 뉴스레터.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1141",
      "org": "경향신문",
      "title": "로봇청소기가 우리집 사진 찍어 외부 유출?…6종 ... (제목 일부만 확인)",
      "published": "2025-09-02",
      "url": "https://www.khan.co.kr/article/202509021447001",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "한국소비자원·한국인터넷진흥원의 로봇청소기 6종 보안 점검 결과 보도. 3개 제품의 사용자 인증 미비로 집 내부 사진 노출·카메라 강제 활성화 위험을 전한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1142",
      "org": "아시아경제",
      "title": "\"로봇청소기 개인정보 관리 대체로 안전…미흡 사례 ... (제목 일부만 확인)",
      "published": "2026-09-14",
      "url": "https://view.asiae.co.kr/article/2026091410054053414",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "개인정보보호위원회의 로봇청소기 5개 사업자 점검 결과 보도. 영상·음성·사진 침해 위험 미확인, 영상 직접 전송·사진 단기 삭제, 동의 구분·국외 이전 고지 등 미흡 사항을 전한다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-968",
      "org": "MIT Technology Review",
      "title": "A Roomba recorded a woman on the toilet. How did screenshots end up on Facebook?",
      "published": "2022-12-19",
      "url": "https://www.technologyreview.com/2022/12/19/1065306/roomba-irobot-robot-vacuums-artificial-intelligence-training-data-privacy/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "개발용 Roomba J7 이 찍은 가정 내 사적 이미지가 라벨링 위탁 사슬을 거쳐 SNS 에 유출된 경위를 밝힌 탐사 보도. 사건의 1차 보도라 medium.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1144",
      "org": "Raina, N., Somasundaram, G., Zheng, K. 외 (Meta Reality Labs, arXiv)",
      "title": "EgoBlur: Responsible Innovation in Aria",
      "published": "2023-08-24",
      "url": "https://arxiv.org/abs/2308.13093",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "1인칭 영상의 행인 얼굴·차량 번호판을 검출해 가우시안 블러로 가리는 익명화 모델을 공개한 프리프린트. 초록만 확인.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1145",
      "org": "Choi, M. 외 (arXiv)",
      "title": "Real-Time Privacy Preservation for Robot Visual Perception",
      "published": "2025-05-08",
      "url": "https://arxiv.org/abs/2505.05519",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "논리 명세와 등각 예측으로 민감 객체를 실시간으로 가리는 PCVS 방법을 제안한 프리프린트. 초록만 확인.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1146",
      "org": "Huang, X., Pan, S., Reinhardt, D., & Bennewitz, M. (arXiv)",
      "title": "Designing Privacy-Preserving Visual Perception for Robot Navigation Based on User Privacy Preferences",
      "published": "2026-04-07",
      "url": "https://arxiv.org/abs/2604.06382",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "두 사용자 연구로 이동 서비스 로봇 카메라의 선호 가림 방식과 거리–해상도 관계를 밝히고 사용자 설정 정책을 제안한 프리프린트. 초록만 확인.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1147",
      "org": "Xu, Y., & Ayday, E. (arXiv)",
      "title": "Seeing Less Is Not Seeing Safely: Privacy Leakage from Task-Scoped Robot Perception Exports",
      "published": "2026-09-02",
      "url": "https://arxiv.org/abs/2609.03055",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "가정용 로봇의 작업 한정 인지 출력이 과업 성능이 같아도 재식별 위험이 크게 다름을 보인 프리프린트. 초록만 확인.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1148",
      "org": "ACM/IEEE HRI 2026 Companion (저자 미확인)",
      "title": "The Privacy-Preserving Capabilities of a Service Robot in a Healthcare Setting",
      "published": "2026-03",
      "url": "https://doi.org/10.1145/3776734.3794481",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 의사·환자 얼굴 인식과 비대상자 얼굴 가림을 진료실 모의 시나리오로 실험한 HRI 2026 컴패니언 논문으로, 검색 결과 요약으로만 확인했다(ACM 페이지 403).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-1149",
      "org": "European Data Protection Board (EDPB)",
      "title": "Guidelines 3/2019 on processing of personal data through video devices",
      "published": "2020-01",
      "url": "https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-32019-processing-personal-data-through-video_en",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "GDPR 을 영상 장치 처리에 적용하는 EDPB 지침 최종판의 소개 페이지. PDF 본문 추출에 실패해 소개 페이지 범위만 확인했다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/security-and-privacy/privacy-and-video-data.md",
      "sections": [
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11"
      ],
      "rationale": "섹션 3: f12·f10(가정 로봇 영상 유출·취약점), f19(이차 이용 경로 위험, 추정), f20(핵심 질문 답, 추정) / 섹션 4: 이동형 영상정보처리기기 f1, 촬영 표시·거부(opt-out) f2·f4, 가명처리 f9, 원본 활용 특례 f8, 작업 한정 인지 출력 f16 / 섹션 5: 가정 — f10(예외·성과: 앱 인증 취약점)·f11(예외·성과: 점검 결과, 단기 삭제)·f12(예외·성과: 위탁 경유 유출), 병원 — f17(작업 대상: 얼굴 가림, 모의 실험임 명시), 실외 — f7(제약: 배달로봇 외부 표시). 물류창고·제조 공장·상업 시설 사례는 찾지 못함을 명시 / 섹션 6: 촬영 표시·거부 수용 f2·f4, 검출 후 블러 f13, 명세 기반 실시간 가림 f14, 촬영 시점 저해상도화 f15, 출력 필드 설계 f16, 목적별 이용 구분 f5·f6 / 섹션 7: 개인정보 보호법 제25조의2 f2, 이동형 영상정보처리기기 안내서 f3~f6, 가명정보 처리 가이드라인 f9, 규제샌드박스 실증특례 f8, EDPB 지침 3/2019 f18, EgoBlur f13 / 섹션 8: f13~f17 / 섹션 9: f21(직접 범위), f22(연계 대상) / 섹션 10: f23 — 16, 19, 37, 43, 45, 47, 50, 51, 52, 54, 58, 59, 60, 63, 65, 66 / 섹션 11: 기존 oq-143·oq-171·oq-181·oq-185·oq-211·oq-214·oq-228(미해결 유지; oq-181 은 f11 로 부분 근거, oq-228 은 f5·f6 로 부분 근거)과 open_questions_new 4건. 다음 실행 후보: 65. 가정·공동주택 페이지 5절에 f10~f12, 63. 병원·의료 페이지에 f17 반영."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "가명처리",
      "term_en": "Pseudonymisation",
      "definition": "추가 정보 없이는 특정 개인을 알아볼 수 없도록 개인정보의 일부를 삭제·대체하는 처리로, 한국 가명정보 처리 가이드라인은 2024년 개정에서 영상·이미지·음성 같은 비정형 데이터로 대상을 넓혔다."
    },
    {
      "term_ko": "얼굴 가림",
      "term_en": "Face Obfuscation",
      "definition": "영상에서 얼굴을 검출한 뒤 블러·모자이크·합성 얼굴 등으로 가려 신원을 알아볼 수 없게 하는 처리로, 로봇 영상의 저장·전송·학습 전에 쓰인다."
    },
    {
      "term_ko": "영상정보 원본 활용 규제샌드박스 실증특례",
      "term_en": "Regulatory Sandbox Special Demonstration Exemption for Raw Video Use",
      "definition": "자율주행차·이동형 로봇 개발에 가명처리하지 않은 영상 원본을 쓰도록 개인정보보호위원회가 안전조치를 조건으로 기업별로 허용하는 한시적 특례다."
    }
  ],
  "open_questions_new": [
    "여러 제조사 로봇의 영상과 위치 정보를 모아 관제하는 플랫폼 사업자는 개인정보 보호법상 이동형 영상정보처리기기 운영자인가, 현장 운영 사업자의 수탁자인가, 그리고 촬영 표시·거부 의사 처리 의무는 누구에게 있는가? | 관련 영역: 53. 개인정보·영상 데이터, 58. 다사업자 책임·계약·데이터 | 근거: f22 | 종류: 일반",
    "로봇이 플랫폼·클라우드·로그로 내보내는 인지 출력(객체 목록·의미 지도·궤적)의 재식별 위험을 측정하는 공개 평가 기준이나 벤치마크가 있는가? | 관련 영역: 53. 개인정보·영상 데이터, 54. 시험·형식 검증·벤치마크 | 근거: f16 | 종류: 일반",
    "피촬영자가 한 로봇에 밝힌 촬영 거부 의사를 같은 현장의 다른 로봇과 플랫폼 기록에 공통으로 반영하는 방법이나 운영 사례가 있는가? | 관련 영역: 53. 개인정보·영상 데이터, 19. 사람·보행자 모델 | 근거: f4 | 종류: 일반",
    "EDPB 영상 장치 지침 3/2019 를 이동 로봇 카메라에 적용한 유럽 감독기관의 결정이나 해석 사례가 있으며, 보존 기간 권고는 무엇인가? | 관련 영역: 53. 개인정보·영상 데이터, 59. 법·규제·보험·라이선스 | 근거: f18 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 15,
    "cross_checked_count": 3,
    "unverified": [
      "개인정보 보호법 제25조의2 조문 원문: 국가법령정보센터 페이지 본문 추출 실패, 개인정보 포털과 법률사무소 요약으로 확인(시행일 2023-09-15 는 비공식 법령 DB 에만 있어 넣지 않음)",
      "안내서(2024.9.) PDF 본문 미열람: 세부 내용은 김·장 뉴스레터·정보통신신문 요약 기준",
      "가명정보 처리 가이드라인 개정판 원문 미열람: 개인정보 포털 게시글은 본문 없음, 세종 뉴스레터 요약 기준",
      "f10 한국소비자원·한국인터넷진흥원 보도자료 원문은 인증서 오류로 열지 못해 기사 기준",
      "f11 개인정보보호위원회 로봇청소기 점검 보도자료 원문 미확인(기사 기준)",
      "f13 EgoBlur 학습 데이터 규모·성능 수치는 검색 요약에만 있어 넣지 않음",
      "f15 선호 해상도 32×32 이하 수치는 검색 요약에만 있어 넣지 않음",
      "f17 HRI 2026 논문 원문 미열람(ACM 403), 저자 미확인",
      "f18 EDPB 지침 PDF 본문 추출 실패로 보존 기간·가정 활동 예외 세부 미확인",
      "ISO 31700-1:2023(소비재 개인정보 중심 설계) 은 ISO 페이지 403 으로 원문을 열지 못하고 신규 출처 상한 때문에 넣지 않음",
      "보행자 위치 데이터 최소 수집·궤적 익명화 전용 자료는 찾지 못함",
      "oq-171·oq-181: 병원·세대 내부가 제25조의2 의 '공개된 장소'에 해당하는지 개인정보보호위원회 해석 원문 미확인",
      "oq-214 안전성 확보조치 기준 개정판 조항은 이번에 조사하지 못함"
    ],
    "scope_violations": [
      "f7: 실외 배달로봇의 외부 표시 의무는 현장 운영 사업자의 법적 의무이며 원문 19장 '업종별 조건'에 가까워, ROP 직접 범위는 f21 에서 표시 수단 기록·거부 의사 전달로 한정함",
      "f10: 로봇청소기 앱 인증·펌웨어 취약점은 제조사 제품 보안(로봇 자체) 문제로 f22 에서 '연계 대상: '으로 구분함",
      "f13·f14·f17: 기기 쪽 얼굴 검출·가림은 원문 19장 '로봇 자체 지능·제어'(센서 인식)에 걸칠 수 있어 기술 근거로만 제안하고, 플랫폼 수준 적용 여부는 추정(f21)으로 둠"
    ],
    "budget_used": {
      "queries": 15,
      "sources": 15
    },
    "limits": "web_fetch_available: true · fetch_mode full. 검색 15회/30, 신규 출처 15건/15(ref-1135~ref-1149, 예약 구간 안)로 신규 출처 상한에 도달해 ISO 31700-1:2023, 개인정보 포털 가명정보 가이드라인 게시글, 로봇신문 로봇청소기 보안 기사, 비공식 법령 DB(casenote)의 조문 전문을 출처로 넣지 않았다. 재사용 출처 없음(참고문헌 목록 요약에 이 영역 인용 0건; 같은 URL 이 이미 있으면 퍼블리셔가 합친다). 원문 열람: 14건 WebFetch 로 열었고 ref-1148 만 403 으로 못 열어 source_unopened 로 표시했다. arXiv 4건(ref-1144~ref-1147)은 초록만 읽었다. 국가법령정보센터·한국소비자원·KISA·ISO·ACM 은 본문 추출 실패·인증서 오류·403 이었다. 교차 확인 3건(f2: 개인정보 포털·김·장, f3: 개인정보보호위원회 게시판·정보통신신문, f6: 김·장·정보통신신문). 기사 근거 finding(f10·f11)은 low. 벤더 기능 주장 없음(f11 의 처리 방식은 규제기관 점검 결과 보도). 분류 원문 핵심 질문에는 f20 으로 답했고 결론은 '공개된 장소 촬영은 표시·거부 수용이 요구되고 이차 이용에는 가명처리나 특례가 필요하며, 가림 기술은 인식 오류·재식별 한계가 있어 목적별 수집 범위와 이차 이용 통제 규칙이 함께 필요하다'는 추정이다. 현장 유형 사례는 가정(f10~f12)·병원(f17, 모의)·실외(f7)이며 물류창고·제조 공장·상업 시설·기타는 찾지 못했다. 국내 자료는 개인정보보호위원회 3건(ref-1135·ref-1138·ref-1139)·법률사무소 2건·기사 3건이다. 이 영역에 걸린 기존 열린 질문 7건은 원문 확인이 부족해 해결 제안하지 않았다(oq-181 은 f11 이 동의·계약 구분 점검을 보여 부분 근거, oq-228 은 f5·f6 이 목적 외 이용 판단 사례를 보여 부분 근거). 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈 관련 주장은 내지 않았다. L. AI·학습 기술 관련 finding(f13·f14·f16의 인식·학습 데이터)은 적용 대상인 이 영역과 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영에 함께 연결했다(f23). 용어집에 이미 있는 이동형 영상정보처리기기·역할 기반 접근 통제·감사 추적은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음."
  }
}
```

### runs/2026-09-30-16/verification.json

```json
{
  "run_id": "2026-09-30-16",
  "stage": "first",
  "verdict": "조건부 승인",
  "retry_reason": null,
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 개인정보 포털(ref-1138)을 열어 정의(착용·휴대하거나 이동 가능한 물체에 부착·거치)와 예시(스마트안경·스마트폰·드론·자율주행차, 배달로봇)를 확인했다. 안내서 게시글(ref-1135)도 '드론, 로봇 등'을 명시한다. 두 출처 모두 개인정보보호위원회라서 독립 교차 확인은 아니다. 정의 문구에 '거치'가 빠져 있으니 원문대로 '부착·거치'로 적는다."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": true,
      "tag_decision": "강등",
      "note": "부분 뒷받침. 공개된 장소에서 업무 목적 촬영을 원칙적으로 제한하는 것, 동의하거나 거부 의사를 밝히지 않은 경우의 예외, 불빛·소리·안내판 표시는 ref-1138(열람)과 ref-588(열람) 두 곳에서 확인했다. 반면 '목욕실 등 사생활 침해 우려가 큰 장소 촬영 금지' 구절은 인용한 두 출처 어디에도 없다(포털 페이지 미기재, 김·장 뉴스레터에도 없음). 이 구절은 비공식 법령 DB 검색 결과에만 나온다. 처리: 이 구절만 떼어 [추정]으로 강등하고 '법령 원문 미확인'을 표시하며, 나머지 문장은 [사실]로 유지한다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. 개인정보보호위원회 게시판(ref-1135)에서 게시일 2024-10-14와 안내서 제목(2024.9.)을 열어 확인했고, 정보통신신문(ref-1137, 2024-10-14)이 같은 공개를 보도했다. 발행 주체가 서로 다르다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 김·장 뉴스레터(ref-588)를 열어 opt-out('일종의 Opt-out 방식임'), 다중 채널 표시, 기획·설계 단계의 목적 명확화·최소 수집, 보관·파기 단계의 보호책임자 지정·운영방침 공개·보유기간 설정을 확인했다. 안내서 PDF 원문이 아니라 법률사무소의 2차 요약에 기댄 단일 출처라는 점을 본문에 밝힌다. 뉴스레터 발행일은 2024-10-14로 확인했다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인하되 문구를 정정해야 한다. 원문은 '가명·익명처리 없이 AI 학습 등에 활용하는 것은 예측 가능성이 있다고 보기 어려움'이며, 원본이 필요하면 규제샌드박스(실증특례)를 활용하라고 한다. 이 맥락은 자율주행차 같은 고속 이동 기기다. 따라서 '동의 없이 … 허용되지 않는다'를 '가명·익명처리 없이 AI 학습에 쓰는 것은 예측 가능성이 있다고 보기 어렵고, 원본이 필요하면 규제샌드박스를 활용해야 한다'로 고친다. 사고 원인 파악·보험 처리 이용 부분은 원문과 일치한다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. 김·장(ref-588)에서 '자율주행차와 같이 고속 이동하면서 영상을 촬영하는 경우', 익명·가명처리로 권리행사 가능성 최소화, 규제샌드박스 활용을 확인했다. 정보통신신문(ref-1137)에서 원칙적 가명처리(얼굴 모자이크)와 원본 필수 시 규제샌드박스 예외를 확인했다. 두 출처 모두 안내서의 2차 요약이라는 점을 밝힌다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 정보통신신문(ref-1137)을 열어 자율주행차·배달로봇의 외부 촬영 표시와 위탁 시 보호책임자 지정·정기 점검·교육을 확인했다. 기사 제목 전체('자율주행차·로봇 카메라 촬영 시 외부에 표시해야')도 확인했다. 외부 표시는 운영 사업자의 의무이므로 본문에서는 연계 대상으로 서술한다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 정책브리핑(ref-1139, 2023-11-15)에서 영상정보 원본 활용 규제샌드박스 실증특례를 이번 달부터 운영하고 연내 9개 기업 승인을 추진한다는 내용을 확인했다. '서비스 고도화 목적에 한해'의 '한해'는 원문에서 한정 표현으로 확인하지 못했으므로 빼거나 완화한다. 2023년 발표이므로 기준일을 밝힌다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 세종 뉴스레터(ref-1140)를 열어 2024-02-05 개정, 비정형 데이터 포함, 목적·환경·민감도에 따른 위험 판단, 기술 신뢰성 문서화, 처리 후 자체 검수를 확인했다. 영상정보 처리 방법으로 '이미지 필터링, 이미지 암호화, 얼굴 합성, 인페인팅, AI 이용 영상정보 가명처리'가 나열돼 있다. 가이드라인 원문이 아니라 법률사무소 요약이다. 뉴스레터 발행일은 2024-02-08이다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. 경향신문(ref-1141, 2025-09-02)에서 한국인터넷진흥원·한국소비자원의 6종 점검, 나르왈·드리미·에코백스의 사용자 인증 절차 미비로 인한 집 사진 노출·카메라 강제 활성화 위험, 삼성·LG의 접근 통제·업데이트 양호를 확인했다. 기관 보도자료는 열지 못해 기사 단일 출처이므로 신뢰도 low를 유지한다. 제품 보안 취약점은 제조사 쪽 연계 대상이다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": true,
      "tag_decision": "유지",
      "note": "확인. 아시아경제(ref-1142, 2026-09-14)를 열어 5개 사업자, 침해 위험 미확인, 실시간 영상 암호화·앱 직접 전송, 음성 미저장, 동의·계약 이행 구분, 사전 선택권, 국외 이전 고지, 국내대리인 미흡을 확인했다. 검증 검색에서 여러 매체(이투데이·보안뉴스·SBS Biz 등) 요약이 같은 내용을 전하는 것을 확인했다(해당 기사 원문은 미열람). 장애물 사진 삭제 조건은 검색 요약상 '다음 청소 때, 이용자가 조회한 뒤, 또는 24시간 후'이고 브랜드별로 다르므로 '이용자 조회 뒤'를 더하고 '브랜드별로 다름'을 밝힌다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. MIT Technology Review(ref-968, 2022-12-19, Eileen Guo)를 열어 개발용 Roomba J7, 15장, 화장실의 여성·아동, Scale AI → 베네수엘라 작업자 → Facebook·Discord, 200만 장 이상 공유, 동의서와 '녹화 중' 라벨을 근거로 든 점을 확인했다. 단일 탐사 보도다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2308.13093 초록(v1 2023-08-24, v2 2023-09-06)에서 얼굴·번호판 검출 뒤 가우시안 블러, Casual Conversations V2 평가, Project Aria 1인칭 영상을 확인했다. 기기·데이터 수집 쪽 처리이므로 본문에서는 기술 근거로만 쓴다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2505.05519 초록(2025-05-08, Choi 외)에서 PCVS, 논리 명세, 등각 예측 기반 이론적 하한, 여러 데이터셋에서 95% 이상 명세 만족, 가린 영상으로도 로봇이 정상 동작함을 확인했다. 프리프린트 단일 출처다. 용어집의 '등각 예측(conformal-prediction)'에 연결한다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인. arXiv 2604.06382 초록(v1 2026-04-07, 개정 2026-06-30)에서 시각적 추상화와 촬영 시점 저해상도화 선호, 해상도가 프라이버시 수준과 로봇 근접도에 따라 달라진다는 점, 사용자 설정 거리–해상도 정책을 확인했다. 프리프린트다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인하되 두 가지를 정정한다. (1) 초록은 결과가 시뮬레이션 120개 장면(AI2-THOR·ProcTHOR)에서 나왔다고 밝히므로 본문에 시뮬레이션 결과임을 명시한다. (2) 0.077은 '추정 정확도'가 아니라 목표 범주 macro-F1(1.000 → 0.077)이다. 나머지 수치(1.000, 0.898, 0.532~0.970, 0.995)와 결론 문구는 초록과 일치한다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "원문 미열람(ACM 403). 검색 결과로 실재와 요약 내용(비대상자 얼굴 가림은 안정적, 정면 시 환자 인식, 자세·가림·조명 변화로 신뢰도 저하, 의사 진료실 모의 시나리오)을 확인했다. 서지를 정정한다: 정확한 제목은 'The Privacy-Preserving Capabilities of a Service Robot in a Scenario-Based Healthcare Setting', 저자는 Sarfraz, B. M., Saplacan Lindblom, D., Baselizadeh, A., Torresen, J., 발행일은 2026-03-16(HRI Companion '26)이다. 모의 실험임을 명시하고 신뢰도는 medium 이하다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": false,
      "cross_checked": false,
      "tag_decision": "강등",
      "note": "부분 뒷받침. EDPB 페이지를 열어 지침 3/2019 제목과 최종판(2.0) 채택(2020-01)을 확인했다. 그러나 '처리의 적법 근거, 투명성, 정보주체 권리, 기술적 보호조치를 다룬다'는 목록은 연 페이지에 없다(PDF 본문 추출 실패, 페이지 주제 태그는 Technology·Biometrics·Law enforcement). 처리: 목록 구절을 [추정]으로 강등해 '다루는 범위 세부는 원문 미확인'으로 표시하거나 삭제하고, 채택 사실만 [사실]로 유지한다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. f12·f7·f5의 종합이며 근거 출처는 모두 열람 확인했다. f5 문구 정정(가명·익명처리 없는 AI 학습)에 맞춰 근거 서술을 맞춘다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 핵심 질문의 답이다. 근거 finding의 정정(f5 문구, f16 시뮬레이션)을 반영한다. 핵심 질문의 '사람의 위치 정보' 부분은 전용 자료를 찾지 못했다는 한계를 본문에 명시한다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 다만 '촬영 금지 장소(화장실·탈의실 등)' 예시는 f2에서 강등된 구절(인용 출처 미확인)에 기대므로, '사생활 침해 우려 장소'로 일반화하고 법령 원문 미확인을 표시하거나 예시를 뺀다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 원문 19장의 책임 경계(로봇 자체 지능·제어, 업종별 조건)에 맞게 연계 대상을 구분했다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지. 연결 영역의 번호와 이름이 부록 A 원문 명칭과 일치한다(16·19·37·43·45·47·50·51·52·54·58·59·60·63·65·66). L. AI·학습 기술 교차 규칙에 따라 45·47에 연결한 것도 적절하다."
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
      "51. 인증·권한·격리 페이지의 옛 정의('영상·작업자 데이터 보호')가 이 영역의 출발점이다. 충돌은 없으며 10절에서 연결만 한다.",
      "용어 '이동형 영상정보처리기기'(mobile-video-information-processing-device)는 용어집에 이미 있으므로 새로 등록하지 않고 링크한다. '등각 예측'(conformal-prediction)도 기존 용어로 링크한다."
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
    "f2: '목욕실 등 사생활 침해 우려가 큰 장소에서의 촬영 금지' 구절을 [사실] 문장에서 떼어 [추정]으로 강등하고 '법령 원문 미확인'을 병기한다. 공개 장소 촬영 제한·예외·표시 방법 문장은 [사실][^ref-1138][^ref-588]으로 유지한다. 이유: 인용한 ref-1138·ref-588 어느 쪽에도 해당 구절이 없다.",
    "f21: 9절의 '촬영 금지 장소(화장실·탈의실 등)' 예시를 '사생활 침해 우려 장소'로 바꾸고 해당 법령 조항은 원문 미확인이라고 적는다. 이유: 근거인 f2 구절이 강등됐다.",
    "f5: '동의 없이 인공지능 학습에 쓰는 것은 … 허용되지 않는다'를 '가명·익명처리 없이 인공지능 학습에 쓰는 것은 예측 가능성이 있다고 보기 어렵고, 원본이 필요하면 규제샌드박스(실증특례)를 활용해야 한다'로 고치고, 자율주행차 등 고속 이동 기기 맥락임을 밝힌다. 이유: ref-588 원문 표현이 그렇다.",
    "f16: 결과가 시뮬레이션(AI2-THOR·ProcTHOR, 120개 장면)에서 나왔음을 본문에 명시하고, '목표 범주 추정 정확도가 0.077'을 '목표 범주 macro-F1 이 1.000에서 0.077로'로 고친다. 이유: ref-1147 초록의 지표와 실험 환경.",
    "f18: '처리의 적법 근거, 투명성, 정보주체 권리, 기술적 보호조치를 다룬다' 구절을 삭제하거나 [추정]·'원문 미확인'으로 표시하고, 지침 최종판 채택(2020-01)만 [사실]로 둔다. 이유: 연 EDPB 페이지가 이 목록을 뒷받침하지 않는다.",
    "f11: 장애물 사진 삭제 조건을 '브랜드별로 다음 청소 때, 이용자가 조회한 뒤, 또는 24시간 후 삭제'로 고친다. 이유: 검증 검색 결과의 복수 매체 요약.",
    "f8: '서비스 고도화 목적에 한해'의 '한해'를 빼거나 '목적으로'로 완화한다. 이유: ref-1139에서 한정 표현을 확인하지 못했다.",
    "f1: 정의를 원문대로 '부착·거치하여'로 적는다. 이유: ref-1138 원문 문구.",
    "ref-588: 발행일을 2024-10-14로 채운다(각주의 '미확인'을 바꾸고 reference_updates 의 published 도 같이 고친다). 이유: 김·장 뉴스레터 페이지 확인.",
    "ref-1140: 발행일을 2024-02-08로 채운다. 이유: 세종 뉴스레터 페이지 확인.",
    "ref-1148: 제목을 'The Privacy-Preserving Capabilities of a Service Robot in a Scenario-Based Healthcare Setting'로, 기관·저자를 'Sarfraz, B. M., Saplacan Lindblom, D., Baselizadeh, A., & Torresen, J. (HRI Companion '26)'로, 발행일을 2026-03-16으로 고치고, 각주 접근일 뒤 ' (원문 미열람)'과 reference_updates 의 source_unopened: true 를 유지한다. 이유: 검증 검색 결과의 ACM 서지.",
    "ref-1137: 제목의 '(제목 일부만 확인)'을 지우고 '\"자율주행차·로봇 카메라 촬영 시 외부에 표시해야\"'로 적는다. 이유: 기사 페이지에서 전체 제목을 확인했다.",
    "6절·9절: 기기 쪽 얼굴 검출·가림(f13·f14·f17)과 모바일앱 인증(f10)은 분류 원문 19장 '로봇 자체 지능·제어' 쪽의 연계 대상으로 서술하고, ROP 직접 범위는 f21 추정 범위(등록 정보 기록, 목적별 데이터 흐름·보유 기간, 출력 필드 축소, 거부 의사 전달)로 한정한다. 이유: 범위 경계 규칙 4.",
    "용어집 후보 '영상정보 원본 활용 규제샌드박스 실증특례'의 정의에서 '안전조치를 조건으로'와 '한시적'을 빼거나 미확인으로 둔다. 이유: f8 출처에 안전조치 항목과 기간이 없다.",
    "5절: 현장 유형 사례는 가정(f10~f12), 병원(f17, 모의 실험임 명시), 실외(f7)만 쓰고 물류창고·제조 공장·상업 시설·기타 사례는 찾지 못했다고 적는다. site_matrix_updates 는 이 세 칸(가정|N, 병원|N, 실외|N)만 낸다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인. 확인 21건, 미확인 2건(f2·f18 부분 뒷받침), 교차 확인 4건(f2·f3·f6·f11). 강등: f2 의 '목욕실 등 촬영 금지' 구절 사실 → 추정(인용 출처에 없음), f18 의 지침 다루는 범위 구절 사실 → 추정(원문 미확인). 원문 미열람 출처: ref-1148(ACM 403, 검색 결과로 서지 확인). 주의: 안내서(2024.9.)와 가명정보 처리 가이드라인의 세부 내용은 원문 PDF가 아니라 법률사무소 뉴스레터와 기사의 2차 요약에 근거한다. 기술 연구(f13~f16)는 프리프린트 초록 기준이고, f16 은 시뮬레이션 결과, f17 은 모의 진료실 실험이다. 로봇청소기 점검 사례(f10·f11)는 기사 근거다. 사람의 위치 정보 최소 수집·궤적 익명화 전용 자료는 찾지 못했다. 물류창고·제조 공장·상업 시설·기타 현장 사례는 없다. 이 영역의 기존 열린 질문 7건(oq-143·oq-171·oq-181·oq-185·oq-211·oq-214·oq-228)은 해결 제안 없이 열림으로 유지한다. 정정 요청 없음. 검증 검색 3회(리서치 15회와 합쳐 18/30)."
}
```

### runs/2026-09-30-16/pages.json

```json
{
  "run_id": "2026-09-30-16",
  "outline": [
    {
      "path": "docs/categories/security-and-privacy/privacy-and-video-data.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 900,
      "summary": "로봇 영상은 촬영 장치보다 학습·라벨링 위탁 같은 이차 이용 경로에서 유출 위험이 커지는 것으로 보여, 이차 이용 목적과 위탁 사슬의 접근 범위를 수집 시점부터 정해 둘 필요가 있다. [추정][^ref-968][^ref-1137][^ref-588]",
      "planned_findings": [
        "f19",
        "f12",
        "f10",
        "f20"
      ]
    },
    {
      "path": "docs/categories/security-and-privacy/privacy-and-video-data.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 1000,
      "summary": "이동형 영상정보처리기기, 촬영 사실 표시, 촬영 거부(opt-out), 가명처리, 원본 활용 실증특례, 얼굴 가림, 작업 한정 인지 출력, 등각 예측을 정리한다. [사실][^ref-1138][^ref-588]",
      "planned_findings": [
        "f1",
        "f2",
        "f4",
        "f9",
        "f8",
        "f13",
        "f16",
        "f14"
      ]
    },
    {
      "path": "docs/categories/security-and-privacy/privacy-and-video-data.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 2400,
      "summary": "가정(로봇청소기 영상 유출·점검), 병원(모의 진료실 얼굴 가림), 실외(배달로봇 외부 표시) 사례를 여섯 항목으로 정리하고, 물류창고·제조 공장·상업 시설·기타 사례는 찾지 못했음을 밝힌다. [사실][^ref-1142][^ref-1148][^ref-1137]",
      "planned_findings": [
        "f10",
        "f11",
        "f12",
        "f17",
        "f7",
        "f4",
        "f5"
      ]
    },
    {
      "path": "docs/categories/security-and-privacy/privacy-and-video-data.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 2200,
      "summary": "촬영 표시·거부 수용, 목적별 이용 구분·가명처리, 검출 후 가림, 명세 기반 실시간 가림, 촬영 시점 저해상도화, 인지 출력 필드 설계가 제안되었고 각각 인식 오류나 재식별 위험의 한계가 보고되었다. [추정][^ref-588][^ref-1144][^ref-1147]",
      "planned_findings": [
        "f2",
        "f4",
        "f5",
        "f6",
        "f9",
        "f13",
        "f14",
        "f15",
        "f16",
        "f17",
        "f22"
      ]
    },
    {
      "path": "docs/categories/security-and-privacy/privacy-and-video-data.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 800,
      "summary": "개인정보 보호법 제25조의2, 이동형 영상정보처리기기 안내서(2024.9.), 가명정보 처리 가이드라인(2024-02 개정), 원본 활용 실증특례, 유럽데이터보호이사회(EDPB) 지침 3/2019, EgoBlur 를 표로 정리한다. [사실][^ref-1135][^ref-1140][^ref-1149]",
      "planned_findings": [
        "f2",
        "f3",
        "f8",
        "f9",
        "f13",
        "f18"
      ]
    },
    {
      "path": "docs/categories/security-and-privacy/privacy-and-video-data.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 1000,
      "summary": "EgoBlur, PCVS, 거리–해상도 선호 연구, 작업 한정 인지 출력 유출 연구, 병원 모의 실험 논문, Roomba 영상 유출 탐사 보도를 요약한다. [사실][^ref-1144][^ref-1147]",
      "planned_findings": [
        "f12",
        "f13",
        "f14",
        "f15",
        "f16",
        "f17",
        "f21"
      ]
    },
    {
      "path": "docs/categories/security-and-privacy/privacy-and-video-data.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 900,
      "summary": "ROP는 등록 정보 기록, 목적별 데이터 흐름·보유 기간, 출력 필드 축소, 거부 의사 전달을 맡고, 기기 쪽 가림·앱 인증(제조사), 외부 표시·보호책임자(운영 사업자), 특례 승인(개인정보보호위원회)은 연계 대상으로 보인다. [추정][^ref-588][^ref-1141]",
      "planned_findings": [
        "f21",
        "f22"
      ]
    },
    {
      "path": "docs/categories/security-and-privacy/privacy-and-video-data.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 1200,
      "summary": "16·19·37·43·45·47·50·51·52·54·58·59·60·63·65·66 영역과 번호·이름으로 연결한다. [추정][^ref-1141][^ref-1147]",
      "planned_findings": [
        "f23"
      ]
    },
    {
      "path": "docs/categories/security-and-privacy/privacy-and-video-data.md",
      "section": "11. 열린 질문",
      "budget_chars": 1400,
      "summary": "기존 열린 질문 7건을 등록 문장 그대로 열림으로 유지하고(부분 근거 메모는 [추정]과 각주), 새 질문 4건(플랫폼 사업자 지위, 인지 출력 재식별 평가 기준, 거부 의사 공유, 유럽데이터보호이사회 지침 적용 사례)을 올린다.",
      "planned_findings": [
        "f4",
        "f5",
        "f6",
        "f11",
        "f16",
        "f18",
        "f22"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/security-and-privacy/privacy-and-video-data.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "seed → draft: 3~11절 첫 작성(제25조의2·이동형 안내서, 목적별 이용·가명처리, 가림·저해상도·출력 필드 기술, 가정·병원·실외 사례, 책임 경계, 연결 16개 영역, 열린 질문 11건), 13절 각주, 1차 수정 15건·2차 수정 4건 반영"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area53-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 53. 개인정보·영상 데이터 의 \"6. 대표 접근법과 기술\" 절(1,883자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area53-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 53. 개인정보·영상 데이터 의 \"11. 열린 질문\" 절을 옮겼다. 2차 수정: 기존 질문 7건을 등록 문장 그대로 옮기고 부분 근거 메모 2건에 [추정]·각주, EDPB 풀어쓰기"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area53-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 53. 개인정보·영상 데이터 의 \"8. 대표 연구와 자료\" 절을 옮겼다. 2차 수정: Xu·Ayday 항목의 플랫폼 필드 설계 연결 문장을 [추정]으로 분리"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area53-s4.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 53. 개인정보·영상 데이터 의 \"4. 핵심 개념과 용어\" 절(1,008자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area53-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 53. 개인정보·영상 데이터 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절을 옮겼다. 2차 수정: EDPB 풀어쓰기"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area53-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 53. 개인정보·영상 데이터 의 \"7. 관련 표준·프레임워크·오픈소스\" 절을 옮겼다. 2차 수정: EDPB·GDPR 풀어쓰기"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area53-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 53. 개인정보·영상 데이터 의 \"3. 왜 중요한가\" 절을 옮겼다. 2차 수정: SNS 풀어쓰기"
    }
  ],
  "changelog_entry": "2026-09-30 | 53. 개인정보·영상 데이터 | seed → draft: 3~11절 첫 작성(제25조의2·이동형 안내서, 목적별 이용·가명처리, 가림·저해상도·출력 필드 기술, 가정·병원·실외 사례, 책임 경계), 1차 수정 15건·2차 수정 4건 반영 | run 2026-09-30-16",
  "index_updates": {
    "home_recent": "2026-09-30 — 53. 개인정보·영상 데이터: seed → draft, 3~11절 첫 작성(이동형 영상정보처리기기 촬영 표시·거부, 가명처리·원본 활용 특례, 얼굴 가림·저해상도·인지 출력 필드 기술, 가정·병원·실외 사례)",
    "category_recent": "2026-09-30 — 53. 개인정보·영상 데이터: seed → draft, 3~11절 첫 작성과 각주(개인정보 보호법 제25조의2, 이동형 안내서, 가림 기술 연구, 로봇청소기 점검 사례)",
    "area_recent": "2026-09-30 — 53. 개인정보·영상 데이터: 3~11절 첫 작성, 1차 수정 15건(목욕실 촬영 금지 구절·EDPB 범위 강등, f5·f16 문구 정정)과 2차 수정 4건(8절 해석 문장 [추정], 11절 등록 문장 일치·메모 태그, 약어 풀어쓰기) 반영"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "pseudonymisation",
      "term_ko": "가명처리",
      "term_en": "Pseudonymisation",
      "definition": "추가 정보 없이는 특정 개인을 알아볼 수 없도록 개인정보의 일부를 삭제·대체하는 처리로, 한국 가명정보 처리 가이드라인은 2024년 개정에서 영상·이미지·음성 같은 비정형 데이터로 대상을 넓혔다.",
      "description": "개정 가이드라인은 영상·이미지 처리 방법으로 필터링·암호화·합성 얼굴·인페인팅·AI 기반 처리를 제시한다(법률사무소 요약 기준).",
      "related_areas": [
        53,
        45,
        47
      ],
      "sources": [
        "ref-1140"
      ]
    },
    {
      "action": "new",
      "slug": "face-obfuscation",
      "term_ko": "얼굴 가림",
      "term_en": "Face Obfuscation",
      "definition": "영상에서 얼굴을 검출한 뒤 블러·모자이크·합성 얼굴 등으로 가려 신원을 알아볼 수 없게 하는 처리로, 로봇 영상의 저장·전송·학습 전에 쓰인다.",
      "description": "예로 EgoBlur는 1인칭 영상의 행인 얼굴과 차량 번호판을 가우시안 블러로 가리며, 병원 모의 실험에서는 자세·가림·조명 변화가 인식 신뢰도를 낮추는 한계가 보고되었다.",
      "related_areas": [
        53,
        45,
        63
      ],
      "sources": [
        "ref-1144",
        "ref-1140",
        "ref-1137",
        "ref-1148"
      ]
    },
    {
      "action": "new",
      "slug": "raw-video-regulatory-sandbox-exemption",
      "term_ko": "영상정보 원본 활용 규제샌드박스 실증특례",
      "term_en": "Regulatory Sandbox Special Demonstration Exemption for Raw Video Use",
      "definition": "자율주행차·이동형 로봇 서비스 고도화 목적으로 가명처리하지 않은 영상 원본을 개발에 쓰도록 개인정보보호위원회가 기업별로 승인하는 규제샌드박스 특례로, 2023-11 운영이 발표되었다.",
      "description": "안전조치 항목과 특례 기간은 확인한 출처에 없어 미확인이다. 이동형 기기 안내서는 연구 목적상 원본이 불가피할 때 이 특례를 검토하게 한다.",
      "related_areas": [
        53,
        59,
        47
      ],
      "sources": [
        "ref-1139",
        "ref-588"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-1135",
      "org": "개인정보보호위원회",
      "title": "[현재 안내서] 이동형 영상정보처리기기를 위한 개인영상정보 보호ㆍ활용 안내서(2024.9.)",
      "published": "2024-10-14",
      "url": "https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS217&mCode=G010030000&nttId=10679",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "개인정보보호위원회 안내서 게시글. 제25조의2 신설에 따라 드론·로봇 등 이동형 기기로 공개된 장소에서 개인 식별 영상을 촬영할 수 있는 경우와 보호·활용 기준을 안내한다고 설명한다(PDF 본문은 열지 않음).",
      "cited_by": [
        "docs/categories/security-and-privacy/privacy-and-video-data.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-588",
      "org": "김·장 법률사무소",
      "title": "‘이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서’ 공개 (뉴스레터)",
      "published": "2024-10-14",
      "url": "https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=30477",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "2024-10-14 공개된 안내서의 요지를 정리한 법률사무소 뉴스레터. 촬영 표시 다중 채널, 촬영 거부의 opt-out 성격, 단계별 준수사항, 사고 영상 이용과 가명·익명처리 없는 AI 학습 구분, 익명·가명처리 권고를 설명한다.",
      "cited_by": [
        "docs/categories/security-and-privacy/privacy-and-video-data.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1137",
      "org": "정보통신신문",
      "title": "\"자율주행차·로봇 카메라 촬영 시 외부에 표시해야\"",
      "published": "2024-10-14",
      "url": "https://www.koit.co.kr/news/articleView.html?idxno=125844",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "안내서 공개 보도. 자율주행차·배달로봇 외부 촬영 표시, AI 개발 전 얼굴 모자이크, 위탁 처리 시 보호책임자·정기 점검을 전한다. 내용이 개인정보보호위원회 게시 안내서와 일치해 medium.",
      "cited_by": [
        "docs/categories/security-and-privacy/privacy-and-video-data.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1138",
      "org": "개인정보보호위원회 (개인정보 포털)",
      "title": "개인정보 포털 — 이동형 영상정보처리기기 제도 및 신청방법 안내",
      "published": null,
      "url": "https://www.privacy.go.kr/front/contents/cntntsView.do?contsNo=286",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-09-30",
      "summary": "이동형 영상정보처리기기의 정의, 공개 장소 업무 목적 촬영 제한과 예외, 불빛·소리·안내판 등 촬영 표시, 드론의 인터넷 공지 방식을 안내한다.",
      "cited_by": [
        "docs/categories/security-and-privacy/privacy-and-video-data.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1139",
      "org": "개인정보보호위원회 (대한민국 정책브리핑)",
      "title": "자율주행차·이동형 로봇 개발에 ‘영상데이터’ 원본 활용 허용",
      "published": "2023-11-15",
      "url": "https://www.korea.kr/news/policyNewsView.do?newsId=148922669",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "자율주행차·이동형 로봇 서비스 고도화 목적의 영상정보 원본 활용 규제샌드박스 실증특례를 11월부터 운영하고 연내 9개 기업 승인을 추진한다는 정책 보도. 보도자료 성격이라 medium.",
      "cited_by": [
        "docs/categories/security-and-privacy/privacy-and-video-data.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1140",
      "org": "법무법인(유) 세종",
      "title": "개인정보보호위원회, 비정형데이터 가명처리 관련 가명정보 처리 가이드라인 개정 (뉴스레터)",
      "published": "2024-02-08",
      "url": "https://www.shinkim.com/kor/media/newsletter/2342",
      "type": "업계 보고서",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "2024-02 개정 가명정보 처리 가이드라인의 비정형 데이터(영상·이미지·음성·텍스트) 가명처리 기준과 처리 방법, 시나리오를 요약한 법률사무소 뉴스레터.",
      "cited_by": [
        "docs/categories/security-and-privacy/privacy-and-video-data.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1141",
      "org": "경향신문",
      "title": "로봇청소기가 우리집 사진 찍어 외부 유출?…6종 ... (제목 일부만 확인)",
      "published": "2025-09-02",
      "url": "https://www.khan.co.kr/article/202509021447001",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "한국소비자원·한국인터넷진흥원의 로봇청소기 6종 보안 점검 결과 보도. 3개 제품의 사용자 인증 미비로 집 내부 사진 노출·카메라 강제 활성화 위험을 전한다.",
      "cited_by": [
        "docs/categories/security-and-privacy/privacy-and-video-data.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1142",
      "org": "아시아경제",
      "title": "\"로봇청소기 개인정보 관리 대체로 안전…미흡 사례 ... (제목 일부만 확인)",
      "published": "2026-09-14",
      "url": "https://view.asiae.co.kr/article/2026091410054053414",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-09-30",
      "summary": "개인정보보호위원회의 로봇청소기 5개 사업자 점검 결과 보도. 영상·음성·사진 침해 위험 미확인, 영상 직접 전송·사진 브랜드별 삭제, 동의 구분·국외 이전 고지 등 미흡 사항을 전한다.",
      "cited_by": [
        "docs/categories/security-and-privacy/privacy-and-video-data.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-968",
      "org": "MIT Technology Review",
      "title": "A Roomba recorded a woman on the toilet. How did screenshots end up on Facebook?",
      "published": "2022-12-19",
      "url": "https://www.technologyreview.com/2022/12/19/1065306/roomba-irobot-robot-vacuums-artificial-intelligence-training-data-privacy/",
      "type": "기사",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "개발용 Roomba J7 이 찍은 가정 내 사적 이미지가 라벨링 위탁 사슬을 거쳐 SNS 에 유출된 경위를 밝힌 탐사 보도. 사건의 1차 보도라 medium.",
      "cited_by": [
        "docs/categories/security-and-privacy/privacy-and-video-data.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1144",
      "org": "Raina, N., Somasundaram, G., Zheng, K. 외 (Meta Reality Labs, arXiv)",
      "title": "EgoBlur: Responsible Innovation in Aria",
      "published": "2023-08-24",
      "url": "https://arxiv.org/abs/2308.13093",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "1인칭 영상의 행인 얼굴·차량 번호판을 검출해 가우시안 블러로 가리는 익명화 모델을 공개한 프리프린트. 초록만 확인.",
      "cited_by": [
        "docs/categories/security-and-privacy/privacy-and-video-data.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1145",
      "org": "Choi, M. 외 (arXiv)",
      "title": "Real-Time Privacy Preservation for Robot Visual Perception",
      "published": "2025-05-08",
      "url": "https://arxiv.org/abs/2505.05519",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "논리 명세와 등각 예측으로 민감 객체를 실시간으로 가리는 PCVS 방법을 제안한 프리프린트. 초록만 확인.",
      "cited_by": [
        "docs/categories/security-and-privacy/privacy-and-video-data.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1146",
      "org": "Huang, X., Pan, S., Reinhardt, D., & Bennewitz, M. (arXiv)",
      "title": "Designing Privacy-Preserving Visual Perception for Robot Navigation Based on User Privacy Preferences",
      "published": "2026-04-07",
      "url": "https://arxiv.org/abs/2604.06382",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "두 사용자 연구로 이동 서비스 로봇 카메라의 선호 가림 방식과 거리–해상도 관계를 밝히고 사용자 설정 정책을 제안한 프리프린트. 초록만 확인.",
      "cited_by": [
        "docs/categories/security-and-privacy/privacy-and-video-data.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1147",
      "org": "Xu, Y., & Ayday, E. (arXiv)",
      "title": "Seeing Less Is Not Seeing Safely: Privacy Leakage from Task-Scoped Robot Perception Exports",
      "published": "2026-09-02",
      "url": "https://arxiv.org/abs/2609.03055",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "가정용 로봇의 작업 한정 인지 출력이 과업 성능이 같아도 재식별 위험이 크게 다름을 시뮬레이션(AI2-THOR·ProcTHOR, 120개 장면)으로 보인 프리프린트. 초록만 확인.",
      "cited_by": [
        "docs/categories/security-and-privacy/privacy-and-video-data.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1148",
      "org": "Sarfraz, B. M., Saplacan Lindblom, D., Baselizadeh, A., & Torresen, J. (HRI Companion '26)",
      "title": "The Privacy-Preserving Capabilities of a Service Robot in a Scenario-Based Healthcare Setting",
      "published": "2026-03-16",
      "url": "https://doi.org/10.1145/3776734.3794481",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "원문 미열람. 의사·환자 얼굴 인식과 비대상자 얼굴 가림을 진료실 모의 시나리오로 실험한 HRI 2026 컴패니언 논문으로, 검색 결과 요약으로만 확인했다(ACM 페이지 403).",
      "cited_by": [
        "docs/categories/security-and-privacy/privacy-and-video-data.md"
      ],
      "source_unopened": true
    },
    {
      "id": "ref-1149",
      "org": "European Data Protection Board (EDPB)",
      "title": "Guidelines 3/2019 on processing of personal data through video devices",
      "published": "2020-01",
      "url": "https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-32019-processing-personal-data-through-video_en",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-09-30",
      "summary": "GDPR 을 영상 장치 처리에 적용하는 EDPB 지침 최종판의 소개 페이지. PDF 본문 추출에 실패해 소개 페이지 범위(제목·최종판 채택)만 확인했다.",
      "cited_by": [
        "docs/categories/security-and-privacy/privacy-and-video-data.md"
      ],
      "source_unopened": false
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "여러 제조사 로봇의 영상과 위치 정보를 모아 관제하는 플랫폼 사업자는 개인정보 보호법상 이동형 영상정보처리기기 운영자인가, 현장 운영 사업자의 수탁자인가, 그리고 촬영 표시·거부 의사 처리 의무는 누구에게 있는가?",
      "areas": [
        53,
        58
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "로봇이 플랫폼·클라우드·로그로 내보내는 인지 출력(객체 목록·의미 지도·궤적)의 재식별 위험을 측정하는 공개 평가 기준이나 벤치마크가 있는가?",
      "areas": [
        53,
        54
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "피촬영자가 한 로봇에 밝힌 촬영 거부 의사를 같은 현장의 다른 로봇과 플랫폼 기록에 공통으로 반영하는 방법이나 운영 사례가 있는가?",
      "areas": [
        53,
        19
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "유럽데이터보호이사회(European Data Protection Board, EDPB) 영상 장치 지침 3/2019 를 이동 로봇 카메라에 적용한 유럽 감독기관의 결정이나 해석 사례가 있으며, 보존 기간 권고는 무엇인가?",
      "areas": [
        53,
        59
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "가정",
      "item": "시작 조건",
      "link": "docs/categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시",
      "title": "53. 개인정보·영상 데이터"
    },
    {
      "site_type": "가정",
      "item": "작업 대상",
      "link": "docs/categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시",
      "title": "53. 개인정보·영상 데이터"
    },
    {
      "site_type": "가정",
      "item": "수행 자원",
      "link": "docs/categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시",
      "title": "53. 개인정보·영상 데이터"
    },
    {
      "site_type": "가정",
      "item": "제약",
      "link": "docs/categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시",
      "title": "53. 개인정보·영상 데이터"
    },
    {
      "site_type": "가정",
      "item": "완료·인계",
      "link": "docs/categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시",
      "title": "53. 개인정보·영상 데이터"
    },
    {
      "site_type": "가정",
      "item": "예외·성과",
      "link": "docs/categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시",
      "title": "53. 개인정보·영상 데이터"
    },
    {
      "site_type": "병원",
      "item": "작업 대상",
      "link": "docs/categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시",
      "title": "53. 개인정보·영상 데이터"
    },
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시",
      "title": "53. 개인정보·영상 데이터"
    },
    {
      "site_type": "병원",
      "item": "예외·성과",
      "link": "docs/categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시",
      "title": "53. 개인정보·영상 데이터"
    },
    {
      "site_type": "실외",
      "item": "시작 조건",
      "link": "docs/categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시",
      "title": "53. 개인정보·영상 데이터"
    },
    {
      "site_type": "실외",
      "item": "작업 대상",
      "link": "docs/categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시",
      "title": "53. 개인정보·영상 데이터"
    },
    {
      "site_type": "실외",
      "item": "수행 자원",
      "link": "docs/categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시",
      "title": "53. 개인정보·영상 데이터"
    },
    {
      "site_type": "실외",
      "item": "제약",
      "link": "docs/categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시",
      "title": "53. 개인정보·영상 데이터"
    },
    {
      "site_type": "실외",
      "item": "완료·인계",
      "link": "docs/categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시",
      "title": "53. 개인정보·영상 데이터"
    },
    {
      "site_type": "실외",
      "item": "예외·성과",
      "link": "docs/categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시",
      "title": "53. 개인정보·영상 데이터"
    }
  ],
  "standards_updates": [
    {
      "name": "개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한)",
      "kind": "프레임워크",
      "org": "개인정보보호위원회",
      "url": "https://www.privacy.go.kr/front/contents/cntntsView.do?contsNo=286",
      "related_areas": [
        53,
        59
      ],
      "summary": "업무 목적으로 공개된 장소에서 이동형 기기로 사람을 촬영하는 것을 원칙적으로 제한하고, 동의 등의 경우와 촬영 사실을 표시했는데도 거부 의사가 없는 경우를 허용하며, 불빛·소리·안내판 등으로 촬영 사실을 표시하게 하는 법령 조항이다.",
      "ref_id": "ref-1138"
    },
    {
      "name": "이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서(2024.9.)",
      "kind": "프레임워크",
      "org": "개인정보보호위원회",
      "url": "https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS217&mCode=G010030000&nttId=10679",
      "related_areas": [
        53,
        59,
        66
      ],
      "summary": "2024-10-14 게시된 안내서로, 드론·로봇 등 이동형 기기로 공개된 장소에서 개인 식별 영상을 촬영할 수 있는 경우와 수집·이용 시 보호·활용 기준을 제시한다.",
      "ref_id": "ref-1135"
    },
    {
      "name": "가명정보 처리 가이드라인(2024-02 개정, 비정형 데이터 포함)",
      "kind": "프레임워크",
      "org": "개인정보보호위원회",
      "url": "https://www.shinkim.com/kor/media/newsletter/2342",
      "related_areas": [
        53,
        45,
        47
      ],
      "summary": "영상·이미지·음성·텍스트 같은 비정형 데이터의 가명처리 기준(식별 위험 판단, 기술 신뢰성 문서화, 처리 후 자체 검증)과 영상 처리 방법을 제시한다(법률사무소 요약 기준).",
      "ref_id": "ref-1140"
    },
    {
      "name": "영상정보 원본 활용 규제샌드박스 실증특례",
      "kind": "프레임워크",
      "org": "개인정보보호위원회",
      "url": "https://www.korea.kr/news/policyNewsView.do?newsId=148922669",
      "related_areas": [
        53,
        59,
        47
      ],
      "summary": "자율주행차·이동형 로봇 서비스 고도화 목적으로 영상정보 원본 활용을 허용하는 특례로, 2023-11 운영과 연내 9개 기업 승인 추진이 발표되었다.",
      "ref_id": "ref-1139"
    },
    {
      "name": "EDPB Guidelines 3/2019 on processing of personal data through video devices",
      "kind": "프레임워크",
      "org": "European Data Protection Board (EDPB)",
      "url": "https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-32019-processing-personal-data-through-video_en",
      "related_areas": [
        53,
        59
      ],
      "summary": "일반 개인정보 보호법(GDPR)을 영상 장치의 개인정보 처리에 적용하는 지침으로 최종판을 2020-01 채택했다. 다루는 범위 세부는 원문 미확인.",
      "ref_id": "ref-1149"
    },
    {
      "name": "EgoBlur",
      "kind": "오픈소스",
      "org": "Meta Reality Labs",
      "url": "https://arxiv.org/abs/2308.13093",
      "related_areas": [
        53,
        45
      ],
      "summary": "1인칭 영상에서 행인 얼굴과 차량 번호판을 검출해 가우시안 블러로 가리는 익명화 모델로 2023년 공개되었다.",
      "ref_id": "ref-1144"
    }
  ],
  "additional_research_requests": [
    "6절·9절: 개인정보 보호법 제25조의2 조문 원문(국가법령정보센터)으로 '목욕실 등 사생활 침해 우려가 큰 장소 촬영 금지' 구절의 존재와 문구를 확인해야 한다. 현재 인용 출처에 없어 [추정]·법령 원문 미확인으로 두었다.",
    "4·6절: 이동형 영상정보처리기기 안내서(2024.9.) PDF 원문으로 opt-out·다중 채널 표시·사고 영상·AI 학습 판단을 확인해 법률사무소 요약 의존을 줄일 필요가 있다.",
    "7절: 유럽데이터보호이사회(EDPB) 지침 3/2019 본문(PDF)에서 다루는 범위(적법 근거·투명성·정보주체 권리·보존 기간·가정 예외)를 확인해야 한다. 검증에서 해당 구절을 삭제했다.",
    "3·6절: 핵심 질문의 '사람의 위치 정보' 부분(보행자 위치 최소 수집, 궤적 익명화)을 직접 다룬 자료가 없어 본문에 넣지 못했다.",
    "5절: 물류창고·제조 공장·상업 시설·기타 현장의 로봇 영상·작업자 데이터 보호 사례를 찾지 못해 해당 현장 유형 사례를 쓰지 못했다.",
    "7절: 가명정보 처리 가이드라인(2024-02 개정) 원문(발행 기관 개인정보보호위원회 게시 URL)과 ISO 31700-1:2023(소비재 개인정보 중심 설계)을 확인하면 표와 표준 목록 URL을 보강할 수 있다.",
    "5절 병원 사례: HRI 2026 컴패니언 논문 원문으로 시작 조건·제약·완료·인계 칸(현재 미확인)을 채울 근거가 필요하다.",
    "11절 oq-171·oq-181·oq-214: 병원·세대 내부의 '공개된 장소' 해당 여부 해석과 안전성 확보조치 기준 개정판 조항 조사가 필요하다.",
    "다음 실행 후보: 65. 가정·공동주택 페이지 5절에 로봇청소기 점검·유출 사례(ref-1141·ref-1142·ref-968), 63. 병원·의료 페이지에 모의 진료실 얼굴 가림 실험(ref-1148) 반영을 제안한다(예산으로 이번 실행에서는 미룸)."
  ],
  "fixes_applied": [
    "f2 목욕실 등 촬영 금지 구절 강등 — 6절 '촬영 사실 표시와 거부 의사 수용'에서 공개 장소 촬영 제한·예외·표시 방법 문장은 [사실][^ref-1138][^ref-588]으로 두고, 목욕실 등 촬영 금지 구절은 별도 문장으로 떼어 [추정]과 '법령 원문 미확인'을 병기했다.",
    "f21 촬영 금지 장소 예시 변경 — 9절 표 '업종별 조건' 행의 '촬영 금지 장소(화장실·탈의실 등)'를 '사생활 침해 우려 장소(해당 법령 조항은 원문 미확인)'로 바꿨고, 10절 16. 장소 의미·지도 관리 연결도 '촬영 제한이 필요한 장소'로 일반화했다.",
    "f5 문구 정정 — 5절 실외 사례 예외·성과 칸과 6절 '목적별 이용 구분과 가명처리'에서 '가명·익명처리 없이 인공지능 학습에 쓰는 것은 예측 가능성이 있다고 보기 어렵고, 원본이 필요하면 규제샌드박스(실증특례)를 활용해야 한다'로 고치고 자율주행차 등 고속 이동 기기 맥락임을 밝혔다. 3절 종합 문장도 '가명·익명처리 없는 인공지능 학습'으로 맞췄다.",
    "f16 정정 — 6절 '인지 출력 필드 설계'에 시뮬레이션(AI2-THOR·ProcTHOR, 120개 장면) 결과임을 명시하고 '목표 범주 macro-F1 이 1.000에서 0.077로'로 고쳤으며, 8절 요약에도 시뮬레이션임을 밝혔다.",
    "f18 범위 구절 삭제 — 7절 표 EDPB 행에서 '적법 근거·투명성·정보주체 권리·기술적 보호조치' 목록을 삭제하고 최종판 채택(2020-01)만 [사실]로 두었으며 '다루는 범위 세부는 원문 미확인'을 적었다.",
    "f11 삭제 조건 정정 — 5절 가정 사례 완료·인계 칸을 '장애물 인식 사진은 브랜드별로 다음 청소 때, 이용자가 조회한 뒤, 또는 24시간 후 삭제'로 고쳤다.",
    "f8 한정 표현 완화 — 4절 용어와 7절 표, 용어집 정의에서 '서비스 고도화 목적에 한해'를 '서비스 고도화 목적으로'로 바꿨다.",
    "f1 정의 문구 — 4절 이동형 영상정보처리기기 정의를 원문대로 '부착·거치하여'로 적었다.",
    "ref-588 발행일 — 13절 각주의 발행일을 2024-10-14로 채우고 reference_updates 의 published 도 2024-10-14로 고쳤다.",
    "ref-1140 발행일 — 13절 각주와 reference_updates 의 발행일을 2024-02-08로 채웠다.",
    "ref-1148 서지 정정 — 제목을 'The Privacy-Preserving Capabilities of a Service Robot in a Scenario-Based Healthcare Setting', 기관·저자를 'Sarfraz, B. M., Saplacan Lindblom, D., Baselizadeh, A., & Torresen, J. (HRI Companion '26)', 발행일을 2026-03-16으로 13절 각주·8절·reference_updates 에 반영하고, 각주 접근일 뒤 ' (원문 미열람)'과 source_unopened: true 를 유지했다.",
    "ref-1137 제목 — '(제목 일부만 확인)'을 지우고 '\"자율주행차·로봇 카메라 촬영 시 외부에 표시해야\"'로 13절 각주와 reference_updates 에 적었다.",
    "6·9절 범위 경계 — 6절 '검출 후 가림'과 5절 가정·병원 사례 서술에서 기기 쪽 얼굴 검출·가림과 모바일앱 인증을 분류 원문 19장 '로봇 자체 지능·제어' 쪽 연계 대상으로 서술하고, 9절 ROP 직접 범위를 등록 정보 기록·목적별 데이터 흐름·보유 기간·출력 필드 축소·거부 의사 전달로 한정했다.",
    "용어집 실증특례 정의 — '안전조치를 조건으로'와 '한시적'을 정의에서 빼고, description 에 안전조치 항목과 특례 기간은 미확인이라고 적었다.",
    "5절 현장 유형 — 가정(f10~f12), 병원(f17, 모의 실험임 명시), 실외(f7)만 사례로 쓰고 물류창고·제조 공장·상업 시설·기타 사례는 찾지 못했다고 절 첫머리에 적었으며, site_matrix_updates 는 가정·병원·실외 세 현장 유형 칸만 냈다.",
    "분량 초과 자동 분리: 53. 개인정보·영상 데이터 본문 11,190자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 3,997자",
    "2차: 8절 Xu·Ayday 태그 — 분리 페이지 2026-09-30-area53-s8.md 에서 '시뮬레이션으로 보였다'까지를 [사실][^ref-1147]로 두고, '이 결과는 플랫폼이 로봇에서 받는 데이터의 필드 설계와 직접 이어지는 것으로 보인다'를 별도 문장으로 떼어 [추정][^ref-1147]로 표시했다.",
    "2차: 11절 등록 문장 일치 — 분리 페이지 2026-09-30-area53-s11.md 의 oq-143·oq-171·oq-181·oq-185·oq-211·oq-214·oq-228 질문 문장을 docs/open-questions.md 등록 문장 그대로 옮기고(oq-171 괄호 문구, oq-181 '그리고 이에 대한 개인정보보호위원회 해석이나 가이드라인이 있는가', oq-185 '(1X NEO 등)', oq-228 '국내 개인정보 보호 법령의' 복원), 이번 실행의 메모는 질문 문장 뒤 별도 문장으로 두었다.",
    "2차: 11절 메모 태그·각주 — oq-181 뒤 로봇청소기 점검 부분 근거 메모에 [추정][^ref-1142]를, oq-228 뒤 안내서 사고 영상·인공지능 학습 판단 부분 근거 메모에 [추정][^ref-588]을 붙이고, 분리 페이지 8. 출처에 두 각주 정의를 두었으며 프런트매터 sources 를 [ref-588, ref-1142]로 채웠다.",
    "2차: 약어 풀어쓰기 — 7절 분리 페이지 표에서 EDPB 를 '유럽데이터보호이사회(European Data Protection Board, EDPB)', GDPR 을 '일반 개인정보 보호법(General Data Protection Regulation, GDPR)'으로, 10절 분리 페이지 59번 연결과 11절 분리 페이지 새 질문(및 open_question_updates 의 같은 질문)에서 EDPB 를 같은 방식으로, 3절 분리 페이지의 SNS 를 '소셜 네트워크 서비스(SNS)'로 풀어 썼다."
  ]
}
```

### runs/2026-09-30-16/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
```

### runs/2026-09-30-16/pages/categories/security-and-privacy/privacy-and-video-data.md

```markdown
---
title: "53. 개인정보·영상 데이터"
type: area
category: "N. 보안·개인정보"
area_no: 53
related_areas: [16, 19, 37, 43, 45, 47, 50, 51, 52, 54, 58, 59, 60, 63, 65, 66]
tags: [이동형 영상정보처리기기, 촬영 거부, 가명처리, 얼굴 가림, 작업 한정 인지 출력]
status: draft
confidence: medium
created: 2026-09-28
updated: 2026-09-30
sources: [ref-1135, ref-588, ref-1137, ref-1138, ref-1139, ref-1140, ref-1141, ref-1142, ref-968, ref-1144, ref-1145, ref-1146, ref-1147, ref-1148, ref-1149]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [N. 보안·개인정보](index.md) › 53. 개인정보·영상 데이터

# 53. 개인정보·영상 데이터

!!! info "소속 대분류"
    [N. 보안·개인정보](index.md) — 핵심 질문:
    누가 어떤 로봇에 무엇을 시킬 수 있는지 통제하고, 데이터와 사람의 정보를 어떻게 지킬 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

영상·작업자·거주자 데이터 보호, 최소 수집·익명화 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **개인정보·영상 데이터 보호**: 카메라 영상과 작업자·환자·거주자 데이터를 보호한다
- **사람 데이터 최소 수집·익명화**: 보행자 위치·영상에서 신원을 떼어 내고 필요한 만큼만 모은다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 26번 영역 ‘사이버보안·접근권한·개인정보’에서 왔다. 그 본문은 [51. 인증·권한·격리](authentication-authorization-and-isolation.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

로봇이 찍은 영상과 사람의 위치 정보를 어디까지 모으고 어떻게 지킬 것인가? [분류원문]

## 3. 왜 중요한가

로봇 영상은 촬영 장치 자체보다 학습·라벨링 위탁 같은 이차 이용 경로에서 유출 위험이 커지는 것으로 보여, 영상을 모으는 쪽이 이차 이용 목적과 위탁 사슬의 접근 범위를 수집 시점부터 정해 둘 필요가 있다. [추정][^ref-968][^ref-1137][^ref-588]

자세한 내용은 주제 페이지 [53. 개인정보·영상 데이터 — 왜 중요한가](../../topics/2026/2026-09-30-area53-s3.md)에 있다.

## 4. 핵심 개념과 용어

앞 절의 규칙과 기술을 읽으려면 다음 용어가 필요하다.

자세한 내용은 주제 페이지 [53. 개인정보·영상 데이터 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area53-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

이 영역의 근거는 가정·병원·실외 세 현장 유형에서만 찾았고, 물류창고·제조 공장·상업 시설·기타 현장의 로봇 영상 보호 사례는 이번 조사에서 찾지 못했다.

**현장 유형:** 가정

**사례:** 가정에서 카메라를 단 로봇청소기가 집 안을 촬영하고 사진·영상을 앱과 서버로 보냄

| 항목 | 내용 |
|---|---|
| 시작 조건 | 청소 중 장애물을 인식하려고 사진을 찍거나, 사용자가 앱에서 실시간 영상을 본다 [사실][^ref-1142] |
| 작업 대상 | 집 내부 사진·실시간 영상·음성 명령 같은 정보와 화면에 찍히는 거주자 [사실][^ref-1142][^ref-968] |
| 수행 자원 | 로봇청소기와 제조사의 모바일앱·서버, 개발 단계에서는 학습 데이터 라벨링 위탁 업체 [사실][^ref-1141][^ref-968] |
| 제약 | 앱의 사용자 인증·접근 통제, 동의 처리와 계약 이행 처리의 구분, 서비스 개선용 수집의 사전 거부 선택권, 국외 이전 고지, 국내대리인 지정 [사실][^ref-1141][^ref-1142] |
| 완료·인계 | 실시간 영상은 암호화해 사용자 앱으로 직접 보내고, 장애물 인식 사진은 브랜드별로 다음 청소 때, 이용자가 조회한 뒤, 또는 24시간 후 삭제한다(2026-09 점검 결과 보도 기준) [사실][^ref-1142] |
| 예외·성과 | 인증 미비 제품은 집 사진 노출·카메라 강제 활성화 위험이 있었고, 개발용 기기 영상은 라벨링 위탁 경로로 유출되었다 [사실][^ref-1141][^ref-968]. 처리량·비용 영향은 미확인 |

개인정보보호위원회가 2026-09-14 발표한 로봇청소기 5개 사업자 점검에서는 영상·음성·사진의 개인정보 침해 위험이 확인되지 않았고 음성 명령을 서버에 저장하지 않는 방식이 확인되었으나, 동의와 계약 이행 처리의 구분, 서비스 개선용 수집의 사전 거부 선택권, 국외 이전 고지, 국내대리인 지정은 미흡했다(기사 기준). [사실][^ref-1142] 앞서 2025-09 한국소비자원·한국인터넷진흥원 점검(모바일앱 보안·정책 관리·기기 보안)에서는 나르왈·드리미·에코백스 3개 제품의 사용자 인증 절차 미비가 지적되었고 삼성전자·LG전자 제품은 접근 통제와 업데이트 체계가 양호했다(기사 기준, 기관 보도자료 원문 미확인). [사실][^ref-1141]

해외 사례에서 iRobot은 Scale AI에 200만 장 넘는 이미지를 공유했으며, 시험 참가자 동의와 녹화 중 표시 스티커를 근거로 들었다. [사실][^ref-968] 이 사례에서 앱 인증·기기 보안은 제조사 몫의 연계 대상이고, 이 영역이 관여하는 부분은 영상의 전송 경로·보유 기간과 이차 이용 통제로 보인다. [추정][^ref-1141][^ref-1142][^ref-968]

**현장 유형:** 병원

**사례:** 병원 진료실(모의 시나리오)에서 서비스 로봇이 대상이 아닌 사람의 얼굴을 가림

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 진료실 안 의사·환자와 대상이 아닌 사람의 얼굴 영상 [사실][^ref-1148] |
| 수행 자원 | 의사·환자를 알아보도록 학습한 얼굴 인식으로 대상이 아닌 사람의 얼굴을 가리는 서비스 로봇 [사실][^ref-1148] |
| 제약 | 미확인 |
| 완료·인계 | 미확인 |
| 예외·성과 | 대상이 아닌 사람은 안정적으로 가려졌지만 자세 변화·가림·조명 변화가 인식 신뢰도를 낮춰 보호에 한계가 있었다 [사실][^ref-1148] |

이 사례는 실제 병원 도입이 아니라 진료실을 흉내 낸 모의 시나리오 실험이며, 논문 원문은 열지 못해 검색 결과 요약으로 확인했다. [사실][^ref-1148] 기기 쪽 얼굴 인식·가림은 제조사 쪽 연계 대상이고, 이 영역은 가린 영상인지 여부를 받아 데이터 흐름 규칙에 반영하는 쪽에 관여하는 것으로 보인다. [추정][^ref-1141][^ref-588]

**현장 유형:** 실외

**사례:** 공개된 장소를 다니는 배달로봇의 카메라 촬영

| 항목 | 내용 |
|---|---|
| 시작 조건 | 업무 목적으로 공개된 장소를 이동하며 카메라로 주변을 촬영한다 [사실][^ref-1138][^ref-1137] |
| 작업 대상 | 행인 등 개인을 알아볼 수 있는 영상 [사실][^ref-1135][^ref-1137] |
| 수행 자원 | 배달로봇과 그 운영 사업자, 영상 처리를 위탁받은 수탁자 [사실][^ref-1137] |
| 제약 | 로봇 외부에 촬영 사실과 구체적 내용을 표시하고, 명확히 거부하는 사람의 의사를 받아들여야 한다 [사실][^ref-1137][^ref-588] |
| 완료·인계 | 안내서는 보관·파기 단계에서 보유기간을 정하고 영상정보 보호책임자 지정과 운영방침 공개를 요구한다(법률사무소 요약 기준) [사실][^ref-588] |
| 예외·성과 | 안전 주행 목적으로 찍힌 사고 영상을 사고 원인 파악·보험 처리에 쓰는 것은 수집 목적과 관련성이 있다고 보지만, 가명·익명처리 없이 인공지능 학습에 쓰는 것은 예측 가능성이 있다고 보기 어렵다(자율주행차 등 고속 이동 기기 맥락) [사실][^ref-588] |

안내서 공개 보도(2024-10-14)는 카메라를 단 자율주행차와 배달로봇이 외부에 촬영 사실과 구체적 내용을 표시해야 하고, 영상 처리를 위탁할 때는 보호책임자 지정과 정기 점검이 필요하다고 전했다. [사실][^ref-1137] 외부 표시와 보호책임자 지정은 현장 운영 사업자의 의무이므로 ROP 입장에서는 연계 대상이며, 플랫폼은 로봇별 표시 수단을 기록하고 거부 의사를 여러 로봇에 전달하는 쪽을 맡는 것으로 보인다. [추정][^ref-588][^ref-1137]

## 6. 대표 접근법과 기술

로봇 영상 보호 접근법은 촬영 표시·거부 수용과 목적별 이용 구분 같은 운영 규칙, 기기·수집 단계의 가림·저해상도화, 플랫폼으로 내보내는 출력의 설계로 나눌 수 있으며, 기술마다 인식 오류나 재식별 위험의 한계가 보고되었다. [추정][^ref-588][^ref-1144][^ref-1147]

자세한 내용은 주제 페이지 [53. 개인정보·영상 데이터 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area53-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

앞 절의 접근법을 받치는 법령·지침·도구는 다음과 같다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

자세한 내용은 주제 페이지 [53. 개인정보·영상 데이터 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area53-s7.md)에 있다.

## 8. 대표 연구와 자료

기술 연구는 모두 프리프린트·학회 부록 논문이며 초록이나 검색 결과 요약 기준이다.

자세한 내용은 주제 페이지 [53. 개인정보·영상 데이터 — 대표 연구와 자료](../../topics/2026/2026-09-30-area53-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

확인한 자료를 종합하면 ROP가 직접 맡을 범위는 등록 정보 기록, 목적별 데이터 흐름·보유 기간 관리, 인지 출력 필드 축소, 거부 의사 전달로 보이고, 기기 쪽 처리와 운영자 의무는 연계 대상이다. [추정][^ref-588][^ref-1147][^ref-1141]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 로봇 등록 정보에 카메라 유무·촬영 사실 표시 수단·영상 전송 경로를 기록하고, 로봇이 내보내는 인지 출력의 필드를 과업에 필요한 만큼으로 줄이는 규칙을 둔다 [추정][^ref-1138][^ref-1147] | 연계 대상: 카메라 펌웨어, 기기 쪽 얼굴 검출·가림, 모바일앱 인증은 제조사가 맡는다 [추정][^ref-1141] |
| 업종별 조건 | 사생활 침해 우려 장소(해당 법령 조항은 원문 미확인)를 지도 구역으로 표시해 경로·카메라 모드 제약으로 반영하고, 촬영 거부 의사를 받아 여러 로봇에 전달하는 창구를 둔다 [추정][^ref-588] | 연계 대상: 로봇 외부 촬영 표시 부착과 영상정보 보호책임자 지정·운영방침 공개는 현장 운영 사업자가, 원본 영상 활용 특례 승인은 개인정보보호위원회가 맡는다 [추정][^ref-588][^ref-1137][^ref-1139] |
| 시설·설비 제어 | 시설 쪽 영상의 상태와 이용 여부를 받아 데이터 흐름 규칙에 반영한다 [추정][^ref-588] | 연계 대상: 시설 CCTV 운영은 시설 관리자가 맡는다 [추정][^ref-588] |

표와 별도로, 관제 표시·사고 조사·학습 같은 목적별로 영상·위치 데이터의 흐름과 보유 기간을 나눠 관리하는 일도 ROP 직접 범위로 보인다. [추정][^ref-588][^ref-1142]

이 경계는 제품 전략에 따라 이동할 수 있다([범위 경계](../../about/scope-boundary.md)). 이종 제조사를 연결하는 ROP는 기기 쪽 가림 처리와 앱 보안을 제조사에 맡기고, 그 결과와 상태를 받아 작업·경로·권한 제약과 데이터 흐름 규칙에 반영하는 쪽을 담당하는 것으로 보인다. [추정][^ref-1141][^ref-588][^ref-1139][^ref-1137]

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 권한·통신 보안, 지도·사람 모델, 기록·학습 데이터, 법규, 적용 현장과 이어진다.

자세한 내용은 주제 페이지 [53. 개인정보·영상 데이터 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area53-s10.md)에 있다.

## 11. 열린 질문

이 영역에 걸린 기존 질문은 모두 열림으로 유지하고, 이번 실행에서 새 질문 4건을 올린다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [53. 개인정보·영상 데이터 — 열린 질문](../../topics/2026/2026-09-30-area53-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-1135]: 개인정보보호위원회, [현재 안내서] 이동형 영상정보처리기기를 위한 개인영상정보 보호ㆍ활용 안내서(2024.9.), 2024-10-14, https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS217&mCode=G010030000&nttId=10679, 접근일 2026-09-30
[^ref-588]: 김·장 법률사무소, ‘이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서’ 공개 (뉴스레터), 2024-10-14, https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=30477, 접근일 2026-09-30
[^ref-1137]: 정보통신신문, "자율주행차·로봇 카메라 촬영 시 외부에 표시해야", 2024-10-14, https://www.koit.co.kr/news/articleView.html?idxno=125844, 접근일 2026-09-30
[^ref-1138]: 개인정보보호위원회 (개인정보 포털), 개인정보 포털 — 이동형 영상정보처리기기 제도 및 신청방법 안내, 미확인, https://www.privacy.go.kr/front/contents/cntntsView.do?contsNo=286, 접근일 2026-09-30
[^ref-1139]: 개인정보보호위원회 (대한민국 정책브리핑), 자율주행차·이동형 로봇 개발에 ‘영상데이터’ 원본 활용 허용, 2023-11-15, https://www.korea.kr/news/policyNewsView.do?newsId=148922669, 접근일 2026-09-30
[^ref-1141]: 경향신문, 로봇청소기가 우리집 사진 찍어 외부 유출?…6종 ... (제목 일부만 확인), 2025-09-02, https://www.khan.co.kr/article/202509021447001, 접근일 2026-09-30
[^ref-1142]: 아시아경제, "로봇청소기 개인정보 관리 대체로 안전…미흡 사례 ... (제목 일부만 확인), 2026-09-14, https://view.asiae.co.kr/article/2026091410054053414, 접근일 2026-09-30
[^ref-968]: MIT Technology Review, A Roomba recorded a woman on the toilet. How did screenshots end up on Facebook?, 2022-12-19, https://www.technologyreview.com/2022/12/19/1065306/roomba-irobot-robot-vacuums-artificial-intelligence-training-data-privacy/, 접근일 2026-09-30
[^ref-1144]: Raina, N., Somasundaram, G., Zheng, K. 외 (Meta Reality Labs, arXiv), EgoBlur: Responsible Innovation in Aria, 2023-08-24, https://arxiv.org/abs/2308.13093, 접근일 2026-09-30
[^ref-1147]: Xu, Y., & Ayday, E. (arXiv), Seeing Less Is Not Seeing Safely: Privacy Leakage from Task-Scoped Robot Perception Exports, 2026-09-02, https://arxiv.org/abs/2609.03055, 접근일 2026-09-30
[^ref-1148]: Sarfraz, B. M., Saplacan Lindblom, D., Baselizadeh, A., & Torresen, J. (HRI Companion '26), The Privacy-Preserving Capabilities of a Service Robot in a Scenario-Based Healthcare Setting, 2026-03-16, https://doi.org/10.1145/3776734.3794481, 접근일 2026-09-30 (원문 미열람)
```

### docs/categories/security-and-privacy/privacy-and-video-data.md

```markdown
---
title: "53. 개인정보·영상 데이터"
type: area
category: "N. 보안·개인정보"
area_no: 53
related_areas: []
tags: []
status: seed
created: 2026-09-28
updated: 2026-09-28
sources: []
version: 1
---

[홈](../../index.md) › [N. 보안·개인정보](index.md) › 53. 개인정보·영상 데이터

# 53. 개인정보·영상 데이터

!!! info "소속 대분류"
    [N. 보안·개인정보](index.md) — 핵심 질문:
    누가 어떤 로봇에 무엇을 시킬 수 있는지 통제하고, 데이터와 사람의 정보를 어떻게 지킬 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: seed · 신뢰도: 미부여 · 페이지 버전: 1 · 마지막 갱신: 2026-09-28 · 마지막 실행: 없음
<!-- auto:page-status:end -->

## 1. 한 줄 정의

영상·작업자·거주자 데이터 보호, 최소 수집·익명화 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **개인정보·영상 데이터 보호**: 카메라 영상과 작업자·환자·거주자 데이터를 보호한다
- **사람 데이터 최소 수집·익명화**: 보행자 위치·영상에서 신원을 떼어 내고 필요한 만큼만 모은다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 26번 영역 ‘사이버보안·접근권한·개인정보’에서 왔다. 그 본문은 [51. 인증·권한·격리](authentication-authorization-and-isolation.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

로봇이 찍은 영상과 사람의 위치 정보를 어디까지 모으고 어떻게 지킬 것인가? [분류원문]

## 3. 왜 중요한가

아직 작성되지 않음

## 4. 핵심 개념과 용어

아직 작성되지 않음

## 5. 적용 사례 (현장 유형 명시)

아직 작성되지 않음

## 6. 대표 접근법과 기술

아직 작성되지 않음

## 7. 관련 표준·프레임워크·오픈소스

아직 작성되지 않음

## 8. 대표 연구와 자료

아직 작성되지 않음

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

아직 작성되지 않음

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

아직 작성되지 않음

## 11. 열린 질문

아직 작성되지 않음

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
아직 기록된 업데이트가 없다.
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

(아직 각주가 없다. 본문이 작성되면 출처 각주를 여기에 둔다.)
```

### runs/2026-09-30-16/pages/topics/2026/2026-09-30-area53-s6.md

```markdown
---
title: "53. 개인정보·영상 데이터 — 대표 접근법과 기술"
type: topic
category: "N. 보안·개인정보"
primary_area_no: 53
related_areas: [16, 19, 37, 43, 45, 47, 50, 51, 52, 54, 58, 59, 60, 63, 65, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-588, ref-1137, ref-1138, ref-1140, ref-1141, ref-1144, ref-1145, ref-1146, ref-1147, ref-1148]
last_run: 2026-09-30
version: 1
split_from: docs/categories/security-and-privacy/privacy-and-video-data.md#6
---

[홈](../../index.md) › [주제](../index.md) › 53. 개인정보·영상 데이터 — 대표 접근법과 기술

# 53. 개인정보·영상 데이터 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 로봇 영상 보호 접근법은 촬영 표시·거부 수용과 목적별 이용 구분 같은 운영 규칙, 기기·수집 단계의 가림·저해상도화, 플랫폼으로 내보내는 출력의 설계로 나눌 수 있으며, 기술마다 인식 오류나 재식별 위험의 한계가 보고되었다. [추정][^ref-588][^ref-1144][^ref-1147]
- 이 페이지는 [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

로봇 영상 보호 접근법은 촬영 표시·거부 수용과 목적별 이용 구분 같은 운영 규칙, 기기·수집 단계의 가림·저해상도화, 플랫폼으로 내보내는 출력의 설계로 나눌 수 있으며, 기술마다 인식 오류나 재식별 위험의 한계가 보고되었다. [추정][^ref-588][^ref-1144][^ref-1147]

### 촬영 사실 표시와 거부 의사 수용

개인정보 보호법 제25조의2는 업무 목적으로 공개된 장소에서 이동형 영상정보처리기기로 사람을 촬영하는 것을 원칙적으로 제한하되, 동의 등 제15조제1항의 경우와 촬영 사실을 명확히 표시했는데도 정보주체가 거부 의사를 밝히지 않은 경우 등을 허용하고, 촬영 시 불빛·소리·안내판 등으로 촬영 사실을 표시하게 한다. [사실][^ref-1138][^ref-588] 같은 조가 목욕실 등 사생활 침해 우려가 큰 장소에서의 촬영을 금지한다는 설명도 있으나, 인용한 출처에는 이 구절이 없어 법령 원문 미확인 상태다. [추정]

안내서는 촬영 사실 표시에 불빛·소리·안내판·안내서면·안내방송 등 기기 특성에 맞는 다중 채널 방식을 권장하고, 기획·설계 단계부터 목적 명확화와 최소 수집을 요구한다(안내서 원문이 아니라 법률사무소 요약 기준, 2024-10-14). [사실][^ref-588] 한계로, 안내서는 고속으로 이동하며 촬영하는 기기는 거부 의사를 파악하기 어렵다고 본다. [사실][^ref-588]

### 목적별 이용 구분과 가명처리

안내서는 안전 주행 목적으로 촬영된 사고 영상을 사고 원인 파악·보험 처리에 이용·제공하는 것은 당초 수집 목적과 관련성이 있다고 보지만, 자율주행차 등 고속 이동 기기의 영상을 가명·익명처리 없이 인공지능 학습에 쓰는 것은 예측 가능성이 있다고 보기 어렵고, 원본이 필요하면 규제샌드박스(실증특례)를 활용해야 한다고 설명한다. [사실][^ref-588] 같은 맥락에서 얼굴 모자이크 같은 익명·가명처리를 권고한다(두 출처 모두 안내서의 2차 요약). [사실][^ref-588][^ref-1137]

2024-02 개정 가명정보 처리 가이드라인은 처리 목적·환경·민감도에 따른 식별 위험 판단, 적용 기술의 신뢰성 문서화와 처리 후 자체 검증을 요구하고, 영상·이미지 처리 방법으로 필터링·암호화·합성 얼굴·인페인팅·AI 기반 처리를 제시한다(법률사무소 요약 기준). [사실][^ref-1140]

### 검출 후 가림

Meta Reality Labs의 EgoBlur(2023)는 1인칭 영상에서 행인 얼굴과 차량 번호판을 검출해 가우시안 블러로 가리는 익명화 모델을 공개했다. [사실][^ref-1144] 병원 모의 실험에서는 대상이 아닌 사람의 얼굴이 안정적으로 가려졌지만 자세·가림·조명 변화가 인식 신뢰도를 낮췄다. [사실][^ref-1148] 이런 기기·수집 단계의 얼굴 검출·가림은 분류 원문 19장의 '로봇 자체 지능·제어'(센서 인식) 쪽 연계 대상으로 보이며, ROP는 그 결과를 받아 데이터 흐름 규칙에 반영하는 쪽이다. [추정][^ref-1141][^ref-588]

### 명세 기반 실시간 가림

Choi 외(2025)의 PCVS는 '사람이 있을 때 얼굴을 보이지 않는다' 같은 논리 명세로 가릴 대상을 정하고, 프레임마다 검출과 등각 예측으로 명세 만족 확률의 하한을 보장하며 실시간으로 가린다. [사실][^ref-1145] 여러 데이터셋에서 95% 넘는 명세 만족을 보였고 가린 영상으로도 로봇이 정상 동작했다고 보고했다(프리프린트 초록 기준). [사실][^ref-1145]

### 촬영 시점 저해상도화

Huang·Pan·Reinhardt·Bennewitz(2026)는 카메라를 단 이동 서비스 로봇에 관한 두 차례 사용자 연구에서 사용자가 시각적 추상화와 촬영 시점 저해상도화를 선호하고, 원하는 해상도가 요구 프라이버시 수준과 로봇과의 거리에 따라 달라진다는 결과를 얻어 사용자가 설정하는 거리–해상도 정책을 제안했다. [사실][^ref-1146]

### 인지 출력 필드 설계

Xu·Ayday(2026-09)는 가정용 로봇이 원본 대신 내보내는 작업 한정 인지 출력 3종을 시뮬레이션(AI2-THOR·ProcTHOR, 120개 장면)에서 비교해, 과업 성공(1.000)과 경로 효율(0.898)은 같아도 표현 수준 연결 가능성이 0.532~0.970으로 크게 다르고, 목표 레이블을 공간 영역으로 바꾸면 목표 범주 macro-F1 이 1.000에서 0.077로 떨어지면서 과업 성공은 0.995를 유지했다고 보고했다. [사실][^ref-1147] 저자들은 필드 제거나 추상화가 보편적으로 더 안전하지 않아 과업별 평가가 필요하다고 결론지었다. [사실][^ref-1147]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/security-and-privacy/privacy-and-video-data.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/security-and-privacy/privacy-and-video-data.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md)
- 관련 영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/security-and-privacy/privacy-and-video-data.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-588]: 김·장 법률사무소, ‘이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서’ 공개 (뉴스레터), 2024-10-14, https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=30477, 접근일 2026-09-30
[^ref-1137]: 정보통신신문, "자율주행차·로봇 카메라 촬영 시 외부에 표시해야", 2024-10-14, https://www.koit.co.kr/news/articleView.html?idxno=125844, 접근일 2026-09-30
[^ref-1138]: 개인정보보호위원회 (개인정보 포털), 개인정보 포털 — 이동형 영상정보처리기기 제도 및 신청방법 안내, 미확인, https://www.privacy.go.kr/front/contents/cntntsView.do?contsNo=286, 접근일 2026-09-30
[^ref-1140]: 법무법인(유) 세종, 개인정보보호위원회, 비정형데이터 가명처리 관련 가명정보 처리 가이드라인 개정 (뉴스레터), 2024-02-08, https://www.shinkim.com/kor/media/newsletter/2342, 접근일 2026-09-30
[^ref-1141]: 경향신문, 로봇청소기가 우리집 사진 찍어 외부 유출?…6종 ... (제목 일부만 확인), 2025-09-02, https://www.khan.co.kr/article/202509021447001, 접근일 2026-09-30
[^ref-1144]: Raina, N., Somasundaram, G., Zheng, K. 외 (Meta Reality Labs, arXiv), EgoBlur: Responsible Innovation in Aria, 2023-08-24, https://arxiv.org/abs/2308.13093, 접근일 2026-09-30
[^ref-1145]: Choi, M. 외 (arXiv), Real-Time Privacy Preservation for Robot Visual Perception, 2025-05-08, https://arxiv.org/abs/2505.05519, 접근일 2026-09-30
[^ref-1146]: Huang, X., Pan, S., Reinhardt, D., & Bennewitz, M. (arXiv), Designing Privacy-Preserving Visual Perception for Robot Navigation Based on User Privacy Preferences, 2026-04-07, https://arxiv.org/abs/2604.06382, 접근일 2026-09-30
[^ref-1147]: Xu, Y., & Ayday, E. (arXiv), Seeing Less Is Not Seeing Safely: Privacy Leakage from Task-Scoped Robot Perception Exports, 2026-09-02, https://arxiv.org/abs/2609.03055, 접근일 2026-09-30
[^ref-1148]: Sarfraz, B. M., Saplacan Lindblom, D., Baselizadeh, A., & Torresen, J. (HRI Companion '26), The Privacy-Preserving Capabilities of a Service Robot in a Scenario-Based Healthcare Setting, 2026-03-16, https://doi.org/10.1145/3776734.3794481, 접근일 2026-09-30 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-16 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-16 | 53. 개인정보·영상 데이터 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-09-30-16/pages/topics/2026/2026-09-30-area53-s11.md

```markdown
---
title: "53. 개인정보·영상 데이터 — 열린 질문"
type: topic
category: "N. 보안·개인정보"
primary_area_no: 53
related_areas: [16, 19, 37, 43, 45, 47, 50, 51, 52, 54, 58, 59, 60, 63, 65, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-588, ref-1142]
last_run: 2026-09-30
version: 1
split_from: docs/categories/security-and-privacy/privacy-and-video-data.md#11
---

[홈](../../index.md) › [주제](../index.md) › 53. 개인정보·영상 데이터 — 열린 질문

# 53. 개인정보·영상 데이터 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역에 걸린 기존 질문은 모두 열림으로 유지하고, 이번 실행에서 새 질문 4건을 올린다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역에 걸린 기존 질문은 모두 열림으로 유지하고, 이번 실행에서 새 질문 4건을 올린다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

- **oq-143** (상태: 열림) ROP 의 로봇 대화 기능이 국내 인공지능 기본법의 고영향 인공지능이나 EU AI Act 의 고위험 AI 시스템에 해당하는지, 해당한다면 대화 기록 자동 로그의 항목과 보존 기간을 어떻게 정해야 하는가?
- **oq-171** (상태: 열림) 개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한)의 촬영 사실 표시·촬영 거부 규정이 병원 이송 로봇의 카메라·센서 촬영에 어떻게 적용되며, 환자·방문객 영상을 관제 계층이 어디까지 저장·전송할 수 있는지 법령 원문과 해석 사례로 확인할 수 있는가(이번 조사는 법령 원문을 열지 못했다)? 이번 실행에서도 병원 내부가 '공개된 장소'에 해당하는지에 대한 해석 원문은 확인하지 못했다.
- **oq-181** (상태: 열림) 세대 안에서 거주자가 쓰는 가사 로봇·로봇청소기의 영상 수집에는 개인정보 보호법 제25조의2(이동형 영상정보처리기기)가 적용되는가, 아니면 동의 기반 처리 조항만 적용되는가, 그리고 이에 대한 개인정보보호위원회 해석이나 가이드라인이 있는가? 2026-09 로봇청소기 점검이 동의와 계약 이행 처리의 구분을 점검한 것은 부분 근거로 보인다. [추정][^ref-1142] 적용 조항에 대한 해석은 이번 실행에서 확인하지 못했다.
- **oq-185** (상태: 열림) 소유자가 원격 조작자를 예약해 가정 로봇을 안내하게 하는 방식(1X NEO 등)에서 원격 조작자의 영상 접근·사고 책임을 다루는 국내외 규제·인증 기준이 있는가?
- **oq-211** (상태: 열림) 로봇 플랫폼이 수집하는 텔레메트리·주행 기록·영상의 보존 기간을 정한 국내 기준이나 운영 사례가 개인정보 접속기록 규정 밖에도 있는가?
- **oq-214** (상태: 열림) 로봇 플랫폼에 적용될 수 있는 현행 「개인정보의 안전성 확보조치 기준」(2023-6호 이후 개정판)의 접속기록 보관 기간·점검 주기 조항이 2023-6호와 같은가?
- **oq-228** (상태: 열림) 플랫폼이 시설 CCTV 영상을 로봇 운영용 장면 인식에 쓸 때 국내 개인정보 보호 법령의 고정형 영상정보처리기기 규정상 목적 외 이용이나 안내 의무가 문제 되는가? 이동형 기기 안내서의 사고 영상·인공지능 학습 판단은 부분 근거로 보인다. [추정][^ref-588] 고정형 기기에 대한 해석은 이번 실행에서 확인하지 못했다.
- (새 질문, 상태: 열림) 여러 제조사 로봇의 영상과 위치 정보를 모아 관제하는 플랫폼 사업자는 개인정보 보호법상 이동형 영상정보처리기기 운영자인가, 현장 운영 사업자의 수탁자인가, 그리고 촬영 표시·거부 의사 처리 의무는 누구에게 있는가?
- (새 질문, 상태: 열림) 로봇이 플랫폼·클라우드·로그로 내보내는 인지 출력(객체 목록·의미 지도·궤적)의 재식별 위험을 측정하는 공개 평가 기준이나 벤치마크가 있는가?
- (새 질문, 상태: 열림) 피촬영자가 한 로봇에 밝힌 촬영 거부 의사를 같은 현장의 다른 로봇과 플랫폼 기록에 공통으로 반영하는 방법이나 운영 사례가 있는가?
- (새 질문, 상태: 열림) 유럽데이터보호이사회(European Data Protection Board, EDPB) 영상 장치 지침 3/2019 를 이동 로봇 카메라에 적용한 유럽 감독기관의 결정이나 해석 사례가 있으며, 보존 기간 권고는 무엇인가?

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/security-and-privacy/privacy-and-video-data.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/security-and-privacy/privacy-and-video-data.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md)
- 관련 영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/security-and-privacy/privacy-and-video-data.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-588]: 김·장 법률사무소, ‘이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서’ 공개 (뉴스레터), 2024-10-14, https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=30477, 접근일 2026-09-30
[^ref-1142]: 아시아경제, "로봇청소기 개인정보 관리 대체로 안전…미흡 사례 ... (제목 일부만 확인), 2026-09-14, https://view.asiae.co.kr/article/2026091410054053414, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-16 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-16 | 53. 개인정보·영상 데이터 의 "열린 질문" 절에서 분리 |
```

### runs/2026-09-30-16/pages/topics/2026/2026-09-30-area53-s8.md

```markdown
---
title: "53. 개인정보·영상 데이터 — 대표 연구와 자료"
type: topic
category: "N. 보안·개인정보"
primary_area_no: 53
related_areas: [16, 19, 37, 43, 45, 47, 50, 51, 52, 54, 58, 59, 60, 63, 65, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-968, ref-1144, ref-1145, ref-1146, ref-1147, ref-1148]
last_run: 2026-09-30
version: 1
split_from: docs/categories/security-and-privacy/privacy-and-video-data.md#8
---

[홈](../../index.md) › [주제](../index.md) › 53. 개인정보·영상 데이터 — 대표 연구와 자료

# 53. 개인정보·영상 데이터 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 기술 연구는 모두 프리프린트·학회 부록 논문이며 초록이나 검색 결과 요약 기준이다.
- 이 페이지는 [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

기술 연구는 모두 프리프린트·학회 부록 논문이며 초록이나 검색 결과 요약 기준이다.

- Raina, Somasundaram, Zheng 외(Meta Reality Labs), EgoBlur: Responsible Innovation in Aria(2023) — 1인칭 영상의 행인 얼굴과 차량 번호판을 검출해 가우시안 블러로 가리는 익명화 모델을 공개했다. 수집 단계 가림 기술의 예다. [사실][^ref-1144]
- Choi 외, Real-Time Privacy Preservation for Robot Visual Perception(2025) — 논리 명세와 등각 예측으로 가릴 대상을 정하고 명세 만족 확률 하한을 보장하는 PCVS를 제안했고, 가린 영상으로도 로봇이 정상 동작함을 보고했다. [사실][^ref-1145]
- Huang, Pan, Reinhardt, Bennewitz, Designing Privacy-Preserving Visual Perception for Robot Navigation Based on User Privacy Preferences(2026) — 두 사용자 연구로 거리–해상도 프라이버시 정책을 제안했다. [사실][^ref-1146]
- Xu, Ayday, Seeing Less Is Not Seeing Safely: Privacy Leakage from Task-Scoped Robot Perception Exports(2026) — 과업 성능이 같은 인지 출력도 재식별 위험이 크게 다르다는 것을 시뮬레이션으로 보였다. [사실][^ref-1147] 이 결과는 플랫폼이 로봇에서 받는 데이터의 필드 설계와 직접 이어지는 것으로 보인다. [추정][^ref-1147]
- Sarfraz, Saplacan Lindblom, Baselizadeh, Torresen, The Privacy-Preserving Capabilities of a Service Robot in a Scenario-Based Healthcare Setting(HRI Companion 2026) — 진료실 모의 시나리오에서 대상이 아닌 사람의 얼굴 가림과 그 한계를 보고했다(원문 미열람). [사실][^ref-1148]
- MIT Technology Review, A Roomba recorded a woman on the toilet. How did screenshots end up on Facebook?(2022, 기사) — 개발용 로봇청소기 영상이 라벨링 위탁 사슬을 거쳐 유출된 경위를 밝힌 탐사 보도다. [사실][^ref-968]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/security-and-privacy/privacy-and-video-data.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/security-and-privacy/privacy-and-video-data.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md)
- 관련 영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/security-and-privacy/privacy-and-video-data.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-968]: MIT Technology Review, A Roomba recorded a woman on the toilet. How did screenshots end up on Facebook?, 2022-12-19, https://www.technologyreview.com/2022/12/19/1065306/roomba-irobot-robot-vacuums-artificial-intelligence-training-data-privacy/, 접근일 2026-09-30
[^ref-1144]: Raina, N., Somasundaram, G., Zheng, K. 외 (Meta Reality Labs, arXiv), EgoBlur: Responsible Innovation in Aria, 2023-08-24, https://arxiv.org/abs/2308.13093, 접근일 2026-09-30
[^ref-1145]: Choi, M. 외 (arXiv), Real-Time Privacy Preservation for Robot Visual Perception, 2025-05-08, https://arxiv.org/abs/2505.05519, 접근일 2026-09-30
[^ref-1146]: Huang, X., Pan, S., Reinhardt, D., & Bennewitz, M. (arXiv), Designing Privacy-Preserving Visual Perception for Robot Navigation Based on User Privacy Preferences, 2026-04-07, https://arxiv.org/abs/2604.06382, 접근일 2026-09-30
[^ref-1147]: Xu, Y., & Ayday, E. (arXiv), Seeing Less Is Not Seeing Safely: Privacy Leakage from Task-Scoped Robot Perception Exports, 2026-09-02, https://arxiv.org/abs/2609.03055, 접근일 2026-09-30
[^ref-1148]: Sarfraz, B. M., Saplacan Lindblom, D., Baselizadeh, A., & Torresen, J. (HRI Companion '26), The Privacy-Preserving Capabilities of a Service Robot in a Scenario-Based Healthcare Setting, 2026-03-16, https://doi.org/10.1145/3776734.3794481, 접근일 2026-09-30 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-16 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-16 | 53. 개인정보·영상 데이터 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-09-30-16/pages/topics/2026/2026-09-30-area53-s4.md

```markdown
---
title: "53. 개인정보·영상 데이터 — 핵심 개념과 용어"
type: topic
category: "N. 보안·개인정보"
primary_area_no: 53
related_areas: [16, 19, 37, 43, 45, 47, 50, 51, 52, 54, 58, 59, 60, 63, 65, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1135, ref-588, ref-1138, ref-1139, ref-1140, ref-1144, ref-1145, ref-1147]
last_run: 2026-09-30
version: 1
split_from: docs/categories/security-and-privacy/privacy-and-video-data.md#4
---

[홈](../../index.md) › [주제](../index.md) › 53. 개인정보·영상 데이터 — 핵심 개념과 용어

# 53. 개인정보·영상 데이터 — 핵심 개념과 용어

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 앞 절의 규칙과 기술을 읽으려면 다음 용어가 필요하다.
- 이 페이지는 [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md) 페이지의 "핵심 개념과 용어" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md) 페이지를 쓰는 과정에서 "핵심 개념과 용어" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

앞 절의 규칙과 기술을 읽으려면 다음 용어가 필요하다.

- **이동형 영상정보처리기기(Mobile Video Information Processing Device)** — 개인정보 보호법상 사람이 신체에 착용·휴대하거나 이동 가능한 물체에 부착·거치하여 사람 또는 사물의 영상을 촬영하는 장치이며, 개인정보보호위원회는 스마트안경·드론·자율주행차 등을 예로 들고 로봇도 같은 범주의 기기로 안내한다(두 출처 모두 개인정보보호위원회). [사실][^ref-1138][^ref-1135] 용어집: [이동형 영상정보처리기기](../../glossary/mobile-video-information-processing-device.md)
- **촬영 사실 표시** — 이동형 기기로 촬영할 때 불빛·소리·안내판 등으로 촬영 사실을 알리게 하는 요구다. [사실][^ref-1138][^ref-588]
- **촬영 거부(opt-out)** — 안내서는 촬영 거부를 사전 차단 권리가 아닌 선택 해제 방식으로 설명해, 기본적으로 촬영하되 피촬영자가 명확히 거부하면 운영자가 받아들이게 한다(법률사무소 요약 기준). [사실][^ref-588]
- **가명처리(Pseudonymisation)** — 2024-02 개정 가명정보 처리 가이드라인은 이미지·영상·음성·텍스트 같은 비정형 데이터를 가명처리 대상에 포함시켰다(법률사무소 요약 기준). [사실][^ref-1140]
- **영상정보 원본 활용 규제샌드박스 실증특례** — 개인정보보호위원회는 2023-11 자율주행차와 이동형 로봇 서비스 고도화 목적으로 영상정보 원본 활용 실증특례를 본격 운영하고 그해 안에 9개 기업 승인을 추진한다고 발표했다(2023-11-15 기준). [사실][^ref-1139]
- **얼굴 가림(Face Obfuscation)** — 영상에서 얼굴 등을 검출해 블러로 가리는 처리이며, 예로 EgoBlur는 1인칭 영상의 행인 얼굴과 차량 번호판을 가우시안 블러로 가린다. [사실][^ref-1144]
- **작업 한정 인지 출력(Task-scoped Perception Export)** — 로봇이 원본 영상 대신 계획기·클라우드·로그·학습 파이프라인으로 내보내는 과업용 인지 결과다. [사실][^ref-1147]
- **등각 예측(Conformal Prediction)** — PCVS가 가림 명세 만족 확률의 하한을 보장하는 데 쓰는 방법이다. [사실][^ref-1145] 용어집: [등각 예측](../../glossary/conformal-prediction.md)

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/security-and-privacy/privacy-and-video-data.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/security-and-privacy/privacy-and-video-data.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md)
- 관련 영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/security-and-privacy/privacy-and-video-data.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1135]: 개인정보보호위원회, [현재 안내서] 이동형 영상정보처리기기를 위한 개인영상정보 보호ㆍ활용 안내서(2024.9.), 2024-10-14, https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS217&mCode=G010030000&nttId=10679, 접근일 2026-09-30
[^ref-588]: 김·장 법률사무소, ‘이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서’ 공개 (뉴스레터), 2024-10-14, https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=30477, 접근일 2026-09-30
[^ref-1138]: 개인정보보호위원회 (개인정보 포털), 개인정보 포털 — 이동형 영상정보처리기기 제도 및 신청방법 안내, 미확인, https://www.privacy.go.kr/front/contents/cntntsView.do?contsNo=286, 접근일 2026-09-30
[^ref-1139]: 개인정보보호위원회 (대한민국 정책브리핑), 자율주행차·이동형 로봇 개발에 ‘영상데이터’ 원본 활용 허용, 2023-11-15, https://www.korea.kr/news/policyNewsView.do?newsId=148922669, 접근일 2026-09-30
[^ref-1140]: 법무법인(유) 세종, 개인정보보호위원회, 비정형데이터 가명처리 관련 가명정보 처리 가이드라인 개정 (뉴스레터), 2024-02-08, https://www.shinkim.com/kor/media/newsletter/2342, 접근일 2026-09-30
[^ref-1144]: Raina, N., Somasundaram, G., Zheng, K. 외 (Meta Reality Labs, arXiv), EgoBlur: Responsible Innovation in Aria, 2023-08-24, https://arxiv.org/abs/2308.13093, 접근일 2026-09-30
[^ref-1145]: Choi, M. 외 (arXiv), Real-Time Privacy Preservation for Robot Visual Perception, 2025-05-08, https://arxiv.org/abs/2505.05519, 접근일 2026-09-30
[^ref-1147]: Xu, Y., & Ayday, E. (arXiv), Seeing Less Is Not Seeing Safely: Privacy Leakage from Task-Scoped Robot Perception Exports, 2026-09-02, https://arxiv.org/abs/2609.03055, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-16 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-16 | 53. 개인정보·영상 데이터 의 "핵심 개념과 용어" 절에서 분리 |
```

### runs/2026-09-30-16/pages/topics/2026/2026-09-30-area53-s10.md

```markdown
---
title: "53. 개인정보·영상 데이터 — 다른 연구영역과의 연결"
type: topic
category: "N. 보안·개인정보"
primary_area_no: 53
related_areas: [16, 19, 37, 43, 45, 47, 50, 51, 52, 54, 58, 59, 60, 63, 65, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-588, ref-1137, ref-1138, ref-1139, ref-1140, ref-1141, ref-1142, ref-968, ref-1144, ref-1145, ref-1146, ref-1147, ref-1148, ref-1149]
last_run: 2026-09-30
version: 1
split_from: docs/categories/security-and-privacy/privacy-and-video-data.md#10
---

[홈](../../index.md) › [주제](../index.md) › 53. 개인정보·영상 데이터 — 다른 연구영역과의 연결

# 53. 개인정보·영상 데이터 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 권한·통신 보안, 지도·사람 모델, 기록·학습 데이터, 법규, 적용 현장과 이어진다.
- 이 페이지는 [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 권한·통신 보안, 지도·사람 모델, 기록·학습 데이터, 법규, 적용 현장과 이어진다.

- [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md) — 촬영 제한이 필요한 장소를 지도 구역으로 두어 경로·카메라 제약에 쓰는 연결이다. [추정][^ref-1138]
- [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) — 사람과의 거리에 따른 해상도 정책과 인지 출력의 재식별 위험이 보행자 위치 데이터와 맞물린다. [추정][^ref-1146][^ref-1147]
- [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md) — 관제에 띄우는 영상과 기록의 보유 기간을 정하는 연결이다. [추정][^ref-588][^ref-1142]
- [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md) — 영상·로그의 전송 경로와 보존·삭제 규칙이 데이터 계층에서 구현된다. [추정][^ref-588][^ref-1142]
- [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md) — 장면 인식 학습에 쓰는 영상의 가명처리와 가림 기술이 이어진다. [추정][^ref-1140][^ref-1144]
- [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md) — 학습 데이터 이용 목적 판단과 라벨링 위탁 관리가 이어진다. [추정][^ref-588][^ref-968]
- [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md) — 사고 영상을 사고 원인 파악에 쓰는 범위가 이어진다. [추정][^ref-588]
- [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md) — 앱 사용자 인증 미비가 영상 노출로 이어진 사례가 명령 권한·격리와 이어진다. [추정][^ref-1141]
- [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md) — 영상 암호화 전송과 보안 점검이 이어진다. [추정][^ref-1141][^ref-1142]
- [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md) — 가림 명세 만족과 재식별 위험 평가가 시험 대상이다. [추정][^ref-1145][^ref-1147]
- [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md) — 영상 처리 위탁과 운영자 책임이 이어진다. [추정][^ref-1137][^ref-968]
- [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) — 제25조의2, 원본 활용 특례, 유럽데이터보호이사회(European Data Protection Board, EDPB) 지침이 이어진다. [추정][^ref-1138][^ref-1139][^ref-1149]
- [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md) — 로봇 카메라에 대한 사용자 선호가 수용성과 이어진다. [추정][^ref-1146]
- [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md) — 진료실 얼굴 가림 모의 실험이 병원 현장 요구와 이어진다. [추정][^ref-1148]
- [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md) — 로봇청소기 영상 유출·점검 사례가 가정 현장 요구와 이어진다. [추정][^ref-1141][^ref-1142][^ref-968]
- [66. 실외](../../categories/site-type-applications/outdoor.md) — 배달로봇 외부 촬영 표시가 실외 현장 요구와 이어진다. [추정][^ref-1137]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/security-and-privacy/privacy-and-video-data.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/security-and-privacy/privacy-and-video-data.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md)
- 관련 영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/security-and-privacy/privacy-and-video-data.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-588]: 김·장 법률사무소, ‘이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서’ 공개 (뉴스레터), 2024-10-14, https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=30477, 접근일 2026-09-30
[^ref-1137]: 정보통신신문, "자율주행차·로봇 카메라 촬영 시 외부에 표시해야", 2024-10-14, https://www.koit.co.kr/news/articleView.html?idxno=125844, 접근일 2026-09-30
[^ref-1138]: 개인정보보호위원회 (개인정보 포털), 개인정보 포털 — 이동형 영상정보처리기기 제도 및 신청방법 안내, 미확인, https://www.privacy.go.kr/front/contents/cntntsView.do?contsNo=286, 접근일 2026-09-30
[^ref-1139]: 개인정보보호위원회 (대한민국 정책브리핑), 자율주행차·이동형 로봇 개발에 ‘영상데이터’ 원본 활용 허용, 2023-11-15, https://www.korea.kr/news/policyNewsView.do?newsId=148922669, 접근일 2026-09-30
[^ref-1140]: 법무법인(유) 세종, 개인정보보호위원회, 비정형데이터 가명처리 관련 가명정보 처리 가이드라인 개정 (뉴스레터), 2024-02-08, https://www.shinkim.com/kor/media/newsletter/2342, 접근일 2026-09-30
[^ref-1141]: 경향신문, 로봇청소기가 우리집 사진 찍어 외부 유출?…6종 ... (제목 일부만 확인), 2025-09-02, https://www.khan.co.kr/article/202509021447001, 접근일 2026-09-30
[^ref-1142]: 아시아경제, "로봇청소기 개인정보 관리 대체로 안전…미흡 사례 ... (제목 일부만 확인), 2026-09-14, https://view.asiae.co.kr/article/2026091410054053414, 접근일 2026-09-30
[^ref-968]: MIT Technology Review, A Roomba recorded a woman on the toilet. How did screenshots end up on Facebook?, 2022-12-19, https://www.technologyreview.com/2022/12/19/1065306/roomba-irobot-robot-vacuums-artificial-intelligence-training-data-privacy/, 접근일 2026-09-30
[^ref-1144]: Raina, N., Somasundaram, G., Zheng, K. 외 (Meta Reality Labs, arXiv), EgoBlur: Responsible Innovation in Aria, 2023-08-24, https://arxiv.org/abs/2308.13093, 접근일 2026-09-30
[^ref-1145]: Choi, M. 외 (arXiv), Real-Time Privacy Preservation for Robot Visual Perception, 2025-05-08, https://arxiv.org/abs/2505.05519, 접근일 2026-09-30
[^ref-1146]: Huang, X., Pan, S., Reinhardt, D., & Bennewitz, M. (arXiv), Designing Privacy-Preserving Visual Perception for Robot Navigation Based on User Privacy Preferences, 2026-04-07, https://arxiv.org/abs/2604.06382, 접근일 2026-09-30
[^ref-1147]: Xu, Y., & Ayday, E. (arXiv), Seeing Less Is Not Seeing Safely: Privacy Leakage from Task-Scoped Robot Perception Exports, 2026-09-02, https://arxiv.org/abs/2609.03055, 접근일 2026-09-30
[^ref-1148]: Sarfraz, B. M., Saplacan Lindblom, D., Baselizadeh, A., & Torresen, J. (HRI Companion '26), The Privacy-Preserving Capabilities of a Service Robot in a Scenario-Based Healthcare Setting, 2026-03-16, https://doi.org/10.1145/3776734.3794481, 접근일 2026-09-30 (원문 미열람)
[^ref-1149]: European Data Protection Board (EDPB), Guidelines 3/2019 on processing of personal data through video devices, 2020-01, https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-32019-processing-personal-data-through-video_en, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-16 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-16 | 53. 개인정보·영상 데이터 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-09-30-16/pages/topics/2026/2026-09-30-area53-s7.md

```markdown
---
title: "53. 개인정보·영상 데이터 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "N. 보안·개인정보"
primary_area_no: 53
related_areas: [16, 19, 37, 43, 45, 47, 50, 51, 52, 54, 58, 59, 60, 63, 65, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-1135, ref-588, ref-1137, ref-1138, ref-1139, ref-1140, ref-1144, ref-1149]
last_run: 2026-09-30
version: 1
split_from: docs/categories/security-and-privacy/privacy-and-video-data.md#7
---

[홈](../../index.md) › [주제](../index.md) › 53. 개인정보·영상 데이터 — 관련 표준·프레임워크·오픈소스

# 53. 개인정보·영상 데이터 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 앞 절의 접근법을 받치는 법령·지침·도구는 다음과 같다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.
- 이 페이지는 [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

앞 절의 접근법을 받치는 법령·지침·도구는 다음과 같다. 전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| 개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한) | 프레임워크 | 법령. 공개된 장소의 업무 목적 촬영 제한과 예외, 촬영 사실 표시를 정한다 [사실][^ref-1138][^ref-588] | 개인정보 포털, 김·장 법률사무소 뉴스레터 |
| 이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서(2024.9.) | 프레임워크 | 2024-10-14 게시. 제25조의2 신설에 따라 촬영할 수 있는 경우와 수집·이용 시 보호·활용 기준을 제시한다 [사실][^ref-1135][^ref-1137] | 개인정보보호위원회 게시판, 정보통신신문 |
| 가명정보 처리 가이드라인(2024-02 개정) | 프레임워크 | 영상·이미지 같은 비정형 데이터의 가명처리 기준과 처리 방법을 제시한다(법률사무소 요약 기준) [사실][^ref-1140] | 법무법인(유) 세종 뉴스레터 |
| 영상정보 원본 활용 규제샌드박스 실증특례 | 프레임워크 | 자율주행차·이동형 로봇 서비스 고도화 목적으로 영상 원본 활용을 허용하는 특례로 2023-11 운영을 발표했다 [사실][^ref-1139] | 대한민국 정책브리핑 |
| 유럽데이터보호이사회(European Data Protection Board, EDPB) Guidelines 3/2019(영상 장치를 통한 개인정보 처리) | 프레임워크 | 일반 개인정보 보호법(General Data Protection Regulation, GDPR)을 영상 장치의 개인정보 처리에 적용하는 지침으로 최종판을 2020-01 채택했다. 다루는 범위 세부는 원문 미확인 [사실][^ref-1149] | EDPB |
| EgoBlur | 오픈소스 | 1인칭 영상의 행인 얼굴·차량 번호판을 가리는 익명화 모델을 공개했다 [사실][^ref-1144] | arXiv |

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/security-and-privacy/privacy-and-video-data.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/security-and-privacy/privacy-and-video-data.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md)
- 관련 영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/security-and-privacy/privacy-and-video-data.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1135]: 개인정보보호위원회, [현재 안내서] 이동형 영상정보처리기기를 위한 개인영상정보 보호ㆍ활용 안내서(2024.9.), 2024-10-14, https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS217&mCode=G010030000&nttId=10679, 접근일 2026-09-30
[^ref-588]: 김·장 법률사무소, ‘이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서’ 공개 (뉴스레터), 2024-10-14, https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=30477, 접근일 2026-09-30
[^ref-1137]: 정보통신신문, "자율주행차·로봇 카메라 촬영 시 외부에 표시해야", 2024-10-14, https://www.koit.co.kr/news/articleView.html?idxno=125844, 접근일 2026-09-30
[^ref-1138]: 개인정보보호위원회 (개인정보 포털), 개인정보 포털 — 이동형 영상정보처리기기 제도 및 신청방법 안내, 미확인, https://www.privacy.go.kr/front/contents/cntntsView.do?contsNo=286, 접근일 2026-09-30
[^ref-1139]: 개인정보보호위원회 (대한민국 정책브리핑), 자율주행차·이동형 로봇 개발에 ‘영상데이터’ 원본 활용 허용, 2023-11-15, https://www.korea.kr/news/policyNewsView.do?newsId=148922669, 접근일 2026-09-30
[^ref-1140]: 법무법인(유) 세종, 개인정보보호위원회, 비정형데이터 가명처리 관련 가명정보 처리 가이드라인 개정 (뉴스레터), 2024-02-08, https://www.shinkim.com/kor/media/newsletter/2342, 접근일 2026-09-30
[^ref-1144]: Raina, N., Somasundaram, G., Zheng, K. 외 (Meta Reality Labs, arXiv), EgoBlur: Responsible Innovation in Aria, 2023-08-24, https://arxiv.org/abs/2308.13093, 접근일 2026-09-30
[^ref-1149]: European Data Protection Board (EDPB), Guidelines 3/2019 on processing of personal data through video devices, 2020-01, https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-32019-processing-personal-data-through-video_en, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-16 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-16 | 53. 개인정보·영상 데이터 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-09-30-16/pages/topics/2026/2026-09-30-area53-s3.md

```markdown
---
title: "53. 개인정보·영상 데이터 — 왜 중요한가"
type: topic
category: "N. 보안·개인정보"
primary_area_no: 53
related_areas: [16, 19, 37, 43, 45, 47, 50, 51, 52, 54, 58, 59, 60, 63, 65, 66]
tags: [분리 페이지]
status: draft
confidence: medium
created: 2026-09-30
updated: 2026-09-30
sources: [ref-588, ref-1137, ref-1138, ref-1140, ref-1141, ref-968, ref-1144, ref-1145, ref-1146, ref-1147, ref-1148]
last_run: 2026-09-30
version: 1
split_from: docs/categories/security-and-privacy/privacy-and-video-data.md#3
---

[홈](../../index.md) › [주제](../index.md) › 53. 개인정보·영상 데이터 — 왜 중요한가

# 53. 개인정보·영상 데이터 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 로봇 영상은 촬영 장치 자체보다 학습·라벨링 위탁 같은 이차 이용 경로에서 유출 위험이 커지는 것으로 보여, 영상을 모으는 쪽이 이차 이용 목적과 위탁 사슬의 접근 범위를 수집 시점부터 정해 둘 필요가 있다. [추정][^ref-968][^ref-1137][^ref-588]
- 이 페이지는 [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

로봇 영상은 촬영 장치 자체보다 학습·라벨링 위탁 같은 이차 이용 경로에서 유출 위험이 커지는 것으로 보여, 영상을 모으는 쪽이 이차 이용 목적과 위탁 사슬의 접근 범위를 수집 시점부터 정해 둘 필요가 있다. [추정][^ref-968][^ref-1137][^ref-588]

2022-12 보도에 따르면 카메라를 단 개발용 로봇청소기(iRobot Roomba J7 계열)가 시험 가정에서 찍은 화장실의 여성, 미성년자 등 사적 장면의 스크린샷 15장이 학습 데이터 라벨링 위탁(Scale AI의 해외 계약 작업자)을 거쳐 소셜 네트워크 서비스(SNS)에 유출되었다. [사실][^ref-968] 한국에서도 2025-09 보도에서 점검 대상 로봇청소기 6종 가운데 3개 제품이 사용자 인증 절차 미비로 집 내부 사진이 외부로 노출되거나 카메라가 강제로 활성화될 수 있었다고 전해졌다. [사실][^ref-1141]

확인한 자료를 종합하면 한국에서는 공개된 장소의 로봇 촬영에 촬영 사실 표시와 거부 의사 수용이 요구되고, 이차 이용(특히 가명·익명처리 없는 인공지능 학습)에는 가명처리나 별도 특례가 필요하며, 검출 후 가림·명세 기반 실시간 가림·촬영 시점 저해상도화·출력 필드 축소 같은 기술은 모두 인식 오류나 재식별 위험의 한계가 보고되었다. [추정][^ref-1138][^ref-588][^ref-1140][^ref-1144][^ref-1145][^ref-1146][^ref-1147][^ref-1148] 그래서 수집 범위를 목적별로 정하고 이차 이용을 통제하는 운영 규칙이 기술과 함께 필요한 것으로 보인다. [추정][^ref-588][^ref-1147]

핵심 질문의 '사람의 위치 정보' 부분(보행자 위치 최소 수집, 궤적 익명화)만을 다룬 자료는 이번 조사에서 찾지 못했다. 또 병원 내부나 세대 내부 촬영이 제25조의2의 '공개된 장소' 기준과 어떻게 맞물리는지도 확인하지 못해 열린 질문(oq-171, oq-181)으로 남아 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/security-and-privacy/privacy-and-video-data.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/security-and-privacy/privacy-and-video-data.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md)
- 관련 영역: [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [37. 관제 화면·실행 기록](../../categories/field-operations-and-monitoring/control-screen-and-execution-records.md), [43. 데이터·관측성·배포](../../categories/platform-architecture-and-infrastructure/data-observability-and-deployment.md), [45. 문서·도면·장면 이해](../../categories/ai-and-learning/document-drawing-and-scene-understanding.md), [47. AI·학습·적응과 모델 운영](../../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md), [50. 안전 표준·인증·사고 조사](../../categories/safety/safety-standards-certification-and-incident-investigation.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md), [52. 통신 보호·위협 관리·감사](../../categories/security-and-privacy/communication-protection-threat-management-and-audit.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [58. 다사업자 책임·계약·데이터](../../categories/governance-law-and-society/multi-party-responsibility-contracts-and-data.md), [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md), [60. 노동·수용성·접근성](../../categories/governance-law-and-society/labor-acceptance-and-accessibility.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/security-and-privacy/privacy-and-video-data.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-588]: 김·장 법률사무소, ‘이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서’ 공개 (뉴스레터), 2024-10-14, https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=30477, 접근일 2026-09-30
[^ref-1137]: 정보통신신문, "자율주행차·로봇 카메라 촬영 시 외부에 표시해야", 2024-10-14, https://www.koit.co.kr/news/articleView.html?idxno=125844, 접근일 2026-09-30
[^ref-1138]: 개인정보보호위원회 (개인정보 포털), 개인정보 포털 — 이동형 영상정보처리기기 제도 및 신청방법 안내, 미확인, https://www.privacy.go.kr/front/contents/cntntsView.do?contsNo=286, 접근일 2026-09-30
[^ref-1140]: 법무법인(유) 세종, 개인정보보호위원회, 비정형데이터 가명처리 관련 가명정보 처리 가이드라인 개정 (뉴스레터), 2024-02-08, https://www.shinkim.com/kor/media/newsletter/2342, 접근일 2026-09-30
[^ref-1141]: 경향신문, 로봇청소기가 우리집 사진 찍어 외부 유출?…6종 ... (제목 일부만 확인), 2025-09-02, https://www.khan.co.kr/article/202509021447001, 접근일 2026-09-30
[^ref-968]: MIT Technology Review, A Roomba recorded a woman on the toilet. How did screenshots end up on Facebook?, 2022-12-19, https://www.technologyreview.com/2022/12/19/1065306/roomba-irobot-robot-vacuums-artificial-intelligence-training-data-privacy/, 접근일 2026-09-30
[^ref-1144]: Raina, N., Somasundaram, G., Zheng, K. 외 (Meta Reality Labs, arXiv), EgoBlur: Responsible Innovation in Aria, 2023-08-24, https://arxiv.org/abs/2308.13093, 접근일 2026-09-30
[^ref-1145]: Choi, M. 외 (arXiv), Real-Time Privacy Preservation for Robot Visual Perception, 2025-05-08, https://arxiv.org/abs/2505.05519, 접근일 2026-09-30
[^ref-1146]: Huang, X., Pan, S., Reinhardt, D., & Bennewitz, M. (arXiv), Designing Privacy-Preserving Visual Perception for Robot Navigation Based on User Privacy Preferences, 2026-04-07, https://arxiv.org/abs/2604.06382, 접근일 2026-09-30
[^ref-1147]: Xu, Y., & Ayday, E. (arXiv), Seeing Less Is Not Seeing Safely: Privacy Leakage from Task-Scoped Robot Perception Exports, 2026-09-02, https://arxiv.org/abs/2609.03055, 접근일 2026-09-30
[^ref-1148]: Sarfraz, B. M., Saplacan Lindblom, D., Baselizadeh, A., & Torresen, J. (HRI Companion '26), The Privacy-Preserving Capabilities of a Service Robot in a Scenario-Based Healthcare Setting, 2026-03-16, https://doi.org/10.1145/3776734.3794481, 접근일 2026-09-30 (원문 미열람)

## 9. 검증 노트

원 페이지와 함께 실행 2026-09-30-16 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-09-30 | 2026-09-30-16 | 53. 개인정보·영상 데이터 의 "왜 중요한가" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 1144건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 320개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- 3d-scene-graph: 3차원 장면 그래프 (3D Scene Graph)
- aas-registry-and-discovery: 자산관리셸 레지스트리·디스커버리 (AAS Registry / Discovery)
- ablation-study: 절제 실험 (Ablation Study)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- agentic-ai: 에이전틱 AI (Agentic AI)
- aggregation-event: 집계 이벤트 (AggregationEvent)
- agv-technical-data-submodel: AGV 기술 데이터 서브모델 (Technical Data for AGV in Intralogistics (IDTA 02047))
- alternative-name: 대체 이름 (Alternative Name (IMDF alt_name))
- amr-assisted-order-picking: AMR 협업 피킹 (AMR-assisted Order Picking)
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
- automatic-simulation-model-generation: 자동 시뮬레이션 모델 생성 (Automatic Simulation Model Generation (ASMG))
- automation-bias: 자동화 편향 (Automation Bias)
- b2mml: B2MML (Business To Manufacturing Markup Language (B2MML))
- bag-file: 백 파일 (Bag File (rosbag2))
- battery-swapping: 배터리 교환 (Battery Swapping)
- behavior-domain-definition-language: 행동 영역 정의 언어 (Behavior Domain Definition Language (BDDL))
- behavior-tree: 행동 트리 (Behavior Tree)
- block-reference: 블록 참조 (Block Reference (INSERT))
- bpmn: 비즈니스 프로세스 모델 및 표기법 (Business Process Model and Notation (BPMN))
- brainless-robot: 브레인리스 로봇 (Brainless Robot)
- building-information-modeling: 건물 정보 모델링 (Building Information Modeling (BIM))
- building-topology-ontology: 건물 위상 온톨로지 (Building Topology Ontology (BOT))
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
- giai: 글로벌 개별 자산 식별자 (Global Individual Asset Identifier (GIAI))
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
- hungarian-method: 헝가리안 방법 (Hungarian Method)
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
- lane-closure: 차선 폐쇄 (Lane Closure)
- language-guided-floor-plan-generation: 언어 유도 평면도 생성 (Language-guided Floor Plan Generation)
- latent-failure: 잠재 실패 (Latent Failure)
- layout-interchange-format: 레이아웃 교환 형식 (Layout Interchange Format (LIF))
- level-alignment-fiducial: 층 정렬 기준점 (Fiducial (Level Alignment Fiducial))
- lifelong-mapf: 지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF))
- lift-adapter: 승강기 어댑터 (Lift Adapter)
- linear-temporal-logic: 선형 시간 논리 (Linear Temporal Logic (LTL))
- littles-law: 리틀의 법칙 (Little's Law)
- llm-agent: LLM 에이전트 (LLM Agent)
- llm-modulo-framework: LLM-모듈로 프레임워크 (LLM-Modulo Framework)
- location-check-digit: 위치 체크 디지트 (Location Check Digit)
- lockout-tagout: 잠금·표지 (Lockout/Tagout (LOTO))
- log-playback: 로그 재생 (Log Playback)
- managed-node: 관리형 노드 (Managed Node (ROS 2 Lifecycle Node))
- map-alignment: 지도 정합 (Map Alignment)
- map-version: 지도 버전 (Map Version (VDA 5050 mapId / mapVersion))
- mapf: 다중 에이전트 경로 찾기 (Multi-Agent Path Finding (MAPF))
- maps-of-dynamics: 움직임 지도 (Maps of Dynamics (MoD))
- market-based-task-allocation: 시장 기반 작업 배정 (Market-based Task Allocation)
- matter: 매터 (Matter (Connectivity Standards Alliance smart home standard))
- mcap: MCAP (MCAP)
- milp: 혼합 정수 계획 (Mixed Integer Linear Programming (MILP))
- mission-specification-pattern: 미션 명세 패턴 (Mission Specification Pattern)
- mobile-manipulator: 모바일 매니퓰레이터 (Mobile Manipulator)
- mobile-video-information-processing-device: 이동형 영상정보처리기기 (Mobile Video Information Processing Device)
- model-checking: 모델 검사 (Model Checking)
- model-context-protocol: 모델 컨텍스트 프로토콜 (Model Context Protocol (MCP))
- model-registry: 모델 레지스트리 (Model Registry)
- model-substitution-and-routing-dilution: 모델 대체·라우팅 희석 (Model Substitution / Routing Dilution)
- models-and-simulations-credibility-assessment: 모델·시뮬레이션 신뢰도 평가 (Models and Simulations Credibility Assessment (NASA-STD-7009))
- mqtt: 메시지 큐잉 원격 측정 전송 (Message Queuing Telemetry Transport (MQTT))
- mrta: 다중 로봇 작업 배정 (Multi-Robot Task Allocation (MRTA))
- multi-agent-pickup-and-delivery: 다중 에이전트 픽업·배송 (Multi-Agent Pickup and Delivery (MAPD))
- multi-fleet-orchestration: 다중 플릿 오케스트레이션 (Multi-Fleet Orchestration)
- multi-trip-vehicle-routing-problem: 다중 운행 차량 경로 문제 (Multi-Trip Vehicle Routing Problem (MTVRP))
- nearest-vehicle-first-rule: 최근접 차량 우선 규칙 (Nearest Vehicle First (NVF) Rule)
- neuro-symbolic-ai: 신경-기호 AI (Neuro-symbolic AI)
- number-of-clicks: 클릭 수 지표 (Number of Clicks (NoC))
- observability: 관측성 (Observability)
- occupancy-grid-map: 점유 격자 지도 (Occupancy Grid Map (OGM))
- ocel: 객체 중심 이벤트 로그 (Object-Centric Event Log (OCEL))
- ontology-evolution: 온톨로지 진화 (Ontology Evolution)
- ontology-pitfall: 온톨로지 피트폴 (Ontology Pitfall)
- ontology-population: 온톨로지 채우기 (Ontology Population)
- open-rmf: 오픈 RMF (Open-RMF (Open Robotics Middleware Framework))
- openapi-specification: OpenAPI 명세 (OpenAPI Specification (OAS))
- opentelemetry: 오픈텔레메트리 (OpenTelemetry (OTel))
- operating-mode: 운용 모드 (Operating Mode (VDA 5050 operatingMode))
- operating-zone: 운용 구역 (Operating Zone (ISO 3691-4))
- optimality-gap: 최적성 간격 (Optimality Gap)
- order-batching: 주문 배치 (Order Batching)
- outdoor-mobile-robot-operational-safety-certification: 실외이동로봇 운행안전인증 (Outdoor Mobile Robot Operational Safety Certification)
- over-the-air-update: 무선 업데이트 (Over-the-Air Update (OTA))
- overall-equipment-effectiveness: 종합설비효율 (Overall Equipment Effectiveness (OEE))
- panoptic-quality: 파놉틱 품질 (Panoptic Quality (PQ))
- panoptic-symbol-spotting: 파놉틱 심볼 스포팅 (Panoptic Symbol Spotting)
- pass-k: pass^k 지표 (pass^k)
- pddl: 계획 도메인 정의 언어 (Planning Domain Definition Language (PDDL))
- perfect-order-fulfillment: 완전 주문 이행률 (Perfect Order Fulfillment)
- performable-action: 수행 가능 동작 (Performable Action (Open-RMF perform_action))
- personal-delivery-device: 개인 배송 장치 (Personal Delivery Device (PDD))
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- post-encroachment-time: 침범 후 시간 (Post-Encroachment Time (PET))
- power-and-force-limiting: 동력·힘 제한 (Power and Force Limiting (PFL))
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
- precedence-constraint: 선후 제약 (Precedence Constraint)
- predictive-maintenance: 예지 정비 (Predictive Maintenance)
- presumption-of-conformity: 적합성 추정 (Presumption of Conformity)
- priority-inheritance-with-backtracking: 우선순위 상속·되돌림 (Priority Inheritance with Backtracking (PIBT))
- private-5g-network: 5G 특화망(이음5G) (Private 5G Network (e-Um 5G))
- process-mining: 프로세스 마이닝 (Process Mining)
- prompt-injection: 프롬프트 주입 (Prompt Injection)
- protective-separation-distance: 보호 분리 거리 (Protective Separation Distance)
- public-area-mobile-robot: 공공 영역 이동로봇 (Public-area Mobile Robot (PMR))
- put-wall: 풋월 (Put Wall)
- raster-to-vector-conversion: 래스터–벡터 변환 (Raster-to-Vector Conversion)
- read-point: 판독 지점 (Read Point (EPCIS readPoint))
- reality-gap: 현실 격차 (Reality Gap (Sim-to-Real Gap))
- regression-testing: 회귀 시험 (Regression Testing)
- release-zone: 해제 구역 (Release Zone)
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
- role-based-access-control: 역할 기반 접근 통제 (Role-Based Access Control (RBAC))
- root-cause-analysis-rca: 근본 원인 분석 (Root Cause Analysis (RCA))
- runtime-verification: 런타임 검증 (Runtime Verification)
- safe-interval-path-planning: 안전 구간 경로 계획 (Safe Interval Path Planning (SIPP))
- saga: 사가 (Saga)
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
- slot-filling: 슬롯 채우기 (Slot Filling)
- smart-hospital-leading-model: 스마트병원 선도모델 (Smart Hospital Leading Model)
- smart-logistics-center-certification: 스마트물류센터 인증 (Smart Logistics Center Certification)
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
- stpa: 시스템 이론적 프로세스 분석 (System-Theoretic Process Analysis (STPA))
- stride-threat-classification: STRIDE 위협 분류 (STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege))
- structured-output: 구조화 출력 (Structured Output)
- success-weighted-by-path-length: 경로 길이 가중 성공률 (Success weighted by Path Length (SPL))
- supervisory-control: 감독 제어 (Supervisory Control)
- table-structure-recognition: 표 구조 인식 (Table Structure Recognition)
- tamper-evident-log: 변조 탐지 로그 (Tamper-evident Log)
- task-decomposition: 작업 분해 (Task Decomposition)
- technology-readiness-level: 기술 성숙도 (Technology Readiness Level (TRL))
- teleoperation: 원격 조작 (Teleoperation)
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- traversability: 통과 가능성 (Traversability)
- uncertainty-alignment: 불확실도 정렬 (Uncertainty Alignment)
- underspecification: 과소명세 (Underspecification)
- urdf: 통합 로봇 기술 형식 (Unified Robot Description Format (URDF))
- use-case-template: 사용 사례 템플릿 (Use Case Template (IEC 62559-2))
- user-simulator: 사용자 시뮬레이터 (User Simulator)
- vda-5050-cancel-order: 주문 취소 즉시 동작 (cancelOrder (VDA 5050 instant action))
- vda-5050-factsheet: VDA 5050 팩트시트 (VDA 5050 factsheet)
- vda-5050: VDA 5050 (VDA 5050)
- verification-and-validation-of-simulation-models: 시뮬레이션 모델 검증·타당성 확인 (Verification and Validation (V&V) of Simulation Models)
- version-iri: 버전 IRI (Version IRI (owl:versionIRI))
- virtual-commissioning: 가상 시운전 (Virtual Commissioning)
- vision-language-action-model: 비전 언어 행동 모델 (Vision-Language-Action Model (VLA))
- voice-picking: 음성 피킹 (Voice-Directed Picking (Voice Picking))
- waveless-order-release: 웨이브리스 출고 지시 (Waveless Order Release)
- webhook: 웹훅 (Webhook)
- wes-wcs-wms-mes-tms: 창고 실행·창고 제어·창고 관리·제조 실행·운송 관리 시스템 (Warehouse Execution System / Warehouse Control System / Warehouse Management System / Manufacturing Execution System / Transportation Management System)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [53] 에 걸린 7건 / 전체 258건)

```markdown
- oq-143 [열림] ROP 의 로봇 대화 기능이 국내 인공지능 기본법의 고영향 인공지능이나 EU AI Act 의 고위험 AI 시스템에 해당하는지, 해당한다면 대화 기록 자동 로그의 항목과 보존 기간을 어떻게 정해야 하는가? (영역 13, 59, 53)
- oq-171 [열림] 개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한)의 촬영 사실 표시·촬영 거부 규정이 병원 이송 로봇의 카메라·센서 촬영에 어떻게 적용되며, 환자·방문객 영상을 관제 계층이 어디까지 저장·전송할 수 있는지 법령 원문과 해석 사례로 확인할 수 있는가(이번 조사는 법령 원문을 열지 못했다)? (영역 63, 53)
- oq-181 [열림] 세대 안에서 거주자가 쓰는 가사 로봇·로봇청소기의 영상 수집에는 개인정보 보호법 제25조의2(이동형 영상정보처리기기)가 적용되는가, 아니면 동의 기반 처리 조항만 적용되는가, 그리고 이에 대한 개인정보보호위원회 해석이나 가이드라인이 있는가? (영역 65, 53)
- oq-185 [열림] 소유자가 원격 조작자를 예약해 가정 로봇을 안내하게 하는 방식(1X NEO 등)에서 원격 조작자의 영상 접근·사고 책임을 다루는 국내외 규제·인증 기준이 있는가? (영역 65, 53, 58)
- oq-211 [열림] 로봇 플랫폼이 수집하는 텔레메트리·주행 기록·영상의 보존 기간을 정한 국내 기준이나 운영 사례가 개인정보 접속기록 규정 밖에도 있는가? (영역 43, 53)
- oq-214 [열림] 로봇 플랫폼에 적용될 수 있는 현행 「개인정보의 안전성 확보조치 기준」(2023-6호 이후 개정판)의 접속기록 보관 기간·점검 주기 조항이 2023-6호와 같은가? (영역 43, 53)
- oq-228 [열림] 플랫폼이 시설 CCTV 영상을 로봇 운영용 장면 인식에 쓸 때 국내 개인정보 보호 법령의 고정형 영상정보처리기기 규정상 목적 외 이용이나 안내 의무가 문제 되는가? (영역 45, 53)
```

### runs/2026-09-30-16/verification2.json

```json
{
  "run_id": "2026-09-30-16",
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
      "11절(분리 페이지 docs/topics/2026/2026-09-30-area53-s11.md)의 기존 열린 질문 oq-171·oq-181·oq-185·oq-228 문장이 docs/open-questions.md 등록 문장과 다르다. 이번 실행은 이 질문들을 갱신하지 않으므로(open_question_updates 에 없음) 페이지 문장과 등록 문장이 어긋난다."
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
    "8절(원 페이지 8절 원문, 분리 페이지 2026-09-30-area53-s8.md): Xu·Ayday 항목의 '플랫폼이 로봇에서 받는 데이터의 필드 설계와 직접 이어진다'를 [사실] 문장에서 떼어 별도 문장으로 두고 [추정][^ref-1147]로 표시한다. 이유: f16 에서 [사실]로 남는 것은 인지 출력 3종을 비교한 결과뿐이다. 플랫폼 필드 설계와의 연결은 f21([추정])의 해석이므로 [사실]로 쓰면 태그가 올라간다.",
    "11절(원 페이지 11절 원문, 분리 페이지 2026-09-30-area53-s11.md): 기존 열린 질문 7건의 질문 문장을 docs/open-questions.md 등록 문장 그대로 옮긴다. 현재 oq-171 은 '법령 원문과 해석 사례로 확인할 수 있는가(이번 조사는 법령 원문을 열지 못했다)'가 바뀌었고, oq-181 은 '그리고 이에 대한 개인정보보호위원회 해석이나 가이드라인이 있는가'가 빠졌으며, oq-185 는 '(1X NEO 등)'이, oq-228 은 '국내 개인정보 보호 법령의'가 빠졌다. 이번 실행의 메모는 질문 문장 뒤에 별도 문장으로 둔다. 이유: 이번 실행은 이 질문들을 갱신하지 않으므로 등록 문장과 페이지 문장이 같아야 한다.",
    "11절: oq-181 뒤 메모 '2026-09 로봇청소기 점검이 동의와 계약 이행 처리의 구분을 점검한 것은 부분 근거'에 [추정][^ref-1142]를, oq-228 뒤 메모 '이동형 기기 안내서의 사고 영상·인공지능 학습 판단은 부분 근거'에 [추정][^ref-588]을 붙이고, 13절(분리 페이지 8. 출처)에 두 각주 정의를 둔다. 이유: 출처가 있는 사실(f11, f5·f6)을 근거로 든 판단 문장인데 태그와 각주가 없다.",
    "7절·10절·11절(각 분리 페이지): 약어를 각 페이지에서 처음 쓸 때 풀어 쓴다. EDPB 는 '유럽데이터보호이사회(European Data Protection Board, EDPB)'로(f18 의 표기), 7절의 GDPR 은 '일반 개인정보 보호법(General Data Protection Regulation, GDPR)'으로 쓴다. 3절(분리 페이지 2026-09-30-area53-s3.md)의 SNS 는 '소셜 네트워크 서비스(SNS)'로 쓴다. 이유: 공통 표기 규약상 약어는 첫 등장 시 풀어 쓴다."
  ],
  "confidence": "medium",
  "verification_note": "판정: 조건부 승인 / 2차 수정 후 재검증. 확인 21건, 미확인 2건(f2·f18 부분 뒷받침), 교차 확인 4건(f2·f3·f6·f11). 강등: f2 의 '목욕실 등 촬영 금지' 구절 사실 → 추정(인용 출처에 없음, 본문에 법령 원문 미확인 표시), f18 의 지침 다루는 범위 구절 사실 → 추정(원문 미확인, 본문에서 삭제). 원문 미열람 출처: ref-1148(ACM 403, 검색 결과로 서지 확인). 주의: 안내서(2024.9.)와 가명정보 처리 가이드라인의 세부 내용은 원문 PDF가 아니라 법률사무소 뉴스레터와 기사의 2차 요약에 근거한다. 기술 연구(f13~f16)는 프리프린트 초록 기준이다. 그중 f16 은 시뮬레이션 결과이고, f17 은 모의 진료실 실험이다. 로봇청소기 점검 사례(f10·f11)는 기사 근거다. 사람의 위치 정보를 최소로 모으거나 궤적을 익명화하는 데 관한 전용 자료는 찾지 못했다. 물류창고·제조 공장·상업 시설·기타 현장 사례는 없다. 이 영역의 기존 열린 질문 7건(oq-143·oq-171·oq-181·oq-185·oq-211·oq-214·oq-228)은 해결 제안 없이 열림으로 유지한다. 정정 요청은 없다. 2차 검증 결과: 1차 수정 지시 15건은 모두 이행됐다(f2 구절 분리·강등, f21 예시 일반화, f5·f16·f11·f8·f1 문구 정정, f18 범위 구절 삭제, ref-588·ref-1140·ref-1148·ref-1137 서지 정정, 6·9절 범위 경계, 용어집 실증특례 정의, 5절 현장 유형 세 가지와 site_matrix_updates 일치). 드리프트는 없다. 다만 8절 분리 페이지에서 해석 문장 1건에 태그가 [사실]로 올라가 있고, 11절에서 기존 열린 질문 문장이 등록 문장과 다르며 근거 메모 2건에 태그·각주가 없다. 약어 풀어쓰기도 빠졌다. [분류원문]은 보존됐고, 섹션 순서와 링크는 형식 검증 코드 기준으로 준수·유효하다. 자동 분리된 주제 페이지 7건은 원 절 내용을 그대로 옮겼다. 참고(스토리텔러 수정 대상 아님): 자동 분리 뒤 원 페이지 프런트매터 sources 에는 본문에서 더 인용하지 않는 ref-1140·ref-1145·ref-1146·ref-1149 가 남아 있다. reference_updates 의 cited_by 도 원 페이지만 가리키므로 분리 페이지 인용 반영은 퍼블리셔 자동 영역에 맡긴다. 9절의 '이 경계는 제품 전략에 따라 이동할 수 있다'는 원문 19장 문장이지만 링크가 붙어 [분류원문] 태그 없이 쓰였다. standards_updates 의 가명정보 처리 가이드라인 URL 은 발행 기관이 아닌 법률사무소 뉴스레터다. 2차 검증에서는 도구를 쓰지 않았다.",
  "retry_reason": null
}
```
