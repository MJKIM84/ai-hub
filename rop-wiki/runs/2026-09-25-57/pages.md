# 스토리텔러 산출 2026-09-25-57

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/manual-capability-ontology/stage-2-document-types.md | draft | q2-01 답함, q2-02·q2-03 부분 답, 후속 질문 2건(q2-07·q6-07), 완료 조건 미충족·전환 아니오, 출처 14건, 이력 추가. H1 아래 단계 상태 줄을 고쳐야 해 patches 대신 전체 content 로 보냄 |
| update | docs/tracks/manual-capability-ontology/document-type-matrix.md | draft | 매트릭스 9/64칸 채움(페이로드·액세서리 문서 행 추가), 공개 문서 샘플 4건, 출처·이력 갱신. H1 아래 산출 단계 상태 줄을 고쳐야 해 전체 content 로 보냄 |
| update | docs/tracks/manual-capability-ontology/ontology-draft.md | draft | v0.3 → v0.4: 근거 문서 속성 '문서 유형'·'이용 조건' 추가와 확정(f3·f17), 속성 '정보 형태'는 6절 질문에 합침. H1 버전 표기를 고쳐야 해 전체 content 로 보냄 |
| update | docs/tracks/manual-capability-ontology/index.md | draft | 6. 살아있는 산출물 링크: 온톨로지 초안 v0.4, 문서 유형 매트릭스 초안(9/64칸·샘플 4건) 반영. 상태 줄은 입력 그대로(현재 단계 단계 1 유지) |
| update | docs/ideas/robot-capability-ontology.md | draft | 3절에 매뉴얼 대상 추출 연구, 4절에 제조사 문서 유형·공개 샘플·이용 조건 단락 추가(실행 2026-09-25-57) |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 매뉴얼 기반 로봇 기능 온톨로지 단계 2 | q2-01 답함, q2-02·q2-03 부분 답, 문서 유형 매트릭스 9/64칸·공개 문서 샘플 4건, 온톨로지 초안 v0.4, 후속 질문 2건 | run 2026-09-25-57
- 홈 최근 업데이트: 2026-09-25 — 매뉴얼 기반 로봇 기능 온톨로지 단계 2. 로봇 문서 유형과 정보 구조 조사: 제조사 문서 유형 질문 q2-01 답함, 문서 유형 매트릭스·공개 문서 샘플 4건 초안, 온톨로지 초안 v0.4
- 대분류 최근 업데이트: 2026-09-25 — 5. 로봇 능력·작업 온톨로지(트랙 단계 2): 제조사 문서 유형·정보 형태·공개 샘플 조사, 세부영역 반영 제안(6절)
- 세부영역 최근 업데이트: 2026-09-25 — 5. 로봇 능력·작업 온톨로지: 트랙 단계 2 실행이 능력 정보의 문서 유형·형태별 분산과 기계가독 스키마 사례를 6. 대표 접근법과 기술 절에 반영하도록 제안

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 사용 정보 | Information for Use (Instructions for Use) | 제조사가 제품 사용자에게 제공하는 설명 정보로, IEC/IEEE 82079-1:2019 가 모든 종류 제품의 사용 정보 작성 원칙과 요구사항을 정한다. | 5, 21 | ref-724, ref-723 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-719 | Boston Dynamics (boston-dynamics/spot-sdk GitHub) | spot-sdk — README | 벤더 문서 | medium | https://github.com/boston-dynamics/spot-sdk |
| ref-720 | Kinova (Kinovarobotics/kortex GitHub) | kortex — readme | 벤더 문서 | medium | https://github.com/Kinovarobotics/kortex |
| ref-721 | Doosan Robotics (doosan-robotics/doosan-robot2 GitHub) | doosan-robot2 — README (humble) | 벤더 문서 | medium | https://github.com/doosan-robotics/doosan-robot2 |
| ref-722 | Rainbow Robotics (RainbowRobotics/rbpodo GitHub) | rbpodo — README | 벤더 문서 | medium | https://github.com/RainbowRobotics/rbpodo |
| ref-723 | ISO | ISO 20607:2019 - Safety of machinery — Instruction handbook — General drafting principles | 표준 | medium | https://www.iso.org/standard/68519.html |
| ref-724 | IEC / IEEE / ISO | IEC/IEEE 82079-1:2019 - Preparation of information for use (instructions for use) of products — Part 1: Principles and general requirements | 표준 | medium | https://www.iso.org/standard/71620.html |
| ref-725 | 두산로보틱스 | 매뉴얼 : Doosan Robotics Training & Service | 벤더 문서 | low | https://robotlab.doosanrobotics.com/ko/board/Resources/Manual |
| ref-726 | Rainbow Robotics | Rainbow Robotics 협동로봇 기술자료 (rb_cobot_docs) | 벤더 문서 | low | https://rainbowrobotics.github.io/rb_cobot_docs/ko/ |
| ref-727 | OpenDataLab (opendatalab/OmniDocBench GitHub) | OmniDocBench — README | 오픈소스 문서 | high | https://github.com/opendatalab/OmniDocBench |
| ref-728 | Springer Nature (게재 장 저자 미확인) | Conversational Knowledge Extraction from Technical Manuals: An LLM-Based Framework with Ontological Guidance | 논문 | medium | https://link.springer.com/chapter/10.1007/978-3-032-19096-3_30 |
| ref-729 | Springer Nature (게재 장 저자 미확인) | Enhancing LLMs for Manufacturing Information Extraction | 논문 | medium | https://link.springer.com/chapter/10.1007/978-981-92-1468-6_21 |
| ref-040 | Open Robotics | PerformAction Tutorial - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | high | https://osrf.github.io/ros2multirobotbook/integration_fleets_action_tutorial.html |
| ref-228 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050 — json_schemas/factsheet.schema | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/json_schemas/factsheet.schema |
| ref-230 | MassRobotics | MassRobotics-AMR/AMR_Interop_Standard — AMR_Interop_Standard.json | 표준 | medium | https://github.com/MassRobotics-AMR/AMR_Interop_Standard/blob/main/AMR_Interop_Standard.json |

