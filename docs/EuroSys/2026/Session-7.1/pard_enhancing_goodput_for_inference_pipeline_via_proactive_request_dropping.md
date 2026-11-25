---
title: "PARD: Enhancing Goodput for Inference Pipeline via Proactive Request Dropping"
description: "EuroSys 2026 · LLM Inference · Zhixin Zhao (Tianjin University), Yitao Hu (Tianjin University), Simin Chen (Uni"
tags:
  - "EuroSys2026"
  - "LLM Inference"
---

# PARD: Enhancing Goodput for Inference Pipeline via Proactive Request Dropping

**中文标题：** PARD：通过主动丢弃请求提升推理流水线的有效吞吐

**所属 Session：** [Session 7.1: LLM Inference](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：LLM Inference。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · LLM Inference</p>
</div>

**作者**：Zhixin Zhao (Tianjin University), Yitao Hu (Tianjin University), Simin Chen (University of Texas at Dallas), Mingfang Ji (Tianjin University), Wei Yang (University of Texas at Dallas), Yuhao Zhang (Tianjin University), Laiping Zhao (Tianjin University), Wenxin Li (Tianjin University), Xiulong Liu (Tianjin University), Wenyu Qu (Tianjin University), Hao Wang (Stevens Institue of Technology)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803581)

## 英文摘要

Modern deep neural network (DNN) and large language model (LLM) applications integrate multiple models into inference pipelines with stringent latency requirements for customized tasks. To mitigate extensive request timeouts caused by accumulation, systems for inference pipelines commonly drop a subset of requests so the remaining ones can satisfy latency constraints. Since it is commonly believed that request dropping adversely affects goodput, existing systems only drop requests when they have to, which we call reactive dropping. However, this reactive policy can not maintain high goodput, as it neither makes timely dropping decisions nor identifies the proper set of requests to drop, leading to issues of dropping requests too late or dropping the wrong set of requests.

We propose that the inference system should proactively drop certain requests in advance to enhance the goodput across the entire workload. To achieve this, we design an inference system PARD. It enhances goodput with timely and precise dropping decisions by integrating a proactive dropping method that decides when to drop requests using runtime information of the inference pipeline, and an adaptive request priority mechanism that selects which specific requests to drop based on remaining latency budgets and workload intensity. Evaluation on a cluster of 64 GPUs over real-world workloads shows that PARD achieves 16%–176% higher goodput than the state of the art while reducing the drop rate and wasted computation resources by 1.6×–17× and 1.5×–62× respectively.

## 中文摘要

现代深度神经网络（DNN）和大语言模型（LLM）应用将多个模型集成到推理流水线中，以满足定制任务的严格时延要求。为缓解请求积压导致的大量请求超时，推理流水线系统通常丢弃一部分请求，以使剩余请求能够满足时延约束。由于人们普遍认为丢弃请求会损害有效吞吐，现有系统只在不得不丢弃时才丢弃请求，我们称之为被动丢弃。然而，这种被动策略无法维持高有效吞吐，因为它既不能及时做出丢弃决策，也不能识别出应当丢弃的合适请求集，从而导致丢弃过晚或丢弃了错误的请求集。

我们提出，推理系统应主动提前丢弃某些请求，以提升整个工作负载的有效吞吐。为此，我们设计了推理系统 PARD。它通过集成一种主动丢弃方法和一种自适应请求优先级机制来提升有效吞吐，前者利用推理流水线的运行时信息决定何时丢弃请求，后者根据剩余时延预算和工作负载强度选择具体丢弃哪些请求，从而以及时而精确的丢弃决策提升有效吞吐。在由 64 块 GPU 组成的集群上针对真实工作负载的评估表明，PARD 的有效吞吐比现有先进工作高 16%–176%，同时将丢弃率和浪费的计算资源分别降低 1.6–17 倍和 1.5–62 倍。

**英文关键词：** Machine learning systems; Inference serving; Request scheduling; Overload control

**中文关键词：** 机器学习系统、推理服务、请求调度、过载控制

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
