(너의 규칙은 시스템 프롬프트의 agents/shared-rules.md 와 agents/verifier.md 이다. 아래는 이번 실행의 컨텍스트와 입력이다.)

## 실행 컨텍스트

- run_id: 2026-10-09-13
- date: 2026-10-09
- run_type: update (갱신)
- 대상: 33. 시나리오 모델·편집 (I. 설계·시뮬레이션)
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

### runs/2026-10-09-13/target.json

```json
{
  "run_id": "2026-10-09-13",
  "date": "2026-10-09",
  "weekday": "Fri",
  "run_number": 146,
  "run_type": "update",
  "forced": true,
  "target": {
    "area_no": 33,
    "area_name": "33. 시나리오 모델·편집",
    "category": "I. 설계·시뮬레이션",
    "category_letter": "I"
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
  "selection_rationale": "CLI 지정 run_type=update, area=33"
}
```

### runs/2026-10-09-13/research.json

```json
{
  "run_id": "2026-10-09-13",
  "date": "2026-10-09",
  "run_type": "update",
  "target": {
    "area_no": 33,
    "area_name": "33. 시나리오 모델·편집",
    "category": "I. 설계·시뮬레이션"
  },
  "gaps": [
    "섹션 5. 적용 사례 (현장 유형 명시) — 물류창고 사례 없음('찾지 못했다'로 남음), 국내 자료 없음",
    "섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 — '개별 시나리오 인스턴스의 버전 관리 방식은 공개 자료에서 찾지 못했다'는 문장이 근거 없이 남아 있음(oq-234)",
    "섹션 6·7. 대표 접근법·관련 오픈소스 — 시설 주석 편집기를 traffic-editor 로만 서술. Open-RMF 의 후속 편집기(Site Editor) 전환이 반영되지 않음(바뀐 출처)",
    "섹션 6·8 — 로봇 쪽 시나리오 기술 언어(OpenSCENARIO 2 DSL 재사용), 시나리오 변형·인스턴스 해석·출처 추적 연구 없음",
    "섹션 11. 열린 질문 — oq-131·oq-233·oq-234·oq-235·oq-236 해결 근거 미조사",
    "섹션 3. 왜 중요한가 — 실무자 면담 같은 직접 근거 없이 종합 추정만 있음",
    "정정 요청 없음, 발행 2년이 지난 표준·수치 없음(Arena-Bench 2022 는 논문이라 재확인 대상 아님)"
  ],
  "research_questions": [
    "현장·로봇·사람·작업을 담은 시나리오를 어떻게 표현하고 다시 쓸 것인가? [분류원문]",
    "oq-234 형식 판이 바뀔 때 개별 시나리오 인스턴스를 옮기고 호환성을 검사하는 버전 관리 규칙을 공개한 로봇 시뮬레이션 도구나 표준이 있는가? (섹션 9 문장 정정 겨냥)",
    "oq-235 장애·긴급 요청을 시각·발생 조건으로 선언하는 방식을 여러 제조사 로봇과 설비 장애까지 일반화한 시나리오 형식이 있는가? (섹션 6·11 겨냥)",
    "oq-131 실행 기록이나 사고 기록을 시뮬레이션 시나리오로 바꾸는 공개 형식·방법이 있는가? (섹션 6·11 겨냥)",
    "물류창고 현장의 시나리오 예제·벤치마크·편집 도구는 무엇이 있으며(oq-236 국내 예제 라이브러리 포함) 무엇을 담는가? (섹션 5 겨냥)",
    "oq-233 시설 주석 편집기와 건물 형식(Open-RMF traffic-editor·.building.yaml)은 이후 어떻게 바뀌었고, 로봇 쪽에서 기존 시나리오 형식(OpenSCENARIO 등)을 조합해 쓰는 사례가 있는가? (섹션 6·7·9 겨냥)"
  ],
  "findings": [
    {
      "id": "f1",
      "claim": "ASAM OpenSCENARIO XML 1.4.0 문서의 하위 호환성 절은 판 사이 호환 여부를 판마다 선언한다: 1.4.0 은 1.3.1 과, 1.3.1 은 1.3.0 과 완전히 호환되고, 1.2.0 은 1.1.1·1.0.0 과 호환되지만, 1.3.0 은 의미상 잘못된 시나리오를 허용하던 스키마 오류를 고쳐 1.2.0 과 완전히 호환되지 않는다.",
      "tag": "사실",
      "source_ids": [
        "ref-1511"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "1.4.0 은 'fully backwards compatible with v1.3.1'. 1.3.0 은 XSD 스키마 오류 수정과 위치·방향 계산 정정으로 1.2.0 과 완전 호환이 아니다. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f2",
      "claim": "ASAM OpenSCENARIO XML 은 1.2.0 시나리오 파일을 1.3.0 으로 옮기는 XSLT 이전 스크립트를 제공하고 스크립트가 경고를 내면 원래부터 잘못된 시나리오이므로 사람이 고치게 하며, 모든 판에 폐기 요소를 뺀 엄격 스키마를 두어 폐기 요소를 찾아 바꾸게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1511"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "1.2.0→1.3.0 XSLT 이전 스크립트, 경고 시 수동 수정. 판마다 폐기 요소 없는 strict schema 제공. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f3",
      "claim": "확인한 도로 교통 시나리오 표준에는 개별 시나리오 파일을 형식 판 사이에서 옮기는 규칙(판별 호환 선언, 이전 스크립트, 엄격 스키마 검사)이 공개되어 있으므로, 33. 시나리오 모델·편집 페이지 9절의 '개별 시나리오 인스턴스의 버전 관리 방식은 공개 자료에서 찾지 못했다'는 서술은 도로 교통 분야에 한해 고쳐야 하며 로봇 시뮬레이션 형식의 같은 규칙은 여전히 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1511",
        "ref-1088"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f1·f2 의 OpenSCENARIO XML 판 이전 규칙을 이전 실행(2026-09-30-12)의 '인스턴스 버전 관리 방식 미확인' 판단과 대조했다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f4",
      "claim": "Ortega·Wiest·Pasch·Hochgeschwender(arXiv 2605.29973, ERAS 2026 채택)가 확장한 시험 틀 RoboVAST 는 환경을 FloorPlan 모델(.fpm), 과제를 OpenSCENARIO DSL 의 추상 시나리오, 시작·목표 자세·장애물 수·센서 잡음·설정 파일을 변형 파일(.vast)로 나누고, 각 인스턴스를 모든 값이 정해진 구체 시험 구성(scenario.config)으로 해석한 뒤 실행마다 해석된 매개변수·rosbag·시각·합격 여부·결정적 실행 식별자를 남긴다.",
      "tag": "사실",
      "source_ids": [
        "ref-1515"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "환경(.fpm)→메시·점유 격자, 추상 시나리오(OpenSCENARIO DSL), 변형(.vast)→구체 구성(scenario.config). 실행별 rosbag, Nav2 결과(test.xml), metadata.yaml, 경로에서 만든 결정적 실행 id.",
      "as_of": "2026-05-29",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f5",
      "claim": "같은 연구는 시험 산출물 사이의 관계를 W3C PROV(PROV-O)를 핵심 메타모델로 DCAT·Dublin Core·QUDT 와 함께 JSON-LD 로 기록해 SPARQL 로 질의하게 했으며, 저자들은 이 메타모델이 일반화하기 어려울 수 있고 로봇 분야 공동 어휘가 없다고 한계를 밝혔다.",
      "tag": "사실",
      "source_ids": [
        "ref-1515"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "PROV-O 중심, JSON-LD 직렬화. 저자 한계: 메타모델이 'may be hard to generalize', 로봇 분야 통제 어휘 부재.",
      "as_of": "2026-05-29",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f6",
      "claim": "RoboVAST 처럼 환경 모델·추상 시나리오·변형을 나누고 인스턴스를 구체 구성으로 해석해 출처 기록과 함께 남기는 방식은, 형식 판 이전 규칙과 별개로 개별 시나리오 인스턴스를 식별·재현하는 근거가 되어 oq-234 에 부분 답이 될 것으로 보이나, 단일 로봇 주행 시험 기준이라 다중 플릿·설비 시나리오에 맞는지는 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-1515"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f4·f5 의 실행별 구체 구성·출처 기록을 oq-234(인스턴스 버전 관리)와 대조. 평가 대상은 이동로봇 주행 데이터셋이다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f7",
      "claim": "Pasch·Mirus·Zhang·Scholl(Intel Labs, arXiv 2409.07080)의 Scenario Execution for Robotics 는 ASAM OpenSCENARIO 2 로 쓴 로봇 시나리오를 구문 분석해 행동 트리(PyTrees)로 바꿔 실행하는 백엔드·미들웨어 독립 파이썬 라이브러리이며, Gazebo·Nav2·PyBullet 라이브러리를 두고 매개변수 값 목록을 조합마다 하나의 실행 시나리오로 펼친다.",
      "tag": "사실",
      "source_ids": [
        "ref-1512"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "OpenSCENARIO 2 → ANTLR4 구문 분석 → PyTrees 행동 트리. 매개변수 8개 값 × 8개 값으로 64개 시나리오 생성 예.",
      "as_of": "2024-09-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f8",
      "claim": "Scenario Execution for Robotics 의 저자들은 시뮬레이션과 실물 실험에서 위치 데이터만 바꾼 같은 시나리오 파일을 썼다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1512"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Turtlebot4 두 대의 시뮬레이션–실물 시험에서 'use the exact same scenario description file'(위치 데이터 제외).",
      "as_of": "2024-09-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f9",
      "claim": "같은 연구는 2D 라이다 스캔에 가우시안 잡음을 더하거나 검출을 무작위로 빼는 ROS 2 노드로 장애를 주입하고 잡음 크기와 누락 비율을 시나리오 매개변수로 두었으며, 장애 수준이 높아질수록 AMCL 위치추정 오차가 커지는 것을 기능 시연으로 보였다.",
      "tag": "사실",
      "source_ids": [
        "ref-1512"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "잡음 표준편차 0.1·0.2·0.5 로 변화. 저자는 위치추정 성능 평가가 아니라 기능 시연이라고 밝힘.",
      "as_of": "2024-09-11",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f10",
      "claim": "자율주행 분야의 시나리오 기술 언어 OpenSCENARIO 2 가 이동로봇 주행 시나리오 기술(Scenario Execution for Robotics, RoboVAST)에 다시 쓰이고 있으므로, 이 영역 9절에서 연계 대상으로만 둔 도로 교통 시나리오 표준이 로봇 시나리오의 과제·사건 기술 언어 후보가 될 수 있어 oq-233 의 '기존 형식 조합' 쪽에 부분 근거가 될 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1512",
        "ref-1515",
        "ref-1088"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "두 연구는 저자(Pasch)가 겹쳐 독립 출처가 아니다. 다중 로봇 플릿·승강기·문 사건 표현 여부는 확인하지 못함.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f11",
      "claim": "ros2_fault_injection 은 ROS 2 의 토픽·변환(TF)·서비스에 장애를 주입하는 프레임워크로, 오도메트리·LaserScan·관절 상태·IMU·TF·속도 명령·트리거 서비스·점군 장애 유형과 시나리오 실행 중 기대 결과를 확인하는 단언(assertion)을 두고 pluginlib 로 새 주입기를 더하게 한다.",
      "tag": "사실",
      "source_ids": [
        "ref-1518"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "'A ROS 2 framework for injecting faults into topics, transforms, and services.' 관리 주체·판·발행일은 문서 첫 페이지에 없음. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f12",
      "claim": "확인한 장애 주입 선언은 ARIAC 의 설비·도구 장애(시작 시각·지속 시간·발생 횟수 매개변수), Scenario Execution 의 센서 잡음 매개변수, ros2_fault_injection 의 메시지 단위 장애로 나뉘며, 여러 제조사 로봇 플릿과 승강기·문 같은 설비 장애를 한 형식으로 선언하는 사례는 이번에도 찾지 못해 oq-235 는 열린 채로 남는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-528",
        "ref-1512",
        "ref-1518"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "ARIAC 장애 4종은 START_TIME·DURATION·TESTER·GRASP_OCCURRENCE 매개변수로 선언(원문 확인). 나머지 둘은 센서·메시지 수준이다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f13",
      "claim": "Ortega·Parra·Schneider·Hochgeschwender(Frontiers in Robotics and AI, 2024-08)는 도메인 전문가 14명 면담에서 환경 모델과 로봇 과제를 묶은 시험 시나리오의 변형 관리가 이동로봇 시뮬레이션 시험을 꺼리는 주요 장벽으로 나타났다고 보고했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1516"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "면담 14명. 기존 CAD·3D 모델링 도구는 시험 목적에 따라 바뀌어야 하는 장면에 맞지 않는다고 지적.",
      "as_of": "2024-08-02",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f14",
      "claim": "같은 연구는 기존 모델을 고치지 않고 동적 문·다른 과제 명세 같은 의미를 덧붙이는 조합형 실행 시나리오를 제안해 점유 격자 지도·3D 메시·Gazebo 월드·주행 경유점을 생성했고, 정적 시험·무작위로 움직이는 문·로봇이 다가오면 닫히는 문의 세 시나리오로 공개 주행 스택에서 1년 넘게 드러나지 않은 설정 오류를 찾았다.",
      "tag": "사실",
      "source_ids": [
        "ref-1516"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "환경 모델은 FloorPlan DSL 기반, 동적 문은 시간 또는 로봇 접근 거리로 작동하는 Gazebo 플러그인. 모델 재사용 확인.",
      "as_of": "2024-08-02",
      "site_type": null,
      "flow_item": "예외·성과"
    },
    {
      "id": "f15",
      "claim": "Open-RMF 의 Site Editor(rmf_site)는 Rust 와 Bevy 게임 엔진으로 만든 대규모 RMF 배치 현장 시각화·편집 도구로 데스크톱과 웹(WebAssembly)에서 돌며, rmf_site_ros2 의 rmf_site_cmake 가 Site Editor 프로젝트에서 시뮬레이션과 주행 그래프를 생성한다.",
      "tag": "사실",
      "source_ids": [
        "ref-482"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "'an experimental approach to visualizing and editing large RMF deployment sites'. 웹 판은 저장·불러오기 없이 JSON 내려받기만 지원. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f16",
      "claim": "Open-RMF 상호운용 그룹 공지(2024-06-05)는 Site Editor 를 예전 traffic-editor 를 대체하는 도구로 소개하고, 시각화·시뮬레이션용 3D 환경, 환경 안의 로봇, 로봇 교통 규칙, 승강기와 문을 편집 대상으로 들었다.",
      "tag": "사실",
      "source_ids": [
        "ref-1510"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "Site Editor 는 'a replacement for the old traffic editor'. Bevy 기반이라 하위 사용자가 확장 가능.",
      "as_of": "2024-06-05",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f17",
      "claim": "traffic-editor 문서는 편집기의 목표를 여러 플릿의 의도를 제조사 중립 방식으로 표현하고 실제 환경을 반영한 3D 시뮬레이션 월드를 생성하는 것으로 밝히면서, 다음 판은 영상 좌표 대신 데카르트 좌표나 위경도 좌표를 기본으로 하려 하나 일정은 정해지지 않았다고 적는다.",
      "tag": "사실",
      "source_ids": [
        "ref-079"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "현행 주석은 바탕 평면도 영상의 픽셀 좌표(+Y 아래)이며 지도 생성 단계에서 축을 뒤집는다. 다음 판 일정은 'not a hard schedule'. (발행일 미확인, 확인일 기준)",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f18",
      "claim": "Open-RMF 의 시설 주석 편집기가 traffic-editor(.building.yaml)에서 Site Editor 로 넘어가고 있으므로, ROP 시나리오 모델이 건물 파일을 환경 참조로 묶는다면 편집기·건물 형식 전환에 따른 참조 이전 규칙이 함께 필요할 것으로 보이며, 기존 .building.yaml 을 Site Editor 형식으로 옮기는 공식 방법은 이번에 확인하지 못했다.",
      "tag": "추정",
      "source_ids": [
        "ref-482",
        "ref-1510",
        "ref-079"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f15·f16·f17 종합. 세 출처 모두 Open-RMF 쪽 자료라 독립 확인이 아니다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f19",
      "claim": "Jiang·Zhang·Veerapaneni·Li(SoCS 2024)에 따르면 Amazon Robotics 가 후원한 2023 League of Robot Runners 지속형 다중 에이전트 경로 찾기 경진대회는 Warehouse(140×500, 정점 38,586개, 에이전트 8,000)와 Sortation(140×500, 정점 54,320개, 에이전트 10,000) 지도를 포함한 시나리오로 단계당 1초 계획 제한 아래 처리량을 겨뤘으며, 이는 실제 물류창고 배치가 아니라 경진대회 벤치마크다.",
      "tag": "사실",
      "source_ids": [
        "ref-1514"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "지도: Random·City·Game·Warehouse·Sortation. 목표는 단계당 평균 도달 목표 수(처리량). 지도는 미리 주어지고 30분 전처리.",
      "as_of": "2024-04-24",
      "site_type": "물류창고",
      "flow_item": "작업 대상"
    },
    {
      "id": "f20",
      "claim": "같은 경진대회에서는 외부 작업 배정기가 에이전트가 현재 목표에 도달할 때마다 새 목표를 정확히 하나씩 주는 방식으로 작업이 생긴다.",
      "tag": "사실",
      "source_ids": [
        "ref-1514"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "'assigns exactly one new goal to an agent if the agent reaches its current one'. 작업 분포는 균일 표본 추출로 가정되는 경우가 많다고 적음.",
      "as_of": "2024-04-24",
      "site_type": "물류창고",
      "flow_item": "시작 조건"
    },
    {
      "id": "f21",
      "claim": "NVIDIA 는 Isaac Sim 의 Warehouse Creator 확장이 2D 격자 배치를 Modular Warehouse 자산 묶음의 USD 창고로 바꾸는 대화형 배치 편집기이며 바닥·벽·기둥 같은 건물 구조만 생성한다고 설명한다.",
      "tag": "추정",
      "source_ids": [
        "ref-1517"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "벤더 주장: 'an interactive plan builder that converts a 2D grid layout into a USD warehouse'. omni.warehouse.creator.api/ui 두 확장. 로봇·랙·작업 배치 언급 없음(페이지 갱신 2026-09-18).",
      "as_of": "2026-09-18",
      "site_type": "물류창고",
      "flow_item": null,
      "vendor_claim": true
    },
    {
      "id": "f22",
      "claim": "Elmaaroufi 외의 ScenicNL(COLM 2024)은 여러 대규모 언어 모델 프롬프트를 컴파일러·시뮬레이터와 엮어, 세부가 불확실한 경찰 사고 보고서(최근 5년 캘리포니아 자율주행차 사고 보고)를 불확실성을 확률 분포로 담은 Scenic 시나리오 프로그램으로 바꿔 '만약 ~였다면' 시나리오를 탐색하게 했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1513"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "입력: 캘리포니아 자율주행차 사고 보고서. 출력: 확률적 Scenic 프로그램. 초록 기준(정량 결과는 미열람).",
      "as_of": "2024-10-02",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f23",
      "claim": "사고 기록 같은 서술형 기록을 확률적 시나리오 프로그램으로 바꾸는 방법은 도로 교통 분야에 있으나, 로봇 플릿의 실행 기록(작업·배정·위치·사건 시각)을 시나리오 사양으로 바꾸는 공개 형식이나 변환 규칙은 이번 조사에서도 찾지 못해 oq-131 은 열린 채로 남는 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1513",
        "ref-1086"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "ScenicNL 과 Scenic 3.0 은 자율 시스템 시나리오 언어이며 로봇 플릿 실행 기록 입력은 다루지 않는다.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f24",
      "claim": "레온 대학교 연구진(WAF 2025)은 공개 지리공간 데이터로 3D 시나리오를 만들어 주요 로봇 플랫폼에서 쓸 수 있는 시뮬레이션 모델을 생성하고 Gazebo·Unity 의 ROS 2 시스템과 연동하는 방법을 제안했다.",
      "tag": "사실",
      "source_ids": [
        "ref-1519"
      ],
      "cross_checked": false,
      "confidence": "medium",
      "evidence_excerpt": "'publicly available geospatial data'로 3D 시나리오 생성, 'simulationready models compatible with major robotics platforms'. 데이터셋 이름은 초록에 없음.",
      "as_of": "2025",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f25",
      "claim": "이번에 확인한 자료를 더하면 핵심 질문(현장·로봇·사람·작업을 담은 시나리오를 어떻게 표현하고 다시 쓸 것인가)에 대해, 로봇 쪽에서도 환경 모델·추상 시나리오·변형을 나누고 구체 인스턴스를 해석·기록하는 도구와 자율주행 시나리오 언어의 재사용이 나타나지만, 환경·로봇·사람·물품·작업·정책·물리·장애를 한 형식으로 담는 공통 표준은 여전히 확인하지 못한 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1515",
        "ref-1512",
        "ref-1516",
        "ref-116"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f4·f7·f14 와 미션 기술 형식에 표준이 없다는 기존 근거(ref-116)를 종합.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    },
    {
      "id": "f26",
      "claim": "연계 대상: OpenSCENARIO XML 의 판 이전 스크립트나 Open-RMF 편집기 전환 같은 외부 시나리오·건물 형식의 판 규칙은 각 형식 관리 주체의 몫이며, ROP 는 자기 시나리오 모델의 판 규칙과 참조하는 외부 형식 판의 대응을 맡을 것으로 보인다.",
      "tag": "추정",
      "source_ids": [
        "ref-1511",
        "ref-482"
      ],
      "cross_checked": false,
      "confidence": "low",
      "evidence_excerpt": "f2·f15 를 분류 원문 19장 경계(이종 제조사를 잇는 ROP 는 인터페이스와 실행 보장을 맡음)에 맞춰 정리.",
      "as_of": "2026-10-09",
      "site_type": null,
      "flow_item": null
    }
  ],
  "sources": [
    {
      "id": "ref-079",
      "org": "Open Robotics",
      "title": "Traffic Editor - Programming Multiple Robots with ROS 2",
      "published": null,
      "url": "https://osrf.github.io/ros2multirobotbook/traffic-editor.html",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "Open-RMF traffic-editor GUI 설명. 층·벽·문·승강기·차선·웨이포인트 속성 주석과 .building.yaml 저장, 시뮬레이션 월드 생성, 좌표계와 다음 판 계획.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/osrf/ros2multirobotbook/master/src/traffic-editor.md",
      "source_unopened": false
    },
    {
      "id": "ref-528",
      "org": "NIST (usnistgov/ARIAC_docs)",
      "title": "ARIAC 2025 Documentation — Challenges",
      "published": null,
      "url": "https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html",
      "type": "정부·연구기관",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "ARIAC 민첩성 과제 4종(컨베이어·전압 시험기·진공 도구 고장, 긴급 주문)과 매개변수(START_TIME·DURATION·TESTER·TOOL·GRASP_OCCURRENCE·ID).",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/usnistgov/ARIAC_docs/main/docs/pages/challenges.rst",
      "source_unopened": false
    },
    {
      "id": "ref-1088",
      "org": "ASAM e.V.",
      "title": "ASAM OpenSCENARIO® XML",
      "published": null,
      "url": "https://www.asam.net/standards/detail/openscenario-xml/",
      "type": "표준",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 주행·교통 시뮬레이터의 동적 내용을 XML 로 기술하는 표준의 공식 소개 페이지(이번 실행에서 다시 열지 않음).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-1086",
      "org": "Vin, E., Kashiwa, S., Rhea, M., Fremont, D. J., Kim, E., Dreossi, T., Ghosh, S., Yue, X., Sangiovanni-Vincentelli, A. L., & Seshia, S. A. (CAV 2023, arXiv)",
      "title": "3D Environment Modeling for Falsification and Beyond with Scenic 3.0",
      "published": "2023-07",
      "url": "https://arxiv.org/abs/2307.03325",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 확률적 시나리오 언어 Scenic 3.0 의 3차원 환경 모델링과 반증 기반 시험(이번 실행에서 다시 열지 않음).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-116",
      "org": "Filippone, G., Pettinari, S., & Pelliccione, P.",
      "title": "Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis",
      "published": "2026-03",
      "url": "https://arxiv.org/abs/2603.15427",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "원문 미열람. 행동 트리·상태 기계·HTN·BPMN 미션 기술 형식 비교, 미션 명세 표준 부재 지적(이번 실행에서 다시 열지 않음).",
      "fetched": false,
      "fetched_via": null,
      "fetch_url": null,
      "source_unopened": true
    },
    {
      "id": "ref-482",
      "org": "Open-RMF (open-rmf/rmf_site)",
      "title": "rmf_site — RMF Site Editor (README)",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_site",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "Rust·Bevy 기반 RMF 배치 현장 시각화·편집 도구 Site Editor 의 README. 데스크톱·웹 빌드, rmf_site_ros2 로 시뮬레이션·주행 그래프 생성.",
      "fetched": true,
      "fetched_via": "github_raw",
      "fetch_url": "https://raw.githubusercontent.com/open-rmf/rmf_site/main/README.md",
      "source_unopened": false
    },
    {
      "id": "ref-1510",
      "org": "Open Robotics Discourse (Open-RMF 상호운용 그룹, 작성자 grey)",
      "title": "Interoperability Interest Group June 6, 2024: Preview of the RMF Site Editor",
      "published": "2024-06-05",
      "url": "https://discourse.openrobotics.org/t/interoperability-interest-group-june-6-2024-preview-of-the-rmf-site-editor/38070",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "Site Editor 를 예전 traffic-editor 의 대체 도구로 소개하고 편집 대상(3D 환경·로봇·교통 규칙·승강기·문)과 Bevy 기반 확장성을 설명한 공지.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1511",
      "org": "ASAM e.V.",
      "title": "ASAM OpenSCENARIO XML v1.4.0 — 5 Backward compatibility",
      "published": null,
      "url": "https://openscenario.asam.net/ASAM_OpenSCENARIO_XML/v1.4.0/05_backward_compatibility/01_backward_compatibility.html",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "OpenSCENARIO XML 판 사이 하위 호환성 선언, 1.2.0→1.3.0 XSLT 이전 스크립트, 폐기 요소 없는 엄격 스키마를 설명하는 공식 문서 절.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1512",
      "org": "Pasch, F., Mirus, F., Zhang, Y., & Scholl, K.-U. (Intel Labs, arXiv)",
      "title": "Scenario Execution for Robotics: A generic, backend-agnostic library for running reproducible robotics experiments and tests",
      "published": "2024-09-11",
      "url": "https://arxiv.org/abs/2409.07080",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "OpenSCENARIO 2 로 쓴 로봇 시나리오를 행동 트리로 바꿔 실행하는 라이브러리. 매개변수 변형, 라이다 장애 주입, 시뮬레이션–실물 같은 시나리오 파일 사용(프리프린트, 본문 HTML 확인).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2409.07080v1",
      "source_unopened": false
    },
    {
      "id": "ref-1513",
      "org": "Elmaaroufi, K., Shanker, D., Cismaru, A., Vazquez-Chanlatte, M., Sangiovanni-Vincentelli, A., Zaharia, M., & Seshia, S. A. (COLM 2024, arXiv)",
      "title": "ScenicNL: Generating Probabilistic Scenario Programs from Crash Reports",
      "published": "2024-05-03",
      "url": "https://arxiv.org/abs/2405.03709",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "대규모 언어 모델·컴파일러·시뮬레이터를 엮어 경찰 사고 보고서를 확률적 Scenic 시나리오 프로그램으로 바꾸는 연구(초록 페이지 기준, 최종 수정 2024-10-02).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1514",
      "org": "Jiang, H., Zhang, Y., Veerapaneni, R., & Li, J. (SoCS 2024, arXiv)",
      "title": "Scaling Lifelong Multi-Agent Path Finding to More Realistic Settings: Research Challenges and Opportunities",
      "published": "2024-04-24",
      "url": "https://arxiv.org/abs/2404.16162",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "2023 League of Robot Runners 우승 방법과 연구 과제. Warehouse·Sortation 등 경진대회 지도 규모, 목표 배정 방식, 단계당 1초 계획 제한을 기술(본문 HTML 확인).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2404.16162v1",
      "source_unopened": false
    },
    {
      "id": "ref-1515",
      "org": "Ortega, A., Wiest, S., Pasch, F., & Hochgeschwender, N. (arXiv, ERAS 2026 채택)",
      "title": "Replicable Simulation-Based Robot Validation through Provenance",
      "published": "2026-05-28",
      "url": "https://arxiv.org/abs/2605.29973",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "RoboVAST 시험 틀에 W3C PROV 기반 출처 기록과 FAIR 메타데이터를 더해 시뮬레이션 시험의 재현성을 높이는 연구. 환경·추상 시나리오·변형 분리와 구체 구성 해석(본문 HTML v2 확인).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": "https://arxiv.org/html/2605.29973v2",
      "source_unopened": false
    },
    {
      "id": "ref-1516",
      "org": "Ortega, A., Parra, S., Schneider, S., & Hochgeschwender, N. (Frontiers in Robotics and AI 11)",
      "title": "Composable and executable scenarios for simulation-based testing of mobile robots",
      "published": "2024-08-02",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11327003/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "전문가 14명 면담으로 시나리오 변형 관리의 어려움을 확인하고, FloorPlan DSL 기반 조합형 실행 시나리오로 Gazebo 월드·지도·경유점을 생성해 주행 스택 설정 오류를 찾은 연구.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1517",
      "org": "NVIDIA",
      "title": "Isaac Sim Documentation — Warehouse Creator Extension",
      "published": null,
      "url": "https://docs.isaacsim.omniverse.nvidia.com/latest/assets/asset_utilities/ext_omni_warehouse_creator.html",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "2D 격자 배치를 USD 창고 건물 구조로 생성하는 Isaac Sim 확장(omni.warehouse.creator.api/ui) 문서. 페이지 갱신 2026-09-18.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1518",
      "org": "ros2_fault_injection 프로젝트 (Read the Docs)",
      "title": "ros2_fault_injection documentation",
      "published": null,
      "url": "https://ros2-fault-injection.readthedocs.io/",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "ROS 2 토픽·TF·서비스 장애 주입 프레임워크 문서 첫 페이지. 장애 유형 목록, 단언, pluginlib 확장 구조. 관리 주체·판 미표기.",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    },
    {
      "id": "ref-1519",
      "org": "Sánchez de la Fuente, S., Prieto López, L., González Santamarta, M. Á., Matellán Olivera, V. 외 (Universidad de León, WAF 2025)",
      "title": "Scenario Generation for Robot Simulation from Public Data",
      "published": "2025",
      "url": "https://portalcientifico.unileon.es/documentos/6972798ce66b2902147b1aeb",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "공개 지리공간 데이터로 로봇 시뮬레이션용 3D 시나리오를 생성해 Gazebo·Unity 의 ROS 2 시스템과 연동하는 방법(학회 논문집 초록 기준).",
      "fetched": true,
      "fetched_via": "webfetch",
      "fetch_url": null,
      "source_unopened": false
    }
  ],
  "page_proposals": [
    {
      "action": "update",
      "path": "docs/categories/design-and-simulation/scenario-model-and-editing.md",
      "sections": [
        "3",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "11"
      ],
      "rationale": "갱신(차등): 섹션 3 — f13(전문가 면담 근거)으로 종합 추정 보강 / 섹션 5 — 물류창고 사례 추가: f19(Warehouse·Sortation 지도, 작업 대상)·f20(목표 배정, 시작 조건), 경진대회 벤치마크이지 실제 현장이 아님을 밝힘. f21 은 편집 도구로 [추정]+'벤더 주장' 병기. '물류창고 사례를 찾지 못했다' 문장 교체, 국내 자료는 여전히 없음 / 섹션 6·7 — f15·f16·f17·f18(traffic-editor→Site Editor 전환, 바뀐 출처), f7·f8·f9(OpenSCENARIO 2 를 쓰는 로봇 시나리오 실행 라이브러리), f11(ros2_fault_injection), f4·f5(RoboVAST), f24(공개 데이터 기반 생성). 6·7절 본문은 주제 페이지로 분리되어 있으므로 요약 문장과 주제 페이지 갱신을 함께 제안 / 섹션 8 — f13·f14·f22·f4 대표 연구 추가 / 섹션 9 — '개별 시나리오 인스턴스 버전 관리 방식을 찾지 못했다' 문장을 f1·f2·f3(도로 교통 표준의 판 이전 규칙)·f6(인스턴스 해석·출처 기록)로 정정하고 f26(연계 대상: 외부 형식 판 규칙) 추가, f10 으로 OpenSCENARIO 를 '참조 설계'만이 아니라 로봇 시나리오 기술 후보로도 서술 / 섹션 10 — 54. 시험·형식 검증·벤치마크(f4·f9·f14), 57. 자산·소프트웨어 수명주기 관리(f1·f2·f6), 61. 물류창고(f19·f20), 27. 다중 로봇 경로·교통 관리 — MAPF(f19), 11. 채팅으로 실제 상황 시뮬레이션 재현·36. 가상 시운전·실제 상황 재현(f22·f23) 연결 추가, related_areas 에 57·61 추가 제안 / 섹션 11 — oq-234 부분 근거(f3·f6), oq-235 미해결(f12), oq-131 미해결(f23), oq-233 부분 근거(f10·f18), oq-236 미해결(국내 자료 없음), 새 질문 3건. 다음 실행 후보: docs/topics/2026/2026-09-30-area33-s7.md 표에 Site Editor·Scenario Execution·RoboVAST·ros2_fault_injection·League of Robot Runners 행 추가."
    }
  ],
  "glossary_candidates": [
    {
      "term_ko": "데이터 출처 추적",
      "term_en": "Data Provenance (W3C PROV)",
      "definition": "어떤 산출물이 어떤 입력·설정·실행·주체로부터 만들어졌는지를 기계가 읽을 수 있는 관계로 기록하는 일로, W3C PROV 가 그 표준 데이터 모델이며 시뮬레이션 시험의 재현성 확보에 쓰인다."
    },
    {
      "term_ko": "추상 시나리오·구체 시나리오",
      "term_en": "Abstract Scenario / Concrete Scenario",
      "definition": "매개변수와 변형 범위만 정한 시나리오(추상)와 모든 값이 하나로 정해져 바로 실행할 수 있는 시나리오 인스턴스(구체)를 구분하는 말로, 시험 도구가 추상 시나리오를 여러 구체 시나리오로 펼쳐 실행한다."
    },
    {
      "term_ko": "엄격 스키마",
      "term_en": "Strict Schema (deprecated elements removed)",
      "definition": "형식의 판에서 폐기 예정 요소를 뺀 검증용 스키마로, 기존 시나리오 파일을 이 스키마로 검사해 다음 판에서 사라질 요소를 찾아 바꾸게 한다(ASAM OpenSCENARIO XML)."
    }
  ],
  "open_questions_new": [
    "RoboVAST 처럼 추상 시나리오를 구체 인스턴스로 해석하고 실행마다 출처를 기록하는 방식을 여러 제조사 로봇 플릿과 승강기·문 같은 설비가 함께 있는 다중 로봇 시나리오에 적용한 사례가 있는가? | 관련 영역: 33. 시나리오 모델·편집, 54. 시험·형식 검증·벤치마크 | 근거: f6 | 종류: 일반",
    "Open-RMF Site Editor 의 현장 형식이 기존 traffic-editor 의 .building.yaml 을 대체하는가, 그리고 기존 건물 파일을 옮기는 공식 변환 도구나 판 이전 규칙이 있는가? | 관련 영역: 33. 시나리오 모델·편집, 15. 지도·공간·위치 모델 | 근거: f18 | 종류: 일반",
    "OpenSCENARIO 2 DSL 로 다중 로봇 플릿의 작업 배정과 승강기·문 같은 설비 사건을 기술할 수 있는가, 기술하려면 어떤 확장 라이브러리가 필요한가? | 관련 영역: 33. 시나리오 모델·편집, 22. 설비·건물 시스템 연동 | 근거: f10 | 종류: 일반"
  ],
  "open_questions_resolved": [],
  "self_check": {
    "source_count": 16,
    "cross_checked_count": 0,
    "unverified": [
      "oq-234 부분 답: 도로 교통 표준(OpenSCENARIO XML)의 판 이전 규칙과 RoboVAST 인스턴스 해석은 확인했으나, 로봇 시뮬레이션 형식(SDFormat·Open-RMF 건물 파일)의 시나리오 판 이전 규칙은 확인하지 못함. SDFormat 변환 규칙 파일(1_10.convert)은 열었으나 내용이 비어 근거로 쓰지 않음",
      "oq-235 미해결: 여러 제조사 플릿과 설비 장애를 함께 선언하는 형식 없음",
      "oq-131 미해결: 로봇 플릿 실행 기록을 시나리오로 바꾸는 공개 형식 없음(자율주행 쪽 MathWorks Scenario Builder·특허는 벤더·특허 자료라 근거로 쓰지 않음)",
      "oq-236 미해결: 국내 다중 로봇 시나리오 예제 라이브러리를 찾지 못함(한국어 검색 4회)",
      "oq-135 이번 실행에서 조사하지 못함",
      "f19·f20 League of Robot Runners 공식 사이트·2024 대회 자료는 열지 않고 우승 팀 논문 기준",
      "ref-1518 관리 주체·판·발행일 미확인",
      "ref-1511 문서 절의 발행일 미확인(1.4.0 판 공개일은 이전 실행에서 2026-05-19 로 확인됨)",
      "f21 Isaac Sim Warehouse Creator 기능은 벤더 문서뿐이며 독립 확인하지 못함",
      "Scenario Execution 공식 저장소 README 는 403/404 로 열지 못해 논문 본문으로 대신함",
      "f10 의 두 출처는 공동 저자가 겹쳐 독립 출처가 아님"
    ],
    "scope_violations": [
      "f9·f11·f12: 센서·메시지 장애 주입과 위치추정 성능은 로봇 자체 지능·제어 경계의 내용이라, 시나리오에 장애를 선언하는 방식의 근거로만 씀",
      "f21: 3D 창고 건물 자산 생성은 시뮬레이터·벤더 쪽 연계 대상이며 시나리오 환경 참조의 사례로만 제안",
      "f22·f23: 도로 교통 사고 보고 기반 생성은 자율주행 분야 내용이라 로봇 플릿 재현의 참고 사례로만 씀",
      "f26: 외부 형식 판 규칙은 형식 관리 주체 몫이므로 claim 을 '연계 대상: '으로 시작"
    ],
    "budget_used": {
      "queries": 19,
      "sources": 11
    },
    "limits": "web_fetch_available: true · fetch_mode full. 갱신(update) 실행이며 정정 요청·발행 2년 지난 표준이 없어 빈·약한 절(5절 물류창고·국내 사례, 9절 판 관리 문장, 6·7절 편집기 전환)과 열린 질문 oq-131·oq-233·oq-234·oq-235·oq-236 만 조사했다. 검색 19회/30, 신규 출처 11건/15(ref-482~ref-1519, 예약 구간 안), 모두 원문 페이지를 열었다(webfetch 10, github_raw 1). 재사용 5건 가운데 ref-079·ref-528 은 입력의 원문 텍스트(inbox)로 확인했고 ref-1088·ref-1086·ref-116 은 다시 열지 않았다(source_unopened). 교차 확인 0건: 새 근거가 모두 단일 출처라 신뢰도는 medium 이하다. 벤더 주장 1건(f21). 핵심 질문 답은 f25(추정)로 갱신했다. 현장 유형: 이번 새 사례는 물류창고(f19·f20 경진대회 벤치마크, f21 편집 도구)뿐이며 실제 물류창고 배치 사례와 국내 자료는 여전히 찾지 못했다. 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험)과 18. 실시간 세계 상태·데이터 일관성(현재 상태)을 섞지 않았고, 시나리오는 가정한 미래 실험의 입력으로만 다뤘다. 해결 제안한 열린 질문 없음(oq-234 는 부분 근거). 답한 트랙 질문 없음(트랙 실행 아님). 입력 누락 없음. 우선 지정 질문 없음."
  }
}
```

