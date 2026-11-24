---
title: "Generalizing Reuse Patterns for Efficient DNN on Microcontrollers"
description: "ASPLOS 2025 · Session 1C · 泛化复用模式：实现微控制器上的高效 DNN"
tags:
  - "ASPLOS2025"
  - "Session 1C"
  - "Edge Computing"
---

# Generalizing Reuse Patterns for Efficient DNN on Microcontrollers

**中文标题：** 泛化复用模式：实现微控制器上的高效 DNN

**所属 Session：** [Session 1C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Jiesong Liu (North Carolina State University), Bin Ren (College of William and Mary), Xipeng Shen (North Carolina State University)

**单位：** North Carolina State University；College of William and Mary

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716257) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Deep Neural Networks (DNNs) face challenges in deployment on resource-constrained devices due to their high computational demands. Leveraging redundancy in input data and activation maps for computation reuse is an effective way to accelerate DNN inference, especially for microcontrollers where the computing power is very limited. This work points out an important limitation in current reusebased DNN optimizations, the narrow definition of reuse patterns in data. It proposes the concept of generalized reuse and uncovers the relations between generalized reuse patterns and row/column reorder of a matrix view of the input or activation map of a DNN. It revolutionizes the conventional view of explorable reuse patterns, drastically expanding the reuse space. It further develops two novel analytical models for analyzing the impacts of reuse patterns on the accuracy and latency of DNNs, enabling efficient selection of appropriate reuse patterns. Experiments show that generalized reuse consistently brings significant benefits, regardless of the differences among DNNs or microcontroller hardware. It delivers 1.03-2.2× speedups or 1-8% accuracy improvement over conventional reuse.

## 中文摘要

深度神经网络（DNN）计算需求高，使其在资源受限设备上的部署面临挑战。利用输入数据与激活图中的冗余进行计算复用，是加速 DNN 推理的有效手段，对于计算能力极为有限的微控制器尤为如此。本工作指出当前基于复用的 DNN 优化存在一个重要局限，即对数据中复用模式的定义过于狭窄。文章提出广义复用（generalized reuse）的概念，并揭示了广义复用模式与 DNN 输入或激活图的矩阵视图行/列重排之间的关系。这一认识革新了关于可探索复用模式的传统观念，大幅拓展了复用空间。作者进一步提出两个新颖的分析模型，用于分析复用模式对 DNN 精度与时延的影响，从而能够高效地选择合适的复用模式。实验表明，无论 DNN 之间或微控制器硬件之间存在何种差异，广义复用都能持续带来显著收益：相较传统复用，可实现 1.03–2.2 倍加速或 1–8% 的精度提升。

## 英文关键词

real-time machine learning, compiler optimization

## 中文关键词

实时机器学习；编译器优化

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716257)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 1C](index.md) · [返回 ASPLOS 2025](../index.md)
