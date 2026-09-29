import { runtimeEntry, runtimeSecret } from './access.mjs';
import { Sandbox } from '@vercel/sandbox';
import { isActive, ownerHash, slotNames, dayPrefix, errorStatus, publicSession } from './session-policy.mjs';

async function inventory() {
  // Includes stopped names: a used daily slot must never be recreated or resumed.
  const yesterday = new Date(Date.now() - 86_400_000);
  const groups = await Promise.all([dayPrefix(), dayPrefix(yesterday)].map(async namePrefix => {
    const result = await Sandbox.list({namePrefix, sortBy: 'name', sortOrder: 'desc', limit: 50});
    return result.toArray();
  }));
  return groups.flat();
}
export async function findSession(token) {
  const owner = ownerHash(token);
  const items = await inventory();
  return {items, item: items.find(x => isActive(x) && x.tags?.owner === owner)};
}
export async function loadSession(item) {
  // Do not implicitly restart a stopped VM when reading status.
  const sandbox = await Sandbox.get({name: item.name, resume: false});
  if (!isActive(sandbox)) return null;
  return sandbox;
}
async function ready(sandbox) {
  const url = sandbox.domain(8000);
  const end = Math.min(Date.now() + 90_000, sandbox.expiresAt?.getTime() ?? Infinity);
  while (Date.now() < end) {
    try {
      const response = await fetch(`${url}/healthz`, {signal: AbortSignal.timeout(5000), cache: 'no-store'});
      if (response.ok) {
        const state=await response.json();
        if (state.mode === 'personal_api' && state.access_required === true) return publicSession(sandbox);
      }
    } catch { /* Startup is bounded; failed readiness never returns a launch link. */ }
    await new Promise(resolve => setTimeout(resolve, 1000));
  }
  throw new Error('Runtime readiness timeout');
}
async function boot(sandbox, minutes, entrySecret) {
  const url = sandbox.domain(8000);
  await sandbox.runCommand({
    cmd: '/usr/bin/flock',
    args: ['-n', '/tmp/rop-server.lock', '/opt/rop-venv/bin/python', '-m', 'robot_platform.cloud'],
    cwd: '/opt/robot-app/robot-simulator', detached: true,
    env: {PYTHONPATH: '/opt/robot-app/robot-simulator/src',
      ROBOT_ENTRY_REQUIRED:'1', ROBOT_ENTRY_SECRET:entrySecret,
      ROBOT_PUBLIC_ORIGINS: url, ROBOT_MAX_VISITORS: '1',
      ROBOT_VISITOR_TTL_SECONDS: String(minutes * 60), ROBOT_KEY_TTL_SECONDS: String(Math.min(minutes * 60, 1800)),
      FORWARDED_ALLOW_IPS: '*', PORT: '8000', OMP_NUM_THREADS: '1', OPENBLAS_NUM_THREADS: '1'},
  });
  return ready(sandbox);
}
export async function launch(token, config, dependencies = {}) {
  const {find = findSession, load = loadSession, create = options => Sandbox.create(options), start = boot, wait = ready} = dependencies;
  const {items, item} = await find(token);
  if (item) {
    const existing = await load(item);
    if (existing) return runtimeEntry(await wait(existing),token,existing.name,config.access);
  }
  if (!config.snapshot) return {error: '실행 환경을 준비 중입니다. 잠시 후 다시 방문해 주세요.', status: 503};
  if (items.filter(isActive).length >= config.concurrent) return {error: '현재 시뮬레이션 공간이 모두 사용 중입니다. 잠시 후 다시 시도해 주세요.', status: 429};
  const used = new Set(items.map(x => x.name));
  for (const name of slotNames(config.daily)) {
    if (used.has(name)) continue;
    let sandbox;
    try {
      // Server-enforced unique names are the daily hard ceiling, even across concurrent functions.
      sandbox = await create({name, source: {type: 'snapshot', snapshotId: config.snapshot},
        resources: {vcpus: 2}, ports: [8000], timeout: config.minutes * 60_000,
        persistent: false, tags: {app: 'robot-lab', owner: ownerHash(token), access:'password-v1'},
      });
    } catch (error) {
      if (errorStatus(error) === 409) {
        const latest = await find(token);
        if (latest.item) {
          const existing = await load(latest.item);
          if (existing) return runtimeEntry(await wait(existing),token,existing.name,config.access);
        }
        continue;
      }
      throw error;
    }
    try { return runtimeEntry(await start(sandbox, config.minutes, runtimeSecret(token,sandbox.name,config.access.secret)),token,sandbox.name,config.access); }
    catch (error) { await sandbox.stop().catch(() => {}); throw error; }
  }
  return {error: '오늘의 시뮬레이션 제공 한도에 도달했습니다. 다음 날 다시 이용해 주세요. 기존 시뮬레이션은 계속 이용할 수 있습니다.', status: 429};
}
export async function stop(token) {
  const {item} = await findSession(token);
  if (item) {
    const sandbox = await loadSession(item);
    if (sandbox) await sandbox.stop();
  }
}
