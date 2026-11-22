---
title: "BITE: Boosting LLM Training via Sandwich-Bite Dataflow and Dynamic Subspace Auto-Alignment"
description: "MICRO 2026 · Session 8C · BITE：通过 Sandwich-Bite 数据流与动态子空间自动对齐加速 LLM 训练"
tags:
  - "MICRO2026"
  - "LLM Inference"
  - "LLM Training"
---

# BITE: Boosting LLM Training via Sandwich-Bite Dataflow and Dynamic Subspace Auto-Alignment

**中文标题：** BITE：通过 Sandwich-Bite 数据流与动态子空间自动对齐加速 LLM 训练

**所属 Session：** [Session 8C](index.md) · [MICRO 2026](../index.md)

**作者：** Ruibing Song, Taowen Wang, Guangyan Sun, Chunshu Wu, Qifan Wang, Dongfang Liu, Sushant Kondguli, Yuchen Hao, Ang Li, Tong Geng

**来源：** MICRO 2026，pp. 3037–3052；[DOI](https://doi.org/10.1109/MICRO67795.2026.00205)

## 英文摘要

Large Language Models (LLMs) are transforming Artificial Intelligence (AI), yet their explosive scaling has driven up the computational, energy, and financial costs of training to unsustainable levels. While GPUs dominate LLM training, their general-purpose architecture incurs inherent inefficiencies, particularly in communication and memory handling, and constrains algorithmic optimization, leaving substantial performance potential untapped. Custom accelerators could address these bottlenecks, but existing designs focus on LLM inference or the training of small transformer models, failing to meet the demands of LLM training, whose extreme scale has produced unique and complex challenges. This gap calls for an efficient hardware architecture that both supports state-of-the-art LLM training optimizations and enables new opportunities, guiding the future exploration of custom LLM training hardware. To address this gap, we present BITE, an efficient LLM training accelerator through a tight co-design of algorithm and architecture. BITE introduces a "sandwich-bite" heterogeneous multi-core micro-architecture that optimizes training flow to reduce off-chip communication and memory footprint and a dynamic subspace auto-alignment technique that leverages hardware flexibility to accelerate model convergence. Evaluations across modern LLMs demonstrate that BITE achieves an average of 77% communication reduction, 61% memory footprint reduction, 31% training step reduction, 4.54x speedup, and 7.11x energy savings over GPU-based training, laying a robust foundation for future exploration.

## 中文摘要

大语言模型 (LLM) 正在改变人工智能 (AI)，但其爆炸性扩展已将训练的计算、能源和财务成本推高至不可持续的水平。虽然 GPU 在 LLM 训练中占据主导地位，但其通用架构会导致固有的低效率，特别是在通信和内存管理方面，并限制算法优化，从而导致大量性能潜力未被开发。定制加速器可以解决这些瓶颈，但现有设计侧重于LLM推理或小型Transformer模型的训练，无法满足LLM训练的需求，其极端规模带来了独特而复杂的挑战。这一差距需要高效的硬件架构，既支持最先进的 LLM 训练优化，又能够带来新的机会，从而指导定制 LLM 训练硬件的未来探索。为了解决这一差距，我们推出了 BITE，这是一种通过算法和架构的紧密协同设计实现的高效 LLM 训练加速器。 BITE 引入了“sandwich-bite”异构多核微架构，可优化训练流程以减少片外通信和内存占用，以及动态子空间自动对齐技术，可利用硬件灵活性加速模型收敛。对现代大语言模型的评估表明，与基于 GPU 的训练相比，BITE 平均减少了 77% 的通信，减少了 61% 的内存占用，减少了 31% 的训练步骤，速度达到基线的 4.54 倍，能耗降至基线的 1/7.11，为未来的探索奠定了坚实的基础。

## 中文关键词

大语言模型；训练加速器；算法与硬件协同设计；数据流；动态子空间对齐

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 8C](index.md) · [MICRO 2026 主页](../index.md)
