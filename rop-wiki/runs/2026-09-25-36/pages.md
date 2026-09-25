# 스토리텔러 산출 2026-09-25-36

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/floorplan-recognition/stage-2-data-and-standards.md | draft | q2-02 답함(3절 q2-02 소제목 신설: BIM·벡터 CAD·래스터 입력별 정보 항목과 빠지는 정보, 입력 형식별 비교표), 2절 표에 q2-08·q2-09 추가, 4·5·6·7·8·9절 갱신. H1 아래 단계 상태 줄(열린 질문 6건·답한 질문 2건)은 H2 밖이라 patches 로 바꾸지 못했다 — 퍼블리셔 쪽 갱신 필요 |
| update | docs/tracks/floorplan-recognition/space-graph-schema-draft.md | draft | 초안 v0.4 → v0.5: 문 BIM 대응 클래스 IfcDoor(f1), 계단 BIM 대응 클래스 IfcStair(f3), 엘리베이터 유형 값 ELEVATOR 확정(f4), 평면도 길이 단위·축척 정보 속성(f12) 반영, 6절에 거부된 변경(계단이 잇는 층 도출, 래스터 축척 복원)과 프록시·충전 위치 질문 추가. H1 의 '(v0.4)' 표기는 H2 밖이라 patches 로 바꾸지 못했다 — 퍼블리셔가 프런트매터 ontology_version 으로 '(v0.5)'로 맞춰야 한다 |
| update | docs/ideas/floorplan-recognition.md | draft | 4절에 '입력 형식별 정보 항목' 소절(q2-02, 실행 2026-09-25-36) 신설, 4절 머리말과 q2-01 소절의 'q2-02 미조사' 문장을 갱신 |
| update | docs/tracks/floorplan-recognition/index.md | draft | 6. 살아있는 산출물 링크 갱신(스키마 초안 v0.5, 아이디어 4절 입력 형식별 정보 항목, 백로그 q2-02 답함·후속 질문 2건). H1 아래 트랙 상태 줄(현재 단계 단계 2, 마지막 트랙 실행)은 H2 밖이라 patches 로 바꾸지 못했다 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 건축 도면 자동 인식 단계 2 | q2-02 답함(도면 입력 형식별 정보 항목), 공간 그래프 스키마 초안 v0.4 → v0.5, 후속 질문 2건(q2-08·q2-09), 1차 조건부 승인 수정 17건 이행 | run 2026-09-25-36
- 홈 최근 업데이트: 2026-09-25 — 건축 도면 자동 인식 단계 2: 도면 입력 형식(BIM·벡터 CAD·래스터 스캔)별로 담기는 정보와 빠지는 정보 정리(q2-02), 공간 그래프 스키마 초안 v0.5
- 대분류 최근 업데이트: 2026-09-25 — 건축 도면 자동 인식 단계 2: 6. 지도·공간·위치 모델 관련 도면 입력 형식별 정보 항목(q2-02) 확인, 스키마 초안 v0.5(실행 2026-09-25-36)
- 세부영역 최근 업데이트: 2026-09-25 — 건축 도면 자동 인식 단계 2: 도면 입력 형식별 공간 정보와 국내 CAD 레이어 표준을 7. 관련 표준·프레임워크·오픈소스 절에 반영하도록 제안(실행 2026-09-25-36)

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 도면 교환 형식 | Drawing Exchange Format (DXF) | 레이어·블록·엔터티로 CAD 도면을 담는 교환 파일 형식으로, ezdxf 문서 기준 좌표·길이 값에 단위가 붙지 않고 모델 공간 단위는 선택 헤더 변수($INSUNITS)로 준다. | 6, 28 | ref-743, ref-744, ref-745 |
| new | 블록 참조 | Block Reference (INSERT) | CAD 도면에서 여러 번 재사용하는 엔터티 묶음(블록)을 위치·회전·축척을 주어 한 번 배치한 것으로, 태그가 붙은 속성 텍스트(ATTRIB)를 달아 메타데이터를 실을 수 있다. | 6, 27 | ref-743, ref-753 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-738 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcDoor (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 표준 | high | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/shared/IfcSharedBldgElements/Entities/IfcDoor.md |
| ref-739 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcStair (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 표준 | high | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/shared/IfcSharedBldgElements/Entities/IfcStair.md |
| ref-740 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcTransportElementTypeEnum (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 표준 | high | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Types/IfcTransportElementTypeEnum.md |
| ref-741 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcWall (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 표준 | high | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/shared/IfcSharedBldgElements/Entities/IfcWall.md |
| ref-742 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcBuildingStorey (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 ADD2와 문구가 다를 수 있음) | 표준 | high | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/core/IfcProductExtension/Entities/IfcBuildingStorey.md |
| ref-743 | Moitzi, M. (mozman/ezdxf GitHub) | ezdxf documentation — Concepts: Blocks (docs/source/concepts/blocks.rst) | 오픈소스 문서 | medium | https://github.com/mozman/ezdxf/blob/master/docs/source/concepts/blocks.rst |
| ref-744 | Moitzi, M. (mozman/ezdxf GitHub) | ezdxf documentation — Concepts: Layers (docs/source/concepts/layers.rst) | 오픈소스 문서 | medium | https://github.com/mozman/ezdxf/blob/master/docs/source/concepts/layers.rst |
| ref-745 | Moitzi, M. (mozman/ezdxf GitHub) | ezdxf documentation — Concepts: DXF Units (docs/source/concepts/units.rst) | 오픈소스 문서 | medium | https://github.com/mozman/ezdxf/blob/master/docs/source/concepts/units.rst |
| ref-746 | ISO | ISO 13567-1:2017 - Technical product documentation — Organization and naming of layers for CAD — Part 1: Overview and principles | 표준 | medium | https://www.iso.org/standard/70181.html |
| ref-747 | National Institute of Building Sciences (United States National CAD Standard) | AIA CAD Layer Guidelines, Layer Name Format (NCS V5) | 표준 | medium | https://www.nationalcadstandard.org/ncs5/pdfs/ncs5_clg_lnf.pdf |
| ref-748 | 국가표준인증통합정보시스템(KSSN) | KS F 1542(2020 확인) CAD 도면 작성을 위한 레이어 원칙과 기준 | 표준 | medium | https://www.kssn.net/search/stddetail.do?itemNo=K001010129900 |
| ref-749 | 국토교통부 건설사업정보시스템(CALS) | 건설CALS 전자도면 작성표준 | 정부·연구기관 | medium | https://www.calspia.go.kr/portal/intro/introStandard02.do |
| ref-750 | 신동철(대한건축학회 논문집 계획계) | 건축 표준 캐드 레이어의 실무적용 실태 분석 연구 | 논문 | medium | https://www.dbpia.co.kr/Journal/articleDetail?nodeId=NODE01288876 |
| ref-751 | Noardo, F., Arroyo Ohori, K., Krijnen, T., & Stoter, J. (Applied Sciences 11(5), 2232) | An Inspection of IFC Models from Practice | 논문 | medium | https://www.mdpi.com/2076-3417/11/5/2232 |
| ref-752 | arXiv 2607.12678 저자(미확인) | Text-Aided Multi-Modal Panoptic Symbol Spotting for CAD Floor Plan Drawings | 논문 | medium | https://arxiv.org/abs/2607.12678 |
| ref-753 | ArchiAI Lab (ArchCAD-400K 프로젝트) | ArchCAD-400k: A Large-Scale CAD drawings Dataset and New Baseline for Panoptic Symbol Spotting — project page | 오픈소스 문서 | medium | https://archiai-lab.github.io/ArchCAD.github.io/ |
| ref-754 | Buildings(MDPI) 게재 논문 저자(미확인) | Raster Image-Based House-Type Recognition and Three-Dimensional Reconstruction Technology | 논문 | medium | https://doi.org/10.3390/buildings15071178 |
| ref-755 | 국토교통부 | 건설산업 BIM 시행지침 정책정보 상세보기 | 정부·연구기관 | medium | https://www.molit.go.kr/USR/policyData/m_34681/dtl.jsp?srch_usr_titl=Y&psize=10&lcmspage=1&id=4634 |

## 열린 질문 갱신

- 없음

## 흐름 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| ISO 13567-1:2017 CAD 레이어 구성·명명 — Part 1: 개요와 원칙 | 표준 | ISO | 6, 28 | ref-746 | https://www.iso.org/standard/70181.html |
| 미국 국가 CAD 표준(NCS) AIA CAD 레이어 이름 형식(V5, V6 판 있음) | 표준 | National Institute of Building Sciences | 6, 28 | ref-747 | https://www.nationalcadstandard.org/ncs5/pdfs/ncs5_clg_lnf.pdf |
| KS F 1542 CAD 도면 작성을 위한 레이어 원칙과 기준 | 표준 | 국가표준인증통합정보시스템(KSSN) | 6, 28 | ref-748 | https://www.kssn.net/search/stddetail.do?itemNo=K001010129900 |
| 건설CALS/EC 전자도면 작성표준(V1.1, KCCS-0001-2006) | 표준 | 한국건설기술연구원(건설CALS 체계) | 6, 28 | ref-749 | https://www.calspia.go.kr/portal/intro/introStandard02.do |
| ezdxf (DXF 읽기·쓰기 라이브러리) | 오픈소스 | Moitzi, M. (mozman/ezdxf GitHub) | 6 | ref-743 | https://github.com/mozman/ezdxf/blob/master/docs/source/concepts/blocks.rst |

## 추가 조사 요청

- 단계 2 페이지·스키마 초안·트랙 개요의 H1 아래 상태 줄과 스키마 초안 H1 의 '(v0.4)' 표기는 H2 절 밖이어서 patches 로 갱신할 수 없었다: 단계 상태 줄(열린 질문 6건·답한 질문 2건·마지막 실행 2026-09-25), 스키마 H1 '(v0.5)', 트랙 개요 상태 줄(현재 단계: 단계 2. 필요한 데이터와 표준 조사 · 마지막 트랙 실행: 2026-09-25)을 퍼블리셔가 프런트매터·트랙 설정 값으로 맞추도록 pipeline 담당에게 요청한다
- q2-03(관제 수용 형식): 층별 지도·공용 자원 목록을 로봇 관제·ROP가 받아들이는 형식(제조사 지도 형식, LIF, Open-RMF building.yaml 등) — 단계 2 완료 조건과 아이디어 4절에 필요
- 단계 2 완료 조건: 표준에 대응시킨 관계(엣지) 유형(문·계단·엘리베이터 연결의 IndoorGML·IFC 대응) 근거 — 스키마 초안 3절에 필요
- 실무 IFC 모델에서 엘리베이터·문·계단이 IfcBuildingElementProxy 로 내보내진 사례·비율(q2-09) — 단계 2 페이지 4절 불확실성 해소에 필요
- KS F 1542·건설CALS 전자도면 작성표준 원문의 문·계단·승강기·충전 위치 레이어·심벌 코드와 국내 실무 준수율(q2-08) — 원문 미열람으로 확인하지 못함

## 이행한 수정 지시

- f22 강등·분리 — 단계 2 페이지 3절 래스터 소절과 아이디어 4절 표에서 MLSTRUCT-FP 축척 메타데이터·Raster-to-Graph 512×512 정규화는 [사실](ref-069·ref-070), '축척을 별도 메타데이터나 축척 표기·치수 문자 인식으로 얻어야 한다'는 [추정]으로 나눠 썼다.
- f24 분리 — 계단·난간(CubiCasa5K·Kratochvila 외)과 출입문·창호·벽체·도면 문자(AI Hub) 라벨은 [사실], 엘리베이터 라벨 미확인은 [추정](전체 클래스 목록 미열람, 부재 확정 아님, q2-04)으로 나눠 썼다.
- f25 문구 — '축척이 이미지에 없다'를 빼고 '축척은 축척 표기·치수 문자에서 인식으로 복원해야 한다'로 써 f23 과 어긋나지 않게 했다([추정] 유지).
- f2 정의 — IfcWall 을 '공간을 둘러싸거나 나누는 수직 구조'로 고쳤고 evidence_excerpt 의 인용 문구는 직접 인용하지 않았다.
- f3 정의·컨테이너 — IfcStair 를 '다른 높이의 층 사이를 걸어서 오가게 하는 수직 통로'로, 컨테이너를 '기본 IfcBuildingStorey, 층에 할당할 수 없으면 IfcBuilding, 외부는 IfcSite'로 고치고 '여러 층에 걸치면' 표현과 인용 문구를 뺐다(단계 페이지·스키마 초안).
- f5 정의 — IfcBuildingStorey 를 '수직으로 경계 지어진 공간들의 (거의) 수평 집합'으로 옮겼다.
- f10·f11·f12 귀속 — DXF 진술을 모두 'ezdxf(오픈소스 DXF 라이브러리) 문서는 …라고 설명한다'로 쓰고, 벡터 CAD 소절 머리와 각주 제목에 'Autodesk 공식 DXF 참조 아님'을 남겼다.
- f7 — ref-751 기관을 'Noardo, F., Arroyo Ohori, K., Krijnen, T., & Stoter, J. (Applied Sciences 11(5), 2232)'로 고치고(각주·reference_updates), 본문의 '점검·채점했다'를 '점검했다'로 줄였다.
- f14 — 'NCS V5 문서 기준이며 2026-09-25 확인 시점에 V6 판(ncs6_clg_lnf.pdf)이 있다'를 본문·불확실성·참고문헌 요약에 명시했다.
- f15 — 'KS F 1542 로 국가표준화' 파생 관계를 삭제하고 건설CALS/EC 전자도면 작성표준(V1.0 2004-08, V1.1 KCCS-0001-2006 은 2006-12-26 한국건설기술연구원장 공고)과 KS F 1542(2020-12-21 확인)를 따로 썼으며 두 문서의 관계는 미확인으로 두었다.
- f19 — 예시 코드 'FM B 1321'을 빼고 주석의 유형·속성 결합 구조와 다중 모달 방법만 썼으며 발행일을 2026-07-14 로 적었다(본문·각주·reference_updates).
- f27 — 문장 앞에 '연계 대상: '을 붙이고 BIM 기반 지도·위치추정은 로봇 자체 지능·제어 쪽이며 도면 입력이 담지 못하는 정보의 근거로만 쓴다고 밝혔다.
- 원문 미열람 표기 — 단계 2 페이지 8절 각주에서 ref-746~ref-752·ref-754·ref-755 와 재사용 ref-063·ref-066·ref-067·ref-069·ref-070·ref-073·ref-074·ref-078·ref-081·ref-084·ref-215 의 접근일 뒤에 ' (원문 미열람)'을 붙였고(ref-156·ref-214·ref-334 는 페이지에 이미 있는 줄 유지), reference_updates 의 ref-746~ref-752·ref-754·ref-755 에 source_unopened: true 를 넣었다.
- 온톨로지 v0.4 → v0.5 — 스키마 초안 2절에 문 BIM 대응 클래스 IfcDoor(IfcRelFillsElement, OverallWidth·OperationType 메모, f1), 계단 BIM 대응 클래스 IfcStair(분해·기본 컨테이너, f3), 엘리베이터 유형 값 ELEVATOR 확정과 '(단계 2에서 확정)' 제거(f4), 평면도 길이 단위·축척 정보($INSUNITS, ezdxf 문서 기준, f12)를 반영했고, 계단이 잇는 층 도출(f6)은 6절 q3-05 질문, 래스터 축척 복원(f22)은 6절 q4-05 질문으로 두었으며 문의 IndoorGML 2.0 질문은 그대로 두었다. 프런트매터 ontology_version 과 ontology_draft_version 을 '0.5'로 맞췄다.
- 중복 새 질문 — 벡터 CAD 텍스트 결합 처리 흐름의 사람 검토 질문은 backlog_updates 에 넣지 않고 단계 2 페이지 5절에 'q3-01 로 흡수'로만 적었다.
- 단계 페이지 6절 — 두 완료 조건을 모두 미충족으로 적고 검증 판정 칸을 '미충족 · 미승인', 표 아래 줄을 '다음 단계로 전환: 아니오(q2-03 미작성, 엣지 표준 대응 없음; 열린 질문 q2-03·q2-04·q2-06·q2-07)'로 썼다.
- 중복 내용 — f6·f9·f18·f20·f22·f24·f26·f27 은 기존 각주(ref-156·ref-334·ref-214·ref-215·ref-066·ref-067·ref-084·ref-069·ref-070·ref-063·ref-078·ref-074·ref-081)를 재사용하고 q2-02 맥락의 연결로만 짧게 썼으며, f4 는 ref-213 과 ref-740 을 함께 썼다.
- docs/tracks/floorplan-recognition/space-graph-schema-draft.md: 각주 정의 10개를 참고문헌에서 만들어 붙임: ref-073, ref-738, ref-739, ref-740, ref-741, ref-745, ref-746, ref-747, ref-751, ref-754

## 트랙 갱신

- 단계 페이지: docs/tracks/floorplan-recognition/stage-2-data-and-standards.md
- 온톨로지 초안 버전: 0.5
- 트랙 로그 항목: 답한 질문: q2-02(도면 입력 형식별 정보 항목, f1~f30) / 새 질문: q2-08(f15), q2-09(f7); 벡터 CAD 텍스트 결합 처리 흐름의 사람 검토 질문은 q3-01 과 중복이어서 등록하지 않음 / 온톨로지 변경: v0.4 → v0.5: 문 BIM 대응 클래스 IfcDoor 추가(f1), 계단 BIM 대응 클래스 IfcStair 추가(f3), 엘리베이터 유형 값 ELEVATOR 확정(f4), 평면도 길이 단위·축척 정보 속성 추가(f12); 거부: 계단이 잇는 층 도출(f6 추정 → 6절 질문 q3-05), 래스터 축척 복원 방식(f22 강등 → 6절 질문 q4-05); 근거 실행 2026-09-25-36 / 완료 조건 평가: 미충족(부족: 관제 수용 형식 q2-03 미작성, 관계(엣지) 쪽 표준 대응 없음) / 세부영역 반영 제안: 6. 지도·공간·위치 모델 2건, 28. 표준·상호운용성·다사업자 거버넌스 1건, 27. AI·학습·적응과 모델 운영 1건 / 다음 실행 제안: q2-03, q2-07 / 비고: 단계·스키마·개요 페이지의 H1 아래 상태 줄과 스키마 H1 버전 표기는 patches 범위 밖이라 갱신하지 못함
- 개요 진행 현황: 단계 2 진행 중 — 열린 질문 6, 답함 2, 완료 조건 미충족

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q2-02 | 답함 | docs/tracks/floorplan-recognition/stage-2-data-and-standards.md#q2-02 | — | — | — |
| q2-08 | 열림 | — | 국내 실무 건축 CAD 도면은 KS F 1542·건설CALS 전자도면 작성표준의 레이어 체계를 얼마나 따르며, 그 표준 레이어·심벌 코드에 문·계단·승강기·충전 위치를 구분하는 코드가 있는가? (q2-02 에서 파생) | 2 | f15 |
| q2-09 | 열림 | — | 실무 IFC 모델에서 엘리베이터·문·계단이 IfcBuildingElementProxy 로 내보내지는 경우를 어떻게 찾아 보정하며(IDS 검사, 이름·형상 규칙 등), 그 빈도를 보고한 자료가 있는가? (q2-02 에서 파생) | 2 | f7 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 6 | 7. 관련 표준·프레임워크·오픈소스 | 도면 입력 형식별로 담기는 공간 정보와 빠지는 정보: IFC 4.3 의 IfcDoor·IfcStair·IfcTransportElement(ELEVATOR)·IfcBuildingStorey(ref-738~ref-742), DXF 좌표 무단위와 $INSUNITS(ezdxf 문서 기준, ref-745), 래스터 축척 메타데이터 사례(ref-069·ref-070, 일반화는 추정), 국내 CAD 레이어 표준(KS F 1542 ref-748, 건설CALS 전자도면 작성표준 ref-749), 충전 위치 표준 표현 부재(추정), BIM 기반 지도의 한계(연계 대상, ref-081). |
| 6 | 8. 대표 연구와 자료 | 교차 규칙(도면 해석은 6. 지도·공간·위치 모델에 적용)에 따라 ArchCAD-400K 레이어·블록 기반 자동 라벨링(ref-753), CAD 텍스트 결합 심볼 스포팅 프리프린트(ref-752, 2026-07-14), 래스터 치수 문자 인식 축척 계산(ref-754, 저자 보고 95% 초과)을 27. AI·학습·적응과 모델 운영 페이지와 함께 연결. |
| 28 | 7. 관련 표준·프레임워크·오픈소스 | CAD 레이어 명명 표준 ISO 13567-1:2017(ref-746), 미국 NCS AIA 레이어 형식(V5 기준, V6 판 있음, ref-747), KS F 1542(ref-748)와 건설CALS/EC 전자도면 작성표준(한국건설기술연구원 공고, ref-749)을 따로 기재(파생 관계 미확인), 실무 IFC 모델의 IfcBuildingElementProxy 오용 점검(Noardo 외 2021, ref-751), 국토교통부 건설산업 BIM 시행지침(2022-07, ref-755). |
| 27 | 8. 대표 연구와 자료 | 도면 해석 AI 방법으로 CAD 레이어·블록 계층을 이용한 자동 라벨링(ArchCAD-400K, ref-753), 텍스트 주석 유형·속성을 결합한 다중 모달 심볼 스포팅(arXiv 2607.12678, ref-752), YOLOv8·OFA-OCR 기반 래스터 축척 인식(ref-754)을 적용 대상 6. 지도·공간·위치 모델과 양쪽 연결. |
