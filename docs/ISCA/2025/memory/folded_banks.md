---
title: "Folded Banks: 面向细粒度随机访问带宽的3D堆叠HBM设计"
description: "ISCA 2025论文解读：Folded Banks提出新型3D堆叠HBM设计，通过折叠式Bank架构实现细粒度随机访问时的高带宽利用率。"
tags: ["ISCA2025", "HBM", "3D堆叠", "内存带宽", "AMD", "随机访问"]
---

# Folded Banks: 3D-Stacked HBM Design for Fine-Grained Random-Access Bandwidth

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">Folded Banks 针对 HBM 在细粒度随机访问场景下带宽利用率低的问题，提出折叠式 Bank 架构，通过重新组织存储阵列布局，在小尺寸随机访问时充分利用 HBM 的 TSV 带宽。</p>
<p class="paper-seo-summary__tags">ISCA 2025 · HBM · 3D堆叠内存 · 随机访问带宽 · AMD Research</p>
</div>

**作者**：Vignesh Adhinarayanan, Brad Beckmann, Wantong Li, Mohammad Seyedzadeh, Sergey Blagodurov, Derrick Aguren, Hayden Hyungdong Lee  
**机构**：AMD Research  
**会议**：ISCA 2025, Tokyo, Japan  
**Session**：Session 9C: Memory Technology  

---

## 一句话总结

> HBM 在大块顺序访问时带宽充裕，但细粒度随机访问时 Bank 冲突严重；Folded Banks 通过折叠 Bank 布局显著改善随机访问带宽利用率。

## 背景与动机

- **HBM 随机访问低效**：HBM 的 Bank 数量有限，细粒度随机访问导致频繁 Bank 冲突和 Row Buffer Miss
- **AI 工作负载特性**：GNN、稀疏 Attention 等 AI 工作负载产生大量不规则内存访问
- **Folded Banks 方案**：折叠存储阵列，将原来物理相邻的行分配到不同逻辑 Bank，减少冲突概率

## 主要贡献

1. **折叠 Bank 架构**：通过物理地址映射创新，将 HBM 的有效 Bank 数量倍增
2. **TSV 带宽利用**：折叠设计允许同时访问更多独立 Bank，提升 TSV 实际利用率
3. **向后兼容**：在不改变 HBM 标准接口的前提下实现 Bank 折叠

## 实验结果

- 细粒度随机访问带宽提升 **1.8–2.5×**
- GNN 推理端到端加速 **1.4×**

## 关键词

HBM · 3D堆叠内存 · 随机访问 · Bank冲突 · AMD Research · ISCA 2025
