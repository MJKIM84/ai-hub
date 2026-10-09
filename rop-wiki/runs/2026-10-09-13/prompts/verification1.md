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
- verification_stage: first
- verifier_budget:
    - max_search_queries: 30
    - max_sources_per_run: 15
    - new_topic_pages: 1
    - page_updates: 2
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
        "ref-1509"
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
        "ref-1509",
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
        "ref-1509"
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
      "id": "ref-1509",
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
    "limits": "web_fetch_available: true · fetch_mode full. 갱신(update) 실행이며 정정 요청·발행 2년 지난 표준이 없어 빈·약한 절(5절 물류창고·국내 사례, 9절 판 관리 문장, 6·7절 편집기 전환)과 열린 질문 oq-131·oq-233·oq-234·oq-235·oq-236 만 조사했다. 검색 19회/30, 신규 출처 11건/15(ref-1509~ref-1519, 예약 구간 안), 모두 원문 페이지를 열었다(webfetch 10, github_raw 1). 재사용 5건 가운데 ref-079·ref-528 은 입력의 원문 텍스트(inbox)로 확인했고 ref-1088·ref-1086·ref-116 은 다시 열지 않았다(source_unopened). 교차 확인 0건: 새 근거가 모두 단일 출처라 신뢰도는 medium 이하다. 벤더 주장 1건(f21). 핵심 질문 답은 f25(추정)로 갱신했다. 현장 유형: 이번 새 사례는 물류창고(f19·f20 경진대회 벤치마크, f21 편집 도구)뿐이며 실제 물류창고 배치 사례와 국내 자료는 여전히 찾지 못했다. 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험)과 18. 실시간 세계 상태·데이터 일관성(현재 상태)을 섞지 않았고, 시나리오는 가정한 미래 실험의 입력으로만 다뤘다. 해결 제안한 열린 질문 없음(oq-234 는 부분 근거). 답한 트랙 질문 없음(트랙 실행 아님). 입력 누락 없음. 우선 지정 질문 없음."
  }
}
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

### docs/categories/design-and-simulation/capacity-sizing-and-layout-design.md (요약)

```markdown
# 35. 처리능력·규모·배치 설계

소속 대분류: I. 설계·시뮬레이션 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

필요한 로봇 수·배치·병목·여러 현장의 자원 배치를 설계하고, 로봇이 다니기 쉬운 공간을 만든다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **처리능력·규모 산정**: 처리할 일의 양에 맞는 로봇 수·종류, 충전기·작업대 배치, 운영 시간대를 정한다
- **병목 분석**: 로봇·설비·사람·승강기 가운데 어디가 병목인지 찾는다
- **다현장 자원 배치**: 여러 현장 사이에서 로봇과 자원을 어디에 얼마나 둘지 정한다
- **로봇 친화 공간 설계·개조**: 문 폭·문턱·경사·승강기 연동·충전 공간처럼 로봇이 다니고 일하기 쉬운 공간을 설계하거나 기존 공간을 고친다

이전 분류(2026-09-24)에서 이 페이지는 옛 3번 영역 ‘처리능력·거점·설비 계획’(옛 대분류 A. 업무·공급망 설계)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 물동량에 필요한 로봇 수와 종류, 작업대·충전기 배치, 교대 운영, 여러 거점의 자원 배치를 결정 [옛 분류원문]

> 옛 질문: 로봇을 늘려야 할까, 포장대나 엘리베이터가 병목일까? [옛 분류원문]

## 2. 핵심 질문

로봇을 늘려야 할까, 공간이나 설비가 병목일까? [분류원문]
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

### docs/categories/chat-based-configuration-and-operation/chat-scenario-composition.md (요약)

```markdown
# 9. 채팅으로 시나리오 구성

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

대화로 할 일·물품·사람·순서·기한·실패 처리 조건을 정한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 시나리오 구성**: 할 일·물품·사람·순서·반복·기한·실패 처리 조건을 대화로 정하고, 모자란 조건은 선택지와 이유를 붙인 질문으로 채운다
- **합의 내용 보존·변경 표시**: 대화가 이어져도 이미 합의한 단계를 지우지 않고 바뀐 부분만 반영하며, 사용자가 정한 값을 모델 추정보다 우선한다

## 2. 핵심 질문

할 일·사람·순서·실패 처리를 대화로 빠짐없이 정하려면 무엇을 되물어야 하는가? [분류원문]
```

### docs/categories/chat-based-configuration-and-operation/chat-real-situation-simulation-replay.md (요약)

```markdown
# 11. 채팅으로 실제 상황 시뮬레이션 재현

소속 대분류: C. 채팅 기반 구성·운영 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-29 · 버전: 2

## 1. 한 줄 정의

실제로 있었던 상황을 대화로 시뮬레이션에 재현하고, 재현이 실제와 얼마나 맞는지 보이며, 조건을 바꿔 비교한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **채팅으로 실제 상황 시뮬레이션 재현**: 현장에서 실제로 있었던 상황(혼잡, 고장, 승강기 대기, 사람 흐름)을 대화로 설명하거나 운영 기록을 지정하면 시뮬레이션으로 재현한다
- **대화로 조건 바꿔 비교**: 재현한 상황에서 로봇 수·경로·정책을 대화로 바꿔 다시 돌리고 결과 차이를 설명한다
- **재현 충실도 확인**: 재현한 시뮬레이션이 실제 기록(시각·위치·사건 순서)과 얼마나 맞는지 비교해 보여 주고, 맞지 않는 부분을 알려 준다

## 2. 핵심 질문

실제로 있었던 상황을 대화만으로 시뮬레이션에 재현하고, 조건을 바꿔 비교할 수 있는가? [분류원문]
```

### docs/categories/space-and-map-model/maps-from-floor-plans-and-bim.md (요약)

```markdown
# 14. 도면·BIM에서 지도 만들기

소속 대분류: D. 공간·지도 모델 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

평면도·BIM에서 공간과 시설을 인식해 지도 초안을 만들고 현장과 맞춘다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **도면 인식**: 평면도(PDF·이미지·CAD)에서 벽·문·승강기·계단·충전 위치를 인식해 층별 지도와 공용 자원 목록의 초안을 만든다
- **BIM·CAD 가져오기**: IFC 같은 건물 정보 모델에서 공간과 시설을 가져온다
- **축척 보정·도면–현장 정합**: 도면 픽셀을 미터로 보정하고, 도면과 센서 지도·현장의 차이를 확인해 맞춘다

이 영역의 일부는 이전 분류(2026-09-24)의 옛 6번 영역 ‘지도·공간·위치 모델’에서 왔다. 그 본문은 [15. 지도·공간·위치 모델](map-space-and-location-model.md)로 옮겼으며, 이 영역은 그 내용을 출발점으로 삼는다.

## 2. 핵심 질문

이미 있는 도면과 건물 모델에서 로봇이 쓸 지도를 얼마나 자동으로 만들 수 있는가? [분류원문]

> 원문 주석: 채팅 기능은 대화가 부르는 엔진과 짝을 이룬다. **맵 작성은 14·15번, 시나리오 구성과 실제 상황 재현은 33·36번, 로봇 구성은 5번, 업무 지시는 25·26번**의 기능을 대화로 쓰게 하는 것이다. [분류원문]

> 원문 주석: 지도는 한 번 만들고 끝나지 않는다. **현장과 도면의 차이 확인(14번), 좌표 정렬과 위치추정 신뢰도(15번), 지도 버전 관리(16번)**가 함께 필요하다. [분류원문]

> 원문 주석: AI는 특정 기능 하나에만 해당하지 않는다. **매뉴얼 해석은 4·55번, 도면 해석은 14번, 학습 기반 배정은 25번, 장애 분석은 38번**에 적용되는 연구 방법이다. [분류원문]
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

### docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md (요약)

```markdown
# 19. 사람·보행자 모델

소속 대분류: E. 사물·사람·실시간 상태 · 상태: published · 신뢰도: low · 마지막 갱신: 2026-09-30 · 버전: 2

## 1. 한 줄 정의

현장 사람의 위치·흐름·혼잡을 모델링해 계획과 안전에 쓴다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **사람·보행자 모델**: 현장 사람의 위치·목적지·멈춤·교차를 모델링해 로봇 계획과 안전에 반영한다
- **사람 흐름·혼잡 추정**: 시간대·구역별 사람의 흐름과 혼잡을 추정해 경로와 작업 시간에 반영한다

## 2. 핵심 질문

현장 사람의 위치와 흐름을 어떻게 알고 계획과 안전에 반영할 것인가? [분류원문]
```

### docs/categories/integration/facility-and-building-system-integration.md (요약)

```markdown
# 22. 설비·건물 시스템 연동

소속 대분류: F. 연동 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

문·승강기·출입통제·컨베이어·PLC·고정 센서와 작업을 연계한다 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **설비·건물 연동**: 문·승강기·출입통제·컨베이어·자동창고·PLC·빌딩 관리 시스템과 작업을 연계한다
- **승강기·문 예약과 연동**: 승강기와 문을 예약하고 로봇의 진입과 설비 상태를 맞물려 확인한다
- **로봇–설비 작업 동기화**: 컨베이어·작업대 준비와 로봇 도착처럼 설비와 로봇의 시점을 맞춘다
- **IoT·고정 센서 연동**: 고정 카메라·출입 센서·환경 센서처럼 로봇 밖의 센서 데이터를 연결한다

이전 분류(2026-09-24)에서 이 페이지는 옛 10번 영역 ‘설비·건물 시스템 연동’(옛 대분류 C. 연결·실행 기반)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 컨베이어, 자동창고, 작업대, PLC, 문, 승강기, 출입통제 시스템과 작업을 연계 [옛 분류원문]

> 옛 질문: 컨베이어 준비와 로봇 도착을 어떻게 맞출까? [옛 분류원문]

## 2. 핵심 질문

문·승강기·설비의 준비와 로봇의 도착을 어떻게 맞출 것인가? [분류원문]
```

### docs/categories/planning-and-optimization/task-and-workflow-modeling.md (요약)

```markdown
# 24. 작업·워크플로 모델링

소속 대분류: G. 계획·최적화 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

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

### docs/categories/execution-collaboration-and-recovery/exception-recovery-replanning-and-business-continuity.md (요약)

```markdown
# 32. 예외 복구·재계획·업무 연속성

소속 대분류: H. 실행·협업·예외 복구 · 상태: published · 신뢰도: medium · 마지막 갱신: 2026-09-25 · 버전: 2

## 1. 한 줄 정의

고장·통신 단절·누락에 대한 복구와 제한 운영 [분류원문]

이 영역이 다루는 일(2026-09-28 리스트업 기준):

- **예외 복구**: 고장·통신 단절·물품 누락·긴급 요청에 재배정·우회·수동 처리·제한 운영을 결정한다
- **제한 운영·업무 연속성**: 일부 장비가 멈춰도 업무를 이어 가는 운영 수준과 절차를 정한다

이전 분류(2026-09-24)에서 이 페이지는 옛 20번 영역 ‘예외 복구·재계획·업무 연속성’(옛 대분류 E. 협업·현장 운영)이었다. 아래는 그때의 원문 정의·질문·주석이며, 보관한 옛 원문과 글자 단위로 같다.

> 옛 정의: 고장·통신 단절·화물 누락·긴급 주문 등에 대해 재배정, 우회, 수동 처리, 제한 운영을 결정 [옛 분류원문]

> 옛 질문: 운반 중 고장 난 로봇의 화물과 남은 주문은 어떻게 처리할까? [옛 분류원문]

## 2. 핵심 질문

작업 중 로봇이 고장 나면 남은 일은 누가 어떻게 이어받는가? [분류원문]
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

### docs/open-questions.md (요약: 대상 영역 [33] 에 걸린 8건 / 전체 309건)

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

### runs/2026-10-09-12/research.md

