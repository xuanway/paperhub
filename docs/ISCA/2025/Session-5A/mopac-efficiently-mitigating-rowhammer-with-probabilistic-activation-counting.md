---
title: "MoPAC: Efficiently Mitigating Rowhammer with Probabilistic Activation Counting"
description: "ISCA 2025 · Session 5A · MoPAC: 基于概率激活计数的高效Rowhammer缓解"
tags:
  - "ISCA2025"
  - "Session 5A"
  - "RowHammer"
---

# MoPAC: Efficiently Mitigating Rowhammer with Probabilistic Activation Counting

**中文标题：** MoPAC: 基于概率激活计数的高效Rowhammer缓解

**所属 Session：** [Session 5A](index.md) · [ISCA 2025](../index.md)

**作者：** Suhas Vittal, Salman Qazi, Poulami Das, Moin Qureshi

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3730997) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

Rowhammer has worsened over the last decade. Existing in-DRAM solutions, such as TRR, were broken with simple patterns. In re- sponse, the recent DDR5 JEDEC standards modify the DRAM array to enable Per-Row Activation Counters (PRAC) for tracking aggressor rows. They also extend the DRAM timings to support the opera- tions required to update the PRAC counters. Unfortunately, the in- creased memory timings cause significant performance overheads (on average 10%) even for benign applications and even at current Rowhammer thresholds. The goal of this paper is to minimize the slowdown of PRAC while retaining the security benefits of PRAC. This paper proposes Mitigating Rowhammer with Probabilistic Activation Counts (MoPAC), which reduces the slowdown of updat- ing the PRAC counters by performing the updates probabilistically, thereby incurring the latency overhead of counter updates for only a small subset of activations. To ensure security in the presence of probabilistic counters, MOPAC adjusts the threshold at which the row undergoes mitigation. We propose two variants of MoPAC: MoPAC-C (Memory-Controller Side) and MoPAC-D (DRAM Side). MoPAC-C relies on having two types of precharge commands: one that incurs normal latency and does not do counter updates, and the other that incurs higher latency and performs counter updates. MoPAC-C probabilistically chooses when the longer precharge must be used to perform update of the PRAC counter. MoPAC-D is a completely in-DRAM solution that probabilistically selects which activations will be selected for performing counter updates and obtains the time required for counter-updates using ALERT or REF. Our evaluations show that, for a Rowhammer threshold of 500 (10× lower than current thresholds), MoPAC-C and MoPAC-D incur an average slowdown of only 1.7% and 0.7%, much less than the 10% incurred by PRAC. MoPAC removes one of the major obstacles to the commercial adoption of PRAC.

## 中文摘要

行锤漏洞（Rowhammer）在过去十年愈发严重。现有的DRAM内置防护方案（例如TRR）已经被简单访问模式攻破。为此，新版DDR5 JEDEC标准改造DRAM阵列，引入逐行激活计数器（PRAC）来追踪攻击行；同时拉长DRAM时序，支撑PRAC计数器更新操作。但拉长的内存时序会带来显著性能开销：即便对于无害程序、在当前Rowhammer阈值下，平均减速也高达10%。本文目标是在保留PRAC安全防护能力的前提下，尽可能降低性能损失。

本文提出MoPAC（Mitigating Rowhammer with Probabilistic Activation Counts），基于概率化更新计数器来降低PRAC更新带来的减速，仅对一小部分激活操作执行计数器更新。为保证概率化计数器下的安全性，MoPAC动态调整触发防护的阈值。MoPAC包含两种实现：MoPAC-C（内存控制器侧）与MoPAC-D（DRAM芯片侧）。
MoPAC-C支持两种预充电命令：一种是常规延迟、不更新计数器；另一种延迟更高、执行计数器更新。MoPAC-C概率性选择何时使用高延迟预充电，完成PRAC计数更新。
MoPAC-D是完全在DRAM内部实现的方案，概率挑选部分激活操作执行计数更新，并借助ALERT或REF信号获取计数器更新所需时间。

评测结果表明，在Rowhammer阈值设为500（比现有阈值低一个数量级）时，MoPAC-C、MoPAC-D平均减速仅1.7%、0.7%，远低于PRAC基线的10%。MoPAC消除了PRAC走向商用的一大阻碍。

## 英文关键词

DRAM, Rowhammer, Security, PRAC, ABO

## 中文关键词

动态随机存取存储器（DRAM）, 行锤攻击（Rowhammer）, 安全, PRAC, 地址位翻转（ABO）

## 代码与研究制品

- [研究制品](https://zenodo.org/records/15103420)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3730997)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 5A](index.md) · [返回 ISCA 2025](../index.md)
