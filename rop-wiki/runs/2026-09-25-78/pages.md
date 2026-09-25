# 스토리텔러 산출 2026-09-25-78

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md | draft | q4-04 답함(3절 {#q4-04} 신설: 지도 판 식별·배포 규칙은 사실, 판 대응표·재검증 범위·배포 순서·안전 재검토 구분은 추정), 후속 질문 q4-15·q5-08, q4-14 폐기로 2절 표에서 제외, 상태 줄 답한 질문 4건, 6절 막힌 질문에 q4-15 추가, 7절 목록에 23·25 추가, 4·5·8·9절 갱신. 머리 줄 수정 때문에 전체 페이지로 보냄 |
| update | docs/tracks/floorplan-recognition/space-graph-schema-draft.md | draft | v1.1 → v1.2: 평면도 '버전' 속성에 값 후보(상태·개정 코드, 후보)와 IFC GlobalId 대응 메모 추가(f7·f9). 층별 지도 '판 식별자(후보)'는 반영하지 않고 6절 지도 버전 항목 근거 보강, 정합 절차 초안에 판 교체 시 재검증 단계 추가. H1 버전 표기를 (v1.2)로 맞추려고 전체 페이지로 보냄 |
| update | docs/ideas/floorplan-recognition.md | draft | 5절에 '도면·지도 판 관리와 재검증' 소절 신설(q4-04 요약, 정합 절차 초안 7단계 추가, 종합은 추정) |
| update | docs/tracks/floorplan-recognition/index.md | draft | 6. 살아있는 산출물 링크: 스키마 초안 현재 버전 v1.2 로 갱신, 실행 2026-09-25-78(q4-04) 요약 단락 추가. 상태 줄(현재 단계 4, 마지막 트랙 실행 2026-09-25)은 바뀌지 않음 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 건축 도면 자동 인식 단계 4 | q4-04 답함(지도 판 식별·배포 규칙과 도면 개정 관리는 사실, 판 대응표·재검증 범위·배포 순서는 추정), 공간 그래프 스키마 초안 v1.1 → v1.2, 후속 질문 q4-15·q5-08, q4-14 중복 폐기 | run 2026-09-25-78
- 홈 최근 업데이트: 2026-09-25 — 건축 도면 자동 인식 단계 4: q4-04(도면·지도가 바뀔 때의 판 관리와 재검증) 답함, 공간 그래프 스키마 초안 v1.2
- 대분류 최근 업데이트: 2026-09-25 — 6. 지도·공간·위치 모델(건축 도면 자동 인식 트랙 단계 4): 지도 판 식별·배포 규칙, 도면 개정 관리와 판 대응표·차이 기반 재검증 범위(추정) 정리
- 세부영역 최근 업데이트: 2026-09-25 — 6. 지도·공간·위치 모델: 트랙 단계 4 q4-04 결과(지도 판 관리·재검증)를 6절·9절 반영 제안으로 남김

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 공통 데이터 환경 | Common Data Environment (CDE) | ISO 19650 정보 관리에서 도면·모델 같은 정보 컨테이너를 상태·개정 메타데이터와 함께 관리하는 환경(영국 국가 부속서 기반 지침 기준). | 6, 24 | ref-745 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-153 | Open Robotics | Fleet Adapter Tutorial - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html |
| ref-212 | continua-systems (GitHub) | vdma-lif — schema/lif-schema.json (JSON parsers and models for the VDMA LIF, VDMA 공식 산출물이 아닌 제3자 스키마) | 오픈소스 문서 | medium | https://github.com/continua-systems/vdma-lif/blob/main/schema/lif-schema.json |
| ref-652 | Stefanini, E., Ciancolini, E., Settimi, A., & Pallottino, L. | Safe and Robust Map Updating for Long-Term Operations in Dynamic Environments | 논문 | medium | https://www.mdpi.com/1424-8220/23/13/6066 |
| ref-743 | IfcOpenShell (IfcOpenShell GitHub) | IfcDiff - IfcOpenShell documentation (src/ifcopenshell-python/docs/ifcdiff.rst, v0.8.0) | 오픈소스 문서 | medium | https://docs.ifcopenshell.org/ifcdiff.html |
| ref-744 | Open Robotics (open-rmf) | rmf_building_map_msgs — rmf_building_map_msgs/msg/BuildingMap.msg | 오픈소스 문서 | medium | https://github.com/open-rmf/rmf_building_map_msgs/blob/main/rmf_building_map_msgs/msg/BuildingMap.msg |
| ref-745 | UK BIM Framework | Information management according to BS EN ISO 19650 Guidance Part C: Facilitating the common data environment (workflow and technical solutions), Edition 1 | 정부·연구기관 | medium | https://ukbimframework.org/wp-content/uploads/2020/09/Guidance-Part-C_Facilitating-the-common-data-environment-workflow-and-technical-solutions_Edition-1.pdf |
| ref-746 | ACCA software (BibLus) | Container Information States ISO 19650: WIP, Shared, Published, Archived | 벤더 문서 | low | https://biblus.accasoftware.com/en/container-information-states-iso-19650-wip-shared-published-archived/ |
| ref-747 | 이일곤, 김현민, 안준상, 최재웅 | ISO 19650 기반의 한국형 공통데이터환경(CDE) 개발을 위한 CDE 워크플로우와 정보컨테이너 체계 수립 연구 | 논문 | medium | https://koreascience.kr/article/JAKO202309243229252.pdf |
| ref-748 | Liu, H., Gao, G., & Gu, M. (EG-ICE 2023, 511-520) | A Parallel IFC Normalization Algorithm for Incremental Storage and Version Control (arXiv 프리프린트) | 논문 | medium | https://arxiv.org/abs/2312.14931 |
| ref-749 | Esser, S., Vilgertshofer, S., & Borrmann, A. (Automation in Construction 155, 105063) | Version control for asynchronous BIM collaboration: Model merging through graph analysis and transformation | 논문 | medium | https://www.sciencedirect.com/science/article/pii/S0926580523003230 |
| ref-472 | A3 (Association for Advancing Automation) | ANSI/A3 R15.08-2 Safety Standard for Industrial Mobile Robot Systems and Applications Now Available | 표준 | medium | https://www.automate.org/robotics/news/ansi-a3-r15-08-2-safety-standard-for-industrial-mobile-robot-systems-and-applications-now-available |
| ref-470 | ISO | ISO 3691-4:2023 - Industrial trucks — Safety requirements and verification — Part 4: Driverless industrial trucks and their systems | 표준 | medium | https://www.iso.org/standard/83545.html |
| ref-752 | NODE Robotics | Real-time Robot Map Management for Mobile Fleets (NODE.maps) | 벤더 문서 | low | https://node-robotics.com/solutions/node-fleet-autonomy-services/nodemaps |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 제조사가 자사 로봇 지도(SLAM 지도)의 판을 바꿀 때 변경 내용과 판 식별자를 ROP 나 상위 관제에 알리는 계약·인터페이스 관행이나 공개 사례가 있는가? | 24, 28 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 출하 | 완료·인계 | docs/tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md#q4-04 | 단계 4. 지도 변환 보정과 현장 정합 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| IfcDiff (IfcOpenShell IFC 모델 비교 도구, v0.8.0 문서) | 오픈소스 | IfcOpenShell | 6, 24 | ref-743 | https://docs.ifcopenshell.org/ifcdiff.html |
| BS EN ISO 19650 Guidance Part C: 공통 데이터 환경(Edition 1) | 프레임워크 | UK BIM Framework | 6, 24, 28 | ref-745 | https://ukbimframework.org/wp-content/uploads/2020/09/Guidance-Part-C_Facilitating-the-common-data-environment-workflow-and-technical-solutions_Edition-1.pdf |

## 추가 조사 요청

- q4-04 후속: Open-RMF building.yaml·주행 그래프 파일에 판 표기가 있는지(단계 4 페이지 3절 q4-04 의 형식 밖 판 메타데이터 추정 보강에 필요)
- q4-04 후속: ISO 19650-1·2 발행 기관 자료(또는 국내 KS 부합화본)로 정보 컨테이너 상태·개정 코드를 확인(현재 f7 은 업체 블로그 기준으로 강등)
- q4-04 후속: ISO 3691-4:2023 과 ANSI/A3 R15.08-2-2023 에서 운용 구역·지도 변경 뒤 재검증·재평가를 요구하는 조문(안전 재검토 구분 추정의 근거 보강)
- q4-04 후속: VDMA LIF 공식 명세에서 layoutVersion 등 판 필드 확인(현재 제3자 스키마 기준)

## 이행한 수정 지시

- f7 강등 — 단계 페이지 q4-04 절과 아이디어 페이지에서 [추정]으로 쓰고 '영국 BIM Framework 지침 Part C(2020-09, ISO 19650-2 영국 국가 부속서 기준)는 CDE 정보 컨테이너 메타데이터에 상태·개정 코드를 두며, 상태 목록은 업체 블로그(벤더 문서) 요약 기준' 범위로 줄였다.
- f1~f4 중복 방지 — q4-04 절에서 mapId·mapVersion 식별, 사전 적재·활성화, 구역 집합 불변·새 zoneSetId, initializePosition 은 q4-02·q4-03 절로 링크만 하고 UNKNOWN_MAP_ID·관제 책임, mapHash, enableMap 시 다른 판 비활성, DUPLICATE_MAP, 지도 자체 삭제 금지와 deleteMap, zoneSet 의 mapVersion 비참조, 신규 zoneSet DISABLED 만 ref-031 각주로 더하고 발행일 미확인(oq-005)을 표기했다.
- ref-031 직접 인용 — 모든 페이지에서 ref-031 문장은 재서술만 했고 직접 인용은 0회다.
- f16 — 새 문장을 만들지 않고 q4-03 절의 기존 ref-153 문장으로 링크했다.
- f12 — 문장을 'Stefanini 외(Sensors 23(13), 2023-06-30)는 자세 추정이 틀리면 지도 갱신이 오류를 낳는다고 보고, 자세 추정 불확실성을 고려한 안전한 라이다 점유 격자 지도 갱신을 제안했다'로 고치고 연계 대상 표시를 유지했다.
- f10 — ref-748 각주·참고문헌 기관을 'Liu, H., Gao, G., & Gu, M. (EG-ICE 2023, 511-520)'으로, 제목에 arXiv 프리프린트임을 적었다.
- f8 — 게재 승인일을 쓰지 않고 '2023, 게재지 미확인'으로만 적었다.
- f13·f14 — 본문에 'ISO 3691-4:2023 판 기준', 'ANSI/A3 R15.08-2-2023 기준'을 명시하고 이후 개정·후속 파트 내용은 미확인이라고만 적었다.
- f15 — [추정]에 '벤더 주장(원문 미열람)'을 병기하고 판 식별·종합의 근거로 쓰지 않는다고 적었다.
- f23 — 검색 횟수를 '검색 13회, 한국어 3회'로 self_check 와 맞췄다.
- 각주 — ref-745~ref-752 와 ref-212·ref-652 의 각주 정의에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었으며, ref-743·ref-744 는 표시하지 않았고 ref-153 은 기존 참고문헌 표기를 따랐다.
- 평면도 modify 승인 — 스키마 초안 2절 평면도 행의 '버전'에 상태·개정 코드 값 후보(영국 BIM Framework 지침, ISO 19650-2 영국 국가 부속서 기준, 후보)와 IFC GlobalId 대응 메모를 더하고 확정 유지, ontology_version 1.1 → 1.2, 세부 코드 값은 넣지 않았다.
- 층별 지도 판 식별자 거부 — 스키마 초안에 반영하지 않고 6절 지도 버전 항목의 근거 보강(f1·f3·f5·f6, 판 대응표 추정 f17)으로 두었다.
- q4-04 답함 — 단계 페이지 3절 {#q4-04} 소제목 첫 단락에 판 식별·배포 규칙은 사실, 판 대응표·재검증 범위·배포 순서·안전 재검토 구분은 이 위키의 종합(추정·low)임을 명시했다.
- 백로그 q4-14 — backlog_updates 에서 폐기로 바꾸고 단계 페이지 2절 표에서 뺐다(2절 머리 문장에 사유 명시).
- 용어집 — '정보 컨테이너'는 등록하지 않았고, '공통 데이터 환경' 정의를 지시한 범위로 줄이고 '단일 정보원' 문구를 뺐다.
- 단계 페이지 6절 — 완료 조건 두 항목의 충족 판정을 유지하고 '다음 단계로 전환: 아니오(막힌 질문 …)'로 적었으며 stage_transition 을 넣지 않고 트랙 개요 현재 단계를 단계 4 로 유지했다.
- f22 — 시나리오 표 앞에 '다음은 설명을 위한 가상의 시나리오이다'를 두고 물류 흐름 단계 출하, 완료·인계 칸만 f22 로 채우고 나머지는 해당 없음으로 두었다.
- 2차: 단계 4 페이지 상태 줄 — '답한 질문: 3건'을 '답한 질문: 4건'으로 고쳤고, 절 밖이라 페이지 머리를 포함한 전체 페이지(content)로 보냈으며 퍼블리셔 요청 문장은 additional_research_requests 에서 뺐다.
- 2차: 스키마 초안 H1 — '(v1.1)'을 '(v1.2)'로 고쳐 프런트매터 ontology_version·ontology_draft_version 과 맞췄고, 전체 페이지(content)로 보냈으며 additional_research_requests 의 해당 요청 문장을 지웠다.
- 2차: 단계 4 페이지 6절 아래 줄을 '다음 단계로 전환: 아니오(막힌 질문 q4-05·q4-07·q4-08·q4-09·q4-10·q4-11·q4-12·q4-13·q4-15)'로 고치고 log_entry 의 막힌 질문 목록에도 q4-15 를 더했다.
- 2차: 단계 4 페이지 7절 글머리 목록에 23. 시험·형식 검증·벤치마크(도면 판 차이 기반 재검증 범위, 추정)와 25. 안전·위험 관리(운용 구역·위험성평가 표준과 안전 재검토, 연계 대상 명시, 추정) 항목을 더해 프런트매터 related_areas 와 맞췄다(새 사실 없음).

## 트랙 갱신

- 단계 페이지: docs/tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md
- 온톨로지 초안 버전: 1.2
- 트랙 로그 항목: 답한 질문: q4-04(f1~f23; 판 식별·배포 규칙과 도면 개정 관리·판 비교는 사실, 판 대응표·재검증 범위·배포 순서·안전 재검토 구분은 추정) / 새 질문: q4-15(f18), q5-08(f19) / 백로그 정리: q4-14 폐기(q4-13 과 같은 질문) / 온톨로지 변경: v1.1 → v1.2: 평면도 '버전' 값 후보(상태·개정 코드, 후보)와 IFC GlobalId 대응 메모 추가(f7·f9); 거부: 층별 지도 '판 식별자(후보)'(f1·f3·f5·f6 → 6절 지도 버전 항목 근거 보강). 버전 이력 행: 1.2 | 2026-09-25 | 평면도 '버전' 값 후보(상태·개정 코드)와 IFC GlobalId 대응 메모 추가(f7·f9), 거부: 층별 지도 '판 식별자(후보)'(6절 근거 보강) | 2026-09-25-78 / 완료 조건 평가: 충족(검증 stage_complete true), 단계 전환 미승인(막힌 질문 q4-05·q4-07·q4-08·q4-09·q4-10·q4-11·q4-12·q4-13·q4-15) / 세부영역 반영 제안: 24. 자산·소프트웨어 수명주기 관리, 6. 지도·공간·위치 모델(2건), 23. 시험·형식 검증·벤치마크 — 4건 / 다음 실행 제안: q4-07(지도 파일 변환·배포와 mapVersion 책임) 또는 q4-08(플릿별 그래프 동기화)
- 개요 진행 현황: 단계 4 진행 중 — 열린 질문 9, 답함 4, 완료 조건 충족(단계 전환 미승인)

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q4-04 | 답함 | docs/tracks/floorplan-recognition/stage-4-map-conversion-and-site-alignment.md#q4-04 | — | — | — |
| q4-14 | 폐기 | — | — | — | — |
| q4-15 | 열림 | — | 도면 개정의 판 차이(IfcDiff 의 추가·삭제·변경 요소)에서 영향받는 공간 노드·차선·목적지와 그 요소가 걸친 제조사별 지도 판·구역 집합·좌표 변환을 자동으로 추려 재검증 범위를 정하는 규칙은 무엇이며, GlobalId 가 없는 CAD·래스터 도면에서는 요소 대응을 어떻게 만드는가? (q4-04 에서 파생) | 4 | f18 |
| q5-08 | 열림 | — | 지도 판을 교체한 뒤 재검증 시험(목적지 대응점 잔차, 영향받은 차선 주행, 구역 규칙 확인)의 합격 기준과 판 교체에 드는 중단 시간·재검증 공수를 어떤 지표로 측정하는가? (q4-04 에서 파생) | 5 | f19 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 24 | 6. 대표 접근법과 기술 | VDA 5050 3.0.0 지도 판 식별(mapId·mapVersion)·사전 적재·활성화(mapId 당 한 판)·관제 주도 삭제 규칙, 공통 데이터 환경의 도면 상태·개정 관리(추정)와 IfcDiff 기반 IFC 판 비교, 판 대응표와 차이 기반 재검증 범위·배포 순서(추정) |
| 6 | 6. 대표 접근법과 기술 | 지도 판 관리와 판 대응표(도면 개정·공간 그래프 판·제조사 지도 판·구역 집합·좌표 변환을 한 행으로 묶음, 추정), Open-RMF 건물 지도 메시지의 판 필드 부재 |
| 6 | 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준) | 판 대응표 관리·재검증 범위 산정·배포 순서는 ROP, 지도 갱신 계산과 보호 영역·안전 기능 재검증은 로봇·통합자 쪽 연계 대상이라는 경계(추정) |
| 23 | 6. 대표 접근법과 기술 | 도면 판 차이(추가·삭제·변경 요소)로 재검증 범위를 좁히는 방법과 구역·동선 변경 여부에 따른 안전 재검토 구분(추정), oq-090 근거 보강 |
