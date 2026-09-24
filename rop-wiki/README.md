# ROP 연구 위키 (rop-wiki)

SCM(Supply Chain Management, 공급망 관리) 관점의 로봇 오케스트레이션 플랫폼(Robot Orchestration Platform, ROP) 연구 위키와, 그 위키를 매일 한 번 조사·검증·서술해 채우는 에이전트 파이프라인, 그리고 여러 세부영역을 가로지르는 중점 연구 트랙을 한 폴더에 담은 저장소다. 이 문서는 저장소 소개, 설치, 사이트 빌드, 수동 실행, 스케줄 등록·해제·확인, 검사, 사용자 개입 지점, 문제 해결, 커밋 방식을 다룬다. 실행 절차의 정본은 [`pipeline/RUN.md`](pipeline/RUN.md)이며, 이 문서의 실행·스케줄·문제 해결 절은 그 문서의 해당 절(2·4·5·6·7절)을 가리킨다.

모든 명령은 위키 루트 `rop-wiki/`(이 파일이 있는 폴더)에서 실행한다. 위키는 `ai-hub` git 저장소의 하위 폴더이며, 커밋은 그 저장소에 남는다(9절).

## 1. 저장소 소개

**위키.** 7개 대분류·28개 세부 연구영역을 뼈대로 하는 연구 위키다. 뼈대의 정본은 분류 원문 `_source/ROP_SCM_연구분야_분류.md`이며, 대분류·세부영역의 명칭·번호·정의·질문은 위키 어디서도 바꾸지 않는다. 원문에서 옮긴 문장에는 `[분류원문]` 태그가 붙고, 퍼블리셔의 원문 보호 검사가 글자 단위로 대조한다. 페이지는 홈, 소개 7, 대분류 7(A. 업무·공급망 설계 ~ G. 안전·보안·지능·거버넌스), 세부영역 28(1. 주문·업무 시스템 연계 ~ 28. 표준·상호운용성·다사업자 거버넌스, 시드 상태로 시작), 중점 연구 트랙 15, 횡단 페이지(용어집, 참고문헌, 표준·프레임워크 목록, 열린 질문, 물류 흐름 매트릭스, 변경 이력, 운영 지표, 정정 요청 안내), 운영 로그로 구성되며 mkdocs-material 정적 사이트로 빌드한다. 본문의 모든 주장은 `[사실]`/`[추정]`/`[의견]` 태그와 각주(`[^ref-003]`)를 갖고, 트랙 가설은 `[가설]`, 사용자 실험은 `[사용자 실험]`으로 표시한다. 표기를 읽는 법은 `docs/about/reading-guide.md`에 있다.

**파이프라인.** 매일 06:00(Asia/Seoul)에 `pipeline/run_daily.sh`가 리서치 에이전트 → 내용 검증 에이전트(1차) → 스토리텔러 에이전트 → 내용 검증 에이전트(2차) → 퍼블리셔 순으로 실행되어 그날의 연구영역(또는 트랙의 현재 단계)을 조사·검증·서술하고 위키에 반영한다. 세 에이전트는 `claude -p`(Claude Code CLI 헤드리스)로 실행되며, 프롬프트는 `agents/shared-rules.md` + `agents/<역할>.md` + 실행 컨텍스트 + 입력 파일 본문을 이어 붙인 텍스트 하나다. 에이전트는 파일을 직접 읽거나 쓰지 않고 `schemas/*.json`에 맞는 JSON 하나를 반환하며, 리서치·검증 에이전트는 WebSearch·WebFetch만, 스토리텔러는 도구 없이 실행된다. 퍼블리셔(`pipeline/publish.py`)는 LLM이 아닌 스크립트이며 스키마 검증 → 프런트매터 검증 → 원문 보호 검사 → 링크·각주 검사 → 반영 → 사이트 빌드 → 커밋 → 일일 로그 → 알림 순으로 실행하고, 하나라도 실패하면 반영하지 않는다. 검증을 통과하지 않은 산출물은 게시되지 않는다. 대상은 `config/rotation.yaml`이 정한다: 1주기는 1. 주문·업무 시스템 연계부터 28. 표준·상호운용성·다사업자 거버넌스까지 번호순 영역 심화, 2주기부터는 점수, 매 7번째 실행은 주간 정리, 매월 첫 실행은 월간 재검증, 주 2회(기본 화·금)는 트랙 실행이다. 독자용 설명은 `docs/about/agents.md`에 있다.

**중점 연구 트랙.** 첫 트랙 "매뉴얼 기반 로봇 기능 온톨로지"(`manual-capability-ontology`)는 로봇 매뉴얼과 기술 설명서 같은 비정형 문서를 온톨로지로 구조화해 ROP에서 로봇 기능을 활용하는 방법을 7단계(단계 1. 기존 능력 표현 모델과 표준 조사 → 단계 2. 로봇 문서 유형과 정보 구조 조사 → 단계 3. 비정형 문서에서 온톨로지를 추출하는 방법 조사 → 단계 4. 온톨로지를 실행에 연결하는 방법 조사 → 단계 5. 완전성과 정확성을 검증하는 방법 조사 → 단계 6. 변경 관리·운영·거버넌스 조사 → 단계 7. ROP 활용 시나리오 종합과 가설 판정)로 조사한다. 단계 이름은 `config/tracks/manual-capability-ontology.yaml`의 `stage_names`(사양서 8.1의 단계 제목)와 같으며, 표시할 때는 번호와 이름을 함께 쓴다. 중심은 5. 로봇 능력·작업 온톨로지이고, 9. 로봇·제조사 관제 연동, 21. 온보딩·설정·현장 시운전, 23. 시험·형식 검증·벤치마크, 24. 자산·소프트웨어 수명주기 관리, 27. AI·학습·적응과 모델 운영을 함께 다루며, 활용처로 8. 실시간 세계 상태·데이터 일관성, 12. 명령·작업 실행의 신뢰성, 13. 작업 배정 — MRTA, 25. 안전·위험 관리, 28. 표준·상호운용성·다사업자 거버넌스에 연결한다. 트랙은 분류를 바꾸지 않는다. 정의는 `config/tracks/manual-capability-ontology.yaml`, 페이지는 `docs/tracks/manual-capability-ontology/`, 질문 백로그의 원천은 `data/tracks/manual-capability-ontology/backlog.json`(시드 질문 `q1-01`부터 31건)이다. 트랙 실행 1회는 현재 단계의 열린 질문 1~3개에 답하고, 후속 질문을 백로그에 올리고, 온톨로지 초안 변경 여부와 단계 완료 조건을 평가하고, 트랙 로그에 기록한다.

### 1.1 저장소 구조

