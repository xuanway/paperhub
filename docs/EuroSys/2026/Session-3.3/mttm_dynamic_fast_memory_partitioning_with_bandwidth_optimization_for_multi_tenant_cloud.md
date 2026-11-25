---
title: "MTTM: Dynamic Fast Memory Partitioning with Bandwidth Optimization for Multi-tenant Cloud"
description: "EuroSys 2026 · Cloud & Serverless Resource Management · Changjun Lee (KAIST), Sangjin Choi (KAIST), Youngjin Kwon (KAIST)"
tags:
  - "EuroSys2026"
  - "Cloud & Serverless Resource Management"
---

# MTTM: Dynamic Fast Memory Partitioning with Bandwidth Optimization for Multi-tenant Cloud

**中文标题：** MTTM：面向多租户云的带宽优化动态快速内存划分

**所属 Session：** [Session 3.3: Cloud & Serverless Resource Management](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Cloud & Serverless Resource Management。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Cloud & Serverless Resource Management</p>
</div>

**作者**：Changjun Lee (KAIST), Sangjin Choi (KAIST), Youngjin Kwon (KAIST)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769371)

## 英文摘要

Memory tiering, which extends local DRAM by incorporating remote DRAM or NVM via Compute Express Link (CXL), offers a promising solution to the DRAM capacity scaling problem. However, in multi-tenant cloud environments, efficient management of fast memory requires not only optimizing data movement across tiers but also effectively distributing DRAM capacity when tenants compete. Moreover, bandwidth utilization is critically impacted by memory request rejection, which depends on the distribution of local DRAM. While previous research has extensively addressed data movement, DRAM distribution among multiple tenants remains underexplored.

This work tackles the challenges of local DRAM distribution and efficient bandwidth utilization in multi-tenant cloud environments. We propose MTTM, a tiered memory system that implements DRAM-sensitivity-based memory partitioning strategy, allocates fast memory based on workload characteristics, and dynamically adjusts local DRAM allocation to mitigate memory request rejection. Implemented in Linux v5.15, MTTM is evaluated on nine cloud workloads, demonstrating clear performance improvements over state-of-the-art baselines across various workload mixes, memory configuration, and remote memory access latencies.

## 中文摘要

内存分层通过Compute Express Link（CXL）引入远端DRAM或NVM来扩展本地DRAM，为DRAM容量扩展问题提供了一种有前景的解决方案。然而，在多租户云环境中，高效管理快速内存不仅需要优化跨层的数据移动，还需要在租户竞争时有效地分配DRAM容量。此外，带宽利用率受到内存请求拒绝的严重影响，而请求拒绝又取决于本地DRAM的分布。尽管已有研究广泛探讨了数据移动问题，多租户之间的DRAM分配仍研究不足。

本工作应对多租户云环境中本地DRAM分配与高效带宽利用的挑战。我们提出MTTM，一个分层内存系统，它实现基于DRAM敏感度的内存划分策略，根据工作负载特征分配快速内存，并动态调整本地DRAM分配以缓解内存请求拒绝。MTTM在Linux v5.15中实现，并在九种云工作负载上进行了评估，在多种工作负载组合、内存配置和远端内存访问延迟下，相比最先进的基线展现出明显的性能提升。

**英文关键词：** Tiered memory, Multi tenants, Fast memory partitioning

**中文关键词：** 分层内存、多租户、快速内存划分

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
