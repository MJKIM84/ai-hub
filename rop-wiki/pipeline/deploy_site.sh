#!/usr/bin/env bash
# ROP 연구 위키 — 사이트 빌드와 원격 배포(GitHub Pages, gh-deploy 방식).
#
# 공개 배포(https://mjkim84.github.io/ai-hub/)는 .github/workflows/rop-wiki-pages.yml(GitHub Actions)이 담당한다.
# 이 스크립트는 그 대체 수단(gh-deploy 방식)의 수동 배포 명령이며, config/ops.yaml 의 deploy.method 가
# actions 인 동안은 --yes 를 줘도 아무것도 하지 않는다(10행). 두 방식을 동시에 켜지 않도록 deploy.method 값 하나로 고른다.
#
# 사용: bash pipeline/deploy_site.sh [--yes] [--no-build]
#   (옵션 없음)  로컬 빌드(settings.site_build_cmd, 기본 mkdocs build --strict)만 하고, 원격 배포는 무엇을 할지 출력만 한다(exit 0)
#   --yes        config/ops.yaml 의 deploy.enabled 가 true 이고 deploy.method 가 gh-deploy 일 때만 실제로 배포한다:
#                  mkdocs gh-deploy --force --remote-name <deploy.remote_name> --remote-branch <deploy.remote_branch>
#                (사이트를 다시 빌드해 gh-pages 브랜치에 커밋하고 원격에 강제 푸시한다. 작업 브랜치와 docs 는 바꾸지 않는다)
#   --no-build   로컬 빌드 확인을 건너뛴다(gh-deploy 는 어차피 다시 빌드한다)
# deploy.method 가 actions 면 이 스크립트는 푸시하지 않는다 — GitHub Actions 워크플로(deploy/github-pages.yml 을
#   .github/workflows/ 로 복사)가 저장소에 푸시된 내용으로 빌드·배포한다.
# 켜기: python3 pipeline/lib/notify.py --enable deploy && bash pipeline/deploy_site.sh --yes      (저장소 설정은 deploy/README.md)
# 종료 코드: 0 성공(또는 배포하지 않음), 1 로컬 빌드 실패, 2 옵션 오류, 4 원격 배포 실패
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
PY="${PYTHON:-python3}"
YES=0; BUILD=1
while [ $# -gt 0 ]; do
  case "$1" in
    --yes) YES=1; shift;;
    --no-build) BUILD=0; shift;;
    -h|--help) sed -n '2,16p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; exit 0;;
    *) echo "[deploy_site] 알 수 없는 옵션: $1"; exit 2;;
  esac
done
ops() { "$PY" pipeline/lib/notify.py --get "$1" --default "${2:-}" 2>/dev/null || printf '%s\n' "${2:-}"; }
ENABLED="$(ops deploy.enabled false)"
METHOD="$(ops deploy.method gh-deploy)"
REMOTE="$(ops deploy.remote_name origin)"
BRANCH="$(ops deploy.remote_branch gh-pages)"
BUILD_CMD="$("$PY" pipeline/lib/runs.py setting --key site_build_cmd --default "mkdocs build --strict" 2>/dev/null || echo "mkdocs build --strict")"
MSG="deploy: ROP 연구 위키 사이트 $(date '+%Y-%m-%d %H:%M %Z') (pipeline/deploy_site.sh)"
DEPLOY_CMD=(mkdocs gh-deploy --force --remote-name "$REMOTE" --remote-branch "$BRANCH" --message "$MSG")
SHOWN="mkdocs gh-deploy --force --remote-name $REMOTE --remote-branch $BRANCH --message \"$MSG\""

# 1. 로컬 빌드(배포 여부와 관계없이 사이트가 깨지지 않았는지 먼저 본다)
if [ "$BUILD" = 1 ]; then
  echo "[deploy_site] 로컬 빌드: $BUILD_CMD"
  if ! bash -c "$BUILD_CMD"; then
    echo "[deploy_site] 로컬 빌드 실패 — 원격 배포하지 않는다"
    exit 1
  fi
fi

# 2. 원격 배포 여부
why=""
[ "$ENABLED" != "true" ] && why="config/ops.yaml 의 deploy.enabled 가 false 다"
[ -z "$why" ] && [ "$METHOD" != "gh-deploy" ] && why="deploy.method 가 '$METHOD' 다(actions 면 GitHub Actions 워크플로가 배포한다 — deploy/README.md)"
[ -z "$why" ] && [ "$YES" != 1 ] && why="--yes 가 없다(원격 배포는 명시적으로 확인한 경우에만 한다)"
if [ -n "$why" ]; then
  echo "[deploy_site] 원격 배포하지 않는다: $why"
  echo "[deploy_site] 켜져 있고 --yes 였다면 실행했을 명령: (cd $ROOT && $SHOWN)"
  exit 0
fi

# 3. gh-deploy (사이트를 gh-pages 브랜치에 커밋해 강제 푸시). 원격이 없으면 알기 쉬운 메시지로 끝낸다
if ! git -C "$ROOT" remote get-url "$REMOTE" >/dev/null 2>&1; then
  echo "[deploy_site] git 원격 '$REMOTE' 이 없다(deploy.remote_name). 원격 배포 실패"
  exit 4
fi
echo "[deploy_site] 원격 배포: $SHOWN"
if ! "${DEPLOY_CMD[@]}"; then
  echo "[deploy_site] 원격 배포 실패(푸시 권한·네트워크를 확인한다). 로컬 사이트(site/)와 커밋은 그대로다"
  exit 4
fi
echo "[deploy_site] 원격 배포 완료: $REMOTE/$BRANCH (저장소 Settings → Pages 에서 Source 를 이 브랜치로 두어야 공개된다)"