### runs/2026-10-09-13/verification.json

```json
{
  "run_id": "2026-10-09-13",
  "stage": "first",
  "verdict": "조건부 승인",
  "claim_checks": [
    {
      "finding_id": "f1",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ref-1511 원문을 직접 열었다. 1.4.0↔1.3.1 완전 호환, 1.3.1↔1.3.0 완전 호환, 1.3.0 은 스키마 오류 수정(의미상 잘못된 시나리오 허용)과 위치·방향 계산 정정으로 1.2.0 과 완전 호환이 아니며, 1.2.0 은 1.1.1·1.0.0 과 호환된다는 내용이 모두 원문과 맞다. 문서 머리에 2026-05-08 표기가 있으나 발행일인지 분명하지 않다. 이전 실행은 1.4.0 공개일을 2026-05-19 로 적었다. 발행일은 미확인으로 두고 기준일은 확인일로 한다. 단일 출처다."
    },
    {
      "finding_id": "f2",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 원문에 1.2.0→1.3.0 XSLT 이전 스크립트가 있고, 경고가 나면 원래 의미상 잘못된 시나리오이므로 사람이 확인·수정해야 한다고 적혀 있다. 모든 판에 폐기 요소를 뺀 엄격 스키마를 둔다는 내용도 원문과 일치한다. 단일 출처다."
    },
    {
      "finding_id": "f3",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지: f1·f2 를 기존 9절 판단과 대조한 종합이다. ref-1088 은 이번 실행에서 다시 열지 않았고 참고문헌 목록 등재로 실재를 확인했다(원문 미열람). '도로 교통 분야에 한정한 정정'이라는 범위는 적절하다."
    },
    {
      "finding_id": "f4",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: arXiv HTML v2 에서 .fpm 환경 모델→메시·점유 격자, OpenSCENARIO DSL 추상 시나리오, .vast 변형 파일, scenario.config 구체 구성, 실행별 rosbag·test.xml·metadata.yaml, 경로에서 만든 결정적 실행 id 를 확인했다. 초록 페이지 Comments 에 ERAS 2026 채택이 적혀 있다. v1 은 2026-05-28, v2 는 2026-05-29 이다. 단일 출처다."
    },
    {
      "finding_id": "f5",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: PROV-O 를 핵심으로 DCAT·Dublin Core·QUDT 를 함께 쓰고 JSON-LD 로 직렬화해 SPARQL 로 질의한다. 저자가 밝힌 한계('may be hard to generalize', 로봇 분야 통제 어휘 부재)도 원문과 일치한다."
    },
    {
      "finding_id": "f6",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지: 단일 로봇 주행 시험 기준이라는 한계를 밝혔고, oq-234 에는 부분 근거로만 쓴다. 해결 판정은 하지 않는다."
    },
    {
      "finding_id": "f7",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: ANTLR4 구문 분석→PyTrees 행동 트리, 백엔드 독립 파이썬 라이브러리, Nav2·Gazebo·PyBullet 사용, 8×8=64 구체 시나리오를 원문에서 확인했다. 다만 Zhang, Y. 의 소속은 Intel Labs 가 아니라 카를스루에 응용과학대·KIT 이므로 '(Intel Labs)' 표기를 고치게 한다."
    },
    {
      "finding_id": "f8",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 위치 데이터(초기 자세·기준점·주행 목표)를 빼면 시뮬레이션과 실물 실험에 'exact same scenario description file'을 썼다는 서술이 원문에 있다."
    },
    {
      "finding_id": "f9",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 가우시안 잡음·검출 무작위 누락, 표준편차 0.1·0.2·0.5, 장애가 늘수록 위치추정 품질 저하, '심층 평가가 아닌 기능 시연'이라는 저자 진술이 모두 원문에 있다. 센서 수준 장애는 로봇 자체 지능·제어 경계의 내용이므로 시나리오 장애 선언 방식의 근거로만 쓴다."
    },
    {
      "finding_id": "f10",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지: ref-1512·ref-1515 는 공동 저자(Pasch)가 겹쳐 독립 출처가 아니다. ref-1088 은 원문 미열람이다. 외부 표준(ASAM 관리)은 연계 대상이라는 범위를 유지해야 한다."
    },
    {
      "finding_id": "f11",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "부분 확인(2회 열람): 소개 문구('A ROS 2 framework for injecting faults into topics, transforms, and services.')와 장애 유형 목록(Odometry·LaserScan·Joint State·IMU·TF·Twist·Trigger Service·Point Cloud)은 확인했다. 단언(Assertions·Assertion Events)과 'Injector Factory and Pluginlib' 절은 목차 수준에서만 보였다. '시나리오 실행 중 기대 결과를 확인한다', 'pluginlib 로 새 주입기를 더한다'는 기능 설명은 첫 페이지 본문에 없어 표현을 좁히게 한다. 관리 주체·판·발행일은 미표기다."
    },
    {
      "finding_id": "f12",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지: ARIAC 매개변수는 입력 원문(ref-528 원문 텍스트)으로 확인했다. 다중 제조사·설비 장애 형식을 찾지 못했다는 결론이며 oq-235 는 열린 채로 둔다."
    },
    {
      "finding_id": "f13",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: PMC 본문에서 전문가 14명 면담과, 시나리오 변이 관리가 'a major barrier'라는 서술, CAD·3D 모델링 도구가 맞지 않는다는 지적을 확인했다. Frontiers in Robotics and AI 11권, 2024-08-02 이다. 대상은 이동로봇 시뮬레이션 시험 일반이며 ROP 실무자 면담이 아니다."
    },
    {
      "finding_id": "f14",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 기존 모델을 고치지 않고 의미를 더하는 조합형 시나리오이며, 점유 격자 지도·3D 메시·Gazebo 월드(SDF)·YAML 경유점을 만든다. 정적 문·무작위 문·접근 시 닫히는 문의 세 시나리오로, 1년 넘게 드러나지 않은 공개 주행 스택의 설정 오류를 찾았다. 본문 앞 100,000자를 기준으로 확인했다."
    },
    {
      "finding_id": "f15",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: rmf_site README(raw)에 'experimental approach to visualizing and editing large RMF deployment sites'라는 서술, Rust·Bevy 사용, 데스크톱·웹 지원, rmf_site_ros2 의 rmf_site_cmake 로 시뮬레이션·주행 그래프를 생성한다는 내용, 웹 판은 저장·불러오기가 없고 JSON 내보내기만 된다는 내용이 있다."
    },
    {
      "finding_id": "f16",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 2024-06-05 grey 작성 공지에 'foremost a replacement for the old traffic editor'라는 서술과 편집 대상 다섯 가지(3D 환경·로봇·교통 규칙·승강기·문), Bevy 기반 확장성이 있다. ref-482 와 같은 Open-RMF 쪽 자료라 독립 확인은 아니다."
    },
    {
      "finding_id": "f17",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 입력 원문(data/source_texts/ref-079.txt)에 제조사 중립 표현 목표, 3D 시뮬레이션 월드 생성이라는 부차 목표, 다음 판이 데카르트·위경도 좌표를 기본으로 한다는 계획과 'not a hard schedule' 표기가 있다. 원문 자체에 작성 시점이 표기돼 있지 않다."
    },
    {
      "finding_id": "f18",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지: f15·f16·f17 의 종합이다. 세 출처 모두 Open-RMF 쪽이라 독립 확인이 아니며, .building.yaml 이전 방법이 미확인이라는 점을 적절히 남겼다."
    },
    {
      "finding_id": "f19",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: Amazon Robotics 후원, Warehouse 140×500·38,586 정점·8,000 에이전트, 단계당 1초 계획 제한, 처리량 목표, 30분 전처리를 원문에서 확인했다. 초록 페이지 Comments 에서 SoCS 2024 채택도 확인했다. 다만 원문 안에서 Sortation 정점 수가 표 1 은 54,320, 그림 1(b) 설명은 54,230 으로 서로 다르다. 경진대회 벤치마크이지 실제 물류창고가 아니라는 단서는 적절하다."
    },
    {
      "finding_id": "f20",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 'assigns exactly one new goal to an agent if the agent reaches its current one'이라는 문장과 작업이 대개 균일 표본 추출이라는 서술이 원문에 있다."
    },
    {
      "finding_id": "f21",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정]·벤더 주장 유지. 'interactive plan builder that converts a 2D grid layout into a USD warehouse'와 두 확장(api·ui), 페이지 갱신일 2026-09-18 을 확인했다. 다만 원문은 '건물 구조만' 생성한다고 한정하지 않는다. 바닥·벽·기둥 외에 천장, 하역장·점검구·창 같은 타일 변형도 언급한다. '만' 한정은 브리프의 해석이므로 빼게 한다. 로봇·랙 언급이 없다는 점은 맞다."
    },
    {
      "finding_id": "f22",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: COLM 2024 이고 v1 2024-05-03, v3 2024-10-02 다. 저자 7명, 여러 LLM·컴파일러·시뮬레이터 결합, 경찰 사고 보고서→확률적 Scenic 프로그램, 최근 5년 캘리포니아 자율주행차 사고 보고 평가를 초록에서 확인했다. 다만 초록은 ''만약 ~였다면' 시나리오 탐색'을 시스템 기능으로 밝히지 않고 동기로만 언급하므로 그 구절을 빼게 한다."
    },
    {
      "finding_id": "f23",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지: oq-131 미해결 결론이다. ref-1086 은 이번 실행에서 다시 열지 않았다(원문 미열람, 참고문헌 목록 등재로 실재 확인)."
    },
    {
      "finding_id": "f24",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "확인: 레온 대학교 포털 초록에서 공개 지리공간 데이터로 3D 시나리오를 자동 생성하고, 주요 로봇 플랫폼용 시뮬레이션 모델을 만들며, Gazebo·Unity 의 ROS 2 시스템과 연동한다는 내용을 확인했다. WAF 2025(카르타헤나) 논문집 72-86쪽이다. 초록 기준이다."
    },
    {
      "finding_id": "f25",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지: 핵심 질문에 대한 종합이다. ref-116 은 이번 실행에서 원문 미열람이다. '공통 표준은 확인하지 못했다'는 미확인 표현이 적절하다."
    },
    {
      "finding_id": "f26",
      "source_exists": true,
      "supports_claim": true,
      "cross_checked": false,
      "tag_decision": "유지",
      "note": "[추정] 유지: '연계 대상: '으로 시작하고 분류 원문 19장 경계에 맞다."
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
      "ref-079·ref-528·ref-1088·ref-1086·ref-116 은 기존 각주를 재사용했다(새 각주 아님).",
      "f19 League of Robot Runners Warehouse 지도: 기존 5절은 MovingAI MAPF 창고형 격자 지도를 '현장 사례가 아니므로 7절'로 보냈다. 같은 벤치마크 계열을 5절 사례로 넣으려면 기준(ARIAC 처럼 작업 발생 규칙을 갖춘 경진대회 시나리오)을 밝혀야 한다.",
      "새 열린 질문 3번(OpenSCENARIO 2 DSL 로 다중 플릿·설비 사건 기술)은 oq-233(기존 형식 조합)·oq-235(설비 장애 선언 일반화)와 겹치나, 특정 언어의 표현력을 묻는 좁은 질문이라 등록을 허용한다.",
      "새 열린 질문 1번(RoboVAST 방식의 다중 로봇 적용)은 oq-234 의 후속이며 중복은 아니다."
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
    "ref-1512 각주·reference_updates 의 기관 표기 '(Intel Labs, arXiv)'를 '(Intel Labs 외, arXiv)'로 고치고, 본문에서 f7 을 쓸 때도 'Intel Labs 연구진'으로만 단정하지 않는다 — 원문에서 Zhang, Y. 의 소속은 카를스루에 응용과학대·KIT 다.",
    "f11: 문장을 'ros2_fault_injection 은 ROS 2 의 토픽·변환(TF)·서비스에 장애를 주입하는 프레임워크로, 오도메트리·LaserScan·관절 상태·IMU·TF·Twist·트리거 서비스·점군 장애 유형을 두고 문서에 단언(assertion)과 pluginlib 기반 주입기 팩토리 절을 둔다' 수준으로 좁혀 [사실]로 쓴다 — 첫 페이지에서는 단언의 동작 방식과 pluginlib 로 새 주입기를 더하는 방법이 목차 수준으로만 확인됐다. ref-1518 각주 발행일은 '미확인'으로 둔다.",
    "f19: Sortation 지도의 정점 수를 쓸 때 '54,320(논문 표 1 기준; 같은 논문 그림 설명은 54,230)'으로 적거나 정점 수를 빼고 지도 크기·에이전트 수만 쓴다 — 출처 안에서 두 값이 다르다.",
    "f21: '바닥·벽·기둥 같은 건물 구조만 생성한다'에서 '만' 한정을 빼고, '바닥·벽·기둥 같은 건물 요소를 생성하며 문서에 로봇·랙 배치에 관한 설명은 없다'로 고친다. [추정]과 '벤더 주장' 병기는 유지한다 — 원문은 생성 범위를 건물 구조로 한정한다고 말하지 않는다.",
    "f21 은 편집 도구이므로 5절 물류창고 사례의 여섯 항목 표 칸을 채우는 근거로 쓰지 않는다. 사례 아래 설명문이나 6·7절 요약에서 [추정]·'벤더 주장'과 함께 짧게 언급만 한다.",
    "f22: ''만약 ~였다면' 시나리오를 탐색하게 했다' 구절을 빼고 나머지만 [사실]로 쓴다 — 초록은 반사실 탐색을 시스템 기능으로 명시하지 않고 기존 방법의 한계(동기)로만 언급한다.",
    "5절 물류창고 사례(f19·f20): 사례 제목과 사례 아래 문장에 '경진대회 벤치마크 시나리오이며 실제 물류창고 배치가 아니다'를 밝힌다. MovingAI 격자 지도를 7절에 둔 기존 판단과의 차이는 '작업 발생 규칙(목표 도달 시 새 목표 1개 배정)과 계획 시간 제한을 갖춘 경진대회 시나리오'라는 기준으로 설명한다. 기존 '물류창고 현장의 시나리오 예제·템플릿 사례는 찾지 못했다' 문장은 '실제 물류창고 현장의 시나리오 예제와 국내 자료는 여전히 찾지 못했다'로 바꿔 남긴다.",
    "9절: '개별 시나리오 인스턴스의 버전 관리 방식은 공개 자료에서 찾지 못했다' 문장을 다음으로 나눠 다시 쓴다. f1·f2 는 OpenSCENARIO XML 의 판별 호환 선언·이전 스크립트·엄격 스키마에 관한 [사실]로 쓴다. f3·f6 은 [추정]으로 쓰고, '로봇 시뮬레이션 형식(SDFormat·Open-RMF 건물 파일)의 같은 규칙은 아직 확인하지 못했다'는 단서를 반드시 남긴다. oq-234 는 해결로 바꾸지 않는다.",
    "9절 표·본문에서 f10 을 쓸 때 OpenSCENARIO 2 를 '로봇 시나리오의 과제·사건 기술 언어 후보'로 [추정]으로만 쓰고, 표준 자체(ASAM 관리)는 계속 '외부와 연계하는 것' 칸에 둔다. 두 근거 연구가 공동 저자를 공유해 독립 확인이 아님을 함께 적는다.",
    "f9·f11·f12 의 센서·메시지 수준 장애 주입은 로봇 자체 지능·제어 쪽 연계 대상이다. 6절 요약과 10절 연결(54. 시험·형식 검증·벤치마크)에서는 '시나리오에 장애를 매개변수로 선언하는 방식'의 예로만 서술하고, ROP가 센서 장애를 직접 만든다고 쓰지 않는다.",
    "3절: f13 을 [사실]로 더하되, 면담 대상이 이동로봇 시뮬레이션 시험 일반의 도메인 전문가 14명이라는 범위를 밝힌다. 기존 종합 문장은 [추정] 태그를 그대로 둔다.",
    "분할된 절(6·7·8·10·11)은 영역 페이지의 해당 절에 요약 문단을 patch(append)로만 반영한다. 기존 주제 페이지(2026-09-30-area33-s6·s7·s8·s10·s11)는 이번 실행에서 갱신하지 않는다 — page_updates 예산(2)을 넘지 않게 하려는 것이며, s7 표 행 추가는 다음 실행 후보로 넘긴다.",
    "11절: oq-234(f3·f6)·oq-233(f10·f18)은 부분 근거, oq-235(f12)·oq-131(f23)·oq-236(국내 자료 없음)은 미해결로 적는다. oq-135 는 이번 실행에서 조사하지 않았다고 밝힌다. 해결 처리는 하지 않는다.",
    "ref-1088·ref-1086·ref-116 은 이번 실행에서 다시 열지 않았다. 기존 각주 줄(접근일 2026-09-30)을 그대로 쓰고 접근일을 2026-10-09 로 바꾸지 않는다. reference_updates 에 넣는다면 source_unopened: true 로 둔다.",
    "ref-1515 각주 발행일은 2026-05-28(v1)로 적고 'ERAS 2026 채택'을 병기한다. ref-1511 각주 발행일은 '미확인'으로 둔다 — 문서 머리의 2026-05-08 표기가 발행일인지 불분명하다."
  ],
  "confidence": "low",
  "verification_note": "판정: 1차 조건부 승인. 확인 26건, 미확인 0건, 교차 확인 0건. 강등: 없음. 대신 f11·f21·f22 는 원문에 없는 한정·기능 구절을 빼서 주장을 좁히고, f19 는 출처 안에서 다르게 적힌 정점 수를 병기하도록 했다. 원문 미열람 출처: ref-1088, ref-1086, ref-116(이번 실행에서 다시 열지 않음. 참고문헌 목록 등재로 실재만 확인). 신규 출처 11건(ref-482~ref-1519)은 모두 검증자가 원문 또는 초록 페이지를 직접 열었다. ref-079·ref-528 은 입력 원문 텍스트로 대조했다. 주의: 새 근거는 모두 단일 출처다. Open-RMF 편집기 전환(f15·f16·f17)과 OpenSCENARIO 2 의 로봇 재사용(f7·f4)은 각각 같은 조직이나 공동 저자의 자료라 독립 확인이 아니다. 판 이전 규칙은 도로 교통 표준(OpenSCENARIO XML)에서만 확인됐고, 로봇 시뮬레이션 형식의 규칙은 여전히 미확인이다(oq-234 부분 근거, 해결 아님). 물류창고 사례(League of Robot Runners)는 경진대회 벤치마크이며 실제 현장이 아니다. 국내 자료도 없다. Isaac Sim Warehouse Creator(f21)는 벤더 주장이다. oq-131·oq-235·oq-236 은 미해결이고 oq-135 는 조사하지 않았다. 정정 요청은 없다. 검증 검색 0회, 열람 14회.",
  "retry_reason": null
}
```

