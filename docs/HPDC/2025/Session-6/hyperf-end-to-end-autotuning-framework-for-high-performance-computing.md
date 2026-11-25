---
title: "HYPERF: End-to-End Autotuning Framework for High-Performance Computing"
description: "HPDC 2025 · Session 6 — Tuning and Performance"
tags:
  - "HPDC2025"
  - "Session 6"
  - "Tuning and Performance"
---

# HYPERF: End-to-End Autotuning Framework for High-Performance Computing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2025 主会 Session 6 — Tuning and Performance（2025年7月23日 10:30–12:15 · Session Chair：Jay Lofstead）。</p>
<p class="paper-seo-summary__tags">HPDC 2025 · Session 6</p>
</div>

**官方资料**：[HPDC 2025 官方议程](https://hpdc.sci.utah.edu/2025/program.html) · [ACM DOI](https://doi.org/10.1145/3731545.3731588) · [Slides](https://hpdc.sci.utah.edu/2025/assets/slides/main_session/park.pdf)

**作者**：Juseong Park, Yongwon Shin, Junghyun Lee, Junseo Lee, Juyeon Kim, Oh-Kyoung Kwon, Hyojin Sung

**会议**：HPDC 2025 · Notre Dame, IN, USA

**Session**：Session 6 — Tuning and Performance（2025年7月23日 10:30–12:15 · Session Chair：Jay Lofstead）

---

## 英文摘要

The increasing complexity and diversity of modern high-performance computing (HPC) systems require automated performance tuning approaches that generalize across architectures and workloads. Unlike traditional compiler optimizations and hand-tuned libraries relying on hard-coded, engineering-intensive heuristics, autotuning treats optimization as a search problem, iteratively evaluating candidate programs to identify high-performing configurations. However, current HPC autotuning solutions often suffer from low abstraction levels, limited search spaces, and restricted extensibility due to their tight integration with compilers. This paper proposes HYPERF, an end-to-end HPC autotuning framework that combines user-friendly pragma-based interfaces with tensor-level autotuning from deep learning frameworks for flexible candidate generation and efficient optimization. HYPERF adopts an offloading approach, identifying regions annotated with custom pragmas, translating them to tensor-based IR, and delegating to a tensor-level autotuner. To maximize tuning opportunities, HYPERF extends the tensor-level autotuner to pre-process generated TIR and broaden the autotuning scope. We evaluate HYPERF across HPC benchmarks, demonstrating that it outperforms baseline OpenMP versions by up to 103.5x, achieving average improvements of 6.1x over existing autotuning methods and 4.2x over polyhedral compilers. These results underscore the strength of HYPERF’s hybrid autotuning approach, balancing programmability, efficiency, and extensibility.

## 中文摘要

现代高性能计算（HPC）系统日益增长的复杂性与多样性，要求自动性能调优方法能够跨体系结构与负载泛化。与依赖硬编码、工程密集型启发式的传统编译器优化和手工调优库不同，自动调优将优化视为搜索问题，迭代评估候选程序以找出高性能配置。然而，当前 HPC 自动调优方案往往因与编译器紧密耦合而存在抽象层次低、搜索空间有限、可扩展性受限等问题。本文提出 HYPERF，一个端到端 HPC 自动调优框架，将易用的 pragma 接口与来自深度学习框架的张量级自动调优相结合，以实现灵活的候选生成与高效优化。HYPERF 采用卸载式方法：识别用自定义 pragma 标注的区域，将其翻译为基于张量的 IR，并交由张量级自动调优器处理。为最大化调优机会，HYPERF 扩展了张量级自动调优器，以预处理生成的 TIR 并拓宽自动调优范围。我们在 HPC 基准上评估 HYPERF，表明其相比基线 OpenMP 版本最高提升 103.5 倍，相比现有自动调优方法平均提升 6.1 倍，相比多面体编译器提升 4.2 倍。这些结果凸显了 HYPERF 混合自动调优方法的优势，在可编程性、效率与可扩展性之间取得平衡。

---

[← 返回 Session 6 — Tuning and Performance](index.md)
