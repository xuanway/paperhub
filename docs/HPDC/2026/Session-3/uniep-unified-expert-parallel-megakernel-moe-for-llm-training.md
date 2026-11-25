---
title: "UniEP: Unified Expert-Parallel MegaKernel MoE for LLM Training"
description: "HPDC 2026 · Session 3 — MoE Systems & Distributed LLM Training"
tags:
  - "HPDC2026"
  - "Session 3"
  - "MoE Systems & Distributed LLM Training"
---

# UniEP: Unified Expert-Parallel MegaKernel MoE for LLM Training

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 3 — MoE Systems & Distributed LLM Training（2026年7月14日 13:30–14:30 · Session Chair：Peter Dinda）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 3</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807818)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#ZhengZCZ26](https://dblp.org/db/conf/hpdc/hpdc2026.html#ZhengZCZ26)

**作者**：Size Zheng, Xuegui Zheng, Li-Wen Chang, Jidong Zhai

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 3 — MoE Systems & Distributed LLM Training（2026年7月14日 13:30–14:30 · Session Chair：Peter Dinda）

---

## 英文摘要

As LLM training grows increasingly resource-intensive and expert parallelism (EP) becomes essential for scaling MoE models, EP optimizations are widely adopted in production frameworks like Megatron-LM. Existing solutions often rely on ad-hoc, complex kernels that lack adaptability across diverse optimization configurations and frequently neglect numerical stability, failing to meet the strict precision requirements of large-scale training. In this paper, we introduce UniEP, a novel system that unifies diverse EP optimization strategies into a cohesive abstraction. UniEP fuses the MoE communication and computation into MegaKernels, effectively transforming complex architectural tuning into a unified parameter search space for automated adaptability. Crucially, UniEP incorporates a deterministic token ordering mechanism that guarantees numerical consistency with sequential execution, even under aggressive overlap schedules. We evaluate UniEP on GPU clusters equipped with NVIDIA Hopper GPUs. Our results demonstrate that UniEP achieves 1.03×-1.38× speedups over state-of-the-art work, effectively mitigating communication bottlenecks while maintaining the rigorous accuracy standards required for production LLM training.

## 中文摘要

随着 LLM 训练的资源消耗日益增长，专家并行（EP）成为扩展 MoE 模型的关键，EP 优化被 Megatron-LM 等生产框架广泛采用。现有方案往往依赖特定的、复杂的核，缺乏跨多样优化配置的适应性，并且常常忽视数值稳定性，无法满足大规模训练的严格精度要求。本文提出 UniEP，一个将多样 EP 优化策略统一为内聚抽象的新系统。UniEP 将 MoE 通信与计算融合为 MegaKernel，有效地将复杂的架构调优转变为统一的参数搜索空间，实现自动化适配。关键的是，UniEP 引入了确定性的令牌排序机制，即使在激进的重叠调度下也能保证与顺序执行一致的数值一致性。我们在配备 NVIDIA Hopper GPU 的集群上评估 UniEP。结果表明，UniEP 相比最先进工作取得 1.03–1.38 倍加速，在保持生产级 LLM 训练所需严格精度标准的同时，有效缓解通信瓶颈。

---

[← 返回 Session 3 — MoE Systems & Distributed LLM Training](index.md)
