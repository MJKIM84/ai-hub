import fs from 'fs';
import path from 'path';

// .env.production.local에서 CRON_SECRET 파싱
const envPath = path.resolve('.env.production.local');
const envContent = fs.readFileSync(envPath, 'utf8');
const lines = envContent.split('\n');

let cronSecret = '';
for (const line of lines) {
  const trimmed = line.trim();
  if (trimmed.startsWith('CRON_SECRET=') || trimmed.startsWith('CRON_SECRET =')) {
    cronSecret = trimmed.split('=').slice(1).join('=').replace(/^["']|["']$/g, '').trim();
    console.log('Found CRON_SECRET, length:', cronSecret.length);
    break;
  }
}

// 디버그: CRON_SECRET 못찾으면 키 목록 출력
if (!cronSecret) {
  const keys = lines.filter(l => l.includes('=')).map(l => l.split('=')[0].trim()).filter(Boolean);
  console.log('Available keys:', keys.join(', '));
}

if (!cronSecret) {
  console.error('CRON_SECRET not found');
  process.exit(1);
}

const baseUrl = 'https://findmy.ai.kr';
const mode = process.argv[2] || 'discover'; // 'discover' or 'articles'

console.log(`[${mode}] 크롤링 시작...`);

const res = await fetch(`${baseUrl}/api/cron/${mode}`, {
  headers: { Authorization: `Bearer ${cronSecret}` },
});

const data = await res.json();
console.log(`[${mode}] Status: ${res.status}`);
console.log(JSON.stringify(data, null, 2));
