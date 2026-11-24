---
title: "Mugi: Value Level Parallelism For Efficient LLMs"
description: "ASPLOS 2026 · Session 3A · Mugi：面向高效 LLM 的值级并行"
tags:
  - "ASPLOS2026"
  - "Session 3A"
  - "LLM Attention & KV Cache"
---

# Mugi: Value Level Parallelism For Efficient LLMs

**中文标题：** Mugi：面向高效 LLM 的值级并行

**所属 Session：** [Session 3A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Daniel Price (University of Central Florida), Prabhu Vellaisamy (Carnegie Mellon University), John Paul Shen (Carnegie Mellon University), Di Wu (University of Central Florida)

**单位：** University of Central Florida；Carnegie Mellon University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790189) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Value level parallelism (VLP) has been proposed to improve the efficiency of large-batch, low-precision general matrix multiply (GEMM) between symmetric activations and weights. In transformer based large language models (LLMs), there exist more sophisticated operations beyond activation-weight GEMM. In this paper, we explore how VLP benefits LLMs. First, we generalize VLP for nonlinear approximations, outperforming existing nonlinear approximations in end-toend LLM accuracy, performance, and efficiency. Our VLP approximation follows a value-centric approach, where important values are assigned with greater accuracy. Second, we optimize VLP for small-batch GEMMs with asymmetric inputs efficiently, which leverages timely LLM optimizations, including weight-only quantization, key-value (KV) cache quantization, and group query attention. Finally, we design a new VLP architecture, Mugi, to encapsulate the innovations above and support full LLM workloads, while providing better performance, efficiency and sustainability. Our experimental results show that Mugi can offer significant improvements on throughput and energy efficiency, up to 45× and 668× for nonlinear softmax operations, and 2.07× and 3.11× for LLMs, and also decrease operational carbon for LLM operation by 1.45× and embodied carbon by 1.48×.

## 中文摘要

值级并行（VLP）已被提出用于提升对称激活与权重之间大批量、低精度通用矩阵乘法（GEMM）的效率。在基于 transformer 的大语言模型（LLM）中，还存在激活-权重 GEMM 之外的更复杂操作。本文探讨 VLP 如何为 LLM 带来收益。首先，我们将 VLP 推广至非线性近似，在端到端 LLM 精度、性能和效率上均优于现有的非线性近似方法。我们的 VLP 近似采用以值为中心的方法，即重要值被赋予更高的精度。其次，我们针对具有非对称输入的小批量 GEMM 高效地优化 VLP，并借助当前的 LLM 优化技术，包括仅权重量化、键值（KV）缓存量化以及分组查询注意力。最后，我们设计了一种新的 VLP 架构 Mugi，以封装上述创新并支持完整的 LLM 工作负载，同时提供更好的性能、效率和可持续性。实验结果表明，Mugi 能在吞吐和能效上带来显著提升：非线性 softmax 操作最高分别达 45× 和 668×，LLM 最高分别达 2.07× 和 3.11×，同时将 LLM 运行的运行碳排放降低 1.45×、隐含碳排放降低 1.48×。

## 英文关键词

value-level parallelism, value reuse, data reuse, computation reuse, unary computing, temporal coding, quantization, general matrix multiplication, nonlinear approximation, large language model, KV cache, group query attention

## 中文关键词

值级并行；值复用；数据复用；计算复用；一元计算；时间编码；量化；通用矩阵乘法；非线性近似；大语言模型；KV 缓存；分组查询注意力

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790189)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 3A](index.md) · [返回 ASPLOS 2026](../index.md)
