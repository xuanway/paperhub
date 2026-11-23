---
title: "Enabling Ahead Prediction with Practical Energy Constraints"
description: "ISCA 2025 · Session 4B · 在实际能耗约束下实现超前预测"
tags:
  - "ISCA2025"
  - "Session 4B"
  - "Microarchitecture I"
---

# Enabling Ahead Prediction with Practical Energy Constraints

**中文标题：** 在实际能耗约束下实现超前预测

**所属 Session：** [Session 4B](index.md) · [ISCA 2025](../index.md)

**作者：** Chester(Lingzhe) Cai, Aniket Deshmukh, Yale Patt

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3730998) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Accurate branch predictors require multiple cycles to produce a prediction, and that latency hurts processor performance. "Ahead prediction" solves the performance problem by starting the predic- tion early. Unfortunately, this means making the prediction without the directions of the N branches between when the prediction starts and when the relevant branch’s prediction is needed. The energy required to consider all 2𝑛 possible cases increases by 14.6x, mak- ing ahead prediction not viable. This paper shows that most of the intermediate branch directions never materialize, reducing the number of observed missing history patterns significantly (usually, only one or two). We modified the TAGE predictor to eliminate those branches from having to be considered. The result, our ahead predictor can produce a performance benefit of 4.4%, while causing an increase in energy consumption of only 1.5x, far less than the 14.6x that was thought to be necessary, and very much viable.

## 中文摘要

高精度分支预测器需要多个周期才能输出预测结果，该延迟会损害处理器性能。“提前预测”通过尽早启动预测来解决该性能问题。但弊端在于：从预测启动到需要得到目标分支预测结果这段时间内，中间存在N条分支，预测时还不知道这些分支的走向，需要对所有2ⁿ种可能情况进行考量，能耗上涨至原来的14.6倍，使得提前预测方案难以落地。
本文发现，绝大多数中间分支的实际走向并不会全部出现，观测到的缺失历史模式数量大幅减少（通常仅一到两种）。我们对TAGE预测器进行改造，不再需要对这些分支进行遍历考量。最终，该提前预测器可以带来4.4%的性能收益，而能耗仅提升至原来的1.5倍，远低于之前认为必需的14.6倍，具备很高的可行性。

## 英文关键词

CPU architecture, Branch Prediction

## 中文关键词

CPU架构, 分支预测

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3730998)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 4B](index.md) · [返回 ISCA 2025](../index.md)
