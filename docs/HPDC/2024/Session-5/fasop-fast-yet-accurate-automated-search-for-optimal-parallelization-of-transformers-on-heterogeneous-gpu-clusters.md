---
title: "FASOP: Fast yet Accurate Automated Search for Optimal Parallelization of Transformers on Heterogeneous GPU Clusters"
description: "HPDC 2024 · Session 5 — Performance modeling & LLMs"
tags:
  - "HPDC2024"
  - "Session 5"
  - "Performance modeling & LLMs"
---

# FASOP: Fast yet Accurate Automated Search for Optimal Parallelization of Transformers on Heterogeneous GPU Clusters

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2024 主会 Session 5 — Performance modeling & LLMs（2024年6月6日 16:10–17:25 · Session Chair：Ignacio Laguna）。</p>
<p class="paper-seo-summary__tags">HPDC 2024 · Session 5</p>
</div>

**官方资料**：[HPDC 2024 官方议程](https://hpdc.sci.utah.edu/2024/program.html) · [ACM DOI](https://doi.org/10.1145/3625549.3658687)

**作者**：Sunyeol Hwang, Eungyeong Lee, Hongseok Oh, Youngmin Yi

**会议**：HPDC 2024 · Pisa, Italy

**Session**：Session 5 — Performance modeling & LLMs（2024年6月6日 16:10–17:25 · Session Chair：Ignacio Laguna）

---

## 英文摘要

Transformer-based large language models have recently shown remarkable performance, but their significantly large parameters require efficient training, which is commonly realized by utilizing both data- and model-parallel deep learning on a GPU cluster. To minimize the training time, the optimal degrees of data and model parallelisms and the optimal model partitioning should be searched. When heterogeneous GPU clusters are used to utilize as many GPUs as possible, it becomes more challenging. In this work, we propose a framework named FASOP that automatically and rapidly finds the (near-)optimal degrees of parallelisms and model partitioning of Transformer-based models on heterogeneous GPU clusters, with an accurate estimation of pipelining latency and communications. Moreover, it can search for optimal cluster configurations that minimize the training time while satisfying the cost of GPU clusters. The proposed model partitioning algorithm in FASOP is three orders of magnitude faster than Dynamic Programming in the state-of-the-art for GPT-2 1.5B on a mixed set of 32 GPUs with A100 and A10, leading to a few seconds instead of several hours. And, FASOP shows only 8.7% mean absolute error in training time estimation for GPT-2 1.5B. With a fast yet accurate search, FASOP achieved up to 1.37× speedup compared to Megatron-LM.

## 中文摘要

基于 Transformer 的大语言模型近来展现出卓越性能，但其参数量极大，需要高效训练，通常通过 GPU 集群上的数据并行与模型并行深度学习来实现。为最小化训练时间，需要搜索数据并行与模型并行的最优并行度以及最优模型划分。当使用异构 GPU 集群以尽可能利用更多 GPU 时，这一问题更具挑战。本工作提出名为 FASOP 的框架，可在异构 GPU 集群上自动、快速地找到基于 Transformer 模型的（近）最优并行度与模型划分，并准确估计流水线延迟与通信。此外，它还能搜索在满足 GPU 集群成本约束下最小化训练时间的最优集群配置。FASOP 提出的模型划分算法在由 A100 与 A10 混合组成的 32 块 GPU 上，对 GPT-2 1.5B 比最先进的动态规划快三个数量级，从数小时缩短到数秒。并且，FASOP 对 GPT-2 1.5B 的训练时间估计平均绝对误差仅为 8.7%。凭借快速而准确的搜索，FASOP 相比 Megatron-LM 取得最高 1.37 倍加速。

## 英文关键词

Heterogeneous cluster, Distributed deep learning, Parallelization strategy, Large language model

## 中文关键词

异构集群，分布式深度学习，并行化策略，大语言模型

---

[← 返回 Session 5 — Performance modeling & LLMs](index.md)