## 열린 질문 갱신

- 없음

## 흐름 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| ISO 20607:2019 기계 안전 — 설명서 일반 작성 원칙 | 표준 | ISO | 5, 21, 25 | ref-723 | https://www.iso.org/standard/68519.html |
| IEC/IEEE 82079-1:2019 제품 사용 정보 작성 — Part 1: 원칙과 일반 요구사항 | 표준 | IEC / IEEE / ISO | 5, 21 | ref-724 | https://www.iso.org/standard/71620.html |
| OmniDocBench (PDF 문서 파싱 벤치마크) | 오픈소스 | OpenDataLab | 27, 23 | ref-727 | https://github.com/opendatalab/OmniDocBench |

## 추가 조사 요청

- 단계 2 페이지 3절 q2-01·문서 유형 매트릭스: 사용자 매뉴얼, 오류 코드표, 치수도·도면 유형의 공개 샘플과 그 안의 기능 정보가 필요하다 — 이번 샘플에서 확인하지 못해 매트릭스 해당 행이 미조사로 남았다.
- q2-07·매트릭스 4절: AMR 제조사(MiR·OTTO·국내 물류로봇 업체)의 공개 매뉴얼·REST API 문서와 이용 조건 — AMR 샘플이 없어 완료 조건 미충족.
- q2-03·q6-07: 두산로보틱스 로봇랩·레인보우 rb_cobot_docs 등 포털 매뉴얼 문서의 이용 약관 원문 — 코드 라이선스와 별개인 문서 이용 조건이 미확인이다.
- q2-02 남은 부분: 로봇 매뉴얼의 형태별(문장·파라미터 표·그림·코드 예제) 추출 정확도를 측정한 공개 데이터셋·평가 방법(q3-01과 함께).
- ref-728·ref-729: 저자와 발행일 확인(현재 '게재 장 저자 미확인', 발행일 미확인).
- 리서치 담당: ref-040 의 출처 표시(fetched_via github_raw·fetch_url null)를 실제 경로(data/source_texts, inbox)로 바로잡을 것 — 1차 검증 노트의 지적.
- pipeline 담당: 트랙 단계 페이지·트랙 보조 페이지의 H1 아래 상태 줄과 온톨로지 초안 H1 의 버전 표기는 H2 절 밖에 있어 patches 로 고칠 수 없다. 이번 실행은 required_fixes 이행을 위해 이 세 페이지를 전체 content 로 보냈다. 절 밖 머리 영역 패치 지원 또는 이 경우의 예외 규정을 요청한다.
- 사용자 확인: 트랙 정의 current_stage 는 1 이고 단계 1 전환 승인 기록이 없는데 이번 실행은 CLI 지정으로 단계 2를 다뤘다. 트랙 개요의 현재 단계 표기와 단계 1 완료 판정 결정이 필요하다.

