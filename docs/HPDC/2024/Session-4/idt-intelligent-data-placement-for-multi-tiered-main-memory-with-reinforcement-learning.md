---
title: "IDT: Intelligent Data Placement for Multi-tiered Main Memory with Reinforcement Learning"
description: "HPDC 2024 · Session 4 — Software Systems & Workflows"
tags:
  - "HPDC2024"
  - "Session 4"
  - "Software Systems & Workflows"
---

# IDT: Intelligent Data Placement for Multi-tiered Main Memory with Reinforcement Learning

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPDC 2024 主会 Session 4 — Software Systems & Workflows（2024年6月6日 11:45–13:00 · Session Chair：Massimo Coppola）。</p>
<p class="paper-seo-summary__tags">HPDC 2024 · Session 4</p>
</div>

**官方资料**：[HPDC 2024 官方议程](https://hpdc.sci.utah.edu/2024/program.html) · [ACM DOI](https://doi.org/10.1145/3625549.3658659)

**作者**：Juneseo Chang, Wanju Doh, Yaebin Moon, Eojin Lee, Jung Ho Ahn

**会议**：HPDC 2024 · Pisa, Italy

**Session**：Session 4 — Software Systems & Workflows（2024年6月6日 11:45–13:00 · Session Chair：Massimo Coppola）

---

## 英文摘要

To address the limitation of a DRAM-based single-tier in satisfying the comprehensive demands of main memory, multi-tiered memory systems are gaining widespread adoption. To support these systems, operating-system-level solutions that analyze the application’s memory access patterns and ensure data placement in the appropriate memory tier have been vastly explored. In this paper, we identify reinforcement learning (RL) as an effective solution for tiered memory management, and its policy can be formulated in a solvable form using RL. We also demonstrate that an effective region-granularity memory access monitoring method is necessary to provide an accurate environment state to the RL model. Thus, we propose IDT, an intelligent data placement for multi-tiered main memory. IDT incorporates an RL-based demotion policy autotuning and a mechanism that efficiently demotes cold pages to lower-tier memory. IDT also promotes hot pages to upper-tier memory to minimize access on slow memory, featuring a lightweight machine learning algorithm. IDT employs region-granularity memory access monitoring with statistical-testing-based adjacent region merge and split to improve precision and mitigate ambiguity observed in prior works. Experiments on an actual four-tiered memory system show that IDT achieves an average 2.08× speedup over the default Linux kernel and 11.2% performance improvement compared to the state-of-the-art solution.

## 中文摘要

为突破基于 DRAM 的单层内存难以满足主存综合需求的局限，多层内存系统正被广泛采用。为支持这些系统，已有大量研究探索操作系统级方案，通过分析应用的内存访问模式并确保数据放置到合适的内存层。本文确认强化学习（RL）是分层内存管理的有效方案，且其策略可用 RL 表述为可求解形式。我们还证明，有效的区域粒度内存访问监控方法对于为 RL 模型提供准确的环境状态十分必要。因此，我们提出 IDT，一种面向多层主存的智能数据放置方案。IDT 包含基于 RL 的降级策略自动调优，以及一种将冷页面高效降级到低层内存的机制。IDT 还将热页面提升到上层内存以最小化对慢速内存的访问，并采用轻量级机器学习算法。IDT 采用区域粒度内存访问监控，通过基于统计检验的相邻区域合并与拆分来提升精度，并缓解先前工作中观察到的歧义。在真实的四层内存系统上的实验表明，IDT 相比默认 Linux 内核平均加速 2.08 倍，相比最先进方案性能提升 11.2%。

## 英文关键词

Memory Tiering, Emerging Memory Technologies, Memory Management, Reinforcement Learning

## 中文关键词

内存分层，新兴内存技术，内存管理，强化学习

---

[← 返回 Session 4 — Software Systems & Workflows](index.md)
