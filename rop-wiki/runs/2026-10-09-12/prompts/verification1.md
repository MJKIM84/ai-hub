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
- verification_stage: first
- verifier_budget:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
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
        "ref-1481"
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
        "ref-1481",
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
      "id": "ref-1481",
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
      "summary": "ref-1481 연구의 대학 보도. 충돌 12건, 좁은 보도·많은 교차의 위험, 경로·배송 지점 권고를 소개.",
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
      "f14 는 ref-1481 과 같은 대학의 보도라 독립 출처 아님. 논문 본문(충돌 수·예측 요인 계수) 미열람",
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
    "limits": "web_fetch_available: true · fetch_mode full. 갱신(update) 실행으로, 정정 요청이 없어 원문 미열람·검색 결과 기준이던 주장의 재확인과 약한 절(5·7·9·11)과 열린 질문(oq-272·oq-273·oq-274·oq-298·oq-303)만 조사했다. 검색 15회/30, 신규 출처 11건/15(ref-1479~ref-1489, 예약 구간 안). 재사용 8건 가운데 ref-1171(Aalto 초록)·ref-1173(github_raw)·ref-1182(OpenAlex 초록)·ref-1083(arXiv)·ref-406(inbox 원문)은 이번에 열었고, ref-1176·ref-1177·ref-1181 은 열지 않았다(fetched false). 신규 11건은 모두 원문 또는 공식 초록을 열었다. 다만 ref-1479·ref-1480·ref-1481 은 OpenAlex 초록만 열었다. 교차 확인 0건이다. 같은 저자군·같은 기관 쌍(ref-1480과 ref-1176, ref-1482와 ref-1481)은 독립 출처로 보지 않았다. 주요 정정 근거: 5절 상업 시설 사례의 '실제 쇼핑몰 시험'은 HRI 2013 초록에 없고 TRO 2015 확장판 초록에 있다(f3·f4). 7절 REP-155 는 2026-10-09 원문 기준으로 여전히 Draft 이며(f1), 지난 실행의 '공식 채택' 검색 요약과의 차이는 원문 기준으로 정리된다. 한국 자료: 신규 ref-1483(보안뉴스)·ref-1487(고려대 구로병원)·ref-1488(현대자동차그룹), 재사용 ref-1177·ref-1181. 현장 유형: 병원(f10·f11·f18)·상업 시설(f4·f5)·실외(f13·f14·f15·f16·f17)이며 물류창고는 기존 ILIAD 사례를 유지하고 새 근거는 찾지 않았다. 제조 공장·가정 사례는 없다. 18. 실시간 세계 상태·데이터 일관성(현재 관측: f6·f7)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험: f22)을 구분했다. L. AI·학습 기술 관련 f9·f21 은 46. 예측·학습 기반 최적화와 25. 작업 배정 — MRTA 에 함께 연결하자고 제안했다. 열린 질문에 대한 부분 근거: oq-272(f6·f8), oq-273(f9·f10·f11·f12), oq-274(f16·f17), oq-298(f19·f20), oq-303·oq-256(f22). 해결 제안은 없다. 벤더 기능·성능 주장은 없다(f18 은 협약 내용 진술이다). 페이지 갱신 제안은 1건(대상 영역 페이지)이며 63. 병원·의료, 66. 실외, 27. 다중 로봇 경로·교통 관리 — MAPF 반영은 다음 실행 후보로 남겼다. 입력 누락 없음, 우선 지정 질문 없음."
  }
}
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

### docs/categories/objects-people-and-live-state/work-object-and-asset-identification-and-handover-tracking.md (요약)

```markdown
# 17. 작업 대상·자산 식별과 인계 추적

소속 대분류: E. 사물·사람·실시간 상태 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 4

## 1. 한 줄 정의

물품·자산·도구 같은 작업 대상의 식별·위치·인계 책임을 추적하고, 사람에게 넘길 때 수령인을 확인한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **작업 대상 식별·추적**: 물품·자산·도구·운반구·검체·세탁물처럼 작업 대상의 식별자·위치·적재 관계를 추적한다
- **인계·책임 기록**: 누가 언제 무엇을 넘겨받았는지 관측 근거와 함께 기록한다
- **이벤트 공통 형식**: 상태·위치·이동·인계 이벤트를 공통 형식으로 주고받는다(GS1 EPCIS 등)
- **수령인 확인**: 물건을 사람에게 넘길 때 받는 사람을 PIN·카드·앱으로 확인하고 인계 기록을 남긴다

이전 분류(2026-09-24)에서 이 페이지는 옛 7번 영역 ‘화물·재고·자산 식별과 추적’(옛 대분류 B. 공통 정보·환경 모델)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 제품·박스·팔레트·운반구·로봇을 식별하고, 적재 관계·위치·인계 이력을 연결 [옛 분류원문]

> 옛 질문: 로봇은 도착했는데 실제로 어떤 팔레트가 인계됐는가? [옛 분류원문]

> 옛 원문 주석: **7번은 SCM 관점에서 특히 빠뜨리기 쉽다.** 로봇 위치를 추적하는 것과 화물의 위치·인계 책임을 추적하는 것은 다르다. GS1 EPCIS는 제품·자산의 상태, 위치, 이동, 인계에 관한 이벤트를 공유하는 참고 표준이다. [3] [옛 분류원문]

이전 분류 기준: 원문의 [3]은 참고문헌 [ref-003](../../references/ref-003.md)에 해당한다.[^ref-003]

## 2. 핵심 질문

로봇이 도착했을 때 실제로 무엇이 누구에게 넘겨졌는지 어떻게 확인할 것인가? [분류원문]

> 원문 주석: **17번은 특히 빠뜨리기 쉽다.** 로봇 위치를 추적하는 것과 작업 대상의 위치·인계 책임을 추적하는 것은 다르다. GS1 EPCIS는 제품·자산의 상태, 위치, 이동, 인계에 관한 이벤트를 공유하는 참고 표준이다. [3] [분류원문]

원문의 [3]은 참고문헌 [ref-003](../../references/ref-003.md)에 해당한다.[^ref-003]
```

### docs/categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md (요약)

```markdown
# 18. 실시간 세계 상태·데이터 일관성

소속 대분류: E. 사물·사람·실시간 상태 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

로봇·설비·공간·물품의 현재 상태를 통합하고, 관측의 신선도·신뢰도를 관리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **실시간 세계 상태 통합**: 로봇·설비·공간·물품·사람의 현재 상태를 한곳에 모으고 지연·누락·충돌·불확실성을 관리한다
- **관측 신선도·신뢰도**: 오래되거나 불확실한 관측(예를 들어 30초 전의 문 상태)을 지금의 판단에 써도 되는지 정한다

이전 분류(2026-09-24)에서 이 페이지는 옛 8번 영역 ‘실시간 세계 상태·데이터 일관성’(옛 대분류 B. 공통 정보·환경 모델)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 로봇·설비·공간·화물의 현재 상태를 통합하고, 시간 지연·누락·충돌·불확실성을 관리 [옛 분류원문]

> 옛 질문: 문이 열려 있다는 정보가 30초 전이라면 지금도 통과 가능하다고 볼 수 있을까? [옛 분류원문]

> 옛 원문 주석: 8번의 실시간 모델이 **현재 상태를 표현**한다면, 22번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [옛 분류원문]

## 2. 핵심 질문

조금 전에 받은 상태 정보를 지금의 판단에 믿고 써도 되는가? [분류원문]

> 원문 주석: 18번의 실시간 모델이 **현재 상태를 표현**한다면, 34번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [분류원문]
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

### docs/categories/space-and-map-model/place-semantics-and-map-management.md (요약)

```markdown
# 16. 장소 의미·지도 관리

소속 대분류: D. 공간·지도 모델 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

장소에 이름·용도를 붙이고, 지도를 편집하고, 바뀔 때 버전을 관리한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **장소 의미·이름**: 구역·방·목적지에 이름·별칭·용도를 붙여 업무와 대화에서 같은 장소를 같은 이름으로 가리키게 한다
- **지도 버전·변경 관리**: 배치 변경과 임시 통제 구역을 지도에 반영하고 지도 버전을 관리한다
- **지도·환경 편집기**: 사람이 직접 공간과 시설을 그리고 고치는 편집 화면을 제공한다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 6번 영역 ‘지도·공간·위치 모델’에서 왔다. 그 본문은 [15. 지도·공간·위치 모델](map-space-and-location-model.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

같은 장소를 모두가 같은 이름으로 부르고, 공간이 바뀌면 지도를 어떻게 따라 바꿀 것인가? [분류원문]

> 원문 주석: 지도는 한 번 만들고 끝나지 않는다. **현장과 도면의 차이 확인(14번), 좌표 정렬과 위치추정 신뢰도(15번), 지도 버전 관리(16번)**가 함께 필요하다. [분류원문]
```

### docs/categories/planning-and-optimization/task-sequencing-and-scheduling.md (요약)

```markdown
# 26. 작업 순서·스케줄링

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

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

### docs/categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md (요약)

```markdown
# 27. 다중 로봇 경로·교통 관리 — MAPF

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

여러 로봇의 경로·통과 시점·우선권을 조율한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **다중 로봇 경로·교통 관리**: 여러 로봇의 경로와 통과 시점을 조율하고 혼잡·교착·우선권을 처리한다
- **이기종 로봇 간 통행 우선권**: 서로 다른 제조사의 로봇이 좁은 통로에서 만날 때 누가 양보할지 정한다

이전 분류(2026-09-24)에서 이 페이지는 옛 15번 영역 ‘다중 로봇 경로·교통 관리 — MAPF’(옛 대분류 D. 계획·최적화)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 여러 로봇의 경로와 통과 시점을 조율하고, 혼잡·교착·우선권을 처리 [옛 분류원문]

> 옛 질문: 서로 다른 제조사의 로봇이 좁은 통로에서 마주치면 누가 양보할까? [옛 분류원문]

## 2. 핵심 질문

서로 다른 제조사의 로봇이 좁은 통로에서 마주치면 누가 양보할까? [분류원문]
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

### docs/categories/design-and-simulation/simulation-and-predictive-digital-twin.md (요약)

```markdown
# 34. 시뮬레이션·예측용 디지털 트윈

소속 대분류: I. 설계·시뮬레이션 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

물리·센서·다중 로봇 시뮬레이션과 그 자산, 운영 정책·수요 변화 예측 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **시뮬레이션 엔진**: 로봇·설비·물품·사람을 물리·센서 수준에서 가상으로 재현한다(MuJoCo·Gazebo·Isaac Sim 등)
- **운영 정책·수요 변화 예측**: 배치·운영 정책·일의 양이 바뀔 때의 효과를 가상 환경에서 미리 본다
- **시뮬레이션 관측 모델**: 잡음·지연이 있는 관측을 만들어 시뮬레이션 시험이 현실의 불확실성을 반영하게 한다
- **시뮬레이션 자산 관리**: 로봇·물품·환경의 3D 모델과 물성 값을 출처·라이선스와 함께 관리해 시뮬레이션에 쓴다

이전 분류(2026-09-24)에서 이 페이지는 옛 22번 영역 ‘시뮬레이션·예측용 디지털 트윈’(옛 대분류 F. 도입·검증·유지관리)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 로봇·설비·물동량을 가상 환경에서 재현하고, 배치·운영 정책·수요 변화의 효과를 예측 [옛 분류원문]

> 옛 질문: 성수기 주문량이 늘면 어디가 먼저 막힐까? [옛 분류원문]

> 옛 원문 주석: 8번의 실시간 모델이 **현재 상태를 표현**한다면, 22번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [옛 분류원문]

## 2. 핵심 질문

현장을 바꾸기 전에 가상 환경에서 결과를 얼마나 믿을 만하게 미리 볼 수 있는가? [분류원문]

> 원문 주석: 18번의 실시간 모델이 **현재 상태를 표현**한다면, 34번은 그 모델을 이용해 **가정한 미래를 실험**한다. 구분해두면 디지털 트윈이라는 이름 아래 서로 다른 기능이 섞이지 않는다. [분류원문]
```

### docs/categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md (요약)

```markdown
# 36. 가상 시운전·실제 상황 재현

소속 대분류: I. 설계·시뮬레이션 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

설치 전 가상 시운전, 실행 전 계획 검증, 운영 기록 기반 재현, 시뮬레이션–현실 차이 관리 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **실행 전 계획 검증**: 선언한 초기 조건에서 경로·자원·능력을 실제로 실행하지 않고 정적으로 검사한다
- **가상 시운전**: 실제 설치 전에 연동과 운영 정책을 가상 환경에서 시험한다
- **운영 기록 기반 재현**: 실제 운영 기록으로 시뮬레이션의 초기 상태와 사건을 다시 구성한다
- **시뮬레이션–현실 차이 관리**: 시뮬레이션 결과를 현실에 적용할 때 생기는 차이를 측정하고 보정한다
- **디지털 트윈 동기화**: 실시간 상태를 가상 모델에 계속 반영해 현재 상태 표현과 미래 실험을 잇는다

## 2. 핵심 질문

설치 전에 가상으로 시운전하고, 실제로 있었던 문제를 시뮬레이션에서 다시 볼 수 있는가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]
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

### docs/categories/safety/human-proximity-safety.md (요약)

```markdown
# 49. 사람 근접 안전

소속 대분류: M. 안전 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

사람과의 분리 거리·감속·양보, 구역별 속도·진입 제한 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **사람 근접 안전**: 사람과의 분리 거리를 지키고 감속·양보·재개를 판단한다
- **구역별 속도·진입 제한**: 구역·시간대별 속도 제한과 진입 금지를 설정해 계획과 실행에 반영한다

## 2. 핵심 질문

사람 가까이에서 로봇은 얼마나 떨어지고, 언제 느려지고 멈춰야 하는가? [분류원문]
```

### docs/categories/security-and-privacy/privacy-and-video-data.md (요약)

```markdown
# 53. 개인정보·영상 데이터

소속 대분류: N. 보안·개인정보 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

영상·작업자·거주자 데이터 보호, 최소 수집·익명화 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **개인정보·영상 데이터 보호**: 카메라 영상과 작업자·환자·거주자 데이터를 보호한다
- **사람 데이터 최소 수집·익명화**: 보행자 위치·영상에서 신원을 떼어 내고 필요한 만큼만 모은다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 26번 영역 ‘사이버보안·접근권한·개인정보’에서 왔다. 그 본문은 [51. 인증·권한·격리](authentication-authorization-and-isolation.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

로봇이 찍은 영상과 사람의 위치 정보를 어디까지 모으고 어떻게 지킬 것인가? [분류원문]
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

### docs/categories/site-type-applications/hospital-and-healthcare.md (요약)

```markdown
# 63. 병원·의료

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

검체·약품·식사·린넨 이송, 감염 관리, 환자 정보 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **병원 적용**: 검체·약품·식사·린넨 이송과 감염 관리 구역, 환자 정보 보호를 다룬다

## 2. 핵심 질문

감염 관리와 환자 정보 보호 조건에서 병원 이송을 어떻게 운영할 것인가? [분류원문]
```

### docs/categories/site-type-applications/commercial-facilities.md (요약)

```markdown
# 64. 상업 시설

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

호텔 객실 배송, 식당 서빙, 매장·쇼핑몰 안내·청소 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **상업 시설 적용**: 호텔 객실 배송·식당 서빙·매장 안내·청소와 영업 시간에 맞춘 운영을 다룬다

## 2. 핵심 질문

손님이 있는 영업 시간에 호텔·식당·매장의 로봇을 어떻게 운영할 것인가? [분류원문]
```

### docs/categories/site-type-applications/outdoor.md (요약)

```markdown
# 66. 실외

소속 대분류: Q. 현장 유형별 적용 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

실외 배송·순찰·캠퍼스, 보도 주행 규정, 날씨 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **실외 적용**: 실외 배송·순찰·캠퍼스 운영과 보도 주행 규정·위성 위치·날씨 조건을 다룬다

## 2. 핵심 질문

보도와 날씨 조건에서 실외 로봇을 어떻게 운영할 것인가? [분류원문]
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 15건 / 전체 1262건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

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

### docs/glossary/index.md (요약: 용어 358개, slug: 한국어 (영어). 정의는 docs/glossary/<slug>.md)

```markdown
- 3d-scene-graph: 3차원 장면 그래프 (3D Scene Graph)
- a-b-update: A/B 업데이트 (A/B Update (Dual Partition Update with Rollback))
- aas-registry-and-discovery: 자산관리셸 레지스트리·디스커버리 (AAS Registry / Discovery)
- ablation-study: 절제 실험 (Ablation Study)
- action-dependency-graph: 행동 의존 그래프 (Action Dependency Graph (ADG))
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
- workflow-net: 워크플로 넷 (Workflow Net (WF-net))
- zone-set: 구역 집합 (Zone Set (VDA 5050 zoneSet))
- zones-and-conduits: 보안 구역과 도관 (Zones and Conduits (IEC 62443))
```

### docs/open-questions.md (요약: 대상 영역 [19] 에 걸린 9건 / 전체 309건)

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

### runs/2026-10-09-11/research.md

