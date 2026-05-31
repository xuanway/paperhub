---
title: "GraphPipe: Improving Performance and Scalability of DNN Training with Graph Pipeline Parallelism"
description: "ASPLOS 2025 · ML Training"
tags:
  - "ASPLOS2025"
  - "ML Training"
---

# GraphPipe: Improving Performance and Scalability of DNN Training with Graph Pipeline Parallelism

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 ASPLOS 2025，所属 Track: ML Training。</p>
<p class="paper-seo-summary__tags">ASPLOS 2025 · ML Training</p>
</div>

**论文链接**：[https://doi.org/10.1145/3669940.3707220](https://doi.org/10.1145/3669940.3707220)
**作者**：Byungsoo Jeon (NVIDIA), Mengdi Wu (Carnegie Mellon Univerisity), Shiyi Cao (UC Berkeley), Sunghyun Kim (Massachusetts Institute of Technology), Sunghyun Park (NVIDIA), Neeraj Aggarwal (Carnegie Mellon University), Colin Unger (Stanford University), Daiyaan Arfeen (Carnegie Mellon University), Peiyuan Liao (Carnegie Mellon University), Xupeng Miao (Carnegie Mellon University), Mohammad Alizadeh (Massachusetts Institute of Technology), Gregory R. Ganger (Carnegie Mellon University), Tianqi Chen (Carnegie Mellon University), Zhihao Jia (Carnegie Mellon University)
**会议**：ASPLOS 2025

---

## 一句话总结

> 该工作面向 ML Training 场景，围绕 Improving Performance and Scalability of DNN Training with Graph Pipeline Parallelism 提出系统化优化方案，重点涉及 GraphPipe、Improving、Performance 等关键技术点。

## 方法简述

- 以 GraphPipe 为核心切入点，构建针对 ML Training 工作负载的优化路径。
- 从算法、编译或体系结构层面进行联合设计，减少关键瓶颈。
- 通过模块化设计保持方案可迁移性与工程可落地性。

## 主要结果

- 在性能、能效或可扩展性指标上预期优于基线方案。
- 在真实系统落地时兼顾实现复杂度与工程可维护性。
- 方法具备与现有软硬件栈集成的潜力，适用于后续扩展验证。
