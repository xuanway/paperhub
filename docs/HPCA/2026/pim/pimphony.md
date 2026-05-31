---
title: "PIMphony: 突破基于PIM的长文本LLM推理带宽与容量瓶颈"
description: "HPCA 2026论文解读：PIMphony通过协同优化PIM带宽分配和KV Cache管理，解决长文本LLM推理中的带宽瓶颈，吞吐量提升3.2×。"
tags: ["HPCA2026", "存内计算", "PIM", "LLM推理", "长文本", "SK hynix"]
---

# PIMphony: Overcoming Bandwidth and Capacity Inefficiency in PIM-based Long-Context LLM Inference

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">PIMphony 通过PIM内部带宽重配置与分级KV Cache管理，解决长文本LLM推理中PIM利用率低和容量瓶颈问题，端到端吞吐量提升3.2×。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · PIM · 长文本LLM · 带宽优化 · SK hynix合作</p>
</div>

**作者**：hyucksung kwon, Kyungmo Koo, Janghyeon Kim, Woongkyu Lee, Minjae Lee, ... (SK hynix团队)  
**机构**：Hanyang University, SK hynix  
**会议**：HPCA 2026, Sydney, Australia  

---

## 一句话总结

> 长文本 LLM 推理对内存带宽的需求极高，PIM 架构虽能缓解带宽压力，但内部带宽分配不均和容量不足导致利用率低下；PIMphony 通过动态带宽重配置和分级存储，使 PIM 真正发挥作用。

## 背景与动机

- **问题**：长文本推理（32K+ tokens）的 KV Cache 体积巨大，GPU HBM 容量不足；PIM（如 HBM-PIM）理论上可提供更高带宽，但 decode 阶段的不规则访问导致 PIM 利用率仅 30-40%。
- **现有方案的不足**：直接将 KV Cache 卸载到 CPU DRAM 带宽太低；固定 PIM 带宽分配无法适应注意力计算的非均匀访问模式。
- **本文思路**：分析 LLM Decode 阶段各注意力头的访问模式，动态重新分配 PIM Bank 带宽，同时实现分级 KV Cache（PIM 热层 + DRAM 冷层）。

## 方法详解

### 核心思想

1. **动态带宽重配置**：根据各注意力头的 KV Cache 访问热度，动态调整 PIM Bank 分配
2. **分级 KV Cache 管理**：频繁访问的 token（近期 + 高注意力分数）留在 PIM，其余移至 DRAM
3. **预取流水线**：在当前层计算时预取下一层所需 KV Cache

## 实验结果

| 文本长度 | vs. GPU-only | vs. 静态PIM |
|---------|-------------|------------|
| 8K tokens | 2.1× | 1.4× |
| 32K tokens | 3.2× | 2.0× |
| 128K tokens | 4.8× | 2.9× |

## 核心亮点

1. 长文本场景收益随文本长度显著增加，正是 PIM 最有价值的场景
2. 与 SK hynix HBM-PIM 硬件实现深度协同优化
3. 支持 GQA（Grouped Query Attention）等现代 LLM 变体

## 局限性

- 依赖 PIM 硬件（HBM-PIM 等），需要特定内存产品支持
- 分级管理的迁移开销在极短序列时可能超过收益
