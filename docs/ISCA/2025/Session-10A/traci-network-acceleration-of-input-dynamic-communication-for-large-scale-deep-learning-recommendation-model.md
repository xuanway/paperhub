---
title: "TRACI: Network Acceleration of Input-Dynamic Communication for Large-Scale Deep Learning Recommendation Model"
description: "ISCA 2025 · Session 10A · TRACI：面向大规模深度学习推荐模型输入动态通信的网络加速"
tags:
  - "ISCA2025"
  - "Session 10A"
  - "ML Accelerators IV"
---

# TRACI: Network Acceleration of Input-Dynamic Communication for Large-Scale Deep Learning Recommendation Model

**中文标题：** TRACI：面向大规模深度学习推荐模型输入动态通信的网络加速

**所属 Session：** [Session 10A](index.md) · [ISCA 2025](../index.md)

**作者：** Guyue Huang, Hao Li, Le Qin, Jiayi Huang, Yangwook Kang, Yufei Ding, Yuan Xie

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731105) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Large-scale deep learning recommendation models (DLRMs) rely on embedding layers with terabyte-scale embedding tables, which present significant challenges to memory capacity. In addition, these embedding layers exhibit sparse and random data access patterns, which demand high memory bandwidth. Multi-GPU sys- tems provide a promising solution, allowing for the scaling of both memory and aggregated bandwidth. However, network commu- nication bandwidth becomes a bottleneck for multi-GPU DLRM systems. Overcoming the communication bottleneck is crucial to unlocking the potential of multi-GPU systems for efficient and high-performance DLRM training. This paper introduces TRACI, an in-network acceleration ar- chitecture designed to optimize the communication operator in embedding layers: Aggregation. While in-network acceleration has proven successful for the All-Reduce communication collective, ex- isting solutions do not directly apply to Aggregation due to two key challenges. Firstly, existing multi-GPU shared memory operations are designed for point-to-point communication and do not allow the network to proactively optimize communication. Secondly, in Aggregation, data transfer patterns are dynamic and dependent on input, demanding the network to dynamically discover and exploit message connections on-the-fly. To address these challenges, we propose a solution that involves a novel network transaction and switch hardware design. We introduce a new network transaction that augments messages with input reuse and output reuse iden- tifications, and can empower the network to proactively reduce data transfers. Additionally, we present an in-switch cache and a reduction table structure, effectively harnessing input and output reuse opportunities. Using these innovations, TRACI achieves up to 4.04×and an average of 3.12×speedup to Aggregation for a 64-GPU system.

## 中文摘要

大规模深度学习推荐模型（DLRM）依赖包含TB级嵌入表的嵌入层，对存储容量提出极高要求。同时，嵌入层访存具有稀疏、随机的特征，需要很高的内存带宽。多GPU系统是一种可行方案，可以同时扩展存储容量与聚合带宽。但在多GPU DLRM系统中，网络通信带宽会成为瓶颈。突破通信瓶颈，是充分发挥多GPU系统能力、实现高效高性能DLRM训练的关键。

本文提出TRACI，一种网内加速架构，专门优化嵌入层中的通信算子：聚合（Aggregation）。虽然网内加速在All-Reduce集合通信上已经取得很好效果，但现有方案无法直接适配聚合算子，存在两大难点：第一，现有多GPU共享内存操作面向点对点通信设计，网络无法主动优化通信；第二，聚合的数据传输模式是动态、输入相关的，要求网络能够实时发现并利用消息之间的关联。

针对上述问题，本文设计全新的网络事务与交换机硬件。定义一种新型网络事务，在消息中附带输入复用、输出复用标识，让网络可以主动削减数据传输量；同时提出交换机内缓存与归约表结构，充分挖掘输入、输出复用机会。依托这些创新，在64-GPU集群上，TRACI对聚合算子最高提速4.04倍，平均提速3.12倍。

## 英文关键词

Deep Learning Recommendation System, GPU

## 中文关键词

深度学习推荐模型, GPU

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731105)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 10A](index.md) · [返回 ISCA 2025](../index.md)
