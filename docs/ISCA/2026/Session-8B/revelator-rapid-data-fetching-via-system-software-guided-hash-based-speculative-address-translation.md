---
title: "Revelator: Rapid Data Fetching via System-Software-Guided Hash-based Speculative Address Translation"
description: "ISCA 2026 · Session 8B · Revelator: Rapid Data Fetching via System-Software-Guided Hash-based Speculative Address Translation"
tags:
  - "ISCA2026"
  - "Session 8B"
  - "Prefetching and Cache 1"
---

# Revelator: Rapid Data Fetching via System-Software-Guided Hash-based Speculative Address Translation

**中文标题：** Revelator: 借助系统软件引导的基于哈希的推测性地址翻译实现快速数据获取

**所属 Session：** [Session 8B](index.md) · [ISCA 2026](../index.md)

**作者：** Konstantinos Kanellopoulos, Konstantinos Sgouras, Harsh Songara, Andreas Kosmas Kakolyris, Vlad-Petru Nitu, Spiros Galanopoulos, Rahul Bera, Konstantina Koliogeorgi, Rakesh Kumar, Onur Mutlu

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Address translation is a significant performance bottleneck in modern computing systems. Predicting the physical address (PA) of the requested data before address translation completes is a promising technique to hide the latency of address translation. However, accurately predicting the PA based on the virtual address (VA) is highly challenging due to the inherent unpredictability of the VA-to-PA mappings that conventional operating systems introduce. Prior works try to introduce predictability into VA-to-PA mappings but exhibit two key shortcomings: (i) they rely on the availability of large pages or VA-to-PA contiguity, and (ii) they store speculation-related metadata in costly hardware components whose power and area overheads may not always justify their benefits. We introduce Revelator, a new hardware-OS cooperative technique that uses hashing to enable highly accurate speculative address translation with small system modifications. At the OS level, Revelator employs a tiered hash-based memory allocation policy for both program data and last-level page table entries (PTEs) to establish predictable VA-to-PA and VA-to-PTE mappings. At the hardware level, after an L2 TLB miss, a lightweight speculation engine uses the OS’s hash functions to predict the VA-to-PA and VA-to-PTE mappings and prefetch the corresponding cache blocks before address translation completes, thereby both hiding address translation latency and accelerating page table walks (PTWs). Revelator comes with two key benefits: (i) it does not rely on large pages or VA-to-PA contiguity to achieve high speculation accuracy, and (ii) it requires small OS and hardware modifications. Our evaluation across 11 data-intensive workloads shows that, (i) in single-core systems, Revelator provides an average speedup of 15.3% over the state-of-the-art speculative address translation technique under high memory fragmentation, and (ii) in virtualized environments, by accurately predicting both guest and host physical addresses, Revelator provides a 13.6% average speedup over Nested Paging. In multicore systems, Revelator’s benefits scale with core count, enabling a speedup of 1.40× (1.50×) over Transparent Huge Pages (THP) across 30 server workload mixes from Google in a 16-core system under medium (high) memory fragmentation. These gains come at very small hardware cost. Our RTL synthesis shows that Revelator incurs only 0.02% area and 0.03% power overheads on top of a high-end server-grade CPU. Revelator is freely available at github.com/CMU-SAFARI/Virtuoso.

## 中文摘要

地址翻译是现代计算系统中的显著性能瓶颈。在地址翻译完成之前预测所请求数据的物理地址（PA），是一种有望隐藏地址翻译延迟的技术。然而，由于传统操作系统引入的 VA 到 PA 映射本身具有不可预测性，基于虚拟地址（VA）准确预测 PA 极具挑战。已有工作试图为 VA 到 PA 映射引入可预测性，但存在两个关键缺陷：(i) 它们依赖大页或 VA 到 PA 的连续性是否可得；(ii) 它们将推测相关的元数据存储在昂贵的硬件组件中，其功耗与面积开销并不总能证明其收益合理。我们提出 Revelator，一种新的硬件—操作系统协同技术，它利用哈希，只需少量系统修改即可实现高精度的推测性地址翻译。在操作系统层面，Revelator 对程序数据和末级页表项（PTE）均采用分层的、基于哈希的内存分配策略，以建立可预测的 VA 到 PA 以及 VA 到 PTE 映射。在硬件层面，发生 L2 TLB 缺失后，一个轻量级推测引擎使用操作系统的哈希函数预测 VA 到 PA 和 VA 到 PTE 映射，并在地址翻译完成之前预取相应的缓存块，从而既隐藏地址翻译延迟，又加速页表遍历（PTW）。Revelator 有两个关键优势：(i) 它不依赖大页或 VA 到 PA 连续性即可实现高推测准确率；(ii) 它只需要对操作系统和硬件做少量修改。我们在 11 个数据密集型工作负载上的评估表明：(i) 在单核系统中，Revelator 在高内存碎片情况下相较最先进的推测性地址翻译技术平均加速 15.3%；(ii) 在虚拟化环境中，通过准确预测客户机与宿主机的物理地址，Revelator 相较嵌套分页（Nested Paging）平均加速 13.6%。在多核系统中，Revelator 的收益随核数扩展：在 16 核系统中，针对来自 Google 的 30 个服务器工作负载混合，在中度（高度）内存碎片下相较透明大页（THP）实现 1.40×（1.50×）的加速。这些收益来自极小的硬件成本。我们的 RTL 综合显示，Revelator 在高端服务器级 CPU 之上仅带来 0.02% 的面积和 0.03% 的功耗开销。Revelator 已在 github.com/CMU-SAFARI/Virtuoso 免费提供。

## 代码与研究制品

论文对应实现位于 Virtuoso 模拟框架中；仓库文档包含 Revelator 的分配器与地址翻译实现说明。

- [代码仓库：CMU-SAFARI/Virtuoso](https://github.com/CMU-SAFARI/Virtuoso)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 8B](index.md) · [返回 ISCA 2026](../index.md)
