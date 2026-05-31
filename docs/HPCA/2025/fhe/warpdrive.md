---
title: "WarpDrive: GPU Tensor Core加速FHE"
description: "HPCA 2025论文解读：WarpDrive利用GPU Tensor Core与CUDA Core协同加速全同态加密，结合NTT与模乘的混合计算模式，实现FHE的GPU端到端加速。"
tags: ["HPCA2025", "同态加密", "FHE", "GPU", "Tensor Core", "CUDA", "Ant Group"]
---

# WarpDrive: GPU-Based Fully Homomorphic Encryption Acceleration Leveraging Tensor and CUDA Cores

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">WarpDrive 系统地将 FHE 多项式操作（NTT、模乘、密钥切换）拆分为 Tensor Core 友好的矩阵乘法子任务与 CUDA Core 处理的标量任务，充分利用 GPU 两类计算资源，相比最优 GPU 基线实现 3～5× 加速。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · FHE · GPU Tensor Core · CUDA Core · 协同计算 · Ant Group</p>
</div>

**作者**：Guang Fan, Mingzhe Zhang, Fangyu Zheng, Shengyu Fan, Tian Zhou, Xianglong Deng, Wenxu Tang, Liang Kong, Yixuan Song, Shoumeng Yan  
**机构**：Ant Group; Institute of Information Engineering, Chinese Academy of Sciences; University of Chinese Academy of Sciences  
**会议**：HPCA 2025, Las Vegas, NV, USA  

---

## 一句话总结

> 现有 GPU-FHE 实现（cuFHE、TFHE-rs GPU）只使用 CUDA Core，Tensor Core 闲置；WarpDrive 将 NTT 的蝶形运算重新表述为大规模矩阵乘，充分激活 A100/H100 的 Tensor Core 资源，整体 FHE 吞吐提升 3～5×。

## 背景与动机

- **GPU 上 FHE 的现状**：cuFHE、TFHE-rs-CUDA、CGGI-CUDA 等实现均依赖 CUDA Core（FP32/INT32 乘加），A100 Tensor Core（FP16/BF16/INT8）几乎完全闲置
- **Tensor Core 的机会**：NTT 的核心是蝶形运算（2 点 DFT），可以批量重组为矩阵乘形式，匹配 Tensor Core 的 wm×wn×wk tile 计算模式
- **混合使用的挑战**：Tensor Core 输出精度受限（FP16 尾数仅 10 位），需要结合 CUDA Core 做模数精度补偿

## 方法详解

### Tensor Core 适配 NTT

将标准 Cooley-Tukey NTT 重组为"矩阵-向量乘"形式：
- 每 $\log_2 N$ 层蝶形操作中，每层对应一个大规模矩阵乘 $\mathbf{A} \times \mathbf{v}$
- 矩阵 A 中元素为旋转因子（twiddle factors），使用 Tensor Core 的 INT8/BF16 模式

### CUDA Core 精度补偿

- Tensor Core 计算后，CUDA Core 对每个多项式系数做 mod-reduction 精度修正
- 针对每种 FHE 模数（CKKS：2^60-bit 素数），提前计算 Barrett 参数，运行时查表

### 密钥切换优化

- KeySwitch 的内积操作（$\sum_i a_i \cdot k_i$）直接表述为批量矩阵乘，完全由 Tensor Core 处理
- 共享内存 tiling 设计减少 HBM 访问次数

## 实验结果

| 基线 | 指标 | WarpDrive 加速比 |
|------|------|----------------|
| cuFHE (A100) | TFHE Bootstrapping | 5.1× |
| CGGI-CUDA | CGGI 门延迟 | 4.3× |
| HElib-GPU | CKKS Mul 吞吐 | 3.2× |
| Tensor Core 利用率 | — | 从 ~5% 提升至 72% |

## 核心亮点

1. 首次将 FHE 多项式操作系统地映射到 GPU Tensor Core
2. 混合精度方案（Tensor Core + CUDA Core）保证 FHE 数学正确性
3. 在商用 GPU（A100）上可直接运行，无需专用硬件

## 局限性

- BF16/FP16 精度限制了可支持的 FHE 参数集（最大模数位数受限）
- 对 TFHE（布尔 FHE）的适配效果好于 CKKS（浮点 FHE）
