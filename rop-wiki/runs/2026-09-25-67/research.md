# 리서치 브리프 2026-09-25-67

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-67 |
| 날짜 | 2026-09-25 |
| 실행 유형 | category_link (대분류 연결) |
| 대상 영역 | 해당 없음 |
| 대분류 | F. 도입·검증·유지관리 |

## 갭(비어 있거나 약한 섹션)

- F. 도입·검증·유지관리 대분류 페이지의 '다른 대분류와의 연결' 절이 '아직 작성되지 않음' 상태
- E. 협업·현장 운영 페이지가 20. 예외 복구·재계획·업무 연속성 ↔ 22. 시뮬레이션·예측용 디지털 트윈, E ↔ 21. 온보딩·설정·현장 시운전, E ↔ 24. 자산·소프트웨어 수명주기 관리를 '근거 없음'으로 남김(이번 실행에서도 근거 미확보)
- B. 공통 정보·환경 모델 페이지가 23. 시험·형식 검증·벤치마크, 24. 자산·소프트웨어 수명주기 관리와의 연결을 '아직 다루지 않은 연결'로 둠 — 이번 실행 f11·f15 가 근거가 될 수 있음
- G. 안전·보안·지능·거버넌스 쪽 세부영역 페이지(25~28)가 seed 이거나 심화 전이라 G 연결은 F 쪽 근거에 기댐

## 조사 질문

