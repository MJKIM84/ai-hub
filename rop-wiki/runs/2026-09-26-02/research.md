# 리서치 브리프 2026-09-26-02

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-26-02 |
| 날짜 | 2026-09-26 |
| 실행 유형 | monthly_recheck (월간 재검증) |
| 대상 영역 | 해당 없음 |
| 대분류 | 해당 없음 |

## 갭(비어 있거나 약한 섹션)

- target.json 이 재검증 대상 목록을 주지 않아(CLI 지정 monthly_recheck) 참고문헌 목록에서 발행 2년이 지난 표준·규정을 골라 재검증 대상으로 삼음
- ref-022 VDA 5050 2.0.0(2022-01): 3.0.0 판과의 관계 재확인 필요
- ref-139 ISO 22400-2:2014: 개정(Amd)·후속판 여부 미기록(4. 성과·경제성·프로세스 개선 7절 인용)
- ref-568 KS B ISO/TS 15066·ref-211 KS B ISO 10218-2: ISO 10218-2:2025 통합 이후 상태 미기록
- ref-470 ISO 3691-4:2023, ref-566 ISO 12100:2010: 개정 진행 여부 미기록
- ref-486 ISO 22301:2019: 개정 1:2024 내용 미기록
- ref-030 W3C SSN(2017): 2023 Edition 초안 존재 여부 미기록
- ref-345 실내공간정보 구축 작업규정(2018)과 ref-679(2021 고시)의 판 관계 미정리
- ref-637 산업 디지털 전환 촉진법 제명 변경(oq-122) 미확인
- ref-509 ISO 20607:2019·ref-510 IEC/IEEE 82079-1:2019 개정 진행 여부 미기록

## 조사 질문

