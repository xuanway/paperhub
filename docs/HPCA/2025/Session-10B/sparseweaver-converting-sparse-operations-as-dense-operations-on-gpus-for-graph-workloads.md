---
title: "SparseWeaver: Converting Sparse Operations as Dense Operations on GPUs for Graph Workloads"
description: "HPCA 2025 · All in on GPUs"
tags:
  - "HPCA2025"
  - "All in on GPUs"
---

# SparseWeaver: Converting Sparse Operations as Dense Operations on GPUs for Graph Workloads

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: All in on GPUs。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · All in on GPUs</p>
</div>

**论文链接**：
**作者**：Shinnung Jeong (Yonsei University), Liam Paul Cooper (Georgia Tech), Ju Min Lee (Yonsei University), Heelim Choi (Yonsei University), Nicholas Parnenzini (Georgia Institute of Technology), Chihyo Ahn (Georgia Tech), Yongwoo Lee (Yonsei University), Hanjun Kim (Yonsei University), Hyesoon Kim (Georgia Tech)
**会议**：HPCA 2025

---

## 中文标题

SparseWeaver：在 GPU 上将稀疏操作转换为稠密操作以处理图负载

## 英文摘要

Thanks to their scalable parallel processing capability, GPUs are promising computing resources for graph processing, in which identical operations are applied to a large number of edges and vertices. However, the sparsity and skewness of real-world graphs cause imbalanced workloads across GPU threads within the same warp, thus impeding efficient processing on the GPU. To mitigate this workload imbalance problem, existing works propose workload balancing hardware and software schemes. However, these solutions often suffer from additional memory overhead or increased computations and communication overheads during inter-warp and intra-warp synchronization. This work proposes a new hardware-software collaborative graph processing framework, SparseWeaver, that converts sparse operations in graph processing into dense operations using graph topology and makes the workloads balanced across GPU threads. Based on the analysis of common patterns in software schemes, we propose Weaver, a new lightweight GPU functional unit microarchitecture that fully leverages the benefits of the GPU architecture and exploits memory access locality. We prototype SparseWeaver on the open-source RISC-V Vortex GPU and demonstrate 2.36 times faster execution time compared to state-of-the-art schemes while incurring a low area overhead of 0.045% from increased dedicated logic registers.

## 中文摘要

得益于可扩展的并行处理能力，GPU 是图处理中颇具前景的计算资源，因为图处理会对大量边和顶点施加相同的操作。然而，真实图的稀疏性与偏斜性导致同一线程束（warp）内 GPU 线程之间的负载不均衡，从而阻碍 GPU 上的高效处理。为缓解该负载不均衡问题，已有工作提出了负载均衡的硬件与软件方案。但这些方案往往伴随额外的内存开销，或在线程束间与线程束内同步过程中产生更多的计算与通信开销。本文提出一种新的软硬件协同图处理框架 SparseWeaver，它利用图拓扑将图处理中的稀疏操作转换为稠密操作，并使负载在 GPU 线程间均衡。基于对软件方案中常见模式的分析，我们提出 Weaver，一种新的轻量级 GPU 功能单元微架构，充分利用 GPU 架构的优势并挖掘访存局部性。我们在开源 RISC-V Vortex GPU 上对 SparseWeaver 进行原型实现，相较最先进方案执行时间快 2.36 倍，同时因增加专用逻辑寄存器仅带来 0.045% 的低面积开销。
