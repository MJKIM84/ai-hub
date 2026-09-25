# 스토리텔러 산출 2026-09-25-80

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/tracks/floorplan-recognition/stage-5-verification-and-hypotheses.md | draft | q5-01 답함(3절 신설), 2절에 q5-04~q5-10 행 추가, 4·5·6·8·9절 갱신, 상태 줄 갱신(seed 페이지 전체를 content 로 보냄). 2차 수정: 6절 첫 완료 조건을 한 행·미충족으로 되돌림, 4절 결론의 '클래스별' 삭제 |
| update | docs/ideas/floorplan-recognition.md | draft | 6절 전체 교체: 도입 단락을 소절 출처(q1-04 선행 근거, q5-01 답)에 맞게 고치고 '평가 지표 (q5-01)' 소절(세 층 지표·운영 허용치 변환·경로 차이 정의·ROP 경계, 추정 중심)을 더함, 근거 공백 문장에 태그·각주 추가 |
| update | docs/tracks/floorplan-recognition/index.md | draft | 6절에 실행 2026-09-25-80(단계 5, q5-01) 산출물 요약 단락 추가 |

## 변경 이력·색인

- 변경 이력: 2026-09-25 | 건축 도면 자동 인식 단계 5 | q5-01 답함(요소 인식·구조·그래프·지도·정렬과 주행 세 층 평가 지표, 추정 종합), 후속 질문 2건, 1차 조건부 승인 수정 12건·2차 수정 4건 이행 | run 2026-09-25-80
- 홈 최근 업데이트: 2026-09-25 — 건축 도면 자동 인식 단계 5: q5-01 답함 — 도면 인식·지도 품질을 요소 인식·구조·그래프·지도·정렬 세 층으로 재는 지표 구성(추정)과 주행 시험 표준(연계 대상) 정리
- 대분류 최근 업데이트: 2026-09-25 — 6. 지도·공간·위치 모델(건축 도면 자동 인식 트랙 단계 5): 도면 기반 지도의 품질 지표와 목적지 잔차를 노드 허용 편차로 판정하는 방법(추정) 정리, 세부영역 반영 제안
- 세부영역 최근 업데이트: 2026-09-25 — 6. 지도·공간·위치 모델: 트랙 건축 도면 자동 인식 단계 5(q5-01)에서 지도 품질 지표(SLABIM 정답 자세, CAD 지도 위치추정 오차, 상대 지표의 한계)를 확인해 6·8절 반영을 제안

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 경로 길이 가중 성공률 | Success weighted by Path Length (SPL) | 내비게이션 에피소드마다 성공 여부에 최단 경로 길이를 실제 경로 길이(최단보다 짧으면 최단)로 나눈 비율을 곱해 평균한 지표로, 도착 여부와 경로 효율을 함께 잰다. | 23, 6 | ref-750 |
| new | 파놉틱 품질 | Panoptic Quality (PQ) | 매칭된 인스턴스의 평균 IoU(분할 품질)와 TP/(TP+0.5FP+0.5FN)(인식 품질)의 곱으로, 요소를 맞게 찾았는지와 모양을 정확히 잡았는지를 함께 재는 지표다. | 27, 6 | ref-067 |
| new | 그래프 편집 거리 | Graph Edit Distance (GED) | 한 그래프를 다른 그래프로 바꾸는 노드·엣지 추가·삭제·치환의 최소 비용으로, 평면도 방 연결 그래프의 구조 차이를 재는 데 쓴다. | 6, 27, 23 | ref-745 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-743 | Chen, J., Liu, C., Wu, J., & Furukawa, Y. | Floor-SP: Inverse CAD for Floorplans by Sequential Room-wise Shortest Path | 논문 | medium | https://arxiv.org/abs/1908.06702 |
| ref-744 | Stekovic, S., Rad, M., Fraundorfer, F., & Lepetit, V. | MonteFloor: Extending MCTS for Reconstructing Accurate Large-Scale Floor Plans | 논문 | medium | https://arxiv.org/abs/2103.11161 |
| ref-745 | van Engelenburg, C. 외 (caspervanengelenburg GitHub) | ssig — README (SSIG: A Visually-Guided Graph Edit Distance for Floor Plan Similarity, ICCVW 2023) | 오픈소스 문서 | medium | https://github.com/caspervanengelenburg/ssig |
| ref-746 | ISO | ISO 18646-2:2024 - Robotics — Performance criteria and related test methods for service robots — Part 2: Navigation | 표준 | medium | https://www.iso.org/standard/82643.html |
| ref-747 | KISTI ScienceON(정부 R&D 보고서) | 이동/조작/HRI/통신성능 등 서비스로봇 성능평가 및 표준화 기술개발 | 정부·연구기관 | medium | https://scienceon.kisti.re.kr/srch/selectPORSrchReport.do?cn=TRKO201800040065 |
| ref-748 | ASTM International | F3244 Standard Test Method for Navigation: Defined Area | 표준 | medium | https://store.astm.org/f3244-21.html |
| ref-749 | Bostelman, R. V., Hong, T. H., & Cheok, G. S. (NIST) | Navigation Performance Evaluation for Automated Guided Vehicles | 정부·연구기관 | medium | https://www.nist.gov/publications/navigation-performance-evaluation-automated-guided-vehicles |
| ref-750 | Anderson, P. 외 | On Evaluation of Embodied Navigation Agents | 논문 | medium | https://arxiv.org/abs/1807.06757 |
| ref-751 | Kästner, L. 외 | Arena-Bench: A Benchmarking Suite for Obstacle Avoidance Approaches in Highly Dynamic Environments | 논문 | medium | https://arxiv.org/abs/2206.05728 |
| ref-752 | Filatov, A. 외 | 2D SLAM Quality Evaluation Methods | 논문 | medium | https://arxiv.org/abs/1708.02354 |
| ref-753 | Francis, A. 외 | Long-Range Indoor Navigation with PRM-RL | 논문 | medium | https://arxiv.org/abs/1902.09458 |
| ref-754 | HKUST Aerial Robotics Group (HKUST-Aerial-Robotics GitHub) | SLABIM — README (SLABIM: A SLAM-BIM Coupled Dataset in HKUST Main Building) | 오픈소스 문서 | medium | https://github.com/HKUST-Aerial-Robotics/SLABIM |
| ref-063 | Kalervo, A., Ylioinas, J., Häikiö, M., Karhu, A., & Kannala, J. | CubiCasa5K: A Dataset and an Improved Multi-Task Model for Floorplan Image Analysis | 논문 | medium | https://arxiv.org/abs/1904.01920 |
| ref-067 | Fan, Z., Zhu, L., Li, H., Chen, X., Zhu, S., & Tan, P. | FloorPlanCAD: A Large-Scale CAD Drawing Dataset for Panoptic Symbol Spotting | 논문 | medium | https://arxiv.org/abs/2105.07147 |
| ref-070 | Hu, S. 외 | Raster-to-Graph — README (Raster-to-Graph: Floorplan Recognition via Autoregressive Graph Prediction with an Attention Transformer) | 오픈소스 문서 | medium | https://github.com/SizheHu/Raster-to-Graph |
| ref-065 | Liu, C., Wu, J., Kohli, P., & Furukawa, Y. | FloorplanTransformation — README (Raster-to-Vector: Revisiting Floorplan Transformation) | 오픈소스 문서 | medium | https://github.com/art-programmer/FloorplanTransformation |
| ref-628 | Lee, H.-C., Woo, H.-M., & Shin, S. (International Journal of Precision Engineering and Manufacturing) | Digital Twin-based Sensor-Free Virtual Mapping for Autonomous Mobile Robot Localization | 논문 | medium | https://link.springer.com/article/10.1007/s12541-026-01598-2 |
| ref-031 | VDA / VDMA (VDA5050 GitHub) | VDA5050/VDA5050_EN.md — Official Specification document for the VDA 5050 | 표준 | medium | https://github.com/VDA5050/VDA5050/blob/main/VDA5050_EN.md |
| ref-153 | Open Robotics | Fleet Adapter Tutorial - Programming Multiple Robots with ROS 2 | 오픈소스 문서 | medium | https://osrf.github.io/ros2multirobotbook/integration_fleets_adapter_tutorial.html |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | ISO 18646-2:2024 의 지도 작성 정확도 시험은 무엇을 어떤 기준점과 절차로 측정하며, KS 로 부합화되어 국내 물류 로봇 시험에 쓰이는가? | 23, 6 | 열림 | — |

