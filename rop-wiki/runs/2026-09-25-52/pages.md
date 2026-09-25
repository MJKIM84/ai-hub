# 스토리텔러 산출 2026-09-25-52

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md | draft | 영역 심화: 3~11절 신규 작성(4·6·7·8절은 주제 페이지로 분리), 2차 수정: 10절 연결 문장 5건 태그·표현 정정, 7절 요약 강등, 9절 표 범위 정정, sources 정리 |
| create | docs/topics/2026/2026-09-25-area21-s6.md | draft | 자동 분리: 21. 온보딩·설정·현장 시운전 의 "6. 대표 접근법과 기술" 절을 옮겼다. 2차 수정: 문서 해석 AI 문장을 자연어 능력 설명 기준 [추정]으로 정정 |
| create | docs/topics/2026/2026-09-25-area21-s7.md | draft | 자동 분리: 21. 온보딩·설정·현장 시운전 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다. 2차 수정: 요약 문장 [추정]으로 강등 |
| create | docs/topics/2026/2026-09-25-area21-s4.md | draft | 자동 분리: 21. 온보딩·설정·현장 시운전 의 "4. 핵심 개념과 용어" 절을 옮겼다 |
| create | docs/topics/2026/2026-09-25-area21-s8.md | draft | 자동 분리: 21. 온보딩·설정·현장 시운전 의 "8. 대표 연구와 자료" 절을 옮겼다. 2차 수정: Beinschob 외 항목의 평가 문장 삭제 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 21. 온보딩·설정·현장 시운전 | 영역 심화: 3~11절 신규 작성(표준 등록 메시지·어댑터 설정·평면도 주석·반자동 지도 작성·가상 시운전, 적치 시나리오) | run 2026-09-25-52
- 홈 최근 업데이트: 2026-09-25 — 21. 온보딩·설정·현장 시운전: 영역 심화 초안 작성(등록 표준 메시지, 지도 정합, 반자동 지도 작성, 가상 시운전)
- 대분류 최근 업데이트: 2026-09-25 — 21. 온보딩·설정·현장 시운전: 3~11절 초안 작성, 적치 단계 새 제조사 AMR 시운전 시나리오
- 세부영역 최근 업데이트: 2026-09-25 — 21. 온보딩·설정·현장 시운전: 3~11절 신규 작성, 트랙 반영 제안 가운데 재확인된 5건 반영

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 가상 시운전 | Virtual Commissioning | 제어 로직·로봇 프로그램·관제 설정을 현장 설치 전에 가상 모델과 연결해 시험함으로써 현장 시운전의 시간과 위험을 줄이려는 방법이다. | 21, 22 | ref-640 |
| new | 플러그 앤 프로듀스 | Plug and Produce | 새 설비나 자원을 연결하면 기술된 능력 정보를 바탕으로 최소한의 설정만으로 생산·작업에 투입되게 하려는 통합 방식이다. | 21, 5 | ref-037 |
| new | 신원 보고 | Identity Report (MassRobotics identityReport) | MassRobotics AMR 상호운용 표준에서 로봇이 제조사·모델·일련번호·외곽 치수와 선택적으로 속도·화물 한계·문서 위치를 알리는 메시지다. | 21, 9 | ref-230 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-004 | Open Robotics | RMF Core Overview — Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/rmf-core.html |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-251 | Open Robotics | Programming Multiple Robots with ROS 2 — integration_fleets (Fleet Adapter integration) | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/integration_fleets.html |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 표준 | medium | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema |
| ref-079 | Open Robotics | Programming Multiple Robots with ROS 2 — traffic-editor | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/traffic-editor.html |
| ref-153 | Open Robotics | Programming Multiple Robots with ROS 2 — integration_fleets_adapter_tutorial | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html |
| ref-229 | IDTA (admin-shell-io/submodel-templates) | IDTA 02020 Submodel Capability Description 1.0 — README | 표준 | medium | https://github.com/admin-shell-io/submodel-templates/tree/main/published/Capability%20Description |
| ref-046 | VDMA (Intralogistics-2X-LIF GitHub) | Layout-Interchange-Format — Repository for the Layout Interchange Format (LIF) developed by the VDMA | 표준 | medium | https://github.com/Intralogistics-2X-LIF/Layout-Interchange-Format |
| ref-217 | Beinschob, P. 외 | Semi-automated map creation for fast deployment of AGV fleets in modern logistics | 논문 | medium | https://www.sciencedirect.com/science/article/abs/pii/S0921889015302724 |
| ref-269 | Heselden, J. R., & Das, G. P. | Unified Map Handling for Robotic Systems: Enhancing Interoperability and Efficiency Across Diverse Environments | 논문 | medium | https://arxiv.org/abs/2404.13499 |
| ref-037 | Vieira da Silva, L. M., Köcher, A., Gill, M. S., Weiss, M., & Fay, A. | Toward a Mapping of Capability and Skill Models using Asset Administration Shells and Ontologies | 논문 | medium | https://arxiv.org/abs/2307.00827 |
| ref-637 | Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A. | Toward a Method to Generate Capability Ontologies from Natural Language Descriptions | 논문 | medium | https://arxiv.org/abs/2406.07962 |
| ref-470 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 표준 | medium | https://www.iso.org/standard/83545.html |
| ref-639 | 부산일보 | KTL·통합물류협회 ‘물류로봇 시험인증’ 협력 강화 ‘맞손’ | 기사 | low | https://www.busan.com/view/busan/view.php?code=2026072420194685883 |
| ref-640 | Siemens Digital Industries Software | Virtual commissioning with Siemens solutions reduces launch time by three weeks | 벤더 문서 | low | https://resources.sw.siemens.com/en-US/case-study-idc/ |
| ref-265 | European Commission CORDIS | PAN-ROBOTS: Automating logistics for the factory of the future | 정부·연구기관 | medium | https://cordis.europa.eu/article/id/160857-panrobots-automating-logistics-for-the-factory-of-the-future |
| ref-163 | 노주형, 강규리, 김연찬, 심현철 (한국로봇학회) | 탐사 및 엘리베이터 연계를 이용한 완전 자율 다층 실내 지도 구축 시스템 | 논문 | medium | https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART003305667 |
| ref-643 | Open Robotics (open-rmf/rmf_site) | rmf_site — README (RMF Site Editor) | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_site |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 국내 물류센터가 새 제조사 AMR 을 관제에 등록할 때 VDA 5050 팩트시트나 MassRobotics 신원 보고 같은 표준 등록 정보를 실제로 받은 사례가 있는가, 있다면 등록·설정 공수는 얼마나 줄었는가? | 21, 9 | 열림 | — |
| new | — | 제조사 로봇 지도와 공통 관제 지도 사이 지도 정합(대응점 설정)의 오차를 현장 시운전에서 어떤 기준과 시험으로 합격 판정하는가? | 21, 6, 23 | 열림 | — |
| new | — | 출처 충돌: 레이아웃 교환 형식(LIF)의 현행 판과 발행일(2023-09 1.0.0 대 VDMA 2024-03)은 무엇인가? | 21, 6 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 적치 | 시작 조건 | docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 21. 온보딩·설정·현장 시운전 |
| 적치 | 작업 대상 | docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 21. 온보딩·설정·현장 시운전 |
| 적치 | 수행 자원 | docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 21. 온보딩·설정·현장 시운전 |
| 적치 | 제약 | docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 21. 온보딩·설정·현장 시운전 |
| 적치 | 완료·인계 | docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 21. 온보딩·설정·현장 시운전 |
| 적치 | 예외·성과 | docs/categories/f-deployment-verification-and-maintenance/21-onboarding-configuration-and-commissioning.md#5-현장-시나리오-물류-흐름의-어느-단계인지-명시 | 21. 온보딩·설정·현장 시운전 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| RMF Site Editor (rmf_site) | 오픈소스 | Open Robotics (open-rmf) | 21, 6 | ref-643 | https://github.com/open-rmf/rmf_site |

