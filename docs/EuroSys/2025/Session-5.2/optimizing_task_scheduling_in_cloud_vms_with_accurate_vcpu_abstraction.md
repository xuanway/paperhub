---
title: "Optimizing Task Scheduling in Cloud VMs with Accurate vCPU Abstraction"
description: "EuroSys 2025 · Virtualization · Edward Guo (Hofstra University), Weiwei Jia (The University of Rhode Island), Xi"
tags:
  - "EuroSys2025"
  - "Virtualization"
---

# Optimizing Task Scheduling in Cloud VMs with Accurate vCPU Abstraction

**中文标题：** 通过精确的虚拟 CPU 抽象优化云虚拟机任务调度

**所属 Session：** [Session 5.2: Virtualization](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Virtualization。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Virtualization</p>
</div>

**作者**：Edward Guo (Hofstra University), Weiwei Jia (The University of Rhode Island), Xiaoning Ding (New Jersey Institute of Technology), Jianchen Shan (Hofstra University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696092)

## 英文摘要

The paper shows that task scheduling in Cloud VMs hasn’t evolved quickly to handle the dynamic vCPU resources. The existing vCPU abstraction cannot accurately depict the vCPU dynamics in capacity, activity, and topology, and these mismatches can mislead the scheduler, causing performance degradation and system anomalies. The paper proposes a novel solution, vSched, which probes accurate vCPU abstraction through a set of lightweight microbenchmarks (vProbers) without modifying the hypervisor, and leverages the probed information to optimize task scheduling in cloud VMs with three new techniques: biased vCPU selection, intra-VM harvesting, and relaxed work conservation. Our evaluation of vSched’s implementation in x86 Linux Kernel demonstrates that it can effectively improve both system throughput and workload latency across various VM types in the dynamic multi-cloud environment.

## 中文摘要

本文表明，云虚拟机中的任务调度尚未快速演进以应对动态的 vCPU 资源。现有的 vCPU 抽象无法准确刻画 vCPU 在容量、活跃度和拓扑方面的动态性，这些失配会误导调度器，导致性能下降和系统异常。本文提出一种新方案 vSched，它通过一组轻量级微基准测试（vProbers）在不修改 hypervisor 的情况下探测准确的 vCPU 抽象，并利用探测到的信息，借助三项新技术优化云虚拟机中的任务调度：偏置的 vCPU 选择、VM 内收割以及松弛的工作守恒。我们在 x86 Linux 内核中对 vSched 实现的评估表明，它能在动态的多云环境中跨多种 VM 类型有效提升系统吞吐量和负载延迟。

**英文关键词：** Task Scheduling, Virtualization, Cloud Computing, Resource Probing, Operating Systems

**中文关键词：** 任务调度、虚拟化、云计算、资源探测、操作系统

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
