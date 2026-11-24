---
title: "DS-TPU: Dynamical System for on-Device Lifelong Graph Learning with Nonlinear Node Interaction"
description: "ISCA 2025 · Session 10A · DS-TPU：面向设备端终身图学习的非线性节点交互动力系统"
tags:
  - "ISCA2025"
  - "Session 10A"
  - "ML Accelerators IV"
---

# DS-TPU: Dynamical System for on-Device Lifelong Graph Learning with Nonlinear Node Interaction

**中文标题：** DS-TPU：面向设备端终身图学习的非线性节点交互动力系统

**所属 Session：** [Session 10A](index.md) · [ISCA 2025](../index.md)

**作者：** Chunshu Wu, Ruibing Song, Chuan Liu, Pouya Haghi, Ang Li, Michael Huang, Tong (Tony) Geng

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731091) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Graph learning on dynamical systems has recently surfaced as an emerging research domain. By leveraging a novel electronic Dy- namical System (DS), various graph learning challenges have been effectively tackled through a rapid, spontaneous natural annealing process. This method has attracted increasing attention due to its orders-of-magnitude improvements in speed and energy efficiency compared to traditional Graph Neural Network (GNN) approaches for inference tasks. However, (1) the current DS hardware only supports inference, missing its native solution for training; while relying on conventional hardware is likely more expensive than GNNs. (2) The current DS architecture only allows linear interac- tions among its nodes, limiting training accuracy. In this work, we present a Dynamical-System Training-Processing Unit (DS-TPU) developed through algorithm-architecture co-design to tackle the two major challenges: (1) An on-device lifelong learn- ing mechanism that leverages feedback electric current as the loss function in response to the observed training data, allowing electron-speed refinement on the present model parameters. (2) A nonlinear DS node interaction mechanism constructed from Cheby- shev polynomials to significantly improve the compatibility be- tween the DS hardware and the embedded relation of graph data. Extensive evaluations using six real-world graph learning applica- tions demonstrate that for accuracy, DS-TPU achieves 10.8% MAE reduction over the best results of five widely used GNNs. In terms of training performance, the 5-Watt DS-TPU architecture achieves on- average 810×speedup over the offline training for DS on an Nvidia A100 GPU, and 640×over GNN training on the same GPU. In terms of inference performance, DS-TPU achieves 2548×over the A100 GPU and 115×over the best state-of-the-art GNN accelerators.

## 中文摘要

动态系统上的图学习是近年新兴研究方向。该方法利用一种新型电子动态系统（DS），借助快速自发的自然退火过程，高效求解各类图学习任务。相较于传统图神经网络（GNN）推理，它在速度与能效上高出数个数量级，因此受到越来越多关注。但该方案存在两大短板：（1）现有动态系统硬件仅支持推理，缺少原生训练方案；如果依赖传统硬件做训练，开销甚至高于GNN；（2）现有动态系统架构的节点之间仅支持线性交互，制约了训练精度。

本文通过算法-架构协同设计，提出动态系统训练处理单元（DS-TPU），解决上述两个核心问题：（1）设备端终身学习机制，以反馈电流作为损失函数响应观测到的训练数据，以电子传输速度对模型参数进行迭代调优；（2）基于切比雪夫多项式构建非线性动态系统节点交互机制，大幅提升动态系统硬件与图数据内在关联特征的适配性。

在6个真实图学习任务上的大量评测表明：精度方面，DS-TPU相比5种主流GNN的最优结果，平均绝对误差（MAE）降低10.8%；训练性能上，5瓦功耗的DS-TPU架构，相比在NVIDIA A100上离线训练动态系统模型平均提速810倍，相比同卡上GNN训练提速640倍；推理性能上，DS-TPU相比A100 GPU提速2548倍，对比最优GNN专用加速器提速115倍。

## 英文关键词

Dynamical System, Energy-Based Model, Graph Learning

## 中文关键词

动力系统, 基于能量的模型, 图学习

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731091)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 10A](index.md) · [返回 ISCA 2025](../index.md)
