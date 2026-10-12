# 리서치 브리프 2026-10-12-07

| 항목 | 값 |
|---|---|
| 실행 id | 2026-10-12-07 |
| 날짜 | 2026-10-12 |
| 실행 유형 | update (갱신) |
| 대상 영역 | 45. 문서·도면·장면 이해 |
| 대분류 | L. AI·학습 기술 |

## 갭(비어 있거나 약한 섹션)

- 섹션 5. 적용 사례 — 실외 표(116·119행)가 '여러 로봇(대수 미확인)', '미확인(실험 수치가 초록에 없음)'으로 초록 기준이고, 물류창고 표(95·100·101·104행)가 '창고 CCTV 카메라 30대'로 기존 시설 CCTV 처럼 읽히며 작업 대상·예외·성과가 미확인
- 섹션 6. 대표 접근법과 기술(분리 2026-09-30-area45-s6) — AAS-RAIL 문장(45행)에 56.2%의 산출 조건(낙관적 정규식)과 고정 슬롯 평가 조건이 없고, LangExtract 소절(49행)에 원문 위치를 못 찾는 경우의 표시가 없으며, 도면 인식 소절에 입력 형식·제외 객체가, 융합 소절에 관측 주기·좌표 기준 조건이 없음
- 섹션 7. 관련 표준·프레임워크·오픈소스(분리 2026-09-30-area45-s7) — 근거 위치 자료형(Docling ProvenanceItem), 장면 그래프 파일 API(Spark-DSG), 한국어 문서 OCR 평가 자원, BIM 좌표 변환 범위(IfcMapConversion) 없음. AI Hub 문단(49행)에 메타데이터 필드 없음
- 섹션 8. 대표 연구와 자료(분리 2026-09-30-area45-s8) — Raster2Seq·면적 추정(Aliyev·Barsi)·Hydra-Multi·BIM-Loc 없음, AAS-RAIL(42행)·Robinson(44행)·Strader(46행) 항목의 조건 미기재
- 섹션 9. 책임 경계 — '카메라망의 소유·운영 주체는 출처가 밝히지 않아 미확인'(148행)
- 섹션 11. 열린 질문(분리 2026-09-30-area45-s11) — oq-147·oq-196·oq-225·oq-226·oq-227 의 부분 근거 갱신 필요. oq-197 은 이미 해결(도면 트랙 stage-2 q2-04)이라 대상이 아님
- 정정 요청 없음(target.json corrections 비어 있음). 메모·검증에서 나온 위키 내부 정정: 창고 카메라 30대의 설치 주체, Strader 실물 2대·데이터셋 3대 구분, AAS-RAIL 56.2% 조건

## 조사 질문

