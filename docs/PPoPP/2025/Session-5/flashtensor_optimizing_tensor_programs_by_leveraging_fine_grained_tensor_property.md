---
title: "FlashTensor: Optimizing Tensor Programs by Leveraging Fine-grained Tensor Property"
description: "PPoPP 2025 Session 5（Deep Neural Networks）：细粒度张量属性驱动优化，端到端平均加速 1.50×"
tags:
  - "PPoPP2025"
  - "Session-5"
  - "Deep Neural Networks"
  - "Tensor Programs"
  - "Memory Optimization"
  - "Long Context"
authors:
  - "Runxin Zhong"
  - "Yuyang Jin"
  - "Chen Zhang"
  - "Kinman Lei"
  - "Shuangyu Li"
  - "Jidong Zhai"
session: "Session 5: Deep Neural Networks"
session_number: 5
session_chair: "Wei Niu"
date: "2025-03-03"
time: "17:00–17:20"
room: "Acacia D"
doi: "10.1145/3710848.3710864"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# FlashTensor: Optimizing Tensor Programs by Leveraging Fine-grained Tensor Property

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 FlashTensor，从计算图中提取 reduce dependency、broadcastability 等细粒度张量属性，并据此进行图变换与 kernel 映射，降低长上下文 DNN 的显存开销并提升推理性能。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 5: Deep Neural Networks</p>
</div>

**作者**：Runxin Zhong, Yuyang Jin, Chen Zhang, Kinman Lei, Shuangyu Li, Jidong Zhai (Tsinghua University)

**会议**：PPoPP 2025 · 2025 年 3 月 3 日 17:00–17:20 · Session 5: Deep Neural Networks（主席：Wei Niu）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710864) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 提出 FlashTensor，从计算图中提取 reduce dependency、broadcastability 等细粒度张量属性，并据此进行图变换与 kernel 映射，降低长上下文 DNN 的显存开销并提升推理性能。

## 研究问题

长上下文 DNN 会产生极大的中间张量，带来沉重的显存开销；现有优化对张量属性的感知不足，既难以充分优化显存，也会在长上下文场景下造成低效计算。

## 方法简述

- 从计算图中提取并识别关键张量属性，如 reduce dependency 与 broadcastability。
- 基于这些属性组合执行计算图变换与 kernel 映射优化。

## 主要结果

- 在 7 个模型上，端到端性能平均加速 1.50×、核心模块平均加速 3.24×（对比 8 个 SOTA 工作，H100）。
- 在 A100 上端到端与核心模块平均加速分别达到 1.86× 与 3.70×。

<details>
<summary>原文摘要（英文）</summary>

Deep neural networks (DNNs) have shown significant effectiveness in natural language processing and video applications. However, DNN models, especially for long-context tasks, introduce extremely large intermediate tensors, producing substantial memory overhead. Although considerable efforts have been made to optimize DNNs, insufficient awareness of tensor properties has hindered effective memory optimization and can lead to inefficient computations in a long-context scenario. In this paper, we present FlashTensor1, a DNN optimization system that reduces memory overhead and improves inference performance by leveraging fine-grained tensor properties. We first extract and identify essential tensor properties from a computation graph, such as reduce dependency and broadcastability. Then, we apply various optimizations involving transformation and kernel mapping based on these properties. Experiments on seven models demonstrate that FlashTensor achieves speedups of 1.50× and 3.24× on average for end-to-end and core module performance, respectively, compared to eight state-of-the-art works, on H100 (1.86× and 3.70× on A100).

</details>

---

> 所属 Session：[Session 5: Deep Neural Networks](index.md) · 返回 [PPoPP 2025 总览](../index.md)