### runs/2026-10-09-13/pages.json

```json
{
  "run_id": "2026-10-09-13",
  "outline": [
    {
      "path": "docs/categories/design-and-simulation/scenario-model-and-editing.md",
      "section": "3. 왜 중요한가",
      "budget_chars": 550,
      "summary": "이동로봇 시뮬레이션 시험 전문가 14명 면담에서 시나리오 변형 관리가 주요 장벽으로 나타났다는 직접 근거를 기존 종합 추정에 더하고, 2026-09-30 주제 페이지로 가는 링크를 되살린다. [사실][^ref-1516]",
      "planned_findings": [
        "f13"
      ]
    },
    {
      "path": "docs/categories/design-and-simulation/scenario-model-and-editing.md",
      "section": "5. 적용 사례 (현장 유형 명시)",
      "budget_chars": 1100,
      "summary": "기존 다섯 사례에 물류창고 현장 유형의 League of Robot Runners 경진대회 시나리오를 더하되 실제 물류창고 배치가 아님을 밝힌다. [사실][^ref-1514]",
      "planned_findings": [
        "f19",
        "f20",
        "f21"
      ]
    },
    {
      "path": "docs/categories/design-and-simulation/scenario-model-and-editing.md",
      "section": "6. 대표 접근법과 기술",
      "budget_chars": 1550,
      "summary": "Open-RMF 편집기의 Site Editor 전환, OpenSCENARIO 2 의 로봇 재사용, 환경·추상 시나리오·변형 분리, 장애 매개변수 선언 사례를 더하고 2026-09-30 주제 페이지 링크를 되살린다. [사실][^ref-1510][^ref-1512][^ref-1515]",
      "planned_findings": [
        "f4",
        "f7",
        "f8",
        "f9",
        "f11",
        "f12",
        "f15",
        "f16",
        "f17",
        "f18",
        "f25"
      ]
    },
    {
      "path": "docs/categories/design-and-simulation/scenario-model-and-editing.md",
      "section": "7. 관련 표준·프레임워크·오픈소스",
      "budget_chars": 650,
      "summary": "Site Editor, OpenSCENARIO XML 판 호환 규칙, Scenario Execution for Robotics, RoboVAST, League of Robot Runners 를 표로 더하고 2026-09-30 표가 있는 주제 페이지 링크를 되살린다. [사실][^ref-482][^ref-1511][^ref-1512][^ref-1515][^ref-1514]",
      "planned_findings": [
        "f1",
        "f4",
        "f7",
        "f15",
        "f19"
      ]
    },
    {
      "path": "docs/categories/design-and-simulation/scenario-model-and-editing.md",
      "section": "8. 대표 연구와 자료",
      "budget_chars": 950,
      "summary": "조합형 실행 시나리오, 출처 기록 기반 재현, OpenSCENARIO 2 로봇 실행, 사고 보고서 변환, 경진대회, 공개 데이터 기반 생성 연구를 더한다. [사실][^ref-1516][^ref-1515][^ref-1513]",
      "planned_findings": [
        "f5",
        "f13",
        "f14",
        "f22",
        "f24"
      ]
    },
    {
      "path": "docs/categories/design-and-simulation/scenario-model-and-editing.md",
      "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
      "budget_chars": 1500,
      "summary": "판 관리 문장을 도로 교통 표준의 판 이전 규칙(사실)과 로봇 형식 미확인(추정)으로 나누어 고치고, OpenSCENARIO 2 를 과제·사건 기술 언어 후보로 추정하며 외부 형식 판 규칙을 연계 대상으로 둔다. [추정][^ref-1511][^ref-1515]",
      "planned_findings": [
        "f1",
        "f2",
        "f3",
        "f6",
        "f10",
        "f26"
      ]
    },
    {
      "path": "docs/categories/design-and-simulation/scenario-model-and-editing.md",
      "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
      "budget_chars": 800,
      "summary": "54. 시험·형식 검증·벤치마크, 57. 자산·소프트웨어 수명주기 관리, 61. 물류창고, 27. 다중 로봇 경로·교통 관리 — MAPF, 36. 가상 시운전·실제 상황 재현·11. 채팅으로 실제 상황 시뮬레이션 재현, 15. 지도·공간·위치 모델과의 연결을 더한다. [추정][^ref-1515][^ref-1511]",
      "planned_findings": [
        "f4",
        "f9",
        "f14",
        "f1",
        "f6",
        "f19",
        "f22",
        "f23",
        "f18"
      ]
    },
    {
      "path": "docs/categories/design-and-simulation/scenario-model-and-editing.md",
      "section": "11. 열린 질문",
      "budget_chars": 950,
      "summary": "이번 실행 전 8건·새 질문 3건으로 첫 문장을 고치고, oq-234·oq-233 은 부분 근거, oq-235·oq-131·oq-236 은 미해결, oq-135 는 미조사로 적는다. [추정][^ref-1511][^ref-1515]",
      "planned_findings": [
        "f3",
        "f6",
        "f10",
        "f12",
        "f18",
        "f23"
      ]
    }
  ],
  "pages": [
    {
      "path": "docs/categories/design-and-simulation/scenario-model-and-editing.md",
      "action": "update",
      "status": "draft",
      "diff_summary": "차등 갱신: 3절 면담 근거 추가, 5절 물류창고 경진대회 사례 추가·문장 교체, 6·7·8·10절 요약 덧붙임과 2026-09-30 주제 페이지 링크 복원, 9절 판 관리 문장 정정, 11절 첫 문장 건수 정정·진행 현황, 13절 각주 11건 추가, related_areas 에 57·61 추가, last_run 2026-10-09 (2차 수정 5건 반영)",
      "patches": [
        {
          "section": "3. 왜 중요한가",
          "action": "append",
          "frontmatter": {
            "last_run": "2026-10-09",
            "related_areas": [
              9,
              11,
              14,
              15,
              18,
              19,
              22,
              24,
              27,
              32,
              34,
              36,
              44,
              54,
              57,
              61,
              62,
              63,
              64,
              65,
              66
            ],
            "sources": [
              "ref-1086",
              "ref-104",
              "ref-079",
              "ref-971",
              "ref-528",
              "ref-1087",
              "ref-1088",
              "ref-726",
              "ref-1089",
              "ref-815",
              "ref-1090",
              "ref-116",
              "ref-1091",
              "ref-1092",
              "ref-046",
              "ref-482",
              "ref-1510",
              "ref-1511",
              "ref-1512",
              "ref-1513",
              "ref-1514",
              "ref-1515",
              "ref-1516",
              "ref-1517",
              "ref-1518",
              "ref-1519"
            ]
          },
          "content": "(절 본문 생략 — runs/2026-10-09-13/pages/categories/design-and-simulation/scenario-model-and-editing.md 의 해당 절을 본다)"
        },
        {
          "section": "5. 적용 사례 (현장 유형 명시)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-09-13/pages/categories/design-and-simulation/scenario-model-and-editing.md 의 해당 절을 본다)"
        },
        {
          "section": "6. 대표 접근법과 기술",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-09-13/pages/categories/design-and-simulation/scenario-model-and-editing.md 의 해당 절을 본다)"
        },
        {
          "section": "7. 관련 표준·프레임워크·오픈소스",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-09-13/pages/categories/design-and-simulation/scenario-model-and-editing.md 의 해당 절을 본다)"
        },
        {
          "section": "8. 대표 연구와 자료",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-09-13/pages/categories/design-and-simulation/scenario-model-and-editing.md 의 해당 절을 본다)"
        },
        {
          "section": "9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-09-13/pages/categories/design-and-simulation/scenario-model-and-editing.md 의 해당 절을 본다)"
        },
        {
          "section": "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-09-13/pages/categories/design-and-simulation/scenario-model-and-editing.md 의 해당 절을 본다)"
        },
        {
          "section": "11. 열린 질문",
          "action": "replace",
          "content": "(절 본문 생략 — runs/2026-10-09-13/pages/categories/design-and-simulation/scenario-model-and-editing.md 의 해당 절을 본다)"
        },
        {
          "section": "13. 참고 자료 (각주)",
          "action": "append",
          "content": "(절 본문 생략 — runs/2026-10-09-13/pages/categories/design-and-simulation/scenario-model-and-editing.md 의 해당 절을 본다)"
        }
      ]
    },
    {
      "path": "docs/topics/2026/2026-10-09-area33-s6.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 33. 시나리오 모델·편집 의 \"6. 대표 접근법과 기술\" 절(2,409자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-09-area33-s8.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 33. 시나리오 모델·편집 의 \"8. 대표 연구와 자료\" 절(1,827자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-09-area33-s10.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 33. 시나리오 모델·편집 의 \"10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)\" 절(1,294자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-09-area33-s11.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 33. 시나리오 모델·편집 의 \"11. 열린 질문\" 절(1,273자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-09-area33-s7.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 33. 시나리오 모델·편집 의 \"7. 관련 표준·프레임워크·오픈소스\" 절(996자)을 옮겼다"
    },
    {
      "path": "docs/topics/2026/2026-10-09-area33-s3.md",
      "action": "create",
      "status": "draft",
      "diff_summary": "자동 분리: 33. 시나리오 모델·편집 의 \"3. 왜 중요한가\" 절(589자)을 옮겼다"
    }
  ],
  "changelog_entry": "2026-10-09 | 33. 시나리오 모델·편집 | 갱신: 5절 물류창고 경진대회 사례 추가, 9절 시나리오 판 관리 문장 정정, Open-RMF Site Editor 전환·OpenSCENARIO 2 로봇 재사용·RoboVAST 반영, 1차 조건부 승인 수정 15건·2차 수정 5건 반영(2026-09-30 주제 페이지 링크 복원, 11절 건수 정정) | run 2026-10-09-13",
  "index_updates": {
    "home_recent": "2026-10-09 — 33. 시나리오 모델·편집: 물류창고 경진대회 시나리오 사례 추가, 시나리오 판 이전 규칙(OpenSCENARIO XML)과 로봇 형식 미확인을 9절에 정정 반영",
    "category_recent": "2026-10-09 — 33. 시나리오 모델·편집: 3·5·6·7·8·9·10·11절 차등 갱신(League of Robot Runners 물류창고 사례, Open-RMF Site Editor 전환, OpenSCENARIO 2 로봇 재사용, RoboVAST 인스턴스 기록)",
    "area_recent": "2026-10-09 — 33. 시나리오 모델·편집: 갱신(차등) — 5절 물류창고 사례(경진대회 벤치마크) 추가, 9절 판 관리 문장 정정, 6·7·8·10·11절 요약 덧붙임과 2026-09-30 주제 페이지 링크 복원, 각주 11건 추가, 1차 수정 15건·2차 수정 5건 반영"
  },
  "glossary_updates": [
    {
      "action": "new",
      "slug": "data-provenance",
      "term_ko": "데이터 출처 추적",
      "term_en": "Data Provenance (W3C PROV)",
      "definition": "어떤 산출물이 어떤 입력·설정·실행·주체로부터 만들어졌는지를 기계가 읽을 수 있는 관계로 기록하는 일로, W3C PROV 가 그 표준 데이터 모델이며 시뮬레이션 시험의 재현성 확보에 쓰인다.",
      "description": "RoboVAST 확장 연구는 PROV-O 를 핵심 메타모델로 DCAT·Dublin Core·QUDT 와 함께 JSON-LD 로 기록해 SPARQL 로 질의하게 했다.",
      "related_areas": [
        33,
        54,
        57
      ],
      "sources": [
        "ref-1515"
      ]
    },
    {
      "action": "new",
      "slug": "abstract-and-concrete-scenario",
      "term_ko": "추상 시나리오·구체 시나리오",
      "term_en": "Abstract Scenario / Concrete Scenario",
      "definition": "매개변수와 변형 범위만 정한 시나리오(추상)와 모든 값이 하나로 정해져 바로 실행할 수 있는 시나리오 인스턴스(구체)를 구분하는 말로, 시험 도구가 추상 시나리오를 여러 구체 시나리오로 펼쳐 실행한다.",
      "description": "RoboVAST 는 OpenSCENARIO DSL 추상 시나리오와 변형 파일을 구체 시험 구성(scenario.config)으로 해석하고, Scenario Execution for Robotics 는 매개변수 값 목록을 조합마다 하나의 실행 시나리오로 펼친다.",
      "related_areas": [
        33,
        54
      ],
      "sources": [
        "ref-1515",
        "ref-1512"
      ]
    },
    {
      "action": "new",
      "slug": "strict-schema",
      "term_ko": "엄격 스키마",
      "term_en": "Strict Schema (deprecated elements removed)",
      "definition": "형식의 판에서 폐기 예정 요소를 뺀 검증용 스키마로, 기존 시나리오 파일을 이 스키마로 검사해 다음 판에서 사라질 요소를 찾아 바꾸게 한다(ASAM OpenSCENARIO XML).",
      "related_areas": [
        33,
        57
      ],
      "sources": [
        "ref-1511"
      ]
    }
  ],
  "reference_updates": [
    {
      "id": "ref-482",
      "org": "Open-RMF (open-rmf/rmf_site)",
      "title": "rmf_site — RMF Site Editor (README)",
      "published": null,
      "url": "https://github.com/open-rmf/rmf_site",
      "type": "오픈소스 문서",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "Rust·Bevy 기반 RMF 배치 현장 시각화·편집 도구 Site Editor 의 README. 데스크톱·웹 빌드, rmf_site_ros2 로 시뮬레이션·주행 그래프 생성.",
      "cited_by": [
        "docs/categories/design-and-simulation/scenario-model-and-editing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1510",
      "org": "Open Robotics Discourse (Open-RMF 상호운용 그룹, 작성자 grey)",
      "title": "Interoperability Interest Group June 6, 2024: Preview of the RMF Site Editor",
      "published": "2024-06-05",
      "url": "https://discourse.openrobotics.org/t/interoperability-interest-group-june-6-2024-preview-of-the-rmf-site-editor/38070",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "Site Editor 를 예전 traffic-editor 의 대체 도구로 소개하고 편집 대상(3D 환경·로봇·교통 규칙·승강기·문)과 Bevy 기반 확장성을 설명한 공지.",
      "cited_by": [
        "docs/categories/design-and-simulation/scenario-model-and-editing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1511",
      "org": "ASAM e.V.",
      "title": "ASAM OpenSCENARIO XML v1.4.0 — 5 Backward compatibility",
      "published": null,
      "url": "https://openscenario.asam.net/ASAM_OpenSCENARIO_XML/v1.4.0/05_backward_compatibility/01_backward_compatibility.html",
      "type": "표준",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "OpenSCENARIO XML 판 사이 하위 호환성 선언, 1.2.0→1.3.0 XSLT 이전 스크립트, 폐기 요소 없는 엄격 스키마를 설명하는 공식 문서 절. 발행일 미확인(문서 머리의 2026-05-08 표기가 발행일인지 불분명).",
      "cited_by": [
        "docs/categories/design-and-simulation/scenario-model-and-editing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1512",
      "org": "Pasch, F., Mirus, F., Zhang, Y., & Scholl, K.-U. (Intel Labs 외, arXiv)",
      "title": "Scenario Execution for Robotics: A generic, backend-agnostic library for running reproducible robotics experiments and tests",
      "published": "2024-09-11",
      "url": "https://arxiv.org/abs/2409.07080",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "OpenSCENARIO 2 로 쓴 로봇 시나리오를 행동 트리로 바꿔 실행하는 라이브러리. 매개변수 변형, 라이다 장애 주입, 시뮬레이션–실물 같은 시나리오 파일 사용(프리프린트, 본문 HTML 확인). 저자 Zhang, Y. 의 소속은 카를스루에 응용과학대·KIT.",
      "cited_by": [
        "docs/categories/design-and-simulation/scenario-model-and-editing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1513",
      "org": "Elmaaroufi, K., Shanker, D., Cismaru, A., Vazquez-Chanlatte, M., Sangiovanni-Vincentelli, A., Zaharia, M., & Seshia, S. A. (COLM 2024, arXiv)",
      "title": "ScenicNL: Generating Probabilistic Scenario Programs from Crash Reports",
      "published": "2024-05-03",
      "url": "https://arxiv.org/abs/2405.03709",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "대규모 언어 모델·컴파일러·시뮬레이터를 엮어 경찰 사고 보고서를 확률적 Scenic 시나리오 프로그램으로 바꾸는 연구(초록 페이지 기준, 최종 수정 2024-10-02).",
      "cited_by": [
        "docs/categories/design-and-simulation/scenario-model-and-editing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1514",
      "org": "Jiang, H., Zhang, Y., Veerapaneni, R., & Li, J. (SoCS 2024, arXiv)",
      "title": "Scaling Lifelong Multi-Agent Path Finding to More Realistic Settings: Research Challenges and Opportunities",
      "published": "2024-04-24",
      "url": "https://arxiv.org/abs/2404.16162",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "2023 League of Robot Runners 우승 방법과 연구 과제. Warehouse·Sortation 등 경진대회 지도 규모, 목표 배정 방식, 단계당 1초 계획 제한을 기술(본문 HTML 확인). Sortation 정점 수는 표 1 은 54,320, 그림 설명은 54,230.",
      "cited_by": [
        "docs/categories/design-and-simulation/scenario-model-and-editing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1515",
      "org": "Ortega, A., Wiest, S., Pasch, F., & Hochgeschwender, N. (arXiv, ERAS 2026 채택)",
      "title": "Replicable Simulation-Based Robot Validation through Provenance",
      "published": "2026-05-28",
      "url": "https://arxiv.org/abs/2605.29973",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "RoboVAST 시험 틀에 W3C PROV 기반 출처 기록과 FAIR 메타데이터를 더해 시뮬레이션 시험의 재현성을 높이는 연구. 환경·추상 시나리오·변형 분리와 구체 구성 해석(v1 2026-05-28, 본문 HTML v2 확인).",
      "cited_by": [
        "docs/categories/design-and-simulation/scenario-model-and-editing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1516",
      "org": "Ortega, A., Parra, S., Schneider, S., & Hochgeschwender, N. (Frontiers in Robotics and AI 11)",
      "title": "Composable and executable scenarios for simulation-based testing of mobile robots",
      "published": "2024-08-02",
      "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11327003/",
      "type": "논문",
      "reliability": "high",
      "accessed": "2026-10-09",
      "summary": "전문가 14명 면담으로 시나리오 변형 관리의 어려움을 확인하고, FloorPlan DSL 기반 조합형 실행 시나리오로 Gazebo 월드·지도·경유점을 생성해 주행 스택 설정 오류를 찾은 연구.",
      "cited_by": [
        "docs/categories/design-and-simulation/scenario-model-and-editing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1517",
      "org": "NVIDIA",
      "title": "Isaac Sim Documentation — Warehouse Creator Extension",
      "published": null,
      "url": "https://docs.isaacsim.omniverse.nvidia.com/latest/assets/asset_utilities/ext_omni_warehouse_creator.html",
      "type": "벤더 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "2D 격자 배치를 USD 창고로 바꾸는 Isaac Sim 확장(omni.warehouse.creator.api/ui) 문서. 바닥·벽·기둥 같은 건물 요소를 생성하며 로봇·랙 배치 설명은 없다. 벤더 주장. 페이지 갱신 2026-09-18.",
      "cited_by": [
        "docs/categories/design-and-simulation/scenario-model-and-editing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1518",
      "org": "ros2_fault_injection 프로젝트 (Read the Docs)",
      "title": "ros2_fault_injection documentation",
      "published": null,
      "url": "https://ros2-fault-injection.readthedocs.io/",
      "type": "오픈소스 문서",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "ROS 2 토픽·TF·서비스 장애 주입 프레임워크 문서 첫 페이지. 장애 유형 목록, 단언·pluginlib 주입기 팩토리 절(목차 수준 확인). 관리 주체·판 미표기.",
      "cited_by": [
        "docs/categories/design-and-simulation/scenario-model-and-editing.md"
      ],
      "source_unopened": false
    },
    {
      "id": "ref-1519",
      "org": "Sánchez de la Fuente, S., Prieto López, L., González Santamarta, M. Á., Matellán Olivera, V. 외 (Universidad de León, WAF 2025)",
      "title": "Scenario Generation for Robot Simulation from Public Data",
      "published": "2025",
      "url": "https://portalcientifico.unileon.es/documentos/6972798ce66b2902147b1aeb",
      "type": "논문",
      "reliability": "medium",
      "accessed": "2026-10-09",
      "summary": "공개 지리공간 데이터로 로봇 시뮬레이션용 3D 시나리오를 생성해 Gazebo·Unity 의 ROS 2 시스템과 연동하는 방법(학회 논문집 초록 기준).",
      "cited_by": [
        "docs/categories/design-and-simulation/scenario-model-and-editing.md"
      ],
      "source_unopened": false
    }
  ],
  "open_question_updates": [
    {
      "action": "new",
      "question": "RoboVAST 처럼 추상 시나리오를 구체 인스턴스로 해석하고 실행마다 출처를 기록하는 방식을 여러 제조사 로봇 플릿과 승강기·문 같은 설비가 함께 있는 다중 로봇 시나리오에 적용한 사례가 있는가?",
      "areas": [
        33,
        54
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "Open-RMF Site Editor 의 현장 형식이 기존 traffic-editor 의 .building.yaml 을 대체하는가, 그리고 기존 건물 파일을 옮기는 공식 변환 도구나 판 이전 규칙이 있는가?",
      "areas": [
        33,
        15
      ],
      "status": "열림",
      "link": null
    },
    {
      "action": "new",
      "question": "OpenSCENARIO 2 DSL 로 다중 로봇 플릿의 작업 배정과 승강기·문 같은 설비 사건을 기술할 수 있는가, 기술하려면 어떤 확장 라이브러리가 필요한가?",
      "areas": [
        33,
        22
      ],
      "status": "열림",
      "link": null
    }
  ],
  "site_matrix_updates": [
    {
      "site_type": "물류창고",
      "item": "시작 조건",
      "link": "docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시",
      "title": "33. 시나리오 모델·편집"
    },
    {
      "site_type": "물류창고",
      "item": "작업 대상",
      "link": "docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시",
      "title": "33. 시나리오 모델·편집"
    },
    {
      "site_type": "물류창고",
      "item": "수행 자원",
      "link": "docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시",
      "title": "33. 시나리오 모델·편집"
    },
    {
      "site_type": "물류창고",
      "item": "제약",
      "link": "docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시",
      "title": "33. 시나리오 모델·편집"
    },
    {
      "site_type": "물류창고",
      "item": "예외·성과",
      "link": "docs/categories/design-and-simulation/scenario-model-and-editing.md#5-적용-사례-현장-유형-명시",
      "title": "33. 시나리오 모델·편집"
    }
  ],
  "standards_updates": [
    {
      "name": "Scenario Execution for Robotics (OpenSCENARIO 2 기반 로봇 시나리오 실행 라이브러리)",
      "kind": "오픈소스",
      "org": "Pasch, F. 외 (Intel Labs 외)",
      "url": "https://arxiv.org/abs/2409.07080",
      "related_areas": [
        33,
        54
      ],
      "summary": "ASAM OpenSCENARIO 2 로 쓴 로봇 시나리오를 행동 트리(PyTrees)로 바꿔 실행하는 백엔드·미들웨어 독립 파이썬 라이브러리로, Gazebo·Nav2·PyBullet 라이브러리와 매개변수 조합 전개를 둔다.",
      "ref_id": "ref-1512"
    },
    {
      "name": "RoboVAST (출처 기록 기반 시뮬레이션 시험 틀)",
      "kind": "프레임워크",
      "org": "Ortega, A., Wiest, S., Pasch, F., & Hochgeschwender, N.",
      "url": "https://arxiv.org/abs/2605.29973",
      "related_areas": [
        33,
        54,
        57
      ],
      "summary": "환경(FloorPlan 모델)·추상 시나리오(OpenSCENARIO DSL)·변형 파일을 나누고 인스턴스를 구체 시험 구성으로 해석해 실행별 기록과 W3C PROV 기반 출처를 남기는 시험 틀이다.",
      "ref_id": "ref-1515"
    }
  ],
  "additional_research_requests": [
    "9절·11절(oq-234): 로봇 시뮬레이션 형식(SDFormat·Open-RMF 건물 파일·Site Editor 형식)에서 개별 시나리오 인스턴스를 형식 판 사이에서 옮기는 규칙이나 변환 도구가 있는지 — 현재 판 이전 규칙은 도로 교통 표준에서만 확인됐다.",
    "6절·11절(oq-233 및 새 질문): 기존 .building.yaml 을 Site Editor 형식으로 옮기는 공식 방법과 Site Editor 저장 형식의 판 규칙 — 편집기 전환에 따른 환경 참조 이전 규칙을 서술하는 데 필요하다.",
    "5절(oq-236): 실제 물류창고 현장의 시나리오 예제·템플릿과 국내 다중 로봇 시나리오 예제 라이브러리 — 현재 물류창고 사례는 경진대회 벤치마크뿐이다.",
    "5절: League of Robot Runners 공식 사이트·2024 대회 자료로 지도 규모·작업 발생 규칙(f19·f20)을 교차 확인 — 현재 우승 팀 논문 단일 출처이며 Sortation 정점 수가 논문 안에서 두 값으로 적혀 있다.",
    "11절(oq-135): 로봇 작업 시나리오 구성에서 되물어야 할 항목의 표준 질문 목록 — 이번 실행에서 조사하지 않았다.",
    "예산으로 미룸: 주제 페이지 docs/topics/2026/2026-09-30-area33-s7.md 표에 Site Editor·Scenario Execution·RoboVAST·ros2_fault_injection·League of Robot Runners 행 추가(1차 수정 지시로 이번 실행에서 주제 페이지를 갱신하지 않음).",
    "참고문헌 정리: ref-1516(PMC URL)과 ref-1134(Frontiers URL)가 같은 논문(Ortega 외, Frontiers in Robotics and AI, 2024-08-02)을 가리키므로 병합 여부 확인이 필요하다.",
    "파이프라인 담당: 분량 자동 분리 코드가 이미 분리된 절을 다시 분리할 때 기존 '자세한 내용은 주제 페이지 …' 링크 줄을 버린다. 이번 재실행에서는 각 절 append 첫 줄에 다른 문구의 2026-09-30 주제 페이지 링크를 넣어 대응했으나, 분리 코드가 기존 링크를 보존하도록 고칠 것을 요청한다."
  ],
  "fixes_applied": [
    "ref-1512 기관 표기 — 13절 각주와 reference_updates 의 org 를 '(Intel Labs 외, arXiv)'로 고치고, 6·8절 본문에서도 'Pasch 외(Intel Labs 외)'로만 써서 Intel Labs 연구진으로 단정하지 않았다.",
    "f11 — 6절에 '…Twist·트리거 서비스·점군 장애 유형을 두고 문서에 단언(assertion)과 pluginlib 기반 주입기 팩토리 절을 둔다' 수준으로 좁힌 문장을 [사실]로 썼고, ref-1518 각주 발행일은 '미확인'으로 두었다.",
    "f19 — 5절 물류창고 사례 작업 대상 칸에 Sortation 정점 수를 '54,320개 — 논문 표 1 기준; 같은 논문 그림 설명은 54,230개'로 병기했다.",
    "f21 — '만' 한정을 빼고 '바닥·벽·기둥 같은 건물 요소를 생성한다고 설명하고, 문서에 로봇·랙 배치에 관한 설명은 없다'로 고쳤으며 [추정] 벤더 주장 병기를 유지했다.",
    "f21 — 5절 물류창고 사례의 여섯 항목 표 칸에는 쓰지 않고 사례 아래 설명문 한 단락에만 [추정] 벤더 주장과 함께 짧게 언급했다.",
    "f22 — ''만약 ~였다면' 시나리오를 탐색하게 했다' 구절을 빼고 8절에서 나머지만 [사실]로 썼다.",
    "5절 — 사례 제목과 사례 아래 문장에 '경진대회 벤치마크 시나리오이며 실제 물류창고 배치가 아니다'를 밝히고, Moving AI 격자 지도를 7절에 둔 판단과의 차이를 '작업 발생 규칙(목표 도달 시 새 목표 1개 배정)과 계획 시간 제한을 갖춘 경진대회 시나리오' 기준으로 설명했으며, 기존 문장을 '실제 물류창고 현장의 시나리오 예제와 국내 자료는 여전히 찾지 못했다'로 바꿨다.",
    "9절 — '개별 시나리오 인스턴스의 버전 관리 방식은 공개 자료에서 찾지 못했다' 문장을 f1·f2 의 OpenSCENARIO XML 판별 호환 선언·이전 스크립트·엄격 스키마 [사실] 두 문장과 f3·f6 [추정] 문장으로 나눠 다시 썼고, '로봇 시뮬레이션 형식(SDFormat·Open-RMF 건물 파일)의 같은 규칙은 아직 확인하지 못했다' 단서를 남겼으며 oq-234 는 열린 채로 두었다.",
    "9절 표 — 업종별 조건 행의 'ROP가 직접 맡는 것' 칸에 OpenSCENARIO 2 를 '로봇 시나리오의 과제·사건 기술 언어 후보'로 [추정]으로만 쓰고 두 근거 연구가 공동 저자를 공유해 독립 확인이 아님을 적었으며, 표준 자체(ASAM 관리)는 '외부와 연계하는 것' 칸에 두었다.",
    "f9·f11·f12 — 6절 요약에서 '시나리오에 장애를 매개변수로 선언하는 방식의 예'로만 쓰고 센서·메시지 수준 장애 주입은 로봇 자체 지능·제어 쪽 연계 대상이라 ROP가 직접 만들지 않는다고 밝혔으며, 10절 54. 시험·형식 검증·벤치마크 연결에서도 같은 단서를 두었다.",
    "3절 — f13 을 [사실]로 덧붙이며 면담 대상이 이동로봇 시뮬레이션 시험 일반의 도메인 전문가 14명임을 밝혔고, 기존 종합 문장의 [추정] 태그는 그대로 두었다.",
    "분할된 절(6·7·8·10·11)은 영역 페이지 해당 절에 append 패치로만 요약을 더했고, 기존 주제 페이지 2026-09-30-area33-s6·s7·s8·s10·s11 은 갱신하지 않았으며 s7 표 행 추가는 additional_research_requests 에 다음 실행 후보로 넘겼다.",
    "11절 — oq-234(f3·f6)·oq-233(f10·f18)은 부분 근거, oq-235(f12)·oq-131(f23)·oq-236(국내 자료 없음)은 미해결로 적고 oq-135 는 이번 실행에서 조사하지 않았다고 밝혔으며, 해결 처리와 open_question_updates 의 상태 변경은 하지 않았다.",
    "ref-1088·ref-1086·ref-116 — 13절의 기존 각주 줄(접근일 2026-09-30)을 그대로 두고 접근일을 바꾸지 않았으며, reference_updates 에는 넣지 않았다.",
    "ref-1515 각주 발행일을 2026-05-28(v1)로 적고 기관 표기에 'ERAS 2026 채택'을 병기했으며, ref-1511 각주 발행일은 '미확인'으로 두었다.",
    "2차: 기존 주제 페이지 링크 복원 — 3·6·7·8·10절 append 패치 첫 줄과 11절 replace 본문 둘째 단락에 '2026-09-30 실행까지 정리한 내용은 [33. 시나리오 모델·편집 — … (2026-09-30)](../../topics/2026/2026-09-30-area33-sN.md)에 있다' 형식으로 2026-09-30-area33-s3·s6·s7·s8·s10·s11 링크를 하나씩 넣었다(7절은 Moving AI MAPF 벤치마크·VDMA 레이아웃 교환 형식이 그 표에 있음을 함께 밝혀 5절 끝 안내의 근거를 이었다). 링크는 영역 페이지와 분리 주제 페이지 어느 쪽에 놓여도 맞도록 ../../topics/… 형식으로 썼다.",
    "2차: 11절 — replace 로 첫 문장을 '이번 실행 전 이 영역에 걸린 열린 질문은 8건이고, 이번 실행(2026-10-09-13)에서 3건을 새로 올렸으며 해결 처리한 질문은 없다'로 고쳤다(입력 열린 질문 목록 기준).",
    "2차: 10절 — '이 변환은 언어 모델을 쓰므로 … 44. 로봇 기반 모델·언어 모델 계획과도 이어진다. [사실]'을 'ScenicNL 은 여러 대규모 언어 모델 프롬프트를 컴파일러·시뮬레이터와 엮는다. [사실][^ref-1513]'과 '그래서 이런 기록 변환 방식은 … 44. 로봇 기반 모델·언어 모델 계획과도 이어질 것으로 보인다. [추정][^ref-1513]' 두 문장으로 나눴다.",
    "2차: 절 번호 참조 — 6절의 '8절에 정리했다', 8절의 '면담 근거는 3절에 있다'·'6절에 요약했다'·'5절 물류창고 사례의 근거다', 10절의 '(9절)'·'(5절)', 11절의 '(9절)'을 모두 '원 페이지 [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md)의 <절 번호와 절 이름>' 형식으로 고쳤고, 같은 유형인 7절 표의 '5절 물류창고 사례' 표기도 같은 형식으로 맞췄다.",
    "2차: last_run — 3절 patch 의 frontmatter 에 last_run: 2026-10-09 를 넣었다.",
    "분량 초과 자동 분리: 33. 시나리오 모델·편집 본문 14,129자 > 기준 4,000자 → 6개 절을 주제 페이지로 옮김, 남은 본문 6,692자"
  ]
}
```

