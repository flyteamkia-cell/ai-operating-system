/**
 * Domain types. Single source of truth for the identity spine.
 * Every downstream module imports from here; no structural duplication.
 */

export type ContentId = string & { readonly __brand: 'ContentId' };
export type PublicationId = string & { readonly __brand: 'PublicationId' };
export type ExperimentId = string & { readonly __brand: 'ExperimentId' };

export const CONTENT_ID_RE = /^c_\d{8}_[a-z0-9-]{3,48}$/;

export function contentId(date: Date, slug: string): ContentId {
  const d = date.toISOString().slice(0, 10).replace(/-/g, '');
  const s = slug.toLowerCase().trim().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 48);
  const id = `c_${d}_${s}`;
  if (!CONTENT_ID_RE.test(id)) throw new Error(`invalid content_id: ${id}`);
  return id as ContentId;
}

export type ContentFormat = 'reel' | 'carousel' | 'story' | 'post' | 'live' | 'article';
export type ContentStatus =
  | 'idea' | 'briefed' | 'recorded' | 'edited' | 'scheduled' | 'published' | 'archived';

/** Fixed comparison ages. Comparing posts at arbitrary ages is invalid. */
export type AgeBucket = 'h24' | 'h72' | 'd7' | 'd30';
export const AGE_BUCKET_HOURS: Record<AgeBucket, number> = { h24: 24, h72: 72, d7: 168, d30: 720 };

export interface Content {
  contentId: ContentId;
  slug: string;
  format: ContentFormat;
  pillar: string;
  status: ContentStatus;
  hookType?: string;
  ctaType?: string;
  topics: string[];
  experimentId?: ExperimentId;
  briefPath?: string;
  createdAt: string;
  updatedAt: string;
}

export interface Publication {
  publicationId: PublicationId;
  contentId: ContentId;
  platform: 'instagram';
  platformMediaId: string;
  permalink?: string;
  mediaType?: string;
  durationSeconds?: number;
  publishedAt: string;
}

/** Own-account metrics. Private fields are unavailable for competitors — never merge these types. */
export interface OwnMetrics {
  reach?: number;
  views?: number;
  likes?: number;
  comments?: number;
  saves?: number;
  shares?: number;
  avgWatchSeconds?: number;
  totalWatchSeconds?: number;
  profileVisits?: number;
  follows?: number;
}

export interface MetricSnapshot extends OwnMetrics {
  publicationId: PublicationId;
  ageBucket: AgeBucket;
  capturedAt: string;
  schemaVersion: string;
  raw: unknown;
}

/** Competitor data is structurally distinct on purpose: the type system prevents invalid comparison. */
export interface CompetitorPost {
  accountId: string;
  mediaId: string;
  mediaType?: string;
  caption?: string;
  permalink?: string;
  postedAt: string;
  likeCount: number;
  commentsCount: number;
  followersAtCapture: number;
  capturedAt: string;
}

export type Verdict = 'pending' | 'supported' | 'refuted' | 'inconclusive';

export interface Experiment {
  experimentId: ExperimentId;
  hypothesis: string;
  /** Exactly one. Two manipulated variables produce no learning. */
  variable: string;
  controlDef: string;
  successMetric: keyof OwnMetrics | 'saveRate' | 'shareRate' | 'holdRate' | 'followerConversion';
  minSample: number;
  startedAt: string;
  closedAt?: string;
  verdict: Verdict;
  verdictNote?: string;
}

export const MIN_SAMPLE_FOR_CLAIM = 3;
