---
title: "AccelES: Accelerating Top-K SpMV for Embedding Similarity via Low-bit Pruning"
description: "HPCA 2025 · Stacking the Layers (Sparsity)"
tags:
  - "HPCA2025"
  - "Stacking the Layers (Sparsity)"
---

# AccelES: Accelerating Top-K SpMV for Embedding Similarity via Low-bit Pruning

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Stacking the Layers (Sparsity)。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Stacking the Layers (Sparsity)</p>
</div>

**论文链接**：
**作者**：Jiaqi Zhai (Huazhong University of Science and Technology), Xuanhua Shi (Huazhong University of Science and Technology), Kaiyi Huang (Huazhong University of Science and Technology), Chencheng Ye (Huazhong University of Science and Technology), Weifang Hu (Huazhong University of Science and Technology), Bingsheng He (National University of Singapore), Hai Jin (Huazhong University of Science and Technology)
**会议**：HPCA 2025

---

## 中文标题

AccelES：通过低比特剪枝加速面向嵌入相似度的 Top-K SpMV

## 英文摘要

In the realm of recommendation systems, achieving real-time performance in embedding similarity tasks is often hindered by the limitations of traditional Top-K sparse matrix-vector multiplication (SpMV) methods, which suffer from high latency due to inefficient memory access patterns. This paper identifies these critical gaps and introduces AccelES, a novel approach that significantly enhances the efficiency of Top-K SpMV. Our method employs a two-stage calculation scheme: the first stage utilizes a compact, low-bit dataset to quickly identify the most relevant entries, while the second stage performs full-precision calculations solely on this pruned subset, thereby minimizing computational overhead. Furthermore, AccelES incorporates innovative matrix representations, Ultra-CSR and Random-CSR, which optimize memory bandwidth utilization. Experimental results demonstrate that AccelES accelerates performance, surpassing state-of-the-art FPGA, GPU, and CPU solutions by factors of 3.4×, 2.5×, and 153.3×, respectively, under controlled conditions. These advancements not only enhance processing speed but also significantly improve real-time performance in recommendation systems, establishing AccelES as a pivotal contribution to the field of Top-K sparse matrix-vector multiplication.

## 中文摘要

在推荐系统领域，嵌入相似度任务的实时性能常因传统 Top-K 稀疏矩阵向量乘（SpMV）方法的局限而受阻，这些方法因低效的内存访问模式而具有高时延。本文指出上述这些关键缺口，并提出 AccelES，一种显著提升 Top-K SpMV 效率的新方法。我们的方法采用两阶段计算方案：第一阶段利用紧凑的低比特数据集快速识别最相关的条目，第二阶段仅在该剪枝后的子集上执行全精度计算，从而最小化计算开销。此外，AccelES 引入了创新的矩阵表示 Ultra-CSR 与 Random-CSR，可优化内存带宽利用率。实验结果表明，在受控条件下 AccelES 的性能分别超过最先进的 FPGA、GPU 和 CPU 方案 3.4 倍、2.5 倍和 153.3 倍。这些进展不仅提升了处理速度，也显著改善了推荐系统中的实时性能，使 AccelES 成为 Top-K 稀疏矩阵向量乘领域的一项关键贡献。