빌드 사양서 3장의 구조에 구축 중 추가된 파일(`data/`, `pipeline/lib/`, `pipeline/checks/`, 스케줄 스크립트, `schemas/examples/`)을 더한 실제 구조다.

```
ai-hub/                                   # git 저장소 루트 (Next.js 프로젝트). 퍼블리셔는 이 저장소에 커밋한다
└─ rop-wiki/                              # 위키 루트. settings.repo_path "./rop-wiki", settings.repo_root ".."
   ├─ README.md                           # 이 문서
   ├─ requirements.txt                    # mkdocs-material, pyyaml, jsonschema
   ├─ mkdocs.yml                          # pipeline/lib/nav.py 가 생성한다. 내비게이션은 사양서 4.8 순서로 고정. 손으로 고치지 않는다
   ├─ _source/ROP_SCM_연구분야_분류.md     # 분류 원문. 읽기 전용(pipeline/checks/source.sha256 로 변조를 검사한다)
   ├─ docs/                               # 위키 페이지 (mkdocs docs_dir)
   │  ├─ index.md                         # 홈
   │  ├─ about/                           # 소개 7페이지 (what-is-rop, scope-boundary, research-method, idea-mapping, agents, reading-guide, how-to-contribute)
   │  ├─ categories/<대분류 slug>/         # 대분류 index.md + 세부영역 NN-<slug>.md (폴더 7 · 파일 28)
   │  ├─ tracks/manual-capability-ontology/   # 트랙 개요, 단계 1~7, 온톨로지 초안, 모델·표준 비교표, 문서 유형 매트릭스, 평가 절차, 질문 백로그, 로그, 실험
   │  ├─ topics/                          # 주제 페이지 색인 + YYYY/YYYY-MM-DD-<slug>.md (2주기부터 생성)
   │  ├─ glossary/, references/, standards/   # 용어집(시드 13건), 참고문헌(ref-001 ~ ref-010), 표준·프레임워크 목록
   │  ├─ flow-matrix.md, open-questions.md, changelog.md, metrics.md, corrections.md   # 횡단 페이지
   │  └─ logs/                            # index.md + daily/YYYY-MM-DD.md, weekly/YYYY-Www.md (퍼블리셔가 생성)
   ├─ agents/                             # shared-rules.md, researcher.md, verifier.md, storyteller.md (파일 머리에 version)
   ├─ templates/                          # 페이지 템플릿 12종 + README.md
   ├─ schemas/                            # research/verification/pages .schema.json + examples/ + README.md
   ├─ config/                             # settings.yaml, rotation.yaml, priority.yaml, tracks/manual-capability-ontology.yaml, README.md
   ├─ data/                               # 퍼블리셔가 자동 갱신 영역을 다시 쓸 때 원천으로 삼는 JSON (open_questions, changelog, flow_matrix, tracks/<slug>/{backlog,log,ontology_versions})
   ├─ inbox/corrections.md                # 정정 요청함
   ├─ experiments/                        # 사용자 실험 결과 (README.md 에 폴더·서식 규칙)
   ├─ pipeline/
   │  ├─ RUN.md                           # 사람이 읽는 일일 실행 절차 (정본)
   │  ├─ run_daily.sh                     # 일일 실행 스크립트 (준비 → 대상 선정 → 리서치 → 1차 검증 → 스토리텔러 → 2차 검증 → 퍼블리셔 → 일일 로그)
   │  ├─ select_target.py                 # 대상 선정 → runs/<id>/target.json
   │  ├─ agent_runner.py                  # claude -p 호출 (probe: 웹 도구 점검, run: 에이전트 실행)
   │  ├─ publish.py                       # 퍼블리셔 (사양서 6.4 의 9단계)
   │  ├─ render_run_md.py, scaffold.py    # 실행 산출물 렌더링, 시드 페이지·자동 영역·mkdocs.yml 생성
   │  ├─ lib/                             # 공용 모듈 (runs, render, nav, frontmatter, source, verbatim, autoregion, paths, korean)
   │  ├─ checks/                          # run_all.sh, check_frontmatter.py, protect_source.py, check_links.py, check_urls.py, test_source.py, test_lib.py, source.sha256
   │  ├─ cron.example                     # cron 등록 예시 (CRON_TZ=Asia/Seoul, 0 6 * * *)
   │  └─ install_cron.sh, uninstall_cron.sh   # 스케줄 등록·해제
   ├─ runs/                               # 실행 산출물 (첫 실행 때 생성). runs/<DATE>-<NN>/, 보류 runs/parked/<DATE>-<NN>/, cron 출력 runs/cron.log
   └─ site/                               # mkdocs 빌드 결과 (git 무시)
```

실행 폴더 `runs/<DATE>-<NN>/`에는 `target.json`, `probe.json`, `docs_tree.txt`, `prompts/`(에이전트에 준 프롬프트와 응답), `research.json`·`research.md`, `verification.json`·`verification.md`, `pages/`·`pages.json`·`pages.md`, `verification2.json`·`verification2.md`, `log.md`, `timings.json`, `summary.json`, `build.log`가 남는다(주간 정리는 `link_check.txt`·`url_check.json`도).

## 2. 설치

### 2.1 요구 사항

| 항목 | 요구 | 비고 |
|---|---|---|
| 운영체제·셸 | Linux, bash | 스크립트는 `#!/usr/bin/env bash`이며 `set -euo pipefail`로 실행된다 |
| Python | 3.11 | `python3 --version`. 다른 인터프리터를 쓰려면 환경변수 `PYTHON`으로 지정한다(`PYTHON=/usr/bin/python3.11 bash pipeline/run_daily.sh`) |
| 파이썬 패키지 | `pyyaml`, `jsonschema`, `mkdocs`, `mkdocs-material` | `requirements.txt`. 외부 패키지를 더 요구하지 않는다 |
| Claude Code CLI | `claude` 실행 파일, 로그인 상태 | 에이전트 실행(`claude -p`)에 쓴다. 경로는 `config/settings.yaml`의 `claude_bin`(기본 `claude`) |
| git | 저장소 루트 `..`(ai-hub) | 퍼블리셔 7단계 커밋에 쓴다. `git_commit: false`면 필요 없다 |
| cron | `crontab` 명령(cronie 등) | 스케줄 등록에만 필요하다. 없으면 5절의 명령을 다른 스케줄러에 등록한다 |
| 네트워크 | 웹 검색 필수, 페이지 열람 권장 | 2.4절 |

### 2.2 파이썬 패키지

```bash
cd rop-wiki
python3 -m pip install -r requirements.txt
python3 -c "import yaml, jsonschema, mkdocs; print('ok')"
```

가상환경을 쓰면 cron 등록 시 `PATH`에 그 환경의 `bin`이 들어가야 한다. `install_cron.sh`는 `command -v claude mkdocs python3`로 찾은 디렉터리를 `PATH`에 넣으므로, 가상환경을 활성화한 셸에서 등록하면 된다.

