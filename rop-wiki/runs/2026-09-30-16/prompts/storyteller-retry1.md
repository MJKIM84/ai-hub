(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/storyteller.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

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

### docs/categories/security-and-privacy/index.md

```markdown
---
title: "N. 보안·개인정보"
type: category
status: seed
created: 2026-09-28
updated: 2026-09-28
version: 1
---

[홈](../../index.md) › N. 보안·개인정보

# N. 보안·개인정보

## 핵심 질문

누가 어떤 로봇에 무엇을 시킬 수 있는지 통제하고, 데이터와 사람의 정보를 어떻게 지킬 것인가? [분류원문]

## 개요

인증·권한·격리, 통신 보호, 위협 관리와 감사 기록, 문서·대화 입력 보안, 개인정보·영상 데이터 보호. [분류원문]

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **51. 인증·권한·격리** | 장비·사용자 인증, 명령 권한, 원격 접속 계정, 고객·현장 격리 | 외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가? | [51. 인증·권한·격리](authentication-authorization-and-isolation.md) | published |
| **52. 통신 보호·위협 관리·감사** | 통신 보호, 위협 모델·취약점, 문서·대화 입력 보안, 감사 기록 | 통신·문서·대화를 통한 공격이 로봇 동작으로 이어지지 않게 하려면? | [52. 통신 보호·위협 관리·감사](communication-protection-threat-management-and-audit.md) | published |
| **53. 개인정보·영상 데이터** | 영상·작업자·거주자 데이터 보호, 최소 수집·익명화 | 로봇이 찍은 영상과 사람의 위치 정보를 어디까지 모으고 어떻게 지킬 것인가? | [53. 개인정보·영상 데이터](privacy-and-video-data.md) | seed |

[분류원문]
<!-- auto:category-area-table:end -->

## 이 대분류의 핵심 포인트

ROS 2도 인증·암호화·접근권한과 보안 위협 모델을 별도로 다룬다. 기능 연동과 보안 연동은 함께 설계해야 하는 영역이다. [9][10] [분류원문]

## 다른 대분류와의 연결

아직 작성되지 않음(에이전트가 채운다).

## 이 대분류의 자료

<!-- auto:category-sources:start -->
이 대분류의 페이지가 인용했거나 이 대분류 영역과 연결된 출처는 모두 31건이다(논문 8건 · 기사·보고서 6건 · 업체 발표 0건 · 표준·오픈소스·기관 자료 17건). 유형은 참고문헌의 출처 유형을 따르며, 업체 발표는 '벤더 문서' 유형이다. 묶음마다 발행일이 최근인 것부터 10건까지 보이고, 전체 목록은 [참고문헌](../../references/index.md)에 있다.

**논문**

- [ref-1112](../../references/ref-1112.md) — Nagaraja, N., Bagari, A., & Bahsi, H. (arXiv), When Prompts Control Robots: Prompt Injection Attacks in Multi-Agent Robotic Systems (발행 2026-08)
- [ref-585](../../references/ref-585.md) — Jaatun 외(Journal of Cybersecurity and Privacy 6(2), 52), Security Aspects of Zones and Conduits in IEC 62443 (발행 2026)
- [ref-1108](../../references/ref-1108.md) — Mayoral-Vilches, V. (Alias Robotics, arXiv), The Cybersecurity of a Humanoid Robot (발행 2025-09-17)
- [ref-700](../../references/ref-700.md) — Ravichandran, Z., Robey, A., Kumar, V., Pappas, G. J., & Hassani, H.(IEEE RA-L 2026 채택 표기), Safety Guardrails for LLM-Enabled Robots (발행 2025-03)
- [ref-857](../../references/ref-857.md) — Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J., Jailbreaking LLM-Controlled Robots (발행 2024-11-09)
- [ref-1113](../../references/ref-1113.md) — Zhang, W., Kong, X., Dewitt, C., Braunl, T., & Hong, J. B. (arXiv), A Study on Prompt Injection Attack Against LLM-Integrated Mobile Robotic Systems (발행 2024-08)
- [ref-1110](../../references/ref-1110.md) — Fernández-Becerra, L., González-Santamarta, M. Á., Guerrero-Higueras, Á. M., Rodríguez-Lera, F. J., & Matellán Olivera, V. (arXiv), Enhancing Trust in Autonomous Agents: An Architecture for Accountability and Explainability through Blockchain and Large Language Models (발행 2024-03)
- [ref-1114](../../references/ref-1114.md) — Quarta, D., Pogliani, M., Polino, M., Maggi, F., Zanchettin, A. M., & Zanero, S. (IEEE S&P 2017), An Experimental Security Analysis of an Industrial Robot Controller (발행 2017)

**기사·보고서**

- [ref-1109](../../references/ref-1109.md) — IES (Integrated Equipment Services), Machinery Regulation Guide (발행 2026-08-27)
- [ref-1111](../../references/ref-1111.md) — 엠에스투데이, 선박·위성·로봇까지 해킹 표적…정부, ‘피지컬 AI’ 산업 보안 기준 제시 (발행 2026-03-06)
- [ref-969](../../references/ref-969.md) — 바이라인네트워크, '로봇청소기' 다수 제품 보안 취약…대응방안은? (발행 2025-10-31)
- [ref-588](../../references/ref-588.md) — 김·장 법률사무소, '이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서' 관련 인사이트 (발행 미확인)
- [ref-471](../../references/ref-471.md) — A3(Association for Advancing Automation), Updated ISO 10218 \| Answers to Frequently Asked Questions (FAQs) (발행 미확인)
- [ref-1106](../../references/ref-1106.md) — OWASP GenAI Security Project, LLM01:2025 Prompt Injection (발행 미확인)

**업체 발표**

- 아직 없음

**표준·오픈소스·기관 자료**

- [ref-582](../../references/ref-582.md) — NIST, NIST SP 800-82 Rev. 3, Guide to Operational Technology (OT) Security (발행 2023-09)
- [ref-555](../../references/ref-555.md) — European Union (EUR-Lex), Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery (발행 2023-06)
- [ref-1107](../../references/ref-1107.md) — CISA (미국 사이버보안·기반시설보안청), Aethon TUG Home Base Server (ICSA-22-102-05) (발행 2022-04-12)
- [ref-580](../../references/ref-580.md) — Open Robotics (ROS 2 Design), ROS 2 Security Enclaves (발행 2020-05)
- [ref-579](../../references/ref-579.md) — Open Robotics (ROS 2 Design), ROS 2 Access Control Policies (발행 2019-08)
- [ref-584](../../references/ref-584.md) — CSA / IEC (ANSI Webstore), CAN/CSA IEC 62443-3-3-2017 - Industrial communication networks - Network and system security - Part 3-3: System security requirements and security levels (Adopted IEC 62443-3-3:2013, first edition, 2013-08) (발행 2013-08)
- [ref-591](../../references/ref-591.md) — European Commission (Shaping Europe's digital future), The Cyber Resilience Act - Summary of the legislative text (발행 미확인)
- [ref-590](../../references/ref-590.md) — 한국인터넷진흥원(KISA), 로봇 보안취약점 점검 체크리스트 해설서 (발행 미확인)
- [ref-589](../../references/ref-589.md) — 법제처 국가법령정보센터, 근로자참여 및 협력증진에 관한 법률 (발행 미확인)
- [ref-587](../../references/ref-587.md) — 법제처 국가법령정보센터, 개인정보 보호법 (발행 미확인)
- 그 밖에 7건
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
- 2026-09-30 · 갱신 · [52. 통신 보호·위협 관리·감사](communication-protection-threat-management-and-audit.md) — seed → draft: 3~11절 첫 작성(통신 인증·암호화, 위협 모델·IEC 62443, LLM 탈옥·프롬프트 주입 방어, 변조 탐지 감사 기록, 병원·가정·제조 공장 적용 사례, 책임 경계, 연결 19개 영역, 열린 질문), 13절 각주 17건. 2차 수정 6건 반영(5·8절 요약 태그, 6절 도식 안내 문장 분리·일반화 문장 한정, 3절 EU 규정 범위, 연계 대상 해석 태그 분리) (실행 2026-09-30-11)
- 2026-09-30 · 생성 · [52. 통신 보호·위협 관리·감사 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area52-s6.md) — 자동 분리: 52. 통신 보호·위협 관리·감사 의 "6. 대표 접근법과 기술" 절(2,109자)을 옮겼다 (실행 2026-09-30-11)
- 2026-09-30 · 생성 · [52. 통신 보호·위협 관리·감사 — 대표 연구와 자료](../../topics/2026/2026-09-30-area52-s8.md) — 자동 분리: 52. 통신 보호·위협 관리·감사 의 "8. 대표 연구와 자료" 절(1,206자)을 옮겼다 (실행 2026-09-30-11)
- 2026-09-30 · 생성 · [52. 통신 보호·위협 관리·감사 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area52-s10.md) — 자동 분리: 52. 통신 보호·위협 관리·감사 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,102자)을 옮겼다 (실행 2026-09-30-11)
- 2026-09-30 · 생성 · [52. 통신 보호·위협 관리·감사 — 왜 중요한가](../../topics/2026/2026-09-30-area52-s3.md) — 자동 분리: 52. 통신 보호·위협 관리·감사 의 "3. 왜 중요한가" 절(1,079자)을 옮겼다 (실행 2026-09-30-11)
<!-- auto:category-recent:end -->

## 참고 자료

원문의 [9]는 참고문헌 [ref-009](../../references/ref-009.md)에 해당한다.[^ref-009] 원문의 [10]은 참고문헌 [ref-010](../../references/ref-010.md)에 해당한다.[^ref-010]

[^ref-009]: ROS 2 Design, ROS 2 DDS-Security Integration, 미확인, https://design.ros2.org/articles/ros2_dds_security.html, 접근일 2026-09-28
[^ref-010]: ROS 2 Design, ROS 2 Robotic Systems Threat Model, 미확인, https://design.ros2.org/articles/ros2_threat_model.html, 접근일 2026-09-28
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

### templates/category.md

```markdown
---
title: "{{category}}"                       # 원문 명칭 그대로. 예: "B. 로봇 온톨로지"
type: category
category: "{{category}}"                    # title 과 같은 값
tags: [{{tags}}]                            # 선택. 없으면 []
status: {{status}}                          # seed | published. 시드 대분류 페이지는 seed 이며, "다른 대분류와의 연결"이 채워져 게시되면 published 로 바꾼다 [가정]
created: {{created}}                        # YYYY-MM-DD
updated: {{updated}}                        # YYYY-MM-DD
sources: [{{sources}}]                      # 원문 주석의 [n] 에 대응하는 참고문헌 id. 예: [ref-003]
version: {{version}}                        # 정수
---
<!--
[템플릿] 대분류 페이지 (type: category)
경로: docs/categories/<대분류 slug>/index.md
쓰임: 구축 시 원문 부분(핵심 질문·개요·세부 연구영역·이 대분류의 핵심 포인트)을 채워 만든다. "다른 대분류와의 연결"은 에이전트(스토리텔러)가 관련 영역을 다루는 실행에서 채우고, "세부 연구영역" 표(페이지·현재 상태 열 포함)와 "이 대분류의 자료"(논문·기사·업체 발표·표준 묶음별 출처 목록, 2026-09-28 추가), "최근 업데이트"는 퍼블리셔가 자동 갱신한다.
일곱 섹션(4.3 + 2026-09-28 추가): 핵심 질문 / 개요 / 세부 연구영역 / 이 대분류의 핵심 포인트 / 다른 대분류와의 연결 / 이 대분류의 자료 / 최근 업데이트. 제목·순서 고정. H2 문자열은 사양서 4.3 문구 그대로이며 번호를 붙이지 않는다(pipeline/checks/protect_source.py 의 CATEGORY_SECTIONS 와 글자 단위로 같다. "1. 핵심 질문"처럼 번호를 붙이면 "섹션 제목·순서 불일치"로 반려된다). 각주 정의를 둘 자리로 번호 없는 "참고 자료" 절을 여섯 섹션 뒤에 하나 더 두었다. 이 절은 사양서 4.3 의 여섯 섹션에 없는 구축자 추가 절이다 [가정].

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

[경로 규약] 이 페이지에서 홈은 ../../index.md, 같은 대분류의 세부영역은 <파일>.md, 다른 대분류는 ../<대분류 slug>/index.md 이다.
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
[홈](../../index.md) › {{category}}

# {{category}}

## 핵심 질문

{{core_question}} [분류원문]
<!-- 분류 원문 1장 표의 "핵심 질문" 칸 문장 그대로. 예: "서로 다른 제조사의 로봇을 어떻게 등록하고, 할 수 있는 일을 같은 말로 표현해, 시스템과 쉽게 연결할 것인가? [분류원문]". 수정 금지. -->

## 개요

{{overview_paragraph}} [분류원문]
<!-- 분류 원문에서 이 대분류 장의 첫 문단(표 위의 문단)을 굵게 표기까지 그대로 옮긴다. 예: "서로 다른 제조사의 로봇을 등록하고, 무엇을 할 수 있는지 공통 모델로 표현하고, 그 모델로 시스템과 로봇이 쉽게 연동되게 하는 온톨로지 기능 전체. [분류원문]". 굵은 표기가 있으면 그대로 두고, 명사형으로 끝나는 문단도 고치지 않는다. -->

## 세부 연구영역

표의 세부 연구영역·무엇을 연구하는가·핵심 질문 열은 원문 그대로이고, 페이지·현재 상태 열은 위키에서 덧붙인 것이다. 현재 상태는 퍼블리셔가 자동으로 갱신한다.

<!-- auto:category-area-table:start -->
| 세부 연구영역 | 무엇을 연구하는가 | 핵심 질문 | 페이지 | 현재 상태 |
|---|---|---|---|---|
| **{{area_no}}. {{area_name}}** | {{what_to_research}} | {{area_question}} | [{{area_no}}. {{area_name}}]({{area_file}}.md) | {{area_status}} |
| **{{area_no}}. {{area_name}}** | {{what_to_research}} | {{area_question}} | [{{area_no}}. {{area_name}}]({{area_file}}.md) | {{area_status}} |
| **{{area_no}}. {{area_name}}** | {{what_to_research}} | {{area_question}} | [{{area_no}}. {{area_name}}]({{area_file}}.md) | {{area_status}} |
| **{{area_no}}. {{area_name}}** | {{what_to_research}} | {{area_question}} | [{{area_no}}. {{area_name}}]({{area_file}}.md) | {{area_status}} |

[분류원문]
<!-- auto:category-area-table:end -->
<!--
원문 표의 행(대분류마다 3~7행)을 모두 그대로 옮기고(앞 3열은 원문 셀과 글자 단위로 같게, 첫 열의 굵은 표기 유지, 첫 열에 링크를 씌우지 않음), "페이지" 열에 세부영역 페이지 링크, "현재 상태" 열에 해당 페이지 프런트매터 status(seed | draft | verified | published | needs_update | deprecated)를 둔다(4.3 의 "링크와 현재 상태 열만 추가"). 표 바로 아래 빈 줄 다음에 [분류원문] 한 줄을 둔다. 퍼블리셔(pipeline/checks/protect_source.py check_category)가 각 행의 앞 3칸과 [분류원문] 줄을 원문과 대조한다.
표 전체는 auto:category-area-table 마커 안에 있고 퍼블리셔(pipeline/lib/render.py render_category_area_table)가 원문 파서와 세부영역 페이지의 status 로 다시 쓴다. 스토리텔러는 마커 사이를 건드리지 않는다. 마커 위의 안내 문장은 마커 밖이므로 그대로 둔다. 이 key 는 사양서에 없는 구축자 추가 key 이며, 시드 대분류 페이지·agents/shared-rules.md 6절의 auto key 목록·퍼블리셔(pipeline/lib/autoregion.py AUTO_KEYS)가 같은 값을 쓴다 [가정 — 사용자 결정 항목: 표 전체를 자동 영역으로 둘지, 표는 마커 밖에 두고 현재 상태 열만 갱신할지].
-->

## 이 대분류의 핵심 포인트

{{key_point_paragraphs}}
<!--
분류 원문에서 이 대분류 장의 표 아래 설명 문단들을 순서대로 모두 옮긴다. 문단마다 끝에 " [분류원문]" 을 붙이고, 그 줄에는 태그 뒤에 아무것도(각주 포함) 붙이지 않는다. 원문의 [n] 번호 표기는 문장 안에 그대로 둔다. 예: "... 참고 표준이다. [3] [분류원문]". 대응 각주 [^ref-00n] 은 이 절이 아니라 "참고 자료" 절의 별도 문장에 둔다. 굵게·기울임 표기를 유지한다. 에이전트는 이 절의 원문 문장을 고치지 않고, 원문 문단 뒤에 자기 문장을 덧붙이지도 않는다.
퍼블리셔(pipeline/checks/protect_source.py check_category)는 이 절에서 " [분류원문]" 으로 끝나는 줄만 모아 원문 문단 목록과 글자 단위로 대조한다. 태그 뒤에 각주를 붙이면 그 줄이 빠져 "핵심 포인트 문단 불일치"로 반려된다.
-->

## 다른 대분류와의 연결

{{category_connections}}
<!--
에이전트가 채운다. 목록 형식: "- [F. 연동](../integration/index.md) — 이 대분류의 어떤 영역이 저 대분류의 어떤 영역과 왜 이어지는지 한두 문장(세부영역은 번호와 이름 함께)". 주장에는 태그·각주. 구축 시에는 "아직 작성되지 않음"으로 둔다.
M. 안전, N. 보안·개인정보, P. 거버넌스·법규·사회처럼 여러 대분류에 걸쳐 적용되는 대분류는 그 적용 관계를 드러낸다. Q. 현장 유형별 적용은 현장마다 다른 요구를 모으고 모든 현장에 공통인 기능은 A~P에 둔다는 원문 취지를 지킨다. L. AI·학습 기술의 교차 규칙(매뉴얼 해석은 4. 이기종 로봇 등록과 55. 현장 조사·설치·시운전, 도면 해석은 14. 도면·BIM에서 지도 만들기, 학습 기반 배정은 25. 작업 배정 — MRTA, 장애 분석은 38. 모니터링·이상 탐지·원인 분석)과 C. 채팅 기반 구성·운영의 엔진 짝(맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번)을 여기서도 지킨다.
-->

## 이 대분류의 자료

<!-- auto:category-sources:start -->
(퍼블리셔가 자동 생성: 이 대분류 페이지·소속 세부영역·주제 페이지가 인용한 출처를 논문 / 기사·보고서 / 업체 발표(벤더 문서) / 표준·오픈소스·기관 자료로 묶어 최근 발행순으로 보인다)
<!-- auto:category-sources:end -->

## 최근 업데이트

<!-- auto:category-recent:start -->
퍼블리셔가 자동으로 채운다.
<!-- auto:category-recent:end -->
<!-- 퍼블리셔가 이 대분류에 속한 세부영역·주제 페이지의 최근 변경을 최신순으로 넣는다(날짜 | 실행 id | 페이지 | 변경 요약). 마커 사이는 스토리텔러가 건드리지 않는다. -->

## 참고 자료

{{source_footnote_sentences}}

{{footnotes}}
<!-- "이 대분류의 핵심 포인트" 원문 문단의 [n] 에 대응하는 각주를 별도 문장으로 두고(예: "원문의 [3]은 참고문헌 [ref-003](../../references/ref-003.md)에 해당한다.[^ref-003]"), 그 아래에 각주 정의를 둔다. 형식: "[^ref-003]: 기관, 제목, 발행일, URL, 접근일 YYYY-MM-DD". "다른 대분류와의 연결"에서 쓴 각주도 여기에 둔다. 각주가 없으면 "없음". 이 절은 사양서 4.3 의 여섯 섹션 밖의 보조 절로, 5.3 의 각주 정의 자리를 위해 구축자가 추가했으며 번호를 붙이지 않는다 [가정]. -->
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 0건 / 전체 1134건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
```

### docs/glossary/index.md (요약: 용어 316개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

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

### docs/open-questions.md (요약: 대상 영역 [53] 에 걸린 7건 / 전체 254건)

```markdown
- oq-143 [열림] ROP 의 로봇 대화 기능이 국내 인공지능 기본법의 고영향 인공지능이나 EU AI Act 의 고위험 AI 시스템에 해당하는지, 해당한다면 대화 기록 자동 로그의 항목과 보존 기간을 어떻게 정해야 하는가? (영역 13, 59, 53)
- oq-171 [열림] 개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한)의 촬영 사실 표시·촬영 거부 규정이 병원 이송 로봇의 카메라·센서 촬영에 어떻게 적용되며, 환자·방문객 영상을 관제 계층이 어디까지 저장·전송할 수 있는지 법령 원문과 해석 사례로 확인할 수 있는가(이번 조사는 법령 원문을 열지 못했다)? (영역 63, 53)
- oq-181 [열림] 세대 안에서 거주자가 쓰는 가사 로봇·로봇청소기의 영상 수집에는 개인정보 보호법 제25조의2(이동형 영상정보처리기기)가 적용되는가, 아니면 동의 기반 처리 조항만 적용되는가, 그리고 이에 대한 개인정보보호위원회 해석이나 가이드라인이 있는가? (영역 65, 53)
- oq-185 [열림] 소유자가 원격 조작자를 예약해 가정 로봇을 안내하게 하는 방식(1X NEO 등)에서 원격 조작자의 영상 접근·사고 책임을 다루는 국내외 규제·인증 기준이 있는가? (영역 65, 53, 58)
- oq-211 [열림] 로봇 플랫폼이 수집하는 텔레메트리·주행 기록·영상의 보존 기간을 정한 국내 기준이나 운영 사례가 개인정보 접속기록 규정 밖에도 있는가? (영역 43, 53)
- oq-214 [열림] 로봇 플랫폼에 적용될 수 있는 현행 「개인정보의 안전성 확보조치 기준」(2023-6호 이후 개정판)의 접속기록 보관 기간·점검 주기 조항이 2023-6호와 같은가? (영역 43, 53)
- oq-228 [열림] 플랫폼이 시설 CCTV 영상을 로봇 운영용 장면 인식에 쓸 때 국내 개인정보 보호 법령의 고정형 영상정보처리기기 규정상 목적 외 이용이나 안내 의무가 문제 되는가? (영역 45, 53)
```

### docs/standards/index.md (요약: 278개 — 이름 · 종류 · 발행 기관)

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
```

