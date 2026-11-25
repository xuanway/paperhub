---
title: "Faster and Cheaper: Pushing the Sequence Alignment Throughput with Commercial CPUs"
description: "PPoPP 2026 Session 9（Parallel Algorithms）：商用 CPU 上吞吐提升 2.27–3.28×、成本降低 2.54–5.65×"
tags:
  - "PPoPP2026"
  - "Session-9"
  - "Parallel Algorithms"
  - "Sequence Alignment"
  - "SIMD"
  - "Seed Extension"
authors:
  - "Zhonghai Zhang"
  - "Yewen Li"
  - "Ke Meng"
  - "Chunming Zhang"
  - "Guangming Tan"
session: "Session 9: Parallel Algorithms"
session_number: 9
session_chair: "Kenjiro Taura"
date: "2026-02-03"
time: "14:50–15:10"
room: "Pyrmont"
doi: "10.1145/3774934.3786421"
program_url: "https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program"
---

# Faster and Cheaper: Pushing the Sequence Alignment Throughput with Commercial CPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">提出 FastAlign，面向商用 CPU 的端到端序列比对方案，用多级种子算法与查询内并行种子扩展提升吞吐、消除冗余，输出与 BWA-MEM 完全一致。</p>
<p class="paper-seo-summary__tags">PPoPP 2026 · Session 9: Parallel Algorithms</p>
</div>

**作者**：Zhonghai Zhang, Yewen Li, Ke Meng, Chunming Zhang, and Guangming Tan — Institute of Computing Technology at Chinese Academy of Sciences, China; University of Chinese Academy of Sciences, China; Hong Kong University of Science and Technology, China; Phil Rivers Technology, China

**会议**：PPoPP 2026 · 2026 年 2 月 3 日 14:50–15:10 · Session 9: Parallel Algorithms（主席：Kenjiro Taura）· Pyrmont

**论文**：[ACM Digital Library](https://doi.org/10.1145/3774934.3786421) · [PPoPP 2026 会议日程](https://ppopp26.sigplan.org/track/PPoPP-2026-papers#program)

---

## 英文摘要

This paper proposes FastAlign, a faster, cheaper, and practical end-to-end solution for sequence alignment using commercial CPUs. It introduces two key innovations: a multi-stage seeding algorithm that improves search performance while maintaining low memory consumption, and an intra-query parallel seed-extension algorithm that eliminates redundancy and increases SIMD utilization. Evaluation results show that FastAlign achieves 2.27× ∼3.28× throughput speedup and 2.54× ∼5.65× cost reduction compared to state-of-the-art CPU and GPU baselines while guaranteeing 100% identical output to the de facto software BWA-MEM. FastAlign is open-sourced at https://github.com/zzhofict/BWA-FastAlign.git.

## 中文摘要

本文提出 FastAlign，一个使用商用 CPU 的更快、更经济且实用的端到端序列比对解决方案。它包含两项关键创新：一种在保持低内存占用的同时提升搜索性能的多阶段种子（seeding）算法，以及一种消除冗余并提高 SIMD 利用率的查询内并行种子扩展算法。评估结果表明，在保证与事实标准软件 BWA-MEM 输出 100% 一致的前提下，FastAlign 相比最先进的 CPU 与 GPU 基线取得 2.27×～3.28× 的吞吐加速和 2.54×～5.65× 的成本降低。FastAlign 已在 https://github.com/zzhofict/BWA-FastAlign.git 开源。

## 英文关键词

Computational Genomics, Next-Generation Sequencing, Sequence Alignment, Parallel System

## 中文关键词

计算基因组学；下一代测序；序列比对；并行系统

---

## 一句话总结

> 提出 FastAlign，面向商用 CPU 的端到端序列比对方案，用多级种子算法与查询内并行种子扩展提升吞吐、消除冗余，输出与 BWA-MEM 完全一致。

## 研究问题

序列比对需要更快、更便宜的实用端到端方案；现有实现难以在保持输出正确一致的前提下同时提升吞吐与降低硬件成本。

## 方法简述

- 提出多级种子（multi-stage seeding）算法，在提升搜索性能的同时保持较低内存占用。
- 设计查询内并行的种子扩展算法，消除冗余并提高 SIMD 利用率。
- 构建基于商用 CPU 的端到端比对方案，保证与事实标准 BWA-MEM 输出一致。

## 主要结果

- 相比最先进的 CPU 与 GPU 基线，吞吐提升 2.27×–3.28×，成本降低 2.54×–5.65×。
- 保证与 BWA-MEM 输出 100% 完全相同。

---

> 所属 Session：[Session 9: Parallel Algorithms](index.md) · 返回 [PPoPP 2026 总览](../index.md)
