---
title: "Syno: Structured Synthesis for Neural Operators"
description: "ASPLOS 2026 · Session 6A · Syno：神经算子的结构化合成"
tags:
  - "ASPLOS2026"
  - "Session 6A"
  - "Neural Network Acceleration"
---

# Syno: Structured Synthesis for Neural Operators

**中文标题：** Syno：神经算子的结构化合成

**所属 Session：** [Session 6A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Yongqi Zhuo (Tsinghua University), Zhengyuan Su (Tsinghua University), Chenggang Zhao (Tsinghua University), Mingyu Gao (Tsinghua University)

**单位：** Tsinghua University

**来源：** ASPLOS 2025 · Volume 3 · [论文 DOI](https://doi.org/10.1145/3676642.3736118) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

The desires for better prediction accuracy and higher execution performance in neural networks never end. Neural architecture search (NAS) and tensor compilers are two popular techniques to optimize these two goals, but they are both limited to composing or optimizing existing manually designed operators rather than coming up with completely new designs. In this work, we explore the less studied direction of neural operator synthesis, which aims to automatically and efficiently discover novel neural operators with better accuracy and/or speed. We develop an end-to-end framework Syno, to realize practical neural operator synthesis. Syno makes use of a novel set of fine-grained primitives defined on tensor dimensions, which ensure various desired properties to ease model training, and also enable expression canonicalization techniques to avoid redundant candidates during search. Syno further adopts a novel guided synthesis flow to obtain valid operators matched with the specified input/output dimension sizes, and leverages efficient stochastic tree search algorithms to quickly explore the design space. We demonstrate that Syno discovers better operators with average speedups of 1.37× to 2.06× on various hardware and compiler choices, while keeping less than 1% accuracy loss even on NAS-optimized models.

## 中文摘要

对神经网络更高预测精度和更优执行性能的追求永无止境。神经架构搜索（NAS）和张量编译器是优化这两个目标的两种流行技术，但它们都局限于组合或优化现有的人工设计算子，而无法提出全新的设计。在本工作中，我们探索了研究较少的神经算子合成方向，旨在自动且高效地发现具有更好精度和/或速度的新颖神经算子。我们开发了一个端到端框架 Syno，以实现实用的神经算子合成。Syno 利用一组定义在张量维度上的新颖细粒度原语，这些原语确保多种所需性质以便于模型训练，同时也使表达式规范化技术能够避免搜索过程中的冗余候选。Syno 进一步采用一种新颖的引导式合成流程，以获得与指定输入/输出维度大小匹配的有效算子，并利用高效的随机树搜索算法快速探索设计空间。我们证明，Syno 在各种硬件和编译器选择下发现了更优算子，平均加速 1.37 倍至 2.06 倍，即使在经 NAS 优化的模型上也保持低于 1% 的精度损失。

## 英文关键词

Program Synthesis; Neural Architecture Search

## 中文关键词

程序合成；神经架构搜索

## 代码与研究制品

- [代码仓库](https://github.com/tsinghua-ideal/Syno)
- [实验复现仓库](https://github.com/Yongqi-Zhuo/Syno-AE)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676642.3736118)
- [ASPLOS 2025 · Volume 3 论文集](https://doi.org/10.1145/3676642)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

## 来源说明

该文发表于 **ASPLOS 2025 Volume 3**，并列入 **ASPLOS 2026** 的宣讲日程。本目录按宣讲 Session 收录；引用时请使用上述 DOI 对应的出版信息。

原始摘要整理记录：

> **来源说明**：该文收录于 ASPLOS '25（第 30 届）论文集 Volume 3（`ASPLOS2025-Proceedings-volume3.pdf`），在 ASPLOS 2026 Program 中作为宣讲论文列出；本地 ASPLOS 2026 两卷论文集（Volume 1/2）未收录。

[返回 Session 6A](index.md) · [返回 ASPLOS 2026](../index.md)
