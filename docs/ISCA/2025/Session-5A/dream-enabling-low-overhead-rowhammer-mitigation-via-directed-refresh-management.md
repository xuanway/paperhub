---
title: "DREAM: Enabling Low-Overhead Rowhammer Mitigation via Directed Refresh Management"
description: "ISCA 2025 · Session 5A · DREAM: 基于定向刷新管理的低开销Rowhammer缓解"
tags:
  - "ISCA2025"
  - "Session 5A"
  - "RowHammer"
---

# DREAM: Enabling Low-Overhead Rowhammer Mitigation via Directed Refresh Management

**中文标题：** DREAM: 基于定向刷新管理的低开销Rowhammer缓解

**所属 Session：** [Session 5A](index.md) · [ISCA 2025](../index.md)

**作者：** Hritvik Taneja, Moin Qureshi

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731117) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

This paper focuses on Memory-Controller (MC) side Rowhammer mitigation. MC-side mitigation consists of two parts: First, a tracker to identify the aggressor rows. Second, a command to let the MC inform the DRAM chip to perform victim-refresh for the specified aggressor row. To facilitate this, prior works assumed a per-bank Nearby Row Refresh (NRR) command. However, JEDEC standards did not support NRR. Instead, JEDEC introduced Directed Refresh Management (DRFM), which can simultaneously perform mitiga- tions for one row each in 8 (DRFMsb) or 32 (DRFMab) banks. As DRFM stalls 8-32 banks, it incurs high overheads. For example, at a threshold of 2K, PARA incurs a slowdown of 3.9% with NRR, 12.7% with DRFMsb, and 49% with DRFMab. Although counter-based trackers can avoid these slowdowns, they require significant storage. The goal of our paper is to reduce the performance and storage overheads of MC-based mitigations by using properties of DRFM. 

Our paper proposes DREAM, DRFM-Aware Rowhammer Mit- igation. We propose two variants of DREAM. Our first design, DREAM-R, reduces the performance overhead of randomized trackers by increasing the time between sampling the row and issuing a DRFM. The delay allows other banks the time to sample their own rows, thereby increasing the number of rows mitigated under a single DRFM. DREAM-R reduces the average performance over- head of PARA from 12.7% (DRFMsb) to 4.24% and MINT from 15.9% (DRFMsb) to 2.1%. We bound the impact of delayed DRFM on the tolerated Rowhammer threshold. Our second design DREAM-C, reduces the storage for counter-based trackers by leveraging the fact that DRFM can concurrently mitigate several rows. DREAM-C forms a gang containing 32-256 rows, randomly selected equally from all the 32 banks, and allocates a single counter for the entire gang. DREAM-C reduces the storage required at a threshold of 500 to only 1KB/bank, which is 8x lower than Graphene while avoiding the complexity of CAM lookups and incurring negligible slowdown. We also show that DREAM compares favorably to PRAC.

## 中文摘要

本文聚焦内存控制器（MC）侧的行锤（Rowhammer）防护方案。控制器侧防护包含两部分：一是追踪器，识别攻击行；二是命令，由控制器通知DRAM芯片，对指定攻击行执行受害行刷新。为实现该机制，以往研究假设存在按存储体的近邻行刷新（NRR）命令，但JEDEC标准并不支持NRR，而是引入了定向刷新管理（DRFM）：DRFMsb可以同时对8个存储体各选一行执行防护，DRFMab则支持32个存储体。但DRFM会阻塞8–32个存储体，开销很大。例如阈值设为2000时，基线PARA在NRR下减速3.9%，DRFMsb下减速12.7%，DRFMab下高达49%。基于计数器的追踪器虽然可以缓解减速，但存储开销巨大。本文目标是利用DRFM本身特性，降低控制器侧防护的性能与存储开销。

本文提出DREAM，一种感知DRFM的行锤防护方案，包含两个变体：
第一种DREAM-R：拉长行采样与下发DRFM命令之间的间隔，降低随机追踪器的性能开销。该延迟给其他存储体留出采样时间，让一次DRFM可以同时防护更多行。DREAM-R把PARA在DRFMsb下的平均开销从12.7%降到4.24%，MINT从15.9%降到2.1%；同时约束延迟下发DRFM对行锤容忍阈值带来的影响。 第二种DREAM-C：利用DRFM可以并行防护多行的特点，减少计数器追踪器的存储。DREAM-C构建行组，每组包含32–256行，从全部32个存储体中等概率随机选取，整个行组只分配一个计数器。阈值500时，DREAM-C存储开销仅 1KB/存储体，相比Graphene降低8倍，无需CAM查表，复杂度低，减速几乎可以忽略。
本文同时对比表明DREAM相比PRAC具备优势。

## 英文关键词

DRAM, Rowhammer, Security, DRFM

## 中文关键词

动态随机存取存储器（DRAM）, 行锤攻击（Rowhammer）, 安全, DRFM

## 代码与研究制品

- [代码仓库](https://github.com/hritwik567/dream-ae)
- [研究制品](https://doi.org/10.5281/zenodo.15299886)

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731117)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 5A](index.md) · [返回 ISCA 2025](../index.md)
