---
title: "Using Analytical Performance/Power Model and Fine-Grained DVFS to Enhance AI Accelerator Energy Efficiency"
description: "ASPLOS 2025 · Session 5A · 利用解析式性能/功耗模型与细粒度 DVFS 提升 AI 加速器能效"
tags:
  - "ASPLOS2025"
  - "Session 5A"
  - "ML Systems 1"
---

# Using Analytical Performance/Power Model and Fine-Grained DVFS to Enhance AI Accelerator Energy Efficiency

**中文标题：** 利用解析式性能/功耗模型与细粒度 DVFS 提升 AI 加速器能效

**所属 Session：** [Session 5A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Zibo Wang (State Key Laboratory for Novel Software Technology, Nanjing University), Yijia Zhang (Peng Cheng Laboratory), Fuchun Wei (Huawei Technologies Co., Ltd), Bingqiang Wang (Peng Cheng Laboratory), Yanlin Liu (Huawei Technologies Co., Ltd), Zhiheng Hu (Huawei Technologies Co., Ltd), Jingyi Zhang (Huawei Technologies Co., Ltd), Xiaoxin Xu (Huawei Technologies Co., Ltd), Jian He (Huawei Technologies Co., Ltd), Xiaoliang Wang (State Key Laboratory for Novel Software Technology, Nanjing University), Wanchun Dou (State Key Laboratory for Novel Software Technology, Nanjing University), Guihai Chen (State Key Laboratory for Novel Software Technology, Nanjing University), Chen Tian (State Key Laboratory for Novel Software Technology, Nanjing University)

**单位：** State Key Laboratory for Novel Software Technology, Nanjing University；Peng Cheng Laboratory；Huawei Technologies Co., Ltd

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707231) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Recent advancements in deep learning have significantly increased AI processors' energy consumption, which is becoming a critical factor limiting AI development. Dynamic Voltage and Frequency Scaling (DVFS) stands as a key method in power optimization. However, due to the latency of DVFS control in AI processors, previous works typically apply DVFS control at the granularity of a program's entire duration or sub-phases, rather than at the level of AI operators. The advent of millisecond-level DVFS capabilities on the latest Ascend NPU platforms enables us to set frequency ∗corresponding authors individually for single or multiple operators, opening up the opportunity for further enhancing energy efficiency through fine-grained DVFS control. To ensure performance is unaffected in DVFS, our work builds performance and power models for each operator. Through in-depth timeline analysis, we demonstrate that the cycle count of an operator can be modeled as a convex piecewise linear function of frequency, resulting in a performance model with an average error of 1.96%. Moreover, we build power models that incorporate temperature-dependent terms, which enhances the model's precision and results in an average error of 4.62%. Based on our performance and power models as well as the fine-grained DVFS functionality of Ascend NPU, we propose a DVFS strategy that integrates operator classification, preprocessing, and a genetic algorithm-based search. Experiments on applications including GPT-3 training achieve a reduction in AICore (the computing component within the Ascend NPU) power by 13.44% and NPU chip power by 4.95%, while limiting performance degradation to 1.76%.

## 中文摘要

近期深度学习的进展显著提高了 AI 处理器的能耗，能耗正成为制约 AI 发展的关键因素。动态电压频率调节（DVFS）是功耗优化的关键方法。然而，由于 AI 处理器中 DVFS 控制存在延迟，先前工作通常以程序的整个执行时长或子阶段为粒度施加 DVFS 控制，而不是在 AI 算子级别施加控制。最新昇腾 NPU 平台上毫秒级 DVFS 能力的出现，使我们能够为单个或多个算子分别设置频率，从而为通过细粒度 DVFS 控制进一步提升能效提供了机会。为确保 DVFS 中性能不受影响，我们的工作为每个算子构建了性能模型与功耗模型。通过深入的时间线分析，我们证明算子的周期数可以建模为频率的凸分段线性函数，由此得到的性能模型平均误差为 1.96%。此外，我们构建了包含温度相关项的功耗模型，这提升了模型的精度，平均误差为 4.62%。基于我们的性能模型与功耗模型以及昇腾 NPU 的细粒度 DVFS 功能，我们提出一种融合算子分类、预处理与基于遗传算法搜索的 DVFS 策略。在包括 GPT-3 训练在内的应用上的实验，使 AICore（昇腾 NPU 内的计算部件）功耗降低 13.44%，NPU 芯片功耗降低 4.95%，同时将性能下降限制在 1.76%。

## 英文关键词

AI Accelerator; Performance Model; Power Model; Fine-grained DVFS; Genetic Algorithm

## 中文关键词

AI 加速器；性能模型；功耗模型；细粒度 DVFS；遗传算法

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707231)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 5A](index.md) · [返回 ASPLOS 2025](../index.md)
