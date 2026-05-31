---
title: "Relax: Composable Abstractions for End-to-End Dynamic Machine Learning"
description: "ASPLOS 2025 · ML Compilers"
tags:
  - "ASPLOS2025"
  - "ML Compilers"
---

# Relax: Composable Abstractions for End-to-End Dynamic Machine Learning

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 ASPLOS 2025，所属 Track: ML Compilers。</p>
<p class="paper-seo-summary__tags">ASPLOS 2025 · ML Compilers</p>
</div>

**论文链接**：[https://doi.org/10.1145/3676641.3716249](https://doi.org/10.1145/3676641.3716249)
**作者**：Ruihang Lai (Carnegie Mellon University), Junru Shao (OpenAI), Siyuan Feng (Shanghai Jiao Tong University), Steven Lyubomirsky (NVIDIA), Bohan Hou (Carnegie Mellon University), Wuwei Lin (OpenAI), Zihao Ye (University of Washington), Hongyi Jin (Carnegie Mellon University), Yuchen Jin (Hyperbolic), Jiawei Liu (University of Illinois Urbana-Champaign), Lesheng Jin (Hyperbolic), Yaxing Cai (NVIDIA), Ziheng Jiang (ByteDance), Yong Wu (NVIDIA), Sunghyun Park (NVIDIA), Prakalp Srivastava (Netflix), Jared Roesch (NVIDIA), Todd C. Mowry (Carnegie Mellon University), Tianqi Chen (Carnegie Mellon University,NVIDIA)
**会议**：ASPLOS 2025

---

## 一句话总结

> 该工作面向 ML Compilers 场景，围绕 Composable Abstractions for End-to-End Dynamic Machine Learning 提出系统化优化方案，重点涉及 Relax、Composable、Abstractions 等关键技术点。

## 方法简述

- 以 Relax 为核心切入点，构建针对 ML Compilers 工作负载的优化路径。
- 从算法、编译或体系结构层面进行联合设计，减少关键瓶颈。
- 通过模块化设计保持方案可迁移性与工程可落地性。

## 主要结果

- 在性能、能效或可扩展性指标上预期优于基线方案。
- 在真实系统落地时兼顾实现复杂度与工程可维护性。
- 方法具备与现有软硬件栈集成的潜力，适用于后续扩展验证。
