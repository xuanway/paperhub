---
title: "DPU-KV: On the Benefits of DPU Offloading for In-Memory Key-Value Stores at the Edge"
description: "HPDC 2025 · Session 3 — Storage Systems"
tags:
  - "HPDC2025"
  - "Session 3"
  - "Storage Systems"
---

# DPU-KV: On the Benefits of DPU Offloading for In-Memory Key-Value Stores at the Edge

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2025 主会 Session 3 — Storage Systems（2025年7月21日 15:30–16:45 · Session Chair：Hariharan Devarajan）。</p>
<p class="paper-seo-summary__tags">HPDC 2025 · Session 3</p>
</div>

**官方资料**：[HPDC 2025 官方议程](https://hpdc.sci.utah.edu/2025/program.html) · [ACM DOI](https://doi.org/10.1145/3731545.3731571) · [Slides](https://hpdc.sci.utah.edu/2025/assets/slides/main_session/kashyap.pdf)

**作者**：Arjun Kashyap, Yuke Li, Xiaoyi Lu

**会议**：HPDC 2025 · Notre Dame, IN, USA

**Session**：Session 3 — Storage Systems（2025年7月21日 15:30–16:45 · Session Chair：Hariharan Devarajan）

---

## 英文摘要

In-memory key-value stores (KVS) are widely used for edge data storage, where low latency and high throughput are essential. Data Processing Units (DPUs), with their low power use and offloading capabilities, suit resource-constrained edge computing. While DPUs offer a new design point for KVS, their offloading in edge environments remains underexplored and challenging. In this paper, we unveil the potential of offloading in-memory CPU-based KVS to SoC-based DPUs, specifically NVIDIA’s BlueField-2 (BF-2) and BlueField-3 (BF-3), with the aim of enhancing KVS performance. We propose a principled exploration methodology of dividing a KVS (i.e., MICA) into its logical components and identifying the CPU-intensive KVS component (i.e., communication engine). Next, we perform fine-grained offloading analysis and explorations on DPUs. To maximize benefits in terms of latency and throughput from fine-grained KVS offloading on DPUs, we propose a series of significant performance optimizations, including a key-value-based queue-pair model, overlapped KV request/response processing, reduced DMA operations per KV batch, dual-communication engine, and a sharding-based design. Our key finding is that our proposed fine-grained KVS offloading designs on modern DPU architectures (i.e., BF-2 and BF-3) can provide much lower latency (up to 68%) and higher throughput (up to 36%) than MICA (CPU-only) and coarse-grained DPU offloading schemes at the edge. To our knowledge, this paper is the first to explore the performance benefits of fine-grained KVS offloading to DPUs at the edge.

## 中文摘要

内存键值存储（KVS）广泛用于边缘数据存储，其中低延迟与高吞吐至关重要。数据处理单元（DPU）凭借低功耗与卸载能力，适合资源受限的边缘计算。尽管 DPU 为 KVS 提供了新的设计空间，但其在边缘环境中的卸载仍未得到充分探索且颇具挑战。本文揭示将基于 CPU 的内存 KVS 卸载到基于 SoC 的 DPU（具体为 NVIDIA BlueField-2（BF-2）和 BlueField-3（BF-3））以提升 KVS 性能的潜力。我们提出一种有原则的探索方法：将 KVS（即 MICA）拆分为其逻辑组件，并识别出 CPU 密集的 KVS 组件（即通信引擎）。随后，我们在 DPU 上进行细粒度卸载分析与探索。为在 DPU 上通过细粒度 KVS 卸载最大化延迟与吞吐方面的收益，我们提出一系列重要的性能优化，包括基于键值对的队列对模型、重叠的 KV 请求/响应处理、减少每 KV 批次的 DMA 操作、双通信引擎以及基于分片的设计。我们的关键发现是：所提出的面向现代 DPU 架构（BF-2 与 BF-3）的细粒度 KVS 卸载设计，在边缘可提供比 MICA（纯 CPU）与粗粒度 DPU 卸载方案低得多的延迟（最高降低 68%）和更高的吞吐（最高提升 36%）。据我们所知，本文首次探索了在边缘将细粒度 KVS 卸载到 DPU 的性能收益。

## 英文关键词

Data Processing Units (DPUs), Key-Value Stores, Offloading, Edge

## 中文关键词

数据处理单元（DPU），键值存储，卸载，边缘

---

[← 返回 Session 3 — Storage Systems](index.md)