### runs/2026-10-09-13/format_check.md

```markdown
# 형식 검증 결과(pages)

- 판정: 통과
- 차등 갱신 패치 적용:
    - docs/categories/design-and-simulation/scenario-model-and-editing.md (9개 절)
- 분량 초과 자동 분리:
    - docs/categories/design-and-simulation/scenario-model-and-editing.md "6. 대표 접근법과 기술" → docs/topics/2026/2026-10-09-area33-s6.md (2,409자)
    - docs/categories/design-and-simulation/scenario-model-and-editing.md "8. 대표 연구와 자료" → docs/topics/2026/2026-10-09-area33-s8.md (1,827자)
    - docs/categories/design-and-simulation/scenario-model-and-editing.md "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" → docs/topics/2026/2026-10-09-area33-s10.md (1,294자)
    - docs/categories/design-and-simulation/scenario-model-and-editing.md "11. 열린 질문" → docs/topics/2026/2026-10-09-area33-s11.md (1,273자)
    - docs/categories/design-and-simulation/scenario-model-and-editing.md "7. 관련 표준·프레임워크·오픈소스" → docs/topics/2026/2026-10-09-area33-s7.md (996자)
    - docs/categories/design-and-simulation/scenario-model-and-editing.md "3. 왜 중요한가" → docs/topics/2026/2026-10-09-area33-s3.md (589자)
```

### runs/2026-10-09-13/pages/categories/design-and-simulation/scenario-model-and-editing.md

