---
area: 48
title: "48. 안전·위험 관리"
researched: 2026-10-11
researcher: "OpenAI Codex"
---

# 48. 안전·위험 관리 — 보완 조사

## 요약
- 플릿 위험 분석에 STPA 산출물과 11로봇 제어구조 분석 사례를 보강한다. 분석 모델과 현장 효과를 구별한다(보완 1~3).
- R15.08 Part 3 발행, ISO 개발단계, 국내 KS 번호·범위를 각각 공식 목록의 확인 범위로 정리한다(보완 4~6).
- 국내 위험성평가의 주체·참여·변경 조건과 2026 행정예고안을 구분한다(보완 7~9).
- VDA pause, 감시 코드, 제조사 인터록, RMF 플릿 선택 기능의 실제 경계를 보강한다(보완 10~13).
- EU 변경 조건과 SafeGate의 평가 분모를 분리하고, 개별 인증 판단·검증되지 않은 성능 일반화는 열린 질문으로 남긴다(보완 14~15).

## 보완 항목

문장 ID F01 등은 원문 재대조 기록과 연결된다. 본문의 근거 메모에 직접 인용을 한 번씩 싣고, 부록 D·E는 그 ID와 위치를 참조한다. 표준 목록을 본 경우 본문 열람으로 집계하지 않았다.

### 01. 6. 대표 접근법 — 추가: STPA 산출물과 재개 시나리오
- 새 내용:
  - **F01** STPA Handbook은 분석 목적, 제어구조, 위험한 제어행동, 손실 시나리오를 기본 분석 흐름으로 제시한다. [사실][^n1]
  - **F02** 위험한 제어행동 분석은 미제공, 위험한 제공, 잘못된 시점·순서, 지속 제어의 과도한 지속·조기 종료를 구별한다. [사실][^n1]
- 근거 메모:
  - F01: PDF 14쪽, Chapter 2 Method Overview. 원문 “Defining the purpose … control structure … unsafe control actions … Scenarios”.
  - F02: PDF 36쪽, Table 2.3 아래 네 유형. 원문 “too early, too late”.
- 범위·독립성·위키 대조: 방법론 원문 한 출처다. 항공기 예시를 로봇 플릿의 실증 결과로 계산하지 않는다. 위키의 STPA 소개는 유지하고 실제 분석 산출물만 보강한다.
- ROP 시사점: 혼합 플릿에서는 손실→위험→제어행동→안전제약→시험의 연결표를 작성한다. 제어구조에는 ROP, 어댑터, 로봇, 설비, 현장 운영자를 넣고 정지뿐 아니라 잘못된 재개와 오래된 상태에 따른 재배정을 분석한다. [의견]

### 02. 8. 대표 연구 — 추가: 다중 로봇 제어구조 비교의 조건
- 새 내용:
  - **F03** Bensaci 등의 2020년 연구는 화학 분석실에서 화학제품을 운반하는 11로봇 시스템을 분석 대상으로 설정한다. [사실][^n2]
  - **F04** 이 연구는 중앙형·계층형·수정 계층형의 STPA 시나리오를 Bowtie 기반 반정량 평가로 분류한다. [사실][^n2]
  - **F05** 저자들은 일부 시나리오와 원인 요인을 정량적으로 구별하기 어려워 평가에서 합쳤다는 한계를 명시한다. [사실][^n2]
- 근거 메모:
  - F03: 공개 논문 §3, 본문 7쪽; 열람 L749~755. 원문 “eleven robots”.
  - F04: §3.1, §4.1~5.2; 열람 L807~851, L902~956. 원문 “semi quantitative”.
  - F05: §6 결론 마지막 문단, 본문 17쪽; L1969~1982. 원문 “the same in our evaluation”.
- 범위·독립성·위키 대조: 공개 early article 본문을 읽었다. 11대 실물의 사고율을 비교한 시험으로 확인한 것이 아니다. 중앙형 열위라는 저자 결론을 모든 ROP 구조에 일반화하지 않는다. 2023 STPA/SPN 논문 C02는 여전히 원문 미열람이며 이 논문으로 대신 검증했다고 쓰지 않는다.
- ROP 시사점: 제어구조 대안을 비교할 때 누락 명령, 지연 명령, 통신 단절을 따로 등록하고 빈도·심각도에 사용한 가정과 데이터 출처를 남긴다. 정량 데이터가 없으면 분석 결과를 사고 확률처럼 표시하지 않는다. [의견]

### 03. 5. 적용 사례·8. 대표 연구 — 추가: 건설 현장 평가와 효과의 구분
- 새 내용:
  - **F06** Belzile 등의 사례는 캐나다 몬트리올 Pomerleau 건설 현장에 Clearpath Jackal을 배치하려는 상황을 다룬다. [사실][^n3]
  - **F07** 논문의 잔류 위험지수는 제안한 완화대책을 바탕으로 다시 추정한 값이다. [사실][^n3]
- 근거 메모:
  - F06: PDF 5쪽 §4 Case Study. 원문 “intended deployment”.
  - F07: PDF 7쪽 §4.3, Table 3 앞 문단. 원문 “a new risk index was estimated”.
- 범위·독립성·위키 대조: 단일 로봇 현장 맥락의 위험성평가다. 실제 현장이라는 조건과 완화대책 효과를 실험으로 검증했다는 주장을 구별한다. arXiv v1 업로드일은 2025-02-28이고 동일 제목 2021 ICAR 워크숍판도 존재한다. 두 판은 독립 출처가 아니다.
- ROP 시사점: 현장별 위험등록부에 초기 위험, 제안 대책, 예상 잔류 위험, 조치 완료 증거, 재검증 결과를 별도 필드로 둔다. 건설 현장의 평가 항목을 물류센터의 검증된 수치로 복사하지 않는다. [의견]

### 04. 7. 표준·오픈소스 — 수정: R15.08 Part 3 발행 상태
- 대상 문장/정정 대상 원문 구절: “로봇 자체는 Part 1, 사용자 요구는 예정된 Part 3 이 맡는다.”
- 새 내용:
  - **F08** A3 공식 목록은 ANSI/A3 R15.08-3-2026의 발행일을 2026-04-23으로 표시한다. [사실][^n4]
- 근거 메모:
  - F08: 공식 목록 Published, 열람 L260~263. 원문 “Published April 23, 2026”.
- 범위·독립성·위키 대조: 유료 규격 본문은 읽지 않았다. 공식 목록의 발행 사실만 정정하며 사용자 의무의 세부 조항을 새로 확정하지 않는다. A3의 Part 2 발표와는 같은 기관 계열이다.
- ROP 시사점: 사용자 운용·변경관리 검토용 표준 목록에 발행된 Part 3를 추가하고, 실제 계약·안전 요구 매핑 전 정식 본문의 적용범위를 확인한다. [의견]

### 05. 7. 표준·오픈소스 — 수정: 두 ISO 개정 프로젝트의 실제 단계
- 대상 문장/정정 대상 원문 구절: “차기판(제2판 초안)이 위원회 검토 단계에 있다.”
- 새 내용:
  - **F09** ISO 목록에서 ISO/DIS 3691-4의 차기판은 Edition 3으로 표시된다. [사실][^n5]
  - **F10** 이 프로젝트의 DIS 투표 종료 단계 40.60은 2026-09-10으로 기록된다. [사실][^n5]
  - **F11** ISO/DIS 12100.3 프로젝트는 2026-09-15에 40.60 투표 종료 단계로 기록된다. [사실][^n6]
- 근거 메모:
  - F09: 공식 목록 머리말 L15, General information. 원문 “Edition 3”.
  - F10: Life cycle L182. 원문 “40.60 2026-09-10 Close of voting”.
  - F11: Life cycle L140~143. 원문 “40.60 2026-09-15 Close of voting”.
- 범위·독립성·위키 대조: 둘 다 공식 목록만 열람했다. 단계 40.60을 국제표준 발행 또는 FDIS 완료로 번역하지 않는다. 위키의 3691-4 위원회 초안·제2판 표기는 접근일 현재의 목록과 다르다. 12100의 FDIS 전망은 전망으로 남긴다.
- ROP 시사점: 표준 대장에 발행본과 개발 프로젝트를 따로 기록하고, 개발단계의 예상 요구를 적용 의무로 배포하지 않는다. [의견]

### 06. 7. 표준·오픈소스·11. 열린 질문 — 추가: 국내 번호와 범위
- 새 내용:
  - **F12** 공식 목록은 KS B 7327의 표제를 산업용 이동 머니퓰레이터의 응용을 위한 안전 요구사항으로 표시하고 발행일을 2024-11-01로 기록한다. [사실][^n7]
  - **F13** 이 목록의 적용범위에는 통합 제조 시스템, 관제 시스템, 군집 관리 시스템, 기타 기계 설비류가 표준의 대상에서 제외된다고 적혀 있다. [사실][^n7]
  - **F14** KS B ISO 3691-4의 2026-09-14판 공식 목록은 국제표준 부합화를 ISO 3691-4:2023(IDT)로 표시한다. [사실][^n8]
- 근거 메모:
  - F12: 목록 L208~212. 원문 “KS B 7327 … 산업용 이동 머니퓰레이터의 응용을 위한 안전 요구사항 … 2024-11-01”.
  - F13: 목록 적용범위 L228. 원문 “관제 시스템, 군집 관리 시스템”.
  - F14: 목록 구매정보 L212~214, 상세정보 고시2026-0288. 원문 “2026-09-14 … ISO 3691-4:2023(IDT)”.
- 범위·독립성·위키 대조: 두 KS 모두 목록만 읽었다. KS B 7327을 R15.08-2의 동일 채택판 또는 혼합 플릿 전체 인증으로 쓰지 않는다. 국내 IDT 판과 ISO에서 개발 중인 DIS는 구별한다. 조항별 국제 대응표는 확인 못 했다.
- ROP 시사점: 로봇 본체·머니퓰레이터 응용과 관제·플릿 통합의 위험평가 범위를 나누고, 빠진 인터페이스 위험을 시스템 위험등록부에서 다룬다. [의견]

### 07. 3. 범위·9. 책임 경계 — 추가: 국내 고시의 주체와 변경 조건
- 새 내용:
  - **F15** 고시2024-76 제5조제2항은 해당 도급사업의 도급사업주와 수급사업주가 각각 위험성평가를 실시하도록 규정한다. [사실][^n9]
  - **F16** 같은 고시 제6조는 위험 수준 기준 설정부터 감소대책 실행 확인까지 열거한 경우에 해당 작업 근로자를 참여시키도록 규정한다. [사실][^n9]
  - **F17** 제15조제2항은 열거한 변경 등에 따라 추가적인 유해·위험요인이 생기는 경우 수시 위험성평가를 요구한다. [사실][^n9]
- 근거 메모:
  - F15: 제5조제2항, 저장 본문 L46~49. 원문 “각각 제1항에 따른 위험성평가를 실시하여야 한다”.
  - F16: 제6조 각 호. 원문 “해당 작업에 종사하는 근로자를 참여시켜야 한다”.
  - F17: 제15조제2항 본문 및 제1~6호. 원문 “추가적인 유해ㆍ위험요인이 생기는 경우”.
- 범위·독립성·위키 대조: 열람한 판은 2024-12-18 고시, 2025-01-02 시행이다. 제15조제4항의 상시평가 인정 경로 등 관련 규정도 함께 검토해야 한다. 소프트웨어 버전 변경 그 자체가 자동으로 재심사 대상이라는 결론은 내리지 않는다. 2026 상위법 개정과 개별 사업장 적용은 이 문서에서 확정하지 않았다.
- ROP 시사점: ROP 변경심사표에 변경한 작업절차, 추가 위험, 평가 담당자, 근로자 참여 기록을 남긴다. ROP 사업자·제조사·설비업체의 계약상 역할은 해당 현장의 법적 주체와 함께 별도 확정한다. [의견]

### 08. 6. 대표 접근법 — 추가: 운영자 참여 기록의 구체화
- 새 내용:
  - **F18** 고용노동부의 근로자 참여 가이드는 수급업체 근로자 청취조사에서 아차사고 경험과 개선 의견을 수집하는 방법을 제시한다. [사실][^n11]
  - **F19** 같은 가이드는 문자와 QR코드를 통한 익명 제안 방식을 사례로 소개한다. [사실][^n11]
