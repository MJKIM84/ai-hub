# 리서치 브리프 2026-09-26-01

| 항목 | 값 |
|---|---|
| 실행 id | 2026-09-26-01 |
| 날짜 | 2026-09-26 |
| 실행 유형 | weekly_review (주간 정리) |
| 대상 영역 | 해당 없음 |
| 대분류 | 해당 없음 |

## 갭(비어 있거나 약한 섹션)

- url_check.json 오류 2건: ref-172(GitHub 위키, 미러 없음), ref-637(국가법령정보센터 한글 경로 URL)
- url_check.json 미러 오류 1건: ref-412(Open-RMF place.json)
- 참고문헌 목록 중복 의심: ref-315·ref-709(같은 정책브리핑 보도자료), ref-584·ref-707·ref-767(같은 IEC 62443-3-3:2013)
- 참고문헌 목록 번호 공백: ref-781~ref-791 미등록(보류 실행 산출물로 추정)

## 조사 질문

1. 점검 대상 ref-172: https://github.com/nasa-jpl/rosa/wiki/Custom-Agents (url_check 오류, 미러 없음)
2. 점검 대상 ref-412: https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/place.json (정책 차단, 미러 오류)
3. 점검 대상 ref-637: https://www.law.go.kr/법령/산업디지털전환촉진법/(18692,20220104) (url_check 오류)
4. 점검 대상 참고문헌 중복 의심: ref-315·ref-709, ref-584·ref-707·ref-767
5. 점검 대상 내부 링크·각주: link_check.txt 통과(파일 1240개, 경고 0건) — 추가 조치 없음

## 발견 사항

| id | 태그 | 주장 | 출처 | 교차 확인 | 신뢰도 | 기준일 | 흐름 단계 / 항목 | 표시 |
|---|---|---|---|---|---|---|---|---|
| f1 | [사실] | ref-172(ROSA 위키 Custom Agents) 정규 URL 은 이 환경에서 미러가 없어 오류로 기록됐으나, GitHub 위키 원문 경로(raw.githubusercontent.com/wiki/nasa-jpl/rosa/Custom-Agents.md)는 오늘 기준 열리고 내용이 ROSA 를 다른 로봇에 맞게 도구·프롬프트로 사용자 정의하는 안내로 제목과 일치한다. | ref-172 | 아니오 | medium | 2026-09-26 | — | — |
| f2 | [사실] | ref-412(Open-RMF rmf_ros2 place.json) 는 url_check 에서 미러 오류로 기록됐으나 오늘 raw 경로가 열리고 스키마 제목이 'Place Description' 으로 등록 제목과 일치해, 미러 오류는 일시적 실패로 보인다. | ref-412 | 아니오 | medium | 2026-09-26 | — | — |
| f3 | [사실] | ref-637 의 등록 URL 은 한글 경로가 퍼센트 인코딩되지 않은 형태여서 점검 스크립트에서 오류가 났으며, 같은 경로를 인코딩한 URL 이 검색 결과에 '산업디지털전환촉진법' 제목으로 나타나 문서 자체는 존재하는 것으로 확인된다. | ref-637 | 아니오 | medium | 2026-09-26 | — | 원문 미열람 |
| f4 | [추정] | 검색 결과에 국가법령정보센터 제목 '산업 디지털 전환 및 인공지능 활용 촉진법' 이 나타나고 같은 제명 변경을 담은 개정안 발의 보도가 있어, ref-637 이 가리키는 법률의 제명·현행 판이 바뀌었을 가능성이 있으나 시행 여부는 확인하지 못했다. | ref-637 | 아니오 | low | 2026-09-26 | — | 원문 미열람 |
| f5 | [사실] | ref-315 와 ref-709 는 호스트만 다르고(www.korea.kr/briefing 과 korea.kr/news) 같은 보도자료 id(newsId=156480155)와 같은 제목을 가리켜 참고문헌 중복으로 보인다. | ref-315, ref-709 | 아니오 | medium | 2026-09-26 | — | 원문 미열람 |
| f6 | [사실] | ref-584(CSA 채택판, ANSI 웹스토어), ref-707(iTeh 샘플 PDF), ref-767(iTeh 카탈로그)은 모두 IEC 62443-3-3:2013 한 표준을 가리키는 서로 다른 URL 이어서 대표 출처 하나로 합칠 후보다. | ref-584, ref-707, ref-767 | 아니오 | medium | 2026-09-26 | — | 원문 미열람 |

