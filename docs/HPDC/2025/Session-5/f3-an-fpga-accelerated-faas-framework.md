---
title: "F3: An FPGA-accelerated FaaS Framework"
description: "HPDC 2025 · Session 5 — Clouds and FaaS"
tags:
  - "HPDC2025"
  - "Session 5"
  - "Clouds and FaaS"
---

# F3: An FPGA-accelerated FaaS Framework

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2025 主会 Session 5 — Clouds and FaaS（2025年7月22日 15:30–16:50 · Session Chair：Hao Wang）。</p>
<p class="paper-seo-summary__tags">HPDC 2025 · Session 5</p>
</div>

**官方资料**：[HPDC 2025 官方议程](https://hpdc.sci.utah.edu/2025/program.html) · [ACM DOI](https://doi.org/10.1145/3731545.3731582) · [Slides](https://hpdc.sci.utah.edu/2025/assets/slides/main_session/koshiba.pdf)

**作者**：Charalampos Mainas, Martin Lambeck, Bruno Scheufler, Laurent Bindschaedler, Atsushi Koshiba, Pramod Bhatotia

**会议**：HPDC 2025 · Notre Dame, IN, USA

**Session**：Session 5 — Clouds and FaaS（2025年7月22日 15:30–16:50 · Session Chair：Hao Wang）

---

## 英文摘要

FPGAs provide a programmable, energy-efficient, and compute-intensive acceleration substrate; thus, on the one hand, they offer a compelling solution for optimizing serverless workloads in cloud environments. On the other hand, FPGAs also introduce significant challenges that directly contradict the serverless model in the cloud, includingtheirlow-levelandcomplexprogrammingAPIs,lackofvirtualization and isolation mechanisms, high reconfiguration and communication overheads, and absence of orchestration mechanisms. To this end, we present F3, the first system that enables efficient and secure use of FPGAs to accelerate serverless functions. F3 allows serverless functions to easily offload their tasks to FPGAs without worrying about low-level device management. The system automatically deploys and invokes FPGA-accelerated functions while providing isolation, high throughput, and low latency. To achieve thesedesigngoals,F3simplifiesthecomplexityofFPGAinitialization by a high-level hardware-agnostic API, enables function isolation with unikernel-based FPGA virtualization, reduces cold starts and communication overheads with a per-node FPGA resource manager, and maximizes FPGA utilization with an FPGA-aware orchestrator. Weimplementanopen-sourceprototypeof F3basedonapractical serverless framework, which consists of OpenFaaS, Kubernetes, and containerd, following the CRI/OCI industry standards for cloud orchestrationengines.Ourevaluationdemonstratessignificantlatency reduction and throughput improvements for real-world application workloads, microbenchmarks, and Azure production traces.

## 中文摘要

FPGA 提供了可编程、高能效且计算密集的加速基底；因此，一方面，它们为优化云环境中的无服务器负载提供了极具吸引力的方案。另一方面，FPGA 也带来了与云中无服务器模型直接相悖的重大挑战，包括其低层且复杂的编程 API、缺乏虚拟化与隔离机制、重配置与通信开销高，以及缺少编排机制。为此，我们提出 F3，首个能够高效、安全地利用 FPGA 加速无服务器函数的系统。F3 使无服务器函数能够轻松将任务卸载到 FPGA，而无需操心底层设备管理。系统自动部署并调用 FPGA 加速函数，同时提供隔离、高吞吐与低延迟。为实现这些设计目标，F3 通过高层、硬件无关的 API 简化了 FPGA 初始化的复杂性，借助基于 unikernel 的 FPGA 虚拟化实现函数隔离，通过每节点 FPGA 资源管理器减少冷启动与通信开销，并以 FPGA 感知的编排器最大化 FPGA 利用率。我们基于一个实用的无服务器框架实现了 F3 的开源原型，该框架由 OpenFaaS、Kubernetes 和 containerd 组成，遵循云编排引擎的 CRI/OCI 行业标准。我们的评估表明，在真实应用负载、微基准和 Azure 生产轨迹上，延迟显著降低、吞吐显著提升。

## 英文关键词

FPGA, hardware acceleration, serverless computing

## 中文关键词

FPGA，硬件加速，无服务器计算

---

[← 返回 Session 5 — Clouds and FaaS](index.md)
