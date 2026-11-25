---
title: "Liger: Interleaving Intra- and Inter-Operator Parallelism for Distributed Large Model Inference"
description: "PPoPP 2024 Session Compilers and Runtimes for Parallel Systems：跨请求交错计算与通信，4 卡延迟降 36.0%、吞吐升 1.34×"
tags:
  - "PPoPP2024"
  - "Session-2"
  - "Compilers and Runtimes for Parallel Systems"
  - "distributed inference"
  - "GPU scheduling"
  - "multi-GPU"
authors:
  - "Jiangsu Du"
  - "Jinhui Wei"
  - "Jiazhi Jiang"
  - "Shenggan Cheng"
  - "Zhiguang Chen"
  - "Dan Huang"
  - "Yutong Lu"
session: "Session 2: Compilers and Runtimes for Parallel Systems"
session_number: 2
session_chair: "Mohamed Riyadh Baghdadi"
date: "2024-03-04"
time: "11:30–11:50"
room: "Moorfoot"
doi: "10.1145/3627535.3638466"
program_url: "https://ppopp24.sigplan.org/program/program-PPoPP-2024/"
---

# Liger: Interleaving Intra- and Inter-Operator Parallelism for Distributed Large Model Inference

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 Liger 分布式推理运行时，将跨请求的计算与通信内核交错调度到多 GPU 的多条流上，并预判竞争、拆分长内核；4 卡下延迟降 36.0%、吞吐升 1.34×。</p>
<p class="paper-seo-summary__tags">PPoPP 2024 · Session 2: Compilers and Runtimes for Parallel Systems</p>
</div>

**作者**：Jiangsu Du, Jinhui Wei, Jiazhi Jiang (Sun Yat-sen University); Shenggan Cheng (National University of Singapore); Zhiguang Chen, Dan Huang, Yutong Lu (Sun Yat-sen University)

**会议**：PPoPP 2024 · 2024 年 3 月 4 日 11:30–11:50 · Session 2: Compilers and Runtimes for Parallel Systems（主席：Mohamed Riyadh Baghdadi）· Moorfoot

**论文**：[ACM Digital Library](https://doi.org/10.1145/3627535.3638466) · [PPoPP 2024 会议日程](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

---

## 英文摘要

Distributed large model inference is still in a dilemma where balancing cost and effect. The online scenarios demand intra-operator parallelism to achieve low latency and intensive communications makes it costly. Conversely, the inter-operator parallelism can achieve high throughput with much fewer communications, but it fails to enhance the effectiveness. In this paper, we present Liger, a distributed large model inference runtime system that is of capability to achieve low latency at high throughput on the multi-GPU architecture. The key idea lies in the novel interleaved parallelism, which interleaves the computation and communication across requests. Liger enables this parallelism by carefully scheduling computation and communication kernels across requests onto multiple streams of multiple GPUs. It achieves precise control of kernel execution order efficiently by mixing use the CPU-GPU synchronization and the inter-stream synchronization. To prevent scheduling failures caused by resource contention, Liger introduces a contention factor strategy to anticipate the penalty of contention. It enables a higher degree of overlap by decomposing lengthy kernels into smaller, more manageable units at runtime. Extensive evaluations show that Liger, in most cases, outperforms existing parallelism approaches across models and devices, presenting the best latency and throughput results. In a 4-device case, Liger reduces the average latency by 36.0% while maintaining the same throughput compared to the inter-operator approach. Meanwhile, it improves the throughput by 1.34× with improved average latency compared to the intra-operator approach.

## 中文摘要

分布式大模型推理仍处于成本与效果难以兼顾的困境。在线场景要求算子内并行以实现低延迟，而密集的通信使其代价高昂。相反，算子间并行能以少得多的通信获得高吞吐，但无法提升效果。在本文中，我们提出 Liger，一个分布式大模型推理运行时系统，能够在多 GPU 架构上以高吞吐实现低延迟。其核心思想是新颖的交错并行（interleaved parallelism），它在请求之间交错计算与通信。Liger 通过将不同请求的计算与通信内核精心调度到多个 GPU 的多条流上来实现这种并行。它混合使用 CPU-GPU 同步与流间同步，从而高效地精确控制内核执行顺序。为防止资源竞争导致的调度失败，Liger 引入了竞争因子（contention factor）策略来预判竞争惩罚。它通过在运行时将冗长的内核分解为更小、更易管理的单元，实现更高程度的重叠。大量评估表明，在大多数情况下，Liger 在多种模型与设备上优于现有的并行方法，给出最佳的延迟与吞吐结果。在 4 设备场景下，与算子间方法相比，Liger 在保持相同吞吐的同时将平均延迟降低 36.0%。同时，与算子内方法相比，它在平均延迟有所改善的情况下将吞吐提升 1.34×。

## 英文关键词

Distributed Large Model Inference, GPU Scheduling, Multi-GPU Architecture

## 中文关键词

分布式大模型推理；GPU 调度；多 GPU 架构

---

## 一句话总结

> 提出 Liger 分布式推理运行时，将跨请求的计算与通信内核交错调度到多 GPU 的多条流上，并预判竞争、拆分长内核；4 卡下延迟降 36.0%、吞吐升 1.34×。

## 研究问题

在线场景需要算子内并行以获得低延迟，但密集通信使其代价高昂；算子间并行能以更少通信获得高吞吐，却无法改善效果，难以兼顾成本与效果。

## 方法简述

- 提出跨请求的交错并行（interleaved parallelism），在请求之间交错计算与通信
- 将不同请求的计算与通信内核调度到多个 GPU 的多条流上，并混合使用 CPU-GPU 同步与流间同步来精确控制内核执行顺序
- 引入竞争因子（contention factor）策略预判资源竞争的惩罚，避免竞争导致的调度失败
- 在运行时将冗长内核分解为更小、更易管理的单元，以获得更高程度的重叠

## 主要结果

- 在 4 设备场景下，相比算子间方法在保持相同吞吐的同时将平均延迟降低 36.0%
- 相比算子内方法，吞吐提升 1.34× 且平均延迟有所改善
- 在多数情况下于多种模型与设备上优于现有并行方法，给出最佳延迟与吞吐

---

> 所属 Session：[Session 2: Compilers and Runtimes for Parallel Systems](index.md) · 返回 [PPoPP 2024 总览](../index.md)