1. 매뉴얼·도면·현장 영상을 AI가 얼마나 정확히 읽어 낼 수 있는가? [분류원문]
2. oq-196 관련: 보고된 도면 인식 점수는 어떤 입력 형식·판정 기준·제외 객체·평가 분모 위에서 나왔으며 비주거 시설 도면에 옮길 수 있는가? (섹션 6·8 겨냥)
3. oq-147·oq-226 관련: 데이터시트·URDF 추출 정확도 수치는 어떤 조건의 값이며, 공개 구현은 추출 항목의 원문 위치를 찾지 못한 경우를 어떻게 표시하는가? (섹션 6·7·8 겨냥)
4. 다중 로봇 장면 그래프·카메라망 기반 다중 로봇 실증은 실물 로봇 몇 대·어떤 카메라·어떤 판정 기준으로 무엇을 보였고 사람 개입은 얼마나 있었는가? (섹션 5·8·9 겨냥)
5. oq-227 관련: 고정 카메라와 로봇 관측을 합칠 때 공개 자료는 관측 주기·동기화·좌표 기준을 어떻게 다루는가, BIM 좌표·현장 정합의 조건은 무엇인가? (섹션 6·7 겨냥)
6. oq-225 관련: 한국어 문서 OCR·파싱 평가 자원과 국내 도면 데이터의 메타데이터는 무엇을 담고 무엇이 빠져 있는가? (섹션 7 겨냥)

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | AECV-Bench 의 평가는 모두 원본 CAD·BIM 형식(DWG, RVT, IFC)이 아닌 래스터 PNG 도면 영상을 입력으로 쓴다. 벡터 기하나 객체 계층을 쓰는 모델은 평가하지 않는다. | ref-1073 | 아니오 | medium | 2026-10-12 | — | — |
| f2 | [사실] | AECV-Bench 의 개수 세기 과제는 문·창·침실·화장실 4종만 다루며, 계단·엘리베이터·기계 설비·구조 부재·내화 구성(fire-rated assemblies)은 평가하지 않는다. | ref-1073 | 아니오 | medium | 2026-10-12 | — | — |
| f3 | [사실] | Raster2Seq 는 선행 연구(Stekovic 외 2021, MonteFloor)의 평가 프로토콜을 따라 정답 방마다 IoU 가 가장 큰 예측 방을 짝지어 Room·Corner·Angle 을 정밀도·재현율·F1 으로 평가하며, 방 단위 짝은 IoU 가 0.5 를 넘을 때 유효로 본다. | ref-1667 | 아니오 | medium | 2026-10-12 | — | — |
| f4 | [사실] | Raster2Seq 의 모서리 판정(예측과 정답 모서리 거리 10픽셀 이내, 각도 차 5도 미만)은 이 논문 고유 기준이 아니라 Stekovic 외(2021)의 프로토콜을 따른 것이며, 256×256 영상 기준의 픽셀 허용 오차다. | ref-1667 | 아니오 | medium | 2026-10-12 | — | — |
| f5 | [사실] | Raster2Seq 는 한계로, 문·창처럼 드문 의미 구조의 위치를 가끔(occasionally) 잘못 잡아 방 내부에 문·창을 생성하는 실패 예를 제시하며, 이 실패의 발생률은 보고하지 않는다. | ref-1667 | 아니오 | medium | 2026-10-12 | — | — |
| f6 | [사실] | Aliyev·Barsi 의 실험에서 BakLLaVA 는 색상으로 방 유형을 구분한 주거 평면도 100장 모두에서 실제 예측 대신 템플릿 자리표시자를 출력해(검증 실패 시 1회 재시도 후 사용 불가 처리) 정량 평가에서 제외됐고, LLaVA-LLaMA 3 와 MiniCPM-V 2.6 만 평가됐다. | ref-1668 | 아니오 | medium | 2026-10-12 | — | — |
| f7 | [사실] | 이 연구는 방을 개체 단위가 아니라 방 유형 단위로 맞춘다. 한 도면 안 같은 유형의 정답 면적을 합쳐 비교점 하나로 만들어, 정답 방 다각형 894개에서 비교 쌍 472개를 만든다. | ref-1668 | 아니오 | medium | 2026-10-12 | — | — |
| f8 | [사실] | 같은 논문 안에서 픽셀 세기 기준선의 평가 단위 서술이 어긋난다. 초록은 MAPE 5.68%를 방 개체 단위, 1.58%를 도면 단위라고 적지만, §4.1·표 2 는 5.68%를 방 유형별 도면 단위 비교 472쌍 전체의 값으로 보고한다. | ref-1668 | 아니오 | medium | 2026-10-12 | — | — |
| f9 | [의견] | ROP 가 도면 인식 점수를 인용할 때는 입력 형식(래스터/벡터·BIM), 평가에서 빠진 객체, 판정 기준(IoU·픽셀 허용 오차), 평가 분모(유효 출력 표본과 전체 표본)를 함께 적어야 하며, 픽셀 기준 점수를 미터 단위 통과 가능성으로 바꿔 읽지 않고 승강기·방화문·충전 위치 같은 운영 객체는 별도 인수 시험으로 확인해야 한다. | ref-1073, ref-1667, ref-1668 | 아니오 | low | 2026-10-12 | — | — |
| f10 | [사실] | IFC 4.3 의 IfcMapConversion 은 국지 공학 좌표계를 지도 좌표계로 옮기는 변환(세 축 공통 축척 하나로 단위 변환, z축 기준 반시계 회전, Eastings·Northings·OrthogonalHeight 이동)을 기술하며, 지리 좌표계에서 지도로의 투영 자체는 다루지 않는다. | ref-1669 | 아니오 | medium | 2026-10-12 | — | — |
| f11 | [사실] | BIM-Loc 의 실제 공사장 데이터(홍콩시립대 공사 현장)는 손에 든 센서로 Ouster OS0-128 7개·Livox Mid-360 2개, 모두 9개 시퀀스(누적 3.5 km 초과)로 구성되며, 운용 중인 로봇 대수와는 무관하다. | ref-1670 | 아니오 | medium | 2026-10-12 | — | — |
| f12 | [사실] | BIM-Loc 의 공사장 실험에는 정답 궤적이 없어, 사무실 실험의 절대 궤적 오차(ATE) 대신 MME·scan-to-BIM·Wasserstein 같은 대리 지표로 평가한다. | ref-1670 | 아니오 | medium | 2026-10-12 | — | — |
| f13 | [추정] | Hilti × Trimble 2026 SLAM 챌린지 데이터 설명은 평면도가 공사 종료 시점의 의도된(완공) 상태를 보여 주며, 공사 중 벽·기둥이 차례로 지어지므로 이른 시기 기록에는 평면도 요소가 모두 있지는 않다고 적는다. | ref-1676 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f14 | [추정] | 같은 저장소는 2026-09-21 에 정답 수집 장치의 센서 동기화 설명을 추가했다고 기록하며, 그 설명은 정답 LiDAR·IMU 는 PPS 신호로 하드웨어 동기화하고 독립 동작하는 Insta360 은 두 IMU 신호의 자이로 크기를 맞춰 시간 오프셋과 시계 배율을 추정해 맞춘다고 적는다. | ref-1676 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f15 | [의견] | BIM·도면 좌표와 현장 정합에 관해 이 영역에는 요약·연결만 두는 것이 맞다. ROP 지도 인계 기록에는 좌표 변환 메타데이터 검사·실측 정합 검사·주행 가능성 검사 결과를 따로 두고, 도면 판(완공 의도 상태인지)·촬영일·센서 시간 보정 방식과 정합에 쓴 정답 종류를 함께 남겨야 한다. 주 서술 위치는 14. 도면·BIM에서 지도 만들기와 건축 도면 자동 인식 트랙이다. | ref-1669, ref-1670, ref-1676 | 아니오 | low | 2026-10-12 | — | — |
| f16 | [사실] | AAS-RAIL 은 미리 정한 목표 속성마다 값 하나를 채우는 고정 슬롯 값 예측으로 평가하며(문법 제약 디코딩), 속성 검출은 평가 범위 밖이라 정밀도·재현율·F1 은 보고하지 않는다. 51.8%→71.7%는 이 조건의 속성 추출 정확도다. | ref-1071 | 아니오 | medium | 2026-10-12 | — | — |
| f17 | [사실] | AAS-RAIL 의 56.2%는 여러 번 나오거나 무관한 일치의 모호성을 일부러 무시한 낙관적 정규식 검색으로 정답 속성값이 문서에서 발견된 비율이며, 속성 이름과 값이 함께 문서에 있는 경우는 13.4%뿐이었다. | ref-1071 | 아니오 | medium | 2026-10-12 | — | — |
| f18 | [의견] | 기존 위키의 AAS-RAIL 서술(51.8%→71.7%, 원문에서 확인 가능한 속성 56.2%)은 틀린 문장이 아니므로 지우지 말고, '고정 슬롯 평가'와 '모호성을 무시한 낙관적 정규식 기준, 이름·값 동시 13.4%'라는 조건을 붙여야 한다. 원문에 같은 값이 있다는 것과 그 값이 그 속성의 근거라는 것은 따로 검토해야 한다. | ref-1071 | 아니오 | low | 2026-10-12 | — | — |
| f19 | [사실] | URDF 에서 로봇 온톨로지를 채우는 LLM 파이프라인(gpt-oss:20b, PR2·Pepper·TIAGo 예비 평가)은 Pepper 의 사용자 신호용 ChestButton 을 접촉면 하위 유형의 Bumper 로 분류했고, 저자들은 물리적 성질은 맞았지만 항행 안전 센서와 사람–로봇 상호작용 입력을 구분할 기능 문맥이 없었다고 설명한다. | ref-239 | 아니오 | medium | 2026-10-12 | — | — |
| f20 | [사실] | LangExtract 의 Extraction 자료형은 추출 텍스트를 원문에서 찾지 못하면 원문 문자 구간(char_interval)을 None 으로 둔다. 즉 항목마다 원문 위치가 항상 붙는 것은 아니다. | ref-1671 | 아니오 | medium | 2026-10-12 | — | — |
| f21 | [사실] | Docling Core 의 ProvenanceItem(PDF·HTML·docx·pptx 에서 추출한 요소가 원문을 가리키는 근거 항목)은 쪽 번호(page_no)·영역 상자(bbox)·문자 구간(charspan) 세 필드를 모두 필수로 가진다. | ref-1672 | 아니오 | medium | 2026-10-12 | — | — |
| f22 | [의견] | 추출값과 근거 위치는 따로 저장하고, char_interval 이 None 이거나 근거 항목(ProvenanceItem) 자체가 없는 추출은 검토 대기로 두어야 한다. Docling 자료형에서는 세 필드가 필수라 '쪽·상자가 빈 근거 항목'은 생기지 않으므로 메모의 그 표현은 맞지 않다. 위치가 있다는 사실만으로 로봇 능력을 실행 가능으로 확정하지도 않는다. | ref-1671, ref-1672 | 아니오 | low | 2026-10-12 | — | — |
| f23 | [사실] | AI Hub 「건축 도면 데이터」(71465)의 건축 개요 데이터 속성표(3-2-4)는 14개 필수 속성 가운데 설계단계(design_stage, 범위 계획·실시)와 축척(scale, 원문 표기 '축적도')을 둔다. 데이터는 1.0판 2023-07-26 개방, 1.1판 2023-12-15 최종 개방이다. | ref-1012 | 아니오 | medium | 2026-10-12 | — | — |
| f24 | [추정] | ONTHEIT 는 KDoc-OCRBench-V2 를 한국 공공부문 단일 쪽 PDF 849개와 검증된 시험 56,197건(문장 존재 6,290·표 셀 49,115·머리말/꼬리말 792, 표가 약 87%)으로 구성하고, 실버 라벨 뒤 수동 검토했다고 설명한다. 문서 유형에 공공 매뉴얼(216개)은 있으나 로봇 매뉴얼은 따로 없다. | ref-1673 | 아니오 | low | 2026-10-12 | — | 벤더 주장 |
| f25 | [사실] | Hydra-Multi 는 각 로봇의 장면 그래프 전체를 제어 스테이션으로 주기적으로 전송하고, 로봇 쪽에서 삭제된 노드·엣지는 중앙 그래프에서도 지운다. 변경분만 보내거나 통신 단절 복구를 보장하는 방식의 근거가 아니다. | ref-1674 | 아니오 | medium | 2026-10-12 | — | — |
| f26 | [사실] | Hydra-Multi 의 평가는 uHumans2 시뮬레이션, 손에 든 장치로 따로 기록한 두 시퀀스를 서로 다른 두 로봇으로 취급한 SidPac, 실물 Jackal 2대로 기록한 Simmons 데이터로 이뤄진다. 재생 시퀀스 수를 동시에 운용한 로봇 대수로 세면 안 된다. | ref-1674 | 아니오 | medium | 2026-10-12 | — | — |
| f27 | [사실] | Strader 외의 종단 간 실물 실험(West Point Camp Buckner 실외)은 이종 로봇 2대(Clearpath Husky, Boston Dynamics Spot)로 했고, 장면 그래프 융합 절제 실험(§5.2)은 Kimera-Multi 데이터셋의 로봇 3대 기록(acl_jackal2, sparkal1, sparkal2)을 썼다. | ref-1070 | 아니오 | medium | 2026-10-12 | 실외 / 수행 자원 | — |
| f28 | [사실] | 이 연구의 재위치 평가는 Husky 와 Spot 이 비슷하게 지난 약 500 m 구간에서 10 m 마다 두 로봇 카메라 간 상대 자세를 추정해, 수동 확인한 루프 폐쇄로 자세 그래프 최적화한 의사 정답과 5 m·10도 이내면 성공으로 보았고, 성공률은 Husky 64%, Spot 65%였다. | ref-1070 | 아니오 | medium | 2026-10-12 | 실외 / 예외·성과 | — |
| f29 | [사실] | 같은 실험의 자연어 임무 시험은 단일 로봇 8회·다중 로봇 12회로, 실행 성공률은 단일 로봇이 쉬움·중간·어려움 100%·50%·50%, 다중 로봇이 66%·100%·75%였다. | ref-1070 | 아니오 | medium | 2026-10-12 | 실외 / 예외·성과 | — |
| f30 | [사실] | MIT-SPARK 의 Spark-DSG 는 Python 예제에서 JSON 장면 그래프 파일을 DynamicSceneGraph.load 로 불러와 객체·장소·방 등 층과 노드에 접근하는 API 를 보여 준다. | ref-1675 | 아니오 | medium | 2026-10-12 | — | — |
| f31 | [의견] | Spark-DSG 의 그래프 파일 API 는 교환 어댑터의 출발점으로는 쓸 수 있지만, 다른 제조사 장면 그래프와의 단위·좌표계·객체 식별자·삭제 표시 의미는 별도 계약으로 정해야 하며, Hydra-Multi 의 주기적 전체 전송을 플릿 통신 설계의 근거로 그대로 옮기지 말고 전송량·삭제 전파·초기 좌표 정합을 인수 시험에서 따로 재야 한다. | ref-1674, ref-1675 | 아니오 | low | 2026-10-12 | — | — |
| f32 | [사실] | Robinson 외의 창고 실험은 통로 6개(각 약 27 m)의 중형 창고 시험 구역에 로봇만 둔 상태에서, 연구팀이 설치한 맞춤 카메라 30대(Raspberry Pi 4 와 Camera Module 3, PoE 전원, 5 fps)로 했다. 창고가 원래 운영하던 CCTV 를 재사용한 것이 아니다. | ref-1065 | 아니오 | medium | 2026-10-12 | 물류창고 / 수행 자원 | — |
| f33 | [사실] | 전체 시스템 검증(§5.2)에서는 로봇 4대가 30개 카메라 시야 가운데 무작위로 정한 목표 지점으로 이동하고 도착하면 바로 새 목표를 받는 방식으로 45분 동안 1.3 km 를 다니며 지점 간 임무 76건을 마쳤다. | ref-1065 | 아니오 | medium | 2026-10-12 | 물류창고 / 예외·성과 | — |
| f34 | [사실] | 이 45분 시험에는 10·17·37·41분에 네 번 사람 개입이 있었다. 앞의 두 번은 최대 곡률 구간 추종 실패에 따른 충돌로 17분 뒤 현장에서 제어 이득을 조정해 해소했고, 뒤의 두 번은 로봇 일시 오분류와 학습이 적은 시각 영역에서의 방향 추정 오류가 자세 갱신 시간 초과로 제어기를 멈춘 인식 문제였다. | ref-1065 | 아니오 | medium | 2026-10-12 | 물류창고 / 예외·성과 | — |
| f35 | [사실] | Brorsson 외의 상용차 공장 배치에서 각 천장 카메라는 장애물 검출용 저해상도(640×360) 영상을 10 Hz, 로봇 위치 추정용 고해상도(3840×2160) 영상을 1 Hz 로 보내고, 로봇은 1 Hz 위치 추정값을 탑재 모터 오도메트리와 융합해 실시간 위치를 얻는다. | ref-308 | 아니오 | medium | 2026-10-12 | 제조 공장 / 수행 자원 | — |
| f36 | [사실] | RGB-only 능동 장면 그래프 연구는 MapAnything 이 모든 카메라 자세를 첫 입력 영상 기준으로 내므로, 첫 영상의 자세(외부 카메라 또는 로봇 초기 시점)만 알면 모든 자세를 일관된 전역 좌표로 나타내기에 충분하다고 적는다. | ref-1069 | 아니오 | medium | 2026-10-12 | — | — |
| f37 | [사실] | 같은 연구의 기하 관계 판정 임계값(수직 간격·바닥 겹침·수평 근접)은 실험 내내 고정하되 데이터셋마다 한 번 경험적으로 맞췄고, 데이터셋에 관계 정답이 없어 정량 평가는 노드에만 했다. | ref-1069 | 아니오 | medium | 2026-10-12 | — | — |
| f38 | [의견] | 고정 카메라와 로봇 관측을 합치는 입력에는 수집 시각·좌표 기준·관측 주기·동기화 방식(하드웨어 동기 여부)·정답 종류를 붙여야 하며, 공장 배치 보고·시뮬레이션 연구·데이터셋 설명의 서로 다른 조건을 합쳐 범용 허용 시간 차를 만들어서는 안 된다. | ref-308, ref-1069, ref-1676 | 아니오 | low | 2026-10-12 | — | — |
| f39 | [의견] | 다중 로봇 실증을 인용할 때는 임무 완료 수와 사람 개입 수, 실물 로봇 대수와 데이터셋 재생 대수를 함께 적어야 하며, 재위치 성공률(5 m·10도 기준)을 좁은 통로·도킹의 정밀 위치 보증으로 다시 쓰지 않아야 한다. 외부 카메라 기반 운용은 로봇 외형이 비슷해지거나 학습이 적은 구역이 생길 때 인식 재검증·정지·복구 담당을 정해 두어야 한다. | ref-1065, ref-1070 | 아니오 | low | 2026-10-12 | — | — |

