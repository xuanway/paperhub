---
title: "Genesis: 混合CV-DV量子计算机的Hamiltonian模拟编译器"
description: "ISCA 2025论文解读：Genesis专为混合连续变量(CV)和离散变量(DV)量子硬件设计Hamiltonian模拟编译器，充分利用两种量子模态的互补优势。"
tags: ["ISCA2025", "量子计算", "Hamiltonian模拟", "CV-DV量子", "量子编译器", "NCSU"]
---

# Genesis: A Compiler for Hamiltonian Simulation on Hybrid CV-DV Quantum Computers

**作者**：Zihan Chen, Jiakang Li, Minghao Guo, Henry Chen, Zirui Li, Joel Bierman, Yipeng Huang, Huiyang Zhou, Yuan Liu, Eddy Z. Zhang  
**机构**：NC State University (NCSU)  
**会议**：ISCA 2025 · Session 8B: Quantum III  

---

## 一句话总结

> CV（连续变量，如玻色子模式）和 DV（离散变量，如量子比特）量子计算模式各有所长；Genesis 编译器自动分配 Hamiltonian 模拟任务到最适合的模态。

## 主要贡献

1. **混合 CV-DV 编译框架**：将 Hamiltonian 模拟分解为 CV 适合的玻色子操作和 DV 量子门
2. **任务分配优化**：最优化分配各项模拟步骤到 CV 或 DV 模式
3. **资源节省**：与纯 DV 方案相比，量子比特需求减少 30–50%

## 关键词

Hamiltonian模拟 · CV-DV混合量子 · 量子编译器 · 玻色子模式 · NCSU · ISCA 2025
