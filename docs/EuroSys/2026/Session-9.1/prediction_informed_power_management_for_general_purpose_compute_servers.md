---
title: "Prediction-Informed Power Management for General-Purpose Compute Servers"
description: "EuroSys 2026 · Cloud · Jonggyu Park (University of Washington), Simon Peter (University of Washington),"
tags:
  - "EuroSys2026"
  - "Cloud"
---

# Prediction-Informed Power Management for General-Purpose Compute Servers

**中文标题：** 面向通用计算服务器的预测驱动功耗管理

**所属 Session：** [Session 9.1: Cloud](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Cloud。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Cloud</p>
</div>

**作者**：Jonggyu Park (University of Washington), Simon Peter (University of Washington), Thomas E. Anderson (University of Washington)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803617)

## 英文摘要

This paper presents PIP (Prediction-Informed Power), a power control framework for general-purpose compute servers. PIP introduces two key innovations: (1) a machine learning-based power model that predicts the impact of hypothetical CPU throttling actions before execution, and (2) a prediction-informed control loop that selects CPU configurations to maximize performance and power utilization based on these predictions. By leveraging fine-grained runtime CPU metrics, PIP can accurately estimate counterfactual power usage, allowing the control system to align power demand with the budget more quickly. Unlike traditional reactive approaches, PIP maintains effective control under frequent budget fluctuations, achieving safe oversubscription by up to 70%. Our evaluation on diverse application workloads, none of which are included in the model’s training set, shows that PIP yields up to a 3.2× speedup over a state-of-the-art feedback-based system for single-application runs, and up to a 3.4× speedup for multi-application scenarios under power constraints.

## 中文摘要

本文提出 PIP（Prediction-Informed Power），一个面向通用计算服务器的功耗控制框架。PIP 引入两项关键创新：（1）一个基于机器学习的功耗模型，在执行前预测假设的 CPU 降频动作所产生的影响；（2）一个预测驱动的控制环路，基于这些预测选择 CPU 配置以最大化性能和功耗利用率。通过利用细粒度的运行时 CPU 指标，PIP 能够准确估计反事实功耗，使控制系统更快地将功耗需求与预算对齐。与传统反应式方法不同，PIP 在频繁的预算波动下仍保持有效控制，实现高达 70% 的安全超售。我们在多样的应用工作负载（均不在模型训练集中）上的评估表明，对于单应用运行，PIP 相比最先进的基于反馈的系统最高实现 3.2× 的加速；在功耗约束下的多应用场景中最高实现 3.4× 的加速。

**英文关键词：** Data center operation, power management, power oversubscription

**中文关键词：** 数据中心运营、功耗管理、功耗超售

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
