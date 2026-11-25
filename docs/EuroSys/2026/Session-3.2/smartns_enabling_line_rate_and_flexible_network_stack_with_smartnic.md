---
title: "SmartNS: Enabling Line-rate and Flexible Network Stack with SmartNIC"
description: "EuroSys 2026 · Datacenter Network Fabrics & RDMA · Xuzheng Chen (Zhejiang University), Jie Zhang (Zhejiang University), Baolin Zhu "
tags:
  - "EuroSys2026"
  - "Datacenter Network Fabrics & RDMA"
---

# SmartNS: Enabling Line-rate and Flexible Network Stack with SmartNIC

**中文标题：** SmartNS：基于 SmartNIC 实现线速且灵活的网络栈

**所属 Session：** [Session 3.2: Datacenter Network Fabrics & RDMA](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Datacenter Network Fabrics & RDMA。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Datacenter Network Fabrics & RDMA</p>
</div>

**作者**：Xuzheng Chen (Zhejiang University), Jie Zhang (Zhejiang University), Baolin Zhu (Zhejiang University), Xueying Zhu (Zhejiang University), Zhongqing Chen (Alibaba Cloud), Ting Fu (Alibaba Group), Shu Ma (Alibaba Group), Lingjun Zhu (Alibaba Group), Chao Shi (Alibaba Group), Yin Zhang (Zhejiang University), Yuanchao Shu (Zhejiang University), Peng Cheng (Zhejiang University), Zeke Wang (Zhejiang University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803594)

## 英文摘要

As the gap between network and CPU speeds rapidly increases, the CPU-centric network stack proves inadequate due to excessive CPU and memory overheads. Though hardware-offloaded network stacks alleviate these issues, they suffer from limited flexibility in both control and data planes. It seems promising to offload network stacks to SmartNICs to provide high flexibility. However, naive offloading leads to low throughput due to the inherent architectural limitations of widespread off-path SmartNICs. Even simple operations on staged network traffic would overwhelm the limited SmartNIC memory bandwidth. To this end, we design SmartNS, a SmartNIC-centric network stack with software transport programmability and line-rate packet processing capabilities. To tackle the limitations of SmartNIC-induced challenges, we propose a header-only offloading TX path and an unlimited-working-set in-cache processing RX path to minimize memory traffic to fit the wimpy SmartNIC memory bandwidth. To fully utilize the SmartNIC computing resources, we propose a programmable offloading engine to enable cloud providers to offload customized tasks along with the network stack processing. We prototype SmartNS using the widespread Nvidia BlueField-3 SmartNIC, and implement RoCEv2 and Solar transport protocols by leveraging SmartNS’s software programmability. SmartNS achieves 2.2× higher throughput than the microkernel-based baseline in block storage disaggregation and 1.3× higher throughput than the hardware-offloaded baseline in KVCache transfer.

## 中文摘要

随着网络与 CPU 速度之间的差距迅速扩大，以 CPU 为中心的网络栈因过高的 CPU 与内存开销而显得力不从心。尽管硬件卸载的网络栈缓解了这些问题，但其控制面与数据面的灵活性都受限。将网络栈卸载到 SmartNIC 上以提供高灵活性看似颇具前景。然而，由于广泛使用的旁路式（off-path）SmartNIC 固有的架构局限，朴素的卸载方案会导致吞吐量偏低。即便对分阶段处理的网络流量做简单操作，也会压垮有限的 SmartNIC 内存带宽。为此，我们设计了 SmartNS，一个以 SmartNIC 为中心、具备软件传输可编程性与线速报文处理能力的网络栈。为应对 SmartNIC 带来的挑战，我们提出仅头部的卸载发送路径与无限工作集的缓存内处理接收路径，以最小化内存流量，从而适配孱弱的 SmartNIC 内存带宽。为充分利用 SmartNIC 的计算资源，我们提出可编程卸载引擎，使云提供商能够随网络栈处理一同卸载定制任务。我们基于广泛使用的 Nvidia BlueField-3 SmartNIC 实现了 SmartNS 原型，并借助其软件可编程性实现了 RoCEv2 与 Solar 传输协议。在块存储解耦场景中，SmartNS 相比基于微内核的基线实现了 2.2 倍的吞吐提升；在 KVCache 传输中相比硬件卸载基线实现了 1.3 倍的吞吐提升。

**英文关键词：** SmartNIC, Network stack, Datacenter network, RDMA

**中文关键词：** SmartNIC、网络栈、数据中心网络、RDMA

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