## 이행한 수정 지시

- f2 열거 삭제 — 단계 2 페이지 3절 q2-01·4절, 아이디어 페이지 4절에서 '조립·설치·운전·유지보수·폐기' 열거를 빼고 '모든 종류 제품의 사용 정보 작성 원칙·요구사항(2019 판, 2012 초판 대체)'으로만 썼고, 용어집 '사용 정보' 정의에서도 같은 열거를 뺐다.
- f7 축소 — 다운로드 페이지(도면·카탈로그·기술자료) 서술과 README 의 'API 참조' 링크 서술을 모두 빼고, 포트 5000·5001, C++17·Python, 개요·예제 문서 링크만 [추정] 벤더 주장으로 썼으며 rb_cobot_docs 는 '협동로봇 기술자료 공개 페이지(원문 미열람)'로만 언급했다.
- f8 분리 — 팩트시트 필수 블록 구성은 [사실][^ref-228]로, '사양서·데이터시트 정보의 표준화된 대응물'은 이 위키의 해석으로 밝힌 별도 문장 [추정]으로 썼고, ref-228 각주는 참고문헌 목록의 기존 줄을 그대로 썼다(매트릭스 사양서·데이터시트 행도 '표준 대응물' [추정]).
- f9·f13·f16 — 단계 2 페이지에서 각 문장에 '이 위키의 종합(추론)이며 측정 근거 없음'을 밝히고 [추정]을 유지했으며, f16 순서는 '측정 결과로 읽지 않는다'고 명시했다.
- q2-01 답함(신뢰도는 페이지 confidence low) — 3절 답과 매트릭스에서 사용자 매뉴얼·오류 코드표·치수도·도면 행을 미조사로 남기고 3절에 '이번 샘플에서 확인하지 못했다'를 명시했다.
- 벤더 문서 근거 finding — 단계 2 페이지·매트릭스·아이디어 페이지·반영 제안에서 f3·f4·f5·f6·f7·f11·f17·f18·f19 문장에 '[추정] 벤더 주장'을 병기하고 문서 구조·정보 형태·이용 조건 사례로만 인용했으며, 매트릭스 칸마다 샘플 이름을 병기했다.
- f4 경계 — Kortex 저수준 제어(서보 모드) 문서는 문서 유형 사례로만 보고 분류 원문 9장 '로봇 자체 지능·제어' 연계 대상으로 표시했다(단계 2 페이지 q2-01, [의견]). Gen3 lite 는 펌웨어 2.3.4·API 2.3.0 으로 구분해 적었다.
- f20 — 'MiR 저장소 경로 404'를 어디에도 쓰지 않고 'AMR 제조사의 공개 매뉴얼 샘플은 이번 조사에서 찾지 못했다(부재 확정 아님)'로만 [추정] 서술했다.
- 원문 미열람 표시 — ref-723·724·725·726·728·729·230 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었다. ref-040·ref-228 은 기존 각주 줄을 그대로, ref-230 은 기존 줄에 미열람 표시를 더해 썼다.
- ref-728·ref-729 — 각주 발행일 자리를 '미확인', 기관 자리를 'Springer Nature (게재 장 저자 미확인)'으로 적었다.
- 온톨로지 변경 — 근거 문서에 속성 '문서 유형'·'이용 조건'만 더하고(f3·f17[^ref-719]) 상태를 초안→확정으로 바꿨으며 ontology_version 을 0.4 로 올렸다(프런트매터·H1 '(v0.4)'·도식 제목·JSON ontology_draft_version). 상태 줄은 auto:page-status 마커 안이라 퍼블리셔가 프런트매터 값으로 다시 채우므로 마커 안은 손대지 않았다. '정보 형태'는 반영하지 않고 6절 '근거 문서의 단위와 버전' 질문에 합쳤다.
- 중복 새 질문 — '형태별 추출 정확도 측정 데이터셋·평가 방법'은 backlog_updates 에 넣지 않고 단계 2 페이지 3절 q2-02 의 남은 부분(q3-01 과 함께)과 5절 표 아래 문장으로 적었다.
- q2-02·q2-03 — backlog_updates 에 status '조사 중', answer_link null 로 냈고 단계 2 페이지 2절 표에서는 '열림', 답한 실행 id·답 위치를 비웠다.
- 단계 2 페이지 6절 — 두 완료 조건 모두 '미충족', 검증 판정 '미충족 · 미승인', 표 아래 '다음 단계로 전환: 아니오(q2-02·q2-03 부분 답, q2-04·q2-05·q2-06 열림, 매트릭스 미조사 칸)', 상태 줄 '단계 상태: 진행 중 · … · 완료 조건: 미충족'으로 썼고 track_updates.stage_transition 을 넣지 않았다.
- 트랙 개요 상태 줄 — 입력 줄이 이미 '현재 단계: 단계 1. 기존 능력 표현 모델과 표준 조사 · 마지막 트랙 실행: 2026-09-25'이므로 그대로 두었다(개요 페이지는 6절만 patch).
- 세부영역 반영 제안 — 5. 로봇 능력·작업 온톨로지 6절, 21. 온보딩·설정·현장 시운전 6절, 27. AI·학습·적응과 모델 운영 6·8절 제안을 area_reflection_proposals 와 트랙 로그에만 남기고 세부영역 페이지는 고치지 않았으며, 27 제안에 교차 규칙(매뉴얼 해석은 5·21 에 적용)과 양쪽 연결을 밝혔다.
- docs/ideas/robot-capability-ontology.md: 각주 정의 10개를 참고문헌에서 만들어 붙임: ref-719, ref-720, ref-721, ref-722, ref-723, ref-724, ref-725, ref-727, ref-728, ref-729

