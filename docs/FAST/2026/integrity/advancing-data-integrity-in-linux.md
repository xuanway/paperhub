---
title: "Advancing Data Integrity in Linux"
description: "FAST 2026 · Integrity · 第 643–658 页"
tags:
  - "FAST2026"
  - "Integrity"
---

# Advancing Data Integrity in Linux

**中文标题**：提升 Linux 中的数据完整性

**Session**：Integrity · 2026-02-26 14:00–15:20 · Chair：Gala Yadgar（Technion—Israel Institute of Technology）

**作者**：Anuj Gupta, Samsung Semiconductor; Christoph Hellwig, unaffiliated; Kanchan Joshi, Vikash Kumar, and Javier Gonzalez, Samsung Semiconductor; Roshan R Nair, EPFL; Jinyoung Choi, Samsung Semiconductor

**会议**：FAST 2026 · Santa Clara, CA · 第 643–658 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/gupta](https://www.usenix.org/conference/fast26/presentation/gupta)

**论文 PDF**：[fast26-gupta.pdf](https://www.usenix.org/system/files/fast26-gupta.pdf)

---

## 英文摘要

Standalone hardware-only or software-only methods fail to provide comprehensive coverage in detecting data corruption. End-to-end data protection (E2EDP) addresses this by carrying per-block protection information (PI) throughout the I/O stack, from the application through the system software to the storage device. Although devices have supported PI for more than a decade, Linux remains incomplete in its support and utilization of these capabilities.

This paper closes two fundamental gaps in the mainline Linux kernel and introduces a PI-aware filesystem design with implementation and evaluation. First, we add a new *io_uring* interface that allows applications to exchange integrity metadata alongside the data. Second, we add flexible PI placement in Linux’s *block-integrity* enabling support for a device configuration that was otherwise rejected. Finally, we introduce *Filesystem Protection Information (FS-PI)*, a PI-aware design direction in which filesystems generate and verify integrity metadata directly while leveraging PI-capable hardware. We implement FS-PI in two major filesystems: in *XFS*, FS-PI introduces native data checksumming, extending data-integrity guarantees for the first time; in *BTRFS*, FS-PI replaces the checksum tree with a lightweight path that reduces metadata traffic, write amplification, and device wear.

We evaluated the cost and gains of FS-PI in BTRFS and XFS. The evaluation shows that FS-PI improves BTRFS performance by 26%, reduces host CPU utilization by 58%, and reduces device writes by 52%, extending SSD lifetime by 23%.

## 中文摘要

仅依赖硬件的独立方法或仅依赖软件的独立方法都无法在检测数据损坏方面提供全面覆盖。端到端数据保护（E2EDP）通过在整个 I/O 栈中携带逐块保护信息（PI）来解决这一问题，即从应用经过系统软件一直到存储设备。尽管设备支持 PI 已超过十年，但 Linux 在支持和利用这些能力方面仍不完整。

本文弥补了主线 Linux 内核中的两个根本性缺口，并引入一种 PI 感知的文件系统设计，同时给出实现与评估。首先，我们新增一个 *io_uring* 接口，使应用能够随数据一起交换完整性元数据。其次，我们在 Linux 的 *block-integrity* 中新增灵活的 PI 放置方式，从而支持原本会被拒绝的设备配置。最后，我们引入 *文件系统保护信息（FS-PI）*，这是一种 PI 感知的设计方向：文件系统在利用支持 PI 的硬件的同时，直接生成并验证完整性元数据。我们在两个主流文件系统中实现了 FS-PI：在 *XFS* 中，FS-PI 引入原生数据校验和，首次扩展了数据完整性保证；在 *BTRFS* 中，FS-PI 用轻量级路径替代校验和树，从而减少元数据流量、写放大和设备磨损。

我们在 BTRFS 和 XFS 中评估了 FS-PI 的成本与收益。评估表明，FS-PI 将 BTRFS 性能提升 26%，将主机 CPU 使用率降低 58%，并将设备写入减少 52%，从而将 SSD 寿命延长 23%。