1. 새 현장에 설치하고, 변경하면서, 오래 운영하려면? [분류원문]
2. 제조사 펌웨어가 바뀌면 어떤 현장과 기능을 다시 검증해야 할까? [분류원문]
3. 21. 온보딩·설정·현장 시운전이 등록·설정하는 정보(팩트시트, 어댑터 설정, 경로망·지도 정합)는 B. 공통 정보·환경 모델과 C. 연결·실행 기반, D. 계획·최적화의 어느 세부영역으로 넘어가는가?
4. 22. 시뮬레이션·예측용 디지털 트윈은 A. 업무·공급망 설계(처리능력·성과)와 D. 계획·최적화(배정·경로망)의 어떤 결정을 가정한 미래로 실험하며, 8. 실시간 세계 상태·데이터 일관성과 어떻게 구분되는가?
5. 23. 시험·형식 검증·벤치마크는 C. 연결·실행 기반의 인터페이스·설비 연동, D. 계획·최적화의 교착·경로 알고리즘, E. 협업·현장 운영의 장애 대응을 어떤 시험·검증으로 잇는가? (oq-055, oq-058, oq-087 관련)
6. 24. 자산·소프트웨어 수명주기 관리의 지도·펌웨어 버전과 배터리 열화 정보는 B. 공통 정보·환경 모델, C. 연결·실행 기반, D. 계획·최적화, G. 안전·보안·지능·거버넌스의 어느 규칙·제약과 맞물리는가? (oq-090, oq-091 관련)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | A. 업무·공급망 설계의 3. 처리능력·거점·설비 계획 ↔ F. 도입·검증·유지관리의 22. 시뮬레이션·예측용 디지털 트윈: RAWSim-O 는 로봇 이동형 풀필먼트 시스템(RMFS) 운영의 여러 결정 문제가 미치는 효과를 연구하기 위한 이산 사건 시뮬레이션 프레임워크다. | ref-101 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f2 | [사실] | A. 업무·공급망 설계의 4. 성과·경제성·프로세스 개선 및 D. 계획·최적화의 13. 작업 배정 — MRTA ↔ 22. 시뮬레이션·예측용 디지털 트윈: Merschformann 외(2019)의 시뮬레이션 조건에서는 피킹 주문 배정 규칙이 단위 처리량을 크게 바꾸었다. | ref-398 | 아니오 | medium | 2019 | 피킹 / 예외·성과 | 원문 미열람 |
| f3 | [추정] | 연계 대상: 22. 시뮬레이션·예측용 디지털 트윈의 성수기 시나리오 입력(주문·물동량 전망)은 A. 업무·공급망 설계의 1. 주문·업무 시스템 연계를 거쳐 상위 업무 시스템의 수요예측에서 받는 것으로 보이며, 수요예측 자체는 분류 원문 9장의 상위 업무 시스템 경계에 속한다. | ref-521 | 아니오 | low | 2024 | 피킹 / 시작 조건 | 원문 미열람 |
| f4 | [추정] | A. 업무·공급망 설계의 3. 처리능력·거점·설비 계획 ↔ 21. 온보딩·설정·현장 시운전: 다중 AGV 도입이 정밀 지도 작성·좌표 지정·수작업 경로망 설계로 오래 걸린다는 연구와 설치 기간을 6개월에서 2개월로 줄일 수 있다는 과제 측 보고가 있어, 온보딩 기간이 증차한 로봇이 처리능력으로 바뀌는 시점을 좌우하는 것으로 보인다. | ref-217, ref-265 | 아니오 | low | 2017 | 적치 / 예외·성과 | 원문 미열람 |
| f5 | [추정] | A. 업무·공급망 설계의 2. 공정·워크플로 모델링 ↔ 23. 시험·형식 검증·벤치마크: 워크플로 넷의 건전성(soundness) 판정 복잡도를 다룬 연구(2022)가 있어 공정 모델의 형식적 점검이 형식 검증과 이어질 것으로 보이나, 물류 로봇 공정 적용 사례는 확인되지 않았다. | ref-121 | 아니오 | low | 2022 | — | 원문 미열람 |
| f6 | [사실] | B. 공통 정보·환경 모델의 5. 로봇 능력·작업 온톨로지 ↔ 21. 온보딩·설정·현장 시운전: IDTA 02020 능력 기술(Capability Description) 서브모델은 공정이 요구하는 능력과 자원이 제공하는 능력을 비교하게 하고, 능력을 속성·제약(전제조건·순서)·스킬로 구조화해 자원의 매칭과 시운전을 돕는다고 설명한다. | ref-229 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f7 | [사실] | Vieira da Silva 외(2024-06)는 자연어 능력 설명에서 대규모 언어 모델(LLM)을 이용해 능력 온톨로지를 생성하는 방법을 제안했다. | ref-465 | 아니오 | medium | 2024-06 | — | 원문 미열람 |
| f8 | [추정] | G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영 ↔ 21. 온보딩·설정·현장 시운전: 분류 원문 8장 교차 규칙이 매뉴얼 해석을 5. 로봇 능력·작업 온톨로지와 21. 온보딩·설정·현장 시운전에 적용되는 AI 연구 방법으로 두므로, LLM 기반 능력 온톨로지 생성은 새 로봇 등록 작업을 줄이는 방법으로 두 대분류를 잇는 것으로 보인다. | ref-465, ref-229 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f9 | [사실] | B. 공통 정보·환경 모델의 6. 지도·공간·위치 모델 ↔ 21. 온보딩·설정·현장 시운전: Open-RMF 플릿 어댑터 튜토리얼은 로봇 좌표계와 RMF 좌표계 사이 변환을 위한 기준 좌표(대응 경유점)를 설정에 두고, 대응 경유점을 최소 4개 둘 것을 권한다. | ref-153 | 아니오 | medium | 2026-09-25 | 적치 / 수행 자원 | — |
| f10 | [사실] | 21. 온보딩·설정·현장 시운전 ↔ B. 공통 정보·환경 모델의 6. 지도·공간·위치 모델, C. 연결·실행 기반의 10. 설비·건물 시스템 연동, D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF: Open-RMF traffic-editor 는 차선·경유점·충전소·주차 지점·문·승강기·층과 기준점(fiducial)을 이용한 층간 정렬을 주석하게 하고, 주석한 그래프는 building_map_generator 로 주행 그래프로 내보내져 플릿 어댑터의 경로 계획에 쓰인다. | ref-079 | 아니오 | medium | 2026-09-25 | — | — |
| f11 | [사실] | B. 공통 정보·환경 모델의 6. 지도·공간·위치 모델 ↔ 24. 자산·소프트웨어 수명주기 관리: VDA 5050 3.0.0 은 지도 내려받기·활성화·삭제 즉시 동작(downloadMap·enableMap·deleteMap)을 두고 같은 mapId 에서는 한 번에 한 버전만 활성화하게 하며, 상태 스키마는 로봇이 mapId·mapVersion·mapStatus(ENABLED·DISABLED)를 보고하게 한다. | ref-031, ref-051 | 아니오 | medium | 2026-09-25 | 적치 / 시작 조건 | — |
| f12 | [추정] | 분류 원문이 6. 지도·공간·위치 모델에 '지도 버전 관리'를, 24. 자산·소프트웨어 수명주기 관리의 정의에 '지도 버전'을 함께 넣고 VDA 5050 이 지도 배포·활성화를 관제의 지시로 두므로, 지도 버전의 내용 정의는 B. 공통 정보·환경 모델 쪽, 배포·활성화 시점 조율과 이력 관리는 F. 도입·검증·유지관리 쪽이 맡는 분담이 될 것으로 보인다. | ref-031 | 아니오 | low | 2026-09-25 | — | — |
| f13 | [사실] | Kritzinger 외(2018)는 제조 분야 문헌을 검토해 물리 객체와 디지털 객체 사이 데이터 흐름의 자동화 정도에 따라 디지털 모델·디지털 섀도·디지털 트윈을 구분했다. | ref-291 | 아니오 | medium | 2018 | — | 원문 미열람 |
| f14 | [추정] | B. 공통 정보·환경 모델의 8. 실시간 세계 상태·데이터 일관성 ↔ 22. 시뮬레이션·예측용 디지털 트윈: 8번은 현재 상태를 표현하고 22번은 그 모델을 이용해 가정한 미래를 실험한다는 분류 원문 구분에 따라, 22번은 8번의 현재 상태(로봇·설비·배터리 상태)를 시나리오 초기값으로 받는 쪽이 될 것으로 보이며, 근거 분류 자료가 물류가 아닌 제조 대상이라는 한계가 있다. | ref-291, ref-406 | 아니오 | low | 2026-09-25 | — | — |
| f15 | [사실] | B. 공통 정보·환경 모델의 8. 실시간 세계 상태·데이터 일관성 ↔ 24. 자산·소프트웨어 수명주기 관리: VDA 5050 상태 스키마는 충전 상태(stateOfCharge), 배터리 건강 상태(batteryHealth, 0~100%), 현재 충전량으로 추정한 도달 거리(range), 충전 여부(charging)를 로봇이 보고하게 한다. | ref-051 | 아니오 | medium | 2026-09-25 | 출하 / 수행 자원 | — |
| f16 | [사실] | B. 공통 정보·환경 모델의 6. 지도·공간·위치 모델 및 C. 연결·실행 기반의 10. 설비·건물 시스템 연동 ↔ 22. 시뮬레이션·예측용 디지털 트윈: Open-RMF 시뮬레이션 문서에 따르면 building_map_generator 는 traffic-editor 로 주석한 건물 지도에서 Gazebo 시뮬레이션 세계와 주행 그래프를 만들고, 문·승강기 플러그인, 워크셀을 흉내 내는 TeleportDispenser·TeleportIngestor, 여러 플릿 어댑터의 승강기 요청을 조율하는 lift_supervisor 를 둔다. | ref-406 | 아니오 | medium | 2026-09-25 | — | — |
| f17 | [사실] | B. 공통 정보·환경 모델의 6. 지도·공간·위치 모델 ↔ 22. 시뮬레이션·예측용 디지털 트윈: Sommer 외(2023)는 건물 환경 스캔과 객체 검출을 입력으로 생산 계획용 디지털 트윈을 자동 생성하는 방법을 제시했다. | ref-241 | 아니오 | medium | 2023 | — | 원문 미열람 |
| f18 | [사실] | C. 연결·실행 기반의 9. 로봇·제조사 관제 연동 ↔ 21. 온보딩·설정·현장 시운전: VDA 5050 3.0.0 은 팩트시트를 관제에서 이동로봇 설정을 돕는 매개변수·제조사 정보로 두고, 초기 설정과 관제–이동로봇 능력 사이의 지속적인 호환성 평가에 쓰도록 한다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f19 | [사실] | VDA 5050 팩트시트 스키마는 적재 명세(loadSpecification.loadSets), 로봇 구성의 버전 목록(mobileRobotConfiguration.versions, 예: softwareVersion), 충전 설정(batteryCharging: criticalLowChargingLevel·minimumDesiredChargingLevel·maximumDesiredChargingLevel·minimumChargingTime)을 담아, 한 등록 정보가 21. 온보딩·설정·현장 시운전, 24. 자산·소프트웨어 수명주기 관리, D. 계획·최적화의 16. 공용 자원·충전·에너지 최적화에 함께 쓰인다. | ref-228 | 아니오 | medium | 2026-09-25 | — | — |
| f20 | [사실] | C. 연결·실행 기반의 9. 로봇·제조사 관제 연동 ↔ 21. 온보딩·설정·현장 시운전: Open-RMF 플릿 어댑터 설정은 최대 선·각속도와 가속도, 수행 가능한 작업 유형(loop·delivery·clean), 로봇 외곽 반경, 배터리·재충전 임계값, 제조사 관제 API 연결 정보(주소·계정)를 요구한다. | ref-153 | 아니오 | medium | 2026-09-25 | 적치 / 수행 자원 | — |
| f21 | [사실] | 22. 시뮬레이션·예측용 디지털 트윈·23. 시험·형식 검증·벤치마크 ↔ C. 연결·실행 기반의 10. 설비·건물 시스템 연동: Open-RMF 시뮬레이션 문서는 시뮬레이션 속 로봇이 배터리 소모나 충돌 비용 없이 장시간·가속 조건으로 드문 예외 상황을 시험할 수 있고, 장시간 시뮬레이션이 배치 전 시설 소유자의 확신을 높인다고 설명한다. | ref-406 | 아니오 | medium | 2026-09-25 | — | — |
| f22 | [사실] | C. 연결·실행 기반의 9. 로봇·제조사 관제 연동 ↔ 22. 시뮬레이션·예측용 디지털 트윈: Open-RMF 시뮬레이션의 slotcar 플러그인은 경로·모드 요청을 받아 레일식으로 움직이고 센서 기반 주행 스택 없이 로봇 상태를 발행하는 전체 제어(full control) 로봇 모델이다. | ref-406 | 아니오 | medium | 2026-09-25 | — | — |
| f23 | [추정] | slotcar 같은 단순화 모델은 제조사 관제·로봇 고유 거동을 재현하지 않으므로, 9. 로봇·제조사 관제 연동 방식(전체 제어·신호등·읽기 전용)과 제조사별 거동 차이가 22. 시뮬레이션·예측용 디지털 트윈의 처리량 예측 오차 원인이 될 것으로 보인다(oq-086). | ref-406 | 아니오 | low | 2026-09-25 | — | — |
| f24 | [사실] | C. 연결·실행 기반의 9. 로봇·제조사 관제 연동 ↔ 24. 자산·소프트웨어 수명주기 관리: VDA 5050 3.0.0 은 로봇이 사용할 수 없는 선택 필드가 담긴 주문을 받으면 UNSUPPORTED_PARAMETER 오류를 CRITICAL 수준과 오류 필드 참조로 보고하게 한다. | ref-031 | 아니오 | medium | 2026-09-25 | 적치 / 예외·성과 | — |
| f25 | [사실] | C. 연결·실행 기반의 12. 명령·작업 실행의 신뢰성 ↔ 24. 자산·소프트웨어 수명주기 관리: ROS 2 관리형 노드는 Unconfigured·Inactive·Active·Finalized 상태와 configure·activate 같은 전이를 두어, 감독 도구가 구성요소 준비를 확인한 뒤 실행을 허용하게 한다. | ref-364 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f26 | [사실] | C. 연결·실행 기반의 9. 로봇·제조사 관제 연동·12. 명령·작업 실행의 신뢰성 ↔ 23. 시험·형식 검증·벤치마크: 공개 개인 프로젝트 vda5050-sim 은 VDA 5050 3.0.0 주문 수명주기·동작·교통 제어 의미를 명세와 대조하는 적합성 시험 묶음과 고장 주입을, vda5050-lab 은 MQTT 기록에서 반복 주문 id·재연결·취소 불일치를 진단한다고 README 에 적으며, 둘 다 VDA·VDMA 공식 적합성 시험이 아니다. | ref-407, ref-408 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f27 | [추정] | OTTO by Rockwell Automation 은 자사 AMR 이 여러 관제 업체와 VDA 5050 인증을 마쳤다고 2026-04 발표했으나, 인증의 시험 항목은 확인되지 않았다. | ref-608 | 아니오 | low | 2026-04 | — | 원문 미열람, 벤더 주장 |
| f28 | [추정] | 연계 대상: ros2_fault_injection 은 오도메트리·레이저 스캔·IMU·점군 같은 센서 신호와 속도 명령을 조작하는 로봇 수준 장애 주입 도구이며, 23. 시험·형식 검증·벤치마크에서 ROP 쪽 장애 주입은 같은 프록시 방식을 C. 연결·실행 기반의 관제 명령·상태 메시지와 설비 응답 수준에 적용하는 형태가 될 것으로 보인다. | ref-601 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f29 | [사실] | D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF ↔ 22. 시뮬레이션·예측용 디지털 트윈: 다중 AGV 시스템의 경로망(roadmap)을 시뮬레이션 기반으로 자동 설계하는 연구(IEEE T-ASE 2024)가 있다. | ref-267 | 아니오 | medium | 2024 | — | 원문 미열람 |
| f30 | [사실] | D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF ↔ 23. 시험·형식 검증·벤치마크: Stern 외(2019)는 MAPF 의 가정·목적함수를 공통 용어로 정리하고 격자 기반 벤치마크를 소개했으나, 그 성과가 실제 물류센터 처리량으로 얼마나 이어지는지는 확인되지 않았다(oq-058). | ref-186 | 아니오 | medium | 2019-06 | — | 원문 미열람 |
| f31 | [사실] | Yan 외(2026-02)는 기존 MAPF 연구가 단순한 운동 모델과 완전한 실행·통신을 가정한다고 지적하고, 플릿 관리 시스템 안에서 계획 시점·방법·복구 설계 선택을 비교하는 시험대(LSMART)를 제안해 D. 계획·최적화의 경로 알고리즘과 23. 시험·형식 검증·벤치마크를 잇는다. | ref-604 | 아니오 | medium | 2026-02-17 | — | 원문 미열람 |
| f32 | [사실] | von Berg 외(2026-05)는 창고 물류 AGV 의 교착 회피를 전이 시스템 인코딩과 BDD 로 분석한 사례 연구를 발표해, 15. 다중 로봇 경로·교통 관리 — MAPF 의 교착 문제가 23. 시험·형식 검증·벤치마크의 형식 검증 대상이 됨을 보인다(계산 규모 한계는 oq-088). | ref-609 | 아니오 | medium | 2026-05 | — | 원문 미열람 |
| f33 | [사실] | D. 계획·최적화의 13. 작업 배정 — MRTA ↔ 23. 시험·형식 검증·벤치마크: Lott·Honary(2026-09 프리프린트)는 분산 작업 배정기 6종을 패킷 손실·페이딩 같은 통신 저하 조건에서 이동 거리·안정성·계산 부담으로 비교하는 벤치마크를 제시했다. | ref-493 | 아니오 | medium | 2026-09 | — | 원문 미열람 |
| f34 | [사실] | D. 계획·최적화의 16. 공용 자원·충전·에너지 최적화 ↔ 24. 자산·소프트웨어 수명주기 관리: 플릿 수준에서 배터리 건강(열화)을 고려해 자율이동로봇의 작업 배정·충전 일정을 정하는 연구(2026-03, 프리프린트)가 있다. | ref-403 | 아니오 | medium | 2026-03 | — | 원문 미열람 |
| f35 | [추정] | 로봇이 보고하는 batteryHealth 가 낮아지면 같은 충전 상태에서도 도달 거리(range)가 짧아질 수 있어, 24. 자산·소프트웨어 수명주기 관리의 배터리 열화 정보가 D. 계획·최적화의 13. 작업 배정 — MRTA·16. 공용 자원·충전·에너지 최적화의 제약 입력이 되는 것으로 보인다(물류센터 실측 자료 미확인). | ref-051, ref-403 | 아니오 | low | 2026-09-25 | 출하 / 제약 | — |
| f36 | [사실] | E. 협업·현장 운영의 20. 예외 복구·재계획·업무 연속성 ↔ 23. 시험·형식 검증·벤치마크: NIST ARIAC 2025 문서는 컨베이어 고장, 전압 시험기 고장, 진공 그리퍼 파지 실패, 긴급(고우선) 주문을 과제로 두어 설비·로봇 장애와 긴급 주문 대응을 평가한다. | ref-528 | 아니오 | medium | 2026-09-25 | 예외·성과 | — |
| f37 | [추정] | ARIAC 같은 장애 과제 정의와 장애 주입 도구를 결합하면, 20. 예외 복구·재계획·업무 연속성의 재배정·수동 전환·제한 운영 동작을 업데이트마다 다시 돌리는 회귀 시험 시나리오로 만들 수 있을 것으로 보이나, 물류 오케스트레이션에 적용해 공개한 사례는 확인되지 않았다(oq-087). | ref-528, ref-601 | 아니오 | low | 2026-09-25 | 피킹 / 예외·성과 | — |
| f38 | [사실] | E. 협업·현장 운영의 17. 로봇 간 협업·물리적 인계 ↔ 23. 시험·형식 검증·벤치마크: ASTM F3499-21 은 자율 무인 지상 차량(A-UGV)의 도킹 성능을 확인하는 시험 방법이며, 그 결과를 로봇팔 파지 허용 오차와 잇는 기준은 확인되지 않았다(oq-063). | ref-204 | 아니오 | medium | 2021 | 완료·인계 | 원문 미열람 |
| f39 | [사실] | E. 협업·현장 운영의 19. 모니터링·이상 탐지·원인 분석 ↔ 24. 자산·소프트웨어 수명주기 관리: Lei 외(2025)는 산업용 로봇의 고장 모드·데이터 수집·모델 기반과 데이터 기반 진단을 상태 기반 정비 관점에서 정리한 검토를 발표했다. | ref-553 | 아니오 | medium | 2025 | — | 원문 미열람 |
| f40 | [사실] | E. 협업·현장 운영의 19. 모니터링·이상 탐지·원인 분석 ↔ 23. 시험·형식 검증·벤치마크: ROSMonitoring 은 ROS 시스템의 런타임 검증 프레임워크로, 운영 중 감시가 사전 시험을 보완하는 연결 지점이 된다. | ref-602 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f41 | [사실] | G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ 21. 온보딩·설정·현장 시운전·23. 시험·형식 검증·벤치마크: ISO 3691-4:2023 은 AGV·AMR 을 포함한 무인 산업 차량과 그 시스템의 안전 요구와 검증 수단을 정하며, 운용 구역 준비를 부속서 A 에 둔다. | ref-470 | 아니오 | medium | 2023-06 | 적치 / 제약 | 원문 미열람 |
| f42 | [추정] | 연계 대상: 국내에는 바퀴형 서비스 로봇의 이동 성능 시험방법 KS B ISO 18646-1 과 한국로봇산업진흥원의 시험평가 서비스가 있어, 로봇 자체 성능 시험은 시험기관 쪽이고 23. 시험·형식 검증·벤치마크의 ROP 몫은 그 결과를 등록·배정 조건으로 받는 쪽으로 보인다(oq-089). | ref-606, ref-607 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f43 | [추정] | 한국산업기술시험원(KTL)과 통합물류협회가 물류로봇 시험인증 협력을 강화하기로 했다고 2026-07 보도되어, 국내 물류로봇 시험·인증 체계가 23. 시험·형식 검증·벤치마크와 28. 표준·상호운용성·다사업자 거버넌스를 잇는 후보가 될 것으로 보인다. | ref-466 | 아니오 | low | 2026-07-24 | — | 원문 미열람 |
| f44 | [사실] | G. 안전·보안·지능·거버넌스의 26. 사이버보안·접근권한·개인정보 ↔ 24. 자산·소프트웨어 수명주기 관리: IEC TR 62443-2-3:2015 는 산업 자동화·제어 시스템(IACS) 환경의 패치 관리를 다루는 기술 보고서다. | ref-554 | 아니오 | medium | 2015-06 | — | 원문 미열람 |
| f45 | [추정] | G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ 24. 자산·소프트웨어 수명주기 관리: 로봇 시스템 위험성평가 가이드는 설비·작업 변경 시 위험성평가를 다시 하도록 권하므로, 펌웨어·안전 파라미터·오케스트레이션 정책 변경이 재평가 촉발 조건이 될 수 있어 보이나, 국내 공식 규정은 미확인이다(oq-092, oq-093). | ref-559 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f46 | [사실] | G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영 ↔ 23. 시험·형식 검증·벤치마크: ALFRED 와 LoTa-Bench 는 자연어 지시를 행동 계획으로 바꾸는 체화 에이전트를 시뮬레이터 결과(목표 조건·성공률)로 자동 평가하는 공개 벤치마크다. | ref-539, ref-541 | 아니오 | medium | 2024-02 | — | 원문 미열람 |
| f47 | [사실] | G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스 ↔ 22. 시뮬레이션·예측용 디지털 트윈: 제조용 디지털 트윈 프레임워크 ISO 23247 은 국내에 KS X ISO 23247-1 로 등재되어 있고, 2026 년 디지털 트윈 결합을 다루는 Part 6 이 발행되었으나 물류센터 적용 여부는 미확인이다(oq-085). | ref-516, ref-518 | 아니오 | medium | 2026 | — | 원문 미열람 |
| f48 | [추정] | 이번에 확인한 VDA 5050 적합성 시험 근거가 제3자 오픈소스 도구와 벤더 발표뿐이라, 어느 시험 결과를 새 로봇 연동 승인 기준으로 쓰고 판 차이(2.x·3.0.0)로 생기는 UNSUPPORTED_PARAMETER 같은 미지원 오류를 누가 판정·수정할지가 23. 시험·형식 검증·벤치마크·24. 자산·소프트웨어 수명주기 관리에서 28. 표준·상호운용성·다사업자 거버넌스로 넘어가는 과제가 될 것으로 보인다(oq-055, oq-091). | ref-407, ref-408, ref-608, ref-031 | 아니오 | low | 2026-09-25 | — | — |

