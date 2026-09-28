"""Review-first floor-plan import. Pixels are evidence; metres require calibration.

Detection proposes geometry and PDF text labels, never silently creates a
traversable door or a physical facility. Only reviewed objects generate a
Project. No document content is evaluated as instructions.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import json
import math
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import sys
from xml.etree import ElementTree
from urllib.parse import unquote

import numpy as np

from .domain import Element, Environment, Floor, Pose, Project, Size

KINDS = {'room', 'corridor', 'wall', 'door', 'opening', 'stairs', 'elevator', 'charger', 'dock', 'loading'}
LABEL_KIND = {
    'corridor': 'corridor', 'hallway': 'corridor', '복도': 'corridor',
    'stair': 'stairs', '계단': 'stairs', 'lift': 'elevator',
    'elevator': 'elevator', '승강기': 'elevator', '엘리베이터': 'elevator',
    'charging': 'charger', '충전': 'charger', 'dock': 'dock', '도킹': 'dock',
    'loading': 'loading', '하역': 'loading', 'door': 'door', '출입구': 'door',
}
MAX_BYTES = 20_000_000
MAX_PAGES = 12


def _command(args, *, input=None, timeout=40, env=None):
    try:
        return subprocess.run(args, input=input, check=True, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE, timeout=timeout, env=env).stdout
    except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
        raise ValueError('도면 변환에 실패했습니다. 파일 형식과 PDF 암호·도구 설치를 확인하세요') from None


def _ppm(data):
    # ffmpeg/pdftoppm emit P6. Dimensions are bounded before allocating arrays.
    match = re.match(rb'P6\s+(?:#[^\n]*\n\s*)*(\d+)\s+(\d+)\s+(255)\s', data)
    if not match:
        raise ValueError('도면 픽셀을 읽을 수 없습니다')
    width, height = int(match[1]), int(match[2])
    if not 100 <= width <= 5000 or not 100 <= height <= 5000 or width * height > 12_000_000:
        raise ValueError('도면 해상도는 100~5000px, 1200만 픽셀 이하로 준비하세요')
    start = match.end()
    if len(data) - start != width * height * 3:
        raise ValueError('도면 픽셀 길이가 맞지 않습니다')
    return np.frombuffer(data, dtype=np.uint8, offset=start).reshape(height, width, 3)


def _raster_pixels(raster):
    """Read bounded RGB pixels, compositing transparent plan margins on white."""
    if not shutil.which('ffmpeg') or not shutil.which('ffprobe'):
        raise ValueError('이미지 변환 도구 ffmpeg과 ffprobe을 설치하세요')
    metadata=json.loads(_command(['ffprobe','-v','error','-select_streams','v:0',
        '-show_entries','stream=width,height,pix_fmt','-of','json',str(raster)],timeout=20))
    streams=metadata.get('streams',[])
    if not streams:
        raise ValueError('도면 픽셀을 읽을 수 없습니다')
    width,height=streams[0].get('width'),streams[0].get('height')
    if (type(width) is not int or type(height) is not int or
        not 100<=width<=5000 or not 100<=height<=5000 or width*height>12_000_000):
        raise ValueError('도면 해상도는 100~5000px, 1200만 픽셀 이하로 준비하세요')
    pix_fmt=streams[0].get('pix_fmt','')
    has_alpha=(pix_fmt in {'rgba','bgra','argb','abgr','ya8','ya16be','ya16le'} or
        pix_fmt.startswith('yuva'))
    args=['ffmpeg','-v','error','-i',str(raster)]
    if has_alpha:
        # ffmpeg's default RGB conversion makes transparent PNG areas black.
        # Those margins otherwise look like one huge wall to line detection.
        args += ['-f','lavfi','-i',f'color=c=white:s={width}x{height}',
                 '-filter_complex','[1:v][0:v]overlay=format=auto,format=rgb24']
    args += ['-frames:v','1','-f','image2pipe','-vcodec','ppm','-']
    return _ppm(_command(args,timeout=35))


def _runs(row, minimum):
    edge = np.diff(np.r_[False, row, False].astype(np.int8))
    return [(int(a), int(b)) for a, b in zip(np.flatnonzero(edge == 1), np.flatnonzero(edge == -1))
            if b - a >= minimum]


def _long_lines(rgb, *, gap_limit=6):
    height, width = rgb.shape[:2]
    # Work at original coordinates after a bounded rasterization. Long dark
    # contiguous strokes are candidate walls, not confirmed architecture.
    gray = np.mean(rgb.astype(np.uint16), axis=2)
    dark = gray < 110
    raw = []
    def strokes(binary, minimum):
        parts=_runs(binary, 15)
        joined=[]
        for a,b in parts:
            # Physical wall proposals bridge antialiasing only. Room outline
            # proposals may use a wider gap, but remain review-only.
            if joined and a-joined[-1][1]<=gap_limit:
                joined[-1]=(joined[-1][0],b)
            else: joined.append((a,b))
        return [(a,b) for a,b in joined if b-a>=minimum]
    for y in range(height):
        raw.extend(('h', a, y, b, y + 1) for a, b in strokes(dark[y], max(45, int(width * .06))))
    for x in range(width):
        raw.extend(('v', x, a, x + 1, b) for a, b in strokes(dark[:, x], max(45, int(height * .06))))
    # Merge adjacent rows/columns of the same stroke; suppress duplicate
    # fragments from letterforms or hatch marks by requiring useful length.
    grouped = []
    for orient in ('h', 'v'):
        lines = sorted((r for r in raw if r[0] == orient), key=lambda r: (r[2] if orient == 'h' else r[1], r[1] if orient == 'h' else r[2]))
        for line in lines:
            candidates = [i for i, old in enumerate(grouped) if old[0] == orient and
                          (line[2] <= old[4] + 2 if orient == 'h' else line[1] <= old[3] + 2) and
                          (min(line[3], old[3]) - max(line[1], old[1]) >= .7 * min(line[3]-line[1], old[3]-old[1])
                           if orient == 'h' else min(line[4], old[4])-max(line[2], old[2]) >= .7 * min(line[4]-line[2], old[4]-old[2]))]
            if candidates:
                i = candidates[-1]
                old = grouped[i]
                grouped[i] = (orient, min(old[1], line[1]), min(old[2], line[2]),
                              max(old[3], line[3]), max(old[4], line[4]))
            else:
                grouped.append(line)
    result = sorted((r for r in grouped if (r[4]-r[2]>=2 if r[0]=='h' else r[3]-r[1]>=2)),
                    key=lambda r: (r[2], r[1]))
    return result[:250]


def _pdf_words(path, page_number, width, height):
    if not shutil.which('pdftotext'):
        return []
    try:
        xml = _command(['pdftotext', '-f', str(page_number), '-l', str(page_number),
                        '-bbox-layout', str(path), '-'], timeout=20)
        root = ElementTree.fromstring(xml)
    except (ValueError, ElementTree.ParseError):
        return []
    pages = [e for e in root.iter() if e.tag.endswith('page')]
    if not pages:
        return []
    page = pages[0]
    source_width=float(page.attrib['width']); source_height=float(page.attrib['height'])
    # Poppler's bbox-layout page metadata retains the PDF MediaBox orientation,
    # while its word boxes and pdftoppm raster honor /Rotate. Swap the scale
    # basis for 90°/270° sheets so labels stay on the visible floorplan.
    if (width > height) != (source_width > source_height):
        source_width,source_height=source_height,source_width
    sx, sy = width / source_width, height / source_height
    def read_word(e):
        return {'text': e.text.strip(), 'bbox_px': [float(e.attrib['xMin'])*sx,
            float(e.attrib['yMin'])*sy, float(e.attrib['xMax'])*sx, float(e.attrib['yMax'])*sy]}

    # pdftotext preserves the reading order inside each XML line, including
    # /Rotate pages whose visual baseline is vertical. Never join across
    # separate lines: nearby room names can otherwise become one label.
    lines = [[read_word(e) for e in line.iter()
              if e.tag.endswith('word') and e.text and e.text.strip()]
             for line in page.iter() if line.tag.endswith('line')]
    if not lines:
        lines = [[read_word(e) for e in page.iter()
                  if e.tag.endswith('word') and e.text and e.text.strip()]]
    grouped=[]
    for words in lines:
        current=None
        for word in words:
            if current is not None:
                a=current['bbox_px']; b=word['bbox_px']
                same_y=abs((a[1]+a[3]-b[1]-b[3])/2)<8
                same_x=abs((a[0]+a[2]-b[0]-b[2])/2)<8
                adjacent=(same_y and (0<=b[0]-a[2]<25 or 0<=a[0]-b[2]<25)) or (
                    same_x and (0<=b[1]-a[3]<25 or 0<=a[1]-b[3]<25))
                if adjacent:
                    current['text']+=' '+word['text']
                    current['bbox_px']=[min(a[0],b[0]),min(a[1],b[1]),
                                        max(a[2],b[2]),max(a[3],b[3])]
                    continue
            current=dict(word)
            grouped.append(current)
    return grouped[:1000]


def _image_words(path, width, height):
    """OS OCR when available; absence is explicit rather than fabricated text."""
    script=Path(__file__).resolve().parents[2]/'scripts'/'floorplan_ocr.swift'
    if sys.platform=='darwin' and shutil.which('swift') and script.exists():
        try:
            cache=Path(tempfile.gettempdir())/'robot-floorplan-swift-cache'
            cache.mkdir(exist_ok=True)
            environment=dict(os.environ,CLANG_MODULE_CACHE_PATH=str(cache),SWIFT_MODULECACHE_PATH=str(cache))
            rows=json.loads(_command(['swift',str(script),str(path),str(width),str(height)],timeout=90,env=environment))
            return [r for r in rows if isinstance(r.get('text'),str) and len(r.get('bbox_px',[]))==4][:1000], 'macOS Vision'
        except (ValueError,json.JSONDecodeError):
            return [], '로컬 OCR 실패; 실제 모델로 이미지 후보를 보강하고 원문을 검토하세요'
    return [], 'OCR 도구 없음; 공간 이름을 수동으로 입력하세요'


def _proposals(rgb, words):
    words=[word for word in words if word.get('review_status')!='rejected']
    height, width = rgb.shape[:2]
    lines = _long_lines(rgb)
    proposals = []
    for i, (_, x0, y0, x1, y1) in enumerate(lines):
        if (x1-x0)*(y1-y0) > .08 * width * height:
            continue
        proposals.append(dict(id=f'wall-{i}', kind='wall', name=f'벽 후보 {i+1}',
                              bbox_px=[x0,y0,x1,y1], status='proposed',
                              evidence='도면의 긴 어두운 선; 벽 여부와 개구부 검토 필요', source='image_geometry'))
        # A gap in a drawn line is not evidence of a door: it can be a window,
        # furniture, a label, or raster noise. Door candidates need a visible
        # source label or a separately marked model proposal with human review.
    # A longer interrupted outline is useful for finding a room candidate,
    # but must never be reused as a physical wall: the interruption may be a
    # real doorway. Every room candidate still needs original-image review.
    room_lines = _long_lines(rgb, gap_limit=65)
    xs = sorted(set(round((r[1]+r[3])/2) for r in room_lines if r[0]=='v'))
    ys = sorted(set(round((r[2]+r[4])/2) for r in room_lines if r[0]=='h'))
    if len(xs) <= 30 and len(ys) <= 30:
        room_index = 0
        for x0,x1 in zip(xs,xs[1:]):
            for y0,y1 in zip(ys,ys[1:]):
                if x1-x0 < width*.035 or y1-y0 < height*.035:
                    continue
                htop = any(r[0]=='h' and abs((r[2]+r[4])/2-y0)<7 and r[1]<=x0+8 and r[3]>=x1-8 for r in room_lines)
                hbottom = any(r[0]=='h' and abs((r[2]+r[4])/2-y1)<7 and r[1]<=x0+8 and r[3]>=x1-8 for r in room_lines)
                vleft = any(r[0]=='v' and abs((r[1]+r[3])/2-x0)<7 and r[2]<=y0+8 and r[4]>=y1-8 for r in room_lines)
                vright = any(r[0]=='v' and abs((r[1]+r[3])/2-x1)<7 and r[2]<=y0+8 and r[4]>=y1-8 for r in room_lines)
                if all((htop,hbottom,vleft,vright)):
                    room_index += 1
                    label = next((w['text'] for w in words if x0 < (w['bbox_px'][0]+w['bbox_px'][2])/2 < x1
                                  and y0 < (w['bbox_px'][1]+w['bbox_px'][3])/2 < y1), None)
                    kind = LABEL_KIND.get((label or '').lower(), 'room')
                    proposals.append(dict(id=f'room-{room_index}', kind=kind, name=label or f'공간 후보 {room_index}',
                                          bbox_px=[x0,y0,x1,y1], status='proposed',source='enclosed_geometry',
                                          evidence='중간 개구 가능성을 포함한 공간 외곽 후보와 내부 원문 문자; 경계 검토 필요' if label else '중간 개구 가능성을 포함한 공간 외곽 후보; 경계·용도·이름 검토 필요'))
    for i,label in enumerate(words):
        value=label['text'].strip()
        kind=next((kind for term,kind in LABEL_KIND.items() if re.search(r'(?<!\w)'+re.escape(term)+r'(?!\w)',value,re.I)),None)
        if kind not in ('stairs','elevator','charger','dock','loading','door'):continue
        x0,y0,x1,y1=label['bbox_px']
        span=max(10,min(35,max(x1-x0,y1-y0)))
        box=[max(0,x0-span/2),max(0,y0-span/2),min(width,x1+span/2),min(height,y1+span/2)]
        proposals.append(dict(id=f'label-{i}',kind=kind,name=value[:120],bbox_px=box,status='proposed',
                              source='image_geometry',evidence='원본에 표시된 문자; 시설 위치·크기·성능과 문 여부 검토 필요'))
    # OCR text alone can identify a facility label but cannot prove its shape
    # or capacity. Keep as a label awaiting an explicitly drawn/reviewed object.
    return proposals[:500], words


def _safe_id(value):
    if not isinstance(value,str) or not re.fullmatch(r'[0-9a-f]{32}',value):
        raise ValueError('도면 식별자가 올바르지 않습니다')
    return value


def _box(value, width, height):
    if not isinstance(value,list) or len(value)!=4 or not all(type(v) in (int,float) and math.isfinite(v) for v in value):
        raise ValueError('객체 위치는 유한한 픽셀 경계 네 값이 필요합니다')
    x0,y0,x1,y1=map(float,value)
    if not (0<=x0<x1<=width and 0<=y0<y1<=height):
        raise ValueError('객체 경계가 도면 밖이거나 크기가 없습니다')
    return [x0,y0,x1,y1]


def _annotations(words):
    words=[word for word in words if word.get('review_status')!='rejected']
    return [dict(text=w['text'],bbox_px=w['bbox_px'],kind='dimension_or_scale')
            for w in words if re.search(r'\b\d+(?:\.\d+)?\s*(?:mm|cm|m|ft)\b|\b1\s*:\s*\d+\b|\b\d+\s*\'\s*(?:-\s*\d+(?:\s+\d+/\d+)?\s*["]?)?|\bscale\s*:',w['text'],re.I)
            or re.search(r'\bscale\W+of\W+(?:feet|meters|metres)\b',w['text'],re.I)][:100]


class FloorplanStore:
    def __init__(self, folder):
        self.folder=Path(folder)
        self.folder.mkdir(parents=True,exist_ok=True)

    def _path(self, plan_id):
        return self.folder / (_safe_id(plan_id)+'.json')

    def _load(self, plan_id):
        path=self._path(plan_id)
        if not path.exists(): raise ValueError('등록한 도면을 찾을 수 없습니다')
        return json.loads(path.read_text())

    def _save(self, plan):
        target=self._path(plan['id'])
        tmp=target.with_suffix('.tmp')
        contents=json.dumps(plan,ensure_ascii=False,allow_nan=False)
        tmp.write_text(contents)
        tmp.replace(target)
        # Every reviewed revision remains available after another drawing is
        # selected. Generating a map can complete the same review revision, so
        # its snapshot is updated with that generated result.
        history=self.folder/'history'/plan['id']
        history.mkdir(parents=True,exist_ok=True)
        version=history/f"{plan['revision']}.json"
        version_tmp=version.with_suffix('.tmp')
        version_tmp.write_text(contents)
        version_tmp.replace(version)

    def register(self, filename, content):
        if not isinstance(content,bytes) or not 0<len(content)<=MAX_BYTES:
            raise ValueError('도면은 비어 있지 않은 20MB 이하 PDF·PNG·JPEG 파일이어야 합니다')
        suffix = '.pdf' if content.startswith(b'%PDF-') else '.png' if content.startswith(b'\x89PNG\r\n\x1a\n') else '.jpg' if content.startswith(b'\xff\xd8\xff') else None
        if suffix is None: raise ValueError('PDF·PNG·JPEG 도면만 등록할 수 있습니다')
        title=Path(unquote(filename or '도면')).name[:200]
        digest=hashlib.sha256(content).hexdigest()
        plan_id=digest[:32]
        if self._path(plan_id).exists(): return self._load(plan_id)
        source=self.folder/(plan_id+suffix)
        source.write_bytes(content)
        pages=[]
        if suffix=='.pdf':
            if not shutil.which('pdftoppm'): raise ValueError('PDF 변환 도구 pdftoppm을 설치하세요')
            with tempfile.TemporaryDirectory() as folder:
                prefix=Path(folder)/'page'
                _command(['pdftoppm','-f','1','-l',str(MAX_PAGES+1),'-r','95','-png',str(source),str(prefix)],timeout=90)
                files=sorted(Path(folder).glob('page-*.png'))
                if len(files)>MAX_PAGES: raise ValueError(f'도면은 최대 {MAX_PAGES}페이지까지 등록할 수 있습니다')
                if not files: raise ValueError('PDF에서 페이지를 읽지 못했습니다')
                for i,file in enumerate(files):
                    raster=self.folder/f'{plan_id}-page-{i+1}.png'
                    shutil.copyfile(file,raster)
                    pages.append(self._page(raster, i+1, source, pdf=True))
        else:
            pages=[self._page(source,1,source,pdf=False)]
        plan=dict(id=plan_id,title=title,sha256=digest,source_format=suffix[1:],revision=1,
                  pages=pages,review_status='review_required',generated_environment=None)
        self._save(plan)
        return plan

    def _page(self, raster, number, source, *, pdf):
        pixels=_raster_pixels(raster)
        height,width=pixels.shape[:2]
        words=_pdf_words(source,number,width,height) if pdf else []
        ocr_status='PDF 텍스트 계층' if words else None
        if not words:
            words,ocr_status=_image_words(raster,width,height)
        candidates,words=_proposals(pixels,words)
        return dict(number=number,width_px=width,height_px=height,name=f'{number}층',
                    elevation_m=(number-1)*3.2,elevation_basis='명시적 기본값 3.2 m/층; 검토 필요',
                    scale=None, scale_basis='미입력',candidates=candidates,text_labels=words,
                    recognized_annotations=_annotations(words),ocr_status=ocr_status,
                    image_name=raster.name)

    def list(self):
        rows=[]
        for path in sorted(self.folder.glob('*.json')):
            p=json.loads(path.read_text())
            candidates=[c for page in p['pages'] for c in page['candidates']]
            rows.append(dict(id=p['id'],title=p['title'],revision=p['revision'],review_status=p['review_status'],
                             page_count=len(p['pages']),unreviewed=sum(c['status']=='proposed' for c in candidates),
                             deferred=sum(c['status']=='deferred' for c in candidates),
                             generated=bool(p.get('generated_environment')),
                             image_available=all((self.folder/page['image_name']).is_file() for page in p['pages']),
                             recovered=bool(p.get('recovered_from')),
                             source_warning=p.get('recovered_source_missing'),
                             version_count=len(self.versions(p['id'])),updated_at=path.stat().st_mtime))
        return sorted(rows,key=lambda row:row['updated_at'],reverse=True)

    def versions(self, plan_id):
        latest=self._load(plan_id)
        history=self.folder/'history'/_safe_id(plan_id)
        paths=sorted((path for path in history.glob('*.json') if path.stem.isdigit()),key=lambda path:int(path.stem),reverse=True) if history.exists() else []
        rows=[]
        for path in paths:
            if not path.stem.isdigit(): continue
            plan=json.loads(path.read_text())
            candidates=[c for page in plan['pages'] for c in page['candidates']]
            rows.append(dict(revision=plan['revision'],review_status=plan['review_status'],
                             unreviewed=sum(c['status']=='proposed' for c in candidates),
                             deferred=sum(c['status']=='deferred' for c in candidates),
                             generated=bool(plan.get('generated_environment')),
                             recovered_from=plan.get('recovered_from')))
        if not any(row['revision']==latest['revision'] for row in rows):
            candidates=[c for page in latest['pages'] for c in page['candidates']]
            rows.insert(0,dict(revision=latest['revision'],review_status=latest['review_status'],
                               unreviewed=sum(c['status']=='proposed' for c in candidates),
                               deferred=sum(c['status']=='deferred' for c in candidates),
                               generated=bool(latest.get('generated_environment')),
                               recovered_from=latest.get('recovered_from')))
        return rows

    def resume(self, plan_id, revision):
        latest=self._load(plan_id)
        if type(revision) is not int or revision<1: raise ValueError('이어갈 도면 버전을 선택하세요')
        source=self.folder/'history'/_safe_id(plan_id)/f'{revision}.json'
        if source.exists(): prior=json.loads(source.read_text())
        elif revision==latest['revision']: prior=latest
        else: raise ValueError('도면 기록 버전을 찾지 못했습니다')
        resumed=deepcopy(prior)
        resumed['revision']=latest['revision']+1
        resumed['resumed_from_revision']=revision
        # The reviewed map version remains the source revision until the user
        # changes geometry and explicitly regenerates it.
        self._save(resumed)
        return resumed

    def get(self, plan_id): return self._load(plan_id)

    def image(self, plan_id, page_number):
        plan=self._load(plan_id)
        if not type(page_number) is int or not 1<=page_number<=len(plan['pages']): raise ValueError('도면 페이지가 없습니다')
        return self.folder/plan['pages'][page_number-1]['image_name']

    def retry_ocr(self, plan_id, revision, page_number):
        """Retry local OCR without replacing a reviewed map or its candidates."""
        plan=self._load(plan_id)
        if type(revision) is not int or revision!=plan['revision']:
            raise ValueError('도면이 변경됐습니다. 최신 검토 버전을 다시 불러오세요')
        if type(page_number) is not int or not 1<=page_number<=len(plan['pages']):
            raise ValueError('도면 페이지가 없습니다')
        page=plan['pages'][page_number-1]
        words,status=_image_words(self.image(plan_id,page_number),page['width_px'],page['height_px'])
        if not words:
            page['ocr_status']=status+' · 확정 지도와 기존 후보는 보존됨'
        else:
            # Repeated OCR runs must not duplicate an already reviewed label.
            def same_label(a,b):
                ax=(a['bbox_px'][0]+a['bbox_px'][2])/2;ay=(a['bbox_px'][1]+a['bbox_px'][3])/2
                bx=(b['bbox_px'][0]+b['bbox_px'][2])/2;by=(b['bbox_px'][1]+b['bbox_px'][3])/2
                return a['text'].casefold()==b.get('original_text',b['text']).casefold() and math.hypot(ax-bx,ay-by)<12
            existing=page.get('text_labels',[])
            added=[dict(word,source='local_ocr_retry') for word in words
                   if not any(same_label(word,old) for old in existing)]
            page['text_labels']=[*existing,*added]
            page['ocr_status']=f'{status} · 재시도 성공 · 신규 문자 {len(added)}개'
        # Also update captions already read by an older annotation rule.
        # These remain source text only; they never set a metric calibration.
        page['recognized_annotations']=_annotations(page.get('text_labels',[]))
        # OCR metadata is not map geometry. Keep the approved environment
        # revision intact, including when the operating system denies OCR.
        self._save(plan)
        return plan

    def retry_geometry(self, plan_id, revision, page_number):
        """Refresh proposals; preserve reviewed objects and any confirmed map."""
        plan=self._load(plan_id)
        if type(revision) is not int or revision!=plan['revision']:
            raise ValueError('도면이 변경됐습니다. 최신 검토 버전을 다시 불러오세요')
        if type(page_number) is not int or not 1<=page_number<=len(plan['pages']):
            raise ValueError('도면 페이지가 없습니다')
        page=plan['pages'][page_number-1]
        local_sources={'image_geometry','enclosed_geometry'}
        pixels=_raster_pixels(self.image(plan_id,page_number))
        proposals,_=_proposals(pixels,page.get('text_labels',[]))
        has_reviewed=any(c.get('source') in local_sources and c['status']!='proposed'
                         for c in page['candidates'])
        # A fresh, untouched import can replace stale machine suggestions.
        # Once a person has reviewed a candidate or generated a map, only
        # append novel proposals; never rewrite their decisions or old map.
        retained=(list(page['candidates']) if has_reviewed or plan.get('generated_environment') else
                  [c for c in page['candidates'] if c.get('source') not in local_sources])
        used_ids={c['id'] for c in retained}
        def same_proposal(candidate,old):
            return (candidate['kind']==old['kind'] and
                all(abs(a-b)<=8 for a,b in zip(candidate['bbox_px'],old['bbox_px'])))
        additions=[]
        for candidate in proposals:
            if any(same_proposal(candidate,old) for old in retained+additions):
                continue
            if candidate['id'] in used_ids:
                candidate['id']=f"retry-{revision}-{candidate['id']}"
            used_ids.add(candidate['id'])
            additions.append(candidate)
        if not additions and len(retained)==len(page['candidates']):
            return plan
        if len(retained)+len(additions)>500:
            raise ValueError('재분석 후보가 층당 검토 한도 500개를 초과합니다')
        page['candidates']=[*retained,*additions]
        plan['revision']+=1
        plan['review_status']='review_required'
        self._save(plan)
        return plan

    def save_visual_drafts(self, plan_id, revision, page_number, response):
        """Append bounded model visual proposals; never mark them as observed facts."""
        plan=self._load(plan_id)
        if type(revision) is not int or plan['revision']!=revision:
            raise ValueError('도면이 변경됐습니다. 최신 검토 버전을 다시 불러오세요')
        if type(page_number) is not int or not 1<=page_number<=len(plan['pages']):
            raise ValueError('도면 페이지가 없습니다')
        if not isinstance(response,dict) or not isinstance(response.get('candidates'),list) or not isinstance(response.get('labels'),list):
            raise ValueError('이미지 분석 응답 형식이 올바르지 않습니다')
        page=plan['pages'][page_number-1]
        if any(c['source']=='model_visual_draft' and c['status']=='proposed' for c in page['candidates']):
            raise ValueError('이전 AI 시각 후보를 먼저 확정하거나 제외하세요')
        existing=list(page['candidates']);drafts=[];labels=[];omitted=[]
        for i,row in enumerate(response['candidates'][:50]):
            try:
                if not isinstance(row,dict) or set(row)-{'kind','name','bbox_px'} or row.get('kind') not in KINDS:
                    raise ValueError('종류 오류')
                name=row.get('name')
                if not isinstance(name,str) or not name.strip() or len(name)>120:
                    raise ValueError('이름 오류')
                box=_box(row.get('bbox_px'),page['width_px'],page['height_px'])
                if box[2]-box[0]<5 or box[3]-box[1]<5:
                    raise ValueError('너무 작은 경계')
            except ValueError:
                omitted.append('후보 위치·종류 오류');continue
            # An exact-ish duplicate of an already reviewed image proposal
            # adds no useful choice and may make a dense sheet harder to review.
            def overlap(other):
                a=other['bbox_px'];ix=max(0,min(box[2],a[2])-max(box[0],a[0]));iy=max(0,min(box[3],a[3])-max(box[1],a[1]))
                union=(box[2]-box[0])*(box[3]-box[1])+(a[2]-a[0])*(a[3]-a[1])-ix*iy
                return ix*iy/union if union else 0.
            if any(c['kind']==row['kind'] and overlap(c)>.7 for c in existing+drafts):
                omitted.append('기존 후보와 겹침');continue
            drafts.append(dict(id=f'vision-{revision}-{page_number}-{i}',kind=row['kind'],name=name.strip(),
                bbox_px=box,status='proposed',source='model_visual_draft',served_floors=[],
                evidence='Codex 이미지 시각 제안; 원본의 문자·경계·시설 종류와 위치를 사용자가 확인해야 함'))
        for row in response['labels'][:50]:
            try:
                if not isinstance(row,dict) or set(row)-{'text','bbox_px'} or not isinstance(row.get('text'),str) or not row['text'].strip() or len(row['text'])>160:
                    raise ValueError('문자 오류')
                box=_box(row.get('bbox_px'),page['width_px'],page['height_px'])
            except ValueError:
                omitted.append('문자 위치·형식 오류');continue
            labels.append(dict(text=row['text'].strip(),bbox_px=box,source='model_visual_draft'))
        if len(existing)+len(drafts)>500:raise ValueError('모델 후보를 더하면 층당 검토 한도 500개를 초과합니다')
        page['candidates']=existing+drafts
        page['text_labels']+=labels
        page['visual_draft']=dict(model_execution=response.get('model_execution'),
            notes=str(response.get('notes',''))[:2000],added_candidates=len(drafts),added_labels=len(labels),
            omitted=omitted,original_ocr_status=page.get('ocr_status'),review_required=True)
        # Unreviewed visual suggestions cannot change the already generated
        # environment. Keep its provenance usable while the new drafts await
        # human review; a subsequent material review invalidates it instead.
        plan.update(revision=revision+1,review_status='review_required')
        self._save(plan)
        return plan

    def split_page_into_floors(self, plan_id, payload):
        """Create separately reviewable floors from one multi-plan sheet.

        The user supplies crop regions and floor names. We retain the parent
        drawing and never pretend that a floor label proves a region boundary.
        """
        parent=self._load(plan_id)
        if not isinstance(payload,dict) or set(payload)!={'revision','page_number','regions'} or payload['revision']!=parent['revision']:
            raise ValueError('분리할 도면의 최신 버전을 확인하세요')
        number=payload['page_number']
        if type(number) is not int or not 1<=number<=len(parent['pages']):
            raise ValueError('분리할 도면 쪽을 확인하세요')
        regions=payload['regions']
        if not isinstance(regions,list) or not 2<=len(regions)<=MAX_PAGES-len(parent['pages'])+1:
            raise ValueError('한 쪽에서 구분할 층 영역은 2개 이상, 총 12층 이하여야 합니다')
        source=parent['pages'][number-1]
        normalized=[]
        for region in regions:
            if not isinstance(region,dict) or set(region)!={'bbox_px','name','elevation_m'}:
                raise ValueError('층 영역의 위치·이름·기준 높이를 입력하세요')
            box=_box(region['bbox_px'],source['width_px'],source['height_px'])
            if box[2]-box[0]<100 or box[3]-box[1]<100:
                raise ValueError('각 층 영역은 가로·세로 100px 이상이어야 합니다')
            name=region['name'];elevation=region['elevation_m']
            if not isinstance(name,str) or not name.strip() or len(name)>100 or type(elevation) not in (int,float) or not math.isfinite(elevation):
                raise ValueError('층 이름과 실제 층 기준 높이를 확인하세요')
            normalized.append(dict(bbox_px=box,name=name.strip(),elevation_m=float(elevation)))
        for i,left in enumerate(normalized):
            for right in normalized[i+1:]:
                a,b,c,d=left['bbox_px'];w,x,y,z=right['bbox_px']
                overlap=max(0,min(c,y)-max(a,w))*max(0,min(d,z)-max(b,x))
                if overlap>.01*min((c-a)*(d-b),(y-w)*(z-x)):
                    raise ValueError('층 영역이 겹칩니다. 각 층의 평면 범위를 따로 그리세요')
        normalized.sort(key=lambda row:(row['elevation_m'],row['name']))
        digest=hashlib.sha256(json.dumps(dict(parent=plan_id,revision=parent['revision'],page=number,regions=normalized),
                                       sort_keys=True).encode()).hexdigest()[:32]
        if self._path(digest).exists():return self._load(digest)
        pages=[]
        for old in parent['pages']:
            if old['number']!=number:
                page=deepcopy(old);page['number']=len(pages)+1
                pages.append(page)
                continue
            for region in normalized:
                x0,y0,x1,y1=region['bbox_px']
                x,y=round(x0),round(y0);width=round(x1)-x;height=round(y1)-y
                raster=self.folder/f'{digest}-page-{len(pages)+1}.png'
                _command(['ffmpeg','-v','error','-i',str(self.folder/old['image_name']),'-vf',
                          f'crop={width}:{height}:{x}:{y}','-frames:v','1','-y',str(raster)],timeout=35)
                pixels=_ppm(_command(['ffmpeg','-v','error','-i',str(raster),'-frames:v','1',
                                      '-f','image2pipe','-vcodec','ppm','-'],timeout=35))
                words=[]
                for word in old['text_labels']:
                    a,b,c,d=word['bbox_px'];cx=(a+c)/2;cy=(b+d)/2
                    if x<=cx<x+width and y<=cy<y+height:
                        words.append(dict(word,bbox_px=[max(0,a-x),max(0,b-y),min(width,c-x),min(height,d-y)]))
                candidates,words=_proposals(pixels,words)
                pages.append(dict(number=len(pages)+1,width_px=width,height_px=height,
                                  name=region['name'],elevation_m=region['elevation_m'],
                                  elevation_basis='사용자가 원본 시트를 층별로 구분하고 입력',
                                  scale=old['scale'],scale_basis=old['scale_basis'],
                                  candidates=candidates,text_labels=words,
                                  recognized_annotations=_annotations(words),ocr_status=old['ocr_status'],
                                  image_name=raster.name,source_region=dict(parent_plan_id=plan_id,
                                  parent_page=number,bbox_px=region['bbox_px'])))
        derived=dict(id=digest,title=parent['title']+' · 층별 분리',sha256=parent['sha256'],
                     source_format=parent['source_format'],revision=1,pages=pages,
                     review_status='review_required',generated_environment=None,
                     parent_plan_id=plan_id,parent_revision=parent['revision'])
        self._save(derived)
        return derived

    def review(self, plan_id, payload):
        plan=self._load(plan_id)
        if not isinstance(payload,dict) or set(payload)!={'revision','pages'} or payload['revision']!=plan['revision']:
            raise ValueError('검토 중 도면이 바뀌었습니다. 최신 버전을 다시 불러오세요')
        if not isinstance(payload['pages'],list) or len(payload['pages'])!=len(plan['pages']):
            raise ValueError('모든 층의 검토 정보가 필요합니다')
        pages=[]
        for old,row in zip(plan['pages'],payload['pages']):
            if not isinstance(row,dict) or set(row)-{'name','elevation_m','calibration','candidates','text_labels'}:
                raise ValueError('층 검토 필드가 올바르지 않습니다')
            name=row.get('name')
            elevation=row.get('elevation_m')
            if not isinstance(name,str) or not name.strip() or len(name)>100 or type(elevation) not in (int,float) or not math.isfinite(elevation):
                raise ValueError('층 이름과 실제 층 높이를 확인하세요')
            calibration=row.get('calibration')
            if calibration is None:
                scale=None; basis='미입력';saved_calibration=None
            else:
                if not isinstance(calibration,dict) or not {'pixels','metres'}<=set(calibration) or set(calibration)-{'pixels','metres','basis','evidence'}:
                    raise ValueError('축척 보정은 도면 픽셀 거리와 실제 미터 거리가 필요합니다')
                pixels,metres=calibration['pixels'],calibration['metres']
                if any(type(v) not in (int,float) or not math.isfinite(v) or v<=0 for v in (pixels,metres)):
                    raise ValueError('축척 거리는 양의 유한한 값이어야 합니다')
                scale=metres/pixels
                if not .0001<=scale<=2: raise ValueError('축척이 비정상적입니다. 픽셀·미터를 다시 확인하세요')
                basis_kind=calibration.get('basis','unknown')
                basis_labels={'drawing':'사용자가 확인한 도면 표기','measured':'사용자 제공 실측값',
                              'assumed':'시험 가정(실측 아님)','unknown':'입력 출처 미확인(실측 아님)'}
                if basis_kind not in basis_labels:
                    raise ValueError('축척 근거는 도면 표기·실측값·시험 가정 중에서 선택하세요')
                evidence=calibration.get('evidence','')
                if not isinstance(evidence,str) or len(evidence)>200:
                    raise ValueError('축척 근거 설명은 200자 이하로 입력하세요')
                evidence=evidence.strip()
                if basis_kind in ('drawing','measured') and not evidence:
                    raise ValueError('도면 표기 또는 실측값의 위치·출처를 입력하세요')
                basis=f'{basis_labels[basis_kind]}: {pixels:g} px = {metres:g} m'
                if evidence: basis+=f' · {evidence}'
                saved_calibration=dict(pixels=float(pixels),metres=float(metres),basis=basis_kind,evidence=evidence)
            labels=row.get('text_labels')
            if labels is None:
                reviewed_labels=old.get('text_labels',[])
            else:
                originals=old.get('text_labels',[])
                if not isinstance(labels,list) or len(labels)!=len(originals):
                    raise ValueError('인식 문자 목록이 변경됐습니다. 최신 도면을 다시 불러오세요')
                reviewed_labels=[]
                for original,choice in zip(originals,labels):
                    if not isinstance(choice,dict) or set(choice)-{'text','review_status','review_note'}:
                        raise ValueError('인식 문자 검토 필드가 올바르지 않습니다')
                    text=choice.get('text')
                    status=choice.get('review_status','raw')
                    note=choice.get('review_note','')
                    source_text=original.get('original_text',original['text'])
                    previous_status=original.get('review_status','raw')
                    if (not isinstance(text,str) or not text.strip() or len(text)>160 or
                            status not in ('raw','confirmed','corrected','rejected') or
                            not isinstance(note,str) or len(note)>400):
                        raise ValueError('인식 문자와 판정 사유를 확인하세요')
                    if (status=='raw' and (text!=source_text or previous_status!='raw') or
                            status=='confirmed' and text!=source_text or
                            status=='corrected' and text==source_text or
                            status!='raw' and not note.strip()):
                        raise ValueError('문자 정정·제외에는 원본과 대조한 사유가 필요합니다')
                    reviewed_labels.append(dict(original,text=text,original_text=source_text,
                                                review_status=status,review_note=note.strip()))
            candidates=row.get('candidates')
            if not isinstance(candidates,list) or len(candidates)>500:
                raise ValueError('층당 객체는 500개 이하로 검토하세요')
            previous={c['id']:c for c in old['candidates']}
            seen=set(); reviewed=[]
            for candidate in candidates:
                if not isinstance(candidate,dict) or set(candidate)-{'id','kind','name','bbox_px','status','source','evidence','served_floors','connects','clear_width_px','clear_opening_bbox_px','vertical_link_id'}:
                    raise ValueError('객체 검토 필드가 올바르지 않습니다')
                cid,kind,status=candidate.get('id'),candidate.get('kind'),candidate.get('status')
                if not isinstance(cid,str) or not re.fullmatch(r'[A-Za-z0-9_-]{1,80}',cid) or cid in seen:
                    raise ValueError('객체 식별자가 중복되거나 올바르지 않습니다')
                seen.add(cid)
                if kind not in KINDS or status not in ('proposed','confirmed','rejected','deferred'):
                    raise ValueError('객체 종류와 검토 상태를 확인하세요')
                label=candidate.get('name')
                if not isinstance(label,str) or not label.strip() or len(label)>120: raise ValueError('객체 이름을 확인하세요')
                box=_box(candidate.get('bbox_px'),old['width_px'],old['height_px'])
                source_kind=candidate.get('source','user_added')
                if source_kind not in ('image_geometry','enclosed_geometry','model_visual_draft','user_added'):
                    raise ValueError('객체 출처가 올바르지 않습니다')
                evidence=candidate.get('evidence','')
                if not isinstance(evidence,str):
                    raise ValueError('원본 대조 근거를 글로 입력하세요')
                prior=previous.get(cid)
                if status=='confirmed' and (prior is None or prior.get('status')!='confirmed'):
                    # A generated proposal's text says only that it *needs*
                    # review. Clicking Confirm must record a distinct human
                    # decision before it can affect graph or physics.
                    if (not evidence.strip() or
                            (prior is not None and evidence.strip()==prior.get('evidence','').strip()) or
                            evidence.strip()=='사용자가 원본 도면 위에서 추가한 후보'):
                        raise ValueError(f'{label}: 확정 전에 원본과 대조한 위치·형상 근거를 입력하세요')
                served=candidate.get('served_floors',[])
                if not isinstance(served,list) or any(not isinstance(v,int) or not 1<=v<=len(plan['pages']) for v in served):
                    raise ValueError('층간 시설의 연결 층 번호를 확인하세요')
                vertical_link=candidate.get('vertical_link_id','')
                if (not isinstance(vertical_link,str) or len(vertical_link)>100 or
                    (vertical_link.strip() and kind not in ('stairs','elevator'))):
                    raise ValueError('계단·승강기에서만 같은 시설의 연결 이름을 지정하세요')
                vertical_link=vertical_link.strip()
                connects=candidate.get('connects',[])
                if not isinstance(connects,list) or len(connects) not in (0,2) or any(not isinstance(v,str) for v in connects) or len(set(connects))!=len(connects):
                    raise ValueError('문·개방 통로의 연결 공간은 서로 다른 공간 두 곳을 선택하세요')
                if connects and kind not in ('door','opening'):
                    raise ValueError('연결 공간은 문이나 개방 통로에만 지정할 수 있습니다')
                clear_width=candidate.get('clear_width_px')
                if clear_width is not None and (kind not in ('door','opening') or type(clear_width) not in (int,float)
                                                or not math.isfinite(clear_width) or clear_width<=0
                                                or clear_width>max(box[2]-box[0],box[3]-box[1])):
                    raise ValueError('문·개방 통로의 실제 개구 폭은 후보 상자 안의 양의 픽셀 거리여야 합니다')
                clear_box=None
                if candidate.get('clear_opening_bbox_px') is not None:
                    if kind not in ('door','opening'):
                        raise ValueError('실제 개구 범위는 문·개방 통로에만 지정할 수 있습니다')
                    clear_box=_box(candidate['clear_opening_bbox_px'],old['width_px'],old['height_px'])
                    if not (box[0]<=clear_box[0]<clear_box[2]<=box[2] and
                            box[1]<=clear_box[1]<clear_box[3]<=box[3]):
                        raise ValueError('실제 개구 범위는 원본 후보 상자 안에 있어야 합니다')
                    if clear_width is None:
                        raise ValueError('실제 개구 범위를 지정했다면 통과 방향의 개구 폭도 입력하세요')
                    nearby_walls=[wall for wall in candidates if isinstance(wall,dict)
                                  and wall.get('kind')=='wall' and wall.get('status')=='confirmed'
                                  and isinstance(wall.get('bbox_px'),list) and len(wall['bbox_px'])==4
                                  and wall['bbox_px'][0]<=box[2]+2 and box[0]<=wall['bbox_px'][2]+2
                                  and wall['bbox_px'][1]<=box[3]+2 and box[1]<=wall['bbox_px'][3]+2]
                    width_axes=(clear_box[2]-clear_box[0],clear_box[3]-clear_box[1])
                    if nearby_walls:
                        wall=max(nearby_walls,key=lambda row:max(row['bbox_px'][2]-row['bbox_px'][0],
                                                                  row['bbox_px'][3]-row['bbox_px'][1]))
                        horizontal=wall['bbox_px'][2]-wall['bbox_px'][0]>=wall['bbox_px'][3]-wall['bbox_px'][1]
                        expected_width=width_axes[0 if horizontal else 1]
                        if not math.isclose(expected_width,clear_width,abs_tol=.1):
                            raise ValueError('확정 벽의 방향과 실제 개구 범위·입력 폭이 다릅니다')
                    elif not any(math.isclose(axis,clear_width,abs_tol=.1) for axis in width_axes):
                        raise ValueError('실제 개구 범위와 입력한 개구 폭이 다릅니다')
                reviewed.append(dict(id=cid,kind=kind,name=label,bbox_px=box,status=status,source=source_kind,
                                     evidence=evidence[:400],served_floors=served,
                                     connects=connects,**({'clear_width_px':float(clear_width)} if clear_width is not None else {}),
                                     **({'clear_opening_bbox_px':clear_box} if clear_box is not None else {}),
                                     **({'vertical_link_id':vertical_link} if vertical_link else {})))
            links=[(c['kind'],c['vertical_link_id']) for c in reviewed if c['status']=='confirmed' and c.get('vertical_link_id')]
            if len(links)!=len(set(links)):
                raise ValueError('같은 층의 두 시설에 동일한 층간 연결 이름을 사용할 수 없습니다')
            confirmed_zones={c['id'] for c in reviewed if c['status']=='confirmed' and c['kind'] in ('room','corridor')}
            if any(any(endpoint not in confirmed_zones for endpoint in c['connects']) for c in reviewed if c['status']=='confirmed'):
                raise ValueError('연결 공간은 이 층에서 확정한 방·복도 두 곳이어야 합니다')
            pages.append(dict(old,name=name,elevation_m=float(elevation),scale=scale,scale_basis=basis,
                              calibration=saved_calibration,candidates=reviewed,text_labels=reviewed_labels,
                              recognized_annotations=_annotations(reviewed_labels)))
        def confirmed_geometry(page):
            calibration=page.get('calibration')
            basis=(calibration.get('basis'),calibration.get('evidence','')) if calibration else page['scale_basis']
            return (page['name'],page['elevation_m'],page['scale'],basis,
                    sorted((c['id'],c['kind'],c['name'],tuple(c['bbox_px']),tuple(c.get('served_floors',[])),c.get('vertical_link_id',''),tuple(c.get('connects',[])),c.get('clear_width_px'),tuple(c.get('clear_opening_bbox_px',[])))
                           for c in page['candidates'] if c['status']=='confirmed'))
        geometry_changed=any(confirmed_geometry(old)!=confirmed_geometry(new)
                             for old,new in zip(plan['pages'],pages))
        has_deferred=any(c['status']=='deferred' for p in pages for c in p['candidates'])
        plan.update(revision=plan['revision']+1,pages=pages,
                    review_status='review_required' if geometry_changed or not plan.get('generated_environment')
                                  else 'generated_partial' if has_deferred else 'generated',
                    generated_environment=None if geometry_changed else plan.get('generated_environment'))
        self._save(plan)
        return plan

    def generate(self, plan_id, revision, project):
        plan=self._load(plan_id)
        if revision!=plan['revision']: raise ValueError('도면 검토 버전이 바뀌었습니다. 최신 버전을 확인하세요')
        if any(p['scale'] is None for p in plan['pages']): raise ValueError('모든 층의 축척 픽셀·미터 비율을 입력하세요. 시험 가정은 실제 건물 치수로 간주하지 않습니다')
        if any(c['status']=='proposed' for p in plan['pages'] for c in p['candidates']):
            raise ValueError('모든 객체 후보를 확정하거나 제외하세요')
        floors=[]; elements=[]
        for p in plan['pages']:
            fid=f'{plan_id[:10]}-floor-{p["number"]}'
            scale=p['scale']
            floors.append(Floor(id=fid,name=p['name'],elevation=p['elevation_m'],
                                width=p['width_px']*scale,depth=p['height_px']*scale))
            confirmed=[c for c in p['candidates'] if c['status']=='confirmed']
            apertures=[c for c in confirmed if c['kind'] in ('door','opening')]
            def aperture_box(candidate, horizontal):
                """Use the reviewed clear gap, not the door swing symbol, for physics."""
                if candidate.get('clear_opening_bbox_px') is not None:
                    return candidate['clear_opening_bbox_px']
                x0,y0,x1,y1=candidate['bbox_px']
                clear=candidate.get('clear_width_px')
                if clear is None:
                    # A symbol box may include a long door-swing arc. The
                    # graph already uses its short axis as an uncertain upper
                    # bound; cutting the whole box from a wall would create a
                    # wider physical passage than planning had approved.
                    clear=min(x1-x0,y1-y0)
                if horizontal:
                    center=(x0+x1)/2
                    return [center-clear/2,y0,center+clear/2,y1]
                center=(y0+y1)/2
                return [x0,center-clear/2,x1,center+clear/2]
            def aperture_horizontal(candidate):
                x0,y0,x1,y1=candidate['bbox_px']
                nearby=[wall for wall in confirmed if wall['kind']=='wall' and
                        wall['bbox_px'][0]<=x1+2 and x0<=wall['bbox_px'][2]+2 and
                        wall['bbox_px'][1]<=y1+2 and y0<=wall['bbox_px'][3]+2]
                if nearby:
                    wall=max(nearby,key=lambda row:max(row['bbox_px'][2]-row['bbox_px'][0],
                                                        row['bbox_px'][3]-row['bbox_px'][1]))
                    box=wall['bbox_px']
                    return box[2]-box[0]>=box[3]-box[1]
                return x1-x0<=y1-y0
            def aperture_targets_wall(candidate, wall_box, horizontal):
                """A swing-symbol corner must not cut a neighboring wall.

                A reviewed clear-gap box identifies the wall line directly.
                Without one, require the symbol centre to sit on that line;
                overlap of the wide swing-symbol box alone is not evidence of
                a passage through this particular wall.
                """
                a,b,d,e=wall_box
                clear=candidate.get('clear_opening_bbox_px')
                if horizontal:
                    wall_line=(b+e)/2
                    if clear is not None:
                        return clear[1]-2<=wall_line<=clear[3]+2
                    symbol=candidate['bbox_px']
                    return b-2<=(symbol[1]+symbol[3])/2<=e+2
                wall_line=(a+d)/2
                if clear is not None:
                    return clear[0]-2<=wall_line<=clear[2]+2
                symbol=candidate['bbox_px']
                return a-2<=(symbol[0]+symbol[2])/2<=d+2
            for c in confirmed:
                box=c['bbox_px']; x0,y0,x1,y1=box
                if c['kind']=='wall':
                    fragments=[box]
                    for aperture in apertures:
                        next_parts=[]
                        for a,b,d,e in fragments:
                            horizontal=d-a>=e-b
                            if not aperture_targets_wall(aperture,(a,b,d,e),horizontal):
                                next_parts.append([a,b,d,e])
                                continue
                            dx0,dy0,dx1,dy1=aperture_box(aperture,horizontal)
                            if horizontal and b<=dy1 and dy0<=e and a<dx1 and dx0<d:
                                if dx0-a>2: next_parts.append([a,b,min(dx0,d),e])
                                if d-dx1>2: next_parts.append([max(dx1,a),b,d,e])
                            elif not horizontal and a<=dx1 and dx0<=d and b<dy1 and dy0<e:
                                if dy0-b>2: next_parts.append([a,b,d,min(dy0,e)])
                                if e-dy1>2: next_parts.append([a,max(dy1,b),d,e])
                            else: next_parts.append([a,b,d,e])
                        fragments=next_parts
                elif c['kind'] in ('door','opening'):
                    fragments=[aperture_box(c,aperture_horizontal(c))]
                else: fragments=[box]
                for k,part in enumerate(fragments):
                    a,b,d,e=part
                    # Existing physical environment uses rectangular footprints.
                    # A PDF's elevation/material is not inferred: explicit defaults.
                    element=Element(id=f'{fid}-{c["id"]}-{k}',kind=c['kind'],name=c['name'],floor_id=fid,
                                    pose=Pose(x=(a+d)*scale/2,y=(p['height_px']-(b+e)/2)*scale),
                                    size=Size(x=max(.02,(d-a)*scale),y=max(.02,(e-b)*scale),
                                              z=.05 if c['kind'] in ('room','corridor') else 2.4 if c['kind']=='wall' else 2.1))
                    if c['kind'] in ('stairs','elevator'):
                        element.facility.served_floors=[f'{plan_id[:10]}-floor-{n}' for n in c.get('served_floors',[])]
                    elements.append(element)
        if not any(e.kind in ('room','corridor') for e in elements):
            raise ValueError('확정한 방 또는 복도가 필요합니다')
        environment=Environment(id=f'floorplan-{plan_id}',name=plan['title'],version=plan['revision'],floors=floors,elements=elements)
        graph=self._graph(plan,elements)
        environment.reviewed_topology=graph
        # New map is an editor draft; existing project and its execution are
        # untouched. Placements/tasks must be made on the reviewed new map.
        raw=project.model_dump(mode='json')
        raw.update(name=f'{plan["title"]} · 운영 초안',environment=environment.model_dump(mode='json'),
                   robots=[],people=[],items=[],tasks=[],faults=[],revision=1)
        payload=Project.model_validate(raw).model_dump(mode='json')
        deferred_count=sum(c['status']=='deferred' for p in plan['pages'] for c in p['candidates'])
        plan['generated_environment']=dict(revision=plan['revision'],environment=environment.model_dump(mode='json'),
                                           graph=graph,project=payload,
                                           limits=['재질: concrete 기본값','벽 높이: 2.4 m 기본값','문 높이: 2.1 m 기본값',
                                                   '도면에서 문 작동 방식은 알 수 없어 시뮬레이션은 수직 상승문 기본값 사용',
                                                   '인식되지 않은 문·시설은 추가·확정 전 통행 불가',
                                                   '기존 로봇·작업 위치는 새 지도에 자동 재배치하지 않음']+
                                                  ([f'미검토 후보 {deferred_count}개는 이 지도에서 제외; 부분 검토 지도'] if deferred_count else []))
        plan['review_status']='generated_partial' if deferred_count else 'generated'
        self._save(plan)
        return deepcopy(plan['generated_environment'])

    def _graph(self, plan, elements):
        zones={e.id:e for e in elements if e.kind in ('room','corridor')}
        reviewed={f'{plan["id"][:10]}-floor-{page["number"]}-{c["id"]}-0':c
                  for page in plan['pages'] for c in page['candidates'] if c['status']=='confirmed'}
        edges=[]
        unlinked_apertures=[]
        for aperture in (e for e in elements if e.kind in ('door','opening')):
            # A reviewed aperture must touch exactly two zones. Adjacency or
            # closeness alone never grants passage through an unreviewed wall.
            adjacent=[]
            for z in zones.values():
                if z.floor_id!=aperture.floor_id: continue
                dx=abs(z.pose.x-aperture.pose.x);dy=abs(z.pose.y-aperture.pose.y)
                if dx<=z.size.x/2+aperture.size.x/2+.15 and dy<=z.size.y/2+aperture.size.y/2+.15:
                    adjacent.append(z.id)
            chosen=reviewed.get(aperture.id,{}).get('connects',[])
            if chosen:
                selected=[f'{aperture.floor_id}-{cid}-0' for cid in chosen]
                linked=selected if all(node in adjacent for node in selected) else []
            else:
                linked=adjacent if len(adjacent)==2 else []
            if len(linked)==2:
                candidate=reviewed.get(aperture.id,{})
                page=next(p for p in plan['pages'] if aperture.floor_id==f'{plan["id"][:10]}-floor-{p["number"]}')
                reviewed_width=candidate.get('clear_width_px')
                edges.append(dict(from_id=linked[0],to_id=linked[1],via=aperture.id,
                                  width_m=reviewed_width*page['scale'] if reviewed_width is not None else min(aperture.size.x,aperture.size.y),
                                  condition='reviewed_door' if aperture.kind=='door' else 'reviewed_opening'))
            else:
                unlinked_apertures.append(dict(id=aperture.id,name=aperture.name,kind=aperture.kind,
                                               floor_id=aperture.floor_id,adjacent_zones=adjacent,
                                               reason=('지정한 공간 두 곳 모두와 위치가 맞닿지 않습니다. 원본 위치·경계를 확인하세요'
                                                       if chosen else '확정한 서로 다른 공간 두 곳과 맞닿아야 통행 연결을 만들 수 있습니다')))
        for facility in (e for e in elements if e.kind in ('stairs','elevator')):
            for zone in zones.values():
                accessible_floors=facility.facility.served_floors if facility.kind=='elevator' else [facility.floor_id]
                if (zone.floor_id in accessible_floors and
                    abs(zone.pose.x-facility.pose.x)<=zone.size.x/2 and
                    abs(zone.pose.y-facility.pose.y)<=zone.size.y/2):
                    edges.append(dict(from_id=zone.id,to_id=facility.id,via=facility.id,
                                      width_m=min(facility.size.x,facility.size.y),condition='reviewed_landing_zone'))
            # Explicit served-floor evidence is retained in the facility;
            # cross-floor route edges require a corresponding reviewed landing.
            source_link=reviewed.get(facility.id,{}).get('vertical_link_id','')
            for peer in (e for e in elements if e.kind==facility.kind and e.id!=facility.id and
                         ((source_link and reviewed.get(e.id,{}).get('vertical_link_id','')==source_link)
                          or (not source_link and not reviewed.get(e.id,{}).get('vertical_link_id')
                              and e.name==facility.name))):
                if peer.floor_id in facility.facility.served_floors and facility.floor_id in peer.facility.served_floors:
                    if facility.id<peer.id:
                        edges.append(dict(from_id=facility.id,to_id=peer.id,via=facility.kind,
                                          width_m=min(facility.size.x,facility.size.y,peer.size.x,peer.size.y),condition='reviewed_both_landings'))
        zone_adjacency={zone_id:set() for zone_id in zones}
        for edge in edges:
            if edge['from_id'] in zones and edge['to_id'] in zones:
                zone_adjacency[edge['from_id']].add(edge['to_id'])
                zone_adjacency[edge['to_id']].add(edge['from_id'])
        components=[];remaining=set(zones)
        while remaining:
            start=min(remaining);group={start};frontier=[start];remaining.remove(start)
            while frontier:
                for other in sorted(zone_adjacency[frontier.pop()] & remaining):
                    remaining.remove(other);group.add(other);frontier.append(other)
            components.append(sorted(group))
        overlapping_zones=[]
        zone_list=list(zones.values())
        for index,left in enumerate(zone_list):
            for right in zone_list[index+1:]:
                if left.floor_id!=right.floor_id:
                    continue
                left_x=(left.pose.x-left.size.x/2,left.pose.x+left.size.x/2)
                right_x=(right.pose.x-right.size.x/2,right.pose.x+right.size.x/2)
                left_y=(left.pose.y-left.size.y/2,left.pose.y+left.size.y/2)
                right_y=(right.pose.y-right.size.y/2,right.pose.y+right.size.y/2)
                area=max(0,min(left_x[1],right_x[1])-max(left_x[0],right_x[0])) * max(
                    0,min(left_y[1],right_y[1])-max(left_y[0],right_y[0]))
                smaller=min(left.size.x*left.size.y,right.size.x*right.size.y)
                if smaller>0 and area/smaller>=.8:
                    overlapping_zones.append(dict(first_id=left.id,second_id=right.id,
                                                  floor_id=left.floor_id,
                                                  smaller_covered_ratio=round(area/smaller,3)))
        return dict(nodes=[dict(id=e.id,name=e.name,kind=e.kind,floor_id=e.floor_id) for e in elements if e.kind in ('room','corridor','stairs','elevator')],
                    containment=[dict(container=e.floor_id,member=e.id) for e in elements if e.kind in ('room','corridor')],
                    connections=edges,resources=[e.id for e in elements if e.kind in ('charger','dock','loading','elevator')],
                    isolated_zones=sorted(node for node,neighbors in zone_adjacency.items() if not neighbors),
                    zone_components=components,unlinked_apertures=unlinked_apertures,
                    overlapping_zones=overlapping_zones,
                    source_plan_id=plan['id'],source_revision=plan['revision'])

    def context(self, project):
        eid=project.environment.id
        if not eid.startswith('floorplan-'):
            topology=project.environment.reviewed_topology
            if isinstance(topology,dict) and topology.get('source_plan_id'):
                return {'status':'stale','reason':'도면 출처 식별자가 현재 환경에서 끊어졌습니다. 검토 도면에서 지도를 다시 생성하세요'}
            return None
        try: plan=self._load(eid.removeprefix('floorplan-'))
        except ValueError: return {'status':'missing','reason':'도면 근거를 찾지 못했습니다'}
        generated=plan.get('generated_environment')
        if not generated or generated['revision']!=project.environment.version:
            return {'status':'stale','reason':'도면 확정 버전과 현재 환경이 다릅니다. 도면을 다시 검토하세요'}
        original=generated['environment']==project.environment.model_dump(mode='json')
        scale_basis=[(f'입력 출처 미확인(실측 아님): 100 px = {p["scale"]*100:g} m'
                      if p.get('scale') is not None and not p.get('calibration') else p['scale_basis'])
                     for p in plan['pages']]
        return dict(status='confirmed' if original else 'user_edited',
                    graph=generated['graph'] if original else self._graph(plan,project.environment.elements),
                    scale_basis=scale_basis,
                    limits=generated['limits'])
