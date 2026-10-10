---
area: 20
title: "20. 로봇·제조사 관제 연동"
researched: 2026-10-10
researcher: OpenAI Codex
---

# 20. 로봇·제조사 관제 연동 — 보완 조사

## 요약

- 제조사 관제를 거치는지와 오픈 로보틱스 미들웨어 프레임워크(Open Robotics Middleware Framework, Open-RMF)의 전체 제어(Full Control) 여부는 별도로 판단해야 한다. [의견][^n5][^n20]
- VDA 5050 3.0.0의 보도자료 본문 날짜는 2026-04-20이다. [사실][^n3] 발행일은 공식 자료에도 3월 17일과 19일이 달리 표시되어 하나로 확정하지 않았다. [의견][^n2][^n4]
- 기존 논문의 120 ms는 본문에서 상태 갱신 간격으로 보고된다. [사실][^n7] 자동차 공장 적용을 목표로 한 실험실 연구와 공장 운영 실적을 구분해야 한다. [의견][^n7]
- Open-RMF의 GoToZone 주 PR은 확인일에도 미병합 상태다. [사실][^n11] EasyTrafficLight 수정은 `rmf_fleet_adapter` 2.14.0 변경 이력에서 확인했다. [사실][^n10]
- Automate 2026과 국내 호텔 사례를 추가하되 벤더 주장으로 표시한다. [의견][^n16][^n17]

## 보완 항목

### 7. 관련 표준·프레임워크·오픈소스 — 수정

- 대상 문장: "공식 저장소 main 명세의 판 표기는 3.0.0이고 VDA가 3.0 판 발행을 보도자료로 알렸으나, 정확한 발행일은 미확인이다(oq-005)."
- 새 내용: VDA 5050 3.0.0의 공식 저장소 릴리스 설명은 VDA 발행일을 2026-03-19로 적는다. [사실][^n2] VDA 발행물 카탈로그는 2026-03-17을 표시한다. [사실][^n4] VDA 보도자료 본문 날짜는 2026-04-20이다. [사실][^n3] 서지에는 문서 판의 월인 2026-03을 적고, 서로 다른 일자 표시는 별도 주석으로 남기는 것이 좋다. [의견][^n1][^n2][^n3][^n4]
- 근거 메모: n2 릴리스 첫 문단의 "released by the VDA on March 19th, 2026"; n4 제목 아래 "March 17, 2026"; n3 제목 아래 "Berlin, April 20, 2026". n2의 GitHub API `published_at`은 `2026-03-18T19:23:27Z`이다. 저장소 게시 시각, 카탈로그 표시일, 문서 발행 설명, 보도자료 날짜를 분리했다. URL의 `260421`을 본문 날짜로 대체하지 않았다. 3월 17일과 19일의 차이가 생긴 이유는 확인 못 함. 네 자료는 모두 VDA 계열이므로 독립 교차 확인이 아니다. Idealworks의 2월 17일 채택 주장은 부록 C의 후보 X1로 남겼다.

### 5. 적용 사례 (현장 유형 명시) — 수정

- 대상 문장: "개별 로봇 제어(저수준 제어·전체 제어·VDA 5050 직접 연결)는 ROP가 경로·교통을 통합 조정할 수 있는 대신 제조사가 경로 지정·중단·교체 API나 VDA 5050 지원을 제공해야 하고, 제조사 관제 위임이나 신호등·읽기 전용 수준 연동은 연동 부담이 작은 대신 공용 통로·승강기·문에서의 조정이 일시정지·재개나 상태 관측에 그칠 것으로 보인다."
- 새 내용: Open-RMF는 제조사 관제 API를 통해서도 전체 제어를 구현하는 구조를 지원한다. [사실][^n5][^n20] 연동 위치와 제어 권한을 별도 항목으로 기록하는 것이 좋다. [의견][^n5] 제어 권한에는 경로 지정·교체, 정지, 진행 상태 반환을 각각 적는 것이 좋다. [의견][^n5][^n6]
- 근거 메모: n5 「Mobile Robot Fleet Integration」은 "fleet manager allows us to specify explicit paths"라고 설명하고, 「Fleet Adapter Template」은 중간 fleet manager를 선택 사항으로 둔다. n20 「Open-RMF」는 "full control fleet adapter for RMF"를 통해 InOrbit 제어 플릿을 연결한다고 명시한다. Open-RMF와 InOrbit은 다른 프로젝트·기관이다. 두 문서가 확인하는 범위는 **관제 API 경유 전체 제어라는 연결 구조**다. 같은 RMF 연동을 설명하므로 엄격한 독립 재검증 집계에는 넣지 않았다. 특정 제품의 실제 성능이나 모든 API의 호환성을 검증한 것은 아니다. 국내 물류센터에서 두 방식의 비용·처리량을 같은 조건으로 비교한 자료는 확인 못 함.

### 6. 대표 접근법과 기술 — 추가

- 새 내용: `EasyTrafficLight::moving_from()`의 API 계약은 통신 지연과 감속 능력을 고려해 다음 체크포인트(checkpoint)에서 정지할 시간을 확보한 때만 호출하도록 권고한다. [사실][^n6] 같은 API의 `Blocker` 설명은 제어 권한 부족으로 풀 수 없는 교착에서 사람 개입이 필요할 수 있다고 적는다. [사실][^n6] 정지 명령의 존재만 확인하지 말고 정지 가능 거리와 정지 확인 응답도 연동 계약에 적는 것이 좋다. [의견][^n6]
- 근거 메모: n6 태그 2.14.0, `moving_from()` 앞 주석의 "accounting for the network latency" 및 `Blocker` 앞 "Human intervention may be required". 구현 API의 전제와 한계이며 실험 대수·처리량 수치가 아니다. 단일 프로젝트 근거다. 제한 제어가 모든 교착을 해결한다는 보장으로 확대하지 않았다.

### 6. 대표 접근법과 기술 — 추가

- 새 내용: VDA 5050 3.0.0은 로봇과 브로커(broker)의 연결이 끊겨도 로봇이 마지막으로 실행 허용된 노드까지 받은 주문을 수행한다고 명시한다. [사실][^n1] 같은 판은 주문 동작·즉시 동작·구역 동작(zone action)의 상태를 각각 `actionStates`·`instantActionStates`·`zoneActionStates`로 나눈다. [사실][^n1] 어댑터는 연결 단절과 동작 실패를 별도 상태로 보존하는 것이 좋다. [의견][^n1]
- 근거 메모: n1 §4.1의 "last released node"; §6.6.9와 §7.7의 세 배열 이름. 명세 3.0.0에 한정한다. 구역 동작의 실행 예정 상태 보고는 선택 사항이므로 모든 예정 동작을 반드시 보고한다는 뜻으로 옮기지 않았다. 단일 규격 근거다. 기존 위키의 연결 상태 열거에 추가하는 **단절 시 실행 의미와 상태 분리**이며, 복구 알고리즘 제안은 10절 연결로 한정한다.

### 8. 대표 연구와 자료 — 수정

- 대상 문장: "작업 상태 갱신 평균 지연 120 ms를 보고했으나 단일 출처이고 측정 조건은 미확인이다."
- 새 내용: Lopes 등의 논문은 본문 6.2절에서 로봇 상태의 평균 갱신 간격을 약 120 ms로 보고한다. [사실][^n7] 이 논문의 실물 시험 장소는 약 500 m²의 대학 실험실이다. [사실][^n7] 논문은 최대 20대의 동시 감시를 보고한다. [사실][^n7] 이 결과를 자동차 공장의 장기 운영 지연이나 20대 동시 주행 제어 성능으로 인용하지 않는 것이 좋다. [의견][^n7]
- 근거 메모: n7 p.21 §6.2 "average update interval", p.12 §5.3 "laboratory", p.21 §6.2 "up to 20 robots". p.1 초록의 "latency"와 p.21의 지표 명칭이 다르다. p.21 그림으로도 재확인했다. p.6 §4에는 개발 대상 세 로봇(ASTI, AiTEN, SEER)이 소개된다. 세 기종 설명과 최대 20대 감시 결과를 구별했다. 20대의 기종별 구성·시험 기간·표본 수·측정 타임스탬프 정의는 확인 못 함. p.21 §7은 감시·감독 중심이라고 한정한다. 단일 연구팀의 결과이며 독립 재현은 확인 못 함.

### 8. 대표 연구와 자료 — 추가

- 새 내용: Franke 등의 연구는 2023년 봄 여섯 회사가 참여한 워크숍으로 표준 인터페이스 요구를 수집했다. [사실][^n8] 이 연구는 연동 요구 분석 자료로 분류하는 것이 좋다. [의견][^n8] 직접 제어와 관제 위임의 처리량 비교 근거로 쓰는 것은 적절하지 않다. [의견][^n8]
- 근거 메모: n8 p.4 §3.1 "six participating companies". 참여 구성이 소프트웨어 기업 관계자 2, 하드웨어 제조사 3, 창고 사용자 1로 명시된다. 논문 본문과 학술지 서지 페이지를 열어 저자·DOI·발행일 2023-10-11을 확인했다. 실물 플릿의 정량 비교 실험이 아닌 워크숍 연구다. 기존의 주변 설비 범위 문장은 반복 추가하지 않는다. 다른 연구팀인 n7과도 같은 성능 주장을 검증한 관계는 아니다.

### 8. 대표 연구와 자료 — 추가

- 새 내용: ARM Institute의 IO-AMRs 과제 소개는 Siemens Technology를 주관 기관으로 적는다. [사실][^n9] 과제 소개는 다중 지도 관리자·연결 계층·전역 플릿 관리자를 개발할 계획으로 설명한다. [사실][^n9] 이 소개를 이미 달성한 운영 성과의 근거로 쓰지 않는 것이 좋다. [의견][^n9]
- 근거 메모: n9 「Participants」의 "Lead: Siemens Technology"와 「Technical Approach」의 "will leverage". 기존 위키의 과제 목표 설명을 실제 원문으로 확인하고 주관 기관·계획 단계라는 범위를 보완했다. 과제 완료일, 공개 소스 릴리스, 실물 대수와 성능 결과는 이 페이지에서 확인 못 함. 과제 발주·소개 기관의 1차 자료지만 독립 성능 평가 자료는 아니다.

### 7. 관련 표준·프레임워크·오픈소스 — 추가

- 새 내용: Open-RMF의 GoToZone 주 PR #516은 구역 이름을 받아 내부 경유점을 예약하는 기능을 제안한다. [사실][^n11] 이 PR은 2026-10-10 확인 시 미병합 상태다. [사실][^n11] 어댑터의 릴리스 기능 목록과 개발 중인 기능 목록을 구분하는 것이 좋다. [의견][^n11]
- 근거 메모: n11 PR 설명의 "zone booking system"과 상태 "Open"; GitHub API의 `merged_at: null`을 확인했다. 구역 감독 노드와 플릿 어댑터의 요청·예약 메시지 연동이 제안 범위다. 2026-05-04 SIG 공지와 CHART 기여 계획(부록 C의 X5·X6)은 같은 개발 작업이므로 독립 검증으로 세지 않았다. CHART의 하드웨어 시험 주장을 업스트림 릴리스 검증으로 바꾸지 않았다. PR은 공개 제안 자체의 근거이며 코드·CHANGELOG 근거는 아래 고정 태그를 사용한다.

### 7. 관련 표준·프레임워크·오픈소스 — 추가

- 새 내용: `rmf_fleet_adapter` 2.14.0의 변경 이력 날짜는 2026-09-26이다. [사실][^n10] 이 판의 변경 이력에는 EasyTrafficLight의 플릿 상태 발행 수정이 들어 있다. [사실][^n10] 같은 변경 이력에는 EasyTrafficLight의 누적 지연 계산 수정이 들어 있다. [사실][^n10] 신호등 연동을 평가할 때 사용 패키지 판을 함께 기록하는 것이 좋다. [의견][^n10]
- 근거 메모: n10 태그 2.14.0의 첫 항목 및 "Fix EasyTrafficLight publish fleet state", "Fix cumulative delay calculation in EasyTrafficLight". 각각 #525, #524다. Open-RMF 전체 제품의 단일 버전 번호로 표현하지 않았다. 수정 이력은 실제 교통 성능 향상률을 증명하지 않는다. n6과 같은 프로젝트이므로 두 문서를 독립 검증으로 세지 않았다.

