---
title: "gLLM: Global Balanced Pipeline Parallelism Systems for Distributed LLMs Serving with Token Throttling"
description: "SC 2025 · Machine Learning: Inference and Serving · Tianyu Guo; Xianwei Zhang; Jiangsu Du; Zhiguang Chen; Nong Xiao; Yutong Lu"
tags:
  - "SC2025"
  - "Machine Learning: Inference and Serving"
---

# gLLM: Global Balanced Pipeline Parallelism Systems for Distributed LLMs Serving with Token Throttling

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 SC 2025，所属方向：Machine Learning: Inference and Serving。</p>
<p class="paper-seo-summary__tags">SC 2025 · Machine Learning: Inference and Serving</p>
</div>

**作者**：Tianyu Guo; Xianwei Zhang; Jiangsu Du; Zhiguang Chen; Nong Xiao; Yutong Lu

**会议**：SC 2025 · St. Louis, MO

## 摘要

Pipeline parallelism has emerged as a predominant approach for deploying LLMs across distributed nodes. However, it often suffers from performance limitations caused by pipeline bubbles, which primarily result from imbalanced computation delays across batches. Existing methods attempt to address this through hybrid scheduling of chunked prefill and decode tokens. However, such methods may experience significant fluctuations due to either insufficient prefill tokens or uneven distribution of decode tokens, ultimately leading to computational imbalance. To overcome these inefficiencies, we present gLLM, a globally balanced system incorporating token throttling. Our token throttling mechanism is a fine-grained scheduling policy that independently regulates the quantities of prefill and decode tokens by leveraging global information from the inference system. Furthermore, gLLM runtime adopts an asynchronous execution and message passing architecture. Evaluations show that gLLM delivers 11%

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
