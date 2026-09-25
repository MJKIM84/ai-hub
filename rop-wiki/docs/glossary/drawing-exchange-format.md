---
title: "도면 교환 형식 (Drawing Exchange Format (DXF))"
type: glossary
term_ko: 도면 교환 형식
term_en: Drawing Exchange Format (DXF)
definition: 레이어·블록·엔터티로 CAD 도면을 담는 교환 파일 형식으로, ezdxf 문서 기준 좌표·길이 값에 단위가 붙지 않고 모델 공간 단위는 선택 헤더 변수($INSUNITS)로 준다.
related_areas: [6, 28]
tags: []
status: published
confidence: medium
created: 2026-09-25
updated: 2026-09-25
sources: [ref-424, ref-425, ref-426]
version: 1
---

[홈](../index.md) › [용어집](index.md) › 도면 교환 형식

# 도면 교환 형식 (Drawing Exchange Format (DXF))

## 용어

| 한글 | 영문 | 약어와 풀어 쓴 이름 |
|---|---|---|
| 도면 교환 형식 | Drawing Exchange Format (DXF) | DXF — Drawing Exchange Format |

## 한 줄 정의

레이어·블록·엔터티로 CAD 도면을 담는 교환 파일 형식으로, ezdxf 문서 기준 좌표·길이 값에 단위가 붙지 않고 모델 공간 단위는 선택 헤더 변수($INSUNITS)로 준다. [추정][^ref-424][^ref-425][^ref-426]

## 설명

레이어는 객체를 논리적 묶음으로 나누는 수단이며 레이어 이름의 의미는 형식이 정하지 않아, 벽·문 같은 요소의 의미는 프로젝트의 레이어 명명 관례(ISO 13567, 미국 NCS, KS F 1542 등)에 기댄다. 근거는 Autodesk 공식 참조가 아닌 오픈소스 라이브러리 ezdxf 문서다.

## 관련 영역

- [6. 지도·공간·위치 모델](../categories/b-common-information-and-environment-model/06-map-space-and-location-model.md)
- [28. 표준·상호운용성·다사업자 거버넌스](../categories/g-safety-security-intelligence-and-governance/28-standards-interoperability-and-multi-vendor-governance.md)

## 출처

[^ref-424]: Moitzi, M. (mozman/ezdxf GitHub), ezdxf documentation — Concepts: Blocks (docs/source/concepts/blocks.rst), 미확인, https://github.com/mozman/ezdxf/blob/master/docs/source/concepts/blocks.rst, 접근일 2026-09-25
[^ref-425]: Moitzi, M. (mozman/ezdxf GitHub), ezdxf documentation — Concepts: Layers (docs/source/concepts/layers.rst), 미확인, https://github.com/mozman/ezdxf/blob/master/docs/source/concepts/layers.rst, 접근일 2026-09-25
[^ref-426]: Moitzi, M. (mozman/ezdxf GitHub), ezdxf documentation — Concepts: DXF Units (docs/source/concepts/units.rst), 미확인, https://github.com/mozman/ezdxf/blob/master/docs/source/concepts/units.rst, 접근일 2026-09-25

- 참고문헌 페이지: [ref-424](../references/ref-424.md), [ref-425](../references/ref-425.md), [ref-426](../references/ref-426.md)
