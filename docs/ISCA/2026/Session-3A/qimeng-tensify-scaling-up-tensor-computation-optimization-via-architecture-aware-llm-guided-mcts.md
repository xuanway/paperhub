---
title: "QiMeng-Tensify: Scaling up Tensor Computation Optimization via Architecture-Aware LLM-Guided MCTS"
description: "ISCA 2026 · Session 3A · QiMeng-Tensify: Scaling up Tensor Computation Optimization via Architecture-Aware LLM-Guided MCTS"
tags:
  - "ISCA2026"
  - "Session 3A"
  - "ML Accelerators 1"
---

# QiMeng-Tensify: Scaling up Tensor Computation Optimization via Architecture-Aware LLM-Guided MCTS

**中文标题：** QiMeng-Tensify: 通过架构感知 LLM 引导的 MCTS 扩展张量计算优化

**所属 Session：** [Session 3A](index.md) · [ISCA 2026](../index.md)

**作者：** Shouyang Dong, Jun Bi, Yuanbo Wen, Xiyue Yu, Jianxing Xu, Guanglin Xu, Ling Li, Xuehai Zhou, Tianshi Chen, Qi Guo

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

The growing scale and complexity of large language models (LLMs) have intensified the need for optimizing large-scale tensor computations (e.g., self-attention and mixture-of-experts) on hardware platforms. Existing solutions rely on either manual expert optimization or exploration-based auto-tuning methods. However, neither approach scales effectively for LLMs with hundreds, even thousands of operators and dynamic control flows, because of prohibitive optimization overheads or suboptimal performance. To address this problem, we present QiMeng-Tensify, the first framework that combines LLMs with sequential decision optimization for large-scale graph-level tensor computation. Our key insight is that: (1) tensor computation optimization can be formulated as a generalized sequential decision problem to enlarge the optimization space, and (2) LLMs inherently encode rich optimization knowledge and can reason about architectural characteristics, which can effectively guide this decision process. Concretely, we first model tensor computation optimization as a Markov Decision Process (MDP), enabling unconstrained graph transformations over pre-defined scheduling rules. To efficiently explore the vast transformation space, we introduce an architecture-aware LLM-guided Monte Carlo Tree Search (MCTS). The LLM shapes the prior probability distribution over candidate transformations, guiding the search direction toward promising program sketches and parameter configurations. To adapt to concrete hardware and workloads, we propose an architecture-aware prior adaptation mechanism that distills natural-language heuristics from a lightweight offline stage. We conducted comprehensive experiments for representative subgraphs and LLMs on NVIDIA A100 and H100. Regarding subgraphs, QiMeng-Tensify averagely outperforms PyTorch, TensorRT, TVM, Triton, FlashAttention, Welder, Mirage, and Reasoning Compiler by 6.49×, 2.86×, 1.68×, 2.64×, 1.27×, 13.49×, 1.29×, and 1.31×, respectively. For LLM workloads, QiMeng-Tensify achieves average speedups of 1.56×, 1.22× and 1.30× over PyTorch, TensorRT-LLM and Mirage on the A100, and 1.78×, 1.29× and 1.30× on the H100, respectively. Results well demonstrate that QiMeng-Tensify provides a generalizable paradigm for optimizing large-scale tensor computation.

## 中文摘要

大语言模型（LLM）不断增长的规模和复杂性加剧了在硬件平台上优化大规模张量计算（如自注意力和混合专家）的需求。现有解决方案依赖于人工专家优化或基于探索的自动调优方法。然而，对于具有成百上千个算子以及动态控制流的LLM来说，由于优化开销过高或性能次优，这两种方法都无法有效扩展。为解决此问题，我们提出QiMeng-Tensify，这是首个将LLM与序列决策优化相结合用于大规模图级张量计算的框架。我们的关键洞察是：(1) 张量计算优化可以被建模为一个广义的序列决策问题以扩大优化空间；(2) LLM天然编码了丰富的优化知识并能推理架构特征，可有效指导这一决策过程。具体地，我们首先将张量计算优化建模为马尔可夫决策过程（MDP），允许在预定义的调度规则上进行无约束的图变换。为高效地探索庞大的变换空间，我们引入了架构感知的LLM引导的蒙特卡洛树搜索（MCTS）。LLM塑造候选变换上的先验概率分布，将搜索方向引导向有前景的程序框架和参数配置。为适应具体的硬件和工作负载，我们提出了一种架构感知的先验自适应机制，从轻量离线阶段提取自然语言启发式信息。我们在NVIDIA A100和H100上对代表性子图和LLM进行了全面实验。在子图方面，QiMeng-Tensify相对于PyTorch、TensorRT、TVM、Triton、FlashAttention、Welder、Mirage和Reasoning Compiler分别实现了平均6.49×、2.86×、1.68×、2.64×、1.27×、13.49×、1.29×和1.31×的性能提升。对于LLM工作负载，QiMeng-Tensify在A100上相比PyTorch、TensorRT-LLM和Mirage实现了平均1.56×、1.22×和1.30×的加速，在H100上则分别为1.78×、1.29×和1.30×。结果充分表明QiMeng-Tensify为优化大规模张量计算提供了可推广的范式。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 3A](index.md) · [返回 ISCA 2026](../index.md)
