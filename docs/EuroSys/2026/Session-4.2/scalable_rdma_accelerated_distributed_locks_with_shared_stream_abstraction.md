---
title: "Scalable RDMA-accelerated Distributed Locks with Shared Stream Abstraction"
description: "EuroSys 2026 · Distributed Consensus, Blockchain & Storage · Miao Cai (Nanjing University of Aeronautics and Astronautics), Junru Shen (Hohai"
tags:
  - "EuroSys2026"
  - "Distributed Consensus, Blockchain & Storage"
---

# Scalable RDMA-accelerated Distributed Locks with Shared Stream Abstraction

**中文标题：** 基于共享流抽象的可扩展RDMA加速分布式锁

**所属 Session：** [Session 4.2: Distributed Consensus, Blockchain & Storage](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Distributed Consensus, Blockchain & Storage。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Distributed Consensus, Blockchain & Storage</p>
</div>

**作者**：Miao Cai (Nanjing University of Aeronautics and Astronautics), Junru Shen (Hohai University), Xiaojian Liao (Beihang University), Rong Gu (State Key Laboratory for Novel Software Technology, Nanjing University), Yanchao Zhao (Nanjing University of Aeronautics and Astronautics), Hao Han (Nanjing University of Aeronautics and Astronautics), Bing Chen (Nanjing University of Aeronautics and Astronautics), Baoliu Ye (State Key Laboratory for Novel Software Technology, Nanjing University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803598)

## 英文摘要

Blazing fast RDMA technology revolutionizes modern distributed systems and propels them to offload performance-critical data paths onto this network fabric. Designing an RDMA-optimized data path needs to clear a main hurdle— non-scalable distributed locks. Through a performance dissection of existing lock schemes, we find that software-based lock request ordering and polling-based lock ownership transfer scale poorly, leading to high NIC contention and heavy network congestion. To resolve these bottlenecks, this paper proposes StreamLock, a scalable lock primitive that co-designs the distributed lock protocol with fast RDMA networks. The core of StreamLock is a novel shared stream abstraction with two mechanisms: (i) scalable request ordering by repurposing the line-speed packet receiving provided by modern NICs; (ii) peer-to-peer notification to achieve one-round-trip-time lock ownership transfer. We implement StreamLock with off-the-shelf RDMA NICs and compare it with state-of-the-art distributed locks. Comprehensive experimental results showcase that StreamLock outperforms them significantly.

## 中文摘要

极速的RDMA技术革新了现代分布式系统，推动其将性能关键的数据路径卸载到这一网络架构上。设计RDMA优化的数据路径需要克服一个主要障碍——不可扩展的分布式锁。通过对现有锁方案进行性能剖析，我们发现基于软件的锁请求排序和基于轮询的锁所有权转移可扩展性很差，导致严重的NIC争用和沉重的网络拥塞。为解决这些瓶颈，本文提出StreamLock，一种将分布式锁协议与高速RDMA网络协同设计的可扩展锁原语。StreamLock的核心是一种新颖的共享流抽象，包含两种机制：(i) 复用现代NIC提供的线速数据包接收能力，实现可扩展的请求排序；(ii) 通过对等通知实现单次往返时延的锁所有权转移。我们使用现成的RDMA NIC实现StreamLock，并将其与最先进的分布式锁进行比较。全面的实验结果表明，StreamLock显著优于这些方案。

**英文关键词：** Distributed System, RDMA network, Concurrency Control

**中文关键词：** 分布式系统、RDMA网络、并发控制

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
