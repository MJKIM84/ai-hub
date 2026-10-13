---
title: "핵심 학습 자료"
type: field-research
research: pm-interview-prep
level: study
hide: [toc]
search: {exclude: true}
related_areas: [1, 4, 20, 21, 22, 42, 48, 50, 51, 55]
tags: [면접 준비, 학습 자료, 제품 문서, 표준, 법령, 열람 기록]
status: published
confidence: medium
created: 2026-10-12
updated: 2026-10-12
version: 1
sources: [ref-031, ref-251, ref-282, ref-283, ref-284, ref-306, ref-470, ref-1135, ref-1383, ref-1494, ref-1579, ref-1580, ref-1589, ref-1591, ref-1592, ref-1593, ref-1594, ref-1595, ref-1596, ref-1597, ref-1598, ref-1599, ref-1600, ref-1601, ref-1602, ref-1603, ref-1604, ref-1605, ref-1606, ref-1610, ref-1611, ref-1612]
---

[홈](../../index.md) › [확장 아이디어](../../ideas/index.md) › [스터디](../index.md) › [면접 준비](index.md) › 핵심 학습 자료

# 핵심 학습 자료

<!-- auto:page-status:start -->
> 페이지 상태: published · 신뢰도: medium · 페이지 버전: 1 · 마지막 갱신: 2026-10-12 · 마지막 실행: 없음
<!-- auto:page-status:end -->

PM이 읽어야 할 학습 단위 18개다. 각 단위는 주자료와 필요한 공식 보조 문서로 구성하며, 전문 전체를 읽었다는 뜻은 아니다. 발행·개정일이 없는 웹 문서는 그렇게 표시하고 접근일로만 식별한다. 검색 엔진의 수집일이나 저작권 연도를 발행일로 쓰지 않는다. 다른 페이지의 S번호는 이 페이지의 카드를 가리키며, 각 카드의 URL·일자·판·읽은 절·한계는 각주의 참고문헌 페이지에 있다.

**먼저 읽을 것:** S01·S02·S04·S05·S07·S08·S09·S11·S14. 나머지는 심화다. 처음에는 **S01·S02 제품 → S05 운영 사례 → S07·S08 연동 → S11 시험 → S14 영상법** 순서로 읽고, 실제 제어·취소와 연동 판단을 위해 S04·S09를 이어 읽는다.

## 18개 학습 단위

