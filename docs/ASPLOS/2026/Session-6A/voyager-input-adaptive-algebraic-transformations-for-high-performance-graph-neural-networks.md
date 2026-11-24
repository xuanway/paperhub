---
title: "Voyager: Input-Adaptive Algebraic Transformations for High-Performance Graph Neural Networks"
description: "ASPLOS 2026 · Session 6A · Voyager：面向高性能图神经网络的输入自适应代数变换"
tags:
  - "ASPLOS2026"
  - "Session 6A"
  - "Neural Network Acceleration"
---

# Voyager: Input-Adaptive Algebraic Transformations for High-Performance Graph Neural Networks

**中文标题：** Voyager：面向高性能图神经网络的输入自适应代数变换

**所属 Session：** [Session 6A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Yangjie Zhou (Shanghai Jiao Tong University), Wenting Shen (Alibaba Group), Jingwen Leng (Shanghai Jiao Tong University), Shuwen Lu (Shanghai Jiao Tong University), Zihan Liu (Shanghai Jiao Tong University), Weihao Cui (Shanghai Jiao Tong University), Zhendong Zhang (Shanghai Qi Zhi Institute), Wencong Xiao (Alibaba Group), Baole Ai (Alibaba Group), Wei Lin (Alibaba Group), Deze Zeng (China University of Geosciences), Yun Liang (Peking University), Quan Chen (Shanghai Jiao Tong University), Ning Liu (Shanghai Jiao Tong University), Minyi Guo (Shanghai Jiao Tong University)

**单位：** Shanghai Jiao Tong University；Alibaba Group；Shanghai Qi Zhi Institute；China University of Geosciences；Peking University

**来源：** ASPLOS 2025 · Volume 3 · [论文 DOI](https://doi.org/10.1145/3676642.3736121) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Graph neural networks (GNNs) are gaining popularity in diverse application domains and growing in complexity. As a result, it is crucial to achieve high-performance GNN execution. Among various techniques, algebraic transformations, including operator reordering and operator fusion, have been successfully applied to improve the computation and memory access efficiencies of DNN models. However, directly applying these methods to GNNs results in suboptimal performance. This is primarily due to the diversity of input graph structures, making it challenging to predict performance benefits. Additionally, the complex dependencies introduced by these input graph structures limit the effectiveness of existing optimization techniques. To address these challenges, we propose𝑉𝑜𝑦𝑎𝑔𝑒𝑟, an input-adaptive compiler designed specifically for GNNs. Unlike existing methods that rely on static optimization rules,𝑉𝑜𝑦𝑎𝑔𝑒𝑟 dynamically generates and evaluates a wide range of algebraic transformation candidates, including novel reordering and fusion strategies tailored to graph characteristics. By leveraging symbolic graph attributes, 𝑉𝑜𝑦𝑎𝑔𝑒𝑟efficiently estimates tensor shapes and prunes low-performance candidates. A runtime selection module further enhances performance by choosing the optimal transformation based on real-time input features. Our evaluation shows that 𝑉𝑜𝑦𝑎𝑔𝑒𝑟 achieves an average 3.5× speedup on GPUs over the state-of-the-art works on representative GNNs and datasets.

## 中文摘要

图神经网络（GNN）在众多应用领域中日益普及，且复杂度不断提升。因此，实现高性能的 GNN 执行至关重要。在各种技术中，包括算子重排序与算子融合在内的代数变换已被成功用于提升 DNN 模型的计算效率与访存效率。然而，将这些方法直接应用于 GNN 会导致性能次优。这主要是由于输入图结构的多样性，使得性能收益难以预测；此外，这些输入图结构引入的复杂依赖关系也限制了现有优化技术的有效性。为应对这些挑战，我们提出 Voyager，一个专为 GNN 设计的输入自适应编译器。与依赖静态优化规则的现有方法不同，Voyager 动态生成并评估范围广泛的代数变换候选，其中包括针对图特征定制的新颖重排序与融合策略。借助符号图属性，Voyager 能够高效地估计张量形状并剪除低性能候选。运行时选择模块进一步根据实时输入特征选择最优变换，从而进一步提升性能。我们的评估表明，在代表性 GNN 与数据集上，Voyager 在 GPU 上相比最先进工作平均取得 3.5 倍加速。

## 英文关键词

Graph Neural Networks, Compilation Optimization, High-Performance Computing

## 中文关键词

图神经网络；编译优化；高性能计算

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676642.3736121)
- [ASPLOS 2025 · Volume 3 论文集](https://doi.org/10.1145/3676642)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

## 来源说明

该文发表于 **ASPLOS 2025 Volume 3**，并列入 **ASPLOS 2026** 的宣讲日程。本目录按宣讲 Session 收录；引用时请使用上述 DOI 对应的出版信息。

原始摘要整理记录：

> **来源说明**：该文收录于 ASPLOS '25（第 30 届）论文集 Volume 3（`ASPLOS2025-Proceedings-volume3.pdf`），在 ASPLOS 2026 Program 中作为宣讲论文列出；本地 ASPLOS 2026 两卷论文集（Volume 1/2）未收录。

[返回 Session 6A](index.md) · [返回 ASPLOS 2026](../index.md)