```markdown
# 리서치 브리프 2026-10-09-11

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-09-11 |
| 날짜 | 2026-10-09 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 18. 실시간 세계 상태·데이터 일관성 |
| 대분류 | E. 사물·사람·실시간 상태 |

## 갭(비어 있거나 약한 섹션)

- 섹션 5. 적용 사례 (현장 유형 명시) — 물류창고 시나리오 2건뿐, 병원·제조 공장·기타 현장 사례 없음
- 섹션 6. 대표 접근법과 기술 — 시각 필드·QoS 외에 시간이 지날수록 믿음을 낮추는 확률 모델, 허가 만료 시각(lease) 같은 접근이 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 — 로봇–승강기·자동문 인터페이스 표준(ISO 초안, 싱가포르 TR 93)과 OPC UA 시각 필드가 원문 확인 없이 비어 있음(ref-288 원문 미열람 상태)
- 섹션 8. 대표 연구와 자료 — 반정적 대상의 지속성 추정 연구, 운영 중 시뮬레이션 초기화 연구 없음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 — 위치추정 품질 점수로 신뢰 판단을 한다는 서술이 VDA 5050 원문(로그·시각화 전용 규정)과 맞는지 미확인
- 섹션 10. 다른 연구영역과의 연결 — 트랙 floorplan-recognition 단계 3 반영 제안 2건(정적 능력 대조와 현재 상태 층 분리, 34. 시뮬레이션·예측용 디지털 트윈에 현재 상태 초기값 공급) 미반영
- 섹션 11. 열린 질문 — oq-034(설비 상태 허용 경과 시간), oq-035(시각 동기화), oq-028(위치추정 신뢰도), oq-037(출처 충돌)에 새 근거 없음
- 정정 요청 없음(inbox/corrections.md 비어 있음)

## 조사 질문

1. 조금 전에 받은 상태 정보를 지금의 판단에 믿고 써도 되는가? [분류원문]
2. 문·승강기·충전기 같은 설비 상태를 몇 초까지 믿을지 정한 표준·국내 기준이 새로 나왔는가, 로봇–승강기·자동문 인터페이스 표준은 어디까지 와 있는가? (oq-034, 섹션 7·11 겨냥)
3. 상태 보고 주기·시각 체계가 다른 로봇이 섞일 때 시각 동기화와 수신 시각 처리를 어떻게 하는가? (oq-035, 섹션 6 겨냥)
4. VDA 5050 의 위치추정 품질 정보(localizationScore 등)를 관제 판단 논리에 써도 되는가? (oq-028, 섹션 9 겨냥)
5. 트랙 floorplan-recognition 단계 3 반영 제안: 정적 능력·지도 대조와 현재 상태 층(문 상태, Open-RMF 차선 폐쇄)을 어떻게 나누며, 운영 중 예측 시뮬레이션을 현재 상태로 초기화한다는 연구 근거는 무엇인가? (섹션 10 겨냥)
6. 물류창고 밖의 현장(병원·제조 공장·기타)에서 설비·로봇 상태를 통합하거나 오래된 상태를 다룬 사례는 무엇인가, 한국 자료는 있는가? (섹션 5 겨냥)
7. 오래된 관측을 고정 임계값이 아니라 시간에 따라 믿음을 낮추는 방식으로 다루는 연구가 있는가? (섹션 6·8 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Open-RMF 의 rmf_fleet_msgs/LaneRequest 메시지는 플릿 이름과 열 차선 목록(open_lanes)·닫을 차선 목록(close_lanes)만으로 이루어져, 경로망(내비게이션 그래프) 자체를 바꾸지 않고 차선의 통행 가능 여부만 바꾸는 요청이다. | ref-1451 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f2 | [사실] | Open-RMF rmf_traffic 의 LaneClosure 클래스는 그래프 안 차선의 폐쇄 상태(열림·닫힘)를 따로 기술하고 차선 번호별로 열기·닫기·열림 확인을 제공한다. | ref-1453 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f3 | [사실] | Open-RMF 유지관리자는 정비 중인 승강기·문을 RMF 에 알리는 방법으로, 그 승강기·문을 지나는 차선을 찾아 닫는 차선 폐쇄 기능을 권했고, 폐쇄 시점은 통합자가 정하며 플릿 어댑터가 승강기 상태(lift_states)의 OFFLINE 을 보고 해당 차선을 닫는 구성을 제안했다. | ref-1452, ref-286 | 아니오 | medium | 2024-01-24 | 제약 | — |
| f4 | [추정] | 로봇이 어디를 지날 수 있는가에 대한 정적 대조(5. 로봇 능력·작업 표현의 능력, 15. 지도·공간·위치 모델의 경로망)와, 지금 그 길이 열려 있는가를 나타내는 현재 상태 층(문 상태, 승강기 운영 모드, 차선 폐쇄)을 분리하고 18. 실시간 세계 상태·데이터 일관성이 후자를 시각과 함께 공급하는 구성이 Open-RMF 의 설계와 맞을 것으로 보인다. | ref-1451, ref-1453, ref-1452, ref-286 | 아니오 | low | 2026-10-09 | 제약 | — |
| f5 | [사실] | 기계 수준 온라인 시뮬레이션 체계적 문헌 고찰(Deubert 외, 2024)은 온라인 시뮬레이션이 시스템의 실제 상태로 초기화되어야 하며, 이를 위해 상태 데이터의 명확한 정의·가용성·충분한 품질·충분한 갱신 빈도가 필요하고, 초기화 방식으로 실시스템과 동기화된 상위 시뮬레이션에서 복제하는 방법과 센서·구성요소 상태 측정에서 시작하는 방법이 있다고 정리한다. | ref-1449 | 아니오 | medium | 2024-01-15 | — | — |
| f6 | [사실] | Galka(WSC 2024)는 SAP EWM 을 쓰는 주문 피킹 시스템의 시뮬레이션 기반 디지털 트윈에서, 빈 부하 상태로 시작하는 기준 모델 대신 실제 시스템의 부하 상태로 동기화하는 초기화 방식을 제안해 초기 과도 구간을 크게 줄였다고 보고했다. | ref-1450 | 아니오 | medium | 2024 | 물류창고 | 원문 미열람 |
| f7 | [사실] | 운영 중 예측 시뮬레이션은 실제 상태로 초기화해야 한다는 점을 기계 수준 온라인 시뮬레이션 고찰과 물류창고 피킹 디지털 트윈 연구가 함께 다룬다. | ref-1449, ref-1450 | 예 | medium | 2024 | — | — |
| f8 | [추정] | 18. 실시간 세계 상태·데이터 일관성은 현재 상태를 시각·품질 정보와 함께 34. 시뮬레이션·예측용 디지털 트윈의 초기값으로 넘기는 쪽이고, 34번은 그 초기값에서 가정한 미래를 실험하는 쪽으로 나누는 것이 분류 원문의 구분과 위 연구들의 초기화 요건(상태 정의·품질·갱신 빈도)에 맞을 것으로 보인다. | ref-1449, ref-1450 | 아니오 | low | 2026-10-09 | — | — |
| f9 | [사실] | 용인세브란스병원은 한국로봇산업진흥원 AI·5G 기반 서비스로봇 융합모델 실증사업으로 로봇 5종 10대를 들였고, 혈액 이송 로봇이 승강기·스피드게이트·자동문과 연동해 통제 구역과 층 사이를 이동하며, 통합반응상황실의 5G 기반 관제 플랫폼이 로봇 상태와 위치를 실시간으로 모니터링한다고 보도되었다. | ref-1461 | 아니오 | low | 2022-11-18 | 병원 / 수행 자원 | — |
| f10 | [사실] | 싱가포르 창이종합병원(CGH)의 RoMi-H 는 제조사가 다른 로봇들이 공통 미들웨어로 병원의 기존 승강기·자동문을 함께 쓰게 하며, 새로 들인 로봇도 기존 승강기·자동문과 연동하도록 설정할 수 있고 긴급한 작업을 하는 로봇에 우선권을 준다고 보도되었다. | ref-1459 | 아니오 | medium | 2022-05-28 | 병원 / 수행 자원 | — |
| f11 | [사실] | 싱가포르 국가 표준 Technical Reference 93(TR 93)은 자율 로봇과 승강기·자동문 같은 건물 설비 사이의 데이터 교환 지침을 정하며, KONE 의 차세대 승강기는 TR 93 에 맞춘 클라우드 연결·개방 API 로 RoMi-H 로봇과 시험 연동되었다. | ref-1458 | 아니오 | medium | 2022-05-28 | — | — |
| f12 | [사실] | 연계 대상: Schulze 외(Frontiers in Robotics and AI, 2025-02)의 요양 시설·대학 사무 건물 실증에서 로봇은 승강기 문 상태를 자기 라이다로 직접 판단했고, 승강기 문은 6초만 열려 있었으며, 의도하지 않은 층에서 멈춘 이유를 구분하지 못했고, 119건 작업 가운데 문·승강기가 얽힌 작업의 약 14%가 실패했으며 주된 원인은 위치추정·검출 오류였다. | ref-1460 | 아니오 | medium | 2025-02-25 | 기타 / 예외·성과 | — |
| f13 | [추정] | 승강기 문처럼 열림 상태가 수 초만 유지되는 설비에서는 '열림' 정보의 허용 경과 시간을 그 설비의 유지 시간보다 짧게 잡아야 하고, 설비가 보고한 상태와 로봇이 직접 관측한 상태를 함께 확인해야 할 것으로 보인다. | ref-1460, ref-286 | 아니오 | low | 2026-10-09 | 기타 / 제약 | — |
| f14 | [사실] | 김지형(2023)은 두산 로봇팔(Modbus)과 KUKA 로봇팔(UDP 소켓)을 스마트 커넥터로 OPC UA Pub/Sub 서버에 모아 3D 실시간 디지털 트윈으로 연결했으며, 초당 50개 이상 노드 수집과 약 70 fps 렌더링을 보고했으나 종단 간 지연·동기화 오차 수치는 제시하지 않았다. | ref-1462, ref-296 | 아니오 | medium | 2023-08-31 | 제조 공장 | — |
| f15 | [사실] | 같은 논문(DOI 10.7236/JIIBC.2023.23.4.189, 23권 4호 189-196쪽, 발행처 국제인공지능학회)을 KCI 는 지능정보논문지로, KoreaScience 는 한국인터넷방송통신학회논문지로 적어, 게재지 이름 충돌(oq-037)은 같은 논문에 대한 두 등재 정보의 차이로 확인된다. | ref-296, ref-1462 | 아니오 | medium | 2026-10-09 | — | — |
| f16 | [사실] | OPC UA 의 DataValue 는 값과 함께 데이터 원천이 붙인 시각(sourceTimestamp), 서버가 값을 받거나 정확하다고 안 시각(serverTimestamp), 품질 상태 코드(Good·Uncertain·Bad)를 담고, 클라이언트는 값을 쓰기 전에 최소한 상태 코드의 심각도를 확인해야 한다. | ref-288 | 아니오 | medium | 2026-10-09 | — | — |
| f17 | [사실] | W3C SOSA 온톨로지는 관측 활동이 끝난 시각(resultTime)과 관측 결과가 대상에 적용되는 시각(phenomenonTime)을 구분한다. | ref-030 | 아니오 | medium | 2017-10-19 | — | 원문 미열람 |
| f18 | [사실] | VDA 5050 3.0.0 에서 로봇 상태 메시지는 관련 사건이 생기거나 최소 30초마다 발행되고, 시각은 ISO 8601 UTC 밀리초 형식이며, 이번에 읽은 범위에서 시계 동기화 요구는 찾지 못했고, connection 토픽은 관제가 로봇 상태 점검에 쓰지 말라고 적는다. | ref-031, ref-051 | 아니오 | medium | 2026-10-09 | — | — |
| f19 | [사실] | VDA 5050 3.0.0 에서 관제가 구역·간선 사용 요청을 허가할 때 허가 만료 시각(leaseExpiry)을 붙일 수 있고, 그 시각이 지나면 허가는 무효로 보아 요청 상태를 EXPIRED 로 바꾸며, 관제는 같은 requestId 로 새 만료 시각을 보내 연장한다. | ref-031 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f20 | [추정] | 허가에 만료 시각을 붙이는 VDA 5050 의 방식과 연결 상실 시 값을 STALE 로 표시하는 Sparkplug 의 방식을 설비 상태에 적용하면, '문 열림' 같은 관측에 유효 만료 시각을 붙이고 지나면 재확인을 요구하는 규칙으로 허가 경과 시간 문제를 다룰 수 있을 것으로 보인다. | ref-031, ref-287 | 아니오 | low | 2026-10-09 | 제약 | — |
| f21 | [사실] | VDA 5050 3.0.0 은 위치추정 품질 점수(localizationScore)와 편차 범위(deviationRange)를 로그·시각화 용도로만 쓰라고 정하고, 판단에 쓸 수 있는 신호로는 위치추정 여부(localized: true 면 x·y·theta 를 믿을 수 있음)를 둔다. | ref-031, ref-051 | 아니오 | medium | 2026-10-09 | — | — |
| f22 | [추정] | VDA 5050 을 따르는 로봇에 대해 ROP 가 위치를 얼마나 믿을지 판단할 때 품질 점수·편차 범위를 판단 논리로 쓰면 규격의 용도 규정과 어긋나므로, 위치추정 여부와 보고 시각, 그리고 설비·다른 로봇 관측과의 대조를 판단 근거로 삼아야 할 것으로 보이며, 이는 현재 페이지 9절의 '품질 점수·편차 범위로 판단' 서술의 수정이 필요함을 뜻한다(oq-028). | ref-031, ref-051 | 아니오 | low | 2026-10-09 | — | — |
| f23 | [사실] | Rosen·Mason·Leonard(ICRA 2016)는 반정적 환경의 특징이 시간이 지나며 남아 있을지 사라질지를 확률 생성 모델로 기술하고, 각 특징이 아직 존재하는지에 대한 믿음을 매 순간 정확히 온라인 계산하는 재귀 베이즈 추정기인 지속성 필터(persistence filter)를 제시했다. | ref-1454 | 아니오 | medium | 2016-06 | — | — |
| f24 | [사실] | Perpetua(Saavedra-Ruiz 외, IROS 2025)는 지속성 필터와 출현 필터를 혼합·연결해 반정적 특징이 사라지거나 다시 나타날 확률을 추정하고, 특징 변화에 대한 사전 지식을 넣고 온라인으로 적응하며, 관측 누락에 강하다고 보고했다. | ref-1455 | 아니오 | medium | 2025-07-24 | — | — |
| f25 | [추정] | 지속성 필터 계열 방법은 '몇 초까지 믿는다'는 고정 임계값 대신 마지막 관측 뒤 시간에 따라 상태 믿음을 낮추는 방식으로 오래된 관측을 다룰 수 있게 하지만, 이번에 확인한 적용 대상은 로봇 지도의 특징이며 문·승강기 같은 설비 상태에 적용한 사례는 찾지 못했다. | ref-1454, ref-1455 | 아니오 | low | 2026-10-09 | 제약 | — |
| f26 | [사실] | ISO/TC 299 의 ISO/AWI 26159-2(로봇 응용을 위한 기반시설 — 승강기·자동문 연동 요구사항)는 2025-11-13 신규 과제로 등록된 초안 단계로, 로봇–승강기·로봇–자동문 연동의 최소 데이터 교환·하드웨어 요구·안전 고려사항과 화재 대피 같은 비상 상황, 정전 같은 비정상 상황의 통신을 다루되 특정 메시지 프로토콜은 범위에서 뺀다. | ref-1456 | 아니오 | medium | 2025-11-13 | — | — |
| f27 | [사실] | ISO/TC 178 의 ISO/CD TS 8100-11(승강기와 다른 시스템의 상호운용)은 2026-08-28 의견 수렴이 끝난 위원회 초안으로, 원격 감시·원격 호출 등록·건물 자동화 연동·로봇(AGV·MAR) 연동의 네 사용 사례를 위한 승강기 상호운용 온톨로지와 안전 관련 기능을 정하고 oneM2M·OPC UA 를 적용 예로 든다. | ref-1457 | 아니오 | medium | 2026-08-28 | — | — |
| f28 | [추정] | 2026-10-09 기준 로봇–승강기·자동문 인터페이스의 국제 표준은 초안 단계이고 공개된 범위 설명과 싱가포르 TR 93 소개 자료 어디에도 설비 상태를 몇 초까지 믿을지 정한 내용은 보이지 않아, oq-034 는 여전히 열린 질문으로 보인다. | ref-1456, ref-1457, ref-1458 | 아니오 | low | 2026-10-09 | 제약 | — |
| f29 | [사실] | Yang·Liew(arXiv, 2025-10)는 정밀 시간 프로토콜(PTP)로 로봇들의 운영체제 시계를 마이크로초 수준으로 맞췄지만, 로봇 컴퓨터(NUC 11)의 무선랜 카드가 PTP 에 필요한 하드웨어 시각 기록을 지원하지 않아 실험 전에 유선 이더넷으로 동기화했다고 적었다. | ref-1463 | 아니오 | medium | 2025-10-10 | — | — |
| f30 | [사실] | Sparkplug 사양은 MQTT 브로커가 유언 메시지로 대신 보낸 노드 종료(NDEATH)의 시각은 실제 종료 시각이 아니므로 호스트가 자기 수신 UTC 시각으로 오프라인을 표시하게 하고, 이를 위해 엣지 노드와 호스트의 시계를 NTP 같은 방법으로 맞추도록 요구한다. | ref-287 | 아니오 | medium | 2026-10-09 | 예외·성과 | — |
| f31 | [추정] | 무선으로 연결된 이기종 로봇은 마이크로초 수준 동기화를 기대하기 어렵고 VDA 5050 이 시계 동기화를 요구하지 않으므로, ROP 는 로봇이 붙인 시각과 자기 수신 시각을 함께 기록하고 둘의 차이로 시계 오차를 추정해 상태의 경과 시간을 계산하는 방식이 필요할 것으로 보인다(oq-035). | ref-1463, ref-031, ref-287 | 아니오 | low | 2026-10-09 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-030 | W3C / OGC | Semantic Sensor Network Ontology | 2017-10-19 | 표준 | medium | 2026-10-09 | https://www.w3.org/TR/vocab-ssn/ | 예 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-10-09 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | 표준 | high | 2026-10-09 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 아니오 |
| ref-286 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg | 아니오 |
| ref-287 | Eclipse Foundation (eclipse-sparkplug GitHub) | Sparkplug Specification — Chapter 5 Operational Behavior (Sparkplug_5_Operational_Behavior.adoc) | 미확인 | 표준 | medium | 2026-10-09 | https://github.com/eclipse-sparkplug/sparkplug/blob/master/specification/src/main/asciidoc/chapters/Sparkplug_5_Operational_Behavior.adoc | 아니오 |
| ref-288 | OPC Foundation | OPC Unified Architecture – Part 4: Services - 7.11 DataValue | 미확인 | 표준 | high | 2026-10-09 | https://reference.opcfoundation.org/specs/OPC-10000-4/7.11 | 아니오 |
| ref-296 | 김지형 | OPC UA를 활용한 이기종 로봇의 실시간 디지털 트윈 설계 및 구현 | 2023 | 논문 | medium | 2026-10-09 | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002993454 | 아니오 |
| ref-1449 | Deubert, D., Klingel, L., & Selig, A. (arXiv; The International Journal of Advanced Manufacturing Technology 2024 표기) | Online Simulation at Machine Level: A Systematic Review | 2024-01-15 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2401.07841 | 아니오 |
| ref-1450 | Galka, S. (Winter Simulation Conference 2024) | Reducing Transient Behavior in Simulation-Based Digital Twins: A Novel Initialization Approach for Order Picking Systems | 2024 | 논문 | medium | 2026-10-09 | https://informs-sim.org/wsc24papers/con211.pdf | 예 |
| ref-1451 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_fleet_msgs/msg/LaneRequest.msg | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_fleet_msgs/msg/LaneRequest.msg | 아니오 |
| ref-1452 | Open Robotics Discourse (open-rmf 질의응답 #414) | How to inform RMF that lift or door are not available? (#414) | 2024-01-13 | 오픈소스 문서 | medium | 2026-10-09 | https://discourse.openrobotics.org/t/how-to-inform-rmf-that-lift-or-door-are-not-available-414/44744 | 아니오 |
| ref-1453 | Open Robotics (open-rmf, rmf_traffic API 문서) | Class LaneClosure — rmf_traffic API documentation | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://openrmf.readthedocs.io/projects/rmf-traffic/en/latest/api/classrmf__traffic_1_1agv_1_1LaneClosure.html | 아니오 |
| ref-1454 | Rosen, D. M., Mason, J., & Leonard, J. J. (MIT DSpace; ICRA 2016) | Towards lifelong feature-based mapping in semi-static environments | 2016-06 | 논문 | medium | 2026-10-09 | https://dspace.mit.edu/handle/1721.1/107620 | 아니오 |
| ref-1455 | Saavedra-Ruiz, M., Nashed, S. B., Gauthier, C., & Paull, L. (arXiv; IROS 2025 채택 표기) | Perpetua: Multi-Hypothesis Persistence Modeling for Semi-Static Environments | 2025-07-24 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2507.18808 | 아니오 |
| ref-1456 | ISO (ISO/TC 299 Robotics) | ISO/AWI 26159-2 Robotics — Infrastructure for robot applications — Part 2: Requirements for interfacing with lifts (elevators) and automatic doorways | 미확인 | 표준 | medium | 2026-10-09 | https://www.iso.org/standard/92741.html | 아니오 |
| ref-1457 | ISO (ISO/TC 178 Lifts, escalators and moving walks) | ISO/CD TS 8100-11 Lifts for the transport of persons and goods — Part 11: Interoperability between lift and other systems | 미확인 | 표준 | medium | 2026-10-09 | https://www.iso.org/standard/73063.html | 아니오 |
| ref-1458 | Changi General Hospital (CGH) | Changi General Hospital, CapitaLand Investment and KONE collaborate to advance the integration of robotics in buildings | 2022-05-28 | 정부·연구기관 | medium | 2026-10-09 | https://www.cgh.com.sg/news/announcements/changi-general-hospital-capitaland-investment-and-kone-collaborate-to-advance-the-integration-of-robotics-in-buildings | 아니오 |
| ref-1459 | The Straits Times (SingHealth 게재, Wong Shiying) | New software enables different robots to communicate with each other and building infrastructure | 2022-05-28 | 기사 | medium | 2026-10-09 | https://www.singhealth.com.sg/news/tomorrows-medicine/new-software-enables-different-robots-to-communicate-with-each-other-and-building-infrastructure | 아니오 |
| ref-1460 | Schulze, P. R., Müller, S., Müller, T., & Gross, H.-M. (TU Ilmenau; Frontiers in Robotics and AI) | On realizing autonomous transport services in multi story buildings with doors and elevators | 2025-02-25 | 논문 | high | 2026-10-09 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1546894/full | 아니오 |
| ref-1461 | 메디포뉴스 (이형규) | 용인세브란스병원, 지능형 의료서비스로봇 생태계 구축 | 2022-11-18 | 기사 | low | 2026-10-09 | https://medifonews.com/news/article.html?no=172554 | 아니오 |
| ref-1462 | 김지형 (KoreaScience 수록, 한국인터넷방송통신학회논문지 표기) | OPC UA를 활용한 이기종 로봇의 실시간 디지털 트윈 설계 및 구현 (Design and Implementation of Real-time Digital Twin in Heterogeneous Robots using OPC UA) | 2023-08-31 | 논문 | medium | 2026-10-09 | https://koreascience.or.kr/journal/view.jsp?kj=OTNBBE&py=2023&vnc=v23n4&sp=189 | 아니오 |
| ref-1463 | Yang, Q., & Liew, S. C. (The Chinese University of Hong Kong, arXiv) | Multi-robot Rigid Formation Navigation via Synchronous Motion and Discrete-time Communication-Control Optimization | 2025-10-10 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2510.02624 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md | 5, 6, 7, 8, 9, 10, 11 | 갱신(update) 차등 반영. 5절 적용 사례(현장 유형 명시): 병원 사례 f9(용인세브란스, 한국)·f10(CGH RoMi-H), 기타 현장 사례 f12·f13(요양 시설·대학 건물, 연계 대상 표시), 제조 공장 사례 f14 — 물류창고 외 현장 유형 보강 / 6절 대표 접근법: f16(OPC UA 원천·서버 시각과 품질 코드), f17(SOSA 관측 시각 구분), f19·f20(허가 만료 시각 방식), f23~f25(지속성 필터 계열), f29~f31(시계 동기화와 수신 시각) / 7절 표준: f26·f27(ISO 초안 2건), f11(싱가포르 TR 93), f16(ref-288 원문 확인), f18·f19·f21(VDA 5050 3.0.0) / 8절 연구: f5~f7(온라인 시뮬레이션 초기화), f12, f14, f23·f24, f29 / 9절 책임 경계: f21·f22 — 현재 표의 '품질 점수·편차 범위로 신뢰 판단' 서술이 VDA 5050 의 '로그·시각화 전용' 규정과 어긋나므로 위치추정 여부·보고 시각·교차 관측 기준으로 고칠 것 / 10절 연결: 트랙 floorplan-recognition 단계 3 반영 제안 2건 검토 결과 — 제안 1(실행 2026-09-25-65) → f1~f4(5. 로봇 능력·작업 표현·15. 지도·공간·위치 모델의 정적 대조와 이 영역의 현재 상태 층 분리, 22. 설비·건물 시스템 연동·27. 다중 로봇 경로·교통 관리 — MAPF 와 차선 폐쇄로 연결; 제안 원문의 f20 어포던스 연구는 이번에 재확인하지 못해 제외), 제안 2(실행 2026-09-25-70) → f5~f8(34. 시뮬레이션·예측용 디지털 트윈에 현재 상태 초기값 공급; 제안이 든 IFAC 2024 연구는 재확인하지 못해 ref-1449·ref-1450 으로 대체, 제안의 옛 번호 '8.'·'22.'는 새 번호 18·34 로 표기) / 11절 열린 질문: oq-034 에 f26~f28, oq-035 에 f18·f29~f31, oq-028 에 f21·f22, oq-037 에 f15 부분 근거(해결 제안 없음)와 새 질문 3건. 다음 실행 후보: 15. 지도·공간·위치 모델 페이지의 위치추정 신뢰도 서술에 f21 반영 검토. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 지속성 필터 | Persistence Filter | 반정적 환경의 특징이 마지막 관측 뒤에도 아직 남아 있을 확률을 시간에 따라 재귀적으로 계산하는 베이즈 추정기다. |
| 허가 만료 시각 | Lease Expiry (VDA 5050 leaseExpiry) | VDA 5050 에서 관제가 구역·간선 사용 허가에 붙이는 만료 시각으로, 이 시각이 지나면 허가는 무효가 되어 요청 상태가 EXPIRED 로 바뀐다. |
| 온라인 시뮬레이션 | Online Simulation | 운영 중인 실제 시스템의 현재 상태로 초기화하거나 동기화해 가까운 미래의 결과를 예측하는 데 쓰는 시뮬레이션이다. |
| 정밀 시간 프로토콜 | Precision Time Protocol (PTP, IEEE 1588) | 네트워크로 연결된 장치들의 시계를 하드웨어 시각 기록의 도움을 받아 마이크로초 이하 수준으로 맞추는 시계 동기화 프로토콜이다. |

## 열린 질문

새로 생긴 질문:

- 로봇이 직접 관측한 승강기·문 상태와 설비 제어기가 보고한 상태가 다를 때 어느 쪽을 기준으로 통과·탑승을 확정하는지 정한 표준이나 현장 사례가 있는가? | 관련 영역: 18. 실시간 세계 상태·데이터 일관성, 22. 설비·건물 시스템 연동 | 근거: f13 | 종류: 일반
- 지속성 필터처럼 마지막 관측 뒤 시간에 따라 믿음을 낮추는 확률 모델을 문·승강기·충전기 같은 설비 상태의 허용 경과 시간 판단에 적용한 연구나 사례가 있는가? | 관련 영역: 18. 실시간 세계 상태·데이터 일관성, 46. 예측·학습 기반 최적화 | 근거: f25 | 종류: 일반
- 실시간 세계 상태를 예측 시뮬레이션의 초기값으로 넘길 때 어떤 상태 항목·품질·시각 정보를 넘겨야 하는지 정한 인터페이스가 다중 이동로봇 운영에 쓰인 사례가 있는가? | 관련 영역: 18. 실시간 세계 상태·데이터 일관성, 34. 시뮬레이션·예측용 디지털 트윈 | 근거: f8 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 22 · 교차 확인: 1
- 예산 사용량: 검색 15회 · 신규 출처 15건
- 미확인 항목:
    - 트랙 반영 제안 2가 든 IFAC 2024 연구(운영 중 예측 시뮬레이션의 실부하 상태 초기화)를 다시 찾지 못해 다른 출처로 대체함
    - 트랙 반영 제안 1의 어포던스 상태 연구(트랙 실행 2026-09-25-65 의 f20)를 재확인하지 못해 이번 브리프에 넣지 않음
    - ref-1450 Galka(WSC 2024) PDF 본문 추출 실패, 초록(검색 결과) 범위로만 사용하고 개선 폭 수치 미확인
    - ISO/AWI 26159-2·ISO/CD TS 8100-11·싱가포르 TR 93 본문 미열람(초안·유료), 상태 신선도 조항 유무 미확인
    - f9 용인세브란스 사례는 기사 1건 기준이며 교차 확인 못함
    - f15 oq-037: KCI 와 KoreaScience 가 같은 DOI·권호·쪽·발행처에 서로 다른 학술지명을 적어, 어느 이름이 현재 공식 명칭인지(학술지 명칭 변경 여부) 미확인
    - VDA 5050 3.0.0 명세 마지막 7,761자는 읽지 않음
    - 국내 로봇–승강기 연동 TTA·KS 표준의 상태 갱신 주기·응답 시간 항목 미확인
- 범위 경계 위반 의심:
    - f12: 승강기 문 상태 라이다 검출·위치추정은 분류 원문 19장 '로봇 자체 지능·제어' 경계라 claim 을 '연계 대상: '으로 시작하고, ROP 쪽 함의는 f13 에서 상태 대조 규칙으로만 서술
    - f26·f27·f11: 승강기·자동문 제어와 비상 운전은 '시설·설비 제어' 경계의 연계 대상이며, 이 브리프는 데이터 교환 항목(ROP 가 받는 상태)의 범위로만 다룸
    - f29: 로봇 내부 시계·네트워크 카드는 제조사 몫이며 ROP 는 수신 시각 기록·오차 추정(f31)만 맡는 것으로 서술
- 한계: web_fetch_available: true · fetch_mode full. 실행 유형 update 이므로 정정 요청(없음)·빈 절·트랙 반영 제안 2건·대상 영역 열린 질문(oq-028·oq-034·oq-035·oq-037)에 해당하는 것만 조사했다. 검색 15회/30, 신규 출처 15건/15(ref-1449~ref-1463, 예약 구간 안)로 신규 출처 상한에 도달해, 더 찾지 않은 것: 국내 TTA·KS 로봇–승강기 연동 표준 본문, 상업 시설 현장의 상태 통합 사례, 시계 동기화 허용 오차 기준. 신규 출처 가운데 ref-1450 을 뺀 14건은 원문(또는 초록 페이지)을 열었다. 재사용 7건 가운데 ref-031(github_raw)·ref-030(github_raw, 편집자 초안 공식 산출물)·ref-288·ref-296(webfetch)은 이번에 열었고, ref-051·ref-286·ref-287 은 입력의 원문 텍스트(data/source_texts)를 읽었다. 교차 확인 1건(f7: 온라인 시뮬레이션 실제 상태 초기화, 단 ref-1450 은 초록만). 벤더 주장 없음. 한국 자료: ref-1461(용인세브란스, 병원), ref-1462·ref-296(김지형 2023, 제조 공장). 현장 유형: 물류창고(f6), 병원(f9·f10), 제조 공장(f14), 기타(f12·f13 요양 시설·대학 건물). 18. 실시간 세계 상태·데이터 일관성(현재 상태 공급)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험)을 f8 에서 구분했다. 트랙 반영 제안 처리: 제안 1(2026-09-25-65) → f1~f4, 제안 2(2026-09-25-70) → f5~f8, 제안 문구의 옛 번호(6·5·8·22)는 새 번호(15·5·18·34)로 바꿔 적었다. 열린 질문 oq-028(f21·f22), oq-034(f26~f28), oq-035(f18·f29~f31), oq-037(f15)에는 부분 근거만 더했고 해결 제안은 없다. f21 은 현재 페이지 9절 표의 서술(품질 점수·편차 범위로 신뢰 판단)과 VDA 5050 원문이 어긋날 수 있음을 보이므로 9절 수정을 제안했다. 입력 누락 없음. 우선 지정 질문 없음.
```

