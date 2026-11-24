---
title: "NeuStream: Bridging Deep Learning Serving and Stream Processing"
description: "EuroSys 2025 · Graph and Stream processing · Haochen Yuan (Peking University), Yuanqing Wang (Peking University and Microsoft"
tags:
  - "EuroSys2025"
  - "Graph and Stream processing"
---

# NeuStream: Bridging Deep Learning Serving and Stream Processing

**中文标题：** 连接深度学习服务与流处理

**所属 Session：** [Session 5.1: Graph and Stream processing](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Graph and Stream processing。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Graph and Stream processing</p>
</div>

**作者**：Haochen Yuan (Peking University), Yuanqing Wang (Peking University and Microsoft Research), Wenhao Xie (Peking University), Yu Cheng (Peking University and Microsoft Research), Ziming Miao (Microsoft Research), Lingxiao Ma (Microsoft Research), Jilong Xue (Microsoft Research), Zhi Yang (Peking University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717489)

## 英文摘要

Modern Deep Neural Network (DNN) exhibits a pattern where multiple sub-models are executed, guided by control flows such as loops and switch/merge operations. This dynamic nature introduces complexities in batching the requests of such DNNs for efficient execution on GPUs. In this paper, we present NeuStream, a programming model and runtime system for serving deep learning workloads using stream processing. NeuStream decomposes the inference workflow into modules and forms them into a streaming processing system where a request flows through. Based on such abstraction, NeuStream is able to batch requests at fine-grained module granularity. To maximize serving goodput, NeuStream exploits a two-level scheduling approach to decide the best batching requests and resource allocation for each module while satisfying service level objectives (SLOs). Our evaluation of NeuStream on a set of modern DNNs like Large Language Models (LLM) and diffusion models, etc., shows that NeuStream significantly improves goodput compared to state-of-the-art DNN serving systems.

## 中文摘要

现代深度神经网络（DNN）呈现出由循环、switch/merge 等控制流引导、执行多个子模型的模式。这种动态特性为对此类 DNN 的请求进行批处理以在 GPU 上高效执行带来了复杂性。本文提出 NeuStream，一个使用流处理来服务深度学习工作负载的编程模型与运行时系统。NeuStream 将推理工作流分解为模块，并将其组织为请求在其中流动的流处理系统。基于这种抽象，NeuStream 能够在细粒度的模块级别对请求进行批处理。为最大化服务有效吞吐（goodput），NeuStream 采用两级调度方法，在满足服务等级目标（SLO）的同时为每个模块决定最佳的请求批处理与资源分配。我们在大型语言模型（LLM）、扩散模型等一系列现代 DNN 上对 NeuStream 的评估表明，与最先进的 DNN 服务系统相比，NeuStream 显著提升了有效吞吐。

**英文关键词：** Deep Learning Serving, dynamic Neural Networks, Streaming Processing System

**中文关键词：** 深度学习服务、动态神经网络、流处理系统

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
