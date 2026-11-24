---
title: "PCcheck: Persistent Concurrent Checkpointing for ML"
description: "ASPLOS 2025 · Session 6A · PCcheck：面向机器学习的持久化并发检查点机制"
tags:
  - "ASPLOS2025"
  - "Session 6A"
  - "ML Systems 2"
---

# PCcheck: Persistent Concurrent Checkpointing for ML

**中文标题：** PCcheck：面向机器学习的持久化并发检查点机制

**所属 Session：** [Session 6A](index.md) · [ASPLOS 2025](../index.md)

**作者：** Foteini Strati (ETH Zurich), Michal Friedman (ETH Zurich), Ana Klimovic (ETH Zurich)

**单位：** ETH Zurich

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707255) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Training large-scale machine learning (ML) models is expensive and time-intensive, consuming many hardware accelerators for days or weeks. As the scale of hardware deployments and training time continue to grow, the probability of failures also increases. The desire to use cheaper cloud resources, such as spot VMs, to lower costs also dramatically increases the frequency of failures. The standard approach to deal with failures is to periodically pause training and checkpoint model parameters to persistent storage. Unfortunately, today's checkpointing mechanisms introduce high overhead when applied at high frequencies, yet frequent checkpointing is necessary to avoid long recovery times. We present a concurrent checkpointing mechanism, PCcheck, that allows frequent checkpointing with minimal overhead. Our framework supports persisting checkpoints to SSD and persistent main memory (PMEM) for both singlemachine and distributed settings. PCcheck enables checkpointing as frequently as every 10 iterations for detailed monitoring and fast recovery times in case of failures, while maintaining minimal (3%) overhead on training throughput.

## 中文摘要

训练大规模机器学习（ML）模型代价高昂且耗时，需要占用大量硬件加速器数天乃至数周。随着硬件部署规模与训练时长的持续增长，发生故障的概率也随之上升。为降低成本而希望使用更廉价的云资源（例如竞价型虚拟机），同样大幅提高了故障发生的频率。应对故障的标准做法是定期暂停训练，并将模型参数检查点写入持久化存储。遗憾的是，当今的检查点机制在高频率使用时会引入高开销，然而要避免漫长的恢复时间又必须进行频繁的检查点。我们提出一种并发检查点机制 PCcheck，它能够以极小的开销实现频繁的检查点。我们的框架支持将检查点持久化到 SSD 和持久化主存（PMEM），适用于单机与分布式两种场景。PCcheck 可以实现每 10 次迭代一次的检查点频率，从而支持细粒度监控，并在发生故障时快速恢复，同时对训练吞吐仅保持极小的（3%）开销。

## 英文关键词

Fault Tolerant Training

## 中文关键词

容错训练

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707255)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 6A](index.md) · [返回 ASPLOS 2025](../index.md)
