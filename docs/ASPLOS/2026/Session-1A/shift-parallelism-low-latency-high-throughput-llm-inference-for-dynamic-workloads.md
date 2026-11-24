---
title: "Shift Parallelism: Low-Latency, High-Throughput LLM Inference for Dynamic Workloads"
description: "ASPLOS 2026 · Session 1A · Shift Parallelism：面向动态工作负载的低延迟、高吞吐 LLM 推理"
tags:
  - "ASPLOS2026"
  - "Session 1A"
  - "LLM Serving: Throughput Optimization"
---

# Shift Parallelism: Low-Latency, High-Throughput LLM Inference for Dynamic Workloads

**中文标题：** Shift Parallelism：面向动态工作负载的低延迟、高吞吐 LLM 推理

**所属 Session：** [Session 1A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Mert Hidayetoglu (Snowflake), Aurick Qiao (Snowflake), Michael Wyatt (Snowflake), Jeff Rasley (Snowflake), Yuxiong He (Snowflake), Samyam Rajbhandari (Snowflake)

**单位：** Snowflake

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790219) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Efficient parallelism is necessary for achieving low-latency, high-throughput inference with large language models (LLMs). Tensor parallelism (TP) is the state-of-the-art method for reducing LLM response latency, however GPU communications reduces combined token throughput. On the other hand, data parallelism (DP) obtains a higher throughput yet is slow in response latency. Best of both worlds does not exist, and it is not possible to combine TP and DP because of the KV cache variance across the parallelisms. We notice Sequence Parallelism (SP—Ulysses in training) has similar properties as DP but with KV cache invariance. We adapt SP to inference, and combine it with TP to get the best of both worlds. Our solution: Shift Parallelism. Shift Parallelism dynamically switches across TP and SP, and minimizes latency in low traffic without losing throughput in high traffic. The efficient GPU communications of Shift Parallelism yields up to i) 1.51× faster response in interactive workloads and ii) 50% higher throughput in batch workloads, compared to a TP-only solution. We evaluate Shift Parallelism with real-world production traces with dynamic traffic patterns as well as synthetic benchmarking patterns across models, context sizes, and arrival rates. All results affirm the same: Shift Parallelism has a better latency vs. throughput tradeoff than TP or DP, and hence obtains low latency without degrading throughput in dynamic workloads.

## 中文摘要

高效的并行策略是实现大语言模型（LLM）低延迟、高吞吐推理的必要条件。张量并行（TP）是降低 LLM 响应延迟的当前最优方法，但 GPU 间通信会降低合计的 token 吞吐。另一方面，数据并行（DP）可获得更高吞吐，但响应延迟较高。两者兼得的最优解并不存在，且由于不同并行方式之间 KV cache 存在差异，无法直接组合 TP 与 DP。我们注意到序列并行（SP——在训练中即 Ulysses）具有与 DP 相似的特性，但保持 KV cache 不变性。我们将 SP 适配到推理场景，并与 TP 结合以兼得两者之长。我们的方案是：Shift Parallelism。Shift Parallelism 在 TP 与 SP 之间动态切换，在低流量时最小化延迟，同时在高流量下不损失吞吐。与仅采用 TP 的方案相比，Shift Parallelism 高效的 GPU 通信带来：i）交互式工作负载下响应速度最高提升 1.51×；ii）批处理工作负载下吞吐最高提升 50%。我们使用具有动态流量模式的真实生产轨迹，以及跨不同模型、上下文长度和请求到达率的合成基准模式来评估 Shift Parallelism。所有结果都印证了同一点：Shift Parallelism 在延迟与吞吐之间取得了优于 TP 或 DP 的权衡，因而能在动态工作负载下获得低延迟而不降低吞吐。

## 英文关键词

原文无 Keywords

## 中文关键词

原文无 Keywords

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790219)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 1A](index.md) · [返回 ASPLOS 2026](../index.md)
