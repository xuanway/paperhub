---
title: "LSQCA: 容错量子计算的Load/Store体系结构"
description: "HPCA 2025论文解读：LSQCA为有限规模容错量子计算机提出专用Load/Store体系结构，通过将逻辑量子比特的存储与计算解耦，在有限物理量子比特预算下实现更大规模的量子算法执行。"
tags: ["HPCA2025", "量子计算", "容错量子计算", "量子纠错", "体系结构", "东京大学", "NTT"]
---

# LSQCA: Resource-Efficient Load/Store Architecture for Limited-Scale Fault-Tolerant Quantum Computing

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">LSQCA 借鉴经典计算机的 Load/Store 体系结构思想，提出将逻辑量子比特分为"活跃寄存器"和"存储器"两层，通过量子态传输（Teleportation）在两层间移动量子态，使有限物理量子比特的容错量子计算机能执行远超其物理规模的量子算法。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · 容错量子计算 · 量子纠错 · Load/Store 架构 · 量子体系结构 · 东京大学 · NTT</p>
</div>

**作者**：Takumi Kobori, Yasunari Suzuki, Yosuke Ueno, Teruo Tanimoto, Synge Todo, Yuuki Tokunaga  
**机构**：University of Tokyo; NTT Computer and Data Science Laboratories; RIKEN; Kyushu University  
**会议**：HPCA 2025, Las Vegas, NV, USA  

---

## 一句话总结

> 容错量子计算机需要大量物理量子比特来纠错，当前量子计算机规模（1000～10000 物理比特）远不足以运行实用算法；LSQCA 通过"量子 Load/Store"将不活跃的逻辑量子比特压缩存储，大幅降低物理比特需求。

## 背景与动机

- **容错量子计算的规模差距**：运行 Shor 算法（破解 RSA-2048）需要约 400 万物理量子比特（表面码，距离 d=27），而当前最先进量子机只有 ~1000 物理比特
- **逻辑量子比特的稀疏性**：量子算法在任意时刻只有少数逻辑量子比特处于"活跃"计算状态，大量比特处于等待状态
- **经典 Load/Store 的启发**：经典 CPU 寄存器数量有限，通过 Load/Store 指令在内存和寄存器间移动数据；量子计算可以类比，用"量子内存"存储不活跃量子比特

## LSQCA 架构设计

### 两层量子存储层次

- **量子寄存器层**（Quantum Register File, QRF）：小规模高质量逻辑量子比特（约 50 逻辑比特），使用高距离表面码（d=15～27），支持快速门操作
- **量子内存层**（Quantum Memory, QMem）：大容量低保真度量子比特存储（约 500 逻辑比特），使用较低距离码（d=7～11），只需保存量子态，不执行计算

### 量子 Load/Store 操作

- **Q-Store（写入量子内存）**：通过量子态传输（Teleportation）将量子比特从 QRF 移动到 QMem，释放 QRF 空间
- **Q-Load（从量子内存读取）**：将所需量子比特从 QMem 传输回 QRF，恢复到可计算状态

### 编译器支持

- 量子电路编译器分析每个量子比特的活跃窗口
- 自动插入 Q-Load/Q-Store 指令，最小化 QRF 占用

## 实验结果

| 指标 | 传统架构 | LSQCA | 改进 |
|------|---------|-------|------|
| 运行 50-qubit Grover 所需物理比特 | 4.2M | 1.1M | 3.8× 减少 |
| 量子内存引入的延迟开销 | — | 8.3% | — |
| 传输保真度（Teleportation） | — | 99.95% | — |

## 核心亮点

1. 借鉴经典 Load/Store 思想，为量子计算机体系结构设计提供新维度
2. 使近期小规模容错量子计算机可执行更复杂的量子算法
3. 量子 Teleportation 的保真度损失可控，不显著影响整体算法正确性

## 局限性

- Q-Load/Store 操作的延迟（每次 Teleportation ~100μs）对实时性要求高的算法影响较大
- 需要物理层面支持高保真量子态传输，对量子互连要求高
