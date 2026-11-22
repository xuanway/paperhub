---
title: "Hera: Eliminating the I/O Tax of RAID on High-Capacity SSDs"
description: "MICRO 2026 · Session 8B · Hera：消除大容量 SSD 上 RAID 的额外 I/O 开销"
tags:
  - "MICRO2026"
  - "Storage"
---

# Hera: Eliminating the I/O Tax of RAID on High-Capacity SSDs

**中文标题：** Hera：消除大容量 SSD 上 RAID 的额外 I/O 开销

**所属 Session：** [Session 8B](index.md) · [MICRO 2026](../index.md)

**作者：** Jian Chen, Congming Gao, Fan Yang, Qing Wang, Zhengzhi Xin, Yuhao Zhang, Youyou Lu, Jiwu Shu

**来源：** MICRO 2026，pp. 2924–2939；[DOI](https://doi.org/10.1109/MICRO67795.2026.00198)

## 英文摘要

Ultra-high-capacity (UHC) SSDs have become a cornerstone of modern storage arrays. However, their deployment introduces a critical bottleneck: the RAID reconstruction imposes a heavy I/O tax on the external PCIe bus, significantly prolonging recovery times and compromising both data durability and service availability. Fortunately, the internal architecture of UHC SSDs, which features high-density channel configurations (e.g., 16 or 32 channels), delivers an aggregate internal bandwidth that far exceeds the capacity of saturated external PCIe bus. Therefore, we propose to harness this underutilized internal resource to offload RAID-related operations. In this work, we present Hera, a novel SSD array framework that enables inter-SSD communication to exploit internal bandwidth for RAID tasks while reserving the host-facing PCIe bus exclusively for host requests. Hera is built upon Amphisbaena, a dual-interface SSD design equipped with a standard host interface and a dedicated inter-SSD port for peer-to-peer (P2P) data exchange. We evaluate Hera across RAID5 and RAID6 configurations, focusing on device reconstruction and partial stripe writes. Experimental results demonstrate that Hera reduces reconstruction time by more than 45% on average. Additionally, for partial stripe writes, Hera delivers up to 2× the write bandwidth of conventional RAID architectures.

## 中文摘要

超高容量 (UHC) SSD 已成为现代存储阵列的基石。然而，它们的部署引入了一个关键瓶颈：RAID重建对外部PCIe总线施加了沉重的I/O负担，显着延长了恢复时间并损害了数据持久性和服务可用性。幸运的是，UHC SSD 的内部架构具有高密度通道配置（例如 16 或 32 通道），可提供远远超过饱和外部 PCIe 总线容量的聚合内部带宽。因此，我们建议利用这一未充分利用的内部资源来卸载与 RAID 相关的操作。在这项工作中，我们提出了 Hera，一种新颖的 SSD 阵列框架，它使 SSD 之间的通信能够利用内部带宽来执行 RAID 任务，同时保留面向主机的 PCIe 总线专门用于主机请求。 Hera 基于 Amphisbaena 构建，这是一种双接口 SSD 设计，配备标准主机接口和用于点对点 (P2P) 数据交换的专用 SSD 间端口。我们跨 RAID5 和 RAID6 配置评估 Hera，重点关注设备重建和部分条带写入。实验结果表明，Hera 平均减少了 45% 以上的重建时间。此外，对于部分条带写入，Hera 可提供高达传统 RAID 架构 2 倍的写入带宽。

## 中文关键词

超高容量固态硬盘；磁盘冗余阵列；点对点互连；输入输出效率

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 8B](index.md) · [MICRO 2026 主页](../index.md)
