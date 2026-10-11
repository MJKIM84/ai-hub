---
area: 49
title: "49. 사람 근접 안전"
researched: 2026-10-11
researcher: "OpenAI Codex"
---

# 49. 사람 근접 안전 — 보완 조사

## 요약

- 구역 제한의 지원 능력·단위·활성화와 실제 감속 확인을 구분하는 보완안을 제시한다. [의견]
- 병원 모사 시험의 표현을 바로잡고 실물 창고·병원 연구의 조건과 분모를 덧붙인다. [의견]
- 편안함 연구와 임무 효율 연구를 사람 안전의 보편 수치로 옮기지 않도록 제안한다. [의견]
- 국내 원조문과 표준 공개 목록에서 확인한 범위를 제시하며, 별표·유료 전문 미열람은 그대로 남긴다. [의견]
- 사람 위치 연계에는 측정시각·좌표계·오류·차량 실행 확인을 검증 항목으로 추가한다. [의견]

## 보완 항목

### [6. 대표 접근법과 기술] — 추가

**보완 01: SSM 측정 조건과 불확실성** · 진단/질문: W01·W07·W21 / Q1

- **H01** 새 내용: NIST 논문에서 레일 장착 6자유도 매니퓰레이터의 반응시간 실측값은 0.113초였다. [사실][^n1]
  - 근거 메모: C01 · §5, PDF8쪽(P7),L723–730 · 원문 “0.113 s”. 특정 작업셀 장치의 측정값. AMR 기본값이나 현재 표준 요구값으로 전용하지 않는다. 단일 출처 계열, 독립 교차 확인 없음.
- **H02** 새 내용: 같은 논문은 분리거리 평가에서 로봇과 작업자의 위치 불확실성을 각각 ZR과 ZS로 다룬다. [사실][^n1]
  - 근거 메모: C01 · §6, PDF8쪽(P7),L733–742 · 원문 “position uncertainties”. 2017 권호의 연구 설명이며 규범 조항의 직접 인용은 아니다. 단일 출처 계열, 독립 교차 확인 없음.
- **H03** 새 내용: SICK의 설명에 따르면 보호필드 전환과 추가 샘플링 설정은 감지 응답시간을 늘린다. [추정][^n2]
  - 근거 메모: C05 · Multiple sampling 앞 문단과 해당 절,L84–88 · 원문 “switching between cases adds to the response time”. 제조사 기술 설명. 개별 센서·제어기·하중·바닥 조건의 시험값은 별도 확인해야 한다. 단일 출처 계열, 독립 교차 확인 없음.

- ROP 시사점: 로봇별 반응·제동 측정값, 센서 신선도, 하중 조건의 소유자와 갱신 시점을 ROP 연계 명세에 따로 기록한다. 현장 검증 주체는 계약과 안전 설계 자료로 확인한다. [의견]

### [6. 대표 접근법과 기술] — 추가

**보완 02: 속도 구역의 지원 능력·단위·진입 경계** · 진단/질문: W10 / Q2

- **H04** 새 내용: VDA5050 3.0.0은 로봇이 처리할 수 있는 구역 유형을 factsheet의 supportedZones로 신고하도록 요구한다. [사실][^n3]
  - 근거 메모: C06 · §6.4,L845 · 원문 “shall therefore report”. 명세상 요구. 모든 기종이 모든 구역을 지원한다는 뜻은 아니다. 단일 출처 계열, 독립 교차 확인 없음.
- **H05** 새 내용: 같은 판의 SPEED_LIMIT 구역 진입 판단은 적재물을 포함한 로봇 외곽을 기준으로 한다. [사실][^n3]
  - 근거 메모: C06 · §6.4.1.1,L853–870 · 원문 “including its load”. 명세의 contour-based 분류. 외곽 일부가 진입하면 구역 진입이다. 단일 출처 계열, 독립 교차 확인 없음.
- **H06** 새 내용: SPEED_LIMIT의 maximumSpeed는 m/s 단위로 지정된다. [사실][^n3]
  - 근거 메모: C06 · §6.4.1.1,Table6,L870 · 원문 “in m/s”. 명세의 절대 선속도 단위. 단일 출처 계열, 독립 교차 확인 없음.
- **H07** 새 내용: 같은 명세는 구역에 진입하는 시점에 이미 제한속도에 도달하도록 요구한다. [사실][^n3]
  - 근거 메모: C06 · §6.4.1.1,Table6,L870 · 원문 “already be reached upon entering”. shall의 요구 강도를 유지. 실제 차량의 감속시간 실측을 제공하는 문장은 아니다. 단일 출처 계열, 독립 교차 확인 없음.

- ROP 시사점: 구역 등록 시 supportedZones와 적재 외곽을 확인하고, 감속 시작점을 진입 경계 앞에 두는 통합 시험을 설계한다. [의견]

### [6. 대표 접근법과 기술] — 추가

**보완 03: 구역 전송과 활성화의 분리** · 진단/질문: W10·W30 / Q2

- **H08** 새 내용: 구역 집합의 내용을 바꿀 때는 새 zoneSetId를 사용해야 한다. [사실][^n3]
  - 근거 메모: C06 · §6.4.2,L907 · 원문 “new `zoneSetId`”. 동일 식별자 내용 불변 계약. 단일 출처 계열, 독립 교차 확인 없음.
- **H09** 새 내용: 새 구역 집합은 DISABLED 상태에서 enableZoneSet 동작으로 활성화한 뒤 사용해야 한다. [사실][^n3]
  - 근거 메모: C06 · §6.4.2,L909 · 원문 “enabled through”. 전송과 활성화의 구별. 제동 완료 확인과 동일하지 않다. 단일 출처 계열, 독립 교차 확인 없음.

- ROP 시사점: 전송 완료, 활성화 상태, 실제 감속 관측을 서로 다른 상태로 기록한다. 구역 내용 변경은 새ID로 배포하고 미활성 로봇의 경로 진입을 운영 정책에서 다룬다. [의견]

### [7. 관련 표준·프레임워크·오픈소스] — 추가

**보완 04: Nav2의 센서 신선도와 0의 의미** · 진단/질문: W22·W23 / Q2

- **H10** 새 내용: Nav2 Jazzy의 Collision Monitor 문서는 이 노드가 하드 실시간 안전 인증을 제공하지 않는다고 명시한다. [사실][^n4]
  - 근거 메모: C07 · 소개,L545 · 원문 “does not provide hard real-time safety certifications”. 2026-10-11 열람한 Jazzy 문서. 별도 안전장치의 인증 여부를 판정하는 문장이 아니다. 단일 출처 계열, 독립 교차 확인 없음.
- **H11** 새 내용: source_timeout을 0.0으로 설정하면 새 센서 데이터가 없을 때 정지시키는 차단 동작이 비활성화된다. [사실][^n4]
  - 근거 메모: C07 · source_timeout,L619 · 원문 “disables this blocking mechanism”. 이 파라미터에 관한 문서 설명에 한정한다. 단일 출처 계열, 독립 교차 확인 없음.
- **H12** 새 내용: Nav2 Speed Filter에서 speed_limit 값 0은 속도 제한이 없다는 뜻이다. [사실][^n5]
  - 근거 메모: C08 · speed_limit_topic,L468–472 · 원문 “Zero value means no speed restriction”. 상대값/절대값 선택과 무관한 메시지 의미이며 정지 명령이 아니다. 단일 출처 계열, 독립 교차 확인 없음.

- ROP 시사점: 센서 stale 정지 정책과 speed_limit 메시지를 서로 다른 계약으로 취급한다. source_timeout=0이나 speed_limit=0을 일괄적인 안전 정지 설정으로 내보내지 않는다. [의견]

### [6. 대표 접근법과 기술] — 추가

**보완 05: RMF 계획 제약과 차량 실행 확인** · 진단/질문: W30 / Q2

- **H13** 새 내용: Open-RMF 2.14.0의 limit_lane_speeds 구현은 0 이하 속도 제한 요청을 무시한다. [사실][^n6]
  - 근거 메모: C09 · FleetUpdateHandle.cpp,L2248–2261 · 원문 “request.speed_limit() <= 0.0”. 고정 태그 코드 정독. 경고는 통로를 닫으려면 close_lanes API를 쓰도록 안내한다. 단일 출처 계열, 독립 교차 확인 없음.
- **H14** 새 내용: 유효한 속도 제한 요청은 planner 그래프의 통로 속성에 반영된다. [사실][^n6]
  - 근거 메모: C09 · FleetUpdateHandle.cpp,L2263–2276 · 원문 “properties.speed_limit(request.speed_limit());”. 계획 계층의 코드 경로. 물리적 감속 완료 ACK를 확인한 것은 아니다. 단일 출처 계열, 독립 교차 확인 없음.

- ROP 시사점: 어댑터에서 제한 없음·양수 제한·통로 폐쇄·보호정지를 별도 명령으로 표현한다. planner 상태 갱신만으로 차량 감속 완료를 보고하지 않도록 검증 절차를 둔다. [의견]

### [8. 대표 연구와 자료] — 추가

**보완 06: CBF 창고 연구의 실물 규모와 지표 분모** · 진단/질문: W13 / Q3

- **H15** 새 내용: Farrell 등의 창고 연구는 Freight·Jackal·Megarover 실물 플랫폼을 평가했다. [사실][^n7]
  - 근거 메모: C11 · §VI,L192–194 및 §VII,L223 · 원문 “real-world experiments”. arXiv2503.21141v1. OptiTrack 위치계측 조건. 단위 과제 각 설정10회이며 플릿 실험과 분모를 혼합하지 않는다. 단일 출처 계열, 독립 교차 확인 없음.
- **H16** 새 내용: 이 연구의 Table IV 값은 Open-RMF가 계획상 로봇을 정지시킨 시간을 제외한다. [사실][^n7]
  - 근거 메모: C11 · §VI-B,TableIV,L210–218 · 원문 “exclude periods”. 4대·1.0m/s 또는2대·1.5m/s, 보행자0/1/2명 조건. 전체 임무 처리량 지표로 전용하지 않는다. 단일 출처 계열, 독립 교차 확인 없음.

- ROP 시사점: Open-RMF의 상위 배정과 로컬 제어 장벽 함수(CBF)를 분리한 연구 구조를 참고하되, 현장 처리량 비교에는 계획 정지시간도 포함한다. [의견]

### [8. 대표 연구와 자료] — 추가

**보완 07: HATA의 혼잡 비용과 임무 실패 지표** · 진단/질문: W11·W24 / Q3

- **H17** 새 내용: HATA의 5·10·15대 로봇 평가는 기록된 사람 궤적을 재생하는 시뮬레이션이다. [사실][^n8]
  - 근거 메모: C12 · §IV-B,L131–136 · 원문 “within a simulated environment”. arXiv2508.19731v1. 실측 궤적을 사용한 사실이 로봇의 현장 운용 시험을 뜻하지 않는다. 단일 출처 계열, 독립 교차 확인 없음.
- **H18** 새 내용: HATA 논문의 실패율은 교착 또는 10분 제한시간 때문에 완료하지 못한 과제의 비율이다. [사실][^n8]
  - 근거 메모: C12 · §V,TableI/II 설명,L171 · 원문 “due to deadlock or timeout”. 임무 미완료 지표이며 사고율이나 사람 충돌률이 아니다. 단일 출처 계열, 독립 교차 확인 없음.

- ROP 시사점: 사람 이동 통계 기반 배정과 실시간 안전 감지를 별도 기능으로 관리한다. 26%·19% 요약 개선치를 쓰려면 기준선·가중 평균·실패 시행 포함 여부를 확보한다. [의견]

### [5. 적용 사례 (현장 유형 명시)] — 추가

**보완 08: 실제 병원 혈액 운송 시연과 이종 로봇 시험의 구별** · 진단/질문: W20 / Q4

- **H19** 새 내용: Tartu 병원 현장 시험에서 TIAGo는 중환자실에서 검사실로 혈액 샘플을 운반했다. [사실][^n9]
  - 근거 메모: C18 · §3.1,Figure8,L459–461 · 원문 “blood samples from ICU to the lab”. 실제 병원 시연. 의료진 적재·요청 확인→운반→검사실 인계 확인→ICU 복귀 흐름이 기술돼 있다. 단일 출처 계열, 독립 교차 확인 없음.
- **H20** 새 내용: 같은 논문에서 TIAGo와 Jackal의 이종 다로봇 검증은 시험 환경에서 수행됐다. [사실][^n9]
  - 근거 메모: C18 · §4,Increasing the number and diversity of robots,L489 · 원문 “in a testing environment”. 병원 내부 복수 배송로봇 적용은 당시 미래 과제. 병원 이종 플릿 상시 운영 실증으로 쓰지 않는다. 단일 출처 계열, 독립 교차 확인 없음.

