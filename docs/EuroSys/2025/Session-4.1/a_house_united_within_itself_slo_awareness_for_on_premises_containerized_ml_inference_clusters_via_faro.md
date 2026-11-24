---
title: "A House United Within Itself: SLO-Awareness for On-Premises Containerized ML Inference Clusters via Faro"
description: "EuroSys 2025 · ML Systems · Beomyeol Jeon (University of Illinois Urbana-Champaign), Chen Wang (IBM Research"
tags:
  - "EuroSys2025"
  - "ML Systems"
---

# A House United Within Itself: SLO-Awareness for On-Premises Containerized ML Inference Clusters via Faro

**中文标题：** 同心协力：利用 Faro 为本地容器化机器学习推理集群提供 SLO 感知

**所属 Session：** [Session 4.1: ML Systems](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：ML Systems。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · ML Systems</p>
</div>

**作者**：Beomyeol Jeon (University of Illinois Urbana-Champaign), Chen Wang (IBM Research), Diana Arroyo (IBM Research), Alaa Youssef (IBM Research), Indranil Gupta (University of Illinois Urbana-Champaign)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696071)

## 英文摘要

This paper tackles the challenge of running multiple ML inference jobs (models) under time-varying workloads, on a constrained on-premises production cluster. Our system Faro takes in latency Service Level Objectives (SLOs) for each job, auto-distills them into utility functions, “sloppifies” these utility functions to make them amenable to mathematical optimization, automatically predicts workload via probabilistic prediction, and dynamically makes implicit cross-job resource allocations, in order to satisfy cluster-wide objectives, e.g., total utility, fairness, and other hybrid variants. A major challenge Faro tackles is that using precise utilities and high-fidelity predictors, can be too slow (and in a sense too precise!) for the fast adaptation we require. Faro’s solution is to “sloppify” (relax) its multiple design components to achieve fast adaptation without overly degrading solution quality. Faro is implemented in a stack consisting of Ray Serve running atop a Kubernetes cluster. Trace-driven cluster deployments show that Faro achieves 2.3×–23× lower SLO violations compared to state-of-the-art systems.

## 中文摘要

本文解决在资源受限的本地部署生产集群上、于时变工作负载下运行多个机器学习推理作业（模型）的挑战。我们的系统 Faro 接收每个作业的延迟服务等级目标（SLO），将其自动蒸馏为效用函数，对这些效用函数进行“松弛化”处理以使其适合数学优化，通过概率预测自动预测工作负载，并动态进行隐式的跨作业资源分配，以满足集群级目标，例如总效用、公平性及其他混合变体。Faro 应对的一个主要挑战是：使用精确的效用函数和高保真预测器，对于我们所需的快速自适应而言可能太慢（某种意义上也过于精确！）。Faro 的解决方案是“松弛化”（放宽）其多个设计组件，以实现快速自适应而不过度降低求解质量。Faro 实现在由运行于 Kubernetes 集群之上的 Ray Serve 构成的软件栈中。基于轨迹的集群部署表明，与最先进的系统相比，Faro 将 SLO 违例降低 2.3 倍至 23 倍。

**英文关键词：** Machine Learning, Inference, Resource constraints, Autoscaling, Multi-tenancy

**中文关键词：** 机器学习、推理、资源约束、自动扩缩容、多租户

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