- 근거 메모:
  - F18: PDF 9쪽·인쇄6쪽 핵심 포인트. 원문 “아차사고 사례”.
  - F19: PDF 10쪽·인쇄7쪽 사례1. 원문 “문자·QR코드를 활용하여 익명으로”.
- 범위·독립성·위키 대조: 공식 가이드의 참여 방법 사례다. 통제집단이 있는 사고감소 효과 검증으로 해석하지 않는다. 고시와 가이드는 고용노동부 정책 계열로 독립 두 출처가 아니다.
- ROP 시사점: 플릿 위험 검토에 운영자·정비자·청소/도급 작업자의 아차사고 제보를 연결하고, 제보→평가→조치→현장 피드백의 처리 이력을 남긴다. [의견]

### 09. 12. 최근 확인 — 추가: 위험성평가 개정안의 지위
- 새 내용:
  - **F20** 고용노동부는 2026-09-23 공고2026-461로 사업장 위험성평가 지침 전부개정고시안을 행정예고했다. [사실][^n10]
  - **F21** 공고의 의견 제출 기한은 2026-10-13이다. [사실][^n10]
- 근거 메모:
  - F20: 공고 HWPX 첫머리 L1~6. 원문 “전부개정고시(안) 행정예고”.
  - F21: 공고 3. 의견제출 L39~40. 원문 “13일까지”.
- 범위·독립성·위키 대조: 접근일은 2026-10-11이다. 행정예고를 최종 고시 발령 또는 시행으로 쓰지 않는다. 본문 개정안의 상세 요구는 시행 규정으로 인용하지 않는다.
- ROP 시사점: 법규 변경 대장에 예고안과 현행 문서를 분리하고 최종 발령·시행일을 후속 확인한 뒤 현장 위험성평가 절차를 갱신한다. [의견]

### 10. 4. 주요 구성요소·5. 적용 사례 — 추가: VDA 5050의 정지·재개 계약
- 새 내용:
  - **F22** VDA 5050 3.0.0은 자신을 안전 표준으로 간주하거나 적용해서는 안 된다고 명시한다. [사실][^n12]
  - **F23** startPause에서는 일시정지 가능한 행동은 정지하고 나머지 행동은 계속된다. [사실][^n12]
  - **F24** stopPause는 pause 모드를 해제하는 동작으로 정의된다. [사실][^n12]
  - **F25** safetyState의 비상정지 필드명은 activeEmergencyStop이고 값은 MANUAL, REMOTE, NONE이다. [사실][^n12]
- 근거 메모:
  - F22: 범위 제외항목, 고정 명세 L135~136. 원문 “shall not be regarded or applied as a safety standard”.
  - F23: 고정 명세 actions 표 L701. 원문 “other actions continue”.
  - F24: 고정 명세 actions 표 L702. 원문 “Deactivates the pause mode”.
  - F25: 고정 명세 L1916~1918; json_schemas/state.schema L893~908. 원문 “activeEmergencyStop … MANUAL … REMOTE … NONE”.
- 범위·독립성·위키 대조: 명세와 스키마는 같은 VDA 프로젝트다. REMOTE는 시설 비상정지의 원격 확인 상태를 나타내며, 이 필드 자체에서 임의 ROP 명령경로의 PL을 도출하지 않는다. stopPause는 비상정지 회로 리셋의 일반 명령으로 확인되지 않았다.
- ROP 시사점: 업무 pause 해제와 현장 안전정지 해제 승인을 별도 상태로 관리한다. 안전 기능 해제의 제조사·설비 조건을 충족했다고 확인하기 전 작업 재개를 지시하지 않는 정책을 검토한다. [의견]

### 11. 6. 대표 접근법·7. 공개 구현 — 추가: 감시와 대응의 구분
- 새 내용:
  - **F26** Nav2 collision_monitor의 1.5.2 README는 하드 실시간 안전 인증을 제공하지 않는다고 명시한다. [사실][^n13]
  - **F27** Monitoring ROS2 논문의 제안 방식은 위반의 탐지와 보고로 한정된다. [사실][^n20]
- 근거 메모:
  - F26: README L10. 원문 “does not provide hard real-time safety certifications”.
  - F27: PDF 7쪽·인쇄214쪽 §3 끝. 원문 “limited to detecting and reporting violations”.
- 범위·독립성·위키 대조: Nav2의 한 구현과 Ogma 논문의 방식은 별개다. 두 출처가 모든 ROS 2 구현의 동일한 속성을 입증하는 것은 아니다. 모니터 코드의 실시간성 설명을 ROS 2 시스템 전체의 인증으로 확대하지 않는다.
- ROP 시사점: 위험등록부에 탐지 주체, 대응 결정자, 실제 정지 액추에이터, 최대 허용 지연, 감시 자체 장애 시 대응을 분리해 기입한다. 둘은 독립 자료이지만 공통의 제품 안전성 주장을 교차 입증한 것으로 세지 않는다. [의견]

### 12. 9. 책임 경계 — 추가: 제조사 플릿 정보와 안전 인터록
- 새 내용:
  - **F28** OMRON LD Safety Guide Rev H는 플릿의 위치·크기·경로계획 정보 교환을 충돌 방지 인터록으로 보지 않으며 사용/통합자의 별도 인터록 책임을 설명한다. [추정][^n14]
  - **F29** 같은 매뉴얼은 외부 비상정지에 사용자 제공 부품이 포함될 때 전체 PL·PFH 계산과 최종 위험성평가를 사용자 책임으로 설명한다. [추정][^n14]
- 근거 메모:
  - F28: PDF/인쇄17쪽 Fleet 경고. 원문 “not an interlocked method”.
  - F29: PDF/인쇄18쪽 PL and PFH 표 주석. 원문 “inclusive of user-supplied components”.
- 범위·독립성·위키 대조: 단일 벤더·특정 제품의 2019년 매뉴얼이므로 처음부터 추정 태그를 쓴다. 해당 설명을 타사 플릿 전체의 법률 의무 또는 현재 모든 OMRON 모델의 구성으로 일반화하지 않는다.
- ROP 시사점: 관제의 위치 공유·교통 조율과 안전 인터록 경로를 서로 다른 인터페이스로 문서화하고, 시스템 통합 때 추가된 부품까지 포함한 검증 자료를 요구한다. [의견]

### 13. 5. 적용 사례 — 수정: RMF 화재 신호의 플릿 선택
- 대상 문장/정정 대상 원문 구절: “이슈 작성 시점(2025-04-04) 기준으로 비상 신호는 대상 플릿을 구분하지 않는 불리언 값이었고, 이후 구현 여부는 미확인이다.”
- 새 내용:
  - **F30** RMF issue 658의 작성자는 2025-04-04에 두 건물의 배치에서 한 건물 화재경보가 모든 로봇을 주차시킨다고 보고했다. [사실][^n15]
  - **F31** rmf_fleet_adapter CHANGELOG는 플릿 이름으로 화재경보를 분리하는 PR413을 2.10.0(2025-05-09) 절에 수록한다. [사실][^n17]
  - **F32** rmf_ros2 2.14.0의 대상 비상신호 처리기는 fleet_names가 비었거나 자신의 플릿 이름을 포함하면 handle_emergency에 is_emergency 값을 전달한다. [사실][^n16]
- 근거 메모:
  - F30: 이슈 본문 L160,168~174. 원문 “ALL robots will go into parking”.
  - F31: 2.14.0 고정 CHANGELOG L100~111. 원문 “separate fire alarm by fleet names”.
  - F32: FleetUpdateHandle.cpp L1444~1465; Node.cpp L73~79. 원문 “emergency_signal->fleet_names.empty()”.
- 범위·독립성·위키 대조: 보고, 변경 이력, 코드는 모두 Open-RMF 계열이므로 독립 교차 확인이 아니다. 코드 열람은 배치 시험·대피 안전성 인증이 아니다. 2.14.0은 확인한 판이며 기능 최초 도입판으로 쓰지 않는다. 건물 구분은 플릿 이름 매핑 설계와 별도다.
- ROP 시사점: 전체 플릿 전파를 뜻하는 빈 목록을 운영 UI에서 명확히 표시하고 잘못된 플릿 선택, 지연·중복 신호, 재개 전 승인 조건을 시험한다. 화재 시 로봇의 이동/정지 정책은 현장 대피 계획과 함께 정한다. [의견]

### 14. 9. 책임 경계·11. 열린 질문 — 추가: EU 실질적 변경의 조건
- 새 내용:
  - **F33** Regulation (EU) 2023/1230 제3조(16)의 실질적 변경 정의에는 출시·사용 개시 뒤 제조사가 예상하거나 계획하지 않은 물리적 또는 디지털 변경이 포함된다. [사실][^n18]
  - **F34** 그 정의는 새 위험요인 또는 기존 위험 증가로 안전에 영향을 주며, 안전제어시스템 변경을 필요로 하는 방호장치 추가 또는 안정성·기계적 강도의 추가 보호조치를 필요로 한다는 조건을 둔다. [사실][^n18]
  - **F35** 제54조의 일반 적용일은 2027-01-20이고 열거된 조항에는 별도 적용일이 있다. [사실][^n18]
- 근거 메모:
  - F33: 2026-07-27 통합본 PDF 6쪽 Art.3(16). 원문 “physical or digital means … not foreseen or planned”.
  - F34: 같은 조항 Art.3(16)(a)~(b). 원문 “existing safety control system … stability or mechanical strength”.
  - F35: 통합본 PDF 51~52쪽 Art.54. 원문 “20 January 2027”.
- 범위·독립성·위키 대조: EU 관할의 통합 참고본 조문 확인이다. 제18조도 검토했지만 ROP 정책/어댑터의 개별 업데이트가 실질적 변경인지 또는 누가 제조자인지는 판정하지 않는다. 디지털 변경이라는 이유만으로 모든 갱신을 재인증 대상으로 쓰지 않는다.
- ROP 시사점: 업데이트마다 안전 관련 동작 변화, 제조사 예상 범위, 추가 위험, 방호/안전제어 변경의 영향을 기록하고 해당 관할 전문가의 적용 판단에 연결한다. [의견]

### 15. 8. 대표 연구 — 추가: SafeGate 평가 층위와 확인되지 않은 분모
- 새 내용:
  - **F36** SafeGate v1의 230개 합성 작업 벤치마크는 실행 전 단계 1~3을 평가한다. [사실][^n19]
  - **F37** 같은 논문은 별도로 30개 AI2-THOR 시뮬레이션 시나리오를 평가했다고 보고한다. [사실][^n19]
  - **F38** 실물 로봇 결과는 §VI-C에서 정성 결과로 보고된다. [사실][^n19]
- 근거 메모:
  - F36: PDF 6쪽 §V-A. 원문 “synthetic benchmark of 230 robot tasks”.
  - F37: PDF 6쪽 §V 서두·§V-B. 원문 “30 AI2-THOR”.
  - F38: PDF 8쪽 §VI-C. 원문 “Qualitative results”.
- 범위·독립성·위키 대조: arXiv v1 프리프린트이며 게재지와 저자 공식 실행코드는 확인 못 했다. PDF 7~8쪽을 이미지로 대조했다. 식(9)의 충돌률 분모는 실행된 작업인데 §VI-B는 30개를 모두 차단하며 CR=0이라고 쓴다. 실행 0건 처리 규칙을 확인하지 못해 이 수치를 검증된 무사고율로 인용하지 않는다. 표II의 총183건과 전체230건 간 제외/범주 규칙도 미확정이다.
- ROP 시사점: 실행 전 분류, 계획 검증, 실행 중 감시를 서로 다른 시험 묶음으로 관리한다. 위험 작업 차단률과 실제 실행된 작업의 안전 결과를 다른 분모로 공개하고 미실행을 성공 실행으로 세지 않는다. [의견]

## 답한 열린 질문

아래 질문은 원문 ID와 의미를 유지한 요약이다. 긴 문장의 반복 인용은 피했다. 원문 전체와 질문 ID는 `.research-work/M-48/2026-09-25-area25-s11.txt`의 「3. 본문」에 보존되어 있다.