### 근거 발췌

- **f1**: v1 PDF 6절 한계 'Focus on 2D raster images'(p.19): "All evaluations use rasterized PNG images of drawings rather than native CAD or BIM formats (DWG, RVT, IFC)". 평면도 120장·QA 192쌍 벤치마크의 범위 조건
- **f2**: v1 PDF 6절 한계 'Limited object classes'(p.20): "stairs, elevators, mechanical equipment, structural members, fire-rated assemblies, are not evaluated". 메모는 앞의 세 종류만 적었으나 검증에서 다섯 종류를 함께 적도록 보완
- **f3**: v3 §4.1 Metrics: "We follow the evaluation protocol used by prior work [Stekovic et al. 2021]" … "a match is considered valid if the IoU exceeds 0.5". 모든 데이터셋을 256×256 고정 해상도로 실험. 통과 폭·지도 안전성 지표가 아님
- **f4**: v3 §4.1: "we follow the protocol of [Stekovic et al. 2021] … A corner is considered correctly recovered if the distance is within 10 pixels and the angle difference is less than 5 degrees". 메모 F04 를 선행 프로토콜 기준으로 정정. 시설별 미터 허용 오차와 다름
- **f5**: v3 §4.5 Limitations·Fig. 8: "the model occasionally fails to accurately localize windows and doors", 캡션 "may generate windows and doors inside rooms". 전체 데이터에서의 발생 비율 수치 없음
- **f6**: §3.4(p.895): "Responses failing validation were retried once" … "BakLLaVA consistently returned template placeholders rather than genuine predictions across all 100 plans and we excluded it". 본문 모델명 LLaVA-LLaMA 3, 보충자료 modelfile 은 llama3.2-vision
- **f7**: §3.4(p.895): "all ground-truth instances of the same type within a plan were aggregated into a single comparison point" … "resulting in 472 matched comparisons in total (100 plans × up to 5 room types, minus 27 … 1 …)". 주거 도면만 대상
- **f8**: 초록: "MAPE = 5.68% at the room-instance level, and MAPE = 1.58% when evaluated at the floor plan level". §4.1: "aggregated across all 472 plan-level room-type comparisons … MAPE 5.68 ± 7.21%", 표 2 제목 "plan-level evaluation". 어느 쪽이 맞는지는 판단하지 않음
- **f9**: f1·f2(입력 PNG·미평가 객체), f3·f4(IoU 0.5·10 px/5° at 256×256), f6·f7·f8(유효 출력 제외와 집계 단위)에서 도출. 메모 A01~A03 'ROP 시사점'
- **f10**: ifc4.3-main 원본 IfcMapConversion.md: "NOTE The IfcMapConversion does not handle the projection of a map from the geodetic coordinate reference system." 축척·회전·이동 정의 같은 문서. 공식 HTML(IFC4.3.2.0)은 Cloudflare 차단으로 못 열어 판·절 번호는 적지 않음
- **f11**: arXiv v1 §4.2.1: 공사장 "9 data sequences", 두 LiDAR(Ouster OS0-128, Livox Mid-360)로 수집, 누적 3.5 km 초과, handheld sensor suite. 사무실 벤치마크(HKUST, 9개 시퀀스)와 구별
- **f12**: arXiv v1 §4.2.3: "where ground truth trajectories were unavailable" → 대리 지표(MME, scan-to-BIM, Wasserstein). IJRR 게재판(DOI 10.1177/02783649261462593)과 문구 대조는 하지 않음
- **f13**: 벤더 주장: README 'Dataset Floorplans': "The floorplans show the intended state of the building at the end of construction … not all elements are present in the earlier recordings." Hilti·Trimble·Oxford DRS 공동 산업 벤치마크 저장소(고정 커밋 e0c9277)
- **f14**: 벤더 주장: README News "[2026-09-21] Added the explanation about the sensors synchronization in the ground truth collection device", 'Sensors synchronization' 절. 문서 변경 기록이며 동기화 효과 수치·허용 시간 기준은 없음
- **f15**: f10(투영 미처리)·f11·f12(정답 궤적 없음)·f13·f14(완공 의도 평면도, 동기화 설명)에서 도출. 독립 검증 결과의 배치 판단(A04~A06 은 14영역·도면 트랙 stage-2·stage-4 가 주 위치)
- **f16**: v1 §3.4: "The task is evaluated as a fixed-slot value prediction problem with a predefined set of target properties" … "Precision, recall, and F1-score are not reported because property detection is outside the scope". 4개 제조사 데이터시트–AAS 200쌍
- **f17**: v1 §5 Discussion: "a regular-expression search that deliberately ignored ambiguities arising from multiple occurrences or unrelated matches. Despite these optimistic assumptions, … only 56.2% … only 13.4% contained both the property name and value"
- **f18**: f16·f17 에서 도출. 대상: 2026-09-30-area45-s8.md 42행, 2026-09-30-area45-s6.md 45행 AAS-RAIL 문장
- **f19**: v1 §4.3 Pepper: "mapped the non-standard interaction hardware ChestButton_frame, as a Bumper with a ContactSurface sub-type"; §4.4: 기능 문맥 부족 설명. ICSR 2026 게재(arXiv 표기). 세 플랫폼 예비 사례라 오류 비율은 산출 불가
- **f20**: 고정 커밋 74df59f langextract/core/data.py Extraction 설명: "char_interval: The character interval of the extraction in the original text. None when the extraction text could not be located in the source document." 자료형 정의이며 로봇 문서 성능은 미측정
- **f21**: 고정 커밋 0d5a7bd docling_core/types/doc/common/reference.py: class ProvenanceItem — page_no: int, bbox: BoundingBox, charspan: CharSpan(기본값 없음). 설명 "lightweight pointer back into the original document". 추출 내용의 의미 정확성은 보장하지 않음
- **f22**: f20·f21 에서 도출. 메모 A09 'ROP 시사점' 문구를 검증 결과(F18 필드 필수)대로 정정. oq-147 부분 근거
- **f23**: 공식 데이터 페이지 3-2-4: "design_stage | string | y | 설계단계 | 계획, 실시", "scale | number | y | 축적도"(축척의 오기로 보임). 변경 이력: 1.1 2023-12-15, 1.0 2023-07-26, 2025-05-08 구축업체정보 수정. 샘플값 완전성은 검증하지 않음
- **f24**: 벤더 주장: 고정 커밋 cdfc6d0 kdoc_benchmark_v2/README.md "56,197 verified test cases across 849 single-page PDFs from Korean public-sector documents", 파일별 건수, "silver labelling, and manual review: ONTHEIT". 제공자 자체 집계·외부 재현 없음
- **f25**: arXiv v1 III-A: "the entire scene graph is transmitted periodically from each robot to the control station", 삭제된 노드·엣지를 프런트엔드 그래프에서도 제거하는 book-keeping 설명. IROS 2023(DOI 10.1109/IROS55552.2023.10341838)
- **f26**: arXiv v1 IV-A: SidPac "two separate recordings as two different robots", Simmons 는 Intel Realsense D455 를 단 Jackal 로봇 2대, uH2 는 시뮬레이션
- **f27**: v2 §5.1: "two heterogeneous robots: a wheeled robot (Clearpath Husky) and a quadruped (Boston Dynamics Spot)"; §5.2: Kimera-Multi hybrid·outdoor 시퀀스에서 "acl jackal2, sparkal1, and sparkal2 robots" 데이터. 그래서 논문 전체를 '2대'로 단정하지 않음
- **f28**: v2 §5.1: "within 5 meters and 10 degrees of the pseudo ground truth pose computed via pose graph optimization with manually verified loop closures. The Husky achieved a relocalization success rate of 64%, while the Spot achieved 65%". 측량 정답이 아니며 도킹 정밀도 판정 아님
- **f29**: v2 표 1: grounding·planning·execution 성공률, "single-robot (8 trials) and multi-robot (12 trials)". Execute 열 단일 100/50/50, 다중 66/100/75. 시험 횟수가 적어 비율 비교에 한계
- **f30**: 고정 커밋 3c40997 examples/python_api.py: "G = dsg.DynamicSceneGraph.load(str(path_to_dsg))"(uHumans2 예제 그래프). 같은 연구실 구현의 내부 API 이며 다중 제조사 교환 표준이 아님
- **f31**: f25·f26·f30 에서 도출. 메모 A11·A13 'ROP 시사점'. 16. 장소 의미·지도 관리, 18. 실시간 세계 상태·데이터 일관성과 연결 검토
- **f32**: v1 §4.1: "with only robots present in the test area. We instrumented it with 30 custom cameras (Raspberry Pi 4 Model B with Camera Module 3, powered over PoE), each streaming at 5 fps". 기존 위키 '창고 CCTV 카메라 30대'(본 페이지 5절 표, s8)의 정정 근거
- **f33**: v1 §5.2: "Each was assigned a random goal position among the 30 camera views" … "The system ran for 45 min, over which the fleet traversed 1.3 km", "The fleet completed 76 point-to-point missions". 운반물 처리 성과가 아님
- **f34**: v1 §5.2: "the system needed four interventions, at minutes 10, 17, 37, and 41" … "The first two were collisions" … "The last two were perception-driven" … "triggered a pose-update timeout that halted the controller". 저자는 시제품 조건이라고 밝힘
- **f35**: v1 IV-A2 카메라 영상 두 흐름(10 Hz 장애물, 1 Hz 위치)과 IV-B1: "performed at a low frequency (1 Hz). However, onboard the robot, the low-rate position estimates are fused with motor odometry". 메모는 [추정]으로 냈으나 원문에 직접 서술된 구성이라 [사실]
- **f36**: v1 III-B: "knowing the pose of the first input image (e.g., an external camera or the robot's initial viewpoint) is sufficient to express all poses in a consistent global frame". 실제 시설 측량 정합 성능은 검증하지 않음
- **f37**: v1 III-B: "All geometric relation thresholds … are fixed across experiments and tuned empirically once per dataset"; IV: "Quantitative evaluation is therefore restricted to nodes, since datasets … do not provide ground-truth relational annotations". Replica·ReplicaCAD 기준
- **f38**: f35(1 Hz 위치+오도메트리), f36·f37(첫 영상 자세, 데이터셋별 임계값), f14(PPS 동기·IMU 정렬)에서 도출. oq-227·oq-035 부분 근거이며 허용 시간 차 수치는 여전히 없음
- **f39**: f27~f29(2대/3대, 64%·65%, 8·12회), f32~f34(45분·76건·개입 4회, 인식 원인 정지)에서 도출. 메모 A12·A14 'ROP 시사점'

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-1073 | Kondratenko, A., Birhane, M., Hsain, H. E., & Maciocci, G. (arXiv) | AECV-Bench: Benchmarking Multimodal Models on Architectural and Engineering Drawings Understanding | 2026-01-08 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2601.04819 | 아니오 |
| ref-1071 | Groß, J., & Heidrich, J. (arXiv) | AAS-RAIL: Improving Information Extraction for Asset Administration Shells through Retrieval-Augmented In-Context Learning | 2026-09-07 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2609.07334 | 아니오 |
| ref-239 | Dussard, B., & Sarthou, G. (LAAS-CNRS) | Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF | 2026-06 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2606.17073 | 아니오 |
| ref-1012 | AI Hub (한국지능정보사회진흥원) — 구축 주관 에이치씨아이플러스(주) | 건축 도면 데이터 | 2023-07-26 | 정부·연구기관 | high | 2026-10-12 | https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71465 | 아니오 |
| ref-1070 | Strader, J., Ray, A., Arkin, J. 외 (arXiv) | Language-Grounded Hierarchical Planning and Execution with Multi-Robot 3D Scene Graphs | 2025-07-10 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2506.07454 | 아니오 |
| ref-1065 | Robinson, L., Ramtoula, B., Izaaryene, A., Newman, P., & De Martini, D. (arXiv) | Multi-Robot Planning and Control from CCTV Camera Networks in a Real Warehouse | 2026-06-04 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2606.06762 | 아니오 |
| ref-308 | Brorsson, E. 외 | Infrastructure-based Autonomous Mobile Robots for Internal Logistics -- Challenges and Future Perspectives | 2025-12 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2512.15215 | 아니오 |
| ref-1069 | Modi, G., Buoso, D., Averta, G., & De Martini, D. (arXiv) | RGB-only Active 3D Scene Graph Generation for Indoor Mobile Robots | 2026-05-18 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2605.18197 | 아니오 |
| ref-1667 | Phung, H., & Averbuch-Elor, H. (Cornell University, arXiv; SIGGRAPH 2026) | Raster2Seq: Polygon Sequence Generation for Floorplan Reconstruction | 2026-08-07 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2602.09016v3 | 아니오 |
| ref-1668 | Aliyev, N., & Barsi, Á. (Periodica Polytechnica Civil Engineering) | Evaluating Vision-language Models for Zero-shot Room Area Estimation in Floor Plan Images | 2026-08-05 | 논문 | medium | 2026-10-12 | https://pp.bme.hu/ci/article/view/44138 | 아니오 |
| ref-1669 | buildingSMART (IFC4.3.x-development GitHub) | IFC 4.3 — IfcMapConversion (개발 브랜치 ifc4.3-main 원본, 게시판 IFC 4.3 HTML과 문구가 다를 수 있음) | 미확인 | 표준 | high | 2026-10-12 | https://github.com/buildingSMART/IFC4.3.x-development/blob/ifc4.3-main/docs/schemas/resource/IfcRepresentationResource/Entities/IfcMapConversion.md | 아니오 |
| ref-1670 | Zhang, Y., Lu, L., Pan, Y. 외 (arXiv; The International Journal of Robotics Research) | BIM-Loc: BIM-Integrated Discrepancy-Aware LiDAR-based Indoor Localization | 2026-06-12 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2606.14237v1 | 아니오 |
| ref-1671 | Google (google/langextract) | LangExtract — langextract/core/data.py (Extraction 자료형, commit 74df59f) | 미확인 | 오픈소스 문서 | high | 2026-10-12 | https://github.com/google/langextract/blob/74df59f5d20f3ae854204caf59bc21e28d2157ff/langextract/core/data.py | 아니오 |
| ref-1672 | Docling Project (docling-project/docling-core) | docling-core — docling_core/types/doc/common/reference.py (ProvenanceItem, commit 0d5a7bd) | 미확인 | 오픈소스 문서 | high | 2026-10-12 | https://github.com/docling-project/docling-core/blob/0d5a7bdc6eec6138055714756277730f1520ca61/docling_core/types/doc/common/reference.py | 아니오 |
| ref-1673 | ONTHEIT (ONTHEIT-AI/BizOnAI-OCR) | KDoc-OCRBench-V2 (Korean Document OCR Benchmark v2) — README (commit cdfc6d0) | 미확인 | 벤더 문서 | medium | 2026-10-12 | https://github.com/ONTHEIT-AI/BizOnAI-OCR/blob/cdfc6d0c4e415121ae476456ee13f1dea9e7f583/kdoc_benchmark_v2/README.md | 아니오 |
| ref-1674 | Chang, Y., Hughes, N., Ray, A., & Carlone, L. (MIT SPARK, arXiv; IROS 2023) | Hydra-Multi: Collaborative Online Construction of 3D Scene Graphs with Multi-Robot Teams | 2023-04-26 | 논문 | medium | 2026-10-12 | https://arxiv.org/abs/2304.13487v1 | 아니오 |
| ref-1675 | MIT-SPARK (MIT-SPARK/Spark-DSG) | Spark-DSG — examples/python_api.py (commit 3c40997) | 미확인 | 오픈소스 문서 | medium | 2026-10-12 | https://github.com/MIT-SPARK/Spark-DSG/blob/3c40997e4ae739c56ed3cdd6ef5e882d403d8b64/examples/python_api.py | 아니오 |
| ref-1676 | Hilti Research · Trimble · Oxford DRS (Hilti-Research/hilti-trimble-slam-challenge-2026) | Hilti × Trimble 360 Visual-Inertial SLAM Challenge 2026 — README (commit e0c9277) | 미확인 | 벤더 문서 | medium | 2026-10-12 | https://github.com/Hilti-Research/hilti-trimble-slam-challenge-2026/blob/e0c9277e20ab6d856703d3749d52b3a0f9b43926/README.md | 아니오 |

