---
title: "DiTango: Cost-Effective Parallel Diffusion Generation with Selective Attention State Reuse"
description: "HPDC 2026 · Session 12 — Emerging Generative & Agentic AI Workloads"
tags:
  - "HPDC2026"
  - "Session 12"
  - "Emerging Generative & Agentic AI Workloads"
---

# DiTango: Cost-Effective Parallel Diffusion Generation with Selective Attention State Reuse

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 12 — Emerging Generative & Agentic AI Workloads（2026年7月16日 14:40–15:40 · Session Chair：Stefan Andrei）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 12</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807581)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#ChenZZLJZ26](https://dblp.org/db/conf/hpdc/hpdc2026.html#ChenZZLJZ26)

**作者**：Yuyang Chen, Runxin Zhong, Zan Zong, Hengjie Li, Yuyang Jin, Jidong Zhai

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 12 — Emerging Generative & Agentic AI Workloads（2026年7月16日 14:40–15:40 · Session Chair：Stefan Andrei）

---

## 英文摘要

Recent advances in AI-generated content have driven widespread adoption of Diffusion Transformers (DiTs) for high-resolution, long-duration content generation. While parallelization techniques accelerate diffusion inference, they face significant scalability challenges due to excessive communication overhead in multi-node environments. We observe that sequence partitions in Context Parallelism (CP) exhibit distinct heterogeneity: spatially proximate partitions contribute more significantly to attention computation results. By mapping this heterogeneous pattern to hierarchical communication topology, we can access high-contribution partitions with reduced communication cost. This insight motivates our novel selective attention state mechanism that strategically balances partial attention computation and historical result reuse across denoising steps. We present DiTango1, an efficient parallel framework for DiT generation. DiTango features an anchor-guided state selection planner that optimizes computation-reuse decisions for each partition, complemented by a runtime that orchestrates efficient state-centric operations. This design achieves superior system efficiency while preserving generation quality. Experimental evaluation on popular diffusion models demonstrates that DiTango achieves up to 1.9× end-to-end and 3.2× attention speedup with near-linear scaling in multi-node settings, while maintaining generation quality comparable to state-of-the-art approaches.

## 中文摘要

近期 AI 生成内容的进展推动了扩散 Transformer（DiT）在高分辨率、长时长内容生成中的广泛采用。尽管并行化技术加速了扩散推理，但由于多节点环境中的过量通信开销，它们面临显著的可扩展性挑战。我们观察到，上下文并行（CP）中的序列划分呈现明显的异质性：空间上邻近的划分对注意力计算结果的贡献更大。通过将这种异质模式映射到分层通信拓扑，我们能够以更低的通信成本访问高贡献划分。这一洞见促成了我们新颖的选择性注意力状态机制，在去噪步骤间策略性地权衡部分注意力计算与历史结果复用。我们提出 DiTango，一个面向 DiT 生成的高效并行框架。DiTango 具备锚点引导的状态选择规划器，为每个划分优化计算-复用决策，并配有编排高效状态中心操作的运行时。该设计在保持生成质量的同时取得优异的系统效率。在流行扩散模型上的实验评估表明，DiTango 在多节点环境中取得最高 1.9 倍端到端加速和 3.2 倍注意力加速，并具有近线性扩展性，同时保持与最先进方法相当的生成质量。

## 英文关键词

Diffusion, Parallelism, Long Context

## 中文关键词

扩散模型，并行性，长上下文

---

[← 返回 Session 12 — Emerging Generative & Agentic AI Workloads](index.md)
