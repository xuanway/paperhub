---
title: "Towards a Noise-Resilient TAGE via PURE"
description: "MICRO 2026 · Session 3A · 通过 PURE 构建抗噪声 TAGE 分支预测器"
tags:
  - "MICRO2026"
---

# Towards a Noise-Resilient TAGE via PURE

**中文标题：** 通过 PURE 构建抗噪声 TAGE 分支预测器

**所属 Session：** [Session 3A](index.md) · [MICRO 2026](../index.md)

**作者：** Tingji Zhang, Fang Su, Peng Qu, Wenjian He, Xiaoyi Liu, Xuefeng Zhang, Youhui Zhang

**来源：** MICRO 2026，pp. 929–943；[DOI](https://doi.org/10.1109/MICRO67795.2026.00075)

## 英文摘要

Modern server workloads exhibit large instruction footprints and complex control-flow, leading to significant mispredictions even for the state-of-the-art TAGE-SC-L. We demonstrate that prediction quality is not primarily limited by TAGE's intrinsic representational power or capacity, but by indiscriminate allocations that waste predictor capacity and impede online learning. Our analysis reveals that if shielded from unnecessary allocations, a standard 64KB TAGE can achieve performance approaching that of an infinite-capacity TAGE. Driven by this observation, we propose PURE (Pattern-Utility Rejection of Entry Allocation), a mechanism based on input sanitization. Unlike existing profile-guided solutions that bypass the predictor by offloading targeted branches to auxiliary models, PURE uses offline profiles to identify and filter noise-dominated patterns before they enter the predictor. This approach improves TAGE's learning efficiency and preserves capacity for useful patterns across branches of varying prediction difficulty. Across 12 widely used server applications, PURE reduces MPKI by an average of 25.2% (7.8% to 41.7%) over a 64KB TAGE-SC-L, outperforming state-of-the-art profile-guided schemes by 9.3% with 22KB of metadata.

## 中文摘要

现代服务器工作负载表现出庞大的指令占用空间和复杂的控制流，即使对于最先进的 TAGE-SC-L 也会导致严重的预测错误。我们证明，预测质量主要不受 TAGE 内在表征能力或能力的限制，而是受到浪费预测能力并阻碍在线学习的不加区别的分配的限制。我们的分析表明，如果避免不必要的分配，标准 64KB TAGE 可以实现接近无限容量 TAGE 的性能。在这一观察的推动下，我们提出了 PURE（模式实用程序拒绝条目分配），这是一种基于输入清理的机制。与通过将目标分支卸载到辅助模型来绕过预测器的现有配置文件引导解决方案不同，PURE 使用离线配置文件在噪声主导的模式进入预测器之前识别和过滤它们。这种方法提高了 TAGE 的学习效率，并保留了跨不同预测难度的分支的有用模式的能力。在 12 个广泛使用的服务器应用程序中，PURE 比 64KB TAGE-SC-L 平均减少了 MPKI 25.2%（7.8% 到 41.7%），比使用 22KB 元数据的最先进的配置文件引导方案高出 9.3%。

## 中文关键词

分支预测；TAGE；噪声抑制；微架构；预测准确率

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 3A](index.md) · [MICRO 2026 主页](../index.md)
