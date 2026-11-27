---
title: "AQPIM: Breaking the PIM Capacity Wall for LLMs with In-Memory Activation Quantization"
description: "HPCA 2026 · Efficient LLM Inference Techniques"
tags:
  - "HPCA2026"
  - "Efficient LLM Inference Techniques"
---

# AQPIM: Breaking the PIM Capacity Wall for LLMs with In-Memory Activation Quantization

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Efficient LLM Inference Techniques。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Efficient LLM Inference Techniques</p>
</div>

**论文链接**：
**作者**：Kosuke Matsushima Institute of Science Tokyo , Yasuyuki Okoshi Institute of Science Tokyo , Masato Motomura Institute of Science Tokyo , Daichi Fujiki Institute of Science Tokyo
**会议**：HPCA 2026

---

## 中文标题

AQPIM：以存内激活量化打破 LLM 的 PIM 容量墙

## 英文摘要

Processing-in-Memory (PIM) architectures offer a promising solution to the memory bottlenecks in data-intensive machine learning, yet often overlook the growing challenge of activation memory footprint. Conventional PIM approaches struggle with massive KV cache sizes generated in long-context scenarios by Transformer-based models, frequently exceeding PIM’s limited memory capacity, while techniques like sparse attention can conflict with PIM’s need for data locality. Existing PIM approaches and quantization methods are often insufficient or poorly suited for leveraging the unique characteristics of activations. This work identifies an opportunity for PIM-specialized activation quantization to enhance bandwidth and compute efficiency. We explore clustering-based vector quantization approaches, which align well with activation characteristics and PIM’s internal bandwidth capabilities. Building on this, we introduce AQPIM, a novel PIM-aware activation quantization framework based on Product Quantization (PQ), optimizing it for modern Large Language Models (LLMs). By performing quantization directly within memory, AQPIM leverages PIM’s high internal bandwidth and enables direct computation on compressed data, significantly reducing both memory footprint and computational overhead for attention computation. AQPIM addresses PQ’s accuracy challenges by introducing several algorithmic optimizations. Evaluations demonstrate that AQPIM achieves significant performance improvements, drastically reducing of GPU-CPU communication that can account for 90∼98.5% of decoding latency, together with 3.4× speedup over a SOTA PIM approach.

## 中文摘要

存内处理（PIM）架构为数据密集型机器学习的内存瓶颈提供了有前景的方案，却常常忽视日益增长的激活内存占用这一挑战。传统 PIM 方法难以应对基于 Transformer 的模型在长上下文场景中产生的大规模 KV 缓存，其规模经常超出 PIM 有限的存储容量，而稀疏注意力等技术又与 PIM 对数据局部性的需求相冲突。现有 PIM 方法与量化方法往往不足以利用激活的独特特征。本文发现了一个面向 PIM 的专用激活量化机会，可提升带宽与计算效率。我们探索了基于聚类的向量量化方法，它与激活特征以及 PIM 的内部带宽能力高度契合。在此基础上，我们提出 AQPIM，一个基于乘积量化（PQ）的 PIM 感知激活量化框架，并针对现代大语言模型进行优化。通过在内存内部直接完成量化，AQPIM 利用 PIM 的高内部带宽并支持在压缩数据上直接计算，显著降低注意力计算的内存占用与计算开销。AQPIM 通过多项算法优化解决了 PQ 的精度挑战。评估表明，AQPIM 带来显著的性能提升，大幅减少了可占解码时延 90∼98.5% 的 GPU-CPU 通信，并相对最先进的 PIM 方法实现 3.4× 加速。
