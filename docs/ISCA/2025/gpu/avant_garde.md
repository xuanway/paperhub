---
title: "Avant-Garde: 为GPU赋能缩放数值格式"
description: "ISCA 2025论文解读：Avant-Garde为GPU引入缩放数值格式（Scaled Numeric Formats），通过格式感知的硬件支持提升低精度计算精度，减少模型精度损失。"
tags: ["ISCA2025", "GPU", "数值格式", "低精度", "量化", "EPFL", "Samsung"]
---

# Avant-Garde: Empowering GPUs with Scaled Numeric Formats

**作者**：Minseong Gil, Jungrae Kim, Geonhwa Jeong, Yongjun Park, Torsten Hoefler  
**机构**：EPFL, Yonsei University, Samsung  
**会议**：ISCA 2025 · Session 1C: GPUs & Ray Tracing  

---

## 一句话总结

> INT8/FP8 等低精度格式存在精度损失；Avant-Garde 引入缩放数值格式（如 MX 格式），在 GPU 计算单元中以少量硬件开销支持更高精度的低位宽计算。

## 主要贡献

1. **缩放格式硬件**：为 GPU CUDA Core/Tensor Core 添加向量缩放支持
2. **精度恢复**：相比纯 FP8，缩放格式在相同位宽下提升数值表示范围
3. **与现有流水线集成**：对现有 GPU 流水线改动最小化

## 关键词

GPU · 缩放数值格式 · MX格式 · 低精度计算 · EPFL · Samsung · ISCA 2025
