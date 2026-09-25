# 스토리텔러 산출 2026-09-25-22

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/floorplan-recognition/stage-1-prior-work-and-products.md | draft | q1-04 답함(3절 소제목 신설), 후속 질문 q1-08·q5-04 등록, 4·6·7·8·9절 갱신. 초안 변경 없음. 2차: f1 문장을 '검색 요약에는 소요 시간 수치가 없다(원문 미열람)'로 수정 |
| update | docs/ideas/floorplan-recognition.md | draft | 3절에 현장 모델링 부담의 근거 소절 추가, 6절에 단계 5 조사 전 선행 근거(가설 3 비교 기준 후보·측정 대상 반복 작업) 작성. 2차: 6절 마지막 문장에 '연계 대상: '과 [추정] 태그·각주 추가 |
| update | docs/tracks/floorplan-recognition/index.md | draft | 6. 살아있는 산출물 링크의 백로그·아이디어 페이지 현황을 실행 2026-09-25-22 기준으로 갱신(상태 줄은 변경 없음) |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 건축 도면 자동 인식 단계 1 | q1-04 답함(현장 모델링 시간·반복 작업 자료 유형과 반복 작업 목록 정리), 후속 질문 q1-08·q5-04 등록, 아이디어 3 6절 선행 근거 작성, 초안 변경 없음 | run 2026-09-25-22
- 홈 최근 업데이트: 2026-09-25 — 건축 도면 자동 인식 단계 1: q1-04 답함 — 새 현장 지도 작성·공용 자원 등록 시간은 정성 연구·과제 보고값·벤더 주장·도구 문서로만 확인되고 독립 시간 측정 자료는 찾지 못함
- 대분류 최근 업데이트: 2026-09-25 — 건축 도면 자동 인식 단계 1(중심 6. 지도·공간·위치 모델): q1-04 답함, 반복 작업 목록(지도 작성 주행·위치 지정·경로망 설계·좌표 대응·레이아웃 재입력) 정리, 세부영역 반영 제안 7건
- 세부영역 최근 업데이트: 2026-09-25 — 건축 도면 자동 인식 단계 1: 3. 왜 중요한가(지도 작성의 시간 병목)와 9절(SLAM 지도 작성은 연계 대상, 좌표 정렬·레이아웃 전달은 ROP 쪽) 반영 제안

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 경로망 | Roadmap | 다중 AGV·이동로봇이 따라 달릴 수 있는 노드와 엣지의 주행 경로 그래프로, 현장 도입 때 전문가가 설계하거나 자동 생성한다. | 15, 21, 6 | ref-217, ref-320, ref-321 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-318 | European Commission (CORDIS) | PAN-ROBOTS: Automating logistics for the factory of the future | 정부·연구기관 | medium | https://cordis.europa.eu/article/id/160857-panrobots-automating-logistics-for-the-factory-of-the-future |
| ref-319 | Beinschob, P., & Reinke, C. | Graph SLAM based mapping for AGV localization in large-scale warehouses | 논문 | medium | https://ieeexplore.ieee.org/document/7312637/ |
| ref-320 | IEEE 게재 논문 저자(미확인) | Simulation-Based Approach for Automatic Roadmap Design in Multi-AGV Systems (IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)) | 논문 | medium | https://ieeexplore.ieee.org/document/10287275/ |
| ref-321 | Rüdt, M., Enke, C., & Furmans, K. (KIT) | Automated Generation of Continuous-Space Roadmaps for Routing Mobile Robot Fleets (v2 제목: Continuous-Space Roadmap Generation for Mobile Robot Fleets with Distance Constraints and Geometry-Aware Discretization) | 논문 | medium | https://arxiv.org/abs/2511.07175 |
| ref-322 | Heselden, J. R., & Das, G. P. | Unified Map Handling for Robotic Systems: Enhancing Interoperability and Efficiency Across Diverse Environments | 논문 | medium | https://arxiv.org/abs/2404.13499 |
| ref-323 | Macenski, S. (SteveMacenski GitHub) | slam_toolbox — README (Slam Toolbox for lifelong mapping and localization in potentially massive maps with ROS) | 오픈소스 문서 | medium | https://github.com/SteveMacenski/slam_toolbox |
| ref-324 | OTTO Motors (Rockwell Automation) | Maximize AMR productivity and simplify commissioning with our latest software release | 벤더 문서 | low | https://ottomotors.com/blog/amr-productivity-software-release/ |
| ref-326 | Mobile Industrial Robots(MiR) (ManualsLib 게재본) | MiR250 User Manual — Creating and configuring a map (page 104, 제조사 공식 사이트가 아닌 매뉴얼 게재 사이트 사본) | 벤더 문서 | low | https://www.manualslib.com/manual/1941073/Mir-Mir250.html?page=104 |
| ref-327 | ScaliRo | LIF – Layout Interchange Format Explained | 벤더 문서 | low | https://scaliro.de/en/lif/ |

