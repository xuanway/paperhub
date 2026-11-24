---
title: "Symbiosis: The Art of Application and Kernel Cache Cooperation"
description: "FAST 2024 · Caching · 第 51–70 页"
tags:
  - "FAST2024"
  - "Caching"
---

# Symbiosis: The Art of Application and Kernel Cache Cooperation

**中文标题**：Symbiosis：应用与内核缓存协作的艺术

**Session**：Caching · 2024-02-27 14:00–15:15 · Chair：Carl Waldspurger（Carl Waldspurger Consulting）

**作者**：Yifan Dai, Jing Liu, Andrea Arpaci-Dusseau, and Remzi Arpaci-Dusseau, University of Wisconsin—Madison

**会议**：FAST 2024 · Santa Clara, CA · 第 51–70 页

**USENIX 页面**：[https://www.usenix.org/conference/fast24/presentation/dai](https://www.usenix.org/conference/fast24/presentation/dai)

**论文 PDF**：[fast24-dai.pdf](https://www.usenix.org/system/files/fast24-dai.pdf)

---

## 英文摘要

We introduce *Symbiosis*, a framework for key-value storage systems that dynamically configures application and kernel cache sizes to improve performance. We integrate Symbiosis into three production systems — LevelDB, WiredTiger, and RocksDB — and, through a series of experiments on various read-heavy workloads and environments, show that Symbiosis improves performance by 1.5× on average and over 5× at best compared to static configurations, across a wide range of synthetic and real-world workloads.

## 中文摘要

我们提出 *Symbiosis*，一个面向键值存储系统的框架，它动态配置应用缓存和内核缓存的大小以提升性能。我们将 Symbiosis 集成到三个生产系统——LevelDB、WiredTiger 和 RocksDB——并通过在各种读密集型负载和环境上的一系列实验表明，与静态配置相比，Symbiosis 在广泛的合成和真实负载上将性能平均提升 1.5 倍，最高提升超过 5 倍。
