---
title: "STRAW: Stress-Aware WL-Based Read Disturbance Management for High-Density NAND Flash Memory"
description: "ASPLOS 2026 · Session 2D · STRAW：面向高密度 NAND 闪存的压力感知、基于字线的读干扰管理"
tags:
  - "ASPLOS2026"
  - "Session 2D"
  - "DRAM Reliability & Security"
---

# STRAW: Stress-Aware WL-Based Read Disturbance Management for High-Density NAND Flash Memory

**中文标题：** STRAW：面向高密度 NAND 闪存的压力感知、基于字线的读干扰管理

**所属 Session：** [Session 2D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Myoungjun Chun (Soongsil University), Jaeyong Lee (Seoul National University), Inhyuk Choi (Seoul National University), Jisung Park (POSTECH (Pohang University of Science and Technology)), Myungsuk Kim (Kyungpook National University), Jihong Kim (Seoul National University)

**单位：** Soongsil University；Seoul National University；POSTECH (Pohang University of Science and Technology)；Kyungpook National University

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790228) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

While NAND flash memory has continuously increased its storage density over decades, this progress has exacerbated the read-disturbance problem. In this work, we identify two fundamental limitations of existing read-disturbance management techniques that trigger read reclaim (RR) at the block granularity: (i) they overlook the heterogeneous reliability impact of read disturbance across individual wordlines (WLs), leading to unnecessary RR in many cases; and (ii) they address read disturbance only after disturbance-induced errors have already accumulated, which forces substantial RR-induced copy overheads in read-disturbance-prone modern NAND flash memory. To address these limitations, we propose STRAW (STRess-Aware Wordline-based read-disturbance management), a new technique that minimizes RR overheads through two key ideas: (i) stress-aware WL-based read reclaim, which monitors the accumulated read-disturbance effect on each WL and reclaims only heavily disturbed WLs, and (ii) stress-reduced read, which mitigates disturbance on valid WLs during each read operation by scaling pass-through voltages based on WL validity. Our experimental results using a modern SSD emulator show that STRAW reduces RR-induced page-copy overhead by 88.6% on average compared with the state-of-the-art technique.

## 中文摘要

尽管 NAND 闪存在过去几十年中持续提升存储密度，但这一进展也加剧了读干扰问题。在本工作中，我们指出现有以块为粒度触发读回收（read reclaim，RR）的读干扰管理技术存在两个根本性局限：(i) 它们忽略了读干扰对不同字线（wordline，WL）可靠性影响的差异性，导致在许多情况下进行不必要的 RR；(ii) 它们仅在干扰引发的错误已经累积之后才处理读干扰，这迫使易受读干扰影响的现代 NAND 闪存承受大量由 RR 引起的拷贝开销。为解决这些局限，我们提出 STRAW（STRess-Aware Wordline-based read-disturbance management，压力感知的基于字线读干扰管理），这是一种通过两个关键思路最小化 RR 开销的新技术：(i) 压力感知的基于 WL 的读回收，它监控每条 WL 上累积的读干扰效应，并且只回收受干扰严重的 WL；以及(ii) 降低应力的读操作，它在每次读操作期间根据 WL 的有效性调整通过电压，从而减轻对有效 WL 的干扰。我们使用现代 SSD 模拟器的实验结果表明，与现有先进技术相比，STRAW 平均将 RR 引起的页拷贝开销降低了 88.6%。

## 英文关键词

solid-state drives (SSDs), NAND flash memory, read disturbance, read reclaim, SSD lifetime, I/O performance

## 中文关键词

固态硬盘（SSDs）；NAND 闪存；读干扰；读回收；SSD 寿命；I/O 性能

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790228)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 2D](index.md) · [返回 ASPLOS 2026](../index.md)
