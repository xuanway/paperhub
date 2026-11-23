---
title: "TrioSim: A Lightweight Simulator for Large-Scale DNN Workloads on Multi-GPU Systems"
description: "ISCA 2025 · Session 8A · TrioSim：面向多 GPU 系统大规模 DNN 负载的轻量级模拟器"
tags:
  - "ISCA2025"
  - "Session 8A"
  - "Performance and Modeling"
---

# TrioSim: A Lightweight Simulator for Large-Scale DNN Workloads on Multi-GPU Systems

**中文标题：** TrioSim：面向多 GPU 系统大规模 DNN 负载的轻量级模拟器

**所属 Session：** [Session 8A](index.md) · [ISCA 2025](../index.md)

**作者：** Ying Li, Yuhui Bao, Gongyu Wang, Xinxin Mei, Pranav Vaid, Anandaroop Ghosh, Adwait Jog, Darius Bunandar, Ajay Joshi, Yifan Sun

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731082) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Deep Neural Networks (DNNs) have become increasingly capable of performing tasks ranging from image recognition to content gen- eration. The training and inference of DNNs heavily rely on GPUs, as GPUs’ massively parallel architecture delivers extremely high computing capability. With the growing complexity of DNNs and the size of training datasets, training DNNs with a large number of GPUs is becoming a prevalent strategy. Researchers have been exploring how to design software and hardware systems for GPU farms to achieve the best utilization, efficiency, and DNN accuracy during training or inference. However, when designing and deploy- ing such systems, designers usually rely on testing on physical hard- ware platforms equipped with many GPUs, incurring high costs that are almost prohibitive for system designers to test different configurations and designs, even for highly resourceful companies. While an alternative solution is to test on GPU simulators, they are often too slow for these large-scale systems and depend on profiling details collected from real distributed systems to initiate the simulation. To address these challenges, we present TrioSim, a novel lightweight simulator for DNNs on multi-GPU systems. TrioSim combines performance modeling techniques and simula- tion methods to achieve high flexibility, high simulation speed, and high accuracy. TrioSim minimizes the required input from users by only relying on operator-level execution traces collected on a single GPU and can simulate new software and hardware designs that involve multiple GPUs connected with complex, asymmetrical interconnects. Completing within seconds, TrioSim predicts the execution time of DNN training on multi-GPU systems with aver- age errors of 2.91%, 4.54%, and 6.82% for data parallelism, tensor parallelism, and pipeline parallelism, respectively.

## 中文摘要

深度神经网络（DNN）已经能够完成图像识别、内容生成等各类任务。DNN的训练与推理高度依赖GPU，GPU的大规模并行架构可以提供极强算力。随着DNN复杂度、训练数据集规模持续增长，使用大量GPU开展DNN训练已成为主流方案。研究者不断探索GPU集群的软硬件系统设计，力求在训练或推理阶段获得最优的硬件利用率、执行效率与模型精度。
但在设计、部署这类系统时，开发者通常需要在搭载多块GPU的物理硬件平台上开展测试，成本高昂；即便是资源雄厚的企业，也很难遍历测试大量不同配置与架构方案。另一种备选方案是GPU仿真器，但这类仿真器针对大规模系统往往速度很慢，并且依赖真实分布式系统采集的性能剖面数据才能启动仿真。

针对上述难题，本文提出TrioSim，一款面向多GPU系统DNN负载的轻量化仿真器。TrioSim融合性能建模技术与仿真方法，兼顾高灵活性、仿真速度与预测精度。它对用户输入要求很低，仅需要在单块GPU上采集算子级执行轨迹，就可以仿真由多GPU组成、互联拓扑复杂且非对称的新型软硬件方案。
TrioSim可在数秒内完成仿真，对多GPU上DNN训练执行时间的预测误差：数据并行平均2.91%，张量并行平均4.54%，流水线并行平均6.82%。

## 英文关键词

Deep Neural Networks, Multi-GPU Systems, Simulation

## 中文关键词

深度神经网络, 多 GPU 系统, 模拟

## 代码与研究制品

- [代码仓库](https://github.com/sarchlab/triosim)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731082)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 8A](index.md) · [返回 ISCA 2025](../index.md)
