---
title: "FAST: 支持可调精度与可扩展并行的FHE加速器"
description: "ISCA 2025论文解读：FAST提出支持可调位宽与可扩展并行度的FHE加速架构，通过精度自适应实现FHE不同操作的高效执行。"
tags: ["ISCA2025", "同态加密", "FHE", "可扩展并行", "NTT", "ICT CAS"]
---

# FAST: An FHE Accelerator for Scalable-parallelism with Tunable-bit

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">FAST 设计可调精度、可扩展并行的 FHE 专用加速器，针对 CKKS/BFV 不同阶段的精度需求动态调整计算单元位宽，在保证正确性的同时最大化硬件利用率。</p>
<p class="paper-seo-summary__tags">ISCA 2025 · 同态加密FHE · 可调精度 · 可扩展并行 · ICT CAS</p>
</div>

**作者**：Shengyu Fan, Xianglong Deng, Liang Kong, Guiming Shi, Guang Fan, Rui Hou, Dan Meng, Mingzhe Zhang  
**机构**：Institute of Computing Technology, Chinese Academy of Sciences (ICT CAS)  
**会议**：ISCA 2025, Tokyo, Japan  
**Session**：Session 1B: Crypto & Fully Homomorphic Encryption  

---

## 一句话总结

> FHE 不同操作需要不同精度；FAST 通过可调位宽和可扩展并行架构，统一高效地支持 CKKS/BFV 全运算流程。

## 背景与动机

- **FHE 精度异构性**：CKKS 的 Bootstrapping 等操作需要高精度（60-bit），而普通乘法可用低精度（30-bit），固定位宽浪费算力
- **并行度受限**：传统 FHE 加速器针对固定规模设计，无法随硬件规模弹性扩展
- **本文方案**：可调位宽乘法器 + 可扩展 NTT 并行引擎，支持运行时精度和并行度配置

## 主要贡献

1. **Tunable-bit 乘法器**：支持 30/60/120-bit 动态配置，低精度时并行度倍增
2. **可扩展 NTT 引擎**：蝶形单元数量可配置，单芯片到多芯片均适用
3. **任务调度器**：静态分析 FHE 计算图，自动分配各阶段最优精度和并行度
4. **完整 CKKS/BFV 支持**：涵盖加密、乘法、Bootstrapping 全流程

## 实验结果

| 操作 | vs. CPU | vs. F1加速器 |
|------|---------|-------------|
| CKKS 乘法 | >500× | 3.2× |
| Bootstrapping | >200× | 2.1× |
| BFV 同态操作 | >400× | 2.8× |

## 关键词

同态加密 · FHE · 可调精度 · NTT · CKKS · BFV · ISCA 2025
