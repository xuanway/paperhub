---
title: "Cambricon-DG: An Accelerator for Redundant-Free Dynamic Graph Neural Networks Based on Nonlinear Isolation"
description: "HPCA 2025 · Traversing Winning Paths"
tags:
  - "HPCA2025"
  - "Traversing Winning Paths"
---

# Cambricon-DG: An Accelerator for Redundant-Free Dynamic Graph Neural Networks Based on Nonlinear Isolation

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Traversing Winning Paths。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Traversing Winning Paths</p>
</div>

**论文链接**：
**作者**：Zhifei Yue (University of Science and Technology of China), Xinkai Song (Institute of Computing Technology，Chinese Academy of Sciences), Tianbo Liu (University of Science and Technology of China), Xing Hu (Institute of Computing Technology，Chinese Academy of Sciences), Rui Zhang (Institute of Computing Technology, Chinese Academy of Sciences), Zidong Du (Institute of Computing Technology, Chinese Academy of Sciences), Wei Li (Institute of Computing Technology, Chinese Academy of Sciences), Qi Guo (Institute of Computing Technology, Chinese Academy of Sciences), Tianshi Chen (Institute of Computing Technology, Chinese Academy of Sciences)
**会议**：HPCA 2025

---

## 中文标题

Cambricon-DG：基于非线性隔离的无冗余动态图神经网络加速器

## 英文摘要

Dynamic Graph Neural Networks (DGNNs) have demonstrated significant potential in handling temporal graph-structured data. Typical DGNNs combine GNNs to process the structural information of graph and RNNs to capture the dynamic temporal information of graphs. However, current GNN accelerators process DGNNs by treating graph snapshots as static entities, leading to substantial redundant computations and memory accesses. While some DGNN accelerators have attempted to mitigate this redundancy, they face the challenge of maintaining accuracy for incremental processing due to the nonlinear activation function in GNNs. To address these issues, we propose a novel nonlinear isolation mechanism for incremental processing of DGNNs, which eliminates all redundant operations without accuracy loss. Additionally, we introduce a vertex-wise computation scheme for RNNs to minimize redundancy and reduce off-chip memory access. To validate the effectiveness of the mechanism, we implemented software optimizations on GPUs, achieving an 8.53× performance improvement over full-graph computation schemes. To address the inefficiency of graph topology operations on GPUs, we propose the Cambricon-DG accelerator, which features a dedicated hardware pipeline, an efficient topology management engine for graph traversal and topology sorting, and a hybrid computation engine that supports both GNN and RNN computations, thus improving hardware utilization. We evaluate Cambricon-DG on seven real-world dynamic graph datasets using five representative DGNN models. The results show that Cambricon-DG achieves an average speedup of 49.73×, 12.15×, and 7.03×, and an average energy saving of 41.31×, 9.47×, and 5.23× over the state-of-the-art static/dynamic GNN accelerators I-GCN, RACE, and DeltaGNN, respectively.

## 中文摘要

动态图神经网络（DGNN）在处理时序图结构数据方面展现出巨大潜力。典型 DGNN 结合 GNN 处理图的结构信息与 RNN 捕捉图的动态时序信息。然而现有 GNN 加速器将图快照视为静态实体来处理 DGNN，导致大量冗余计算与内存访问。尽管部分 DGNN 加速器尝试缓解该冗余，但由于 GNN 中的非线性激活函数，其在增量处理时难以保持精度。为此我们提出一种新颖的非线性隔离机制用于 DGNN 增量处理，可在无精度损失的前提下消除全部冗余操作。此外，我们为 RNN 引入顶点级计算方案以最小化冗余并减少片外内存访问。为验证该机制的有效性，我们在 GPU 上实现了软件优化，相比全图计算方案取得 8.53 倍性能提升。针对 GPU 上图拓扑操作效率低下的问题，我们提出 Cambricon-DG 加速器，其具备专用硬件流水线、用于图遍历与拓扑排序的高效拓扑管理引擎，以及同时支持 GNN 与 RNN 计算的混合计算引擎，从而提升硬件利用率。我们使用五种代表性 DGNN 模型在七个真实动态图数据集上评估 Cambricon-DG。结果表明，与最先进的静态/动态 GNN 加速器 I-GCN、RACE 和 DeltaGNN 相比，Cambricon-DG 平均分别取得 49.73 倍、12.15 倍和 7.03 倍加速比，并平均分别节省 41.31 倍、9.47 倍和 5.23 倍能量。
