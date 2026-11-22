---
title: "DUALign: A Hardware-Assisted Memory Mapping Strategy for PNM-Accelerated LLM Serving"
description: "MICRO 2026 · Session 5C · DUALign：面向近存处理加速 LLM 服务的硬件辅助内存映射策略"
tags:
  - "MICRO2026"
  - "LLM Inference"
  - "Near-Memory Computing"
---

# DUALign: A Hardware-Assisted Memory Mapping Strategy for PNM-Accelerated LLM Serving

**中文标题：** DUALign：面向近存处理加速 LLM 服务的硬件辅助内存映射策略

**所属 Session：** [Session 5C](index.md) · [MICRO 2026](../index.md)

**作者：** Euijun Kim, Joshua Gabriel Dela Rosa, Bogil Kim, Youngin Kim, Seungyong Lee, Joonseop Sim, Youngpyo Joo, William J. Song

**来源：** MICRO 2026，pp. 1767–1783；[DOI](https://doi.org/10.1109/MICRO67795.2026.00126)

## 英文摘要

Large language model (LLM) inference is limited by memory capacity and bandwidth. To improve throughput, LLM serving frameworks reduce per-user memory footprint by allocating key-value (KV) cache space on demand as they grow, enabling higher user concurrency within limited device memory. In parallel, recent architectures integrate processing-near-memory (PNM) capability into GPUs to accelerate bandwidth-intensive attention layers. Placed on the logic die of high-bandwidth memory (HBM), PNM units can exploit high internal bandwidth when their operands reside within a local HBM stack. However, these approaches are difficult to combine: PNM uses physical addressing to place data within a target HBM stack, whereas LLM serving frameworks on GPUs rely on memory virtualization and cannot directly control physical memory placement. To reconcile this incompatibility, we propose DUALign, a hardware-assisted memory mapping strategy that enables HBM-stack-aware data placement under virtualized memory. DUALign introduces subpages as a fine-grained unit for stack-aware data placement and aligns physical-to-DRAM mapping such that each subpage fits entirely within an HBM stack. This allows the driver to control subpage-to-stack placement simply through physical frame number (PFN) assignment, so that subpages from the same virtual page can be distributed across stacks for GPU execution or gathered within a single stack for PNM locality, while preserving the address translation mechanism of GPUs. By combining PNM acceleration with virtualized on-demand KV cache allocation, DUALign improves throughput by up to 2.29x over physical addressing PNM designs with a 5.97x increase in user concurrency.

## 中文摘要

大语言模型 (LLM) 推理受到内存容量和带宽的限制。为了提高吞吐量，LLM 服务框架通过根据需要分配键值 (KV) 缓存空间来减少每个用户的内存占用，从而在有限的设备内存内实现更高的用户并发性。与此同时，最新的架构将近存处理 (PNM) 功能集成到 GPU 中，以加速带宽密集型关注层。 PNM 单元放置在高带宽存储器 (HBM) 的逻辑芯片上，当其操作数驻留在本地 HBM 堆栈中时，可以利用高内部带宽。然而，这些方法很难组合起来：PNM 使用物理寻址将数据放置在目标 HBM 堆栈中，而 GPU 上的 LLM 服务框架依赖于内存虚拟化，无法直接控制物理内存放置。为了解决这种不兼容性，我们提出了 DUALign，这是一种硬件辅助内存映射策略，可在虚拟化内存下实现 HBM 堆栈感知数据放置。 DUALign 引入子页作为堆栈感知数据放置的细粒度单元，并对齐物理到 DRAM 映射，以便每个子页完全适合 HBM 堆栈。这使得驱动程序只需通过物理帧号 (PFN) 分配来控制子页面到堆栈的放置，以便来自同一虚拟页面的子页面可以跨堆栈分布以供 GPU 执行，或聚集在单个堆栈内以实现 PNM 局部性，同时保留 GPU 的地址转换机制。通过将 PNM 加速与虚拟化按需 KV 缓存分配相结合，DUALign 的吞吐量比物理寻址 PNM 设计提高了 2.29 倍，用户并发性提高了 5.97 倍。

## 中文关键词

近存处理；内存管理；大语言模型；硬件辅助映射

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 5C](index.md) · [MICRO 2026 主页](../index.md)