```markdown
---
title: "33. 시나리오 모델·편집"
type: area
category: "I. 설계·시뮬레이션"
area_no: 33
related_areas: [9, 11, 14, 15, 18, 19, 22, 24, 27, 32, 34, 36, 44, 54, 57, 61, 62, 63, 64, 65, 66]
tags: [시나리오 형식, OpenSCENARIO, Open-RMF, 장애 주입, 시나리오 라이브러리, 미션 기술 형식]
status: draft
confidence: low
created: 2026-09-28
updated: 2026-10-09
sources: [ref-1086, ref-104, ref-079, ref-971, ref-528, ref-1087, ref-1088, ref-726, ref-1089, ref-815, ref-1090, ref-116, ref-1091, ref-1092, ref-046, ref-482, ref-1510, ref-1511, ref-1512, ref-1513, ref-1514, ref-1515, ref-1516, ref-1517, ref-1518, ref-1519]
last_run: 2026-10-09
version: 3
---

[홈](../../index.md) › [I. 설계·시뮬레이션](index.md) › 33. 시나리오 모델·편집

# 33. 시나리오 모델·편집

!!! info "소속 대분류"
    [I. 설계·시뮬레이션](index.md) — 핵심 질문:
    현장을 바꾸거나 로봇을 늘리기 전에 가상으로 설계하고 결과를 미리 볼 수 있는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: low · 페이지 버전: 2 · 마지막 갱신: 2026-09-30 · 마지막 실행: 2026-09-30
<!-- auto:page-status:end -->

## 1. 한 줄 정의

시나리오 형식, 예제 라이브러리, 시나리오·워크플로 편집기 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **시나리오 모델·형식**: 환경·로봇·사람·물품·작업·정책·물리·장애를 담는 버전 있는 시나리오 형식을 정한다
- **시나리오 라이브러리**: 현장 유형별 예제·템플릿(아파트·공장·호텔·물류 시설 등)을 모아 다시 쓴다
- **시나리오·워크플로 편집기**: 사람이 직접 시나리오와 워크플로를 화면에서 그리고 고친다(노코드 편집)

## 2. 핵심 질문

현장·로봇·사람·작업을 담은 시나리오를 어떻게 표현하고 다시 쓸 것인가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

## 3. 왜 중요한가

시나리오를 정해진 형식으로 표현해 두지 않으면 계획기·정책을 같은 조건에서 비교하거나 장애·긴급 요청 대응 시험을 반복하기 어렵고, 조건마다 시나리오 파일이 불어나며, 미션과 환경을 정의할 도메인 전문가가 쓸 공통 형식도 없다는 것이 확인한 자료의 종합이다. [추정][^ref-726][^ref-1091][^ref-528][^ref-1088][^ref-116]

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 왜 중요한가](../../topics/2026/2026-10-09-area33-s3.md)에 있다.

## 4. 핵심 개념과 용어

시나리오를 표현하는 형식들은 정적 환경과 동적 내용을 나누고, 매개변수·확률 분포·장애 선언으로 한 시나리오를 여러 조건에 다시 쓰게 한다. [추정][^ref-1088][^ref-1086][^ref-528]

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area33-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

아래 여섯 사례는 모두 실제 현장 배치가 아니라 공개된 시뮬레이션 예제 월드·벤치마크·경진대회 시나리오를 여섯 항목으로 정리한 것이며, 이 영역에서는 각 시나리오가 무엇을 어떤 단위로 담았는지를 본다. [사실][^ref-104][^ref-971][^ref-1087][^ref-1514]

**현장 유형:** 상업 시설

**사례:** Open-RMF 예제 호텔·공항 터미널 월드의 다중 플릿 순찰·청소 시나리오(시뮬레이션 예제 월드)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 월드를 띄운 뒤 dispatch_clean·dispatch_patrol 같은 작업 명령을 따로 넣으면 작업이 생긴다. [사실][^ref-104] |
| 작업 대상 | 호텔 월드의 로비와 객실 2개 층 공간을 순찰(loop)·청소한다(예제 명령은 로비 청소). [사실][^ref-104] |
| 수행 자원 | 호텔 월드에는 로봇 플릿 3개(로봇 4대), 승강기 2대, 여러 문이 있고, 디스패처가 [플릿 어댑터](../../glossary/fleet-adapter.md)들 사이의 작업 입찰을 조율한다. [사실][^ref-104] |
| 제약 | 공항 터미널 월드는 차선·목적지·로봇이 많은 대형 지도에 선택적으로 군중 시뮬레이션과 사람이 모는 읽기 전용(read_only) 카트를 더해 순찰·배송·청소를 실행한다. [사실][^ref-104] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

rmf_demos의 시나리오는 건물 구성(차선·승강기·문·충전 위치)을 담은 월드를 띄운 뒤 작업을 명령으로 따로 넣는 구조다(2026-09-30 확인). [사실][^ref-104] 호텔·공항 터미널 모두 시뮬레이션 예제 월드이며 실제 시설의 도입 사례가 아니다.

**현장 유형:** 병원

**사례:** Open-RMF 예제 클리닉 월드에서 두 층의 간호 스테이션 사이 순찰(시뮬레이션 예제 월드)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 순찰 명령(dispatch_patrol)으로 작업을 넣는다. 예제 명령은 1층과 2층의 간호 스테이션을 순찰 지점으로 지정한다. [사실][^ref-104] |
| 작업 대상 | 두 층에 걸친 간호 스테이션 사이의 순찰 경로(공간) [사실][^ref-104] |
| 수행 자원 | 역할이 다른 로봇 플릿 2개와 승강기 2대 [사실][^ref-104] |
| 제약 | 로봇이 승강기 2대가 있는 2개 층 시설에서 층을 오가며 순찰해야 한다. [사실][^ref-104] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

클리닉 월드는 병원형 시나리오 예제이며 실제 병원 배치 사례가 아니다. 이 월드는 승강기 2대가 있는 2개 층 시설이고, 로봇이 층을 오가며 순찰한다. [사실][^ref-104] 층간 이동이 승강기를 거친다는 점에서 이 예제는 설비를 시나리오 요소로 담는 예로 볼 수 있다. [추정][^ref-104]

**현장 유형:** 실외

**사례:** Open-RMF 예제 캠퍼스 월드의 배송 로봇 장거리 순찰(시뮬레이션 예제 월드)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 작업 명령으로 장거리 순찰을 넣는다. [사실][^ref-104] |
| 작업 대상 | 차선을 GPS WGS84 좌표로 행성 규모에 주석한 넓은 캠퍼스 공간 [사실][^ref-104] |
| 수행 자원 | 여러 대의 배송 로봇 [사실][^ref-104] |
| 제약 | 해당 없음 |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

캠퍼스 월드는 실내 층 좌표 대신 지구 좌표로 공간을 주석한 실외 시나리오 예제다. [사실][^ref-104] 같은 예제 모음의 제조·물류 월드는 영상 데모뿐이라 사례로 세우지 않고 7절에서만 다룬다.

**현장 유형:** 가정

**사례:** BEHAVIOR-1K의 일상 가정 활동 라이브러리(벤치마크)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | '로봇이 무엇을 해 주길 바라는가' 설문으로 고른 일상 가정 활동 1,000개를 BDDL로 명세하고, 장면 50개와 물리·의미 속성을 주석한 객체 9,000개 이상(강체·변형체·액체)을 OmniGibson 시뮬레이터에 구현했다. [사실][^ref-971] |
| 수행 자원 | 해당 없음 |
| 제약 | 해당 없음 |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

이 사례는 활동이 일상 가정 활동이라서 현장 유형을 '가정'으로 분류했으며, 장면에는 주택뿐 아니라 정원·식당·사무실도 들어 있다. [사실][^ref-971] 실제 가정 배치가 아니라 시뮬레이션 벤치마크다.

**현장 유형:** 제조 공장

**사례:** NIST ARIAC 전기차 배터리 생산 시설 시나리오의 키팅·모듈 조립과 장애 주입(경진대회 시나리오)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 키팅과 모듈 조립 두 작업을 주문으로 받는다. [사실][^ref-1087] |
| 작업 대상 | 배터리 셀 4개를 트레이에 담는 키트, 셀 4개와 상하 케이스로 조립하는 모듈 [사실][^ref-1087] |
| 수행 자원 | 시나리오에 컨베이어·전압 시험기·진공 그리퍼가 들어 있고, 각각을 고장 대상으로 선언할 수 있다. [사실][^ref-528] |
| 제약 | 해당 없음 |
| 완료·인계 | 아직 발표되지 않은 긴급 주문이 남아 있으면 경기 상태가 '주문 완료'로 바뀌지 않는다. [사실][^ref-1087] |
| 예외·성과 | 컨베이어 고장(시작 시각·지속 시간), 전압 시험기 고장(시작·지속·대상 시험기), 진공 그리퍼 파지 실패(도구·몇 번째 파지인지), 긴급 주문(시작 시각·주문 id) 네 과제를 매개변수로 선언해 시각이나 발생 횟수 조건으로 주입한다. [사실][^ref-528] |

ARIAC는 경진대회용 시뮬레이션 시나리오이며 실제 공장 사례가 아니다. ARIAC는 장애와 긴급 요청을 매개변수로 선언해 시나리오에 주입한다. [사실][^ref-528] 예외를 시나리오 안의 선언으로 다루는 이 방식은 이 영역이 참고할 점으로 보인다. [추정][^ref-528]

**현장 유형:** 물류창고

**사례:** 2023 League of Robot Runners 경진대회의 Warehouse·Sortation 지도 시나리오(경진대회 벤치마크 시나리오이며 실제 물류창고 배치가 아니다)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 외부 작업 배정기가 에이전트가 현재 목표에 도달할 때마다 새 목표를 정확히 하나씩 주는 방식으로 작업이 생긴다. [사실][^ref-1514] |
| 작업 대상 | Warehouse 지도(140×500, 정점 38,586개)와 Sortation 지도(140×500, 정점 54,320개 — 논문 표 1 기준; 같은 논문 그림 설명은 54,230개)의 공간 [사실][^ref-1514] |
| 수행 자원 | Warehouse 지도에 에이전트 8,000, Sortation 지도에 에이전트 10,000 [사실][^ref-1514] |
| 제약 | 단계당 1초 계획 제한이 있고, 지도는 미리 주어져 30분 전처리를 허용한다. [사실][^ref-1514] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 처리량(단계당 평균 도달 목표 수)으로 겨룬다. [사실][^ref-1514] |

이 경진대회는 Amazon Robotics 가 후원한 지속형 다중 에이전트 경로 찾기 대회이며, 위 시나리오는 경진대회 벤치마크 시나리오이고 실제 물류창고 배치가 아니다(SoCS 2024 논문, 2024-04-24 기준). [사실][^ref-1514] 같은 벤치마크 계열인 Moving AI 격자 지도는 현장 사례가 아니어서 7절에 두었지만, 이 시나리오는 ARIAC 처럼 작업 발생 규칙(목표 도달 시 새 목표 1개 배정)과 계획 시간 제한을 갖춘 경진대회 시나리오이므로 사례로 세웠다.

물류창고 환경을 만드는 편집 도구로, NVIDIA 는 Isaac Sim 의 Warehouse Creator 확장이 2D 격자 배치를 Modular Warehouse 자산 묶음의 USD 창고로 바꾸는 대화형 배치 편집기이며 바닥·벽·기둥 같은 건물 요소를 생성한다고 설명하고, 문서(2026-09-18 갱신)에 로봇·랙 배치에 관한 설명은 없다. [추정] 벤더 주장[^ref-1517]

실제 물류창고 현장의 시나리오 예제와 국내 자료는 여전히 찾지 못했다. Moving AI 경로 찾기 벤치마크의 시나리오 파일과 VDMA 레이아웃 교환 형식은 현장 사례가 아니므로 7절에서 다룬다.

## 6. 대표 접근법과 기술

시나리오를 만들고 고치는 접근은 확률적 시나리오 언어, 정적 월드와 작업 명령의 분리, 건물 주석 편집기, 미션 기술 형식과 그 편집기, 언어 모델 기반 환경 생성으로 나눌 수 있다. [의견]

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 대표 접근법과 기술](../../topics/2026/2026-10-09-area33-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

시나리오 형식과 예제·벤치마크는 분야별로 따로 나뉘어 있으며, 아래 표는 이번에 확인한 형식·오픈소스·평가 프로그램을 이 영역과의 관계로 정리한 것이다. [추정][^ref-1088][^ref-104][^ref-971][^ref-528][^ref-1091]

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-10-09-area33-s7.md)에 있다.

## 8. 대표 연구와 자료

시나리오의 표현·생성·비교를 다룬 대표 연구는 확률적 시나리오 언어, 대규모 활동 라이브러리, 주행 벤치마크, 언어 모델 기반 환경 생성, 미션 기술 형식 비교로 나뉜다. [의견]

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 대표 연구와 자료](../../topics/2026/2026-10-09-area33-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

확인한 자료를 종합하면 ROP는 시나리오 모델·현장 유형별 예제 라이브러리·편집기·형식 변환을 맡고, 물리·센서 시뮬레이션 엔진과 로봇 모델, 설비 제어, 도로 교통 시나리오 표준은 참조·변환해 묶는 연계 대상으로 두는 것으로 보인다. [추정][^ref-104][^ref-528][^ref-1092][^ref-1088]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 시나리오에 어떤 로봇을 어디에 둘지(로봇 구성)를 정하고 로봇 모델을 참조로 묶는다. [추정][^ref-104][^ref-1092] | 물리·센서 시뮬레이션 엔진과 로봇 기구학·동역학·센서 모델(SDFormat 로봇 기술)은 시뮬레이터·로봇 제조사 쪽 연계 대상이다. [추정][^ref-1092] |
| 시설·설비 제어 | 승강기·문·컨베이어 같은 설비를 시나리오 요소로 선언하고 설비 장애를 시각·발생 조건으로 주입한다. [추정][^ref-104][^ref-528] | 컨베이어·작업셀 같은 설비 제어 자체는 설비 쪽 연계 대상이다. [추정][^ref-104][^ref-528] |
| 업종별 조건 | 도로 교통 시나리오 표준의 구조(정적·동적 분리, 매개변수화)를 참조 설계로 삼는다. [추정][^ref-1088] OpenSCENARIO 2 가 이동로봇 주행 시나리오 기술(Scenario Execution for Robotics, RoboVAST)에 다시 쓰이고 있으므로 로봇 시나리오의 과제·사건 기술 언어 후보로 볼 수 있으나, 근거 두 연구는 공동 저자를 공유해 독립 확인이 아니다. [추정][^ref-1512][^ref-1515][^ref-1088] | 도로 교통 시나리오 표준(OpenSCENARIO·OpenDRIVE) 자체는 ASAM 이 관리하는 자율주행 분야의 연계 대상이다. [추정][^ref-1088] |

ROP가 직접 맡을 범위는 네 가지로 보인다: 환경 참조·로봇 구성·사람 흐름·작업·정책·장애 주입을 묶은 시나리오 모델, 현장 유형별 예제 라이브러리, 시설 주석·작업·미션을 그리는 편집기와 미션 형식 선택, 시나리오를 여러 시뮬레이터 형식으로 내보내는 변환이다. [추정][^ref-104][^ref-528][^ref-079][^ref-1090][^ref-116][^ref-1092]

시나리오 모델에 판(버전)을 두는 것은 1절 리스트업이 정한 목표다. 도로 교통 시나리오 표준인 ASAM OpenSCENARIO XML 1.4.0 문서의 하위 호환성 절은 판 사이 호환 여부를 판마다 선언한다: 1.4.0 은 1.3.1 과, 1.3.1 은 1.3.0 과 완전히 호환되고, 1.2.0 은 1.1.1·1.0.0 과 호환되지만, 1.3.0 은 의미상 잘못된 시나리오를 허용하던 스키마 오류를 고쳐 1.2.0 과 완전히 호환되지 않는다(2026-10-09 확인). [사실][^ref-1511] 같은 표준은 1.2.0 시나리오 파일을 1.3.0 으로 옮기는 XSLT 이전 스크립트를 제공하고 스크립트가 경고를 내면 원래부터 잘못된 시나리오이므로 사람이 고치게 하며, 모든 판에 폐기 요소를 뺀 엄격 스키마를 두어 폐기 요소를 찾아 바꾸게 한다. [사실][^ref-1511]

따라서 개별 시나리오 파일을 형식 판 사이에서 옮기는 규칙(판별 호환 선언, 이전 스크립트, 엄격 스키마 검사)은 도로 교통 분야에서는 공개되어 있으나, 로봇 시뮬레이션 형식(SDFormat·Open-RMF 건물 파일)의 같은 규칙은 아직 확인하지 못했다. [추정][^ref-1511][^ref-1088] RoboVAST 처럼 환경 모델·추상 시나리오·변형을 나누고 인스턴스를 구체 구성으로 해석해 출처 기록과 함께 남기는 방식은 형식 판 이전 규칙과 별개로 개별 시나리오 인스턴스를 식별·재현하는 근거가 될 것으로 보이나, 단일 로봇 주행 시험 기준이라 다중 플릿·설비 시나리오에 맞는지는 확인하지 못했다(관련 질문 oq-234 는 열린 채로 둔다). [추정][^ref-1515] 그래서 로봇 시뮬레이션 형식을 참조하는 ROP 시나리오 모델의 판 관리 규칙은 아직 직접 근거 없이 설계해야 하는 부분으로 남는다. [추정][^ref-046][^ref-104][^ref-079]

연계 대상: OpenSCENARIO XML 의 판 이전 스크립트나 Open-RMF 편집기 전환 같은 외부 시나리오·건물 형식의 판 규칙은 각 형식 관리 주체의 몫이며, ROP 는 자기 시나리오 모델의 판 규칙과 참조하는 외부 형식 판의 대응을 맡을 것으로 보인다. [추정][^ref-1511][^ref-482]

경계는 제품 전략에 따라 이동할 수 있다. 이종 제조사를 연결하는 ROP는 시뮬레이터·제조사·설비 쪽 기능을 직접 만들기보다 참조·변환해 시나리오에 묶는 역할을 맡을 것으로 보인다. [추정][^ref-1092][^ref-104][^ref-528][^ref-1088] 경계 기준은 [범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 시나리오를 대화로 만드는 C. 채팅 기반 구성·운영, 시나리오를 실행·재현하는 I. 설계·시뮬레이션의 다른 영역, 시나리오에 들어가는 공간·사람·설비·작업 영역, 적용 현장인 Q. 현장 유형별 적용과 이어진다. [추정][^ref-104][^ref-116][^ref-1089]

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 다른 연구영역과의 연결](../../topics/2026/2026-10-09-area33-s10.md)에 있다.

## 11. 열린 질문

이번 실행 전 이 영역에 걸린 열린 질문은 8건이고, 이번 실행(2026-10-09-13)에서 3건을 새로 올렸으며 해결 처리한 질문은 없다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 열린 질문](../../topics/2026/2026-10-09-area33-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [33. 시나리오 모델·편집](scenario-model-and-editing.md) — 영역 심화: 3~11절 신규 작성(현장 유형 사례 5건: 상업 시설·병원·실외·가정·제조 공장), 1차 조건부 승인 수정 13건 반영, 13절 각주 15건. 2차 수정: 4절 요약 태그 [추정]으로 정정, 5절 병원·제조 공장 사례 서술의 사실·추정 분리 (실행 2026-09-30-12)
- 2026-09-30 · 생성 · [33. 시나리오 모델·편집 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area33-s7.md) — 자동 분리: 33. 시나리오 모델·편집 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,795자)을 옮겼다 (실행 2026-09-30-12)
- 2026-09-30 · 생성 · [33. 시나리오 모델·편집 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area33-s10.md) — 자동 분리: 33. 시나리오 모델·편집 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,571자)을 옮겼다 (실행 2026-09-30-12)
- 2026-09-30 · 생성 · [33. 시나리오 모델·편집 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area33-s6.md) — 자동 분리: 33. 시나리오 모델·편집 의 "6. 대표 접근법과 기술" 절(1,360자)을 옮겼다 (실행 2026-09-30-12)
- 2026-09-30 · 생성 · [33. 시나리오 모델·편집 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area33-s4.md) — 자동 분리: 33. 시나리오 모델·편집 의 "4. 핵심 개념과 용어" 절(1,249자)을 옮겼다. 2차 수정: 세 줄 요약·본문 첫 문장 태그를 [사실]에서 [추정]으로 정정 (실행 2026-09-30-12)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-1086]: Vin, E., Kashiwa, S., Rhea, M., Fremont, D. J., Kim, E., Dreossi, T., Ghosh, S., Yue, X., Sangiovanni-Vincentelli, A. L., & Seshia, S. A. (CAV 2023, arXiv), 3D Environment Modeling for Falsification and Beyond with Scenic 3.0, 2023-07, https://arxiv.org/abs/2307.03325, 접근일 2026-09-30
[^ref-104]: Open-RMF (open-rmf/rmf_demos), rmf_demos — README, 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-30
[^ref-079]: Open Robotics (osrf/ros2multirobotbook), Programming Multiple Robots with ROS 2 — Traffic Editor, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-30
[^ref-971]: Li, C., Zhang, R., Wong, J. 외 (Stanford, arXiv), BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation, 2024-03, https://arxiv.org/abs/2403.09227, 접근일 2026-09-30
[^ref-528]: NIST (usnistgov/ARIAC_docs), ARIAC Documentation — Challenges, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html, 접근일 2026-09-30
[^ref-1087]: NIST (usnistgov/ARIAC_docs), ARIAC Documentation — Scenario, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/scenario.html, 접근일 2026-09-30
[^ref-1088]: ASAM e.V., ASAM OpenSCENARIO® XML, 미확인, https://www.asam.net/standards/detail/openscenario-xml/, 접근일 2026-09-30
[^ref-726]: Kästner, L., Bhuiyan, T., Le, T. A. 외 (RA-L 2022, arXiv), Arena-Bench: A Benchmarking Suite for Obstacle Avoidance Approaches in Highly Dynamic Environments, 2022-06, https://arxiv.org/abs/2206.05728, 접근일 2026-09-30
[^ref-1089]: Shcherbyna, V. 외 (arXiv), Arena 4.0: A Comprehensive ROS2 Development and Benchmarking Platform for Human-centric Navigation Using Generative-Model-based Environment Generation, 2024-09, https://arxiv.org/abs/2409.12471, 접근일 2026-09-30
[^ref-1090]: BehaviorTree.CPP 프로젝트 (behaviortree.dev), Groot2, 미확인, https://www.behaviortree.dev/groot/, 접근일 2026-09-30
[^ref-116]: Filippone, G., Pettinari, S., & Pelliccione, P. (IEEE TSE, arXiv), Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis, 2026-03, https://arxiv.org/abs/2603.15427, 접근일 2026-09-30
[^ref-1091]: Moving AI Lab (Sturtevant 외), MAPF Benchmarks, 미확인, https://movingai.com/benchmarks/mapf/index.html, 접근일 2026-09-30
[^ref-1092]: Open Source Robotics Foundation, SDFormat (Simulation Description Format), 미확인, http://sdformat.org/, 접근일 2026-09-30
[^ref-046]: VDMA (Intralogistics-2X-LIF), Layout Interchange Format (LIF) — README, 2023-09, https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format, 접근일 2026-09-30

[^ref-482]: Open-RMF (open-rmf/rmf_site), rmf_site — RMF Site Editor (README), 미확인, https://github.com/open-rmf/rmf_site, 접근일 2026-10-09
[^ref-1511]: ASAM e.V., ASAM OpenSCENARIO XML v1.4.0 — 5 Backward compatibility, 미확인, https://openscenario.asam.net/ASAM_OpenSCENARIO_XML/v1.4.0/05_backward_compatibility/01_backward_compatibility.html, 접근일 2026-10-09
[^ref-1512]: Pasch, F., Mirus, F., Zhang, Y., & Scholl, K.-U. (Intel Labs 외, arXiv), Scenario Execution for Robotics: A generic, backend-agnostic library for running reproducible robotics experiments and tests, 2024-09-11, https://arxiv.org/abs/2409.07080, 접근일 2026-10-09
[^ref-1514]: Jiang, H., Zhang, Y., Veerapaneni, R., & Li, J. (SoCS 2024, arXiv), Scaling Lifelong Multi-Agent Path Finding to More Realistic Settings: Research Challenges and Opportunities, 2024-04-24, https://arxiv.org/abs/2404.16162, 접근일 2026-10-09
[^ref-1515]: Ortega, A., Wiest, S., Pasch, F., & Hochgeschwender, N. (arXiv, ERAS 2026 채택), Replicable Simulation-Based Robot Validation through Provenance, 2026-05-28, https://arxiv.org/abs/2605.29973, 접근일 2026-10-09
[^ref-1517]: NVIDIA, Isaac Sim Documentation — Warehouse Creator Extension, 미확인, https://docs.isaacsim.omniverse.nvidia.com/latest/assets/asset_utilities/ext_omni_warehouse_creator.html, 접근일 2026-10-09
```

### docs/categories/design-and-simulation/scenario-model-and-editing.md

