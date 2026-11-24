---
title: "RosenBridge: A Framework for Enabling Express I/O Paths Across the Virtualization Boundary"
description: "FAST 2026 · Virtualization · 第 425–442 页"
tags:
  - "FAST2026"
  - "Virtualization"
---

# RosenBridge: A Framework for Enabling Express I/O Paths Across the Virtualization Boundary

**中文标题**：RosenBridge：跨越虚拟化边界启用快速 I/O 路径的框架

**Session**：Virtualization · 2026-02-25 16:10–17:30 · Chair：Mai Zheng（Iowa State University）

**作者**：Shi Qiu, Xiamen University; Li Wang, KylinSoft; Jianqin Yan and Ruofan Xiong, Xiamen University; Leping Yang, Shanghai Jiao Tong University; Xin Yao, Renhai Chen, and Gong Zhang, Huawei; Dongsheng Li, The National University of Defense Technology; Jiwu Shu, Tsinghua University; Yiming Zhang, Shanghai Jiao Tong University and Xiamen University

**会议**：FAST 2026 · Santa Clara, CA · 第 425–442 页

**USENIX 页面**：[https://www.usenix.org/conference/fast26/presentation/qiu](https://www.usenix.org/conference/fast26/presentation/qiu)

**论文 PDF**：[fast26-qiu.pdf](https://www.usenix.org/system/files/fast26-qiu.pdf)

---

## 英文摘要

With the emergence of high-performance storage devices, the overhead of the storage stack has become a major I/O performance bottleneck. To alleviate this problem, a number of express I/O paths have been proposed based on the concept of near-data processing (NDP), such as query I/O resubmission (XRP) and GPU-direct storage (GDS). Unfortunately, in virtualized environments, none of these bare-metal express I/O paths can cross the virtualization boundary between the guest virtual machines (VMs) and the host, leaving applications inside guest VMs unable to benefit from them.

This paper presents RosenBridge, a framework for enabling express I/O paths across the virtualization boundary. At the core of RosenBridge is a new paravirtualized I/O device called virtio-ndp, which allows the guest to offload NDP optimizations to the hypervisor in the host userspace based on uBPF (userspace Berkeley Packet Filter). We connect the virtio-ndp backend with the host kernel’s asynchronous I/O stack for efficient I/O scheduling, and provide a set of helper functions for convenient guest-host address translation. We strictly limit the memory access scope of uBPF programs to guarantee security and collaboratively throttle the multi-path I/O to ensure fairness among guest VMs. We demonstrate the effectiveness of RosenBridge through two use cases, respectively supporting XRP and GDS in virtualized environments. Evaluation shows that RosenBridge significantly outperforms the state-of-the-art I/O paravirtualization frameworks (virtio and vhost) in I/O performance, while effectively reducing CPU usage. Compared to the bare-metal express I/O paths (XRP and GDS), RosenBridge only incurs a slight performance degradation.

## 中文摘要

随着高性能存储设备的出现，存储栈开销已成为主要的 I/O 性能瓶颈。为缓解这一问题，基于近数据处理（NDP）概念的一系列快速 I/O 路径被提出，例如查询 I/O 重新提交（XRP）和 GPU 直连存储（GDS）。遗憾的是，在虚拟化环境中，这些裸机快速 I/O 路径都无法跨越客户虚拟机（VM）与主机之间的虚拟化边界，导致客户 VM 内的应用无法从中受益。

本文提出 RosenBridge，一个跨越虚拟化边界启用快速 I/O 路径的框架。RosenBridge 的核心是一种名为 virtio-ndp 的新型半虚拟化 I/O 设备，它使客户机能够基于 uBPF（用户态 Berkeley Packet Filter）将 NDP 优化卸载到主机用户态的虚拟机监控器。我们将 virtio-ndp 后端与主机内核的异步 I/O 栈连接，以实现高效的 I/O 调度，并提供一组辅助函数以便于客户机—主机地址转换。我们严格限制 uBPF 程序的内存访问范围以保证安全，并协同限流多路径 I/O 以确保客户 VM 之间的公平性。我们通过两个用例展示 RosenBridge 的有效性，分别在虚拟化环境中支持 XRP 和 GDS。评估表明，RosenBridge 在 I/O 性能上显著优于最先进的 I/O 半虚拟化框架（virtio 和 vhost），同时有效降低 CPU 使用率。与裸机快速 I/O 路径（XRP 和 GDS）相比，RosenBridge 仅带来轻微的性能下降。
