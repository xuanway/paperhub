---
title: "A4: Microarchitecture-Aware LLC Management for Datacenter Servers with Emerging I/O Devices"
description: "ISCA 2025 · Session 4C · A4：面向新兴 I/O 设备数据中心服务器的微架构感知 LLC 管理"
tags:
  - "ISCA2025"
  - "Session 4C"
  - "Datacenter & Cloud"
---

# A4: Microarchitecture-Aware LLC Management for Datacenter Servers with Emerging I/O Devices

**中文标题：** A4：面向新兴 I/O 设备数据中心服务器的微架构感知 LLC 管理

**所属 Session：** [Session 4C](index.md) · [ISCA 2025](../index.md)

**作者：** Haneul Park, Jiaqi Lou, Sangjin Lee, Yifan Yuan, KyoungSoo Park, Yongseok Son, Ipoom Jeong, Nam Sung Kim

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731114) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

In modern server CPUs, the Last-Level Cache (LLC) serves not only as a victim cache for higher-level private caches but also as a buffer for low-latency DMA transfers between CPU cores and I/O devices through Direct Cache Access (DCA). However, prior work has shown that high-bandwidth network-I/O devices can rapidly flood the LLC with packets, often causing significant contention with co-running workloads. One step further, this work explores hidden microarchitectural properties of the Intel Xeon CPUs, un- covering two previously unrecognized LLC contentions triggered by emerging high-bandwidth I/O devices. Specifically, (C1) DMA- written cache lines in LLC ways designated for DCA (referred to as DCA ways) are migrated to certain LLC ways (denoted as inclu- sive ways) when accessed by CPU cores, unexpectedly contending with non-I/O cache lines within the inclusive ways. In addition, (C2) high-bandwidth storage-I/O devices, which are increasingly common in datacenter servers, benefit little from DCA while con- tending with (latency-sensitive) network-I/O devices within DCA ways. To this end, we present A4, a runtime LLC management framework designed to alleviate both (C1) and (C2) among diverse co-running workloads, using a hidden knob and other hardware features implemented in those CPUs. Additionally, we demonstrate that A4 can also alleviate other previously known network-I/O- driven LLC contentions. Overall, it improves the performance of latency-sensitive, high-priority workloads by 51% without notably compromising that of low-priority workloads.

## 中文摘要

在现代服务器 CPU 中，末级高速缓存 (LLC) 不仅充当高级私有高速缓存的牺牲缓存，还充当通过直接高速缓存访问 (DCA) 在 CPU 内核和 I/O 设备之间进行低延迟 DMA 传输的缓冲区。然而，先前的研究表明，高带宽网络 I/O 设备可能会快速向 LLC 发送大量数据包，这通常会导致与共同运行的工作负载发生严重争用。更进一步，这项工作探索了英特尔至强 CPU 隐藏的微架构属性，揭示了由新兴高带宽 I/O 设备引发的两个先前未被识别的 LLC 争用。具体地，(C1)指定用于DCA的LLC路(称为DCA路)中的DMA写入的高速缓存线在被CPU核访问时迁移到某些LLC路(表示为包含路)，意外地与包含路内的非I/O高速缓存线竞争。此外，在数据中心服务器中越来越常见的 (C2) 高带宽存储 I/O 设备在与 DCA 路内的（延迟敏感的）网络 I/O 设备竞争时，几乎无法从 DCA 中获益。为此，我们推出了 A4，这是一个运行时 LLC 管理框架，旨在使用未公开的配置参数和这些 CPU 中实现的其他硬件功能来减轻不同共同运行工作负载之间的 (C1) 和 (C2) 负担。此外，我们证明 A4 还可以缓解其他先前已知的网络 I/O 驱动的 LLC 争用。总体而言，它将延迟敏感的高优先级工作负载的性能提高了 51%，而不会明显影响低优先级工作负载的性能。

## 英文关键词

Direct Cache Access, Non-inclusive caches, Last-Level Cache, Datacenter server

## 中文关键词

直接缓存访问（DCA）, 非包含式缓存, 末级缓存（LLC）, 数据中心服务器

## 代码与研究制品

- [代码仓库](https://github.com/ece-fast-lab/ISCA-2025-A4)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731114)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 4C](index.md) · [返回 ISCA 2025](../index.md)
