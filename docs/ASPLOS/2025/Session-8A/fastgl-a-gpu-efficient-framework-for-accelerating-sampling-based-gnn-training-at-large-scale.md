---
title: "FastGL: A GPU-Efficient Framework for Accelerating Sampling-Based GNN Training at Large Scale"
description: "ASPLOS 2025 · Session 8A · FastGL：面向大规模采样式 GNN 训练的 GPU 高效框架"
tags:
  - "ASPLOS2025"
  - "Session 8A"
  - "ML Training"
---

# FastGL: A GPU-Efficient Framework for Accelerating Sampling-Based GNN Training at Large Scale

**中文标题：** FastGL：面向大规模采样式 GNN 训练的 GPU 高效框架

**所属 Session：** [Session 8A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Zeyu Zhu (Institute of Automation, Chinese Academy of Sciences,School of Future Technology, University of Chinese Academy of Sciences), Peisong Wang (Institute of Automation, Chinese Academy of Sciences), Qinghao Hu (Institute of Automation, Chinese Academy of Sciences,AiRiA), Gang Li (Shanghai Jiao Tong University), Xiaoyao Liang (Shanghai Jiao Tong University), Jian Cheng (Institute of Automation, Chinese Academy of Sciences,AiRiA)

**单位：** Institute of Automation, Chinese Academy of Sciences,School of Future Technology, University of Chinese Academy of Sciences；Institute of Automation, Chinese Academy of Sciences；Institute of Automation, Chinese Academy of Sciences,AiRiA；Shanghai Jiao Tong University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3622781.3674167) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Graph Neural Networks (GNNs) have shown great superiority on non-Euclidean graph data, achieving ground-breaking performance on various graph-related tasks. As a practical solution to train GNN on large graphs with billions of nodes and edges, the sampling-based training is widely adopted by existing training frameworks. However, through an in-depth analysis, we observe that the efficiency of existing samplingbased training frameworks is still limited due to the key bottlenecks lying in all three phases of sampling-based training, i.e., subgraph sample, memory IO, and computation. To this end, we propose FastGL, a GPU-efficient Framework for accelerating sampling-based training of GNN at Large scale by simultaneously optimizing all above three phases, taking into account both GPU characteristics and graph structure. Specifically, by exploiting the inherent overlap within graph structures, FastGL develops the Match-Reorder strategy to reduce the data traffic, which accelerates the memory IO without incurring any GPU memory overhead. Additionally, FastGL leverages a Memory-Aware computation method, harnessing the GPU memory's hierarchical nature to mitigate irregular data access during computation. FastGL further incorporates the Fused-Map approach aimed at diminishing the synchronization overhead during sampling. Extensive experiments demonstrate that FastGL can achieve an average speedup of 11.8×, 2.2× and 1.5× over the state-of-the-art frameworks PyG, DGL, and GNNLab, respectively. Our

## 中文摘要

图神经网络（GNN）在非欧几里得图数据上展现出极大优势，在各类图相关任务上取得了突破性表现。作为在具有数十亿节点和边的大图上训练 GNN 的实用方案，基于采样的训练被现有训练框架广泛采用。然而，通过深入分析，我们观察到现有采样式训练框架的效率仍然受限，其关键瓶颈存在于采样式训练的全部三个阶段，即子图采样、内存 IO 与计算。为此，我们提出 FastGL，一个面向大规模 GNN 采样式训练的 GPU 高效框架，它同时优化上述全部三个阶段，并同时考虑 GPU 特性与图结构。具体而言，通过利用图结构中固有的重叠性，FastGL 提出 Match-Reorder 策略来减少数据流量，从而在不引入任何 GPU 内存开销的前提下加速内存 IO。此外，FastGL 采用内存感知（Memory-Aware）的计算方法，利用 GPU 内存的层次特性来缓解计算过程中的不规则数据访问。FastGL 还引入了 Fused-Map 方法，旨在降低采样过程中的同步开销。大量实验表明，FastGL 相比最先进的框架 PyG、DGL 和 GNNLab 分别平均可取得 11.8×、2.2× 和 1.5× 的加速。Our

## 英文关键词

原文无 Keywords

## 中文关键词

原文无 Keywords

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3622781.3674167)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 8A](index.md) · [返回 ASPLOS 2025](../index.md)
