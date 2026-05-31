---
title: "Efficient Lossless Compression of Scientific Floating-Point Data on CPUs and GPUs"
description: "ASPLOS 2025 · Potpourri"
tags:
  - "ASPLOS2025"
  - "Potpourri"
---

# Efficient Lossless Compression of Scientific Floating-Point Data on CPUs and GPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 ASPLOS 2025，所属 Track: Potpourri。</p>
<p class="paper-seo-summary__tags">ASPLOS 2025 · Potpourri</p>
</div>

**论文链接**：[https://doi.org/10.1145/3669940.3707280](https://doi.org/10.1145/3669940.3707280)
**作者**：Noushin Azami (Department of Computer Science, Texas State University), Alex Fallin (Department of Computer Science, Texas State University), Martin Burtscher (Department of Computer Science, Texas State University)
**会议**：ASPLOS 2025

---

## 一句话总结

> 该工作面向 Potpourri 场景，围绕 Efficient Lossless Compression of Scientific Floating-Point Data on CPUs and GPUs 提出系统化优化方案，重点涉及 Lossless、Compression、Scientific 等关键技术点。

## 方法简述

- 以 Lossless 为核心切入点，构建针对 Potpourri 工作负载的优化路径。
- 从算法、编译或体系结构层面进行联合设计，减少关键瓶颈。
- 在 GPU 执行与调度路径上引入针对性优化。

## 主要结果

- 提升并行执行效率与资源利用率。
- 目标是降低时延并提升吞吐/可扩展性。
- 方法具备与现有软硬件栈集成的潜力，适用于后续扩展验证。
