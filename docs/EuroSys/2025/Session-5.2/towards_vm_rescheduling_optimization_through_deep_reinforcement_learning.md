---
title: "Towards VM Rescheduling Optimization Through Deep Reinforcement Learning"
description: "EuroSys 2025 · Virtualization · Xianzhong Ding (University of California, Merced), Yunkai Zhang (University of C"
tags:
  - "EuroSys2025"
  - "Virtualization"
---

# Towards VM Rescheduling Optimization Through Deep Reinforcement Learning

**中文标题：** 通过深度强化学习优化虚拟机重新调度

**所属 Session：** [Session 5.2: Virtualization](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Virtualization。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Virtualization</p>
</div>

**作者**：Xianzhong Ding (University of California, Merced), Yunkai Zhang (University of California, Berkeley), Binbin Chen (ByteDance), Donghao Ying (UC Berkeley), Tieying Zhang (ByteDance), Jianjun Chen (Bytedance), Lei Zhang (ByteDance), Alberto Cerpa (University of California, Merced), Wan Du (University of California Merced)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717476)

## 英文摘要

Modern industry-scale data centers need to manage a large number of virtual machines (VMs). Due to the continual creation and release of VMs, many small resource fragments are scattered across physical machines (PMs). To handle these fragments, data centers periodically reschedule some VMs to alternative PMs, a practice commonly referred to as VM rescheduling. Despite the increasing importance of VM rescheduling as data centers grow in size, the problem remains understudied. We first show that, unlike most combinatorial optimization tasks, the inference time of VM rescheduling algorithms significantly influences their performance, due to dynamic VM state changes during this period. This causes existing methods to scale poorly. Therefore, we develop a reinforcement learning system for VM rescheduling, VMR2L, which incorporates a set of customized techniques, such as a two-stage framework that accommodates diverse constraints and workload conditions, a feature extraction module that captures relational information specific to rescheduling, as well as a risk-seeking evaluation enabling users to optimize the trade-off between latency and accuracy. We conduct extensive experiments with data from an industry-scale data center. Our results show that VMR2L can achieve a performance comparable to the optimal solution but with a running time of seconds. Code12 and datasets3 are open-sourced.

## 中文摘要

现代工业规模的数据中心需要管理大量虚拟机（VM）。由于 VM 的持续创建与释放，许多小的资源碎片散布在物理机（PM）上。为处理这些碎片，数据中心会周期性地将一些 VM 重新调度到其他 PM，这种做法通常称为 VM 重调度。尽管随着数据中心规模增长 VM 重调度日益重要，该问题仍研究不足。我们首先表明，与大多数组合优化任务不同，VM 重调度算法的推理时间会显著影响其性能，因为在此期间 VM 状态会发生动态变化。这导致现有方法扩展性差。因此，我们开发了一个用于 VM 重调度的强化学习系统 VMR2L，它融合了一系列定制技术，例如可适应多样约束和工作负载条件的两阶段框架、能够捕捉重调度特有的关系信息的特征提取模块，以及使用户能够优化延迟与精度之间权衡的风险寻求式评估。我们使用来自工业规模数据中心的数据进行了大量实验。结果表明，VMR2L 可以达到与最优解相当的性能，但运行时间仅为数秒。代码¹² 与数据集³ 已开源。

**英文关键词：** Cloud Computing, Virtual Machine Rescheduling, Reinforcement Learning, Resource Management

**中文关键词：** 云计算、虚拟机重调度、强化学习、资源管理

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
