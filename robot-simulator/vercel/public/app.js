const start = document.querySelector('#start');
const stop = document.querySelector('#stop');
const status = document.querySelector('#status');
let session = null;
function message(text, error = false) {status.textContent = text; status.classList.toggle('error', error);}
async function call(method) {
  const response = await fetch('/api/session', {method, credentials: 'same-origin', cache: 'no-store'});
  let result;
  try {result = await response.json();}
  catch {throw new Error('실행 서버에 연결할 수 없습니다. 잠시 후 다시 시도해 주세요.');}
  if (!response.ok) throw new Error(result.error || '연결에 실패했습니다. 다시 시도해 주세요.');
  return result;
}
function render() {
  start.disabled = false;
  start.textContent = session ? '열린 체험으로 이동 →' : '시뮬레이터 체험 시작 →';
  stop.hidden = !session;
  if (session) {
    const end = session.expiresAt ? new Date(session.expiresAt).toLocaleTimeString('ko-KR', {hour:'2-digit', minute:'2-digit'}) : '30분 이내';
    message(`체험 공간이 준비되었습니다. 종료 예정: ${end}.`);
  }
}
start.addEventListener('click', async () => {
  start.disabled = true;
  message('로봇과 물리 실행 환경을 준비하고 있습니다. 잠시만 기다려 주세요.');
  try {
    const result = await call('POST');
    session = result.session;
    render();
    // Same-tab navigation avoids blocked popups. Browser back returns to the session controls.
    location.assign(session.url);
  } catch (error) {render(); message(error.message, true);}
});
stop.addEventListener('click', async () => {
  stop.disabled = start.disabled = true;
  message('체험 공간을 종료하고 있습니다.');
  try {await call('DELETE'); session = null; render(); message('체험이 종료되었습니다. 임시 구성과 결과가 삭제됩니다.');}
  catch (error) {render(); message(error.message, true);}
  finally {stop.disabled = false;}
});
async function refresh() {
  try {session = (await call('GET')).session; render(); if (!session) message('새 체험 공간에서 시작합니다.');}
  catch (error) {render(); message(error.message, true);}
}
window.addEventListener('pageshow', refresh);
