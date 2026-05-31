---
title: "Resource Analysis of Low-Overhead Transversal Architectures for Reconfigurable Atom Arrays"
description: "ISCA 2025论文解读：分析可重构原子阵列平台上横向（transversal）量子门架构的资源开销，揭示其相对于表面码的优势。"
tags: ["ISCA2025", "量子计算", "原子阵列", "横向门", "容错", "Harvard"]
---

# Resource Analysis of Low-Overhead Transversal Architectures for Reconfigurable Atom Arrays

**作者**：Hengyun Zhou, Casey Duckering, Chen Zhao, Dolev Bluvstein, Madelyn Cain, Aleksander Kubica, Sheng-Tao Wang, Mikhail D. Lukin  
**机构**：Harvard University, QuEra Computing  
**会议**：ISCA 2025 · Session 7C: Quantum II  

---

## 一句话总结

> 可重构原子阵列支持横向逻辑门，其容错开销远低于表面码+T注入方案；本文系统量化这一优势并给出未来量子计算机设计启示。

## 主要贡献

1. **横向门资源分析**：在可重构原子阵列（如 QuEra Aquila）上量化实现 Clifford+T 通用门集的开销
2. **与表面码对比**：证明横向方案在特定电路类型上 qubit 开销减少 5–10×
3. **容错阈值分析**：估计横向架构的错误阈值和逻辑错误率

## 关键词

原子阵列 · 横向门 · 容错量子计算 · Harvard · QuEra · ISCA 2025
