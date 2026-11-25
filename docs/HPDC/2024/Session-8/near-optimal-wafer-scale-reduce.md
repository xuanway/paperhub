---
title: "Near-Optimal Wafer-Scale Reduce"
description: "HPDC 2024 · Session 8 — Communication & Storage"
tags:
  - "HPDC2024"
  - "Session 8"
  - "Communication & Storage"
---

# Near-Optimal Wafer-Scale Reduce

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2024 主会 Session 8 — Communication & Storage（2024年6月7日 14:00–15:40 · Session Chair：Bogdan Nicolae）。</p>
<p class="paper-seo-summary__tags">HPDC 2024 · Session 8</p>
</div>

**官方资料**：[HPDC 2024 官方议程](https://hpdc.sci.utah.edu/2024/program.html) · [ACM DOI](https://doi.org/10.1145/3625549.3658693)

**作者**：Piotr Luczynski, Lukas Gianinazzi, Patrick Iff, Leighton Wilson, Daniele De Sensi, Torsten Hoefler

**会议**：HPDC 2024 · Pisa, Italy

**Session**：Session 8 — Communication & Storage（2024年6月7日 14:00–15:40 · Session Chair：Bogdan Nicolae）

---

## 英文摘要

Efficient Reduce and AllReduce communication collectives are a critical cornerstone of high-performance computing (HPC) applications. We present the first systematic investigation of Reduce and AllReduce on the Cerebras Wafer-Scale Engine (WSE). This architecture has been shown to achieve unprecedented performance both for machine learning workloads and other computational problems like FFT. We introduce a performance model to estimate the execution time of algorithms on the WSE and validate our predictions experimentally for a wide range of input sizes. In addition to existing implementations, we design and implement several new algorithms specifically tailored to the architecture. Moreover, we establish a lower bound for the runtime of a Reduce operation on the WSE. Based on our model, we automatically generate code that achieves near-optimal performance across the whole range of input sizes. Experiments demonstrate that our new Reduce and AllReduce algorithms outperform the current vendor solution by up to 3.27×. Additionally, our model predicts performance with less than 4% error. The proposed communication collectives increase the range of HPC applications that can benefit from the high throughput of the WSE. Our model-driven methodology demonstrates a disciplined approach that can lead the way to further algorithmic advancements on wafer-scale architectures.

## 中文摘要

高效的 Reduce 与 AllReduce 通信集合操作是高性能计算（HPC）应用的关键基石。我们首次对 Cerebras 晶圆级引擎（WSE）上的 Reduce 与 AllReduce 进行系统研究。该架构已被证明在机器学习负载以及 FFT 等其他计算问题上能取得前所未有的性能。我们引入一个性能模型来估计 WSE 上算法的执行时间，并在广泛的输入规模上通过实验验证预测。除现有实现外，我们专门针对该架构设计并实现了若干新算法。此外，我们建立了 WSE 上 Reduce 操作运行时间的下界。基于我们的模型，我们自动生成代码，在整个输入规模范围内实现近最优性能。实验表明，我们新的 Reduce 与 AllReduce 算法相比当前厂商方案最高快 3.27 倍。并且，我们的模型预测性能的误差小于 4%。所提出的通信集合操作扩大了能够受益于 WSE 高吞吐的 HPC 应用范围。我们的模型驱动方法展示了一种严谨的途径，可引领晶圆级架构上进一步的算法进步。

## 英文关键词

Communication Collectives, Message Passing, Reduction

## 中文关键词

通信集合操作，消息传递，归约

---

[← 返回 Session 8 — Communication & Storage](index.md)
