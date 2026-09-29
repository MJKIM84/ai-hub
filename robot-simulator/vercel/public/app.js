const start = document.querySelector('#start');
const stop = document.querySelector('#stop');
const status = document.querySelector('#status');
const form = document.querySelector('#entry-form');
const password = document.querySelector('#password');
const passwordField = document.querySelector('#password-field');
let session = null;
let requiresPassword = true;
let busy = false;
function message(text, error = false) {status.textContent = text; status.classList.toggle('error', error);}
async function call(method, path='/api/session', body) {
  const response = await fetch(path, {method, credentials:'same-origin',cache:'no-store',
    ...(body ? {headers:{'Content-Type':'application/json'},body:JSON.stringify(body)} : {})});
  if(response.status===429 && path==='/api/access')throw new Error('입력 시도가 많습니다. 최대 10분 후 다시 시도해 주세요.');
  let result;
  try {result = await response.json();}
  catch {throw new Error('실행 서버에 연결할 수 없습니다. 잠시 후 다시 시도해 주세요.');}
  if (!response.ok) {
    if (response.status===401)requiresPassword=true;
    throw new Error(result.error || '연결에 실패했습니다. 다시 시도해 주세요.');
  }
  return result;
}
function render() {
  start.disabled = busy;
  start.textContent = busy ? '입장 준비 중…' : '시뮬레이션 시작하기';
  stop.hidden = !session;
  stop.disabled = busy;
  passwordField.hidden = !requiresPassword;
  password.required = requiresPassword;
  password.disabled = busy || !requiresPassword;
}
form.addEventListener('submit', async event => {
  event.preventDefault();
  if(busy)return;
  // Read before disabling; the password is never kept in browser storage.
  const submitted = password.value;
  if(requiresPassword && !submitted){password.focus();return;}
  busy=true;render();password.removeAttribute('aria-invalid');
  message(requiresPassword ? '비밀번호를 확인하고 있습니다.' : '로봇과 물리 실행 환경을 준비하고 있습니다.');
  try {
    if(requiresPassword){await call('POST','/api/access',{password:submitted});requiresPassword=false;password.value='';render();}
    message('로봇과 물리 실행 환경을 준비하고 있습니다. 잠시만 기다려 주세요.');
    const result = await call('POST');
    session = result.session;
    location.assign(session.url);
  } catch (error) {
    password.value='';busy=false;render();message(error.message,true);
    if(requiresPassword){password.setAttribute('aria-invalid','true');password.focus();}
  }
});
stop.addEventListener('click', async () => {
  busy=true;render();message('시뮬레이션 공간을 종료하고 있습니다.');
  try {await call('DELETE');session=null;message('시뮬레이션이 종료되었습니다. 임시 구성과 결과가 삭제됩니다.');}
  catch(error){message(error.message,true);}
  finally{busy=false;render();}
});
async function refresh() {
  busy=true;render();
  try {
    const result=await call('GET');session=result.session;requiresPassword=result.requiresPassword===true;
    message(requiresPassword ? '관리자 비밀번호를 입력해 주세요.' : session ? '열려 있는 시뮬레이션으로 다시 입장할 수 있습니다.' : '비밀번호 확인 완료. 시뮬레이션을 시작할 수 있습니다.');
  } catch(error){message(error.message,true);}
  finally{password.value='';busy=false;render();}
}
window.addEventListener('pageshow',refresh);
