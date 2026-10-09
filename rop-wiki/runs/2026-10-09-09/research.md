# 리서치 브리프 2026-10-09-09

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-09-09 |
| 날짜 | 2026-10-09 |
| 실행 유형 | category_link (대분류 연결) |
| 대상 영역 | 해당 없음 |
| 대분류 | M. 안전 |

## 갭(비어 있거나 약한 섹션)

- M. 안전 대분류 페이지의 '다른 대분류와의 연결' 절이 '아직 작성되지 않음' 상태다. 48. 안전·위험 관리, 49. 사람 근접 안전, 50. 안전 표준·인증·사고 조사와 다른 16개 대분류의 연결이 정리되지 않았다
- 48. 안전·위험 관리 페이지는 이전 분류(2026-09-26) 기준이라 C. 채팅 기반 구성·운영, K. 플랫폼 아키텍처·인프라, O. 검증·도입·수명주기의 56. 운영 이관·확대·교육, P. 거버넌스·법규·사회와 잇는 근거가 페이지 안에 없다
- 48·49·50 페이지의 10절(다른 연구영역과의 연결)은 49·50 이 주제 페이지로 분리되어 있고 대분류 단위로 묶인 연결이 없다
- 정지·재개 판단에 쓰는 VDA 5050 안전 상태·운용 모드의 원문 확인과, 관제 통신이 끊겼을 때의 정지 경로(oq-095) 근거가 약하다
- ANSI/A3 R15.08-3(사용자 의무)과 국내 로봇작업 특별교육처럼 운영·교육 쪽 근거(oq-265, oq-275)가 게시 페이지에 없다
- Q. 현장 유형별 적용의 64. 상업 시설에 사람 근접 안전 적용 사례가 없다

## 조사 질문

