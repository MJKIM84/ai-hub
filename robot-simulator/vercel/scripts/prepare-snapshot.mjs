// Run from vercel/ after linking the Vercel project and pulling .env.local.
// Only the public Git commit is downloaded; no local data, credentials or visitor state.
import { Sandbox } from '@vercel/sandbox';
import { writeFile } from 'node:fs/promises';
const revision = process.argv[2];
if (!/^[a-f0-9]{40}$/.test(revision || '')) throw new Error('Supply the reviewed public Git commit SHA.');
const sandbox = await Sandbox.create({
  name: `rop-build-${Date.now()}`, image: 'vercel/sandbox/universal',
  timeout: 20 * 60_000, resources: {vcpus: 2}, persistent: false,
  tags: {app: 'robot-lab-build'},
  source: {type: 'git', url: 'https://github.com/MJKIM84/ai-hub.git', revision, depth: 1},
});
console.log('Build sandbox:', sandbox.name);
async function run(cmd, args, extra = {}) {
  const result = await sandbox.runCommand({cmd, args, ...extra});
  if (result.exitCode !== 0) throw new Error(`${cmd} failed (${result.exitCode}): ${await result.stderr()}`);
  console.log(`${cmd}: done`);
}
try {
  await run('apt-get', ['update'], {sudo:true});
  await run('apt-get', ['install','-y','--no-install-recommends','libgl1','libegl1','libglfw3','ffmpeg','poppler-utils','python3-venv'], {sudo:true});
  await run('python3', ['-m','venv','/opt/rop-venv'], {sudo:true});
  await run('/opt/rop-venv/bin/pip', ['install','--no-cache-dir','-r','requirements.lock'], {sudo:true,cwd:'/vercel/sandbox/robot-simulator'});
  await run('npm', ['ci','--no-audit','--no-fund'], {cwd:'/vercel/sandbox/robot-simulator/web'});
  await run('npm', ['run','build'], {cwd:'/vercel/sandbox/robot-simulator/web'});
  await run('/opt/rop-venv/bin/python', ['-c','import mujoco; print(mujoco.__version__)']);
  // Remove build-only modules and Git history from the public runtime snapshot.
  await run('rm', ['-rf','/vercel/sandbox/.git','/vercel/sandbox/robot-simulator/web/node_modules']);
  const snapshot = await sandbox.snapshot({expiration:0});
  await writeFile('.snapshot.json', JSON.stringify({snapshotId:snapshot.snapshotId,revision,createdAt:new Date().toISOString()},null,2));
  console.log('Runtime snapshot:', snapshot.snapshotId);
} finally {await sandbox.stop().catch(() => {});}
