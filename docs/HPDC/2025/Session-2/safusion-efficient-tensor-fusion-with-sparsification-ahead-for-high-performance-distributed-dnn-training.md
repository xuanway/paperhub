---
title: "SAFusion: Efficient Tensor Fusion with Sparsification Ahead for High-Performance Distributed DNN Training"
description: "HPDC 2025 · Session 2 — Model Training"
tags:
  - "HPDC2025"
  - "Session 2"
  - "Model Training"
---

# SAFusion: Efficient Tensor Fusion with Sparsification Ahead for High-Performance Distributed DNN Training

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2025 主会 Session 2 — Model Training（2025年7月21日 13:15–15:00 · Session Chair：Ali Jannesari）。</p>
<p class="paper-seo-summary__tags">HPDC 2025 · Session 2</p>
</div>

**官方资料**：[HPDC 2025 官方议程](https://hpdc.sci.utah.edu/2025/program.html) · [ACM DOI](https://doi.org/10.1145/3731545.3731581) · [Slides](https://hpdc.sci.utah.edu/2025/assets/slides/main_session/ming.pdf)

**作者**：Zhangqiang Ming, Yuchong Hu, Xinjue Zheng, Wenxiang Zhou, Dan Feng

**会议**：HPDC 2025 · Notre Dame, IN, USA

**Session**：Session 2 — Model Training（2025年7月21日 13:15–15:00 · Session Chair：Ali Jannesari）

---

## 英文摘要

Distributed deep neural networks (DNN) training systems deployed across workers have been widely used in various domains, while the communication overhead among workers for synchronizing gradient tensors often becomes the performance bottleneck. To optimize communication efficiency, state-of-the-art studies often apply both two techniques: i) gradient sparsification compression, which truncates the gradient to its largest elements to reduce the communication traffic, and ii) tensor fusion, which merges multiple gradient tensors within a fusion buffer to transmit them together to reduce the communication startup overhead. However, we find that existing studies often apply gradient sparsification after tensor fusion (we call sparsification-behind tensor fusion), which leads to a fact that a lot of fused gradient tensors are missed after the sparsification, thus impairing the convergence performance. In this paper, we propose a new tensor fusion mechanism for high-performance distributed DNN training, called SAFusion, which performs sparsification on each of gradient tensors before merging them during tensor fusion, instead of sparsification-behind tensor fusion, so as to avoid gradient tensor missing and thus improve the convergence performance. Further, we find that SAFusion will face two limitations: the long synchronization waiting time across different workers and many waiting periods within each worker during tensor fusion, so we propose two efficient (inter-worker and intra-worker) tensor fusion schemes to address the two limitations. We prototype SAFusion, and experiments on local and cloud clusters show that SAFusion improves the training throughput by 49.71%-144.42% over training without tensor fusion, and by 18.96%-60.89% over state-of-the-art tensor fusion schemes, while maintaining approximately the same convergence performance as the non-compression baseline.

## 中文摘要

部署在多个工作节点上的分布式深度神经网络（DNN）训练系统已在各领域广泛使用，而工作节点间同步梯度张量的通信开销往往成为性能瓶颈。为优化通信效率，最先进的研究通常同时应用两种技术：i) 梯度稀疏化压缩，将梯度截断为最大的元素以减少通信流量；ii) 张量融合，将一个融合缓冲区内的多个梯度张量合并后一起传输，以降低通信启动开销。然而，我们发现现有研究往往在张量融合之后进行梯度稀疏化（我们称之为“稀疏化在后”的张量融合），导致大量已融合的梯度张量在稀疏化后被遗漏，从而损害收敛性能。本文提出一种面向高性能分布式 DNN 训练的新张量融合机制 SAFusion：它在张量融合时先对每个梯度张量分别进行稀疏化，再将其合并，而非“稀疏化在后”，从而避免梯度张量遗漏并改善收敛性能。此外，我们发现 SAFusion 会面临两个局限：不同工作节点间较长的同步等待时间，以及每个工作节点内张量融合期间的多个等待期；因此我们提出两种高效方案（工作节点间与工作节点内）来解决这两个局限。我们实现了 SAFusion 原型，在本地与云集群上的实验表明，相比不使用张量融合的训练，SAFusion 将训练吞吐提升 49.71%–144.42%；相比最先进的张量融合方案提升 18.96%–60.89%，同时保持与非压缩基线大致相同的收敛性能。

## 英文关键词

High Performance, Distributed DNN Training, Gradient Sparsification Compression, Tensor Fusion

## 中文关键词

高性能，分布式 DNN 训练，梯度稀疏化压缩，张量融合

---

[← 返回 Session 2 — Model Training](index.md)
