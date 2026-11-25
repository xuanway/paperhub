---
title: "TACO: Efficient Communication Compression of Intermediate Tensors for Scalable Tensor-Parallel LLM Training"
description: "HPDC 2026 · Session 3 — MoE Systems & Distributed LLM Training"
tags:
  - "HPDC2026"
  - "Session 3"
  - "MoE Systems & Distributed LLM Training"
---

# TACO: Efficient Communication Compression of Intermediate Tensors for Scalable Tensor-Parallel LLM Training

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 3 — MoE Systems & Distributed LLM Training（2026年7月14日 13:30–14:30 · Session Chair：Peter Dinda）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 3</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807584)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#LiuLTLLYHWZTT26](https://dblp.org/db/conf/hpdc/hpdc2026.html#LiuLTLLYHWZTT26)

**作者**：Man Liu, Xingchen Liu, Xingjian Tian, Bing Lu, Shengkai Lyu, Shengquan Yin, Wenjing Huang, Zheng Wei, Hairui Zhao, Guangming Tan, Dingwen Tao

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 3 — MoE Systems & Distributed LLM Training（2026年7月14日 13:30–14:30 · Session Chair：Peter Dinda）

---

## 英文摘要

Handling communication overhead in large-scale tensor-parallel training remains a critical challenge due to the dense, near-zero distributions of intermediate tensors, which exacerbate errors under frequent communication and introduce significant computational overhead during compression. To this end, we propose TACO (Tensor-parallel Adaptive COmmunication compression), a robust FP8-based framework for compressing TP intermediate tensors. First, we employ a data-driven reshaping strategy combined with an Adaptive Scale–Hadamard Transform to enable high-fidelity FP8 quantization, while its Dual-Scale Quantization mechanism ensures numerical stability throughout training. Second, we design a highly fused compression operator to reduce memory traffic and kernel launch overhead, allowing efficient overlap with communication. Finally, we integrate TACO with existing state-of-the-art methods for Data and Pipeline Parallelism to develop a compression-enabled 3Dparallel training framework. Detailed experiments on GPT models and Qwen model demonstrate up to 1.87× end-to-end throughput improvement while maintaining near-lossless accuracy, validating the effectiveness and efficiency of TACO in large-scale training.

## 中文摘要

由于中间张量呈现稠密且接近零的分布，在大规模张量并行训练中处理通信开销仍是一项关键挑战：这种分布会加剧频繁通信下的误差，并在压缩过程中引入显著的计算开销。为此，我们提出 TACO（张量并行自适应通信压缩），一个基于 FP8、用于压缩张量并行（TP）中间张量的鲁棒框架。首先，我们采用数据驱动的重整形策略，结合自适应 Scale–Hadamard 变换，实现高保真 FP8 量化，其双尺度量化机制在整个训练过程中保证数值稳定性。其次，我们设计了一个高度融合的压缩算子，以减少内存流量与核启动开销，使其能够与通信高效重叠。最后，我们将 TACO 与现有最先进的数据并行和流水线并行方法集成，构建了一个支持压缩的三维并行训练框架。在 GPT 与 Qwen 模型上的详细实验表明，在保持近乎无损精度的同时，端到端吞吐最高提升 1.87 倍，验证了 TACO 在大规模训练中的有效性与高效性。

## 英文关键词

Tensor parallelism, quantization, distributed training, communication compression, large language model.

## 中文关键词

张量并行，量化，分布式训练，通信压缩，大语言模型。

---

[← 返回 Session 3 — MoE Systems & Distributed LLM Training](index.md)
