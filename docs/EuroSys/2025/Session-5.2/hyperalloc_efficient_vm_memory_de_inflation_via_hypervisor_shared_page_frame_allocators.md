---
title: "HyperAlloc: Efficient VM Memory De/Inflation via Hypervisor-Shared Page-Frame Allocators"
description: "EuroSys 2025 · Virtualization · Lars Wrenger (Leibniz Universität Hannover), Kenny Albes (Leibniz Universität Ha"
tags:
  - "EuroSys2025"
  - "Virtualization"
---

# HyperAlloc: Efficient VM Memory De/Inflation via Hypervisor-Shared Page-Frame Allocators

**中文标题：** 通过虚拟机监控器共享页帧分配器高效调整虚拟机内存膨胀

**所属 Session：** [Session 5.2: Virtualization](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Virtualization。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Virtualization</p>
</div>

**作者**：Lars Wrenger (Leibniz Universität Hannover), Kenny Albes (Leibniz Universität Hannover), Marco Wurps (Leibniz Universität Hannover), Christian Dietrich (Technische Universität Braunschweig), Daniel Lohmann (Leibniz Universität Hannover)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717484)

## 英文摘要

The provisioning of the right amount of DRAM to virtual machines (VMs) is still a major challenge and cost driver in virtualization settings. Many VMs run applications with highly volatile memory demands, which either leads to massive overprovisioning in low-demand phases or poor QoS in high-demand phases. Memory hotplugging and ballooning have become established techniques (in Linux/KVM available via virtio-mem and virtio-balloon) to dynamically de/inflate the physical memory of a VM cooperatively, by having the guests give back unused memory to the hypervisor. However, current VM deflation techniques are either not DMA-safe, preventing the passthrough of important devices like GPUs or NICs, or are not flexible or fast enough to cope with the frequently changing demands of the guest.

We present HyperAlloc, a DMA-safe and extremely efficient mechanism for virtual machine de/inflation. The core idea is to provide the hypervisor direct access to the guest’s page-frame allocator, greatly reducing the communication overhead. HyperAlloc can shrink virtual machines 362 times faster than virtio-balloon and 10 times faster than virtio-mem while having no measurable impact on the guest’s performance. HyperAlloc’s automatic reclamation provides for better memory elasticity by reducing the average memory footprint of a clang compilation by 17 percent compared to virtio-balloon’s free-page reporting while, again, having no measurable impact on the guest’s performance.

## 中文摘要

为虚拟机（VM）配置适量的 DRAM 仍是虚拟化环境中的一大挑战和成本驱动因素。许多 VM 运行内存需求高度波动的应用，这要么导致低需求阶段的大量超额配置，要么在高需求阶段导致较差的 QoS。内存热插拔和内存气球已成为成熟技术（在 Linux/KVM 中通过 virtio-mem 和 virtio-balloon 提供），通过让 guest 将未使用的内存归还给 hypervisor，以协作方式动态缩减或扩充 VM 的物理内存。然而，当前的 VM 缩减技术要么不是 DMA 安全的，从而无法直通 GPU 或 NIC 等重要设备，要么不够灵活或快速，无法应对 guest 频繁变化的需求。

我们提出 HyperAlloc，一种 DMA 安全且极其高效的虚拟机内存缩减与扩充机制。其核心思想是让 hypervisor 直接访问 guest 的页帧分配器，从而大幅降低通信开销。HyperAlloc 缩减虚拟机比 virtio-balloon 快 362 倍、比 virtio-mem 快 10 倍，同时对 guest 性能没有可测量的影响。HyperAlloc 的自动回收通过将 clang 编译的平均内存占用相比 virtio-balloon 的空闲页上报降低 17%，提供了更好的内存弹性，同时同样对 guest 性能没有可测量的影响。

**英文关键词：** Virtual Machines, Ballooning, Overcommitment, Allocators

**中文关键词：** 虚拟机、内存气球、内存超额配置、分配器

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
