---
title: "SAGe: A Lightweight Algorithm-Architecture Co-Design for Mitigating the Data Preparation Bottleneck in Large-Scale Genome Sequence Analysis"
description: "HPCA 2026 · Genomics and Bioinformatics"
tags:
  - "HPCA2026"
  - "Genomics and Bioinformatics"
---

# SAGe: A Lightweight Algorithm-Architecture Co-Design for Mitigating the Data Preparation Bottleneck in Large-Scale Genome Sequence Analysis

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Genomics and Bioinformatics。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Genomics and Bioinformatics</p>
</div>

**论文链接**：
**作者**：Nika Mansouri Ghiasi ETH Zurich , Talu Güloglu ETH Zurich , Harun Mustafa ETH Zurich and Johns Hopkins University , Can Firtina ETH Zurich and UMD , Konstantina Koliogeorgi ETH Zurich , Konstantinos Kanellopoulos ETH Zurich , Haiyu Mao King's College London , Rakesh Nadig ETH Zurich , Mohammad Sadrosadati ETH Zürich , Jisung Park POSTECH (Pohang University of Science and Technology) , Onur Mutlu ETH Zurich
**会议**：HPCA 2026

---

## 中文标题

SAGe：缓解大规模基因组序列分析数据准备瓶颈的轻量级算法-架构协同设计

## 英文摘要

Genome sequence analysis, which examines the DNA sequences of organisms, drives advances in many critical medical and biotechnological fields. Given its importance and the exponentially growing volumes of genomic sequence data, there are extensive efforts to accelerate genome sequence analysis. In this work, we demonstrate a major bottleneck that greatly limits and diminishes the benefits of state-of-the-art genome sequence analysis accelerators: the data preparation bottleneck, where genomic sequence data is stored in compressed form and needs to be first decompressed and formatted before an accelerator can operate on it. To mitigate this bottleneck, we propose SAGe, an algorithm-architecture co-design for highly-compressed storage and high-performance access of large-scale genomic sequence data. The key challenge is to improve data preparation performance while maintaining high compression ratios (comparable to genomic-specific compression algorithms) at low hardware cost. We address this challenge by leveraging key properties of genomic datasets to co-design (i) a lossless (de)compression algorithm, (ii) hardware that decompresses data with lightweight operations and efficient streaming accesses, (iii) storage data layout, and (iv) interface commands to access data. SAGe is highly versatile, as it supports datasets from different sequencing technologies and species. Due to its lightweight design, SAGe can be seamlessly integrated with a broad range of hardware accelerators for genome sequence analysis to mitigate their data preparation bottlenecks. Our results demonstrate that SAGe improves the average end-to-end performance and energy efficiency of two state-of-the-art genome sequence analysis accelerators by 3.0×–32.1× and 13.0×–34.0×, respectively, compared to when the accelerators rely on state-of-the-art software and hardware decompression tools.

## 中文摘要

基因组序列分析通过考察生物的 DNA 序列，推动了许多关键医学与生物技术领域的进步。鉴于其重要性以及指数增长的基因组序列数据量，已有大量工作致力于加速基因组序列分析。本文指出一个严重限制并削弱最先进基因组序列分析加速器收益的主要瓶颈：数据准备瓶颈，即基因组序列数据以压缩形式存储，必须先解压并格式化，加速器才能对其运算。为缓解该瓶颈，本文提出 SAGe，一种面向大规模基因组序列数据高压缩存储与高性能访问的算法-架构协同设计。关键挑战在于：在保持高压缩比（可与基因组专用压缩算法媲美）的同时提升数据准备性能，且硬件开销要低。我们利用基因组数据集的关键特性，协同设计 (i) 无损（解）压缩算法，(ii) 以轻量操作和高效流式访问解压数据的硬件，(iii) 存储数据布局，以及 (iv) 访问数据的接口命令。SAGe 通用性强，支持来自不同测序技术与物种的数据集。得益于轻量设计，SAGe 可与广泛的基因组序列分析硬件加速器无缝集成，缓解其数据准备瓶颈。结果表明，相比加速器依赖最先进的软件与硬件解压工具的情形，SAGe 将两个最先进基因组序列分析加速器的平均端到端性能与能效分别提升 3.0 倍–32.1 倍和 13.0 倍–34.0 倍。
