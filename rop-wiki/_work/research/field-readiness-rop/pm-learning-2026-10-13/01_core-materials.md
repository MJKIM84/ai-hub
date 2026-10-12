# 로봇 서비스 PM 핵심 학습 자료

조사·접근일: **2026-10-13 KST**. 인터넷에 공개된 원문을 열어 관련 절을 확인했다. 아래 18개 학습 단위는 주자료와 필요한 공식 보조문서로 구성한다. 전문 전체를 읽었다는 의미는 아니다. 발행·개정일이 없는 웹 문서는 이를 명시하고 접근일로만 식별한다. 검색 엔진의 수집일·저작권 연도는 발행일로 사용하지 않는다.

과제 번호: **① 서비스·사업, ② ROP·연동, ③ 구축·운영**. 먼저 읽기는 S01·02·04·05·07·08·09·11·14, 나머지는 심화다. 각 문서에서 사용하는 S번호 링크는 이 파일의 **URL·일자·판·관련 절·한계** 전체를 참조한다.

근거 표기: **[제조사 문서]**는 제조사 사양·설명이며 현장 실증과 구별한다. 성능·효과 홍보는 **[제조사 주장]**으로 쓴다. **[운영기관 보고]**도 독립 감사 결과는 아니다. **[연구]**, **[표준·법령]**, **[PM 제안]**, **[미확인]**을 구별한다.

|자료|연결 과제|읽을 부분과 핵심 내용|PM이 내려야 할 결정|한계|
|---|---|---|---|---|
|S01 Robotnik RB-SUMMIT 자료 묶음 / 먼저|①②③|제품 구성, 운동학, RLC·Command Manager|구매 구성과 추가 개발 범위|R&D AMR이며 완제품 배송·안내 서비스가 아님|
|S02 Boston Dynamics Spot 제품·기체 설명 / 먼저|①③|사양, 추가 Arm·센서, 구형 Gamma 구별|계단·점검 수요가 추가 비용을 정당화하는가|웹과 구형 기체 사양 상충|
|S03 Spot Payload Configuration / 심화|①③|질량·무게중심·다리 간섭|센서·적재함·Arm을 함께 장착할 수 있는가|적재량은 물체 조작 능력이 아님|
|S04 Spot SDK / 먼저|②③|GraphNav 피드백, Robot Services, 5.2 변경|명령 소유권·단절·복구 계약|SDK 사용 가능과 현장 안전성은 별개|
|S05 NAVER 1784 / 먼저|①②③|Rookie, ROBOPORT, ARC, Works assistant|로봇과 빌딩·직원 앱을 함께 설계할 범위|운영기관이자 기술 공급자의 소개; ROI 미공개|
|S06 BMW Hams Hall / 심화|①③|SpOTTO의 시각·열·음향 점검과 후속 활용|이동 성공 대신 유효한 측정과 조치를 정의|회사 발표; 독립 검증·효과 수치 부족|
|S07 Open-RMF Fleet Integration / 먼저|②|Full Control·Traffic Light·adapter callbacks|제조사 제어 수준에 맞는 조율 범위|SDK 어댑터와 제품별 검증은 직접 필요|
|S08 Open-RMF Doors and Lifts / 먼저|②③|지도 식별자와 설비 어댑터|승강기·문 업체와 연동 책임/권한 합의|물리 개조·설비 인증을 대신하지 않음|
|S09 VDA 5050 / 먼저|②③|범위, order, state, cancel, maps|판·선택 기능·에러 의미의 적합성 시험|안전·시설·고객 IT API는 별도|
|S10 ROS 2 QoS와 MQTT / 심화|②③|신선도·생존 확인·전달 보장|상태와 명령에 다른 통신 정책 적용|QoS는 실물 업무 완료 보장이 아님|
|S11 NIST 로봇 시험 방법 / 먼저|③|변수 통제, 반복, 성능 측정|미션 조건을 반복 가능한 인수시험으로 변환|응급 대응 도메인의 합격 수치를 전용하지 않음|
|S12 ISO 13482 / 심화|③|공개 scope·제외 대상·판 상태|개인 지원 서비스 로봇 적용성 검토 의뢰|유료 전문 미열람, 인증 판단 불가|
|S13 ISO 3691-4 / 심화|③|무인 산업차량과 운영 구역|산업 운반 용도 및 운영 구역 검토 의뢰|유료 전문 미열람, 모든 서비스 로봇에 자동 적용 안 됨|
|S14 개인정보 보호법 / 먼저|①②③|제25조의2 이동형 영상|로비·사무실 영상의 법적 근거·표시·권리 처리|구역의 공개성, 실제 데이터 처리 방식별 판단 필요|
|S15 개인정보위 공식 해설 / 심화|①③|처리 단계별 준수·권고, 위탁·학습 활용|영상 최소 수집·보관·처리업체 책임|2024 해설; 2026 법령과 함께 읽기|
|S16 소방·승강기 법령 / 심화|②③|피난시설 관리, 승강기 안전검사|충전·대기 위치와 연동 변경 승인|개별 건물·변경공사의 적법성 결론은 별도|
|S17 Social Robot Navigation Survey / 심화|①③|§5 평가 지표와 실험 방법|안내 완주·추종 유지·불편·접근성 평가|연구 종합; 특정 제품의 수용성 수치 아님|
|S18 FLIR 측정 매뉴얼 / 심화|①③|초점·측정 범위·방사율·반사온도·거리|점검 데이터의 유효성 기준|G series 매뉴얼이며 Spot 기본 센서 사양이 아님|

