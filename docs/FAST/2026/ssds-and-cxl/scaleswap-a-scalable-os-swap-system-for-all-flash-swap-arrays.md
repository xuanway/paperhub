---
title: "ScaleSwap: A Scalable OS Swap System for All-Flash Swap Arrays"
description: "FAST 2026 · SSDs and CXL · 第 363–380 页"
tags:
  - "FAST2026"
  - "SSDs and CXL"
---

# ScaleSwap: A Scalable OS Swap System for All-Flash Swap Arrays

**中文标题**：ScaleSwap：面向全闪存交换阵列的可扩展操作系统交换系统

**Session**：SSDs and CXL · 2026-02-25 14:00–15:40 · Chair：Ethan Miller（University of California, Santa Cruz, and Pure Storage）

**作者**：Taehwan Ahn, Chanhyeong Yu, Sangjin Lee, and Yongseok Son, Chung-Ang University

**会议**：FAST 2026 · Santa Clara, CA · 第 363–380 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/ahn](https://www.usenix.org/conference/fast26/presentation/ahn)

**论文 PDF**：[fast26-ahn.pdf](https://www.usenix.org/system/files/fast26-ahn.pdf)

---

## 英文摘要

This paper presents a scalable OS swap system, ScaleSwap, designed to enhance core and SSD scalability on all-flash swap arrays. Specifically, ScaleSwap first enables a one-to-one swap model where each core exclusively manages its own swap resources, enabling core-centric swap in/out operations. Second, ScaleSwap devises opportunistic inter-core swap assistance, allowing each core to delegate swap metadata access to other cores as needed. Finally, ScaleSwap adopts core-affinity page and LRU management to mitigate LRU lock contention during swap in/out operations. We implement ScaleSwap in the Linux kernel and evaluate its performance on a 128-core machine with an all-flash swap array comprising eight NVMe SSDs. Our evaluation shows that ScaleSwap achieves up to 3.4× higher throughput and up to 11.5× lower average latency than the Linux swap system. Furthermore, ScaleSwap outperforms two prior systems, TMO and ExtMEM, by up to 64% and 5×, respectively.

## 中文摘要

本文提出 ScaleSwap，一个可扩展的操作系统交换系统，旨在提升全闪存交换阵列上的核心与 SSD 可扩展性。具体而言，ScaleSwap 首先实现一对一交换模型，使每个核心独占管理自己的交换资源，从而支持以核心为中心的换入/换出操作。其次，ScaleSwap 设计机会式核间交换协助机制，允许每个核心按需将交换元数据访问委托给其他核心。最后，ScaleSwap 采用核心亲和性的页面管理和 LRU 管理，以缓解换入/换出操作期间的 LRU 锁竞争。我们在 Linux 内核中实现 ScaleSwap，并在配备由八块 NVMe SSD 组成的全闪存交换阵列的 128 核机器上评估其性能。评估表明，与 Linux 交换系统相比，ScaleSwap 的吞吐量最高提升 3.4 倍，平均延迟最多降低 11.5 倍。此外，ScaleSwap 分别比 TMO 和 ExtMEM 这两个先前系统高出最多 64% 和 5 倍。
