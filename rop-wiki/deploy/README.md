# deploy/ — 사이트 원격 배포·운영 설정 안내

이 폴더는 ROP 연구 위키를 외부에 공개하는 방법(GitHub Pages)과 운영 서버의 비밀값 설정 방법을 정리한다. 외부에 영향을 주는 스위치는 모두 `config/ops.yaml` 에 있고 기본값은 꺼짐(`false`)이다. 이 폴더의 워크플로 파일은 템플릿이라 그대로 두면 아무것도 실행되지 않는다.

| 스위치 (`config/ops.yaml`) | 기본값 | 켜면 일어나는 일 | 켜는 명령 |
|---|---|---|---|
| `deploy.enabled` | `false` | 사이트를 GitHub Pages 에 공개한다(아래 두 방식 중 하나) | `python3 pipeline/lib/notify.py --enable deploy` |
| `notify.enabled` + `notify.channel` | `false`, `none` | 실행이 끝날 때 슬랙·이메일로 결과를 보낸다 | `python3 pipeline/lib/notify.py --enable notify --channel slack_webhook` |
| `cron.enabled` | `false` | `install_cron.sh` 가 운영 서버 crontab 에 등록할 수 있게 된다 | `python3 pipeline/lib/notify.py --enable cron && bash pipeline/install_cron.sh` |

현재 값은 `python3 pipeline/lib/notify.py --status` 로 본다. 끄는 명령은 `--enable` 을 `--disable` 로 바꾼다. 이 명령은 `ops.yaml` 의 해당 `enabled:` 줄(과 `channel:` 줄)만 고치고 주석은 그대로 둔다.

## 1. 먼저 확인할 것

- **공개 범위:** GitHub Pages 사이트는 저장소가 비공개여도 인터넷에 공개된다(Enterprise 의 비공개 Pages 는 예외). 위키의 연구 내용과 실행 로그(`docs/logs/`)를 공개해도 되는지 먼저 확인한다.
- **요금제:** 비공개 저장소에서 Pages 를 쓰려면 유료 요금제(Pro·Team 이상)가 필요하다.
- **방식은 하나만:** 저장소의 Pages 배포 원천(Source)은 하나뿐이다. 아래 A(Actions)와 B(gh-deploy) 중 하나만 고르고, `deploy.method` 를 그에 맞춘다.
- **주소:** 이 저장소(`MJKIM84/ai-hub`)라면 `https://mjkim84.github.io/ai-hub/` 가 된다. 이 주소를 `notify.site_url` 에 적으면 알림에 그날 일일 로그 페이지 링크가 붙는다.

## 2. 방식 A — GitHub Actions 가 빌드·배포 (권장: 서버에 푸시 권한 외 추가 설정 없음)

저장소에 푸시된 내용으로 GitHub 가 `mkdocs build --strict` 를 돌리고 공식 액션(`configure-pages`, `upload-pages-artifact`, `deploy-pages`)으로 배포한다.

1. 워크플로 템플릿을 복사한다(저장소 루트에서).

   ```bash
   mkdir -p .github/workflows
   cp rop-wiki/deploy/github-pages.yml .github/workflows/rop-wiki-pages.yml
   ```

2. 저장소 **Settings → Pages → Build and deployment → Source** 를 **GitHub Actions** 로 바꾼다.
3. `config/ops.yaml` 에서 `deploy.enabled: true`, `deploy.method: actions` 로 바꾼다.

   ```bash
   cd rop-wiki && python3 pipeline/lib/notify.py --enable deploy --method actions
   ```

4. 커밋·푸시한 뒤 **Actions → rop-wiki pages → Run workflow** 로 처음 한 번 수동 실행한다. 워크플로는 `ops.yaml` 의 두 값을 읽어 배포 여부를 정한다(아니면 빌드만 하고 배포 단계를 건너뛴다).
5. (선택) 매일 자동 배포: 워크플로의 `push:` 절 주석을 풀고 `branches` 를 일일 파이프라인이 커밋하는 브랜치로 바꾼다. 서버의 `config/settings.yaml` 에서 `git_push: true` 여야 커밋이 GitHub 에 올라간다.

끄기: `python3 pipeline/lib/notify.py --disable deploy` 후 커밋·푸시(워크플로는 빌드만 한다). 완전히 없애려면 `.github/workflows/rop-wiki-pages.yml` 을 지우고 Settings → Pages 에서 사이트를 내린다(Unpublish).

## 3. 방식 B — 운영 서버가 gh-pages 브랜치를 직접 푸시 (`mkdocs gh-deploy`)

서버에서 사이트를 빌드해 `gh-pages` 브랜치에 커밋하고 원격에 강제 푸시한다. 작업 브랜치와 `docs/` 는 바꾸지 않는다. 서버에 저장소 푸시 권한(SSH 키 또는 토큰)이 있어야 한다.

1. `config/ops.yaml` 에서 `deploy.enabled: true`(`deploy.method: gh-deploy` 는 기본값).

   ```bash
   cd rop-wiki && python3 pipeline/lib/notify.py --enable deploy
   ```

