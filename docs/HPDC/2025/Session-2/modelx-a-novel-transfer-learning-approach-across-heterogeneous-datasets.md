---
title: "ModelX: A Novel Transfer Learning Approach Across Heterogeneous Datasets"
description: "HPDC 2025 · Session 2 — Model Training"
tags:
  - "HPDC2025"
  - "Session 2"
  - "Model Training"
---

# ModelX: A Novel Transfer Learning Approach Across Heterogeneous Datasets

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2025 主会 Session 2 — Model Training（2025年7月21日 13:15–15:00 · Session Chair：Ali Jannesari）。</p>
<p class="paper-seo-summary__tags">HPDC 2025 · Session 2</p>
</div>

**官方资料**：[HPDC 2025 官方议程](https://hpdc.sci.utah.edu/2025/program.html) · [ACM DOI](https://doi.org/10.1145/3731545.3731593) · [Slides](https://hpdc.sci.utah.edu/2025/assets/slides/main_session/dey.pdf)

**作者**：Arunavo Dey, Neil Antony, Aakash Raj Dhakal, Tapasya Patki, Aniruddha Marathe, Jae Seung Yeom, Tanzima Islam

**会议**：HPDC 2025 · Notre Dame, IN, USA

**Session**：Session 2 — Model Training（2025年7月21日 13:15–15:00 · Session Chair：Ali Jannesari）

---

## 英文摘要

Leveraging an existing performance model to predict the runtime of a new application on a new system can save days and weeks of data collection time. However, knowledge transfer between High Performance Computing (HPC) systems can be challenging due to data heterogeneity caused by differences in data collection methods, architectural or application-specific individuality. This results in (1) sets of performance features that have significantly different names, orders, or the number of performance features that do not match between two datasets (heterogeneous domains), or (2) distribution shifts between datasets although their feature names match (homogeneous domains). While existing transfer learning techniques can handle mild distribution shifts, they fail to transfer knowledge when the source and target features do not match. This work introduces a novel transfer learning methodology–Cross Prediction Model (ModelX), which overcomes the large distribution discrepancy between homogeneous domains and enables transfer learning between heterogeneous domains. Extensive evaluations show that ModelX outperforms traditional transfer learning methods for all experiments using 11 HPC and 4 Machine Learning (ML) datasets. To the best of our knowledge, this is the first methodology to enable knowledge transfer between two heterogeneous domains with no matching features. Finally, we demonstrate an application of ModelX to an HPC job scheduling scenario using real-world job traces where it helps to reduce the job turnaround time of a set of jobs by 71%.

## 中文摘要

利用已有的性能模型来预测新应用在新系统上的运行时间，可节省数天乃至数周的数据收集时间。然而，由于数据收集方法、架构或应用个性差异所导致的数据异质性，高性能计算（HPC）系统之间的知识迁移可能颇具挑战。这会造成：(1) 两个数据集之间的性能特征集合名称、顺序或数量显著不同、互不匹配（异构域）；或 (2) 尽管特征名称匹配，数据集之间仍存在分布偏移（同构域）。现有迁移学习技术能处理轻微的分布偏移，但当源域与目标域特征不匹配时便无法迁移知识。本工作提出一种新颖的迁移学习方法——交叉预测模型（ModelX），它克服了同构域之间的大幅分布差异，并支持异构域之间的迁移学习。大量评估表明，在使用 11 个 HPC 和 4 个机器学习（ML）数据集的所有实验中，ModelX 均优于传统迁移学习方法。据我们所知，这是首个能够在两个无匹配特征的异构域之间实现知识迁移的方法。最后，我们展示了 ModelX 在 HPC 作业调度场景中的应用：在真实作业轨迹上，它帮助将一组作业的周转时间缩短了 71%。

## 英文关键词

Transfer learning, Heterogeneous domains, Predictive performance, Intelligent scheduling

## 中文关键词

迁移学习，异构域，预测性能，智能调度

---

[← 返回 Session 2 — Model Training](index.md)
