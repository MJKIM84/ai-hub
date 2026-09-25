# 리서치 브리프 2026-09-25-69

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-25-69 |
| 날짜 | 2026-09-25 |
| 실행 유형 | area_deep_dive (영역 심화) |
| 대상 영역 | 28. 표준·상호운용성·다사업자 거버넌스 |
| 대분류 | G. 안전·보안·지능·거버넌스 |

## 갭(비어 있거나 약한 섹션)

- 섹션 3. 왜 중요한가 비어 있음
- 섹션 4. 핵심 개념과 용어 비어 있음(적합성 시험·ECLASS·의미 식별자는 용어집에 있으나 의미적 버전 관리·서비스 수준 협약·감사 추적·산업데이터 없음)
- 섹션 5. 현장 시나리오 비어 있음(물류 흐름 단계 명시 필요)
- 섹션 6. 대표 접근법과 기술 비어 있음
- 섹션 7. 관련 표준·프레임워크·오픈소스 비어 있음(트랙 반영 제안 12건 대기)
- 섹션 8. 대표 연구와 자료 비어 있음
- 섹션 9. ROP가 직접 맡는 것과 외부와 연계하는 것 비어 있음
- 섹션 10. 다른 연구영역과의 연결 비어 있음
- 섹션 11. 열린 질문 비어 있음(oq-004·005·020·025·026·027·041·044·055·065·085·089·091·096 이 이 영역에 걸려 있음)

## 조사 질문