1. 여러 로봇·사람·설비가 함께 움직일 때 생기는 위험을 어떻게 찾고 막을 것인가? [분류원문]
2. 48. 안전·위험 관리의 정지·재개 판단은 B. 로봇 온톨로지(6)·F. 연동(20·21·22)·H. 실행·협업·예외 복구(29·31·32)·K. 플랫폼 아키텍처·인프라(42)의 어떤 상태·명령·통신 경로에 기대는가? (oq-095, oq-229 관련)
3. 49. 사람 근접 안전의 구역·속도·사람 흐름 규칙은 D. 공간·지도 모델(15·16)·E. 사물·사람·실시간 상태(18·19)·G. 계획·최적화(25·27·28)·I. 설계·시뮬레이션(34·36)과 어떻게 이어지는가?
4. 50. 안전 표준·인증·사고 조사의 표준 개정·인증·사고 기록은 A. 기획·사업(1·2·3)·J. 현장 운영·관제(37·38·40)·N. 보안·개인정보(51·52·53)·O. 검증·도입·수명주기(54·55·56·57)·P. 거버넌스·법규·사회(58·59·60)와 어디서 만나는가? (oq-102, oq-252, oq-254, oq-265, oq-275 관련)
5. 언어 모델이 지시하는 로봇 계획의 안전 검사는 C. 채팅 기반 구성·운영(12·13)과 L. AI·학습 기술(44·47)의 '사람이 확인·승인한 계획만 실행' 원칙과 어떻게 맞물리는가? (oq-106, oq-144 관련)
6. M. 안전의 적용 사례는 Q. 현장 유형별 적용의 일곱 현장 유형 가운데 어디에 근거가 있으며, 한국 법령·인증·사고 자료는 무엇이 있는가?

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ A. 기획·사업의 2. 사용 사례·요구·책임 범위: ANSI/A3 R15.08 시리즈는 로봇 자체(1부), 산업용 이동로봇 시스템·적용의 통합(2부, 2023), 사용자의 산업용 이동로봇 적용 사용(3부, 2026)으로 나뉘어 제조사·통합자·사용자의 안전 책임을 부별로 다룬다. | ref-1419, ref-1084 | 아니오 | medium | 2026-09-17 | — | — |
| f2 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ A. 기획·사업의 2. 사용 사례·요구·책임 범위: R15.08 시리즈가 통합자와 사용자의 의무를 따로 두므로, 여러 제조사 로봇을 묶는 ROP 사업자가 현장마다 통합자 역할을 맡는지 사용자의 위험성평가를 지원하는 역할에 머무는지가 책임 범위 정의에 들어가야 할 것으로 보인다(oq-096). | ref-1419, ref-1084, ref-472 | 아니오 | low | 2026-10-09 | — | — |
| f3 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ A. 기획·사업의 1. 기술·시장·업체 동향: 주요 로봇 안전 표준의 개정이 2025~2026년에 몰려 있다. ISO 10218-1/-2 개정판은 2025-02에 나왔고 EN ISO 판의 참조가 2026-09-07 EU 관보에 실렸다. ANSI/A3 R15.08-3 은 A3 판매 페이지 기준 2026-04-23에 발행됐고, ISO 13482 개정판은 2026-09-15 기준 FDIS 단계다. | ref-1116, ref-1420, ref-1117 | 아니오 | medium | 2026-09 | — | — |
| f4 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ A. 기획·사업의 3. 경제성·조달·사업 모델·P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스: 2023-11-17 시행된 개정 지능형로봇법에 따라 보도에서 실외이동로봇을 운영하는 자는 보험(또는 공제)에 의무 가입해야 한다. 산업통상자원부는 한국로봇산업협회를 손해보장사업 실시기관으로 지정해 보험상품 출시를 지원한다. | ref-1424 | 아니오 | medium | 2023-11-16 | 실외 / 제약 | — |
| f5 | [추정] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ A. 기획·사업의 3. 경제성·조달·사업 모델: 실외 로봇 도입에서는 보험 가입과 인증 유지가 운영비 항목이 될 것으로 보인다. 인증 단위가 로봇과 관제장치의 조합이므로, 관제를 맡는 ROP 사업자가 운영자 의무 범위에 드는지가 조달·계약 단계의 쟁점이 될 것으로 보인다. | ref-1424, ref-980 | 아니오 | low | 2026-10-09 | 실외 / 제약 | — |
| f6 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ B. 로봇 온톨로지의 6. 온톨로지 기반 시스템·로봇 연동·H. 실행·협업·예외 복구의 29. 명령·작업 실행의 신뢰성: VDA 5050 3.0.0 의 운용 모드 가운데 AUTOMATIC 은 관제가 로봇을 완전히 제어하는 상태, SEMIAUTOMATIC 은 관제가 제어하되 주행 속도를 HMI 가 조정하는 상태다. INTERVENED·MANUAL·STARTUP·SERVICE·TEACH_IN 에서는 관제가 로봇을 제어하지 않는다. | ref-031 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f7 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ B. 로봇 온톨로지의 6. 온톨로지 기반 시스템·로봇 연동: 6. 온톨로지 기반 시스템·로봇 연동의 '실행 시점 조건 판단'에 배터리·적재 상태와 함께 운용 모드와 안전 상태(비상정지·보호 필드 침범)를 넣어야, 관제가 제어권이 없는 로봇에 작업을 내리지 않을 것으로 보인다. | ref-031 | 아니오 | low | 2026-10-09 | 제약 | — |
| f8 | [추정] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ B. 로봇 온톨로지의 4. 이기종 로봇 등록: 로봇마다 R15.08 유형(A·B·C), 적용 안전 표준과 판, 인증 상태를 등록 정보로 두면 표준 개정과 인증 범위를 배정·경로 제약으로 추적할 수 있을 것으로 보인다. | ref-1419, ref-1116, ref-980 | 아니오 | low | 2026-10-09 | — | — |
| f9 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션: Obi 외(2026-04)는 언어 모델이 제어하는 로봇 시스템에 실행 전 안전 게이트(SafeGate)와 작업 안전 계약을 두는 방법을 제안했다. | ref-417 | 아니오 | medium | 2026-04 | 제약 | 원문 미열람 |
| f10 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ C. 채팅 기반 구성·운영의 13. 대화형 기능의 신뢰·기반: Ravichandran 외의 RoboGuard 에서는 악성 프롬프트와 격리한 신뢰 기점 LLM 이 미리 정한 안전 규칙을 시간 논리 제약으로 바꾸고 제어 합성으로 계획과의 충돌을 푼다. 저자들은 최악의 탈옥 공격에서 위험 계획 실행이 92% 이상에서 3% 미만으로 줄었다고 보고했다. | ref-700 | 아니오 | medium | 2026-03-03 | 제약 | 원문 미열람 |
| f11 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ C. 채팅 기반 구성·운영의 13. 대화형 기능의 신뢰·기반·N. 보안·개인정보의 52. 통신 보호·위협 관리·감사: Robey 외(2024-10)는 언어 모델이 제어하는 로봇이 해로운 물리 행동을 하도록 만드는 탈옥 알고리즘 RoboPAIR 를 제시했다. GPT-4o 계획기를 쓴 Clearpath Jackal 과 GPT-3.5 를 연동한 Unitree Go2 등에서 공격 성공률이 자주 100%에 이르렀다고 보고했다. | ref-857 | 아니오 | medium | 2024-10-17 | 제약 | 원문 미열람 |
| f12 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ C. 채팅 기반 구성·운영의 12. 채팅으로 업무 지시·오케스트레이션·13. 대화형 기능의 신뢰·기반: 분류 원문 C 주석의 '사람이 확인·승인한 계획만 실행' 원칙에 실행 전 안전 게이트·가드레일 같은 자동 검사를 더하면, 대화 지시에서 로봇 동작까지 이어지는 경로가 48. 안전·위험 관리의 위험성평가 대상이 될 것으로 보인다. 로봇 자체 안전 기능은 연계 대상으로 남는다. | ref-417, ref-700 | 아니오 | low | 2026-10-09 | 완료·인계 | 원문 미열람 |
| f13 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ D. 공간·지도 모델의 16. 장소 의미·지도 관리·F. 연동의 21. 상호운용 표준·적합성: VDA 5050 3.0.0 은 기능·운영·시스템 안전 요구를 정하지 않으며, 안전 표준으로 여기거나 적용해서는 안 된다고 범위 절에 적는다. | ref-031 | 아니오 | medium | 2026-10-09 | — | — |
| f14 | [사실] | M. 안전의 49. 사람 근접 안전 ↔ D. 공간·지도 모델의 16. 장소 의미·지도 관리: VDA 5050 3.0.0 의 BLOCKED 구역에는 로봇이 들어가서는 안 되며, 구역 안에 있는 로봇은 멈추고 BLOCKED_ZONE_VIOLATION 오류를 CRITICAL 수준으로 보고한다. SPEED_LIMIT 구역에서는 구역에 들어설 때 이미 최대 속도(m/s) 이하여야 한다. | ref-031 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f15 | [추정] | M. 안전의 49. 사람 근접 안전 ↔ D. 공간·지도 모델의 16. 장소 의미·지도 관리: 지도에 붙은 진입 금지·속도 제한 구역은 VDA 5050 이 정한 교통 관리 규칙이며 안전 기능이 아니다. 따라서 위험성평가에서 이를 위험 감소 조치로 인정받으려면 ISO 3691-4 의 운용 구역 준비와 로봇의 안전 등급 보호 필드 설정에 맞춰야 할 것으로 보인다(oq-229). | ref-031, ref-470 | 아니오 | low | 2026-10-09 | 제약 | — |
| f16 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ D. 공간·지도 모델의 15. 지도·공간·위치 모델: ISO 3691-4:2023 은 무인 산업 차량이 운행하는 구역의 상태가 안전 운용에 큰 영향을 준다고 보고, 운용 구역 준비를 부속서 A 에 둔다. | ref-470 | 아니오 | medium | 2023-06 | 제약 | 원문 미열람 |
| f17 | [사실] | 연계 대상: M. 안전의 48. 안전·위험 관리 ↔ D. 공간·지도 모델의 15. 지도·공간·위치 모델: Abdul Hafez 외(IJRR, 2025-05)는 무결성 위험 지표로 EKF 기반 SLAM 위치추정의 안전성을 정량화했다. 데이터 연관 오류가 위치를 크게 해칠 수 있고, 랜드마크 밀도가 지나치게 높으면 안전성이 오히려 떨어진다고 보고했다. | ref-161 | 아니오 | medium | 2025-05 | — | 원문 미열람 |
| f18 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성: Open-RMF 승강기 상태(LiftState)의 현재 모드에는 알 수 없음·사람·AGV·화재·오프라인·비상이 있다. 이 가운데 사람·AGV 모드만 설정할 수 있고 나머지는 읽기 전용이다. | ref-286 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f19 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ E. 사물·사람·실시간 상태의 18. 실시간 세계 상태·데이터 일관성: 승강기의 화재·비상 모드 제어는 시설·설비 제어 경계의 연계 대상이다. ROP 는 탑승을 확정하기 전에 최신 모드를 확인해 작업·경로 제약에 반영하는 쪽을 맡는 것으로 보인다. | ref-286 | 아니오 | low | 2026-10-09 | 제약 | — |
| f20 | [사실] | M. 안전의 49. 사람 근접 안전 ↔ E. 사물·사람·실시간 상태의 19. 사람·보행자 모델: 한림대학교성심병원은 밤에 인식한 경로가 낮 혼잡에서는 원활하지 않을 수 있다고 보고, 로봇 통행 경로와 작업 정지 지점을 전용 스티커로 표시했다. | ref-1181 | 아니오 | low | 2024-07-12 | 병원 / 제약 | 원문 미열람 |
| f21 | [추정] | M. 안전의 49. 사람 근접 안전 ↔ E. 사물·사람·실시간 상태의 19. 사람·보행자 모델: 병원의 사람·휠체어 대기 규칙이나 창고의 학습된 사람 흐름처럼 사람 흐름 정보는 구역·시간대별 대기·속도 규칙으로 49. 사람 근접 안전과 이어질 것으로 보인다. 이때 사람 검출·안전 정지는 로봇이 맡는 연계 대상이다. | ref-1181, ref-1180 | 아니오 | low | 2026-10-09 | 제약 | 원문 미열람 |
| f22 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ F. 연동의 22. 설비·건물 시스템 연동: 국가기술표준원은 2021-11 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항과 평가 방법을 정한 국가표준 KS B 7317 을 제정했다. | ref-945 | 아니오 | medium | 2021-11-11 | 제약 | 원문 미열람 |
| f23 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ F. 연동의 22. 설비·건물 시스템 연동·N. 보안·개인정보의 51. 인증·권한·격리·53. 개인정보·영상 데이터: ISO 13482 개정 초안(ISO/DIS 13482:2024, DIN EN ISO 13482 2024-10 초안)은 구성을 로봇 유형별로 바꾸고 탑승형 로봇 절을 뺐다. 사이버보안, 데이터 보호, 승강기와 협동하는 로봇(참고 부속서 H) 절을 새로 넣었다. | ref-1425 | 아니오 | medium | 2024-10 | — | — |
| f24 | [추정] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ F. 연동의 22. 설비·건물 시스템 연동: 로봇의 승강기 탑승 안전 요구가 국내 KS 와 서비스 로봇 안전 표준 개정 초안 양쪽에 들어오므로, ROP 는 승강기 연동 요청·운영 모드 확인을 맡고 탑승 안전의 적합성은 로봇·승강기 쪽 표준에 맡기는 경계가 될 것으로 보인다. 개정 초안 내용이 최종판에 남았는지는 확인하지 못했다(oq-254). | ref-945, ref-1425, ref-1117 | 아니오 | low | 2026-10-09 | 제약 | — |
| f25 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ F. 연동의 20. 로봇·제조사 관제 연동: Open-RMF 기능 요청 이슈 #658 은 화재경보가 울리면 로봇들이 주차 위치로 이동하지만, 비상 신호가 대상 플릿을 구분하지 않는 불리언 값이라고 지적한다. | ref-567 | 아니오 | medium | 2025-04-04 | 시작 조건 | 원문 미열람 |
| f26 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ F. 연동의 21. 상호운용 표준·적합성: ISO 21423(산업용 이동로봇 통신·상호운용성)의 범위는 여러 제조사 AMR·플릿 관리 장비·기업 자원 사이의 통신 프로토콜이다. 안전 요구와 공공 도로 이동 기계는 범위에서 뺀다. | ref-159 | 아니오 | medium | 2026-10-09 | — | 원문 미열람 |
| f27 | [추정] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ F. 연동의 21. 상호운용 표준·적합성: VDA 5050 과 ISO 21423 같은 상호운용 표준이 안전 요구를 범위에서 빼므로, 연동 적합성 시험(21. 상호운용 표준·적합성)과 안전 표준 적합성·인증(50. 안전 표준·인증·사고 조사)은 별도 경로로 관리해야 할 것으로 보인다. | ref-031, ref-159 | 아니오 | low | 2026-10-09 | — | — |
| f28 | [사실] | M. 안전의 49. 사람 근접 안전 ↔ G. 계획·최적화의 25. 작업 배정 — MRTA: Kazemi Eskeri 외(IROS 2025)는 사람과 함께 쓰는 환경에서 사람을 고려하는 다중 로봇 작업 배정 방법을 다뤘다. | ref-1083 | 아니오 | medium | 2025-08-27 | 수행 자원 | 원문 미열람 |
| f29 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ G. 계획·최적화의 28. 공용 자원·충전·에너지 최적화: Open-RMF 데모에서는 비상 경보가 켜지면 모든 로봇을 가장 가까운 주차 위치로 보낸다. | ref-104 | 아니오 | medium | 2026-10-09 | 예외·성과 | 원문 미열람 |
| f30 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ G. 계획·최적화의 27. 다중 로봇 경로·교통 관리 — MAPF: Open-RMF 는 긴급 작업을 높은 우선순위 참여자가 교통 협상을 강제하는 방식으로 다룬다. | ref-004 | 아니오 | medium | 2026-10-09 | 제약 | — |
| f31 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ G. 계획·최적화의 27. 다중 로봇 경로·교통 관리 — MAPF: Reliability Engineering & System Safety 게재 연구(2023)는 다중 이동로봇 운반 작업의 충돌 위험원을 STPA 와 확률 페트리넷(SPN)으로 모델링·분석했다. | ref-565 | 아니오 | medium | 2023 | — | 원문 미열람 |
| f32 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ H. 실행·협업·예외 복구의 29. 명령·작업 실행의 신뢰성: VDA 5050 3.0.0 의 안전 상태(safetyState)는 activeEmergencyStop 을 MANUAL(로봇에서 수동 확인), REMOTE(시설 비상정지를 원격 확인), NONE 으로 보고하고, fieldViolation 으로 레이저·범퍼 같은 보호 필드 침범 여부를 보고한다. | ref-031 | 아니오 | medium | 2026-10-09 | 예외·성과 | — |
| f33 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ H. 실행·협업·예외 복구의 29. 명령·작업 실행의 신뢰성·31. 사람–로봇 협업: ROP 의 재개 지시는 비상정지가 NONE 이고 운용 모드가 AUTOMATIC 으로 돌아온 것을 확인한 뒤에 내려야 할 것으로 보인다. MANUAL 비상정지는 로봇에서 사람이 확인해야 하므로 현장 인력 출동이 복구 절차에 들어갈 것으로 보인다(oq-095). | ref-031 | 아니오 | low | 2026-10-09 | 완료·인계 | — |
| f34 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성: VDA 5050 3.0.0 에서 로봇은 브로커와 연결이 끊겨도 받은 주문 정보를 유지하고, 마지막으로 해제된 노드까지 주문을 수행한다. | ref-031 | 아니오 | medium | 2026-10-09 | 예외·성과 | — |
| f35 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성·J. 현장 운영·관제의 40. 운영 절차·요청 창구: 2026-09 식품 제조 공장에서 멈춘 제품 적재 로봇을 점검하던 노동자가 끼여 숨진 사고에 대해, 고용노동부 통영지청은 전원 차단·기동스위치 잠금·표지(LOTO)가 실시되지 않았다고 지적했다. | ref-1125 | 아니오 | low | 2026-09-29 | 제조 공장 / 제약 | 원문 미열람 |
| f36 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성: 2023-11 농산물유통센터에서 상자를 팔레트로 옮기는 로봇의 센서 오류를 점검하고 프로그램을 고친 뒤 작동을 확인하던 작업자가 로봇에 압착되어 숨졌다. | ref-1124 | 아니오 | low | 2023-11-08 | 물류창고 / 예외·성과 | 원문 미열람 |
| f37 | [추정] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ H. 실행·협업·예외 복구의 32. 예외 복구·재계획·업무 연속성·J. 현장 운영·관제의 40. 운영 절차·요청 창구: 확인한 두 사망 사고가 모두 점검·작동 확인 같은 비정상 작업 중에 났으므로, ROP 가 정지 뒤 재가동·재개를 지시하기 전에 작업 중인 사람과 잠금 상태를 확인하는 절차가 복구 절차와 운영 절차의 접점이 될 것으로 보인다. | ref-1124, ref-1125, ref-031 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f38 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈·36. 가상 시운전·실제 상황 재현: Huck·Ledermann·Kröger(SPCE 2020)는 사람 모델과 최적화 알고리즘으로 시뮬레이션 안에서 고위험 사람 행동을 만들어, 물리 시제품이 없는 초기 설계 단계의 산업용 로봇 셀에서 작업자 위험을 드러내는 방법을 개념 증명으로 보였다. | ref-1241 | 아니오 | medium | 2020-11-20 | 예외·성과 | 원문 미열람 |
| f39 | [사실] | M. 안전의 49. 사람 근접 안전 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈·E. 사물·사람·실시간 상태의 19. 사람·보행자 모델: Open-RMF 시뮬레이션은 menge 로 가상 사람을 움직이는 선택 기능 crowdsim 을 traffic-editor 에서 켤 수 있고, 예제 공항 터미널 월드가 이를 군중 시뮬레이션에 쓴다. | ref-406 | 아니오 | medium | 2026-10-09 | 상업 시설 / 제약 | — |
| f40 | [사실] | M. 안전의 49. 사람 근접 안전 ↔ I. 설계·시뮬레이션의 34. 시뮬레이션·예측용 디지털 트윈: Rondoni 외(Scientific Reports, 2024-08)는 모의 병원 환경에서 병원 물류 로봇 HOSBOT 과 TIAGo 를 실내 보행 속도에 견줄 만한 0.2·0.6·1.0 m/s 로 주행시켜 7개 지표로 비교했다. 최고 속도에서는 방향 오차가 커졌다. | ref-1081 | 아니오 | medium | 2024-08-07 | 병원 / 제약 | 원문 미열람 |
| f41 | [추정] | 연계 대상: M. 안전의 50. 안전 표준·인증·사고 조사 ↔ I. 설계·시뮬레이션의 36. 가상 시운전·실제 상황 재현: Wind River 인터뷰(2014)는 IEC 61508-7 이 시뮬레이션을 시험 목적의 설비 거동 모사로 정의한다고 인용하고, 기능안전 표준이 안전 확인에 시뮬레이션을 권고한다고 해석했다. 그러나 이동로봇 안전 인증이 시뮬레이션 결과를 근거로 받아들이는 절차는 찾지 못했다. | ref-1249 | 아니오 | low | 2014-11-20 | — | 원문 미열람 |
| f42 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ J. 현장 운영·관제의 37. 관제 화면·실행 기록: Winfield 외(2022-05)는 사회적 로봇의 사고 조사를 위한 윤리적 블랙박스(Ethical Black Box) 개방 표준 초안을 제안했다. | ref-1120 | 아니오 | medium | 2022-05-13 | 예외·성과 | 원문 미열람 |
| f43 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석: Sanders·Sener·Chen(Applied Ergonomics, 2024)은 미국 OSHA 중대 부상 보고(Severe Injury Reports)에서 작업장 로봇 관련 부상을 분석했다. | ref-1122 | 아니오 | medium | 2024 | 예외·성과 | 원문 미열람 |
| f44 | [추정] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ J. 현장 운영·관제의 37. 관제 화면·실행 기록: 플릿 수준에서 명령·정지·재가동·운용 모드 전환·안전 상태 보고를 시각과 함께 남기는 실행 기록이 사고·아차 사고 조사의 입력이 될 것으로 보인다. 그 최소 항목을 정한 표준은 확인하지 못했다(oq-252). | ref-1120, ref-1122, ref-031 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f45 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석·O. 검증·도입·수명주기의 54. 시험·형식 검증·벤치마크: Ferrando 외(2020)의 ROSMonitoring 은 ROS 응용의 형식 속성을 ROS 바깥에서 명세해 실행 중에 검증하는 런타임 검증 틀이다. 여러 ROS 배포판에 옮겨 쓸 수 있고 특정 명세 형식에 묶이지 않는다. | ref-1426 | 아니오 | medium | 2020-12-03 | — | — |
| f46 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ J. 현장 운영·관제의 38. 모니터링·이상 탐지·원인 분석: 진입 금지 구역 위반이나 정지 지시 뒤 응답처럼 안전과 관련된 운영 규칙을 실행 중에 감시하는 런타임 검증이 38. 모니터링·이상 탐지·원인 분석과 48. 안전·위험 관리를 잇는 방법이 될 것으로 보인다. 다만 제조사가 다른 플릿에 적용한 사례는 확인하지 못했다. | ref-1426, ref-031 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f47 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ J. 현장 운영·관제의 40. 운영 절차·요청 창구: ANSI/A3 R15.08-3-2026 은 산업용 이동로봇을 운영하는 사용자에게 위험성평가와 그 결과 위험 감소 조치의 유지, 변경 관리, 직원 교육과 안전 작업 절차를 요구한다. | ref-1419, ref-1421 | 예 | medium | 2026-10-04 | — | — |
| f48 | [추정] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ J. 현장 운영·관제의 40. 운영 절차·요청 창구·O. 검증·도입·수명주기의 56. 운영 이관·확대·교육: R15.08-3 의 사용자 교육·안전 작업 절차 요구는 40. 운영 절차·요청 창구의 현장 절차와 56. 운영 이관·확대·교육의 교육 계획으로 넘어갈 것으로 보인다. 여러 제조사 로봇이 섞인 현장에서 누가 이를 이행하는지는 확인하지 못했다(oq-265). | ref-1419, ref-1421 | 아니오 | low | 2026-10-09 | — | — |
| f49 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조: FORT Robotics 사례 소개에 따르면, 한 창고의 울타리 친 AMR 구역에서 문에 단 주 제어기가 문이 열리면 모든 로봇에 무선 안전 비상정지를 보낸다. 이 시스템은 ISO 13849 범주 3·PLd 로 설계됐다고 한다. | ref-1422 | 아니오 | low | 2023-05-18 | 물류창고 / 예외·성과 | 벤더 주장 |
| f50 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ K. 플랫폼 아키텍처·인프라의 42. 분산 시스템·통신·컴퓨팅 구조: VDA 5050 은 안전 표준이 아니고, 연결이 끊긴 로봇은 받은 주문을 이어 수행한다. 따라서 플릿 일괄 정지는 관제 메시지 경로가 아니라 그와 독립된 안전 등급 정지 경로에 맡기고, ROP 는 정지 결과를 상태로 받아 작업을 보류·재배정하는 구조가 두 대분류의 경계가 될 것으로 보인다(oq-095). | ref-031, ref-1422 | 아니오 | low | 2026-10-09 | 예외·성과 | — |
| f51 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ L. AI·학습 기술의 47. AI·학습·적응과 모델 운영: EU AI Act(Regulation (EU) 2024/1689)는 부속서 I 의 EU 조화 법령(기계류 등) 대상 제품의 안전 구성요소이거나 제품 자체이면서 제3자 적합성 평가를 받는 AI 시스템을 고위험 AI 로 분류한다. | ref-621 | 아니오 | medium | 2026-10-09 | — | 원문 미열람 |
| f52 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ L. AI·학습 기술의 47. AI·학습·적응과 모델 운영·O. 검증·도입·수명주기의 56. 운영 이관·확대·교육: 법무법인 태평양 해설에 따르면 고영향 인공지능사업자 책무 고시·가이드라인 초안은 개발 단계에서 사람이 개입할 기준과 긴급 정지 같은 개입 방법을 정하게 하고, 운영 단계에서 성능 저하·오류의 정기 점검과 관리자 교육을 요구한다. | ref-1341 | 아니오 | medium | 2025-09-30 | 예외·성과 | 원문 미열람 |
| f53 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ L. AI·학습 기술의 44. 로봇 기반 모델·언어 모델 계획·47. AI·학습·적응과 모델 운영: AI 가 정지·경로·구역 결정에 관여하면 실행 전 안전 게이트 같은 채택 검사는 47. AI·학습·적응과 모델 운영의 채택 기준과 48. 안전·위험 관리의 위험성평가 양쪽에 걸칠 것으로 보인다. 이런 AI 가 제품 안전 구성요소로 분류되는지는 열린 질문이다(oq-106). | ref-621, ref-417 | 아니오 | low | 2026-10-09 | — | 원문 미열람 |
| f54 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ N. 보안·개인정보의 51. 인증·권한·격리·52. 통신 보호·위협 관리·감사: 산업용 로봇 안전 표준 ISO 10218-1/-2 의 2025년 개정판에는 사이버보안 요구가 새로 들어갔다. | ref-1116, ref-1076 | 예 | medium | 2026-09-18 | — | — |
| f55 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스: EN ISO 10218-1:2025·-2:2025 의 참조는 위원회 시행결정 (EU) 2026/2015 에 따라 2026-09-07 EU 관보에 실려 기계류 지침 2006/42/EC 의 조화 표준이 됐다. | ref-1116 | 아니오 | medium | 2026-09-18 | — | — |
| f56 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ N. 보안·개인정보의 52. 통신 보호·위협 관리·감사: Carr 외(2022)는 ROS 로 구동되는 시스템에서 디지털 트윈에 대한 중간자 공격이 물리 로봇의 실패로 이어질 수 있으며, 이는 산업용 로봇팔과 자율이동로봇 모두에 해당한다고 보고했다. | ref-1242 | 아니오 | medium | 2022-11-17 | — | 원문 미열람 |
| f57 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ N. 보안·개인정보의 51. 인증·권한·격리·53. 개인정보·영상 데이터: 산업용·서비스 로봇 안전 표준에 사이버보안과 데이터 보호가 들어오면서, ROP 가 내리는 원격 정지·재개·구역 변경 명령의 권한 통제와 사람 위치·영상 데이터 처리도 안전 평가 대상이 될 것으로 보인다. | ref-1116, ref-1425 | 아니오 | low | 2026-10-09 | 제약 | — |
| f58 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ O. 검증·도입·수명주기의 55. 현장 조사·설치·시운전: Belzile 외(2025-02)는 ISO 10218, ISO/TS 15066, ANSI/RIA R15.08, ANSI/ITSDF B56.5, CSA Z434 를 검토한 결과, 이동로봇 전용이면서 여러 배치 상황에 적용할 수 있는 표준이 없다고 보았다. 이에 건설 현장 이동로봇 배치 전에 쓸 위험성평가 틀을 제안했다. | ref-563 | 아니오 | medium | 2025-02 | 기타 / 제약 | 원문 미열람 |
| f59 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ O. 검증·도입·수명주기의 56. 운영 이관·확대·교육: 법제처 법령해석 23-0872(2023-11-21)는 산업안전보건법 시행규칙 별표 5 제1호라목 36란의 특별교육 대상 '로봇작업'이 '산업용 로봇'을 쓰는 작업으로 한정되지 않는다고 회답했다. KS B ISO 8373 의 '로봇'이 산업용·서비스용·의료용을 포괄한다는 점을 근거로 들었다. | ref-1423 | 아니오 | medium | 2023-11-21 | 제약 | — |
| f60 | [추정] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ O. 검증·도입·수명주기의 56. 운영 이관·확대·교육: 법제처 해석에 따르면 서비스·이동 로봇을 쓰는 작업도 로봇작업 특별교육 대상이 될 수 있으므로, ROP 를 들인 현장의 운영 이관 교육 계획에 법정 특별교육 해당 여부 판단이 들어가야 할 것으로 보인다. 고용노동부의 적용 지침은 확인하지 못했다(oq-275). | ref-1423 | 아니오 | low | 2026-10-09 | — | — |
| f61 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ O. 검증·도입·수명주기의 57. 자산·소프트웨어 수명주기 관리: R15.08-3 은 공급자가 배치한 뒤 사용자가 산업용 이동로봇이나 그 적용·운영 환경을 바꾸는 경우에도 사용자의 위험성평가 의무가 적용된다고 한다. | ref-1419 | 아니오 | medium | 2026-09-17 | — | — |
| f62 | [추정] | M. 안전의 48. 안전·위험 관리 ↔ O. 검증·도입·수명주기의 57. 자산·소프트웨어 수명주기 관리: ROP 에서 구역·속도 제한·경로망·운영 정책을 바꾸는 일이 사용자 쪽 변경 관리와 위험성 재평가의 계기가 될 수 있으므로, 설정 변경 이력을 판 단위로 남기고 재평가 필요 여부를 표시하는 기능이 두 영역을 잇는 것으로 보인다(oq-093, oq-282). | ref-1419, ref-031 | 아니오 | low | 2026-10-09 | — | — |
| f63 | [사실] | M. 안전의 49. 사람 근접 안전 ↔ O. 검증·도입·수명주기의 54. 시험·형식 검증·벤치마크: Francis 외(2023)는 사회적 로봇 내비게이션 알고리즘의 평가 원칙과 지침을 정리했다. | ref-1079 | 아니오 | medium | 2023-06-29 | — | 원문 미열람 |
| f64 | [사실] | M. 안전의 48. 안전·위험 관리 ↔ P. 거버넌스·법규·사회의 58. 다사업자 책임·계약·데이터: ANSI/A3 R15.08-2(2023-10)는 산업용 이동로봇 시스템과 적용의 안전 요구를 다루는 2부로 발표됐다. | ref-472, ref-1084 | 아니오 | medium | 2023-10 | — | 원문 미열람 |
| f65 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스: 실외이동로봇 운행안전인증은 지능형 로봇 개발 및 보급 촉진법 제40조의2 에 근거하며, 인증 절차와 기준은 산업통상자원부 고시(2023-11-17)로 정해졌다. | ref-980, ref-1118 | 아니오 | medium | 2023-11-17 | 실외 / 제약 | 원문 미열람 |
| f66 | [사실] | M. 안전의 49. 사람 근접 안전 ↔ P. 거버넌스·법규·사회의 59. 법·규제·보험·라이선스: 산업안전보건기준에 관한 규칙 제223조(운전 중 위험 방지)는 산업용 로봇의 운전 중 위험 방지 조치를 정한다. 같은 조는 한국산업표준이나 국제 안전기준에 맞는 경우 방책 같은 조치를 생략할 수 있게 한다. | ref-562 | 아니오 | medium | 2023-07-01 | 제약 | 원문 미열람 |
| f67 | [사실] | M. 안전의 49. 사람 근접 안전 ↔ P. 거버넌스·법규·사회의 60. 노동·수용성·접근성: Han 외(CHI 2024)는 이동장애인 15명과 로봇 실무자 8명을 면담하고 공동설계 워크숍을 연 결과, 이동장애인이 보도 로봇과 보도 공간을 두고 경쟁한다고 느끼고 부족한 연석 경사로 같은 기존 장벽 위에서 로봇이 운행된다고 보고했다. | ref-1214 | 아니오 | medium | 2024-04-07 | 실외 / 작업 대상 | 원문 미열람 |
| f68 | [추정] | M. 안전의 49. 사람 근접 안전 ↔ Q. 현장 유형별 적용의 61. 물류창고: 아마존은 자사 풀필먼트 센터에서 직원이 로보틱스 테크 조끼를 켜고 로봇 구역에 들어가면 로봇이 자동으로 감속하거나 경로를 바꾸고, 가까운 로봇은 정지한다고 설명한다. | ref-1080 | 아니오 | low | 2026-10-09 | 물류창고 / 제약 | 원문 미열람, 벤더 주장 |
| f69 | [사실] | M. 안전의 50. 안전 표준·인증·사고 조사 ↔ Q. 현장 유형별 적용의 65. 가정·공동주택: Webb 외(2021)는 지원 주거 아파트에서 넘어진 거주자를 보조 로봇이 직원에게 알리지 못한 모의 사고를, 역할극 증언 면담과 윤리적 블랙박스 기록으로 조사하는 방법을 시험했다. | ref-1121 | 아니오 | medium | 2021-06-29 | 가정 / 예외·성과 | 원문 미열람 |
| f70 | [사실] | M. 안전의 49. 사람 근접 안전 ↔ Q. 현장 유형별 적용의 66. 실외: 한국로봇산업진흥원은 실외이동로봇 운행안전인증 대상을 최고 속도 15km/h 이하·최대 질량 500kg 이하로 두고 주변 인식과 비상정지를 심사하며, 인증 뒤 2년 주기 정기점검을 둔다. | ref-980 | 아니오 | medium | 2026-09-30 | 실외 / 제약 | 원문 미열람 |

