---
title: "Gigaflow: Pipeline-Aware Sub-Traversal Caching for Modern SmartNICs"
description: "ASPLOS 2025 · Session 8B · Gigaflow：面向现代 SmartNIC 的流水线感知子遍历缓存"
tags:
  - "ASPLOS2025"
  - "Session 8B"
  - "Networking"
---

# Gigaflow: Pipeline-Aware Sub-Traversal Caching for Modern SmartNICs

**中文标题：** Gigaflow：面向现代 SmartNIC 的流水线感知子遍历缓存

**所属 Session：** [Session 8B](index.md) · [ASPLOS 2025](../index.md)

**作者：** Annus Zulfiqar (University of Michigan), Ali Imran (University of Michigan), Venkat Kunaparaju (Purdue University), Ben Pfaff (Feldera Inc.), Gianni Antichi (Politecnico di Milano), Muhammad Shahbaz (University of Michigan)

**单位：** University of Michigan；Purdue University；Feldera Inc.；Politecnico di Milano

**来源：** ASPLOS 2025 · [论文 DOI](https://doi.org/10.1145/3676641.3716000) · [官方日程](https://www.asplos-conference.org/asplos2025/program.html)

## 英文摘要

The success of modern public/edge clouds hinges heavily on the performance of their end-host network stacks if they are to support the emerging and diverse tenants' workloads (e.g., distributed training in the cloud to fast inference at the edge). Virtual Switches (vSwitches) are vital components of this stack, providing a unified interface to enforce high-level policies on incoming packets and route them to physical interfaces, containers, or virtual machines. As performance demands escalate, there has been a shift toward offloading vSwitch processing to SmartNICs to alleviate CPU load and improve efficiency. However, existing solutions struggle to handle the growing flow rule space within the NIC, leading to high miss rates and poor scalability. In this paper, we introduce Gigaflow, a novel caching system tailored for deployment on SmartNICs to accelerate vSwitch packet processing. Our core insight is that by harnessing the inherent pipeline-aware locality within programmable vSwitch pipelines—defining policies (e.g., L2, L3, and ACL) and their execution order (e.g., using P4 and OpenFlow)—we can create cache rules for shared segments (subtraversals) within the pipeline, rather than caching entire flows. These shared segments can be reused across multiple flows, resulting in higher cache efficiency and greater rule-space coverage. Our evaluations show that Gigaflow achieves up to a 51% improvement in cache hit rate (average 25% improvement) over traditional caching solutions (i.e., Megaflow), while capturing up to 450× more rule space within the limited memory of today's SmartNICs—all while operating at line speed.

## 中文摘要

若要支撑新兴且多样化的租户工作负载（从云端的分布式训练到边缘的快速推理），现代公有云/边缘云的成功在很大程度上取决于其终端主机网络栈的性能。虚拟交换机（vSwitch）是该网络栈的关键组成部分，它提供统一的接口，对入向数据包执行高层策略，并将其路由到物理接口、容器或虚拟机。随着性能需求不断攀升，业界已开始将 vSwitch 处理卸载到 SmartNIC，以减轻 CPU 负载并提升效率。然而，现有方案难以应对 NIC 内不断增长的流规则空间，导致高缺失率和较差的可扩展性。本文提出 Gigaflow，一种专为在 SmartNIC 上部署而设计的新型缓存系统，用于加速 vSwitch 的数据包处理。我们的核心洞见是：借助可编程 vSwitch 流水线中固有的流水线感知局部性——即定义策略（如 L2、L3 和 ACL）及其执行顺序（如使用 P4 和 OpenFlow）——我们可以为流水线内的共享片段（子遍历）创建缓存规则，而不是缓存整条流。这些共享片段可跨多条流复用，从而带来更高的缓存效率和更大的规则空间覆盖。评估表明，与传统的缓存方案（即 Megaflow）相比，Gigaflow 的缓存命中率最高提升 51%（平均提升 25%），同时在当今 SmartNIC 有限的内存中覆盖多达 450 倍的规则空间，且全程以线速运行。

## 英文关键词

SmartNICs; Slowpath; Megaflow; Gigaflow; Traversal; Sub-traversal; Caching; SDN; OVS; P4; FPGA; LTM

## 中文关键词

SmartNIC；慢路径；Megaflow；Gigaflow；遍历；子遍历；缓存；SDN；OVS；P4；FPGA；LTM

## 相关链接

- [论文 DOI](https://doi.org/10.1145/3676641.3716000)
- [ASPLOS 2025 官方 Program](https://www.asplos-conference.org/asplos2025/program.html)

[返回 Session 8B](index.md) · [返回 ASPLOS 2025](../index.md)
