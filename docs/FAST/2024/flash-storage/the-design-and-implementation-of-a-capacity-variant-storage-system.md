---
title: "The Design and Implementation of a Capacity-Variant Storage System"
description: "FAST 2024 · Flash Storage · 第 159–176 页"
tags:
  - "FAST2024"
  - "Flash Storage"
---

# The Design and Implementation of a Capacity-Variant Storage System

**中文标题**：容量可变存储系统的设计与实现

**Session**：Flash Storage · 2024-02-28 09:00–10:15 · Chair：Jooyoung Hwang（Samsung Electronics）

**作者**：Ziyang Jiao and Xiangqun Zhang, Syracuse University; Hojin Shin and Jongmoo Choi, Dankook University; Bryan S. Kim, Syracuse University

**会议**：FAST 2024 · Santa Clara, CA · 第 159–176 页

**USENIX 页面**：[https://www.usenix.org/conference/fast24/presentation/jiao](https://www.usenix.org/conference/fast24/presentation/jiao)

**论文 PDF**：[fast24-jiao.pdf](https://www.usenix.org/system/files/fast24-jiao.pdf)

---

## 英文摘要

We present the design and implementation of a capacity-variant storage system (CVSS) for flash-based solid-state drives (SSDs). CVSS aims to maintain high performance throughout the lifetime of an SSD by allowing storage capacity to gracefully reduce over time, thus preventing fail-slow symptoms. The CVSS comprises three key components (1) CV-SSD, an SSD that minimizes write amplification and gracefully reduces its exported capacity with age; (2) CV-FS, a log-structured file system for elastic logical partition; and (3) CV-manager, a user-level program that orchestrates system components based on the state of the storage system. We demonstrate the effectiveness of CVSS with synthetic and real workloads, showing significant improvements in latency, throughput, and lifetime compared to a fixed-capacity storage system. Specifically, under real workloads, CVSS reduces the latency, improves the throughput, and extends the lifetime by 8–53%, 49–316%, and 268–327%, respectively.

## 中文摘要

我们提出一种面向基于闪存的固态硬盘（SSD）的容量可变存储系统（CVSS）的设计与实现。CVSS 旨在通过允许存储容量随时间优雅地减少，在整个 SSD 生命周期内保持高性能，从而防止 fail-slow 症状。CVSS 包含三个关键组件：(1) CV-SSD，一种最小化写放大并随老化优雅降低其导出容量的 SSD；(2) CV-FS，一种用于弹性逻辑分区的日志结构文件系统；(3) CV-manager，一个根据存储系统状态编排系统组件的用户级程序。我们使用合成和真实负载证明 CVSS 的有效性，与固定容量存储系统相比，其在延迟、吞吐量和寿命方面均有显著改善。具体而言，在真实负载下，CVSS 将延迟降低、吞吐量提升、寿命延长分别达到 8–53%、49–316% 和 268–327%。
