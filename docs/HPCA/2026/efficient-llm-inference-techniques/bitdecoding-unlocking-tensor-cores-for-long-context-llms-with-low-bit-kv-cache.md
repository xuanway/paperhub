---
title: "BitDecoding: Unlocking Tensor Cores for Long-Context LLMs with Low-Bit KV Cache"
description: "HPCA 2026 · Efficient LLM Inference Techniques"
tags:
  - "HPCA2026"
  - "Efficient LLM Inference Techniques"
---

# BitDecoding: Unlocking Tensor Cores for Long-Context LLMs with Low-Bit KV Cache

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Efficient LLM Inference Techniques。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Efficient LLM Inference Techniques</p>
</div>

**论文链接**：
**作者**：Dayou Du University of Edinburgh , Shijie Cao Microsoft Research , Jianyi Cheng University of Edinburgh, UK , Luo Mai University of Edinburgh , Ting Cao Institute for AI Industry Research (AIR), Tsinghua University , Mao Yang Microsoft Research
**会议**：HPCA 2026

---

## 中文标题

BitDecoding：为低比特 KV 缓存的长上下文 LLM 解锁张量核心

## 英文摘要

The rise of long-context Large Language Models (LLMs) amplifies memory and bandwidth demands during autoregressive decoding, as the Key–Value (KV) cache grows with each generated token. Low-bit KV-cache quantization (e.g., 4-bit or 2-bit) can reduce memory footprint while preserving accuracy, but existing systems suffer from slow decoding due to their exclusive reliance on CUDA cores, neglecting Tensor Cores—the primary source of compute on modern GPUs. We present BitDecoding, a new long-context LLMs inference system with low-bit KV cache. BitDecoding enables efficient low-bit KV cache decoding by cooperatively leveraging CUDA Cores and Tensor Cores. It introduces methods for automatically inducing optimized layouts to exploit Tensor Cores, along with novel warp-level parallelization strategies for dequantization. For unified system support, BitDecoding includes a query transformation module supporting diverse attention variants, a quantization kernel to support both tensor-wise and channel-wise scaling used in various quantization algorithms with high performance, and a dequantization kernel with a software-defined pipeline to coordinate CUDA and Tensor Cores execution for mix-precision operations. In addition, architecture-specific optimizations leverage Hopper’s warpgroup tensor instructions and Blackwell’s native low-precision tensor formats to maximize decoding throughput on the latest GPU generations. Evaluated on Blackwell, Hopper, Ada, and Ampere architectures, BitDecoding attains on average a 7.5× decoding speedup over FP16 FlashDecoding-v2, and further reaches up to 8.6× with native MXFP4 formats on Blackwell, while surpassing the state-of-the-art low-bit system QServe by up to 4.3×. On LLaMA-3.1-8B with a 128K context, BitDecoding reduces single-batch decoding latency by 3×, demonstrating substantial improvements for long-context generation, and is open sourced at https://github.com/OpenBitSys/BitDecoding.

## 中文摘要

长上下文大语言模型（LLM）的兴起放大了自回归解码时的内存与带宽需求，因为键值（KV）缓存随每生成一个 token 而增长。低比特 KV 缓存量化（如 4 比特或 2 比特）可在保持精度的同时减少内存占用，但现有系统因仅依赖 CUDA 核心而解码缓慢，忽视了现代 GPU 上主要的算力来源张量核心。我们提出 BitDecoding，一个采用低比特 KV 缓存的长上下文 LLM 推理新系统。BitDecoding 通过协同利用 CUDA 核心与张量核心，高效实现低比特 KV 缓存解码。它引入了自动推导优化布局以利用张量核心的方法，以及用于反量化的新型 warp 级并行策略。为提供统一的系统支持，BitDecoding 包含支持多种注意力变体的查询变换模块、支持逐张量与逐通道缩放且高性能的量化内核，以及带软件定义流水线、协调 CUDA 核心与张量核心执行混合精度运算的反量化内核。此外，架构相关优化利用 Hopper 的 warpgroup 张量指令与 Blackwell 的原生低精度张量格式，在最新几代 GPU 上最大化解码吞吐。在 Blackwell、Hopper、Ada 与 Ampere 架构上的评估表明，BitDecoding 平均比 FP16 FlashDecoding-v2 取得 7.5× 解码加速，在 Blackwell 上使用原生 MXFP4 格式可达 8.6×，同时比最先进的低比特系统 QServe 高出最多 4.3×。在 128K 上下文的 LLaMA-3.1-8B 上，BitDecoding 将单批解码时延降低 3×，展示了对长上下文生成的显著改进，并已在 https://github.com/OpenBitSys/BitDecoding 开源。
