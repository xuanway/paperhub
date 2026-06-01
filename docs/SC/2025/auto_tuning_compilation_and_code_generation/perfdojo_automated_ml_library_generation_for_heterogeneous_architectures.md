---
title: "PerfDojo: Automated ML Library Generation for Heterogeneous Architectures"
description: "SC 2025 · Auto-Tuning, Compilation, and Code Generation · Andrei Ivanov; Siyuan Shen; Gioele Gottardo; Marcin Chrapek; Afif Boudaoud; Timo"
tags:
  - "SC2025"
  - "Auto-Tuning, Compilation, and Code Generation"
---

# PerfDojo: Automated ML Library Generation for Heterogeneous Architectures

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Auto-Tuning, Compilation, and Code Generation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Auto-Tuning, Compilation, and Code Generation</p>
</div>

**作者**：Andrei Ivanov; Siyuan Shen; Gioele Gottardo; Marcin Chrapek; Afif Boudaoud; Timo Schneider; Luca Benini; Torsten Hoefler

**会议**：SC 2025 · St. Louis, MO

## 摘要

The increasing complexity of machine learning models and the proliferation of diverse hardware architectures (CPUs, GPUs, accelerators) make achieving optimal performance a significant challenge. Heterogeneity in instruction sets, specialized kernel requirements for different data types and model features (e.g., sparsity, quantization), and architecture-specific optimizations complicate performance tuning. Manual optimization is resource-intensive, while existing automatic approaches often rely on complex hardware-specific heuristics and uninterpretable intermediate representations, hindering performance portability. We introduce PerfLLM, a novel automatic optimization methodology leveraging large language models (LLMs) and reinforcement learning (RL). Central to this is PerfDojo, an environment framing optimization as an RL game using a human-readable, mathematically-inspired code representation that guarantees semantic validity through transformations. This allows effective optimizat

---

## 一句话总结

> 该工作属于 Auto-Tuning, Compilation, and Code Generation 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Auto-Tuning, Compilation, and Code Generation 领域贡献新的设计范式或评估框架。
