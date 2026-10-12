# 진행 상황

갱신: 2026-10-13. 기준 main `9c4de242d0f08ac8804707b7cc7787fbd261fef4`.
작업 브랜치 `codex/field-readiness-rop`. 전체 상태: 진행 중.

## 현재 위치

- 기준 커밋이 조사 시작 시 main HEAD임을 확인하고 지정 브랜치를 생성했다.
- 제공된 로컬 발표 정리를 읽었다. 원문을 저장소에 복사하지 않았다.
- 저장소 목록에서 지정 영역, 분리 페이지, 참고문헌, 최신 외부 조사와 시뮬레이터 코드 위치를 확인했다.
- 기존 위키 차이표 완료. 다음: 공개 원문 검증을 정리하고 02~08 및 sources.md 완성.
- 외부 원문 조사 진행 중: 프로토콜·SDK·법령·공식 연혁. 열람 실패는 sources.md에 기록한다.

## 파일 상태

|파일|상태|완료 내용/남은 일|
|---|---|---|
|README.md|완료|범위·기준·공개 원칙·인터넷 접근 기준|
|PROGRESS.md|갱신 중|파일별 커밋 시 동시 갱신|
|01_existing-wiki-gap-matrix.md|완료|24개 주제 대조, 기존 질문·트랙의 미완료 범위 확인|
|02_event-claim-verification.md|완료|발표 주장 16행, 날짜/법령/SDK 구별, 전사 미확인 유지|
|03_research-findings.md|완료|A~F, 조건부 능력·통신 계약·연속성·성과 정의|
|04_field-failure-cases.md|완료|일반화한 10사례·반증 시험·재현 패키지|
|05_decision-matrices.md|완료|10개 조건 측정표·3대안 판단·업종/책임/비용·인수 관문|
|06_simulation-validation-boundaries.md|완료|코드 4파일·6근거, 실패 5유형의 모델/관측/보정 경계|
|07_research-backlog.md|완료|15개 후속 질문, 기존 oq/트랙·담당·닫는 조건 연결|
|08_wiki-publication-map.md|완료|25개 기존 페이지·트랙·질문 연결 후보, 게시 없음|
|sources.md|진행 중|원문 위치·짧은 인용·버전·발행/접근일·실패 기록 수집|

## 재개 규칙

이 파일부터 읽고 마지막 커밋을 확인한다. main/claude 브랜치를 변경하지 않는다. 모든 변경 경로가 `rop-wiki/_work/research/field-readiness-rop/` 아래인지 확인한다. 발표 원문과 실명·비공개 수치를 추가하지 않는다. 파일 하나를 완성하면 해당 파일과 진행 상황을 한 커밋으로 남긴다. 코드나 시뮬레이션을 실행하지 않는다.

## 완료 이력

- 초기화: README.md 완료, 기준·범위·입력 확인.

- 01 완료: 24개 주제 대조; 기존 온톨로지 환경 조건·통신·복구·성과 조사 재사용.

- 02_event-claim-verification.md 완료: 발표 주장 16행, 날짜/법령/SDK 구별, 전사 미확인 유지。

- 03_research-findings.md 완료: A~F, 조건부 능력·통신 계약·연속성·성과 정의。

- 04_field-failure-cases.md 완료: 일반화한 10사례·반증 시험·재현 패키지。

- 05_decision-matrices.md 완료: 10개 조건 측정표·3대안 판단·업종/책임/비용·인수 관문。

- 06_simulation-validation-boundaries.md 완료: 코드 4파일·6근거, 실패 5유형의 모델/관측/보정 경계。

- 07_research-backlog.md 완료: 15개 후속 질문, 기존 oq/트랙·담당·닫는 조건 연결。

- 08_wiki-publication-map.md 완료: 25개 기존 페이지·트랙·질문 연결 후보, 게시 없음。
