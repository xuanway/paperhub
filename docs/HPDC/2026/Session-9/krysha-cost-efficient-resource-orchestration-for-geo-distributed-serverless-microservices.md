---
title: "Krysha: Cost-Efficient Resource Orchestration for Geo-Distributed Serverless Microservices"
description: "HPDC 2026 · Session 9 — Cloud, Serverless & Microservices"
tags:
  - "HPDC2026"
  - "Session 9"
  - "Cloud, Serverless & Microservices"
---

# Krysha: Cost-Efficient Resource Orchestration for Geo-Distributed Serverless Microservices

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 9 — Cloud, Serverless & Microservices（2026年7月16日 10:20–11:20 · Session Chair：Santonu Sarkar）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 9</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807589)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#ZhangJ26](https://dblp.org/db/conf/hpdc/hpdc2026.html#ZhangJ26)

**作者**：Yuqiu Zhang, Hans-Arno Jacobsen

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 9 — Cloud, Serverless & Microservices（2026年7月16日 10:20–11:20 · Session Chair：Santonu Sarkar）

---

## 英文摘要

The convergence of microservice architectures and serverless computing promises an elastic and cost-efficient model for modern cloud applications that often span multiple geo-distributed regions. However, prevailing serverless orchestrators that prioritize resource utilization or simple cold-start mitigation often prove suboptimal concerning SLO compliance and cost-efficiency in this emerging use case. In this paper, we present Krysha, an adaptive orchestration framework that jointly optimizes function scheduling and resource allocation for geo-distributed serverless microservices. Krysha employs a novel bi-level scheduling strategy: global-level early-binding to regions for fast function dispersion, coupled with regional-level late-binding to compute nodes for optimized resource use and cost. Moreover, Krysha achieves fine-grained resource allocation by decoupling CPU and memory provisioning and applying in-place vertical scaling on individual function instances. These capabilities are guided by a comprehensive cost model and practical online optimization techniques. Our extensive evaluation shows that Krysha can achieve up to 74.7% cost savings in scaled deployments compared to state-of-the-art alternatives while maintaining SLO requirements.

## 中文摘要

微服务架构与无服务器计算的融合，为常常横跨多个地理分布区域的现代云应用带来了弹性且高性价比的模型。然而，在此新兴用例中，优先考虑资源利用率或仅简单缓解冷启动的主流无服务器编排器，在 SLO 合规性与成本效率方面往往表现欠佳。本文提出 Krysha，一个自适应编排框架，联合优化地理分布式无服务器微服务的函数调度与资源分配。Krysha 采用新颖的双层调度策略：全局层面向区域进行早绑定（early-binding）以实现函数的快速分散，区域层面向计算节点进行晚绑定（late-binding）以优化资源使用与成本。此外，Krysha 通过解耦 CPU 与内存供给并对单个函数实例应用原地垂直伸缩，实现细粒度资源分配。这些能力由全面的成本模型与实用的在线优化技术指导。我们的大量评估表明，与最先进的替代方案相比，Krysha 在规模化部署中可节省高达 74.7% 的成本，同时满足 SLO 要求。

## 英文关键词

Cloud Resource Management, Serverless Computing

## 中文关键词

云资源管理，无服务器计算

---

[← 返回 Session 9 — Cloud, Serverless & Microservices](index.md)