### 2.3 Claude Code CLI 로그인

```bash
claude --version                      # 설치 확인 (구축 시 확인한 버전: 2.1.281)
claude auth status                    # 로그인 상태
claude auth login                     # 로그인이 필요하면
# 헤드리스 호출이 되는지 확인 (RUN.md 1절과 같은 명령)
echo 'Return {"ok":true}' | claude -p --output-format json \
  --json-schema '{"type":"object","properties":{"ok":{"type":"boolean"}},"required":["ok"]}' --tools ""
```

cron은 로그인 셸의 환경을 쓰지 않으므로, 사용자 계정의 로그인 상태가 cron 실행에서도 유지되는지 첫 등록 뒤 `runs/cron.log`로 확인한다. 장기 실행 환경에서는 `claude setup-token`으로 만든 장기 토큰 또는 환경변수 `ANTHROPIC_API_KEY`를 crontab에 두는 방법이 있다 [가정: 사양서는 인증 방식을 정하지 않는다. 어느 쪽을 쓸지는 운영 환경에 따른 사용자 결정 항목이다].

### 2.4 네트워크 요구

| 도구 | 필요 정도 | 없을 때 |
|---|---|---|
| 웹 검색(WebSearch) | 필수 | `config/settings.yaml`의 `web_tools_required: true`(사양서 0장)에 따라 준비 단계에서 즉시 중단하고 로그에 남긴다(exit 3) |
| 페이지 열람(WebFetch) | 필수 | 기본 설정 `web_fetch_required: true`(사양서 0장·7.3)에서는 준비 단계에서 즉시 중단하고 로그에 남긴다(exit 3). 네트워크 정책으로 열람이 막힌 환경에서만 사용자 override(`--allow-no-fetch`, 환경변수 `ROP_ALLOW_NO_FETCH=1`, 또는 설정 `web_fetch_required: false`)로 계속 진행할 수 있다. 이때 에이전트에 `web_fetch_available: false`를 알리고 로그에 "페이지 열람 불가 — 원문 미열람 모드(사용자 override)"를 남긴다. 에이전트는 출처 실재성을 검색 결과의 기관·제목·URL 일치로 확인하고, 모든 출처에 "원문 미열람"을 표시하며, 신뢰도 `high`를 주지 않는다(교차 확인돼도 `medium` 상한) |

점검 명령은 `python3 pipeline/agent_runner.py probe`다. `claude -p --tools WebSearch`로 검색 1회, `claude -p --tools WebFetch`로 `settings.web_fetch_probe_url`(기본 GS1 EPCIS 페이지) 열람 1회를 실제로 해 보고 `web_search_available`·`web_fetch_available`을 돌려준다. 셸 `curl` 결과는 `details.web_fetch_curl` 참고값일 뿐 판정에 쓰지 않는다(프록시 정책이 curl과 도구에 다르게 적용될 수 있다). 실행마다 같은 점검이 준비 단계에서 자동으로 돌고 결과는 `runs/<id>/probe.json`에 남는다.

에이전트 모델은 `config/settings.yaml`의 `model`(기본 `claude-opus-5-5`)이며 `agent_runner.py`가 `claude -p --model`로 넘긴다. 비우면 CLI 기본 모델을 쓴다.

### 2.5 설치 확인

```bash
bash -n pipeline/run_daily.sh && python3 -m py_compile pipeline/*.py pipeline/lib/*.py pipeline/checks/*.py   # 문법
python3 -c "import yaml,glob; [yaml.safe_load(open(p, encoding='utf-8')) for p in glob.glob('config/**/*.yaml', recursive=True)]; print('ok')"   # 설정
bash pipeline/checks/run_all.sh                  # 프런트매터 → 원문 보호 → 링크·각주 → 단위 테스트 → mkdocs build --strict (6절)
python3 pipeline/select_target.py --date 2026-09-25 --stdout    # 그날의 대상을 미리 본다(파일·부작용 없음)
```

## 3. 사이트 빌드·미리보기

```bash
mkdocs build --strict        # site/ 에 정적 사이트를 만든다. 경고도 실패로 취급한다(퍼블리셔 6단계와 같은 명령, settings.site_build_cmd)
mkdocs serve                 # 로컬 미리보기(기본 http://127.0.0.1:8000). 파일을 고치면 자동으로 다시 빌드한다
```

`mkdocs.yml`은 `pipeline/lib/nav.py`가 생성하므로 손으로 고치지 않는다. 페이지를 더하거나 뺀 뒤 내비게이션을 다시 만들려면 `python3 pipeline/scaffold.py --refresh-auto`를 실행한다(자동 갱신 영역과 `mkdocs.yml`만 다시 쓴다). `site/`는 `.gitignore`에 있어 커밋되지 않는다.

## 4. 수동 실행

정본: [`pipeline/RUN.md`](pipeline/RUN.md) 2절(명령·옵션), 3절(단계별 읽고 쓰는 파일), 4절(재시도·보류 규칙), 5절(`--resume` 사용법).

### 4.1 명령 예

```bash
bash pipeline/run_daily.sh                                        # 오늘(settings.timezone) 정규 실행: 대상 선정 규칙대로
bash pipeline/run_daily.sh --date 2026-09-24 --run-type area_deep_dive --area 7     # 드라이런: 7. 화물·재고·자산 식별과 추적 영역 심화
bash pipeline/run_daily.sh --run-type track --track manual-capability-ontology --stage 1                     # 트랙 드라이런: 단계 1. 기존 능력 표현 모델과 표준 조사 (질문은 백로그에서 자동 선택)
bash pipeline/run_daily.sh --run-type track --track manual-capability-ontology --stage 1 --question-ids q1-01,q1-02   # 다룰 질문 지정
bash pipeline/run_daily.sh --run-type weekly_review               # 주간 정리만 따로
bash pipeline/run_daily.sh --resume 2026-09-24-01                 # 있는 산출물부터 이어서(보류 폴더면 되돌려 재투입)
bash pipeline/run_daily.sh --resume 2026-09-24-01 --step publish  # 한 단계만
bash pipeline/run_daily.sh --no-build --no-commit                 # 빌드·커밋 없이(시험)
bash pipeline/run_daily.sh --allow-no-fetch                       # 페이지 열람이 막힌 환경에서 원문 미열람 모드로 진행(사용자 override)
ROP_ALLOW_NO_FETCH=1 bash pipeline/run_daily.sh                   # 같은 override 를 환경변수로(cron 줄에 넣을 때)
bash pipeline/run_daily.sh --help
```

사양서 9장 단계 3의 드라이런 두 번은 위 둘째·셋째 명령이다. `--date`를 주면 그 날짜가 실행 id·페이지 `updated`·접근일이 된다.

