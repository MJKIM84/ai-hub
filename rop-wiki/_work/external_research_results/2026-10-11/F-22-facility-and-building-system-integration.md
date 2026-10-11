---
area: 22
title: "22. 설비·건물 시스템 연동"
researched: 2026-10-11
researcher: "OpenAI Codex"
---

# 22. 설비·건물 시스템 연동 — 보완 조사

## 요약

- 국내 인증기관의 운영 설명, 국가 연구개발 계획, KS·협회 표준을 증빙 종류별로 구분했다. K01~K04 참조.
- RMF 세션 수락·해제와 작업대 완료 판정의 코드 근거를 보강했다. K05~K07 참조.
- 제조사 어댑터, PLC 연결, 물리 인계 예시는 적용 판과 현장 조건을 함께 기록했다. K08~K11 참조.
- 병원 실물 관찰, 호텔·그래프 수치실험, 버튼 조작 연구를 구분했다. 국내 물류센터 처리량으로의 전용은 보류한다. K12~K13 참조.
- 원문 열람18/20(90%). 독립 교차 확인은 질적 관찰 X01 한 건으로 한정하며, 법정 인증 의무·표준 미열람 조항·벤더 운영 성능은 확정하지 않았다.

## 보완 항목

대상 문장 전체는 작업폴더의 위키 보존본과 부록 A 진단표에서 추적한다. 긴 위키 문장을 반복 인용하는 대신 절·문장 주제를 식별한다. F번호는 부록 D의 원문 재대조 행과 연결된다. 코드 링크의 커밋은 각주에 고정했다.

### K01 [7. 표준·오픈소스 — REEC 운영기관과 설계 연구 추가]

- F01. 스마트도시협회는 로봇 친화형 건축물 인증(REEC)의 운영 사무국을 공개하고 있다. [사실][^n1]
- F02. 그 평가 분야에는 건축·시설물, 네트워크·시스템, 로봇 운영 관리, 서비스 구현 수준이 포함된다. [사실][^n1]
- F03. Park와 Park의 2026년 설계 연구는 현장실험이 아닌 기존 인증기준 비교로 기준을 도출했다. [사실][^n2]
- 근거 메모: Q1. 기관 설명과 그 설명을 인용한 설계 논문은 인증 운영의 독립 교차 검증이 아니다. REEC 소개·연혁의 열람일은2026-10-11이며 게시일·기준의 세부 판은 미확인이다. 논문의 설계 제안을 인증기관의 현행 심사 규칙으로 바꾸지 않는다. 각 사실의 직접 구절·위치는 부록 D 참조.
- ROP 시사점: ROP의 설비 연동 수용기준과 건축물 인증 항목을 별도 목록으로 관리하고, 실제 적용 판·심사 범위를 발주 시 확인하는 편이 좋다. [의견]

### K02 [3. 중요성·국내 동향 — 국토부 연구계획의 날짜·상태 수정]

- 대상 문장 식별: 부록 A의 국토부 발행일·연구개발 항목.
- F04. 국토교통부 보도자료는 로봇 친화형 건축물 핵심기술 개발의 사업기간을 2025~2028년으로 제시한다. [사실][^n3]
- F05. 같은 자료는 기술 실증 결과를 토대로 기술표준·인증제도 등의 개선 방안을 마련할 계획이라고 설명한다. [사실][^n3]
- 근거 메모: Q1. 보도2025-05-28과 배포2025-05-27을 구분한다. 이 자료는2025-10~2026-10 조사창보다 앞선 기준 자료다. 사업 착수와 인증 시행을 구분하며 이후 완료 여부는 확인하지 못했다. 각 사실의 직접 구절·위치는 부록 D 참조.
- ROP 시사점: R&D 계획, 민간 인증기관의 운영 설명, 현장 설비 연결 계약을 각각 다른 증빙으로 관리하는 편이 좋다. [의견]

### K03 [7. 표준·오픈소스 — KS B 7317 개정 이력 수정]

- 대상 문장 식별: 부록 A의 KS B7317 2021년판 항목.
- F06. KS B 7317의 공식 이력은 2025-05-09 변경을 ‘개정’으로 기록한다. [사실][^n4]
- F07. 공식 목록의 적용 대상 엘리베이터는 병원 환자 전용 엘리베이터를 제외한다. [사실][^n4]
- 근거 메모: Q1·Q2. KS 목록의 최종개정확인일이라는 통합필드만 보지 않고 이력의 ‘개정’ 구분을 확인했다. 표준 본문은 미열람이다. 적용범위는 목록이 제공하는 범위까지만 사용하고 인증 의무나 안전 적합성 판단으로 확장하지 않는다. 각 사실의 직접 구절·위치는 부록 D 참조.
- ROP 시사점: 안전 표준 검토에는 판·범위·대상 승강기 유형을 함께 기록해야 한다. [의견]

### K04 [7. 표준·오픈소스 — KOLA 제정 발표의 확인 범위 수정]

- 대상 문장 식별: 부록 A의 협회표준 번호·제정일 미확인 항목.
- F08. KOLA는 2026-03-27 게시물에서 ‘엘리베이터와 로봇의 상호 연동을 위한 가이드라인’ 단체표준을 제정했다고 발표했다. [사실][^n5]
- F09. 그 발표는 가이드라인의 대상으로 일반사항, 시험 설비, 시험 절차를 열거한다. [사실][^n5]
- 근거 메모: Q2. C06 보도자료 전문을 읽었으며 단체표준 본문을 읽은 것으로 계산하지 않는다. 게시일을 제정일로 치환하지 않는다. 표준번호·메시지·RMF 매핑은 미확인이다. 각 사실의 직접 구절·위치는 부록 D 참조.
- ROP 시사점: KOLA–RMF 매핑은 원문 표준의 메시지와 시험 시나리오를 확보한 뒤 작성해야 한다. [의견]

### K05 [4. 구성 요소 — 승강기 세션 수락의 의미 추가]

- F10. RMF LiftState의 session_id는 승강기 제어를 부여받은 세션을 나타내도록 정의되어 있다. [사실][^n6]
- F11. 2024년 개발자 답변은 안전한 세션 수행에 AGV 모드가 필요한 장치라면 모드 전환을 마친 뒤 session_id를 내보내라고 권고한다. [사실][^n8]
- F12. 그 답변은 별도 AGV 모드가 없는 승강기도 있을 수 있다고 설명한다. [사실][^n8]
- 근거 메모: Q3. n6·n8은 같은 RMF 계열이다. 현재 고정 메시지의 의미와2024년 토론의 설계 의도를 대조했을 뿐 현재 현장의 안전 동작을 재현하지 않았다. 기존 위키의 모드 상수 열거는 새 내용으로 반복하지 않는다. 각 사실의 직접 구절·위치는 부록 D 참조.
- ROP 시사점: 장치별 세션 수락 조건을 어댑터 계약에 명시하고 수락 전 탑승을 막는 시험을 마련하는 편이 좋다. [의견]

### K06 [6. 대표 접근법 — 세션 종료와 최근 구현 변경 추가]

- F13. 고정 코드의 lift supervisor는 활성 세션이 있을 때 같은 session_id의 갱신·종료 요청을 처리하는 분기를 둔다. [사실][^n7]
- F14. supervisor에 활성 요청이 없는데 설비 상태에 세션이 남아 있으면 세션 종료 요청을 발행한다. [사실][^n7]
- F15. fleet_adapter 변경기록의 2.13.0(2026-06-15)에는 승강기가 이미 해당 층에 있을 때 legacy 완료 상태를 내보내는 변경이 실려 있다. [사실][^n7]
- 근거 메모: Q3. 커밋4cea3fe…의 해당 함수만 확인했다. CHANGELOG에는2.14.0(2026-09-26)도 있으므로2.13.0을 최신판이라 부르지 않는다. supervisor의 세션 조정은 전체 시스템의 최적 승강기 배차를 입증하지 않는다. 각 사실의 직접 구절·위치는 부록 D 참조.
- ROP 시사점: 세션 유실·중복 종료·설비 상태 잔류 상황을 현장 인수시험에 포함하는 편이 좋다. [의견]

### K07 [4. 구성 요소 — 작업대 접수·완료 조건 추가]

- F16. DispenserResult와 IngestorResult 메시지는 ACKNOWLEDGED와 SUCCESS를 서로 다른 상태값으로 정의한다. [사실][^n6]
- F17. DispenseItem 구현은 요청 ID가 일치하는 SUCCESS 수신을 완료 상태로 바꾼다. [사실][^n7]
- F18. 같은 구현은 요청을 확인한 뒤 최신 상태 큐에서 요청 ID가 사라진 경우에도 완료로 간주한다. [사실][^n7]
- 큐 소거만으로 완료 처리하면 현장 큐의 취소·실패 의미에 따라 잘못된 인계 완료 판단이 생길 수 있다. [추정][^n7]
- 근거 메모: Q5. n6·n7은 독립 출처가 아니다. ACK 단독 수신, SUCCESS 수신, ACK 이후 큐 소거를 구별한다. 상태 큐 소거는 실제 적재물의 센서 확인과 동일하다고 보장되지 않는다. 후자는 구현에서 도출한 설계 위험 해석이다. 각 사실의 직접 구절·위치는 부록 D 참조.
- ROP 시사점: 실물 인계 성공을 뜻하는 센서·PLC 조건을 별도로 정하고, 큐 소거가 취소·오류를 뜻하는 경우를 구별해야 한다. [의견]

