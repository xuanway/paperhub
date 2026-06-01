---
title: "Phoenix: A Refactored I/O Stack for GPU Direct Storage Without Phony Buffers"
description: "SC 2025 · Data Analytics, Visualization, and Storage · Jianqin Yan; Shi Qiu; Yina Lv; Yifan Hu; Hao Chen; Zhirong Shen; Xin Yao; Renhai"
tags:
  - "SC2025"
  - "Data Analytics, Visualization, and Storage"
---

# Phoenix: A Refactored I/O Stack for GPU Direct Storage Without Phony Buffers

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Data Analytics, Visualization, and Storage。</p>
<p class="paper-seo-summary__tags">SC 2025 · Data Analytics, Visualization, and Storage</p>
</div>

**作者**：Jianqin Yan; Shi Qiu; Yina Lv; Yifan Hu; Hao Chen; Zhirong Shen; Xin Yao; Renhai Chen; Jiwu Shu; Gong Zhang; Yiming Zhang

**会议**：SC 2025 · St. Louis, MO

## 摘要

GPU Direct Storage (GDS) plays a vital role in GPU storage systems, utilizing P2P-DMA technology to establish a direct data transfer path between the GPU and storage devices. This direct path reduces storage access latency and CPU overhead, thus improving data transfer efficiency. Currently, however, GDS employs a phony buffer in host memory to interact with the Linux kernel, resulting in suboptimal performance, additional resource consumption, and deployment complexity. In this paper, we propose Phoenix, a refactored GDS software stack without phony buffers. Phoenix employs the memory mapping service of ZONE_DEVICE to map GPU memory into the page table at system startup. The kernel module of Phoenix stores the returned address information, allocates user-space virtual memory, and establishes a mapping with the designated GPU memory. Extensive evaluation shows that, compared to the existing GDS software stack, Phoenix reduces software overhead along the critical I/O path and improves e

---

## 一句话总结

> 该工作属于 Data Analytics, Visualization, and Storage 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Data Analytics, Visualization, and Storage 领域贡献新的设计范式或评估框架。