### 4.2 옵션

| 옵션 | 뜻 |
|---|---|
| `--date YYYY-MM-DD` | 실행 날짜. 기본은 `settings.timezone`의 오늘. 환경변수 `ROP_TODAY`와 같다 |
| `--run-type T` | 실행 유형을 지정한다. 값: `area_deep_dive`(영역 심화) · `topic`(주제 조사) · `update`(갱신) · `weekly_review`(주간 정리) · `monthly_recheck`(월간 재검증) · `track`(트랙 실행) |
| `--area N` | 대상 세부영역 번호(1~28) |
| `--track S` | 트랙 slug(예 `manual-capability-ontology`) |
| `--stage N` | 트랙 단계(1~7) |
| `--question-ids a,b` | 이번에 다룰 백로그 질문 id(쉼표 구분. 사양서 8.2의 1~3개 규칙은 자동 선택에만 적용되며 지정한 id의 개수는 검사하지 않으므로 3개 이하로 준다) |
| `--run-id ID` | 실행 id를 지정한다. 기본 `<date>-<NN>` 자동 부여(같은 날 두 번째는 `-02`) |
| `--resume ID` | `runs/<ID>/`(또는 `runs/parked/<ID>/`)의 산출물이 있는 단계는 건너뛰고 다음 단계부터 이어간다. 보류 폴더는 `runs/<ID>/`로 되돌리고 `summary.json`의 보류 표시를 지운다 |
| `--step S` | 단일 단계만 실행한다. 값: `prepare` · `select` · `research` · `verify1` · `storytell` · `verify2` · `publish` · `log`. `prepare`·`select` 외에는 `--resume`(또는 `--run-id`)이 필요하다 |
| `--skip-probe` | 드라이런 전용. 웹 도구 점검을 생략한다(기존 `probe.json` 재사용, 없으면 WebSearch 는 점검하지 않고 `web_search_available: null`과 "웹 도구 점검 생략(드라이런)"을 기록하며, WebFetch 는 curl 참고값만 쓴다) |
| `--allow-no-fetch` | 사용자 override. 페이지 열람 도구를 쓸 수 없어도 중단하지 않고 원문 미열람 모드로 진행한다. 환경변수 `ROP_ALLOW_NO_FETCH=1`과 같다 |
| `--no-build` | 퍼블리셔 6단계(사이트 빌드)를 건너뛴다(8단계의 재빌드도) |
| `--no-commit` | 퍼블리셔 7단계(커밋)를 건너뛴다(커밋 해시 기록 커밋도) |
| `-h`, `--help` | 사용법 |

`--run-type`을 주면 대상 선정 규칙 대신 그 값을 쓰고 `target.json`에 `forced: true`가 기록된다. `--area`·`--track`·`--stage`·`--question-ids`는 `--run-type`(또는 트랙 실행일의 트랙 선정)과 함께 줄 때만 반영되며, 단독으로 주면 무시되고 정규 선정 규칙대로 대상이 정해진다.

### 4.3 종료 코드와 결과 확인

| exit | 뜻 |
|---|---|
| 0 | 완료(게시) 또는 `--step`으로 지정한 단계 완료 |
| 2 | 옵션·설정 오류, 재개할 실행 폴더 없음, 또는 보류(`runs/parked/<id>/`로 이동) |
| 3 | 준비 단계 즉시 중단(웹 검색 도구 없음, override 없이 페이지 열람 도구 없음 등). 중단 로그는 커밋된다 |
| 4 | 퍼블리셔 실패(검사 실패·빌드 실패·커밋 실패). 되돌린 상태의 실패 일일 로그(`(중단)`)를 커밋한다. 고친 뒤 `--resume <id> --step publish` |
| 그 밖의 값 | 단계 스크립트(`select_target.py`, `agent_runner.py probe`, `pipeline/lib/runs.py` 등)가 낸 실패 코드를 `run_daily.sh`의 실패 트랩(`trap … ERR` → `exit "$rc"`)이 그대로 전파한 것이다(예: `select_target.py`가 대상을 정하지 못하면 1). 원인은 `runs/<id>/log.md`의 "실패: 단계 <단계> (run_daily.sh 줄 N, exit N)" 줄과 `summary.json`의 `end_state`에서 본다(실행 폴더가 만들어지기 전에 실패하면 표준 출력, cron이면 `runs/cron.log`에만 남는다). 고친 뒤 `--resume <id>` |

결과는 `runs/<id>/log.md`(단계별 진행), `summary.json`(`end_state`, `published`, `parked`, 소요 시간), `research.md`·`verification.md`·`pages.md`·`verification2.md`(사람이 읽는 산출물), `docs/logs/daily/<date>.md`(일일 로그: 단계별 결과와 소요 시간, 검증 판정, 생성·갱신 페이지, 예산 사용량, 다음 실행 메모)에서 본다. 게시되면 `docs/changelog.md`, 홈·대분류·세부영역의 "최근 업데이트", 트랙 실행이면 트랙 로그·질문 백로그·온톨로지 초안이 함께 갱신된다.

### 4.4 부분 도구

```bash
python3 pipeline/select_target.py --date 2026-09-25 --stdout      # 대상 미리 보기
python3 pipeline/agent_runner.py probe                             # 웹 도구 점검
python3 pipeline/agent_runner.py run --role researcher --run-id 2026-09-24-01 --dry-run   # 프롬프트만 만들어 runs/<id>/prompts/ 에 저장
python3 pipeline/publish.py 2026-09-24-01 --check-only             # 퍼블리셔 1단계(스키마·판정 확인)만
python3 pipeline/publish.py 2026-09-24-01 --dry-run                # 1~4단계까지 하고 되돌림
python3 pipeline/lib/runs.py unpark --run-id 2026-09-24-01         # 보류 산출물 재투입(--resume 이 자동으로 한다)
python3 pipeline/render_run_md.py 2026-09-24-01                    # research.md 등 다시 렌더링
```

## 5. 스케줄 등록·해제·확인

정본: [`pipeline/RUN.md`](pipeline/RUN.md) 6절. 스케줄러는 cron이고 실행 시각은 매일 06:00 Asia/Seoul(사양서 0장 `run_time: "06:00 Asia/Seoul"`)이다. 예시 파일은 [`pipeline/cron.example`](pipeline/cron.example)이다.

**현재 상태(2026-09-24).** 구축 환경에는 `crontab` 명령이 없어 등록 블록은 `bash pipeline/install_cron.sh --dry-run`으로만 확인했고 스케줄은 미등록이다(`bash pipeline/uninstall_cron.sh`는 "crontab 명령이 없다"로 exit 1). 운영 환경에서 `bash pipeline/install_cron.sh`로 등록하고 `crontab -l`로 확인한다. 어느 환경·스케줄러에 등록할지는 완료 보고서(사양서 11장)의 사용자 결정 항목이다.

