# 리서치 브리프 2026-10-11-03

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-11-03 |
| 날짜 | 2026-10-11 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 22. 설비·건물 시스템 연동 |
| 대분류 | F. 연동 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 — 국토부 '로봇 친화형 건축물' 핵심기술 개발 보도자료(ref-322)는 제목만 확인돼 발행일·사업기간·세부 과제가 비어 있고, KS B 7317 은 '2021년 11월 제정'만 있어 이후 개정 이력이 없음
- 섹션 4·6. 핵심 개념·대표 접근법(주제 페이지 2026-09-25-area10-s4) — 승강기 세션을 언제 '수락'으로 볼지, 세션 종료·잔류 처리, 작업대 결과의 완료 판정 조건 근거가 약함. 제조사 어댑터(KONE·Dormakaba)와 PLC 연결의 실제 조건이 없음
- 섹션 5. 적용 사례 — 물류창고 가상 시나리오뿐이며 실제 설비 연결(PLC·드라이 접점)과 화재 복구, 상업 시설 사례가 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스(주제 페이지 2026-09-25-area10-s7) — KOLA 단체표준이 '표준 번호·제정일·내용 미확인', SEMI E84 현행판·후속 개발 제안, BACnet 출입통제 문서의 지위가 비어 있음
- 섹션 8. 대표 연구와 자료(주제 페이지 2026-09-25-area10-s8) — '모두 원문을 열지 못해 결과 수치는 쓰지 않는다'로 남아 있어 각 연구의 실험 조건(실물·수치 실험)과 승강기 결과가 비어 있음
- 섹션 9·11 — 출입통제 연동에서 권한 확인 주체(oq-043), 단체표준–Open-RMF 대응(oq-041), 인계 신호 표준(oq-042), 물류센터 승강기 병목(oq-010)이 열려 있음

## 조사 질문

