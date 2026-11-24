---
title: "TUNA: Tuning Unstable and Noisy Cloud Applications"
description: "EuroSys 2025 · Cloud and Serverless Computing · Johannes Freischuetz (University of Wisconsin - Madison), Konstantinos Kanellis "
tags:
  - "EuroSys2025"
  - "Cloud and Serverless Computing"
---

# TUNA: Tuning Unstable and Noisy Cloud Applications

**中文标题：** 调优不稳定且有噪声的云应用

**所属 Session：** [Session 7.1: Cloud and Serverless Computing](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Cloud and Serverless Computing。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Cloud and Serverless Computing</p>
</div>

**作者**：Johannes Freischuetz (University of Wisconsin - Madison), Konstantinos Kanellis (University of Wisconsin-Madison), Brian Kroth (Microsoft), Shivaram Venkataraman (University of Wisconsin-Madison)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717480)

## 英文摘要

Autotuning plays a pivotal role in optimizing the performance of systems, particularly in large-scale cloud deployments. One of the main challenges in performing autotuning in the cloud arises from performance variability. We first investigate the extent to which noise slows autotuning and find that as little as 5% noise can lead to a 2.5x slowdown in converging to the best-performing configuration. We measure the magnitude of noise in cloud computing settings and find that while some components (CPU, disk) have almost no performance variability, there are still sources of significant variability (caches, memory). Furthermore, variability leads to autotuning finding unstable configurations. As many as 63.3% of the configurations selected as "best" during tuning can have their performance degrade by 30% or more when deployed. Using this as motivation, we propose a novel approach to improve the efficiency of autotuning systems by (a) detecting and removing outlier configurations and (b) using ML-based approaches to provide a more stable true signal of de-noised experiment results to the optimizer. The resulting system, TUNA (Tuning Unstable and Noisy Cloud Applications) enables faster convergence and robust configurations. Tuning PostgreSQL running mssales, an enterprise production workload, we find that TUNA can lead to 1.88x lower running time on average with 2.58𝑥lower standard deviation compared to traditional sampling methodologies.

## 中文摘要

自动调优在优化系统性能方面起着关键作用，在大规模云部署中尤为如此。在云中执行自动调优的主要挑战之一来自性能波动。我们首先研究了噪声在多大程度上拖慢自动调优，发现低至 5% 的噪声就可使收敛到最佳性能配置的速度慢 2.5 倍。我们测量了云计算环境中的噪声幅度，发现尽管某些组件（CPU、磁盘）几乎没有性能波动，但仍存在波动显著的来源（缓存、内存）。此外，波动会导致自动调优找到不稳定的配置。在调优过程中被选为“最佳”的配置中，多达 63.3% 在部署后性能可能下降 30% 或更多。以此为动机，我们提出一种新方法提升自动调优系统的效率：（a）检测并剔除离群配置；（b）使用基于机器学习的方法，为优化器提供更稳定的、去噪后的实验结果真实信号。由此得到的系统 TUNA（Tuning Unstable and Noisy Cloud Applications）实现了更快的收敛和更稳健的配置。在调优运行企业生产负载 mssales 的 PostgreSQL 时，我们发现相比传统采样方法，TUNA 平均运行时间降低 1.88 倍，标准差降低 2.58 倍。

**英文关键词：** Bayesian Optimization, Autotuning, Performance Tuning, Noise Reduction, Performance Variability

**中文关键词：** 贝叶斯优化、自动调优、性能调优、降噪、性能波动

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
