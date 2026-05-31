---
title: "QPRAC: 基于优先队列的高效PRAC Rowhammer缓解"
description: "HPCA 2025论文解读：QPRAC利用优先队列数据结构优化DDR5 PRAC的行激活追踪，在保证安全性的前提下将PRAC的性能开销降低50%以上。"
tags: ["HPCA2025", "Rowhammer", "DRAM安全", "PRAC", "DDR5", "优先队列", "UBC"]
---

# QPRAC: Towards Secure and Practical PRAC-based Rowhammer Mitigation using Priority Queues

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">QPRAC 将 DDR5 PRAC 机制中的行激活计数改为基于优先队列的高效追踪，能够在常数时间内找到当前激活次数最高的 DRAM 行，使 Rowhammer 缓解的平均性能开销从 PRAC 的 2.1% 降至 0.9%，同时保持安全性。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Rowhammer · PRAC · DDR5 · 优先队列 · 内存安全 · UBC · Toronto</p>
</div>

**作者**：Jeonghyun Woo, Shaopeng (Chris) Lin, Prashant J. Nair, Aamer Jaleel, Gururaj Saileshwar  
**机构**：The University of British Columbia (UBC); University of Toronto; NVIDIA  
**会议**：HPCA 2025, Las Vegas, NV, USA  

---

## 一句话总结

> DDR5 PRAC 为每行 DRAM 维护激活计数，但查找最高计数行（即最危险行）需要遍历所有行，开销大；QPRAC 用优先队列维护 Top-K 高风险行，使刷新决策从 O(N) 降至 O(log K)，大幅降低性能开销。

## 背景与动机

- **PRAC 的性能开销**：DDR5 PRAC 在每次 Refresh 周期检查是否有行需要被 Alert-Back-Off 触发，需要定期扫描计数器，造成内存带宽占用
- **现有 PRAC 实现的低效性**：朴素实现中，内存控制器维护所有行的计数数组，找到最需要刷新的行需要全量扫描
- **优先队列的机会**：只有少数（Top-K 个）行的激活计数接近 Rowhammer 阈值，可以用优先队列专注追踪这些"高风险行"

## QPRAC 设计

### 优先队列行追踪

- 维护容量为 K（典型值 K=32）的最大堆（Max-Heap），记录当前激活计数最高的 K 行
- 每次行激活时：
  1. 若该行已在堆中，更新其计数
  2. 若不在堆中且激活次数超过低水位线，入堆并淘汰最低计数条目
- ABO 触发检查：只需比较堆顶元素（最大计数），O(1) 完成

### 安全性保证

- 理论证明：若 HC_first = T，则 QPRAC 中任何行的激活计数一旦接近 T，必定已进入优先队列被追踪
- 低水位线参数设置保证误放概率（False Negative 率）< $10^{-15}$

### 与 DAPPER 协同

QPRAC 可与同一 Session 的 DAPPER 结合（DAPPER 专注于缓解攻击时的"性能攻击"），两者从不同维度互补。

## 实验结果

| 方案 | 安全性 | 平均 IPC 开销 | 最坏情况开销 |
|------|--------|-------------|------------|
| 原始 PRAC | ✅ | 2.1% | 12.4% |
| QPRAC | ✅ | 0.9% | 5.3% |
| DAPPER | ✅ | 1.4% | 3.2% |
| QPRAC + DAPPER | ✅ | 0.7% | 2.8% |

## 核心亮点

1. 将 PRAC 平均性能开销降低 57%，最坏情况开销降低 57%
2. 优先队列设计简洁，可直接集成到现有 DDR5 内存控制器中
3. 与 DAPPER 等其他方案兼容，可组合使用

## 局限性

- K=32 的优先队列对极端攻击模式（轮流攻击 32+ 行）存在遗漏风险，需要仔细参数调整
- 优先队列的硬件实现（特别是 32 条目动态排序）有一定面积成本