## 흐름 매트릭스 갱신

| 단계 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 출하 | 제약 | docs/tracks/floorplan-recognition/stage-5-verification-and-hypotheses.md#q5-01 | 단계 5. 검증 방법과 가설 판정 |
| 출하 | 완료·인계 | docs/tracks/floorplan-recognition/stage-5-verification-and-hypotheses.md#q5-01 | 단계 5. 검증 방법과 가설 판정 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| ISO 18646-2:2024 서비스 로봇 성능 기준과 시험 방법 — Part 2: 주행 | 표준 | ISO | 23, 6 | ref-746 | https://www.iso.org/standard/82643.html |
| ASTM F3244 Standard Test Method for Navigation: Defined Area | 표준 | ASTM International | 23 | ref-748 | https://store.astm.org/f3244-21.html |
| SSIG (평면도 구조 유사도 지표) | 오픈소스 | van Engelenburg, C. 외 (caspervanengelenburg GitHub) | 6, 27, 23 | ref-745 | https://github.com/caspervanengelenburg/ssig |
| SLABIM (SLAM–BIM 결합 데이터셋) | 오픈소스 | HKUST Aerial Robotics Group | 6, 23 | ref-754 | https://github.com/HKUST-Aerial-Robotics/SLABIM |

## 추가 조사 요청

