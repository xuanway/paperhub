---
title: "AutoSSD: CXL-Enhanced Autonomous SSDs for Low Tail Latency"
description: "HPDC 2025 · Session 3 — Storage Systems"
tags:
  - "HPDC2025"
  - "Session 3"
  - "Storage Systems"
---

# AutoSSD: CXL-Enhanced Autonomous SSDs for Low Tail Latency

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2025 主会 Session 3 — Storage Systems（2025年7月21日 15:30–16:45 · Session Chair：Hariharan Devarajan）。</p>
<p class="paper-seo-summary__tags">HPDC 2025 · Session 3</p>
</div>

**官方资料**：[HPDC 2025 官方议程](https://hpdc.sci.utah.edu/2025/program.html) · [ACM DOI](https://doi.org/10.1145/3731545.3731579) · [Slides](https://hpdc.sci.utah.edu/2025/assets/slides/main_session/shen.pdf)

**作者**：Mingyao Shen, Suyash Mahar, Heewoo Kim, Joseph Izraelevitz, Steven Swanson

**会议**：HPDC 2025 · Notre Dame, IN, USA

**Session**：Session 3 — Storage Systems（2025年7月21日 15:30–16:45 · Session Chair：Hariharan Devarajan）

---

## 英文摘要

All-SSD RAID arrays offer high performance but suffer from long tail latencies due to background processes like garbage collection. Globally scheduling accesses to avoid busy SSDs may mitigate this problem, but such a solution presents challenges in collecting realtime data about SSD performance and tracking the location of redirected blocks. We propose AutoSSD, a scalable, CXL-based SSD array designed to reduce tail latency in SSD RAID systems through autonomous IO traffic balancing. Using CXL’s cache coherence, SSDs efficiently share their internal states and redirect requests to non-busy SSDs without CPU intervention. AutoSSD employs an innovative hybrid redirection strategy, combining a static RAID+ algorithm with the dynamic selection of non-busy SSDs, thereby balancing overhead reduction and redirection flexibility. Our evaluation shows that AutoSSD consistently reduces tail latencies by 13.3-44.3% compared to Linux RAID across various workloads, from microbenchmarks to real-world applications.

## 中文摘要

全 SSD RAID 阵列提供高性能，但因垃圾回收等后台进程而存在长尾延迟。全局调度访问以避开繁忙 SSD 可缓解该问题，但此类方案在收集 SSD 性能实时数据以及跟踪重定向块位置方面存在挑战。我们提出 AutoSSD，一种可扩展的、基于 CXL 的 SSD 阵列，通过自主 I/O 流量均衡来降低 SSD RAID 系统中的尾延迟。利用 CXL 的缓存一致性，SSD 能够高效共享其内部状态，并在无需 CPU 干预的情况下将请求重定向到非繁忙 SSD。AutoSSD 采用创新的混合重定向策略，将静态 RAID+ 算法与非繁忙 SSD 的动态选择相结合，从而在降低开销与重定向灵活性之间取得平衡。我们的评估表明，从微基准到真实应用的各种负载下，AutoSSD 相比 Linux RAID 持续将尾延迟降低 13.3%–44.3%。

## 英文关键词

Solid-State Drive, Compute Express Link, Tail Latency, Redundant Array of Independent Disks

## 中文关键词

固态硬盘，Compute Express Link，尾延迟，独立磁盘冗余阵列

---

[← 返回 Session 3 — Storage Systems](index.md)