### runs/2026-10-09-10/research.md

```markdown
# 리서치 브리프 2026-10-09-10

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-09-10 |
| 날짜 | 2026-10-09 |
| 실행 유형 | category_link (대분류 연결) |
| 대상 영역 | 해당 없음 |
| 대분류 | N. 보안·개인정보 |

## 갭(비어 있거나 약한 섹션)

- N. 보안·개인정보 대분류 페이지의 '다른 대분류와의 연결' 절이 '아직 작성되지 않음' 상태다. 51. 인증·권한·격리, 52. 통신 보호·위협 관리·감사, 53. 개인정보·영상 데이터와 다른 16개 대분류의 연결이 정리되지 않았다
- 51. 인증·권한·격리 페이지는 이전 분류(2026-09-25) 기준이라 C. 채팅 기반 구성·운영, D. 공간·지도 모델, J. 현장 운영·관제의 40. 운영 절차·요청 창구, P. 거버넌스·법규·사회의 58. 다사업자 책임·계약·데이터와 잇는 근거가 페이지 안에 없다
- 51·52·53 페이지의 10절(다른 연구영역과의 연결)은 주제 페이지로 분리되어 있고 대분류 단위로 묶인 연결이 없다
- D. 공간·지도 모델 페이지는 N. 보안·개인정보와의 연결을 '근거 없음'으로 남겼다(지도 데이터의 접근 통제·개인정보)
- Q. 현장 유형별 적용 가운데 물류창고·상업 시설·기타 현장의 보안·개인정보 사례가 51·52·53 게시 페이지에 없다
- EU 사이버복원력법 보고 의무(2026-09-11 시행)와 EU 데이터법처럼 최근 시행된 규정이 게시 페이지에 반영되지 않았다

## 조사 질문

1. 누가 어떤 로봇에 무엇을 시킬 수 있는지 통제하고, 데이터와 사람의 정보를 어떻게 지킬 것인가? [분류원문]
2. 외부 유지보수 계정이 어느 로봇에 어떤 명령까지 내릴 수 있는가? [분류원문]
3. 51. 인증·권한·격리의 명령 권한·장비 인증은 B. 로봇 온톨로지(4·6·7)·F. 연동(20·22)·G. 계획·최적화(25)·H. 실행·협업·예외 복구(29)·K. 플랫폼 아키텍처·인프라(41)의 어느 인터페이스와 이어지는가? (oq-056, oq-082, oq-100, oq-113 관련)
4. 52. 통신 보호·위협 관리·감사의 위협·감사 기록은 C. 채팅 기반 구성·운영(12·13)·E. 사물·사람·실시간 상태(18)·J. 현장 운영·관제(37·38·40)·L. AI·학습 기술(44·47)·M. 안전(48·50)·O. 검증·도입·수명주기(54·55·57)와 어디서 만나는가? (oq-144, oq-246, oq-248, oq-291 관련)
5. 53. 개인정보·영상 데이터의 수집·보관 규칙은 D. 공간·지도 모델(15·16)·E. 사물·사람·실시간 상태(17·19)·L. AI·학습 기술(45·47)·P. 거버넌스·법규·사회(58·59·60)와 어떻게 이어지는가? (oq-259, oq-285, oq-214 관련)
6. 보안 인증·규제(IEC 62443, ISO 10218 개정, EU 사이버복원력법, EU 데이터법, 국내 로봇 보안모델)는 A. 기획·사업(1·2·3)에 어떤 요구를 넘기는가?
7. N. 보안·개인정보의 적용 사례는 Q. 현장 유형별 적용의 일곱 현장 유형 가운데 어디에 근거가 있으며 한국 자료는 무엇이 있는가?

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ A. 기획·사업의 1. 기술·시장·업체 동향: 과학기술정보통신부와 한국인터넷진흥원(KISA)은 2026-03-05 로봇 보안모델 고도화판과 로봇 보안요구사항 해설서를 공개했고, 피지컬 AI 확산과 유럽·북미 사이버보안 규제 강화를 반영해 기업이 개발·수출 과정의 보안 요구를 파악하게 하는 것을 목적으로 밝혔다. | ref-1373, ref-1111 | 아니오 | medium | 2026-03-05 | — | — |
| f2 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ A. 기획·사업의 3. 경제성·조달·사업 모델: KUKA 는 iiQKA.OS2 운영체제와 KR C5-2 제어기 플랫폼이 IEC 62443-4-2 보안 수준 2(SL2) 인증을 받았고 로봇 제조사 가운데 처음이라고 2026-09-02 발표했으며, 발표문에는 인증 기관이 나오지 않는다. | ref-1375 | 아니오 | low | 2026-09-02 | — | 벤더 주장 |
| f3 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ A. 기획·사업의 3. 경제성·조달·사업 모델: IEC 62443 이 보안 수준을 정하고 로봇 제어기 단위의 인증 발표가 나오고 있으므로, 로봇·플랫폼 조달 요구에 구성요소 보안 인증 여부와 목표 보안 수준을 넣는 일이 3. 경제성·조달·사업 모델로 넘어갈 것으로 보이나, 플릿 관리 소프트웨어 단위의 인증 사례는 확인하지 못했다. | ref-1105, ref-1375 | 아니오 | low | 2026-10-09 | — | — |
| f4 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ A. 기획·사업의 2. 사용 사례·요구·책임 범위: 52. 통신 보호·위협 관리·감사 페이지는 ROP 가 자신이 여는 연결의 보안과 전체 연결 구조의 위협 모델을 맡고 로봇 제어기·펌웨어와 현장 망 보안은 제조사·시설 IT/OT 쪽 연계 대상으로 두므로, 이 보안 책임 경계가 2. 사용 사례·요구·책임 범위의 책임 범위 정의에 들어가야 할 것으로 보인다. | ref-1114, ref-1107, ref-009 | 아니오 | low | 2026-09-30 | — | — |
| f5 | [사실] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ B. 로봇 온톨로지의 4. 이기종 로봇 등록: VDA 5050 3.0.0 은 로봇이 새 인증서 묶음을 내려받아 활성화하게 하는 즉시 동작 updateCertificate 를 두고, 내려받기도 TLS 로 보호해야 하며 활성화 전에 인증서 체인을 검증하는 것이 바람직하다고 적는다. | ref-031 | 아니오 | medium | 2026-10-09 | — | — |
| f6 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ B. 로봇 온톨로지의 4. 이기종 로봇 등록·7. 온톨로지 검증·변경 관리, O. 검증·도입·수명주기의 57. 자산·소프트웨어 수명주기 관리: 로봇마다 인증서 교체 지원 여부와 인증서 판·만료를 등록 정보로 두고 교체 이력을 판 관리와 함께 다루면 인증서 교체 대상과 시점을 추적할 수 있을 것으로 보이며, 교체 승인과 실패 때 되돌림 책임은 열린 질문(oq-113)으로 남는다. | ref-031 | 아니오 | low | 2026-10-09 | — | — |
| f7 | [추정] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ B. 로봇 온톨로지의 4. 이기종 로봇 등록: 53. 개인정보·영상 데이터 페이지가 카메라 유무·촬영 사실 표시 수단·영상 전송 경로 기록과 로봇 인지 출력 필드 축소를 ROP 직접 범위로 보므로, 이런 개인정보 관련 속성이 4. 이기종 로봇 등록의 등록 항목으로 넘어갈 것으로 보인다. | ref-1145, ref-588 | 아니오 | low | 2026-09-30 | — | 원문 미열람 |
| f8 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ B. 로봇 온톨로지의 6. 온톨로지 기반 시스템·로봇 연동: ROS 2 접근 제어 정책은 인클레이브별로 토픽·서비스·액션 단위의 허용·거부를 두므로, '진단은 허용하고 이동은 막는' 명령 단위 권한을 걸려면 6. 온톨로지 기반 시스템·로봇 연동이 능력을 실제 명령에 묶을 때 권한 정책과 같은 명령 식별자를 공유해야 할 것으로 보인다. | ref-579, ref-405 | 아니오 | low | 2026-10-09 | 제약 | — |
| f9 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ C. 채팅 기반 구성·운영의 13. 대화형 기능의 신뢰·기반: OWASP LLM01:2025 는 프롬프트 주입을 사용자가 직접 넣는 직접 주입과 문서·웹 같은 외부 내용에 숨은 지시가 들어오는 간접 주입으로 나누고 완화책을 정리한다. | ref-1106 | 아니오 | medium | 2026-10-09 | — | 원문 미열람 |
| f10 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션: 대규모 언어 모델을 통합한 이동로봇 시스템에 대한 프롬프트 주입 공격 연구(Zhang 외, 2024-08)와 다중 에이전트 로봇 시스템에서 프롬프트가 로봇을 제어할 때의 프롬프트 주입 공격 연구(Nagaraja 외, 2026-08)가 있다. | ref-1113, ref-1112 | 아니오 | medium | 2026-08 | — | 원문 미열람 |
| f11 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ C. 채팅 기반 구성·운영의 13. 대화형 기능의 신뢰·기반·L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획: Robey 외는 언어 모델이 제어하는 로봇에서 탈옥 알고리즘 RoboPAIR 의 공격 성공률이 자주 100%에 이르렀다고 보고했고, Ravichandran 외의 RoboGuard 는 최악의 탈옥 공격에서 위험 계획 실행을 92% 이상에서 3% 미만으로 줄였다고 보고했다. | ref-857, ref-700 | 아니오 | medium | 2025-03 | 제약 | 원문 미열람 |
| f12 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션: Open-RMF REST API 를 언어 모델 도구로 노출하는 MCP 서버(Nayantra) 같은 구조에서는 탈옥된 모델이 해로운 동작을 낼 수 있으므로, 모델에 넘기는 도구·로봇·구역 권한을 최소로 제한하는 접근 통제가 분류 원문 C 주석의 '사람이 확인·승인한 계획만 실행' 원칙과 함께 두 대분류의 경계가 될 것으로 보인다. | ref-854, ref-857 | 아니오 | low | 2026-10-09 | 제약 | 원문 미열람 |
| f13 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션: '사람이 확인·승인한 계획만 실행'이 지켜졌음을 사후에 보이려면 누가 어떤 계획을 언제 승인했는지를 변조 탐지가 가능한 감사 기록으로 남겨야 할 것으로 보이며, 자율 에이전트 행동을 블록체인 기록과 언어 모델 설명으로 추적하는 구조 연구(2024-03)가 그 후보다. | ref-1110 | 아니오 | low | 2026-10-09 | 완료·인계 | 원문 미열람 |
| f14 | [사실] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ D. 공간·지도 모델의 16. 장소 의미·지도 관리: 개인정보보호위원회가 2026-09-14 발표한 로봇청소기 5개 브랜드 점검에서 집 내부 구조를 나타내는 지도 정보는 모든 제품이 기기에 저장하고 스마트폰에는 저장하지 않았으며 일부 제품은 서버에도 저장했고, 일부 사업자는 로봇청소기 접근통제와 개인정보 전송 암호화가 미흡했다. | ref-1372, ref-1141 | 아니오 | medium | 2026-09-14 | 가정 / 작업 대상 | — |
| f15 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리·53. 개인정보·영상 데이터 ↔ D. 공간·지도 모델의 15. 지도·공간·위치 모델·16. 장소 의미·지도 관리: 건물 내부 지도가 개인정보 점검 대상 정보로 다뤄지고 VDA 5050 이 지도를 관제가 지정한 링크에서 내려받게 하므로, ROP 가 보관·배포하는 지도의 저장 위치·전송 암호화·접근 권한을 정하는 일이 두 대분류를 잇는 지점이 될 것으로 보인다. | ref-1372, ref-031 | 아니오 | low | 2026-10-09 | — | — |
| f16 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성: Shen 외(2026-09, 프리프린트)는 ROS 2 에서 환경 변수 하나를 바꾸면 사전 빌드된 훅이 텔레메트리·제어 신호를 발행 전에 가로채고 주입할 수 있음을 보였고, Secure ROS 2 를 쓴 실제 Franka 로봇팔에서 약 3 ms 지터로 위조 텔레메트리를 넣어 AI 기반 탐지기 상대로도 87% 성공했다고 보고했다. | ref-1374 | 아니오 | medium | 2026-09-08 | — | — |
| f17 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성·J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석: 로봇이 보고하는 상태가 통신 보호 이전 단계에서 위조될 수 있고 위치 스푸핑이 배정을 무너뜨린다는 연구가 있으므로, 18. 실시간 세계 상태·데이터 일관성의 상태 신뢰도 판단과 38. 모니터링·이상 탐지·원인 분석은 암호화된 보고만 믿지 말고 설비 센서·다른 로봇 관측과 교차 확인해야 할 것으로 보인다(oq-082). | ref-1374, ref-494 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f18 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리·53. 개인정보·영상 데이터 ↔ E. 사물·사람·실시간 상태의 17. 작업 대상·자산 식별과 인계 추적: 병원 운반 로봇 Zena RX 는 생체 인식과 직원 PIN 으로 잠금 칸을 연다고 제조사가 밝히고 공동주택 배달 로봇 도입 계획은 비밀번호로 적재함을 열게 했으므로, '누구에게 넘겼는가' 기록은 인증 수단과 생체·전화번호 처리 규칙에 기댈 것으로 보인다. | ref-1299, ref-1301 | 아니오 | low | 2026-10-09 | 병원 / 완료·인계 | 원문 미열람, 벤더 주장 |
| f19 | [사실] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ E. 사물·사람·실시간 상태의 19. 사람·보행자 모델: ROS 규약 제안 REP-155(Draft)는 사람마다 영속 ID 를 두고 얼굴·몸·음성 ID 를 후보 대응으로 연결하며, 개인정보·동의는 다루지 않는다. | ref-1173 | 아니오 | medium | 2022-01-11 | — | 원문 미열람 |
| f20 | [사실] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ F. 연동의 20. 로봇·제조사 관제 연동: 2025-08 한 보안 연구자는 Pudu Robotics 로봇 관리 소프트웨어가 유효한 인증 토큰만 확인하고 그 뒤 권한을 검사하지 않아, 교차 사이트 스크립팅이나 체험 계정으로 얻은 토큰으로 주문을 바꾸고 로봇을 다른 위치로 보내고 이름을 바꿀 수 있었다고 공개했다. | ref-1368, ref-1369 | 아니오 | medium | 2025-08-29 | 상업 시설 / 예외·성과 | — |
| f21 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ F. 연동의 20. 로봇·제조사 관제 연동: 미국 CISA 권고 ICSA-22-102-05(2022-04-12)는 병원 자율이동로봇 TUG 를 제어하는 Home Base Server 에서 인증 없이 웹소켓으로 로봇을 제어할 수 있는 취약점(CVE-2022-1070, CVSS 9.8)과 인가 누락 취약점을 공개했다. | ref-1107 | 아니오 | medium | 2022-04-12 | 병원 / 예외·성과 | 원문 미열람 |
| f22 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ F. 연동의 20. 로봇·제조사 관제 연동: 식당 서빙 로봇과 병원 운반 로봇 사례 모두 제조사 플릿 서버·관리 API 의 인증·인가 결함이 로봇 제어로 이어졌으므로, ROP 가 제조사 관제를 연결할 때 연결 계정의 권한 범위와 인가 확인을 연동 승인 조건으로 둬야 할 것으로 보인다(oq-100). | ref-1368, ref-1107 | 아니오 | low | 2026-10-09 | 제약 | — |
| f23 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ F. 연동의 21. 상호운용 표준·적합성: VDA 5050 3.0.0 은 범위 절에서 보안 통신·데이터 보호의 메커니즘·기술·절차를 정하지 않는다고 밝히고, 프로토콜 보안은 브로커 구성으로 다뤄야 하며 이 지침에서는 다루지 않는다고 적는다. | ref-031 | 아니오 | medium | 2026-10-09 | — | — |
| f24 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ F. 연동의 21. 상호운용 표준·적합성: 상호운용 규격이 통신 보안을 범위 밖 브로커 구성에 맡기므로 21. 상호운용 표준·적합성의 적합성 시험과 브로커·API 의 상호 인증·TLS 설정 확인은 별도 경로로 관리해야 할 것으로 보이며, 그 최소 요구를 정한 공개 보안 프로파일은 확인하지 못했다(oq-246). | ref-031, ref-1105 | 아니오 | low | 2026-10-09 | — | — |
| f25 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ F. 연동의 22. 설비·건물 시스템 연동: 승강기 같은 설비를 조작하는 서비스 로봇(FlashBot)도 같은 관리 API 결함의 대상이 될 수 있다고 보도되었으므로, 로봇 관제·설비 어댑터 구성요소를 SROS 2 인클레이브처럼 별도 신원·접근 규칙으로 나눠 설비 명령 권한을 제한하는 설계가 두 대분류의 경계가 될 것으로 보인다(oq-056). | ref-1369, ref-405 | 아니오 | low | 2026-10-09 | 제약 | — |
| f26 | [사실] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ G. 계획·최적화의 25. 작업 배정 — MRTA: Francos 외(2026-08, 프리프린트)는 위치 스푸핑으로 오염된 에이전트가 롤아웃 기반 다중 로봇 배정·경로 계획의 비용 개선을 없앨 수 있다고 보고, 스푸핑 공격 모델과 탐지된 적대 에이전트를 이후 계획에서 빼는 방법을 제안했다. | ref-494 | 아니오 | medium | 2026-08 | — | 원문 미열람 |
| f27 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ G. 계획·최적화의 25. 작업 배정 — MRTA·27. 다중 로봇 경로·교통 관리 — MAPF: 제조사 관리 API 를 거쳐 주문을 바꾸거나 로봇 위치를 옮길 수 있었던 사례가 있으므로, ROP 의 배정·교통 계획은 자신이 내리지 않은 임무 변경·이동을 로봇 상태에서 감지해 해당 로봇을 계획에서 보류하는 규칙이 필요할 것으로 보인다. | ref-1368 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f28 | [사실] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ H. 실행·협업·예외 복구의 29. 명령·작업 실행의 신뢰성: VDA 5050 3.0.0 에서 updateCertificate 동작은 실행 중에는 인증서를 내려받아 설치 중이라는 상태로, 실패하면 내려받기 또는 설치 실패로 보고되므로, 보안 명령도 일반 명령처럼 실행 확인·실패 처리 대상이 된다. | ref-031 | 아니오 | medium | 2026-10-09 | 완료·인계 | — |
| f29 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성: 식당 서빙 로봇 관리 API 결함으로 영업 중 플릿 전체 작업을 취소하거나 멈출 수 있었다고 보도되었으므로, 보안 사고로 플릿 일부·전체를 격리하고 수동 운영으로 넘어가는 시나리오가 32. 예외 복구·재계획·업무 연속성의 복구 절차에 들어가야 할 것으로 보인다. | ref-1368, ref-1369 | 아니오 | low | 2026-10-09 | 상업 시설 / 예외·성과 | — |
| f30 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈: Carr 외(2022)는 ROS 로 구동되는 시스템에서 디지털 트윈에 대한 중간자 공격이 물리 로봇의 실패로 이어질 수 있으며, 이는 산업용 로봇팔과 자율이동로봇 모두에 해당한다고 보고했다. | ref-1304 | 아니오 | medium | 2022-11-17 | — | 원문 미열람 |
| f31 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사·53. 개인정보·영상 데이터 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현: 가정한 미래를 실험하는 시뮬레이션과 실제 상황 재현에 운영 기록·영상을 입력으로 쓰면 그 기록의 무결성과 '재현' 목적의 이용 범위를 함께 정해야 할 것으로 보이며, 이는 현재 상태를 표현하는 18. 실시간 세계 상태·데이터 일관성의 상태 신뢰도 문제(f17)와 구분된다. | ref-1304, ref-588 | 아니오 | low | 2026-10-09 | — | 원문 미열람 |
| f32 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ J. 현장 운영·관제의 37. 관제 화면·실행 기록: Fernández-Becerra 외(2024-03)는 자율 에이전트의 행동을 블록체인 기반 기록과 대규모 언어 모델 설명으로 남겨 책임 추적성과 설명 가능성을 높이는 구조를 제안했다. | ref-1110 | 아니오 | medium | 2024-03 | — | 원문 미열람 |
| f33 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ J. 현장 운영·관제의 37. 관제 화면·실행 기록: 업계 해설에 따르면 EU 기계류 규정 (EU) 2023/1230 은 변조 보호, 개입 증거 기록, 안전 소프트웨어 판 추적 로그를 요구하며 2027-01-20 전면 적용된다. | ref-1109 | 아니오 | medium | 2026-08-27 | — | 원문 미열람 |
| f34 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ J. 현장 운영·관제의 40. 운영 절차·요청 창구: Pudu 사례에서 연구자의 신고(2025-08-12 시작)는 보안 신고 창구가 없어 응답을 받지 못하다가 고객사(Skylark Holdings·Zensho)에 알린 뒤에야 처리되었고, 제조사는 이후 취약점을 고치고 보안 대응 센터와 신고 주소를 만들었다. | ref-1368, ref-1369 | 아니오 | medium | 2025-09-05 | 상업 시설 / 예외·성과 | — |
| f35 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ J. 현장 운영·관제의 40. 운영 절차·요청 창구·O. 검증·도입·수명주기의 57. 자산·소프트웨어 수명주기 관리·P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스: EU 사이버복원력법에 따라 2026-09-11 부터 디지털 요소 제품 제조자는 적극 악용되는 취약점과 중대 사고를 ENISA 단일 보고 플랫폼으로 알려야 하며, 인지 후 24시간 안에 조기 경보, 72시간 안에 통지, 취약점은 시정 조치가 나온 뒤 14일 안에 최종 보고를 낸다. | ref-1367 | 아니오 | medium | 2026-09-11 | 예외·성과 | — |
| f36 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ J. 현장 운영·관제의 40. 운영 절차·요청 창구: 신고 창구가 없던 제조사 사례와 24·72시간 보고 시한을 함께 보면, 여러 제조사 로봇을 운영하는 현장의 요청 창구에 보안 취약점·사고 접수와 제조사·ROP 사업자 사이 통보 경로를 두는 일이 40. 운영 절차·요청 창구로 넘어갈 것으로 보이며, 플랫폼 사업자의 보고 의무 해당 여부는 열린 질문(oq-291)이다. | ref-1367, ref-1368 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f37 | [사실] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ K. 플랫폼 아키텍처·인프라의 41. 플랫폼 아키텍처·외부 API: Open-RMF 문서는 웹 대시보드를 TLS 로 제공하고 OIDC 로 사용자 역할을 담은 서명 토큰을 API 서버에 보내 역할에 따라 접근을 허용하며, ROS 2 쪽 구성요소는 SROS 2 인클레이브로 권한을 나눈다고 설명한다. | ref-405 | 아니오 | medium | 2026-10-09 | — | — |
| f38 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조: ROS 2 는 DDS 보안 규격의 인증·접근 통제·암호화 플러그인을 쓰고, ROS 2 위협 모델 초안은 보안이 꺼진 시스템에서는 어떤 노드든 어떤 토픽에나 발행할 수 있어 신원 위조와 명령 가로채기가 가능하다고 정리한다. | ref-009, ref-010 | 아니오 | medium | 2026-10-09 | — | — |
| f39 | [사실] | N. 보안·개인정보의 51. 인증·권한·격리·53. 개인정보·영상 데이터 ↔ K. 플랫폼 아키텍처·인프라의 43. 데이터·관측성·배포: 2026-09-14 로봇청소기 점검 보도에 따르면 개인정보보호위원회는 점검 후속 조치로 접근권한 부여 내역 보관 기간을 200일에서 3년으로, 접속기록 보관 기간을 90일에서 2년 이상으로 늘리도록 했다. | ref-1372 | 아니오 | medium | 2026-09-14 | 가정 / 제약 | — |
| f40 | [사실] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ L. AI·학습 기술의 45. 문서·도면·장면 이해·47. AI·학습·적응과 모델 운영: 개인정보보호위원회는 2023-11 자율주행차·이동형 로봇 개발에 영상데이터 원본 활용을 허용하는 방향을 밝혔고, 2026-05-06 ICT 규제샌드박스 심의위원회는 배달로봇 카메라 원본 영상을 AI 학습에 쓰는 과제에 연구 목적 내 활용·개인 식별 금지·제3자 제공 금지 등을 조건으로 실증특례를 승인했다. | ref-1138, ref-1342 | 아니오 | medium | 2026-05-06 | 실외 / 제약 | 원문 미열람 |
| f41 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ L. AI·학습 기술의 47. AI·학습·적응과 모델 운영: EU AI Act 제12조는 고위험 AI 시스템이 수명 기간 동안 사건 기록(로그)을 자동으로 남길 수 있어야 하고, 위험 상황·실질적 변경 식별, 시판 후 감시, 배포자의 운영 감시에 필요한 사건을 기록하게 한다. | ref-863 | 아니오 | medium | 2024-06-13 | — | 원문 미열람 |
| f42 | [사실] | N. 보안·개인정보의 51. 인증·권한·격리·52. 통신 보호·위협 관리·감사 ↔ M. 안전의 50. 안전 표준·인증·사고 조사: 산업용 로봇 안전 표준 ISO 10218-1/-2 의 2025년 개정판에는 사이버보안 요구가 새로 들어갔다. | ref-1116, ref-1076 | 예 | medium | 2026-09-18 | — | 원문 미열람 |
| f43 | [사실] | N. 보안·개인정보의 51. 인증·권한·격리·53. 개인정보·영상 데이터 ↔ M. 안전의 50. 안전 표준·인증·사고 조사: 서비스 로봇 안전 표준 ISO 13482 개정 초안(ISO/DIS 13482:2024, DIN EN ISO 13482 2024-10 초안)은 사이버보안과 데이터 보호 절을 새로 넣었다. | ref-1425 | 아니오 | medium | 2024-10 | — | 원문 미열람 |
| f44 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ M. 안전의 48. 안전·위험 관리: Quarta 외(IEEE S&P 2017)는 널리 쓰이는 산업용 로봇 제어기의 소프트웨어 취약점과 구조적 결함으로 제어 정확성과 작업자 안전 요구를 무너뜨릴 수 있음을 실험으로 보인 것으로 보인다. | ref-1114 | 아니오 | low | 2017 | 제조 공장 / 예외·성과 | 원문 미열람 |
| f45 | [추정] | N. 보안·개인정보의 51. 인증·권한·격리 ↔ M. 안전의 48. 안전·위험 관리: 산업용·서비스 로봇 안전 표준에 사이버보안과 데이터 보호가 들어오면서, ROP 가 내리는 원격 정지·재개·구역 변경 명령의 권한 통제가 안전 평가 대상이 될 것으로 보인다. | ref-1116, ref-1425 | 아니오 | low | 2026-10-09 | 제약 | 원문 미열람 |
| f46 | [사실] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ O. 검증·도입·수명주기의 57. 자산·소프트웨어 수명주기 관리: ROS 2 위협 모델 초안은 빌드 팜과 서드파티 구성요소를 통한 공급망 위협을 주요 위협으로 들고, Shen 외(2026-09)는 제3자 Docker 컨테이너·보조 도구에 대한 폭넓은 의존을 이용해 악성 훅이 든 패키지를 퍼뜨릴 수 있다고 적는다. | ref-010, ref-1374 | 아니오 | medium | 2026-09-08 | — | — |
| f47 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ O. 검증·도입·수명주기의 55. 현장 조사·설치·시운전: ROS 2 위협 모델 초안이 기본 자격증명을 쓰는 SSH 같은 원격 접속을 권한 상승 경로로 들므로, 설치·시운전 점검 항목에 기본 자격증명 변경과 원격 접속 범위 확인이 들어가야 할 것으로 보인다. | ref-010 | 아니오 | low | 2026-10-09 | 제약 | — |
| f48 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ O. 검증·도입·수명주기의 54. 시험·형식 검증·벤치마크: 2025년 한국인터넷진흥원·한국소비자원의 로봇청소기 6종 점검은 모바일앱 보안·정책 관리·기기 보안 3개 영역 40개 항목으로 이루어졌다고 보도되어, 로봇 보안 시험 항목의 국내 참고 틀이 될 것으로 보인다. | ref-969 | 아니오 | low | 2025-10-31 | 가정 | 원문 미열람 |
| f49 | [사실] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ P. 거버넌스·법규·사회의 58. 다사업자 책임·계약·데이터: EU 데이터법은 2025-09-12 부터 적용되며, 로봇·산업 기계 같은 연결 제품의 사용자가 사용으로 생긴 데이터에 접근해 직접 쓰거나 제3자와 공유할 수 있게 하고, 데이터 보유자(보통 제조사)는 사용자와 계약을 두고 생성 데이터 종류·양·수집 빈도를 알려야 한다. | ref-1376 | 아니오 | medium | 2026-10-09 | — | — |
| f50 | [추정] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ P. 거버넌스·법규·사회의 58. 다사업자 책임·계약·데이터: 여러 제조사 로봇의 데이터를 모아 관제하는 ROP 사업자가 데이터법상 사용자·제3자 가운데 어느 쪽이고 개인정보 처리에서 운영자·수탁자 가운데 어느 쪽인지가 계약으로 정해야 할 쟁점이 될 것으로 보인다(oq-259). | ref-1376, ref-588 | 아니오 | low | 2026-10-09 | — | — |
| f51 | [사실] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스: 개인정보보호위원회 이동형 영상정보처리기기 안내서 공개 보도와 법률사무소 해설은 카메라를 단 자율주행차·배달로봇이 외부에 촬영 사실을 표시하고 명확히 거부하는 사람의 의사를 받아들여야 한다고 전한다. | ref-1136, ref-588 | 아니오 | medium | 2024-10-14 | 실외 / 제약 | 원문 미열람 |
| f52 | [사실] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ P. 거버넌스·법규·사회의 60. 노동·수용성·접근성·Q. 현장 유형별 적용의 61. 물류창고: 프랑스 개인정보 감독기관 CNIL 은 2023-12-27 결정(2024-01-23 공표)으로 Amazon France Logistique 에 3,200만 유로 과징금을 부과했는데, 물류창고 작업자 스캐너 기록으로 10분 넘는 비활동을 실시간 경보하고 1.25초 안의 빠른 스캔을 표시하는 지표와 모든 데이터·지표의 31일 보관을 과도하다고 보았다. | ref-1370, ref-1371 | 예 | medium | 2024-01-23 | 물류창고 / 제약 | — |
| f53 | [추정] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ P. 거버넌스·법규·사회의 60. 노동·수용성·접근성·J. 현장 운영·관제의 39. 운영 성과 측정·개선: 작업자 스캐너 기록의 개인별 비활동·속도 지표가 과도한 감시로 판단된 사례가 있으므로, ROP 가 로봇 작업과 연결해 개별 작업자의 처리량·위치를 기록할 때 39. 운영 성과 측정·개선의 지표를 집계 단위로 두고 보존 기간을 줄이는 설계가 필요할 것으로 보인다(oq-285). | ref-1370, ref-589 | 아니오 | low | 2026-10-09 | 물류창고 / 제약 | — |
| f54 | [사실] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ P. 거버넌스·법규·사회의 60. 노동·수용성·접근성: 근로자참여 및 협력증진에 관한 법률 제20조는 사업장 내 근로자 감시 설비의 설치를 노사협의회 협의 사항으로 둔다. | ref-589 | 아니오 | medium | 2026-10-09 | 제약 | 원문 미열람 |
| f55 | [추정] | N. 보안·개인정보의 52. 통신 보호·위협 관리·감사 ↔ Q. 현장 유형별 적용의 67. 기타 현장: Pudu 관리 API 결함 보도는 사무실에서 승강기 같은 설비를 조작하는 서비스 로봇(FlashBot)이 사무실 시스템을 망가뜨리거나 지식재산을 빼내는 데 쓰일 수 있다고 평가했는데, 이는 연구자·매체의 평가이며 확인된 사고는 아니다. | ref-1369, ref-1368 | 아니오 | low | 2025-09-05 | 기타 / 예외·성과 | — |
| f56 | [사실] | N. 보안·개인정보의 53. 개인정보·영상 데이터 ↔ Q. 현장 유형별 적용의 63. 병원·의료: 진료실을 흉내 낸 모의 시나리오에서 의사·환자를 알아보도록 학습한 서비스 로봇은 대상이 아닌 사람의 얼굴을 안정적으로 가렸지만 자세 변화·가림·조명 변화가 인식 신뢰도를 낮췄다. | ref-1146 | 아니오 | medium | 2026-03-16 | 병원 / 예외·성과 | 원문 미열람 |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-009 | ROS 2 Design | ROS 2 DDS-Security Integration | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://design.ros2.org/articles/ros2_dds_security.html | 아니오 |
| ref-010 | ROS 2 Design | ROS 2 Robotic Systems Threat Model | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://design.ros2.org/articles/ros2_threat_model.html | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-10-09 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-405 | Open Robotics | Security - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://osrf.github.io/ros2multirobotbook/security.html | 아니오 |
| ref-579 | Open Robotics (ROS 2 Design) | ROS 2 Access Control Policies | 2019-08 | 오픈소스 문서 | medium | 2026-10-09 | https://design.ros2.org/articles/ros2_access_control_policies.html | 아니오 |
| ref-494 | Francos, R. M., Garces, D., Akgün, O. E., Bastian, N. D., & Gil, S.(Harvard·JHU) | Trust-Aware Sequential Decision Making and Rollout Planning for Resilient Multi-Robot Systems | 2026-08 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2608.25690 | 예 |
| ref-588 | 김·장 법률사무소 | '이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서' 관련 인사이트 | 미확인 | 업계 보고서 | medium | 2026-10-09 | https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=30477 | 예 |
| ref-589 | 법제처 국가법령정보센터 | 근로자참여 및 협력증진에 관한 법률 | 미확인 | 정부·연구기관 | medium | 2026-10-09 | https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=105636 | 예 |
| ref-857 | Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J. | Jailbreaking LLM-Controlled Robots | 2024-11-09 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2410.13691 | 예 |
| ref-700 | Ravichandran, Z., Robey, A., Kumar, V., Pappas, G. J., & Hassani, H.(IEEE RA-L 2026 채택 표기) | Safety Guardrails for LLM-Enabled Robots | 2025-03 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2503.07885 | 예 |
| ref-854 | Open Source Robotics Alliance (OSRA) Interop SIG | Open Robotics Discourse, Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP) | 2026-06-25 | 오픈소스 문서 | medium | 2026-10-09 | https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687 | 예 |
| ref-863 | European Commission — AI Act Service Desk | Article 12: Record-keeping (Regulation (EU) 2024/1689, Artificial Intelligence Act) | 2024-06-13 | 정부·연구기관 | medium | 2026-10-09 | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-12 | 예 |
| ref-969 | 바이라인네트워크 | '로봇청소기' 다수 제품 보안 취약…대응방안은? | 2025-10-31 | 기사 | low | 2026-10-09 | https://byline.network/2025/10/31-283/ | 예 |
| ref-1076 | Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv) | Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066 | 2026-02-19 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2602.17822 | 예 |
| ref-1105 | IEC (SyC Smart Energy) | IEC 62443 | 미확인 | 표준 | medium | 2026-10-09 | https://syc-se.iec.ch/deliveries/cybersecurity-guidelines/security-standards-and-best-practices/iec-62443/ | 예 |
| ref-1106 | OWASP GenAI Security Project | LLM01:2025 Prompt Injection | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://genai.owasp.org/llmrisk/llm01-prompt-injection/ | 예 |
| ref-1107 | CISA (미국 사이버보안·기반시설보안청) | Aethon TUG Home Base Server (ICSA-22-102-05) | 2022-04-12 | 정부·연구기관 | medium | 2026-10-09 | https://www.cisa.gov/news-events/ics-advisories/icsa-22-102-05 | 예 |
| ref-1109 | IES (Integrated Equipment Services) | Machinery Regulation Guide | 2026-08-27 | 업계 보고서 | medium | 2026-10-09 | https://www.ies.co.uk/reference-library/machinery-regulation-guide | 예 |
| ref-1110 | Fernández-Becerra, L., González-Santamarta, M. Á., Guerrero-Higueras, Á. M., Rodríguez-Lera, F. J., & Matellán Olivera, V. (arXiv) | Enhancing Trust in Autonomous Agents: An Architecture for Accountability and Explainability through Blockchain and Large Language Models | 2024-03 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2403.09567 | 예 |
| ref-1111 | 엠에스투데이 | 선박·위성·로봇까지 해킹 표적…정부, '피지컬 AI' 산업 보안 기준 제시 | 2026-03-06 | 기사 | low | 2026-10-09 | https://www.mstoday.co.kr/news/articleView.html?idxno=100755 | 예 |
| ref-1112 | Nagaraja, N., Bagari, A., & Bahsi, H. (arXiv) | When Prompts Control Robots: Prompt Injection Attacks in Multi-Agent Robotic Systems | 2026-08 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2608.00747 | 예 |
| ref-1113 | Zhang, W., Kong, X., Dewitt, C., Braunl, T., & Hong, J. B. (arXiv) | A Study on Prompt Injection Attack Against LLM-Integrated Mobile Robotic Systems | 2024-08 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2408.03515 | 예 |
| ref-1114 | Quarta, D., Pogliani, M., Polino, M., Maggi, F., Zanchettin, A. M., & Zanero, S. (IEEE S&P 2017) | An Experimental Security Analysis of an Industrial Robot Controller | 2017 | 논문 | medium | 2026-10-09 | https://files01.core.ac.uk/download/pdf/84891817.pdf | 예 |
| ref-1116 | IBF Solutions | New standards for industrial robots EN ISO 10218-1 and -2 | 2026-09-18 | 업계 보고서 | medium | 2026-10-09 | https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2 | 예 |
| ref-1136 | 정보통신신문 | "자율주행차·로봇 카메라 촬영 시 외부에 표시해야" | 2024-10-14 | 기사 | low | 2026-10-09 | https://www.koit.co.kr/news/articleView.html?idxno=125844 | 예 |
| ref-1138 | 개인정보보호위원회 (대한민국 정책브리핑) | 자율주행차·이동형 로봇 개발에 '영상데이터' 원본 활용 허용 | 2023-11-15 | 정부·연구기관 | medium | 2026-10-09 | https://www.korea.kr/news/policyNewsView.do?newsId=148922669 | 예 |
| ref-1141 | 아시아경제 | "로봇청소기 개인정보 관리 대체로 안전…미흡 사례 ... (제목 일부만 확인) | 2026-09-14 | 기사 | low | 2026-10-09 | https://view.asiae.co.kr/article/2026091410054053414 | 예 |
| ref-1145 | Xu, Y., & Ayday, E. (arXiv) | Seeing Less Is Not Seeing Safely: Privacy Leakage from Task-Scoped Robot Perception Exports | 2026-09-02 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2609.03055 | 예 |
| ref-1146 | Sarfraz, B. M., Saplacan Lindblom, D., Baselizadeh, A., & Torresen, J. (HRI Companion '26) | The Privacy-Preserving Capabilities of a Service Robot in a Scenario-Based Healthcare Setting | 2026-03-16 | 논문 | medium | 2026-10-09 | https://doi.org/10.1145/3776734.3794481 | 예 |
| ref-1173 | ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan | REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction | 2022-01-11 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst | 예 |
| ref-1299 | ST Engineering Aethon (Newswire 게재 보도자료) | ST Engineering Aethon Launches Zena RX, Redefining Secure Delivery of Medications, Specimens and Sensitive Goods in Hospitals | 2024-04-29 | 벤더 문서 | low | 2026-10-09 | https://www.newswire.com/news/st-engineering-aethon-launches-zena-rx-redefining-secure-delivery-of-22310264 | 예 |
| ref-1301 | 경향신문 (곽희양) | 내년 2월 자율주행 로봇이 아파트 내에서 배달 음식 나른다 | 2020-07-03 | 기사 | low | 2026-10-09 | https://www.khan.co.kr/article/202007031130001 | 예 |
| ref-1304 | Carr, C., Wang, S., Wang, P., & Han, L. (arXiv) | Attacking Digital Twins of Robotic Systems to Compromise Security and Safety | 2022-11-17 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2211.09507 | 예 |
| ref-1342 | 메트로신문 | AI·커머스·플랫폼 분야 규제 특례 확대…사업화 지원 | 2026-05-06 | 기사 | low | 2026-10-09 | https://www.metroseoul.co.kr/article/20260506500296 | 예 |
| ref-1425 | DIN Media | DIN EN ISO 13482 - 2024-10 (Draft standard) Robotik - Sicherheitsanforderungen für Serviceroboter (ISO/DIS 13482:2024) | 2024-10 | 표준 | medium | 2026-10-09 | https://www.dinmedia.de/de/norm-entwurf/din-en-iso-13482/384079303 | 예 |
| ref-1367 | European Commission (Shaping Europe's digital future) | CRA reporting | 미확인 | 정부·연구기관 | high | 2026-10-09 | https://digital-strategy.ec.europa.eu/en/policies/cra-reporting | 아니오 |
| ref-1368 | The Register | Researcher who found McDonald's free-food hack turns her attention to Chinese restaurant robots | 2025-08-29 | 기사 | medium | 2026-10-09 | https://www.theregister.com/2025/08/29/pudu_robots_hackable/ | 아니오 |
| ref-1369 | Hackmag | Researcher finds a way to hack Chinese Pudu service robots | 2025-09-05 | 기사 | low | 2026-10-09 | https://hackmag.com/news/pudu-bugs | 아니오 |
| ref-1370 | Silicon UK | France Fines Amazon 32m Euros Over 'Excessive' Worker Surveillance | 2024-01-23 | 기사 | medium | 2026-10-09 | https://www.silicon.co.uk/e-marketing/ecommerce/cnil-france-amazon-fine-546858 | 아니오 |
| ref-1371 | CNIL (Commission nationale de l'informatique et des libertés) | Employee monitoring: CNIL fined AMAZON FRANCE LOGISTIQUE €32 million | 2024-01-23 | 정부·연구기관 | medium | 2026-10-09 | https://cnil.fr/en/employee-monitoring-cnil-fined-amazon-france-logistique-eu32-million | 예 |
| ref-1372 | 바이라인네트워크 (곽중희) | 개인정보위 "로봇청소기 5개 브랜드, 특별한 침해 위험 없어" | 2026-09-14 | 기사 | medium | 2026-10-09 | https://byline.network/2026/09/14-623/ | 아니오 |
| ref-1373 | 바이라인네트워크 | 과기정통부, 선박·우주·로봇 보안 매뉴얼 공개 | 2026-03-06 | 기사 | medium | 2026-10-09 | https://byline.network/2026/03/6-340/ | 아니오 |
| ref-1374 | Shen, L., Geng, S., Zheng, Y., & Lu, C. X. (arXiv) | Seeing is Not Believing: Breaking the Physical-to-Digital Trust Boundary in Robotics | 2026-09-08 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2609.08280 | 아니오 |
| ref-1375 | KUKA (Robotics Tomorrow 게재 보도자료) | KUKA is First to Achieve Security Level 2 Certification for Robotics Industry | 2026-09-02 | 벤더 문서 | low | 2026-10-09 | https://www.roboticstomorrow.com/news/2026/09/02/kuka-is-first-to-achieve-security-level-2-certification-for-robotics-industry/27035/ | 아니오 |
| ref-1376 | European Commission (Shaping Europe's digital future) | Data Act explained | 미확인 | 정부·연구기관 | high | 2026-10-09 | https://digital-strategy.ec.europa.eu/en/policies/data-act-explained | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/security-and-privacy/index.md | 5. 다른 대분류와의 연결 | category_link: '다른 대분류와의 연결' 절만 patches 로 채운다. 대분류별 finding — A. 기획·사업: f1(1, 한국 보안모델), f2(3, 벤더 주장)·f3(3), f4(2) / B. 로봇 온톨로지: f5·f6(4·7, 인증서 교체, oq-113), f7(4, 개인정보 속성), f8(6, 명령 단위 권한) / C. 채팅 기반 구성·운영: f9(13), f10(12), f11(13·44), f12(12, 최소 권한), f13(12, 승인 감사 기록) — 분류 원문 C 주석 '사람이 확인·승인한 계획만 실행'과 함께 / D. 공간·지도 모델: f14(16, 가정 지도 저장 위치)·f15(15·16) — D 페이지가 '근거 없음'으로 둔 N 연결을 채움 / E. 사물·사람·실시간 상태: f16·f17(18, 텔레메트리 위조, oq-082), f18(17, 벤더 주장), f19(19) / F. 연동: f20·f21·f22(20, oq-100), f23·f24(21, oq-246), f25(22, oq-056) / G. 계획·최적화: f26·f27(25·27) / H. 실행·협업·예외 복구: f28(29), f29(32) / I. 설계·시뮬레이션: f30(34), f31(34·36) — 가정한 미래 실험 쪽이며 18. 실시간 세계 상태·데이터 일관성(f16·f17)과 구분 / J. 현장 운영·관제: f32·f33(37, oq-248·oq-249), f17(38), f34·f35·f36(40, oq-291) / K. 플랫폼 아키텍처·인프라: f37(41), f38(42), f39(43, oq-214) / L. AI·학습 기술: f40(45·47, 원본 영상), f41(47), f11(44) / M. 안전: f42·f43(50, oq-102·oq-254), f44·f45(48) / O. 검증·도입·수명주기: f48(54), f47(55), f46·f6·f35(57) / P. 거버넌스·법규·사회: f49·f50(58, oq-259), f35·f51(59), f52·f53·f54(60, oq-285·oq-099) / Q. 현장 유형별 적용: f52(61 물류창고, 로봇이 아닌 스캐너 사례임을 밝힘), f44(62 제조 공장), f21·f56(63 병원·의료), f20·f29·f34(64 상업 시설), f14·f39·f48(65 가정·공동주택), f40·f51(66 실외), f55(67 기타 현장). 벤더 주장 f2·f18 은 [추정]과 '벤더 주장' 병기. 로봇 제어기·펌웨어 보안, 승강기 제어, 카메라 기기 쪽 처리는 '연계 대상'으로 짧게. 아직 다루지 않은 연결: 23. 업무 시스템 연동, 24. 작업·워크플로 모델링, 26. 작업 순서·스케줄링, 28. 공용 자원·충전·에너지 최적화, 30. 로봇 간 협업·물리적 인계, 33. 시나리오 모델·편집, 35. 처리능력·규모·배치 설계, 46. 예측·학습 기반 최적화, 49. 사람 근접 안전, 56. 운영 이관·확대·교육, 5. 로봇 능력·작업 표현, 8~11. 채팅 영역. 다음 실행 후보: 51. 인증·권한·격리(이전 분류 기준) 10절에 f5·f20·f22·f37 반영, 52. 통신 보호·위협 관리·감사 7절에 f35(사이버복원력법 보고 의무) 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 적극 악용 취약점 | Actively Exploited Vulnerability (EU Cyber Resilience Act) | 악의적 악용의 믿을 만한 증거가 있는 취약점으로, EU 사이버복원력법이 2026-09-11 부터 제조자에게 24시간 조기 경보·72시간 통지·최종 보고를 요구하는 대상이다. |
| 연결 제품 | Connected Product (EU Data Act) | 사용·성능·환경 데이터를 만들고 전송할 수 있는 제품으로, EU 데이터법이 사용자에게 그 데이터의 접근·공유 권리를 주는 대상이며 집행위원회 해설은 로봇과 산업 기계를 예로 든다. |
| 원격 증명 | Remote Attestation | 원격 검증자가 기기가 보고하는 상태·측정값을 근거로 그 기기가 정상적으로 동작하고 있음을 확인하는 절차로, 보고 데이터가 발행 전에 위조되면 무력화될 수 있다. |

## 열린 질문

새로 생긴 질문:

- ROP 가 제조사 플릿 관리 서버·관리 API 를 연동하기 전에 인증 뒤 권한 검사 같은 인가 결함을 확인하는 최소 보안 시험 항목을 정한 공개 기준이나 사례가 있는가? | 관련 영역: 51. 인증·권한·격리, 20. 로봇·제조사 관제 연동, 54. 시험·형식 검증·벤치마크 | 근거: f22 | 종류: 일반
- 로봇이 발행 전 단계에서 위조한 텔레메트리를 설비 센서·다른 로봇 관측과 교차 확인해 플릿 수준에서 탐지하는 방법의 효과를 측정한 연구가 있는가? | 관련 영역: 52. 통신 보호·위협 관리·감사, 18. 실시간 세계 상태·데이터 일관성, 38. 모니터링·이상 탐지·원인 분석 | 근거: f17 | 종류: 일반
- EU 데이터법에서 여러 제조사 로봇의 데이터를 모아 관제하는 오케스트레이션 플랫폼 사업자는 사용자·제3자·데이터 보유자 가운데 어느 지위이며, 제조사에 로봇 데이터 제공을 요구할 수 있는가? | 관련 영역: 58. 다사업자 책임·계약·데이터, 53. 개인정보·영상 데이터 | 근거: f50 | 종류: 일반
- 작업자 스캐너 기록의 개인별 비활동·속도 지표를 과도한 감시로 본 CNIL 판단이 로봇 작업 기록에서 만든 작업자 지표에 적용된 감독기관 결정이나 국내 해석이 있는가? | 관련 영역: 53. 개인정보·영상 데이터, 60. 노동·수용성·접근성, 39. 운영 성과 측정·개선 | 근거: f53 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 45 · 교차 확인: 2
- 예산 사용량: 검색 13회 · 신규 출처 10건
- 미확인 항목:
    - f20·f29·f34·f55 Pudu 사례는 연구자 블로그 공개를 옮긴 기사 두 건 기준이며 연구자 원문과 제조사 공식 공지는 열지 못함(교차 확인 아님)
    - ref-1371 CNIL 공지는 페이지가 '더 이상 제공되지 않음'으로 열려 검색 결과 요약 범위로만 사용
    - f39 접근권한 내역·접속기록 보관 기간 연장의 적용 대상과 근거 조항은 기사에 없어 미확인(oq-214)
    - f2 KUKA IEC 62443-4-2 SL2 인증은 벤더 주장, 인증 기관·인증서 미확인
    - MiR Fleet Enterprise 의 IEC 62443-4-2 정렬 주장은 PDF 본문을 추출하지 못해 쓰지 않음
    - ISO 10218-1:2025 사이버보안 조항 번호는 여전히 미확인(oq-102)
    - KISA 로봇 보안모델 고도화판·해설서의 요구 항목은 원문을 열지 못해 미확인(oq-250)
    - EU 사이버복원력법 규정 원문(제14조)은 열지 않고 집행위원회 안내 페이지만 확인
    - 재사용 출처 35건은 이번 실행에서 다시 열지 않음
- 범위 경계 위반 의심:
    - f2·f3·f44: 로봇 제어기 보안 인증·제어기 취약점은 원문 19장 '로봇 자체 지능·제어' 경계의 제조사 몫이라 ROP 는 조달 요구·연결 대상 위협 근거로만 서술
    - f21·f25: 병원 플릿 서버의 방화벽·VPN, 승강기 조작은 시설·설비 제어 경계의 연계 대상이며 ROP 는 연결 계정 권한과 설비 명령 권한 분리로만 서술
    - f14·f18·f56: 로봇청소기 앱 인증·기기 저장, 잠금 칸 생체 인증, 기기 쪽 얼굴 가림은 제조사 기능이라 연계 대상이며 ROP 는 결과·상태 기록 쪽만 서술
    - f35·f49·f51·f52·f54: 법령 해석과 적용 판단은 운영 사업자·법무 몫이며 ROP 는 기록·통보·데이터 흐름 규칙 제공 범위로만 연결
    - f52: CNIL 사례는 로봇이 아닌 작업자 스캐너 기록이라 claim 에 그 사실을 밝힘
- 한계: web_fetch_available: true · fetch_mode full. 대분류 연결(category_link) 실행이다. 근거는 먼저 게시된 51·52·53 페이지와 A·B·D·E·F·G 대분류 페이지, 이전 브리프(2026-10-09-08, 2026-10-09-09)의 검증된 주장에서 찾고 재사용 출처 id 를 썼다(재사용 35건 가운데 이번에 다시 연 것은 ref-031(github_raw) 1건이고 나머지 34건은 fetched false·source_unopened true). 신규 출처는 10건(ref-1367~ref-1376, 예약 구간 안)이며 ref-1371(CNIL 공지)을 뺀 9건은 원문을 열었다. 검색 13회/30, 신규 출처 10건/15. 교차 확인 2건(f42 ISO 10218 사이버보안, f52 CNIL Amazon 과징금). 벤더 주장 2건(f2·f18). 같은 정부 발표를 옮긴 기사 쌍(f1, f51)과 같은 연구자 공개를 옮긴 기사 쌍(f20 등)은 독립 출처로 보지 않아 교차 확인으로 세지 않았다. 한국 자료: 신규 ref-1372·ref-1373, 재사용 ref-589·ref-588·ref-969·ref-1111·ref-1136·ref-1138·ref-1141·ref-1301·ref-1342. 현장 유형: 물류창고(f52·f53, 로봇이 아닌 스캐너 사례)·제조 공장(f44)·병원(f18·f21·f56)·상업 시설(f20·f29·f34)·가정(f14·f39·f48)·실외(f40·f51)·기타(f55) 각 1건 이상. 18. 실시간 세계 상태·데이터 일관성(현재 상태, f16·f17)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래, f30·f31)을 구분했다. 분류 원문 교차 규칙에 해당하는 L. AI·학습 기술 연결(f11·f40·f41)은 적용 대상 영역과 함께 제안했다. 열린 질문 oq-056·oq-082·oq-099·oq-100·oq-102·oq-113·oq-214·oq-246·oq-248·oq-249·oq-250·oq-259·oq-285·oq-291 에는 부분 근거만 더했고 해결 제안은 없다. 대분류 페이지 절 번호는 이전 대분류 연결 실행과 같이 제목 순서(핵심 질문·개요·세부 연구영역·핵심 포인트·다른 대분류와의 연결)에 따라 '5'로 매겼다 [가정]. 아직 근거를 찾지 못한 연결은 page_proposals 의 rationale 에 적었다. 정정 요청 없음. 우선 지정 질문 없음. 입력 누락 없음.
```