| 자료 | 과제 | 읽을 부분과 핵심 내용 | PM이 내려야 할 결정 | 한계 |
|---|---|---|---|---|
| S01 Robotnik RB-SUMMIT 자료 묶음 / 먼저 | ①②③ | 제품 구성, 운동학, RLC·Command Manager | 구매 구성과 추가 개발 범위 | 연구개발용 AMR이며 완제품 배송·안내 서비스가 아니다 |
| S02 Boston Dynamics Spot 제품·기체 설명 / 먼저 | ①③ | 사양, 추가 Arm·센서, 구형 Gamma 구별 | 계단·점검 수요가 추가 비용을 정당화하는가 | 웹과 구형 기체 사양이 상충 |
| S03 Spot 페이로드 구성 요구 / 심화 | ①③ | 질량·무게중심·다리 간섭 | 센서·적재함·Arm을 함께 장착할 수 있는가 | 적재량은 물체 조작 능력이 아니다 |
| S04 Spot SDK / 먼저 | ②③ | GraphNav 피드백, Robot Services, 5.2 변경 | 명령 소유권·단절·복구 계약 | SDK 사용 가능과 현장 안전성은 별개 |
| S05 NAVER 1784 / 먼저 | ①②③ | Rookie, ROBOPORT, ARC, Works assistant | 로봇과 빌딩·직원 앱을 함께 설계할 범위 | 운영기관이자 기술 공급자의 소개. ROI 미공개 |
| S06 BMW Hams Hall / 심화 | ①③ | SpOTTO의 시각·열·음향 점검과 후속 활용 | 이동 성공 대신 유효한 측정과 조치를 정의 | 회사 발표. 독립 검증·효과 수치 부족 |
| S07 Open-RMF 플릿 연동 / 먼저 | ② | Full Control·Traffic Light·어댑터 콜백 | 제조사 제어 수준에 맞는 조율 범위 | 제품별 어댑터와 검증은 직접 필요 |
| S08 Open-RMF 문·승강기 / 먼저 | ②③ | 지도 식별자와 설비 어댑터 | 승강기·문 업체와 연동 책임·권한 합의 | 물리 개조·설비 인증을 대신하지 않는다 |
| S09 VDA 5050 3.0.0 / 먼저 | ②③ | 범위, order, state, cancel, maps | 판·선택 기능·오류 의미의 적합성 시험 | 안전·시설·고객 IT API는 별도 |
| S10 ROS 2 QoS와 MQTT / 심화 | ②③ | 신선도·생존 확인·전달 보장 | 상태와 명령에 다른 통신 정책 적용 | QoS는 실물 업무 완료 보장이 아니다 |
| S11 NIST 로봇 시험 방법 / 먼저 | ③ | 변수 통제, 반복, 성능 측정 | 미션 조건을 반복 가능한 인수시험으로 변환 | 응급 대응 도메인의 합격 수치를 전용하지 않는다 |
| S12 ISO 13482 / 심화 | ③ | 공개 범위·제외 대상·판 상태 | 개인 지원 서비스 로봇 적용성 검토 의뢰 | 유료 전문 미열람. 인증 판단 불가 |
| S13 ISO 3691-4 / 심화 | ③ | 무인 산업차량과 운영 구역 | 산업 운반 용도와 운영 구역 검토 의뢰 | 유료 전문 미열람. 모든 서비스 로봇에 자동 적용되지 않는다 |
| S14 개인정보 보호법 제25조의2 / 먼저 | ①②③ | 이동형 영상정보처리기기 | 로비·사무실 영상의 법적 근거·표시·권리 처리 | 구역의 공개성과 실제 데이터 처리 방식별 판단 필요 |
| S15 개인정보위 보도자료와 안내서 / 심화 | ①③ | 처리 단계별 준수·권고, 위탁·학습 활용 | 영상 최소 수집·보관·처리업체 책임 | 2024년 안내서. 2026 법령과 함께 읽는다 |
| S16 소방·승강기 법령 / 심화 | ②③ | 피난시설 관리, 승강기 안전검사 | 충전·대기 위치와 연동 변경 승인 | 개별 건물·변경 공사의 적법성 결론은 별도 |
| S17 사회적 로봇 주행 조사 논문 / 심화 | ①③ | §5 평가 지표와 실험 방법 | 안내 완주·추종 유지·불편·접근성 평가 | 연구 종합. 특정 제품의 수용성 수치가 아니다 |
| S18 FLIR 측정 매뉴얼 / 심화 | ①③ | 초점·측정 범위·방사율·반사 온도·거리 | 점검 데이터의 유효성 기준 | G 시리즈 매뉴얼이며 Spot 기본 센서 사양이 아니다 |

## 자료별 메모

**S01 Robotnik — RB-SUMMIT과 소프트웨어.** [추정] 벤더 주장: 현재 제품 페이지는 연구개발용 이동 로봇으로 소개하며 적재 50 kg, 최대 5시간, 최대 2.5 m/s, IP54, 5G 라우터·충전소 등을 제시한다.[^ref-1591] 2024년 6월 데이터시트(CF 06.24)는 구동 방식을 "Skid steering / Omnidirectional (mecanum)"으로 나누고 4개 구동 모터·치수·구성표를 적으며, 3 m/s·기본 4G·IP50/53처럼 현재 페이지와 다른 값이 있다.[^ref-1592] 소프트웨어 페이지는 개방형 구조, RLC와 Command Manager, 위치 추정·주행을 설명하지만 개정일·배포판이 없다.[^ref-1593] 제조사 ROS 2 시뮬레이션 저장소의 지원 로봇 목록에는 RB-SUMMIT이 skid-steering으로 올라 있다.[^ref-1594] 읽기만 했고 실행하지 않았으며, 시뮬레이션 공개가 실기 SDK 전체 공개의 증명은 아니다. 적용: 차체를 배송함·안내 화면·점검 센서와 결합하는 **개발형 AMR 후보**로 읽는다. 공개 자료만으로 국내 공용 공간 운행 승인, 정확한 회전 공간, 최신 실기 제어 API 권한·라이선스·유지보수 SLA를 확정하지 않는다.

