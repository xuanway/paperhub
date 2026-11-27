---
title: "The Last-Level Branch Predictor Revisited"
description: "HPCA 2026 · CPU Microarchitecture Optimization"
tags:
  - "HPCA2026"
  - "CPU Microarchitecture Optimization"
---

# The Last-Level Branch Predictor Revisited

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: CPU Microarchitecture Optimization。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · CPU Microarchitecture Optimization</p>
</div>

**论文链接**：
**作者**：David Schall Technical University of Munich , Mária Ďuračková University Of Edinburgh , Boris Grot University of Edinburgh, UK
**会议**：HPCA 2026

---

## 中文标题

末级分支预测器再审视

## 英文摘要

Branch prediction is critical for high-performance CPUs, with mispredictions causing significant execution inefficiencies. Modern server workloads exacerbate the challenge due to expanding instruction and branch working sets, while predictor capacities remain limited to avoid latency increases. A recently introduced hierarchical branch predictor design, LLBP, demonstrated a way to reduce misprediction rates by augmenting an unmodified TAGE-based predictor with a decoupled highcapacity metadata store. Despite using a large amount of storage, LLBP was shown to achieve only a fraction of the accuracy gain of an equal-sized (but impractical) TAGE-based predictor. This work provides a detailed analysis of LLBP, identifying sources of its accuracy loss. Chief among these are contention within certain sets of LLBP’s high-capacity metadata store (namely those containing patterns for hard-to-predict branches), as well as duplication of patterns, which leads to prolonged training time. To address these issues, we propose dynamic context depth adaptation, an enhancement to the original LLBP design, which yields a significantly better distribution of patterns for hard-to-predict branches, thereby reducing both pattern set contention and pattern duplication. Our proposed design that realizes dynamic context depth adaptation requires only small modifications to the baseline LLBP while increasing its accuracy by 0.8–11.5% (average 3.6%).

## 中文摘要

分支预测对高性能 CPU 至关重要，预测错误会造成严重的执行低效。现代服务器负载中指令与分支工作集不断扩大，而预测器容量为避免时延上升只能保持有限，这进一步加剧了挑战。近期提出的层次化分支预测器设计 LLBP 表明，可在未修改的 TAGE 预测器上增加解耦的大容量元数据存储，以降低预测错误率。尽管使用了大量存储，LLBP 所获精度增益仅为同等容量（但不实用）的 TAGE 预测器的一小部分。本文对 LLBP 做详细分析，找出其精度损失来源。其中最主要的是 LLBP 大容量元数据存储中某些集合内部的冲突，即包含难以预测分支模式的集合，以及模式重复，后者导致训练时间延长。为解决这些问题，我们提出动态上下文深度自适应，这是对原始 LLBP 设计的增强，可为难以预测的分支提供显著更优的模式分布，从而同时减少模式集合冲突与模式重复。实现动态上下文深度自适应只需对基线 LLBP 做小幅修改，即可将其精度提升 0.8–11.5%（平均 3.6%）。