1. 제조사·ROP·설비업체 중 누가 연동 오류를 수정하고 변경을 승인할까? [분류원문]
2. 로봇–관제 공통 규격(VDA 5050, MassRobotics AMR 상호운용 표준, Open-RMF)은 누가 관리하고, 각 규격은 관제와 로봇 사이 책임을 어떻게 나누는가? (섹션 3·7·9 겨냥)
3. 공통 규격과 ROP API 의 변경 정책(판 번호 규칙, 하위 호환, 폐기 예고)은 어떻게 정해지는가? (섹션 4·6 겨냥, oq-091 관련)
4. 적합성 시험·인증은 어떤 형태로 운영되는가(OPC UA 인증, VDA 5050 인증 발표, 국내 단체표준 상호운용성 시험 절차)? (섹션 6·7 겨냥, oq-055 관련)
5. 여러 사업자가 함께 만든 로봇 운행 데이터의 소유권·접근권은 국내외 법제에서 어떻게 다뤄지는가? (섹션 3·9 겨냥)
6. 다사업자 운영에서 서비스 수준과 감사 이력은 어떤 표준 요구로 뒷받침되는가? (섹션 4·6·7 겨냥)
7. 한국의 로봇 상호운용·건물 연동 관련 국가표준·단체표준은 무엇이 있는가? (섹션 7 겨냥, oq-041·oq-026 관련)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 은 VDA 와 VDMA 가 개발하고 카를스루에 공대(KIT) 물류연구소(IFL)가 위탁을 받아 개발을 주도하며 공식 GitHub 저장소를 관리하고, 명세는 사용이 선택적이고 구속력이 없다고 밝힌다. | ref-031, ref-704 | 아니오 | medium | 2026-09-25 | — | — |
| f2 | [사실] | VDA 5050 3.0.0 은 주문 배정·경로 계산·교착 탐지와 해소·교통 제어를 관제 쪽, 위치 추정·경로와 동작 실행·상태의 지속 전송을 이동로봇 쪽 책임으로 나누고, 기능·운영·시스템 안전 요구와 교통 관리 로직은 다루지 않는다고 명시한다. | ref-031 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f3 | [사실] | VDA 5050 공식 저장소 README 는 VDA 웹사이트의 공식 PDF 가 GitHub 내용보다 우선하며, 어느 판에 대해서도 지원·유지보수·문제 해결을 받을 법적 권리가 없다고 적는다. | ref-704 | 아니오 | medium | 2026-09-25 | — | — |
| f4 | [사실] | VDA 5050 의 변경은 GitHub 이슈로 제안되고 월례 회의에서 논의되는 이슈에 진행 표시를, 수용된 변경에 반영 예정 판의 마일스톤을 붙이는 방식으로 관리되며, 3.0.1 은 오타·수정, 3.1.0 은 하위 호환 변경용이고 호환을 깨는 4.0.0 은 현재 계획되지 않았다. | ref-704 | 아니오 | medium | 2026-09-25 | — | — |
| f5 | [사실] | VDA 5050 3.0.0 은 의미적 버전 관리를 따라 필수 필드 추가 같은 파괴적 변경은 주 버전, 선택 매개변수 추가 같은 기능 추가는 부 버전, 오타 수정은 수 버전으로 올리고, 메시지 헤더의 version 필드에 [Major].[Minor].[Patch] 형식의 프로토콜 판을 싣는다. | ref-031, ref-051 | 아니오 | medium | 2026-09-25 | — | — |
| f6 | [사실] | 의미적 버전 관리(Semantic Versioning) 2.0.0 은 공개 API 선언을 요구하고, 호환되지 않는 API 변경은 MAJOR, 하위 호환 기능 추가는 MINOR, 하위 호환 버그 수정은 PATCH 를 올리며, 기능을 폐기할 때는 먼저 폐기 표시를 담은 부 버전을 낸 뒤 주 버전에서 제거하도록 권한다. | ref-706 | 아니오 | medium | 2026-09-25 | — | — |
| f7 | [사실] | IETF RFC 9745 는 자원이 폐기되었거나 폐기될 것임을 알리는 Deprecation HTTP 응답 헤더를 정하고, RFC 8594 의 Sunset 헤더와 함께 쓰일 때 Sunset 시각은 Deprecation 시각보다 이르면 안 된다. | ref-713 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f8 | [추정] | ROP 의 API 변경 정책은 상위 업무 시스템에 여는 API 에는 의미적 버전 관리와 폐기 예고·종료 시각 공지를 적용하고, 로봇 쪽에는 VDA 5050 헤더 version 처럼 로봇별 프로토콜 판을 기록해 판 차이를 관리하는 두 갈래로 설계할 수 있어 보인다. | ref-706, ref-713, ref-031, ref-051 | 아니오 | low | 2026-09-25 | — | — |
| f9 | [사실] | MassRobotics AMR 상호운용 표준의 JSON 스키마는 신원 보고(identityReport)와 상태 보고(statusReport) 두 보고 메시지만 정의하고 명령·작업 배정 메시지는 두지 않는다. | ref-253 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f10 | [사실] | MassRobotics AMR 상호운용 표준은 여러 제조사의 AMR 이 같은 현장에서 공존하도록 로봇의 위치·속도·방향·상태(health)·작업 가용성 정보를 공유하게 하는 것을 목적으로 한다. | ref-253 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f11 | [사실] | Open-RMF 는 플릿마다 플릿 어댑터가 제조사 고유 API 를 RMF 교통 일정·협상 인터페이스에 잇게 하고, 연동 수준을 전체 제어(Full Control)·신호등(Traffic Light)·읽기 전용(Read Only)·인터페이스 없음(No Interface)으로 나눠 제조사 관제를 표준화 없이 그 수준에 맞춰 통합한다. | ref-004 | 아니오 | medium | 2026-09-25 | 수행 자원 | — |
| f12 | [사실] | Open-RMF 는 2024-04-15 운영을 시작한 오픈소스 로보틱스 연합(OSRA) 체계에서 프로젝트 관리 위원회(PMC)가 일상 운영을 맡고, 기술 거버넌스 위원회(TGC)가 PMC 활동을 감독하며, 거버넌스 문서 개정은 해당 기구의 승인과 이사회 비준을 거친다. | ref-711, ref-710 | 아니오 | medium | 2024-03 | — | — |
| f13 | [사실] | OPC Foundation 은 규격 적합성을 확인하는 적합성 시험 도구(CTT)를 제공하고, 제조사가 자체 인증하거나 재단이 인정한 독립 시험소의 인증을 받게 하며, 통과 제품에 인증서와 인증 로고를 준다. | ref-712 | 아니오 | medium | 2026-09-25 | — | 원문 미열람 |
| f14 | [추정] | 이번에 읽은 VDA 5050 3.0.0 명세와 저장소 README 에는 공식 적합성 시험·인증 절차가 정의되어 있지 않아 보이며, 확인한 VDA 5050 인증 근거는 제조사–관제 업체 간 인증 발표와 제3자 오픈소스 시험 도구뿐이다(부재 확정 아님). | ref-031, ref-704, ref-608, ref-407, ref-408 | 아니오 | low | 2026-09-25 | — | — |
| f15 | [추정] | OTTO by Rockwell Automation 은 자사 AMR 이 Idealworks·NAiSE·SYNAOS 등 VDA 5050 관제 업체와 인증을 마쳤다고 발표했으나 인증의 시험 항목과 주체는 공개 자료로 확인되지 않았다. | ref-608 | 아니오 | low | 2026-04 | — | 원문 미열람, 벤더 주장 |
| f16 | [사실] | 한국지능형로봇표준포럼(KOROS)은 단체표준 KOROS 1148-8:2025 '서비스 로봇을 위한 모듈 — 제2-8부: 소프트웨어 모듈용 정보모델 상호운용성 시험 절차'를 제·개정 현황에 올렸다. | ref-718 | 아니오 | medium | 2025 | — | 원문 미열람 |
| f17 | [사실] | EU 데이터법(Regulation (EU) 2023/2854, 2023-12-13 채택, 2024-01-11 발효)은 기업·이용자·공공 사이 데이터 접근·이용 규칙을 정하고, 제품 제조사와 데이터 보유자에게 데이터 공유·상호운용성 의무를, 데이터 처리 서비스 제공자에게 고객의 사업자 전환 허용 의무를 둔다. | ref-707 | 아니오 | medium | 2023-12-13 | — | 원문 미열람 |
| f18 | [사실] | 한국 산업디지털전환촉진법은 상당한 투자와 노력으로 산업데이터를 새로 생성한 자에게 사용·수익 권리를 주고, 2인 이상이 공동으로 생성하거나 제3자에게 제공한 경우 당사자 약정이 없으면 각자 사용·수익 권리를 가진다고 정한다. | ref-708, ref-709 | 아니오 | medium | 2022-01-04 | — | 원문 미열람 |
| f19 | [추정] | 로봇 상태·운행 기록처럼 제조사 로봇, ROP, 현장 운영사가 함께 만드는 데이터는 국내법상 공동 생성 데이터로 볼 여지가 있어, 약정이 없으면 각 사업자가 사용·수익 권리를 가지므로 연동 계약에서 데이터 범위·이용 목적·제3자 제공을 따로 정해야 할 것으로 보인다. | ref-708, ref-707 | 아니오 | low | 2026-09-25 | 완료·인계 | 원문 미열람 |
| f20 | [사실] | ISO 10218-2:2025 는 로봇 자체를 다루는 Part 1 과 구분해 산업용 로봇 적용과 로봇 셀의 안전 요구를 다루며, 통합자(integrator)가 합리적으로 예견할 수 있는 위험원과 위험 상황을 대상으로 한다. | ref-560 | 아니오 | medium | 2025-02 | — | 원문 미열람 |
| f21 | [추정] | 분류 원문 질문과 관련해, 확인한 규격을 종합하면 연동 오류 수정 책임은 규격 불일치는 해당 메시지를 구현한 쪽(로봇 제조사 또는 관제), 플릿 어댑터·매핑 오류는 ROP, 시스템 수준 위험과 변경 승인은 통합자 역할을 맡는 쪽으로 나누는 구조가 될 수 있어 보이나, 이를 정한 공식 기준은 확인되지 않았다. | ref-031, ref-004, ref-560, ref-704 | 아니오 | low | 2026-09-25 | 예외·성과 | — |
| f22 | [사실] | IEC 62443-3-3:2013 은 제어 시스템이 감사 대상 이벤트를 기록하고(SR 2.8), 감사 기록에 타임스탬프를 쓰며(SR 2.11), 감사 정보를 보호하도록(SR 3.9) 요구하고, SR 2.8 의 강화 요구로 중앙에서 관리하는 시스템 전체 감사 추적을 둔다. | ref-715 | 아니오 | medium | 2013-08 | — | 원문 미열람 |
| f23 | [사실] | ISO/IEC 20000-1:2018 은 서비스 관리 시스템의 수립·실행·유지·지속 개선 요구사항을 정하는 표준으로, 서비스 수준 관리를 관계·합의 프로세스에 포함한다. | ref-716 | 아니오 | medium | 2018 | — | 원문 미열람 |
| f24 | [추정] | 이종 플릿 환경의 서비스 수준은 ROP 가 고객과 맺는 가용성·응답 목표가 제조사 관제·설비업체의 목표에 기대므로, 서비스 관리 표준의 서비스 수준 관리와 감사 추적 요구를 결합해 사업자별 목표와 장애 귀책을 기록으로 확인하는 구조가 필요해 보인다. | ref-716, ref-715 | 아니오 | low | 2026-09-25 | 예외·성과 | 원문 미열람 |
| f25 | [사실] | 산업통상자원부 국가기술표준원은 2021-11-11 행정안전부(승강기 안전기준 소관)와 협력해 로봇의 엘리베이터 탑승 시 안전 요구사항과 실내 배송 로봇 등에 관한 국가표준(KS)을 제정한다고 밝혔다. | ref-717 | 아니오 | medium | 2021-11-11 | 제약 | 원문 미열람 |
| f26 | [추정] | 출하 단계에서 한 제조사가 로봇 펌웨어를 올려 VDA 5050 프로토콜 판이 바뀌면, 관제가 헤더 version 으로 판 차이를 감지하고 지원하지 않는 선택 필드는 UNSUPPORTED_PARAMETER 오류로 드러나므로, 변경 승인 전 판 호환 시험과 수정 책임을 계약으로 정해 두어야 출하 마감 전 작업 실패를 막을 수 있을 것으로 보인다. | ref-031, ref-051 | 아니오 | low | 2026-09-25 | 출하 / 예외·성과 | — |
| f27 | [추정] | 입고 단계에서 새 제조사 로봇을 등록할 때 MassRobotics 신원 보고의 제조사명·모델·일련번호나 VDA 5050 헤더의 manufacturer·serialNumber 를 감사 기록의 주체 식별자로 쓰면, 이후 연동 오류와 변경 이력을 제조사별로 귀속할 수 있을 것으로 보인다. | ref-253, ref-051 | 아니오 | low | 2026-09-25 | 입고 / 수행 자원 | — |
| f28 | [추정] | 연계 대상: VDA 5050 이 범위 밖으로 둔 기능·시스템 안전과 로봇의 위치 추정·주행 실행은 제조사 쪽이며, 28. 표준·상호운용성·다사업자 거버넌스에서 ROP 몫은 인터페이스 판·적합성·책임 경계를 정하고 확인하는 쪽으로 보인다. | ref-031 | 아니오 | low | 2026-09-25 | — | — |
| f29 | [사실] | VDA 5050 공식 저장소 main 브랜치 명세는 3.0.0 판이며 문서 머리에 발행일이 적혀 있지 않아, 3.0.0 발행일 충돌(oq-005)은 명세 원문으로 해소되지 않는다. | ref-031 | 아니오 | medium | 2026-09-25 | — | — |
| f30 | [추정] | 28. 표준·상호운용성·다사업자 거버넌스는 규격 판·책임 분리로 9. 로봇·제조사 관제 연동, 적합성 시험으로 23. 시험·형식 검증·벤치마크, 판 이행으로 24. 자산·소프트웨어 수명주기 관리, 감사 추적으로 26. 사이버보안·접근권한·개인정보, 통합자 위험성평가로 25. 안전·위험 관리, 승강기 연동 표준으로 10. 설비·건물 시스템 연동과 맞물리는 것으로 보인다. | ref-031, ref-004, ref-712, ref-715, ref-560, ref-717 | 아니오 | low | 2026-09-25 | — | — |

