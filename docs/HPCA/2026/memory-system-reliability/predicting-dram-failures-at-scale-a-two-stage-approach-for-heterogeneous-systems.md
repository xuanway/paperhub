---
title: "Predicting DRAM Failures at Scale: A Two-Stage Approach for Heterogeneous Systems"
description: "HPCA 2026 · Memory System Reliability"
tags:
  - "HPCA2026"
  - "Memory System Reliability"
---

# Predicting DRAM Failures at Scale: A Two-Stage Approach for Heterogeneous Systems

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Memory System Reliability。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Memory System Reliability</p>
</div>

**论文链接**：
**作者**：Chenglin Wang Xiamen University , Shouxin Wang Xiamen University , Shuyue Zhou Xiamen University , Ronglong Wu Xiamen University , Zhirong Shen Xiamen University , Lu Tang Xiamen University , Yiming Zhang Xiamen University , Jialiang Yu Huawei , Min Zhou Huawei
**会议**：HPCA 2026

---

## 中文标题

大规模 DRAM 故障预测：面向异构系统的两阶段方法

## 英文摘要

Memory failures in large-scale production environments pose critical threats to system reliability and service availability. While existing studies have conducted in-depth analyses of the temporal and spatial correlations of memory errors, differences in characteristics across architectures remain largely unexplored. To uncover these overlooked correlations, this paper conducts an extensive analysis of over 130,000 DDR4 DIMMs collected from large-scale heterogeneous production clusters over a nine-month period. Through systematic spatial and temporal analysis across two Intel x86 architectures and four major DRAM vendors, we uncover five new findings and propose a novel two-stage training strategy. This strategy addresses sample quality issues by applying temporal weighting to positive samples and adaptive reweighting to negative samples. It also incorporates comprehensive multi-dimensional feature engineering, covering static, spatial, temporal, and micro-level characteristics. Finally, it integrates dual-driven sampling strategies and adaptive prediction timing to balance prediction accuracy and operational efficiency. Extensive evaluation shows that our CatBoost-based model achieves F1-scores of 49.9% on Intel x86v5 and 57.6% on Intel x86v6, substantially outperforming existing methods. This cross-architecture validation demonstrates the robustness and generalization of our approach across different hardware platforms. To the best of our knowledge, our work presents the first large-scale cross-architecture analysis of memory error patterns and provides new insights for production-scale memory failure prediction systems.

## 中文摘要

大规模生产环境中的内存故障严重威胁系统可靠性与服务可用性。已有研究对内存错误的时间与空间相关性进行了深入分析，但不同体系结构之间的特征差异仍基本未被探索。为揭示这些被忽视的相关性，本文对来自大规模异构生产集群、覆盖九个月采集的 13 万多条 DDR4 DIMM 数据进行了广泛分析。通过对两种 Intel x86 架构和四家主要 DRAM 供应商开展系统的空间与时间分析，我们发现五个新现象，并提出一种新颖的两阶段训练策略。该策略对正样本施加时间加权、对负样本进行自适应重加权，以解决样本质量问题；同时引入覆盖静态、空间、时间与微观层面的多维度特征工程，并结合双驱动采样策略与自适应预测时机，在预测精度与运维效率之间取得平衡。大量评估表明，我们基于 CatBoost 的模型在 Intel x86v5 上取得 49.9%、在 Intel x86v6 上取得 57.6% 的 F1 分数，显著优于现有方法。这种跨架构验证体现了该方法在不同硬件平台上的鲁棒性与泛化能力。据我们所知，本工作是首个针对内存错误模式的大规模跨架构分析，并为生产规模的内存故障预测系统提供了新的洞见。
