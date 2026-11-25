---
title: "Endeavor: Efficient PairHMM for Detection of DNA Variants in Genome-Scale Datasets"
description: "HPDC 2026 · Session 5 — Scientific Applications at Scale"
tags:
  - "HPDC2026"
  - "Session 5"
  - "Scientific Applications at Scale"
---

# Endeavor: Efficient PairHMM for Detection of DNA Variants in Genome-Scale Datasets

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 5 — Scientific Applications at Scale（2026年7月15日 10:20–11:20 · Session Chair：Michael Papka）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 5</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807593)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#GracaI26](https://dblp.org/db/conf/hpdc/hpdc2026.html#GracaI26)

**作者**：Miguel Graça, Aleksandar Ilic

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 5 — Scientific Applications at Scale（2026年7月15日 10:20–11:20 · Session Chair：Michael Papka）

---

## 英文摘要

DNA variant calling represents a key operation in bioinformatics pipelines that aims at identifying genetic variants. Given an evidenced explosion in genomic data availability, there is an urgent need for a high-performant, portable and efficient solution for variant calling, which can further improve our understanding of genomic structure and genetic basis for complex diseases. In its most common formulation, the Pair Hidden Markov Model (PairHMM) algorithm for variant calling stands as the main bottleneck in the pipeline, accounting for up to 70% of the execution time in large-scale genomic datasets. The state-of-the-art approaches for accelerating PairHMM in CPUs and GPUs do not scale to long DNA sequences and only explore very limited anti-diagonal data parallelism, which yields poor performance. In this work, Endeavor is proposed as a new parallelization strategy for PairHMM that redefines its traditional formulation to explore row-level fine-grained parallelism without loss in solution accuracy. Based on this, a novel and portable SIMD-based approach is derived for efficient and high-performance processing of short and long sequences in CPUs and GPUs, leveraging novel levels of parallelism and synchronization to achieve high throughput in sequences up to 100k basepairs for the first time. Evaluation on Intel and AMD CPUs shows that Endeavor outperforms GKL up to 2.14x in peak throughput and GATK HaplotypeCaller by at least 2x in real-world datasets, while NVIDIA and AMD GPUs achieve up to 2.05x speedups in genome-scale datasets when compared to state-of-the-art GPU-based methods.

## 中文摘要

DNA 变异检测是生物信息学流水线中的一项关键操作，旨在识别遗传变异。鉴于基因组数据可得性的爆发式增长，迫切需要高性能、可移植且高效的变异检测方案，以进一步加深我们对基因组结构以及复杂疾病遗传基础的理解。在最常见的表述中，用于变异检测的成对隐马尔可夫模型（PairHMM）算法是流水线中的主要瓶颈，在大规模基因组数据集中占执行时间高达 70%。在 CPU 和 GPU 上加速 PairHMM 的最先进方法无法扩展到长 DNA 序列，且只探索了非常有限的反对角线数据并行性，性能不佳。在本工作中，我们提出 Endeavor，一种新的 PairHMM 并行化策略，它重新定义传统表述，在不损失解精度的前提下探索行级细粒度并行性。基于此，推导出一种新颖且可移植的基于 SIMD 的方法，用于在 CPU 和 GPU 上高效、高性能地处理短序列与长序列，利用新的并行与同步层次，首次在长达 10 万个碱基对的序列上实现高吞吐。在 Intel 与 AMD CPU 上的评估表明，Endeavor 的峰值吞吐相比 GKL 最高提升 2.14 倍，在真实数据集上相比 GATK HaplotypeCaller 至少提升 2 倍；而在基因组规模数据集上，相比最先进的基于 GPU 的方法，NVIDIA 与 AMD GPU 取得最高 2.05 倍加速。

## 英文关键词

Variant Calling, Parallel Computing, Bioinformatics

## 中文关键词

变异检测，并行计算，生物信息学

---

[← 返回 Session 5 — Scientific Applications at Scale](index.md)