### runs/2026-09-30-16/docs_tree.txt

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
glossary/aas-registry-and-discovery.md
glossary/ablation-study.md
glossary/action-dependency-graph.md
glossary/affordance.md
glossary/age-of-information.md
glossary/agentic-ai.md
glossary/aggregation-event.md
glossary/agv-technical-data-submodel.md
glossary/alternative-name.md
glossary/amr-assisted-order-picking.md
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
glossary/automatic-simulation-model-generation.md
glossary/automation-bias.md
glossary/b2mml.md
glossary/bag-file.md
glossary/battery-swapping.md
glossary/behavior-domain-definition-language.md
glossary/behavior-tree.md
glossary/block-reference.md
glossary/bpmn.md
glossary/brainless-robot.md
glossary/building-information-modeling.md
glossary/building-topology-ontology.md
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
glossary/drawing-exchange-format.md
glossary/dual-system-architecture.md
glossary/eclass.md
glossary/edit-cost.md
glossary/elevator-operating-rate.md
glossary/empanelment-programme.md
glossary/enclave.md
glossary/epcis-error-declaration.md
glossary/epcis.md
glossary/event-driven-rescheduling.md
glossary/event-trace.md
glossary/excessive-agency.md
glossary/expected-value-of-perfect-information.md
glossary/explicit-implicit-confirmation.md
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
glossary/giai.md
glossary/goal-condition.md
glossary/goods-to-person.md
glossary/grade-certainty-of-evidence.md
glossary/grai.md
glossary/graph-edit-distance.md
glossary/guidance-graph.md
glossary/hallucination.md
glossary/hddl.md
glossary/hierarchical-task-network.md
glossary/high-impact-ai.md
glossary/human-in-the-loop.md
glossary/hungarian-method.md
glossary/idempotency-key.md
glossary/identity-report.md
glossary/iec-common-data-dictionary.md
glossary/ifc.md
glossary/imitation-learning.md
glossary/index.md
glossary/indoor-mapping-data-format.md
glossary/indoor-space-subspacing.md
glossary/indoorgml.md
glossary/industrial-data.md
glossary/information-delivery-specification.md
glossary/information-for-use.md
glossary/infrastructure-mounted-sensing.md
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
glossary/lane-closure.md
glossary/language-guided-floor-plan-generation.md
glossary/latent-failure.md
glossary/layout-interchange-format.md
glossary/level-alignment-fiducial.md
glossary/lifelong-mapf.md
glossary/lift-adapter.md
glossary/linear-temporal-logic.md
glossary/littles-law.md
glossary/llm-agent.md
glossary/llm-modulo-framework.md
glossary/location-check-digit.md
glossary/managed-node.md
glossary/map-alignment.md
glossary/map-version.md
glossary/mapf.md
glossary/maps-of-dynamics.md
glossary/market-based-task-allocation.md
glossary/matter.md
glossary/mcap.md
glossary/milp.md
glossary/mission-specification-pattern.md
glossary/mobile-manipulator.md
glossary/mobile-video-information-processing-device.md
glossary/model-checking.md
glossary/model-context-protocol.md
glossary/model-registry.md
glossary/model-substitution-and-routing-dilution.md
glossary/mqtt.md
glossary/mrta.md
glossary/multi-agent-pickup-and-delivery.md
glossary/multi-fleet-orchestration.md
glossary/multi-trip-vehicle-routing-problem.md
glossary/nearest-vehicle-first-rule.md
glossary/neuro-symbolic-ai.md
glossary/number-of-clicks.md
glossary/observability.md
glossary/occupancy-grid-map.md
glossary/ocel.md
glossary/ontology-evolution.md
glossary/ontology-pitfall.md
glossary/ontology-population.md
glossary/open-rmf.md
glossary/openapi-specification.md
glossary/opentelemetry.md
glossary/operating-mode.md
glossary/operating-zone.md
glossary/optimality-gap.md
glossary/order-batching.md
glossary/outdoor-mobile-robot-operational-safety-certification.md
glossary/over-the-air-update.md
glossary/overall-equipment-effectiveness.md
glossary/panoptic-quality.md
glossary/panoptic-symbol-spotting.md
glossary/pass-k.md
glossary/pddl.md
glossary/perfect-order-fulfillment.md
glossary/performable-action.md
glossary/personal-delivery-device.md
glossary/plug-and-produce.md
glossary/post-encroachment-time.md
glossary/power-and-force-limiting.md
glossary/pre-execution-plan-verification.md
glossary/pre-hold-post-condition.md
glossary/precedence-constraint.md
glossary/predictive-maintenance.md
glossary/priority-inheritance-with-backtracking.md
glossary/private-5g-network.md
glossary/process-mining.md
glossary/prompt-injection.md
glossary/protective-separation-distance.md
glossary/public-area-mobile-robot.md
glossary/put-wall.md
glossary/raster-to-vector-conversion.md
glossary/read-point.md
glossary/reality-gap.md
glossary/regression-testing.md
glossary/release-zone.md
glossary/remote-controlled-small-vehicle.md
glossary/required-and-provided-capability.md
glossary/resource-constrained-project-scheduling-problem.md
glossary/risk-assessment.md
glossary/roadmap.md
glossary/robot-as-a-service.md
glossary/robot-density.md
glossary/robot-foundation-model.md
glossary/robot-friendly-building-certification.md
glossary/robot-task-fitness-matrix.md
glossary/robotic-middleware-for-healthcare.md
glossary/robotic-mobile-fulfillment-system.md
glossary/role-based-access-control.md
glossary/root-cause-analysis-rca.md
glossary/runtime-verification.md
glossary/safe-interval-path-planning.md
glossary/saga.md
glossary/scan-vs-bim.md
glossary/scenario-reconstruction.md
glossary/schedule-stability.md
glossary/scor.md
glossary/self-driving-laboratory.md
glossary/semantic-id.md
glossary/semantic-map.md
glossary/semantic-versioning.md
glossary/semi-open-queueing-network.md
glossary/semi-static-object.md
glossary/service-level-agreement.md
glossary/service-triad.md
glossary/shacl.md
glossary/shifting-bottleneck-detection-active-period-method.md
glossary/shuttle-based-storage-and-retrieval-system.md
glossary/signal-temporal-logic.md
glossary/sila-2.md
glossary/similarity-transformation.md
glossary/simulation-description-format.md
glossary/situation-awareness-based-agent-transparency.md
glossary/situation-state-tracking.md
glossary/skill-interface.md
glossary/skill.md
glossary/slot-filling.md
glossary/smart-hospital-leading-model.md
glossary/smart-logistics-center-certification.md
glossary/software-nameplate.md
glossary/source-grounding.md
glossary/space-boundary.md
glossary/space-graph.md
glossary/speed-and-separation-monitoring.md
glossary/sscc.md
glossary/state-of-charge.md
glossary/state-of-health.md
glossary/stpa.md
glossary/structured-output.md
glossary/success-weighted-by-path-length.md
glossary/supervisory-control.md
glossary/table-structure-recognition.md
glossary/task-decomposition.md
glossary/technology-readiness-level.md
glossary/teleoperation.md
glossary/time-window.md
glossary/topological-map.md
glossary/traversability.md
glossary/uncertainty-alignment.md
glossary/underspecification.md
glossary/urdf.md
glossary/user-simulator.md
glossary/vda-5050-cancel-order.md
glossary/vda-5050-factsheet.md
glossary/vda-5050.md
glossary/verification-and-validation-of-simulation-models.md
glossary/version-iri.md
glossary/virtual-commissioning.md
glossary/vision-language-action-model.md
glossary/voice-picking.md
glossary/waveless-order-release.md
glossary/webhook.md
glossary/wes-wcs-wms-mes-tms.md
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
references/ref-110.md
references/ref-111.md
references/ref-112.md
references/ref-113.md
references/ref-114.md
references/ref-115.md
references/ref-116.md
references/ref-117.md
references/ref-118.md
references/ref-119.md
references/ref-120.md
references/ref-121.md
references/ref-122.md
references/ref-123.md
references/ref-124.md
references/ref-125.md
references/ref-126.md
references/ref-127.md
references/ref-128.md
references/ref-129.md
references/ref-130.md
references/ref-131.md
references/ref-132.md
references/ref-133.md
references/ref-134.md
references/ref-135.md
references/ref-136.md
references/ref-137.md
references/ref-138.md
references/ref-139.md
references/ref-140.md
references/ref-141.md
references/ref-142.md
references/ref-143.md
references/ref-144.md
references/ref-145.md
references/ref-146.md
references/ref-147.md
references/ref-148.md
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
topics/2026/2026-09-30-area33-s10.md
topics/2026/2026-09-30-area33-s11.md
topics/2026/2026-09-30-area33-s3.md
topics/2026/2026-09-30-area33-s4.md
topics/2026/2026-09-30-area33-s6.md
topics/2026/2026-09-30-area33-s7.md
topics/2026/2026-09-30-area33-s8.md
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
      "summary": "개인정보 보호법 제25조의2, 이동형 영상정보처리기기 안내서(2024.9.), 가명정보 처리 가이드라인(2024-02 개정), 원본 활용 실증특례, EDPB 지침 3/2019, EgoBlur 를 표로 정리한다. [사실][^ref-1135][^ref-1140][^ref-1149]",
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
        "f17"
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
      "budget_chars": 1300,
      "summary": "기존 열린 질문 7건(oq-143·oq-171·oq-181·oq-185·oq-211·oq-214·oq-228)을 열림으로 유지하고 새 질문 4건(플랫폼 사업자 지위, 인지 출력 재식별 평가 기준, 거부 의사 공유, EDPB 지침 적용 사례)을 올린다.",
      "planned_findings": [
        "f4",
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
      "diff_summary": "seed → draft: 3~11절 첫 작성(제25조의2·이동형 안내서, 목적별 이용·가명처리, 가림·저해상도·출력 필드 기술, 가정·병원·실외 사례, 책임 경계, 연결 16개 영역, 열린 질문 11건), 13절 각주 15건, 1차 수정 15건 반영"
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
      "diff_summary": "자동 분리: 53. 개인정보·영상 데이터 의 \"11. 열린 질문\" 절(1,476자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area53-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 53. 개인정보·영상 데이터 의 \"8. 대표 연구와 자료\" 절(1,142자)을 옮겼다"
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
      "diff_summary": "자동 분리: 53. 개인정보·영상 데이터 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(965자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area53-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 53. 개인정보·영상 데이터 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(794자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-09-30-area53-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 53. 개인정보·영상 데이터 의 \"3. 왜 중요한가\" 절(780자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-09-30 | 53. 개인정보·영상 데이터 | seed → draft: 3~11절 첫 작성(제25조의2·이동형 안내서, 목적별 이용·가명처리, 가림·저해상도·출력 필드 기술, 가정·병원·실외 사례, 책임 경계), 1차 수정 15건 반영 | run 2026-09-30-16",
  "index_updates": {
    "home_recent": "2026-09-30 — 53. 개인정보·영상 데이터: seed → draft, 3~11절 첫 작성(이동형 영상정보처리기기 촬영 표시·거부, 가명처리·원본 활용 특례, 얼굴 가림·저해상도·인지 출력 필드 기술, 가정·병원·실외 사례)",
    "category_recent": "2026-09-30 — 53. 개인정보·영상 데이터: seed → draft, 3~11절 첫 작성과 각주 15건(개인정보 보호법 제25조의2, 이동형 안내서, 가림 기술 연구, 로봇청소기 점검 사례)",
    "area_recent": "2026-09-30 — 53. 개인정보·영상 데이터: 3~11절 첫 작성, 1차 수정 15건 반영(목욕실 촬영 금지 구절·EDPB 범위 강등, f5·f16 문구 정정)"
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
      "question": "EDPB 영상 장치 지침 3/2019 를 이동 로봇 카메라에 적용한 유럽 감독기관의 결정이나 해석 사례가 있으며, 보존 기간 권고는 무엇인가?",
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
      "summary": "GDPR 을 영상 장치의 개인정보 처리에 적용하는 지침으로 최종판을 2020-01 채택했다. 다루는 범위 세부는 원문 미확인.",
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
    "7절: EDPB 지침 3/2019 본문(PDF)에서 다루는 범위(적법 근거·투명성·정보주체 권리·보존 기간·가정 예외)를 확인해야 한다. 검증에서 해당 구절을 삭제했다.",
    "3·6절: 핵심 질문의 '사람의 위치 정보' 부분(보행자 위치 최소 수집, 궤적 익명화)을 직접 다룬 자료가 없어 본문에 넣지 못했다.",
    "5절: 물류창고·제조 공장·상업 시설·기타 현장의 로봇 영상·작업자 데이터 보호 사례를 찾지 못해 해당 현장 유형 사례를 쓰지 못했다.",
    "7절: 가명정보 처리 가이드라인(2024-02 개정) 원문과 ISO 31700-1:2023(소비재 개인정보 중심 설계)을 확인하면 표를 보강할 수 있다.",
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
    "분량 초과 자동 분리: 53. 개인정보·영상 데이터 본문 11,190자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 3,997자"
  ]
}
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
sources: []
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
- **oq-171** (상태: 열림) 개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한)의 촬영 사실 표시·촬영 거부 규정이 병원 이송 로봇의 카메라·센서 촬영에 어떻게 적용되며, 환자·방문객 영상을 관제 계층이 어디까지 저장·전송할 수 있는가? 이번 실행에서도 병원 내부가 '공개된 장소'에 해당하는지에 대한 해석 원문은 확인하지 못했다.
- **oq-181** (상태: 열림) 세대 안에서 거주자가 쓰는 가사 로봇·로봇청소기의 영상 수집에는 제25조의2가 적용되는가, 아니면 동의 기반 처리 조항만 적용되는가? 2026-09 로봇청소기 점검이 동의와 계약 이행 처리의 구분을 점검한 것은 부분 근거이나, 적용 조항 해석은 확인하지 못했다.
- **oq-185** (상태: 열림) 소유자가 원격 조작자를 예약해 가정 로봇을 안내하게 하는 방식에서 원격 조작자의 영상 접근·사고 책임을 다루는 국내외 규제·인증 기준이 있는가?
- **oq-211** (상태: 열림) 로봇 플랫폼이 수집하는 텔레메트리·주행 기록·영상의 보존 기간을 정한 국내 기준이나 운영 사례가 개인정보 접속기록 규정 밖에도 있는가?
- **oq-214** (상태: 열림) 로봇 플랫폼에 적용될 수 있는 현행 「개인정보의 안전성 확보조치 기준」(2023-6호 이후 개정판)의 접속기록 보관 기간·점검 주기 조항이 2023-6호와 같은가?
- **oq-228** (상태: 열림) 플랫폼이 시설 CCTV 영상을 로봇 운영용 장면 인식에 쓸 때 고정형 영상정보처리기기 규정상 목적 외 이용이나 안내 의무가 문제 되는가? 이동형 기기 안내서의 사고 영상·인공지능 학습 판단은 부분 근거이나, 고정형 기기에 대한 해석은 확인하지 못했다.
- (새 질문, 상태: 열림) 여러 제조사 로봇의 영상과 위치 정보를 모아 관제하는 플랫폼 사업자는 개인정보 보호법상 이동형 영상정보처리기기 운영자인가, 현장 운영 사업자의 수탁자인가, 그리고 촬영 표시·거부 의사 처리 의무는 누구에게 있는가?
- (새 질문, 상태: 열림) 로봇이 플랫폼·클라우드·로그로 내보내는 인지 출력(객체 목록·의미 지도·궤적)의 재식별 위험을 측정하는 공개 평가 기준이나 벤치마크가 있는가?
- (새 질문, 상태: 열림) 피촬영자가 한 로봇에 밝힌 촬영 거부 의사를 같은 현장의 다른 로봇과 플랫폼 기록에 공통으로 반영하는 방법이나 운영 사례가 있는가?
- (새 질문, 상태: 열림) EDPB 영상 장치 지침 3/2019 를 이동 로봇 카메라에 적용한 유럽 감독기관의 결정이나 해석 사례가 있으며, 보존 기간 권고는 무엇인가?

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

