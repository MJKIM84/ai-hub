# Robot simulator

기존 ROP 연구 앱의 배포용 소스입니다. Python/FastAPI/MuJoCo 실행부와 React/Three.js 화면을 하나의 서버에서 제공합니다. `rop-wiki`의 GitHub Pages 배포와 독립적입니다.

## 포함 범위

- 처음 열리는 예제: 2개 층, 승강기, AMR 1대·조작 팔 3대·Spot 1대, 이동 보행자 3명, 상자 1개.
- 원래 구현의 환경 편집, 도면 검토, 기능 온톨로지, 계획 도우미, 2D/3D 관제, 물리 실행.
- 방문자마다 독립된 임시 작업 공간. 운영자의 데이터·API 키·Codex 로그인은 상속하지 않습니다.
- 모델 키 없이 예제 수동 실행 가능. 실제 모델 대화에는 방문자 API 연결·동의가 필요합니다.
- 기존 사용자 업로드, 대화·승인 이력, 개인 설정, 결과 전체, 인증 파일은 이 저장소에 포함하지 않습니다.

## 배포 상태

외부 실행 서버는 아직 연결하지 않았습니다. `Dockerfile`, `railway.json`, 공개 방문자 진입점과 자동 검사를 준비했습니다. `.github/workflows/robot-simulator.yml`이 Linux에서 방문자 격리 검사와 컨테이너 빌드·물리 단계 실행을 검사합니다. 실제 모델에 유료 요청을 보내지 않습니다.

## Railway 배포

1. GitHub 저장소 `MJKIM84/ai-hub`를 연결하고 서비스의 **Root Directory**를 `/robot-simulator`, **Config File**을 `/robot-simulator/railway.json`으로 설정합니다.
2. 리소스·요금 한도를 결정합니다. **인스턴스 1개**, 작업자 프로세스 1개로 시작합니다. 물리 엔진은 CPU에서 실행하고 3D 화면은 방문자의 브라우저가 그립니다. 실제 동시 접속 성능은 배포 후 측정해야 합니다.
3. 서비스의 공개 HTTPS 도메인을 생성합니다. `RAILWAY_PUBLIC_DOMAIN`이 있으면 앱이 이 주소를 사용합니다. 사용자 도메인은 `ROBOT_PUBLIC_ORIGINS=https://실제-도메인`으로 지정합니다. 뒤에 `/`를 붙이지 않습니다.
4. Railway 프록시만 컨테이너 포트에 접근하도록 하고 `FORWARDED_ALLOW_IPS=*`를 설정합니다. 이렇게 해야 프록시가 전달한 HTTPS를 인식해 보안 쿠키와 출처 검사를 적용합니다. 자체 서버에서 포트를 직접 인터넷에 노출할 때 이 설정을 사용하지 않습니다.
5. 배포 후 `/healthz`, 새 방문자 공간, 실제 지도·로봇·보행자 로딩, 시작·일시 정지·결과 저장을 확인합니다.
6. 확인한 HTTPS 주소를 `rop-wiki/docs/about/simulator.md`에 실행 링크로 추가하고 홈의 준비 중 안내를 갱신합니다.

`PORT`는 호스팅 서비스 값을 사용합니다. 상태 검사는 방문자 공간이나 시뮬레이션을 만들지 않습니다. 허용된 HTTPS 주소가 없으면 서버가 시작하지 않습니다.

## 다른 Docker 서버

이 디렉터리에서:

```sh
docker build -t rop-simulator .
docker run --rm --name rop-simulator \
  --cpus=2 --memory=3g \
  -p 127.0.0.1:8000:8000 \
  -e ROBOT_PUBLIC_ORIGINS=https://simulator.example.com \
  -e FORWARDED_ALLOW_IPS='*' \
  rop-simulator
```

위 주소는 예시입니다. 자체 HTTPS 역방향 프록시에서 루프백 포트로 연결하고 실제 주소로 바꿉니다. `*`는 프록시만 포트에 접근할 수 있는 이 구성에서만 사용합니다. 서버를 여러 프로세스·복제본으로 늘리면 메모리의 방문자 상태가 공유되지 않으므로 현재 버전에서는 지원하지 않습니다.

## 운영 설정

| 변수 | 기본값 | 의미 |
|---|---:|---|
| `ROBOT_PUBLIC_ORIGINS` | 없음 | 정확한 시뮬레이터 HTTPS 주소. 위키 주소를 넣지 않음 |
| `RAILWAY_PUBLIC_DOMAIN` | 호스팅 제공 | 위 주소를 생략한 Railway 환경의 도메인 |
| `PORT` | 8000 | 실행 포트 |
| `ROBOT_MAX_VISITORS` | 2 | 동시에 유지하는 방문자 공간 수, 1–8 |
| `ROBOT_VISITOR_TTL_SECONDS` | 1800 | 공간 수명, 300–14400초 |
| `ROBOT_KEY_TTL_SECONDS` | 1800 | 방문자 키 메모리 보관 상한, 60–1800초 |
| `FORWARDED_ALLOW_IPS` | 127.0.0.1 | 전달된 HTTPS 정보를 신뢰할 프록시 주소 |

방문자가 자리를 떠나도 공간은 만료될 때까지 남습니다. 만료·연결 종료·서버 재시작 시 결과가 사라지므로 다운로드를 안내합니다. 운영자 API 키를 환경 변수에 추가하거나 `.codex`·개인 `data` 폴더를 마운트하지 않습니다. 컨테이너의 CPU·메모리 및 플랫폼 비용 한도를 별도로 설정해야 합니다. 대규모 공개 서비스용 부하·악용 대응 검증을 완료한 배포는 아닙니다.

## 환경 차이와 근거

- 원래 macOS 전용 Swift/Vision OCR은 Linux에 없습니다. PDF 렌더링·텍스트 추출과 이미지 변환 도구는 포함되지만 래스터 이미지의 자동 문자 인식은 제한됩니다. 도면에서 공간 이름은 수동 검토·입력할 수 있습니다.
- 실제 물리 실행에 필요한 예제·온톨로지 기본 문서·Spot 형상 파일을 포함했습니다. `assets/robots/spot/LICENSE`와 `PROVENANCE.json`을 유지합니다. 제3자 자산 권리는 해당 원문을 따릅니다.
- MuJoCo·Python 의존성은 `requirements.lock`, 웹 의존성은 `web/package-lock.json`으로 고정합니다. 모델 답변 품질·실물 로봇 검증·클라우드의 전체 218초 시나리오 검증은 컨테이너 시작 검사로 대체하지 않습니다.
- 공개 예제의 기존 로컬 실행 결과는 [위키 소개](../rop-wiki/docs/about/simulator.md)에 범위와 함께 정리했습니다.

## 개발 검사

```sh
python -m venv .venv
.venv/bin/pip install -r requirements.lock pytest==8.4.2 httpx==0.28.1
.venv/bin/python -m pytest tests -q
cd web
npm ci
npm run build
```

정적 화면만 GitHub Pages에 복사하면 `/api`와 물리 실행이 동작하지 않습니다. 위키는 시뮬레이터 서버로 이동하는 진입점으로 사용합니다.
