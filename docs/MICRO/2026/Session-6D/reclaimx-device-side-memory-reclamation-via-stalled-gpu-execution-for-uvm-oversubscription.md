---
title: "ReclaimX: Device-Side Memory Reclamation via Stalled GPU Execution for UVM Oversubscription"
description: "MICRO 2026 · Session 6D · ReclaimX：通过暂停 GPU 执行实现统一虚拟内存超额使用时的设备端内存回收"
tags:
  - "MICRO2026"
  - "GPU"
---

# ReclaimX: Device-Side Memory Reclamation via Stalled GPU Execution for UVM Oversubscription

**中文标题：** ReclaimX：通过暂停 GPU 执行实现统一虚拟内存超额使用时的设备端内存回收

**所属 Session：** [Session 6D](index.md) · [MICRO 2026](../index.md)

**作者：** Seongtae Bang, Hyunkyun Shin, Hyungwon Park, Minho Kim, Daehoon Kim

**来源：** MICRO 2026，pp. 2263–2277；[DOI](https://doi.org/10.1109/MICRO67795.2026.00156)

## 英文摘要

Unified Virtual Memory (UVM) enables GPUs to execute workloads whose memory footprints exceed device capacity, yet oversubscribed execution remains bottlenecked by far-page-fault recovery. Our characterization shows that, at 150% oversubscription, fault handling can consume up to 45% of total kernel execution time. Under capacity pressure, a far-page fault simultaneously signals the need to free HBM capacity and stalls the faulting texture processing cluster (TPC) until recovery completes. Baseline UVM leaves this fault-stalled execution capacity idle while a host-driven recovery path, guided by coarse 2 MB region history despite 64 KB demand granularity, selects victims and initiates reclamation. We present ReclaimX, a GPU-resident memory-management architecture that uses fault-stalled TPCs to perform device-side reclamation during recovery. ReclaimX runs reclamation only on fault-stalled TPCs, drawing service capacity from execution contexts whose foreground progress has already stopped, and therefore requires neither static resource reservation nor proactive throttling. To make this loop effective, ReclaimX combines 64 KB victim ordering with selective compressed-resident retention and device-side local restore, converting selected host-mediated migrations into on-device restores while shortening subsequent recovery paths. Across 12 oversubscribed workloads, ReclaimX delivers a geometric-mean performance improvement of 2.33× over baseline UVM. Among the prefetch-integrated configurations we evaluate, ReclaimX reduces far-page faults by 90.6% and achieves a geometric-mean speedup of up to 3.61×. These results show that far-page faults can expose both the need for capacity relief and the stalled compute needed to perform it, enabling fine-grained device-side memory management under UVM oversubscription.

## 中文摘要

统一虚拟内存 (UVM) 使 GPU 能够执行内存占用超出设备容量的工作负载，但超额执行仍然受到远端缺页异常恢复的瓶颈。我们的表征表明，在 150% 超额使用的情况下，故障处理可能会消耗高达 45% 的总内核执行时间。在容量压力下，远端缺页异常会同时发出释放 HBM 容量的信号，并停止发生故障的纹理处理集群 (TPC)，直到恢复完成。基线 UVM 使这种故障停滞的执行能力闲置，而主机驱动的恢复路径（尽管需求粒度为 64 KB，但由粗略的 2 MB 区域历史记录引导）选择受害者并启动回收。我们推出了 ReclaimX，这是一种驻留在 GPU 上的内存管理架构，它使用故障停滞的 TPC 在恢复期间执行设备端回收。 ReclaimX 仅在故障停滞的 TPC 上运行回收，从前台进度已停止的执行上下文中获取服务容量，因此既不需要静态资源预留，也不需要主动限制。为了使这个循环有效，ReclaimX 将 64 KB 受害者排序与选择性压缩驻留保留和设备端本地恢复相结合，将选定的主机介导的迁移转换为设备上恢复，同时缩短后续恢复路径。在 12 个超额使用工作负载中，ReclaimX 的几何平均性能比基线 UVM 提高了 2.33 倍。在我们评估的预取集成配置中，ReclaimX 将远端缺页异常减少了 90.6%，并实现了高达 3.61 倍的几何平均加速。这些结果表明，远端缺页异常可能会暴露容量释放的需求以及执行容量释放所需的计算停滞，从而在 UVM 超额使用下实现细粒度的设备端内存管理。

## 中文关键词

图形处理器；统一虚拟内存；内存管理；显存超额使用；设备端内存回收

## 代码与研究制品

在所提供论文正文与附录中未找到可确认属于本文的公开代码入口。

[返回 Session 6D](index.md) · [MICRO 2026 主页](../index.md)
