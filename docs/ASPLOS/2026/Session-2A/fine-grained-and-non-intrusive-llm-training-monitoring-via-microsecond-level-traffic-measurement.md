---
title: "Fine-grained and Non-intrusive LLM Training Monitoring via Microsecond-level Traffic Measurement"
description: "ASPLOS 2026 · Session 2A · 基于微秒级流量测量的细粒度且非侵入式 LLM 训练监控"
tags:
  - "ASPLOS2026"
  - "Session 2A"
  - "LLM Training Systems"
---

# Fine-grained and Non-intrusive LLM Training Monitoring via Microsecond-level Traffic Measurement

**中文标题：** 基于微秒级流量测量的细粒度且非侵入式 LLM 训练监控

**所属 Session：** [Session 2A](index.md) · [ASPLOS 2026](../index.md)

**作者：** Yibo Xiao (Nanjing University), Hao Zheng (Nanjing University, China.), Haifeng Sun (National University of Singapore), Qingkai Meng (Nanjing University), Jiong Duan (Nanjing University), Xiaohe Hu (Infrawaves), Rong Gu (Nanjing University), Guihai Chen (Nanjing University), Chen Tian (Nanjing University)

**单位：** Nanjing University；Nanjing University, China.；National University of Singapore；Infrawaves

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790163) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Large language model (LLM) training is prone to anomalies due to its long duration and large scale, which can lead to significant performance degradation or even training crashes. Due to the synchronization nature of LLM training, anomalies exhibit the cascading effect, making their diagnosis challenging. Existing approaches rely on collecting communication operator information via code instrumentation, which yields only coarse-grained monitoring data and requires modifications to training code or communication libraries. We propose Pulse, a fine-grained, non-intrusive, and easyto-deploy monitoring system. Our key idea is to enable fine-grained monitoring via traffic measurement. Pulse conducts microsecond-level RDMA traffic measurement on NICs, and transforms flow-level measurements into communication operator measurements, thereby enabling fine-grained and non-intrusive monitoring. We deploy Pulse on a testbed with 64 H200 GPUs and evaluate its anomaly localization capability under common failure scenarios. Pulse achieves machine-level localization in 10 out of 12 scenarios, while existing methods succeed in only 4 and even misdiagnose 2 of the remaining scenarios. Additionally, Pulse achieves over 90% precision and 100% recall, supports up to 2000 concurrent RDMA flow measurements per NIC, and imposes negligible overhead on training performance, making it a practical solution for real-world LLM training environments.

## 中文摘要

大语言模型（LLM）训练因其长时长和大规模而容易发生异常，这些异常可能导致显著的性能下降甚至训练崩溃。由于 LLM 训练的同步特性，异常会表现出级联效应，使其诊断颇具挑战。现有方法依赖通过代码插桩收集通信算子信息，只能获得粗粒度的监控数据，并且需要修改训练代码或通信库。我们提出 Pulse，一个细粒度、非侵入式且易于部署的监控系统。我们的核心思想是通过流量测量实现细粒度监控。Pulse 在网卡（NIC）上进行微秒级的 RDMA 流量测量，并将流级测量转化为通信算子测量，从而实现细粒度且非侵入式的监控。我们在配备 64 块 H200 GPU 的测试平台上部署 Pulse，并评估其在常见故障场景下的异常定位能力。在 12 个场景中，Pulse 在其中 10 个实现了机器级定位，而现有方法仅在 4 个场景中成功，甚至对其余 2 个场景作出误诊。此外，Pulse 实现了超过 90% 的精确率和 100% 的召回率，每个网卡支持多达 2000 个并发 RDMA 流量测量，并且对训练性能带来的开销可忽略不计，使其成为适用于真实 LLM 训练环境的实用方案。

## 英文关键词

Network Measurement; LLM Training Monitoring; Smart NICs

## 中文关键词

网络测量；LLM 训练监控；智能网卡

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790163)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 2A](index.md) · [返回 ASPLOS 2026](../index.md)
