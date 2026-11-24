---
title: "Pegasus: Transparent and Unified Kernel-Bypass Networking for Fast Local and Remote Communication"
description: "EuroSys 2025 · Distributed Systems · Dinglan Peng (Purdue University), Congyu Liu (Purdue University), Tapti Palit (P"
tags:
  - "EuroSys2025"
  - "Distributed Systems"
---

# Pegasus: Transparent and Unified Kernel-Bypass Networking for Fast Local and Remote Communication

**中文标题：** 面向快速本地和远程通信的透明统一内核旁路网络

**所属 Session：** [Session 3.1: Distributed Systems](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Distributed Systems。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Distributed Systems</p>
</div>

**作者**：Dinglan Peng (Purdue University), Congyu Liu (Purdue University), Tapti Palit (Purdue University), Anjo Vahldiek-Oberwagner (Intel Labs), Mona Vij (Intel Labs), Pedro Fonseca (Purdue University)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3696083)

## 英文摘要

Modern software architectures in cloud computing are highly reliant on interconnected local and remote services. Popular architectures, such as the service mesh, rely on the use of independent services or sidecars for a single application. While such modular approaches simplify application development and deployment, they also introduce significant communication overhead since now even local communication that is handled by the kernel becomes a performance bottleneck. This problem has been identified and partially solved for remote communication over fast NICs through the use of kernel-bypass data plane systems. However, existing kernel-bypass mechanisms challenge their practical deployment by either requiring code modification or supporting only a small subset of the network interface.

In this paper, we propose Pegasus, a framework for transparent kernel bypass for local and remote communication. By transparently fusing multiple applications into a single process, Pegasus provides an in-process fast path to bypass the kernel for local communication. To accelerate remote communication over fast NICs, Pegasus uses DPDK to directly access the NIC. Pegasus supports transparent kernel bypass for unmodified binaries by implementing core OS services in user space, such as scheduling and memory management, thus removing the kernel from the critical path. Our experiments on a range of real-world applications show that, compared with Linux, Pegasus improves the throughput by 19% to 33% for local communication and 178% to 442% for remote communication, without application changes. Furthermore, Pegasus achieves 222% higher throughput than Linux for co-located, IO-intensive applications that require both local and remote communication, with each communication optimization contributing significantly.

## 中文摘要

云计算中的现代软件架构高度依赖互联的本地与远程服务。诸如服务网格之类的流行架构，依赖为单个应用使用独立服务或边车。这类模块化方法虽然简化了应用的开发与部署，却也引入了显著的通信开销，因为如今连由内核处理的本地通信都成了性能瓶颈。对于经由高速网卡的远程通信，这一问题已被识别，并通过内核旁路数据面系统得到部分解决。然而，现有的内核旁路机制要么需要修改代码，要么只支持一小部分网络接口，使其实际部署面临挑战。

本文提出 Pegasus，一个面向本地与远程通信的透明内核旁路框架。Pegasus 通过将多个应用透明地融合进单个进程，为本地通信提供绕过内核的进程内快速路径。为经由高速网卡加速远程通信，Pegasus 使用 DPDK 直接访问网卡。Pegasus 通过在用户空间实现调度和内存管理等核心操作系统服务，为未经修改的二进制程序提供透明内核旁路，从而将内核移出关键路径。我们在多种真实应用上的实验表明，与 Linux 相比，Pegasus 在无需修改应用的情况下将本地通信吞吐提升 19% 至 33%，将远程通信吞吐提升 178% 至 442%。此外，对于同时需要本地和远程通信的同机 IO 密集型应用，Pegasus 的吞吐比 Linux 高出 222%，且每一项通信优化都有显著贡献。

**英文关键词：** operating systems, kernel-bypass networking

**中文关键词：** 操作系统、内核旁路网络

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
