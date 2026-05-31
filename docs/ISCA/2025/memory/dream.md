---
title: "DREAM: 基于定向刷新管理的低开销Rowhammer缓解"
description: "ISCA 2025论文解读：DREAM提出定向刷新管理机制，通过精确定位高风险行并优先刷新，以极低性能开销实现高效Rowhammer缓解。"
tags: ["ISCA2025", "Rowhammer", "DRAM安全", "定向刷新", "GaTech", "Moin Qureshi"]
---

# DREAM: Enabling Low-Overhead Rowhammer Mitigation via Directed Refresh Management

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DREAM 通过定向（Directed）刷新管理策略，优先对高激活频率的 DRAM 行进行预防性刷新，避免对低风险行的冗余刷新，从而在保证 Rowhammer 安全的同时最小化性能开销。</p>
<p class="paper-seo-summary__tags">ISCA 2025 · Rowhammer缓解 · 定向刷新 · DRAM安全 · Georgia Tech · Moin Qureshi</p>
</div>

**作者**：Hritvik Taneja, Moin Qureshi  
**机构**：Georgia Institute of Technology  
**会议**：ISCA 2025, Tokyo, Japan  
**Session**：Session 5A: RowHammer  

---

## 一句话总结

> 传统 RFM 刷新所有邻居行代价高；DREAM 通过追踪高频行并定向刷新，将刷新开销降低一个数量级，同时保持完整的 Rowhammer 防护。

## 背景与动机

- **RFM 开销问题**：DDR5 的 RFM 对每次超阈值激活触发邻居行刷新，实际攻击分散时导致大量冗余刷新
- **定向缓解思路**：维护高激活频率行的排名，只刷新真正高风险的邻居行
- **DREAM 方案**：轻量级硬件追踪器 + 定向刷新调度，精准缓解而非全面刷新

## 主要贡献

1. **高频行追踪器**：小型 SRAM 结构维护当前激活频率 Top-K 行的排名表
2. **定向刷新策略**：仅对排名前列的行触发邻居刷新，跳过低频行
3. **自适应阈值**：根据 DRAM 工作负载动态调整触发阈值，平衡安全性与性能
4. **DDR5 兼容**：与 PRAC/RFM 标准接口兼容，可集成到内存控制器

## 实验结果

| 指标 | DREAM | 标准 RFM |
|------|-------|---------|
| Rowhammer 防护 | ✓ 完整 | ✓ 完整 |
| 刷新操作数 | 10× 减少 | 基准 |
| IPC 开销 | < 0.3% | 1–5% |

## 关键词

Rowhammer · 定向刷新 · DRAM安全 · RFM · Georgia Tech · ISCA 2025
