---
title: "CXL AnySSD: A Composable CXL SSD Using a CXL Type-2 Device and Any SSDs"
description: "MICRO 2026 · Session 6D · CXL AnySSD：利用 CXL Type-2 设备与任意 SSD 构建可组合 CXL SSD"
tags:
  - "MICRO2026"
  - "CXL"
  - "Storage"
---

# CXL AnySSD: A Composable CXL SSD Using a CXL Type-2 Device and Any SSDs

**中文标题：** CXL AnySSD：利用 CXL Type-2 设备与任意 SSD 构建可组合 CXL SSD

**所属 Session：** [Session 6D](index.md) · [MICRO 2026](../index.md)

**作者：** Yang Zhou, Houxiang Ji, Bikrant Das Sharma, Jiyuan Zhang, Yu Li, Linjie Ma, Jaeyong Lee, Myoungjun Chun, Jihong Kim, Sudarsun Kannan, Nam Sung Kim

**来源：** MICRO 2026，pp. 2201–2215；[DOI](https://doi.org/10.1109/MICRO67795.2026.00152)

## 英文摘要

Using only DRAM to meet the memory capacity demanded by emerging applications has become increasingly expensive under various physical constraints of server platforms. While SSDs offer a lower cost/GB than DRAM, they incur high latency and CPU-cycle consumption when managed by the kernel because of page fault handling and I/O stack processing. To tackle this challenge, memory-semantic SSDs, also referred to as CXL SSDs, have been developed, exposing SSDs directly as byte-addressable memory through the emerging CXL interface, offering 59% lower latency than the kernel-managed SSD. Nonetheless, such CXL SSDs, integrating SSDs and DRAM as cache within a single physical device, do not allow us to flexibly choose the DRAM-SSD capacity ratio or SSDs with specific performance characteristics and capacities. In this paper, leveraging the hardware-driven Device-to-Host (D2H) and Device-to-Device (D2D) access capability of CXL Type-2 devices, we propose CXL AnySSD, a composable CXL SSD. By loosely coupling SSDs with DRAM, it can overcome the limitations of both kernel-managed SSDs and CXL SSDs described above. We built a hardware prototype of CXL AnySSD using a CXL Type-2 device and evaluate it using not only a microbenchmark but also vector database, key-value store, and graph applications. Our evaluation shows that CXL AnySSD can deliver 1.7x lower latency and comparable bandwidth to an industry CXL SSD when configured appropriately for a given workload. CXL AnySSD offers 3.1x and 1.1x higher QPS than the CXL SSD for the vector database and key-value store applications, respectively. Lastly, CXL AnySSD provides 19% lower execution time for the graph applications.

## 中文摘要

在服务器平台的各种物理限制下，仅使用 DRAM 来满足新兴应用所需的内存容量变得越来越昂贵。虽然 SSD 的每 GB 成本低于 DRAM，但由于缺页异常处理和 I/O 堆栈处理，由内核管理时它们会产生高时延和 CPU 周期消耗。为了应对这一挑战，开发了内存语义 SSD（也称为 CXL SSD），通过新兴的 CXL 接口将 SSD 直接暴露为字节可寻址内存，与内核管理的 SSD 相比，时延降低了 59%。尽管如此，此类CXL SSD将SSD和DRAM作为缓存集成在单个物理设备中，不允许我们灵活选择DRAM-SSD容量比或具有特定性能特征和容量的SSD。在本文中，利用CXL Type-2设备的硬件驱动的设备到主机（D2H）和设备到设备（D2D）访问能力，我们提出了CXL AnySSD，一种可组合的CXL SSD。通过将 SSD 与 DRAM 松散耦合，可以克服上述内核管理 SSD 和 CXL SSD 的限制。我们使用 CXL Type-2 设备构建了 CXL AnySSD 的硬件原型，并不仅使用微基准测试，还使用矢量数据库、键值存储和图形应用程序对其进行评估。我们的评估表明，当针对给定工作负载进行适当配置时，CXL AnySSD 可以将时延降低 1.7 倍，并提供与行业 CXL SSD 相当的带宽。对于矢量数据库和键值存储应用程序，CXL AnySSD 的 QPS 分别比 CXL SSD 高 3.1 倍和 1.1 倍。最后，CXL AnySSD 使图形应用程序的执行时间缩短了 19%。

## 中文关键词

CXL；CXL 固态硬盘；异构内存；可组合存储；Type-2 设备

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

## 来源核对说明

Artifact 附录明确标注“Publicly available?: No”，未提供公开代码下载地址。

[返回 Session 6D](index.md) · [MICRO 2026 主页](../index.md)
