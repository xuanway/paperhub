---
title: "Veritas – Demystifying Silent Data Corruptions: μArch-Level Modeling and Fleet Data of Modern x86 CPUs"
description: "HPCA 2025 · Reliable Bets"
tags:
  - "HPCA2025"
  - "Reliable Bets"
---

# Veritas – Demystifying Silent Data Corruptions: μArch-Level Modeling and Fleet Data of Modern x86 CPUs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2025，所属 Track: Reliable Bets。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Reliable Bets</p>
</div>

**论文链接**：
**作者**：Odysseas Chatzopoulos (University of Athens), Nikos Karystinos (University of Athens), George Papadimitriou (University of Athens), Dimitris Gizopoulos (University of Athens), Harish Dattatraya Dixit (Meta Platforms, Inc.), Sriram Sankar (Meta Platforms, Inc.)
**会议**：HPCA 2025

---

## 中文标题

Veritas：揭秘静默数据损坏——现代 x86 CPU 的微架构级建模与机群数据

## 英文摘要

Hyperscalers have reported unexpectedly high numbers of defective CPU chips, with a defect rate of 1 in a 1000, leading to Silent Data Corruptions (SDCs) in their computing fleets. However, there is no public data on the rate of SDC incidents (corrupted program executions) in large fleets, nor nor any detailed information on which CPU units, microarchitectures, or workloads are more likely to generate SDCs due to silicon defects. While CPU array structures have been studied for fault effects, arithmetic units like integer and floating-point units have not been thoroughly analyzed as potential root causes of SDCs. This paper addresses this critical gap by accurately modeling hardware faults in the arithmetic units of modern x86 CPUs and measuring the probability and rates of SDCs. Using a full-system gem5-based fault injector, the paper examines SDC trends across five recent x86 microarchitectures, various arithmetic units, and instruction classes. By integrating real-world defect rates from large-scale datacenter experiments with early-stage modeling and simulation, the paper provides critical insights into SDC incident rates across different systems. This information is essential for guiding hardware-based or software-based fault protection methods and is the paper’s primary contribution to minimizing the impact of silent data corruptions in computing.

## 中文摘要

超大规模云厂商报告了出乎意料的高缺陷 CPU 芯片数量，缺陷率高达千分之一，导致其计算机群中出现静默数据损坏（SDC）。然而，目前既没有关于大型机群中 SDC 事件（程序执行结果被损坏）发生率的公开数据，也没有关于哪些 CPU 单元、微架构或负载更可能因硅缺陷而产生 SDC 的详细信息。虽然 CPU 阵列结构已就故障影响进行过研究，但整数与浮点单元等算术单元作为 SDC 潜在根因尚未得到深入分析。本文通过精确建模现代 x86 CPU 算术单元中的硬件故障并测量 SDC 的概率与发生率，来填补这一关键空白。借助基于 gem5 的全系统故障注入器，本文考察了五种近期 x86 微架构、多种算术单元与指令类别中的 SDC 趋势。通过将大规模数据中心实验中的真实缺陷率与早期建模和仿真相结合，本文给出了关于不同系统中 SDC 事件发生率的关键洞见。这些信息对于指导基于硬件或基于软件的故障保护方法至关重要，也是本文在最大限度降低计算中静默数据损坏影响方面的主要贡献。