|질문|판정·답변|근거·한계|
|---|---|---|
|oq-070: 2024-11 이동식 협동로봇 KS 번호와 국제규격 대응|**부분 답변**: KS B7327의 번호·표제·목록범위를 확인했다. [추정]|보완6 F12~F14, [^n7][^n8]. 국제 조항대응은 미확정|
|oq-064: R15.08-2 유형C 통합요구에 대응하는 국내 기준|**부분 답변**: 관련 KS를 식별했지만 R15.08-2와의 동등성·시스템 통합 전체를 포괄하는 인증 대응은 확인하지 못했다. [추정]|보완6. KS7327 목록의 관제/군집관리 제외범위를 함께 제시|
|oq-093: ROP 정책·어댑터 변경에 EU 실질적 변경 판단이 적용되는가|**부분 답변**: 디지털 변경을 포함하는 조건부 정의와 일반적용일을 확인했다. 특정 업데이트의 법적 분류는 답하지 않았다. [추정]|보완14 F33~F35, [^n18]|
|신규 질문: 혼합 플릿 RA를 누가 수행·갱신하는가|**부분 답변**: 국내 고시의 도급/수급 주체와 근로자 참여 조건을 제시했다. ROP·제조사·설비업체별 실제 책임은 미확정이다. [추정]|보완7·12, [^n9][^n14]|
|신규 질문: VDA 원격/플릿 정지 경로의 PL 요구|**부분 답변**: 명세의 비안전규격 범위와 상태필드를 확인했다. 특정 제어경로의 PL을 결정하지 못했다. [추정]|보완10·12, [^n12][^n14]|
|oq-092: 펌웨어·안전파라미터 변경의 국내 재심사|**확인 못 함**: 일반 인증 절차만으로 해당 제도의 구체적인 재심사 조건을 확정할 수 없다.|U04; C34 미채택|
|신규 질문: 규칙223 울타리 생략의 AMR플릿 적용|**확인 못 함**: 개별 현장/인증기준의 적용을 확인하지 않았다.|U05; 사람 근접·인증 심화는 M49/M50 연결로 남김|

## 새로 생긴 열린 질문

- SafeGate의 실행 0건일 때 CR 산정 규칙과 표II에서 제외한 범주를 저자 코드·원자료로 재현할 수 있는가?
- RMF 선택 비상신호를 건물/구역 모델에 연결할 때 플릿 공유·재개 승인·네트워크 단절을 어떻게 검증하는가?
- 혼합 제조사 현장에서 위험성평가의 제어구조·변경 이력·근로자 제보를 하나의 위험등록부로 연결한 공개 실증은 있는가?

### 확인 못 한 항목 대장

집계 단위는 아래 **U01~U14의 질문/증거 공백 14개**다. 단순히 접근 실패 URL 수나 태그 수를 세지 않는다. 본문과 중복되는 공백은 이 ID로 합산한다.

|ID|남은 공백|후속 확인 조건|
|---|---|---|
|U01|2023 STPA/SPN 논문 C02 본문|출판사/저자 공개 원문을 확보해 모델·실험 조건 재평가|
|U02|다중로봇 구조 분석의 실물/혼합제조사 안전 효과, Belzile 판 차이|현장시험 설계·원자료와2021/2025판 전체변경 이력|
|U03|KS7327과R15.08-2/ISO10218 조항별 대응·동등 인증|각 규격 본문과 공식 대응/인증 기준|
|U04|국내 설치 작업장 인증의 펌웨어/안전파라미터 변경 재심사|해당 인증 제도의 공식 변경심사 조항|
|U05|규칙223 울타리 예외의 개별AMR플릿 적용|현행 조문·공식 해석과 현장 적용 조건|
|U06|ROP 원격/플릿 안전정지 경로의 요구PL·검증|기능별 위험평가와 제조사 안전 인터페이스 증거|
|U07|실제 혼합플릿 프로젝트의 수행·갱신 책임 주체|관할법·사업주구조·계약·통합범위 확인|
|U08|특정ROP 업데이트의 EU 실질적 변경 해당 여부|정의 각 조건과 해당 제품 변경 영향에 대한 판단|
|U09|SafeGate 저자 공식코드·재현자료|논문과 저자가 연결한 저장소/데이터|
|U10|SafeGate 실행0건의CR=0 산정 규칙|분모/예외 처리 구현·저자 설명|
|U11|SafeGate 표II183건과전체230건의 포함·제외 규칙|범주별 데이터·혼동행렬 산출 과정|
|U12|RMF 실제배치의 비상/재개/통신장애 동작|고정판 통합시험·현장 비상계획 검증|
|U13|2026 위험성평가 고시안의 최종 발령·시행 상태|행정예고 이후 최종 고시와 상위법 변화의 종합 확인|
|U14|목록만 본5개 표준의 세부 요구|Part3,ISO DIS3691-4,DIS12100.3,KS7327,KS3691-4의 정식본문|

## 출처

집계: 총 **20개**, 원문 열람 **15/20(75%)**, 1차 자료 **20개(본문15·공식목록5)**, 독립 교차 확인된 주장 **0개**. 새 출처 **14개**. 원문 열람은 인용 관련절의 직접 열람을 뜻한다. 미러·판 차이는 신규 독립 출처로 세지 않았다. 위키에서 이미 다룬 C03/C07/C23/C28/C33/C37의 후속판·원문 확인은 새 출처 수에서 보수적으로 제외했다.

