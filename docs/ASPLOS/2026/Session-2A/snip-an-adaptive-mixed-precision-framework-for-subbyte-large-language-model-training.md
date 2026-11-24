---
title: "SNIP: An Adaptive Mixed Precision Framework for Subbyte Large Language Model Training"
description: "ASPLOS 2026 · Session 2A · SNIP：面向亚字节大语言模型训练的自适应混合精度框架"
tags:
  - "ASPLOS2026"
  - "Session 2A"
  - "LLM Training Systems"
---

# SNIP: An Adaptive Mixed Precision Framework for Subbyte Large Language Model Training

**中文标题：** SNIP：面向亚字节大语言模型训练的自适应混合精度框架

**所属 Session：** [Session 2A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Yunjie Pan (University of Michigan), Jiecao Yu (Meta Platforms, Inc.), Yongyi Yang (University of Michigan, Ann Arbor), Hanmei Yang (University of Massachusetts Amherst), Zhaoxia (Summer) Deng (Meta), Scott Mahlke (University of Michigan)

**单位：** University of Michigan；Meta Platforms, Inc.；University of Michigan, Ann Arbor；University of Massachusetts Amherst；Meta

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790223) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Training large language models (LLMs) efficiently while preserving model quality poses significant challenges, particularly with subbyte precision supported by state-of-the-art GPUs. Current mixed-precision training approaches either apply uniform precision to all GEMM operations or rely on heuristic-based methods that fail to generalize during training, leading to suboptimal convergence and instability. To address these challenges, this paper introduces SNIP, a fine-grained adaptive mixed-precision training framework for LLM pretraining that supports subbyte precision. SNIP periodically collects statistics on activations, gradients, and optimizer states to assess the precision loss impact on model quality. We define two key metrics: loss divergence in the forward pass, caused by quantization-induced increases in training loss, and weight divergence in the backward pass, which measures error propagation through gradients affecting model updates. These metrics guide an Integer Linear Programming (ILP) problem that systematically optimizes layerwise precision to minimize overall quality loss while meeting efficiency targets. Experiments on 1B, 3B, 7B and 70B Llama-like models demonstrate that SNIP consistently outperforms existing baselines, reducing FLOPs by up to 80% while preserving model quality across different model sizes and training phases with minimal computational overhead.

## 中文摘要

在保持模型质量的同时高效训练大语言模型（LLM）面临重大挑战，尤其是在当前最先进 GPU 所支持的亚字节精度下。现有的混合精度训练方法要么对所有 GEMM 运算施加统一精度，要么依赖基于启发式的方法，后者在训练过程中难以泛化，导致收敛次优和训练不稳定。为应对这些挑战，本文提出 SNIP，一个面向 LLM 预训练的细粒度自适应混合精度训练框架，支持亚字节精度。SNIP 周期性地收集关于激活、梯度和优化器状态的统计信息，以评估精度损失对模型质量的影响。我们定义了两个关键指标：前向传播中的损失发散，由量化引起的训练损失上升所导致；以及反向传播中的权重发散，它衡量通过梯度传播并影响模型更新的误差。这些指标指导一个整数线性规划（ILP）问题，系统性地优化逐层精度，以在满足效率目标的同时最小化整体质量损失。在 1B、3B、7B 和 70B 的 Llama 类模型上的实验表明，SNIP 持续优于现有基线，在不同模型规模和训练阶段下将 FLOPs 降低多达 80% 的同时保持模型质量，且计算开销极小。

## 英文关键词

Mixed-precision training, Quantization, Large language models, Neural network

## 中文关键词

混合精度训练；量化；大语言模型；神经网络

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790223)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 2A](index.md) · [返回 ASPLOS 2026](../index.md)
