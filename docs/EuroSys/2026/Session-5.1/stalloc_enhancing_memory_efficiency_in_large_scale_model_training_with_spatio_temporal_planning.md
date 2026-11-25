---
title: "STAlloc: Enhancing Memory Efficiency in Large-Scale Model Training with Spatio-Temporal Planning"
description: "EuroSys 2026 · AI · Zixiao Huang (Tsinghua University), Junhao Hu (Infinigence-AI), Hao Lin (Tsinghu"
tags:
  - "EuroSys2026"
  - "AI"
---

# STAlloc: Enhancing Memory Efficiency in Large-Scale Model Training with Spatio-Temporal Planning

**中文标题：** STAlloc：基于时空规划提升大规模模型训练的内存效率

**所属 Session：** [Session 5.1: AI](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：AI。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · AI</p>
</div>

**作者**：Zixiao Huang (Tsinghua University), Junhao Hu (Infinigence-AI), Hao Lin (Tsinghua University), Chunyang Zhu (Infinigence-AI), Yueran Tang (Infinigence-AI), Quanlu Zhang (Infinigence-AI), Zhen Guo (Infinigence-AI), Zhenhua Li (Tsinghua University), Shengen Yan (Tsinghua University), Zhenhua Zhu (Tsinghua University), Guohao Dai (Shanghai Jiao Tong University), Yu Wang (Tsinghua University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769335)

## 英文摘要

The rapid scaling of large language models (LLMs) has significantly increased GPU memory pressure, which is further aggravated by training optimization techniques such as virtual pipeline and recomputation that disrupt tensor lifespans and introduce considerable memory fragmentation. Such fragmentation stems from the use of online GPU memory allocators in popular deep learning frameworks like PyTorch, which disregard tensor lifespans. As a result, this inefficiency can waste as much as 43% of memory and trigger out-of-memory errors, undermining the effectiveness of optimization methods.

To address this, we introduce STAlloc, a GPU memory allocator for deep learning frameworks that reduces fragmentation by exploiting the spatial and temporal regularity in memory allocation behaviors of training workloads. STAlloc introduces a novel paradigm that combines offline planning with online allocation. The offline planning leverages spatio-temporal regularities to generate a near-optimal allocation plan, while the online allocation handles complex and dynamic models such as Mixture-of-Experts (MoE). Built as a pluggable PyTorch memory allocator, STAlloc reduces fragmentation ratio on average by 85.1% (up to 100%) across both dense and MoE models, with negligible overhead. This enables more efficient, high-throughput training configurations and improves throughput performance by up to 32.5%.

## 中文摘要

大语言模型（LLM）规模的快速扩张显著加剧了GPU内存压力，而虚拟流水线和重计算等训练优化技术进一步加重了这一问题，它们打乱了张量的生命周期并引入大量内存碎片。这种碎片源于PyTorch等流行深度学习框架中使用在线GPU内存分配器，这些分配器忽略了张量的生命周期。结果，这种低效可能浪费高达43%的内存并触发内存溢出错误，削弱优化方法的效果。

为此，我们提出STAlloc，一种面向深度学习框架的GPU内存分配器，它利用训练负载内存分配行为中的空间与时间规律来减少碎片。STAlloc引入了一种将离线规划与在线分配相结合的新范式。离线规划利用时空规律生成接近最优的分配方案，而在线分配则处理专家混合（MoE）等复杂动态模型。作为可插拔的PyTorch内存分配器，STAlloc在稠密模型和MoE模型上将碎片率平均降低85.1%（最高达100%），且开销可忽略。这使得更高效、高吞吐的训练配置成为可能，并将吞吐性能提升多达32.5%。

**英文关键词：** Memory Defragmentation, Large Language Model, GPU, Distributed Training

**中文关键词：** 内存碎片整理、大语言模型、GPU、分布式训练

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
