---
title: "On-device Semantic Selection Made Low Latency and Memory Efficient with Monolithic Forwarding"
description: "EuroSys 2026 · Edge Computing, IoT & Embedded AI · Jiahao Zhou (Shanghai Jiao Tong University), Chengliang Lin (Shanghai Jiao Tong "
tags:
  - "EuroSys2026"
  - "Edge Computing, IoT & Embedded AI"
---

# On-device Semantic Selection Made Low Latency and Memory Efficient with Monolithic Forwarding

**中文标题：** 借助整体式前向实现低延迟、内存高效的端侧语义选择

**所属 Session：** [Session 12.2: Edge Computing, IoT & Embedded AI](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Edge Computing, IoT & Embedded AI。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Edge Computing, IoT & Embedded AI</p>
</div>

**作者**：Jiahao Zhou (Shanghai Jiao Tong University), Chengliang Lin (Shanghai Jiao Tong University), Dingji Li (Huawei), Mingkai Dong (Shanghai Jiao Tong University), Haibo Chen (Shanghai Jiao Tong University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803572)

## 英文摘要

Semantic top-𝐾selection with cross-encoder rerankers underpins on-device AI services, such as retrieval-augmented generation, agent memory, and personalized recommendation. However, its latency and memory demands dominate end-to-end budgets on edge hardware. Revisiting the objective of top-𝐾selection, we reveal that only relative rankings matter, not exact per-candidate scores. We further observe sequence-level sparsity: relative rankings progressively stabilize in intermediate layers, enabling early pruning prior to completing full inference.

Building on this insight, we propose monolithic forwarding and develop a training-free inference system, PRISM. By maintaining a global view of all candidates, it reduces latency through progressive cluster pruning. It also bounds peak memory usage by strategically overlapping I/O with computation via overlapped layer streaming and chunked execution. We evaluate PRISM against state-of-the-art baselines on rerankers from 0.6 B to 8 B parameters across Apple M2 and RTX 5070. PRISM consistently reduces latency by up to 89.2% and peak memory by up to 91.3% in microbenchmarks, without compromising precision. Across three real-world on-device AI applications, PRISM lowers latency by 11.6%–51.0% and peak memory by 18.6%–77.8%, demonstrating substantial improvements in efficiency and deployability.

## 中文摘要

使用交叉编码器重排器进行语义top-K选择，是端侧AI服务（如检索增强生成、智能体记忆和个性化推荐）的基础。然而，其延迟和内存需求在边缘硬件上占据了端到端预算的主要部分。重新审视top-K选择的目标，我们发现只有相对排序重要，而非每个候选的精确分数。我们进一步观察到序列级稀疏性：相对排序在中间层逐步稳定，使得在完成完整推理之前即可进行提前剪枝。

基于这一洞见，我们提出整体式前向（monolithic forwarding），并开发了一个无需训练的推理系统PRISM。通过维护所有候选的全局视图，它借助渐进式簇剪枝降低延迟。它还通过重叠的层流式加载和分块执行，将I/O与计算策略性地重叠，从而限制峰值内存使用。我们在Apple M2和RTX 5070上，针对参数量从0.6B到8B的重排器，将PRISM与最先进的基线进行比较。在微基准测试中，PRISM在不损失精度的前提下将延迟降低多达89.2%、峰值内存降低多达91.3%。在三个真实的端侧AI应用中，PRISM将延迟降低11.6%–51.0%、峰值内存降低18.6%–77.8%，在效率与可部署性上展现出显著改进。

**英文关键词：** Semantic Selection, Edge Computing, Inference Optimization, Reranking

**中文关键词：** 语义选择、边缘计算、推理优化、重排序

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