### K08 [6. 대표 접근법 — KONE 공개 어댑터의 연결 조건 추가]

- F19. CHART의 공개 KONE 어댑터 README는 RMF 메시지와 KONE API v2.0 사이에서 WebSocket으로 명령·상태를 교환하는 구조를 설명한다. [사실][^n9]
- F20. 그 README는 실제 승강기 제어용 access_id와 access_secret을 KONE 담당자에게 받도록 안내한다. [사실][^n9]
- 이 프로젝트는 싱가포르 The Galen의 실제 KONE 승강기로 시험했다고 보고한다. 독립 시험 성적서는 확인하지 못했다. [추정][^n9]
- 근거 메모: Q4. n9은2023년 고정 공개 구현이다. 현행 KONE 공식 계약을 확보한 것은 아니다. 동일 조직의 README·설정·코드는 한 출처로 센다. 오래된 OPC 경로(C16)는 별도 구현이며 이 구조와 섞지 않았다. 각 사실의 직접 구절·위치는 부록 D 참조.
- ROP 시사점: 어댑터 검토에는 현행 API 판·권한 범위·건물 등록·세션 유지 조건의 확인을 포함하는 편이 좋다. [의견]

### K09 [6. 대표 접근법 — 자동문 하드웨어·자격증명 조건 추가]

- F21. Dormakaba 어댑터 README는 열거된 EL301·ED250 문 구동기에 IoT connector를 장착해야 한다고 안내한다. [사실][^n10]
- F22. 같은 문서는 문 클라우드 API 접근 자격증명을 Dormakaba가 제공한다고 안내한다. [사실][^n10]
- 근거 메모: Q4·Q7. n10의 README 조건만 채택한다. EL301·ED250 시험 주장은 프로젝트 자체 보고이며 임의 자동문의 지원을 입증하지 않는다. 클라우드 자격증명 제공과 건물 출입권한 승인 정책은 다른 확인 항목이다. 각 사실의 직접 구절·위치는 부록 D 참조.
- ROP 시사점: 문 열기 API 자격증명 외에 로봇의 공간별 출입권한과 비상 우선권의 결정 주체를 확인해야 한다. [의견]

### K10 [5. 적용 사례 — PLC와 건물 비상 신호의 현장 연결 추가]

- F23. HopeTechnik 설계 문서는 승강기 PLC가 드라이 접점으로 내부 신호를 제어하는 연결 구조를 설명한다. [사실][^n11]
- F24. 그 현장 복구표는 화재 알람 시 PLC를 오류 상태로 두고 재시작을 위한 수동 개입을 요구한다. [사실][^n11]
- 근거 메모: Q3·Q7. n11은 한 도서관 현장의 설계·복구 설명이다. 다른 건물의 화재 제어·복구 조건으로 일반화하지 않는다. 문서 첫 부분의 상태1Hz와 Server절의2초 표기는 충돌하므로 전송주기 결론은 보류한다. 각 사실의 직접 구절·위치는 부록 D 참조.
- ROP 시사점: ROP 장애 복구와 건물 설비의 비상 복귀를 각각 시험하고, 수동 복귀 책임자를 정하는 편이 좋다. [의견]

### K11 [6·7. 대표 접근법·표준 — 물리 인계 절차와 중립 규격 범위 추가]

- F25. OMRON I680-E-02의 인계 예시는 위치·준비 상태 확인, 적재물 교환, 정지·최종 위치 확인, 출발 준비 확인을 구분한다. [사실][^n12]
- F26. 이 매뉴얼은 해당 절차가 예시이며 응용 요구에 따라 달라질 수 있다고 명시한다. [사실][^n12]
- F27. SEMI 공식 목록은 E84-0823을 현행판으로 표시하며 반도체 캐리어 인계를 범위로 설명한다. [사실][^n13]
- F28. 2025-12-17 작성된 SEMI Doc7442는 E84를 출발점으로 별도의 인계 규격과 TCP/IP 하위규격을 만들자는 개발제안이다. [사실][^n14]
- 근거 메모: Q5. n12는 제조사 기술문서의 예시 절차, n13은 반도체 인계규격의 공식 목록, n14는 신규 표준 개발제안이다. 서로의 구현 적합성을 검증한 독립 근거가 아니다. SNARF 승인과 표준 발행은 구분한다. OMRON의 Lift 절은 적재장치 리프트이므로 건물 승강기 사례로 쓰지 않는다. 각 사실의 직접 구절·위치는 부록 D 참조.
- ROP 시사점: ROP는 준비·허가·이송·완료의 의미를 현장 PLC와 합의하고, 물리 인계 완료를 상위 작업 완료에 연결하는 편이 좋다. [의견]

### K12 [8. 대표 연구 — 병원 실물 연구의 실패 유형·한계 수정]

- 대상 문장 식별: 부록 A의 병원2026 논문 원문 미열람 항목.
- F29. Lee 등의 실물 조사는 고려대구로병원의 단일 로봇으로 수행한 비응급 배송 122건을 분석했다. [사실][^n15]
- F30. 그 논문은 배송 실패 14건 중 승강기 호출 통신 오류 2건과 탑승·하차 막힘 8건을 구분했다. [사실][^n15]
- F31. 그 논문의 59.01% EOR 임계값은 현장별 보정이 필요한 값으로 명시되어 있다. [사실][^n15]
- F38. 논문 §3.1에 기재된 전체 성공률은87.03%다. [사실][^n15]
- 수치 대조: 122건과 실패14건이 같은 집계 대상이라면 산술 성공률은 약88.52%가 된다. 두 값의 관계를 원자료로 확인하기 전에는 전체 성공률을 성능 근거로 채택하지 않는 편이 좋다. [의견][^n15]
- X01. 사람과 승강기를 공유하는 실물 환경에서 로봇의 층간 이동이 지연된 사례가 있다. [사실][^n15][^n18]
- 근거 메모: Q6. n15의 분석은2025-06-18~29 비응급 배송, 직원용 공용 승강기, 단일 로봇이다. 현장 운영자와 제조사 DOGU가 공동 저자다. EOR은 승강기 가동률(Elevator Operating Rate)이며 해당 임계값을 국내 물류센터에 그대로 쓰지 않는다. 각 사실의 직접 구절·위치는 부록 D 참조.
- ROP 시사점: 가동률·통신 상태·카 내부 점유를 구분해 수집하고, 현장별 임계값을 새로 검증하는 편이 좋다. [의견]

### K13 [8. 대표 연구 — 호텔·그래프·버튼 조작 실험의 범위 수정]

- 대상 문장 식별: 부록 A의 호텔·그래프·다층 지도 논문 원문 미열람 항목.
- F32. Han 등의 호텔 연구는 실제 평면 정보를 이용해 배송 수요를 생성한 수치실험이며 기본 승강기 대기를 30초로 설정했다. [사실][^n16]
- F33. Kim 등의 그래프 연구는 15층 건물을 나타내는 그래프에서 소포 1·3·5·7개 시나리오를 평가했다. [사실][^n17]
- F34. 노주형 등의 실물 연구는 KAIST N1의 5~9층에서 각 층 절반 영역을 대상으로 로봇 팔의 승강기 버튼 조작을 사용했다. [사실][^n18]
- F35. 그 연구의 승강기 상호작용 시험에서는 20회 중 19회 성공이 보고됐다. [사실][^n18]
- 근거 메모: Q6. n16은 대련해사대·Bath의 수치실험, n17은 고려대세종·FieldRo의 그래프 실험, n18은 KAIST의 로봇 한 대 실물 지도 구축이다. 평면의 출처가 실제 호텔이라는 사실이 호텔 실물 운용 성능을 뜻하지 않는다. 지도 알고리즘 성능 심화는 이 영역에서 제외한다. 각 사실의 직접 구절·위치는 부록 D 참조.
- ROP 시사점: 설비 API 연동과 로봇의 버튼 조작을 서로 다른 연결 방식으로 기록하고, 공유 승강기 지연 시험을 따로 두는 편이 좋다. [의견]

### K14 [7·9. 표준·책임 경계 — BACnet 접근통제 백서의 지위 추가]

- F36. BAC-09-08은 2008-09-27자 백서이며 표준 변경을 제안하는 작업 문서라고 명시한다. [사실][^n19]
- F37. 그 백서는 인증과 권한 검사를 구분하고, 특정 문을 특정 시간에 통과할 권한을 검사 예로 든다. [사실][^n19]
- 근거 메모: Q7. n19는 현행 ANSI/ASHRAE135의 규범 본문이 아니다. 2022년 호스팅 경로도 발행일이 아니다. NIST C28은 본문 미열람이고 n19 기여자와도 겹쳐 독립 검증으로 쓰지 않는다. 각 사실의 직접 구절·위치는 부록 D 참조.
- ROP 시사점: 인증·권한 판단은 건물 정책과 연결하고, ROP의 문 열기 요청과 실제 통행 승인을 분리하는 편이 좋다. [의견]

### K15 [5. 적용 사례 — 기존 상업건물의 공급자 도입 사례 추가]

- NAVER LABS는2026-07-23 발표에서 Tokyo Midtown Yaesu의 기존 화물 승강기와 자동문을 ARC로 연결했다고 설명한다. [추정][^n20]
- 근거 메모: Q4·Q7. 공급자 블로그 본문 Connecting robots to building infrastructure 및 Integration across robot types and manufacturers를 구분해서 읽었다. 이기종 지원 설계와 연말 전층 확대 계획을 이미 운영 중인 실증으로 계산하지 않는다. 각 사실의 직접 구절·위치는 부록 D 참조.
- ROP 시사점: 기존 건물 도입에서는 연동 설비 목록과 실제 운영 중인 로봇 종류·층 범위를 고객 측 자료로 추가 확인하는 편이 좋다. [의견]

