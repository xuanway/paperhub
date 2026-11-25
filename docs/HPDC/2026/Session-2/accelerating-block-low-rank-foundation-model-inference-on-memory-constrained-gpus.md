---
title: "Accelerating Block Low-Rank Foundation Model Inference on Memory-Constrained GPUs"
description: "HPDC 2026 · Session 2 — Scaling Generative Inference"
tags:
  - "HPDC2026"
  - "Session 2"
  - "Scaling Generative Inference"
---

# Accelerating Block Low-Rank Foundation Model Inference on Memory-Constrained GPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 2 — Scaling Generative Inference（2026年7月14日 11:30–12:30 · Session Chair：Bogdan Nicolae）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 2</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807580)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#AbillamaLDBSK26](https://dblp.org/db/conf/hpdc/hpdc2026.html#AbillamaLDBSK26)

**作者**：Pierre Abillama, Changwoo Lee, Juechu Dong, David Blaauw, Dennis Sylvester, Hun-Seok Kim

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 2 — Scaling Generative Inference（2026年7月14日 11:30–12:30 · Session Chair：Bogdan Nicolae）

---

## 英文摘要

Recent advances in transformer-based foundation models have made them the default choice for many tasks, but their rapidly growing size makes fitting a full model on a single GPU increasingly difficult and their computational cost prohibitive. Block low-rank (BLR) compression techniques address this challenge by learning compact representations of weight matrices. While traditional low-rank (LR) methods often incur sharp accuracy drops, BLR approaches such as Monarch and BLAST can better capture the underlying structure, thus preserving accuracy while reducing computations and memory footprints. In this work, we use roofline analysis to show that, although BLR methods achieve theoretical savings and practical speedups for single-token inference, multi-token inference often becomes memory-bound in practice, increasing latency despite compiler-level optimizations in PyTorch. To address this, we introduce custom Triton kernels with partial fusion and memory layout optimizations for both Monarch and BLAST. On memory-constrained NVIDIA GPUs such as Jetson Orin Nano and A40, our kernels deliver up to 3.76× speedups and 3× model size compression over PyTorch dense baselines using CUDA backend and compiler-level optimizations, while supporting various models including Llama-7/1B, GPT2-S, DiT-XL/2, and ViT-B.

## 中文摘要

近期基于 Transformer 的基础模型的进展使其成为众多任务的默认选择，但其规模快速增长，使得在单块 GPU 上容纳完整模型愈发困难，计算成本也高得难以承受。块低秩（BLR）压缩技术通过学习权重矩阵的紧凑表示来应对这一挑战。传统低秩（LR）方法往往导致精度急剧下降，而 Monarch、BLAST 等 BLR 方法能更好地刻画底层结构，从而在降低计算量与内存占用的同时保持精度。在本工作中，我们通过 roofline 分析表明：尽管 BLR 方法在单 token 推理中能带来理论收益与实际加速，但在多 token 推理中往往在实际中变为内存受限，即便经过 PyTorch 的编译器级优化，延迟仍然上升。为此，我们针对 Monarch 与 BLAST 引入带部分融合和内存布局优化的定制 Triton 核。在 Jetson Orin Nano、A40 等显存受限的 NVIDIA GPU 上，与使用 CUDA 后端和编译器级优化的 PyTorch 稠密基线相比，我们的核实现最高 3.76 倍加速和 3 倍模型体积压缩，并支持 Llama-7/1B、GPT2-S、DiT-XL/2 和 ViT-B 等多种模型。

## 英文关键词

Triton, Resource-Constrained GPU, Hardware Acceleration, Block Low-Rank Matrix Multiplication, Roofline Modeling

## 中文关键词

Triton，资源受限 GPU，硬件加速，块低秩矩阵乘法，Roofline 建模

---

[← 返回 Session 2 — Scaling Generative Inference](index.md)
