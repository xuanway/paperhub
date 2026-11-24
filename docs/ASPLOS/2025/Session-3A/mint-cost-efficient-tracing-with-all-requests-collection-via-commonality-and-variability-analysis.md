---
title: "Mint: Cost-Efficient Tracing with All Requests Collection via Commonality and Variability Analysis"
description: "ASPLOS 2025 · Session 3A · Mint：通过共性与差异性分析实现全请求采集的低成本追踪"
tags:
  - "ASPLOS2025"
  - "Session 3A"
  - "Performance Analysis & Tracing"
---

# Mint: Cost-Efficient Tracing with All Requests Collection via Commonality and Variability Analysis

**中文标题：** Mint：通过共性与差异性分析实现全请求采集的低成本追踪

**所属 Session：** [Session 3A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Haiyu Huang (Sun Yat-sen University), Cheng Chen (Alibaba Group), Kunyi Chen (Alibaba Group), Pengfei Chen (Sun Yat-sen University), Guangba Yu (Sun Yat-sen University), Zilong He (Sun Yat-sen University), Yilun Wang (Sun Yat-sen University), Huxing Zhang (Alibaba Group), Qi Zhou (Alibaba Group)

**单位：** Sun Yat-sen University；Alibaba Group

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707287) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Distributed traces contain valuable information but are often massive in volume, posing a core challenge in tracing framework design: balancing the tradeoff between preserving essential trace information and reducing trace volume. To address this tradeoff, previous approaches typically used a '1 or 0' sampling strategy: retaining sampled traces while completely discarding unsampled ones. However, based on an empirical study on real-world production traces, we discover that the '1 or 0' strategy actually fails to effectively balance this tradeoff. To achieve a more balanced outcome, we shift the strategy from the '1 or 0' paradigm to the 'commonality + variability' paradigm. The core of 'commonality + variability' paradigm is to first parse traces into common patterns and variable parameters, then aggregate the patterns and filter the parameters. We propose a cost-efficient tracing framework, Mint, which implements the 'commonality + variability' paradigm on the agent side to enable all requests capturing. Our experiments show that Mint can capture all traces and retain more trace information while optimizing trace storage (reduced * Pengfei Chen is the corresponding author. to an average of 2.7%) and network overhead (reduced to an average of 4.2%). Moreover, experiments also demonstrate that Mint is lightweight enough for production use.

## 中文摘要

分布式追踪含有有价值的信息，但往往体量巨大，这给追踪框架设计带来了一个核心挑战：在保留关键追踪信息与降低追踪体量之间取得平衡。为应对这一权衡，以往方法通常采用"1 或 0"的采样策略：保留被采样的追踪，而完全丢弃未被采样的追踪。然而，基于对真实生产追踪的实证研究，我们发现"1 或 0"策略实际上未能有效平衡这一权衡。为获得更为均衡的结果，我们将策略从"1 或 0"范式转变为"共性 + 差异性"范式。"共性 + 差异性"范式的核心是先将追踪解析为共性模式与可变参数，再对模式进行聚合、对参数进行过滤。我们提出一种低成本追踪框架 Mint，它在 agent 侧实现"共性 + 差异性"范式，从而支持全请求采集。实验表明，Mint 能够捕获全部追踪并保留更多追踪信息，同时优化追踪存储（平均降低至 2.7%）与网络开销（平均降低至 4.2%）。此外，实验还表明 Mint 足够轻量，可满足生产环境使用。

## 英文关键词

原文无 Keywords

## 中文关键词

原文无 Keywords

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707287)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 3A](index.md) · [返回 ASPLOS 2025](../index.md)
