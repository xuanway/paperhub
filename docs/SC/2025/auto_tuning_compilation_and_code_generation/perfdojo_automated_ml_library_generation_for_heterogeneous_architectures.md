---
title: "PerfDojo: Automated ML Library Generation for Heterogeneous Architectures"
description: "SC 2025 · Auto-Tuning, Compilation, and Code Generation · Andrei Ivanov; Siyuan Shen; Gioele Gottardo; Marcin Chrapek; Afif Boudaoud; Timo"
tags:
  - "SC2025"
  - "Auto-Tuning, Compilation, and Code Generation"
---

# PerfDojo: Automated ML Library Generation for Heterogeneous Architectures

**中文标题：** 面向异构架构的机器学习库自动生成

**所属 Session：** [Auto-Tuning, Compilation, and Code Generation](index.md) · [SC 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Auto-Tuning, Compilation, and Code Generation。</p>
<p class="paper-seo-summary__tags">SC 2025 · Auto-Tuning, Compilation, and Code Generation</p>
</div>

**作者**：Andrei Ivanov; Siyuan Shen; Gioele Gottardo; Marcin Chrapek; Afif Boudaoud; Timo Schneider; Luca Benini; Torsten Hoefler

**会议**：SC 2025 · St. Louis, MO

**官方资料：** [论文详情](https://sc25.conference-program.com/?post_type=page&p=14&id=pap959&sess=sess290)（摘要、论文及演示材料以官方页面提供情况为准）

## 摘要摘录

原有摘录在 1000 字符处截断；完整摘要请查看官方论文详情。

The increasing complexity of machine learning models and the proliferation of diverse hardware architectures (CPUs, GPUs, accelerators) make achieving optimal performance a significant challenge. Heterogeneity in instruction sets, specialized kernel requirements for different data types and model features (e.g., sparsity, quantization), and architecture-specific optimizations complicate performance tuning. Manual optimization is resource-intensive, while existing automatic approaches often rely on complex hardware-specific heuristics and uninterpretable intermediate representations, hindering performance portability. We introduce PerfLLM, a novel automatic optimization methodology leveraging large language models (LLMs) and reinforcement learning (RL). Central to this is PerfDojo, an environment framing optimization as an RL game using a human-readable, mathematically-inspired code representation that guarantees semantic validity through transformations. This allows effective optimizat

---

[返回 Session](index.md) · [SC 2025 主页](../index.md)
