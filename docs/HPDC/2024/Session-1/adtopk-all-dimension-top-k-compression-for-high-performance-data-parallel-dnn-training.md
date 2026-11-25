---
title: "ADTopk: All-Dimension Top-k Compression for High-Performance Data-Parallel DNN Training"
description: "HPDC 2024 · Session 1 — Compression and AI"
tags:
  - "HPDC2024"
  - "Session 1"
  - "Compression and AI"
---

# ADTopk: All-Dimension Top-k Compression for High-Performance Data-Parallel DNN Training

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2024 主会 Session 1 — Compression and AI（2024年6月5日 11:20–13:00 · Session Chair：Domenico Talia）。</p>
<p class="paper-seo-summary__tags">HPDC 2024 · Session 1</p>
</div>

**官方资料**：[HPDC 2024 官方议程](https://hpdc.sci.utah.edu/2024/program.html) · [ACM DOI](https://doi.org/10.1145/3625549.3658678)

**作者**：Zhangqiang Ming, Yuchong Hu, Wenxiang Zhou, Xinjue Zheng, Chenxuan Yao, Dan Feng

**会议**：HPDC 2024 · Pisa, Italy

**Session**：Session 1 — Compression and AI（2024年6月5日 11:20–13:00 · Session Chair：Domenico Talia）

---

## 英文摘要

Data-parallel deep neural networks (DNN) training systems deployed across nodes have been widely used in various domains, while the system performance is often bottlenecked by the communication overhead among workers for synchronizing gradients. Top-k sparsification compression is the de facto approach to alleviate the communication bottleneck, which truncates the gradient to its largest k elements before sending it to other nodes. However, we observe that the traditional Top-k still has performance issues: i) the gradient at each layer of a DNN is typically represented as a tensor of multiple dimensions, and the largest k elements selected by the traditional Top-k are centered in only some of all dimensions and hence the training may miss many dimensions (we call dimension missing), which leads to low convergence performance; ii) the traditional Top-k performs the selection by globally sorting the gradient elements in each layer (we call single global sorting), which leads to a low GPU core parallelism and hence a low training throughput. In this paper, we propose an all-dimension Top-k sparsification scheme, called ADTopk, which selects the largest k elements from all dimensions of the gradient tensor in each layer, meaning that each dimension must provide some elements, so as to avoid the dimension missing. Further, ADTopk enables each dimension to perform sorting locally within the elements of the dimension, and thus all dimensions can perform multiple local sortings independently and parallelly, instead of a single global sorting for the entire gradient tensor in each layer. On top of ADTopk, we further propose an interleaving compression scheme and an efficient threshold estimation algorithm so as to enhance the performance of ADTopk. We build a sparsification compression data-parallel DNN training framework and implement a compression library containing state-of-the-art sparsification algorithms. Experiments on a local cluster and Alibaba Cloud show that compared with state-of-the-art sparsification compression methods, ADTopk improves the training throughput by 12.28%-293.49% with approximately the same convergence accuracy as the non-compression baseline.

## 中文摘要

跨节点部署的数据并行深度神经网络（DNN）训练系统已在各领域广泛使用，而系统性能往往受限于工作节点间同步梯度的通信开销。Top-k 稀疏化压缩是缓解通信瓶颈的事实标准方法，它在将梯度发送到其他节点前将其截断为最大的 k 个元素。然而，我们观察到传统 Top-k 仍存在性能问题：i) DNN 每层的梯度通常表示为多维张量，传统 Top-k 选出的最大 k 个元素仅集中在部分维度上，因而训练可能遗漏许多维度（我们称之为维度缺失），导致收敛性能偏低；ii) 传统 Top-k 通过对每层梯度元素进行全局排序来完成选择（我们称之为单一全局排序），导致 GPU 核并行度低，进而训练吞吐低。本文提出一种全维度 Top-k 稀疏化方案 ADTopk，它从每层梯度张量的所有维度中选取最大的 k 个元素，即每个维度都必须贡献一些元素，从而避免维度缺失。此外，ADTopk 使每个维度在该维度的元素内局部排序，因此所有维度可以独立并行地执行多次局部排序，而非对每层整个梯度张量做单一全局排序。在 ADTopk 之上，我们进一步提出交织压缩方案与高效阈值估计算法，以增强 ADTopk 的性能。我们构建了稀疏化压缩数据并行 DNN 训练框架，并实现了包含最先进稀疏化算法的压缩库。在本地集群与阿里云上的实验表明，与最先进的稀疏化压缩方法相比，ADTopk 在收敛精度与非压缩基线大致相同的情况下，将训练吞吐提升 12.28%–293.49%。

## 英文关键词

High Performance, Data-Parallel DNN Training, Gradient Sparsification Compression

## 中文关键词

高性能，数据并行 DNN 训练，梯度稀疏化压缩

---

[← 返回 Session 1 — Compression and AI](index.md)
