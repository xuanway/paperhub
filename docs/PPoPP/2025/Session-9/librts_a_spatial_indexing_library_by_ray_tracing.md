---
title: "LibRTS: A Spatial Indexing Library by Ray Tracing"
description: "PPoPP 2025 Session 9（Concurrent Data Structures and Synchronization II）：把空间查询映射为 RT 问题，点查询最高 85.1×"
tags:
  - "PPoPP2025"
  - "Session-9"
  - "Concurrent Data Structures and Synchronization II"
  - "Ray Tracing"
  - "Spatial Index"
  - "BVH"
authors:
  - "Liang Geng"
  - "Rubao Lee"
  - "Xiaodong Zhang"
session: "Session 9: Concurrent Data Structures and Synchronization II"
session_number: 9
session_chair: "Pengfei Su"
date: "2025-03-04"
time: "16:20–16:40"
room: "Acacia D"
doi: "10.1145/3710848.3710850"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# LibRTS: A Spatial Indexing Library by Ray Tracing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出空间索引库 LibRTS，把点查询与范围查询表述为适合光线追踪硬件的问题，利用 RT core 的 BVH 遍历能力加速空间查询，并支持数据动态变更。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 9: Concurrent Data Structures and Synchronization II</p>
</div>

**作者**：Liang Geng (The Ohio State University); Rubao Lee (Freelance); Xiaodong Zhang (The Ohio State University)

**会议**：PPoPP 2025 · 2025 年 3 月 4 日 16:20–16:40 · Session 9: Concurrent Data Structures and Synchronization II（主席：Pengfei Su）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710850) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 提出空间索引库 LibRTS，把点查询与范围查询表述为适合光线追踪硬件的问题，利用 RT core 的 BVH 遍历能力加速空间查询，并支持数据动态变更。

## 研究问题

RT core 本质上是 BVH 树遍历的硬件加速器，具备加速空间负载的潜力；但其专用编程模型使非渲染场景难以直接使用。

## 方法简述

- 设计通用的空间索引框架，把空间查询转化为适合 RT core 的问题，而非逐类问题定制。
- 克服负载均衡挑战，支持点查询、范围查询以及可变数据（mutable）。

## 主要结果

- 相比 CPU 与 GPU 空间库，点查询最高加速 85.1×，range-contains 查询最高 94.0×，range-intersects 查询最高 11.0×。
- 在 point-in-polygon 实际应用中，比 SOTA 的 RT 方法最高快 3.8×。

<details>
<summary>原文摘要（英文）</summary>

The Ray-Tracing (RT) core has become a widely integrated feature in modern GPUs to accelerate ray-tracing rendering. Recent research has shown that RT cores can also be repurposed to accelerate non-rendering workloads. Since the RT core essentially serves as a hardware accelerator for Bounding Volume Hierarchy (BVH) tree traversal, it holds the potential to significantly improve the performance of spatial workloads. However, the specialized RT programming model poses challenges for using RT cores in these scenarios. Inspired by the core functionality of RT cores, we designed and implemented LibRTS, a spatial index library that leverages RT cores to accelerate spatial queries. LibRTS supports both point and range queries and remains mutable to accommodate changing data. Instead of relying on a case-by-case approach, LibRTS provides a general, high-performance spatial indexing framework for spatial data processing. By formulating spatial queries as RT-suitable problems and overcoming load-balancing challenges, LibRTS delivers superior query performance through RT cores without requiring developers to master complex programming on this specialized hardware. Compared to CPU and GPU spatial libraries, LibRTS achieves speedups of up to 85.1x for point queries, 94.0x for range-contains queries, and 11.0x for range-intersects queries. In a real-world application, point- in-polygon testing, LibRTS also surpasses the state-of-the-art RT method by up to 3.8x.

</details>

---

> 所属 Session：[Session 9: Concurrent Data Structures and Synchronization II](index.md) · 返回 [PPoPP 2025 总览](../index.md)