## 추가 조사 요청

- 트랙 반영 제안 가운데 이번 실행에서 다시 확인하지 않은 항목(MiR 평면도 업로드·축척 요건 벤더 주장 ref-271 등, 충전기 마커 등록 절차 ref-219, OTTO 설정 복제·부분 재지도화, Boniardi 외 2019, Beinschob·Reinke 2015 ref-266, 다중 AGV 경로망 자동 설계 IEEE T-ASE 2024 ref-267, Rüdt 외 2025 ref-268, 국내 건설로봇 문헌고찰)을 다음 21. 온보딩·설정·현장 시운전 실행에서 검증해 6·8절에 반영할지 판단해야 한다.
- 중복 id 병합 확인: ref-217(Beinschob 외 2017), ref-265(PAN-Robots CORDIS), ref-269(Heselden·Das 2024), ref-079(traffic-editor), ref-046(LIF), ref-470(ISO 3691-4), ref-229(IDTA 02020)가 기존 참고문헌과 같은 URL 인지, ref-153 이 ref-105 와 같은 문서인지 퍼블리셔가 확인해 기존 id 로 합쳐야 한다.
- ref-004 참고문헌 항목: 이번 실행은 cited_by 추가만 의도한다. 퍼블리셔는 docs/references/ref-004.md 의 기존 org·title·url·accessed·summary 를 유지하고 cited_by 만 합쳐야 한다(입력에 기존 summary 가 없어 reference_updates 의 summary 는 중립 문구로 채웠다).
- 3절·5절의 설치 기간 단축 수치(PAN-Robots 6→2개월, Siemens 3주)를 독립 출처로 교차 확인할 자료가 필요하다(현재 과제·벤더 측 보고값뿐).
- 5절 완료·인계 칸과 10절 23. 시험·형식 검증·벤치마크 연결: 현장 시운전의 합격 기준(지도 정합 오차, 위치 정확도 시험 방법)에 관한 표준·지침 근거가 필요하다(ISO 3691-4 시운전 절차 원문 또는 공인 해설).
- 10절 10. 설비·건물 시스템 연동 연결: 다층 자율 지도 작성(노주형 외 2026)과 설비 연동의 관계를 영역 페이지에 쓰려면 승강기 연동 관점의 근거가 더 필요하다(이번에는 연결 문장에서 뺐다).
- 7절: KTL–KILA 협약(2026-07-23)의 기관 보도자료 원문과 이후 실증 실적 확인이 필요하다.
- 11절 oq-022: 국내 물류센터의 CAD·BIM 도면 활용 사례를 추가 한국어 검색으로 찾아야 한다.

