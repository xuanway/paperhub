---
title: "EFFACT: 全栈FHE加速平台"
description: "HPCA 2025论文解读：EFFACT是清华大学提出的全栈FHE加速平台，通过NTT硬件优化、Bootstrapping专用引擎和编译器协同，实现端到端FHE应用加速。"
tags: ["HPCA2025", "同态加密", "FHE", "全栈加速", "CKKS", "Bootstrapping", "清华大学"]
---

# EFFACT: A Highly Efficient Full-Stack FHE Acceleration Platform

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">EFFACT 从硬件到软件构建全栈 FHE 加速平台，包括专用 NTT 引擎、Bootstrapping 加速模块和 FHE 编译优化层，实现多种 FHE 工作负载的统一高效加速。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · 同态加密 · 全栈加速 · CKKS Bootstrapping · 清华大学</p>
</div>

**作者**：Yi Huang, Xinsheng Gong, Xiangyu Kong, Dibei Chen, Jianfeng Zhu, Wenping Zhu, Liangwei Li, Mingyu Gao, Aoyang Zhang, Shaojun Wei, Leibo Liu  
**机构**：Tsinghua University  
**会议**：HPCA 2025, Las Vegas, NV, USA  

---

## 一句话总结

> EFFACT 以"全栈"视角解决 FHE 加速问题：硬件层优化 NTT/ModMul，系统层优化 Bootstrapping 调度，编译层自动融合多项式操作，整体端到端加速比较 CPU 提升超过 200×。

## 背景与动机

- **FHE 的计算复杂度**：CKKS Bootstrapping 是最耗时操作，由数百次多项式 NTT 变换和模乘组成
- **碎片化方案的不足**：现有工作（F1、BTS、SHARP 等）只优化单一层次（NTT 硬件或调度），忽略跨层协同优化机会
- **全栈机会**：硬件、运行时调度和编译优化协同设计，可消除多项式操作间的冗余数据搬移

## 方法详解

### 三层协同架构

**硬件层：高效 NTT + ModMul 引擎**
- 蝶形 NTT 单元采用 radix-4 设计，比 radix-2 减少 25% 运算次数
- Residue Number System (RNS) 并行模乘，支持任意 limb 数量的 CKKS 参数

**系统层：Bootstrapping 调度优化**
- 将 CKKS Bootstrapping 分解为 CoeffToSlot/SlotToCoeff/EvalMod 三个阶段
- 动态调度 NTT 引擎，最大化各阶段的流水线并行度

**编译层：多项式操作融合**
- 识别并融合连续的 ModMul + NTT 操作，减少中间结果写回 DRAM 的次数
- 自动推导最优的 NTT 操作顺序（Lazy NTT 策略）

## 实验结果

| 工作负载 | CPU | EFFACT | 加速比 |
|---------|-----|--------|--------|
| NTT (N=2^16) | 1.1ms | 0.005ms | 220× |
| CKKS Mul (L=14) | 22ms | 0.09ms | 244× |
| CKKS Bootstrapping | 920ms | 7.8ms | 118× |
| 逻辑回归推理 | 38min | 12.6s | 180× |

## 核心亮点

1. 全栈协同：硬件、系统、编译三层联合优化，避免单层优化的局部最优
2. 支持 CKKS、BGV、BFV 三种主流方案，参数可配置
3. 相比同期最佳单层加速工作（BTS），端到端 Bootstrapping 快 3.2×

## 局限性

- 全栈设计增加了系统复杂度，对编译器的依赖较高
- Bootstrapping 精度（有效位数）与加速性能存在权衡