### 근거 발췌

- **f1**: raw 위키 원문의 절 제목 'Adding Tools', 새 클래스·인스턴스를 만들어 도구와 프롬프트로 ROSA 를 다른 로봇에 맞추는 방법을 설명한다.
- **f2**: 스키마 title "Place Description", 설명 "Description of a place that the robot can go to"; 경유점 또는 경유점+선택적 방향을 받는다.
- **f3**: 검색 결과 URL: https://www.law.go.kr/%EB%B2%95%EB%A0%B9/%EC%82%B0%EC%97%85...(18692,20220104), 제목 '산업디지털전환촉진법'. 원문 미열람(정책 차단).
- **f4**: 검색 요약: law.go.kr lsInfoP 제목 '산업 디지털 전환 및 인공지능 활용 촉진법'; 2025-10-01 시행판 링크 존재. 개정안은 현행법 제명 변경을 골자로 한다고 보도됨. 원문 미열람.
- **f5**: 두 항목 모두 제목 '국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다', newsId=156480155, 발행 2021-11. 참고문헌 목록 대조 결과.
- **f6**: 세 항목 제목이 모두 IEC 62443-3-3:2013(2013-08) System security requirements and security levels 이며 ref-584 는 CSA 채택판 표기. 참고문헌 목록 대조 결과.

## 출처

| id | 기관 | 제목 | 발행일 | 유형 | 신뢰도 | 접근일 | URL | 원문 미열람 |
|---|---|---|---|---|---|---|---|---|
| ref-172 | NASA Jet Propulsion Laboratory (nasa-jpl) | Custom Agents · nasa-jpl/rosa Wiki | 미확인 | 오픈소스 문서 | medium | 2026-09-26 | https://github.com/nasa-jpl/rosa/wiki/Custom-Agents | 아니오 |
| ref-412 | Open Robotics (open-rmf) | rmf_ros2 — rmf_fleet_adapter/schemas/place.json | 미확인 | 오픈소스 문서 | medium | 2026-09-26 | https://github.com/open-rmf/rmf_ros2/blob/main/rmf_fleet_adapter/schemas/place.json | 아니오 |
| ref-637 | 국가법령정보센터(산업통상자원부) | 산업 디지털 전환 촉진법 (법률 제18692호) | 2022-01-04 | 정부·연구기관 | medium | 2026-09-26 | https://www.law.go.kr/법령/산업디지털전환촉진법/(18692,20220104) | 예 |
| ref-315 | 산업통상자원부 국가기술표준원(대한민국 정책브리핑) | 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 | 2021-11 | 정부·연구기관 | medium | 2026-09-26 | https://www.korea.kr/briefing/pressReleaseView.do?newsId=156480155 | 예 |
| ref-709 | 대한민국 정책브리핑(산업통상자원부 국가기술표준원) | 국가표준(KS) 제정으로 로봇의 엘리베이터 탑승 돕는다 | 2021-11-11 | 정부·연구기관 | medium | 2026-09-26 | https://korea.kr/news/pressReleaseView.do?newsId=156480155 | 예 |
| ref-584 | CSA / IEC (ANSI Webstore) | CAN/CSA IEC 62443-3-3-2017 - Industrial communication networks - Network and system security - Part 3-3: System security requirements and security levels (Adopted IEC 62443-3-3:2013, first edition, 2013-08) | 2013-08 | 표준 | medium | 2026-09-26 | https://webstore.ansi.org/standards/csa/csaiec624432017-2442576 | 예 |
| ref-707 | IEC | IEC 62443-3-3:2013 Industrial communication networks — Network and system security — Part 3-3: System security requirements and security levels (sample) | 2013-08 | 표준 | medium | 2026-09-26 | https://cdn.standards.iteh.ai/samples/19488/7c0b753be32e46fc986c23c32efbdbe8/IEC-62443-3-3-2013.pdf | 예 |
| ref-767 | IEC | IEC 62443-3-3:2013 Industrial communication networks — Network and system security — Part 3-3: System security requirements and security levels | 2013-08 | 표준 | medium | 2026-09-26 | https://standards.iteh.ai/catalog/standards/iec/c32e05fe-78a2-467e-a24d-0fc422289f55/iec-62443-3-3-2013 | 예 |

### 출처 요약

