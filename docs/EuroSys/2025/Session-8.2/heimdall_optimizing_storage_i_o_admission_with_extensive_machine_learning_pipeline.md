---
title: "Heimdall: Optimizing Storage I/O Admission with Extensive Machine Learning Pipeline"
description: "EuroSys 2025 · Storage · Daniar H. Kurniawan (University of Chicago and MangoBoost Inc.), Rani Ayu Putri "
tags:
  - "EuroSys2025"
  - "Storage"
---

# Heimdall: Optimizing Storage I/O Admission with Extensive Machine Learning Pipeline

**中文标题：** 利用广泛的机器学习流水线优化存储 I/O 准入

**所属 Session：** [Session 8.2: Storage](index.md) · [EuroSys 2025](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2025，所属方向：Storage。</p>
<p class="paper-seo-summary__tags">EuroSys 2025 · Storage</p>
</div>

**作者**：Daniar H. Kurniawan (University of Chicago and MangoBoost Inc.), Rani Ayu Putri (Bandung Institute of Technology and University of Chicago), Peiran Qin (University of Chicago), Kahfi S. Zulkifli (Bandung Institute of Technology), Ray A. O. Sinurat (University of Chicago), Janki Bhimani (Florida International University), Sandeep Madireddy (Argonne National Laboratory), Achmad Imam Kistijantoro (Bandung Institute of Technology), Haryadi Gunawi (University of Chicago)

**会议**：EuroSys 2025 · Rotterdam, Netherlands

**官方资料：** [EuroSys 2025 官方议程](https://2025.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3689031.3717496)

## 英文摘要

This paper introduces Heimdall, a highly accurate and efficient machine learning-powered I/O admission policy for flash storage, designed to operate in a black-box manner. We make domain-specific innovations in various ML stages by introducing accurate period-based labeling, 3-stage noise filtering, in-depth feature engineering, and fine-grained tuning, which together improve the decision accuracy from 67% up to 93%. We perform various deployment optimizations to reach a sub-µs inference latency and a small, 28KB, memory overhead. With 500 unbiased random experiments derived from production traces, we show Heimdall delivers 15-35% lower average I/O latency compared to the state of the art and up to 2× faster to a baseline. Heimdall is ready for user-level, in-kernel, and distributed deployments.

## 中文摘要

本文介绍 Heimdall，一种面向闪存存储的高精度、高效率、由机器学习驱动的 I/O 准入策略，设计上以黑盒方式运行。我们在机器学习的各个阶段进行了领域特定的创新，引入精确的基于周期的标注、三阶段噪声过滤、深入的特性工程以及细粒度调优，共同将决策准确率从 67% 提升至 93%。我们进行了多种部署优化，使推理延迟降至亚微秒级，内存开销仅 28KB。基于从生产 trace 中导出的 500 次无偏随机实验，我们表明 Heimdall 相比最先进方案将平均 I/O 延迟降低 15%–35%，相比基线最高快 2 倍。Heimdall 已可用于用户态、内核内以及分布式部署。

**英文关键词：** ML for systems; I/O admission control; File and storage systems; Operating systems; Distributed systems

**中文关键词：** 面向系统的机器学习、I/O 准入控制、文件与存储系统、操作系统、分布式系统

---

[返回 Session](index.md) · [EuroSys 2025 主页](../index.md)
