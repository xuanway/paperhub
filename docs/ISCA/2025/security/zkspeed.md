---
title: "Need for zkSpeed: 为零知识证明加速HyperPlonk"
description: "ISCA 2025论文解读：zkSpeed针对HyperPlonk ZKP协议设计专用硬件加速器，通过多变量多项式承诺优化实现高吞吐ZKP证明生成。"
tags: ["ISCA2025", "ZKP", "零知识证明", "HyperPlonk", "硬件加速", "NYU"]
---

# Need for zkSpeed: Accelerating HyperPlonk for Zero-Knowledge Proofs

**作者**：Alhad Daftardar, Jianqiao Mo, Joey Ah-kiow, Benedikt Bünz, Ramesh Karri, Siddharth Garg, Brandon Reagen  
**机构**：New York University (NYU)  
**会议**：ISCA 2025 · Session 10C: Security  

---

## 一句话总结

> ZKP 证明生成（Prover）是区块链和隐私计算的主要算力瓶颈；zkSpeed 为 HyperPlonk 协议中的多变量多项式承诺计算设计专用加速器，实现数十倍加速。

## 背景与动机

- **ZKP 应用场景**：以太坊 zkEVM、隐私交易、可验证计算均需高效 ZKP Prover
- **HyperPlonk 优势**：相比 Groth16/PLONK，HyperPlonk 使用多变量多项式，减少电路约束数
- **Prover 瓶颈**：多变量 SumCheck 协议和多线性 PCS（多项式承诺）是主要开销

## 主要贡献

1. **SumCheck 专用引擎**：流水线并行 SumCheck 轮次计算
2. **多线性 PCS 加速**：针对 KZG/Pedersen 承诺的批量 MSM（多标量乘法）加速
3. **内存访问优化**：分析多变量求值的内存访问模式并设计专用缓存
4. **系统集成**：与完整 HyperPlonk 验证者协议集成

## 实验结果

- HyperPlonk Prover 加速 **>50×**（vs. CPU 基线）
- 能效比 GPU 高 **10×**

## 关键词

ZKP · 零知识证明 · HyperPlonk · MSM · 区块链 · NYU · ISCA 2025
