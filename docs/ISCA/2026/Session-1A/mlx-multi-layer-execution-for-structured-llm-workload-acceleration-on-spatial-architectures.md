---
title: "MLX: Multi-Layer Execution for Structured LLM Workload Acceleration on Spatial Architectures"
description: "ISCA 2026 · Session 1A · MLX: Multi-Layer Execution for Structured LLM Workload Acceleration on Spatial Architectures"
tags:
  - "ISCA2026"
  - "Session 1A"
  - "Best Paper Candidate Session"
---

# MLX: Multi-Layer Execution for Structured LLM Workload Acceleration on Spatial Architectures

**中文标题：** MLX: 面向空间架构上结构化 LLM 工作负载加速的多层执行

**所属 Session：** [Session 1A](index.md) · [ISCA 2026](../index.md)

**作者：** Haibin Wu, Wenming Li, Zhihua Fan, Zirui Ma, Yuqun Liu, Tengfei Xia, Yanhuan Liu, Kunming Zhang, Xiaochun Ye, Dongrui Fan, Jian Weng

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Structured sparsity is a promising approach to scaling large-language-model (LLM) inference, but existing forms such as butterfly-structured sparse projections and transformations often map inefficiently to GPUs due to deep stage dependencies and limited bulk parallelism. This paper presents MLX, an algorithm–architecture co-design for structured LLM inference. MLX couples semantic-aware FFT compression and hierarchical sparse projections with spatial dataflow execution, enabling staged structured operators to run efficiently on compact arrays. MLX defines Closed Dependency Components (CDCs) to capture deterministic forward-only dataflow regions that can be folded across layers and pipelined on compact arrays. It then realizes CDCs through a multi-layer execution architecture with bounded-hop skip-hop routing, tag-based scheduling, and decoupled compute/transfer pipelines to overlap communication and computation across deep operators. We prototype MLX in 12 nm and show that it achieves 3.2× hardware speedup and 3.1× energy savings over Jetson Xavier. A transformer-specialized reduced design further delivers up to 5.7× speedup over prior sparse accelerators. MLX also scales nearly linearly to 8×8 meshes and remains effective for long sequences from 1K to 4K, demonstrating that structured operator semantics can be translated into efficient spatial execution for sparse LLMs.

## 中文摘要

结构化稀疏性是一种有前景的扩展大语言模型（LLM）推理的方法，但现有的形式（如蝶形结构稀疏投影和变换）由于深度阶段依赖性和有限的批量并行性，通常在 GPU 上映射效率低下。本文提出 MLX，一种用于结构化 LLM 推理的算法-架构协同设计。MLX 将语义感知的 FFT 压缩和层次化稀疏投影与空间数据流执行相结合，使分阶段的结构化算子能够在紧凑阵列上高效运行。MLX 定义了封闭依赖组件（CDC）来捕获确定性的前向数据流区域，这些区域可以跨层折叠并在紧凑阵列上流水线化。然后，MLX 通过多层执行架构实现 CDC，该架构具有有界跳数的跳步路由、基于标签的调度以及解耦的计算/传输流水线，以在深层算子之间重叠通信和计算。我们用 12 nm 工艺实现了 MLX 的原型，结果表明，与 Jetson Xavier 相比，它实现了 3.2× 的硬件加速和 3.1× 的能效提升。一个针对 Transformer 精简的设计进一步在之前的稀疏加速器基础上实现了高达 5.7× 的加速。MLX 还能在 8×8 网格上近乎线性地扩展，并且在 1K 到 4K 的长序列上保持有效，证明了结构化算子语义可以转化为针对稀疏 LLM 的高效空间执行。

## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 1A](index.md) · [返回 ISCA 2026](../index.md)
