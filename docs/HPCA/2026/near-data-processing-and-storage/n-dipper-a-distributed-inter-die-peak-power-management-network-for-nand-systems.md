---
title: "N-DIPPER: A Distributed Inter-die Peak Power Management Network for NAND Systems"
description: "HPCA 2026 · Near-Data Processing and Storage"
tags:
  - "HPCA2026"
  - "Near-Data Processing and Storage"
---

# N-DIPPER: A Distributed Inter-die Peak Power Management Network for NAND Systems

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Near-Data Processing and Storage。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Near-Data Processing and Storage</p>
</div>

**论文链接**：
**作者**：Jinwoo Park KAIST , John Kim KAIST
**会议**：HPCA 2026

---

## 中文标题

N-DIPPER：面向 NAND 系统的分布式跨 die 峰值功耗管理网络

## 英文摘要

As NAND flash memory continues to scale, the increasing word-line (WL) stack height and higher program voltage requirements have led to severe peak-current overlaps across dies within a package. Such overlaps cause power-management-IC (PMIC) limit violations, voltage droops, and reliability degradation. Traditional static solutions – such as controller throttling or slope control – cannot fully address these issues because dynamic process, voltage, and temperature (PVT) variations and wear-out-induced drift cause both nondeterministic inter-die timing mismatches and peak-current magnitude fluctuations, forcing conservative guardbands that limit system parallelism and performance. To overcome these challenges, we propose N-DIPPER (NAND Distributed Inter-die Peak PowER Management Network), a cooperative runtime inter-die scheduling framework that dynamically schedules high-current (HC) phases through lightweight in-package (inter-die) fabric. N-DIPPER is based on token-based scheduling across the fabric to serialize scheduling of HC phases while device-aware information is leveraged to avoid utilizing worst-case guardbands. Our evaluation results show that N-DIPPER eliminates PMIC-limit violations (100%) while sustaining 97% of the baseline throughput (without any peak power management) across diverse workloads and die configurations.

## 中文摘要

随着 NAND 闪存持续微缩，不断增加的字线（WL）堆叠高度和更高的编程电压需求，导致同一封装内各 die 之间出现严重的峰值电流重叠。这类重叠会造成电源管理芯片（PMIC）超限、电压跌落和可靠性退化。传统的静态方案，如控制器节流或斜率控制，无法完全解决这些问题，因为动态的工艺、电压和温度（PVT）变化以及磨损引起的漂移，既会造成非确定性的 die 间时序失配，也会带来峰值电流幅度的波动，迫使系统采用保守的保护带，限制了并行度与性能。为克服这些挑战，我们提出 N-DIPPER（NAND Distributed Inter-die Peak PowER Management Network），一个协作式运行时 die 间调度框架，通过轻量级的封装内（die 间）互连动态调度大电流（HC）阶段。N-DIPPER 基于互连上的令牌式调度，将 HC 阶段的调度串行化，同时利用器件感知信息避免采用最坏情况的保护带。评估结果表明，在多种负载与 die 配置下，N-DIPPER 在 100% 消除 PMIC 超限的同时，仍保持基线（不含任何峰值功耗管理）97% 的吞吐。
