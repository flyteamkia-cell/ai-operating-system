/**
 * Deterministic metric derivation. No model ever computes these.
 * Every function returns null on insufficient data rather than a plausible number.
 */
import type { MetricSnapshot, CompetitorPost } from '../core/domain.js';
import { MIN_SAMPLE_FOR_CLAIM } from '../core/domain.js';

const ratio = (n?: number, d?: number): number | null =>
  n == null || d == null || d <= 0 ? null : n / d;

export const saveRate = (m: MetricSnapshot) => ratio(m.saves, m.reach);
export const shareRate = (m: MetricSnapshot) => ratio(m.shares, m.reach);
export const followerConversion = (m: MetricSnapshot) => ratio(m.follows, m.reach);

/** Requires video length; without it, avg watch seconds is not comparable across posts. */
export const holdRate = (m: MetricSnapshot, durationSeconds?: number) =>
  ratio(m.avgWatchSeconds, durationSeconds);

export const engagementRate = (m: MetricSnapshot) =>
  ratio((m.likes ?? 0) + (m.comments ?? 0) + (m.saves ?? 0) + (m.shares ?? 0), m.reach);

/**
 * Competitor engagement proxy. Public signals only, normalized by follower count.
 * Comparable ONLY within the competitor set — never against own-account rates (ADR-0005).
 */
export const competitorProxy = (p: CompetitorPost) =>
  ratio(p.likeCount + p.commentsCount, p.followersAtCapture);

export function median(xs: number[]): number | null {
  const v = xs.filter(Number.isFinite).sort((a, b) => a - b);
  if (v.length === 0) return null;
  const mid = v.length >> 1;
  const hi = v[mid] as number;
  return v.length % 2 ? hi : ((v[mid - 1] as number) + hi) / 2;
}

export interface Comparison {
  status: 'inconclusive' | 'measured';
  n: number;
  variantMedian: number | null;
  baselineMedian: number | null;
  lift: number | null;
  reason?: string;
}

/**
 * The guardrail that stops narrative fabrication: below the sample threshold
 * the answer is 'inconclusive', and callers must surface it verbatim.
 */
export function compare(variant: number[], baseline: number[], minSample = MIN_SAMPLE_FOR_CLAIM): Comparison {
  const n = variant.length;
  if (n < minSample || baseline.length < minSample) {
    return {
      status: 'inconclusive', n, variantMedian: median(variant), baselineMedian: median(baseline),
      lift: null, reason: `sample below threshold (n=${n}, baseline=${baseline.length}, required=${minSample})`,
    };
  }
  const v = median(variant), b = median(baseline);
  return { status: 'measured', n, variantMedian: v, baselineMedian: b, lift: v != null && b ? v / b - 1 : null };
}
