---
title: "Variational Quantum Algorithms in the era of Early Fault Tolerance"
description: "ISCA 2025论文解读：分析早期容错量子计算（early fault tolerance）阶段VQA算法的资源需求和优化策略。"
tags: ["ISCA2025", "量子计算", "VQA", "早期容错", "NISQ", "UChicago"]
---

# Variational Quantum Algorithms in the era of Early Fault Tolerance

**作者**：Siddharth Dangwal, Suhas Vittal, Lennart Maximilian Seifert, Fred Chong, Gokul Ravi  
**机构**：University of Chicago, GaTech  
**会议**：ISCA 2025 · Session 7C: Quantum II  

---

## 一句话总结

> 量子计算从 NISQ 过渡到全容错的早期阶段（EFT），VQA 算法如何利用有限纠错资源？本文分析并提出 EFT 时代 VQA 的最优执行策略。

## 主要贡献

1. **EFT 资源模型**：量化早期容错硬件（有限 magic state 和逻辑量子比特）对 VQA 的约束
2. **混合编译策略**：部分量子比特用纠错保护，部分使用物理量子比特，最优分配方案
3. **错误感知优化**：VQA 参数优化考虑有限纠错带来的噪声特征
4. **基准测试**：在 VQE、QAOA 等典型 VQA 上验证策略收益

## 关键词

VQA · 早期容错 · NISQ · 量子资源优化 · UChicago · ISCA 2025
