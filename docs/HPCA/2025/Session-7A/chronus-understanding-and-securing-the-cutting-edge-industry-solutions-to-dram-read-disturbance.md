---
title: "Chronus: Understanding and Securing the Cutting-Edge Industry Solutions to DRAM Read Disturbance"
description: "HPCA 2025 · Hammering the Odds"
tags:
  - "HPCA2025"
  - "Hammering the Odds"
---

# Chronus: Understanding and Securing the Cutting-Edge Industry Solutions to DRAM Read Disturbance

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Hammering the Odds。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Hammering the Odds</p>
</div>

**论文链接**：
**作者**：Oğuzhan Canpolat (TOBB ETÜ & ETH Zürich), Giray Yaglikci (ETH Zürich), Geraldo Francisco de Oliveira (ETH Zürich), Ataberk Olgun (ETH Zürich), Nisa Bostanci (ETH Zürich), Ismail Emir Yuksel (ETH Zürich), Haocong Luo (ETH Zürich), Oğuz Ergin (TOBB ETÜ), Onur Mutlu (ETH Zürich)
**会议**：HPCA 2025

---

## 中文标题

Chronus：理解并加固 DRAM 读干扰的前沿工业解决方案

## 英文摘要

Read disturbance in modern DRAM is an important robustness (security, safety, and reliability) problem, where repeatedly accessing (hammering) a row of DRAM cells (DRAM row) induces bitflips in other physically nearby DRAM rows. Shrinking technology node size exacerbates DRAM read disturbance over generations. To help mitigate read disturbance, the latest DDR5 specifications (as of April 2024) introduced a new RowHammer mitigation framework, called Per Row Activation Counting (PRAC). PRAC 1) enables the DRAM chip to accurately track row activations by allocating an activation counter per row and 2) provides the DRAM chip with the necessary time window to perform RowHammer-preventive refreshes by introducing a new back-off signal. Unfortunately, no prior work rigorously studies PRAC’s security guarantees and overheads. In this paper, we 1) present the first rigorous security, performance, energy, and cost analyses of PRAC and 2) propose Chronus, a new mechanism that addresses PRAC’s two major weaknesses. Our analysis shows that PRAC’s system performance overhead on benign applications is non-negligible for modern DRAM chips and prohibitively large for future DRAM chips that are more vulnerable to read disturbance. We identify two weaknesses of PRAC that cause these overheads. First, PRAC increases critical DRAM access latency parameters due to the additional time required to increment activation counters. Second, PRAC performs a constant number of preventive refreshes at a time, making it vulnerable to an adversarial access pattern, known as the wave attack, and consequently requiring it to be configured for significantly smaller activation thresholds. To address PRAC’s two weaknesses, we propose a new on-DRAM-die RowHammer mitigation mechanism, Chronus. Chronus 1) updates row activation counters concurrently while serving accesses by separating counters from the data and 2) prevents the wave attack by dynamically controlling the number of preventive refreshes performed. Our performance analysis shows that Chronus’s system performance overhead is near-zero for modern DRAM chips and very low for future DRAM chips. Chronus outperforms three variants of PRAC and three other state-of-the-art read disturbance solutions. We discuss Chronus’s and PRAC’s implications for future systems and foreshadow future research directions. To aid future research, we open-source our Chronus implementation at https://github.com/CMU-SAFARI/Chronus.

## 中文摘要

现代 DRAM 中的读干扰是重要的鲁棒性（安全、安防与可靠性）问题：反复访问（锤击）DRAM 的一行会在物理相邻的其他行中引发位翻转，且随工艺节点缩小逐代加剧。为缓解读干扰，最新的 DDR5 规范（截至 2024 年 4 月）引入了 Rowhammer 缓解框架 PRAC（逐行激活计数）：它为每行分配激活计数器以精确跟踪行激活，并通过新的退避信号为 DRAM 芯片提供执行预防性刷新所需的时间窗口。此前尚无工作严格研究 PRAC 的安全保证与开销。本文首次对 PRAC 做严格的安全、性能、能耗与成本分析，并提出 Chronus 以解决其两大缺陷。分析表明，PRAC 的系统性能开销对现代 DRAM 芯片不可忽略，对更易受读干扰影响的未来芯片则高得难以承受：其一，PRAC 因递增激活计数器的额外时间而抬高关键 DRAM 访问时延；其二，它每次执行固定数量的预防性刷新，易受波攻击这一对抗性访问模式的影响，因而必须配置小得多的激活阈值。Chronus 是新的 DRAM 裸片内缓解机制：它将计数器与数据分离，在服务访问的同时并发更新激活计数器；并通过动态控制预防性刷新的数量来抵御波攻击。性能分析显示，Chronus 的开销对现代 DRAM 芯片近乎为零、对未来芯片也很低，并优于 PRAC 的三种变体及另外三种最先进的读干扰方案。我们还讨论了二者对未来系统的启示与后续研究方向，并在 https://github.com/CMU-SAFARI/Chronus 开源了实现。
