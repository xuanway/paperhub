---
title: "Exploring and Mitigating Failure Behavior of Large Language Model Training Workloads in HPC Systems"
description: "SC 2025 · Anomaly Detection, Failure Management, and Resilience 2 · Pengfei Yu; Jingjing Gu; Hao Han; Dazhong Shen; Bao Wen; Yang Liu"
tags:
  - "SC2025"
  - "Anomaly Detection, Failure Management, and Resilience 2"
---

# Exploring and Mitigating Failure Behavior of Large Language Model Training Workloads in HPC Systems

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Anomaly Detection, Failure Management, and Resilience 2。</p>
<p class="paper-seo-summary__tags">SC 2025 · Anomaly Detection, Failure Management, and Resilience 2</p>
</div>

**作者**：Pengfei Yu; Jingjing Gu; Hao Han; Dazhong Shen; Bao Wen; Yang Liu

**会议**：SC 2025 · St. Louis, MO

## 摘要

The exponential growth of large language model (LLM) training demands in HPC systems has exposed critical reliability challenges, particularly from transient faults. Unlike resilience studies in conventional DNN inference, the massive parameter scale and iterative updates in LLM training trigger more complex failure patterns. To address these challenges, we introduce LLMFI, a new fault injection tool, and reveal six distinct failure behaviors through 300K+ fault injection experiments (exceeding 5K GPU node-hours). Our key insight is that, while most injected faults are eventually masked by the training iteration mechanism, a critical subset leads to catastrophic failures or performance degradation. Further, we propose LLMFT, a novel machine-learning-based fault tolerance framework that implements closed-loop error control via heuristic feature extraction, fault detector, and dual recovery mechanisms. Extensive evaluation demonstrates that LLMFT achieves an average of 97.61% F1-score in

---

## 一句话总结

> 该工作属于 Anomaly Detection, Failure Management, and Resilience 2 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Anomaly Detection, Failure Management, and Resilience 2 领域贡献新的设计范式或评估框架。
