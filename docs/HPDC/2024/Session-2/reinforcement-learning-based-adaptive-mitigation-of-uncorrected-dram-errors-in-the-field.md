---
title: "Reinforcement Learning-based Adaptive Mitigation of Uncorrected DRAM Errors in the Field"
description: "HPDC 2024 · Session 2 — Resilience"
tags:
  - "HPDC2024"
  - "Session 2"
  - "Resilience"
---

# Reinforcement Learning-based Adaptive Mitigation of Uncorrected DRAM Errors in the Field

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2024 主会 Session 2 — Resilience（2024年6月5日 14:00–15:15 · Session Chair：Changhee Jung）。</p>
<p class="paper-seo-summary__tags">HPDC 2024 · Session 2</p>
</div>

**官方资料**：[HPDC 2024 官方议程](https://hpdc.sci.utah.edu/2024/program.html) · [ACM DOI](https://doi.org/10.1145/3625549.3658686)

**作者**：Isaac Boixaderas, Sergi Moré, Javier Bartolome, David Vicente, Petar Radojković, Paul M. Carpenter, Eduard Ayguadé

**会议**：HPDC 2024 · Pisa, Italy

**Session**：Session 2 — Resilience（2024年6月5日 14:00–15:15 · Session Chair：Changhee Jung）

---

## 英文摘要

Scaling to larger systems, with current levels of reliability, requires cost-effective methods to mitigate hardware failures. One of the main causes of hardware failure is an uncorrected error in memory, which terminates the current job and wastes all computation since the last checkpoint. This paper presents the first adaptive method for triggering uncorrected error mitigation. It uses a prediction approach that considers the likelihood of an uncorrected error and its current potential cost. The method is based on reinforcement learning, and the only user-defined parameters are the mitigation cost and whether the job can be restarted from a mitigation point. We evaluate our method using classical machine learning metrics together with a cost–benefit analysis, which compares the cost of mitigation actions with the benefits from mitigating some of the errors. On two years of production logs from the MareNostrum supercomputer, our method reduces lost compute time by 54% compared with no mitigation and is just 6% below the optimal Oracle method. All source code is open source.

## 中文摘要

以当前的可靠性水平扩展到更大规模系统，需要经济有效的方法来缓解硬件故障。硬件故障的主要原因之一是内存中的未纠正错误，它会终止当前作业并浪费自上次检查点以来的全部计算。本文提出首个用于触发未纠正错误缓解的自适应方法。它采用一种预测方法，同时考虑未纠正错误的可能性及其当前潜在代价。该方法基于强化学习，仅有的用户自定义参数是缓解代价以及作业能否从缓解点重启。我们使用经典机器学习指标并结合成本-收益分析来评估该方法，将缓解行动的成本与缓解部分错误所带来的收益进行比较。在 MareNostrum 超级计算机两年的生产日志上，与不缓解相比，我们的方法将损失的算时减少 54%，仅比最优 Oracle 方法低 6%。所有源代码均已开源。

## 英文关键词

Memory system, Reliability, Error prediction, Machine learning, Reinforcement learning, Cost–benefit analysis.

## 中文关键词

内存系统，可靠性，错误预测，机器学习，强化学习，成本-收益分析。

---

[← 返回 Session 2 — Resilience](index.md)
