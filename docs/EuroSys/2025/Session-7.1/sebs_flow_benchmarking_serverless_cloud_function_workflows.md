---
title: "SeBS-Flow: Benchmarking Serverless Cloud Function Workflows"
description: "EuroSys 2025 · Cloud and Serverless Computing · Larissa Schmid (Karlsruhe Institute of Technology), Marcin Copik (ETH Zurich), A"
tags:
  - "EuroSys2025"
  - "Cloud and Serverless Computing"
---

# SeBS-Flow: Benchmarking Serverless Cloud Function Workflows

**中文标题：** 无服务器云函数工作流基准测试

**所属 Session：** [Session 7.1: Cloud and Serverless Computing](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Cloud and Serverless Computing。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Cloud and Serverless Computing</p>
</div>

**作者**：Larissa Schmid (Karlsruhe Institute of Technology), Marcin Copik (ETH Zurich), Alexandru Calotoiu (ETH Zurich), Laurin Brandner (ETH Zurich), Anne Koziolek (Karlsruhe Institute of Technology), Torsten Hoefler (ETH Zurich)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717465)

## 英文摘要

Serverless computing has emerged as a prominent paradigm, with a significant adoption rate among cloud customers. While this model offers advantages such as abstraction from the deployment and resource scheduling, it also poses limitations in handling complex use cases due to the restricted nature of individual functions. Serverless workflows address this limitation by orchestrating multiple functions into a cohesive application. However, existing serverless workflow platforms exhibit significant differences in their programming models and infrastructure, making fair and consistent performance evaluations difficult in practice. To address this gap, we propose the first serverless workflow benchmarking suite SeBS-Flow, providing a platform-agnostic workflow model that enables consistent benchmarking across various platforms. SeBS-Flow includes six real-world application benchmarks and four microbenchmarks representing different computational patterns. We conduct comprehensive evaluations on three major cloud platforms, assessing performance, cost, scalability, and runtime deviations. We make our benchmark suite open-source, enabling rigorous and comparable evaluations of serverless workflows over time. Implementation: https://github.com/spcl/serverless-benchmarks Artifact: https://github.com/spcl/sebs-flow-artifact

## 中文摘要

无服务器计算已成为一种突出的范式，在云客户中具有显著的采用率。虽然该模型提供了诸如从部署和资源调度中抽象出来等优势，但由于单个函数的受限特性，它在处理复杂用例时也存在局限。无服务器工作流通过将多个函数编排为内聚的应用来应对这一局限。然而，现有无服务器工作流平台在编程模型和基础设施上存在显著差异，使得在实践中进行公平且一致的性能评估变得困难。为填补这一空白，我们提出首个无服务器工作流基准测试套件 SeBS-Flow，它提供平台无关的工作流模型，从而能够在不同平台上进行一致的基准测试。SeBS-Flow 包含六个真实应用基准和四个代表不同计算模式的微基准。我们在三个主要云平台上进行了全面评估，考察性能、成本、可扩展性和运行时偏差。我们将基准套件开源，以便对无服务器工作流进行严格且可随时间比较的评估。实现：https://github.com/spcl/serverless-benchmarks 制品：https://github.com/spcl/sebs-flow-artifact

**英文关键词：** benchmark, serverless, function-as-a-service, faas, workflow, orchestration, serverless DAG

**中文关键词：** 基准测试、无服务器、函数即服务、FaaS、工作流、编排、无服务器 DAG

## 代码与研究制品

- 代码：[https://github.com/spcl/serverless-benchmarks](https://github.com/spcl/serverless-benchmarks)
- 制品：[https://github.com/spcl/sebs-flow-artifact](https://github.com/spcl/sebs-flow-artifact)

以上链接来自论文现有摘要中的公开资料。

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