```markdown
# 리서치 브리프 2026-10-09-12

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-09-12 |
| 날짜 | 2026-10-09 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 19. 사람·보행자 모델 |
| 대분류 | E. 사물·사람·실시간 상태 |

## 갭(비어 있거나 약한 섹션)

- 정정 요청 없음(inbox/corrections.md 에 대상 페이지 요청 없음). 갱신 실행이므로 원문 미열람·검색 결과 기준 주장의 재확인과 약한 절만 다룬다
- 섹션 5. 적용 사례 (현장 유형 명시) — 상업 시설 사례(Kidokoro 외, HRI 2013)의 '실제 쇼핑몰 시험'이 원문 미열람·검색 결과 기준이고, 병원 사례는 기사 1건, 실외·제조 공장·가정 사례 없음
- 섹션 6. 대표 접근법과 기술(주제 페이지로 분리) — 2023 년 이후 움직임 지도 기반 장기 예측·배정 연구와 시설 센서 사람 검출을 교통 제약으로 바꾸는 방식이 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스(주제 페이지로 분리) — REP-155 의 현재 상태(Draft 여부) 재확인 필요, Open-RMF 의 사람 장애물 메시지·검출 패키지 미기재
- 섹션 8. 대표 연구와 자료(주제 페이지로 분리) — 움직임 지도 서베이(ref-1171)·Kidokoro 외(ref-1182) 원문 미열람
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 — 직접 범위 서술이 추정뿐이고 오케스트레이션 계층의 구현 사례가 없음
- 섹션 11. 열린 질문 — oq-272·oq-273·oq-274·oq-298·oq-303 에 근거가 없음

## 조사 질문

1. 현장 사람의 위치와 흐름을 어떻게 알고 계획과 안전에 반영할 것인가? [분류원문]
2. 게시 페이지가 원문 미열람·검색 결과 기준으로 둔 주장(Kidokoro 외 쇼핑몰 시험, 움직임 지도 서베이의 정의, REP-155 의 상태, ATC 데이터셋의 추적 방식)은 원문·초록 기준으로 여전히 맞는가? (섹션 5·7·8 재확인)
3. oq-272 여러 제조사 로봇과 설비 센서가 각자 감지한 사람 위치를 하나의 사람 흐름 모델로 합칠 때 좌표·시각·신뢰도·익명화 형식을 정한 공개 규격이나 구현이 있는가? (섹션 7·9)
4. oq-273 병원·상업 시설·물류창고에서 시간대별 사람 혼잡을 로봇 작업 시간 추정과 배정·스케줄링에 반영해 처리 시간이나 지연 변화를 측정한 현장 연구가 있는가? (섹션 5·6)
5. oq-274 공공 인파 밀집 데이터를 실외 배송로봇의 경로·운행 제한에 연동한 국내 사례나 데이터 제공 조건이 있는가? (섹션 5·9)
6. oq-298 시간대별 사람 흐름을 담은 움직임 지도를 장소 목록·지도 판과 함께 관리하고 경로·작업 시간 계획에 넘기는 공통 형식이나 현장 사례가 있는가? (섹션 6·7)
7. 제조 공장·가정·실외 현장에서 사람 흐름·혼잡을 로봇 운영에 반영한 사례가 있는가? (섹션 5)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | ROS 규약 제안 REP-155(ROS4HRI)는 2026-10-09 확인 기준으로도 상태가 Draft, 유형이 Informational 이며, 식별되지 않은 사람을 익명 사람으로 표시하되 그 ID 는 영속을 보장하지 않고, 개인정보·동의는 다루지 않는다. | ref-1173 | 아니오 | medium | 2026-10-09 | 작업 대상 | — |
| f2 | [사실] | Kucner 외 서베이(IJRR 42(11), 2023-09)의 초록은 움직임 지도를 환경의 전형적 움직임 패턴을 기록한 지도로 정의하고, 궤적이나 짧고 끊긴 움직임 관측으로 만들며 전역 경로 계획·위치추정 개선·사람 움직임 예측에 쓰인다고 하고, 새 분류 체계를 제안하며 이 분야가 실제 적용에 이를 만큼 성숙했지만 빠르게 발전 중이라고 결론짓는다. | ref-1171 | 아니오 | medium | 2023-09 | — | — |
| f3 | [사실] | Kidokoro 외(HRI 2013)의 초록은 보행자 흐름·보행자 상호작용·보행 쾌적성의 세 모델로 로봇이 사람 사이를 다니는 가상 상황을 시뮬레이션하는 방법을 친근한 순찰(friendly-patrolling) 시나리오에 구현했고, 현장 실험에서 노출만 최대화한 로봇보다 주변 보행자가 보행 쾌적성을 더 좋게 인식했다고 적지만, 실험 장소가 쇼핑몰이라고는 밝히지 않는다. | ref-1182 | 아니오 | medium | 2013-03 | 제약 | — |
| f4 | [사실] | 같은 연구의 확장판(Kidokoro 외, IEEE Transactions on Robotics 31(6), 2015)은 로봇 주변 군중 형성 예측·보행 쾌적성 추정·혼잡 사전 회피 계획을 결합해 다음 이동 단계를 고르는 방법을 실제 쇼핑몰에서 시험해, 혼잡으로 인한 로봇의 보행 쾌적성 영향을 줄였다고 초록에 적는다. | ref-1479 | 아니오 | medium | 2015-11-11 | 상업 시설 / 제약 | — |
| f5 | [사실] | ATC 데이터셋을 공개한 ATR 연구진(Brščić 외, IEEE THMS 43(6), 2013)은 사람 키보다 높게 단 여러 3차원 거리 센서로 넓은 공공 공간에서 사람의 위치·방향·키를 추적하는 방법을 쇼핑센터에 구현했다고 보고했다. | ref-1480, ref-1176 | 아니오 | medium | 2013-10-17 | 상업 시설 / 작업 대상 | — |
| f6 | [사실] | Open-RMF 의 장애물 메시지(rmf_obstacle_msgs/Obstacle)는 헤더의 좌표 프레임·시각, 발행 주체(source), 층 이름(level_name), 분류 라벨(예: human), 3차원 경계 상자, 예상 수명(lifetime), 추가·삭제 동작을 담으며, 확인한 정의에는 검출 신뢰도나 익명화를 위한 필드가 없다. | ref-1484 | 아니오 | medium | 2026-10-09 | 작업 대상 | — |
| f7 | [사실] | Open-RMF 의 rmf_obstacle 저장소는 기존 CCTV·영상 센서로 군중을 검출하는 용도의 사람 검출 노드(단안 카메라 YOLO-V4, OAK-D 카메라)를 두고, lane_blocker 노드가 /rmf_obstacles 의 장애물이 플릿 주행 차선과 겹치면 차선을 닫았다가 비면 다시 열거나 속도 제한(기본 0.5 m/s)을 건다. | ref-1485 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f8 | [추정] | f6·f7 에 따르면 시설 카메라의 사람 검출 결과를 층·발행 주체·수명과 함께 모아 여러 플릿의 차선 폐쇄·속도 제한으로 바꾸는 경로가 오케스트레이션 계층(Open-RMF)에 이미 있어 19. 사람·보행자 모델의 ROP 직접 범위 예시가 될 수 있으나, 신뢰도·익명화 형식은 정해져 있지 않아 oq-272 는 부분적으로만 답해진 것으로 보인다. | ref-1484, ref-1485, ref-1173 | 아니오 | low | 2026-10-09 | 제약 | — |
| f9 | [사실] | Kazemi Eskeri 외(IROS 2025)는 시간대별 사람 존재 확률을 담은 이산 격자형 움직임 지도를 다중 로봇 작업 배정의 확률적 비용에 넣어, ATC 쇼핑몰 데이터의 기록 궤적을 재생한 시뮬레이션에서 임무 완료 시간을 움직임 무시 방법 대비 최대 26%, 기준 방법 대비 최대 19% 줄였다고 보고했으며 실제 로봇 실험은 없다. | ref-1083 | 아니오 | medium | 2025-08-27 | 예외·성과 | — |
| f10 | [사실] | 고려대학교 구로병원 연구(Lee 외, Digital Health 12, 2026)는 약제부→응급실 직원 전용 승강기 경로에서 의약품 배송로봇(DOGU IROI)의 비긴급 임무 122건(2025-06-18~29)을 분석해 전체 성공률 87.03%, 승강기 가동률 59.01% 미만에서 95.52% 였고, 실패 14건 가운데 8건이 승강기 탑승·하차 중 막힘이었으며 탑승 인원이 1명 늘 때 실패 오즈비가 1.73 이었다고 보고했다. | ref-1487 | 아니오 | medium | 2026-03-31 | 병원 / 예외·성과 | — |
| f11 | [사실] | 같은 연구는 혼잡이 임계값 아래일 때 로봇 배송을 배정하고, 승강기가 운행 중이며 가동률이 60% 이상이면 출발을 미루도록 권고하며, 59.01% 임계값은 현장 고유값이라 다른 곳에서는 다시 보정해야 한다고 적는다. | ref-1487 | 아니오 | medium | 2026-03-31 | 병원 / 제약 | — |
| f12 | [추정] | oq-273 에 대해 f9(쇼핑몰 데이터 기반 시뮬레이션)와 f10·f11(병원 승강기 혼잡의 현장 측정)은 사람 혼잡이 로봇 작업 시간·실패에 주는 영향을 재고 배정 시점에 반영하는 근거가 되지만, 복도·구역 단위의 시간대별 사람 흐름을 작업 시간 추정과 스케줄링에 넣어 현장에서 효과를 잰 연구는 이번에도 찾지 못했다. | ref-1083, ref-1487 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f13 | [사실] | Gehrke 외(Transportation Research Interdisciplinary Perspectives 18, 2023)는 미국 노던애리조나대학교 캠퍼스 10곳에서 일주일간 녹화한 영상으로 보도 자율 배송로봇과 보행자·자전거 이용자의 상호작용 빈도·심각도를 침범 후 시간(PET)으로 재고, 중간·위험 충돌의 예측 요인을 모델링했다. | ref-1481 | 아니오 | medium | 2023-03-01 | 실외 / 제약 | — |
| f14 | [사실] | 노던애리조나대학교 보도(2023-05-16)에 따르면 이 연구에서 충돌(0초)이 12건 관찰됐고, 보도가 좁고 교차가 많은 지점일수록 위험 상호작용이 많았으며, 연구진은 넓은 보도에서 나란히 주행하도록 경로를 정하고 사람이 많은 지점의 횡단을 줄이며 덜 붐비는 표시된 지점으로 배송하도록 권고했다. | ref-1482 | 아니오 | medium | 2023-05-16 | 실외 / 제약 | — |
| f15 | [추정] | f13·f14 에 따르면 실외 보도 로봇의 보행자 충돌 위험은 보도 폭·교차 수·사람 활동량 같은 지점 특성과 이어지므로, ROP 가 실외 경로망에 지점별 보행자 활동·폭 속성을 두고 경로·배송 지점 선택의 비용으로 쓰는 방식이 19. 사람·보행자 모델과 27. 다중 로봇 경로·교통 관리 — MAPF 를 잇는 것으로 보인다. | ref-1481, ref-1482 | 아니오 | low | 2026-10-09 | 실외 / 제약 | — |
| f16 | [사실] | 연계 대상: 2024-08 경기 의왕시 부곡파출소 앞 횡단보도에서 경찰청 실시간 교통신호정보를 현대차·기아 로보틱스랩 관제 시스템과 연동해, 실외 이동로봇이 카메라 신호 인식과 별도로 신호 상태를 실시간으로 받아 횡단보도를 건너는 시연이 열렸다. | ref-1483 | 아니오 | low | 2024-08-10 | 실외 / 시작 조건 | — |
| f17 | [추정] | oq-274 에 대해 국내에서는 공공 교통신호 데이터를 실외 로봇 관제 시스템에 연동한 시연(f16)은 확인되지만, 인파관리지원시스템 같은 공공 인파 밀집 데이터를 로봇 경로·운행 제한에 연동한 사례나 데이터 제공 조건은 이번에도 찾지 못했다. | ref-1483, ref-1177 | 아니오 | low | 2026-10-09 | 실외 / 시작 조건 | — |
| f18 | [사실] | 현대자동차·기아와 한림대학교의료원은 2025-04-07 한림대학교성심병원을 시험장으로 병원 맞춤형 배송 로봇과 관제 시스템을 함께 개발·실증하는 협약을 맺으면서 병원을 환자·의료진·휠체어·이동식 침대가 섞인 고밀도 환경으로 규정했으나, 이 발표는 조선비즈 기사(2024-07)의 로봇 대수나 사람·휠체어 앞 대기 규칙을 확인해 주지 않는다. | ref-1488, ref-1181 | 아니오 | medium | 2025-04-07 | 병원 / 제약 | — |
| f19 | [사실] | Kairos(Catalano 외, arXiv 프리프린트 2026-09-23)는 3차원 장면 그래프의 복셀마다 사람 존재율과 이동 방향 분포를 두고 임의의 미래 시각을 스펙트럼 예측기로 예측해 주행 노드 단위로 모으는 4차원 장면 그래프를 제안했고, 로봇이 모은 캠퍼스·쇼핑몰·11개월 역 구내 데이터로 평가해 사람을 만나는 계획 과제에서 시간 불변 지도보다 같은 성공률로 더 많은 사람을 만났다고 보고했다. | ref-1486 | 아니오 | medium | 2026-09-23 | — | — |
| f20 | [추정] | oq-298 에 대해 f19 처럼 사람 존재·흐름 예측을 장면 그래프의 장소·주행 노드에 붙이는 연구 구현은 있으나, 움직임 지도를 장소 목록·지도 판과 함께 관리하는 공통 형식이나 현장 운영 사례는 이번에도 찾지 못했다. | ref-1486, ref-1171 | 아니오 | low | 2026-10-09 | — | — |
| f21 | [사실] | Zhu 외(arXiv 2025-10-03, IEEE RA-L 표기)는 시간대별 움직임 패턴을 담는 시간 조건부 움직임 지도를 써서 최대 60초 앞의 사람 움직임을 예측해, 실제 데이터셋 두 개에서 학습 기반 방법보다 평균 변위 오차를 최대 50% 줄였다고 보고했다. | ref-1489 | 아니오 | medium | 2025-10-03 | — | — |
| f22 | [사실] | Open-RMF 시뮬레이션 문서는 하드웨어 시험에서 기록한 데이터로 시뮬레이션 상황을 다시 만들 수 있다고 적고, menge 를 엔진으로 쓰는 선택 기능 crowdsim 을 traffic_editor 에서 켜 airport_terminal 예제에서 가상 사람을 움직이게 하지만, 기록된 사람 흐름을 crowdsim 입력으로 옮기는 방법은 설명하지 않는다. | ref-406 | 아니오 | medium | 2026-10-09 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1171 | Kucner, T. P., Magnusson, M., Mghames, S., Palmieri, L., Verdoja, F., Swaminathan, C. S., Krajník, T., Schaffernicht, E., Bellotto, N., Hanheide, M., & Lilienthal, A. J. (The International Journal of Robotics Research 42(11)) | Survey of maps of dynamics for mobile robots | 2023 | 논문 | medium | 2026-10-09 | https://journals.sagepub.com/doi/10.1177/02783649231190428 | 아니오 |
| ref-1173 | ROS (ros-infrastructure/rep 저장소), Séverin Lemaignan | REP 155 -- Conventions, Topics, Interfaces for Perception in Human-Robot Interaction | 2022-01-11 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/ros-infrastructure/rep/blob/master/rep-0155.rst | 아니오 |
| ref-1176 | ATR (Advanced Telecommunications Research Institute International), Brščić, D. 외 | ATC shopping center tracking dataset | 미확인 | 정부·연구기관 | medium | 2026-10-09 | https://dil.atr.jp/crest2010_HRI/ATC_dataset/ | 예 |
| ref-1177 | 행정안전부 (대한민국 정책브리핑) | 29일부터 인파관리지원시스템 본격 운영…다중운집 인파사고 예방 | 2023-12-27 | 정부·연구기관 | medium | 2026-10-09 | https://www.korea.kr/news/policyNewsView.do?newsId=148924176 | 예 |
| ref-1181 | 조선비즈 (이정아, 다음 뉴스 게재) | 로봇과 인간이 공존하는 병원…약 배달 로봇에 길 비켜주고 엘리베이터도 잡아줘 | 2024-07-12 | 기사 | low | 2026-10-09 | https://v.daum.net/v/bc4riunbUE | 예 |
| ref-1182 | Kidokoro, H., Kanda, T., Brščić, D., & Shiomi, M. (ACM/IEEE HRI 2013) | Will I bother here? - A robot anticipating its influence on pedestrian walking comfort | 2013-03 | 논문 | medium | 2026-10-09 | https://www.semanticscholar.org/paper/Will-I-bother-here-A-robot-anticipating-its-on-Kidokoro-Kanda/bc0b26f1c13405fd89eb6d280bee739aed5b07a6 | 아니오 |
| ref-406 | Open Robotics | Simulation - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://osrf.github.io/ros2multirobotbook/simulation.html | 아니오 |
| ref-1083 | Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv) | Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments | 2025-08-27 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2508.19731 | 아니오 |
| ref-1479 | Kidokoro, H., Kanda, T., Brščić, D., & Shiomi, M. (IEEE Transactions on Robotics 31(6)) | Simulation-Based Behavior Planning to Prevent Congestion of Pedestrians Around a Robot | 2015-11-11 | 논문 | medium | 2026-10-09 | https://doi.org/10.1109/TRO.2015.2492862 | 아니오 |
| ref-1480 | Brščić, D., Kanda, T., Ikeda, T., & Miyashita, T. (IEEE Transactions on Human-Machine Systems 43(6)) | Person Tracking in Large Public Spaces Using 3-D Range Sensors | 2013-10-17 | 논문 | medium | 2026-10-09 | https://doi.org/10.1109/THMS.2013.2283945 | 아니오 |
| ref-1481 | Gehrke, S. R., Phair, C. D., Russo, B. J., & Smaglik, E. J. (Transportation Research Interdisciplinary Perspectives 18) | Observed sidewalk autonomous delivery robot interactions with pedestrians and bicyclists | 2023-03-01 | 논문 | medium | 2026-10-09 | https://doi.org/10.1016/j.trip.2023.100789 | 아니오 |
| ref-1482 | Northern Arizona University (NAU Review) | Got robot delivery? New research demonstrates need for robot-friendly infrastructure | 2023-05-16 | 정부·연구기관 | medium | 2026-10-09 | https://in.nau.edu/news/delivery-robot-research/ | 아니오 |
| ref-1483 | 보안뉴스 (박미영) | 경찰청 제공 실시간 교통신호정보, 보행자와 함께 거닐 실외 이동로봇의 눈이 되다 | 2024-08-10 | 기사 | low | 2026-10-09 | https://www.boannews.com/news/articleView.html?idxno=131956 | 아니오 |
| ref-1484 | Open Robotics (open-rmf/rmf_internal_msgs) | rmf_obstacle_msgs/msg/Obstacle.msg | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_obstacle_msgs/msg/Obstacle.msg | 아니오 |
| ref-1485 | Open Robotics (open-rmf/rmf_obstacle) | rmf_obstacle — README | 미확인 | 오픈소스 문서 | high | 2026-10-09 | https://github.com/open-rmf/rmf_obstacle | 아니오 |
| ref-1486 | Catalano, I., Placed, J. A., Civera, J., & Peña Queralta, J. (arXiv) | Kairos: Grounded Forecasting of Presence and Directional Flow in 4D Scene Graphs | 2026-09-23 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2609.27467 | 아니오 |
| ref-1487 | Lee, Y. 외, Park, I.-H. (교신) (Digital Health 12, 고려대학교 구로병원) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 2026-03-31 | 논문 | high | 2026-10-09 | https://journals.sagepub.com/doi/10.1177/20552076261437181 | 아니오 |
| ref-1488 | 현대자동차그룹 | 현대자동차·기아, 한림대의료원과 로봇 친화 병원 공동 구축 위한 업무협약 체결 | 2025-04-07 | 벤더 문서 | medium | 2026-10-09 | https://www.hyundaimotorgroup.com/ko/news/CONT0000000000173736 | 아니오 |
| ref-1489 | Zhu, Y., Rudenko, A., Kucner, T. P., Lilienthal, A. J., & Magnusson, M. (arXiv; IEEE RA-L 표기) | Long-Term Human Motion Prediction Using Spatio-Temporal Maps of Dynamics | 2025-10-03 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2510.03031 | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/objects-people-and-live-state/people-and-pedestrian-model.md | 5, 6, 7, 8, 9, 11 | 갱신(차등): 섹션 5 — 상업 시설 사례의 쇼핑몰 시험 근거를 바로잡음: HRI 2013 초록(f3, ref-1182)은 친근한 순찰 시나리오의 현장 실험만 적고 쇼핑몰을 밝히지 않으며, 쇼핑몰 시험은 TRO 2015 확장판(f4, ref-1479)의 초록에 있으므로 사례 제목·각주를 ref-1479 중심으로 고치고 '원문 미열람, 검색 결과 기준' 문구를 정리. ATC 데이터셋 추적 방식은 f5 로 보강(같은 저자군이라 교차 확인 아님). 병원 — 고려대학교 구로병원 승강기 혼잡 사례(f10·f11, 한국, 여섯 항목: 수행 자원·제약·예외·성과) 추가, 한림대 사례는 f18 로 맥락만 보강하고 기사 1건 기준임을 유지. 실외 — 대학 캠퍼스 보도 배송로봇 관측 사례(f13·f14, f15) 추가로 '실외 사례 없음' 문장 수정, 의왕시 교통신호 연동 시연(f16)은 연계 대상으로 짧게. 제조 공장·가정은 여전히 사례 없음. 섹션 6(주제 페이지) — 시설 카메라 사람 검출→차선 폐쇄·속도 제한(f7), 움직임 지도 기반 배정(f9)·장기 예측(f21)·4D 장면 그래프 예측(f19). 섹션 7(주제 페이지) — REP-155 상태 Draft 재확인(f1), Open-RMF 장애물 메시지·rmf_obstacle(f6·f7). 섹션 8(주제 페이지) — 움직임 지도 서베이 초록 확인(f2), f9·f10·f13·f19·f21 추가. 섹션 9 — 직접 범위 예시로 f8(Open-RMF 장애물·lane_blocker), 외부 검출 모델 실행·카메라는 연계 대상. 섹션 11 — oq-272 부분 근거 f6·f8, oq-273 부분 근거 f9·f10·f11·f12, oq-274 부분 근거 f16·f17, oq-298 부분 근거 f19·f20, oq-303·oq-256 부분 근거 f22(모두 미해결 유지), 새 열린 질문 2건. 교차 규칙: 학습 기반 예측·배정(f9·f21)은 46. 예측·학습 기반 최적화와 25. 작업 배정 — MRTA 양쪽 연결, 현재 관측(f6·f7)은 18. 실시간 세계 상태·데이터 일관성, crowdsim(f22)은 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현 쪽으로 구분. 다음 실행 후보: 63. 병원·의료 페이지 5절에 f10·f11, 66. 실외 페이지에 f13·f14·f16, 27. 다중 로봇 경로·교통 관리 — MAPF 에 f7. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 평균 변위 오차 | Average Displacement Error (ADE) | 궤적 예측에서 예측 구간의 모든 시점에 대해 예측 위치와 실제 위치 사이 거리를 평균한 오차 지표이다. |
| 4차원 장면 그래프 | 4D Scene Graph | 3차원 장면 그래프의 장소·물체 노드에 시간 축을 더해 사람 존재나 흐름 같은 시간에 따라 변하는 상태를 함께 표현·예측하는 표현이다. |

## 열린 질문

새로 생긴 질문:

- 시설 카메라의 사람 검출 결과로 플릿 주행 차선을 닫거나 속도를 제한하는 방식(Open-RMF lane_blocker)을 여러 제조사 로봇 현장에서 운영할 때 오검출·과도한 차선 폐쇄가 처리량과 지연에 주는 영향을 측정한 자료가 있는가? | 관련 영역: 19. 사람·보행자 모델, 27. 다중 로봇 경로·교통 관리 — MAPF, 18. 실시간 세계 상태·데이터 일관성 | 근거: f7 | 종류: 일반
- 병원 승강기 가동률·탑승 인원 같은 혼잡 임계값(예: 고려대 구로병원의 약 60%)을 다른 병원·건물로 옮겨 로봇 배정 시점에 쓸 때 재보정하는 방법이나 다기관 연구가 있는가? | 관련 영역: 19. 사람·보행자 모델, 26. 작업 순서·스케줄링, 22. 설비·건물 시스템 연동 | 근거: f11 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 19 · 교차 확인: 0
- 예산 사용량: 검색 15회 · 신규 출처 11건
- 미확인 항목:
    - Kidokoro 외 HRI 2013 과 TRO 2015 는 OpenAlex 초록만 열었고 본문 미열람(IEEE Xplore 빈 응답, CroRIS 대기 페이지). 쇼핑몰 효과 수치 미확인
    - ref-1171 움직임 지도 서베이는 Aalto 포털 초록만 열었고 본문 PDF 는 추출 실패
    - f5 는 ATC 데이터셋(ref-1176)과 같은 저자군의 논문이라 독립 교차 확인 아님. ATC 센서 49대·약 900㎡ 수치는 이번에 다시 확인하지 않음
    - f14 는 ref-1481 과 같은 대학의 보도라 독립 출처 아님. 논문 본문(충돌 수·예측 요인 계수) 미열람
    - f10·f11 고려대 구로병원 연구는 단일 출처, 교차 확인 실패
    - f18 은 조선비즈 기사(ref-1181)의 로봇 73대·대기 규칙을 확인해 주지 않음. 한림대 사례의 독립 확인은 여전히 실패
    - f19 Kairos 는 동료심사 전 프리프린트, 계획 과제의 목적(만남 최대화)은 본문 앞부분 기준 해석이며 데이터셋 이름(ATC·HB 표기)과의 대응 미확인
    - f21 의 데이터셋 이름 미확인(초록에 없음)
    - Open-RMF rmf_obstacle 의 이슈 #22(장애물 서버 통합 계획)는 403 으로 열지 못함
    - STRANDS 요양시설 배치에서 FreMEn 으로 상호작용 확률을 예측해 일정을 짠 내용은 PDF 추출 실패로 출처로 넣지 않음
    - 제조 공장·가정 현장의 사람 흐름 반영 사례는 이번에도 찾지 못함
    - 공공 인파 밀집 데이터의 실외 로봇 연동 국내 사례 미발견(oq-274)
- 범위 경계 위반 의심:
    - f7·f8: 카메라 영상의 사람 검출 모델 실행은 원문 19장 '로봇 자체 지능·제어'·센서 인식 쪽에 가까워 연계 대상으로 두고, ROP 직접 범위는 검출 결과(장애물 메시지)를 모아 차선 폐쇄·속도 제한 같은 교통 제약으로 쓰는 부분으로 한정해야 함
    - f16: 교통신호 시스템은 시설·공공 시스템 경계의 연계 대상이므로 claim 을 '연계 대상: '으로 시작
    - f10·f11: 승강기 운행·호출 제어는 시설·설비 제어 경계의 연계 대상이며, ROP 쪽은 혼잡 지표를 받아 배정·출발 시점을 정하는 부분으로만 서술해야 함
    - f13·f14: 보도 위 국소 회피·양보 동작은 로봇 제조사 몫이며, ROP 쪽은 경로·배송 지점 선택 비용(f15, 추정)으로만 연결
- 한계: web_fetch_available: true · fetch_mode full. 갱신(update) 실행으로, 정정 요청이 없어 원문 미열람·검색 결과 기준이던 주장의 재확인과 약한 절(5·7·9·11)과 열린 질문(oq-272·oq-273·oq-274·oq-298·oq-303)만 조사했다. 검색 15회/30, 신규 출처 11건/15(ref-1479~ref-1489, 예약 구간 안). 재사용 8건 가운데 ref-1171(Aalto 초록)·ref-1173(github_raw)·ref-1182(OpenAlex 초록)·ref-1083(arXiv)·ref-406(inbox 원문)은 이번에 열었고, ref-1176·ref-1177·ref-1181 은 열지 않았다(fetched false). 신규 11건은 모두 원문 또는 공식 초록을 열었다. 다만 ref-1479·ref-1480·ref-1481 은 OpenAlex 초록만 열었다. 교차 확인 0건이다. 같은 저자군·같은 기관 쌍(ref-1480과 ref-1176, ref-1482와 ref-1481)은 독립 출처로 보지 않았다. 주요 정정 근거: 5절 상업 시설 사례의 '실제 쇼핑몰 시험'은 HRI 2013 초록에 없고 TRO 2015 확장판 초록에 있다(f3·f4). 7절 REP-155 는 2026-10-09 원문 기준으로 여전히 Draft 이며(f1), 지난 실행의 '공식 채택' 검색 요약과의 차이는 원문 기준으로 정리된다. 한국 자료: 신규 ref-1483(보안뉴스)·ref-1487(고려대 구로병원)·ref-1488(현대자동차그룹), 재사용 ref-1177·ref-1181. 현장 유형: 병원(f10·f11·f18)·상업 시설(f4·f5)·실외(f13·f14·f15·f16·f17)이며 물류창고는 기존 ILIAD 사례를 유지하고 새 근거는 찾지 않았다. 제조 공장·가정 사례는 없다. 18. 실시간 세계 상태·데이터 일관성(현재 관측: f6·f7)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래 실험: f22)을 구분했다. L. AI·학습 기술 관련 f9·f21 은 46. 예측·학습 기반 최적화와 25. 작업 배정 — MRTA 에 함께 연결하자고 제안했다. 열린 질문에 대한 부분 근거: oq-272(f6·f8), oq-273(f9·f10·f11·f12), oq-274(f16·f17), oq-298(f19·f20), oq-303·oq-256(f22). 해결 제안은 없다. 벤더 기능·성능 주장은 없다(f18 은 협약 내용 진술이다). 페이지 갱신 제안은 1건(대상 영역 페이지)이며 63. 병원·의료, 66. 실외, 27. 다중 로봇 경로·교통 관리 — MAPF 반영은 다음 실행 후보로 남겼다. 입력 누락 없음, 우선 지정 질문 없음.
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

### runs/2026-09-30-12/research.md

```markdown
# 리서치 브리프 2026-09-30-12

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-30-12 |
| 날짜 | 2026-09-30 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 33. 시나리오 모델·편집 |
| 대분류 | I. 설계·시뮬레이션 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음 — 시나리오 기술 언어, 정적 환경과 동적 내용의 분리, 매개변수화·카탈로그, 장애 주입 선언, 반증 기반 시험 용어 없음
- 섹션 5. 적용 사례 (현장 유형 명시) 비어 있음 — 상업 시설(호텔·공항)·병원(클리닉)·실외(캠퍼스)·가정(가정 활동)·제조 공장(배터리 생산) 시나리오 예제와 여섯 항목 정리 없음
- 섹션 6. 대표 접근법과 기술 비어 있음 — 확률적 시나리오 언어, 건물 주석 편집기, 행동 트리·BPMN 같은 미션 형식, LLM 기반 환경·시나리오 생성 근거 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음 — ASAM OpenSCENARIO, SDFormat, VDMA LIF, Open-RMF rmf_demos·traffic-editor, BEHAVIOR-1K·BDDL, NIST ARIAC, MovingAI MAPF 벤치마크, Groot2 위치 없음
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (책임 경계 기준) 비어 있음
- 섹션 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) 비어 있음
- 섹션 11. 열린 질문 비어 있음 — 이 영역에 걸린 기존 열린 질문 oq-131·oq-135 반영 필요
- 프런트매터 related_areas·sources 비어 있음

