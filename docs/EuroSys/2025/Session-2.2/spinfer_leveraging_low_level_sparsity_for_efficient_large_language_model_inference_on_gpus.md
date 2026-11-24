---
title: "SpInfer: Leveraging Low-Level Sparsity for Efficient Large Language Model Inference on GPUs"
description: "EuroSys 2025 · LLM Serving · Ruibo FAN (Data Science and Analytics Thrust, HKUST(GZ)), Xiangrui YU (Data Scie"
tags:
  - "EuroSys2025"
  - "LLM Serving"
---

# SpInfer: Leveraging Low-Level Sparsity for Efficient Large Language Model Inference on GPUs

**中文标题：** 利用底层稀疏性实现 GPU 上的高效大语言模型推理

**所属 Session：** [Session 2.2: LLM Serving](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：LLM Serving。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · LLM Serving</p>
</div>

**作者**：Ruibo FAN (Data Science and Analytics Thrust, HKUST(GZ)), Xiangrui YU (Data Science and Analytics Thrust, HKUST(GZ)), Peijie Dong (Data Science and Analytics Thrust, HKUST(GZ)), Zeyu Li (Data Science and Analytics Thrust, HKUST(GZ)), Gu Gong (Data Science and Analytics Thrust, HKUST(GZ)), QIANG WANG (Harbin Institute of Technology (Shenzhen)), Wei Wang (Hong Kong University of Science and Technology), Xiaowen Chu (Data Science and Analytics Thrust, HKUST(GZ))

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717481)

**获奖：** 最佳论文（秋季投稿）（[官方获奖名单](https://2025.eurosys.org/awards.html)）

## 英文摘要

Large Language Models (LLMs) have demonstrated remarkable capabilities, but their immense scale poses significant challenges in terms of both memory and computational costs. While unstructured pruning offers promising solutions by introducing sparsity to reduce resource requirements, realizing its benefits in LLM inference remains elusive. This is primarily due to the storage overhead of indexing non-zero elements and the inefficiency of sparse matrix multiplication (SpMM) kernels at low sparsity levels (around 50%). In this paper, we present SpInfer, a high-performance framework tailored for sparsified LLM inference on GPUs. SpInfer introduces Tensor-Core-Aware Bitmap Encoding (TCA-BME), a novel sparse format that minimizes indexing overhead by leveraging efficient bitmap-based indexing, optimized for GPU Tensor Core architectures. Furthermore, SpInfer integrates an optimized SpMM kernel with Shared Memory Bitmap Decoding (SMBD) and asynchronous pipeline design to enhance computational efficiency. Experimental results show that SpInfer significantly outperforms state-of-the-art SpMM implementations (up to 2.14× and 2.27× over Flash-LLM and SparTA, respectively) across a range of sparsity levels (30% to 70%), with substantial improvements in both memory efficiency and end-to-end inference speed (up to 1.58×). SpInfer outperforms highly optimized cuBLAS at sparsity levels as low as 30%, marking the first effective translation of unstructured pruning’s theoretical advantages into practical performance gains for LLM inference.

## 中文摘要

大语言模型（LLM）已展现出卓越的能力，但其巨大规模在内存与计算开销两方面都带来了重大挑战。非结构化剪枝通过引入稀疏性来降低资源需求，提供了有前景的解决方案，但在 LLM 推理中兑现其收益仍非易事。这主要归因于非零元素索引的存储开销，以及稀疏矩阵乘（SpMM）内核在低稀疏度（约 50%）下的低效。本文提出 SpInfer，一个面向 GPU 上稀疏化 LLM 推理的高性能框架。SpInfer 引入张量核感知位图编码（TCA-BME），这是一种新颖的稀疏格式，通过利用高效的位图索引来最小化索引开销，并针对 GPU 张量核架构进行了优化。此外，SpInfer 集成了优化的 SpMM 内核，配备共享内存位图解码（SMBD）和异步流水线设计，以提升计算效率。实验结果表明，在 30% 至 70% 的一系列稀疏度下，SpInfer 显著优于最先进的 SpMM 实现（相比 Flash-LLM 和 SparTA 分别最高达 2.14 倍和 2.27 倍），并在内存效率和端到端推理速度上均有显著提升（最高 1.58 倍）。在低至 30% 的稀疏度下，SpInfer 即优于高度优化的 cuBLAS，首次将非结构化剪枝的理论优势有效转化为 LLM 推理的实际性能收益。

**英文关键词：** Unstructured Pruning, SpMM, Sparse, LLM Inference, GPU, Tensor Core

**中文关键词：** 非结构化剪枝、SpMM、稀疏、LLM 推理、GPU、张量核

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
