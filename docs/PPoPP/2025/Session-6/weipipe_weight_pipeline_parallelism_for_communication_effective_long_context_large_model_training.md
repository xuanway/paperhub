---
title: "WeiPipe: Weight Pipeline Parallelism for Communication-Effective Long-Context Large Model Training"
description: "PPoPP 2025 Session 6（Large Language Models）：由传激活改为传权重，降低长上下文训练通信量"
tags:
  - "PPoPP2025"
  - "Session-6"
  - "Large Language Models"
  - "Pipeline Parallelism"
  - "Long Context"
  - "LLM Training"
authors:
  - "Junfeng Lin"
  - "Liu Ziming"
  - "Yang You"
  - "Jun Wang"
  - "Weihao Zhang"
  - "Rong Zhao"
session: "Session 6: Large Language Models"
session_number: 6
session_chair: "Minjia Zhang"
date: "2025-03-04"
time: "10:20–10:40"
room: "Acacia D"
doi: "10.1145/3710848.3710869"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# WeiPipe: Weight Pipeline Parallelism for Communication-Effective Long-Context Large Model Training

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出权重流水并行 WeiPipe，把流水线从传递激活改为传递权重及其梯度，在不依赖集合通信原语的前提下降低长上下文大模型训练的通信开销。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 6: Large Language Models</p>
</div>

**作者**：Junfeng Lin (Tsinghua University); Ziming Liu, Yang You (National University of Singapore); Jun Wang (CETHIK Group Co. Ltd.); Weihao Zhang (Lynxi Technologies Co. Ltd); Rong Zhao (Tsinghua University)

**会议**：PPoPP 2025 · 2025 年 3 月 4 日 10:20–10:40 · Session 6: Large Language Models（主席：Minjia Zhang）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710869) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 提出权重流水并行 WeiPipe，把流水线从传递激活改为传递权重及其梯度，在不依赖集合通信原语的前提下降低长上下文大模型训练的通信开销。

## 研究问题

长上下文 LLM 使激活及其梯度体积显著增大，传统流水并行因此面临更大的通信挑战，成为训练效率瓶颈。

## 方法简述

- 在流水线 worker 间只传递权重及其梯度，而不是激活。
- 不依赖集合通信原语，保证在通信受限环境下的可扩展性。
- 给出 WeiPipe-Interleave（强调通信效率）与 WeiPipe-zero-bubble（追求最小气泡率）等四种变体。

## 主要结果

- 在最多 32 块 GPU、NVLink+以太网与 PCIe+以太网等不同基础设施上，WeiPipe-Interleave 吞吐显著优于 SOTA 流水并行与 FSDP。
- 在通信受限场景下表现出更强的可扩展性。

<details>
<summary>原文摘要（英文）</summary>

Training large language models (LLMs) has become increasingly expensive due to the rapid expansion in model size. Pipeline parallelism is a widely used distributed training technique. However, as LLMs with larger context become prevalent and memory optimization techniques advance, traditional PP methods encounter greater communication challenges due to the increased size of activations and gradients of activations. To address this issue, we introduce weight-pipeline parallelism (WeiPipe) that transitions from an activation-passing pipeline to a weight-passing pipeline. WeiPipe reduces communication costs and achieves a more balanced utilization by transmitting only weights and their gradients between workers in a pipeline manner. WeiPipe does not rely on collective communication primitives, thus ensuring scalability. We present four variations of WeiPipe parallelism, including WeiPipe-Interleave, which emphasizes communication efficiency, and WeiPipe-zero-bubble, discussing the potential for minimal bubble ratios. Our implementation of WeiPipe-Interleave, performed on up to 32 GPUs and tested in various model configurations, including large-context LLM training, demonstrates a significant improvement in throughput compared to state-of-the-art pipeline parallelism and fully sharded data parallelism with different underlying infrastructures, including NVLink connections within cluster with Ethernet among cluster, and PCIe within cluster and Ethernet among cluster. Additionally, WeiPipe also shows greater scalability in communication-constrained scenarios compared to state-of-art strategies.

</details>

---

> 所属 Session：[Session 6: Large Language Models](index.md) · 返回 [PPoPP 2025 总览](../index.md)