| 할 일 | 명령 | 설명 |
|---|---|---|
| 등록 | `bash pipeline/install_cron.sh` | `config/settings.yaml`의 `run_time`을 읽어 HH:MM → 시각(`06:00 Asia/Seoul` → `0 6 * * *`), `run_time`에 적힌 시간대(없으면 `timezone`) → `CRON_TZ`로 삼아 crontab에 `# rop-wiki:begin` ~ `# rop-wiki:end` 마커 블록을 넣는다. 이미 있으면 그 블록만 바꾸고 다른 항목은 건드리지 않는다. `claude`·`mkdocs`·`python3`가 있는 디렉터리를 `PATH` 줄에 넣는다 |
| 등록 내용 미리 보기 | `bash pipeline/install_cron.sh --dry-run` | crontab을 바꾸지 않고 블록만 출력한다 |
| 시각·시간대 덮어쓰기 | `bash pipeline/install_cron.sh --schedule "0 7 * * *" --tz UTC` | 설정과 다르게 등록할 때. 보통은 0장 설정(`run_time`)을 바꾸고 다시 등록한다 |
| 확인 | `crontab -l` | 마커 사이가 등록 블록이다. 실행 출력은 `runs/cron.log`에 누적되고, 실행별 상세는 `runs/<DATE>-<NN>/log.md`, 일일 로그는 `docs/logs/daily/<DATE>.md` |
| 해제 | `bash pipeline/uninstall_cron.sh` | 마커 사이의 줄만 지운다(`--dry-run`으로 미리 보기). 블록이 없으면 그렇다고 알린다 |

등록되는 블록. 위키 루트 경로와 `PATH` 줄은 등록하는 환경에서 찾은 값으로 채워진다(아래는 구축 환경에서 `bash pipeline/install_cron.sh --dry-run`으로 얻은 출력 그대로이며, 다른 환경에서는 `cd` 뒤의 경로와 `PATH` 값이 달라진다):

```cron
# rop-wiki:begin (pipeline/install_cron.sh 가 관리한다. 손으로 고치지 말고 install/uninstall_cron.sh 를 쓴다)
CRON_TZ=Asia/Seoul
PATH=/opt/node22/bin:/usr/local/bin:/usr/bin:/bin
0 6 * * * cd /home/user/ai-hub/rop-wiki && /usr/bin/env bash pipeline/run_daily.sh >> runs/cron.log 2>&1
# rop-wiki:end
```

- `CRON_TZ`는 cronie 계열 cron이 지원하는 시간대 지정이다. 지원하지 않는 cron이면 이 줄을 지우고 서버 시간대로 시각을 환산한다(UTC 서버면 `0 21 * * *` = 전날 21:00 UTC = 06:00 KST).
- `crontab` 명령이 없으면 `install_cron.sh`가 exit 1로 끝나며 등록할 명령 한 줄을 출력한다. 그 줄을 n8n·GitHub Actions 등 다른 스케줄러에 등록한다.
- 같은 날 두 번 실행되면 실행 id가 `<DATE>-02`로 붙는다. 실패한 실행을 다시 하려면 새 실행이 아니라 `--resume <run_id>`를 쓴다.
- 손으로 넣으려면 `crontab -e`에서 `cron.example`의 주석이 아닌 세 줄(`CRON_TZ`, `PATH`, 실행 줄)을 붙여 넣고 경로와 `PATH`를 바꾼다(`cron.example` 머리 주석에 "아래 네 줄"이라 적힌 것은 오기이며 세 줄이 맞다).

## 6. 검사 스크립트

```bash
bash pipeline/checks/run_all.sh              # 프런트매터 → 원문 보호(내비 재생성 일치 포함) → 링크·각주 → 파서 단위 테스트 → 라이브러리 단위 테스트 → mkdocs build --strict
bash pipeline/checks/run_all.sh --no-build   # 빌드 제외
ROP_CHECK_URLS=1 bash pipeline/checks/run_all.sh   # 외부 접속이 되는 환경에서 참고문헌 URL 열림 확인까지(결과 data/url_check.json)
python3 pipeline/scaffold.py --apply-url-check     # 열림이 확인된 참고문헌의 신뢰도를 유형 기준값으로 올린다(원문 미열람 medium 상한 해제)
```

| 검사 | 스크립트 | 무엇을 보는가 |
|---|---|---|
| 프런트매터 | `pipeline/checks/check_frontmatter.py` | 모든 `docs/**/*.md`의 필수 필드(`title, type, status, created, updated, version` + 유형별 필수), 허용 값, 날짜 형식, 본문 첫 줄이 이동 경로(`홈 › …`)인지 |
| 원문 보호 | `pipeline/checks/protect_source.py` | 세부영역 28·대분류 7·홈·소개 페이지의 `[분류원문]` 문장과 명칭·번호·정의·질문을 `_source/` 원문과 글자 단위로 대조, `mkdocs.yml` 내비게이션이 4.8 순서와 같은지, 원문 파일의 해시(`source.sha256`) |
| 링크·각주 | `pipeline/checks/check_links.py` | 상대 경로 링크의 파일 존재, `[^id]` 참조마다 정의가 있는지 |
| 단위 테스트 | `pipeline/checks/test_source.py`, `test_lib.py` | 원문 파서와 공용 모듈 |
| URL 열림(선택) | `pipeline/checks/check_urls.py [--strict] [--json 경로]` | 참고문헌 프런트매터 `url`에 HEAD/GET 요청. 기본 exit 0, `--strict`면 열리지 않는 항목이 있을 때 exit 1 |
| 사이트 빌드 | `mkdocs build --strict` | 깨진 링크·내비게이션 경고를 실패로 취급 |

퍼블리셔는 같은 검사를 실행마다 2~4·6단계에서 수행한다. 사람이 페이지·템플릿·설정을 직접 고쳤을 때는 커밋 전에 `run_all.sh`를 돌린다.

## 7. 사용자 개입 지점

사양서 7.4의 일곱 지점이다. 어느 것이든 페이지 본문을 직접 고치는 대신 정해진 파일에 적으면 다음 실행에서 에이전트가 근거를 확인하고 결과가 변경 이력에 남는다. 독자용 설명은 `docs/about/how-to-contribute.md`, 설정 항목 설명은 `config/README.md`에 있다.