### 근거 발췌

- **f1**: ANSI 블로그는 3부가 "describes user responsibilities for safe operation of IMR applications"라고 쓰고 유형 A·B·C 정의는 1부를 따른다고 적는다. 2부가 IMR 시스템·적용 통합 안전을 다룬다는 것은 The Robot Report(2023-10-26) 기준.
- **f2**: 2부는 통합, 3부는 사용자 의무로 나뉜다. ROP 사업자의 해당 역할을 정한 자료는 찾지 못했다.
- **f3**: IBF: "On 7 September 2026, their references were published in the Official Journal". A3 판매 페이지: 발행일 2026-04-23, 77쪽. ISO 13482 단계는 50. 안전 표준·인증·사고 조사 페이지의 ref-1117 기준이다.
- **f4**: 메트로신문(2023-11-16): 보도에서 운영하는 자는 "보험(또는 공제)에 의무적으로 가입해야 합니다." 운행안전인증 대상은 질량 500kg·속도 15km/h 이하·폭 800mm 미만이다. 조항 번호는 기사에 없다.
- **f5**: 보험 의무는 운영자에게 있다(기사). 인증 대상은 로봇과 관제장치의 조합이다(진흥원 페이지, 49. 사람 근접 안전 페이지 기준).
- **f6**: AUTOMATIC: "Fleet control is in full control of the mobile robot." MANUAL·SERVICE·TEACH_IN 등은 관제가 제어하지 않는 상태이며, SERVICE 에서는 권한 있는 인력이 로봇을 재구성할 수 있다(3.0.0, 7.8절·6.6.6절).
- **f7**: VDA 5050 상태 메시지에는 운용 모드와 safetyState(activeEmergencyStop, fieldViolation)가 함께 들어 있다. 이를 능력 실행 조건에 넣은 공개 구현은 확인하지 못했다.
- **f8**: R15.08-3 은 유형 A·B·C 시스템에 적용된다. ISO 10218 은 판이 바뀌었고, 실외 인증은 질량·속도 조건이 붙는다. 50. 안전 표준·인증·사고 조사 페이지 9절의 등록 제안을 이어받은 것이다.
- **f9**: Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems(arXiv 2604.05427). 48. 안전·위험 관리 페이지 10절에서 재인용했다.
- **f10**: 저자 보고값이며 독립 재현은 확인하지 못했다. 2026-03 개정판 기준이다. (재인용: 2026-10-09-08)
- **f11**: Jailbreaking LLM-Controlled Robots(arXiv 2410.13691). 저자 보고값이다. (재인용: 2026-10-09-08)
- **f12**: 두 연구 모두 언어 모델 계획과 실행 사이에 검사 계층을 둔다. 다중 로봇 플릿의 배정·경로 계획에 적용한 사례는 찾지 못했다.
- **f13**: Scope: "does not define functional, operational, or system safety requirements"이며, 안전 표준으로 "shall not be regarded or applied"라고 적는다.
- **f14**: 6.4.1.1절 표 6의 윤곽 기반 구역 정의다. BLOCKED 구역은 LINE_GUIDED 구역보다 우선한다(6.4.4절).
- **f15**: VDA 5050 은 안전 요구를 정하지 않는다. ISO 3691-4 는 운용 구역 준비를 부속서 A 에 둔다(원문 미열람). 둘을 잇는 검증 주체는 확인하지 못했다.
- **f16**: 48. 안전·위험 관리 페이지 4절의 운용 구역 정의에서 재인용했다. 표준 본문은 열람하지 않았다(oq-170).
- **f17**: SLAM 위치추정 자체는 분류 원문 19장의 '로봇 자체 지능·제어' 경계에 속한다. D. 공간·지도 모델 페이지 M 절에서 재인용했다.
- **f18**: E. 사물·사람·실시간 상태 페이지 M 절에서 재인용했다.
- **f19**: 모드가 읽기 전용이므로 ROP 몫은 확인과 반영이다. 모드 정보를 몇 초까지 믿을지는 oq-034 다.
- **f20**: 조선비즈 2024-07-12 기사 1건 기준이다. E. 사물·사람·실시간 상태 페이지 D 절에서 재인용했다.
- **f21**: ILIAD 는 학습한 사람 흐름에 맞춰 창고 자율 지게차 경로를 계획했다. 병원 사례는 기사 1건 기준이다.
- **f22**: 국가기술표준원 보도(KDI 경제정보센터 게재, 2021-11-11)이며, 50. 안전 표준·인증·사고 조사 페이지 3절에서 재인용했다.
- **f23**: DIN Media 초안 소개: "Die Struktur des Dokuments wurde von Sicherheitsanforderungen in spezifische Robotertypen geändert". 초안 기준이며 최종판 반영 여부는 확인하지 못했다.
- **f24**: KS B 7317(2021)과 ISO/DIS 13482:2024 부속서 H 가 있고, ISO 13482 는 FDIS 단계다. 두 문서의 대응 관계는 확인하지 못했다.
- **f25**: 이슈 작성 시점(2025-04-04) 기준이며 이후 구현 여부는 확인하지 못했다. 48. 안전·위험 관리 페이지 5절에서 재인용했다.
- **f26**: D. 공간·지도 모델 페이지 F 절(확인일 2026-10-09, 발행 진행 중 단계 60.00)에서 재인용했다. (발행일 미확인, 확인일 기준)
- **f27**: 두 문서 모두 안전 요구를 정하지 않는다고 범위에서 밝힌다.
- **f28**: Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments(arXiv 2508.19731). 49. 사람 근접 안전 페이지 6절·9절에서 재인용했다.
- **f29**: rmf_demos README 기준이다. G. 계획·최적화 페이지 옛 G 절에서 재인용했다.
- **f30**: RMF Core Overview 기준이다. 48. 안전·위험 관리 페이지 5절에서 재인용했다.
- **f31**: Collision hazard modeling and analysis in a multi-mobile robots system transportation task with STPA and SPN. 저자는 확인하지 못했다.
- **f32**: 7.8절: REMOTE 는 "facility emergency stop shall be acknowledged remotely"이다. 3.0.0 본문에서 AUTOACK 값은 찾지 못했다.
- **f33**: 안전 상태와 운용 모드 정의에서 끌어낸 판단이다. 재개 판정 규칙을 정한 표준은 확인하지 못했다.
- **f34**: 4.1절: "fulfills the order up to the last released node".
- **f35**: 경남도민일보 2026-09-29 보도 기준이며 원인은 확정되지 않았다. 50. 안전 표준·인증·사고 조사 페이지 5절에서 재인용했다.
- **f36**: 경향신문 2023-11-08 보도 기준이다. 경찰은 로봇이 사람을 상자로 인식한 것으로 보았다. 50. 안전 표준·인증·사고 조사 페이지 5절에서 재인용했다.
- **f37**: 두 사고는 기사 기준이다. 플릿 관제의 재개 지시와 잠금·표지를 잇는 공개 절차는 확인하지 못했다.
- **f38**: Simulation-based Testing for Early Safety-Validation of Robot Systems(arXiv 2011.10294). (재인용: 2026-10-09-07)
- **f39**: Simulation 장 기준이다. 이는 가정한 미래를 실험하는 쪽이며 현재 상태 표현(18. 실시간 세계 상태·데이터 일관성)과 구분한다. (재인용: 2026-10-09-07)
- **f40**: 실제 병원이 아닌 시뮬레이션 평가다. 49. 사람 근접 안전 페이지 5절에서 재인용했다.
- **f41**: 업체 블로그의 표준 인용이며, IEC 61508-7 원문은 열람하지 않았다. (재인용: 2026-10-09-07)
- **f42**: An Ethical Black Box for Social Robots: a draft Open Standard(arXiv 2205.06564). 50. 안전 표준·인증·사고 조사 페이지에서 재인용했다.
- **f43**: Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports. 50. 안전 표준·인증·사고 조사 페이지 8절에서 재인용했다.
- **f44**: 윤리적 블랙박스 초안은 사회적 로봇 단위이고, VDA 5050 은 안전 상태·운용 모드를 보고한다. 둘을 플릿 기록으로 잇는 공개 규약은 확인하지 못했다.
- **f45**: 초록 기준: "portability across multiple ROS distributions". 시험 대상은 Mars Curiosity 로버 시뮬레이션이다(LNCS, 2020-12-03).
- **f46**: ROSMonitoring 은 단일 ROS 시스템 대상이다. VDA 5050 구역 위반은 BLOCKED_ZONE_VIOLATION 오류로 보고된다.
- **f47**: ANSI 블로그(2026-09-17)는 위험성평가·기록 유지·교육·안전 작업 절차를, Robotics 24/7(2026-10-04)은 위험성평가·변경 관리·직원 교육·정기 검토와 점검을 든다. 표준 본문은 유료라 열람하지 않았다.
- **f48**: 두 출처 모두 사용자 의무를 들지만 이종 플릿의 이행 주체는 다루지 않는다.
- **f49**: 벤더 주장: 로봇마다 차량 안전 제어기(VSC)를 달고 주파수 도약 무선으로 연결하며, 소규모 시험 운영 단계다. 플릿 관리 시스템·WMS 연동은 언급하지 않는다(A3 게재, 2023-05-18).
- **f50**: VDA 5050 범위와 연결 단절 동작, 그리고 무선 안전 정지 사례(벤더 주장)에서 끌어낸 판단이다. 이 구조를 규정한 표준은 확인하지 못했다.
- **f51**: European Commission AI Act 정책 페이지 기준이다. (재인용: 2026-10-09-08)
- **f52**: 2025-09 초안 기준의 법무법인 해설이며, 확정 고시 원문은 확인하지 못했다. (재인용: 2026-10-09-08)
- **f53**: 고위험 분류 기준과 실행 전 안전 게이트 연구를 함께 본 판단이다.
- **f54**: IBF: 개정 항목에 "cybersecurity and risk assessment"가 포함된다. Hartmann 외(2026-02)는 네트워크 로봇 시스템의 무단 접근 방지 요구가 추가됐다고 분석한다. 조항 번호는 확인하지 못했다(oq-102).
- **f55**: IBF Solutions 2026-09-18 기사 기준이다. 기계류 규정 (EU) 2023/1230 에 따른 조화 여부는 기사에 없다.
- **f56**: Attacking Digital Twins of Robotic Systems to Compromise Security and Safety(arXiv 2211.09507). (재인용: 2026-10-09-07)
- **f57**: ISO 10218(2025) 개정과 ISO/DIS 13482:2024 초안의 새 절에서 끌어낸 판단이다. 플랫폼 명령 경로에 적용한 기준은 확인하지 못했다.
- **f58**: 프리프린트이며, 50. 안전 표준·인증·사고 조사 페이지 5절의 기타 사례에서 재인용했다.
- **f59**: 회답: "'산업용 로봇'을 사용하는 작업으로 한정되지 않습니다." 법원 판결 같은 기속력은 없다(네플라 위키 게재본으로 열람).
- **f60**: 해석은 로봇 범위를 산업용으로 한정하지 않았다. 서빙·배송 로봇 운영 인력에 실제로 적용한 사례는 찾지 못했다.
- **f61**: ANSI 블로그(2026-09-17) 요약 기준이다. 사용자가 IMR, 적용 또는 운영 환경을 바꾸면 같은 의무가 적용된다.
- **f62**: R15.08-3 의 변경 관리 요구와 VDA 5050 의 관제 측 구역·지도 설정에서 끌어낸 판단이다. 이 설정 변경이 법적으로 '변경'에 해당하는지는 확인하지 못했다.
- **f63**: Principles and Guidelines for Evaluating Social Robot Navigation Algorithms(ACM THRI, arXiv 2306.16740). E. 사물·사람·실시간 상태 페이지 O 절에서 재인용했다.
- **f64**: A3 발표와 The Robot Report 기사는 같은 발표를 다뤄 독립 출처로 보지 않았다. 통합자의 시스템 수준 위험성평가 주체는 oq-096 이다.
- **f65**: 50. 안전 표준·인증·사고 조사 페이지 5절에서 재인용했다. 심사 항목 수는 출처마다 8개와 16가지로 달라 정하지 않는다(oq-186, oq-230).
- **f66**: 2023-07-01 시행본 기준이다. 물류센터 AMR 플릿에도 적용되는지는 oq-097 이다.
- **f67**: Co-design Accessible Public Robots(arXiv 2404.05050). E. 사물·사람·실시간 상태 페이지 P 절에서 재인용했다.
- **f68**: 벤더 주장: 감속 속도·거리 값은 공개되지 않았다(발행일 미확인, 확인일 기준). 49. 사람 근접 안전 페이지 5절에서 재인용했다.
- **f69**: 실제 사고가 아닌 모의 시나리오다. 50. 안전 표준·인증·사고 조사 페이지 5절에서 재인용했다.
- **f70**: 인증기관 페이지(확인일 2026-09-30) 기준이다. 49. 사람 근접 안전 페이지 5절에서 재인용했다. (발행일 미확인, 확인일 기준)

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | high | 2026-10-09 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — Demonstrations of Open-RMF (README) | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/open-rmf/rmf_demos | 예 |
| ref-159 | ISO | ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability | 미확인 | 표준 | medium | 2026-10-09 | https://www.iso.org/standard/86749.html | 예 |
| ref-161 | Abdul Hafez, O., Joerger, M., & Spenko, M. | Quantifying mobile robot localization safety for an EKF-based SLAM estimator: An integrity monitoring approach | 2025-05 | 논문 | medium | 2026-10-09 | https://journals.sagepub.com/doi/10.1177/02783649241287797 | 예 |
| ref-286 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg | 아니오 |
| ref-406 | Open Robotics | Simulation - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-10-09 | https://osrf.github.io/ros2multirobotbook/simulation.html | 아니오 |
| ref-417 | Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab) | Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems | 2026-04 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2604.05427 | 예 |
| ref-470 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 2023-06 | 표준 | medium | 2026-10-09 | https://www.iso.org/standard/83545.html | 예 |
| ref-472 | A3(Association for Advancing Automation) | ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available | 2023-10 | 표준 | medium | 2026-10-09 | https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available | 예 |
| ref-562 | 국가법령정보센터(고용노동부) | 산업안전보건기준에 관한 규칙 제223조(운전 중 위험 방지) | 2023-07-01 | 정부·연구기관 | medium | 2026-10-09 | https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EC%82%B0%EC%97%85%EC%95%88%EC%A0%84%EB%B3%B4%EA%B1%B4%EA%B8%B0%EC%A4%80%EC%97%90%EA%B4%80%ED%95%9C%EA%B7%9C%EC%B9%99/(20230701,00367,20221018)/%EC%A0%9C223%EC%A1%B0 | 예 |
| ref-563 | Belzile, B. 외 | From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment | 2025-02 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2502.20693 | 예 |
| ref-565 | Reliability Engineering & System Safety (저자 미확인) | Collision hazard modeling and analysis in a multi-mobile robots system transportation task with STPA and SPN | 2023 | 논문 | medium | 2026-10-09 | https://www.sciencedirect.com/science/article/abs/pii/S0951832023000534 | 예 |
| ref-567 | Open-RMF (open-rmf/rmf GitHub) | [Feature request]: Fire alarm separation for different fleets · Issue #658 · open-rmf/rmf | 2025-04-04 | 오픈소스 문서 | medium | 2026-10-09 | https://github.com/open-rmf/rmf/issues/658 | 예 |
| ref-621 | European Commission | AI Act \| Shaping Europe's digital future | 미확인 | 정부·연구기관 | medium | 2026-10-09 | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | 예 |
| ref-945 | 산업통상자원부 국가기술표준원 (KDI 경제정보센터 게재) | 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 | 2021-11-11 | 정부·연구기관 | medium | 2026-10-09 | https://eiec.kdi.re.kr/policy/materialView.do?num=220004 | 예 |
| ref-980 | 한국로봇산업진흥원 | 실외이동로봇 운행안전인증 | 미확인 | 정부·연구기관 | medium | 2026-10-09 | https://www.kiria.org/portal/cert/portalCertEstiSafe.do | 예 |
| ref-1076 | Hartmann, D., Hamříková, K., Vysocký, A., Laciok, V., & Bernatík, A. (arXiv) | Evolution of Safety Requirements in Industrial Robotics: Comparative Analysis of ISO 10218-1/2 (2011 vs. 2025) and Integration of ISO/TS 15066 | 2026-02-19 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2602.17822 | 예 |
| ref-1079 | Francis, A., Pérez-D'Arpino, C., Li, C. 외 (ACM Transactions on Human-Robot Interaction, arXiv) | Principles and Guidelines for Evaluating Social Robot Navigation Algorithms | 2023-06-29 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2306.16740 | 예 |
| ref-1080 | Amazon | Ever wonder how people and robots team up on your Amazon order? | 미확인 | 벤더 문서 | low | 2026-10-09 | https://www.aboutamazon.com/news/operations/ever-wonder-how-people-and-robots-team-up-on-your-amazon-order | 예 |
| ref-1081 | Rondoni 외 (Scientific Reports) | Navigation benchmarking for autonomous mobile robots in hospital environments | 2024-08-07 | 논문 | medium | 2026-10-09 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11306802/ | 예 |
| ref-1083 | Kazemi Eskeri, M., Kyrki, V., Baumann, D., & Kucner, T. P. (IROS 2025, arXiv) | Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments | 2025-08-27 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2508.19731 | 예 |
| ref-1084 | The Robot Report | New AMR safety standard available with release of ANSI/A3 R15.08-2 | 2023-10-26 | 기사 | low | 2026-10-09 | https://www.therobotreport.com/new-amr-safety-standard-available-with-release-of-ansi-a3-r15-08-2/ | 예 |
| ref-1116 | IBF Solutions | New standards for industrial robots EN ISO 10218-1 and -2 | 2026-09-18 | 업계 보고서 | medium | 2026-10-09 | https://www.ibf-solutions.com/en/seminars-and-news/news/new-standards-for-industrial-robots-en-iso-10218-1-and-2 | 아니오 |
| ref-1117 | Institute for Standardization of Serbia (ISS) — ISO 프로젝트 정보 | ISO/FDIS 13482 Robotics — Safety requirements for service robots | 미확인 | 표준 | medium | 2026-10-09 | https://iss.rs/en/project/show/iso:proj:83498 | 예 |
| ref-1118 | 산업통상자원부 | 실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시 | 2023-11-17 | 정부·연구기관 | medium | 2026-10-09 | https://www.motir.go.kr/kor/article/ATCL0c554f816/64488/view | 예 |
| ref-1120 | Winfield, A. F. T., van Maris, A., Salvini, P., & Jirotka, M. (arXiv) | An Ethical Black Box for Social Robots: a draft Open Standard | 2022-05-13 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2205.06564 | 예 |
| ref-1121 | Webb, H., Dumitru, M., van Maris, A., Winkle, K., Jirotka, M., & Winfield, A. (Frontiers in Robotics and AI) | Role-Play as Responsible Robotics: The Virtual Witness Testimony Role-Play Interview for Investigating Hazardous Human-Robot Interactions | 2021-06-29 | 논문 | medium | 2026-10-09 | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2021.644336/full | 예 |
| ref-1122 | Sanders, N. E., Sener, E., & Chen, K. B. (Applied Ergonomics 121) | Robot-related injuries in the workplace: An analysis of OSHA Severe Injury Reports | 2024 | 논문 | medium | 2026-10-09 | https://eprints.whiterose.ac.uk/id/eprint/217393/ | 예 |
| ref-1124 | 경향신문 | ‘로봇이 사람을 박스로 인식’ 고성 농산물유통센터서 40대 압착 사망 | 2023-11-08 | 기사 | low | 2026-10-09 | https://www.khan.co.kr/article/202311081103001 | 예 |
| ref-1125 | 경남도민일보 | 오뚜기에스에프 끼임사고, 기본 예방조치 안 지켰다 | 2026-09-29 | 기사 | low | 2026-10-09 | https://www.idomin.com/news/articleView.html?idxno=2015923 | 예 |
| ref-1180 | ILIAD 프로젝트 컨소시엄 (EU Horizon 2020) | Concluding ILIAD | 2021-06 | 정부·연구기관 | medium | 2026-10-09 | https://iliad-project.eu/concluding-iliad/ | 예 |
| ref-1181 | 조선비즈 (이정아, 다음 뉴스 게재) | 로봇과 인간이 공존하는 병원…약 배달 로봇에 길 비켜주고 엘리베이터도 잡아줘 | 2024-07-12 | 기사 | low | 2026-10-09 | https://v.daum.net/v/bc4riunbUE | 예 |
| ref-1214 | Han, H. Z. 외 (Carnegie Mellon University) — CHI '24 | Co-design Accessible Public Robots: Insights from People with Mobility Disability, Robotic Practitioners and Their Collaborations | 2024-04-07 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2404.05050 | 예 |
| ref-1241 | Huck, T. P., Ledermann, C., & Kröger, T. (arXiv; SPCE 2020) | Simulation-based Testing for Early Safety-Validation of Robot Systems | 2020-11-20 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2011.10294 | 예 |
| ref-1242 | Carr, C., Wang, S., Wang, P., & Han, L. (arXiv) | Attacking Digital Twins of Robotic Systems to Compromise Security and Safety | 2022-11-17 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2211.09507 | 예 |
| ref-1249 | Wind River (Engblom, J. 인터뷰, Buchwieser, A.) | Using Simics and Simulation in IEC61508 Safety-Critical Systems – an Interview with Andreas Buchwieser | 2014-11-20 | 벤더 문서 | low | 2026-10-09 | https://www.windriver.com/blog/using-simics-and-simulation-in-iec61508-safety-critical-systems-an-interview-with-andreas-buchwieser | 예 |
| ref-857 | Robey, A., Ravichandran, Z., Kumar, V., Hassani, H., & Pappas, G. J. (University of Pennsylvania, arXiv) | Jailbreaking LLM-Controlled Robots | 2024-10-17 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2410.13691 | 예 |
| ref-700 | Ravichandran, Z., Robey, A., Kumar, V., Pappas, G. J., & Hassani, H. (arXiv) | Safety Guardrails for LLM-Enabled Robots | 2025-03-10 | 논문 | medium | 2026-10-09 | https://arxiv.org/abs/2503.07885 | 예 |
| ref-1341 | 법무법인 태평양(BKL) AI팀 | AI기본법 가이드라인 해설 시리즈 (4) 고영향 인공지능사업자의 책무 관련 고시 및 가이드라인 | 2025-09-30 | 업계 보고서 | medium | 2026-10-09 | https://www.bkl.co.kr/law/insight/newsletter/6248 | 예 |
| ref-1419 | ANSI (American National Standards Institute) Blog | ANSI/A3 R15.08-3-2026: Industrial Mobile Robot Applications | 2026-09-17 | 표준 | medium | 2026-10-09 | https://blog.ansi.org/?p=190868 | 아니오 |
| ref-1420 | A3(Association for Advancing Automation) | ANSI/A3 R15.08-3-2026, American National Standard for Industrial Mobile Robots – Safety Requirements – Part 3: Use of IMR Applications | 2026-04-23 | 표준 | medium | 2026-10-09 | https://www.automate.org/store/products/ansi-a3-r15-08-3-2026-american-national-standard-for-industrial-mobile-robots-safety-requirements-part-3-use-of-imr-applications-pdf-download | 아니오 |
| ref-1421 | Robotics 24/7 | A3 announces R15.08 Part 3 safety standard for industrial mobile robot users is now available | 2026-10-04 | 기사 | medium | 2026-10-09 | https://www.robotics247.com/article/a3-announces-r15.08-part-3-safety-standard-for-industrial-mobile-robot-users-is-now-available | 아니오 |
| ref-1422 | FORT Robotics (A3 Case Studies 게재) | Case Study: Wireless E-Stopping Improves Safety Around Warehouse AMRs | 2023-05-18 | 벤더 문서 | low | 2026-10-09 | https://www.automate.org/robotics/case-studies/case-study-wireless-e-stopping-improves-safety-around-warehouse-amrs | 아니오 |
| ref-1423 | 법제처 (네플라 위키 게재본) | [법제처 유권해석] 유해하거나 위험한 작업에 필요한 안전보건교육을 추가로 해야 하는 '로봇작업'이 '산업용 로봇을 사용하는 작업'으로 한정되는지 여부(산업안전보건법 시행규칙 별표 5 제1호라목 등 관련) | 2023-11-21 | 정부·연구기관 | medium | 2026-10-09 | https://www.nepla.ai/wiki/근로-직업과-자격/산업안전-중대재해/-유권해석-산업안전보건법-시행규칙-별표-5-안전보건교육-교육대상별-교육내용-제26조제1항-등-관련/-법제처-유권해석-유해하거나-위험한-작업에-필요한-안전보건교육을-추가로-해야-하는-로봇작업-이-산업용-로봇을-사용하는-작업-으로-한정되는지-여부-산업안전보건법-시행규칙-별표-5-제1호라목-등-관련-zr592w1xv96k | 아니오 |
| ref-1424 | 메트로신문 (한용수) | 보도·횡단보도 걷는 배달·순찰 로봇 나온다… 실외이동로봇 시대 개막 | 2023-11-16 | 기사 | medium | 2026-10-09 | https://www.metroseoul.co.kr/article/20231116500208 | 아니오 |
| ref-1425 | DIN Media | DIN EN ISO 13482 - 2024-10 (Draft standard) Robotik - Sicherheitsanforderungen für Serviceroboter (ISO/DIS 13482:2024) | 2024-10 | 표준 | medium | 2026-10-09 | https://www.dinmedia.de/de/norm-entwurf/din-en-iso-13482/384079303 | 아니오 |
| ref-1426 | Ferrando, A., Cardoso, R. C., Fisher, M., Ancona, D., Franceschini, L., & Mascardi, V. (University of Manchester research portal; LNCS) | ROSMonitoring: A Runtime Verification Framework for ROS | 2020-12-03 | 논문 | medium | 2026-10-09 | https://research.manchester.ac.uk/en/publications/rosmonitoring-a-runtime-verification-framework-for-ros/ | 아니오 |

