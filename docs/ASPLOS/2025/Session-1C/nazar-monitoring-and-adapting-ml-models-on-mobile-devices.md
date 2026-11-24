---
title: "Nazar: Monitoring and Adapting ML Models on Mobile Devices"
description: "ASPLOS 2025 · Session 1C · Nazar：移动设备上机器学习模型的监控与自适应"
tags:
  - "ASPLOS2025"
  - "Session 1C"
  - "Edge Computing"
---

# Nazar: Monitoring and Adapting ML Models on Mobile Devices

**中文标题：** Nazar：移动设备上机器学习模型的监控与自适应

**所属 Session：** [Session 1C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Wei Hao (Columbia University), Zixi Wang (Columbia University), Lauren Hong (Columbia University), Lingxiao Li (Columbia University), Nader Karayanni (Columbia University), AnMei Dasbach-Prisk (University of California San Diego), Chengzhi Mao (Columbia University), Junfeng Yang (Columbia University), Asaf Cidon (Columbia University)

**单位：** Columbia University；University of California San Diego

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707246) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

ML models are increasingly run locally on mobile devices for low-latency inference and offline operation. However, it is hard for ML operators to track on-device model accuracy, which can degrade unpredictably (e.g., due to local data drift). We design Nazar, the first end-to-end system for continuously monitoring and adapting models on mobile devices without requiring feedback from users. Our key observation is that accuracy degradation is often due to a specific root cause, which may affect a large group of devices. Once Nazar detects a degradation affecting a large number of devices, it automatically pinpoints the root causes and adapts the model specifically to them. Evaluation on two computer vision datasets shows that Nazar consistently boosts accuracy compared to existing approaches by up to 19.4%.

## 中文摘要

为了获得低时延推理与离线运行能力，ML 模型越来越多地在移动设备本地执行。然而，ML 运营方难以跟踪设备端模型的精度，而该精度可能不可预测地退化（例如由本地数据漂移引起）。我们设计了 Nazar，这是首个无需用户反馈即可在移动设备上持续监控并自适应调整模型的端到端系统。我们的关键观察是：精度退化往往由某个特定根因造成，而该根因可能影响一大群设备。一旦 Nazar 检测到影响大量设备的精度退化，它就会自动定位根因，并针对这些根因对模型进行适配。在两个计算机视觉数据集上的评估表明，与现有方法相比，Nazar 能够持续提升精度，最高可达 19.4%。

## 英文关键词

Machine Learning System Design; Root Cause Analysis; Drift Adaptation; Mobile Devices

## 中文关键词

机器学习系统设计；根因分析；漂移自适应；移动设备

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707246)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 1C](index.md) · [返回 ASPLOS 2025](../index.md)
