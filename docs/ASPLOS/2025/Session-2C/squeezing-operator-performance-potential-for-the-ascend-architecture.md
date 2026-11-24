---
title: "Squeezing Operator Performance Potential for the Ascend Architecture"
description: "ASPLOS 2025 · Session 2C · 挖掘 Ascend 架构的算子性能潜力"
tags:
  - "ASPLOS2025"
  - "Session 2C"
  - "Accelerators"
---

# Squeezing Operator Performance Potential for the Ascend Architecture

**中文标题：** 挖掘 Ascend 架构的算子性能潜力

**所属 Session：** [Session 2C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Yuhang Zhou (State Key Laboratory for Novel Software Technology, Nanjing University), Zhibin Wang (State Key Laboratory for Novel Software Technology, Nanjing University), Guyue Liu (Peking University), Shipeng Li (State Key Laboratory for Novel Software Technology, Nanjing University), Xi Lin (State Key Laboratory for Novel Software Technology, Nanjing University), Zibo Wang (State Key Laboratory for Novel Software Technology, Nanjing University), Yongzhong Wang (Huawei Technologies Co., Ltd.), Fuchun Wei (Huawei Technologies Co., Ltd.), Jingyi Zhang (Huawei Technologies Co., Ltd.), Zhiheng Hu (Huawei Technologies Co., Ltd.), Yanlin Liu (Huawei Technologies Co., Ltd.), Chunsheng Li (Huawei Technologies Co., Ltd.), Ziyang Zhang (Huawei Technologies Co., Ltd.), Yaoyuan Wang (Huawei Technologies Co., Ltd.), Bin Zhou (Shandong University), Wanchun Dou (Nanjing University, State Key Laboratory for Novel Software Technology), Guihai Chen (Nanjing University, State Key Laboratory for Novel Software Technology), Chen Tian (Nanjing University, State Key Laboratory for Novel Software Technology)

**单位：** State Key Laboratory for Novel Software Technology, Nanjing University；Peking University；Huawei Technologies Co., Ltd.；Shandong University；Nanjing University, State Key Laboratory for Novel Software Technology

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716243) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

With the rise of deep learning, many companies have developed domain-specific architectures (DSAs) optimized for AI workloads, with Ascend being a representative. To fully realize the operator performance on Ascend, effective analysis and optimization is urgently needed. Compared to GPU, Ascend requires users to manage operations manually, leading to complex performance issues that require precise analysis. ∗corresponding authors However, existing roofline models face challenges of visualization complexity and inaccurate performance assessment. To address these needs, we introduce a component-based roofline model that abstracts components to capture operator performance, thereby effectively identifying bottleneck components. Furthermore, through practical operator optimization case studies, we illustrate a comprehensive process of optimization based on roofline analysis, summarizing common performance issues and optimization strategies. Finally, extensive end-to-end optimization experiments demonstrate significant model speed improvements, ranging from 1.07× to 2.15×, along with valuable insights from practice.

## 中文摘要

随着深度学习的兴起，许多公司开发了针对 AI 负载优化的领域特定架构（DSA），Ascend 是其中的代表。为在 Ascend 上充分释放算子性能，迫切需要有效的分析与优化。与 GPU 相比，Ascend 要求用户手动管理各项操作，从而导致复杂的性能问题，需要精确的分析。然而，现有的 roofline 模型面临可视化复杂与性能评估不准确等挑战。为满足这些需求，我们提出一种基于组件的 roofline 模型，通过抽象组件来刻画算子性能，从而有效识别瓶颈组件。此外，通过实际的算子优化案例研究，我们展示了基于 roofline 分析的系统化优化流程，总结了常见的性能问题与优化策略。最后，大量端到端优化实验表明，模型速度获得 1.07× 至 2.15× 的显著提升，并给出了来自实践的有价值洞见。

## 英文关键词

AI Accelerator; Performance Modeling; Roofline Model; Operator Optimization

## 中文关键词

AI 加速器；性能建模；Roofline 模型；算子优化

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716243)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 2C](index.md) · [返回 ASPLOS 2025](../index.md)