## 트랙 갱신

- 단계 페이지: docs/tracks/manual-capability-ontology/stage-2-document-types.md
- 온톨로지 초안 버전: 0.4
- 트랙 로그 항목: 답한 질문: q2-01(사용자 매뉴얼·오류 코드표·치수도·도면 유형은 이번 샘플에서 미확인) / 부분 답: q2-02(형태별 추출 정확도 측정 자료 없음), q2-03(AMR 공개 매뉴얼 샘플·포털 매뉴얼 이용 약관 미확인) / 새 질문: q2-07(f20, 단계 2. 로봇 문서 유형과 정보 구조 조사), q6-07(f19, 단계 6. 변경 관리·운영·거버넌스 조사). 중복 1건(형태별 추출 정확도 측정 → q2-02·q3-01)은 등록하지 않음 / 온톨로지 변경: v0.3 → v0.4: 개념 '근거 문서' 속성 '문서 유형'·'이용 조건' 추가와 상태 초안→확정(f3·f17), 근거 실행 2026-09-25-57. 속성 '정보 형태'는 거부(f16 측정 없는 추론, 문서 안 위치 단위 속성일 수 있음) — 6절 '근거 문서의 단위와 버전' 질문에 합침 / 완료 조건 평가: 미충족(부족: 문서 유형 매트릭스 9/64칸만 채움, 사용자 매뉴얼·오류 코드표·치수도·도면 행 미조사, 공개 문서 샘플 목록에 AMR 샘플·매뉴얼 이용 조건 없음). 단계 전환 미승인 / 세부영역 반영 제안: 5. 로봇 능력·작업 온톨로지(6절), 21. 온보딩·설정·현장 시운전(6절), 27. AI·학습·적응과 모델 운영(6·8절) 4건 / 다음 실행 제안: q2-04, q2-05, q2-06, q2-07 과 q2-02·q2-03 남은 부분. 참고: 트랙 정의 current_stage 는 1 이고 단계 1 전환 승인 기록이 없는데 이번 실행은 CLI 지정으로 단계 2를 다뤘다 — 트랙 개요 현재 단계 표기와 단계 1 완료 판정은 사용자 확인 필요
- 개요 진행 현황: 단계 2 진행 중 — 열린 질문 6, 답함 1, 완료 조건 미충족(트랙 개요의 현재 단계 표기는 단계 1 유지, 단계 1 전환 승인 기록 없음 — 사용자 확인 필요)

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q2-01 | 답함 | docs/tracks/manual-capability-ontology/stage-2-document-types.md#q2-01 | — | — | — |
| q2-02 | 조사 중 | — | — | — | — |
| q2-03 | 조사 중 | — | — | — | — |
| q2-07 | 열림 | — | AMR 제조사(MiR·OTTO·국내 물류로봇 업체 등)가 공개하는 매뉴얼·REST API 문서는 무엇이며, 공개되지 않을 때 표준 스키마(VDA 5050 팩트시트·MassRobotics)로 대신할 수 있는 정보와 없는 정보는 무엇인가? (q2-03 에서 파생) | 2 | f20 |
| q6-07 | 열림 | — | SDK 코드 라이선스와 별개로 제조사 매뉴얼 문서를 자동 추출·재가공해 능력 온톨로지에 쓰는 것이 이용 조건상 허용되는가, 이를 누가 확인하고 기록하는가? (q2-03 에서 파생) | 6 | f19 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 5 | 6. 대표 접근법과 기술 | 능력 정보는 제조사 문서 유형(통합·API 가이드, 설치·안전 매뉴얼, 릴리스 노트, 페이로드·액세서리 문서, 사양서·데이터시트)과 형태(문장·코드 예제·설정 파일·기계가독 스키마)별로 흩어져 있는 것으로 보이며, 이 대응과 형태별 추출 용이성 순서는 측정 근거 없는 이 위키의 종합이다([추정], f9·f16). 기계가독 형태의 사례로 VDA 5050 팩트시트 필수 블록([사실], ref-228)과 Open-RMF config.yaml actions·JSON 요청·코드 예제([사실], ref-040)를 든다. 제조사 문서 근거는 [추정] 벤더 주장. |
| 21 | 6. 대표 접근법과 기술 | 온보딩 때 모을 제조사 문서 유형과 공개 경로·이용 조건: 두산로보틱스 로봇랩 설치·기타 매뉴얼과 doosan-robot2(Apache 2.0·BSD 3-Clause), 레인보우로보틱스 rbpodo(Apache 2.0)·rb_cobot_docs(원문 미열람) — 모두 [추정] 벤더 주장. 포털 매뉴얼 문서 이용 조건은 미확인이고, AMR 제조사 공개 매뉴얼 샘플은 이번 조사에서 찾지 못했다(부재 확정 아님, f5·f7·f19·f20). |
| 27 | 6. 대표 접근법과 기술 | 분류 원문 8장 교차 규칙에 따라 매뉴얼 해석은 이 영역의 방법이 5. 로봇 능력·작업 온톨로지와 21. 온보딩·설정·현장 시운전에 적용되는 것이다. 매뉴얼 대상 LLM 추출 방법으로 온톨로지 제약 RAG 기반 개체·관계 추출과 대화형 절차 안내를 결합한 프레임워크(ref-728, 원문 미열람)와 제조 문서 항목–속성–값 삼중항 추출 벤치마크 ManuExtract(ref-729, 원문 미열람)를 든다(f14·f15). 적용 대상 영역 페이지 양쪽에 연결한다. |
| 27 | 8. 대표 연구와 자료 | 범용 문서 파싱 벤치마크 OmniDocBench(1,651 PDF 페이지, 텍스트·표·수식·읽기 순서 평가, 문서 유형에 매뉴얼 없음, ref-727)와 매뉴얼 대상 추출 연구 두 건(ref-728·ref-729)을 자료로 추가한다. 로봇 매뉴얼 형태별 추출 난이도를 측정한 공개 자료는 이번 조사에서 찾지 못했다(부재 확정 아님, f12·f13). 교차 규칙에 따라 5. 로봇 능력·작업 온톨로지와 21. 온보딩·설정·현장 시운전에도 연결한다. |
