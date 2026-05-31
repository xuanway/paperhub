---
title: "MIRZA: 基于随机化与ALERT的高效Rowhammer防御"
description: "HPCA 2026论文解读：MIRZA通过行地址随机化与ALERT机制协同工作，在极低性能开销下有效缓解Rowhammer攻击。"
tags: ["HPCA2026", "DRAM安全", "Rowhammer", "内存安全", "Georgia Tech"]
---

# MIRZA: Efficiently Mitigating Rowhammer with Randomization and ALERT

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">MIRZA 将行地址随机化（RAR）与 DRAM ALERT 机制结合，以低于 0.5% 的性能开销消除 Rowhammer 攻击，优于现有防御方案 3-5×。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · DRAM安全 · Rowhammer · 内存安全 · Georgia Tech</p>
</div>

**作者**：Hritvik Taneja, Ali Hajiabadi, Michele Marazzi, Kaveh Razavi, Moinuddin K. Qureshi  
**机构**：Georgia Tech, ETH Zürich, ABB Research  
**会议**：HPCA 2026, Sydney, Australia  

---

## 一句话总结

> Rowhammer 防御的核心挑战是"以够低代价追踪够多行"，MIRZA 通过行地址随机化将攻击者的目标分散，结合 DRAM 内置 ALERT 机制按需刷新，实现接近零开销的防御。

## 背景与动机

- **问题**：Rowhammer 攻击通过高频访问"侵略行（Aggressor Row）"导致相邻行（受害行）发生比特翻转，威胁内存完整性。随着 DRAM 密度提升，触发阈值（TRH）从数万次降至数千次。
- **现有方案的不足**：PARA、TRR 等方案需追踪大量行激活计数，硬件开销大；pTRR 在自适应攻击下失效。
- **本文思路**：随机化使攻击者无法预测哪行是受害行，ALERT 信号在真正危险时才触发刷新，避免频繁误刷新。

## 方法详解

### 核心思想

1. **行地址随机化（RAR）**：DRAM 控制器使用密钥对物理行地址进行随机置换，使攻击者无法确定侵略行与受害行的对应关系
2. **ALERT 联动**：当 DRAM 内部监测到行激活数接近阈值，发出 ALERT 信号，控制器仅对 ALERT 发出的行执行邻行刷新

### 随机化更新策略

密钥定期更新（每隔数百毫秒），确保攻击者即使短期猜中映射关系，也无法积累足够激活次数。

## 实验结果

| 方案 | 性能开销 | 安全性（vs. 最优攻击） |
|------|---------|----------------------|
| pTRR | 1.2% | 可被绕过 |
| Hydra | 2.8% | 安全 |
| **MIRZA** | **0.4%** | **安全** |

## 核心亮点

1. 性能开销仅 0.4%，比现有安全方案低 3-7×
2. 随机化使所有已知 Rowhammer 攻击模式失效
3. 与现有 DRAM ALERT 标准兼容，无需修改 DRAM 芯片

## 局限性

- 依赖 DRAM 内置 ALERT 机制，需 DRAM 厂商支持
- 随机化密钥管理引入微小的密钥存储和更新开销
