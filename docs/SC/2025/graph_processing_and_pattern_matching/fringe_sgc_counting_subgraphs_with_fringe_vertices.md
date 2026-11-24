---
title: "Fringe-SGC: Counting Subgraphs with Fringe Vertices"
description: "SC 2025 · Graph Processing and Pattern Matching · Cameron Bradley; Ghadeer Ahmed H Alabandi; Martin Burtscher"
tags:
  - "SC2025"
  - "Graph Processing and Pattern Matching"
---

# Fringe-SGC: Counting Subgraphs with Fringe Vertices

**中文标题：** 含边缘顶点的子图计数

**所属 Session：** [Graph Processing and Pattern Matching](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Graph Processing and Pattern Matching。</p>
<p class="paper-seo-summary__tags">SC 2025 · Graph Processing and Pattern Matching</p>
</div>

**作者**：Cameron Bradley; Ghadeer Ahmed H Alabandi; Martin Burtscher

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap521&sess=sess180)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Subgraph counting (SGC) is a fundamental component of many important applications, including cybersecurity, drug discovery, social network analysis, and natural language processing. However, current SGC approaches can only handle very small patterns (aka subgraphs) because the computational load increases exponentially with the size of the pattern. To overcome this limitation for certain patterns, we introduce a new technique and algorithm called Fringe-SGC for counting the exact number of times a subgraph occurs in a larger graph. Our approach conventionally searches only for the “core” of the subgraph and then uses set-based methods to compute the number of occurrences that the “fringes” add. Our evaluation shows that Fringe-SGC is able to count the instances of many subgraphs that are too large for state-of-the-art SGC frameworks. Furthermore, Fringe-SGC running on a GPU outperforms the state-of-the-art GPU-based SGC frameworks by up to 20× on average, especially on patterns with ma

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
