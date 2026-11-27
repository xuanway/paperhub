---
title: "LILo: Harnessing the On-chip Accelerators in Intel CPUs for Compressed LLM Inference Acceleration"
description: "HPCA 2026 · LLM Systems and Microarchitecture Tools"
tags:
  - "HPCA2026"
  - "LLM Systems and Microarchitecture Tools"
---

# LILo: Harnessing the On-chip Accelerators in Intel CPUs for Compressed LLM Inference Acceleration

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: LLM Systems and Microarchitecture Tools。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · LLM Systems and Microarchitecture Tools</p>
</div>

**论文链接**：
**作者**：Hyungyo Kim UIUC , Qirong Xia UIUC , Jinghan Huang UIUC , Nachuan Wang UIUC , Jung Ho Ahn Seoul National University , Younjoo Lee Seoul National University , Wajdi K Feghali Intel , Ren Wang Intel Labs , Nam Sung Kim UIUC
**会议**：HPCA 2026

---

## 中文标题

LILo：利用 Intel CPU 片内加速器加速压缩 LLM 推理

## 英文摘要

The ever-growing sizes of large language models (LLMs) introduce significant infrastructure challenges due to their immense memory capacity demands. While the de facto approach has been to deploy multiple high-end GPUs, each with a limited memory capacity, the prohibitive cost of such systems has become a major barrier to the widespread deployment of frontier LLMs. As a result, CPU-based inference has become an appealing and cost-efficient alternative, since a CPU can offer an order of magnitude larger memory capacity at a fraction of the cost while providing competitive throughput for matrix-vector multiplication with the latest Advanced Matrix Extensions (AMX). It not only broadens accessibility for users without multi-GPU setups but also enables hyperscalers to leverage underutilized CPU servers to accommodate temporarily surging inference demand. Nevertheless, even CPU’s large memory capacity has become insufficient to serve LLMs with hundreds of billions of parameters. Under the memory capacity constraint, we may offload parameters to storage devices and fetch them on demand, but doing so significantly degrades inference performance due to the high latency and low bandwidth of storage devices. To address this challenge, we propose LILO, an LLM inference framework that leverages In-memory Analytics Accelerator (IAA) in the latest Intel CPUs, to accelerate inference under memory capacity constraints. By storing model parameters in a compressed format and decompressing them on demand using IAA, LILO enables significantly reduced storage access during inference under memory capacity constraints while preserving the model accuracy and behavior. LILO orchestrates the concurrent execution of on-chip accelerators, i.e., IAA, Advanced Vector Extensions (AVX), and AMX, to facilitate high-throughput decompression alongside inference computation. Furthermore, LILO implements selective compression, a Mixture-of-Expert (MoE)-aware optimization that reduces the decompression overhead by up to 1.9×. We demonstrate that LILO reduces inference latency by up to 4.9× and 4.3× for Llama3-405B and DeepSeek-R1, respectively, under memory capacity constraints compared to the baseline inference solely relying on storage-offloading without compression.

## 中文摘要

大语言模型（LLM）规模持续增长，巨大的内存容量需求带来显著的基础设施挑战。通常做法是部署多块内存容量有限的高端 GPU，但其高昂成本已成为前沿 LLM 广泛部署的主要障碍。于是基于 CPU 的推理成为有吸引力且高性价比的替代方案：CPU 能以低得多的成本提供高一个数量级的存储容量，并借助最新的高级矩阵扩展（AMX）为矩阵—向量乘提供有竞争力的吞吐。这既让没有多 GPU 的用户更易使用，也让超大规模厂商能利用空闲 CPU 服务器承接临时激增的推理需求。然而即便是 CPU 的大容量内存，也不足以服务数千亿参数的 LLM。在容量受限时可把参数卸载到存储并按需取回，但存储的高时延与低带宽会严重损害推理性能。为此我们提出 LILO，一个利用最新 Intel CPU 中内存分析加速器（IAA）的 LLM 推理框架。LILO 以压缩格式存放参数并用 IAA 按需解压，在保持模型精度与行为的同时显著减少推理时的存储访问；它协同调度 IAA、高级向量扩展（AVX）与 AMX 等片上加速器并发执行，在推理计算的同时实现高吞吐解压。此外，LILO 提出选择性压缩这一感知混合专家（MoE）的优化，将解压开销最多降低 1.9 倍。实验表明，在内存容量受限下，相比仅依赖存储卸载而不压缩的基线，LILO 对 Llama3-405B 与 DeepSeek-R1 的推理时延分别最多降低 4.9 倍与 4.3 倍。