### 근거 발췌

- **f1**: 3.0.0 명세: VDA·VDMA 개발, KIT IFL 이 개발 주도·공식 GitHub 저장소 관리. 'The use of this specification is optional and non-binding'. 두 출처 모두 VDA 측 문서라 독립 아님 (발행일 미확인, 확인일 기준)
- **f2**: 관제: 주문 배정, 경로 계산, 교착 탐지·해소, 교통 제어 / 로봇: 위치 추정, 경로 실행, 동작 실행, 상태 지속 전송. 안전 요구와 교통 관리 로직은 범위 밖으로 명시 (발행일 미확인, 확인일 기준)
- **f3**: README: VDA 웹사이트 공식 PDF 가 GitHub 내용에 우선. 'no legal entitlement to support, maintenance, troubleshooting' (발행일 미확인, 확인일 기준)
- **f4**: README: 이슈에 'VD(M)A in progress' 표시(월례 회의), 수용 변경에 마일스톤. V3.0.1 오타·수정, V3.1.0 비파괴·하위 호환, V4.0.0 파괴적 변경·현재 미계획 (발행일 미확인, 확인일 기준)
- **f5**: 명세: Major = 새 필수 필드 등 파괴적 변경, Minor = 선택 매개변수 추가, Patch = 오타 수정. state.schema 헤더 version 설명 'Version of the protocol [Major].[Minor].[Patch]' (발행일 미확인, 확인일 기준)
- **f6**: 'Software using Semantic Versioning MUST declare a public API.' 폐기 시 폐기 표시를 담은 새 부 버전 발행 후 주 버전에서 제거. 0.y.z 는 초기 개발 (발행일 미확인, 확인일 기준)
- **f7**: 검색 요약: Deprecation 헤더는 URI 로 식별되는 자원의 폐기(예정)를 알리며 자원의 의미·기능 변화를 뜻하지 않는다. Sunset 시각은 Deprecation 시각보다 이를 수 없다 (발행일 미확인, 확인일 기준)
- **f8**: f5·f6·f7 종합. 물류 로봇 관제에 이 정책을 적용한 공개 사례는 확인하지 못함
- **f9**: 스키마: identityReport 필수 uuid·timestamp·manufacturerName·robotModel·robotSerialNumber·baseRobotEnvelope / statusReport 필수 uuid·timestamp·operationalState·location. 명령 메시지 없음 (발행일 미확인, 확인일 기준)
- **f10**: README: 'location, speed, direction, health, tasking / availability and other performance characteristics' 공유로 다수 제조사 AMR 의 공존 지원 (발행일 미확인, 확인일 기준)
- **f11**: 'Each robot fleet ... is expected to have a fleet adapter that connects its fleet-specific API to the interfaces of the core RMF traffic scheduling and negotiation system' (발행일 미확인, 확인일 기준)
- **f12**: 헌장(검색 요약): Open-RMF PMC 가 일상 운영 담당, TGC 가 PMC 감독. P&P 저장소 README: TGC 문서는 TGC 승인·OSRF 이사회 비준, PMC 는 저장소 목록·작업반 헌장 비준. 두 출처 모두 OSRA 측
- **f13**: 검색 요약: 'self-certification' 또는 독립 인증 시험소(Certification Test Lab) 인증 선택, OPC Foundation 인증서·'Certified' 로고 발급 (발행일 미확인, 확인일 기준)
- **f14**: 명세·README 에 인증 절차 언급 없음(읽은 범위 기준). vda5050-sim·vda5050-lab 은 개인 프로젝트이며 VDA·VDMA 공식 시험 아님 (재인용: 2026-09-25-67)
- **f15**: 벤더 주장: OTTO 100·600·1200·1500 이 VDA 5050 관제 업체들과 'certified' 라고 발표(2026-04, 검색 요약)
- **f16**: KOROS 제·개정 현황 게시물 제목 기준. 시험 항목·ISO 22166 계열과의 관계는 원문 미열람으로 미확인
- **f17**: 검색 요약: 'Product manufacturers and holders of data are subject to extensive data sharing and data interoperability requirements', 처리 서비스 제공자는 전환(switching) 허용 의무
- **f18**: 검색 요약: 2022-07 시행. 공동 생성 시 각자 사용·수익 권리, 약정이 있으면 약정에 따름. 제3자 제공 시 생성자와 제3자 모두 권리. 요약이 두 출처 중 어디서 왔는지 구분 불가
- **f19**: f17·f18 을 ROP 운영 데이터에 적용한 추정. 법률 해석·국내 계약 사례는 확인하지 못함
- **f20**: 검색 요약: 'Industrial robot applications and robot cells', 2025-02 발행, 'reasonably foreseeable by the integrator' 위험을 다룸. 물류 이동로봇 플릿 적용 범위는 미확인
- **f21**: f2(관제·로봇 책임 분리, 안전 범위 밖), f11(플릿 어댑터), f20(통합자 위험), f3(표준 기구는 지원 의무 없음) 종합 추정
- **f22**: 검색 요약: SR 2.8 auditable events, SR 2.9 저장 용량, SR 2.10 감사 처리 실패 대응, SR 2.11 타임스탬프, SR 3.9 감사 정보 보호, RE 'centrally managed, system-wide audit trail'
- **f23**: 검색 요약: 'specifies requirements for establishing, implementing, maintaining and continually improving a service management system', 서비스 수준 관리 포함
- **f24**: f22·f23 종합 추정. 물류 로봇 다사업자 SLA 공개 사례·수치는 확인하지 못해 넣지 않음
- **f25**: 보도자료(검색 요약): 속도 제어, 위험 상황 보호 정지, 높낮이차·틈새 극복, 추락·넘어짐 방지 기준. KS 번호는 확인하지 못함
- **f26**: f5 와 이전 실행의 UNSUPPORTED_PARAMETER(CRITICAL) 보고 규정을 결합한 시나리오 (재인용: 2026-09-25-67)
- **f27**: identityReport 필수 manufacturerName·robotModel·robotSerialNumber, VDA 5050 헤더 manufacturer·serialNumber 를 근거로 한 적용 추정
- **f28**: f2 의 범위 제외 문구와 분류 원문 9장 '로봇 자체 지능·제어' 경계를 대조한 추정
- **f29**: raw 명세: 'Version 3.0.0', 머리에 발행일 없음, 저작권자 VDA (발행일 미확인, 확인일 기준)
- **f30**: f2·f11·f13·f22·f20·f25 를 세부영역에 대응시킨 종합

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://osrf.github.io/ros2multirobotbook/rmf-core.html | 아니오 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md | 아니오 |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema | 아니오 |
| ref-407 | gpue (GitHub) | vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/gpue/vda5050-sim | 예 |
| ref-408 | ekusiadadus (GitHub) | vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces) | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/ekusiadadus/vda5050-lab | 예 |
| ref-608 | OTTO by Rockwell Automation | OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments | 2026-04 | 벤더 문서 | low | 2026-09-25 | https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/ | 예 |
| ref-704 | VDA / VDMA / KIT IFL (VDA5050 GitHub) | VDA5050/VDA5050 — README | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/VDA5050/VDA5050 | 아니오 |
| ref-253 | MassRobotics | AMR_Interop_Standard — MassRobotics AMR Interoperability Standard (README, JSON schema) | 미확인 | 표준 | medium | 2026-09-25 | https://github.com/MassRobotics-AMR/AMR_Interop_Standard | 예 |
| ref-706 | Semantic Versioning (Tom Preston-Werner, semver.org) | Semantic Versioning 2.0.0 | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://semver.org/spec/v2.0.0.html | 아니오 |
| ref-707 | European Union (EUR-Lex) | Regulation (EU) 2023/2854 of the European Parliament and of the Council of 13 December 2023 on harmonised rules on fair access to and use of data (Data Act) | 2023-12-13 | 정부·연구기관 | medium | 2026-09-25 | https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng | 예 |
| ref-708 | 국가법령정보센터(산업통상자원부) | 산업 디지털 전환 촉진법 (법률 제18692호) | 2022-01-04 | 정부·연구기관 | medium | 2026-09-25 | https://www.law.go.kr/법령/산업디지털전환촉진법/(18692,20220104) | 예 |
| ref-709 | 소프트웨어정책연구소(SPRi) | 산업 디지털 전환 촉진법의 의미와 시사점 | 미확인 | 정부·연구기관 | medium | 2026-09-25 | https://spri.kr/posts/view/23480?code=industry_trend | 예 |
| ref-710 | Open Source Robotics Alliance (Open Robotics) | osra-policies-and-procedures — README | 미확인 | 오픈소스 문서 | medium | 2026-09-25 | https://github.com/openrobotics/osra-policies-and-procedures | 아니오 |
| ref-711 | Open Source Robotics Alliance | Charter of the Open Source Robotics Alliance Project 'Open-RMF' | 2024-03 | 오픈소스 문서 | medium | 2026-09-25 | https://osralliance.org/wp-content/uploads/2024/03/open-rmf-project-charter.pdf | 예 |
| ref-712 | OPC Foundation | How to Certify - OPC Foundation | 미확인 | 표준 | medium | 2026-09-25 | https://opcfoundation.org/certification/how-to-certify/ | 예 |
| ref-713 | IETF (RFC Editor) | RFC 9745: The Deprecation HTTP Response Header Field | 미확인 | 표준 | medium | 2026-09-25 | https://www.rfc-editor.org/info/rfc9745/ | 예 |
| ref-560 | ISO | ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells | 2025-02 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/73934.html | 예 |
| ref-715 | IEC | IEC 62443-3-3:2013 Industrial communication networks — Network and system security — Part 3-3: System security requirements and security levels (sample) | 2013-08 | 표준 | medium | 2026-09-25 | https://cdn.standards.iteh.ai/samples/19488/7c0b753be32e46fc986c23c32efbdbe8/IEC-62443-3-3-2013.pdf | 예 |
| ref-716 | ISO/IEC | ISO/IEC 20000-1:2018 - Information technology — Service management — Part 1: Service management system requirements | 2018 | 표준 | medium | 2026-09-25 | https://www.iso.org/standard/70636.html | 예 |
| ref-717 | 대한민국 정책브리핑(산업통상자원부 국가기술표준원) | 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 | 2021-11-11 | 정부·연구기관 | medium | 2026-09-25 | https://korea.kr/news/pressReleaseView.do?newsId=156480155 | 예 |
| ref-718 | 한국지능형로봇표준포럼(KOROS) | KOROS 1148-8:2025 서비스 로봇을 위한 모듈 - 제2-8부 : 소프트웨어 모듈용 정보모델 상호운용성 시험 절차 | 2025 | 표준 | medium | 2026-09-25 | http://www.koros.or.kr/bbs/board.php?bo_table=notice27&wr_id=223 | 예 |

