---
title: "NVMePass: A Lightweight, High-performance and Scalable NVMe Virtualization Architecture with I/O Queues Passthrough"
description: "HPCA 2025 · The Winning System"
tags:
  - "HPCA2025"
  - "The Winning System"
---

# NVMePass: A Lightweight, High-performance and Scalable NVMe Virtualization Architecture with I/O Queues Passthrough

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: The Winning System。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · The Winning System</p>
</div>

**论文链接**：
**作者**：Yiquan Chen (Zhejiang University & Alibaba Group), Zhen Jin (Zhejiang University), Yijing Wang (Alibaba Group), Yi Chen (University of Michigan), Jiexiong Xu (Zhejiang University), Hao Yu (Alibaba Group), Jinlong Chen (Alibaba Group), Wenhai Lin (Zhejiang University), Kanghua Fang (Alibaba Group), Keyao Zhang (Zhejiang University), Chengkun Wei (Zhejiang University), Qiang Liu (Alibaba Group), Yuan Xie (HKUST), Wenzhi Chen (Zhejiang University)
**会议**：HPCA 2025

---

## 中文标题

NVMePass：轻量、高性能、可扩展的 I/O 队列直通 NVMe 虚拟化架构

## 英文摘要

Most data-intensive applications currently run on NVMe storage, and virtualization is essential in cloud computing. Existing NVMe virtualization technologies include software-based and hardware-assisted. Virtio suffers from severe performance degradation, and polling-based solutions consume too many valuable CPU resources. Hardware-assisted solutions provide high performance and no CPU usage but have the challenges of developing dedicated hardware. In this paper, we propose NVMePass, a novel software-hardware co-design NVMe passthrough virtualization architecture designed to achieve high performance and no CPU overhead while maintaining high scalability. The key ideas of NVMePass are NVMe I/O queues passthrough for VMs and a mechanism to ensure security. The NVMePass supports DMA and interrupts remapping for VMs without hypervisor involvement, eliminating virtualization overhead and providing near-native performance. Isolation is achieved by I/O queues and logical block address resources exclusively allocated to VMs. We propose NVMe Resource Domain (NRD) and implement it in the NVMe controller to intercept illegal I/O requests. Thus, isolation and security are fully achieved. Results from our experiments show that NVMePass can provide comparable performance to VFIO, with an IOPS of 100.1%-100.5% of VFIO. Furthermore, compared to SPDK-Vhost, NVMePass achieves 40.0% lower latency when running 150 VMs, and NVMePass has an improvement of 68.0% OPS performance in a real-world application when running 100 VMs.

## 中文摘要

当前大多数数据密集型应用运行在 NVMe 存储之上，而虚拟化在云计算中不可或缺。已有的 NVMe 虚拟化技术包括基于软件与硬件辅助两类。Virtio 存在严重性能下降，基于轮询的方案则消耗过多宝贵的 CPU 资源。硬件辅助方案性能高且不占用 CPU，但面临开发专用硬件的挑战。本文提出 NVMePass，一种新颖的软硬件协同设计 NVMe 直通虚拟化架构，旨在实现高性能与零 CPU 开销的同时保持良好的可扩展性。NVMePass 的核心思想是为虚拟机提供 NVMe I/O 队列直通，并提供确保安全的机制。NVMePass 支持在无需 hypervisor 介入的情况下为虚拟机重映射 DMA 与中断，从而消除虚拟化开销并提供接近原生的性能。隔离性通过将 I/O 队列与逻辑块地址资源独占分配给虚拟机来实现。我们提出 NVMe 资源域（NRD）并在 NVMe 控制器中实现，以拦截非法 I/O 请求，从而完整实现隔离与安全。实验结果表明，NVMePass 能提供与 VFIO 相当的性能，IOPS 达到 VFIO 的 100.1%-100.5%。此外，与 SPDK-Vhost 相比，NVMePass 在运行 150 台虚拟机时时延降低 40.0%，在运行 100 台虚拟机的真实应用中 OPS 性能提升 68.0%。
