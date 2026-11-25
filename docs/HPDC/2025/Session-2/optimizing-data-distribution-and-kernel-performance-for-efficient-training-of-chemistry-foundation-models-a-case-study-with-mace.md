---
title: "Optimizing Data Distribution and Kernel Performance for Efficient Training of Chemistry Foundation Models: A Case Study with MACE"
description: "HPDC 2025 · Session 2 — Model Training"
tags:
  - "HPDC2025"
  - "Session 2"
  - "Model Training"
---

# Optimizing Data Distribution and Kernel Performance for Efficient Training of Chemistry Foundation Models: A Case Study with MACE

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2025 主会 Session 2 — Model Training（2025年7月21日 13:15–15:00 · Session Chair：Ali Jannesari）。</p>
<p class="paper-seo-summary__tags">HPDC 2025 · Session 2</p>
</div>

**官方资料**：[HPDC 2025 官方议程](https://hpdc.sci.utah.edu/2025/program.html) · [ACM DOI](https://doi.org/10.1145/3731545.3731594) · [Slides](https://hpdc.sci.utah.edu/2025/assets/slides/main_session/firoz.pdf)

**作者**：Jesun Sahariar Firoz, Franco Pellegrini, Mario Geiger, Darren Hsu, Jenna A. Bilbrey, Han-Yi Chou, Maximilian Stadler, Markus Hoehnerbach, Tingyu Wang, Dejun Lin, Emine Kucukbenli, Henry W. Sprueill, Ilyes Batatia, Sotiris S. Xantheas, MalSoon Lee, Chris Mundy, Gabor Csanyi, Justin S. Smith, Ponnuswamy Sadayappan, Sutanay Choudhury

**会议**：HPDC 2025 · Notre Dame, IN, USA

**Session**：Session 2 — Model Training（2025年7月21日 13:15–15:00 · Session Chair：Ali Jannesari）

---

## 英文摘要

Chemistry Foundation Models (CFMs) that leverage Graph Neural Networks (GNNs) operating on 3D molecular graph structures are becoming indispensable tools for computational chemists and materials scientists. These models facilitate the understanding of matter and the discovery of new molecules and materials. In contrast to GNNs operating on large homogeneous graphs, GNNs used by CFMs process a large number of geometric graphs of varying sizes, requiring different optimization strategies than those developed for large homogeneous GNNs. This paper presents optimizations for two critical phases of CFM training: data distribution and model training, targeting MACE - a state-of-the-art CFM. We address the challenge of load balancing in data distribution by formulating it as a multi-objective bin packing problem. We propose an iterative algorithm that provides a highly effective, fast, and practical solution, ensuring efficient data distribution. For the training phase, we identify symmetric tensor contraction as the key computational kernel in MACE and optimize this kernel to improve the overall performance. Our combined approach of balanced data distribution and kernel optimization significantly enhances the training process of MACE. Experimental results demonstrate a substantial speedup, reducing per-epoch execution time for training from 12 to 2 minutes on 740 GPUs with a 2.6M sample dataset.

## 中文摘要

利用图神经网络（GNN）处理三维分子图结构的化学基础模型（CFM）正成为计算化学家和材料科学家不可或缺的工具。这些模型有助于理解物质、发现新分子与新材料。与处理大型同构图 GNN 不同，CFM 使用的 GNN 要处理大量规模各异的几何图，因而需要不同于大型同构 GNN 的优化策略。本文针对 CFM 训练的两个关键阶段——数据分布与模型训练——提出优化，研究对象是 MACE，一个最先进的 CFM。我们将数据分布中的负载均衡挑战建模为多目标装箱问题，并提出一种迭代算法，给出高效、快速且实用的解，确保数据分布高效。在训练阶段，我们识别出对称张量缩并是 MACE 中的关键计算核，并对其优化以提升整体性能。平衡数据分布与核优化相结合，显著改善了 MACE 的训练过程。实验结果表明加速显著：在 740 块 GPU、260 万样本数据集上，每个 epoch 的训练执行时间从 12 分钟降至 2 分钟。

## 英文关键词

Geometric graph neural networks, geometric graphs, Computational chemistry, Foundation models, Batching, Tensor analysis.

## 中文关键词

几何图神经网络，几何图，计算化学，基础模型，批处理，张量分析。

---

[← 返回 Session 2 — Model Training](index.md)
