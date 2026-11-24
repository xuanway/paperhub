---
title: "Hitchhike: Efficient Request Submission via Deferred Enforcement of Address Contiguity"
description: "ASPLOS 2026 · Session 5D · Hitchhike：通过延迟执行地址连续性校验实现高效请求提交"
tags:
  - "ASPLOS2026"
  - "Session 5D"
  - "Storage & Caching"
---

# Hitchhike: Efficient Request Submission via Deferred Enforcement of Address Contiguity

**中文标题：** Hitchhike：通过延迟执行地址连续性校验实现高效请求提交

**所属 Session：** [Session 5D](index.md) · [ASPLOS 2026](../index.md)

**作者：** xuda zheng (Huazhong University of Science and Technology), Jian Zhou (Huazhong University of Science and Technology), Shuhan Bai (Huazhong University of Science and Technology), Runjin Wu (Huazhong University of Science and Technology), Xianlin Tang (Huazhong University of Science and Technology), Zhiyuan Li (Huazhong University of Science and Technology), Hong Jiang (UT Arlington), Fei Wu (Huazhong University of Science and Technology)

**单位：** Huazhong University of Science and Technology；UT Arlington

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790173) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Modern storage systems operate under high concurrency, making large volumes of outstanding I/Os the norm. However, current I/O submission logic requires requests assigned to the same CPU core to be processed in a serialized manner, turning the software stack into a bottleneck due to high per-request overhead. We argue that the primary cause of this inefficiency lies in the end-to-end enforcement of the strict address contiguity validation—the constraint that each I/O request must access a contiguous range of addresses (e.g., file offsets, sectors, and logical block addresses). Through system-level analysis, we find that while the address contiguity requirement is crucial at the device level as defined by the NVMe protocol, it is unnecessarily enforced throughout the entire I/O stack. Based on this insight, we propose Hitchhike, an efficient request submission logic that defers address contiguity validation to the device driver. Unlike solutions that resort to kernel-bypass or aggressive polling for performance, Hitchhike achieves high efficiency within the standard OS stack by allowing a single request to encapsulate multiple non-contiguous address ranges. This mechanism drastically reduces the number of individual requests traversing the stack, thereby amortizing the kernel's per-request overhead. We apply Hitchhike to a graph engine, a B-tree store, and FIO. Experimental results show that Hitchhike effectively improves throughput and reduces CPU overhead, while preserving compatibility with existing kernel semantics and hardware interfaces.

## 中文摘要

现代存储系统在高并发下运行，使得大量未完成的 I/O 成为常态。然而，当前的 I/O 提交逻辑要求分配给同一 CPU 核的请求以串行方式处理，由于每请求开销很高，这使软件栈成为瓶颈。我们认为，这种低效的主要原因在于对严格地址连续性校验的端到端强制执行——即每个 I/O 请求必须访问连续地址范围（例如文件偏移、扇区和逻辑块地址）这一约束。通过系统级分析，我们发现，虽然地址连续性要求在设备层是至关重要的（由 NVMe 协议定义），但它在整个 I/O 栈中被不必要地强制执行。基于这一洞见，我们提出 Hitchhike，一种高效的请求提交逻辑，它将地址连续性校验延迟到设备驱动。与为提升性能而诉诸内核旁路或激进轮询的解决方案不同，Hitchhike 通过在标准 OS 栈内允许单个请求封装多个非连续地址范围来实现高效率。该机制大幅减少了穿越栈的单个请求数量，从而摊薄了内核的每请求开销。我们将 Hitchhike 应用于一个图引擎、一个 B-tree 存储和 FIO。实验结果表明，Hitchhike 有效提升了吞吐量并降低了 CPU 开销，同时保持与现有内核语义和硬件接口的兼容性。

## 英文关键词

NVMe SSD; Parallelism; Asynchronous I/O stack

## 中文关键词

NVMe SSD；并行性；异步 I/O 栈

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790173)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 5D](index.md) · [返回 ASPLOS 2026](../index.md)
