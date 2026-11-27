---
title: "VQ-LLM: High-performance Code Generation for Vector Quantization Augmented LLM Inference"
description: "HPCA 2025 · Viva Las Learning Models"
tags:
  - "HPCA2025"
  - "Viva Las Learning Models"
---

# VQ-LLM: High-performance Code Generation for Vector Quantization Augmented LLM Inference

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Viva Las Learning Models。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Viva Las Learning Models</p>
</div>

**论文链接**：
**作者**：Zihan Liu (Shanghai Jiao Tong University), Xinhao Luo (Shanghai Jiao Tong University), Junxian Guo (Shanghai Jiao Tong University), Wentao Ni (Shanghai Jiao Tong University), Yangjie Zhou (Shanghai Jiao Tong University), Yue Guan (Shanghai Jiao Tong University), Cong Guo (Shanghai Jiao Tong University), Weihao Cui (Shanghai Jiao Tong University), Yu Feng (Shanghai Jiao Tong University), Minyi Guo (Shanghai Jiao Tong University), Yuhao Zhu (University of Rochester), Minjia Zhang (University of Illinois at Urbana-Champaign), Jingwen Leng (Shanghai Jiao Tong University), Chen Jin (Magik Compute)
**会议**：HPCA 2025

---

## 中文标题

VQ-LLM：面向向量量化增强 LLM 推理的高性能代码生成

## 英文摘要

Vector quantization (VQ), which treats a vector as a compression unit, gains increasing research interests for its potential to accelerate large language models (LLMs). Compared to conventional element-wise quantization methods, VQ algorithms can compress weight and KV cache tensors in LLMs with a greater ratio while maintaining the high model accuracy. However, translating a VQ algorithm’s memory reduction into the actual latency improvement is challenging. We profile and analyze the current approach of integrating VQ into computation kernels and show that its major inefficiency lies in the poor access efficiency of codebooks in VQ algorithms and uncoordinated computation dataflow. Meanwhile, the diversity of VQ algorithms (e.g., different vector sizes and entry counts) and LLMs’ computation kernels (e.g matrix-matrix/vector multiplication and attention computation) makes it impractical to manually craft efficient kernel implementations for each specific case. In this work, we design and implement VQ-LLM, an efficient fused VQ kernel generation framework. We first introduce a software abstraction called codebook cache to optimize codebook access efficiency and support the integration of VQ with various computations. The codebook cache adaptively stores different entries across the GPU’s memory hierarchy, including off-chip global memory, on-chip shared memory, and registers. Centered around the codebook cache, we design an efficient computation engine that optimizes memory traffic during computations involving codebooks. This compute engine adopts the codebook-centric dataflow and fusion optimizations. Additionally, we provide adaptive heuristics to tailor parameter selection in our optimizations to diverse VQ configurations. Our optimizations achieve the latency reduction of 64.36% to 99.1% compared to existing open-source implementations. A final comparison with state-of-the-art element-wise quantization methods like AWQ and QoQ shows that our VQ-LLM is practically viable, achieving latencies close or even better latencies to those at equivalent bitwidths, potentially offering greater accuracy.

## 中文摘要

向量量化（VQ）把向量视为压缩单元，因其加速大语言模型（LLM）的潜力而日益受到关注。与传统逐元素量化相比，VQ 能以更高的压缩比压缩 LLM 的权重和 KV 缓存张量，同时保持较高的模型精度。然而，把 VQ 算法的内存节省转化为实际的时延改善并非易事。我们剖析了当前把 VQ 集成到计算内核的方法，发现其低效主要源于 VQ 算法中码本访存效率低下以及计算数据流不协调。同时，VQ 算法（如不同向量大小和条目数量）与 LLM 计算内核（如矩阵-矩阵/向量乘法和注意力计算）的多样性，使手工编写各情况下的高效内核不现实。本文设计并实现 VQ-LLM，一个高效融合式 VQ 内核生成框架。我们首先引入称为码本缓存的软件抽象，以优化码本访存效率并支持 VQ 与各类计算集成。码本缓存把不同条目自适应地存放在 GPU 存储层次中，包括片外全局内存、片上共享内存和寄存器。以码本缓存为中心，我们设计了高效计算引擎，采用以码本为中心的数据流与融合优化减少涉及码本计算的内存流量。此外，我们提供自适应启发式方法，使参数选择适配不同 VQ 配置。与现有开源实现相比，我们的优化把时延降低 64.36% 到 99.1%。最后，与 AWQ、QoQ 等最先进的逐元素量化方法相比，VQ-LLM 具有实际可行性：其时延接近甚至优于同等比特宽度下的时延，并可能提供更高的精度。
