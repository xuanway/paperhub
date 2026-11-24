---
title: "POD-Attention: Unlocking Full Prefill-Decode Overlap for Faster LLM Inference"
description: "ASPLOS 2025 · Session 7A · POD-Attention：解锁 Prefill 与 Decode 完全重叠以加速 LLM 推理"
tags:
  - "ASPLOS2025"
  - "Session 7A"
  - "Serving LLMs"
---

# POD-Attention: Unlocking Full Prefill-Decode Overlap for Faster LLM Inference

**中文标题：** POD-Attention：解锁 Prefill 与 Decode 完全重叠以加速 LLM 推理

**所属 Session：** [Session 7A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Aditya K Kamath (Paul G Allen School of Computer Science and Engineering, University of Washington), Ramya Prabhu (Microsoft Research India), Jayashree Mohan (Microsoft Research India), Simon Peter (Paul G Allen School of Computer Science and Engineering, University of Washington), Ramachandran Ramjee (Microsoft Research India), Ashish Panwar (Microsoft Research India)

**单位：** Paul G Allen School of Computer Science and Engineering, University of Washington；Microsoft Research India

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3715996) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Each request in LLM inference goes through two phases: compute-bound prefill and memory-bandwidth-bound decode. To improve GPU utilization, recent systems use hybrid batching that combines the prefill and decode phases of different requests into the same batch. This approach optimizes linear operations but remains inefficient for attention computation because existing attention kernels specialize execution independently for the prefill and decode phases. In this paper, we present POD-Attention — the first GPU kernel that efficiently computes attention for hybrid batches. POD-Attention aims to maximize the utilization of both compute and memory bandwidth by carefully allocating the GPU's resources such that prefill and decode operations happen concurrently on the same multiprocessor. POD-Attention speeds up attention computation by up to 59% (mean 28%), enabling higher throughput and lower latency LLM inference compared to the use of independently optimized prefill and decode attention kernels.

## 中文摘要

LLM 推理中的每个请求都要经历两个阶段：计算受限的 prefill 和内存带宽受限的 decode。为提升 GPU 利用率，近期系统采用混合批处理，将不同请求的 prefill 与 decode 阶段合并到同一批次中。这种方法优化了线性运算，但对注意力计算而言仍然效率不高，因为现有注意力内核针对 prefill 和 decode 阶段分别独立地专门化执行。本文提出 POD-Attention —— 首个能高效计算混合批次注意力的 GPU 内核。POD-Attention 通过精心分配 GPU 资源，使 prefill 与 decode 操作在同一多处理器上并发执行，从而最大化计算与内存带宽两者的利用率。与使用各自独立优化的 prefill 和 decode 注意力内核相比，POD-Attention 将注意力计算加速最高 59%（平均 28%），从而带来更高吞吐和更低时延的 LLM 推理。

## 英文关键词

Large language models; GPUs; self-attention

## 中文关键词

大语言模型；GPU；自注意力

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3715996)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 7A](index.md) · [返回 ASPLOS 2025](../index.md)
