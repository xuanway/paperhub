---
title: "The First Star-by-Star $N$-body/Hydrodynamics Simulation of Our Galaxy Coupling with a Surrogate Model"
description: "SC 2025 · Applications: Large-Scale Scientific Simulation · Keiya Hirashima; Michiko Fujii; Takayuki Saitoh; Naoto Harada; Kentaro Nomura; K"
tags:
  - "SC2025"
  - "Applications: Large-Scale Scientific Simulation"
---

# The First Star-by-Star $N$-body/Hydrodynamics Simulation of Our Galaxy Coupling with a Surrogate Model

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Applications: Large-Scale Scientific Simulation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Applications: Large-Scale Scientific Simulation</p>
</div>

**作者**：Keiya Hirashima; Michiko Fujii; Takayuki Saitoh; Naoto Harada; Kentaro Nomura; Kohji Yoshikawa; Yutaka Hirai; Tetsuro Asano; Kana Moriwaki; Masaki Iwasawa; Takashi Okamoto; Junichiro Makino

**会议**：SC 2025 · St. Louis, MO

## 摘要

A major goal of computational astrophysics is to simulate the Milky Way galaxy with sufficient resolution, down to individual stars. However, the scaling fails due to some small-scale, short-timescale phenomena, such as supernova explosions. We have developed a novel integration scheme of $N$-body/hydrodynamics simulations working with machine learning. This approach bypasses the short timesteps caused by supernova explosions using a surrogate model, thereby improving scalability. With this method, we reached 300 billion particles using 148,900 nodes, equivalent to 7,147,200 CPU cores, breaking through the billion-particle barrier currently faced by state-of-the-art simulations. This resolution allows us to perform the first star-by-star galaxy simulation, which resolves individual stars in the Milky Way galaxy. The performance scales over $10^4$ CPU cores, an upper limit in the current state-of-the-art simulations using both A64FX and X86-64 processors and NVIDIA CUDA GPUs.

---

## 一句话总结

> 该工作属于 Applications: Large-Scale Scientific Simulation 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Applications: Large-Scale Scientific Simulation 领域贡献新的设计范式或评估框架。
