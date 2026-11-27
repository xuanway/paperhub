---
title: "GenPairX: A Hardware-Algorithm Co-Designed Accelerator for Paired-End Read Mapping"
description: "HPCA 2026 · Genomics and Bioinformatics"
tags:
  - "HPCA2026"
  - "Genomics and Bioinformatics"
---

# GenPairX: A Hardware-Algorithm Co-Designed Accelerator for Paired-End Read Mapping

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Genomics and Bioinformatics。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Genomics and Bioinformatics</p>
</div>

**论文链接**：
**作者**：Julien Eudine Huawei Technologies Switzerland AG , Chu Li Huawei Zurich Research Center , Zhuo Cheng Huawei Zurich Research Center , Renzo Andri Huawei Technologies Switzerland AG , Onur Mutlu ETH Zurich , Can Firtina ETH Zurich and UMD , Mohammad Sadrosadati ETH Zürich , Nika Mansouri Ghiasi ETH Zurich , Konstantina Koliogeorgi ETH Zurich , Anirban Nag Huawei Zurich Research Center , Arash Tavakkol Huawei Zurich Research Center , Haiyu Mao King's College London , Shai Bergman Huawei Zurich Research Center , Ji Zhang Huawei Zurich Research Center
**会议**：HPCA 2026

---

## 中文标题

GenPairX：面向双端读段比对的硬件-算法协同设计加速器

## 英文摘要

Genome sequencing has become a central focus in computational biology due to its critical role in applications such as personalized medicine, disease outbreak tracking, and evolutionary research. A genome study typically begins with sequencing, which produces millions to billions of short DNA fragments known as reads. Extracting meaningful biological insights from these reads requires a computationally intensive step called read mapping, where each read is aligned to a reference genome. Read mapping for short reads comes in two forms: single-end and paired-end, with the latter being more prevalent due to its higher accuracy and support for advanced analysis. Read mapping remains a major performance bottleneck in genome analysis as a result of the extensive use of computationally intensive dynamic programming. Prior efforts have attempted to mitigate this cost by employing filters to identify and potentially discard computationally expensive matches and leveraging hardware accelerators to speed up the computations. While partially effective, these approaches have limitations. In particular, existing filters are often ineffective for paired-end reads, as they evaluate each read independently and exhibit relatively low filtering ratios. In this work, we propose GenPairX, a hardware-algorithm co-designed accelerator that efficiently minimizes the computational load of paired-end read mapping while enhancing the throughput of memory-intensive operations. GenPairX introduces: (1) a novel filtering algorithm that jointly considers both reads in a pair to improve filtering effectiveness, and a lightweight alignment algorithm to replace most of the computationally expensive dynamic programming operations, and (2) two specialized hardware mechanisms to support the proposed algorithms. The proposed hardware addresses the high memory bandwidth demands of the read filtering process via orchestration of memory accesses over high-bandwidth memory channels, and accelerates the alignment of candidate reads via simple vectorized logical XOR operators. Our evaluations show that GenPairX delivers substantial performance improvements over state-of-the-art solutions, achieving 1575× and 1.43× higher throughput per watt compared to leading CPU-based and accelerator-based read mappers, respectively, all without compromising accuracy.

## 中文摘要

基因组测序因在个性化医疗、疾病爆发追踪与演化研究中的关键作用，已成为计算生物学的核心关注点。一项基因组研究通常从测序开始，产生数百万至数十亿条称为读段的短 DNA 片段；要从这些读段中提取有意义的生物学洞见，需要计算密集的读段比对，即将每条读段与参考基因组对齐。短读段比对分为单端与双端两种形式，后者因精度更高并支持高级分析而更为普遍。由于大量使用计算密集的动态规划，读段比对仍是基因组分析的主要性能瓶颈。此前工作尝试用过滤器识别并丢弃计算代价高昂的匹配、以硬件加速器加快计算来缓解该开销，但现有过滤器对双端读段常无效：它们独立评估每条读段，过滤率相对较低。本文提出 GenPairX，一种硬件-算法协同设计的加速器，在降低双端读段比对计算负载的同时提升访存密集型操作的吞吐。GenPairX 引入：(1) 联合考虑一对中两条读段的新型过滤算法，以及替换大部分高代价动态规划操作的轻量级对齐算法；(2) 两种支撑上述算法的专用硬件机制，通过在高带宽存储通道上编排访存来满足读段过滤的高带宽需求，并用简单的向量化逻辑 XOR 运算加速候选读段的对齐。评估表明，相比领先的基于 CPU 与基于加速器的读段比对器，GenPairX 的每瓦吞吐分别提升 1575 倍和 1.43 倍，且不损失精度。
