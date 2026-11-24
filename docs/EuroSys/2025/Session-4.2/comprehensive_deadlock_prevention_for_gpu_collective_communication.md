---
title: "Comprehensive Deadlock Prevention for GPU Collective Communication"
description: "EuroSys 2025 · GPU Systems · LiChen Pan (School of Computer Science, Peking University), Juncheng Liu (OneFlo"
tags:
  - "EuroSys2025"
  - "GPU Systems"
---

# Comprehensive Deadlock Prevention for GPU Collective Communication

**中文标题：** GPU 集合通信的全面死锁预防

**所属 Session：** [Session 4.2: GPU Systems](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：GPU Systems。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · GPU Systems</p>
</div>

**作者**：LiChen Pan (School of Computer Science, Peking University), Juncheng Liu (OneFlow Inc.), Yongquan Fu (Science and Technology Laboratory of Parallel and Distributed Processing; College of Computer, National University of Defense Technology, Changsha, Hunan province, China), Jinhui Yuan (OneFlow Inc.), Rongkai Zhang (None), PengZe Li (School of Computer Science, Peking University), Zhen Xiao (School of Computer Science, Peking University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717466)

## 英文摘要

Distributed deep neural network training necessitates efficient GPU collective communications, which are inherently susceptible to deadlocks. GPU collective deadlocks arise easily in distributed deep learning applications when multiple collectives circularly wait for each other. GPU collective deadlocks pose a significant challenge to the correct functioning and efficiency of distributed deep learning, and no general effective solutions are currently available. Only in specific scenarios, ad-hoc methods, making an application invoke collectives in a consistent order across GPUs, can be used to prevent circular collective dependency and deadlocks.

This paper presents DFCCL, a novel GPU collective communication library that provides a comprehensive approach for GPU collective deadlock prevention while maintaining high performance. DFCCL achieves preemption for GPU collectives at the bottom library level, effectively preventing deadlocks even if applications cause circular collective dependency. DFCCL ensures high performance with its execution and scheduling methods for collectives. Experiments show that DFCCL effectively prevents GPU collective deadlocks in various situations. Moreover, extensive evaluations demonstrate that DFCCL delivers performance comparable to or superior to NCCL, the state-of-the-art collective communication library highly optimized for NVIDIA GPUs.

## 中文摘要

分布式深度神经网络训练需要高效的 GPU 集合通信，而这类通信本身容易发生死锁。在分布式深度学习应用中，当多个集合通信相互循环等待时，GPU 集合死锁很容易出现。GPU 集合死锁对分布式深度学习的正确运行和效率构成重大挑战，目前尚无通用有效的解决方案。仅在特定场景下，可以采用临时性方法——要求应用在各 GPU 上以一致的顺序调用集合通信——来预防循环的集合依赖和死锁。

本文提出 DFCCL，一个新颖的 GPU 集合通信库，它提供了一种全面的 GPU 集合死锁预防方法，同时保持高性能。DFCCL 在库的底层实现了 GPU 集合通信的抢占，即使应用造成循环的集合依赖也能有效预防死锁。DFCCL 通过对集合通信的执行与调度方法保证高性能。实验表明，DFCCL 在多种情形下都能有效预防 GPU 集合死锁。此外，大量评估表明，DFCCL 的性能与 NCCL 相当或更优；NCCL 是当前针对 NVIDIA GPU 高度优化的最先进集合通信库。

**英文关键词：** Collective Communication, GPU, Deadlock Prevention, Preemption

**中文关键词：** 集合通信、GPU、死锁预防、抢占

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
