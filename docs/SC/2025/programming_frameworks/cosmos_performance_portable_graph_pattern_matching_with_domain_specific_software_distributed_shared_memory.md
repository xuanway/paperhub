---
title: "COSMOS: Performance Portable Graph Pattern Matching with Domain-Specific Software Distributed Shared Memory"
description: "SC 2025 · Programming Frameworks · Zhiheng Lin; Ke Meng; Changjie Xu; Weichen Cao; Guangming Tan"
tags:
  - "SC2025"
  - "Programming Frameworks"
---

# COSMOS: Performance Portable Graph Pattern Matching with Domain-Specific Software Distributed Shared Memory

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Programming Frameworks。</p>
<p class="paper-seo-summary__tags">SC 2025 · Programming Frameworks</p>
</div>

**作者**：Zhiheng Lin; Ke Meng; Changjie Xu; Weichen Cao; Guangming Tan

**会议**：SC 2025 · St. Louis, MO

## 摘要

Graph pattern matching (GPM) is essential in fields like circuit logic synthesis, anomaly detection, social network analysis, cheminformatics, recommendation systems, and classification systems. Its NP-completeness and the irregular nature of graph data make scaling to distributed systems challenging. By utilizing architecture-specific communication techniques and topology-aware data partitioning, the scalability of GPM on large-scale data can be improved. However, the lack of performance portability complicates the parallel evolution of GPM software with hardware architectures, burdening developers. This paper proposes a vertex-addressing scheme based on a distributed shared memory model (DSM) that relaxes strict DSM constraints, achieving both performance portability and scalability. This approach enables seamless code extension to thousands of nodes across different supercomputing architectures while maintaining performance comparable to manually optimized versions.

---

## 一句话总结

> 该工作属于 Programming Frameworks 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Programming Frameworks 领域贡献新的设计范式或评估框架。