## 열린 질문 갱신

- 없음

## 흐름 매트릭스 갱신

- 없음

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| SLAM Toolbox | 오픈소스 | Macenski, S. (SteveMacenski GitHub) | 6, 21 | ref-323 | https://github.com/SteveMacenski/slam_toolbox |

## 추가 조사 요청

- 단계 1 페이지 H1 아래 단계 상태 줄(답한 질문 3건 → 4건, 열린 질문 3건 유지)은 H2 밖이라 patches 로 고칠 수 없다. 퍼블리셔가 백로그 수치로 갱신하거나 다음 전체 재작성 실행에서 고치도록 pipeline 담당에게 요청한다.
- q5-04: PAN-Robots 설치 기간 6개월→2개월의 비교 조건(대상 공장 규모·기준 시스템·단계별 소요 시간)을 과제 최종 보고서로 확인해야 아이디어 3 6절의 비교 기준으로 쓸 수 있다.
- q1-08: 국내 물류센터의 지도 작성·공용 자원 등록·좌표 정렬 소요 시간을 단계별로 공개한 공공·학술 자료가 21. 온보딩·설정·현장 시운전 3절과 단계 1 완료에 필요하다.
- ref-320 저자 목록과 ref-318 CORDIS 원 게재일이 미확인이다.
- Beinschob 외(2017, ref-217) 원문을 열어 소요 시간 수치 제시 여부를 확인해야 한다(현재는 검색 요약에 수치가 없다는 것만 확인).

## 이행한 수정 지시

