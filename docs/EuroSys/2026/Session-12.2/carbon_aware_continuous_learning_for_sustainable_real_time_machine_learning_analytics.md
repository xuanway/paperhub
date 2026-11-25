---
title: "Carbon-Aware Continuous Learning for Sustainable Real-Time Machine Learning Analytics"
description: "EuroSys 2026 · Edge Computing, IoT & Embedded AI · Gwanjong Park (Sungkyunkwan University), Osama Khan (Sungkyunkwan University), D"
tags:
  - "EuroSys2026"
  - "Edge Computing, IoT & Embedded AI"
---

# Carbon-Aware Continuous Learning for Sustainable Real-Time Machine Learning Analytics

**中文标题：** 面向可持续实时机器学习分析的碳感知持续学习

**所属 Session：** [Session 12.2: Edge Computing, IoT & Embedded AI](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Edge Computing, IoT & Embedded AI。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Edge Computing, IoT & Embedded AI</p>
</div>

**作者**：Gwanjong Park (Sungkyunkwan University), Osama Khan (Sungkyunkwan University), Dongho Ha (Unaffiliated), Myeongjae Jeon (POSTECH), Euiseong Seo (Sungkyunkwan University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769361)

## 英文摘要

Real-time machine learning (ML) analytics models deployed on edge servers often experience degraded inference accuracy due to data drift. Continuous learning mitigates this by periodically retraining models using newly collected data. However, retraining incurs significant computational overhead, increasing energy consumption and carbon footprint several-fold. Existing approaches for reducing carbon footprint predominantly focus on general workload scheduling strategies, such as shifting jobs to periods or regions with lower carbon intensity. However, they neglect continuous-learning-specific parameters like data labeling model, retraining threshold, and retraining hyperparameters. Consequently, these approaches miss opportunities to further reduce the carbon footprint and enhance inference accuracy in continuous learning systems under dynamic data drift. In this paper, we propose a novel Carbon-footprint-aware Continuous Learning (CCL) scheme that minimizes carbon emissions during model retraining without sacrificing inference accuracy. Distinct from prior workload scheduling approaches, CCL adaptively adjusts labeling model, retraining threshold, and retraining hyperparameters based on predictive models that estimate data drift severity and carbon intensity dynamics. Our adaptive real-time optimization approach consistently achieves a near-optimal balance between accuracy and carbon footprint under dynamic conditions. Experimental results demonstrate that CCL reduces operational carbon footprint by up to 68.5% compared to state-of-the-art carbon-agnostic methods, with negligible accuracy degradation.

## 中文摘要

部署在边缘服务器上的实时机器学习（ML）分析模型常因数据漂移而出现推理精度下降。持续学习通过定期使用新采集的数据重新训练模型来缓解这一问题。然而，重新训练会带来显著的计算开销，使能耗和碳足迹增加数倍。现有减少碳足迹的方法主要关注通用工作负载调度策略，例如将作业转移到碳强度较低的时段或区域。然而，它们忽视了持续学习特有的参数，如数据标注模型、重训练阈值和重训练超参数。因此，在动态数据漂移下，这些方法错失了进一步降低持续学习系统碳足迹并提升推理精度的机会。本文提出一种新颖的碳足迹感知持续学习（CCL）方案，在不牺牲推理精度的前提下最小化模型重训练过程中的碳排放。与先前的工作负载调度方法不同，CCL 基于估计数据漂移严重程度和碳强度动态的预测模型，自适应地调整标注模型、重训练阈值和重训练超参数。我们的自适应实时优化方法在动态条件下始终实现精度与碳足迹之间的近似最优平衡。实验结果表明，与先进的碳无感知方法相比，CCL 将运营碳足迹最多降低 68.5%，而精度下降可忽略。

**英文关键词：** continuous learning, sustainability, energy-efficiency, real-time data analytics, reinforcement learning

**中文关键词：** 持续学习、可持续性、能效、实时数据分析、强化学习

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