- ROP 시사점: 혼잡으로 기다릴 위치, 병원 직원의 인계 확인, 재출발 조건을 하나의 임무 상태 기록에 연결한다. 병원 플릿 규모나 장기 무사고 성과는 별도 운영 자료를 요구한다. [의견]

### [5. 적용 사례 (현장 유형 명시)] — 수정

**보완 09: 모의 병원은 실물 시험 공간** · 진단/질문: W14 / Q4

- 대상 문장(위키5절): “이 사례는 실제 병원이 아닌 모의 병원 환경에서 수행한 시뮬레이션 평가다(Scientific Reports, 2024-08-07).”

- **H21** 새 내용: Rondoni 등의 병원 벤치마크는 병원 공간을 실물로 모사한 환경에서 수행됐다. [사실][^n10]
  - 근거 메모: C19 · Experimental testing,L210–221 · 원문 “replicates the physical layout”. HOSBOT·TIAGo와 Vicon8카메라를 사용했다. 실제 환자와 함께 상시 운영한 결과나 컴퓨터 시뮬레이션만의 결과로 분류하지 않는다. 단일 출처 계열, 독립 교차 확인 없음.
- **H22** 새 내용: 이 연구의 이동 장애물은 원격조종되는 두 번째 이동로봇 베이스였다. [사실][^n10]
  - 근거 메모: C19 · Mobile Obstacle,L128 · 원문 “testing mobile base teleoperated”. 사람을 대상으로 안전거리를 검증한 시험과 구별한다. 단일 출처 계열, 독립 교차 확인 없음.

- ROP 시사점: 위키의 시뮬레이션 표현을 실물 모사 환경으로 구체화하고, 시험속도0.2·0.6·1.0m/s를 법정 사람 근접 속도처럼 인용하지 않는다. [의견]

### [8. 대표 연구와 자료] — 추가

**보완 10: 편안함 표본·분모·예측기 한계** · 진단/질문: W05·W25 / Q4

- **H23** 새 내용: Jafari 등의 편안함 연구는 23~41세 자원자 32명을 대상으로 했다. [사실][^n11]
  - 근거 메모: C20 · §IV,L112–114 · 원문 “Twenty-two males and ten females”. arXiv2604.13677v1. 원격조종 로봇·3.2m복도·1.4/2.8m/s. 160회 중 전체수집실패2회 제외,측면거리 관련 분석은 추가13회 제외. 단일 출처 계열, 독립 교차 확인 없음.
- **H24** 새 내용: 그 연구의 복합 예측기는 분석에 사용한 데이터와 같은 데이터로 평가됐다. [사실][^n11]
  - 근거 메모: C20 · §V-C,L262 · 원문 “the same dataset”. 독립 시험집합 성능이 아니다. 단일 출처 계열, 독립 교차 확인 없음.
- **H25** 새 내용: 논문에서 보고한 오즈비 3.67은 편안하다고 예측된 경우와 그렇지 않은 경우의 실제 편안함 오즈를 비교한 값이다. [사실][^n11]
  - 근거 메모: C20 · §V-B,TableVI 설명,L243 · 원문 “The odds ratios”. 사고 감소 확률·안전거리 인증·인과 효과와 구분한다. 부록D에서 표 산술을 별도로 대조한다. 단일 출처 계열, 독립 교차 확인 없음.

- ROP 시사점: 편안함 지표와 보호정지 성능을 별도 평가표로 운영한다. 자율주행·고령자·아동·휠체어 사용자에게 옮겨 쓰기 전 해당 조건의 데이터를 추가 검증한다. [의견]

### [7. 관련 표준·프레임워크·오픈소스] — 추가

**보완 11: 한국 운행안전인증의 원조문과 최신 고시 상태** · 진단/질문: W16~W19·W31 / Q5

- **H26** 새 내용: 시행규칙 제7조의4제1항은 운행안전인증 기준의 최대 질량을 적재물 포함 500kg 이하로 정한다. [사실][^n13]
  - 근거 메모: C22 · 제7조의4제1항제1호,L82–84 · 원문 “500킬로그램 이하일 것”. 2025-10-01 시행판의 해당 조문. 모든 공간에서의 운행허가 조건을 완결하는 것으로 해석하지 않는다. 단일 출처 계열, 독립 교차 확인 없음.
- **H27** 새 내용: 같은 항의 최대 속도 기준은 시속 15km 이하이다. [사실][^n13]
  - 근거 메모: C22 · 제7조의4제1항제2호,L85 · 원문 “시속 15킬로미터 이하일 것”. 세부사항은 제2항에서 고시로 위임한다. 단일 출처 계열, 독립 교차 확인 없음.
- **H28** 새 내용: 제7조의5의 신청서류에는 횡단보도 통행방식과 통신장애·사고·혼잡 대응 시나리오를 담은 운행계획서가 포함된다. [사실][^n13]
  - 근거 메모: C22 · 제7조의5제1항제4호,L91–98 · 원문 “혼잡상황 대응 시나리오”. 서류 요구사항의 직접 확인이며 ROP 사업자의 법적 지위를 해석하지 않는다. 단일 출처 계열, 독립 교차 확인 없음.
- **H29** 새 내용: 산업통상부는 관련 고시의 2025-021호 일부개정을 2025-11-24 공식 게시했다. [사실][^n12]
  - 근거 메모: C21 · 게시글64952,L196·201·203·210–215 · 원문 “2025-021”. 공식 공고 메타데이터만 확인. 첨부 별표를 읽지 못했으므로 질량별 운행속도와 횡단보도 세부 변경을 확정하지 않는다. 단일 출처 계열, 독립 교차 확인 없음.

- ROP 시사점: ROP 운행계획 자료에 통신장애·혼잡·횡단 시나리오를 구조화하되, 최신 별표를 확보하기 전2023기사 수치를 현행 구역 정책으로 자동 변환하지 않는다. [의견]

### [7. 관련 표준·프레임워크·오픈소스] — 추가

**보완 12: ISO13482의 현행판과 개정 절차** · 진단/질문: W02 / Q6

- **H30** 새 내용: ISO의 개정 13482 목록은 2026-09-15에 승인 단계 50.20에 들어간 개발 중 문서로 표시된다. [사실][^n14]
  - 근거 메모: C26 · Life cycle,L67–69 및 L107 · 원문 “Under development”. ISO/FDIS13482,edition2. 정식 발행이 완료됐다는 뜻으로 쓰지 않는다. 단일 출처 계열, 독립 교차 확인 없음.
- **H31** 새 내용: ISO13482:2014의 공식 목록은 이 판을 Published 및 개정 예정 단계 90.92로 표시한다. [사실][^n15]
  - 근거 메모: C27 · General information,L77–87 · 원문 “Published”. 2014-02 edition1의 목록 정보. 개정판 세부 요구를 확정하는 근거가 아니다. 단일 출처 계열, 독립 교차 확인 없음.

- ROP 시사점: 2014판 공개 범위와 개발 중인2판의 상태를 별도 항목으로 관리한다. FDIS의 내용을 발행된 요구사항으로 고정하지 않는다. [의견]

### [7. 관련 표준·프레임워크·오픈소스] — 추가

**보완 13: 이동부 위험과 정적 장애물 시험의 범위** · 진단/질문: W26·W27 / Q6

- **H32** 새 내용: ISO10218-1:2025의 공개 범위는 이동 플랫폼에 부착되거나 그 일부인 로봇·매니퓰레이터의 이동성 관련 위험을 다루지 않는다고 명시한다. [사실][^n20]
  - 근거 메모: C44 · Scope,L95–108 · 원문 “mobility when robots or manipulators”. Part1 공개 범위의 제외 위험만 확인. 이동 매니퓰레이터 전체를 표준 밖이라고 판정하지 않는다. 단일 출처 계열, 독립 교차 확인 없음.
- **H33** 새 내용: KS B8252의 공개 적용 범위는 실내 이동로봇의 정적 장애물 보호정지 평가이다. [사실][^n16]
  - 근거 메모: C30 · 적용 범위,L229;이력L244 · 원문 “정적 장애물의 보호정지”. 2020상세 페이지와2025-09-05확인이력. 움직이는 사람과의 거리 수치나 국내 병원 의무속도는 전문 미열람으로 확인 못 함. 단일 출처 계열, 독립 교차 확인 없음.

- ROP 시사점: 로봇 팔의 안전 요구, 이동부의 사람 감지, 정적 보호정지 시험의 검증 범위를 구분한 적용성 표를 만든다. 법적 의무 판단은 이 자료만으로 하지 않는다. [의견]

### [9. ROP가 직접 맡는 것과 외부와 연계하는 것] — 추가

**보완 14: 조끼 사례와 고정 공개 인터페이스의 증거 차이** · 진단/질문: W12·W30 / Q7

- **H34** 새 내용: Amazon은 작업자 조끼의 신호에 따라 로봇이 감속·우회하고 가까워지면 정지한다고 설명한다. [추정][^n17]
  - 근거 메모: C33 · 본문,L11–12 · 원문 “automatically slow down”. 회사 단독 운영 설명. 제조사가 다른 플릿의 공통 인터페이스·거리·지연·안전등급은 확인 못 함. 단일 출처 계열, 독립 교차 확인 없음.
- **H35** 새 내용: 이 구현은 사람 식별자별 위치를 `/humans/persons/<id>/position` 토픽에 `PointOfInterest3DStamped` 형식으로 발행한다. [사실][^n18]
  - 근거 메모: C35 · src/yolo_uwb_fusion_node.cpp,L70–77·141–149·159–168 · 원문 “PointOfInterest3DStamped”. commit934ca8387a205aaac894da22451970a203777e18. 문서와 코드가 같은 프로젝트이므로 독립 검증으로 세지 않는다. 단일 출처 계열, 독립 교차 확인 없음.
- **H36** 새 내용: 이 구현의 transformUWBPosition 함수는 좌표변환 예외를 잡은 경우 입력 좌표를 그대로 반환한다. [사실][^n18]
  - 근거 메모: C35 · src/yolo_uwb_fusion_node.cpp,L92–95(catch 블록) · 원문 “return pt;”. 조건부 코드 동작만 확인. 실제 운용 실패·안전사고·상위 계층 보정 부재를 실증한 것은 아니다. 단일 출처 계열, 독립 교차 확인 없음.

- ROP 시사점: 사람 좌표 수신에는 원래 측정시각·좌표계·변환 성공 여부·만료시각을 명시한다. C35의 예외 경로는 시험 대상으로 삼고, 위치 발행과 차량 감속 확인을 별도 단계로 검증한다. [의견]

### [6. 대표 접근법과 기술] — 추가

**보완 15: 취약 보행자·가림 조건의 평가 공백** · 진단/질문: W20 / Q8

- **H37** 새 내용: NavWareSet 프로젝트는 통제 실내 수집 실험의 참가자를 총 17명으로 설명한다. [사실][^n19]
  - 근거 메모: C41 · Experiment description,L58 및 scene표L63–110 · 원문 “In total 17 participants”. 그룹과 쌍에 같은 참가자가 중복되므로 합산20명으로 바꾸지 않는다. 취약인구 안전성 검증 결과는 확인 못 함. 단일 출처 계열, 독립 교차 확인 없음.
- **H38** 새 내용: NavWareSet의 시나리오에는 시야가 가려진 모퉁이에서 로봇과 사람이 만나는 상황이 포함된다. [사실][^n19]
  - 근거 메모: C41 · Scenarios Table,L53 · 원문 “BLIND CORNER”. 데이터 시나리오의 존재만 확인. 검출 실패율·충돌위험의 독립 실증은 아니다. 단일 출처 계열, 독립 교차 확인 없음.

- ROP 시사점: 모퉁이 가림·경로 점유·혼잡을 재생 시험에 포함하고, 아동·보행 보조기·휠체어 사용자별 감지 누락과 우회 가능성을 별도로 평가한다. 존재하는 데이터셋만으로 취약인구 범위가 충족됐다고 판단하지 않는다. [의견]

## 답한 열린 질문

질문 식별은 위키11절의 원래 질문 순서를 따른다(원문 oq-id 없음). 짧은 인용만 싣고 전체 원문은 [보존한 질문 페이지](.research-work/M-49/2026-09-30-area49-s11.txt)의 「3. 본문」을 참조한다. OQ번호는 이번 조사에서 붙인 식별자다.