- 단계 5 페이지 3절·4절: ISO 18646-2:2024 의 지도 작성 정확도·경로 이탈 시험 절차(기준점, 측정 방법)와 KS B ISO 18646-2 부합화 여부 — 원문 미열람으로 세부가 미확인이다
- 단계 5 페이지 3절: Floor-SP 와 MonteFloor 가 각각 쓰는 모서리·방·각도 매칭 규칙(방 IoU 임계값 수치 포함)을 논문별로 구분해 확인 — 이번에는 문구 출처가 구분되지 않아 교차 확인으로 보지 않았다
- 단계 5 q5-02: 현장 모델링 시간 단축을 수작업 대비 소요 시간·수정 횟수로 측정한 연구·사례 — 완료 조건 '평가 지표와 검증 절차' 행을 채우는 데 필요하다
- 단계 5 q5-03: 단계 1~4 결과로 가설 1~3 을 판정할 기준과 근거 — 가설 판정표 작성에 필요하다
- 국내 R&D 보고서 ref-747 의 발행일과 세부 지표(위치인식·지도작성 성능 지표 정의)
- 물류센터·창고 평면도에 인식 지표를 적용한 평가나 도면 기반 지도로 한 물류 로봇 주행 평가 사례 — 확인한 지표는 주거 평면도·대학·사무 건물 기준이다

## 이행한 수정 지시

