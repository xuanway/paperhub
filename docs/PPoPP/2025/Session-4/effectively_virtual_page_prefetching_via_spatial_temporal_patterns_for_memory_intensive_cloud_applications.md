---
title: "Effectively Virtual Page Prefetching via Spatial-Temporal Patterns for Memory-intensive Cloud Applications"
description: "PPoPP 2025 Session 4（Memory）：面向 VM 的时空模式页预取，性能损失降低 45%"
tags:
  - "PPoPP2025"
  - "Session-4"
  - "Memory"
  - "Page Prefetching"
  - "Virtualization"
  - "Cloud"
authors:
  - "Yun Wang"
  - "Liang Chen"
  - "Tianmai Deng"
  - "Ben Luo"
  - "Yibin Shen"
  - "Zhixiang Wei"
  - "Yixiao Xu"
  - "Minglang Huang"
  - "Zhengwei Qi"
session: "Session 4: Memory"
session_number: 4
session_chair: "Dong Li"
date: "2025-03-03"
time: "16:00–16:20"
room: "Acacia D"
doi: "10.1145/3710848.3710865"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# Effectively Virtual Page Prefetching via Spatial-Temporal Patterns for Memory-intensive Cloud Applications

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出面向虚拟机的页预取系统 vPrefetcher，用时空模式驱动的 Trend 算法提前准备将被访问的页面，降低内存复用场景下的性能损失。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 4: Memory</p>
</div>

**作者**：Yun Wang (Shanghai Jiao Tong University); Liang Chen (Alibaba Group); Tianmai Deng (Shanghai Jiao Tong University); Ben Luo (Alibaba Group); Yibin Shen (Alibaba Cloud); Zhixiang Wei, Yixiao Xu, Minglang Huang, Zhengwei Qi (Shanghai Jiao Tong University)

**会议**：PPoPP 2025 · 2025 年 3 月 3 日 16:00–16:20 · Session 4: Memory（主席：Dong Li）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710865) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 提出面向虚拟机的页预取系统 vPrefetcher，用时空模式驱动的 Trend 算法提前准备将被访问的页面，降低内存复用场景下的性能损失。

## 研究问题

现有预取方法在虚拟机内存复用环境中表现不佳（如 Leap 主要依赖地址信息），难以在维持服务质量与优化资源利用之间取得平衡。

## 方法简述

- 监控 VM 对当前未驻留内存的访问行为，提前准备相应页面。
- Trend 算法利用空间与时间访问模式提升预取效果，并降低内存回收开销。

## 主要结果

- 在典型数据中心应用、内存复用条件下，VM 性能损失最高降低 45%。
- 效果显著优于现有预取方案。

<details>
<summary>原文摘要（英文）</summary>

In today’s data-driven era, the explosive growth of global data volume has led to an increasing consumption of computing and storage resources. Effective management of virtual machines (VMs) memory usage is critical for cloud vendors to optimize system performance and resource utilization. Existing memory prefetching methods often slow down system performance, creating a difficult balance between maintaining service quality and optimizing resource use. For instance, Leap, which primarily utilizes address information, performs poorly in VM environments. The main issue is the performance drop caused by the reuse of memory resources in virtualized environments, a common situation in public clouds. To tackle this, we introduce vPrefetcher, a page prefetching system designed specifically for VMs. vPrefetcher monitors how VMs access memory that is not currently in use and prepares that memory in advance. Our unique Trend algorithm uses the spatial and temporal patterns to improve how memory is prefetched, reduce the overhead of memory reclamation. By applying vPrefetcher in tests with typical data center applications under memory reuse conditions, we have noticed a significant improvement. Our system reduces the performance loss in VMs by up to 45%, which is a considerable improvement over existing solutions. 0 20 40 60 80 100 Memory (%) Swapped-memory when fixed size swap enable Memory remain unreclaimed and unused. DBSQL Hadoop Memory Hotness level7 level6 level5 level4 level3 level2 level1 level0 0 25 50 75 100 125 150 175 Time 0 20 40 60 80 100 Memory (%) Performance degradation due to memory swapping SparkGraph 0 25 50 75 100 125 150 175 Time SparkMem Figure 1. Heatmap profiles the memory page table usage across various workloads, utilizing a total of 24GB memory with 2MB per page. The page table is categorized into eight levels (0 to 7), where level 0 represents the least accessed and level 7 the most accessed pages. Grey areas indicate pages eligible for reclamation when a fixed-sized (60%) swap is enabled. Notably, DBSQL shows swap inefficiencies, while swap usage in other workloads adversely impacts performance.

</details>

---

> 所属 Session：[Session 4: Memory](index.md) · 返回 [PPoPP 2025 总览](../index.md)