이 절에는 각주가 없다.

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
- Xu, Ayday, Seeing Less Is Not Seeing Safely: Privacy Leakage from Task-Scoped Robot Perception Exports(2026) — 과업 성능이 같은 인지 출력도 재식별 위험이 크게 다르다는 것을 시뮬레이션으로 보였다. 플랫폼이 로봇에서 받는 데이터의 필드 설계와 직접 이어진다. [사실][^ref-1147]
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
- [59. 법·규제·보험·라이선스](../../categories/governance-law-and-society/law-regulation-insurance-and-licensing.md) — 제25조의2, 원본 활용 특례, EDPB 지침이 이어진다. [추정][^ref-1138][^ref-1139][^ref-1149]
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
| EDPB Guidelines 3/2019(영상 장치를 통한 개인정보 처리) | 프레임워크 | GDPR 을 영상 장치의 개인정보 처리에 적용하는 지침으로 최종판을 2020-01 채택했다. 다루는 범위 세부는 원문 미확인 [사실][^ref-1149] | EDPB |
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

2022-12 보도에 따르면 카메라를 단 개발용 로봇청소기(iRobot Roomba J7 계열)가 시험 가정에서 찍은 화장실의 여성, 미성년자 등 사적 장면의 스크린샷 15장이 학습 데이터 라벨링 위탁(Scale AI의 해외 계약 작업자)을 거쳐 SNS에 유출되었다. [사실][^ref-968] 한국에서도 2025-09 보도에서 점검 대상 로봇청소기 6종 가운데 3개 제품이 사용자 인증 절차 미비로 집 내부 사진이 외부로 노출되거나 카메라가 강제로 활성화될 수 있었다고 전해졌다. [사실][^ref-1141]

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


