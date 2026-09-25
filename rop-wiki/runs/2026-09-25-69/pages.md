# 스토리텔러 산출 2026-09-25-69

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md | draft | seed → draft: 3~11절 첫 작성, 페이지 상태 자동 영역 추가, 13절 각주. 2차: 9절 승강기 연계 칸 [추정]으로 정정, ISO 10218-2 적용 범위 미확인 단서 추가, 5절 시작 조건 칸에 가상 설정 표시와 [추정] 태그 추가 |
| create | docs/topics/2026/2026-09-25-area28-s7.md | draft | 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,840자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area28-s6.md | draft | 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "6. 대표 접근법과 기술" 절(1,549자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area28-s11.md | draft | 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "11. 열린 질문" 절(1,233자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area28-s4.md | draft | 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "4. 핵심 개념과 용어" 절(1,053자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area28-s3.md | draft | 자동 분리: 28. 표준·상호운용성·다사업자 거버넌스 의 "3. 왜 중요한가" 절(802자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 28. 표준·상호운용성·다사업자 거버넌스 | seed → draft: 3~11절 첫 작성(규격 구속력·데이터 권리, 판 번호·폐기 예고·적합성 시험, 입고·출하 시나리오, 책임 경계·연결·열린 질문), f12 추정 강등 반영, 2차 수정(9절 태그·단서, 5절 시작 조건 태그) | run 2026-09-25-69
- 홈 최근 업데이트: 2026-09-25 — 28. 표준·상호운용성·다사업자 거버넌스: 3~11절 첫 작성(VDA 5050 판 정책·책임 분리, 적합성 시험, 데이터 권리 법제, 감사·서비스 수준)
- 대분류 최근 업데이트: 2026-09-25 — 28. 표준·상호운용성·다사업자 거버넌스: seed → draft, 3~11절 첫 작성과 13절 각주
- 세부영역 최근 업데이트: 2026-09-25 — 28. 표준·상호운용성·다사업자 거버넌스: 3~11절 첫 작성(실행 2026-09-25-69), 트랙 반영 제안 가운데 VDA 5050·MassRobotics 분만 7절에 반영

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 의미적 버전 관리 | Semantic Versioning (SemVer) | 공개 API 를 선언하고 호환되지 않는 변경·하위 호환 기능 추가·하위 호환 수정을 각각 MAJOR·MINOR·PATCH 번호로 올려 변경의 호환성을 판 번호로 알리는 규칙이다. | 28, 24, 9 | ref-706, ref-031 |
| new | 서비스 수준 협약 | Service Level Agreement (SLA) | 서비스 제공자와 고객이 가용성·응답 시간 같은 측정 가능한 서비스 목표를 합의해 문서로 정한 것이다. | 28, 20 | ref-716 |
| new | 감사 추적 | Audit Trail | 누가 언제 무엇을 했는지를 시간 순서로 남긴 변경·접근·명령 기록으로, 사후에 책임과 원인을 확인하는 데 쓴다. | 28, 26 | ref-715 |
| new | 산업데이터 | Industrial Data | 산업 활동 과정에서 생성·활용되는 데이터(산업디지털전환촉진법의 용어). | 28 | ref-708 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/rmf-core.html |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-051 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/state.schema | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/state.schema |
| ref-407 | gpue (GitHub) | vda5050-sim — README (Standards-compliant VDA5050 (v3.0.0) robot fleet simulator — MQTT or NATS) | 오픈소스 문서 | medium | https://github.com/gpue/vda5050-sim |
| ref-408 | ekusiadadus (GitHub) | vda5050-lab — README (Diagnose VDA 5050 order, reconnect, and cancel failures from MQTT traces) | 오픈소스 문서 | medium | https://github.com/ekusiadadus/vda5050-lab |
| ref-608 | OTTO by Rockwell Automation | OTTO Adds VDA 5050 Certifications to Support Mixed-Fleet Deployments | 벤더 문서 | low | https://ottomotors.com/company/newsroom/press-releases/otto-adds-vda-5050-certifications-to-support-mixed-fleet-deployments/ |
| ref-704 | VDA / VDMA / KIT IFL (VDA5050 GitHub) | VDA5050/VDA5050 — README | 표준 | medium | https://github.com/VDA5050/VDA5050 |
| ref-253 | MassRobotics | AMR_Interop_Standard — MassRobotics AMR Interoperability Standard (README, JSON schema) | 표준 | medium | https://github.com/MassRobotics-AMR/AMR_Interop_Standard |
| ref-706 | Semantic Versioning (Tom Preston-Werner, semver.org) | Semantic Versioning 2.0.0 | 오픈소스 문서 | medium | https://semver.org/spec/v2.0.0.html |
| ref-707 | European Union (EUR-Lex) | Regulation (EU) 2023/2854 of the European Parliament and of the Council of 13 December 2023 on harmonised rules on fair access to and use of data (Data Act) | 정부·연구기관 | medium | https://eur-lex.europa.eu/eli/reg/2023/2854/oj/eng |
| ref-708 | 국가법령정보센터(산업통상자원부) | 산업 디지털 전환 촉진법 (법률 제18692호) | 정부·연구기관 | medium | https://www.law.go.kr/법령/산업디지털전환촉진법/(18692,20220104) |
| ref-709 | 소프트웨어정책연구소(SPRi) | 산업 디지털 전환 촉진법의 의미와 시사점 | 정부·연구기관 | medium | https://spri.kr/posts/view/23480?code=industry_trend |
| ref-710 | Open Source Robotics Alliance (Open Robotics) | osra-policies-and-procedures — README | 오픈소스 문서 | medium | https://github.com/openrobotics/osra-policies-and-procedures |
| ref-711 | Open Source Robotics Alliance | Charter of the Open Source Robotics Alliance Project 'Open-RMF' | 오픈소스 문서 | medium | https://osralliance.org/wp-content/uploads/2024/03/open-rmf-project-charter.pdf |
| ref-712 | OPC Foundation | How to Certify - OPC Foundation | 표준 | medium | https://opcfoundation.org/certification/how-to-certify/ |
| ref-713 | IETF (RFC Editor) | RFC 9745: The Deprecation HTTP Response Header Field | 표준 | medium | https://www.rfc-editor.org/info/rfc9745/ |
| ref-560 | ISO | ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells | 표준 | medium | https://www.iso.org/standard/73934.html |
| ref-715 | IEC | IEC 62443-3-3:2013 Industrial communication networks — Network and system security — Part 3-3: System security requirements and security levels (sample) | 표준 | medium | https://cdn.standards.iteh.ai/samples/19488/7c0b753be32e46fc986c23c32efbdbe8/IEC-62443-3-3-2013.pdf |
| ref-716 | ISO/IEC | ISO/IEC 20000-1:2018 - Information technology — Service management — Part 1: Service management system requirements | 표준 | medium | https://www.iso.org/standard/70636.html |
| ref-717 | 대한민국 정책브리핑(산업통상자원부 국가기술표준원) | 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 | 정부·연구기관 | medium | https://korea.kr/news/pressReleaseView.do?newsId=156480155 |
| ref-718 | 한국지능형로봇표준포럼(KOROS) | KOROS 1148-8:2025 서비스 로봇을 위한 모듈 - 제2-8부 : 소프트웨어 모듈용 정보모델 상호운용성 시험 절차 | 표준 | medium | http://www.koros.or.kr/bbs/board.php?bo_table=notice27&wr_id=223 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | ROP 사업자·로봇 제조사·현장 운영사가 함께 만든 로봇 운행·상태 데이터의 사용·수익 권리를 산업디지털전환촉진법의 공동 생성 규정에 따라 계약에서 어떻게 나누는가, 국내 로봇 관제 계약 사례가 있는가? | 28 | 열림 | — |
| new | — | EU 데이터법의 데이터 공유 의무가 이종 로봇 플릿에서 제조사가 ROP 사업자(제3자)에게 로봇 사용 데이터를 제공해야 하는 근거가 되는가, 된다면 그 범위는 무엇인가? | 28, 9 | 열림 | — |
| new | — | KOROS 1148-8:2025 의 상호운용성 시험 절차는 어떤 시험 항목을 두며, 물류 로봇 관제 연동의 적합성 시험 기준으로 쓸 수 있는가? | 28, 23 | 열림 | — |
| new | — | 이종 플릿 현장에서 ROP 가 고객과 맺는 가용성·응답 시간 목표를 제조사 관제·설비업체의 서비스 수준 목표와 어떻게 연쇄해 맞추며, 공개된 계약 구조나 사례가 있는가? | 28, 20 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 입고 | 시작 조건 | docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 28. 표준·상호운용성·다사업자 거버넌스 |
| 입고 | 수행 자원 | docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 28. 표준·상호운용성·다사업자 거버넌스 |
| 출하 | 시작 조건 | docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 28. 표준·상호운용성·다사업자 거버넌스 |
| 출하 | 수행 자원 | docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 28. 표준·상호운용성·다사업자 거버넌스 |
| 출하 | 제약 | docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 28. 표준·상호운용성·다사업자 거버넌스 |
| 출하 | 예외·성과 | docs/categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 28. 표준·상호운용성·다사업자 거버넌스 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| Semantic Versioning 2.0.0 | 프레임워크 | Semantic Versioning (semver.org) | 28, 24 | ref-706 | https://semver.org/spec/v2.0.0.html |
| IETF RFC 9745 The Deprecation HTTP Response Header Field | 표준 | IETF | 28, 1 | ref-713 | https://www.rfc-editor.org/info/rfc9745/ |
| IEC 62443-3-3:2013 시스템 보안 요구사항과 보안 수준 | 표준 | IEC | 28, 26 | ref-715 | https://cdn.standards.iteh.ai/samples/19488/7c0b753be32e46fc986c23c32efbdbe8/IEC-62443-3-3-2013.pdf |
| ISO/IEC 20000-1:2018 서비스 관리 시스템 요구사항 | 표준 | ISO/IEC | 28 | ref-716 | https://www.iso.org/standard/70636.html |
| KOROS 1148-8:2025 서비스 로봇을 위한 모듈 — 제2-8부: 소프트웨어 모듈용 정보모델 상호운용성 시험 절차 | 표준 | 한국지능형로봇표준포럼(KOROS) | 28, 23 | ref-718 | http://www.koros.or.kr/bbs/board.php?bo_table=notice27&wr_id=223 |
| OPC Foundation 인증 프로그램(적합성 시험 도구 CTT·독립 시험소 인증) | 평가 프로그램 | OPC Foundation | 28, 23 | ref-712 | https://opcfoundation.org/certification/how-to-certify/ |

## 추가 조사 요청

- 9절·3절: VDA 5050 3.0.0 2 Scope 의 '운영자·통합자·차량 제조사·관제 제공자 사이 책임을 배분하지 않는다(Operational Responsibilities)' 문구를 finding 으로 올려 책임 경계 서술을 [사실]로 보강할 필요가 있다(1차 검증 노트 제안).
- 7절: 트랙 반영 제안 10건(2026-09-25-11·16·19·28·35·36·41·44·47·53·54 — IEEE 1872·AAS·ECLASS·IEC CDD·IDTA·ISO 22166·IFC·IndoorGML·ISO 19164·VDMA LIF·CAD 레이어·SHACL·IDS)은 이번 실행에서 재확인하지 못해 반영하지 않았다. 해당 출처 메타데이터를 입력에 넣고 재확인해야 한다.
- 7절: 국가기술표준원이 발표한 로봇 엘리베이터 탑승 KS 의 번호가 표준 목록의 KS B 7317 과 같은지 확인이 필요하다(oq-041 관련).
- 3절: EU 데이터법 주요 조항의 적용 개시일을 EUR-Lex 원문으로 확인해야 한다.
- 3절: 산업디지털전환촉진법 2025-05-27 일부개정 판(법률 제20964호)에서 산업데이터 공동 생성 조문이 같은지 확인해야 한다.
- 7절·9절: KOROS 1148-8:2025 의 시험 항목과 ISO 22166 계열과의 관계, ISO 10218-2:2025 의 물류 이동로봇 플릿 적용 여부 확인이 필요하다.
- 6절: 물류 로봇 다사업자 SLA 의 공개 계약 구조·사례, 그리고 VDA 5050 공식 적합성 시험 유무(oq-055)를 추가 조사해야 한다.

## 이행한 수정 지시

- f12 강등 — 7절·8절에서 Open-RMF 거버넌스 문장을 [추정]으로 쓰고 '2024-04-15 운영 시작'을 빼고, 개정 경로를 'TGC 문서는 TGC 승인·OSRF 이사회 비준, 저장소 목록·작업반 헌장은 해당 PMC 비준'으로 나눠 썼다.
- f11 수정 — 6절에서 '플릿 능력을 가정하지 않고 전체 제어·신호등·읽기 전용 세 수준으로 통합하고, 인터페이스 없음은 RMF 와 호환되지 않는다'로 고치고 용어집 '플릿 제어 수준' 링크로 표기했다.
- f2 구분 — 7절과 9절에서 '관제가 교착 탐지·해소 기능을 맡는다'와 '교통 조율 알고리즘 자체와 안전 요구는 VDA 5050 범위 밖'을 별도 문장으로 썼다.
- f17 — 3절에 발효일 2024-01-11 만 [사실]로 쓰고 '주요 조항의 적용 개시일은 미확인이다'를 덧붙였다.
- f18 — 3절에 '법률 제18692호, 2022-01-04 공포 기준'을 적고 '2025-05-27 일부개정 판에서 같은 조문인지는 미확인'을 덧붙였다.
- f16 — 7절 문장의 기준일을 '2025-06-04, KOROS 게시일, 원문 미열람'으로 고치고 각주·참고문헌 발행일도 2025-06-04 로 맞췄다.
- f13 — 6절·7절에서 '인증서'를 빼고 '인증 로고'만 썼다.
- f15 — 6절에 '[추정] 벤더 주장' 표기와 시험 항목·주체 미확인 문구를 유지했다.
- f8·f14·f19·f21·f24·f26·f27·f28·f30 — 모두 [추정] 태그를 유지했고, 9절 f21 문장에 '이를 정한 공식 기준은 확인되지 않았다'를 그대로 두었다.
- 각주 — fetched false 출처 15건(ref-407·408·608·253·707·708·709·711·712·713·560·715·716·717·718)의 각주 정의 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었다.
- 7절 트랙 반영 — VDA 5050(f1·f2·f4·f5·f29)과 MassRobotics(f9·f10)만 반영하고 'VDA 5050 3.0.0 발행 2026-03'과 'MassRobotics 1.0' 판 표기는 싣지 않았으며(발행일은 oq-005 로 유지), 나머지 10건은 반영하지 않았다.
- 산업데이터 용어 — glossary_updates 정의를 '산업 활동 과정에서 생성·활용되는 데이터(산업디지털전환촉진법의 용어)'로 줄이고 권리 규정은 3절 본문에서 다뤘다.
- 서비스 수준 협약 용어 — glossary_updates 정의에서 '미달 시 처리 방식'을 뺐다.
- 11절 — oq-005·055·091·096·041·026 을 열림으로 유지하고 open_questions_new 4건을 새 질문으로 쓰고 open_question_updates 에 new 로 냈다.
- 2차: 9절 표 '시설·설비 제어' 행 — 외부 연계 칸 '연계 대상: 승강기 안전기준·제어.'의 태그를 [사실]에서 [추정][^ref-717]로 고쳤다.
- 2차: 9절 ISO 10218-2:2025 문장(f20) — 문장 뒤에 '물류 이동로봇 플릿에 적용되는지는 미확인이다.'를 덧붙였다.
- 2차: 5절 표 '시작 조건' 칸 — (입고)·(출하) 두 문장에 '(설명용 가상 설정)'을 밝히고, 셀 끝(출하 문장 뒤)에 [추정][^ref-031][^ref-051]을 붙였다.
- 2차: fixes_applied '각주' 항목 — 원문 미열람 출처 목록의 'ref-705'·'ref-714'를 'ref-253'·'ref-560'으로 고쳤다.