**S02 Boston Dynamics — Spot 제품과 About Spot.** [추정] 벤더 주장: 현재 제품 페이지는 최대 적재 14 kg, 평균 운용 90분, 배터리 564 Wh·충전 60분을 적고, 운용 시간이 페이로드와 환경에 따라 달라진다고 밝힌다.[^ref-1595] SDK 5.2.0 문서의 기체 사양은 **Spot Gamma**를 대상으로 하며 605 Wh·충전 120분처럼 값이 다르다.[^ref-1596] 현재 웹의 길이 표기는 단위가 맞지 않아 확정 치수로 쓰지 않았다. 적용: 카탈로그의 최대 단차와 계단 형태·적재·조명·마찰을 함께 확인한다. 구형 Gamma의 환경 값이나 배터리 값을 최신 구매품에 합치지 않는다. 동적 보행자 안전성은 정적 장애물 회피 문구만으로 판단하지 않는다.

**S03 Boston Dynamics — 페이로드 구성 요구.** [추정] 벤더 주장: 페이로드 포트·폭·길이·높이·무게·다리 간섭·Arm 아래 여유를 정하고, Spot Arm의 무게는 8 kg이다.[^ref-1597] 합산 페이로드 한도 14 kg에 Arm도 들어간다. 본체 운반 한도에서 Arm 질량을 뺀 값을 곧바로 손으로 들 수 있는 물체 질량으로 해석하지 않는다. 적용: 센서·브래킷·통신 장치·적재함·내용물의 질량표와 장착 도면을 구매 전에 검토한다. 문 열기와 자동 상하차는 별도 Arm·그리퍼·소프트웨어·문 형태별 검증 대상이다.

**S04 Boston Dynamics — Spot SDK 실행과 복구.** [추정] 벤더 주장: GraphNav 문서는 NavigateTo·NavigateRoute·NavigateToAnchor와 상태·피드백, 자율 주행 오류를 설명하고 STATUS_LOST 같은 상태를 구분한다.[^ref-1579] Robot Services 문서는 인증 뒤의 시간 동기·lease, 비상 정지, 로봇 명령·상태·로그·영상 서비스를 설명하며 명령을 내리려면 lease를 얻어야 한다.[^ref-1598] 릴리스 노트의 최신 판은 5.2.0이며 Keepalive의 halt와 motors-off 구분, 미션·Autowalk, Orbit 예제 변경을 적는다.[^ref-1383] 도착 피드백과 위치 정밀 확인은 다르고 LOST와 STUCK도 다르다. 적용: 로봇별 단절 동작을 버전을 고정한 뒤 시험한다. 전원 차단이 모든 상황에서 안전한 정지는 아니다. SDK 호출 성공을 실제 서비스 완료로 간주하지 않는다.

**S05 NAVER — 1784 공식 소개.** [추정] 운영기관 보고: 직원 앱(Works assistant), 로봇 배송(Rookie), 로봇 전용 승강기(ROBOPORT), 클라우드·5G 기반 다중 로봇 시스템(ARC)을 함께 소개한다.[^ref-1599] 발행·개정일과 제품 판은 없다. 적용: 이용자 서비스와 건물 설비를 함께 기획한 사례로 쓴다. 로봇 전용 승강기가 있는 빌딩의 경험을 기존 공용 승강기 빌딩의 비용·성공률로 옮길 수 없다.

