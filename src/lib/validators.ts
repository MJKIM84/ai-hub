import { z } from 'zod';

export const serviceCreateSchema = z.object({
  url: z.string().url('올바른 URL을 입력해주세요'),
  name: z.string().min(1, '서비스 이름을 입력해주세요').max(100),
  description: z.string().max(500).optional(),
  tagline: z.string().max(200).optional(),
  category: z.string().min(1),
  tags: z.array(z.string()).optional().default([]),
  pricingModel: z.enum(['free', 'freemium', 'paid']).default('free'),
  logoUrl: z.string().url().optional().or(z.literal('')),
  faviconUrl: z.string().url().optional().or(z.literal('')),
  ogImageUrl: z.string().url().optional().or(z.literal('')),
  isKorean: z.boolean().optional().default(false),
  source: z.enum(['user', 'auto', 'developer']).optional().default('user'),
});

export const editRequestSchema = z.object({
  serviceId: z.string().min(1),
  requestType: z.enum(['claim', 'edit']),
  contactEmail: z.string().email('올바른 이메일을 입력해주세요'),
  changes: z.record(z.string(), z.unknown()).optional().default({}),
  reason: z.string().max(500).optional(),
});

export const scrapeRequestSchema = z.object({
  url: z.string().url('올바른 URL을 입력해주세요'),
});

export const voteRequestSchema = z.object({
  serviceId: z.string().min(1),
  type: z.enum(['upvote', 'downvote', 'click']),
});

export const commentCreateSchema = z.object({
  serviceId: z.string().min(1),
  content: z.string().min(1, '댓글을 입력해주세요').max(1000),
  authorName: z.string().min(1, '닉네임을 입력해주세요').max(50),
  password: z.string().min(1, '비밀번호를 입력해주세요').max(100),
  parentId: z.string().optional(),
});

export const commentUpdateSchema = z.object({
  commentId: z.string().min(1),
  content: z.string().min(1, '댓글을 입력해주세요').max(1000),
  password: z.string().min(1, '비밀번호를 입력해주세요'),
});

export const commentDeleteSchema = z.object({
  commentId: z.string().min(1),
  password: z.string().min(1, '비밀번호를 입력해주세요'),
});

export const commentVoteSchema = z.object({
  commentId: z.string().min(1),
  type: z.enum(['like', 'dislike']),
});

export const serviceQuerySchema = z.object({
  q: z.string().optional(),
  category: z.string().optional(),
  pricing: z.string().optional(),
  korean: z.coerce.boolean().optional(),
  sort: z.enum(['gravity', 'newest', 'popular', 'name']).optional().default('gravity'),
  page: z.coerce.number().int().positive().optional().default(1),
  limit: z.coerce.number().int().min(1).max(50).optional().default(12),
});
