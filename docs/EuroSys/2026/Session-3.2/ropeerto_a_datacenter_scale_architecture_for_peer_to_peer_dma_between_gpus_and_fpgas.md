---
title: "RoPeerTo: A Datacenter-Scale Architecture for Peer-To-Peer DMA between GPUs and FPGAs"
description: "EuroSys 2026 · Datacenter Network Fabrics & RDMA · Marco Venere (Politecnico di Milano), Giuseppe Sorrentino (Politecnico di Milano"
tags:
  - "EuroSys2026"
  - "Datacenter Network Fabrics & RDMA"
---

# RoPeerTo: A Datacenter-Scale Architecture for Peer-To-Peer DMA between GPUs and FPGAs

**中文标题：** RoPeerTo：面向数据中心规模的 GPU 与 FPGA 间对等 DMA 架构

**所属 Session：** [Session 3.2: Datacenter Network Fabrics & RDMA](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Datacenter Network Fabrics & RDMA。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Datacenter Network Fabrics & RDMA</p>
</div>

**作者**：Marco Venere (Politecnico di Milano), Giuseppe Sorrentino (Politecnico di Milano), Benjamin Ramhorst (ETH Zurich), Maximilian Jakob Heer (ETH Zurich), Lucian Petrica (AMD Research and Advanced Development), Dario Korolija (AMD Research and Advanced Development), Marco D. Santambrogio (Politecnico di Milano), Davide Conficconi (Politecnico di Milano), Gustavo Alonso (ETH Zurich), Ken O'Brien (AMD Research and Advanced Development)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803620)

## 英文摘要

Modern datacenters integrate heterogeneous accelerators, such as GPUs and FPGAs, to speed up different stages of compute-intensive pipelines. GPUs are best suited for massively parallel workloads (e.g., deep learning), while FPGAs excel at task-level parallelism, stream-oriented processing, and in-network acceleration. Since these architectures must exchange data efficiently, literature introduced Peer-To-Peer (P2P) communication across PCI Express (PCIe) devices, to reduce CPU-driven orchestration and avoid intermediate, redundant buffer copies that degrade performance. However, current solutions are either closed-source or tied to proprietary frameworks, limiting P2P communication across most PCIe-based devices and requiring significant technical effort to enable P2P capabilities on supported hardware. For this reason, we propose RoPeerTo, a fully open-source, datacenter-scale architecture for P2P DMA communication over PCIe, validated on both GPUs and FPGAs. The goal is to provide a general, open alternative that ensures flexibility, efficiency, and usability. To this end, we design a complete HW/SW stack operating across different layers, supporting standard protocols for DMA-based memory sharing, advanced tools for device virtualization, memory address translation, and access protection. The result is a unified framework exposing a high-level API to end users, that enables direct communication between accelerators such as FPGAs and GPUs, and abstracts away the underlying hardware setup and management. We validate the system across different scenarios. First, we isolate the communication layer, observing a 5.61× speedup and a 37.99% reduction in GPU power consumption during data transfer. Next, we leverage the system for a compute-intensive workload where communication is only a partial bottleneck, achieving a 6.77% speedup without any compute-side modifications. Finally, we evaluate communication-heavy distributed computing workloads, demonstrating up to a 21.79× speedup in network-bound data scattering.

## 中文摘要

现代数据中心集成 GPU 和 FPGA 等异构加速器，以加速计算密集型流水线中的不同阶段。GPU 最适合大规模并行工作负载（如深度学习），而 FPGA 擅长任务级并行、面向流的处理以及网内加速。由于这些架构必须高效地交换数据，已有文献提出了跨 PCI Express（PCIe）设备的对等（P2P）通信，以减少由 CPU 驱动的编排，并避免会损害性能的中间冗余缓冲区拷贝。然而，现有方案要么是闭源的，要么绑定于专有框架，限制了大多数基于 PCIe 的设备之间的 P2P 通信，并且在受支持的硬件上启用 P2P 能力需要大量技术投入。为此，我们提出 RoPeerTo，一个完全开源、面向数据中心规模的 PCIe 上 P2P DMA 通信架构，并在 GPU 和 FPGA 上进行了验证。其目标是提供一个通用、开放的替代方案，确保灵活性、高效性和易用性。为此，我们设计了一套跨不同层次的完整软硬件栈，支持基于 DMA 的内存共享的标准协议，以及设备虚拟化、内存地址转换和访问保护等高级工具。最终形成一个统一的框架，向终端用户提供高层 API，使 FPGA 和 GPU 等加速器之间能够直接通信，并屏蔽底层的硬件设置与管理。我们在多种场景下验证了该系统。首先，我们隔离出通信层，观察到数据传输过程中获得 5.61 倍的加速，GPU 功耗降低 37.99%。接着，我们将该系统用于一个通信只是部分瓶颈的计算密集型工作负载，在计算侧未做任何修改的情况下获得 6.77% 的加速。最后，我们评估了通信密集的分布式计算工作负载，在网络受限的数据分发场景中实现了最高 21.79 倍的加速。

**英文关键词：** peer-to-peer dma, direct memory access, heterogeneous systems

**中文关键词：** 对等 DMA、直接内存访问、异构系统

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