1. 재검증 대상 ref-022 VDA 5050 2.0.0(2022-01): 현행판 여부
2. 재검증 대상 ref-139 ISO 22400-2:2014: 개정·후속판 여부(4. 성과·경제성·프로세스 개선 인용)
3. 재검증 대상 ref-568 KS B ISO/TS 15066(ISO/TS 15066:2016 부합)·ref-211 KS B ISO 10218-2: ISO 10218-2:2025 발행 뒤 상태
4. 재검증 대상 ref-470 ISO 3691-4:2023: 개정 진행 여부
5. 재검증 대상 ref-566 ISO 12100:2010: 개정 진행 여부
6. 재검증 대상 ref-486 ISO 22301:2019: 개정 1:2024 반영
7. 재검증 대상 ref-502 BPMN 2.0.2(2014-01)·ref-119 IEC 62264-3:2016: 현행판 여부(2. 공정·워크플로 모델링 인용)
8. 재검증 대상 ref-767 IEC 62443-3-3:2013: 현행판 여부
9. 재검증 대상 ref-030 W3C SSN(2017-10-19): 후속판 여부
10. 재검증 대상 ref-345 실내공간정보 구축 작업규정(2018-03-05): 현행 고시 여부
11. 재검증 대상 ref-314 KS B 7317(2021-11): 개정 여부
12. 재검증 대상 ref-637 산업 디지털 전환 촉진법(2022-01-04): 제명 변경·시행 여부(oq-122)
13. 재검증 대상 ref-509 ISO 20607:2019·ref-510 IEC/IEEE 82079-1:2019: 개정 진행 여부

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | VDA 5050 공식 저장소 main 브랜치의 최신 게시판은 3.0.0 이므로, ref-022 가 가리키는 VDA 5050 2.0.0(2022-01)은 현행판이 아니라 이전 판으로 대체됨 상태다. | ref-052, ref-032, ref-022 | 아니오 | medium | 2026-09-26 | — | — |
| f2 | [사실] | ISO 22400-2:2014 에는 에너지 관리용 KPI 를 더한 개정 1(ISO 22400-2:2014/Amd 1:2017)이 2017-04 에 발행돼 있어, 4. 성과·경제성·프로세스 개선이 인용하는 ISO 22400-2:2014 는 개정 1과 함께 읽어야 한다. | ref-812, ref-139 | 아니오 | medium | 2017-04 | — | 원문 미열람 |
| f3 | [사실] | ISO 22400-2 는 개정판 ISO/DIS 22400-2 가 진행 중이며 2024-09-17 FDIS 등록이 승인돼 ISO 22400-2:2014 를 대체할 예정으로 표시돼 있으나, 새 판의 발행은 이번 실행에서 확인하지 못했다. | ref-811, ref-139 | 아니오 | medium | 2024-09-17 | — | 원문 미열람 |
| f4 | [사실] | ISO/TS 15066:2016 의 협동 적용 요구사항 대부분은 협동이 로봇 단독이 아닌 적용의 문제라는 이유로 ISO 10218-2:2025 에 통합되었다. | ref-471, ref-560 | 아니오 | medium | 2025-02 | — | 원문 미열람 |
| f5 | [사실] | ISO 목록에서 ISO/TS 15066:2016 은 폐지되지 않고 2022 년 확인된 판으로 남아 있으며, 이를 대체할 ISO/AWI 15066-1(Collaborative Safety)이 개발 초기 단계에 있다. | ref-814, ref-813 | 아니오 | medium | 2026-09-26 | — | 원문 미열람 |
| f6 | [추정] | 국가표준 목록에서 KS B ISO 10218-2 는 '2017 확인', KS B ISO/TS 15066 은 '2022 확인' 판으로 검색되고 ISO 10218-2:2025 를 부합화한 KS 는 이번 검색에서 확인되지 않아, 국내 KS 는 아직 구판(ISO 10218-2:2011·ISO/TS 15066:2016) 기준일 가능성이 있다. | ref-825, ref-568, ref-211 | 아니오 | low | 2026-09-26 | — | 원문 미열람 |
| f7 | [사실] | ISO 3691-4 는 2023 판이 현행이지만 차기판(ISO/CD 3691-4, 제2판 초안)이 위원회 검토 단계에 있다. | ref-819, ref-470 | 아니오 | medium | 2026-09-26 | — | 원문 미열람 |
| f8 | [사실] | ISO 12100:2010 은 개정이 진행 중이며, 독일 DIN 이 개정 초안(DIN EN ISO 12100, 2025-01, ISO/DIS 12100:2024 기반)을 게시했다. | ref-820, ref-566 | 아니오 | medium | 2025-01 | — | 원문 미열람 |
| f9 | [추정] | ISO 12100 개정판은 2026 년 FDIS 단계 도달이 예상되며 2027-01-20 부터 적용되는 EU 기계 규정 2023/1230 에 맞춰 EN ISO 문안을 정렬하는 것으로 보인다. | ref-821, ref-555 | 아니오 | low | 2025-12-11 | — | 원문 미열람 |
| f10 | [사실] | ISO 22301:2019 에는 2024-02 발행된 개정 1(기후 행동 변경)이 있어, 조직 상황(4.1)과 이해관계자(4.2) 조항에서 기후 변화의 관련성 검토를 요구한다. | ref-822, ref-486 | 아니오 | medium | 2024-02 | — | 원문 미열람 |
| f11 | [추정] | OMG BPMN 은 2014-01 발행된 2.0.2 판이 여전히 최신판으로 보이며, 이번 검색에서 그 뒤의 새 판은 확인되지 않았다. | ref-502 | 아니오 | medium | 2026-09-26 | — | 원문 미열람 |
| f12 | [추정] | IEC 62264-3 은 2016 발행 제2판이 최신으로 검색되며, 이번 실행에서 그 뒤의 새 판은 확인되지 않아 2. 공정·워크플로 모델링의 인용은 유효한 것으로 보인다. | ref-119 | 아니오 | medium | 2026-09-26 | — | 원문 미열람 |
| f13 | [추정] | IEC 62443-3-3 은 2013-08 발행 제1판이 현행으로 검색되며, 개정판 진행 상태는 이번 실행에서 확인하지 못했다. | ref-767 | 아니오 | low | 2026-09-26 | — | 원문 미열람 |
| f14 | [사실] | W3C 는 SSN 온톨로지의 후속판 'Semantic Sensor Network Ontology - 2023 Edition' 을 공개 작업 초안(Working Draft)으로 냈고 아직 권고안이 아니므로, 현행 권고안은 ref-030 의 2017 판이다. | ref-817, ref-818, ref-030 | 아니오 | medium | 2025 | — | — |
| f15 | [사실] | IEC/IEEE 82079-1 은 2019 판(제2판)이 현행이며 차기판이 위원회 초안(IEC/IEEE CD 82079-1) 단계에 있다. | ref-823, ref-510 | 아니오 | medium | 2026-09-26 | — | 원문 미열람 |
| f16 | [추정] | ISO 20607:2019 는 디지털 사용 설명서를 반영하는 개정(ISO/DIS 20607)이 진행돼 2025-05-03 국제 투표가 끝났고 EN 채택 기한이 2026-01-20 으로 알려졌으나, 새 판 발행은 이번 실행에서 확인하지 못했다. | ref-824, ref-509 | 아니오 | low | 2026-09-26 | — | 원문 미열람 |
| f17 | [사실] | ref-345 는 실내공간정보 구축 작업규정의 2018-03-05 판을 가리키고, 같은 규정의 고시 제2021-1445호(2021-12-24) 판이 ref-679 로 따로 등록돼 있어 ref-345 는 구판이며, 2021 판 이후 개정 고시는 이번 검색에서 확인되지 않았다. | ref-345, ref-679 | 아니오 | medium | 2021-12-24 | — | 원문 미열람 |
| f18 | [추정] | KS B 7317(2021-11 제정)은 이번 검색에서 개정 기록이 확인되지 않았고 현행 표준으로 검색된다. | ref-314 | 아니오 | low | 2026-09-26 | — | 원문 미열람 |
| f19 | [사실] | 국가법령정보센터에 '산업 디지털 전환 및 인공지능 활용 촉진법' 제명의 법령 제정·개정문 페이지가 존재해, ref-637 이 가리키는 산업 디지털 전환 촉진법의 제명이 바뀐 것으로 확인된다. | ref-815, ref-637 | 아니오 | medium | 2026-09-26 | — | 원문 미열람 |
| f20 | [추정] | 제명이 바뀐 '산업 디지털 전환 및 인공지능 활용 촉진법' 은 2026-07-01 부터 시행된 것으로 보도됐으나, 데이터 공동 생성 규정의 조문 번호·내용 변화는 확인하지 못했다. | ref-816 | 아니오 | low | 2026-09-26 | — | 원문 미열람 |

