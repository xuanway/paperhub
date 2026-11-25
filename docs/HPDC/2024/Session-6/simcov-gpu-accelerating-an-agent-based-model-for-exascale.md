---
title: "SIMCoV-GPU: Accelerating an Agent-Based Model for Exascale"
description: "HPDC 2024 · Session 6 — Accelerators & Scientific applications"
tags:
  - "HPDC2024"
  - "Session 6"
  - "Accelerators & Scientific applications"
---

# SIMCoV-GPU: Accelerating an Agent-Based Model for Exascale

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2024 主会 Session 6 — Accelerators & Scientific applications（2024年6月7日 10:00–11:15 · Session Chair：Raffaele Montella）。</p>
<p class="paper-seo-summary__tags">HPDC 2024 · Session 6</p>
</div>

**官方资料**：[HPDC 2024 官方议程](https://hpdc.sci.utah.edu/2024/program.html) · [ACM DOI](https://doi.org/10.1145/3625549.3658692)

**作者**：Kirtus Leyba, Steven Hofmeyr, Stephanie Forrest, Judy Cannon, Melanie Moses

**会议**：HPDC 2024 · Pisa, Italy

**Session**：Session 6 — Accelerators & Scientific applications（2024年6月7日 10:00–11:15 · Session Chair：Raffaele Montella）

---

## 英文摘要

Modern supercomputers rely on graphics processing units (GPUs) to achieve unprecedented computational capabilities. Multi-node computation with GPUs promises to accelerate and scale simulations dramatically across many domains, and many scientific simulations have been adapted to this new paradigm of supercomputing. However, agent-based models (ABMs) are a class of simulations that to date have seen little development for multinode, multi-GPU supercomputers because their computation flow poses unique algorithmic and communication challenges for effective performance on GPU enabled supercomputers. In particular, many ABMs have irregular and dynamic communication patterns, resource competition that causes race conditions, and unpredictable effects on load balancing. We studied the Spatial Immune Model of Coronavirus, or SIMCoV, as a target ABM application for acceleration. SIMCoV is a large-scale ABM which simulates the spread of viral infection through the epithelial tissue of the lungs and models the immune response with diffusing inflammatory signals and mobile T cell agents. Our multinode, multi-GPU implementation of SIMCoV achieves significant speedups over a competitive baseline version, up to 11.9x with a ratio of 32 CPU cores to a single GPU. The paper describes SIMCoV’s GPU-specific optimizations, reports empirical results, and demonstrates effective solutions to the challenges of accelerating ABMs on modern supercomputers.

## 中文摘要

现代超级计算机依赖图形处理器（GPU）实现前所未有的计算能力。多节点 GPU 计算有望在众多领域大幅加速并扩展模拟规模，许多科学模拟已适配这一超级计算新范式。然而，基于智能体的模型（ABM）是一类迄今在多节点、多 GPU 超级计算机上发展较少的模拟，因为其计算流程在 GPU 超级计算机上高效运行面临独特的算法与通信挑战。特别是，许多 ABM 具有不规则且动态的通信模式、引发竞态条件的资源竞争，以及对负载均衡的不可预测影响。我们研究了新冠病毒空间免疫模型（SIMCoV），作为加速的目标 ABM 应用。SIMCoV 是一个大规模 ABM，模拟病毒感染通过肺部上皮组织的传播，并用扩散的炎症信号与移动 T 细胞智能体对免疫响应建模。我们的多节点、多 GPU 实现相比有竞争力的基线版本取得显著加速，在 32 个 CPU 核心对单块 GPU 的配比下最高达 11.9 倍。本文描述了 SIMCoV 针对 GPU 的优化，报告了实证结果，并展示了在现代超级计算机上加速 ABM 所面临挑战的有效解决方案。

---

[← 返回 Session 6 — Accelerators & Scientific applications](index.md)