## 수정 지시

- 판정(verdict): 수정 후 재검증
- 재작업 사유(retry_reason): —
- 수정 지시(required_fixes):
    - 8절(원 페이지 8절 원문, 분리 페이지 2026-09-30-area53-s8.md): Xu·Ayday 항목의 '플랫폼이 로봇에서 받는 데이터의 필드 설계와 직접 이어진다'를 [사실] 문장에서 떼어 별도 문장으로 두고 [추정][^ref-1147]로 표시한다. 이유: f16 에서 [사실]로 남는 것은 인지 출력 3종을 비교한 결과뿐이다. 플랫폼 필드 설계와의 연결은 f21([추정])의 해석이므로 [사실]로 쓰면 태그가 올라간다.
    - 11절(원 페이지 11절 원문, 분리 페이지 2026-09-30-area53-s11.md): 기존 열린 질문 7건의 질문 문장을 docs/open-questions.md 등록 문장 그대로 옮긴다. 현재 oq-171 은 '법령 원문과 해석 사례로 확인할 수 있는가(이번 조사는 법령 원문을 열지 못했다)'가 바뀌었고, oq-181 은 '그리고 이에 대한 개인정보보호위원회 해석이나 가이드라인이 있는가'가 빠졌으며, oq-185 는 '(1X NEO 등)'이, oq-228 은 '국내 개인정보 보호 법령의'가 빠졌다. 이번 실행의 메모는 질문 문장 뒤에 별도 문장으로 둔다. 이유: 이번 실행은 이 질문들을 갱신하지 않으므로 등록 문장과 페이지 문장이 같아야 한다.
    - 11절: oq-181 뒤 메모 '2026-09 로봇청소기 점검이 동의와 계약 이행 처리의 구분을 점검한 것은 부분 근거'에 [추정][^ref-1142]를, oq-228 뒤 메모 '이동형 기기 안내서의 사고 영상·인공지능 학습 판단은 부분 근거'에 [추정][^ref-588]을 붙이고, 13절(분리 페이지 8. 출처)에 두 각주 정의를 둔다. 이유: 출처가 있는 사실(f11, f5·f6)을 근거로 든 판단 문장인데 태그와 각주가 없다.
    - 7절·10절·11절(각 분리 페이지): 약어를 각 페이지에서 처음 쓸 때 풀어 쓴다. EDPB 는 '유럽데이터보호이사회(European Data Protection Board, EDPB)'로(f18 의 표기), 7절의 GDPR 은 '일반 개인정보 보호법(General Data Protection Regulation, GDPR)'으로 쓴다. 3절(분리 페이지 2026-09-30-area53-s3.md)의 SNS 는 '소셜 네트워크 서비스(SNS)'로 쓴다. 이유: 공통 표기 규약상 약어는 첫 등장 시 풀어 쓴다.