### runs/2026-09-30-20/research.md

```markdown
# 리서치 브리프 2026-09-30-20

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-20 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 19. 사람·보행자 모델 |
| 대분류 | E. 사물·사람·실시간 상태 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 움직임 지도(Maps of Dynamics)·사회적 힘 모델·사람 궤적 예측·사회적 내비게이션·사람 표현(ROS4HRI) 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 물류창고·병원·상업 시설·실외·기타의 사람 흐름 반영 사례와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 실시간 사람 검출·추적, 장기 시공간 흐름 지도, 단기 궤적 예측, 보행자 행동 모델(시뮬레이션), 운영 규칙 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — REP-155(ROS4HRI), HuNavSim, Open-RMF CrowdSim(Menge), 공개 데이터셋(THÖR·ATC) 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 oq-256 반영 필요
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 현장 사람의 위치와 흐름을 어떻게 알고 계획과 안전에 반영할 것인가? [분류원문]
2. 사람의 위치·목적지·멈춤·교차를 표현하는 모델(움직임 지도, 궤적 예측, 사회적 힘 모델)에는 무엇이 있고 각각 무엇을 입력으로 받아 어디에 쓰는가? (섹션 4·6·8 겨냥)
3. 시간대·구역별 사람 흐름과 혼잡을 장기 관측으로 추정하는 방법과 그 효과를 로봇 경로·작업에 반영해 평가한 연구는 무엇인가? (섹션 6·8 겨냥)
4. 사람 정보를 로봇·시스템 사이에서 주고받는 공통 표현(ROS 규약 등)과 보행자 시뮬레이터·공개 데이터셋에는 무엇이 있는가? (섹션 7 겨냥)
5. 물류창고·병원·상업 시설·실외 현장에서 사람 흐름·혼잡을 로봇 운영에 반영한 사례는 무엇이며, 한국 사례(병원 로봇 운영, 공공 인파 밀집 관리)는 어떤가? (섹션 3·5 겨냥, 한국 자료 우선)
6. oq-256 실제 운영 기록을 재생해 재현한 상황에서 조건을 바꿀 때 기록된 사람·다른 에이전트가 반응하지 않는 문제를 다른 분야(자율주행 시뮬레이션)는 어떻게 다루는가? (섹션 6·11 겨냥)
7. 사람·보행자 모델에서 ROP가 직접 맡을 것과 로봇 제조사(온보드 검출·국소 회피)·설비·공공 시스템에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Kucner 외(IJRR 42(11), 2023)의 서베이에 따르면 움직임 지도(Maps of Dynamics, MoD)는 환경의 전형적인 움직임 패턴을 저장하는 지도로, 궤적이나 짧고 끊긴 움직임 관측으로 만들 수 있으며 전역 경로 계획·위치 추정 개선·사람 움직임 예측에 쓰여 로봇이 감지 범위 밖과 미래의 움직임을 예상하게 한다. | ref-1204 | 아니오 | medium | 2023 | 제약 | 원문 미열람 |
| f2 | [사실] | Rudenko 외의 사람 움직임 궤적 예측 서베이(IJRR 2020)는 보행자 중심의 지상 2차원 궤적 예측 방법을 여러 연구 공동체에 걸쳐 정리하고, 움직임 모델링 방식과 사용하는 맥락 정보 수준이라는 두 축의 분류 체계를 제안하며 데이터셋과 성능 지표를 함께 검토한다. | ref-1205 | 아니오 | medium | 2019-12 | — | — |
| f3 | [사실] | Helbing·Molnár(Physical Review E 51, 1995)의 사회적 힘 모델은 보행자 움직임을 원하는 속도로 가속하려는 항, 다른 보행자·경계와 거리를 두려는 반발 항, 끌림 항의 합으로 보고, 상호작용하는 군중 시뮬레이션에서 관측되는 집단 현상의 자기조직화를 재현한다. | ref-1207 | 아니오 | medium | 1995-05 | — | 원문 미열람 |
| f4 | [사실] | ROS REP-155(ROS4HRI, 2022-01-11 작성, 원문 상태 Draft)는 사람을 영속적인 person ID 와 추적 중에만 유효한 face·body·voice ID 의 조합으로 표현하고, /humans/persons/tracked 같은 토픽과 person_<ID> 좌표 프레임에 위치 신뢰도(1.0 지금 보임, 1 미만 이전에 보임, 0 추적된 적 없음)를 두며 아직 식별되지 않은 익명 사람도 표시한다. | ref-1206 | 아니오 | medium | 2022-01-11 | 작업 대상 | — |
| f5 | [사실] | REP-155 에서 영속 person ID 는 얼굴 인식·음성 인식·옷 색 같은 신체 특징 기반 식별 노드가 부여해 세션을 넘어 같은 사람을 다시 알아보게 하므로, 사람 표현이 개인 식별 정보와 연결될 수 있다. | ref-1206 | 아니오 | medium | 2022-01-11 | 작업 대상 | — |
| f6 | [사실] | THÖR 데이터셋(Rudenko 외, RA-L 2020)은 실내 환경에서 사람 움직임 궤적과 시선 데이터를 모으고 위치·머리 방향·시선·사회적 그룹·장애물 지도·목표 좌표의 정답을 제공하며, 3차원 라이다 데이터와 공간을 주행하는 이동로봇을 포함한다. | ref-1208 | 아니오 | medium | 2019-12 | — | — |
| f7 | [사실] | 상업 시설 사례: 일본 오사카 ATC 쇼핑센터의 약 900㎡ 구역에 천장 3차원 거리 센서 49대를 두어 2012-10-24~2013-11-29 가운데 92일(매주 수·일요일 9:40~20:20) 보행자를 추적한 ATC 데이터셋은 시각·사람 id·x·y·높이·속도·이동 방향·몸 방향을 제공하며 연구 목적으로만 쓸 수 있다. | ref-1209 | 아니오 | medium | 2026-09-30 | 상업 시설 / 작업 대상 | — |
| f8 | [사실] | 상업 시설 사례: Kidokoro 외(HRI 2013)는 쇼핑몰에서 사람을 모으는 로봇이 혼잡을 일으켜 지나가는 보행자의 보행 쾌적성을 해치는 문제에 대해, 보행자 행동 모델로 가상의 주행 상황을 시뮬레이션해 혼잡을 예상하고 미리 피하도록 계획하는 방법을 실제 쇼핑몰에서 시험해 영향을 줄였다고 보고했다. | ref-1218 | 아니오 | medium | 2013-03 | 상업 시설 / 제약 | 원문 미열람 |
| f9 | [사실] | Vintr 외(Frontiers in Robotics and AI, 2022)는 대학 건물 복도(약 500㎡)에서 3차원 라이다로 한 달간(2019-03) 모은 600만 건 이상의 사람 검출로 FreMEn·HyperTime·GMM 등 20여 개 시공간 보행자 흐름 지도를 학습시키고, 경로 계획 시뮬레이션에서 예상 조우(Expected Encounters)와 예상 경로 길이로 비교해 공간과 시간을 따로 모델링한 방법(HyT×GMM 등)이 더 나았다고 보고했다. | ref-1211 | 아니오 | medium | 2022-07-04 | 기타 / 제약 | — |
| f10 | [사실] | 같은 연구의 현장 실험(프랑스 UTBM 대학 홀, 2019-12-12~13, Toyota HSR, 40분 세션 네 번)에서 사람 흐름의 시간대 패턴을 따르는 예측형 주행은 두 세션 모두 불편을 드러낸 사람이 0명이었고 반응형 주행은 2명·1명이었다. | ref-1211 | 아니오 | low | 2022-07-04 | 기타 / 예외·성과 | — |
| f11 | [사실] | Francis 외(2023, 저자 52명)는 사회적 내비게이션 로봇을 안전·쾌적·가독성·예의·사회적 역량·상대 이해·능동성·맥락 대응의 원칙을 지키는 로봇으로 정의하고, 지표·시나리오·데이터셋·시뮬레이터 사용 지침과 서로 다른 시뮬레이터·로봇·데이터셋 결과를 비교하기 위한 지표 프레임워크를 제안했다. | ref-1079 | 아니오 | medium | 2023-09-19 | 예외·성과 | — |
| f12 | [사실] | HuNavSim(Pérez-Higueras 외, RA-L 2023)은 ROS 2 기반 오픈소스 도구로 Gazebo 같은 로봇 시뮬레이터와 함께 이동로봇 주변 사람 에이전트의 다양한 보행 행동을 시뮬레이션하고, 사회적 내비게이션 벤치마킹용 지표 묶음을 제공한다. | ref-1213 | 아니오 | medium | 2023-09-13 | — | — |
| f13 | [사실] | Open-RMF 시뮬레이션에서 군중 시뮬레이션(CrowdSim)은 선택 기능으로 rmf_traffic_editor 에서 켤 수 있으며 Menge 를 핵심 엔진으로 써 시뮬레이션 세계의 에이전트를 제어한다. | ref-406 | 아니오 | medium | 2026-09-30 | — | — |
| f14 | [사실] | 물류창고 사례: EU ILIAD 프로젝트(2017~2021)는 스웨덴 외레브로의 Orkla Foods 창고 두 곳(상온·냉장)에서 자율 지게차 플릿을 시연했으며, 2D·3D 레이저, 컬러·깊이 카메라, 안전조끼 검출 전용 카메라를 결합해 작업자를 검출·추적하고, 현장별 사람 이동 패턴을 움직임 지도로 학습해 사람 흐름에 맞춘 경로 계획에 썼다. | ref-1215 | 아니오 | medium | 2021-06 | 물류창고 / 제약 | — |
| f15 | [사실] | 병원 사례(한국): 조선비즈(2024-07) 보도에 따르면 한림대학교성심병원은 붐비지 않는 밤에 인식한 경로가 낮의 혼잡에서는 원활하지 않을 수 있어 로봇 통행 경로와 작업 정지 지점에 전용 스티커를 붙여 표시했고, 로봇은 사람이나 휠체어와 마주치면 무조건 기다리도록 설계되었다. | ref-1217 | 아니오 | low | 2024-07-12 | 병원 / 제약 | — |
| f16 | [사실] | 연계 대상: 행정안전부의 인파관리지원시스템은 2023-12-29부터 전국 중점관리지역 100곳에서 이동통신 3사의 기지국 접속정보로 인파 밀집도·혼잡도를 추정하고 협소 도로 비율 같은 공간 특성을 더해 위험도를 산출해 지도에 색으로 표시하며, 위험 수준에 따라 지자체 공무원에게 경보를 보낸다. | ref-1210 | 아니오 | medium | 2023-12-27 | 실외 / 시작 조건 | — |
| f17 | [사실] | Waymax(Gulino 외, 2023) 자율주행 시뮬레이터는 기록된 궤적을 그대로 따르는 로그 재생 에이전트와, 규칙 기반(지능형 운전자 모델, IDM)·학습 기반 행동 모델로 다른 참가자에 반응하는 모의 에이전트를 함께 제공하며, 강화학습 에이전트가 모의 에이전트의 행동에 과적합할 수 있음을 보였다. | ref-1128 | 아니오 | medium | 2023-10-12 | 실외 / 예외·성과 | — |
| f18 | [추정] | oq-256 에 대해 자율주행 시뮬레이션은 기록 재생 에이전트를 반응형 모델로 바꾸는 방식으로 비반응 문제를 다루지만 모델 편향이 생기므로, 로봇 플릿 재현에서도 기록된 사람을 사회적 힘 모델·HuNavSim·Menge 같은 보행자 모델로 기록 위치에서 이어받아 움직이게 하는 방식이 가능해 보이나, 로봇 플릿 재현에 적용한 공개 사례는 이번에 찾지 못했다. | ref-1128, ref-1207, ref-1213, ref-406 | 아니오 | low | 2026-09-30 | 예외·성과 | — |
| f19 | [추정] | 확인한 자료를 종합하면 핵심 질문(현장 사람의 위치와 흐름을 어떻게 알고 계획과 안전에 반영할 것인가)에 대해, 로봇 탑재·천장 센서로 사람을 실시간 검출·추적하고, 장기 관측으로 시간대별 흐름 지도(움직임 지도)를 학습하며, 궤적 예측·보행자 행동 모델로 가까운 미래와 가상 상황을 추정해 경로 비용·속도 제약·혼잡 회피·운영 규칙(전용 통로, 무조건 대기)으로 반영하는 방식이 쓰이지만, 효과 근거는 소규모 실험·단일 사례 중심인 것으로 보인다. | ref-1204, ref-1205, ref-1209, ref-1211, ref-1215, ref-1217, ref-1218 | 아니오 | low | 2026-09-30 | — | — |
| f20 | [추정] | 확인한 자료를 종합하면 19. 사람·보행자 모델에서 ROP가 직접 맡을 범위는 여러 로봇과 설비 센서가 보고한 사람 위치를 공통 좌표·시각·신뢰도로 모으고, 구역·시간대별로 집계·익명화한 사람 흐름·혼잡 모델을 유지해 경로·구역 비용, 작업 시간 추정, 배정·스케줄링에 넘기는 일로 보인다. | ref-1204, ref-1206, ref-1211, ref-1215 | 아니오 | low | 2026-09-30 | 제약 | — |
| f21 | [추정] | 연계 대상: 분류 원문 19장 기준으로 로봇의 온보드 사람 검출·추적, 국소 회피와 정지·양보 동작, 사람 근접 안전 기능은 로봇 자체 지능·제어(제조사)에, CCTV·기지국 기반 인파 관리는 시설·공공 시스템에 속하므로, ROP는 그 결과를 받아 계획 제약으로 쓰고 로봇에 대기·우회 같은 운영 규칙을 요청하는 쪽을 맡는 것으로 보인다. | ref-1215, ref-1217, ref-1210 | 아니오 | low | 2026-09-30 | 수행 자원 | — |
| f22 | [추정] | 이 영역은 사람 위치의 현재 상태와 신선도의 18. 실시간 세계 상태·데이터 일관성(f4), 가정한 미래를 실험하는 보행자 시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈(f3·f12·f13), 기록 재현의 36. 가상 시운전·실제 상황 재현(f17·f18, oq-256), 흐름 지도를 얹을 15. 지도·공간·위치 모델과 구역 의미의 16. 장소 의미·지도 관리(f1·f15), 작업 시간 추정의 26. 작업 순서·스케줄링(f20), 혼잡을 반영한 경로의 27. 다중 로봇 경로·교통 관리 — MAPF(f9·f14), 사람 근접 안전의 49. 사람 근접 안전(f21), 사람 식별 정보의 53. 개인정보·영상 데이터(f5), 학습 기반 예측의 46. 예측·학습 기반 최적화(f2·f9), 평가 지표의 54. 시험·형식 검증·벤치마크(f11), 현장 협업의 31. 사람–로봇 협업(f15), 적용 현장인 61. 물류창고(f14)·63. 병원·의료(f15)·64. 상업 시설(f7·f8)·66. 실외(f16·f17)와 이어진다. | ref-1206, ref-1207, ref-1213, ref-406, ref-1128, ref-1204, ref-1217, ref-1211, ref-1215, ref-1205, ref-1079, ref-1209, ref-1218, ref-1210 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1204 | Kucner, T. P., Magnusson, M., Mghames, S., Palmieri, L., Verdoja, F., Swaminathan, C. S., Krajník, T., Schaffernicht, E., Bellotto, N., Hanheide, M., & Lilienthal, A. J. (The International Journal of Robotics Research 42(11)) | Survey of maps of dynamics for mobile robots | 2023 | 논문 | medium | 2026-09-30 | https://journals.sagepub.com/doi/10.1177/02783649231190428 | 예 |
| ref-1205 | Rudenko, A., Palmieri, L., Herman, M., Kitani, K. M., Gavrila, D. M., & Arras, K. O. (arXiv; IJRR 39(8), 2020) | Human Motion Trajectory Prediction: A Survey | 2019-12-17 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/1905.06113 | 아니오 |
| ref-1206 | ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan | REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction | 2022-01-11 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst | 아니오 |
| ref-1207 | Helbing, D., & Molnár, P. (Physical Review E 51(5)) | Social force model for pedestrian dynamics | 1995-05-01 | 논문 | medium | 2026-09-30 | https://link.aps.org/doi/10.1103/PhysRevE.51.4282 | 예 |
| ref-1208 | Rudenko, A., Kucner, T. P., Swaminathan, C. S., Chadalavada, R. T., Arras, K. O., & Lilienthal, A. J. (arXiv; IEEE RA-L 5(2), 2020) | THÖR: Human-Robot Navigation Data Collection and Accurate Motion Trajectories Dataset | 2019-12-11 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/1909.04403 | 아니오 |
| ref-1209 | ATR (Advanced Telecommunications Research Institute International), Brščić, D. 외 | ATC shopping center tracking dataset | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://dil.atr.jp/crest2010_HRI/ATC_dataset/ | 아니오 |
| ref-1210 | 행정안전부 (대한민국 정책브리핑) | 29일부터 인파관리지원시스템 본격 운영…다중운집 … (제목 일부만 확인) | 2023-12-27 | 정부·연구기관 | medium | 2026-09-30 | https://www.korea.kr/news/policyNewsView.do?newsId=148924176 | 아니오 |
| ref-1211 | Vintr, T., Blaha, J., Rektoris, M., Ulrich, J., Rouček, T., Broughton, G., Yan, Z., & Krajník, T. (Frontiers in Robotics and AI) | Toward Benchmarking of Long-Term Spatio-Temporal Maps of Pedestrian Flows for Human-Aware Navigation | 2022-07-04 | 논문 | high | 2026-09-30 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.890013/full | 아니오 |
| ref-1079 | Francis, A., Pérez-D'Arpino, C., Li, C., Xia, F. 외 (arXiv; ACM Transactions on Human-Robot Interaction) | Principles and Guidelines for Evaluating Social Robot Navigation Algorithms | 2023-09-19 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2306.16740 | 아니오 |
| ref-1213 | Pérez-Higueras, N., Otero, R., Caballero, F., & Merino, L. (arXiv; IEEE RA-L 2023) | HuNavSim: A ROS 2 Human Navigation Simulator for Benchmarking Human-Aware Robot Navigation | 2023-09-13 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2305.01303 | 아니오 |
| ref-406 | Open Robotics (osrf/ros2multirobotbook) | Programming Multiple Robots with ROS 2 — Simulation | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://osrf.github.io/ros2multirobotbook/simulation.html | 아니오 |
| ref-1215 | ILIAD 프로젝트 컨소시엄 (EU Horizon 2020) | Concluding ILIAD | 2021-06 | 정부·연구기관 | medium | 2026-09-30 | https://iliad-project.eu/concluding-iliad/ | 아니오 |
| ref-1128 | Gulino, C., Fu, J., Luo, W. 외 (Waymo; arXiv) | Waymax: An Accelerated, Data-Driven Simulator for Large-Scale Autonomous Driving Research | 2023-10-12 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2310.08710 | 아니오 |
| ref-1217 | 조선비즈 (이정아, 다음 뉴스 게재) | 로봇과 인간이 공존하는 병원…약 배달 로봇에 길 비켜주고 엘리베이터도 잡아줘 | 2024-07-12 | 기사 | low | 2026-09-30 | https://v.daum.net/v/bc4riunbUE | 아니오 |
| ref-1218 | Kidokoro, H., Kanda, T., Brščić, D., & Shiomi, M. (ACM/IEEE HRI 2013) | Will I bother here? - A robot anticipating its influence on pedestrian walking comfort | 2013-03 | 논문 | medium | 2026-09-30 | https://www.semanticscholar.org/paper/Will-I-bother-here-A-robot-anticipating-its-on-Kidokoro-Kanda/bc0b26f1c13405fd89eb6d280bee739aed5b07a6 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f19(핵심 질문 답, 추정), f15(낮 혼잡으로 경로가 원활하지 않은 병원 사례), f8(로봇이 혼잡을 만드는 문제) / 섹션 4: 움직임 지도 f1, 사람 궤적 예측 f2, 사회적 힘 모델 f3, 사람 표현·위치 신뢰도 f4, 사회적 내비게이션 원칙 f11, 로그 재생·반응형 에이전트 f17 / 섹션 5: 물류창고 — f14(제약), 병원 — f15(제약, 한국), 상업 시설 — f7(작업 대상)·f8(제약), 실외 — f16(시작 조건, 한국, 연계 대상)·f17(예외·성과), 기타(대학 건물) — f9(제약)·f10(예외·성과). 제조 공장·가정 사례는 찾지 못했음을 명시 / 섹션 6: 실시간 검출·추적 f14·f7, 장기 시공간 흐름 지도 f1·f9·f10, 단기 궤적 예측 f2, 보행자 행동 모델과 시뮬레이션 f3·f8·f12·f13, 운영 규칙 f15, 기록 재현의 반응형 대체 f17·f18 / 섹션 7: REP-155(ROS4HRI) f4·f5, HuNavSim f12, Open-RMF CrowdSim(Menge) f13, 데이터셋 THÖR f6·ATC f7, 평가 지침 f11 / 섹션 8: f1·f2·f3·f8·f9·f11·f17 / 섹션 9: f20(직접 범위), f21(연계 대상) / 섹션 10: f22 — 15, 16, 18, 26, 27, 31, 34, 36, 46, 49, 53, 54, 61, 63, 64, 66 (18번과 34번 구분 유지, L 대분류 46번 연결) / 섹션 11: 기존 oq-256(f17·f18 로 부분 근거, 미해결 유지)과 open_questions_new 3건. 다음 실행 후보: 63. 병원·의료 페이지 5절에 f15, 61. 물류창고 페이지에 f14, 36. 가상 시운전·실제 상황 재현 페이지 11절 oq-256 에 f17·f18 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 사회적 힘 모델 | Social Force Model | 보행자 움직임을 원하는 속도로의 가속, 다른 보행자·벽과의 거리 유지(반발), 끌림을 나타내는 가상의 힘의 합으로 계산하는 보행자 행동 모델이다. |
| 사람 움직임 궤적 예측 | Human Motion Trajectory Prediction | 관측된 과거 위치와 주변 맥락(다른 사람·장애물·목적지)을 바탕으로 사람의 가까운 미래 이동 경로를 추정하는 기법이다. |
| 사회적 내비게이션 | Social Robot Navigation (Human-aware Navigation) | 로봇이 사람 사이를 이동할 때 안전뿐 아니라 쾌적성·가독성·예의 같은 사회적 원칙을 지키도록 경로와 행동을 정하는 주행 방식이다. |
| 로그 재생 에이전트·반응형 에이전트 | Log-replay Agent / Reactive Agent | 시뮬레이션에서 기록된 궤적을 그대로 따르는 배경 참가자(로그 재생)와, 제어 대상의 행동에 반응해 움직임을 바꾸는 모델 기반 참가자(반응형)를 구분하는 용어이다. |

## 열린 질문

새로 생긴 질문:

- 여러 제조사 로봇과 설비 센서가 각자 감지한 사람 위치를 하나의 사람 흐름 모델로 합칠 때 좌표·시각·신뢰도·익명화 형식을 정한 공개 규격이나 구현이 있는가? | 관련 영역: 19. 사람·보행자 모델, 18. 실시간 세계 상태·데이터 일관성, 53. 개인정보·영상 데이터 | 근거: f4 | 종류: 일반
- 병원·상업 시설·물류창고에서 시간대별 사람 혼잡을 로봇 작업 시간 추정과 배정·스케줄링에 반영해 처리 시간이나 지연 변화를 측정한 현장 연구가 있는가? | 관련 영역: 19. 사람·보행자 모델, 26. 작업 순서·스케줄링, 63. 병원·의료 | 근거: f15 | 종류: 일반
- 기지국 기반 인파관리지원시스템 같은 공공 인파 밀집 데이터를 실외 배송로봇의 경로·운행 제한에 연동한 국내 사례나 데이터 제공 조건이 있는가? | 관련 영역: 19. 사람·보행자 모델, 66. 실외 | 근거: f16 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 0
- 예산 사용량: 검색 16회 · 신규 출처 15건
- 미확인 항목:
    - f1 Kucner 외 서베이 원문 미열람(SAGE·Lincoln 403, DARKO 페이지 초록이 다른 논문 문장으로 보여 채택하지 않음) — 검색 요약 범위만 사용
    - f2 Rudenko 서베이의 세부 분류 명칭(물리 기반·패턴 기반·계획 기반 등) 미확인 — PDF 추출 실패
    - f3 Helbing·Molnár 원문 미열람
    - f8 Kidokoro 외 원문·초록 미열람, 혼잡 감소 효과 수치 미확인
    - f4 REP-155 상태: 원문 파일은 Draft, 검색 요약(ROS4HRI 소개)은 '공식 채택'으로 표현 — 최종 상태 미확인
    - f9 벤치마크 수치(600만 건 이상, 약 500㎡)는 요약 도구 경유로 읽어 원문 문구 대조 미확인
    - f10 현장 실험은 40분 세션 4회로 표본이 매우 작음
    - f14 ILIAD 의 창고 현장 정량 효과(사람 방해·처리 시간) 미확인
    - f15 한림대학교성심병원 로봇의 사람 대기 규칙은 기사 1건 기준, 독립 확인 실패
    - oq-256 부분 답: 로봇 플릿 재현에서 기록된 사람을 반응형 보행자 모델로 대체한 공개 사례 미발견
    - 제조 공장·가정 현장의 사람 흐름 반영 사례 미발견
    - ILIAD Safety Stack 논문(RAM 2023) PDF 404 로 넣지 않음
    - Patient–Robot Co-Navigation of Crowded Hospital Environments(Applied Sciences 2023) 403 으로 넣지 않음
- 범위 경계 위반 의심:
    - f14·f15·f21: 온보드 사람 검출·추적, 국소 회피, 정지·양보 동작은 원문 19장 '로봇 자체 지능·제어' 연계 영역이므로 f21 을 '연계 대상: '으로 두고 ROP 직접 범위는 f20 에서 흐름 모델 집계·계획 반영으로 한정함
    - f16: 기지국 기반 공공 인파 관리는 ROP 밖 공공·시설 시스템이므로 '연계 대상: '으로 표시
    - f17: 자율주행 차량 시뮬레이션은 '업종별 조건(실외 차량)' 쪽 자료로, 기록 재현 방법 참고로만 쓰고 로봇 플릿 적용은 추정(f18)으로 둠
    - f3·f12·f13: 보행자 시뮬레이션은 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험) 쪽 기능이고, 현재 사람 위치 표현(f4)은 18. 실시간 세계 상태·데이터 일관성 쪽이므로 연결 제안(f22)에서 구분함
- 한계: web_fetch_available: true · fetch_mode full. 검색 16회/30, 신규 출처 15건/15(ref-1204~ref-1218, 예약 구간 안)로 신규 출처 상한에 도달해 Mavrogiannis 외 사회적 내비게이션 서베이, ILIAD Safety Stack 논문, 병원 군중 동행 리뷰, Kairos(arXiv 2609.27467, 4D 장면 그래프 기반 존재·흐름 예측)를 출처로 넣지 않았다(다음 실행 후보). 재사용 출처 없음(참고문헌 목록 요약에 행이 없어 같은 URL 이 이미 있으면 퍼블리셔 병합 필요; 특히 ref-406 ros2multirobotbook 시뮬레이션 장). 원문 열람: 15건 중 12건을 열었고(webfetch 10, github_raw 2), ref-1204(403)·ref-1207·ref-1218 은 fetched false·원문 미열람이다. 논문 다수는 arXiv 초록 수준만 열었다. 교차 확인 0건. 벤더 주장 없음. 분류 원문 핵심 질문에는 f19 로 답했고 결론은 '실시간 검출·추적, 장기 흐름 지도, 궤적 예측, 보행자 행동 모델, 운영 규칙으로 반영하는 방식은 확인되나 효과 근거는 소규모 실험·단일 사례 중심'이라는 추정이다. 현장 유형 사례는 물류창고(f14)·병원(f15, 한국)·상업 시설(f7·f8)·실외(f16 한국, f17)·기타(f9·f10 대학 건물)이며 제조 공장·가정은 찾지 못했다. 국내 자료는 행정안전부 정책브리핑(ref-1210)과 조선비즈(ref-1217)다. 기존 열린 질문 oq-256 은 f17·f18 로 부분 근거만 있어 해결 제안하지 않았다. L. AI·학습 기술 관련(학습 기반 궤적 예측·흐름 지도 f2·f9)은 46. 예측·학습 기반 최적화와 이 영역 양쪽 연결을 f22 에서 제안했다. 18. 실시간 세계 상태·데이터 일관성과 34. 시뮬레이션·예측용 디지털 트윈은 섞지 않았다. 용어집에 이미 있는 움직임 지도·인프라 장착 센서·통과 가능성·속도·분리 감시·보호 분리 거리·반정적 객체·침범 후 시간은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음.
```

