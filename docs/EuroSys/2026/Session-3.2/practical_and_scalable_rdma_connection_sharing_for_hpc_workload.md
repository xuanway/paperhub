---
title: "Practical and Scalable RDMA Connection Sharing for HPC Workload"
description: "EuroSys 2026 · Datacenter Network Fabrics & RDMA · Yuejie Wang (Peking University), Tuo Fang (Huawei Technologies Co., Ltd.), Biyu "
tags:
  - "EuroSys2026"
  - "Datacenter Network Fabrics & RDMA"
---

# Practical and Scalable RDMA Connection Sharing for HPC Workload

**中文标题：** 面向 HPC 负载的实用且可扩展的 RDMA 连接共享

**所属 Session：** [Session 3.2: Datacenter Network Fabrics & RDMA](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Datacenter Network Fabrics & RDMA。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Datacenter Network Fabrics & RDMA</p>
</div>

**作者**：Yuejie Wang (Peking University), Tuo Fang (Huawei Technologies Co., Ltd.), Biyu Peng (Huawei Technologies Co., Ltd.), Yang Cheng (Huawei Technologies Co., Ltd.), Xin Sun (Huawei Technologies Co., Ltd.), Chengchao Xu (Huawei Technologies Co., Ltd.), Yuchen Tang (Huawei Technologies Co., Ltd.), Yuxin Ren (Huawei Technologies Co., Ltd.), Ning Jia (Huawei Technologies Co., Ltd.), Xinwei Hu (Huawei Technologies Co., Ltd.), Yunfei Du (Huawei Technologies Co., Ltd.), Guyue (Grace) Liu (Peking University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769381)

## 英文摘要

RDMA is a fundamental communication infrastructure in high-performance computing (HPC). However, as the number of RDMA connections increases, system performance rapidly declines and memory consumption increases sharply. Previous research demonstrates that sharing RDMA connections among processes is necessary and effective to address the scalability problem. Unfortunately, previous work shares connections in software, thus incurring substantial overhead to each packet operation, and fails to comprehensively explore control policies to achieve superior sharing decisions.

This paper proposes a novel RDMA connection-sharing framework for HPC with a zero-cost hardware-assisted data plane and a lightweight fine-grained control plane. We leverage advanced RDMA extended reliable connection transport to fully offload connection sharing to the NIC. The control software contains a comprehensive set of fine-grained yet simple sharing policies that jointly distribute messages across multiple levels. To minimize the control plane execution overhead, we combine several optimizations tailored to the characteristics of HPC. Evaluation of real-world HPC applications shows up to 67.6% better performance and more than 120GB of memory savings. Our solution has been deployed in a commercial HPC cluster with 85 nodes, delivering 10% end-to-end performance improvement to the customer.

## 中文摘要

RDMA 是高性能计算（HPC）中的基础通信设施。然而，随着 RDMA 连接数量的增加，系统性能迅速下降，内存消耗急剧上升。已有研究表明，在进程之间共享 RDMA 连接是解决可扩展性问题的必要且有效的手段。遗憾的是，先前的工作以软件方式共享连接，因而对每次报文操作都带来可观的开销，并且未能全面探索控制策略以实现更优的共享决策。

本文提出一种面向 HPC 的新型 RDMA 连接共享框架，具有零开销的硬件辅助数据面和轻量级的细粒度控制面。我们利用先进的 RDMA 扩展可靠连接传输，将连接共享完全卸载到网卡。控制软件包含一整套细粒度且简单的共享策略，可在多个层面共同分发消息。为最小化控制面的执行开销，我们结合了若干针对 HPC 特性定制的优化。对真实 HPC 应用的评估显示，性能最高提升 67.6%，并节省超过 120GB 内存。我们的方案已部署在一个拥有 85 个节点的商业 HPC 集群中，为客户带来了 10% 的端到端性能提升。

**英文关键词：** HPC, RDMA,Scalability

**中文关键词：** HPC、RDMA、可扩展性

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
