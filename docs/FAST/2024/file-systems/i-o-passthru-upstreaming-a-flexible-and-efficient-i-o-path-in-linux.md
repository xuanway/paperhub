---
title: "I/O Passthru: Upstreaming a flexible and efficient I/O Path in Linux"
description: "FAST 2024 · File Systems · 第 107–122 页"
tags:
  - "FAST2024"
  - "File Systems"
---

# I/O Passthru: Upstreaming a flexible and efficient I/O Path in Linux

**中文标题**：I/O Passthru：向 Linux 上游贡献灵活高效的 I/O 路径

**Session**：File Systems · 2024-02-27 15:45–17:00 · Chair：Peter Macko（MongoDB）

**作者**：Kanchan Joshi, Anuj Gupta, Javier González, Ankit Kumar, Krishna Kanth Reddy, Arun George, and Simon Lund, Samsung Semiconductor; Jens Axboe, Meta Platforms Inc.

**会议**：FAST 2024 · Santa Clara, CA · 第 107–122 页

**USENIX 页面**：[https://www.usenix.org/conference/fast24/presentation/joshi](https://www.usenix.org/conference/fast24/presentation/joshi)

**论文 PDF**：[fast24-joshi.pdf](https://www.usenix.org/system/files/fast24-joshi.pdf)

---

## 英文摘要

New storage interfaces continue to emerge fast on Non-Volatile Memory Express (NVMe) storage. Fitting these innovations in the general-purpose I/O stack of operating systems has been challenging and time-consuming. The NVMe standard is no longer limited to block-I/O, but the Linux I/O advances historically centered around the block-I/O path. The lack of scalable OS interfaces risks the adoption of the new storage innovations.

We introduce *I/O Passthru*, a new I/O Path that has made its way into the mainline Linux Kernel. The key ingredients of this new path are *NVMe char interface* and *io_uring command*. In this paper, we present our experience building and upstreaming I/O Passthru and report on how this helps to consume new NVMe innovations without changes to the Linux kernel. We provide experimental results to (i) compare its efficiency against existing *io_uring* block path and (ii) demonstrate its flexibility by integrating data placement into Cachelib. FIO peak performance workloads show 16–40% higher IOPS than block path.

## 中文摘要

新的存储接口在非易失性内存标准（NVMe）存储上不断快速涌现。将这些创新融入操作系统的通用 I/O 栈一直充满挑战且耗时。NVMe 标准已不再局限于块 I/O，但 Linux 的 I/O 进展历来围绕块 I/O 路径展开。缺乏可扩展的操作系统接口，可能会阻碍新的存储创新被采用。

我们提出 *I/O Passthru*，一条已进入 Linux 主线内核的新 I/O 路径。这条新路径的关键组成部分是 *NVMe 字符接口* 和 *io_uring 命令*。本文介绍我们构建并上游化 I/O Passthru 的经验，并报告它如何帮助在不修改 Linux 内核的情况下使用新的 NVMe 创新。我们提供实验结果：(i) 将其效率与现有 *io_uring* 块路径进行比较；(ii) 通过将数据放置集成到 Cachelib 来展示其灵活性。FIO 峰值性能负载显示，其 IOPS 比块路径高 16–40%。