## S01

**Robotnik — RB-SUMMIT 및 Software solutions**

- [현재 제품 페이지](https://robotnik.eu/products/mobile-robots/rb-summit/): 발행·개정일/하드웨어 세부 판 미표시. 읽은 절: Mobile Robot ideal for R&D applications, Technical specifications, Components, RB-SUMMIT+, Robotnik’s Software.
- [공식 데이터시트](https://robotnik.eu/wp-content/uploads/2024/05/Robotnik_Datasheet_RB-SUMMIT_2024_EN.pdf): **CF: 06.24**, 2024-06 표기, Standard version, p1~2. 구동 방식·4개 모터·치수·구성표 확인. PDF 원문 텍스트 열람 성공, 도구의 이미지 렌더링은 cache miss.
- [Software solutions](https://robotnik.eu/software-solutions/): 개정일·배포판 미표시. Open Architecture, RLC and Command Manager, Advanced Localization and Navigation.
- [제조사 ROS 2 시뮬레이션 README](https://github.com/RobotnikAutomation/robotnik_simulation/blob/jazzy-devel/README.md): `jazzy-devel`, 개정일 미확인. Supported Robots에서 RB-SUMMIT `skid-steering` 확인. **읽기만 했고 실행하지 않았다.** 시뮬레이션 공개는 실기 SDK 전체 공개의 증명이 아니다.
- 핵심 근거 구절: 데이터시트 “Skid steering / Omnidirectional (mecanum)”; 제품 페이지 “payload of 50 kg”.
- [제조사 문서] 현재 페이지는 50 kg, 최대 5시간, 최대 2.5 m/s, IP54, 5G router·충전소 등을 제시한다. 2024 표의 3 m/s·기본 4G·IP50/53과 구성이 다르다. 어느 값을 실제 구매품에 적용할지는 견적 구성표로 확정한다.
- 적용: 차체를 배송함·안내 화면·점검 센서와 결합하는 **개발형 AMR 후보**로 읽는다. 공개 자료만으로 국내 공용 공간 운행 승인, 정확한 회전 공간, 최신 실기 제어 API 권한·라이선스·유지보수 SLA를 확정하지 않는다.

## S02

**Boston Dynamics — Spot 제품 및 About Spot**

- [현재 제품 페이지](https://bostondynamics.com/products/spot/): 일자·제품 세부 판 미표시. Spot Specifications, Equip Spot for success, Extend Spot’s reach.
- [About Spot](https://dev.bostondynamics.com/docs/concepts/about_spot.html): SDK 문서 **5.2.0**, 개정일 미표시. Robot specifications의 대상은 **Spot Gamma**. Environment, Power, Payload, Sensing, Connectivity.
- 근거 구절: 현재 제품 “Runtime may vary depending on payloads and environmental factors”; SDK “Robot type | Spot Gamma”.
- [제조사 문서] 현재 페이지에는 최대 적재 14 kg, 평균 운용 90분, 배터리 564 Wh·충전 60분이 있다. Gamma 설명에는 605 Wh·충전 120분이 있다. 현재 웹의 길이 `110mm (43.3 in)`는 단위 불일치가 있어 확정 치수로 채택하지 않았다.
- 적용: 카탈로그 최대 단차와 계단 형태·적재·조명·마찰을 함께 확인한다. 구형 Gamma의 환경 값이나 배터리 값을 최신 구매품에 합치지 않는다. 동적 보행자 안전성은 정적 장애물 회피 문구만으로 판단하지 않는다.

## S03

**Boston Dynamics — Payload Configuration Requirements**

- [공식 SDK 원문](https://dev.bostondynamics.com/docs/payload/payload_configuration_requirements.html): **5.2.0**, 개정일 미표시.
- 읽을 절: Payload ports / width / length / height / weight / leg Interference / under arm clearance.
- 근거 구절: “The Spot Arm weighs 8 kg.”
- [제조사 문서] 합산 페이로드 한도 14 kg에 Arm도 들어간다. 무게중심과 다리의 운동 범위, 자기 복귀 때의 간섭을 고려한다. 본체의 운반 한도에서 Arm 질량을 뺀 값을 곧바로 손으로 들 수 있는 물체 질량으로 해석하지 않는다.
- 적용: 센서·브래킷·통신 장치·적재함·내용물의 질량표와 장착 도면을 구매 전에 검토한다. 문 열기와 자동 상하차는 별도 Arm·그리퍼·소프트웨어·문 형태별 검증 대상이다.

## S04

**Boston Dynamics — Spot SDK 실행과 복구**

- [GraphNav and Robot Locomotion](https://dev.bostondynamics.com/docs/concepts/autonomy/graphnav_and_robot_locomotion.html): **5.2.0**, 개정일 미표시. NavigateTo/Route/Anchor, Status and feedback, Autonomous navigation errors.
- [Robot Services](https://dev.bostondynamics.com/docs/concepts/robot_services.html): **5.2.0**, 개정일 미표시. 인증 이후의 time sync·lease, estop, robot-command, robot-state, log-status, image.
- [Release Notes](https://dev.bostondynamics.com/docs/release_notes.html): 열람 시 상단 **Release 5.2.0**, 발행일 미표시. Breaking Changes, Keepalive, Missions/Autowalk, Orbit Sample Code.
- 근거 구절: GraphNav “STATUS_LOST”; Services “acquires a lease”; Release Notes “HaltRobot”.
- [제조사 문서] 도착 피드백과 위치 정밀 확인은 다르며 LOST와 STUCK도 다르다. 명령 ID·기한·피드백을 추적한다. 5.2에는 Keepalive의 halt/motors-off 구분 및 기존 일부 점검 서비스의 변경이 기록돼 있다.
- 적용: 로봇별 단절 동작을 버전 고정 후 시험한다. 전원 차단이 모든 상황에서 안전한 정지는 아니다. Orbit v1 예제와 기존 v0 클라이언트 차이도 배포 전 확인한다. SDK 호출 성공을 실제 서비스 완료로 간주하지 않는다.

## S05

**NAVER — 1784 공식 운영 소개**

- [운영기관 원문](https://www.navercorp.com/en/service/1784): 발행·개정일, ARC/Rookie 제품판 미표시. 페이지의 다른 뉴스 날짜를 본문 날짜로 전용하지 않는다.
- 읽을 절: Rookie, ROBOPORT, ARC System, Works assistant.
- 근거 구절: “A single app that assists with daily tasks.”
- [운영기관 보고] 직원 앱의 로봇 배송, 로봇 전용 승강기, 클라우드·5G 기반 다중 로봇 시스템을 함께 소개한다.
- 적용: 이용자 서비스와 건물 설비를 함께 기획한 사례로 활용한다. 로봇 전용 승강기가 있는 빌딩의 경험을 기존 공용 승강기 빌딩의 비용·성공률로 옮길 수 없다. 구매 가능한 4휠 제품의 구동 방식 근거로 사용하지 않는다.

## S06

**BMW Group — Good boy SpOTTO, Hams Hall**

- [운영기관 보도자료](https://www.press.bmwgroup.com/united-kingdom/article/detail/T0441735EN_GB/%E2%80%9Cgood-boy-spotto%E2%80%9D%3A-robot-dog-scans-and-monitors-manufacturing-equipment-at-bmw-group-plant-hams-hall?language=en_GB): **2024-05-07**, 기체·페이로드 상세판 미표시.
- 읽을 절: 첫 본문, Three-dimensional digital twin 설명, A reliable maintenance watchdog.
- 근거 구절: “visual, thermal and acoustic sensors”.
- [운영기관 보고] 시각·열·음향 데이터를 디지털 트윈과 보전에 활용하며 설비 온도·압축공기 누출 점검을 소개한다.
- 적용: 순찰 결과를 보전 티켓·검사·조치 완료와 연결하는 설계 근거다. 본체 기본 센서만으로 전부 수행한다고 해석하지 않는다. 절감액·탐지 정확도·장기 무개입률은 이 자료로 입증되지 않는다.

## S07

**Open Robotics — Mobile Robot Fleet Integration**

- [공식 문서](https://osrf.github.io/ros2multirobotbook/integration_fleets.html): 웹 가이드, 발행·개정일/고정 배포판 미표시. C++ API, Python Bindings, Fleet Adapter Template.
- 근거 구절: “the path can be interrupted at any time and replaced”.
- [표준·공식 구현 문서] Full Control 설명은 경로 명령·중단/교체·현재 위치 제공을 전제로 한다. Traffic Light는 pause/resume 중심이다. `RobotCommandHandle`/`RobotUpdateHandle`, EasyFullControl callback을 통해 제조사 API와 연결한다.
- 적용: 제조사와 ‘우리가 어느 수준까지 명령·중단·위치 확인을 할 수 있는가’를 먼저 확인한다. Open-RMF를 깔면 모든 제조사 로봇을 같은 수준으로 제어한다는 제안은 피한다. 결제·사용자·물품 인계·안전 인증은 별도 설계다.

## S08

**Open Robotics — Doors 및 Lifts**

- [Doors](https://osrf.github.io/ros2multirobotbook/integration_doors.html), [Lifts](https://osrf.github.io/ros2multirobotbook/integration_lifts.html): 웹 가이드, 발행·개정일/고정판 미표시. 각각 Map requirements, Integration.
- 근거 구절: Doors “only automated doors can be integrated”; Lifts “lift controller accepts commands”.
- [공식 구현 문서] 문·승강기 이름과 층을 지도에 대응시키고 제어 가능한 설비와 어댑터를 연결한다.
- 적용: API 사용권, 관리주체·설비 업체 승인, 수동 운전·화재 모드·오래된 상태 처리를 협의한다. 종이 도면에 승강기가 존재한다는 이유로 API가 있다고 가정하지 않는다. 구체적인 예약·점유 상태 계약은 프로젝트 제안으로 별도 작성한다.

## S09

**VDA·VDMA — VDA 5050 Version 3.0.0**

- [공식 원문 고정 태그](https://github.com/VDA5050/VDA5050/blob/3.0.0/VDA5050_EN.md), [발행 기록](https://github.com/VDA5050/VDA5050/releases): 발행 설명 **2026-03-19**, GitHub release 표시는 03-18 UTC. **3.0.0**. 공식 저장소가 안내하는 VDA PDF와 차이가 있으면 PDF 우선이므로 계약 동결 시 대조해야 한다.
- 읽을 절: **§2 Scope, §4.1, §5.3~5.4, §6.1.2~6.1.4, §6.3, §6.6, §6.10, §7.2~7.8**.
- 근거 구절: “Operational Responsibilities”; “orderId and same orderUpdateId”.
- [표준] fleet control–mobile robot 사이 통신 명세다. 시설·외부 IT 인터페이스, 안전·보안 구현, 프로젝트 책임 할당은 범위 밖이다. 주문 갱신·취소·중복·오래된 갱신·지도 오류를 읽는다.
- 적용: 기능 지원표와 양방향 적합성 시험을 계약에 넣는다. Spot/RB-SUMMIT이 이 판을 기본 지원하는지는 **미확인**이다. ROP 상위 서비스 API와 같은 것으로 취급하지 않는다.

## S10

**ROS 2 Jazzy QoS 및 OASIS MQTT 5.0**

- [ROS 공식 문서 원본](https://raw.githubusercontent.com/ros2/ros2_documentation/jazzy/source/Concepts/Intermediate/About-Quality-of-Service-Settings.rst): `jazzy` branch, 개정일 미표시. QoS policies, QoS profiles, QoS events. docs.ros.org 화면은 접근 차단되어 공식 저장소 원본으로 회복했다.
- [MQTT 원문](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html): **OASIS Standard 5.0, 2019-03-07**, **§4.3.1~4.3.3**.
- 근거 구절: ROS “expired messages are silently dropped”; MQTT “QoS 2: Exactly once delivery”.
- [표준·공식 문서] ROS의 deadline·lifespan·liveliness는 서로 다른 개념이다. MQTT의 QoS는 메시지 전달 규칙이다.
- [PM 제안] API 재요청·DB 저장·제조사 명령·실물 인계까지 한 번만 수행되게 하려면 각각의 중복 방지와 재조정이 필요하다. 메시지 QoS만으로 업무의 exactly-once를 주장하지 않는다.

## S11

**NIST — Performance of Emergency Response Robots**

- [원문](https://www.nist.gov/programs-projects/performance-emergency-response-robots): 발행 **2014-04-28**, 갱신 **2026-04-24**, 프로젝트 공식 웹 문서.
- 읽을 절: 반복 가능한 test apparatus/procedures/metrics 설명, 환경 변수를 단계적으로 도입하는 문단.
- 근거 구절: “Variables are controlled initially to measure baseline performance.”
- [공식 연구·시험 방법] 기본 성능을 측정한 뒤 조명·젖음 등 변수를 추가하고 반복해 능력을 평가한다.
- 적용: 같은 지도·하중·설정에서 반복, 이후 단일 변수와 복합 조건을 시험한다. 사무빌딩 로봇의 법정 합격 수치나 상용 안전 인증 근거로 NIST 응급 대응 시험 각도를 전용하지 않는다.

## S12

**ISO — ISO 13482:2014**

- [공식 초록·판 상태](https://www.iso.org/standard/53820.html): **Edition 1, 2014-02**, 2020 확인; 접근 시 Published이며 ISO/FDIS 13482 대체판 개발 중 표시.
- 읽은 범위: Abstract, General information, Life cycle. **유료 전문 미열람.**
- 근거 구절: “mobile servant robot”.
- [표준] personal care 로봇의 범위·유형과 제외 대상을 공개 초록에서 확인했다.
- 적용: 고객 용도가 해당 분류인지 안전 전문 담당자가 판단하고 원문·제품 선언을 확보한다. 이 조사로 충돌 힘·정지 거리·속도 한계·인증 적합성을 확정하지 않는다. 4족이라는 외형만으로 적용 여부를 결정하지 않는다.

## S13

**ISO — ISO 3691-4:2023**

- [공식 초록·판 상태](https://www.iso.org/standard/83545.html): **Edition 2, 2023-06**, 접근 시 Published; ISO/DIS 3691-4 개발 중. 2020판은 폐지·대체 표시를 확인했다.
- 읽은 범위: Abstract, General information, Next version. **유료 전문 미열람.**
- 근거 구절: “The condition of the operating zone has a significant effect”.
- [표준] 무인 산업차량과 시스템, 운영 구역의 중요성을 설명한다.
- 적용: 산업 운반 구성 및 현장 조건의 안전 검토에 사용한다. ‘AMR’ 명칭만으로 빌딩 안내·4족 점검까지 이 규격의 인증을 보장하지 않는다. 국내 법적 의무·KS 채택판·계약 적용판은 별도 확인한다.

## S14

**대한민국 — 개인정보 보호법 제25조의2**

- [현행 조문 원문](https://www.law.go.kr/LSW/lsSideInfoP.do?docCls=jo&joBrNo=02&joNo=0025&lsiSeq=283839&urlMode=lsScJoRltInfoR): **법률 제21445호, 2026-03-10 개정, 시행 2026-09-11** 표시. 제25조의2 자체 신설일은 2023-03-14로 구별.
- 읽을 절: **제25조의2 제1~4항**. 짧은 구절: “업무를 목적으로”, “공개된 장소”.
- [법령] 공개된 장소에서의 업무 목적 이동형 개인영상 촬영은 법정 허용 사유·제한·고지와 함께 판단해야 한다. 표시했더라도 부당한 권리 침해나 합리적 범위 초과가 허용되는 것은 아니다. 사생활 침해 장소의 제한도 있다.
- 적용: 로비/제한 사무실의 공개성, 촬영과 저장·전송 목적, 거부 대응, 보관·삭제·위탁을 개인정보 담당자와 확정한다. 이 조문 하나로 전체 개인정보 적법성을 판단하지 않는다.

## S15

**개인정보보호위원회 — 개인영상정보 보호·활용 기준 공식 해설**

- [공식 게시문 본문](https://pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS074&mCode=C020010000&nttId=10678): **2024-10-14**, 소개하는 안내서 판은 **2024.9**.
- 읽은 절: ①8대 기본원칙, ②처리 단계별 준수·권고, ③AI 학습 활용, ④보관·관리.
- 근거 구절: “목적에 필요한 범위에서 최소화”.
- [공식 해설] 촬영·이용·제공·보관·파기와 위탁 책임을 구분한다. 특정인 추적·감시 등은 별도 주의가 필요한 사례로 설명한다.
- 한계: **게시문 본문 열람이며 첨부 안내서 PDF 전문 열람으로 계산하지 않는다.** 해설은 2024 기준이므로 S14의 2026 현행 조문과 함께 읽는다. 자율주행용 영상을 마케팅·얼굴 인증·LLM 학습에 전용할 수 있다는 근거가 아니다.

## S16

**대한민국 — 피난시설 관리와 승강기 안전검사**

- [소방시설법 제16조](https://www.law.go.kr/LSW/lsSideInfoP.do?docCls=jo&joBrNo=00&joNo=0016&lsiSeq=236977&urlMode=lsScJoRltInfoR): **법률 제18522호, 2021-11-30**, 조문 화면 시행 **2022-12-01**. [현행 전체법 연결 화면](https://www.law.go.kr/LSW/lsInfoP.do?ancYnChk=0&chrClsCd=010202&efYd=20241201&lsiSeq=236977&urlMode=lsInfoP)은 **2024-12-01** 표시. 동일 법령의 단계별 시행 표시를 구별하며 ‘2024에 제16조가 신설됐다’고 해석하지 않는다.
- [승강기법 제32조](https://www.law.go.kr/LSW/lsSideInfoP.do?docCls=jo&joBrNo=00&joNo=0032&lsiSeq=259475&urlMode=lsScJoRltInfoR): **법률 제20159호, 2024-01-30 개정, 시행 2025-01-31**. 제1항 정기·수시·정밀안전검사.
- 근거 구절: 소방 “장애물을 설치하는 행위”; 승강기 “제어방식”.
- [법령] 피난시설 등의 폐쇄·훼손·장애물 설치를 제한한다. 승강기는 관리주체의 안전검사 의무와 제어방식 변경 등 수시검사 사유를 구별한다.
- 적용: 충전기·적재함·정지 로봇의 피난 방해와 방화문 개방 고정 여부를 검토한다. 모든 로봇 API 연동이 수시검사를 요한다고 단정하지 않고 변경 범위를 설비 업체·관리주체·검사기관에 확인한다.

## S17

**Mavrogiannis 외 — Core Challenges of Social Robot Navigation: A Survey**

- [저자 등록 원문 정보](https://arxiv.org/abs/2103.05668), [PDF](https://arxiv.org/pdf/2103.05668): **arXiv:2103.05668 v2, 2021-03-17**. v1 2021-03-09.
- 읽은 범위: **§5 Core Evaluation Challenges, §5.1 Metrics, §5.2 평가 방법**, PDF p13~20 중심. 논문 전체 정독 아님.
- 근거 구절: “datasets, simulations, and real-world experiments”.
- [연구] 도착 여부뿐 아니라 안전·편안함·사회적 적절성을 평가하고 데이터셋·시뮬레이션·실사용 평가를 구별한다.
- 적용: 안내에서 일행 이탈, 혼잡, 사람의 부담과 직원 인계를 시험한다. 특정 제품의 ‘사람 친화적’ 성능 수치로 인용하지 않는다. 최신 제품 사양이 아닌 평가 관점을 위한 기초 문헌이다.

## S18

**FLIR — Measuring temperatures**

- [공식 매뉴얼](https://docs.flir.com/T810605/en-US/latest/s10.html): **FLIR G series, T810605-AI-en-US**, `latest`, 발행·개정일 미표시.
- 읽은 절: Basic steps, Temperature range, Measurement parameters / Types of parameters.
- 근거 구절: “Emissivity”, “Reflected temperature”, “Object distance”.
- [제조사 문서] 온도 측정에는 초점·측정 범위와 측정 매개변수 설정이 필요하다.
- 적용: 같은 설비에서 거리·각도·초점·방사율·반사조건·교정 정보까지 기록해야 비교 가능한 점검을 설계할 수 있다. 구체 센서 정확도와 설치 조건은 구매 센서 매뉴얼·교정 성적서로 검증한다. 이 문서의 카메라가 특정 Spot 구성에 포함된다는 뜻은 아니다.

## 열람 실패와 미채택 기록

|자료·경로|열람 결과|처리|
|---|---|---|
|RB-SUMMIT 현재 페이지의 [Drive 데이터시트](https://drive.google.com/file/d/1kD_-uBxx74P_0vLDj8EcTcrmP3PTfk0F/view)|뷰어 래퍼만 노출, 최신 PDF 본문 미확인|현재 HTML와 공식 2024 PDF를 분리. 최신 PDF 사양 추측 안 함|
|[Spot lease.html](https://dev.bostondynamics.com/docs/concepts/lease.html)|접근 실패|열린 Robot Services의 lease 설명만 사용|
|[Robotnik robot_simple_command_manager](https://github.com/RobotnikAutomation/robot_simple_command_manager)|cache miss|실기 API 엔드포인트를 만들어 내지 않음. 제조사 Software solutions의 공개 범위만 사용|
|[ROS QoS HTML](https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html)|Anubis Access Denied|공식 ros2_documentation jazzy 원문으로 회복|
|[사회적 주행 논문 HTML v5 시도](https://arxiv.org/html/2103.05668v5)|Internal Error, 해당 판 존재 확인 안 됨|등록 이력 v2와 PDF만 채택. v5 내용 사용 안 함|
|[NSF 논문 미러](https://par.nsf.gov/servlets/purl/10483177)|timeout|저자 arXiv PDF로 회복|
|[CGH 병원 발표 PDF](https://www.nhcs.com.sg/sites/shcommonassets/Documents/News/changi-general-hospital-introduces-three-robots-to-augment-its-care-team-at-the-emergency-department/Media%20Release_CGH%20introduces%20three%20robots%20to%20augment%20its%20care%20team%20at%20the%20Emergency%20Department.pdf)|404|핵심 사례·정량 성과에 사용 안 함|
|개인정보 보호법 시행령 제27조의2 간편 URL 및 [연계 페이지](https://www.law.go.kr/LSW/lsLinkCommonInfo.do?chrClsCd=010202&lspttninfSeq=182197)|Internal Error|상위법 제25조의2와 공식 해설 범위만 사용. 표시 방식의 세부 시행령 적합성은 후속 확인|
|ISO 13482·3691-4 유료 전문|공개 초록만 열람, 전문 미구매|수치·세부 절차·인증 판정의 근거로 쓰지 않음|

[PM 제안] 미확인은 존재하지 않는다는 뜻이 아니다. 제품 가격, API 계약, 유지보수, 국내 인증, 소음, 비용 절감·성공률·수용성은 공급사 문서와 현장 시험으로 닫는다.