### 근거 발췌

- **f1**: RAWSim-O README: RMFS 의 결정 문제 효과를 연구하는 이산 사건 시뮬레이션 프레임워크 (재인용: 22. 시뮬레이션·예측용 디지털 트윈 페이지 7절·A 대분류 페이지) (발행일 미확인, 확인일 기준)
- **f2**: RMFS 결정 규칙 시뮬레이션 연구에서 피킹 주문 배정 규칙이 단위 처리량에 큰 영향(모델·시뮬레이션 조건의 저자 보고) (재인용: 2026-09-25-56)
- **f3**: Le·Fan(2024)은 물류·공급망 디지털 트윈 개념 틀을 제안하고 실데이터 검증 논문이 소수라고 보고 (재인용: 2026-09-25-56)
- **f4**: Beinschob 외(2017) 도입 지연 원인 / PAN-Robots 설치 기간 6→2개월은 과제 측 보고값, 비교 조건 미확인 (재인용: 2026-09-25-52)
- **f5**: Blondin 외, The complexity of soundness in workflow nets (LICS 2022) (재인용: 2026-09-25-29, A 대분류 페이지)
- **f6**: README: capability 는 'implementation-independent specification of a function in industrial production'; 요구·제공 능력 비교, properties·constraints·skills 구조
- **f7**: Toward a Method to Generate Capability Ontologies from Natural Language Descriptions (arXiv 2406.07962) (재인용: 2026-09-25-52)
- **f8**: 교차 규칙(분류 원문 8장)과 f6·f7 의 결합에 따른 이 위키의 추론. 온보딩 현장 적용 사례는 미확인
- **f9**: "A minimum of 4 matching waypoints is recommended."
- **f10**: 원문: annotated Graphs are exported as navigation graphs using the building_map_generator, used by rmf_fleet_adapters for path planning
- **f11**: "There shall only be one version of maps with the same mapId enabled at a time" / state.schema maps: mapId, mapVersion, mapStatus(ENABLED, DISABLED)
- **f12**: 분류 원문 6번 주석·24번 한 줄 정의와 VDA 5050 지도 배포 즉시 동작에서 끌어낸 이 위키의 추론
- **f13**: Digital Twin in manufacturing: A categorical literature review and classification (IFAC 2018) — 제조 대상 분류 (재인용: 2026-09-25-32)
- **f14**: 분류 원문 7장 구분 + 제조 대상 디지털 섀도·트윈 구분 + Open-RMF 시뮬레이션 문서에서 끌어낸 추론
- **f15**: state.schema batteryState: stateOfCharge, batteryHealth, range('Estimated reach with current State of Charge in meter'), charging
- **f16**: simulation.md: building_map_generator 가 .building.yaml 에서 월드·주행 그래프 생성; door·lift 플러그인, TeleportDispenser/TeleportIngestor, lift supervisor
- **f17**: Automated generation of digital twin for a built environment using scan and object detection as input for production planning (2023) — 생산 계획 대상 (재인용: 2026-09-25-56)
- **f18**: "Factsheet shall be used to support initial configuration and ongoing compatibility assessment between fleet control and mobile robot capabilities."
- **f19**: factsheet.schema: loadSpecification.loadSets, mobileRobotConfiguration.versions(softwareVersion 등), mobileRobotConfiguration.batteryCharging.criticalLowChargingLevel 외
- **f20**: integration_fleets_adapter_tutorial.md: speed limits, task capabilities, robot profiles, battery params, recharge thresholds, fleet manager prefix/username/password
- **f21**: "Long running simulations can instill confidence in facility owners prior to deployment."
- **f22**: simulation.md: slotcar 는 rail-like navigation 으로 full control 로봇을 모사, 센서 기반 주행 스택 불필요
- **f23**: f22 의 단순화 모델 설명에서 끌어낸 추론. 오차 크기 자료 미확인
- **f24**: "The mobile robot shall report an error of type 'UNSUPPORTED_PARAMETER' with level 'CRITICAL'"
- **f25**: ROS 2 Design node_lifecycle: managed node 상태 기계 (재인용: 2026-09-25-38, C 대분류 페이지)
- **f26**: 두 README 의 자기 기술 (재인용: 2026-09-25-38, C 대분류 페이지)
- **f27**: 벤더 주장: Idealworks·NAiSE·SYNAOS 와 VDA 5050 인증 완료 발표 (재인용: 2026-09-25-59)
- **f28**: README 기준 센서 신호 장애 주입과 Twist 명령 조작 (재인용: 2026-09-25-59). ROP 적용은 추론
- **f29**: Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (재인용: 2026-09-25-56)
- **f30**: Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks (2019) (재인용: 2026-09-25-59)
- **f31**: LSMART 와 지속형 AGV 플릿 관리 설계 선택 연구(arXiv 2602.15721, 프리프린트) (재인용: 2026-09-25-59)
- **f32**: BDD-Based Deadlock Avoidance for AGVs in Warehouse Logistics (FM 2026 사례 연구) (재인용: 2026-09-25-59)
- **f33**: Decentralized Multi-Robot Task Allocation Under Degraded Communication: A Benchmark (재인용: 2026-09-25-55, D 대분류 페이지)
- **f34**: Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots (arXiv 2603.22731) (재인용: 2026-09-25-61)
- **f35**: f15 의 상태 필드와 f34 의 연구에서 끌어낸 추론 (재인용: 2026-09-25-61 출하 시나리오)
- **f36**: "A specified vacuum gripper will fail during grasp attempts." (challenges.rst, ARIAC 2025 기준)
- **f37**: f36·f28 에서 끌어낸 추론 (재인용: 2026-09-25-59 피킹 회귀 시험 시나리오)
- **f38**: Standard Test Method for Confirming the Docking Performance of A-UGVs (2021) (재인용: 2026-09-25-60, E 대분류 페이지)
- **f39**: Condition monitoring and fault diagnosis of industrial robots: A review (Sci China Tech Sci 68, 2025) (재인용: 2026-09-25-61)
- **f40**: ROSMonitoring: a Runtime Verification Framework for ROS — README (재인용: 2026-09-25-59)
- **f41**: ISO 3691-4:2023 소개 (재인용: 2026-09-25-52·59·63). 세부 시험 항목 미확인
- **f42**: KSSN 표준 정보와 KIRIA 시험평가 페이지 (재인용: 2026-09-25-59). 오케스트레이션 수준 시험 포함 여부 미확인
- **f43**: 부산일보 2026-07-24 기사(1차 출처 미확인) (재인용: 2026-09-25-52)
- **f44**: IEC TR 62443-2-3:2015 Patch management in the IACS environment (재인용: 2026-09-25-61)
- **f45**: 세이프틱스 위험성평가 가이드(업체 자료, 발행일 미확인) (재인용: 2026-09-25-61) (발행일 미확인, 확인일 기준)
- **f46**: ALFRED(AI2-THOR 가정 작업), LoTa-Bench(ICLR 2024, 성공률 비교) (재인용: 2026-09-25-62). 물류 지시 데이터셋은 아님
- **f47**: KSSN KS X ISO 23247-1, ISO 23247-6:2026 Digital twin composition (재인용: 2026-09-25-56)
- **f48**: f24·f26·f27 에서 끌어낸 추론. VDA 공식 인증 절차 부재는 확정 사실 아님

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 아니오 |
| ref-079 | Open Robotics | Traffic Editor - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/traffic-editor.html | 아니오 |
| ref-101 | Merschformann, M. (RAWSim-O GitHub) | RAWSim-O: A simulation framework for Robotic Mobile Fulfillment Systems (README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/merschformann/RAWSim-O | 예 |
| ref-121 | Blondin, M., Mazowiecki, F., & Offtermatt, P. (LICS 2022) | The complexity of soundness in workflow nets | 2022 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2201.05588 | 예 |
| ref-153 | Open Robotics | Fleet Adapter Tutorial - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html | 아니오 |
| ref-186 | Stern, R., Sturtevant, N. R., Felner, A., Koenig, S. 외 | Multi-Agent Pathfinding: Definitions, Variants, and Benchmarks | 2019-06 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/1906.08291 | 예 |
| ref-204 | ASTM International | Standard Test Method for Confirming the Docking Performance of A-UGVs (ASTM F3499-21) | 2021 | 표준 | medium | 2026-09-25 | https://www.astm.org/f3499-21.html | 예 |
| ref-217 | Beinschob, P., Meyer, M., Reinke, C., Digani, V., Secchi, C., & Sabattini, L. | Semi-automated map creation for fast deployment of AGV fleets in modern logistics | 2017 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0921889015302724 | 예 |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema | 아니오 |
| ref-229 | IDTA(Industrial Digital Twin Association) | IDTA 02020 Capability Description 1.0 — README (admin-shell-io/submodel-templates) | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description | 예 |
| ref-241 | Sommer, M., Stjepandić, J., Stobrawa, S., & von Soden, M. | Automated generation of digital twin for a built environment using scan and object detection as input for production planning | 2023 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S2452414X23000353 | 예 |
| ref-265 | European Commission (CORDIS) | PAN-ROBOTS: Automating logistics for the factory of the future | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://cordis.europa.eu/article/id/160857-panrobots-automating-logistics-for-the-factory-of-the-future | 예 |
| ref-267 | IEEE 게재 논문 저자(미확인) | Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)) | 2024 | 논문 | medium | 2026-09-25 | https://ieeexplore.ieee.org/document/10287275/ | 예 |
| ref-291 | Kritzinger, W., Karner, M., Traar, G., Henjes, J., & Sihn, W. | Digital Twin in manufacturing: A categorical literature review and classification | 2018 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/pii/S2405896318316021 | 예 |
| ref-364 | ROS 2 Design | Managed nodes (ROS 2 Design: node_lifecycle) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://design.ros2.org/articles/node_lifecycle.html | 예 |
| ref-398 | Merschformann, M., Lamballais, T., de Koster, R., & Suhl, L. | Decision rules for robotic mobile fulfillment systems | 2019 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/pii/S2214716019300946 | 예 |
| ref-403 | Li, J., Li, S., Chu, J., Li, W., & Chen, D.(UT Austin) | Fleet-Level Battery-Health-Aware Scheduling for Autonomous Mobile Robots | 2026-03 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2603.22731 | 예 |
| ref-406 | Open Robotics | Simulation - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/simulation.html | 아니오 |
| ref-407 | gpue (GitHub) | vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/gpue/vda5050-sim | 예 |
| ref-408 | ekusiadadus (GitHub) | vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/ekusiadadus/vda5050-lab | 예 |
| ref-465 | Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A. | Toward a Method to Generate Capability Ontologies from Natural Language Descriptions | 2024-06 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2406.07962 | 예 |
| ref-466 | 부산일보 | KTL·통합물류협회 ‘물류로봇 시험인증’ 협력 강화 ‘맞손’ | 2026-07-24 | 기사 | low | 2026-09-25 | https://www.busan.com/view/busan/view.php?code=2026072420194685883 | 예 |
| ref-470 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 2023-06 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/83545.html | 예 |
| ref-493 | Lott, J., & Honary, V.(University of San Diego) | Decentralized Multi-Robot Task Allocation Under Degraded Communication: A Benchmark of Performance, Reliability, and Computation | 2026-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2609.13711 | 예 |
| ref-516 | 한국표준협회 KSSN(국가표준인증종합정보센터) | KS X ISO 23247-1 자동화 시스템 및 통합 — 제조를 위한 디지털 트윈 프레임워크 — 제1부: 개요 및 일반 원리 | 미확인 | 표준 | medium | 2026-09-25 | https://www.kssn.net/search/stddetail.do?itemNo=K001010140724 | 예 |
| ref-518 | ISO | ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition | 2026 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/87426.html | 예 |
| ref-521 | Le, T. V., & Fan, R. | Digital twins for logistics and supply chain systems: Literature review, conceptual framework, research potential, and practical challenges | 2024 | 논문 | medium | 2026-09-25 | https://www.sciencedirect.com/science/article/abs/pii/S0360835223007921 | 예 |
| ref-528 | NIST (usnistgov/ARIAC_docs) | ARIAC 2025 Documentation — Challenges | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://pages.nist.gov/ARIAC_docs/en/latest/pages/challenges.html | 아니오 |
| ref-539 | askforalfred (ALFRED 공식 저장소) | ALFRED — A Benchmark for Interpreting Grounded Instructions for Everyday Tasks (GitHub README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/askforalfred/alfred | 예 |
| ref-541 | lbaa2022 (LoTa-Bench 공식 저장소) | LLMTaskPlanning — LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents (ICLR 2024) (GitHub README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/lbaa2022/LLMTaskPlanning | 예 |
| ref-553 | Lei, Y., Liu, H., Li, N. 외 | Condition monitoring and fault diagnosis of industrial robots: A review (Science China Technological Sciences 68, 1110301) | 2025 | 논문 | medium | 2026-09-25 | https://link.springer.com/article/10.1007/s11431-024-2810-2 | 예 |
| ref-554 | IEC | IEC TR 62443-2-3:2015 Security for industrial automation and control systems - Part 2-3: Patch management in the IACS environment | 2015-06 | 표준 | medium | 2026-09-25 | https://webstore.iec.ch/en/publication/22811 | 예 |
| ref-559 | 세이프틱스(Safetics) | 로봇 시스템 위험성평가 가이드 | 미확인 | 벤더 문서 | low | 2026-09-25 | https://doc.safetics.io/insight-risk-assessment/ | 예 |
| ref-601 | reeceholland (ros2_fault_injection GitHub) | ros2_fault_injection — README | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/reeceholland/ros2_fault_injection | 예 |
| ref-602 | University of Liverpool Autonomy and Verification (ROSMonitoring GitHub) | ROSMonitoring: a Runtime Verification Framework for ROS — README | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/autonomy-and-verification-uol/ROSMonitoring | 예 |
| ref-604 | Yan, J., Zhang, Y., Liu, Z., Zhang, H., Jiang, H., Chen, J., Smith, S. F., & Li, J. | Lifelong Scalable Multi-Agent Realistic Testbed and A Comprehensive Study on Design Choices in Lifelong AGV Fleet Management Systems | 2026-02-17 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2602.15721 | 예 |
| ref-606 | 한국표준협회 KSSN(국가표준인증종합정보센터) | KS B ISO 18646-1 로봇 — 서비스 로봇의 성능 기준 및 관련 시험방법 — 제1부 : 바퀴형 로봇의 이동능력 | 미확인 | 표준 | medium | 2026-09-25 | https://www.kssn.net/search/stddetail.do?itemNo=K001010113281 | 예 |
| ref-607 | 한국로봇산업진흥원(KIRIA) | 시험평가 \| KIRIA 첨단로봇 실증지원 디지털 플랫폼 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://kiria.org/rp/kiria/tva/inr/page.dn | 예 |
| ref-608 | OTTO by Rockwell Automation | OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments | 2026-04 | 벤더 문서 | low | 2026-09-25 | https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/ | 예 |
| ref-609 | von Berg, B., Aichernig, B. K., & Wedenik, F. | BDD-Based Deadlock Avoidance for Automated Guided Vehicles in Warehouse Logistics (Case Study Paper) | 2026-05 | 논문 | medium | 2026-09-25 | https://link.springer.com/chapter/10.1007/978-3-032-26204-2_16 | 예 |

### 출처 요약

- **ref-031**: VDA 5050 3.0.0 명세 원문. 팩트시트 용도, 지도 배포 즉시 동작, UNSUPPORTED_PARAMETER, 범위 제외(안전·교통 전략·외부 IT 인터페이스)를 확인.
- **ref-051**: 상태 메시지 JSON 스키마. maps(mapId·mapVersion·mapStatus), batteryState(stateOfCharge·batteryHealth·range·charging), 오류 수준, 운용 모드 확인.
- **ref-079**: traffic-editor 로 차선·경유점·충전소·주차·문·승강기·층 정렬을 주석하고 주행 그래프로 내보내는 흐름.
- **ref-101**: 원문 미열람. RMFS 결정 문제 효과를 연구하는 이산 사건 시뮬레이션 프레임워크.
- **ref-121**: 원문 미열람. 워크플로 넷 건전성 판정의 계산 복잡도 연구.
- **ref-153**: 플릿 어댑터 설정 항목(속도 한계·작업 유형·기준 좌표·관제 연결·배터리)과 대응 경유점 4개 이상 권장.
- **ref-186**: 원문 미열람. MAPF 정의·변형·격자 벤치마크 정리.
- **ref-204**: 원문 미열람. A-UGV 도킹 성능 확인 시험 방법.
- **ref-217**: 원문 미열람. AGV 플릿 신속 배치를 위한 반자동 지도 작성과 도입 지연 원인.
- **ref-228**: 팩트시트 JSON 스키마. loadSets, mobileRobotConfiguration.versions, batteryCharging 필드 확인.
- **ref-229**: 능력 기술 서브모델 README. 요구·제공 능력 비교와 속성·제약·스킬 구조.
- **ref-241**: 원문 미열람. 스캔·객체 검출로 건물 환경 디지털 트윈 자동 생성.
- **ref-265**: 원문 미열람. EU 과제 소개, 설치 기간 단축 보고(과제 측).
- **ref-267**: 원문 미열람. 시뮬레이션 기반 다중 AGV 경로망 자동 설계.
- **ref-291**: 원문 미열람. 제조 분야 디지털 모델·섀도·트윈 구분.
- **ref-364**: 원문 미열람. ROS 2 관리형 노드 상태 기계.
- **ref-398**: 원문 미열람. RMFS 결정 규칙의 시뮬레이션 비교.
- **ref-403**: 원문 미열람. 플릿 배터리 열화를 고려한 AMR 스케줄링(프리프린트).
- **ref-406**: Open-RMF 시뮬레이션: 배치 전 시험 이점, 월드 생성, 문·승강기·워크셀 플러그인, lift_supervisor, slotcar 모델.
- **ref-407**: 원문 미열람. VDA 5050 3.0.0 플릿 시뮬레이터, 적합성 시험 묶음·고장 주입(개인 프로젝트).
- **ref-408**: 원문 미열람. MQTT 기록 기반 VDA 5050 주문·재연결·취소 진단 도구(개인 프로젝트).
- **ref-465**: 원문 미열람. 자연어 설명에서 LLM 으로 능력 온톨로지 생성.
- **ref-466**: 원문 미열람. 국내 물류로봇 시험인증 협력 보도.
- **ref-470**: 원문 미열람. 무인 산업 차량과 시스템의 안전 요구·검증.
- **ref-493**: 원문 미열람. 통신 저하 조건의 분산 배정기 벤치마크(프리프린트).
- **ref-516**: 원문 미열람. 제조 디지털 트윈 프레임워크 국내 부합 표준.
- **ref-518**: 원문 미열람. 디지털 트윈 결합을 다루는 ISO 23247 Part 6.
- **ref-521**: 원문 미열람. 물류·공급망 디지털 트윈 검토와 개념 틀.
- **ref-528**: ARIAC 2025 과제: 컨베이어·전압 시험기·진공 그리퍼 고장, 긴급 주문.
- **ref-539**: 원문 미열람. 자연어 지시를 가정 작업 행동 순서로 대응시키는 벤치마크.
- **ref-541**: 원문 미열람. 언어 기반 작업 계획기의 자동 정량 평가 벤치마크.
- **ref-553**: 원문 미열람. 산업용 로봇 상태 감시·고장 진단 검토.
- **ref-554**: 원문 미열람. IACS 환경 패치 관리 기술 보고서.
- **ref-559**: 원문 미열람. 로봇 시스템 위험성평가 절차 안내(업체 자료).
- **ref-601**: 원문 미열람. ROS 2 센서 신호·속도 명령 장애 주입 도구.
- **ref-602**: 원문 미열람. ROS 런타임 검증 프레임워크.
- **ref-604**: 원문 미열람. FMS 안의 지속형 MAPF 시험대와 설계 선택 연구.
- **ref-606**: 원문 미열람. 바퀴형 서비스 로봇 이동 성능 시험방법 KS.
- **ref-607**: 원문 미열람. 한국로봇산업진흥원 로봇 시험평가 안내.
- **ref-608**: 원문 미열람. OTTO AMR 의 VDA 5050 인증 발표(벤더 보도자료).
- **ref-609**: 원문 미열람. 창고 AGV 교착 회피의 BDD 기반 사례 연구.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/f-deployment-verification-and-maintenance/index.md | 5. 다른 대분류와의 연결 | '다른 대분류와의 연결' 절만 patches 로 채운다. A. 업무·공급망 설계: f1·f2(22↔3·4), f3(22↔1, 연계 대상), f4(21↔3), f5(23↔2) / B. 공통 정보·환경 모델: f6·f7(21↔5), f9·f10(21↔6), f11·f12(24↔6 지도 버전), f13·f14(22↔8, 8·22 구분 유지), f15(24↔8), f16·f17(22↔6) / C. 연결·실행 기반: f18·f19·f20(21↔9), f10(21↔10), f16·f21(22·23↔10), f22·f23(22↔9, oq-086), f24(24↔9), f25(24↔12), f26·f27(23↔9·12, f27 벤더 주장 병기), f28(23↔12, 연계 대상) / D. 계획·최적화: f2(22↔13), f29(22↔15), f10(21↔15), f30·f31·f32(23↔15), f33(23↔13), f19·f34·f35(24↔13·16) / E. 협업·현장 운영: f36·f37(23↔20), f38(23↔17), f39(24↔19), f40(23↔19) / G. 안전·보안·지능·거버넌스: f41(21·23↔25), f42·f43(23↔28, 연계 대상), f44(24↔26), f45(24↔25), f8·f46(21·23↔27, 교차 규칙), f47(22↔28), f48(23·24↔28) / '아직 다루지 않은 연결': 20. 예외 복구·재계획·업무 연속성 ↔ 22. 시뮬레이션·예측용 디지털 트윈(oq-081), 21. 온보딩·설정·현장 시운전 ↔ E. 협업·현장 운영, 22 ↔ 26. 사이버보안·접근권한·개인정보, 11. 분산 시스템·통신·컴퓨팅 구조, 7. 화물·재고·자산 식별과 추적과의 연결은 근거 미확보. 다음 실행 후보: B. 공통 정보·환경 모델 페이지의 '아직 다루지 않은 연결'(23·24)을 f11·f15 로 보강. |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- Open-RMF 시뮬레이션의 lift_supervisor 처럼 여러 플릿의 승강기·문 요청 조율을 시뮬레이션에서 검증한 결과를 실제 설비 연동 시운전의 합격 기준으로 쓸 수 있는가, 쓴다면 시뮬레이션과 현장의 차이를 어떻게 확인하는가? | 관련 영역: 22. 시뮬레이션·예측용 디지털 트윈, 23. 시험·형식 검증·벤치마크, 10. 설비·건물 시스템 연동, 21. 온보딩·설정·현장 시운전 | 근거: f16 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 38 · 교차 확인: 0
- 예산 사용량: 검색 1회 · 신규 출처 0건
- 미확인 항목:
    - 모든 finding 교차 확인 없음(단일 출처이거나 같은 기관 출처 쌍: f11 은 VDA 명세와 VDA 스키마로 독립 출처 아님)
    - f27 OTTO VDA 5050 인증의 시험 항목 미확인(벤더 주장)
    - f43 KTL·통합물류협회 협력 내용은 기사 기준, 1차 출처 미확인
    - f45 국내 변경 후 재평가 공식 규정 미확인(oq-092)
    - 20. 예외 복구·재계획·업무 연속성 ↔ 22. 시뮬레이션·예측용 디지털 트윈 연결 근거 미확보(oq-081)
    - ref-407·ref-408·ref-121·ref-204·ref-539·ref-541 은 이번 입력의 참고문헌 요약 목록에 없어 게시 페이지 각주·이전 브리프 값을 옮겼고, 유형·신뢰도는 이번 실행의 판단
- 범위 경계 위반 의심:
    - f3: 수요예측은 분류 원문 9장 상위 업무 시스템 경계라 '연계 대상:' 표시
    - f28: 센서 신호 장애 주입은 로봇 자체 인식·주행 견고성 시험이라 '연계 대상:' 표시
    - f42: 로봇 자체 성능 시험은 시험기관·제조사 쪽이라 '연계 대상:' 표시
    - f13·f17·f47: 제조 대상 자료라 물류 적용은 미확인으로 명시
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문을 연 출처: ref-031(VDA5050_EN.md), ref-051(state.schema), ref-228(factsheet.schema), ref-079(traffic-editor.md), ref-153(fleet adapter tutorial), ref-406(simulation.md), ref-229(IDTA 02020 README), ref-528(ARIAC challenges.rst). 나머지 30건은 게시 페이지 각주·이전 브리프 재사용이며 원문 미열람(신뢰도 상한 medium). 대분류 연결 실행 규칙(R-3)에 따라 근거를 게시된 21~24 세부영역 페이지와 A·B·C·D·E 대분류 페이지 각주에서 먼저 찾았고 신규 출처는 0건이다. 한국어 검색 1회(물류센터 AMR 가상 시운전 디지털 트윈)는 기사·업체 블로그뿐이라 쓰지 않았다. 한국 자료: KS B ISO 18646-1(ref-606), KIRIA 시험평가(ref-607), KTL 협력 보도(ref-466), KS X ISO 23247-1(ref-516). 교차 규칙: 매뉴얼 해석 AI 는 f8 로 21. 온보딩·설정·현장 시운전·5. 로봇 능력·작업 온톨로지·27. AI·학습·적응과 모델 운영에 함께 연결했다. 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈은 f14 에서 원문 구분대로 나눴다. 페이지 절 번호는 대분류 페이지 절 순서(핵심 질문·개요·세부 연구영역·핵심 포인트·다른 대분류와의 연결)로 5를 붙였다 [가정]. 정정 요청 없음. 해결된 열린 질문 없음.
