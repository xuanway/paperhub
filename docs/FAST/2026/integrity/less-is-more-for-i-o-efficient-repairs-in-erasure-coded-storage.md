---
title: "LESS is More for I/O-Efficient Repairs in Erasure-Coded Storage"
description: "FAST 2026 · Integrity · 第 631–642 页"
tags:
  - "FAST2026"
  - "Integrity"
---

# LESS is More for I/O-Efficient Repairs in Erasure-Coded Storage

**中文标题**：LESS：面向纠删码存储 I/O 高效修复的少即是多方案

**Session**：Integrity · 2026-02-26 14:00–15:20 · Chair：Gala Yadgar（Technion—Israel Institute of Technology）

**作者**：Keyun Cheng, The Chinese University of Hong Kong; Guodong Li, Shandong University; Xiaolu Li, Huazhong University of Science and Technology; Sihuang Hu, Shandong University; Patrick P. C. Lee, The Chinese University of Hong Kong

**会议**：FAST 2026 · Santa Clara, CA · 第 631–642 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/cheng](https://www.usenix.org/conference/fast26/presentation/cheng)

**论文 PDF**：[fast26-cheng.pdf](https://www.usenix.org/system/files/fast26-cheng.pdf)

---

## 英文摘要

I/O efficiency is critical for erasure-coded repair performance in modern distributed storage. We propose LESS, a family of repair-friendly erasure code constructions that reduces both the amount of data accessed and the number of I/O seeks in single-block repairs, while ensuring balanced reductions across blocks. LESS layers multiple extended sub-stripes formed by widely deployed Reed-Solomon coding, and is configurable to balance the trade-off between the amount of data accessed and I/O seeks. Evaluation shows that LESS on HDFS reduces both single-block repair and full-node recovery times compared to state-of-the-art I/O-optimal erasure codes.

## 中文摘要

I/O 效率对现代分布式存储中纠删码修复性能至关重要。我们提出 LESS，一族对修复友好的纠删码构造，它在单块修复中同时减少访问的数据量和 I/O 寻道次数，并确保各块之间的削减保持均衡。LESS 将多个由广泛部署的 Reed-Solomon 编码形成的扩展子条带分层组合，并可配置以在访问数据量与 I/O 寻道之间取得权衡。评估表明，与最先进的 I/O 最优纠删码相比，HDFS 上的 LESS 同时缩短了单块修复时间和全节点恢复时间。
