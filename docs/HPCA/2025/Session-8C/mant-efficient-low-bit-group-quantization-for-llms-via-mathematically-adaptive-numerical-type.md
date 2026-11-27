---
title: "MANT: Efficient Low-bit Group Quantization for LLMs via Mathematically Adaptive Numerical Type"
description: "HPCA 2025 · Viva Las Learning Models"
tags:
  - "HPCA2025"
  - "Viva Las Learning Models"
---

# MANT: Efficient Low-bit Group Quantization for LLMs via Mathematically Adaptive Numerical Type

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Viva Las Learning Models。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Viva Las Learning Models</p>
</div>

**论文链接**：
**作者**：Weiming Hu (Shanghai Jiao Tong University), Haoyan Zhang (Shanghai Jiao Tong University), Cong Guo (Department of Computer Science and Engineering, Shanghai Jiao Tong University), Yu Feng (Shanghai Jiao Tong University), Renyang Guan (Shanghai Jiao Tong University), Zhendong Hua (Shanghai Jiao Tong University), Zihan Liu (Shanghai Jiao Tong University), Yue Guan (Shanghai Jiao Tong University), Minyi Guo (Shanghai Jiao Tong University), Jingwen Leng (Shanghai Jiao Tong University)
**会议**：HPCA 2025

---

## 中文标题

MANT：通过数学自适应数值类型实现 LLM 高效低位组量化

## 英文摘要

Large language models (LLMs) are one of the most important killer computer applications. The recent algorithmic advancement proposes a fine-grained group-wise quantization for LLMs, which treats a small set (e.g., 64) of values in a tensor as a compression unit. It effectively preserves the model accuracy without retraining, and has become the standard approach to efficiently deploy LLMs. On the other hand, there are works that propose various adaptive data types to better adapt to different distributions and further reduce the required bit length for LLMs. In this work, our detailed analysis unveils a key finding that while different tensors exhibit similar distributions, small groups can have markedly different distributions. As such, the group-level diversity requires a new level of adaptivity for which existing adaptive data types fail to provide. In this paper, we propose MANT, a mathematically adaptive numeric type, featuring a more flexible encoding paradigm with a wider range of data distribution and more efficient decoding-computation fusion mechanism to address these challenges. Based on MANT, we develop a supporting framework to assign the appropriate data type for each group adaptively. Meanwhile, the dynamically generated Key-Value (KV) caches in LLMs introduce further complexity for real-time quantization. To tackle this, we propose an efficient real-time quantization mechanism. Besides, we implement a specific processing element (PE) to efficiently support MANT and incorporate a real-time quantization unit. By integrating these components into a systolic array, MANT unifies the group-wise weight and KV cache quantization and addresses the associated challenges. Our evaluation shows achieving, on average, 2.99× (up to 4.46×) speedup and 2.81× (up to 4.10×) energy reduction to the state-of-the-art LLM accelerator.

## 中文摘要

大语言模型（LLM）是最重要的杀手级计算机应用之一。近期算法进展提出面向 LLM 的细粒度分组量化，它将张量中一小组（例如 64 个）数值视为一个压缩单元。该方法无需重新训练即可有效保持模型精度，已成为高效部署 LLM 的标准方法。另一方面，一些工作提出了各种自适应数据类型，以更好地适应不同分布并进一步降低 LLM 所需的位长。本工作的详细分析揭示了一个关键发现：尽管不同张量呈现相似的分布，但小的分组可能具有显著不同的分布。因此，分组级多样性需要新层次的自适应性，而现有自适应数据类型无法提供。本文提出 MANT，一种数学自适应的数值类型，它具有更灵活的编码范式以覆盖更广的数据分布，并采用更高效的解码与计算融合机制应对这些挑战。基于 MANT，我们开发了一个支撑框架，为每个分组自适应地分配合适的数据类型。同时，LLM 中动态生成的键值（KV）缓存为实时量化带来了额外复杂性。为此，我们提出一种高效的实时量化机制。此外，我们实现了一个专用处理单元（PE）以高效支持 MANT，并集成了实时量化单元。通过将这些组件集成到脉动阵列中，MANT 统一了分组级权重与 KV 缓存量化并解决了相关挑战。评估表明，相比最先进的 LLM 加速器，平均实现 2.99 倍（最高 4.46 倍）加速与 2.81 倍（最高 4.10 倍）能耗降低。