|질문 식별·요지|답변 상태·근거|남은 부분|
|---|---|---|
|OQ1 “누가 검증하는가?” — 플릿 구역과 보호필드 정합|부분 답변. H04~14의 전송/활성화/계획 계약을 확인했다.|위험감소 인정 조건·현장 검증 책임자·실측 ACK는 확인 못 함.|
|OQ2 “8개 항목” / “16가지” — 심사 항목 차이|미해결. H26~29로 현행 원조문과 고시 게시 상태까지만 보완했다.|최종 별표와 기관 안내의 상하 항목 대조 확인 못 함.|
|OQ3 “사람 근접 속도·거리 기준” — 국내 실내 기준|부분 답변. H30~33의 판·공개 적용 범위를 확인했다.|병원/상업/공동주택 모두에 적용되는 강제 속도·거리값은 확인 못 함.|
|OQ4 “여러 로봇 플릿에 동시에 전달” — 사람 위치 연계|부분 답변. H34의 기업 사례와 H35~36의 공개 구현을 구분했다.|이종 플릿 동시 감속·정지의 공통 안전 인터페이스와 검증 사례 확인 못 함.|

답변 표는 위 주장 ID를 참조하며 새로운 사실 문장을 추가하지 않는다. 완전히 답한 기존 열린 질문은0개다.

## 새로 생긴 열린 질문

- U01. VDA zoneSet 활성화부터 실제 제한속도 도달까지 어떤 주체가 측정하고 승인하는가? — 확인 못 함.
- U02. 로봇별 지연·제동·하중·센서 오차가 바뀌면 안전구역과 ROP 정책을 어떻게 함께 재검증하는가? — 확인 못 함.
- U03. Nav2와 RMF의 서로 다른0값 계약을 이종 어댑터의 실행시험으로 확인한 공개 자료가 있는가? — 확인 못 함.
- U04. Farrell 연구의 고정 실행 코드와 현장 센서·통신 조건으로 재현한 독립 결과가 있는가? — 확인 못 함.
- U05. HATA의26%·19% 개선을 재계산할 수 있는 집계 분모·실패시행 처리·고정 코드가 있는가? — 확인 못 함.
- U06. C20 TableVI와 TableVII의 정밀도·재현율 값은 저자 정정 또는 원자료로 어떻게 해소되는가? — 확인 못 함.
- U07. Tartu 병원의 장기 운영기간·완료율·사고율과 복수 제조사 실제 병원 배치 결과는 무엇인가? — 확인 못 함.
- U08. 실외인증2025-021 최종 별표에서 질량별 속도와 횡단보도 조건은 어떻게 개정됐는가? — 확인 못 함.
- U09. 기관 안내의8항목과2023기사16항목은 현재 어느 계층·판에 대응하는가? — 확인 못 함.
- U10. ISO10218-2:2025 본문의 이동 매니퓰레이터 통합 조건과 현행 SSM 세부 요구는 무엇인가? — 확인 못 함.
- U11. ISO13482 개정판은 언제 정식 발행되며 기존판에서 실제 어떤 사람 근접 요구가 바뀌는가? — 확인 못 함.
- U12. KS B8252 확인판 전문 및 국내 실내 운행 법규에 동적 사람 근접 속도·거리 요구가 있는가? — 확인 못 함.
- U13. 착용장치/출입 신호의 위치를 여러 제조사에 전달할 때 공통 감속·정지 ACK와 안전 기능 소유자는 누구인가? — 확인 못 함.
- U14. C35 좌표변환 실패·오래된 UWB 입력·검출 소실을 전체 시스템이 어떻게 처리하며 어떤 시험으로 검증했는가? — 확인 못 함.
- U15. 아동·휠체어·보행 보조기·시각장애 사용자별 가림/양보/통로 점유 상황에서 독립적으로 측정한 감지·접근성 결과가 있는가? — 확인 못 함.

## 출처

집계: 총20개, 원문 열람15/20(75%), 1차 자료19개, 독립 교차 확인된 주장0개. 새 출처12개. 원문 열람은 실제로 관련 본문/코드를 읽었다는 뜻이며 문서 전체 정독을 뜻하지 않는다. 공식 목록/공고 메타데이터5개는 분자에서 제외한다. 기존 논문의 다른 호스트·고정판 및 동일 Nav2 Collision Monitor 설명은 새 출처에 중복 계상하지 않았다.

[^n1]: Jeremy A. Marvel, Rick Norcross, Implementing speed and separation monitoring in collaborative robot workcells, RCIM44(2017)144–155; DOI10.1016/j.rcim.2016.08.001; 승인2016-08-01 [C01 원문](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=914783). 접근일2026-10-11. 원문 열람(관련 본문/코드). 1차 연구; C02/C03와NIST계열

