---
title: "Instruction-Aware Cooperative TLB and Cache Replacement Policies"
description: "ASPLOS 2025 · Memory Management"
tags:
  - "ASPLOS2025"
  - "Memory Management"
---

# Instruction-Aware Cooperative TLB and Cache Replacement Policies

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 ASPLOS 2025，所属 Track: Memory Management。</p>
<p class="paper-seo-summary__tags">ASPLOS 2025 · Memory Management</p>
</div>

**论文链接**：[https://doi.org/10.1145/3669940.3707247](https://doi.org/10.1145/3669940.3707247)
**作者**：Dimitrios Chasapis (Barcelona Supercomputing Center (BSC)), Georgios Vavouliotis (Unaffiliated), Daniel A. Jiménez (Texas A&M University), Marc Casas (Barcelona Supercomputing Center (BSC),Universitat Politècnica de Catalunya (UPC))
**会议**：ASPLOS 2025

---

## 一句话总结

> 该工作面向 Memory Management 场景，围绕 Instruction-Aware Cooperative TLB and Cache Replacement Policies 提出系统化优化方案，重点涉及 Instruction-Aware、Cooperative、TLB 等关键技术点。

## 方法简述

- 以 Instruction-Aware 为核心切入点，构建针对 Memory Management 工作负载的优化路径。
- 从算法、编译或体系结构层面进行联合设计，减少关键瓶颈。
- 针对缓存层次与数据复用策略进行改进。

## 主要结果

- 降低访存开销并改善性能稳定性。
- 在真实系统落地时兼顾实现复杂度与工程可维护性。
- 方法具备与现有软硬件栈集成的潜力，适用于后续扩展验证。