### 출처 요약

- **ref-004**: 원문 미열람. 작업·교통 조율, 플릿 어댑터, 긴급 작업의 우선 협상 구조를 설명한다.
- **ref-031**: VDA 5050 3.0.0 명세 원문이다. 범위 절의 안전 표준 아님 선언, 구역 유형(BLOCKED·SPEED_LIMIT), 연결 단절 동작, 운용 모드, 안전 상태(activeEmergencyStop·fieldViolation)를 확인했다.
- **ref-104**: 원문 미열람. Open-RMF 데모 세계와 비상 경보 시 주차 동작을 설명한다.
- **ref-159**: 원문 미열람. 산업용 이동로봇 통신·상호운용성 표준으로, 안전 요구는 범위에서 뺀다(D. 공간·지도 모델 페이지 기준).
- **ref-161**: 원문 미열람. 무결성 위험 지표로 SLAM 위치추정의 안전성을 정량화한 IJRR 논문이다.
- **ref-286**: 원문 미열람. 승강기 상태 메시지로 층·문·운행 상태와 모드(사람·AGV·화재·오프라인·비상)를 담는다.
- **ref-406**: 원문 미열람. Open-RMF 시뮬레이션의 문·승강기 플러그인, crowdsim 군중 시뮬레이션을 설명한다.
- **ref-417**: 원문 미열람. 언어 모델이 제어하는 로봇에 실행 전 안전 게이트와 작업 안전 계약을 두는 방법을 다룬다.
- **ref-470**: 원문 미열람. 무인 산업 차량과 그 시스템의 안전 요구·검증 표준이며 운용 구역 준비를 부속서 A 에 둔다.
- **ref-472**: 원문 미열람. R15.08-2(산업용 이동로봇 시스템·적용 안전) 발행 발표다.
- **ref-562**: 원문 미열람. 산업용 로봇 운전 중 위험 방지 조치와 표준 부합 시 방책 생략 규정이다.
- **ref-563**: 원문 미열람. 이동로봇 안전 표준을 검토하고 건설 현장 배치 전 위험성평가 틀을 제안한 프리프린트다.
- **ref-565**: 원문 미열람. 다중 이동로봇 운반 작업의 충돌 위험원을 STPA 와 SPN 으로 분석했다.
- **ref-567**: 원문 미열람. 화재경보 비상 신호가 플릿을 구분하지 않는 문제를 제기한 기능 요청이다.
- **ref-621**: 원문 미열람. EU AI Act 의 위험 기반 분류와 고위험 AI 기준을 설명하는 정책 페이지다.
- **ref-945**: 원문 미열람. 이동 로봇의 엘리베이터 탑승 안전 요구사항 KS B 7317 제정 보도다.
- **ref-980**: 원문 미열람. 실외이동로봇 운행안전인증의 대상·심사항목·정기점검 안내 페이지다.
- **ref-1076**: 원문 미열람. ISO 10218 2011판과 2025판을 비교하며 사이버보안·무단 접근 방지 요구가 늘었다고 분석한다.
- **ref-1079**: 원문 미열람. 사회적 로봇 내비게이션 평가 원칙·지침이다.
- **ref-1080**: 원문 미열람. 풀필먼트 센터의 로보틱스 테크 조끼와 로봇 감속·정지를 설명하는 업체 글이다.
- **ref-1081**: 원문 미열람. 모의 병원 환경에서 병원 물류 로봇의 주행 속도별 성능을 비교한 연구다.
- **ref-1083**: 원문 미열람. 사람과 함께 쓰는 환경에서 사람을 고려한 다중 로봇 작업 배정을 다룬다.
- **ref-1084**: 원문 미열람. R15.08-2 발행과 통합자·사용자 역할을 전한 기사다.
- **ref-1116**: ISO 10218-1/-2:2025 개정 항목(사이버보안 포함)과 EN ISO 판 참조의 EU 관보 등재(2026-09-07, 기계류 지침 조화)를 전한다.
- **ref-1117**: 원문 미열람. ISO 13482 개정 프로젝트의 FDIS 단계 정보다.
- **ref-1118**: 원문 미열람. 실외이동로봇 운행안전인증 절차·기준 고시다.
- **ref-1120**: 원문 미열람. 사회적 로봇 사고 조사를 위한 윤리적 블랙박스 개방 표준 초안이다.
- **ref-1121**: 원문 미열람. 모의 사고를 역할극 증언 면담으로 조사하는 방법을 시험했다.
- **ref-1122**: 원문 미열람. OSHA 중대 부상 보고로 작업장 로봇 관련 부상을 분석했다.
- **ref-1124**: 원문 미열람. 농산물유통센터 로봇 점검 중 압착 사망 사고 보도다.
- **ref-1125**: 원문 미열람. 식품 공장 적재 로봇 점검 중 끼임 사망 사고와 잠금·표지 미실시 지적 보도다.
- **ref-1180**: 원문 미열람. 창고 자율 지게차가 학습한 사람 흐름에 맞춰 경로를 계획한 EU 프로젝트 정리다.
- **ref-1181**: 원문 미열람. 병원의 배달 로봇 경로 표시와 혼잡 대응 보도다.
- **ref-1214**: 원문 미열람. 이동장애인과 로봇 실무자의 공공 로봇 접근성 공동설계 연구다.
- **ref-1241**: 원문 미열람. 시뮬레이션에서 고위험 사람 행동을 생성해 로봇 셀 위험을 찾는 방법이다.
- **ref-1242**: 원문 미열람. 로봇 디지털 트윈에 대한 중간자 공격이 물리 로봇 실패로 이어짐을 보고했다.
- **ref-1249**: 원문 미열람. IEC 61508 맥락에서 시뮬레이션 활용을 다룬 업체 인터뷰다.
- **ref-857**: 원문 미열람. 언어 모델 제어 로봇 탈옥 알고리즘 RoboPAIR 를 제시했다.
- **ref-700**: 원문 미열람. 언어 모델 로봇용 안전 가드레일 RoboGuard 를 제안했다.
- **ref-1341**: 원문 미열람. 고영향 인공지능사업자 책무 고시·가이드라인 초안 해설이다.
- **ref-1419**: R15.08-3 의 범위(유형 A·B·C, 지상 이동 로봇)와 사용자 의무(위험성평가·기록 유지·배치 후 변경 때의 적용·교육·안전 작업 절차)를 요약한 ANSI 블로그 글이다. 표준 본문은 유료라 열람하지 않았다.
- **ref-1420**: A3 판매 페이지다. 발행일 2026-04-23, 77쪽이며 사용자의 위험성평가와 변경 관리를 다룬다고 소개한다. 본문은 열람하지 않았다.
- **ref-1421**: A3·ANSI 의 R15.08-3 공개 발표를 전한 기사다. 위험성평가·변경 관리·직원 교육·정기 검토와 점검을 사용자 의무로 든다.
- **ref-1422**: 창고 울타리 구역 AMR 에 무선 안전 비상정지(ISO 13849 범주 3·PLd 설계 주장)를 적용한 업체 사례 소개다.
- **ref-1423**: 법제처 법령해석 23-0872 의 질의·회답·이유 게재본이다. 로봇작업 특별교육 대상이 산업용 로봇 작업으로 한정되지 않는다고 회답했다. 법제처 원문 사이트에서는 열지 않았다.
- **ref-1424**: 2023-11-17 개정 지능형로봇법 시행에 따른 실외이동로봇 보도 통행, 운행안전인증 대상, 운영자 보험 의무, 손해보장사업 실시기관 지정을 전한 기사다.
- **ref-1425**: ISO 13482 개정 초안 소개다. 로봇 유형별 구조로 바꾸고 탑승형 절을 뺐으며, 사이버보안·데이터 보호·승강기 협동 로봇(부속서 H) 절을 새로 넣었다. 초안 본문은 열람하지 않았다.
- **ref-1426**: ROS 응용의 형식 속성을 외부에서 명세해 실행 중에 검증하는 런타임 검증 틀이다. 초록만 확인했다.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/safety/index.md | 5. 다른 대분류와의 연결 | category_link: '다른 대분류와의 연결' 절만 patches 로 채운다. 대분류별 finding — A. 기획·사업: f1·f2(2, oq-096), f3(1), f4·f5(3, 실외 보험) / B. 로봇 온톨로지: f6·f7(6, 실행 시점 조건에 운용 모드·안전 상태), f8(4) / C. 채팅 기반 구성·운영: f9(12), f10·f11·f12(13), 분류 원문 C 주석 '사람이 확인·승인한 계획만 실행'과 함께 / D. 공간·지도 모델: f13·f14·f15(16, oq-229), f16(15, oq-170), f17(15, 연계 대상) / E. 사물·사람·실시간 상태: f18·f19(18), f20·f21(19) / F. 연동: f22·f23·f24(22, oq-254), f25(20), f26·f27(21) / G. 계획·최적화: f28(25), f29(28), f30·f31(27) / H. 실행·협업·예외 복구: f32·f33(29·31, oq-095), f34(32), f35·f36·f37(32·40) / I. 설계·시뮬레이션: f38(34·36), f39·f40(34), f41(36, 연계 대상) — 가정한 미래 실험 쪽이며 18. 실시간 세계 상태·데이터 일관성의 현재 상태 표현(f18·f19)과 구분 / J. 현장 운영·관제: f42·f44(37, oq-252), f43·f45·f46(38), f47·f48(40, oq-265) / K. 플랫폼 아키텍처·인프라: f49(벤더 주장)·f50(42, oq-095) / L. AI·학습 기술: f51·f52·f53(47, oq-106) / N. 보안·개인정보: f54·f57(51·52, oq-102), f56(52), f23·f57(53) / O. 검증·도입·수명주기: f45·f63(54), f58(55), f52·f59·f60(56, oq-275), f61·f62(57, oq-093·oq-282) / P. 거버넌스·법규·사회: f2·f64(58), f4·f55·f65·f66(59), f67(60) / Q. 현장 유형별 적용: f36·f49·f68(61 물류창고), f35(62 제조 공장), f20·f40(63 병원·의료), f39(64 상업 시설, 시뮬레이션 예제), f69(65 가정·공동주택), f4·f67·f70(66 실외), f58(67 기타 현장). 벤더 주장 f49·f68 은 [추정]과 '벤더 주장'을 병기하고, 연계 대상 f17·f41 과 로봇 자체 안전 기능·승강기 모드 제어·SLAM 은 '연계 대상'으로 짧게 쓴다. 상호운용 규격(VDA 5050·ISO 21423)은 안전 표준이 아니라는 점(f13·f26)을 유지한다. 아직 다루지 않은 연결: 23. 업무 시스템 연동, 30. 로봇 간 협업·물리적 인계, 39. 운영 성과 측정·개선, 41. 플랫폼 아키텍처·외부 API, 43. 데이터·관측성·배포, 46. 예측·학습 기반 최적화, 64. 상업 시설의 실제 현장 사례. 다음 실행 후보: 48. 안전·위험 관리(이전 분류 기준) 10절에 f32·f33·f47·f61·f54 반영. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 변경 관리 | Management of Change (MOC) | 설비·적용·운영 환경이나 설정을 바꿀 때 그 변경이 만드는 위험을 다시 평가하고 기록·승인하는 절차로, ANSI/A3 R15.08-3 이 산업용 이동로봇 사용자에게 요구하는 항목 가운데 하나다. |
| 안전 상태 보고 | Safety State (VDA 5050 safetyState) | VDA 5050 상태 메시지에서 로봇이 활성 비상정지의 종류(MANUAL·REMOTE·NONE)와 보호 필드 침범 여부(fieldViolation)를 관제에 알리는 항목이다. |
| 무선 안전 비상정지 | Wireless Safety-rated Emergency Stop | 관제 통신과 별도의 안전 등급 무선 경로로 여러 이동로봇을 한꺼번에 멈추게 하는 비상정지 방식이다. |

