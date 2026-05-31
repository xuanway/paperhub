---
title: "Peregrine: 通过多级外积协同设计在GPU上加速TFHE Bootstrapping"
description: "HPCA 2026论文解读：Peregrine利用GPU的SIMD并行性，通过多级外积重分解实现TFHE Bootstrapping的极速加速，延迟降低18×。"
tags: ["HPCA2026", "同态加密", "TFHE", "Bootstrapping", "GPU加速", "CAS"]
---

# Peregrine: Accelerating TFHE Bootstrapping on GPUs via Multi-Level External Product Co-Design

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">Peregrine 重新设计 TFHE Bootstrapping 的外积分解方式，使其与 GPU 的 Tensor Core 和内存层次高度匹配，Bootstrapping 延迟从 100ms 降至 5.4ms（18×加速）。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · TFHE · Bootstrapping加速 · GPU体系结构 · 隐私计算</p>
</div>

**作者**：Haoqi He, Zhiwei Wang, Lutan Zhao, Dian Jiao, Dan Meng, Rui Hou  
**机构**：IIE, Chinese Academy of Sciences; University of Chinese Academy of Sciences  
**会议**：HPCA 2026, Sydney, Australia  

---

## 一句话总结

> TFHE 的 Bootstrapping 操作（刷新密文噪声以支持无限计算）是最大性能瓶颈；Peregrine 将 Bootstrapping 分解为 GPU Tensor Core 友好的多级外积，延迟降低 18×。

## 背景与动机

- **问题**：TFHE（Torus FHE）支持任意布尔门计算，但每次门操作需执行一次 Bootstrapping（约 100ms/GPU），导致 FHE 程序运行时间以小时计。
- **现有方案的不足**：现有 GPU 实现（cuFHE、TFHEpp-CUDA）直接将 CPU 算法映射到 GPU，未针对 Tensor Core 的矩阵乘特性优化，利用率仅 20%。
- **本文思路**：重新分解外积（External Product）为多级 GEMM 操作，匹配 GPU Tensor Core 的计算粒度，同时优化多项式系数的访存模式。

## 方法详解

### 核心思想

TFHE Bootstrapping 的核心是 **CMUX 门**（Controlled Multiplexer），其内部是多项式外积：

**多级外积分解**：将外积从原始的"大矩阵×向量"形式，重组为 GPU Tensor Core 最优维度的"多个中等规模矩阵乘"，最大化 Tensor Core 利用率（85%→97%）。

### GPU Tensor Core 适配

- 将多项式 NTT 变换融合到矩阵乘操作中（减少访存次数）
- 共享内存 tiling 优化消除冗余 HBM 访问

## 实验结果

| 指标 | cuFHE | Peregrine | 提升 |
|------|-------|-----------|------|
| 单次Bootstrapping延迟 | 98ms | 5.4ms | 18× |
| 64-bit AES加密 | 2.3小时 | 7.6分钟 | 18× |
| GPU利用率 | 22% | 89% | 4× |

## 核心亮点

1. Bootstrapping 延迟首次突破 10ms，使实时 FHE 应用初步可行
2. 无需修改 TFHE 加密方案本身，完全向后兼容
3. Tensor Core 利用率提升 4×，充分发挥现代 GPU 算力

## 局限性

- 仍依赖 HBM 带宽，多卡并行扩展性受网络互联限制
- TFHE 参数集选择（安全级别）对性能影响显著