| 지점 | 파일 | 하는 일 | 반영 시점 |
|---|---|---|---|
| 우선순위 지정 | `config/priority.yaml`의 `areas`·`topics`·`questions` | 먼저 다룰 세부영역(`area_no`, `weight`, `reason`), 주제(`title`, `area_no`, `weight`), 질문(`question`, `area_no`)을 적는다. 네 키는 빈 목록이라도 모두 있어야 한다 | 다음 대상 선정에서 순환보다 우선한다. 최근 7일 안에 다룬 항목은 건너뛴다(`rotation.priority.skip_if_targeted_within_days`) |
| 트랙 질문 | `config/priority.yaml`의 `track_questions` | 트랙 백로그에 넣을 질문(`track`, `stage`, `question`, `priority: high/normal/low`) | 퍼블리셔가 제기 근거 "사용자"로 백로그에 등록하고, 다음 트랙 실행에서 사용자 지정 질문으로 가장 먼저 다룬다 |
| 정정 요청 | `inbox/corrections.md` | `## corr-NNN` 블록에 페이지, 문제 문장, 근거, 요청일, 요청자, 상태(`open`)를 적는다. 형식·거부 사유는 `docs/corrections.md` | 다음 실행에서 그 페이지의 갱신이 당일 작업에 들어가고, 1차 검증 항목 11로 확인되며, 퍼블리셔가 반영된 요청(검증 결과의 `corrections_applied`)의 상태를 `applied`로 바꾸고 처리 실행·처리 메모 줄을 덧붙인 뒤 변경 이력에 남긴다. 반영하지 않기로 판정된 요청을 `rejected`로 바꾸는 처리는 현재 미구현이며 그 요청은 `open`으로 남는다 [가정: 퍼블리셔·검증 스키마 담당에게 `corrections_rejected` 필드와 처리 추가를 요청한다. 그때까지는 사람이 `inbox/corrections.md`의 상태 줄을 직접 `rejected`로 바꾸고 처리 메모에 사유를 적는다] |
| 보류 산출물 | `runs/parked/<실행 id>/` | 1차 반려 또는 2차 불통과가 재시도(`max_retries`, 기본 2회) 뒤에도 이어지거나 스키마 불일치가 재실행 뒤에도 남으면 실행 폴더가 통째로 옮겨진다. `log.md`·`verification.md`·`verification2.md`의 사유와 `research.md`·`pages/`를 검토한다 | 재투입은 `bash pipeline/run_daily.sh --resume <실행 id>`(걸렸던 단계부터 다시 진행). 폐기는 `runs/parked/<실행 id>/DISCARDED` 파일에 날짜와 사유 한 줄. 같은 영역이 3회 연속 보류되면 대상 선정에서 제외되고 열린 질문에 검토 요청이 올라간다. `priority.yaml`의 `areas`에 지정하면 제외가 풀린다 |
| 에이전트 규칙 변경 | `agents/shared-rules.md`, `researcher.md`, `verifier.md`, `storyteller.md` | 파일 머리 3행의 `version: <major>.<minor> (<날짜>)`를 올리고(규칙 추가·삭제는 major, 문구·서식은 minor [가정]), `data/changelog.json`의 `items`에 `{"date", "run_id": "manual-<날짜>", "action": "갱신", "page": "agents/<파일>", "summary"}`를 더한다. 절차는 `RUN.md` 8.1절 | 프롬프트는 파일 전문을 그대로 붙이므로 다음 실행부터 적용된다. 어느 실행이 어느 버전으로 돌았는지는 `runs/<id>/prompts/`로 추적한다. 사용자 확인 없이 규칙을 완화하지 않는다 |
| 실험 결과 | `experiments/<YYYY-MM-DD>-<slug>/` | 사용자가 직접 수행한 실험의 `README.md`(트랙·단계·답하려는 질문·목적·방법·결과 요약·한계)와 데이터 파일을 둔다. 서식은 `experiments/README.md` | 다음 트랙 실행에서 리서치 에이전트가 읽어 `[사용자 실험]` 태그로 반영한다. `[사실]`로 올라가려면 내용 검증 에이전트의 판정이 필요하다 |
| 구축 멈춤 지점 | `config/settings.yaml`의 `checkpoints` | `true`(기본)면 구축 순서(사양서 9장)의 두 지점 — 단계 1 뼈대 생성 뒤(구조·소개 페이지·원문 보호 검사 결과), 단계 3 드라이런 두 번 뒤(산출물·소요 시간·예산 사용량) — 에서 사용자 확인을 받는다 | 구축 절차에만 쓰이며 일일 실행 스크립트는 이 값을 읽지 않는다(`RUN.md` 8.2절) |

구축 시 확인한 에이전트 파일 버전(2026-09-24): `shared-rules.md` 1.1, `researcher.md` 1.1, `verifier.md` 1.3, `storyteller.md` 1.3.

## 8. 문제 해결

정본: [`pipeline/RUN.md`](pipeline/RUN.md) 7절(증상별 확인·조치), 4절(재시도·보류 규칙), 5절(`--resume`). 아래는 사양서 7.3의 실패 처리와 자주 만나는 증상을 표로 모은 것이다.

