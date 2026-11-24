---
title: "Rearchitecting Buffered I/O in the Era of High-Bandwidth SSDs"
description: "FAST 2026 · Tiering, Mobile, and SSDs · 第 579–596 页"
tags:
  - "FAST2026"
  - "Tiering, Mobile, and SSDs"
---

# Rearchitecting Buffered I/O in the Era of High-Bandwidth SSDs

**中文标题**：高带宽 SSD 时代下缓冲 I/O 的重新架构

**Session**：Tiering, Mobile, and SSDs · 2026-02-26 10:50–12:30 · Chair：Vasily Tarasov（IBM Research）

**作者**：Yekang Zhan, Tianze Wang, Zheng Peng, Haichuan Hu, Jiahao Wu, Xiangrui Yang, and Qiang Cao, Huazhong University of Science and Technology; Hong Jiang, University of Texas at Arlington; Jie Yao, Huazhong University of Science and Technology

**会议**：FAST 2026 · Santa Clara, CA · 第 579–596 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/zhan](https://www.usenix.org/conference/fast26/presentation/zhan)

**论文 PDF**：[fast26-zhan.pdf](https://www.usenix.org/system/files/fast26-zhan.pdf)

---

## 英文摘要

Buffered I/O via page cache has been prevalently used by applications for decades due to its user-friendliness and high performance. However, the existing buffered I/O architecture fails to effectively utilize high-bandwidth Solid-State Drives (SSDs) caused by 1) costly page caching overused for buffering all incoming writes in the critical path, 2) the limited concurrency of page management, and 3) the high read-before-write penalty for partial-page writes.

This paper rearchitects buffered I/O and proposes a write-scrap buffering approach (WSBuffer) to remove the aforementioned shackles of buffered I/O on writes to proactively exploit fast SSDs while retaining all the advantages of buffered I/O on reads. WSBuffer first presents a novel memory-page buffering structure, scrap buffer, to efficiently buffer SSD-I/O unfriendly writes and expensive partial-page writes. WSBuffer further proposes a buffer-minimized data access mechanism to partially buffer small and unaligned parts of user writes via the scrap buffer while directly sending large and aligned parts to underlying SSDs. Finally, WSBuffer devises an opportunistic two-stage dirty-data flushing mechanism and a concurrent page management mechanism to achieve fluent and fast dirty-data flushing. The experimental results show that WSBuffer outperforms Linux file systems of EXT4, F2FS, BTRFS and XFS, as well as the state-of-the-art buffered I/O optimization of ScaleCache by up to 3.91X and 82.80X in throughput and latency respectively.

## 中文摘要

数十年来，通过页缓存进行的缓冲 I/O 因其用户友好性和高性能而被应用广泛使用。然而，现有缓冲 I/O 架构无法有效利用高带宽固态硬盘（SSD），原因包括：1) 在关键路径上为缓冲所有传入写而过度使用代价高昂的页缓存；2) 页面管理的并发性有限；3) 部分页写入面临高昂的写前读惩罚。

本文重新架构缓冲 I/O，并提出一种写碎片缓冲方法（WSBuffer），以消除缓冲 I/O 在写方面的上述束缚，从而主动利用快速 SSD，同时保留缓冲 I/O 在读方面的全部优势。WSBuffer 首先提出一种新颖的内存页缓冲结构——碎片缓冲区（scrap buffer），以高效缓冲对 SSD I/O 不友好的写入和昂贵的部分页写入。WSBuffer 进一步提出一种缓冲区最小化的数据访问机制：通过碎片缓冲区部分缓冲用户写入中的小型和非对齐部分，同时将大型和对齐部分直接发送到底层 SSD。最后，WSBuffer 设计了一种机会式两阶段脏数据刷写机制和一种并发页面管理机制，以实现流畅快速的脏数据刷写。实验结果表明，与 EXT4、F2FS、BTRFS 和 XFS 等 Linux 文件系统以及最先进的缓冲 I/O 优化 ScaleCache 相比，WSBuffer 的吞吐量最多提升 3.91 倍，延迟最多降低 82.80 倍。
