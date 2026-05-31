---
title: "MoPAC: 基于概率激活计数的高效Rowhammer缓解"
description: "ISCA 2025论文解读：MoPAC提出概率激活计数机制，以极低硬件开销准确追踪DRAM行激活频率，高效缓解Rowhammer攻击。"
tags: ["ISCA2025", "Rowhammer", "DRAM安全", "概率计数", "GaTech", "Moin Qureshi"]
---

# MoPAC: Efficiently Mitigating Rowhammer with Probabilistic Activation Counting

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">MoPAC 用概率激活计数器（Probabilistic Activation Counter）替代精确计数，以极小的存储开销近似追踪 DRAM 行的激活频率，精准触发预防性刷新来缓解 Rowhammer。</p>
<p class="paper-seo-summary__tags">ISCA 2025 · Rowhammer缓解 · DRAM安全 · 概率计数 · Georgia Tech</p>
</div>

**作者**：Suhas Vittal, Salman Qazi, Poulami Das, Moin Qureshi  
**机构**：Georgia Institute of Technology, Google  
**会议**：ISCA 2025, Tokyo, Japan  
**Session**：Session 5A: RowHammer  

---

## 一句话总结

> 精确计数每行激活次数代价高昂；MoPAC 利用概率计数在小内存开销下高精度追踪高频行，实现低开销高效 Rowhammer 缓解。

## 背景与动机

- **Rowhammer 威胁升级**：DRAM 工艺缩小导致阈值（TRH）持续降低，现代 DRAM 需更频繁缓解
- **精确计数开销**：为每行维护精确激活计数器需要大量 SRAM 面积，不现实
- **概率计数思路**：借鉴 Count-Min Sketch 等概率数据结构，用极少计数位近似高激活行

## 主要贡献

1. **概率激活计数器设计**：基于哈希的计数器组，以 O(log N) 空间实现 O(1) 准确度估计
2. **误差分析**：证明在标准 Rowhammer 攻击模型下，MoPAC 的漏报率极低（< 0.01%）
3. **预防刷新集成**：与 PRAC（Per-Row Activation Counting）标准接口兼容
4. **面积开销**：计数器 SRAM 开销 < 0.1% DRAM 芯片面积

## 实验结果

- 在 TRH=1000 下，Rowhammer 缓解 **100% 有效**，漏报率 < 0.001%
- 性能开销 < 0.5%（较精确计数方案减少 80% 刷新操作）

## 关键词

Rowhammer · DRAM安全 · 概率计数 · 预防刷新 · Georgia Tech · ISCA 2025
