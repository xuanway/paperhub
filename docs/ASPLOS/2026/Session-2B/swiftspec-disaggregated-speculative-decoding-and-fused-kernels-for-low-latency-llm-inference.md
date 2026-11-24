---
title: "SwiftSpec: Disaggregated Speculative Decoding and Fused Kernels for Low-Latency LLM Inference"
description: "ASPLOS 2026 · Session 2B · SwiftSpec：面向低延迟 LLM 推理的解聚式投机解码与融合内核"
tags:
  - "ASPLOS2026"
  - "Session 2B"
  - "Speculative Decoding"
---

# SwiftSpec: Disaggregated Speculative Decoding and Fused Kernels for Low-Latency LLM Inference

**中文标题：** SwiftSpec：面向低延迟 LLM 推理的解聚式投机解码与融合内核

**所属 Session：** [Session 2B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Ziyi Zhang (ByteDance Seed & University of Chicago), Ziheng Jiang (ByteDance Seed), Chengquan Jiang (ByteDance Seed), Menghan Yu (ByteDance Seed), Size Zheng (ByteDance Seed), Haibin Lin (ByteDance Seed), Xin Liu (ByteDance Seed), Henry Hoffmann (University of Chicago)

**单位：** ByteDance Seed & University of Chicago；ByteDance Seed；University of Chicago

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790246) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Low-latency, single-request decoding of large language models is critical for interactive systems with tight SLA demands. Prior work reduces latency through speculative decoding (combining a small draft model with a larger target model), but the draft model remains on the critical path, and communication overhead limits scaling across GPUs due to the small batch size associated with single-request decoding. To address these limitations, this paper introduces SwiftSpec: a system architecture that disaggregates draft and target models across homogeneous GPUs within a single node and utilizes NCCL-low-latency primitives directly to improve the performance of core GEMM and attention kernels. Our implementation includes 3k lines of custom CUDA for fused kernels and an evolving tree cache for KV-cache consistency and maximized reuse between draft and target models. On a single 8×H800 GPU node, SwiftSpec achieves 347 tokens/s for Llama-3-70B—1.3× faster than NVIDIA's own benchmarks on a higher-performance 8×H200 setup—and averages 1.75× faster decoding than state-of-the-art speculative decoding across five model families and six datasets. Specifically, we find that for Llama-3-70B SwiftSpec is significantly faster across all 480 tested queries, showing 1. speedup over the best open-source baseline for 95th percentile requests. Code for SwiftSpec will be

## 中文摘要

面向大型语言模型的低延迟、单请求解码，对于具有严格 SLA 要求的交互式系统至关重要。先前的工作通过投机解码（将小型草稿模型与较大的目标模型相结合）来降低延迟，但草稿模型仍处于关键路径上，并且由于单请求解码对应的小批量大小，通信开销限制了跨 GPU 的扩展。为解决这些局限，本文提出 SwiftSpec：一种将草稿模型与目标模型解聚到单节点内的同构 GPU 上，并直接利用 NCCL 低延迟原语来提升核心 GEMM 与注意力内核性能的系统架构。我们的实现包含 3k 行用于融合内核的自定义 CUDA 代码，以及一个用于保持 KV 缓存一致性并最大化草稿模型与目标模型之间复用的演化树缓存。在单个 8×H800 GPU 节点上，SwiftSpec 对 Llama-3-70B 达到 347 tokens/s——比 NVIDIA 在性能更高的 8×H200 配置上给出的自身基准快 1.3×——并且在五个模型家族和六个数据集上平均比最先进的投机解码快 1.75×。具体而言，我们发现对于 Llama-3-70B，SwiftSpec 在所有 480 条测试查询上均显著更快，在第 95 百分位请求上相比最佳开源基线展现出 1. 的加速。SwiftSpec 的代码将

## 英文关键词

large language model serving, speculative decoding, kernel optimization

## 中文关键词

大语言模型服务；投机解码；内核优化

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790246)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 2B](index.md) · [返回 ASPLOS 2026](../index.md)
