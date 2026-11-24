---
title: "GFS: A Preemption-aware Scheduling Framework for GPU Clusters with Predictive Spot Instance Management"
description: "ASPLOS 2026 · Session 2C · GFS：面向 GPU 集群的抢占感知调度框架，具备预测性竞价实例管理"
tags:
  - "ASPLOS2026"
  - "Session 2C"
  - "GPU Systems & Scheduling"
---

# GFS: A Preemption-aware Scheduling Framework for GPU Clusters with Predictive Spot Instance Management

**中文标题：** GFS：面向 GPU 集群的抢占感知调度框架，具备预测性竞价实例管理

**所属 Session：** [Session 2C](index.md) · [ASPLOS 2026](../index.md)

**作者：** Jiaang Duan (Shanghai Jiao Tong University), Shenglin Xu (Shanghai Jiao Tong University), Shiyou Qian (Shanghai Jiao Tong University), Dingyu Yang (Zhejiang University), Kangjin Wang (Alibaba Group), Chenzhi Liao (Alibaba Group), Yinghao Yu (Alibaba Group), Qin Hua (Shanghai Jiao Tong Univeristy), Hanwen Hu (Shanghai Jiao Tong University), Qi Wang (Alibaba Group), Wenchao Wu (Alibaba Group), Dongqing Bao (Alibaba Group), Tianyu Lu (Alibaba Group), Jian Cao (Shanghai Jiao Tong University), Guangtao Xue (Shanghai Jiao Tong University), Guodong Yang (Alibaba Group), Liping Zhang (Alibaba Group), Gang Chen (Zhejiang University)

**单位：** Shanghai Jiao Tong University；Zhejiang University；Alibaba Group；Shanghai Jiao Tong Univeristy

**来源：** ASPLOS 2026 · Volume 1 · [论文 DOI](https://doi.org/10.1145/3760250.3762231) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

The surge in large language models (LLMs) has fundamentally reshaped the landscape of GPU usage patterns, creating an urgent need for more efficient management strategies. While cloud providers employ spot instances to reduce costs for low-priority (LP) tasks, existing schedulers still grapple with high eviction rates and lengthy queuing times. To address these limitations, we present GFS, a novel preemptive scheduling framework that enhances service-level objective (SLO) compliance for high-priority (HP) tasks while minimizing preemptions to LP tasks. Firstly, GFS utilizes a lightweight forecasting model that predicts GPU demand among different tenants, enabling proactive resource management. Secondly, GFS employs a dynamic allocation mechanism to adjust the spot quota for LP tasks with guaranteed durations. Lastly, GFS incorporates a preemptive scheduling policy that prioritizes HP tasks while minimizing the impact on LP tasks. We demonstrate the effectiveness of GFS through both realworld implementation and simulations. The results show that GFS reduces eviction rates by 33.0%, and cuts queuing delays by 44.1% for LP tasks. Furthermore, GFS enhances the GPU allocation rate by up to 22.8% in real production clusters. In a production cluster of more than 10,000 GPUs, GFS yields roughly $459,715 in monthly benefits.

## 中文摘要

大语言模型（LLM）的激增从根本上重塑了 GPU 使用模式的格局，催生出对更高效管理策略的迫切需求。尽管云提供商采用竞价实例来降低低优先级（LP）任务的成本，现有调度器仍在艰难应对高驱逐率与漫长的排队时间。为解决这些局限，我们提出 GFS，一种新颖的抢占式调度框架，它提升高优先级（HP）任务对服务等级目标（SLO）的达成度，同时将对 LP 任务的抢占降至最低。首先，GFS 使用一个轻量级预测模型来预测不同租户之间的 GPU 需求，从而实现主动的资源管理。其次，GFS 采用动态分配机制，为具有时长保证的 LP 任务调整竞价配额。最后，GFS 引入一种抢占式调度策略，优先处理 HP 任务，同时尽量减小对 LP 任务的影响。我们通过真实系统实现与仿真验证了 GFS 的有效性。结果表明，GFS 将驱逐率降低了 33.0%，并将 LP 任务的排队延迟削减了 44.1%。此外，GFS 在真实生产集群中将 GPU 分配率最多提升了 22.8%。在超过 10,000 块 GPU 的生产集群中，GFS 每月带来约 $459,715 的收益。

## 英文关键词

Spot instance; forecasting model; preemptive scheduling

## 中文关键词

竞价实例；预测模型；抢占式调度

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3760250.3762231)
- [ASPLOS 2026 · Volume 1 论文集](https://doi.org/10.1145/3760250)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 2C](index.md) · [返回 ASPLOS 2026](../index.md)
