# 리서치 브리프 2026-09-25-73

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-73 |
| 날짜 | 2026-09-25 |
| 실행 유형 | category_link (대분류 연결) |
| 대상 영역 | 해당 없음 |
| 대분류 | G. 안전·보안·지능·거버넌스 |

## 갭(비어 있거나 약한 섹션)

- G. 안전·보안·지능·거버넌스 대분류 페이지의 '다른 대분류와의 연결' 절이 '아직 작성되지 않음' 상태
- C. 연결·실행 기반 페이지가 27. AI·학습·적응과 모델 운영과의 연결을 '근거 없음'으로 두었음(이번 실행에서 보강 후보를 냄)
- A. 업무·공급망 설계 페이지가 25. 안전·위험 관리, 26. 사이버보안·접근권한·개인정보, 27. AI·학습·적응과 모델 운영과의 연결을 아직 다루지 않았음
- E. 협업·현장 운영 페이지가 26. 사이버보안·접근권한·개인정보와의 연결을 '근거 없음'으로 두었음(이번 실행에서 보강 후보를 냄)
- F. 도입·검증·유지관리 쪽 24. 자산·소프트웨어 수명주기 관리 ↔ 27. AI·학습·적응과 모델 운영(모델 버전 관리) 연결이 어느 대분류 페이지에도 없음

## 조사 질문

