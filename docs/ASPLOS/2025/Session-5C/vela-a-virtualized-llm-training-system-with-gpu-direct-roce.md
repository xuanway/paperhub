---
title: "Vela: A Virtualized LLM Training System with GPU Direct RoCE"
description: "ASPLOS 2025 · Session 5C · Vela：基于 GPU Direct RoCE 的虚拟化 LLM 训练系统"
tags:
  - "ASPLOS2025"
  - "Session 5C"
  - "Large Language Models"
---

# Vela: A Virtualized LLM Training System with GPU Direct RoCE

**中文标题：** Vela：基于 GPU Direct RoCE 的虚拟化 LLM 训练系统

**所属 Session：** [Session 5C](index.md) · [ASPLOS 2025](../index.md)

**作者：** Apoorve Mohan (IBM Research), Robert Walkup (IBM Research), Bengi Karacali (IBM Research), Ming-Hung Chen (IBM Research), Abdullah Kayi (IBM Research), Liran Schour (IBM), Shweta Salaria (IBM Research), Sophia Wen (IBM Research), IHsin Chung (IBM Research), Abdul Alim (IBM Research), Constantinos Evangelinos (IBM Research), Lixiang Luo (IBM Research), Marc Dombrowa (IBM Research), Laurent Schares (IBM Research), Ali Sydney (IBM Research), Pavlos Maniotis (IBM Research), Sandhya Koteshwara (IBM Research), Brent Tang (IBM), Joel Belog (IBM), Rei Odaira (IBM), Vasily Tarasov (IBM Research), Eran Gampel (IBM Cloud), Drew Thorstensen (IBM), Talia Gershon (IBM Research), Seetharami Seelam (IBM Research)

**单位：** IBM Research；IBM；IBM Cloud

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716280) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Vela is a cloud-native system designed for LLM training workloads built using off-the-shelf hardware, Linux KVM-based virtualization, and a virtualized RDMA over Converged Ethernet (RoCE) network. Vela virtual machines (VMs) support,. sed network interface. In this paper, we share Vela's key architectural aspects with details from an NVIDIA A100 GPU-based deployment in one of the IBM Cloud data centers. Throughout the paper, we share insights and experiences from designing, building, and operating the system over a ∼2.5 year timeframe to highlight the capabilities of readily available software and hardware technologies and the improvement opportunities for future AI systems, thereby making AI infrastructure more accessible to a broader community. As we evaluated the system for performance at ∼1500 GPU scale, we achieved ∼80% of the ideal throughput while training a 50 billion parameter decoder model using model parallelism, and ∼70% HighPerformance Linpack benchmark.

## 中文摘要

Vela 是一个面向 LLM 训练工作负载的云原生系统，采用现成硬件、基于 Linux KVM 的虚拟化以及虚拟化的融合以太网 RDMA（RoCE）网络构建。Vela 虚拟机（VM）支持,. sed 网络接口。在本文中，我们结合 IBM Cloud 某数据中心内基于 NVIDIA A100 GPU 的部署细节，分享 Vela 的关键架构设计。在全文各节中，我们分享在约 2.5 年时间里设计、构建与运维该系统所得的见解与经验，以凸显现成可用的软硬件技术所具备的能力以及未来 AI 系统的改进空间，从而使 AI 基础设施对更广泛的使用群体更加可及。当我们在约 1500 GPU 规模上评估该系统的性能时，在使用模型并行训练 500 亿参数解码器模型时达到了理想吞吐的约 80%，并达到 HighPerformance Linpack 基准测试的约 70%。

## 英文关键词

Virtualization, Cloud Computing, High Performance Computing, AI Infrastructure

## 中文关键词

虚拟化；云计算；高性能计算；AI 基础设施

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716280)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 5C](index.md) · [返回 ASPLOS 2025](../index.md)
