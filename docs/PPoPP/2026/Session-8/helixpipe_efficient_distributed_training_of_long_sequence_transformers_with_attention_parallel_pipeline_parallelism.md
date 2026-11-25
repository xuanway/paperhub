---
title: "HelixPipe: Efficient Distributed Training of Long Sequence Transformers with Attention Parallel Pipeline Parallelism"
description: "PPoPP 2026 Session 8（Distributed Training）：注意力并行流水+无注意力重算，7B/128k 序列提速 26%"
tags:
  - "PPoPP2026"
  - "Session-8"
  - "Distributed Training"
  - "pipeline parallelism"
  - "long sequence"
  - "distributed training"
authors:
  - "Geng Zhang"
  - "Shenggan Cheng"
  - "Xuanlei Zhao"
  - "Ziming Liu"
  - "Yang You"
session: "Session 8: Distributed Training"
session_number: 8
session_chair: "Bo Fang"
date: "2026-02-03"
time: "14:50–15:10"
room: "Balmoral"
doi: "10.1145/3774934.3786417"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# HelixPipe: Efficient Distributed Training of Long Sequence Transformers with Attention Parallel Pipeline Parallelism

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出面向长序列 Transformer 训练的流水并行 HelixPipe，把不同微批的注意力计算分散到不同流水级并行执行以减少气泡，7B 模型 128k 序列在 64 卡上提速 26%。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 8: Distributed Training</p>
</div>

**作者**：Geng Zhang, Shenggan Cheng, Xuanlei Zhao, Ziming Liu, and Yang You — National University of Singapore, Singapore

**会议**：PPoPP 2026 · 2026 年 2 月 3 日 14:50–15:10 · Session 8: Distributed Training（主席：Bo Fang）· Balmoral

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786417) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

As transformer sequence lengths grow, existing pipeline parallelisms incur suboptimal performance due to the quadratic attention computation and the substantial memory overhead. To relieve these challenges, we propose HelixPipe, a novel pipeline parallelism for long sequence transformer training. First, HelixPipe introduces attention parallel partition, which schedules attention computations of different micro batches across different pipeline stages in parallel, reducing pipeline bubbles. Second, it employs a two-fold first-in-last-out micro batch schedule to balance memory usage and overlap communication with computation. Additionally, HelixPipe utilizes recomputation without attention and chunked MLP to mitigate fragmentation and enable longer sequences. Experiments demonstrate that HelixPipe gains increasing advantages with longer sequence lengths, and outperforms existing methods in throughput and scalability across varying pipeline sizes, model sizes, and cluster configurations. Notably, it achieves a 26% speedup over baseline methods when training a 7B model with 128k sequence length on 64 H20 GPUs. Code is available at https://github.com/zxgx/Megatron-LM.

## 中文摘要

随着 Transformer 序列长度增长，现有流水线并行由于注意力计算的二次复杂度以及巨大的内存开销而性能欠佳。为缓解这些挑战，我们提出 HelixPipe，一种面向长序列 Transformer 训练的新型流水线并行方法。首先，HelixPipe 引入注意力并行划分，将不同微批的注意力计算调度到不同流水线阶段并行执行，从而减少流水线气泡。其次，它采用双重的后进先出微批调度，以平衡内存使用并重叠通信与计算。此外，HelixPipe 采用不含注意力的重计算与分块 MLP，以缓解内存碎片并支持更长的序列。实验表明，HelixPipe 的优势随序列长度增加而增大，并在不同流水线规模、模型规模和集群配置下，于吞吐量与可扩展性方面优于现有方法。值得注意的是，在 64 块 H20 GPU 上以 128k 序列长度训练 7B 模型时，它相比基线方法取得了 26% 的加速。代码见 https://github.com/zxgx/Megatron-LM。

## 英文关键词

Distributed Deep Learning, Pipeline Parallelism, Long Sequence Transformer

## 中文关键词

分布式深度学习；流水线并行；长序列 Transformer

---

## 一句话总结

> 提出面向长序列 Transformer 训练的流水并行 HelixPipe，把不同微批的注意力计算分散到不同流水级并行执行以减少气泡，7B 模型 128k 序列在 64 卡上提速 26%。

## 研究问题

随着序列长度增长，注意力的二次方计算开销与庞大的显存占用使现有流水并行性能次优。

## 方法简述

- 提出注意力并行划分，将不同微批的注意力计算调度到不同流水级上并行执行，减少流水气泡。
- 采用 two-fold first-in-last-out 微批调度，平衡显存使用并重叠通信与计算。
- 采用不含注意力的重计算与分块 MLP，缓解显存碎片并支持更长的序列。

## 主要结果

- 序列越长 HelixPipe 的优势越明显，在不同流水规模、模型规模与集群配置下吞吐与可扩展性均优于现有方法。
- 在 64 张 H20 GPU 上以 128k 序列长度训练 7B 模型时，相比基线方法取得 26%的加速。

---

> 所属 Session：[Session 8: Distributed Training](index.md) · 返回 [PPoPP 2026 总览](../index.md)