## 답한 열린 질문

질문 전문은 위키 보존본 `.research-work/F-22/wiki-s11.txt` 11~14행에 있다. 다음은 식별용 요약이며 질문을 새로 고친 것이 아니다.

|질문 식별|답변 수준|답 요약|
|---|---|---|
|oq-010 국내 다층 물류센터의 승강기 병목·병원/호텔 결과 전용|부분 답변|병원 실물 조사와 모델 연구의 조건을 확인했다(K12~K13). 국내 다층 물류센터의 화물승강기 정량자료 및 전용가능성은 확인 못 함. 일반화 보류 [의견][^n15][^n16][^n17][^n18]|
|새1 KOLA 가이드라인의 메시지·RMF 대응|부분 답변|제정기관 발표와 RMF 세션 의미를 확인했다(K04~K06). 표준 원문의 메시지·시험조건·매핑은 확인 못 함 [의견][^n5][^n6][^n8]|
|새2 제조사 중립 인계신호 규격|부분 답변|반도체 범위의 E84 목록과 개발제안, 제조사 예시 절차를 구분했다(K11). 범용 컨베이어의 공개·완결된 중립계약 확보로 보지 않는다 [의견][^n12][^n13][^n14]|
|새3 BACnet·보안문 설계/국내사례와 권한 주체|부분 답변|BACnet 백서의 개념과 자동문 연결 조건을 확인했다(K09·K14). 국내 로봇 보안문 운영의 권한판단 실체·비상우선권은 확인 못 함 [의견][^n10][^n19]|

완전히 답한 기존 열린 질문은0개다. 질문의 하위 근거를 보강했을 뿐 미확인 부분을 해결한 것으로 합산하지 않는다.

## 새로 생긴 열린 질문

|ID|추가 확인할 항목|
|---|---|
|U01|국내 다층 물류센터의 화물승강기·층간 반송설비 병목을 분리한 실측 처리량 자료|
|U02|KOLA 단체표준 번호·정확한 제정일·본문·RMF 메시지 대응표|
|U03|KS B7317 최신 본문과 판별 변경 조항; 목록 적용범위 이상의 해석|
|U04|REEC 현행 상세 심사기준 판·법정 의무의 근거·개별 건물의 최신 심사 범위|
|U05|KONE 현행 공식 API 계약, 지원 승강기·건물 등록·권한과 과거 공개 어댑터의 차이|
|U06|현대엘리베이터 현행 로봇 연동 API 원문·인증·장애 계약|
|U07|TTA 10.1486 Part1/R1·Part2/R1 본문과 설비 연동 범위|
|U08|SEMI E84 본문 및 Doc7442 결과 규격의 발행 여부·현재 판|
|U09|범용 컨베이어에서 준비·허가·이송·완료·오류를 포괄하는 제조사 중립 공개 규격|
|U10|국내 보안문·BACnet 로봇 연동의 실제 권한 결정 주체와 비상 우선권|
|U11|HopeTechnik 문서의 상태 전송주기1Hz/2초 충돌을 설명하는 구현·설정|
|U12|NAVER Yaesu 사례의 독립 운영평가와 실제 이기종·전층 운영 범위|
|U13|병원 논문의 분석122건·실패14건과 전체성공률87.03% 사이의 집계 불일치 원인|

확인 못 함은 U01~U13의13개 고유 항목이다. 동일 공백의 재언급은 중복 집계하지 않는다. 검색에서 찾지 못했다는 뜻이며 자료 자체가 없다는 증명은 아니다.

## 출처

집계: 총20개, 원문 열람18/20, 1차 자료20개(이 중 공식 목록만2개), 독립 교차 확인된 주장1개(X01, 질적 관찰). 원문 미열람2개는 KS·SEMI 본문이며 목록의 범위·판만 사용한다. KOLA 자료는 보도자료 전문 열람이고 표준 본문 열람이 아니다. 기존 위키 자료7개(n3·n4·n6·n15~n18), 새 출처13개다. 같은 문헌의 미러·새 판·커밋을 새 출처로 중복 집계하지 않았다. 출판사 PDF 복구 경로도 원 논문1개로 센다.