| 증상 | 원인·확인 | 조치 |
|---|---|---|
| `web_search_available: false`로 준비 단계 중단(exit 3, 로그 "즉시 중단: 웹 검색(WebSearch) 도구를 쓸 수 없다(web_tools_required)") | 웹 검색 도구 없음(사양서 7.3 "즉시 중단·로그"). `settings.web_tools_required: true` | `claude -p --tools WebSearch`가 동작하는지, 네트워크 정책이 검색을 막는지 확인한다. `runs/<id>/probe.json`의 `details.web_search` 참고. 복구 뒤 `--resume <id>`(준비 단계부터 다시 점검한다) |
| "즉시 중단: 페이지 열람(WebFetch) 도구를 쓸 수 없다"(exit 3) / override 로 계속된 실행 / curl로는 열리는데(또는 반대) | 페이지 열람 차단. 판정은 `claude -p --tools WebFetch` 결과이고 셸 curl은 참고값(`probe.json`의 `details.web_fetch` vs `details.web_fetch_curl`) | 기본은 중단이다(2.4절). 열람이 막힌 환경이면 `--allow-no-fetch`(또는 `ROP_ALLOW_NO_FETCH=1`)로 원문 미열람 모드를 쓴다. 이때 모든 출처에 "원문 미열람"이 붙고 신뢰도 `high`가 없다. 열람이 되는 환경에서 `ROP_CHECK_URLS=1 bash pipeline/checks/run_all.sh` → `python3 pipeline/scaffold.py --apply-url-check`로 참고문헌 신뢰도를 올린다 |
| 일일 로그 "예산 사용량" 표에 초과·도달 표시 | 리서치 결과의 `self_check.budget_used`가 `target.json`의 예산(`daily_budget.max_search_queries`·`max_sources_per_run`, 트랙은 `track_max_*`)에 닿음. 사양서 7.3 "부분 결과로 진행하되 로그에 표시" | 실행은 부분 결과로 게시된다. 반복되면 `config/settings.yaml`의 `daily_budget`을 조정하거나 `priority.yaml`에 질문을 좁혀 적는다 |
| 로그 "스키마 불일치" 뒤 보류(`runs/parked/`) | 에이전트 반환 JSON이 `schemas/*.json`을 통과하지 못했다. 사양서 7.3대로 `## 스키마 불일치 (재실행)` 절을 붙여 1회 재실행한 뒤에도 실패 | `runs/parked/<id>/prompts/*.response.json`(`research`·`verification1`·`storyteller`·`verification2`)과 `log.md`의 오류 목록을 본다. 프롬프트·스키마를 고쳤으면 `--resume <id>`(걸린 단계부터). 스키마 자체를 바꿨으면 `schemas/README.md`의 예시 검사도 다시 돌린다 |
| `claude 오류 응답: API Error 400 … input_schema does not support oneOf/allOf`, `--json-schema is not a valid JSON Schema`, `strict mode: missing type` | `agent_runner.py`가 스키마를 CLI용으로 바꾸지 못한 경우 | `schemas/*.json`을 고쳤다면 최상위 `allOf/oneOf/anyOf`를 쓰지 말고 `pipeline/lib/runs.py`의 `cli_schema()`(`$schema`·`$id`·`$defs` 제거, 하위 스키마 `type` 보충)를 확인한다 |
| 1차 검증 반려·2차 불통과가 `max_retries`(기본 2회) 뒤에도 이어져 보류(exit 2) | `verification.md`·`verification2.md`의 반려 사유·수정 지시 | 7절 "보류 산출물"대로 검토한 뒤 `--resume <id>` 또는 폐기(`DISCARDED`). 직전 판정은 `verification.attemptN.json`·`verification2.attemptN.json`에 남는다 |
| 같은 영역이 3회 연속 보류 | 사양서 7.3. 대상 선정(`rotation.exclude_after_consecutive_parks: 3`)에서 그 영역이 제외되고 `data/open_questions.json`에 사용자 검토 요청이 올라간다 | 열린 질문의 검토 요청을 읽고 `runs/parked/`를 정리한다. 다시 다루게 하려면 `config/priority.yaml`의 `areas`에 그 영역을 지정한다(제외 해제, 바로 다음 실행부터 선정 가능). 보류된 실행은 최근 7일 감점·건너뜀 집계에 세지 않는다. 재투입해 게시까지 가면 연속 보류 횟수에 세지 않는다 |
| `mkdocs build --strict` 실패(퍼블리셔 6단계, exit 4) | 보통 내비게이션·링크·앵커 경고. `runs/<id>/build.log` | 사양서 6.4·7.3대로 5단계 반영은 스냅숏(`runs/<id>/backup/`)으로 되돌려져 있고 커밋은 없다. 원인을 고친 뒤 `--resume <id> --step publish`. 앵커 오류는 `RUN.md` 7절의 "4단계 제목 앵커 검사" 항목 참고 |
| 확정 로그 재빌드 실패(퍼블리셔 8단계) | `runs/<id>/build-final.log`, `summary.json`의 `final_log_rebuild_failed` | 8단계는 7단계 커밋 전에 돈다. 재빌드가 실패하면 확정 일일 로그 대신 예비 일일 로그가 커밋에 들어간다. 원인 수정 뒤 `--resume <id> --step log` |
| 퍼블리셔 2·3·4단계 검사 실패(참고문헌 id 충돌, 온톨로지 버전 불일치, `replaced_by` 없음, 원문 보호 diff, 깨진 링크·각주) | 스토리텔러 산출물 `runs/<id>/pages/`·`pages.json`의 문제. 반영 전이라 되돌릴 것은 없다 | `pages/`를 고쳐 `--resume <id> --step publish`. `[분류원문]` 문장·절 제목을 바꾼 경우는 원문대로 되돌린다 |
| `claude 실행 파일을 찾을 수 없다` | cron이면 `PATH` 줄, 셸이면 `which claude` | `install_cron.sh`가 넣은 `PATH`를 확인하거나 `settings.claude_bin`에 절대 경로를 적는다 |
| claude 인증 오류(`claude -p` 응답이 `is_error: true`이고 로그인·인증 관련 문구) | 로그인 만료, cron 환경에서 자격 증명을 읽지 못함 | `claude auth status` → `claude auth login`. cron에서는 2.3절의 장기 토큰(`claude setup-token`) 또는 `ANTHROPIC_API_KEY`를 crontab 환경에 둔다 [가정]. 고친 뒤 `--resume <id>` |
| 에이전트 호출 시간 초과·턴 초과 | `settings.agent_timeout_sec`(기본 1800초), `max_turns`(리서치 60·검증 40·스토리텔러 8) | 값을 올리거나 예산을 줄인다. 재실행은 `--resume <id> --step <단계>` |
| 설정 파일을 읽을 수 없어 중단(exit 2) | `config/*.yaml`이 `yaml.safe_load`로 읽히지 않음 | 2.5절의 설정 확인 명령으로 오류 위치를 찾는다. `priority.yaml`은 네 키가 모두 있어야 한다 |
| git 커밋 실패(퍼블리셔 7단계, exit 4) | identity 없음, 저장소 잠금 등 | 파일은 반영된 채 남고 빌드는 성공한 상태다. identity가 없으면 스크립트가 임시 identity로 커밋하므로 다른 원인을 `runs/<id>/log.md`에서 본다. 고친 뒤 `--resume <id> --step publish` |
| `crontab` 명령이 없다 | cron 미설치 | cron(cronie 등)을 설치하거나 `install_cron.sh`가 출력한 명령을 다른 스케줄러에 등록한다 |
| 정정 요청이 다뤄진 실행 뒤에도 `inbox/corrections.md`의 상태가 `open`이다 | 퍼블리셔는 검증 결과의 `corrections_applied`에 든 id만 `applied`로 바꾼다. 반영하지 않기로 판정된 요청을 `rejected`로 바꾸는 처리는 미구현이다(7절 "정정 요청") | `runs/<id>/verification.md`의 항목 11 판정과 `verification2.md`를 보고, 반영하지 않을 요청이면 상태 줄을 직접 `rejected`로 바꾸고 처리 메모에 사유를 적는다 [가정] |
| 같은 날 실행이 두 개 | 실행 id `-02` | 정상이다. 일일 로그에 실행 블록이 최신순으로 추가된다 |
| 산출물이 어디 있는지 | — | `runs/<id>/research.md`, `verification.md`, `verification2.md`, `pages.md`, `log.md`, `summary.json`; 사이트는 `site/` 또는 `mkdocs serve` |

