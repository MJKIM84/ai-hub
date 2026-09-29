# 스토리텔러 산출 2026-09-29-07

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/robot-ontology/heterogeneous-robot-registration.md | draft | 영역 심화: 섹션 3~11 신규 작성(finding 26건 반영, 1차 조건부 승인 수정 13건 이행), 프런트매터 related_areas·tags·confidence·sources·last_run 추가, version 2. 출처 id ref-228 는 직전 실행과 충돌하므로 퍼블리셔가 새 id 를 부여해야 한다 |
| create | docs/topics/2026/2026-09-29-area04-s4.md | draft | 자동 분리: 4. 이기종 로봇 등록 의 "4. 핵심 개념과 용어" 절(2,184자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area04-s6.md | draft | 자동 분리: 4. 이기종 로봇 등록 의 "6. 대표 접근법과 기술" 절(1,749자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area04-s8.md | draft | 자동 분리: 4. 이기종 로봇 등록 의 "8. 대표 연구와 자료" 절(1,238자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area04-s7.md | draft | 자동 분리: 4. 이기종 로봇 등록 의 "7. 관련 표준·프레임워크·오픈소스" 절(1,149자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area04-s11.md | draft | 자동 분리: 4. 이기종 로봇 등록 의 "11. 열린 질문" 절(1,109자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area04-s10.md | draft | 자동 분리: 4. 이기종 로봇 등록 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절(805자)을 옮겼다 |
| create | docs/topics/2026/2026-09-29-area04-s3.md | draft | 자동 분리: 4. 이기종 로봇 등록 의 "3. 왜 중요한가" 절(734자)을 옮겼다 |

## 변경 이력·색인

- 변경 이력: 2026-09-29 | 4. 이기종 로봇 등록 | 영역 심화: 섹션 3~11 신규 작성(병원 사례 2건·기타 1건, 표준 8종, 언어 모델 추출 연구 3건), 1차 조건부 승인 수정 13건 이행 | run 2026-09-29-07
- 홈 최근 업데이트: 2026-09-29 — 4. 이기종 로봇 등록: 영역 심화로 3~11절 신규 작성. VDA 5050 팩트시트·자산관리셸 서브모델·MassRobotics 신원 보고의 등록 항목, Open-RMF 어댑터 설정과 병원 현장 등록 사례, 문서·URDF 능력 추출과 사람 검토 연구를 정리했다
- 대분류 최근 업데이트: 2026-09-29 — 4. 이기종 로봇 등록: 영역 심화, 3~11절 신규 작성(신뢰도 medium, 새 출처 15건, 새 열린 질문 4건, oq-128 은 미해결)
- 세부영역 최근 업데이트: 2026-09-29 — 실행 2026-09-29-07: 3~11절 신규 작성. 1차 조건부 승인 수정 13건 이행(디지털 명판·세 형식 공통 항목 강등, OPC UA 식별 속성 축소, 벤더 주장 병기)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 디지털 명판 | Digital Nameplate (IDTA 02006) | 제조사명·제품명·일련번호·제조일과 하드웨어·펌웨어·소프트웨어 버전 같은 식별·버전 항목을 담는 자산관리셸 서브모델로, 산업 장비의 명판 정보를 기계가독 형식으로 교환하게 한다. | 4, 21, 57 | ref-876 |
| new | AGV 기술 데이터 서브모델 | Technical Data for AGV in Intralogistics (IDTA 02047) | 실내 물류용 AGV·AMR 의 유형·기술 매개변수·VDA 5050 팩트시트·에너지·통신·배터리·안전·임시 기술 데이터를 컬렉션으로 나눠 담는 자산관리셸 서브모델 템플릿이다. | 4, 5, 21 | ref-198 |
| new | 통합 로봇 기술 형식 | Unified Robot Description Format (URDF) | 로봇의 링크와 관절로 구조·운동학·물리 속성을 기술하는 ROS 계열의 XML 형식으로, 식별자 자체에는 의미가 없어 온톨로지로 옮기려면 해석이 필요하다. | 4, 5, 45 | ref-239 |
| new | 자산관리셸 레지스트리·디스커버리 | AAS Registry / Discovery | 자산관리셸 API 명세(IDTA-01002)가 정한 서비스로, 등록된 자산관리셸과 서브모델의 서술자를 관리하고 자산 식별자로 해당 자산관리셸을 찾게 한다. | 4, 6, 21 | ref-880 |
| new | 온톨로지 채우기 | Ontology Population | 이미 정해진 온톨로지의 개념·관계에 맞춰 문서·모델 파일 같은 원천에서 개체와 관계 인스턴스를 뽑아 채우는 작업으로, 언어 모델을 쓸 때는 검증과 사람 검토를 함께 둔다. | 4, 45, 47 | ref-239 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-228 | VDA (Verband der Automobilindustrie) · VDMA, VDA5050 GitHub 공식 저장소 | VDA5050/json_schemas/factsheet.schema (main) | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema |
| ref-198 | Industrial Digital Twin Association (IDTA) | IDTA 02047-1-0 Submodel Template: Technical Data for AGV in Intralogistics | 표준 | high | https://industrialdigitaltwin.org/wp-content/uploads/2025/03/IDTA-02047-1-0-Submodel_Technical-Data-for-AGV.pdf |
| ref-230 | MassRobotics (AMR Interoperability Working Group) | AMR_Interop_Standard.json — MassRobotics AMR Interoperability Standard JSON schema | 표준 | high | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json |
| ref-239 | Dussard, B., & Sarthou, G. (LAAS-CNRS) | Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF | 논문 | medium | https://arxiv.org/abs/2606.17073 |
| ref-153 | Open Robotics (Programming Multiple Robots with ROS 2) | Fleet Adapter Tutorial (integration_fleets_adapter_tutorial) - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html |
| ref-874 | Valner, R., Masnavi, H., Rybalskii, I., Põlluäär, R., Kõiv, E., Aabloo, A., Kruusamäe, K., & Singh, A. K. (University of Tartu), Frontiers in Robotics and AI | Scalable and heterogenous mobile robot fleet-based task automation in crowded hospital environments—a field test | 논문 | high | https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2022.922835/full |
| ref-875 | 로봇신문 | [기업 최전선을 가다-클로봇] 로봇 소프트웨어로 쓰는 ‘피지컬 AI’ 시대의 서막 | 기사 | low | https://www.irobotnews.com/news/articleView.html?idxno=43274 |
| ref-876 | Industrial Digital Twin Association (IDTA) | IDTA 02006-3-0 Submodel Template: Digital Nameplate for Industrial Equipment | 표준 | high | https://industrialdigitaltwin.org/wp-content/uploads/2025/10/IDTA-02006-3-0-1_Submodel_Digital-Nameplate.pdf |
| ref-043 | 신민종, 한영석, 정재윤 (한국디지털산업학회지 29(4)) | 자산관리쉘 표준을 이용한 자율이동로봇 모니터링 시스템 설계 | 논문 | medium | https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART003140560 |
| ref-878 | Changi General Hospital, Centre for Healthcare Assistive & Robotics Technology (CHART) | RoMi-H Empanelment Programme 2025 | 정부·연구기관 | medium | https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste |
| ref-031 | VDA (Verband der Automobilindustrie) · VDMA, VDA5050 GitHub 공식 저장소 | VDA5050_EN.md — VDA 5050 Interface for the communication between automated guided vehicles (AGV) and a master control (Version 3.0.0, main) | 표준 | high | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-880 | Industrial Digital Twin Association (IDTA), admin-shell-io GitHub 공식 저장소 | aas-specs-api — Repository of the Asset Administration Shell Specification IDTA-01002 API (README) | 표준 | high | https://github.com/admin-shell-io/aas-specs-api |
| ref-881 | OPC Foundation | OPC 40010-1: OPC UA for Robotics — Part 1: Vertical Integration (Version 1.02) | 표준 | high | https://reference.opcfoundation.org/Robotics/v100/docs/ |
| ref-465 | Vieira da Silva, L. M., Köcher, A., Gehlhoff, F., & Fay, A. | Toward a Method to Generate Capability Ontologies from Natural Language Descriptions | 논문 | medium | https://arxiv.org/abs/2406.07962 |
| ref-883 | Abolhasani, M. S., & Pan, R. | Leveraging LLM for Automated Ontology Extraction and Knowledge Graph Generation | 논문 | medium | https://arxiv.org/abs/2412.00608 |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| update | oq-128 | 국내 현장에서 VDA 5050 팩트시트나 자산관리셸 능력 기술을 로봇 등록 데이터로 실제 쓰는 사례가 있으며, 채팅 로봇 구성이 그 데이터를 읽어 되묻기를 줄일 수 있는가? | 10, 4, 21 | 열림 | docs/categories/robot-ontology/heterogeneous-robot-registration.md#11-열린-질문 |
| new | — | 문서·URDF 에서 추출한 능력 항목마다 매뉴얼의 절·줄 위치를 근거로 붙여 검토자가 원문과 대조해 확정·반려하는 공개 구현이나 연구가 있는가? | 4, 45, 7 | 열림 | — |
| new | — | VDA 5050 팩트시트·IDTA 02047 서브모델·MassRobotics identityReport 사이의 필드 대응표(예: maximumLoadMass 와 cargoMaxWeight)가 공식으로 제공되는가, ROP 등록부는 어느 형식을 정본으로 삼고 나머지를 어떻게 변환해야 하는가? | 4, 21, 5 | 열림 | — |
| new | — | 싱가포르 공공 의료의 RoMi-H 등재 프로그램처럼 벤더·통합사를 사전 평가해 등록 자격을 주는 관문을 국내 병원·공공 현장에서 운용한 사례나 제도가 있는가? | 4, 63, 58 | 열림 | — |
| new | — | 팩트시트·명판에 없는 능력(문 조작·승강기 탑승·인계 동작 등)을 등록할 때 Open-RMF 의 task_capabilities 나 자산관리셸 능력 기술 서브모델을 실제로 쓴 사례가 있는가? | 4, 5, 6 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 병원 | 시작 조건 | docs/categories/robot-ontology/heterogeneous-robot-registration.md#5-적용-사례-현장-유형-명시 | 4. 이기종 로봇 등록 |
| 병원 | 작업 대상 | docs/categories/robot-ontology/heterogeneous-robot-registration.md#5-적용-사례-현장-유형-명시 | 4. 이기종 로봇 등록 |
| 병원 | 수행 자원 | docs/categories/robot-ontology/heterogeneous-robot-registration.md#5-적용-사례-현장-유형-명시 | 4. 이기종 로봇 등록 |
| 병원 | 제약 | docs/categories/robot-ontology/heterogeneous-robot-registration.md#5-적용-사례-현장-유형-명시 | 4. 이기종 로봇 등록 |
| 병원 | 완료·인계 | docs/categories/robot-ontology/heterogeneous-robot-registration.md#5-적용-사례-현장-유형-명시 | 4. 이기종 로봇 등록 |
| 기타 | 수행 자원 | docs/categories/robot-ontology/heterogeneous-robot-registration.md#5-적용-사례-현장-유형-명시 | 4. 이기종 로봇 등록 |
| 기타 | 제약 | docs/categories/robot-ontology/heterogeneous-robot-registration.md#5-적용-사례-현장-유형-명시 | 4. 이기종 로봇 등록 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| IDTA 02006 Digital Nameplate for Industrial Equipment (3.0) | 표준 | IDTA(Industrial Digital Twin Association) | 4, 21, 57 | ref-876 | https://industrialdigitaltwin.org/wp-content/uploads/2025/10/IDTA-02006-3-0-1_Submodel_Digital-Nameplate.pdf |
| IDTA-01002 Asset Administration Shell Specification — API (3.2.0) | 표준 | IDTA(Industrial Digital Twin Association) | 4, 6, 21 | ref-880 | https://github.com/admin-shell-io/aas-specs-api |
| RoMi-H Empanelment Programme (싱가포르 공공 의료기관 시스템 통합사 등재) | 평가 프로그램 | Changi General Hospital CHART(Centre for Healthcare Assistive & Robotics Technology) | 4, 63, 58 | ref-878 | https://www.cgh.com.sg/news/robotics/empanelment-for-robotic-middleware-for-healthcare--romi-h--syste |

## 추가 조사 요청

- 4절·7절 디지털 명판(IDTA 02006 3.0)의 정확한 필수·선택 속성 목록 — PDF 본문을 열어 YearOfConstruction·OrderCodeOfManufacturer 의 카디널리티 변경까지 확인해야 f5 를 [사실]로 되돌릴 수 있다
- 7절 OPC UA for Robotics(OPC 40010-1 1.02) ControllerType 의 식별 속성과 SoftwareRevision 유무 — 이번 검증이 열람 상한으로 확인하지 못해 본문에서 뺐다
- 4절·6절 IDTA 02047 서브모델의 개별 속성명과 VDA 5050 팩트시트 필드 대응 세부, 그리고 디지털 명판·기술 데이터 서브모델과의 연계 여부 — 검색 요약과 README 에서 확인하지 못해 서술을 컬렉션 이름 수준으로 제한했다
- 6절 자산관리셸 디스커버리·레지스트리 호출 순서(자산 ID→AAS ID→엔드포인트) — IDTA Part 2 원문 미열람으로 본문에 단정하지 않았다
- 5절 제조 공장·물류창고·상업 시설·가정·실외 현장의 이기종 로봇 등록 사례 — 제조 공장 후보(MDPI Applied Sciences 다중 브랜드 플릿 통합)는 403 으로 열지 못했다
- 5절 RoMi-H 등재 평가의 기술 항목(어댑터 시험·적합성 검사 등) — 공지에 없어 미확인
- 4절 URDF 공식 문서 — wiki.ros.org·docs.ros.org 를 열지 못해 URDF 정의를 arXiv 초록에 기댔다
- 11절 oq-128 국내 운영 사례 — 중기부 스마트공장 고도화 사업의 AAS 적용 의무화 문구가 검색 요약에만 보여 확인이 필요하다

## 이행한 수정 지시

- f5 강등 — 4절 디지털 명판 항목과 7절 표를 [추정][^ref-876]으로 쓰고 '필수 6개·선택 5개' 구분을 뺐으며 식별·버전 항목을 담는다는 수준으로만 서술하고 필수·선택 구분은 '미확인'으로 남겼다. 정확한 목록은 additional_research_requests 1번으로 넘겼다
- 용어집 '디지털 명판' 정의 수정 — glossary_updates 에서 필수·선택 구절을 지우고 식별·버전 항목을 담는 서브모델로 고쳤으며 description 에 필수·선택 미확인을 적었다
- f7 강등 — 3절에서 세 형식의 공통 항목을 제조사명·기종(시리즈)·일련번호로 좁혀 [추정][^ref-228][^ref-230][^ref-876]으로 쓰고, 치수·최대 적재·최대 속도는 VDA 5050 팩트시트와 MassRobotics identityReport 두 형식의 공통 항목으로만 별도 문장([추정][^ref-228][^ref-230])에 썼다
- f8 축소 — 7절 표의 OPC UA for Robotics 행에 MotionDevice 의 Manufacturer·Model·SerialNumber·ProductCode 네 가지만 [사실]로 쓰고 Controller 의 식별 속성과 SoftwareRevision 은 '미확인'으로 표시했다. reference_updates 의 ref-881 요약도 같은 범위로 고쳤다
- f4 구절 제거 — 4절 AGV 기술 데이터 서브모델 항목과 7절 표에서 '디지털 명판·기술 데이터 서브모델과 연계' 구절을 빼고 7개 컬렉션 이름과 혼합 플릿 통합·시운전·운영·유지보수 목표만 [사실][^ref-198]으로 썼다
- f9 표현 수정 — 6절 '표준 문서 자체의 기계가독 형식'에서 '배포하기 시작했다'를 '제공한다'로 썼다
- f19·f20·f21 정량 결과 제외 — 6절·8절에 정확도 수치를 쓰지 않았고 6절에 '정량 결과는 초록에 없어 적지 않는다'고 밝혔으며 f22 는 [사실][^ref-239][^ref-465][^ref-883]으로 유지했다
- f16 벤더 주장 병기 — 5절 기타 사례와 8절에서 [추정] 벤더 주장[^ref-875]으로 쓰고 '국내 첫 이기종 로봇 통합관제 솔루션'과 '50대 이상'을 기사 인용임을 밝혀 썼으며 VDA 5050 지원·연동 제조사 수·등록 방식은 쓰지 않았다
- 5절 현장 유형 명시 — 병원 2건(타르투대학교병원 검체 운반 f13, RoMi-H 등재 f15)과 기타 1건(인천공항 f16)을 각각 현장 유형·사례·여섯 항목 표·서술로 썼고, 물류창고·제조 공장·상업 시설·가정·실외 사례는 확인되지 않았음을 절 첫 문장에 적었으며, site_matrix_updates 의 site_type 을 병원·기타로만 냈다
- 9절 경계 — f24·f25 를 [추정]으로만 쓰고 f25 의 위치추정·주행 방식·펌웨어 버전은 '연계 대상:' 단락에서 분류 원문 19장 '로봇 자체 지능·제어' 행의 연계 대상으로 짧게 다뤘다
- 11절 열린 질문 — oq-128 을 해결로 바꾸지 않고 f17·f18 로 부분 진전(국내 설계 연구·벤더 소개만 확인, 운영 사례 미확인)임을 적었으며 open_questions_new 4건을 브리프 형식대로 open_question_updates 에 new 로 등록했다(근거 f23·f7·f15·f12)
- f11·f23 유지 — 6절에서 둘 다 [추정]으로 쓰고 '확인되지 않았다'는 서술을 남겼으며, f11 의 자산 ID→AAS ID→엔드포인트 순서는 '원문을 열지 못해 단정하지 않는다'고 적었다
- 각주 표기 — 8절에서 ref-239·ref-465·ref-883 은 arXiv 초록으로, ref-043 은 KCI 초록만 확인했음을 밝혔고, ref-198·ref-876 의 각주 정의에 ' (원문 미열람)'을 붙이지 않았다
- 분량 초과 자동 분리: 4. 이기종 로봇 등록 본문 11,446자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 4,109자
