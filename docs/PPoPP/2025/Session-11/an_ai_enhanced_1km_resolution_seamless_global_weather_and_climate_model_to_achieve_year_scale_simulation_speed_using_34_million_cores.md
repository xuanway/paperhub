---
title: "An AI-Enhanced 1km-Resolution Seamless Global Weather and Climate Model to Achieve Year-Scale Simulation Speed using 34 Million Cores"
description: "PPoPP 2025 Session 11（Parallel Algorithms and Applications）：AI 物理套件 + 混合精度，3400 万核上实现 1km 全球模拟"
tags:
  - "PPoPP2025"
  - "Session-11"
  - "Parallel Algorithms and Applications"
  - "Weather and Climate"
  - "Supercomputing"
  - "Mixed Precision"
authors:
  - "Xiaohui Duan"
  - "Yi Zhang"
  - "Kai Xu"
  - "Haohuan Fu"
  - "Bin Yang"
  - "Yiming Wang"
  - "Yilun Han"
  - "Siyuan Chen"
  - "Zhuangzhuang Zhou"
  - "Chenyu Wang"
  - "Dongqiang Huang"
  - "Huihai An"
  - "Xiting Ju"
  - "Haopeng Huang"
  - "Zhuang Liu"
  - "Wei Xue"
  - "Weiguo Liu"
  - "Bowen Yan"
  - "Jianye Hou"
  - "Maoxue Yu"
  - "Wenguang Chen"
  - "Jian Li"
  - "Zhao Jing"
  - "Hailong Liu"
  - "Lixin Wu"
session: "Session 11: Parallel Algorithms and Applications"
session_number: 11
session_chair: "Weicong Chen"
date: "2025-03-05"
time: "12:40–13:00"
room: "Acacia D"
doi: "10.1145/3710848.3710893"
program_url: "https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program"
---

# An AI-Enhanced 1km-Resolution Seamless Global Weather and Climate Model to Achieve Year-Scale Simulation Speed using 34 Million Cores

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">面向新一代神威超算优化 GRIST 全球-区域一体化天气气候模式，融合 AI 增强物理套件、OpenMP 并行化与混合精度，实现 1km 分辨率并扩展到 3400 万核。</p>
<p class="paper-seo-summary__tags">PPoPP 2025 · Session 11: Parallel Algorithms and Applications</p>
</div>

**作者**：Xiaohui Duan (Shandong University); Yi Zhang (PIESAT Information Technology, Co. Ltd.); Kai Xu (Laoshan Laboratory); Haohuan Fu (Tsinghua University); Bin Yang (Tianjin University); Yiming Wang (PIESAT Information Technology, Co. Ltd.); Yilun Han (Tsinghua University); Siyuan Chen (PIESAT Information Technology, Co. Ltd.); Zhuangzhuang Zhou, Chenyu Wang, Dongqiang Huang (National Supercomputing Center in Wuxi); Huihai An (Shandong University); Xiting Ju, Haopeng Huang, Zhuang Liu, Wei Xue (Tsinghua University); Weiguo Liu (Shandong University); Bowen Yan (Tsinghua University); Jianye Hou (The Chinese University of Hong Kong); Maoxue Yu (Laoshan Laboratory); Wenguang Chen (Tsinghua University); Jian Li (Chinese Academy of Meteorological Sciences); Zhao Jing, Hailong Liu, Lixin Wu (Laoshan Laboratory)

**会议**：PPoPP 2025 · 2025 年 3 月 5 日 12:40–13:00 · Session 11: Parallel Algorithms and Applications（主席：Weicong Chen）· Acacia D

**论文**：[ACM Digital Library](https://doi.org/10.1145/3710848.3710893) · [PPoPP 2025 会议日程](https://ppopp25.sigplan.org/track/PPoPP-2025-Main-Conference-1#program)

---

## 一句话总结

> 面向新一代神威超算优化 GRIST 全球-区域一体化天气气候模式，融合 AI 增强物理套件、OpenMP 并行化与混合精度，实现 1km 分辨率并扩展到 3400 万核。

## 研究问题

气候变化背景下，全球风暴解析模式（GSRM）对理解极端天气至关重要，但 1km 分辨率带来的计算量与性能可移植性挑战巨大。

## 方法简述

- 引入 AI 增强的物理套件（AI-enhanced physics suite）。
- 基于 OpenMP 的并行化改造。
- 混合精度优化，同时提升效率与性能可移植性，并保持统一的天气—气候建模能力。

## 主要结果

- 以 1km 分辨率成功复现受超强台风杜苏芮影响的“23.7”华北极端降雨过程。
- 扩展到 3400 万核，达到 3km 下 491 SDPD、1km 下 181 SDPD 的模拟速度。

<details>
<summary>原文摘要（英文）</summary>

Global Storm Resolving Models (GSRMs) is crucial for understanding extreme weather events under the climate change background. In this study, we optimize Global-Regional Integrated Forecast System (GRIST), which is a unified weather-climate modeling system designed for research and operation, for the next-generation Sunway supercomputer, incorporating AI-enhanced physics suite, OpenMP-based parallelization, and mixed-precision optimizations to enhance both efficiency and performance portability, as well as the unified modeling capability. Our experiments successfully capture significant events during the “23.7” extreme rainfall over northern China influenced by super Typhoon Doksuri, at 1km resolution. Notably, our work scales to 34 million cores, enabling simulation speeds at 491 SDPD (3km) and 181 SDPD (1km).

</details>

---

> 所属 Session：[Session 11: Parallel Algorithms and Applications](index.md) · 返回 [PPoPP 2025 总览](../index.md)
