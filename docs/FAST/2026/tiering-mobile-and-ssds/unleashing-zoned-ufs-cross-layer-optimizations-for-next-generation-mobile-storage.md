---
title: "Unleashing Zoned UFS: Cross-Layer Optimizations for Next-Generation Mobile Storage"
description: "FAST 2026 · Tiering, Mobile, and SSDs · 第 527–542 页"
tags:
  - "FAST2026"
  - "Tiering, Mobile, and SSDs"
---

# Unleashing Zoned UFS: Cross-Layer Optimizations for Next-Generation Mobile Storage

**中文标题**：释放分区 UFS 的潜力：面向下一代移动存储的跨层优化

**Session**：Tiering, Mobile, and SSDs · 2026-02-26 10:50–12:30 · Chair：Vasily Tarasov（IBM Research）

**作者**：Jungae Kim, SK hynix Inc.; Jaegeuk Kim, Google; Kyu-Jin Cho, Seoul National University; Sungjin Park, Jinwoo Kim, Jieun Kim, and Iksung Oh, SK hynix Inc.; Chul Lee, Bart Van Assche, Daeho Jeong, and Konstantin Vyshetsky, Google; Jin-Soo Kim, Seoul National University

**会议**：FAST 2026 · Santa Clara, CA · 第 527–542 页

**论文类型**：Deployed-Systems Paper

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/kim-jungae](https://www.usenix.org/conference/fast26/presentation/kim-jungae)

**论文 PDF**：[fast26-kim-jungae.pdf](https://www.usenix.org/system/files/fast26-kim-jungae.pdf)

---

## 英文摘要

Zoned UFS (ZUFS) has emerged as a next-generation mobile storage technology that reduces the logical-to-physical (L2P) mapping overhead of conventional UFS (CUFS) by enforcing sequential writes within fixed-size zones. While the concept appears straightforward, deploying ZUFS in commercial smartphones introduces non-trivial challenges across the mobile storage stack. In this paper, we identify three key obstacles: managing limited SRAM across multiple open zones, ensuring end-to-end write ordering guarantees, and mitigating severe garbage collection overhead caused by large zones.

We address these challenges through cross-layer optimizations spanning device firmware, the SCSI/UFS driver, the block layer, F2FS, and Android framework: a dynamic device-side buffer management scheme that opportunistically shares SRAM, a write ordering mechanism that eliminates reordering hazards, and a proactive garbage collection framework that reclaims free space in the background. Evaluation on a commercial smartphone shows that ZUFS sustains over 2x higher write throughput under fragmentation and reduces mobile game loading time by 14% compared to CUFS, while maintaining stable read performance. These results demonstrate that ZUFS’s full potential can only be realized through coordinated redesign across the entire mobile storage stack.

## 中文摘要

分区 UFS（ZUFS）已成为一种下一代移动存储技术，它通过在固定大小的分区内强制顺序写入，降低传统 UFS（CUFS）的逻辑到物理（L2P）映射开销。虽然概念看似简单，但在商用智能手机中部署 ZUFS 会在移动存储栈的各个环节带来不小的挑战。本文识别出三个关键障碍：在多个打开的分区之间管理有限的 SRAM、确保端到端写顺序保证，以及缓解大分区导致的严重垃圾回收开销。

我们通过横跨设备固件、SCSI/UFS 驱动、块层、F2FS 和 Android 框架的跨层优化来应对这些挑战：一种机会式共享 SRAM 的动态设备端缓冲区管理方案、一种消除重排序风险的写顺序机制，以及一种在后台回收空闲空间的前瞻性垃圾回收框架。在商用智能手机上的评估表明，与 CUFS 相比，ZUFS 在碎片化情况下可维持超过 2 倍的写吞吐量，并将移动游戏加载时间缩短 14%，同时保持稳定的读性能。这些结果表明，只有通过整个移动存储栈的协同重新设计，才能充分发挥 ZUFS 的潜力。
