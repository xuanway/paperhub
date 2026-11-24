---
title: "T2-RELION: Task Parallelism, Tensor Core Accelerated RELION for Cryo-EM 3D Reconstruction"
description: "SC 2025 · Applications: Biological Modeling · Jiayu Fu; Jingle Xu; Lin Gan; Tianqi Mao; Zirong Shen; Yinuo Wang; Zeyu Song; Xi"
tags:
  - "SC2025"
  - "Applications: Biological Modeling"
---

# T2-RELION: Task Parallelism, Tensor Core Accelerated RELION for Cryo-EM 3D Reconstruction

**中文标题：** 利用任务并行和张量核心加速 RELION 冷冻电镜三维重建

**所属 Session：** [Applications: Biological Modeling](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Applications: Biological Modeling。</p>
<p class="paper-seo-summary__tags">SC 2025 · Applications: Biological Modeling</p>
</div>

**作者**：Jiayu Fu; Jingle Xu; Lin Gan; Tianqi Mao; Zirong Shen; Yinuo Wang; Zeyu Song; Xiaohui Duan; Wei Xue; Guangwen Yang

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap445&sess=sess303)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Cryo-electron microscopy (cryo-EM) is a key technique for structural biology, but its computational efficiency, particularly during 3D reconstruction, remains a bottleneck. We introduce T2-RELION, a highly optimized version of RELION for cryo-EM 3D reconstruction on CPU-GPU platforms. RELION is a widely used open-source package in the cryo-EM community. We identify and resolve key inefficiencies in RELION’s parallelization strategy and memory management by proposing task parallelism and a three-phase GPU memory management strategy. Furthermore, we leverage Tensor Cores to accelerate the hot-spot kernel for difference calculation, employing an advanced pipelining strategy to hide latency and enable thread block-level data reuse. On a quad-A100 GPU machine, performance evaluations demonstrate that T2-RELION outperforms RELION 4.0. For the hot-spot kernel, our optimizations achieve 1.90-23.7 times speedup. For the whole application using CNG and Trpv1 datasets, we observe 3.86 times and 2

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
