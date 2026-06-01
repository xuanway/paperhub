---
title: "MaverIQ: Fingerprint-Guided Extrapolation and Fragmentation-Aware Layering for Intent-Based LLM Serving"
description: "SC 2025 · Machine Learning: Inference and Serving · Dimitrios Liakopoulos; Prasoon Sinha; Tianrui Hu; Myungjin Lee; Neeraja J. Yadwa"
tags:
  - "SC2025"
  - "Machine Learning: Inference and Serving"
---

# MaverIQ: Fingerprint-Guided Extrapolation and Fragmentation-Aware Layering for Intent-Based LLM Serving

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Inference and Serving。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Inference and Serving</p>
</div>

**作者**：Dimitrios Liakopoulos; Prasoon Sinha; Tianrui Hu; Myungjin Lee; Neeraja J. Yadwadkar

**会议**：SC 2025 · St. Louis, MO

## 摘要

Large language models (LLMs) are becoming ubiquitous across industries, where applications demand diverse user intents. To meet those intents, developers must manually explore combinations of parallelism and compression techniques that affect resource usage, latency, cost, and accuracy. Prior works automate this process but incur high profiling costs, inefficient GPU use, or ignore diverse user-intents. We build MaverIQ, an automated intent-based LLM inference serving system that translates user-expressed intents into LLM deployment configurations and deploys the chosen configurations to improve operational cost for the provider. To reduce profiling costs, MaverIQ introduces and observes LLM fingerprint—a compact proxy of the LLM—under a few configurations, and uses novel analytical models to extrapolate the observed fingerprint data to the full LLM. To cut provider costs, we exploit our key observation that uneven LLM layer distribution minimally affects inference latency. MaverIQ cut

---

## 一句话总结

> 该工作属于 Machine Learning: Inference and Serving 方向，在高性能计算领域提出关键设计，在 SC 2025 语境下验证其价值。

## 方法简述

- 识别 HPC 系统中的核心挑战或性能瓶颈。
- 提出系统级或算法级优化方案，注重可扩展性。
- 在超算或大规模集群上进行充分评估。

## 主要结果

- 在性能、可扩展性或能效方面相对基线实现改进。
- 为 Machine Learning: Inference and Serving 领域贡献新的设计范式或评估框架。