### 출처 요약

- **ref-004**: 작업·교통 조율, Fleet Adapter, 설비 연동 구조 참고.
- **ref-031**: VDA 5050 3.0.0 명세 원문. 관제·로봇 책임 분리, 범위 제외, 의미적 버전 규칙.
- **ref-051**: VDA 5050 상태 메시지 JSON 스키마. 헤더 version·manufacturer·serialNumber, 오류 수준 정의.
- **ref-407**: 원문 미열람. 개인 프로젝트의 VDA 5050 3.0.0 시뮬레이터·적합성 시험 묶음. 공식 시험 아님.
- **ref-408**: 원문 미열람. MQTT 기록에서 VDA 5050 주문·재연결·취소 불일치를 진단하는 개인 도구.
- **ref-608**: 원문 미열람. OTTO AMR 이 여러 VDA 5050 관제 업체와 인증을 마쳤다는 벤더 발표.
- **ref-704**: VDA 5050 공식 저장소 README. 기여·이슈 처리 방식, 계획 판(3.0.1·3.1.0·4.0.0), 공식 PDF 우선과 지원 의무 부인 문구.
- **ref-253**: MassRobotics 공식 저장소. 다수 제조사 AMR 공존 목적, identityReport·statusReport 두 보고 메시지 스키마.
- **ref-706**: 공개 API 선언과 MAJOR·MINOR·PATCH 증가 규칙, 폐기 절차를 정한 버전 관리 명세.
- **ref-707**: 원문 미열람. EU 데이터법. 연결 제품 데이터 접근·공유, 제조사·데이터 보유자의 공유·상호운용성 의무, 처리 서비스 전환 의무.
- **ref-708**: 원문 미열람. 산업데이터 생성자의 사용·수익 권리, 공동 생성·제3자 제공 시 권리 귀속 규정.
- **ref-709**: 원문 미열람. 산업 디지털 전환 촉진법의 내용과 시사점 분석.
- **ref-710**: OSRA 정책·절차 문서 저장소. TGC 문서 승인·이사회 비준, PMC 의 저장소 목록·작업반 헌장 비준, 개정 제안 절차.
- **ref-711**: 원문 미열람. Open-RMF 프로젝트 헌장. 프로젝트 리더·PMC·작업반 구성과 PMC 의 일상 운영 책임.
- **ref-712**: 원문 미열람. OPC 제품의 자체 인증·독립 시험소 인증 절차와 적합성 시험 도구 안내.
- **ref-713**: 원문 미열람. 자원 폐기(예정)를 알리는 Deprecation HTTP 응답 헤더와 Sunset 헤더(RFC 8594)와의 관계.
- **ref-560**: 원문 미열람. 산업용 로봇 적용·로봇 셀의 안전 요구. 통합자가 예견 가능한 위험을 대상으로 함.
- **ref-715**: 원문 미열람. 산업 자동화·제어 시스템의 시스템 보안 요구. 감사 대상 이벤트·타임스탬프·감사 정보 보호 요구 포함.
- **ref-716**: 원문 미열람. 서비스 관리 시스템 요구사항 표준. 서비스 수준 관리 포함.
- **ref-717**: 원문 미열람. 로봇 엘리베이터 탑승 안전 요구사항·실내 배송 로봇 KS 제정 보도자료.
- **ref-718**: 원문 미열람. 서비스 로봇 소프트웨어 모듈 정보모델의 상호운용성 시험 절차 단체표준 제·개정 게시물.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md | 3, 4, 5, 6, 7, 8, 9, 10, 11 | seed 페이지 3~11절 첫 작성. 3절: f21(분류 원문 질문, 추정), f1·f3(표준 기구는 구속력·지원 의무 없음), f17·f18(데이터 권리 법제) / 4절: f6(의미적 버전 관리), f7(폐기 예고), f22(감사 추적), f23(서비스 수준 관리), f18(산업데이터) / 5절: f26(출하·예외·성과), f27(입고·수행 자원) / 6절: f4·f5·f6·f7·f8(변경 정책), f13·f14·f15(적합성 시험·인증, f15 벤더 주장 병기), f19·f24 / 7절: f1·f2·f4·f5·f29(VDA 5050, 트랙 반영 제안 2026-09-25-02 의 3.0.0 판 확인분), f9·f10(MassRobotics, 2026-09-25-02 f13 확인분), f11·f12(Open-RMF·OSRA), f13(OPC UA 인증), f16·f25(국내 단체표준·KS), f17·f18·f20·f22·f23 / 8절: f14 근거 도구 / 9절: f21·f24(직접), f28('연계 대상') / 10절: f30 / 11절: oq-005·055·091·096·041·026 유지와 open_questions_new 4건. 다음 실행 후보: 트랙 반영 제안 12건 중 IEEE 1872·AAS·ECLASS·IEC CDD·IDTA·ISO 22166·IFC·IndoorGML·ISO 19164·LIF·CAD 레이어·SHACL·IDS 관련(2026-09-25-11·16·19·28·35·36·41·44·47·53·54)은 출처 메타데이터가 입력에 없어 이번에 재확인하지 못했다. |

