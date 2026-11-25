---
title: "ETS: Deep Learning Training Iteration Time Prediction based on Execution Trace Sliding Window"
description: "HPDC 2024 · Session 5 — Performance modeling & LLMs"
tags:
  - "HPDC2024"
  - "Session 5"
  - "Performance modeling & LLMs"
---

# ETS: Deep Learning Training Iteration Time Prediction based on Execution Trace Sliding Window

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2024 主会 Session 5 — Performance modeling & LLMs（2024年6月6日 16:10–17:25 · Session Chair：Ignacio Laguna）。</p>
<p class="paper-seo-summary__tags">HPDC 2024 · Session 5</p>
</div>

**官方资料**：[HPDC 2024 官方议程](https://hpdc.sci.utah.edu/2024/program.html) · [ACM DOI](https://doi.org/10.1145/3625549.3658658)

**作者**：Zichao Yang, Hao GUO, Heng Wu, Yuewen WU, Hua Zhong, Wenbo ZHANG, Chuan Zhou, Yan Liu

**会议**：HPDC 2024 · Pisa, Italy

**Session**：Session 5 — Performance modeling & LLMs（2024年6月6日 16:10–17:25 · Session Chair：Ignacio Laguna）

---

## 英文摘要

Deep learning (DL) has become essential across various computer science domains. Accurately predicting iteration time for DL models in diverse cloud data center environments is critical for making high-quality scheduling decisions. Existing approaches neglect the sequential features inherent in the runtime execution, leading to issues such as overlooking DL framework overhead and struggling to handle diverse sizes of DL models, resulting in either low accuracy or slow convergence of the prediction model. This paper introduces ETS, a novel iteration time prediction method utilizing execution trace sliding windows. Our observation reveals that DL models exhibit a highly sequential runtime execution nature. Building upon this insight, we leverage sliding windows to extract a novel type of sequential features from the runtime execution trace. These features comprehensively capture DL framework overhead and address the diversity challenge in DL model sizes. By combining a best-practice method to train a prediction model, we achieve high accuracy and rapid convergence simultaneously. Experimental validation on over 14,000 DL model configurations demonstrates ETS’s effectiveness in predicting the iteration time of DL models, achieving a mere 5.9% prediction error with a training time at the 10-minute level, and improving scheduling outcomes by reducing job completion time by 17%.

## 中文摘要

深度学习（DL）已成为计算机科学各领域不可或缺的工具。在多样的云数据中心环境中准确预测 DL 模型的迭代时间，对于做出高质量调度决策至关重要。现有方法忽略了运行时执行固有的序列特征，导致忽视 DL 框架开销、难以处理不同规模的 DL 模型，从而造成预测模型精度低或收敛慢。本文提出 ETS，一种利用执行轨迹滑动窗口的新颖迭代时间预测方法。我们的观察揭示 DL 模型具有高度序列化的运行时执行特性。基于这一洞见，我们利用滑动窗口从运行时执行轨迹中提取一类新颖的序列特征。这些特征全面捕捉 DL 框架开销，并解决 DL 模型规模多样性带来的挑战。结合最佳实践的预测模型训练方法，我们同时实现了高精度与快速收敛。在 14000 多个 DL 模型配置上的实验验证表明，ETS 在预测 DL 模型迭代时间方面有效，预测误差仅 5.9%，训练时间在 10 分钟量级，并将作业完成时间缩短 17%，改善了调度效果。

## 英文关键词

performance modelling, deep learning training

## 中文关键词

性能建模，深度学习训练

---

[← 返回 Session 5 — Performance modeling & LLMs](index.md)
