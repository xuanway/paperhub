---
title: "CoCoTree: A Computation-Capable Architecture for Collective Communication in Scalable PIM"
description: "HPCA 2026 · Processing-in-Memory Architectures"
tags:
  - "HPCA2026"
  - "Processing-in-Memory Architectures"
---

# CoCoTree: A Computation-Capable Architecture for Collective Communication in Scalable PIM

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Processing-in-Memory Architectures。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Processing-in-Memory Architectures</p>
</div>

**论文链接**：
**作者**：Shunchen Shi Institute of Computing Technology, Chinese Academy of Sciences ; University of Chinese Academy of Sciences , Qijia Yang Institute of Computing Technology, Chinese Academy of Sciences ; University of Chinese Academy of Sciences , Fan Yang Institute of Computing Technology, Chinese Academy of Science , Yu Huang Huazhong University of Science and Technology , Youwei Zhuo Peking University , Zhichun Li Institute of Computing Technology, Chinese Academy of Sciences ; University of Chinese Academy of Sciences , Ninghui Sun State Key Laboratory of Computer Architecture, Institute of Computing Technology, Chinese Academy of Sciences, University of Chinese Academy of Sciences , Xueqi Li State Key Lab of Processors, Institute of Computing Technology, CAS
**会议**：HPCA 2026

---

## 中文标题

CoCoTree：面向可扩展 PIM 集合通信的具备计算能力架构

## 英文摘要

The growing demand for high-bandwidth and large-capacity memory access in data-intensive workloads has driven the development and deployment of Processing-in-Memory (PIM) architectures. However, existing DIMM-based PIM systems suffer from the severe communication bottleneck between the processing elements (PEs) near the PIM banks due to their requirement on host CPU forwarding. This bottleneck limits the efficiency of collective operations and degrades scalability and performance for workloads that require inter-PE communication. To address the communication limitation, we propose CoCoTree, a computation-capable architecture for collective communication in scalable DIMM-based PIM. CoCoTree supports direct and high-throughput inter-PE communication without host intervention. CoCoTree accelerates key collective communication using novel hierarchical binary tree topology and lightweight in-network computation support. We design and implement microarchitectures for the main building blocks: Co-Leaf and Co-Node, to efficiently handle the data packing, routing, and processing in CoCoTree. Furthermore, we also introduce a packet-based communication protocol tailored to the CoCoTree architecture, which decouples control and data through a two-phase configuration-computation communication mechanism to efficiently support a wide range of collective communication operations. CoCoTree effectively mitigates inter-PE communication bottlenecks, enabling scalable PIM systems capable of meeting the demands of growing data size. Experimental results show that CoCoTree achieves up to 95.6× improvement for collective operations and improves end-to-end application performance by up to 10.5× across various workloads over the baseline PIM, while outperforming state-of-the-art PIM communication architectures in both performance and scalability.

## 中文摘要

数据密集型负载对高带宽、大容量内存访问的需求不断增长，推动了存内处理（PIM）架构的发展与部署。然而，现有基于 DIMM 的 PIM 系统由于需要主机 CPU 转发，在 PIM bank 附近的处理单元（PE）之间存在严重的通信瓶颈。该瓶颈限制了集合操作的效率，并削弱了需要 PE 间通信的负载的可扩展性与性能。为解决通信局限，我们提出 CoCoTree，一种面向可扩展 DIMM 型 PIM 中集合通信的具备计算能力的架构。CoCoTree 无需主机干预即可支持 PE 间直接、高吞吐的通信，并利用新颖的分层二叉树拓扑和轻量级网内计算支持来加速关键集合通信。我们为主构建模块 Co-Leaf 与 Co-Node 设计并实现了微架构，以高效处理数据打包、路由与处理。此外，我们提出一种面向 CoCoTree 的基于分组的通信协议，通过两阶段的“配置—计算”机制将控制与数据解耦，从而高效支持多种集合通信操作。CoCoTree 有效缓解了 PE 间通信瓶颈，使可扩展 PIM 系统能够满足不断增长的数据规模需求。实验结果表明，相比基线 PIM，CoCoTree 对集合操作最高提升 95.6 倍，端到端应用性能在各种负载上最高提升 10.5 倍，并在性能与可扩展性上均优于最先进的 PIM 通信架构。