1. 전체 영역에 어떤 공통 제약과 관리 체계를 적용할 것인가? [분류원문]
2. 25. 안전·위험 관리는 C. 연결·실행 기반·D. 계획·최적화·E. 협업·현장 운영의 어느 세부영역에 어떤 안전 상태·구역·비상 신호로 제약을 거는가, 그리고 ROP 몫과 연계 대상의 경계는 어디인가?
3. 26. 사이버보안·접근권한·개인정보는 9. 로봇·제조사 관제 연동, 10. 설비·건물 시스템 연동, 13. 작업 배정 — MRTA, 18. 사람–로봇 협업·운영 인터페이스, 24. 자산·소프트웨어 수명주기 관리와 어떤 권한·인증서·패치·영상 데이터로 이어지는가?
4. 27. AI·학습·적응과 모델 운영은 분류 원문 8장 교차 규칙의 적용 대상(5. 로봇 능력·작업 온톨로지, 6. 지도·공간·위치 모델, 13. 작업 배정 — MRTA, 19. 모니터링·이상 탐지·원인 분석, 21. 온보딩·설정·현장 시운전) 외에 C. 연결·실행 기반·F. 도입·검증·유지관리와 무엇으로 이어지는가? (C. 연결·실행 기반 페이지의 '근거 없음' 갭 겨냥)
5. 28. 표준·상호운용성·다사업자 거버넌스는 1. 주문·업무 시스템 연계, 9. 로봇·제조사 관제 연동, 15. 다중 로봇 경로·교통 관리 — MAPF, 19. 모니터링·이상 탐지·원인 분석, 23. 시험·형식 검증·벤치마크, 24. 자산·소프트웨어 수명주기 관리에 어떤 표준·판·책임 문제를 넘겨받는가?
6. 게시된 다른 대분류 페이지(A~F)의 G. 안전·보안·지능·거버넌스 쪽 연결 서술 가운데 G 쪽 세부영역 근거로 다시 확인·보강할 것은 무엇인가?

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [추정] | G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스 ↔ A. 업무·공급망 설계의 1. 주문·업무 시스템 연계: ISA-95 계열 작업 지시 동사·메서드(B2MML CHANGE·CANCEL, OPC UA for ISA-95 Job Control)와 VDA 5050·Open-RMF 주문·작업 요청을 잇는 표준 매핑이 확인되지 않아, 번역 규칙의 소유와 변경 승인이 거버넌스 과제로 넘어갈 것으로 보인다. | ref-129, ref-130, ref-031, ref-125 | 아니오 | low | 2026-09-25 | — | — |
| f2 | [추정] | G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스 ↔ A. 업무·공급망 설계의 1. 주문·업무 시스템 연계: 상위 업무 시스템에 여는 ROP API 의 판 번호·폐기 예고 정책은 ROP 몫으로 보이며, 의미적 버전 관리(SemVer 2.0.0)와 RFC 9745 Deprecation 헤더가 그 규칙의 후보가 된다. | ref-635, ref-706 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f3 | [추정] | G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영 ↔ A. 업무·공급망 설계의 1. 주문·업무 시스템 연계: 주문·납기 제약을 받는 배정·계획 모델의 버전·변경 승인은 ROP 몫이고, 수요예측 모델은 분류 원문 9장 상위 업무 시스템 경계의 연계 대상으로 보인다. | ref-626, ref-618 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f4 | [사실] | G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영 ↔ B. 공통 정보·환경 모델의 5. 로봇 능력·작업 온톨로지: 대규모 언어 모델로 능력 온톨로지를 생성하는 연구(2024-04)와 로봇 기술 파일(URDF)에서 로봇 온톨로지를 LLM 으로 채우는 연구(2026-06)가 있어, 분류 원문 8장의 매뉴얼 해석 교차 규칙이 두 대분류를 잇는다. | ref-238, ref-239 | 아니오 | medium | 2026-06 | — | 원문 미열람 |
| f5 | [사실] | G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영 ↔ B. 공통 정보·환경 모델의 6. 지도·공간·위치 모델: 비전 언어 모델로 평면도 지도를 해석하는 연구(2024-09)가 있어, 분류 원문 8장 교차 규칙의 도면 해석이 두 대분류를 잇는다. | ref-076 | 아니오 | medium | 2024-09 | — | 원문 미열람 |
| f6 | [사실] | G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스 ↔ B. 공통 정보·환경 모델의 5. 로봇 능력·작업 온톨로지: 무인운반차 기술 데이터 서브모델 IDTA 02047, 서비스 로봇 모듈 공통 정보 모델 ISO 22166-201(2024-02), 국내 KS B 7321-2 같은 제조사 독립 정보 모델 표준이 있다. | ref-234, ref-240, ref-138 | 아니오 | medium | 2024-02 | — | 원문 미열람 |
| f7 | [사실] | G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스 ↔ B. 공통 정보·환경 모델의 6. 지도·공간·위치 모델: ISO 21423 은 산업용 이동로봇의 통신·상호운용성을 다루는 국제표준이며, 그 공통 좌표계와 제조사 지도 식별자의 대응은 확인되지 않았다. | ref-159 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f8 | [추정] | G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ B. 공통 정보·환경 모델의 8. 실시간 세계 상태·데이터 일관성: Open-RMF 승강기 상태의 운영 모드에 사람·AGV·화재·오프라인·비상이 있으므로, 탑승 확정 전에 최신 모드를 확인하는 규칙이 안전 조건과 맞물릴 것으로 보이며, 설비 안전 제어 자체는 연계 대상이다. | ref-286 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f9 | [사실] | G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ C. 연결·실행 기반의 10. 설비·건물 시스템 연동: 국가기술표준원은 2021-11 이동 로봇의 엘리베이터 탑승 안전 요구사항과 평가 방법을 정한 KS B 7317 을 제정했고, Open-RMF 승강기 상태의 운영 모드에는 화재·비상이 포함된다. | ref-314, ref-315, ref-286 | 아니오 | medium | 2021-11 | — | 원문 미열람 |
| f10 | [사실] | G. 안전·보안·지능·거버넌스의 26. 사이버보안·접근권한·개인정보 ↔ C. 연결·실행 기반의 9. 로봇·제조사 관제 연동·11. 분산 시스템·통신·컴퓨팅 구조: ROS 2 는 DDS 보안 규격의 인증·접근통제·암호화 플러그인을 쓰고, Open-RMF 는 같은 신원과 접근통제 규칙을 공유하는 SROS 2 인클레이브로 구성요소 권한을 나누며 웹 대시보드에는 TLS 와 OpenID Connect 기반 역할 토큰을 쓴다. | ref-009, ref-405 | 아니오 | medium | 2026-09-25 | — | — |
| f11 | [사실] | G. 안전·보안·지능·거버넌스의 26. 사이버보안·접근권한·개인정보 ↔ C. 연결·실행 기반의 9. 로봇·제조사 관제 연동: VDA 5050 3.0.0 은 MQTT 용 TLS 자격증명을 내려받는 사전 정의 동작 updateCertificate 를 두고, 내려받기도 TLS 로 보호하고 인증서 체인을 검증하도록 권하므로, 인증서 교체가 관제 연동 경로를 거치는 보안 명령이 된다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f12 | [사실] | G. 안전·보안·지능·거버넌스의 26. 사이버보안·접근권한·개인정보 ↔ C. 연결·실행 기반의 9. 로봇·제조사 관제 연동: ROS 2 위협 모델 초안은 기본 사용자명·암호가 설정된 이미지의 SSH 접속을 진입점으로 들고, CISA 권고(ICSA-21-280-02)는 MiR 차량과 플릿 소프트웨어 취약점으로 로봇 제어와 서비스 거부가 가능하다고 보고했다. | ref-010, ref-583 | 아니오 | medium | 2021-01 | — | — |
| f13 | [추정] | G. 안전·보안·지능·거버넌스의 26. 사이버보안·접근권한·개인정보 ↔ C. 연결·실행 기반의 10. 설비·건물 시스템 연동: 로봇 관제가 문·승강기 어댑터에 요청을 보내는 구조에서는 어느 관제 구성요소가 어떤 설비 명령을 낼 수 있는지를 인클레이브·권한 파일 같은 접근통제 단위로 정해야 할 것으로 보이며, 공개 구성·사례는 확인되지 않았다. | ref-405, ref-283, ref-284 | 아니오 | low | 2026-09-25 | — | — |
| f14 | [사실] | G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ C. 연결·실행 기반의 12. 명령·작업 실행의 신뢰성: VDA 5050 3.0.0 상태 메시지의 safetyState 는 비상정지 종류(eStop)와 보호 필드 침범(fieldViolation)을 보고하며, 명세는 스스로 기능·운영·시스템 안전 요구를 정하지 않고 안전 표준으로 적용해서는 안 된다고 밝힌다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f15 | [추정] | G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ C. 연결·실행 기반의 12. 명령·작업 실행의 신뢰성: ROP 는 로봇이 보고한 안전 상태가 해제되고 운용 모드가 자동으로 돌아온 뒤 재개를 지시하는 운영 조율을 맡고, 정지·재개 지시를 확실하게 전달하는 문제가 12. 명령·작업 실행의 신뢰성과 맞물리는 것으로 보인다. | ref-031 | 아니오 | low | 2026-09-25 | 피킹 / 제약 | — |
| f16 | [사실] | G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스 ↔ C. 연결·실행 기반의 9. 로봇·제조사 관제 연동: VDA 5050 3.0.0 은 경로 계산·교착 해소·교통 관리를 관제 기능으로, 위치 추정과 주문 실행을 이동로봇 기능으로 나누며, 제조사 중립 연동의 기준으로 VDA 5050 외에 MassRobotics AMR 상호운용 표준과 ISO 21423 이 있다. | ref-031, ref-253, ref-159 | 아니오 | medium | 2026-09-25 | — | — |
| f17 | [추정] | G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스 ↔ C. 연결·실행 기반의 9. 로봇·제조사 관제 연동: 확인한 VDA 5050 적합성 시험 근거가 제3자 오픈소스 도구와 벤더 발표뿐이라, 어느 시험 결과를 연동 승인 기준으로 삼고 누가 연동 오류를 판정할지가 거버넌스 과제로 넘어갈 것으로 보이며, 공식 인증 절차의 부재는 확정되지 않았다. | ref-407, ref-408, ref-608, ref-031 | 아니오 | low | 2026-09-25 | — | — |
| f18 | [추정] | G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스 ↔ C. 연결·실행 기반의 10. 설비·건물 시스템 연동: 국내에서 로봇 엘리베이터 탑승 KS 가 제정되었고, 대한승강기협회가 엘리베이터와 로봇 연동 단체표준을 제정했다고 기사로 전해져, 설비 연동 표준이 두 대분류를 잇는 것으로 보인다. | ref-709, ref-316, ref-317 | 아니오 | low | 2021-11-11 | — | 원문 미열람 |
| f19 | [사실] | G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영 ↔ C. 연결·실행 기반의 9. 로봇·제조사 관제 연동: 오픈소스 ROS-MCP-Server 는 rosbridge 를 통해 LLM 에게 ROS 토픽 발행·구독, 서비스·액션 호출, 파라미터 설정을 도구로 노출하며, README 는 권한 기능을 앞으로 기여받을 기능으로만 언급한다. | ref-679 | 아니오 | medium | 2026-09-25 | — | — |
| f20 | [추정] | G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영·26. 사이버보안·접근권한·개인정보 ↔ C. 연결·실행 기반의 12. 명령·작업 실행의 신뢰성: LLM 에 저수준 로봇 도구를 직접 열면 명령 상태 관리와 실행 전 검증을 우회할 수 있으므로, ROP 는 검증 경로로 들어가는 상위 도구(작업 요청 제출 등)만 노출해야 할 것으로 보인다. | ref-679, ref-417 | 아니오 | low | 2026-09-25 | 제약 | — |
| f21 | [사실] | G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영 ↔ C. 연결·실행 기반의 12. 명령·작업 실행의 신뢰성: Tang 외(2026-06, 프리프린트)는 산업용 다중 로봇에서 LLM 에이전트의 제안이 결정적 검증과 원자적 반영(atomic commit)을 거쳐야만 실행 상태·자원 잠금 기록에 받아들여지는 구조를 제안했다. | ref-677 | 아니오 | medium | 2026-06 | — | 원문 미열람 |
| f22 | [사실] | G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영 ↔ D. 계획·최적화의 13. 작업 배정 — MRTA: 분류 원문 8장 교차 규칙대로 학습 기반 배차 연구(이종 그래프 어텐션 스케줄러, 창고 강화학습 배정 RTAW)와 LLM 기반 다중 로봇 작업 배정 연구가 두 영역을 잇는다. | ref-399, ref-623, ref-090, ref-168 | 아니오 | medium | 2025-12 | — | 원문 미열람 |
| f23 | [사실] | G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영 ↔ D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF·16. 공용 자원·충전·에너지 최적화: 모방 학습을 적용한 지속형 MAPF 연구(2024-10)와 자율 피킹 로봇의 배터리 관리에 심층 강화학습을 쓰는 연구(2026-07)가 있다. | ref-199, ref-531 | 아니오 | medium | 2026-07 | — | 원문 미열람 |
| f24 | [사실] | G. 안전·보안·지능·거버넌스의 26. 사이버보안·접근권한·개인정보 ↔ D. 계획·최적화의 13. 작업 배정 — MRTA: 2026-08 프리프린트는 위치 스푸핑으로 오염된 에이전트가 롤아웃 기반 다중 로봇 배정·경로 계획의 비용 개선을 없앨 수 있다고 보고 탐지된 적대 에이전트를 이후 계획에서 빼는 방법을 제안했으며, 실험은 GPS 스푸핑 데이터와 택시 수요로 했다. | ref-494 | 아니오 | medium | 2026-08 | — | 원문 미열람 |
| f25 | [사실] | G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF: VDA 5050 3.0.0 은 진입 금지(BLOCKED)·해제(RELEASE)·속도 제한(SPEED_LIMIT)·우선(PRIORITY)·벌점(PENALTY) 같은 구역 유형을 교통 관리 수단으로 정의하되, 안전 표준으로 적용하지 말라고 밝힌다. | ref-031 | 아니오 | medium | 2026-09-25 | 제약 | — |
| f26 | [사실] | G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ D. 계획·최적화의 16. 공용 자원·충전·에너지 최적화: Open-RMF 데모는 비상 경보가 켜지면 로봇들을 가장 가까운 주차 위치로 보내고, 2025-04-04 기능 요청 이슈 기준 비상 신호는 대상 플릿을 구분하지 않는 불리언 값이었다. | ref-104, ref-567 | 아니오 | medium | 2025-04-04 | 출하 / 수행 자원 | 원문 미열람 |
| f27 | [사실] | G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF: Open-RMF 는 긴급 작업을 높은 우선순위 참여자가 교통 협상을 강제하는 방식으로 다룬다. | ref-004 | 아니오 | medium | 2026-09-25 | — | — |
| f28 | [추정] | G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스 ↔ D. 계획·최적화의 15. 다중 로봇 경로·교통 관리 — MAPF: VDA 5050 은 교통 조율 전략을 명세에서 빼고 Open-RMF 는 시스템 통합사가 배치한 판정자가 협상 결과를 고르게 하므로, 한 현장의 우선권 판정 규칙을 누가 정하고 승인하는지가 거버넌스 과제로 넘어갈 것으로 보인다. | ref-031, ref-004 | 아니오 | low | 2026-09-25 | — | — |
| f29 | [사실] | G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ E. 협업·현장 운영의 17. 로봇 간 협업·물리적 인계: ANSI/A3 R15.08-2-2023 은 이동 플랫폼에 로봇팔을 단 모바일 매니퓰레이터를 산업용 이동로봇 유형 C 로 다루며 시스템·적용 단위의 안전 요구를 정한다. | ref-210, ref-472 | 아니오 | medium | 2023-10 | — | 원문 미열람 |
| f30 | [추정] | G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ E. 협업·현장 운영의 17. 로봇 간 협업·물리적 인계·18. 사람–로봇 협업·운영 인터페이스: 사람 감지·보호 필드·비상정지 같은 안전 기능은 제조사·통합사·설비 쪽 연계 대상이고, ROP 는 로봇이 보고한 안전 상태를 표시하고 재개·수동 전환 승인을 작업 흐름에 반영하는 경계로 보인다. | ref-470, ref-051, ref-210 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f31 | [사실] | G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ E. 협업·현장 운영의 18. 사람–로봇 협업·운영 인터페이스(국내): 고용노동부는 2023-07 고정식·이동식 산업용 로봇의 협동작업 안전 가이드를 배포했고, 중소벤처기업부는 2024-11 이동식 협동로봇 안전기준 산업표준 제정을 발표했다. | ref-473, ref-475, ref-561 | 아니오 | medium | 2024-11 | — | 원문 미열람 |
| f32 | [사실] | G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영·25. 안전·위험 관리 ↔ E. 협업·현장 운영의 18. 사람–로봇 협업·운영 인터페이스: LLM 계획기가 불확실할 때 사람에게 되묻는 연구(KnowNo, 2023-07), 사용자 명령의 모호성을 해소하는 연구(CLARA, 2024), 자연어 명령의 실행 전 안전 게이트 연구(SafeGate, 2026-04)가 있다. | ref-351, ref-353, ref-417 | 아니오 | medium | 2026-04 | 피킹 / 시작 조건 | 원문 미열람 |
| f33 | [사실] | G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영 ↔ E. 협업·현장 운영의 19. 모니터링·이상 탐지·원인 분석: Das 외(2021-01)는 로봇 실패 설명을 생성해 사용자의 고장 복구 지원을 개선하는 연구를 발표했으며, 분류 원문 8장 교차 규칙의 장애 분석이 두 대분류를 잇는다. | ref-476 | 아니오 | medium | 2021-01 | — | 원문 미열람 |
| f34 | [추정] | G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스 ↔ E. 협업·현장 운영의 19. 모니터링·이상 탐지·원인 분석: VDA 5050 오류 수준, MassRobotics 운용 상태, Open-RMF 작업 상태가 서로 다른 어휘이고 공통 매핑 표준이 확인되지 않아, 이종 플릿의 오류·원인 범주 해석 규칙을 누가 정하고 바꾸는지가 거버넌스 과제로 넘어갈 것으로 보인다. | ref-051, ref-230, ref-111 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f35 | [사실] | G. 안전·보안·지능·거버넌스의 26. 사이버보안·접근권한·개인정보 ↔ E. 협업·현장 운영의 18. 사람–로봇 협업·운영 인터페이스: 근로자참여 및 협력증진에 관한 법률 제20조는 사업장 내 근로자 감시 설비의 설치를 노사협의회 협의 사항으로 두어, 카메라를 단 로봇이 작업자를 촬영하는 현장에서 영상 수집 조건이 사람–로봇 협업의 제약이 된다. | ref-589, ref-010 | 아니오 | medium | 2026-09-25 | 입고 / 제약 | — |
| f36 | [추정] | G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ E. 협업·현장 운영의 20. 예외 복구·재계획·업무 연속성: 비상 해제 후 어떤 작업을 어떤 순서로 재개할지와 대상 플릿 구분이 출하 마감 준수에 영향을 주므로, 비상 대응 뒤의 재개가 예외 복구 과제로 넘어가는 것으로 보인다. | ref-567, ref-004 | 아니오 | low | 2026-09-25 | 출하 / 예외·성과 | — |
| f37 | [추정] | G. 안전·보안·지능·거버넌스의 26. 사이버보안·접근권한·개인정보 ↔ E. 협업·현장 운영의 20. 예외 복구·재계획·업무 연속성: 출하 마감 중 오류 로봇을 제조사 원격 유지보수로 복구하려 할 때, 대상 로봇·진단 명령만 허용하고 이동 명령은 막으며 세션을 감사 기록으로 남기는 권한 제약이 복구 속도와 맞물릴 것으로 보인다. | ref-010, ref-583, ref-405 | 아니오 | low | 2026-09-25 | 출하 / 제약 | — |
| f38 | [사실] | 연계 대상: G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ F. 도입·검증·유지관리의 21. 온보딩·설정·현장 시운전·23. 시험·형식 검증·벤치마크 — ISO 3691-4:2023 은 무인 산업 차량과 그 시스템의 안전 요구와 검증 수단을 정하고 운용 구역 준비를 부속서 A 에 둔다. | ref-470 | 아니오 | medium | 2023-06 | — | 원문 미열람 |
| f39 | [추정] | G. 안전·보안·지능·거버넌스의 25. 안전·위험 관리 ↔ F. 도입·검증·유지관리의 24. 자산·소프트웨어 수명주기 관리: 업체 가이드가 설비·작업 변경 시 위험성평가를 다시 하도록 권하므로 펌웨어·안전 파라미터·오케스트레이션 정책 변경이 재평가 촉발 조건이 될 수 있어 보이나, 국내 공식 규정은 확인되지 않았다. | ref-559 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f40 | [사실] | G. 안전·보안·지능·거버넌스의 26. 사이버보안·접근권한·개인정보 ↔ F. 도입·검증·유지관리의 24. 자산·소프트웨어 수명주기 관리: IEC TR 62443-2-3:2015 는 산업 자동화·제어 시스템 환경의 패치 관리를 다루고, ROS 2 위협 모델 초안은 빌드 팜·개발자 작업 환경을 통한 공급망 위협에 바이너리 서명과 소스 감사를 완화책으로 든다. | ref-554, ref-010 | 아니오 | medium | 2021-01 | — | — |
| f41 | [사실] | G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영 ↔ F. 도입·검증·유지관리의 21. 온보딩·설정·현장 시운전·23. 시험·형식 검증·벤치마크: 자연어 능력 설명에서 LLM 으로 능력 온톨로지를 생성하는 방법(2024-06)이 제안되었고, ALFRED 와 LoTa-Bench 는 자연어 지시를 행동 계획으로 바꾸는 체화 에이전트를 시뮬레이터 결과로 자동 평가하는 공개 벤치마크다(물류 지시 데이터셋 아님). | ref-465, ref-539, ref-541 | 아니오 | medium | 2024-06 | — | 원문 미열람 |
| f42 | [추정] | G. 안전·보안·지능·거버넌스의 27. AI·학습·적응과 모델 운영 ↔ F. 도입·검증·유지관리의 24. 자산·소프트웨어 수명주기 관리: 24. 자산·소프트웨어 수명주기 관리의 정의가 '모델 버전'과 배포·복구를 포함하므로, 학습 배차 모델 교체를 모델 레지스트리의 버전·별칭과 운영 준비도 시험 기준으로 관리하는 일이 두 대분류를 잇는 것으로 보인다. | ref-626, ref-625 | 아니오 | low | 2026-09-25 | 출하 / 예외·성과 | 원문 미열람 |
| f43 | [사실] | G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스 ↔ F. 도입·검증·유지관리의 22. 시뮬레이션·예측용 디지털 트윈: 제조용 디지털 트윈 프레임워크 ISO 23247 은 국내에 KS X ISO 23247-1 로 등재되어 있고 2026 년 디지털 트윈 결합을 다루는 Part 6 이 발행되었으나, 제조 대상 표준이다. | ref-516, ref-518 | 아니오 | medium | 2026 | — | 원문 미열람 |
| f44 | [추정] | G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스 ↔ F. 도입·검증·유지관리의 23. 시험·형식 검증·벤치마크: 국내에는 로봇 자체 성능 시험(KS B ISO 18646-1, 한국로봇산업진흥원 시험평가)과 소프트웨어 모듈 정보모델 상호운용성 시험 절차(KOROS 1148-8:2025)가 있어, 로봇 성능 시험은 시험기관 쪽이고 ROP 몫은 그 결과를 연동 승인·등록 조건으로 받는 쪽으로 보인다. | ref-606, ref-607, ref-710, ref-466 | 아니오 | low | 2026-09-25 | — | 원문 미열람 |
| f45 | [추정] | G. 안전·보안·지능·거버넌스의 28. 표준·상호운용성·다사업자 거버넌스 ↔ F. 도입·검증·유지관리의 24. 자산·소프트웨어 수명주기 관리: 관제가 VDA 5050 헤더 version 으로 판 차이를 감지하고 로봇이 지원하지 않는 선택 필드는 UNSUPPORTED_PARAMETER 오류로 드러나므로, 펌웨어·프로토콜 판 이행 때 호환 시험과 수정 책임을 누가 지는지가 두 대분류 사이의 과제로 보인다. | ref-031, ref-051, ref-635 | 아니오 | low | 2026-09-25 | 출하 / 예외·성과 | — |

