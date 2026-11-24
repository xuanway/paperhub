---
title: "Phoenix: A Refactored I/O Stack for GPU Direct Storage Without Phony Buffers"
description: "SC 2025 · Data Analytics, Visualization, and Storage · Jianqin Yan; Shi Qiu; Yina Lv; Yifan Hu; Hao Chen; Zhirong Shen; Xin Yao; Renhai"
tags:
  - "SC2025"
  - "Data Analytics, Visualization, and Storage"
---

# Phoenix: A Refactored I/O Stack for GPU Direct Storage Without Phony Buffers

**中文标题：** 面向 GPU 直接存储的重构 I/O 栈：无需伪缓冲区

**所属 Session：** [Data Analytics, Visualization, and Storage](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Data Analytics, Visualization, and Storage。</p>
<p class="paper-seo-summary__tags">SC 2025 · Data Analytics, Visualization, and Storage</p>
</div>

**作者**：Jianqin Yan; Shi Qiu; Yina Lv; Yifan Hu; Hao Chen; Zhirong Shen; Xin Yao; Renhai Chen; Jiwu Shu; Gong Zhang; Yiming Zhang

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap664&sess=sess283)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

GPU Direct Storage (GDS) plays a vital role in GPU storage systems, utilizing P2P-DMA technology to establish a direct data transfer path between the GPU and storage devices. This direct path reduces storage access latency and CPU overhead, thus improving data transfer efficiency. Currently, however, GDS employs a phony buffer in host memory to interact with the Linux kernel, resulting in suboptimal performance, additional resource consumption, and deployment complexity. In this paper, we propose Phoenix, a refactored GDS software stack without phony buffers. Phoenix employs the memory mapping service of ZONE_DEVICE to map GPU memory into the page table at system startup. The kernel module of Phoenix stores the returned address information, allocates user-space virtual memory, and establishes a mapping with the designated GPU memory. Extensive evaluation shows that, compared to the existing GDS software stack, Phoenix reduces software overhead along the critical I/O path and improves e

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
