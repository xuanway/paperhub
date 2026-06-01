---
title: "Fringe-SGC: Counting Subgraphs with Fringe Vertices"
description: "SC 2025 · Graph Processing and Pattern Matching · Cameron Bradley; Ghadeer Ahmed H Alabandi; Martin Burtscher"
tags:
  - "SC2025"
  - "Graph Processing and Pattern Matching"
---

# Fringe-SGC: Counting Subgraphs with Fringe Vertices

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Graph Processing and Pattern Matching。</p>
<p class="paper-seo-summary__tags">SC 2025 · Graph Processing and Pattern Matching</p>
</div>

**作者**：Cameron Bradley; Ghadeer Ahmed H Alabandi; Martin Burtscher

**会议**：SC 2025 · St. Louis, MO

## 摘要

Subgraph counting (SGC) is a fundamental component of many important applications, including cybersecurity, drug discovery, social network analysis, and natural language processing. However, current SGC approaches can only handle very small patterns (aka subgraphs) because the computational load increases exponentially with the size of the pattern. To overcome this limitation for certain patterns, we introduce a new technique and algorithm called Fringe-SGC for counting the exact number of times a subgraph occurs in a larger graph. Our approach conventionally searches only for the “core” of the subgraph and then uses set-based methods to compute the number of occurrences that the “fringes” add. Our evaluation shows that Fringe-SGC is able to count the instances of many subgraphs that are too large for state-of-the-art SGC frameworks. Furthermore, Fringe-SGC running on a GPU outperforms the state-of-the-art GPU-based SGC frameworks by up to 20× on average, especially on patterns with ma

---

## 一句话总结

> 该工作属于 Graph Processing and Pattern Matching 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Graph Processing and Pattern Matching 领域贡献新的设计范式或评估框架。
