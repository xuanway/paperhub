---
title: "Loki: A System for Serving ML Inference Pipelines with Hardware and Accuracy Scaling"
description: "HPDC 2024 · Session 7 — Resource Management"
tags:
  - "HPDC2024"
  - "Session 7"
  - "Resource Management"
---

# Loki: A System for Serving ML Inference Pipelines with Hardware and Accuracy Scaling

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2024 主会 Session 7 — Resource Management（2024年6月7日 11:45–13:00 · Session Chair：Kento Sato）。</p>
<p class="paper-seo-summary__tags">HPDC 2024 · Session 7</p>
</div>

**官方资料**：[HPDC 2024 官方议程](https://hpdc.sci.utah.edu/2024/program.html) · [ACM DOI](https://doi.org/10.1145/3625549.3658688)

**作者**：Sohaib Ahmad, Hui Guan, Ramesh K. Sitaraman

**会议**：HPDC 2024 · Pisa, Italy

**Session**：Session 7 — Resource Management（2024年6月7日 11:45–13:00 · Session Chair：Kento Sato）

---

## 英文摘要

The rapid adoption of machine learning (ML) has underscored the importance of serving ML models with high throughput and resource efficiency. Traditional approaches to managing increasing query demands have predominantly focused on hardware scaling, which involves increasing server count or computing power. However, this strategy can often be impractical due to limitations in the available budget or compute resources. As an alternative, accuracy scaling offers a promising solution by adjusting the accuracy of ML models to accommodate fluctuating query demands. Yet, existing accuracy scaling techniques target independent ML models and tend to underperform while managing inference pipelines. Furthermore, they lack integration with hardware scaling, leading to potential resource inefficiencies during low-demand periods. To address the limitations, this paper introduces Loki, a system designed for serving inference pipelines effectively with both hardware and accuracy scaling. Loki incorporates an innovative theoretical framework for optimal resource allocation and an effective query routing algorithm, aimed at improving system accuracy and minimizing latency deadline violations. Our empirical evaluation demonstrates that through accuracy scaling, the effective capacity of a fixed-size cluster can be enhanced by more than 2.7× compared to relying solely on hardware scaling. When compared with state-of-the-art inference-serving systems, Loki achieves up to a 10× reduction in Service Level Objective (SLO) violations, with minimal compromises on accuracy and while fulfilling throughput demands.

## 中文摘要

机器学习的快速普及凸显了以高吞吐与高资源效率服务 ML 模型的重要性。应对查询需求增长的传统方法主要聚焦硬件扩展，即增加服务器数量或算力。然而，受预算或计算资源限制，该策略往往不切实际。作为一种替代，精度扩展通过调整 ML 模型的精度来适应波动的查询需求，提供了有前景的方案。但现有精度扩展技术针对独立的 ML 模型，在管理推理流水线时往往表现不佳。此外，它们缺乏与硬件扩展的整合，在低需求期可能导致资源低效。为克服这些局限，本文提出 Loki，一个旨在同时利用硬件与精度扩展来高效服务推理流水线的系统。Loki 包含用于最优资源分配的新颖理论框架与有效的查询路由算法，旨在提升系统精度并最小化延迟截止期违规。我们的实证评估表明，通过精度扩展，固定规模集群的有效容量相比仅依赖硬件扩展可提升 2.7 倍以上。与最先进的推理服务系统相比，Loki 将服务等级目标（SLO）违规降低最高 10 倍，对精度的损害极小，同时满足吞吐需求。

## 英文关键词

Inference Serving, Model Serving, Inference Pipelines, Machine Learning, Autoscaling

## 中文关键词

推理服务，模型服务，推理流水线，机器学习，自动伸缩

---

[← 返回 Session 7 — Resource Management](index.md)