- f10 삭제 — BlueBotics 문장을 단계 페이지·아이디어 페이지·반영 제안 어디에도 넣지 않았고 ref-325 를 각주·프런트매터 sources·reference_updates 에서 뺐다.
- f16·f18 ref-163 재사용 — 두 주장 모두 기존 ref-163 각주(참고문헌 줄 그대로)를 쓰고 중복 출처는 만들지 않았다.
- f2 강등 — 단계 페이지 3절·아이디어 3·6절에서 [추정]으로 쓰고 '과제 측 보고값, 비교 조건·측정 방법 미확인'과 기준일 '2015-04(재게재 기사 기준, CORDIS 원 게재일 미확인)'을 문장에 넣었다.
- f4 비교 절 삭제 — 연결성·중복성 비교 문장을 빼고 개미 군집 최적화 경로망 생성·SIPP 기반 MAPF 시뮬레이터 평가·처리량 기반 플릿 규모 제안만 [추정]으로 썼으며, ref-320 발행 정보를 'IEEE Transactions on Automation Science and Engineering 21(4), 2024 (2023 온라인 공개)'로 고쳤다.
- f5 서지 정정 — ref-321 기관을 'Rüdt, M., Enke, C., & Furmans, K. (KIT)'로 고치고 각주 제목에 v2 제목을 병기했다.
- f12 분리 — 경유점 속성 사람 입력은 q1-03 을 짧게 참조한 [사실] 문장, 현장마다 반복된다는 절은 별도 [추정] 문장으로 쓰고 기존 ref-079 각주를 재사용했다.
- f13 분리 — 플릿별 설정 항목은 [사실], 플릿을 더할 때마다 반복된다는 절은 별도 [추정] 문장으로 썼다.
- f15 오류 절 삭제 — 좌표 오기·스테이션 누락·충돌 절을 빼고 '프로젝트당 수 인일' 부분만 [추정] 벤더 주장으로 남겼다.
- f7 병기 — '프로젝트 문서의 자체 벤치마크 보고값(독립 측정 아님)'을 문장에 넣고 같은 소절에 SLAM 은 연계 대상임을 밝혔으며, f16 의 자율 탐사 SLAM·엘리베이터 버튼 조작도 연계 대상으로 짧게 적었다.
- f9 병기 — [추정] 뒤에 '벤더 주장'을 붙이고 제조사 공식 사이트가 아닌 매뉴얼 게재 사이트 사본임을 문장과 각주에 밝혔다.
- f11 병기 — [추정] 벤더 주장에 '내부 시험, 측정 조건 미공개'를 붙이고 ref-324 발행일을 2023(소프트웨어 2.28 판 발표 기준)으로 적었다.
- 원문 미열람 표시 — ref-318·ref-319·ref-320·ref-321·ref-322·ref-324·ref-326·ref-327 각주 접근일 뒤에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었으며, ref-079·ref-046·ref-217 은 기존 정의를 재사용하고 ref-105·ref-163 은 참고문헌 페이지 줄 그대로 옮겼다.
- 용어 — '지도 정합'은 glossary_updates 에 넣지 않았고 '경로망(Roadmap)'만 신규로 냈다.
- 아이디어 6절 — '단계 5 조사 전 선행 근거'를 먼저 밝히고 PAN-Robots 비교를 [추정] 과제 측 보고값으로, 독립 측정 연구 부재를 검색 범위 기준(부재 확인 아님)으로 적고, 벤더 수치(OTTO·ScaliRo)는 가설 3 판정 근거로 쓰지 않는다고 명시했다.
- 세부영역 반영 제안 — 21. 온보딩·설정·현장 시운전, 15. 다중 로봇 경로·교통 관리 — MAPF, 6. 지도·공간·위치 모델 페이지를 직접 고치지 않고 area_reflection_proposals 로만 냈으며 f10 을 빼고 f4 는 비교 절을 뺀 내용만 넣었다.
- 단계 1 페이지 6절 — 두 완료 조건을 '충족', 검증 판정을 '충족 · 미승인'으로 두고 '다음 단계로 전환: 아니오(막힌 질문 q1-05·q1-06 과 이번에 등록할 국내 소요 시간 질문 q1-08)'로 썼으며 단계 상태는 '진행 중'을 유지했다.
- 2차: 단계 1 페이지 3절 q1-04 「설치 병목을 정성적으로 기술한 연구」 첫 문단의 '소요 시간 수치는 제시하지 않았다.'를 '검색 요약에는 소요 시간 수치가 없다(원문 미열람).'로 고쳤다.
- 2차: 아이디어 페이지 6절 「측정 대상 후보: 반복 작업 목록」 마지막 문장 앞에 '연계 대상: '을 두고 끝에 [추정][^ref-105][^ref-046]을 붙였다(두 각주 정의는 같은 절에 있음).
- 2차: area_reflection_proposals 의 21. 온보딩·설정·현장 시운전 '6. 대표 접근법과 기술' 요약에서 '[추정](…)'·'[사실](…)' 표기를 '[추정], ref-217·ref-079·ref-105·ref-046'·'[사실], ref-105' 형식으로 고쳤고, 벤더 주장 표기도 '[추정] 벤더 주장, ref-324' 로 맞췄다.

## 트랙 갱신

