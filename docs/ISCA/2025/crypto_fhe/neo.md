---
title: "Neo: 基于张量核心的高效FHE加速"
description: "ISCA 2025论文解读：Neo利用GPU张量核心（Tensor Core）加速FHE中的NTT和多项式乘法运算，实现低成本高效FHE计算。"
tags: ["ISCA2025", "同态加密", "FHE", "张量核心", "NTT", "ICT CAS"]
---

# Neo: Towards Efficient Fully Homomorphic Encryption Acceleration using Tensor Core

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">Neo 将 FHE 核心操作（NTT、多项式模乘）映射到 GPU 张量核心（Tensor Core/矩阵乘单元），利用现有 GPU 硬件实现高效 FHE 加速，无需定制 ASIC。</p>
<p class="paper-seo-summary__tags">ISCA 2025 · 同态加密 · 张量核心 · GPU加速 · NTT · ICT CAS</p>
</div>

**作者**：Dian Jiao, Xianglong Deng, Zhiwei Wang, Shengyu Fan, Yi Chen, Dan Meng, Rui Hou, Mingzhe Zhang  
**机构**：Institute of Computing Technology, Chinese Academy of Sciences (ICT CAS)  
**会议**：ISCA 2025, Tokyo, Japan  
**Session**：Session 1B: Crypto & Fully Homomorphic Encryption  

---

## 一句话总结

> GPU 张量核心本为 DNN 矩阵乘设计，Neo 将 FHE 的 NTT 和多项式运算重新表达为矩阵乘形式，充分利用张量核心算力实现高效 FHE 加速。

## 背景与动机

- **FHE 计算瓶颈**：NTT（数论变换）和多项式模乘是 FHE 最耗时的操作
- **GPU 张量核心算力丰富**：现代 GPU（A100、H100）有大量 Tensor Core，但传统 FHE 实现无法充分利用
- **本文思路**：将 NTT 分解为蝶形矩阵乘形式，映射到张量核心；多项式乘法通过 NTT 域转换实现

## 主要贡献

1. **NTT→矩阵乘映射**：将 N 点 NTT 表达为多级小矩阵乘法序列，适配张量核心的 16×16 操作
2. **精度适配**：分析 FHE 精度需求，利用张量核心 INT8/FP16/BF16 格式覆盖模数运算
3. **数据布局优化**：针对张量核心访存模式设计 FHE 多项式系数的内存布局
4. **完整 CKKS 实现**：在 A100 GPU 上验证完整的 CKKS 同态运算

## 实验结果

- 比 CPU（单线程）快 **>500×**
- 比传统 GPU CUDA 实现快 **3-5×**（充分利用张量核心）
- 与专用 FHE ASIC（F1、SHARP）相当，但使用通用 GPU 硬件

## 关键词

同态加密 · 张量核心 · NTT · GPU加速 · CKKS · ICT CAS · ISCA 2025
