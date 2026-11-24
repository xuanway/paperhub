---
title: "I/O in a Flash: Evolution of ONTAP to Low-Latency SSDs"
description: "FAST 2024 · Flash Storage · 第 177–192 页"
tags:
  - "FAST2024"
  - "Flash Storage"
---

# I/O in a Flash: Evolution of ONTAP to Low-Latency SSDs

**中文标题**：闪存中的 I/O：ONTAP 向低延迟 SSD 的演进

**Session**：Flash Storage · 2024-02-28 09:00–10:15 · Chair：Jooyoung Hwang（Samsung Electronics）

**作者**：Matthew Curtis-Maury, Ram Kesavan, Bharadwaj V R, Nikhil Mattankot, Vania Fang, Yash Trivedi, Kesari Mishra, and Qin Li, NetApp, Inc

**会议**：FAST 2024 · Santa Clara, CA · 第 177–192 页

**论文类型**：Deployed-Systems Paper

**USENIX 页面**：[https://www.usenix.org/conference/fast24/presentation/curtis-maury](https://www.usenix.org/conference/fast24/presentation/curtis-maury)

**论文 PDF**：[fast24-curtis-maury.pdf](https://www.usenix.org/system/files/fast24-curtis-maury.pdf)

---

## 英文摘要

Flash-based persistent storage media are capable of sub-millisecond latency I/O. However, a storage architecture optimized for spinning drives may contain software delays that make it impractical for use with such media. The NetApp® ONTAP® storage system was designed originally for spinning drives, and needed alterations before it was productized as an all-SSD system. In this paper, we focus on the changes made to the read I/O path over the last several years, which have been crucial to this transformation, and present them in chronological fashion together with the associated performance analysis.

## 中文摘要

基于闪存的持久存储介质能够提供亚毫秒级延迟的 I/O。然而，为旋转磁盘优化的存储架构可能包含软件延迟，使其不适用于此类介质。NetApp® ONTAP® 存储系统最初是为旋转磁盘设计的，在作为全 SSD 系统产品化之前需要进行改造。本文聚焦过去几年对读 I/O 路径所做的改变——这些改变对这一转型至关重要——并按时序呈现这些改变及相关的性能分析。
