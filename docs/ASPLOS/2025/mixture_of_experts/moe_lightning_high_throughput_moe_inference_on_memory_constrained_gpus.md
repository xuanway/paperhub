---
title: "MoE-Lightning: High-Throughput MoE Inference on Memory-constrained GPUs"
description: "ASPLOS 2025 · Mixture of Experts"
tags:
  - "ASPLOS2025"
  - "Mixture of Experts"
---

# MoE-Lightning: High-Throughput MoE Inference on Memory-constrained GPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 ASPLOS 2025，所属 Track: Mixture of Experts。</p>
<p class="paper-seo-summary__tags">ASPLOS 2025 · Mixture of Experts</p>
</div>

**论文链接**：[https://doi.org/10.1145/3669940.3707267](https://doi.org/10.1145/3669940.3707267)
**作者**：Shiyi Cao (UC Berkeley), Shu Liu (UC Berkeley), Tyler Griggs (UC Berkeley), Peter Schafhalter (UC Berkeley), Xiaoxuan Liu (UC Berkeley), Ying Sheng (Stanford University), Joseph E. Gonzalez (UC Berkeley), Matei Zaharia (UC Berkeley), Ion Stoica (UC Berkeley)
**会议**：ASPLOS 2025

---

## 一句话总结

> 该工作面向 Mixture of Experts 场景，围绕 High-Throughput MoE Inference on Memory-constrained GPUs 提出系统化优化方案，重点涉及 MoE-Lightning、High-Throughput、MoE 等关键技术点。

## 方法简述

- 以 MoE-Lightning 为核心切入点，构建针对 Mixture of Experts 工作负载的优化路径。
- 从算法、编译或体系结构层面进行联合设计，减少关键瓶颈。
- 在 GPU 执行与调度路径上引入针对性优化。

## 主要结果

- 提升并行执行效率与资源利用率。
- 降低内存瓶颈并提升系统效率。
- 方法具备与现有软硬件栈集成的潜力，适用于后续扩展验证。