## 이행한 수정 지시

- f2 필수 절 정정 — 6절 '표준 메시지로 로봇 등록 정보 받기'에서 필수 여섯 절(과 헤더 필드)·선택 mobileRobotConfiguration 으로 고쳐 쓰고 [추정][^ref-228]로 강등했으며 7절 표 행도 [추정]으로 표기했다.
- f22 표현 정정 — 5절 제약 칸을 '팩트시트의 필수·선택 최상위 절과 신원 보고 필드'로 고쳐 쓰고 [추정]을 유지했다.
- f10 분리 — 6절에서 Full Control·Traffic Light 문장에 [사실][^ref-251], Read Only 문장에 [사실][^ref-004]를 붙이고 '온보딩 때 연동 수준이 선택 사항'은 별도 [추정] 문장으로 분리했으며 ref-004 각주는 공통 참고문헌 형식 줄을 그대로 옮겼다.
- f14 구절 삭제 — '사물인터넷 장치 개조나 외부 시스템 연동 없이'를 빼고 8절 연구 사례로만 두었으며 로봇 자체 기능 연구(연계 대상)임을 밝혔다.
- f20 비교 기준 — 4·5·6절에서 [추정] 벤더 주장을 유지하고 6절에 '현장 시운전만 한 유사 업그레이드 프로젝트(8주) 대비 3주 단축, 고속 분류기, Tecnomatix Plant Simulation'으로 적었으며 '코드를 설계와 대조 검증해 큰 변경 불필요' 구절은 뺐다.
- f4·f5 LIF 기준일 — 7절 표 아래에 'VDMA 2024-03 인용[^ref-031]'과 '1.0.0, 2023-09[^ref-046]'을 둘 다 제시하고, 11절과 open_question_updates 에 출처 충돌 질문을 올렸다.
- f12 — 3·5절에서 [추정]과 '과제 측 보고값, 비교 조건 미확인'을 유지하고, 6절에서 원인 설명은 'PAN-Robots 과제 측은 … 서술한다'로 과제 측 서술로만 적었다.
- 4절 용어 — '좌표 대응·좌표 정합'을 용어집 '지도 정합 (Map Alignment)'으로 통일하고 대응점 설정을 그 방법으로 설명했으며, 팩트시트·LIF·경로망·플릿 어댑터는 기존 용어집 링크만 걸고 glossary_updates 는 가상 시운전·플러그 앤 프로듀스·신원 보고 3건만 냈다.
- 각주 — ref-251·ref-229·ref-217~ref-163 각주 정의에 ' (원문 미열람)'을 붙이고 reference_updates 의 source_unopened 를 true 로 두었으며, ref-004 는 공통 참고문헌 각주 형식 줄을 그대로 복사했다.
- 10절 연결 — f17 을 5. 로봇 능력·작업 온톨로지와 27. AI·학습·적응과 모델 운영 양쪽에 연결했고, 22. 시뮬레이션·예측용 디지털 트윈 연결은 가상 시운전·팩트시트의 시뮬레이션 용도로 한정했으며 8. 실시간 세계 상태·데이터 일관성은 연결하지 않았다.
- 트랙 반영 제안 — traffic-editor(f8), 플릿 어댑터 설정(f7), Beinschob 외(f11), Heselden·Das(f13), PAN-Robots(f12)만 반영하고 MiR·OTTO 벤더 주장, Boniardi 외 2019, ref-266~ref-268, 국내 건설로봇 문헌고찰은 본문에서 빼고 additional_research_requests 에 다음 실행 후보로 적었다.
- f1 인용 위치 — 6절에서 'VDA 5050 3.0.0 표 2(4.3절)'로 적고 ref-031 직접 인용은 그 한 곳에서만 했다.
- 분량 초과 자동 분리: 21. 온보딩·설정·현장 시운전 본문 7,666자 > 기준 4,000자 → 4개 절을 주제 페이지로 옮김, 남은 본문 3,676자
- 2차: 10절 5. 로봇 능력·작업 온톨로지 연결 — 지시 문장 그대로 '요구·제공 능력 비교(IDTA 02020)와 자연어 능력 설명에서 능력 온톨로지를 생성하는 방법이 로봇 등록 작업을 줄이는 데 쓰일 수 있다. [추정][^ref-229][^ref-637]'로 고쳤다.
- 2차: 10절 27. AI·학습·적응과 모델 운영 연결 문장과 주제 페이지 s6 '능력 기술과 문서 해석 AI' 소절 마지막 문장 — 둘 다 지시 문장('자연어 능력 설명에서 LLM 으로 … 적용하는 연구 방법이다. [추정][^ref-637]')으로 바꾸어 '매뉴얼' 표현을 없앴다.
- 2차: 10절 9. 로봇·제조사 관제 연동 연결 — '연동 수준'을 빼고 '팩트시트·신원 보고·어댑터 설정이 관제 연동의 첫 단계가 되는 것으로 보인다. [추정][^ref-031][^ref-230][^ref-153]'로 강등했다.
- 2차: 10절 10. 설비·건물 시스템 연동 연결 — 다층 지도 작성 부분을 빼고 '평면도 위 승강기·문 주석이 설비 연동과 맞물리는 것으로 보인다. [추정][^ref-079]'로 강등했다(ref-163 은 추가하지 않았다).
- 2차: 10절 23. 시험·형식 검증·벤치마크 연결 — '시운전 합격 판정 기준은 아직 열린 질문(11절)이며, 국내 물류로봇 시험·실증 체계가 이 판정과 이어질 수 있다. [추정][^ref-639]'로 고쳤다.
- 2차: 7절 요약 문장 — 세부영역 페이지 7절과 주제 페이지 s7 의 1절·3절 첫 문장의 [사실]을 [추정]으로 강등했다.
- 2차: 주제 페이지 s8 Beinschob 외 항목 — '이 영역의 설치 공수 문제를 정리한 대표 문헌이다' 문장을 삭제했다.
- 2차: 9절 표 '시설·설비 제어' 행 — ROP 칸의 '운행 구역 설정'을 '레이아웃·지도 정합 설정'으로 바꾸고, 표 바로 아래에 '이 표는 관제 인터페이스 자료에서 끌어낸 이 위키의 추론을 정리한 것이다. [추정][^ref-031][^ref-153][^ref-251]' 한 줄을 두었다(스토리텔러 규칙 4.4 에 따라 finding id 'f23' 은 본문에 쓰지 않았다).
- 2차: 세부영역 페이지 프런트매터 sources 에서 본문 미인용·각주 미정의인 ref-004·ref-163·ref-643 을 뺐다(10절에 새로 인용하지 않았으므로 13절 각주 추가 없음). reference_updates 의 ref-163·ref-643 cited_by 도 실제 인용한 주제 페이지로 바로잡았다.
- 2차: open_question_updates 두 번째 항목의 '좌표 대응(대응점 설정)'을 페이지 11절과 같은 '지도 정합(대응점 설정)'으로 고쳤다.
- 2차: reference_updates 의 ref-004 — 페이지 전용 문구를 지우고 중립 요약으로 바꾸었으며 org·title·url·accessed 는 공통 참고문헌 각주 형식 값 그대로 두고 cited_by 만 주제 페이지 s6 로 넣었다. 기존 summary 가 입력에 없어 퍼블리셔가 기존 값을 유지하도록 additional_research_requests 에 요청했다.