[^n1]: Nancy G. Leveson, John P. Thomas, STPA Handbook, March 2018, DOI 없음. [원문 또는 공식 목록](https://psas.scripts.mit.edu/home/get_file.php?name=STPA_handbook.pdf). 접근일 2026-10-11. 원문 열람(인용 관련 본문).
[^n2]: Chaima Bensaci, Youcef Zennir, Denis Pomorski, Fares Innal, Yiliu Liu, Cherif Tolba. STPA and Bowtie risk analysis study for centralized and hierarchical control architectures comparison. Alexandria Engineering Journal 59(5),3799–3816,2020. 공개 early article 판은 2020-06-21 채택, 공개목록 July2020; 정확 온라인 발행일 미확인. DOI10.1016/j.aej.2020.06.036. [원문 또는 공식 목록](https://www.researchgate.net/publication/342753871_STPA_and_Bowtie_Risk_Analysis_Study_for_Centralized_and_Hierarchical_Control_Architectures_Comparison). 접근일 2026-10-11. 원문 열람(인용 관련 본문).
[^n3]: Bruno Belzile, Tatiana Wanang-Siyapdjie, Sina Karimi, Rafael Gomes Braga, Ivanka Iordanova, David St-Onge, From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment, arXiv:2502.20693v1, 2025-02-28. DOI10.48550/arXiv.2502.20693. 동일 제목 ICAR2021 Workshop on Design, Learning, and control for safe human-robot collaboration,2021-12-07 별도 확보;2025판의 별도 학술지 게재 확인 못 함. [원문 또는 공식 목록](https://arxiv.org/abs/2502.20693v1). 접근일 2026-10-11. 원문 열람(인용 관련 본문).
[^n4]: A3, ANSI/A3 R15.08-3-2026, Part 3: Use of IMR Applications, Published April 23,2026,77 pages. [원문 또는 공식 목록](https://www.automate.org/store/products/ansi-a3-r15-08-3-2026-american-national-standard-for-industrial-mobile-robots-safety-requirements-part-3-use-of-imr-applications-pdf-download). 접근일 2026-10-11. 원문 미열람(공식 목록만 열람).
[^n5]: ISO/DIS 3691-4, Edition 3, 개발 중. open 시 현재 단계40.60; 40.60 진입2026-09-10, 새 표준 발행 아님. [원문 또는 공식 목록](https://www.iso.org/standard/88615.html). 접근일 2026-10-11. 원문 미열람(공식 목록만 열람).
[^n6]: ISO/DIS12100.3, Edition2, 개발 중. open 시40.60. 40.60 진입2026-09-15. 2026-06-29 새DIS투표결정, 2026-07-20 투표시작. [원문 또는 공식 목록](https://www.iso.org/standard/88578.html). 접근일 2026-10-11. 원문 미열람(공식 목록만 열람).
[^n7]: 한국표준협회/국가기술표준원, KS B7327 산업용 이동 머니퓰레이터의 응용을 위한 안전 요구사항,2024-11-01,고시2024-0480,61쪽. [원문 또는 공식 목록](https://www.kssn.net/search/stddetail.do?itemNo=K001010149365). 접근일 2026-10-11. 원문 미열람(공식 목록만 열람).
[^n8]: 한국표준협회/국가기술표준원,KS B ISO3691-4 산업용 트럭 — 안전 요구사항과 검증 — 제4부: 무인 산업용 트럭과 시스템,2026-09-14,고시2026-0288,ISO3691-4:2023(IDT). [원문 또는 공식 목록](https://www.kssn.net/search/stddetail.do?itemNo=K001010158178). 접근일 2026-10-11. 원문 미열람(공식 목록만 열람).
[^n9]: 고용노동부, 사업장 위험성평가에 관한 지침,고시2024-76,2024-12-18,시행2025-01-02. [원문 또는 공식 목록](https://www.law.go.kr/LSW/admRulLsInfoR.do?admRulSeq=2100000251014&joTpYn=Y&languageType=KO&chrClsCd=010202). 접근일 2026-10-11. 원문 열람(인용 관련 본문).
[^n10]: 고용노동부 공고2026-461, 사업장 위험성평가에 관한 지침 전부개정고시(안) 행정예고,2026-09-23,의견마감2026-10-13. [원문 또는 공식 목록](https://moel.go.kr/info/lawinfo/lawmaking/view.do?bbs_seq=20260900747). 접근일 2026-10-11. 원문 열람(인용 관련 본문).
[^n11]: 고용노동부, 위험성평가 근로자 참여 가이드,표지2024-12,게시2024-12-31,12PDF쪽. [원문 또는 공식 목록](https://www.moel.go.kr/policy/policydata/view.do?bbs_seq=20241202175). 접근일 2026-10-11. 원문 열람(인용 관련 본문).
[^n12]: VDA/VDMA, Interface for the Communication between Mobile Robots and a Fleet Control,VDA5050 3.0.0,2026-03. [원문 또는 공식 목록](https://github.com/VDA5050/VDA5050/blob/3.0.0/VDA5050_EN.md). 접근일 2026-10-11. 원문 열람(인용 관련 본문).
[^n13]: Nav2, nav2_collision_monitor README,tag1.5.2,commit7b9be248a652224a19305469fd5e854d50512341,발행일 미확인. [원문 또는 공식 목록](https://github.com/ros-navigation/navigation2/blob/1.5.2/nav2_collision_monitor/README.md). 접근일 2026-10-11. 원문 열람(인용 관련 본문).
[^n14]: OMRON Robotics and Safety Technologies, Mobile Robot LD Safety Guide,I616-E-06/18393-000 RevH,개정이력October2019. [원문 또는 공식 목록](https://files.omron.eu/downloads/latest/manual/en/i616_mobile_robot_ld_safety_guide_system_manual_en.pdf?v=1). 접근일 2026-10-11. 원문 열람(인용 관련 본문).
[^n15]: TanJunKiat, Open-RMF issue658 Fire alarm separation for different fleets,2025-04-04. [원문 또는 공식 목록](https://github.com/open-rmf/rmf/issues/658). 접근일 2026-10-11. 원문 열람(인용 관련 본문).
[^n16]: Open-RMF rmf_ros2 FleetUpdateHandle,tag2.14.0,commit7f7b247a618c22f76bf01ff0fb393f72317f6d9a. [원문 또는 공식 목록](https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/src/rmf_fleet_adapter/agv/FleetUpdateHandle.cpp). 접근일 2026-10-11. 원문 열람(인용 관련 본문).
[^n17]: Open-RMF rmf_fleet_adapter CHANGELOG,tag2.14.0,표시일2026-09-26. [원문 또는 공식 목록](https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/CHANGELOG.rst). 접근일 2026-10-11. 원문 열람(인용 관련 본문).
[^n18]: EU Regulation2023/1230,원법2023-06-14,통합본2026-07-27,CELEX02023R1230. [원문 또는 공식 목록](https://eur-lex.europa.eu/eli/reg/2023/1230/2026-07-27/eng/pdf). 접근일 2026-10-11. 원문 열람(인용 관련 본문).
[^n19]: Ike Obi,Vishnunandan L.N. Venkatesh,Weizheng Wang,Ruiqi Wang,Dayoon Suh,Temitope I. Amosa,Wonse Jo,Byung-Cheol Min,Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems,arXiv2604.05427v1,2026-04-07, DOI10.48550/arXiv.2604.05427,게재지 미확인. [원문 또는 공식 목록](https://arxiv.org/abs/2604.05427v1). 접근일 2026-10-11. 원문 열람(인용 관련 본문).
[^n20]: Ivan Perez,Anastasia Mavridou,Tom Pressburger,Alexander Will,Patrick J. Martin,Monitoring ROS2: from Requirements to Autonomous Robots,arXiv2209.14030v1,2022-09-28,Formal Methods for Autonomous Systems and Automated and verifiable Software sYstem DEvelopment, EPTCS371 pp208–216. DOI10.4204/EPTCS.371.15. [원문 또는 공식 목록](https://arxiv.org/abs/2209.14030v1). 접근일 2026-10-11. 원문 열람(인용 관련 본문).

## 부록 A. 1단계 진단표와 조사 질문

### M-48 1단계 진단 — 2026-10-11

검색 전에 `04_M-48_prompt.md`, 대상 위키 본문과 링크된 절 분리6개를 끝까지 읽었다. 본문 version3 표시갱신2026-09-26이며2026-09-28리스트업 문구도있다. 2026-09-25의7절과2026-09-26의재검증7절 모두읽었고 같은문장을 별도주장으로중복집계하지않는다. 원문 HTML/txt는이폴더에보존. 이단계는진단이며아직검색결론을내리지않았다.

#### 약한 주장 목록
원문전체는각보존본에있다. 아래는저작물의장문을반복전재하지않고짧은원문구절과문장주제를식별한다.

|위치|원문 구절/식별|약한 이유·확인 대상|
|---|---|---|
|본문3·분리3|시스템수준위험성평가 대상 “되는 것으로 보인다”|차량·통합범위와ROP법적책임을추론; 규범본문/통합자설명필요|
|본문4·분리6|ISO12100 위험성평가·3단계|카탈로그근거/본문미열람. 정확한순서·잔류위험근거|
|본문4·분리7|ISO3691-4 운용구역 부속서A|범위소개로세부요구사실화한것인지점검|
|본문4·분리6|VDA safetyState·fieldViolation|추정.3.0.0고정명세와폐기·변경필드확인|
|본문4·분리7|ISO10218-2:2025 협동적용통합|A3FAQ/ISO목록본문미열람.대부분vs전체차이|
|본문4·8·분리6·8|STPA 다중로봇|논문본문미열람인데사실태그, 실험환경·방법·범위확인|
|본문5 피킹시나리오 시작/수행|작업자진입·안전보고·업무보류|가상시나리오추정; 안전기능vs업무요청구별|
|본문5 피킹 제약/완료|자동모드복귀·stopPause로재개|보호정지해제와업무pause해제를같은순서로간주하는위험|
|본문5 피킹 예외|업무보류·재배정|설계의견으로분리필요, 물리정지해제조건의공식근거없음|
|본문5 화재|기능요청의로봇주차|2025이슈본문미열람인데사실; 실제고정코드추적|
|본문5 화재 제약|플릿구분불리언 “이후 구현 여부는 미확인”|이슈일자이후PR·구현·변경기록필요|
|본문5 화재 제약|긴급작업우선교통협상|일반교통우선순위를화재안전기능으로옮길수있는지한계|
|본문6 대표접근|위험평가·상태전달·실행전필터|분류자체추정. 각각의안전보장범위구별필요|
|본문7·분리7|대부분 “본문은 열람하지 않았다”|표준목록과본문신뢰수준분리|
|본문8·분리8|Bensaci2018·STPA/SPN2023|서지·원문·제어구조·물류전용가능성확인|
|분리6·8|Belzile2025현장전문가검증|저자보고추정.검증이실물안전성시험인지방법검토인지|
|분리6·8|SafeGate230작업·30AI2THOR·실로봇|프리프린트판·방법·평가분모/누락·논문한계확인|
|본문9|안전상태수집·재개·제조사안전기능|전체책임행추정.산업현장통합자/사용자·안전성입증경계|
|본문9|ROP는안전기능을대신하지않음|VDA의비안전규격성질에서개별제품안전아키텍처역할을일반화하지않기|
|본문10|ISO10218사이버보안·안전연결|다른영역연결로만유지;보안기술심화제외|
|분리3|규칙223조1.8m울타리와생략|2023-07-01판/미열람.현행조문·시행일·공식해설필요.법률적용추론금지|
|분리3·7|2024이동식협동로봇KS|보도자료표준번호미확인;원고시와목록범위확인|
|분리7(09-25)|R15.08 Part3예정|진행·발행상태최근1년확인필수|
|분리7(09-26)|KS10218·15066구판가능성|검색미발견을부재로단정하지않음|
|분리7(09-26)|ISO/CD3691-4초안|현재프로젝트단계·차기판지위확인,2023발행본과분리|
|분리7(09-26)|ISO12100 DIS/DIN2025·Intertek2026전망|규범기관상태와시험기관예측구별,예측을완료로쓰지않음|
|분리7(09-26)|ISO15066유효·AWI15066-1|최신상태확인만필요;생체접촉수치심화는M49범위|

#### 1~13절 공백
|절|진단|
|---|---|
|1|범위정의충분.정의개작안함|
|2|복합상호작용위험질문있음.분석산출물·수용기준공백|
|3|국내법과표준책임분담소개,법조문구판·추정많음|
|4|상태메시지와안전기능·안전상태·업무일시정지구분부족|
|5|물류가상2사례.실물현장평가·위험등록부·안전검증방법공백|
|6|STPA·표준·SafeGate있으나실제절차·구현한계/비교공백|
|7|미열람규격많고최근재검증도목록·전망기반|
|8|논문조건·원문·재현/비교·장애한계공백|
|9|제조사·통합자·사용자책임이추정.변경후재평가누가하는지공백|
|10|다른영역연결충분.그영역의조사를미리하지않음|
|11|oq064/070/092/093+신규3.답변기준필요|
|12|2026-09-26월간재검증.지난1년실제변경확인|
|13|원문미열람·main링크·발행일미확인.고정판/정확서지필요|

#### 열린 질문
질문전문은2026-09-25-area25-s11.txt의3.본문에보존되어있다. 다음은원문id와식별요약이다.
|id|질문 식별|대응|
|---|---|---|
|oq-064|R15.08-2 TypeC통합요구와국내KS/인증|Q2·Q3|
|oq-070|2024-11이동식협동로봇KS번호·ISO10218/3691대응|Q3|
|oq-092|펌웨어·안전파라미터변경후국내재심사공식규정|Q7|
|oq-093|EU실질적변경과오케스트레이션정책·어댑터업데이트|Q7(조문·공식해설까지만)|
|신규1|VDA원격비상정지/플릿일괄정지의PL요구|Q5|
|신규2|혼합현장시스템수준RA수행·갱신주체|Q1·Q2·Q4|
|신규3|규칙223울타리생략의AMR플릿적용|Q3·Q4(적용법률해석안함)|

#### 2025년 이전 정보 후보
ISO12100:2010, ISO3691-4:2023, R15.08-2:2023, ISO/TS15066:2016/확인2022, KSBISO/TS15066제정2017/확인2022, KS10218-2확인2017, 규칙223시행2023-07-01, 이동식협동로봇2024-11발표, STPA2018·STPA/SPN2023. 폐지·개정과현재유효·적용판을별도로확인한다.

#### 조사 질문과 답변 기준
|번호|질문|답한 것으로 볼 기준|
|---|---|---|
|Q1|플릿의정상구성요소상호작용위험을STPA·FMEA/평가체계로어떻게찾고산출물을남기는가?|원문방법단계·제어구조·위험시나리오·안전제약·검증조건을추적하고다중로봇사례와한계확인|
|Q2|통합자·사용자·차량안전의경계와ISO12100/3691-4/R15.08후속파트의현재상태는?|발행기관판·개정단계·범위/책임의공식원문,2025-10~2026-10변경확정|
|Q3|국내이동식협동로봇KS번호·범위·현행국내부합표준은?|KATS공고·e나라목록과가능한본문에서번호·시행/발행일·범위확인,국외규격과표제만으로동일성추정안함|
|Q4|국내사업장위험성평가의현행수행·갱신·근로자참여요구는?|법령·고시현행조문과공식가이드에서단계·수시평가트리거·최근개정확인;사업자별적용법률판단안함|
|Q5|VDA정지/재개·ROS감시기능의실제계약과안전보장한계는?|고정명세·코드·개발문서에서업무pause와안전정지·재개조건구별;PL/안전인증주장은공식근거없으면보류|
|Q6|RMF화재대응의플릿선택·주차·재개동작은이슈이후어떻게변했는가?|이슈→PR→고정코드·변경기록대조,실제요청스키마·대상조건·복구의한계확인|
|Q7|펌웨어·정책·어댑터변경시위험재평가/재검증의공식조건은?|국내공식심사규정·EU원문/공식해설·제조사매뉴얼에서명시트리거확인;개별ROP업데이트법률분류추정안함|
|Q8|실행전안전게이트·런타임모니터의검증가능범위는?|SafeGate등원문판·평가분모·실물vs시뮬레이션·실패/인증한계및공개코드확인;일반LLM연구심화제외|

2단계는질문마다표준/학술/구현/국내/반대한계등최소3관점별개검색,중복제거후5후보이상. 검색이끝나기전원문근거결론을작성하지않는다.


## 부록 B. 검색 기록

### M-48 2단계 검색 기록
검색일 2026-10-11. 건진 수는 후보 목록에 채택한 서로 다른 문서 수다. 무관 검색 결과·미러는 제외하며 0도 기록했다. 같은 문서를 재발견한 검색은 동일 ID로 표시한다. 검색 출력 원문은 search-Q*.json에 보존했다.
|관점|검색어|날짜|건진 출처 수|ID|
|---|---|---|---:|---|
|Q1a 방법론|STPA handbook multi robot system risk analysis control structure MIT|2026-10-11|3|C01,C04,C05|
|Q1b 학술|"multi-mobile robots" "STPA" "SPN"|2026-10-11|1|C02|
|Q1c 현장·한계|"From Safety Standards to Safe Operation" risk deployment limitations|2026-10-11|1|C03|
|Q2a 표준기관|site.automate.org "R15.08-3" 2026|2026-10-11|1|C06|
|Q2b 표준 개정|site.iso.org "3691-4" "12100" 2026|2026-10-11|2|C07,C08|
|Q2c 통합자 책임|site.automate.org "R15.08-2" integrator user risk assessment|2026-10-11|1|C10|
|Q2d ③ 학술·통합 위험|industrial mobile robot system integration safety risk assessment R15.08 research|2026-10-11|1|C11|
|Q2e ⑥ 개정 전망 검증|ISO 12100 revision 2026 FDIS status|2026-10-11|2|C09,C12|
|Q3a ⑤ 국내 표준|site.kats.go.kr 이동식 협동로봇 2024 11 표준 KS|2026-10-11|1|C15|
|Q3b ① 표준 목록|"이동식 협동로봇" "KS" 안전 요구사항|2026-10-11|2|C13,C16|
|Q3c ④ 산업·현장|"mobile collaborative robot" "Korea" "standard" 2025|2026-10-11|0|없음|
|Q3d ① 표준 번호·부합화|"KS B 7327" 안전|2026-10-11|2|C14,C17|
|Q3e ③ 학술·국내 표준 한계|"이동식 협동로봇" "안전" "논문"|2026-10-11|0|없음|
|Q4a ① 법령|site.law.go.kr 사업장 위험성평가에 관한 지침 2026|2026-10-11|1|C18|
|Q4b ⑤ 국내 공식 가이드|site.moel.go.kr 위험성평가 2026 근로자 참여 수시 평가|2026-10-11|2|C19,C20|
|Q4c ⑥ 한계·개선|site.kosha.or.kr 위험성평가 실효성 근로자 참여 변경 작업|2026-10-11|1|C21|
|Q4d ③ 학술·실효성|"위험성평가" "근로자 참여" "실효성" 논문|2026-10-11|1|C22|
|Q5a ① 인터페이스 규격|site.vda5050.org OR site.github.com/VDA5050 "3.0.0" "safety"|2026-10-11|1|C23|
|Q5b ② 공개 구현|site.docs.nav2.org collision monitor safety certification|2026-10-11|2|C25,C26|
|Q5c ⑥ 재개·안전 한계|VDA 5050 stopPause emergency stop safety protocol limitations|2026-10-11|1|C24|
|Q5d ④ 제조사 안전 책임|site.omron.com mobile robot safety pause restart risk assessment manual|2026-10-11|1|C27|
|Q6a ② 구현·변경 이력|site.github.com/open-rmf fire emergency fleet 658|2026-10-11|1|C29|
|Q6b ④ 배치·산업 통합|Open RMF fire alarm emergency parking fleet integration|2026-10-11|3|C29,C30,C31|
|Q6c ⑥ 미해결·실패|site.github.com/open-rmf fire emergency resume issue fleet|2026-10-11|2|C28,C42|
|Q6d ④ 산업·비상운영 사례|"robot" "fire alarm" "fleet" "hospital"|2026-10-11|1|C32|
|Q7a ① 법령|site.eur-lex.europa.eu 2023/1230 substantial modification software safety|2026-10-11|1|C33|
|Q7b ⑤ 국내 공식 심사|site.kosha.or.kr 협동로봇 설치 작업장 안전인증 변경 재심사 소프트웨어|2026-10-11|1|C34|
|Q7c ④ 제조사 변경 통제|site.mobile-industrial-robots.com software update risk assessment safety manual|2026-10-11|2|C35,C36|
|Q7d ① 국내 심사 규정|"협동로봇" "재심사" 안전인증|2026-10-11|0|없음|
|Q8a ③ 학술|"SafeGate" "2604.05427"|2026-10-11|0|없음|
|Q8b ② 공개 구현|SafeGate embodied robot safety gate github|2026-10-11|1|C37|
|Q8c ⑥ 검증 한계|runtime assurance mobile robots safety monitor limitations formal verification|2026-10-11|3|C38,C39,C40|
|Q8d ① 안전 검증 지침|site.nasa.gov runtime assurance robot verification safety|2026-10-11|1|C41|
|Q8e ② 저자 공개 구현|"SafeGate" "Obi" "github"|2026-10-11|0|없음|

관점 확인: Q1 방법론·다중로봇 학술·배치 한계; Q2 발행기관·통합 범위·학술·개정 전망 반증; Q3 국내 발표·표준 목록·산업 구현(영어 최초 검색과 학술 탐색은 0건); Q4 조문·국내 안내·실효성/학술; Q5 규격·공개 구현·제조사/재개 한계; Q6 코드·배치 사례·실패 이슈; Q7 법령·국내 심사·제조사 변경관리; Q8 학술·공개 구현 탐색·검증 한계 및 공공 연구. 검색 관점의 다양성과 출처의 기관 독립성은 별도로 평가한다.
최근 1년 후보: R15.08-3-2026, ISO DIS3691-4/12100.3 단계, 2026-09 위험성평가 행정예고. 3단계에서 날짜·지위를 확인하기 전 결론으로 사용하지 않는다.

#### 3단계 원문 추적·서지 보완 검색(4회)
|관점|검색어|날짜|건진 관련 문서 수|후보 및 처리|
|---|---|---|---:|---|
|③ 원문 추적|"Collision hazard modeling" "Bensaci" pdf|2026-10-11|1|C02 동일논문재발견,새독립본문없음|
|③ 원문 추적|"STPA and Bowtie" pdf|2026-10-11|1|C04 동일논문NTNU링크,NVA이동으로본문미확보|
|① 국내 부합표준|"KS B ISO 3691-4" "2026"|2026-10-11|1|C43 추가후보1개,공식목록열람|
|③ 출판 이력|"From Safety Standards to Safe Operation" "2021"|2026-10-11|1|C03 2021워크숍판확보,같은연구서지보완|

누적검색38회(2단계34회+3단계보완4회). 같은문서의재발견은신규출처로중복집계하지않는다.

#### 재개 후 원문 추적(2회)
|관점|검색어|날짜|건진 수|처리|
|---|---|---|---:|---|
|③ 학술 원문|"STPA and Bowtie risk analysis" "pdf" Bensaci|2026-10-11|1|C04 공개 본문 ResearchGate에서 후속 열람 성공|
|③ 학술 원문|"Collision hazard modeling" "109138" repository|2026-10-11|1|C02 동일 출판사 자료; 새 본문 없음|
누적40검색, 후보43개. URL 직접 열기/다운로드는 검색횟수에 중복 계산하지 않음.

## 부록 C. 출처 평가표

### M-48 3단계 출처 평가표 — 완료

접근일2026-10-11. 후보43개 전부 원문 URL 열람을 시도했다. 관련 본문 열람은 인용할 절을 직접 읽었다는 뜻이며 문서 전체 정독과 다르다. 최종20개 중15개 관련 본문 열람(75%),5개 공식 표준 목록만 열람. 미열람 표준의 내용은 범위·판·발행/개발 지위로 제한한다. 아래 미확인 서지가 남은 비채택 자료는 결론에 사용하지 않았다.

|ID|서지·판·발행일|열람 상태·근거|구분·독립 계열|신뢰도·채택 판단|최종 사용|
|---|---|---|---|---|---|
|C01|Nancy G. Leveson, John P. Thomas, STPA Handbook, March 2018, DOI 없음|관련 본문 열람. C01.pdf/txt, PDF 14~15·36·42쪽 등. 웹 타임아웃 뒤 curl 성공|1차 방법 저자, MIT STAMP|high: 방법 절차. 플릿 실험의 효과 근거는 아님|채택 n1|
|C02|Chaima Bensaci, Youcef Zennir, Denis Pomorski, Fares Innal, Mary Ann Lundteigen, Collision hazard modeling and analysis in a multi-mobile robots system transportation task with STPA and SPN, RESS 234(2023)109138, DOI 10.1016/j.ress.2023.109138. 서지는 검색 단계 확인|열람 실패: ScienceDirect 403. 다른 공개 본문 미확보|1차 논문 후보, C04와 같은 연구 계열|본문 신뢰도 평가 불가. 결론 근거 제외|제외: 범위/중복/미열람 또는 미확인; 주장근거로 사용 안 함|
|C03|Bruno Belzile, Tatiana Wanang-Siyapdjie, Sina Karimi, Rafael Gomes Braga, Ivanka Iordanova, David St-Onge, From Safety Standards to Safe Operation with Mobile Robotic Systems Deployment, arXiv:2502.20693v1, 2025-02-28. DOI10.48550/arXiv.2502.20693. 동일 제목 ICAR2021 Workshop on Design, Learning, and control for safe human-robot collaboration,2021-12-07 별도 확보;2025판의 별도 학술지 게재 확인 못 함|관련 본문 열람. C03.pdf/txt PDF 3~7쪽, 부록 9~10쪽. C03-2021.pdf/txt 표지에서 ICAR workshop 2021-12-07 확인|1차, ÉTS/Pomerleau. 두 판은 독립 아님|medium: 실물 현장 맥락의 위험평가 사례이며 사고율 개선 실험으로 해석 금지. 2025 업로드판과 2021 워크숍판을 구별; 동일내용/전체판차이를 확정하지 않음|채택 n3|
|C04|Chaima Bensaci, Youcef Zennir, Denis Pomorski, Fares Innal, Yiliu Liu, Cherif Tolba. STPA and Bowtie risk analysis study for centralized and hierarchical control architectures comparison. Alexandria Engineering Journal 59(5),3799–3816,2020. 공개 early article 판은 2020-06-21 채택, 공개목록 July2020; 정확 온라인 발행일 미확인. DOI10.1016/j.aej.2020.06.036|원문 열람: 출판사403 뒤 ResearchGate 공개 논문 본문 성공. C04-case.txt §2~3; C04-sections.txt §4~6·표3~4. PDF 다운로드는 실패, 논문 전체텍스트의 관련절 직접 열람|1차 논문 저자 원문, Bensaci 계열(C02와 비독립)|medium: 11로봇 화학실험실 제어구조의 분석 사례. 현장 사고율 측정·중앙제어 일반열위로 확대 금지. Bowtie의 정량 구별 한계 명시|채택 n2|
|C05|Dro J. Gregorian, Sam M. Yoo, A System-Theoretic Approach to Risk Analysis, MIT MS Engineering and Management thesis, June 2021|PDF 확보, 표지·목차 확인. 핵심 방법/한계 본문 평가는 미완료|1차 학위논문, MIT/Nancy Leveson 계열 C01과 비독립|미평가. 최종 인용 전 관련 절 열람 필요|제외: 범위/중복/미열람 또는 미확인; 주장근거로 사용 안 함|
|C06|A3, ANSI/A3 R15.08-3-2026, Part 3: Use of IMR Applications, Published April 23,2026,77 pages|원문 미열람(공식 판매 목록만). open-C06 L260~263|1차 목록, A3; C10과 비독립|high: 발행일·표제·공식 범위만. 세부 shall 요구 금지|채택 n4|
|C07|ISO/DIS 3691-4, Edition 3, 개발 중. open 시 현재 단계40.60; 40.60 진입2026-09-10, 새 표준 발행 아님|원문 미열람(공식 목록·개발 이력만). open-C07|1차 목록, ISO/TC110|high: 개발 지위만. CD/발행본과 혼동 금지|채택 n5|
|C08|ISO3691-4:2023, Edition2,2023-06,발행 이력2023-06-12|원문 미열람(공식 목록만). open-C08|1차 목록, C07과 같은 프로젝트|high: 판·범위·지위. 상세 부속서 본문 근거 아님|제외: 범위/중복/미열람 또는 미확인; 주장근거로 사용 안 함|
|C09|ISO/DIS12100.3, Edition2, 개발 중. open 시40.60. 40.60 진입2026-09-15. 2026-06-29 새DIS투표결정, 2026-07-20 투표시작|원문 미열람(공식 목록·개발 이력). open-C09 L133~143|1차 목록, ISO/TC199; C12는 같은 개정 사안 논평|high: 지위만. 2026 FDIS 전망을 발행 사실로 쓰지 않음|채택 n6|
|C10|A3, ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available,2023-10-10|공식 발표 관련 본문 열람. open-C10 L6~32. 표준 본문 미열람|1차 발표, A3 C06과 비독립|high: 공식 발표 범위. 세부 규범 근거로 확대 금지|제외: 범위/중복/미열람 또는 미확인; 주장근거로 사용 안 함|
|C11|Samuel Kangwagye, Mazin Hamad, Alessandro De Toni, Vasilije Rakcevic, Valentin Le Mesle, Achim J. Lilienthal, Sami Haddadin. ANSI/RIA R15.08-1/2 and ANSI/A3 R15.08-2 Compliant Safety-Oriented Software Components for Industrial Mobile Robots, IEEE/SICE SII2026 pp948–955, DOI10.1109/SII64115.2026.11404583|원문 미열람(대학 서지·초록). open-C11|1차 논문 후보, TUM/협력기관|실험 주장 채택 불가. 정확 발행 월일 미확인|제외: 범위/중복/미열람 또는 미확인; 주장근거로 사용 안 함|
|C12|CEN-CENELEC newsletter/ETUC, Revision of EN ISO12100 ‘Safety of Machinery’ Reaches Critical Stage,2026-03-31|원문 본문 열람. open-C12 L25~35|1차 참여자 논평, 개정 프로젝트는 C09와 겹침|medium: 협상 경과/당사자 시각. 현재 표준 지위는 ISO 목록 우선|제외: 범위/중복/미열람 또는 미확인; 주장근거로 사용 안 함|
|C13|대구광역시, 「대구 이동식 협동로봇 규제자유특구」 산업표준 제정으로, 글로벌 자율제조 도시 기반 마련. 2024-11-04|관련 본문 열람. open-C13, KS번호와 주요내용. 날짜/본문 전체 재대조 남음|1차 실증사업 발표, C16과 동일 사업|high: 발표 내용. 사업 성과의 독립 검증 아님|제외: 범위/중복/미열람 또는 미확인; 주장근거로 사용 안 함|
|C14|한국표준협회/국가기술표준원, KS B7327 산업용 이동 머니퓰레이터의 응용을 위한 안전 요구사항,2024-11-01,고시2024-0480,61쪽|원문 미열람(공식 목록만). open-C14 L208~243|1차 목록, KS|high: 번호·범위. 관제/군집관리 제외 문구 중요. 인용표준 목록을 제정 당시 판으로 오인하지 않음|채택 n7|
|C15|KS B7313 산업용 협동 로봇, 정확 판·발행일 재대조 필요|원문 미열람(목록). open-C15|1차 목록, KS|목록 서지 추가 확인 필요. M49 범위 심화 제외|제외: 범위/중복/미열람 또는 미확인; 주장근거로 사용 안 함|
|C16|중소벤처기업부, 특구 시행령 개정 보도자료 bcIdx1069234,2026년 발표(정확 표제·게시일 재대조 필요)|관련 본문 열람. open-C16 L439~440 등|1차 사업 발표, C13과 비독립|medium: 사업 홍보의 수치·성과는 독립 검증 아님. 최종 포함 여부 미정|제외: 범위/중복/미열람 또는 미확인; 주장근거로 사용 안 함|
|C17|Safetics, FAQ / SafetyDesigner Collision Risk Analysis,발행일 미확인|관련 FAQ 원문 열람. open-C17 L72~79 등|1차 벤더 설명, Safetics|medium: 제품 주장으로 한정하고 [추정]. KS 공식 요구·인증 효력의 증거 아님|제외: 범위/중복/미열람 또는 미확인; 주장근거로 사용 안 함|
|C18|고용노동부, 사업장 위험성평가에 관한 지침,고시2024-76,2024-12-18,시행2025-01-02|원문 관련 조문 열람. C18-body.html/txt, 제5~15조. 최초 웹은 껍데기였으나 공개 본문 endpoint로 확보|1차 행정규칙, 고용노동부|high: 현행 snapshot 조문. 2026 상위법 변화와의 조합은 추가 확인하며 개별 사업장 법률 적용 판단 금지|채택 n9|
|C19|고용노동부 공고2026-461, 사업장 위험성평가에 관한 지침 전부개정고시(안) 행정예고,2026-09-23,의견마감2026-10-13|원문 열람. 공고·개정안 HWPX를 내려받아 XML 텍스트 추출. C19notice.txt 및 C19draft.txt|1차 공식 예고, C18과 같은 기관|high: 아직 예고안. 시행규정으로 쓰지 않음. 개정안 상세 조문 대조 남음|채택 n10|
|C20|고용노동부, 위험성평가 근로자 참여 가이드,표지2024-12,게시2024-12-31,12PDF쪽|원문 열람: PDF12쪽 전체 텍스트, 인쇄6쪽 수급업체 청취,7쪽 QR/문자 익명제안,9쪽 체크리스트. C20.pdf/txt|1차 공식 가이드, C18~19와 같은 정책 계열|high: 참여 방식 사례 소개에 한정. 사고감소 효과의 독립 평가 아님|채택 n11|
|C21|KOSHA, 위험성평가 이행·점검 매뉴얼,검색에2023-안전보건평가실 표시. 정확 서지 미확인|열람 실패. web0행, curl은 포털 HTML(C21.download), PDF 아님|1차 후보, KOSHA/MOEL 정책 계열|본문 근거 제외|제외: 범위/중복/미열람 또는 미확인; 주장근거로 사용 안 함|
|C22|안태령·고왕열·곽대훈, 소규모 외주공사의 위험성평가 운영실태 분석 및 개선방안에 관한 연구,안전문화연구57,355–372,2026,DOI10.52902/kjsc.2026.57.355|원문 미열람(초록·KCI 서지). open-C22|1차 논문 후보, 충남대/우송정보대|설문 수치·인과 주장 채택 불가. 로봇 플릿 직접 사례 아님|제외: 범위/중복/미열람 또는 미확인; 주장근거로 사용 안 함|
|C23|VDA/VDMA, Interface for the Communication between Mobile Robots and a Fleet Control,VDA5050 3.0.0,2026-03|관련 명세 원문 열람. C23.md,3.0.0 고정 태그. 명세1916~1918행 및 state.schema893~908행 activeEmergencyStop/MANUAL/REMOTE/NONE 대조|1차 명세, VDA프로젝트 C24와 비독립|high: 메시지 계약. 안전 표준/PL 보장 아님|채택 n12|
|C24|VDA5050, VDA5050 3.0.0 Discussion596/release,2026-03(정확 일자 재확인)|릴리스 관련 본문 열람. open-C24|1차 프로젝트 발표, C23과 비독립|high: 변경 안내. activeEmergenceStop 오타 가능하므로 실제 명세 이름 우선|제외: 범위/중복/미열람 또는 미확인; 주장근거로 사용 안 함|
|C25|Nav2, nav2_collision_monitor README,tag1.5.2,commit7b9be248a652224a19305469fd5e854d50512341,발행일 미확인|관련 원문 열람. C25.md,문서1~12행. Jazzy문서도 확보했으나 고정 코드판과 동일판으로 묶지 않음|1차 공개 구현, Nav2|high: CPU 구현/하드 실시간 안전 인증 미제공 설명. 모든 ROS2의 성질로 확대 금지|채택 n13|
|C26|Nav2 Jazzy, Collision Detector Node,발행일 미확인|관련 문서 원문 열람. open-C26 L496~497. 고정 소스 링크 추가 확인 필요|1차 공개 구현, C25와 비독립|high: 속도 영향 없이 상태를 발행하는 노드 계약|제외: 범위/중복/미열람 또는 미확인; 주장근거로 사용 안 함|
|C27|OMRON Robotics and Safety Technologies, Mobile Robot LD Safety Guide,I616-E-06/18393-000 RevH,개정이력October2019|관련 원문 열람. C27.pdf/txt PDF12,17~20쪽 등|1차 제조사 매뉴얼, OMRON|medium: LD제품·그 판의 사용자 책임/구성 지침. 벤더 주장은 [추정], 타사 플릿 일반화 금지|채택 n14|
|C28|TanJunKiat, Open-RMF issue658 Fire alarm separation for different fleets,2025-04-04|이슈 본문 열람. open-C28. 현재Open 표시는 구현 부재 증거 아님|1차 사용자 문제제기, Open-RMF|medium: 보고 당시 현상. PR413 및 고정코드와 후속 대조 완료. 이슈상태를 구현부재로 인용하지 않음|채택 n15|
|C29|Open-RMF rmf_demos README,tag2.10.0,commit990e09220ed60af69cf0dac32b34312acb2244b1,발행일 미확인|web503 뒤 고정 원문 다운로드 성공. rmf_demos-README.md. 관련 본문 정독 남음|1차 공개 구현, Open-RMF|평가 미완료. tag2.10.0과 rmf_ros2 tag2.14.0을 호환 조합으로 단정 금지|제외: 범위/중복/미열람 또는 미확인; 주장근거로 사용 안 함|
|C30|Open-RMF rmf_ros2 FleetUpdateHandle,tag2.14.0,commit7f7b247a618c22f76bf01ff0fb393f72317f6d9a|원문 관련 함수 열람. FleetUpdateHandle.cpp1444~1465·hpp. 원 후보hpp는보조,실행cpp와 Node.cpp73~79행 구독 연결 확인. 단위 실행시험은 미수행|1차 코드, Open-RMF|high: 해당 commit의 필터 동작. 실행/배치 시험은 하지 않음|채택 n16|
|C31|Open-RMF rmf_fleet_adapter CHANGELOG,tag2.14.0,표시일2026-09-26|관련 변경 항목 열람. rmf-CHANGELOG.rst. PR413 merge2025-04-10T03:52:57Z,mergeSHA5f5462ac98f68b245de87a56b34c81a866861ec5|1차 변경 이력, C28~30과 비독립|high: 코드와 이력 연결. CHANGELOG100~111행 2.10.0(2025-05-09)절에 PR413 수록. 태그2.14.0은 확인판이지 도입판 아님|채택 n17|
|C32|AFRY, Revolutionising hospital logistics with autonomous mobile robots,발행일 미확인|원문 본문 열람. open-C32 L15~44|1차 벤더 사례, AFRY/OMRON|medium: 노르웨이 병원·15AMR·계획완료mid2025. 실현 완료/안전인증으로 확대 금지|제외: 범위/중복/미열람 또는 미확인; 주장근거로 사용 안 함|
|C33|EU Regulation2023/1230,원법2023-06-14,통합본2026-07-27,CELEX02023R1230|관련 원문 조문 열람. C33.pdf/txt PDF6(3조16호),24(18조),51~52(54조). 통합본 자체는 문서 참고본임을 표지에 명시|1차 법령 통합자료, EU|high: 정의/조문·적용일. 일반 적용2027-01-20,예외 별도. 개별 ROP 업데이트가 실질적 변경인지 판정 금지|채택 n18|
|C34|산업안전보건인증원, 안전인증 심사 종류 및 절차,발행일 미확인|웹 타임아웃 후 curl HTML 확보. C34.html/txt. 협동로봇 설치 후 소프트웨어 변경 재심사 요건은 아직 찾지 못함|1차 기관 안내,KOSHA|일반 절차와 특정 인증 제도 구별 필요. 질문 답변 근거 미확정|제외: 범위/중복/미열람 또는 미확인; 주장근거로 사용 안 함|
|C35|MiR600 User Guide2.0,미러 제공자Jugard+Kuenstner,정확 발행일 미확인|열람 실패: 웹 접근불가,curl은 일반HTML(C35.pdf). 원문PDF 아님|1차 매뉴얼 후보,MiR C36과 비독립|본문 근거 제외|제외: 범위/중복/미열람 또는 미확인; 주장근거로 사용 안 함|
|C36|MiR, Security Advisories,발행일 미확인|원문 목록의 안내 본문 열람. open-C36 L42~48|1차 벤더,MiR|medium: 개별 CVE 본문은 미열람. 보안 갱신 권고를 안전 재인증 의무로 치환 금지|제외: 범위/중복/미열람 또는 미확인; 주장근거로 사용 안 함|
|C37|Ike Obi,Vishnunandan L.N. Venkatesh,Weizheng Wang,Ruiqi Wang,Dayoon Suh,Temitope I. Amosa,Wonse Jo,Byung-Cheol Min,Pre-Execution Safety Gate & Task Safety Contracts for LLM-Controlled Robot Systems,arXiv2604.05427v1,2026-04-07, DOI10.48550/arXiv.2604.05427,게재지 미확인|관련 본문 열람. C37.pdf/txt PDF3~8쪽. 8쪽논문,게재지 미확인|1차 프리프린트,Purdue SMART 등|medium: 평가 분모/정성 실로봇·합성명령 구별. 동명Github를 저자코드로 오인 금지|채택 n19|
|C38|Ankush Desai,Shromona Ghosh,Sanjit A. Seshia,Natarajan Shankar,Ashish Tiwari,Soter: Programming Safe Robotics System using Runtime Assurance,UCB/EECS-2018-127,2018-08-21|후보2019DSN DOI열람 실패. 별개 2018기술보고서 PDF 관련본문 열람: §1~3 RTA 세 요소/회복집합/전환주기 조건. 드론 사례|1차 보고서,Berkeley/SRI|2018원문을2019출판판 열람으로 세지 않음. 최종 제외: M48의 직접 다중로봇 분석 C04를 우선, 2019판을 열었다고 계산하지 않음|제외: 범위/중복/미열람 또는 미확인; 주장근거로 사용 안 함|
|C39|Ivan Perez,Anastasia Mavridou,Tom Pressburger,Alexander Will,Patrick J. Martin,Monitoring ROS2: from Requirements to Autonomous Robots,arXiv2209.14030v1,2022-09-28,Formal Methods for Autonomous Systems and Automated and verifiable Software sYstem DEvelopment, EPTCS371 pp208–216. DOI10.4204/EPTCS.371.15|관련 본문 열람. C39.pdf/txt PDF4~7쪽(인쇄211~214)|1차 논문,NASA Ames/KBR/VCU|high: 도구 구조/명시 한계. 모니터 C99 hard realtime과 ROS2 전체 안전 보증 구별|채택 n20|
|C40|Joakim Schack Betzer,Jalil Boudjadar,Mirgita Frasheri,Prasad Talasila,Digital Twin Enabled Runtime Verification for Autonomous Mobile Robots under Uncertainty,arXiv2412.09913v1,2024-12-13,게재지 미확인|관련 본문 열람. C40.pdf/txt PDF6~8쪽|1차 프리프린트,Aarhus|medium: TurtleBot3 Burger 속도추종/요가매트험로 실험. 플릿 충돌안전 실험 아님|제외: 범위/중복/미열람 또는 미확인; 주장근거로 사용 안 함|
|C41|J Tanner Slagel,Lauren M. White,Aaron Dutle,César A. Muñoz,Nicolas Crespo,A Verification Framework for Runtime Assurance of Autonomous UAS,NASA20240007986,DASC2024. 정확서지 추가확인|PDF 확보·표지만 확인. C41.pdf/txt. 관련 본문 평가 미완료|1차 연구,NASA Langley. C39와 NASA기관 중첩도 검토 필요|다중AMR직접근거아님. 범위상 제외 가능|제외: 범위/중복/미열람 또는 미확인; 주장근거로 사용 안 함|
|C42|Yadunund 외,Failover functionality for fleet adapters,rmf_ros2 issue100,2021-08-17|이슈 본문/토론 관련 부분 열람. open-C42|1차 프로젝트 이슈,Open-RMF|medium: 과거제안·Open표시만으로현재복구불가 단정금지. 최신코드추적 전 결론 제외|제외: 범위/중복/미열람 또는 미확인; 주장근거로 사용 안 함|
|C43|한국표준협회/국가기술표준원,KS B ISO3691-4 산업용 트럭 — 안전 요구사항과 검증 — 제4부: 무인 산업용 트럭과 시스템,2026-09-14,고시2026-0288,ISO3691-4:2023(IDT)|원문 미열람(공식 목록만). open-C43 L212~244. 3단계 보완검색S3에서 발견|1차 목록,KS/ISO부합화|high: 판·부합화만. 국제표준현재DIS와국내IDT발행본분리|채택 n8|

## 부록 D. 검증 기록

### M-48 5단계 자체 검증 기록

2026-10-11. **검증 전 전체 초안 `draft-stage4.md`를 작성한 뒤** 아래 검사를 수행했다. `verification-evidence-pass1.json`에 첫 재대조, `verification-evidence-final.json`에 최종 38개 근거를 보존했다. 새 사실 문장36개와 벤더 추정2개를 모두 검토했다. 원문 구절은 각 F-ID의 본문 근거 메모에 한 번만 인용한다.

#### 필수 9개 검사

|검사|수행·판정|
|---|---|
|1. 사실 재대조|F01~F38의 저장 원문을 다시 열고 구절·맥락을 확인했다. 사실36개 모두 직접 근거가 있다. PDF는 인용 쪽을 다시 추출하고, SafeGate 표/식은 7~8쪽 PNG로도 확인했다. 단어검색만으로 논리를 검증했다고 보지 않고 원문에서 주장 범위도 대조했다.|
|2. 추론 분리|ROP 설계 제안은 각 항목의 의견으로 분리했다. 논문 분석을 사고감소·인증 입증으로 확대하지 않았다. 열린질문 답변의 종합 판단은 추정으로 표시했다.|
|3. 수치·번호|11로봇은 논문 분석대상, 230은 합성 작업,30은 시뮬레이션으로 구별. RMF도입기록2.10.0과확인판2.14.0 구별. 실제변수명인용1곳·OMRON인쇄쪽2곳 수정. SafeGate CR/표II 분모는확인못함U10/U11 유지.|
|4. 서지|20개 채택 출처의 표제·저자/기관·판·날짜를 평가표와 원문에 재대조했다. 이슈 저자 TanJunKiat 확인. C03/C37/C39 arXiv v1 고정. C03의2021워크숍판과2025업로드구분; C04 공개early article과최종권호 구분; 확정하지못한월일/게재지는미확인 표시.|
|5. 표현 강도|국내고시의 실시/참여 의무와 공식가이드 사례를 구별. VDA의 shall not을 금지로, pauseAllowed의 조건을 유지. 제조사 설명2개는추정. 권고를 일반 법적 의무로 올리지 않았다.|
|6. 시행 상태|A3발행목록,ISO DIS개발단계,KS발행판,고시2024-76의판·시행일,2026행정예고,EU일반적용2027-01-20을구분. 고시안과ISO초안을시행/발행본으로쓰지않았다.|
|7. 독립성|기관·연구팀·프로젝트를 다시 묶었다. RMF3출처,MOEL3출처는같은계열. VDA문서/스키마도한프로젝트. 다른팀의다른시스템은동일주장재현으로계산하지않음. 독립교차확인0.|
|8. 중복|위키본문/분리6페이지와표제·식별자·URL을대조. 기존6출처는신규로세지않음. 단순STPA소개·일반위험평가소개는복제하지않고산출물/조건/검증경계에추가. Part3·ISO상태·RMF미구현후속을정정대상으로표시.|
|9. 범위|M48의플릿/시스템위험평가·운용/변경통제에집중. 생체접촉수치/인증절차/법률적용은심화하지않음. M49/M50의연구를미리하지않았다.|

#### 수정 이력

|항목|처음 태그 → 최종 태그|바꾼 이유|
|---|---|---|
|F32 근거 인용|사실 → 사실|초안 인용의 변수명 msg를 실제 고정 코드의 emergency_signal로 바로잡음. 조건·동작에 관한 본문 문장은 변경 없음.|
|F28 근거 위치|추정 → 추정|OMRON PDF17쪽의 인쇄쪽은16이 아니라17임을 다시 확인.|
|F29 근거 위치|추정 → 추정|OMRON PDF18쪽의 인쇄쪽은17이 아니라18임을 다시 확인.|
|F01/F12/F14/F25/F33/F34 근거 구절|사실 → 사실|주장의 여러 구성요소에 바로 연결되도록 짧은 발췌를 보강. 생략은 …로 표시. 내용·태그 변경 없음.|
|F06/F36 인용 문자열|사실 → 사실|다단 PDF의 layout추출은 열을 섞어 문자열검색이 실패했다. 인용한 같은쪽을 raw추출하여 구절 확인. 사실을 조정하지 않고 추출방식 교정.|
|F18 인용 문자열|사실 → 사실|raw추출은 한글 공백을 잃었다. 같은 PDF9쪽의 layout추출에서 구절을 확인.|
|출처 n12/n13 링크|태그 변경 없음|후보 URL이 남아 있던 main/Jazzy 링크를 실제 인용한3.0.0/1.5.2 고정 원문으로 수정.|
|그 밖의 사실 문장|사실 → 사실|원문·범위·판 조건이 초안과 일치. 변경 없음.|
|F28/F29 벤더 내용|추정 → 추정|처음부터 단일 벤더 설명으로 보수적으로 분류. 변경 없음.|
|SafeGate CR/표II 수치|미채택 → 미채택|초안 이전 분석에서 분모 공백을 발견해 성능 사실 주장에 넣지 않음. 태그 낮춤/검증본문수정으로 부풀리지 않음.|

**태그 낮춤0건, 검증에서 고친 본문 문장0개.** 별도로 근거 인용 오류1건과 위치 오류2건을 교정했다. 근거 보강·서지 고정·추출방식 개선을 본문 문장 수정으로 세지 않았다. 사실 문장의 근거를 못 찾았는데도 태그를 유지한 경우는 없다.

#### 첫 영역 대비 감시

|지표|F21 기준|M48|판정|
|---|---:|---:|---|
|보완|15|15|동일수, 품질기준 축소 없음|
|채택출처|20|20|모든43후보의접근·채택여부별도기록|
|원문열람|14/20=70%|15/20=75%|+5%p,유료목록5개는분자제외|
|독립교차주장|0|0|같은계열/다른대상자료를독립재현으로부풀리지않음|
|태그낮춤|1|0|낮춤목표치를맞추지않음;초안부터벤더추정·성능보류|
|검증본문수정|별도미집계|0|근거오류3건은별도공개|
|확인못함|11|14|U01~U14로명시,미해결을삭제하여수치를낮추지않음|

이전 완료 파일의 미집계 수치는 추정하지 않았다. 원문비율은 충족하지만 규격본문과 현장안전성의 증거 공백은 그대로 남는다.

### 주장별 재대조 결과

직접 인용은 본문 각 F-ID의 근거 메모를 참조한다. 아래는 저장된 원문을 다시 연 결과다.

|주장|처음→최종|원문 위치|재대조|
|---|---|---|---|
|F01|사실→사실|C01: PDF 14쪽, Chapter 2 Method Overview|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F02|사실→사실|C01: PDF 36쪽, Table 2.3 아래 네 유형|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F03|사실→사실|C04: 공개 논문 §3, 본문 7쪽; 열람 L749~755|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F04|사실→사실|C04: §3.1, §4.1~5.2; 열람 L807~851, L902~956|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F05|사실→사실|C04: §6 결론 마지막 문단, 본문 17쪽; L1969~1982|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F06|사실→사실|C03: PDF 5쪽 §4 Case Study|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F07|사실→사실|C03: PDF 7쪽 §4.3, Table 3 앞 문단|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F08|사실→사실|C06: 공식 목록 Published, 열람 L260~263|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F09|사실→사실|C07: 공식 목록 머리말 L15, General information|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F10|사실→사실|C07: Life cycle L182|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F11|사실→사실|C09: Life cycle L140~143|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F12|사실→사실|C14: 목록 L208~212|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F13|사실→사실|C14: 목록 적용범위 L228|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F14|사실→사실|C43: 목록 구매정보 L212~214, 상세정보 고시2026-0288|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F15|사실→사실|C18: 제5조제2항, 저장 본문 L46~49|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F16|사실→사실|C18: 제6조 각 호|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F17|사실→사실|C18: 제15조제2항 본문 및 제1~6호|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F18|사실→사실|C20: PDF 9쪽·인쇄6쪽 핵심 포인트|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F19|사실→사실|C20: PDF 10쪽·인쇄7쪽 사례1|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F20|사실→사실|C19: 공고 HWPX 첫머리 L1~6|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F21|사실→사실|C19: 공고 3. 의견제출 L39~40|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F22|사실→사실|C23: 범위 제외항목, 고정 명세 L135~136|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F23|사실→사실|C23: 고정 명세 actions 표 L701|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F24|사실→사실|C23: 고정 명세 actions 표 L702|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F25|사실→사실|C23: 고정 명세 L1916~1918; json_schemas/state.schema L893~908|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F26|사실→사실|C25: README L10|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F27|사실→사실|C39: PDF 7쪽·인쇄214쪽 §3 끝|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F28|추정→추정|C27: PDF/인쇄17쪽 Fleet 경고|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F29|추정→추정|C27: PDF/인쇄18쪽 PL and PFH 표 주석|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F30|사실→사실|C28: 이슈 본문 L160,168~174|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F31|사실→사실|C31: 2.14.0 고정 CHANGELOG L100~111|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F32|사실→사실|C30: FleetUpdateHandle.cpp L1444~1465; Node.cpp L73~79|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F33|사실→사실|C33: 2026-07-27 통합본 PDF 6쪽 Art.3(16)|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F34|사실→사실|C33: 같은 조항 Art.3(16)(a)~(b)|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F35|사실→사실|C33: 통합본 PDF 51~52쪽 Art.54|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F36|사실→사실|C37: PDF 6쪽 §V-A|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F37|사실→사실|C37: PDF 6쪽 §V 서두·§V-B|직접 구절·맥락 확인; 본문 내용 변경 없음|
|F38|사실→사실|C37: PDF 8쪽 §VI-C|직접 구절·맥락 확인; 본문 내용 변경 없음|

## 부록 E. 독립 검증 대조표

같은 내용을 직접 뒷받침하는 독립된 두 출처가 있어야 독립 교차 확인으로 센다. 동일 원문의 미러·판 차이, 같은 프로젝트의 코드와 변경 이력, 다른 제품의 유사한 제한은 그 기준을 충족하지 않는다.

|주장ID|직접 근거|비교한 자료·관계|독립 교차 확인 판정|
|---|---|---|---|
|F01|[^n1], 본문 인용 위치 참조|C04는 별도 연구팀의 방법 적용. 방법을 인용하는 관계이며 동일효과 독립재현 아님|불인정: 단독 근거/서로 다른 주장|
|F02|[^n1], 본문 인용 위치 참조|C04는 별도 연구팀의 방법 적용. 방법을 인용하는 관계이며 동일효과 독립재현 아님|불인정: 단독 근거/서로 다른 주장|
|F03|[^n2], 본문 인용 위치 참조|C01과 분석원리는 연결되나 11로봇 사례/평가결과는 C04 단독;C02 본문미열람|불인정: 단독 근거/서로 다른 주장|
|F04|[^n2], 본문 인용 위치 참조|C01과 분석원리는 연결되나 11로봇 사례/평가결과는 C04 단독;C02 본문미열람|불인정: 단독 근거/서로 다른 주장|
|F05|[^n2], 본문 인용 위치 참조|C01과 분석원리는 연결되나 11로봇 사례/평가결과는 C04 단독;C02 본문미열람|불인정: 단독 근거/서로 다른 주장|
|F06|[^n3], 본문 인용 위치 참조|2021워크숍판은 같은연구; C04는다른현장·다른방법/주장|불인정: 단독 근거/서로 다른 주장|
|F07|[^n3], 본문 인용 위치 참조|2021워크숍판은 같은연구; C04는다른현장·다른방법/주장|불인정: 단독 근거/서로 다른 주장|
|F08|[^n4], 본문 인용 위치 참조|C10은 같은A3·다른파트|불인정: 단독 근거/서로 다른 주장|
|F09|[^n5], 본문 인용 위치 참조|C08은 같은ISO 프로젝트의발행본;새DIS단계 확인은C07 단독|불인정: 단독 근거/서로 다른 주장|
|F10|[^n5], 본문 인용 위치 참조|C08은 같은ISO 프로젝트의발행본;새DIS단계 확인은C07 단독|불인정: 단독 근거/서로 다른 주장|
|F11|[^n6], 본문 인용 위치 참조|C12는 개정참여자논평;현재단계의독립원문증거로합산안함|불인정: 단독 근거/서로 다른 주장|
|F12|[^n7], 본문 인용 위치 참조|C13/C16은같은표준제정사업 발표;조항대응미확정|불인정: 단독 근거/서로 다른 주장|
|F13|[^n7], 본문 인용 위치 참조|C13/C16은같은표준제정사업 발표;조항대응미확정|불인정: 단독 근거/서로 다른 주장|
|F14|[^n8], 본문 인용 위치 참조|ISO기반국내채택목록;ISO DIS와다른판,동일주장독립재현아님|불인정: 단독 근거/서로 다른 주장|
|F15|[^n9], 본문 인용 위치 참조|C19/C20은같은MOEL 정책계열·다른문서지위|불인정: 단독 근거/서로 다른 주장|
|F16|[^n9], 본문 인용 위치 참조|C19/C20은같은MOEL 정책계열·다른문서지위|불인정: 단독 근거/서로 다른 주장|
|F17|[^n9], 본문 인용 위치 참조|C19/C20은같은MOEL 정책계열·다른문서지위|불인정: 단독 근거/서로 다른 주장|
|F18|[^n11], 본문 인용 위치 참조|C18은같은기관;참여의무와실무사례는다른주장|불인정: 단독 근거/서로 다른 주장|
|F19|[^n11], 본문 인용 위치 참조|C18은같은기관;참여의무와실무사례는다른주장|불인정: 단독 근거/서로 다른 주장|
|F20|[^n10], 본문 인용 위치 참조|C18/C20은같은기관;예고와시행고시는별개|불인정: 단독 근거/서로 다른 주장|
|F21|[^n10], 본문 인용 위치 참조|C18/C20은같은기관;예고와시행고시는별개|불인정: 단독 근거/서로 다른 주장|
|F22|[^n12], 본문 인용 위치 참조|동일프로젝트명세/스키마 대조;외부안전성검증아님|불인정: 단독 근거/서로 다른 주장|
|F23|[^n12], 본문 인용 위치 참조|동일프로젝트명세/스키마 대조;외부안전성검증아님|불인정: 단독 근거/서로 다른 주장|
|F24|[^n12], 본문 인용 위치 참조|동일프로젝트명세/스키마 대조;외부안전성검증아님|불인정: 단독 근거/서로 다른 주장|
|F25|[^n12], 본문 인용 위치 참조|동일프로젝트명세/스키마 대조;외부안전성검증아님|불인정: 단독 근거/서로 다른 주장|
|F26|[^n13], 본문 인용 위치 참조|C39는별도연구팀·다른도구;Nav2 인증문구는C25단독|불인정: 단독 근거/서로 다른 주장|
|F27|[^n20], 본문 인용 위치 참조|C25는별도프로젝트·다른노드;Ogma보고한계는C39단독|불인정: 단독 근거/서로 다른 주장|
|F28|[^n14], 본문 인용 위치 참조|단일벤더매뉴얼;Nav2/VDA는제품별보장·책임을재현하지않음|불인정: 단독 근거/서로 다른 주장|
|F29|[^n14], 본문 인용 위치 참조|단일벤더매뉴얼;Nav2/VDA는제품별보장·책임을재현하지않음|불인정: 단독 근거/서로 다른 주장|
|F30|[^n15], 본문 인용 위치 참조|C30/C31은같은Open-RMF;과거보고와후속구현을시간순대조|불인정: 단독 근거/서로 다른 주장|
|F31|[^n17], 본문 인용 위치 참조|C30은같은프로젝트코드;릴리스이력추적의일관성확인|불인정: 단독 근거/서로 다른 주장|
|F32|[^n16], 본문 인용 위치 참조|C28/C31 및PR413/82는같은Open-RMF;실행시험아님|불인정: 단독 근거/서로 다른 주장|
|F33|[^n18], 본문 인용 위치 참조|한EU법령의서로다른조문;국내고시와같은관할/주장아님|불인정: 단독 근거/서로 다른 주장|
|F34|[^n18], 본문 인용 위치 참조|한EU법령의서로다른조문;국내고시와같은관할/주장아님|불인정: 단독 근거/서로 다른 주장|
|F35|[^n18], 본문 인용 위치 참조|한EU법령의서로다른조문;국내고시와같은관할/주장아님|불인정: 단독 근거/서로 다른 주장|
|F36|[^n19], 본문 인용 위치 참조|저자프리프린트단독;독립재현/공식코드확보못함|불인정: 단독 근거/서로 다른 주장|
|F37|[^n19], 본문 인용 위치 참조|저자프리프린트단독;독립재현/공식코드확보못함|불인정: 단독 근거/서로 다른 주장|
|F38|[^n19], 본문 인용 위치 참조|저자프리프린트단독;독립재현/공식코드확보못함|불인정: 단독 근거/서로 다른 주장|

독립 교차 확인된 동일 주장: **0개**. 프로젝트 내부 일관성 확인과 독립 교차 검증을 구별했다.

### M-48 4단계 분석 기록

2026-10-11. 원자 주장 38개(초안 사실36·추정2), 보완15개. `claims.json`은 주장·출처·원문 위치·구절·저장본 매핑이고 `amendments.json`은 위키 분류·범위·설계 의견이다. `draft-body.md`는 검증 전 초안이다.

#### 질문별 종합

|질문|결과와 위키 분류|교차 확인·범위|남은 공백|
|---|---|---|---|
|Q1 플릿 위험평가|STPA 절차/산출물, 11로봇 화학실험실 구조 분석, 건설 현장 평가를 보완1~3에 추가|방법론·다중로봇 분석·단일로봇 배치 사례가 각각 다른 주장. 동일 효과를 독립 재현한 증거 아님|2023 STPA/SPN 본문, 실제 혼합 제조사 플릿의 장기 안전 결과|
|Q2 표준·책임 경계|Part3 예정 문구 정정, ISO 개발단계 정정(보완4~5)|발행기관 목록은 날짜·범위까지. 표준 요구 본문은 미열람|정식 본문에 근거한 통합자·사용자 조항 매핑|
|Q3 국내KS|KS B7327 번호와 범위, KSBISO3691-4 IDT 목록 추가(보완6)|정부 발표와 같은 표준을 중복 독립 증거로 세지 않음|R15.08-2/ISO10218-2와의 조항 대응·인증 등가성|
|Q4 국내RA|2024-76 판의 주체·근로자 참여·추가 위험 조건, 가이드 사례, 2026예고안 추가(보완7~9)|조문·공식가이드·예고안은 같은 정책 계열. 상위법 전체 적용 판단 아님|2026최종고시와 법령 적용 조합, 실제 계약 책임 주체|
|Q5 정지/감시경계|VDA3.0.0 계약, Nav2 인증 설명, Ogma 감시 한계, LD 인터록 설명 추가(보완10~12)|서로 다른 제품·규격의 제한을 한 제품의 보장으로 합치지 않음|원격 안전명령의 PL과 해당 현장 승인 조건|
|Q6 RMF화재|2025 이슈를 PR/CHANGELOG/고정코드로 추적, 구현미확인 문구 수정(보완13)|같은 프로젝트 내부 추적. 실행시험·현장 대피 검증 없음|장애/복구/재개 조건과 실제 배치 동작|
|Q7 변경관리|국내 추가위험 조건과 EU정의/일반적용일 분리(보완7·14)|관할·시행 지위를 별도 표시. 로봇 펌웨어에 대한 법률 분류 안 함|국내 설치 작업장 재심사, 개별 ROP변경의 EU 적용|
|Q8 안전게이트|230합성 작업·30시뮬레이션·실물정성결과 분리, 분모 문제 보류(보완15)|저자실험 원문만 확인. 2026프리프린트, 독립 재현 아님|공식코드, CR0 분모, 표II183과전체230의 처리규칙|

#### 충돌·판 차이 처리

|대조|관찰|처리|
|---|---|---|
|위키 Part3 예정 / A3 2026목록|발행일2026-04-23|공식목록의 발행 사실만 정정|
|위키 ISO/CD·차기2판 / ISO프로젝트|DIS·Edition3·40.60|접근일현재 목록을 명시. 위키조회당시 페이지가 실제로 무엇이었는지 추정하지 않음|
|ISO12100 검색스니펫40.20 / 목록40.60|본문이 후속단계 날짜를 제공|목록본문 기준, FDIS완료/발행으로 확대하지 않음|
|KS7327 / KS3691 IDT / ISO DIS|서로다른표준·발행판|형식적 유사성으로 동일성 도출 금지|
|국내2024고시 / 2026예고안|기존판과 아직 의견수렴 중인 안|최종시행규정으로 합치지 않음|
|VDA릴리스문구오타 / 실제스키마|activeEmergenceStop와activeEmergencyStop|고정 명세·스키마 일치명을 사용|
|RMF이슈Open / mergedPR·고정코드|Open표시와 기능존재는다른문제|이슈상태에서구현부재를추론하지않음;2.10.0기록과2.14.0확인판구분|
|Belzile2021 / arXiv2025|워크숍판과나중업로드판|2025년새현장실증이라고서술하지않음;두판독립계산금지|
|SafeGate식9 / VI-B|executed분모와모두차단/CR0서술|계산규칙미확인으로성능수치전재보류;저자오류라고단정하지않음|

#### 독립성 판정

독립 교차 확인된 동일 주장 **0개**. 서로 다른 팀의 STPA 활용이나 감시 기술은 참고 관점이 다양하다는 뜻이며 동일 제품·동일 조건의 안전성 주장을 두 번 검증한 것이 아니다. MIT 방법서와 Bensaci 논문은 별도 저자이지만 후자가 해당 방법론을 인용·적용한다는 사실만으로 독립 재현이라고 세지 않았다. RMF의 이슈/PR/코드/CHANGELOG는 한 프로젝트 내부 추적이다. 부록E는 독립 여부와 비인정 이유를 전부 표시한다.

#### ROP 위험등록부 제안 예시 — 전부 의견

다음은 원문의 실험 결과가 아니라 위 근거를 읽고 제안하는 분석 양식이다.

|제어행동·상황|위험 시나리오|등록할 안전제약 후보|검증 증거 후보|
|---|---|---|---|
|재개 승인 전 stopPause|안전정지 해제와 업무 재개가 잘못 결합|현장 승인·로봇 안전상태·업무pause 상태를 구별|승인누락·지연상태·중복재개의 상태전이시험|
|선택 플릿 비상신호|빈 fleet_names가 의도와 다르게 전체플릿에 전달|대상목록 검토·전파범위 표시|빈목록/일치/불일치/복수플릿 시험 및 현장 대피계획 검토|
|어댑터/운영정책 갱신|작업절차 변화로 기존 RA의 가정이 깨짐|변경범위·추가위험·검토자·배포승인 연결|변경전후 시나리오, 회귀시험, 조치완료·재검증 기록|

각 행에는 손실/위험ID, 제어주체, 통제대상, 피드백의 시간적 유효성, 제조사 인터페이스 조건, 조치 소유자, 수용 기준을 덧붙인다. 이 표를 사용한다는 사실만으로 PL·인증·법적 적합성이 입증되지는 않는다.

## 제출 지표

- 보완 항목 수: 15
- 새 출처 수: 14 (채택 총20)
- 원문 열람 비율: 15/20, 75%
- 독립 교차 확인 주장: 0
- 5단계 태그 낮춤: 0
- 검증에서 고친 본문 문장: 0 (근거 인용 오류1·위치 오류2는 별도)
- 확인 못 한 항목: 14 (U01~U14)
