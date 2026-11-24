---
title: "Reducing Page Faults via Invalidation-based Mapping Propagation in Multi-GPU Systems"
description: "ISCA 2026 · Session 6C · Reducing Page Faults via Invalidation-based Mapping Propagation in Multi-GPU Systems"
tags:
  - "ISCA2026"
  - "Session 6C"
  - "GPUs and Compilation"
---

# Reducing Page Faults via Invalidation-based Mapping Propagation in Multi-GPU Systems

**中文标题：** 通过基于失效的映射传播减少多 GPU 系统中的缺页

**所属 Session：** [Session 6C](index.md) · [ISCA 2026](../index.md)

**作者：** Junsung Kim, Dongho Ha, Sungwoo Kim, Wonho Cho, Sungbin Kim, Yufei Ding, Won Woo Ro

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Unified Virtual Memory in multi-GPU systems provides scalable hardware resources with simplified memory management to users. However, its performance is often restricted by high-latency page faults. When a page migrates, the migration mechanism invalidates old mappings on all GPUs but updates the new mapping only on the destination GPU. This leaves other GPUs’ page table entries invalid, generating subsequent page faults when the non-destination GPUs attempt to access the migrated page. Additionally, we observe that naively updating all GPUs’ entries incurs extra page table walks, resulting in significant latency overhead. To address this, we propose ShadowUpdate, a redesign of the migration handling mechanism to reduce page faults by leveraging the invalidation phase. ShadowUpdate exploits the existing invalidation broadcast to proactively propagate the new mapping simultaneously. By combining invalidation and mapping updates, this approach eliminates redundant page faults and the associated page table walks, accelerating the overall migration process. To ensure correctness, ShadowUpdate also includes a lightweight in-flight migration tracker that holds translation requests during migration, records the new mapping at invalidation, and releases the requests once the page copy completes to prevent invalid accesses. ShadowUpdate improves overall performance by 1.40× on average over a baseline UVM design across 14 representative multi-GPU UVM workloads.

## 中文摘要

多 GPU 系统中的统一虚拟内存为用户提供了可扩展的硬件资源和简化的内存管理。然而，其性能常受高延迟缺页异常的制约。当页面迁移时，迁移机制会使所有 GPU 上的旧映射失效，但仅在目标 GPU 上更新新映射。这使其他 GPU 的页表项保持无效，当非目标 GPU 尝试访问已迁移页面时便会产生后续缺页。此外，我们观察到朴素地更新所有 GPU 的页表项会带来额外的页表遍历，造成显著的延迟开销。为解决这一问题，我们提出 ShadowUpdate，一种重新设计的迁移处理机制，通过利用失效阶段来减少缺页。ShadowUpdate 利用现有的失效广播，同时主动传播新映射。通过将失效与映射更新合并，该方法消除了冗余缺页及其相关的页表遍历，加速了整体迁移过程。为确保正确性，ShadowUpdate 还包含一个轻量级的在途迁移跟踪器，在迁移期间暂挂地址转换请求，在失效时记录新映射，并在页面复制完成后释放请求，以防止无效访问。在 14 个代表性多 GPU UVM 工作负载上，ShadowUpdate 相比基线 UVM 设计平均提升整体性能 1.40 倍。


## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 6C](index.md) · [返回 ISCA 2026](../index.md)
