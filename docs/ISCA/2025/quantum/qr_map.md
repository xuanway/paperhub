---
title: "QR-Map: 基于地图的量子电路抽象与量子比特复用优化"
description: "ISCA 2025论文解读：QR-Map提出地图抽象方法将量子电路分析转化为图映射问题，实现高效的量子比特复用优化。"
tags: ["ISCA2025", "量子计算", "量子比特复用", "电路优化", "POSTECH"]
---

# QR-Map: A Map-Based Approach to Quantum Circuit Abstraction for Qubit Reuse Optimization

**作者**：Hyungseok Kim, Enhyeok Jang, Seungwoo Choi, Youngmin Kim, Won Woo Ro  
**机构**：POSTECH  
**会议**：ISCA 2025 · Session 8B: Quantum III  

---

## 一句话总结

> 量子电路中可复用的量子比特（已测量且不再使用）能减少所需物理量子比特数；QR-Map 将复用机会识别转化为图映射问题，高效寻找最优复用策略。

## 主要贡献

1. **地图抽象**：将量子电路的量子比特生命周期表达为二维地图
2. **图匹配算法**：在地图上搜索量子比特复用机会，减少所需量子比特数
3. **编译集成**：与 Qiskit、Cirq 编译流程集成

## 关键词

量子比特复用 · 量子电路优化 · 编译优化 · POSTECH · ISCA 2025
