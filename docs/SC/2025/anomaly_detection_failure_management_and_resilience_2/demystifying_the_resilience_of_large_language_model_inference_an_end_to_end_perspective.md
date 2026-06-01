---
title: "Demystifying the Resilience of Large Language Model Inference: An End-to-End Perspective"
description: "SC 2025 · Anomaly Detection, Failure Management, and Resilience 2 · Yu Sun; Zachary Coalson; Shiyang Chen; Hang Liu; Zhao Zhang; Sanghyun Hong; Bo F"
tags:
  - "SC2025"
  - "Anomaly Detection, Failure Management, and Resilience 2"
---

# Demystifying the Resilience of Large Language Model Inference: An End-to-End Perspective

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Anomaly Detection, Failure Management, and Resilience 2。</p>
<p class="paper-seo-summary__tags">SC 2025 · Anomaly Detection, Failure Management, and Resilience 2</p>
</div>

**作者**：Yu Sun; Zachary Coalson; Shiyang Chen; Hang Liu; Zhao Zhang; Sanghyun Hong; Bo Fang; Lishan Yang

**会议**：SC 2025 · St. Louis, MO

## 摘要

Deep neural networks are known to be resilient to random bitwise faults in their parameters. However, this resilience has primarily been established through evaluations on classification models. The extent to which this claim holds for large language models remains under-explored. In this work, we conduct an extensive measurement study on the impact of random bitwise faults in commercial-scale language model inference. We first expose that these language models are not truly resilient to random bit-flips. While aggregate metrics such as accuracy may suggest resilience, an in-depth inspection of the generated outputs shows significant degradation in text quality. Our analysis also shows that tasks requiring more complex reasoning suffer more from performance and quality degradation. Moreover, we extend our resilience analysis to models with augmented reasoning capabilities, such as Chain of Thought or Mixture of Experts architectures.

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