## 용어 후보

| 용어(한글) | 용어(영문) | 한 줄 정의 |
|---|---|---|
| 의미적 버전 관리 | Semantic Versioning (SemVer) | 공개 API 를 선언하고 호환되지 않는 변경·하위 호환 기능 추가·하위 호환 수정을 각각 MAJOR·MINOR·PATCH 번호로 올려 변경의 호환성을 판 번호로 알리는 규칙이다. |
| 서비스 수준 협약 | Service Level Agreement (SLA) | 서비스 제공자와 고객이 가용성·응답 시간 같은 측정 가능한 서비스 목표와 미달 시 처리 방식을 합의해 문서로 정한 것이다. |
| 감사 추적 | Audit Trail | 누가 언제 무엇을 했는지를 시간 순서로 남긴 변경·접근·명령 기록으로, 사후에 책임과 원인을 확인하는 데 쓴다. |
| 산업데이터 | Industrial Data | 한국 산업디지털전환촉진법에서 산업 활동 과정에서 생성·활용되는 데이터로, 상당한 투자로 이를 생성한 자에게 사용·수익 권리가 인정된다. |

## 열린 질문

새로 생긴 질문:

- ROP 사업자·로봇 제조사·현장 운영사가 함께 만든 로봇 운행·상태 데이터의 사용·수익 권리를 산업디지털전환촉진법의 공동 생성 규정에 따라 계약에서 어떻게 나누는가, 국내 로봇 관제 계약 사례가 있는가? | 관련 영역: 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f18 | 종류: 일반
- EU 데이터법의 데이터 공유 의무가 이종 로봇 플릿에서 제조사가 ROP 사업자(제3자)에게 로봇 사용 데이터를 제공해야 하는 근거가 되는가, 된다면 그 범위는 무엇인가? | 관련 영역: 28. 표준·상호운용성·다사업자 거버넌스, 9. 로봇·제조사 관제 연동 | 근거: f17 | 종류: 일반
- KOROS 1148-8:2025 의 상호운용성 시험 절차는 어떤 시험 항목을 두며, 물류 로봇 관제 연동의 적합성 시험 기준으로 쓸 수 있는가? | 관련 영역: 28. 표준·상호운용성·다사업자 거버넌스, 23. 시험·형식 검증·벤치마크 | 근거: f16 | 종류: 일반
- 이종 플릿 현장에서 ROP 가 고객과 맺는 가용성·응답 시간 목표를 제조사 관제·설비업체의 서비스 수준 목표와 어떻게 연쇄해 맞추며, 공개된 계약 구조나 사례가 있는가? | 관련 영역: 28. 표준·상호운용성·다사업자 거버넌스, 20. 예외 복구·재계획·업무 연속성 | 근거: f24 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 21 · 교차 확인: 0
- 예산 사용량: 검색 18회 · 신규 출처 15건
- 미확인 항목:
    - 모든 finding 교차 확인 없음(단일 출처이거나 같은 기관 출처 쌍: f1 은 VDA 명세·README, f12 는 OSRA 헌장·정책 저장소, f5 는 VDA 명세·스키마)
    - f18 검색 요약 문구가 ref-708·ref-709 중 어느 출처에서 왔는지 구분 불가
    - f17 EU 데이터법의 적용 개시일(2025-09-12)은 법률사무소 검색 요약에만 있어 넣지 않음
    - f25 로봇 엘리베이터 탑승 KS 의 번호·세부 메시지 미확인(oq-041 미해결)
    - f16 KOROS 1148-8:2025 시험 항목과 ISO 22166 계열 관계 미확인
    - f15 OTTO VDA 5050 인증의 시험 항목·주체 미확인(벤더 주장)
    - ref-704·ref-253·ref-706·ref-709·ref-710·ref-712·ref-713 발행일 미확인
    - oq-005 VDA 5050 3.0.0 발행일은 명세 원문에 날짜가 없어 해소 못 함(f29)
    - oq-055 VDA 5050 공식 적합성 시험 부재는 읽은 명세·README 범위에서만 확인(f14), 해결 제안하지 않음
