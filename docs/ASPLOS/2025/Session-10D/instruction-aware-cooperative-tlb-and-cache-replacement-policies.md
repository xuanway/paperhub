---
title: "Instruction-Aware Cooperative TLB and Cache Replacement Policies"
description: "ASPLOS 2025 · Session 10D · 指令感知的 TLB 与缓存协同替换策略"
tags:
  - "ASPLOS2025"
  - "Session 10D"
  - "Memory Management"
---

# Instruction-Aware Cooperative TLB and Cache Replacement Policies

**中文标题：** 指令感知的 TLB 与缓存协同替换策略

**所属 Session：** [Session 10D](index.md) · [ASPLOS 2025](../index.md)

**作者：** Dimitrios Chasapis (Barcelona Supercomputing Center (BSC)), Georgios Vavouliotis (Unaffiliated), Daniel A. Jiménez (Texas A&M University), Marc Casas (Barcelona Supercomputing Center (BSC),Universitat Politècnica de Catalunya (UPC))

**单位：** BSC；Unaffiliated；Texas A&M University；UPC

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707247) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Modern server and data center applications are characterized not only by large datasets, but also by large instruction footprints that incur frequent cache and Translation Lookaside Buffer (TLB) misses due to instruction accesses. Instruction TLB misses are particularly problematic as they cause pipeline stalls that significantly harm performance. This paper proposes cooperative last-level TLB (STLB) and L2 cache (L2C) replacement policies targeting workloads with large instruction footprints. We propose Instruction Translation Prioritization (iTP), an STLB replacement policy that maximizes the number of instruction hits in the STLB at the expense of increasing data page walks. To compensate for the increase in data page walks, we propose extended Page Table Prioritization (xPTP), a new L2C replacement policy that amplifies the benefits of iTP by effectively reducing L2C misses due to data page walks. Our proposal, iTP+xPTP, combines iTP at STLB and xPTP at L2C. iTP+xPTP employs an adaptive mechanism that switches between xPTP and LRU policies at L2C based on the pressure placed on the virtual memory subsystem. Our proposal, iTP+xPTP, improves single-core geometric mean performance by 18.9% over a baseline that uses the LRU replacement policy at both STLB and L2C across a set of contemporary server workloads. Under SMT co-location, the corresponding performance uplift is 11.4%. Finally, we show that iTP+xPTP outperforms the state-of-the-art STLB and cache replacement policies.

## 中文摘要

现代服务器与数据中心应用的特征不仅在于数据集庞大，还在于指令足迹巨大，这会因指令访问而引发频繁的缓存与转译后备缓冲器（TLB）缺失。指令 TLB 缺失尤其成问题，因为它们会造成流水线停顿，从而显著损害性能。本文提出面向大指令足迹工作负载的末级 TLB（STLB）与 L2 缓存（L2C）协同替换策略。我们提出指令转换优先（Instruction Translation Prioritization，iTP），这是一种 STLB 替换策略，以增加数据页表遍历为代价，最大化 STLB 中的指令命中次数。为补偿数据页表遍历的增加，我们提出扩展页表优先（extended Page Table Prioritization，xPTP），这是一种新的 L2C 替换策略，通过有效减少因数据页表遍历造成的 L2C 缺失来放大 iTP 的收益。我们提出的方案 iTP+xPTP 将 STLB 上的 iTP 与 L2C 上的 xPTP 相结合。iTP+xPTP 采用自适应机制，根据虚拟内存子系统承受的压力在 L2C 上于 xPTP 与 LRU 策略之间切换。在一组当代服务器工作负载上，与在 STLB 和 L2C 均使用 LRU 替换策略的基线相比，我们提出的 iTP+xPTP 将单核几何平均性能提升 18.9%。在 SMT 协同部署下，相应的性能提升为 11.4%。最后，我们表明 iTP+xPTP 优于当前最先进的 STLB 与缓存替换策略。

## 英文关键词

virtual memory, address translation, translation lookaside buffer, TLB management, replacement policy

## 中文关键词

虚拟内存；地址转换；转译后备缓冲器；TLB 管理；替换策略

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707247)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 10D](index.md) · [返回 ASPLOS 2025](../index.md)
