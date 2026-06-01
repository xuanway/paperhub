---
title: "Accelerated Spatio-Temporal Bayesian Modeling for Multivariate Gaussian Processes"
description: "SC 2025 · Machine Learning: Methods · Lisa Gaedke-Merzhäuser; Vincent Maillou; Fernando Rodriguez Avellaneda; Olaf Sch"
tags:
  - "SC2025"
  - "Machine Learning: Methods"
---

# Accelerated Spatio-Temporal Bayesian Modeling for Multivariate Gaussian Processes

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Methods。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Methods</p>
</div>

**作者**：Lisa Gaedke-Merzhäuser; Vincent Maillou; Fernando Rodriguez Avellaneda; Olaf Schenk; Paula Moraga; Mathieu Luisier; Alexandros Nikolaos Ziogas; Haavard Rue

**会议**：SC 2025 · St. Louis, MO

## 摘要

Multivariate Gaussian processes (GPs) offer a powerful probabilistic framework to represent complex interdependent phenomena. They pose, however, significant computational challenges in high-dimensional settings, which frequently arise in spatio-temporal applications. We present DALIA, a highly scalable framework for performing Bayesian inference tasks on spatio-temporal multivariate GPs, based on the methodology of integrated nested Laplace approximations. Our approach relies on a sparse inverse covariance matrix formulation of the GP, puts forward a GPU-accelerated block-dense approach, and introduces a hierarchical, triple-layer, distributed-memory parallel scheme. We showcase weak-scaling performance surpassing the state of the art by two orders of magnitude on a model whose parameter space is 8$\times$ larger and measure strong-scaling speedups of three orders of magnitude when running on 496 GH200 superchips on the Alps supercomputer. Applying DALIA to an air pollution study over

---

## 一句话总结

> 该工作属于 Machine Learning: Methods 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Machine Learning: Methods 领域贡献新的设计范式或评估框架。