## 9. ai-hub 저장소의 하위 폴더와 커밋 방식

이 위키는 `ai-hub`(Next.js 프로젝트) git 저장소의 하위 폴더 `rop-wiki/`다. `config/settings.yaml`의 `repo_root: ".."`가 저장소 루트, `repo_path: "./rop-wiki"`가 루트에서 본 위키 폴더다. 위키의 스크립트는 `ai-hub`의 다른 파일을 읽거나 쓰지 않는다.

**퍼블리셔의 커밋(자동).** 퍼블리셔 7단계는 저장소 루트에서 `git commit -- <경로>`로 `rop-wiki/docs`·`data`·`config`·`mkdocs.yml`·`inbox`·`runs/<run_id>`·`runs/parked/<run_id>`만 담아 현재 브랜치에 커밋한다. 사용자가 다른 파일을 스테이지해 두었어도 섞지 않지만, 이 경로 안의 미커밋 변경은 그 실행이 바꾼 파일이 아니어도 함께 들어간다. 확정 일일 로그·`summary.json`·퍼블리셔 단계 기록은 커밋 전에 모두 쓰므로 실행 뒤 미커밋 파일이 남지 않는다(amend 없음). 커밋은 자기 해시를 담을 수 없어서, 바로 뒤에 `summary.json`의 `commit` 필드만 바꾸는 작은 커밋 `run(DATE): 커밋 해시 기록 <id> → <hash>`를 하나 더 만든다. [가정] 메시지 형식은 사양서 6.4대로 `run(DATE): <실행 유형> <대상 영역 이름> — 생성 n/갱신 n`이다(예 `run(2026-09-24): 영역 심화 7. 화물·재고·자산 식별과 추적 — 생성 0/갱신 1`). 주간 정리는 대상 영역 자리에 ISO 주(`2026-W40`), 트랙 실행은 트랙·단계·질문 id를 본문 둘째 줄에 둔다. 보류·중단된 실행도 일일 로그를 커밋하며 제목 끝에 `(보류)` 같은 종료 상태를 괄호로 붙인다. `git config user.name`이 없으면 임시 identity("ROP 연구 위키 퍼블리셔")로 커밋한다. 원격 푸시는 `git_push: true`일 때만 하며 기본은 하지 않는다. 커밋 자체를 끄려면 `git_commit: false` 또는 `--no-commit`.

**사람의 커밋.** 퍼블리셔가 스테이지하지 않는 파일(`agents/`, `templates/`, `schemas/`, `pipeline/`, `experiments/`, `README.md`, `requirements.txt`)과 사용자가 고친 `config/`·`inbox/`는 사람이 직접 커밋한다. 다만 `config/`·`inbox/`의 미커밋 변경은 퍼블리셔가 다음 실행 커밋(`run(DATE): …`)에 함께 스테이지하므로, 실행 커밋과 분리해 남기려면 실행 전에 직접 커밋한다(보류·중단 실행의 일일 로그 커밋도 같은 경로를 스테이지한다). 메시지는 기존 이력과 같이 `<유형>(rop-wiki): <요약>` 형식을 쓴다(예 `docs(rop-wiki): 분류 원문(_source) 추가`) [가정: 사양서는 사람 커밋의 형식을 정하지 않는다]. 커밋 전에 `bash pipeline/checks/run_all.sh`를 돌린다.

**커밋되는 것과 안 되는 것.** `runs/<DATE>-<NN>/`은 재현을 위해 커밋한다(`.gitignore`에서 무시하지 않으며 `prompts/`도 남긴다). `runs/cron.log`는 퍼블리셔의 스테이지 대상이 아니므로 커밋되지 않는다 [가정: cron 출력은 기록이 아니라 운영 로그로 보고 커밋하지 않는다]. `site/`(빌드 결과)와 `__pycache__/`는 `.gitignore`에 있다. `_source/ROP_SCM_연구분야_분류.md`는 읽기 전용이며 바꾸면 `pipeline/checks/protect_source.py`의 해시 검사가 실패한다.

## 10. [가정] 목록

사양서에 없어 이 문서가 정한 것이다. 바꿔도 사양서와 어긋나지 않는다.

- cron 환경의 Claude 인증 방식(`claude setup-token` 장기 토큰 또는 `ANTHROPIC_API_KEY`)은 사용자 결정 항목이다. 사양서는 로그인 방식을 정하지 않는다.
- 에이전트 파일 버전 규칙(규칙 추가·삭제는 major, 문구·서식은 minor)과 변경 이력의 `run_id: manual-<날짜>`는 `pipeline/RUN.md` 8.1절의 가정을 따른다.
- 사람이 직접 커밋할 때의 메시지 형식 `<유형>(rop-wiki): <요약>`은 기존 커밋 이력에서 가져온 것이다.
- `runs/cron.log`는 커밋하지 않는다.
- 페이지 열람 차단 시의 override(`--allow-no-fetch`, `ROP_ALLOW_NO_FETCH=1`, `web_fetch_required: false`)는 사양서에 없는 예외다. 기본값은 사양서대로 중단(`web_fetch_required: true`)이다.
- 실행마다 실행 커밋과 커밋 해시 기록 커밋, 두 개가 생긴다. 실행 커밋 하나만 원하면 `summary.json`의 `commit`을 비워 두는 방식으로 바꿀 수 있다.
- 정정 요청을 `rejected`로 바꾸는 퍼블리셔 처리는 미구현이다(`pipeline/publish.py`는 `corrections_applied`만 다룬다). 구현될 때까지 반영하지 않을 요청은 사람이 상태 줄을 직접 바꾼다. 퍼블리셔·검증 스키마 담당에게 `corrections_rejected` 필드와 처리 추가를 요청한다.

## 11. 관련 문서

- [`pipeline/RUN.md`](pipeline/RUN.md) — 일일 실행 절차 정본(준비물, 명령·옵션, 단계별 파일, 재시도·보류, `--resume`, 스케줄, 문제 해결, 개입 절차)
- [`config/README.md`](config/README.md) — 설정 항목과 대상 선정 규칙
- [`agents/`](agents/) — 에이전트 규칙 파일 4종
- [`schemas/README.md`](schemas/README.md) — 에이전트 출력 JSON 스키마
- [`templates/README.md`](templates/README.md) — 페이지 템플릿 12종과 섹션 제목 정본
- [`experiments/README.md`](experiments/README.md) — 사용자 실험 결과 폴더 규칙
- [`docs/about/agents.md`](docs/about/agents.md), [`docs/about/how-to-contribute.md`](docs/about/how-to-contribute.md), [`docs/about/reading-guide.md`](docs/about/reading-guide.md), [`docs/corrections.md`](docs/corrections.md) — 독자용 소개·개입 방법·표기 읽는 법·정정 요청 안내