### 근거 발췌

- **f1**: README 원문(github_raw): "The main branch contains the latest published version of VDA 5050 (currently version 3.0.0)". 향후 3.0.1·3.1.0·4.0.0 계획도 언급. 3.0 발행 보도자료는 ref-032(같은 VDA 계열로 독립 출처 아님). (발행일 미확인, 확인일 기준)
- **f2**: 검색 요약: Amendment 1: Key performance indicators for energy management, Published 2017-04, stage 60.60. 원문 미열람.
- **f3**: 검색 요약: ISO/DIS 22400-2 is expected to replace ISO 22400-2:2014; DIS approved for registration as FDIS on 2024-09-17. 원문 미열람, 발행 여부 미확인.
- **f4**: 검색 요약: most of the requirements of ISO/TS 15066 have been incorporated into ISO 10218-2:2025 because human-robot collaboration relates to the application. A3 FAQ 원문 미열람.
- **f5**: 검색 요약: ISO/TS 15066:2016 last reviewed and confirmed in 2022 … not withdrawn; ISO/AWI 15066-1 in development that will replace it. 원문 미열람.
- **f6**: 검색 결과 제목: 'KS B ISO 10218-2(2017 확인) … 제2부: 로봇 시스템 및 통합', 'KS B ISO TS 15066(2022 확인)'. 부재 확인이 아니라 검색 범위 내 미발견.
- **f7**: 검색 요약: ISO/CD 3691-4 Industrial trucks — … Part 4 (iso.org/standard/88615); ISO 3691-4:2023 is expected to be replaced; a draft is being reviewed by the committee. 원문 미열람.
- **f8**: 검색 요약: DIN EN ISO 12100 - 2025-01 draft standard; revision titled 'Safety of machinery … (ISO/DIS 12100:2024)'. 원문 미열람.
- **f9**: 검색 요약(업계 블로그): ISO/DIS 12100 Ed.2 in second enquiry … could reach FDIS in 2026; ISO/TC 199 and CEN/TC 114 under Vienna Agreement to align with Machinery Regulation applying 20 January 2027. 원문 미열람.
- **f10**: 검색 요약: ISO 22301:2019/Amd 1:2024 Climate action changes, published February 2024; modifies Clause 4.1 and 4.2. 원문 미열람.
- **f11**: 검색 요약: The latest version is BPMN 2.0.2, published in January 2014; OMG 이슈 트래커에 2.0.2 대상 이슈가 2025-08 까지 있으나 BPMN 2.1 발행 정보 없음. 원문 미열람.
- **f12**: 검색 요약: IEC 62264-3:2016 second edition cancels and replaces the 2007 first edition; 후속판 개발 정보는 검색 결과에서 확인되지 않음. 원문 미열람.
- **f13**: 검색 요약: IEC 62443-3-3 currently exists as Edition 1.0, published in August 2013; Edition 2 초안 상태 정보 없음. 원문 미열람.
- **f14**: 작업반 저장소 README 원문(github_raw): 2023 edition 은 Public Working Draft 로 표시. W3C 뉴스: First Public Working Draft … inappropriate to cite this document as other than a work in progress. 두 출처 모두 W3C 계열.
- **f15**: 검색 요약: IEC/IEEE CD 82079-1 (iso.org/standard/87206); a draft is being reviewed by the committee for a new edition; 2019 Ed.2 가 최신 판매판. 원문 미열람.
- **f16**: 검색 요약(업계 뉴스): ISO/DIS 20607 … Close of Voting … ended on 3 May 2025; deadline for adoption by CEN/CENELEC 20 January 2026; 개정 초점은 디지털 사용 설명서. 원문 미열람.
- **f17**: 참고문헌 목록 대조: ref-345 발행 2018-03-05, ref-679 '고시 제2021-1445호, 2021-12-24'. 검색 결과에서도 법령정보센터 최신 경로가 (2021-1445,20211224). 원문 미열람.
- **f18**: 검색 결과: KSSN 표준 상세 페이지(K001010135682)가 같은 제목으로 검색되고, 2026 년 기사들이 이 표준에 따른 엘리베이터 탑승 로봇 안전성 평가를 언급. 개정 여부는 원문 미열람으로 미확인.
- **f19**: 검색 결과 제목: '법령 > 제정·개정문 > 산업 디지털 전환 및 인공지능 활용 촉진법 | 국가법령정보센터'(lsiSeq=281883). 원문 미열람, 조문 내용 미확인.
- **f20**: 기사 검색 요약: 「산업 디지털 전환 및 인공지능 활용 촉진법」은 2026년 7월 1일부터 시행; 기존 산업 디지털 전환 촉진법을 개정해 AI 활용을 포함. 원문 미열람. (발행일 미확인, 확인일 기준)

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-022 | VDA(Verband der Automobilindustrie) | VDA 5050 Version 2.0.0 — Interface for the communication between automated guided vehicles (AGV) and a master control | 2022-01 | 표준 | medium | 2026-09-26 | https://www.vda.de/dam/jcr:f0c9c019-1506-4dee-998a-e92723fbf025/EN-VDA5050-V2_0_0.pdf | 예 |
| ref-032 | VDA(Verband der Automobilindustrie) | Version 3.0 of VDA 5050 released | 2026-04 | 표준 | medium | 2026-09-26 | https://www.vda.de/en/press/press-releases/2026/260421_PM_VDA_5050_EN | 예 |
| ref-052 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — README.md | 미확인 | 표준 | high | 2026-09-26 | https://github.com/VDA5050/VDA5050/blob/main/README.md | 아니오 |
| ref-139 | ISO | ISO 22400-2:2014 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions | 2014 | 표준 | medium | 2026-09-26 | https://www.iso.org/standard/54497.html | 예 |
| ref-811 | ISO | ISO/DIS 22400-2 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions | 미확인 | 표준 | medium | 2026-09-26 | https://www.iso.org/standard/87563.html | 예 |
| ref-812 | ISO | ISO 22400-2:2014/Amd 1:2017 - Automation systems and integration — Key performance indicators (KPIs) for manufacturing operations management — Part 2: Definitions and descriptions — Amendment 1: Key performance indicators for energy management | 2017-04 | 표준 | medium | 2026-09-26 | https://www.iso.org/standard/68295.html | 예 |
| ref-471 | A3(Association for Advancing Automation) | Updated ISO 10218 \| Answers to Frequently Asked Questions (FAQs) | 미확인 | 업계 보고서 | medium | 2026-09-26 | https://www.automate.org/robotics/blogs/updated-iso-10218-faq | 예 |
| ref-560 | ISO | ISO 10218-2:2025 - Robotics — Safety requirements — Part 2: Industrial robot applications and robot cells | 2025-02 | 표준 | medium | 2026-09-26 | https://www.iso.org/standard/73934.html | 예 |
| ref-813 | ISO | ISO/AWI 15066-1 - Collaborative Safety | 미확인 | 표준 | medium | 2026-09-26 | https://www.iso.org/standard/91522.html | 예 |
| ref-814 | ISO | ISO/TS 15066:2016 - Robots and robotic devices — Collaborative robots | 2016 | 표준 | medium | 2026-09-26 | https://www.iso.org/standard/62996.html | 예 |
| ref-825 | 국가표준인증통합정보시스템(KSSN) | KS B ISO 10218-2(2017 확인) 로봇 및 로봇 장치 - 산업용 로봇의 안전에 관한 요구사항 - 제2부: 로봇 시스템 및 통합 | 미확인 | 표준 | medium | 2026-09-26 | https://www.kssn.net/search/stddetail.do?itemNo=K001010116494 | 예 |
| ref-568 | 한국표준정보망(KSSN, 국가기술표준원) | KS B ISO/TS 15066 로봇 및 로봇 장치 - 협동로봇 (2022-10-12 확인판 있음) | 2017-02-28 | 표준 | medium | 2026-09-26 | https://www.kssn.net/search/stddetail.do?itemNo=K001010113282 | 예 |
| ref-211 | 국가표준인증통합정보시스템(KSSN) | KS B ISO 10218-2 로봇 및 로봇 장치 - 산업용 로봇의 안전에 관한 요구사항 - 제2부: 로봇 시스템 및 통합 | 미확인 | 표준 | medium | 2026-09-26 | https://www.kssn.net/search/stddetail.do?itemNo=K001010083660 | 예 |
| ref-470 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 2023-06 | 표준 | medium | 2026-09-26 | https://www.iso.org/standard/83545.html | 예 |
| ref-819 | ISO | ISO/CD 3691-4 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 미확인 | 표준 | medium | 2026-09-26 | https://www.iso.org/standard/88615.html | 예 |
| ref-566 | CEN (iTeh Standards 카탈로그) | EN ISO 12100:2010 - Safety of machinery - General principles for design - Risk assessment and risk reduction | 2010 | 표준 | medium | 2026-09-26 | https://standards.iteh.ai/catalog/standards/cen/74a41162-9d84-4410-a8a3-606630770ab9/en-iso-12100-2010 | 예 |
| ref-820 | DIN Media | DIN EN ISO 12100 - 2025-01 (Draft standard) | 2025-01 | 표준 | medium | 2026-09-26 | https://www.dinmedia.de/en/draft-standard/din-en-iso-12100/386233502 | 예 |
| ref-821 | Intertek | Machines Got Smarter, Now ISO 12100 has to Catch Up | 2025-12-11 | 업계 보고서 | low | 2026-09-26 | https://www.intertek.com/blog/2025/12-11-machines-and-iso-12100/ | 예 |
| ref-555 | European Union (EUR-Lex) | Regulation (EU) 2023/1230 of the European Parliament and of the Council on machinery | 2023-06 | 정부·연구기관 | medium | 2026-09-26 | https://eur-lex.europa.eu/eli/reg/2023/1230/oj/eng | 예 |
| ref-486 | ISO | ISO 22301:2019 - Security and resilience — Business continuity management systems — Requirements | 2019 | 표준 | medium | 2026-09-26 | https://www.iso.org/standard/75106.html | 예 |
| ref-822 | ISO | ISO 22301:2019/Amd 1:2024 - Security and resilience — Business continuity management systems — Requirements — Amendment 1: Climate action changes | 2024-02 | 표준 | medium | 2026-09-26 | https://www.iso.org/standard/88412.html | 예 |
| ref-502 | OMG(Object Management Group) | Business Process Model and Notation (BPMN), Version 2.0.2 | 2014-01 | 표준 | medium | 2026-09-26 | https://www.omg.org/spec/BPMN/2.0.2/ | 예 |
| ref-119 | IEC / ISO | IEC 62264-3:2016 - Enterprise-control system integration — Part 3: Activity models of manufacturing operations management | 2016 | 표준 | medium | 2026-09-26 | https://www.iso.org/standard/67480.html | 예 |
| ref-767 | IEC | IEC 62443-3-3:2013 Industrial communication networks — Network and system security — Part 3-3: System security requirements and security levels | 2013-08 | 표준 | medium | 2026-09-26 | https://standards.iteh.ai/catalog/standards/iec/c32e05fe-78a2-467e-a24d-0fc422289f55/iec-62443-3-3-2013 | 예 |
| ref-030 | W3C / OGC | Semantic Sensor Network Ontology | 2017-10-19 | 표준 | medium | 2026-09-26 | https://www.w3.org/TR/vocab-ssn/ | 예 |
| ref-817 | W3C | First Public Working Draft: Semantic Sensor Network Ontology - 2023 Edition | 2025 | 표준 | medium | 2026-09-26 | https://www.w3.org/news/2025/first-public-working-draft-semantic-sensor-network-ontology-2023-edition/ | 예 |
| ref-818 | W3C Spatial Data on the Web WG (w3c/sdw-sosa-ssn GitHub) | sdw-sosa-ssn — README (Repository of the Spatial Data on the Web Working Group for the SOSA/SSN vocabulary) | 미확인 | 표준 | high | 2026-09-26 | https://github.com/w3c/sdw-sosa-ssn | 아니오 |
| ref-510 | IEC / IEEE / ISO | IEC/IEEE 82079-1:2019 - Preparation of information for use (instructions for use) of products — Part 1: Principles and general requirements | 2019 | 표준 | medium | 2026-09-26 | https://www.iso.org/standard/71620.html | 예 |
| ref-823 | IEC / IEEE / ISO | IEC/IEEE CD 82079-1 - Preparation of information for use (instructions for use) of products — Part 1: Principles and general requirements | 미확인 | 표준 | medium | 2026-09-26 | https://www.iso.org/standard/87206.html | 예 |
| ref-509 | ISO | ISO 20607:2019 - Safety of machinery — Instruction handbook — General drafting principles | 2019 | 표준 | medium | 2026-09-26 | https://www.iso.org/standard/68519.html | 예 |
| ref-824 | IBF Solutions | New EN ISO 20607 – Instruction handbook for machinery | 미확인 | 업계 보고서 | low | 2026-09-26 | https://www.ibf-solutions.com/en/seminars-and-news/news/new-en-iso-20607-instruction-handbook-for-machinery | 예 |
| ref-345 | 국토교통부(법제처 국가법령정보센터) | 실내공간정보 구축 작업규정 | 2018-03-05 | 정부·연구기관 | medium | 2026-09-26 | https://law.go.kr/admRulLsInfoP.do?admRulSeq=2100000116559 | 예 |
| ref-679 | 국토교통부(법제처 국가법령정보센터) | 실내공간정보구축작업규정 (고시 제2021-1445호, 2021-12-24) | 2021-12-24 | 정부·연구기관 | medium | 2026-09-26 | https://www.law.go.kr/%ED%96%89%EC%A0%95%EA%B7%9C%EC%B9%99/%EC%8B%A4%EB%82%B4%EA%B3%B5%EA%B0%84%EC%A0%95%EB%B3%B4%EA%B5%AC%EC%B6%95%EC%9E%91%EC%97%85%EA%B7%9C%EC%A0%95/(2021-1445,20211224) | 예 |
| ref-314 | 국가표준인증통합정보시스템(KSSN) | KS B 7317 이동 로봇의 엘리베이터 탑승을 위한 안전 요구사항 및 평가 방법 | 2021-11 | 표준 | medium | 2026-09-26 | https://www.kssn.net/search/stddetail.do?itemNo=K001010135682 | 예 |
| ref-637 | 국가법령정보센터(산업통상자원부) | 산업 디지털 전환 촉진법 (법률 제18692호) | 2022-01-04 | 정부·연구기관 | medium | 2026-09-26 | https://www.law.go.kr/법령/산업디지털전환촉진법/(18692,20220104) | 예 |
| ref-815 | 국가법령정보센터 | 법령 > 제정·개정문 > 산업 디지털 전환 및 인공지능 활용 촉진법 | 미확인 | 정부·연구기관 | medium | 2026-09-26 | https://law.go.kr/lsInfoP.do?lsiSeq=281883&viewCls=lsRvsDocInfoR | 예 |
| ref-816 | 폴리뉴스 | [입법이 산업을 바꾼다] 공장이 AI를 쓰기 시작했다…'산업 AI법' 시행이 제조업을 바꾼다 | 미확인 | 기사 | low | 2026-09-26 | https://www.polinews.co.kr/news/articleView.html?idxno=743929 | 예 |

