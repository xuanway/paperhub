---
title: "Flex: Fast, Accurate DNN Inference on Low-Cost Edges Using Heterogeneous Accelerator Execution"
description: "EuroSys 2025 · ML Systems · Tanmoy Sen (University of Virginia), Haiying Shen (University of Virginia), Anan"
tags:
  - "EuroSys2025"
  - "ML Systems"
---

# Flex: Fast, Accurate DNN Inference on Low-Cost Edges Using Heterogeneous Accelerator Execution

**中文标题：** 利用异构加速器执行在低成本边缘设备上实现快速准确的深度神经网络推理

**所属 Session：** [Session 4.1: ML Systems](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：ML Systems。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · ML Systems</p>
</div>

**作者**：Tanmoy Sen (University of Virginia), Haiying Shen (University of Virginia), Anand Iyer (Georgia Tech)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696067)

## 英文摘要

Significant breakthroughs in machine learning (ML) and the advantages of on-device processing have led to edge devices increasingly incorporating accelerators like GPUs, NPUs, and DSPs. However, these accelerators consume energy, prompting users to limit their floating-point precision. Many edge device users are in regions where including high-fidelity accelerators is too costly, leading to low-cost devices with low precision, sacrificing accuracy. Previous work predetermined layer assignments between the CPU and accelerator offline for high accuracy and low latency without considering the input, but we observe that input affects optimal layer assignment. To address this, we present Flex, a system for Fast, Accurate DNN Inference on Low-Cost Edges using Heterogeneous Accelerator eXecution. Leveraging common observations from models on various edge devices, Flex uses a lightweight heuristic and reinforcement learning (RL) to dynamically assign layers across the CPU and accelerator. Experiments show Flex improves average inference time by up to 39%, accuracy by up to 22%, and energy consumption by up to 61% compared to state-of-the-art methods, and is only 4.2% less optimal than the best achievable results.

## 中文摘要

机器学习（ML）的重大突破以及端侧处理的优势，使边缘设备越来越多地集成 GPU、NPU 和 DSP 等加速器。然而，这些加速器会消耗能量，促使用户限制浮点精度。许多边缘设备用户所在地区难以承担高保真加速器的成本，因而只能使用低精度、牺牲精度的低成本设备。先前的工作为了兼顾高精度与低延迟，离线预先确定 CPU 与加速器之间的层分配，而未考虑输入，但我们观察到输入会影响最优的层分配。为此，我们提出 Flex，一个利用异构加速器执行在低成本边缘设备上实现快速、准确 DNN 推理的系统。基于在各种边缘设备上从模型中得到的共性观察，Flex 使用轻量级启发式方法与强化学习（RL）在 CPU 与加速器之间动态分配层。实验表明，与最先进的方法相比，Flex 将平均推理时间最多改善 39%、精度最多提升 22%、能耗最多降低 61%，且与可达最优结果相比仅差 4.2%。

**英文关键词：** Edge devices, Low Cost Accelerators, Mobile computing, Machine learning

**中文关键词：** 边缘设备、低成本加速器、移动计算、机器学习

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
