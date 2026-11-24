---
title: "CETOFS: A High-Performance File System with Host-Server Collaboration for Remote Storage"
description: "FAST 2026 · Integrity · 第 659–674 页"
tags:
  - "FAST2026"
  - "Integrity"
---

# CETOFS: A High-Performance File System with Host-Server Collaboration for Remote Storage

**中文标题**：CETOFS：面向远程存储、主机—服务器协同的高性能文件系统

**Session**：Integrity · 2026-02-26 14:00–15:20 · Chair：Gala Yadgar（Technion—Israel Institute of Technology）

**作者**：Wenqing Jia, Dejun Jiang, and Jin Xiong, State Key Lab of Processors, Institute of Computing Technology, Chinese Academy of Sciences; and University of Chinese Academy of Sciences

**会议**：FAST 2026 · Santa Clara, CA · 第 659–674 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/jia](https://www.usenix.org/conference/fast26/presentation/jia)

**论文 PDF**：[fast26-jia.pdf](https://www.usenix.org/system/files/fast26-jia.pdf)

---

## 英文摘要

With the development of high-performance RDMA network and modern storage devices, disaggregated NVMe SSDs have become increasingly popular due to the high resource utilization and superior performance. Although existing kernel file systems (e.g., Ext4) can directly access the disaggregated SSD via the NVMe-over-RDMA protocol, the data path suffers from heavy kernel stack overhead and thus degraded performance. The extra networking latency introduced in accessing remote storage also prevents file system from achieving scalable concurrent accesses and efficient failure-atomic IO. In this paper, we present CETOFS, a high-performance file system with host-server collaboration for disaggregated NVMe SSD. CETOFS designs a userspace-kernel collaborative architecture to place data plane entirely in userspace meanwhile separate permission checking from in-kernel control plane. Then CETOFS exploits the processing capability of remote storage server to offload three tasks: permission checking, concurrency control, and failure-atomic IO guaranteeing. The offloading mechanisms greatly reduce the networking overhead. We implement CETOFS and evaluate it against both kernel and userspace file systems. The evaluation shows CETOFS achieves high-performance data path that reduces latency by up to 52% for single-threaded file access and improves throughput by up to 19X for concurrent accesses.

## 中文摘要

随着高性能 RDMA 网络和现代存储设备的发展，分离式 NVMe SSD 因其高资源利用率和优越性能而日益流行。尽管现有内核文件系统（例如 Ext4）可以通过 NVMe-over-RDMA 协议直接访问分离式 SSD，但其数据路径受制于沉重的内核栈开销，从而导致性能下降。访问远程存储所引入的额外网络延迟，也使文件系统无法实现可扩展的并发访问和高效的故障原子 I/O。本文提出 CETOFS，一个面向分离式 NVMe SSD、采用主机—服务器协同的高性能文件系统。CETOFS 设计了一种用户态—内核协同架构，将数据平面完全放在用户态，同时将权限检查与内核内控制平面分离。随后，CETOFS 利用远程存储服务器的处理能力来卸载三项任务：权限检查、并发控制和故障原子 I/O 保证。这些卸载机制大幅降低了网络开销。我们实现了 CETOFS，并与内核文件系统和用户态文件系统进行了对比评估。评估表明，CETOFS 实现了高性能数据路径，将单线程文件访问延迟最多降低 52%，并将并发访问吞吐量最多提升 19 倍。
