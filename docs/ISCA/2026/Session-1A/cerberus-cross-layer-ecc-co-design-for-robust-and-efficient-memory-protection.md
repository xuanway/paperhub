---
title: "Cerberus: Cross-Layer ECC Co-Design for Robust and Efficient Memory Protection"
description: "ISCA 2026 · Session 1A · Cerberus: Cross-Layer ECC Co-Design for Robust and Efficient Memory Protection"
tags:
  - "ISCA2026"
  - "Session 1A"
  - "Best Paper Candidate Session"
---

# Cerberus: Cross-Layer ECC Co-Design for Robust and Efficient Memory Protection

**中文标题：** Cerberus: 面向鲁棒高效内存保护的跨层 ECC 协同设计

**所属 Session：** [Session 1A](index.md) · [ISCA 2026](../index.md)

**作者：** Junhwan Kim, Seunghyun Kim, Yesin Ryu, Saeid Gorgin, Jungrae Kim

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

As DRAM scales to higher density and I/O speeds, ensuring data correctness becomes increasingly difficult. Industry has responded with a three-layer stack—on-die ECC (O-ECC), link ECC (L-ECC), and system ECC (S-ECC)—but these layers have evolved independently, often duplicating redundancy, leaving coverage gaps, and occasionally interfering. We propose Cerberus, a cross-layer ECC co-design that unifies protection across device, link, and system while preserving each layer’s native role. At its core is an Encode-Once, Decode-Many (EODM) architecture: the controller performs a single encoding whose redundancy is reused by L-ECC for immediate write-path detection/retry, by O-ECC for in-device repair on reads, and by S-ECC for strong end-to-end recovery. Cerberus jointly designs complementary parity/syndrome structures, orders decoders and allocates the correction budget to prevent miscorrection amplification, and enables selective correction under tight redundancy constraints. Our evaluations show improved resilience to clustered and peripheral faults while reducing redundancy overhead, underscoring the importance of coordinated cross-layer protection for next-generation memory systems, such as custom HBMs.

## 中文摘要

随着 DRAM 向更高密度和更高 I/O 速度扩展，确保数据正确性变得愈发困难。业界采用三层堆栈来应对——片内 ECC（O-ECC）、链路 ECC（L-ECC）和系统 ECC（S-ECC）——但这些层独立演进，常常重复冗余、留下覆盖缺口，有时甚至相互干扰。我们提出 Cerberus，一种跨层 ECC 协同设计方案，统一了设备、链路和系统层面的保护，同时保留每一层的原生角色。其核心是一次编码、多次解码（EODM）架构：控制器执行一次编码，其冗余被 L-ECC 用于写路径即时检测/重试、被 O-ECC 用于读路径片内修复、被 S-ECC 用于强大的端到端恢复。Cerberus 联合设计了互补的奇偶校验/校正子结构，对解码器进行排序并分配纠错预算以防止误纠放大，并在严格的冗余约束下实现选择性纠错。我们的评估表明，在降低冗余开销的同时，增强了对集群故障和外围故障的韧性，突显了为下一代内存系统（如定制 HBM）进行协调的跨层保护的重要性。

## 代码与研究制品

论文对应的代码或实验材料链接：

- [代码仓库：99june18/Cerberus](https://github.com/99june18/Cerberus)

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 1A](index.md) · [返回 ISCA 2026](../index.md)
