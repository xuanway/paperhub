---
title: "混合SLC-MLC RRAM混信号PIM架构：通过梯度重分布实现Transformer加速"
description: "ISCA 2025论文解读：提出结合SLC和MLC RRAM的混合混信号PIM架构，通过梯度重分布提升Transformer模型的存内计算精度和效率。"
tags: ["ISCA2025", "存内计算", "RRAM", "混信号", "Transformer", "UCSD"]
---

# Hybrid SLC-MLC RRAM Mixed-Signal Processing-in-Memory Architecture for Transformer Acceleration via Gradient Redistribution

**作者**：Chang Eun Song, Priyansh Bhatnagar, ZIHAN XIA, Nam Sung Kim, Tajana S Rosing, Mingu Kang  
**机构**：UC San Diego  
**会议**：ISCA 2025 · Session 6C: Memory Acceleration  

---

## 一句话总结

> RRAM 存内计算受限于 MLC 精度不足；本文混合 SLC（高精度）和 MLC（高密度）RRAM，通过梯度重分布优化精度-面积权衡，高效加速 Transformer。

## 主要贡献

1. **SLC-MLC 混合架构**：关键权重用 SLC 存储保证精度，其余用 MLC 节省面积
2. **梯度重分布**：训练阶段将精度敏感权重重分配到 SLC 区域
3. **混信号计算**：模拟矩阵乘法加速 Attention 操作

## 关键词

RRAM · 存内计算 · 混信号 · Transformer · 梯度重分布 · UCSD · ISCA 2025
