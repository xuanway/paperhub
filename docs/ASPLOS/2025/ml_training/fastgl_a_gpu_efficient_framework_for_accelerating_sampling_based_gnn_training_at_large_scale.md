---
title: "FastGL: A GPU-Efficient Framework for Accelerating Sampling-Based GNN Training at Large Scale"
description: "ASPLOS 2025 · ML Training"
tags:
  - "ASPLOS2025"
  - "ML Training"
---

# FastGL: A GPU-Efficient Framework for Accelerating Sampling-Based GNN Training at Large Scale

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 ASPLOS 2025，所属 Track: ML Training。</p>
<p class="paper-seo-summary__tags">ASPLOS 2025 · ML Training</p>
</div>

**论文链接**：[https://doi.org/10.1145/3622781.3674167](https://doi.org/10.1145/3622781.3674167)
**作者**：Zeyu Zhu (Institute of Automation, Chinese Academy of Sciences,School of Future Technology, University of Chinese Academy of Sciences), Peisong Wang (Institute of Automation, Chinese Academy of Sciences), Qinghao Hu (Institute of Automation, Chinese Academy of Sciences,AiRiA), Gang Li (Shanghai Jiao Tong University), Xiaoyao Liang (Shanghai Jiao Tong University), Jian Cheng (Institute of Automation, Chinese Academy of Sciences,AiRiA)
**会议**：ASPLOS 2025

---

## 一句话总结

> 该工作面向 ML Training 场景，围绕 A GPU-Efficient Framework for Accelerating Sampling-Based GNN Training at Large Scale 提出系统化优化方案，重点涉及 FastGL、GPU-Efficient、Accelerating 等关键技术点。

## 方法简述

- 以 FastGL 为核心切入点，构建针对 ML Training 工作负载的优化路径。
- 从算法、编译或体系结构层面进行联合设计，减少关键瓶颈。
- 在 GPU 执行与调度路径上引入针对性优化。

## 主要结果

- 提升并行执行效率与资源利用率。
- 目标是降低时延并提升吞吐/可扩展性。
- 方法具备与现有软硬件栈集成的潜力，适用于后续扩展验证。
