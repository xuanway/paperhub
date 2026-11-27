---
title: "CROSS: Compiler-Driven Optimization of Sparse DNNs Using Sparse/Dense Computation Kernels"
description: "HPCA 2025 · Stacking the Layers (Sparsity)"
tags:
  - "HPCA2025"
  - "Stacking the Layers (Sparsity)"
---

# CROSS: Compiler-Driven Optimization of Sparse DNNs Using Sparse/Dense Computation Kernels

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Stacking the Layers (Sparsity)。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Stacking the Layers (Sparsity)</p>
</div>

**论文链接**：
**作者**：Fangxin Liu (Shanghai Jiao Tong University), Shiyuan Huang (Shanghai Jiao Tong University), Ning Yang (Shanghai Jiao Tong University), Zongwu Wang (Shanghai Jiao Tong University), Haomin Li (Shanghai Jiao Tong University), Li Jiang (Shanghai Jiao Tong University)
**会议**：HPCA 2025

---

## 中文标题

CROSS：利用稀疏/稠密计算内核的编译器驱动稀疏 DNN 优化

## 英文摘要

As deep learning models continue to grow larger and more complex, exploiting sparsity is becoming one of the most critical areas for enhancing efficiency and scalability. Several methods for leveraging sparsity have been proposed to more effectively balance the trade-off between compression ratio and accuracy. While these methods offer algorithmic advantages, they also introduce significant hardware overhead due to index-based encoding and decoding. In this paper, we propose CROSS, an end-to-end compilation optimization technique to achieve sparse DNN acceleration using GPU computation kernels. The key insight behind CROSS is to exploit parameter distribution locality and reconcile the “sparse” DNN computation with the high-performance “dense” computation kernels. Specifically, we perform an in-depth analysis of sparse operations in mainstream DNN computing frameworks. We then decompose the sparse workload into multiple components to create highly efficient, specialized operators with different sparsity levels. Additionally, we introduce a novel sparse graph translation technique to facilitate computation kernel processing of the sparse workload. The resulting CROSS framework can accommodate various sparsity patterns and optimization techniques, delivering an average 2.03× speedup on inference latency compared to seven state-of-the-art solutions with smaller memory footprints across various models and datasets.

## 中文摘要

随着深度学习模型不断增大并日趋复杂，利用稀疏性正成为提升效率与可扩展性最关键的方向之一。已有若干利用稀疏性的方法被提出，以更有效地在压缩率与精度之间取得平衡。这些方法虽带来算法优势，但也因基于索引的编码与解码而引入显著的硬件开销。本文提出 CROSS，一种端到端编译优化技术，利用 GPU 计算内核实现稀疏 DNN 加速。CROSS 的核心洞见是利用参数分布局部性，并将“稀疏”的 DNN 计算与高性能的“稠密”计算内核协调起来。具体而言，我们深入分析了主流 DNN 计算框架中的稀疏运算，然后将稀疏负载分解为多个分量，以构建具有不同稀疏度的高效专用算子。此外，我们引入一种新颖的稀疏图转换技术，以便计算内核处理该稀疏负载。所得的 CROSS 框架可适配各种稀疏模式与优化技术，在多种模型与数据集上相比七种最先进方案平均取得 2.03 倍的推理时延加速，且内存占用更小。
