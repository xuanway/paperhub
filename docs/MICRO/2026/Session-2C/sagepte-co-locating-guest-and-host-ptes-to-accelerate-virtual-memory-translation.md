---
title: "SagePTE: Co-Locating Guest and Host PTEs to Accelerate Virtual Memory Translation"
description: "MICRO 2026 · Session 2C · SagePTE：通过共置客户机与宿主机页表项加速虚拟内存地址转换"
tags:
  - "MICRO2026"
---

# SagePTE: Co-Locating Guest and Host PTEs to Accelerate Virtual Memory Translation

**中文标题：** SagePTE：通过共置客户机与宿主机页表项加速虚拟内存地址转换

**所属 Session：** [Session 2C](index.md) · [MICRO 2026](../index.md)

**作者：** Amir Noohi, Mostafa Derispour, Rodrigo C. O. Rocha, Antonio Barbalace, Artemiy Margaritov

**来源：** MICRO 2026，pp. 707–722；[DOI](https://doi.org/10.1109/MICRO67795.2026.00061)

## 英文摘要

Hardware-assisted virtualization relies on two-dimensional (2D) nested address translation, trading the crippling software traps of Shadow Page Tables for severe access-time latency. This overhead is heavily concentrated at the leaf of the page walk: the final host page-table traversal required to resolve the data page. To eliminate this bottleneck, we introduce SagePTE, a hardware-software co-design that bridges the gap between nested and shadow paging by shadowing only the leaf PTEs, directly in-place within the guest page table. By expanding the guest page table layout on-demand in host memory, SagePTE co-locates guest and host mappings into a unified 128-bit extended entry. To maintain strict isolation while guaranteeing trap-free leaf synchronization, our design seamlessly repurposes existing silicon primitives, such as 128-bit compare-and-swap logic. Zero-delay hardware access mediation within the core's memory execution path safely masks guest reads and upgrades guest writes, triggering automatic hardware synchronization. This allows the page walker to fetch both translations simultaneously and bypass the final host walk entirely. SagePTE operates purely beneath the virtualization boundary, supporting unmodified guests without para-virtualization. We formally verify SagePTE's isolation guarantees using Alloy and evaluate it on ARM, demonstrating average end-to-end speedups over nested translation of 1.30x with 4 KB pages and 1.22x with Transparent Huge Pages (THP).

## 中文摘要

硬件辅助虚拟化依赖于二维 (2D) 嵌套地址转换，用影子页表的严重软件陷阱换取严重的访问时间时延。此开销主要集中在页遍历的叶节点：解析数据页所需的最终主机页表遍历。为了消除这一瓶颈，我们引入了 SagePTE，这是一种硬件-软件协同设计，通过直接在来宾页表中直接隐藏叶 PTE，弥合了嵌套分页和影子分页之间的差距。通过在主机内存中按需扩展客户页表布局，SagePTE 将客户和主机映射共同定位到一个统一的 128 位扩展条目中。为了保持严格的隔离，同时保证无陷阱叶同步，我们的设计无缝地重新利用现有的硅基元，例如 128 位比较和交换逻辑。核心内存执行路径中的零时延硬件访问中介可以安全地屏蔽访客读取并升级访客写入，从而触发自动硬件同步。这允许页表遍历器同时获取两个翻译并完全绕过最终的主机遍历。 SagePTE 纯粹在虚拟化边界下运行，支持未经修改的来宾，无需半虚拟化。我们使用 Alloy 正式验证了 SagePTE 的隔离保证，并在 ARM 上对其进行了评估，证明了使用 4 KB 页面的嵌套翻译平均端到端加速为 1.30 倍，使用透明大页面 (THP) 的嵌套翻译为 1.22 倍。

## 中文关键词

虚拟内存；地址转换；嵌套分页；页表；虚拟化；页表遍历；软硬件协同设计

## 代码与研究制品

- 代码与复现实验仓库：[https://github.com/amirmnoohi/SagePTE-AE](https://github.com/amirmnoohi/SagePTE-AE)
- 研究制品归档：[https://doi.org/10.5281/zenodo.21876937](https://doi.org/10.5281/zenodo.21876937)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 2C](index.md) · [MICRO 2026 主页](../index.md)
