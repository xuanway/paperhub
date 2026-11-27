---
title: "The Importance of Generalizability in Machine Learning for Systems"
description: "HPCA 2025 · Best of CAL"
tags:
  - "HPCA2025"
  - "Best of CAL"
---

# The Importance of Generalizability in Machine Learning for Systems

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Best of CAL。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Best of CAL</p>
</div>

**论文链接**：
**作者**：Varun Gohil (Massachusetts Institute of Technology), Sundar Dev (Google), Gaurang Upasani (Google), David Lo (Google), Parthasarathy Ranganathan (Google), Christina Delimitrou (Massachusetts Institute of Technology)
**会议**：HPCA 2025

---

## 中文标题

机器学习用于系统时泛化能力的重要性

## 英文摘要

Using machine learning (ML) to tackle computer systems tasks is gaining popularity. One of the shortcomings of such ML-based approaches is the inability of models to generalize to out-of-distribution data i.e., data whose distribution is different than the training dataset. We showcase that this issue exists in cloud environments by analyzing various ML models used to improve resource balance in Google's fleet. We discuss the trade-offs associated with different techniques used to detect out-of-distribution data. Finally, we propose and demonstrate the efficacy of using Bayesian models to detect the model's confidence in its output when used to improve cloud server resource balance.

## 中文摘要

使用机器学习（ML）来应对计算机系统的各类任务正变得越来越流行，相关研究也在迅速增加。然而，此类基于 ML 的方法存在一项不足，即模型缺乏泛化能力：它无法泛化到分布外数据，也就是其分布与训练数据集不同的数据。一旦部署环境中的数据分布与训练时不同，模型的预测就可能不再可靠。我们通过分析 Google 集群中用于改善资源平衡的多种 ML 模型，展示了这一问题在云环境中确实存在。我们还讨论了为检测这类分布外数据而采用的不同技术，以及它们各自所伴随的权衡与取舍。最后，针对模型被用于改善云服务器资源平衡这一场景，我们提出使用贝叶斯模型来检测模型对其输出的置信度，并演示了这种做法在该场景下的有效性。