**S06 BMW Group — Hams Hall의 SpOTTO.** [추정] 운영기관 보고: 2024-05-07 보도자료는 시각·열·음향 센서 데이터를 3차원 디지털 트윈과 보전에 활용하고 설비 온도·압축공기 누출 점검을 소개한다.[^ref-1600] 적용: 순찰 결과를 보전 티켓·검사·조치 완료와 연결하는 설계 근거다. 본체 기본 센서만으로 전부 수행한다고 해석하지 않는다. 절감액·탐지 정확도·장기 무개입률은 이 자료로 입증되지 않는다.

**S07 Open Robotics — 플릿 연동.** [사실] Full Control 어댑터는 경로를 지정하고 언제든 중단·교체할 수 있으며 현재 위치를 제공한다는 전제이고, Traffic Light는 일시정지·재개 중심이다. 명령·갱신 핸들과 EasyFullControl 콜백으로 제조사 API를 연결한다.[^ref-251] 적용: 제조사와 "우리가 어느 수준까지 명령·중단·위치 확인을 할 수 있는가"를 먼저 확인한다. Open-RMF를 깔면 모든 제조사 로봇을 같은 수준으로 제어한다는 제안은 피한다. 결제·사용자·물품 인계·안전 인증은 별도 설계다.

**S08 Open Robotics — 문과 승강기.** [사실] 자동문만 연동할 수 있고, 승강기 제어기가 명령을 받아들여야 하며, 문·승강기 이름과 층을 지도에 대응시킨 뒤 어댑터를 연결한다.[^ref-283][^ref-284] 적용: API 사용권, 관리주체·설비 업체 승인, 수동 운전·화재 모드·오래된 상태 처리를 협의한다. 도면에 승강기가 있다는 이유로 API가 있다고 가정하지 않는다.

**S09 VDA·VDMA — VDA 5050 3.0.0.** [사실] 관제와 이동 로봇 사이의 통신 명세다. 범위 밖으로 안전 요구, 교통 관리 논리, 주변 설비·외부 IT 인터페이스, 프로젝트 조정·구현 절차, 운영 책임 할당, 사이버보안을 명시한다. 주문 갱신·취소·같은 orderId와 orderUpdateId의 처리·지도 오류를 §6에서 다룬다.[^ref-031] 3.0.0 판의 발행 기록은 저장소 릴리스 페이지에 있다.[^ref-1601] 적용: 기능 지원표와 양방향 적합성 시험을 계약에 넣는다. Spot·RB-SUMMIT이 이 판을 기본 지원하는지는 **미확인**이다.

**S10 ROS 2 Jazzy QoS와 OASIS MQTT 5.0.** [사실] ROS 2의 QoS에서 deadline·lifespan·liveliness는 서로 다른 개념이고 만료된 메시지는 조용히 버려진다.[^ref-282] MQTT 5.0은 QoS 0·1·2의 전달 등급을 정한다.[^ref-306] [의견] API 재요청·DB 저장·제조사 명령·실물 인계까지 한 번만 수행되게 하려면 각각의 중복 방지와 재조정이 필요하다. 메시지 QoS만으로 업무의 exactly-once를 주장하지 않는다.

**S11 NIST — 응급 대응 로봇 성능.** [사실] 반복 가능한 시험 장치·절차·지표를 정의하고, 처음에는 변수를 통제해 기준 성능을 잰 뒤 조명·젖음 같은 변수를 단계적으로 더한다.[^ref-1580] 적용: 같은 지도·하중·설정에서 반복한 뒤 단일 변수와 복합 조건을 시험한다. 응급 대응 시험의 수치를 사무빌딩 로봇의 법정 합격값이나 인증 근거로 전용하지 않는다.

**S12 ISO 13482:2014.** [사실] 공개 초록과 판 상태만 읽었다. 개인 지원(personal care) 로봇의 범위·유형과 제외 대상을 적고, 대체판이 개발 중이다.[^ref-1602] 유료 전문은 열지 않았다. 적용: 고객 용도가 해당 분류인지 안전 전문 담당자가 판단하고 원문·제품 선언을 확보한다. 이 조사로 충돌 힘·정지 거리·속도 한계·인증 적합성을 확정하지 않는다.

