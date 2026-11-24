---
title: "Stability-Preserving Lossy Compression for Large-Scale Partial Differential Equations"
description: "SC 2025 · Compression and Data Reduction 1 · Qian Gong; Mark Ainsworth; Jieyang Chen; Xin Liang; Liangji Zhu; Ethan Klasky; T"
tags:
  - "SC2025"
  - "Compression and Data Reduction 1"
---

# Stability-Preserving Lossy Compression for Large-Scale Partial Differential Equations

**中文标题：** 面向大规模偏微分方程的稳定性保持有损压缩

**所属 Session：** [Compression and Data Reduction 1](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Compression and Data Reduction 1。</p>
<p class="paper-seo-summary__tags">SC 2025 · Compression and Data Reduction 1</p>
</div>

**作者**：Qian Gong; Mark Ainsworth; Jieyang Chen; Xin Liang; Liangji Zhu; Ethan Klasky; Tushar Athawale; Qing Liu; Anand Rangarajan; Sanjay Ranka; Scott Klasky

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap770&sess=sess162)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Checkpoint/Restart (C/R) strategies are vital for fault tolerance in PDE-based scientific simulations, yet traditional checkpointing incurs significant I/O overhead. Lossy compression offers a scalable solution by reducing checkpoint data size, but conventional methods often lack control over physical invariants (e.g., energy), leading to instability such as oscillations or divergence in partial differential equation (PDE) systems. This paper introduces a stability-preserving compression approach tailored for PDE simulations by explicitly controlling kinetic and potential energy perturbations to ensure stable restarts. Extensive experiments conducted across diverse PDE configurations demonstrate that our method maintains numerical stability with minimal error magnification—even across multiple checkpoint-restart cycles—outperforming state-of-the-art lossy compressors. Parallel evaluations on the Frontier supercomputer show up to 8.4× improvement in checkpoint write performance and 6.3×

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
