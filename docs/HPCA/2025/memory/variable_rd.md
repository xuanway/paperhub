---
title: "Variable Read Disturbance: DRAM读扰动时间变异性分析"
description: "HPCA 2025论文解读：ETH Zürich Onur Mutlu团队对真实DRAM芯片的读扰动（Read Disturbance）进行系统实验分析，发现Rowhammer阈值存在显著时间变化特性，对现有缓解方案提出新挑战。"
tags: ["HPCA2025", "Rowhammer", "DRAM安全", "读扰动", "ETH Zürich", "实验分析"]
---

# Variable Read Disturbance: An Experimental Analysis of Temporal Variation in DRAM Read Disturbance

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">本文对 272 颗真实 DRAM 芯片进行全面实验，发现 Rowhammer 阈值（Hammer Count for Bit Flip, HC_first）随温度、时间、读写历史等因素发生显著变化，最大变化幅度超过 50%，对所有基于静态阈值的 Rowhammer 缓解方案提出根本性挑战。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · Rowhammer · DRAM · 读扰动 · 时间变化 · ETH Zürich · Onur Mutlu</p>
</div>

**作者**：Ataberk Olgun, Nisa Bostanci, Ismail Emir Yuksel, Giray Yaglikci, Geraldo F. Oliveira, Haocong Luo, Oguzhan Canpolat, Minesh Patel, Onur Mutlu  
**机构**：ETH Zürich; Rutgers University  
**会议**：HPCA 2025, Las Vegas, NV, USA  

---

## 一句话总结

> Rowhammer 缓解方案通常假设 Hammer Count 阈值是固定的（如 RowPress Threshold 为 4800），但本文实验发现这一阈值随时间持续变化，最高变化幅度超过 50%，静态缓解阈值既可能漏防攻击，也可能过度刷新损害性能。

## 背景与动机

- **Rowhammer 阈值的重要性**：所有基于行激活计数的缓解方案（PARA、PRISM、Hydra、PRAC等）都依赖一个假设的最小 Hammer Count 阈值（HC_first）
- **实际测量的挑战**：研究界通常在实验室环境下测量 HC_first，但真实部署环境中温度、负载历史等条件持续变化
- **时间变异性**：DRAM 细胞的电荷保留能力受工艺变化和老化影响，Rowhammer 漏洞的严重程度应随时间演变

## 实验设计

- **测试平台**：272 颗 DRAM 芯片（覆盖 Samsung、SK Hynix、Micron 三大厂商的多个工艺代）
- **测量方法**：使用 DRAM Bender 框架精确控制行激活序列，在不同温度（20°C ～ 80°C）、不同时间点重复测量 HC_first
- **时间跨度**：每个芯片测量周期为 6 个月

## 关键发现

| 发现 | 数值 |
|------|------|
| HC_first 最大时间变化幅度 | 54.3%（同一芯片不同时间点） |
| 温度 80°C vs 20°C 时 HC_first 差异 | 平均降低 31% |
| "安全" 时期后出现新位翻转的芯片比例 | 23% |
| 部分芯片 HC_first 随时间持续下降 | 6 个月内下降 > 30% |

## 对缓解方案的影响

1. **静态阈值方案（PRISM、Hydra）**：若阈值设置偏高，温度升高后可能出现漏防
2. **基于计数的方案（TRR、DDR5 RFM）**：计数周期需要考虑 HC_first 的最坏情况，实际平均性能开销可能被低估
3. **工厂测试的局限性**：出厂时通过测试的芯片，使用一段时间后可能变得不安全

## 核心亮点

1. 首次系统量化 Rowhammer 阈值的时间变异性，实验规模最大（272 颗芯片，6 个月）
2. 发现"Rowhammer 漏洞会随时间加重"，对内存系统安全有深远影响
3. 开源测试数据和 DRAM Bender 测试框架

## 局限性

- 实验基于特定工艺代芯片，新工艺（如 DDR5 1z nm）可能有不同变化特性
- 真实服务器负载模式下的 HC_first 变化规律仍需进一步研究
