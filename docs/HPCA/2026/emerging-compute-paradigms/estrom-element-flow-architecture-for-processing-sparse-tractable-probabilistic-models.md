---
title: "ESTroM: Element-Flow Architecture For Processing Sparse Tractable Probabilistic Models"
description: "HPCA 2026 · Emerging Compute Paradigms"
tags:
  - "HPCA2026"
  - "Emerging Compute Paradigms"
---

# ESTroM: Element-Flow Architecture For Processing Sparse Tractable Probabilistic Models

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Emerging Compute Paradigms。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Emerging Compute Paradigms</p>
</div>

**论文链接**：
**作者**：anjunyi fan Peking University , Xuejie Liu Peking University , Anji Liu University of California, Los Angeles , Qiuping Wu Peking University , Jiaqi Yang Peking University , Yuchao Qin Peking University , Guy Van den Broeck University of California at Los Angeles , Yitao Liang Peking University , Bonan Yan Peking University
**会议**：HPCA 2026

---

## 中文标题

ESTroM：处理稀疏易处理概率模型的元素流架构

## 英文摘要

Probabilistic Circuits (PCs) models are emerging popular tractable probabilistic models. Their internal connections are represented in the form of directed acyclic graphs (DAGs) with sum nodes and product nodes, ensuring their internal parameter efficiency and model expressiveness in terms of probabilistic inference. Despite these algorithmic advantages, executing PC still faces graph structure deployment issues. PyJuice on GPU with the block-sparse parallel computation methods causes a parallelism-sparsity gap, while DAG-style processing does not take advantage of the repetitive characteristics of PC internal nodes, resulting in low throughput. To address this challenge, this work proposes the ESTroM, an efficient architecture that provides novel graph-element (nodes/edges) parallelism with sparsity-aware compilation. Through analysis of the sum/product node computational requirements, ESTroM core uses compressed matrices for sum/product nodes DAG representations, edge-based dataflow for product node processing, and node-based dataflow for sum node processing. With intra-core rewind and inter-core multicast optimizations, we develop a prototype ESTroM chip and a demonstrative system for a PC-based neural lossless compression application. Our ablation experiments show ESTroM offers a speed improvement of 2.11∼3.79× compared to the state-of-the-art DAG processing unit (DPU)-v2 with the same computing resources. Under various typical PC structures, ESTroM achieves a speedup of 18.7× compared to DPU-v2 and 3.9× compared to NVIDIA RTX 4090 GPU with PyJuice framework. In terms of neural lossless compression, ESTroM demonstrates a 1.39× improvement in compression ratio compared to the industrial-standard Z-standard (Zstd) algorithms with the highest compression level, while offering 16.3∼65.2× improvement in compression speed compared to Zstd on Intel Xeon Gold 6230. In a nutshell, this work develops novel graph element parallelism and element-flow architecture theory with practical prototype chips and systems, revealing a new hardware-perspective path for the “scaling law” of emerging tractable probabilistic models.

## 中文摘要

概率电路（PC）是一类新兴的易处理概率模型，其内部连接以含求和节点与乘积节点的有向无环图（DAG）表示，在概率推断上兼具参数效率与表达能力。尽管具备算法优势，PC 的执行仍面临图结构部署问题：GPU 上的 PyJuice 采用块稀疏并行计算，造成并行度与稀疏性之间的鸿沟；而 DAG 式处理未利用 PC 内部节点的重复特征，吞吐偏低。为此，本文提出 ESTroM，一种高效架构，提供新颖的图元素（节点/边）并行与稀疏感知编译。通过分析求和/乘积节点的计算需求，其核心用压缩矩阵表示节点 DAG，乘积节点采用基于边的数据流、求和节点采用基于节点的数据流，并结合核内回卷与核间多播优化，研制出原型芯片及面向 PC 神经网络无损压缩的演示系统。消融实验显示，在相同计算资源下，ESTroM 相比最先进的 DAG 处理单元 DPU-v2 加速 2.11∼3.79 倍；在多种典型 PC 结构下，相比 DPU-v2 与采用 PyJuice 框架的 NVIDIA RTX 4090 GPU 分别加速 18.7 倍和 3.9 倍。在神经网络无损压缩方面，相比最高压缩等级的工业标准 Zstd 算法，压缩比提升 1.39 倍，同时在 Intel Xeon Gold 6230 上压缩速度提升 16.3∼65.2 倍。综上，本文提出新的图元素并行与元素流架构理论，并给出实用原型芯片与系统。
