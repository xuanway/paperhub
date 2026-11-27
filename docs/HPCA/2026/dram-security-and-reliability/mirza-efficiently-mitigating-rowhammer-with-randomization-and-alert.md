---
title: "MIRZA: Efficiently Mitigating Rowhammer with Randomization and ALERT"
description: "HPCA 2026 · DRAM Security and Reliability"
tags:
  - "HPCA2026"
  - "DRAM Security and Reliability"
---

# MIRZA: Efficiently Mitigating Rowhammer with Randomization and ALERT

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: DRAM Security and Reliability。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · DRAM Security and Reliability</p>
</div>

**论文链接**：
**作者**：Hritvik Taneja Georgia Tech , Ali Hajiabadi ETH Zurich , Michele Marazzi ABB Research , Kaveh Razavi ETH Zürich , Moinuddin K. Qureshi Georgia Tech
**会议**：HPCA 2026

---

## 中文标题

MIRZA：利用随机化与 ALERT 高效缓解 Rowhammer

## 英文摘要

In-DRAM Rowhammer mitigation requires three resources: space (to track aggressor rows), time (to perform mitigation), and energy (to refresh victim rows). An ideal in-DRAM mitigation must minimize all three overheads. Recent randomized trackers, such as MINT, can perform tracking with negligible storage overheads. However, they perform mitigation proactively and frequently, which incurs significant performance and energy overheads at low thresholds. Recently, JEDEC introduced Per-Row Activation Counters (PRAC) and ALERT Back Off (ABO) protocol to obtain the time for mitigation reactively, as needed. While PRAC+ABO minimizes the time and energy overheads of mitigation, PRAC incurs significant changes to the DRAM array and significant performance overhead (6.5% on average) due to increased memory timings to update the PRAC counters. Our goal is to develop an efficient in-DRAM mitigation that has low storage, performance, and energy overheads. Our paper proposes MIRZA, the first low-cost reactive in-DRAM mitigation. MIRZA relies on MINT to track aggressor rows. However, instead of proactively doing mitigation at regular intervals (via REF or RFM), MIRZA uses ABO to reactively obtain the time required for mitigation. To avoid frequent ABO, MIRZA employs Coarse-Grained Filtering to disable mitigations if the activation count is below a certain Filtering Threshold. To tolerate a threshold of 1K, MIRZA requires a storage overhead of only 196 bytes of SRAM per bank. Compared to MINT, MIRZA reduces the mitigation overheads by 28.5x. Compared to PRAC, MIRZA has 45x lower area overheads and negligible slowdown (0.36% average slowdown vs. 6.5% for PRAC).

## 中文摘要

DRAM 内 Rowhammer 缓解需要三种资源：空间（跟踪攻击者行）、时间（执行缓解）与能量（刷新受害行），理想方案须最小化这三项开销。随机化跟踪器 MINT 能以可忽略的存储开销完成跟踪，但主动且频繁地缓解，在低阈值下带来显著性能与能量开销。JEDEC 提出的逐行激活计数（PRAC）与 ALERT 退避（ABO）协议可按需反应式获得缓解时间；PRAC+ABO 虽最小化了时间与能量开销，PRAC 却对 DRAM 阵列改动大，并因更新计数器所需的时序增加带来平均 6.5% 的性能开销。我们的目标是存储、性能与能量开销均低的高效 DRAM 内缓解，为此提出 MIRZA，首个低成本反应式 DRAM 内缓解。MIRZA 依赖 MINT 跟踪攻击者行，但不以固定间隔通过 REF 或 RFM 主动缓解，而用 ABO 反应式获得缓解时间；为避免频繁 ABO，它采用粗粒度过滤，在激活计数低于某阈值时禁用缓解。为容忍 1K 阈值，MIRZA 每 bank 仅需 196 字节 SRAM。相比 MINT，其缓解开销降低 28.5 倍；相比 PRAC，面积开销低 45 倍且性能下降可忽略（平均 0.36%，PRAC 为 6.5%）。