### 근거 발췌

- **f1**: A. 업무·공급망 설계 페이지 G 연결 항목과 같은 근거. 표준 매핑 부재는 조사 범위의 관찰이며 부재 확인은 아님(oq-020). (재인용: 2026-09-25-29)
- **f2**: 28. 표준·상호운용성·다사업자 거버넌스 9절 표 '상위 업무 시스템' 행의 [추정] 주장(ref-635, ref-706). SemVer 는 호환되지 않는 API 변경에 주 버전을 올리게 한다.
- **f3**: 27. AI·학습·적응과 모델 운영 9절 표 '상위 업무 시스템' 행: ROP 는 배정·계획 모델의 버전·변경 승인, 수요예측 모델은 연계 대상.
- **f4**: B. 공통 정보·환경 모델 페이지 G 연결 항목의 [사실] 주장과 같은 각주. 두 연구는 각각 단일 출처. (재인용: 2026-09-25-32)
- **f5**: DeFazio 외, Vision Language Models Can Parse Floor Plan Maps(2024-09). B. 공통 정보·환경 모델 페이지 G 연결 항목과 같은 각주. (재인용: 2026-09-25-32)
- **f6**: B. 공통 정보·환경 모델 페이지 G 연결 항목과 같은 각주. KS 부합화 여부는 oq-004·oq-026 에서 열림. (재인용: 2026-09-25-32)
- **f7**: ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability. 발행 여부·좌표계 정의 미확인(oq-027). (발행일 미확인, 확인일 기준)
- **f8**: LiftState.msg 운영 모드 값(HUMAN·AGV·FIRE·OFFLINE·EMERGENCY). B. 공통 정보·환경 모델 페이지 G 연결 항목과 같은 주장. (재인용: 2026-09-25-32)
- **f9**: C. 연결·실행 기반 페이지 G 연결 항목과 같은 각주. 승강기 탑승 안전과 설비 안전 제어 자체는 분류 원문 9장 시설·설비 제어 경계의 연계 대상. (재인용: 2026-09-25-38)
- **f10**: Open-RMF 보안 문서: "An 'enclave' is a process or group of processes that will share the same identity and access control rules." 대시보드는 TLS·OIDC(Keycloak), 역할별 ID 토큰.
- **f11**: VDA 5050 6.2.3.1 사전 정의 동작 updateCertificate. 명세는 보안 기구 전체는 범위 밖으로 둔다. 26. 사이버보안·접근권한·개인정보 9절의 '보안 명령 조율' [추정]의 근거.
- **f12**: 위협 모델(DRAFT, 최종 수정 2021-01): "Many images are setup with a default username and password." CISA 권고 내용은 26. 사이버보안·접근권한·개인정보 5절 기준(원문 미열람).
- **f13**: C. 연결·실행 기반 페이지 G 연결 항목과 같은 주장. 관련 열린 질문 oq-043·oq-056. (재인용: 2026-09-25-38)
- **f14**: VDA 5050 2장 범위: "does not define functional, operational, or system safety requirements and shall not be regarded or applied as a safety standard."
- **f15**: 25. 안전·위험 관리 5절 피킹 시나리오와 10절 연결의 [추정] 주장. 원격 비상정지 지시 경로의 성능 수준 요구 여부는 oq-095 로 열림.
- **f16**: VDA 5050 5.3~5.4 관제·이동로봇 기능 구분(원문 열람). MassRobotics·ISO 21423 은 C. 연결·실행 기반 페이지 G 연결 항목 기준(원문 미열람).
- **f17**: C. 연결·실행 기반·F. 도입·검증·유지관리 페이지의 같은 [추정] 주장. OTTO 인증 발표는 벤더 주장이며 시험 항목 미확인(oq-055).
- **f18**: 단체표준 원문·발행일 미확인(기사 보도 기준). 메시지 내용은 oq-041 로 열림.
- **f19**: README: "publish & subscribe to topics, call services & actions, set parameters, read sensor data, and monitor robot state in real time." 기여 안내에 'permissions' 가 새 기능 후보로 적힘.
- **f20**: 트랙 nl-task-chatbot 단계 3 finding f20 의 종합 판단을 대분류 연결로 옮김. 검증 전 트랙 추정이다. (재인용: 2026-09-25-71)
- **f21**: Verification-Gated Agentic Mission-State Governance(arXiv 2606.31339). 산업용 다중 로봇 대상이며 물류 적용 미확인. (재인용: 2026-09-25-71)
- **f22**: D. 계획·최적화 페이지 G 연결 항목과 27. AI·학습·적응과 모델 운영 5절 근거. LLM 배정 결과 수치는 출처 충돌(oq-030)로 쓰지 않는다.
- **f23**: D. 계획·최적화 페이지 G 연결 항목 기준. 두 연구 모두 프리프린트, 원문 미열람.
- **f24**: D. 계획·최적화 페이지 G 연결 항목 기준. 물류센터 적용 미확인. 배정 전 보고값 검증 기준은 oq-082 로 열림.
- **f25**: VDA 5050 6.4.1 구역 유형(BLOCKED: "shall not enter" 등)과 2장 범위의 안전 표준 부인 문구. 교통 수단과 안전 기능을 구분하는 근거.
- **f26**: rmf_demos README·open-rmf/rmf 이슈 #658. 이후 구현 여부 미확인. 주차 위치 배분이 공용 자원 문제와 겹친다.
- **f27**: 25. 안전·위험 관리 5절 출하 시나리오 제약 칸과 10절 15. 다중 로봇 경로·교통 관리 — MAPF 연결의 근거(RMF Core Overview).
- **f28**: D. 계획·최적화 페이지 G 연결 항목의 [추정] 주장(oq-057). (재인용: 2026-09-25-55)
- **f29**: E. 협업·현장 운영 페이지 G 연결 항목 기준(원문 미열람). 국내 대응 KS 여부는 oq-064.
- **f30**: E. 협업·현장 운영 페이지 G 연결 항목과 25. 안전·위험 관리 9절의 [추정] 경계. (재인용: 2026-09-25-60)
- **f31**: 게시물 제목·요약 기준(원문 미열람). 제정 KS 번호·내용은 oq-070 로 열림.
- **f32**: E. 협업·현장 운영 페이지 G 연결 항목과 25·27 페이지 근거. 실험 환경은 물류 현장이 아님.
- **f33**: Explainable AI for Robot Failures(2021-01). E. 협업·현장 운영 페이지 G 연결 항목과 같은 각주. (재인용: 2026-09-25-60)
- **f34**: E. 협업·현장 운영 페이지 G 연결 항목의 [추정] 주장(oq-033, oq-073). (재인용: 2026-09-25-60)
- **f35**: 26. 사이버보안·접근권한·개인정보 5절 입고 시나리오 제약 칸(호 번호 미확인). 위협 모델은 카메라 영상을 사적 데이터로 분류. 적용 해석은 oq-099.
- **f36**: 25. 안전·위험 관리 5절 출하 시나리오 예외·성과 칸의 [추정] 주장.
- **f37**: 26. 사이버보안·접근권한·개인정보 5절 원격 유지보수 시나리오의 [추정] 주장. 로봇·명령 단위 권한 매트릭스 공개 표준은 미확인(oq-100).
- **f38**: 25. 안전·위험 관리 4절과 F. 도입·검증·유지관리 페이지 G 연결 항목 기준(원문 미열람). 세부 시험 항목 미확인.
- **f39**: F. 도입·검증·유지관리 페이지 G 연결 항목의 [추정] 주장(oq-092, oq-093). 근거가 업체 자료 하나다.
- **f40**: 위협 모델: "An attacker compromising the build-farm or the developer workstation could introduce a vulnerability in a binary..." IEC TR 은 F 페이지 기준(원문 미열람).
- **f41**: F. 도입·검증·유지관리 페이지 G 연결 항목 기준. 온보딩 현장 적용 사례 미확인.
- **f42**: 27. AI·학습·적응과 모델 운영 5절 출하 시나리오 예외·성과 칸의 [추정] 주장과 분류 원문 24 정의의 '모델 버전'. 어느 대분류 페이지에도 아직 없는 연결.
- **f43**: F. 도입·검증·유지관리 페이지 G 연결 항목 기준. 물류센터 적용 여부는 oq-085.
- **f44**: F. 도입·검증·유지관리 페이지 G 연결 항목과 28 페이지 각주. 물류로봇 시험인증 협력은 기사 기준. 관련 oq-089·oq-111.
- **f45**: 28. 표준·상호운용성·다사업자 거버넌스 5절 출하 시나리오 예외·성과 칸의 [추정] 주장. 2.x·3.0.0 혼재 운영은 oq-091.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 아니오 |
| ref-009 | ROS 2 Design | ROS 2 DDS-Security Integration | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://design.ros2.org/articles/ros2_dds_security.html | 아니오 |
| ref-010 | ROS 2 Design | ROS 2 Robotic Systems Threat Model | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://design.ros2.org/articles/ros2_threat_model.html | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 예 |
| ref-076 | DeFazio, D., Mehta, H., Wang, M., Yang, P., Blackburn, J., & Zhang, S. | Vision Language Models Can Parse Floor Plan Maps | 2024-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2409.12842 | 예 |
| ref-090 | Kannan, S. S., Venkatesh, V. L. N., & Min, B.-C. | SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models | 2023-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2309.10062 | 예 |
| ref-104 | Open Robotics (open-rmf) | rmf_demos — Demonstrations of Open-RMF (README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_demos | 예 |
| ref-111 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_state.json | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_state.json | 예 |
| ref-125 | Open Robotics (open-rmf) | rmf_api_msgs — rmf_api_msgs/schemas/task_request.json | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_api_msgs/blob/main/rmf_api_msgs/schemas/task_request.json | 예 |
| ref-129 | MESA International | B2MML-BatchML/Schema/B2MML-TransactionProfile.xsd | 2023 | 표준 | medium | 2026-09-25 | https://github.com/MESAInternational/B2MML-BatchML/blob/master/Schema/B2MML-TransactionProfile.xsd | 예 |
| ref-130 | OPC Foundation | UA-Nodeset ISA95-JOBCONTROL — opc.ua.isa95-jobcontrol.nodeset2 (NodeSet2.xml·documentation.csv) | 2024-01-31 | 표준 | medium | 2026-09-25 | https://github.com/OPCFoundation/UA-Nodeset/tree/latest/ISA95-JOBCONTROL | 예 |
| ref-138 | 국가표준인증통합정보시스템(KSSN) | KS B 7321-2 로봇 — 서비스 로봇 모듈용 정보 모델 — 제2부: 소프트웨어 모듈용 정보 모델 | 미확인 | 표준 | medium | 2026-09-25 | https://www.kssn.net/search/stddetail.do?itemNo=K001010147546 | 예 |
| ref-159 | ISO | ISO 21423 - Robotics — Industrial mobile robots — Communications and interoperability | 미확인 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/86749.html | 예 |
| ref-168 | Kaitha, S., & Yu, S. 외(arXiv 2512.02810) | Phase-Adaptive LLM Framework with Multi-Stage Validation for Construction Robot Task Allocation: A Systematic Benchmark Against Traditional Optimization Algorithms | 2025-12 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2512.02810 | 예 |
| ref-199 | arXiv 2410.21415 저자(미확인) | Deploying Ten Thousand Robots: Scalable Imitation Learning for Lifelong Multi-Agent Path Finding | 2024-10 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2410.21415 | 예 |
| ref-210 | ANSI / A3(Association for Advancing Automation) | ANSI/A3 R15.08-2-2023 - Industrial Mobile Robots - Safety Requirements - Part 2: Requirements for IMR system(s) and IMR application(s) | 2023 | 표준 | medium | 2026-09-25 | https://webstore.ansi.org/standards/ria/ansia3r15082023 | 예 |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json | 예 |
| ref-234 | IDTA(Industrial Digital Twin Association) | IDTA 02047 Technical Data for Automated Guided Vehicles 1.0 — README (admin-shell-io/submodel-templates) | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/admin-shell-io/submodel-templates/tree/main/published/Technical%20Data%20for%20Automated%20Guided%20Vehicles | 예 |
| ref-238 | Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A. | On the Use of Large Language Models to Generate Capability Ontologies | 2024-04 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2404.17524 | 예 |
| ref-239 | Dussard, B., & Sarthou, G. (LAAS-CNRS) | Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF | 2026-06 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2606.17073 | 예 |
| ref-240 | ISO | ISO 22166-201:2024 - Robotics — Modularity for service robots — Part 201: Common information model for modules | 2024-02 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/82334.html | 예 |
| ref-253 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — README | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard | 예 |
| ref-283 | Open Robotics | Doors (integration_doors) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_doors.html | 예 |
| ref-284 | Open Robotics | Lifts (integration_lifts) - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/integration_lifts.html | 예 |
| ref-286 | Open Robotics (open-rmf) | rmf_internal_msgs — rmf_lift_msgs/msg/LiftState.msg | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf_internal_msgs/blob/main/rmf_lift_msgs/msg/LiftState.msg | 예 |
| ref-314 | 국가표준인증통합정보시스템(KSSN) | KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법 | 2021-11 | 표준 | medium | 2026-09-25 | https://www.kssn.net/search/stddetail.do?itemNo=K001010135682 | 예 |
| ref-315 | 산업통상자원부 국가기술표준원(대한민국 정책브리핑) | 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 | 2021-11 | 정부·연구기관 | medium | 2026-09-25 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156480155 | 예 |
| ref-316 | 건설기술신문 | 승강기협, 엘리베이터-로봇 연동 단체표준 제정 | 미확인 | 기사 | low | 2026-09-25 | https://www.ctman.kr/35296 | 예 |
| ref-317 | 전기신문 | 승강기협회 '로봇-승강기 연동 표준개발'로 승강기 4차산업 견인 | 미확인 | 기사 | low | 2026-09-25 | https://www.electimes.com/news/articleView.html?idxno=320147 | 예 |
| ref-351 | Ren, A. Z. 외 | Robots That Ask For Help: Uncertainty Alignment for Large Language Model Planners | 2023-07 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2307.01928 | 예 |
| ref-353 | Park, J., Lim, S., Lee, J., Park, S., Chang, M., Yu, Y., & Choi, S. | CLARA: Classifying and Disambiguating User Commands for Reliable Interactive Robotic Agents | 2024 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2306.10376 | 예 |
| ref-399 | Wang, Z., & Gombolay, M. | Heterogeneous graph attention networks for scalable multi-robot scheduling with temporospatial constraints | 미확인 | 논문 | medium | 2026-09-25 | https://link.springer.com/article/10.1007/s10514-021-09997-2 | 예 |
| ref-405 | Open Robotics | Security - Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/security.html | 아니오 |
| ref-407 | gpue (GitHub) | vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/gpue/vda5050-sim | 예 |
| ref-408 | ekusiadadus (GitHub) | vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/ekusiadadus/vda5050-lab | 예 |
| ref-417 | Obi, I., Venkatesh, V. L. N., Wang, W., Wang, R., Suh, D., Amosa, T. I., Jo, W., & Min, B.-C.(Purdue University SMART Lab) | Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems | 2026-04 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2604.05427 | 예 |
| ref-465 | Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A. | Toward a Method to Generate Capability Ontologies from Natural Language Descriptions | 2024-06 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2406.07962 | 예 |
| ref-466 | 부산일보 | KTL·통합물류협회 ‘물류로봇 시험인증’ 협력 강화 ‘맞손’ | 2026-07-24 | 기사 | low | 2026-09-25 | https://www.busan.com/view/busan/view.php?code=2026072420194685883 | 예 |
| ref-470 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 2023-06 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/83545.html | 예 |
| ref-472 | A3(Association for Advancing Automation) | ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available | 2023-10 | 업계 보고서 | medium | 2026-09-25 | https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available | 예 |
| ref-473 | 고용노동부 | 고정식 이동식 산업용 로봇의 협동작업 안전 가이드 배포 | 2023-07 | 정부·연구기관 | medium | 2026-09-25 | https://www.moel.go.kr/policy/policydata/view.do?bbs_seq=20230700065 | 예 |
| ref-475 | 중소벤처기업부(대한민국 정책브리핑) | ｢대구 이동식 협동로봇 규제자유특구｣ 산업표준 제정으로, 이동식 협동로봇 상용화 길 열렸다! | 2024-11 | 정부·연구기관 | medium | 2026-09-25 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156658517 | 예 |
| ref-476 | Das, D., Banerjee, S., & Chernova, S. | Explainable AI for Robot Failures: Generating Explanations that Improve User Assistance in Fault Recovery | 2021-01 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2101.01625 | 예 |
| ref-494 | Francos, R. M., Garces, D., Akgün, O. E., Bastian, N. D., & Gil, S.(Harvard·JHU) | Trust-Aware Sequential Decision Making and Rollout Planning for Resilient Multi-Robot Systems | 2026-08 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2608.25690 | 예 |
| ref-516 | 한국표준협회 KSSN(국가표준인증종합정보센터) | KS X ISO 23247-1 자동화 시스템 및 통합 — 제조를 위한 디지털 트윈 프레임워크 — 제1부: 개요 및 일반 원리 | 미확인 | 표준 | medium | 2026-09-25 | https://www.kssn.net/search/stddetail.do?itemNo=K001010140724 | 예 |
| ref-518 | ISO | ISO 23247-6:2026 — Automation systems and integration — Digital twin framework for manufacturing — Part 6: Digital twin composition | 2026 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/87426.html | 예 |
| ref-531 | arXiv 2607.05683 저자(미확인) | Deep Reinforcement Learning for Dynamic Battery Management of Autonomous Order Pickers | 2026-07 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2607.05683 | 예 |
| ref-539 | askforalfred (ALFRED 공식 저장소) | ALFRED — A Benchmark for Interpreting Grounded Instructions for Everyday Tasks (GitHub README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/askforalfred/alfred | 예 |
| ref-541 | lbaa2022 (LoTa-Bench 공식 저장소) | LLMTaskPlanning — LoTa-Bench: Benchmarking Language-oriented Task Planners for Embodied Agents (ICLR 2024) (GitHub README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/lbaa2022/LLMTaskPlanning | 예 |
| ref-554 | IEC | IEC TR 62443-2-3:2015 Security for industrial automation and control systems - Part 2-3: Patch management in the IACS environment | 2015-06 | 표준 | medium | 2026-09-25 | https://webstore.iec.ch/en/publication/22811 | 예 |
| ref-559 | 세이프틱스(Safetics) | 로봇 시스템 위험성평가 가이드 | 미확인 | 벤더 문서 | low | 2026-09-25 | https://doc.safetics.io/insight-risk-assessment/ | 예 |
| ref-561 | 대한민국 정책브리핑(중소벤처기업부) | 이동식 협동로봇 ‘안전기준 산업표준’ 제정…상용화 길 열어 | 2024-11-03 | 정부·연구기관 | medium | 2026-09-25 | https://www.korea.kr/news/policyNewsView.do?newsId=148935814 | 예 |
| ref-567 | Open-RMF (open-rmf/rmf GitHub) | [Feature request]: Fire alarm separation for different fleets · Issue #658 · open-rmf/rmf | 2025-04-04 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/open-rmf/rmf/issues/658 | 예 |
| ref-583 | CISA | Mobile Industrial Robots Vehicles and MiR Fleet Software (ICSA-21-280-02) | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://www.cisa.gov/news-events/ics-advisories/icsa-21-280-02 | 예 |
| ref-589 | 법제처 국가법령정보센터 | 근로자참여 및 협력증진에 관한 법률 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=105636 | 예 |
| ref-606 | 한국표준협회 KSSN(국가표준인증종합정보센터) | KS B ISO 18646-1 로봇 — 서비스 로봇의 성능 기준 및 관련 시험방법 — 제1부 : 바퀴형 로봇의 이동능력 | 미확인 | 표준 | medium | 2026-09-25 | https://www.kssn.net/search/stddetail.do?itemNo=K001010113281 | 예 |
| ref-607 | 한국로봇산업진흥원(KIRIA) | 시험평가 — KIRIA 첨단로봇 실증지원 디지털 플랫폼 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://kiria.org/rp/kiria/tva/inr/page.dn | 예 |
| ref-608 | OTTO by Rockwell Automation | OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments | 2026-04 | 벤더 문서 | low | 2026-09-25 | https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/ | 예 |
| ref-618 | ISO/IEC | ISO/IEC 42001:2023 - AI management systems | 2023 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/42001 | 예 |
| ref-623 | Agrawal, A. 외 | RTAW: An Attention Inspired Reinforcement Learning Method for Multi-Robot Task Allocation in Warehouse Environments | 2022-09 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2209.05738 | 예 |
| ref-625 | Breck, E. 외 (Google Research) | The ML Test Score: A Rubric for ML Production Readiness and Technical Debt Reduction | 2017 | 논문 | medium | 2026-09-25 | https://research.google/pubs/the-ml-test-score-a-rubric-for-ml-production-readiness-and-technical-debt-reduction/ | 예 |
| ref-626 | MLflow (Linux Foundation 오픈소스 프로젝트) | ML Model Registry \| MLflow AI Platform | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://mlflow.org/docs/latest/ml/model-registry/ | 예 |
| ref-635 | Semantic Versioning (Tom Preston-Werner, semver.org) | Semantic Versioning 2.0.0 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://semver.org/spec/v2.0.0.html | 예 |
| ref-677 | Tang, G. 외(arXiv 2606.31339) | Verification-Gated Agentic Mission-State Governance for Intelligent Industrial Multi-Robot Systems | 2026-06 | 논문 | medium | 2026-09-25 | https://arxiv.org/abs/2606.31339 | 예 |
| ref-679 | robotmcp (ROS-MCP-Server 공식 저장소) | ros-mcp-server — Connect AI models like Claude & GPT with robots using MCP and ROS (GitHub README) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/robotmcp/ros-mcp-server | 아니오 |
| ref-706 | IETF (RFC Editor) | RFC 9745: The Deprecation HTTP Response Header Field | 미확인 | 표준 | medium | 2026-09-25 | https://www.rfc-editor.org/info/rfc9745/ | 예 |
| ref-709 | 대한민국 정책브리핑(산업통상자원부 국가기술표준원) | 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 | 2021-11-11 | 정부·연구기관 | medium | 2026-09-25 | https://korea.kr/news/pressReleaseView.do?newsId=156480155 | 예 |
| ref-710 | 한국지능형로봇표준포럼(KOROS) | KOROS 1148-8:2025 서비스 로봇을 위한 모듈 - 제2-8부 : 소프트웨어 모듈용 정보모델 상호운용성 시험 절차 | 2025-06-04 | 표준 | medium | 2026-09-25 | http://www.koros.or.kr/bbs/board.php?bo_table=notice27&wr_id=223 | 예 |

### 출처 요약

- **ref-004**: RMF 교통 스케줄·협상·긴급 작업 우선 협상 구조(이전 실행에서 원문 열람, 이번 실행 재열람 안 함).
- **ref-009**: 원문 미열람. ROS 2 의 DDS-Security 인증·접근통제·암호화 플러그인 통합 설계(이번 실행 재열람 안 함).
- **ref-010**: ROS 2 로봇 시스템 위협 모델 초안(최종 수정 2021-01). 기본 자격증명 SSH, 카메라 영상·로그 민감 자산, 빌드 팜 공급망 위협과 감사·서명 완화책.
- **ref-031**: VDA 5050 3.0.0 명세. 안전 표준 부인 문구, safetyState, updateCertificate, 관제·로봇 기능 구분, 구역 유형을 이번 실행에서 원문으로 확인.
- **ref-051**: 원문 미열람. VDA 5050 상태 메시지 JSON 스키마(오류 수준·운용 모드·적재물·배터리 필드).
- **ref-076**: 원문 미열람. 비전 언어 모델로 평면도 지도를 해석하는 연구.
- **ref-090**: 원문 미열람. LLM 기반 다중 로봇 작업 계획·배정.
- **ref-104**: 원문 미열람. Open-RMF 데모 구성과 비상 경보 시 주차 동작.
- **ref-111**: 원문 미열람. Open-RMF 작업 상태 스키마.
- **ref-125**: 원문 미열람. Open-RMF 작업 요청 스키마.
- **ref-129**: 원문 미열람. B2MML 거래 동사(CHANGE·CANCEL 등) 정의.
- **ref-130**: 원문 미열람. OPC UA for ISA-95 Job Control 작업 지시 메서드.
- **ref-138**: 원문 미열람. 서비스 로봇 소프트웨어 모듈 정보 모델 KS.
- **ref-159**: 원문 미열람. 산업용 이동로봇 통신·상호운용성 국제표준(발행 여부 미확인).
- **ref-168**: 원문 미열람. LLM 기반 로봇 작업 배정 벤치마크(결과 수치 출처 충돌, oq-030).
- **ref-199**: 원문 미열람. 모방 학습 기반 지속형 MAPF.
- **ref-210**: 원문 미열람. 산업용 이동로봇 시스템·적용 안전 요구(유형 C 모바일 매니퓰레이터 포함).
- **ref-230**: 원문 미열람. MassRobotics 상태 보고 JSON 스키마(운용 상태 어휘).
- **ref-234**: 원문 미열람. 무인운반차 기술 데이터 서브모델.
- **ref-238**: 원문 미열람. LLM 으로 능력 온톨로지 생성.
- **ref-239**: 원문 미열람. URDF 에서 로봇 온톨로지를 LLM 으로 채우는 연구.
- **ref-240**: 원문 미열람. 서비스 로봇 모듈 공통 정보 모델.
- **ref-253**: 원문 미열람. MassRobotics AMR 상호운용 표준 저장소(신원·상태 보고).
- **ref-283**: 원문 미열람. Open-RMF 문 연동.
- **ref-284**: 원문 미열람. Open-RMF 승강기 연동.
- **ref-286**: 원문 미열람. 승강기 상태 메시지(층 이름, 운영 모드).
- **ref-314**: 원문 미열람. 이동 로봇 엘리베이터 탑승 안전 KS.
- **ref-315**: 원문 미열람. 로봇 엘리베이터 탑승 KS 제정 보도자료.
- **ref-316**: 원문 미열람. 대한승강기협회 엘리베이터–로봇 연동 단체표준 제정 기사.
- **ref-317**: 원문 미열람. 로봇–승강기 연동 표준 개발 기사.
- **ref-351**: 원문 미열람. KnowNo: 등각 예측 기반으로 불확실할 때 사람에게 묻는 LLM 계획기.
- **ref-353**: 원문 미열람. 사용자 명령 분류·모호성 해소.
- **ref-399**: 원문 미열람. 학습 기반 다중 로봇 스케줄링.
- **ref-405**: RMF 의 SROS 2 인클레이브·서명 권한 파일, 대시보드 TLS·OIDC 역할 토큰.
- **ref-407**: 원문 미열람. VDA 5050 3.0.0 시뮬레이터와 적합성 시험 묶음(개인 프로젝트).
- **ref-408**: 원문 미열람. MQTT 기록 기반 VDA 5050 진단 도구(개인 프로젝트).
- **ref-417**: 원문 미열람. SafeGate: 자연어 명령 실행 전 결정적 안전 판정과 작업 안전 계약.
- **ref-465**: 원문 미열람. 자연어 능력 설명에서 LLM 으로 능력 온톨로지 생성.
- **ref-466**: 원문 미열람. KTL·통합물류협회 물류로봇 시험인증 협력 기사.
- **ref-470**: 원문 미열람. 무인 산업 차량과 시스템의 안전 요구·검증, 운용 구역 부속서 A.
- **ref-472**: 원문 미열람. R15.08-2 발행 안내.
- **ref-473**: 원문 미열람. 산업용 로봇 협동작업 안전 가이드 배포 게시물.
- **ref-475**: 원문 미열람. 이동식 협동로봇 산업표준 제정 보도자료.
- **ref-476**: 원문 미열람. 로봇 실패 설명 생성으로 고장 복구 지원 개선.
- **ref-494**: 원문 미열람. 위치 스푸핑 에이전트를 고려한 신뢰 인지 다중 로봇 배정·계획.
- **ref-516**: 원문 미열람. 제조용 디지털 트윈 프레임워크 KS 부합화 표준.
- **ref-518**: 원문 미열람. 디지털 트윈 결합 표준.
- **ref-531**: 원문 미열람. 자율 피킹 로봇 배터리 관리의 심층 강화학습.
- **ref-539**: 원문 미열람. 자연어 지시 기반 체화 에이전트 벤치마크.
- **ref-541**: 원문 미열람. 언어 기반 작업 계획기 자동 평가 벤치마크.
- **ref-554**: 원문 미열람. IACS 환경 패치 관리 기술 보고서.
- **ref-559**: 원문 미열람. 업체의 로봇 시스템 위험성평가 가이드(변경 시 재평가 권고).
- **ref-561**: 원문 미열람. 이동식 협동로봇 안전기준 산업표준 제정 소식.
- **ref-567**: 원문 미열람. 화재경보 시 로봇 주차와 플릿별 구분 기능 요청.
- **ref-583**: 원문 미열람. MiR 차량·플릿 소프트웨어 취약점 권고.
- **ref-589**: 원문 미열람. 제20조 노사협의회 협의 사항(근로자 감시 설비 설치).
- **ref-606**: 원문 미열람. 바퀴형 서비스 로봇 이동 성능 시험방법 KS.
- **ref-607**: 원문 미열람. 한국로봇산업진흥원 시험평가 서비스 안내.
- **ref-608**: 원문 미열람. VDA 5050 인증 취득 벤더 발표(시험 항목 미확인).
- **ref-618**: 원문 미열람. AI 관리 시스템 표준.
- **ref-623**: 원문 미열람. 창고 다중 로봇 작업 배정 강화학습(시뮬레이션 창고).
- **ref-625**: 원문 미열람. ML 운영 준비도 시험 기준.
- **ref-626**: 원문 미열람. 모델 레지스트리의 버전·별칭 관리.
- **ref-635**: 원문 미열람. 의미적 버전 관리 규칙(이전 실행에서 열람, 이번 실행 재열람 안 함).
- **ref-677**: 원문 미열람. LLM 제안의 결정적 검증과 원자적 반영을 거치는 관리형 블랙보드 구조.
- **ref-679**: rosbridge 로 LLM 에 ROS 토픽·서비스·액션·파라미터를 도구로 노출. 권한 기능은 향후 기여 항목.
- **ref-706**: 원문 미열람. API 폐기 예고 HTTP 헤더.
- **ref-709**: 원문 미열람. 로봇 엘리베이터 탑승 KS 제정 발표(속도 제어·보호 정지 등).
- **ref-710**: 원문 미열람. 소프트웨어 모듈 정보모델 상호운용성 시험 절차 단체표준.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/g-safety-security-intelligence-and-governance/index.md | 5. 다른 대분류와의 연결 | '다른 대분류와의 연결' 절만 채운다(patches replace). A. 업무·공급망 설계: f1·f2·f3 / B. 공통 정보·환경 모델: f4·f5·f6·f7·f8 / C. 연결·실행 기반: f9·f10·f11·f12·f13·f14·f15·f16·f17·f18·f19·f20·f21(C 페이지의 27. AI·학습·적응과 모델 운영 '근거 없음' 갭에 대한 보강 후보 f19~f21) / D. 계획·최적화: f22·f23·f24·f25·f26·f27·f28 / E. 협업·현장 운영: f29~f37(E 페이지가 근거 없음으로 둔 26. 사이버보안·접근권한·개인정보 연결 후보 f35·f37) / F. 도입·검증·유지관리: f38~f45(24. 자산·소프트웨어 수명주기 관리 ↔ 27. AI·학습·적응과 모델 운영 신규 연결 f42). 게시된 A~F 대분류 페이지의 G 쪽 서술과 같은 각주를 재사용해 상호 참조 링크를 둔다. 교차 확인된 연결은 없음. '아직 다루지 않은 연결'에 11. 분산 시스템·통신·컴퓨팅 구조 ↔ 25·27, 7. 화물·재고·자산 식별과 추적 ↔ G, 2·3·4 ↔ 25·26, 14. 작업 순서·스케줄링 ↔ G 를 적는다. |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- ROP 가 VDA 5050 updateCertificate 같은 보안 명령으로 제조사 로봇의 인증서를 교체할 때, 교체 시점·대상 승인과 실패 시 되돌림 책임은 ROP 사업자·제조사·현장 IT 조직 중 누가 지는가? | 관련 영역: 26. 사이버보안·접근권한·개인정보, 9. 로봇·제조사 관제 연동, 24. 자산·소프트웨어 수명주기 관리 | 근거: f11 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 70 · 교차 확인: 0
- 예산 사용량: 검색 1회 · 신규 출처 0건
- 미확인 항목:
    - 모든 finding 교차 확인 없음: 연결마다 단일 출처이거나 같은 발행 주체 출처
    - f19~f21: C. 연결·실행 기반 페이지가 '근거 없음'으로 둔 27. AI·학습·적응과 모델 운영 연결의 보강 후보이며, f20·f21 은 트랙 nl-task-chatbot 실행 2026-09-25-71 의 검증 전 finding 을 재인용
    - f42: 24. 자산·소프트웨어 수명주기 관리 ↔ 27. AI·학습·적응과 모델 운영 연결은 게시 페이지의 [추정] 주장과 분류 원문 정의에 기댄 새 연결
    - ref-031 의 '책임 분배는 범위 밖' 문구는 WebFetch 요약에만 나타나 원문 구절을 확인하지 못해 쓰지 않음
    - ISO 10218-1:2025 사이버보안 조항(5.1.16 로 검색 요약에 나옴)은 G 내부 연결(25↔26)이라 이번 대분류 연결에 쓰지 않았고 oq-102 해결 근거로도 올리지 않음
- 범위 경계 위반 의심:
    - f38: ISO 3691-4 안전 요구는 로봇 자체 안전 기능 쪽이라 '연계 대상: '으로 표시
    - f8·f9·f26: 승강기·비상 신호 관련 설비 안전 제어는 분류 원문 9장 시설·설비 제어 경계의 연계 대상이며 ROP 는 운영 모드 확인만 맡는다고 claim·excerpt 에 적음
    - f3: 수요예측 모델은 상위 업무 시스템 경계의 연계 대상으로 명시
    - f19·f20: 로봇 토픽·액션 직접 제어는 로봇 자체 지능·제어 경계와 맞닿아 ROP 는 상위 도구 노출 경계만 판단
- 한계: 대분류 연결(category_link) 실행. web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문을 연 출처: ref-031(VDA5050_EN.md), ref-405(security.md), ref-010(ros2 threat model), ref-679(ros-mcp-server README). 나머지 재사용 66건은 이번 실행에서 열지 않아 fetched false·신뢰도 상한 medium. 신규 출처 0건(예약 구간 ref-711~ref-740 미사용), 검색 1회/30(ISO 10218-1:2025 사이버보안 조항 확인용, 결과는 G 내부 연결이라 finding 에 쓰지 않음). 근거는 게시된 25~28 세부영역 페이지와 A~F 대분류 페이지의 G 쪽 연결 서술(검증된 주장·각주)을 재사용했고, 같은 주장은 기존 태그를 유지하거나 낮췄다. 한국어 검색은 하지 않음(국내 근거는 기존 KS·정부 출처 재사용: ref-314·315·473·475·561·589·606·607·709·710). 교차 규칙: 27. AI·학습·적응과 모델 운영 finding 은 적용 대상 5. 로봇 능력·작업 온톨로지(f4), 6. 지도·공간·위치 모델(f5), 13. 작업 배정 — MRTA(f22), 19. 모니터링·이상 탐지·원인 분석(f33), 21. 온보딩·설정·현장 시운전(f41)과 함께 냈다. 8. 실시간 세계 상태·데이터 일관성(f8)과 22. 시뮬레이션·예측용 디지털 트윈(f43)은 섞지 않았다. 정정 요청 없음. 용어 후보 없음(관련 용어는 이미 용어집에 있음). 아직 근거가 없는 연결: 11. 분산 시스템·통신·컴퓨팅 구조 ↔ 25·27, 7. 화물·재고·자산 식별과 추적 ↔ G, 14. 작업 순서·스케줄링 ↔ G, 2·3·4 ↔ 25·26.
