---
title: "SALT: 追踪子阵列而非行的Rowhammer无爆炸半径防御"
description: "HPCA 2026论文解读：SALT将Rowhammer防御粒度从行级提升到子阵列级，彻底消除爆炸半径问题，以极低开销提供强安全保证。"
tags: ["HPCA2026", "DRAM安全", "Rowhammer", "子阵列", "Georgia Tech"]
---

# SALT: Track-and-Mitigate Subarrays, Not Rows, for Blast-Radius-Free Rowhammer Defense

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">SALT 将 Rowhammer 防御单元从"行"提升为"子阵列"，通过追踪子阵列激活模式消除爆炸半径（blast radius）问题，同时将计数器存储开销降低 128×。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · DRAM安全 · Rowhammer防御 · 子阵列级保护</p>
</div>

**作者**：Moinuddin K. Qureshi  
**机构**：Georgia Tech  
**会议**：HPCA 2026, Sydney, Australia  

---

## 一句话总结

> 现有 Rowhammer 防御追踪单行激活，但刷新时须刷新相邻行（产生爆炸半径）；SALT 转而追踪子阵列，从根本上消除爆炸半径，计数器开销减少 128×。

## 背景与动机

- **问题**：现有方案追踪每一行的激活次数，当某行激活超阈值时刷新其相邻行。但相邻行本身可能成为下一轮攻击目标（爆炸半径/cascading问题）。
- **现有方案的不足**：PARA 等方案需 O(行数) 计数器；Hydra 虽优化，但爆炸半径问题仍未彻底解决。
- **本文思路**：DRAM 的物理结构天然具有"子阵列"层次，一个子阵列内的行共享同一批字线驱动器；追踪子阵列激活可大幅减少状态并消除爆炸半径。

## 方法详解

### 核心思想

子阵列（约 128-512 行）是 DRAM 物理刷新的自然边界：
1. 追踪每个**子阵列**的激活次数，而非每一行
2. 当子阵列激活数超阈值，对**整个子阵列**执行批量刷新
3. 无需刷新相邻子阵列，因此无爆炸半径

### 计数器优化

每个子阵列仅需一个计数器，相比行级追踪节省 128-512× 存储空间，可完全存储在片上 SRAM。

## 实验结果

| 方案 | 计数器数量 | 爆炸半径 | 性能开销 |
|------|----------|---------|---------|
| 行级追踪（Hydra） | ~64K | 存在 | 1.5% |
| **SALT** | **512** | **无** | **0.7%** |

## 核心亮点

1. 从概念上彻底解决 Rowhammer 爆炸半径问题
2. 计数器存储需求降低 128× 以上，可完全片上化
3. 与现有 DRAM 接口（DDR5 RFM）兼容

## 局限性

- 子阵列级刷新会临时中断整个子阵列访问，带来突发延迟
- 子阵列内部的局部热行仍需额外保护机制
