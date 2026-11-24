---
title: "Trinity: Three-Dimensional Tensor Program Optimization via Tile-level Equality Saturation"
description: "ASPLOS 2026 · Session 4B · Trinity：通过 Tile 级等式饱和实现的三维张量程序优化"
tags:
  - "ASPLOS2026"
  - "Session 4B"
  - "ML Compilers & Tensor Programs"
---

# Trinity: Three-Dimensional Tensor Program Optimization via Tile-level Equality Saturation

**中文标题：** Trinity：通过 Tile 级等式饱和实现的三维张量程序优化

**所属 Session：** [Session 4B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Jaehyeong Park (KAIST), Youngchan Kim (KAIST), Haechan An (KAIST), Gieun Jeong (KAIST), Jeehoon Kang (FuriosaAI), Dongsu Han (KAIST)

**单位：** KAIST；FuriosaAI

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790240) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Modern tensor program optimizers operate at two separate levels: graph-level optimizations (operator fusion, algebraic rewrites) and operator-level scheduling (tiling, parallelization). This separation prevents them from discovering cross-operator, tile-level optimizations that make hand-tuned kernels like FlashAttention effective. We present Trinity, the first tensor program optimizer that achieves scalable joint optimization through tile-level equality saturation. Our key insight is that optimal performance requires simultaneously optimizing three interdependent dimensions — algebraic equivalence, memory I/O, and compute orchestration. To enable this, Trinity introduces a novel fine-grained IR that exposes all three axes as firstclass, rewritable entities and applies equality saturation to perform scalable joint optimization. As a result, Trinity automatically discovers complex optimizations that require coordinated reasoning across all three dimensions. Across diverse Transformer variants, Trinity achieves up to 2.09× speedup over TensorRT and 2.35× over TorchInductor, both state-of-the-art production compilers.

## 中文摘要

现代张量程序优化器在两个相互独立的层面上工作：图级优化（算子融合、代数重写）与算子级调度（分块、并行化）。这种分离使它们无法发现跨算子、Tile 级的优化，而正是这类优化让 FlashAttention 等手工调优的内核得以高效。我们提出 Trinity，这是首个通过 Tile 级等式饱和实现可扩展联合优化的张量程序优化器。我们的核心洞见是：要达到最优性能，需要同时优化三个相互依赖的维度——代数等价性、内存 I/O 和计算编排。为此，Trinity 引入一种新颖的细粒度 IR，将全部三个轴暴露为一等的、可重写的实体，并应用等式饱和来执行可扩展的联合优化。由此，Trinity 能够自动发现需要在全部三个维度上协同推理的复杂优化。在多种 Transformer 变体上，Trinity 相对于 TensorRT 和 TorchInductor（两者均为当前最先进的生产级编译器）分别取得最高 2.09× 和 2.35× 的加速。

## 英文关键词

Tensor Program Optimization, Equality Saturation, Joint Optimization, Inference Latency

## 中文关键词

张量程序优化；等式饱和；联合优化；推理延迟

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790240)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 4B](index.md) · [返回 ASPLOS 2026](../index.md)
