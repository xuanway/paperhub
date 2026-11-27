---
title: "TB-STC: Transposable Block-wise N:M Structured Sparse Tensor Core"
description: "HPCA 2025 · Stacking the Layers (Sparsity)"
tags:
  - "HPCA2025"
  - "Stacking the Layers (Sparsity)"
---

# TB-STC: Transposable Block-wise N:M Structured Sparse Tensor Core

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Stacking the Layers (Sparsity)。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Stacking the Layers (Sparsity)</p>
</div>

**论文链接**：
**作者**：Jun Liu (Shanghai Jiao Tong University), Shulin Zeng (Tsinghua University, Infinigence-AI), Junbo Zhao (Tsinghua University), Li Ding (Shanghai Jiao Tong University), Zeyu Wang (Shanghai Jiao Tong University), Jinhao Li (Shanghai Jiao Tong University), Zhenhua Zhu (Tsinghua University), Xuefei Ning (Tsinghua University), Chen Zhang (Shanghai Jiao Tong University), Yu Wang (Tsinghua University), Guohao Dai (Shanghai Jiao Tong University, Infinigence-AI)
**会议**：HPCA 2025

---

## 中文标题

TB-STC：可转置的分块 N:M 结构化稀疏张量核心

## 英文摘要

The computational and memory demands of Deep Learning (DL) models, from convolutional neural networks to Large Language Models (LLMs), are experiencing a notable surge. The sparsification (e.g., weight pruning and sparse attention) represents a significant approach to reducing latency and energy consumption. However, it is non-trivial to identify a good trade-off between model accuracy and hardware efficiency. Existing work has sought to mitigate the hardware complexity overhead through structured sparsity, yet the resulting accuracy loss remains considerable (e.g., more than 6% accuracy drop with 50% structured sparsity on OPT-6.7B and Llama2-7B). To address the above challenges, this paper proposes Transposable Block-wise Structured Sparsity (TBS). Our key insight is that the weight matrices of the forward and backward pass are transposed to each other during DL training. Exploiting this transposition property facilitates obtaining a structured sparsity pattern that is closer to the unstructured sparsity. In contrast, existing studies explore only one-dimensional structured sparsity. In light of these observations, we propose the transposable block-wise structured sparsity pattern with an efficient end-to-end sparse training method. This method improves accuracy by up to 2.58% over other structured sparsity studies under the same sparsity degree. At the micro-architecture level, we propose TB-STC, a Transposable Block-wise N:M Sparse Tensor Core to efficiently and flexibly facilitate the TBS pattern. TB-STC introduces an adaptive codec architecture for on-the-fly storage format conversion with a higher bandwidth utilization (1.47×), and implements an I/O-aware configurable architecture for sparsity-aware scheduling with a better computational utilization (1.57×). Compared with existing work, TB-STC improves the Energy-Delay Product (EDP) by an average of 3.82× and offers an enhanced accuracy-EDP Pareto frontier across various sparse DL models.

## 中文摘要

从卷积神经网络到大型语言模型（LLM），深度学习（DL）模型的计算与内存需求正显著增长。稀疏化（如权重剪枝与稀疏注意力）是降低时延与能耗的重要手段，但很难在模型精度与硬件效率之间取得良好折中。已有工作借助结构化稀疏缓解硬件复杂度开销，但精度损失仍相当可观，例如在 OPT-6.7B 与 Llama2-7B 上采用 50% 结构化稀疏时精度下降超过 6%。为此本文提出可转置分块结构化稀疏（TBS）。我们的洞见是：训练中前向与反向传播的权重矩阵互为转置，利用该转置特性可获得更接近非结构化稀疏的结构化稀疏模式，而现有研究仅探索一维结构化稀疏。我们据此提出 TBS 模式与高效的端到端稀疏训练方法，在相同稀疏度下精度比其他结构化稀疏研究最高提升 2.58%。在微架构层面，我们提出 TB-STC，一种可转置的分块 N:M 稀疏张量核心，以高效灵活地支持 TBS：其自适应编解码架构实现即时存储格式转换，带宽利用率提高 1.47 倍；其 I/O 感知的可配置架构实现稀疏感知调度，计算利用率提高 1.57 倍。与现有工作相比，TB-STC 平均将能量延迟积（EDP）改善 3.82 倍，并在多种稀疏 DL 模型上提供更优的精度-EDP 帕累托前沿。
