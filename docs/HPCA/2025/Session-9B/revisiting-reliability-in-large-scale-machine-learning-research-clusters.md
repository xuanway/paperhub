---
title: "Revisiting Reliability in Large-Scale Machine Learning Research Clusters"
description: "HPCA 2025 · Industry Session"
tags:
  - "HPCA2025"
  - "Industry Session"
---

# Revisiting Reliability in Large-Scale Machine Learning Research Clusters

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Industry Session。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Industry Session</p>
</div>

**论文链接**：
**作者**：Apostolos Kokolis (Meta), Michael Kuchnik (Meta), John Hoffman (Meta), Adithya Kumar (Meta), Parth Malani (Meta), Faye Ma (Meta), Zachary DeVito (Meta), Shubho Sengupta (Meta), Kalyan Saladi (Meta), Carole-Jean Wu (Meta)
**会议**：HPCA 2025

---

## 中文标题

重新审视大规模机器学习研究集群的可靠性

## 英文摘要

Reliability is a fundamental challenge in operating large-scale machine learning (ML) infrastructures, particularly as the scale of ML models and training clusters continues to grow. Despite decades of research on infrastructure failures, the impact of job failures across different scales remains unclear. This paper presents a view of managing two large, multi-tenant ML clusters, providing quantitative analysis, operational experience, and our own perspective in understanding and addressing reliability concerns at scale. Our analysis reveals that while large jobs are most vulnerable to failures, smaller jobs make up the majority of jobs in the clusters and should be incorporated into optimization objectives. We identify key workload properties, compare them across clusters, and demonstrate essential reliability requirements for pushing the boundaries of ML training at scale. We hereby introduce a taxonomy of failures and key reliability metrics, analyze 11 months of data from two state-of-the-art ML environments with 4 million jobs and over 150 million A100 GPU hours. Building on our data, we fit a failure model to project Mean Time to Failure for various GPU scales. We further propose a method to estimate a related metric, Effective Training Time Ratio, as a function of job parameters, and we use this model to gauge the efficacy of potential software mitigations at scale. Our work provides valuable insights and future research directions for improving the reliability of AI supercomputer clusters, emphasizing the need for flexible, workload-agnostic, and reliability-aware infrastructure, system software, and algorithms.

## 中文摘要

可靠性是运行大规模机器学习（ML）基础设施的基本挑战，尤其随着 ML 模型与训练集群规模持续增长。尽管针对基础设施故障已有数十年研究，但作业故障在不同规模下的影响仍不清楚。本文呈现了管理两个大型多租户 ML 集群的视角，提供定量分析、运维经验以及我们理解和应对大规模可靠性问题的观点。我们的分析表明，尽管大型作业最易受故障影响，但小型作业构成了集群中作业的大多数，应被纳入优化目标。我们识别了关键的负载属性，在两个集群间进行比较，并阐明了将大规模 ML 训练推向极限所必需的关键可靠性要求。我们据此提出了故障分类法与关键可靠性指标，分析了两个最先进 ML 环境中 11 个月的数据，涵盖 400 万个作业与超过 1.5 亿 A100 GPU 机时。基于我们的数据，我们拟合了故障模型，以预测不同 GPU 规模下的平均无故障时间。我们进一步提出一种方法，用于估计相关指标“有效训练时间比”随作业参数变化的函数，并利用该模型评估潜在软件缓解措施在大规模下的有效性。我们的工作为提升 AI 超级计算机集群的可靠性提供了有价值的洞见与未来研究方向，强调需要灵活、与负载无关且可靠性感知的基础设施、系统软件与算法。
