---
title: "SG-IOV: Socket-Granular I/O Virtualization for SmartNIC-Based Container Networks"
description: "ASPLOS 2026 · Session 8B · SG-IOV：面向基于 SmartNIC 的容器网络的套接字粒度 I/O 虚拟化"
tags:
  - "ASPLOS2026"
  - "Session 8B"
  - "Serverless & Cloud Networking"
---

# SG-IOV: Socket-Granular I/O Virtualization for SmartNIC-Based Container Networks

**中文标题：** SG-IOV：面向基于 SmartNIC 的容器网络的套接字粒度 I/O 虚拟化

**所属 Session：** [Session 8B](index.md) · [ASPLOS 2026](../index.md)

**作者：** Chenxingyu Zhao (University of Washington), Hongtao Zhang (University of Washington), Jaehong Min (University of Washington), Shengkai Lin (Shanghai Jiao Tong University), Wei Zhang (University of Connecticut), Kaiyuan Zhang (University of Washington), Ming Liu (University of Wisconsin–Madison), Arvind Krishnamurthy (University of Washington)

**单位：** University of Washington；Shanghai Jiao Tong University；University of Connecticut；University of Wisconsin–Madison

**来源：** ASPLOS 2026 · Volume 2 · [论文 DOI](https://doi.org/10.1145/3779212.3790218) · [官方日程](https://www.asplos-conference.org/asplos2026/program/index.html)

## 英文摘要

I/O Virtualization (IOV) is a cornerstone of cloud computing, with container networking as a critical form of IOV in modern cloud paradigms. While container networks serve as feature-rich infrastructure, they incur a high CPU tax yet leave room for efficiency improvement. A natural idea is to offload container networks onto hardware such as SmartNICs via IOV interfaces. However, existing IOV mechanisms, such as SR-IOV, are misaligned with container requirements: limited device scalability versus high container density, packet-layer abstraction versus application-layer processing demands, and coarse-grained virtualization versus fine-grained container workloads. In this work, we propose Socket-Granular I/O Virtualization (SG-IOV), a new IOV mechanism to offload container networks efficiently. SG-IOV provisions socket-level devices, supports size-varying transformations over a message-stream abstraction, and enables granular virtualization. Realizing this vision is non-trivial: Finer granularity stresses device scalability, while size-varying message processing complicates IO buffer management. Additionally, many fine-grained devices strain hardware virtualization enforcement. To overcome these challenges, the core principle of SG-IOV is that software mediates signals (e.g., descriptors) while accelerators touch the payload. This separation enables several innovations: resource multiplexing to support scalability, adaptive handling of size-varying tasks, and intermediate queuing to enforce virtualization. We prototype SG-IOV on the latest NVIDIA BlueField-3 and deliver an end-to-end container network solution. Our evaluations show that SG-IOV scales beyond 4K devices (10x more than VFs). Compared to Cilium, SG-IOV saves up to 1.9 cores per 10Gbps of traffic. Beyond core savings, SG-IOV achieves 53% higher bandwidth and reduces latency by up to 48%.

## 中文摘要

I/O 虚拟化（IOV）是云计算的基石，而容器网络是现代云范式中 IOV 的一种关键形态。容器网络虽然扮演着功能丰富的基础设施角色，却带来高昂的 CPU 开销，同时仍留有提升效率的空间。一个自然的想法是通过 IOV 接口将容器网络卸载到 SmartNIC 等硬件上。然而，现有 IOV 机制（如 SR-IOV）与容器的需求并不契合：设备可扩展性有限而容器密度很高，数据包层抽象而存在应用层处理需求，粗粒度虚拟化而容器工作负载细粒度。在本工作中，我们提出套接字粒度 I/O 虚拟化（SG-IOV），一种用于高效卸载容器网络的新型 IOV 机制。SG-IOV 提供套接字级设备，在消息流抽象之上支持尺寸可变的变换，并实现细粒度虚拟化。实现这一愿景并非易事：更细的粒度给设备可扩展性带来压力，而尺寸可变的消息处理使 IO 缓冲区管理复杂化。此外，大量细粒度设备给硬件虚拟化的强制执行带来压力。为克服这些挑战，SG-IOV 的核心原则是：软件负责中介信号（如描述符），而加速器负责处理载荷。这种分离带来了多项创新：用于支持可扩展性的资源复用、对尺寸可变任务的自适应处理，以及用于强制执行虚拟化的中间排队。我们在最新的 NVIDIA BlueField-3 上构建了 SG-IOV 原型，并交付了端到端的容器网络解决方案。评估表明，SG-IOV 可扩展到 4K 以上设备（比 VF 多 10 倍）。与 Cilium 相比，SG-IOV 每 10Gbps 流量最多节省 1.9 个核。除节省核之外，SG-IOV 还将带宽提高了 53%，并将延迟最多降低 48%。

## 英文关键词

SmartNIC; I/O Virtualization; Container Network; Cloud Computing

## 中文关键词

SmartNIC；I/O 虚拟化；容器网络；云计算

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3779212.3790218)
- [ASPLOS 2026 · Volume 2 论文集](https://doi.org/10.1145/3779212)
- [ASPLOS 2026 Detailed Program](https://www.asplos-conference.org/asplos2026/program/index.html)

[返回 Session 8B](index.md) · [返回 ASPLOS 2026](../index.md)
