---
title: "Grad: Intelligent Microservice Scaling by Harnessing Resource Fungibility"
description: "HPCA 2025 · The Winning System"
tags:
  - "HPCA2025"
  - "The Winning System"
---

# Grad: Intelligent Microservice Scaling by Harnessing Resource Fungibility

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: The Winning System。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · The Winning System</p>
</div>

**论文链接**：
**作者**：Liao Chen (University of Macau, Macau SAR, China), Chenyu Lin (University of Macau, Macau SAR, China), Shutian Luo (Yale University), Huanle Xu (University of Macau, Macau SAR, China), Chengzhong Xu (University of Macau, Macau SAR, China)
**会议**：HPCA 2025

---

## 中文标题

Grad：利用资源可替代性的智能微服务伸缩

## 英文摘要

Microservice applications are commonly deployed alongside other services to enhance resource utilization. However, this practice also leads to notable resource contention. While existing studies primarily focus on scaling critical microservices responsible for performance degradation to mitigate violations of SLAs regarding end-to-end latency in highly interfered environments, they often overlook the potential advantages of scaling non-critical microservices for optimized resource efficiency. In this paper, we introduce Grad, an intelligent microservice scaling framework by harnessing resource fungibility between critical and non-critical microservices. Addressing the challenges posed by the dynamic nature of resource fungibility during scaling, Grad incorporates three key components. First, Grad employs a modular learning approach to profile individual microservice latency in relation to environmental conditions. Utilizing gradient extracts from this profile, Grad designs a scalable optimization module to dynamically select the optimal set of microservices for scaling. To rapidly mitigate SLA violations, Grad also deploys an accurate end-to-end latency predictor, serving as an simulator to obtain real-time feedback. We evaluate Grad in our cluster using real microservice benchmarks and production traces, demonstrating its ability to reduce resource usage by 49.1% and lower the probability of SLA violations by 3.7× when compared to state-of-the-art solutions.

## 中文摘要

微服务应用通常与其他服务共同部署以提升资源利用率，但这一做法也带来明显的资源竞争。现有研究主要关注对导致性能下降的关键微服务进行伸缩，以缓解高干扰环境下端到端时延的 SLA 违约，却往往忽视了伸缩非关键微服务以优化资源效率的潜在收益。本文提出 Grad，一个利用关键微服务与非关键微服务之间资源可替代性的智能微服务伸缩框架。针对伸缩过程中资源可替代性动态变化带来的挑战，Grad 包含三个关键组件。首先，Grad 采用模块化学习方法，对单个微服务的时延与环境条件之间的关系进行刻画。利用该刻画提取的梯度信息，Grad 设计了可扩展的优化模块，动态选取最优的微服务集合进行伸缩。为快速缓解 SLA 违约，Grad 还部署了精确的端到端时延预测器，作为模拟器提供实时反馈。我们在集群中使用真实微服务基准与生产 trace 评估 Grad，结果表明：与最先进的方案相比，Grad 可降低 49.1% 的资源用量，并将 SLA 违约概率降低 3.7 倍。
