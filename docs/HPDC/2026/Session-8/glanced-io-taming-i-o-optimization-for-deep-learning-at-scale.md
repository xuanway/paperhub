---
title: "GLANCED-IO: Taming I/O Optimization for Deep Learning at Scale"
description: "HPDC 2026 · Session 8 — Storage & I/O for Data-Intensive Workloads"
tags:
  - "HPDC2026"
  - "Session 8"
  - "Storage & I/O for Data-Intensive Workloads"
---

# GLANCED-IO: Taming I/O Optimization for Deep Learning at Scale

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2026 主会 Session 8 — Storage & I/O for Data-Intensive Workloads（2026年7月15日 14:40–15:40 · Session Chair：Sarah Neuwirth）。</p>
<p class="paper-seo-summary__tags">HPDC 2026 · Session 8</p>
</div>

**官方资料：** [HPDC 2026 官方议程](https://hpdc.sci.utah.edu/2026/program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3806645.3807588)

**DBLP**：[https://dblp.org/db/conf/hpdc/hpdc2026.html#SinuratNCZMFARG26](https://dblp.org/db/conf/hpdc/hpdc2026.html#SinuratNCZMFARG26)

**作者**：Ray A. O. Sinurat, William Nixon, Philip Carns, Huihuo Zheng, Sandeep Madireddy, Sam Foreman, Troy Arcomano, Robert Ross, Haryadi S. Gunawi, Hariharan Devarajan

**会议**：HPDC 2026 · Cleveland, OH, USA

**Session**：Session 8 — Storage & I/O for Data-Intensive Workloads（2026年7月15日 14:40–15:40 · Session Chair：Sarah Neuwirth）

---

## 英文摘要

Scientific deep learning (DL) at scale typically trains on terabyte-scale datasets across thousands of accelerators, placing immense pressure on storage systems to keep pace with computation. Existing solutions respond to this demand by tuning individual I/O parameters to accelerate training performance. However, these techniques are limited by costly experiments, configuration space explosion, and inability to generalize application-specific optimizations. This leads to applications running with suboptimal configurations that reduce training efficiency, system utilization, or both. To address the challenge of finding the optimal configuration efficiently, we developed GLANCED-IO, a cross-layer I/O optimization framework that optimizes DL pipelines with high-fidelity approximation and efficient configuration space exploration. Through this work, we identified the following three key findings. First, independently optimizing either the application or system configurations leaves up to 2.4× performance on the table for scientists to efficiently run DL pipelines on HPC systems. Second, GLANCED-IO’s one-factor-at-a-time (OFAT)-guided greedy exploration strategy achieved results comparable to more-expensive autotuning techniques while removing the pre-training required by ML-based approaches. Third, GLANCED-IO avoids executing the full application during optimization by operating on representative data subsets without GPUs, yet preserves 93% performance fidelity on average when deployed in DL pipelines. We demonstrate the efficacy of GLANCED-IO by optimizing large-scale global weather forecasting DL workloads, achieving up to 1.57× better performance than state-of-the-art with 2.3× fewer configuration evaluations than AIIO and 3.3× faster optimization than DeepHyper.

## 中文摘要

大规模科学深度学习（DL）通常要在数千个加速器上基于 TB 级数据集训练，给存储系统带来跟上计算步伐的巨大压力。现有方案通过调优单个 I/O 参数来加速训练性能。然而，这些技术受限于昂贵的实验、配置空间爆炸以及无法泛化应用特定优化，导致应用以次优配置运行，降低训练效率、系统利用率或两者兼有。为高效寻找最优配置，我们开发了 GLANCED-IO，一个跨层 I/O 优化框架，通过高保真近似和高效配置空间探索来优化 DL 流水线。通过这项工作，我们得到以下三点关键发现。第一，独立优化应用或系统配置，会使科学家在 HPC 系统上高效运行 DL 流水线时最多损失 2.4 倍的性能。第二，GLANCED-IO 的单因子（OFAT）引导的贪心探索策略取得了与更昂贵的自动调优技术相当的结果，同时免除了基于机器学习方法所需的前期训练。第三，GLANCED-IO 在优化过程中通过在不使用 GPU 的情况下对代表性数据子集进行操作，避免执行完整应用，但在部署于 DL 流水线时平均仍保持 93% 的性能保真度。我们通过优化大规模全球天气预报 DL 负载证明了 GLANCED-IO 的有效性，相比最先进方法取得最高 1.57 倍的性能提升，配置评估次数比 AIIO 少 2.3 倍，优化速度比 DeepHyper 快 3.3 倍。

## 英文关键词

GLANCED-IO, Deep Learning, I/O Optimization, Autotuning, Joint Metric, Proxy Approximation, OFAT, DFTracer, DLIO

## 中文关键词

GLANCED-IO，深度学习，I/O 优化，自动调优，联合指标，代理近似，OFAT，DFTracer，DLIO

---

[← 返回 Session 8 — Storage & I/O for Data-Intensive Workloads](index.md)