## 열린 질문

새로 생긴 질문:

- 관제 통신과 독립된 안전 등급 무선 비상정지(플릿 일괄 정지)를 제조사가 다른 이동로봇 플릿에 적용한 사례가 있으며, 그 정지 결과를 오케스트레이션 플랫폼이 상태로 받아 작업 보류·재배정에 쓰는 인터페이스가 정해져 있는가? | 관련 영역: 48. 안전·위험 관리, 42. 분산 시스템·통신·컴퓨팅 구조, 29. 명령·작업 실행의 신뢰성 | 근거: f49 | 종류: 일반
- ISO 13482 개정 초안(ISO/DIS 13482:2024)의 승강기 협동 로봇 요구(부속서 H)는 국내 KS B 7317 과 어떻게 대응하며, 이 요구가 최종판에 남았는가? | 관련 영역: 50. 안전 표준·인증·사고 조사, 22. 설비·건물 시스템 연동 | 근거: f23 | 종류: 일반
- 진입 금지 구역 위반이나 정지 지시 뒤 응답 같은 안전 관련 운영 규칙을 런타임 검증으로 감시하는 방법을 제조사가 다른 이동로봇 플릿에 적용해 효과를 측정한 연구나 제품이 있는가? | 관련 영역: 48. 안전·위험 관리, 38. 모니터링·이상 탐지·원인 분석, 54. 시험·형식 검증·벤치마크 | 근거: f46 | 종류: 일반
- 실외이동로봇의 운행안전인증 단위에 관제장치가 포함될 때, 관제를 맡는 오케스트레이션 플랫폼 사업자도 지능형로봇법의 운영자 보험 가입 의무 대상이 되는가? | 관련 영역: 59. 법·규제·보험·라이선스, 58. 다사업자 책임·계약·데이터, 66. 실외 | 근거: f5 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 48 · 교차 확인: 2
- 예산 사용량: 검색 11회 · 신규 출처 8건
- 미확인 항목:
    - EU 기계류 규정 (EU) 2023/1230 원문(ref-555)을 EUR-Lex 에서 두 번 열었으나 빈 본문이 돌아와 실질적 변경 정의·부속서 III 1.1.9 를 확인하지 못함(finding 으로 내지 않음)
    - Intertek 의 'EN ISO 13482:2026' 표기는 페이지가 403 으로 열리지 않아 쓰지 않음(ref-1117 의 FDIS 단계와 충돌 가능성 미확인)
    - 대한민국 정책브리핑(ref-991)은 ECONNRESET 으로 열지 못해 보험 의무 교차 확인 실패(f4 단일 출처)
    - 법무법인 지평 PDF 는 본문 추출 실패로 쓰지 않음
    - f49·f68 벤더 주장은 독립 출처로 확인하지 못함
    - f3 의 R15.08-3 발행일은 A3 판매 페이지 기준(2026-04-23)이며, 공개 발표(2026-10-04)와 날짜가 다름
    - ISO 10218-1:2025 사이버보안 요구의 조항 번호는 확인하지 못함(oq-102)
    - 산업안전보건법 시행규칙 별표 5 로봇작업 특별교육의 교육 내용·시간은 확인하지 못함
    - 재사용 출처 40건은 이번 실행에서 다시 열지 않음
