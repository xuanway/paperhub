---
title: "PADE: A Predictor-Free Sparse Attention Accelerator via Unified Execution and Stage Fusion"
description: "HPCA 2026 · Efficient LLM Inference Techniques"
tags:
  - "HPCA2026"
  - "Efficient LLM Inference Techniques"
---

# PADE: A Predictor-Free Sparse Attention Accelerator via Unified Execution and Stage Fusion

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Efficient LLM Inference Techniques。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Efficient LLM Inference Techniques</p>
</div>

**论文链接**：
**作者**：Huizheng Wang Tsinghua University , Hongbin Wang Tsinghua University , Zichuan Wang Tsinghua University , Zhiheng Yue Tsinghua University , Yang Wang Tsinghua University , Chao Li Shanghai Jiao Tong University , Yang Hu Tsinghua University , Shouyi Yin Tsinghua University
**会议**：HPCA 2026

---

## 中文标题

PADE：通过统一执行与阶段融合实现无需预测器的稀疏注意力加速器

## 英文摘要

Attention-based models have revolutionized AI, but the quadratic cost of self-attention incurs severe computational and memory overhead. Sparse attention methods alleviate this by skipping low-relevance token pairs. However, current approaches lack practicality due to the heavy expense of added sparsity predictor, which severely drops their hardware efficiency. This paper advances the state-of-the-art (SOTA) by proposing a bit-serial enable stage-fusion (BSF) mechanism, which eliminates the need for a separate predictor. However, it faces key challenges: 1) Inaccurate bit-sliced sparsity speculation leads to incorrect pruning; 2) Hardware under-utilization due to fine-grained and imbalanced bit-level workloads. 3) Tiling difficulty caused by the row-wise dependency in sparsity pruning criteria. We propose PADE, a predictor-free algorithm-hardware co-design for dynamic sparse attention acceleration. PADE features three key innovations: 1) Bit-wise uncertainty interval-enabled guard filtering (BUI-GF) strategy to accurately identify trivial tokens during each bit round; 2) Bidirectional sparsity-based out-of-order execution (BS-OOE) to improve hardware utilization; 3) Interleaving-based sparsity-tiled attention (ISTA) to reduce both I/O and computational complexity. These techniques, combined with custom accelerator designs, enable practical sparsity acceleration without relying on an added sparsity predictor. Extensive experiments on 22 benchmarks show that PADE achieves 7.43× speed up and 31.1× higher energy efficiency than Nvidia H100 GPU. Compared to SOTA accelerators, PADE achieves 5.1×, 4.3× and 3.4× energy saving than Sanger, DOTA and SOFA.

## 中文摘要

基于注意力的模型革新了人工智能，但自注意力的二次方开销带来严重的计算与内存开销。稀疏注意力方法通过跳过低相关性的 token 对来缓解这一问题。然而，现有方法因额外稀疏预测器的高昂代价而缺乏实用性，严重降低了硬件效率。本文提出比特串行使能阶段融合（BSF）机制来推进最先进水平（SOTA），该机制无需单独的预测器。但它面临关键挑战：1）比特切片稀疏推测不准确导致错误剪枝；2）细粒度且不均衡的比特级负载造成硬件利用率不足；3）稀疏剪枝准则中的行间依赖造成分块困难。我们提出 PADE，一个面向动态稀疏注意力加速的无需预测器的算法—硬件协同设计。PADE 有三项关键创新：1）基于比特不确定区间的保护过滤（BUI-GF）策略，在每个比特轮次中准确识别平凡 token；2）基于双向稀疏性的乱序执行（BS-OOE）以提升硬件利用率；3）基于交织的稀疏分块注意力（ISTA）以同时降低 I/O 与计算复杂度。这些技术与定制加速器设计相结合，无需额外稀疏预测器即可实现实用的稀疏加速。在 22 个基准上的大量实验表明，PADE 相较 Nvidia H100 GPU 实现 7.43× 加速与 31.1× 能效提升。与 SOTA 加速器相比，PADE 比 Sanger、DOTA 与 SOFA 分别节能 5.1×、4.3× 与 3.4×。