```markdown
---
title: "33. 시나리오 모델·편집"
type: area
category: "I. 설계·시뮬레이션"
area_no: 33
related_areas: [9, 11, 14, 15, 18, 19, 22, 24, 27, 32, 34, 36, 44, 54, 62, 63, 64, 65, 66]
tags: [시나리오 형식, OpenSCENARIO, Open-RMF, 장애 주입, 시나리오 라이브러리, 미션 기술 형식]
status: published
confidence: low
created: 2026-09-28
updated: 2026-09-30
sources: [ref-1086, ref-104, ref-079, ref-971, ref-528, ref-1087, ref-1088, ref-726, ref-1089, ref-815, ref-1090, ref-116, ref-1091, ref-1092, ref-046]
last_run: 2026-09-30
version: 2
---

[홈](../../index.md) › [I. 설계·시뮬레이션](index.md) › 33. 시나리오 모델·편집

# 33. 시나리오 모델·편집

!!! info "소속 대분류"
    [I. 설계·시뮬레이션](index.md) — 핵심 질문:
    현장을 바꾸거나 로봇을 늘리기 전에 가상으로 설계하고 결과를 미리 볼 수 있는가? [분류원문]

<!-- auto:area-tracks:start -->
<!-- auto:area-tracks:end -->

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: low · 페이지 버전: 2 · 마지막 갱신: 2026-09-30 · 마지막 실행: 2026-09-30
<!-- auto:page-status:end -->

## 1. 한 줄 정의

시나리오 형식, 예제 라이브러리, 시나리오·워크플로 편집기 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **시나리오 모델·형식**: 환경·로봇·사람·물품·작업·정책·물리·장애를 담는 버전 있는 시나리오 형식을 정한다
- **시나리오 라이브러리**: 현장 유형별 예제·템플릿(아파트·공장·호텔·물류 시설 등)을 모아 다시 쓴다
- **시나리오·워크플로 편집기**: 사람이 직접 시나리오와 워크플로를 화면에서 그리고 고친다(노코드 편집)

## 2. 핵심 질문

현장·로봇·사람·작업을 담은 시나리오를 어떻게 표현하고 다시 쓸 것인가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

## 3. 왜 중요한가

시나리오를 정해진 형식으로 표현해 두지 않으면 계획기·정책을 같은 조건에서 비교하거나 장애·긴급 요청 대응 시험을 반복하기 어렵고, 조건마다 시나리오 파일이 불어나며, 미션과 환경을 정의할 도메인 전문가가 쓸 공통 형식도 없다는 것이 확인한 자료의 종합이다. [추정][^ref-726][^ref-1091][^ref-528][^ref-1088][^ref-116]

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 왜 중요한가](../../topics/2026/2026-09-30-area33-s3.md)에 있다.

## 4. 핵심 개념과 용어

시나리오를 표현하는 형식들은 정적 환경과 동적 내용을 나누고, 매개변수·확률 분포·장애 선언으로 한 시나리오를 여러 조건에 다시 쓰게 한다. [추정][^ref-1088][^ref-1086][^ref-528]

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area33-s4.md)에 있다.

## 5. 적용 사례 (현장 유형 명시)

아래 다섯 사례는 모두 실제 현장 배치가 아니라 공개된 시뮬레이션 예제 월드·벤치마크·경진대회 시나리오를 여섯 항목으로 정리한 것이며, 이 영역에서는 각 시나리오가 무엇을 어떤 단위로 담았는지를 본다. [사실][^ref-104][^ref-971][^ref-1087]

**현장 유형:** 상업 시설

**사례:** Open-RMF 예제 호텔·공항 터미널 월드의 다중 플릿 순찰·청소 시나리오(시뮬레이션 예제 월드)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 월드를 띄운 뒤 dispatch_clean·dispatch_patrol 같은 작업 명령을 따로 넣으면 작업이 생긴다. [사실][^ref-104] |
| 작업 대상 | 호텔 월드의 로비와 객실 2개 층 공간을 순찰(loop)·청소한다(예제 명령은 로비 청소). [사실][^ref-104] |
| 수행 자원 | 호텔 월드에는 로봇 플릿 3개(로봇 4대), 승강기 2대, 여러 문이 있고, 디스패처가 [플릿 어댑터](../../glossary/fleet-adapter.md)들 사이의 작업 입찰을 조율한다. [사실][^ref-104] |
| 제약 | 공항 터미널 월드는 차선·목적지·로봇이 많은 대형 지도에 선택적으로 군중 시뮬레이션과 사람이 모는 읽기 전용(read_only) 카트를 더해 순찰·배송·청소를 실행한다. [사실][^ref-104] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

rmf_demos의 시나리오는 건물 구성(차선·승강기·문·충전 위치)을 담은 월드를 띄운 뒤 작업을 명령으로 따로 넣는 구조다(2026-09-30 확인). [사실][^ref-104] 호텔·공항 터미널 모두 시뮬레이션 예제 월드이며 실제 시설의 도입 사례가 아니다.

**현장 유형:** 병원

**사례:** Open-RMF 예제 클리닉 월드에서 두 층의 간호 스테이션 사이 순찰(시뮬레이션 예제 월드)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 순찰 명령(dispatch_patrol)으로 작업을 넣는다. 예제 명령은 1층과 2층의 간호 스테이션을 순찰 지점으로 지정한다. [사실][^ref-104] |
| 작업 대상 | 두 층에 걸친 간호 스테이션 사이의 순찰 경로(공간) [사실][^ref-104] |
| 수행 자원 | 역할이 다른 로봇 플릿 2개와 승강기 2대 [사실][^ref-104] |
| 제약 | 로봇이 승강기 2대가 있는 2개 층 시설에서 층을 오가며 순찰해야 한다. [사실][^ref-104] |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

클리닉 월드는 병원형 시나리오 예제이며 실제 병원 배치 사례가 아니다. 이 월드는 승강기 2대가 있는 2개 층 시설이고, 로봇이 층을 오가며 순찰한다. [사실][^ref-104] 층간 이동이 승강기를 거친다는 점에서 이 예제는 설비를 시나리오 요소로 담는 예로 볼 수 있다. [추정][^ref-104]

**현장 유형:** 실외

**사례:** Open-RMF 예제 캠퍼스 월드의 배송 로봇 장거리 순찰(시뮬레이션 예제 월드)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 작업 명령으로 장거리 순찰을 넣는다. [사실][^ref-104] |
| 작업 대상 | 차선을 GPS WGS84 좌표로 행성 규모에 주석한 넓은 캠퍼스 공간 [사실][^ref-104] |
| 수행 자원 | 여러 대의 배송 로봇 [사실][^ref-104] |
| 제약 | 해당 없음 |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

캠퍼스 월드는 실내 층 좌표 대신 지구 좌표로 공간을 주석한 실외 시나리오 예제다. [사실][^ref-104] 같은 예제 모음의 제조·물류 월드는 영상 데모뿐이라 사례로 세우지 않고 7절에서만 다룬다.

**현장 유형:** 가정

**사례:** BEHAVIOR-1K의 일상 가정 활동 라이브러리(벤치마크)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 해당 없음 |
| 작업 대상 | '로봇이 무엇을 해 주길 바라는가' 설문으로 고른 일상 가정 활동 1,000개를 BDDL로 명세하고, 장면 50개와 물리·의미 속성을 주석한 객체 9,000개 이상(강체·변형체·액체)을 OmniGibson 시뮬레이터에 구현했다. [사실][^ref-971] |
| 수행 자원 | 해당 없음 |
| 제약 | 해당 없음 |
| 완료·인계 | 해당 없음 |
| 예외·성과 | 해당 없음 |

이 사례는 활동이 일상 가정 활동이라서 현장 유형을 '가정'으로 분류했으며, 장면에는 주택뿐 아니라 정원·식당·사무실도 들어 있다. [사실][^ref-971] 실제 가정 배치가 아니라 시뮬레이션 벤치마크다.

**현장 유형:** 제조 공장

**사례:** NIST ARIAC 전기차 배터리 생산 시설 시나리오의 키팅·모듈 조립과 장애 주입(경진대회 시나리오)

| 항목 | 내용 |
|---|---|
| 시작 조건 | 키팅과 모듈 조립 두 작업을 주문으로 받는다. [사실][^ref-1087] |
| 작업 대상 | 배터리 셀 4개를 트레이에 담는 키트, 셀 4개와 상하 케이스로 조립하는 모듈 [사실][^ref-1087] |
| 수행 자원 | 시나리오에 컨베이어·전압 시험기·진공 그리퍼가 들어 있고, 각각을 고장 대상으로 선언할 수 있다. [사실][^ref-528] |
| 제약 | 해당 없음 |
| 완료·인계 | 아직 발표되지 않은 긴급 주문이 남아 있으면 경기 상태가 '주문 완료'로 바뀌지 않는다. [사실][^ref-1087] |
| 예외·성과 | 컨베이어 고장(시작 시각·지속 시간), 전압 시험기 고장(시작·지속·대상 시험기), 진공 그리퍼 파지 실패(도구·몇 번째 파지인지), 긴급 주문(시작 시각·주문 id) 네 과제를 매개변수로 선언해 시각이나 발생 횟수 조건으로 주입한다. [사실][^ref-528] |

ARIAC는 경진대회용 시뮬레이션 시나리오이며 실제 공장 사례가 아니다. ARIAC는 장애와 긴급 요청을 매개변수로 선언해 시나리오에 주입한다. [사실][^ref-528] 예외를 시나리오 안의 선언으로 다루는 이 방식은 이 영역이 참고할 점으로 보인다. [추정][^ref-528]

물류창고 현장의 시나리오 예제·템플릿 사례는 이번 조사에서 찾지 못했다. 경로 찾기 벤치마크의 시나리오 파일과 VDMA 레이아웃 교환 형식은 현장 사례가 아니므로 7절에서 다룬다. 국내 자료도 찾지 못했다.

## 6. 대표 접근법과 기술

시나리오를 만들고 고치는 접근은 확률적 시나리오 언어, 정적 월드와 작업 명령의 분리, 건물 주석 편집기, 미션 기술 형식과 그 편집기, 언어 모델 기반 환경 생성으로 나눌 수 있다. [의견]

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area33-s6.md)에 있다.

## 7. 관련 표준·프레임워크·오픈소스

시나리오 형식과 예제·벤치마크는 분야별로 따로 나뉘어 있으며, 아래 표는 이번에 확인한 형식·오픈소스·평가 프로그램을 이 영역과의 관계로 정리한 것이다. [추정][^ref-1088][^ref-104][^ref-971][^ref-528][^ref-1091]

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area33-s7.md)에 있다.

## 8. 대표 연구와 자료

시나리오의 표현·생성·비교를 다룬 대표 연구는 확률적 시나리오 언어, 대규모 활동 라이브러리, 주행 벤치마크, 언어 모델 기반 환경 생성, 미션 기술 형식 비교로 나뉜다. [의견]

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 대표 연구와 자료](../../topics/2026/2026-09-30-area33-s8.md)에 있다.

## 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)

확인한 자료를 종합하면 ROP는 시나리오 모델·현장 유형별 예제 라이브러리·편집기·형식 변환을 맡고, 물리·센서 시뮬레이션 엔진과 로봇 모델, 설비 제어, 도로 교통 시나리오 표준은 참조·변환해 묶는 연계 대상으로 두는 것으로 보인다. [추정][^ref-104][^ref-528][^ref-1092][^ref-1088]

| 경계 | ROP가 직접 맡는 것 | 외부와 연계하는 것 |
|---|---|---|
| 로봇 자체 지능·제어 | 시나리오에 어떤 로봇을 어디에 둘지(로봇 구성)를 정하고 로봇 모델을 참조로 묶는다. [추정][^ref-104][^ref-1092] | 물리·센서 시뮬레이션 엔진과 로봇 기구학·동역학·센서 모델(SDFormat 로봇 기술)은 시뮬레이터·로봇 제조사 쪽 연계 대상이다. [추정][^ref-1092] |
| 시설·설비 제어 | 승강기·문·컨베이어 같은 설비를 시나리오 요소로 선언하고 설비 장애를 시각·발생 조건으로 주입한다. [추정][^ref-104][^ref-528] | 컨베이어·작업셀 같은 설비 제어 자체는 설비 쪽 연계 대상이다. [추정][^ref-104][^ref-528] |
| 업종별 조건 | 도로 교통 시나리오 표준의 구조(정적·동적 분리, 매개변수화)를 참조 설계로 삼는다. [추정][^ref-1088] | 도로 교통 시나리오 표준(OpenSCENARIO·OpenDRIVE)은 자율주행 분야의 연계 대상이다. [추정][^ref-1088] |

ROP가 직접 맡을 범위는 네 가지로 보인다: 환경 참조·로봇 구성·사람 흐름·작업·정책·장애 주입을 묶은 시나리오 모델, 현장 유형별 예제 라이브러리, 시설 주석·작업·미션을 그리는 편집기와 미션 형식 선택, 시나리오를 여러 시뮬레이터 형식으로 내보내는 변환이다. [추정][^ref-104][^ref-528][^ref-079][^ref-1090][^ref-116][^ref-1092]

시나리오 모델에 판(버전)을 두는 것은 1절 리스트업이 정한 목표다. 개별 시나리오 인스턴스의 버전 관리 방식은 확인한 공개 자료에서 찾지 못했으므로, 판 관리 규칙은 아직 근거 없이 설계해야 하는 부분이다. [추정][^ref-1088][^ref-046][^ref-104][^ref-079]

경계는 제품 전략에 따라 이동할 수 있다. 이종 제조사를 연결하는 ROP는 시뮬레이터·제조사·설비 쪽 기능을 직접 만들기보다 참조·변환해 시나리오에 묶는 역할을 맡을 것으로 보인다. [추정][^ref-1092][^ref-104][^ref-528][^ref-1088] 경계 기준은 [범위 경계](../../about/scope-boundary.md)에 있다.

## 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)

이 영역은 시나리오를 대화로 만드는 C. 채팅 기반 구성·운영, 시나리오를 실행·재현하는 I. 설계·시뮬레이션의 다른 영역, 시나리오에 들어가는 공간·사람·설비·작업 영역, 적용 현장인 Q. 현장 유형별 적용과 이어진다. [추정][^ref-104][^ref-116][^ref-1089]

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area33-s10.md)에 있다.

## 11. 열린 질문

이 영역에 걸린 열린 질문은 기존 2건과 이번 실행에서 새로 올린 4건이며, 기존 2건은 이번 조사에서도 해결 근거를 찾지 못했다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

자세한 내용은 주제 페이지 [33. 시나리오 모델·편집 — 열린 질문](../../topics/2026/2026-09-30-area33-s11.md)에 있다.

## 12. 최근 업데이트 (자동)

<!-- auto:area-recent:start -->
- 2026-09-30 · 갱신 · [33. 시나리오 모델·편집](scenario-model-and-editing.md) — 영역 심화: 3~11절 신규 작성(현장 유형 사례 5건: 상업 시설·병원·실외·가정·제조 공장), 1차 조건부 승인 수정 13건 반영, 13절 각주 15건. 2차 수정: 4절 요약 태그 [추정]으로 정정, 5절 병원·제조 공장 사례 서술의 사실·추정 분리 (실행 2026-09-30-12)
- 2026-09-30 · 생성 · [33. 시나리오 모델·편집 — 관련 표준·프레임워크·오픈소스](../../topics/2026/2026-09-30-area33-s7.md) — 자동 분리: 33. 시나리오 모델·편집 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,795자)을 옮겼다 (실행 2026-09-30-12)
- 2026-09-30 · 생성 · [33. 시나리오 모델·편집 — 다른 연구영역과의 연결](../../topics/2026/2026-09-30-area33-s10.md) — 자동 분리: 33. 시나리오 모델·편집 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(1,571자)을 옮겼다 (실행 2026-09-30-12)
- 2026-09-30 · 생성 · [33. 시나리오 모델·편집 — 대표 접근법과 기술](../../topics/2026/2026-09-30-area33-s6.md) — 자동 분리: 33. 시나리오 모델·편집 의 "6. 대표 접근법과 기술" 절(1,360자)을 옮겼다 (실행 2026-09-30-12)
- 2026-09-30 · 생성 · [33. 시나리오 모델·편집 — 핵심 개념과 용어](../../topics/2026/2026-09-30-area33-s4.md) — 자동 분리: 33. 시나리오 모델·편집 의 "4. 핵심 개념과 용어" 절(1,249자)을 옮겼다. 2차 수정: 세 줄 요약·본문 첫 문장 태그를 [사실]에서 [추정]으로 정정 (실행 2026-09-30-12)
<!-- auto:area-recent:end -->

## 13. 참고 자료 (각주)

[^ref-1086]: Vin, E., Kashiwa, S., Rhea, M., Fremont, D. J., Kim, E., Dreossi, T., Ghosh, S., Yue, X., Sangiovanni-Vincentelli, A. L., & Seshia, S. A. (CAV 2023, arXiv), 3D Environment Modeling for Falsification and Beyond with Scenic 3.0, 2023-07, https://arxiv.org/abs/2307.03325, 접근일 2026-09-30
[^ref-104]: Open-RMF (open-rmf/rmf_demos), rmf_demos — README, 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-30
[^ref-079]: Open Robotics (osrf/ros2multirobotbook), Programming Multiple Robots with ROS 2 — Traffic Editor, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-30
[^ref-971]: Li, C., Zhang, R., Wong, J. 외 (Stanford, arXiv), BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation, 2024-03, https://arxiv.org/abs/2403.09227, 접근일 2026-09-30
[^ref-528]: NIST (usnistgov/ARIAC_docs), ARIAC Documentation — Challenges, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html, 접근일 2026-09-30
[^ref-1087]: NIST (usnistgov/ARIAC_docs), ARIAC Documentation — Scenario, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/scenario.html, 접근일 2026-09-30
[^ref-1088]: ASAM e.V., ASAM OpenSCENARIO® XML, 미확인, https://www.asam.net/standards/detail/openscenario-xml/, 접근일 2026-09-30
[^ref-726]: Kästner, L., Bhuiyan, T., Le, T. A. 외 (RA-L 2022, arXiv), Arena-Bench: A Benchmarking Suite for Obstacle Avoidance Approaches in Highly Dynamic Environments, 2022-06, https://arxiv.org/abs/2206.05728, 접근일 2026-09-30
[^ref-1089]: Shcherbyna, V. 외 (arXiv), Arena 4.0: A Comprehensive ROS2 Development and Benchmarking Platform for Human-centric Navigation Using Generative-Model-based Environment Generation, 2024-09, https://arxiv.org/abs/2409.12471, 접근일 2026-09-30
[^ref-1090]: BehaviorTree.CPP 프로젝트 (behaviortree.dev), Groot2, 미확인, https://www.behaviortree.dev/groot/, 접근일 2026-09-30
[^ref-116]: Filippone, G., Pettinari, S., & Pelliccione, P. (IEEE TSE, arXiv), Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis, 2026-03, https://arxiv.org/abs/2603.15427, 접근일 2026-09-30
[^ref-1091]: Moving AI Lab (Sturtevant 외), MAPF Benchmarks, 미확인, https://movingai.com/benchmarks/mapf/index.html, 접근일 2026-09-30
[^ref-1092]: Open Source Robotics Foundation, SDFormat (Simulation Description Format), 미확인, http://sdformat.org/, 접근일 2026-09-30
[^ref-046]: VDMA (Intralogistics-2X-LIF), Layout Interchange Format (LIF) — README, 2023-09, https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format, 접근일 2026-09-30
```

### runs/2026-10-09-13/pages/topics/2026/2026-10-09-area33-s6.md

```markdown
---
title: "33. 시나리오 모델·편집 — 대표 접근법과 기술"
type: topic
category: "I. 설계·시뮬레이션"
primary_area_no: 33
related_areas: [9, 11, 14, 15, 18, 19, 22, 24, 27, 32, 34, 36, 44, 54, 57, 61, 62, 63, 64, 65, 66]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-079, ref-116, ref-1510, ref-1512, ref-1515, ref-1516, ref-1518, ref-482, ref-528]
last_run: 2026-10-09
version: 1
split_from: docs/categories/design-and-simulation/scenario-model-and-editing.md#6
---

[홈](../../index.md) › [주제](../index.md) › 33. 시나리오 모델·편집 — 대표 접근법과 기술

# 33. 시나리오 모델·편집 — 대표 접근법과 기술

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 시나리오를 만들고 고치는 접근은 확률적 시나리오 언어, 정적 월드와 작업 명령의 분리, 건물 주석 편집기, 미션 기술 형식과 그 편집기, 언어 모델 기반 환경 생성으로 나눌 수 있다. [의견]
- 이 페이지는 [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md) 페이지의 "대표 접근법과 기술" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md) 페이지를 쓰는 과정에서 "대표 접근법과 기술" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

시나리오를 만들고 고치는 접근은 확률적 시나리오 언어, 정적 월드와 작업 명령의 분리, 건물 주석 편집기, 미션 기술 형식과 그 편집기, 언어 모델 기반 환경 생성으로 나눌 수 있다. [의견]


2026-09-30 실행까지 정리한 내용은 [33. 시나리오 모델·편집 — 대표 접근법과 기술 (2026-09-30)](2026-09-30-area33-s6.md)에 있다.

### 2026-10-09 갱신에서 더한 접근

**시설 주석 편집기의 전환.** Open-RMF 상호운용 그룹 공지(2024-06-05)는 Site Editor 를 예전 traffic-editor 를 대체하는 도구로 소개하고, 시각화·시뮬레이션용 3D 환경, 환경 안의 로봇, 로봇 교통 규칙, 승강기와 문을 편집 대상으로 들었다. [사실][^ref-1510] Site Editor(rmf_site)는 Rust 와 Bevy 게임 엔진으로 만든 대규모 RMF 배치 현장 시각화·편집 도구로 데스크톱과 웹(WebAssembly)에서 돌며, rmf_site_ros2 의 rmf_site_cmake 가 Site Editor 프로젝트에서 시뮬레이션과 주행 그래프를 생성한다(2026-10-09 확인). [사실][^ref-482] traffic-editor 문서는 편집기의 목표를 여러 플릿의 의도를 제조사 중립 방식으로 표현하고 실제 환경을 반영한 3D 시뮬레이션 월드를 생성하는 것으로 밝히면서, 다음 판은 영상 좌표 대신 데카르트 좌표나 위경도 좌표를 기본으로 하려 하나 일정은 정해지지 않았다고 적는다. [사실][^ref-079] 그래서 ROP 시나리오 모델이 건물 파일을 환경 참조로 묶는다면 편집기·건물 형식 전환에 따른 참조 이전 규칙이 함께 필요할 것으로 보이며, 기존 .building.yaml 을 Site Editor 형식으로 옮기는 공식 방법은 확인하지 못했다(세 출처 모두 Open-RMF 쪽 자료라 독립 확인이 아니다). [추정][^ref-482][^ref-1510][^ref-079]

**도로 교통 시나리오 언어의 로봇 재사용.** Pasch 외(Intel Labs 외, 2024-09)의 Scenario Execution for Robotics 는 [ASAM OpenSCENARIO](../../glossary/asam-openscenario.md) 2 로 쓴 로봇 시나리오를 구문 분석해 [행동 트리](../../glossary/behavior-tree.md)(PyTrees)로 바꿔 실행하는 백엔드·미들웨어 독립 파이썬 라이브러리이며, Gazebo·Nav2·PyBullet 라이브러리를 두고 매개변수 값 목록을 조합마다 하나의 실행 시나리오로 펼친다. [사실][^ref-1512] 저자들은 시뮬레이션과 실물 실험에서 위치 데이터만 바꾼 같은 시나리오 파일을 썼다고 보고했다. [사실][^ref-1512]

**환경·추상 시나리오·변형의 분리.** Ortega·Wiest·Pasch·Hochgeschwender(2026-05, ERAS 2026 채택)가 확장한 시험 틀 RoboVAST 는 환경을 FloorPlan 모델(.fpm), 과제를 OpenSCENARIO DSL 의 추상 시나리오, 시작·목표 자세·장애물 수·센서 잡음·설정 파일을 변형 파일(.vast)로 나누고, 각 인스턴스를 모든 값이 정해진 구체 시험 구성(scenario.config)으로 해석한 뒤 실행마다 해석된 매개변수·rosbag·시각·합격 여부·결정적 실행 식별자를 남긴다. [사실][^ref-1515] 기존 모델에 의미를 덧붙이는 조합형 실행 시나리오 연구는 원 페이지 [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md)의 8. 대표 연구와 자료에 정리했다.

**장애를 시나리오 매개변수로 선언.** 아래는 시나리오에 [장애 주입](../../glossary/fault-injection.md)을 매개변수로 선언하는 방식의 예이며, 센서·메시지 수준 장애 주입 자체는 로봇 자체 지능·제어 쪽 연계 대상이라 ROP가 직접 만드는 기능으로 다루지 않는다. Scenario Execution 연구는 2D 라이다 스캔에 가우시안 잡음을 더하거나 검출을 무작위로 빼는 ROS 2 노드로 장애를 주입하고 잡음 크기와 누락 비율을 시나리오 매개변수로 두었으며, 장애 수준이 높아질수록 AMCL 위치추정 오차가 커지는 것을 기능 시연으로 보였다. [사실][^ref-1512] ros2_fault_injection 은 ROS 2 의 토픽·변환(TF)·서비스에 장애를 주입하는 프레임워크로, 오도메트리·LaserScan·관절 상태·IMU·TF·Twist·트리거 서비스·점군 장애 유형을 두고 문서에 단언(assertion)과 pluginlib 기반 주입기 팩토리 절을 둔다(관리 주체·판 미확인, 2026-10-09 확인). [사실][^ref-1518] 확인한 장애 선언은 ARIAC 의 설비·도구 장애(시작 시각·지속 시간·발생 횟수 매개변수), Scenario Execution 의 센서 잡음 매개변수, ros2_fault_injection 의 메시지 단위 장애로 나뉘며, 여러 제조사 로봇 플릿과 승강기·문 같은 설비 장애를 한 형식으로 선언하는 사례는 이번에도 찾지 못했다. [추정][^ref-528][^ref-1512][^ref-1518]

이번에 확인한 자료를 더하면, 로봇 쪽에서도 환경 모델·추상 시나리오·변형을 나누고 구체 인스턴스를 해석·기록하는 도구와 자율주행 시나리오 언어의 재사용이 나타나지만, 환경·로봇·사람·물품·작업·정책·물리·장애를 한 형식으로 담는 공통 표준은 여전히 확인하지 못한 것으로 보인다. [추정][^ref-1515][^ref-1512][^ref-1516][^ref-116]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/design-and-simulation/scenario-model-and-editing.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/design-and-simulation/scenario-model-and-editing.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md)
- 관련 영역: [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/design-and-simulation/scenario-model-and-editing.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-079]: Open Robotics (osrf/ros2multirobotbook), Programming Multiple Robots with ROS 2 — Traffic Editor, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-30
[^ref-116]: Filippone, G., Pettinari, S., & Pelliccione, P. (IEEE TSE, arXiv), Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis, 2026-03, https://arxiv.org/abs/2603.15427, 접근일 2026-09-30
[^ref-1510]: Open Robotics Discourse (Open-RMF 상호운용 그룹, 작성자 grey), Interoperability Interest Group June 6, 2024: Preview of the RMF Site Editor, 2024-06-05, https://discourse.openrobotics.org/t/interoperability-interest-group-june-6-2024-preview-of-the-rmf-site-editor/38070, 접근일 2026-10-09
[^ref-1512]: Pasch, F., Mirus, F., Zhang, Y., & Scholl, K.-U. (Intel Labs 외, arXiv), Scenario Execution for Robotics: A generic, backend-agnostic library for running reproducible robotics experiments and tests, 2024-09-11, https://arxiv.org/abs/2409.07080, 접근일 2026-10-09
[^ref-1515]: Ortega, A., Wiest, S., Pasch, F., & Hochgeschwender, N. (arXiv, ERAS 2026 채택), Replicable Simulation-Based Robot Validation through Provenance, 2026-05-28, https://arxiv.org/abs/2605.29973, 접근일 2026-10-09
[^ref-1516]: Ortega, A., Parra, S., Schneider, S., & Hochgeschwender, N. (Frontiers in Robotics and AI 11), Composable and executable scenarios for simulation-based testing of mobile robots, 2024-08-02, https://pmc.ncbi.nlm.nih.gov/articles/PMC11327003/, 접근일 2026-10-09
[^ref-1518]: ros2_fault_injection 프로젝트 (Read the Docs), ros2_fault_injection documentation, 미확인, https://ros2-fault-injection.readthedocs.io/, 접근일 2026-10-09
[^ref-482]: Open-RMF (open-rmf/rmf_site), rmf_site — RMF Site Editor (README), 미확인, https://github.com/open-rmf/rmf_site, 접근일 2026-10-09
[^ref-528]: NIST (usnistgov/ARIAC_docs), ARIAC Documentation — Challenges, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-09-13 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-09 | 2026-10-09-13 | 33. 시나리오 모델·편집 의 "대표 접근법과 기술" 절에서 분리 |
```

### runs/2026-10-09-13/pages/topics/2026/2026-10-09-area33-s8.md