**S13 ISO 3691-4:2023.** [사실] 공개 초록과 판 상태만 읽었다. 무인 산업차량과 그 시스템을 다루고, 운영 구역의 조건이 안전 운행에 큰 영향을 준다고 적는다. 공공 구역에서 운행하는 차량은 적용 제외로 두고 ISO 13482를 가리킨다.[^ref-470] 적용: 산업 운반 구성과 현장 조건의 안전 검토에 쓴다. "AMR"이라는 이름만으로 빌딩 안내·4족 점검까지 이 규격의 인증을 보장하지 않는다.

**S14 개인정보 보호법 제25조의2.** [사실] 법률 제21445호(2026-03-10 개정, 시행 2026-09-11) 열람본. 업무를 목적으로 공개된 장소에서 이동형 영상정보처리기기로 개인영상정보를 촬영하는 것은 법정 허용 사유·제한·고지와 함께 판단해야 한다. 표시했더라도 부당한 권리 침해나 합리적 범위 초과는 허용되지 않고, 사생활 침해 우려가 큰 장소의 제한도 있다.[^ref-1603] 제25조의2 자체의 신설은 2023년이다. 적용: 로비와 제한 사무실의 공개성, 촬영과 저장·전송 목적, 거부 대응, 보관·삭제·위탁을 개인정보 담당자와 확정한다.

**S15 개인정보보호위원회 — 보도자료와 안내서.** [사실] 2024-10-14 보도자료는 「이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서」(2024년 9월)를 소개하며, 8대 기본 원칙, 처리 단계별 준수·권고, AI 학습 활용, 보관·관리를 요약하고 목적에 필요한 범위에서 최소화를 강조한다.[^ref-1494][^ref-1135] 보도자료 본문과 안내서 게시 페이지를 읽은 것이며 안내서 PDF 전문 열람으로 세지 않는다. 2024년 자료이므로 S14의 2026 현행 조문과 함께 읽는다.

**S16 피난시설 관리와 승강기 안전검사.** [사실] 소방시설 설치 및 관리에 관한 법률 제16조는 특정소방대상물 관계인에게 피난시설·방화구획·방화시설의 폐쇄·훼손, 물건 적치나 장애물 설치, 용도 장애, 변경을 금지한다.[^ref-1604] 승강기 안전관리법 제32조는 관리주체의 정기·수시·정밀안전검사를 정하고, 제어방식 변경 등이 수시검사 사유다.[^ref-1605] 적용: 충전기·적재함·정지한 로봇의 피난 방해와 방화문 고정 개방 여부를 검토한다. 모든 로봇 API 연동이 수시검사를 요한다고 단정하지 않고 변경 범위를 설비 업체·관리주체·검사기관에 확인한다.

**S17 Mavrogiannis 외 — 사회적 로봇 주행의 핵심 과제 조사.** [사실] §5(PDF 13~24쪽)에서 평가 지표와 평가 방법을 다루며, 도착 여부뿐 아니라 안전·편안함·사회적 적절성을 평가하고 데이터셋·시뮬레이션·실사용 실험을 구별한다.[^ref-1606] 적용: 안내에서 일행 이탈, 혼잡, 사람의 부담과 직원 인계를 시험한다. 특정 제품의 "사람 친화적" 성능 수치로 인용하지 않는다.

**S18 FLIR — 온도 측정.** [추정] 벤더 주장: 온도 측정에는 초점·측정 범위와 방사율·반사 온도·거리 같은 측정 매개변수 설정이 필요하다.[^ref-1589] 적용: 같은 설비에서 거리·각도·초점·방사율·반사 조건·교정 정보까지 기록해야 비교 가능한 점검을 설계할 수 있다. 이 문서의 카메라가 특정 Spot 구성에 포함된다는 뜻은 아니다.

## 보조 연습: 제어 API와 완성된 서비스의 차이

