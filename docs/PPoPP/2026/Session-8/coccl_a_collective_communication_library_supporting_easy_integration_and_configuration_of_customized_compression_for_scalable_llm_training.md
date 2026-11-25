---
title: "COCCL: A Collective Communication Library Supporting Easy Integration and Configuration of Customized Compression for Scalable LLM Training"
description: "PPoPP 2026 Session 8（Distributed Training）：NCCL 之上的压缩集成通信库，3D 并行训练吞吐提升 1.24×"
tags:
  - "PPoPP2026"
  - "Session-8"
  - "Distributed Training"
  - "collective communication"
  - "compression"
  - "LLM training"
authors:
  - "Xingchen Liu"
  - "Haoran Kong"
  - "Hairui Zhao"
  - "Shengkai Lyu"
  - "Zheng Wei"
  - "Man Liu"
  - "Xingjian Tian"
  - "Liyang Zhao"
  - "Zhuohan Chen"
  - "Fakang Wang"
  - "Zizhong Chen"
  - "Zhan Wang"
  - "Guangming Tan"
  - "Dingwen Tao"
session: "Session 8: Distributed Training"
session_number: 8
session_chair: "Bo Fang"
date: "2026-02-03"
time: "14:10–14:30"
room: "Balmoral"
doi: "10.1145/3774934.3786432"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# COCCL: A Collective Communication Library Supporting Easy Integration and Configuration of Customized Compression for Scalable LLM Training

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出基于 NCCL 的集合通信库 COCCL，用可配置编程模型集成压缩并提供压缩感知算法与运行时重叠，70 亿参数 3D 并行训练吞吐提升 1.24 倍且精度不变。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 8: Distributed Training</p>
</div>

**作者**：Xingchen Liu, Haoran Kong, Hairui Zhao, Shengkai Lyu, Zheng Wei, Man Liu, Xingjian Tian, Liyang Zhao, Zhuohan Chen, Fakang Wang, Zizhong Chen, Zhan Wang, Guangming Tan, and Dingwen Tao — University of Chinese Academy of Sciences, China; Shenzhen Loop Area Institute, China; Chinese University of Hong Kong, Shenzhen, China; Jilin University, China; Ant Group, China

**会议**：PPoPP 2026 · 2026 年 2 月 3 日 14:10–14:30 · Session 8: Distributed Training（主席：Bo Fang）· Balmoral

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786432) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

Collective communication is critical to scaling large language model (LLM) training across various parallelism strategies, including data, tensor, and pipeline parallelism on GPU clusters. However, as model sizes and training scales increase, communication overhead is emerging as a major performance bottleneck. While compression is a promising mitigation strategy, existing solutions often lack user-transparency, hinder deployment and extensibility, and are not co-designed with communication algorithms. To address these limitations, we present COCCL, a high-performance collective communication library built on top of NCCL. COCCL introduces a novel programming model that can easily integrate compression into communication workflows with flexible configurability. It features a suite of compression-aware collective algorithms and runtime overlap mechanisms that mitigate error propagation and reduce computational overhead. We integrate well-established compression techniques into COCCL and tune the compression configurations during 3D-parallel training on GPT and Qwen models with up to 7 billion parameters. Using the optimal configuration (COCCL-3D), we achieve 1.24× throughput improvement while maintaining training accuracy.

## 中文摘要

集合通信对于在 GPU 集群上以数据并行、张量并行和流水线并行等多种并行策略扩展大语言模型（LLM）训练至关重要。然而，随着模型规模和训练规模的增长，通信开销正逐渐成为主要的性能瓶颈。压缩是一种有前景的缓解策略，但现有方案往往缺乏对用户的透明性、不利于部署与扩展，且未与通信算法协同设计。为解决这些局限，我们提出 COCCL，一个构建于 NCCL 之上的高性能集合通信库。COCCL 引入了一种新颖的编程模型，能够以灵活可配置的方式将压缩便捷地集成到通信工作流中。它提供了一套压缩感知的集合算法与运行时重叠机制，可缓解误差传播并降低计算开销。我们将成熟的压缩技术集成到 COCCL 中，并在参数量最高达 70 亿的 GPT 与 Qwen 模型的三维并行训练过程中调优压缩配置。采用最优配置（COCCL-3D）时，我们在保持训练精度的同时实现了 1.24 倍的吞吐提升。

## 英文关键词

Collective communication, large language model, training, communication compression

## 中文关键词

集合通信；大语言模型；训练；通信压缩

---

## 一句话总结

> 提出基于 NCCL 的集合通信库 COCCL，用可配置编程模型集成压缩并提供压缩感知算法与运行时重叠，70 亿参数 3D 并行训练吞吐提升 1.24 倍且精度不变。

## 研究问题

随着模型与训练规模扩大，通信开销成为主要性能瓶颈；现有压缩方案缺乏用户透明性、阻碍部署与扩展，且未与通信算法协同设计。

## 方法简述

- 提出新的编程模型，使压缩能够以灵活可配置的方式集成进通信流程。
- 设计一套压缩感知的集合通信算法。
- 采用运行时重叠机制，抑制误差传播并降低压缩带来的计算开销。
- 将成熟压缩技术集成到 COCCL，并在最多 70 亿参数的 GPT 与 Qwen 模型 3D 并行训练中调优压缩配置。

## 主要结果

- 在 GPT 与 Qwen 模型上完成 3D 并行训练压缩配置调优，采用最优配置 COCCL-3D 获得 1.24 倍吞吐提升。
- 在提升吞吐的同时保持了训练精度。

---

> 所属 Session：[Session 8: Distributed Training](index.md) · 返回 [PPoPP 2026 总览](../index.md)
