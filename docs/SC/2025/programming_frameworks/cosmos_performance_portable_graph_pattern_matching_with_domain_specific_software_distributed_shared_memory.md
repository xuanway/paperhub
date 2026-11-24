---
title: "COSMOS: Performance Portable Graph Pattern Matching with Domain-Specific Software Distributed Shared Memory"
description: "SC 2025 · Programming Frameworks · Zhiheng Lin; Ke Meng; Changjie Xu; Weichen Cao; Guangming Tan"
tags:
  - "SC2025"
  - "Programming Frameworks"
---

# COSMOS: Performance Portable Graph Pattern Matching with Domain-Specific Software Distributed Shared Memory

**中文标题：** 利用领域专用软件分布式共享内存实现性能可移植的图模式匹配

**所属 Session：** [Programming Frameworks](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Programming Frameworks。</p>
<p class="paper-seo-summary__tags">SC 2025 · Programming Frameworks</p>
</div>

**作者**：Zhiheng Lin; Ke Meng; Changjie Xu; Weichen Cao; Guangming Tan

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap659&sess=sess294)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要

Graph pattern matching (GPM) is essential in fields like circuit logic synthesis, anomaly detection, social network analysis, cheminformatics, recommendation systems, and classification systems. Its NP-completeness and the irregular nature of graph data make scaling to distributed systems challenging. By utilizing architecture-specific communication techniques and topology-aware data partitioning, the scalability of GPM on large-scale data can be improved. However, the lack of performance portability complicates the parallel evolution of GPM software with hardware architectures, burdening developers. This paper proposes a vertex-addressing scheme based on a distributed shared memory model (DSM) that relaxes strict DSM constraints, achieving both performance portability and scalability. This approach enables seamless code extension to thousands of nodes across different supercomputing architectures while maintaining performance comparable to manually optimized versions.

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
