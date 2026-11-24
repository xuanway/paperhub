---
title: "gParaKV: A GPGPU-Accelerated Key-Value Separation-Based KV Store with Optimized Compaction and Garbage Collection"
description: "SC 2025 · Data Analytics, Visualization, and Storage · Hui Sun; Xiangxiang Jiang; Xiao Qin; Song Jiang; Enhui Wang"
tags:
  - "SC2025"
  - "Data Analytics, Visualization, and Storage"
---

# gParaKV: A GPGPU-Accelerated Key-Value Separation-Based KV Store with Optimized Compaction and Garbage Collection

**中文标题：** 基于 GPU 加速键值分离并优化合并与垃圾回收的键值存储

**所属 Session：** [Data Analytics, Visualization, and Storage](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Data Analytics, Visualization, and Storage。</p>
<p class="paper-seo-summary__tags">SC 2025 · Data Analytics, Visualization, and Storage</p>
</div>

**作者**：Hui Sun; Xiangxiang Jiang; Xiao Qin; Song Jiang; Enhui Wang

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap943&sess=sess283)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

LSM tree-based key-value stores are widely deployed in modern cloud storage systems thanks to high data storage efficiency and retrieval capabilities. The compaction in the LSM tree, however, results in severe performance bottlenecks, especially in large-sized value cases. While key-value separation methods mitigate the performance bottlenecks caused by compaction, the existing methods do not fully address merge-sorting during compaction and expensive garbage collection (GC). We propose gParaKV, a GPGPU-empowered KV store with a KV separation mechanism, leveraging the GPGPU parallel technology to accelerate merge-sorting in compaction and GC. gParaKV embraces a GPGPU bitmap structure, parallel data marking, and a parallel GC mechanism. These critical components curtail the overhead of merge-sorting and GC by virtue of parallel computing. We compare it with state-of-the-art KV stores under various workloads. The experimental results show that gParaKV can improve the write performance an

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
