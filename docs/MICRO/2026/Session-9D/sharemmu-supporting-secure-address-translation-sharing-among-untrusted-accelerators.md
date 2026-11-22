---
title: "ShareMMU: Supporting Secure Address Translation Sharing Among Untrusted Accelerators"
description: "MICRO 2026 · Session 9D · ShareMMU：支持不可信加速器之间安全共享地址转换"
tags:
  - "MICRO2026"
  - "Address Translation"
---

# ShareMMU: Supporting Secure Address Translation Sharing Among Untrusted Accelerators

**中文标题：** ShareMMU：支持不可信加速器之间安全共享地址转换

**所属 Session：** [Session 9D](index.md) · [MICRO 2026](../index.md)

**作者：** Faiz Alam, Mohamed Tarek Ibn Ziad, Yuanchao Xu, Abdulrahman Mahmoud, Greg Byrd, Aamer Jaleel

**来源：** MICRO 2026，pp. 3461–3478；[DOI](https://doi.org/10.1109/MICRO67795.2026.00231)

## 英文摘要

The growing demand for accelerated computing is driving widespread deployment of multi-accelerator systems in the cloud and at the edge. These systems are temporally shared across processes that may not mutually trust one another and often include large pools of third-party, untrusted accelerators operating within a shared virtual address space. Due to the limited capability of the Input-Output Memory Management Unit (IOMMU) in supporting address translation, SoC designers are integrating large Shared Translation Lookaside Buffers (TLBs) that serve many accelerators and processes. While effective for performance, shared TLBs introduce new security risks that require urgent and careful consideration. This paper presents ShareMMU, an IOMMU design that securely enables reuse of pre-translated addresses across multiple untrusted accelerators while also mitigating potential side channels in the shared TLB. Compared to state-of-the-art mechanisms like Border Control and CryptoMMU, which incur 32% and 17% performance overhead, respectively, ShareMMU incurs a negligible 1.66% performance overhead relative to an unsecured baseline. Our side-channel resilient variant, ShareMMU-SP, incurs roughly 2.82% overhead.

## 中文摘要

对加速计算不断增长的需求正在推动多加速器系统在云端和边缘的广泛部署。这些系统在彼此可能不相互信任的进程之间时间共享，并且通常包括在共享虚拟地址空间内运行的大量第三方、不受信任的加速器。由于输入输出内存管理单元 (IOMMU) 在支持地址转换方面的能力有限，SoC 设计人员正在集成为许多加速器和进程提供服务的大型共享地址转换后备缓冲器 (TLB)。虽然共享 TLB 对性能有效，但它带来了新的安全风险，需要紧急和仔细的考虑。本文介绍了 ShareMMU，这是一种 IOMMU 设计，可以安全地跨多个不受信任的加速器重用预转换地址，同时还可以减少共享 TLB 中潜在的侧通道。与边界控制和 CryptoMMU 等最先进的机制（分别产生 32% 和 17% 的性能开销）相比，相对于不安全的基线，ShareMMU 产生的性能开销可以忽略不计，为 1.66%。我们的侧通道弹性变体 ShareMMU-SP 会产生大约 2.82% 的开销。

## 中文关键词

输入输出内存管理单元；加速器；访问控制；地址转换；共享地址转换缓存；内存隔离

## 代码与研究制品

- 代码与研究制品归档：[https://doi.org/10.5281/zenodo.21543532](https://doi.org/10.5281/zenodo.21543532)

以上入口来自论文正文或 Artifact 附录。

[返回 Session 9D](index.md) · [MICRO 2026 主页](../index.md)
