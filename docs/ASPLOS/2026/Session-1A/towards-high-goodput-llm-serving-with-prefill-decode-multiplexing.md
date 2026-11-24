---
title: "Towards High-Goodput LLM Serving with Prefill-decode Multiplexing"
description: "ASPLOS 2026 · Session 1A · 面向预填充-解码多路复用的高有效吞吐 LLM 服务"
tags:
  - "ASPLOS2026"
  - "Session 1A"
  - "LLM Serving: Throughput Optimization"
---

# Towards High-Goodput LLM Serving with Prefill-decode Multiplexing

**中文标题：** 面向预填充-解码多路复用的高有效吞吐 LLM 服务

**所属 Session：** [Session 1A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Weihao Cui (Shanghai Jiao Tong University), Yukang Chen (Shanghai Jiao Tong University), Han Zhao (Shanghai Jiao Tong University), Ziyi Xu (Shanghai Jiao Tong University), Xiaoze Fan (Shanghai Jiao Tong University), Xusheng Chen (University of Hong Kong), Yangjie Zhou (National University of Singapore), Shixuan Sun (Shanghai Jiao Tong University), Bingsheng He (National University of Singapore), Quan Chen (Shanghai Jiao Tong University)

**单位：** Shanghai Jiao Tong University；University of Hong Kong；National University of Singapore

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790236) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Large Language Model (LLM) serving must meet stringent Service Level Objectives (SLOs) for both the prefill and decode phases. Some existing solutions disaggregate the two phases, causing potential resource idleness or compute redundancy. Others split the prefill phase into chunks and fuse it with decode iteration, creating a dilemma between SLO compliance and high utilization. To address these issues, an efficient serving system should dynamically adapt compute allocation, decouple compute from memory management, and execute prefill and decode independently. We present MuxWise, an LLM serving framework that adopts a new paradigm, intra-GPU prefill-decode multiplexing, to meet these requirements. To fully exploit the paradigm, MuxWise integrates a bubble-less multiplex engine, a contention-tolerant estimator, and an SLO-aware dispatcher. Evaluation shows that MuxWise improves peak throughput under SLO guarantees by an average of 2.20× (up to 3.06×) over state-of-the-art baselines.

## 中文摘要

大语言模型（LLM）服务必须同时满足预填充阶段与解码阶段严格的服务等级目标（SLO）。部分现有方案将这两个阶段分离（disaggregate），会造成潜在的资源闲置或计算冗余。另一些方案将预填充阶段切分为多个块并与解码迭代融合，形成了 SLO 满足与高利用率之间的两难。为解决这些问题，高效的服务系统应动态调整计算分配、将计算与内存管理解耦，并独立执行预填充与解码。我们提出 MuxWise，一个采用新范式——GPU 内预填充-解码多路复用（intra-GPU prefill-decode multiplexing）——的 LLM 服务框架，以满足上述需求。为充分发挥该范式的优势，MuxWise 集成了无气泡（bubble-less）多路复用引擎、可容忍资源竞争的估计器（contention-tolerant estimator）以及 SLO 感知调度器。评估表明，在 SLO 保障下，MuxWise 相较当前最优基线将峰值吞吐平均提升 2.20×（最高 3.06×）。

## 英文关键词

LLM Serving, PD-Multiplexing, Goodput

## 中文关键词

LLM 服务；PD 多路复用；有效吞吐

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790236)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 1A](index.md) · [返回 ASPLOS 2026](../index.md)
