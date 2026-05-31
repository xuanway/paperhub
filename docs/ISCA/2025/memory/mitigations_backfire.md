---
title: "When Mitigations Backfire: PRAC时序侧信道攻击与防御"
description: "ISCA 2025论文解读：揭示PRAC（Per-Row Activation Counting）Rowhammer缓解方案引入新型时序侧信道，并提出相应防御机制。"
tags: ["ISCA2025", "Rowhammer", "PRAC", "时序侧信道", "DRAM安全"]
---

# When Mitigations Backfire: Timing Channel Attacks and Defense for PRAC-Based Rowhammer Mitigations

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">PRAC 标准通过计数激活次数触发预防性刷新，但刷新操作本身会引入可观测的时序变化，攻击者可借此推断其他进程的 DRAM 访问模式，形成新型时序侧信道。本文分析攻击路径并提出防御。</p>
<p class="paper-seo-summary__tags">ISCA 2025 · PRAC · Rowhammer · 时序侧信道 · DRAM安全 · UBC</p>
</div>

**作者**：Jeonghyun Woo, Joyce Qu, Gururaj Saileshwar, Prashant Nair  
**机构**：University of British Columbia, Georgia Tech  
**会议**：ISCA 2025, Tokyo, Japan  
**Session**：Session 5A: RowHammer  

---

## 一句话总结

> Rowhammer 缓解措施本身可成为侧信道：PRAC 触发的预防刷新暴露了受害进程的访问模式；本文揭示攻击并提出低开销防御。

## 背景与动机

- **PRAC 缓解机制**：DDR5 的 PRAC 标准要求 DRAM 控制器追踪行激活计数并触发 RFM（Refresh Management）
- **新型攻击面**：RFM 刷新会占用总线，攻击者通过监测总线延迟可推断哪些行被高频访问
- **安全隐患**：可用于侧信道推断密码密钥、推断进程地址分布等

## 主要贡献

1. **攻击建模**：形式化分析 PRAC-RFM 时序侧信道，量化信息泄露率
2. **概念验证攻击**：在实际 DDR5 系统上演示通过总线延迟推断内存访问模式
3. **防御机制**：
   - **随机化刷新延迟**：增加 RFM 时序随机噪声
   - **批量刷新**：合并多个 RFM 操作，降低时序区分度
4. **安全性分析**：证明防御后信息泄露率降低至不可利用水平

## 实验结果

- 攻击可在 10ms 内以 >95% 准确率推断受害进程热点行
- 提出防御方案将信息泄露降至 <5%，性能开销 <1%

## 关键词

PRAC · Rowhammer · 时序侧信道 · DDR5 · DRAM安全 · ISCA 2025
