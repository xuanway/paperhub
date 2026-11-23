---
title: "FRED: A Wafer-scale Fabric for 3D Parallel DNN Training"
description: "ISCA 2025 · Session 1A · FRED: 用于3D并行DNN训练的Wafer-scale互联结构"
tags:
  - "ISCA2025"
  - "Session 1A"
  - "ML Accelerators I"
---

# FRED: A Wafer-scale Fabric for 3D Parallel DNN Training

**中文标题：** FRED: 用于3D并行DNN训练的Wafer-scale互联结构

**所属 Session：** [Session 1A](index.md) · [ISCA 2025](../index.md)

**作者：** Saeed Rashidi, William Won, Sudarshan Srinivasan, Puneet Gupta, Tushar Krishna

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731055) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Wafer-scale systems are an emerging technology that tightly integrates high-end accelerator chiplets with high-speed wafer-scale interconnects, enabling low-latency and high-bandwidth connectivity. This makes them a promising platform for deep neural network (DNN) training. However, current network-on-wafer topologies, such as 2D Meshes, lack the flexibility needed to support various parallelization strategies effectively. In this paper, we propose Fred, a wafer-scale fabric architecture tailored to the unique communication needs of DNN training. Fred creates a distributed on-wafer topology with tiny microswitches, providing nonblocking connectivity for collective communications between arbitrary groups of accelerators and enabling in-switch collective support. Our results show that for sample parallelization strategies, Fred can improve the average end-to-end training time of ResNet-152, Transformer-17B, GPT-3, and Transformer-1T by 1.76×, 1.87×, 1.34×, and 1.4×, respectively, compared to a baseline wafer-scale Mesh.

## 中文摘要

晶圆级系统是一项新兴技术，它将高端加速器小芯片与高速晶圆级互连紧密集成，从而实现低延迟和高带宽连接。这使它们成为深度神经网络（DNN）训练的有前途的平台。然而，当前的晶圆上网络拓扑（例如 2D 网格）缺乏有效支持各种并行化策略所需的灵活性。在本文中，我们提出了 Fred，这是一种针对 DNN 训练的独特通信需求量身定制的晶圆级互连结构架构。 Fred 创建了带有微型交换机的分布式晶圆上拓扑，为任意加速器组之间的集合通信提供无阻塞连接，并实现交换机内集合通信支持。我们的结果表明，对于所评估的并行化策略，与基准晶圆级 Mesh 相比，Fred 可以将 ResNet-152、Transformer-17B、GPT-3 和 Transformer-1T 的端到端训练分别获得 1.76×、1.87×、1.34× 和 1.4×。

## 英文关键词

Wafer-Scale Systems, Distributed DNN Training, Collective Communication, Network Topology

## 中文关键词

晶圆级系统, 分布式深度神经网络训练, 集合通信, 网络拓扑

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731055)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 1A](index.md) · [返回 ISCA 2025](../index.md)
