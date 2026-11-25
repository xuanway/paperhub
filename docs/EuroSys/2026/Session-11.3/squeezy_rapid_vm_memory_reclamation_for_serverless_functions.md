---
title: "Squeezy: Rapid VM Memory Reclamation for Serverless Functions"
description: "EuroSys 2026 · Virtualization, Containers & OS Specialization · Orestis Lagkas Nikolos (National Technical University of Athens, Athens, Greece)"
tags:
  - "EuroSys2026"
  - "Virtualization, Containers & OS Specialization"
---

# Squeezy: Rapid VM Memory Reclamation for Serverless Functions

**中文标题：** Squeezy：面向无服务器函数的快速 VM 内存回收

**所属 Session：** [Session 11.3: Virtualization, Containers & OS Specialization](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Virtualization, Containers & OS Specialization。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Virtualization, Containers & OS Specialization</p>
</div>

**作者**：Orestis Lagkas Nikolos (National Technical University of Athens, Athens, Greece), Chloe Alverti (University of Illinois Urbana-Champaign, Illinois, USA), Stratos Psomadakis (National Technical University of Athens, Athens, Greece), Georgios Goumas (National Technical University of Athens, Athens, Greece), Nectarios Koziris (National Technical University of Athens, Athens, Greece)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769357)

## 英文摘要

Resource elasticity is one of the key defining characteristics of the Function-as-a-Service (FaaS) serverless computing paradigm. While compute resources assigned to VM-sandboxed functions can be seamlessly adjusted on the fly, memory elasticity remains challenging. Hot(un)plugging memory resources suffers from long reclamation latencies and occupies valuable CPU resources. We identify the obliviousness of the OS memory manager to the hotplugged memory as the key issue hindering hot-unplug performance, and design Squeezy, a novel approach for fast and efficient VM memory hot(un)plug, targeting VM-sandboxed serverless functions. Our key insight is that by segregating hotplugged memory regions from regular VM memory, we are able to bound the lifetime of allocations within these regions thus enabling their fast and efficient reclamation. We implement Squeezy in Linux v6.6 as an extension to the OS memory manager. Our evaluation reveals that Squeezy is an order-of-magnitude faster than state-of-the-art, keeping tail latency bounded, when reclaiming VM memory, achieving sub-second reclamation of multiple GiBs of memory while serving realistic FaaS load.

## 中文摘要

资源弹性是函数即服务（FaaS）无服务器计算范式的关键定义特征之一。虽然分配给 VM 沙箱函数的计算资源可以即时无缝调整，但内存弹性仍然具有挑战性。内存热（插）拔面临回收时延长的问题，并占用宝贵的 CPU 资源。我们发现，操作系统内存管理器对热插拔内存的无感知是阻碍热拔性能的关键问题，并据此设计了 Squeezy，一种面向 VM 沙箱无服务器函数的快速高效 VM 内存热（插）拔新方法。我们的关键洞察是：通过将热插拔内存区域与常规 VM 内存隔离，我们能够限定这些区域内分配对象的生命周期，从而实现快速高效的回收。我们在 Linux v6.6 中将 Squeezy 实现为操作系统内存管理器的扩展。评估表明，在承担真实 FaaS 负载时回收 VM 内存，Squeezy 比现有先进方案快一个数量级，且尾延迟保持有界，实现了数 GiB 内存的亚秒级回收。

**英文关键词：** Cloud Computing, Serverless, FaaS, Virtualization, Memory Elasticity, Ballooning, Memory Hotunplug, Partitioning, Allocation

**中文关键词：** 云计算、无服务器、FaaS、虚拟化、内存弹性、内存气球、内存热拔、分区、分配

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
