---
title: "모델 컨텍스트 프로토콜 (Model Context Protocol (MCP))"
type: glossary
term_ko: 모델 컨텍스트 프로토콜
term_en: Model Context Protocol (MCP)
definition: LLM 이 외부 시스템의 상태를 조회하고 정해진 도구로 동작을 수행하도록 도구·자원을 구조화해 노출하는 개방형 연결 규약이다.
related_areas: [31, 47, 51]
tags: []
status: published
confidence: low
created: 2026-09-25
updated: 2026-09-25
sources: [ref-712]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 모델 컨텍스트 프로토콜

# 모델 컨텍스트 프로토콜 (Model Context Protocol (MCP))

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 모델 컨텍스트 프로토콜 | Model Context Protocol (MCP) | MCP — Model Context Protocol |

## 한 줄 정의

LLM 이 외부 시스템의 상태를 조회하고 정해진 도구로 동작을 수행하도록 도구·자원을 구조화해 노출하는 개방형 연결 규약이다. [추정][^ref-712]

## 설명

로봇 분야에서는 ROS-MCP-Server 처럼 ROS·ROS 2 의 토픽·서비스·액션을 LLM 도구로 노출하는 구현이 있으며, 노출한 도구 목록이 LLM 이 닿는 범위를 정한다.

## 관련 영역

- [47. AI·학습·적응과 모델 운영](../categories/ai-and-learning/ai-learning-adaptation-and-model-operations.md)
- [51. 인증·권한·격리](../categories/security-and-privacy/authentication-authorization-and-isolation.md)
- [31. 사람–로봇 협업](../categories/execution-collaboration-and-recovery/human-robot-collaboration.md)

## 출처

[^ref-712]: robotmcp (ROS-MCP-Server 공식 저장소), ros-mcp-server — Connect AI models like Claude & GPT with robots using MCP and ROS (GitHub README), 미확인, https://github.com/robotmcp/ros-mcp-server, 접근일 2026-09-25

- 참고문헌 페이지: [ref-712](../references/ref-712.md)
