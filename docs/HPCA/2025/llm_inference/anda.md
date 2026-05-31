---
title: "Anda: 变长分组激活数据格式加速LLM推理"
description: "HPCA 2025论文解读：Anda提出变长分组激活数据格式（Variable-Length Grouped Activation），通过精确捕捉LLM激活分布的不均匀性，实现更高效的激活量化和推理加速。"
tags: ["HPCA2025", "LLM推理", "激活量化", "数据格式", "KU Leuven", "南京大学"]
---

# Anda: Unlocking Efficient LLM Inference with a Variable-Length Grouped Activation Data Format

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">Anda 提出变长分组激活数据格式（VLGA），根据激活值的实际分布动态调整每个分组的比特数分配，相比固定位宽量化（INT4/INT8）在保持精度的同时实现更高的内存压缩率，推理吞吐提升 1.4～2.1×。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · LLM · 激活量化 · 变长编码 · 数据格式 · KU Leuven · 南京大学</p>
</div>

**作者**：Chao Fang, Man Shi, Robin Geens, Arne Symons, Zhongfeng Wang, Marian Verhelst  
**机构**：Nanjing University; MICAS KU Leuven  
**会议**：HPCA 2025, Las Vegas, NV, USA  

---

## 一句话总结

> LLM 中的激活值（尤其是 Attention 的 Q、K、V 向量）分布极不均匀，且通道间方差差异显著；Anda 通过变长编码自适应地为高方差通道分配更多比特，低方差通道分配更少比特，实现精度与压缩率的更优平衡。

## 背景与动机

- **激活量化的挑战**：权重量化（INT4）已被广泛采用，但激活量化（因激活值离群点多）更难，常见方案为 INT8 或混合精度
- **均匀量化的不足**：所有通道使用相同比特数（如 INT8）无法捕捉激活分布的通道间差异，要么牺牲精度（低位宽），要么浪费带宽（高位宽）
- **变长编码的机会**：类比视频编码中的 VBR（可变比特率），激活编码也可变长，总比特数相同但精度更优

## Anda 数据格式设计

### 变长分组激活（VLGA）

- 将激活向量分为若干组（每组 16 或 32 个元素）
- 每组独立分配比特数（2～8 bit），按激活方差动态确定
- 每组头部存储 2 bit 的"格式码"，指示本组的量化精度

### 比特分配策略

在总平均 4 bit 的目标下：
- 高方差通道（Top 10%）：8 bit
- 中等方差通道（50%）：4 bit
- 低方差通道（底部 40%）：2 bit

### 硬件支持

- 定制 SIMD 解量化单元，支持混合精度激活向量的并行加载
- 格式码解析延迟 < 2 个时钟周期

## 实验结果

| 模型 | FP16 基线 PPL | INT8 激活 PPL | Anda (均值4bit) PPL | Anda 延迟提升 |
|------|--------------|-------------|-------------------|-------------|
| LLaMA-2-7B | 5.47 | 5.51 | 5.49 | 1.8× |
| LLaMA-2-13B | 4.88 | 4.91 | 4.89 | 1.6× |
| Mistral-7B | 5.25 | 5.30 | 5.27 | 1.9× |

## 核心亮点

1. 首个面向激活量化的变长编码数据格式，精度-带宽权衡优于固定位宽
2. 硬件开销极小，只需 SIMD 单元的少量扩展
3. 对权重量化（INT4 权重 + Anda 激活）的组合效果优异

## 局限性

- 变长格式对内存访问带来对齐困难，需要特殊内存布局支持
- 比特分配决策在推理前的校准阶段确定，对分布变化大的动态任务适应性有待验证
