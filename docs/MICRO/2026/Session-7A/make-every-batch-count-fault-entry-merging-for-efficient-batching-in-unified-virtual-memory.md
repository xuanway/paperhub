---
title: "Make Every Batch Count: Fault Entry Merging for Efficient Batching in Unified Virtual Memory"
description: "MICRO 2026 · Session 7A · Make Every Batch Count：通过缺页条目合并实现统一虚拟内存的高效批处理"
tags:
  - "MICRO2026"
---

# Make Every Batch Count: Fault Entry Merging for Efficient Batching in Unified Virtual Memory

**中文标题：** Make Every Batch Count：通过缺页条目合并实现统一虚拟内存的高效批处理

**所属 Session：** [Session 7A](index.md) · [MICRO 2026](../index.md)

**作者：** Jane Rhee, Sejin Park, Gunjae Koo, Yunho Oh, Myung Kuk Yoon

**来源：** MICRO 2026，pp. 2293–2309；[DOI](https://doi.org/10.1109/MICRO67795.2026.00158)

## 英文摘要

While traditional system architectures with heterogeneous memory domains impose significant programming complexity, the abstraction of a unified memory space substantially improves programmability in high-performance computing. Heterogeneous Memory Management (HMM) represents a prominent standardization approach, with NVIDIA Unified Virtual Memory (UVM) as its primary real-world implementation. Despite its advantages, UVM incurs significant overhead in page fault handling due to its demand paging mechanism. To alleviate this cost, NVIDIA UVM processes page faults in batches and merges duplicate fault entries, thereby reducing redundant transfers and enhancing PCIe utilization. However, our analysis reveals that the current fault merging mechanism adversely affects batching efficiency in two major respects. First, duplicate fault entries account for an average of 60.0% of each batch, wasting available batch capacity. Second, duplicate entries are merged only after being fetched, introducing unnecessary fetching and preprocessing overhead. These inefficiencies stem from the dependency between fault merging and fault batching, as duplicates can only be identified after fetching, causing the two to interfere with each other. To address this limitation, this work proposes a novel device-side fault merging mechanism using a 2D fault window that eliminates duplicate faults without compromising batching efficiency. By performing merging directly on the GPU without driver intervention, duplicate entries can be merged independently of the batching process. Although merging all duplicate fault entries in the fault buffer may yield optimal performance, such an approach is impractical in real systems due to the latency incurred when searching across the entire buffer. We therefore extend our design with fault coalescing, which combines contiguous page faults into a single fault, providing a more practical means of improving performance. Our evaluation demonstrates that the resulting 16x16 fault window achieves an average IPC improvement of 34.4% over the default host-side approach.

## 中文摘要

虽然具有异构内存域的传统系统架构带来了显着的编程复杂性，但统一内存空间的抽象大大提高了高性能计算中的可编程性。异构内存管理 (HMM) 代表了一种突出的标准化方法，其中 NVIDIA 统一虚拟内存 (UVM) 作为其主要的实际实现。尽管 UVM 有其优点，但由于其请求分页机制，它在缺页异常处理方面会产生大量开销。为了减轻这种成本，NVIDIA UVM 批量处理缺页异常并合并重复的错误条目，从而减少冗余传输并提高 PCIe 利用率。然而，我们的分析表明，当前的故障合并机制在两个主要方面对批处理效率产生了不利影响。首先，重复的缺页条目平均占每个批次的60.0%，浪费了可用的批次容量。其次，重复的条目仅在获取后才会合并，从而引入了不必要的获取和预处理开销。这些低效率源于故障合并和缺页批处理之间的依赖性，因为只有在获取后才能识别重复项，导致两者相互干扰。为了解决这个限制，这项工作提出了一种新颖的设备端故障合并机制，使用 2D 缺页窗口来消除重复故障而不影响批处理效率。通过直接在 GPU 上执行合并而无需驱动程序干预，可以独立于批处理过程来合并重复条目。尽管合并故障缓冲区中的所有重复缺页条目可能会产生最佳性能，但由于在整个缓冲区中搜索时会产生时延，因此这种方法在实际系统中是不切实际的。因此，我们通过缺页合并扩展了我们的设计，它将连续的缺页异常合并为单个缺页条目，从而提供了一种更实用的提高性能的方法。我们的评估表明，与默认主机端方法相比，最终的 16x16 缺页窗口平均 IPC 提高了 34.4%。

## 中文关键词

统一虚拟内存；缺页异常；内存超额使用；缺页批处理；条目合并

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 7A](index.md) · [MICRO 2026 主页](../index.md)