- 검증 노트: 판정: 조건부 승인 / 2차 수정 후 재검증. 확인 21건, 미확인 2건(f2·f18 부분 뒷받침), 교차 확인 4건(f2·f3·f6·f11). 강등: f2 의 '목욕실 등 촬영 금지' 구절 사실 → 추정(인용 출처에 없음, 본문에 법령 원문 미확인 표시), f18 의 지침 다루는 범위 구절 사실 → 추정(원문 미확인, 본문에서 삭제). 원문 미열람 출처: ref-1148(ACM 403, 검색 결과로 서지 확인). 주의: 안내서(2024.9.)와 가명정보 처리 가이드라인의 세부 내용은 원문 PDF가 아니라 법률사무소 뉴스레터와 기사의 2차 요약에 근거한다. 기술 연구(f13~f16)는 프리프린트 초록 기준이다. 그중 f16 은 시뮬레이션 결과이고, f17 은 모의 진료실 실험이다. 로봇청소기 점검 사례(f10·f11)는 기사 근거다. 사람의 위치 정보를 최소로 모으거나 궤적을 익명화하는 데 관한 전용 자료는 찾지 못했다. 물류창고·제조 공장·상업 시설·기타 현장 사례는 없다. 이 영역의 기존 열린 질문 7건(oq-143·oq-171·oq-181·oq-185·oq-211·oq-214·oq-228)은 해결 제안 없이 열림으로 유지한다. 정정 요청은 없다. 2차 검증 결과: 1차 수정 지시 15건은 모두 이행됐다(f2 구절 분리·강등, f21 예시 일반화, f5·f16·f11·f8·f1 문구 정정, f18 범위 구절 삭제, ref-588·ref-1140·ref-1148·ref-1137 서지 정정, 6·9절 범위 경계, 용어집 실증특례 정의, 5절 현장 유형 세 가지와 site_matrix_updates 일치). 드리프트는 없다. 다만 8절 분리 페이지에서 해석 문장 1건에 태그가 [사실]로 올라가 있고, 11절에서 기존 열린 질문 문장이 등록 문장과 다르며 근거 메모 2건에 태그·각주가 없다. 약어 풀어쓰기도 빠졌다. [분류원문]은 보존됐고, 섹션 순서와 링크는 형식 검증 코드 기준으로 준수·유효하다. 자동 분리된 주제 페이지 7건은 원 절 내용을 그대로 옮겼다. 참고(스토리텔러 수정 대상 아님): 자동 분리 뒤 원 페이지 프런트매터 sources 에는 본문에서 더 인용하지 않는 ref-1140·ref-1145·ref-1146·ref-1149 가 남아 있다. reference_updates 의 cited_by 도 원 페이지만 가리키므로 분리 페이지 인용 반영은 퍼블리셔 자동 영역에 맡긴다. 9절의 '이 경계는 제품 전략에 따라 이동할 수 있다'는 원문 19장 문장이지만 링크가 붙어 [분류원문] 태그 없이 쓰였다. standards_updates 의 가명정보 처리 가이드라인 URL 은 발행 기관이 아닌 법률사무소 뉴스레터다. 2차 검증에서는 도구를 쓰지 않았다.

이전 초안(runs/<run_id>/pages.json, pages/)과 2차 판정(verification2.json)은 입력에 있다. storyteller.md 9절대로 이행하고 모든 페이지의 content 를 포함한 전체 pages.json 을 다시 반환한다.
