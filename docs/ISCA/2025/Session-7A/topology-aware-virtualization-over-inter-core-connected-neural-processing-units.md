---
title: "Topology-Aware Virtualization over Inter-Core Connected Neural Processing Units"
description: "ISCA 2025 · Session 7A · 面向核间互连神经处理器的拓扑感知虚拟化"
tags:
  - "ISCA2025"
  - "Session 7A"
  - "ML Acceleration III"
---

# Topology-Aware Virtualization over Inter-Core Connected Neural Processing Units

**中文标题：** 面向核间互连神经处理器的拓扑感知虚拟化

**所属 Session：** [Session 7A](index.md) · [ISCA 2025](../index.md)

**作者：** Dahu Feng, Erhu Feng, Dong Du, Pinjie Xu, Yubin Xia, Haibo Chen, Rong Zhao

**来源：** ISCA 2025 · [论文 DOI](https://doi.org/10.1145/3695053.3731002) · [官方日程](https://www.iscaconf.org/isca2025/program/)

## 英文摘要

With the rapid development of artificial intelligence (AI) appli- cations, an emerging class of AI accelerators, termed Inter-core Connected Neural Processing Units (NPU), has been adopted in both cloud and edge computing environments, like Graphcore IPU, Tenstorrent, etc. Despite their innovative design, these NPUs often demand substantial hardware resources, leading to suboptimal re- source utilization due to the imbalance of hardware requirements across various tasks. To address this issue, prior research has ex- plored virtualization techniques for monolithic NPUs, but has ne- glected inter-core connected NPUs with the hardware topology. This paper introduces vNPU, the first comprehensive virtualiza- tion design for inter-core connected NPUs, integrating three novel techniques: (1) NPU route virtualization, which redirects instruc- tion and data flow from virtual NPU cores to physical ones, creating a virtual topology; (2) NPU memory virtualization, designed to min- imize translation stalls for SRAM-centric and NoC-equipped NPU cores, thereby maximizing the memory bandwidth; and (3) Best- effort topology mapping, which determines the optimal mapping from all candidate virtual topologies, balancing resource utilization with end-to-end performance. We have developed a prototype of vNPU on both an FPGA platform (Chipyard+FireSim) and a simula- tor (DCRA). Evaluation results demonstrate that when executing multiple NPU workloads on virtual NPUs, vNPU achieves perfor- mance improvements of up to 1.92x and 1.28x for the Transformer and ResNet models, respectively, in comparison to the MIG-based virtualization method. Furthermore, the hardware performance overhead associated with the virtualization itself is minimal, incur- ring less than 1% reduction in end-to-end performance.

## 中文摘要

人工智能应用快速发展，一类新兴AI加速器——核间互联型神经网络处理单元（NPU），已经在云与边缘场景落地，代表产品如Graphcore IPU、Tenstorrent等。这类NPU架构新颖，但硬件资源开销巨大；不同任务对硬件资源需求不均衡，导致资源利用率偏低。
已有研究针对单体NPU开展虚拟化技术探索，但忽略了带拓扑互联的核间互联型NPU。本文提出vNPU，首个面向核间互联NPU的完整虚拟化方案，包含三项创新机制：（1）NPU路由虚拟化，将虚拟NPU核的指令与数据流重定向到物理核，构建虚拟拓扑；（2）NPU内存虚拟化，针对以SRAM为主、搭载片上网络的NPU核，减少地址转换停顿，最大化内存带宽；（3）尽力型拓扑映射，在全部候选虚拟拓扑中求解最优映射方案，均衡资源利用率与端到端性能。

本文基于FPGA平台（Chipyard+FireSim）与仿真器（DCRA）搭建vNPU原型。评测结果表明：在虚拟NPU上同时运行多个NPU负载时，对比基于MIG的虚拟化方案，Transformer模型最高提速1.92倍，ResNet最高提速1.28倍。虚拟化本身带来的性能开销很小，端到端性能损失不到1%。

## 英文关键词

Virtualization, System-on-Chip, Accelerator, AI

## 中文关键词

虚拟化, 片上系统, 加速器, 人工智能

## 代码与研究制品

在现有本地资料中未找到可确认的公开代码或研究制品入口。

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3695053.3731002)
- [ISCA 2025 Main Program](https://www.iscaconf.org/isca2025/program/)

[返回 Session 7A](index.md) · [返回 ISCA 2025](../index.md)
