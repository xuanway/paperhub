---
title: "Training one DeePMD Model in Minutes: a Step towards Online Learning"
description: "PPoPP 2024 Session ML Workloads：小批量拟牛顿优化器，8 数据集平均 32.2×，DeePMD 训练降至分钟级"
tags:
  - "PPoPP2024"
  - "Session-6"
  - "ML Workloads"
  - "Parallel training"
  - "Molecular dynamics"
  - "GPU"
authors:
  - "Siyu Hu"
  - "Tong Zhao"
  - "Qiuchen Sha"
  - "Enji Li"
  - "Xiangyu Meng"
  - "Liping Liu"
  - "Lin-Wang Wang"
  - "Guangming Tan"
  - "Weile Jia"
session: "Session 6: ML Workloads"
session_number: 6
session_chair: "Xipeng Shen"
date: "2024-03-05"
time: "12:10–12:30"
room: "Moorfoot"
doi: "10.1145/3627535.3638505"
program_url: "https://ppopp24.sigplan.org/program/program-PPoPP-2024/"
---

# Training one DeePMD Model in Minutes: a Step towards Online Learning

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">针对 DeePMD 训练的原子力拟合难题，该文设计基于扩展卡尔曼滤波的小批量拟牛顿优化器，8 个数据集上平均加速 32.2 倍，训练从数小时降至数分钟。</p>
<p class="paper-seo-summary__tags">PPoPP 2024 · Session 6: ML Workloads</p>
</div>

**作者**：Siyu Hu, Tong Zhao, Qiuchen Sha, Enji Li (State Key Lab of Processors, Institute of Computing Technology, Chinese Academy of Sciences; University of Chinese Academy of Sciences); Xiangyu Meng (College of Computer Science and Technology, Qingdao Institute of Software, China University of Petroleum); Liping Liu, Lin-Wang Wang (Institute of Semiconductors, Chinese Academy of Sciences; University of Chinese Academy of Sciences); Guangming Tan, Weile Jia (State Key Lab of Processors, Institute of Computing Technology, Chinese Academy of Sciences; University of Chinese Academy of Sciences)

**会议**：PPoPP 2024 · 2024 年 3 月 5 日 12:10–12:30 · Session 6: ML Workloads（主席：Xipeng Shen）· Moorfoot

**论文**：[ACM Digital Library](https://doi.org/10.1145/3627535.3638505) · [PPoPP 2024 会议日程](https://ppopp24.sigplan.org/program/program-PPoPP-2024/)

---

## 英文摘要

Neural Network Molecular Dynamics (NNMD) has become a major approach in material simulations, which can speedup the molecular dynamics (MD) simulation for thousands of times, while maintaining ab initio accuracy, thus has a potential to fundamentally change the paradigm of material simulations. However, there are two time-consuming bottlenecks of the NNMD developments. One is the data access of ab initio calculation results. The other, which is the focus of the current work, is reducing the training time of NNMD model. The training of NNMD model is different from most other neural network training because the atomic force (which is related to the gradient of the network) is an important physical property to be fit. Tests show the traditional stochastic gradient methods, like the Adam algorithms, cannot efficiently deploy the multisample minibatch algorithm. As a result, a typical training (taking the Deep Potential Molecular Dynamics (DeePMD) as an example) can take many hours. In this work, we designed a heuristic minibatch quasi-Newtonian optimizer based on Extended Kalman Filter method. An early reduction of gradient and error is adopted to reduce memory footprint and communication. The memory footprint, communication and settings of hyper-parameters of this new method are analyzed in detail. Computational innovations such as customized kernels of the symmetry-preserving descriptor are applied to exploit the computing power of the heterogeneous architecture. Experiments are performed on 8 different datasets representing different real case situations, and numerical results show that our new method has an average speedup of 32.2 compared to the Reorganized Layer-wised Extended Kalman Filter with 1 GPU, reducing the absolute training time of one DeePMD model from hours to several minutes, making it one step toward online training.

## 中文摘要

神经网络分子动力学（NNMD）已成为材料模拟中的主要方法，它可以将分子动力学（MD）模拟加速数千倍，同时保持从头算（ab initio）精度，因而有潜力从根本上改变材料模拟的范式。然而，NNMD 的开发存在两个耗时瓶颈。一是从头算计算结果的数据访问。另一个（也是当前工作的重点）是缩短 NNMD 模型的训练时间。NNMD 模型的训练与大多数其他神经网络训练不同，因为原子力（它与网络梯度相关）是需要拟合的重要物理性质。测试表明，传统随机梯度方法（如 Adam 算法）无法高效地部署多样本小批量（minibatch）算法。结果，一次典型训练（以深度势分子动力学（DeePMD）为例）可能耗时数小时。在本工作中，我们基于扩展卡尔曼滤波方法设计了一种启发式的小批量拟牛顿优化器。采用梯度与误差的提前归约以降低内存占用和通信。本文详细分析了这一新方法的内存占用、通信与超参数设置。应用了对称保持描述符的定制内核等计算创新，以发挥异构架构的算力。实验在代表不同真实场景的 8 个不同数据集上进行，数值结果表明，与单 GPU 上的重组织逐层扩展卡尔曼滤波方法相比，我们的新方法平均加速 32.2 倍，将单个 DeePMD 模型的绝对训练时间从数小时缩短到几分钟，使其朝着在线训练迈出一步。

## 英文关键词

Parallel training, Molecular dynamics, First principle, ab initio, GPU

## 中文关键词

并行训练；分子动力学；第一性原理；从头算；GPU

---

## 一句话总结

> 针对 DeePMD 训练的原子力拟合难题，该文设计基于扩展卡尔曼滤波的小批量拟牛顿优化器，8 个数据集上平均加速 32.2 倍，训练从数小时降至数分钟。

## 研究问题

NNMD 训练需拟合与网络梯度相关的原子力，传统随机梯度方法（如 Adam）无法高效部署多样本小批量，使一次典型 DeePMD 训练需数小时，难以支撑在线学习。

## 方法简述

- 基于扩展卡尔曼滤波方法设计启发式小批量拟牛顿优化器，替代 Adam 等随机梯度方法以适配原子力拟合。
- 采用梯度与误差的提前归约（early reduction），降低内存占用与通信量。
- 详细分析新方法的内存占用、通信与超参数设置，并应用对称保持描述符的定制内核以发挥异构架构算力。

## 主要结果

- 在代表不同真实场景的 8 个数据集上，相比单 GPU 上的重组织逐层扩展卡尔曼滤波方法平均加速 32.2 倍。
- 将单个 DeePMD 模型的绝对训练时间从数小时缩短到几分钟，向在线训练迈出一步。

---

> 所属 Session：[Session 6: ML Workloads](index.md) · 返回 [PPoPP 2024 总览](../index.md)