### runs/2026-09-25-48/research.md

```markdown
# 리서치 브리프 2026-09-25-48

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-48 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 19. 모니터링·이상 탐지·원인 분석 |
| 대분류 | E. 협업·현장 운영 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음
- 섹션 5. 현장 시나리오 비어 있음 — 지연 원인(로봇·문·앞 공정) 구분 시나리오 필요
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음
- 섹션 10. 다른 연구영역과의 연결 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 기존 oq-018, oq-033 관련

## 조사 질문

1. 지연 원인이 로봇 고장인지, 문인지, 앞 공정인지 어떻게 찾을까? [분류원문]
2. 로봇–관제 인터페이스 표준(VDA 5050, MassRobotics)과 Open-RMF 는 오류·운용 상태·연결 상태·설비(문) 상태·작업 지연을 어떤 필드와 값으로 보고하는가? (섹션 6·7 겨냥)
3. oq-033 Open-RMF 로봇 상태, VDA 5050 action 상태·오류, MassRobotics 운용 상태를 하나의 공통 상태·오류 어휘로 옮기는 표준 매핑이나 공개 구현이 있는가? (섹션 7·11 겨냥)
4. oq-018 이동로봇·작업대·승강기가 섞인 창고 흐름에 활성 구간 기반 이동 병목 탐지나 객체 중심 프로세스 마이닝을 적용한 연구가 있는가? (섹션 6·8 겨냥)
5. 로그·지표·추적을 연결하는 관측(observability) 오픈소스와 로봇 진단 도구에는 무엇이 있는가? (섹션 4·7 겨냥)
6. 다중 로봇 고장 탐지·진단, 근본 원인 분석 연구와 LLM 기반 실패 설명(27. AI·학습·적응과 모델 운영 교차)은 무엇을 제공하는가? (섹션 6·8 겨냥)
7. 국내 물류 로봇 관제·이상 대응 연구는 무엇이 있고, ROP 직접 범위와 연계 대상(로봇 내부 진단)의 경계는 어디인가? (섹션 8·9 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 최신판 상태(state) 스키마의 오류 객체는 errorType 과 errorLevel 을 필수로 두며, errorLevel 은 WARNING·URGENT·CRITICAL·FATAL 네 값으로 로봇이 현재 주문을 계속할 수 있는지와 새 주문을 받을 수 있는지를 구분한다. | ref-051 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f2 | [사실] | VDA 5050 최신판 상태 스키마는 오류와 관련된 nodeId·edgeId·orderId·actionId 등을 가리키는 errorReferences, 사람이 읽는 설명(errorDescription)과 조치 힌트(errorHint)를 둘 수 있게 하고, 오류와 별도로 INFO·DEBUG 수준의 information 배열을 둔다. | ref-051 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f3 | [사실] | VDA 5050 3.0.0 명세는 실패한 동작(actionStatus FAILED)이 해당하는 오류 보고와 대응하도록 설명하며, 예로 집기·내려놓기 실패를 든다. | ref-031 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f4 | [사실] | VDA 5050 connection 토픽은 로봇의 마지막 유언(last will) 메시지로, 정상 종료(OFFLINE)와 예기치 않은 연결 끊김(CONNECTION_BROKEN)을 구분해 관제에 알린다. | ref-506 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f5 | [사실] | MassRobotics AMR 상호운용 표준의 상태 보고는 운용 상태(operationalState)에 navigating·idle·disabled·offline·charging 외에 waitingHumanEvent·waitingExternalEvent·waitingInternalEvent·manualOverride 를 두어 대기 원인을 사람·외부·내부 사건으로 나누고, 정상 운용 때는 생략하는 errorCodes 배열을 둔다. | ref-230 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f6 | [사실] | Open-RMF 에서 문 노드는 문 상태(DoorState)를 /door_states 토픽으로 발행하고, 문 모드(DoorMode)는 closed·moving·open·offline·unknown 다섯 값이다. | ref-313, ref-283 | 아니오 | medium | 2026-09-25 | 보충 / 제약 | — |
| f7 | [사실] | Open-RMF 문 어댑터는 플릿 어댑터의 문 요청을 받아 진행 중인 로봇 작업을 방해하지 않을 때만 문을 움직이게 하는 상태 감독자 역할을 한다. | ref-283 | 아니오 | medium | 2026-09-25 | 보충 / 제약 | — |
| f8 | [사실] | Open-RMF 작업 상태(task_state) 스키마는 작업·단계·이벤트 상태 토큰으로 blocked·delayed·error·failed·underway·completed 등을 두고, 완료 예상 시간(estimate_millis), 중단 기록(interruptions), 배정 상태(failed_to_assign 등)를 함께 기록한다. | ref-111 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f9 | [사실] | Open-RMF 경보 메시지(rmf_task_msgs Alert)는 심각도 등급(INFO·WARNING·ERROR), 운영자가 고를 수 있는 응답 목록, 관련 작업 id 를 담는다. | ref-503 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f10 | [추정] | f1~f9 에 따르면 분류 원문의 질문(지연 원인이 로봇·문·앞 공정 중 무엇인가)은 작업 상태의 지연·차단(Open-RMF), 로봇 오류 수준과 연결 끊김(VDA 5050), 외부 사건 대기(MassRobotics), 문 모드(Open-RMF)를 같은 시간축에 맞춰 보는 방식으로 접근할 수 있어 보이나, 세 어휘가 서로 달라 ROP 가 자체 원인 범주로 옮기는 매핑이 필요할 것으로 보인다. | ref-051, ref-506, ref-230, ref-313, ref-111 | 아니오 | low | 2026-09-25 | 보충 / 예외·성과 | — |
| f11 | [사실] | ROS 2 diagnostics 는 하드웨어 드라이버가 /diagnostics 토픽에 DiagnosticArray 로 진단 정보를 발행하게 하고, diagnostic_updater(발행 도우미), diagnostic_aggregator(플러그인 규칙으로 집계), diagnostic_remote_logging(InfluxDB 등 원격 전송) 등의 패키지를 제공한다. | ref-500 | 아니오 | medium | 2026-09-25 | — | — |
| f12 | [사실] | ros2_tracing 은 LTTng 기반으로 ROS 2 핵심 패키지에 추적 지점(tracepoint)을 넣고 실행 시 추적을 설정하는 도구를 제공하는 저오버헤드 추적 프레임워크이다. | ref-501 | 아니오 | medium | 2026-09-25 | — | — |
| f13 | [사실] | OpenTelemetry 명세는 추적(traces)·지표(metrics)·로그(logs)·배기지(baggage) 신호를 정의하고, 추적을 부모–자식 관계의 스팬(span)으로 이루어진 방향 비순환 그래프로 보며, TraceId·SpanId 로 신호를 서로 연결한다. | ref-502 | 아니오 | medium | 2026-09-25 | — | — |
| f14 | [추정] | 주문 id·작업 id·로봇 동작 id 를 하나의 추적 문맥으로 묶으면(OpenTelemetry 식 추적과 VDA 5050 errorReferences 의 orderId·actionId) 로봇 오류를 해당 주문 지연과 연결할 수 있을 것으로 보이나, 물류 로봇 관제에 적용한 공개 사례는 이번 실행에서 확인하지 못했다. | ref-502, ref-051 | 아니오 | low | 2026-09-25 | 예외·성과 | — |
| f15 | [사실] | Khalastchi·Kalech(Sensors, 2019)의 설문 논문은 다중 로봇 시스템의 속성이 고장 탐지·진단(FDD)에 서로 다른 어려움을 준다고 보고 적용 가능한 FDD 접근을 정리하며, 계획 진단에서 실패한 동작을 찾는 1차 진단과 그 근본 원인(에이전트·장비)을 찾는 2차 진단을 구분한다. | ref-509 | 아니오 | medium | 2019 | 예외·성과 | 원문 미열람 |
| f16 | [사실] | Roser·Nakano·Tanaka(WSC 2003)는 무인운반차(AGV) 시스템에서 가동률·대기 시간 기반 병목 탐지와 자신들의 이동 병목(shifting bottleneck) 탐지 방법을 비교해, 기존 두 방법은 주 병목을 안정적으로 찾지 못할 때가 있다고 보고한다. | ref-510 | 아니오 | medium | 2003 | 예외·성과 | 원문 미열람 |
| f17 | [사실] | Soldani·Brogi(ACM Computing Surveys, 2022)는 다중 서비스 클라우드 응용의 이상 탐지와 실패 근본 원인 분석 기법을 정리하며, 로그에서 서비스 간 인과 그래프를 도출해 원인을 좁히는 접근을 포함한다. | ref-511 | 아니오 | medium | 2022 | — | 원문 미열람 |
| f18 | [사실] | REFLECT(Liu 외, CoRL 2023)는 영상·소리·로봇 상태 같은 다중 감각 관측을 계층적 경험 요약으로 바꾼 뒤 LLM 에 실패 원인 설명과 수정 계획을 묻는 방법으로, 실행 실패와 계획 실패를 모두 다룬다. | ref-512 | 아니오 | medium | 2023 | 예외·성과 | 원문 미열람 |
| f19 | [사실] | 공급망 관리(SCM)에서 프로세스 마이닝의 현황·활용 사례·연구 전망을 정리한 리뷰 논문이 International Journal of Production Research(2024)에 게재되었다. | ref-513 | 아니오 | medium | 2024 | — | 원문 미열람 |
| f20 | [사실] | 국내 연구(DBpia, 2026-07)는 다중 AMR 운영용 웹 기반 사용자 중심 관제 인터페이스를 가상 테스트베드에서 피험자 10명으로 예비 평가해, 대조군 대비 이상 대응 시간이 39.6% 단축되었다고 보고한다. | ref-514 | 아니오 | low | 2026-07 | 예외·성과 | 원문 미열람 |
| f21 | [추정] | 연계 대상: 센서·모터·드라이버 수준의 진단(ROS 2 diagnostics 같은 로봇 내부 진단)과 개별 부품 고장 진단은 로봇 제조사 영역이며, 이종 로봇을 연결하는 ROP 는 표준 인터페이스가 보고하는 오류 수준·연결 상태·설비 상태·작업 상태를 모아 원인 범주(로봇·설비·통신·공정)로 구분하고 업무 영향과 연결하는 부분을 맡는 경계가 될 것으로 보인다. | ref-500, ref-051, ref-506, ref-111 | 아니오 | low | 2026-09-25 | 예외·성과 | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 아니오 |
| ref-500 | ROS (ros/diagnostics GitHub) | diagnostics — README (ros2 branch) | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/ros/diagnostics/blob/ros2/README.md | 아니오 |
| ref-501 | ROS 2 (ros2/ros2_tracing GitHub) | ros2_tracing — README | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/ros2/ros2_tracing | 아니오 |
| ref-502 | OpenTelemetry (CNCF) | OpenTelemetry Specification — Overview | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/overview.md | 아니오 |
| ref-503 | Open Robotics (open-rmf/rmf_internal_msgs) | rmf_task_msgs/msg/Alert.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_task_msgs/msg/Alert.msg | 아니오 |
| ref-313 | Open Robotics (open-rmf/rmf_internal_msgs) | rmf_door_msgs/msg/DoorMode.msg | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_door_msgs/msg/DoorMode.msg | 아니오 |
| ref-111 | Open Robotics (open-rmf/rmf_api_msgs) | rmf_api_msgs/schemas/task_state.json | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 아니오 |
| ref-506 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/connection.schema | 미확인 | 표준 | high | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/connection.schema | 아니오 |
| ref-230 | MassRobotics (MassRobotics-AMR/AMR_Interop_Standard) | AMR_Interop_Standard.json | 미확인 | 표준 | high | 2026-09-25 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json | 아니오 |
| ref-283 | Open Robotics (osrf/ros2multirobotbook) | Programming Multiple Robots with ROS 2 — Doors | 미확인 | 오픈소스 문서 | high | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_doors.html | 아니오 |
| ref-509 | Khalastchi, E., & Kalech, M. | Fault Detection and Diagnosis in Multi-Robot Systems: A Survey | 2019 | 논문 | medium | 2026-09-25 | https://doi.org/10.3390/s19184019 | 예 |
| ref-510 | Roser, C., Nakano, M., & Tanaka, M. | Comparison of bottleneck detection methods for AGV systems | 2003 | 논문 | medium | 2026-09-25 | https://keio.elsevierpure.com/en/publications/comparison-of-bottleneck-detection-methods-for-agv-systems/ | 예 |
| ref-511 | Soldani, J., & Brogi, A. | Anomaly Detection and Failure Root Cause Analysis in (Micro) Service-Based Cloud Applications: A Survey | 2022 | 논문 | medium | 2026-09-25 | https://dl.acm.org/doi/full/10.1145/3501297 | 예 |
| ref-512 | Liu, Z., Bahety, A., & Song, S. | REFLECT: Summarizing Robot Experiences for Failure Explanation and Correction | 2023 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2306.15724 | 예 |
| ref-513 | Leopold, H. 외(International Journal of Production Research) | Process mining in supply chain management: state-of-the-art, use cases and research outlook | 2024 | 논문 | medium | 2026-09-25 | https://www.tandfonline.com/doi/full/10.1080/00207543.2024.2412285 | 예 |
| ref-514 | DBpia 게재 논문(저자 미확인) | 다중 자율이동로봇 (AMR) 운영을 위한 웹 기반 사용자 중심 관제 인터페이스 설계 연구 | 2026-07 | 논문 | medium | 2026-09-25 | https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE12892366 | 예 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/e-collaboration-and-field-operations/19-monitoring-anomaly-detection-and-root-cause-analysis.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 3절: f10·f16·f20(지연 원인 구분과 병목 탐지의 필요) / 4절: f1(오류 수준), f4(연결 끊김), f13(추적·스팬), f15(FDD 1차·2차 진단), f16(이동 병목) / 5절: 보충 단계에서 문 대기로 AMR 이 지연되는 시나리오 f5·f6·f7·f8·f10 (제약·예외·성과) / 6절: 상태·오류 어휘의 시간축 결합 f10, 추적 문맥 연결 f14, 병목 탐지 f16, 근본 원인 분석 f15·f17, LLM 실패 설명 f18(27. AI·학습·적응과 모델 운영과 양쪽 연결) / 7절: VDA 5050 f1~f4, MassRobotics f5, Open-RMF f6~f9, ROS 2 diagnostics f11, ros2_tracing f12, OpenTelemetry f13 / 8절: f15~f20 / 9절: f21(로봇 내부 진단은 연계 대상) / 10절: 9. 로봇·제조사 관제 연동(f1~f5), 10. 설비·건물 시스템 연동(f6·f7), 12. 명령·작업 실행의 신뢰성(f3·f8), 4. 성과·경제성·프로세스 개선(f16·f19, oq-018), 18. 사람–로봇 협업·운영 인터페이스(f9·f20), 20. 예외 복구·재계획·업무 연속성(f1·f9), 8. 실시간 세계 상태·데이터 일관성(f10, 현재 상태 표현), 27. AI·학습·적응과 모델 운영(f18) / 11절: oq-018·oq-033 과 새 질문 3건 |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 근본 원인 분석 | Root Cause Analysis (RCA) | 관측된 이상이나 실패를 일으킨 가장 근원적인 원인(구성 요소·사건)을 찾아내는 분석이다. |
| 고장 탐지·진단 | Fault Detection and Diagnosis (FDD) | 시스템에 고장이 생겼음을 알아내고(탐지) 그 종류와 위치·원인을 밝히는(진단) 기법의 총칭이다. |
| 이동 병목 탐지 | Shifting Bottleneck Detection (Active Period Method) | 각 설비·차량이 끊김 없이 활성 상태로 있는 구간의 길이로 시점마다 병목을 판정하고 병목의 이동을 추적하는 방법이다. |
| 분산 추적 | Distributed Tracing | 하나의 요청이 여러 구성 요소를 거치는 과정을 공통 추적 id 로 묶은 스팬들의 그래프로 기록하는 관측 기법이다. |

## 열린 질문

새로 생긴 질문:

- VDA 5050 3.0 의 네 단계 오류 수준(WARNING·URGENT·CRITICAL·FATAL)과 2.x 의 두 단계(WARNING·FATAL)가 섞인 이종 플릿에서 오류 수준을 어떻게 맞춰 해석하는가? | 관련 영역: 19. 모니터링·이상 탐지·원인 분석, 9. 로봇·제조사 관제 연동 | 근거: f1 | 종류: 일반
- 물류 로봇 작업 지연을 로봇·설비·통신·공정 원인으로 나누는 공개 원인 분류 체계나 현장 데이터셋이 있는가? | 관련 영역: 19. 모니터링·이상 탐지·원인 분석, 4. 성과·경제성·프로세스 개선 | 근거: f10 | 종류: 일반
- 국내 물류센터에서 로봇 정지·지연의 원인별 발생 비율이나 이상 대응 시간을 실측해 공개한 자료가 있는가? | 관련 영역: 19. 모니터링·이상 탐지·원인 분석, 20. 예외 복구·재계획·업무 연속성 | 근거: f20 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 17 · 교차 확인: 0
- 예산 사용량: 검색 25회 · 신규 출처 15건
- 미확인 항목:
    - f3 VDA 5050 명세의 동작 실패–오류 대응 문구는 요약 도구 경유로 읽어 원문 문구와 글자 단위 대조 미확인
    - f15~f20 논문 원문 미열람(검색 요약 기준)
    - f20 국내 논문 저자 미확인, 수치는 피험자 10명 가상 테스트베드 예비 연구 조건
    - ref-513 공저자 전체 미확인
    - oq-018 미해결: AGV 병목 탐지(f16)와 SCM 프로세스 마이닝 리뷰(f19)는 찾았으나 이동로봇·작업대·승강기 혼합 흐름 적용 연구는 미발견
    - oq-033 미해결: 세 어휘 공통 매핑 표준·공개 구현 미발견(ros_amr_interop 의 MassRobotics 송신기는 YAML 로 ROS 2 데이터를 매핑하나 오류·상태 어휘 매핑 설명 없음)
    - 모든 finding 교차 확인 없음
- 범위 경계 위반 의심:
    - f21: 센서·모터·드라이버 진단은 분류 원문 9장 로봇 자체 지능·제어 연계 영역이므로 연계 대상으로 표시
    - f7: 문 제어 자체는 시설·설비 제어 연계 영역이며 ROP 는 문 상태 확인·요청만 다룬다는 구분 필요
    - f20: 논문의 디지털 트윈은 실시간 상태 표시(8. 실시간 세계 상태·데이터 일관성)이며 22. 시뮬레이션·예측용 디지털 트윈과 섞지 않도록 주의
- 한계: web_fetch_available: false, fetch_mode mirror_only. raw.githubusercontent.com 으로 연 출처: 재사용 ref-031·ref-051, 신규 ref-500~ref-283. 신규 ref-509~ref-514 는 원문 미열람(신뢰도 상한 medium). 검색 25회/30, 신규 출처 15건/15(상한 도달로 Spatial Process Mining arXiv 2506.06081, inorbit-ai ros_amr_interop README 는 출처로 넣지 않음, 다음 실행 후보). 참고문헌 목록이 요약본(대상 페이지 인용 0건)으로만 와서 VDA 5050 connection.schema·MassRobotics JSON·Open-RMF 문 연동 장 등이 기존 id 로 이미 있는지 확인하지 못함 — 같은 URL 이면 퍼블리셔 병합 필요. 한국어 검색 3회에서 국내 물류센터 로봇 장애 원인 분석·프로세스 마이닝 사례는 찾지 못했고 국내 자료는 f20 1건. 벤더 가동률 사례 글(oxmaint 등)은 방법이 공개되지 않아 넣지 않음. 27. AI·학습·적응과 모델 운영 관련 f18 은 27번 페이지와 양쪽 연결 제안. 정정 요청 없음.
```

