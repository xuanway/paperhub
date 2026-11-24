---
title: "ZRAID: Leveraging Zone Random Write Area (ZRWA) for Alleviating Partial Parity Tax in ZNS RAID"
description: "ASPLOS 2025 · Session 4B · ZRAID：利用分区随机写区域（ZRWA）缓解 ZNS RAID 中的部分校验开销"
tags:
  - "ASPLOS2025"
  - "Session 4B"
  - "Memory & Storage"
---

# ZRAID: Leveraging Zone Random Write Area (ZRWA) for Alleviating Partial Parity Tax in ZNS RAID

**中文标题：** ZRAID：利用分区随机写区域（ZRWA）缓解 ZNS RAID 中的部分校验开销

**所属 Session：** [Session 4B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Minwook Kim (Seoul National University), Seongyeop Jeong (Seoul National University), Jin-Soo Kim (Seoul National University)

**单位：** Seoul National University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707248) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

The Zoned Namespace (ZNS) SSD is an innovative technology that aims to mitigate the block interface tax associated with conventional SSDs. However, constructing a RAID system using ZNS SSDs presents a significant challenge in managing partial parity for incomplete stripes. Previous research permanently logs partial parity in a limited number of reserved zones, which not only creates bottlenecks in throughput but also exacerbates write amplification, thereby reducing the device's lifetime. We refer to these inefficiencies as the partial parity tax. In this paper, we present ZRAID, a software ZNS RAID layer that leverages the newly added Zone Random Write Area (ZRWA) feature in the ZNS Command Set, to alleviate partial parity tax. ZRWA enables in-place updates within a confined area near the write pointer. ZRAID temporarily stores partial parity within the ZRWA of data zones. Thus, partial parity writes are distributed across multiple data zones, effectively eliminating throughput bottlenecks. Furthermore, any expired partial parity in the ZRWA is overwritten by subsequent data, avoiding unnecessary flash writes. With the introduction of ZRWA, ZRAID can leverage general schedulers, overcoming the queue depth limitations of ZNScompatible schedulers. Our evaluation with actual ZNS SSDs demonstrates a significant improvement in write throughput: up to 34.7% in the fio microbenchmark, and an average of 14.5% in db_bench on RocksDB, along with up to a 1.6x reduction in flash write amplification.

## 中文摘要

分区命名空间（Zoned Namespace，ZNS）SSD 是一项创新技术，旨在缓解传统 SSD 所伴随的块接口开销。然而，使用 ZNS SSD 构建 RAID 系统时，如何管理不完整条带的部分校验是一项重大挑战。已有研究将部分校验永久记录在数量有限的预留分区中，这不仅造成吞吐量瓶颈，还加剧了写放大，从而缩短设备寿命。我们将这些低效之处称为部分校验开销。本文提出 ZRAID，这是一个软件 ZNS RAID 层，利用 ZNS 命令集中新增的分区随机写区域（Zone Random Write Area，ZRWA）特性来缓解部分校验开销。ZRWA 支持在写指针附近的受限区域内进行原地更新。ZRAID 将部分校验临时存储在数据分区的 ZRWA 内。因此，部分校验写被分散到多个数据分区，有效消除了吞吐量瓶颈。此外，ZRWA 中任何已过期的部分校验都会被后续数据覆盖，从而避免不必要的闪存写入。随着 ZRWA 的引入，ZRAID 可以使用通用调度器，克服了兼容 ZNS 的调度器在队列深度上的限制。我们在真实 ZNS SSD 上的评估表明写吞吐量显著提升：在 fio 微基准测试中最高提升 34.7%，在 RocksDB 上的 db_bench 中平均提升 14.5%，同时闪存写放大最多降低 1.6 倍。

## 英文关键词

Zoned Namespaces, RAID, Zone Random Write Area (ZRWA), Partial Parity

## 中文关键词

分区命名空间；RAID；分区随机写区域（ZRWA）；部分校验

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707248)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 4B](index.md) · [返回 ASPLOS 2025](../index.md)