- 단계 페이지: docs/tracks/floorplan-recognition/stage-1-prior-work-and-products.md
- 온톨로지 초안 버전: 0.3
- 트랙 로그 항목: 답한 질문: q1-04(현장 모델링 시간·반복 작업은 정성 연구·과제 측 보고값·벤더 주장·도구·형식 문서로만 확인, 독립 시간 측정 자료는 검색 범위에서 찾지 못함 — f1·f2·f3·f4·f5·f6·f7·f8·f9·f11·f12·f13·f14·f15·f16·f17·f18·f19, f10 삭제) / 새 질문: q1-08(국내 소요 시간 자료, f17), q5-04(PAN-Robots 비교 조건, f2) / 온톨로지 변경: 없음(v0.3 유지 — q1-04 는 시간·작업 부담 자료 질문이라 개념·관계 근거 없음) / 완료 조건 평가: 충족(검증 판정 충족, 단계 전환 미승인 — 막힌 질문 q1-05·q1-06·q1-08) / 세부영역 반영 제안: 21. 온보딩·설정·현장 시운전 3건, 15. 다중 로봇 경로·교통 관리 — MAPF 2건, 6. 지도·공간·위치 모델 2건 / 다음 실행 제안: q1-05 또는 q1-06, 이어서 q1-08 / 비고: 단계 페이지 상태 줄(답한 질문 4건)은 패치 범위 밖이라 미갱신
- 개요 진행 현황: 단계 1 진행 중 — 열린 질문 3, 답함 4, 완료 조건 충족(검증 판정 충족, 단계 전환 미승인: 막힌 질문 q1-05·q1-06·q1-08)

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q1-04 | 답함 | docs/tracks/floorplan-recognition/stage-1-prior-work-and-products.md#q1-04 | — | — | — |
| q1-08 | 열림 | — | 국내 물류센터에서 로봇 도입 시 지도 작성·충전소 등 공용 자원 등록·제조사별 좌표 정렬에 든 시간을 단계별로 공개한 공공·학술 자료나 사례가 있는가? (q1-04 에서 파생) | 1 | f17 |
| q5-04 | 열림 | — | PAN-Robots 과제가 보고한 설치 기간 6개월→2개월의 비교 조건(대상 공장 규모, 기준 시스템, 단계별 소요 시간)을 과제 결과 보고서·산출물로 확인해, 도면 기반 자동 생성의 시간 단축 효과를 판정할 기준 자료로 쓸 수 있는가? (q1-04 에서 파생) | 5 | f2 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 21 | 3. 왜 중요한가 | 새 현장 AGV·이동로봇 도입의 긴 설치 시간 원인으로 정밀 2D 지도 작성, 픽업·하역 위치 지정, 전문가 수작업 경로망 설계가 꼽힌다(Beinschob 외 2017 [사실], ref-217). 지도 작성은 새 환경 배치의 시간이 많이 드는 과정이다(Heselden·Das 2024 [사실], ref-322). PAN-Robots 설치 기간 6개월→2개월은 과제 측 보고값(비교 조건 미확인, [추정], ref-318). |
| 21 | 6. 대표 접근법과 기술 | 새 현장·새 제조사마다 반복되는 작업(지도 작성 주행, 위치 지정, 경로망 설계, 좌표 대응, 형식별 레이아웃 재입력)의 정리: [추정], ref-217·ref-079·ref-105·ref-046. Open-RMF 플릿 어댑터 설정의 층별 좌표 대응점·사양·작업 능력 항목: [사실], ref-105. OTTO 설정 복제·부분 재지도화: [추정] 벤더 주장, ref-324. |
| 21 | 8. 대표 연구와 자료 | Beinschob 외(2017, ref-217), Beinschob·Reinke(2015, ref-319), 다중 AGV 경로망 자동 설계 연구(IEEE T-ASE 2024, ref-320, 비교 절 제외), Rüdt 외(2025, ref-321), Heselden·Das(2024, ref-322), PAN-Robots CORDIS 기사(ref-318, [추정]). |
| 15 | 6. 대표 접근법과 기술 | 경로망은 보통 전문가가 수작업으로 설계해 시간이 많이 들고 최적이 아닐 수 있으며, 개미 군집 최적화 기반 생성과 SIPP 기반 MAPF 시뮬레이터 평가([추정], ref-320), 스테이션 상호작용 지점과 운송 수요를 반영한 연속 공간 경로망 자동 생성([사실], ref-321)이 제안됐다. |
| 15 | 8. 대표 연구와 자료 | IEEE Transactions on Automation Science and Engineering 21(4) 2024 경로망 자동 설계 연구(ref-320, 저자 미확인), Rüdt·Enke·Furmans(KIT, arXiv 2511.07175, ref-321). |
| 6 | 3. 왜 중요한가 | 지도 작성은 새 환경 배치의 시간 병목이며([사실], ref-322), SLAM 계산 자체는 실시간보다 빠르다는 프로젝트 자체 보고(ref-323)와 함께 보면 시간의 큰 부분은 데이터 수집 주행과 사람의 주석·설계에서 나오는 것으로 보인다([추정]). |
| 6 | 9. ROP가 직접 맡는 것과 외부와 연계하는 것 (부록 A 9장 기준) | 연계 대상: SLAM 지도 작성 주행과 로봇 쪽 위치추정 지도 생성(ref-323, ref-326). ROP 쪽: 플릿별 좌표 대응점 설정(ref-105), 레이아웃 전달·버전 관리(ref-046), 공용 자원 등록([추정]). |