### data/source_texts/ref-406.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

````text
# Simulation

This chapter describes how to generate building models from
`traffic_editor` files, and then simulate fleets of robots in those models.

## Motivation

Simulation environments for testing robotic solutions offer immense value across
various stages of R&D and deployment. More notably, simulations provide the
following benefits:

- **Time and resource saving:** While testing with hardware is indispensable,
  the process can slow development with additional setup time, robot
  downtime and reset periods between trials. As the number of participants
  scale, so do costs associated with purchasing hardware and consumables for
  testing. This is especially true when utilizing a solution such as RMF, which aims to
  integrate several mobile/stationary robots together with building systems such as doors
  and lifts. Simulations provide a potentially cost-effective and time-saving alternative
  for evaluating the behavior of robot systems at scale. More importantly,
  simulations can help answer questions prior to deployment such as how many
  participants can be supported or how the existing behavior would change with
  the introduction of a new fleet, both of which can inform purchasing decisions
  for facility owners.

- **Robust testing:** Robots in simulation neither run out of battery nor incur costs when they happen to unfortunately crash into something. Scenarios
  can be tested for hours at a stretch, at faster speeds, to fine tune
  algorithms and verify their robustness. One consideration about the appropriate amount of scenario testing to run is a decision that depends on how much compute power you want to avail for the simulation. With the introduction of cloud simulation, this limit is then a trade off of cost and speed as well. As scenarios in simulation are
  repeatable, fixes for undesirable bugs encountered can be readily validated.
  Reaction of the system to edge cases which are rare but have severe
  consequences can also be studied through simulation. Data logged from hardware
  trials can be used to recreate the scenario in simulation which may be further
  helpful for debugging. Lastly, long running simulations can instill confidence
  in facility owners prior to deployment.