- 범위 경계 위반 의심:
    - f28: 기능·시스템 안전과 로봇 주행 실행은 분류 원문 9장 로봇 자체 지능·제어 경계라 '연계 대상:' 표시
    - f25: 승강기 안전기준·제어는 시설·설비 제어 경계라 표준 존재만 기술하고 10. 설비·건물 시스템 연동과의 연결로 제안
    - f20: ISO 10218-2 는 산업용 로봇 셀 표준이라 물류 이동로봇 적용은 미확인으로 명시
    - f17·f18·f19: 법 해석은 ROP 직접 범위가 아니며 계약 조건으로 반영할 과제로만 제안
- 한계: web_fetch_available: false · fetch_mode mirror_only. raw.githubusercontent.com 으로 원문을 연 출처: ref-031(VDA5050_EN.md), ref-051(state.schema), ref-004(rmf-core.md), ref-704(VDA5050 README), ref-253(MassRobotics README·JSON 스키마), ref-706(semver.md), ref-710(OSRA P&P README). 나머지 14건은 검색 요약 기준 원문 미열람(신뢰도 상한 medium). 원문을 연 출처가 있어도 공통 규칙 0절 6항에 따라 high 는 주지 않았다. 신규 출처 15건(ref-704~ref-718, 예약 구간 안)으로 신규 출처 상한에 도달해 실외이동로봇 운행안전인증(KIRIA)·국내 로봇 표준화 로드맵 논문은 넣지 못했다. 재사용 6건(ref-004·031·051·407·408·608)은 이전 브리프·역할 규칙 예시의 값을 썼다. 트랙 반영 제안 12건 가운데 VDA 5050 3.0.0 판(2026-09-25-02)과 MassRobotics(2026-09-25-02 f13)는 f29·f9·f10 으로 확인했고, 나머지(IEEE 1872·AAS·ECLASS·IEC CDD·IDTA·ISO 22166·IFC·IndoorGML·ISO 19164·VDMA LIF·CAD 레이어 표준·SHACL·IDS)는 해당 ref id 의 메타데이터가 입력에 없어 이번 실행에서 재확인하지 못하고 다음 실행 후보로 남겼다. 한국 자료: 산업디지털전환촉진법(ref-708), SPRi(ref-709), 국가기술표준원 보도자료(ref-717), KOROS 단체표준(ref-718). 8. 실시간 세계 상태·데이터 일관성과 22. 시뮬레이션·예측용 디지털 트윈 관련 주장 없음. 27. AI·학습·적응과 모델 운영 관련 주장 없음. 정정 요청 없음. 해결된 열린 질문 없음.
