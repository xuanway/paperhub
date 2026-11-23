---
title: "Chip Architectures Under Advanced Computing Sanctions"
description: "ISCA 2025 · Session 7A · 先进计算制裁下的芯片架构"
tags:
  - "ISCA2025"
  - "Session 7A"
  - "ML Acceleration III"
---

# Chip Architectures Under Advanced Computing Sanctions

**中文标题：** 先进计算制裁下的芯片架构

**所属 Session：** [Session 7A](index.md) · [ISCA 2025](../index.md)

**作者：** August Ning, David Wentzlaff

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731012) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

The rise of large scale machine learning models has generated un- precedented requirements and demand on computing hardware to enable these trillion parameter models. However, the importance of these bleeding-edge chips to the global economy, technological advancement, and strategic national interests have made them tar- gets of sanctions. Recent advanced computing sanctions set limits on a device’s Total Processing Performance, device bandwidth, and Performance Density and placed export controls on flagship data center and consumer products. In this work, we present the first study on the architectural and economic externality implications of these advanced computing sanctions and their effects on large language model (LLM) inference. We identify which architectural parameters are limited under ex- isting regulations, and perform thorough design space exploration of compliant designs. Optimized designs are able to improve LLM inference prefill performance by 4% and decoding performance by 27% compared to a restricted device baseline. We then demonstrate how an architecture-first approach for computing policies allows chip designers and policymakers to craft efficient guidelines that achieve desired goals while minimizing negative externalities. We show how architectural features can unify marketing-based data center vs. non-data center regulations and how policies can be specified to create gaming-focused de- vice architectures which are inherently limited in AI performance. Augmenting existing performance metrics with insightful architec- tural constraints better predict workload performance. Combined metrics achieved up to 42.4x narrower distributions compared to using theoretical compute performance alone, enable targeted and efficient policies.

## 中文摘要

大规模机器学习模型兴起，对支撑万亿参数模型的算力硬件提出了前所未有的需求。但这类尖端芯片对全球经济、技术进步与国家战略利益至关重要，因此成为制裁对象。近期的先进计算制裁对芯片的总处理性能、带宽、性能密度设置上限，面向旗舰数据中心与消费级产品实施出口管制。

本文首次研究这类先进计算制裁带来的架构层面与经济外部性影响，以及它们对大语言模型（LLM）推理的作用。我们梳理现有法规所限制的架构参数，并对合规芯片设计开展充分的设计空间探索。对比受限基线设备，优化后的合规设计在LLM推理的预填充阶段性能提升4%，解码阶段提升27%。

本文继而论证：以架构优先的算力监管思路，能够帮助芯片设计者与政策制定者制定高效规则，在达成管控目标的同时降低负面外部效应。文章说明如何通过架构特征统一现有基于营销口径划分的数据中心/非数据中心监管规则；同时可以设计面向游戏场景的芯片架构，使其原生限制AI推理性能。
在原有性能指标基础上增加架构约束，能够更好预测负载实际性能。相比仅依靠理论算力指标，组合指标下的性能分布区间收窄最高可达42.4倍，支撑更精准、高效的监管政策。

## 英文关键词

Advanced Computing Sanctions, Artificial Intelligence

## 中文关键词

先进计算制裁, 人工智能

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731012)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 7A](index.md) · [返回 ISCA 2025](../index.md)