- 범위 경계 위반 의심:
    - f17: SLAM 위치추정 안전성은 원문 19장 '로봇 자체 지능·제어' 경계라 claim 을 '연계 대상: '으로 시작
    - f41: 기능안전 인증과 시뮬레이션 인정은 인증 기관·제조사 몫이라 '연계 대상: '으로 시작
    - f18·f19·f22·f24: 승강기 모드 제어와 탑승 안전은 시설·설비 제어 경계의 연계 대상이며, ROP 는 확인·요청 범위로만 서술
    - f9~f12·f32·f49: 비상정지 회로·보호 필드·무선 안전 정지 같은 안전 기능은 로봇 제조사·통합자 몫의 연계 대상이며, ROP 는 상태 수신과 작업 보류·재개로만 서술
    - f4·f5·f55·f59·f65·f66: 법령 해석과 적용 판단은 운영 사업자·법무 몫이며, ROP 는 인증·운행 조건을 제약으로 반영하는 범위로만 연결
- 한계: web_fetch_available: true · fetch_mode full. 대분류 연결(category_link) 실행이다. 근거는 먼저 게시된 48·49·50 페이지와 A·B·D·E·F·G 대분류 페이지, 이전 브리프(2026-10-09-07, 2026-10-09-08)의 검증된 주장에서 찾고 재사용 출처 id 를 썼다(재사용 40건, 이번에 다시 연 것은 ref-031(github_raw)·ref-1116(webfetch) 2건이고 나머지 38건은 fetched false·source_unopened true). 신규 출처는 8건(ref-1419~ref-1426, 예약 구간 안)이고 모두 원문 페이지를 열었다. 다만 ref-1419·ref-1420·ref-1425 는 유료 표준의 공식 소개 자료여서 표준 본문은 보지 못했다. 검색 11회/30, 신규 출처 8건/15. 교차 확인 2건(f47 R15.08-3 사용자 의무, f54 ISO 10218 사이버보안). 벤더 주장 2건(f49·f68). 한국 자료: 신규 ref-1423(법제처 해석)·ref-1424(기사), 재사용 ref-562·ref-945·ref-980·ref-1118·ref-1124·ref-1125·ref-1181·ref-1341. 현장 유형: 물류창고·제조 공장·병원·상업 시설(시뮬레이션 예제)·가정·실외·기타 각 1건 이상이며, 상업 시설의 실제 현장 사례는 찾지 못했다. 18. 실시간 세계 상태·데이터 일관성(현재 상태, f18·f19)과 34. 시뮬레이션·예측용 디지털 트윈(가정한 미래, f38·f39)을 구분했다. 분류 원문 교차 규칙에 해당하는 L. AI·학습 기술 연결(f51~f53)은 적용 대상인 48. 안전·위험 관리와 함께 제안했다. 열린 질문 가운데 oq-095(f32·f33·f50), oq-254(f23·f24, 초안 기준), oq-265(f47·f48, 이행 주체 미확인), oq-275(f59·f60, 지침 미확인), oq-102(f54, 조항 미확인), oq-229(f15)에는 부분 근거만 더했고 해결 제안은 없다. 대분류 페이지 절 번호는 제목 순서(핵심 질문·개요·세부 연구영역·핵심 포인트·다른 대분류와의 연결)를 따라 '5'로 매겼다 [가정]. 정정 요청 없음. 우선 지정 질문 없음. 입력 누락 없음.
