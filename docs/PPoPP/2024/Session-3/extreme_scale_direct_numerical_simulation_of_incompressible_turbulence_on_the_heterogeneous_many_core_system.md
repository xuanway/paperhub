---
title: "Extreme-scale Direct Numerical Simulation of Incompressible Turbulence on the Heterogeneous Many-core System"
description: "PPoPP 2024 Session High Performance Computing：天河异构 DNS 求解器：10.6× 加速、258 亿网格线性强扩展"
tags:
  - "PPoPP2024"
  - "Session-3"
  - "High Performance Computing"
  - "direct numerical simulation"
  - "heterogeneous many-core"
  - "high performance computing"
authors:
  - "Jiabin Xie"
  - "Guangnan Feng"
  - "Han Huang"
  - "Junxuan Feng"
  - "Zhiguang Chen"
  - "Yutong Lu"
session: "Session 3: High Performance Computing"
session_number: 3
session_chair: "Helen Xu"
date: "2024-03-04"
time: "15:00–15:20"
room: "Moorfoot"
doi: "10.1145/3627535.3638479"
program_url: "https://ppopp24.sigplan.org/program/program-PPoPP-2024/"
---

# Extreme-scale Direct Numerical Simulation of Incompressible Turbulence on the Heterogeneous Many-core System

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">PowerLLEL++ 以自适应多层并行、层次化分块与内核融合、PDD 三对角求解及 RDMA 通信优化，在新天河上最高加速 10.6×，258 亿网格保持线性强扩展。</p>
<p class="paper-seo-summary__tags">PPoPP 2024 · Session 3: High Performance Computing</p>
</div>

**作者**：Jiabin Xie, Guangnan Feng, Han Huang, Junxuan Feng, Zhiguang Chen, Yutong Lu (Sun Yat-sen University)

**会议**：PPoPP 2024 · 2024 年 3 月 4 日 15:00–15:20 · Session 3: High Performance Computing（主席：Helen Xu）· Moorfoot

**论文**：[ACM Digital Library](https://doi.org/10.1145/3627535.3638479) · [PPoPP 2024 会议日程](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

---

## 英文摘要

Direct numerical simulation (DNS) is a technique that directly solves the fluid Navier-Stokes equations with high spatial and temporal resolutions, which has driven much research regarding the nature of turbulence. For high-Reynolds number (Re) incompressible turbulence of particular interest, where the nondimensional Recharacterizes the flow regime, the application of DNS is hindered by the fact that the numerical grid size (i.e., the memory requirement) scales with Re3, while the overall computational cost scales with Re4. Recent studies have shown that developing efficient parallel methods for heterogeneous many-core systems is promising to solve this computational challenge. We develop PowerLLEL++, a high-performance and scalable implicit finite difference solver for heterogeneous manycore systems, to accelerate the extreme-scale DNS of incompressible turbulence. To achieve this goal, an adaptive multi-level parallelization strategy is first proposed to fully exploit the multi-level parallelism and computing power of heterogeneous many-core systems. Second, hierarchical-memory-adapted data reuse/tiling strategy and kernel fusion are adopted to improve the performance of memory-bound stencil-like operations. Third, a parallel tridiagonal solver based on the parallel diagonal dominant (PDD) algorithm is developed to minimize the number of global data transposes. Fourth, three effective communication optimizations are implemented by Remote Direct Memory Access (RDMA) to maximize the performance of the remaining global transposes and halo exchange. Results show that the solver exploits the heterogeneous computing power of the new Tianhe supercomputer and achieves a speedup of up to 10.6× (against the CPU-only performance). Linear strong scaling is obtained with a grid size of up to 25.8 billion.

## 中文摘要

直接数值模拟（DNS）是一种以高空间与时间分辨率直接求解流体 Navier–Stokes 方程的技术，它推动了许多关于湍流本质的研究。对于特别受关注的高雷诺数（Re）不可压缩湍流——其中无量纲 Re 表征流动状态——DNS 的应用受到阻碍：数值网格规模（即内存需求）随 Re³ 增长，而总体计算代价随 Re⁴ 增长。近期研究表明，为异构众核系统开发高效并行方法有望解决这一计算挑战。我们开发了 PowerLLEL++，一个面向异构众核系统的高性能、可扩展隐式有限差分求解器，用于加速不可压缩湍流的极端规模 DNS。为实现该目标，首先提出一种自适应多层并行策略，以充分挖掘异构众核系统的多层次并行性与算力。其次，采用适应层次化存储的数据复用/分块策略与内核融合，以提升访存受限的模板类操作的性能。第三，开发了基于并行对角占优（PDD）算法的并行三对角求解器，以最小化全局数据转置的次数。第四，通过远程直接内存访问（RDMA）实现了三项有效的通信优化，以最大化剩余全局转置与 halo 交换的性能。结果表明，该求解器充分利用了新天河超级计算机的异构算力，最高取得 10.6× 的加速（相对纯 CPU 性能）。在最大 258 亿的网格规模下获得了线性强扩展。

## 英文关键词

incompressible turbulence, direct numerical simulation, heterogeneous, many-core, high performance computing

## 中文关键词

不可压缩湍流；直接数值模拟；异构；众核；高性能计算

---

## 一句话总结

> PowerLLEL++ 以自适应多层并行、层次化分块与内核融合、PDD 三对角求解及 RDMA 通信优化，在新天河上最高加速 10.6×，258 亿网格保持线性强扩展。

## 研究问题

高雷诺数不可压缩湍流的 DNS 中，网格规模随 Re³ 增长、总计算代价随 Re⁴ 增长，巨大开销阻碍其应用；现有并行方法难以在异构众核系统上高效支撑此类极端规模模拟。

## 方法简述

- 提出自适应多层并行策略，充分挖掘异构众核系统的多层次并行性与算力
- 采用适应层次化存储的数据复用/分块（tiling）策略与内核融合，提升访存受限的模板类（stencil-like）操作性能
- 基于并行对角占优（PDD）算法设计并行三对角求解器，最小化全局数据转置次数
- 通过远程直接内存访问（RDMA）实现三项通信优化，最大化剩余全局转置与 halo 交换的性能

## 主要结果

- 求解器充分利用新天河超级计算机的异构算力，相对纯 CPU 性能最高取得 10.6× 加速
- 在最大 258 亿的网格规模下获得线性强扩展（linear strong scaling）
- 验证了隐式有限差分 DNS 在异构众核系统上的极端规模可行性

---

> 所属 Session：[Session 3: High Performance Computing](index.md) · 返回 [PPoPP 2024 总览](../index.md)
