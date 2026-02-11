function levenshteinDistance(a: string, b: string): number {
  const matrix: number[][] = [];
  for (let i = 0; i <= b.length; i++) matrix[i] = [i];
  for (let j = 0; j <= a.length; j++) matrix[0][j] = j;

  for (let i = 1; i <= b.length; i++) {
    for (let j = 1; j <= a.length; j++) {
      if (b[i - 1] === a[j - 1]) {
        matrix[i][j] = matrix[i - 1][j - 1];
      } else {
        matrix[i][j] = Math.min(
          matrix[i - 1][j - 1] + 1,
          matrix[i][j - 1] + 1,
          matrix[i - 1][j] + 1
        );
      }
    }
  }
  return matrix[b.length][a.length];
}

export function fuzzyMatch(query: string, target: string, maxDistance: number = 2): boolean {
  const q = query.toLowerCase();
  const t = target.toLowerCase();

  if (t.includes(q)) return true;

  const words = t.split(/\s+/);
  for (const word of words) {
    if (q.length >= 3 && levenshteinDistance(q, word) <= maxDistance) {
      return true;
    }
  }
  return false;
}

export function calculateRelevanceScore(query: string, fields: { name: string; description: string | null; tags: string; category: string }): number {
  const q = query.toLowerCase();
  let score = 0;

  if (fields.name.toLowerCase().includes(q)) score += 10;
  if (fields.name.toLowerCase().startsWith(q)) score += 5;

  if (fields.description?.toLowerCase().includes(q)) score += 3;

  if (fields.category.toLowerCase().includes(q)) score += 4;

  try {
    const tags: string[] = JSON.parse(fields.tags);
    for (const tag of tags) {
      if (tag.toLowerCase().includes(q)) score += 2;
    }
  } catch {}

  if (fuzzyMatch(q, fields.name)) score += 2;

  return score;
}
