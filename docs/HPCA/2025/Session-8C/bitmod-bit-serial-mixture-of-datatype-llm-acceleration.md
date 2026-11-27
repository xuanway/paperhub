---
title: "BitMoD: Bit-serial Mixture-of-Datatype LLM Acceleration"
description: "HPCA 2025 · Viva Las Learning Models"
tags:
  - "HPCA2025"
  - "Viva Las Learning Models"
---

# BitMoD: Bit-serial Mixture-of-Datatype LLM Acceleration

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Viva Las Learning Models。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Viva Las Learning Models</p>
</div>

**论文链接**：
**作者**：Yuzong Chen (Cornell University), Ahmed F. AbouElhamayed (Cornell University), Xilai Dai (Cornell University), Yang Wang (Microsoft Research), Marta Andronic (Imperial College London), George A. Constantinides (Imperial College London), Mohamed S. Abdelfattah (Cornell University)
**会议**：HPCA 2025

---

## 中文标题

BitMoD：位串行混合数据类型的 LLM 加速

## 英文摘要

Large language models (LLMs) have demonstrated remarkable performance across various machine learning tasks. Yet the substantial memory footprint of LLMs significantly hinders their deployment. In this paper, we improve the accessibility of LLMs through BitMoD1, an algorithm-hardware co-design solution that enables efficient LLM acceleration at low weight precision. On the algorithm side, BitMoD introduces fine-grained data type adaptation that uses a different numerical data type to quantize a group of (e.g., 128) weights. Through the careful design of these new data types, BitMoD is able to quantize LLM weights to very low precision (e.g., 4 bits and 3 bits) while maintaining high accuracy. On the hardware side, BitMoD employs a bit-serial processing element to easily support multiple numerical precisions and data types; our hardware design includes two key innovations: First, it employs a unified representation to process different weight data types, thus reducing the hardware cost. Second, it adopts a bit-serial dequantization unit to rescale the per-group partial sum with minimal hardware overhead. Our evaluation on six representative LLMs demonstrates that BitMoD significantly outperforms state-of-the-art LLM quantization and acceleration methods. For discriminative tasks, BitMoD can quantize LLM weights to 4-bit with < 0.5% accuracy loss on average. For generative tasks, BitMoD is able to quantize LLM weights to 3-bit while achieving better perplexity than prior LLM quantization scheme. Combining the superior model performance with an efficient accelerator design, BitMoD achieves an average of 1.69× and 1.48× speedups compared to prior LLM accelerators ANT and OliVe, respectively.

## 中文摘要

大语言模型（LLM）在各类机器学习任务中都展现出卓越性能，然而其庞大的内存占用严重阻碍了部署。本文通过 BitMoD 提升 LLM 的可及性，这是一种算法与硬件协同设计的方案，可在低权重精度下实现高效的 LLM 加速。算法层面，BitMoD 引入细粒度数据类型自适应，用不同的数值数据类型量化一组（例如 128 个）权重。通过精心设计这些新数据类型，BitMoD 能把 LLM 权重量化到极低精度（例如 4 比特和 3 比特），同时保持高精度。硬件层面，BitMoD 采用位串行处理单元，可轻松支持多种数值精度与数据类型；其硬件设计包含两项关键创新：一是采用统一表示处理不同权重数据类型，从而降低硬件开销；二是采用位串行反量化单元，以极小硬件开销对每组部分和重新缩放。在六个代表性 LLM 上的评估表明，BitMoD 显著优于最先进的 LLM 量化与加速方法。对于判别式任务，BitMoD 可把 LLM 权重量化到 4 比特，平均精度损失小于 0.5%。对于生成式任务，BitMoD 能把 LLM 权重量化到 3 比特，同时取得比先前 LLM 量化方案更好的困惑度。凭借优异的模型性能与高效的加速器设计，BitMoD 相比先前 LLM 加速器 ANT 和 OliVe 分别平均实现 1.69 倍和 1.48 倍加速比。