- f1: '가장 가까운 하나만 참 양성으로 센다' 구절 삭제 — 단계 5 페이지 3절 요소 인식 지표에서 모서리 10픽셀·각도 5° 기준을 Floor-SP(ref-743) 기준으로 적고 방 IoU 는 수치 없이 '임계값'으로 두었으며, MonteFloor(ref-744)는 같은 세 수준 지표로 평가한다는 문장만 남겼다(아이디어 페이지 6절도 같음)
- f8: '2021 개정에서 통신 장애와 경로 위 장애물을 더했다'를 '시험에 쓸 장애 유형으로 장애물과 통신 장애 두 가지를 둔다'로 고쳐 단계 5 페이지 3절에 실었다
- f12: 세 지표가 같은 데이터 시퀀스의 여러 SLAM 결과를 비교할 때만 쓰는 상대 지표이며 기준 지도 없이 절대 품질을 판정하는 지표가 아니라는 한계를 같은 항목에 병기했다
- f7·f8·f9·f11·f13: 단계 5 페이지 3절에서 각 항목을 '연계 대상: '으로 시작하고, 주행 시험 소절 머리에 로봇 자체 지능·제어 경계의 연계 대상임을 밝힌 뒤 ROP 는 제조사·통합자 시험 결과를 받아 쓴다는 f23 문장으로 연결했다
- f19: 세 층 지표 표에서 주행 성공률·SPL·경로 이탈·좁은 통로 통과(와 위치추정 오차)를 '3. 주행 — 연계 대상(제조사·통합자 시험 결과 수용)' 행으로 분리하고, ROP 쪽 측정은 '3. 지도·정렬' 행(기준 지도 대비 지도 정확도·목적지 대응점 잔차·경로 차이·도착 인정 판정)으로 구분했으며 Mermaid 도식에도 같은 구분을 반영했다(아이디어 페이지 6절 표도 같음)
- f20: '문 폭 대비 차체 여유' 예시를 삭제하고 운영 허용치 예시는 VDA 5050 노드 허용 편차만 두었다(단계 5 페이지 3절·시나리오 제약 칸, 아이디어 페이지 6절)
- f22: '다음은 설명을 위한 가상의 시나리오이다. 수치는 넣지 않았다.'로 시작하고 완료·인계 칸 문장에 '이 가정 사례에서는'을 넣어 가정 사례임을 밝혔으며 수치는 쓰지 않았다
- f15·f17: 새 각주를 만들지 않고 기존 ref-628·ref-153 각주 정의 줄을 재사용하고 접근일 뒤에 ' (원문 미열람)'을 붙였다
- 각주: ref-743·ref-744·ref-746·ref-747·ref-748·ref-749·ref-750·ref-751·ref-752·ref-753·ref-063·ref-067·ref-628·ref-153 의 각주 정의에 ' (원문 미열람)'을 붙이고 reference_updates 에 source_unopened: true 를 넣었으며, ref-745·ref-754·ref-070·ref-065(와 inbox 원문 ref-031)에는 미열람 표기를 붙이지 않았다
- ref-754: 본문에 'README 기준 ICRA 2025 채택 2025-01-28'로 기준일을 적고 각주 정의와 reference_updates 의 발행일을 2025-01-28 로 두었다
- 단계 5 페이지 2절: 백로그의 q5-04~q5-08 을 제기 근거(백로그 origin 과 origin_run_id: f2·f21·f14·f8·f19)와 함께 '열림' 행으로 더하고, 새 질문 q5-09·q5-10 행까지 포함해 상태 줄을 '열린 질문: 9건 · 답한 질문: 1건'으로 맞췄다
- 새 질문 1(q5-09, 합격 임계값의 운영 허용치 도출)의 질문 끝에 '(관련: q4-12, q5-08)'을 병기해 단계 5 페이지 2·5절과 backlog_updates 에 실었다
- 2차: 단계 5 페이지 6절 완료 조건 첫 두 행을 트랙 개요 5절 문구 그대로 한 행('평가 지표와 검증 절차가 … "6. 검증 방법" 절에 실림')으로 합치고, 충족 여부 '미충족', 근거 '평가 지표 소절만 실림(실행 2026-09-25-80, 추정 중심), 검증 절차(q5-02) 미조사', 검증 판정 '미충족 · 미승인'으로 고쳤다
- 2차: 단계 5 페이지 4절 결론 첫 항목에서 '클래스별'을 빼 '정밀도·재현율·F1(IoU 또는 거리 임계값 매칭)'으로 고치고 [사실] 태그와 각주는 유지했다
- 2차: 아이디어 페이지 6절 patch 를 절 전체 replace 로 바꾸고, 첫 단락을 '앞 두 소절은 q1-04 답(실행 2026-09-25-22)의 선행 근거이고 평가 지표 소절은 q5-01 답(실행 2026-09-25-80)의 요약이며, 검증 절차는 q5-02 이후 실행이 채운다'는 내용으로 고쳤다(두 기존 소절과 각주는 그대로 유지)
- 2차: 아이디어 페이지 6절 '평가 지표' 소절의 '확인한 인식 지표는 주거 평면도 기준이며 … 찾지 못했다(부재 확인 아님)' 문장 끝에 [추정][^ref-747][^ref-754][^ref-753] 을 붙이고, 세 각주 정의를 소절 끝에 더하고 patch frontmatter 의 sources 에 ref-747·ref-753·ref-754 를 추가했다

## 트랙 갱신

