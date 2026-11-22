---
title: "CacheFlex: Direct Software-Managed Access to Higher-Level Cache for Scalable Vector Support"
description: "MICRO 2026 · Session 6D · CacheFlex：通过软件直接管理的高层级缓存访问实现可扩展向量支持"
tags:
  - "MICRO2026"
  - "Cache"
---

# CacheFlex: Direct Software-Managed Access to Higher-Level Cache for Scalable Vector Support

**中文标题：** CacheFlex：通过软件直接管理的高层级缓存访问实现可扩展向量支持

**所属 Session：** [Session 6D](index.md) · [MICRO 2026](../index.md)

**作者：** Jingqun Zhang, Maohua Nie, Jiayi Wang, Weihang Li, Rishi Sappidi, Shwet Chitnis, Ang Li

**来源：** MICRO 2026，pp. 2186–2200；[DOI](https://doi.org/10.1109/MICRO67795.2026.00151)

## 英文摘要

Modern CPUs demand urgent upgrades to keep up with the AI revolution. While peak compute throughput can be multiplied by widening vector/SIMD lanes, significant improvements of the cache system remain challenging. We pinpoint L1 data cache capacity as the single design parameter that yields the highest performance and efficiency gains. However, L1 capacity is constrained by its tight coupling within the core pipeline and the single-digit-cycle latency requirement, so we turn to the private L2 cache that provides an order of magnitude more capacity but is conventionally inaccessible from software. This work proposes CacheFlex, an ISA and microarchitecture co-design that enables software-managed, direct access to private L2 SRAM by allowing runtime conversion of parts of L2 into a scratchpad memory (SPM). Through a lightweight ISA extension, software explicitly controls data placement and lifetime within the L2. CacheFlex integrates into an out-of-order pipeline with cross-domain memory consistency and OS context-switch support, with merely 2.02% area overhead relative to the L2 in a post-layout 12 nm implementation. We prototype CacheFlex based on the Armv8-A SVE ISA, model it in gem5, and evaluate it using optimized general matrix multiplication (GEMM) kernels with diverse model-derived shapes, FlashAttention-based fused attention, and full-layer workloads from LLaMA-3.2-1B and BERT-Base in the prefill phase. As the vector length (VL) scales from VL = 4 (512-bit) to VL = 16 (2048-bit), CacheFlex's kernel-level geometric-mean speedup and memory-subsystem energy reduction grow from 1.12× and 26% to 1.44× and 40%, respectively, bridging the widening gap between per-instruction data demand and memory performance. On full transformer layers combining CacheFlex with FlashAttention, the design delivers up to 1.78× speedup and 45% memory-subsystem energy savings (BERT-Base, sequence length T = 4096, VL = 16; LLaMA-3.2-1B: 1.64× and 38%). CacheFlex is complementary to hardware prefetching, and its benefit grows as vector width and peak compute throughput increase for compute-intensive AI kernels.

## 中文摘要

现代 CPU 需要紧急升级才能跟上人工智能革命的步伐。虽然峰值计算吞吐量可以通过加宽矢量/SIMD 通道来倍增，但缓存系统的显着改进仍然具有挑战性。我们将 L1 数据缓存容量确定为可产生最高性能和效率增益的单一设计参数。然而，L1 容量受到其在核心管道内的紧密耦合和个位数周期时延要求的限制，因此我们转向私有 L2 缓存，它提供了一个数量级的容量，但通常无法通过软件访问。这项工作提出了 CacheFlex，这是一种 ISA 和微架构协同设计，通过允许在运行时将 L2 部分转换为暂存存储器 (SPM)，实现对私有 L2 SRAM 的软件管理、直接访问。通过轻量级 ISA 扩展，软件可以明确控制 L2 内的数据放置和生命周期。 CacheFlex 集成到具有跨域内存一致性和操作系统上下文切换支持的无序管道中，相对于布局后 12 nm 实现中的 L2，区域开销仅为 2.02%。我们基于 Armv8-A SVE ISA 设计了 ​​CacheFlex 原型，在 gem5 中对其进行建模，并使用具有多种模型衍生形状的优化通用矩阵乘法 (GEMM) 内核、基于 FlashAttention 的融合注意力以及预填充阶段来自 LLaMA-3.2-1B 和 BERT-Base 的全层工作负载对其进行评估。随着向量长度 (VL) 从 VL = 4（512 位）扩展到 VL = 16（2048 位），CacheFlex 的内核级几何平均加速和内存子系统能耗分别从 1.12 倍和 26% 增长到 1.44 倍和 40%，从而缩小了每条指令数据需求和内存性能之间日益扩大的差距。在将 CacheFlex 与 FlashAttention 相结合的完整Transformer层上，该设计可实现高达 1.78 倍的加速和 45% 的内存子系统节能（BERT-Base，序列长度 T = 4096，VL = 16；LLaMA-3.2-1B：1.64 倍和 38%）。 CacheFlex 是对硬件预取的补充，其优势随着计算密集型 AI 内核的向量宽度和峰值计​​算吞吐量的增加而增长。

## 中文关键词

处理器微架构；指令集扩展；可扩展向量处理；可重构缓存；软件管理暂存存储器

## 代码与研究制品

- 代码与复现实验仓库：[https://github.com/JingqunZhang/cacheflex-ae](https://github.com/JingqunZhang/cacheflex-ae)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 6D](index.md) · [MICRO 2026 主页](../index.md)
