---
title: "SALT: Track-and-Mitigate Subarrays, Not Rows, for Blast-Radius-Free Rowhammer Defense"
description: "HPCA 2026 · DRAM Security and Reliability"
tags:
  - "HPCA2026"
  - "DRAM Security and Reliability"
---

# SALT: Track-and-Mitigate Subarrays, Not Rows, for Blast-Radius-Free Rowhammer Defense

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: DRAM Security and Reliability。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · DRAM Security and Reliability</p>
</div>

**论文链接**：
**作者**：Moinuddin K. Qureshi Georgia Tech
**会议**：HPCA 2026

---

## 中文标题

SALT：按子阵列而非行进行追踪与缓解，实现无爆炸半径的 Rowhammer 防御

## 英文摘要

Typical in-DRAM Rowhammer mitigation operates by identifying aggressor rows and refreshing a limited number of victim rows on either side of the aggressor row. The number of victim rows is specified by the Blast Radius. JEDEC recently introduced state-of-the-art Rowhammer defense, which includes Per-Row-Activation-Counting (PRAC) to identify aggressor rows and Alert-Back-Off (ABO) to allow the DRAM chip to obtain time to refresh two victim rows on either side of the aggressor row. The implicit assumption in PRAC is that charge loss beyond the two victim rows is negligibly small and does not represent a threat to the security of PRAC. In this paper, we develop Ripple Attack that can amplify even a small amount of leakage in distant rows to cause charge loss equivalent to 3x-78x the activations tolerated by PRAC for the given threshold. The goal of our paper is to develop an in-DRAM mitigation that tolerates Rowhammer without relying on a pre-defined Blast Radius. We observe that as subarrays are spatially isolated from each other, activity in one subarray does not cause charge leakage in rows of another subarray. To develop Blast-Radius-Free Rowhammer mitigation, we propose SALT (Subarray-Level Tracking and Mitigation). SALT tracks activation counts per subarray, and when the count exceeds a specified value, it triggers ABO to obtain time for refreshing a portion of the subarray. SALT bounds the maximum number of activations to the subarray before all rows are guaranteed to be refreshed, thus providing Blast-Radius-Free Rowhammer mitigation. To reduce the slowdown from ABO, SALT-C coordinates the demand refresh operations such that ABO is not required if the activations to the subarray are below what can be handled by the demand refresh, thus reducing ABO by 48x. SALT-C not only provides stronger security guarantees than PRAC due to Blast-Radius-Freedom, but also has 38x lower storage overhead than PRAC, and incurs lower slowdown (0.3% vs 1.7%) than PRAC.

## 中文摘要

典型的 DRAM 内 Rowhammer 缓解方法依靠识别攻击者行，并刷新其两侧有限数量的受害行，受害行数量由爆炸半径（Blast Radius）决定。JEDEC 近期提出的最先进防御包含逐行激活计数（PRAC）以识别攻击者行，并用 Alert-Back-Off（ABO）让 DRAM 芯片获得时间刷新攻击者行两侧的两个受害行。PRAC 隐含假设两个受害行之外的电荷泄漏可忽略，不构成安全威胁。本文提出 Ripple Attack，可将远处行中极小的泄漏放大，造成相当于 PRAC 在给定阈值下所容忍激活次数 3× 至 78× 的电荷损失。本文目标是设计不依赖预定义爆炸半径的 DRAM 内缓解方案。我们观察到子阵列在空间上相互隔离，一个子阵列的活动不会引起另一子阵列行的电荷泄漏。为此提出 SALT（子阵列级追踪与缓解）：按子阵列追踪激活计数，计数超过给定值时触发 ABO 以获得刷新该子阵列一部分的时间；SALT 限定了全部行被保证刷新之前子阵列的最大激活次数，从而实现无爆炸半径的缓解。为减少 ABO 造成的性能下降，SALT-C 协调按需刷新，使激活次数处于按需刷新可处理范围时无需 ABO，从而将 ABO 减少 48×。SALT-C 比 PRAC 提供更强的安全保障，存储开销低 38×，性能下降更小（0.3% 对 1.7%）。
