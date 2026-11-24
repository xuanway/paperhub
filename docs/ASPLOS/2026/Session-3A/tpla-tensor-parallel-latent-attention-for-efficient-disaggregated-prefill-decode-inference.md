---
title: "TPLA: Tensor Parallel Latent Attention for Efficient Disaggregated Prefill & Decode Inference"
description: "ASPLOS 2026 · Session 3A · TPLA：面向高效分离式 Prefill 与 Decode 推理的张量并行潜在注意力"
tags:
  - "ASPLOS2026"
  - "Session 3A"
  - "LLM Attention & KV Cache"
---

# TPLA: Tensor Parallel Latent Attention for Efficient Disaggregated Prefill & Decode Inference

**中文标题：** TPLA：面向高效分离式 Prefill 与 Decode 推理的张量并行潜在注意力

**所属 Session：** [Session 3A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Xiaojuan Tang (Peking University), Fanxu Meng (Peking University), Pingzhi Tang (Peking University), Yuxuan Wang (Peking University), Di Yin (Tencent YouTu Lab), Xing Sun (Tencent YouTu Lab), Muhan Zhang (Peking University)

**单位：** Peking University；Tencent YouTu Lab

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790237) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Multi-Head Latent Attention (MLA), introduced in DeepSeek-V2, compresses key–value states into a low-rank latent vector cKV, caching only this vector to reduce memory. In tensor parallelism (TP), however, attention heads are computed across multiple devices, and each device must load the full cKV, eroding the advantage of MLA over Grouped Query Attention (GQA). We present TPLA, a scheme that partitions both the latent representation and each head's input dimension across devices, performs attention independently on each shard, and aggregates the results with an all-reduce. Unlike GLA, every attention head in TPLA still attends to the full latent space, preserving MLA's representational capacity while reducing the per-device KV cache. To make TPLA drop-in compatible with MLA checkpoints, we further derive orthogonal reparameterizations of RMSNorm and softmax—instantiated with Hadamard and PCA transforms—that mitigate crossshard discrepancies when slicing latent vectors across devices. Finally, we introduce a prefill-decode separation scheme that keeps the MLA form during compute-bound prefilling and switches to TPLA during memory-bound decoding, minimizing conversion-induced error. By reducing the per-device KV cache for DeepSeek-V3 and Kimi-K2, we achieve 1.79× and 1.93× speedups respectively, at a 32Ktoken context length while maintaining accuracy on commonsense and LongBench benchmarks. TPLA can be further implemented on top of FlashAttention-3, enabling practical end-to-end acceleration.

## 中文摘要

DeepSeek-V2 中提出的多头潜在注意力（MLA）将键值状态压缩为低秩潜在向量 cKV，仅缓存该向量以减少内存占用。然而在张量并行（TP）下，注意力头跨多个设备计算，每个设备都必须加载完整的 cKV，从而侵蚀了 MLA 相对于分组查询注意力（GQA）的优势。我们提出 TPLA，该方案将潜在表示与每个头的输入维度同时跨设备切分，在每个分片上独立执行注意力，并通过 all-reduce 聚合结果。与 GLA 不同，TPLA 中的每个注意力头仍然对完整的潜在空间做注意力，在降低每设备 KV 缓存的同时保持了 MLA 的表示能力。为使 TPLA 能够直接兼容 MLA 检查点，我们进一步推导了 RMSNorm 与 softmax 的正交重参数化——分别以 Hadamard 与 PCA 变换实例化——以缓解跨设备切分潜在向量时的跨分片（cross-shard）偏差。最后，我们引入一种预填充-解码分离方案：在计算受限的预填充阶段保持 MLA 形式，在访存受限的解码阶段切换为 TPLA，从而最小化转换引入的误差。通过降低 DeepSeek-V3 与 Kimi-K2 的每设备 KV 缓存，我们在 32K token 的上下文长度下分别实现了 1.79× 与 1.93× 的加速，同时在常识和 LongBench 基准上保持精度。TPLA 还可以进一步在 FlashAttention-3 之上实现，从而获得实用的端到端加速。

## 英文关键词

MLA, GQA, GLA, TP, PD Disaggregate, KV Cache, PCA, Hadamard

## 中文关键词

MLA；GQA；GLA；TP；PD 分离；KV 缓存；PCA；Hadamard

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790237)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 3A](index.md) · [返回 ASPLOS 2026](../index.md)
