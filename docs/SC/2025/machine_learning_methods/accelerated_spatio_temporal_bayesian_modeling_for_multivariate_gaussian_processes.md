---
title: "Accelerated Spatio-Temporal Bayesian Modeling for Multivariate Gaussian Processes"
description: "SC 2025 · Machine Learning: Methods · Lisa Gaedke-Merzhäuser; Vincent Maillou; Fernando Rodriguez Avellaneda; Olaf Sch"
tags:
  - "SC2025"
  - "Machine Learning: Methods"
---

# Accelerated Spatio-Temporal Bayesian Modeling for Multivariate Gaussian Processes

**中文标题：** 面向多变量高斯过程的加速时空贝叶斯建模

**所属 Session：** [Machine Learning: Methods](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Methods。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Methods</p>
</div>

**作者**：Lisa Gaedke-Merzhäuser; Vincent Maillou; Fernando Rodriguez Avellaneda; Olaf Schenk; Paula Moraga; Mathieu Luisier; Alexandros Nikolaos Ziogas; Haavard Rue

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap484&sess=sess183)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

Multivariate Gaussian processes (GPs) offer a powerful probabilistic framework to represent complex interdependent phenomena. They pose, however, significant computational challenges in high-dimensional settings, which frequently arise in spatio-temporal applications. We present DALIA, a highly scalable framework for performing Bayesian inference tasks on spatio-temporal multivariate GPs, based on the methodology of integrated nested Laplace approximations. Our approach relies on a sparse inverse covariance matrix formulation of the GP, puts forward a GPU-accelerated block-dense approach, and introduces a hierarchical, triple-layer, distributed-memory parallel scheme. We showcase weak-scaling performance surpassing the state of the art by two orders of magnitude on a model whose parameter space is 8$\times$ larger and measure strong-scaling speedups of three orders of magnitude when running on 496 GH200 superchips on the Alps supercomputer. Applying DALIA to an air pollution study over

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
