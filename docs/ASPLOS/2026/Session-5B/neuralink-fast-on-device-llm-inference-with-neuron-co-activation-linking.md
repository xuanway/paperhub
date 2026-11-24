---
title: "Neuralink: Fast on-Device LLM Inference with Neuron Co-Activation Linking"
description: "ASPLOS 2026 · Session 5B · Neuralink：利用神经元共激活链接实现快速的端侧 LLM 推理"
tags:
  - "ASPLOS2026"
  - "Session 5B"
  - "On-Device & Edge AI"
---

# Neuralink: Fast on-Device LLM Inference with Neuron Co-Activation Linking

**中文标题：** Neuralink：利用神经元共激活链接实现快速的端侧 LLM 推理

**所属 Session：** [Session 5B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Tuowei Wang (Tsinghua University), Ruwen Fan (Tsinghua University), Minxing Huang (Tianjin University), Zixu Hao (Tsinghua University), Kun Li (Microsoft Research), Ting Cao (Microsoft Research), Youyou Lu (Tsinghua University), Yaoxue Zhang (Tsinghua University), Ju Ren (Tsinghua University)

**单位：** Tsinghua University；Tianjin University；Microsoft Research

**来源：** ASPLOS 2025 · Volume 3 · [论文 DOI](https://doi.org/10.1145/3676642.3736114) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Large Language Models (LLMs) have achieved remarkable success across various domains, yet deploying them on mobile devices remains an arduous challenge due to their extensive computational and memory demands. While lightweight LLMs have been developed to fit mobile environments, they suffer from degraded model accuracy. In contrast, sparsity-based techniques minimize DRAM usage by selectively transferring only relevant neurons to DRAM while retaining the full model in external storage, such as flash. However, such approaches are critically limited by numerous I/O operations, particularly on smartphones with severe IOPS constraints. In this paper, we propose Neuralink, a novel approach that accelerates LLM inference on smartphones by optimizing neuron placement in flash memory. Neuralink leverages the concept of Neuron Co-Activation, where neurons frequently activated together are linked to facilitate continuous read access and optimize I/O efficiency. Our approach incorporates a two-stage solution: an offline stage that reorganizes neuron placement based on co-activation patterns, and an online stage that employs tailored data access and caching strategies to align well with hardware characteristics. Evaluations conducted on a variety of smartphones and LLMs demonstrate that Neuralink achieves on average 1.49× improvements in end-to-end latency compared to the state-of-the-art. As the first solution to optimize storage placement under sparsity, Neuralink explores a new optimization space at the intersection of sparsity-driven algorithm and storage-level system co-design for LLM inference.

## 中文摘要

大语言模型（LLM）已在各个领域取得显著成功，然而由于其巨大的计算与内存需求，将其部署到移动设备上仍是一项艰巨的挑战。为适配移动环境，人们已开发出轻量级 LLM，但其模型精度有所下降。相比之下，基于稀疏性的技术通过仅将相关神经元选择性地传输到 DRAM、同时将完整模型保留在闪存等外部存储中，从而最小化 DRAM 使用量。然而，这类方法严重受限于大量 I/O 操作，在 IOPS 约束严苛的智能手机上尤为如此。本文提出 Neuralink，一种通过在闪存中优化神经元放置来加速智能手机上 LLM 推理的新方法。Neuralink 利用神经元共激活（Neuron Co-Activation）的概念，将频繁共同激活的神经元链接起来，以实现连续的读取访问并优化 I/O 效率。我们的方法包含两阶段方案：离线阶段基于共激活模式重新组织神经元放置，在线阶段采用定制化的数据访问与缓存策略，以与硬件特性良好匹配。在多种智能手机和 LLM 上进行的评估表明，与最先进方案相比，Neuralink 在端到端延迟上平均取得 1.49 倍的改进。作为首个在稀疏性条件下优化存储放置的方案，Neuralink 在稀疏驱动的算法与存储级系统协同设计的交叉点上，为 LLM 推理探索了新的优化空间。

## 英文关键词

Mobile Computing, Large Language Model, Model Sparsity, Parameter Storage

## 中文关键词

移动计算；大语言模型；模型稀疏性；参数存储

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676642.3736114)
- [ASPLOS 2025 · Volume 3 论文集](https://doi.org/10.1145/3676642)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

## 来源说明

该文发表于 **ASPLOS 2025 Volume 3**，并列入 **ASPLOS 2026** 的宣讲日程。本目录按宣讲 Session 收录；引用时请使用上述 DOI 对应的出版信息。

原始摘要整理记录：

> **来源说明**：该文收录于 ASPLOS '25（第 30 届）论文集 Volume 3（`ASPLOS2025-Proceedings-volume3.pdf`），在 ASPLOS 2026 Program 中作为宣讲论文列出；本地 ASPLOS 2026 两卷论文集（Volume 1/2）未收录。

[返回 Session 5B](index.md) · [返回 ASPLOS 2026](../index.md)