### 출처 요약

- **ref-022**: 원문 미열람. 재검증 대상: VDA 5050 2.0.0 판.
- **ref-032**: 원문 미열람. VDA 5050 3.0 발행 보도자료.
- **ref-052**: 공식 저장소 README. main 브랜치가 최신 게시판(현재 3.0.0)이라고 밝히고 향후 판 계획을 적는다.
- **ref-139**: 원문 미열람. 재검증 대상: 제조 운영 관리 KPI 정의 표준 2014 판.
- **ref-811**: 원문 미열람. ISO 22400-2 개정판 프로젝트 페이지. 검색 요약상 2024-09-17 FDIS 등록 승인, 2014 판 대체 예정.
- **ref-812**: 원문 미열람. ISO 22400-2:2014 의 에너지 관리 KPI 개정 1.
- **ref-471**: 원문 미열람. ISO 10218:2025 개정 FAQ, ISO/TS 15066 요구사항의 10218-2 통합 설명.
- **ref-560**: 원문 미열람. 산업용 로봇 적용·셀 안전 요구 2025 판.
- **ref-813**: 원문 미열람. ISO/TS 15066:2016 을 대체할 협동 안전 표준의 예비 작업 항목(AWI).
- **ref-814**: 원문 미열람. 협동로봇 기술 사양. 검색 요약상 2022 확인, 폐지되지 않음.
- **ref-825**: 원문 미열람. KS B ISO 10218-2 의 2017 확인 판 상세 페이지.
- **ref-568**: 원문 미열람. ISO/TS 15066 부합 KS.
- **ref-211**: 원문 미열람. ISO 10218-2 부합 KS.
- **ref-470**: 원문 미열람. 무인 산업용 트럭 안전 요구 2023 판.
- **ref-819**: 원문 미열람. ISO 3691-4 차기판 위원회 초안 프로젝트 페이지.
- **ref-566**: 원문 미열람. 재검증 대상: 위험성평가 기본 표준 2010 판.
- **ref-820**: 원문 미열람. ISO/DIS 12100:2024 기반 EN ISO 12100 개정 초안의 독일 게시본.
- **ref-821**: 원문 미열람. ISO 12100 개정 진행과 EU 기계 규정 정렬을 설명하는 시험인증기관 블로그.
- **ref-555**: 원문 미열람. EU 기계 규정.
- **ref-486**: 원문 미열람. 업무 연속성 관리 시스템 요구사항.
- **ref-822**: 원문 미열람. ISO 22301 기후 행동 개정 1, 4.1·4.2 조항 수정.
- **ref-502**: 원문 미열람. BPMN 2.0.2 명세.
- **ref-119**: 원문 미열람. 제조 운영 관리 활동 모델 제2판.
- **ref-767**: 원문 미열람. 시스템 보안 요구사항과 보안 수준 제1판.
- **ref-030**: 원문 미열람. SSN/SOSA 2017 권고안.
- **ref-817**: 원문 미열람. SSN 2023 Edition 첫 공개 작업 초안 발행 공지.
- **ref-818**: 작업반 저장소 README. SSN 2023 Edition 을 편집자 초안·공개 작업 초안 상태로 안내하며 2017 판과의 변경 목록은 싣지 않는다.
- **ref-510**: 원문 미열람. 제품 사용 정보 작성 원칙 2019 판.
- **ref-823**: 원문 미열람. IEC/IEEE 82079-1 차기판 위원회 초안 프로젝트 페이지.
- **ref-509**: 원문 미열람. 기계 설명서 작성 원칙 2019 판.
- **ref-824**: 원문 미열람. ISO/DIS 20607 개정 진행(투표 종료 2025-05-03, EN 채택 기한 2026-01-20)을 전하는 기계 안전 컨설팅사 뉴스.
- **ref-345**: 원문 미열람. 실내공간정보 구축 작업규정 2018 판.
- **ref-679**: 원문 미열람. 실내공간정보 구축 작업규정 2021 고시 판.
- **ref-314**: 원문 미열람. 이동 로봇 엘리베이터 탑승 안전 KS.
- **ref-637**: 원문 미열람. 산업 디지털 전환 촉진법 제정판.
- **ref-815**: 원문 미열람. 제명이 바뀐 산업 디지털 전환 및 인공지능 활용 촉진법의 제정·개정문 페이지(검색 결과 제목·URL 로 존재 확인).
- **ref-816**: 원문 미열람. 산업 디지털 전환 및 인공지능 활용 촉진법이 2026-07-01 시행됐다고 전하는 기사.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/a-business-supply-chain-design/04-performance-economics-and-process-improvement.md | 4, 7 | needs_update 제안 (f2·f3): ISO 22400-2:2014 인용에 개정 1:2017(에너지 관리 KPI, ref-812)과 진행 중인 개정판 ISO/DIS 22400-2(2024-09-17 FDIS 등록 승인, ref-811)를 병기하고 기준일을 갱신한다. 4·7절은 주제 페이지로 분리돼 있으므로 해당 주제 페이지(2026-09-25-area04-s4, 2026-09-25-area04-s7)와 표준 목록의 ISO 22400-2 항목도 함께 고친다. 다음 실행 후보: 2. 공정·워크플로 모델링의 BPMN 2.0.2(f11)·IEC 62264-3:2016(f12)은 유효로 판정해 수정 불필요. |
| update | docs/categories/g-safety-security-intelligence-and-governance/25-safety-and-risk-management.md | 7 | needs_update 제안 (f4·f5·f6·f7·f8·f9): ISO/TS 15066 요구사항의 ISO 10218-2:2025 통합과 ISO/AWI 15066-1 개발, KS B ISO/TS 15066·KS B ISO 10218-2 의 구판 기준 가능성, ISO 3691-4 차기판(CD)·ISO 12100 개정 초안 진행을 반영. 다음 실행 후보: ref-022 needs_update(3.0.0 으로 대체됨, f1), ref-345 deprecated 제안(대체 출처: ref-679, f17), ref-637 needs_update(제명 변경 f19·f20, 28. 표준·상호운용성·다사업자 거버넌스 표기 재확인), ref-030 SSN 에 2023 Edition 초안 병기(f14, 5. 로봇 능력·작업 온톨로지와 트랙 manual-capability-ontology 비교표), ref-486 에 개정 1:2024 병기(f10, 20. 예외 복구·재계획·업무 연속성), ref-509·ref-510 개정 진행 병기(f15·f16, 트랙 매뉴얼 문서 유형), ref-767 IEC 62443-3-3·ref-314 KS B 7317 유효(f13·f18). |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- ISO 10218-2:2025 발행 뒤 국내 KS B ISO 10218-2 와 KS B ISO/TS 15066 은 새 판으로 부합 개정되었거나 개정 예고되었는가, 국내 협동로봇 설치 작업장 안전인증은 어느 판을 기준으로 하는가? | 관련 영역: 25. 안전·위험 관리, 18. 사람–로봇 협업·운영 인터페이스 | 근거: f6 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 38 · 교차 확인: 0
- 예산 사용량: 검색 20회 · 신규 출처 15건
- 미확인 항목:
    - f3 ISO 22400-2 개정판의 발행 여부 미확인(FDIS 등록 승인까지만)
    - f6 KS B ISO 10218-2·KS B ISO/TS 15066 의 2025 판 부합 여부 미확인(검색 범위 내 미발견)
    - f9 ISO 12100 FDIS 시점은 업계 블로그 요약뿐
    - f13 IEC 62443-3-3 개정판 진행 상태 미확인
    - f16 ISO 20607 새 판 발행 여부 미확인
    - f18 KS B 7317 개정 여부 미확인
    - f20 산업 디지털 전환 및 인공지능 활용 촉진법 시행일은 기사 1건뿐, 데이터 공동 생성 조문 번호·내용 미확인(oq-122 부분 답)
    - MassRobotics AMR 상호운용 표준(ref-033) 판 정보는 공식 저장소 README 에 없어 재검증하지 못함