- **ref-172**: ROSA 를 다른 로봇에 맞게 새 클래스·인스턴스를 만들고 도구·프롬프트로 사용자 정의하는 방법을 설명하는 공식 위키 문서.
- **ref-412**: 로봇이 갈 수 있는 장소(경유점, 선택적 방향)를 기술하는 Open-RMF 작업 설명 JSON 스키마.
- **ref-637**: 원문 미열람. 2022-01-04 공포된 산업 디지털 전환 촉진법 제정 법률 본문(국가법령정보센터).
- **ref-315**: 원문 미열람. KS B 7317 제정을 알리는 국가기술표준원 보도자료.
- **ref-709**: 원문 미열람. ref-315 와 같은 보도자료 id 를 가리키는 다른 경로의 URL.
- **ref-584**: 원문 미열람. IEC 62443-3-3:2013 의 캐나다 채택판 판매 페이지.
- **ref-707**: 원문 미열람. IEC 62443-3-3:2013 의 iTeh 샘플 PDF.
- **ref-767**: 원문 미열람. IEC 62443-3-3:2013 의 iTeh 카탈로그 페이지.

## 페이지 제안

| 동작 | 경로 | 섹션 | 이유 |
|---|---|---|---|
| update | docs/references/ref-637.md | — | needs_update 제안 (f3·f4): URL 을 퍼센트 인코딩 형태로 바꾸고, 제명이 '산업 디지털 전환 및 인공지능 활용 촉진법'으로 바뀌었는지 확인되면 현행 판 링크를 병기한다. 이 출처를 인용하는 28. 표준·상호운용성·다사업자 거버넌스 페이지의 제명 표기도 재확인 대상. |
| update | docs/references/ref-709.md | — | deprecated 제안(대체 페이지·출처: docs/references/ref-315.md) (f5): 같은 보도자료 newsId=156480155 중복. 다음 실행 후보: ref-707·ref-767 을 ref-584 와 한 표준(IEC 62443-3-3:2013)으로 정리(f6), ref-172 를 config/source_mirrors.yaml 에 GitHub 위키 raw 경로로 등록(f1). |

## 용어 후보

- 없음

## 열린 질문

새로 생긴 질문:

- ref-637 이 가리키는 산업 디지털 전환 촉진법의 제명이 '산업 디지털 전환 및 인공지능 활용 촉진법'으로 바뀌어 시행되었는가, 바뀌었다면 데이터 공동 생성 규정의 조문 번호와 내용도 달라졌는가? | 관련 영역: 28. 표준·상호운용성·다사업자 거버넌스 | 근거: f4 | 종류: 일반

해결 제안(판정은 검증 에이전트):

- 없음

## 자체 점검

- 출처 수: 8 · 교차 확인: 0
- 예산 사용량: 검색 2회 · 신규 출처 0건
- 미확인 항목:
    - f4 제명 변경 법률의 시행 여부·시행일 미확인(원문 정책 차단)
    - ref-637 인코딩 URL 원문 미열람, 검색 결과 URL·제목 일치로만 확인
    - f5·f6 중복 판단은 참고문헌 목록 대조이며 각 URL 원문 미열람
- 범위 경계 위반 의심:
    - 없음
- 한계: 주간 정리: 신규 조사 없음, 신규 출처 0건. web_fetch_available: false · fetch_mode mirror_only 로 정책 차단 797건은 링크 오류가 아니어서 다시 열지 않았고, url_check 의 오류·미러 실패 3건만 점검했다. ref-172 는 source_mirrors.yaml 에 없는 GitHub 위키 raw 경로(raw.githubusercontent.com/wiki/…)로 열렸다. ref-412 미러는 오늘 열림(일시 오류). ref-637 은 검색 2회로 URL 존재만 확인했다. 검색 중 제명 변경 가능성이 드러났으나 새 사실 조사는 하지 않고 열린 질문으로 보냈다. 페이지 제안은 갱신 상한 2건에 맞췄고 ref-707·ref-767 정리와 ref-172 미러 등록은 다음 실행 후보로 남겼다. 운영 참고(파이프라인): 참고문헌 번호 ref-781~ref-791 이 비어 있고, 보류 실행 2026-09-25-100 은 run_id 가 스키마 패턴(끝 두 자리)에 맞지 않아 2026-09-25-00 으로 기록됐으며 그 브리프의 ref-748~ref-750 은 현재 참고문헌 목록의 같은 id(JSON Schema 계열)와 다른 문헌을 가리켜 재게시 시 id 재부여가 필요하다. 이전 주간 정리 2026-09-25-87 도 보류 상태다. link_check 는 통과(경고 0건).
