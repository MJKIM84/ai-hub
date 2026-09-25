# 스토리텔러 산출 2026-09-25-64

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md | draft | seed → draft: 3~11절 첫 작성(접근 제어 구조, 규제·한국 개인영상 규정, 출하·입고 시나리오, 경계·연결·열린 질문), 페이지 상태 자동 영역 추가, 13절 각주. 2차: 7절 첫 문장을 [의견]으로 바꾸고 ref-031 각주 제거, 8절 학술 자료 문장 수정 |
| create | docs/topics/2026/2026-09-25-area26-s6.md | draft | 자동 분리: 26. 사이버보안·접근권한·개인정보 의 "6. 대표 접근법과 기술" 절(1,606자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area26-s7.md | draft | 자동 분리: 26. 사이버보안·접근권한·개인정보 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다. 2차: 첫 문장을 [의견]으로 바꾸고 ref-031 각주 제거, NIST 행에서 '산업용 IoT' 삭제 |
| create | docs/topics/2026/2026-09-25-area26-s3.md | draft | 자동 분리: 26. 사이버보안·접근권한·개인정보 의 "3. 왜 중요한가" 절(1,078자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area26-s11.md | draft | 자동 분리: 26. 사이버보안·접근권한·개인정보 의 "11. 열린 질문" 절(1,016자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area26-s4.md | draft | 자동 분리: 26. 사이버보안·접근권한·개인정보 의 "4. 핵심 개념과 용어" 절(1,004자)을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area26-s10.md | draft | 자동 분리: 26. 사이버보안·접근권한·개인정보 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(771자)을 옮겼다. 형식 재작성: 3절 세부영역 링크 9개를 주제 페이지 위치 기준 경로(../../categories/…)로 고쳤다 |
| create | docs/topics/2026/2026-09-25-area26-s8.md | draft | 자동 분리: 26. 사이버보안·접근권한·개인정보 의 "8. 대표 연구와 자료" 절을 옮겼다. 2차: 첫 문장의 학술 논문 성격 서술을 바로잡았다 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 26. 사이버보안·접근권한·개인정보 | 영역 심화: 3~11절 첫 작성(SROS 2·Open-RMF·VDA 5050·MQTT 접근 제어, 로봇 안전·EU·한국 개인영상 규정, 출하·입고 시나리오, 새 열린 질문 5건) | run 2026-09-25-64
- 홈 최근 업데이트: 2026-09-25 — 26. 사이버보안·접근권한·개인정보: 영역 심화로 3~11절 첫 작성(명령 권한의 세 층, 로봇 보안 규제, 원격 유지보수·카메라 영상 시나리오)
- 대분류 최근 업데이트: 2026-09-25 — 26. 사이버보안·접근권한·개인정보: 영역 심화 초안 작성, 외부 유지보수 권한과 영상·작업자 데이터 제약 정리
- 세부영역 최근 업데이트: 2026-09-25 — 26. 사이버보안·접근권한·개인정보: 3~11절 첫 작성(신뢰도 medium, 새 열린 질문 5건)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 보안 구역과 도관 | Zones and Conduits (IEC 62443) | 공통 보호 요구를 공유하는 시스템·구성요소 묶음(구역)과 두 개 이상의 구역을 잇는 통신 채널 묶음(도관)으로 산업 제어 시스템을 나눠 보호하는 IEC 62443의 구조다. | 26, 10, 11 | ref-618 |
| new | 권한 파일 | Permissions File (DDS-Security) | DDS 참여자의 권한을 담은 서명된 XML 문서로, ROS 2 보안에서 참여자마다 도메인 보호 방식을 정한 거버넌스 파일과 함께 둔다. | 26, 11 | ref-009 |
| new | 이동형 영상정보처리기기 | Mobile Video Information Processing Device | 업무 목적으로 운영할 때 개인정보 보호법 제25조의2가 공개된 장소에서의 촬영을 제한하는, 이동하며 영상을 촬영하는 기기다. | 26, 18, 27 | ref-620 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-009 | Open Robotics (ROS 2 Design) | ROS 2 DDS-Security integration | 오픈소스 문서 | medium | https://design.ros2.org/articles/ros2_dds_security.html |
| ref-010 | Open Robotics (ROS 2 Design) | ROS 2 Robotic Systems Threat Model | 오픈소스 문서 | medium | https://design.ros2.org/articles/ros2_threat_model.html |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — VDA5050_EN.md (VDA 5050 Version 3.0.0) | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-610 | Open Robotics (ROS 2 Design) | ROS 2 Access Control Policies | 오픈소스 문서 | medium | https://design.ros2.org/articles/ros2_access_control_policies.html |
| ref-611 | Open Robotics (ROS 2 Design) | ROS 2 Security Enclaves | 오픈소스 문서 | medium | https://design.ros2.org/articles/ros2_security_enclaves.html |
| ref-405 | Open Robotics (osrf/ros2multirobotbook) | Programming Multiple Robots with ROS 2 — Security | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/security.html |
| ref-613 | Eclipse Foundation (Eclipse Mosquitto) | mosquitto.conf man page | 오픈소스 문서 | medium | https://mosquitto.org/man/mosquitto-conf-5.html |
| ref-471 | Association for Advancing Automation (A3) | Updated ISO 10218 \| Answers to Frequently Asked Questions (FAQs) | 업계 보고서 | medium | https://www.automate.org/robotics/blogs/updated-iso-10218-faq |
| ref-615 | NIST | NIST SP 800-82 Rev. 3, Guide to Operational Technology (OT) Security | 정부·연구기관 | medium | https://csrc.nist.gov/pubs/sp/800/82/r3/final |
| ref-616 | CISA | Mobile Industrial Robots Vehicles and MiR Fleet Software (ICSA-21-280-02) | 정부·연구기관 | medium | https://www.cisa.gov/news-events/ics-advisories/icsa-21-280-02 |
| ref-617 | CSA / IEC (ANSI Webstore) | CAN/CSA IEC 62443-3-3-2017 - Industrial communication networks - Network and system security - Part 3-3: System security requirements and security levels (Adopted IEC 62443-3-3:2013, first edition, 2013-08) | 표준 | medium | https://webstore.ansi.org/standards/csa/csaiec624432017-2442576 |
| ref-618 | Jaatun 외(Journal of Cybersecurity and Privacy 6(2), 52) | Security Aspects of Zones and Conduits in IEC 62443 | 논문 | medium | https://www.mdpi.com/2624-800X/6/2/52 |
| ref-620 | 법제처 국가법령정보센터 | 개인정보 보호법 | 정부·연구기관 | medium | https://www.law.go.kr/lsEfInfoP.do?lsiSeq=195062 |
| ref-621 | 김·장 법률사무소 | '이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서' 관련 인사이트 | 업계 보고서 | medium | https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=30477 |
| ref-622 | 법제처 국가법령정보센터 | 근로자참여 및 협력증진에 관한 법률 | 정부·연구기관 | medium | https://www.law.go.kr/LSW/lsInfoP.do?lsiSeq=105636 |
| ref-623 | 한국인터넷진흥원(KISA) | 로봇 보안취약점 점검 체크리스트 해설서 | 정부·연구기관 | medium | https://kisa.or.kr/2060205/form?lang_type=KO&page=&postSeq=36 |
| ref-624 | European Commission (Shaping Europe's digital future) | The Cyber Resilience Act - Summary of the legislative text | 정부·연구기관 | medium | https://digital-strategy.ec.europa.eu/en/policies/cra-summary |
| ref-555 | European Union (EUR-Lex) | Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery | 정부·연구기관 | medium | https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 물류센터 내부처럼 공개되지 않은 작업장에서 카메라를 단 로봇이 작업자를 촬영할 때 개인정보 보호법 제25조의2와 근로자 감시 설비 협의 가운데 무엇이 적용되는지 공식 해석이 있는가? | 26, 18 | 열림 | — |
| new | — | 외부 유지보수 계정의 권한을 로봇·명령 단위로 나눈 매트릭스(예: 진단은 허용, 이동은 불허)를 공개한 로봇 관제·ROP 구성이나 표준이 있는가? | 26, 9 | 열림 | — |
| new | — | 여러 화주가 로봇 플릿을 공유하는 창고에서 고객별 작업·데이터 격리를 오케스트레이션 수준에서 규정한 표준이나 공개 설계가 있는가? | 26, 28 | 열림 | — |
| new | — | ISO 10218-1:2025 의 사이버보안 요구는 어느 조항에서 무엇(접근 제한·원격 접속·로그 등)을 요구하며 로봇 관제 연동에 어떤 조건을 주는가? | 26, 25 | 열림 | — |
| new | — | EU 기계 규정 부속서 III 1.1.9 의 적용일이 사이버 복원력법(2027-12-11)에 맞춰 연기되는지 확정됐는가? | 26, 25 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 출하 | 시작 조건 | docs/categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 26. 사이버보안·접근권한·개인정보 |
| 출하 | 작업 대상 | docs/categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 26. 사이버보안·접근권한·개인정보 |
| 출하 | 수행 자원 | docs/categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 26. 사이버보안·접근권한·개인정보 |
| 출하 | 제약 | docs/categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 26. 사이버보안·접근권한·개인정보 |
| 출하 | 완료·인계 | docs/categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 26. 사이버보안·접근권한·개인정보 |
| 출하 | 예외·성과 | docs/categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 26. 사이버보안·접근권한·개인정보 |
| 입고 | 시작 조건 | docs/categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 26. 사이버보안·접근권한·개인정보 |
| 입고 | 작업 대상 | docs/categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 26. 사이버보안·접근권한·개인정보 |
| 입고 | 수행 자원 | docs/categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 26. 사이버보안·접근권한·개인정보 |
| 입고 | 제약 | docs/categories/g-safety-security-intelligence-and-governance/26-cybersecurity-access-control-and-privacy.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 26. 사이버보안·접근권한·개인정보 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| NIST SP 800-82 Rev. 3 Guide to Operational Technology (OT) Security | 프레임워크 | NIST | 26, 10 | ref-615 | https://csrc.nist.gov/pubs/sp/800/82/r3/final |
| Eclipse Mosquitto (MQTT 브로커, mosquitto.conf ACL·인증서 인증) | 오픈소스 | Eclipse Foundation | 26, 9, 11 | ref-613 | https://mosquitto.org/man/mosquitto-conf-5.html |
| SROS 2 접근 제어 정책(ROS 2 Access Control Policies) | 프레임워크 | ROS 2 Design | 26, 11 | ref-610 | https://design.ros2.org/articles/ros2_access_control_policies.html |
| ROS 2 보안 인클레이브(ROS 2 Security Enclaves) | 프레임워크 | ROS 2 Design | 26, 10, 11 | ref-611 | https://design.ros2.org/articles/ros2_security_enclaves.html |
| KISA 로봇 보안취약점 점검 체크리스트 해설서 | 프레임워크 | 한국인터넷진흥원(KISA) | 26 | ref-623 | https://kisa.or.kr/2060205/form?lang_type=KO&page=&postSeq=36 |

## 추가 조사 요청

- 4절·7절: IEC 62443-3-3 원문 또는 IEC 공식 자료로 7개 기본 요구와 보안 수준(SL 1~4)의 정의를 확인해야 한다 — ref-617 이 검증에서 실재·내용 미확인이어서 [추정]으로만 썼고 '보안 수준' 용어집 후보도 이번에 내지 않았다.
- 3절·11절: ISO 10218-1:2025 의 사이버보안 조항 번호와 요구 내용(접근 제한·원격 접속·로그 등)을 ISO 원문이나 독립 해설로 확인해야 한다 — 현재 A3 FAQ 한 건 기준이다.
- 5절·7절: 개인정보보호위원회 '이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서' 원본과 발행일을 확인해야 한다 — 현재 법률사무소 해설(ref-621)을 거친 2차 자료라 [추정]으로 강등됐다.
- 3절: CISA ICSA-21-280-02 의 발행일과 영향 제품 판을 확인해야 한다 — 기준일을 확인일로만 두었다.
- 7절: 개인정보 보호법 제25조의2 시행일과 근로자참여법 제20조의 호 번호를 원문으로 확인해야 한다.
- 7절: NIST SP 800-82 Rev. 3 의 범위에 산업용 IoT 가 포함되는지 원문으로 확인해야 한다 — 검색 요약에서 직접 확인하지 못해 2차 지시로 본문에서 뺐다.
- 8절: 물류 로봇·AMR 관제 보안을 직접 다룬 학술 연구를 찾아야 한다 — 이번 조사에서 확인한 학술 논문은 IEC 62443 구역·도관 논문 한 건뿐이다.
- 11절: oq-082(보고값 위조 검증 기준), oq-056(설비 어댑터 인클레이브 단위), oq-043(출입통제 연동 권한)에 답할 공개 설계·사례 조사가 필요하다.
- 3절·11절: EU 기계 규정 부속서 III 1.1.9 적용일의 CRA 정렬·연기 확정 여부를 EU 공식 자료로 확인해야 한다.
- 6절: MiR 등 제조사 관제의 보안 기능·IEC 62443-4-2 정렬 주장은 독립 인증 자료가 있을 때만 다룰 수 있다 — f13 은 출처 미확인으로 삭제됐다.

## 이행한 수정 지시

- f6 표현 수정 — 6절 'VDA 5050과 MQTT 브로커 접근 제어'에서 '보안 통신·데이터 보호 메커니즘을 규정하지 않고 … 계획·운영·유지보수·안전 책임도 배분하지 않는다'로 고쳐 '보안 책임' 표현을 뺐다.
- f7 요구·권고 구분 — 6절에서 '내려받기는 TLS로 보호해야 하고(요구), 활성화 전 인증서 체인 확인은 권고한다'로 나눠 썼다.
- f8 용어 통일 — 4절·6절에서 'RELEASE 유형 구역' 대신 '해제 구역(Release Zone)'으로 쓰고 ../../glossary/release-zone.md 에 연결했다.
- f11 강등 — 4절과 7절 표에서 [추정]으로 쓰고 판 표기를 'IEC 62443-3-3:2013(CSA 2017 채택판 판매 목록 기준)'으로 했으며, ref-617 각주에 ' (원문 미열람)'을 붙였다.
- f12 수정 — 4절에서 '구역 경계에서 통신을 제한·여과' 부분을 빼고 구역·도관 정의만 남겼으며, ref-618 각주·reference_updates 의 발행일을 2026, 기관을 'Jaatun 외(Journal of Cybersecurity and Privacy 6(2), 52)'로 적었다.
- f13 제외 — 본문(6절 포함)에 넣지 않았고 reference_updates 와 각주에서 ref-619 를 뺐다.
- f20 강등 — 5절 시나리오 2 서술과 7절 법규 목록에서 [추정]으로 쓰고 '법률사무소 해설을 거친 2차 자료이며 안내서 발행일 미확인'을 병기했다.
- f16 적용일 한정 — 3절·7절에서 '규정의 일반 적용일은 2027-01-20'으로 쓰고 연기 여부를 단정하지 않았으며, 부속서 III 1.1.9 적용일 연기 확정 여부 질문을 11절과 open_question_updates(영역 26·25)에 더했다.
- f14 기준일 — 3절·8절에서 발행일 미확인, 확인일 2026-09-25 기준으로 적고 최신 취약점 동향을 대표하지 않는다고 밝혔다.
- f21 조항 표기 — 5절·7절에서 '제20조(협의 사항)'까지만 쓰고 '호 번호 미확인'을 병기했다.
- f5 초안 명시 — 3절 첫 문장과 8절에서 'ROS 2 위협 모델 초안(DRAFT, 최종 수정 2021-01)'임을 밝혔다.
- 각주 발행일 — ref-009 2019-07(최종 수정 2020-07), ref-010 2019-03(최종 수정 2021-01), ref-610 2019-08(최종 수정 2021-06), ref-611 2020-05(최종 수정 2020-07)를 각주에 적고 reference_updates published 에 같은 값을 넣었다.
- 원문 미열람 표기 — ref-555·615·616·617·618·620·621·622·623·624 와 ref-471 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었으며, ref-009·010·031·405·610·611·613 에는 표기하지 않았다.
- 용어 정의 축소 — glossary_updates 의 '이동형 영상정보처리기기' 정의를 '업무 목적으로 운영할 때 개인정보 보호법 제25조의2가 공개된 장소에서의 촬영을 제한하는, 이동하며 영상을 촬영하는 기기'로 줄였다.
- 기존 열린 질문 유지 — oq-043·oq-056·oq-082 를 11절에 열림으로 두고 f3·f30 은 부분 근거로만 연결했으며 open_question_updates 에 해결로 내지 않았다.
- 분량 초과 자동 분리: 26. 사이버보안·접근권한·개인정보 본문 10,220자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 3,687자
- 형식 재작성: docs/topics/2026/2026-09-25-area26-s10.md 3절의 세부영역 링크 9개(9·10·13·18·19·24·25·27·28)가 원 세부영역 페이지 기준 상대 경로로 남아 깨졌으므로 주제 페이지 위치 기준 ../../categories/<대분류 slug>/<파일>.md 로 고쳤다. 내용·태그·각주는 바꾸지 않았다.
- 2차: 7절 첫 단락 태그 — 세부영역 페이지 7절과 docs/topics/2026/2026-09-25-area26-s7.md 의 1. 세 줄 요약·3. 본문 첫 문장을 '이 위키가 이번 실행의 출처 상태를 정리하면, 기술 근거는 대부분 단일 공식 문서이고 법규·표준은 검색 요약 기준(원문 미열람)이다. [의견]'으로 고치고 이 문장에서 ref-031 각주를 뺐다(ref-031 은 s7 표의 VDA 5050 행 등 다른 문장에서만 쓴다).
- 2차: 8절 첫 단락 출처 성격 — 세부영역 페이지 8절과 docs/topics/2026/2026-09-25-area26-s8.md 의 1. 세 줄 요약·3. 본문 첫 문장을 '이번 조사에서 확인한 학술 논문은 IEC 62443 구역·도관 논문(ref-618) 한 건이며, 물류 로봇 보안을 직접 다룬 학술 연구는 확인하지 못했다'로 고치고, 이 위키의 정리임을 문장 앞에 밝혔다.
- 2차: NIST SP 800-82 Rev. 3 행 — docs/topics/2026/2026-09-25-area26-s7.md 3절 표의 NIST 행에서 '산업용 IoT'를 빼고 건물 자동화·물리적 출입통제와 SP 800-53 Rev. 5 OT 오버레이는 그대로 두었다. reference_updates 의 ref-615 요약에서도 같은 표현을 뺐다.