- 범위 경계 위반 의심:
    - 없음
- 한계: 월간 재검증: target.json 이 재검증 대상을 지정하지 않아 참고문헌 목록에서 발행 2년이 지난 표준·규정 중 세부영역 페이지 인용과 연관된 것을 골랐다(전수 재검증 아님). web_fetch_available: false · fetch_mode mirror_only 로 github_raw 원문은 2건(ref-052 VDA 5050 README, ref-818 SOSA/SSN 작업반 README)만 열었고 나머지는 검색 결과 요약 범위만 사용해 신뢰도 상한 medium. 교차 확인 0건(같은 발행 기관 계열 출처뿐이거나 단일 출처). 판정 요약: 대체됨 — ref-022(3.0.0), ref-345(2021 고시 ref-679); 개정·후속 진행 — ref-139(Amd1·DIS), ref-568(10218-2:2025 통합·AWI 15066-1), ref-470(CD), ref-566(DIS), ref-486(Amd1:2024), ref-030(2023 Edition WD), ref-509·ref-510(DIS·CD), ref-637(제명 변경); 유효 — ref-502, ref-119, ref-767, ref-314(모두 추정 수준). oq-122 는 제명 변경·시행은 확인했으나 조문 변화가 미확인이라 해결로 올리지 않았다. 페이지 제안은 갱신 상한 2건에 맞추고 나머지는 rationale 에 다음 실행 후보로 남겼다. 입력의 대상 세부영역 페이지는 1~4번만 주어져 25. 안전·위험 관리 등 나머지 페이지의 인용 문장은 직접 대조하지 못했다. 신규 출처 15건(ref-811~ref-825) 상한 도달.
