---
title: "Full-Core Fluid-Structure-Interaction Simulation of Nuclear Reactor on CPU+GPU Hybrid Clusters"
description: "HPDC 2026 · Session 5 — Scientific Applications at Scale"
tags:
  - "HPDC2026"
  - "Session 5"
  - "Scientific Applications at Scale"
---

# Full-Core Fluid-Structure-Interaction Simulation of Nuclear Reactor on CPU+GPU Hybrid Clusters

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 5 — Scientific Applications at Scale（2026年7月15日 10:20–11:20 · Session Chair：Michael Papka）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 5</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807600)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#MiaoWLZCZNBW26](https://dblp.org/db/conf/hpdc/hpdc2026.html#MiaoWLZCZNBW26)

**作者**：Xue Miao, Jue Wang, Qida Lin, Shufei Zhang, Rongqiang Cao, Chunbao Zhou, Ningming Nie, He Bai, Yangang Wang

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 5 — Scientific Applications at Scale（2026年7月15日 10:20–11:20 · Session Chair：Michael Papka）

---

## 英文摘要

Nuclear reactor FSI simulation faces two key challenges: "Mapping wall" bottleneck in data transfer across non-matching mesh coupling interfaces; Low hardware utilization from multi-physics solvers’ heterogeneous core tasks (compute- vs. memory-intensive). Therefore, an innovative FSI framework integrating two strategies is proposed: Scalable radial basis function mapping—restructuring the global problem into massive independent subproblems via task partitioning, preallocation, and multi-granularity load balancing to eliminate communication overhead; Dependency-aware multi-stream optimization—deeply overlapping heterogeneous solver tasks to maximize hardware utilization. It first achieves parameter transfer across ~90,000 non-matching coupling interfaces in China Experimental Fast Reactor, with 86.36% strong scaling and 94.01% weak scaling. The combined optimizations yield ~60% performance gain, increase strong scaling by over 20 percentage points, and achieve high weak scaling of ~97%. Moreover, the FSI results align well with publicly available data, verifying its correctness.

## 中文摘要

核反应堆流固耦合（FSI）模拟面临两个关键挑战：跨非匹配网格耦合界面数据传输中的“映射墙”瓶颈；多物理场求解器异构核心任务（计算密集与内存密集）导致的硬件利用率低。因此，提出一个融合两种策略的创新 FSI 框架：可扩展径向基函数映射——通过任务划分、预分配与多粒度负载均衡，将全局问题重构为大量独立子问题，以消除通信开销；依赖感知的多流优化——深度重叠异构求解器任务，以最大化硬件利用率。它首次在中国实验快堆中实现约 90,000 个非匹配耦合界面的参数传递，强扩展性达 86.36%，弱扩展性达 94.01%。组合优化带来约 60% 的性能提升，将强扩展性提高 20 多个百分点，并实现约 97% 的高弱扩展性。此外，FSI 结果与公开数据吻合良好，验证了其正确性。

## 英文关键词

Advanced computing strategies, Massively parallel algorithms, Fluid-structure interaction simulation

## 中文关键词

先进计算策略，大规模并行算法，流固耦合模拟

---

[← 返回 Session 5 — Scientific Applications at Scale](index.md)
