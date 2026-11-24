---
title: "Toasty: Speeding up network I/O with cache-warm buffers"
description: "ASPLOS 2026 · Session 5D · Toasty：使用缓存预热缓冲区加速网络 I/O"
tags:
  - "ASPLOS2026"
  - "Session 5D"
  - "Storage & Caching"
---

# Toasty: Speeding up network I/O with cache-warm buffers

**中文标题：** Toasty：使用缓存预热缓冲区加速网络 I/O

**所属 Session：** [Session 5D](index.md) · [ASPLOS 2026](../index.md)

**作者：** Preeti Preeti (IIT Bombay), Nitish Bhat (IIT Bombay), Ashwin Kumar (IIT Bombay), Mythili Vutukuru (Indian Institute of Technology, Bombay)

**单位：** IIT Bombay；Indian Institute of Technology, Bombay

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790235) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

Modern NICs DMA packets directly to the LLC using technologies like DDIO, reducing access latencies for networking applications. Prior work has observed several performance issues with DDIO when the working set of packet buffers does not fit into LLC. For example, the leaky DMA problem arises when incoming packets evict older packets that have not yet been processed by the application from LLC, causing them to be fetched again from main memory. While using a smaller pool of packet buffers that fits in cache is an obvious solution, this may result in the NIC running out of buffers to DMA packets into when a burst of packets arrives. This paper proposes Toasty, a system that mitigates this tradeoff between high throughput and resilience to packet loss that arises when sizing the network packet buffer pool. While prior work has proposed hardware-based solutions to this problem, Toasty is a software-only solution that can be deployed on commodity NIC hardware. Toasty manages the packet buffer pool as a LIFO stack instead of a FIFO queue, and adapts the number of buffers populated into the NIC hardware RX ring based on incoming packet load and application processing rate. Together, these changes enable Toasty to recirculate a small working set of cache-warm buffers in steady state, while falling back to a larger pool of buffers during traffic bursts. We implement Toasty over the AF_XDP kernel bypass framework, and our evaluation shows that Toasty improves network throughput for a variety of network functions by up to 78% over the default buffer pool implementation of AF_XDP. We also show that Toasty matches the performance of a small buffer pool that fits in cache, while being more resilient to traffic bursts.

## 中文摘要

现代 NIC 使用 DDIO 等技术将数据包直接 DMA 到 LLC，从而降低网络应用的访问延迟。先前工作已经观察到，当数据包缓冲区的工作集无法放入 LLC 时，DDIO 会出现若干性能问题。例如，当到达的数据包将尚未被应用处理的较早数据包从 LLC 中驱逐出去时，就会出现泄漏 DMA 问题，导致这些数据包需要再次从主存中取回。虽然使用能够放入缓存的较小数据包缓冲区池是一个显而易见的解决方案，但这可能导致在数据包突发到达时 NIC 没有缓冲区可用于 DMA 数据包。本文提出 Toasty，一个缓解这一权衡的系统，该权衡在确定网络数据包缓冲区池大小时出现，即高吞吐量与丢包韧性之间的权衡。虽然先前工作已提出针对该问题的基于硬件的解决方案，但 Toasty 是一种纯软件解决方案，可部署在商用 NIC 硬件上。Toasty 将数据包缓冲区池作为 LIFO 栈而非 FIFO 队列来管理，并根据到达的数据包负载和应用处理速率，调整填充到 NIC 硬件 RX 环中的缓冲区数量。这些改动共同使 Toasty 在稳态下循环使用一个小的缓存预热缓冲区工作集，同时在流量突发期间回退到更大的缓冲区池。我们在 AF_XDP 内核旁路框架之上实现了 Toasty，评估表明，相比 AF_XDP 默认的缓冲区池实现，Toasty 将多种网络功能的网络吞吐量最多提升了 78%。我们还表明，Toasty 达到了可放入缓存的较小缓冲区池的性能，同时对流量突发更具韧性。

## 英文关键词

Host Network; Network I/O; Cache Efficiency; AF_XDP; DDIO

## 中文关键词

主机网络；网络 I/O；缓存效率；AF_XDP；DDIO

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790235)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 5D](index.md) · [返回 ASPLOS 2026](../index.md)
