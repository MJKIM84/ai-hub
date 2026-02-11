const GRAVITY = 1.8;

export function calculateGravityScore(
  points: number,
  createdAt: Date,
  gravity: number = GRAVITY
): number {
  const hoursAge = (Date.now() - createdAt.getTime()) / (1000 * 60 * 60);
  const denominator = Math.pow(hoursAge + 2, gravity);
  if (denominator === 0) return 0;
  return (points - 1) / denominator;
}

export function calculatePoints(clicks: number, upvotes: number): number {
  return clicks + upvotes * 2;
}
