---
title: "Dynamic Sparsity in Large-Scale Video DiT Training"
description: "ASPLOS 2026 · Session 2A · 大规模视频 DiT 训练中的动态稀疏性"
tags:
  - "ASPLOS2026"
  - "Session 2A"
  - "LLM Training Systems"
---

# Dynamic Sparsity in Large-Scale Video DiT Training

**中文标题：** 大规模视频 DiT 训练中的动态稀疏性

**所属 Session：** [Session 2A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Xin Tan (The Chinese University of Hong Kong), Yuetao Chen (The Chinese University of Hong Kong), Yimin Jiang (Unaffiliated), Xing Chen (StepFun), Kun Yan (StepFun), Nan Duan (StepFun), Yibo Zhu (StepFun), Daxin Jiang (StepFun), Hong Xu (The Chinese University of Hong Kong)

**单位：** The Chinese University of Hong Kong；Unaffiliated；StepFun

**来源：** ASPLOS 2026 · Volume 1 · [论文 DOI](https://doi.org/10.1145/3760250.3762216) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Diffusion Transformers (DiTs) have shown remarkable performance in generating high-quality videos. However, the quadratic complexity of 3D full attention remains a bottleneck in scaling DiT training, especially with high-definition, lengthy videos, where it can consume up to 95% of processing time and demand specialized context parallelism. This paper introduces DSV to accelerate video DiT training by leveraging the dynamic attention sparsity we empirically observe. DSV uses a two-stage algorithm to capture the dynamic sparsity patterns via low-rank based approximation of the original query and key. It employs custom kernels to efficiently identify critical key-value pairs and compute the sparse attention. To accommodate the new sparsity dimension, DSV adopts a hybrid sparsity-aware context parallelism that re-balances the skewed workload across attention heads and blocks due to sparsity heterogeneity. DSV achieves up to 3.02× higher training throughput, scaling to 128 GPUs and 520k token lengths, while maintaining model quality comparable to full attention schemes.

## 中文摘要

扩散 Transformer（DiT）在生成高质量视频方面已展现出显著性能。然而，3D 全注意力的二次复杂度仍是扩展 DiT 训练的瓶颈，尤其在高清、长时长视频场景下，其可占用高达 95% 的处理时间，并需要专门的上下文并行。本文提出 DSV，通过利用我们在实验中观察到的动态注意力稀疏性来加速视频 DiT 训练。DSV 采用两阶段算法，经由对原始 query 和 key 的低秩近似来捕获动态稀疏模式。它使用定制 kernel 来高效识别关键的键值对并计算稀疏注意力。为适应新的稀疏性维度，DSV 采用稀疏感知的混合上下文并行，重新平衡因稀疏性异质性而在注意力头和块之间造成的偏斜负载。DSV 实现了最高 3.02× 的训练吞吐提升，可扩展至 128 个 GPU 和 520k 的 token 长度，同时保持与全注意力方案相当的模型质量。

## 英文关键词

Large-scale training; distributed system; parallelism; video generation

## 中文关键词

大规模训练；分布式系统；并行；视频生成

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3760250.3762216)
- [ASPLOS 2026 · Volume 1 论文集](https://doi.org/10.1145/3760250)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 2A](index.md) · [返回 ASPLOS 2026](../index.md)
