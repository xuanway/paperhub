---
title: "FlexPipe: Adapting Dynamic LLM Serving Through Inflight Pipeline Refactoring in Fragmented Serverless Clusters"
description: "EuroSys 2026 · LLM Inference · Yanying Lin (UCAS, UCSD), Shijie Peng (Shenzhen Institute of Advanced Technology"
tags:
  - "EuroSys2026"
  - "LLM Inference"
---

# FlexPipe: Adapting Dynamic LLM Serving Through Inflight Pipeline Refactoring in Fragmented Serverless Clusters

**中文标题：** FlexPipe：在碎片化无服务器集群中通过运行时流水线重构适配动态 LLM 服务

**所属 Session：** [Session 7.1: LLM Inference](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：LLM Inference。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · LLM Inference</p>
</div>

**作者**：Yanying Lin (UCAS, UCSD), Shijie Peng (Shenzhen Institute of Advanced Technology, Chinese Academy of Sciences), Chengzhi Lu (University of Macau), ChengZhong Xu (University of Macau), Kejiang Ye (Shenzhen Institutes of Advanced Technology, Chinese Academy of Sciences)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769316)

## 英文摘要

Serving Large Language Models (LLMs) in production faces significant challenges from highly variable request patterns and severe resource fragmentation in serverless clusters. Current systems rely on static pipeline configurations that struggle to adapt to dynamic workload conditions, leading to substantial inefficiencies.

We present FlexPipe, a novel system that dynamically reconfigures pipeline architectures during runtime to address these fundamental limitations. FlexPipe decomposes models into fine-grained stages and intelligently adjusts pipeline granularity based on real-time request pattern analysis, implementing three key innovations: fine-grained model partitioning with preserved computational graph constraints, inflight pipeline refactoring with consistent cache transitions, and topology-aware resource allocation that navigates GPU fragmentation. Comprehensive evaluation on an 82-GPU cluster demonstrates that FlexPipe achieves up to 8.5× better resource efficiency while maintaining 38.3% lower latency compared to state-of-the-art systems, reducing GPU reservation requirements from 75% to 30% of peak capacity.

## 中文摘要

在生产环境中服务大语言模型（LLM）面临重大挑战，一方面请求模式高度多变，另一方面无服务器集群中存在严重的资源碎片化。现有系统依赖静态流水线配置，难以适应动态的负载状况，造成显著的效率损失。

我们提出 FlexPipe，一个新系统，它在运行时动态重构流水线架构，以解决上述根本性局限。FlexPipe 将模型分解为细粒度阶段，并基于实时请求模式分析智能调整流水线粒度，实现了三项关键创新：在保持计算图约束的前提下进行细粒度模型划分、带有一致缓存迁移的运行时流水线重构，以及可绕开 GPU 碎片化的拓扑感知资源分配。在 82 块 GPU 集群上的全面评估表明，与最先进系统相比，FlexPipe 的资源效率最高提升 8.5 倍，同时延迟降低 38.3%，并将 GPU 预留需求从峰值容量的 75% 降至 30%。

**英文关键词：** Large Language Models, Serverless Computing, Resource Efficiency, Pipeline Parallelism, Dynamic Scaling

**中文关键词：** 大语言模型、无服务器计算、资源效率、流水线并行、动态伸缩

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