### 6. 대표 접근법과 기술 — 추가

- 새 내용: `ros_amr_interop` 1.1.1의 송신 예제는 로봇 운영체제(Robot Operating System, ROS) 토픽에서 MassRobotics의 `operationalState`와 `errorCodes`를 채우는 설정을 제공한다. [사실][^n13] MassRobotics 태그 1.0의 상태 보고 스키마는 `operationalState`를 필수 필드로 둔다. [사실][^n14] 이 예제를 세 체계 전체의 공통 상태 표준으로 일반화하지 않는 것이 좋다. [의견][^n13][^n14]
- 근거 메모: n13 `massrobotics_amr_sender_py/params/sample_config.yaml`의 `operationalState.valueFrom.rosTopic`, `errorCodes.valueFrom.rosTopic`; n14 `statusReport.required`. 예제의 오류 문자열 분리 주석과 각 토픽 입력을 직접 확인했다. ROS→MassRobotics의 구체적 매핑 사례다. Open-RMF↔VDA 5050↔MassRobotics의 공통 규범 매핑은 확인 못 함. 위키에 이미 있는 YAML 설정 가능 여부에서 한 단계 들어가 실제 필드를 보강했다. 1.1.1·1.0은 각각 고정된 과거 태그이며 최신 지원 범위를 뜻하지 않는다. 두 프로젝트는 별개지만 서로 다른 주장이라 교차 확인으로 세지 않는다.

### 7. 관련 표준·프레임워크·오픈소스 — 추가

- 새 내용: `free_fleet` 태그 1.3.0의 README는 CycloneDDS 기반 메시지 생성을 설명한다. [사실][^n15] 해당 태그의 문서는 ROS 1·ROS 2 쪽 CycloneDDS 버전을 맞추도록 권고한다. [사실][^n15] 위키의 Zenoh 기반 설명과 이 과거 태그의 설치 절차를 섞지 않는 것이 좋다. [의견][^n15]
- 근거 메모: n15 「Message Generation」의 "CycloneDDS", 「Prerequisites」의 "should be the same". 태그 1.3.0의 커밋 시각은 2024-12-31이나 릴리스 발행일과 같은 것으로 간주하지 않았다. 최신 문서의 Zenoh·Nav2 설명은 부록 C X11에서 재확인했다. 해당 새 구조에 대응하는 릴리스 태그는 확인 못 함. 태그 목록을 확인했으나 태그 이름의 크기만으로 최신 배포판을 결정하지 않았다. 설치·통신 구조에 한정하며 실제 로봇 성능은 검증하지 않았다.

### 7. 관련 표준·프레임워크·오픈소스 — 추가

- 새 내용: `vda-5050-lib.js` v1.7.0의 변경 이력은 2026-04-29에 VDA 5050 3.0 지원을 추가했다고 적는다. [사실][^n12] 추가 항목에는 `ZoneSet`·`Responses` 토픽과 3.0용 검증기가 포함된다. [사실][^n12] 어댑터 선정 시 라이브러리 판과 지원 규격 판을 함께 고정하는 것이 좋다. [의견][^n12]
- 근거 메모: n12 v1.7.0 「Features」의 "VDA5050 V3.0 support", `Topic.ZoneSet`, `Topic.Responses`. 규격 원문과 별개 프로젝트의 구현 이력이다. 라이브러리의 선언된 지원 범위를 확인한 것이며, 모든 제조사 로봇과의 적합성·실물 호환성 검증으로 세지 않았다. 위키의 3.0 소개와 중복되지 않는 **구현 릴리스** 정보다.

### 5. 적용 사례 (현장 유형 명시) — 추가

- 새 내용: **현장 유형: 전시 시연.** InOrbit은 Automate 2026에서 자사 시스템으로 여러 제조사의 로봇을 함께 조정한 시연을 공개했다. [추정][^n16] 회사가 적은 참여 기업 10개에는 로봇 업체 외에 위치 추적 업체와 InOrbit 자체가 포함된다. [추정][^n16] 이를 로봇 10대나 10개 AMR 제조사의 상용 공장 운영 사례로 세지 않는 것이 좋다. [의견][^n16]
- 근거 메모: n16 「What you'll see in the demo」의 로봇 업체 열거와 "including InOrbit.AI". 원문은 로봇 공급사 7개, 위치 추적 업체 2개, InOrbit 1개로 설명한다. 이 숫자는 로봇 대수가 아니다. IndustrialSage의 8개 업체 표현은 부록 C X12에서 대조했다. 자료별 집계 기준과 참가 시점의 차이를 완전히 확인하지 못해 단일한 실물 대수는 제시하지 않는다. 원문은 행사 후 영상이 포함된 벤더 페이지이며, 이번 조사에서는 영상 전체를 독립 계수하지 않았다. 성능·가동률은 확인 못 함.

### 5. 적용 사례 (현장 유형 명시) — 추가

- 새 내용: **현장 유형: 국내 호텔.** 카카오모빌리티는 로보티즈와 함께 신라스테이 서초·반얀트리 클럽 앤 스파 서울에 로봇 배송 서비스를 적용했다고 발표했다. [추정][^n17] 이 발표를 국내 플랫폼–로봇 제조사 연동 사례로 분류하는 것이 좋다. [의견][^n17] 같은 장소에서 여러 제조사 플릿을 함께 운영한 증거로 쓰는 것은 보류하는 것이 좋다. [의견][^n17]
- 근거 메모: n17 2026-03-16 보도자료 「로봇 가동률…」 문단의 "신라스테이 서초, 반얀트리 클럽 앤 스파 서울". 구체적 API, 제어 위임 방식, 로봇 대수와 시험 기간은 확인 못 함. 8배 가동률·100% 배송 성공률은 분모와 기간을 확인하지 못해 새 내용에 넣지 않았다. 실제 호텔 서비스에 대한 단일 벤더 발표이며 독립 검증은 아니다. 제조사 다수와 협력한다는 사업 계획을 해당 호텔의 혼합 플릿 증거로 바꾸지 않았다.

### 10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기) — 추가

- 새 내용: **21. 상호운용 표준·적합성** — ISO 21423 공식 카탈로그는 2026-10-10 확인 시 `60.00 — Under publication`을 표시한다. [사실][^n19] **47. AI·학습·적응과 모델 운영** — Nayantra의 Open-RMF REST API를 모델 컨텍스트 프로토콜(Model Context Protocol, MCP) 도구로 노출하는 발표를 검토할 수 있다. [의견][^n18] 해당 SIG 발표 안내의 실행 환경은 NVIDIA Isaac Sim 창고다. [사실][^n18] 이 안내를 실물 다사업자 플릿의 안정성 검증으로 쓰지 않는 것이 좋다. [의견][^n18]
- 근거 메모: n19 「General information / Life cycle」의 "International Standard under publication" 및 단계 60.00. 카탈로그의 2026-10 표시는 발행 완료 확인과 구별했다. ISO 규격 본문은 미열람이며 메시지·의무 사항은 제안하지 않는다. n18 2026-06-25 안내문, 2026-07-02 세션의 "exposes the Open-RMF REST API"와 "NVIDIA Isaac Sim warehouse". 7월 8일 녹화 링크 게시도 확인했지만 영상 전체·실물 대수는 확인 못 함. Nayantra 코드에는 확인 가능한 릴리스 태그가 없어 코드 성능 주장은 채택하지 않았다. 두 출처는 다른 주장에 대응한다.

## 답한 열린 질문

- **oq-005** "출처 충돌: VDA 5050 3.0.0의 정확한 발행일은 언제인가? 검색 요약은 3.0 발행을 2026-03-19, 보도자료를 2026-04-20로 전하지만 보도자료 URL은 2026-04-21 계열이다." → **부분 답변**: 보도자료 본문 날짜는 2026-04-20이다. [사실][^n3] 릴리스 설명의 3월 19일과 공식 카탈로그의 3월 17일은 함께 기록하고 발행일 하나로 합치지 않는 것이 좋다. [의견][^n2][^n4]
- **신규·2026-09-25-20, 분리 페이지에 oq-id 없음** "제조사 관제가 일시정지·재개나 상태 보고만 허용할 때 공용 통로·승강기·문에서 다른 플릿과의 교착을 어떻게 막는가, 제어 수준에 따른 교통 성능 차이를 측정한 연구가 있는가?" → **부분 답변**: EasyTrafficLight API는 정지 시간을 고려한 상태 갱신을 권고한다. [사실][^n6] 같은 API는 해결 불가능한 충돌에서 사람 개입 가능성을 명시한다. [사실][^n6] 제어 수준별 동등 조건 성능 비교는 확인 못 함. 설비 제어 내용은 이번 영역에서 확대하지 않았다.
- **신규·2026-09-25-20, 분리 페이지에 oq-id 없음** "Open-RMF 로봇 상태, VDA 5050 action 상태·오류, MassRobotics 운용 상태를 하나의 공통 상태·오류 어휘로 옮기는 표준 매핑이나 공개 구현이 있는가?" → **부분 답변**: ROS→MassRobotics의 운용 상태·오류 토픽 매핑 예제는 있다. [사실][^n13] 세 체계를 함께 다루는 표준 매핑은 확인 못 함.
- **신규·2026-09-25-20, 분리 페이지에 oq-id 없음** "국내 물류센터에서 로봇을 직접 제어하는 방식과 제조사 관제에 작업을 넘기는 방식 가운데 어느 쪽이 쓰이는지, 선택 기준이나 처리량·연동 비용을 비교한 공개 자료가 있는가?" → **부분 답변**: 연결 위치만으로 전체 제어 여부를 판단하지 않는 기준을 제안한다. [의견][^n5][^n20] 국내 물류센터의 사용 비중·비용·처리량 비교는 확인 못 함. 국내 호텔 사례를 그 답으로 대신하지 않았다.

## 새로 생긴 열린 질문

- U1. VDA 카탈로그의 2026-03-17과 저장소 설명의 2026-03-19는 어떤 업무 단계의 날짜인가? 2월 17일 채택을 확정하는 VDA·VDMA 의결 기록은 있는가?
- U2. 국내 물류센터에서 동일 현장·로봇·작업량으로 직접 제어와 제조사 관제 위임의 연동 공수·비용·처리량을 비교한 원자료는 있는가?
- U3. 제한 제어 플릿의 정지 지연 분포와 교착 발생률을 측정한 공개 시험은 있는가?
- U4. 세 체계의 오류·로봇 상태·동작 상태를 함께 다루는 버전별 공통 매핑과 손실 정보 목록은 있는가?
- U5. Lopes 논문의 20대 구성, 시험 기간, 표본 수, 120 ms 측정 지점은 무엇인가?
- U6. Farooq·Jang 논문의 공개 본문이나 저자 공개본에서 실물 규모와 평가 조건을 확인할 수 있는가?
- U7. IO-AMRs의 완료 보고서·실물 대수·공개 코드와 정량 결과는 어디에 공개됐는가?
- U8. Zenoh 기반 free_fleet에 대응하는 배포 태그와 지원 조합 시험표는 무엇인가?
- U9. Automate 2026의 최종 참여 명단·로봇 대수·재시도 및 실패 기록은 공개됐는가?
- U10. 국내 호텔 사례의 구체적 제어 API, 대수·기간과 독립 운영 기록은 공개됐는가?
- U11. Nayantra의 실물 다제조사 시험과 태그 고정 코드, MCP 호출 실패 처리 시험은 공개됐는가?

위 11개는 이번 조사 범위에서 답을 확인하지 못한 항목이다. 기존 질문과 겹치는 U2~U4도 더 구체적인 후속 근거 요청으로 남겼다. 영역 밖인 EPCIS·GS1·BPMN·ISA-95 매핑 질문 네 개는 이 집계에 넣지 않았다.

## 출처

집계: 총 20개, 원문 열람 20/20, 1차 자료 20개, 독립 교차 확인된 주장 0개.