1. 문·승강기·설비의 준비와 로봇의 도착을 어떻게 맞출 것인가? [분류원문]
2. oq-010 국내 다층 물류센터에서 화물용 승강기나 층간 반송 설비가 로봇 처리량의 병목이 된다는 정량 자료가 있는가, 병원·호텔 사례의 승강기 혼잡 결과를 물류센터에 옮길 수 있는가? (섹션 3·8 겨냥)
3. oq-041 대한승강기협회 '엘리베이터와 로봇의 상호 연동을 위한 가이드라인' 단체표준은 어떤 메시지·상태를 정하며, Open-RMF 승강기 요청·상태 메시지와 어떻게 대응하는가? (oq-283 표준 번호 포함, 섹션 7 겨냥)
4. oq-042 컨베이어·작업대와 이동로봇 사이 적재물 인계 신호(준비·허가·이송·완료)를 제조사 중립으로 정한 공개 표준이나 규격이 있는가? (oq-062 포함, 섹션 6·7 겨냥)
5. oq-043 로봇 관제가 출입통제·건물 자동화 시스템(BACnet 등)을 통해 보안문을 여닫는 공개 설계나 국내 사례가 있고, 권한 확인은 누가 하는가? (섹션 7·9 겨냥)
6. KS B 7317 과 로봇 친화형 건축물 관련 국내 제도·연구개발은 현재 어느 판·단계인가? (oq-098·oq-173·oq-311·oq-179 관련, 섹션 3·7 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | Park·Park 의 2026년 Architectural Research 논문은 초록 기준으로 로봇 친화형 건축물 인증(REEC)과 무장애(BF) 인증을 비교 분석해 사람 중심·로봇 적응형 건축 설계 기준을 도출했다. | ref-1483 | 아니오 | medium | 2026-07-21 | — | — |
| f2 | [추정] | 국토교통부의 로봇 친화형 건축물 설계·시공 및 운영·관리 핵심기술 개발 연구개발은 2025년 5월 착수보고회를 열고 2028년까지 완료할 예정이라고 2차 보도됐다. | ref-322, ref-1484 | 아니오 | low | 2025-05-28 | — | — |
| f3 | [추정] | 같은 연구개발은 세부 중점과제 가운데 하나로 기술 실증을 통한 기술표준·인증제도 개선방안 마련을 두었다고 2차 보도됐다. | ref-322, ref-1484 | 아니오 | low | 2025-05-28 | — | — |
| f4 | [사실] | e-나라표준인증의 KS B 7317 이력은 2021-11-30 제정(고시 2021-0561), 2022-12-09 개정(고시 2022-0571), 2025-05-09 개정(고시 2025-0073)을 기록한다. | ref-314 | 아니오 | medium | 2025-05-09 | — | — |
| f5 | [사실] | 같은 KS B 7317 기본정보는 적용 대상을 엘리베이터 탑승 기능이 있는 서비스 로봇과 병원의 환자 전용 엘리베이터를 제외한 모든 엘리베이터로 적고, 표준개발협력기관을 한국AI·로봇산업협회로 적는다. | ref-314 | 아니오 | medium | 2025-05-09 | — | — |
| f6 | [사실] | 대한승강기협회(KOLA)는 2026-03-27 게시한 보도자료에서 「엘리베이터와 로봇의 상호 연동을 위한 가이드라인」 단체표준을 제정했다고 발표했다. | ref-1485 | 아니오 | medium | 2026-03-27 | — | — |
| f7 | [사실] | e-나라표준인증 단체표준 목록은 이 가이드라인을 표준번호 B-KOLA-0001-7700, 상태 제정, 등록일자 2026-03-24 로 올려 두어, KOLA 게시일(2026-03-27)과 목록 등록일이 다르다. | ref-1486 | 아니오 | medium | 2026-10-11 | — | — |
| f8 | [사실] | KOLA 발표는 이 가이드라인이 엘리베이터와 로봇 상호 연동을 위한 일반사항, 시험 설비 및 시험 절차를 제시하며 e-나라표준인증에서 무료로 내려받을 수 있다고 설명한다. | ref-1485 | 아니오 | medium | 2026-03-27 | — | — |
| f9 | [사실] | Open-RMF 개발자(mxgrey)는 2024년 토론 답변에서, 세션을 안전하게 수행하려면 승강기가 별도 AGV 모드여야 하는 경우 모드 전환을 마칠 때까지 승강기 상태에 session_id 를 내보내지 말아야 한다고 권고했다. | ref-1487 | 아니오 | medium | 2024-08-21 | 제약 | — |
| f10 | [사실] | 같은 답변은 별도 AGV 모드가 없는 승강기도 있을 수 있다고 설명한다. | ref-1487 | 아니오 | medium | 2024-08-21 | 제약 | — |
| f11 | [사실] | rmf_ros2 의 lift_supervisor 구현은 승강기별 활성 세션을 두고, 같은 session_id 의 새 요청은 갱신으로 다시 발행하며 세션 종료 요청이면 종료를 발행하고 활성 세션을 비운다. | ref-1488 | 아니오 | medium | 2026-10-11 | — | — |
| f12 | [사실] | 같은 구현은 감독자에게 활성 요청이 없는데 승강기 상태에 세션이 남아 있으면 승강기가 풀리도록 세션 종료 요청을 계속 발행하며, 승강기 배정을 더 지능적으로 하라는 TODO 만 남겨 두고 배정 규칙은 두지 않는다. | ref-1488 | 아니오 | medium | 2026-10-11 | 예외·성과 | — |
| f13 | [사실] | rmf_fleet_adapter 변경기록의 2.13.0(2026-06-15)에는 승강기가 이미 해당 층에 있으면 legacy 완료 상태를 내보내는 변경(#510)이 실려 있다. | ref-1398 | 아니오 | medium | 2026-06-15 | — | — |
| f14 | [사실] | rmf_ros2 의 DispenseItem 단계는 요청 id 가 일치하는 DispenserResult 가 SUCCESS 이면 완료, FAILED 이면 실패로 바꾸고, ACKNOWLEDGED 는 접수 표시만 한다. | ref-1489 | 아니오 | medium | 2026-10-11 | 완료·인계 | — |
| f15 | [사실] | 같은 구현은 디스펜서 상태의 요청 큐에 요청 id 가 들어 있으면 접수된 것으로 보고, 접수 뒤 큐에서 요청 id 가 사라지면 결과 메시지 없이도 완료로 간주한다. | ref-1489 | 아니오 | medium | 2026-10-11 | 완료·인계 | — |
| f16 | [추정] | 큐 소거만으로 완료 처리하면 현장 작업대 큐에서 요청이 취소·오류로 빠진 경우에도 인계 완료로 잘못 판단할 수 있을 것으로 보인다. | ref-1489 | 아니오 | low | 2026-10-11 | 완료·인계 | — |
| f17 | [사실] | CHART 계열 공개 KONE 승강기 어댑터 README 는 Open-RMF 승강기 메시지와 KONE API v2.0 사이에서 WebSocket 으로 승강기 명령을 보내고 승강기 상태를 받는 구조를 설명한다. | ref-1490 | 아니오 | medium | 2026-10-11 | — | — |
| f18 | [사실] | 같은 README 는 실제 승강기를 제어하려면 access_id 와 access_secret 을 KONE 담당자에게서 받아야 한다고 안내한다. | ref-1490 | 아니오 | medium | 2026-10-11 | — | — |
| f19 | [사실] | 연계 대상: Open-RMF 의 Dormakaba 문 어댑터 README 는 시험한 EL301·ED250 문 구동기에 Dormakaba IoT connector 를 장착해야 한다고 안내한다. | ref-1491 | 아니오 | medium | 2026-10-11 | 수행 자원 | — |
| f20 | [사실] | 같은 README 는 문 클라우드 API 접근 자격증명을 Dormakaba 가 제공한다고 안내한다. | ref-1491 | 아니오 | medium | 2026-10-11 | — | — |
| f21 | [추정] | 연계 대상: HopeTechnik 의 도서관 현장 설계 문서에서는 현장에 새로 설치한 승강기 제어함(lift controller box)의 PLC(Beckhoff CX9020)가 서버의 ADS 명령을 받아 드라이 접점으로 승강기 신호를 조작하며, 승강기 업체가 기존 승강기를 AGV 모드로 개조했다. | ref-1492 | 아니오 | medium | 2026-10-11 | 기타 / 수행 자원 | 벤더 주장 |
| f22 | [추정] | 연계 대상: 같은 문서의 복구표는 화재 경보가 울리면 승강기가 수동 모드로 돌아가고 PLC 가 오류 상태에 머물러, 재시작을 위한 수동 개입이 필요하다고 적는다. | ref-1492 | 아니오 | medium | 2026-10-11 | 기타 / 예외·성과 | 벤더 주장 |
| f23 | [추정] | 같은 문서는 승강기 상태 전송 주기를 개요에서는 1 Hz 로, 서버 절에서는 2초마다로 서로 다르게 적고, 승강기 요청은 1초마다 보낸다고 적는다. | ref-1492 | 아니오 | medium | 2026-10-11 | 기타 | 벤더 주장 |
| f24 | [추정] | OMRON LD 시리즈 통합 안내서(I680-E-02)의 인계 예시는 위치·준비 상태 확인, 적재물 교환, 정지·최종 위치 확인, 출발 준비 확인을 단계로 나눈다고 외부 조사 메모가 전한다. | ref-1493 | 아니오 | low | 2026-10-11 | 완료·인계 | 원문 미열람 |
| f25 | [추정] | 같은 안내서는 그 인계 절차가 예시이며 응용 요구에 따라 달라질 수 있다고 적는다고 외부 조사 메모가 전한다. | ref-1493 | 아니오 | low | 2026-10-11 | — | 원문 미열람 |
| f26 | [사실] | SEMI 공식 판매 목록은 E84-0823 을 현행판(Current)으로 표시하고, E84 의 목적을 자동 반송 시스템(AMHS)과 생산 설비 로드포트 사이 캐리어 인계용 병렬 I/O 신호 개선으로 설명한다. | ref-202 | 아니오 | medium | 2026-10-11 | — | — |
| f27 | [추정] | SEMI Doc 7442 는 E84 를 출발점으로 별도의 인계 인터페이스 규격과 TCP/IP 하위 규격을 만들자는 신규 예비 표준 개발 제안서(SNARF)라고 외부 조사 메모가 전한다. | ref-1494 | 아니오 | low | 2026-10-11 | — | 원문 미열람 |
| f28 | [사실] | 고려대 구로병원 약품 배송 로봇 논문은 ROC 로 찾은 승강기 가동률(EOR) 임계값 59.01% 를 현장 특정값으로 해석해야 하며 다른 병원에 적용할 때 재보정이 필요하다고 명시한다. | ref-943 | 아니오 | medium | 2026-03-31 | 병원 / 제약 | — |
| f29 | [사실] | 2026-10-11 재확인에서도 같은 논문에는 전체 성공률 87.03% 의 분모를 설명하는 구절이 없고, 분석 대상 122건에서 실패 14건을 뺀 108건의 비율은 약 88.52% 로 보고값과 다르다. | ref-943 | 아니오 | medium | 2026-03-31 | 병원 / 예외·성과 | — |
| f30 | [사실] | 사람과 승강기를 함께 쓰는 실제 건물에서 로봇의 층간 이동이 지연된 사례가 서로 다른 두 연구에서 보고됐다: 병원 논문은 승강기 가동률이 높을수록 배송 시간이 길어졌다고, KAIST 지도 구축 논문은 외부 이용자 때문에 승강기가 다른 층으로 가 지연이 생겼다고 적는다. | ref-943, ref-163 | 예 | high | 2026-03 | 제약 | — |
| f31 | [사실] | Han 외 다층 호텔 배송 경로계획 논문은 실제 호텔 평면·층고로 거리 행렬(68×68)만 만들고 배송 수요는 무작위 표본으로 생성했으며, 승강기 기본 대기 시간을 30초로 두었다. | ref-103 | 아니오 | medium | 2025-03-13 | — | — |
| f32 | [사실] | Kim 외 그래프 기반 다층 경로계획 논문은 15층 건물을 나타내는 그래프에서 소포 1·3·5·7개 시나리오로 알고리즘을 평가했다. | ref-321 | 아니오 | medium | 2025-02-28 | — | — |
| f33 | [사실] | 노주형 외 다층 지도 구축 연구는 KAIST N1 건물 5~9층에서 각 층의 절반 영역을 대상으로 평가를 수행했다. | ref-163 | 아니오 | medium | 2026-03 | — | — |
| f34 | [사실] | 같은 연구의 승강기 상호작용 시험에서는 20회 중 19회 성공이 보고됐다. | ref-163 | 아니오 | medium | 2026-03 | — | — |
| f35 | [사실] | BACnet 출입통제 백서 BAC-09-08(2008-09-27)은 SSPC 135 LSS 작업반의 진행 중 작업이자 BACnet 표준 변경 제안의 기초 문서라고 스스로 밝힌다. | ref-1495 | 아니오 | medium | 2008-09-27 | — | — |
| f36 | [사실] | 같은 백서는 인증과 권한 검사를 구분하고, 특정 시간에 특정 문을 통과할 권리를 기본 권한 검사의 예로 든다. | ref-1495 | 아니오 | medium | 2008-09-27 | — | — |
| f37 | [추정] | NAVER LABS 는 2026-07-23 블로그에서 ARC 가 Tokyo Midtown Yaesu 의 기존 화물 승강기·자동문과 출입 경로를 중앙에서 연결한다고 설명하고, 연말까지 전 층 로봇 배송으로 넓힐 계획이라고 밝혔다. | ref-1496 | 아니오 | low | 2026-07-23 | 상업 시설 | 벤더 주장 |
| f38 | [의견] | 구축자 의견: ROP 의 설비 연동 수용 기준은 건축물 인증 항목·국가 연구개발 계획과 별도 목록으로 관리하고, 발주 때 인증의 적용 판·심사 범위와 현장 설비 연결 계약을 서로 다른 증빙으로 확인하는 것이 좋다. | ref-1483, ref-322, ref-1484 | 아니오 | low | 2026-10-11 | — | — |
| f39 | [의견] | 구축자 의견: 승강기 탑승 안전 표준을 검토할 때는 판(제정·개정 일자)·적용 범위·대상 승강기 유형을 함께 기록하는 것이 좋다. | ref-314 | 아니오 | low | 2026-10-11 | — | — |
| f40 | [의견] | 구축자 의견: KOLA 가이드라인과 Open-RMF 승강기 메시지의 대응표는 표준 원문의 메시지·시험 시나리오를 확보한 뒤에 작성하는 것이 맞다. | ref-1485, ref-1486 | 아니오 | low | 2026-10-11 | — | — |
| f41 | [의견] | 구축자 의견: 장치별 세션 수락 조건(AGV 모드 전환 완료 뒤 session_id 보고 여부)을 어댑터 계약에 적고, 수락 전 탑승을 막는지 확인하는 시험을 두는 것이 좋다. | ref-1487 | 아니오 | low | 2026-10-11 | — | — |
| f42 | [의견] | 구축자 의견: 세션 유실·중복 종료·설비 상태의 세션 잔류 상황을 현장 인수 시험 항목에 넣는 것이 좋다. | ref-1488 | 아니오 | low | 2026-10-11 | — | — |
| f43 | [의견] | 구축자 의견: 실물 인계 성공을 뜻하는 센서·PLC 조건을 작업대 결과 메시지와 따로 정하고, 큐 소거가 취소·오류를 뜻하는 경우를 구별하는 것이 맞다. | ref-1489 | 아니오 | low | 2026-10-11 | — | — |
| f44 | [의견] | 구축자 의견: 제조사 승강기 어댑터를 검토할 때는 공개 어댑터의 판과 별도로 현행 API 판·권한 범위·건물 등록·세션 유지 조건을 확인하는 것이 좋다. | ref-1490 | 아니오 | low | 2026-10-11 | — | — |
| f45 | [의견] | 구축자 의견: 자동문 연동에서는 문 열기 API 자격증명과 별도로 로봇의 공간별 출입 권한과 비상 우선권을 누가 정하는지 확인해야 한다. | ref-1491, ref-1495 | 아니오 | low | 2026-10-11 | — | — |
| f46 | [의견] | 구축자 의견: ROP 장애 복구와 건물 설비의 비상 복귀를 따로 시험하고, 화재 뒤 설비 재시작 같은 수동 복귀의 책임자를 정해 두는 것이 좋다. | ref-1492 | 아니오 | low | 2026-10-11 | — | — |
| f47 | [의견] | 구축자 의견: ROP 는 준비·허가·이송·완료의 의미를 현장 PLC·작업대와 합의하고, 물리 인계 완료를 상위 작업 완료에 연결하는 것이 좋다. | ref-202, ref-1493 | 아니오 | low | 2026-10-11 | — | — |
| f48 | [의견] | 구축자 의견: 병원·호텔·그래프·지도 연구의 승강기 결과를 국내 다층 물류센터 처리량으로 옮기는 것은 보류하고, 승강기 가동률·통신 상태·카 내부 점유를 나눠 수집해 현장별 임계값을 새로 검증하는 것이 맞다. | ref-943, ref-103, ref-321, ref-163 | 아니오 | low | 2026-10-11 | — | — |
| f49 | [의견] | 구축자 의견: 설비 API 연동과 로봇팔 버튼 조작을 서로 다른 승강기 연결 방식으로 기록하고, 공유 승강기 지연 시험을 따로 두는 것이 좋다. | ref-163, ref-943 | 아니오 | low | 2026-10-11 | — | — |
| f50 | [의견] | 구축자 의견: 기존 건물 도입 사례는 연동 설비 목록과 실제 운영 중인 로봇 종류·층 범위를 고객 측 자료로 따로 확인하기 전에는 운영 실증으로 세지 않는 것이 맞다. | ref-1496 | 아니오 | low | 2026-10-11 | — | — |

### 근거 발췌

- **f1**: 초록: "comparative analysis … REEC … and Barrier-Free (BF) Certification … design standards were derived". 서지 Architectural Research 28(1), 논문번호 14(Crossref). 본문 미열람이라 연구 방법(현장 실험 여부)은 단정하지 않음
- **f2**: 스마트투데이 2025-05-28 기사: 착수보고회 29일, "이번 R&D는 2028년까지 완료될 예정". 국토부 보도자료 원문(ref-322)은 열지 못해 사업기간 2025~2028 과 보도·배포일은 2차 보도 기준
- **f3**: 기사: 세부 중점과제 "△기술 실증을 통한 기술표준 및 인증제도 개선방안 마련" 포함 세 가지. 보도자료 원문 미열람(ref-322), 이후 완료·인증 시행 여부 미확인
- **f4**: 표준 이력사항 표: 2021-11-30 제정 '수요조사 반영에 의한 제정', 2022-12-09·2025-05-09 개정 '사회적 요청에 의한 개정'. 기존 '2021년 11월 제정' 서술과 맞고 개정 2회가 새 내용. 표준 본문·신구대비표 미열람
- **f5**: 적용범위: "적용 대상 엘리베이터: 병원의 환자 전용 엘리베이터를 제외한 모든 엘리베이터", 담당 국가기술표준원 기계융합산업표준과. 목록 정보만 사용, 인증 의무로 확장하지 않음
- **f6**: KOLA 보도자료(작성일 2026.03.27): "「엘리베이터와 로봇의 상호 연동을 위한 가이드라인」단체표준을 제정했다". 게시일을 제정일로 치환하지 않음. 기존 위키 제정 보도(ref-316·ref-317)를 협회 1차 자료로 보강
- **f7**: 목록 행: "B-KOLA-0001-7700 … 엘리베이터와 로봇의 상호 연동을 위한 가이드라인 … (사)대한승강기협회 … 제정 … 등록일자 2026-03-24". 정확한 제정일·본문 미확인 (발행일 미확인, 확인일 기준)
- **f8**: 보도자료: "일반사항, 시험 설비 및 시험 절차에 대한 가이드라인을 제시", "e-나라표준인증 … 무료로 다운로드가 가능". 표준 본문의 메시지·상태 정의와 Open-RMF 대응은 미확인
- **f9**: Discourse 아카이브(2024-08-21, GitHub 토론 #513): "it should not broadcast the session_id value until it has finished switching into that mode". 설계 의도 설명이며 현장 안전 동작 재현 아님
- **f10**: "Some lifts might not have a special AGV mode" — 이 경우 승강기 상태가 다른 모드 값을 보낼 이유가 없다는 설명. 모드 상수 열거는 기존 위키(2026-09-25-area10-s4)에 있음
- **f11**: Node.cpp _adapter_lift_request_update: "curr_request->session_id == msg->session_id" 분기에서 REQUEST_END_SESSION 이 아니면 갱신 발행, 맞으면 종료 발행 후 nullptr. 커밋 4cea3fe 고정 코드
- **f12**: _lift_state_update: "we keep publishing session end requests to ensure that the lift gets released"; 주석 "TODO(MXG): Make this more intelligent by scheduling the lift". 다중 플릿 배차 최적성은 입증하지 않음
- **f13**: CHANGELOG 2.13.0 (2026-06-15): "emit completion legacy state if lift is already on the level (#510)". 같은 변경기록에 2.14.0(2026-09-26)이 있어 2.13.0 을 최신판으로 부르지 않음
- **f14**: DispenseItem.cpp _get_status: request_guid 일치 시 ACKNOWLEDGED → _request_acknowledged, SUCCESS → STATE_COMPLETED, FAILED → STATE_FAILED. 커밋 4cea3fe 고정 코드
- **f15**: 주석 "The request has been received, so if it's no longer in the queue, then we'll assume it's finished." 접수 표시는 큐에 들어간 것만으로도 설정됨
- **f16**: 구현(큐 소거 → STATE_COMPLETED)에서 도출한 설계 위험 해석. 큐 소거가 실제 적재물 센서 확인과 같다는 보장은 코드에 없음
- **f17**: README: "send various lift commands to KONE API v2.0 via websocket", "get lift state from KONE API v2.0 via websocket". 2023년 고정판(KABAM-Robotics 보존 저장소, 원 저장소 안내는 sharp-rmf/kone-ros-api). 현행 KONE 계약 아님
- **f18**: "To control a live elevator, you will need to get these id & secret from KONE Personnel." The Galen 실기 시험 문구는 프로젝트 자체 보고이며 기존 위키(ref-884)에 같은 사례가 있음
- **f19**: README: "tested with the Dormakaba EL301 and ED250 models. It requires the Dormakaba IoT connector to be fitter[sic] to the above door operators." 임의 자동문 지원을 입증하지 않음
- **f20**: "Credentials to access the door's cloud API will be provided by Dormakaba." 클라우드 자격증명 제공과 건물 출입권한 승인 정책은 별개 확인 항목
- **f21**: 벤더 주장: "A PLC is housed in a lift controller box at level 6 cargo lift lobby", "via ADS … manipulating corresponding signals via dry contact. Beckhoff CX9020"; "the lift vendor upgraded the installed lift … AGV mode". 승강기 자체 PLC 아님 (발행일 미확인, 확인일 기준)
- **f22**: 벤더 주장: Table 1 #2 Fire Alarm: "Manual intervention is needed. PLC will stay in error state until it is restarted." 한 도서관 현장의 설계이므로 다른 건물의 화재 복구 조건으로 일반화하지 않음 (발행일 미확인, 확인일 기준)
- **f23**: 벤더 주장: 개요: LiftState "at a frequency of 1 Hz"; Server 절: "published to the AWS topic every 2 seconds", LiftRequest "every 1 second". 차이를 설명하는 구절 없음 — 전송 주기 결론 보류 (발행일 미확인, 확인일 기준)
- **f24**: 원문 PDF 가 접근 거부(Access Denied)로 열리지 않아 메모 서술만 근거. Lift 절은 적재 장치 리프트이며 건물 승강기 사례가 아님 (발행일 미확인, 확인일 기준)
- **f25**: 원문 미열람(접근 거부). 제조사 예시 절차이며 제조사 중립 규격이 아님 (발행일 미확인, 확인일 기준)
- **f26**: 목록: "Revision: SEMI E84-0823 - Current"(이전 E84-1109 등 Superseded), 초록: AMHS 와 생산 설비 사이 "carrier handoffs (load/unload)" 신호 정의. 표준 본문 미열람 (발행일 미확인, 확인일 기준)
- **f27**: SEMI 다운로드 페이지가 봇 차단으로 열리지 않아 작성일(2025-12-17)·승인일·내용은 메모 서술만 근거. 개발 제안 승인과 표준 발행은 구분 (발행일 미확인, 확인일 기준)
- **f28**: Discussion: "should be interpreted as site-specific and is expected to require recalibration when applied to other hospital environments"; 승강기 카 크기·운반 카트·이용자 구성 차이를 이유로 듦
- **f29**: 초록 "We analyzed 122 non-urgent missions", §3.1 "The overall success rate across all trials was 87.03%". 'all trials' 의 범위 정의 없음. oq-215 근거 보강용이며 수치 자체는 기존 위키에 있음
- **f30**: ref-943 초록 "An increased EOR also prolonged the delivery time"; ref-163 결과 "6층에서 7층으로 이동하는 구간의 경우 외부 이용자에 의해 엘리베이터가 다른 층으로 이동하는 지연이 발생". 기관이 다른 독립 출처(질적 관찰)
- **f31**: 실험 설정: 거리는 "derived from the actual hotel floor plan and floor height", 수요는 "uses random sampling to generate" 10·20·30·60건, "sets the base waiting time for elevators at 30 s". 실제 호텔 운용 성능이 아님
- **f32**: §5: "graph-based environment representing a 15-story building … n = 1, 3, 5, 7". 시뮬레이션 평가이며 실제 건물 운용 아님
- **f33**: 실험: "5층부터 9층까지 각 층의 절반 영역을 대상으로 평가를 수행", 영문 초록 "validated in the KAIST N1 building across five floors (5F–9F)". 로봇 한 대의 실물 지도 구축
- **f34**: Table 5 "Elevator Interaction Task 19 20 95%". 성공률 95% 자체는 기존 위키에 있으며 시행 횟수(19/20)가 새 내용
- **f35**: 표지·초록: "the basis for proposed changes to the BACnet standard. The contents are subject to change." 현행 ANSI/ASHRAE 135 규범 본문이 아니며 2022년 호스팅 경로는 발행일이 아님
- **f36**: "A basic example of authorization validation checks would be the right to pass through a specific door at a specific time." 모든 검사를 통과해야 출입이 허가된다는 설명
- **f37**: 벤더 주장: "From freight elevators and automatic doors to entry and exit routes, ARC serves as a means for central integration"; 전 층 확대는 "plans to expand … by the end of the year" 계획. 독립 운영 평가 없음
- **f38**: 설계 논문(ref-1483)·연구개발 계획 보도(ref-1484)는 인증 운영기관의 현행 심사 규칙이 아님. 외부 조사 메모 K01·K02 의 시사점을 정리
- **f39**: KS B 7317 이 두 차례 개정됐고 병원 환자 전용 엘리베이터를 적용 대상에서 뺀다는 목록 정보에 근거
- **f40**: 발표·목록은 대상 범위(일반사항·시험 설비·시험 절차)와 번호만 확인. 본문 미열람
- **f41**: mxgrey 권고와 AGV 모드가 없는 승강기 존재 설명에 근거
- **f42**: lift_supervisor 의 세션 종료 반복 발행 분기에 근거. 다중 플릿 배정 규칙은 구현에 없음
- **f43**: DispenseItem 의 큐 소거 완료 간주 분기에 근거
- **f44**: KONE 어댑터는 2023년 고정 공개 구현이며 자격증명을 제조사 담당자에게 받는 구조
- **f45**: Dormakaba 는 클라우드 자격증명만 제공한다고 안내하고, BACnet 백서는 인증과 권한 검사를 구분
- **f46**: HopeTechnik 복구표의 화재 경보 뒤 PLC 오류 유지·수동 재시작 요구에 근거
- **f47**: E84(반도체 범위)와 제조사 예시 절차는 서로의 적합성을 검증한 근거가 아님
- **f48**: 병원 논문의 재보정 명시, 호텔·그래프 연구의 수치 실험 성격, 로봇 한 대 실물 지도 구축이라는 조건에 근거(oq-010)
- **f49**: 병원 사례는 제어반 통신 모듈, KAIST 사례는 버튼 조작이며 두 사례 모두 공유 승강기 지연을 보고
- **f50**: Yaesu 발표의 전 층 확대는 계획이고 이기종 지원은 설계 설명

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-322 | 국토교통부 | 올해 '로봇 친화형 건축물 설계·시공 및 운영·관리 핵심기술 개발'부터 착수 (보도자료) | 미확인 | 정부·연구기관 | medium | 2026-10-11 | https://www.molit.go.kr/USR/NEWS/m_71/dtl.jsp?lcmspage=1&id=95090964 | 예 |
| ref-1484 | 스마트투데이(이재수) | "사람과 로봇이 공존하는 스마트 빌딩 앞당긴다"...국토부 산학협력단과 기술개발 착수 | 2025-05-28 | 기사 | low | 2026-10-11 | https://www.smarttoday.co.kr/ko-kr/articles/81933 | 아니오 |
| ref-1483 | Park, Y.; Park, S. (Architectural Research) | Development of Human-Centered, Robot-Adaptive Building Design Standards: Focusing on Korea’s Building Certification Systems | 2026-07-21 | 논문 | medium | 2026-10-11 | https://link.springer.com/article/10.1007/s44515-026-00016-y | 아니오 |
| ref-314 | 국가기술표준원(e-나라표준인증·KSSN) | KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법 | 2025-05-09 | 표준 | medium | 2026-10-11 | https://www.kssn.net/search/stddetail.do?itemNo=K001010135682 | 아니오 |
| ref-1485 | 대한승강기협회(KOLA) | 대한승강기협회, 엘리베이터-로봇 연동 단체표준 제정(26.3.27) | 2026-03-27 | 정부·연구기관 | medium | 2026-10-11 | https://kola.or.kr/pages/61/68/bbs/5705 | 아니오 |
| ref-1486 | 국가기술표준원(e-나라표준인증) | 단체표준 목록 — B-KOLA-0001-7700 엘리베이터와 로봇의 상호 연동을 위한 가이드라인 | 미확인 | 정부·연구기관 | high | 2026-10-11 | https://www.standard.go.kr/KSCI/grpstd/getGrpStdCrtfcReqst.do?menuId=60372&topMenuId=502&upperMenuId=503 | 아니오 |
| ref-1487 | cwrx777; mxgrey (Open Robotics Discourse 아카이브) | Lift session issues - Robot enter lift while lift is still in human mode (#513) | 2024-08-21 | 오픈소스 문서 | medium | 2026-10-11 | https://discourse.openrobotics.org/t/lift-session-issues-robot-enter-lift-while-lift-is-still-in-human-mode-513/44679 | 아니오 |
| ref-1488 | Open-RMF (open-rmf/rmf_ros2 저장소) | rmf_fleet_adapter/src/lift_supervisor/Node.cpp (commit 4cea3fe) | 미확인 | 오픈소스 문서 | high | 2026-10-11 | https://github.com/open-rmf/rmf_ros2/blob/4cea3fe97d4fcafdebd5590247c42b28664e2b55/rmf_fleet_adapter/src/lift_supervisor/Node.cpp | 아니오 |
| ref-1398 | Open-RMF (open-rmf/rmf_ros2 저장소) | Changelog for package rmf_fleet_adapter | 2026-09-26 | 오픈소스 문서 | high | 2026-10-11 | https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst | 아니오 |
| ref-1489 | Open-RMF (open-rmf/rmf_ros2 저장소) | rmf_fleet_adapter/src/rmf_fleet_adapter/phases/DispenseItem.cpp (commit 4cea3fe) | 미확인 | 오픈소스 문서 | high | 2026-10-11 | https://github.com/open-rmf/rmf_ros2/blob/4cea3fe97d4fcafdebd5590247c42b28664e2b55/rmf_fleet_adapter/src/rmf_fleet_adapter/phases/DispenseItem.cpp | 아니오 |
| ref-1490 | CHART; KABAM-Robotics 보존 저장소 | KONE RMF Lift Adapter / kone-ros-api — README (commit 9bc3a87) | 미확인 | 오픈소스 문서 | medium | 2026-10-11 | https://github.com/KABAM-Robotics/lift_kone_adapter/tree/9bc3a87a01eea66c606e0a256e1cd8a8c60bc596 | 아니오 |
| ref-1491 | Open-RMF (open-rmf/door_adapter_dormakaba 저장소) | door_adapter_dormakaba — README (commit 2cf76a6) | 미확인 | 오픈소스 문서 | high | 2026-10-11 | https://github.com/open-rmf/door_adapter_dormakaba/tree/2cf76a6b83ceee31540aeb7e0d7feb2a10042668 | 아니오 |
| ref-1492 | HopeTechnik (RMF Systems Engineering Handbook) | Lift and Doors Integration | 미확인 | 벤더 문서 | medium | 2026-10-11 | https://trl-rmf.github.io/website/content/lift-door-integration.html | 아니오 |
| ref-1493 | OMRON | LD-Series Integration Guide (I680-E-02) | 미확인 | 벤더 문서 | medium | 2026-10-11 | https://www.omron.com.tw/data_pdf/mnu/i680-e-02_ld.pdf?id=3664 | 예 |
| ref-202 | SEMI | E08400 - SEMI E84 - Specification for Enhanced Carrier Handoff Parallel I/O Interface | 미확인 | 표준 | medium | 2026-10-11 | https://store-us.semi.org/products/e08400-semi-e84-specification-for-enhanced-carrier-handoff-parallel-i-o-interface | 아니오 |
| ref-1494 | SEMI Physical Interfaces & Carriers TC (Japan) | SNARF for Doc 7442: Specification for Enhanced Handoff Interface | 미확인 | 표준 | medium | 2026-10-11 | https://downloads.semi.org/web/wstdsbal.nsf/18a679096dfd445188256d35007d447d/0db3fe2c9bb0eb2488258d9400027699!OpenDocument | 예 |
| ref-943 | Lee, Y. 외 (고려대학교 구로병원, 도구공간; Digital Health) | Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments | 2026-03-31 | 논문 | high | 2026-10-11 | https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/ | 아니오 |
| ref-103 | Han, L.; Ding, J.; Liu, S.; Meng, M. (Sensors 25(6):1783) | The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments | 2025-03-13 | 논문 | high | 2026-10-11 | https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/ | 아니오 |
| ref-321 | Kim, S.; Jang, H.; Ha, J.; Lee, D.; Ha, Y.; Song, Y. E. (Electronics 14(5):982) | Efficient Graph-Based Multi-Story Path Planning with Optimized Elevator Selection for Indoor Delivery Robots | 2025-02-28 | 논문 | high | 2026-10-11 | https://doi.org/10.3390/electronics14050982 | 아니오 |
| ref-163 | 노주형, 강규리, 김연찬, 심현철(로봇학회 논문지 21(1):48–57) | 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템 | 2026-03 | 논문 | high | 2026-10-11 | https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667 | 아니오 |
| ref-1495 | SSPC 135 LSS-WG; Isler, B. 외 (BACnet International) | Physical Access Control with BACnet (BAC-09-08 White Paper) | 2008-09-27 | 표준 | medium | 2026-10-11 | https://bacnet.org/wp-content/uploads/sites/4/2022/08/BAC-09-08.pdf | 아니오 |
| ref-1496 | NAVER LABS | NAVER’s ARC Goes to Japan | 2026-07-23 | 벤더 문서 | low | 2026-10-11 | https://naverlabs.com/en/blogDetail?seq=10034507 | 아니오 |

### 출처 요약

- **ref-322**: 원문 미열람. 외부 조사 메모가 인용한 같은 국토부 보도자료('AI 품은 건축물, 이제는 스마트+빌딩 시대', CODIL 보존본 포함)로, 이번에도 MOLIT·CODIL 원문을 열지 못해 보도·배포일과 쪽수는 확인하지 못했다.
- **ref-1484**: 국토부 스마트+빌딩 연구개발 착수 보도. 2028년까지 완료 예정과 기술 실증을 통한 기술표준·인증제도 개선방안 등 세부 과제를 전한다.
- **ref-1483**: 로봇 친화형 건축물 인증과 무장애 인증을 비교해 로봇 적응형 건축 설계 기준을 도출한 논문(28(1), 논문번호 14). 초록과 Crossref 서지만 확인했고 본문은 열지 못했다.
- **ref-314**: KS B 7317 표준 정보. 이번에 e-나라표준인증 상세 페이지에서 제정(2021-11-30)·개정(2022-12-09, 2025-05-09) 이력과 적용 범위·표준개발협력기관을 확인했다. 표준 본문은 미열람.
- **ref-1485**: KOLA 의 「엘리베이터와 로봇의 상호 연동을 위한 가이드라인」 단체표준 제정 보도자료. 대상(일반사항·시험 설비·시험 절차), 협의체 구성, e-나라표준인증 무료 다운로드를 안내한다.
- **ref-1486**: e-나라표준인증 단체표준 목록 검색 결과. KOLA 가이드라인의 표준번호 B-KOLA-0001-7700, 상태 제정, 등록일자 2026-03-24 를 보여 준다. 표준 본문은 미열람.
- **ref-1487**: Open-RMF GitHub 토론 #513 의 Discourse 아카이브. 승강기가 AGV 모드로 바뀌기 전 로봇이 탑승한 문제와, 모드 전환 뒤에 session_id 를 보고하라는 개발자 답변을 담는다.
- **ref-1488**: Open-RMF 승강기 감독자 구현. 같은 세션 요청의 갱신·종료 처리와, 활성 요청 없이 남은 세션에 종료 요청을 반복 발행하는 분기를 담는다.
- **ref-1398**: rmf_fleet_adapter 변경기록. 이번에 2.13.0(2026-06-15)의 승강기가 이미 해당 층에 있을 때 완료 상태를 내보내는 변경(#510)을 확인했다.
- **ref-1489**: Open-RMF 배송 작업의 디스펜서 단계 구현. 결과 메시지(ACKNOWLEDGED·SUCCESS·FAILED)와 상태 큐 소거로 완료를 판정하는 조건을 담는다.
- **ref-1490**: Open-RMF 승강기 메시지와 KONE API v2.0 을 WebSocket 으로 잇는 공개 어댑터 README(원 저장소 안내는 sharp-rmf/kone-ros-api). 실제 승강기 제어 자격증명을 KONE 담당자에게 받도록 안내한다.
- **ref-1491**: Dormakaba 스마트 문용 Open-RMF 문 어댑터 README. EL301·ED250 시험, IoT connector 장착 요구, 문 클라우드 API 자격증명 제공 주체를 적는다.
- **ref-1492**: 한 도서관 현장의 승강기·문 연동 설계와 복구 설명. 승강기 제어함 PLC(Beckhoff CX9020)·드라이 접점 연결, AGV 모드 개조, 화재 경보 시 복구 절차와 메시지 주기를 적는다.
- **ref-1493**: 원문 미열람. OMRON LD 시리즈 이동로봇 통합 안내서로, 외부 조사 메모는 적재물 인계 예시 절차를 담는다고 전한다. 이번 검증에서 접근 거부로 열지 못했다.
- **ref-202**: SEMI E84 판매 목록. 이번에 E84-0823 이 현행판(Current)으로 표시되고 AMHS–생산 설비 캐리어 인계 범위를 설명하는 초록을 확인했다. 표준 본문은 미열람.
- **ref-1494**: 원문 미열람. E84 를 바탕으로 한 새 인계 인터페이스 표준 개발 제안서로 외부 조사 메모가 전한다. 이번 검증에서 봇 차단으로 열지 못해 작성·승인일은 미확인이다.
- **ref-943**: 혼잡한 병원에서 승강기 이용을 고려한 자율 약품 배송 로봇 실증. 이번에 EOR 임계값의 재보정 필요 명시, 배송 지연 관찰, 전체 성공률 분모 설명 부재를 다시 확인했다.
- **ref-103**: 다층 호텔 로봇 배송 경로계획 수치 실험. 실제 호텔 평면으로 거리 행렬을 만들고 수요는 무작위 생성했으며 승강기 기본 대기 30초·운행 40~100초를 둔다.
- **ref-321**: 실내 배송 로봇의 승강기 선택을 최적화한 그래프 기반 다층 경로계획. 15층 건물 그래프에서 소포 1·3·5·7개 시나리오로 평가했다.
- **ref-163**: 탐사와 승강기 연계로 다층 실내 지도를 자율 구축한 KAIST 연구. KAIST N1 5~9층 각 층 절반 영역 평가, 승강기 상호작용 19/20 성공, 외부 이용자로 인한 승강기 지연을 보고한다.
- **ref-1495**: BACnet 으로 출입통제를 구현하기 위한 확장을 설명한 124쪽 백서. 표준 변경 제안의 기초 작업 문서이며 인증과 권한 검사를 구분한다.
- **ref-1496**: NAVER 다중 로봇 플랫폼 ARC 의 Tokyo Midtown Yaesu 도입 소개. 기존 화물 승강기·자동문 연동과 연말 전 층 확대 계획을 공급자 관점에서 설명한다.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/integration/facility-and-building-system-integration.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | 갱신(차등): 섹션 3 — 국토부 연구개발의 2028년 완료 예정·기술표준·인증제도 개선 과제(f2·f3, 보도자료 원문 미열람이라 [추정]·'2차 보도 기준', 보도 날짜는 2025-05-28 기사 기준이며 ref-322 발행일은 미확인 유지). KS B 7317 문장은 기존 '2021년 11월 제정'을 유지하고 개정 이력(2022-12-09·2025-05-09)과 적용 범위(병원 환자 전용 엘리베이터 제외)를 덧붙임(f4·f5); ref-314 발행일을 현행 개정일 2025-05-09 로 갱신 제안 / 섹션 4(분리 2026-09-25-area10-s4) — '승강기 세션과 모드' 항목에 AGV 모드 전환 완료 뒤 session_id 보고 권고와 AGV 모드 없는 승강기(f9·f10); LiftState session_id 정의·모드 상수는 기존 내용 확인(같은 페이지 승강기 세션 항목, 2026-10-10-charging-threshold-charger-lift-evidence, 2026-09-25-area16-s4)이라 새로 넣지 않음 / 섹션 5 — 현장 유형 '기타(도서관)' 실제 설비 연결 사례: 새로 단 승강기 제어함 PLC(Beckhoff CX9020)·ADS·드라이 접점·승강기 업체 AGV 모드 개조(f21), 화재 경보 뒤 PLC 오류 유지·수동 재시작(f22), 메시지 주기 기재 불일치는 결론 없이(f23). '상업 시설' 사례로 NAVER ARC Yaesu(f37, 벤더 주장·계획 구분, f50) / 섹션 6 — 어댑터 요청·상태 감독: lift_supervisor 의 같은 세션 갱신·종료 처리와 잔류 세션 종료 반복 발행, 배정 규칙 미구현 TODO(f11·f12), 변경기록 2.13.0 #510(f13, 2.14.0 존재 병기); lift_supervisor 존재 자체는 기존 내용 확인(categories/integration/index.md 110행). 요청–결과 인계: DispenseItem 의 SUCCESS 완료·큐 소거 완료 간주(f14·f15)와 위험 해석(f16, [추정]); DispenserResult·IngestorResult 의 ACKNOWLEDGED·SUCCESS·FAILED 값 정의는 기존 내용 확인(planning-and-optimization/task-and-workflow-modeling.md 86행)이라 넣지 않음. 제조사 어댑터: KONE API v2.0 WebSocket·자격증명(f17·f18; The Galen 실기 시험은 기존 내용 확인 — ref-884, robot-ontology/ontology-based-system-and-robot-integration.md 102·113행), Dormakaba IoT connector·자격증명(f19·f20). 물리 인계 예시: OMRON(f24·f25, 원문 미열람 [추정]) / 섹션 7(분리 2026-09-25-area10-s7) — KOLA 행 '표준 번호·제정일·내용은 미확인'을 정정: 협회 보도자료(f6·f8, 게시일 2026-03-27)와 e-나라표준인증 목록 B-KOLA-0001-7700·등록일자 2026-03-24(f7)를 날짜가 다르다는 점과 함께, 메시지·RMF 대응은 미확인 유지; 제정 사실 자체는 기존 내용 확인(같은 페이지 ref-316, 2026-09-25-area10-s8 ref-317). KS B 7317 행에 개정 이력·적용 범위(f4·f5). SEMI E84 행 추가 또는 2026-09-25-area17-s7 41행 연결: E84-0823 현행판(f26), Doc7442 개발 제안(f27, 원문 미열람 [추정]). BACnet 출입통제 백서는 표준 변경 제안 작업 문서로(f35·f36) / 섹션 8(분리 2026-09-25-area10-s8) — '원문을 열지 못해 결과 수치는 쓰지 않는다' 문장 갱신: 병원 논문의 EOR 임계값 재보정 명시(f28, 새 내용), 공유 승강기 지연 독립 교차 확인(f30), Han 외는 실제 평면으로 거리 행렬만·수요는 무작위 표본·기본 대기 30초(f31), Kim 외 15층·소포 1·3·5·7(f32), 노주형 외 N1 5~9층 각 층 절반 영역·19/20(f33·f34). Park·Park 설계 기준 논문은 '초록 기준'으로(f1). 기존 내용 확인으로 넣지 않는 것: 병원 논문의 122건·실패 14건 분류(통신 2·막힘 8)·87.03%·59.01%·95.52%(objects-people-and-live-state/people-and-pedestrian-model.md 101~108행, 2026-09-29-area63-s4·s6·s8, design-and-simulation/virtual-commissioning-and-real-situation-replay.md, 2026-09-25-area03-s8), Han 외 승강기 운행 40~100초(planning-and-optimization/shared-resource-charging-and-energy-optimization.md 96~108행, 2026-09-25-area28-s3), 노주형 외 5개 층·27분·95%·버튼 조작(chat-based-configuration-and-operation/chat-map-authoring.md 113행, 2026-09-25-area06-s8, 2026-09-25-area21-s8) / 섹션 9 — 설비 제어 경계: 화재 복구·PLC 재시작은 연계 대상(설비), ROP 는 복구 책임자 지정과 시험(f22·f46); 출입통제는 문 열기 요청과 통행 권한 승인 분리(f36·f45) / 섹션 10(분리 2026-09-25-area10-s10) — 63. 병원·의료(f28·f30), 64. 상업 시설(f37·f1), 51. 인증·권한·격리(f35·f36·f45), 30. 로봇 간 협업·물리적 인계(f14~f16·f24~f27), 32. 예외 복구·재계획·업무 연속성(f22), 50. 안전 표준·인증·사고 조사(f4·f5) / 섹션 11(분리 2026-09-25-area10-s11) — 부분 근거만, 모두 열림 유지: oq-010(f28·f30~f34·f48), oq-041(f6~f10·f40), oq-283(f7 표준 번호 공개, 책임 분담은 미확인), oq-042(f24~f27·f47), oq-062(f26·f27), oq-043(f19·f20·f35·f36·f45), oq-098·oq-173·oq-311(f4·f5, 조항·기준값은 미확인), oq-067·oq-094(f11·f12, 배정 규칙 미구현), oq-215(f29, 분모 설명 없음 재확인 — 새 질문 아님), oq-258·oq-328(f28). 새 질문 6건. 넣지 않는 것: 외부 메모 F01(스마트도시협회 REEC 운영 사무국 — 기존 내용 확인: glossary/robot-friendly-building-certification.md, 2026-09-29-area64-s4 41행·s7 42행; 이번 원문은 접근 제한으로 미열람), F02(평가 분야 4개 명칭 — 확인 불가이고 기존 용어집의 4개 부문 명칭(건축·시설 설계, 네트워크·시스템, 건축 운영 관리, 로봇 지원·기타 서비스)과 충돌, 원문 재확보 필요). 다음 실행 후보: 64. 상업 시설(REEC 현행 심사 기준), 30. 로봇 간 협업·물리적 인계(OMRON·Doc7442 원문 재확보), 51. 인증·권한·격리(BACnet 출입통제). |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- KS B 7317 의 2022-12-09 개정과 2025-05-09 개정은 각각 어떤 조항(요구사항·평가 방법)을 바꿨으며, 그 변경이 승강기 연동 계층이 확인해야 할 항목에 영향을 주는가? (관련 기존 질문: oq-098, oq-173, oq-311) | 관련 영역: 22. 설비·건물 시스템 연동, 50. 안전 표준·인증·사고 조사 | 근거: f4 | 종류: 일반
- 로봇 친화형 건축물 인증의 현행 심사 기준은 어느 판이며, 승강기·자동문·출입통제 연동 항목을 어떤 시험이나 서류로 심사하는가? (관련 기존 질문: oq-179) | 관련 영역: 22. 설비·건물 시스템 연동, 64. 상업 시설 | 근거: f1 | 종류: 일반
- KONE 의 현행 공식 승강기 API 계약(지원 승강기, 건물 등록, 권한 범위, 세션 유지 조건)은 2023년 고정판 공개 RMF 어댑터가 전제한 KONE API v2.0 연결 조건과 어떻게 다른가? | 관련 영역: 22. 설비·건물 시스템 연동, 20. 로봇·제조사 관제 연동 | 근거: f17 | 종류: 일반
- SEMI Doc 7442(E84 를 출발점으로 한 새 인계 인터페이스와 TCP/IP 하위 규격) 개발 제안은 승인 뒤 표준으로 발행됐는가, 반도체 밖 이동로봇–설비 인계에도 쓸 수 있는 범위인가? (관련 기존 질문: oq-042, oq-062) | 관련 영역: 22. 설비·건물 시스템 연동, 30. 로봇 간 협업·물리적 인계 | 근거: f27 | 종류: 일반
- HopeTechnik 승강기·문 연동 문서가 승강기 상태 전송 주기를 1 Hz 와 2초마다로 다르게 적은 것은 어느 쪽이 실제 구현·설정이며, 이런 주기 차이가 설비 상태를 믿을 수 있는 경과 시간 판단에 어떤 영향을 주는가? (관련 기존 질문: oq-034) | 관련 영역: 22. 설비·건물 시스템 연동, 18. 실시간 세계 상태·데이터 일관성 | 근거: f23 | 종류: 일반
- NAVER ARC 의 Tokyo Midtown Yaesu 도입에서 기존 화물 승강기·자동문 연동이 실제로 운영 중인 층·로봇 종류·제조사 범위는 어디까지이며, 공급자 밖의 독립 운영 평가가 있는가? | 관련 영역: 22. 설비·건물 시스템 연동, 64. 상업 시설 | 근거: f37 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 22 · 교차 확인: 1
- 예산 사용량: 검색 0회 · 신규 출처 14건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-11-03/external_research.md)를 변환했다. 2026-10-11 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.
    - f2·f3: 국토부 보도자료 원문(MOLIT·CODIL)을 열지 못해 사업기간 2025~2028, 보도 2025-05-28·배포 2025-05-27, '3쪽'은 미확인 — 2차 보도(ref-1484) 기준 [추정]
    - f1: Park·Park 논문은 초록·Crossref 서지만 확인(본문 미열람). 메모의 '현장실험이 아닌 기존 인증기준 비교' 중 '현장실험이 아닌'은 단정하지 않음. 메모 서지 '28,14' 는 28(1), 논문번호 14 로 정정
    - 메모 F01(스마트도시협회 REEC 운영 사무국)·F02(평가 분야 4개): 스마트도시협회 페이지가 접근 제한으로 열리지 않음. F02 명칭은 기존 용어집 4개 부문 명칭과 달라 충돌 — 원문 재확보 필요, 출처·finding 에서 뺌
    - f7: e-나라표준인증 목록의 등록일자(2026-03-24)와 KOLA 게시일(2026-03-27)이 다르며 정확한 제정일은 미확인. 가이드라인 본문의 메시지·상태 정의, Open-RMF 대응 미확인
    - f4·f5: KS B 7317 표준 본문·신구대비표 미열람 — 개정 조항 미확인
    - f24·f25: OMRON I680-E-02 PDF 접근 거부(Access Denied)로 원문 미열람 — 메모 서술만 근거라 [추정], 메모의 2023-05 판 날짜도 미검증
    - f27: SEMI Doc 7442 SNARF 페이지 봇 차단으로 원문 미열람 — 작성일 2025-12-17·승인일 2025-12-18 미검증, [추정]
    - 커밋 일자 4건(rmf_internal_msgs 2a7f01b 2026-09-22, rmf_ros2 4cea3fe 2026-10-08, KONE 어댑터 9bc3a87 2023-07-13, door_adapter_dormakaba 2cf76a6 2025-06-16)은 확인하지 못해 해당 출처 published 를 null 로 둠
    - f17·f18: KONE 어댑터 README 는 KABAM-Robotics 보존 저장소 판이며 원 저장소(sharp-rmf/kone-ros-api)와 현행 KONE 공식 API 계약은 대조하지 않음. The Galen 실기 시험은 프로젝트 자체 보고
    - f23: HopeTechnik 문서의 1 Hz/2초 차이를 설명하는 구현·설정 근거 없음. 문서 발행일 미확인
    - f29: 87.03% 의 분모는 원문으로 설명되지 않음(oq-215 열림 유지)
    - f37: NAVER Yaesu 운영 범위는 공급자 블로그뿐이며 독립 평가 없음(벤더 주장)
    - 메모 U06(현대엘리베이터 현행 API 원문)·U07(TTA 10.1486 본문)은 이번 메모에 근거 finding 이 없어 열린 질문으로 올리지 않음
    - 벤더 문서만 근거인 f21~f23 은 원문 대조로 문서 내용은 확인했으나, 저장소 규칙(6.2 항목 13)에 따라 독립 출처 교차 확인 전까지 vendor_claim: true·[추정]으로 둔다.
- 범위 경계 위반 의심:
    - f19·f21·f22: 문 구동기 하드웨어(IoT connector), 승강기 제어함 PLC·드라이 접점, 화재 경보 시 설비 복귀는 분류 원문 19장의 '승강기·컨베이어·PLC·설비 안전 제어' 연계 대상이므로 claim 을 '연계 대상: '으로 시작하고, ROP 몫은 요청·상태 확인과 복구 책임 정의(f46)로 한정
    - f4·f5·f39: KS B 7317 은 로봇 자체의 탑승 안전 요구사항으로 이 영역에는 제약 조건·판 정보로만 씀(48·50번 안전 영역 쪽 내용)
    - f35·f36·f45: BACnet 출입통제의 권한 검사는 51. 인증·권한·격리 쪽 내용이 많아 이 영역에는 문 열기 요청과 통행 승인 분리 근거로만 씀
    - f26·f27·f47: SEMI E84·Doc7442 는 반도체 업종 규격으로 이 영역에는 인계 신호 구조의 참고로만 쓰고 물류센터 적용을 주장하지 않음
    - f28~f30: 병원 승강기 연구의 수치는 63. 병원·의료에서 이미 다루므로 이 영역에는 새 내용(재보정 명시·지연 교차 확인·분모 재확인)만 씀
- 한계: 외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 14건/15(ref-1483~ref-1496, 예약 구간 ref-1483~ref-1512 안), 재사용 8건(ref-322·ref-314·ref-1398·ref-202·ref-943·ref-103·ref-321·ref-163). 출처 매핑(검증 결과 기준): 메모 n2→ref-1483, n3→ref-322(같은 국토부 보도자료, 기존 제목·URL 유지)+2차 보도 ref-1484, n4→ref-314(e-나라표준인증 상세로 열람, 발행일을 현행 개정일 2025-05-09 로 갱신), n5→ref-1485, KOLA 표준 번호→e-나라표준인증 단체표준 목록 ref-1486, n7→CHANGELOG ref-1398·lift_supervisor ref-1488·DispenseItem ref-1489, n8→ref-1487, n9→ref-1490, n10→ref-1491, n11→ref-1492, n12→ref-1493(미열람), n13→ref-202, n14→ref-1494(미열람), n15→ref-943, n16→ref-103, n17→ref-321, n18→ref-163, n19→ref-1495, n20→ref-1496. n1(스마트도시협회)은 근거 finding 이 기존 내용 중복(F01)·충돌(F02)이라 출처에서 뺐고, n6(rmf_internal_msgs: ref-286·ref-499·ref-049)은 근거 finding 이 기존 내용 중복(LiftState session_id 정의, 결과 상태값 정의)이라 넣지 않음. 기존 ref 갱신 제안: ref-103 저자(Han, L. 외)·발행일 2025-03-13, ref-321 저자(Kim, S. 외)·발행일 2025-02-28, ref-163 발행일 2026-03·권호 21(1), ref-314 발행일 2025-05-09·이력, ref-202 현행판 E84-0823. fetched: true 는 검증 서브에이전트가 2026-10-11 원문을 내려받아 대조한 출처이고, fetched: false 는 ref-322·ref-1493·ref-1494. ref-1483 은 초록·서지만 확인. 교차 확인 1건(f30: 고려대 구로병원·도구공간 논문과 KAIST 논문, 서로 다른 기관의 질적 관찰). 메모 X01 외 나머지는 단일 출처라 신뢰도 medium 이하. 벤더 주장은 f37(vendor_claim, [추정]). 현장 유형: 병원(f28·f29), 기타(도서관, f21~f23), 상업 시설(f37). 물류창고 실측 자료는 이번에도 없음(oq-010 열림). 열린 질문 해결 제안 없음 — 모두 부분 근거: oq-010 근거 f28·f30~f34·f48, oq-041 근거 f6~f10·f40, oq-283 근거 f7, oq-042 근거 f24~f27·f47, oq-062 근거 f26·f27, oq-043 근거 f19·f20·f35·f36·f45, oq-098·oq-173·oq-311 근거 f4·f5, oq-067·oq-094 근거 f11·f12, oq-215 근거 f29, oq-258·oq-328 근거 f28. 메모의 '새1~새3'은 고유 id 가 없는 질문이 아니라 docs/open-questions.md 의 oq-041·oq-042·oq-043 과 같은 질문임을 질문 문장으로 확인했다. 메모 U01=oq-010, U02=oq-041·oq-283, U09=oq-042, U10=oq-043, U13=oq-215 이므로 새로 만들지 않았다. 메모의 '.research-work' 로컬 보존본 경로·행 번호는 저장소에 없어 쓰지 않고 실제 위키 위치를 적었다. 정정 요청 없음. 용어 후보 없음.