## 조사 질문

1. 현장·로봇·사람·작업을 담은 시나리오를 어떻게 표현하고 다시 쓸 것인가? [분류원문]
2. 로봇 시뮬레이션·자율 시스템 시험에서 쓰는 시나리오 기술 형식·언어는 무엇이며 환경·개체·작업·사건·장애를 어떻게 나누어 담고 판(버전)을 어떻게 관리하는가? (섹션 4·6·7 겨냥)
3. 현장 유형별(호텔·병원·공장·가정·실외·물류창고) 시나리오 예제·템플릿 라이브러리로 공개된 것은 무엇이고 각각 무엇을 담는가? (섹션 5·7 겨냥, 한국 자료 우선)
4. 사람이 화면에서 시나리오·워크플로·미션을 그리고 고치는 편집기와 미션 기술 형식(행동 트리·상태 기계·BPMN 등)은 무엇이며 비교 연구는 무엇을 말하는가? (섹션 6·7·8 겨냥)
5. 언어 모델로 시뮬레이션 환경·시나리오를 자동 생성하는 연구는 무엇을 입력으로 받아 무엇을 만들고 어떻게 평가했는가? (섹션 6·8 겨냥, 9. 채팅으로 시나리오 구성과의 연결)
6. oq-131 플릿 관제 실행 기록을 시나리오 사양으로 바꾸는 공개 형식·변환 규칙, oq-135 시나리오 구성 시 되물어야 할 항목의 표준 목록이 있는가? (섹션 11 겨냥)
7. 33. 시나리오 모델·편집에서 ROP가 직접 맡을 것과 시뮬레이션 엔진·로봇 제조사·설비 쪽에 맡길 것의 경계는 어디이며 어느 영역과 연결되는가? (섹션 9·10 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Vin 외의 Scenic 3.0(CAV 2023)은 자율 시스템·로봇의 환경을 모델링하는 확률적 프로그래밍 언어 Scenic 에 3차원 기하, 가림을 고려한 광선 추적 기반 가시성 판정을 갖춘 정밀 형상 모델, 선형 시간 논리(LTL)로 쓰는 시간 요구사항을 더해 반증(falsification) 기반 시험에 쓸 수 있게 했다. | ref-1135 | 아니오 | medium | 2023-07 | — | — |
| f2 | [사실] | ASAM OpenSCENARIO XML 은 주행·교통 시뮬레이터의 동적 내용(차량·보행자 등 여러 개체의 동기화된 기동)을 계층 구조의 XML 파일(.xosc)로 기술하는 표준으로, 2026-05-19 에 1.4.0 판이 나왔고, 기동·동작·궤적을 카탈로그로 묶고 시나리오 전체를 매개변수화해 시나리오 파일을 대량으로 만들지 않고도 시험을 자동화할 수 있게 한다. | ref-1141 | 아니오 | medium | 2026-05-19 | — | — |
| f3 | [사실] | ASAM 은 도로망은 OpenDRIVE, 노면 형상은 OpenCRG 로 따로 기술하고 OpenSCENARIO XML 은 그 위의 동적 내용만 담게 나누며, 병행 표준 OpenSCENARIO DSL 은 대규모 검증용, XML 은 예측 가능한 정밀 시나리오용으로 역할을 구분한다. | ref-1141 | 아니오 | medium | 2026-05-19 | — | — |
| f4 | [사실] | Open-RMF 의 rmf_demos 는 호텔 월드로 로비와 객실 2개 층, 승강기 2대, 여러 문, 로봇 플릿 3개(로봇 4대)가 층을 오가며 순찰(loop)·청소 작업을 하는 다중 플릿 시나리오를 예제로 제공한다. | ref-104 | 아니오 | medium | 2026-09-30 | 상업 시설 / 수행 자원 | — |
| f5 | [사실] | rmf_demos 의 공항 터미널 월드는 차선·목적지·로봇이 많은 대형 지도에서 여러 플릿과 설비·이용자의 상호작용을 보이며, 선택적으로 군중 시뮬레이션을 켜고 사람이 직접 모는 읽기 전용(read_only) 카트를 함께 두고 순찰·배송·청소 작업을 실행한다. | ref-104 | 아니오 | medium | 2026-09-30 | 상업 시설 / 제약 | — |
| f6 | [사실] | rmf_demos 의 클리닉 월드는 승강기 2대가 있는 2개 층 시설에서 역할이 다른 로봇 플릿 2개가 층을 오가며 간호 스테이션 사이를 순찰하는 병원형 시나리오 예제다. | ref-104 | 아니오 | medium | 2026-09-30 | 병원 / 제약 | — |
| f7 | [사실] | rmf_demos 의 캠퍼스 월드는 차선을 GPS WGS84 좌표로 행성 규모에 주석한 넓은 캠퍼스에서 여러 배송 로봇이 장거리 순찰을 하는 실외 시나리오 예제이고, 제조·물류 월드는 컨베이어·고정 매니퓰레이터 작업셀과 여러 AMR 플릿의 연동을 영상으로만 보인다. | ref-104 | 아니오 | medium | 2026-09-30 | 실외 / 작업 대상 | — |
| f8 | [사실] | rmf_demos 에서 시나리오는 월드(건물 구성·차선·승강기·문·충전 위치)를 띄운 뒤 dispatch_patrol·dispatch_delivery·dispatch_clean 같은 명령으로 작업을 따로 넣는 구조이며, 디스패처가 플릿 어댑터들 사이의 작업 입찰을 조율한다. | ref-104 | 아니오 | medium | 2026-09-30 | 시작 조건 | — |
| f9 | [사실] | Open-RMF 의 traffic-editor 는 시설 지도 위에 벽·문(여닫이·미닫이·양문)·층·승강기, 최대 9개 그래프의 교통 차선, 충전·주차·대기·도킹·시뮬레이션 로봇 생성 위치 같은 웨이포인트 속성, 층 정렬용 기준점을 그려 넣는 GUI 편집기로, 결과를 .building.yaml 파일로 저장하고 building_map_generator 가 이를 물리 시뮬레이션 월드로 자동 생성한다. | ref-079 | 아니오 | medium | 2026-09-30 | — | — |
| f10 | [사실] | Stanford 등의 BEHAVIOR-1K(arXiv 2403.09227, 예비판 CoRL 2022)는 '로봇이 무엇을 해 주길 바라는가' 설문으로 고른 일상 가정 활동 1,000개를 행동 영역 정의 언어(BDDL)로 형식 명세하고, 주택·정원·식당·사무실 등 장면 50개와 물리·의미 속성을 주석한 객체 9,000개 이상, 강체·변형체·액체를 다루는 OmniGibson 시뮬레이터 위에 구현한 활동 라이브러리다. | ref-971 | 아니오 | medium | 2024-03 | 가정 / 작업 대상 | — |
| f11 | [사실] | NIST ARIAC 문서의 시나리오는 전기차 배터리 생산 시설로, 배터리 셀 4개를 트레이에 담는 키팅과 셀 4개와 상하 케이스로 모듈을 조립하는 두 작업을 주문으로 받고, 우선순위가 높은 주문이 남아 있으면 경기 상태가 '주문 완료'로 바뀌지 않게 정한다. | ref-1140 | 아니오 | medium | 2026-09-30 | 제조 공장 / 작업 대상 | — |
| f12 | [사실] | NIST ARIAC 는 컨베이어 고장(START_TIME·DURATION), 전압 시험기 고장(시작·지속·대상 TESTER), 진공 그리퍼 파지 실패(TOOL·몇 번째 파지인지 GRASP_OCCURRENCE), 긴급 주문(START_TIME·ID) 네 가지 민첩성 과제를 매개변수로 선언해, 장애와 긴급 요청을 시각 또는 발생 횟수 조건으로 시나리오에 주입한다. | ref-528 | 아니오 | medium | 2026-09-30 | 제조 공장 / 예외·성과 | — |
| f13 | [사실] | Kästner 외의 Arena-Bench(RA-L 2022)는 동적 환경의 시나리오·월드 생성 도구와 평가 지표를 갖춘 벤치마크 모음으로, 3차원 환경에서 여러 로봇 플랫폼의 모델 기반·학습 기반 주행 계획기를 같은 시나리오로 비교하고 실물 로봇 배치까지 보였다. | ref-726 | 아니오 | medium | 2022-06 | — | — |
| f14 | [사실] | Shcherbyna 외의 Arena 4.0(arXiv 2409.12471)은 대규모 언어 모델과 확산 모델로 텍스트 설명이나 2D 평면 배치에서 사람이 있는 주행 환경을 생성하고, 의미 주석이 달린 3D 자산 데이터베이스로 객체를 배치하며, 사용자 연구에서 이전 판보다 사용성·효율이 나아졌다고 보고했다. | ref-1143 | 아니오 | medium | 2024-09 | — | — |
| f15 | [사실] | Yang 외의 Holodeck(CVPR 2024)은 GPT-4 가 텍스트 설명에서 평면 배치·재질·문과 창을 정하고 공간 관계 제약을 만들어 최적화로 Objaverse 3D 자산을 배치하는 방식으로 오락실·스파·박물관 같은 상호작용 가능한 환경을 자동 생성하며, 주거 장면에서 평가자가 절차적 생성 기준선보다 선호했고 사람이 만든 데이터 없이 음악실·어린이집 같은 새 장면의 주행 학습에 썼다. | ref-815 | 아니오 | medium | 2023-12 | — | — |
| f16 | [추정] | 행동 트리 편집기 Groot2 는 끌어놓기로 트리를 만들며 XML 을 실시간으로 미리 보고, 실행 중인 BehaviorTree.CPP 실행기에 붙어 상태를 보여 주고 전이를 로그로 기록해 속도를 바꿔 재생하며, 유료판에서 블랙보드 표시·중단점·장애 주입을 제공한다고 밝힌다. | ref-1145 | 아니오 | low | 2026-09-30 | — | 벤더 주장 |
| f17 | [사실] | Filippone·Pettinari·Pelliccione(IEEE TSE, arXiv 2603.15427)는 단일·다중 로봇 미션 기술 형식으로 행동 트리·상태 기계·계층적 작업 네트워크(HTN)·BPMN 을 제어 구조·표현력·도구 지원 측면에서 비교하며, 미션을 명세하는 표준이나 널리 받아들여진 형식이 없고 미션은 로봇 전문가가 아닌 도메인 전문가가 정의하는 경우가 많다고 지적했다. | ref-116 | 아니오 | medium | 2026-03 | — | — |
| f18 | [사실] | Moving AI 연구실의 MAPF 벤치마크는 도시·게임·창고형·무작위·미로·방 등 격자 지도 36개마다 출발·도착 쌍을 담은 .scen 시나리오 파일을 무작위형 25개·균등형 25개씩 두어 모두 1,800개의 시나리오 파일을 공개한 재사용 가능한 시나리오 라이브러리다. | ref-1147 | 아니오 | medium | 2026-09-30 | — | — |
| f19 | [사실] | SDFormat(Simulation Description Format)은 로봇 시뮬레이터·시각화·제어용으로 로봇(기구학·동역학·센서)과 환경(조명·지형·OpenStreetMap 도로·3D 모델), 물리 설정을 기술하는 XML 형식으로, Gazebo 에서 시작했고 Open Source Robotics Foundation 이 Apache 2.0 으로 관리한다. | ref-1148 | 아니오 | medium | 2026-09-30 | — | — |
| f20 | [사실] | VDMA 의 레이아웃 교환 형식(LIF) 1.0.0(2023-09)은 무인운반차 통합업체가 주행 경로 레이아웃(간선·노드·스테이션)을 제3자 상위 관제 시스템에 처음 넘길 때 쓰는 비구속적 교환 형식이며, VDA 5050 인터페이스 정의의 영향을 받아 만들어졌다. | ref-046 | 아니오 | medium | 2023-09 | — | — |
| f21 | [추정] | 확인한 형식들은 공통으로 정적 환경(SDFormat 월드, Open-RMF .building.yaml, VDMA LIF 레이아웃, OpenDRIVE 도로망)과 동적 내용(작업 명령, OpenSCENARIO 스토리보드, ARIAC 주문·장애 과제, BDDL 활동)을 나누어 기술하며, 형식 자체의 판(OpenSCENARIO XML 1.4.0, LIF 1.0.0)은 두지만 개별 시나리오 인스턴스의 버전 관리 방식은 확인한 자료에서 찾지 못했다. | ref-1148, ref-079, ref-046, ref-1141, ref-104, ref-528, ref-971 | 아니오 | low | 2026-09-30 | — | — |
| f22 | [추정] | 확인한 자료를 종합하면 핵심 질문(현장·로봇·사람·작업을 담은 시나리오를 어떻게 표현하고 다시 쓸 것인가)에 대해, 공개 형식은 분야별로 나뉘어(자율주행 OpenSCENARIO, 가정 활동 BDDL, 시설 다중 로봇 Open-RMF 건물 파일과 작업 명령, 제조 ARIAC 과제 설정, MAPF .scen) 환경·로봇·사람·물품·작업·정책·물리·장애를 한 형식으로 담는 공통 표준은 찾지 못했고 미션 기술에도 표준이 없으며(f17), 재사용은 매개변수화·카탈로그(f2), 확률 분포 표본 추출(f1), 현장 유형별 예제 월드(f4~f7), 대규모 활동·시나리오 라이브러리(f10·f18), 언어 모델 생성(f14·f15)으로 이루어지는 것으로 보인다. | ref-1141, ref-971, ref-104, ref-528, ref-1147, ref-116, ref-1135, ref-1143, ref-815 | 아니오 | low | 2026-09-30 | — | — |
| f23 | [추정] | 확인한 자료를 종합하면 이 영역이 중요한 까닭은, 계획기·정책을 같은 조건에서 비교하려면 고정된 시나리오 파일이 있어야 하고(f13·f18), 장애·긴급 요청을 시나리오에 선언해야 예외 대응 시험을 반복할 수 있으며(f12), 매개변수화가 없으면 조건별 시나리오 파일이 불어나고(f2), 비전문가가 미션과 환경을 정의해야 하는데 공통 형식이 없기 때문이다(f17). | ref-726, ref-1147, ref-528, ref-1141, ref-116 | 아니오 | low | 2026-09-30 | — | — |
| f24 | [추정] | 확인한 자료를 종합하면 33. 시나리오 모델·편집에서 ROP가 직접 맡을 범위는 환경 참조·로봇 구성·사람 흐름·작업·정책·장애 주입을 묶은 버전 있는 시나리오 모델(f8·f12·f21), 현장 유형별 예제 라이브러리(f4~f7), 시설 주석·작업·미션을 그리는 편집기와 미션 형식 선택(f9·f16·f17), 시나리오를 여러 시뮬레이터 형식으로 내보내는 변환(f9·f19)으로 보인다. | ref-104, ref-528, ref-079, ref-1145, ref-116, ref-1148 | 아니오 | low | 2026-09-30 | — | — |
| f25 | [추정] | 연계 대상: 분류 원문 19장 기준으로 물리·센서 시뮬레이션 엔진과 로봇 기구학·센서 모델(SDFormat 로봇 기술, f19)은 시뮬레이터·로봇 제조사 쪽에, 컨베이어·작업셀 같은 설비 제어(f7·f12)는 설비 쪽에, 도로 교통 시나리오 표준(f2·f3)은 자율주행 분야에 속하므로, ROP 는 이들을 참조·변환해 시나리오에 묶는 역할을 맡을 것으로 보인다. | ref-1148, ref-104, ref-528, ref-1141 | 아니오 | low | 2026-09-30 | — | — |
| f26 | [추정] | 이 영역은 시나리오를 대화로 만드는 9. 채팅으로 시나리오 구성(f14·f15)과 11. 채팅으로 실제 상황 시뮬레이션 재현, 시나리오를 실행하는 34. 시뮬레이션·예측용 디지털 트윈(f19), 기록 재생·재현의 36. 가상 시운전·실제 상황 재현(f16), 규모 산정의 35. 처리능력·규모·배치 설계, 건물·레이아웃 주석의 14. 도면·BIM에서 지도 만들기·15. 지도·공간·위치 모델(f9·f20), 군중·보행자의 19. 사람·보행자 모델(f5·f14), 승강기 연동의 22. 설비·건물 시스템 연동(f4·f6), 미션 형식의 24. 작업·워크플로 모델링(f17), 장애 주입의 32. 예외 복구·재계획·업무 연속성(f12), 경로 시나리오의 27. 다중 로봇 경로·교통 관리 — MAPF(f18), 언어 모델 생성의 44. 로봇 기반 모델·언어 모델 계획(f15), 벤치마크의 54. 시험·형식 검증·벤치마크(f1·f13·f18), 적용 현장인 62. 제조 공장(f11·f12)·63. 병원·의료(f6)·64. 상업 시설(f4·f5)·65. 가정·공동주택(f10)·66. 실외(f7)와 이어진다. | ref-1143, ref-815, ref-1148, ref-1145, ref-079, ref-046, ref-104, ref-116, ref-528, ref-1147, ref-1135, ref-726, ref-1140, ref-971 | 아니오 | low | 2026-09-30 | — | — |

### 근거 발췌

(이전 브리프 요약: 이 소절은 생략했다)
## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1135 | Vin, E., Kashiwa, S., Rhea, M., Fremont, D. J., Kim, E., Dreossi, T., Ghosh, S., Yue, X., Sangiovanni-Vincentelli, A. L., & Seshia, S. A. (CAV 2023, arXiv) | 3D Environment Modeling for Falsification and Beyond with Scenic 3.0 | 2023-07 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2307.03325 | 아니오 |
| ref-104 | Open-RMF (open-rmf/rmf_demos) | rmf_demos — README | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://github.com/open-rmf/rmf_demos | 아니오 |
| ref-079 | Open Robotics (osrf/ros2multirobotbook) | Programming Multiple Robots with ROS 2 — Traffic Editor | 미확인 | 오픈소스 문서 | high | 2026-09-30 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 아니오 |
| ref-971 | Li, C., Zhang, R., Wong, J. 외 (Stanford, arXiv) | BEHAVIOR-1K: A Human-Centered, Embodied AI Benchmark with 1,000 Everyday Activities and Realistic Simulation | 2024-03 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2403.09227 | 아니오 |
| ref-528 | NIST (usnistgov/ARIAC_docs) | ARIAC Documentation — Challenges | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html | 아니오 |
| ref-1140 | NIST (usnistgov/ARIAC_docs) | ARIAC Documentation — Scenario | 미확인 | 정부·연구기관 | high | 2026-09-30 | https://pages.nist.gov/ARIAC_docs/en/latest/pages/scenario.html | 아니오 |
| ref-1141 | ASAM e.V. | ASAM OpenSCENARIO® XML | 미확인 | 표준 | high | 2026-09-30 | https://www.asam.net/standards/detail/openscenario-xml/ | 아니오 |
| ref-726 | Kästner, L., Bhuiyan, T., Le, T. A. 외 (RA-L 2022, arXiv) | Arena-Bench: A Benchmarking Suite for Obstacle Avoidance Approaches in Highly Dynamic Environments | 2022-06 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2206.05728 | 아니오 |
| ref-1143 | Shcherbyna, V. 외 (arXiv) | Arena 4.0: A Comprehensive ROS2 Development and Benchmarking Platform for Human-centric Navigation Using Generative-Model-based Environment Generation | 2024-09 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2409.12471 | 아니오 |
| ref-815 | Yang, Y., Sun, F.-Y., Weihs, L. 외 (CVPR 2024, arXiv) | Holodeck: Language Guided Generation of 3D Embodied AI Environments | 2023-12 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2312.09067 | 아니오 |
| ref-1145 | BehaviorTree.CPP 프로젝트 (behaviortree.dev) | Groot2 | 미확인 | 벤더 문서 | medium | 2026-09-30 | https://www.behaviortree.dev/groot/ | 아니오 |
| ref-116 | Filippone, G., Pettinari, S., & Pelliccione, P. (IEEE TSE, arXiv) | Formalisms for Robotic Mission Specification and Execution: A Comparative Analysis | 2026-03 | 논문 | medium | 2026-09-30 | https://arxiv.org/abs/2603.15427 | 아니오 |
| ref-1147 | Moving AI Lab (Sturtevant 외) | MAPF Benchmarks | 미확인 | 오픈소스 문서 | medium | 2026-09-30 | https://movingai.com/benchmarks/mapf/index.html | 아니오 |
| ref-1148 | Open Source Robotics Foundation | SDFormat (Simulation Description Format) | 미확인 | 오픈소스 문서 | high | 2026-09-30 | http://sdformat.org/ | 아니오 |
| ref-046 | VDMA (Intralogistics-2X-LIF) | Layout Interchange Format (LIF) — README | 2023-09 | 표준 | medium | 2026-09-30 | https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format | 아니오 |

### 출처 요약

(이전 브리프 요약: 이 소절은 생략했다)
## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/design-and-simulation/scenario-model-and-editing.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 섹션 3: f23(왜 중요한가), f22(핵심 질문 답, 추정) / 섹션 4: 확률적 시나리오 언어·반증 f1, 매개변수화·카탈로그 f2, 정적 환경과 동적 내용 분리 f3·f21, 장애 주입 선언 f12, 미션 기술 형식 f17 / 섹션 5: 상업 시설 — f4(호텔, 수행 자원)·f5(공항 터미널, 제약: 군중·수동 카트), 병원 — f6(클리닉, 제약: 층간 승강기), 실외 — f7(캠퍼스, 작업 대상: WGS84 공간), 가정 — f10(일상 활동 라이브러리), 제조 공장 — f11(배터리 생산 작업 대상)·f12(장애 주입 예외·성과). 물류창고는 f18 격자 지도와 f20 레이아웃 형식뿐이고 실제 현장 사례는 찾지 못함을 명시 / 섹션 6: 확률적 언어 f1, 건물 주석 편집 f9, 월드+작업 명령 구조 f8, 미션 형식 비교 f17, 행동 트리 편집·재생 f16(벤더 주장 병기), 언어 모델 기반 환경 생성 f14·f15 / 섹션 7: ASAM OpenSCENARIO f2·f3, SDFormat f19, VDMA LIF f20, Open-RMF rmf_demos·traffic-editor f4~f9, BEHAVIOR-1K·BDDL f10, NIST ARIAC f11·f12, MovingAI MAPF f18, Arena f13·f14, Groot2 f16 / 섹션 8: f1·f10·f13·f14·f15·f17 / 섹션 9: f24(직접 범위), f25(연계 대상) / 섹션 10: f26 — 9, 11, 14, 15, 19, 22, 24, 27, 32, 34, 35, 36, 44, 54, 62, 63, 64, 65, 66 / 섹션 11: 기존 oq-131·oq-135(미해결)와 open_questions_new 4건. 다음 실행 후보: 9. 채팅으로 시나리오 구성 페이지에 f14·f15, 36. 가상 시운전·실제 상황 재현 페이지에 f12·f16 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 오픈시나리오 | ASAM OpenSCENARIO | ASAM 이 관리하는 주행·교통 시뮬레이션 시나리오 기술 표준으로, 여러 개체의 동기화된 기동을 XML(.xosc) 또는 DSL 로 기술하고 카탈로그·매개변수화로 시나리오를 재사용하게 한다. |
| 행동 영역 정의 언어 | Behavior Domain Definition Language (BDDL) | BEHAVIOR 벤치마크가 가정 활동을 시뮬레이션된 물리 상태와 연결된 논리 술어로 형식 명세하는 데 쓰는 도메인 특화 언어다. |
| 시뮬레이션 기술 형식 | Simulation Description Format (SDFormat) | Gazebo 에서 시작해 Open Source Robotics Foundation 이 관리하는, 로봇과 환경·물리 설정을 시뮬레이터·시각화·제어용으로 기술하는 XML 형식이다. |
| 반증 기반 시험 | Falsification | 시나리오 공간을 탐색해 시스템이 명세(예: 시간 논리 요구)를 어기는 반례 시나리오를 찾아내는 시뮬레이션 기반 검증 방법이다. |

## 열린 질문

새로 생긴 질문:

- 환경·로봇·사람·물품·작업·정책·물리·장애를 담는 ROP 시나리오 형식을 SDFormat·Open-RMF 건물 파일·OpenSCENARIO 같은 기존 형식을 조합해 만들 것인가, 새로 정의하고 각 형식으로 내보낼 것인가? | 관련 영역: 33. 시나리오 모델·편집, 34. 시뮬레이션·예측용 디지털 트윈 | 근거: f21 | 종류: 일반
- 형식 판이 바뀔 때 개별 시나리오 인스턴스를 옮기고 호환성을 검사하는 버전 관리 규칙을 공개한 로봇 시뮬레이션 도구나 표준이 있는가? | 관련 영역: 33. 시나리오 모델·편집, 57. 자산·소프트웨어 수명주기 관리 | 근거: f21 | 종류: 일반
- ARIAC 처럼 장애·긴급 요청을 시각·발생 횟수 조건으로 선언하는 방식을 여러 제조사 로봇 플릿과 승강기·문 같은 설비 장애까지 일반화한 시나리오 형식이 있는가? | 관련 영역: 33. 시나리오 모델·편집, 32. 예외 복구·재계획·업무 연속성 | 근거: f12 | 종류: 일반
- 국내 아파트·병원·물류센터·호텔을 본뜬 다중 로봇 시나리오 예제 라이브러리를 공개한 기관이나 프로젝트가 있는가? | 관련 영역: 33. 시나리오 모델·편집, 65. 가정·공동주택 | 근거: f4 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 15 · 교차 확인: 0
- 예산 사용량: 검색 16회 · 신규 출처 15건
- 미확인 항목:
    - f10 BDDL 이 활동을 초기 조건·목표 조건 쌍으로 정의한다는 세부 구조는 검색 요약에만 있어 claim 에 넣지 않음
    - f1 Scenic 이 한 프로그램에서 표본 추출로 여러 장면을 만든다는 설명과 로봇 적용 사례(암석 지대)는 검색 요약에만 있어 넣지 않음
    - f15 Holodeck 3D 자산 수(약 5만 개)는 검색 요약에만 있어 넣지 않음
    - f13 Arena 시나리오 편집기의 끌어놓기 배치·보행자 웨이포인트 기능은 검색 요약에만 있어 넣지 않음
    - f16 Groot2 기능은 제품 페이지뿐이며 독립 출처로 교차 확인하지 못함
    - f2 OpenSCENARIO XML 1.4.0 명세 본문은 열지 않았고 공식 소개 페이지 기준
    - oq-131 미해결: 플릿 실행 기록을 시나리오로 바꾸는 공개 형식은 찾지 못함(찾은 JoyAI-Sim arXiv 2606.16776 은 탁상 조작 과제 재구성이라 제외)
    - oq-135 미해결: 시나리오 구성 시 되물을 항목의 표준 목록은 이번 조사에서 찾지 못함(검색하지 못함)
    - 물류창고 실제 현장의 시나리오 예제·템플릿 사례와 국내 자료는 찾지 못함
    - Bourr·Tiezzi 의 BPMN→X-Klaim 변환(arXiv 2311.04126)은 철회된 논문이라 제외
    - Moskovskaya 외 안내 로봇 LLM 시나리오 생성(arXiv 2509.10317)은 대화 행동 대본 의미의 시나리오라 제외
- 범위 경계 위반 의심:
    - f19: SDFormat 의 로봇 기구학·센서 기술은 로봇 제조사·시뮬레이터 쪽 내용이므로 형식 참조 근거로만 쓰고 f25 에서 연계 대상으로 구분함
    - f2·f3: OpenSCENARIO 는 자율주행 도로 시나리오 표준이므로 ROP 직접 범위가 아니라 참조 설계 사례로만 제안함
    - f7·f12: 컨베이어·작업셀 설비 제어는 설비 쪽 연계 대상이며 시나리오에 장애를 선언하는 방식만 근거로 씀
    - f8·f21: 시나리오는 34. 시뮬레이션·예측용 디지털 트윈이 실행할 가정한 미래의 입력이며 18. 실시간 세계 상태·데이터 일관성의 현재 상태 표현과 섞지 않음
    - f14·f15: 언어 모델 기반 생성은 L. AI·학습 기술(44. 로봇 기반 모델·언어 모델 계획)과 9. 채팅으로 시나리오 구성에도 연결하도록 제안함
- 한계: web_fetch_available: true · fetch_mode full. 검색 16회/30, 신규 출처 15건/15(ref-1135~ref-046, 예약 구간 안)로 출처 상한에 도달해 물류창고 실제 현장 시나리오와 국내 자료, oq-135 조사를 더 하지 못했다. 재사용 출처 없음: NIST ARIAC 는 공통 규칙상 ref-008 이지만 입력 참고문헌 요약에 ref-008 의 등록 URL·제목이 없어 이번에 연 개별 문서 페이지(challenges·scenario)를 새 id(ref-528·ref-1140)로 적었다. 같은 URL 이면 퍼블리셔가 합치고, 다르면 ref-008 과의 관계를 검증에서 확인해 주기 바란다. 원문 열람: 15건 모두 열었다(webfetch 10건, github_raw 5건). 논문은 모두 초록 페이지 기준이다. VDMA LIF 지침 PDF 는 본문 추출에 실패해 공식 저장소 README 로 대신했다. 교차 확인 0건: 각 형식·사례가 한 출처에만 기술되어 있어 finding 신뢰도는 medium 이하로 두었다. Groot2 기능(f16)은 vendor_claim: true·태그 추정·'벤더 주장: ' 첫머리로 냈다. 분류 원문 핵심 질문(현장·로봇·사람·작업을 담은 시나리오를 어떻게 표현하고 다시 쓸 것인가)에는 f22 로 답했고 결론은 '공개 형식은 분야별로 나뉘고 공통 표준은 없으며, 재사용은 매개변수화·표본 추출·예제 라이브러리·언어 모델 생성으로 이루어진다'는 추정이다. 현장 유형 사례는 상업 시설(f4·f5)·병원(f6)·실외(f7)·가정(f10)·제조 공장(f11·f12)이며 물류창고는 격자 지도 벤치마크(f18)와 레이아웃 교환 형식(f20)만 있고 현장 사례는 찾지 못했다. 국내 자료는 한국어 검색 2회에서 이 영역에 맞는 것을 찾지 못했다(찾은 한국지능시스템학회 시뮬레이터 리뷰는 시나리오 정의를 다루지 않아 제외). 기존 열린 질문 oq-131·oq-135 는 해결 근거가 없어 해결 제안하지 않았다. 용어집에 이미 있는 행동 트리·BPMN·HTN·레이아웃 교환 형식·가상 시운전·시나리오 재구성·미션 명세 패턴은 후보로 내지 않았다. 입력 누락 없음. 정정 요청 없음. 우선 지정 질문 없음.
```

### data/source_texts/ref-079.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

````text
# Traffic Editor

This section describes the traffic-editor GUI and simulation tools.

## Introduction and Objectives

Traffic management of heterogeneous robot fleets is non-trivial. One of the
challenges with coordinated management arises from varying semantics in
information models used across fleets. Representations of waypoints, lanes,
charging/docking stations, restricted zones, infrastructure  systems such as
doors & lifts, among others, are subject to vendor's discretion. However,
standardized conventions that convey the capabilities and intentions of fleets
in a shared facility are quintessential for planning. Multi-agent participants
in other modes of transportation such as roadways collectively adhere to a set
of rules and conventions which minimize chaos. More importantly, they allow for
a new participant to readily integrate into the system by following the
prescribed rules. Existing agents can accommodate the new participant as its
behavior is apparent.

Traffic conventions for multi-robot systems do not exist.
The objective of the `traffic_editor` is to fill this gap by expressing the
intentions of various fleets in a standardized, vendor neutral manner through a
graphical interface. Collated traffic information from different fleets can then
be exported for planning and control. A secondary objective and benefit of the
`traffic_editor` is to facilitate generation of 3D simulation worlds which
accurately reflect physical environments.

## Overview

The `traffic_editor` [repository](https://github.com/open-rmf/rmf_traffic_editor) is home to the `traffic_editor` GUI and tools to auto-generate simulation worlds from GUI output.
The GUI is an easy-to-use interface which can create and annotate 2D floor plans with robot traffic along with building infrastructure information.
Often times, there are existing floor plans of the environment, such as architectural drawings, which simplify the task and provide a "reference" coordinate system for vendor-specific maps.
For such cases, `traffic-editor` can import these types of "backgroud images" to serve as a canvas upon which to draw the intended robot traffic maps, and to make it easy to trace the important wall segments required for simulation.

The `traffic_editor` GUI projects are stored as `yaml` files with `.building.yaml` file extensions.
Although the typical workflow uses the GUI and does not require hand-editing the `yaml` files directly, we have used a `yaml` file format to make it easy to parse using custom scripting if needed.
Each `.building.yaml` file includes several attributes for each level in the site as annotated by the user.
An empty `.building.yaml` file appears below.
The GUI tries to make it easy to add and update content to these file.

```yaml
levels:
  L1:
    doors:
      - []
    drawing:
      filename:
    fiducials:
    elevation: 0
    flattened_x_offset: 0
    flattened_y_offset: 0
    floors:
      - parameters: {}
        vertices: []
    lanes:
      - []
    layers:
      {}
    measurements:
      - []
    models:
      -{}
    vertices:
      {}
    walls:
      {}
lifts:
  {}
name: building

```

## GUI Layout

The layout of the `traffic_editor` includes a `Toolbar`, a `Working Area` and a `Sidebar` as seen in the figure below:

![Traffic Editor GUI](images/traffic_editor/layout.png)

The toolbar contains a variety of tools to support actions such as setting the scale of the drawing, aligning levels for multi-level scenarios, adding virtual models to simulated environments, adding robot traffic lanes, simulated flooring, and so on.

As usual in a modern GUI, the top Toolbar contains a variety of tools to interact with items in the main Working Area.
This document will introduce and explain the tools as an example project is created.
However, the first three tools in the toolbar are commonly found in 2D drawing tools, and should behave as expected:

|                    Icon                           |  Name  | Shortkey |               Function               |
|:-------------------------------------------------:|:------:|:--------:|:------------------------------------:|
| ![Select icon](images/traffic_editor/icons/select.svg) | Select |   `Esc`  | Select an entity in the `Working Area` |
|  ![Move icon](images/traffic_editor/icons/move.svg)    |  Move  |    `m`   |  Move an entity in the `Working Area`  |
| ![Rotate icon](images/traffic_editor/icons/rotate.svg) | Rotate |    `r`   | Rotate an entity in the `Working Area` |

The `Working Area` is where the levels, along with their annotations, are rendered.
The user is able to zoom via the mouse scroll wheel, and pan the view by pressing the scroll wheel and moving the mouse cursor.

The `Sidebar` on the right side of the window contains multiple tabs with various functionalities:
* **levels:** to add a new level to the building. This can be done from scratch or by importing a floor plan image file.
* **layers:** to overlap other images such as lidar maps over the level
* **lifts:** to configure and add lifts to the building
* **traffic:** to select which "navigation graph" is currently being edited, and toggle which graph(s) are being rendered.

## Annotation Guide
This section walks through the process of annotating facilities while highlighting the capabilities of the `traffic_editor` GUI.

To create a new traffic editor `Building` file, launch the traffic editor from a terminal window (first sourcing the workspace if `traffic-editor` is built from source).
Then, click `Building -> New...` and choose a location and filename for your `.building.yaml` file.

### Adding a level
A new level in the building can be added by clicking the `Add` button in the `levels` tab of the `Sidebar`.
The operation will open a dialog box where the `name`, `elevation` (in meters) and path to a 2D `drawing` file (`.png`) can be specified.
In most use cases, the floor plan for the level is used as the drawing.
If unspecified, the user may explicitly enter dimensions of the level in the fields provided.

![Add a level dialog](images/traffic_editor/add_level.png)

In the figure above, a new level `L1` at `0m` elevation and a floor plan have been added as reflected in the `levels` tab.
A default scale `1px = 5cm` is applied.
The actual scale can be set by adding a measurement.
Any offsets applied to align levels will be reflected in the `X` and `Y` columns.
Saving the project will update the `tutorial.building.yaml` files as seen below:
```yaml
levels:
  L1:
    drawing:
      filename: office.png
    elevation: 0
    flattened_x_offset: 0
    flattened_y_offset: 0
    layers:
      {}
lifts:
  {}
name: building
```
### Adding a vertex
|                    Icon                    | Shortkey |
|:------------------------------------------:| :-------:|
| ![Vertex icon](images/traffic_editor/icons/vertex.svg)| `v` |

A vertex is a fundamental component of multiple annotations.
Walls, measurements, doors, floor polygons and traffic lanes are created from two or more vertices.
To create a vertex, click on the vertex icon in the `Toolbar` and then click anywhere on the canvas.
The default attributes of a vertex are its coordinates along with an empty name field.
Additional attributes may be added by first selecting the vertex (which will turn it red), and then clicking the `Add` button in the figure.
Short descriptions of these are presented below:
* **is_holding_point:** if true and if the waypoint is part of a traffic lane,
  the `rmf_fleet_adapter` will treat this as a _holding point_ during path
  planning, i.e., the robot is allowed to wait at this waypoint for an indefinite
  period of time.
* **is_parking_spot:** robot's parking spot. [Definition](https://github.com/open-rmf/rmf_traffic/blob/40023b0f9b5d79a4781f6105f0368d74c1dfc443/rmf_traffic/include/rmf_traffic/agv/Graph.hpp#L73-L76)
* **is_passthrough_point:** waypoint which the robot shouldnt stop. [Definition](https://github.com/open-rmf/rmf_traffic/blob/40023b0f9b5d79a4781f6105f0368d74c1dfc443/rmf_traffic/include/rmf_traffic/agv/Graph.hpp#L63-L68)
* **is_charger:** if true and if the waypoint is part of a traffic lane, the
  `rmf_fleet_adapter` will treat this as a charging station.
* **is_cleaning_zone** indicate if current waypoint is a cleaning zone, specifically for `Clean` Task.
* **dock_name:** if specified and if the waypoint is part of a traffic lane, the
  `rmf_fleet_adapter` will issue an `rmf_fleet_msgs::ModeRequest` message with
  `MODE_DOCKING` and `task_id` equal to the specified name to the robot as it approaches this waypoint. This is used when the robot is executing their custom docking sequence (or custom travel path).
* **spawn_robot_type:** the name of the robot model to spawn at this waypoint in
  simulation. The value must match the model's folder name in the assets
  repository. More details on the robot model and plugin required for simulation
  can be found in [Simulation](simulation.md)
* **spawn_robot_name:** a unique identifier for the robot spawned at this
  waypoint. The `rmf_fleet_msgs::RobotState` message published by this robot
  will have `name` field equal to this value.
* **pickup_dispenser** name of the dispenser workcell for `Delivery` Task, typically is the name of the model. See the [Workcell section] (https://osrf.github.io/ros2multirobotbook/simulation.html#workcells) of the Simulation Chapter for more details.
* **dropoff_ingestor** name of the ingestor workcell for `Delivery` Task, typically is the name of the model. See the [Workcell section] (https://osrf.github.io/ros2multirobotbook/simulation.html#workcells) of the Simulation Chapter for more details.
* **human_goal_set_name** The `goal_sets.set_area` name, used by crowd simulation. For more info about `crowd_sim`, please see the [Crowdsim section] (https://osrf.github.io/ros2multirobotbook/simulation.html#crowdsim) of the Simulation Chapter for more details.

![Vertex attributes](images/traffic_editor/add_vertex.png)

Each vertex is stored in the `tutorial.building.yaml` file as a list of x-coordinate, y-coordinate, elevation, vertex_name and a set of additional parameters.

```yaml
  vertices:
    - [1364.76, 1336.717, 0, magni1_charger, {is_charger: [4, true], is_parking_spot: [4, true], spawn_robot_name: [1, magni1], spawn_robot_type: [1, Magni]}]
```
### Adding a measurement
|                    Icon                    |
|:------------------------------------------:|
| ![Measurement icon](images/traffic_editor/icons/measurement.svg)|

Adding a measurement sets the scale of the imported 2D drawing, which is essential for planning and simulation accuracy.
Scalebars or reference dimensions in the floor plan aid with the process. Often, you can draw the measurement line directly on top of a reference scale bar in a drawing.
With the editor in _Building_ mode, select the _Add Measurement_ tool and click on two points with known dimensions.
A pink line is rendered on the map with two vertices at its ends at the selected points.

Note:
A measurement line may be drawn by clicking on existing vertices.
In this scenario, no additional vertices are created at its ends.

Selecting the line populates various parameters in the Properties window of the `Sidebar`.
Setting the `distance` parameter to the physical distance between the points (in meters) will then update the `Scale` for the level.
Currently, you must save the project and restart `traffic-editor` to see the changes reflected (todo: fix this...).

![Measurement properties](images/traffic_editor/add_measurement.png)

The above process adds two `vertices` and a `measurement` field to the `tutorial.building.yaml` file as seen below.
For the measurement field, the first two elements represent the indices of vertices representing the ends of
the line.
The `distance` value is stored in a sub-list of parameters.

```yaml
levels:
  L1:
    drawing:
      filename: office.png
    elevation: 0
    flattened_x_offset: 0
    flattened_y_offset: 0
    layers:
      {}
    measurements:
      - [1, 0, {distance: [3, 8.409]}]
    vertices:
      - [2951.728, 368.353, 0, ""]
      - [2808.142, 1348.9, 0, ""]

lifts:
  {}
name: building
```

### Adding a wall
|                    Icon                    | Shortkey |
|:------------------------------------------:| :-------:|
| ![Wall icon](images/traffic_editor/icons/wall.svg)| `w` |

To annotate walls in the map, select the _Add Wall_ icon from the `Toolbar` and click on consecutive vertices that represent the corners of the wall.
The process of adding wall segments is continuous, and can be exited by pressing the `Esc` key.
Blue lines between vertices are rendered on the map which represent the drawn walls.
If the corner vertices are not present, they will automatically be created when using this tool.
Meshes of the annotated walls are automatically generated during 3D world generation using `building_map_generator`.
By default, the walls are of thickness of 10cm and height 2.5m.
The `wall_height` and `wall_thickness` attributes may be
modified [in the source code](https://github.com/open-rmf/rmf_traffic_editor/blob/main/rmf_building_map_tools/building_map/wall.py#L16-L17).

Wall texture options are available [here](https://github.com/open-rmf/rmf_traffic_editor/tree/main/rmf_building_map_tools/building_map_generator/textures) in the source code.

![Annotating walls](images/traffic_editor/add_wall.png)

Walls are stored in the `tutorial.building.yaml` file as a list with indices of start and end vertices of the wall segment along with an empty parameter set.
```yaml
    walls:
      - [3, 4, {}]
      - [4, 5, {}]
      - [5, 6, {}]
      - [6, 7, {}]
      - [6, 8, {}]
      - [8, 9, {}]
```

### Adding a floor
|                    Icon                    |
|:------------------------------------------:|
| ![Floor icon](images/traffic_editor/icons/floor.svg)|

Flooring is essential for simulations as it provides a ground plane for the robots to travel over.
Floors are annotated using the _Add floor polygon_ tool from the `Main Toolbar` in _Building_ edit mode.
To define a floor, select consecutive vertices to create a polygon that accurately represents the flooring area as seen below.
These vertices will need to be added manually prior to this step.
Once created, save the project and reload.
Selecting the defined floor highlights its texture attributes. Similarly, [default list of available textures](https://github.com/open-rmf/rmf_traffic_editor/tree/main/rmf_building_map_tools/building_map_generator/textures) is available in the source code.

![Highlighting floor's textures](images/traffic_editor/add_floor.png)

Certain scenarios may call for floors with cavities, for example, to represent elevator shafts.
The _Add hole polygon_ tool may be used for this purpose.
Additionally, the shape of a drawn polygon (floor or hole) may be modified using the _Edit polygon_ tool.
Clicking on the tool after selecting an existing polygon enables the user to modify vertices of the polygon.

Each polygon is stored in the `tutorial.building.yaml` file in the format below:
```yaml
    floors:
      - parameters: {texture_name: [1, blue_linoleum], texture_rotation: [3, 0], texture_scale: [3, 1]}
        vertices: [11, 10, 14, 15, 13, 12]
```

### Adding a door
|                    Icon                    |
|:------------------------------------------:|
| ![Door icon](images/traffic_editor/icons/door.svg)|

A door between two vertices can be added in _Building_ edit mode by selecting the _Add door_ tool from the `Main Toolbar`, and clicking on vertices representing the ends of the door.
Selecting an annotated door highlights its properties as seen in the figure below.
Presently, four door `types` are supported: "hinged", "double_hinged", "sliding" and "double_sliding".
The `motion_degrees` parameter specifies the range of motion in the case of hinged doors while the `motion_direction` dictates the direction of swing.
In order for the door to work in simulation, a `name` must be given to the door.

![Door type properties](images/traffic_editor/add_door.png)

Doors are stored in the `tutorial.building.yaml` file as a list with indices of start and end vertices along with the set of parameters that describes the door.

```yaml
 doors:
      - [24, 25, {motion_axis: [1, start], motion_degrees: [3, 90], motion_direction: [2, 1], name: [1, D001], type: [1, double_sliding]}]
```

### Adding a traffic lane
One of the most important tools in the `traffic_editor` GUI is the _Add lane_ tool.
The allowable motions of each fleet operating in the facility is conveyed through its respective Graph which consists of waypoints and connecting lanes.
In this approach, we assume that robots travel along effectively straight-line paths between waypoints.
While this may be perceived as an oversimplification of paths taken by robots that are capable of autonomous navigation, in practice the assumption holds fairly well given that these robots mostly travel along corridors or hallways and seldom in unconstrained open spaces.
For example, even in theoretically unconstrained spaces like building lobbies or shopping-mall atriums, it is likely that the site operator would prefer for the robots to operate in a "traffic lane" on the edge of the space, in order to not impede typical human traffic flows.

The `traffic` tab in the `Sidebar` has a default of nine Graphs for nine different fleets. To annotate lanes for a graph, say Graph 0, select the Graph from the `traffic` tab and click the _Add lane_ tool.
Lanes for this graph can be drawn by clicking vertices to be connected.
If a vertex is not present, it will automatically be added. Properties may be assigned to each vertex as described in the preceding section.
To issue tasks to waypoints that require the robot to terminate at any waypoint, a name must be assigned to the waypoint.

![Graphs' lane colors](images/traffic_editor/add_lane.png)

Each Graph has a unique color for its lanes, and their visibility may be toggled using the checkbox in the `traffic` tab.
A lane that is defined between two waypoints may be configured with these additional properties:
* **bidirectional:** if `true`, the `rmf_fleet_adapter` will plan routes for its
  robot assuming the lanes can be traversed in both directions. Lanes that are
  not bidirectional have arrows indicating their directionality (indigo lanes in
  figure above). A handy shortcut is that when a lane segment is selected, you can
  press the `b` key to toggle between unidirectional and bidirectional motion along that lane.
* **graph_idx**: the Graph number a lane corresponds to
* **orientation**: constrain the lane to make the robot travel in `forward` or `backward` orientation. This can be useful for the final lane segment approaching a docking point or charger, for example.

While lifts that move between levels are now supported in the `traffic_editor`, the **demo_mock_floor_name** and **demo_mock_lift_name** properties were originally engineered to showcase shared lift access in a single floor demonstration environment with a "mock" lift that receives lift commands and transmits lift states but does not actually move between any different floors in a building.
However, as there may be interest in such functionality for testing single-floor hardware setups that seek to emulate multi-floor scenarios, these properties were retained.

* **demo_mock_floor_name**: name of the floor that the robot is on while
  traversing the lane
* **demo_mock_lift_name**: name of the lift that is being entered or exited
  while the robot traverses the lane

To further explain these properties, consider this representation of a
navigation graph where numbers are waypoints and letters are lanes:
```
1 <---a---> 2 <---b---> 3

Waypoint 1 is on floor L1
Waypoint 2 is inside the "lift" named LIFT001
Waypoint 3 is on floor L3
The properties of edge "a" are:
    bidirectional: true
    demo_mock_floor_name: L1
    demo_mock_lift_name: LIFT001
The properties of edge "b" are:
    bidirectional: true
    demo_mock_floor_name: L3
    demo_mock_lift_name: LIFT001
```

If the robot is to travel from waypoint 1 to waypoint 3, the `rmf_fleet_adapter` will request for the "mock lift" to arrive at L1 when the robot approaches waypoint 1.
With confirmation of the "lift" at L1 and its doors in "open" state, the robot will be instructed to move into the "lift" to waypoint 2.
Once the "lift" indicates that it has reached L3, the robot will exit along lane b toward waypoint 3.

Note: when annotating graphs, it is highly recommended to follow an ascending sequence of graph indices without skipping intermediate numbers. Drawn lanes can only be interacted with if their associated Graph is first selected in the `traffic` tab.

The annotated Graphs are eventually exported as `navigation graphs` using the `building_map_generator` which are then used by respective `rmf_fleet_adapters` for path planning.

Lanes are stored in the following format in `tutorial.building.yaml`.
The data structure is a list with the first two elements representing the indices of the two vertices of the lane and a set of parameters with configured properties.
```yaml
    lanes:
      - [32, 33, {bidirectional: [4, true], demo_mock_floor_name: [1, ""], demo_mock_lift_name: [1, ""], graph_idx: [2, 2], orientation: [1, forward]}]
```

### Deriving coordinate-space transforms

Coordinate spaces are confusing!
For historical reasons, the GUI internally creates traffic maps by annotating images, so the "raw" annotations are actually encoded in pixel coordinates of the "base" floorplan image, in pixel coordinates, with +X=right and +Y=down, with the origin in the upper-left of the base floorplan image.
However, during the building map generation step, the vertical axis is flipped to end up in a Cartesian plane, so the vast majority of RMF (that is, everything downstream of traffic-editor and the building map generators) uses a "normal" Cartesian coordinate system. (As an aside -- the next version of traffic-editor is intended to be more flexible in this respect, and will default to a normal Cartesian coordinate system (not an image-based coordinate system), or even global coordinates (lat/lon). Although preliminary work is underway, there is not a hard schedule for this next-gen editor at time of writing, so the rest of this chapter will describe the existing `traffic-editor`.)

Although `traffic-editor` currently uses the upper-left corner of the base floorplan image as the reference frame, maps generated by robots likely will have their origin elsewhere, and will likely be oriented and scaled differently.
It is critical to derive the correct transform between coordinate frames in `traffic_editor` maps and robot maps as
`rmf_fleet_adapters` expect all robots to publish their locations in the RMF coordinate system while the `rmf_fleet_adapters` also issue path requests in the same frame.

To derive such transforms, the `traffic_editor` GUI allows users to overlay robot maps on a floor plan and apply scale, translation and rotation transformations such that the two maps align correctly.
The user can then apply the same transformations to convert between robot map and RMF coordinates when programming interfaces for their robot.

The robot map can be imported by clicking the `Add` button from the `layers` tab in the `Sidebar`.
A dialog box will then prompt the user to upload the robot map image.
The same box contains fields for setting the scale for the image along with applying translations and rotation.
Through visual feedback, the user can determine appropriate values for these fields.
As seen in the image below, importing the robot-generated map into the GUI has it located and oriented
differently than the floor plan.
With the right transformation values, the two maps can be made to overlap.

![Overlap robot-generated map](images/traffic_editor/coordinate_transform.png)

### Adding fiducials
|                    Icon                    |
|:------------------------------------------:|
| ![Fiducial icon](images/traffic_editor/icons/fiducial.svg)|

For maps with multiple levels, fiducials provide a means to scale and align different levels with respect to a reference level.
This is crucial for ensuring dimensional accuracy of annotations across different levels and aligning the
same for simulation.
Fiducials are reference markers placed at locations which are expected to be vertically aligned between two or more levels.
For example, structural columns may run through multiple floors and their locations are often indicated on floor plans.
With two or more pairs of corresponding markers between a level and a reference level, a geometric transformation (translation, rotation and scale) may be derived between the two levels.
This transformation can then be applied to all the vertices and models in the newly defined level.

To begin, add two or more non-collinear fiducials to the reference level with unique `name` attributes using the _Add fiducial_ tool (left image in figure below).
In the newly created level, add the same number of fiducials at locations that are expected to be vertically aligned with matching names as the reference level (right image in figure below).
Saving and reloading the project computes the transformation between the levels which is evident from the Scale
and X-Y offsets for the new level as seen in the `levels` tab.
This level is now ready to be annotated.

![Adding fiducials](images/traffic_editor/add_fiducial.png)

For each level, fiducials are stored in a list of their X & Y coordinates along with their name.
```yaml
    fiducials:
      - [936.809, 1323.141, F1]
      - [1622.999, 1379.32, F2]
      - [2762.637, 346.69, F3]
```

### Adding a lift
Lifts are integral resources that are shared between humans and robot fleets in multi-level facilities.
To add a lift to a building, click the `Add` button in the `lifts` tab in the `Sidebar`.
A dialog box with various configurable properties will load.
It is essential to specify the Name, Reference level and the X&Y coordinates (pixel units) of its cabin center.
A yaw (radians) may further be added to orient the lift as desired.
The width and depth of the cabin (meters) can also be customized.
Lifts can be designed to have multiple cabin doors which may open at more than one level.
To add a cabin door, click the `Add` button in the box below the cabin image.
Each cabin door requires a name along with positional and orientational information.
Here, the X&Y coordinates are relative to the cabin center.

![Configuring lift properties](images/traffic_editor/add_lift.png)

The configured lift is stored in the `tutorial.building.yaml` file as described below:
```yaml
lifts:
  LF001:
    depth: 2
    doors:
      door1:
        door_type: 2
        motion_axis_orientation: 1.57
        width: 1
        x: 1
        y: 0
      door2:
        door_type: 2
        motion_axis_orientation: 1.57
        width: 1
        x: -1
        y: 0
    level_doors:
      L1: [door1]
      L2: [door2]
    reference_floor_name: L1
    width: 2
    x: 827
    y: 357.7
    yaw: 1.09
```

After adding the lift, we would also wish to let our robots to transverse through the lift.
To achieve that, the user needs to create vertices/waypoints which are located within the lift cabin on each floor.
Once done, connect the waypoint within the lift cabin to other vertices via __add_lane__.

### Adding environment assets
Levels may be annotated with thumbnails of models available for simulation using the __Add model__ tool in __Building__ edit mode.
Selecting this tool opens a dialog box with a list of model names and matching thumbnails which can be imported to the map.
Once on the map, their positions and orientations can be adjusted using the _Move_ and _Rotate_ tools. Sample models are provided [here](https://github.com/open-rmf/rmf_traffic_editor/tree/main/rmf_traffic_editor_assets/assets/thumbnails/images/cropped/OpenRobotics)

The [thumbnail_generator documentation](https://github.com/open-rmf/rmf_traffic_editor/tree/main/rmf_traffic_editor#generating-custom-thumbnails) contains instructions on expanding the list of thumbnails for other models.

> Note: If no models are shown on the __add models__ window, Go to "Edit -> Preference", then indicate the thumbnail path. (`e.g. $HOME/rmf_ws/src/rmf/rmf_traffic_editor/rmf_traffic_editor_assets/assets/thumbnails`)

![Model name and thumbnails dialog](images/traffic_editor/add_model.png)

## Conclusion
This chapter covered various capabilities of the `traffic_editor` which are useful for annotating maps of facilities while adhering to a standardized set of semantics.
Examples of other traffic editor projects can be found in the [rmf_demos](https://github.com/open-rmf/rmf_demos) repository.
Running physics based simulations with RMF in the annotated sites is described in the [Simulation](simulation.md) chapter.
````

### data/source_texts/ref-528.txt (원문 텍스트, fetched_via=inbox 또는 github_raw)

```text
.. _CHALLENGES:

==========
Challenges
==========

The agility challenges test teams' ability to adapt to unexpected situations and system failures during competition runs. Successfully handling these challenges is crucial for maintaining high performance and achieving competitive scores.

The competition incorporates challenges to test the robustness of team systems. Teams should be able to recognize when a challenge is occurring and properly handle the situation. There are four possible challenges that can occur during a run:

* **Conveyor Malfunction** - Inspection conveyor stops operating
* **Voltage Tester Malfunction** - One or both voltage testers stop providing data
* **Vacuum Tool Malfunction** - Vacuum gripper fails to grasp objects
* **High Priority Order** - Urgent kit request with time constraints

Conveyor Malfunction
====================

When the conveyor malfunction challenge occurs, the inspection conveyor will pause its motion. In addition, the cell feed will pause, so no new cells can be added during the challenge.

.. list-table:: Conveyor Malfunction Parameters
   :header-rows: 1
   :widths: 20 20 60
   :class: centered-table

   * - Parameter
     - Type
     - Description
   * - ``START_TIME``
     - int
     - Time in seconds when the malfunction begins (minimum: 0)
   * - ``DURATION``
     - int
     - Duration in seconds the malfunction lasts (minimum: 1)

Teams are expected to handle this challenge by:

1. **Detecting the malfunction** by monitoring the conveyor status topic (:ref:`reference <inspection_challenge_anchor>`)
2. **Pausing the inspection system** to avoid conflicts
3. **Waiting for recovery** by monitoring the status topic until it reports operational status
4. **Resuming operations** once the conveyor and cell feed return to normal

Voltage Tester Malfunction
==========================

When the voltage tester malfunction occurs, one or both voltage testers will stop publishing data.

.. list-table:: Voltage Tester Malfunction Parameters
   :header-rows: 1
   :widths: 20 20 60
   :class: centered-table

   * - Parameter
     - Type
     - Description
   * - ``START_TIME``
     - int
     - Time in seconds when the malfunction begins
   * - ``DURATION``
     - int
     - Duration in seconds the malfunction lasts
   * - ``TESTER``
     - int
     - Which voltage tester is affected (1 or 2)

Teams are expected to handle this challenge by:

1. **Detecting the malfunction** by monitoring voltage tester topics for data availability (:ref:`reference <inspection_challenge_anchor>`)
2. **Adapting operations** to avoid using the affected voltage tester(s)
3. **Monitoring for recovery** by watching the status topic until operational status is restored
4. **Continuing progress** using any operational voltage testers to maintain productivity
5. **Resuming full operations** once all voltage testers return to operational status

Vacuum Tool Malfunction
=======================

When the vacuum tool malfunction occurs, a specified vacuum gripper will fail during grasp attempts.

.. list-table:: Vacuum Tool Malfunction Parameters
   :header-rows: 1
   :widths: 20 20 60
   :class: centered-table

   * - Parameter
     - Type
     - Description
   * - ``TOOL``
     - int
     - Which vacuum tool is affected (1 or 2)
   * - ``GRASP_OCCURRENCE``
     - int
     - Which grasp attempt will fail (minimum: 1)

.. note::

  **TOOL**: Refers to the :ref:`vacuum gripper tools <vacuumtools_msg>` VG_2 and VG_4 available to assembly robot 2.

.. note::

  **GRASP_OCCURRENCE**: Specifies which attempt at grasping will fail. For example, if set to 3, the first two grasp attempts will succeed normally, but the third attempt will fail and require retry.

Teams are expected to handle this challenge by:

1. **Detecting the failure** by monitoring the response from the grasp service (:ref:`reference <vacuum_tool_challenge_anchor>`)
2. **Repositioning the gripper** by moving it away from the target object
3. **Retrying the grasp** with proper positioning and approach

High Priority Order
===================

When a high priority order is requested, an internal timer starts tracking completion time. Teams should minimize the time taken to submit this urgent kit request.

.. list-table:: High Priority Order Parameters
   :header-rows: 1
   :widths: 20 20 60
   :class: centered-table

   * - Parameter
     - Type
     - Description
   * - ``START_TIME``
     - int
     - Time in seconds when the high priority order is announced
   * - ``ID``
     - string
     - Unique identifier for the high priority order

Teams are expected to handle this challenge by:

1. **Detecting the request** by monitoring the high priority order topic (:ref:`reference <high-priority-anchor>`)
2. **Switching cell feed** to begin feeding NiMH cells
3. **Building the kit** using four NiMH cells with proper voltage specifications
4. **Delivering the kit** by moving the AGV to the shipping location
5. **Submitting the order** using the high priority submission service with the correct order ID (:ref:`reference <high-priority-anchor>`)
6. **Restoring normal operations** by switching cell feed back to Li-ion batteries
7. **Resuming standard tasks** to continue regular production

Configuration Example
======================

For complete challenge configuration examples showing all challenge types with valid parameters, see the :ref:`Challenges Configuration Reference <challenges_config_example>`.
```
