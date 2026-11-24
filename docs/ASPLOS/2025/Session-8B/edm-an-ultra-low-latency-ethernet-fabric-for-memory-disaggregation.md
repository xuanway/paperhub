---
title: "EDM: An Ultra-Low Latency Ethernet Fabric for Memory Disaggregation"
description: "ASPLOS 2025 · Session 8B · EDM：面向内存解耦的超低时延以太网互联架构"
tags:
  - "ASPLOS2025"
  - "Session 8B"
  - "Networking"
---

# EDM: An Ultra-Low Latency Ethernet Fabric for Memory Disaggregation

**中文标题：** EDM：面向内存解耦的超低时延以太网互联架构

**所属 Session：** [Session 8B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Weigao Su (Purdue University), Vishal Shrivastav (Purdue University)

**单位：** Purdue University

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3669940.3707221) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

Achieving low remote memory access latency remains the primary challenge in realizing memory disaggregation over Ethernet within the datacenters. We present EDM that attempts to overcome this challenge using two key ideas. First, while existing network protocols for remote memory access over the Ethernet, such as TCP/IP and RDMA, are implemented on top of the MAC layer, EDM takes a radical approach by implementing the entire network protocol stack for remote memory access within the Physical layer (PHY) of the Ethernet. This overcomes fundamental latency and bandwidth overheads imposed by the MAC layer, especially for small memory messages. Second, EDM implements a centralized, fast, in-network scheduler for memory traffic within the PHY of the Ethernet switch. Inspired by the classic Parallel Iterative Matching (PIM) algorithm, the scheduler dynamically reserves bandwidth between compute and memory nodes by creating virtual circuits in the PHY, thus eliminating queuing delay and layer 2 packet processing delay at the switch for memory traffic, while maintaining high bandwidth utilization. Our FPGA testbed demonstrates that EDM's network fabric incurs a latency of only ∼300 ns for remote memory access in an unloaded network, which is an order of magnitude lower than state-of-the-art Ethernet-based solutions such as RoCEv2 and comparable to emerging PCIe-based solutions such as CXL. Larger-scale network simulations indicate that even at high network loads, EDM's average latency remains within 1.3× its unloaded latency.

## 中文摘要

在数据中心内实现基于以太网的内存解耦，其首要挑战仍然是降低远程内存访问时延。我们提出 EDM，尝试用两个关键思路来克服这一挑战。首先，现有的以太网远程内存访问网络协议（如 TCP/IP 和 RDMA）都实现在 MAC 层之上，而 EDM 采用了一种激进的做法——将以太网远程内存访问的整个网络协议栈实现在以太网的物理层（PHY）之内。这克服了 MAC 层带来的根本性时延与带宽开销，对小的内存消息尤其如此。其次，EDM 在以太网交换机的 PHY 内实现了一个集中式、快速的网内调度器来处理内存流量。受经典的并行迭代匹配（PIM）算法启发，该调度器通过在 PHY 中建立虚拟电路，在计算节点与内存节点之间动态预留带宽，从而为内存流量消除交换机处的排队时延与二层数据包处理时延，同时保持高带宽利用率。我们的 FPGA 测试平台表明，在空载网络中，EDM 的网络互联结构对远程内存访问仅产生约 300 ns 的时延，比 RoCEv2 等最先进的基于以太网的方案低一个数量级，并与 CXL 等新兴的基于 PCIe 的方案相当。更大规模的网络仿真表明，即使在高网络负载下，EDM 的平均时延仍保持在其空载时延的 1.3 倍以内。

## 英文关键词

Memory Disaggregation; In-Network Scheduler; Ethernet PHY

## 中文关键词

内存解耦；网内调度器；以太网 PHY

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3669940.3707221)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 8B](index.md) · [返回 ASPLOS 2025](../index.md)