2. 처음 한 번 수동으로 배포한다: `bash pipeline/deploy_site.sh --yes`
   - 이 명령은 로컬 빌드(`mkdocs build --strict`)를 먼저 확인하고, 통과하면 `mkdocs gh-deploy --force --remote-name origin --remote-branch gh-pages` 를 실행한다.
   - `--yes` 가 없거나 `deploy.enabled: false` 면 로컬 빌드만 하고 "실행했을 명령"만 출력한다(원격에 아무것도 하지 않는다).
3. 저장소 **Settings → Pages → Source** 를 **Deploy from a branch**, 브랜치 `gh-pages` / `(root)` 로 둔다.
4. 매일 자동 배포: cron 으로 돌리는 서버라면 `pipeline/cron_wrapper.sh` 가 정규 실행이 성공(exit 0)할 때마다 `deploy_site.sh --yes` 를 부른다(`deploy.after_daily_run: true`, 기본값). 수동 실행(`run_daily.sh` 를 직접 부름)에서는 배포하지 않으므로 필요하면 `bash pipeline/deploy_site.sh --yes` 를 따로 실행한다.

끄기: `python3 pipeline/lib/notify.py --disable deploy`. 이미 공개된 사이트를 내리려면 Settings → Pages 에서 Unpublish 하거나 원격의 `gh-pages` 브랜치를 지운다.

`deploy.remote_name`·`deploy.remote_branch` 로 원격 이름과 브랜치를 바꿀 수 있다. `--force` 는 `gh-pages` 브랜치를 매번 새 빌드로 덮어쓴다는 뜻이다(작업 브랜치에는 영향이 없다).

## 4. 알림(슬랙·이메일) 켜기

1. 비밀값을 환경변수로 준다(파일에 적지 않는다). cron 실행이면 5절의 환경 파일에 넣는다.
   - 슬랙: 채널에 Incoming Webhook 을 만들고 URL 을 `ROP_SLACK_WEBHOOK_URL` 로(`https://` 만 허용).
   - 이메일: `config/ops.yaml` 의 `notify.email` 에 `smtp_host`, `smtp_port`, `from`, `to` 를 적고, 계정·비밀번호는 `ROP_SMTP_USERNAME`·`ROP_SMTP_PASSWORD` 로. 포트 587 은 `use_tls: true`(STARTTLS), 465 는 `use_ssl: true`.
2. 스위치를 켠다: `python3 pipeline/lib/notify.py --enable notify --channel slack_webhook` (`email`, `both` 도 된다).
3. 확인: `python3 pipeline/lib/notify.py --test --mock` 은 보낼 메시지와 모의 전송 내용을 출력만 한다(네트워크 없음). `python3 pipeline/lib/notify.py --test` 는 설정대로 시험 메시지를 실제로 보낸다.
4. 어떤 결과에 보낼지는 `notify.on`(`published`, `parked`, `failed`)으로 고른다. 발송에 실패해도 게시·커밋은 되돌리지 않고 결과만 로그에 남는다.

`config/settings.yaml` 의 `notify` 는 사양서 0장 원문 값으로 남겨 두며, 실제 채널은 `ops.yaml` 의 `notify.channel` 을 따른다.

## 5. 운영 서버 환경 파일 `~/.config/rop-wiki/env`

cron 은 로그인 셸의 환경변수를 받지 않는다. `pipeline/cron_wrapper.sh` 는 이 파일이 있으면 실행 전에 읽는다(경로는 `ops.yaml` 의 `cron.env_file`). 파일 권한이 600(또는 400)이 아니면 `runs/cron.log` 에 경고를 남긴다. 값은 로그에 쓰지 않고 설정 여부만 남긴다.

```bash
mkdir -p ~/.config/rop-wiki && touch ~/.config/rop-wiki/env && chmod 600 ~/.config/rop-wiki/env
```

```bash
# ~/.config/rop-wiki/env — 셸 "이름=값" 형식(따옴표 가능). 필요한 줄만 둔다
ROP_SLACK_WEBHOOK_URL=https://hooks.slack.com/services/XXX/YYY/ZZZ
ROP_SMTP_USERNAME=bot@example.com
ROP_SMTP_PASSWORD='앱 비밀번호'
CLAUDE_CODE_OAUTH_TOKEN=...          # 헤드리스 claude -p 인증(claude setup-token 으로 발급). 또는 ANTHROPIC_API_KEY=...
# ROP_ALLOW_NO_FETCH=1               # 페이지 열람이 막힌 환경에서만(원문 미열람 모드 override)
```

## 6. cron 등록 요약

```bash
python3 pipeline/lib/notify.py --enable cron      # 등록 허용
bash pipeline/install_cron.sh --dry-run            # 등록할 블록 미리 보기
bash pipeline/install_cron.sh                      # 등록(crontab 맨 끝, 마커 주석 블록)
bash pipeline/uninstall_cron.sh                    # 해제
```

등록 줄은 `flock -n -E 75 runs/.lock` 으로 겹침을 막고 `pipeline/cron_wrapper.sh` 를 실행한다. 래퍼는 `runs/cron.log` 를 5MB 기준으로 순환하고, 환경 파일을 읽고, `run_daily.sh` 를 4시간 상한(`cron.max_runtime_sec`)으로 실행한다. Debian·Ubuntu 기본 cron 은 `CRON_TZ` 를 무시하므로 `install_cron.sh` 가 cron 데몬을 보고 서버 시간대로 환산해 등록한다(`cron.tz_mode: auto`). 자세한 설명은 `pipeline/cron.example` 에 있다.
