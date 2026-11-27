---
title: "DAPPER: A Performance-Attack-Resilient Tracker for RowHammer Defense"
description: "HPCA 2025 · Hammering the Odds"
tags:
  - "HPCA2025"
  - "Hammering the Odds"
---

# DAPPER: A Performance-Attack-Resilient Tracker for RowHammer Defense

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Hammering the Odds。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Hammering the Odds</p>
</div>

**论文链接**：
**作者**：Jeonghyun Woo (The University of British Columbia (UBC)), Prashant J. Nair (The University of British Columbia (UBC))
**会议**：HPCA 2025

---

## 中文标题

DAPPER：面向 Rowhammer 防御的抗性能攻击跟踪器

## 英文摘要

RowHammer vulnerabilities pose a significant threat to modern DRAM-based systems, where rapid activation of DRAM rows can induce bit-flips in neighboring rows. To mitigate this, state-of-the-art host-side RowHammer mitigations typically rely on shared counters or tracking structures. While these optimizations benefit benign applications, they are vulnerable to Performance Attacks (Perf-Attacks), where adversaries exploit shared structures to reduce DRAM bandwidth for co-running benign applications by increasing DRAM accesses for RowHammer counters or triggering repetitive refreshes required for the early reset of structures, significantly degrading performance. In this paper, we propose secure hashing mechanisms to thwart adversarial attempts to capture the mapping of shared structures. We propose DAPPER, a novel low-cost tracker resilient to Perf-Attacks even at ultra-low RowHammer thresholds. We first present a secure hashing template in the form of DAPPER-S. We then develop DAPPER-H, an enhanced version of DAPPER-S, incorporating double-hashing, novel reset strategies, and mitigative refresh techniques. Our security analysis demonstrates the effectiveness of DAPPER-H against both RowHammer and Perf-Attacks. Experiments with 57 workloads from SPEC2006, SPEC2017, TPC, Hadoop, MediaBench, and YCSB show that, even at an ultra-low RowHammer threshold of 500, DAPPER-H incurs only a 0.9% slowdown in the presence of Perf-Attacks while using only 96KB of SRAM per 32GB of DRAM memory.

## 中文摘要

Rowhammer 漏洞对现代基于 DRAM 的系统构成重大威胁：快速激活 DRAM 行会在相邻行中引发位翻转。为此，最先进的主机侧 Rowhammer 缓解通常依赖共享计数器或跟踪结构。这些优化虽有利于良性应用，却易受性能攻击（Perf-Attack）：攻击者利用共享结构，通过为 Rowhammer 计数器增加 DRAM 访问或触发结构提前复位所需的重复刷新，减少共同运行的良性应用可用的 DRAM 带宽，显著损害性能。本文提出安全哈希机制以挫败攻击者捕获共享结构映射的企图，并提出 DAPPER——一种低成本、即使面对超低 Rowhammer 阈值也能抵御性能攻击的跟踪器。我们首先给出 DAPPER-S 形式的安全哈希模板，进而开发增强版 DAPPER-H，引入双重哈希、新的复位策略与缓解性刷新技术。安全分析表明 DAPPER-H 能有效抵御 Rowhammer 与性能攻击。基于 SPEC2006、SPEC2017、TPC、Hadoop、MediaBench 与 YCSB 的 57 个负载的实验显示，即便在低至 500 的超低 Rowhammer 阈值下，DAPPER-H 在存在性能攻击时也仅带来 0.9% 的性能下降，且每 32GB DRAM 仅使用 96KB SRAM。
