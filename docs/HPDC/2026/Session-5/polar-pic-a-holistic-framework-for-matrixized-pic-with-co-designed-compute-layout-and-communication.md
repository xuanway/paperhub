---
title: "POLAR-PIC: A Holistic Framework for Matrixized PIC with Co-Designed Compute, Layout, and Communication"
description: "HPDC 2026 · Session 5 — Scientific Applications at Scale"
tags:
  - "HPDC2026"
  - "Session 5"
  - "Scientific Applications at Scale"
---

# POLAR-PIC: A Holistic Framework for Matrixized PIC with Co-Designed Compute, Layout, and Communication

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 5 — Scientific Applications at Scale（2026年7月15日 10:20–11:20 · Session Chair：Michael Papka）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 5</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807574)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#RaoCPXFZWGWCL26](https://dblp.org/db/conf/hpdc/hpdc2026.html#RaoCPXFZWGWCL26)

**作者**：Yizhuo Rao, Xingjian Cui, Shangzhi Pang, Jiabin Xie, Guangnan Feng, Ziyan Zhang, Jinhui Wei, Languang Gao, Zhenyu Wang, Zhiguang Chen, Yutong Lu

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 5 — Scientific Applications at Scale（2026年7月15日 10:20–11:20 · Session Chair：Michael Papka）

---

## 英文摘要

Particle-in-Cell (PIC) simulations are fundamental to plasma physics but often suffer from limited scalability due to particle–grid interaction bottlenecks and particle redistribution costs. Specifically, the particle–grid interaction computations have not taken full advantage of the emerging Matrix Processing Units (MPUs), the particle motion introduces irregular memory accesses, and the bulk-synchronous redistribution further destroys long-term data locality thereby limiting parallel efficiency. To address these inefficiencies, we present POLAR-PIC, a co-designed framework for large-scale PIC simulations that (i) reformulates Field Interpolation into an MPU-friendly outer-product form, (ii) maintains a physically ordered particle layout to preserve memory contiguity, and (iii) overlaps particle communication with Deposition to hide redistribution overhead. The evaluation on the pilot system of an Exascale supercomputer demonstrates that POLAR-PIC accelerates the entire particle-processing phase by up to 10.9× in uniform plasma and 4.4× in real-world laser-ion acceleration scenarios compared to the native WarpX reference pipeline on LX2. Ablation studies reveal that the speedups achieved by Interpolation and Deposition are 8.0× and 13.2×, respectively, and the asynchronous communication design sustains a 99.1% overlap ratio. In cross-platform comparisons, POLAR-PIC achieves 13.2% of theoretical peak efficiency on the CPU-based LS system, while WarpX reaches 9.6% on NVIDIA A800 GPUs. Notably, the scalability evaluation demonstrates that POLAR-PIC maintains 67.5% weak scaling efficiency on over 2 million cores under high-migration dynamic workloads, highlighting the importance of holistic co-design for future matrix-centric HPC systems.

## 中文摘要

粒子网格（Particle-in-Cell, PIC）模拟是等离子体物理的基础，但常因粒子-网格交互瓶颈和粒子重分布开销而可扩展性受限。具体而言，粒子-网格交互计算尚未充分利用新兴的矩阵处理单元（MPU），粒子运动引入不规则内存访问，而块同步重分布进一步破坏长期数据局部性，从而限制并行效率。为解决这些低效问题，我们提出 POLAR-PIC，一个面向大规模 PIC 模拟的协同设计框架，它：(i) 将场插值重构为适合 MPU 的外积形式；(ii) 保持物理有序的粒子布局以维持内存连续性；(iii) 将粒子通信与沉积（Deposition）重叠，以隐藏重分布开销。在百亿亿次超级计算机试验系统上的评估表明，相比 LX2 上原生 WarpX 参考流水线，POLAR-PIC 在均匀等离子体中将整个粒子处理阶段加速最高 10.9 倍，在真实激光-离子加速场景中加速 4.4 倍。消融研究表明，插值与沉积分别取得 8.0 倍和 13.2 倍加速，异步通信设计维持 99.1% 的重叠率。跨平台比较中，POLAR-PIC 在基于 CPU 的 LS 系统上达到理论峰值效率的 13.2%，而 WarpX 在 NVIDIA A800 GPU 上为 9.6%。值得注意的是，可扩展性评估表明，在高迁移动态负载下，POLAR-PIC 在超过 200 万核上保持 67.5% 的弱扩展效率，凸显了整体协同设计对未来以矩阵为中心的 HPC 系统的重要性。

## 英文关键词

Particle-in-Cell simulation, High-Performance Computing, Scientific Computing, Hardware Acceleration

## 中文关键词

粒子网格模拟，高性能计算，科学计算，硬件加速

---

[← 返回 Session 5 — Scientific Applications at Scale](index.md)