주 비교는 RB-SUMMIT과 Spot이지만, 4휠 Jackal J100의 공개 API는 "제어 API가 있다"와 "서비스가 완성됐다"의 차이를 공부하기 좋다. [추정] 벤더 주장: Clearpath의 ROS 2 시작 문서는 토픽·액션·서비스로 구성된 API와 속도 명령(cmd_vel)을 설명하며, cmd_vel에 직접 발행하면 센서의 피드백 없이 로봇이 앞으로 구동된다고 경고한다.[^ref-1610] Jackal 사용자 매뉴얼은 연구·프로토타이핑 플랫폼으로 소개하고 별도 센서·자율 주행·안전 운영 검토가 필요하다고 적는다.[^ref-1611] ROS 2 로봇 API 개요(2025-05-13 갱신)는 QoS 프로파일과 이름 공간 같은 공식 API 구조를 보여 준다.[^ref-1612] 이 보조 예제의 토픽을 Robotnik 실기 인터페이스로 복사하지 않는다.

연습 질문: "속도 명령을 보냈다는 기록만으로 배송 완료를 판단할 수 있는가?" 답은 아니며, 위치·진행·인계 증거와 상위 상태 계약이 필요하다. 이 조사에서는 명령·코드·시뮬레이션을 실행하지 않았다.

## 열람 실패와 미채택 기록

| 자료·경로 | 결과 | 처리 |
|---|---|---|
| RB-SUMMIT 현재 페이지가 연결하는 드라이브 데이터시트 | 뷰어 래퍼만 보이고 최신 PDF 본문 미확인 | 현재 HTML과 공식 2024 PDF를 분리. 최신 PDF 사양을 추측하지 않음 |
| Spot SDK lease 문서 | 접근 실패 | Robot Services 문서의 lease 설명만 사용 |
| Robotnik robot_simple_command_manager 저장소 | 열람 실패 | 실기 API 엔드포인트를 만들어 내지 않음. 소프트웨어 페이지의 공개 범위만 사용 |
| ROS 2 QoS 문서 HTML | 접근 차단 | 공식 ros2_documentation 저장소의 jazzy 원문으로 대체 |
| 사회적 주행 논문 HTML v5 | 내부 오류, 해당 판 존재 미확인 | 등록 이력 v2와 PDF만 채택 |
| NSF 논문 미러 | 시간 초과 | 저자 arXiv PDF로 대체 |
| 한 병원의 로봇 도입 보도 PDF | 404 | 사례·정량 성과에 쓰지 않음 |
| 개인정보 보호법 시행령 제27조의2 간편 URL | 내부 오류 | 상위법 제25조의2와 공식 해설 범위만 사용. 표시 방식의 세부 시행령 적합성은 후속 확인 |
| ISO 13482·3691-4 유료 전문 | 공개 초록만 열람 | 수치·세부 절차·인증 판정의 근거로 쓰지 않음 |

[의견] 미확인은 존재하지 않는다는 뜻이 아니다. 제품 가격, API 계약, 유지보수, 국내 인증, 소음, 비용 절감·성공률·수용성은 공급사 문서와 현장 시험으로 닫는다.

## 연결 영역

- [1. 기술·시장·업체 동향](../../categories/planning-and-business/technology-market-and-vendor-trends.md), [4. 이기종 로봇 등록](../../categories/robot-ontology/heterogeneous-robot-registration.md): 제품 자료의 판·구성 관리.
- [20. 로봇·제조사 관제 연동](../../categories/integration/robot-and-vendor-fleet-manager-integration.md), [21. 상호운용 표준·적합성](../../categories/integration/interoperability-standards-and-conformance.md), [22. 설비·건물 시스템 연동](../../categories/integration/facility-and-building-system-integration.md): S07~S09.
- [42. 분산 시스템·통신·컴퓨팅 구조](../../categories/platform-architecture-and-infrastructure/distributed-systems-communication-and-computing.md): S10.
- [48. 안전·위험 관리](../../categories/safety/safety-and-risk-management.md), [51. 인증·권한·격리](../../categories/security-and-privacy/authentication-authorization-and-isolation.md): S11~S16.
- [현장 적용·운영 검증 — 근거와 남은 질문](../field-readiness-rop/evidence-and-open-questions.md): NIST·FLIR·VDA 5050·MQTT를 같은 원문으로 대조한 기록.

