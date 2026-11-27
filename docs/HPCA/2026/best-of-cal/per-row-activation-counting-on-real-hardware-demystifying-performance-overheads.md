---
title: "Per-Row Activation Counting on Real Hardware: Demystifying Performance Overheads"
description: "HPCA 2026 · Best of CAL"
tags:
  - "HPCA2026"
  - "Best of CAL"
---

# Per-Row Activation Counting on Real Hardware: Demystifying Performance Overheads

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Best of CAL。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Best of CAL</p>
</div>

**论文链接**：[https://doi.org/10.1109/LCA.2025.3587293](https://doi.org/10.1109/LCA.2025.3587293)
**作者**：Jumin Kim Seoul National University , Seungmin Baek Seoul National University , Minbok Wi Seoul National University , Hwayong Nam Seoul National University , Michael Jaemin Kim Meta , Sukhan Lee Samsung Electronics , Kyomin Sohn Samsung , Jung Ho Ahn Seoul National University
**会议**：HPCA 2026

---

## 中文标题

真实硬件上的逐行激活计数：揭开性能开销之谜

## 英文摘要

Per-Row Activation Counting (PRAC), a DRAM read disturbance mitigation method, modifies key DRAM timing parameters, reportedly causing significant performance overheads in simulator-based studies. However, given known discrepancies between simulators and real hardware, real-machine experiments are vital for accurate PRAC performance estimation. We present the first real-machine performance analysis of PRAC. After verifying timing modifications on the latest CPUs using microbenchmarks, our analysis shows that PRAC’s average and maximum overheads are just 1.06% and 3.28% for the SPEC CPU2017 workloads—up to 9.15× lower than simulator-based reports. Further, we show that the close page policy minimizes this overhead by effectively hiding the elongated DRAM row precharge operations due to PRAC from the critical path.

## 中文摘要

逐行激活计数（PRAC）是一种用于缓解 DRAM 读干扰的方法，它修改了若干关键的 DRAM 时序参数，据报道，在基于模拟器的研究中，这类时序参数的修改会造成显著的性能开销。然而，考虑到模拟器与真实硬件之间已知存在的偏差，要准确估计 PRAC 的性能，在真实机器上进行的实验是必不可少的。为此，我们给出了首个针对 PRAC 的实机性能分析。在使用微基准在最新一代 CPU 上逐项验证了时序参数的修改之后，我们的实测分析显示，对于 SPEC CPU2017 基准负载，PRAC 的平均开销与最大开销分别仅为 1.06% 与 3.28%，比基于模拟器得到的报告结果低至多 9.15 倍。进一步地，我们还表明，采用 close page 页策略能够有效地把 PRAC 所带来的 DRAM 行预充电操作延长隐藏在关键路径之外，从而把这一开销降低到了最低水平。
