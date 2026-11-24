---
title: "OPIMQ: Order Preserving IO stack for Multi-Queue Block Device"
description: "FAST 2025 · Security, Integrity, and Consistency · 用 cache barrier 保住多队列并行度，IO 栈吞吐提升 2.9 倍"
tags:
  - "FAST2025"
  - "Security, Integrity, and Consistency"
  - "storage order"
  - "multi-queue block device"
---

# OPIMQ: Order Preserving IO stack for Multi-Queue Block Device

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">多队列块设备为每核设置请求队列，但文件系统要的顺序只能靠 Transfer-and-Flush 串行化。OPIMQ 以 Epoch Pinning 与 Dual-Stream Write 保住流内外顺序，FTL 按存储顺序更新映射，三个负载快 2.9、2.8、2.9 倍。</p>
<p class="paper-seo-summary__tags">FAST 2025 · Security, Integrity, and Consistency</p>
</div>

**中文标题**：OPIMQ：面向多队列块设备的保序 I/O 栈

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/kim-jieun](https://www.usenix.org/conference/fast25/presentation/kim-jieun)

**论文 PDF**：[fast25-kim-jieun.pdf](https://www.usenix.org/system/files/fast25-kim-jieun.pdf)

**作者**：Jieun Kim（Korea Advanced Institute of Science and Technology (KAIST)）；Joontaek Oh（University of Wisconsin–Madison）；Juwon Kim、Seung Won Yoo、Youjip Won（Korea Advanced Institute of Science and Technology (KAIST)）

**会议**：FAST 2025 · Santa Clara, CA · 第 425–439 页

**Session**：Security, Integrity, and Consistency · 2025-02-26 14:00–15:40 · Chair：Hyungon Moon（UNIST (Ulsan National Institute of Science and Technology)）

**所属 Session**：[Security, Integrity, and Consistency](index.md) · [FAST 2025](../index.md)

**关键词**：storage order, multi-queue block device, cache barrier, flash translation layer, NVMe, journaling

---

## 英文摘要

In this work, we address the issue of ensuring the storage order in the multi-queue IO stack and propose OPIMQ , an Order-Preserving IO Stack for Multi-Queue Block Devices. OPIMQ consists of four key components: Epoch Pinning , Dual-Stream Write , Order-Preserving Mapping Table Update and Sibling-aware Delayed Mapping . With Epoch Pinning, we can preserve intra-stream order dependency across different queues. With Dual-Stream Write, we can preserve the inter-stream order dependency across different threads. With Order-Preserving Mapping Table Update, FTL can update the mapping table with respect to the storage order. With Sibling-Aware Delayed Mapping, FTL can update the mapping table only when the dual-stream write satisfies the storage order in both streams. Linux IO stack with OPIMQ outperforms the vanilla Linux IO stack by 2.9×, 2.8×, and 2.9× under Filebench varmail, dbench, and sysbench, respectively. The order-preserving FTL accompanies a 1.1% performance penalty in address translation compared to legacy FTL.

## 中文摘要

本文解决多队列 I/O 栈中保证存储顺序的问题，提出 OPIMQ——一种面向多队列块设备的保序 I/O 栈。OPIMQ 由四个关键部分组成：Epoch Pinning、Dual-Stream Write、Order-Preserving Mapping Table Update 与 Sibling-Aware Delayed Mapping。借助 Epoch Pinning，可以在不同队列之间保持流内顺序依赖；借助 Dual-Stream Write，可以在不同线程之间保持流间顺序依赖；借助 Order-Preserving Mapping Table Update，FTL 可以按存储顺序更新映射表；借助 Sibling-Aware Delayed Mapping，FTL 只在双流写满足两条流的存储顺序时才更新映射表。带 OPIMQ 的 Linux I/O 栈在 Filebench varmail、dbench 与 sysbench 下分别比原生 Linux I/O 栈快 2.9 倍、2.8 倍与 2.9 倍。与旧式 FTL 相比，保序 FTL 在地址转换上带来 1.1% 的性能损失。

## 一句话总结

> 存储顺序不必靠等数据落地来保证：把 cache barrier 下沉到 FTL 的映射表更新顺序里，多队列的并行度就能保住。

## 研究背景与问题

- **顺序是应用的硬需求**：文件系统 journaling、log-structured 文件系统、soft updates 与数据库事务，都要求一组块按指定顺序变得持久。
- **现状代价高昂**：存储设备几十年间把性能提升了 1800 倍（300 IOPS 的 HDD 到 550K IOPS 的 Intel Optane 900P），靠的正是多命令队列与多通道并行；但应用只能把写请求与 Transfer-and-Flush 交织，等前一批数据传到设备并持久化后才发下一条，随机写吞吐只剩理想值的 3.4%。
- **单队列方案搬不过来**：BarrierFS 用 cache barrier 命令消除了 Transfer-and-Flush，但只在 eMMC、SATA 这类单队列栈里有效；现代栈是主机多请求队列加设备多命令队列，NVMe 可导出 64K 个 SQ/CQ 对、每个队列 64K 条命令。
- **多队列的既有尝试各有偏差**：HORAE 把顺序强加给无关请求，MQFS、ccNVMe 则会造成请求队列与 CPU 核之间的严重负载失衡。

## 核心贡献

- **把 cache barrier 引入多队列栈**：该命令此前只在移动端单队列存储中生效，OPIMQ 让它在服务器与数据中心的多队列 SSD 上可用。
- **Epoch Pinning**：解决同一线程被迁移到其他核后，同一条流的请求落到不同队列所导致的流内顺序丢失。
- **Dual-Stream Write**：让一条写同时属于两条流，从而在设备侧统一裁决不同线程之间的流间顺序依赖。
- **顺序保持的 FTL（OPFTL）**：用 Order-Preserving Mapping Table Update 与 Sibling-Aware Delayed Mapping，使数据块的持久化与映射表更新都服从存储顺序。

## 方法与技术要点

- **问题建模**：流（stream）指同一线程发出的一组 IO，需排序的写称为 ordered write；跨队列依赖分两类，intra-stream 是同一条流内跨队列，inter-stream 是跨线程。
- **Epoch Pinning**：把同一 epoch 的请求固定投递到同一请求队列，即使线程被调度到别的核也不改变归属，从而在不禁止线程迁移的前提下保住流内顺序。
- **Dual-Stream Write**：特殊的写请求同时挂在两条流上，使跨流顺序约束在设备侧被一并满足，而不是靠主机侧等待。
- **OPFTL 的映射更新**：SSD 可以按任意顺序把写回缓存刷入 flash，但映射表项必须按存储顺序更新，于是数据块对外可见的顺序就等于应用要求的顺序。
- **Sibling-Aware Delayed Mapping**：只有当双流写在两条流上的顺序都满足时才提交映射，避免一条流先可见、另一条流后可见；实现基于 Linux 5.18.18，在 Samsung 980 Pro 与 Cosmos OpenSSD（230 GB、8 通道、单核）上验证。

## 评估与主要结果

- **动机实验**：4 KB 随机写、线程与命令队列从 1 增到 40 时，Transfer-and-Flush 只能达到理想吞吐的 3.4%，单队列 Wait-On-Dispatch 为 47%。
- **整体吞吐与扩展性**：相对原生 Linux 栈，OPIMQ 在 Filebench varmail 与 dbench、sysbench 上分别提升 2.9 倍、2.8 倍、2.9 倍；20 线程 4 KB 写加 fsync 时达 112K IOPS（ccNVMe 为 57K IOPS），40 核上平均 CPU 利用率 OPIMQ 为 22%、MQFS 为 34%，负载分布更均匀。
- **FTL 代价**：OPFTL 相对页映射 FTL 吞吐低 1.05%（1.89 对 1.91 Kops/s），地址转换延迟同为 2.65 µs，即顺序保证的代价约 1.1%。
- **Epoch 影响**：在 varmail、dbench、sysbench 中 99.99% 的 epoch 只含一个请求，epoch 分裂次数分别为 6、0、0，因此 Epoch Pinning 几乎不改变各提交队列的负载分布。

## 代码与研究制品

- [代码仓库](https://github.com/ESOS-Lab/OPIMQ)

[返回 Security, Integrity, and Consistency](index.md) · [返回 FAST 2025](../index.md)