여기서 원문 열람은 **실제로 인용한 문서 자체**를 뜻한다. n19는 공식 카탈로그만 열람했고 ISO 규격 본문은 읽지 않았다. n18은 발표 안내문만 열람했고 영상 전체는 보지 않았다. 벤더 공식 발표도 1차 자료에 포함하지만 성능 주장은 `[추정]`으로 둔다. 신규 출처는 현재 영역 본문·절 분리 페이지에 없는 문서 11개이며, 같은 문서의 고정 태그·원문 PDF로 바꾼 것은 신규로 세지 않았다. n19는 대분류 개요에는 이미 있으나 영역 20의 출처에는 없어 신규로 센다. 엄격한 독립성 기준상 같은 Open-RMF 연동을 설명하는 n5·n20도 독립 재검증으로 세지 않았다.

[^n1]: VDA·VDMA, *Interface for the Communication between Mobile Robots and a Fleet Control*, VDA 5050 3.0.0, 2026-03, 규격 / DOI 해당 없음, https://github.com/VDA5050/VDA5050/blob/3.0.0/VDA5050_EN.md, 접근일 2026-10-10, 원문 열람.
[^n2]: VDA5050 프로젝트·KIT-IFL, *VDA 5050 3.0.0*, 릴리스 태그 3.0.0, 2026-03-18(저장소 게시 UTC); 설명상 VDA 발행 2026-03-19, 릴리스 / DOI 해당 없음, https://github.com/VDA5050/VDA5050/releases/tag/3.0.0, 접근일 2026-10-10, 원문 열람.
[^n3]: VDA, *Version 3.0 of VDA 5050 released*, 공식 보도자료, 2026-04-20, 공식 발표 / DOI 해당 없음, https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN, 접근일 2026-10-10, 원문 열람.
[^n4]: VDA, *VDA 5050*, Version 3.0.0 발행물 카탈로그, 2026-03-17(카탈로그 표시), 카탈로그 / DOI 해당 없음, https://www.vda.de/en/news/publications/publication/vda-5050, 접근일 2026-10-10, 원문 열람.
[^n5]: Open Robotics, *Mobile Robot Fleets — Programming Multiple Robots with ROS 2*, 온라인 문서; 판 번호 미확인, 발행일 미확인, 기술 문서 / DOI 해당 없음, https://osrf.github.io/ros2multirobotbook/integration_fleets.html, 접근일 2026-10-10, 원문 열람.
[^n6]: Open-RMF 개발자, *EasyTrafficLight.hpp*, rmf_ros2 태그 2.14.0, 2026-09-26(패키지 변경 이력 기준), C++ API 헤더 / DOI 해당 없음, https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/include/rmf_fleet_adapter/agv/EasyTrafficLight.hpp, 접근일 2026-10-10, 원문 열람.
[^n7]: David Lopes; Tiago Pereira; André Gonçalves; Francisco Cunha; Fernando Lopes; João Antunes; Victor Santos; Fernanda Coutinho; Jorge Barreiros; João Durães; Patrícia Santos; Fernando Simões; Pedro Ferreira; Elisabete Dinora Caldas de Freitas; João Pedro F. Trovão; João P. Ferreira; Nuno Miguel Fonseca Ferreira, *Integrated Fleet Management of Mobile Robots for Enhancing Industrial Efficiency: A Case Study on Interoperability in Multi-Brand Environments Within the Automotive Sector*, 출판본, 2025-06-27, Applied Sciences 15(13), 7235 / DOI 10.3390/app15137235, https://mdpi-res.com/d_attachment/applsci/applsci-15-07235/article_deploy/applsci-15-07235.pdf, 접근일 2026-10-10, 원문 열람.
[^n8]: Sven Franke; Dennis Lünsch; Jana Jost; Moritz Roidl, *Identification of requirements and opportunities for new types of standardized interfaces for AGV systems based on the VDA 5050 concept*, 영문 출판본, 2023-10-11, Logistics Journal: Proceedings, No.19 / DOI 10.2195/lj_proc_franke_en_202310_01, https://proc.logistics-journal.de/article/download/1067/1036/8465, 접근일 2026-10-10, 원문 열람.
[^n9]: ARM Institute, *Interoperability and Orchestration of Autonomous Mobile Robots (IO-AMRs)*, 공식 과제 소개; 판 미확인, 발행일 미확인, 과제 소개 / DOI 해당 없음, https://arminstitute.org/projects/interoperability-and-orchestration-of-autonomous-mobile-robots-io-amrs/, 접근일 2026-10-10, 원문 열람.
[^n10]: Open-RMF 개발자, *Changelog for package rmf_fleet_adapter*, rmf_ros2 태그 2.14.0, 2026-09-26, CHANGELOG / DOI 해당 없음, https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst, 접근일 2026-10-10, 원문 열람.
[^n11]: chart-singapore / CHART, *Add GoToZone feature*, rmf_ros2 PR #516; 미병합 제안, 2026-04-18(개설); 2026-10-09(확인된 최종 갱신), PR 설명·상태 / DOI 해당 없음, https://github.com/open-rmf/rmf_ros2/pull/516, 접근일 2026-10-10, 원문 열람.
[^n12]: Coaty 프로젝트 개발자, *vda-5050-lib.js — Changelog*, 태그 v1.7.0, 2026-04-29, CHANGELOG / DOI 해당 없음, https://github.com/coatyio/vda-5050-lib.js/blob/v1.7.0/CHANGELOG.md, 접근일 2026-10-10, 원문 열람.
[^n13]: InOrbit 개발자, *ROS AMR interoperability packages / massrobotics_amr_sender*, 태그 1.1.1, 발행일 미확인(태그 대상 커밋 2022-10-28), README·설정 예제 / DOI 해당 없음, https://github.com/inorbit-ai/ros_amr_interop/tree/1.1.1, 접근일 2026-10-10, 원문 열람.
[^n14]: MassRobotics AMR Interoperability Working Group, *AMR_Interop_Standard.json*, 태그 1.0, 발행일 미확인, 규격 JSON 스키마 / DOI 해당 없음, https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/1.0/AMR_Interop_Standard.json, 접근일 2026-10-10, 원문 열람.
[^n15]: Open-RMF 개발자, *Free Fleet — README*, 태그 1.3.0, 발행일 미확인(태그 대상 커밋 2024-12-31), README / DOI 해당 없음, https://github.com/open-rmf/free_fleet/blob/1.3.0/README.md, 접근일 2026-10-10, 원문 열람.
[^n16]: InOrbit.AI, *10 Companies around the World Collaborate to Showcase Robot Orchestration at Automate 2026*, 행사 시연 페이지; 판 미확인, 발행일 미확인, 벤더 공식 발표 / DOI 해당 없음, https://www.inorbit.ai/automate-2026, 접근일 2026-10-10, 원문 열람.
[^n17]: 카카오모빌리티, *카카오모빌리티, 국내 로봇 기업 협력해 ’플랫폼 기반 로봇 생태계 확장’ 지속*, 공식 보도자료, 2026-03-16, 벤더 공식 발표 / DOI 해당 없음, https://www.kakaomobility.com/newsroom/detail/카카오모빌리티-국내-로봇-기업-협력해-플랫폼-기반-로봇-생태계-확장-지속-361, 접근일 2026-10-10, 원문 열람.
[^n18]: Grey / Open Robotics Discourse; 발표자 shashank_br, *Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP)*, 세션 안내·녹화 링크; 코드 판 아님, 2026-06-25(안내); 세션 2026-07-02, 공식 커뮤니티 발표 안내 / DOI 해당 없음, https://discourse.openrobotics.org/t/interop-sig-02-july-2026-natural-language-control-of-open-rmf-fleets-via-the-model-context-protocol-mcp/55687, 접근일 2026-10-10, 원문 열람.
[^n19]: ISO, *ISO 21423 — Robotics — Industrial mobile robots — Communications and interoperability*, Edition 1, 단계 60.00의 공식 카탈로그, 발행일 미확인(카탈로그 Publication date 필드 2026-10; 완료 미확인), ISO/TC 299 카탈로그 / DOI 해당 없음, https://www.iso.org/standard/86749.html, 접근일 2026-10-10, 원문 열람 (공식 카탈로그; 규격 본문 미열람).
[^n20]: InOrbit.AI, *Developer Portal — Docs*, 온라인 문서; 판 미확인, 발행일 미확인, 개발자 문서 / DOI 해당 없음, https://developer.inorbit.ai/docs, 접근일 2026-10-10, 원문 열람.

