---
title: "MISA-AKMC: Achieve Kinetic Monte Carlo Simulation of 20 Quadrillion Atoms on GPU Clusters"
description: "SC 2025 · Applications: Atomistic Modeling · Shunde Li; Zhijie Pan; Ningming Nie; Jue Wang; He Bai; Genshen Chu; Yan Zeng; Xi"
tags:
  - "SC2025"
  - "Applications: Atomistic Modeling"
---

# MISA-AKMC: Achieve Kinetic Monte Carlo Simulation of 20 Quadrillion Atoms on GPU Clusters

**中文标题：** 在 GPU 集群上实现两千万亿原子的动力学蒙特卡洛仿真

**所属 Session：** [Applications: Atomistic Modeling](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Applications: Atomistic Modeling。</p>
<p class="paper-seo-summary__tags">SC 2025 · Applications: Atomistic Modeling</p>
</div>

**作者**：Shunde Li; Zhijie Pan; Ningming Nie; Jue Wang; He Bai; Genshen Chu; Yan Zeng; Xinfu He; Yangang Wang; Changjun Hu; Xuebin Chi

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap172&sess=sess300)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

The Atomic Kinetic Monte Carlo (AKMC) method provides insights into the macroscopic behavior of materials through atomistic-level simulations and finds broad applications in materials science innovation. Improving simulation scale and performance remains a consistent focus in the development of parallel AKMC software. We port the AKMC software to GPU clusters. To alleviate the memory pressure in large-scale complex system simulations, we redesign the data layout and propose the lattice data compression and vacancy data decompression algorithms. Additionally, we propose a multi-level pipeline scheme combined with an on-demand communication forwarding and merging strategy to reduce data transfer and communication overhead. Compared to state-of-the-art KMC software, MISA-AKMC\footnotemark achieves a 10.41-fold improvement in computational throughput and a 52.07-fold expansion in simulation scale. We implement the first true micrometer-scale AKMC simulation involving 20 quadrillion atoms o

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
