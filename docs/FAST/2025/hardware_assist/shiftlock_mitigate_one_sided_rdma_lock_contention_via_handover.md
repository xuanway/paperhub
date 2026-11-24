---
title: "ShiftLock: Mitigate One-sided RDMA Lock Contention via Handover"
description: "FAST 2025 · Hardware Assist · 让 RDMA 客户端直接移交锁而不重试，有效吞吐最高提升 3.62 倍"
tags:
  - "FAST2025"
  - "Hardware Assist"
  - "RDMA"
  - "distributed lock"
  - "杰出工件奖"
---

# ShiftLock: Mitigate One-sided RDMA Lock Contention via Handover

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">一侧 RDMA 锁在高竞争下让所有客户端都向锁服务器重试，吃光服务器 RNIC 的入站 IOPS，有效吞吐大幅下滑。ShiftLock 借 MCS 的接力思路实现客户端间直接移交，微基准有效吞吐最高提升 3.62 倍、尾延迟降低 76.6%，事务吞吐最高提升 2.85 倍。</p>
<p class="paper-seo-summary__tags">FAST 2025 · Hardware Assist · 杰出工件奖</p>
</div>

**中文标题**：ShiftLock：通过锁移交缓解单边 RDMA 锁竞争

**USENIX 页面**：[https://www.usenix.org/conference/fast25/presentation/gao](https://www.usenix.org/conference/fast25/presentation/gao)

**论文 PDF**：[fast25-gao.pdf](https://www.usenix.org/system/files/fast25-gao.pdf)

**作者**：Jian Gao、Qing Wang、Jiwu Shu（Tsinghua University）

**会议**：FAST 2025 · Santa Clara, CA · 第 355–372 页 · **杰出工件奖**

**Session**：Hardware Assist · 2025-02-26 10:50–12:30 · Chair：Kiran Kumar Muniswamy Reddy（Amazon）

**所属 Session**：[Hardware Assist](index.md) · [FAST 2025](../index.md)

**关键词**：RDMA, distributed lock, lock handover, MCS lock, reader-writer lock, contention

---

## 英文摘要

Lock is a basic building block of distributed storage systems. With the extensive deployment of the Remote Direct Memory Access (RDMA) network, RDMA lock has been brought into increasing focus since it can leverage RDMA one-sided verbs to acquire and release locks, achieving high performance without any intervention of server-side CPUs. However, existing RDMA locks are suboptimal under high contention, mainly because clients are likely to fail to acquire a locked lock and must retry. Excessive retries incur high latencies for clients and decrease the overall goodput as they devour the lock server's network inbound IOPS resources.

The MCS lock inspired us that instead of contending, clients can coordinate with each other by directly handing over locks; thus, they can wait locally without retrying. We present ShiftLock, an RDMA lock supporting lock handover among arbitrary clients. At its core is a non-blocking direct client-to-client coordination mechanism with CPU efficiency, scalability, and fault tolerance, realized with proper software design and exertion of RDMA features. Based on it, ShiftLock employs a crafted protocol with reader-writer semantics, starvation-freedom, and low latency or high goodput under low or high contention. Compared to existing locks, ShiftLock improves goodput by up to 3.62× and reduces tail latencies by up to 76.6% in microbenchmarks, respectively, while also improving transaction goodput by up to 2.85×.

## 中文摘要

锁是分布式存储系统的基本构件。随着远程直接内存访问（RDMA）网络的广泛部署，RDMA 锁日益受到关注，因为它可以利用 RDMA 单边动词获取与释放锁，无需服务器端 CPU 介入即可实现高性能。然而，现有 RDMA 锁在高竞争下表现欠佳，主要原因是客户端很可能无法获取已被占用的锁而必须重试。过度重试给客户端带来高延迟，并因消耗锁服务器的网络入站 IOPS 资源而降低整体有效吞吐。受 MCS 锁启发，客户端可以不争抢，而是通过直接移交锁来相互协调，从而在本地等待而无需重试。本文提出 ShiftLock——一种支持任意客户端之间移交的 RDMA 锁。其核心是一种非阻塞、直接的客户端到客户端协调机制，具备 CPU 高效、可扩展与容错的特点，并通过恰当的软件设计与对 RDMA 特性的运用实现。基于该机制，ShiftLock 采用一套精心设计的协议，具备读写语义、无饥饿，并在低竞争下保持低延迟、高竞争下保持高有效吞吐。与现有锁相比，ShiftLock 在微基准中分别把有效吞吐最高提升 3.62 倍、把尾延迟最高降低 76.6%，同时把事务有效吞吐最高提升 2.85 倍。

## 一句话总结

> 竞争不该表现为重试，而该表现为排队：持锁者把锁直接递给下一个客户端，等待者只在本机等一条通知。

## 研究背景与问题

- **服务器 CPU 成为瓶颈**：分布式锁是存储系统的基础件，传统锁管理器靠服务器 CPU 授予与撤销锁，高并发下一次锁请求要几十到几百微秒。
- **RDMA 锁的适用边界**：用一侧 verbs 直接改服务器上的锁项，可绕过服务器 CPU，网络 RTT 可低至 2µs 以内；但在低竞争下才顺滑，因为所有客户端流量都指向同一台锁服务器，形成 N 对 1 的格局。
- **重试的量化代价**：240 个客户端争一把 CAS 锁时，相比无重试的理想情况，有效吞吐从 278.3 Kops/s 掉到 15.5 Kops/s（下降 94.4%），服务器收到的 CAS 请求里有 99.4% 是重试。
- **退避只是概率性缓解**：换上 SMART 的截断指数退避后有效吞吐为 141.4 Kops/s，虽比无退避好 9.1 倍，仍比理想情况差 49.2%，且仍有 87.1% 的 CAS 是重试。

## 核心贡献

- **把锁移交引入分布式环境**：持锁客户端不经解锁，直接把所有权交给下一个客户端，等待者本地等待移交通知，而不是反复向锁项发起 RDMA 重试。
- **非阻塞且 CPU 高效的客户端间协调**：用双侧 RDMA 的 Send/Recv 完成客户端间通信，既避开 RPC 的阻塞与常驻服务线程，也比 Write 省掉锁项里必须维护的地址与 RKey 元数据。
- **基于动态连接的任意客户端互通**：采用 RDMA 动态连接，在不需要维护全网状可靠连接、也不做显式连接管理的前提下，让任意两个客户端之间建立可靠通信。
- **无饥饿的读写语义**：在 MCS 队列之上实现读写锁，且不必维护当前锁模式，低竞争下仍保证单次网络往返完成获取与释放。
- **客户端与服务器协同的容错**：在客户端故障时仍能正确恢复锁的所有权，不因队列断裂而永久卡死。

## 方法与技术要点

- **总体结构**：锁项存放在锁服务器上，客户端用一侧 RDMA 访问锁项，用双侧 RDMA 在彼此之间传递锁所有权；写者以 MCS 队列排队，读者单独组织，两者之间主动转移所有权。
- **入队与等待**：以队列尾指针作为锁项，客户端用扩展原子操作（FAA/CAS）把自己挂到队尾并把自己的地址写进前驱的本地指针，然后在本机轮询自己的标志位。
- **移交路径**：释放时若没有后继就把队尾置空，否则直接把后继的标志置真/发出通知，锁所有权不经过锁项、也不产生对锁项的争用。
- **避免读者饥饿**：在读者与写者之间主动交接所有权，并限制单个写者最多连续持有 N 次，实验取 N=16 时有效吞吐与延迟的平衡最好。
- **容错细节**：等待锁释放超时即判定客户端故障并启动恢复；超时阈值取 3×Tlease。向已故障客户端发消息会收到 RNR 错误并使 DCI 状态转为 error，此时需重置并重新拉起该 QP。

## 评估与主要结果

- **平台**：至少 6 台 Linux 服务器、InfiniBand RDMA 网络、Mellanox ConnectX-5 或更新的网卡；对比对象为现有 RDMA 锁，微基准用 240 个客户端争用同一把锁。
- **微基准**：相比现有锁，高竞争下有效吞吐最高提升 3.62 倍，尾延迟最高降低 76.6%。
- **事务负载**：在 TATP 与 TPC-C 上事务吞吐最高提升 2.85 倍，延迟相当或更低。
- **应用与故障**：银行应用场景中优于 RedLock；与唯一支持故障恢复的基线 DSLR 相比，ShiftLock 同样能恢复，但有效吞吐更低，原因是其超时为 3×Tlease 而 DSLR 为 2×Tlease，且需重建处于 error 状态的 QP；即便如此仍与 DSLR 处于同一数量级。

## 代码与研究制品

- [代码仓库](https://github.com/thustorage/shiftlock)

[返回 Hardware Assist](index.md) · [返回 FAST 2025](../index.md)
