---
title: "SGDRC: Software-Defined Dynamic Resource Control for Concurrent DNN Inference on NVIDIA GPUs"
description: "PPoPP 2025 Session 7（Scheduling and Resource Management）：软件定义显存带宽与 SM 动态分配，平均 SLO 达成率 99%"
tags:
  - "PPoPP2025"
  - "Session-7"
  - "Scheduling and Resource Management"
  - "GPU Sharing"
  - "Resource Management"
  - "DNN Inference"
authors:
  - "Yongkang Zhang"
  - "Haoxuan Yu"
  - "Chenxia Han"
  - "Cheng Wang"
  - "Baotong Lu"
  - "Yunzhe Li"
  - "Zhifeng Jiang"
  - "Yang Li"
  - "Xiaowen Chu"
  - "Huaicheng Li"
session: "Session 7: Scheduling and Resource Management"
session_number: 7
session_chair: "Jie Ren"
date: "2025-03-04"
time: "11:20–11:40"
room: "Acacia D"
doi: "10.1145/3710848.3710863"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# SGDRC: Software-Defined Dynamic Resource Control for Concurrent DNN Inference on NVIDIA GPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 SGDRC，一个完全软件定义的 GPU 显存带宽与计算单元动态管理方案，通过逆向工程显存通道哈希映射并配合 cache coloring，在并发 DNN 推理下兼顾 SLO 与吞吐。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 7: Scheduling and Resource Management</p>
</div>

**作者**：Yongkang Zhang, Haoxuan Yu (HKUST); Chenxia Han (CUHK); Cheng Wang (Alibaba Group); Baotong Lu (Microsoft Research); Yunzhe Li (Shanghai Jiao Tong University); Zhifeng Jiang (HKUST); Yang Li (China University of Geosciences); Xiaowen Chu (HKUST (GZ)); Huaicheng Li (Virginia Tech)

**会议**：PPoPP 2025 · 2025 年 3 月 4 日 11:20–11:40 · Session 7: Scheduling and Resource Management（主席：Jie Ren）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710863) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 提出 SGDRC，一个完全软件定义的 GPU 显存带宽与计算单元动态管理方案，通过逆向工程显存通道哈希映射并配合 cache coloring，在并发 DNN 推理下兼顾 SLO 与吞吐。

## 研究问题

云厂商把高优先级时延敏感（LS）与低优先级尽力而为（BE）的 DNN 推理混部在同一 GPU 上，但 GPU 原生资源管理或依赖特定硬件、或无法动态分配；NVIDIA 也未暴露显存带宽分配接口，使已有工作只能采用保守共享策略或仅适用于少数型号的静态划分。

## 方法简述

- 逆向工程揭示 NVIDIA GPU 通用的 VRAM 通道哈希映射架构，并用软件级 cache coloring 消除通道冲突。
- 采用 bimodal tensors 与 tidal SM masking 动态分配显存带宽和计算单元。
- 基于离线 profiling 指导资源分配决策。

## 主要结果

- 在两块 NVIDIA GPU、11 个主流 DNN 的真实负载上，平均 SLO 达成率达到 99.0%。
- 相比 SOTA GPU 共享方案，整体吞吐最高提升 1.47×，BE 作业吞吐最高提升 2.36×。

<details>
<summary>原文摘要（英文）</summary>

Cloud service providers heavily colocate high-priority, latency-sensitive (LS), and low-priority, best-effort (BE) DNN inference services on the same GPU to improve resource utilization in data centers. Among the critical shared GPU resources, there has been very limited analysis on the dynamic allocation of compute units and VRAM bandwidth, mainly for two reasons: (1) The native GPU resource management solutions are either hardware-specific, or unable to dynamically allocate resources to different tenants, or both; (2) NVIDIA doesn’t expose interfaces for VRAM bandwidth allocation, and the software stack and VRAM channel architectures are black-box, both of which limit the software-level resource management. These drive prior work to design either conservative sharing policies detrimental to throughput, or static resource partitioning only applicable to a few GPU models. To bridge this gap, this paper proposes SGDRC, a fully software-defined dynamic VRAM bandwidth and compute unit management solution for concurrent DNN inference services. SGDRC aims at guaranteeing service quality, maximizing the overall throughput, and providing general applicability to NVIDIA GPUs. SGDRC first reveals a general VRAM channel hash mapping architecture of NVIDIA GPUs through comprehensive reverse engineering and eliminates VRAM channel conflicts using software-level cache coloring. SGDRC applies bimodal tensors and tidal SM masking to dynamically allocate VRAM bandwidth and compute units, and guides the allocation of resources based on offline profiling. We evaluate 11 mainstream DNNs with real-world workloads on two NVIDIA GPUs. The results show that compared with the state-of-the-art GPU sharing solutions, SGDRC achieves the highest SLO attainment rates (99.0% on average), and improves overall throughput by up to 1.47× and BE job throughput by up to 2.36×.

</details>

---

> 所属 Session：[Session 7: Scheduling and Resource Management](index.md) · 返回 [PPoPP 2025 总览](../index.md)
