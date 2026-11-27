---
title: "Anaheim: Architecture and Algorithms for Processing Fully Homomorphic Encryption in Memory"
description: "HPCA 2025 · The Poker Face of FHE"
tags:
  - "HPCA2025"
  - "The Poker Face of FHE"
---

# Anaheim: Architecture and Algorithms for Processing Fully Homomorphic Encryption in Memory

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: The Poker Face of FHE。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · The Poker Face of FHE</p>
</div>

**论文链接**：
**作者**：Jongmin Kim (Seoul National University), Sungmin Yun (Seoul National University), Hyesung Ji (Seoul National University), Wonseok Choi (Seoul National University), Sangpyo Kim (Seoul National University), Jung Ho Ahn (Seoul National University)
**会议**：HPCA 2025

---

## 中文标题

Anaheim：面向内存内全同态加密处理的架构与算法

## 英文摘要

Fully homomorphic encryption (FHE) is a promising solution for privacy-preserving cloud computing as it enables computations on sensitive data without any risk of data leakage. Despite the significant attention FHE has received, substantial computation and memory demands make it hardly practical for real-world applications. We propose a readily available and practical hardware solution to tackle this problem by using GPUs. GPUs have adequate computational and memory resources to handle complex operations in FHE, including number-theoretic transform (NTT), on which most prior work has deeply focused. However, through detailed analyses, we discover that the performance bottleneck on GPUs is primarily due to simpler element-wise operations, which are limited by off-chip memory (DRAM) bandwidth. Motivated by these observations, we develop Anaheim, a processing-in-memory (PIM) architecture for FHE. We develop optimized FHE execution flows and an end-to-end software framework for using PIM with GPUs. Also, we design a versatile PIM unit that handles various modular integer arithmetic PIM instructions, along with an efficient data mapping and associated PIM execution algorithms that minimize data access overhead by leveraging the internal structure of DRAM. Our concerted efforts substantially enhance the performance and energy efficiency of various FHE workloads on GPUs.

## 中文摘要

全同态加密（FHE）是隐私保护云计算的一种很有前景的解决方案，它使得无需担心数据泄露即可对敏感数据进行计算。尽管 FHE 已获得大量关注，但巨大的计算与内存需求使其难以用于实际应用。我们提出一种易获得且实用的硬件方案，即使用 GPU 来解决该问题。GPU 具有足够的计算与内存资源来处理 FHE 中的复杂操作，包括此前大多数工作深入聚焦的数论变换（NTT）。然而通过详细分析，我们发现 GPU 上的性能瓶颈主要源于更简单的逐元素操作，这些操作受限于片外内存（DRAM）带宽。受这些观察启发，我们设计了 Anaheim，一种面向 FHE 的存内处理（PIM）架构。我们开发了优化的 FHE 执行流程，以及一套在 GPU 上使用 PIM 的端到端软件框架。此外，我们设计了一个通用 PIM 单元来处理各种模整数运算 PIM 指令，并给出高效的数据映射及相应的 PIM 执行算法，通过利用 DRAM 的内部结构来最小化数据访问开销。我们的协同努力显著提升了 GPU 上各类 FHE 负载的性能与能效。
