---
title: "LÆGIS: Pinpointing and Addressing Performance Overheads of GPU-based Confidential Computing"
description: "ISCA 2026 · Session 3C · LÆGIS: Pinpointing and Addressing Performance Overheads of GPU-based Confidential Computing"
tags:
  - "ISCA2026"
  - "Session 3C"
  - "Security"
---

# LÆGIS: Pinpointing and Addressing Performance Overheads of GPU-based Confidential Computing

**中文标题：** LÆGIS: 定位并解决基于 GPU 的机密计算的性能开销

**所属 Session：** [Session 3C](index.md) · [ISCA 2026](../index.md)

**作者：** Yang Yang, Adwait Jog

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

GPU-based Confidential Computing (CC) combines a CPU trusted execution environment (TEE) with a CC-capable GPU to protect data in use. However, it faces a memory wall: GPU memory is far more limited than CPU memory. Unified virtual memory (UVM) alleviates this constraint by allowing the CPU and GPU to share a single address space, with pages managed jointly by the GPU’s memory management unit (GMMU) and a CPU-side UVM driver. This design, however, is fault-driven and introduces significant overhead — when the GPU accesses pages residing in CPU memory, it triggers page faults that are aggregated by the GMMU and processed in batches by the driver. Under CC, every page migrated in this process must additionally be encrypted to ensure confidentiality and integrity, further amplifying the cost. We identify three key inefficiencies in UVM-based GPU CC. First, it requires tight CPU–GPU synchronization to negotiate initialization vectors (IVs) for AES-GCM encryption, placing encryption on the critical path. While this design avoids storing IVs and thus eliminates the overhead of integrity-tree maintenance, the resulting synchronization overhead significantly degrades performance. Second, the driver thread often sits idle while waiting for new fault batches to arrive, wasting CPU cycles that could otherwise be used for encryption. Third, even when the CPU is utilized, CPU software encryption throughput is low (1.3 GB/s) because UVM relies on Linux Kernel Crypto APIs that are not currently parallelized, further compounding the slowdown. To address these inefficiencies, we propose LÆGIS, a design that opportunistically pre-encrypts pages on the CPU. LÆGIS leverages secure high-bandwidth memory (HBM) for flexible IV management, introducing an IV Bank stored in 3D-stacked HBM that decouples encryption from CPU–GPU synchronization while eliminating the need for integrity trees. This enables out-of-order encryption and substantially improves UVM performance under CC. Our evaluation shows that LÆGIS significantly reduces CC overhead, achieving up to 3.13× (2.22× on average) and 5.05× (2.74× on average) speedup over the CC baseline under default and aggressive prefetching, respectively.

## 中文摘要

基于 GPU 的机密计算（Confidential Computing, CC）将 CPU 可信执行环境（TEE）与支持 CC 的 GPU 相结合，以保护使用中的数据。然而，它面临内存墙问题：GPU 内存远比 CPU 内存受限制。统一虚拟内存（Unified Virtual Memory, UVM）通过允许 CPU 与 GPU 共享单一地址空间来缓解这一约束，页面由 GPU 的内存管理单元（GMMU）与 CPU 侧的 UVM 驱动共同管理。然而，这种设计是故障驱动的，并引入了显著开销——当 GPU 访问驻留在 CPU 内存中的页时，会触发页错误，这些页错误由 GMMU 聚合、并由驱动批量处理。在 CC 下，此过程中迁移的每个页还必须额外加密以保证机密性与完整性，进一步放大了开销。我们识别出基于 UVM 的 GPU CC 中的三个关键低效之处。第一，它需要紧密的 CPU–GPU 同步来协商用于 AES-GCM 加密的初始化向量（IV），从而将加密置于关键路径上。虽然这种设计避免了存储 IV、因而消除了完整性树维护的开销，但由此产生的同步开销显著降低了性能。第二，驱动线程常常在等待新一批页错误到来时处于空闲状态，浪费了本可用于加密的 CPU 周期。第三，即使 CPU 被利用起来，CPU 软件加密的吞吐率也很低（1.3 GB/s），因为 UVM 依赖当前尚未并行化的 Linux Kernel Crypto API，进一步加剧了性能下降。为解决这些低效问题，我们提出 LÆGIS，一种在 CPU 上机会性地预加密页的设计。LÆGIS 利用安全的高带宽内存（HBM）实现灵活的 IV 管理，在 3D 堆叠 HBM 中引入 IV Bank，使加密与 CPU–GPU 同步解耦，同时消除对完整性树的需求。这使得乱序加密成为可能，并大幅提升 CC 下 UVM 的性能。我们的评估表明，LÆGIS 显著降低了 CC 开销：在默认预取与激进预取配置下，分别相比 CC 基线取得最高 3.13×（平均 2.22×）与 5.05×（平均 2.74×）的加速。


## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：insight-cal-uva/laegis-isca26-artifact](https://github.com/insight-cal-uva/laegis-isca26-artifact)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 3C](index.md) · [返回 ISCA 2026](../index.md)
