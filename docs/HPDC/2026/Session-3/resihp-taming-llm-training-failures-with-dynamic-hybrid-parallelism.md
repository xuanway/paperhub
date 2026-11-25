---
title: "ResiHP: Taming LLM Training Failures with Dynamic Hybrid Parallelism"
description: "HPDC 2026 · Session 3 — MoE Systems & Distributed LLM Training"
tags:
  - "HPDC2026"
  - "Session 3"
  - "MoE Systems & Distributed LLM Training"
---

# ResiHP: Taming LLM Training Failures with Dynamic Hybrid Parallelism

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 3 — MoE Systems & Distributed LLM Training（2026年7月14日 13:30–14:30 · Session Chair：Peter Dinda）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 3</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807815)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#MaGGLYWL26](https://dblp.org/db/conf/hpdc/hpdc2026.html#MaGGLYWL26)

**作者**：Tenghui Ma, Jihu Guo, Wei Gao, Sitian Lu, Zhisheng Ye, Hanjing Wang, Dahua Lin

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 3 — MoE Systems & Distributed LLM Training（2026年7月14日 13:30–14:30 · Session Chair：Peter Dinda）

---

## 英文摘要

Hybrid parallelism underpins large-scale LLM training across tens of thousands of GPUs. At such scale, hardware failures on individual devices lead to performance skew across devices, diminishing overall training efficiency. Existing resilient systems overlook sequence length variability in datasets and device performance skew under hybrid parallelism. As a result, (1) iteration time fluctuations induced by sequence length variability can trigger spurious fail-slow detections, and (2) failures are mitigated through individual adaptations in hybrid parallelism, leading to unnecessary detection overhead and inefficient resilient training. To respond, this paper presents ResiHP, a resilient system that enables robust failure detection and fine-grained adaptation for hybrid parallel training. First, we develop a Detector to accurately identify failures. In particular, it employs a workload-aware execution time predictor that disentangles failures from iteration time fluctuations while remaining lightweight for online detection. Second, we design a Scheduler that dynamically adapts parallelism group sizes, model partitioning, and workload scheduling policies to improve training efficiency under failures. Experiments show that ResiHP improves training throughput by 1.04–4.39× compared with state-of-the-art resilient training systems under diverse failure scenarios in a 256-GPU cluster.

## 中文摘要

混合并行支撑着跨数万块 GPU 的大规模 LLM 训练。在如此规模下，单个设备上的硬件故障会导致设备间性能偏斜，削弱整体训练效率。现有容错系统忽略了数据集中的序列长度变化以及混合并行下的设备性能偏斜。由此导致：(1) 序列长度变化引起的迭代时间波动可能触发虚假的慢故障（fail-slow）检测；(2) 故障通过在混合并行中逐项自适应来缓解，带来不必要的检测开销和低效的容错训练。为此，本文提出 ResiHP，一个面向混合并行训练、支持鲁棒故障检测与细粒度自适应的容错系统。首先，我们开发了一个检测器以准确识别故障。具体而言，它采用负载感知的执行时间预测器，将故障与迭代时间波动区分开，同时保持轻量以支持在线检测。其次，我们设计了一个调度器，动态调整并行组大小、模型划分与负载调度策略，以提升故障下的训练效率。实验表明，在 256 块 GPU 集群的多种故障场景下，ResiHP 相比最先进的容错训练系统将训练吞吐提升 1.04–4.39 倍。

## 英文关键词

Resilient training, Large Language Models (LLMs), Hybrid Parallelism, Failure Handling

## 中文关键词

容错训练，大语言模型（LLM），混合并行，故障处理

---

[← 返回 Session 3 — MoE Systems & Distributed LLM Training](index.md)
