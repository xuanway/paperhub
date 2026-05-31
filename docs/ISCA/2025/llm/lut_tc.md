---
title: "LUT Tensor Core: 基于查找表的低比特LLM推理软硬件协同"
description: "ISCA 2025论文解读：LUT Tensor Core提出用查找表替代LLM量化推理中的乘法操作，并设计专用硬件单元，实现低比特LLM推理的高能效加速。"
tags: ["ISCA2025", "LLM量化", "查找表", "低比特推理", "软硬件协同", "MSRA"]
---

# LUT Tensor Core: A Software-Hardware Co-Design for LUT-Based Low-Bit LLM Inference

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">LUT Tensor Core 将量化 LLM 中的矩阵乘法替换为查找表（LUT）操作，并在 Tensor Core 层级设计 LUT 执行单元，在 W4A8/W4A4 场景下实现极高能效的 LLM 推理。</p>
<p class="paper-seo-summary__tags">ISCA 2025 · LUT推理 · 低比特量化 · Tensor Core · MSRA · Microsoft</p>
</div>

**作者**：Zhiwen Mo, Lei Wang, Jianyu Wei, Zhichen Zeng, Shijie Cao, Lingxiao Ma, Naifeng Jing, Ting Cao, Jilong Xue, Fan Yang, Mao Yang  
**机构**：Microsoft Research Asia (MSRA) 等  
**会议**：ISCA 2025, Tokyo, Japan  
**Session**：Session 4A: LLMs  

---

## 一句话总结

> W4A8 量化推理的主要开销是低比特乘法；LUT Tensor Core 预计算权重-激活乘积表，将推理从"乘加"变为"查表"，配合专用硬件单元实现 2× 以上能效提升。

## 背景与动机

- **低比特推理瓶颈**：W4A8/W4A4 量化虽减少内存，但混合精度乘法（4-bit × 8-bit）在现有 Tensor Core 上效率低
- **LUT 加速原理**：4-bit 权重组合数有限（16种），可预计算所有权重-激活乘积，查表比乘法更快
- **硬件适配**：现有 GPU Tensor Core 不原生支持 LUT 操作，需要微架构扩展

## 主要贡献

1. **LUT 推理框架**：将 GEMM 分解为权重编码 + 查表累加，支持 W4A8/W4A4 量化格式
2. **LUT Tensor Core 微架构**：在 Tensor Core 内集成小型 SRAM 查找表，加速 LUT 读取
3. **编译器支持**：自动生成 LUT 推理计划，无需手动修改 LLM 代码

## 实验结果

- W4A8 推理比标准 INT8 Tensor Core **快 1.6×**，能效提升 **1.9×**
- W4A4 推理在 Llama-2-70B 上比 FP16 快 **4.2×**，精度与 GPTQ 相当

## 关键词

LUT推理 · 低比特量化 · Tensor Core · W4A8 · MSRA · ISCA 2025
