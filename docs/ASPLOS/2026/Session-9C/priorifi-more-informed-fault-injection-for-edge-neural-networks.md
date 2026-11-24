---
title: "PrioriFI: More Informed Fault Injection for Edge Neural Networks"
description: "ASPLOS 2026 · Session 9C · PrioriFI：面向边缘神经网络的更知情故障注入"
tags:
  - "ASPLOS2026"
  - "Session 9C"
  - "Reliability & Fault Tolerance"
---

# PrioriFI: More Informed Fault Injection for Edge Neural Networks

**中文标题：** PrioriFI：面向边缘神经网络的更知情故障注入

**所属 Session：** [Session 9C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Olivia Weng (UC San Diego), Andres Meza (UC San Diego), Nhan Tran (Fermilab), Ryan Kastner (UC San Diego)

**单位：** UC San Diego；Fermilab

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790204) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

As neural networks (NNs) are increasingly used to provide edge intelligence, there is a growing need to make the edge devices that run them robust to faults. Edge devices must mitigate the resulting hardware failures while maintaining strict constraints on power, energy, latency, throughput, memory size, and computational resources. Edge NNs require fundamental changes in model architecture, e.g., quantization and fewer, smaller layers. PrioriFI is a more informed fault injection (FI) algorithm that evaluates edge NN robustness by ranking NN bits based on their fault sensitivity. PrioriFI prioritizes finding highly fault-sensitive bits, that is, the bits most critical to an NN's correctness, first. To accomplish this, PrioriFI uses the Hessian for the initial parameter ranking. Then, during an FI campaign, PrioriFI uses the information gained from past FIs as a heuristic so that future FIs target the bits likely to be the next most sensitive. With PrioriFI, designers can quickly evaluate different NNs and better co-design fault-tolerant edge NN systems.

## 中文摘要

随着神经网络（NN）越来越多地被用于提供边缘智能，人们越来越需要让运行这些网络的边缘设备对故障具有鲁棒性。边缘设备必须缓解由此产生的硬件故障，同时保持对功耗、能耗、延迟、吞吐、内存大小和计算资源的严格约束。边缘 NN 需要在模型架构上做出根本性改变，例如量化以及更少、更小的层。PrioriFI 是一种更知情的故障注入（FI）算法，它通过基于故障敏感度对 NN 的比特进行排序，来评估边缘 NN 的鲁棒性。PrioriFI 优先寻找高度故障敏感的比特，即对 NN 正确性最为关键的比特。为实现这一点，PrioriFI 使用 Hessian 进行初始参数排序。随后，在 FI 活动期间，PrioriFI 将过去 FI 中获得的信息用作启发式依据，使后续 FI 瞄准那些可能是下一个最敏感的比特。借助 PrioriFI，设计者可以快速评估不同的 NN，并更好地协同设计容错边缘 NN 系统。

## 英文关键词

edge AI; hardware-software codesign; neural network reliability; transient errors

## 中文关键词

边缘 AI；软硬件协同设计；神经网络可靠性；瞬态错误

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790204)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 9C](index.md) · [返回 ASPLOS 2026](../index.md)
