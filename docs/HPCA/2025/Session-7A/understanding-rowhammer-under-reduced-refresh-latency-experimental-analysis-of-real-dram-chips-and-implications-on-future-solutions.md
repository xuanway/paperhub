---
title: "Understanding RowHammer Under Reduced Refresh Latency: Experimental Analysis of Real DRAM Chips and Implications on Future Solutions"
description: "HPCA 2025 · Hammering the Odds"
tags:
  - "HPCA2025"
  - "Hammering the Odds"
---

# Understanding RowHammer Under Reduced Refresh Latency: Experimental Analysis of Real DRAM Chips and Implications on Future Solutions

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Hammering the Odds。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Hammering the Odds</p>
</div>

**论文链接**：
**作者**：Yahya Can Tuğrul (TOBB ETÜ & ETH Zürich), Giray Yaglikci (ETH Zürich), Ismail Emir Yuksel (ETH Zürich), Ataberk Olgun (ETH Zürich), Oğuzhan Canpolat (TOBB ETÜ & ETH Zürich), Nisa Bostanci (ETH Zürich), Mohammad Sadrosadati (ETH Zürich), Oguz Ergin (TOBB ETÜ), Onur Mutlu (ETH Zürich)
**会议**：HPCA 2025

---

## 中文标题

降低刷新时延下的 Rowhammer 理解：真实 DRAM 芯片的实验分析及对未来方案的启示

## 英文摘要

Read disturbance in modern DRAM chips is a widespread weakness that is used for breaking memory isolation, one of the fundamental building blocks of system security and privacy. RowHammer is a prime example of read disturbance in DRAM where repeatedly accessing (hammering) a row of DRAM cells (DRAM row) induces bitflips in physically nearby DRAM rows (victim rows). Unfortunately, shrinking technology node size exacerbates RowHammer and as such, significantly fewer accesses can induce bitflips in newer DRAM chip generations. To ensure robust DRAM operation, state-of-the-art mitigation mechanisms restore the charge in potential victim rows (i.e., they perform preventive refresh or charge restoration). With newer DRAM chip generations, these mechanisms perform preventive refresh more aggressively and cause larger performance, energy, or area overheads. Therefore, it is essential to develop a better understanding and in-depth insights into the preventive refresh to secure real DRAM chips at low cost. In this paper, our goal is to mitigate RowHammer at low cost by understanding the preventive refresh latency and the impact of reduced refresh latency on RowHammer. To this end, we present the first rigorous experimental study on the interactions between refresh latency and RowHammer characteristics in real DRAM chips. Our experimental characterization using 388 real DDR4 DRAM chips from three major manufacturers demonstrates that a preventive refresh latency can be significantly reduced (by 64%) at the expense of requiring slightly more (by 0.54%) preventive refreshes. To investigate the impact of reduced preventive refresh latency on system performance and energy efficiency, we reduce the preventive refresh latency and adjust the aggressiveness of existing RowHammer solutions by developing a new mechanism, Partial Charge Restoration for Aggressive Mitigation (PaCRAM). Our results show that by reducing the preventive refresh latency, PaCRAM reduces the performance and energy overheads induced by five state-of-the-art RowHammer mitigation mechanisms with small additional area overhead. Thus, PaCRAM introduces a novel perspective into addressing RowHammer vulnerability at low cost by leveraging our experimental observations. To aid future research, we open-source our PaCRAM implementation at https://github.com/CMU-SAFARI/PaCRAM.

## 中文摘要

现代 DRAM 芯片中的读干扰是普遍存在的弱点，可用于破坏内存隔离这一系统安全与隐私的基础构件。Rowhammer 是 DRAM 读干扰的典型例子：反复访问（锤击）一行会在物理相邻的受害行中引发位翻转。工艺节点缩小使 Rowhammer 加剧，新一代 DRAM 芯片中显著更少的访问即可引发位翻转。为保证 DRAM 可靠运行，最先进的缓解机制会恢复潜在受害行的电荷（即执行预防性刷新或电荷恢复），但随着代际演进，它们更激进地刷新，带来更大的性能、能耗或面积开销。因此，深入理解预防性刷新以低成本保障真实 DRAM 芯片安全至关重要。本文旨在通过理解预防性刷新时延及其降低对 Rowhammer 的影响，以低成本缓解 Rowhammer。我们首次严格实验研究了真实 DRAM 芯片中刷新时延与 Rowhammer 特性的相互作用：对来自三家主要厂商的 388 颗真实 DDR4 DRAM 芯片的表征表明，预防性刷新时延可显著缩短 64%，代价是所需预防性刷新略增 0.54%。为考察其影响，我们开发了新机制 PaCRAM（面向激进缓解的部分电荷恢复），缩短预防性刷新时延并调整现有方案的激进度。结果显示，PaCRAM 以很小的额外面积开销，降低了五种最先进 Rowhammer 缓解机制带来的性能与能耗开销，从而借助实验观察为低成本应对 Rowhammer 漏洞提供了新视角。为便于后续研究，我们在 https://github.com/CMU-SAFARI/PaCRAM 开源了实现。
