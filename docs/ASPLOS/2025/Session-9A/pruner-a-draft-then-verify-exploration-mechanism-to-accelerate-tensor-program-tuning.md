---
title: "Pruner: A Draft-then-Verify Exploration Mechanism to Accelerate Tensor Program Tuning"
description: "ASPLOS 2025 · Session 9A · Pruner：一种加速张量程序调优的“先起草后验证”探索机制"
tags:
  - "ASPLOS2025"
  - "Session 9A"
  - "ML Compilers"
---

# Pruner: A Draft-then-Verify Exploration Mechanism to Accelerate Tensor Program Tuning

**中文标题：** Pruner：一种加速张量程序调优的“先起草后验证”探索机制

**所属 Session：** [Session 9A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Liang Qiao (University of Science and Technology of China), Jun Shi (University of Science and Technology of China), Xiaoyu Hao (University of Science and Technology of China), Xi Fang (University of Science and Technology of China), Sen Zhang (University of Science and Technology of China), Minfan Zhao (University of Science and Technology of China), Ziqi Zhu (University of Science and Technology of China), Junshi Chen (University of Science and Technology of China), Hong An (University of Science and Technology of China), Xulong Tang (University of Pittsburgh), Bing Li (NIO), Honghui Yuan (NIO), Xinyang Wang (NIO)

**单位：** University of Science and Technology of China；University of Pittsburgh；NIO

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716269) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Tensor program tuning is essential for the efficient deployment of deep neural networks. Search-based approaches have demonstrated scalability and effectiveness in automatically finding high-performance programs for specific hardware. However, the search process is often inefficient, taking hours or even days to discover optimal programs due to the exploration mechanisms guided by an accurate but slow-learned cost model. Meanwhile, the learned cost model trained on one platform cannot seamlessly adapt online to another, which we call cross-platform online unawareness. In this work, we propose Pruner and MoA-Pruner. Pruner is a "Draft-then-Verify" exploration mechanism that accelerates the schedule search process. Instead of applying the complex learned cost model to all explored candidates, Pruner drafts small-scale potential candidates by introducing a naive Symbol-based Analyzer (draft model), then identifies the best candidates by the learned cost model. MoA-Pruner introduces a Momentum online Adaptation strategy to address the cross-platform online unawareness. We incorporate Pruner into the TVM and conduct extensive experiments on three GPU-based platforms. Results show considerable speedup in schedule search time. In online tuning scenarios, Pruner and MoA-Pruner achieve an average speedup of 2.6× and 4.82× compared to Ansor. In offline tuning scenarios, Pruner achieves an average speedup of 4.75× and 4.05× compared to TenSet and TLP, respectively. Furthermore, Pruner achieves an average speedup of 4.08× compared to MetaSchedule on TensorCore.

## 中文摘要

张量程序调优对于深度神经网络的高效部署至关重要。基于搜索的方法在自动为特定硬件寻找高性能程序方面已展现出可扩展性与有效性。然而，由于这些探索机制由精确但学习缓慢的代价模型所引导，搜索过程往往效率低下，需要数小时甚至数天才能发现最优程序。同时，在一个平台上训练得到的代价模型无法无缝地在线适配到另一个平台，我们将这一现象称为跨平台在线无感知（cross-platform online unawareness）。在本工作中，我们提出 Pruner 与 MoA-Pruner。Pruner 是一种“先起草后验证”（Draft-then-Verify）的探索机制，用于加速调度搜索过程。Pruner 并不把复杂的已学习代价模型施加于全部已探索候选，而是先借助一个朴素的基于符号的分析器（Symbol-based Analyzer，即起草模型）起草小规模的有潜力的候选，再由已学习代价模型确定最佳候选。MoA-Pruner 引入一种动量在线适配（Momentum online Adaptation）策略来解决跨平台在线无感知问题。我们将 Pruner 集成到 TVM 中，并在三个基于 GPU 的平台上开展了大量实验。结果表明调度搜索时间获得了可观的加速。在在线调优场景下，Pruner 与 MoA-Pruner 相较 Ansor 分别取得平均 2.6× 和 4.82× 的加速。在离线调优场景下，Pruner 相较 TenSet 与 TLP 分别取得平均 4.75× 和 4.05× 的加速。此外，在 TensorCore 上 Pruner 相较 MetaSchedule 取得平均 4.08× 的加速。

## 英文关键词

code generation; compiler optimization; tensor program tuning

## 中文关键词

代码生成；编译器优化；张量程序调优

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716269)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 9A](index.md) · [返回 ASPLOS 2025](../index.md)