[^ref-1591]: Robotnik Automation, RB-SUMMIT — Mobile Robot ideal for R&D applications (제품 페이지), 2020-05-29, https://robotnik.eu/products/mobile-robots/rb-summit/, 접근일 2026-10-12
[^ref-1592]: Robotnik Automation, Robotnik Datasheet RB-SUMMIT 2024 EN (CF 06.24, Standard version), 2024-06, https://robotnik.eu/wp-content/uploads/2024/05/Robotnik_Datasheet_RB-SUMMIT_2024_EN.pdf, 접근일 2026-10-12
[^ref-1593]: Robotnik Automation, Software solutions — Open Architecture, RLC and Command Manager, Advanced Localization and Navigation, 2025-11-28, https://robotnik.eu/software-solutions/, 접근일 2026-10-12
[^ref-1594]: Robotnik Automation (GitHub), robotnik_simulation — README (jazzy-devel), 미확인, https://github.com/RobotnikAutomation/robotnik_simulation/blob/jazzy-devel/README.md, 접근일 2026-10-12
[^ref-1595]: Boston Dynamics, Spot — The Agile Mobile Robot (제품 페이지), 2024-06-24, https://bostondynamics.com/products/spot/, 접근일 2026-10-12
[^ref-1596]: Boston Dynamics (Spot SDK docs), About Spot — Robot specifications (Spot SDK 5.2.0), 미확인, https://dev.bostondynamics.com/docs/concepts/about_spot.html, 접근일 2026-10-12
[^ref-1597]: Boston Dynamics (Spot SDK docs), Payload Configuration Requirements (Spot SDK 5.2.0), 미확인, https://dev.bostondynamics.com/docs/payload/payload_configuration_requirements.html, 접근일 2026-10-12
[^ref-1579]: Boston Dynamics (spot-sdk GitHub), spot-sdk — docs/concepts/autonomy/graphnav_and_robot_locomotion.md (master, blob 1362051), 미확인, https://github.com/boston-dynamics/spot-sdk/blob/master/docs/concepts/autonomy/graphnav_and_robot_locomotion.md, 접근일 2026-10-12
[^ref-1598]: Boston Dynamics (Spot SDK docs), Robot Services (Spot SDK 5.2.0), 미확인, https://dev.bostondynamics.com/docs/concepts/robot_services.html, 접근일 2026-10-12
[^ref-1383]: Boston Dynamics, Spot SDK Release Notes, 미확인, https://dev.bostondynamics.com/docs/release_notes, 접근일 2026-10-12
[^ref-1599]: NAVER Corp., 1784 — Service (Rookie, ROBOPORT, ARC System, Works assistant), 미확인, https://www.navercorp.com/en/service/1784, 접근일 2026-10-12
[^ref-1600]: BMW Group PressClub (UK), "Good boy SpOTTO": robot dog scans and monitors manufacturing equipment at BMW Group Plant Hams Hall, 2024-05-07, https://www.press.bmwgroup.com/united-kingdom/article/detail/T0441735EN_GB/%E2%80%9Cgood-boy-spotto%E2%80%9D%3A-robot-dog-scans-and-monitors-manufacturing-equipment-at-bmw-group-plant-hams-hall?language=en_GB, 접근일 2026-10-12
[^ref-251]: Open Robotics, Mobile Robot Fleets (integration_fleets) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_fleets.html, 접근일 2026-10-12
[^ref-283]: Open Robotics, Doors (integration_doors) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_doors.html, 접근일 2026-10-12
[^ref-284]: Open Robotics, Lifts (integration_lifts) - Programming Multiple Robots with ROS 2, 미확인, https://osrf.github.io/ros2multirobotbook/integration_lifts.html, 접근일 2026-10-12
[^ref-031]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050, 미확인, https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md, 접근일 2026-10-12
[^ref-1601]: VDA / VDMA (VDA5050 GitHub), VDA5050/VDA5050 — Releases (3.0.0), 2026-03-19, https://github.com/VDA5050/VDA5050/releases, 접근일 2026-10-12
[^ref-282]: Open Robotics (ROS 2 Documentation), Quality of Service settings — ROS 2 Documentation: Jazzy, 미확인, https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html, 접근일 2026-10-12
[^ref-306]: OASIS, MQTT Version 5.0, 2019-03, https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html, 접근일 2026-10-12
[^ref-1580]: NIST, Performance of Emergency Response Robots, 2014-04-28, https://www.nist.gov/programs-projects/performance-emergency-response-robots, 접근일 2026-10-12
[^ref-1602]: ISO, ISO 13482:2014 Robots and robotic devices — Safety requirements for personal care robots, 2014-02, https://www.iso.org/standard/53820.html, 접근일 2026-10-12
[^ref-470]: ISO, ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems, 2023-06, https://www.iso.org/standard/83545.html, 접근일 2026-10-12
[^ref-1603]: 개인정보보호위원회 (국가법령정보센터), 개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한), 2026-09-11, https://www.law.go.kr/LSW/lsSideInfoP.do?docCls=jo&joBrNo=02&joNo=0025&lsiSeq=283839&urlMode=lsScJoRltInfoR, 접근일 2026-10-12
[^ref-1494]: 개인정보보호위원회, 자율주행 인공지능(AI) 발전을 위한 개인영상정보 보호ㆍ활용 기준 나왔다, 2024-10-14, https://pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=10678, 접근일 2026-10-12
[^ref-1135]: 개인정보보호위원회, [현재 안내서] 이동형 영상정보처리기기를 위한 개인영상정보 보호ㆍ활용 안내서(2024.9.), 2024-10-14, https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS217&mCode=G010030000&nttId=10679, 접근일 2026-10-12
[^ref-1604]: 소방청 (국가법령정보센터), 소방시설 설치 및 관리에 관한 법률 제16조(피난시설, 방화구획 및 방화시설의 관리), 2022-12-01, https://www.law.go.kr/LSW/lsSideInfoP.do?docCls=jo&joBrNo=00&joNo=0016&lsiSeq=236977&urlMode=lsScJoRltInfoR, 접근일 2026-10-12
[^ref-1605]: 행정안전부 (국가법령정보센터), 승강기 안전관리법 제32조(승강기의 안전검사), 2025-01-31, https://www.law.go.kr/LSW/lsSideInfoP.do?docCls=jo&joBrNo=00&joNo=0032&lsiSeq=259475&urlMode=lsScJoRltInfoR, 접근일 2026-10-12
[^ref-1606]: Christoforos Mavrogiannis 외 (arXiv), Core Challenges of Social Robot Navigation: A Survey, 2021-03-09, https://arxiv.org/abs/2103.05668, 접근일 2026-10-12
[^ref-1589]: Teledyne FLIR, Measuring temperatures (FLIR 사용 설명서 T810605, latest), 미확인, https://docs.flir.com/T810605/en-US/latest/s10.html, 접근일 2026-10-12
[^ref-1610]: Clearpath Robotics, ROS 2 — Getting Started (Clearpath Robotics Documentation, ROS 2 Jazzy), 2026-02-11, https://docs.clearpathrobotics.com/docs/ros/, 접근일 2026-10-12
[^ref-1611]: Clearpath Robotics, Jackal User Manual, 2025-08-28, https://docs.clearpathrobotics.com/docs_robots/outdoor_robots/jackal/user_manual_jackal/, 접근일 2026-10-12
[^ref-1612]: Clearpath Robotics, ROS 2 Robot API — Overview (Clearpath Robotics Documentation, ROS 2 Jazzy), 2025-05-13, https://docs.clearpathrobotics.com/docs/ros/api/overview/, 접근일 2026-10-12