n1의 [동일 규격 공식 PDF](https://www.vda.de/dam/jcr%3A09f03b91-13e2-4db3-bf30-4f221710071b/VDA5050-V3.0.0-2025-03.pdf) 표지에서 `Version 3.0.0, March 2026`을 재확인했다. URL 파일명의 2025를 발행연도로 쓰지 않았다.

고정 파일 보조 링크: n13 [송신 설정](https://github.com/inorbit-ai/ros_amr_interop/blob/1.1.1/massrobotics_amr_sender_py/params/sample_config.yaml), [송신 README](https://github.com/inorbit-ai/ros_amr_interop/blob/1.1.1/massrobotics_amr_sender_py/README.md); n2 [릴리스 메타데이터](https://api.github.com/repos/VDA5050/VDA5050/releases/tags/3.0.0); n11 [PR 상태 메타데이터](https://api.github.com/repos/open-rmf/rmf_ros2/pulls/516). 저장소 작업이나 코드 실행 검증은 하지 않았다.

## 부록 A. 1단계 진단표와 조사 질문

검색 전에 현재 본문과 분리된 4·6·7·8·10·11절을 끝까지 읽고 진단을 고정했다. 아래 진단은 당시의 조사 필요성 기록이며 결론이 아니다. 인용의 화면 각주 번호만 생략했다. 중복되는 요약 문장은 가능한 한 한 번만 적었다.

대상: [현재 페이지](https://mjkim84.github.io/ai-hub/categories/integration/robot-and-vendor-fleet-manager-integration/), [대분류 개요](https://mjkim84.github.io/ai-hub/categories/integration/).

절 분리 페이지: [4절](https://mjkim84.github.io/ai-hub/topics/2026/2026-09-25-area09-s4/), [6절](https://mjkim84.github.io/ai-hub/topics/2026/2026-09-25-area09-s6/), [7절](https://mjkim84.github.io/ai-hub/topics/2026/2026-09-25-area09-s7/), [8절](https://mjkim84.github.io/ai-hub/topics/2026/2026-09-25-area09-s8/), [10절](https://mjkim84.github.io/ai-hub/topics/2026/2026-09-25-area09-s10/), [11절](https://mjkim84.github.io/ai-hub/topics/2026/2026-09-25-area09-s11/).

### 약한 주장 목록

|위치|원문|점검 이유|
|---|---|---|
|본문|AMR(Autonomous Mobile Robot, 자율이동로봇) 제조사마다 자체 플릿 관리 소프트웨어를 쓰기 때문에 여러 브랜드를 섞은 플릿을 한 현장에서 운영하기 어렵다는 문제가 연구 과제로 다뤄지고 있다. [사실] 미국 ARM Institute의 IO-AMRs 과제는 이 문제를 풀려고 다중 지도 관리자·연결 계층·전역 플릿 관리자를 만드는 것을 목표로 한다. [사실]|단일 출처 또는 같은 프로젝트 문서 의존; 원문 미열람 각주 또는 미확인 표기 점검|
|본문|표준 쪽에서도 같은 문제를 다룬다. VDA 5050은 서로 다른 제조사의 AGV(Automated Guided Vehicle, 무인운반차)·AMR을 하나의 관제(fleet control)로 운용하기 위한 제조사 중립 통신 인터페이스이다. [사실]|단일 출처 또는 같은 프로젝트 문서 의존|
|본문|이 영역의 옛 분류의 질문은 개별 로봇을 직접 제어할지, 제조사 관제에 작업을 맡길지이다. Interact Analysis는 자사 분석(의견)에서 제3자 관제가 로봇에 직접 접속하는 저수준 제어가 현재 가장 흔하고 제조사 관제에 작업을 넘기는 고수준 제어가 늘고 있으나, 장기적으로 어느 쪽이 쓰일지는 아직 정해지지 않았다고 본다. [의견] 어느 쪽을 고르느냐에 따라 ROP가 공용 통로·승강기·문에서 다른 플릿과 교통을 조정할 수 있는 정도와 제조사에 요구해야 할 API가 달라질 것으로 보인다. [추정]|추정·의견 포함; 사실과 추론 분리 대상|
|본문|플릿 어댑터(Fleet Adapter) — Open-RMF에서 제조사별 API를 RMF 교통 스케줄·협상 시스템의 인터페이스에 잇고, 로봇의 예상 이동 경로(itinerary)를 시설 전체의 중앙 교통 스케줄에 보고해 플릿 사이 충돌을 찾아 협상하게 하는 구성요소이다. [사실] Open-RMF 통합 문서는 어댑터를 하드웨어별 인터페이스와 RMF 범용 인터페이스 사이의 다리로 설명한다. [사실]|단일 출처 또는 같은 프로젝트 문서 의존|
|본문|상위 시스템이 출하 팔레트 운반을 요청하면, ROP는 연동 방식에 따라 이를 VDA 5050 주문(노드·엣지와 pick·drop action)이나 제조사 관제·Open-RMF 어댑터의 이동·동작 명령으로 바꿔 전달해야 할 것으로 보인다. [추정]|추정·의견 포함; 사실과 추론 분리 대상|
|본문|개별 로봇 제어(저수준 제어·전체 제어·VDA 5050 직접 연결)는 ROP가 경로·교통을 통합 조정할 수 있는 대신 제조사가 경로 지정·중단·교체 API나 VDA 5050 지원을 제공해야 하고, 제조사 관제 위임이나 신호등·읽기 전용 수준 연동은 연동 부담이 작은 대신 공용 통로·승강기·문에서의 조정이 일시정지·재개나 상태 관측에 그칠 것으로 보인다. [추정] 두 방식의 처리량·비용을 정량 비교한 자료는 이번 조사에서 찾지 못했다.|추정·의견 포함; 사실과 추론 분리 대상|
|본문|Open-RMF 전체 제어로 붙이려면 제조사 관제(또는 로봇 API)가 로봇이 따를 명시적 경로를 지정할 수 있고, 그 경로를 언제든 중단해 새 경로로 바꿀 수 있으며, 이동 중 위치를 실시간으로 갱신해 주어야 한다. [사실]|단일 출처 또는 같은 프로젝트 문서 의존|
|본문|VDA 5050 3.0.0의 pick·drop action은 적재물이 로봇에 들어왔거나 떠났고 로봇이 새 적재 상태를 보고했을 때를 완료(FINISHED)로 정의하므로, 관제는 action 상태와 적재 상태로 적재·하역 완료를 확인할 수 있다. [사실] Open-RMF 어댑터 튜토리얼은 로봇·제조사 관제 API에 명령 완료 확인 함수를 요구한다. [사실]|단일 출처 또는 같은 프로젝트 문서 의존|
|본문|주문 거절 오류(NO_ROUTE_TO_TARGET 등), 연결 단절(CONNECTION_BROKEN), Open-RMF 로봇 상태 error가 보고되면 ROP는 이를 공통 예외로 옮겨 다른 로봇·플릿 재배정이나 사람 확인으로 넘겨야 할 것으로 보인다. [추정]|추정·의견 포함; 사실과 추론 분리 대상|
|본문|Open-RMF 플릿 어댑터는 제조사 관제나 로봇 API가 허용하는 제어 수준에 따라 전체 제어·신호등·읽기 전용 가운데 하나로 RMF에 붙는다. [사실] 아래는 이번 조사에서 확인한 연동 방식이다.|단일 출처 또는 같은 프로젝트 문서 의존|
|본문|VDA 5050 3.0.0은 제조사 중립 관제–로봇 인터페이스로서 팩트시트, 주문 거절 오류, action 진행 상태 보고를 둔다. [사실] 아래 표는 이 영역이 참조하는 표준과 공개 구현이다.|단일 출처 또는 같은 프로젝트 문서 의존|
|본문|VDA 5050이 주변 설비 인터페이스를 다루지 않는다는 한계를 지적한 연구가 있다. [사실] 이번 조사에서 찾은 국내 자료는 기사·벤더 발표뿐이다.|단일 출처 또는 같은 프로젝트 문서 의존|
|본문|이종 제조사를 잇는 어댑터의 명령·상태·오류 변환, 지도 좌표 변환, 완료 확인, 교통·설비 조정 인터페이스 [추정]|추정·의견 포함; 사실과 추론 분리 대상|
|본문|연계 대상: 로컬 경로 계획·장애물 회피·위치추정 같은 로봇 자체 주행 기능은 로봇·제조사 쪽에 남는 것으로 보인다. [추정]|추정·의견 포함; 사실과 추론 분리 대상|
|본문|로봇 작업과 설비를 잇는 별도 인터페이스. [추정] VDA 5050은 AGV·관제와 주변 설비 사이 인터페이스를 다루지 않는다. [사실]|추정·의견 포함; 사실과 추론 분리 대상|
|본문|연계 대상: 승강기·문 제어 자체. Open-RMF 커뮤니티는 승강기·문 어댑터를 플릿 어댑터와 따로 둔다. [사실]|단일 출처 또는 같은 프로젝트 문서 의존|
|본문|이종 제조사를 잇는 ROP의 어댑터는 명령·상태·오류 변환, 지도 좌표 변환, 완료 확인, 교통·설비 조정 인터페이스를 맡는 것으로 보인다. [추정] 교통 조정은 VDA 5050 명세 범위 밖이어서 관제 구현의 몫으로 남는다. [사실]|추정·의견 포함; 사실과 추론 분리 대상|
|본문|분류 원문 19장은 이 경계가 제품 전략에 따라 이동할 수 있다고 보며, 이종 제조사를 연결하는 ROP는 로컬 주행 기능을 제조사에 맡기고 "인터페이스와 실행 보장을 담당할 수 있다"고 적는다(범위 경계). free_fleet처럼 내비게이션 스택에 직접 붙는 방식도 주행 기능을 ROP로 가져오는 것이 아니라 연결 지점을 바꾸는 것이다. [추정]|추정·의견 포함; 사실과 추론 분리 대상|
|본문|5. 로봇 능력·작업 표현 — VDA 5050 팩트시트와 Open-RMF task_capabilities 선언은 능력 모델과 맞춰야 할 입력으로 보인다. [추정]|추정·의견 포함; 사실과 추론 분리 대상|
|절분리 4|플릿 어댑터(Fleet Adapter) — Open-RMF에서 제조사별 API를 RMF 교통 스케줄·협상 시스템의 인터페이스에 잇고, 로봇의 예상 이동 경로(itinerary)를 시설 전체의 중앙 교통 스케줄에 보고해 플릿 사이 충돌을 찾아 협상하게 하는 구성요소이다. [사실] Open-RMF 통합 문서는 어댑터를 하드웨어별 인터페이스와 RMF 범용 인터페이스 사이의 다리로 설명한다. [사실]|단일 출처 또는 같은 프로젝트 문서 의존|
|절분리 4|제어 수준(control level) — Open-RMF는 플릿 어댑터를 RMF가 받는 제어 수준에 따라 전체 제어(Full Control)·신호등(Traffic Light)·읽기 전용(Read Only)·인터페이스 없음(No Interface) 네 범주로 나눈다. [사실] 전체 제어는 실시간 상태와 개별 로봇 경로의 전체 제어를, 신호등은 상태와 로봇별 일시정지·재개 제어를, 읽기 전용은 정기 상태 보고만을 RMF에 준다. [사실]|단일 출처 또는 같은 프로젝트 문서 의존|
|절분리 4|플릿 관리 시스템(Fleet Management System, FMS)·제조사 관제 — 로봇 제조사가 자사 로봇용으로 제공하는 관제 소프트웨어로, AMR 제조사마다 자체 플랫폼을 쓴다. [사실]|단일 출처 또는 같은 프로젝트 문서 의존|
|절분리 4|저수준 제어·고수준 제어(Low-Level Control, High Level Control) — Interact Analysis의 구분(의견)으로, 제3자 관제가 로봇에 직접 접속해 제어하면 저수준, 각 제조사 관제에 작업을 넘기면 고수준이다. [의견]|추정·의견 포함; 사실과 추론 분리 대상|
|절분리 4|메시지 큐잉 원격 측정 전송(Message Queuing Telemetry Transport, MQTT) — VDA 5050 3.0.0이 JSON(JavaScript Object Notation)과 함께 쓰는 메시징 프로토콜로, 명세는 최소 3.1.1판을 요구한다. [사실]|단일 출처 또는 같은 프로젝트 문서 의존|
|절분리 4|주문의 base·horizon 구간 — VDA 5050 3.0.0 주문은 노드·엣지 그래프를 순서 번호(sequenceId)대로 보내며, 실행이 허용된 base 구간과 계획만 된 horizon 구간으로 나눈다. [사실]|단일 출처 또는 같은 프로젝트 문서 의존|
|절분리 4|팩트시트(factsheet) — VDA 5050에서 로봇이 적재 명세·지원 action을 관제에 알리는 메시지이다. [사실]|단일 출처 또는 같은 프로젝트 문서 의존|
|절분리 6|Open-RMF 플릿 어댑터는 제조사 관제나 로봇 API가 허용하는 제어 수준에 따라 전체 제어·신호등·읽기 전용 가운데 하나로 RMF에 붙는다. [사실] 아래는 이번 조사에서 확인한 연동 방식이다.|단일 출처 또는 같은 프로젝트 문서 의존|
|절분리 6|Open-RMF 플릿 어댑터 튜토리얼은 로봇·제조사 관제 API에 이동 명령(목적지 좌표·지도 이름·선택 속도 제한), 정지, 사용자 정의 동작 시작, 위치([x, y, theta])·현재 지도 이름·배터리 충전 상태 조회, 명령 완료 확인을 요구하고, navigate·stop·execute_action 세 콜백을 RMF 명령 실행의 기본으로 둔다. [사실] 로봇별 상태 조회는 비동기 갱신 루프로 처리해 한 로봇의 조회 오류가 다른 로봇의 상태 갱신을 막지 않게 한다. [사실]|단일 출처 또는 같은 프로젝트 문서 의존|
|절분리 6|어댑터 템플릿 설정은 제조사 관제 접속 정보(주소·사용자·암호), RMF 지도와 로봇 지도의 좌표 대응점 목록(reference_coordinates), 속도·가속 한계와 차체 반경, 배터리 사양, 플릿이 수행할 수 있는 작업 유형(task_capabilities)을 플릿 단위로 적게 한다(값은 템플릿 예시값). [사실]|단일 출처 또는 같은 프로젝트 문서 의존|
|절분리 6|VDA 5050 3.0.0은 관제에서 로봇으로 가는 order·instantActions·zoneSet·responses 토픽과 로봇에서 관제로 가는 state·visualization·connection·factsheet 토픽을 둔다. [사실] 주문 갱신은 orderId·orderUpdateId로 추적한다. [사실]|단일 출처 또는 같은 프로젝트 문서 의존|
|절분리 6|connection 토픽은 ONLINE·OFFLINE·CONNECTION_BROKEN·HIBERNATING 상태를 두며, 로봇은 연결할 때 CONNECTION_BROKEN을 담은 MQTT 유언 메시지(last will)를 설정해 비정상 단절 시 브로커가 관제에 대신 알리게 한다. [사실] 교통 관리 로직과 교통 조정 알고리즘은 명세 범위에서 빠져 있어 교통 조정 방식은 관제 구현에 맡겨진다. [사실]|단일 출처 또는 같은 프로젝트 문서 의존|
|절분리 6|Open-RMF의 free_fleet은 fleet_adapter_template 기반 Python 플릿 어댑터로, 제조사 관제를 거치지 않고 각 로봇의 Nav2(ROS 2 Jazzy)·Nav1(ROS 1 Noetic) 내비게이션 스택에 zenoh 통신 계층으로 직접 접속한다. [사실] Nav1 통합은 시뮬레이션과 ROS 1 Noetic에서만 시험됐다. [사실] 이는 연동 방식의 사례이며, 주행 기능 자체의 범위는 9절을 따른다.|단일 출처 또는 같은 프로젝트 문서 의존|
|절분리 6|Open-RMF 로봇 상태 스키마는 상태 값을 uninitialized·offline·shutdown·idle·charging·working·error 일곱 가지로 두고, 운영자가 알아야 할 문제를 범주(category)와 자유 형식 상세(detail)로 된 issues 배열로 보고한다. [사실] 인터페이스마다 상태 어휘가 달라(Open-RMF 로봇 상태 7종, VDA 5050 action 상태·주문 거절 오류 유형, MassRobotics 운용 상태 9종) 어댑터는 이를 ROP 공통 상태·오류로 옮기는 변환표를 가져야 할 것으로 보이며, 이들 사이의 공개 표준 매핑은 이번 검색에서 확인하지 못했다. [추정]|추정·의견 포함; 사실과 추론 분리 대상; 원문 미열람 각주 또는 미확인 표기 점검|
|절분리 7|VDA 5050 3.0.0은 제조사 중립 관제–로봇 인터페이스로서 팩트시트, 주문 거절 오류, action 진행 상태 보고를 둔다. [사실] 아래 표는 이 영역이 참조하는 표준과 공개 구현이다.|단일 출처 또는 같은 프로젝트 문서 의존|
|절분리 7|공식 저장소 main 명세의 판 표기는 3.0.0이고 VDA가 3.0 판 발행을 보도자료로 알렸으나, 정확한 발행일은 미확인이다(oq-005). [사실]|단일 출처 또는 같은 프로젝트 문서 의존; 원문 미열람 각주 또는 미확인 표기 점검|
|절분리 7|로봇이 적재 명세·지원 action을 담은 팩트시트를 factsheet 토픽으로 관제에 알리고, 사전 정의 action으로 옮길 수 없는 동작은 제조사가 추가 action을 정의해 관제가 쓰게 한다. [사실]|단일 출처 또는 같은 프로젝트 문서 의존|
|절분리 7|로봇은 받을 수 없는 주문을 상태 메시지의 오류로 거절하며, 거절 오류 유형에 VALIDATION_FAILURE·UNSUPPORTED_PARAMETER·INVALID_ORDER_ACTION·OUTDATED_ORDER_UPDATE·SAME_ORDER_UPDATE_ID·START_NODE_OUT_OF_RANGE·NO_ROUTE_TO_TARGET 등이 있다. [사실] 상태 메시지는 현재 orderId·orderUpdateId, 마지막으로 지난 노드(lastNodeId·lastNodeSequenceId), action 진행 상태(INITIALIZING·RUNNING·PAUSED·FINISHED·FAILED·RETRIABLE 등)를 보고한다. [사실]|단일 출처 또는 같은 프로젝트 문서 의존|
|절분리 7|여러 제조사 AMR이 같은 공간에서 위치·속도·방향·상태·작업 가용성 정보를 공유하게 하는 것이 목적이며, 공식 JSON 스키마는 식별 보고(identityReport)와 상태 보고(statusReport) 두 메시지만 정의해 로봇에 명령을 보내는 메시지를 두지 않는다. [사실]|단일 출처 또는 같은 프로젝트 문서 의존|
|절분리 7|어댑터 설정에 플릿이 수행할 수 있는 작업 유형(task_capabilities)을 선언하고 [사실], 사용자 정의 동작 시작(start_activity)과 execute_action 콜백으로 제조사 고유 동작을 실행한다. [사실]|단일 출처 또는 같은 프로젝트 문서 의존|
|절분리 7|제조사 관제 없이 로봇 내비게이션 스택에 zenoh로 붙는 Python 플릿 어댑터(6절). [사실]|단일 출처 또는 같은 프로젝트 문서 의존|
|절분리 7|Open-RMF 커뮤니티 어댑터 목록으로, MiR(MiR Fleet)·OTTO Motors·Clearpath·InOrbit 등 제조사·플랫폼별 플릿 어댑터와 KONE 등 승강기 어댑터, 문·기기 어댑터를 함께 모아 둔다. [사실]|단일 출처 또는 같은 프로젝트 문서 의존|
|절분리 7|InOrbit이 공개한 저장소로, ROS 2 로봇을 MQTT 기반 VDA 5050 관제에 연결하는 VDA5050 커넥터와 ROS 2 데이터를 YAML 매핑으로 MassRobotics 상호운용 수신기에 보내는 송신 노드를 제공한다. [사실] README 빌드 표 기준(확인일 2026-09-25) VDA5050 패키지는 ROS 2 Galactic, MassRobotics 송신 노드는 Foxy·Galactic 대상이다. [사실]|단일 출처 또는 같은 프로젝트 문서 의존; 원문 미열람 각주 또는 미확인 표기 점검|
|절분리 8|VDA 5050이 주변 설비 인터페이스를 다루지 않는다는 한계를 지적한 연구가 있다. [사실] 이번 조사에서 찾은 국내 자료는 기사·벤더 발표뿐이다.|단일 출처 또는 같은 프로젝트 문서 의존|
|절분리 8|Franke, S., Lünsch, D., Jost, J., & Roidl, M., Identification of requirements and opportunities for new types of standardized interfaces for AGV systems based on the VDA 5050 concept(2023) — VDA 5050이 AGV·관제 사이 인터페이스만 다루고 AGV·관제와 주변 설비 사이 인터페이스는 다루지 않는다고 지적하고, 소프트웨어 공급사·하드웨어 제조사·사용자 워크숍으로 새 표준 인터페이스 요구를 정리했다. [사실]|단일 출처 또는 같은 프로젝트 문서 의존; 원문 미열람 각주 또는 미확인 표기 점검|
|절분리 8|ScienceDirect 게재 논문(저자 미확인), Heterogeneous multi-agent fleet control system for material handling in a Software-Defined Factory(2026) — 상용 다중 제조사 AMR 플릿과 천장 반송 차량(OHT)·바닥 AGV 사이의 작업 조정을 한 소프트웨어 정의 공장 틀에 넣고, 통신·위치추정·경로계획·작업 배정을 중앙 시스템이 다루는 이종 플릿 제어 시스템을 제안했다. [사실] 제조 공장 대상 연구이므로 물류센터 사례가 아니라 방법 참고로 본다.|단일 출처 또는 같은 프로젝트 문서 의존; 원문 미열람 각주 또는 미확인 표기 점검|
|절분리 8|Applied Sciences 게재 논문(저자 미확인), Integrated Fleet Management of Mobile Robots for Enhancing Industrial Efficiency(2025) — 자동차 공장에서 여러 제조사 AGV·AMR의 위치·상태를 하나의 지도와 웹 플랫폼으로 통합해 감시하는 플릿 관리 소프트웨어를 개발했고, 향후 VDA 5050 통합을 고려한 구조를 두었다. [사실] 작업 상태 갱신 평균 지연 120 ms를 보고했으나 단일 출처이고 측정 조건은 미확인이다. [사실]|단일 출처 또는 같은 프로젝트 문서 의존; 원문 미열람 각주 또는 미확인 표기 점검|
|절분리 8|ARM Institute, Interoperability and Orchestration of Autonomous Mobile Robots(IO-AMRs, 연도 미확인) — 제조사별 플릿 관리 소프트웨어로 인한 혼합 플릿 운영 문제를 다루는 과제이다(3절). [사실]|단일 출처 또는 같은 프로젝트 문서 의존; 원문 미열람 각주 또는 미확인 표기 점검|
|절분리 8|헬로티 기사 — MiR이 기존 RESTful 로봇 인터페이스를 MQTT와 연결해 자사 AMR과 타사 관제 사이에 VDA 5050 메시지를 주고받게 하는 어댑터 'MiR VDA 5050'을 출시했다고 보도했다. [추정] 벤더 주장5|추정·의견 포함; 사실과 추론 분리 대상|
|절분리 8|클로봇 제품 소개 — 브랜드·이동 방식과 무관하게 이기종 로봇을 하나의 시스템처럼 관제한다는 클라우드 기반 플릿 관리 시스템(CROMS)을 제공한다고 밝힌다. [추정] 벤더 주장6|추정·의견 포함; 사실과 추론 분리 대상|
|절분리 8|디지털투데이 기사(2026-05) — 카카오모빌리티가 서비스 요청을 로봇 실행 단위로 추상화하는 Task, 이기종 로봇을 통합 표준 API로 잇는 Command Interface, 장애 시 작업을 다른 로봇에 재배정하는 Reallocation, 건물 인프라·기존 시스템을 잇는 Integration Backbone을 로봇 플랫폼 구성으로 발표했다. [추정] 벤더 주장7|추정·의견 포함; 사실과 추론 분리 대상|
|절분리 8|머니투데이 기사(2026-07-14) — 노바테크가 현대자동차그룹 메타플랜트 아메리카에서 12종 약 300대의 이기종 물류 로봇을 자사 오케스트레이션 플랫폼 하나로 통합 운영한다고 보도됐다. [추정] 벤더 주장8 대상은 전기차 생산 공장이며 물류센터 사례가 아니다.|추정·의견 포함; 사실과 추론 분리 대상|
|절분리 10|15. 지도·공간·위치 모델 — 어댑터 설정의 RMF 지도–로봇 지도 좌표 대응점(reference_coordinates)이 지도 모델과 이어지는 지점으로 보인다. [추정]|추정·의견 포함; 사실과 추론 분리 대상|
|절분리 10|22. 설비·건물 시스템 연동 — VDA 5050은 주변 설비 인터페이스를 다루지 않는다. [사실] Open-RMF 커뮤니티 목록은 승강기·문 어댑터를 플릿 어댑터와 함께 모은다. [사실]|단일 출처 또는 같은 프로젝트 문서 의존|
|절분리 10|42. 분산 시스템·통신·컴퓨팅 구조 — VDA 5050은 MQTT 브로커와 유언 메시지로 연결 단절을 관제에 알린다. [사실]|단일 출처 또는 같은 프로젝트 문서 의존|
|절분리 10|29. 명령·작업 실행의 신뢰성 — 주문 갱신 id, 주문 거절 오류, action 진행 상태는 명령 실행 상태 관리의 재료이다. [추정]|추정·의견 포함; 사실과 추론 분리 대상|
|절분리 10|25. 작업 배정 — MRTA — 장애 시 작업을 다른 로봇에 넘기는 재배정은 배정 문제와 이어진다. [추정] 벤더 주장7|추정·의견 포함; 사실과 추론 분리 대상|
|절분리 10|27. 다중 로봇 경로·교통 관리 — MAPF — Open-RMF는 어댑터가 보고한 예상 경로로 플릿 사이 충돌을 협상하고 [사실], VDA 5050은 교통 조정 알고리즘을 범위 밖으로 둔다. [사실]|단일 출처 또는 같은 프로젝트 문서 의존|
|절분리 10|32. 예외 복구·재계획·업무 연속성 — 거절 오류·연결 단절·로봇 error 뒤의 재배정·사람 확인 규칙이 필요할 것으로 보인다. [추정]|추정·의견 포함; 사실과 추론 분리 대상|

### 우선순위 조사 질문과 답변 기준

- Q1: VDA 5050 3.0.0의 발행·공표일과 ISO 21423의 현재 상태는 무엇인가? 답변 기준: 공식 표지·릴리스·발표 날짜를 구분하고, ISO 공식 카탈로그의 단계와 확인일을 확보한다.
- Q2: 연동 위치(로봇 직접/제조사 관제)와 RMF 제어 수준은 같은 구분인가? 제한 제어의 한계와 비교 근거는 무엇인가? 답변 기준: API 계약과 실제 구현·연구에서 구분 근거를 찾고, 같은 조건의 처리량·비용 비교가 있는지 확인한다.
- Q3: 세 체계의 상태·오류 변환과 단절 후 상태 확인에 쓸 공개 구현이 있는가? 답변 기준: 고정 판 스키마·코드의 필드와 변환 함수를 확인하고, 공통 표준 매핑인지 개별 구현인지 구별한다.
- Q4: 현재 인용한 연구의 원문과 실험 조건은 무엇이며 비창고 사례를 보강할 수 있는가? 답변 기준: 논문 본문에서 저자·DOI·실물/시뮬레이션·규모·120 ms 측정 조건을 확인한다.
- Q5: 최근 1년 Open-RMF zone 및 free_fleet 변경은 실제 공개 구현에 어디까지 반영됐는가? 답변 기준: 태그 고정 코드·CHANGELOG와 문서를 비교하고 제안·병합·릴리스를 구분한다.
- Q6: Automate 2026·국내 도입·자연어/MCP 플릿 제어의 실증 범위는 어디까지인가? 답변 기준: 행사 후 공식 자료·구현·고객 자료에서 참여 주체와 실물/시연 범위를 확인하고 독립 검증 여부를 기록한다.

### 빈 곳·얕은 곳
|절|진단|
|---|---|
|1·2|정의·핵심 질문 있음. 제어 위임·통신의 판단 기준은 후속 보강 필요.|
|3|IO-AMRs 원문 미열람. 시장 추세는 분석업체 의견 1개.|
|4|제어 수준·연동 위치를 구분하는 표 없음.|
|5|가상 물류창고만 있음. 실물 검증 규모·운영 기간·타 현장 사례 부족.|
|6|API 기본 요건 있음. 상태 매핑 구현과 제한 제어의 검증 근거 부족.|
|7|main 링크 중심. VDA 발행일 미확인. 구역 기능과 릴리스 추적 부족.|
|8|원문 미열람 논문에 사실 태그. 저자·DOI·실험 조건 빠짐.|
|9|책임 경계 있음. 연동 위치가 제어 권한을 결정한다는 추론 재점검 필요.|
|10|연결 목록 있음. ISO 진행 단계 등 최신 확인 없음.|
|11|8개 질문 있음. 범위가 다른 인계·업무 매핑 질문은 이번 내용 확장 대상 아님.|
|12|자동 이력 있음. 직접 수정 제안 대상 아님.|
|13|출처 목록 있음. 날짜·원문 열람·고정 판 미흡.|

### 오래된 정보 후보
|원문|후보 이유|
|---|---|
|Franke, S., Lünsch, D., Jost, J., & Roidl, M., Identification of requirements and opportunities for new types of standardized interfaces for AGV systems based on the VDA 5050 concept(2023)|2023 연구의 표준 범위를 2026 판에 그대로 적용했는지 확인 필요. 연구 자체가 틀렸다는 뜻은 아님.|
|README 빌드 표 기준(확인일 2026-09-25) VDA5050 패키지는 ROS 2 Galactic, MassRobotics 송신 노드는 Foxy·Galactic 대상이다.|버전명에 연도는 없으나 구 배포판이므로 별도 후보로 점검. 전후 호환성 단정 금지.|
|옛 정의·이전 분류 날짜|2026 날짜이며 역사 기록. 구정보 수정 대상으로 보지 않음.|

### 열린 질문 원문
- oq-001 (열림 · 제기 2026-09-25 · 실행 2026-09-25-01) 로봇의 적재·하역 완료 신호(VDA 5050 drop 동작 완료, Open-RMF IngestorResult)를 EPCIS 인계 이벤트로 옮기는 표준 매핑이나 공개 구현 사례가 있는가?
- oq-005 (열림 · 제기 2026-09-25 · 실행 2026-09-25-02) 출처 충돌: VDA 5050 3.0.0의 정확한 발행일은 언제인가? 검색 요약은 3.0 발행을 2026-03-19, 보도자료를 2026-04-20로 전하지만 보도자료 URL은 2026-04-21 계열이다.
- oq-007 (열림 · 제기 2026-09-25 · 실행 2026-09-25-03) VDA 5050 3.0.0에서 관제가 loadId를 정할 때 SSCC 같은 GS1 키를 그대로 쓰도록 권고하거나 제약하는 규정이 있는가, 로봇이 판독한 식별자와 다르면 어떻게 보고하는가?
- oq-014 (열림 · 제기 2026-09-25 · 실행 2026-09-25-09) 업무 프로세스 모델(BPMN 등)의 단계 상태와 로봇 작업 상태(Open-RMF 작업 상태, VDA 5050 동작 상태)를 동기화하는 표준 매핑이나 공개 구현이 있는가?
- oq-020 (열림 · 제기 2026-09-25 · 실행 2026-09-25-13) ISA-95 작업 지시·작업 응답(B2MML, OPC UA for ISA-95 Job Control)을 VDA 5050 주문·상태나 Open-RMF 작업 요청·상태로 옮기는 표준 매핑이나 공개 구현이 있는가?
- 신규 (열림 · 제기 2026-09-25 · 실행 2026-09-25-20) 국내 물류센터에서 로봇을 직접 제어하는 방식과 제조사 관제에 작업을 넘기는 방식 가운데 어느 쪽이 쓰이는지, 선택 기준이나 처리량·연동 비용을 비교한 공개 자료가 있는가?
- 신규 (열림 · 제기 2026-09-25 · 실행 2026-09-25-20) 제조사 관제가 일시정지·재개나 상태 보고만 허용할 때 공용 통로·승강기·문에서 다른 플릿과의 교착을 어떻게 막는가, 제어 수준에 따른 교통 성능 차이를 측정한 연구가 있는가?
- 신규 (열림 · 제기 2026-09-25 · 실행 2026-09-25-20) Open-RMF 로봇 상태, VDA 5050 action 상태·오류, MassRobotics 운용 상태를 하나의 공통 상태·오류 어휘로 옮기는 표준 매핑이나 공개 구현이 있는가?

## 부록 B. 검색 기록

날짜는 모두 2026-10-10이다. “건진 출처 수”는 검색 결과 전체 수가 아니라 후보로 남긴 고유 문서 수다. 재검색에서 같은 자료를 다시 찾은 경우도 해당 행에는 표시하되 질문별 후보 합계에서는 한 번만 센다. 검색 관점 수와 독립 출처 수는 다른 지표다. 관점을 바꾼 검색에서 결과가 없으면 0으로 기록했다. 1차 탐색→후보 수집→원문 확인 중 후속 링크·확인 검색→초안→재대조 순서로 진행했다.

### 질문별 관점 검색

|질문|관점|검색어|날짜|건진 출처 수|후보|
|---|---|---|---|---:|---|
|Q1|① 표준·규격 기관|`"VDA 5050" site.vda.de "2026" "March"`|2026-10-10|2|n1, n4; PDF 미러 중복 제외|
|Q1|② 오픈소스|`"VDA5050" "3.0.0" "releases" site.github.com`|2026-10-10|1|n2|
|Q1|④ 산업|`"VDA 5050" "February 17th" Idealworks`|2026-10-10|1|X1|
|Q2|② 오픈소스|`"Mobile Robot Fleets" "fleet manager" site.osrf.github.io`|2026-10-10|1|n5|
|Q2|③ 학술|`"Integrated Fleet Management" "low-level control"`|2026-10-10|1|n7; DOI·MDPI·ResearchGate는 한 문서|
|Q2|⑥ 반대·한계|`"Feature and limitation of traffic-light adapter"`|2026-10-10|1|X2|
|Q3|① 표준·규격 기관|`"AMR_Interop_Standard" "operationalState"`|2026-10-10|0|정확 문자열 결과 없음; 선행 검색·위키 링크로 n14 확보|
|Q3|② 오픈소스|`"ros_amr_interop" "mapping"`|2026-10-10|2|n13, n20|
|Q3|③ 학술|`"Identification of requirements and opportunities" "VDA 5050"`|2026-10-10|1|n8; 재게시 중복 제외|
|Q4|③ 학술|`"Heterogeneous multi-agent fleet control system"`|2026-10-10|1|X3; 출판사·KAIST는 같은 논문|
|Q4|④ 산업·현장|`"Interoperability and Orchestration of Autonomous Mobile Robots" "ARM"`|2026-10-10|1|n9|
|Q4|⑥ 반대·한계|`"Integrated Fleet Management" "7235" "laboratory"`|2026-10-10|1|n7; 같은 논문 재대조|
|Q5|② 오픈소스|`"rmf_ros2" "GoToZone" "516"`|2026-10-10|2|X6와 연결된 n11|
|Q5|④ 산업·현장|`"CHART" "Open-RMF" "zone" "2026"`|2026-10-10|2|X5, X6|
|Q5|⑥ 반대·한계|`"free_fleet" "Nav1" "simulation"`|2026-10-10|1|n15; 포크·요약 제외|
|Q6|④ 산업·현장|`"Automate 2026" "InOrbit" "10 Companies"`|2026-10-10|1|n16|
|Q6|⑤ 국내|`site.kakaomobility.com "로보티즈" "2026-03-16"`|2026-10-10|1|n17; 재인용 기사 제외|
|Q6|② 오픈소스|`"Nayantra" "Open-RMF" "MCP"`|2026-10-10|3|X7, X10, 연결된 n18; 동일 프로젝트로 표시|

### 추가 탐색 기록

|관점|검색어|날짜|건진 출처 수|
|---|---|---|---:|
|① 표준/Q1|`site.vda.de VDA 5050 3.0 released April 2026 March 19 ISO 21423`|2026-10-10|3 (n1·n3·n4)|
|① 표준/Q1|`"ISO 21423" 2026 FDIS published`|2026-10-10|1 (n19)|
|⑤ 국내/Q1|`"VDA 5050" "3.0" 발행 2026`|2026-10-10|0 (국문 2차 해설은 결론에서 제외)|
|⑤ 국내/Q2|`로봇 제조사 관제 직접 제어 위임 비용 처리량 Open RMF`|2026-10-10|0 (동등 조건 비교 미확보)|
|② 코드/Q2|`site.github.com/open-rmf traffic light read only deadlock limitations`|2026-10-10|1 (API로 추적한 n6)|
|① 표준/Q3|`"VDA 5050" "MassRobotics" state mapping specification`|2026-10-10|2 (n1·n14 원문으로 추적)|
|③ 학술/Q3|`"robot interoperability" "state" mapping "VDA" paper`|2026-10-10|1 (n8)|
|⑤ 국내/Q3|`로봇 상태 오류 매핑 VDA 5050 Open-RMF 표준`|2026-10-10|0|
|③ 학술/Q4|`"Integrated Fleet Management" "120" "7235"`|2026-10-10|1 (n7)|
|③ 학술/Q4|`"multi-vendor" "fleet" "Open-RMF" limitations experiment 2025 2026 paper`|2026-10-10|1 (X4)|
|② 코드/Q5|`site.github.com/open-rmf "zone" "2026"`|2026-10-10|2 (n11·X6; 연결 태그 이력 n10 추가)|
|④ 현장/Q5|`site.discourse.openrobotics.org "zone" "2026" RMF`|2026-10-10|1 (X5)|
|⑤ 국내/Q5|`Open RMF 구역 zone 기능 2026 로봇 관제`|2026-10-10|0|
|① 표준/Q5|`"VDA 5050" "Open-RMF" "zones" 2026`|2026-10-10|0 (규격 간 직접 대응 자료 미확보)|
|③ 학술/Q5|`"Open-RMF" "zone" paper 2025 2026`|2026-10-10|0 (해당 기능 검증 논문 미확보)|
|① 기관/Q6|`site.massrobotics.org Automate 2026 interoperability demonstration`|2026-10-10|0 (해당 시연의 독립 기술 평가 미확보)|
|④ 산업/Q6|`"Automate 2026" interoperability AMR demo InOrbit`|2026-10-10|2 (n16·X12)|
|⑤ 국내/Q6|`로봇 통합 관제 제조사 연동 실증 2026 노바테크 카카오모빌리티 공식`|2026-10-10|1 (후속 공식 검색으로 n17 추적)|
|⑤ 국내/Q6|`site.novatech.co.kr 메타플랜트 로봇 300`|2026-10-10|1 (X9 기사; 업체·고객 원자료 미확보)|

### 질문별 후보 목록과 선정

|질문|서로 다른 후보 문서(5개 이상)|분석 결과·위키 대조|
|---|---|---|
|Q1|n1·n2·n3·n4·n19·X1 (6)|발행·게시·보도·채택을 분리. oq-005 부분 답변. ISO는 10절 연결만.|
|Q2|n5·n6·n7·n20·X2·n15 (6)|5절의 연동 위치/제어 권한 묶음 정정. 계약 요건 추가. 비용 우열은 미확인.|
|Q3|n1·n13·n14·n12·n8 (5)|구체적인 ROS→MassRobotics 필드만 추가. 3체계 공통 표준은 미확인. 규격별 상태 목록 단순 반복은 제외.|
|Q4|n7·n8·n9·X3·X4 (5)|n7 지표·장소 정정. n8 연구 방법·n9 과제 단계 추가. X3·X4 결론 배제.|
|Q5|n10·n11·n15·X5·X6·X11 (6)|발표·미병합 PR·태그 릴리스를 구별. 위키에 있는 Nav1 시뮬레이션 제한은 반복 추가하지 않음.|
|Q6|n16·n17·n18·X7·X8·X9·X10·X12 (8)|전시·호텔 사례 추가. 벤더 성과는 추정. 노바테크 보도 반복은 교차 확인으로 세지 않음. MCP는 10절 연결.|

후보 수는 문서 수이며 독립 연구팀 수가 아니다. README의 다른 호스트, DOI 리디렉션, 같은 논문의 재게시를 추가 후보로 세지 않았다. 후보 원문 접근 시도와 제외 이유는 부록 C에 모두 남겼다. 최근 1년 점검은 n2~n4·n10~n12·n16~n19 및 X5~X7이 담당한다.

## 부록 C. 출처 평가표

### 채택 출처 20개

서지의 전체 저자·정확한 제목·판·발행일·게재지·DOI·URL은 같은 행의 각주 정의와 일치한다. 아래 표의 논문은 출판본이며 arXiv 판은 없다. 모든 접근일은 2026-10-10이다.

|후보·서지|열람 상태|1차/2차·독립성|신뢰도와 이유|
|---|---|---|---|
|n1: VDA·VDMA, Interface for the Communication between Mobile Robots and a Fleet Control; VDA 5050 3.0.0; 2026-03; 규격 / DOI 해당 없음 [^n1]|원문 열람|1차; VDA 규격 계열: n2~n4와 동일|high: 고정 판 규범 원문|
|n2: VDA5050 프로젝트·KIT-IFL, VDA 5050 3.0.0; 릴리스 태그 3.0.0; 2026-03-18(저장소 게시 UTC); 설명상 VDA 발행 2026-03-19; 릴리스 / DOI 해당 없음 [^n2]|원문 열람|1차; n1·n3·n4와 동일 계열|high: 게시 메타데이터와 설명 직접 확인; 날짜 의미 구분|
|n3: VDA, Version 3.0 of VDA 5050 released; 공식 보도자료; 2026-04-20; 공식 발표 / DOI 해당 없음 [^n3]|원문 열람|1차; VDA 계열|high: 본문 날짜 직접 확인|
|n4: VDA, VDA 5050; Version 3.0.0 발행물 카탈로그; 2026-03-17(카탈로그 표시); 카탈로그 / DOI 해당 없음 [^n4]|원문 열람|1차; VDA 계열|high: 표시 날짜 확인; 문서 발행과 동일 사건인지 미확인|
|n5: Open Robotics, Mobile Robot Fleets — Programming Multiple Robots with ROS 2; 온라인 문서; 판 번호 미확인; 발행일 미확인; 기술 문서 / DOI 해당 없음 [^n5]|원문 열람|1차; Open-RMF: n6·n10·n11·n15와 공통 생태계|high: API 통합 문서; 운영 성능 검증 아님|
|n6: Open-RMF 개발자, EasyTrafficLight.hpp; rmf_ros2 태그 2.14.0; 2026-09-26(패키지 변경 이력 기준); C++ API 헤더 / DOI 해당 없음 [^n6]|원문 열람|1차; n5·n10·n11과 같은 프로젝트|high: 고정 태그 API 계약|
|n7: David Lopes 외 16명(전체 저자는 n7), Integrated Fleet Management of Mobile Robots for Enhancing Industrial Efficiency: A Case Study on Interoperability in Multi-Brand Environments Within the Automotive Sector; 출판본; 2025-06-27; Applied Sciences 15(13), 7235 / DOI 10.3390/app15137235 [^n7]|원문 열람|1차; Coimbra·GreenAuto 연구팀; n8·n9와 독립|medium: 본문 확보; 120 ms 지표 표현 충돌·실험 세부 부족|
|n8: Sven Franke; Dennis Lünsch; Jana Jost; Moritz Roidl, Identification of requirements and opportunities for new types of standardized interfaces for AGV systems based on the VDA 5050 concept; 영문 출판본; 2023-10-11; Logistics Journal: Proceedings, No.19 / DOI 10.2195/lj_proc_franke_en_202310_01 [^n8]|원문 열람|1차; TU Dortmund·Fraunhofer IML 연구팀; 다른 연구팀과 독립|high: 본문·서지 확인; 워크숍 결과에 한정|
|n9: ARM Institute, Interoperability and Orchestration of Autonomous Mobile Robots (IO-AMRs); 공식 과제 소개; 판 미확인; 발행일 미확인; 과제 소개 / DOI 해당 없음 [^n9]|원문 열람|1차; ARM·Siemens 주관 과제; 성과 자체의 독립 평가 아님|medium: 계획 확인 가능; 완료·규모·성능 미기재|
|n10: Open-RMF 개발자, Changelog for package rmf_fleet_adapter; rmf_ros2 태그 2.14.0; 2026-09-26; CHANGELOG / DOI 해당 없음 [^n10]|원문 열람|1차; n5·n6·n11과 동일 프로젝트|high: 태그 고정 변경 이력|
|n11: chart-singapore / CHART, Add GoToZone feature; rmf_ros2 PR #516; 미병합 제안; 2026-04-18(개설); 2026-10-09(확인된 최종 갱신); PR 설명·상태 / DOI 해당 없음 [^n11]|원문 열람|1차; Open-RMF 기여 프로젝트; X5·X6와 같은 작업|high: PR 상태 확인; 실물 성과·정식 배포 증거로 사용 안 함|
|n12: Coaty 프로젝트 개발자, vda-5050-lib.js — Changelog; 태그 v1.7.0; 2026-04-29; CHANGELOG / DOI 해당 없음 [^n12]|원문 열람|1차; 별도 구현 프로젝트; 규격 적합성 독립 시험은 아님|high: 고정 태그 지원 이력|
|n13: InOrbit 개발자, ROS AMR interoperability packages / massrobotics_amr_sender; 태그 1.1.1; 발행일 미확인(태그 대상 커밋 2022-10-28); README·설정 예제 / DOI 해당 없음 [^n13]|원문 열람|1차; InOrbit 계열: n16·n20과 동일|high: 설정 필드 직접 확인; 최신 지원 범위로 확대 안 함|
|n14: MassRobotics AMR Interoperability Working Group, AMR_Interop_Standard.json; 태그 1.0; 발행일 미확인; 규격 JSON 스키마 / DOI 해당 없음 [^n14]|원문 열람|1차; MassRobotics 규격 프로젝트; n13과 다른 프로젝트|high: 고정 판 스키마|
|n15: Open-RMF 개발자, Free Fleet — README; 태그 1.3.0; 발행일 미확인(태그 대상 커밋 2024-12-31); README / DOI 해당 없음 [^n15]|원문 열람|1차; Open-RMF 계열; X11은 같은 프로젝트|high: 해당 과거 태그에 한정|
|n16: InOrbit.AI, 10 Companies around the World Collaborate to Showcase Robot Orchestration at Automate 2026; 행사 시연 페이지; 판 미확인; 발행일 미확인; 벤더 공식 발표 / DOI 해당 없음 [^n16]|원문 열람|1차; InOrbit 계열; 성능 독립 검증 아님|medium: 원문 확인, 벤더의 실증 설명|
|n17: 카카오모빌리티, 카카오모빌리티, 국내 로봇 기업 협력해 ’플랫폼 기반 로봇 생태계 확장’ 지속; 공식 보도자료; 2026-03-16; 벤더 공식 발표 / DOI 해당 없음 [^n17]|원문 열람|1차; 카카오모빌리티·로보티즈 협업; 독립 운영 평가 아님|medium: 현장 명시; API·대수·기간 미기재|
|n18: Grey / Open Robotics Discourse; 발표자 shashank_br, Interop SIG, 02 July 2026: Natural-Language Control of Open-RMF Fleets via the Model Context Protocol (MCP); 세션 안내·녹화 링크; 코드 판 아님; 2026-06-25(안내); 세션 2026-07-02; 공식 커뮤니티 발표 안내 / DOI 해당 없음 [^n18]|원문 열람 — 안내문만; 영상 전체 미열람|1차; Nayantra 발표자 진술: X7·X10과 동일 작업|medium: 안내 원문 열람; 영상 전체·실물 검증 미확인|
|n19: ISO, ISO 21423 — Robotics — Industrial mobile robots — Communications and interoperability; Edition 1, 단계 60.00의 공식 카탈로그; 발행일 미확인(카탈로그 Publication date 필드 2026-10; 완료 미확인); ISO/TC 299 카탈로그 / DOI 해당 없음 [^n19]|원문 열람 — 카탈로그만; 규격 본문 미열람|1차; ISO 독립 기관; VDA와 다른 규격|high: 진행 상태의 1차 메타데이터; 규격 본문은 미열람|
|n20: InOrbit.AI, Developer Portal — Docs; 온라인 문서; 판 미확인; 발행일 미확인; 개발자 문서 / DOI 해당 없음 [^n20]|원문 열람|1차; n13·n16과 동일 업체; RMF 연동 설명은 같은 연동 생태계|medium: 구체적 API 구조 설명; 실물 성능 미확인|

### 비채택·보조 후보 12개

|후보·서지·URL|열람 상태|1차/2차·독립성|신뢰도·처리|
|---|---|---|---|
|X1: Sarah Kuehn / Idealworks, VDA 5050 3.0.0 Is Here: Three Years of Work, One Major Leap for Robotics Interoperability; 온라인 발표; 2026-03; 게재지·DOI 해당 없음. [원문](https://www.idealworks.com/de/news/vda5050-300-release-march-2026)|원문 열람|1차 벤더 발표; VDA 개발 참여자로 독립성 제한|medium: 채택일 자기 진술. 2월 17일의 협회 의결 원문 미확보. 발행일과 혼합하지 않고 보류.|
|X2: Charly_Wu·grey, Feature and limitation of traffic-light adapter; 토론 #50134; 2025-09-18~23; 포럼·DOI 해당 없음. [원문](https://discourse.openrobotics.org/t/feature-and-limitation-of-traffic-light-adapter/50134)|원문 열람|1차 개발자 설명; Open-RMF 계열|medium: 표준 지원과 맞춤 구현 구분에 유용. 설비 상세는 영역 22이므로 새 본문에서 제외.|
|X3: Muhammad Umar Farooq·Young Jae Jang, Heterogeneous multi-agent fleet control system for material handling in a Software-Defined Factory; 출판본; 2026-04; Journal of Manufacturing Systems 85, 513–530; DOI 10.1016/j.jmsy.2026.01.005. [원문](https://www.sciencedirect.com/science/article/abs/pii/S0278612526000166)|원문 미열람(초록만); 출판사 본문 접근 403|1차 연구 서지·초록만; KAIST 팀|low: 본문 근거 채택 불가. KAIST 기관 서지에서 저자·게재지 확인. 실험 규모·조건 확인 못 함.|
|X4: 저자 미확인, FORMIGA: a fleet management framework for sustainable human–robot collaboration in field robotics; 판·게재지·DOI·발행일 미확인. [원문](https://pmc.ncbi.nlm.nih.gov/articles/PMC12823971/)|열람 실패(브라우저 확인 페이지)|차수 판단 보류; 연구팀 독립성 확인 못 함|low: 검색 요약만으로 실험 조건·서지 작성하지 않음. 결론 배제.|
|X5: grey, Interop SIG, 7 May 2026: Open-RMF Upcoming Zone Feature; 공식 공지; 2026-05-04; 포럼·DOI 해당 없음. [원문](https://discourse.openrobotics.org/t/interop-sig-7-may-2026-open-rmf-upcoming-zone-feature/54490)|원문 열람|1차 발표 공지; CHART/Open-RMF, n11·X6과 같은 작업|high: 당시 검토 중임을 확인. 최신 상태 근거는 n11로 추적.|
|X6: chart-singapore, [Proposal]: Staged contributions from CHART Singapore under RMF 2.0 (Healthcare); issue #726; 2026-04-17; 제안서·DOI 해당 없음. [원문](https://github.com/open-rmf/rmf/issues/726)|원문 열람|1차 제안; n11·X5와 같은 작업|high: 단계 A와 이후 계획을 구별. 하드웨어 시험 자기 보고를 독립 성능 근거로 쓰지 않음.|
|X7: shashank_br, Nayantra – Natural Language Fleet Control via LLM + Open-RMF + MCP; 초기 공개 안내; 2026-05-15; 포럼·DOI 해당 없음. [원문](https://discourse.openrobotics.org/t/nayantra-natural-language-fleet-control-via-llm-open-rmf-mcp/54876)|원문 열람|1차 개발자 발표; n18·X10과 같은 프로젝트|medium: stub·실물·시뮬레이션 기능에 대한 저자 진술. 실물 독립 검증 아님.|
|X8: 클로봇, 통합 로봇 관제 플랫폼 크롬스[CROMS]; 판 미확인; 발행일 미확인; 제품 페이지·DOI 해당 없음. [원문](https://clobot.co.kr/croms)|열람 실패(403)|1차 벤더 제품 소개 후보; Clobot|low: 현재 페이지 원문 미확보. 기존 벤더 주장의 강도를 높이지 않음.|
|X9: 유선일, “로봇 통합 관제 기술, 인정받았다”..노바테크, 70억원 투자 유치; 기사; 2026-07-14; 머니투데이·DOI 해당 없음. [원문](https://www.mt.co.kr/industry/2026/07/14/2026071409414468672)|원문 열람|2차; 노바테크 제공 자료·발언에 의존|medium: 기존 기사 직접 확인. 재배포·동일 발표 보도는 독립 교차 확인 아님. 새 사실로 재추가하지 않음.|
|X10: shashankbr27, Nayantra — LLM-Powered Autonomous Robot Navigation; main README; 발행일 미확인; 저장소·DOI 해당 없음. [원문](https://github.com/shashankbr27/nayantra)|원문 열람|1차 README; n18·X7과 같은 프로젝트|medium: 공개 태그 API 결과가 빈 목록. 태그 고정 코드 조건을 충족하지 못해 코드 근거는 채택하지 않음.|
|X11: Open Robotics, Free Fleet Adapter — Programming Multiple Robots with ROS 2; 온라인 문서; 발행일 미확인; 기술 문서·DOI 해당 없음. [원문](https://osrf.github.io/ros2multirobotbook/integration_free_fleet_adapter.html)|원문 열람|1차; n15와 같은 프로젝트|high: Zenoh 새 구조·Nav1 제한 재확인. 기존 내용 반복은 제외. 대응 태그 확인 못 함.|
|X12: Wes Garrett, InOrbit.AI Demonstrates Live Multi-Vendor Robot Orchestration at Automate 2026; 온라인 기사; 2026-07-02; DOI 해당 없음. [원문](https://www.industrialsage.com/inorbit-robot-orchestration-automate-2026/)|원문 열람|2차; InOrbit 시연·관계자 설명 의존|medium: 8개 업체 표현 비교용. 실제 로봇 수의 독립 계수 자료로 쓰지 않음.|

X3의 [KAIST 기관 서지·초록](https://pure.kaist.ac.kr/en/publications/heterogeneous-multi-agent-fleet-control-system-for-material-handl/)은 열었으나 같은 논문의 본문 열람으로 세지 않았다. X4·X8은 실패한 페이지에서 어떤 기술 결론도 가져오지 않았다. 채택 20개와 보조 후보 12개를 합친 후보 32개 중 인용 대상 문서의 원문 열람은 29/32이다. 이는 최종 채택 출처의 20/20과 다른 집계다.

## 부록 D. 검증 기록

초안을 만든 뒤 2026-10-10에 반대 입장에서 재검토했다. 웹 문서는 다시 열고, PDF·태그 파일은 받아 둔 원문을 다시 열어 대조했다. 논문 p.21은 PDF 페이지 이미지로도 확인했다. 아래 B01~B15는 본문의 보완 항목 순서다. F 번호는 `[사실]` 문장 검증 번호다. 요약과 열린 질문에서 반복한 사실은 같은 번호를 재사용한다.

### 사실 문장별 원문 재대조

|문장|재대조한 원문 위치·짧은 구절|범위·판정|
|---|---|---|
|F01 · B01 · 릴리스 설명의 3월 19일|n2 첫 설명: “March 19th, 2026”|설명에 적힌 날짜라는 사실만 유지. 유일한 발행일 확정 아님.|
|F02 · B01 · 카탈로그 3월 17일|n4 제목 아래: “March 17, 2026”|카탈로그 표시일로 한정.|
|F03 · B01 · 보도자료 4월 20일|n3 제목 아래: “April 20, 2026”|URL 날짜와 구분. 요약·oq-005의 같은 문장도 확인.|
|F04 · B02 · 관제 API 경유 전체 제어|n5 첫 문단: “fleet manager”; B02의 경로 지정 구절과 함께 재대조. n20 Open-RMF 절의 어댑터 설명도 재열람.|연결 구조만 확인. 같은 연동 설명을 독립 재현으로 세지 않음.|
|F05 · B03 · 정지 시간 고려|n6 `moving_from()` 주석: “should only be called”; 네트워크 지연·감속에 관한 연속 주석 확인.|“요구”를 “권고”로 수정. 모든 교착 방지 보장으로 해석하지 않음.|
|F06 · B03 · 사람 개입 가능성|n6 `Blocker` 주석: “Human intervention may be required”|may의 가능성 유지. 열린 질문의 답에도 적용.|
|F07 · B04 · 단절 시 허용 노드까지 실행|n1 §4.1: “last released node”|브로커 단절 상황의 규격 설명. 단절=작업 실패로 변환하지 않도록 권고는 별도 의견.|
|F08 · B04 · 동작 상태 배열 분리|n1 §6.6.9: `actionStates`, `instantActionStates`, `zoneActionStates`|세 배열의 보고 조건을 구분. 예정 구역 동작 보고를 의무화하지 않음.|
|F09 · B05 · 120 ms 지표|n7 p.21 §6.2: “average update interval”, “approximately 120 ms”|초록과 본문 명칭 충돌을 명시. 요약에도 본문 표현 적용.|
|F10 · B05 · 실험실 규모|n7 p.12 §5.3: “approximately 500 m²”|PDF의 면적 단위 확인. 공장 설치 완료로 해석하지 않음.|
|F11 · B05 · 최대 20대 감시|n7 p.21 §6.2: “up to 20 robots”|monitoring 문맥 확인. 20대 실물 동시 주행 제어로 확대하지 않음.|
|F12 · B06 · 여섯 회사 워크숍|n8 p.4 §3.1: “six participating companies”, “spring 2023”|회사 수와 연구 방법 확인. 로봇 시험 대수로 바꾸지 않음.|
|F13 · B07 · IO-AMRs 주관|n9 Participants: “Lead: Siemens Technology”|과제 소개의 명시 정보.|
|F14 · B07 · 개발 계획|n9 Technical Approach: “will leverage”|미래 계획 문맥 확인. 기존 위키의 목표 설명과 중복되는 부분은 성과 주장으로 확장하지 않음.|
|F15 · B08 · GoToZone 제안 내용|n11 Implemented feature: “zone booking system”|공개 PR이 무엇을 제안하는지 확인. 출시된 제품 기능이란 뜻 아님.|
|F16 · B08 · 미병합 상태|n11 PR “Open”; API `merged_at: null`|2026-10-10 관측 상태. 최종 확인된 갱신일 2026-10-09와 구분. 요약에도 동일 적용.|
|F17 · B09 · 패키지 판·날짜|n10 첫 제목: “2.14.0 (2026-09-26)”|Open-RMF 전체 버전으로 쓰지 않음.|
|F18 · B09 · 플릿 상태 발행 수정|n10 2.14.0 항목의 “publish fleet state”; #525|변경 이력에 실린 수정이라는 주장만 유지.|
|F19 · B09 · 누적 지연 계산 수정|n10 2.14.0 항목의 “cumulative delay calculation”; #524|성능 개선율로 확대하지 않음. 요약의 두 수정 언급도 동일 근거.|
|F20 · B10 · 매핑 예제|n13 태그 1.1.1 설정의 `operationalState`·`errorCodes`, 각각의 `rosTopic`|실제 예제 필드 확인. 세 체계 공통 매핑이라는 추론은 배제. 열린 질문의 부분 답변에도 적용.|
|F21 · B10 · 필수 상태 필드|n14 태그 1.0 `statusReport.required`: `operationalState`|과거 고정 판의 스키마 구조에 한정.|
|F22 · B11 · CycloneDDS 구조|n15 태그 1.3.0 Message Generation: “CycloneDDS”|현재 Zenoh 문서의 구조와 분리.|
|F23 · B11 · 버전 일치 권고|n15 Prerequisites: “should be the same”|요구를 권고로 수정.|
|F24 · B12 · 라이브러리 지원 판|n12 v1.7.0 제목 날짜 “2026-04-29”; “VDA5050 V3.0 support”|규격 판과 라이브러리 판을 분리.|
|F25 · B12 · 새 토픽·검증기|n12 Features: `Topic.ZoneSet`, `Topic.Responses`, “pre-compiled validators”|명시된 추가 항목만 확인. 실물 적합성 인증 아님.|
|F26 · B15 · ISO 현재 단계|n19 Life cycle: “60.00”; “Under publication”|카탈로그 원문만 열람. 표준 본문 미열람이며 발행 완료라고 쓰지 않음.|
|F27 · B15 · MCP 안내의 실행 환경|n18 발표 예고: “Isaac Sim warehouse”|발표 안내에 명시된 환경이라는 사실만 유지. 실제 실행 성공·실물 운영 검증으로 확대하지 않음.|

표의 짧은 인용은 본문 근거 메모와 함께 읽는다. PDF의 위첨자 면적 단위는 m²로 표기했고, 코드 식별자는 번역하지 않았다. 분석·권고는 `[의견]`, 단일 벤더의 현장 주장은 `[추정]`으로 분리했다.

### 수정·유지 기록

|항목|처음 태그 → 최종 태그|바꾼 이유|
|---|---|---|
|B03 정지 시간 계약|사실 → 사실|태그 변경 없음. 원문의 should에 맞춰 “요구”를 “권고”로 고쳤다. 열린 질문의 재사용 문장도 함께 수정했다.|
|B11 CycloneDDS 버전|사실 → 사실|태그 변경 없음. should의 강도를 보존하도록 권고로 수정했다.|
|B02 독립성 집계|사실 → 사실|구조 설명은 직접 확인했지만 같은 RMF 연동의 설명이다. 독립 재검증 1개로 셀 여지를 없애고 최종 0개로 집계했다.|
|B09 두 수정 사항|사실 → 사실|한 문장에 묶인 변경 이력을 두 문장으로 나눴다.|
|B05 120 ms·실험 장소|사실 → 사실|변경 없음. 초안부터 지연/갱신 간격 충돌과 실험실 범위를 구분했다.|
|B01 날짜·n1 표지|사실 → 사실|태그 변경 없음. PDF 표지의 March 2026을 추가 확인했다. URL의 2025, 보도자료 URL의 260421을 발행일로 쓰지 않았다.|
|B08 zone 상태|사실 → 사실|변경 없음. 공개 제안·PR 상태만 쓰고 릴리스 완료로 표현하지 않았다.|
|B13 Automate·B14 호텔|추정 → 추정|변경 없음. 원문 열람을 벤더 성과의 독립 검증과 혼동하지 않았다.|
|B15 ISO·MCP|사실/의견 → 사실/의견|변경 없음. 카탈로그/규격 본문, 발표 안내/실물 실증을 각각 구별했다.|
|n7 저자 수|서지 → 서지|17명 전체이므로 표의 “Lopes 외 17명”을 “외 16명”으로 고쳤다. 전체 저자 명단과 대조했다.|
|X12 서지|서지 → 서지|재열람에서 Wes Garrett, 2026-07-02와 정확한 본문 제목을 확인해 미확인 표기를 고쳤다.|
|다른 사실 문장|사실 → 사실|변경 없음. F01~F27의 원문 구절과 위치 재확인 완료.|
|범위·중복|해당 없음|B15에서만 영역 21·47 연결을 제안했다. EPCIS·BPMN·ISA-95 매핑의 구체 내용은 작성하지 않았다. 기존 토픽·상태 목록, Nav1 제약, 과제 목표만을 새 성과처럼 반복하지 않았다.|

**최종 집계:** 보완 항목 15개 · 채택 출처 20개(영역 20 기준 신규 11개) · 채택 출처 원문 열람 20/20(100%) · 사실 검증 단위 27개 · 5단계에서 태그를 낮춘 문장 0개 · 표현 강도를 고친 문장 3개(본문 2개와 열린 질문 재사용 1개) · 독립 교차 확인 0개 · 확인 못 한 항목 11개(U1~U11).

파일·각주·인용 검사는 문서의 누락과 구조만 확인한다. 코드 실행, 실제 로봇 시험, 표준 적합성 인증은 수행하지 않았다.
