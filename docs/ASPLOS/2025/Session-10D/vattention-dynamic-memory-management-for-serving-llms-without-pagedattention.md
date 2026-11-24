---
title: "vAttention: Dynamic Memory Management for Serving LLMs without PagedAttention"
description: "ASPLOS 2025 · Session 10D · vAttention：无需 PagedAttention 的 LLM 服务动态内存管理"
tags:
  - "ASPLOS2025"
  - "Session 10D"
  - "Memory Management"
---

# vAttention: Dynamic Memory Management for Serving LLMs without PagedAttention

**中文标题：** vAttention：无需 PagedAttention 的 LLM 服务动态内存管理

**所属 Session：** [Session 10D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Ramya Prabhu (Microsoft Research), Ajay Nayak (Indian Institute of Science), Jayashree Mohan (Microsoft Research), Ramachandran Ramjee (Microsoft Research), Ashish Panwar (Microsoft Research)

**单位：** Microsoft Research；Indian Institute of Science

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707256) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

PagedAttention is a popular approach for dynamic memory allocation in LLM serving systems. It enables on-demand allocation of GPU memory to mitigate KV cache fragmentation — a phenomenon that crippled the batch size (and consequently throughput) in prior systems. However, in trying to allocate physical memory at runtime, PagedAttention ends up changing the virtual memory layout of the KV cache from contiguous to non-contiguous. Such a design leads to non-trivial programming and performance overheads. We present vAttention — an approach that mitigates fragmentation in physical memory while retaining the virtual memory contiguity of the KV cache. We achieve this by decoupling the allocation of virtual and physical memory using CUDA virtual memory management APIs. We also introduce various LLM-specific optimizations to address the limitations of CUDA virtual memory support. Overall, vAttention is a simpler, portable, and performant alternative to PagedAttention: it supports various attention kernels outof-the-box and improves LLM serving throughput by up to 1.23× compared to the use of PagedAttention-based kernels of FlashAttention-2 and FlashInfer.

## 中文摘要

PagedAttention 是 LLM 服务系统中一种流行的动态内存分配方法。它支持按需分配 GPU 内存，从而缓解 KV cache 碎片化问题——这一问题曾严重限制此前系统中的批大小（并因此限制吞吐量）。然而，为了在运行时分配物理内存，PagedAttention 最终把 KV cache 的虚拟内存布局从连续变为非连续。这种设计带来了不容忽视的编程开销与性能开销。我们提出 vAttention——一种在缓解物理内存碎片化的同时保留 KV cache 虚拟内存连续性的方法。我们通过 CUDA 虚拟内存管理 API 解耦虚拟内存与物理内存的分配来实现这一点。我们还引入了多种面向 LLM 的优化，以应对 CUDA 虚拟内存支持的局限性。总体而言，vAttention 是 PagedAttention 更简单、可移植且高性能的替代方案：它开箱即用支持多种注意力内核，并且与使用 FlashAttention-2 和 FlashInfer 中基于 PagedAttention 的内核相比，将 LLM 服务吞吐量最多提升 1.23 倍。

## 英文关键词

Large language models; KV cache; fragmentation; memory management

## 中文关键词

大语言模型；KV cache；碎片化；内存管理

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707256)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 10D](index.md) · [返回 ASPLOS 2025](../index.md)
