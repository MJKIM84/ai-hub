"""ROP 연구 위키 백본 라이브러리.

모듈
- paths       : 저장소 경로·슬러그 규약(고정)
- source      : 분류 원문(_source/ROP_SCM_연구분야_분류.md) 파서
- verbatim    : 원문 인용 블록에 [분류원문] 태그를 붙이고 벗기는 도우미
- frontmatter : YAML 프런트매터 읽기·쓰기·필수 필드 상수
- autoregion  : <!-- auto:<key>:start --> ~ <!-- auto:<key>:end --> 영역 처리
- nav         : mkdocs 내비게이션 생성과 mkdocs.yml 작성
- render      : data/*.json → 자동 갱신 영역 본문 렌더러
"""
