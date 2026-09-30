# 스토리텔러 산출 2026-09-30-16

## 페이지

| 동작 | 경로 | 상태 | 변경 요약 |
|---|---|---|---|
| update | docs/categories/security-and-privacy/privacy-and-video-data.md | draft | seed → draft: 3~11절 첫 작성(제25조의2·이동형 안내서, 목적별 이용·가명처리, 가림·저해상도·출력 필드 기술, 가정·병원·실외 사례, 책임 경계, 연결 16개 영역, 열린 질문 11건), 13절 각주, 1차 수정 15건·2차 수정 4건 반영 |
| create | docs/topics/2026/2026-09-30-area53-s6.md | draft | 자동 분리: 53. 개인정보·영상 데이터 의 "6. 대표 접근법과 기술" 절(1,883자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area53-s11.md | draft | 자동 분리: 53. 개인정보·영상 데이터 의 "11. 열린 질문" 절을 옮겼다. 2차 수정: 기존 질문 7건을 등록 문장 그대로 옮기고 부분 근거 메모 2건에 [추정]·각주, EDPB 풀어쓰기 |
| create | docs/topics/2026/2026-09-30-area53-s8.md | draft | 자동 분리: 53. 개인정보·영상 데이터 의 "8. 대표 연구와 자료" 절을 옮겼다. 2차 수정: Xu·Ayday 항목의 플랫폼 필드 설계 연결 문장을 [추정]으로 분리 |
| create | docs/topics/2026/2026-09-30-area53-s4.md | draft | 자동 분리: 53. 개인정보·영상 데이터 의 "4. 핵심 개념과 용어" 절(1,008자)을 옮겼다 |
| create | docs/topics/2026/2026-09-30-area53-s10.md | draft | 자동 분리: 53. 개인정보·영상 데이터 의 "10. 다른 연구영역과의 연결 (번호와 이름을 함께 표기)" 절을 옮겼다. 2차 수정: EDPB 풀어쓰기 |
| create | docs/topics/2026/2026-09-30-area53-s7.md | draft | 자동 분리: 53. 개인정보·영상 데이터 의 "7. 관련 표준·프레임워크·오픈소스" 절을 옮겼다. 2차 수정: EDPB·GDPR 풀어쓰기 |
| create | docs/topics/2026/2026-09-30-area53-s3.md | draft | 자동 분리: 53. 개인정보·영상 데이터 의 "3. 왜 중요한가" 절을 옮겼다. 2차 수정: SNS 풀어쓰기 |

## 변경 이력·색인

- 변경 이력: 2026-09-30 | 53. 개인정보·영상 데이터 | seed → draft: 3~11절 첫 작성(제25조의2·이동형 안내서, 목적별 이용·가명처리, 가림·저해상도·출력 필드 기술, 가정·병원·실외 사례, 책임 경계), 1차 수정 15건·2차 수정 4건 반영 | run 2026-09-30-16
- 홈 최근 업데이트: 2026-09-30 — 53. 개인정보·영상 데이터: seed → draft, 3~11절 첫 작성(이동형 영상정보처리기기 촬영 표시·거부, 가명처리·원본 활용 특례, 얼굴 가림·저해상도·인지 출력 필드 기술, 가정·병원·실외 사례)
- 대분류 최근 업데이트: 2026-09-30 — 53. 개인정보·영상 데이터: seed → draft, 3~11절 첫 작성과 각주(개인정보 보호법 제25조의2, 이동형 안내서, 가림 기술 연구, 로봇청소기 점검 사례)
- 세부영역 최근 업데이트: 2026-09-30 — 53. 개인정보·영상 데이터: 3~11절 첫 작성, 1차 수정 15건(목욕실 촬영 금지 구절·EDPB 범위 강등, f5·f16 문구 정정)과 2차 수정 4건(8절 해석 문장 [추정], 11절 등록 문장 일치·메모 태그, 약어 풀어쓰기) 반영

## 용어집 갱신

| 동작 | 용어(한글) | 용어(영문) | 한 줄 정의 | 관련 영역 | 출처 |
|---|---|---|---|---|---|
| new | 가명처리 | Pseudonymisation | 추가 정보 없이는 특정 개인을 알아볼 수 없도록 개인정보의 일부를 삭제·대체하는 처리로, 한국 가명정보 처리 가이드라인은 2024년 개정에서 영상·이미지·음성 같은 비정형 데이터로 대상을 넓혔다. | 53, 45, 47 | ref-1140 |
| new | 얼굴 가림 | Face Obfuscation | 영상에서 얼굴을 검출한 뒤 블러·모자이크·합성 얼굴 등으로 가려 신원을 알아볼 수 없게 하는 처리로, 로봇 영상의 저장·전송·학습 전에 쓰인다. | 53, 45, 63 | ref-1144, ref-1140, ref-1137, ref-1148 |
| new | 영상정보 원본 활용 규제샌드박스 실증특례 | Regulatory Sandbox Special Demonstration Exemption for Raw Video Use | 자율주행차·이동형 로봇 서비스 고도화 목적으로 가명처리하지 않은 영상 원본을 개발에 쓰도록 개인정보보호위원회가 기업별로 승인하는 규제샌드박스 특례로, 2023-11 운영이 발표되었다. | 53, 59, 47 | ref-1139, ref-588 |

## 참고문헌 갱신

| id | 기관 | 제목 | 유형 | 신뢰도 | URL |
|---|---|---|---|---|---|
| ref-1135 | 개인정보보호위원회 | [현재 안내서] 이동형 영상정보처리기기를 위한 개인영상정보 보호ㆍ활용 안내서(2024.9.) | 정부·연구기관 | high | https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS217&mCode=G010030000&nttId=10679 |
| ref-588 | 김·장 법률사무소 | ‘이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서’ 공개 (뉴스레터) | 업계 보고서 | medium | https://www.kimchang.com/ko/insights/detail.kc?sch_section=4&idx=30477 |
| ref-1137 | 정보통신신문 | "자율주행차·로봇 카메라 촬영 시 외부에 표시해야" | 기사 | medium | https://www.koit.co.kr/news/articleView.html?idxno=125844 |
| ref-1138 | 개인정보보호위원회 (개인정보 포털) | 개인정보 포털 — 이동형 영상정보처리기기 제도 및 신청방법 안내 | 정부·연구기관 | high | https://www.privacy.go.kr/front/contents/cntntsView.do?contsNo=286 |
| ref-1139 | 개인정보보호위원회 (대한민국 정책브리핑) | 자율주행차·이동형 로봇 개발에 ‘영상데이터’ 원본 활용 허용 | 정부·연구기관 | medium | https://www.korea.kr/news/policyNewsView.do?newsId=148922669 |
| ref-1140 | 법무법인(유) 세종 | 개인정보보호위원회, 비정형데이터 가명처리 관련 가명정보 처리 가이드라인 개정 (뉴스레터) | 업계 보고서 | medium | https://www.shinkim.com/kor/media/newsletter/2342 |
| ref-1141 | 경향신문 | 로봇청소기가 우리집 사진 찍어 외부 유출?…6종 ... (제목 일부만 확인) | 기사 | low | https://www.khan.co.kr/article/202509021447001 |
| ref-1142 | 아시아경제 | "로봇청소기 개인정보 관리 대체로 안전…미흡 사례 ... (제목 일부만 확인) | 기사 | low | https://view.asiae.co.kr/article/2026091410054053414 |
| ref-968 | MIT Technology Review | A Roomba recorded a woman on the toilet. How did screenshots end up on Facebook? | 기사 | medium | https://www.technologyreview.com/2022/12/19/1065306/roomba-irobot-robot-vacuums-artificial-intelligence-training-data-privacy/ |
| ref-1144 | Raina, N., Somasundaram, G., Zheng, K. 외 (Meta Reality Labs, arXiv) | EgoBlur: Responsible Innovation in Aria | 논문 | medium | https://arxiv.org/abs/2308.13093 |
| ref-1145 | Choi, M. 외 (arXiv) | Real-Time Privacy Preservation for Robot Visual Perception | 논문 | medium | https://arxiv.org/abs/2505.05519 |
| ref-1146 | Huang, X., Pan, S., Reinhardt, D., & Bennewitz, M. (arXiv) | Designing Privacy-Preserving Visual Perception for Robot Navigation Based on User Privacy Preferences | 논문 | medium | https://arxiv.org/abs/2604.06382 |
| ref-1147 | Xu, Y., & Ayday, E. (arXiv) | Seeing Less Is Not Seeing Safely: Privacy Leakage from Task-Scoped Robot Perception Exports | 논문 | medium | https://arxiv.org/abs/2609.03055 |
| ref-1148 | Sarfraz, B. M., Saplacan Lindblom, D., Baselizadeh, A., & Torresen, J. (HRI Companion '26) | The Privacy-Preserving Capabilities of a Service Robot in a Scenario-Based Healthcare Setting | 논문 | medium | https://doi.org/10.1145/3776734.3794481 |
| ref-1149 | European Data Protection Board (EDPB) | Guidelines 3/2019 on processing of personal data through video devices | 정부·연구기관 | medium | https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-32019-processing-personal-data-through-video_en |

## 열린 질문 갱신

| 동작 | id | 질문 | 영역 | 상태 | 링크 |
|---|---|---|---|---|---|
| new | — | 여러 제조사 로봇의 영상과 위치 정보를 모아 관제하는 플랫폼 사업자는 개인정보 보호법상 이동형 영상정보처리기기 운영자인가, 현장 운영 사업자의 수탁자인가, 그리고 촬영 표시·거부 의사 처리 의무는 누구에게 있는가? | 53, 58 | 열림 | — |
| new | — | 로봇이 플랫폼·클라우드·로그로 내보내는 인지 출력(객체 목록·의미 지도·궤적)의 재식별 위험을 측정하는 공개 평가 기준이나 벤치마크가 있는가? | 53, 54 | 열림 | — |
| new | — | 피촬영자가 한 로봇에 밝힌 촬영 거부 의사를 같은 현장의 다른 로봇과 플랫폼 기록에 공통으로 반영하는 방법이나 운영 사례가 있는가? | 53, 19 | 열림 | — |
| new | — | 유럽데이터보호이사회(European Data Protection Board, EDPB) 영상 장치 지침 3/2019 를 이동 로봇 카메라에 적용한 유럽 감독기관의 결정이나 해석 사례가 있으며, 보존 기간 권고는 무엇인가? | 53, 59 | 열림 | — |

## 현장 유형 매트릭스 갱신

| 현장 유형 | 항목 | 링크 | 제목 |
|---|---|---|---|
| 가정 | 시작 조건 | docs/categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시 | 53. 개인정보·영상 데이터 |
| 가정 | 작업 대상 | docs/categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시 | 53. 개인정보·영상 데이터 |
| 가정 | 수행 자원 | docs/categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시 | 53. 개인정보·영상 데이터 |
| 가정 | 제약 | docs/categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시 | 53. 개인정보·영상 데이터 |
| 가정 | 완료·인계 | docs/categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시 | 53. 개인정보·영상 데이터 |
| 가정 | 예외·성과 | docs/categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시 | 53. 개인정보·영상 데이터 |
| 병원 | 작업 대상 | docs/categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시 | 53. 개인정보·영상 데이터 |
| 병원 | 수행 자원 | docs/categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시 | 53. 개인정보·영상 데이터 |
| 병원 | 예외·성과 | docs/categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시 | 53. 개인정보·영상 데이터 |
| 실외 | 시작 조건 | docs/categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시 | 53. 개인정보·영상 데이터 |
| 실외 | 작업 대상 | docs/categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시 | 53. 개인정보·영상 데이터 |
| 실외 | 수행 자원 | docs/categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시 | 53. 개인정보·영상 데이터 |
| 실외 | 제약 | docs/categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시 | 53. 개인정보·영상 데이터 |
| 실외 | 완료·인계 | docs/categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시 | 53. 개인정보·영상 데이터 |
| 실외 | 예외·성과 | docs/categories/security-and-privacy/privacy-and-video-data.md#5-적용-사례-현장-유형-명시 | 53. 개인정보·영상 데이터 |

## 표준·프레임워크 갱신

| 이름 | 종류 | 기관 | 관련 영역 | 참고문헌 | URL |
|---|---|---|---|---|---|
| 개인정보 보호법 제25조의2(이동형 영상정보처리기기의 운영 제한) | 프레임워크 | 개인정보보호위원회 | 53, 59 | ref-1138 | https://www.privacy.go.kr/front/contents/cntntsView.do?contsNo=286 |
| 이동형 영상정보처리기기를 위한 개인영상정보 보호·활용 안내서(2024.9.) | 프레임워크 | 개인정보보호위원회 | 53, 59, 66 | ref-1135 | https://www.pipc.go.kr/np/cop/bbs/selectBoardArticle.do?bbsId=BS217&mCode=G010030000&nttId=10679 |
| 가명정보 처리 가이드라인(2024-02 개정, 비정형 데이터 포함) | 프레임워크 | 개인정보보호위원회 | 53, 45, 47 | ref-1140 | https://www.shinkim.com/kor/media/newsletter/2342 |
| 영상정보 원본 활용 규제샌드박스 실증특례 | 프레임워크 | 개인정보보호위원회 | 53, 59, 47 | ref-1139 | https://www.korea.kr/news/policyNewsView.do?newsId=148922669 |
| EDPB Guidelines 3/2019 on processing of personal data through video devices | 프레임워크 | European Data Protection Board (EDPB) | 53, 59 | ref-1149 | https://www.edpb.europa.eu/our-work-tools/our-documents/guidelines/guidelines-32019-processing-personal-data-through-video_en |
| EgoBlur | 오픈소스 | Meta Reality Labs | 53, 45 | ref-1144 | https://arxiv.org/abs/2308.13093 |

## 추가 조사 요청

- 6절·9절: 개인정보 보호법 제25조의2 조문 원문(국가법령정보센터)으로 '목욕실 등 사생활 침해 우려가 큰 장소 촬영 금지' 구절의 존재와 문구를 확인해야 한다. 현재 인용 출처에 없어 [추정]·법령 원문 미확인으로 두었다.
- 4·6절: 이동형 영상정보처리기기 안내서(2024.9.) PDF 원문으로 opt-out·다중 채널 표시·사고 영상·AI 학습 판단을 확인해 법률사무소 요약 의존을 줄일 필요가 있다.
- 7절: 유럽데이터보호이사회(EDPB) 지침 3/2019 본문(PDF)에서 다루는 범위(적법 근거·투명성·정보주체 권리·보존 기간·가정 예외)를 확인해야 한다. 검증에서 해당 구절을 삭제했다.
- 3·6절: 핵심 질문의 '사람의 위치 정보' 부분(보행자 위치 최소 수집, 궤적 익명화)을 직접 다룬 자료가 없어 본문에 넣지 못했다.
- 5절: 물류창고·제조 공장·상업 시설·기타 현장의 로봇 영상·작업자 데이터 보호 사례를 찾지 못해 해당 현장 유형 사례를 쓰지 못했다.
- 7절: 가명정보 처리 가이드라인(2024-02 개정) 원문(발행 기관 개인정보보호위원회 게시 URL)과 ISO 31700-1:2023(소비재 개인정보 중심 설계)을 확인하면 표와 표준 목록 URL을 보강할 수 있다.
- 5절 병원 사례: HRI 2026 컴패니언 논문 원문으로 시작 조건·제약·완료·인계 칸(현재 미확인)을 채울 근거가 필요하다.
- 11절 oq-171·oq-181·oq-214: 병원·세대 내부의 '공개된 장소' 해당 여부 해석과 안전성 확보조치 기준 개정판 조항 조사가 필요하다.
- 다음 실행 후보: 65. 가정·공동주택 페이지 5절에 로봇청소기 점검·유출 사례(ref-1141·ref-1142·ref-968), 63. 병원·의료 페이지에 모의 진료실 얼굴 가림 실험(ref-1148) 반영을 제안한다(예산으로 이번 실행에서는 미룸).

## 이행한 수정 지시

- f2 목욕실 등 촬영 금지 구절 강등 — 6절 '촬영 사실 표시와 거부 의사 수용'에서 공개 장소 촬영 제한·예외·표시 방법 문장은 [사실][^ref-1138][^ref-588]으로 두고, 목욕실 등 촬영 금지 구절은 별도 문장으로 떼어 [추정]과 '법령 원문 미확인'을 병기했다.
- f21 촬영 금지 장소 예시 변경 — 9절 표 '업종별 조건' 행의 '촬영 금지 장소(화장실·탈의실 등)'를 '사생활 침해 우려 장소(해당 법령 조항은 원문 미확인)'로 바꿨고, 10절 16. 장소 의미·지도 관리 연결도 '촬영 제한이 필요한 장소'로 일반화했다.
- f5 문구 정정 — 5절 실외 사례 예외·성과 칸과 6절 '목적별 이용 구분과 가명처리'에서 '가명·익명처리 없이 인공지능 학습에 쓰는 것은 예측 가능성이 있다고 보기 어렵고, 원본이 필요하면 규제샌드박스(실증특례)를 활용해야 한다'로 고치고 자율주행차 등 고속 이동 기기 맥락임을 밝혔다. 3절 종합 문장도 '가명·익명처리 없는 인공지능 학습'으로 맞췄다.
- f16 정정 — 6절 '인지 출력 필드 설계'에 시뮬레이션(AI2-THOR·ProcTHOR, 120개 장면) 결과임을 명시하고 '목표 범주 macro-F1 이 1.000에서 0.077로'로 고쳤으며, 8절 요약에도 시뮬레이션임을 밝혔다.
- f18 범위 구절 삭제 — 7절 표 EDPB 행에서 '적법 근거·투명성·정보주체 권리·기술적 보호조치' 목록을 삭제하고 최종판 채택(2020-01)만 [사실]로 두었으며 '다루는 범위 세부는 원문 미확인'을 적었다.
- f11 삭제 조건 정정 — 5절 가정 사례 완료·인계 칸을 '장애물 인식 사진은 브랜드별로 다음 청소 때, 이용자가 조회한 뒤, 또는 24시간 후 삭제'로 고쳤다.
- f8 한정 표현 완화 — 4절 용어와 7절 표, 용어집 정의에서 '서비스 고도화 목적에 한해'를 '서비스 고도화 목적으로'로 바꿨다.
- f1 정의 문구 — 4절 이동형 영상정보처리기기 정의를 원문대로 '부착·거치하여'로 적었다.
- ref-588 발행일 — 13절 각주의 발행일을 2024-10-14로 채우고 reference_updates 의 published 도 2024-10-14로 고쳤다.
- ref-1140 발행일 — 13절 각주와 reference_updates 의 발행일을 2024-02-08로 채웠다.
- ref-1148 서지 정정 — 제목을 'The Privacy-Preserving Capabilities of a Service Robot in a Scenario-Based Healthcare Setting', 기관·저자를 'Sarfraz, B. M., Saplacan Lindblom, D., Baselizadeh, A., & Torresen, J. (HRI Companion '26)', 발행일을 2026-03-16으로 13절 각주·8절·reference_updates 에 반영하고, 각주 접근일 뒤 ' (원문 미열람)'과 source_unopened: true 를 유지했다.
- ref-1137 제목 — '(제목 일부만 확인)'을 지우고 '"자율주행차·로봇 카메라 촬영 시 외부에 표시해야"'로 13절 각주와 reference_updates 에 적었다.
- 6·9절 범위 경계 — 6절 '검출 후 가림'과 5절 가정·병원 사례 서술에서 기기 쪽 얼굴 검출·가림과 모바일앱 인증을 분류 원문 19장 '로봇 자체 지능·제어' 쪽 연계 대상으로 서술하고, 9절 ROP 직접 범위를 등록 정보 기록·목적별 데이터 흐름·보유 기간·출력 필드 축소·거부 의사 전달로 한정했다.
- 용어집 실증특례 정의 — '안전조치를 조건으로'와 '한시적'을 정의에서 빼고, description 에 안전조치 항목과 특례 기간은 미확인이라고 적었다.
- 5절 현장 유형 — 가정(f10~f12), 병원(f17, 모의 실험임 명시), 실외(f7)만 사례로 쓰고 물류창고·제조 공장·상업 시설·기타 사례는 찾지 못했다고 절 첫머리에 적었으며, site_matrix_updates 는 가정·병원·실외 세 현장 유형 칸만 냈다.
- 분량 초과 자동 분리: 53. 개인정보·영상 데이터 본문 11,190자 > 기준 4,000자 → 7개 절을 주제 페이지로 옮김, 남은 본문 3,997자
- 2차: 8절 Xu·Ayday 태그 — 분리 페이지 2026-09-30-area53-s8.md 에서 '시뮬레이션으로 보였다'까지를 [사실][^ref-1147]로 두고, '이 결과는 플랫폼이 로봇에서 받는 데이터의 필드 설계와 직접 이어지는 것으로 보인다'를 별도 문장으로 떼어 [추정][^ref-1147]로 표시했다.
- 2차: 11절 등록 문장 일치 — 분리 페이지 2026-09-30-area53-s11.md 의 oq-143·oq-171·oq-181·oq-185·oq-211·oq-214·oq-228 질문 문장을 docs/open-questions.md 등록 문장 그대로 옮기고(oq-171 괄호 문구, oq-181 '그리고 이에 대한 개인정보보호위원회 해석이나 가이드라인이 있는가', oq-185 '(1X NEO 등)', oq-228 '국내 개인정보 보호 법령의' 복원), 이번 실행의 메모는 질문 문장 뒤 별도 문장으로 두었다.
- 2차: 11절 메모 태그·각주 — oq-181 뒤 로봇청소기 점검 부분 근거 메모에 [추정][^ref-1142]를, oq-228 뒤 안내서 사고 영상·인공지능 학습 판단 부분 근거 메모에 [추정][^ref-588]을 붙이고, 분리 페이지 8. 출처에 두 각주 정의를 두었으며 프런트매터 sources 를 [ref-588, ref-1142]로 채웠다.
- 2차: 약어 풀어쓰기 — 7절 분리 페이지 표에서 EDPB 를 '유럽데이터보호이사회(European Data Protection Board, EDPB)', GDPR 을 '일반 개인정보 보호법(General Data Protection Regulation, GDPR)'으로, 10절 분리 페이지 59번 연결과 11절 분리 페이지 새 질문(및 open_question_updates 의 같은 질문)에서 EDPB 를 같은 방식으로, 3절 분리 페이지의 SNS 를 '소셜 네트워크 서비스(SNS)'로 풀어 썼다.
