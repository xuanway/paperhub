---
title: "SYCL++: A Unified Programming Framework for Heterogeneous Supercomputers at Scale"
description: "HPDC 2026 · Session 4 — Programming Models, Frameworks & Compilers"
tags:
  - "HPDC2026"
  - "Session 4"
  - "Programming Models, Frameworks & Compilers"
---

# SYCL++: A Unified Programming Framework for Heterogeneous Supercomputers at Scale

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 4 — Programming Models, Frameworks & Compilers（2026年7月14日 14:40–15:40 · Session Chair：Dhabaleswar K (DK) Panda）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 4</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807812)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#ShenJLMWWZCWZWL26](https://dblp.org/db/conf/hpdc/hpdc2026.html#ShenJLMWWZCWZWL26)

**作者**：Zitao Shen, Yuyang Jin, Kinman Lei, Zixuan Ma, Wenqiang Wang, Yinuo Wang, Wenhao Zhou, Zhenchuan Chen, Di Wei, Qi Zhang, Fei Wang, Ying Liu, Lin Gan, Jidong Zhai

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 4 — Programming Models, Frameworks & Compilers（2026年7月14日 14:40–15:40 · Session Chair：Dhabaleswar K (DK) Panda）

---

## 英文摘要

With the rise of heterogeneous HPC systems, traditional scientific applications face increasingly severe challenges. Today’s supercomputers adopt vastly different designs in compute units, memory hierarchies, and interconnects, making application porting an expensive task that demands significant expert effort. This deep coupling results in fragmented, unmaintainable codebases. In particular, it creates substantial barriers for domain scientists, hindering algorithmic innovation across such diverse architectures. Consequently, there is an urgent need for a unified compiler and programming framework that enables true single-source performance portability across this diverse landscape. However, achieving this unification is challenging due to a central contradiction: while diverse architectures often converge on high-level abstractions, their low-level architectures frequently diverge in parallel execution models, memory management mechanisms, and network topologies. To address this, we propose SYCL++1, a unified programming framework that decouples the expression of computational semantics from platform-specific optimization strategies. SYCL++ introduces declarative primitives that allow a single, clean codebase to be efficiently mapped to different HPC systems. We validate our approach using a real-world CGFDM3D seismic simulation application. Our evaluation demonstrates that SYCL++ achieves performance portability across three distinct platforms, delivering up to 2.2× speedups over baseline SYCL with minimal code divergence. The framework exhibits near linear scaling to 1,597,440 Sunway cores and 8,192 DCUs, enabling high-resolution simulation of realistic earthquake scenarios. We demonstrate this capability by modeling the March 2025 Myanmar earthquake at 125 m resolution. To our knowledge, this is among the first demonstrations of a unified HPC application achieving performance portability across three distinct leading supercomputers.

## 中文摘要

随着异构 HPC 系统的兴起，传统科学应用面临日益严峻的挑战。当今超级计算机在计算单元、内存层次与互连上采用迥异的设计，使得应用移植成为一项昂贵、需要大量专家投入的任务。这种深度耦合导致代码库碎片化、难以维护。尤其严重的是，它为领域科学家制造了巨大障碍，阻碍了在如此多样架构上的算法创新。因此，亟需一个统一的编译器和编程框架，实现跨多样架构的真正单源性能可移植性。然而，实现这种统一颇具挑战，源于一个核心矛盾：多样架构往往在高层抽象上趋同，但其底层架构在并行执行模型、内存管理机制和网络拓扑上常常分化。为应对这一挑战，我们提出 SYCL++，一个将计算语义的表达与平台特定优化策略解耦的统一编程框架。SYCL++ 引入声明式原语，使单一、整洁的代码库能够高效映射到不同 HPC 系统。我们使用真实的 CGFDM3D 地震模拟应用验证了该方法。评估表明，SYCL++ 在三个不同平台上实现性能可移植性，相比基线 SYCL 最高取得 2.2 倍加速，且代码差异极小。该框架在 1,597,440 个申威核心和 8,192 个 DCU 上展现出接近线性的扩展性，支持真实地震场景的高分辨率模拟。我们通过以 125 米分辨率对 2025 年 3 月缅甸地震建模展示了这一能力。据我们所知，这是首批在三个不同的领先超级计算机上实现性能可移植性的统一 HPC 应用之一。

## 英文关键词

High Performance Computing, Performance Portability, Heterogeneous Computing

## 中文关键词

高性能计算，性能可移植性，异构计算

---

[← 返回 Session 4 — Programming Models, Frameworks & Compilers](index.md)