[^n2]: Martin Kidman/SICK, The perfect size of the protective field on an industrial autonomous vehicle;2021-02-09;블로그;DOI해당없음 [C05 원문](https://www.sick.com/ag/en/the-perfect-size-of-the-protective-field-on-an-industrial-autonomous-vehicle/w/blog-size-protective-field-industrial-autonomous-vehicle). 접근일2026-10-11. 원문 열람(관련 본문/코드). 제조사자체설명1차/표준요약2차;C04/C32와비독립

[^n3]: VDA/VDMA, Interface for the Communication between Mobile Robots and a Fleet Control,VDA5050tag3.0.0,2026-03;DOI해당없음 [C06 원문](https://github.com/VDA5050/VDA5050/blob/3.0.0/VDA5050_EN.md). 접근일2026-10-11. 원문 열람(관련 본문/코드). 1차명세;C10과VDA같은프로젝트

[^n4]: Open Navigation/Nav2,Collision Monitor Node,Jazzy문서snapshot2026-10-11,발행일미확인;DOI해당없음 [C07 원문](https://docs.nav2.org/jazzy/configuration_and_development/configuration_guide/core_servers/collision_monitor/configuring_collision_monitor_node/). 접근일2026-10-11. 원문 열람(관련 본문/코드). 1차구현설명;C08과동일Nav2

[^n5]: Open Navigation/Nav2,Speed Filter Parameters,Jazzy문서snapshot,발행일미확인;DOI해당없음 [C08 원문](https://docs.nav2.org/jazzy/configuration_and_development/configuration_guide/core_servers/costmap_2d/costmap_filters/speed_filter/). 접근일2026-10-11. 원문 열람(관련 본문/코드). 1차구현설명;C07과비독립

[^n6]: Open-RMF,rmf_ros2/FleetUpdateHandle.hpp 및cpp,tag2.14.0,commit7f7b247a618c22f76bf01ff0fb393f72317f6d9a,발행일미확인;DOI해당없음 [C09 원문](https://github.com/open-rmf/rmf_ros2/blob/2.14.0/rmf_fleet_adapter/src/rmf_fleet_adapter/agv/FleetUpdateHandle.cpp). 접근일2026-10-11. 원문 열람(관련 본문/코드). 1차구현;RMF프로젝트.논문C11/C18은RMF를이용하지만이코드의독립검증은아님

[^n7]: Seth Farrell, Chenghao Li, Hongzhan Yu, Ryo Yoshimitsu, Sicun Gao, Henrik I. Christensen. Safe Human Robot Navigation in Warehouse Scenario. 인용 본문 arXiv2503.21141v1 (2025-03-27); 출판 2025 IEEE 21st CASE, UC 공식 저장소 발행일2025-08-17, DOI10.1109/CASE58245.2025.11164151. arXiv DOI10.48550/arXiv.2503.21141. 출판 서지 확인: [UC 공식 PDF 표지](https://escholarship.org/content/qt389877j0/qt389877j0.pdf). [C11 원문](https://arxiv.org/html/2503.21141v1). 접근일2026-10-11. 원문 열람(관련 본문/코드). 1차실험;UCSD/IHI,지원IHI.동논문미러는1개

[^n8]: Maryam Kazemi Eskeri,Ville Kyrki,Dominik Baumann,Tomasz Kucner,Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments;arXiv2508.19731v1;IROS2025게재2025-11-27;DOI10.1109/IROS60139.2025.11246701. 출판 서지 확인: [Aalto 공식 목록](https://research.aalto.fi/en/publications/efficient-human-aware-task-allocation-for-multi-robot-systems-in-/). [C12 원문](https://arxiv.org/html/2508.19731v1). 접근일2026-10-11. 원문 열람(관련 본문/코드). 1차시뮬레이션;Aalto저자계열,미러1개

[^n9]: Robert Valner,Houman Masnavi,Igor Rybalskii,Rauno Põlluäär,Erik Kõiv,Alvo Aabloo,Karl Kruusamäe,Arun Kumar Singh,Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test;Front.Robot.AI9,2022-08-23;DOI10.3389/frobt.2022.922835 [C18 원문](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full). 접근일2026-10-11. 원문 열람(관련 본문/코드). 1차현장연구,UniversityofTartu/scafld;코드·Zenodo는동계열

[^n10]: Cristiana Rondoni, Francesco Scotto di Luzio, Christian Tamantini, Nevio Luigi Tagliamonte, Marcello Chiurazzi, Gastone Ciuti, Loredana Zollo. Navigation benchmarking for autonomous mobile robots in hospital environment. Scientific Reports14:18334,2024-08-07; DOI10.1038/s41598-024-69040-z. [C19 원문](https://www.nature.com/articles/s41598-024-69040-z). 접근일2026-10-11. 원문 열람(관련 본문/코드). 1차실물모사병원연구;C18다른연구팀,그러나동일안전효과재현아님

[^n11]: Alireza Jafari,Hong-Son Nguyen,Yen-Chen Liu,Empirical Prediction of Pedestrian Comfort in Mobile Robot Pedestrian Encounters;arXiv2604.13677v1,2026-04-15;DOI10.48550/arXiv.2604.13677;게재지미확인 [C20 원문](https://arxiv.org/html/2604.13677v1). 접근일2026-10-11. 원문 열람(관련 본문/코드). 1차프리프린트실험,독립테스트셋없음;서로다른사람실험과범위대조가능

[^n12]: 산업통상부,실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시,2025-21호,2025-11-24발령·시행;최종게시글64952. 시행일은 [국가법령정보센터 목록](https://law.go.kr/admRulLsInfoP.do?admRulSeq=2100000269426&chrClsCd=) L11에서 확인. [C21 원문](https://www.motir.go.kr/kor/article/ATCL0c554f816/64952/view). 접근일2026-10-11. 원문 미열람(공식 목록/공고 메타데이터만 확인). 1차공식고시메타데이터;C22~25와같은제도계열

[^n13]: 지능형 로봇 개발 및 보급 촉진법 시행규칙,산업통상부령1호,시행2025-10-01;제7조의2~6관련조문 [C22 원문](https://law.go.kr/LSW/lsLinkCommonInfo.do?lspttninfSeq=183075). 접근일2026-10-11. 원문 열람(관련 본문/코드). 1차법령;C21/24/25와같은법체계

[^n14]: ISO/FDIS13482,Robotics—Safety requirements for service robots,edition2,stage50.20(2026-09-15),개발중;DOI해당없음 [C26 원문](https://www.iso.org/standard/83498.html). 접근일2026-10-11. 원문 미열람(공식 목록/공고 메타데이터만 확인). 1차공식목록,ISO/TC299;C27과동계열

[^n15]: ISO13482:2014,Robots and robotic devices—Safety requirements for personal care robots,edition1,2014-02,current표시,90.92개정예정 [C27 원문](https://www.iso.org/standard/53820.html). 접근일2026-10-11. 원문 미열람(공식 목록/공고 메타데이터만 확인). 1차공식목록,ISO/TC299;C26동계열

[^n16]: KS B8252,실내 이동로봇의 보호정지 시험방법,현재상세페이지이력2025-09-05확인;최초판상세URL [C30 원문](https://www.kssn.net/search/stddetail.do?itemNo=K001010127949). 접근일2026-10-11. 원문 미열람(공식 목록/공고 메타데이터만 확인). 1차목록,국내시험표준계열

[^n17]: Emily Esposito Fulkerson/Amazon,Ever wonder how people and robots team up on your Amazon order?,발행일미확인 [C33 원문](https://www.aboutamazon.com/news/operations/ever-wonder-how-people-and-robots-team-up-on-your-amazon-order). 접근일2026-10-11. 원문 열람(관련 본문/코드). 1차기업공식사례,Amazon자기보고

[^n18]: Andreas Vatistas, Nikolaos Lappas 유지관리. human_detection_fusion README, docs/02_interfaces.md, src/yolo_uwb_fusion_node.cpp. commit934ca8387a205aaac894da22451970a203777e18,2026-06-29T19:36:27Z; KIRO/ARISE/ATHENA RC/IKNOWHOW; DOI해당없음. [C35 원문](https://github.com/nikolaslps/human_detection_fusion/blob/934ca8387a205aaac894da22451970a203777e18/src/yolo_uwb_fusion_node.cpp). 접근일2026-10-11. 원문 열람(관련 본문/코드). 1차공개프로젝트,KIRO/IKNOWHOW/ATHENARC같은사업계열

[^n19]: Johnata Brayan, Sihao Deng, Armando Alves Neto, Iaroslav Okunevich, Tomas Krajnik, Francois Bremond, Zhi Yan. NavWareSet: A Dataset of Socially Compliant and Non-Compliant Robot Navigation. 프로젝트 사이트; 연결 논문 IJRR2026, DOI10.1177/02783649261447305(프로젝트 BibTeX), 정확 발행일 미확인; 권호0(0)는 임시 서지이므로 확정 권호로 사용하지 않음. [C41 원문](https://anr-navware.github.io/navwareset/). 접근일2026-10-11. 원문 열람(관련 본문/코드). 1차데이터프로젝트,NavWare;논문/사이트비독립

[^n20]: ISO,ISO10218-1:2025,Robotics—Safety requirements—Part1:Industrial robots,edition3,2025-02,이력발행2025-02-05 [C44 원문](https://www.iso.org/standard/73933.html). 접근일2026-10-11. 원문 미열람(공식 목록/공고 메타데이터만 확인). 1차공식목록;ISO/TC299,관련A3해설과작업계열중복

## 부록 A. 1단계 진단표와 조사 질문

### M-49 1단계 진단 — 2026-10-11

검색 전에 해당 `05_M-49_prompt.md`, 현재 위키 본문(version2,2026-09-30)과 절 분리 **7페이지(s3,s4,s6,s7,s8,s10,s11)**를 끝까지 읽었다. HTML과 article 본문만 추출한 txt를 보존했다. 초기 HTML에는 사이트 전체 탐색 메뉴가 포함돼 있었으므로 article 범위로 다시 추출했다. 다른 영역을 조사한 것이 아니다. 이 단계의 표는 조사할 지점을 식별하며 원문의 사실 여부에 대한 결론은 아니다.

현재페이지: https://mjkim84.github.io/ai-hub/categories/safety/human-proximity-safety/
분리페이지: `topic-links.json`에 정확한7URL을 기록했다. 모든 접근 성공.

## 약한 주장 진단표

긴 위키 문장의 반복 전재를 피하기 위해 짧은 원문 구절과 위치·주장 식별을 함께 적는다. **원문 문장 전체는 아래 지정한 txt의 해당 절에 그대로 보존**되어 있다. 본문과 분리페이지에서 반복되는 같은 주장은 한 번만 진단한다. W번호는 이번 조사에서 부여한 작업 ID다.

|ID|위키 위치·주장 식별(짧은 인용만 따옴표)|약한 이유·확인할 근거|
|---|---|---|
|W01|본문3/s3: 정지성능·센서갱신에따라안전거리달라짐|추정;2016고정작업셀식과이동로봇반응체계의조건구분|
|W02|s3: 로봇종류별표준·법규가속도/구역결정|추정;각규격범위와규범요구분리|
|W03|s3/s7: 국내울타리면제|2024기사만,법령원문미확인;개별적용법률추론금지|
|W04|s3: 보수적정지의처리량·수용성영향|서로다른연구의종합추론;효과측정범위와분모필요|
|W05|s3: 편안함과안전정지거리의별도기준|추정;실증참가자/조건·지표정의필요|
|W06|본문4/s4: ISO/TS15066 SSM 안전감시정지|2016논문하나;현행규격본문과논문판구분|
|W07|s4/s6: 보호분리거리구성요소·접근속도|NIST원문한출처,2016조건;ISO13855구판값을일반AMR속도상한으로오인하지않기|
|W08|s4/s7: ISO3691 운용·제한·사람배제구역|검색요약·원문미확인;공식범위이상주장의증거부족|
|W09|s4: PFL/HGC/SSM분류|2024기사근거추정;규격/공식해설필요|
|W10|s4/s6: VDA구역유형·속도제한|main링크;3.0.0고정본문·스키마·준수조건및적용확인경로필요|
|W11|s4/s6: MoD로사람영향비용추정|HATA단일논문;과거통계예측과실시간사람감지구분|
|W12|본문5: Amazon조끼시작·자원·감속/경로변경/정지|여섯항목중다수가벤더주장,속도·거리·재개·처리량미확인|
|W13|본문5/s6: Farrell CBF·Open-RMF|논문한출처,정량결과미확인;시뮬레이션/실물·대수·안전성제약조건필요|
|W14|본문5: HOSBOT/TIAGo의0.2·0.6·1.0m/s와7지표|단일모의병원연구;실물환자혼재운영과다름.안전기준속도처럼서술하지않기|
|W15|본문5: “감속 속도·거리 값은 미확인이다.”|벤더공식매뉴얼/시험규격/운영조건추적|
|W16|본문5/s7: 국내실외500kg·15km/h·2년점검|기관안내기준;현행고시·별표·시행일과대상조건확인|
|W17|본문5: 질량구간230/100kg·5/10/15km/h|2023기사의당시개정안;최종고시·최근개정원문확인필수|
|W18|본문5: 횡단보도도착후다음신호대기|2023기사의개정안;현재규정의예외·조건확인필요|
|W19|본문5/s11: 심사항목8과16충돌|항목계층·판·대상시험차이확인|
|W20|본문5: 제조·상업·가정현장근접안전사례공백|현장명/구성/제조사/혼재인구/운영결과명시한1차자료필요|
|W21|s6: NIST0.113초·850/1200mm·1600/2000mm/s|특정장치·표준판·접근방향조건누락가능성,원문수치/표확인|
|W22|s6: Nav2영역겹침에서가장강한조치|고정코드·센서타임아웃·속도전달경로·실제범위확인|
|W23|s6: VDA비안전규격성명→안전기능대체불가|원문의범위설명과설계추론을한사실문장에합침;분리필요|
|W24|s6: HATA최대26%·19%향상|기준선·실험환경·팀규모·시나리오별분모미명시|
|W25|s6: 편안함복합지표오즈비3.67|참가자수·장소미확인;신뢰구간·반복측정·대상인구필요|
|W26|s7: ISO10218이15066을 “선택적 지침에서 규범적 요구”로통합|프리프린트해석한출처;발행기관원문/공식해설로대조,모바일부범위구별|
|W27|s7: 0.3m/s·원통시험편200×600/70×400mm|표준본문미열람,검색요약으로수치제시;원문없으면보류|
|W28|s7: R15.08통합자책임·정보교육|기사의표준요약;M48에서확인한서지를복사해독립출처로세지않기|
|W29|s8: 사회적주행8원칙·저자수·학술지판|정확서지/판/평가권고와안전규범을구분|
|W30|본문9: 구역·시간대별ROP제어범위|모든책임행추정;제품별인터페이스와현장주체에근거필요|
|W31|본문9: 실외인증관제장치와ROP범위겹침|인증대상조합에서플랫폼범위로추론;공식정의·변경/원격개입조건필요|
|W32|본문9: 인증적합성은운영사업자몫|위키가추론이라고명시;신청인·책임주체의공식원문필요|
|W33|s10: 다른영역연결16건|대부분설계추정;연결표로만유지,다른영역심화금지|

## 1~13절 공백

|절|공백/유지 판단|
|---|---|
|1|정의충분.새정의작성불필요|
|2|거리·감속·정지질문은있으나로컬안전경로와플릿정책관계명확화필요|
|3|구판SSM값과표준/법규요약에의존;인식실패·불확실성·취약보행자근거얕음|
|4|개념은있으나MoD예측·실시간감지·안전등급검출의구별공백|
|5|창고벤더·병원시뮬레이션·실외제도사례뿐.실물혼재운영과재개/장애조건부족|
|6|알고리즘/프로토콜소개는충분.지연·사람데이터소실·명령적용확인·플릿혼잡입력계약부족|
|7|ISO13482현재판/개정상태누락;ISO10218모바일부범위와실외최종고시부족|
|8|정량주장여러개에분모·실물여부·참가자조건미확인.실패·한계연구부족|
|9|책임범위대부분추정.인증관제장치·안전기능소유자·운영정책주체구별필요|
|10|16연결은충분.영역넘침억제|
|11|질문4개,원문oq-id없음.국내실내기준과외부사람신호이종플릿전달증거공백|
|12|최종작성2026-09-30.최근1년규격·국내인증변경확인필요|
|13|main링크/표준미열람/발행일미확인여럿.고정판과공식원문필요|

## 열린 질문 4개

원문은 `2026-09-30-area49-s11.txt`의3.본문에보존. 원문에oq-id는없다. 아래OQ1~OQ4는로컬식별자다. 긴문장인용대신원문식별구절과의미를기록한다.

|ID|원문 식별 구절|질문 의미|조사 질문|
|---|---|---|---|
|OQ1|“누가 검증하는가?”|관제소프트웨어의구역/속도제한을로봇보호필드와정합하고위험감소조치로검증하는주체/조건|Q1·Q2·Q7|
|OQ2|“8개 항목” / “16가지”|국내운행안전인증의항목계층·세부목록과현재규칙|Q5|
|OQ3|“사람 근접 속도·거리 기준”|국내병원/상업/공동주택실내서비스로봇의관련법규·표준·인증|Q6|
|OQ4|“여러 로봇 플릿에 동시에 전달”|착용장치·출입신호에서얻은사람위치를이종플릿에전달해감속/정지시키는인터페이스/사례|Q7|

## 2025년 이전 정보 후보

NIST SSM2016/ISO13855의당시값,ISO/TS15066:2016,ISO3691-4:2023,R15.08-2:2023,실외인증2023기사개정안,울타리2024기사,병원벤치마크2024. ISO13482는본문에없어현행판/개정상태를새로확인한다. 오래되었다는이유만으로폐지/오류라고판단하지않는다.

## 우선 조사 질문과 답변 기준

|번호|질문|답한 것으로 볼 근거|
|---|---|---|
|Q1|SSM의거리·반응/정지시간·센서오차를관제와로봇안전경계에어떻게연결하는가?|NIST원문·현행규격/공식해설·제조사안전문서에서식의가정과장치별조건,감지실패/지연처리확인|
|Q2|VDA구역·Nav2속도필터·RMF의속도/진입제어는무엇을보장하고어떻게적용확인하는가?|고정명세·코드·메시지·변경이력에서속도단위/구역겹침/해제/타임아웃/확인경로추적;안전인증과분리|
|Q3|CBF창고주행과HATA의사람고려기법은어떤규모·조건에서무엇을개선했는가?|원논문판·실험장치/시뮬레이터·로봇/사람수·기준선/분모·실패조건·공식코드확인|
|Q4|병원·상업시설실제혼재운영과편안함연구는안전거리/속도설계에어떤근거를주는가?|현장1차문서·원연구의참가자/장소·실물/시뮬레이션·지표/한계·독립성확인|
|Q5|국내실외운행인증의현행보행자/속도/질량/횡단조건과8/16항목차이는?|현행고시·별표·기관시행문서의판/시행일·항목계층확정;2023안과2025-10~2026-10개정분리|
|Q6|ISO10218:2025와ISO13482의범위·개정상태,국내실내기준은?|발행기관의현행판/개발단계·모바일머니퓰레이터이동부범위·국내표준/공식기준;법률적용해석금지|
|Q7|외부사람위치/착용장치/출입신호를이종플릿감속·정지에연결한증거와한계는?|제조사공식인터페이스/현장배치/공개구현과안전성검증주체·통신소실조건;벤더주장은추정|
|Q8|아동·휠체어사용자등취약보행자와감지실패를플릿근접안전에어떻게평가하는가?|원실험/데이터셋·접근성공식안내·검출오류/가림/불확실성·시나리오의표본과한계확인|

다음2단계는각질문을3개이상의서로다른관점에서검색하고서로다른후보5개이상을수집한다. 아직검색결론이나최종출처선정은하지않았다.

## 부록 B. 검색 기록

### M-49 2단계 검색 기록

검색일2026-10-11. 건진수는이검색에서채택한서로다른후보문서수이며,동일문서재발견은같은ID다. 무관결과/미러/후보미채택은0으로기록. 질문당관점3개이상과후보5개이상은별도로점검한다.

|관점|검색어|날짜|건진출처수|후보|
|---|---|---|---:|---|
|Q1a ① 표준·공공 연구|site.nist.gov speed separation monitoring ISO 13855 2024 robot reaction time|2026-10-11|2|C01,C02|
|Q1b ④ 제조사 안전 구현|site.sick.com mobile robot protective field stopping distance sensor response safety|2026-10-11|2|C04,C05|
|Q1c ⑥ 학술 한계|speed separation monitoring mobile robot sensor latency occlusion safety limitations study|2026-10-11|2|C01,C03|
|Q2a ① 인터페이스 명세|site.github.com/VDA5050/VDA5050 3.0.0 zones SPEED_LIMIT zoneSetId|2026-10-11|2|C06,C10|
|Q2b ② 로컬 공개 구현|site.docs.nav2.org speed filter collision monitor source_timeout stop_pub_timeout|2026-10-11|1|C07|
|Q2c ⑥ 플릿 구현 한계|site.github.com/open-rmf speed_limit lane closure request fleet adapter|2026-10-11|1|C09|
|Q3a ③ 학술 원문|"Safe Human Robot Navigation in Warehouse Scenario" "Efficient Human-Aware Task Allocation"|2026-10-11|0|없음|
|Q3b ② 연구 공개 구현|"Safe Human Robot Navigation" github OR "human-aware task allocation" github|2026-10-11|0|없음|
|Q3c ⑥ 검증·실패 비교|social navigation control barrier function safety evaluation robot pedestrian limitations benchmark|2026-10-11|3|C13,C14,C15|
|Q4a ④ 실물 운영|site.cordis.europa.eu hospital robot navigation people deployment THOMAS SQUIRREL STRANDS|2026-10-11|2|C16,C17|
|Q4b ③ 실험 원문|"Empirical Prediction of Pedestrian Comfort" OR "Navigation benchmarking for autonomous mobile robots in hospital"|2026-10-11|0|없음|
|Q4c ⑥ 현장 한계|hospital service robot deployment patient pedestrian navigation safety failure field study|2026-10-11|1|C18|
|Q5a ① 현행 법령|실외이동로봇 운행안전인증 기준 고시 2026 2025 별표 속도 질량|2026-10-11|4|C21,C22,C23,C43|
|Q5b ⑤ 인증기관 시행|site.kiria.org 운행안전인증 16 8 심사 항목 2026|2026-10-11|0|없음|
|Q5c ④ 시험·산업 한계|실외이동로봇 안전인증 횡단보도 보행자 시험 관제장치 2025 2026|2026-10-11|1|C43|
|Q6a ① 표준 현황|site.iso.org "13482" "2026"|2026-10-11|2|C26,C27|
|Q6b ④ 통합자 공식 설명|site.automate.org ISO 10218 2025 mobile manipulator mobile platform FAQ|2026-10-11|1|C28|
|Q6c ⑤ 국내 실내 기준|실내 서비스 로봇 안전 표준 KS 13482 병원 속도 거리 인증|2026-10-11|3|C29,C30,C31|
|Q7a ④ 제조사 인터페이스|robot safety wearable vest pedestrian location multi robot fleet safety system SICK|2026-10-11|2|C32,C34|
|Q7b ② 공개 구현|human position detection fleet robot speed limit wearable UWB github ROS2|2026-10-11|1|C35|
|Q7c ⑥ 안전성 검증|wearable worker detection mobile robot safety communication failure industrial risk assessment study|2026-10-11|1|C36|
|Q8a ③ 취약 보행자 연구|robot navigation wheelchair blind pedestrians children safety detection study 2025 2026|2026-10-11|0|없음|
|Q8b ② 데이터·벤치마크|social robot navigation benchmark dataset wheelchair occlusion pedestrian failure|2026-10-11|3|C37,C38,C41|
|Q8c ⑤ 접근성·공식 한계|보행 로봇 시각장애인 휠체어 보행 안전 실험 2025 2026|2026-10-11|0|없음|
|Q3d ③ 단일 논문 검색|"Safe Human Robot Navigation in Warehouse Scenario"|2026-10-11|1|C11|
|Q3e ② 저자·공개 구현 추적|"Efficient Human-Aware Task Allocation" github|2026-10-11|1|C12|
|Q4d ③ 편안함 원연구|"Empirical Prediction of Pedestrian Comfort"|2026-10-11|1|C20|
|Q4e ③ 병원 벤치마크 원연구|"Navigation benchmarking for autonomous mobile robots in hospital environments"|2026-10-11|1|C19|
|Q2d ② 구역별 속도 구현|site.docs.nav2.org speed filter absolute percentage speed_limit|2026-10-11|1|C08|
|Q5d ⑤ 최근 제도·공식 발표|site.motie.go.kr 실외이동로봇 운행안전인증 2025 고시 개정|2026-10-11|4|C21,C22,C24,C25|
|Q7d ④ 착용장치 현장|site.aboutamazon.com robotics tech vest safety robots|2026-10-11|1|C33|
|Q8d ⑥ 취약 보행자·공동 공간|delivery robots sidewalk accessibility blind wheelchair pedestrians study|2026-10-11|1|C39|
|Q8e ⑥ 아동·실패 실험|social navigation robot children blocking abuse field study pedestrians|2026-10-11|2|C39,C40|
|Q8f ③ 휠체어 사용자와 다른 로봇의 공동 공간|"wheelchair users" "robots" "navigation" social|2026-10-11|1|C42|

누적검색34회. Q3a/Q3b/Q4b는복합검색어로대상논문을얻지못해0건으로남기고Q3d/e·Q4d/e의개별검색으로보완했다. Q8c국내검색은무관결과로0건. Q5b제품공표목록은현재질문의심사기준근거로채택하지않았다. 검색시도와원문열람은구별한다.

최근1년추적후보: ISO13482 FDIS상태, ISO10218관련2026공식설명,실외운행고시2025-11예고/최종개정,2026편안함·NavWareSet·휠체어사용자연구. 크롤링일을발행일로쓰지않는다.

### 3단계 원문 복구·적용범위 후속 검색

2단계검색34회와구분한다. 후속검색은같은영역의출처원문·정확서지확인용. 다른영역검색없음. 날짜2026-10-11. 건진수는기존후보를포함한관련문서수,새후보는C44하나. 원문복구미러는추가출처로세지않는다.

|ID/관점|검색어|날짜|건진 출처 수|결과|
|---|---|---|---:|---|
|S3-01 ① 최종 고시|"실외이동로봇" "2025-21" 고시|2026-10-11|1|기존C21공식공고목록재발견.민간법령미러결론제외|
|S3-02 ① 최종 고시|"실외이동로봇" "2025-021" 별표|2026-10-11|1|C21산업통상부목록→게시글64952→첨부추적.별표전문미확보|
|S3-03 ① 원문 경로|"2100000269426"|2026-10-11|1|C21/LSW경로는UI껍데기,full-C21b.txt|
|S3-04 ⑥ 접근성 현장|"Sharing the Sidewalk" robots accessibility arxiv|2026-10-11|0|관련원문확보못함. search-stage3-followup.json|
|S3-05 ⑥ 아동 현장|"Why do children abuse robots" pdf Nomura Kanda|2026-10-11|1|C40저자목록/미러.다른판HRI2015초록을2016저널전문으로사용안함|
|S3-06 ① 표준 원문|"ISO 10218-1:2025" "mobile" site.iso.org|2026-10-11|0|이배치에서관련원문추가확보못함.후속S3-07로좁힘|
|S3-07 ① 표준 범위|site.iso.org/standard "10218-1:2025" "mobility"|2026-10-11|1|C44추가,공식목록직접열람성공. open-C44.txt|
|S3-08 ① 표준 범위|site.iso.org/standard "10218-2:2025" "mobile"|2026-10-11|1|기존GSOpart2preview재발견.실제open은목차만|
|S3-09 ⑤ 인증기관|site.kiria.org/portal/cert/portalCertEstiSafe.do "8"|2026-10-11|0|기존모바일경로도실패. open-C23mobile/open-C23indexed|

후속검색원문은search-stage3-followup.json/search-stage3-scope-legal.txt,고시공식공고문은full-C21-ministry.txt에저장. 최초S3-01~03의검색raw는별도저장못했으나찾은공식페이지를직접열어저장했다. 검색시도와원문열람을구분한다.

C21첨부경로: https://www.motir.go.kr/attach/down/debc2e19d8870bf491bf5e73464259e8/6dffff5145483aa2d1fa6667594d076e/9a9db098b587ee18b321c826f3707a49 . application/octet-stream웹도구미지원,viewer0행. HWPX내부를읽었다고표시하면안됨.

일반curlDNS실패,권한확대정책거절. 같은요청을반복하지않고지원되는웹원문/기존출처캐시로진행했다.

## 부록 C. 출처 평가표

### M-49 3단계 출처 평가 — 최종

2026-10-11. 후보44개 모두 원 URL 접근을 시도했으며 성공한 접근과 실제 관련 본문 정독을 구분했다. 최종20개 중 관련 원문 정독15개(75%). 공식 목록/공고 메타데이터5개는 분자에서 제외했다. 전체 논문/전체 표준을 모두 읽었다는 의미가 아니다. 실패한 출처는 결론에서 제외한다. 채택된 단독 기업 설명은 추정으로만 사용한다.

|ID / 결정|서지·판·날짜|열람 상태·위치|1차/2차·독립성|신뢰도·범위·선정 사유|
|---|---|---|---|---|
|C01 / 채택|Jeremy A. Marvel, Rick Norcross, Implementing speed and separation monitoring in collaborative robot workcells, RCIM44(2017)144–155; DOI10.1016/j.rcim.2016.08.001; 승인2016-08-01|원문 관련 절 열람: NIST공식PDF, full-C01/read-C01-reaction; §5~6/P7|1차 연구; C02/C03와NIST계열|high: 관련 원문 정독 완료. 장치 반응시간과 위치 불확실성에 한정 채택. 식 전체 및 침입거리의 현행 규범 해석은 채택하지 않음.|
|C02 / 제외|Sandor S. Szabo, William P. Shackleford, Richard J. Norcross, Jeremy A. Marvel, A Testbed for Evaluation of Speed and Separation Monitoring in a Human Robot Collaborative Environment; NISTIR7851;2012-03-29; DOI10.6028/NIST.IR.7851|원문 미열람(초록만), open-C02 L115–155|1차연구의공식서지;C01/C03와같은NIST연구계열|제외 — 초록만 확보. C01과 동일 연구계열이며 추가 수치 채택 안 함. 기존 접근 평가: low: 현재는실험수치근거불가. 원문추가열람또는제외|
|C03 / 제외|William P. Shackleford, Sandor S. Szabo, Richard J. Norcross, Jeremy A. Marvel, Integrating Occlusion Monitoring into Human Tracking for Robot Speed and Separation Monitoring; PerMIS2012; 행사2012-03-20~22, NIST게시05-16; DOI미확인|공식6쪽PDF확보, 관련본문정독대기. full-C03|1차연구;C01/C02와연구팀중복|제외 — 원문 PDF 접근 성공, 정독 보류. 동일 NIST 계열 추가문헌보다 채택된 장치 지연 근거에 범위를 제한. 기존 접근 평가: medium잠정:가림문제추적후보. 아직결론인용금지|
|C04 / 제외|SICKAG, TiM7xxS Operating Instructions,8023886/1XPS/2026-07-29,112PDF쪽;DOI해당없음|원문PDF열림,표지·목차확인;제품안전관련절정독대기. open-C04|1차제조사매뉴얼;C05/C32와같은SICK|제외 — 매뉴얼 접근 성공, 안전기능 절 정독 안 함. 특정 센서 제품의 인증범위는 이번 결론에서 제외. 기존 접근 평가: medium잠정:제품한정안전기능/제약. 제조사기술주장[추정],정독전채택불가|
|C05 / 채택|Martin Kidman/SICK, The perfect size of the protective field on an industrial autonomous vehicle;2021-02-09;블로그;DOI해당없음|원문열람,open-C05 본문L4–149|제조사자체설명1차/표준요약2차;C04/C32와비독립|medium:응답시간·하중·환경고려.표준shall/실효성독립검증근거아님|
|C06 / 채택|VDA/VDMA, Interface for the Communication between Mobile Robots and a Fleet Control,VDA5050tag3.0.0,2026-03;DOI해당없음|원문관련명세열람,C06-spec.md §6.4·actions·state;웹raw도확보. M48동일태그캐시재사용기록존재|1차명세;C10과VDA같은프로젝트|high:zone지원범위·속도단위·활성화계약.일반안전인증으로확대금지|
|C07 / 채택|Open Navigation/Nav2,Collision Monitor Node,Jazzy문서snapshot2026-10-11,발행일미확인;DOI해당없음|원문관련절열람,open-C07 L543–630|1차구현설명;C08과동일Nav2|high:CPU/인증미제공·timeout설명.고정코드판과URL문서동일시금지|
|C08 / 채택|Open Navigation/Nav2,Speed Filter Parameters,Jazzy문서snapshot,발행일미확인;DOI해당없음|원문열람,open-C08 L444–494|1차구현설명;C07과비독립|high:0=제한없음,상대/절대값,mask변환,Controller연결.하드웨어안전성추론금지|
|C09 / 채택|Open-RMF,rmf_ros2/FleetUpdateHandle.hpp 및cpp,tag2.14.0,commit7f7b247a618c22f76bf01ff0fb393f72317f6d9a,발행일미확인;DOI해당없음|원문관련코드열람.현재웹URLcachemiss후M48동일태그캐시확보.C09-FleetUpdateHandle.hpp 235–266/cpp2232–2315|1차구현;RMF프로젝트.논문C11/C18은RMF를이용하지만이코드의독립검증은아님|high:planner속도제약/0이하거절/해제.로봇속도준수ACK·실제급정지는이코드만으로확인불가|
|C10 / 제외|ConstantinUp,VDA5050issue641,Question on Table8 - Interaction matrix for zones;2026-07-31;열람시Open,3.0.1milestone|원문열람,open-C10 L141–177|1차프로젝트이슈;C06과비독립|제외 — 상호작용 질의는 LINE_GUIDED/BIDIRECTED이며 SPEED_LIMIT 고장 증거가 아님. 최종 보완과 직접 관련 약함. 기존 접근 평가: medium:질의존재만.배포결함확정·SPEED_LIMIT미동작이라고쓰지않음|
|C11 / 채택|Seth Farrell, Chenghao Li, Hongzhan Yu, Ryo Yoshimitsu, Sicun Gao, Henrik I. Christensen. Safe Human Robot Navigation in Warehouse Scenario. 인용 본문 arXiv2503.21141v1 (2025-03-27); 출판 2025 IEEE 21st CASE, UC 공식 저장소 발행일2025-08-17, DOI10.1109/CASE58245.2025.11164151. arXiv DOI10.48550/arXiv.2503.21141.|원문§IV~VII열람,full-C11/read-C11-end|1차실험;UCSD/IHI,지원IHI.동논문미러는1개|medium: 실물 연구 조건과 Table IV의 RMF 정지시간 제외를 명시. 최종 서지는 UC 공식 PDF 표지에서 확인, 본문 근거는 판 고정 arXiv v1과 구분.|
|C12 / 채택|Maryam Kazemi Eskeri,Ville Kyrki,Dominik Baumann,Tomasz Kucner,Efficient Human-Aware Task Allocation for Multi-Robot Systems in Shared Environments;arXiv2508.19731v1;IROS2025게재2025-11-27;DOI10.1109/IROS60139.2025.11246701|원문§IV~VI열람,full-C12a/read-C12-end.출판서지는Aalto확인;출판PDF403|1차시뮬레이션;Aalto저자계열,미러1개|medium:실측사람궤적재생시뮬레이션.26/19%집계분모재현미완료,실제안전효과주장불가|
|C13 / 제외|SocialZoneCBF;arXiv2405.15101.정확제목·저자·판·발행일·출판DOI추가확인전|열람실패(UnexpectedStatusCode),open-C13|1차논문후보,독립성미평가|제외 — 원문 접근 실패. 검색 요약으로 결론을 쓰지 않음. 기존 접근 평가: low:현재결론근거제외. 필요시HTML/PDF한번추적|
|C14 / 제외|Abhijat Biswas,Allan Wang,Gustavo Silvera,Aaron Steinfeld,Henny Admoni,SocNavBench: A Grounded Simulation Testing Framework for Evaluating Social Navigation;CMU목록2021-08;ACMTHRI;DOI10.1145/3476413;권호추가확인|원문미열람(초록만),open-C14|1차연구공식서지;CMU,광범위가이드C15저자중복추가확인|제외 — 초록만 열람. 코드/논문 본문 미검토, 성능 근거 제외. 기존 접근 평가: low:초록으로벤치마크성능인용금지.코드/본문확보또는제외|
|C15 / 제외|Anthony Francis 외,Principles and Guidelines for Evaluating Social Robot Navigation Algorithms;arXiv2306.16740v4,2023-09-19;DOI10.48550/arXiv.2306.16740;2025THRI판별도확인필요|원문미열람(초록·서지만),open-C15|1차합의/방법론논문;다기관,다른사회주행연구와저자중복가능|제외 — 기존 위키 방법론과 중복. 초록만 확보한 상태에서 새 보완으로 부풀리지 않음. 기존 접근 평가: low현재:위키기존출처,추가근거필요없으면중복제외|
|C16 / 제외|European Commission/CORDIS,HARMONY,Assistive robots redefine routine hospital care;정확게시일추가확인;DOI해당없음|본문확보(www제외URL복구),full-C16;정독대기|프로젝트공식성과소개1차자기보고/기사형식2차;HARMONY|제외 — 공식 성과기사 접근 성공이나 추가 정독 안 함. 실제 혼재 운영 분모는 C18 원논문으로 좁혀 다룸. 기존 접근 평가: medium잠정:독립현장성능시험아님.정독전결론보류|
|C17 / 제외|European Commission/CORDIS,Socially Pertinent Robots in Gerontological Healthcare,project871245(SPRING),reporting;정확보고기간추가확인;DOI해당없음|본문확보,open-C17;정독대기|1차프로젝트보고,SPRING자체성과|제외 — 보고 페이지 확보, 상세 정독 안 함. 프로젝트 성과 소개를 독립 현장 검증으로 세지 않음. 기존 접근 평가: medium잠정:계획/실적/한계구분후판단|
|C18 / 채택|Robert Valner,Houman Masnavi,Igor Rybalskii,Rauno Põlluäär,Erik Kõiv,Alvo Aabloo,Karl Kruusamäe,Arun Kumar Singh,Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test;Front.Robot.AI9,2022-08-23;DOI10.3389/frobt.2022.922835|원문§2~4열람;read-C18-results L459–489핵심|1차현장연구,UniversityofTartu/scafld;코드·Zenodo는동계열|high:실제병원TIAGo시연과시험장이종2대분리.장기간상시운영/사고율근거아님|
|C19 / 채택|Cristiana Rondoni, Francesco Scotto di Luzio, Christian Tamantini, Nevio Luigi Tagliamonte, Marcello Chiurazzi, Gastone Ciuti, Loredana Zollo. Navigation benchmarking for autonomous mobile robots in hospital environment. Scientific Reports14:18334,2024-08-07; DOI10.1038/s41598-024-69040-z.|원문방법·결과열람,open-C19/read-C19-method|1차실물모사병원연구;C18다른연구팀,그러나동일안전효과재현아님|high:실물모사환경/원격조종로봇장애물/선택시험속도.표준해설은원표준과충돌주의|
|C20 / 채택|Alireza Jafari,Hong-Son Nguyen,Yen-Chen Liu,Empirical Prediction of Pedestrian Comfort in Mobile Robot Pedestrian Encounters;arXiv2604.13677v1,2026-04-15;DOI10.48550/arXiv.2604.13677;게재지미확인|원문방법·통계·한계열람,full-C20/read-C20-end|1차프리프린트실험,독립테스트셋없음;서로다른사람실험과범위대조가능|medium:32명/원격조종/158및145분모.OR해석/표VIIprecision-recall불일치주의.단일안전성확률로해석금지|
|C21 / 채택|산업통상부,실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시,2025-21호,2025-11-24발령·시행;최종게시글64952|원문미열람(고시번호·시행상태·공식공고문만).law본문UI껍데기,첨부HWPX웹미지원,viewer0행|1차공식고시메타데이터;C22~25와같은제도계열|high메타데이터/low세부기준:별표3·신구비교미열람.본문열람률분자제외|
|C22 / 채택|지능형 로봇 개발 및 보급 촉진법 시행규칙,산업통상부령1호,시행2025-10-01;제7조의2~6관련조문|원문열람,open-C22 L82–98|1차법령;C21/24/25와같은법체계|high:500kg/15kmh상위기준과운행계획서요구.세부운행허용조건으로확대금지|
|C23 / 제외|한국로봇산업진흥원,실외이동로봇 운행안전인증 안내,발행일미확인;DOI해당없음|열람실패(timeout),open-C23/full-C23a/legal-retry|1차인증기관안내,국내인증제도계열|제외 — 기관 안내 원문 반복 접근 실패. 8/16항목 대조는 확인 못 함으로 남김. 기존 접근 평가: low:8항목문구·16항목대응은원문미확인.현재결론근거제외|
|C24 / 제외|지능형 로봇 개발 및 보급 촉진법,시행2025-10-01,lsiSeq276607;개정법률번호추가확인|원문미열람(UI껍데기),open-C24|1차법령후보,C21~25동일법체계|제외 — 공식 UI만 표시. 실질 조문 미확보이며 C22 확인 조문 이상으로 결론을 넓히지 않음. 기존 접근 평가: low:조문확인전실질결론제외|
|C25 / 제외|산업통상부,실외이동로봇 운행안전인증 절차 및 기준 등에 관한 고시 일부 개정안 행정예고,게시글70637;정확공고번호/일자추가대조필요|공고문확보,open-C25;첨부개정안미열람|1차행정예고;C21최종고시와동계열|제외 — 행정예고 공고문만 확보. C21 최종 고시 게시 상태와 구분하고 첨부 변경 내용은 보류. 기존 접근 평가: medium:예고와최종고시분리.최종변경내용은첨부대조전보류|
|C26 / 채택|ISO/FDIS13482,Robotics—Safety requirements for service robots,edition2,stage50.20(2026-09-15),개발중;DOI해당없음|원문미열람(공식목록/이력),open-C26|1차공식목록,ISO/TC299;C27과동계열|high:미발행승인단계·판정보만.새판요건확정인용금지|
|C27 / 채택|ISO13482:2014,Robots and robotic devices—Safety requirements for personal care robots,edition1,2014-02,current표시,90.92개정예정|원문미열람(공식목록/범위),open-C27|1차공식목록,ISO/TC299;C26동계열|high:판·범위메타데이터.20kmh제외범위를운행허용속도로변환금지|
|C28 / 제외|A3 Online Marketing Team,Updated ISO10218: Answers to Frequently Asked Questions(FAQs),2025-03-20,DOI해당없음|원문FAQ관련절열람,open-C28 L252–305. GSO별도preview는목차만|표준작업참여기관설명1차/표준본문대체로는2차;ISO10218작업계열|제외 — 해설은 표준 전문 아님. 모바일 범위는 C44 공식 공개 범위로 제한. 기존 접근 평가: medium:협동응용내용흡수설명.2026기사아님;mobilebase적용범위원문추적미완료|
|C29 / 제외|KS B ISO13482(2024확인),로봇 및 로봇 장치—개인 지원 로봇 안전 요구사항,2024-05-27확인,한국표준정보망|원문미열람(공식목록·범위),open-C29|1차공식목록;ISO13482국내채택계열|제외 — 카탈로그 범위만 확인, ISO13482 국내채택 정보와 중복. 실내 보호정지 범위는 C30으로 구체화. 기존 접근 평가: high:확인판/범위만.전문속도·거리·법적강제적용확인못함|
|C30 / 채택|KS B8252,실내 이동로봇의 보호정지 시험방법,현재상세페이지이력2025-09-05확인;최초판상세URL|원문미열람(공식목록·범위),open-C30 L229/244|1차목록,국내시험표준계열|high: 공개 범위와 이력만 채택. 2020 상세 페이지에서 2025-09-05 확인 이력을 확인했지만 확인판 전문은 미열람. 동적 보행자 거리나 법적 강제성 판단에 쓰지 않음.|
|C31 / 제외|KS B ISO/TR23482-2,로봇—KS B ISO13482의 적용—제2부:적용 지침;정확고시일추가확인|원문미열람(공식목록);intra실패후www복구,full-C31a|1차목록;13482적용지침으로C27/C29와비독립|제외 — 카탈로그만 확보. 적용 지침을 의무 속도 기준으로 확장하지 않고 중복 제외. 기존 접근 평가: medium:TR지침이며규범적일반속도기준으로전용금지|
|C32 / 제외|SICK,Safely designing mobile robots,e-guide;정확판/발행일미확인|열람실패(도구접근불가),open-C32|1차제조사문서후보;C04/C05같은기관|제외 — 원문 접근 실패. 결론 근거 제외. 기존 접근 평가: low:결론근거제외|
|C33 / 채택|Emily Esposito Fulkerson/Amazon,Ever wonder how people and robots team up on your Amazon order?,발행일미확인|원문관련본문열람,open-C33 L10–13|1차기업공식사례,Amazon자기보고|medium:[추정]으로vest감속·우회·근접정지주장한정.공통프로토콜/수치/PL확인못함|
|C34 / 제외|HaiRobotics,HaiSafety System,발행일미확인|공식본문확보,open-C34;상세정독대기|1차벤더문서,HaiRobotics계열|제외 — 벤더 페이지 확보, 상세 정독 안 함. 벤더 사례 수를 늘리지 않고 C33 한계와 C35 실제 공개 인터페이스를 비교. 기존 접근 평가: medium잠정:단독벤더주장,검증대상·인터페이스확인전보류|
|C35 / 채택|Andreas Vatistas, Nikolaos Lappas 유지관리. human_detection_fusion README, docs/02_interfaces.md, src/yolo_uwb_fusion_node.cpp. commit934ca8387a205aaac894da22451970a203777e18,2026-06-29T19:36:27Z; KIRO/ARISE/ATHENA RC/IKNOWHOW; DOI해당없음.|원문 열람: 고정 커밋 README·인터페이스·189행 소스 직접 정독. C35-fixed-0/1/2.txt 및 각 metadata.json. 소스29–40,61–64,81–96,99–178.|1차공개프로젝트,KIRO/IKNOWHOW/ATHENARC같은사업계열|high: 공개 코드의 입력/출력과 처리만. 시연 성능은 프로젝트 주장. 실행 시험·안전 인증·이종 플릿 동시 감속을 확인한 것은 아님.|
|C36 / 제외|DFKI,Wearable Sensor-Based Human Activity Recognition for Worker Safety in Manufacturing Line,publication15273;저자·게재지·일자추가확인|기관서지페이지확보,open-C36;전문미열람|1차연구의공식서지;DFKI저자계열확인필요|제외 — 서지 페이지만 확보, HAR 연구는 이종 AMR 감속 인터페이스 입증과 다름. 기존 접근 평가: low현재:착용센서HAR와이종AMR안전정지인터페이스는다른범위|
|C37 / 제외|JRDB프로젝트,JackRabbot dataset공식사이트,다년복합자료snapshot2026-10-11;최초논문판별도확인|프로젝트소개/통계/뉴스관련본문열람,open-C37 L18–53|1차데이터프로젝트;JRDB버전끼리비독립|제외 — 프로젝트 소개 읽음. 넓은 데이터 규모를 취약보행자 검증으로 대신하지 않고 C41 통제 시나리오를 채택. 기존 접근 평가: medium:데이터존재/수집목적만.시각장애·휠체어·아동충분표본추론불가;관련셋판분리필요|
|C38 / 제외|Jongwook Bae,Jungho Kim,Junyong Yun,Changwon Kang,Junho Lee,Jeongseon Choi,Chanhyeok Kim,Jungwook Choi,Jun Won Choi,SiT Dataset: Socially Interactive Pedestrian Trajectory Dataset for Social Navigation Robots,HanyangUniversity;프로젝트발행일미확인,NeurIPS2023논문판확인대기|프로젝트방법/센서관련본문열람,open-C38 L7–32|1차프로젝트설명,SiT계열|제외 — 프로젝트 방법 읽음. 원격조종 데이터라는 한계가 C41과 중복이며 취약인구 결과가 아님. 기존 접근 평가: medium:원격조종Husky에서수집한데이터.취약보행자검증/안전인증근거아님|
|C39 / 제외|Sharing the Sidewalk 관련MTI7(5):53(2023),DOI10.3390/mti7050053;정확저자/전체제목원문확인대기|열람실패(DOI/MDPI429),open-C39/full-C39|1차현장연구후보;독립성미평가|제외 — 출판사429/원문 실패. 접근성 실패 사례를 검색 요약만으로 확정하지 않음. 기존 접근 평가: low:검색요약만으로접근성실패사례인용금지|
|C40 / 제외|Tatsuya Nomura,Takayuki Kanda,Hiroyoshi Kidokoro,Yoshitaka Suehiro,Sachie Yamada,Why do children abuse robots?,InteractionStudies17(3),347–369(2016),온라인2017-03-30,DOI10.1075/is.17.3.02nom|원문미열람(초록·목차/authorizationrequired),open-C40|1차논문서지;ATR/Ryukoku/Tokai.같은팀HRI2015확장초록은독립아님|제외 — 원문 유료/초록만. 다른 판의 확장초록을 같은 전문으로 대체하지 않음. 기존 접근 평가: low현재:후속검색의저자공개2015PDF는다른판·저자·DOI.2016전문처럼묶지않음|
|C41 / 채택|Johnata Brayan, Sihao Deng, Armando Alves Neto, Iaroslav Okunevich, Tomas Krajnik, Francois Bremond, Zhi Yan. NavWareSet: A Dataset of Socially Compliant and Non-Compliant Robot Navigation. 프로젝트 사이트; 연결 논문 IJRR2026, DOI10.1177/02783649261447305(프로젝트 BibTeX), 정확 발행일 미확인; 권호0(0)는 임시 서지이므로 확정 권호로 사용하지 않음.|원문 열람: 프로젝트 방법·시나리오·scene표·데이터 설명 L21–124; 서지L208–217,read-bibliography-final.txt. 저널 전문을 읽었다고 집계하지 않음.|1차데이터프로젝트,NavWare;논문/사이트비독립|medium: 통제 실내·대부분 원격조종·17명; 중복 참여 ID 확인. 아동/장애인 안전성 입증 자료가 아님.|
|C42 / 제외|Navigation preferences and challenges of wheelchair users in Australia: implications for autonomous wheelchair design;2026;DOI10.1080/17483107.2026.2640487;저자/정확일자미확인|열람실패(403),open-C42|1차사용자연구후보,독립성미평가|제외 — 출판사403. 외부 AMR와 휠체어 사용자의 혼재 시험으로 볼 근거 없음. 기존 접근 평가: low:외부AMR와휠체어사용자의혼재실험으로볼근거없음.현재제외|
|C43 / 제외|공동주택 단지 내 로봇배송 구현을 위한 인프라 구축(안) 마련,CODIL OTKCRK240304;발행기관/저자/일자미확인|열람실패(502),open-C43|정부연구원문후보,제도요약은2차가능|제외 — 원문502. 보고서 내용 미확인. 기존 접근 평가: low:전문미확보,결론근거제외|
|C44 / 채택|ISO,ISO10218-1:2025,Robotics—Safety requirements—Part1:Industrial robots,edition3,2025-02,이력발행2025-02-05|원문미열람(공식목록·scope공개문구),open-C44 L95–108/142–152|1차공식목록;ISO/TC299,관련A3해설과작업계열중복|high:이동플랫폼관련mobility위험제외등공개범위만.전체이동매니퓰레이터비적용으로확대금지.전문분자제외|

## 집계와 사용 제한

채택20, 새 출처12(기존 문서의 다른 호스트·고정판·동일 Nav2 Collision Monitor 설명은 새 출처로 부풀리지 않음), 1차19, 2차 설명1(C05), 관련 원문 정독15/20. C21·C26·C27·C30·C44는 전문 미열람. 신뢰도 high는 해당 코드·목록의 좁은 사실에 대한 평가이며 실제 안전 효과의 보증이 아니다.

미확인으로 남길 것: 최신 표준 세부 조항, 한국 최종 고시 별표와8/16항목 대응, 안전 기능 소유자·실측 감속 ACK, 공개 구현의 실행 성능, 취약인구의 독립 실증. 최종 주장은 4단계에서 별도 분해하고 5단계에서 다시 대조한다.

## 부록 D. 검증 기록

### 5단계 자체 검증 기록

2026-10-11. draft.md 전체초안 생성 후 수행했다. 사실36개와 벤더 추정2개를 보존 원문 파일에서 다시 열어 대조했다. 단순 문자열 일치 검사는 보조 수단이며 범위·조건·태그 판단은 아래 별도 검사로 수행했다. 수치 계산은 논문 표에 대한 산술 확인일 뿐 독립 실험이나 모델 재현이 아니다.

|검증 항목|처음 태그 → 최종 태그|바꾼 이유·검사 결과|
|---|---|---|
|1. 모든 사실 원문 재대조|사실36 → 사실36|H01~H38 중 추정2개를 제외한36개와 원문·위치를 재확인. H35는 위치 출력 계약으로 본문1문장 수정. H36은 같은 반환구절의 예외 분기 위치로 범위를 좁혔다. H29에는 게시글 행번호를 추가했다.|
|2. 추론 분리|사실/추정/의견 → 유지|원문 계약과 안전 효과를 분리했다. 벤더 설명H03/H34는 추정 유지. 15개 ROP 설계 제안은 의견. 동일코드의 결과를 전체 시스템 안전성으로 확대하지 않았다.|
|3. 수치·번호·번역|유지|0.113초는 레일 매니퓰레이터. VDA m/s·진입 외곽·0값 계약 확인. C19 실물 모사 환경과 원격조종 장애물 확인. C20 32명/160→158→145와 오즈비 재계산, 표의 정밀도·재현율뿐 아니라 특이도 불일치도 기록.|
|4. 서지|유지|C01 게재승인2016과권호2017 구분. C11 CASE DOI/일자는UC표지,인용본문은arXivv1. C12 IROS 출판일은Aalto,인용본문은v1. C19 출판사2024-08-07. C41 프로젝트의IJRR서지이며정확일자는미확인. C09/C35 고정코드 본문 URL로 직접 연결.|
|5. 표현 강도|유지|H04/07/08/09의shall은명세상요구로표기. 시행규칙서류요구는H28로한정. 제조사 권고와 ROP 제안은 법적 의무로 바꾸지 않음.|
|6. 시행 상태|유지|H30 FDIS개발중/50.20과H31 Published/90.92 구분. C21 고시게시일·공식목록시행일만 확인,첨부별표미열람유지. ISO10218발행2025-02는최근1년창밖임도명시.|
|7. 독립성|유지|NIST계열·Nav2 두문서·ISO개정이력·논문미러·KIRO문서/코드를 같은계열로처리. 서로다른조건의연구를독립재현으로세지않음. 독립교차확인주장0개.|
|8. 위키 중복|유지|위키 본문 및7분리페이지의W01~33과 비교. 기존정의·구역목록·조끼존재를새내용으로계상안함. 보완은조건/분모/계약/판/한계,모의병원표현수정1항목.|
|9. 범위 넘침|유지|사람근접관제의구역·배정·위치인터페이스에한정. 법적책임판단,의료기기적합성,인증세부를확정하지않음. 다른영역심화조사없음.|

## 본문 및 근거 변경 이력

|대상|처음 태그 → 최종 태그|변경 이유|
|---|---|---|
|H35|사실 → 사실|UWB 입력 두개 설명을 사람별 위치 출력 토픽·메시지 형식으로 수정. OQ4의 인터페이스 증거에 더 직접적이며 src70–77/141–149/159–168에서 재확인. 본문 수정1문장.|
|H36|사실 → 사실|return pt가 두 분기에 존재해 위치를catch블록92–95행으로 좁혔다. 본문 수정0, 근거위치 정밀화1.|
|H29|사실 → 사실|공고 메타데이터 위치에L196·201·203·210–215를추가했다. 본문 수정0, 근거위치 정밀화1.|
|C20 분석 메모|분석 보류 → 분석 보류|TableVII 특이도.508도TableVI 표두 기반.640과일치하지않음을추가. 표의행열/라벨어느쪽이잘못인지저자확인전확정안함. 본문 주장H25 변경없음.|
|기타 사실·벤더 주장|변경 없음|각 주장별 근거와 범위는 부록E 및 본문 메모에 대응한다.|

## C20 통계표 재계산

TableVI의 표두를 그대로 읽으면 TN=32,FN=31,FP=18,TP=64,N=145다. 논문 식(2)~(6)에 대입하면 정확도96/145≈0.6621, 정밀도64/82≈0.7805, 재현율64/95≈0.6737, 특이도32/50=0.6400이다. TableVII의 복합 예측기 행은0.662/0.674/0.781/0.508이므로 세 지표의 대응이 일치하지 않는다. 행·열 해석 또는 표 표기 중 무엇이 잘못됐는지는 확인 못 했다. 오즈비(32×64)/(31×18)≈3.6703은 논문의3.67과 맞는다. 이 산술 대조만으로 연구 전체 무효나 성능 개선을 주장하지 않는다. [추정][^n11]

## 첫 영역 대비 지표 감시

|지표|01_F-21|05_M-49|판정|
|---|---:|---:|---|
|보완|15|15|수량 맞춤을 위한 약한 출처 추가 없음|
|출처|20|20|미러 및 같은 논문의 출판서지는 중복계상 안 함|
|새 출처|14|12|기존Nav2같은기능설명도보수적으로기존계열분류|
|원문 열람|14/20(70%)|15/20(75%)|+5%p, 메타데이터5개 분자제외|
|독립 교차 확인 주장|0|0|단독자료임을 숨기지 않음|
|태그 낮춤|1|0|초안부터벤더2개를추정으로분리;검증축소의근거로삼지않음|
|검증에서 고친 문장|별도 집계 없음|1|H35 출력 계약으로 수정; 근거위치2건·분석메모1건은 별도|
|확인 못 함|11|15|U01~15에 후속 증거 요구를 열거|

최종 확인: 9개 검증 항목 모두 수행, 사실36개 원문 재대조, 부록E38행, 원문75%, 최종파일 배타적 생성 및 저장 후 해시 확인. 실행 시험·독립 현장 재현은 수행하지 않았다.


## 부록 E. 독립 검증 대조표

### 부록 E용 독립 검증 대조표

독립 교차 확인된 주장은0개다. 각 행은 단일 출처의 직접 대조이며, 이 표 자체를 외부 독립 검증으로 세지 않는다. 인용구는 본문에 한 번만 제시하고 여기서는 주장 ID와 위치로 연결한다.

|주장|1차 근거·위치|비교·독립성|5단계 판정|
|---|---|---|---|
|H01|C01 / §5, PDF8쪽(P7),L723–730|C01/C05는 작업셀 연구와 제조사 설명으로 조건이 다르며 같은 장치 재현 아님.|구절·문맥·위치 재대조, 사실 유지|
|H02|C01 / §6, PDF8쪽(P7),L733–742|C01/C05는 작업셀 연구와 제조사 설명으로 조건이 다르며 같은 장치 재현 아님.|구절·문맥·위치 재대조, 사실 유지|
|H03|C05 / Multiple sampling 앞 문단과 해당 절,L84–88|C01/C05는 작업셀 연구와 제조사 설명으로 조건이 다르며 같은 장치 재현 아님.|구절·문맥·위치 재대조, 추정 유지|
|H04|C06 / §6.4,L845|같은 VDA5050 명세 계열. 독립 차량 준수 시험 없음.|구절·문맥·위치 재대조, 사실 유지|
|H05|C06 / §6.4.1.1,L853–870|같은 VDA5050 명세 계열. 독립 차량 준수 시험 없음.|구절·문맥·위치 재대조, 사실 유지|
|H06|C06 / §6.4.1.1,Table6,L870|같은 VDA5050 명세 계열. 독립 차량 준수 시험 없음.|구절·문맥·위치 재대조, 사실 유지|
|H07|C06 / §6.4.1.1,Table6,L870|같은 VDA5050 명세 계열. 독립 차량 준수 시험 없음.|구절·문맥·위치 재대조, 사실 유지|
|H08|C06 / §6.4.2,L907|같은 VDA5050 명세 계열. 활성화와 물리적 감속 ACK 구분.|구절·문맥·위치 재대조, 사실 유지|
|H09|C06 / §6.4.2,L909|같은 VDA5050 명세 계열. 활성화와 물리적 감속 ACK 구분.|구절·문맥·위치 재대조, 사실 유지|
|H10|C07 / 소개,L545|C07/C08은 동일Nav2 프로젝트. RMF와도 계약이 다르므로 교차확인으로 세지 않음.|구절·문맥·위치 재대조, 사실 유지|
|H11|C07 / source_timeout,L619|C07/C08은 동일Nav2 프로젝트. RMF와도 계약이 다르므로 교차확인으로 세지 않음.|구절·문맥·위치 재대조, 사실 유지|
|H12|C08 / speed_limit_topic,L468–472|C07/C08은 동일Nav2 프로젝트. RMF와도 계약이 다르므로 교차확인으로 세지 않음.|구절·문맥·위치 재대조, 사실 유지|
|H13|C09 / FleetUpdateHandle.cpp,L2248–2261|동일 Open-RMF 고정코드. 논문에서 RMF를 썼다는 사실은 이 API의 독립 재현 아님.|구절·문맥·위치 재대조, 사실 유지|
|H14|C09 / FleetUpdateHandle.cpp,L2263–2276|동일 Open-RMF 고정코드. 논문에서 RMF를 썼다는 사실은 이 API의 독립 재현 아님.|구절·문맥·위치 재대조, 사실 유지|
|H15|C11 / §VI,L192–194 및 §VII,L223|UCSD/IHI 한 연구팀, arXiv/UC/CASE는같은논문. HATA는다른평가지표.|구절·문맥·위치 재대조, 사실 유지|
|H16|C11 / §VI-B,TableIV,L210–218|UCSD/IHI 한 연구팀, arXiv/UC/CASE는같은논문. HATA는다른평가지표.|구절·문맥·위치 재대조, 사실 유지|
|H17|C12 / §IV-B,L131–136|Aalto 연구와 저자저장소는같은계열. C11 실물시험과독립동일주장아님.|구절·문맥·위치 재대조, 사실 유지|
|H18|C12 / §V,TableI/II 설명,L171|Aalto 연구와 저자저장소는같은계열. C11 실물시험과독립동일주장아님.|구절·문맥·위치 재대조, 사실 유지|
|H19|C18 / §3.1,Figure8,L459–461|Tartu 연구·시연·코드는같은프로젝트. C19는다른시험환경.|구절·문맥·위치 재대조, 사실 유지|
|H20|C18 / §4,Increasing the number and diversity of robots,L489|Tartu 연구·시연·코드는같은프로젝트. C19는다른시험환경.|구절·문맥·위치 재대조, 사실 유지|
|H21|C19 / Experimental testing,L210–221|같은병원벤치마크논문. Tartu 실제병원결과와표본·목적다름.|구절·문맥·위치 재대조, 사실 유지|
|H22|C19 / Mobile Obstacle,L128|같은병원벤치마크논문. Tartu 실제병원결과와표본·목적다름.|구절·문맥·위치 재대조, 사실 유지|
|H23|C20 / §IV,L112–114|한프리프린트·동일데이터.산술대조는외부재현아님.|구절·문맥·위치 재대조, 사실 유지|
|H24|C20 / §V-C,L262|한프리프린트·동일데이터.산술대조는외부재현아님.|구절·문맥·위치 재대조, 사실 유지|
|H25|C20 / §V-B,TableVI 설명,L243|한프리프린트·동일데이터.산술대조는외부재현아님.|구절·문맥·위치 재대조, 사실 유지|
|H26|C22 / 제7조의4제1항제1호,L82–84|법령/고시의 같은제도계열. 독립실증대조아님.|구절·문맥·위치 재대조, 사실 유지|
|H27|C22 / 제7조의4제1항제2호,L85|법령/고시의 같은제도계열. 독립실증대조아님.|구절·문맥·위치 재대조, 사실 유지|
|H28|C22 / 제7조의5제1항제4호,L91–98|법령/고시의 같은제도계열. 독립실증대조아님.|구절·문맥·위치 재대조, 사실 유지|
|H29|C21 / 게시글64952,L196·201·203·210–215|법령/고시의 같은제도계열. 독립실증대조아님.|구절·문맥·위치 재대조, 사실 유지|
|H30|C26 / Life cycle,L67–69 및 L107|ISO의같은개정이력. 2014/FDIS는독립자료아님.|구절·문맥·위치 재대조, 사실 유지|
|H31|C27 / General information,L77–87|ISO의같은개정이력. 2014/FDIS는독립자료아님.|구절·문맥·위치 재대조, 사실 유지|
|H32|C44 / Scope,L95–108|ISO공개범위와KS정적시험은다른명제.동적사람안전값교차확인없음.|구절·문맥·위치 재대조, 사실 유지|
|H33|C30 / 적용 범위,L229;이력L244|ISO공개범위와KS정적시험은다른명제.동적사람안전값교차확인없음.|구절·문맥·위치 재대조, 사실 유지|
|H34|C33 / 본문,L11–12|Amazon과KIRO는다른기관이나같은이종플릿안전정지주장을재현하지않음.|구절·문맥·위치 재대조, 추정 유지|
|H35|C35 / src/yolo_uwb_fusion_node.cpp,L70–77·141–149·159–168|Amazon과KIRO는다른기관이나같은이종플릿안전정지주장을재현하지않음.|구절·문맥·위치 재대조, 사실 유지; 본문 수정1|
|H36|C35 / src/yolo_uwb_fusion_node.cpp,L92–95(catch 블록)|Amazon과KIRO는다른기관이나같은이종플릿안전정지주장을재현하지않음.|구절·문맥·위치 재대조, 사실 유지; catch 위치로 정밀화|
|H37|C41 / Experiment description,L58 및 scene표L63–110|NavWare사이트와논문은같은프로젝트.취약인구안전성독립확인없음.|구절·문맥·위치 재대조, 사실 유지|
|H38|C41 / Scenarios Table,L53|NavWare사이트와논문은같은프로젝트.취약인구안전성독립확인없음.|구절·문맥·위치 재대조, 사실 유지|

## 분석 근거와 위키 대조 (4단계 기록, 5단계 교정 반영)

### M-49 4단계 분석

2026-10-11. 3단계 종료 후 주장38개(사실36, 벤더 추정2)를 분해했다. ROP 제안15개는 의견으로 분리한다. 독립 교차 확인된 주장은0개다. 다양한 출처가 서로 다른 범위의 주장을 제공하는 것과 동일 주장의 독립 재현을 구별했다.

|질문|결과/주장|위키 대조|독립성·범위 및 남은 증거|
|---|---|---|---|
|Q1|부분 H01~03|W01/07/21 추가|NIST 작업셀과 SICK 설명은 대상이 다름. 공통 지연 논리는 참고하되 같은 AMR의 독립 실험으로 세지 않음. 현행 SSM 조항/검증주체 미확인.|
|Q2|부분 H04~14|W10/22/23/30 추가|VDA·Nav2·RMF 계약 차이. 세 프로젝트가 서로의 실행 보증을 재현하지 않음. ACK와 실측정지 연결 미확인.|
|Q3|부분 H15~18|W11/13/24 추가|CBF는 실물, HATA는 궤적 재생. 같은 주장을 교차 검증한 논문이 아님. 코드 재현 및26/19%분모 보류.|
|Q4|부분 H19~25|W14 수정, W05/20/25 추가|실제병원/모사병원/성인 편안함의 다른 모집단. 안전속도 보편값 도출 안 함.|
|Q5|부분 H26~29|W16~19/31 추가|상위 시행규칙 원조문과 최종 고시 게시 메타데이터. 서로 같은 법체계이며 별표 독립 확인 아님.|
|Q6|부분 H30~33|W02/26/27 추가|공식 목록 범위까지만. ISO2014/FDIS는 같은 개정 이력, KS정적 시험은 동적 보행자 안전 실증 아님.|
|Q7|부분 H34~36|W12/30 추가|Amazon 단일기업 주장과 공개 ROS 위치 인터페이스를 구별. 동일 이종플릿 동시감속 주장을 입증하지 못함.|
|Q8|부분 H37~38|W20 추가|가림 시나리오 및 표본 구성만 확인. 취약인구 사고위험·감지율의 실증 근거 부족.|

## 충돌·숫자·범위 대조

|충돌|1차 자료별 차이|처리|
|---|---|---|
|Nav2 0 vs RMF 0|C08은제한없음,C09는거절|어댑터계약차이로기술.명세상충이나공통정지로통합하지않음.|
|HATA26/19% vs표의평균|저자요약집계와표별집계분모미재현|숫자확인못함.실제안전효과및교차검증으로세지않음.|
|C20 TableVI vs VII|TableVI표두대로 TP64/FP18/FN31/TN32이면정밀도.7805/재현율.6737/특이도.6400;VII는.674/.781/.508|5단계에서표두·식(2)~(6)·TableVI/VII재대조.어느표의행열이오류인지확정못함.성능수치채택보류,오즈비만문맥한정.|
|모의병원시뮬레이션|C19는Vicon과실제두로봇측정|실물모사시험으로수정.실제환자혼재운영으로확대안함.|
|실제병원이종플릿|C18병원은TIAGo시연;이종2대는시험환경|두범위분리.상시다로봇병원성과미확인.|
|ISO13482 의료로봇설명|C19도입의일반설명 vs C27의medical devices제외|표준범위는공식목록우선,논문표준요약채택안함.병원물류/의료기기동일시안함.|
|2014판 vs FDIS|Published/current와개발중승인단계|개정절차날짜와정식발행분리.|
|국내8 vs16|현재기관안내미열람·최종별표미확보|판/상하항목계층으로추정해해소하지않음.|

## 위키 중복 제외

SSM 정의, VDA 구역 목록, Amazon 조끼의 존재, HATA MoD 도입, 병원 시험속도, 기존 연결16개는 새로 발견했다고 쓰지 않는다. 추가는 계약·분모·판·측정환경·한계이며 수정은 모의 병원 표현이다. 다른 영역 상세는 다루지 않는다.

## 최근1년 확인

C06 VDA3.0.0(2026-03),C21고시게시(2025-11-24),C26 FDIS단계(2026-09-15),C35확인커밋(2026-06-29),C20프리프린트(2026-04-15),C12게재(2025-11-27). ISO10218:2025발행은2025-02로 최근1년 창 밖이지만 사용자가 지정한 적용범위 조사대상이라 포함한다. 게시/커밋/게재 날짜를 기술변경의 최초 시행일로 바꾸지 않는다.


## 기록 보존과 재검증 경로

작업 폴더는 `.research-work/M-49/`이다. `claims.verified.json`에 최종 주장별 원문파일·위치, `source-evaluation.md`에44후보 평가, `stage5-verification.md`와`independent-cross-check.md`에 검증 기록을 보존했다. 보완 대상의 긴 위키 문장은 반복 전재 대신 짧은 식별 구절과 보존 원문 위치를 제공한다. 검색 후 추가 서지 복구 결과는 `search-stage3-final-bibliography.txt`·`C11-publication-final.txt`·`read-bibliography-final.txt`에 있다. 추가 서지 검색의 정확 문자열은 별도 보존되지 않아 검색 횟수 집계에 더하지 않았다. 원문 열기 및 고정 커밋 코드는 별도 획득 기록으로 구별했다.
