---
title: "BatchZK: A Fully Pipelined GPU-Accelerated System for Batch Generation of Zero-Knowledge Proofs"
description: "ASPLOS 2025 · Trust"
tags:
  - "ASPLOS2025"
  - "Trust"
---

# BatchZK: A Fully Pipelined GPU-Accelerated System for Batch Generation of Zero-Knowledge Proofs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 ASPLOS 2025，所属 Track: Trust。</p>
<p class="paper-seo-summary__tags">ASPLOS 2025 · Trust</p>
</div>

**论文链接**：[https://doi.org/10.1145/3669940.3707270](https://doi.org/10.1145/3669940.3707270)
**作者**：Tao Lu (Zhejiang University,National University of Singapore), Yuxun Chen (Zhejiang University), Zonghui Wang (Zhejiang University), Xiaohang Wang (Zhejiang University), Wenzhi Chen (Zhejiang University), Jiaheng Zhang (National University of Singapore)
**会议**：ASPLOS 2025

---

## 一句话总结

> 该工作面向 Trust 场景，围绕 A Fully Pipelined GPU-Accelerated System for Batch Generation of Zero-Knowledge Proofs 提出系统化优化方案，重点涉及 BatchZK、Fully、Pipelined 等关键技术点。

## 方法简述

- 以 BatchZK 为核心切入点，构建针对 Trust 工作负载的优化路径。
- 从算法、编译或体系结构层面进行联合设计，减少关键瓶颈。
- 在 GPU 执行与调度路径上引入针对性优化。

## 主要结果

- 提升并行执行效率与资源利用率。
- 目标是降低时延并提升吞吐/可扩展性。
- 方法具备与现有软硬件栈集成的潜力，适用于后续扩展验证。
