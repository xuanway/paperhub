---
title: "NP-CAM: Efficient and Scalable DNA Classification using a NoC-Partitioned CAM Architecture"
description: "HPCA 2026 · Genomics and Bioinformatics"
tags:
  - "HPCA2026"
  - "Genomics and Bioinformatics"
---

# NP-CAM: Efficient and Scalable DNA Classification using a NoC-Partitioned CAM Architecture

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Genomics and Bioinformatics。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Genomics and Bioinformatics</p>
</div>

**论文链接**：
**作者**：Benjamin F. Morris III Duke University , Tergel Molom-Ochir Duke University , Changchun Zhou Duke University , Yiran Chen Duke University , Alex Jones Syracuse University , Hai "Helen" Li Duke University
**会议**：HPCA 2026

---

## 中文标题

NP-CAM：基于 NoC 分区 CAM 架构的高效可扩展 DNA 分类

## 英文摘要

The rapid advancement in genomic sequencing technologies has resulted in an explosion of data, creating substantial computational bottlenecks in DNA analysis workloads. Applications such as DNA classification are particularly impacted due to their reliance on intensive, large-scale pattern matching. Existing hardware accelerator and software solutions are increasingly unable to manage the scale and energy demands of these datasets, highlighting the need for architectures that can perform faster and more efficient pattern matching. To address these challenges, we propose NP-CAM: a data-optimized, CAM-based accelerator designed for parallel and energy-efficient DNA classification. NP-CAM harnesses a network-on-chip to implement a novel optimized indexing and CAM partitioning scheme that reduces the active search space, allowing significant scalability. We demonstrate results for NP-CAM on commodity 10T binary CAM cell designs. Our experimental evaluations show that NP-CAM achieves a simultaneous 65ˆ improvement in sequence throughput and an over 173ˆ improvement in energy efficiency over state-of-the-art hardware solutions on existing small viral workloads. We go on to demonstrate feasibility for larger bacterial and fungal workloads, enabling scalable DNA classification in the era of large-scale genomic data.

## 中文摘要

基因组测序技术的快速进步带来了数据爆炸，在 DNA 分析负载中造成显著的计算瓶颈。DNA 分类等应用因依赖密集的大规模模式匹配而尤受影响。现有硬件加速器与软件方案日益难以应对这些数据集的规模与能耗需求，凸显出能够更快、更高效执行模式匹配的架构的必要性。为应对这些挑战，本文提出 NP-CAM：一种面向数据优化、基于 CAM 的加速器，用于并行且高能效的 DNA 分类。NP-CAM 利用片上网络（NoC）实现新颖的优化索引与 CAM 分区方案，缩小活跃搜索空间，从而获得显著的可扩展性。我们在商用 10T 二元 CAM 单元设计上给出 NP-CAM 的结果。实验评估表明，在现有小型病毒负载上，相比最先进的硬件方案，NP-CAM 的序列吞吐提升 65 倍，能效提升超过 173 倍。我们进一步证明其在更大规模细菌与真菌负载上的可行性，从而在大规模基因组数据时代实现可扩展的 DNA 分类。
