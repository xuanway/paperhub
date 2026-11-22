---
title: "SYMPHONY: Harmonizing Memory and Communication in LLM Inference on 3D DRAM Accelerators"
description: "MICRO 2026 · Session 8A · SYMPHONY：协调三维 DRAM 加速器上 LLM 推理的内存与通信"
tags:
  - "MICRO2026"
  - "LLM Inference"
  - "DRAM"
---

# SYMPHONY: Harmonizing Memory and Communication in LLM Inference on 3D DRAM Accelerators

**中文标题：** SYMPHONY：协调三维 DRAM 加速器上 LLM 推理的内存与通信

**所属 Session：** [Session 8A](index.md) · [MICRO 2026](../index.md)

**作者：** Sabuj Laskar, Hyojong Kim, Devesh Singh, Mrinmoy Ghosh, Eun Jung Kim

**来源：** MICRO 2026，pp. 2719–2737；[DOI](https://doi.org/10.1109/MICRO67795.2026.00185)

## 英文摘要

In modern LLM autoregressive decoding, model weights and the KV cache can reach hundreds of gigabytes, leading to substantial data movement during execution. Because decoding has low arithmetic intensity, data movement dominates both latency and energy. 3D DRAM accelerators address this bottleneck by colocating compute with stacked DRAM, keeping weights and the KV cache physically close to processing units. When scaled across hundreds of dies interconnected in a mesh, large weight and KV cache tensors can remain near compute, significantly reducing the latency and energy costs of data movement. However, this approach requires careful tensor partitioning and co-optimization of computation, activation communication, and memory access, especially under limited interconnect bandwidth and non-uniform mesh connectivity. To address these challenges, we propose SYMPHONY, a framework that orchestrates the lock-step interplay of memory, compute, and communication. By analyzing six key operators that dominate decode latency, SYMPHONY identifies the specific resource constraints of each, whether they are bound by memory bandwidth, compute or communication. SYMPHONY coordinates these distinct operational profiles by managing the data placement of both the weights and the KV Cache. For weights, SYMPHONY maps memory-bound operators across all PEs to maximize aggregate memory bandwidth while localizing communication-heavy operators to internal PEs. For the KV Cache, SYMPHONY localizes it for short sequences to minimize data movement cost and expands it across all PEs for long contexts when memory is the bottleneck. Furthermore, to refine this coordination, we introduce Border-Enhanced AllReduce Mapping (BEAM), a collective algorithm that utilizes border PEs as auxiliary communication paths. This choreographed approach allows SYMPHONY to achieve 1.35-1.67x lower decode-stage latency compared to state-of-the-art weight partitioning strategies.

## 中文摘要

在现代 LLM 自回归解码中，模型权重和 KV 缓存可以达到数百 GB，导致执行期间发生大量数据移动。由于解码的算术强度较低，因此数据移动在时延和能量方面都占主导地位。 3D DRAM 加速器通过将计算与堆叠 DRAM 并置、保持权重和 KV 缓存在物理上靠近处理单元来解决这一瓶颈。当扩展到网格中互连的数百个芯片时，大权重和 KV 缓存张量可以保持在计算附近，从而显着降低数据移动的时延和能源成本。然而，这种方法需要仔细的张量划分以及计算、激活通信和内存访问的协同优化，特别是在有限的互连带宽和非均匀网格连接的情况下。为了应对这些挑战，我们提出了 SYMPHONY，这是一个协调内存、计算和通信的锁步相互作用的框架。通过分析主导解码时延的六个关键运算符，SYMPHONY 确定了每个运算符的特定资源限制，无论它们是否受到内存带宽、计算或通信的限制。 SYMPHONY 通过管理权重和 KV 缓存的数据放置来协调这些不同的操作配置文件。对于权重，SYMPHONY 将内存限制运算符映射到所有 PE，以最大化聚合内存带宽，同时将通信密集型运算符本地化到内部 PE。对于 KV 缓存，SYMPHONY 将其本地化为短序列，以最大限度地降低数据移动成本，并在内存成为瓶颈时将其扩展到所有 PE，以实现长上下文。此外，为了完善这种协调，我们引入了边界增强型 AllReduce 映射 (BEAM)，这是一种利用边界 PE 作为辅助通信路径的集体算法。与最先进的权重划分策略相比，这种精心设计的方法使 SYMPHONY 的解码阶段时延降低了 1.35-1.67 倍。

## 中文关键词

大语言模型推理；三维堆叠 DRAM；张量并行；集合通信；近存处理

## 代码与研究制品

- 代码仓库：[https://github.com/sabujlaskar/Symphony](https://github.com/sabujlaskar/Symphony)（论文提供的地址；2026-11-10 检查返回 HTTP 404）
- 研究制品归档：[https://doi.org/10.5281/zenodo.21525799](https://doi.org/10.5281/zenodo.21525799)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 8A](index.md) · [MICRO 2026 主页](../index.md)
