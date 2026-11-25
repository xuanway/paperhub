---
title: "MARLIN: Mixed-Precision Auto-Regressive Parallel Inference on Large Language Models"
description: "PPoPP 2025 Session 6（Large Language Models）：批量量化推理 kernel，batch 16–32 近 4× 加速，端到端 2.8×"
tags:
  - "PPoPP2025"
  - "Session-6"
  - "Large Language Models"
  - "LLM Inference"
  - "Quantization"
  - "GPU Kernels"
authors:
  - "Elias Frantar"
  - "Roberto L. Castro"
  - "Jiale Chen"
  - "Torsten Hoefler"
  - "Dan Alistarh"
session: "Session 6: Large Language Models"
session_number: 6
session_chair: "Minjia Zhang"
date: "2025-03-04"
time: "10:00–10:20"
room: "Acacia D"
doi: "10.1145/3710848.3710871"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# MARLIN: Mixed-Precision Auto-Regressive Parallel Inference on Large Language Models

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 MARLIN，为量化 LLM 设计混精度自回归线性 kernel，使批量推理在 batch 16–32 时仍接近 4× 的量化加速，并集成 vLLM 获得端到端收益。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 6: Large Language Models</p>
</div>

**作者**：Elias Frantar (ISTA); Roberto L. Castro (Universidade da Coruña); Jiale Chen (ISTA); Torsten Hoefler (ETH Zürich); Dan Alistarh (ISTA and Neural Magic, Inc.)

**会议**：PPoPP 2025 · 2025 年 3 月 4 日 10:00–10:20 · Session 6: Large Language Models（主席：Minjia Zhang）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710871) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 提出 MARLIN，为量化 LLM 设计混精度自回归线性 kernel，使批量推理在 batch 16–32 时仍接近 4× 的量化加速，并集成 vLLM 获得端到端收益。

## 研究问题

权重量化在单用户推理中因减少访存而大幅加速，但在多客户端批量服务下计算需求显著增加，能否继续维持近内存受限并取得加速仍是开放问题。

## 方法简述

- 结合异步访存、复杂任务调度与流水，支撑批量场景下的计算需求。
- 针对量化权重格式提供定制化 kernel 支持。

## 主要结果

- batch 16–32 时可接近 4× 的最大量化加速，batch 64–128 仍有显著加速。
- 集成 vLLM 后端到端 LLM 推理最高加速 2.8×，并可扩展到 2:4 稀疏等压缩技术。

<details>
<summary>原文摘要（英文）</summary>

As inference on Large Language Models (LLMs) emerges as an important workload in machine learning applications, model weight quantization has become a standard technique for efficient GPU deployment. Quantization not only reduces model size, but has also been shown to yield substantial speedups for single-user inference, due to reduced memory movement, with low accuracy impact. Yet, it remains a key open question whether speedups are achievable also in batched settings with multiple parallel clients, which are highly relevant for practical serving. It is unclear whether GPU kernels can be designed to remain practically memory-bound, while supporting the substantially increased compute requirements of batched workloads. In this paper, we resolve this question positively by introducing a new design for Mixed-precision Auto-Regressive LINear kernels, called MARLIN. Concretely, given a model whose weights are compressed via quantization to, e.g., 4 bits per element, MARLIN shows that batchsizes up to 16-32 can be practically supported with close to maximum (4×) quantization speedup, and larger batchsizes up to 64-128 with gradually decreasing, but still significant, acceleration. MARLIN accomplishes this via a combination of techniques, such as asynchronous memory access, complex task scheduling and pipelining, and bespoke quantization support. Our experiments show that MARLIN’s near-optimal performance on individual LLM layers across different scenarios can also lead to significant end-to-end LLM inference speedups (of up to 2.8×) when integrated with the popular vLLM open-source serving engine. Finally, we show that MARLIN is extensible to further compression techniques, like NVIDIA 2:4 sparsity, leading to additional speedups.

</details>

---

> 所属 Session：[Session 6: Large Language Models](index.md) · 返回 [PPoPP 2025 总览](../index.md)
