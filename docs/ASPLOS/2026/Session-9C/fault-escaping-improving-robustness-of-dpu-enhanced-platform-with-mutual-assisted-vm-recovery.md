---
title: "Fault Escaping: Improving Robustness of DPU Enhanced Platform with Mutual Assisted VM Recovery"
description: "ASPLOS 2026 · Session 9C · Fault Escaping：借助互助式虚拟机恢复提升 DPU 增强平台的鲁棒性"
tags:
  - "ASPLOS2026"
  - "Session 9C"
  - "Reliability & Fault Tolerance"
---

# Fault Escaping: Improving Robustness of DPU Enhanced Platform with Mutual Assisted VM Recovery

**中文标题：** Fault Escaping：借助互助式虚拟机恢复提升 DPU 增强平台的鲁棒性

**所属 Session：** [Session 9C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Chao Zhang (Alibaba Group), Tao Xu (Alibaba Group), Junming Liu (Alibaba Group), Pai Liu (Alibaba Group), Zhilang Xu (Alibaba Group), Kang Yan (Alibaba Group), Shuo Shi (Shanghai Jiao Tong University), Jintao Li (Alibaba Group), Jinhu Li (Alibaba Group), Chen Liang (Alibaba Cloud), Wenhui kevin (Intel Corporation), FeiFei Fan (Intel Corporation), Yibin Shen (Alibaba Cloud), Hang Yang (Alibaba Cloud), Jianming Song (Alibaba Group), Xudong Zheng (Alibaba Group), Jiesheng Wu (Alibaba Group), Jian Li (Shanghai Jiao Tong University)

**单位：** Alibaba Group；Shanghai Jiao Tong University；Alibaba Cloud；Intel Corporation

**来源：** ASPLOS 2025 · Volume 3 · [论文 DOI](https://doi.org/10.1145/3676642.3736124) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Modern cloud servers achieve significant performance improvements by exploiting data processing units (DPUs) to offload virtualization overhead. Unlike traditional monolithic hypervisors, this offloading approach splits VM state and distributes hypervisor functions across the DPU and the Host, transforming the cloud server from a single system into a sophisticated orchestration of multiple self-managed processing units. However, the failure rate of these systems has significantly increased, as errors from either the DPU or the Host can crash the entire machine. All these changes necessitate a comprehensive revamp of current VM fault tolerance and isolation mechanisms. This paper explores a novel approach to VM fault tolerance by treating the split hypervisors on the DPU SoC and the Host as redundant peers. We propose a fault-escaping scheme that enables VMs to escape from a failing SoC or Host. With hybrid synchronization, the entire VM state becomes fully accessible on either the SoC or the Host with minimum synchronization overhead (in kilobytes). Instead of recovering the failed hypervisor, this scheme migrates the verified VM state, allowing the VM to escape from the failure and resume on a new machine. The evaluation demonstrates that the escape-based mechanism introduces no runtime performance overhead, achieves performance levels comparable to VM live migration, and reduces the VM recovery time objective (RTO) by 4× to 14× in one of the largest cloud production environments.

## 中文摘要

现代云服务器通过利用数据处理单元（DPU）卸载虚拟化开销，取得了显著的性能提升。与传统单体 hypervisor 不同，这种卸载方式将 VM 状态拆分，并把 hypervisor 功能分布到 DPU 与 Host 上，使云服务器从单一系统转变为由多个自管理处理单元构成的复杂编排。然而，这些系统的故障率显著上升，因为来自 DPU 或 Host 的错误都可能使整台机器崩溃。所有这些变化都要求对现有的 VM 容错与隔离机制进行全面改造。本文探索了一种新颖的 VM 容错方法：将 DPU SoC 与 Host 上的分裂 hypervisor 视为冗余对等体。我们提出一种故障逃逸（fault-escaping）方案，使 VM 能够从发生故障的 SoC 或 Host 中逃逸。借助混合同步，整个 VM 状态可在 SoC 或 Host 任一侧完全访问，且同步开销极小（以千字节计）。该方案不恢复发生故障的 hypervisor，而是迁移经过校验的 VM 状态，使 VM 得以从故障中逃逸并在新机器上恢复运行。评估表明，基于逃逸的机制不引入任何运行时性能开销，达到与 VM 在线迁移相当的性能水平，并在最大的云生产环境之一中将 VM 恢复时间目标（RTO）降低 4× 到 14×。

## 英文关键词

data processing unit; virtualization; fault tolerance; fault recovery; cloud computing; robustness

## 中文关键词

数据处理单元；虚拟化；容错；故障恢复；云计算；鲁棒性

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676642.3736124)
- [ASPLOS 2025 · Volume 3 论文集](https://doi.org/10.1145/3676642)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

## 来源说明

该文发表于 **ASPLOS 2025 Volume 3**，并列入 **ASPLOS 2026** 的宣讲日程。本目录按宣讲 Session 收录；引用时请使用上述 DOI 对应的出版信息。

原始摘要整理记录：

> **来源说明**：该文收录于 ASPLOS '25（第 30 届）论文集 Volume 3（`ASPLOS2025-Proceedings-volume3.pdf`），在 ASPLOS 2026 Program 中作为宣讲论文列出；本地 ASPLOS 2026 两卷论文集（Volume 1/2）未收录。

[返回 Session 9C](index.md) · [返回 ASPLOS 2026](../index.md)
