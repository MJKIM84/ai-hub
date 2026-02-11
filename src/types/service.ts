export interface Service {
  id: string;
  slug: string;
  url: string;
  name: string;
  description: string | null;
  tagline: string | null;
  logoUrl: string | null;
  faviconUrl: string | null;
  ogImageUrl: string | null;
  category: string;
  tags: string;
  pricingModel: string;
  clicks: number;
  upvotes: number;
  downvotes: number;
  score: number;
  isVerified: boolean;
  isKorean: boolean;
  submittedBy: string | null;
  source: string;
  createdAt: Date;
  updatedAt: Date;
}

export interface ServiceListResponse {
  items: Service[];
  total: number;
  page: number;
  totalPages: number;
  hasMore: boolean;
}

export interface ScrapedData {
  name: string;
  description: string | null;
  ogImageUrl: string | null;
  faviconUrl: string;
  suggestedCategory: string;
  suggestedTags: string[];
}

export interface Comment {
  id: string;
  serviceId: string;
  content: string;
  authorName: string;
  maskedIp: string; // masked IP like "123.45.*.*"
  likes: number;
  dislikes: number;
  parentId: string | null;
  replyToAuthorName?: string; // 답글 대상 닉네임
  replyCount?: number;
  reports: number;
  isHidden: boolean;
  createdAt: string;
}

export interface ServiceCreateInput {
  url: string;
  name: string;
  description?: string;
  tagline?: string;
  category: string;
  tags?: string[];
  pricingModel: string;
  logoUrl?: string;
  faviconUrl?: string;
  ogImageUrl?: string;
  isKorean?: boolean;
}
