---
title: "SCALE: Tackling Communication Bottlenecks in Confidential Multi-GPU ML"
description: "HPCA 2026 · Distributed and Multi-GPU Training"
tags:
  - "HPCA2026"
  - "Distributed and Multi-GPU Training"
---

# SCALE: Tackling Communication Bottlenecks in Confidential Multi-GPU ML

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Distributed and Multi-GPU Training。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Distributed and Multi-GPU Training</p>
</div>

**论文链接**：
**作者**：Joongun Park Georgia Tech , Yongqin Wang University of Southern California , Huan Xu Georgia Institute of Technology , Hanjiang Wu Georgia Institute of Technology , Mengyuan Li USC , Tushar Krishna Georgia Institute of Technology
**会议**：HPCA 2026

---

## 中文标题

SCALE：应对机密多 GPU 机器学习中的通信瓶颈

## 英文摘要

Machine Learning (ML) has become a cornerstone in numerous applications, creating the need for secure and efficient distributed ML frameworks. However, maintaining data privacy in these systems poses significant challenges, particularly in distributed environments where user data and model parameters must frequently be transmitted between GPUs. Confidential GPU computing technologies, such as NVIDIA’s Confidential Computing (CC) mode, offer hardware-based enterprise solutions designed to protect ML workloads in untrusted environments (e.g., public clouds). These technologies leverage heterogeneous systems that combine Confidential Virtual Machines (CVMs) with GPU-based Trusted Execution Environments (TEEs). Nevertheless, confidential computing introduces considerable performance overhead due to its complex heterogeneous architecture and the high-throughput data flows required across TEE security boundaries. For example, encrypted communication occurs both between CVMs and GPU TEEs, and among multiple GPU TEEs, resulting in significant latency compared to native PCIe or high-speed interconnects such as NVLink. Our extensive evaluation shows that these overheads become particularly severe during collective communication operations, which suffer from encryption-induced delays that negatively impact end-to-end training performance. To address this, we propose a co-encryption design that leverages underutilized GPU resources, optimizes encryption and authentication, and introduces a communication algorithm tailored for confidential settings. We evaluate our design using real ML workloads and execution traces collected from four HGX H100/H200 clusters. While CC mode was not available on current NVIDIA software stacks, we incorporate encryption-aware modeling based on hardware specifications to estimate secure communication overheads. Our results demonstrate a 40–70% reduction in communication-related security costs.

## 中文摘要

机器学习（ML）已成为众多应用的基石，由此需要安全高效的分布式 ML 框架。但在用户数据与模型参数须在 GPU 间频繁传输的分布式环境中维护数据隐私极具挑战。NVIDIA 机密计算（CC）模式等机密 GPU 计算技术提供了基于硬件的企业级方案，在不受信环境（如公有云）中保护 ML 负载，其依托将机密虚拟机（CVM）与 GPU 可信执行环境（TEE）结合的异构系统。然而机密计算因复杂异构架构与跨 TEE 安全边界的高吞吐数据流而开销可观：加密通信既发生在 CVM 与 GPU TEE 之间，也发生在多个 GPU TEE 之间，相比原生 PCIe 或 NVLink 等高速互连造成显著时延。我们的大规模评估表明，这些开销在集合通信操作中尤为严重，加密时延损害了端到端训练性能。为此我们提出协同加密设计，利用未被充分利用的 GPU 资源，优化加密与认证，并引入面向机密场景的通信算法。我们使用真实 ML 负载与四个 HGX H100/H200 集群的执行轨迹评估；因当前 NVIDIA 软件栈不提供 CC 模式，我们基于硬件规格做加密感知建模以估计安全通信开销。结果表明通信相关安全成本降低 40–70%。