### 출처 요약

- **ref-1073**: 도면 이해 멀티모달 벤치마크(기존 출처, arXiv DOI 10.48550/arXiv.2601.04819). 이번에 v1 PDF 6절 한계(p.19–20)에서 래스터 PNG 입력과 개수 세기 4종 외 미평가 객체를 확인했다.
- **ref-1071**: 데이터시트에서 AAS 속성을 검색 증강 문맥 예시로 추출하는 연구(기존 출처, arXiv DOI 10.48550/arXiv.2609.07334). 이번에 v1 PDF §3.4 고정 슬롯 평가와 §5 의 56.2%·13.4% 산출 조건을 확인했다.
- **ref-239**: URDF 에서 LLM 으로 로봇 온톨로지를 채우는 예비 연구(기존 출처, arXiv v1 2026-06-10, ICSR 2026 게재 표기). 이번에 PDF §4.3·§4.4 에서 Pepper ChestButton→Bumper 분류 사례를 확인했다.
- **ref-1012**: 주거 3종 건축 도면 48,033장 학습 데이터(기존 출처). 이번에 3-2-4 건축 개요 데이터 속성표(design_stage·scale 필수)와 변경 이력(1.0판 2023-07-26, 1.1판 2023-12-15, 2025-05-08 구축업체정보 수정)을 확인했다.
- **ref-1070**: 다중 로봇 3차원 장면 그래프와 LLM 계획의 실외 실증(기존 출처, v1 2025-06-09·v2 2025-07-10, 공동저자 공식 목록 기준 ISER 2025). 이번에 v2 PDF §5.1(Husky·Spot, 재위치 64%·65%, 표 1)과 §5.2(Kimera-Multi 3대)를 확인했다.
- **ref-1065**: 보정하지 않은 카메라망과 외부 계산으로 창고 로봇 4대를 계획·제어한 실증(기존 출처). 이번에 v1 PDF §4.1(연구팀 설치 카메라 30대)과 §5.2(45분·76임무·개입 4회)를 확인했다.
- **ref-308**: 천장 카메라 기반 사내 물류 이동 로봇의 상용차 공장 배치 보고(기존 출처, arXiv v1 2025-12-17). 이번에 v1 PDF IV-A2·IV-B1 에서 영상 흐름(10 Hz·1 Hz)과 모터 오도메트리 융합을 확인했다.
- **ref-1069**: RGB 영상만으로 능동 3차원 장면 그래프를 만드는 연구(기존 출처). 이번에 v1 PDF III-B 의 첫 영상 자세 조건과 데이터셋별 임계값 조정, 관계 엣지 정량 평가 제외를 확인했다.
- **ref-1667**: 평면도 래스터 영상을 방 다각형 시퀀스로 복원하는 모델. arXiv v3(2026-08-07; v1 2026-02-09, v2 2026-05-11), SIGGRAPH 2026 Conference Papers 게재판 DOI 10.1145/3799902.3811124(2026-07-19, Crossref 확인). §4.1 평가 프로토콜과 §4.5 한계를 열람했다.
- **ref-1668**: 시각–언어 모델 3종의 평면도 방 면적 추정을 주거 평면도 100장으로 평가한 동료심사 논문. 70(3), pp.891–901, DOI 10.3311/PPci.44138(온라인 2026-08-05, Crossref 확인). 본문 PDF §3.4·§4.1·표 2 와 보충자료를 열람했다.
- **ref-1669**: 국지 공학 좌표를 지도 좌표로 옮기는 IFC 엔터티 정의 원본. 공식 HTML(standards.buildingsmart.org, IFC4.3.2.0)은 Cloudflare 차단으로 열지 못해 판·절 번호는 확인하지 않았다.
- **ref-1670**: BIM 과 현장 불일치를 고려한 LiDAR 실내 위치 추정. arXiv v1(2026-06-12), IJRR 온라인 게재 DOI 10.1177/02783649261462593(2026-07-06, Crossref 확인). §4.2.1~4.2.3 사무실·공사장 실험을 열람했다.
- **ref-1671**: LangExtract 추출 결과 자료형 정의(고정 커밋). char_interval 이 원문에서 위치를 찾지 못하면 None 이 된다는 설명을 확인했다. README 는 기존 ref-1074.
- **ref-1672**: Docling 문서 모델의 근거 위치 자료형 ProvenanceItem 정의(고정 커밋). page_no·bbox·charspan 세 필드가 모두 필수임을 확인했다.
- **ref-1673**: 국내 업체가 공개한 한국어 공공부문 문서 OCR 벤치마크 설명(고정 커밋). 문서 849개·시험 56,197건 구성과 라벨링 방식은 제공자 자체 설명이다.
- **ref-1674**: 여러 로봇의 3차원 장면 그래프를 중앙에서 온라인으로 합치는 시스템. arXiv v1(2023-04-26), IROS 2023 pp.10995–11002, DOI 10.1109/IROS55552.2023.10341838(Crossref 확인). III-A 전송 방식과 IV-A 실험 데이터를 열람했다.
- **ref-1675**: MIT SPARK 연구실의 동적 장면 그래프 라이브러리 Python 예제(고정 커밋). JSON 그래프를 DynamicSceneGraph.load 로 읽어 층·노드에 접근하는 API 를 확인했다.
- **ref-1676**: 공사 현장 시계열 SLAM 챌린지 데이터 설명(고정 커밋, 회사 주도 산업 벤치마크). 평면도 설명·2026-09-21 센서 동기화 설명 추가 기록을 확인했다. README 가 인용하는 arXiv 2607.06464(Centanni 외)는 열지 않았다.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/categories/ai-and-learning/document-drawing-and-scene-understanding.md | 5, 6, 7, 8, 9, 10, 11 | 갱신(차등): 섹션 5 — 실외 표: '수행 자원' 행(116행) '여러 로봇(대수 미확인)' → 실물 종단 간 실험은 Clearpath Husky·Boston Dynamics Spot 2대, 장면 그래프 융합 절제 실험은 Kimera-Multi 데이터셋 로봇 3대 기록(f27, '2대'로 단정하지 않음); '예외·성과' 행(119행) 미확인 → 재위치 성공률 Husky 64%·Spot 65%(5 m·10도, 수동 확인 루프 폐쇄 기반 의사 정답, f28), 임무 시험 단일 8회·다중 12회와 실행 성공률(f29). 물류창고 표: 사례 제목(95행)과 '수행 자원'(101행) '창고 CCTV 카메라 30대' → 연구팀이 설치한 맞춤 카메라 30대(Raspberry Pi 4·Camera Module 3, PoE, 5 fps)로 정정(f32); '작업 대상'(100행) → 30개 카메라 시야 안 무작위 목표 지점 간 이동 임무(f33); '제약'에 시험 구역에 로봇만 있었음(f32); '예외·성과'(104행) → 45분·1.3 km·지점 간 임무 76건(f33), 개입 4회(충돌 2·인식 2, f34). 의견 f39. 기존 내용 확인: 제조 공장 표 '제약' 행(87행)의 카메라 하드웨어 미동기(ref-308) — 메모 V02 는 넣지 않음. 메모 A05(BIM-Loc 공사장)는 5절 새 사례로 만들지 않고 6절 요약으로 둠 / 섹션 6(분리 2026-09-30-area45-s6) — 속성 추출 소절 45행 AAS-RAIL 문장: 51.8%→71.7% 는 유지하고 고정 슬롯 평가(f16)·56.2% 는 모호성을 무시한 낙관적 정규식 기준이며 이름·값 동시 13.4%(f17) 조건을 붙임, 의견 f18; URDF ChestButton→Bumper 기능 의미 오류(f19); 원문 위치 소절 49행 LangExtract 뒤에 char_interval None(f20)·Docling ProvenanceItem 필수 필드(f21), 의견 f22(메모 시사점 '쪽·상자가 빈 항목' 표현은 검증 결과대로 정정); 도면 인식 소절에 AECV-Bench 입력 PNG·미평가 객체(f1·f2), 의견 f9; BIM 좌표·현장 정합은 요약·연결 수준 2~3문장만: IfcMapConversion 투영 미처리(f10), BIM-Loc 공사장 9개 시퀀스·정답 궤적 없음(f11·f12), Hilti 평면도 완공 의도 상태·동기화 설명(f13·f14 [추정]·벤더 주장), 의견 f15 — 주 서술은 14. 도면·BIM에서 지도 만들기와 건축 도면 자동 인식 트랙(stage-2 q2-09, stage-4 q4-03·q4-15)으로 연결 제안; 융합 소절에 Brorsson 위치 1 Hz+모터 오도메트리·장애물 10 Hz(f35), RGB-only 첫 영상 자세 조건(f36)·임계값 데이터셋별 조정·관계 엣지 미평가(f37), 의견 f38 / 섹션 7(분리 2026-09-30-area45-s7) — 표: LangExtract 행에 위치 못 찾으면 char_interval None(f20), Docling 행에 ProvenanceItem(f21), 새 행 Spark-DSG(f30, 의견 f31), KDoc-OCRBench-V2(f24, 벤더 주장 [추정]), IfcMapConversion(f10, ifc4.3-main 원본 출처, IFC4.3.2.0 판·절 번호는 적지 않음, 요약·연결 수준). AI Hub 문단(49행)에 건축 개요 메타데이터 design_stage(계획·실시)·scale 필수와 1.0/1.1판 날짜(f23; 도면 트랙 q2-04·14영역 쪽 반영 검토). 기존 내용 확인: IDS 사용자 설명의 적용 대상·요구 구성(메모 F09)은 ref-1362, docs/topics/2026/2026-10-11-area21-s7.md 61~65행, 도면 트랙 stage-2 에 있어 넣지 않음 / 섹션 8(분리 2026-09-30-area45-s8) — 새 항목: Phung·Averbuch-Elor, Raster2Seq(SIGGRAPH 2026, f3~f5; 판정 기준은 Stekovic 외 2021 프로토콜), Aliyev·Barsi(Periodica Polytechnica Civil Eng. 70(3), f6~f8; 5.68%·1.58% 는 평가 단위 충돌로 재사용 보류), Chang 외 Hydra-Multi(IROS 2023, f25·f26), Zhang 외 BIM-Loc(IJRR 2026, f11·f12, 한 줄 요약). 기존 항목 보강: AAS-RAIL(42행, f16·f17), Robinson(44행 '카메라 30대' → 연구팀 설치 카메라, 45분·76임무·개입 4회, f32~f34), Strader(46행, 실물 2대·재위치 64%·65%, ISER 2025, f27~f29), Dussard·Sarthou(f19) / 섹션 9 — 148행 '카메라망의 소유·운영 주체는 출처가 밝히지 않아 미확인' → 5절 물류창고 사례의 카메라는 연구팀이 설치했고 시설이 원래 운영하던 CCTV 를 재사용한 사례가 아님(f32). 기존 시설 CCTV 재사용의 소유·운영 주체는 여전히 미확인 / 섹션 10(분리 2026-09-30-area45-s10) — 연결 제안: f10~f15 는 14. 도면·BIM에서 지도 만들기·건축 도면 자동 인식 트랙, f16~f22 는 로봇 매뉴얼 기반 능력 온톨로지 트랙 stage-3(q3-03·q3-05·q3-08), f25·f26·f30·f31 은 16. 장소 의미·지도 관리·18. 실시간 세계 상태·데이터 일관성 / 섹션 11(분리 2026-09-30-area45-s11) — 해결 제안 없음. 부분 근거: oq-147(f20·f21·f22, 로봇 전용 확정·반려 구현은 여전히 없음), oq-196(f1~f8 은 입력·판정·분모 조건만 보여 주며 비주거 시설 측정값은 없음), oq-225(f24 공공문서 OCR, 로봇 매뉴얼 전용 평가는 없음), oq-226(f16·f17·f19), oq-227(f35~f38, 허용 시간 차 수치 없음; oq-035 와 관련), oq-228 은 답하지 않음(53. 개인정보·영상 데이터 연결). oq-197 은 docs/open-questions.md 에서 이미 '해결'(tracks/floorplan-recognition/stage-2-data-and-standards.md#q2-04)이라 부분 답을 쓰지 않고, AI Hub 구조 8종 이름 문제(메모 U02)도 다루지 않음(f23 은 7절 메타데이터로만 씀). 메모의 '새 질문' 4건은 문구 대조로 기존 oq-225~oq-228 과 같아 새로 만들지 않음 / 후속 정리(이번 갱신 범위 밖): Robinson 외 사례를 인용한 다른 영역 페이지에 '창고 CCTV' 표현이 있으면 f32 로 정리 필요(후속 정리 필요). 다음 실행 후보: 14. 도면·BIM에서 지도 만들기(f10~f15), 18. 실시간 세계 상태·데이터 일관성(f25·f35~f38) |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- 출처 충돌: Aliyev·Barsi(2026)의 픽셀 세기 기준선 MAPE 5.68%·1.58%는 초록(방 개체 단위·도면 단위)과 §4.1·표 2(방 유형별 도면 단위 비교 472쌍)가 평가 단위를 다르게 적는데, 어느 쪽이 맞으며 재현 가능한 출력이 공개됐는가? | 관련 영역: 45. 문서·도면·장면 이해, 14. 도면·BIM에서 지도 만들기 | 근거: f8 | 종류: 출처 충돌
- 도면 인식 벤치마크의 픽셀 기준 점수(방 IoU 0.5, 모서리 10픽셀·5도)를 실제 문 통과 폭·충전기 접근 가능성 같은 미터 단위 주행 조건으로 검증한 평가나 사례가 있는가? | 관련 영역: 45. 문서·도면·장면 이해, 14. 도면·BIM에서 지도 만들기 | 근거: f4 | 종류: 일반
- 여러 제조사 로봇이 장면 그래프를 공유할 때 주기적 전체 전송 대신 변경분 전송, 통신 단절 뒤 재접속, 삭제 충돌 처리를 시험해 허용 기준을 보고한 사례나 공개 구현이 있는가? | 관련 영역: 45. 문서·도면·장면 이해, 18. 실시간 세계 상태·데이터 일관성 | 근거: f25 | 종류: 일반
- 시설 카메라망 기반 다중 로봇 제어를 사람이 함께 다니는 구역이나 장시간 운용에서 시험해 시간당 사람 개입 수와 인식 원인 정지를 보고한 사례가 있는가? | 관련 영역: 45. 문서·도면·장면 이해, 54. 시험·형식 검증·벤치마크 | 근거: f34 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 18 · 교차 확인: 0
- 예산 사용량: 검색 0회 · 신규 출처 10건
- 미확인 항목:
    - 리서치 단계 산출물 출처: 외부 AI 조사 메모(runs/2026-10-12-07/external_research.md)를 변환했다. 2026-10-12 Claude 서브에이전트가 메모의 [사실] 주장을 원문과 대조 검증했고, 검증에서 나온 수정(태그 강등·표현 정정·메타데이터 정정·중복 제거)을 반영했다.
    - f10: buildingSMART 공식 HTML(IFC4.3.2.0, standards.buildingsmart.org)은 Cloudflare 차단으로 열지 못해 ifc4.3-main 원본으로 확인했다. 게시판 판의 절 번호(메모의 §8.18.3.6.1)와 문구 일치는 미확인
    - f8: Aliyev·Barsi 의 5.68%·1.58% 평가 단위는 논문 안에서 서술이 충돌해 어느 쪽인지 확정하지 않음(저자 자료 미확인)
    - f12: BIM-Loc 공사장 시퀀스의 실측 정답 궤적 오차는 저자가 제공하지 않아 미확인. IJRR 게재판 본문은 열지 않고 arXiv v1 로만 확인
    - f13·f14: Hilti 저장소 README 만 근거(회사 주도 저장소)라 [추정]·벤더 주장. README 가 인용한 arXiv 2607.06464 는 열지 않음
    - f24: KDoc-OCRBench-V2 구성·라벨링은 제공자 자체 설명이며 외부 재현 없음. 로봇 매뉴얼 대상 한국어 추출 정확도(oq-225)는 여전히 미확인
    - f19: URDF 기능 의미 오류는 세 플랫폼 예비 사례라 발생률 산출 불가. f16·f17: AAS-RAIL 의 새 제조사 일반화·유의성(신뢰구간) 미보고
    - f29: 임무 시험 횟수(8·12회)가 적어 성공률 비교에 한계. f27 의 ISER 2025 게재와 Robinson 외(f32~f34)의 학회 게재 여부는 출판사 판으로 확인하지 않음
    - f34: 개입 4회는 45분, 로봇만 있는 시험 구역 조건이다. 사람 혼재·야간·장기 운용 개입률은 미확인
    - oq-147(로봇 전용 확정·반려 구현), oq-196(비주거 시설 도면 정밀도·재현율), oq-226(로봇 매뉴얼 추출 벤치마크), oq-227(허용 시간 차·정합 기준 수치), oq-228(국내 CCTV 법령 판단)은 이번 메모로 완전히 답하지 못함
    - 메모가 진단에 쓴 위키 고정 커밋(85960d2)과 배포 페이지의 동일성은 확인하지 않음
- 범위 경계 위반 의심:
    - f10~f15: BIM 좌표 변환·현장 정합은 14. 도면·BIM에서 지도 만들기와 건축 도면 자동 인식 트랙이 주 위치라 이 영역에는 요약·연결 수준으로만 제안함
    - f11·f12·f27·f28·f35·f36: LiDAR 위치 추정·재위치·로봇 탑재 오도메트리 융합은 로봇 쪽 SLAM·위치 추정(분류 원문 19장의 외부 연계)에 걸치므로 플랫폼이 받는 결과의 조건·평가 기준으로만 씀
    - f25·f26·f30·f31: 장면 그래프 공유·교환은 16. 장소 의미·지도 관리, 18. 실시간 세계 상태·데이터 일관성과 겹치며 이 영역에는 장면 인식 결과의 표현·교환 조건으로만 씀
- 한계: 외부 조사 변환이라 검색·열람 횟수 집계 없음(budget_used.queries 0 은 집계 없음을 뜻함). 신규 출처 10건/15(ref-1667~ref-1676, 예약 구간 ref-1667~ref-1696 안), 재사용 8건(ref-1073·ref-1071·ref-239·ref-1012·ref-1070·ref-1065·ref-308·ref-1069). 출처 매핑(검증 결과 기준): 메모 n1→ref-1073, n2→ref-1667, n3→ref-1668, n4→ref-1669(공식 HTML 대신 ifc4.3-main 원본, ref-213 과 같은 형식), n5→ref-1670, n6→ref-1071, n7→ref-239, n8→ref-1671(ref-1074 는 README 라 별도), n9→ref-1672, n10→ref-1012, n11→ref-1673(벤더 문서), n12→ref-1674, n13→ref-1070, n14→ref-1675, n15→ref-1065, n16→ref-308, n17→ref-1069, n18(IDS UserManual)→기존 ref-1362 이나 F09 를 중복으로 빼서 sources 에 넣지 않음, n19→ref-1676(벤더 문서). 교차 확인 0건(모든 사실 finding 이 단일 출처이거나 같은 연구 계열: Hydra-Multi·Strader·Spark-DSG 는 MIT SPARK 계열, Robinson·Modi 는 De Martini 공동저자) — 신뢰도 medium 이하. 검증 반영: F09(IDS)·V02(Brorsson 하드웨어 미동기)·U02(AI Hub 구조 8종)는 중복·대상 외로 넣지 않음; oq-197 은 이미 해결이라 부분 답 안 씀; F02 미평가 객체에 구조 부재·내화 구성 추가; F04 를 Stekovic 외 2021 선행 프로토콜 기준으로 정정(f3·f4); F06 재시도 1회·모델명 확인; F08 출처를 공식 HTML 에서 ifc4.3-main 원본으로 바꾸고 판·절 번호 삭제; F11 '공사장' 명시(사무실 벤치마크와 구별); F12·F13 [추정]·벤더 주장; F18 Docling 세 필드 필수를 반영해 메모 시사점 표현 정정(f22); F22 Strader 실물 2대·절제 데이터셋 3대 구분과 재위치 64%·65% 추가(f27·f28), 임무 시험 횟수(f29); A14 '창고 CCTV 카메라 30대'를 연구팀 설치 카메라로 정정하고 작업 대상을 무작위 목표 이동으로(f32·f33); V01 [추정]·벤더 주장 유지; V03 은 원문 IV-B1 직접 서술이라 [사실](f35); 서지 DOI 보완 — Raster2Seq SIGGRAPH 2026 DOI 10.1145/3799902.3811124, BIM-Loc IJRR DOI 10.1177/02783649261462593, Aliyev·Barsi 70(3) pp.891–901 DOI 10.3311/PPci.44138, Hydra-Multi IROS 2023 DOI 10.1109/IROS55552.2023.10341838(모두 Crossref 로 확인, 메모 U16 해소). A04~A06(f10~f15)은 45 에는 요약·연결 수준으로 제안하고 주 위치는 14영역·도면 트랙으로 둠. 열린 질문: 해결 제안 없음, 부분 근거 oq-147·oq-196·oq-225·oq-226·oq-227. 메모의 '새 질문' 4건은 기존 oq-225~oq-228 과 같아 새로 만들지 않음. 메모 U01~U17 가운데 U01→oq-196, U03→oq-225·oq-226, U04→oq-147, U12→oq-227(oq-035 관련), U15→oq-228 로 기존 질문에 붙이고, U02 는 폐기, U16 은 Crossref 확인으로 해소, U06·U05·U11·U13 만 새 질문 4건으로 올림(나머지 U07~U10·U14·U17 은 unverified 에 남김). 메모의 '.research-work' 로컬 경로·행 번호는 쓰지 않고 원문 절·쪽과 위키 실제 위치를 적었다. 정정 요청 없음. 용어 후보 없음.
