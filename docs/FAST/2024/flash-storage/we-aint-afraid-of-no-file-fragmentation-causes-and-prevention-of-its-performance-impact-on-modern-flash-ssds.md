---
title: "We Ain't Afraid of No File Fragmentation: Causes and Prevention of Its Performance Impact on Modern Flash SSDs"
description: "FAST 2024 · Flash Storage · 第 193–208 页"
tags:
  - "FAST2024"
  - "Flash Storage"
---

# We Ain't Afraid of No File Fragmentation: Causes and Prevention of Its Performance Impact on Modern Flash SSDs

**中文标题**：我们不惧怕文件碎片化：现代闪存 SSD 上碎片化性能影响的原因与预防

**Session**：Flash Storage · 2024-02-28 09:00–10:15 · Chair：Jooyoung Hwang（Samsung Electronics）

**作者**：Yuhun Jun, Sungkyunkwan University and Samsung Electronics Co., Ltd.; Shinhyun Park, Sungkyunkwan University; Jeong-Uk Kang, Samsung Electronics Co., Ltd.; Sang-Hoon Kim, Ajou University; Euiseong Seo, Sungkyunkwan University

**会议**：FAST 2024 · Santa Clara, CA · 第 193–208 页

**获奖**：Best Paper

**USENIX 页面**：[https://www.usenix.org/conference/fast24/presentation/jun](https://www.usenix.org/conference/fast24/presentation/jun)

**论文 PDF**：[fast24-jun.pdf](https://www.usenix.org/system/files/fast24-jun.pdf)

---

## 英文摘要

A few studies reported that fragmentation still adversely affects the performance of flash solid-state disks (SSDs) particularly through request splitting. This research investigates the fragmentation-induced performance degradation across three levels: kernel I/O path, host-storage interface, and flash memory accesses in SSDs. Our analysis reveals that, contrary to assertions in existing literature, the primary cause of the degraded performance is not due to request splitting but stems from a significant increase in die-level collisions. In SSDs, when other writes come between writes of neighboring file blocks, the file blocks are not placed on consecutive dies, resulting in random die allocation. This randomness escalates the chances of die-level collisions, causing deteriorated read performance later. We also reveal that this may happen when a file is overwritten. To counteract this, we propose an NVMe command extension combined with a page-to-die allocation algorithm designed to ensure that contiguous blocks always land on successive dies, even in the face of file fragmentation or overwrites. Evaluations with commercial SSDs and an SSD emulator indicate that our approach effectively curtails the read performance drop arising from both fragmentation and overwrites, all without the need for defragmentation. Representatively, when a 162 MB SQLite database was fragmented into 10,011 pieces, our approach limited the performance drop to 3.5%, while the conventional system experienced a 40% decline.

## 中文摘要

一些研究报道，碎片化仍会通过请求拆分等方式对闪存固态硬盘（SSD）的性能产生不利影响。本研究从三个层面考察碎片化引起的性能下降：内核 I/O 路径、主机—存储接口以及 SSD 内的闪存访问。我们的分析表明，与现有文献的断言相反，性能下降的主要原因并非请求拆分，而是源于 die 级冲突的显著增加。在 SSD 中，当其他写入插入到相邻文件块的写入之间时，这些文件块不会被放置在连续的 die 上，从而导致随机 die 分配。这种随机性提高了 die 级冲突的概率，进而导致后续读性能恶化。我们还揭示，当文件被覆盖写时也可能发生这种情况。为应对这一问题，我们提出一种 NVMe 命令扩展，并结合页到 die 的分配算法，旨在确保即使面对文件碎片化或覆盖写，连续块也始终落在连续的 die 上。在商用 SSD 和 SSD 仿真器上的评估表明，我们的方法有效抑制了碎片化和覆盖写引起的读性能下降，且无需碎片整理。具有代表性的是，当一个 162 MB 的 SQLite 数据库被碎片化为 10,011 个片段时，我们的方法将性能下降限制在 3.5%，而传统系统则下降了 40%。
