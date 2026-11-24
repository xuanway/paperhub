---
title: "StreamGrid: Streaming Point Cloud Analytics via Compulsory Splitting and Deterministic Termination"
description: "ASPLOS 2025 · Session 3B · StreamGrid：通过强制切分与确定性终止实现流式点云分析"
tags:
  - "ASPLOS2025"
  - "Session 3B"
  - "Graphics"
---

# StreamGrid: Streaming Point Cloud Analytics via Compulsory Splitting and Deterministic Termination

**中文标题：** StreamGrid：通过强制切分与确定性终止实现流式点云分析

**所属 Session：** [Session 3B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Yu Feng (Shanghai Jiao Tong University,Shanghai Qi Zhi Institute), Zheng Liu (Shanghai Jiao Tong University), Weikai Lin (University of Rochester), Zihan Liu (Shanghai Jiao Tong University,Shanghai Qi Zhi Institute), Jingwen Leng (Shanghai Jiao Tong University,Shanghai Qi Zhi Institute), Minyi Guo (Shanghai Jiaotong University,Shanghai Qi Zhi Institute), Zhezhi He (Shanghai Jiao Tong University), Jieru Zhao (Shanghai Jiao Tong University), Yuhao Zhu (University of Rochester)

**单位：** Shanghai Jiao Tong University,Shanghai Qi Zhi Institute；Shanghai Jiao Tong University；University of Rochester；Shanghai Jiaotong University,Shanghai Qi Zhi Institute

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716021) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Point clouds are increasingly important in intelligent applications, but frequent off-chip memory traffic in accelerators causes pipeline stalls and leads to high energy consumption. While conventional line buffer techniques can eliminate offchip traffic, they cannot be directly applied to point clouds due to their inherent computation patterns. To address this, we introduce two techniques: compulsory splitting and deterministic termination, enabling fully-streaming processing. We further propose StreamGrid, a framework that integrates these techniques and automatically optimizes on-chip buffer sizes. Our evaluation shows StreamGrid reduces onchip memory by 61.3% and energy consumption by 40.5% with marginal accuracy loss compared to the baselines without our techniques. Additionally, we achieve 10.0× speedup and 3.9× energy efficiency over state-of-the-art accelerators.

## 中文摘要

点云在智能应用中日益重要，但加速器中频繁的片外内存访问会造成流水线停顿并导致高能耗。传统的行缓冲（line buffer）技术虽然能够消除片外访问，但由于点云固有的计算模式，这些技术无法直接应用于点云。为解决这一问题，我们引入两项技术：强制切分（compulsory splitting）与确定性终止（deterministic termination），从而实现全流式处理。我们进一步提出 StreamGrid，这是一个集成上述技术并自动优化片上缓冲区大小的框架。评估表明，与未采用本文技术的基线相比，StreamGrid 在仅有微小精度损失的情况下将片上内存减少 61.3%、能耗降低 40.5%。此外，相较于最先进的加速器，我们实现了 10.0× 的加速比和 3.9× 的能效提升。

## 英文关键词

Hardware Accelerator, Streaming Architecture, Line Buffer, Point Cloud Analytics

## 中文关键词

硬件加速器；流式架构；行缓冲；点云分析

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716021)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 3B](index.md) · [返回 ASPLOS 2025](../index.md)
