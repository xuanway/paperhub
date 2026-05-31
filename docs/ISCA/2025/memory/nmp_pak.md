---
title: "NMP-PaK: 近存处理加速可扩展从头基因组装"
description: "ISCA 2025论文解读：NMP-PaK利用近存处理（NMP）加速基因组从头拼接（De Novo Assembly）中的图构建与遍历操作，大幅降低内存带宽瓶颈。"
tags: ["ISCA2025", "近存处理", "基因组装", "NMP", "生物信息", "Michigan"]
---

# NMP-PaK: Near-Memory Processing Acceleration of Scalable De Novo Genome Assembly

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">NMP-PaK 将基因组从头拼接的关键步骤（k-mer 计数、De Bruijn 图构建与遍历）映射到近存处理架构，利用存储端的带宽优势消除 CPU 内存带宽瓶颈。</p>
<p class="paper-seo-summary__tags">ISCA 2025 · 近存处理 · 基因组装 · NMP · 生物信息计算 · Michigan</p>
</div>

**作者**：Heewoo Kim, Sanjay Sri Vallabh Singapuram, Haojie Ye, Joseph Izraelevitz, Trevor Mudge, Ronald Dreslinski, Nishil Talati  
**机构**：University of Michigan  
**会议**：ISCA 2025, Tokyo, Japan  
**Session**：Session 9C: Memory Technology  

---

## 一句话总结

> 基因组拼接的 k-mer 图操作极度内存密集；NMP-PaK 将 k-mer 计数和图遍历卸载到近存处理单元，以存储侧带宽突破 CPU 带宽瓶颈。

## 背景与动机

- **基因组拼接瓶颈**：De Novo Assembly 中 k-mer 计数和图遍历产生 TB 级随机内存访问
- **CPU 方案低效**：DRAM 带宽成为严重瓶颈，CPU 利用率极低（常 < 30%）
- **NMP 适配性**：k-mer 操作以简单哈希为主，非常适合近存简单计算模式

## 主要贡献

1. **NMP 映射框架**：将 De Novo Assembly 流水线分解为适合近存执行的原语
2. **专用 NMP 指令**：针对哈希表查询、图邻居遍历的专用操作
3. **可扩展性**：支持多 NMP 模块并行，适应大型基因组（人类基因组 ~3 GB）

## 实验结果

- 相比多线程 CPU，k-mer 计数阶段加速 **5–8×**
- 端到端基因组拼接加速 **3–4×**，能效提升 **6×**

## 关键词

近存处理 · 基因组装 · NMP · 生物信息 · University of Michigan · ISCA 2025