```markdown
---
title: "33. 시나리오 모델·편집 — 대표 연구와 자료"
type: topic
category: "I. 설계·시뮬레이션"
primary_area_no: 33
related_areas: [9, 11, 14, 15, 18, 19, 22, 24, 27, 32, 34, 36, 44, 54, 57, 61, 62, 63, 64, 65, 66]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-1512, ref-1513, ref-1514, ref-1515, ref-1516, ref-1519]
last_run: 2026-10-09
version: 1
split_from: docs/categories/design-and-simulation/scenario-model-and-editing.md#8
---

[홈](../../index.md) › [주제](../index.md) › 33. 시나리오 모델·편집 — 대표 연구와 자료

# 33. 시나리오 모델·편집 — 대표 연구와 자료

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 시나리오의 표현·생성·비교를 다룬 대표 연구는 확률적 시나리오 언어, 대규모 활동 라이브러리, 주행 벤치마크, 언어 모델 기반 환경 생성, 미션 기술 형식 비교로 나뉜다. [의견]
- 이 페이지는 [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md) 페이지의 "대표 연구와 자료" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md) 페이지를 쓰는 과정에서 "대표 연구와 자료" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

시나리오의 표현·생성·비교를 다룬 대표 연구는 확률적 시나리오 언어, 대규모 활동 라이브러리, 주행 벤치마크, 언어 모델 기반 환경 생성, 미션 기술 형식 비교로 나뉜다. [의견]


2026-09-30 실행까지 정리한 내용은 [33. 시나리오 모델·편집 — 대표 연구와 자료 (2026-09-30)](2026-09-30-area33-s8.md)에 있다.

### 2026-10-09 갱신에서 더한 연구

- Ortega, A., Parra, S., Schneider, S., Hochgeschwender, N., Composable and executable scenarios for simulation-based testing of mobile robots(Frontiers in Robotics and AI 11, 2024-08-02) — 기존 모델을 고치지 않고 동적 문·다른 과제 명세 같은 의미를 덧붙이는 조합형 실행 시나리오를 제안해 점유 격자 지도·3D 메시·Gazebo 월드·주행 경유점을 생성했고, 정적 시험·무작위로 움직이는 문·로봇이 다가오면 닫히는 문의 세 시나리오로 공개 주행 스택에서 1년 넘게 드러나지 않은 설정 오류를 찾았다. [사실][^ref-1516] 면담 근거는 원 페이지 [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md)의 3. 왜 중요한가에 있다.
- Ortega, A., Wiest, S., Pasch, F., Hochgeschwender, N., Replicable Simulation-Based Robot Validation through Provenance(arXiv 2605.29973, 2026-05-28, ERAS 2026 채택) — 시험 산출물 사이의 관계를 W3C PROV(PROV-O)를 핵심 메타모델로 DCAT·Dublin Core·QUDT 와 함께 JSON-LD 로 기록해 SPARQL 로 질의하게 했으며, 저자들은 이 메타모델이 일반화하기 어려울 수 있고 로봇 분야 공동 어휘가 없다고 한계를 밝혔다. [사실][^ref-1515]
- Pasch, F., Mirus, F., Zhang, Y., Scholl, K.-U.(Intel Labs 외), Scenario Execution for Robotics(arXiv 2409.07080, 2024-09-11) — 자율주행 시나리오 언어 OpenSCENARIO 2 를 로봇 시험 시나리오 기술에 쓰는 라이브러리로, 원 페이지 [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md)의 6. 대표 접근법과 기술에 요약했다. [사실][^ref-1512]
- Elmaaroufi, K. 외, ScenicNL(COLM 2024) — 여러 대규모 언어 모델 프롬프트를 컴파일러·시뮬레이터와 엮어, 세부가 불확실한 경찰 사고 보고서(최근 5년 캘리포니아 자율주행차 사고 보고)를 불확실성을 확률 분포로 담은 Scenic 시나리오 프로그램으로 바꿨다(도로 교통 분야). [사실][^ref-1513]
- Jiang, H., Zhang, Y., Veerapaneni, R., Li, J., Scaling Lifelong Multi-Agent Path Finding to More Realistic Settings(SoCS 2024) — 2023 League of Robot Runners 경진대회의 지도·작업 발생 규칙·계획 시간 제한을 기술하며, 원 페이지 [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md)의 5. 적용 사례 (현장 유형 명시)에 있는 물류창고 사례의 근거다. [사실][^ref-1514]
- Sánchez de la Fuente, S. 외(레온 대학교), Scenario Generation for Robot Simulation from Public Data(WAF 2025) — 공개 지리공간 데이터로 3D 시나리오를 만들어 주요 로봇 플랫폼에서 쓸 수 있는 시뮬레이션 모델을 생성하고 Gazebo·Unity 의 ROS 2 시스템과 연동하는 방법을 제안했다(초록 기준). [사실][^ref-1519]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/design-and-simulation/scenario-model-and-editing.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/design-and-simulation/scenario-model-and-editing.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md)
- 관련 영역: [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/design-and-simulation/scenario-model-and-editing.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1512]: Pasch, F., Mirus, F., Zhang, Y., & Scholl, K.-U. (Intel Labs 외, arXiv), Scenario Execution for Robotics: A generic, backend-agnostic library for running reproducible robotics experiments and tests, 2024-09-11, https://arxiv.org/abs/2409.07080, 접근일 2026-10-09
[^ref-1513]: Elmaaroufi, K., Shanker, D., Cismaru, A., Vazquez-Chanlatte, M., Sangiovanni-Vincentelli, A., Zaharia, M., & Seshia, S. A. (COLM 2024, arXiv), ScenicNL: Generating Probabilistic Scenario Programs from Crash Reports, 2024-05-03, https://arxiv.org/abs/2405.03709, 접근일 2026-10-09
[^ref-1514]: Jiang, H., Zhang, Y., Veerapaneni, R., & Li, J. (SoCS 2024, arXiv), Scaling Lifelong Multi-Agent Path Finding to More Realistic Settings: Research Challenges and Opportunities, 2024-04-24, https://arxiv.org/abs/2404.16162, 접근일 2026-10-09
[^ref-1515]: Ortega, A., Wiest, S., Pasch, F., & Hochgeschwender, N. (arXiv, ERAS 2026 채택), Replicable Simulation-Based Robot Validation through Provenance, 2026-05-28, https://arxiv.org/abs/2605.29973, 접근일 2026-10-09
[^ref-1516]: Ortega, A., Parra, S., Schneider, S., & Hochgeschwender, N. (Frontiers in Robotics and AI 11), Composable and executable scenarios for simulation-based testing of mobile robots, 2024-08-02, https://pmc.ncbi.nlm.nih.gov/articles/PMC11327003/, 접근일 2026-10-09
[^ref-1519]: Sánchez de la Fuente, S., Prieto López, L., González Santamarta, M. Á., Matellán Olivera, V. 외 (Universidad de León, WAF 2025), Scenario Generation for Robot Simulation from Public Data, 2025, https://portalcientifico.unileon.es/documentos/6972798ce66b2902147b1aeb, 접근일 2026-10-09

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-09-13 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-09 | 2026-10-09-13 | 33. 시나리오 모델·편집 의 "대표 연구와 자료" 절에서 분리 |
```

### runs/2026-10-09-13/pages/topics/2026/2026-10-09-area33-s10.md

```markdown
---
title: "33. 시나리오 모델·편집 — 다른 연구영역과의 연결"
type: topic
category: "I. 설계·시뮬레이션"
primary_area_no: 33
related_areas: [9, 11, 14, 15, 18, 19, 22, 24, 27, 32, 34, 36, 44, 54, 57, 61, 62, 63, 64, 65, 66]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-079, ref-104, ref-1086, ref-1089, ref-116, ref-1510, ref-1511, ref-1512, ref-1513, ref-1514, ref-1515, ref-1516, ref-482]
last_run: 2026-10-09
version: 1
split_from: docs/categories/design-and-simulation/scenario-model-and-editing.md#10
---

[홈](../../index.md) › [주제](../index.md) › 33. 시나리오 모델·편집 — 다른 연구영역과의 연결

# 33. 시나리오 모델·편집 — 다른 연구영역과의 연결

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이 영역은 시나리오를 대화로 만드는 C. 채팅 기반 구성·운영, 시나리오를 실행·재현하는 I. 설계·시뮬레이션의 다른 영역, 시나리오에 들어가는 공간·사람·설비·작업 영역, 적용 현장인 Q. 현장 유형별 적용과 이어진다. [추정][^ref-104][^ref-116][^ref-1089]
- 이 페이지는 [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md) 페이지의 "다른 연구영역과의 연결" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md) 페이지를 쓰는 과정에서 "다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이 영역은 시나리오를 대화로 만드는 C. 채팅 기반 구성·운영, 시나리오를 실행·재현하는 I. 설계·시뮬레이션의 다른 영역, 시나리오에 들어가는 공간·사람·설비·작업 영역, 적용 현장인 Q. 현장 유형별 적용과 이어진다. [추정][^ref-104][^ref-116][^ref-1089]


2026-09-30 실행까지 정리한 연결은 [33. 시나리오 모델·편집 — 다른 연구영역과의 연결 (2026-09-30)](2026-09-30-area33-s10.md)에 있다.

### 2026-10-09 갱신에서 더한 연결

- [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md) — RoboVAST 는 실행마다 해석된 매개변수·rosbag·합격 여부·결정적 실행 식별자를 남기고, 조합형 실행 시나리오는 동적 문 시나리오로 공개 주행 스택의 설정 오류를 찾았다. [사실][^ref-1515][^ref-1516] Scenario Execution 의 라이다 잡음 매개변수처럼 장애를 시나리오 매개변수로 선언하는 방식도 시험 시나리오와 이어지며, 센서 장애 주입 자체는 로봇 자체 지능·제어 쪽 연계 대상이다. [추정][^ref-1512]
- [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md) — 시나리오 형식의 판 호환 선언·이전 스크립트·엄격 스키마와 인스턴스별 구체 구성 기록은 시나리오 자산의 수명주기 관리와 이어질 것으로 보인다(원 페이지 [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md)의 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 참고). [추정][^ref-1511][^ref-1515]
- [61. 물류창고](../../categories/site-type-applications/warehouse.md)·[27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md) — League of Robot Runners 의 Warehouse·Sortation 지도 시나리오는 지속형 다중 에이전트 경로 찾기 경진대회 벤치마크이며 실제 물류창고 배치가 아니다(원 페이지 [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md)의 5. 적용 사례 (현장 유형 명시) 참고). [사실][^ref-1514]
- [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md)·[11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md) — 사고 보고서 같은 서술형 기록을 확률적 시나리오 프로그램으로 바꾸는 방법은 도로 교통 분야에 있으나, 로봇 플릿의 실행 기록을 시나리오 사양으로 바꾸는 공개 형식은 찾지 못했다. [추정][^ref-1513][^ref-1086] ScenicNL 은 여러 대규모 언어 모델 프롬프트를 컴파일러·시뮬레이터와 엮는다. [사실][^ref-1513] 그래서 이런 기록 변환 방식은 L. AI·학습 기술의 [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md)과도 이어질 것으로 보인다. [추정][^ref-1513]
- [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md) — Open-RMF 편집기가 traffic-editor 에서 Site Editor 로 넘어가고 traffic-editor 의 다음 판은 데카르트·위경도 좌표를 기본으로 하려 하므로, 시나리오가 참조하는 건물 파일의 형식·좌표계 전환을 함께 따라가야 할 것으로 보인다. [추정][^ref-482][^ref-1510][^ref-079]

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/design-and-simulation/scenario-model-and-editing.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/design-and-simulation/scenario-model-and-editing.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md)
- 관련 영역: [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/design-and-simulation/scenario-model-and-editing.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-079]: Open Robotics (osrf/ros2multirobotbook), Programming Multiple Robots with ROS 2 — Traffic Editor, 미확인, https://osrf.github.io/ros2multirobotbook/traffic-editor.html, 접근일 2026-09-30
[^ref-104]: Open-RMF (open-rmf/rmf_demos), rmf_demos — README, 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-30
[^ref-1086]: Vin, E., Kashiwa, S., Rhea, M., Fremont, D. J., Kim, E., Dreossi, T., Ghosh, S., Yue, X., Sangiovanni-Vincentelli, A. L., & Seshia, S. A. (CAV 2023, arXiv), 3D Environment Modeling for Falsification and Beyond with Scenic 3.0, 2023-07, https://arxiv.org/abs/2307.03325, 접근일 2026-09-30
[^ref-1089]: Shcherbyna, V. 외 (arXiv), Arena 4.0: A Comprehensive ROS2 Development and Benchmarking Platform for Human-centric Navigation Using Generative-Model-based Environment Generation, 2024-09, https://arxiv.org/abs/2409.12471, 접근일 2026-09-30
[^ref-116]: Filippone, G., Pettinari, S., & Pelliccione, P. (IEEE TSE, arXiv), Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis, 2026-03, https://arxiv.org/abs/2603.15427, 접근일 2026-09-30
[^ref-1510]: Open Robotics Discourse (Open-RMF 상호운용 그룹, 작성자 grey), Interoperability Interest Group June 6, 2024: Preview of the RMF Site Editor, 2024-06-05, https://discourse.openrobotics.org/t/interoperability-interest-group-june-6-2024-preview-of-the-rmf-site-editor/38070, 접근일 2026-10-09
[^ref-1511]: ASAM e.V., ASAM OpenSCENARIO XML v1.4.0 — 5 Backward compatibility, 미확인, https://openscenario.asam.net/ASAM_OpenSCENARIO_XML/v1.4.0/05_backward_compatibility/01_backward_compatibility.html, 접근일 2026-10-09
[^ref-1512]: Pasch, F., Mirus, F., Zhang, Y., & Scholl, K.-U. (Intel Labs 외, arXiv), Scenario Execution for Robotics: A generic, backend-agnostic library for running reproducible robotics experiments and tests, 2024-09-11, https://arxiv.org/abs/2409.07080, 접근일 2026-10-09
[^ref-1513]: Elmaaroufi, K., Shanker, D., Cismaru, A., Vazquez-Chanlatte, M., Sangiovanni-Vincentelli, A., Zaharia, M., & Seshia, S. A. (COLM 2024, arXiv), ScenicNL: Generating Probabilistic Scenario Programs from Crash Reports, 2024-05-03, https://arxiv.org/abs/2405.03709, 접근일 2026-10-09
[^ref-1514]: Jiang, H., Zhang, Y., Veerapaneni, R., & Li, J. (SoCS 2024, arXiv), Scaling Lifelong Multi-Agent Path Finding to More Realistic Settings: Research Challenges and Opportunities, 2024-04-24, https://arxiv.org/abs/2404.16162, 접근일 2026-10-09
[^ref-1515]: Ortega, A., Wiest, S., Pasch, F., & Hochgeschwender, N. (arXiv, ERAS 2026 채택), Replicable Simulation-Based Robot Validation through Provenance, 2026-05-28, https://arxiv.org/abs/2605.29973, 접근일 2026-10-09
[^ref-1516]: Ortega, A., Parra, S., Schneider, S., & Hochgeschwender, N. (Frontiers in Robotics and AI 11), Composable and executable scenarios for simulation-based testing of mobile robots, 2024-08-02, https://pmc.ncbi.nlm.nih.gov/articles/PMC11327003/, 접근일 2026-10-09
[^ref-482]: Open-RMF (open-rmf/rmf_site), rmf_site — RMF Site Editor (README), 미확인, https://github.com/open-rmf/rmf_site, 접근일 2026-10-09

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-09-13 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-09 | 2026-10-09-13 | 33. 시나리오 모델·편집 의 "다른 연구영역과의 연결" 절에서 분리 |
```

### runs/2026-10-09-13/pages/topics/2026/2026-10-09-area33-s11.md

```markdown
---
title: "33. 시나리오 모델·편집 — 열린 질문"
type: topic
category: "I. 설계·시뮬레이션"
primary_area_no: 33
related_areas: [9, 11, 14, 15, 18, 19, 22, 24, 27, 32, 34, 36, 44, 54, 57, 61, 62, 63, 64, 65, 66]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-1086, ref-1510, ref-1511, ref-1512, ref-1513, ref-1515, ref-1518, ref-482, ref-528]
last_run: 2026-10-09
version: 1
split_from: docs/categories/design-and-simulation/scenario-model-and-editing.md#11
---

[홈](../../index.md) › [주제](../index.md) › 33. 시나리오 모델·편집 — 열린 질문

# 33. 시나리오 모델·편집 — 열린 질문

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 이번 실행 전 이 영역에 걸린 열린 질문은 8건이고, 이번 실행(2026-10-09-13)에서 3건을 새로 올렸으며 해결 처리한 질문은 없다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.
- 이 페이지는 [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md) 페이지의 "열린 질문" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md) 페이지를 쓰는 과정에서 "열린 질문" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

이번 실행 전 이 영역에 걸린 열린 질문은 8건이고, 이번 실행(2026-10-09-13)에서 3건을 새로 올렸으며 해결 처리한 질문은 없다. 전체 목록은 [열린 질문](../../open-questions.md)에 있다.

2026-09-30 실행까지 정리한 내용은 [33. 시나리오 모델·편집 — 열린 질문 (2026-09-30)](2026-09-30-area33-s11.md)에 있다.

### 2026-10-09 갱신(실행 2026-10-09-13)

이번 조사에서 다룬 기존 질문의 진행은 다음과 같다.

- **oq-234** (상태: 열림) 부분 근거: 도로 교통 표준(ASAM OpenSCENARIO XML)은 시나리오 파일의 판 이전 규칙을 공개하고 RoboVAST 는 인스턴스를 구체 구성으로 해석해 기록하지만, 로봇 시뮬레이션 형식(SDFormat·Open-RMF 건물 파일)의 같은 규칙은 아직 확인하지 못했다(원 페이지 [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md)의 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 참고). [추정][^ref-1511][^ref-1515]
- **oq-233** (상태: 열림) 부분 근거: OpenSCENARIO 2 가 이동로봇 주행 시나리오 기술에 다시 쓰이고 있어 기존 형식 조합 쪽 근거가 될 수 있으나 두 근거 연구는 공동 저자를 공유하며, Open-RMF 편집기의 Site Editor 전환으로 건물 파일 참조의 이전 규칙도 함께 필요할 것으로 보인다. [추정][^ref-1512][^ref-1515][^ref-482][^ref-1510]
- **oq-235** (상태: 열림) 미해결: 여러 제조사 로봇 플릿과 승강기·문 같은 설비 장애를 한 형식으로 선언하는 사례를 이번에도 찾지 못했다. [추정][^ref-528][^ref-1512][^ref-1518]
- **oq-131** (상태: 열림) 미해결: 로봇 플릿 실행 기록(작업·배정·위치·사건 시각)을 시나리오 사양으로 바꾸는 공개 형식이나 변환 규칙을 이번에도 찾지 못했다. [추정][^ref-1513][^ref-1086]
- **oq-236** (상태: 열림) 미해결: 국내 다중 로봇 시나리오 예제 라이브러리를 이번에도 찾지 못했다.
- **oq-135** (상태: 열림) 이번 실행에서 조사하지 않았다.

이번에 새로 올린 질문(번호는 [열린 질문](../../open-questions.md)에서 부여된다):

- RoboVAST 처럼 추상 시나리오를 구체 인스턴스로 해석하고 실행마다 출처를 기록하는 방식을 여러 제조사 로봇 플릿과 승강기·문 같은 설비가 함께 있는 다중 로봇 시나리오에 적용한 사례가 있는가?
- Open-RMF Site Editor 의 현장 형식이 기존 traffic-editor 의 .building.yaml 을 대체하는가, 그리고 기존 건물 파일을 옮기는 공식 변환 도구나 판 이전 규칙이 있는가?
- OpenSCENARIO 2 DSL 로 다중 로봇 플릿의 작업 배정과 승강기·문 같은 설비 사건을 기술할 수 있는가, 기술하려면 어떤 확장 라이브러리가 필요한가?

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/design-and-simulation/scenario-model-and-editing.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/design-and-simulation/scenario-model-and-editing.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md)
- 관련 영역: [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/design-and-simulation/scenario-model-and-editing.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1086]: Vin, E., Kashiwa, S., Rhea, M., Fremont, D. J., Kim, E., Dreossi, T., Ghosh, S., Yue, X., Sangiovanni-Vincentelli, A. L., & Seshia, S. A. (CAV 2023, arXiv), 3D Environment Modeling for Falsification and Beyond with Scenic 3.0, 2023-07, https://arxiv.org/abs/2307.03325, 접근일 2026-09-30
[^ref-1510]: Open Robotics Discourse (Open-RMF 상호운용 그룹, 작성자 grey), Interoperability Interest Group June 6, 2024: Preview of the RMF Site Editor, 2024-06-05, https://discourse.openrobotics.org/t/interoperability-interest-group-june-6-2024-preview-of-the-rmf-site-editor/38070, 접근일 2026-10-09
[^ref-1511]: ASAM e.V., ASAM OpenSCENARIO XML v1.4.0 — 5 Backward compatibility, 미확인, https://openscenario.asam.net/ASAM_OpenSCENARIO_XML/v1.4.0/05_backward_compatibility/01_backward_compatibility.html, 접근일 2026-10-09
[^ref-1512]: Pasch, F., Mirus, F., Zhang, Y., & Scholl, K.-U. (Intel Labs 외, arXiv), Scenario Execution for Robotics: A generic, backend-agnostic library for running reproducible robotics experiments and tests, 2024-09-11, https://arxiv.org/abs/2409.07080, 접근일 2026-10-09
[^ref-1513]: Elmaaroufi, K., Shanker, D., Cismaru, A., Vazquez-Chanlatte, M., Sangiovanni-Vincentelli, A., Zaharia, M., & Seshia, S. A. (COLM 2024, arXiv), ScenicNL: Generating Probabilistic Scenario Programs from Crash Reports, 2024-05-03, https://arxiv.org/abs/2405.03709, 접근일 2026-10-09
[^ref-1515]: Ortega, A., Wiest, S., Pasch, F., & Hochgeschwender, N. (arXiv, ERAS 2026 채택), Replicable Simulation-Based Robot Validation through Provenance, 2026-05-28, https://arxiv.org/abs/2605.29973, 접근일 2026-10-09
[^ref-1518]: ros2_fault_injection 프로젝트 (Read the Docs), ros2_fault_injection documentation, 미확인, https://ros2-fault-injection.readthedocs.io/, 접근일 2026-10-09
[^ref-482]: Open-RMF (open-rmf/rmf_site), rmf_site — RMF Site Editor (README), 미확인, https://github.com/open-rmf/rmf_site, 접근일 2026-10-09
[^ref-528]: NIST (usnistgov/ARIAC_docs), ARIAC Documentation — Challenges, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-09-13 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-09 | 2026-10-09-13 | 33. 시나리오 모델·편집 의 "열린 질문" 절에서 분리 |
```

### runs/2026-10-09-13/pages/topics/2026/2026-10-09-area33-s7.md

