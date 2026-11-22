---
title: "NB-Walker: Non-Blocking Page Table Walker to Enhance Address Translation in NUMA GPUs"
description: "MICRO 2026 · Session 8B · NB-Walker：增强 NUMA GPU 地址转换的非阻塞页表遍历器"
tags:
  - "MICRO2026"
  - "GPU"
  - "Address Translation"
---

# NB-Walker: Non-Blocking Page Table Walker to Enhance Address Translation in NUMA GPUs

**中文标题：** NB-Walker：增强 NUMA GPU 地址转换的非阻塞页表遍历器

**所属 Session：** [Session 8B](index.md) · [MICRO 2026](../index.md)

**作者：** Zihang Chen, Lieven Eeckhout, Hongyuan Liu, Tianao Ge, Xinkai Wang, Jiayi Huang

**来源：** MICRO 2026，pp. 2830–2847；[DOI](https://doi.org/10.1109/MICRO67795.2026.00192)

## 英文摘要

Modern Graphics Processing Unit (GPU) architectures have transitioned toward multi-partitioned or chiplet-based designs to scale compute throughput and memory capacity. However, this evolution introduces significant internal Non-Uniform Memory Access (NUMA) effects, where cross-partition memory latencies diverge significantly. As address translation requires sequential, multi-level probes, these NUMA-induced latencies are amplified, placing unprecedented pressure on the memory management unit. This paper identifies a critical bottleneck: traditional page table walkers employ a rigid, blocking design, where walker hardware resources are held by in-flight requests until the entire multi-level walk completes. Under NUMA conditions, long-latency remote memory probes monopolize these resources, causing translation requests to queue, which eventually stalls the entire GPU pipeline. To mitigate these translation-induced stalls, we propose NB-Walker, a high-throughput, non-blocking address translation architecture. NB-Walker decouples translation issuance from limited page walk buffers by repurposing underutilized L1 cache MSHR entries to buffer walk metadata and track outstanding page table entry fetch requests. This transformation allows the page table walkers to sustain multiple outstanding translation requests concurrently, significantly enhancing memory-level parallelism during the walk process. Furthermore, our design enables opportunistic coalescing of concurrent page table probes, reducing redundant memory traffic to the last-level cache. Experimental results demonstrate that NB-Walker significantly alleviates translation pressure, achieving a 5.56x increase in page table walk throughput on average. This enhanced concurrency translates into an average speedup of 2.78x (up to 5.73x) across translation-intensive workloads with negligible hardware overhead.

## 中文摘要

现代图形处理单元 (GPU) 架构已转向多分区或基于小芯片的设计，以扩展计算吞吐量和内存容量。然而，这种演变引入了显着的内部非均匀内存访问 (NUMA) 效应，其中跨分区内存时延存在显着差异。由于地址转换需要顺序、多级探测，这些 NUMA 引起的时延被放大，给内存管理单元带来前所未有的压力。本文指出了一个关键瓶颈：传统的页表遍历器采用严格的阻塞设计，其中遍历器硬件资源由正在进行的请求占用，直到整个多层遍历完成。在 NUMA 条件下，长时延远程内存探测会独占这些资源，导致转换请求排队，最终导致整个 GPU 管道停顿。为了减轻这些翻译引起的停顿，我们提出了 NB-Walker，一种高吞吐量、非阻塞地址转换架构。 NB-Walker 通过重新利用未充分利用的 L1 缓存 MSHR 条目来缓冲遍历元数据并跟踪未完成的页表条目获取请求，从而将翻译发布与有限的页表遍历缓冲区解耦。这种转换允许页表遍历器同时维持多个未完成的转换请求，从而显着增强遍历过程中的内存级并行性。此外，我们的设计支持并发页表探测的机会合并，减少末级缓存的冗余内存流量。实验结果表明，NB-Walker 显着减轻了翻译压力，页表遍历吞吐量平均提高了 5.56 倍。这种增强的并发性在翻译密集型工作负载中平均加速 2.78 倍（高达 5.73 倍），而硬件开销可以忽略不计。

## 中文关键词

图形处理器；虚拟内存；地址转换；页表遍历器；非均匀内存访问

## 代码与研究制品

- 代码与研究制品归档：[https://doi.org/10.5281/zenodo.21488604](https://doi.org/10.5281/zenodo.21488604)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 8B](index.md) · [MICRO 2026 主页](../index.md)