Physics-based simulators, such as `Gazebo`, carry the benefit of easily
interfacing with ROS 2 nodes through wrappers provided by `gazebo_ros_pkgs`.
Gazebo plugins can be developed that accurately emulate the behavior of robots,
sensors and infrastructure systems which enhance the overall fidelity of
simulations. It is worth emphasizing here that the exact same code used to run the simulations
will also be run on the physical system as well without any changes.

However, despite these compelling benefits, simulations are sparingly employed
by developers and system integrators, citing complexity over generating
environments and configuring them with appropriate plugins. In a recent publication "_A Study on the Challenges of Using Robotics Simulators for Testing_," by Afsoon Afzal, Deborah S. Katz, Claire Le Goues and Christopher S. Timperley they noted the main reasons participants gave for not using simulation for a particular project and summarized their findings as follows:

| Reason for not using simulation  | #  | %  |
|---|---|---|
| Lack of time or resources | 15 | 53.57% |
| Not realistic/accurate enough | 15 | 53.57% |
| Lack of expertise or knowledge on how to use software-based simulation | 6  | 21.43% |
| There was no simulator for the robot | 4  | 14.29% |
| Not applicable | 4  | 14.29% |
| Too much time or compute resources | 2  | 7.14%  |
| Nobody suggested it | 0  | 0.00%  |
| Other | 2  | 7.14%  |

The RMF project aims to address these hurdles by simplifying the process of setting up
simulation environments for multi-fleet traffic control, as we will explain further throughout this section.

## Building Map Generator
`traffic_editor`, discussed in the previous chapter, is a tool to annotate building
floor plans with fleet-specific traffic information in a vendor neutral manner.
This includes waypoints of interest, traffic lanes and shared resources such as
doorways and lifts. It can also be used to markup the walls and floors and add
thumbnails of artifacts in the environment. The ability to auto-generate a 3D
world using this annotated map is significantly valuable for simplifying the
creation and management of simulations. To this end, the `building_map_tools`
package in `traffic_editor` contains an executable `building_map_generator`. The
executable operates in two modes:

1. Generate a Gazebo/Ignition compliant `.world` file
2. Export the fleet specific traffic information in the form
of navigation graphs which are utilized by `fleet_adapters` for planning

![Building map generator](images/building_map_generator.png)

To auto-generate a Gazebo simulation world, the executable takes in the command argument `gazebo` along with others described below:

```bash
usage: building_map_generator gazebo [-h] [--TEMPLATE_WORLD_FILE TEMPLATE_WORLD_FILE]
                                     INPUT OUTPUT_WORLD OUTPUT_MODEL_DIR

positional arguments:
  INPUT                 Input building.yaml file to process
  OUTPUT_WORLD          Name of the .world file to output
  OUTPUT_MODEL_DIR      Path to output the map model files

options:
  -h, --help            show this help message and exit
  --TEMPLATE_WORLD_FILE TEMPLATE_WORLD_FILE
                        Specify the template for the base simulation.
```

The script parses the `.building.yaml` file and generates meshes for the
flooring and walls for each level. Those meshes are then combined into a `model.sdf` file in
the `OUTPUT_MODEL_DIR/` directory. The `model.sdf` files for each level are
imported into the `.world` with filepath `OUTPUT_WORLD`. Model sub-elements for
various static objects annotated in the `traffic_editor` are included in the
`.world` as seen in the snippet below:

