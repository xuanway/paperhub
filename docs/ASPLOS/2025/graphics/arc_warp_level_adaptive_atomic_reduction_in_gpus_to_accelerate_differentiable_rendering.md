---
title: "ARC: Warp-level Adaptive Atomic Reduction in GPUs to Accelerate Differentiable Rendering"
description: "ASPLOS 2025 · Graphics"
tags:
  - "ASPLOS2025"
  - "Graphics"
---

# ARC: Warp-level Adaptive Atomic Reduction in GPUs to Accelerate Differentiable Rendering

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 ASPLOS 2025，所属 Track: Graphics。</p>
<p class="paper-seo-summary__tags">ASPLOS 2025 · Graphics</p>
</div>

**论文链接**：[https://doi.org/10.1145/3669940.3707238](https://doi.org/10.1145/3669940.3707238)
**作者**：Sankeerth Durvasula (Vector Institute, University of Toronto), Adrian Zhao (Vector Institute, University of Toronto), Fan Chen (University of Toronto), Ruofan Liang (Vector Institute, University of Toronto), Pawan Kumar Sanjaya (Vector Institute, University of Toronto), Yushi Guan (Vector Institute, University of Toronto), Christina Giannoula (Vector Institute, University of Toronto), Nandita Vijaykumar (Vector Institute, University of Toronto)
**会议**：ASPLOS 2025

---

## 一句话总结

> 该工作面向 Graphics 场景，围绕 Warp-level Adaptive Atomic Reduction in GPUs to Accelerate Differentiable Rendering 提出系统化优化方案，重点涉及 ARC、Warp-level、Adaptive 等关键技术点。

## 方法简述

- 以 ARC 为核心切入点，构建针对 Graphics 工作负载的优化路径。
- 从算法、编译或体系结构层面进行联合设计，减少关键瓶颈。
- 在 GPU 执行与调度路径上引入针对性优化。

## 主要结果

- 提升并行执行效率与资源利用率。
- 目标是降低时延并提升吞吐/可扩展性。
- 方法具备与现有软硬件栈集成的潜力，适用于后续扩展验证。