```markdown
---
title: "33. 시나리오 모델·편집 — 관련 표준·프레임워크·오픈소스"
type: topic
category: "I. 설계·시뮬레이션"
primary_area_no: 33
related_areas: [9, 11, 14, 15, 18, 19, 22, 24, 27, 32, 34, 36, 44, 54, 57, 61, 62, 63, 64, 65, 66]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-104, ref-1088, ref-1091, ref-1510, ref-1511, ref-1512, ref-1514, ref-1515, ref-482, ref-528, ref-971]
last_run: 2026-10-09
version: 1
split_from: docs/categories/design-and-simulation/scenario-model-and-editing.md#7
---

[홈](../../index.md) › [주제](../index.md) › 33. 시나리오 모델·편집 — 관련 표준·프레임워크·오픈소스

# 33. 시나리오 모델·편집 — 관련 표준·프레임워크·오픈소스

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 시나리오 형식과 예제·벤치마크는 분야별로 따로 나뉘어 있으며, 아래 표는 이번에 확인한 형식·오픈소스·평가 프로그램을 이 영역과의 관계로 정리한 것이다. [추정][^ref-1088][^ref-104][^ref-971][^ref-528][^ref-1091]
- 이 페이지는 [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md) 페이지의 "관련 표준·프레임워크·오픈소스" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md) 페이지를 쓰는 과정에서 "관련 표준·프레임워크·오픈소스" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

시나리오 형식과 예제·벤치마크는 분야별로 따로 나뉘어 있으며, 아래 표는 이번에 확인한 형식·오픈소스·평가 프로그램을 이 영역과의 관계로 정리한 것이다. [추정][^ref-1088][^ref-104][^ref-971][^ref-528][^ref-1091]


2026-09-30 실행까지 정리한 표(Moving AI MAPF 벤치마크·VDMA 레이아웃 교환 형식 등)는 [33. 시나리오 모델·편집 — 관련 표준·프레임워크·오픈소스 (2026-09-30)](2026-09-30-area33-s7.md)에 있다.

### 2026-10-09 갱신에서 더한 항목

| 이름 | 유형 | 이 영역과의 관계 | 출처 |
|---|---|---|---|
| RMF Site Editor (rmf_site) | 오픈소스 | 예전 traffic-editor 를 대체하는 Open-RMF 현장 편집 도구로, 3D 환경·로봇·교통 규칙·승강기·문을 편집하고 시뮬레이션과 주행 그래프를 생성한다. [사실][^ref-482][^ref-1510] | [^ref-482][^ref-1510] |
| ASAM OpenSCENARIO XML 1.4.0 하위 호환성 절 | 표준 | 판별 호환 선언, 1.2.0→1.3.0 XSLT 이전 스크립트, 폐기 요소를 뺀 엄격 스키마로 시나리오 파일의 판 이전을 다룬다(발행일 미확인, 2026-10-09 확인). [사실][^ref-1511] | [^ref-1511] |
| Scenario Execution for Robotics | 오픈소스 | OpenSCENARIO 2 로 쓴 로봇 시나리오를 행동 트리로 바꿔 실행하고 매개변수 조합을 펼친다. [사실][^ref-1512] | [^ref-1512] |
| RoboVAST | 프레임워크 | 환경(FloorPlan 모델)·추상 시나리오(OpenSCENARIO DSL)·변형 파일을 나누고 구체 구성과 실행 기록을 남기는 시험 틀이다. [사실][^ref-1515] | [^ref-1515] |
| League of Robot Runners (2023) | 평가 프로그램 | Warehouse·Sortation 지도를 포함한 지속형 다중 에이전트 경로 찾기 경진대회 시나리오다(원 페이지 [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md)의 5. 적용 사례 (현장 유형 명시)에 있는 물류창고 사례, 실제 현장 아님). [사실][^ref-1514] | [^ref-1514] |

전체 목록은 [표준·프레임워크 목록](../../standards/index.md)에 있다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/design-and-simulation/scenario-model-and-editing.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/design-and-simulation/scenario-model-and-editing.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md)
- 관련 영역: [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/design-and-simulation/scenario-model-and-editing.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-104]: Open-RMF (open-rmf/rmf_demos), rmf_demos — README, 미확인, https://github.com/open-rmf/rmf_demos, 접근일 2026-09-30
[^ref-1088]: ASAM e.V., ASAM OpenSCENARIO® XML, 미확인, https://www.asam.net/standards/detail/openscenario-xml/, 접근일 2026-09-30
[^ref-1091]: Moving AI Lab (Sturtevant 외), MAPF Benchmarks, 미확인, https://movingai.com/benchmarks/mapf/index.html, 접근일 2026-09-30
[^ref-1510]: Open Robotics Discourse (Open-RMF 상호운용 그룹, 작성자 grey), Interoperability Interest Group June 6, 2024: Preview of the RMF Site Editor, 2024-06-05, https://discourse.openrobotics.org/t/interoperability-interest-group-june-6-2024-preview-of-the-rmf-site-editor/38070, 접근일 2026-10-09
[^ref-1511]: ASAM e.V., ASAM OpenSCENARIO XML v1.4.0 — 5 Backward compatibility, 미확인, https://openscenario.asam.net/ASAM_OpenSCENARIO_XML/v1.4.0/05_backward_compatibility/01_backward_compatibility.html, 접근일 2026-10-09
[^ref-1512]: Pasch, F., Mirus, F., Zhang, Y., & Scholl, K.-U. (Intel Labs 외, arXiv), Scenario Execution for Robotics: A generic, backend-agnostic library for running reproducible robotics experiments and tests, 2024-09-11, https://arxiv.org/abs/2409.07080, 접근일 2026-10-09
[^ref-1514]: Jiang, H., Zhang, Y., Veerapaneni, R., & Li, J. (SoCS 2024, arXiv), Scaling Lifelong Multi-Agent Path Finding to More Realistic Settings: Research Challenges and Opportunities, 2024-04-24, https://arxiv.org/abs/2404.16162, 접근일 2026-10-09
[^ref-1515]: Ortega, A., Wiest, S., Pasch, F., & Hochgeschwender, N. (arXiv, ERAS 2026 채택), Replicable Simulation-Based Robot Validation through Provenance, 2026-05-28, https://arxiv.org/abs/2605.29973, 접근일 2026-10-09
[^ref-482]: Open-RMF (open-rmf/rmf_site), rmf_site — RMF Site Editor (README), 미확인, https://github.com/open-rmf/rmf_site, 접근일 2026-10-09
[^ref-528]: NIST (usnistgov/ARIAC_docs), ARIAC Documentation — Challenges, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html, 접근일 2026-09-30
[^ref-971]: Li, C., Zhang, R., Wong, J. 외 (Stanford, arXiv), BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation, 2024-03, https://arxiv.org/abs/2403.09227, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-09-13 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-09 | 2026-10-09-13 | 33. 시나리오 모델·편집 의 "관련 표준·프레임워크·오픈소스" 절에서 분리 |
```

### runs/2026-10-09-13/pages/topics/2026/2026-10-09-area33-s3.md

```markdown
---
title: "33. 시나리오 모델·편집 — 왜 중요한가"
type: topic
category: "I. 설계·시뮬레이션"
primary_area_no: 33
related_areas: [9, 11, 14, 15, 18, 19, 22, 24, 27, 32, 34, 36, 44, 54, 57, 61, 62, 63, 64, 65, 66]
tags: [분리 페이지]
status: draft
confidence: low
created: 2026-10-09
updated: 2026-10-09
sources: [ref-1088, ref-1091, ref-116, ref-1516, ref-528, ref-726]
last_run: 2026-10-09
version: 1
split_from: docs/categories/design-and-simulation/scenario-model-and-editing.md#3
---

[홈](../../index.md) › [주제](../index.md) › 33. 시나리오 모델·편집 — 왜 중요한가

# 33. 시나리오 모델·편집 — 왜 중요한가

<!-- auto:page-status:start -->
<!-- auto:page-status:end -->

## 1. 세 줄 요약

- 시나리오를 정해진 형식으로 표현해 두지 않으면 계획기·정책을 같은 조건에서 비교하거나 장애·긴급 요청 대응 시험을 반복하기 어렵고, 조건마다 시나리오 파일이 불어나며, 미션과 환경을 정의할 도메인 전문가가 쓸 공통 형식도 없다는 것이 확인한 자료의 종합이다. [추정][^ref-726][^ref-1091][^ref-528][^ref-1088][^ref-116]
- 이 페이지는 [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md) 페이지의 "왜 중요한가" 절이 분량 기준을 넘어 옮겨 온 것이다. 원 페이지의 검증을 거친 내용이며 새 주장은 없다.

## 2. 배경

[33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md) 페이지를 쓰는 과정에서 "왜 중요한가" 절의 분량이 세부영역 페이지 기준(4,000자)을 넘어, 내용을 줄이지 않고 이 주제 페이지로 분리했다.

## 3. 본문

시나리오를 정해진 형식으로 표현해 두지 않으면 계획기·정책을 같은 조건에서 비교하거나 장애·긴급 요청 대응 시험을 반복하기 어렵고, 조건마다 시나리오 파일이 불어나며, 미션과 환경을 정의할 도메인 전문가가 쓸 공통 형식도 없다는 것이 확인한 자료의 종합이다. [추정][^ref-726][^ref-1091][^ref-528][^ref-1088][^ref-116]


2026-09-30 실행까지 정리한 내용은 [33. 시나리오 모델·편집 — 왜 중요한가 (2026-09-30)](2026-09-30-area33-s3.md)에 있다.

앞의 종합을 보강하는 면담 근거로, Ortega·Parra·Schneider·Hochgeschwender(Frontiers in Robotics and AI, 2024-08-02)는 이동로봇 시뮬레이션 시험 일반의 도메인 전문가 14명을 면담해 환경 모델과 로봇 과제를 묶은 시험 시나리오의 변형 관리가 이동로봇 시뮬레이션 시험을 꺼리는 주요 장벽으로 나타났다고 보고했다. [사실][^ref-1516] 같은 연구는 기존 CAD·3D 모델링 도구가 시험 목적에 따라 바뀌어야 하는 장면에 맞지 않는다고 지적했다. [사실][^ref-1516] 면담 대상은 이동로봇 시뮬레이션 시험 분야의 전문가이며, ROP 실무자를 면담한 자료는 아직 찾지 못했다.

## 4. 현장 시나리오

현장 시나리오는 원 페이지의 [5. 적용 사례 (현장 유형 명시)](../../categories/design-and-simulation/scenario-model-and-editing.md) 절에 있다.

## 5. ROP 관점의 시사점

ROP가 직접 맡는 것과 외부와 연계하는 것은 원 페이지의 [9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준)](../../categories/design-and-simulation/scenario-model-and-editing.md) 절에 있다.

## 6. 연결되는 연구영역

- 주 연구영역: [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md)
- 관련 영역: [9. 채팅으로 시나리오 구성](../../categories/chat-based-configuration-and-operation/chat-scenario-composition.md), [11. 채팅으로 실제 상황 시뮬레이션 재현](../../categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md), [14. 도면·BIM에서 지도 만들기](../../categories/space-and-map-model/maps-from-floor-plans-and-bim.md), [15. 지도·공간·위치 모델](../../categories/space-and-map-model/map-space-and-location-model.md), [18. 실시간 세계 상태·데이터 일관성](../../categories/objects-people-and-live-state/real-time-world-state-and-data-consistency.md), [19. 사람·보행자 모델](../../categories/objects-people-and-live-state/people-and-pedestrian-model.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md), [24. 작업·워크플로 모델링](../../categories/planning-and-optimization/task-and-workflow-modeling.md), [27. 다중 로봇 경로·교통 관리 — MAPF](../../categories/planning-and-optimization/multi-robot-path-and-traffic-management-mapf.md), [32. 예외 복구·재계획·업무 연속성](../../categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md), [34. 시뮬레이션·예측용 디지털 트윈](../../categories/design-and-simulation/simulation-and-predictive-digital-twin.md), [36. 가상 시운전·실제 상황 재현](../../categories/design-and-simulation/virtual-commissioning-and-real-situation-replay.md), [44. 로봇 기반 모델·언어 모델 계획](../../categories/ai-and-learning/robot-foundation-models-and-llm-planning.md), [54. 시험·형식 검증·벤치마크](../../categories/verification-deployment-and-lifecycle/testing-formal-verification-and-benchmarking.md), [57. 자산·소프트웨어 수명주기 관리](../../categories/verification-deployment-and-lifecycle/asset-and-software-lifecycle-management.md), [61. 물류창고](../../categories/site-type-applications/warehouse.md), [62. 제조 공장](../../categories/site-type-applications/manufacturing-plant.md), [63. 병원·의료](../../categories/site-type-applications/hospital-and-healthcare.md), [64. 상업 시설](../../categories/site-type-applications/commercial-facilities.md), [65. 가정·공동주택](../../categories/site-type-applications/home-and-apartment.md), [66. 실외](../../categories/site-type-applications/outdoor.md)

## 7. 열린 질문

열린 질문은 원 페이지의 [11. 열린 질문](../../categories/design-and-simulation/scenario-model-and-editing.md) 절과 [열린 질문](../../open-questions.md) 페이지에 모은다.

## 8. 출처

[^ref-1088]: ASAM e.V., ASAM OpenSCENARIO® XML, 미확인, https://www.asam.net/standards/detail/openscenario-xml/, 접근일 2026-09-30
[^ref-1091]: Moving AI Lab (Sturtevant 외), MAPF Benchmarks, 미확인, https://movingai.com/benchmarks/mapf/index.html, 접근일 2026-09-30
[^ref-116]: Filippone, G., Pettinari, S., & Pelliccione, P. (IEEE TSE, arXiv), Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis, 2026-03, https://arxiv.org/abs/2603.15427, 접근일 2026-09-30
[^ref-1516]: Ortega, A., Parra, S., Schneider, S., & Hochgeschwender, N. (Frontiers in Robotics and AI 11), Composable and executable scenarios for simulation-based testing of mobile robots, 2024-08-02, https://pmc.ncbi.nlm.nih.gov/articles/PMC11327003/, 접근일 2026-10-09
[^ref-528]: NIST (usnistgov/ARIAC_docs), ARIAC Documentation — Challenges, 미확인, https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html, 접근일 2026-09-30
[^ref-726]: Kästner, L., Bhuiyan, T., Le, T. A. 외 (RA-L 2022, arXiv), Arena-Bench: A Benchmarking Suite for Obstacle Avoidance Approaches in Highly Dynamic Environments, 2022-06, https://arxiv.org/abs/2206.05728, 접근일 2026-09-30

## 9. 검증 노트

원 페이지와 함께 실행 2026-10-09-13 의 1차·2차 검증을 거쳤다. 분리는 코드가 했고 내용은 바꾸지 않았다.

## 10. 이력

| 날짜 | 실행 id | 변경 |
|---|---|---|
| 2026-10-09 | 2026-10-09-13 | 33. 시나리오 모델·편집 의 "왜 중요한가" 절에서 분리 |
```

### docs/references/index.md (요약: 이번 대상 페이지가 인용한 15건 / 전체 1282건. 목록에 없는 출처는 새 id 로 적는다 — 같은 URL 이 이미 있으면 퍼블리셔가 기존 id 로 합친다)

```markdown
| id | 기관 | 제목 | 발행일 | URL | 접근일 | 원문 열람 |
|---|---|---|---|---|---|---|
| ref-046 | VDMA (Intralogistics-2X-LIF GitHub) | Layout-Interchange-Format — README (Repository for the Layout Interchange Format (LIF) developed by the VDMA) | 2023-09 | https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format | 2026-09-25 | 아니오 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 2026-09-25 | 예 |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — Demonstrations of Open-RMF (README) | 미확인 | https://github.com/open-rmf/rmf_demos | 2026-09-25 | 예 |
| ref-116 | Filippone, G., Pettinari, S., & Pelliccione, P. | Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis | 2026-03 | https://arxiv.org/abs/2603.15427 | 2026-09-25 | 아니오 |
| ref-528 | NIST (usnistgov/ARIAC_docs) | ARIAC 2025 Documentation — Challenges | 미확인 | https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html | 2026-09-25 | 예 |
| ref-726 | Kästner, L. 외 | Arena-Bench: A Benchmarking Suite for Obstacle Avoidance Approaches in Highly Dynamic Environments | 2022-06 | https://arxiv.org/abs/2206.05728 | 2026-09-25 | 아니오 |
| ref-815 | Yang, Y., Sun, F.-Y., Weihs, L. 외 (Allen Institute for AI 등) | Holodeck: Language Guided Generation of 3D Embodied AI Environments | 2023-12-14 | https://arxiv.org/abs/2312.09067 | 2026-09-29 | 예 |
| ref-971 | Li, C., Zhang, R., Wong, J. 외 (arXiv; CoRL 2022 예비판) | BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation | 2024-03-14 | https://arxiv.org/abs/2403.09227 | 2026-09-29 | 예 |
| ref-1086 | Vin, E., Kashiwa, S., Rhea, M., Fremont, D. J., Kim, E., Dreossi, T., Ghosh, S., Yue, X., Sangiovanni-Vincentelli, A. L., & Seshia, S. A. (CAV 2023, arXiv) | 3D Environment Modeling for Falsification and Beyond with Scenic 3.0 | 2023-07 | https://arxiv.org/abs/2307.03325 | 2026-09-30 | 예 |
| ref-1087 | NIST (usnistgov/ARIAC_docs) | ARIAC Documentation — Scenario | 미확인 | https://pages.nist.gov/ARIAC_docs/en/latest/pages/scenario.html | 2026-09-30 | 예 |
| ref-1088 | ASAM e.V. | ASAM OpenSCENARIO® XML | 미확인 | https://www.asam.net/standards/detail/openscenario-xml/ | 2026-09-30 | 예 |
| ref-1089 | Shcherbyna, V. 외 (arXiv) | Arena 4.0: A Comprehensive ROS2 Development and Benchmarking Platform for Human-centric Navigation Using Generative-Model-based Environment Generation | 2024-09 | https://arxiv.org/abs/2409.12471 | 2026-09-30 | 예 |
| ref-1090 | BehaviorTree.CPP 프로젝트 (behaviortree.dev) | Groot2 | 미확인 | https://www.behaviortree.dev/groot/ | 2026-09-30 | 예 |
| ref-1091 | Moving AI Lab (Sturtevant 외) | MAPF Benchmarks | 미확인 | https://movingai.com/benchmarks/mapf/index.html | 2026-09-30 | 예 |
| ref-1092 | Open Source Robotics Foundation | SDFormat (Simulation Description Format) | 미확인 | http://sdformat.org/ | 2026-09-30 | 예 |
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

### docs/open-questions.md (요약: 대상 영역 [33] 에 걸린 8건 / 전체 321건)

```markdown
- oq-131 [열림] 플릿 관제의 실행 기록(작업·배정·위치·사건 시각)을 시뮬레이션 시나리오 사양으로 바꾸는 공개 형식이나 변환 규칙이 있는가, 아니면 프로세스 마이닝식 로그 발견을 로봇 플릿 기록에 맞게 새로 정의해야 하는가? (영역 11, 37, 33)
- oq-135 [열림] 로봇 작업 시나리오 구성에서 되물어야 할 항목(할 일·물품·사람·순서·반복·기한·실패 처리)의 표준 질문 목록과 우선순위를 미션 명세 패턴이나 관제 작업 스키마에서 도출한 공개 자료가 있는가? (영역 9, 33)
- oq-233 [열림] 환경·로봇·사람·물품·작업·정책·물리·장애를 담는 ROP 시나리오 형식을 SDFormat·Open-RMF 건물 파일·OpenSCENARIO 같은 기존 형식을 조합해 만들 것인가, 새로 정의하고 각 형식으로 내보낼 것인가? (영역 33, 34)
- oq-234 [열림] 형식 판이 바뀔 때 개별 시나리오 인스턴스를 옮기고 호환성을 검사하는 버전 관리 규칙을 공개한 로봇 시뮬레이션 도구나 표준이 있는가? (영역 33, 57)
- oq-235 [열림] ARIAC 처럼 장애·긴급 요청을 시각·발생 횟수 조건으로 선언하는 방식을 여러 제조사 로봇 플릿과 승강기·문 같은 설비 장애까지 일반화한 시나리오 형식이 있는가? (영역 33, 32)
- oq-236 [열림] 국내 아파트·병원·물류센터·호텔을 본뜬 다중 로봇 시나리오 예제 라이브러리를 공개한 기관이나 프로젝트가 있는가? (영역 33, 65)
- oq-256 [열림] 실제 운영 기록을 재생해 재현한 상황에서 배차 정책이나 로봇 수를 바꿔 비교할 때, 기록된 다른 로봇·사람이 바뀐 조건에 반응하지 않는 문제를 로봇 플릿 재현에서 어떻게 다루는가? (영역 36, 19, 33)
- oq-304 [열림] 대화로 생성한 로봇 시나리오가 형식상 실행 가능한지와 사용자 의도에 맞는지를 승인 전에 각각 어떤 검사로 확인하는가? (영역 9, 33, 13)
```

### runs/2026-10-09-13/verification2.json

```json
{
  "run_id": "2026-10-09-13",
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
      "ref-1516(PMC URL)과 ref-1134(Frontiers URL)가 같은 논문(Ortega 외, Frontiers in Robotics and AI, 2024-08-02)을 가리킬 수 있다. 스토리텔러가 additional_research_requests 로 넘겼다. URL 이 달라 퍼블리셔가 자동으로 합치지 않으므로, 참고문헌 담당이 병합 여부를 확인해야 한다.",
      "자동 분리로 생긴 새 주제 페이지(2026-10-09-area33-s3·s6·s7·s8·s10·s11)가 같은 절의 기존 주제 페이지(2026-09-30-area33-s3·s6·s7·s8·s10·s11)와 제목이 같다. 새 페이지에는 이번 실행에서 더한 내용만 있다. 지금은 영역 페이지가 기존 페이지로 가는 링크를 잃었다(required_fixes 1)."
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
    "3·6·7·8·10·11절 append 패치: 절마다 기존 주제 페이지로 가는 링크 줄을 하나씩 넣는다. 대상은 2026-09-30-area33-s3·s6·s7·s8·s10·s11 이다. 예: '2026-09-30 실행까지 정리한 내용은 [33. 시나리오 모델·편집 — 대표 접근법과 기술 (2026-09-30)](../../topics/2026/2026-09-30-area33-s6.md)에 있다.' 문구는 '자세한 내용은 주제 페이지 …에 있다'와 다르게 쓴다. — 이유: 재분리 때 기존 '자세한 내용은 …' 링크 줄이 빠졌다. 그래서 영역 페이지가 새 주제 페이지(이번 추가분만 담음)만 가리키고, 지난 실행에서 검증·게시한 상세 내용(예: Moving AI 벤치마크·VDMA LIF 를 담은 7절 표)에는 닿지 않는다. 5절 끝의 'Moving AI … VDMA 레이아웃 교환 형식은 … 7절에서 다룬다'도 근거 없는 안내가 된다.",
    "11절: 첫 문장 '이 영역에 걸린 열린 질문은 기존 2건과 이번 실행에서 새로 올린 4건이며, 기존 2건은 이번 조사에서도 해결 근거를 찾지 못했다'를 replace 로 고친다. 건수를 빼고 쓰거나, 입력의 열린 질문 목록 기준으로 '이번 실행 전 이 영역에 걸린 8건, 이번 실행에서 새로 올린 3건'이라고 적는다. — 이유: 지난 실행(2026-09-30-12) 시점의 문장이 그대로 남았다. 이번 실행 내용(oq 6건 진행, 새 질문 3건)과 맞지 않고, 분리된 주제 페이지 2026-10-09-area33-s11 의 세 줄 요약·본문에도 옮겨져 있다.",
    "10절 append(분리 페이지 2026-10-09-area33-s10)의 '이 변환은 언어 모델을 쓰므로 L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획과도 이어진다. [사실][^ref-1513]'을 둘로 나눈다. 'ScenicNL 은 여러 대규모 언어 모델 프롬프트를 컴파일러·시뮬레이터와 엮는다. [사실][^ref-1513]'로 쓰고, 44번과의 연결은 태그 없는 연결 문장이나 [추정]으로 쓴다. — 이유: f22 가 뒷받침하는 것은 언어 모델을 쓴다는 사실뿐이다. 영역 사이의 연결 판단은 브리프 finding 이 아니므로 [사실]을 붙이면 태그가 올라간다.",
    "6·8·10·11절 append 본문의 절 번호 참조를 고친다. 해당 문구는 '8절에 정리했다', '6절에 요약했다', '면담 근거는 3절에 있다', '5절 물류창고 사례', '(9절)'이다. 모두 '원 페이지 [33. 시나리오 모델·편집](../../categories/design-and-simulation/scenario-model-and-editing.md)의 6. 대표 접근법과 기술'처럼 원 페이지 이름과 절 이름을 함께 쓰고 링크를 단다. — 이유: 자동 분리 뒤 이 문장들은 주제 페이지 안에 놓인다. 주제 페이지의 3·5·6·8·9절은 본문·ROP 관점의 시사점·연결되는 연구영역·출처·검증 노트라서, 독자는 다른 절로 읽게 된다.",
    "영역 페이지 프런트매터 last_run 을 2026-09-30 에서 2026-10-09 로 고친다. 3절 patch 의 frontmatter 에 넣는다. — 이유: updated·version 은 이번 실행으로 갱신됐는데 last_run 만 이전 실행 값이다. 분리 주제 페이지들은 last_run 2026-10-09 를 쓴다."
  ],
  "confidence": "low",
  "verification_note": "판정: 1차 조건부 승인 / 2차 수정 후 재검증. 확인 26건, 미확인 0건, 교차 확인 0건. 강등: 없음. 대신 f11·f21·f22 는 원문에 없는 한정·기능 구절을 빼서 주장을 좁혔고, f19 는 출처 안에서 다르게 적힌 Sortation 정점 수(54,320 / 54,230)를 병기했다. 원문 미열람 출처: ref-1088, ref-1086, ref-116(이번 실행에서 다시 열지 않았고, 참고문헌 목록 등재로 실재만 확인했다). 주의: 새 근거는 모두 단일 출처다. Open-RMF 편집기 전환(f15·f16·f17)은 같은 조직의 자료이고, OpenSCENARIO 2 의 로봇 재사용(f7·f4)은 공동 저자의 자료라 독립 확인이 아니다. 판 이전 규칙은 도로 교통 표준(OpenSCENARIO XML)에서만 확인됐다. 로봇 시뮬레이션 형식의 규칙은 여전히 미확인이다(oq-234 부분 근거, 해결 아님). 물류창고 사례(League of Robot Runners)는 경진대회 벤치마크이며 실제 현장이 아니고, 국내 자료도 없다. Isaac Sim Warehouse Creator(f21)는 벤더 주장이다. oq-131·oq-235·oq-236 은 미해결이고 oq-135 는 조사하지 않았다. 정정 요청은 없다. / 2차 수정 후 재검증. 1차 수정 지시 15건은 모두 이행을 확인했다. 브리프 밖 사실 드리프트는 없다. 태그 상향 1건(10절의 44. 로봇 기반 모델·언어 모델 계획 연결 문장에 [사실])을 고치게 했다. [분류원문] 보존(admonition 세 줄·1절·2절·원문 주석 일치), 섹션 순서 준수. 링크 문제: 자동 재분리 때 기존 '자세한 내용은 …' 줄이 빠져, 영역 페이지가 2026-09-30 주제 페이지(3·6·7·8·10·11절 상세 내용)로 가는 링크를 잃었다. 11절 요약 문장의 건수도 지난 실행 기준으로 남아 있다. 분리 페이지 안의 절 번호 참조와 last_run 값도 함께 고치게 했다. 파이프라인 담당 참고: 분량 자동 분리 코드가 기존 주제 페이지 링크 줄을 버린다. 이미 분리된 절을 다시 분리하면 같은 문제가 되풀이되므로, 분리 코드가 기존 링크를 보존하도록 고칠 것을 요청한다. ref-1516 과 ref-1134 의 동일 논문 여부는 참고문헌 정리에서 확인이 필요하다. 2차 검증에서 도구는 쓰지 않았다.",
  "retry_reason": null
}
```