- 단계 페이지: docs/tracks/floorplan-recognition/stage-5-verification-and-hypotheses.md
- 온톨로지 초안 버전: 1.2
- 트랙 로그 항목: 답한 질문: q5-01(f1~f24, 세 층 지표 구성은 추정 종합) / 새 질문: q5-09(f20, 관련 q4-12·q5-08), q5-10(f21) / 온톨로지 변경: 없음(평가 지표는 공간 그래프 스키마의 개념·관계가 아니라 검증 방법이어서 제안 없음, v1.2 유지) / 완료 조건 평가: 미충족(부족: 검증 절차 q5-02 미조사, 가설 판정표 q5-03 없음, 실험 계획 없음; 평가 지표 소절만 아이디어 3. 건축 도면 자동 인식 6절에 추정 중심으로 실음) / 세부영역 반영 제안: 23. 시험·형식 검증·벤치마크 1건, 6. 지도·공간·위치 모델 2건, 27. AI·학습·적응과 모델 운영 1건(총 4건) / 다음 실행 제안: q5-02, q5-03
- 개요 진행 현황: 단계 5 진행 중 — 열린 질문 9, 답함 1, 완료 조건 미충족

### 백로그 갱신

| id | 상태 | 답 링크 | 질문(새 질문) | 단계 | 제기 근거 |
|---|---|---|---|---|---|
| q5-01 | 답함 | docs/tracks/floorplan-recognition/stage-5-verification-and-hypotheses.md#q5-01 | — | — | — |
| q5-09 | 열림 | — | 요소 검출 F1·위치 오차·목적지 잔차·도착 성공률 같은 지도 품질 지표의 합격 임계값을 이미지 픽셀 기준이 아니라 물류 로봇의 노드 허용 편차(VDA 5050 allowedDeviationXY)·문 폭 대비 차체 여유 같은 운영 허용치에서 어떻게 도출하는가? (q5-01 에서 파생) (관련: q4-12, q5-08) | 5 | f20 |
| q5-10 | 열림 | — | 도면 기반 지도와 기준 지도(측량 또는 현장 SLAM 지도)에서 같은 출발–도착 쌍으로 경로 차이(길이 비율, 지나는 공간·문·승강기 순서)를 재는 시험 세트를 물류센터에서 어떻게 구성하는가(쌍 선택, 층간 이동 포함, 제조사별 반복)? (q5-01 에서 파생) | 5 | f21 |

### 세부영역 반영 제안

| 세부영역 번호 | 절 | 요약 |
|---|---|---|
| 23 | 6. 대표 접근법과 기술 | 연계 대상으로 주행 성능 시험 표준·시험법(ISO 18646-2:2024 의 자세 정확도·장애물·경로 이탈·좁은 통로·지도 작성 정확도, ASTM F3244 정의 영역 시험, NIST AGV 경로 추종 시험)과 내비게이션 지표(SPL, Arena-Bench 성공률·경로 길이 등)를 소개하고, 도면 기반 지도의 세 층 품질 지표(요소 인식·구조·그래프·지도·정렬, 추정)와 ROP 는 주행 시험 결과를 받아 쓴다는 경계(추정)를 반영 (근거 f7·f8·f9·f10·f11·f19·f23, 실행 2026-09-25-80) |
| 6 | 6. 대표 접근법과 기술 | 도면 기반 지도의 품질을 목적지 대응점 잔차가 VDA 5050 노드 허용 편차 안에 드는지로 판정하고 픽셀 기준 인식 임계값을 미터·운영 허용치로 옮기는 방법(추정), Open-RMF 층별 MSE 기록을 반영 (근거 f16·f17·f20·f22, 실행 2026-09-25-80). oq-077 근거 보강 |
| 6 | 8. 대표 연구와 자료 | 지도 품질 평가 자료로 SLABIM(BIM 좌표 정답 자세 데이터셋), 연계 대상 Lee·Woo·Shin(2026, CAD 지도 위 위치추정 RMSE), Filatov 외(2017, 같은 시퀀스 비교용 상대 지표라는 한계 병기)를 추가 (근거 f12·f14·f15, 실행 2026-09-25-80) |
| 27 | 6. 대표 접근법과 기술 | 도면 해석 모델의 평가 지표: 모서리·방·각도 정밀도·재현율·F1(Floor-SP), 파놉틱 품질(FloorPlanCAD), 클래스별 IoU(CubiCasa5K), 엣지 F1(Raster-to-Graph), IoU·그래프 편집 거리 가중합(SSIG). 분류 원문 8장 교차 규칙에 따라 적용 대상 6. 지도·공간·위치 모델과 양쪽 연결 (근거 f1·f2·f3·f4·f6, 실행 2026-09-25-80) |