[^n1]: 스마트도시협회, *로봇 친화형 건축물 인증(REEC) 소개·연혁*, 웹 현행 설명, 발행일 미확인, [원문·목록](https://www.smartcity.or.kr/reecintro), 접근2026-10-11, 원문 열람.
[^n2]: Youngsup Park; Sungho Park, *Development of Human-Centered, Robot-Adaptive Building Design Standards: Focusing on Korea’s Building Certification Systems*, Architectural Research 28,14; DOI 10.1007/s44515-026-00016-y, 2026-07-21, [원문·목록](https://link.springer.com/article/10.1007/s44515-026-00016-y), 접근2026-10-11, 원문 열람.
[^n3]: 국토교통부, *“AI 품은 건축물, 이제는 스마트+빌딩 시대”…스마트+빌딩 핵심기술 개발 본격화*, 보도자료 3쪽; CODIL 보존본은 같은 문헌, 보도2025-05-28, 배포2025-05-27, [원문·목록](https://www.codil.or.kr/filebank/files/202505/helpdesk/BBS_202505290921245530.pdf?atchFileId=FILE_000000000010811&fileSn=0), 접근2026-10-11, 원문 열람.
[^n4]: 국가기술표준원, *KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가방법*, 2025-05-09 개정, 고시2025-0073, 2025-05-09, [원문·목록](https://www.standard.go.kr/KSCI/standardIntro/getStandardSearchView.do?ksNo=KSB7317&menuId=919&reformNo=&tmprKsNo=KSB7317&topMenuId=502&upperMenuId=503), 접근2026-10-11, 원문 미열람(공식 목록만).
[^n5]: 대한승강기협회(KOLA), *대한승강기협회, 엘리베이터-로봇 연동 단체표준 제정(26.3.27)*, 보도자료; 표준 본문·번호 미확인, 2026-03-27, [원문·목록](https://kola.or.kr/pages/61/68/bbs/5705), 접근2026-10-11, 원문 열람.
[^n6]: Open-RMF, *rmf_internal_msgs: lift·door·dispenser·ingestor 메시지*, commit 2a7f01baadcc60866b4ee0e686bcaf4cd6f2574b, 커밋2026-09-22, [원문·목록](https://github.com/open-rmf/rmf_internal_msgs/tree/2a7f01baadcc60866b4ee0e686bcaf4cd6f2574b), 접근2026-10-11, 원문 열람.
[^n7]: Open-RMF, *rmf_ros2: fleet_adapter CHANGELOG, lift/door supervisor, DispenseItem/IngestItem*, commit 4cea3fe97d4fcafdebd5590247c42b28664e2b55, 커밋2026-10-08; CHANGELOG 2.13.0은2026-06-15, [원문·목록](https://github.com/open-rmf/rmf_ros2/tree/4cea3fe97d4fcafdebd5590247c42b28664e2b55), 접근2026-10-11, 원문 열람.
[^n8]: cwrx777; mxgrey, *Lift session issues – Robot enter lift while lift is still in human mode (#513)*, GitHub 토론의 Discourse 아카이브, 2024-08-21, [원문·목록](https://discourse.openrobotics.org/t/lift-session-issues-robot-enter-lift-while-lift-is-still-in-human-mode-513/44679), 접근2026-10-11, 원문 열람.
[^n9]: CHART; KABAM-Robotics 보존 저장소, *KONE RMF Lift Adapter / kone-ros-api*, commit 9bc3a87a01eea66c606e0a256e1cd8a8c60bc596, KONE API v2.0, 커밋2023-07-13, [원문·목록](https://github.com/KABAM-Robotics/lift_kone_adapter/tree/9bc3a87a01eea66c606e0a256e1cd8a8c60bc596), 접근2026-10-11, 원문 열람.
[^n10]: Open-RMF, *door_adapter_dormakaba README*, commit 2cf76a6b83ceee31540aeb7e0d7feb2a10042668, 커밋2025-06-16, [원문·목록](https://github.com/open-rmf/door_adapter_dormakaba/tree/2cf76a6b83ceee31540aeb7e0d7feb2a10042668), 접근2026-10-11, 원문 열람.
[^n11]: HopeTechnik, *Lift and Doors Integration, RMF Systems Engineering Handbook*, TRL 현장 설계·복구 설명, 발행일 미확인, [원문·목록](https://trl-rmf.github.io/website/content/lift-door-integration.html), 접근2026-10-11, 원문 열람.
[^n12]: OMRON, *LD-Series Integration Guide*, I680-E-02, 2023-05(Revision History p16), [원문·목록](https://www.omron.com.tw/data_pdf/mnu/i680-e-02_ld.pdf?id=3664), 접근2026-10-11, 원문 열람.
[^n13]: SEMI, *SEMI E84 Specification for Enhanced Carrier Handoff Parallel I/O Interface*, E84-0823, Current 목록, 2023-08 판 식별; 개별 발행일 미확인, [원문·목록](https://store-us.semi.org/products/e08400-semi-e84-specification-for-enhanced-carrier-handoff-parallel-i-o-interface), 접근2026-10-11, 원문 미열람(공식 목록·초록만).
[^n14]: SEMI Physical Interfaces & Carriers TC, Japan, *SNARF for Doc 7442: Specification for Enhanced Handoff Interface*, New Preliminary Standard 개발제안서, 작성2025-12-17, SNARF 승인2025-12-18, [원문·목록](https://downloads.semi.org/web/wstdsbal.nsf/18a679096dfd445188256d35007d447d/0db3fe2c9bb0eb2488258d9400027699!OpenDocument), 접근2026-10-11, 원문 열람.
[^n15]: Yourack Lee 외17명, *Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments*, Digital Health 12:20552076261437181; DOI10.1177/20552076261437181, 2026-03-31, [원문·목록](https://pmc.ncbi.nlm.nih.gov/articles/PMC13039597/), 접근2026-10-11, 원문 열람.
[^n16]: Linghui Han; Junzhe Ding; Songtao Liu; Meng Meng, *The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments*, Sensors 25(6):1783; DOI10.3390/s25061783, 2025-03-13, [원문·목록](https://pmc.ncbi.nlm.nih.gov/articles/PMC11946681/), 접근2026-10-11, 원문 열람.
[^n17]: Seungmin Kim; Hyunseo Jang; Jiseung Ha; Daekug Lee; Yeongho Ha; Young Eun Song, *Efficient Graph-Based Multi-Story Path Planning with Optimized Elevator Selection for Indoor Delivery Robots*, Electronics 14(5):982; DOI10.3390/electronics14050982, 2025-02-28, [원문·목록](https://mdpi-res.com/d_attachment/electronics/electronics-14-00982/article_deploy/electronics-14-00982.pdf), 접근2026-10-11, 원문 열람.
[^n18]: 노주형; 강규리; 김연찬; 심현철, *탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템*, 로봇학회 논문지21(1):48–57; DOI10.7746/jkros.2026.21.1.048, 2026-03(호 표기); 일자 미확인, [원문·목록](https://jkros.org/xml/48719/48719.pdf), 접근2026-10-11, 원문 열람.
[^n19]: SSPC135 LSS-WG; Bernhard Isler 외 기여자, *Physical Access Control with BACnet*, BAC-09-08 White Paper, 124쪽, 2008-09-27, [원문·목록](https://bacnet.org/wp-content/uploads/sites/4/2022/08/BAC-09-08.pdf), 접근2026-10-11, 원문 열람.
[^n20]: NAVER LABS, *NAVER’s ARC Goes to Japan*, 공급자 기술 블로그, 2026-07-23, [원문·목록](https://naverlabs.com/en/blogDetail?seq=10034507), 접근2026-10-11, 원문 열람.




## 부록 A. 1단계 진단표와 조사 질문

## F-22 1단계 진단 — 2026-10-11

검색 전에 현재 본문과 연결된 분리4·7·8·10·11절을 끝까지 읽었다. 본문 버전2, 분리 페이지 버전1, 표시 갱신일2026-09-25. 실제 본문에는 2026-09-28 리스트업 표기가 별도로 있으므로 표시 갱신일만으로 이후 변경이 없다고 단정하지 않는다. 원문은 wiki.html/txt 및 wiki-s{4,7,8,10,11}.html/txt에 보존했다. 아래는 조사 시작 당시의 진단이며 결론은 아니다.

### 약한 주장·근거 공백

전체 대상 문장과 각주는 보존본에서 확인할 수 있다. 긴 문장을 반복 전재하지 않고 원문 그대로의 짧은 구절과 절·대상을 남긴다.

|위치·대상|짧은 원문 구절 또는 식별 대상|약한 이유·확인 방향|
|---|---|---|
|본문3 VDA 경계|“범위에서 제외한다”|단일 규격. 기존 F-21과 중복; 설비 연결 수단까지 확대하지 않음|
|본문3 승강기 영향|“영향을 줄 것으로 보인다”|추정, 화물용 승강기 정량 근거 미확인; Q6|
|본문3 KS B7317|“2021년 11월”|목록·보도자료만, 원문 미열람; Q1|
|본문3 국내 연구개발|“발행일 미확인”|국토부 제목만 확인한 추정, 인증 시행과 다른지; Q1|
|본문5 시작 조건|VDA 해제 구역 허가|가상 작업대의 준비/진입 허가 결합, 실제 연동 검증 없음; Q5|
|본문5 수행 자원·제약|RMF 어댑터, 승강기 세션, AGV모드|단일 프로젝트 문서, 모든 제조사 실물 동작으로 확대 주의; Q3|
|본문5 완료·인계|“맞출 수 있을 것으로 보인다”|인제스터 결과와 구역 허가를 조합한 추론; Q5|
|본문5 예외|“예외로 다뤄야 할 것으로 보인다”|화재·비상·오프라인 모드 기반 설계 추론; Q3·Q7|
|본문6 어댑터 구조|OPC 같은 프로토콜|단일 RMF 문서, OPC라는 예시를 의무 표준으로 읽지 않음; Q3·Q4|
|본문6 작업대|“현장마다 따로 필요하다”|현장 적응의 추정; 공개 중립 handshake 비교 필요; Q5|
|본문7 국제표준|설비–로봇 연동 국제표준 미확인|검색 실패를 부재 증명으로 읽지 않음; Q2·Q5|
|본문8 대표연구|모두 본문 미열람|논문 본문·서지·조건 필요; Q6|
|본문9 책임 경계|어댑터 요청·점유·상태·완료와 설비 안전 제어|대부분 추정; 실제 제공 인터페이스와 일치 여부 Q3·Q4·Q7|
|분리4 문 어댑터|“상태 감독자 역할”|RMF 단일 문서, 직접 요청 처리·세션 규칙 확인; Q3|
|분리4 승강기 어댑터|“직접 보낸 요청은 무효”|강한 일반화인지 실제 문서·코드로 확인; Q3|
|분리4 메시지|“사람 모드”·“화재·오프라인·비상”|움직이는 main 링크. read/write·모드·세션 상태의 실제 구조 Q3|
|분리4 작업대|“표준 규격이 아니라 예시 구현”|DispenserRequest·IngestorResult 원문 미열람 상태; Q5|
|분리7 KS|“원문 미열람”|안전 표준 범위와 탑승 평가, 최신판·개정 여부 확인; Q1|
|분리7 협회 표준|“표준 번호·제정일·내용은 미확인”|2차 보도뿐; 원문등록/번호/제정일 Q2|
|분리7 제조사 API|“메시지 구조·인증 방식은 미확인”|KONE공식미열람, 현대2022·2023기사의 회사 주장; Q4|
|분리8 그래프 경로|“승강기 선택 기준은 미확인”|저자·본문 미확인; Q6|
|분리8 병원2026·호텔2025|논문 초록/제목 수준의 사실 태그|실제 환경·로봇 대수·병목·승강기 정책 Q6|
|분리8 다층 지도2026|“연동 방식 세부는 미확인”|지도 기술 일반론으로 벗어나지 않고 연결방식만 Q4·Q6|
|분리8 협의체|프로토콜(안)·시나리오(안)|제안 단계와 제정표준 혼동 주의; Q2|
|분리8 국토부|“보도자료 제목만 확인했다”|연구착수·인증예고·법정/민간인증 구분 Q1|
|분리10 공용자원·안전 연결|“대기가 층간 운반 처리량에 줄 영향”|추정, 별도 최적화·안전영역 깊은 조사로 확장하지 않음; Q6|

### 1~13절 빈 곳

|절|진단|
|---|---|
|1|정의·범위·옛 분류 설명 충분. 날짜 표식과2026-09-28리스트업은 별도|
|2|설비 준비와 로봇 도착의 동기화 질문만 있음|
|3|VDA외부인터페이스 경계 있음. 국내 제도 날짜·실행 상태 약함|
|4|RMF용어 중심. 명령 접수/설비 준비/인계 완료, 세션 실패 구분 부족|
|5|물류창고 가상 시나리오 중심. 병원·호텔·오피스 실물 규모·방식 공백|
|6|어댑터·작업대·구역 진입 설명. 제조사 API 계약·장애/선점 상세 없음|
|7|협회표준번호 미확인, KS구판, 제조사API미열람. BACnet/출입통제의 실제연결 없음|
|8|논문 전부 미열람. 저자·판·게재일·실물/시뮬레이션·규모 공백|
|9|설비 안전제어와ROP역할 추정. 인증·권한 판단 주체와 상태확인 경계 부족|
|10|다른영역 연결 충분. 연결 제안만 하고 연구범위 확장하지 않음|
|11|oq010+새질문3. 각각 원문 근거 부족|
|12|표시 갱신2026-09-25. 최근1년 제도·표준·RMF변경 조사가 필요|
|13|main링크, 날짜미상, 원문미열람 다수. 고정커밋·공식자료 보강 필요|

### 열린 질문

원문 전체는 wiki-s11.txt 11~14행에 보존했다. 새 질문의 고유 id는 없다.

|id·원문 위치|요지|이번 조사|
|---|---|---|
|oq-010·11행|국내 다층 물류센터 화물용 승강기·반송설비 병목의 정량자료; 병원/호텔 결과의 전용 가능성|Q6|
|새1·12행|대한승강기협회 가이드라인의 호출·탑승·하차·세션해제 메시지와 RMF 대응|Q2·Q3|
|새2·13행|컨베이어·작업대–로봇 인계의 준비·허가·이송·완료를 정하는 제조사 중립 표준|Q5|
|새3·14행|출입통제·BACnet으로 보안문을 여닫는 공개 설계/국내사례와 권한 판단 주체|Q7|

### 오래된 정보 후보

- KS B7317 2021-11: 현재 유효판·최근 확인/개정과 범위를 확인한다.
- 현대엘리베이터 API 공개2022-03, 참여60여곳2023-02: 발표 당시 정보이며 현재 사용성·지원범위와 구분한다.
- RMF 문서·메시지와 협회표준·국토부 발표는 발행일 미확인. 오래됐다고 단정하지 않는다.
- 2025·2026논문은 최신으로 보이지만 원문 미열람이 더 큰 문제다.

### 조사 질문과 답변 기준

|id·우선순위|질문|어떤 근거가 나오면 답한 것으로 보는가|
|---|---|---|
|Q1·1|국내 로봇친화형 건축물 인증은 실제로 시행되는가? KS B7317과 어떤 범위 차이가 있는가?|공식기관의 근거·개시일·신청/심사·기준·운영기관, KS공식판을 확인하고 법정/민간/실증·연구단계를 구분|
|Q2·2|국내 승강기–로봇 연동 표준의 번호·판·메시지/상태와 적용범위는?|협회·표준등록기관·TTA/KS 원문 또는 공식목록, 실제조항을 확보; RMF 대응은 직접근거/설계의견 구분|
|Q3·3|RMF lift/door의 세션·요청/결과·실패 처리는 무엇이며 최근1년 무엇이 바뀌었는가?|메시지와adapter구현을 고정태그/커밋으로 읽고 release/history·timeout/release동작·현장연계조건 확인|
|Q4·4|KONE·현대 등 제조사 API는 어떻게 로봇 요청을 인증하고 호출/탑승/하차 상태를 전달하는가?|공개 API 계약·이벤트·인증·제약 및 도입환경을 확인. 클라우드/현장개조·등록조건과 단일벤더주장 구분|
|Q5·5|로봇–컨베이어/작업대 인계 handshake의 공개 중립 규격·구현이 있는가?|준비·허가·이송·완료·오류의 신호/상태·상관키·동시성·물리완료 의미가 명시된 규격이나구현 확보|
|Q6·6|기존 병원·호텔·경로계획 논문은 승강기 대기를 어떻게 측정/모델링했으며 물류센터에도 적용 가능한가?|본문·서지·실물/시뮬레이션·규모·승강기 정책·혼잡측정조건을 확인, 직접국내물류근거 여부 별도|
|Q7·7|보안문·BMS 연동에서 접근권한과 비상 우선권은 어느 시스템이 판단하며 기존건물 개조의 한계는?|BACnet/출입통제 공식규격·공개어댑터·실증자료로 권한판단·상태확인·예외범위를 확인; 안전설계 일반론은 별도영역으로 남김|

다음 단계는 Q1~Q7 각각 최소3관점의 별도 검색과 질문당5개 이상 후보 선정이다. 아직 검색·결론 작성을 시작하지 않았다.

## 부록 B. 검색 기록

## F-22 검색 기록 — 2026-10-11

한 행마다 web 검색을 개별 실행했다. 날짜는 검색일이다. 건진 수는 해당 결과에서 후보 목록에 남긴 문헌 수이며 검색엔진 전체 결과 수가 아니다. 같은 문헌의 미러·재게시를 한 번만 센다. 여러 검색에서 같은 문헌을 다시 찾은 것은 각 행에 표시하되 후보 총수에서 중복 제거했다. 검색 원본은 search-results.json 및 search-results-2~5.json에 보존했다.

|검색 id·관점|검색어|날짜|건진 출처 수·후보|
|---|---|---|---|
|Q1a ① 제도|site:molit.go.kr 로봇 친화형 건축물 인증 2025 2026 기준 시행|2026-10-11|1 (C01)|
|Q1b ⑤ 국내기관|로봇친화형 건축물 인증 한국로봇산업진흥원 한국건설생활환경시험연구원 2026|2026-10-11|0|
|Q1c ⑥ 시행 한계|robot friendly building certification Korea 2025 2026 pilot standards KS B 7317|2026-10-11|3 (C01, C02, C03)|
|Q2a ① 표준|엘리베이터 로봇 상호 연동 가이드라인 SPS 대한승강기협회 표준 2025|2026-10-11|2 (C04, C06)|
|Q2b ② 구현|site:github.com robot elevator integration Korea standard TTA lift protocol|2026-10-11|1 (C12)|
|Q2c ⑤ 국내|site:tta.or.kr 승강기 로봇 연동 표준 2025 2026|2026-10-11|2 (C07, C08)|
|Q3a ② 공개 구현|site:github.com/open-rmf rmf lift door adapter session timeout 2025 2026|2026-10-11|3 (C09, C10, C11)|
|Q3b ④ 산업|Open RMF elevator door integration KONE adapter building deployment|2026-10-11|2 (C12, C13)|
|Q3c ⑥ 실패 한계|site:discourse.openrobotics.org RMF lift session door stuck timeout emergency|2026-10-11|1 (C14)|
|Q4a ④ 제조사|site:dev.kone.com service robot API call state authentication websocket|2026-10-11|1 (C15)|
|Q4b ② 구현|site:github.com KONE robot lift adapter authentication session|2026-10-11|2 (C12, C16)|
|Q4c ⑤ 국내|site:hyundaielevator.com 로봇 오픈 API 연동 2025 2026|2026-10-11|0|
|Q5a ① 표준|mobile robot conveyor load transfer handshake VDMA 5050 OPC UA standard|2026-10-11|1 (C18)|
|Q5b ② 공개 구현|site:github.com/open-rmf rmf_ingestor_msgs IngestorResult request_guid ACKNOWLEDGED SUCCESS|2026-10-11|1 (C09)|
|Q5c ③ 연구|mobile robot conveyor workcell handover synchronization protocol paper|2026-10-11|1 (C21)|
|Q6a ③ 학술|"Feasibility of autonomous medication delivery robots" "elevator"|2026-10-11|1 (C22)|
|Q6b ④ 산업|elevator robot traffic warehouse multi floor throughput hospital hotel delivery study|2026-10-11|2 (C22, C23)|
|Q6c ⑤ 국내|다층 물류센터 로봇 화물 승강기 병목 대기시간 정량 연구|2026-10-11|0|
|Q7a ① 표준|site:bacnet.org access control access door credential robot elevator|2026-10-11|1 (C27)|
|Q7b ② 공개 구현|site:github.com open rmf dormakaba door adapter access control|2026-10-11|2 (C11, C29)|
|Q7c ④ 산업|robot building access control BACnet elevator emergency integration hospital|2026-10-11|1 (C28)|
|Q1d ⑤ 인증기관 보완|"로봇친화" "인증" "2026" 건축물|2026-10-11|0|
|Q5d ① 인계표준 보완|SEMI E84 automated material handoff AMR AGV handshake transfer standard|2026-10-11|2 (C19, C31)|
|Q5e ④ 제품계약 보완|OMRON LD conveyor top handshake transfer PLC ready complete manual|2026-10-11|1 (C20)|
|Q6d ④ 공급자 보완|site:mobile-industrial-robots.com elevator hospital logistics multi floor robots|2026-10-11|1 (C26)|
|Q4d ⑤ 국내API 보완|현대엘리베이터 MIRI 개발자 API 로봇 연동 문서|2026-10-11|1 (C17)|
|Q2d ① 협회번호 보완|"엘리베이터와 로봇의 상호 연동" "SPS"|2026-10-11|0|
|Q6e ⑤ 국내 연구 보완|site:jkros.org 엘리베이터 다층 배송 로봇 2025 2026|2026-10-11|1 (C25)|
|Q1e ① 제도기관 보완|"로봇" "친화형" "인증" site:kaia.re.kr|2026-10-11|0|
|Q7d ⑤ 국내 현장 보완|site:naverlabs.com 1784 robot building access elevator doors|2026-10-11|1 (C30)|
|Q5f ① 규격 보완|site:reference.opcfoundation.org conveyor mobile robot transfer handshake|2026-10-11|0|

총 31개 개별 검색. C05·C24는 기존 위키 각주에서 직접 추적했다. C29는 검색 결과에 나타난 Open-RMF awesome_adapters 목록의 직접 링크를 후보로 잡았으며 저장소 본문 열람은 3단계에서 한다. Q4c의 분기보고서·연혁은 후보로 채택하지 않고 Q4d의 실제 MIRI 서비스 설명을 남겼다. Q5f는 물리적 화물 인계와 값/결과 데이터 전송을 혼동할 우려가 있어 후보0개로 처리했다. 자료를 못 찾은 관점은 다른 관점의 자료로 해결했다고 기재하지 않았다.


### 원문 추적 중 보완 검색

날짜 2026-10-11. 후보수는 중복 제거 후 새 후보의 수다. 미러와 직접원문 복구는 신규문헌0.
|관점|검색어|날짜|건진 새 후보 수|
|---|---|---|---:|
|국내 인증운영기관|site.smartcity.or.kr 로봇 친화 건축물 인증 REEC|2026-10-11|1(C32; 소개·연혁을 한 묶음)|
|국내 R&D 원문|site.molit.go.kr 2025 5 28 로봇 친화 건축물 스마트 빌딩|2026-10-11|0(C01 CODIL 보존본 추적)|
|표준번호 확인|"엘리베이터와 로봇의 상호 연동을 위한 가이드라인" SPS|2026-10-11|0|
|국내 표준 목록|"TTAK.KO-10.1486-Part1/R1" 표준|2026-10-11|0(C07·C08 동일 목록)|
|제조사 기술문서|"i680-e-02" pdf LD|2026-10-11|0(C20 동일문헌미러)|
|논문 원문복구|"Efficient Graph-Based Multi-Story" pdf|2026-10-11|0(C24 출판사PDF 직접추적)|


## 부록 C. 출처 평가표

## F-22 3단계 출처 평가

접근일 2026-10-11. 후보31개에 C32(REEC 운영기관 소개·연혁 묶음)를 추가 추적했다. 아래 20개를 채택한다. 원문은 관련 본문을 직접 읽었다는 뜻이며 현장 실행·재현을 뜻하지 않는다. KS와 E84는 공식 목록까지만 열어 원문 열람 분자에서 제외한다. KOLA는 표준을 읽은 것이 아니라 제정기관 보도자료 전문을 읽은 별도 문헌이다. OMRON은 웹 도구 PDF 본문 열람에 성공했지만 curl 403 및 스크린샷 캐시 오류로 로컬 PDF·쪽 이미지를 확보하지 못했다. 그 자료에서는 텍스트 절차만 사용한다.

|후보→최종|기관·서지·판·날짜|열람·1/2차|독립성|신뢰도|
|---|---|---|---|---|
|C32→n1|스마트도시협회, 로봇 친화형 건축물 인증(REEC) 소개·연혁, 웹 현행 설명, 발행일 미확인|원문 열람; 1차 기관 설명|SCA; C03이 이 페이지를 인용하므로 운영 여부의 독립 검증 아님|high(기관·평가범위), 실제 심사성능 미검증|
|C03→n2|Youngsup Park; Sungho Park, Development of Human-Centered, Robot-Adaptive Building Design Standards: Focusing on Korea’s Building Certification Systems, Architectural Research 28,14; DOI 10.1007/s44515-026-00016-y, 2026-07-21|원문 열람; 1차 설계 비교 연구|Heerim; 국토부 Smart Building R&D 지원, C32 인용|medium: 문헌비교이며 현장실험 아님|
|C01→n3|국토교통부, “AI 품은 건축물, 이제는 스마트+빌딩 시대”…스마트+빌딩 핵심기술 개발 본격화, 보도자료 3쪽; CODIL 보존본은 같은 문헌, 보도2025-05-28, 배포2025-05-27|원문 열람; 1차 공식 발표|국토부 R&D; C03과 관련 과제계열|high: 연구계획의 확인, 완료·인증시행 증거 아님|
|C02→n4|국가기술표준원, KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가방법, 2025-05-09 개정, 고시2025-0073, 2025-05-09|원문 미열람(공식 목록만); 1차 공식 목록|KATS/한국AI·로봇산업협회|high(개정·범위 목록), 조항 미확인|
|C06→n5|대한승강기협회(KOLA), 대한승강기협회, 엘리베이터-로봇 연동 단체표준 제정(26.3.27), 보도자료; 표준 본문·번호 미확인, 2026-03-27|원문 열람; 1차 제정기관 발표|KOLA 협의체; 참여기관의 재보도는 독립 아님|high(발표 사실), 표준조항의 증거로 사용 안 함|
|C09→n6|Open-RMF, rmf_internal_msgs: lift·door·dispenser·ingestor 메시지, commit 2a7f01baadcc60866b4ee0e686bcaf4cd6f2574b, 커밋2026-09-22|원문 열람; 1차 고정 코드|Open-RMF; C10·C11·C14·C29와 연계|high(정적 메시지 정의); 장치 재현 안 함|
|C10→n7|Open-RMF, rmf_ros2: fleet_adapter CHANGELOG, lift/door supervisor, DispenseItem/IngestItem, commit 4cea3fe97d4fcafdebd5590247c42b28664e2b55, 커밋2026-10-08; CHANGELOG 2.13.0은2026-06-15|원문 열람; 1차 고정 코드|Open-RMF; C09과 동일프로젝트|high(해당분기), 현장 안전·최신 배포 모든동작 확인 아님|
|C14→n8|cwrx777; mxgrey, Lift session issues – Robot enter lift while lift is still in human mode (#513), GitHub 토론의 Discourse 아카이브, 2024-08-21|원문 열람; 1차 개발자 토론|Open-RMF 메시지 설계자 설명; C09·C10과 독립 아님|medium: 보고·권고; 현재 결함 재현 아님|
|C12→n9|CHART; KABAM-Robotics 보존 저장소, KONE RMF Lift Adapter / kone-ros-api, commit 9bc3a87a01eea66c606e0a256e1cd8a8c60bc596, KONE API v2.0, 커밋2023-07-13|원문 열람; 1차 공개 구현·README|CHART/RMF 통합계열; KONE 제조사 최신 계약과 구분|high(코드·설정 존재), 실증자체보고 medium|
|C29→n10|Open-RMF, door_adapter_dormakaba README, commit 2cf76a6b83ceee31540aeb7e0d7feb2a10042668, 커밋2025-06-16|원문 열람; 1차 공개 구현|Open-RMF·Dormakaba 연동계열|high(문서 요구조건), 제품성능은 자체보고|
|C13→n11|HopeTechnik, Lift and Doors Integration, RMF Systems Engineering Handbook, TRL 현장 설계·복구 설명, 발행일 미확인|원문 열람; 1차 수행기관 설계|TRL/RMF 통합 프로젝트; C09·C10과 독립 안전시험 아님|medium: 구체현장 설계, 텔레메트리 주기 서술충돌|
|C20→n12|OMRON, LD-Series Integration Guide, I680-E-02, 2023-05(Revision History p16)|원문 열람; 1차 제품 기술문서|OMRON 단일업체|high(절2-9-3의 예시절차), 범용표준 아님|
|C19→n13|SEMI, SEMI E84 Specification for Enhanced Carrier Handoff Parallel I/O Interface, E84-0823, Current 목록, 2023-08 판 식별; 개별 발행일 미확인|원문 미열람(공식 목록·초록만); 1차 공식 목록|SEMI; C31과 동일 표준화계열|high(목록상 판·범위), 본문 신호시간 미확인|
|C31→n14|SEMI Physical Interfaces & Carriers TC, Japan, SNARF for Doc 7442: Specification for Enhanced Handoff Interface, New Preliminary Standard 개발제안서, 작성2025-12-17, SNARF 승인2025-12-18|원문 열람; 1차 개발제안|SEMI; C19와 독립 아님|high(제안상태); 정식표준 발행 확인 아님|
|C22→n15|Yourack Lee 외17명, Feasibility of autonomous medication delivery robots considering elevator utilization in high-traffic hospital environments, Digital Health 12:20552076261437181; DOI10.1177/20552076261437181, 2026-03-31|원문 열람; 1차 실물 관찰·시뮬레이션 논문|고려대구로병원·DOGU 공동; 공급자 완전독립 아님. KAIST C25와 다른팀·시설|medium: 단일병원·단일로봇, 현장임계값|
|C23→n16|Linghui Han; Junzhe Ding; Songtao Liu; Meng Meng, The Path Planning Problem of Robotic Delivery in Multi-Floor Hotel Environments, Sensors 25(6):1783; DOI10.3390/s25061783, 2025-03-13|원문 열람; 1차 수치실험 논문|Dalian Maritime University 등; C22·C25와 다른팀|medium: 수치실험·고정 승강기시간, 실제 호텔운영 검증 아님|
|C24→n17|Seungmin Kim; Hyunseo Jang; Jiseung Ha; Daekug Lee; Yeongho Ha; Young Eun Song, Efficient Graph-Based Multi-Story Path Planning with Optimized Elevator Selection for Indoor Delivery Robots, Electronics 14(5):982; DOI10.3390/electronics14050982, 2025-02-28|원문 열람; 1차 그래프 모의실험 논문|고려대세종·FieldRo; C22와 기관 일부연결이나 다른실험|medium: 15층 가중그래프; 실건물 성능아님|
|C25→n18|노주형; 강규리; 김연찬; 심현철, 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템, 로봇학회 논문지21(1):48–57; DOI10.7746/jkros.2026.21.1.048, 2026-03(호 표기); 일자 미확인|원문 열람; 1차 실물 연구|KAIST; C22병원·DOGU와 다른 연구팀·실험|medium: N1 5~9층 각층 절반; 버튼조작·한대|
|C27→n19|SSPC135 LSS-WG; Bernhard Isler 외 기여자, Physical Access Control with BACnet, BAC-09-08 White Paper, 124쪽, 2008-09-27|원문 열람; 1차 작업반 설계 백서(규범 아님)|Siemens·HIRSCH·Delta·NIST 참여; C28 Treado 공통|medium(당시개념), 현행BACnet·국내권한 규범 근거아님|
|C30→n20|NAVER LABS, NAVER’s ARC Goes to Japan, 공급자 기술 블로그, 2026-07-23|원문 열람; 1차 공급자 발표|NAVER·Yaesu 사업; 동반블로그는 독립 아님|medium: 도입 주장, 독립운영 평가 미확보|

### 비채택 후보 및 실패

|후보|확인한 서지·원문 상태|평가·제외 이유|
|---|---|---|
|C04|국토부 스마트+빌딩 활성화 로드맵 PDF 경로 열람 실패; 발행일 미확인|검색 경로 실패. C01에서 로드맵 마련2023-12만 확인; 별도 본문 근거로 사용 안 함|
|C05|산업통상자원부, 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다, 게시2021-11-11; 페이지는 제목·첨부만|1차 게시 목록, KATS계열. 당시 제정일을 게시일과 혼동하지 않음. 최신 공식 C02로 대체|
|C07|TTAK.KO-10.1486-Part1/R1, 도심 자율주행 배달로봇 서비스 – 제1부: 연동 요구사항; 상세/목록 HTTP400·웹 실패|공식 검색 색인에는2025-06-27이 있으나 본문 미열람. 내용·엘리베이터 메시지 매핑의 근거로 사용 안 함|
|C08|TTAK.KO-10.1486-Part2/R1, 제2부: 연동 참조구조; 상세 HTTP400·웹 실패|C07과 동일기관·검색색인 단계, 원문 내용 미확인|
|C11|Open-RMF door_adapter_template README, b727f647b6d5c0401d29ddb5ef9ca2c5de574562(2025-06-16), 원문 열람|1차 예제·high(정적 템플릿). REST 블록 작성 요구, 기존 위키에 이미 있음. 실제하드웨어 요구는C29로 추가|
|C15|KONE Service Robot API 공식 포털, 발행일 미확인; 웹본문0행|원문 미열람(앱 셸). 현행 제조사 API 계약 미확인. C12의구현을 공식최신명세로 둔갑시키지 않음|
|C16|CHART KONE OPC controller README,158b5925544e1d9f7270c1fceb552aad1d65e1f8(2020-01-16), 원문 열람|1차·medium. Windows OpenOPC와 ROS2 Dashing 경로. C12 WebSocket과 다름. 오래된 구현·현행적용미확인, 별도 보완 항목 제외|
|C17|현대엘리베이터 MIRI 부가서비스, 날짜 미확인; curl HTML은 제목만, 웹0행|원문 미열람(앱 셸). 인증·제어 API 상세 근거 미확보|
|C18|VDA5050 3.0.0, March2026, 공식목록과 기존보존 PDF 범위절 재열람|1차·high(범위), VDA계열. 주변설비·인프라 인터페이스 제외는 위키와F21에 이미 있음; 새보완 제외|
|C21|Vivek D. Sangani; Shimon Y. Nof, Improving human–robot collaboration in AMR-assisted warehouse picking, Int.J.Adv.Manuf.Technol., 2026-10-05, DOI10.1007/s00170-026-19118-x; 본문§4.2~4.3 열람|1차 수치실험·medium. 적재시간함수·하역고정시간, 물리 인계신호 계약을 명세하지 않아 Q5 결론에서 제외|
|C26|MiR, Interroll Case Study on MiR250 and AMR Logistics, 날짜 미확인; 사례전문 열람|1차 공급자·medium. 스위스다층제조·컨베이어사례, 독립성없음. 국내물류 정량자료 질문에 답 못하며 성능수치 검증불가로 제외|
|C28|Stephen J. Treado; S Cook; Banty Jain; Michael Galler, Modeling Building Access Control with BACnet, NISTIR, 웹게시2017-02-19; 초록만|1차 기관서지·본문 미열람. C27 기여자Treado와같은계열, 독립 BACnet 검증으로 세지 않음|

### 열람·추적 기록

- open-01~06.txt: 웹 도구 원문/실패 응답. c*.html/txt/pdf 및 c09/c10/c11/c12/c16/c29 고정커밋 보존본.
- C01 원URL redirect loop 후 CODIL의 같은 국토부 원문 PDF 열람. C06은 웹실패 후 curl HTML 전문 성공. C32는 웹403 후 curl 전문 성공. C24는 DOI/MDPI본문 실패 후 mdpi-res 출판사PDF 성공.
- C20: 웹PDF 절2-9-3,3-1-1 및 p16 개정이력 읽음; omron-find.txt,omron-body.txt에 보존. 표 그림을 읽은 것으로 표시하지 않음.
- PDF 시각대조: C01표지, C25표지, C27표지 이미지 열람 완료. 연구의 실험조건·제안상태는 추출문 해당절과 대조.
- 최종원문 비율18/20=90%. 1차 문헌20개이나 C02·C19는 본문아닌목록. 논문의 문헌인용·벤더결과까지 모두 독립1차 실험이라는 뜻은 아님.


## 부록 D. 검증 기록

## 5단계 자체 검증 기록

초안: draft-body.md와claims.json. 최종 검토본: reviewed-body.md와claims-reviewed.json. 원문 재대조: fact-verification.md. 반대 입장 대조: independent-verification.md. 자동 문자열 확인 뒤 주변 문맥·표 이미지를 직접 읽었다. 자동 확인만으로 검증 완료로 처리하지 않았다.

|항목|처음 태그 → 최종 태그|바꾼 이유·결과|
|---|---|---|
|1 사실 재대조 F01~F38·X01|사실 → 사실|관련 원문 모두 재열람. F01 짧은 구절을 메뉴의기관명에서 인증제운영총괄로 정밀화. F35 숫자19 단독을Table5의19·20·95% 묶음으로 정밀화|
|1 사실 재대조 F17|사실 → 사실|SUCCESS를 받는다는 표현에 요청ID일치 조건을 추가. 다른 요청 결과까지 완료로 오독하지 않도록 수정|
|1 사실 재대조 F21|사실 → 사실|IoT connector 조건을 문서에열거된 EL301·ED250로 한정. 임의문모델로일반화하지 않음|
|2 추론 분리|변경 없음|RMF 큐 소거의 실물인계 위험은 추정, 설계권고는 의견. 제조사 시험·NAVER 도입 주장은 초안부터추정|
|3 수치·번호 F33|사실 → 사실|그래프논문 §5 Experiment의근거쪽을PDF p11→p10으로수정. 직접렌더링한쪽과대조|
|3 수치 상충 F29·F30·F38|사실 → 사실; F38추가|122건, 실패14건과 전체성공률87.03%가 산술상 맞지 않음을발견. (122−14)/122×100≈88.52%. 다른분모가능성은 원자료없이판단불가. 실제성공률결론보류, U13추가|
|4 서지|변경 없음/서지명 정밀화|n10 열람대상명을README로정정. n2 2026-07-21·n15 2026-03-31·n16 2025-03-13·n17 2025-02-28 원문서지확인. n18 2026-03 호일자만. n19 2008-09-27 표지. 커밋날짜와문서초발행일구분|
|5 표현 강도|변경 없음|n8 should는권고, n12 예시절차 may vary유지. 제조사설치조건을법령상의무로표현하지않음|
|6 시행 상태|변경 없음|REEC운영기관 설명·설계제안·국토부R&D·KOLA발표·KS목록·SEMI개발제안을구분. SNARF승인을완성표준발행으로해석안함|
|7 독립성|변경 없음|RMF계열코드/설명/이슈, SCA와그인용논문, SEMI계열, NIST/백서기여자 중복을교차검증에서제외. X01만별도실물연구의질적관찰로계수|
|8 중복|변경 없음|VDA외부설비인터페이스 제외·RMF모드상수·문템플릿일반론은이미있어새보완에서제외. 원문미열람논문은방법과범위를추가|
|9 범위|변경 없음|지도계획알고리즘최적화·업무시스템·로봇전체안전인증의심화로확대하지않음. 물리설비연동과사례조건만보완|
|최종 형식·인용|완료|부록A~E·15보완·20출처·38F문장+X01·원문18/20. 인용구절과절/쪽/함수위치연결. 원문실패와목록만열람구분|

### 수정 집계 정의

- 태그 낮춤: **0문장**. 제조사성과·설계추론을초안부터추정/의견으로두었기때문이다. 태그변경횟수를만들기위해초안을고의로과장하지않았다.
- 검증에서 고친 문장: **2문장**(F17·F21, 본문 의미·범위를수정한고유문장). F33의근거쪽수정1건, 인용구절정밀화2건, 서지명정밀화1건, 새사실F38추가1건, U13추가1건은이숫자에섞지않는다.
- 확인못함: U01~U13 **13건**.
- 검증 전후를비교하려면draft-body.md와reviewed-body.md, claims.json과claims-reviewed.json을대조하면된다.

### 첫 영역 대비 지표 감시

|지표|01_F-21|03_F-22|검토 결과|
|---|---:|---:|---|
|보완 항목|15|15|같은수지만질문별새근거에맞춰선정|
|출처|20|20|원문미열람목록2개를포함하고성공사례수채우기자료제외|
|원문 비율|14/20=70%|18/20=90%|최소70%충족; 후보전체열람성공률과혼동하지않음|
|독립 교차 확인 주장|0|1|X01질적관찰만; 다른모든단일근거의한계유지|
|태그 낮춤|1|0|초안부터보수태그.0을검증누락으로숨기지않고변경내역공개|
|검증에서 고친 문장|이전기록별도집계없음|2|과거숫자를추측해비교하지않음|
|확인 못 함|11|13|우선질문의남은공백과수치충돌을그대로공개|

한 영역의 지표가 낮아도 목표 숫자에 맞춰 출처·문장·수정 건수를 늘리지 않는다. 검증 깊이는 모든 사실의 대조 행, 후보 탈락 이유, 독립성 판정, 9항목 기록으로 감시한다.


## 사실 문장별 원문 대조

## 사실 원문 재대조

초안 작성 뒤 원문 보존본의 해당 절·함수·표를 다시 읽었다. 아래 짧은 직접 구절은 위치 식별자이며 주변 문맥은 fact-recheck-context.txt와 원문 파일에 남겼다. 한 문헌의 여러 인용 총량은 짧게 유지했다.

|사실ID|출처|직접 구절|원문 위치·보존 파일|결과|
|---|---|---|---|---|
|F01|n1|“인증제 운영 총괄”|인증제도 > 인증기관; `c32.txt`|재대조 완료|
|F02|n1|“로봇 운영 관리 체계”|인증제도 > 인증분야; `c32.txt`|재대조 완료|
|F03|n2|“rather than from field experiments”|§5.2 Future Research Directions; `c03.txt`|재대조 완료|
|F04|n3|“’25~’28”|PDF p1 사업 개요; `c01.txt`|재대조 완료|
|F05|n3|“제도개선 방안을 마련”|PDF p2 셋째 중점과제; `c01.txt`|재대조 완료|
|F06|n4|“2025-05-09”|표준 이력사항 > 구분 개정 / 고시2025-0073; `open-01.txt`|재대조 완료|
|F07|n4|“병원의 환자 전용 엘리베이터를 제외”|일반정보 > 적용범위; `open-01.txt`|재대조 완료|
|F08|n5|“2026.03.27”|게시물 작성일 및 첫 문단; `c06.txt`|재대조 완료|
|F09|n5|“일반사항, 시험 설비 및 시험 절차”|본문 다섯째 □ 문단; `c06.txt`|재대조 완료|
|F10|n6|“has been granted control”|rmf_lift_msgs/msg/LiftState.msg 마지막 주석·필드; `c09/rmf_lift_msgs/msg/LiftState.msg`|재대조 완료|
|F11|n8|“should not broadcast the”|mxgrey 답변 2024-08-21, 둘째 문단; `c14.txt`|재대조 완료|
|F12|n8|“Some lifts might not have a special AGV mode”|동일 답변 셋째 문단; `c14.txt`|재대조 완료|
|F13|n7|“curr_request->session_id == msg->session_id”|src/lift_supervisor/Node.cpp _adapter_lift_request_update; `c10/rmf_fleet_adapter/src/lift_supervisor/Node.cpp`|재대조 완료|
|F14|n7|“REQUEST_END_SESSION”|동일 파일 _lift_state_update 마지막 else if; `c10/rmf_fleet_adapter/src/lift_supervisor/Node.cpp`|재대조 완료|
|F15|n7|“emit completion legacy state if lift is already on the level”|rmf_fleet_adapter/CHANGELOG.rst 2.13.0, #510; `c10/rmf_fleet_adapter/CHANGELOG.rst`|재대조 완료|
|F16|n6|“ACKNOWLEDGED=0”|rmf_dispenser_msgs/msg/DispenserResult.msg 및 rmf_ingestor_msgs/msg/IngestorResult.msg; `c09/rmf_dispenser_msgs/msg/DispenserResult.msg`|재대조 완료|
|F17|n7|“STATE_COMPLETED”|phases/DispenseItem.cpp _get_status, SUCCESS case; `c10/rmf_fleet_adapter/src/rmf_fleet_adapter/phases/DispenseItem.cpp`|재대조 완료|
|F18|n7|“we'll assume it's finished”|동일 함수 queue 검사 마지막 분기; `c10/rmf_fleet_adapter/src/rmf_fleet_adapter/phases/DispenseItem.cpp`|재대조 완료|
|F19|n9|“via websocket”|README 첫 문단·세 구성파일 설명; `c12/README.md`|재대조 완료|
|F20|n9|“access_id and access_secret”|README Fill up config, 1. Get access_id; `c12/README.md`|재대조 완료|
|F21|n10|“requires the Dormakaba IoT connector”|README 도입부; `c29/README.md`|재대조 완료|
|F22|n10|“Credentials”|README 마지막 문장; `c29/README.md`|재대조 완료|
|F23|n11|“dry contact”|Overall System Overview, server→PLC 설명; `c13.txt`|재대조 완료|
|F24|n11|“Manual intervention is needed”|Lift Exceptions and Recovery Behaviour, Table1 row2; `c13.txt`|재대조 완료|
|F25|n12|“readiness check”|§2-9-3, 인쇄p2-13~2-14 / PDF47~48쪽; `omron-body.txt`|재대조 완료|
|F26|n12|“may vary”|§2-9-3 마지막 문단; `omron-body.txt`|재대조 완료|
|F27|n13|“SEMI E84-0823 - Current”|제품목록 Revision 및 Abstract; `open-04.txt`|재대조 완료|
|F28|n14|“New Preliminary Standard”|SNARF 머리·§1·§2; 작성일 필드; `open-04.txt`|재대조 완료|
|F29|n15|“122 eligible missions”|§2.1·2.4 및 §4.5; `c22.txt`|재대조 완료|
|F30|n15|“14 delivery failures”|§3.2 Failure-type classification; `c22.txt`|재대조 완료|
|F31|n15|“site-specific”|§4.5 첫 문단; `c22.txt`|재대조 완료|
|F32|n16|“base waiting time for elevators at 30 s”|§4.1 사례 설정·항목5; `c23.txt`|재대조 완료|
|F33|n17|“15-story building”|§5 Experiment, PDF p10 (쪽 이미지 재대조); `c24.txt`|재대조 완료|
|F34|n18|“각 층의 절반 영역”|§3.3, 인쇄p55 및 §2.3; `c25.txt`|재대조 완료|
|F35|n18|“19 20 95%”|인쇄p56 Table5; `c25.txt`|재대조 완료|
|F36|n19|“basis for proposed changes”|PDF p1 Abstract·표지; `c27.txt`|재대조 완료|
|F37|n19|“specific door at a specific time”|§3 Physical Access Control, PDF p10; `c27.txt`|재대조 완료|
|F38|n15|“87.03%”|§3.1 Relationship between the elevator operating rate and delivery failures; `c22.txt`|재대조 완료|
|X01|n15·n18|n15 “cumulative delays”; n18 “외부 이용자”|n15 §3.4 결과 마지막 문단; n18 인쇄p56 Table5 아래문단. c22.txt 및 c25.txt|두 별도 실물 관찰에서 지연 확인; 수치 일반화 제외|

## 부록 E. 독립 검증 대조표

## 독립 검증 대조표

여기서 독립성은 **근거 출처·연구팀·실험의 독립성**이다. 별도 검토자·에이전트가 검증했다는 뜻은 아니다. 같은 조사자가 초안 이후 반대 입장에서 원문을 다시 읽었다. 원자료·현장실행을 재현하지 않았다.

|항목|지지 근거·위치|반대 근거·독립성 대조|최종 판정|
|---|---|---|---|
|K01 REEC|n1인증기관·분야; n2§2.1·5.2|n2는n1을인용하며R&D지원. 독립 인증실적검증아님|기관 설명·연구방법만 사실; 상세판·법정의무 미확인|
|K02 연구개발|n3p1~2|계획형 미래문장. 인증시행·실증완료 자료가아님|계획임을유지|
|K03 KS|n4일반정보·이력|통합필드명은개정확인일이나이력행은개정. 본문미열람|개정일·목록범위만사실|
|K04 KOLA|n5작성일·첫/다섯째문단|표준번호없음; 첨부사진을표준본문으로볼수없음|보도일·발표내용만사실|
|K05 세션|n6LiftState주석; n8답변|둘다RMF설계계열. n8은AGV모드가없는장치도언급|수락의미와조건부권고. 독립교차0|
|K06 종료·변경|n7supervisor함수·CHANGELOG|같은프로젝트의다른파일. 최신2.14.0과관련변경2.13.0구별|해당분기·변경기록만사실|
|K07 인계완료|n6result메시지; n7DispenseItem|SUCCESS외ACK이후큐소거도완료경로. 요청ID조건존재|초안F17조건추가. 물리센서성공은미증명|
|K08 KONE|n9README·연결코드|과거어댑터판과현행제조사계약다름. 실승강기시험자체보고|구조·절차사실, 성능/시험성과추정|
|K09 자동문|n10README|특정모델과IoTconnector조건; 현장권한정책없음|F21지원모델범위추가|
|K10 PLC비상|n11Overview·Table1|특정현장; 상태1Hz/2초충돌; 독립인증자료아님|연결·복구설명사실, 주기확정보류|
|K11 인계규격|n12§2-9-3; n13목록; n14SNARF|OMRON과SEMI는기관이다르나같은구현검증아님. 예시/반도체범위/제안상태상이|독립교차0.중립범용표준결론보류|
|K12 병원 수치|n15§2.4·3.1·3.2·4.5|122건·14실패와87.03%전체성공률불일치. 제조사공동저자|보고값출처명시, 성공률성능채택보류·U13|
|X01 공유 승강기 지연|n15§3.4 지연결과; n18p56 외부이용자로인한층간지연|구로병원·DOGU와KAIST는저자·시설·실험이다름. 현장·방식·규모차이유지|독립교차1. 질적관찰한정;임계값·국내물류처리량전용안함|
|K13 방법·범위|n16§4.1·5; n17§5; n18§3.3·Table5|실평면기반수치실험과실물구별. C24고려대/C22고려대일부기관중복|방법조건만비교;수치통합없음|
|K14 BACnet|n19표지·§3|2008작업백서. NIST n28초록은Treado겹침·본문미열람|현행규범아님, 독립교차0|
|K15 NAVER|n20관련두소제목|같은사업블로그끼리비독립. 현재배송과연말확대·이기종지원설계구별|추정유지. 독립운영성능미확인|

동일 주장 독립 교차 확인 합계는 **1개**다. 표준 목록의 제정 정보와 구현 기능을 나란히 열거한 것은 교차 검증으로 세지 않았다.

