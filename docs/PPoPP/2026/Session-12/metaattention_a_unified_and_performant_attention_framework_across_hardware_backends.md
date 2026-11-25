---
title: "MetaAttention: A Unified and Performant Attention Framework across Hardware Backends"
description: "PPoPP 2026 Session 12（Optimizing Transformers）：打分+聚合抽象跨后端自动调优，原不支持配置最高 10.4×"
tags:
  - "PPoPP2026"
  - "Session-12"
  - "Optimizing Transformers"
  - "Attention"
  - "Cross-backend Runtime"
  - "Auto-tuning"
authors:
  - "Feiyang Chen"
  - "Yu Cheng"
  - "Lei Wang"
  - "Yuqing Xia"
  - "Ziming Miao"
  - "Lingxiao Ma"
  - "Fan Yang"
  - "Jilong Xue"
  - "Zhi Yang"
  - "Mao Yang"
  - "Xingda Wei"
  - "Haibo Chen"
session: "Session 12: Optimizing Transformers"
session_number: 12
session_chair: "Shaoshuai Zhang"
date: "2026-02-03"
time: "17:55–18:15"
room: "Pyrmont"
doi: "10.1145/3774934.3786444"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# MetaAttention: A Unified and Performant Attention Framework across Hardware Backends

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 MetaAttention，把注意力变体抽象为打分与聚合两类操作并构建跨后端运行时，用 IntermediateTensor 搜索分块与并行方案，最高 10.4× 加速。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 12: Optimizing Transformers</p>
</div>

**作者**：Feiyang Chen, Yu Cheng, Lei Wang, Yuqing Xia, Ziming Miao, Lingxiao Ma, Fan Yang, Jilong Xue, Zhi Yang, Mao Yang, Xingda Wei, and Haibo Chen — Shanghai Jiao Tong University, China; Peking University, China; Microsoft Research, China

**会议**：PPoPP 2026 · 2026 年 2 月 3 日 17:55–18:15 · Session 12: Optimizing Transformers（主席：Shaoshuai Zhang）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786444) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

Computing attention is the backbone of transformer-based models like large language models. However, the increasing diversity of attention algorithms presents significant challenges for unleashing hardware performance. State-of-the-art variants like FlashAttention target a specific attention algorithm or hardware platform, which fail to generalize to other algorithms and platforms. We present MetaAttention, a framework that automatically derives the optimal implementation of an attention algorithm given a hardware platform. Our key insight is that variants of attention can be abstracted into two operations: relevance scoring and aggregation, complemented by customizable functions and configurations like the input shape. Based on it, we systematically design a cross-backend attention runtime around these operations that generalizes to variants of attention with customizable operators. To unleash the hardware performance, we further propose an IntermediateTensor-based search method to find the optimal tiling strategy and the parallelism scheme according to the attention customization and hardware features. MetaAttention delivers up to a 10.4× speedup for configurations previously unsupported by state-of-the-art systems. Additionally, MetaAttention achieves performance comparable to manually-optimized libraries such as FlashMLA while significantly reducing the amount of code required.

## 中文摘要

计算注意力是 Transformer 类模型（如大语言模型）的支柱。然而，注意力算法的日益多样化给释放硬件性能带来了重大挑战。FlashAttention 等最先进的变体针对特定的注意力算法或硬件平台，无法泛化到其他算法与平台。我们提出 MetaAttention，一个能够针对给定硬件平台自动推导出注意力算法最优实现的框架。我们的关键洞见是：各类注意力变体都可抽象为两种操作——相关性评分与聚合，并辅以可定制的函数与配置（如输入形状）。基于此，我们围绕这些操作系统地设计了一个跨后端注意力运行时，可泛化到带有可定制算子的各类注意力变体。为释放硬件性能，我们进一步提出基于 IntermediateTensor 的搜索方法，根据注意力的定制化需求与硬件特征寻找最优分块策略与并行方案。对于此前最先进系统不支持的配置，MetaAttention 可提供最高 10.4× 的加速。此外，MetaAttention 在显著减少所需代码量的同时，达到与 FlashMLA 等手工优化库相当的性能。

## 英文关键词

Attention mechanism, GPU acceleration, Kernel optimization, Cross-platform, Large language models

## 中文关键词

注意力机制；GPU 加速；核函数优化；跨平台；大语言模型

---

## 一句话总结

> 提出 MetaAttention，把注意力变体抽象为打分与聚合两类操作并构建跨后端运行时，用 IntermediateTensor 搜索分块与并行方案，最高 10.4× 加速。

## 研究问题

注意力算法变体日益多样，而 FlashAttention 等最先进方案只针对特定注意力算法或硬件平台，无法泛化到其他算法与平台，难以持续释放硬件性能。

## 方法简述

- 将注意力变体抽象为相关性打分（relevance scoring）与聚合（aggregation）两类操作，并支持可定制算子函数与输入形状等配置。
- 围绕这两类操作系统性设计跨后端的注意力运行时，使其可泛化到带可定制算子的各类注意力变体。
- 提出基于 IntermediateTensor 的搜索方法，依据注意力定制方式与硬件特征寻找最优分块策略与并行方案。

## 主要结果

- 对现有系统此前不支持的配置，最高取得 10.4× 加速。
- 性能与 FlashMLA 等手工优化库相当，同时显著减少了所需代码量。

---

> 所属 Session：[Session 12: Optimizing Transformers](index.md) · 返回 [PPoPP 2026 总览](../index.md)
