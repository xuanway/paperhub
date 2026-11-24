---
title: "OmniCache: Collaborative Caching for Near-storage Accelerators"
description: "FAST 2024 · Distributed Storage · 第 35–50 页"
tags:
  - "FAST2024"
  - "Distributed Storage"
---

# OmniCache: Collaborative Caching for Near-storage Accelerators

**中文标题**：OmniCache：面向近存储加速器的协同缓存

**Session**：Distributed Storage · 2024-02-27 10:45–12:00 · Chair：Raju Rangaswami（Florida International University）

**作者**：Jian Zhang and Yujie Ren, Rutgers University; Marie Nguyen, Samsung; Changwoo Min, Igalia; Sudarsun Kannan, Rutgers University

**会议**：FAST 2024 · Santa Clara, CA · 第 35–50 页

**USENIX 页面**：[https://www.usenix.org/conference/fast24/presentation/zhang-jian](https://www.usenix.org/conference/fast24/presentation/zhang-jian)

**论文 PDF**：[fast24-zhang-jian.pdf](https://www.usenix.org/system/files/fast24-zhang-jian.pdf)

---

## 英文摘要

We propose *OmniCache*, a novel caching design for near-storage accelerators that combines near-storage and host memory capabilities to accelerate I/O and data processing. First, OmniCache introduces a *"near-cache" approach*, maximizing data access to the nearest cache for I/O and processing operations. Second, OmniCache presents *collaborative caching* for concurrent I/O and data processing using host and device caches. Third, OmniCache incorporates a *dynamic model-driven offloading* support, which actively monitors hardware and software metrics for efficient processing across host and device processors. Finally, OmniCache explores the *extensibility of the newly introduced CXL*, a memory expansion technology. Evaluation of OmniCache demonstrates significant performance gains of up to 3.24X for I/O workloads and 3.06X for data processing workloads.

## 中文摘要

我们提出 *OmniCache*，一种面向近存储加速器的新型缓存设计，它结合近存储与主机内存的能力来加速 I/O 和数据处理。首先，OmniCache 引入 *“近缓存”（near-cache）方法*，最大化 I/O 和处理操作对最近缓存的访问。其次，OmniCache 提出*协同缓存*，利用主机和设备缓存同时服务并发的 I/O 与数据处理。第三，OmniCache 融入*动态模型驱动的卸载*支持，主动监控硬件和软件指标，以便在主机与设备处理器之间高效处理。最后，OmniCache 探索了新引入的 CXL 这一内存扩展技术的*可扩展性*。对 OmniCache 的评估表明，其在 I/O 负载上取得最高 3.24 倍的显著性能提升，在数据处理负载上取得最高 3.06 倍的提升。
