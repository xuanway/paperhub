---
title: "The First Star-by-Star $N$-body/Hydrodynamics Simulation of Our Galaxy Coupling with a Surrogate Model"
description: "SC 2025 · Applications: Large-Scale Scientific Simulation · Keiya Hirashima; Michiko Fujii; Takayuki Saitoh; Naoto Harada; Kentaro Nomura; K"
tags:
  - "SC2025"
  - "Applications: Large-Scale Scientific Simulation"
---

# The First Star-by-Star $N$-body/Hydrodynamics Simulation of Our Galaxy Coupling with a Surrogate Model

**中文标题：** 首个与代理模型耦合的银河系逐恒星 N 体与流体动力学仿真

**所属 Session：** [Applications: Large-Scale Scientific Simulation](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Applications: Large-Scale Scientific Simulation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Applications: Large-Scale Scientific Simulation</p>
</div>

**作者**：Keiya Hirashima; Michiko Fujii; Takayuki Saitoh; Naoto Harada; Kentaro Nomura; Kohji Yoshikawa; Yutaka Hirai; Tetsuro Asano; Kana Moriwaki; Masaki Iwasawa; Takashi Okamoto; Junichiro Makino

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap676&sess=sess177)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要

A major goal of computational astrophysics is to simulate the Milky Way galaxy with sufficient resolution, down to individual stars. However, the scaling fails due to some small-scale, short-timescale phenomena, such as supernova explosions. We have developed a novel integration scheme of $N$-body/hydrodynamics simulations working with machine learning. This approach bypasses the short timesteps caused by supernova explosions using a surrogate model, thereby improving scalability. With this method, we reached 300 billion particles using 148,900 nodes, equivalent to 7,147,200 CPU cores, breaking through the billion-particle barrier currently faced by state-of-the-art simulations. This resolution allows us to perform the first star-by-star galaxy simulation, which resolves individual stars in the Milky Way galaxy. The performance scales over $10^4$ CPU cores, an upper limit in the current state-of-the-art simulations using both A64FX and X86-64 processors and NVIDIA CUDA GPUs.

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
