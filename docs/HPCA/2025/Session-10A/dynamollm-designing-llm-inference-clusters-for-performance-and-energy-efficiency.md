---
title: "DynamoLLM: Designing LLM Inference Clusters for Performance and Energy Efficiency"
description: "HPCA 2025 · The Winning System"
tags:
  - "HPCA2025"
  - "The Winning System"
---

# DynamoLLM: Designing LLM Inference Clusters for Performance and Energy Efficiency

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: The Winning System。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · The Winning System</p>
</div>

**论文链接**：
**作者**：Jovan Stojkovic (University of Illinois at Urbana-Champaign), Chaojie Zhang (Microsoft), Íñigo Goiri (Microsoft), Josep Torrellas (UIUC), Esha Choukse (Microsoft)
**会议**：HPCA 2025

---

## 中文标题

DynamoLLM：面向性能与能效的 LLM 推理集群设计

## 英文摘要

The rapid evolution and widespread adoption of generative large language models (LLMs) have made them a pivotal workload in various applications. Today, LLM inference clusters receive a large number of queries with strict Service Level Objectives (SLOs). To achieve the desired performance, these models execute on power-hungry GPUs, causing inference clusters to consume large amounts of energy and, consequently, result in substantial carbon emissions. Fortunately, we find that there is an opportunity to improve energy efficiency by exploiting the heterogeneity in inference compute properties and the fluctuations in inference workloads. However, the diversity and dynamicity of these environments create a large search space, where different system configurations (e.g., number of instances, model parallelism, and GPU frequency) translate into different energy-performance trade-offs. To address these challenges, we propose DynamoLLM, the first energy-management framework for LLM inference environments. DynamoLLM automatically and dynamically reconfigures the inference cluster to optimize for energy of LLM serving under the services’ performance SLOs. We show that at a service level, on average, DynamoLLM conserves 52% of the energy and 38% of the operational carbon emissions, and reduces the cost to the customer by 61%, while meeting the latency SLOs.

## 中文摘要

生成式大语言模型（LLM）的快速演进与广泛采用，使其成为各类应用中的关键负载。如今 LLM 推理集群收到大量带有严格服务等级目标（SLO）的查询。为达到期望性能，这些模型在功耗很高的 GPU 上执行，使推理集群消耗大量电能，进而产生可观的碳排放。幸运的是，我们发现存在提升能效的机会，即利用推理计算特性的异构性以及推理负载的波动。然而这些环境的多样性与动态性造成了巨大的搜索空间，不同的系统配置（如实例数量、模型并行方式和 GPU 频率）会带来不同的能效与性能折衷。为应对这些挑战，我们提出 DynamoLLM，首个面向 LLM 推理环境的能量管理框架。DynamoLLM 自动且动态地重配置推理集群，以在满足服务性能 SLO 的前提下优化 LLM 服务的能耗。我们表明，在服务层面 DynamoLLM 平均节省 52% 的能耗和 38% 的运营碳排放，并在满足时延 SLO 的同时将用户成本降低 61%。
