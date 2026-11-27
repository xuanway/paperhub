---
title: "Scaling Graph Neural Network Training via Geometric Optimization"
description: "HPCA 2026 · Graph Neural Networks and Retrieval Systems"
tags:
  - "HPCA2026"
  - "Graph Neural Networks and Retrieval Systems"
---

# Scaling Graph Neural Network Training via Geometric Optimization

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Graph Neural Networks and Retrieval Systems。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Graph Neural Networks and Retrieval Systems</p>
</div>

**论文链接**：
**作者**：Fangzhou Ye University of Central Florida , Lingxiang Yin University of Central Florida , Hao Zheng University of Central Florida
**会议**：HPCA 2026

---

## 中文标题

借助几何优化扩展图神经网络训练

## 英文摘要

Wafer-scale computing has emerged as an alternative solution to sustain performance scaling in the post-Moore era, driven by recent technology advancements such as chiplet integration. This enables considerable computing and storage capabilities on a single chip, making it capable of accommodating large machine learning models and datasets. Recent efforts have heralded the promise of wafer-scale architectures for deep learning inference and training. However, scaling the training of Graph Neural Networks in wafer-scale architecture remains a challenge and is relatively unexplored due to irregularities in gradient propagation as well as physical constraints from flat on-chip topologies. In this paper, we propose Aster, a topology-aware framework designed to efficiently support GNN training on arbitrary wafer-scale architectures. The proposed framework, as opposed to the current application or topology-specific heuristics, can be generalized to support any network topology and irregular GNN datasets. Specifically, we mathematically formulate commonly seen network topologies in their geometric representation and prioritize communication efficiency during GNN workload partitioning and mapping. Based on the geometric representation, we propose a quadratic assignment problem solver to efficiently map irregular dataflows to a flat topology with reduced communication distance. The simulation results show that Aster can achieve performance speedup by 2.91×, 1.50×, 1.84×, and 1.58× in Mesh and speedup by 3.84×, 1.56×, 2.05×, and 1.49× in Torus on average compared to Mini-cut [1], ScalaGraph [2], Chunk-V [3], and Chunk-E [4], respectively.

## 中文摘要

晶圆级计算已成为后摩尔时代维持性能扩展的替代方案，这得益于芯粒集成等近期技术进步。它可在单芯片上提供可观的计算与存储能力，从而能够容纳大型机器学习模型与数据集。近期工作预示了晶圆级架构在深度学习推理与训练方面的前景。然而，由于梯度传播的不规则性以及平面片上拓扑的物理约束，在晶圆级架构上扩展图神经网络训练仍是一个挑战，相关研究相对匮乏。本文提出 Aster，一个拓扑感知框架，旨在高效支持任意晶圆级架构上的 GNN 训练。该框架有别于当前针对特定应用或拓扑的启发式方法，可泛化以支持任意网络拓扑与不规则 GNN 数据集。具体而言，我们将常见的网络拓扑用其几何表示进行数学建模，并在 GNN 负载划分与映射时优先考虑通信效率。基于该几何表示，我们提出一个二次指派问题求解器，以更短的通信距离高效地将不规则数据流映射到平面拓扑上。模拟结果表明，Aster 在 Mesh 拓扑上相比 Mini-cut [1]、ScalaGraph [2]、Chunk-V [3] 和 Chunk-E [4] 平均分别取得 2.91 倍、1.50 倍、1.84 倍和 1.58 倍的性能加速，在 Torus 拓扑上分别取得 3.84 倍、1.56 倍、2.05 倍和 1.49 倍的加速。
