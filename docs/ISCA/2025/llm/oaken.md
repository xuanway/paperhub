---
title: "Oaken: 在线/离线混合KV Cache量化的高效LLM服务"
description: "ISCA 2025论文解读：Oaken提出在线/离线混合KV Cache量化方案，针对长上下文LLM服务场景大幅降低内存占用并提升吞吐量。"
tags: ["ISCA2025", "LLM服务", "KV Cache", "量化", "POSTECH", "Samsung"]
---

# Oaken: Fast and Efficient LLM Serving with Online-Offline Hybrid KV Cache Quantization

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">Oaken 结合离线统计的通道量化参数和在线动态异常值检测，将 KV Cache 压缩至 4-bit，在保持精度的同时大幅减少 GPU 内存占用并提升 LLM 服务吞吐量。</p>
<p class="paper-seo-summary__tags">ISCA 2025 · KV Cache量化 · LLM服务 · POSTECH · Samsung Research</p>
</div>

**作者**：Minsu Kim, Seongmin Hong, RyeoWook Ko, Soongyu Choi, Hunjong Lee, Junsoo Kim, Joo-Young Kim, Jongse Park  
**机构**：POSTECH, Samsung Research  
**会议**：ISCA 2025, Tokyo, Japan  
**Session**：Session 4A: LLMs  

---

## 一句话总结

> KV Cache 是 LLM 长上下文服务的内存瓶颈；Oaken 通过离线校准 + 在线异常值感知量化，将 KV Cache 压缩至 4-bit，实现高精度低内存的 LLM 服务。

## 背景与动机

- **KV Cache 内存压力**：长上下文（128K+ tokens）下 KV Cache 占据主要 GPU 内存，严重限制并发用户数
- **量化难点**：KV Cache 存在通道异常值（outlier），直接低比特量化导致严重精度损失
- **混合策略**：离线分析通道统计特性，在线处理动态异常值，两者结合平衡精度与效率

## 主要贡献

1. **混合量化方案**：离线统计各 layer 的 Key/Value 通道缩放因子，在线检测并单独处理异常值
2. **量化感知服务系统**：与 PagedAttention、连续批处理集成，量化/反量化开销最小化
3. **硬件友好设计**：量化参数存储格式对 GPU Tensor Core 友好，反量化融入 Attention 计算

## 实验结果

| 模型 | 内存节省 | 吞吐量提升 | 精度损失 |
|------|---------|-----------|---------|
| Llama-2-7B (128K) | 3.2× | 2.1× | <0.5% |
| Llama-2-70B (64K) | 3.0× | 1.8× | <0.5% |

## 关键词

KV Cache · 量化 · LLM服务 · 长上下文 · POSTECH · ISCA 2025