```xml
<include>
  <name>OfficeChairBlack_6</name>
  <uri>model://OfficeChairBlack</uri>
  <pose>4.26201267190027 -7.489812761393875 0 0 0 1.1212</pose>
  <static>True</static>
</include>
```

Similar blocks for annotated robots are
generated. It is the responsibility of the user to append the environment
variable `$GAZEBO_MODEL_PATH` with the relevant paths to the models prior to
loading the `.world` file in Gazebo. This process can be simplified through ROS 2
launch files and will be discussed in later sections.

The parser also includes sdf elements for other dynamic assets such as doors and
lifts. Their mechanisms are discussed in the next section.

By default, the simulation world is loaded without any additional plugins. So if
you were to spawn things like cameras or lidars in your gazebo world it would not
work. This can be bypassed by using the `--TEMPLATE_WORLD_FILE`. This allows you
to add additional simulation assets to your world.

Reconfiguring simulation environments becomes as trivial as editing the
annotations on the 2D drawing and re-running the `building_map_generator`. This
is exceedingly useful to quickly evaluate traffic flow as the spatial
configuration in the facility changes.

To generate navigation graphs for fleet adapters, the `building_map_generator`
is executed with command argument `nav`. The navigation graph is generated as
a `.yaml` file and is parsed during launch by the corresponding fleet adapter.

```bash
usage: building_map_generator nav [-h] INPUT OUTPUT_DIR

positional arguments:
  INPUT       Input building.yaml file to process
  OUTPUT_DIR  Path to output the nav .yaml files
```

## RMF Assets and Plugins

Assets play a pivotal role in recreating environments in simulation. Projects
such as RMF, SubT and others have allowed developers to create and open source
3D models of robots, mechanical infrastructure systems and scene objects.
They are available for download on the [Ignition Fuel app](https://app.ignitionrobotics.org/OpenRobotics/fuel/collections/).
Beyond imparting visual accuracy, assets can be dynamic and interface with RMF
core systems through the aid of plugins.

To simulate the behavior of hardware such as robot models and infrastructure
systems, several Gazebo plugins have been architected. These plugins are
derivatives of the [ModelPlugin](http://osrf-distributions.s3.amazonaws.com/gazebo/api/dev/classgazebo_1_1ModelPlugin.html)
class and tie in standard ROS 2 and RMF core messages to provide necessary
functionality. The following sections briefly describe some of these plugins.

### Robots
As highlighted earlier, several robot models (SESTO, MiR100, Magni, Hospi) have been
open sourced for use in simulation. For these models to emulate the behavior of
their physical counterparts which have been integrated with RMF, they need to 1)
interface with `rmf_fleet_adapters` and 2) navigate to locations in the
simulated world. These functionalities, for a "_full control_" robot type, are
achieved through the `slotcar` [plugin](https://github.com/open-rmf/rmf_simulation/blob/main/rmf_robot_sim_gazebo_plugins/src/slotcar.cpp).
The plugin subscribes to `/robot_path_requests` and `/robot_mode_requests`
topics and responds to relevant `PathRequest` and `ModeRequest` messages
published by its `rmf_fleet_adapter`. The plugin also publishes the robot's
state to the `/robot_state` topic.

To navigate the robot through waypoints in a `PathRequest` message, a simple
"rail-like" navigation algorithm is utilized which accelerates and decelerates
the robot along a straight line from its current position to the next waypoint.
The plugin relies on these fundamental assumptions:
  * The robot model is a two-wheel differential drive robot
  * The left and right wheel joints are named  `joint_tire_left` and `joint_tire_right` respectively

Other parameters, the majority of which are kinematic properties of the robot, are inferred from sdf parameters:
```xml
<plugin name="slotcar" filename="libslotcar.so">
  <nominal_drive_speed>0.5</nominal_drive_speed>
  <nominal_drive_acceleration>0.25</nominal_drive_acceleration>
  <max_drive_acceleration>0.75</max_drive_acceleration>
  <nominal_turn_speed>0.6</nominal_turn_speed>
  <nominal_turn_acceleration>1.5</nominal_turn_acceleration>
  <max_turn_acceleration>2.0</max_turn_acceleration>
  <tire_radius>0.1</tire_radius>
  <base_width>0.3206</base_width>
  <stop_distance>0.75</stop_distance>
  <stop_radius>0.75</stop_radius>
</plugin>
```

During simulation, it is assumed that the robot's path is free of static
obstacles, but the plugin still contains logic to pause the robot's motion if an
obstacle is detected in its path. While it is possible to deploy a sensor based
navigation stack, the approach is avoided to minimize the computational load on
the system from running a navigation stack for each robot in the simulation.
Given the focus on traffic management of heterogeneous fleets and not robot
navigation, the `slotcar` plugin provides an efficient means to simulate the
interaction between RMF core systems and robots.

The `slotcar` plugin is meant to serve as a generalized solution. Vendors are
encouraged to develop and distribute plugins that represent the
capabilities of their robot and the level of integration with RMF more accurately.

### Doors
Unlike robot models whose geometries are fixed and hence can be directly
included in the generated `.world` file, doors are custom defined in
`traffic_editor` and have their own generation pipeline. As seen in the figure
below, an annotated door has several properties which include the location of
its ends, the type of door (hinged, double_hinged, sliding, double_sliding) and
its range of motion (for hinged doors).

![Door properties](images/door_traffic_editor.png)

The `building_map_generator gazebo` script parses a `.building.yaml` file for
any doors and automatically generates an sdf sub-element with links and joints
required for the door along with a configured plugin. The sdf sub-element
generated for the door in the figure above is presented below.

```xml
<model name="coe_door">
  <pose>8.077686357313898 -5.898342045416362 0.0 0 0 1.1560010438234292</pose>
  <plugin filename="libdoor.so" name="door">
    <v_max_door>0.5</v_max_door>
    <a_max_door>0.3</a_max_door>
    <a_nom_door>0.15</a_nom_door>
    <dx_min_door>0.01</dx_min_door>
    <f_max_door>500.0</f_max_door>
    <door left_joint_name="left_joint" name="coe_door" right_joint_name="empty_joint" type="SwingDoor" />
  </plugin>
  <link name="left">
    <pose>0 0 1.11 0 0 0</pose>
    <visual name="left">
      <material>
        <ambient>120 60 0 0.6</ambient>
        <diffuse>120 60 0 0.6</diffuse>
      </material>
      <geometry>
        <box>
          <size>0.8766026166317483 0.03 2.2</size>
        </box>
      </geometry>
    </visual>
    <collision name="left">
      <surface>
        <contact>
          <collide_bitmask>0x02</collide_bitmask>
        </contact>
      </surface>
      <geometry>
        <box>
          <size>0.8766026166317483 0.03 2.2</size>
        </box>
      </geometry>
    </collision>
    <inertial>
      <mass>50.0</mass>
      <inertia>
        <ixx>20.17041666666667</ixx>
        <iyy>23.36846728119012</iyy>
        <izz>3.20555061452345</izz>
      </inertia>
    </inertial>
  </link>
  <joint name="left_joint" type="revolute">
    <parent>world</parent>
    <child>left</child>
    <axis>
      <xyz>0 0 1</xyz>
      <limit>
        <lower>-1.57</lower>
        <upper>0</upper>
      </limit>
    </axis>
    <pose>0.44330130831587417 0 0 0 0 0</pose>
  </joint>
</model>
```

The door [plugin](https://github.com/open-rmf/rmf_simulation/blob/main/rmf_building_sim_common/src/door_common.cpp) responds to `DoorRequest` messages with `door_name` matching its `model name` sdf tag. These messages are published over the `/door_requests` topic. The plugin is agnostic of the type of door defined and relies on the `left_joint_name` and `right_joint_name` parameters to determine which joints to actuate during open and close motions. During these motions, the joints are commanded to their appropriate limits which are specified in the parent element. The joint motions adhere to kinematic constraints specified by sdf parameters while following acceleration and deceleration profiles similar to the `slotcar`.

To avoid situations where one robot requests a door to close on another robot, a `door_supervisor` [node](https://github.com/open-rmf/rmf_ros2/tree/main/rmf_fleet_adapter/src/door_supervisor) is deployed in practice. The node publishes to `/door_requests` and subscribes to `/adapter_door_requests` which the fleet adapters publish to when their robot requires access through a door. The `door_supervisor` keeps track of requests from all the fleet adapters in the system and relays the request to the door adapters while avoiding aforementioned conflicts.

### Lifts
The ability to test lift integration is crucial as these systems are often the operational bottlenecks in facilities given their shared usage by both humans and multi robot fleets. As with annotated doors, lifts can be customized in a number of ways in the `traffic_editor` GUI including the dimension & orientation of the cabin and mapping cabin doors to building levels.

![Customizing lifts in Traffic Editor](images/lift_traffic_editor.png)

The `building_map_generator gazebo` script parses the `.building.yaml` file for lift definitions and auto-generates the sdf elements for the cabin, cabin doors and lift shaft doors.
A prismatic joint is defined at the base of the cabin which is actuated by the lift plugin to move the cabin between different levels.
While the cabin doors are part of the cabin structure, the shaft doors are fixed to the building.
Both sets of doors open and close simultaneously at a given level and are controlled by the lift plugin itself.
These doors are created using the same method as other doors in the building and include the door plugin as well.

The `building_map_generator` also appends a lift plugin (TODO add link element with required parameters to the lift's model sdf block.)

```xml
<plugin filename="liblift.so" name="lift">
  <lift_name>Lift1</lift_name>
  <floor elevation="0.0" name="L1">
    <door_pair cabin_door="CabinDoor_Lift1_door1" shaft_door="ShaftDoor_Lift1_L1_door1" />
  </floor>
  <floor elevation="10.0" name="L2">
    <door_pair cabin_door="CabinDoor_Lift1_door1" shaft_door="ShaftDoor_Lift1_L2_door1" />
    <door_pair cabin_door="CabinDoor_Lift1_door2" shaft_door="ShaftDoor_Lift1_L2_door2" />
  </floor>
  <floor elevation="20.0" name="L3">
    <door_pair cabin_door="CabinDoor_Lift1_door1" shaft_door="ShaftDoor_Lift1_L3_door1" />
  </floor>
  <reference_floor>L1</reference_floor>
  <v_max_cabin>2.0</v_max_cabin>
  <a_max_cabin>1.2</a_max_cabin>
  <a_nom_cabin>1.0</a_nom_cabin>
  <dx_min_cabin>0.001</dx_min_cabin>
  <f_max_cabin>25323.0</f_max_cabin>
  <cabin_joint_name>cabin_joint</cabin_joint_name>
</plugin>
```

The plugin subscribes to `/lift_requests` topic and responds to `LiftRequest` messages with `lift_name` matching its `model name` sdf tag.
The displacement between the cabin's current elevation and that of the `destination_floor` is computed and a suitable velocity is applied to the cabin joint.
Prior to any motion, the cabin doors are closed and only opened at the `destination_floor` if specified in the `LiftRequest` message.
As the cabin and shaft doors are configured with the `door` plugin, they are commanded through `DoorRequest` messages published by the `lift` plugin.
Analogous to the `door_supervisor`, a `lift_supervisor` [node](https://github.com/open-rmf/rmf_ros2/tree/main/rmf_fleet_adapter/src/lift_supervisor) is started in practice to manage requests from different robot fleets.

### Workcells

A common use case is robots performing deliveries within facilities, so a `Delivery` task is configured into the `rmf_fleet_adapters`.
In a delivery task, a payload is loaded onto the robot at one location (pickup waypoint) and unloaded at another (dropoff waypoint).
The loading and unloading of the payload onto and from a robot may be automated by robots/workcells in the facility. These devices are henceforth referred to as dispensers and ingestors respectively.

To replicate the loading and unloading processes in simulation, the `TeleportDispenser` and `TeleportIngestor` [plugins](https://github.com/open-rmf/rmf_simulation/tree/main/rmf_robot_sim_gazebo_plugins/src) have been designed.
These plugins are attached to the `TeleportDispenser` and `TeleportIngestor` [3D models](https://github.com/open-rmf/rmf_demos/tree/main/rmf_demos_assets/models), respectively.
To setup a payload loading station in simulation:
* Add a `TeleportDispenser` model beside the pickup waypoint and assign it a
  unique `name`
* Add the payload model beside the `TeleportDispenser` model (Coke can in image below)

To setup a payload unloading station in simulation:
* Add a `TeleportIngestor` model beside the dropoff waypoint and assign it a
  unique `name`

When a `DispenserRequest` message is published with `target_guid` matching the
name of the `TeleportDispenser` model, the plugin will teleport the payload onto
the nearest robot model. Conversely, when an `IngestorRequest` message is published
with the `target_guid` matching the name of the `TeleportIngestor` model, the
`TeleportIngestor` plugin will teleport the payload from the robot to its location in
the world. The combinations of these plugins allow delivery requests to be simulated.
In the future, these mechanisms will be replaced by actual workcells or robot arms
but the underlying message exchanges will remain the same.

![TeleportDispenser and TeleportIngestor models](images/dispensers.png)

### Crowdsim

Crowd Simulation, aka `CrowdSim` is an optional feature in RMF simulation. User can
choose to enable crowdsim on `rmf_traffic_editor`. In RMF, the crowdsim plugin uses
[menge](https://github.com/open-rmf/menge_vendor) as the core to control each of
simulated agent in the world.

An example of crowdsim is demonstrated on rmf_demos's `airport_world`:
```bash
ros2 launch rmf_demos_gz airport_terminal.launch.xml use_crowdsim:=1
```

For more details on how `crowdsim` works and how to configure it,
please dive in to [the detailed guide for using Crowdsim](https://github.com/FloodShao/crowd_simulation/blob/master/crowd_simulation_doc/crowd_simulation_usage.md).

![crowdsim example](images/airport_crowdsim.png)

---

## Creating Simulations and Running Scenarios
The section aims to provide an overview of the various components in the `rmf_demos` [repository](https://github.com/open-rmf/rmf_demos) which may serve as a reference for setting up other simulations and assigning tasks to robots. Here, we will focus on the `office` world.

### Map package
The `rmf_demos_maps` package houses annotated `traffic_editor` files which will be used for the 3D world generation. Opening the `office.project.yaml` file in `traffic_editor` reveals a single level floorplan that has walls, floors, scale measurements, doors, lanes and models annotated. All the robot lanes are set to `bidirectional` with `graph_idx` equal to "0". The latter signifies that all the lanes belong to the same fleet. In the `airport` world, we have two sets of graphs with indices "0" and "1" which reflect laneways occupiable by two fleets respectively. The figure below highlights properties assigned to a lane and a waypoint that serves as a robot spawn location.

![Robot spawn location properties](images/rmf_demos_maps.png)

To export a 3D world file along with the navigation graphs, the `building_map_generator` script is used. The `CMakeLists.txt` file of this package is configured to automatically run the generator scripts when the package is built. The outputs are installed to the `share/` directory for the package. This allows for the generated files to be easily located and used by other packages in the demo.

```cmake
foreach(path ${traffic_editor_paths})

  # Get the output world name
  string(REPLACE "." ";" list1 ${path})
  list(GET list1 0 name)
  string(REPLACE "/" ";" list2 ${name})
  list(GET list2 -1 world_name)

  set(map_path ${path})
  set(output_world_name ${world_name})
  set(output_dir ${CMAKE_CURRENT_BINARY_DIR}/maps/${output_world_name})
  set(output_world_path ${output_dir}/${output_world_name}.world)
  set(output_model_dir ${output_dir}/models)

  # first, generate the world
  add_custom_command(
    OUTPUT ${output_world_path}
    COMMAND ros2 run rmf_building_map_tools building_map_generator gazebo ${map_path} ${output_world_path} ${output_model_dir}
    DEPENDS ${map_path}
  )

  add_custom_target(generate_${output_world_name} ALL
    DEPENDS ${output_world_path}
  )

  # now, generate the nav graphs
  set(output_nav_graphs_dir ${output_dir}/nav_graphs/)
  set(output_nav_graphs_phony ${output_nav_graphs_dir}/phony)
  add_custom_command(
    OUTPUT ${output_nav_graphs_phony}
    COMMAND ros2 run rmf_building_map_tools building_map_generator nav ${map_path} ${output_nav_graphs_dir}
    DEPENDS ${map_path}
  )

  add_custom_target(generate_${output_world_name}_nav_graphs ALL
    DEPENDS ${output_nav_graphs_phony}
  )

  install(
    DIRECTORY ${output_dir}
    DESTINATION share/${PROJECT_NAME}/maps
  )

endforeach()

```

### Launch Files
The `rmf_demos` package includes all the essential launch files required to bring up the simulation world and start various RMF services. The office simulation is launched using the `office.launch.xml` file. First, a `common.launch.xml` file is loaded and starts:
  * The `rmf_traffic_schedule` node responsible for maintaining the database of robot trajectories and monitoring traffic for conflicts. If a conflict is detected, notifications are sent to relevant fleet adapters which begin the negotiation process to find an optimal resolution.
  * The `building_map_server` which publishes a `BuildingMap` message used by UIs for visualization. The executable takes in the path to the relevant `.building.yaml` file as an argument. The `office.building.yaml` file installed by the `rmf_demos_maps` package is located using the `find-pkg-share` substitution command and is stored in the `config_file` argument.
  * The `rmf_schedule_visualizer` which is an RViz based UI to visualize the traffic lanes, actual positions of the robots, expected trajectory of robots as reflected in the `rmf_traffic_schedule` and states of building systems such as door and lifts.
  * The `door_supervisor` and `lift_supervisor` nodes to manage requests submitted by fleet adapter and UIs.

```xml
<!-- Common launch -->
<include file="$(find-pkg-share demos)/common.launch.xml">
  <arg name="use_sim_time" value="true"/>
  <arg name="viz_config_file" value ="$(find-pkg-share demos)/include/office/office.rviz"/>
  <arg name="config_file" value="$(find-pkg-share rmf_demos_maps)/office/office.building.yaml"/>
</include>
```

To launch a simulated world in gazebo, a snippet from [rmf_demos_gz](https://github.com/open-rmf/rmf_demos/tree/main/rmf_demos_gz)
is shown below. Similarly, user can also choose to run with ignition
simulator, [rmf_demos_ign](https://github.com/open-rmf/rmf_demos/tree/main/rmf_demos_ign)

```xml
  <group>
    <let name="world_path" value="$(find-pkg-share rmf_demos_maps)/maps/office/office.world" />
    <let name="model_path" value="$(find-pkg-share rmf_demos_maps)/maps/office/models:$(find-pkg-share rmf_demos_assets)/models:/usr/share/gazebo-9/models" />
    <let name="resource_path" value="$(find-pkg-share rmf_demos_assets):/usr/share/gazebo-9" />
    <let name="plugin_path" value="$(find-pkg-prefix rmf_gazebo_plugins)/lib:$(find-pkg-prefix building_gazebo_plugins)/lib" />

    <executable cmd="gzserver --verbose -s libgazebo_ros_factory.so -s libgazebo_ros_init.so $(var world_path)" output="both">
      <env name="GAZEBO_MODEL_PATH" value="$(var model_path)" />
      <env name="GAZEBO_RESOURCE_PATH" value="$(var resource_path)" />
      <env name="GAZEBO_PLUGIN_PATH" value="$(var plugin_path)" />
      <env name="GAZEBO_MODEL_DATABASE_URI" value="" />
    </executable>
    <executable cmd="gzclient --verbose $(var world_path)" output="both">
      <env name="GAZEBO_MODEL_PATH" value="$(var model_path)" />
      <env name="GAZEBO_RESOURCE_PATH" value="$(var resource_path)" />
      <env name="GAZEBO_PLUGIN_PATH" value="$(var plugin_path)" />
    </executable>
  </group>
```

Lastly, instances of the "full control" `rmf_fleet_adapter` are launched for each robot type annotated in the map. The navigation graphs for each fleet as generated by the `building_map_generator` script is passed via the `nav_graph_file` argument. For the office map, a single fleet of `Magni` robots is defined. Hence, a single `magni_adapter.launch.xml` file configured with the kinematic properties of this robot type along with spatial thresholds used for planning, is launched. Along with the fleet adapter, a `robot_state_aggregator` node is started. This node aggregates `RobotState` messages with `RobotState.name` containing the `robot_prefix` argument and publishes the aggregate to `/fleet_states` with `FleetState.name` specified by the `fleet_name` argument.

```xml
<group>
  <let name="fleet_name" value="magni"/>
  <include file="$(find-pkg-share rmf_demos)/include/adapters/magni_adapter.launch.xml">
    <arg name="fleet_name" value="$(var fleet_name)"/>
    <arg name="use_sim_time" value="$(var use_sim_time)"/>
    <arg name="nav_graph_file" value="$(find-pkg-share rmf_demos_maps)/maps/office/nav_graphs/0.yaml" />
  </include>
  <include file="$(find-pkg-share rmf_fleet_adapter)/robot_state_aggregator.launch.xml">
    <arg name="robot_prefix" value="magni"/>
    <arg name="fleet_name" value="$(var fleet_name)"/>
    <arg name="use_sim_time" value="true"/>
  </include>
</group>
```

When testing RMF with hardware, the same launch files can be used, with the exception of starting `Gazebo`.
More information on running demos with hardware can be found [the chapter on Integration](integration.md).

### Task Requests
RMF supports various tasks out of the box. For more information see [Tasks in RMF](./task.md)
A web-based dashboard is provided to allow users to send commands to RMF.
Once the [dashboard server](https://github.com/open-rmf/rmf_demos/blob/0d4265a6c81a24e2bbfe6378b4060e94f50066a9/rmf_demos/launch/common.launch.xml#L67-L72) is launched, it can be accessed at https://open-rmf.github.io/rmf-panel-js/.

![Custom RMF web panel](https://github.com/open-rmf/rmf_demos/raw/media/RMF_Panel.png?raw=true)

Alternatively several scripts exist in `rmf_demos_tasks` to assist users with submitting requests from the terminal. Presently the `dispatch_loop.py`, `dispatch_delivery.py` and `dispatch_clean.py` scripts can be used to submit `Loop`, `Delivery` and `Clean` requests.

## Conclusion

This chapter covered the utilization of the `traffic_editor` tool to create annotated maps that allow the auto-generation of 3D worlds for simulations.
It also covered the assets used within simulations and the corresponding plugins necessary for ROS 2 and RMF to interface with them.
A working example of these components running together, in the form of the `rmf_demos_maps` package, was provided as a reference for how to actualize a custom system.
The next chapter will introduces the basic concept behind RMF.
````
