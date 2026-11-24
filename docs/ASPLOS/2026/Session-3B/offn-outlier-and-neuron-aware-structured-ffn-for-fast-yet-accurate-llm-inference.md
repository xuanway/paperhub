---
title: "oFFN: Outlier and Neuron-aware Structured FFN for Fast yet Accurate LLM Inference"
description: "ASPLOS 2026 · Session 3B · oFFN：面向快速且准确的 LLM 推理的离群值与神经元感知结构化 FFN"
tags:
  - "ASPLOS2026"
  - "Session 3B"
  - "Mixture-of-Experts & Efficient Inference"
---

# oFFN: Outlier and Neuron-aware Structured FFN for Fast yet Accurate LLM Inference

**中文标题：** oFFN：面向快速且准确的 LLM 推理的离群值与神经元感知结构化 FFN

**所属 Session：** [Session 3B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Geunsoo Song (Sogang University), Hoeseok Yang (Santa Clara University), Youngmin Yi (Sogang University)

**单位：** Sogang University；Santa Clara University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790194) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

With the advent of large-scale language models (LLMs), various optimization techniques have been proposed to enable efficient inference. Among these, methods that aggressively exploit output activation sparsity have attracted significant attention, which leverage ReLU-fied LLMs and skip the entire memory accesses as well as the computation for the output element if it was predicted as sparse. Achieving fast and accurate prediction of output activation sparsity is crucial to enhancing inference efficiency. However, in practice, phenomena such as activation outliers and hot and cold neurons, which significantly affect the exploitation of sparsity during LLM inference, have either been addressed individually or not structurally integrated in existing work. In this paper, we reveal that these two phenomena are closely related and propose a novel FFN architecture called oFFN (Outlier-aware Structured FFN) that effectively exploits them simultaneously. The proposed method rearranges the FFN weights in both row and column dimensions to enable efficient and accurate prediction of output sparsity, considering outliers, and to enable separation of hot and cold neurons, computing them with respective optimal operations. The proposed method allows for the optimal computation path for each neuron, even when the batch size dynamically changes. Compared to existing sparsity prediction techniques, our method achieves the fastest speed with negligible accuracy loss. Experimental results show that it delivers up to 2.01× faster end-to-end inference speed compared to dense inference, and up to 5.46× acceleration in FFN layers under autoregressive decoding in ReLU-fied LLMs.

## 中文摘要

随着大规模语言模型（LLM）的出现，人们提出了各种优化技术以实现高效推理。其中，积极利用输出激活稀疏性的方法引起了广泛关注，这类方法借助 ReLU 化的 LLM，若某个输出元素被预测为稀疏，则跳过其全部内存访问以及计算。快速且准确地预测输出激活稀疏性对于提升推理效率至关重要。然而在实践中，激活离群值以及热神经元与冷神经元等现象会显著影响 LLM 推理过程中对稀疏性的利用，而这些现象在既有工作中要么被单独处理，要么未被结构化地整合。本文揭示这两种现象密切相关，并提出一种名为 oFFN（Outlier-aware Structured FFN）的新颖 FFN 架构，以同时有效地利用它们。所提方法在行和列两个维度上重排 FFN 权重，从而在考虑离群值的情况下实现高效且准确的输出稀疏性预测，并实现热神经元与冷神经元的分离，以各自最优的操作对它们进行计算。所提方法即使在大批量大小动态变化时，也能为每个神经元提供最优的计算路径。与现有的稀疏性预测技术相比，我们的方法在可忽略的精度损失下达到了最快速度。实验结果表明，在 ReLU 化的 LLM 中，相较稠密推理，它带来了最高 2.01× 的端到端推理速度提升，并在自回归解码下的 FFN 层中实现了最高 5.46× 的加速。

## 英文关键词

Activation Sparsity Prediction, Structured Sparsity, Large Language Models

## 中文关键词

激活稀疏性预测；结构化稀疏；大语言模型

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790194)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 3B](index.md) · [返回 ASPLOS 2026](../index.md)
