---
title: "Beyond SMARTS: Improving Simulation Accuracy with Ranked Set Sampling and Repeated Subsampling"
description: "MICRO 2026 · Session 7B · 超越 SMARTS：通过排序集采样与重复子采样提高仿真精度"
tags:
  - "MICRO2026"
  - "Simulation"
---

# Beyond SMARTS: Improving Simulation Accuracy with Ranked Set Sampling and Repeated Subsampling

**中文标题：** 超越 SMARTS：通过排序集采样与重复子采样提高仿真精度

**所属 Session：** [Session 7B](index.md) · [MICRO 2026](../index.md)

**作者：** Magnus Ekman

**来源：** MICRO 2026，pp. 2468–2478；[DOI](https://doi.org/10.1109/MICRO67795.2026.00169)

## 英文摘要

Computer system simulation studies routinely rely on executing a limited number of short application regions, since full end-to-end simulation is prohibitively time-consuming. To preserve representativeness, existing methods employ either statistical sampling or phase-based characterization to identify representative regions. In this work, we revisit statistical sampling in the context of computer architecture simulation. To assess how the confidence interval varies with different micro-architectural configurations, we examine how the sample standard deviation relates to the sample mean. We show that the ranked set sampling (RSS) technique - well established in the statistical literature - maps naturally to architectural simulation and yields significantly tighter confidence intervals than simple random sampling. Across our experiments, RSS reduces the confidence interval width by up to 50%. We further introduce a repeated subsampling scheme that identifies representative simulation regions for future studies. For a fixed sample size, this approach reduces the maximum observed error from 35% to 10%. Evaluating two selection criteria, we find that more informed subsample selection provides additional accuracy gains. Overall, our method achieves an average error below 2% and a maximum error of 3.5% across individual SPEC CPU 2017 Integer applications when simulating 30 regions of 1 million instructions each.

## 中文摘要

计算机系统仿真研究通常依赖于执行有限数量的短应用程序区域，因为完整的端到端仿真非常耗时。为了保持代表性，现有方法采用统计采样或基于阶段的表征来识别代表性区域。在这项工作中，我们在计算机体系结构模拟的背景下重新审视统计采样。为了评估置信区间如何随不同的微架构配置而变化，我们检查样本标准差与样本均值的关系。我们表明，统计文献中广泛采用的排名集抽样（RSS）技术自然地映射到架构模拟，并且比简单的随机抽样产生更严格的置信区间。在我们的实验中，RSS 将置信区间宽度减少了 50%。我们进一步引入了重复子采样方案，该方案可以确定未来研究的代表性模拟区域。对于固定样本量，此方法将最大观察误差从 35% 降低到 10%。评估两个选择标准，我们发现更明智的子样本选择可以提供额外的准确性增益。总体而言，当模拟 30 个区域（每个区域包含 100 万条指令）时，我们的方法在各个 SPEC CPU 2017 整数应用程序中实现了低于 2% 的平均误差和 3.5% 的最大误差。

## 中文关键词

体系结构仿真；排序集抽样；重复子抽样；仿真精度

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 7B](index.md) · [MICRO 2026 主页](../index.md)
