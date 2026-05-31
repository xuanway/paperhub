---
title: "MagiCache: 虚拟片内计算引擎"
description: "ISCA 2025论文解读：MagiCache提出在LLC（最后级缓存）内构建虚拟计算引擎，利用缓存数据路径执行轻量级计算，减少CPU-内存往返。"
tags: ["ISCA2025", "Cache内计算", "近数据处理", "LLC", "内存系统"]
---

# MagiCache: A Virtual In-Cache Computing Engine

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">MagiCache 在 LLC（末级缓存）内构建虚拟计算引擎，利用缓存数据路径执行简单算术和位运算，减少将数据搬回 CPU 执行的开销，适合内存密集型工作负载。</p>
<p class="paper-seo-summary__tags">ISCA 2025 · 片内计算 · LLC · 近存处理 · 内存密集型</p>
</div>

**作者**：Renhao Fan, Yikai Cui, Weike Li, Mingyu Wang, Zhaolin Li  
**机构**：多家机构  
**会议**：ISCA 2025, Tokyo, Japan  
**Session**：Session 9C: Memory Technology  

---

## 一句话总结

> CPU 常因数据在 LLC 中而无需访问 DRAM，MagiCache 进一步在 LLC 内直接完成简单计算，消除 LLC→CPU 的多余数据往返。

## 主要贡献

1. **虚拟计算引擎**：在 LLC 标签阵列旁增加轻量 ALU，支持整数运算和位操作
2. **编译器支持**：自动识别可在 MagiCache 中执行的计算模式并生成相应指令
3. **缓存一致性**：处理 MagiCache 操作与多核缓存一致性协议的交互

## 关键词

片内计算 · LLC缓存 · 近数据处理 · ISCA 2025
