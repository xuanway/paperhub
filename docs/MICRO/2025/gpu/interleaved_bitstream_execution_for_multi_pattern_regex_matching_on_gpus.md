---
title: "Interleaved Bitstream Execution for Multi-Pattern Regex Matching on GPUs"
description: "MICRO 2025 · GPU"
tags:
  - "MICRO2025"
  - "GPU"
---

# Interleaved Bitstream Execution for Multi-Pattern Regex Matching on GPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 MICRO 2025，所属 Track: GPU。</p>
<p class="paper-seo-summary__tags">MICRO 2025 · GPU</p>
</div>

**论文链接**：
**作者**：Tianao Ge (Hong Kong Univ. of Science and Technology (Guangzhou)); Xiaowen Chu (Data Science and Analytics Thrust, HKUST(GZ)); Hongyuan Liu (Stevens Inst. of Technology)
**会议**：MICRO 2025

---

## 一句话总结

> 该工作面向 GPU 场景，围绕 Interleaved Bitstream Execution for Multi-Pattern Regex Matching on GPUs 提出系统化优化方案，重点涉及 Interleaved、Bitstream、Execution 等关键技术点。

## 方法简述

- 以 Interleaved 为核心切入点，构建针对 GPU 工作负载的优化路径。
- 从算法、编译或体系结构层面进行联合设计，减少关键瓶颈。
- 在 GPU 执行与调度路径上引入针对性优化。

## 主要结果

- 提升并行执行效率与资源利用率。
- 在真实系统落地时兼顾实现复杂度与工程可维护性。
- 方法具备与现有软硬件栈集成的潜力，适用于后续扩展验证。
