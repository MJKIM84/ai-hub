# 원문 제공함 (inbox/sources)

에이전트가 네트워크 정책 때문에 열지 못한 출처의 원문을 사람이 직접 넣는 곳이다. 여기에 넣은 파일은 텍스트로 바뀌어 `data/source_texts/` 에 저장되고, 해당 참고문헌 페이지에 "원문 열람(사용자 제공 파일(inbox))" 이 표시된다. 다음 실행부터 리서치·검증 에이전트가 그 텍스트를 입력으로 받는다.

원문을 열지 못한 출처는 신뢰도가 medium 을 넘지 못한다(`pipeline/lib/sources.py` 의 `apply_fetch_caps`). 표준 PDF, 논문, 기관 보고서처럼 자주 인용되는 출처부터 넣으면 효과가 크다.

## 1. 넣는 방법

1. 원문 파일을 이 폴더에 둔다. 받는 형식은 PDF, HTML(`.html`, `.htm`), 텍스트(`.txt`), 마크다운(`.md`)이다. `.rst`, `.adoc`, `.xml`, `.json`, `.ttl` 같은 텍스트 파일도 그대로 읽는다.
2. 같은 폴더의 `manifest.yaml` 의 `items` 에 항목 하나를 더한다.

   ```yaml
   items:
     - file: EPCIS-Standard-2.0.pdf           # 필수. 이 폴더 안의 파일 이름
       url: https://ref.gs1.org/standards/epcis/   # 원문의 정본 URL. 참고문헌 연결에 쓴다
       title: EPCIS Standard 2.0              # 원문 제목
       org: GS1                               # 기관 또는 저자
       published: 2022-06                     # 발행일(YYYY, YYYY-MM, YYYY-MM-DD). 모르면 비운다
       ref_id: ref-003                        # 선택. 연결할 참고문헌 id
   ```

3. 위키 루트(`rop-wiki/`)에서 실행한다.

   ```bash
   python3 pipeline/ingest_sources.py --dry-run   # 무엇을 할지 먼저 본다(파일을 바꾸지 않음)
   python3 pipeline/ingest_sources.py             # 실제 처리
   ```

## 2. 처리 순서

| 단계 | 하는 일 |
|---|---|
| 텍스트 추출 | PDF 는 `pdftotext`(poppler-utils)를 쓰고, 없으면 `pypdf` 를 별도 프로세스로 쓴다. HTML 은 파이썬 표준 `html.parser` 로 본문만 뽑는다(스크립트·스타일 제외). 텍스트 파일은 그대로 읽는다 |
| 참고문헌 연결 | `ref_id` 가 있으면 그 참고문헌에 연결한다. 없으면 `docs/references/ref-*.md` 가운데 `url` 이 같은 페이지를 찾는다(scheme·`www.`·끝 슬래시는 무시). 둘 다 없으면 `src-<이름>` 으로 저장만 한다 |
| 저장 | `data/source_texts/<ref_id 또는 src-이름>.txt` 와 `data/source_texts/index.json`(sha256, 글자 수, 수집일, 경로 `fetched_via: inbox`) |
| 참고문헌 갱신 | 연결된 페이지의 프런트매터를 `fetched: true`, `fetched_via: inbox`, `source_text: data/source_texts/<id>.txt` 로 바꾸고, 서지 정보 표의 "원문 열람" 행, 각주 형식 줄(접근일, "(원문 미열람)" 제거), 비고 절의 원문 열람 상태 표를 고친다. 유형 기준 신뢰도가 high 인 출처는 medium 상한이 풀린다 |
| 변경 이력 | `data/changelog.json` 에 "원문 텍스트 등록(inbox)" 한 줄을 남긴다(`--no-changelog` 로 끔) |
| 정리 | 처리한 파일을 `inbox/sources/processed/` 로 옮긴다 |

같은 파일을 다시 넣어도 내용(sha256)이 같으면 아무것도 바꾸지 않는다. 이미 `processed/` 로 옮긴 항목은 manifest 에 남아 있어도 건너뛴다. 처리가 끝난 manifest 항목은 지워도 되고 기록으로 남겨 두어도 된다.

## 3. 실패할 때

| 증상 | 원인·조치 |
|---|---|
| "텍스트 추출 실패 — PDF 텍스트 추출 실패(pdftotext 없음; pypdf …)" | `sudo apt-get install poppler-utils` 또는 `python3 -m pip install pypdf` 로 도구를 설치한다. 파일은 inbox 에 남아 있으므로 설치 뒤 다시 실행한다 |
| "추출한 텍스트가 거의 없다" | 스캔 이미지 PDF 다. OCR 로 텍스트 PDF 를 만들어 다시 넣거나, 필요한 부분을 `.txt` 로 옮겨 넣는다 |
| "파일 없음" | manifest 의 `file` 이름과 실제 파일 이름이 다르다(대소문자·확장자 확인) |
| "ref_id … 의 참고문헌 페이지가 아직 없다" | 텍스트는 그 id 로 저장된다. 퍼블리셔가 그 참고문헌 페이지를 만든 뒤 `python3 pipeline/ingest_sources.py` 를 다시 실행하면(manifest 가 비어 있어도) 텍스트가 있는 참고문헌 페이지를 찾아 원문 열람 표시를 붙인다 |
| "manifest url 이 … 와 다르다" | `ref_id` 를 따른다. 다른 출처라면 `ref_id` 를 지우고 다시 실행한다 |

종료 코드는 처리하지 못한 항목이 있으면 1, 아니면 0 이다.

## 4. GitHub 원문 미러

공식 문서의 원문이 GitHub 에 있는 출처(VDA 5050, ROS 2 설계 문서, Open-RMF 책, NIST ARIAC 문서 등)는 파일을 넣지 않아도 된다. `config/source_mirrors.yaml` 에 정본 URL 과 `raw.githubusercontent.com` 원문 경로가 있고, 다음 명령이 원문을 받아 같은 방식으로 저장한다(`fetched_via: github_raw`).

```bash
python3 pipeline/ingest_sources.py --mirrors                 # 모든 참고문헌
python3 pipeline/ingest_sources.py --mirrors --refs ref-004  # 일부만
```

미러 목록의 `relation` 이 `original`(같은 문서의 원본)인 것만 원문 열람으로 친다. `official_artifact`(같은 기관의 스키마·온톨로지 같은 산출물)와 `related`(제3자 구현 등)는 참고용이며 원문 열람으로 치지 않는다.

## 5. 이 폴더의 파일

| 파일 | 뜻 |
|---|---|
| `README.md` | 이 안내 |
| `manifest.yaml` | 넣은 파일의 목록(사람이 쓴다) |
| `processed/` | 처리가 끝난 원문 파일(스크립트가 옮긴다) |
