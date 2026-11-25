---
title: "Parameterized Algorithms for Non-uniform All-to-all"
description: "HPDC 2025 · Session 4 — Efficiency and Sustainability"
tags:
  - "HPDC2025"
  - "Session 4"
  - "Efficiency and Sustainability"
---

# Parameterized Algorithms for Non-uniform All-to-all

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2025 主会 Session 4 — Efficiency and Sustainability（2025年7月22日 10:30–12:15 · Session Chair：Jarek Nabrzyski）。</p>
<p class="paper-seo-summary__tags">HPDC 2025 · Session 4</p>
</div>

**官方资料**：[HPDC 2025 官方议程](https://hpdc.sci.utah.edu/2025/program.html) · [ACM DOI](https://doi.org/10.1145/3731545.3731590) · [Slides](https://hpdc.sci.utah.edu/2025/assets/slides/main_session/fan.pdf)

**作者**：Ke Fan, Jens Domke, Seydou Ba, Sidharth Kumar

**会议**：HPDC 2025 · Notre Dame, IN, USA

**Session**：Session 4 — Efficiency and Sustainability（2025年7月22日 10:30–12:15 · Session Chair：Jarek Nabrzyski）

---

## 英文摘要

MPI_Alltoallv generalizes the uniform all-to-all communication (MPI_Alltoall) by enabling the exchange of data-blocks of varied sizes among processes. This function plays a crucial role in facilitating many computational tasks, such as FFT calculations and graph mining operations. Popular MPI libraries, such as MPICH and OpenMPI, implement MPI_Alltoall using a combination of linear and logarithmic algorithms. However, MPI_Alltoallv typically relies only on variations of linear algorithms, missing the benefits of logarithmic approaches. Furthermore, current algorithms also overlook the intricacies of modern HPC system architectures, such as the significant performance gap between intra-node (local) and inter-node (global) communication. To address these problems, this paper presents two novel algorithms: Parameterized Logarithmic non-uniform All-to-all (ParLogNa) and Parameterized Linear nonuniform All-to-all (ParLinNa). ParLogNa is a tunable logarithmic time algorithm for non-uniform all-to-all, and ParLinNa is a hierarchical and tunable near-linear-time algorithm for non-uniform all-to-all. These algorithms efficiently address the trade-off between bandwidth maximization and latency minimization that existing implementations struggle to optimize. We show a performance improvement over the state-of-the-art implementations by factors of 42x and 138x on Polaris and Fugaku, respectively.

## 中文摘要

MPI_Alltoallv 通过允许进程间交换大小各异的数据块，推广了均匀的全对全通信（MPI_Alltoall）。该函数在 FFT 计算和图挖掘等众多计算任务中发挥着关键作用。MPICH 和 OpenMPI 等主流 MPI 库使用线性与对数算法的组合来实现 MPI_Alltoall。然而，MPI_Alltoallv 通常只依赖线性算法的变体，错失了对数方法带来的收益。此外，当前算法还忽视了现代 HPC 系统架构的复杂性，例如节点内（局部）与节点间（全局）通信之间显著的性能差距。为解决这些问题，本文提出两种新算法：参数化对数非均匀全对全（ParLogNa）与参数化线性非均匀全对全（ParLinNa）。ParLogNa 是一种可调的对数时间非均匀全对全算法，ParLinNa 是一种分层、可调的近线性时间非均匀全对全算法。这些算法有效解决了现有实现难以优化的带宽最大化与延迟最小化之间的权衡。我们展示了相比最先进实现，在 Polaris 和 Fugaku 上分别取得 42 倍和 138 倍的性能提升。

---

[← 返回 Session 4 — Efficiency and Sustainability](index.md)
