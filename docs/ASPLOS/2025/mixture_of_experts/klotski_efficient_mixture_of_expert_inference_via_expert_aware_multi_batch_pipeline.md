---
title: "Klotski: Efficient Mixture-of-Expert Inference via Expert-Aware Multi-Batch Pipeline"
description: "ASPLOS 2025 · Mixture of Experts"
tags:
  - "ASPLOS2025"
  - "Mixture of Experts"
---

# Klotski: Efficient Mixture-of-Expert Inference via Expert-Aware Multi-Batch Pipeline

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 ASPLOS 2025，所属 Track: Mixture of Experts。</p>
<p class="paper-seo-summary__tags">ASPLOS 2025 · Mixture of Experts</p>
</div>

**论文链接**：[https://doi.org/10.1145/3676641.3716261](https://doi.org/10.1145/3676641.3716261)
**作者**：Zhiyuan Fang (Sun Yat-sen University), Yuegui Huang (Sun Yat-sen University), Zicong Hong (Hong Kong University of Science and Technology), Yufeng Lyu (Huawei Technologies Co. Ltd), Wuhui Chen (Sun Yat-sen University,Peng Cheng Laboratory), Yue Yu (Peng Cheng Laboratory), Fan Yu (Huawei Technologies Co. Ltd), Zibin Zheng (Sun Yat-sen University)
**会议**：ASPLOS 2025

---

## 一句话总结

> 该工作面向 Mixture of Experts 场景，围绕 Efficient Mixture-of-Expert Inference via Expert-Aware Multi-Batch Pipeline 提出系统化优化方案，重点涉及 Klotski、Mixture-of-Expert、Inference 等关键技术点。

## 方法简述

- 以 Klotski 为核心切入点，构建针对 Mixture of Experts 工作负载的优化路径。
- 从算法、编译或体系结构层面进行联合设计，减少关键瓶颈。
- 通过模块化设计保持方案可迁移性与工程可落地性。

## 主要结果

- 目标是降低时延并提升吞吐/可扩展性。
- 在真实系统落地时兼顾实现复杂度与工程可维护性。
- 方法具备与现有软硬件栈集成的潜力，适用于后续扩展验证。
