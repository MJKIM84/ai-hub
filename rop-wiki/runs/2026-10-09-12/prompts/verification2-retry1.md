(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-09-12
- date: 2026-10-09
- run_type: update (갱신)
- 대상: 19. 사람·보행자 모델 (E. 사물·사람·실시간 상태)
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

### runs/2026-10-09-12/target.json

```json
{
  "run_id": "2026-10-09-12",
  "date": "2026-10-09",
  "weekday": "Fri",
  "run_number": 145,
  "run_type": "update",
  "forced": true,
  "target": {
    "area_no": 19,
    "area_name": "19. 사람·보행자 모델",
    "category": "E. 사물·사람·실시간 상태",
    "category_letter": "E"
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
  "selection_rationale": "CLI 지정 run_type=update, area=19"
}
```

### runs/2026-10-09-12/research.json

```json
{
  "run_id": "2026-10-09-12",
  "date": "2026-10-09",
  "run_type": "update",
  "target": {
    "area_no": 19,
    "area_name": "19. 사람·보행자 모델",
    "category": "E. 사물·사람·실시간 상태"
  },
  "gaps": [
    "정정 요청 없음(inbox/corrections.md 에 대상 페이지 요청 없음). 갱신 실행이므로 원문 미열람·검색 결과 기준 주장의 재확인과 약한 절만 다룬다",
    "섹션 5. 적용 사례 (현장 유형 명시) — 상업 시설 사례(Kidokoro 외, HRI 2013)의 '실제 쇼핑몰 시험'이 원문 미열람·검색 결과 기준이고, 병원 사례는 기사 1건, 실외·제조 공장·가정 사례 없음",
    "섹션 6. 대표 접근법과 기술(주제 페이지로 분리) — 2023 년 이후 움직임 지도 기반 장기 예측·배정 연구와 시설 센서 사람 검출을 교통 제약으로 바꾸는 방식이 없음",
    "섹션 7. 관련 표준·프레임워크·오픈소스(주제 페이지로 분리) — REP-155 의 현재 상태(Draft 여부) 재확인 필요, Open-RMF 의 사람 장애물 메시지·검출 패키지 미기재",
    "섹션 8. 대표 연구와 자료(주제 페이지로 분리) — 움직임 지도 서베이(ref-1171)·Kidokoro 외(ref-1182) 원문 미열람",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 — 직접 범위 서술이 추정뿐이고 오케스트레이션 계층의 구현 사례가 없음",
    "섹션 11. 열린 질문 — oq-272·oq-273·oq-274·oq-298·oq-303 에 근거가 없음"
  ],
  "research_questions": [
    "현장 사람의 위치와 흐름을 어떻게 알고 계획과 안전에 반영할 것인가? [분류원문]",
    "게시 페이지가 원문 미열람·검색 결과 기준으로 둔 주장(Kidokoro 외 쇼핑몰 시험, 움직임 지도 서베이의 정의, REP-155 의 상태, ATC 데이터셋의 추적 방식)은 원문·초록 기준으로 여전히 맞는가? (섹션 5·7·8 재확인)",
    "oq-272 여러 제조사 로봇과 설비 센서가 각자 감지한 사람 위치를 하나의 사람 흐름 모델로 합칠 때 좌표·시각·신뢰도·익명화 형식을 정한 공개 규격이나 구현이 있는가? (섹션 7·9)",
    "oq-273 병원·상업 시설·물류창고에서 시간대별 사람 혼잡을 로봇 작업 시간 추정과 배정·스케줄링에 반영해 처리 시간이나 지연 변화를 측정한 현장 연구가 있는가? (섹션 5·6)",
    "oq-274 공공 인파 밀집 데이터를 실외 배송로봇의 경로·운행 제한에 연동한 국내 사례나 데이터 제공 조건이 있는가? (섹션 5·9)",
    "oq-298 시간대별 사람 흐름을 담은 움직임 지도를 장소 목록·지도 판과 함께 관리하고 경로·작업 시간 계획에 넘기는 공통 형식이나 현장 사례가 있는가? (섹션 6·7)",
    "제조 공장·가정·실외 현장에서 사람 흐름·혼잡을 로봇 운영에 반영한 사례가 있는가? (섹션 5)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "ROS 규약 제안 REP-155(ROS4HRI)는 2026-10-09 확인 기준으로도 상태가 Draft, 유형이 Informational 이며, 식별되지 않은 사람을 익명 사람으로 표시하되 그 ID 는 영속을 보장하지 않고, 개인정보·동의는 다루지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1173"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원문 머리 필드: Status Draft, Type Informational, Created 11-Jan-2022. 익명 사람은 /anonymous 에 true 를 발행하고 ID 가 영속하지 않을 수 있다. location_confidence 1·0~1·0 규칙. 개인정보·동의 언급 없음(확인일 기준 상태).",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "작업 대상"
    },
    {
      "id": "f2",
      "claim": "Kucner 외 서베이(IJRR 42(11), 2023-09)의 초록은 움직임 지도를 환경의 전형적 움직임 패턴을 기록한 지도로 정의하고, 궤적이나 짧고 끊긴 움직임 관측으로 만들며 전역 경로 계획·위치추정 개선·사람 움직임 예측에 쓰인다고 하고, 새 분류 체계를 제안하며 이 분야가 실제 적용에 이를 만큼 성숙했지만 빠르게 발전 중이라고 결론짓는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1171"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Aalto 연구 포털의 초록(IJRR 42(11) pp. 977–1006, 2023-08-03 온라인): MoD 는 typical motion patterns 를 기록하며, 궤적 또는 끊긴 관측으로 구축, 전역 계획·위치추정·사람 움직임 예측에 사용. 본문 PDF 는 추출 실패로 초록만 확인.",
      "as_of": "2023-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "Kidokoro 외(HRI 2013)의 초록은 보행자 흐름·보행자 상호작용·보행 쾌적성의 세 모델로 로봇이 사람 사이를 다니는 가상 상황을 시뮬레이션하는 방법을 친근한 순찰(friendly-patrolling) 시나리오에 구현했고, 현장 실험에서 노출만 최대화한 로봇보다 주변 보행자가 보행 쾌적성을 더 좋게 인식했다고 적지만, 실험 장소가 쇼핑몰이라고는 밝히지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1182"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "OpenAlex 초록 복원(HRI 2013, pp. 259-266): three underlying models — pedestrian flow, pedestrian interaction, walking comfort; 'friendly-patrolling scenario'; field experiment 결과 보행 쾌적성 개선. 초록에 shopping mall 언급 없음.",
      "as_of": "2013-03",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f4",
      "claim": "같은 연구의 확장판(Kidokoro 외, IEEE Transactions on Robotics 31(6), 2015)은 로봇 주변 군중 형성 예측·보행 쾌적성 추정·혼잡 사전 회피 계획을 결합해 다음 이동 단계를 고르는 방법을 실제 쇼핑몰에서 시험해, 혼잡으로 인한 로봇의 보행 쾌적성 영향을 줄였다고 초록에 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1479"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "OpenAlex 초록(TRO 31(6) pp. 1419–1431, 2015-11-11): 여러 기본 보행자 행동 모델을 결합해 가상 주행 상황을 시뮬레이션하고 결과로 다음 이동 단계를 선택. 'real shopping mall' 시험에서 쾌적성 영향 감소. 효과 수치는 초록에 없음.",
      "as_of": "2015-11-11",
      "site_type": "상업 시설",
      "flow_item": "제약"
    },
    {
      "id": "f5",
      "claim": "ATC 데이터셋을 공개한 ATR 연구진(Brščić 외, IEEE THMS 43(6), 2013)은 사람 키보다 높게 단 여러 3차원 거리 센서로 넓은 공공 공간에서 사람의 위치·방향·키를 추적하는 방법을 쇼핑센터에 구현했다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1480",
        "ref-1176"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "OpenAlex 초록 복원(THMS 43(6) pp. 522–534, 2013-10-17): 'sensors, which are mounted above human height to have less occlusion'; 단일 센서 추적을 결합해 넓은 구역을 최소 센서로 덮음; 쇼핑센터 환경 구현. 센서 수·면적은 초록에 없음. 데이터셋 페이지와 같은 저자군이라 독립 교차 확인 아님.",
      "as_of": "2013-10-17",
      "site_type": "상업 시설",
      "flow_item": "작업 대상"
    },
    {
      "id": "f6",
      "claim": "Open-RMF 의 장애물 메시지(rmf_obstacle_msgs/Obstacle)는 헤더의 좌표 프레임·시각, 발행 주체(source), 층 이름(level_name), 분류 라벨(예: human), 3차원 경계 상자, 예상 수명(lifetime), 추가·삭제 동작을 담으며, 확인한 정의에는 검출 신뢰도나 익명화를 위한 필드가 없다.",
      "tag": "사실",
      "source_ids": [
        "ref-1484"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Obstacle.msg 필드: header(frame_id 기준 측정), id, source, level_name, classification(human, chair 등), bbox, data_resolution, data(옥트리), lifetime, action(ADD·DELETE·DELETEALL). 신뢰도·익명화 필드 없음. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "작업 대상"
    },
    {
      "id": "f7",
      "claim": "Open-RMF 의 rmf_obstacle 저장소는 기존 CCTV·영상 센서로 군중을 검출하는 용도의 사람 검출 노드(단안 카메라 YOLO-V4, OAK-D 카메라)를 두고, lane_blocker 노드가 /rmf_obstacles 의 장애물이 플릿 주행 차선과 겹치면 차선을 닫았다가 비면 다시 열거나 속도 제한(기본 0.5 m/s)을 건다.",
      "tag": "사실",
      "source_ids": [
        "ref-1485"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "README: rmf_human_detector 는 sensor_msgs::Image 에 YOLO-V4 로 사람 검출, 용도는 기존 CCTV 로 군중 검출. lane_blocker_node 파라미터 lane_closure_threshold 1, speed_limit_threshold 3, speed_limit 0.5. 개인정보 언급 없음. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f8",
      "claim": "f6·f7 에 따르면 시설 카메라의 사람 검출 결과를 층·발행 주체·수명과 함께 모아 여러 플릿의 차선 폐쇄·속도 제한으로 바꾸는 경로가 오케스트레이션 계층(Open-RMF)에 이미 있어 19. 사람·보행자 모델의 ROP 직접 범위 예시가 될 수 있으나, 신뢰도·익명화 형식은 정해져 있지 않아 oq-272 는 부분적으로만 답해진 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1484",
        "ref-1485",
        "ref-1173"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Open-RMF 장애물 메시지에는 source·level_name·classification·lifetime 이 있고 REP-155 에는 location_confidence 가 있으나, 두 형식 모두 익명화·집계 규칙을 두지 않음(f1·f6·f7 종합).",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "제약"
    },
    {
      "id": "f9",
      "claim": "Kazemi Eskeri 외(IROS 2025)는 시간대별 사람 존재 확률을 담은 이산 격자형 움직임 지도를 다중 로봇 작업 배정의 확률적 비용에 넣어, ATC 쇼핑몰 데이터의 기록 궤적을 재생한 시뮬레이션에서 임무 완료 시간을 움직임 무시 방법 대비 최대 26%, 기준 방법 대비 최대 19% 줄였다고 보고했으며 실제 로봇 실험은 없다.",
      "tag": "사실",
      "source_ids": [
        "ref-1083"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "arXiv 초록·HTML: 'time-dependent discrete probabilistic model'; ATC 데이터셋(오사카 쇼핑몰) 궤적을 재생한 'simulated environment'; 로봇은 시뮬레이션 차량. 완료 시간 최대 26%·19% 감소.",
      "as_of": "2025-08-27",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f10",
      "claim": "고려대학교 구로병원 연구(Lee 외, Digital Health 12, 2026)는 약제부→응급실 직원 전용 승강기 경로에서 의약품 배송로봇(DOGU IROI)의 비긴급 임무 122건(2025-06-18~29)을 분석해 전체 성공률 87.03%, 승강기 가동률 59.01% 미만에서 95.52% 였고, 실패 14건 가운데 8건이 승강기 탑승·하차 중 막힘이었으며 탑승 인원이 1명 늘 때 실패 오즈비가 1.73 이었다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1487"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "단일 병원·단일 로봇. 실패 원인: 승강기 막힘 8, 복도 자율주행 오류 4, 호출 통신 오류 2. 가동률은 승강기 대기 시간(r=0.458)·이동 시간(r=0.224)과 상관. 임계값 AUC 0.779.",
      "as_of": "2026-03-31",
      "site_type": "병원",
      "flow_item": "예외·성과"
    },
    {
      "id": "f11",
      "claim": "같은 연구는 혼잡이 임계값 아래일 때 로봇 배송을 배정하고, 승강기가 운행 중이며 가동률이 60% 이상이면 출발을 미루도록 권고하며, 59.01% 임계값은 현장 고유값이라 다른 곳에서는 다시 보정해야 한다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1487"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "결론: 'robotic medication delivery should be scheduled when congestion is below critical thresholds'. 실무 경계 약 60%, 한계로 단일 병원·단일 기종과 임계값 재보정 필요를 명시.",
      "as_of": "2026-03-31",
      "site_type": "병원",
      "flow_item": "제약"
    },
    {
      "id": "f12",
      "claim": "oq-273 에 대해 f9(쇼핑몰 데이터 기반 시뮬레이션)와 f10·f11(병원 승강기 혼잡의 현장 측정)은 사람 혼잡이 로봇 작업 시간·실패에 주는 영향을 재고 배정 시점에 반영하는 근거가 되지만, 복도·구역 단위의 시간대별 사람 흐름을 작업 시간 추정과 스케줄링에 넣어 현장에서 효과를 잰 연구는 이번에도 찾지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1083",
        "ref-1487"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f9 는 시뮬레이션뿐이고 f10 의 혼잡 지표는 승강기 가동률·탑승 인원이며 복도 보행자 흐름이 아님.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f13",
      "claim": "Gehrke 외(Transportation Research Interdisciplinary Perspectives 18, 2023)는 미국 노던애리조나대학교 캠퍼스 10곳에서 일주일간 녹화한 영상으로 보도 자율 배송로봇과 보행자·자전거 이용자의 상호작용 빈도·심각도를 침범 후 시간(PET)으로 재고, 중간·위험 충돌의 예측 요인을 모델링했다.",
      "tag": "사실",
      "source_ids": [
        "ref-990"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: 'one week of field-recorded video from ten locations'; PET 를 충돌·지점 특성의 함수로 모델링; 공유 통로 시설 관리 전략 수립에 쓰려는 목적.",
      "as_of": "2023-03-01",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f14",
      "claim": "노던애리조나대학교 보도(2023-05-16)에 따르면 이 연구에서 충돌(0초)이 12건 관찰됐고, 보도가 좁고 교차가 많은 지점일수록 위험 상호작용이 많았으며, 연구진은 넓은 보도에서 나란히 주행하도록 경로를 정하고 사람이 많은 지점의 횡단을 줄이며 덜 붐비는 표시된 지점으로 배송하도록 권고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1482"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "위험 기준: 공유 지점을 1.5초 안에 지남. 심각한 충돌은 로봇이 보행자 앞을 가로지르거나 추월할 때 대부분 발생. 권고: 'parallel travel' along 'wide sidewalks'. 논문과 같은 기관 보도라 독립 출처 아님.",
      "as_of": "2023-05-16",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f15",
      "claim": "f13·f14 에 따르면 실외 보도 로봇의 보행자 충돌 위험은 보도 폭·교차 수·사람 활동량 같은 지점 특성과 이어지므로, ROP 가 실외 경로망에 지점별 보행자 활동·폭 속성을 두고 경로·배송 지점 선택의 비용으로 쓰는 방식이 19. 사람·보행자 모델과 27. 다중 로봇 경로·교통 관리 — MAPF 를 잇는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-990",
        "ref-1482"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "연구진 권고(경로·배송 지점 선택)를 플랫폼 경로 비용으로 옮긴 해석이며 오케스트레이션 플랫폼 적용 사례는 미확인.",
      "as_of": "2026-10-09",
      "site_type": "실외",
      "flow_item": "제약"
    },
    {
      "id": "f16",
      "claim": "연계 대상: 2024-08 경기 의왕시 부곡파출소 앞 횡단보도에서 경찰청 실시간 교통신호정보를 현대차·기아 로보틱스랩 관제 시스템과 연동해, 실외 이동로봇이 카메라 신호 인식과 별도로 신호 상태를 실시간으로 받아 횡단보도를 건너는 시연이 열렸다.",
      "tag": "사실",
      "source_ids": [
        "ref-1483"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "보안뉴스(2024-08-10): 경찰청 '실시간 교통신호정보 수집·제공 시스템'을 관제와 연동, 자체 카메라 인식의 이중화. 참여: 의왕시·도로교통공단·현대차·기아. 인파·보행자 수 데이터 언급 없음.",
      "as_of": "2024-08-10",
      "site_type": "실외",
      "flow_item": "시작 조건"
    },
    {
      "id": "f17",
      "claim": "oq-274 에 대해 국내에서는 공공 교통신호 데이터를 실외 로봇 관제 시스템에 연동한 시연(f16)은 확인되지만, 인파관리지원시스템 같은 공공 인파 밀집 데이터를 로봇 경로·운행 제한에 연동한 사례나 데이터 제공 조건은 이번에도 찾지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1483",
        "ref-1177"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "한국어 검색 2회(실외 배송로봇 유동인구·인파 밀집 데이터 연동)에서 사례 없음. 연동 경로(공공 데이터→로봇 관제)의 선례로만 볼 수 있음.",
      "as_of": "2026-10-09",
      "site_type": "실외",
      "flow_item": "시작 조건"
    },
    {
      "id": "f18",
      "claim": "현대자동차·기아와 한림대학교의료원은 2025-04-07 한림대학교성심병원을 시험장으로 병원 맞춤형 배송 로봇과 관제 시스템을 함께 개발·실증하는 협약을 맺으면서 병원을 환자·의료진·휠체어·이동식 침대가 섞인 고밀도 환경으로 규정했으나, 이 발표는 조선비즈 기사(2024-07)의 로봇 대수나 사람·휠체어 앞 대기 규칙을 확인해 주지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1488",
        "ref-1181"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "현대자동차그룹 보도자료: 고밀도 병원 환경에서 주행 성능·안전성이 핵심, 병원 데이터로 제품 기획·고도화, 로봇 친화 병원 표준·인증체계 공동 수립 계획. 기간은 명시 없음.",
      "as_of": "2025-04-07",
      "site_type": "병원",
      "flow_item": "제약"
    },
    {
      "id": "f19",
      "claim": "Kairos(Catalano 외, arXiv 프리프린트 2026-09-23)는 3차원 장면 그래프의 복셀마다 사람 존재율과 이동 방향 분포를 두고 임의의 미래 시각을 스펙트럼 예측기로 예측해 주행 노드 단위로 모으는 4차원 장면 그래프를 제안했고, 로봇이 모은 캠퍼스·쇼핑몰·11개월 역 구내 데이터로 평가해 사람을 만나는 계획 과제에서 시간 불변 지도보다 같은 성공률로 더 많은 사람을 만났다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1486"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록·HTML: voxel 별 'directional mixture and a presence rate', 주행 노드로 집계·흐름 정렬 점수, 코드 공개(github.com/IacopomC/kairos). 계획 과제 목적은 만남 확률(최대화로 읽힘), 동료심사 전.",
      "as_of": "2026-09-23",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f20",
      "claim": "oq-298 에 대해 f19 처럼 사람 존재·흐름 예측을 장면 그래프의 장소·주행 노드에 붙이는 연구 구현은 있으나, 움직임 지도를 장소 목록·지도 판과 함께 관리하는 공통 형식이나 현장 운영 사례는 이번에도 찾지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1486",
        "ref-1171"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "Kairos 는 연구 코드이며 지도 판 관리·교환 형식을 다루지 않음. 움직임 지도 ROS 2 패키지 검색 1회에서도 계획기 통합 패키지는 확인하지 못함.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f21",
      "claim": "Zhu 외(arXiv 2025-10-03, IEEE RA-L 표기)는 시간대별 움직임 패턴을 담는 시간 조건부 움직임 지도를 써서 최대 60초 앞의 사람 움직임을 예측해, 실제 데이터셋 두 개에서 학습 기반 방법보다 평균 변위 오차를 최대 50% 줄였다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1489"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "초록: MoD 세 유형 평가, time-conditioned MoD 가 가장 정확, 예측 구간 최대 60초, ADE 최대 50% 개선. 데이터셋 이름은 초록에 없음.",
      "as_of": "2025-10-03",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f22",
      "claim": "Open-RMF 시뮬레이션 문서는 하드웨어 시험에서 기록한 데이터로 시뮬레이션 상황을 다시 만들 수 있다고 적고, menge 를 엔진으로 쓰는 선택 기능 crowdsim 을 traffic_editor 에서 켜 airport_terminal 예제에서 가상 사람을 움직이게 하지만, 기록된 사람 흐름을 crowdsim 입력으로 옮기는 방법은 설명하지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-406"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "원문: 'Data logged from hardware trials can be used to recreate the scenario in simulation'. crowdsim 실행 예: airport_terminal.launch.xml use_crowdsim:=1. 기록→보행자 모델 변환 언급 없음.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-1171",
      "org": "Kucner, T. P., Magnusson, M., Mghames, S., Palmieri, L., Verdoja, F., Swaminathan, C. S., Krajník, T., Schaffernicht, E., Bellotto, N., Hanheide, M., & Lilienthal, A. J. (The International Journal of Robotics Research 42(11))",
      "title": "Survey of maps of dynamics for mobile robots",
      "published": "2023",
      "url": "https://journals.sagepub.com/doi/10.1177/02783649231190428",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "움직임 지도(MoD)의 정의·분류 체계·응용·열린 문제를 정리한 서베이. 이번 실행에서는 Aalto 연구 포털의 초록을 열어 확인했다(본문 PDF 는 추출 실패).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://research.aalto.fi/en/publications/survey-of-maps-of-dynamics-for-mobile-robots/",
      "source_unopened": false
    },
    {
      "id": "ref-1173",
      "org": "ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan",
      "title": "REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction",
      "published": "2022-01-11",
      "url": "https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "사람 인지 정보를 ROS 에서 주고받는 규약 제안. 2026-10-09 확인 기준 상태 Draft, 유형 Informational.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/ros-infrastructure/rep/master/rep-0155.rst",
      "source_unopened": false
    },
    {
      "id": "ref-1176",
      "org": "ATR (Advanced Telecommunications Research Institute International), Brščić, D. 외",
      "title": "ATC shopping center tracking dataset",
      "published": null,
      "url": "https://dil.atr.jp/crest2010_HRI/ATC_dataset/",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 오사카 ATC 쇼핑센터 천장 3차원 거리 센서 보행자 추적 데이터셋(이번 실행에서 다시 열지 않음).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-1177",
      "org": "행정안전부 (대한민국 정책브리핑)",
      "title": "29일부터 인파관리지원시스템 본격 운영…다중운집 인파사고 예방",
      "published": "2023-12-27",
      "url": "https://www.korea.kr/news/policyNewsView.do?newsId=148924176",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 기지국 접속정보 기반 인파 밀집도·위험도 산출과 지자체 경보 체계(이번 실행에서 다시 열지 않음).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-1181",
      "org": "조선비즈 (이정아, 다음 뉴스 게재)",
      "title": "로봇과 인간이 공존하는 병원…약 배달 로봇에 길 비켜주고 엘리베이터도 잡아줘",
      "published": "2024-07-12",
      "url": "https://v.daum.net/v/bc4riunbUE",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 한림대학교성심병원 로봇 운영(통행 경로 표시, 사람·휠체어 앞 대기) 보도(이번 실행에서 다시 열지 않음).",
      "source_unopened": true,
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null
    },
    {
      "id": "ref-1182",
      "org": "Kidokoro, H., Kanda, T., Brščić, D., & Shiomi, M. (ACM/IEEE HRI 2013)",
      "title": "Will I bother here? - A robot anticipating its influence on pedestrian walking comfort",
      "published": "2013-03",
      "url": "https://www.semanticscholar.org/paper/Will-I-bother-here-A-robot-anticipating-its-on-Kidokoro-Kanda/bc0b26f1c13405fd89eb6d280bee739aed5b07a6",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "보행자 흐름·상호작용·쾌적성 모델로 로봇이 혼잡 영향을 예상하는 방법(HRI 2013, pp. 259-266). 이번 실행에서 OpenAlex 초록을 열어 확인했으며 초록에는 쇼핑몰 언급이 없다.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://api.openalex.org/works/doi:10.1109/HRI.2013.6483597",
      "source_unopened": false
    },
    {
      "id": "ref-406",
      "org": "Open Robotics",
      "title": "Simulation - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/simulation.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 시뮬레이션 장. 건물 지도 생성, 로봇·문·승강기 플러그인, menge 기반 crowdsim, 하드웨어 기록으로 상황 재현 언급.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1083",
      "org": "Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv)",
      "title": "Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments",
      "published": "2025-08-27",
      "url": "https://arxiv.org/abs/2508.19731",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "움직임 지도를 다중 로봇 작업 배정 비용에 넣은 방법. ATC 데이터 재생 시뮬레이션에서 임무 완료 시간 단축 보고.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2508.19731v1",
      "source_unopened": false
    },
    {
      "id": "ref-1479",
      "org": "Kidokoro, H., Kanda, T., Brščić, D., & Shiomi, M. (IEEE Transactions on Robotics 31(6))",
      "title": "Simulation-Based Behavior Planning to Prevent Congestion of Pedestrians Around a Robot",
      "published": "2015-11-11",
      "url": "https://doi.org/10.1109/TRO.2015.2492862",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "HRI 2013 연구의 저널 확장판. 군중 형성 예측·보행 쾌적성·혼잡 사전 회피 계획을 실제 쇼핑몰에서 시험(OpenAlex 초록 열람, 본문 미열람).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://api.openalex.org/works/doi:10.1109/TRO.2015.2492862",
      "source_unopened": false
    },
    {
      "id": "ref-1480",
      "org": "Brščić, D., Kanda, T., Ikeda, T., & Miyashita, T. (IEEE Transactions on Human-Machine Systems 43(6))",
      "title": "Person Tracking in Large Public Spaces Using 3-D Range Sensors",
      "published": "2013-10-17",
      "url": "https://doi.org/10.1109/THMS.2013.2283945",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "사람 키보다 높게 단 3차원 거리 센서 여러 대로 넓은 공공 공간의 사람 위치·방향·키를 추적하는 방법을 쇼핑센터에 구현(OpenAlex 초록 열람).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://api.openalex.org/works/doi:10.1109/THMS.2013.2283945",
      "source_unopened": false
    },
    {
      "id": "ref-990",
      "org": "Gehrke, S. R., Phair, C. D., Russo, B. J., & Smaglik, E. J. (Transportation Research Interdisciplinary Perspectives 18)",
      "title": "Observed sidewalk autonomous delivery robot interactions with pedestrians and bicyclists",
      "published": "2023-03-01",
      "url": "https://doi.org/10.1016/j.trip.2023.100789",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "대학 캠퍼스 10곳 일주일 영상으로 보도 배송로봇–보행자·자전거 상호작용을 PET 로 분석한 현장 관측 연구(초록 열람).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://api.openalex.org/works/doi:10.1016/j.trip.2023.100789",
      "source_unopened": false
    },
    {
      "id": "ref-1482",
      "org": "Northern Arizona University (NAU Review)",
      "title": "Got robot delivery? New research demonstrates need for robot-friendly infrastructure",
      "published": "2023-05-16",
      "url": "https://in.nau.edu/news/delivery-robot-research/",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "ref-990 연구의 대학 보도. 충돌 12건, 좁은 보도·많은 교차의 위험, 경로·배송 지점 권고를 소개.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://in.nau.edu/news/delivery-robot-research/",
      "source_unopened": false
    },
    {
      "id": "ref-1483",
      "org": "보안뉴스 (박미영)",
      "title": "경찰청 제공 실시간 교통신호정보, 보행자와 함께 거닐 실외 이동로봇의 눈이 되다",
      "published": "2024-08-10",
      "url": "https://www.boannews.com/news/articleView.html?idxno=131956",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "경찰청 실시간 교통신호정보를 현대차·기아 로보틱스랩 관제와 연동해 실외 로봇이 횡단보도를 건너는 의왕시 시연 보도.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.boannews.com/news/articleView.html?idxno=131956",
      "source_unopened": false
    },
    {
      "id": "ref-1484",
      "org": "Open Robotics (open-rmf/rmf_internal_msgs)",
      "title": "rmf_obstacle_msgs/msg/Obstacle.msg",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_obstacle_msgs/msg/Obstacle.msg",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 장애물 메시지 정의. 프레임·시각, 발행 주체, 층, 분류 라벨(human 등), 경계 상자, 수명, 추가·삭제 동작.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_internal_msgs/main/rmf_obstacle_msgs/msg/Obstacle.msg",
      "source_unopened": false
    },
    {
      "id": "ref-1485",
      "org": "Open Robotics (open-rmf/rmf_obstacle)",
      "title": "rmf_obstacle — README",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_obstacle",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "CCTV·카메라 사람 검출 노드와 장애물이 주행 차선과 겹치면 차선을 닫거나 속도를 제한하는 lane_blocker 노드를 제공.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_obstacle/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-1486",
      "org": "Catalano, I., Placed, J. A., Civera, J., & Peña Queralta, J. (arXiv)",
      "title": "Kairos: Grounded Forecasting of Presence and Directional Flow in 4D Scene Graphs",
      "published": "2026-09-23",
      "url": "https://arxiv.org/abs/2609.27467",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "4차원 장면 그래프에 사람 존재율·이동 방향 분포를 두고 미래 시각을 예측하는 프리프린트. 캠퍼스·쇼핑몰·역 구내 데이터 평가, 코드 공개.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2609.27467v1",
      "source_unopened": false
    },
    {
      "id": "ref-1487",
      "org": "Lee, Y. 외, Park, I.-H. (교신) (Digital Health 12, 고려대학교 구로병원)",
      "title": "Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments",
      "published": "2026-03-31",
      "url": "https://journals.sagepub.com/doi/10.1177/20552076261437181",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "고려대 구로병원 의약품 배송로봇 122개 임무의 승강기 혼잡(가동률·탑승 인원)과 성공률·지연을 분석한 전향적 타당성 연구.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://journals.sagepub.com/doi/10.1177/20552076261437181",
      "source_unopened": false
    },
    {
      "id": "ref-1488",
      "org": "현대자동차그룹",
      "title": "현대자동차·기아, 한림대의료원과 로봇 친화 병원 공동 구축 위한 업무협약 체결",
      "published": "2025-04-07",
      "url": "https://www.hyundaimotorgroup.com/ko/news/CONT0000000000173736",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "한림대학교성심병원을 시험장으로 병원 맞춤형 배송 로봇·관제 시스템 공동 개발·실증 협약. 병원을 고밀도 혼재 환경으로 규정.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://www.hyundaimotorgroup.com/ko/news/CONT0000000000173736",
      "source_unopened": false
    },
    {
      "id": "ref-1489",
      "org": "Zhu, Y., Rudenko, A., Kucner, T. P., Lilienthal, A. J., & Magnusson, M. (arXiv; IEEE RA-L 표기)",
      "title": "Long-Term Human Motion Prediction Using Spatio-Temporal Maps of Dynamics",
      "published": "2025-10-03",
      "url": "https://arxiv.org/abs/2510.03031",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "시간 조건부 움직임 지도로 최대 60초 사람 움직임을 예측해 학습 기반 방법보다 ADE 최대 50% 개선을 보고(초록 열람).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/abs/2510.03031",
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md",
      "sections": [
        "5",
        "6",
        "7",
        "8",
        "9",
        "11"
      ],
      "rationale": "갱신(차등): 섹션 5 — 상업 시설 사례의 쇼핑몰 시험 근거를 바로잡음: HRI 2013 초록(f3, ref-1182)은 친근한 순찰 시나리오의 현장 실험만 적고 쇼핑몰을 밝히지 않으며, 쇼핑몰 시험은 TRO 2015 확장판(f4, ref-1479)의 초록에 있으므로 사례 제목·각주를 ref-1479 중심으로 고치고 '원문 미열람, 검색 결과 기준' 문구를 정리. ATC 데이터셋 추적 방식은 f5 로 보강(같은 저자군이라 교차 확인 아님). 병원 — 고려대학교 구로병원 승강기 혼잡 사례(f10·f11, 한국, 여섯 항목: 수행 자원·제약·예외·성과) 추가, 한림대 사례는 f18 로 맥락만 보강하고 기사 1건 기준임을 유지. 실외 — 대학 캠퍼스 보도 배송로봇 관측 사례(f13·f14, f15) 추가로 '실외 사례 없음' 문장 수정, 의왕시 교통신호 연동 시연(f16)은 연계 대상으로 짧게. 제조 공장·가정은 여전히 사례 없음. 섹션 6(주제 페이지) — 시설 카메라 사람 검출→차선 폐쇄·속도 제한(f7), 움직임 지도 기반 배정(f9)·장기 예측(f21)·4D 장면 그래프 예측(f19). 섹션 7(주제 페이지) — REP-155 상태 Draft 재확인(f1), Open-RMF 장애물 메시지·rmf_obstacle(f6·f7). 섹션 8(주제 페이지) — 움직임 지도 서베이 초록 확인(f2), f9·f10·f13·f19·f21 추가. 섹션 9 — 직접 범위 예시로 f8(Open-RMF 장애물·lane_blocker), 외부 검출 모델 실행·카메라는 연계 대상. 섹션 11 — oq-272 부분 근거 f6·f8, oq-273 부분 근거 f9·f10·f11·f12, oq-274 부분 근거 f16·f17, oq-298 부분 근거 f19·f20, oq-303·oq-256 부분 근거 f22(모두 미해결 유지), 새 열린 질문 2건. 교차 규칙: 학습 기반 예측·배정(f9·f21)은 46. 예측·학습 기반 최적화와 25. 작업 배정 — MRTA 양쪽 연결, 현재 관측(f6·f7)은 18. 실시간 세계 상태·데이터 일관성, crowdsim(f22)은 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현 쪽으로 구분. 다음 실행 후보: 63. 병원·의료 페이지 5절에 f10·f11, 66. 실외 페이지에 f13·f14·f16, 27. 다중 로봇 경로·교통 관리 — MAPF 에 f7."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "평균 변위 오차",
      "term_en": "Average Displacement Error (ADE)",
      "definition": "궤적 예측에서 예측 구간의 모든 시점에 대해 예측 위치와 실제 위치 사이 거리를 평균한 오차 지표이다."
    },
    {
      "term_ko": "4차원 장면 그래프",
      "term_en": "4D Scene Graph",
      "definition": "3차원 장면 그래프의 장소·물체 노드에 시간 축을 더해 사람 존재나 흐름 같은 시간에 따라 변하는 상태를 함께 표현·예측하는 표현이다."
    }
  ],
  "open_questions_new": [
    "시설 카메라의 사람 검출 결과로 플릿 주행 차선을 닫거나 속도를 제한하는 방식(Open-RMF lane_blocker)을 여러 제조사 로봇 현장에서 운영할 때 오검출·과도한 차선 폐쇄가 처리량과 지연에 주는 영향을 측정한 자료가 있는가? | 관련 영역: 19. 사람·보행자 모델, 27. 다중 로봇 경로·교통 관리 — MAPF, 18. 실시간 세계 상태·데이터 일관성 | 근거: f7 | 종류: 일반",
    "병원 승강기 가동률·탑승 인원 같은 혼잡 임계값(예: 고려대 구로병원의 약 60%)을 다른 병원·건물로 옮겨 로봇 배정 시점에 쓸 때 재보정하는 방법이나 다기관 연구가 있는가? | 관련 영역: 19. 사람·보행자 모델, 26. 작업 순서·스케줄링, 22. 설비·건물 시스템 연동 | 근거: f11 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 19,
    "cross_checked_count": 0,
    "unverified": [
      "Kidokoro 외 HRI 2013 과 TRO 2015 는 OpenAlex 초록만 열었고 본문 미열람(IEEE Xplore 빈 응답, CroRIS 대기 페이지). 쇼핑몰 효과 수치 미확인",
      "ref-1171 움직임 지도 서베이는 Aalto 포털 초록만 열었고 본문 PDF 는 추출 실패",
      "f5 는 ATC 데이터셋(ref-1176)과 같은 저자군의 논문이라 독립 교차 확인 아님. ATC 센서 49대·약 900㎡ 수치는 이번에 다시 확인하지 않음",
      "f14 는 ref-990 과 같은 대학의 보도라 독립 출처 아님. 논문 본문(충돌 수·예측 요인 계수) 미열람",
      "f10·f11 고려대 구로병원 연구는 단일 출처, 교차 확인 실패",
      "f18 은 조선비즈 기사(ref-1181)의 로봇 73대·대기 규칙을 확인해 주지 않음. 한림대 사례의 독립 확인은 여전히 실패",
      "f19 Kairos 는 동료심사 전 프리프린트, 계획 과제의 목적(만남 최대화)은 본문 앞부분 기준 해석이며 데이터셋 이름(ATC·HB 표기)과의 대응 미확인",
      "f21 의 데이터셋 이름 미확인(초록에 없음)",
      "Open-RMF rmf_obstacle 의 이슈 #22(장애물 서버 통합 계획)는 403 으로 열지 못함",
      "STRANDS 요양시설 배치에서 FreMEn 으로 상호작용 확률을 예측해 일정을 짠 내용은 PDF 추출 실패로 출처로 넣지 않음",
      "제조 공장·가정 현장의 사람 흐름 반영 사례는 이번에도 찾지 못함",
      "공공 인파 밀집 데이터의 실외 로봇 연동 국내 사례 미발견(oq-274)"
    ],
    "scope_violations": [
      "f7·f8: 카메라 영상의 사람 검출 모델 실행은 원문 19장 '로봇 자체 지능·제어'·센서 인식 쪽에 가까워 연계 대상으로 두고, ROP 직접 범위는 검출 결과(장애물 메시지)를 모아 차선 폐쇄·속도 제한 같은 교통 제약으로 쓰는 부분으로 한정해야 함",
      "f16: 교통신호 시스템은 시설·공공 시스템 경계의 연계 대상이므로 claim 을 '연계 대상: '으로 시작",
      "f10·f11: 승강기 운행·호출 제어는 시설·설비 제어 경계의 연계 대상이며, ROP 쪽은 혼잡 지표를 받아 배정·출발 시점을 정하는 부분으로만 서술해야 함",
      "f13·f14: 보도 위 국소 회피·양보 동작은 로봇 제조사 몫이며, ROP 쪽은 경로·배송 지점 선택 비용(f15, 추정)으로만 연결"
    ],
    "budget_used": {
      "queries": 15,
      "sources": 11
    },
    "limits": "web_fetch_available: true · fetch_mode full. 갱신(update) 실행으로, 정정 요청이 없어 원문 미열람·검색 결과 기준이던 주장의 재확인과 약한 절(5·7·9·11)과 열린 질문(oq-272·oq-273·oq-274·oq-298·oq-303)만 조사했다. 검색 15회/30, 신규 출처 11건/15(ref-1479~ref-1489, 예약 구간 안). 재사용 8건 가운데 ref-1171(Aalto 초록)·ref-1173(github_raw)·ref-1182(OpenAlex 초록)·ref-1083(arXiv)·ref-406(inbox 원문)은 이번에 열었고, ref-1176·ref-1177·ref-1181 은 열지 않았다(fetched false). 신규 11건은 모두 원문 또는 공식 초록을 열었다. 다만 ref-1479·ref-1480·ref-990 은 OpenAlex 초록만 열었다. 교차 확인 0건이다. 같은 저자군·같은 기관 쌍(ref-1480과 ref-1176, ref-1482와 ref-990)은 독립 출처로 보지 않았다. 주요 정정 근거: 5절 상업 시설 사례의 '실제 쇼핑몰 시험'은 HRI 2013 초록에 없고 TRO 2015 확장판 초록에 있다(f3·f4). 7절 REP-155 는 2026-10-09 원문 기준으로 여전히 Draft 이며(f1), 지난 실행의 '공식 채택' 검색 요약과의 차이는 원문 기준으로 정리된다. 한국 자료: 신규 ref-1483(보안뉴스)·ref-1487(고려대 구로병원)·ref-1488(현대자동차그룹), 재사용 ref-1177·ref-1181. 현장 유형: 병원(f10·f11·f18)·상업 시설(f4·f5)·실외(f13·f14·f15·f16·f17)이며 물류창고는 기존 ILIAD 사례를 유지하고 새 근거는 찾지 않았다. 제조 공장·가정 사례는 없다. 18. 실시간 세계 상태·데이터 일관성(현재 관측: f6·f7)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험: f22)을 구분했다. L. AI·학습 기술 관련 f9·f21 은 46. 예측·학습 기반 최적화와 25. 작업 배정 — MRTA 에 함께 연결하자고 제안했다. 열린 질문에 대한 부분 근거: oq-272(f6·f8), oq-273(f9·f10·f11·f12), oq-274(f16·f17), oq-298(f19·f20), oq-303·oq-256(f22). 해결 제안은 없다. 벤더 기능·성능 주장은 없다(f18 은 협약 내용 진술이다). 페이지 갱신 제안은 1건(대상 영역 페이지)이며 63. 병원·의료, 66. 실외, 27. 다중 로봇 경로·교통 관리 — MAPF 반영은 다음 실행 후보로 남겼다. 입력 누락 없음, 우선 지정 질문 없음."
  }
}
```

### runs/2026-10-09-12/verification.json

```json
{
  "run_id": "2026-10-09-12",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: raw.githubusercontent.com 원문 열람. 머리 필드 Status Draft·Type Informational·Created 11-Jan-2022, 익명 사람 ID 는 영구 보장 없음, location_confidence 1/1 미만/0 규칙, 개인정보·동의 언급 없음. 단일 출처(공식 원문). 기준일 2026-10-09 확인일."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Aalto 연구 포털 초록 열람. IJRR 42(11) pp. 977-1006, 온라인 2023-08-03, 인쇄 2023-09. 정의·구축·용도·새 분류 체계·성숙하나 빠르게 발전 중이라는 결론 모두 초록에 있음. 본문 미열람이므로 '초록 기준' 범위로만 쓴다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: OpenAlex 초록 복원. 세 모델(보행자 흐름·상호작용·보행 쾌적성), friendly-patrolling 시나리오, 현장 실험에서 노출만 최대화한 로봇보다 쾌적성 개선. 초록에 shopping mall 언급 없음 — 게시 페이지 5절의 '실제 쇼핑몰에서 시험(원문 미열람, 검색 결과 기준)' 서술의 정정 근거. HRI 2013 pp. 259-266, 2013-03."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: OpenAlex 초록. TRO 31(6) pp. 1419-1431, 2015-11-11, 저자 일치. 군중 형성 예측·보행 쾌적성·혼잡 사전 회피 계획, 'real shopping mall' 시험에서 혼잡에 의한 쾌적성 영향 감소. 효과 수치 초록에 없음(미확인)."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: OpenAlex 초록(THMS 43(6) pp. 522-534, 2013-10-17). 사람 키보다 높게 단 여러 3차원 거리 센서, 위치·방향·키 추적, 쇼핑센터 구현. ref-1176 은 이번 실행에서 열지 않았고(원문 미열람) 같은 저자군이므로 교차 확인 아님. 센서 수·면적은 이 출처로 확인되지 않음."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Obstacle.msg 원문(github_raw). header(frame_id 기준), id, source, level_name, classification(human, chair 등), bbox, data_resolution, data(옥트리), lifetime, action(ADD·DELETE·DELETEALL). 신뢰도·익명화 필드 없음. 발행일 미확인, 확인일 2026-10-09."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: README 원문. 단, 'CCTV·영상 센서로 군중 검출' 용도는 단안 카메라용 rmf_human_detector(YOLO-V4)에 적힌 것이고 OAK-D 노드는 MobileNet-SSD 칩 내 추론이다. lane_blocker 기본값 lane_closure_threshold 1, speed_limit_threshold 3, speed_limit 0.5 m/s 확인. 검출 모델 실행은 연계 대상."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지: f6·f7·f1 종합 해석. 다만 '신뢰도·익명화 형식은 정해져 있지 않아'는 부정확 — Open-RMF 장애물 메시지에는 신뢰도 필드가 없고 REP-155 에는 location_confidence 가 있으며, 두 형식 모두 익명화·집계 규칙이 없다로 구분해 쓰게 한다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 초록·HTML. 'time-dependent discrete probabilistic model', ATC 데이터셋(오사카 쇼핑몰) 궤적 재생 시뮬레이션, 로봇은 car-like 차량 모델, 실제 로봇 실험 없음, 최대 26%·19% 단축, IROS 2025 채택 표기. 시뮬레이션 결과임을 본문에 명시해야 함."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: SAGE 원문 열람. 고려대 구로병원, DOGU IROI, 비긴급 122건(2025-06-18~29), 성공률 87.03%, EOR 59.01% 미만 95.52%, 실패 14건(승강기 막힘 8·복도 자율주행 4·호출 통신 2), 탑승 인원 OR 1.73, AUC 0.779, r 0.458·0.224. 주의: 논문은 성공률 분모를 밝히지 않으며 122건·실패 14건으로는 약 88.5% 가 되어 87.03% 와 맞지 않는다(논문 내부 불일치). 단일 병원·단일 기종 단일 출처."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 초록 결론 'scheduled when congestion is below critical thresholds', 4.2절 'defer dispatch if in transit and EOR ≥ 60%', 4.3절 비긴급 작업 미루기·묶기, 59.01% 는 현장 고유값으로 다른 병원에서 재보정 필요. 승강기 운행·호출 제어 자체는 시설·설비 제어 연계 대상."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지: f9(시뮬레이션)와 f10·f11(승강기 혼잡 지표) 종합. f10 의 혼잡 지표가 승강기 가동률·탑승 인원이지 복도 보행자 흐름이 아니라는 점은 원문과 맞음. oq-273 해결 아님."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: OpenAlex 초록. 노던애리조나대 캠퍼스 10곳 일주일 현장 영상, PET 로 심각도 측정, 중간·위험 충돌 예측 요인 모델링, TRIP 18 article 100789, 2023-03-01."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: NAU Review 2023-05-16. 충돌(0초) 12건, 위험 기준 1.5초 미만, 좁은 보도·많은 교차와 위험 증가, 넓은 보도 평행 주행·붐비는 지점 횡단 최소화·덜 붐비는 표시 지점 배송 권고, 심각 충돌은 대부분 가로지르기·추월 때. 논문과 같은 기관 보도라 독립 출처 아님."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지: 연구진 권고를 ROP 경로 비용으로 옮긴 해석이며 플랫폼 적용 사례는 미확인. 보도 위 국소 회피·양보는 로봇 제조사 몫(연계 대상)."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 보안뉴스 2024-08-10(기자 박미영). 의왕 부곡파출소 앞 횡단보도 시연('지난 9일'), 경찰청 실시간 교통신호정보 수집·제공 시스템과 현대차·기아 로보틱스랩 관제 연동, 카메라 인식과 이중화, 참여 경찰청·의왕시·도로교통공단·현대차·기아. 인파·보행자 수 데이터 언급 없음. 기사 1건, '연계 대상:' 표시 적정."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지: 미발견 진술. ref-1177 은 이번 실행에서 원문 미열람(기존 게시 각주는 2026-09-30 열람). oq-274 해결 아님."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 현대자동차그룹 2025-04-07 발표. 한림대학교성심병원 실증 거점, 병원 맞춤형 배송 로봇·관제 시스템 개발, 환자·의료진·휠체어·이동식 침대 혼재 고밀도 환경 규정, 로봇 대수·대기 규칙 언급 없음. 기능·성능 주장이 아닌 협약 내용 진술이라 벤더 주장 병기 대상 아님. ref-1181(조선비즈)은 이번 실행 원문 미열람."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 초록·HTML. 복셀별 방향 혼합·존재율, 스펙트럼 예측기로 임의 미래 시각 예측, 주행 노드로 점유 가중 집계(VI-A1)·흐름 정렬 점수(VI-A2), 캠퍼스·쇼핑몰·11개월 역 구내, 시간 불변 지도보다 같은 성공률에서 더 많은 사람을 만남, 코드 공개. 동료심사 전 프리프린트(2026-09-23). 데이터셋 약칭(ATC·HB)과 환경 대응은 미확인."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "추정 유지: Kairos 가 지도 판 관리·교환 형식을 다루지 않는다는 점은 열람 범위와 맞음. oq-298 해결 아님."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv 초록(2025-10-03, IEEE RA-L 표기). 시간 조건부 MoD 가 가장 정확, 예측 구간 최대 60초, 실제 데이터셋 두 개, 학습 기반 방법 대비 ADE 최대 50% 개선. 데이터셋 이름은 초록에 없어 미확인."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문 data/source_texts/ref-406.txt. 'Data logged from hardware trials can be used to recreate the scenario in simulation', crowdsim 은 rmf_traffic_editor 에서 켜는 선택 기능·menge 엔진, airport_terminal.launch.xml use_crowdsim:=1 예. 기록된 사람 흐름을 crowdsim 입력으로 옮기는 설명 없음. 발행일 미확인."
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
      "f3·f4 는 게시 페이지 5절 상업 시설 사례(ref-1182, '실제 쇼핑몰에서 시험했다(원문 미열람, 검색 결과 기준)')와 겹치며 그 문장을 정정한다 — 쇼핑몰 시험의 근거는 ref-1479 다",
      "f1 은 게시 페이지 7절의 REP-155 Draft 문장(ref-1173)과 같은 주장이므로 기존 각주를 재사용한다",
      "f2 는 게시 페이지 3·4·8절이 인용한 ref-1171(원문 미열람 표시)의 재확인이다",
      "f5 는 게시 페이지 5절 ATC 데이터셋 문장(ref-1176)과 같은 저자군 자료이며 교차 확인이 아니다",
      "f22 는 oq-256·oq-303 에 걸린 기존 ref-406 각주를 재사용한다",
      "f9·f21 의 움직임 지도 기반 배정·예측은 46. 예측·학습 기반 최적화 페이지와 내용이 이어지므로 양쪽 연결만 한다"
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
    "5절 상업 시설 사례: 사례 제목과 표의 근거를 ref-1479(Kidokoro 외, IEEE Transactions on Robotics 31(6), 2015)로 바꾸고 '실제 쇼핑몰에서 시험했다' 문장의 각주를 [^ref-1182] 에서 [^ref-1479] 로 고친다. '(원문 미열람, 검색 결과 기준)' 문구는 삭제한다. ref-1182(HRI 2013)는 f3 범위(세 모델, 친근한 순찰 시나리오의 현장 실험, 초록에 쇼핑몰 언급 없음)로만 인용한다 — 근거: HRI 2013 초록에 shopping mall 이 없고 TRO 2015 초록에 'real shopping mall' 이 있다.",
    "13절 각주: ref-1171 과 ref-1182 는 이번 실행에서 초록을 열었으므로 접근일을 2026-10-09 로 바꾸고 ' (원문 미열람)' 을 뺀다. ref-1171 발행일은 2023-09(IJRR 42(11), pp. 977-1006)로 적는다. 본문에서 이 두 출처는 '초록 기준'임을 밝힌다 — 본문 PDF 는 열지 못했다.",
    "13절 각주: 이번 실행에서 열지 않은 ref-1176·ref-1177·ref-1181 은 기존 각주 줄(접근일 2026-09-30)을 그대로 두고 접근일을 2026-10-09 로 바꾸지 않는다.",
    "f5: ref-1480 과 ref-1176 을 교차 확인으로 쓰지 않는다 — 같은 ATR 저자군이다. ATC 센서 49대·약 900㎡ 수치는 기존 ref-1176 각주로만 둔다.",
    "f7: 'CCTV·기존 영상 센서로 군중 검출' 용도는 단안 카메라용 rmf_human_detector(YOLO-V4)에만 붙인다. OAK-D 노드는 칩 내 추론(MobileNet-SSD)으로 따로 적는다. 사람 검출 모델 실행·카메라는 '연계 대상'으로 짧게 둔다. ROP 직접 범위는 /rmf_obstacles 장애물을 모아 차선 폐쇄·속도 제한으로 바꾸는 부분으로 한정한다 — 분류 원문 19장 '로봇 자체 지능·제어(센서 인식)' 경계다.",
    "f8(9절·11절): '신뢰도·익명화 형식은 정해져 있지 않다'를 'Open-RMF 장애물 메시지에는 검출 신뢰도 필드가 없고, REP-155 는 location_confidence 를 두지만 두 형식 모두 익명화·집계 규칙이 없다'로 구분해 쓴다. [추정] 태그를 유지한다.",
    "f10: 성공률 87.03% 는 '논문 보고값'으로 적는다. 논문이 분모를 밝히지 않았고 보고된 122건·실패 14건과 맞지 않으므로 '성공률 산출 기준 미확인'을 함께 적는다. 수치를 다시 계산해 바꾸지 않는다. '단일 병원·단일 기종' 한계를 유지한다.",
    "f10·f11: 혼잡 지표는 용어집의 '승강기 가동률 (Elevator Operating Rate (EOR))'으로 표기한다. 승강기 운행·호출 제어는 '연계 대상'으로 둔다. ROP 쪽은 혼잡 지표를 받아 배정·출발 시점을 정하는 부분으로만 쓴다(6절·9절).",
    "f13·f14: 지표는 용어집의 '침범 후 시간 (Post-Encroachment Time (PET))'으로 적는다. f14 는 논문과 같은 기관의 보도이므로 교차 확인으로 쓰지 않는다. 보도 위 국소 회피·양보 동작은 제조사 '연계 대상'으로 둔다. f15 는 [추정] 으로 둔다.",
    "5절 '사례를 찾지 못한 현장 유형' 문장: '실외에서는 … 찾지 못했다'를 고쳐 실외 사례(f13·f14, 현장 유형 실외)를 여섯 항목 표로 추가한다. 제조 공장·가정은 여전히 사례가 없다고 남긴다. 의왕시 교통신호 연동 시연(f16)은 '연계 대상'으로 9절에 짧게 둔다.",
    "f9 는 '기록 궤적을 재생한 시뮬레이션 결과이며 실제 로봇 실험은 없다'를 함께 적는다. f19 는 '동료심사 전 프리프린트(2026-09-23)'임을, f21 은 '데이터셋 이름 미확인'임을 함께 적는다. f9·f21(학습·예측 기반)은 46. 예측·학습 기반 최적화와 25. 작업 배정 — MRTA 양쪽에 연결한다(교차 규칙).",
    "f6·f7(현재 관측)은 18. 실시간 세계 상태·데이터 일관성 쪽으로 둔다. f22(crowdsim, 기록 재현)는 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현 쪽으로 구분해 연결한다 — 두 영역을 섞지 않는다.",
    "11절: oq-256·oq-272·oq-273·oq-274·oq-298·oq-303 은 부분 근거만 더한다. 상태는 '열림'으로 두고 해결로 바꾸지 않는다 — 어느 finding 도 질문에 완전히 답하지 않는다.",
    "용어집: '평균 변위 오차'·'4차원 장면 그래프'는 신규 등록하되, '4차원 장면 그래프' 정의에 기존 용어 '3차원 장면 그래프 (3D Scene Graph)'와 연결한다. 움직임 지도·차선 폐쇄·승강기 가동률·침범 후 시간은 이미 있으므로 신규 등록하지 않는다."
  ],
  "confidence": "low",
  "verification_note": "판정: 조건부 승인. 확인 22건, 미확인 0건, 교차 확인 0건. 강등: 없음. 원문 미열람 출처: ref-1176, ref-1177, ref-1181(이번 실행에서 다시 열지 않음, 기존 각주는 2026-09-30 열람). 주의: 신규 근거는 모두 단일 출처다. 같은 저자군·같은 기관 쌍(ref-1480과 ref-1176, ref-1482와 ref-990)은 독립 출처가 아니다. ref-1171·ref-1182·ref-1479·ref-1480·ref-990 은 초록만 확인했다. 게시 페이지 5절의 '쇼핑몰 시험' 근거는 HRI 2013(ref-1182)이 아니라 TRO 2015 확장판(ref-1479)으로 정정된다. 고려대 구로병원 연구(ref-1487)는 성공률 87.03% 의 분모를 밝히지 않았고, 보고된 임무 122건·실패 14건과 맞지 않는다. 같은 연구는 단일 병원·단일 기종이며 혼잡 지표는 승강기 가동률이다. Kazemi Eskeri 외(ref-1083)는 시뮬레이션 결과이고 Kairos(ref-1486)는 동료심사 전 프리프린트다. 3·6·9절의 핵심 판단은 여전히 [추정]이다. 열린 질문 oq-256·oq-272·oq-273·oq-274·oq-298·oq-303 은 부분 근거만 있어 해결로 인정하지 않는다. 정정 요청 없음. 브리프 기록 주의: ref-406 은 fetched_via 가 github_raw 로 적혔으나 실제 근거는 입력 원문(data/source_texts/ref-406.txt, inbox)이고 fetch_url 이 비어 있다.",
  "retry_reason": null
}
```

### runs/2026-10-09-12/pages.json

```json
{
  "run_id": "2026-10-09-12",
  "outline": [
    {
      "path": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 0,
      "summary": "변경 없음. 기존 요약과 주제 페이지 링크를 유지한다."
    },
    {
      "path": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md",
      "section": "4. 핵심 개념과 용어",
      "budget_chars": 200,
      "summary": "움직임 지도를 서베이 초록 기준(ref-1171, 본문 미열람)으로 정의하는 한 항목을 덧붙인다. [사실][^ref-1171]",
      "planned_findings": [
        "f2"
      ]
    },
    {
      "path": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 3300,
      "summary": "상업 시설 사례의 쇼핑몰 시험 근거를 TRO 2015 확장판으로 정정하고(ref-1479), 고려대 구로병원 승강기 혼잡 사례와 대학 캠퍼스 보도 배송로봇 관측 사례를 여섯 항목 표로 더한다. [사실][^ref-1479][^ref-1487][^ref-990]",
      "planned_findings": [
        "f3",
        "f4",
        "f5",
        "f10",
        "f11",
        "f13",
        "f14",
        "f15",
        "f18"
      ]
    },
    {
      "path": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1400,
      "summary": "기존 요약 문장 뒤에 2026-09-30 주제 페이지 링크를 되살리고, 시설 카메라 사람 검출→차선 폐쇄·속도 제한, 움직임 지도 기반 배정(시뮬레이션)·장기 예측·4차원 장면 그래프 예측을 덧붙인다. [사실][^ref-1485][^ref-1083]",
      "planned_findings": [
        "f7",
        "f9",
        "f11",
        "f19",
        "f21"
      ]
    },
    {
      "path": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 900,
      "summary": "REP-155 사실 문장 뒤에 2026-09-30 주제 페이지 링크를 되살리고, REP-155 Draft 재확인과 Open-RMF 장애물 메시지·rmf_obstacle·crowdsim 을 덧붙인다. [사실][^ref-1173][^ref-1484]",
      "planned_findings": [
        "f1",
        "f6",
        "f7",
        "f22"
      ]
    },
    {
      "path": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 1200,
      "summary": "기존 요약 뒤에 2026-09-30 주제 페이지 링크를 되살리고, 움직임 지도 서베이 초록 확인과 연구 7건을 덧붙인다(Brščić 외는 '사람 키보다 높게 단' 센서로 표기). [사실][^ref-1171]",
      "planned_findings": [
        "f2",
        "f4",
        "f5",
        "f9",
        "f10",
        "f13",
        "f19",
        "f21"
      ]
    },
    {
      "path": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 1900,
      "summary": "시설 카메라 검출→교통 제약, 승강기 혼잡→배정·출발 시점, 실외 보도 경로 비용을 직접 범위 예시로 더하고 검출 모델·승강기 제어·국소 회피·교통신호 시스템을 연계 대상으로 둔다. [추정][^ref-1485][^ref-1487]",
      "planned_findings": [
        "f7",
        "f8",
        "f10",
        "f11",
        "f15",
        "f16",
        "f17"
      ]
    },
    {
      "path": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 800,
      "summary": "기존 요약 뒤에 2026-09-30 주제 페이지 링크를 되살리고 25·22·46·27 연결과 18·34·36 구분을 덧붙인다. [추정][^ref-1083][^ref-1484]",
      "planned_findings": [
        "f6",
        "f7",
        "f9",
        "f10",
        "f21",
        "f22"
      ]
    },
    {
      "path": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md",
      "section": "11. 열린 질문",
      "budget_chars": 1100,
      "summary": "기존 요약 뒤에 2026-09-30 주제 페이지 링크(oq-261·oq-294·oq-307 서술 포함)를 되살리고, oq-256·oq-272·oq-273·oq-274·oq-298·oq-303 부분 근거(모두 열림)와 새 질문 2건을 덧붙인다. [추정][^ref-1484][^ref-1487]",
      "planned_findings": [
        "f8",
        "f12",
        "f17",
        "f20",
        "f22"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "차등 갱신: 5절 상업 시설 사례 근거를 ref-1182→ref-1479 로 정정하고 병원(고려대 구로병원)·실외(대학 캠퍼스 보도) 사례 추가, 4절 덧붙임, 6·7·8·10·11절 기존 요약·2026-09-30 주제 페이지 링크 유지와 새 내용 추가, 9절 경계 표 보강, 13절 각주 정리, 프런트매터 sources 에 기존 ref-1175·ref-1079 유지(2차 수정 반영)",
      "patches": [
        {
          "section": "4. 핵심 개념과 용어",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-09-12/pages/categories/objects-people-and-live-state/people-and-pedestrian-model.md 의 해당 절을 본다)"
        },
        {
          "section": "5. 적용 사례 (현장 유형 명시)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-09-12/pages/categories/objects-people-and-live-state/people-and-pedestrian-model.md 의 해당 절을 본다)"
        },
        {
          "section": "6. 대표 접근법과 기술",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-09-12/pages/categories/objects-people-and-live-state/people-and-pedestrian-model.md 의 해당 절을 본다)"
        },
        {
          "section": "7. 관련 표준·프레임워크·오픈소스",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-09-12/pages/categories/objects-people-and-live-state/people-and-pedestrian-model.md 의 해당 절을 본다)"
        },
        {
          "section": "8. 대표 연구와 자료",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-09-12/pages/categories/objects-people-and-live-state/people-and-pedestrian-model.md 의 해당 절을 본다)"
        },
        {
          "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-09-12/pages/categories/objects-people-and-live-state/people-and-pedestrian-model.md 의 해당 절을 본다)"
        },
        {
          "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-09-12/pages/categories/objects-people-and-live-state/people-and-pedestrian-model.md 의 해당 절을 본다)"
        },
        {
          "section": "11. 열린 질문",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-09-12/pages/categories/objects-people-and-live-state/people-and-pedestrian-model.md 의 해당 절을 본다)"
        },
        {
          "section": "13. 참고 자료 (각주)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-09-12/pages/categories/objects-people-and-live-state/people-and-pedestrian-model.md 의 해당 절을 본다)",
          "frontmatter": {
            "related_areas": [
              15,
              16,
              18,
              22,
              25,
              26,
              27,
              31,
              34,
              36,
              46,
              49,
              53,
              54,
              61,
              63,
              64,
              66
            ],
            "sources": [
              "ref-1171",
              "ref-1172",
              "ref-1173",
              "ref-1174",
              "ref-1175",
              "ref-1176",
              "ref-1177",
              "ref-1178",
              "ref-1079",
              "ref-1179",
              "ref-406",
              "ref-1180",
              "ref-1128",
              "ref-1181",
              "ref-1182",
              "ref-1479",
              "ref-1480",
              "ref-990",
              "ref-1482",
              "ref-1483",
              "ref-1484",
              "ref-1485",
              "ref-1486",
              "ref-1487",
              "ref-1488",
              "ref-1489",
              "ref-1083"
            ],
            "last_run": "2026-10-09",
            "confidence": "low"
          }
        }
      ]
    },
    {
      "path": "docs/topics/2026/2026-10-09-area19-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 19. 사람·보행자 모델 의 \"6. 대표 접근법과 기술\" 절(1,552자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-09-area19-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 19. 사람·보행자 모델 의 \"8. 대표 연구와 자료\" 절(1,472자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-09-area19-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 19. 사람·보행자 모델 의 \"11. 열린 질문\" 절(1,150자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-09-area19-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 19. 사람·보행자 모델 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(925자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-09-area19-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 19. 사람·보행자 모델 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(733자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-10-09 | 19. 사람·보행자 모델 | 갱신: 상업 시설 사례의 쇼핑몰 시험 근거를 HRI 2013(ref-1182)에서 TRO 2015 확장판(ref-1479)으로 정정, 병원(고려대 구로병원 승강기 혼잡)·실외(대학 캠퍼스 보도 배송로봇) 사례 추가, Open-RMF 사람 장애물·차선 차단과 움직임 지도 기반 배정·예측 보강, 열린 질문 부분 근거·새 질문 2건 | run 2026-10-09-12",
  "index_updates": {
    "home_recent": "2026-10-09 — 19. 사람·보행자 모델: 상업 시설 사례 근거 정정(TRO 2015 확장판), 병원(고려대 구로병원 승강기 혼잡)·실외(대학 캠퍼스 보도 배송로봇) 사례 추가, Open-RMF 사람 장애물·차선 차단과 움직임 지도 기반 배정·예측 보강",
    "category_recent": "2026-10-09 — 19. 사람·보행자 모델: 5절 사례 정정·추가(병원·실외), 6~11절 보강(시설 카메라 사람 검출→차선 폐쇄, 움직임 지도 배정·예측, 열린 질문 부분 근거)",
    "area_recent": "2026-10-09 — 19. 사람·보행자 모델: 갱신 — 5절 상업 시설 사례 근거를 ref-1479 로 정정, 병원·실외 사례 추가, 4·6·7·8·10·11절 보강(2026-09-30 주제 페이지 링크 유지), 9절 경계 표 보강, 13절 각주 정리"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "average-displacement-error",
      "term_ko": "평균 변위 오차",
      "term_en": "Average Displacement Error (ADE)",
      "definition": "궤적 예측에서 예측 구간의 모든 시점에 대해 예측 위치와 실제 위치 사이 거리를 평균한 오차 지표이다.",
      "description": "사람 움직임 궤적 예측의 성능을 비교할 때 쓴다. Zhu 외(2025-10-03)는 시간 조건부 움직임 지도로 최대 60초 앞을 예측해 학습 기반 방법보다 이 오차를 최대 50% 줄였다고 보고했다(데이터셋 이름 미확인).",
      "related_areas": [
        19,
        46
      ],
      "sources": [
        "ref-1489"
      ]
    },
    {
      "action": "new",
      "slug": "4d-scene-graph",
      "term_ko": "4차원 장면 그래프",
      "term_en": "4D Scene Graph",
      "definition": "3차원 장면 그래프(3D Scene Graph)의 장소·물체 노드에 시간 축을 더해 사람 존재나 흐름 같은 시간에 따라 변하는 상태를 함께 표현·예측하는 표현이다.",
      "description": "기존 용어 3차원 장면 그래프(3d-scene-graph)를 시간 축으로 확장한 것이다. Kairos(Catalano 외, 2026-09-23, 동료심사 전 프리프린트)는 복셀마다 사람 존재율과 이동 방향 분포를 두고 미래 시각을 예측해 주행 노드 단위로 모은다.",
      "related_areas": [
        19,
        16,
        46
      ],
      "sources": [
        "ref-1486"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-1171",
      "org": "Kucner, T. P., Magnusson, M., Mghames, S., Palmieri, L., Verdoja, F., Swaminathan, C. S., Krajník, T., Schaffernicht, E., Bellotto, N., Hanheide, M., & Lilienthal, A. J. (The International Journal of Robotics Research 42(11))",
      "title": "Survey of maps of dynamics for mobile robots",
      "published": "2023-09",
      "url": "https://journals.sagepub.com/doi/10.1177/02783649231190428",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "움직임 지도(MoD)의 정의·분류 체계·응용·열린 문제를 정리한 서베이(IJRR 42(11) pp. 977-1006). 2026-10-09 Aalto 연구 포털의 초록을 열어 확인했다(본문 PDF 는 추출 실패).",
      "cited_by": [
        "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1173",
      "org": "ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan",
      "title": "REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction",
      "published": "2022-01-11",
      "url": "https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "사람 인지 정보를 ROS 에서 주고받는 규약 제안. 2026-10-09 확인 기준 상태 Draft, 유형 Informational.",
      "cited_by": [
        "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1182",
      "org": "Kidokoro, H., Kanda, T., Brščić, D., & Shiomi, M. (ACM/IEEE HRI 2013)",
      "title": "Will I bother here? - A robot anticipating its influence on pedestrian walking comfort",
      "published": "2013-03",
      "url": "https://www.semanticscholar.org/paper/Will-I-bother-here-A-robot-anticipating-its-on-Kidokoro-Kanda/bc0b26f1c13405fd89eb6d280bee739aed5b07a6",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "보행자 흐름·상호작용·쾌적성 모델로 로봇이 혼잡 영향을 예상하는 방법(HRI 2013, pp. 259-266). OpenAlex 초록을 열어 확인했으며 초록에는 쇼핑몰 언급이 없다.",
      "cited_by": [
        "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-406",
      "org": "Open Robotics",
      "title": "Simulation - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/simulation.html",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 시뮬레이션 장. 건물 지도 생성, 로봇·문·승강기 플러그인, menge 기반 crowdsim, 하드웨어 기록으로 상황 재현 언급.",
      "cited_by": [
        "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1083",
      "org": "Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv)",
      "title": "Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments",
      "published": "2025-08-27",
      "url": "https://arxiv.org/abs/2508.19731",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "움직임 지도를 다중 로봇 작업 배정 비용에 넣은 방법. ATC 데이터 재생 시뮬레이션에서 임무 완료 시간 단축 보고(실제 로봇 실험 없음).",
      "cited_by": [
        "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1479",
      "org": "Kidokoro, H., Kanda, T., Brščić, D., & Shiomi, M. (IEEE Transactions on Robotics 31(6))",
      "title": "Simulation-Based Behavior Planning to Prevent Congestion of Pedestrians Around a Robot",
      "published": "2015-11-11",
      "url": "https://doi.org/10.1109/TRO.2015.2492862",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "HRI 2013 연구의 저널 확장판. 군중 형성 예측·보행 쾌적성·혼잡 사전 회피 계획을 실제 쇼핑몰에서 시험(OpenAlex 초록 열람, 본문 미열람).",
      "cited_by": [
        "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1480",
      "org": "Brščić, D., Kanda, T., Ikeda, T., & Miyashita, T. (IEEE Transactions on Human-Machine Systems 43(6))",
      "title": "Person Tracking in Large Public Spaces Using 3-D Range Sensors",
      "published": "2013-10-17",
      "url": "https://doi.org/10.1109/THMS.2013.2283945",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "사람 키보다 높게 단 3차원 거리 센서 여러 대로 넓은 공공 공간의 사람 위치·방향·키를 추적하는 방법을 쇼핑센터에 구현(OpenAlex 초록 열람).",
      "cited_by": [
        "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-990",
      "org": "Gehrke, S. R., Phair, C. D., Russo, B. J., & Smaglik, E. J. (Transportation Research Interdisciplinary Perspectives 18)",
      "title": "Observed sidewalk autonomous delivery robot interactions with pedestrians and bicyclists",
      "published": "2023-03-01",
      "url": "https://doi.org/10.1016/j.trip.2023.100789",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "대학 캠퍼스 10곳 일주일 영상으로 보도 배송로봇–보행자·자전거 상호작용을 PET 로 분석한 현장 관측 연구(초록 열람).",
      "cited_by": [
        "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1482",
      "org": "Northern Arizona University (NAU Review)",
      "title": "Got robot delivery? New research demonstrates need for robot-friendly infrastructure",
      "published": "2023-05-16",
      "url": "https://in.nau.edu/news/delivery-robot-research/",
      "type": "정부·연구기관",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "ref-990 연구의 대학 보도. 충돌 12건, 좁은 보도·많은 교차의 위험, 경로·배송 지점 권고를 소개(논문과 같은 기관이라 독립 출처 아님).",
      "cited_by": [
        "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1483",
      "org": "보안뉴스 (박미영)",
      "title": "경찰청 제공 실시간 교통신호정보, 보행자와 함께 거닐 실외 이동로봇의 눈이 되다",
      "published": "2024-08-10",
      "url": "https://www.boannews.com/news/articleView.html?idxno=131956",
      "type": "기사",
      "reliability": "low",
      "accessed": "2026-10-09",
      "summary": "경찰청 실시간 교통신호정보를 현대차·기아 로보틱스랩 관제와 연동해 실외 로봇이 횡단보도를 건너는 의왕시 시연 보도.",
      "cited_by": [
        "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1484",
      "org": "Open Robotics (open-rmf/rmf_internal_msgs)",
      "title": "rmf_obstacle_msgs/msg/Obstacle.msg",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_obstacle_msgs/msg/Obstacle.msg",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "Open-RMF 장애물 메시지 정의. 프레임·시각, 발행 주체, 층, 분류 라벨(human 등), 경계 상자, 수명, 추가·삭제 동작. 신뢰도·익명화 필드 없음.",
      "cited_by": [
        "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1485",
      "org": "Open Robotics (open-rmf/rmf_obstacle)",
      "title": "rmf_obstacle — README",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_obstacle",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "CCTV·카메라 사람 검출 노드와 장애물이 주행 차선과 겹치면 차선을 닫거나 속도를 제한하는 lane_blocker 노드를 제공.",
      "cited_by": [
        "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1486",
      "org": "Catalano, I., Placed, J. A., Civera, J., & Peña Queralta, J. (arXiv)",
      "title": "Kairos: Grounded Forecasting of Presence and Directional Flow in 4D Scene Graphs",
      "published": "2026-09-23",
      "url": "https://arxiv.org/abs/2609.27467",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "4차원 장면 그래프에 사람 존재율·이동 방향 분포를 두고 미래 시각을 예측하는 프리프린트(동료심사 전). 캠퍼스·쇼핑몰·역 구내 데이터 평가, 코드 공개.",
      "cited_by": [
        "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1487",
      "org": "Lee, Y. 외, Park, I.-H. (교신) (Digital Health 12, 고려대학교 구로병원)",
      "title": "Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments",
      "published": "2026-03-31",
      "url": "https://journals.sagepub.com/doi/10.1177/20552076261437181",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "고려대 구로병원 의약품 배송로봇 122개 임무의 승강기 혼잡(가동률·탑승 인원)과 성공률·지연을 분석한 전향적 타당성 연구. 성공률 87.03% 의 분모는 밝히지 않음.",
      "cited_by": [
        "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1488",
      "org": "현대자동차그룹",
      "title": "현대자동차·기아, 한림대의료원과 로봇 친화 병원 공동 구축 위한 업무협약 체결",
      "published": "2025-04-07",
      "url": "https://www.hyundaimotorgroup.com/ko/news/CONT0000000000173736",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "한림대학교성심병원을 시험장으로 병원 맞춤형 배송 로봇·관제 시스템 공동 개발·실증 협약. 병원을 고밀도 혼재 환경으로 규정.",
      "cited_by": [
        "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1489",
      "org": "Zhu, Y., Rudenko, A., Kucner, T. P., Lilienthal, A. J., & Magnusson, M. (arXiv; IEEE RA-L 표기)",
      "title": "Long-Term Human Motion Prediction Using Spatio-Temporal Maps of Dynamics",
      "published": "2025-10-03",
      "url": "https://arxiv.org/abs/2510.03031",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "시간 조건부 움직임 지도로 최대 60초 사람 움직임을 예측해 학습 기반 방법보다 ADE 최대 50% 개선을 보고(초록 열람, 데이터셋 이름 미확인).",
      "cited_by": [
        "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md"
      ],
      "source_unopened": false
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "시설 카메라의 사람 검출 결과로 플릿 주행 차선을 닫거나 속도를 제한하는 방식(Open-RMF lane_blocker)을 여러 제조사 로봇 현장에서 운영할 때 오검출·과도한 차선 폐쇄가 처리량과 지연에 주는 영향을 측정한 자료가 있는가?",
      "areas": [
        19,
        27,
        18
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "병원 승강기 가동률·탑승 인원 같은 혼잡 임계값(예: 고려대 구로병원의 약 60%)을 다른 병원·건물로 옮겨 로봇 배정 시점에 쓸 때 재보정하는 방법이나 다기관 연구가 있는가?",
      "areas": [
        19,
        26,
        22
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "병원",
      "item": "시작 조건",
      "link": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시",
      "title": "19. 사람·보행자 모델"
    },
    {
      "site_type": "병원",
      "item": "작업 대상",
      "link": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시",
      "title": "19. 사람·보행자 모델"
    },
    {
      "site_type": "병원",
      "item": "수행 자원",
      "link": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시",
      "title": "19. 사람·보행자 모델"
    },
    {
      "site_type": "병원",
      "item": "제약",
      "link": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시",
      "title": "19. 사람·보행자 모델"
    },
    {
      "site_type": "병원",
      "item": "예외·성과",
      "link": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시",
      "title": "19. 사람·보행자 모델"
    },
    {
      "site_type": "상업 시설",
      "item": "작업 대상",
      "link": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시",
      "title": "19. 사람·보행자 모델"
    },
    {
      "site_type": "상업 시설",
      "item": "수행 자원",
      "link": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시",
      "title": "19. 사람·보행자 모델"
    },
    {
      "site_type": "상업 시설",
      "item": "제약",
      "link": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시",
      "title": "19. 사람·보행자 모델"
    },
    {
      "site_type": "상업 시설",
      "item": "예외·성과",
      "link": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시",
      "title": "19. 사람·보행자 모델"
    },
    {
      "site_type": "실외",
      "item": "작업 대상",
      "link": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시",
      "title": "19. 사람·보행자 모델"
    },
    {
      "site_type": "실외",
      "item": "수행 자원",
      "link": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시",
      "title": "19. 사람·보행자 모델"
    },
    {
      "site_type": "실외",
      "item": "제약",
      "link": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시",
      "title": "19. 사람·보행자 모델"
    },
    {
      "site_type": "실외",
      "item": "예외·성과",
      "link": "docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#5-적용-사례-현장-유형-명시",
      "title": "19. 사람·보행자 모델"
    }
  ],
  "standards_updates": [
    {
      "name": "Open-RMF 장애물 메시지(rmf_internal_msgs의 rmf_obstacle_msgs)",
      "kind": "오픈소스",
      "org": "Open Robotics (open-rmf)",
      "url": "https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_obstacle_msgs/msg/Obstacle.msg",
      "related_areas": [
        19,
        18,
        27
      ],
      "summary": "프레임·시각, 발행 주체, 층, 분류 라벨(human 등), 3차원 경계 상자, 수명, 추가·삭제 동작을 담는 장애물 메시지. 확인한 정의에 검출 신뢰도·익명화 필드는 없다(확인일 2026-10-09).",
      "ref_id": "ref-1484"
    },
    {
      "name": "Open-RMF rmf_obstacle (사람 검출·lane_blocker)",
      "kind": "오픈소스",
      "org": "Open Robotics (open-rmf)",
      "url": "https://github.com/open-rmf/rmf_obstacle",
      "related_areas": [
        19,
        27,
        18
      ],
      "summary": "단안 카메라(YOLO-V4)·OAK-D 사람 검출 노드와, 장애물이 플릿 주행 차선과 겹치면 차선을 닫거나 속도를 제한(기본 0.5 m/s)하는 lane_blocker 노드를 제공한다(확인일 2026-10-09).",
      "ref_id": "ref-1485"
    }
  ],
  "additional_research_requests": [
    "E. 사물·사람·실시간 상태 대분류 페이지 '다른 대분류와의 연결' 절의 G. 계획·최적화(26. 작업 순서·스케줄링), I. 설계·시뮬레이션(34. 시뮬레이션·예측용 디지털 트윈), Q. 현장 유형별 적용 항목이 Kidokoro 외 HRI 2013(ref-1182)을 쇼핑몰 사례 근거로 인용한다. 이번 갱신으로 쇼핑몰 시험의 근거가 TRO 2015 확장판(ref-1479)으로 정정됐으므로 다음 대분류 연결(category_link) 실행에서 해당 문장의 각주를 정정해야 한다. 실외 사례도 이제 있으므로 같은 절의 '아직 다루지 않은 연결'의 'Q. 현장 유형별 적용' 문장도 고쳐야 한다(예산·실행 유형으로 이번에 미룸)",
    "pipeline 담당 확인 요청: 자동 분리 코드가 절 안의 기존 '자세한 내용은 주제 페이지 …' 링크 줄을 새 분리 주제 페이지로 옮기지 않고 버렸다(2차 검증 지적). 이번 재실행에서는 6·7·8·10·11절 첫 문단의 요약 문장 바로 뒤에 2026-09-30 주제 페이지 링크 문장을 넣어 원 절과 분리 주제 페이지 양쪽에 남도록 했다. 또 새 분리 주제 페이지(2026-10-09-area19-s6·s7·s8·s10·s11)의 H1 이 기존 2026-09-30 분리 주제 페이지와 같아지는 문제의 처리 방안(제목에 날짜를 붙이거나 기존 주제 페이지에 합치는 방식)이 필요하다",
    "다음 실행 후보: 63. 병원·의료 5절에 고려대 구로병원 승강기 혼잡 사례(ref-1487), 66. 실외에 캠퍼스 보도 배송로봇 관측(ref-990·ref-1482)과 의왕시 교통신호 연동 시연(ref-1483), 27. 다중 로봇 경로·교통 관리 — MAPF 에 Open-RMF lane_blocker(ref-1485) 반영",
    "5절 병원 사례: 고려대 구로병원 연구(ref-1487)의 성공률 87.03% 산출 분모를 확인할 수 있는 정오표·추가 자료와, 다른 병원에서 승강기 혼잡을 독립적으로 측정한 자료가 필요하다(단일 출처·내부 불일치)",
    "5절 상업 시설 사례: Kidokoro 외 TRO 2015(ref-1479) 본문의 쇼핑몰 시험 효과 수치, ATC 데이터셋 센서 49대·약 900㎡ 수치의 재확인이 필요하다",
    "5절: 제조 공장·가정 현장에서 사람 흐름·혼잡을 로봇 운영에 반영한 사례가 여전히 없다",
    "5절 병원 사례: 한림대학교성심병원 로봇 대수(73대)·사람·휠체어 앞 대기 규칙을 기사(ref-1181) 외 독립 출처로 확인하지 못했다"
  ],
  "fixes_applied": [
    "5절 상업 시설 사례 근거 정정 — 사례 제목을 'Kidokoro 외, IEEE Transactions on Robotics 2015'로 바꾸고 표의 모든 칸과 '실제 쇼핑몰에서 시험했다' 문장의 각주를 [^ref-1479]로 고쳤으며 '(원문 미열람, 검색 결과 기준)' 문구를 지웠다. ref-1182 는 세 모델·친근한 순찰 시나리오의 현장 실험·초록에 쇼핑몰 언급 없음 범위의 한 문장에만 인용했다.",
    "13절 ref-1171·ref-1182 각주 — 접근일을 2026-10-09 로 바꾸고 ' (원문 미열람)'을 뺐으며 ref-1171 발행일을 2023-09 로 적었다. 본문에서는 4절 움직임 지도 항목·8절 서베이 항목에 '초록 기준(본문 미열람)'을, 5절 HRI 2013 문장에 '초록 기준'을 밝혔다.",
    "13절 ref-1176·ref-1177·ref-1181 각주 — 기존 줄(접근일 2026-09-30)을 그대로 두었고 참고문헌 갱신에도 넣지 않았다.",
    "f5 — Brščić 외(ref-1480) 문장에 '데이터셋과 같은 저자군이라 독립 교차 확인이 아니다'를 밝히고 ref-1176 과 교차 확인으로 쓰지 않았다. ATC 센서 49대·약 900㎡ 수치는 기존 ref-1176 각주 문장에만 두었다.",
    "f7 — 6절에서 'CCTV 영상으로 군중 검출' 용도는 단안 카메라용 rmf_human_detector(YOLO-V4)에만 붙이고 OAK-D 노드는 칩 내 추론(MobileNet-SSD)으로 따로 적었다. 6절·9절에서 사람 검출 모델 실행·카메라를 연계 대상으로 두고, ROP 직접 범위는 /rmf_obstacles 장애물을 모아 차선 폐쇄·속도 제한으로 바꾸는 부분으로 한정했다.",
    "f8 — 9절 끝 문단과 11절 oq-272 항목에서 'Open-RMF 장애물 메시지에는 검출 신뢰도 필드가 없고, REP-155 는 location_confidence 를 두지만 두 형식 모두 익명화·집계 규칙이 없다'로 구분해 쓰고 [추정]을 유지했다.",
    "f10 — 5절 표와 서술에서 87.03% 를 '논문 보고 성공률'로 적고 '성공률 산출 기준 미확인'을 함께 적었으며, 다시 계산한 수치는 쓰지 않았다. '단일 병원·단일 기종' 한계를 서술과 6절에 남겼다.",
    "f10·f11 — 혼잡 지표를 용어집 '승강기 가동률'(elevator-operating-rate) 링크로 표기했다. 5절·6절·9절에서 승강기 운행·호출 제어를 연계 대상으로 두고, ROP 쪽은 혼잡 지표를 받아 배정·출발 시점을 정하는 부분으로만 썼다.",
    "f13·f14 — 지표를 용어집 '침범 후 시간'(post-encroachment-time) 링크로 적었다. f14(ref-1482)는 '논문과 같은 기관의 보도라 독립 교차 확인이 아니다'를 밝혔다. 보도 위 국소 회피·양보 동작을 제조사 연계 대상으로 5절·9절에 두고 f15 는 [추정]으로 썼다.",
    "5절 '사례를 찾지 못한 현장 유형' 문장 — 실외 문장을 고치고 실외 사례(노던애리조나대학교 캠퍼스 보도, f13·f14)를 여섯 항목 표로 추가했다. 제조 공장·가정은 사례가 없다고 남겼고, 의왕시 교통신호 연동 시연(f16)은 9절 표에 '연계 대상:'으로 짧게 두었다.",
    "f9·f19·f21 — 6절과 8절에서 f9 에 '기록 궤적을 재생한 시뮬레이션 결과이며 실제 로봇 실험은 없다', f19 에 '동료심사 전 프리프린트(2026-09-23)', f21 에 '데이터셋 이름 미확인'을 함께 적었다. f9·f21 은 6절과 10절에서 46. 예측·학습 기반 최적화와 25. 작업 배정 — MRTA 양쪽에 연결했다(프런트매터 related_areas 에 25 추가).",
    "f6·f7 은 6절·7절·10절에서 현재 관측으로 18. 실시간 세계 상태·데이터 일관성 쪽에 두었다. f22(crowdsim, 기록 재현)는 7절·10절에서 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현 쪽으로 구분해 연결했다.",
    "11절 — oq-256·oq-272·oq-273·oq-274·oq-298·oq-303 에 부분 근거만 덧붙이고 상태를 모두 '열림'으로 두었다. open_question_updates 에 상태 변경을 내지 않았다.",
    "용어집 — '평균 변위 오차'와 '4차원 장면 그래프'를 신규로 냈고, '4차원 장면 그래프' 정의와 설명에 기존 용어 '3차원 장면 그래프 (3D Scene Graph)'를 연결했다. 움직임 지도·차선 폐쇄·승강기 가동률·침범 후 시간은 신규로 내지 않고 본문에서 기존 용어집 페이지에 링크만 했다.",
    "2차: 세부영역 페이지 6·7·8·10·11절의 2026-09-30 주제 페이지 링크 복구 — 다섯 절을 append 대신 replace 패치로 보내, 각 절 첫 문단의 기존 요약 문장 바로 뒤에 '2026-09-30 실행에서 검증한 이 절의 상세 내용은 주제 페이지 [19. 사람·보행자 모델 — …](../../topics/2026/2026-09-30-area19-sN.md)에 있다.' 문장을 두었다. 자동 분리 뒤에도 세부영역 페이지 해당 절에 남는 앞 두 문장 안에 들어가 새 2026-10-09 분리 주제 페이지 링크와 함께 놓이고, 분리 주제 페이지 3. 본문 첫머리에도 그대로 옮겨진다. 7절은 REP-155 사실 문장 뒤에 링크를 두고 추정 문장을 다음 단락으로 나눴으며, 11절 링크 문장에는 oq-261·oq-294·oq-307 서술이 그 페이지에 있음을 밝혔다.",
    "2차: 8절(분리 시 2026-10-09-area19-s8) Brščić 외 항목 — '천장 높이 3차원 거리 센서'를 '사람 키보다 높게 단 여러 3차원 거리 센서'로 고쳤다.",
    "2차: 세부영역 페이지 프런트매터 sources — 근거 없이 빠졌던 ref-1175(THÖR)와 ref-1079(Francis 외 평가 지침)를 기존 순서 자리에 되살렸다(기존 페이지처럼 분리 주제 페이지의 출처를 함께 올리는 관행이며 13절 각주 정의는 기존과 같이 두지 않았다).",
    "분량 초과 자동 분리: 19. 사람·보행자 모델 본문 12,913자 > 기준 4,000자 → 5개 절을 주제 페이지로 옮김, 남은 본문 8,122자"
  ]
}
```

### runs/2026-10-09-12/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md (9개 절)
- 분량 초과 자동 분리:
    - docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-10-09-area19-s6.md (1,552자)
    - docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md "8. 대표 연구와 자료" → docs/topics/2026/2026-10-09-area19-s8.md (1,472자)
    - docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md "11. 열린 질문" → docs/topics/2026/2026-10-09-area19-s11.md (1,150자)
    - docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-10-09-area19-s7.md (925자)
    - docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-10-09-area19-s10.md (733자)
```

### runs/2026-10-09-12/pages/categories/objects-people-and-live-state/people-and-pedestrian-model.md

```markdown
---
title: "19. 사람·보행자 모델"
type: area
category: "E. 사물·사람·실시간 상태"
area_no: 19
related_areas: [15, 16, 18, 22, 25, 26, 27, 31, 34, 36, 46, 49, 53, 54, 61, 63, 64, 66]
tags: [움직임 지도, 사람 궤적 예측, 사회적 힘 모델, 사회적 내비게이션, ROS4HRI]
status: draft
confidence: low
created: 2026-09-28
updated: 2026-10-09
sources: [ref-1171, ref-1172, ref-1173, ref-1174, ref-1175, ref-1176, ref-1177, ref-1178, ref-1079, ref-1179, ref-406, ref-1180, ref-1128, ref-1181, ref-1182, ref-1479, ref-1480, ref-990, ref-1482, ref-1483, ref-1484, ref-1485, ref-1486, ref-1487, ref-1488, ref-1489, ref-1083]
last_run: 2026-10-09
version: 3
---

[홈](../../index.md) › [E. 사물·사람·실시간 상태](index.md) › 19. 사람·보행자 모델

# 19. 사람·보행자 모델

!!! info "소속 대분류"
    [E. 사물·사람·실시간 상태](index.md) — 핵심 질문:
    작업 대상·사람·설비·로봇이 지금 어디에 어떤 상태로 있는지 어떻게 믿을 수 있게 알 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: low · 페이지 버전: 2 · 마지막 갱신: 2026-09-30 · 마지막 실행: 2026-09-30
<!-- auto:page-status:end -->

## 1. 한 줄 정의

현장 사람의 위치·흐름·혼잡을 모델링해 계획과 안전에 쓴다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **사람·보행자 모델**: 현장 사람의 위치·목적지·멈춤·교차를 모델링해 로봇 계획과 안전에 반영한다
- **사람 흐름·혼잡 추정**: 시간대·구역별 사람의 흐름과 혼잡을 추정해 경로와 작업 시간에 반영한다

## 2. 핵심 질문

현장 사람의 위치와 흐름을 어떻게 알고 계획과 안전에 반영할 것인가? [분류원문]

## 3. 왜 중요한가

확인한 자료를 종합하면, 현장 사람의 위치와 흐름은 로봇 탑재·천장 센서로 사람을 실시간 검출·추적하고, 장기 관측으로 시간대별 흐름 지도(움직임 지도)를 학습하며, 궤적 예측·보행자 행동 모델로 가까운 미래와 가상 상황을 추정해 경로 비용·속도 제약·혼잡 회피·운영 규칙(전용 통로, 무조건 대기)으로 계획과 안전에 반영된다. [추정][^ref-1171][^ref-1172][^ref-1178][^ref-1180]

자세한 내용은 주제 페이지 [19. 사람·보행자 모델 — 왜 중요한가](../../topics/2026/2026-09-30-area19-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 영역의 핵심 개념은 사람 흐름을 저장하는 지도, 가까운 미래 경로를 추정하는 예측, 보행자 행동을 계산하는 모델, 사람 정보를 주고받는 표현 규약이다. [추정][^ref-1171][^ref-1172][^ref-1174][^ref-1173]

자세한 내용은 주제 페이지 [19. 사람·보행자 모델 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area19-s4.md)에 있다.

- **[움직임 지도](../../glossary/maps-of-dynamics.md)(Maps of Dynamics, MoD)** — 서베이 초록 기준으로, 환경의 전형적 움직임 패턴을 기록한 지도이며 궤적이나 짧고 끊긴 움직임 관측으로 만들고 전역 경로 계획·위치추정 개선·사람 움직임 예측에 쓴다(2023-09 발행, 본문 미열람). [사실][^ref-1171]

## 5. 적용 사례 (현장 유형 명시)

근거를 찾은 다섯 현장 유형(물류창고·병원·상업 시설·실외·기타)의 사례를 나눠 적는다. 현장 유형 × 대분류 적용 사례는 [현장 유형 매트릭스](../../site-matrix.md)에 모인다.

**현장 유형:** 물류창고

**사례:** 창고 자율 지게차 플릿이 작업자 이동 패턴을 반영해 주행(EU ILIAD 프로젝트, 스웨덴 외레브로)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 창고 작업자의 위치와 현장별 사람 이동 패턴(정보) [사실][^ref-1180] |
| 수행 자원 | 자율 지게차 플릿. 2D·3D 레이저, 컬러·깊이 카메라, 안전조끼 검출 전용 카메라를 결합해 작업자를 검출·추적 [사실][^ref-1180] |
| 제약 | 움직임 지도로 학습한 사람 흐름에 맞춘 경로 계획, 움직임별 사회적 비용으로 계산한 속도 제약 [사실][^ref-1180] |
| 완료·인계 | 미확인 |
| 예외·성과 | 전원 투입부터 첫 임무까지 1시간 미만. 사람 방해·처리 시간에 대한 정량 효과는 미확인 [사실][^ref-1180] |

ILIAD 프로젝트(2021-06 종료)는 외레브로의 Orkla Foods 창고 두 곳(상온·냉장)에서 자율 지게차 플릿을 시연했다. [사실][^ref-1180] 작업자 검출·추적은 로봇 탑재 기능이므로 ROP 관점에서는 연계 대상이고, 이 영역에서 볼 부분은 현장별 사람 이동 패턴을 지도로 학습해 경로 계획에 쓴 점이다. [추정][^ref-1180]

**현장 유형:** 병원

**사례:** 병원 복도에서 운반 로봇이 낮 시간 혼잡에 대응(한림대학교성심병원, 한국)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 낮 시간 복도의 환자·휠체어와 로봇 통행 경로(사람·공간) [사실][^ref-1181] |
| 수행 자원 | 로봇 7종 73대(기사 기준) [사실][^ref-1181] |
| 제약 | 로봇 통행 경로와 작업 정지 지점에 전용 스티커 표시, 환자나 휠체어와 마주치면 로봇이 무조건 대기 [사실][^ref-1181] |
| 완료·인계 | 미확인 |
| 예외·성과 | 20개월간 서비스 35,492건(기사 기준). 대기 규칙이 처리 시간에 준 영향은 미확인 [사실][^ref-1181] |

조선비즈 기사(2024-07-12)에 따르면 이 병원은 밤에 인식한 경로가 낮의 혼잡에서는 원활하지 않을 수 있다고 보고 경로를 따로 표시했고, 로봇은 환자나 휠체어와 마주치면 “무조건 기다리도록 설계됐다”(기사 1건 기준, 독립 확인 없음). [사실][^ref-1181]

현대자동차·기아와 한림대학교의료원은 2025-04-07 한림대학교성심병원을 시험장으로 병원 맞춤형 배송 로봇과 관제 시스템을 함께 개발·실증하는 협약을 맺으면서 병원을 환자·의료진·휠체어·이동식 침대가 섞인 고밀도 환경으로 규정했지만, 이 발표는 위 기사의 로봇 대수나 사람·휠체어 앞 대기 규칙을 확인해 주지 않아 운영 규칙은 여전히 기사 1건 기준이다. [사실][^ref-1488][^ref-1181]

**현장 유형:** 병원

**사례:** 약제부에서 응급실로 의약품을 나르는 배송로봇의 승강기 혼잡 대응(고려대학교 구로병원, 한국)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 약제부→응급실 비긴급 의약품 배송 임무(2025-06-18~29, 122건) [사실][^ref-1487] |
| 작업 대상 | 의약품(물건)과, 로봇과 함께 직원 전용 승강기를 쓰는 탑승 인원(사람) [사실][^ref-1487] |
| 수행 자원 | 의약품 배송로봇 DOGU IROI(단일 기종)와 직원 전용 승강기 [사실][^ref-1487] |
| 제약 | 승강기 혼잡. 탑승 인원이 1명 늘 때 실패 오즈비 1.73이었고, 연구진은 승강기가 운행 중이며 [승강기 가동률](../../glossary/elevator-operating-rate.md)이 60% 이상이면 출발을 미루도록 권고 [사실][^ref-1487] |
| 완료·인계 | 미확인 |
| 예외·성과 | 논문 보고 성공률 87.03%(성공률 산출 기준 미확인), 승강기 가동률 59.01% 미만에서 95.52%. 실패 14건 가운데 8건이 승강기 탑승·하차 중 막힘 [사실][^ref-1487] |

Lee 외(Digital Health 12, 2026-03-31)는 단일 병원·단일 기종의 비긴급 임무 122건을 분석했고, 실패 14건은 승강기 막힘 8건, 복도 자율주행 오류 4건, 호출 통신 오류 2건이었다. [사실][^ref-1487] 성공률 87.03%는 논문 보고값이며, 논문이 분모를 밝히지 않았고 보고된 임무 122건·실패 14건과 맞지 않아 산출 기준은 미확인이다. [사실][^ref-1487] 연구진은 혼잡이 임계값 아래일 때 로봇 배송을 배정하도록 권고하면서, 59.01% 임계값은 현장 고유값이라 다른 곳에서는 다시 보정해야 한다고 적었다. [사실][^ref-1487] 승강기 운행·호출 제어는 시설·설비 제어 경계의 연계 대상이고, 이 영역에서 볼 부분은 혼잡 지표를 받아 배송의 배정·출발 시점을 정하는 일이다. [추정][^ref-1487]

**현장 유형:** 상업 시설

**사례:** 쇼핑몰에서 로봇이 주변 보행자 혼잡을 예상해 다음 이동을 계획(Kidokoro 외, IEEE Transactions on Robotics 2015)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 로봇 주변에 형성되는 군중과 그 곁을 지나가는 보행자(사람) [사실][^ref-1479] |
| 수행 자원 | 로봇과, 여러 기본 보행자 행동 모델을 결합해 가상 주행 상황을 시뮬레이션하고 그 결과로 다음 이동 단계를 고르는 계획 기능 [사실][^ref-1479] |
| 제약 | 로봇 주변 혼잡으로 지나가는 보행자의 보행 쾌적성을 해치지 않을 것 [사실][^ref-1479] |
| 완료·인계 | 미확인 |
| 예외·성과 | 실제 쇼핑몰 시험에서 혼잡으로 인한 로봇의 보행 쾌적성 영향 감소(초록 기준). 효과 수치는 미확인 [사실][^ref-1479] |

이 방법은 로봇 주변 군중 형성 예측·보행 쾌적성 추정·혼잡 사전 회피 계획을 결합해 다음 이동 단계를 고르며, 2015-11-11 발표된 저널판 초록에 따르면 실제 쇼핑몰에서 시험했다. [사실][^ref-1479] 앞선 학회판(Kidokoro 외, HRI 2013)의 초록은 보행자 흐름·보행자 상호작용·보행 쾌적성의 세 모델로 로봇이 사람 사이를 다니는 가상 상황을 시뮬레이션하는 방법을 친근한 순찰(friendly-patrolling) 시나리오에 구현했고, 현장 실험에서 노출만 최대화한 로봇보다 주변 보행자가 보행 쾌적성을 더 좋게 인식했다고 적지만 실험 장소가 쇼핑몰이라고는 밝히지 않는다(초록 기준). [사실][^ref-1182]

같은 상업 시설 유형의 ATC 데이터셋은 로봇 적용 사례가 아니라 보행자 관측 데이터셋이다. 오사카 ATC 쇼핑센터의 약 900㎡ 구역에 천장 3차원 거리 센서 49대를 두어 2012-10-24~2013-11-29 가운데 92일(매주 수·일요일 9:40~20:20) 보행자를 추적했고, 시각·사람 id·위치·높이·속도·이동 방향·몸 방향을 연구 목적으로만 제공한다. [사실][^ref-1176] 데이터셋을 공개한 ATR 연구진(Brščić 외, 2013-10-17)은 사람 키보다 높게 단 여러 3차원 거리 센서로 넓은 공공 공간에서 사람의 위치·방향·키를 추적하는 방법을 쇼핑센터에 구현했다고 보고했다(초록 기준이며, 데이터셋과 같은 저자군이라 독립 교차 확인이 아니다). [사실][^ref-1480]

**현장 유형:** 실외

**사례:** 대학 캠퍼스 보도에서 자율 배송로봇과 보행자·자전거 이용자의 상호작용 관측(노던애리조나대학교, 미국)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 보도를 함께 쓰는 보행자·자전거 이용자(사람)와 보도 공간 [사실][^ref-990] |
| 수행 자원 | 보도 자율 배송로봇(기종 미확인). 관측은 캠퍼스 10곳에서 일주일간 녹화한 현장 영상 [사실][^ref-990] |
| 제약 | 보도가 좁고 교차가 많은 지점일수록 위험 상호작용이 많았고, 심각한 충돌은 대부분 로봇이 보행자 앞을 가로지르거나 추월할 때 발생 [사실][^ref-1482] |
| 완료·인계 | 미확인 |
| 예외·성과 | 상호작용 심각도를 [침범 후 시간](../../glossary/post-encroachment-time.md)(Post-Encroachment Time, PET)으로 재고, 충돌(0초) 12건 관찰 [사실][^ref-990][^ref-1482] |

Gehrke 외(Transportation Research Interdisciplinary Perspectives 18, 2023-03-01)는 이 영상으로 보도 자율 배송로봇과 보행자·자전거 이용자의 상호작용 빈도·심각도를 침범 후 시간으로 재고, 중간·위험 충돌의 예측 요인을 모델링했다(초록 기준). [사실][^ref-990] 같은 대학의 보도(2023-05-16)에 따르면 연구진은 넓은 보도에서 나란히 주행하도록 경로를 정하고, 사람이 많은 지점의 횡단을 줄이며, 덜 붐비는 표시된 지점으로 배송하도록 권고했다(논문과 같은 기관의 보도라 독립 교차 확인이 아니다). [사실][^ref-1482] 보도 위 국소 회피·양보 동작은 로봇 제조사 몫의 연계 대상이고, ROP 쪽에서는 실외 경로망에 지점별 보행자 활동·보도 폭 속성을 두고 경로·배송 지점 선택의 비용으로 쓰는 방식으로 이어질 것으로 보이나 플랫폼 적용 사례는 확인하지 못했다. [추정][^ref-990][^ref-1482]

**현장 유형:** 기타

**사례:** 대학 건물에서 시간대별 사람 흐름을 따르는 로봇 주행(Vintr 외, 프랑스 UTBM)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 대학 건물 공간(약 500㎡)의 보행자 흐름. 2019-03 한 달간 3차원 라이다로 600만 건 이상 검출 [사실][^ref-1178] |
| 수행 자원 | 3차원 라이다(Velodyne HDL-32E) 관측과 흐름 지도를 쓰는 이동로봇(기종 미확인) [사실][^ref-1178] |
| 제약 | 시공간 흐름 지도를 쓴 경로 계획. 경로 계획 시뮬레이션에서 예상 조우(Expected Encounters)와 예상 경로 길이로 방법을 비교 [사실][^ref-1178] |
| 완료·인계 | 미확인 |
| 예외·성과 | 불편을 드러낸 사람: 예측형 주행 두 세션 모두 0명, 반응형 주행 2명·1명(40분 세션 네 번, 방법당 두 세션) [사실][^ref-1178] |

2019-12-12~13 UTBM 대학 홀 현장 실험에서 사람 흐름의 시간대 패턴을 따르는 예측형 주행은 두 세션 모두 불편을 드러낸 사람이 0명, 반응형 주행은 2명·1명이었지만, 40분 세션 네 번(방법당 두 세션)의 매우 작은 표본이며 로봇이 없는 대조 측정에서는 통행자 211명 중 불만이 0명이었다. [사실][^ref-1178]

**사례를 찾지 못한 현장 유형:** 제조 공장·가정 사례는 이번 갱신에서도 찾지 못했다. 실외의 공공 연계(행정안전부 인파관리지원시스템, 경찰청 실시간 교통신호정보 연동 시연)는 로봇 적용 사례가 아닌 연계 대상으로 9절에서, 자율주행 시뮬레이터 Waymax는 기록 재현 방법 참고로 6절에서 다룬다.

## 6. 대표 접근법과 기술

사람 위치·흐름을 계획에 반영하는 접근은 실시간 검출·추적, 장기 흐름 지도, 단기 궤적 예측, 보행자 행동 모델, 운영 규칙으로 나뉘며 효과 근거는 소규모 실험·단일 사례 중심이다. [추정][^ref-1178][^ref-1180][^ref-1181] 2026-09-30 실행에서 검증한 이 절의 상세 내용은 주제 페이지 [19. 사람·보행자 모델 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area19-s6.md)에 있다.

자세한 내용은 주제 페이지 [19. 사람·보행자 모델 — 대표 접근법과 기술](../../topics/2026/2026-10-09-area19-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

사람 표현에는 원문 상태가 Draft(2022-01-11 작성)인 ROS 규약 제안 REP-155(ROS4HRI)가 있다. [사실][^ref-1173] 2026-09-30 실행에서 검증한 이 절의 상세 내용은 주제 페이지 [19. 사람·보행자 모델 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area19-s7.md)에 있다.

자세한 내용은 주제 페이지 [19. 사람·보행자 모델 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-09-area19-s7.md)에 있다.

## 8. 대표 연구와 자료

대표 자료는 흐름 지도·궤적 예측 서베이, 고전 보행자 모델, 현장 시험 연구, 평가 지침, 기록 재현 시뮬레이터로 나뉜다. [추정][^ref-1171][^ref-1178] 2026-09-30 실행에서 검증한 이 절의 상세 내용은 주제 페이지 [19. 사람·보행자 모델 — 대표 연구와 자료](../../topics/2026/2026-09-30-area19-s8.md)에 있다.

자세한 내용은 주제 페이지 [19. 사람·보행자 모델 — 대표 연구와 자료](../../topics/2026/2026-10-09-area19-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 여러 로봇과 설비 센서가 보고한 사람 위치를 공통 좌표·시각·신뢰도로 모으고, 구역·시간대별로 집계·익명화한 사람 흐름·혼잡 모델을 유지해 경로·구역 비용, 작업 시간 추정, 배정·스케줄링에 넘긴다 [추정][^ref-1173][^ref-1178] | 로봇의 온보드 사람 검출·추적, 안전 센서 기반 감속·정지, 국소 회피(연계 대상) [추정][^ref-1180] |
| 로봇 자체 지능·제어(시설 카메라 사람 검출) | /rmf_obstacles 로 모인 사람 장애물을 층·발행 주체·수명과 함께 받아 여러 플릿의 차선 폐쇄·속도 제한 같은 교통 제약으로 바꾼다. Open-RMF lane_blocker가 오케스트레이션 계층의 예시가 될 수 있다 [추정][^ref-1484][^ref-1485] | 카메라와 사람 검출 모델 실행(단안 카메라 YOLO-V4 노드, OAK-D 칩 내 추론 노드). 센서 인식 쪽 연계 대상 [추정][^ref-1485] |
| 로봇 자체 지능·제어(운영 규칙) | 로봇에 대기·우회 같은 운영 규칙을 요청하고, 구역별 속도·진입 제한을 운영 제약으로 관리한다(49. 사람 근접 안전과 연결) [추정][^ref-1181] | 요청받은 규칙을 실제 동작으로 수행하는 로봇 제어(연계 대상) [추정][^ref-1181] |
| 시설·설비 제어 | 승강기 가동률·탑승 인원 같은 혼잡 지표를 받아 로봇 배송의 배정·출발 시점을 정한다(예: 가동률이 높고 승강기가 운행 중이면 출발 보류) [추정][^ref-1487] | 승강기 운행·호출 제어(연계 대상) [추정][^ref-1487] |
| 업종별 조건(실외 보도) | 실외 경로망에 지점별 보행자 활동·보도 폭 속성을 두고 경로·배송 지점 선택의 비용으로 쓴다(플랫폼 적용 사례 미확인) [추정][^ref-990][^ref-1482] | 보도 위 국소 회피·양보 동작(로봇 제조사, 연계 대상) [추정][^ref-1482] |
| 업종별 조건 | 공공 인파 밀집 정보를 받으면 실외 로봇의 경로·운행 제약으로 반영하는 쪽을 맡는다(연동 사례 미확인) [추정][^ref-1177] | 행정안전부 인파관리지원시스템: 2023-12-29부터 전국 중점관리지역 100곳에서 이동통신 3사 기지국 접속정보로 인파 밀집도·혼잡도를 추정하고 협소 도로 비율 같은 공간 특성을 더해 위험도를 산출해 지도에 색으로 표시하며, 위험 수준에 따라 지자체 공무원에게 경보를 보낸다(연계 대상) [사실][^ref-1177] |
| 업종별 조건(공공 교통신호) | 공공 데이터를 관제에 받아 실외 로봇 운행 판단을 보조하는 연동 지점. 교통신호 연동 시연은 있으나 인파 밀집 데이터 연동 사례는 미확인 [추정][^ref-1483][^ref-1177] | 연계 대상: 2024-08 경기 의왕시 부곡파출소 앞 횡단보도에서 경찰청 실시간 교통신호정보를 현대차·기아 로보틱스랩 관제 시스템과 연동해, 실외 이동로봇이 카메라 신호 인식과 별도로 신호 상태를 실시간으로 받아 횡단보도를 건너는 시연(기사 1건 기준) [사실][^ref-1483] |

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

사람 표현의 영속 ID 가 얼굴·음성 인식과 연결될 수 있으므로, ROP가 보관하는 사람 정보는 개인이 아니라 구역·시간대 집계로 두는 것이 이 경계를 지키는 방식으로 보인다. [추정][^ref-1173] 시설 카메라 검출을 교통 제약으로 바꾸는 경로는 오케스트레이션 계층에 이미 있지만, Open-RMF 장애물 메시지에는 검출 신뢰도 필드가 없고 REP-155는 location_confidence를 두지만 두 형식 모두 익명화·집계 규칙이 없어, 여러 출처의 사람 위치를 합치는 형식은 부분적으로만 정해진 것으로 보인다. [추정][^ref-1484][^ref-1485][^ref-1173] 경계 전체는 [범위 경계](../../about/scope-boundary.md) 페이지에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 현재 사람 위치를 다루는 18. 실시간 세계 상태·데이터 일관성과, 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈 양쪽에 걸치며 둘을 구분해 연결한다. [추정][^ref-1173][^ref-1179] 2026-09-30 실행에서 검증한 이 절의 상세 내용은 주제 페이지 [19. 사람·보행자 모델 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area19-s10.md)에 있다.

자세한 내용은 주제 페이지 [19. 사람·보행자 모델 — 다른 연구영역과의 연결](../../topics/2026/2026-10-09-area19-s10.md)에 있다.

## 11. 열린 질문

기록 재현에서 사람을 반응하게 만드는 방법과, 여러 출처의 사람 위치를 통합·익명화하는 형식은 아직 답이 없다. [추정][^ref-1128][^ref-1173] 2026-09-30 실행에서 검증한 이 절의 상세 내용(oq-261·oq-294·oq-307 서술 포함)은 주제 페이지 [19. 사람·보행자 모델 — 열린 질문](../../topics/2026/2026-09-30-area19-s11.md)에 있다.

자세한 내용은 주제 페이지 [19. 사람·보행자 모델 — 열린 질문](../../topics/2026/2026-10-09-area19-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [19. 사람·보행자 모델](people-and-pedestrian-model.md) — 영역 심화: 섹션 3~11 신규 작성(현장 유형 사례 4건: 물류창고·병원·상업 시설·기타), 13절 각주, 1차 조건부 승인 수정 16건 이행, 2차 수정: 5절 기타 사례 제약 칸을 비교 지표로 바로잡음·완료·인계 칸 두 곳 미확인·병원 서술의 검증 상태 문장 태그 제거, 7절 요약 문장을 사실·추정으로 분리 (실행 2026-09-30-20)
- 2026-09-30 · 생성 · [19. 사람·보행자 모델 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area19-s6.md) — 자동 분리: 19. 사람·보행자 모델 의 "6. 대표 접근법과 기술" 절을 옮겼다. 2차 수정: 장기 시공간 흐름 지도 첫 문장을 ref-1171 확인 범위(전형적 움직임 패턴 지도)로 고침 (실행 2026-09-30-20)
- 2026-09-30 · 생성 · [19. 사람·보행자 모델 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area19-s4.md) — 자동 분리: 19. 사람·보행자 모델 의 "4. 핵심 개념과 용어" 절을 옮겼다(2차 재실행에서 변경 없음) (실행 2026-09-30-20)
- 2026-09-30 · 생성 · [19. 사람·보행자 모델 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area19-s7.md) — 자동 분리: 19. 사람·보행자 모델 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다. 2차 수정: 요약·첫 문장을 REP-155 사실 문장과 종합 판단 추정 문장으로 나눔 (실행 2026-09-30-20)
- 2026-09-30 · 생성 · [19. 사람·보행자 모델 — 대표 연구와 자료](../../topics/2026/2026-09-30-area19-s8.md) — 자동 분리: 19. 사람·보행자 모델 의 "8. 대표 연구와 자료" 절을 옮겼다. 2차 수정: Helbing·Molnár 항목에서 '보행자 시뮬레이션에 널리 쓰이는' 삭제 (실행 2026-09-30-20)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-1171]: Kucner, T. P., Magnusson, M., Mghames, S., Palmieri, L., Verdoja, F., Swaminathan, C. S., Krajník, T., Schaffernicht, E., Bellotto, N., Hanheide, M., & Lilienthal, A. J. (The International Journal of Robotics Research 42(11)), Survey of maps of dynamics for mobile robots, 2023-09, https://journals.sagepub.com/doi/10.1177/02783649231190428, 접근일 2026-10-09
[^ref-1172]: Rudenko, A., Palmieri, L., Herman, M., Kitani, K. M., Gavrila, D. M., & Arras, K. O. (arXiv; IJRR 39(8), 2020), Human Motion Trajectory Prediction: A Survey, 2019-12-17, https://arxiv.org/abs/1905.06113, 접근일 2026-09-30
[^ref-1173]: ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan, REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction, 2022-01-11, https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst, 접근일 2026-10-09
[^ref-1174]: Helbing, D., & Molnár, P. (Physical Review E 51(5)), Social force model for pedestrian dynamics, 1995-05-01, https://link.aps.org/doi/10.1103/PhysRevE.51.4282, 접근일 2026-09-30 (원문 미열람)
[^ref-1176]: ATR (Advanced Telecommunications Research Institute International), Brščić, D. 외, ATC shopping center tracking dataset, 미확인, https://dil.atr.jp/crest2010_HRI/ATC_dataset/, 접근일 2026-09-30
[^ref-1177]: 행정안전부 (대한민국 정책브리핑), 29일부터 인파관리지원시스템 본격 운영…다중운집 인파사고 예방, 2023-12-27, https://www.korea.kr/news/policyNewsView.do?newsId=148924176, 접근일 2026-09-30
[^ref-1178]: Vintr, T., Blaha, J., Rektoris, M., Ulrich, J., Rouček, T., Broughton, G., Yan, Z., & Krajník, T. (Frontiers in Robotics and AI), Toward Benchmarking of Long-Term Spatio-Temporal Maps of Pedestrian Flows for Human-Aware Navigation, 2022-07-04, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.890013/full, 접근일 2026-09-30
[^ref-1179]: Pérez-Higueras, N., Otero, R., Caballero, F., & Merino, L. (arXiv; IEEE RA-L 2023), HuNavSim: A ROS 2 Human Navigation Simulator for Benchmarking Human-Aware Robot Navigation, 2023-09-13, https://arxiv.org/abs/2305.01303, 접근일 2026-09-30
[^ref-1180]: ILIAD 프로젝트 컨소시엄 (EU Horizon 2020), Concluding ILIAD, 2021-06, https://iliad-project.eu/concluding-iliad/, 접근일 2026-09-30
[^ref-1128]: Gulino, C., Fu, J., Luo, W. 외 (Waymo; arXiv), Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research, 2023-10-12, https://arxiv.org/abs/2310.08710, 접근일 2026-09-30
[^ref-1181]: 조선비즈 (이정아, 다음 뉴스 게재), 로봇과 인간이 공존하는 병원…약 배달 로봇에 길 비켜주고 엘리베이터도 잡아줘, 2024-07-12, https://v.daum.net/v/bc4riunbUE, 접근일 2026-09-30
[^ref-1182]: Kidokoro, H., Kanda, T., Brščić, D., & Shiomi, M. (ACM/IEEE HRI 2013), Will I bother here? - A robot anticipating its influence on pedestrian walking comfort, 2013-03, https://www.semanticscholar.org/paper/Will-I-bother-here-A-robot-anticipating-its-on-Kidokoro-Kanda/bc0b26f1c13405fd89eb6d280bee739aed5b07a6, 접근일 2026-10-09
[^ref-1479]: Kidokoro, H., Kanda, T., Brščić, D., & Shiomi, M. (IEEE Transactions on Robotics 31(6)), Simulation-Based Behavior Planning to Prevent Congestion of Pedestrians Around a Robot, 2015-11-11, https://doi.org/10.1109/TRO.2015.2492862, 접근일 2026-10-09
[^ref-1480]: Brščić, D., Kanda, T., Ikeda, T., & Miyashita, T. (IEEE Transactions on Human-Machine Systems 43(6)), Person Tracking in Large Public Spaces Using 3-D Range Sensors, 2013-10-17, https://doi.org/10.1109/THMS.2013.2283945, 접근일 2026-10-09
[^ref-990]: Gehrke, S. R., Phair, C. D., Russo, B. J., & Smaglik, E. J. (Transportation Research Interdisciplinary Perspectives 18), Observed sidewalk autonomous delivery robot interactions with pedestrians and bicyclists, 2023-03-01, https://doi.org/10.1016/j.trip.2023.100789, 접근일 2026-10-09
[^ref-1482]: Northern Arizona University (NAU Review), Got robot delivery? New research demonstrates need for robot-friendly infrastructure, 2023-05-16, https://in.nau.edu/news/delivery-robot-research/, 접근일 2026-10-09
[^ref-1483]: 보안뉴스 (박미영), 경찰청 제공 실시간 교통신호정보, 보행자와 함께 거닐 실외 이동로봇의 눈이 되다, 2024-08-10, https://www.boannews.com/news/articleView.html?idxno=131956, 접근일 2026-10-09
[^ref-1484]: Open Robotics (open-rmf/rmf_internal_msgs), rmf_obstacle_msgs/msg/Obstacle.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_obstacle_msgs/msg/Obstacle.msg, 접근일 2026-10-09
[^ref-1485]: Open Robotics (open-rmf/rmf_obstacle), rmf_obstacle — README, 미확인, https://github.com/open-rmf/rmf_obstacle, 접근일 2026-10-09
[^ref-1487]: Lee, Y. 외, Park, I.-H. (교신) (Digital Health 12, 고려대학교 구로병원), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://journals.sagepub.com/doi/10.1177/20552076261437181, 접근일 2026-10-09
[^ref-1488]: 현대자동차그룹, 현대자동차·기아, 한림대의료원과 로봇 친화 병원 공동 구축 위한 업무협약 체결, 2025-04-07, https://www.hyundaimotorgroup.com/ko/news/CONT0000000000173736, 접근일 2026-10-09
```

### docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md

```markdown
---
title: "19. 사람·보행자 모델"
type: area
category: "E. 사물·사람·실시간 상태"
area_no: 19
related_areas: [15, 16, 18, 26, 27, 31, 34, 36, 46, 49, 53, 54, 61, 63, 64, 66]
tags: [움직임 지도, 사람 궤적 예측, 사회적 힘 모델, 사회적 내비게이션, ROS4HRI]
status: published
confidence: low
created: 2026-09-28
updated: 2026-09-30
sources: [ref-1171, ref-1172, ref-1173, ref-1174, ref-1175, ref-1176, ref-1177, ref-1178, ref-1079, ref-1179, ref-406, ref-1180, ref-1128, ref-1181, ref-1182]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [E. 사물·사람·실시간 상태](index.md) › 19. 사람·보행자 모델

# 19. 사람·보행자 모델

!!! info "소속 대분류"
    [E. 사물·사람·실시간 상태](index.md) — 핵심 질문:
    작업 대상·사람·설비·로봇이 지금 어디에 어떤 상태로 있는지 어떻게 믿을 수 있게 알 것인가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: low · 페이지 버전: 2 · 마지막 갱신: 2026-09-30 · 마지막 실행: 2026-09-30
<!-- auto:page-status:end -->

## 1. 한 줄 정의

현장 사람의 위치·흐름·혼잡을 모델링해 계획과 안전에 쓴다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **사람·보행자 모델**: 현장 사람의 위치·목적지·멈춤·교차를 모델링해 로봇 계획과 안전에 반영한다
- **사람 흐름·혼잡 추정**: 시간대·구역별 사람의 흐름과 혼잡을 추정해 경로와 작업 시간에 반영한다

## 2. 핵심 질문

현장 사람의 위치와 흐름을 어떻게 알고 계획과 안전에 반영할 것인가? [분류원문]

## 3. 왜 중요한가

확인한 자료를 종합하면, 현장 사람의 위치와 흐름은 로봇 탑재·천장 센서로 사람을 실시간 검출·추적하고, 장기 관측으로 시간대별 흐름 지도(움직임 지도)를 학습하며, 궤적 예측·보행자 행동 모델로 가까운 미래와 가상 상황을 추정해 경로 비용·속도 제약·혼잡 회피·운영 규칙(전용 통로, 무조건 대기)으로 계획과 안전에 반영된다. [추정][^ref-1171][^ref-1172][^ref-1178][^ref-1180]

자세한 내용은 주제 페이지 [19. 사람·보행자 모델 — 왜 중요한가](../../topics/2026/2026-09-30-area19-s3.md)에 있다.

## 4. 핵심 개념과 용어

이 영역의 핵심 개념은 사람 흐름을 저장하는 지도, 가까운 미래 경로를 추정하는 예측, 보행자 행동을 계산하는 모델, 사람 정보를 주고받는 표현 규약이다. [추정][^ref-1171][^ref-1172][^ref-1174][^ref-1173]

자세한 내용은 주제 페이지 [19. 사람·보행자 모델 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area19-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

근거를 찾은 네 현장 유형(물류창고·병원·상업 시설·기타)의 사례를 나눠 적는다. 현장 유형 × 대분류 적용 사례는 [현장 유형 매트릭스](../../site-matrix.md)에 모인다.

**현장 유형:** 물류창고

**사례:** 창고 자율 지게차 플릿이 작업자 이동 패턴을 반영해 주행(EU ILIAD 프로젝트, 스웨덴 외레브로)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 창고 작업자의 위치와 현장별 사람 이동 패턴(정보) [사실][^ref-1180] |
| 수행 자원 | 자율 지게차 플릿. 2D·3D 레이저, 컬러·깊이 카메라, 안전조끼 검출 전용 카메라를 결합해 작업자를 검출·추적 [사실][^ref-1180] |
| 제약 | 움직임 지도로 학습한 사람 흐름에 맞춘 경로 계획, 움직임별 사회적 비용으로 계산한 속도 제약 [사실][^ref-1180] |
| 완료·인계 | 미확인 |
| 예외·성과 | 전원 투입부터 첫 임무까지 1시간 미만. 사람 방해·처리 시간에 대한 정량 효과는 미확인 [사실][^ref-1180] |

ILIAD 프로젝트(2021-06 종료)는 외레브로의 Orkla Foods 창고 두 곳(상온·냉장)에서 자율 지게차 플릿을 시연했다. [사실][^ref-1180] 작업자 검출·추적은 로봇 탑재 기능이므로 ROP 관점에서는 연계 대상이고, 이 영역에서 볼 부분은 현장별 사람 이동 패턴을 지도로 학습해 경로 계획에 쓴 점이다. [추정][^ref-1180]

**현장 유형:** 병원

**사례:** 병원 복도에서 운반 로봇이 낮 시간 혼잡에 대응(한림대학교성심병원, 한국)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 낮 시간 복도의 환자·휠체어와 로봇 통행 경로(사람·공간) [사실][^ref-1181] |
| 수행 자원 | 로봇 7종 73대(기사 기준) [사실][^ref-1181] |
| 제약 | 로봇 통행 경로와 작업 정지 지점에 전용 스티커 표시, 환자나 휠체어와 마주치면 로봇이 무조건 대기 [사실][^ref-1181] |
| 완료·인계 | 미확인 |
| 예외·성과 | 20개월간 서비스 35,492건(기사 기준). 대기 규칙이 처리 시간에 준 영향은 미확인 [사실][^ref-1181] |

조선비즈 기사(2024-07-12)에 따르면 이 병원은 밤에 인식한 경로가 낮의 혼잡에서는 원활하지 않을 수 있다고 보고 경로를 따로 표시했고, 로봇은 환자나 휠체어와 마주치면 “무조건 기다리도록 설계됐다”(기사 1건 기준, 독립 확인 없음). [사실][^ref-1181]

**현장 유형:** 상업 시설

**사례:** 쇼핑몰에서 사람을 모으는 로봇이 보행자 혼잡을 예상해 위치를 계획(Kidokoro 외, HRI 2013)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 로봇 주변을 지나가는 보행자와 그 흐름(사람) [사실][^ref-1182] |
| 수행 자원 | 사람을 모으는 로봇과, 보행자 행동 모델로 가상 주행 상황을 시뮬레이션하는 계획 기능 [사실][^ref-1182] |
| 제약 | 로봇이 모은 사람 때문에 생기는 혼잡으로 지나가는 보행자의 보행 쾌적성을 해치지 않을 것 [사실][^ref-1182] |
| 완료·인계 | 미확인 |
| 예외·성과 | 노출만 최대화한 로봇에 비해 주변 보행자가 보행 쾌적성을 더 좋게 인식. 효과 수치는 미확인 [사실][^ref-1182] |

이 연구는 혼잡을 예상하고 미리 피하도록 계획하는 방법을 실제 쇼핑몰에서 시험했다(원문 미열람, 검색 결과 기준). [사실][^ref-1182] 같은 상업 시설 유형의 ATC 데이터셋은 로봇 적용 사례가 아니라 보행자 관측 데이터셋이다. 오사카 ATC 쇼핑센터의 약 900㎡ 구역에 천장 3차원 거리 센서 49대를 두어 2012-10-24~2013-11-29 가운데 92일(매주 수·일요일 9:40~20:20) 보행자를 추적했고, 시각·사람 id·위치·높이·속도·이동 방향·몸 방향을 연구 목적으로만 제공한다. [사실][^ref-1176]

**현장 유형:** 기타

**사례:** 대학 건물에서 시간대별 사람 흐름을 따르는 로봇 주행(Vintr 외, 프랑스 UTBM)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 미확인 |
| 작업 대상 | 대학 건물 공간(약 500㎡)의 보행자 흐름. 2019-03 한 달간 3차원 라이다로 600만 건 이상 검출 [사실][^ref-1178] |
| 수행 자원 | 3차원 라이다(Velodyne HDL-32E) 관측과 흐름 지도를 쓰는 이동로봇(기종 미확인) [사실][^ref-1178] |
| 제약 | 시공간 흐름 지도를 쓴 경로 계획. 경로 계획 시뮬레이션에서 예상 조우(Expected Encounters)와 예상 경로 길이로 방법을 비교 [사실][^ref-1178] |
| 완료·인계 | 미확인 |
| 예외·성과 | 불편을 드러낸 사람: 예측형 주행 두 세션 모두 0명, 반응형 주행 2명·1명(40분 세션 네 번, 방법당 두 세션) [사실][^ref-1178] |

2019-12-12~13 UTBM 대학 홀 현장 실험에서 사람 흐름의 시간대 패턴을 따르는 예측형 주행은 두 세션 모두 불편을 드러낸 사람이 0명, 반응형 주행은 2명·1명이었지만, 40분 세션 네 번(방법당 두 세션)의 매우 작은 표본이며 로봇이 없는 대조 측정에서는 통행자 211명 중 불만이 0명이었다. [사실][^ref-1178]

**사례를 찾지 못한 현장 유형:** 실외에서는 이 영역의 로봇 적용 사례를 찾지 못했다. 행정안전부 인파관리지원시스템은 로봇 사례가 아닌 연계 대상으로 9절에서, 자율주행 시뮬레이터 Waymax는 기록 재현 방법 참고로 6절에서 다룬다. 제조 공장·가정 사례도 찾지 못했다.

## 6. 대표 접근법과 기술

사람 위치·흐름을 계획에 반영하는 접근은 실시간 검출·추적, 장기 흐름 지도, 단기 궤적 예측, 보행자 행동 모델, 운영 규칙으로 나뉘며 효과 근거는 소규모 실험·단일 사례 중심이다. [추정][^ref-1178][^ref-1180][^ref-1181]

자세한 내용은 주제 페이지 [19. 사람·보행자 모델 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area19-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

사람 표현에는 원문 상태가 Draft(2022-01-11 작성)인 ROS 규약 제안 REP-155(ROS4HRI)가 있다. [사실][^ref-1173] 보행자 시뮬레이션·데이터셋·평가 지침은 오픈소스와 연구 자료 중심이다. [추정][^ref-1179]

자세한 내용은 주제 페이지 [19. 사람·보행자 모델 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area19-s7.md)에 있다.

## 8. 대표 연구와 자료

대표 자료는 흐름 지도·궤적 예측 서베이, 고전 보행자 모델, 현장 시험 연구, 평가 지침, 기록 재현 시뮬레이터로 나뉜다. [추정][^ref-1171][^ref-1178]

자세한 내용은 주제 페이지 [19. 사람·보행자 모델 — 대표 연구와 자료](../../topics/2026/2026-09-30-area19-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 여러 로봇과 설비 센서가 보고한 사람 위치를 공통 좌표·시각·신뢰도로 모으고, 구역·시간대별로 집계·익명화한 사람 흐름·혼잡 모델을 유지해 경로·구역 비용, 작업 시간 추정, 배정·스케줄링에 넘긴다 [추정][^ref-1173][^ref-1178] | 로봇의 온보드 사람 검출·추적, 안전 센서 기반 감속·정지, 국소 회피(연계 대상) [추정][^ref-1180] |
| 로봇 자체 지능·제어(운영 규칙) | 로봇에 대기·우회 같은 운영 규칙을 요청하고, 구역별 속도·진입 제한을 운영 제약으로 관리한다(49. 사람 근접 안전과 연결) [추정][^ref-1181] | 요청받은 규칙을 실제 동작으로 수행하는 로봇 제어(연계 대상) [추정][^ref-1181] |
| 업종별 조건 | 공공 인파 밀집 정보를 받으면 실외 로봇의 경로·운행 제약으로 반영하는 쪽을 맡는다(연동 사례 미확인) [추정][^ref-1177] | 행정안전부 인파관리지원시스템: 2023-12-29부터 전국 중점관리지역 100곳에서 이동통신 3사 기지국 접속정보로 인파 밀집도·혼잡도를 추정하고 협소 도로 비율 같은 공간 특성을 더해 위험도를 산출해 지도에 색으로 표시하며, 위험 수준에 따라 지자체 공무원에게 경보를 보낸다(연계 대상) [사실][^ref-1177] |

이 경계는 제품 전략에 따라 이동할 수 있다. 자사 로봇까지 만드는 회사는 로컬 주행을 포함할 수 있지만, **이종 제조사를 연결하는 ROP는 그 기능을 제조사에 맡기고 인터페이스와 실행 보장을 담당할 수 있다.** [분류원문]

사람 표현의 영속 ID 가 얼굴·음성 인식과 연결될 수 있으므로, ROP가 보관하는 사람 정보는 개인이 아니라 구역·시간대 집계로 두는 것이 이 경계를 지키는 방식으로 보인다. [추정][^ref-1173] 경계 전체는 [범위 경계](../../about/scope-boundary.md) 페이지에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 현재 사람 위치를 다루는 18. 실시간 세계 상태·데이터 일관성과, 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈 양쪽에 걸치며 둘을 구분해 연결한다. [추정][^ref-1173][^ref-1179]

자세한 내용은 주제 페이지 [19. 사람·보행자 모델 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area19-s10.md)에 있다.

## 11. 열린 질문

기록 재현에서 사람을 반응하게 만드는 방법과, 여러 출처의 사람 위치를 통합·익명화하는 형식은 아직 답이 없다. [추정][^ref-1128][^ref-1173]

자세한 내용은 주제 페이지 [19. 사람·보행자 모델 — 열린 질문](../../topics/2026/2026-09-30-area19-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [19. 사람·보행자 모델](people-and-pedestrian-model.md) — 영역 심화: 섹션 3~11 신규 작성(현장 유형 사례 4건: 물류창고·병원·상업 시설·기타), 13절 각주, 1차 조건부 승인 수정 16건 이행, 2차 수정: 5절 기타 사례 제약 칸을 비교 지표로 바로잡음·완료·인계 칸 두 곳 미확인·병원 서술의 검증 상태 문장 태그 제거, 7절 요약 문장을 사실·추정으로 분리 (실행 2026-09-30-20)
- 2026-09-30 · 생성 · [19. 사람·보행자 모델 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area19-s6.md) — 자동 분리: 19. 사람·보행자 모델 의 "6. 대표 접근법과 기술" 절을 옮겼다. 2차 수정: 장기 시공간 흐름 지도 첫 문장을 ref-1171 확인 범위(전형적 움직임 패턴 지도)로 고침 (실행 2026-09-30-20)
- 2026-09-30 · 생성 · [19. 사람·보행자 모델 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area19-s4.md) — 자동 분리: 19. 사람·보행자 모델 의 "4. 핵심 개념과 용어" 절을 옮겼다(2차 재실행에서 변경 없음) (실행 2026-09-30-20)
- 2026-09-30 · 생성 · [19. 사람·보행자 모델 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area19-s7.md) — 자동 분리: 19. 사람·보행자 모델 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다. 2차 수정: 요약·첫 문장을 REP-155 사실 문장과 종합 판단 추정 문장으로 나눔 (실행 2026-09-30-20)
- 2026-09-30 · 생성 · [19. 사람·보행자 모델 — 대표 연구와 자료](../../topics/2026/2026-09-30-area19-s8.md) — 자동 분리: 19. 사람·보행자 모델 의 "8. 대표 연구와 자료" 절을 옮겼다. 2차 수정: Helbing·Molnár 항목에서 '보행자 시뮬레이션에 널리 쓰이는' 삭제 (실행 2026-09-30-20)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-1171]: Kucner, T. P., Magnusson, M., Mghames, S., Palmieri, L., Verdoja, F., Swaminathan, C. S., Krajník, T., Schaffernicht, E., Bellotto, N., Hanheide, M., & Lilienthal, A. J. (The International Journal of Robotics Research 42(11)), Survey of maps of dynamics for mobile robots, 2023, https://journals.sagepub.com/doi/10.1177/02783649231190428, 접근일 2026-09-30 (원문 미열람)
[^ref-1172]: Rudenko, A., Palmieri, L., Herman, M., Kitani, K. M., Gavrila, D. M., & Arras, K. O. (arXiv; IJRR 39(8), 2020), Human Motion Trajectory Prediction: A Survey, 2019-12-17, https://arxiv.org/abs/1905.06113, 접근일 2026-09-30
[^ref-1173]: ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan, REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction, 2022-01-11, https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst, 접근일 2026-09-30
[^ref-1174]: Helbing, D., & Molnár, P. (Physical Review E 51(5)), Social force model for pedestrian dynamics, 1995-05-01, https://link.aps.org/doi/10.1103/PhysRevE.51.4282, 접근일 2026-09-30 (원문 미열람)
[^ref-1176]: ATR (Advanced Telecommunications Research Institute International), Brščić, D. 외, ATC shopping center tracking dataset, 미확인, https://dil.atr.jp/crest2010_HRI/ATC_dataset/, 접근일 2026-09-30
[^ref-1177]: 행정안전부 (대한민국 정책브리핑), 29일부터 인파관리지원시스템 본격 운영…다중운집 인파사고 예방, 2023-12-27, https://www.korea.kr/news/policyNewsView.do?newsId=148924176, 접근일 2026-09-30
[^ref-1178]: Vintr, T., Blaha, J., Rektoris, M., Ulrich, J., Rouček, T., Broughton, G., Yan, Z., & Krajník, T. (Frontiers in Robotics and AI), Toward Benchmarking of Long-Term Spatio-Temporal Maps of Pedestrian Flows for Human-Aware Navigation, 2022-07-04, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.890013/full, 접근일 2026-09-30
[^ref-1179]: Pérez-Higueras, N., Otero, R., Caballero, F., & Merino, L. (arXiv; IEEE RA-L 2023), HuNavSim: A ROS 2 Human Navigation Simulator for Benchmarking Human-Aware Robot Navigation, 2023-09-13, https://arxiv.org/abs/2305.01303, 접근일 2026-09-30
[^ref-1180]: ILIAD 프로젝트 컨소시엄 (EU Horizon 2020), Concluding ILIAD, 2021-06, https://iliad-project.eu/concluding-iliad/, 접근일 2026-09-30
[^ref-1128]: Gulino, C., Fu, J., Luo, W. 외 (Waymo; arXiv), Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research, 2023-10-12, https://arxiv.org/abs/2310.08710, 접근일 2026-09-30
[^ref-1181]: 조선비즈 (이정아, 다음 뉴스 게재), 로봇과 인간이 공존하는 병원…약 배달 로봇에 길 비켜주고 엘리베이터도 잡아줘, 2024-07-12, https://v.daum.net/v/bc4riunbUE, 접근일 2026-09-30
[^ref-1182]: Kidokoro, H., Kanda, T., Brščić, D., & Shiomi, M. (ACM/IEEE HRI 2013), Will I bother here? - A robot anticipating its influence on pedestrian walking comfort, 2013-03, https://www.semanticscholar.org/paper/Will-I-bother-here-A-robot-anticipating-its-on-Kidokoro-Kanda/bc0b26f1c13405fd89eb6d280bee739aed5b07a6, 접근일 2026-09-30 (원문 미열람)
```

### runs/2026-10-09-12/pages/topics/2026/2026-10-09-area19-s6.md

```markdown
---
title: "19. 사람·보행자 모델 — 대표 접근법과 기술"
type: topic
category: "E. 사물·사람·실시간 상태"
primary_area_no: 19
related_areas: [15, 16, 18, 22, 25, 26, 27, 31, 34, 36, 46, 49, 53, 54, 61, 63, 64, 66]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-1083, ref-1178, ref-1180, ref-1181, ref-1485, ref-1486, ref-1487, ref-1489]
last_run: 2026-10-09
version: 1
split_from: docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#6
---

[홈](../../index.md) › [주제](../index.md) › 19. 사람·보행자 모델 — 대표 접근법과 기술

# 19. 사람·보행자 모델 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 사람 위치·흐름을 계획에 반영하는 접근은 실시간 검출·추적, 장기 흐름 지도, 단기 궤적 예측, 보행자 행동 모델, 운영 규칙으로 나뉘며 효과 근거는 소규모 실험·단일 사례 중심이다. [추정][^ref-1178][^ref-1180][^ref-1181] 2026-09-30 실행에서 검증한 이 절의 상세 내용은 주제 페이지 [19. 사람·보행자 모델 — 대표 접근법과 기술](2026-09-30-area19-s6.md)에 있다.
- 이 페이지는 [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

사람 위치·흐름을 계획에 반영하는 접근은 실시간 검출·추적, 장기 흐름 지도, 단기 궤적 예측, 보행자 행동 모델, 운영 규칙으로 나뉘며 효과 근거는 소규모 실험·단일 사례 중심이다. [추정][^ref-1178][^ref-1180][^ref-1181] 2026-09-30 실행에서 검증한 이 절의 상세 내용은 주제 페이지 [19. 사람·보행자 모델 — 대표 접근법과 기술](2026-09-30-area19-s6.md)에 있다.

### 2026-10-09 갱신에서 더한 접근

**시설 카메라 사람 검출을 교통 제약으로.** Open-RMF의 rmf_obstacle 저장소는 기존 CCTV 영상으로 군중을 검출하는 용도의 단안 카메라 사람 검출 노드(rmf_human_detector, YOLO-V4)와, 이와 별도로 OAK-D 카메라의 칩 내 추론(MobileNet-SSD) 검출 노드를 둔다. lane_blocker 노드는 /rmf_obstacles 의 장애물이 플릿 주행 차선과 겹치면 차선을 닫았다가 비면 다시 열거나 속도 제한(기본 0.5 m/s)을 건다(확인일 2026-10-09). [사실][^ref-1485] 사람 검출 모델 실행과 카메라는 센서 인식 쪽 연계 대상이고, ROP 쪽 접근은 모인 장애물을 [차선 폐쇄](../../glossary/lane-closure.md)·속도 제한 같은 교통 제약으로 바꾸는 부분이며, 이 관측은 현재 상태이므로 18. 실시간 세계 상태·데이터 일관성 쪽에 놓인다. [추정][^ref-1485]

**움직임 지도를 작업 배정 비용에.** Kazemi Eskeri 외(IROS 2025, arXiv 2025-08-27)는 시간대별 사람 존재 확률을 담은 이산 격자형 [움직임 지도](../../glossary/maps-of-dynamics.md)를 다중 로봇 작업 배정의 확률적 비용에 넣어, 임무 완료 시간을 움직임 무시 방법 대비 최대 26%, 기준 방법 대비 최대 19% 줄였다고 보고했다. [사실][^ref-1083] 이 수치는 ATC 쇼핑몰 데이터의 기록 궤적을 재생한 시뮬레이션 결과이며 실제 로봇 실험은 없다. [사실][^ref-1083]

**장기 사람 움직임 예측.** Zhu 외(arXiv 2025-10-03, IEEE RA-L 표기)는 시간대별 움직임 패턴을 담은 시간 조건부 움직임 지도로 최대 60초 앞의 사람 움직임을 예측해, 실제 데이터셋 두 개에서 학습 기반 방법보다 평균 변위 오차(Average Displacement Error, ADE)를 최대 50% 줄였다고 보고했다(데이터셋 이름 미확인). [사실][^ref-1489] Kairos(Catalano 외, 2026-09-23)는 [3차원 장면 그래프](../../glossary/3d-scene-graph.md)의 복셀마다 사람 존재율과 이동 방향 분포를 두고 임의의 미래 시각을 예측해 주행 노드 단위로 모으는 4차원 장면 그래프를 제안했고, 캠퍼스·쇼핑몰·11개월 역 구내 데이터로 평가해 사람을 만나는 계획 과제에서 시간 불변 지도보다 같은 성공률로 더 많은 사람을 만났다고 보고했다(동료심사 전 프리프린트). [사실][^ref-1486] 이런 학습·예측 결과를 배정·경로 비용에 넣는 방법은 46. 예측·학습 기반 최적화와 25. 작업 배정 — MRTA 양쪽에 걸친다. [추정][^ref-1083][^ref-1489]

**혼잡 지표로 배정·출발 시점 조정.** 병원 사례에서는 혼잡이 임계값 아래일 때 배송을 배정하고, 승강기가 운행 중이며 [승강기 가동률](../../glossary/elevator-operating-rate.md)이 60% 이상이면 출발을 미루라는 권고가 나왔다(단일 병원·단일 기종, 임계값은 현장 고유값). [사실][^ref-1487] ROP 쪽에서는 이 혼잡 지표를 받아 배정·출발 시점을 정하는 부분을 맡고, 승강기 운행·호출 제어는 연계 대상으로 남는 것으로 보인다. [추정][^ref-1487]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md)
- 관련 영역: [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1083]: Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv), Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments, 2025-08-27, https://arxiv.org/abs/2508.19731, 접근일 2026-10-09
[^ref-1178]: Vintr, T., Blaha, J., Rektoris, M., Ulrich, J., Rouček, T., Broughton, G., Yan, Z., & Krajník, T. (Frontiers in Robotics and AI), Toward Benchmarking of Long-Term Spatio-Temporal Maps of Pedestrian Flows for Human-Aware Navigation, 2022-07-04, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.890013/full, 접근일 2026-09-30
[^ref-1180]: ILIAD 프로젝트 컨소시엄 (EU Horizon 2020), Concluding ILIAD, 2021-06, https://iliad-project.eu/concluding-iliad/, 접근일 2026-09-30
[^ref-1181]: 조선비즈 (이정아, 다음 뉴스 게재), 로봇과 인간이 공존하는 병원…약 배달 로봇에 길 비켜주고 엘리베이터도 잡아줘, 2024-07-12, https://v.daum.net/v/bc4riunbUE, 접근일 2026-09-30
[^ref-1485]: Open Robotics (open-rmf/rmf_obstacle), rmf_obstacle — README, 미확인, https://github.com/open-rmf/rmf_obstacle, 접근일 2026-10-09
[^ref-1486]: Catalano, I., Placed, J. A., Civera, J., & Peña Queralta, J. (arXiv), Kairos: Grounded Forecasting of Presence and Directional Flow in 4D Scene Graphs, 2026-09-23, https://arxiv.org/abs/2609.27467, 접근일 2026-10-09
[^ref-1487]: Lee, Y. 외, Park, I.-H. (교신) (Digital Health 12, 고려대학교 구로병원), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://journals.sagepub.com/doi/10.1177/20552076261437181, 접근일 2026-10-09
[^ref-1489]: Zhu, Y., Rudenko, A., Kucner, T. P., Lilienthal, A. J., & Magnusson, M. (arXiv; IEEE RA-L 표기), Long-Term Human Motion Prediction Using Spatio-Temporal Maps of Dynamics, 2025-10-03, https://arxiv.org/abs/2510.03031, 접근일 2026-10-09

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-09-12 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-09 | 2026-10-09-12 | 19. 사람·보행자 모델 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-10-09-12/pages/topics/2026/2026-10-09-area19-s8.md

```markdown
---
title: "19. 사람·보행자 모델 — 대표 연구와 자료"
type: topic
category: "E. 사물·사람·실시간 상태"
primary_area_no: 19
related_areas: [15, 16, 18, 22, 25, 26, 27, 31, 34, 36, 46, 49, 53, 54, 61, 63, 64, 66]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-1083, ref-1171, ref-1178, ref-1479, ref-1480, ref-1486, ref-1487, ref-1489, ref-990]
last_run: 2026-10-09
version: 1
split_from: docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#8
---

[홈](../../index.md) › [주제](../index.md) › 19. 사람·보행자 모델 — 대표 연구와 자료

# 19. 사람·보행자 모델 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 대표 자료는 흐름 지도·궤적 예측 서베이, 고전 보행자 모델, 현장 시험 연구, 평가 지침, 기록 재현 시뮬레이터로 나뉜다. [추정][^ref-1171][^ref-1178] 2026-09-30 실행에서 검증한 이 절의 상세 내용은 주제 페이지 [19. 사람·보행자 모델 — 대표 연구와 자료](2026-09-30-area19-s8.md)에 있다.
- 이 페이지는 [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

대표 자료는 흐름 지도·궤적 예측 서베이, 고전 보행자 모델, 현장 시험 연구, 평가 지침, 기록 재현 시뮬레이터로 나뉜다. [추정][^ref-1171][^ref-1178] 2026-09-30 실행에서 검증한 이 절의 상세 내용은 주제 페이지 [19. 사람·보행자 모델 — 대표 연구와 자료](2026-09-30-area19-s8.md)에 있다.

### 2026-10-09 갱신에서 더한 자료

- Kucner 외, Survey of maps of dynamics for mobile robots(IJRR 42(11), 2023-09) — 초록 기준으로 움직임 지도를 환경의 전형적 움직임 패턴을 기록한 지도로 정의하고 새 분류 체계를 제안하며, 이 분야가 실제 적용에 이를 만큼 성숙했지만 빠르게 발전 중이라고 결론짓는다(본문 미열람). [사실][^ref-1171]
- Kidokoro 외, Simulation-Based Behavior Planning to Prevent Congestion of Pedestrians Around a Robot(IEEE Transactions on Robotics 31(6), 2015) — 혼잡 사전 회피 계획을 실제 쇼핑몰에서 시험한 저널판이다(초록 기준, 5절 상업 시설 사례). [사실][^ref-1479]
- Brščić 외, Person Tracking in Large Public Spaces Using 3-D Range Sensors(IEEE THMS 43(6), 2013) — 사람 키보다 높게 단 여러 3차원 거리 센서로 쇼핑센터의 사람 위치·방향·키를 추적한 방법이다(초록 기준). [사실][^ref-1480]
- Kazemi Eskeri 외, Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments(IROS 2025) — 움직임 지도를 작업 배정 비용에 넣은 연구이며 결과는 기록 궤적 재생 시뮬레이션이다. [사실][^ref-1083]
- Zhu 외, Long-Term Human Motion Prediction Using Spatio-Temporal Maps of Dynamics(2025) — 시간 조건부 움직임 지도로 최대 60초 앞을 예측한다(데이터셋 이름 미확인). [사실][^ref-1489]
- Catalano 외, Kairos(2026) — 4차원 장면 그래프로 사람 존재·흐름을 예측하는 동료심사 전 프리프린트이며 코드가 공개돼 있다. [사실][^ref-1486]
- Lee 외, Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments(Digital Health 12, 2026) — 고려대학교 구로병원 의약품 배송로봇의 승강기 혼잡과 실패를 분석한 단일 병원 연구다(5절 병원 사례). [사실][^ref-1487]
- Gehrke 외, Observed sidewalk autonomous delivery robot interactions with pedestrians and bicyclists(2023) — 대학 캠퍼스 보도 배송로봇과 보행자의 상호작용을 침범 후 시간으로 분석한 현장 관측 연구다(5절 실외 사례). [사실][^ref-990]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md)
- 관련 영역: [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1083]: Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv), Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments, 2025-08-27, https://arxiv.org/abs/2508.19731, 접근일 2026-10-09
[^ref-1171]: Kucner, T. P., Magnusson, M., Mghames, S., Palmieri, L., Verdoja, F., Swaminathan, C. S., Krajník, T., Schaffernicht, E., Bellotto, N., Hanheide, M., & Lilienthal, A. J. (The International Journal of Robotics Research 42(11)), Survey of maps of dynamics for mobile robots, 2023-09, https://journals.sagepub.com/doi/10.1177/02783649231190428, 접근일 2026-10-09
[^ref-1178]: Vintr, T., Blaha, J., Rektoris, M., Ulrich, J., Rouček, T., Broughton, G., Yan, Z., & Krajník, T. (Frontiers in Robotics and AI), Toward Benchmarking of Long-Term Spatio-Temporal Maps of Pedestrian Flows for Human-Aware Navigation, 2022-07-04, https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.890013/full, 접근일 2026-09-30
[^ref-1479]: Kidokoro, H., Kanda, T., Brščić, D., & Shiomi, M. (IEEE Transactions on Robotics 31(6)), Simulation-Based Behavior Planning to Prevent Congestion of Pedestrians Around a Robot, 2015-11-11, https://doi.org/10.1109/TRO.2015.2492862, 접근일 2026-10-09
[^ref-1480]: Brščić, D., Kanda, T., Ikeda, T., & Miyashita, T. (IEEE Transactions on Human-Machine Systems 43(6)), Person Tracking in Large Public Spaces Using 3-D Range Sensors, 2013-10-17, https://doi.org/10.1109/THMS.2013.2283945, 접근일 2026-10-09
[^ref-1486]: Catalano, I., Placed, J. A., Civera, J., & Peña Queralta, J. (arXiv), Kairos: Grounded Forecasting of Presence and Directional Flow in 4D Scene Graphs, 2026-09-23, https://arxiv.org/abs/2609.27467, 접근일 2026-10-09
[^ref-1487]: Lee, Y. 외, Park, I.-H. (교신) (Digital Health 12, 고려대학교 구로병원), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://journals.sagepub.com/doi/10.1177/20552076261437181, 접근일 2026-10-09
[^ref-1489]: Zhu, Y., Rudenko, A., Kucner, T. P., Lilienthal, A. J., & Magnusson, M. (arXiv; IEEE RA-L 표기), Long-Term Human Motion Prediction Using Spatio-Temporal Maps of Dynamics, 2025-10-03, https://arxiv.org/abs/2510.03031, 접근일 2026-10-09
[^ref-990]: Gehrke, S. R., Phair, C. D., Russo, B. J., & Smaglik, E. J. (Transportation Research Interdisciplinary Perspectives 18), Observed sidewalk autonomous delivery robot interactions with pedestrians and bicyclists, 2023-03-01, https://doi.org/10.1016/j.trip.2023.100789, 접근일 2026-10-09

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-09-12 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-09 | 2026-10-09-12 | 19. 사람·보행자 모델 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-10-09-12/pages/topics/2026/2026-10-09-area19-s11.md

```markdown
---
title: "19. 사람·보행자 모델 — 열린 질문"
type: topic
category: "E. 사물·사람·실시간 상태"
primary_area_no: 19
related_areas: [15, 16, 18, 22, 25, 26, 27, 31, 34, 36, 46, 49, 53, 54, 61, 63, 64, 66]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-1083, ref-1128, ref-1171, ref-1173, ref-1177, ref-1483, ref-1484, ref-1486, ref-1487, ref-406]
last_run: 2026-10-09
version: 1
split_from: docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#11
---

[홈](../../index.md) › [주제](../index.md) › 19. 사람·보행자 모델 — 열린 질문

# 19. 사람·보행자 모델 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 기록 재현에서 사람을 반응하게 만드는 방법과, 여러 출처의 사람 위치를 통합·익명화하는 형식은 아직 답이 없다. [추정][^ref-1128][^ref-1173] 2026-09-30 실행에서 검증한 이 절의 상세 내용(oq-261·oq-294·oq-307 서술 포함)은 주제 페이지 [19. 사람·보행자 모델 — 열린 질문](2026-09-30-area19-s11.md)에 있다.
- 이 페이지는 [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

기록 재현에서 사람을 반응하게 만드는 방법과, 여러 출처의 사람 위치를 통합·익명화하는 형식은 아직 답이 없다. [추정][^ref-1128][^ref-1173] 2026-09-30 실행에서 검증한 이 절의 상세 내용(oq-261·oq-294·oq-307 서술 포함)은 주제 페이지 [19. 사람·보행자 모델 — 열린 질문](2026-09-30-area19-s11.md)에 있다.

### 2026-10-09 갱신: 부분 근거(모두 열림 유지)

- **oq-256**·**oq-303** (상태: 열림) — Open-RMF 문서는 하드웨어 시험 기록으로 상황을 다시 만들 수 있다고 적고 crowdsim으로 가상 사람을 움직이지만, 기록된 사람 흐름을 crowdsim 입력으로 옮기는 방법은 설명하지 않는다. [사실][^ref-406]
- **oq-272** (상태: 열림) — Open-RMF 장애물 메시지는 층·발행 주체·분류·수명을 담지만 검출 신뢰도 필드가 없고, REP-155는 location_confidence를 두지만 두 형식 모두 익명화·집계 규칙이 없다. [추정][^ref-1484][^ref-1173]
- **oq-273** (상태: 열림) — 쇼핑몰 데이터 재생 시뮬레이션의 배정 연구와 병원 승강기 혼잡의 현장 측정은 근거가 되지만, 병원 연구의 혼잡 지표는 승강기 가동률·탑승 인원이며, 복도·구역 단위의 시간대별 사람 흐름을 작업 시간 추정·스케줄링에 넣어 현장에서 효과를 잰 연구는 이번에도 찾지 못했다. [추정][^ref-1083][^ref-1487]
- **oq-274** (상태: 열림) — 공공 교통신호 데이터를 실외 로봇 관제에 연동한 국내 시연은 확인되지만, 공공 인파 밀집 데이터를 로봇 경로·운행 제한에 연동한 사례나 데이터 제공 조건은 이번에도 찾지 못했다. [추정][^ref-1483][^ref-1177]
- **oq-298** (상태: 열림) — 사람 존재·흐름 예측을 장면 그래프의 장소·주행 노드에 붙이는 연구 구현(동료심사 전)은 있으나, 움직임 지도를 장소 목록·지도 판과 함께 관리하는 공통 형식이나 현장 운영 사례는 이번에도 찾지 못했다. [추정][^ref-1486][^ref-1171]

새로 올린 질문(번호는 [열린 질문](../../open-questions.md) 목록에서 부여):

- 시설 카메라의 사람 검출 결과로 플릿 주행 차선을 닫거나 속도를 제한하는 방식(Open-RMF lane_blocker)을 여러 제조사 로봇 현장에서 운영할 때 오검출·과도한 차선 폐쇄가 처리량과 지연에 주는 영향을 측정한 자료가 있는가?
- 병원 승강기 가동률·탑승 인원 같은 혼잡 임계값(예: 고려대학교 구로병원의 약 60%)을 다른 병원·건물로 옮겨 로봇 배정 시점에 쓸 때 재보정하는 방법이나 다기관 연구가 있는가?

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md)
- 관련 영역: [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1083]: Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv), Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments, 2025-08-27, https://arxiv.org/abs/2508.19731, 접근일 2026-10-09
[^ref-1128]: Gulino, C., Fu, J., Luo, W. 외 (Waymo; arXiv), Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research, 2023-10-12, https://arxiv.org/abs/2310.08710, 접근일 2026-09-30
[^ref-1171]: Kucner, T. P., Magnusson, M., Mghames, S., Palmieri, L., Verdoja, F., Swaminathan, C. S., Krajník, T., Schaffernicht, E., Bellotto, N., Hanheide, M., & Lilienthal, A. J. (The International Journal of Robotics Research 42(11)), Survey of maps of dynamics for mobile robots, 2023-09, https://journals.sagepub.com/doi/10.1177/02783649231190428, 접근일 2026-10-09
[^ref-1173]: ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan, REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction, 2022-01-11, https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst, 접근일 2026-10-09
[^ref-1177]: 행정안전부 (대한민국 정책브리핑), 29일부터 인파관리지원시스템 본격 운영…다중운집 인파사고 예방, 2023-12-27, https://www.korea.kr/news/policyNewsView.do?newsId=148924176, 접근일 2026-09-30
[^ref-1483]: 보안뉴스 (박미영), 경찰청 제공 실시간 교통신호정보, 보행자와 함께 거닐 실외 이동로봇의 눈이 되다, 2024-08-10, https://www.boannews.com/news/articleView.html?idxno=131956, 접근일 2026-10-09
[^ref-1484]: Open Robotics (open-rmf/rmf_internal_msgs), rmf_obstacle_msgs/msg/Obstacle.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_obstacle_msgs/msg/Obstacle.msg, 접근일 2026-10-09
[^ref-1486]: Catalano, I., Placed, J. A., Civera, J., & Peña Queralta, J. (arXiv), Kairos: Grounded Forecasting of Presence and Directional Flow in 4D Scene Graphs, 2026-09-23, https://arxiv.org/abs/2609.27467, 접근일 2026-10-09
[^ref-1487]: Lee, Y. 외, Park, I.-H. (교신) (Digital Health 12, 고려대학교 구로병원), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://journals.sagepub.com/doi/10.1177/20552076261437181, 접근일 2026-10-09
[^ref-406]: Open Robotics, Simulation - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-10-09

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-09-12 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-09 | 2026-10-09-12 | 19. 사람·보행자 모델 의 "열린 질문" 절에서 분리 |
```

### runs/2026-10-09-12/pages/topics/2026/2026-10-09-area19-s7.md

```markdown
---
title: "19. 사람·보행자 모델 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "E. 사물·사람·실시간 상태"
primary_area_no: 19
related_areas: [15, 16, 18, 22, 25, 26, 27, 31, 34, 36, 46, 49, 53, 54, 61, 63, 64, 66]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-1173, ref-1179, ref-1484, ref-1485, ref-406]
last_run: 2026-10-09
version: 1
split_from: docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#7
---

[홈](../../index.md) › [주제](../index.md) › 19. 사람·보행자 모델 — 관련 표준·프레임워크·오픈소스

# 19. 사람·보행자 모델 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 사람 표현에는 원문 상태가 Draft(2022-01-11 작성)인 ROS 규약 제안 REP-155(ROS4HRI)가 있다. [사실][^ref-1173] 2026-09-30 실행에서 검증한 이 절의 상세 내용은 주제 페이지 [19. 사람·보행자 모델 — 관련 표준·프레임워크·오픈소스](2026-09-30-area19-s7.md)에 있다.
- 이 페이지는 [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

사람 표현에는 원문 상태가 Draft(2022-01-11 작성)인 ROS 규약 제안 REP-155(ROS4HRI)가 있다. [사실][^ref-1173] 2026-09-30 실행에서 검증한 이 절의 상세 내용은 주제 페이지 [19. 사람·보행자 모델 — 관련 표준·프레임워크·오픈소스](2026-09-30-area19-s7.md)에 있다.

보행자 시뮬레이션·데이터셋·평가 지침은 오픈소스와 연구 자료 중심이다. [추정][^ref-1179]

### 2026-10-09 갱신에서 확인한 것

2026-10-09 원문 확인 기준으로도 REP-155의 상태는 Draft, 유형은 Informational이며, 식별되지 않은 사람은 익명 사람으로 표시하되 그 ID의 영속은 보장하지 않고, 개인정보·동의는 다루지 않는다. [사실][^ref-1173]

Open-RMF 장애물 메시지(rmf_obstacle_msgs/Obstacle)는 헤더의 좌표 프레임·시각, 발행 주체(source), 층 이름(level_name), 분류 라벨(예: human), 3차원 경계 상자, 예상 수명(lifetime), 추가·삭제 동작을 담으며, 확인한 정의에는 검출 신뢰도나 익명화를 위한 필드가 없다(확인일 2026-10-09). [사실][^ref-1484] 같은 생태계의 rmf_obstacle 저장소가 이 장애물을 만드는 사람 검출 노드와 차선을 막는 lane_blocker 노드를 둔다(6절). [사실][^ref-1485]

Open-RMF 시뮬레이션 문서는 하드웨어 시험에서 기록한 데이터로 시뮬레이션 상황을 다시 만들 수 있다고 적고, menge를 엔진으로 쓰는 선택 기능 crowdsim을 traffic_editor에서 켜 airport_terminal 예제에서 가상 사람을 움직이게 하지만, 기록된 사람 흐름을 crowdsim 입력으로 옮기는 방법은 설명하지 않는다. [사실][^ref-406] crowdsim은 가정한 미래를 실험하는 쪽(34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현)이고, 장애물 메시지는 현재 관측을 표현하는 쪽(18. 실시간 세계 상태·데이터 일관성)이므로 둘을 구분해 다룬다. [추정][^ref-406][^ref-1484]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md)
- 관련 영역: [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1173]: ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan, REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction, 2022-01-11, https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst, 접근일 2026-10-09
[^ref-1179]: Pérez-Higueras, N., Otero, R., Caballero, F., & Merino, L. (arXiv; IEEE RA-L 2023), HuNavSim: A ROS 2 Human Navigation Simulator for Benchmarking Human-Aware Robot Navigation, 2023-09-13, https://arxiv.org/abs/2305.01303, 접근일 2026-09-30
[^ref-1484]: Open Robotics (open-rmf/rmf_internal_msgs), rmf_obstacle_msgs/msg/Obstacle.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_obstacle_msgs/msg/Obstacle.msg, 접근일 2026-10-09
[^ref-1485]: Open Robotics (open-rmf/rmf_obstacle), rmf_obstacle — README, 미확인, https://github.com/open-rmf/rmf_obstacle, 접근일 2026-10-09
[^ref-406]: Open Robotics, Simulation - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-10-09

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-09-12 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-09 | 2026-10-09-12 | 19. 사람·보행자 모델 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-10-09-12/pages/topics/2026/2026-10-09-area19-s10.md

```markdown
---
title: "19. 사람·보행자 모델 — 다른 연구영역과의 연결"
type: topic
category: "E. 사물·사람·실시간 상태"
primary_area_no: 19
related_areas: [15, 16, 18, 22, 25, 26, 27, 31, 34, 36, 46, 49, 53, 54, 61, 63, 64, 66]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-1083, ref-1173, ref-1179, ref-1484, ref-1485, ref-1486, ref-1487, ref-1489, ref-406, ref-990]
last_run: 2026-10-09
version: 1
split_from: docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md#10
---

[홈](../../index.md) › [주제](../index.md) › 19. 사람·보행자 모델 — 다른 연구영역과의 연결

# 19. 사람·보행자 모델 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 현재 사람 위치를 다루는 18. 실시간 세계 상태·데이터 일관성과, 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈 양쪽에 걸치며 둘을 구분해 연결한다. [추정][^ref-1173][^ref-1179] 2026-09-30 실행에서 검증한 이 절의 상세 내용은 주제 페이지 [19. 사람·보행자 모델 — 다른 연구영역과의 연결](2026-09-30-area19-s10.md)에 있다.
- 이 페이지는 [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 현재 사람 위치를 다루는 18. 실시간 세계 상태·데이터 일관성과, 가정한 미래를 실험하는 34. 시뮬레이션·예측용 디지털 트윈 양쪽에 걸치며 둘을 구분해 연결한다. [추정][^ref-1173][^ref-1179] 2026-09-30 실행에서 검증한 이 절의 상세 내용은 주제 페이지 [19. 사람·보행자 모델 — 다른 연구영역과의 연결](2026-09-30-area19-s10.md)에 있다.

### 2026-10-09 갱신에서 더한 연결

- [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md) — 움직임 지도를 작업 배정 비용에 넣는 연구(시뮬레이션 결과)와 병원 승강기 혼잡에 따른 배정 시점 권고가 사람 혼잡 정보를 배정으로 잇는다. [추정][^ref-1083][^ref-1487]
- [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md) — 시간 조건부 움직임 지도 예측(데이터셋 이름 미확인)과 4차원 장면 그래프 예측(동료심사 전)이 경로·배정 비용의 입력 후보다. [추정][^ref-1489][^ref-1486]
- [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md) — 병원 승강기 혼잡이 배송 실패·지연과 이어지므로 승강기 상태·혼잡 지표를 받는 연동이 이 영역의 입력이 된다. 승강기 제어 자체는 연계 대상이다. [추정][^ref-1487]
- [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) — 사람 장애물에 따른 차선 폐쇄·속도 제한과 실외 보도의 지점별 보행자 비용은 경로·교통 관리의 제약으로 넘어간다. [추정][^ref-1485][^ref-990]
- [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md)과 [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md)·[36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md) — 시설 카메라가 검출한 현재 사람 장애물은 현재 상태 표현이고, crowdsim의 가상 사람은 가정한 미래를 실험하는 데 쓰므로 둘을 구분해 연결한다. [추정][^ref-1484][^ref-406]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md)
- 관련 영역: [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [16. 장소 의미·지도 관리](../../categories/space-and-map-model/place-semantics-and-map-management.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [25. 작업 배정 — MRTA](../../categories/planning-and-optimization/task-allocation-mrta.md), [26. 작업 순서·스케줄링](../../categories/planning-and-optimization/task-sequencing-and-scheduling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [31. 사람–로봇 협업](../../categories/execution-collaboration-and-recovery/human-robot-collaboration.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [46. 예측·학습 기반 최적화](../../categories/ai-and-learning/prediction-and-learning-based-optimization.md), [49. 사람 근접 안전](../../categories/safety/human-proximity-safety.md), [53. 개인정보·영상 데이터](../../categories/security-and-privacy/privacy-and-video-data.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1083]: Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv), Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments, 2025-08-27, https://arxiv.org/abs/2508.19731, 접근일 2026-10-09
[^ref-1173]: ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan, REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction, 2022-01-11, https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst, 접근일 2026-10-09
[^ref-1179]: Pérez-Higueras, N., Otero, R., Caballero, F., & Merino, L. (arXiv; IEEE RA-L 2023), HuNavSim: A ROS 2 Human Navigation Simulator for Benchmarking Human-Aware Robot Navigation, 2023-09-13, https://arxiv.org/abs/2305.01303, 접근일 2026-09-30
[^ref-1484]: Open Robotics (open-rmf/rmf_internal_msgs), rmf_obstacle_msgs/msg/Obstacle.msg, 미확인, https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_obstacle_msgs/msg/Obstacle.msg, 접근일 2026-10-09
[^ref-1485]: Open Robotics (open-rmf/rmf_obstacle), rmf_obstacle — README, 미확인, https://github.com/open-rmf/rmf_obstacle, 접근일 2026-10-09
[^ref-1486]: Catalano, I., Placed, J. A., Civera, J., & Peña Queralta, J. (arXiv), Kairos: Grounded Forecasting of Presence and Directional Flow in 4D Scene Graphs, 2026-09-23, https://arxiv.org/abs/2609.27467, 접근일 2026-10-09
[^ref-1487]: Lee, Y. 외, Park, I.-H. (교신) (Digital Health 12, 고려대학교 구로병원), Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, 2026-03-31, https://journals.sagepub.com/doi/10.1177/20552076261437181, 접근일 2026-10-09
[^ref-1489]: Zhu, Y., Rudenko, A., Kucner, T. P., Lilienthal, A. J., & Magnusson, M. (arXiv; IEEE RA-L 표기), Long-Term Human Motion Prediction Using Spatio-Temporal Maps of Dynamics, 2025-10-03, https://arxiv.org/abs/2510.03031, 접근일 2026-10-09
[^ref-406]: Open Robotics, Simulation - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/simulation.html, 접근일 2026-10-09
[^ref-990]: Gehrke, S. R., Phair, C. D., Russo, B. J., & Smaglik, E. J. (Transportation Research Interdisciplinary Perspectives 18), Observed sidewalk autonomous delivery robot interactions with pedestrians and bicyclists, 2023-03-01, https://doi.org/10.1016/j.trip.2023.100789, 접근일 2026-10-09

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-09-12 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-09 | 2026-10-09-12 | 19. 사람·보행자 모델 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 15건 / 전체 1282건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-406 | Open Robotics | Simulation - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/simulation.html | 2026-09-25 | 예 |
| ref-1079 | Francis, A., Pérez-D'Arpino, C., Li, C. 외 (ACM Transactions on Human-Robot Interaction, arXiv) | Principles and Guidelines for Evaluating Social Robot Navigation Algorithms | 2023-06-29 | https://arxiv.org/abs/2306.16740 | 2026-09-30 | 예 |
| ref-1128 | Gulino, C., Fu, J., Luo, W. 외 (Waymo, arXiv) | Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research | 2023-10-12 | https://arxiv.org/abs/2310.08710 | 2026-09-30 | 예 |
| ref-1171 | Kucner, T. P., Magnusson, M., Mghames, S., Palmieri, L., Verdoja, F., Swaminathan, C. S., Krajník, T., Schaffernicht, E., Bellotto, N., Hanheide, M., & Lilienthal, A. J. (The International Journal of Robotics Research 42(11)) | Survey of maps of dynamics for mobile robots | 2023 | https://journals.sagepub.com/doi/10.1177/02783649231190428 | 2026-09-30 | 아니오 |
| ref-1172 | Rudenko, A., Palmieri, L., Herman, M., Kitani, K. M., Gavrila, D. M., & Arras, K. O. (arXiv; IJRR 39(8), 2020) | Human Motion Trajectory Prediction: A Survey | 2019-12-17 | https://arxiv.org/abs/1905.06113 | 2026-09-30 | 예 |
| ref-1173 | ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan | REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction | 2022-01-11 | https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst | 2026-09-30 | 예 |
| ref-1174 | Helbing, D., & Molnár, P. (Physical Review E 51(5)) | Social force model for pedestrian dynamics | 1995-05-01 | https://link.aps.org/doi/10.1103/PhysRevE.51.4282 | 2026-09-30 | 아니오 |
| ref-1175 | Rudenko, A., Kucner, T. P., Swaminathan, C. S., Chadalavada, R. T., Arras, K. O., & Lilienthal, A. J. (arXiv; IEEE RA-L 5(2), 2020) | THÖR: Human-Robot Navigation Data Collection and Accurate Motion Trajectories Dataset | 2019-12-11 | https://arxiv.org/abs/1909.04403 | 2026-09-30 | 예 |
| ref-1176 | ATR (Advanced Telecommunications Research Institute International), Brščić, D. 외 | ATC shopping center tracking dataset | 미확인 | https://dil.atr.jp/crest2010_HRI/ATC_dataset/ | 2026-09-30 | 예 |
| ref-1177 | 행정안전부 (대한민국 정책브리핑) | 29일부터 인파관리지원시스템 본격 운영…다중운집 인파사고 예방 | 2023-12-27 | https://www.korea.kr/news/policyNewsView.do?newsId=148924176 | 2026-09-30 | 예 |
| ref-1178 | Vintr, T., Blaha, J., Rektoris, M., Ulrich, J., Rouček, T., Broughton, G., Yan, Z., & Krajník, T. (Frontiers in Robotics and AI) | Toward Benchmarking of Long-Term Spatio-Temporal Maps of Pedestrian Flows for Human-Aware Navigation | 2022-07-04 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.890013/full | 2026-09-30 | 예 |
| ref-1179 | Pérez-Higueras, N., Otero, R., Caballero, F., & Merino, L. (arXiv; IEEE RA-L 2023) | HuNavSim: A ROS 2 Human Navigation Simulator for Benchmarking Human-Aware Robot Navigation | 2023-09-13 | https://arxiv.org/abs/2305.01303 | 2026-09-30 | 예 |
| ref-1180 | ILIAD 프로젝트 컨소시엄 (EU Horizon 2020) | Concluding ILIAD | 2021-06 | https://iliad-project.eu/concluding-iliad/ | 2026-09-30 | 예 |
| ref-1181 | 조선비즈 (이정아, 다음 뉴스 게재) | 로봇과 인간이 공존하는 병원…약 배달 로봇에 길 비켜주고 엘리베이터도 잡아줘 | 2024-07-12 | https://v.daum.net/v/bc4riunbUE | 2026-09-30 | 예 |
| ref-1182 | Kidokoro, H., Kanda, T., Brščić, D., & Shiomi, M. (ACM/IEEE HRI 2013) | Will I bother here? - A robot anticipating its influence on pedestrian walking comfort | 2013-03 | https://www.semanticscholar.org/paper/Will-I-bother-here-A-robot-anticipating-its-on-Kidokoro-Kanda/bc0b26f1c13405fd89eb6d280bee739aed5b07a6 | 2026-09-30 | 아니오 |
```

### docs/glossary/index.md (요약: 용어 364개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- 3d-scene-graph: 3차원 장면 그래프 (3D Scene Graph)
- a-b-update: A/B 업데이트 (A/B Update (Dual Partition Update with Rollback))
- aas-registry-and-discovery: 자산관리셸 레지스트리·디스커버리 (AAS Registry / Discovery)
- ablation-study: 절제 실험 (Ablation Study)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
- actively-exploited-vulnerability: 적극 악용 취약점 (Actively Exploited Vulnerability (EU Cyber Resilience Act))
- affordance: 어포던스 (Affordance)
- age-of-information: 정보 나이 (Age of Information (AoI))
- agentic-ai: 에이전틱 AI (Agentic AI)
- aggregation-event: 집계 이벤트 (AggregationEvent)
- agv-technical-data-submodel: AGV 기술 데이터 서브모델 (Technical Data for AGV in Intralogistics (IDTA 02047))
- alarm-management: 경보 관리 (Alarm Management (ANSI/ISA 18.2))
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
- curb-cut: 연석 경사로 (Curb Cut (Curb Ramp))
- cyber-resilience-act: 사이버복원력법 (Cyber Resilience Act (CRA))
- data-holder: 데이터 보유자 (Data Holder (EU Data Act))
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
- level-alignment-fiducial: 층 정렬 기준점 (Fiducial (Level Alignment Fiducial))
- life-cycle-costing: 수명주기 비용 분석 (Life Cycle Costing (LCC, IEC 60300-3-3))
- lifelong-mapf: 지속형 다중 에이전트 경로 찾기 (Lifelong Multi-Agent Path Finding (Lifelong MAPF))
- lift-adapter: 승강기 어댑터 (Lift Adapter)
- linear-temporal-logic: 선형 시간 논리 (Linear Temporal Logic (LTL))
- littles-law: 리틀의 법칙 (Little's Law)
- llm-agent: LLM 에이전트 (LLM Agent)
- llm-modulo-framework: LLM-모듈로 프레임워크 (LLM-Modulo Framework)
- localization-score: 위치추정 품질 점수 (Localization Score (VDA 5050 localizationScore))
- location-check-digit: 위치 체크 디지트 (Location Check Digit)
- lockout-tagout: 잠금·표지 (Lockout/Tagout (LOTO))
- log-playback: 로그 재생 (Log Playback)
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
- opentelemetry-genai-semantic-conventions: 생성형 AI 의미 규약 (OpenTelemetry GenAI Semantic Conventions)
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
- pay-per-pick: 피킹량 기반 과금 (Pay-per-pick)
- payback-period: 투자 회수 기간 (Payback Period)
- pddl: 계획 도메인 정의 언어 (Planning Domain Definition Language (PDDL))
- perfect-order-fulfillment: 완전 주문 이행률 (Perfect Order Fulfillment)
- performable-action: 수행 가능 동작 (Performable Action (Open-RMF perform_action))
- personal-delivery-device: 개인 배송 장치 (Personal Delivery Device (PDD))
- plug-and-produce: 플러그 앤 프로듀스 (Plug and Produce)
- post-encroachment-time: 침범 후 시간 (Post-Encroachment Time (PET))
- post-occupancy-evaluation: 사용 후 평가 (Post-Occupancy Evaluation (POE))
- power-and-force-limiting: 동력·힘 제한 (Power and Force Limiting (PFL))
- pre-execution-plan-verification: 사전 실행 계획 검증 (Pre-execution Plan Verification)
- pre-hold-post-condition: 전제·유지·사후 조건 (Pre-, Hold-, Post-condition)
- precedence-constraint: 선후 제약 (Precedence Constraint)
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
- stpa: 시스템 이론적 프로세스 분석 (System-Theoretic Process Analysis (STPA))
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
- technology-readiness-level: 기술 성숙도 (Technology Readiness Level (TRL))
- teleoperation: 원격 조작 (Teleoperation)
- time-window: 시간창 (Time Window)
- topological-map: 위상 지도 (Topological Map)
- total-cost-of-ownership: 총소유비용 (Total Cost of Ownership (TCO))
- traversability: 통과 가능성 (Traversability)
- uncertainty-alignment: 불확실도 정렬 (Uncertainty Alignment)
- underspecification: 과소명세 (Underspecification)
- urdf: 통합 로봇 기술 형식 (Unified Robot Description Format (URDF))
- use-case-template: 사용 사례 템플릿 (Use Case Template (IEC 62559-2))
- user-simulator: 사용자 시뮬레이터 (User Simulator)
- utaut: 통합 기술 수용 이론 (Unified Theory of Acceptance and Use of Technology (UTAUT))
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
- wireless-safety-rated-emergency-stop: 무선 안전 비상정지 (Wireless Safety-rated Emergency Stop)
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [19] 에 걸린 9건 / 전체 321건)

```markdown
- oq-256 [열림] 실제 운영 기록을 재생해 재현한 상황에서 배차 정책이나 로봇 수를 바꿔 비교할 때, 기록된 다른 로봇·사람이 바뀐 조건에 반응하지 않는 문제를 로봇 플릿 재현에서 어떻게 다루는가? (영역 36, 19, 33)
- oq-261 [열림] 피촬영자가 한 로봇에 밝힌 촬영 거부 의사를 같은 현장의 다른 로봇과 플랫폼 기록에 공통으로 반영하는 방법이나 운영 사례가 있는가? (영역 53, 19)
- oq-272 [열림] 여러 제조사 로봇과 설비 센서가 각자 감지한 사람 위치를 하나의 사람 흐름 모델로 합칠 때 좌표·시각·신뢰도·익명화 형식을 정한 공개 규격이나 구현이 있는가? (영역 19, 18, 53)
- oq-273 [열림] 병원·상업 시설·물류창고에서 시간대별 사람 혼잡을 로봇 작업 시간 추정과 배정·스케줄링에 반영해 처리 시간이나 지연 변화를 측정한 현장 연구가 있는가? (영역 19, 26, 63)
- oq-274 [열림] 기지국 기반 인파관리지원시스템 같은 공공 인파 밀집 데이터를 실외 배송로봇의 경로·운행 제한에 연동한 국내 사례나 데이터 제공 조건이 있는가? (영역 19, 66)
- oq-294 [열림] 사람 존재 정보로 세계 상태 정보의 확실도를 낮추는 방식을 물류창고·병원 같은 이동로봇 현장의 문·통로·적재물 상태 판단에 적용한 연구나 사례가 있는가? (영역 18, 19, 31)
- oq-298 [열림] 시간대별 사람 흐름을 담은 움직임 지도(maps of dynamics)를 ROP 의 장소 목록·지도 판과 함께 관리하고 경로·작업 시간 계획에 넘기는 공통 형식이나 현장 사례가 있는가? (영역 16, 19, 27)
- oq-303 [열림] 대화로 실제 상황을 재현할 때 운영 기록에 남은 사람 흐름·혼잡을 시뮬레이션의 보행자 모델 입력으로 옮긴 연구나 사례가 있는가? (영역 11, 19, 36)
- oq-307 [열림] 사람 행동 모델로 고위험 상황을 생성하는 시뮬레이션 위험 식별 방법을 다중 이동로봇 플릿과 보행자가 많은 병원·상업 시설 공간에 적용한 사례가 있는가? (영역 48, 34, 19)
```

### runs/2026-10-09-12/verification2.json

```json
{
  "run_id": "2026-10-09-12",
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
    "ok": false,
    "overlaps": [
      "새 분리 주제 페이지 5건(docs/topics/2026/2026-10-09-area19-s6·s7·s8·s10·s11.md)은 기존 분리 주제 페이지(docs/topics/2026/2026-09-30-area19-s6·s7·s8·s10·s11.md)와 H1 제목이 같다(예: '19. 사람·보행자 모델 — 대표 접근법과 기술'). 제목은 분리 코드가 만들므로 pipeline 담당이 정할 사항이며, 이번 수정 지시는 두 페이지 사이의 연결 복구로 한정한다",
      "세부영역 페이지 6·7·8·10·11절이 이제 2026-10-09 분리 주제 페이지만 가리킨다. 2026-09-30 분리 주제 페이지로 가는 링크가 사라져, 이미 게시·검증된 상세 내용으로 가는 경로가 끊겼다"
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
    "세부영역 페이지 6·7·8·10·11절: 기존 링크 줄 '자세한 내용은 주제 페이지 [19. 사람·보행자 모델 — …](../../topics/2026/2026-09-30-area19-sN.md)에 있다.'가 갱신·자동 분리 과정에서 사라졌다. 절마다 2026-09-30 주제 페이지 링크를 되살려, 새 2026-10-09 분리 주제 페이지 링크와 함께 둔다. 방법은 둘 중 하나다: 세부영역 페이지 해당 절에 두 링크를 함께 두거나, 2026-10-09 분리 주제 페이지 3. 본문 첫머리에 해당 2026-09-30 주제 페이지 링크를 둔다. 이유: 지금 상태로는 이전 실행에서 검증·게시한 6·7·8·10·11절의 상세 내용(기존 열린 질문 oq-261·oq-294·oq-307 서술 포함)에 세부영역 페이지에서 갈 수 없다. 원 절 내용을 그대로 옮기지 않은 것이기도 하다(부록 R-3).",
    "2026-10-09-area19-s8.md의 Brščić 외 항목: '천장 높이 3차원 거리 센서'를 '사람 키보다 높게 단 여러 3차원 거리 센서'로 고친다. 이유: f5(ref-1480 초록)는 'mounted above human height'까지만 말한다. '천장'은 ref-1176(ATC 데이터셋 페이지)의 표현이므로 ref-1480 각주로 쓰면 드리프트다.",
    "세부영역 페이지 프런트매터 sources: 기존에 있던 ref-1175(THÖR)와 ref-1079(Francis 외 평가 지침)가 근거 없이 빠졌다. 되살린다. 이유: 브리프와 1차 판정 어디에도 이 두 출처를 빼라는 근거가 없다. diff_summary에도 언급이 없다. 기존 프런트매터는 분리 주제 페이지의 출처까지 함께 올리는 관행을 따랐다(ref-406도 같은 방식이었다)."
  ],
  "confidence": "low",
  "verification_note": "판정: 조건부 승인 / 2차 수정 후 재검증. 확인 22건, 미확인 0건, 교차 확인 0건. 강등: 없음. 원문 미열람 출처: 이번 실행에서 다시 열지 않은 ref-1176, ref-1177, ref-1181. 이들의 기존 각주는 2026-09-30 열람이며 접근일을 바꾸지 않았다. 주의: 신규 근거는 모두 단일 출처다. 같은 저자군·같은 기관 쌍(ref-1480과 ref-1176, ref-1482와 ref-990)은 독립 출처가 아니다. ref-1171·ref-1182·ref-1479·ref-1480·ref-990은 초록만 확인했다. 5절 상업 시설 사례의 쇼핑몰 시험 근거는 HRI 2013(ref-1182)이 아니라 TRO 2015 확장판(ref-1479)으로 정정됐다. 고려대학교 구로병원 연구(ref-1487)의 성공률 87.03%는 논문 보고값이다. 산출 기준은 미확인이고, 단일 병원·단일 기종 연구이며, 혼잡 지표는 승강기 가동률이다. Kazemi Eskeri 외(ref-1083)는 시뮬레이션 결과이고, Kairos(ref-1486)는 동료심사 전 프리프린트다. 3·6·9절의 핵심 판단은 여전히 [추정]이다. 열린 질문 oq-256·oq-272·oq-273·oq-274·oq-298·oq-303은 부분 근거만 있어 열림을 유지한다. 정정 요청은 없다. / 2차 수정 후 재검증. 1차 수정 지시 14건은 모두 이행됐다. 태그 상향은 없다. 드리프트 1건(s8 Brščić 항목의 '천장 높이')을 고치도록 지시했다. [분류원문] 보존, 섹션 순서 준수. 링크 문제: 세부영역 페이지 6·7·8·10·11절에서 2026-09-30 분리 주제 페이지 5건으로 가는 링크가 갱신과 자동 분리 과정에서 사라졌다. 프런트매터 sources에서 ref-1175·ref-1079가 근거 없이 빠졌다. pipeline 담당 확인 사항: 자동 분리 코드가 절 안의 기존 '자세한 내용은 주제 페이지 …' 줄을 옮기지 않고 버리는지 확인해야 한다. 새 분리 주제 페이지 제목이 기존 분리 주제 페이지와 같아지는 문제(같은 H1이 두 개)도 처리 방안이 필요하다.",
  "retry_reason": null
}
```
