---
title: "Stramash: A Fused-kernel Operating System For Cache-Coherent, Heterogeneous-ISA Platforms"
description: "ASPLOS 2025 · Potpourri"
tags:
  - "ASPLOS2025"
  - "Potpourri"
---

# Stramash: A Fused-kernel Operating System For Cache-Coherent, Heterogeneous-ISA Platforms

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 ASPLOS 2025，所属 Track: Potpourri。</p>
<p class="paper-seo-summary__tags">ASPLOS 2025 · Potpourri</p>
</div>

**论文链接**：[https://doi.org/10.1145/3676641.3716275](https://doi.org/10.1145/3676641.3716275)
**作者**：Tong Xing (The University of Edinburgh), Cong Xiong (Imperial College London), Tianrui Wei (UC Berkeley), April Sanchez (Google), Binoy Ravindran (Virginia Tech), Jonathan Balkind (UC Santa Barbara), Antonio Barbalace (The University of Edinburgh)
**会议**：ASPLOS 2025

---

## 一句话总结

> 该工作面向 Potpourri 场景，围绕 A Fused-kernel Operating System For Cache-Coherent, Heterogeneous-ISA Platforms 提出系统化优化方案，重点涉及 Stramash、Fused-kernel、Operating 等关键技术点。

## 方法简述

- 以 Stramash 为核心切入点，构建针对 Potpourri 工作负载的优化路径。
- 从算法、编译或体系结构层面进行联合设计，减少关键瓶颈。
- 针对缓存层次与数据复用策略进行改进。

## 主要结果

- 降低访存开销并改善性能稳定性。
- 在真实系统落地时兼顾实现复杂度与工程可维护性。
- 方法具备与现有软硬件栈集成的潜力，适用于后续扩展验证。
