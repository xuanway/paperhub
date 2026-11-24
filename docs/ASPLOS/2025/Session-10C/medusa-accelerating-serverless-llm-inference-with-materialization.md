---
title: "Medusa: Accelerating Serverless LLM Inference with Materialization"
description: "ASPLOS 2025 · Session 10C · Medusa：利用物化加速 Serverless LLM 推理"
tags:
  - "ASPLOS2025"
  - "Session 10C"
  - "Serverless Computing"
---

# Medusa: Accelerating Serverless LLM Inference with Materialization

**中文标题：** Medusa：利用物化加速 Serverless LLM 推理

**所属 Session：** [Session 10C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Shaoxun Zeng (Tsinghua University), Minhui Xie (Tsinghua University), Shiwei Gao (Tsinghua University), Youmin Chen (Tsinghua University), Youyou Lu (Tsinghua University)

**单位：** Tsinghua University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707285) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Serverless is a promising paradigm to provide scalable, costefficient, and easy-to-use model inference services. However, the cold start of model inference functions requires loading models to the devices, which incurs high latencies and undermines the benefits of serverless computing. In LLMs, things get even worse since two extra stages are introduced: a KV cache initialization stage that profiles and anticipates memory reservation for KV cache, and a capturing stage which dynamically constructs CUDA graphs for different batch sizes. Both stages are paramount to the inference performance, but become the main culprit of cold start latency. This paper proposes Medusa to mitigate the long cold start latency through state materialization. Instead of dynamic profiling and construction in the runtime, Medusa materializes the CUDA graphs as well as the information needed by the KV cache initialization in the offline phase, and restores them efficiently in the online phase. Medusa further introduces two novel techniques – offline-online cooperated parameters restoration and triggering-kernels enhanced kernel address restoration – to tackle non-deterministic issues in CUDA graphs. Medusa successfully materializes and restores CUDA graphs across 10 models (with a total of 139364 CUDA graph nodes), and reduces the latency of model loading by 42.5%. Under real-world LLM inference workloads, Medusa reduces the tail latency of the time to first token (TTFT) by 53.0%.

## 中文摘要

Serverless 是一种有前景的范式，可提供可扩展、成本高效且易用的模型推理服务。然而，模型推理函数的冷启动需要将模型加载到设备上，这会带来高延迟并削弱 Serverless 计算的优势。在 LLM 中情况更糟，因为引入了两个额外阶段：KV cache 初始化阶段，它通过剖析来预测并为 KV cache 预留内存；以及捕获（capturing）阶段，它为不同的批大小动态构建 CUDA 图。这两个阶段对推理性能至关重要，却成为冷启动延迟的主要元凶。本文提出 Medusa，通过状态物化来缓解过长的冷启动延迟。Medusa 不在运行时进行动态剖析与构建，而是在离线阶段物化 CUDA 图以及 KV cache 初始化所需的信息，并在在线阶段高效地将其恢复。Medusa 进一步引入两项新技术——离线与在线协同的参数恢复，以及触发内核增强的内核地址恢复——以解决 CUDA 图中的非确定性问题。Medusa 成功地在 10 个模型（共 139364 个 CUDA 图节点）上物化并恢复 CUDA 图，并将模型加载延迟降低 42.5%。在真实世界的 LLM 推理工作负载下，Medusa 将首 token 时延（time to first token，TTFT）的尾部延迟降低 53.0%。

## 英文关键词

LLM; serverless computing; machine learning system

## 中文关键词

LLM；Serverless 计算；机器学习系统

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707285)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 10C](index.md) · [返回 ASPLOS 2025](../index.md)
